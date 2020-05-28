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
    
    Exceptions
    
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
    :param UserPoolId: [REQUIRED]\nThe user pool ID for the user pool where you want to add custom attributes.\n

    :type CustomAttributes: list
    :param CustomAttributes: [REQUIRED]\nAn array of custom attributes, such as Mutable and Name.\n\n(dict) --Contains information about the schema attribute.\n\nName (string) --A schema attribute of the name type.\n\nAttributeDataType (string) --The attribute data type.\n\nDeveloperOnlyAttribute (boolean) --\nNote\nWe recommend that you use WriteAttributes in the user pool client to control how attributes can be mutated for new use cases instead of using DeveloperOnlyAttribute .\n\nSpecifies whether the attribute type is developer only. This attribute can only be modified by an administrator. Users will not be able to modify this attribute using their access token. For example, DeveloperOnlyAttribute can be modified using the API but cannot be updated using the API.\n\nMutable (boolean) --Specifies whether the value of the attribute can be changed.\nFor any user pool attribute that\'s mapped to an identity provider attribute, you must set this parameter to true . Amazon Cognito updates mapped attributes when users sign in to your application through an identity provider. If an attribute is immutable, Amazon Cognito throws an error when it attempts to update the attribute. For more information, see Specifying Identity Provider Attribute Mappings for Your User Pool .\n\nRequired (boolean) --Specifies whether a user pool attribute is required. If the attribute is required and the user does not provide a value, registration or sign-in will fail.\n\nNumberAttributeConstraints (dict) --Specifies the constraints for an attribute of the number type.\n\nMinValue (string) --The minimum value of an attribute that is of the number data type.\n\nMaxValue (string) --The maximum value of an attribute that is of the number data type.\n\n\n\nStringAttributeConstraints (dict) --Specifies the constraints for an attribute of the string type.\n\nMinLength (string) --The minimum length.\n\nMaxLength (string) --The maximum length.\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
Represents the response from the server for the request to add custom attributes.





Exceptions

CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.UserImportInProgressException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


    :return: {}
    
    
    :returns: 
    CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
    CognitoIdentityProvider.Client.exceptions.InvalidParameterException
    CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
    CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
    CognitoIdentityProvider.Client.exceptions.UserImportInProgressException
    CognitoIdentityProvider.Client.exceptions.InternalErrorException
    
    """
    pass

def admin_add_user_to_group(UserPoolId=None, Username=None, GroupName=None):
    """
    Adds the specified user to the specified group.
    Calling this action requires developer credentials.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.admin_add_user_to_group(
        UserPoolId='string',
        Username='string',
        GroupName='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID for the user pool.\n

    :type Username: string
    :param Username: [REQUIRED]\nThe username for the user.\n

    :type GroupName: string
    :param GroupName: [REQUIRED]\nThe group name.\n

    :returns: 
    CognitoIdentityProvider.Client.exceptions.InvalidParameterException
    CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
    CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
    CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
    CognitoIdentityProvider.Client.exceptions.UserNotFoundException
    CognitoIdentityProvider.Client.exceptions.InternalErrorException
    
    """
    pass

def admin_confirm_sign_up(UserPoolId=None, Username=None, ClientMetadata=None):
    """
    Confirms user registration as an admin without using a confirmation code. Works on any user.
    Calling this action requires developer credentials.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.admin_confirm_sign_up(
        UserPoolId='string',
        Username='string',
        ClientMetadata={
            'string': 'string'
        }
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID for which you want to confirm user registration.\n

    :type Username: string
    :param Username: [REQUIRED]\nThe user name for which you want to confirm user registration.\n

    :type ClientMetadata: dict
    :param ClientMetadata: A map of custom key-value pairs that you can provide as input for any custom workflows that this action triggers.\nIf your user pool configuration includes triggers, the AdminConfirmSignUp API action invokes the AWS Lambda function that is specified for the post confirmation trigger. When Amazon Cognito invokes this function, it passes a JSON payload, which the function receives as input. In this payload, the clientMetadata attribute provides the data that you assigned to the ClientMetadata parameter in your AdminConfirmSignUp request. In your function code in AWS Lambda, you can process the ClientMetadata value to enhance your workflow for your specific needs.\nFor more information, see Customizing User Pool Workflows with Lambda Triggers in the Amazon Cognito Developer Guide .\n\nNote\nTake the following limitations into consideration when you use the ClientMetadata parameter:\n\nAmazon Cognito does not store the ClientMetadata value. This data is available only to AWS Lambda triggers that are assigned to a user pool to support custom workflows. If your user pool configuration does not include triggers, the ClientMetadata parameter serves no purpose.\nAmazon Cognito does not validate the ClientMetadata value.\nAmazon Cognito does not encrypt the the ClientMetadata value, so don\'t use it to provide sensitive information.\n\n\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
Represents the response from the server for the request to confirm registration.





Exceptions

CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.UnexpectedLambdaException
CognitoIdentityProvider.Client.exceptions.UserLambdaValidationException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.TooManyFailedAttemptsException
CognitoIdentityProvider.Client.exceptions.InvalidLambdaResponseException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.LimitExceededException
CognitoIdentityProvider.Client.exceptions.UserNotFoundException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


    :return: {}
    
    
    :returns: 
    CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
    CognitoIdentityProvider.Client.exceptions.InvalidParameterException
    CognitoIdentityProvider.Client.exceptions.UnexpectedLambdaException
    CognitoIdentityProvider.Client.exceptions.UserLambdaValidationException
    CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
    CognitoIdentityProvider.Client.exceptions.TooManyFailedAttemptsException
    CognitoIdentityProvider.Client.exceptions.InvalidLambdaResponseException
    CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
    CognitoIdentityProvider.Client.exceptions.LimitExceededException
    CognitoIdentityProvider.Client.exceptions.UserNotFoundException
    CognitoIdentityProvider.Client.exceptions.InternalErrorException
    
    """
    pass

def admin_create_user(UserPoolId=None, Username=None, UserAttributes=None, ValidationData=None, TemporaryPassword=None, ForceAliasCreation=None, MessageAction=None, DesiredDeliveryMediums=None, ClientMetadata=None):
    """
    Creates a new user in the specified user pool.
    If MessageAction is not set, the default is to send a welcome message via email or phone (SMS).
    Alternatively, you can call AdminCreateUser with \xe2\x80\x9cSUPPRESS\xe2\x80\x9d for the MessageAction parameter, and Amazon Cognito will not send any email.
    In either case, the user will be in the FORCE_CHANGE_PASSWORD state until they sign in and change their password.
    AdminCreateUser requires developer credentials.
    See also: AWS API Documentation
    
    Exceptions
    
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
        ],
        ClientMetadata={
            'string': 'string'
        }
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID for the user pool where the user will be created.\n

    :type Username: string
    :param Username: [REQUIRED]\nThe username for the user. Must be unique within the user pool. Must be a UTF-8 string between 1 and 128 characters. After the user is created, the username cannot be changed.\n

    :type UserAttributes: list
    :param UserAttributes: An array of name-value pairs that contain user attributes and attribute values to be set for the user to be created. You can create a user without specifying any attributes other than Username . However, any attributes that you specify as required (in or in the Attributes tab of the console) must be supplied either by you (in your call to AdminCreateUser ) or by the user (when he or she signs up in response to your welcome message).\nFor custom attributes, you must prepend the custom: prefix to the attribute name.\nTo send a message inviting the user to sign up, you must specify the user\'s email address or phone number. This can be done in your call to AdminCreateUser or in the Users tab of the Amazon Cognito console for managing your user pools.\nIn your call to AdminCreateUser , you can set the email_verified attribute to True , and you can set the phone_number_verified attribute to True . (You can also do this by calling .)\n\nemail : The email address of the user to whom the message that contains the code and username will be sent. Required if the email_verified attribute is set to True , or if 'EMAIL' is specified in the DesiredDeliveryMediums parameter.\nphone_number : The phone number of the user to whom the message that contains the code and username will be sent. Required if the phone_number_verified attribute is set to True , or if 'SMS' is specified in the DesiredDeliveryMediums parameter.\n\n\n(dict) --Specifies whether the attribute is standard or custom.\n\nName (string) -- [REQUIRED]The name of the attribute.\n\nValue (string) --The value of the attribute.\n\n\n\n\n

    :type ValidationData: list
    :param ValidationData: The user\'s validation data. This is an array of name-value pairs that contain user attributes and attribute values that you can use for custom validation, such as restricting the types of user accounts that can be registered. For example, you might choose to allow or disallow user sign-up based on the user\'s domain.\nTo configure custom validation, you must create a Pre Sign-up Lambda trigger for the user pool as described in the Amazon Cognito Developer Guide. The Lambda trigger receives the validation data and uses it in the validation process.\nThe user\'s validation data is not persisted.\n\n(dict) --Specifies whether the attribute is standard or custom.\n\nName (string) -- [REQUIRED]The name of the attribute.\n\nValue (string) --The value of the attribute.\n\n\n\n\n

    :type TemporaryPassword: string
    :param TemporaryPassword: The user\'s temporary password. This password must conform to the password policy that you specified when you created the user pool.\nThe temporary password is valid only once. To complete the Admin Create User flow, the user must enter the temporary password in the sign-in page along with a new password to be used in all future sign-ins.\nThis parameter is not required. If you do not specify a value, Amazon Cognito generates one for you.\nThe temporary password can only be used until the user account expiration limit that you specified when you created the user pool. To reset the account after that time limit, you must call AdminCreateUser again, specifying 'RESEND' for the MessageAction parameter.\n

    :type ForceAliasCreation: boolean
    :param ForceAliasCreation: This parameter is only used if the phone_number_verified or email_verified attribute is set to True . Otherwise, it is ignored.\nIf this parameter is set to True and the phone number or email address specified in the UserAttributes parameter already exists as an alias with a different user, the API call will migrate the alias from the previous user to the newly created user. The previous user will no longer be able to log in using that alias.\nIf this parameter is set to False , the API throws an AliasExistsException error if the alias already exists. The default value is False .\n

    :type MessageAction: string
    :param MessageAction: Set to 'RESEND' to resend the invitation message to a user that already exists and reset the expiration limit on the user\'s account. Set to 'SUPPRESS' to suppress sending the message. Only one value can be specified.

    :type DesiredDeliveryMediums: list
    :param DesiredDeliveryMediums: Specify 'EMAIL' if email will be used to send the welcome message. Specify 'SMS' if the phone number will be used. The default value is 'SMS' . More than one value can be specified.\n\n(string) --\n\n

    :type ClientMetadata: dict
    :param ClientMetadata: A map of custom key-value pairs that you can provide as input for any custom workflows that this action triggers.\nYou create custom workflows by assigning AWS Lambda functions to user pool triggers. When you use the AdminCreateUser API action, Amazon Cognito invokes the function that is assigned to the pre sign-up trigger. When Amazon Cognito invokes this function, it passes a JSON payload, which the function receives as input. This payload contains a clientMetadata attribute, which provides the data that you assigned to the ClientMetadata parameter in your AdminCreateUser request. In your function code in AWS Lambda, you can process the clientMetadata value to enhance your workflow for your specific needs.\nFor more information, see Customizing User Pool Workflows with Lambda Triggers in the Amazon Cognito Developer Guide .\n\nNote\nTake the following limitations into consideration when you use the ClientMetadata parameter:\n\nAmazon Cognito does not store the ClientMetadata value. This data is available only to AWS Lambda triggers that are assigned to a user pool to support custom workflows. If your user pool configuration does not include triggers, the ClientMetadata parameter serves no purpose.\nAmazon Cognito does not validate the ClientMetadata value.\nAmazon Cognito does not encrypt the the ClientMetadata value, so don\'t use it to provide sensitive information.\n\n\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --
Represents the response from the server to the request to create the user.

User (dict) --
The newly created user.

Username (string) --
The user name of the user you wish to describe.

Attributes (list) --
A container with information about the user type attributes.

(dict) --
Specifies whether the attribute is standard or custom.

Name (string) --
The name of the attribute.

Value (string) --
The value of the attribute.





UserCreateDate (datetime) --
The creation date of the user.

UserLastModifiedDate (datetime) --
The last modified date of the user.

Enabled (boolean) --
Specifies whether the user is enabled.

UserStatus (string) --
The user status. Can be one of the following:

UNCONFIRMED - User has been created but not confirmed.
CONFIRMED - User has been confirmed.
ARCHIVED - User is no longer active.
COMPROMISED - User is disabled due to a potential security threat.
UNKNOWN - User status is not known.
RESET_REQUIRED - User is confirmed, but the user must request a code and reset his or her password before he or she can sign in.
FORCE_CHANGE_PASSWORD - The user is confirmed and the user can sign in using a temporary password, but on first sign-in, the user must change his or her password to a new value before doing anything else.


MFAOptions (list) --
The MFA options for the user.

(dict) --

This data type is no longer supported. You can use it only for SMS MFA configurations. You can\'t use it for TOTP software token MFA configurations.

To set either type of MFA configuration, use the  AdminSetUserMFAPreference or  SetUserMFAPreference actions.
To look up information about either type of MFA configuration, use the  AdminGetUserResponse$UserMFASettingList or  GetUserResponse$UserMFASettingList responses.

DeliveryMedium (string) --
The delivery medium to send the MFA code. You can use this parameter to set only the SMS delivery medium value.

AttributeName (string) --
The attribute name of the MFA option type. The only valid value is phone_number .













Exceptions

CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.UserNotFoundException
CognitoIdentityProvider.Client.exceptions.UsernameExistsException
CognitoIdentityProvider.Client.exceptions.InvalidPasswordException
CognitoIdentityProvider.Client.exceptions.CodeDeliveryFailureException
CognitoIdentityProvider.Client.exceptions.UnexpectedLambdaException
CognitoIdentityProvider.Client.exceptions.UserLambdaValidationException
CognitoIdentityProvider.Client.exceptions.InvalidLambdaResponseException
CognitoIdentityProvider.Client.exceptions.PreconditionNotMetException
CognitoIdentityProvider.Client.exceptions.InvalidSmsRoleAccessPolicyException
CognitoIdentityProvider.Client.exceptions.InvalidSmsRoleTrustRelationshipException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.UnsupportedUserStateException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


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
    RESET_REQUIRED - User is confirmed, but the user must request a code and reset his or her password before he or she can sign in.
    FORCE_CHANGE_PASSWORD - The user is confirmed and the user can sign in using a temporary password, but on first sign-in, the user must change his or her password to a new value before doing anything else.
    
    """
    pass

def admin_delete_user(UserPoolId=None, Username=None):
    """
    Deletes a user as an administrator. Works on any user.
    Calling this action requires developer credentials.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.admin_delete_user(
        UserPoolId='string',
        Username='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID for the user pool where you want to delete the user.\n

    :type Username: string
    :param Username: [REQUIRED]\nThe user name of the user you wish to delete.\n

    :returns: 
    CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
    CognitoIdentityProvider.Client.exceptions.InvalidParameterException
    CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
    CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
    CognitoIdentityProvider.Client.exceptions.UserNotFoundException
    CognitoIdentityProvider.Client.exceptions.InternalErrorException
    
    """
    pass

def admin_delete_user_attributes(UserPoolId=None, Username=None, UserAttributeNames=None):
    """
    Deletes the user attributes in a user pool as an administrator. Works on any user.
    Calling this action requires developer credentials.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.admin_delete_user_attributes(
        UserPoolId='string',
        Username='string',
        UserAttributeNames=[
            'string',
        ]
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID for the user pool where you want to delete user attributes.\n

    :type Username: string
    :param Username: [REQUIRED]\nThe user name of the user from which you would like to delete attributes.\n

    :type UserAttributeNames: list
    :param UserAttributeNames: [REQUIRED]\nAn array of strings representing the user attribute names you wish to delete.\nFor custom attributes, you must prepend the custom: prefix to the attribute name.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
Represents the response received from the server for a request to delete user attributes.





Exceptions

CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.UserNotFoundException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


    :return: {}
    
    
    :returns: 
    CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
    CognitoIdentityProvider.Client.exceptions.InvalidParameterException
    CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
    CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
    CognitoIdentityProvider.Client.exceptions.UserNotFoundException
    CognitoIdentityProvider.Client.exceptions.InternalErrorException
    
    """
    pass

def admin_disable_provider_for_user(UserPoolId=None, User=None):
    """
    Disables the user from signing in with the specified external (SAML or social) identity provider. If the user to disable is a Cognito User Pools native username + password user, they are not permitted to use their password to sign-in. If the user to disable is a linked external IdP user, any link between that user and an existing user is removed. The next time the external user (no longer attached to the previously linked DestinationUser ) signs in, they must create a new user account. See .
    This action is enabled only for admin access and requires developer credentials.
    The ProviderName must match the value specified when creating an IdP for the pool.
    To disable a native username + password user, the ProviderName value must be Cognito and the ProviderAttributeName must be Cognito_Subject , with the ProviderAttributeValue being the name that is used in the user pool for the user.
    The ProviderAttributeName must always be Cognito_Subject for social identity providers. The ProviderAttributeValue must always be the exact subject that was used when the user was originally linked as a source user.
    For de-linking a SAML identity, there are two scenarios. If the linked identity has not yet been used to sign-in, the ProviderAttributeName and ProviderAttributeValue must be the same values that were used for the SourceUser when the identities were originally linked in the call. (If the linking was done with ProviderAttributeName set to Cognito_Subject , the same applies here). However, if the user has already signed in, the ProviderAttributeName must be Cognito_Subject and ProviderAttributeValue must be the subject of the SAML assertion.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.admin_disable_provider_for_user(
        UserPoolId='string',
        User={
            'ProviderName': 'string',
            'ProviderAttributeName': 'string',
            'ProviderAttributeValue': 'string'
        }
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID for the user pool.\n

    :type User: dict
    :param User: [REQUIRED]\nThe user to be disabled.\n\nProviderName (string) --The name of the provider, for example, Facebook, Google, or Login with Amazon.\n\nProviderAttributeName (string) --The name of the provider attribute to link to, for example, NameID .\n\nProviderAttributeValue (string) --The value of the provider attribute to link to, for example, xxxxx_account .\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.UserNotFoundException
CognitoIdentityProvider.Client.exceptions.AliasExistsException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def admin_disable_user(UserPoolId=None, Username=None):
    """
    Disables the specified user.
    Calling this action requires developer credentials.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.admin_disable_user(
        UserPoolId='string',
        Username='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID for the user pool where you want to disable the user.\n

    :type Username: string
    :param Username: [REQUIRED]\nThe user name of the user you wish to disable.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
Represents the response received from the server to disable the user as an administrator.





Exceptions

CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.UserNotFoundException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


    :return: {}
    
    
    :returns: 
    CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
    CognitoIdentityProvider.Client.exceptions.InvalidParameterException
    CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
    CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
    CognitoIdentityProvider.Client.exceptions.UserNotFoundException
    CognitoIdentityProvider.Client.exceptions.InternalErrorException
    
    """
    pass

def admin_enable_user(UserPoolId=None, Username=None):
    """
    Enables the specified user as an administrator. Works on any user.
    Calling this action requires developer credentials.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.admin_enable_user(
        UserPoolId='string',
        Username='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID for the user pool where you want to enable the user.\n

    :type Username: string
    :param Username: [REQUIRED]\nThe user name of the user you wish to enable.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
Represents the response from the server for the request to enable a user as an administrator.





Exceptions

CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.UserNotFoundException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


    :return: {}
    
    
    :returns: 
    CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
    CognitoIdentityProvider.Client.exceptions.InvalidParameterException
    CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
    CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
    CognitoIdentityProvider.Client.exceptions.UserNotFoundException
    CognitoIdentityProvider.Client.exceptions.InternalErrorException
    
    """
    pass

def admin_forget_device(UserPoolId=None, Username=None, DeviceKey=None):
    """
    Forgets the device, as an administrator.
    Calling this action requires developer credentials.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.admin_forget_device(
        UserPoolId='string',
        Username='string',
        DeviceKey='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID.\n

    :type Username: string
    :param Username: [REQUIRED]\nThe user name.\n

    :type DeviceKey: string
    :param DeviceKey: [REQUIRED]\nThe device key.\n

    :returns: 
    CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
    CognitoIdentityProvider.Client.exceptions.InvalidParameterException
    CognitoIdentityProvider.Client.exceptions.InvalidUserPoolConfigurationException
    CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
    CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
    CognitoIdentityProvider.Client.exceptions.UserNotFoundException
    CognitoIdentityProvider.Client.exceptions.InternalErrorException
    
    """
    pass

def admin_get_device(DeviceKey=None, UserPoolId=None, Username=None):
    """
    Gets the device, as an administrator.
    Calling this action requires developer credentials.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.admin_get_device(
        DeviceKey='string',
        UserPoolId='string',
        Username='string'
    )
    
    
    :type DeviceKey: string
    :param DeviceKey: [REQUIRED]\nThe device key.\n

    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID.\n

    :type Username: string
    :param Username: [REQUIRED]\nThe user name.\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --
Gets the device response, as an administrator.

Device (dict) --
The device.

DeviceKey (string) --
The device key.

DeviceAttributes (list) --
The device attributes.

(dict) --
Specifies whether the attribute is standard or custom.

Name (string) --
The name of the attribute.

Value (string) --
The value of the attribute.





DeviceCreateDate (datetime) --
The creation date of the device.

DeviceLastModifiedDate (datetime) --
The last modified date of the device.

DeviceLastAuthenticatedDate (datetime) --
The date in which the device was last authenticated.









Exceptions

CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.InvalidUserPoolConfigurationException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.InternalErrorException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException


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
    
    
    :returns: 
    CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
    CognitoIdentityProvider.Client.exceptions.InvalidParameterException
    CognitoIdentityProvider.Client.exceptions.InvalidUserPoolConfigurationException
    CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
    CognitoIdentityProvider.Client.exceptions.InternalErrorException
    CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
    
    """
    pass

def admin_get_user(UserPoolId=None, Username=None):
    """
    Gets the specified user by user name in a user pool as an administrator. Works on any user.
    Calling this action requires developer credentials.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.admin_get_user(
        UserPoolId='string',
        Username='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID for the user pool where you want to get information about the user.\n

    :type Username: string
    :param Username: [REQUIRED]\nThe user name of the user you wish to retrieve.\n

    :rtype: dict

ReturnsResponse Syntax
{
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
    ],
    'PreferredMfaSetting': 'string',
    'UserMFASettingList': [
        'string',
    ]
}


Response Structure

(dict) --
Represents the response from the server from the request to get the specified user as an administrator.

Username (string) --
The user name of the user about whom you are receiving information.

UserAttributes (list) --
An array of name-value pairs representing user attributes.

(dict) --
Specifies whether the attribute is standard or custom.

Name (string) --
The name of the attribute.

Value (string) --
The value of the attribute.





UserCreateDate (datetime) --
The date the user was created.

UserLastModifiedDate (datetime) --
The date the user was last modified.

Enabled (boolean) --
Indicates that the status is enabled.

UserStatus (string) --
The user status. Can be one of the following:

UNCONFIRMED - User has been created but not confirmed.
CONFIRMED - User has been confirmed.
ARCHIVED - User is no longer active.
COMPROMISED - User is disabled due to a potential security threat.
UNKNOWN - User status is not known.
RESET_REQUIRED - User is confirmed, but the user must request a code and reset his or her password before he or she can sign in.
FORCE_CHANGE_PASSWORD - The user is confirmed and the user can sign in using a temporary password, but on first sign-in, the user must change his or her password to a new value before doing anything else.


MFAOptions (list) --

This response parameter is no longer supported. It provides information only about SMS MFA configurations. It doesn\'t provide information about TOTP software token MFA configurations. To look up information about either type of MFA configuration, use the  AdminGetUserResponse$UserMFASettingList response instead.


(dict) --

This data type is no longer supported. You can use it only for SMS MFA configurations. You can\'t use it for TOTP software token MFA configurations.

To set either type of MFA configuration, use the  AdminSetUserMFAPreference or  SetUserMFAPreference actions.
To look up information about either type of MFA configuration, use the  AdminGetUserResponse$UserMFASettingList or  GetUserResponse$UserMFASettingList responses.

DeliveryMedium (string) --
The delivery medium to send the MFA code. You can use this parameter to set only the SMS delivery medium value.

AttributeName (string) --
The attribute name of the MFA option type. The only valid value is phone_number .





PreferredMfaSetting (string) --
The user\'s preferred MFA setting.

UserMFASettingList (list) --
The MFA options that are enabled for the user. The possible values in this list are SMS_MFA and SOFTWARE_TOKEN_MFA .

(string) --








Exceptions

CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.UserNotFoundException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


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
        ],
        'PreferredMfaSetting': 'string',
        'UserMFASettingList': [
            'string',
        ]
    }
    
    
    :returns: 
    UNCONFIRMED - User has been created but not confirmed.
    CONFIRMED - User has been confirmed.
    ARCHIVED - User is no longer active.
    COMPROMISED - User is disabled due to a potential security threat.
    UNKNOWN - User status is not known.
    RESET_REQUIRED - User is confirmed, but the user must request a code and reset his or her password before he or she can sign in.
    FORCE_CHANGE_PASSWORD - The user is confirmed and the user can sign in using a temporary password, but on first sign-in, the user must change his or her password to a new value before doing anything else.
    
    """
    pass

def admin_initiate_auth(UserPoolId=None, ClientId=None, AuthFlow=None, AuthParameters=None, ClientMetadata=None, AnalyticsMetadata=None, ContextData=None):
    """
    Initiates the authentication flow, as an administrator.
    Calling this action requires developer credentials.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.admin_initiate_auth(
        UserPoolId='string',
        ClientId='string',
        AuthFlow='USER_SRP_AUTH'|'REFRESH_TOKEN_AUTH'|'REFRESH_TOKEN'|'CUSTOM_AUTH'|'ADMIN_NO_SRP_AUTH'|'USER_PASSWORD_AUTH'|'ADMIN_USER_PASSWORD_AUTH',
        AuthParameters={
            'string': 'string'
        },
        ClientMetadata={
            'string': 'string'
        },
        AnalyticsMetadata={
            'AnalyticsEndpointId': 'string'
        },
        ContextData={
            'IpAddress': 'string',
            'ServerName': 'string',
            'ServerPath': 'string',
            'HttpHeaders': [
                {
                    'headerName': 'string',
                    'headerValue': 'string'
                },
            ],
            'EncodedData': 'string'
        }
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe ID of the Amazon Cognito user pool.\n

    :type ClientId: string
    :param ClientId: [REQUIRED]\nThe app client ID.\n

    :type AuthFlow: string
    :param AuthFlow: [REQUIRED]\nThe authentication flow for this call to execute. The API action will depend on this value. For example:\n\nREFRESH_TOKEN_AUTH will take in a valid refresh token and return new tokens.\nUSER_SRP_AUTH will take in USERNAME and SRP_A and return the SRP variables to be used for next challenge execution.\nUSER_PASSWORD_AUTH will take in USERNAME and PASSWORD and return the next challenge or tokens.\n\nValid values include:\n\nUSER_SRP_AUTH : Authentication flow for the Secure Remote Password (SRP) protocol.\nREFRESH_TOKEN_AUTH /REFRESH_TOKEN : Authentication flow for refreshing the access token and ID token by supplying a valid refresh token.\nCUSTOM_AUTH : Custom authentication flow.\nADMIN_NO_SRP_AUTH : Non-SRP authentication flow; you can pass in the USERNAME and PASSWORD directly if the flow is enabled for calling the app client.\nUSER_PASSWORD_AUTH : Non-SRP authentication flow; USERNAME and PASSWORD are passed directly. If a user migration Lambda trigger is set, this flow will invoke the user migration Lambda if the USERNAME is not found in the user pool.\nADMIN_USER_PASSWORD_AUTH : Admin-based user password authentication. This replaces the ADMIN_NO_SRP_AUTH authentication flow. In this flow, Cognito receives the password in the request instead of using the SRP process to verify passwords.\n\n

    :type AuthParameters: dict
    :param AuthParameters: The authentication parameters. These are inputs corresponding to the AuthFlow that you are invoking. The required values depend on the value of AuthFlow :\n\nFor USER_SRP_AUTH : USERNAME (required), SRP_A (required), SECRET_HASH (required if the app client is configured with a client secret), DEVICE_KEY\nFor REFRESH_TOKEN_AUTH/REFRESH_TOKEN : REFRESH_TOKEN (required), SECRET_HASH (required if the app client is configured with a client secret), DEVICE_KEY\nFor ADMIN_NO_SRP_AUTH : USERNAME (required), SECRET_HASH (if app client is configured with client secret), PASSWORD (required), DEVICE_KEY\nFor CUSTOM_AUTH : USERNAME (required), SECRET_HASH (if app client is configured with client secret), DEVICE_KEY\n\n\n(string) --\n(string) --\n\n\n\n

    :type ClientMetadata: dict
    :param ClientMetadata: A map of custom key-value pairs that you can provide as input for certain custom workflows that this action triggers.\nYou create custom workflows by assigning AWS Lambda functions to user pool triggers. When you use the AdminInitiateAuth API action, Amazon Cognito invokes the AWS Lambda functions that are specified for various triggers. The ClientMetadata value is passed as input to the functions for only the following triggers:\n\nPre signup\nPre authentication\nUser migration\n\nWhen Amazon Cognito invokes the functions for these triggers, it passes a JSON payload, which the function receives as input. This payload contains a validationData attribute, which provides the data that you assigned to the ClientMetadata parameter in your AdminInitiateAuth request. In your function code in AWS Lambda, you can process the validationData value to enhance your workflow for your specific needs.\nWhen you use the AdminInitiateAuth API action, Amazon Cognito also invokes the functions for the following triggers, but it does not provide the ClientMetadata value as input:\n\nPost authentication\nCustom message\nPre token generation\nCreate auth challenge\nDefine auth challenge\nVerify auth challenge\n\nFor more information, see Customizing User Pool Workflows with Lambda Triggers in the Amazon Cognito Developer Guide .\n\nNote\nTake the following limitations into consideration when you use the ClientMetadata parameter:\n\nAmazon Cognito does not store the ClientMetadata value. This data is available only to AWS Lambda triggers that are assigned to a user pool to support custom workflows. If your user pool configuration does not include triggers, the ClientMetadata parameter serves no purpose.\nAmazon Cognito does not validate the ClientMetadata value.\nAmazon Cognito does not encrypt the the ClientMetadata value, so don\'t use it to provide sensitive information.\n\n\n\n(string) --\n(string) --\n\n\n\n

    :type AnalyticsMetadata: dict
    :param AnalyticsMetadata: The analytics metadata for collecting Amazon Pinpoint metrics for AdminInitiateAuth calls.\n\nAnalyticsEndpointId (string) --The endpoint ID.\n\n\n

    :type ContextData: dict
    :param ContextData: Contextual data such as the user\'s device fingerprint, IP address, or location used for evaluating the risk of an unexpected event by Amazon Cognito advanced security.\n\nIpAddress (string) -- [REQUIRED]Source IP address of your user.\n\nServerName (string) -- [REQUIRED]Your server endpoint where this API is invoked.\n\nServerPath (string) -- [REQUIRED]Your server path where this API is invoked.\n\nHttpHeaders (list) -- [REQUIRED]HttpHeaders received on your server in same order.\n\n(dict) --The HTTP header.\n\nheaderName (string) --The header name\n\nheaderValue (string) --The header value.\n\n\n\n\n\nEncodedData (string) --Encoded data containing device fingerprinting details, collected using the Amazon Cognito context data collection library.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ChallengeName': 'SMS_MFA'|'SOFTWARE_TOKEN_MFA'|'SELECT_MFA_TYPE'|'MFA_SETUP'|'PASSWORD_VERIFIER'|'CUSTOM_CHALLENGE'|'DEVICE_SRP_AUTH'|'DEVICE_PASSWORD_VERIFIER'|'ADMIN_NO_SRP_AUTH'|'NEW_PASSWORD_REQUIRED',
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


Response Structure

(dict) --
Initiates the authentication response, as an administrator.

ChallengeName (string) --
The name of the challenge which you are responding to with this call. This is returned to you in the AdminInitiateAuth response if you need to pass another challenge.

MFA_SETUP : If MFA is required, users who do not have at least one of the MFA methods set up are presented with an MFA_SETUP challenge. The user must set up at least one MFA type to continue to authenticate.
SELECT_MFA_TYPE : Selects the MFA type. Valid MFA options are SMS_MFA for text SMS MFA, and SOFTWARE_TOKEN_MFA for TOTP software token MFA.
SMS_MFA : Next challenge is to supply an SMS_MFA_CODE , delivered via SMS.
PASSWORD_VERIFIER : Next challenge is to supply PASSWORD_CLAIM_SIGNATURE , PASSWORD_CLAIM_SECRET_BLOCK , and TIMESTAMP after the client-side SRP calculations.
CUSTOM_CHALLENGE : This is returned if your custom authentication flow determines that the user should pass another challenge before tokens are issued.
DEVICE_SRP_AUTH : If device tracking was enabled on your user pool and the previous challenges were passed, this challenge is returned so that Amazon Cognito can start tracking this device.
DEVICE_PASSWORD_VERIFIER : Similar to PASSWORD_VERIFIER , but for devices only.
ADMIN_NO_SRP_AUTH : This is returned if you need to authenticate with USERNAME and PASSWORD directly. An app client must be enabled to use this flow.
NEW_PASSWORD_REQUIRED : For users which are required to change their passwords after successful first login. This challenge should be passed with NEW_PASSWORD and any other required attributes.


Session (string) --
The session which should be passed both ways in challenge-response calls to the service. If AdminInitiateAuth or AdminRespondToAuthChallenge API call determines that the caller needs to go through another challenge, they return a session with other challenge parameters. This session should be passed as it is to the next AdminRespondToAuthChallenge API call.

ChallengeParameters (dict) --
The challenge parameters. These are returned to you in the AdminInitiateAuth response if you need to pass another challenge. The responses in this parameter should be used to compute inputs to the next call (AdminRespondToAuthChallenge ).
All challenges require USERNAME and SECRET_HASH (if applicable).
The value of the USER_ID_FOR_SRP attribute will be the user\'s actual username, not an alias (such as email address or phone number), even if you specified an alias in your call to AdminInitiateAuth . This is because, in the AdminRespondToAuthChallenge API ChallengeResponses , the USERNAME attribute cannot be an alias.

(string) --
(string) --




AuthenticationResult (dict) --
The result of the authentication response. This is only returned if the caller does not need to pass another challenge. If the caller does need to pass another challenge before it gets tokens, ChallengeName , ChallengeParameters , and Session are returned.

AccessToken (string) --
The access token.

ExpiresIn (integer) --
The expiration period of the authentication result in seconds.

TokenType (string) --
The token type.

RefreshToken (string) --
The refresh token.

IdToken (string) --
The ID token.

NewDeviceMetadata (dict) --
The new device metadata from an authentication result.

DeviceKey (string) --
The device key.

DeviceGroupKey (string) --
The device group key.











Exceptions

CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.InternalErrorException
CognitoIdentityProvider.Client.exceptions.UnexpectedLambdaException
CognitoIdentityProvider.Client.exceptions.InvalidUserPoolConfigurationException
CognitoIdentityProvider.Client.exceptions.UserLambdaValidationException
CognitoIdentityProvider.Client.exceptions.InvalidLambdaResponseException
CognitoIdentityProvider.Client.exceptions.MFAMethodNotFoundException
CognitoIdentityProvider.Client.exceptions.InvalidSmsRoleAccessPolicyException
CognitoIdentityProvider.Client.exceptions.InvalidSmsRoleTrustRelationshipException
CognitoIdentityProvider.Client.exceptions.PasswordResetRequiredException
CognitoIdentityProvider.Client.exceptions.UserNotFoundException
CognitoIdentityProvider.Client.exceptions.UserNotConfirmedException


    :return: {
        'ChallengeName': 'SMS_MFA'|'SOFTWARE_TOKEN_MFA'|'SELECT_MFA_TYPE'|'MFA_SETUP'|'PASSWORD_VERIFIER'|'CUSTOM_CHALLENGE'|'DEVICE_SRP_AUTH'|'DEVICE_PASSWORD_VERIFIER'|'ADMIN_NO_SRP_AUTH'|'NEW_PASSWORD_REQUIRED',
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
    MFA_SETUP : If MFA is required, users who do not have at least one of the MFA methods set up are presented with an MFA_SETUP challenge. The user must set up at least one MFA type to continue to authenticate.
    SELECT_MFA_TYPE : Selects the MFA type. Valid MFA options are SMS_MFA for text SMS MFA, and SOFTWARE_TOKEN_MFA for TOTP software token MFA.
    SMS_MFA : Next challenge is to supply an SMS_MFA_CODE , delivered via SMS.
    PASSWORD_VERIFIER : Next challenge is to supply PASSWORD_CLAIM_SIGNATURE , PASSWORD_CLAIM_SECRET_BLOCK , and TIMESTAMP after the client-side SRP calculations.
    CUSTOM_CHALLENGE : This is returned if your custom authentication flow determines that the user should pass another challenge before tokens are issued.
    DEVICE_SRP_AUTH : If device tracking was enabled on your user pool and the previous challenges were passed, this challenge is returned so that Amazon Cognito can start tracking this device.
    DEVICE_PASSWORD_VERIFIER : Similar to PASSWORD_VERIFIER , but for devices only.
    ADMIN_NO_SRP_AUTH : This is returned if you need to authenticate with USERNAME and PASSWORD directly. An app client must be enabled to use this flow.
    NEW_PASSWORD_REQUIRED : For users which are required to change their passwords after successful first login. This challenge should be passed with NEW_PASSWORD and any other required attributes.
    
    """
    pass

def admin_link_provider_for_user(UserPoolId=None, DestinationUser=None, SourceUser=None):
    """
    Links an existing user account in a user pool (DestinationUser ) to an identity from an external identity provider (SourceUser ) based on a specified attribute name and value from the external identity provider. This allows you to create a link from the existing user account to an external federated user identity that has not yet been used to sign in, so that the federated user identity can be used to sign in as the existing user account.
    For example, if there is an existing user with a username and password, this API links that user to a federated user identity, so that when the federated user identity is used, the user signs in as the existing user account.
    See also .
    This action is enabled only for admin access and requires developer credentials.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.admin_link_provider_for_user(
        UserPoolId='string',
        DestinationUser={
            'ProviderName': 'string',
            'ProviderAttributeName': 'string',
            'ProviderAttributeValue': 'string'
        },
        SourceUser={
            'ProviderName': 'string',
            'ProviderAttributeName': 'string',
            'ProviderAttributeValue': 'string'
        }
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID for the user pool.\n

    :type DestinationUser: dict
    :param DestinationUser: [REQUIRED]\nThe existing user in the user pool to be linked to the external identity provider user account. Can be a native (Username + Password) Cognito User Pools user or a federated user (for example, a SAML or Facebook user). If the user doesn\'t exist, an exception is thrown. This is the user that is returned when the new user (with the linked identity provider attribute) signs in.\nFor a native username + password user, the ProviderAttributeValue for the DestinationUser should be the username in the user pool. For a federated user, it should be the provider-specific user_id .\nThe ProviderAttributeName of the DestinationUser is ignored.\nThe ProviderName should be set to Cognito for users in Cognito user pools.\n\nProviderName (string) --The name of the provider, for example, Facebook, Google, or Login with Amazon.\n\nProviderAttributeName (string) --The name of the provider attribute to link to, for example, NameID .\n\nProviderAttributeValue (string) --The value of the provider attribute to link to, for example, xxxxx_account .\n\n\n

    :type SourceUser: dict
    :param SourceUser: [REQUIRED]\nAn external identity provider account for a user who does not currently exist yet in the user pool. This user must be a federated user (for example, a SAML or Facebook user), not another native user.\nIf the SourceUser is a federated social identity provider user (Facebook, Google, or Login with Amazon), you must set the ProviderAttributeName to Cognito_Subject . For social identity providers, the ProviderName will be Facebook , Google , or LoginWithAmazon , and Cognito will automatically parse the Facebook, Google, and Login with Amazon tokens for id , sub , and user_id , respectively. The ProviderAttributeValue for the user must be the same value as the id , sub , or user_id value found in the social identity provider token.\nFor SAML, the ProviderAttributeName can be any value that matches a claim in the SAML assertion. If you wish to link SAML users based on the subject of the SAML assertion, you should map the subject to a claim through the SAML identity provider and submit that claim name as the ProviderAttributeName . If you set ProviderAttributeName to Cognito_Subject , Cognito will automatically parse the default unique identifier found in the subject from the SAML token.\n\nProviderName (string) --The name of the provider, for example, Facebook, Google, or Login with Amazon.\n\nProviderAttributeName (string) --The name of the provider attribute to link to, for example, NameID .\n\nProviderAttributeValue (string) --The value of the provider attribute to link to, for example, xxxxx_account .\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.UserNotFoundException
CognitoIdentityProvider.Client.exceptions.AliasExistsException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def admin_list_devices(UserPoolId=None, Username=None, Limit=None, PaginationToken=None):
    """
    Lists devices, as an administrator.
    Calling this action requires developer credentials.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.admin_list_devices(
        UserPoolId='string',
        Username='string',
        Limit=123,
        PaginationToken='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID.\n

    :type Username: string
    :param Username: [REQUIRED]\nThe user name.\n

    :type Limit: integer
    :param Limit: The limit of the devices request.

    :type PaginationToken: string
    :param PaginationToken: The pagination token.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --
Lists the device\'s response, as an administrator.

Devices (list) --
The devices in the list of devices response.

(dict) --
The device type.

DeviceKey (string) --
The device key.

DeviceAttributes (list) --
The device attributes.

(dict) --
Specifies whether the attribute is standard or custom.

Name (string) --
The name of the attribute.

Value (string) --
The value of the attribute.





DeviceCreateDate (datetime) --
The creation date of the device.

DeviceLastModifiedDate (datetime) --
The last modified date of the device.

DeviceLastAuthenticatedDate (datetime) --
The date in which the device was last authenticated.





PaginationToken (string) --
The pagination token.







Exceptions

CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.InvalidUserPoolConfigurationException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.InternalErrorException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException


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
    
    
    :returns: 
    CognitoIdentityProvider.Client.exceptions.InvalidParameterException
    CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
    CognitoIdentityProvider.Client.exceptions.InvalidUserPoolConfigurationException
    CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
    CognitoIdentityProvider.Client.exceptions.InternalErrorException
    CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
    
    """
    pass

def admin_list_groups_for_user(Username=None, UserPoolId=None, Limit=None, NextToken=None):
    """
    Lists the groups that the user belongs to.
    Calling this action requires developer credentials.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.admin_list_groups_for_user(
        Username='string',
        UserPoolId='string',
        Limit=123,
        NextToken='string'
    )
    
    
    :type Username: string
    :param Username: [REQUIRED]\nThe username for the user.\n

    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID for the user pool.\n

    :type Limit: integer
    :param Limit: The limit of the request to list groups.

    :type NextToken: string
    :param NextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

Groups (list) --
The groups that the user belongs to.

(dict) --
The group type.

GroupName (string) --
The name of the group.

UserPoolId (string) --
The user pool ID for the user pool.

Description (string) --
A string containing the description of the group.

RoleArn (string) --
The role ARN for the group.

Precedence (integer) --
A nonnegative integer value that specifies the precedence of this group relative to the other groups that a user can belong to in the user pool. If a user belongs to two or more groups, it is the group with the highest precedence whose role ARN will be used in the cognito:roles and cognito:preferred_role claims in the user\'s tokens. Groups with higher Precedence values take precedence over groups with lower Precedence values or with null Precedence values.
Two groups can have the same Precedence value. If this happens, neither group takes precedence over the other. If two groups with the same Precedence have the same role ARN, that role is used in the cognito:preferred_role claim in tokens for users in each group. If the two groups have different role ARNs, the cognito:preferred_role claim is not set in users\' tokens.
The default Precedence value is null.

LastModifiedDate (datetime) --
The date the group was last modified.

CreationDate (datetime) --
The date the group was created.





NextToken (string) --
An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.







Exceptions

CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.UserNotFoundException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


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
    
    
    :returns: 
    CognitoIdentityProvider.Client.exceptions.InvalidParameterException
    CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
    CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
    CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
    CognitoIdentityProvider.Client.exceptions.UserNotFoundException
    CognitoIdentityProvider.Client.exceptions.InternalErrorException
    
    """
    pass

def admin_list_user_auth_events(UserPoolId=None, Username=None, MaxResults=None, NextToken=None):
    """
    Lists a history of user activity and any risks detected as part of Amazon Cognito advanced security.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.admin_list_user_auth_events(
        UserPoolId='string',
        Username='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID.\n

    :type Username: string
    :param Username: [REQUIRED]\nThe user pool username or an alias.\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of authentication events to return.

    :type NextToken: string
    :param NextToken: A pagination token.

    :rtype: dict

ReturnsResponse Syntax
{
    'AuthEvents': [
        {
            'EventId': 'string',
            'EventType': 'SignIn'|'SignUp'|'ForgotPassword',
            'CreationDate': datetime(2015, 1, 1),
            'EventResponse': 'Success'|'Failure',
            'EventRisk': {
                'RiskDecision': 'NoRisk'|'AccountTakeover'|'Block',
                'RiskLevel': 'Low'|'Medium'|'High',
                'CompromisedCredentialsDetected': True|False
            },
            'ChallengeResponses': [
                {
                    'ChallengeName': 'Password'|'Mfa',
                    'ChallengeResponse': 'Success'|'Failure'
                },
            ],
            'EventContextData': {
                'IpAddress': 'string',
                'DeviceName': 'string',
                'Timezone': 'string',
                'City': 'string',
                'Country': 'string'
            },
            'EventFeedback': {
                'FeedbackValue': 'Valid'|'Invalid',
                'Provider': 'string',
                'FeedbackDate': datetime(2015, 1, 1)
            }
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

AuthEvents (list) --
The response object. It includes the EventID , EventType , CreationDate , EventRisk , and EventResponse .

(dict) --
The authentication event type.

EventId (string) --
The event ID.

EventType (string) --
The event type.

CreationDate (datetime) --
The creation date

EventResponse (string) --
The event response.

EventRisk (dict) --
The event risk.

RiskDecision (string) --
The risk decision.

RiskLevel (string) --
The risk level.

CompromisedCredentialsDetected (boolean) --
Indicates whether compromised credentials were detected during an authentication event.



ChallengeResponses (list) --
The challenge responses.

(dict) --
The challenge response type.

ChallengeName (string) --
The challenge name

ChallengeResponse (string) --
The challenge response.





EventContextData (dict) --
The user context data captured at the time of an event request. It provides additional information about the client from which event the request is received.

IpAddress (string) --
The user\'s IP address.

DeviceName (string) --
The user\'s device name.

Timezone (string) --
The user\'s time zone.

City (string) --
The user\'s city.

Country (string) --
The user\'s country.



EventFeedback (dict) --
A flag specifying the user feedback captured at the time of an event request is good or bad.

FeedbackValue (string) --
The event feedback value.

Provider (string) --
The provider.

FeedbackDate (datetime) --
The event feedback date.







NextToken (string) --
A pagination token.







Exceptions

CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.UserNotFoundException
CognitoIdentityProvider.Client.exceptions.UserPoolAddOnNotEnabledException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


    :return: {
        'AuthEvents': [
            {
                'EventId': 'string',
                'EventType': 'SignIn'|'SignUp'|'ForgotPassword',
                'CreationDate': datetime(2015, 1, 1),
                'EventResponse': 'Success'|'Failure',
                'EventRisk': {
                    'RiskDecision': 'NoRisk'|'AccountTakeover'|'Block',
                    'RiskLevel': 'Low'|'Medium'|'High',
                    'CompromisedCredentialsDetected': True|False
                },
                'ChallengeResponses': [
                    {
                        'ChallengeName': 'Password'|'Mfa',
                        'ChallengeResponse': 'Success'|'Failure'
                    },
                ],
                'EventContextData': {
                    'IpAddress': 'string',
                    'DeviceName': 'string',
                    'Timezone': 'string',
                    'City': 'string',
                    'Country': 'string'
                },
                'EventFeedback': {
                    'FeedbackValue': 'Valid'|'Invalid',
                    'Provider': 'string',
                    'FeedbackDate': datetime(2015, 1, 1)
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    CognitoIdentityProvider.Client.exceptions.InvalidParameterException
    CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
    CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
    CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
    CognitoIdentityProvider.Client.exceptions.UserNotFoundException
    CognitoIdentityProvider.Client.exceptions.UserPoolAddOnNotEnabledException
    CognitoIdentityProvider.Client.exceptions.InternalErrorException
    
    """
    pass

def admin_remove_user_from_group(UserPoolId=None, Username=None, GroupName=None):
    """
    Removes the specified user from the specified group.
    Calling this action requires developer credentials.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.admin_remove_user_from_group(
        UserPoolId='string',
        Username='string',
        GroupName='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID for the user pool.\n

    :type Username: string
    :param Username: [REQUIRED]\nThe username for the user.\n

    :type GroupName: string
    :param GroupName: [REQUIRED]\nThe group name.\n

    :returns: 
    CognitoIdentityProvider.Client.exceptions.InvalidParameterException
    CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
    CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
    CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
    CognitoIdentityProvider.Client.exceptions.UserNotFoundException
    CognitoIdentityProvider.Client.exceptions.InternalErrorException
    
    """
    pass

def admin_reset_user_password(UserPoolId=None, Username=None, ClientMetadata=None):
    """
    Resets the specified user\'s password in a user pool as an administrator. Works on any user.
    When a developer calls this API, the current password is invalidated, so it must be changed. If a user tries to sign in after the API is called, the app will get a PasswordResetRequiredException exception back and should direct the user down the flow to reset the password, which is the same as the forgot password flow. In addition, if the user pool has phone verification selected and a verified phone number exists for the user, or if email verification is selected and a verified email exists for the user, calling this API will also result in sending a message to the end user with the code to change their password.
    Calling this action requires developer credentials.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.admin_reset_user_password(
        UserPoolId='string',
        Username='string',
        ClientMetadata={
            'string': 'string'
        }
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID for the user pool where you want to reset the user\'s password.\n

    :type Username: string
    :param Username: [REQUIRED]\nThe user name of the user whose password you wish to reset.\n

    :type ClientMetadata: dict
    :param ClientMetadata: A map of custom key-value pairs that you can provide as input for any custom workflows that this action triggers.\nYou create custom workflows by assigning AWS Lambda functions to user pool triggers. When you use the AdminResetUserPassword API action, Amazon Cognito invokes the function that is assigned to the custom message trigger. When Amazon Cognito invokes this function, it passes a JSON payload, which the function receives as input. This payload contains a clientMetadata attribute, which provides the data that you assigned to the ClientMetadata parameter in your AdminResetUserPassword request. In your function code in AWS Lambda, you can process the clientMetadata value to enhance your workflow for your specific needs.\nFor more information, see Customizing User Pool Workflows with Lambda Triggers in the Amazon Cognito Developer Guide .\n\nNote\nTake the following limitations into consideration when you use the ClientMetadata parameter:\n\nAmazon Cognito does not store the ClientMetadata value. This data is available only to AWS Lambda triggers that are assigned to a user pool to support custom workflows. If your user pool configuration does not include triggers, the ClientMetadata parameter serves no purpose.\nAmazon Cognito does not validate the ClientMetadata value.\nAmazon Cognito does not encrypt the the ClientMetadata value, so don\'t use it to provide sensitive information.\n\n\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
Represents the response from the server to reset a user password as an administrator.





Exceptions

CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.UnexpectedLambdaException
CognitoIdentityProvider.Client.exceptions.UserLambdaValidationException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.InvalidLambdaResponseException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.LimitExceededException
CognitoIdentityProvider.Client.exceptions.UserNotFoundException
CognitoIdentityProvider.Client.exceptions.InvalidSmsRoleAccessPolicyException
CognitoIdentityProvider.Client.exceptions.InvalidEmailRoleAccessPolicyException
CognitoIdentityProvider.Client.exceptions.InvalidSmsRoleTrustRelationshipException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


    :return: {}
    
    
    :returns: 
    CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
    CognitoIdentityProvider.Client.exceptions.InvalidParameterException
    CognitoIdentityProvider.Client.exceptions.UnexpectedLambdaException
    CognitoIdentityProvider.Client.exceptions.UserLambdaValidationException
    CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
    CognitoIdentityProvider.Client.exceptions.InvalidLambdaResponseException
    CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
    CognitoIdentityProvider.Client.exceptions.LimitExceededException
    CognitoIdentityProvider.Client.exceptions.UserNotFoundException
    CognitoIdentityProvider.Client.exceptions.InvalidSmsRoleAccessPolicyException
    CognitoIdentityProvider.Client.exceptions.InvalidEmailRoleAccessPolicyException
    CognitoIdentityProvider.Client.exceptions.InvalidSmsRoleTrustRelationshipException
    CognitoIdentityProvider.Client.exceptions.InternalErrorException
    
    """
    pass

def admin_respond_to_auth_challenge(UserPoolId=None, ClientId=None, ChallengeName=None, ChallengeResponses=None, Session=None, AnalyticsMetadata=None, ContextData=None, ClientMetadata=None):
    """
    Responds to an authentication challenge, as an administrator.
    Calling this action requires developer credentials.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.admin_respond_to_auth_challenge(
        UserPoolId='string',
        ClientId='string',
        ChallengeName='SMS_MFA'|'SOFTWARE_TOKEN_MFA'|'SELECT_MFA_TYPE'|'MFA_SETUP'|'PASSWORD_VERIFIER'|'CUSTOM_CHALLENGE'|'DEVICE_SRP_AUTH'|'DEVICE_PASSWORD_VERIFIER'|'ADMIN_NO_SRP_AUTH'|'NEW_PASSWORD_REQUIRED',
        ChallengeResponses={
            'string': 'string'
        },
        Session='string',
        AnalyticsMetadata={
            'AnalyticsEndpointId': 'string'
        },
        ContextData={
            'IpAddress': 'string',
            'ServerName': 'string',
            'ServerPath': 'string',
            'HttpHeaders': [
                {
                    'headerName': 'string',
                    'headerValue': 'string'
                },
            ],
            'EncodedData': 'string'
        },
        ClientMetadata={
            'string': 'string'
        }
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe ID of the Amazon Cognito user pool.\n

    :type ClientId: string
    :param ClientId: [REQUIRED]\nThe app client ID.\n

    :type ChallengeName: string
    :param ChallengeName: [REQUIRED]\nThe challenge name. For more information, see .\n

    :type ChallengeResponses: dict
    :param ChallengeResponses: The challenge responses. These are inputs corresponding to the value of ChallengeName , for example:\n\nSMS_MFA : SMS_MFA_CODE , USERNAME , SECRET_HASH (if app client is configured with client secret).\nPASSWORD_VERIFIER : PASSWORD_CLAIM_SIGNATURE , PASSWORD_CLAIM_SECRET_BLOCK , TIMESTAMP , USERNAME , SECRET_HASH (if app client is configured with client secret).\nADMIN_NO_SRP_AUTH : PASSWORD , USERNAME , SECRET_HASH (if app client is configured with client secret).\nNEW_PASSWORD_REQUIRED : NEW_PASSWORD , any other required attributes, USERNAME , SECRET_HASH (if app client is configured with client secret).\n\nThe value of the USERNAME attribute must be the user\'s actual username, not an alias (such as email address or phone number). To make this easier, the AdminInitiateAuth response includes the actual username value in the USERNAMEUSER_ID_FOR_SRP attribute, even if you specified an alias in your call to AdminInitiateAuth .\n\n(string) --\n(string) --\n\n\n\n

    :type Session: string
    :param Session: The session which should be passed both ways in challenge-response calls to the service. If InitiateAuth or RespondToAuthChallenge API call determines that the caller needs to go through another challenge, they return a session with other challenge parameters. This session should be passed as it is to the next RespondToAuthChallenge API call.

    :type AnalyticsMetadata: dict
    :param AnalyticsMetadata: The analytics metadata for collecting Amazon Pinpoint metrics for AdminRespondToAuthChallenge calls.\n\nAnalyticsEndpointId (string) --The endpoint ID.\n\n\n

    :type ContextData: dict
    :param ContextData: Contextual data such as the user\'s device fingerprint, IP address, or location used for evaluating the risk of an unexpected event by Amazon Cognito advanced security.\n\nIpAddress (string) -- [REQUIRED]Source IP address of your user.\n\nServerName (string) -- [REQUIRED]Your server endpoint where this API is invoked.\n\nServerPath (string) -- [REQUIRED]Your server path where this API is invoked.\n\nHttpHeaders (list) -- [REQUIRED]HttpHeaders received on your server in same order.\n\n(dict) --The HTTP header.\n\nheaderName (string) --The header name\n\nheaderValue (string) --The header value.\n\n\n\n\n\nEncodedData (string) --Encoded data containing device fingerprinting details, collected using the Amazon Cognito context data collection library.\n\n\n

    :type ClientMetadata: dict
    :param ClientMetadata: A map of custom key-value pairs that you can provide as input for any custom workflows that this action triggers.\nYou create custom workflows by assigning AWS Lambda functions to user pool triggers. When you use the AdminRespondToAuthChallenge API action, Amazon Cognito invokes any functions that are assigned to the following triggers: pre sign-up , custom message , post authentication , user migration , pre token generation , define auth challenge , create auth challenge , and verify auth challenge response . When Amazon Cognito invokes any of these functions, it passes a JSON payload, which the function receives as input. This payload contains a clientMetadata attribute, which provides the data that you assigned to the ClientMetadata parameter in your AdminRespondToAuthChallenge request. In your function code in AWS Lambda, you can process the clientMetadata value to enhance your workflow for your specific needs.\nFor more information, see Customizing User Pool Workflows with Lambda Triggers in the Amazon Cognito Developer Guide .\n\nNote\nTake the following limitations into consideration when you use the ClientMetadata parameter:\n\nAmazon Cognito does not store the ClientMetadata value. This data is available only to AWS Lambda triggers that are assigned to a user pool to support custom workflows. If your user pool configuration does not include triggers, the ClientMetadata parameter serves no purpose.\nAmazon Cognito does not validate the ClientMetadata value.\nAmazon Cognito does not encrypt the the ClientMetadata value, so don\'t use it to provide sensitive information.\n\n\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ChallengeName': 'SMS_MFA'|'SOFTWARE_TOKEN_MFA'|'SELECT_MFA_TYPE'|'MFA_SETUP'|'PASSWORD_VERIFIER'|'CUSTOM_CHALLENGE'|'DEVICE_SRP_AUTH'|'DEVICE_PASSWORD_VERIFIER'|'ADMIN_NO_SRP_AUTH'|'NEW_PASSWORD_REQUIRED',
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


Response Structure

(dict) --
Responds to the authentication challenge, as an administrator.

ChallengeName (string) --
The name of the challenge. For more information, see .

Session (string) --
The session which should be passed both ways in challenge-response calls to the service. If the or API call determines that the caller needs to go through another challenge, they return a session with other challenge parameters. This session should be passed as it is to the next RespondToAuthChallenge API call.

ChallengeParameters (dict) --
The challenge parameters. For more information, see .

(string) --
(string) --




AuthenticationResult (dict) --
The result returned by the server in response to the authentication request.

AccessToken (string) --
The access token.

ExpiresIn (integer) --
The expiration period of the authentication result in seconds.

TokenType (string) --
The token type.

RefreshToken (string) --
The refresh token.

IdToken (string) --
The ID token.

NewDeviceMetadata (dict) --
The new device metadata from an authentication result.

DeviceKey (string) --
The device key.

DeviceGroupKey (string) --
The device group key.











Exceptions

CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.CodeMismatchException
CognitoIdentityProvider.Client.exceptions.ExpiredCodeException
CognitoIdentityProvider.Client.exceptions.UnexpectedLambdaException
CognitoIdentityProvider.Client.exceptions.InvalidPasswordException
CognitoIdentityProvider.Client.exceptions.UserLambdaValidationException
CognitoIdentityProvider.Client.exceptions.InvalidLambdaResponseException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.InvalidUserPoolConfigurationException
CognitoIdentityProvider.Client.exceptions.InternalErrorException
CognitoIdentityProvider.Client.exceptions.MFAMethodNotFoundException
CognitoIdentityProvider.Client.exceptions.InvalidSmsRoleAccessPolicyException
CognitoIdentityProvider.Client.exceptions.InvalidSmsRoleTrustRelationshipException
CognitoIdentityProvider.Client.exceptions.AliasExistsException
CognitoIdentityProvider.Client.exceptions.PasswordResetRequiredException
CognitoIdentityProvider.Client.exceptions.UserNotFoundException
CognitoIdentityProvider.Client.exceptions.UserNotConfirmedException
CognitoIdentityProvider.Client.exceptions.SoftwareTokenMFANotFoundException


    :return: {
        'ChallengeName': 'SMS_MFA'|'SOFTWARE_TOKEN_MFA'|'SELECT_MFA_TYPE'|'MFA_SETUP'|'PASSWORD_VERIFIER'|'CUSTOM_CHALLENGE'|'DEVICE_SRP_AUTH'|'DEVICE_PASSWORD_VERIFIER'|'ADMIN_NO_SRP_AUTH'|'NEW_PASSWORD_REQUIRED',
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

def admin_set_user_mfa_preference(SMSMfaSettings=None, SoftwareTokenMfaSettings=None, Username=None, UserPoolId=None):
    """
    Sets the user\'s multi-factor authentication (MFA) preference, including which MFA options are enabled and if any are preferred. Only one factor can be set as preferred. The preferred MFA factor will be used to authenticate a user if multiple factors are enabled. If multiple options are enabled and no preference is set, a challenge to choose an MFA option will be returned during sign in.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.admin_set_user_mfa_preference(
        SMSMfaSettings={
            'Enabled': True|False,
            'PreferredMfa': True|False
        },
        SoftwareTokenMfaSettings={
            'Enabled': True|False,
            'PreferredMfa': True|False
        },
        Username='string',
        UserPoolId='string'
    )
    
    
    :type SMSMfaSettings: dict
    :param SMSMfaSettings: The SMS text message MFA settings.\n\nEnabled (boolean) --Specifies whether SMS text message MFA is enabled.\n\nPreferredMfa (boolean) --Specifies whether SMS is the preferred MFA method.\n\n\n

    :type SoftwareTokenMfaSettings: dict
    :param SoftwareTokenMfaSettings: The time-based one-time password software token MFA settings.\n\nEnabled (boolean) --Specifies whether software token MFA is enabled.\n\nPreferredMfa (boolean) --Specifies whether software token MFA is the preferred MFA method.\n\n\n

    :type Username: string
    :param Username: [REQUIRED]\nThe user pool username or alias.\n

    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.PasswordResetRequiredException
CognitoIdentityProvider.Client.exceptions.UserNotFoundException
CognitoIdentityProvider.Client.exceptions.UserNotConfirmedException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def admin_set_user_password(UserPoolId=None, Username=None, Password=None, Permanent=None):
    """
    Sets the specified user\'s password in a user pool as an administrator. Works on any user.
    The password can be temporary or permanent. If it is temporary, the user status will be placed into the FORCE_CHANGE_PASSWORD state. When the user next tries to sign in, the InitiateAuth/AdminInitiateAuth response will contain the NEW_PASSWORD_REQUIRED challenge. If the user does not sign in before it expires, the user will not be able to sign in and their password will need to be reset by an administrator.
    Once the user has set a new password, or the password is permanent, the user status will be set to Confirmed .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.admin_set_user_password(
        UserPoolId='string',
        Username='string',
        Password='string',
        Permanent=True|False
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID for the user pool where you want to set the user\'s password.\n

    :type Username: string
    :param Username: [REQUIRED]\nThe user name of the user whose password you wish to set.\n

    :type Password: string
    :param Password: [REQUIRED]\nThe password for the user.\n

    :type Permanent: boolean
    :param Permanent: True if the password is permanent, False if it is temporary.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.UserNotFoundException
CognitoIdentityProvider.Client.exceptions.InternalErrorException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.InvalidPasswordException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def admin_set_user_settings(UserPoolId=None, Username=None, MFAOptions=None):
    """
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param UserPoolId: [REQUIRED]\nThe ID of the user pool that contains the user that you are setting options for.\n

    :type Username: string
    :param Username: [REQUIRED]\nThe user name of the user that you are setting options for.\n

    :type MFAOptions: list
    :param MFAOptions: [REQUIRED]\nYou can use this parameter only to set an SMS configuration that uses SMS for delivery.\n\n(dict) --\nThis data type is no longer supported. You can use it only for SMS MFA configurations. You can\'t use it for TOTP software token MFA configurations.\nTo set either type of MFA configuration, use the AdminSetUserMFAPreference or SetUserMFAPreference actions.\nTo look up information about either type of MFA configuration, use the AdminGetUserResponse$UserMFASettingList or GetUserResponse$UserMFASettingList responses.\n\nDeliveryMedium (string) --The delivery medium to send the MFA code. You can use this parameter to set only the SMS delivery medium value.\n\nAttributeName (string) --The attribute name of the MFA option type. The only valid value is phone_number .\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
Represents the response from the server to set user settings as an administrator.





Exceptions

CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.UserNotFoundException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


    :return: {}
    
    
    :returns: 
    CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
    CognitoIdentityProvider.Client.exceptions.InvalidParameterException
    CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
    CognitoIdentityProvider.Client.exceptions.UserNotFoundException
    CognitoIdentityProvider.Client.exceptions.InternalErrorException
    
    """
    pass

def admin_update_auth_event_feedback(UserPoolId=None, Username=None, EventId=None, FeedbackValue=None):
    """
    Provides feedback for an authentication event as to whether it was from a valid user. This feedback is used for improving the risk evaluation decision for the user pool as part of Amazon Cognito advanced security.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.admin_update_auth_event_feedback(
        UserPoolId='string',
        Username='string',
        EventId='string',
        FeedbackValue='Valid'|'Invalid'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID.\n

    :type Username: string
    :param Username: [REQUIRED]\nThe user pool username.\n

    :type EventId: string
    :param EventId: [REQUIRED]\nThe authentication event ID.\n

    :type FeedbackValue: string
    :param FeedbackValue: [REQUIRED]\nThe authentication event feedback value.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.UserNotFoundException
CognitoIdentityProvider.Client.exceptions.UserPoolAddOnNotEnabledException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def admin_update_device_status(UserPoolId=None, Username=None, DeviceKey=None, DeviceRememberedStatus=None):
    """
    Updates the device status as an administrator.
    Calling this action requires developer credentials.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.admin_update_device_status(
        UserPoolId='string',
        Username='string',
        DeviceKey='string',
        DeviceRememberedStatus='remembered'|'not_remembered'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID.\n

    :type Username: string
    :param Username: [REQUIRED]\nThe user name.\n

    :type DeviceKey: string
    :param DeviceKey: [REQUIRED]\nThe device key.\n

    :type DeviceRememberedStatus: string
    :param DeviceRememberedStatus: The status indicating whether a device has been remembered or not.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
The status response from the request to update the device, as an administrator.





Exceptions

CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.InvalidUserPoolConfigurationException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.UserNotFoundException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


    :return: {}
    
    
    :returns: 
    CognitoIdentityProvider.Client.exceptions.InvalidParameterException
    CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
    CognitoIdentityProvider.Client.exceptions.InvalidUserPoolConfigurationException
    CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
    CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
    CognitoIdentityProvider.Client.exceptions.UserNotFoundException
    CognitoIdentityProvider.Client.exceptions.InternalErrorException
    
    """
    pass

def admin_update_user_attributes(UserPoolId=None, Username=None, UserAttributes=None, ClientMetadata=None):
    """
    Updates the specified user\'s attributes, including developer attributes, as an administrator. Works on any user.
    For custom attributes, you must prepend the custom: prefix to the attribute name.
    In addition to updating user attributes, this API can also be used to mark phone and email as verified.
    Calling this action requires developer credentials.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.admin_update_user_attributes(
        UserPoolId='string',
        Username='string',
        UserAttributes=[
            {
                'Name': 'string',
                'Value': 'string'
            },
        ],
        ClientMetadata={
            'string': 'string'
        }
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID for the user pool where you want to update user attributes.\n

    :type Username: string
    :param Username: [REQUIRED]\nThe user name of the user for whom you want to update user attributes.\n

    :type UserAttributes: list
    :param UserAttributes: [REQUIRED]\nAn array of name-value pairs representing user attributes.\nFor custom attributes, you must prepend the custom: prefix to the attribute name.\n\n(dict) --Specifies whether the attribute is standard or custom.\n\nName (string) -- [REQUIRED]The name of the attribute.\n\nValue (string) --The value of the attribute.\n\n\n\n\n

    :type ClientMetadata: dict
    :param ClientMetadata: A map of custom key-value pairs that you can provide as input for any custom workflows that this action triggers.\nYou create custom workflows by assigning AWS Lambda functions to user pool triggers. When you use the AdminUpdateUserAttributes API action, Amazon Cognito invokes the function that is assigned to the custom message trigger. When Amazon Cognito invokes this function, it passes a JSON payload, which the function receives as input. This payload contains a clientMetadata attribute, which provides the data that you assigned to the ClientMetadata parameter in your AdminUpdateUserAttributes request. In your function code in AWS Lambda, you can process the clientMetadata value to enhance your workflow for your specific needs.\nFor more information, see Customizing User Pool Workflows with Lambda Triggers in the Amazon Cognito Developer Guide .\n\nNote\nTake the following limitations into consideration when you use the ClientMetadata parameter:\n\nAmazon Cognito does not store the ClientMetadata value. This data is available only to AWS Lambda triggers that are assigned to a user pool to support custom workflows. If your user pool configuration does not include triggers, the ClientMetadata parameter serves no purpose.\nAmazon Cognito does not validate the ClientMetadata value.\nAmazon Cognito does not encrypt the the ClientMetadata value, so don\'t use it to provide sensitive information.\n\n\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
Represents the response from the server for the request to update user attributes as an administrator.





Exceptions

CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.UnexpectedLambdaException
CognitoIdentityProvider.Client.exceptions.UserLambdaValidationException
CognitoIdentityProvider.Client.exceptions.InvalidLambdaResponseException
CognitoIdentityProvider.Client.exceptions.AliasExistsException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.UserNotFoundException
CognitoIdentityProvider.Client.exceptions.InternalErrorException
CognitoIdentityProvider.Client.exceptions.InvalidSmsRoleAccessPolicyException
CognitoIdentityProvider.Client.exceptions.InvalidEmailRoleAccessPolicyException
CognitoIdentityProvider.Client.exceptions.InvalidSmsRoleTrustRelationshipException


    :return: {}
    
    
    :returns: 
    CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
    CognitoIdentityProvider.Client.exceptions.InvalidParameterException
    CognitoIdentityProvider.Client.exceptions.UnexpectedLambdaException
    CognitoIdentityProvider.Client.exceptions.UserLambdaValidationException
    CognitoIdentityProvider.Client.exceptions.InvalidLambdaResponseException
    CognitoIdentityProvider.Client.exceptions.AliasExistsException
    CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
    CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
    CognitoIdentityProvider.Client.exceptions.UserNotFoundException
    CognitoIdentityProvider.Client.exceptions.InternalErrorException
    CognitoIdentityProvider.Client.exceptions.InvalidSmsRoleAccessPolicyException
    CognitoIdentityProvider.Client.exceptions.InvalidEmailRoleAccessPolicyException
    CognitoIdentityProvider.Client.exceptions.InvalidSmsRoleTrustRelationshipException
    
    """
    pass

def admin_user_global_sign_out(UserPoolId=None, Username=None):
    """
    Signs out users from all devices, as an administrator. It also invalidates all refresh tokens issued to a user. The user\'s current access and Id tokens remain valid until their expiry. Access and Id tokens expire one hour after they are issued.
    Calling this action requires developer credentials.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.admin_user_global_sign_out(
        UserPoolId='string',
        Username='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID.\n

    :type Username: string
    :param Username: [REQUIRED]\nThe user name.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
The global sign-out response, as an administrator.





Exceptions

CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.UserNotFoundException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


    :return: {}
    
    
    :returns: 
    CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
    CognitoIdentityProvider.Client.exceptions.InvalidParameterException
    CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
    CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
    CognitoIdentityProvider.Client.exceptions.UserNotFoundException
    CognitoIdentityProvider.Client.exceptions.InternalErrorException
    
    """
    pass

def associate_software_token(AccessToken=None, Session=None):
    """
    Returns a unique generated shared secret key code for the user account. The request takes an access token or a session string, but not both.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.associate_software_token(
        AccessToken='string',
        Session='string'
    )
    
    
    :type AccessToken: string
    :param AccessToken: The access token.

    :type Session: string
    :param Session: The session which should be passed both ways in challenge-response calls to the service. This allows authentication of the user as part of the MFA setup process.

    :rtype: dict

ReturnsResponse Syntax
{
    'SecretCode': 'string',
    'Session': 'string'
}


Response Structure

(dict) --

SecretCode (string) --
A unique generated shared secret code that is used in the TOTP algorithm to generate a one time code.

Session (string) --
The session which should be passed both ways in challenge-response calls to the service. This allows authentication of the user as part of the MFA setup process.







Exceptions

CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.InternalErrorException
CognitoIdentityProvider.Client.exceptions.SoftwareTokenMFANotFoundException


    :return: {
        'SecretCode': 'string',
        'Session': 'string'
    }
    
    
    :returns: 
    CognitoIdentityProvider.Client.exceptions.InvalidParameterException
    CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
    CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
    CognitoIdentityProvider.Client.exceptions.InternalErrorException
    CognitoIdentityProvider.Client.exceptions.SoftwareTokenMFANotFoundException
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def change_password(PreviousPassword=None, ProposedPassword=None, AccessToken=None):
    """
    Changes the password for a specified user in a user pool.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.change_password(
        PreviousPassword='string',
        ProposedPassword='string',
        AccessToken='string'
    )
    
    
    :type PreviousPassword: string
    :param PreviousPassword: [REQUIRED]\nThe old password.\n

    :type ProposedPassword: string
    :param ProposedPassword: [REQUIRED]\nThe new password.\n

    :type AccessToken: string
    :param AccessToken: [REQUIRED]\nThe access token.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
The response from the server to the change password request.





Exceptions

CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.InvalidPasswordException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.LimitExceededException
CognitoIdentityProvider.Client.exceptions.PasswordResetRequiredException
CognitoIdentityProvider.Client.exceptions.UserNotFoundException
CognitoIdentityProvider.Client.exceptions.UserNotConfirmedException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


    :return: {}
    
    
    :returns: 
    CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
    CognitoIdentityProvider.Client.exceptions.InvalidParameterException
    CognitoIdentityProvider.Client.exceptions.InvalidPasswordException
    CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
    CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
    CognitoIdentityProvider.Client.exceptions.LimitExceededException
    CognitoIdentityProvider.Client.exceptions.PasswordResetRequiredException
    CognitoIdentityProvider.Client.exceptions.UserNotFoundException
    CognitoIdentityProvider.Client.exceptions.UserNotConfirmedException
    CognitoIdentityProvider.Client.exceptions.InternalErrorException
    
    """
    pass

def confirm_device(AccessToken=None, DeviceKey=None, DeviceSecretVerifierConfig=None, DeviceName=None):
    """
    Confirms tracking of the device. This API call is the call that begins device tracking.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param AccessToken: [REQUIRED]\nThe access token.\n

    :type DeviceKey: string
    :param DeviceKey: [REQUIRED]\nThe device key.\n

    :type DeviceSecretVerifierConfig: dict
    :param DeviceSecretVerifierConfig: The configuration of the device secret verifier.\n\nPasswordVerifier (string) --The password verifier.\n\nSalt (string) --The salt.\n\n\n

    :type DeviceName: string
    :param DeviceName: The device name.

    :rtype: dict

ReturnsResponse Syntax
{
    'UserConfirmationNecessary': True|False
}


Response Structure

(dict) --
Confirms the device response.

UserConfirmationNecessary (boolean) --
Indicates whether the user confirmation is necessary to confirm the device response.







Exceptions

CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.InvalidPasswordException
CognitoIdentityProvider.Client.exceptions.InvalidLambdaResponseException
CognitoIdentityProvider.Client.exceptions.UsernameExistsException
CognitoIdentityProvider.Client.exceptions.InvalidUserPoolConfigurationException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.PasswordResetRequiredException
CognitoIdentityProvider.Client.exceptions.UserNotFoundException
CognitoIdentityProvider.Client.exceptions.UserNotConfirmedException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


    :return: {
        'UserConfirmationNecessary': True|False
    }
    
    
    :returns: 
    CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
    CognitoIdentityProvider.Client.exceptions.InvalidParameterException
    CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
    CognitoIdentityProvider.Client.exceptions.InvalidPasswordException
    CognitoIdentityProvider.Client.exceptions.InvalidLambdaResponseException
    CognitoIdentityProvider.Client.exceptions.UsernameExistsException
    CognitoIdentityProvider.Client.exceptions.InvalidUserPoolConfigurationException
    CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
    CognitoIdentityProvider.Client.exceptions.PasswordResetRequiredException
    CognitoIdentityProvider.Client.exceptions.UserNotFoundException
    CognitoIdentityProvider.Client.exceptions.UserNotConfirmedException
    CognitoIdentityProvider.Client.exceptions.InternalErrorException
    
    """
    pass

def confirm_forgot_password(ClientId=None, SecretHash=None, Username=None, ConfirmationCode=None, Password=None, AnalyticsMetadata=None, UserContextData=None, ClientMetadata=None):
    """
    Allows a user to enter a confirmation code to reset a forgotten password.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.confirm_forgot_password(
        ClientId='string',
        SecretHash='string',
        Username='string',
        ConfirmationCode='string',
        Password='string',
        AnalyticsMetadata={
            'AnalyticsEndpointId': 'string'
        },
        UserContextData={
            'EncodedData': 'string'
        },
        ClientMetadata={
            'string': 'string'
        }
    )
    
    
    :type ClientId: string
    :param ClientId: [REQUIRED]\nThe app client ID of the app associated with the user pool.\n

    :type SecretHash: string
    :param SecretHash: A keyed-hash message authentication code (HMAC) calculated using the secret key of a user pool client and username plus the client ID in the message.

    :type Username: string
    :param Username: [REQUIRED]\nThe user name of the user for whom you want to enter a code to retrieve a forgotten password.\n

    :type ConfirmationCode: string
    :param ConfirmationCode: [REQUIRED]\nThe confirmation code sent by a user\'s request to retrieve a forgotten password. For more information, see\n

    :type Password: string
    :param Password: [REQUIRED]\nThe password sent by a user\'s request to retrieve a forgotten password.\n

    :type AnalyticsMetadata: dict
    :param AnalyticsMetadata: The Amazon Pinpoint analytics metadata for collecting metrics for ConfirmForgotPassword calls.\n\nAnalyticsEndpointId (string) --The endpoint ID.\n\n\n

    :type UserContextData: dict
    :param UserContextData: Contextual data such as the user\'s device fingerprint, IP address, or location used for evaluating the risk of an unexpected event by Amazon Cognito advanced security.\n\nEncodedData (string) --Contextual data such as the user\'s device fingerprint, IP address, or location used for evaluating the risk of an unexpected event by Amazon Cognito advanced security.\n\n\n

    :type ClientMetadata: dict
    :param ClientMetadata: A map of custom key-value pairs that you can provide as input for any custom workflows that this action triggers.\nYou create custom workflows by assigning AWS Lambda functions to user pool triggers. When you use the ConfirmForgotPassword API action, Amazon Cognito invokes the function that is assigned to the post confirmation trigger. When Amazon Cognito invokes this function, it passes a JSON payload, which the function receives as input. This payload contains a clientMetadata attribute, which provides the data that you assigned to the ClientMetadata parameter in your ConfirmForgotPassword request. In your function code in AWS Lambda, you can process the clientMetadata value to enhance your workflow for your specific needs.\nFor more information, see Customizing User Pool Workflows with Lambda Triggers in the Amazon Cognito Developer Guide .\n\nNote\nTake the following limitations into consideration when you use the ClientMetadata parameter:\n\nAmazon Cognito does not store the ClientMetadata value. This data is available only to AWS Lambda triggers that are assigned to a user pool to support custom workflows. If your user pool configuration does not include triggers, the ClientMetadata parameter serves no purpose.\nAmazon Cognito does not validate the ClientMetadata value.\nAmazon Cognito does not encrypt the the ClientMetadata value, so don\'t use it to provide sensitive information.\n\n\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
The response from the server that results from a user\'s request to retrieve a forgotten password.





Exceptions

CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.UnexpectedLambdaException
CognitoIdentityProvider.Client.exceptions.UserLambdaValidationException
CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.InvalidPasswordException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.CodeMismatchException
CognitoIdentityProvider.Client.exceptions.ExpiredCodeException
CognitoIdentityProvider.Client.exceptions.TooManyFailedAttemptsException
CognitoIdentityProvider.Client.exceptions.InvalidLambdaResponseException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.LimitExceededException
CognitoIdentityProvider.Client.exceptions.UserNotFoundException
CognitoIdentityProvider.Client.exceptions.UserNotConfirmedException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


    :return: {}
    
    
    :returns: 
    CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
    CognitoIdentityProvider.Client.exceptions.UnexpectedLambdaException
    CognitoIdentityProvider.Client.exceptions.UserLambdaValidationException
    CognitoIdentityProvider.Client.exceptions.InvalidParameterException
    CognitoIdentityProvider.Client.exceptions.InvalidPasswordException
    CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
    CognitoIdentityProvider.Client.exceptions.CodeMismatchException
    CognitoIdentityProvider.Client.exceptions.ExpiredCodeException
    CognitoIdentityProvider.Client.exceptions.TooManyFailedAttemptsException
    CognitoIdentityProvider.Client.exceptions.InvalidLambdaResponseException
    CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
    CognitoIdentityProvider.Client.exceptions.LimitExceededException
    CognitoIdentityProvider.Client.exceptions.UserNotFoundException
    CognitoIdentityProvider.Client.exceptions.UserNotConfirmedException
    CognitoIdentityProvider.Client.exceptions.InternalErrorException
    
    """
    pass

def confirm_sign_up(ClientId=None, SecretHash=None, Username=None, ConfirmationCode=None, ForceAliasCreation=None, AnalyticsMetadata=None, UserContextData=None, ClientMetadata=None):
    """
    Confirms registration of a user and handles the existing alias from a previous user.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.confirm_sign_up(
        ClientId='string',
        SecretHash='string',
        Username='string',
        ConfirmationCode='string',
        ForceAliasCreation=True|False,
        AnalyticsMetadata={
            'AnalyticsEndpointId': 'string'
        },
        UserContextData={
            'EncodedData': 'string'
        },
        ClientMetadata={
            'string': 'string'
        }
    )
    
    
    :type ClientId: string
    :param ClientId: [REQUIRED]\nThe ID of the app client associated with the user pool.\n

    :type SecretHash: string
    :param SecretHash: A keyed-hash message authentication code (HMAC) calculated using the secret key of a user pool client and username plus the client ID in the message.

    :type Username: string
    :param Username: [REQUIRED]\nThe user name of the user whose registration you wish to confirm.\n

    :type ConfirmationCode: string
    :param ConfirmationCode: [REQUIRED]\nThe confirmation code sent by a user\'s request to confirm registration.\n

    :type ForceAliasCreation: boolean
    :param ForceAliasCreation: Boolean to be specified to force user confirmation irrespective of existing alias. By default set to False . If this parameter is set to True and the phone number/email used for sign up confirmation already exists as an alias with a different user, the API call will migrate the alias from the previous user to the newly created user being confirmed. If set to False , the API will throw an AliasExistsException error.

    :type AnalyticsMetadata: dict
    :param AnalyticsMetadata: The Amazon Pinpoint analytics metadata for collecting metrics for ConfirmSignUp calls.\n\nAnalyticsEndpointId (string) --The endpoint ID.\n\n\n

    :type UserContextData: dict
    :param UserContextData: Contextual data such as the user\'s device fingerprint, IP address, or location used for evaluating the risk of an unexpected event by Amazon Cognito advanced security.\n\nEncodedData (string) --Contextual data such as the user\'s device fingerprint, IP address, or location used for evaluating the risk of an unexpected event by Amazon Cognito advanced security.\n\n\n

    :type ClientMetadata: dict
    :param ClientMetadata: A map of custom key-value pairs that you can provide as input for any custom workflows that this action triggers.\nYou create custom workflows by assigning AWS Lambda functions to user pool triggers. When you use the ConfirmSignUp API action, Amazon Cognito invokes the function that is assigned to the post confirmation trigger. When Amazon Cognito invokes this function, it passes a JSON payload, which the function receives as input. This payload contains a clientMetadata attribute, which provides the data that you assigned to the ClientMetadata parameter in your ConfirmSignUp request. In your function code in AWS Lambda, you can process the clientMetadata value to enhance your workflow for your specific needs.\nFor more information, see Customizing User Pool Workflows with Lambda Triggers in the Amazon Cognito Developer Guide .\n\nNote\nTake the following limitations into consideration when you use the ClientMetadata parameter:\n\nAmazon Cognito does not store the ClientMetadata value. This data is available only to AWS Lambda triggers that are assigned to a user pool to support custom workflows. If your user pool configuration does not include triggers, the ClientMetadata parameter serves no purpose.\nAmazon Cognito does not validate the ClientMetadata value.\nAmazon Cognito does not encrypt the the ClientMetadata value, so don\'t use it to provide sensitive information.\n\n\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
Represents the response from the server for the registration confirmation.





Exceptions

CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.UnexpectedLambdaException
CognitoIdentityProvider.Client.exceptions.UserLambdaValidationException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.TooManyFailedAttemptsException
CognitoIdentityProvider.Client.exceptions.CodeMismatchException
CognitoIdentityProvider.Client.exceptions.ExpiredCodeException
CognitoIdentityProvider.Client.exceptions.InvalidLambdaResponseException
CognitoIdentityProvider.Client.exceptions.AliasExistsException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.LimitExceededException
CognitoIdentityProvider.Client.exceptions.UserNotFoundException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


    :return: {}
    
    
    :returns: 
    CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
    CognitoIdentityProvider.Client.exceptions.InvalidParameterException
    CognitoIdentityProvider.Client.exceptions.UnexpectedLambdaException
    CognitoIdentityProvider.Client.exceptions.UserLambdaValidationException
    CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
    CognitoIdentityProvider.Client.exceptions.TooManyFailedAttemptsException
    CognitoIdentityProvider.Client.exceptions.CodeMismatchException
    CognitoIdentityProvider.Client.exceptions.ExpiredCodeException
    CognitoIdentityProvider.Client.exceptions.InvalidLambdaResponseException
    CognitoIdentityProvider.Client.exceptions.AliasExistsException
    CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
    CognitoIdentityProvider.Client.exceptions.LimitExceededException
    CognitoIdentityProvider.Client.exceptions.UserNotFoundException
    CognitoIdentityProvider.Client.exceptions.InternalErrorException
    
    """
    pass

def create_group(GroupName=None, UserPoolId=None, Description=None, RoleArn=None, Precedence=None):
    """
    Creates a new group in the specified user pool.
    Calling this action requires developer credentials.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_group(
        GroupName='string',
        UserPoolId='string',
        Description='string',
        RoleArn='string',
        Precedence=123
    )
    
    
    :type GroupName: string
    :param GroupName: [REQUIRED]\nThe name of the group. Must be unique.\n

    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID for the user pool.\n

    :type Description: string
    :param Description: A string containing the description of the group.

    :type RoleArn: string
    :param RoleArn: The role ARN for the group.

    :type Precedence: integer
    :param Precedence: A nonnegative integer value that specifies the precedence of this group relative to the other groups that a user can belong to in the user pool. Zero is the highest precedence value. Groups with lower Precedence values take precedence over groups with higher or null Precedence values. If a user belongs to two or more groups, it is the group with the lowest precedence value whose role ARN will be used in the cognito:roles and cognito:preferred_role claims in the user\'s tokens.\nTwo groups can have the same Precedence value. If this happens, neither group takes precedence over the other. If two groups with the same Precedence have the same role ARN, that role is used in the cognito:preferred_role claim in tokens for users in each group. If the two groups have different role ARNs, the cognito:preferred_role claim is not set in users\' tokens.\nThe default Precedence value is null.\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

Group (dict) --
The group object for the group.

GroupName (string) --
The name of the group.

UserPoolId (string) --
The user pool ID for the user pool.

Description (string) --
A string containing the description of the group.

RoleArn (string) --
The role ARN for the group.

Precedence (integer) --
A nonnegative integer value that specifies the precedence of this group relative to the other groups that a user can belong to in the user pool. If a user belongs to two or more groups, it is the group with the highest precedence whose role ARN will be used in the cognito:roles and cognito:preferred_role claims in the user\'s tokens. Groups with higher Precedence values take precedence over groups with lower Precedence values or with null Precedence values.
Two groups can have the same Precedence value. If this happens, neither group takes precedence over the other. If two groups with the same Precedence have the same role ARN, that role is used in the cognito:preferred_role claim in tokens for users in each group. If the two groups have different role ARNs, the cognito:preferred_role claim is not set in users\' tokens.
The default Precedence value is null.

LastModifiedDate (datetime) --
The date the group was last modified.

CreationDate (datetime) --
The date the group was created.









Exceptions

CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.GroupExistsException
CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.LimitExceededException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


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
    
    
    :returns: 
    CognitoIdentityProvider.Client.exceptions.InvalidParameterException
    CognitoIdentityProvider.Client.exceptions.GroupExistsException
    CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
    CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
    CognitoIdentityProvider.Client.exceptions.LimitExceededException
    CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
    CognitoIdentityProvider.Client.exceptions.InternalErrorException
    
    """
    pass

def create_identity_provider(UserPoolId=None, ProviderName=None, ProviderType=None, ProviderDetails=None, AttributeMapping=None, IdpIdentifiers=None):
    """
    Creates an identity provider for a user pool.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_identity_provider(
        UserPoolId='string',
        ProviderName='string',
        ProviderType='SAML'|'Facebook'|'Google'|'LoginWithAmazon'|'SignInWithApple'|'OIDC',
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
    :param UserPoolId: [REQUIRED]\nThe user pool ID.\n

    :type ProviderName: string
    :param ProviderName: [REQUIRED]\nThe identity provider name.\n

    :type ProviderType: string
    :param ProviderType: [REQUIRED]\nThe identity provider type.\n

    :type ProviderDetails: dict
    :param ProviderDetails: [REQUIRED]\nThe identity provider details. The following list describes the provider detail keys for each identity provider type.\n\nFor Google, Facebook and Login with Amazon:\nclient_id\nclient_secret\nauthorize_scopes\n\n\nFor Sign in with Apple:\nclient_id\nteam_id\nkey_id\nprivate_key\nauthorize_scopes\n\n\nFor OIDC providers:\nclient_id\nclient_secret\nattributes_request_method\noidc_issuer\nauthorize_scopes\nauthorize_url if not available from discovery URL specified by oidc_issuer key\ntoken_url if not available from discovery URL specified by oidc_issuer key\nattributes_url if not available from discovery URL specified by oidc_issuer key\njwks_uri if not available from discovery URL specified by oidc_issuer key\nauthorize_scopes\n\n\nFor SAML providers:\nMetadataFile OR MetadataURL\nIDPSignout optional\n\n\n\n\n(string) --\n(string) --\n\n\n\n

    :type AttributeMapping: dict
    :param AttributeMapping: A mapping of identity provider attributes to standard and custom user pool attributes.\n\n(string) --\n(string) --\n\n\n\n

    :type IdpIdentifiers: list
    :param IdpIdentifiers: A list of identity provider identifiers.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'IdentityProvider': {
        'UserPoolId': 'string',
        'ProviderName': 'string',
        'ProviderType': 'SAML'|'Facebook'|'Google'|'LoginWithAmazon'|'SignInWithApple'|'OIDC',
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


Response Structure

(dict) --

IdentityProvider (dict) --
The newly created identity provider object.

UserPoolId (string) --
The user pool ID.

ProviderName (string) --
The identity provider name.

ProviderType (string) --
The identity provider type.

ProviderDetails (dict) --
The identity provider details. The following list describes the provider detail keys for each identity provider type.

For Google, Facebook and Login with Amazon:
client_id
client_secret
authorize_scopes


For Sign in with Apple:
client_id
team_id
key_id
private_key
authorize_scopes


For OIDC providers:
client_id
client_secret
attributes_request_method
oidc_issuer
authorize_scopes
authorize_url if not available from discovery URL specified by oidc_issuer key
token_url if not available from discovery URL specified by oidc_issuer key
attributes_url if not available from discovery URL specified by oidc_issuer key
jwks_uri if not available from discovery URL specified by oidc_issuer key
authorize_scopes


For SAML providers:
MetadataFile OR MetadataURL
IDPSignOut optional




(string) --
(string) --




AttributeMapping (dict) --
A mapping of identity provider attributes to standard and custom user pool attributes.

(string) --
(string) --




IdpIdentifiers (list) --
A list of identity provider identifiers.

(string) --


LastModifiedDate (datetime) --
The date the identity provider was last modified.

CreationDate (datetime) --
The date the identity provider was created.









Exceptions

CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.DuplicateProviderException
CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.LimitExceededException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


    :return: {
        'IdentityProvider': {
            'UserPoolId': 'string',
            'ProviderName': 'string',
            'ProviderType': 'SAML'|'Facebook'|'Google'|'LoginWithAmazon'|'SignInWithApple'|'OIDC',
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
    For Google, Facebook and Login with Amazon:
    client_id
    client_secret
    authorize_scopes
    
    
    For Sign in with Apple:
    client_id
    team_id
    key_id
    private_key
    authorize_scopes
    
    
    For OIDC providers:
    client_id
    client_secret
    attributes_request_method
    oidc_issuer
    authorize_scopes
    authorize_url if not available from discovery URL specified by oidc_issuer key
    token_url if not available from discovery URL specified by oidc_issuer key
    attributes_url if not available from discovery URL specified by oidc_issuer key
    jwks_uri if not available from discovery URL specified by oidc_issuer key
    authorize_scopes
    
    
    For SAML providers:
    MetadataFile OR MetadataURL
    IDPSignOut optional
    
    
    
    """
    pass

def create_resource_server(UserPoolId=None, Identifier=None, Name=None, Scopes=None):
    """
    Creates a new OAuth2.0 resource server and defines custom scopes in it.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_resource_server(
        UserPoolId='string',
        Identifier='string',
        Name='string',
        Scopes=[
            {
                'ScopeName': 'string',
                'ScopeDescription': 'string'
            },
        ]
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID for the user pool.\n

    :type Identifier: string
    :param Identifier: [REQUIRED]\nA unique resource server identifier for the resource server. This could be an HTTPS endpoint where the resource server is located. For example, https://my-weather-api.example.com .\n

    :type Name: string
    :param Name: [REQUIRED]\nA friendly name for the resource server.\n

    :type Scopes: list
    :param Scopes: A list of scopes. Each scope is map, where the keys are name and description .\n\n(dict) --A resource server scope.\n\nScopeName (string) -- [REQUIRED]The name of the scope.\n\nScopeDescription (string) -- [REQUIRED]A description of the scope.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ResourceServer': {
        'UserPoolId': 'string',
        'Identifier': 'string',
        'Name': 'string',
        'Scopes': [
            {
                'ScopeName': 'string',
                'ScopeDescription': 'string'
            },
        ]
    }
}


Response Structure

(dict) --

ResourceServer (dict) --
The newly created resource server.

UserPoolId (string) --
The user pool ID for the user pool that hosts the resource server.

Identifier (string) --
The identifier for the resource server.

Name (string) --
The name of the resource server.

Scopes (list) --
A list of scopes that are defined for the resource server.

(dict) --
A resource server scope.

ScopeName (string) --
The name of the scope.

ScopeDescription (string) --
A description of the scope.













Exceptions

CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.LimitExceededException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


    :return: {
        'ResourceServer': {
            'UserPoolId': 'string',
            'Identifier': 'string',
            'Name': 'string',
            'Scopes': [
                {
                    'ScopeName': 'string',
                    'ScopeDescription': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    CognitoIdentityProvider.Client.exceptions.InvalidParameterException
    CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
    CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
    CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
    CognitoIdentityProvider.Client.exceptions.LimitExceededException
    CognitoIdentityProvider.Client.exceptions.InternalErrorException
    
    """
    pass

def create_user_import_job(JobName=None, UserPoolId=None, CloudWatchLogsRoleArn=None):
    """
    Creates the user import job.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_user_import_job(
        JobName='string',
        UserPoolId='string',
        CloudWatchLogsRoleArn='string'
    )
    
    
    :type JobName: string
    :param JobName: [REQUIRED]\nThe job name for the user import job.\n

    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID for the user pool that the users are being imported into.\n

    :type CloudWatchLogsRoleArn: string
    :param CloudWatchLogsRoleArn: [REQUIRED]\nThe role ARN for the Amazon CloudWatch Logging role for the user import job.\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --
Represents the response from the server to the request to create the user import job.

UserImportJob (dict) --
The job object that represents the user import job.

JobName (string) --
The job name for the user import job.

JobId (string) --
The job ID for the user import job.

UserPoolId (string) --
The user pool ID for the user pool that the users are being imported into.

PreSignedUrl (string) --
The pre-signed URL to be used to upload the .csv file.

CreationDate (datetime) --
The date the user import job was created.

StartDate (datetime) --
The date when the user import job was started.

CompletionDate (datetime) --
The date when the user import job was completed.

Status (string) --
The status of the user import job. One of the following:

Created - The job was created but not started.
Pending - A transition state. You have started the job, but it has not begun importing users yet.
InProgress - The job has started, and users are being imported.
Stopping - You have stopped the job, but the job has not stopped importing users yet.
Stopped - You have stopped the job, and the job has stopped importing users.
Succeeded - The job has completed successfully.
Failed - The job has stopped due to an error.
Expired - You created a job, but did not start the job within 24-48 hours. All data associated with the job was deleted, and the job cannot be started.


CloudWatchLogsRoleArn (string) --
The role ARN for the Amazon CloudWatch Logging role for the user import job. For more information, see "Creating the CloudWatch Logs IAM Role" in the Amazon Cognito Developer Guide.

ImportedUsers (integer) --
The number of users that were successfully imported.

SkippedUsers (integer) --
The number of users that were skipped.

FailedUsers (integer) --
The number of users that could not be imported.

CompletionMessage (string) --
The message returned when the user import job is completed.









Exceptions

CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.PreconditionNotMetException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.LimitExceededException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


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

def create_user_pool(PoolName=None, Policies=None, LambdaConfig=None, AutoVerifiedAttributes=None, AliasAttributes=None, UsernameAttributes=None, SmsVerificationMessage=None, EmailVerificationMessage=None, EmailVerificationSubject=None, VerificationMessageTemplate=None, SmsAuthenticationMessage=None, MfaConfiguration=None, DeviceConfiguration=None, EmailConfiguration=None, SmsConfiguration=None, UserPoolTags=None, AdminCreateUserConfig=None, Schema=None, UserPoolAddOns=None, UsernameConfiguration=None, AccountRecoverySetting=None):
    """
    Creates a new Amazon Cognito user pool and sets the password policy for the pool.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_user_pool(
        PoolName='string',
        Policies={
            'PasswordPolicy': {
                'MinimumLength': 123,
                'RequireUppercase': True|False,
                'RequireLowercase': True|False,
                'RequireNumbers': True|False,
                'RequireSymbols': True|False,
                'TemporaryPasswordValidityDays': 123
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
            'VerifyAuthChallengeResponse': 'string',
            'PreTokenGeneration': 'string',
            'UserMigration': 'string'
        },
        AutoVerifiedAttributes=[
            'phone_number'|'email',
        ],
        AliasAttributes=[
            'phone_number'|'email'|'preferred_username',
        ],
        UsernameAttributes=[
            'phone_number'|'email',
        ],
        SmsVerificationMessage='string',
        EmailVerificationMessage='string',
        EmailVerificationSubject='string',
        VerificationMessageTemplate={
            'SmsMessage': 'string',
            'EmailMessage': 'string',
            'EmailSubject': 'string',
            'EmailMessageByLink': 'string',
            'EmailSubjectByLink': 'string',
            'DefaultEmailOption': 'CONFIRM_WITH_LINK'|'CONFIRM_WITH_CODE'
        },
        SmsAuthenticationMessage='string',
        MfaConfiguration='OFF'|'ON'|'OPTIONAL',
        DeviceConfiguration={
            'ChallengeRequiredOnNewDevice': True|False,
            'DeviceOnlyRememberedOnUserPrompt': True|False
        },
        EmailConfiguration={
            'SourceArn': 'string',
            'ReplyToEmailAddress': 'string',
            'EmailSendingAccount': 'COGNITO_DEFAULT'|'DEVELOPER',
            'From': 'string',
            'ConfigurationSet': 'string'
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
        ],
        UserPoolAddOns={
            'AdvancedSecurityMode': 'OFF'|'AUDIT'|'ENFORCED'
        },
        UsernameConfiguration={
            'CaseSensitive': True|False
        },
        AccountRecoverySetting={
            'RecoveryMechanisms': [
                {
                    'Priority': 123,
                    'Name': 'verified_email'|'verified_phone_number'|'admin_only'
                },
            ]
        }
    )
    
    
    :type PoolName: string
    :param PoolName: [REQUIRED]\nA string used to name the user pool.\n

    :type Policies: dict
    :param Policies: The policies associated with the new user pool.\n\nPasswordPolicy (dict) --The password policy.\n\nMinimumLength (integer) --The minimum length of the password policy that you have set. Cannot be less than 6.\n\nRequireUppercase (boolean) --In the password policy that you have set, refers to whether you have required users to use at least one uppercase letter in their password.\n\nRequireLowercase (boolean) --In the password policy that you have set, refers to whether you have required users to use at least one lowercase letter in their password.\n\nRequireNumbers (boolean) --In the password policy that you have set, refers to whether you have required users to use at least one number in their password.\n\nRequireSymbols (boolean) --In the password policy that you have set, refers to whether you have required users to use at least one symbol in their password.\n\nTemporaryPasswordValidityDays (integer) --In the password policy you have set, refers to the number of days a temporary password is valid. If the user does not sign-in during this time, their password will need to be reset by an administrator.\n\nNote\nWhen you set TemporaryPasswordValidityDays for a user pool, you will no longer be able to set the deprecated UnusedAccountValidityDays value for that user pool.\n\n\n\n\n\n

    :type LambdaConfig: dict
    :param LambdaConfig: The Lambda trigger configuration information for the new user pool.\n\nNote\nIn a push model, event sources (such as Amazon S3 and custom applications) need permission to invoke a function. So you will need to make an extra call to add permission for these event sources to invoke your Lambda function.\nFor more information on using the Lambda API to add permission, see AddPermission .\nFor adding permission using the AWS CLI, see add-permission .\n\n\nPreSignUp (string) --A pre-registration AWS Lambda trigger.\n\nCustomMessage (string) --A custom Message AWS Lambda trigger.\n\nPostConfirmation (string) --A post-confirmation AWS Lambda trigger.\n\nPreAuthentication (string) --A pre-authentication AWS Lambda trigger.\n\nPostAuthentication (string) --A post-authentication AWS Lambda trigger.\n\nDefineAuthChallenge (string) --Defines the authentication challenge.\n\nCreateAuthChallenge (string) --Creates an authentication challenge.\n\nVerifyAuthChallengeResponse (string) --Verifies the authentication challenge response.\n\nPreTokenGeneration (string) --A Lambda trigger that is invoked before token generation.\n\nUserMigration (string) --The user migration Lambda config type.\n\n\n

    :type AutoVerifiedAttributes: list
    :param AutoVerifiedAttributes: The attributes to be auto-verified. Possible values: email , phone_number .\n\n(string) --\n\n

    :type AliasAttributes: list
    :param AliasAttributes: Attributes supported as an alias for this user pool. Possible values: phone_number , email , or preferred_username .\n\n(string) --\n\n

    :type UsernameAttributes: list
    :param UsernameAttributes: Specifies whether email addresses or phone numbers can be specified as usernames when a user signs up.\n\n(string) --\n\n

    :type SmsVerificationMessage: string
    :param SmsVerificationMessage: A string representing the SMS verification message.

    :type EmailVerificationMessage: string
    :param EmailVerificationMessage: A string representing the email verification message.

    :type EmailVerificationSubject: string
    :param EmailVerificationSubject: A string representing the email verification subject.

    :type VerificationMessageTemplate: dict
    :param VerificationMessageTemplate: The template for the verification message that the user sees when the app requests permission to access the user\'s information.\n\nSmsMessage (string) --The SMS message template.\n\nEmailMessage (string) --The email message template.\n\nEmailSubject (string) --The subject line for the email message template.\n\nEmailMessageByLink (string) --The email message template for sending a confirmation link to the user.\n\nEmailSubjectByLink (string) --The subject line for the email message template for sending a confirmation link to the user.\n\nDefaultEmailOption (string) --The default email option.\n\n\n

    :type SmsAuthenticationMessage: string
    :param SmsAuthenticationMessage: A string representing the SMS authentication message.

    :type MfaConfiguration: string
    :param MfaConfiguration: Specifies MFA configuration details.

    :type DeviceConfiguration: dict
    :param DeviceConfiguration: The device configuration.\n\nChallengeRequiredOnNewDevice (boolean) --Indicates whether a challenge is required on a new device. Only applicable to a new device.\n\nDeviceOnlyRememberedOnUserPrompt (boolean) --If true, a device is only remembered on user prompt.\n\n\n

    :type EmailConfiguration: dict
    :param EmailConfiguration: The email configuration.\n\nSourceArn (string) --The Amazon Resource Name (ARN) of a verified email address in Amazon SES. This email address is used in one of the following ways, depending on the value that you specify for the EmailSendingAccount parameter:\n\nIf you specify COGNITO_DEFAULT , Amazon Cognito uses this address as the custom FROM address when it emails your users by using its built-in email account.\nIf you specify DEVELOPER , Amazon Cognito emails your users with this address by calling Amazon SES on your behalf.\n\n\nReplyToEmailAddress (string) --The destination to which the receiver of the email should reply to.\n\nEmailSendingAccount (string) --Specifies whether Amazon Cognito emails your users by using its built-in email functionality or your Amazon SES email configuration. Specify one of the following values:\n\nCOGNITO_DEFAULT\nWhen Amazon Cognito emails your users, it uses its built-in email functionality. When you use the default option, Amazon Cognito allows only a limited number of emails each day for your user pool. For typical production environments, the default email limit is below the required delivery volume. To achieve a higher delivery volume, specify DEVELOPER to use your Amazon SES email configuration.\nTo look up the email delivery limit for the default option, see Limits in Amazon Cognito in the Amazon Cognito Developer Guide .\nThe default FROM address is no-reply@verificationemail.com. To customize the FROM address, provide the ARN of an Amazon SES verified email address for the SourceArn parameter.\n\nDEVELOPER\nWhen Amazon Cognito emails your users, it uses your Amazon SES configuration. Amazon Cognito calls Amazon SES on your behalf to send email from your verified email address. When you use this option, the email delivery limits are the same limits that apply to your Amazon SES verified email address in your AWS account.\nIf you use this option, you must provide the ARN of an Amazon SES verified email address for the SourceArn parameter.\nBefore Amazon Cognito can email your users, it requires additional permissions to call Amazon SES on your behalf. When you update your user pool with this option, Amazon Cognito creates a service-linked role , which is a type of IAM role, in your AWS account. This role contains the permissions that allow Amazon Cognito to access Amazon SES and send email messages with your address. For more information about the service-linked role that Amazon Cognito creates, see Using Service-Linked Roles for Amazon Cognito in the Amazon Cognito Developer Guide .\n\nFrom (string) --Identifies either the sender\xe2\x80\x99s email address or the sender\xe2\x80\x99s name with their email address. For example, testuser@example.com or Test User <testuser@example.com> . This address will appear before the body of the email.\n\nConfigurationSet (string) --The set of configuration rules that can be applied to emails sent using Amazon SES. A configuration set is applied to an email by including a reference to the configuration set in the headers of the email. Once applied, all of the rules in that configuration set are applied to the email. Configuration sets can be used to apply the following types of rules to emails:\n\nEvent publishing \xe2\x80\x93 Amazon SES can track the number of send, delivery, open, click, bounce, and complaint events for each email sent. Use event publishing to send information about these events to other AWS services such as SNS and CloudWatch.\nIP pool management \xe2\x80\x93 When leasing dedicated IP addresses with Amazon SES, you can create groups of IP addresses, called dedicated IP pools. You can then associate the dedicated IP pools with configuration sets.\n\n\n\n

    :type SmsConfiguration: dict
    :param SmsConfiguration: The SMS configuration.\n\nSnsCallerArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) caller. This is the ARN of the IAM role in your AWS account which Cognito will use to send SMS messages.\n\nExternalId (string) --The external ID is a value that we recommend you use to add security to your IAM role which is used to call Amazon SNS to send SMS messages for your user pool. If you provide an ExternalId , the Cognito User Pool will include it when attempting to assume your IAM role, so that you can set your roles trust policy to require the ExternalID . If you use the Cognito Management Console to create a role for SMS MFA, Cognito will create a role with the required permissions and a trust policy that demonstrates use of the ExternalId .\n\n\n

    :type UserPoolTags: dict
    :param UserPoolTags: The tag keys and values to assign to the user pool. A tag is a label that you can use to categorize and manage user pools in different ways, such as by purpose, owner, environment, or other criteria.\n\n(string) --\n(string) --\n\n\n\n

    :type AdminCreateUserConfig: dict
    :param AdminCreateUserConfig: The configuration for AdminCreateUser requests.\n\nAllowAdminCreateUserOnly (boolean) --Set to True if only the administrator is allowed to create user profiles. Set to False if users can sign themselves up via an app.\n\nUnusedAccountValidityDays (integer) --The user account expiration limit, in days, after which the account is no longer usable. To reset the account after that time limit, you must call AdminCreateUser again, specifying 'RESEND' for the MessageAction parameter. The default value for this parameter is 7.\n\nNote\nIf you set a value for TemporaryPasswordValidityDays in PasswordPolicy , that value will be used and UnusedAccountValidityDays will be deprecated for that user pool.\n\n\nInviteMessageTemplate (dict) --The message template to be used for the welcome message to new users.\nSee also Customizing User Invitation Messages .\n\nSMSMessage (string) --The message template for SMS messages.\n\nEmailMessage (string) --The message template for email messages.\n\nEmailSubject (string) --The subject line for email messages.\n\n\n\n\n

    :type Schema: list
    :param Schema: An array of schema attributes for the new user pool. These attributes can be standard or custom attributes.\n\n(dict) --Contains information about the schema attribute.\n\nName (string) --A schema attribute of the name type.\n\nAttributeDataType (string) --The attribute data type.\n\nDeveloperOnlyAttribute (boolean) --\nNote\nWe recommend that you use WriteAttributes in the user pool client to control how attributes can be mutated for new use cases instead of using DeveloperOnlyAttribute .\n\nSpecifies whether the attribute type is developer only. This attribute can only be modified by an administrator. Users will not be able to modify this attribute using their access token. For example, DeveloperOnlyAttribute can be modified using the API but cannot be updated using the API.\n\nMutable (boolean) --Specifies whether the value of the attribute can be changed.\nFor any user pool attribute that\'s mapped to an identity provider attribute, you must set this parameter to true . Amazon Cognito updates mapped attributes when users sign in to your application through an identity provider. If an attribute is immutable, Amazon Cognito throws an error when it attempts to update the attribute. For more information, see Specifying Identity Provider Attribute Mappings for Your User Pool .\n\nRequired (boolean) --Specifies whether a user pool attribute is required. If the attribute is required and the user does not provide a value, registration or sign-in will fail.\n\nNumberAttributeConstraints (dict) --Specifies the constraints for an attribute of the number type.\n\nMinValue (string) --The minimum value of an attribute that is of the number data type.\n\nMaxValue (string) --The maximum value of an attribute that is of the number data type.\n\n\n\nStringAttributeConstraints (dict) --Specifies the constraints for an attribute of the string type.\n\nMinLength (string) --The minimum length.\n\nMaxLength (string) --The maximum length.\n\n\n\n\n\n\n

    :type UserPoolAddOns: dict
    :param UserPoolAddOns: Used to enable advanced security risk detection. Set the key AdvancedSecurityMode to the value 'AUDIT'.\n\nAdvancedSecurityMode (string) -- [REQUIRED]The advanced security mode.\n\n\n

    :type UsernameConfiguration: dict
    :param UsernameConfiguration: You can choose to set case sensitivity on the username input for the selected sign-in option. For example, when this is set to False , users will be able to sign in using either 'username' or 'Username'. This configuration is immutable once it has been set. For more information, see .\n\nCaseSensitive (boolean) -- [REQUIRED]Specifies whether username case sensitivity will be applied for all users in the user pool through Cognito APIs.\nValid values include:\n\n**True ** : Enables case sensitivity for all username input. When this option is set to True , users must sign in using the exact capitalization of their given username. For example, \xe2\x80\x9cUserName\xe2\x80\x9d. This is the default value.\n**False ** : Enables case insensitivity for all username input. For example, when this option is set to False , users will be able to sign in using either 'username' or 'Username'. This option also enables both preferred_username and email alias to be case insensitive, in addition to the username attribute.\n\n\n\n

    :type AccountRecoverySetting: dict
    :param AccountRecoverySetting: Use this setting to define which verified available method a user can use to recover their password when they call ForgotPassword . It allows you to define a preferred method when a user has more than one method available. With this setting, SMS does not qualify for a valid password recovery mechanism if the user also has SMS MFA enabled. In the absence of this setting, Cognito uses the legacy behavior to determine the recovery method where SMS is preferred over email.\n\nNote\nStarting February 1, 2020, the value of AccountRecoverySetting will default to verified_email first and verified_phone_number as the second option for newly created user pools if no value is provided.\n\n\nRecoveryMechanisms (list) --The list of RecoveryOptionTypes .\n\n(dict) --A map containing a priority as a key, and recovery method name as a value.\n\nPriority (integer) -- [REQUIRED]A positive integer specifying priority of a method with 1 being the highest priority.\n\nName (string) -- [REQUIRED]Specifies the recovery method for a user.\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'UserPool': {
        'Id': 'string',
        'Name': 'string',
        'Policies': {
            'PasswordPolicy': {
                'MinimumLength': 123,
                'RequireUppercase': True|False,
                'RequireLowercase': True|False,
                'RequireNumbers': True|False,
                'RequireSymbols': True|False,
                'TemporaryPasswordValidityDays': 123
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
            'VerifyAuthChallengeResponse': 'string',
            'PreTokenGeneration': 'string',
            'UserMigration': 'string'
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
        'UsernameAttributes': [
            'phone_number'|'email',
        ],
        'SmsVerificationMessage': 'string',
        'EmailVerificationMessage': 'string',
        'EmailVerificationSubject': 'string',
        'VerificationMessageTemplate': {
            'SmsMessage': 'string',
            'EmailMessage': 'string',
            'EmailSubject': 'string',
            'EmailMessageByLink': 'string',
            'EmailSubjectByLink': 'string',
            'DefaultEmailOption': 'CONFIRM_WITH_LINK'|'CONFIRM_WITH_CODE'
        },
        'SmsAuthenticationMessage': 'string',
        'MfaConfiguration': 'OFF'|'ON'|'OPTIONAL',
        'DeviceConfiguration': {
            'ChallengeRequiredOnNewDevice': True|False,
            'DeviceOnlyRememberedOnUserPrompt': True|False
        },
        'EstimatedNumberOfUsers': 123,
        'EmailConfiguration': {
            'SourceArn': 'string',
            'ReplyToEmailAddress': 'string',
            'EmailSendingAccount': 'COGNITO_DEFAULT'|'DEVELOPER',
            'From': 'string',
            'ConfigurationSet': 'string'
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
        'Domain': 'string',
        'CustomDomain': 'string',
        'AdminCreateUserConfig': {
            'AllowAdminCreateUserOnly': True|False,
            'UnusedAccountValidityDays': 123,
            'InviteMessageTemplate': {
                'SMSMessage': 'string',
                'EmailMessage': 'string',
                'EmailSubject': 'string'
            }
        },
        'UserPoolAddOns': {
            'AdvancedSecurityMode': 'OFF'|'AUDIT'|'ENFORCED'
        },
        'UsernameConfiguration': {
            'CaseSensitive': True|False
        },
        'Arn': 'string',
        'AccountRecoverySetting': {
            'RecoveryMechanisms': [
                {
                    'Priority': 123,
                    'Name': 'verified_email'|'verified_phone_number'|'admin_only'
                },
            ]
        }
    }
}


Response Structure

(dict) --
Represents the response from the server for the request to create a user pool.

UserPool (dict) --
A container for the user pool details.

Id (string) --
The ID of the user pool.

Name (string) --
The name of the user pool.

Policies (dict) --
The policies associated with the user pool.

PasswordPolicy (dict) --
The password policy.

MinimumLength (integer) --
The minimum length of the password policy that you have set. Cannot be less than 6.

RequireUppercase (boolean) --
In the password policy that you have set, refers to whether you have required users to use at least one uppercase letter in their password.

RequireLowercase (boolean) --
In the password policy that you have set, refers to whether you have required users to use at least one lowercase letter in their password.

RequireNumbers (boolean) --
In the password policy that you have set, refers to whether you have required users to use at least one number in their password.

RequireSymbols (boolean) --
In the password policy that you have set, refers to whether you have required users to use at least one symbol in their password.

TemporaryPasswordValidityDays (integer) --
In the password policy you have set, refers to the number of days a temporary password is valid. If the user does not sign-in during this time, their password will need to be reset by an administrator.

Note
When you set TemporaryPasswordValidityDays for a user pool, you will no longer be able to set the deprecated UnusedAccountValidityDays value for that user pool.






LambdaConfig (dict) --
The AWS Lambda triggers associated with the user pool.

PreSignUp (string) --
A pre-registration AWS Lambda trigger.

CustomMessage (string) --
A custom Message AWS Lambda trigger.

PostConfirmation (string) --
A post-confirmation AWS Lambda trigger.

PreAuthentication (string) --
A pre-authentication AWS Lambda trigger.

PostAuthentication (string) --
A post-authentication AWS Lambda trigger.

DefineAuthChallenge (string) --
Defines the authentication challenge.

CreateAuthChallenge (string) --
Creates an authentication challenge.

VerifyAuthChallengeResponse (string) --
Verifies the authentication challenge response.

PreTokenGeneration (string) --
A Lambda trigger that is invoked before token generation.

UserMigration (string) --
The user migration Lambda config type.



Status (string) --
The status of a user pool.

LastModifiedDate (datetime) --
The date the user pool was last modified.

CreationDate (datetime) --
The date the user pool was created.

SchemaAttributes (list) --
A container with the schema attributes of a user pool.

(dict) --
Contains information about the schema attribute.

Name (string) --
A schema attribute of the name type.

AttributeDataType (string) --
The attribute data type.

DeveloperOnlyAttribute (boolean) --

Note
We recommend that you use WriteAttributes in the user pool client to control how attributes can be mutated for new use cases instead of using DeveloperOnlyAttribute .

Specifies whether the attribute type is developer only. This attribute can only be modified by an administrator. Users will not be able to modify this attribute using their access token. For example, DeveloperOnlyAttribute can be modified using the API but cannot be updated using the API.

Mutable (boolean) --
Specifies whether the value of the attribute can be changed.
For any user pool attribute that\'s mapped to an identity provider attribute, you must set this parameter to true . Amazon Cognito updates mapped attributes when users sign in to your application through an identity provider. If an attribute is immutable, Amazon Cognito throws an error when it attempts to update the attribute. For more information, see Specifying Identity Provider Attribute Mappings for Your User Pool .

Required (boolean) --
Specifies whether a user pool attribute is required. If the attribute is required and the user does not provide a value, registration or sign-in will fail.

NumberAttributeConstraints (dict) --
Specifies the constraints for an attribute of the number type.

MinValue (string) --
The minimum value of an attribute that is of the number data type.

MaxValue (string) --
The maximum value of an attribute that is of the number data type.



StringAttributeConstraints (dict) --
Specifies the constraints for an attribute of the string type.

MinLength (string) --
The minimum length.

MaxLength (string) --
The maximum length.







AutoVerifiedAttributes (list) --
Specifies the attributes that are auto-verified in a user pool.

(string) --


AliasAttributes (list) --
Specifies the attributes that are aliased in a user pool.

(string) --


UsernameAttributes (list) --
Specifies whether email addresses or phone numbers can be specified as usernames when a user signs up.

(string) --


SmsVerificationMessage (string) --
The contents of the SMS verification message.

EmailVerificationMessage (string) --
The contents of the email verification message.

EmailVerificationSubject (string) --
The subject of the email verification message.

VerificationMessageTemplate (dict) --
The template for verification messages.

SmsMessage (string) --
The SMS message template.

EmailMessage (string) --
The email message template.

EmailSubject (string) --
The subject line for the email message template.

EmailMessageByLink (string) --
The email message template for sending a confirmation link to the user.

EmailSubjectByLink (string) --
The subject line for the email message template for sending a confirmation link to the user.

DefaultEmailOption (string) --
The default email option.



SmsAuthenticationMessage (string) --
The contents of the SMS authentication message.

MfaConfiguration (string) --
Can be one of the following values:

OFF - MFA tokens are not required and cannot be specified during user registration.
ON - MFA tokens are required for all user registrations. You can only specify required when you are initially creating a user pool.
OPTIONAL - Users have the option when registering to create an MFA token.


DeviceConfiguration (dict) --
The device configuration.

ChallengeRequiredOnNewDevice (boolean) --
Indicates whether a challenge is required on a new device. Only applicable to a new device.

DeviceOnlyRememberedOnUserPrompt (boolean) --
If true, a device is only remembered on user prompt.



EstimatedNumberOfUsers (integer) --
A number estimating the size of the user pool.

EmailConfiguration (dict) --
The email configuration.

SourceArn (string) --
The Amazon Resource Name (ARN) of a verified email address in Amazon SES. This email address is used in one of the following ways, depending on the value that you specify for the EmailSendingAccount parameter:

If you specify COGNITO_DEFAULT , Amazon Cognito uses this address as the custom FROM address when it emails your users by using its built-in email account.
If you specify DEVELOPER , Amazon Cognito emails your users with this address by calling Amazon SES on your behalf.


ReplyToEmailAddress (string) --
The destination to which the receiver of the email should reply to.

EmailSendingAccount (string) --
Specifies whether Amazon Cognito emails your users by using its built-in email functionality or your Amazon SES email configuration. Specify one of the following values:

COGNITO_DEFAULT

When Amazon Cognito emails your users, it uses its built-in email functionality. When you use the default option, Amazon Cognito allows only a limited number of emails each day for your user pool. For typical production environments, the default email limit is below the required delivery volume. To achieve a higher delivery volume, specify DEVELOPER to use your Amazon SES email configuration.
To look up the email delivery limit for the default option, see Limits in Amazon Cognito in the Amazon Cognito Developer Guide .
The default FROM address is no-reply@verificationemail.com. To customize the FROM address, provide the ARN of an Amazon SES verified email address for the SourceArn parameter.

DEVELOPER

When Amazon Cognito emails your users, it uses your Amazon SES configuration. Amazon Cognito calls Amazon SES on your behalf to send email from your verified email address. When you use this option, the email delivery limits are the same limits that apply to your Amazon SES verified email address in your AWS account.
If you use this option, you must provide the ARN of an Amazon SES verified email address for the SourceArn parameter.
Before Amazon Cognito can email your users, it requires additional permissions to call Amazon SES on your behalf. When you update your user pool with this option, Amazon Cognito creates a service-linked role , which is a type of IAM role, in your AWS account. This role contains the permissions that allow Amazon Cognito to access Amazon SES and send email messages with your address. For more information about the service-linked role that Amazon Cognito creates, see Using Service-Linked Roles for Amazon Cognito in the Amazon Cognito Developer Guide .

From (string) --
Identifies either the sender\xe2\x80\x99s email address or the sender\xe2\x80\x99s name with their email address. For example, testuser@example.com or Test User <testuser@example.com> . This address will appear before the body of the email.

ConfigurationSet (string) --
The set of configuration rules that can be applied to emails sent using Amazon SES. A configuration set is applied to an email by including a reference to the configuration set in the headers of the email. Once applied, all of the rules in that configuration set are applied to the email. Configuration sets can be used to apply the following types of rules to emails:

Event publishing \xe2\x80\x93 Amazon SES can track the number of send, delivery, open, click, bounce, and complaint events for each email sent. Use event publishing to send information about these events to other AWS services such as SNS and CloudWatch.
IP pool management \xe2\x80\x93 When leasing dedicated IP addresses with Amazon SES, you can create groups of IP addresses, called dedicated IP pools. You can then associate the dedicated IP pools with configuration sets.




SmsConfiguration (dict) --
The SMS configuration.

SnsCallerArn (string) --
The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) caller. This is the ARN of the IAM role in your AWS account which Cognito will use to send SMS messages.

ExternalId (string) --
The external ID is a value that we recommend you use to add security to your IAM role which is used to call Amazon SNS to send SMS messages for your user pool. If you provide an ExternalId , the Cognito User Pool will include it when attempting to assume your IAM role, so that you can set your roles trust policy to require the ExternalID . If you use the Cognito Management Console to create a role for SMS MFA, Cognito will create a role with the required permissions and a trust policy that demonstrates use of the ExternalId .



UserPoolTags (dict) --
The tags that are assigned to the user pool. A tag is a label that you can apply to user pools to categorize and manage them in different ways, such as by purpose, owner, environment, or other criteria.

(string) --
(string) --




SmsConfigurationFailure (string) --
The reason why the SMS configuration cannot send the messages to your users.

EmailConfigurationFailure (string) --
The reason why the email configuration cannot send the messages to your users.

Domain (string) --
Holds the domain prefix if the user pool has a domain associated with it.

CustomDomain (string) --
A custom domain name that you provide to Amazon Cognito. This parameter applies only if you use a custom domain to host the sign-up and sign-in pages for your application. For example: auth.example.com .
For more information about adding a custom domain to your user pool, see Using Your Own Domain for the Hosted UI .

AdminCreateUserConfig (dict) --
The configuration for AdminCreateUser requests.

AllowAdminCreateUserOnly (boolean) --
Set to True if only the administrator is allowed to create user profiles. Set to False if users can sign themselves up via an app.

UnusedAccountValidityDays (integer) --
The user account expiration limit, in days, after which the account is no longer usable. To reset the account after that time limit, you must call AdminCreateUser again, specifying "RESEND" for the MessageAction parameter. The default value for this parameter is 7.

Note
If you set a value for TemporaryPasswordValidityDays in PasswordPolicy , that value will be used and UnusedAccountValidityDays will be deprecated for that user pool.


InviteMessageTemplate (dict) --
The message template to be used for the welcome message to new users.
See also Customizing User Invitation Messages .

SMSMessage (string) --
The message template for SMS messages.

EmailMessage (string) --
The message template for email messages.

EmailSubject (string) --
The subject line for email messages.





UserPoolAddOns (dict) --
The user pool add-ons.

AdvancedSecurityMode (string) --
The advanced security mode.



UsernameConfiguration (dict) --
You can choose to enable case sensitivity on the username input for the selected sign-in option. For example, when this is set to False , users will be able to sign in using either "username" or "Username". This configuration is immutable once it has been set. For more information, see .

CaseSensitive (boolean) --
Specifies whether username case sensitivity will be applied for all users in the user pool through Cognito APIs.
Valid values include:

**True ** : Enables case sensitivity for all username input. When this option is set to True , users must sign in using the exact capitalization of their given username. For example, \xe2\x80\x9cUserName\xe2\x80\x9d. This is the default value.
**False ** : Enables case insensitivity for all username input. For example, when this option is set to False , users will be able to sign in using either "username" or "Username". This option also enables both preferred_username and email alias to be case insensitive, in addition to the username attribute.




Arn (string) --
The Amazon Resource Name (ARN) for the user pool.

AccountRecoverySetting (dict) --
Use this setting to define which verified available method a user can use to recover their password when they call ForgotPassword . It allows you to define a preferred method when a user has more than one method available. With this setting, SMS does not qualify for a valid password recovery mechanism if the user also has SMS MFA enabled. In the absence of this setting, Cognito uses the legacy behavior to determine the recovery method where SMS is preferred over email.

RecoveryMechanisms (list) --
The list of RecoveryOptionTypes .

(dict) --
A map containing a priority as a key, and recovery method name as a value.

Priority (integer) --
A positive integer specifying priority of a method with 1 being the highest priority.

Name (string) --
Specifies the recovery method for a user.















Exceptions

CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.LimitExceededException
CognitoIdentityProvider.Client.exceptions.InvalidSmsRoleAccessPolicyException
CognitoIdentityProvider.Client.exceptions.InvalidSmsRoleTrustRelationshipException
CognitoIdentityProvider.Client.exceptions.InvalidEmailRoleAccessPolicyException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.UserPoolTaggingException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


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
                    'RequireSymbols': True|False,
                    'TemporaryPasswordValidityDays': 123
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
                'VerifyAuthChallengeResponse': 'string',
                'PreTokenGeneration': 'string',
                'UserMigration': 'string'
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
            'UsernameAttributes': [
                'phone_number'|'email',
            ],
            'SmsVerificationMessage': 'string',
            'EmailVerificationMessage': 'string',
            'EmailVerificationSubject': 'string',
            'VerificationMessageTemplate': {
                'SmsMessage': 'string',
                'EmailMessage': 'string',
                'EmailSubject': 'string',
                'EmailMessageByLink': 'string',
                'EmailSubjectByLink': 'string',
                'DefaultEmailOption': 'CONFIRM_WITH_LINK'|'CONFIRM_WITH_CODE'
            },
            'SmsAuthenticationMessage': 'string',
            'MfaConfiguration': 'OFF'|'ON'|'OPTIONAL',
            'DeviceConfiguration': {
                'ChallengeRequiredOnNewDevice': True|False,
                'DeviceOnlyRememberedOnUserPrompt': True|False
            },
            'EstimatedNumberOfUsers': 123,
            'EmailConfiguration': {
                'SourceArn': 'string',
                'ReplyToEmailAddress': 'string',
                'EmailSendingAccount': 'COGNITO_DEFAULT'|'DEVELOPER',
                'From': 'string',
                'ConfigurationSet': 'string'
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
            'Domain': 'string',
            'CustomDomain': 'string',
            'AdminCreateUserConfig': {
                'AllowAdminCreateUserOnly': True|False,
                'UnusedAccountValidityDays': 123,
                'InviteMessageTemplate': {
                    'SMSMessage': 'string',
                    'EmailMessage': 'string',
                    'EmailSubject': 'string'
                }
            },
            'UserPoolAddOns': {
                'AdvancedSecurityMode': 'OFF'|'AUDIT'|'ENFORCED'
            },
            'UsernameConfiguration': {
                'CaseSensitive': True|False
            },
            'Arn': 'string',
            'AccountRecoverySetting': {
                'RecoveryMechanisms': [
                    {
                        'Priority': 123,
                        'Name': 'verified_email'|'verified_phone_number'|'admin_only'
                    },
                ]
            }
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_user_pool_client(UserPoolId=None, ClientName=None, GenerateSecret=None, RefreshTokenValidity=None, ReadAttributes=None, WriteAttributes=None, ExplicitAuthFlows=None, SupportedIdentityProviders=None, CallbackURLs=None, LogoutURLs=None, DefaultRedirectURI=None, AllowedOAuthFlows=None, AllowedOAuthScopes=None, AllowedOAuthFlowsUserPoolClient=None, AnalyticsConfiguration=None, PreventUserExistenceErrors=None):
    """
    Creates the user pool client.
    See also: AWS API Documentation
    
    Exceptions
    
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
            'ADMIN_NO_SRP_AUTH'|'CUSTOM_AUTH_FLOW_ONLY'|'USER_PASSWORD_AUTH'|'ALLOW_ADMIN_USER_PASSWORD_AUTH'|'ALLOW_CUSTOM_AUTH'|'ALLOW_USER_PASSWORD_AUTH'|'ALLOW_USER_SRP_AUTH'|'ALLOW_REFRESH_TOKEN_AUTH',
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
        AllowedOAuthFlowsUserPoolClient=True|False,
        AnalyticsConfiguration={
            'ApplicationId': 'string',
            'RoleArn': 'string',
            'ExternalId': 'string',
            'UserDataShared': True|False
        },
        PreventUserExistenceErrors='LEGACY'|'ENABLED'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID for the user pool where you want to create a user pool client.\n

    :type ClientName: string
    :param ClientName: [REQUIRED]\nThe client name for the user pool client you would like to create.\n

    :type GenerateSecret: boolean
    :param GenerateSecret: Boolean to specify whether you want to generate a secret for the user pool client being created.

    :type RefreshTokenValidity: integer
    :param RefreshTokenValidity: The time limit, in days, after which the refresh token is no longer valid and cannot be used.

    :type ReadAttributes: list
    :param ReadAttributes: The read attributes.\n\n(string) --\n\n

    :type WriteAttributes: list
    :param WriteAttributes: The user pool attributes that the app client can write to.\nIf your app client allows users to sign in through an identity provider, this array must include all attributes that are mapped to identity provider attributes. Amazon Cognito updates mapped attributes when users sign in to your application through an identity provider. If your app client lacks write access to a mapped attribute, Amazon Cognito throws an error when it attempts to update the attribute. For more information, see Specifying Identity Provider Attribute Mappings for Your User Pool .\n\n(string) --\n\n

    :type ExplicitAuthFlows: list
    :param ExplicitAuthFlows: The authentication flows that are supported by the user pool clients. Flow names without the ALLOW_ prefix are deprecated in favor of new names with the ALLOW_ prefix. Note that values with ALLOW_ prefix cannot be used along with values without ALLOW_ prefix.\nValid values include:\n\nALLOW_ADMIN_USER_PASSWORD_AUTH : Enable admin based user password authentication flow ADMIN_USER_PASSWORD_AUTH . This setting replaces the ADMIN_NO_SRP_AUTH setting. With this authentication flow, Cognito receives the password in the request instead of using the SRP (Secure Remote Password protocol) protocol to verify passwords.\nALLOW_CUSTOM_AUTH : Enable Lambda trigger based authentication.\nALLOW_USER_PASSWORD_AUTH : Enable user password-based authentication. In this flow, Cognito receives the password in the request instead of using the SRP protocol to verify passwords.\nALLOW_USER_SRP_AUTH : Enable SRP based authentication.\nALLOW_REFRESH_TOKEN_AUTH : Enable authflow to refresh tokens.\n\n\n(string) --\n\n

    :type SupportedIdentityProviders: list
    :param SupportedIdentityProviders: A list of provider names for the identity providers that are supported on this client. The following are supported: COGNITO , Facebook , Google and LoginWithAmazon .\n\n(string) --\n\n

    :type CallbackURLs: list
    :param CallbackURLs: A list of allowed redirect (callback) URLs for the identity providers.\nA redirect URI must:\n\nBe an absolute URI.\nBe registered with the authorization server.\nNot include a fragment component.\n\nSee OAuth 2.0 - Redirection Endpoint .\nAmazon Cognito requires HTTPS over HTTP except for http://localhost for testing purposes only.\nApp callback URLs such as myapp://example are also supported.\n\n(string) --\n\n

    :type LogoutURLs: list
    :param LogoutURLs: A list of allowed logout URLs for the identity providers.\n\n(string) --\n\n

    :type DefaultRedirectURI: string
    :param DefaultRedirectURI: The default redirect URI. Must be in the CallbackURLs list.\nA redirect URI must:\n\nBe an absolute URI.\nBe registered with the authorization server.\nNot include a fragment component.\n\nSee OAuth 2.0 - Redirection Endpoint .\nAmazon Cognito requires HTTPS over HTTP except for http://localhost for testing purposes only.\nApp callback URLs such as myapp://example are also supported.\n

    :type AllowedOAuthFlows: list
    :param AllowedOAuthFlows: The allowed OAuth flows.\nSet to code to initiate a code grant flow, which provides an authorization code as the response. This code can be exchanged for access tokens with the token endpoint.\nSet to implicit to specify that the client should get the access token (and, optionally, ID token, based on scopes) directly.\nSet to client_credentials to specify that the client should get the access token (and, optionally, ID token, based on scopes) from the token endpoint using a combination of client and client_secret.\n\n(string) --\n\n

    :type AllowedOAuthScopes: list
    :param AllowedOAuthScopes: The allowed OAuth scopes. Possible values provided by OAuth are: phone , email , openid , and profile . Possible values provided by AWS are: aws.cognito.signin.user.admin . Custom scopes created in Resource Servers are also supported.\n\n(string) --\n\n

    :type AllowedOAuthFlowsUserPoolClient: boolean
    :param AllowedOAuthFlowsUserPoolClient: Set to true if the client is allowed to follow the OAuth protocol when interacting with Cognito user pools.

    :type AnalyticsConfiguration: dict
    :param AnalyticsConfiguration: The Amazon Pinpoint analytics configuration for collecting metrics for this user pool.\n\nNote\nCognito User Pools only supports sending events to Amazon Pinpoint projects in the US East (N. Virginia) us-east-1 Region, regardless of the region in which the user pool resides.\n\n\nApplicationId (string) -- [REQUIRED]The application ID for an Amazon Pinpoint application.\n\nRoleArn (string) -- [REQUIRED]The ARN of an IAM role that authorizes Amazon Cognito to publish events to Amazon Pinpoint analytics.\n\nExternalId (string) -- [REQUIRED]The external ID.\n\nUserDataShared (boolean) --If UserDataShared is true , Amazon Cognito will include user data in the events it publishes to Amazon Pinpoint analytics.\n\n\n

    :type PreventUserExistenceErrors: string
    :param PreventUserExistenceErrors: Use this setting to choose which errors and responses are returned by Cognito APIs during authentication, account confirmation, and password recovery when the user does not exist in the user pool. When set to ENABLED and the user does not exist, authentication returns an error indicating either the username or password was incorrect, and account confirmation and password recovery return a response indicating a code was sent to a simulated destination. When set to LEGACY , those APIs will return a UserNotFoundException exception if the user does not exist in the user pool.\nValid values include:\n\nENABLED - This prevents user existence-related errors.\nLEGACY - This represents the old behavior of Cognito where user existence related errors are not prevented.\n\nThis setting affects the behavior of following APIs:\n\nAdminInitiateAuth\nAdminRespondToAuthChallenge\nInitiateAuth\nRespondToAuthChallenge\nForgotPassword\nConfirmForgotPassword\nConfirmSignUp\nResendConfirmationCode\n\n\nNote\nAfter February 15th 2020, the value of PreventUserExistenceErrors will default to ENABLED for newly created user pool clients if no value is provided.\n\n

    :rtype: dict

ReturnsResponse Syntax
{
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
            'ADMIN_NO_SRP_AUTH'|'CUSTOM_AUTH_FLOW_ONLY'|'USER_PASSWORD_AUTH'|'ALLOW_ADMIN_USER_PASSWORD_AUTH'|'ALLOW_CUSTOM_AUTH'|'ALLOW_USER_PASSWORD_AUTH'|'ALLOW_USER_SRP_AUTH'|'ALLOW_REFRESH_TOKEN_AUTH',
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
        'AllowedOAuthFlowsUserPoolClient': True|False,
        'AnalyticsConfiguration': {
            'ApplicationId': 'string',
            'RoleArn': 'string',
            'ExternalId': 'string',
            'UserDataShared': True|False
        },
        'PreventUserExistenceErrors': 'LEGACY'|'ENABLED'
    }
}


Response Structure

(dict) --
Represents the response from the server to create a user pool client.

UserPoolClient (dict) --
The user pool client that was just created.

UserPoolId (string) --
The user pool ID for the user pool client.

ClientName (string) --
The client name from the user pool request of the client type.

ClientId (string) --
The ID of the client associated with the user pool.

ClientSecret (string) --
The client secret from the user pool request of the client type.

LastModifiedDate (datetime) --
The date the user pool client was last modified.

CreationDate (datetime) --
The date the user pool client was created.

RefreshTokenValidity (integer) --
The time limit, in days, after which the refresh token is no longer valid and cannot be used.

ReadAttributes (list) --
The Read-only attributes.

(string) --


WriteAttributes (list) --
The writeable attributes.

(string) --


ExplicitAuthFlows (list) --
The authentication flows that are supported by the user pool clients. Flow names without the ALLOW_ prefix are deprecated in favor of new names with the ALLOW_ prefix. Note that values with ALLOW_ prefix cannot be used along with values without ALLOW_ prefix.
Valid values include:

ALLOW_ADMIN_USER_PASSWORD_AUTH : Enable admin based user password authentication flow ADMIN_USER_PASSWORD_AUTH . This setting replaces the ADMIN_NO_SRP_AUTH setting. With this authentication flow, Cognito receives the password in the request instead of using the SRP (Secure Remote Password protocol) protocol to verify passwords.
ALLOW_CUSTOM_AUTH : Enable Lambda trigger based authentication.
ALLOW_USER_PASSWORD_AUTH : Enable user password-based authentication. In this flow, Cognito receives the password in the request instead of using the SRP protocol to verify passwords.
ALLOW_USER_SRP_AUTH : Enable SRP based authentication.
ALLOW_REFRESH_TOKEN_AUTH : Enable authflow to refresh tokens.


(string) --


SupportedIdentityProviders (list) --
A list of provider names for the identity providers that are supported on this client.

(string) --


CallbackURLs (list) --
A list of allowed redirect (callback) URLs for the identity providers.
A redirect URI must:

Be an absolute URI.
Be registered with the authorization server.
Not include a fragment component.

See OAuth 2.0 - Redirection Endpoint .
Amazon Cognito requires HTTPS over HTTP except for http://localhost for testing purposes only.
App callback URLs such as myapp://example are also supported.

(string) --


LogoutURLs (list) --
A list of allowed logout URLs for the identity providers.

(string) --


DefaultRedirectURI (string) --
The default redirect URI. Must be in the CallbackURLs list.
A redirect URI must:

Be an absolute URI.
Be registered with the authorization server.
Not include a fragment component.

See OAuth 2.0 - Redirection Endpoint .
Amazon Cognito requires HTTPS over HTTP except for http://localhost for testing purposes only.
App callback URLs such as myapp://example are also supported.

AllowedOAuthFlows (list) --
The allowed OAuth flows.
Set to code to initiate a code grant flow, which provides an authorization code as the response. This code can be exchanged for access tokens with the token endpoint.
Set to implicit to specify that the client should get the access token (and, optionally, ID token, based on scopes) directly.
Set to client_credentials to specify that the client should get the access token (and, optionally, ID token, based on scopes) from the token endpoint using a combination of client and client_secret.

(string) --


AllowedOAuthScopes (list) --
The allowed OAuth scopes. Possible values provided by OAuth are: phone , email , openid , and profile . Possible values provided by AWS are: aws.cognito.signin.user.admin . Custom scopes created in Resource Servers are also supported.

(string) --


AllowedOAuthFlowsUserPoolClient (boolean) --
Set to true if the client is allowed to follow the OAuth protocol when interacting with Cognito user pools.

AnalyticsConfiguration (dict) --
The Amazon Pinpoint analytics configuration for the user pool client.

Note
Cognito User Pools only supports sending events to Amazon Pinpoint projects in the US East (N. Virginia) us-east-1 Region, regardless of the region in which the user pool resides.


ApplicationId (string) --
The application ID for an Amazon Pinpoint application.

RoleArn (string) --
The ARN of an IAM role that authorizes Amazon Cognito to publish events to Amazon Pinpoint analytics.

ExternalId (string) --
The external ID.

UserDataShared (boolean) --
If UserDataShared is true , Amazon Cognito will include user data in the events it publishes to Amazon Pinpoint analytics.



PreventUserExistenceErrors (string) --
Use this setting to choose which errors and responses are returned by Cognito APIs during authentication, account confirmation, and password recovery when the user does not exist in the user pool. When set to ENABLED and the user does not exist, authentication returns an error indicating either the username or password was incorrect, and account confirmation and password recovery return a response indicating a code was sent to a simulated destination. When set to LEGACY , those APIs will return a UserNotFoundException exception if the user does not exist in the user pool.
Valid values include:

ENABLED - This prevents user existence-related errors.
LEGACY - This represents the old behavior of Cognito where user existence related errors are not prevented.

This setting affects the behavior of following APIs:

AdminInitiateAuth
AdminRespondToAuthChallenge
InitiateAuth
RespondToAuthChallenge
ForgotPassword
ConfirmForgotPassword
ConfirmSignUp
ResendConfirmationCode


Note
After February 15th 2020, the value of PreventUserExistenceErrors will default to ENABLED for newly created user pool clients if no value is provided.










Exceptions

CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.LimitExceededException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.ScopeDoesNotExistException
CognitoIdentityProvider.Client.exceptions.InvalidOAuthFlowException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


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
                'ADMIN_NO_SRP_AUTH'|'CUSTOM_AUTH_FLOW_ONLY'|'USER_PASSWORD_AUTH'|'ALLOW_ADMIN_USER_PASSWORD_AUTH'|'ALLOW_CUSTOM_AUTH'|'ALLOW_USER_PASSWORD_AUTH'|'ALLOW_USER_SRP_AUTH'|'ALLOW_REFRESH_TOKEN_AUTH',
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
            'AllowedOAuthFlowsUserPoolClient': True|False,
            'AnalyticsConfiguration': {
                'ApplicationId': 'string',
                'RoleArn': 'string',
                'ExternalId': 'string',
                'UserDataShared': True|False
            },
            'PreventUserExistenceErrors': 'LEGACY'|'ENABLED'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_user_pool_domain(Domain=None, UserPoolId=None, CustomDomainConfig=None):
    """
    Creates a new domain for a user pool.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_user_pool_domain(
        Domain='string',
        UserPoolId='string',
        CustomDomainConfig={
            'CertificateArn': 'string'
        }
    )
    
    
    :type Domain: string
    :param Domain: [REQUIRED]\nThe domain string.\n

    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID.\n

    :type CustomDomainConfig: dict
    :param CustomDomainConfig: The configuration for a custom domain that hosts the sign-up and sign-in webpages for your application.\nProvide this parameter only if you want to use a custom domain for your user pool. Otherwise, you can exclude this parameter and use the Amazon Cognito hosted domain instead.\nFor more information about the hosted domain and custom domains, see Configuring a User Pool Domain .\n\nCertificateArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of an AWS Certificate Manager SSL certificate. You use this certificate for the subdomain of your custom domain.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'CloudFrontDomain': 'string'
}


Response Structure

(dict) --

CloudFrontDomain (string) --
The Amazon CloudFront endpoint that you use as the target of the alias that you set up with your Domain Name Service (DNS) provider.







Exceptions

CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.LimitExceededException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


    :return: {
        'CloudFrontDomain': 'string'
    }
    
    
    :returns: 
    CognitoIdentityProvider.Client.exceptions.InvalidParameterException
    CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
    CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
    CognitoIdentityProvider.Client.exceptions.LimitExceededException
    CognitoIdentityProvider.Client.exceptions.InternalErrorException
    
    """
    pass

def delete_group(GroupName=None, UserPoolId=None):
    """
    Deletes a group. Currently only groups with no members can be deleted.
    Calling this action requires developer credentials.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_group(
        GroupName='string',
        UserPoolId='string'
    )
    
    
    :type GroupName: string
    :param GroupName: [REQUIRED]\nThe name of the group.\n

    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID for the user pool.\n

    :returns: 
    CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
    CognitoIdentityProvider.Client.exceptions.InvalidParameterException
    CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
    CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
    CognitoIdentityProvider.Client.exceptions.InternalErrorException
    
    """
    pass

def delete_identity_provider(UserPoolId=None, ProviderName=None):
    """
    Deletes an identity provider for a user pool.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_identity_provider(
        UserPoolId='string',
        ProviderName='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID.\n

    :type ProviderName: string
    :param ProviderName: [REQUIRED]\nThe identity provider name.\n

    :returns: 
    CognitoIdentityProvider.Client.exceptions.InvalidParameterException
    CognitoIdentityProvider.Client.exceptions.UnsupportedIdentityProviderException
    CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
    CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
    CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
    CognitoIdentityProvider.Client.exceptions.InternalErrorException
    
    """
    pass

def delete_resource_server(UserPoolId=None, Identifier=None):
    """
    Deletes a resource server.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_resource_server(
        UserPoolId='string',
        Identifier='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID for the user pool that hosts the resource server.\n

    :type Identifier: string
    :param Identifier: [REQUIRED]\nThe identifier for the resource server.\n

    :returns: 
    CognitoIdentityProvider.Client.exceptions.InvalidParameterException
    CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
    CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
    CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
    CognitoIdentityProvider.Client.exceptions.InternalErrorException
    
    """
    pass

def delete_user(AccessToken=None):
    """
    Allows a user to delete himself or herself.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_user(
        AccessToken='string'
    )
    
    
    :type AccessToken: string
    :param AccessToken: [REQUIRED]\nThe access token from a request to delete a user.\n

    """
    pass

def delete_user_attributes(UserAttributeNames=None, AccessToken=None):
    """
    Deletes the attributes for a user.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_user_attributes(
        UserAttributeNames=[
            'string',
        ],
        AccessToken='string'
    )
    
    
    :type UserAttributeNames: list
    :param UserAttributeNames: [REQUIRED]\nAn array of strings representing the user attribute names you wish to delete.\nFor custom attributes, you must prepend the custom: prefix to the attribute name.\n\n(string) --\n\n

    :type AccessToken: string
    :param AccessToken: [REQUIRED]\nThe access token used in the request to delete user attributes.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
Represents the response from the server to delete user attributes.





Exceptions

CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.PasswordResetRequiredException
CognitoIdentityProvider.Client.exceptions.UserNotFoundException
CognitoIdentityProvider.Client.exceptions.UserNotConfirmedException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


    :return: {}
    
    
    :returns: 
    CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
    CognitoIdentityProvider.Client.exceptions.InvalidParameterException
    CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
    CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
    CognitoIdentityProvider.Client.exceptions.PasswordResetRequiredException
    CognitoIdentityProvider.Client.exceptions.UserNotFoundException
    CognitoIdentityProvider.Client.exceptions.UserNotConfirmedException
    CognitoIdentityProvider.Client.exceptions.InternalErrorException
    
    """
    pass

def delete_user_pool(UserPoolId=None):
    """
    Deletes the specified Amazon Cognito user pool.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_user_pool(
        UserPoolId='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID for the user pool you want to delete.\n

    """
    pass

def delete_user_pool_client(UserPoolId=None, ClientId=None):
    """
    Allows the developer to delete the user pool client.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_user_pool_client(
        UserPoolId='string',
        ClientId='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID for the user pool where you want to delete the client.\n

    :type ClientId: string
    :param ClientId: [REQUIRED]\nThe app client ID of the app associated with the user pool.\n

    :returns: 
    CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
    CognitoIdentityProvider.Client.exceptions.InvalidParameterException
    CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
    CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
    CognitoIdentityProvider.Client.exceptions.InternalErrorException
    
    """
    pass

def delete_user_pool_domain(Domain=None, UserPoolId=None):
    """
    Deletes a domain for a user pool.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_user_pool_domain(
        Domain='string',
        UserPoolId='string'
    )
    
    
    :type Domain: string
    :param Domain: [REQUIRED]\nThe domain string.\n

    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def describe_identity_provider(UserPoolId=None, ProviderName=None):
    """
    Gets information about a specific identity provider.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_identity_provider(
        UserPoolId='string',
        ProviderName='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID.\n

    :type ProviderName: string
    :param ProviderName: [REQUIRED]\nThe identity provider name.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'IdentityProvider': {
        'UserPoolId': 'string',
        'ProviderName': 'string',
        'ProviderType': 'SAML'|'Facebook'|'Google'|'LoginWithAmazon'|'SignInWithApple'|'OIDC',
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


Response Structure

(dict) --

IdentityProvider (dict) --
The identity provider that was deleted.

UserPoolId (string) --
The user pool ID.

ProviderName (string) --
The identity provider name.

ProviderType (string) --
The identity provider type.

ProviderDetails (dict) --
The identity provider details. The following list describes the provider detail keys for each identity provider type.

For Google, Facebook and Login with Amazon:
client_id
client_secret
authorize_scopes


For Sign in with Apple:
client_id
team_id
key_id
private_key
authorize_scopes


For OIDC providers:
client_id
client_secret
attributes_request_method
oidc_issuer
authorize_scopes
authorize_url if not available from discovery URL specified by oidc_issuer key
token_url if not available from discovery URL specified by oidc_issuer key
attributes_url if not available from discovery URL specified by oidc_issuer key
jwks_uri if not available from discovery URL specified by oidc_issuer key
authorize_scopes


For SAML providers:
MetadataFile OR MetadataURL
IDPSignOut optional




(string) --
(string) --




AttributeMapping (dict) --
A mapping of identity provider attributes to standard and custom user pool attributes.

(string) --
(string) --




IdpIdentifiers (list) --
A list of identity provider identifiers.

(string) --


LastModifiedDate (datetime) --
The date the identity provider was last modified.

CreationDate (datetime) --
The date the identity provider was created.









Exceptions

CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


    :return: {
        'IdentityProvider': {
            'UserPoolId': 'string',
            'ProviderName': 'string',
            'ProviderType': 'SAML'|'Facebook'|'Google'|'LoginWithAmazon'|'SignInWithApple'|'OIDC',
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
    For Google, Facebook and Login with Amazon:
    client_id
    client_secret
    authorize_scopes
    
    
    For Sign in with Apple:
    client_id
    team_id
    key_id
    private_key
    authorize_scopes
    
    
    For OIDC providers:
    client_id
    client_secret
    attributes_request_method
    oidc_issuer
    authorize_scopes
    authorize_url if not available from discovery URL specified by oidc_issuer key
    token_url if not available from discovery URL specified by oidc_issuer key
    attributes_url if not available from discovery URL specified by oidc_issuer key
    jwks_uri if not available from discovery URL specified by oidc_issuer key
    authorize_scopes
    
    
    For SAML providers:
    MetadataFile OR MetadataURL
    IDPSignOut optional
    
    
    
    """
    pass

def describe_resource_server(UserPoolId=None, Identifier=None):
    """
    Describes a resource server.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_resource_server(
        UserPoolId='string',
        Identifier='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID for the user pool that hosts the resource server.\n

    :type Identifier: string
    :param Identifier: [REQUIRED]\nThe identifier for the resource server\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ResourceServer': {
        'UserPoolId': 'string',
        'Identifier': 'string',
        'Name': 'string',
        'Scopes': [
            {
                'ScopeName': 'string',
                'ScopeDescription': 'string'
            },
        ]
    }
}


Response Structure

(dict) --

ResourceServer (dict) --
The resource server.

UserPoolId (string) --
The user pool ID for the user pool that hosts the resource server.

Identifier (string) --
The identifier for the resource server.

Name (string) --
The name of the resource server.

Scopes (list) --
A list of scopes that are defined for the resource server.

(dict) --
A resource server scope.

ScopeName (string) --
The name of the scope.

ScopeDescription (string) --
A description of the scope.













Exceptions

CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


    :return: {
        'ResourceServer': {
            'UserPoolId': 'string',
            'Identifier': 'string',
            'Name': 'string',
            'Scopes': [
                {
                    'ScopeName': 'string',
                    'ScopeDescription': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    CognitoIdentityProvider.Client.exceptions.InvalidParameterException
    CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
    CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
    CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
    CognitoIdentityProvider.Client.exceptions.InternalErrorException
    
    """
    pass

def describe_risk_configuration(UserPoolId=None, ClientId=None):
    """
    Describes the risk configuration.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_risk_configuration(
        UserPoolId='string',
        ClientId='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID.\n

    :type ClientId: string
    :param ClientId: The app client ID.

    :rtype: dict

ReturnsResponse Syntax
{
    'RiskConfiguration': {
        'UserPoolId': 'string',
        'ClientId': 'string',
        'CompromisedCredentialsRiskConfiguration': {
            'EventFilter': [
                'SIGN_IN'|'PASSWORD_CHANGE'|'SIGN_UP',
            ],
            'Actions': {
                'EventAction': 'BLOCK'|'NO_ACTION'
            }
        },
        'AccountTakeoverRiskConfiguration': {
            'NotifyConfiguration': {
                'From': 'string',
                'ReplyTo': 'string',
                'SourceArn': 'string',
                'BlockEmail': {
                    'Subject': 'string',
                    'HtmlBody': 'string',
                    'TextBody': 'string'
                },
                'NoActionEmail': {
                    'Subject': 'string',
                    'HtmlBody': 'string',
                    'TextBody': 'string'
                },
                'MfaEmail': {
                    'Subject': 'string',
                    'HtmlBody': 'string',
                    'TextBody': 'string'
                }
            },
            'Actions': {
                'LowAction': {
                    'Notify': True|False,
                    'EventAction': 'BLOCK'|'MFA_IF_CONFIGURED'|'MFA_REQUIRED'|'NO_ACTION'
                },
                'MediumAction': {
                    'Notify': True|False,
                    'EventAction': 'BLOCK'|'MFA_IF_CONFIGURED'|'MFA_REQUIRED'|'NO_ACTION'
                },
                'HighAction': {
                    'Notify': True|False,
                    'EventAction': 'BLOCK'|'MFA_IF_CONFIGURED'|'MFA_REQUIRED'|'NO_ACTION'
                }
            }
        },
        'RiskExceptionConfiguration': {
            'BlockedIPRangeList': [
                'string',
            ],
            'SkippedIPRangeList': [
                'string',
            ]
        },
        'LastModifiedDate': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --

RiskConfiguration (dict) --
The risk configuration.

UserPoolId (string) --
The user pool ID.

ClientId (string) --
The app client ID.

CompromisedCredentialsRiskConfiguration (dict) --
The compromised credentials risk configuration object including the EventFilter and the EventAction

EventFilter (list) --
Perform the action for these events. The default is to perform all events if no event filter is specified.

(string) --


Actions (dict) --
The compromised credentials risk configuration actions.

EventAction (string) --
The event action.





AccountTakeoverRiskConfiguration (dict) --
The account takeover risk configuration object including the NotifyConfiguration object and Actions to take in the case of an account takeover.

NotifyConfiguration (dict) --
The notify configuration used to construct email notifications.

From (string) --
The email address that is sending the email. It must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES.

ReplyTo (string) --
The destination to which the receiver of an email should reply to.

SourceArn (string) --
The Amazon Resource Name (ARN) of the identity that is associated with the sending authorization policy. It permits Amazon Cognito to send for the email address specified in the From parameter.

BlockEmail (dict) --
Email template used when a detected risk event is blocked.

Subject (string) --
The subject.

HtmlBody (string) --
The HTML body.

TextBody (string) --
The text body.



NoActionEmail (dict) --
The email template used when a detected risk event is allowed.

Subject (string) --
The subject.

HtmlBody (string) --
The HTML body.

TextBody (string) --
The text body.



MfaEmail (dict) --
The MFA email template used when MFA is challenged as part of a detected risk.

Subject (string) --
The subject.

HtmlBody (string) --
The HTML body.

TextBody (string) --
The text body.





Actions (dict) --
Account takeover risk configuration actions

LowAction (dict) --
Action to take for a low risk.

Notify (boolean) --
Flag specifying whether to send a notification.

EventAction (string) --
The event action.

BLOCK Choosing this action will block the request.
MFA_IF_CONFIGURED Throw MFA challenge if user has configured it, else allow the request.
MFA_REQUIRED Throw MFA challenge if user has configured it, else block the request.
NO_ACTION Allow the user sign-in.




MediumAction (dict) --
Action to take for a medium risk.

Notify (boolean) --
Flag specifying whether to send a notification.

EventAction (string) --
The event action.

BLOCK Choosing this action will block the request.
MFA_IF_CONFIGURED Throw MFA challenge if user has configured it, else allow the request.
MFA_REQUIRED Throw MFA challenge if user has configured it, else block the request.
NO_ACTION Allow the user sign-in.




HighAction (dict) --
Action to take for a high risk.

Notify (boolean) --
Flag specifying whether to send a notification.

EventAction (string) --
The event action.

BLOCK Choosing this action will block the request.
MFA_IF_CONFIGURED Throw MFA challenge if user has configured it, else allow the request.
MFA_REQUIRED Throw MFA challenge if user has configured it, else block the request.
NO_ACTION Allow the user sign-in.








RiskExceptionConfiguration (dict) --
The configuration to override the risk decision.

BlockedIPRangeList (list) --
Overrides the risk decision to always block the pre-authentication requests. The IP range is in CIDR notation: a compact representation of an IP address and its associated routing prefix.

(string) --


SkippedIPRangeList (list) --
Risk detection is not performed on the IP addresses in the range list. The IP range is in CIDR notation.

(string) --




LastModifiedDate (datetime) --
The last modified date.









Exceptions

CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.UserPoolAddOnNotEnabledException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


    :return: {
        'RiskConfiguration': {
            'UserPoolId': 'string',
            'ClientId': 'string',
            'CompromisedCredentialsRiskConfiguration': {
                'EventFilter': [
                    'SIGN_IN'|'PASSWORD_CHANGE'|'SIGN_UP',
                ],
                'Actions': {
                    'EventAction': 'BLOCK'|'NO_ACTION'
                }
            },
            'AccountTakeoverRiskConfiguration': {
                'NotifyConfiguration': {
                    'From': 'string',
                    'ReplyTo': 'string',
                    'SourceArn': 'string',
                    'BlockEmail': {
                        'Subject': 'string',
                        'HtmlBody': 'string',
                        'TextBody': 'string'
                    },
                    'NoActionEmail': {
                        'Subject': 'string',
                        'HtmlBody': 'string',
                        'TextBody': 'string'
                    },
                    'MfaEmail': {
                        'Subject': 'string',
                        'HtmlBody': 'string',
                        'TextBody': 'string'
                    }
                },
                'Actions': {
                    'LowAction': {
                        'Notify': True|False,
                        'EventAction': 'BLOCK'|'MFA_IF_CONFIGURED'|'MFA_REQUIRED'|'NO_ACTION'
                    },
                    'MediumAction': {
                        'Notify': True|False,
                        'EventAction': 'BLOCK'|'MFA_IF_CONFIGURED'|'MFA_REQUIRED'|'NO_ACTION'
                    },
                    'HighAction': {
                        'Notify': True|False,
                        'EventAction': 'BLOCK'|'MFA_IF_CONFIGURED'|'MFA_REQUIRED'|'NO_ACTION'
                    }
                }
            },
            'RiskExceptionConfiguration': {
                'BlockedIPRangeList': [
                    'string',
                ],
                'SkippedIPRangeList': [
                    'string',
                ]
            },
            'LastModifiedDate': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_user_import_job(UserPoolId=None, JobId=None):
    """
    Describes the user import job.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_user_import_job(
        UserPoolId='string',
        JobId='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID for the user pool that the users are being imported into.\n

    :type JobId: string
    :param JobId: [REQUIRED]\nThe job ID for the user import job.\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --
Represents the response from the server to the request to describe the user import job.

UserImportJob (dict) --
The job object that represents the user import job.

JobName (string) --
The job name for the user import job.

JobId (string) --
The job ID for the user import job.

UserPoolId (string) --
The user pool ID for the user pool that the users are being imported into.

PreSignedUrl (string) --
The pre-signed URL to be used to upload the .csv file.

CreationDate (datetime) --
The date the user import job was created.

StartDate (datetime) --
The date when the user import job was started.

CompletionDate (datetime) --
The date when the user import job was completed.

Status (string) --
The status of the user import job. One of the following:

Created - The job was created but not started.
Pending - A transition state. You have started the job, but it has not begun importing users yet.
InProgress - The job has started, and users are being imported.
Stopping - You have stopped the job, but the job has not stopped importing users yet.
Stopped - You have stopped the job, and the job has stopped importing users.
Succeeded - The job has completed successfully.
Failed - The job has stopped due to an error.
Expired - You created a job, but did not start the job within 24-48 hours. All data associated with the job was deleted, and the job cannot be started.


CloudWatchLogsRoleArn (string) --
The role ARN for the Amazon CloudWatch Logging role for the user import job. For more information, see "Creating the CloudWatch Logs IAM Role" in the Amazon Cognito Developer Guide.

ImportedUsers (integer) --
The number of users that were successfully imported.

SkippedUsers (integer) --
The number of users that were skipped.

FailedUsers (integer) --
The number of users that could not be imported.

CompletionMessage (string) --
The message returned when the user import job is completed.









Exceptions

CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


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
    
    Exceptions
    
    :example: response = client.describe_user_pool(
        UserPoolId='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID for the user pool you want to describe.\n

    :rtype: dict
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
                'RequireSymbols': True|False,
                'TemporaryPasswordValidityDays': 123
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
            'VerifyAuthChallengeResponse': 'string',
            'PreTokenGeneration': 'string',
            'UserMigration': 'string'
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
        'UsernameAttributes': [
            'phone_number'|'email',
        ],
        'SmsVerificationMessage': 'string',
        'EmailVerificationMessage': 'string',
        'EmailVerificationSubject': 'string',
        'VerificationMessageTemplate': {
            'SmsMessage': 'string',
            'EmailMessage': 'string',
            'EmailSubject': 'string',
            'EmailMessageByLink': 'string',
            'EmailSubjectByLink': 'string',
            'DefaultEmailOption': 'CONFIRM_WITH_LINK'|'CONFIRM_WITH_CODE'
        },
        'SmsAuthenticationMessage': 'string',
        'MfaConfiguration': 'OFF'|'ON'|'OPTIONAL',
        'DeviceConfiguration': {
            'ChallengeRequiredOnNewDevice': True|False,
            'DeviceOnlyRememberedOnUserPrompt': True|False
        },
        'EstimatedNumberOfUsers': 123,
        'EmailConfiguration': {
            'SourceArn': 'string',
            'ReplyToEmailAddress': 'string',
            'EmailSendingAccount': 'COGNITO_DEFAULT'|'DEVELOPER',
            'From': 'string',
            'ConfigurationSet': 'string'
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
        'Domain': 'string',
        'CustomDomain': 'string',
        'AdminCreateUserConfig': {
            'AllowAdminCreateUserOnly': True|False,
            'UnusedAccountValidityDays': 123,
            'InviteMessageTemplate': {
                'SMSMessage': 'string',
                'EmailMessage': 'string',
                'EmailSubject': 'string'
            }
        },
        'UserPoolAddOns': {
            'AdvancedSecurityMode': 'OFF'|'AUDIT'|'ENFORCED'
        },
        'UsernameConfiguration': {
            'CaseSensitive': True|False
        },
        'Arn': 'string',
        'AccountRecoverySetting': {
            'RecoveryMechanisms': [
                {
                    'Priority': 123,
                    'Name': 'verified_email'|'verified_phone_number'|'admin_only'
                },
            ]
        }
    }
}


Response Structure

(dict) --Represents the response to describe the user pool.

UserPool (dict) --The container of metadata returned by the server to describe the pool.

Id (string) --The ID of the user pool.

Name (string) --The name of the user pool.

Policies (dict) --The policies associated with the user pool.

PasswordPolicy (dict) --The password policy.

MinimumLength (integer) --The minimum length of the password policy that you have set. Cannot be less than 6.

RequireUppercase (boolean) --In the password policy that you have set, refers to whether you have required users to use at least one uppercase letter in their password.

RequireLowercase (boolean) --In the password policy that you have set, refers to whether you have required users to use at least one lowercase letter in their password.

RequireNumbers (boolean) --In the password policy that you have set, refers to whether you have required users to use at least one number in their password.

RequireSymbols (boolean) --In the password policy that you have set, refers to whether you have required users to use at least one symbol in their password.

TemporaryPasswordValidityDays (integer) --In the password policy you have set, refers to the number of days a temporary password is valid. If the user does not sign-in during this time, their password will need to be reset by an administrator.

Note
When you set TemporaryPasswordValidityDays for a user pool, you will no longer be able to set the deprecated UnusedAccountValidityDays value for that user pool.






LambdaConfig (dict) --The AWS Lambda triggers associated with the user pool.

PreSignUp (string) --A pre-registration AWS Lambda trigger.

CustomMessage (string) --A custom Message AWS Lambda trigger.

PostConfirmation (string) --A post-confirmation AWS Lambda trigger.

PreAuthentication (string) --A pre-authentication AWS Lambda trigger.

PostAuthentication (string) --A post-authentication AWS Lambda trigger.

DefineAuthChallenge (string) --Defines the authentication challenge.

CreateAuthChallenge (string) --Creates an authentication challenge.

VerifyAuthChallengeResponse (string) --Verifies the authentication challenge response.

PreTokenGeneration (string) --A Lambda trigger that is invoked before token generation.

UserMigration (string) --The user migration Lambda config type.



Status (string) --The status of a user pool.

LastModifiedDate (datetime) --The date the user pool was last modified.

CreationDate (datetime) --The date the user pool was created.

SchemaAttributes (list) --A container with the schema attributes of a user pool.

(dict) --Contains information about the schema attribute.

Name (string) --A schema attribute of the name type.

AttributeDataType (string) --The attribute data type.

DeveloperOnlyAttribute (boolean) --
Note
We recommend that you use WriteAttributes in the user pool client to control how attributes can be mutated for new use cases instead of using DeveloperOnlyAttribute .

Specifies whether the attribute type is developer only. This attribute can only be modified by an administrator. Users will not be able to modify this attribute using their access token. For example, DeveloperOnlyAttribute can be modified using the API but cannot be updated using the API.

Mutable (boolean) --Specifies whether the value of the attribute can be changed.
For any user pool attribute that\'s mapped to an identity provider attribute, you must set this parameter to true . Amazon Cognito updates mapped attributes when users sign in to your application through an identity provider. If an attribute is immutable, Amazon Cognito throws an error when it attempts to update the attribute. For more information, see Specifying Identity Provider Attribute Mappings for Your User Pool .

Required (boolean) --Specifies whether a user pool attribute is required. If the attribute is required and the user does not provide a value, registration or sign-in will fail.

NumberAttributeConstraints (dict) --Specifies the constraints for an attribute of the number type.

MinValue (string) --The minimum value of an attribute that is of the number data type.

MaxValue (string) --The maximum value of an attribute that is of the number data type.



StringAttributeConstraints (dict) --Specifies the constraints for an attribute of the string type.

MinLength (string) --The minimum length.

MaxLength (string) --The maximum length.







AutoVerifiedAttributes (list) --Specifies the attributes that are auto-verified in a user pool.

(string) --


AliasAttributes (list) --Specifies the attributes that are aliased in a user pool.

(string) --


UsernameAttributes (list) --Specifies whether email addresses or phone numbers can be specified as usernames when a user signs up.

(string) --


SmsVerificationMessage (string) --The contents of the SMS verification message.

EmailVerificationMessage (string) --The contents of the email verification message.

EmailVerificationSubject (string) --The subject of the email verification message.

VerificationMessageTemplate (dict) --The template for verification messages.

SmsMessage (string) --The SMS message template.

EmailMessage (string) --The email message template.

EmailSubject (string) --The subject line for the email message template.

EmailMessageByLink (string) --The email message template for sending a confirmation link to the user.

EmailSubjectByLink (string) --The subject line for the email message template for sending a confirmation link to the user.

DefaultEmailOption (string) --The default email option.



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

SourceArn (string) --The Amazon Resource Name (ARN) of a verified email address in Amazon SES. This email address is used in one of the following ways, depending on the value that you specify for the EmailSendingAccount parameter:

If you specify COGNITO_DEFAULT , Amazon Cognito uses this address as the custom FROM address when it emails your users by using its built-in email account.
If you specify DEVELOPER , Amazon Cognito emails your users with this address by calling Amazon SES on your behalf.


ReplyToEmailAddress (string) --The destination to which the receiver of the email should reply to.

EmailSendingAccount (string) --Specifies whether Amazon Cognito emails your users by using its built-in email functionality or your Amazon SES email configuration. Specify one of the following values:

COGNITO_DEFAULT
When Amazon Cognito emails your users, it uses its built-in email functionality. When you use the default option, Amazon Cognito allows only a limited number of emails each day for your user pool. For typical production environments, the default email limit is below the required delivery volume. To achieve a higher delivery volume, specify DEVELOPER to use your Amazon SES email configuration.
To look up the email delivery limit for the default option, see Limits in Amazon Cognito in the Amazon Cognito Developer Guide .
The default FROM address is no-reply@verificationemail.com. To customize the FROM address, provide the ARN of an Amazon SES verified email address for the SourceArn parameter.

DEVELOPER
When Amazon Cognito emails your users, it uses your Amazon SES configuration. Amazon Cognito calls Amazon SES on your behalf to send email from your verified email address. When you use this option, the email delivery limits are the same limits that apply to your Amazon SES verified email address in your AWS account.
If you use this option, you must provide the ARN of an Amazon SES verified email address for the SourceArn parameter.
Before Amazon Cognito can email your users, it requires additional permissions to call Amazon SES on your behalf. When you update your user pool with this option, Amazon Cognito creates a service-linked role , which is a type of IAM role, in your AWS account. This role contains the permissions that allow Amazon Cognito to access Amazon SES and send email messages with your address. For more information about the service-linked role that Amazon Cognito creates, see Using Service-Linked Roles for Amazon Cognito in the Amazon Cognito Developer Guide .

From (string) --Identifies either the sender\xe2\x80\x99s email address or the sender\xe2\x80\x99s name with their email address. For example, testuser@example.com or Test User <testuser@example.com> . This address will appear before the body of the email.

ConfigurationSet (string) --The set of configuration rules that can be applied to emails sent using Amazon SES. A configuration set is applied to an email by including a reference to the configuration set in the headers of the email. Once applied, all of the rules in that configuration set are applied to the email. Configuration sets can be used to apply the following types of rules to emails:

Event publishing \xe2\x80\x93 Amazon SES can track the number of send, delivery, open, click, bounce, and complaint events for each email sent. Use event publishing to send information about these events to other AWS services such as SNS and CloudWatch.
IP pool management \xe2\x80\x93 When leasing dedicated IP addresses with Amazon SES, you can create groups of IP addresses, called dedicated IP pools. You can then associate the dedicated IP pools with configuration sets.




SmsConfiguration (dict) --The SMS configuration.

SnsCallerArn (string) --The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) caller. This is the ARN of the IAM role in your AWS account which Cognito will use to send SMS messages.

ExternalId (string) --The external ID is a value that we recommend you use to add security to your IAM role which is used to call Amazon SNS to send SMS messages for your user pool. If you provide an ExternalId , the Cognito User Pool will include it when attempting to assume your IAM role, so that you can set your roles trust policy to require the ExternalID . If you use the Cognito Management Console to create a role for SMS MFA, Cognito will create a role with the required permissions and a trust policy that demonstrates use of the ExternalId .



UserPoolTags (dict) --The tags that are assigned to the user pool. A tag is a label that you can apply to user pools to categorize and manage them in different ways, such as by purpose, owner, environment, or other criteria.

(string) --
(string) --




SmsConfigurationFailure (string) --The reason why the SMS configuration cannot send the messages to your users.

EmailConfigurationFailure (string) --The reason why the email configuration cannot send the messages to your users.

Domain (string) --Holds the domain prefix if the user pool has a domain associated with it.

CustomDomain (string) --A custom domain name that you provide to Amazon Cognito. This parameter applies only if you use a custom domain to host the sign-up and sign-in pages for your application. For example: auth.example.com .
For more information about adding a custom domain to your user pool, see Using Your Own Domain for the Hosted UI .

AdminCreateUserConfig (dict) --The configuration for AdminCreateUser requests.

AllowAdminCreateUserOnly (boolean) --Set to True if only the administrator is allowed to create user profiles. Set to False if users can sign themselves up via an app.

UnusedAccountValidityDays (integer) --The user account expiration limit, in days, after which the account is no longer usable. To reset the account after that time limit, you must call AdminCreateUser again, specifying "RESEND" for the MessageAction parameter. The default value for this parameter is 7.

Note
If you set a value for TemporaryPasswordValidityDays in PasswordPolicy , that value will be used and UnusedAccountValidityDays will be deprecated for that user pool.


InviteMessageTemplate (dict) --The message template to be used for the welcome message to new users.
See also Customizing User Invitation Messages .

SMSMessage (string) --The message template for SMS messages.

EmailMessage (string) --The message template for email messages.

EmailSubject (string) --The subject line for email messages.





UserPoolAddOns (dict) --The user pool add-ons.

AdvancedSecurityMode (string) --The advanced security mode.



UsernameConfiguration (dict) --You can choose to enable case sensitivity on the username input for the selected sign-in option. For example, when this is set to False , users will be able to sign in using either "username" or "Username". This configuration is immutable once it has been set. For more information, see .

CaseSensitive (boolean) --Specifies whether username case sensitivity will be applied for all users in the user pool through Cognito APIs.
Valid values include:

**True ** : Enables case sensitivity for all username input. When this option is set to True , users must sign in using the exact capitalization of their given username. For example, \xe2\x80\x9cUserName\xe2\x80\x9d. This is the default value.
**False ** : Enables case insensitivity for all username input. For example, when this option is set to False , users will be able to sign in using either "username" or "Username". This option also enables both preferred_username and email alias to be case insensitive, in addition to the username attribute.




Arn (string) --The Amazon Resource Name (ARN) for the user pool.

AccountRecoverySetting (dict) --Use this setting to define which verified available method a user can use to recover their password when they call ForgotPassword . It allows you to define a preferred method when a user has more than one method available. With this setting, SMS does not qualify for a valid password recovery mechanism if the user also has SMS MFA enabled. In the absence of this setting, Cognito uses the legacy behavior to determine the recovery method where SMS is preferred over email.

RecoveryMechanisms (list) --The list of RecoveryOptionTypes .

(dict) --A map containing a priority as a key, and recovery method name as a value.

Priority (integer) --A positive integer specifying priority of a method with 1 being the highest priority.

Name (string) --Specifies the recovery method for a user.














Exceptions

CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.UserPoolTaggingException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


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
                    'RequireSymbols': True|False,
                    'TemporaryPasswordValidityDays': 123
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
                'VerifyAuthChallengeResponse': 'string',
                'PreTokenGeneration': 'string',
                'UserMigration': 'string'
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
            'UsernameAttributes': [
                'phone_number'|'email',
            ],
            'SmsVerificationMessage': 'string',
            'EmailVerificationMessage': 'string',
            'EmailVerificationSubject': 'string',
            'VerificationMessageTemplate': {
                'SmsMessage': 'string',
                'EmailMessage': 'string',
                'EmailSubject': 'string',
                'EmailMessageByLink': 'string',
                'EmailSubjectByLink': 'string',
                'DefaultEmailOption': 'CONFIRM_WITH_LINK'|'CONFIRM_WITH_CODE'
            },
            'SmsAuthenticationMessage': 'string',
            'MfaConfiguration': 'OFF'|'ON'|'OPTIONAL',
            'DeviceConfiguration': {
                'ChallengeRequiredOnNewDevice': True|False,
                'DeviceOnlyRememberedOnUserPrompt': True|False
            },
            'EstimatedNumberOfUsers': 123,
            'EmailConfiguration': {
                'SourceArn': 'string',
                'ReplyToEmailAddress': 'string',
                'EmailSendingAccount': 'COGNITO_DEFAULT'|'DEVELOPER',
                'From': 'string',
                'ConfigurationSet': 'string'
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
            'Domain': 'string',
            'CustomDomain': 'string',
            'AdminCreateUserConfig': {
                'AllowAdminCreateUserOnly': True|False,
                'UnusedAccountValidityDays': 123,
                'InviteMessageTemplate': {
                    'SMSMessage': 'string',
                    'EmailMessage': 'string',
                    'EmailSubject': 'string'
                }
            },
            'UserPoolAddOns': {
                'AdvancedSecurityMode': 'OFF'|'AUDIT'|'ENFORCED'
            },
            'UsernameConfiguration': {
                'CaseSensitive': True|False
            },
            'Arn': 'string',
            'AccountRecoverySetting': {
                'RecoveryMechanisms': [
                    {
                        'Priority': 123,
                        'Name': 'verified_email'|'verified_phone_number'|'admin_only'
                    },
                ]
            }
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_user_pool_client(UserPoolId=None, ClientId=None):
    """
    Client method for returning the configuration information and metadata of the specified user pool app client.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_user_pool_client(
        UserPoolId='string',
        ClientId='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID for the user pool you want to describe.\n

    :type ClientId: string
    :param ClientId: [REQUIRED]\nThe app client ID of the app associated with the user pool.\n

    :rtype: dict

ReturnsResponse Syntax
{
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
            'ADMIN_NO_SRP_AUTH'|'CUSTOM_AUTH_FLOW_ONLY'|'USER_PASSWORD_AUTH'|'ALLOW_ADMIN_USER_PASSWORD_AUTH'|'ALLOW_CUSTOM_AUTH'|'ALLOW_USER_PASSWORD_AUTH'|'ALLOW_USER_SRP_AUTH'|'ALLOW_REFRESH_TOKEN_AUTH',
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
        'AllowedOAuthFlowsUserPoolClient': True|False,
        'AnalyticsConfiguration': {
            'ApplicationId': 'string',
            'RoleArn': 'string',
            'ExternalId': 'string',
            'UserDataShared': True|False
        },
        'PreventUserExistenceErrors': 'LEGACY'|'ENABLED'
    }
}


Response Structure

(dict) --
Represents the response from the server from a request to describe the user pool client.

UserPoolClient (dict) --
The user pool client from a server response to describe the user pool client.

UserPoolId (string) --
The user pool ID for the user pool client.

ClientName (string) --
The client name from the user pool request of the client type.

ClientId (string) --
The ID of the client associated with the user pool.

ClientSecret (string) --
The client secret from the user pool request of the client type.

LastModifiedDate (datetime) --
The date the user pool client was last modified.

CreationDate (datetime) --
The date the user pool client was created.

RefreshTokenValidity (integer) --
The time limit, in days, after which the refresh token is no longer valid and cannot be used.

ReadAttributes (list) --
The Read-only attributes.

(string) --


WriteAttributes (list) --
The writeable attributes.

(string) --


ExplicitAuthFlows (list) --
The authentication flows that are supported by the user pool clients. Flow names without the ALLOW_ prefix are deprecated in favor of new names with the ALLOW_ prefix. Note that values with ALLOW_ prefix cannot be used along with values without ALLOW_ prefix.
Valid values include:

ALLOW_ADMIN_USER_PASSWORD_AUTH : Enable admin based user password authentication flow ADMIN_USER_PASSWORD_AUTH . This setting replaces the ADMIN_NO_SRP_AUTH setting. With this authentication flow, Cognito receives the password in the request instead of using the SRP (Secure Remote Password protocol) protocol to verify passwords.
ALLOW_CUSTOM_AUTH : Enable Lambda trigger based authentication.
ALLOW_USER_PASSWORD_AUTH : Enable user password-based authentication. In this flow, Cognito receives the password in the request instead of using the SRP protocol to verify passwords.
ALLOW_USER_SRP_AUTH : Enable SRP based authentication.
ALLOW_REFRESH_TOKEN_AUTH : Enable authflow to refresh tokens.


(string) --


SupportedIdentityProviders (list) --
A list of provider names for the identity providers that are supported on this client.

(string) --


CallbackURLs (list) --
A list of allowed redirect (callback) URLs for the identity providers.
A redirect URI must:

Be an absolute URI.
Be registered with the authorization server.
Not include a fragment component.

See OAuth 2.0 - Redirection Endpoint .
Amazon Cognito requires HTTPS over HTTP except for http://localhost for testing purposes only.
App callback URLs such as myapp://example are also supported.

(string) --


LogoutURLs (list) --
A list of allowed logout URLs for the identity providers.

(string) --


DefaultRedirectURI (string) --
The default redirect URI. Must be in the CallbackURLs list.
A redirect URI must:

Be an absolute URI.
Be registered with the authorization server.
Not include a fragment component.

See OAuth 2.0 - Redirection Endpoint .
Amazon Cognito requires HTTPS over HTTP except for http://localhost for testing purposes only.
App callback URLs such as myapp://example are also supported.

AllowedOAuthFlows (list) --
The allowed OAuth flows.
Set to code to initiate a code grant flow, which provides an authorization code as the response. This code can be exchanged for access tokens with the token endpoint.
Set to implicit to specify that the client should get the access token (and, optionally, ID token, based on scopes) directly.
Set to client_credentials to specify that the client should get the access token (and, optionally, ID token, based on scopes) from the token endpoint using a combination of client and client_secret.

(string) --


AllowedOAuthScopes (list) --
The allowed OAuth scopes. Possible values provided by OAuth are: phone , email , openid , and profile . Possible values provided by AWS are: aws.cognito.signin.user.admin . Custom scopes created in Resource Servers are also supported.

(string) --


AllowedOAuthFlowsUserPoolClient (boolean) --
Set to true if the client is allowed to follow the OAuth protocol when interacting with Cognito user pools.

AnalyticsConfiguration (dict) --
The Amazon Pinpoint analytics configuration for the user pool client.

Note
Cognito User Pools only supports sending events to Amazon Pinpoint projects in the US East (N. Virginia) us-east-1 Region, regardless of the region in which the user pool resides.


ApplicationId (string) --
The application ID for an Amazon Pinpoint application.

RoleArn (string) --
The ARN of an IAM role that authorizes Amazon Cognito to publish events to Amazon Pinpoint analytics.

ExternalId (string) --
The external ID.

UserDataShared (boolean) --
If UserDataShared is true , Amazon Cognito will include user data in the events it publishes to Amazon Pinpoint analytics.



PreventUserExistenceErrors (string) --
Use this setting to choose which errors and responses are returned by Cognito APIs during authentication, account confirmation, and password recovery when the user does not exist in the user pool. When set to ENABLED and the user does not exist, authentication returns an error indicating either the username or password was incorrect, and account confirmation and password recovery return a response indicating a code was sent to a simulated destination. When set to LEGACY , those APIs will return a UserNotFoundException exception if the user does not exist in the user pool.
Valid values include:

ENABLED - This prevents user existence-related errors.
LEGACY - This represents the old behavior of Cognito where user existence related errors are not prevented.

This setting affects the behavior of following APIs:

AdminInitiateAuth
AdminRespondToAuthChallenge
InitiateAuth
RespondToAuthChallenge
ForgotPassword
ConfirmForgotPassword
ConfirmSignUp
ResendConfirmationCode


Note
After February 15th 2020, the value of PreventUserExistenceErrors will default to ENABLED for newly created user pool clients if no value is provided.










Exceptions

CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


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
                'ADMIN_NO_SRP_AUTH'|'CUSTOM_AUTH_FLOW_ONLY'|'USER_PASSWORD_AUTH'|'ALLOW_ADMIN_USER_PASSWORD_AUTH'|'ALLOW_CUSTOM_AUTH'|'ALLOW_USER_PASSWORD_AUTH'|'ALLOW_USER_SRP_AUTH'|'ALLOW_REFRESH_TOKEN_AUTH',
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
            'AllowedOAuthFlowsUserPoolClient': True|False,
            'AnalyticsConfiguration': {
                'ApplicationId': 'string',
                'RoleArn': 'string',
                'ExternalId': 'string',
                'UserDataShared': True|False
            },
            'PreventUserExistenceErrors': 'LEGACY'|'ENABLED'
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
    
    Exceptions
    
    :example: response = client.describe_user_pool_domain(
        Domain='string'
    )
    
    
    :type Domain: string
    :param Domain: [REQUIRED]\nThe domain string.\n

    :rtype: dict
ReturnsResponse Syntax{
    'DomainDescription': {
        'UserPoolId': 'string',
        'AWSAccountId': 'string',
        'Domain': 'string',
        'S3Bucket': 'string',
        'CloudFrontDistribution': 'string',
        'Version': 'string',
        'Status': 'CREATING'|'DELETING'|'UPDATING'|'ACTIVE'|'FAILED',
        'CustomDomainConfig': {
            'CertificateArn': 'string'
        }
    }
}


Response Structure

(dict) --
DomainDescription (dict) --A domain description object containing information about the domain.

UserPoolId (string) --The user pool ID.

AWSAccountId (string) --The AWS account ID for the user pool owner.

Domain (string) --The domain string.

S3Bucket (string) --The S3 bucket where the static files for this domain are stored.

CloudFrontDistribution (string) --The ARN of the CloudFront distribution.

Version (string) --The app version.

Status (string) --The domain status.

CustomDomainConfig (dict) --The configuration for a custom domain that hosts the sign-up and sign-in webpages for your application.

CertificateArn (string) --The Amazon Resource Name (ARN) of an AWS Certificate Manager SSL certificate. You use this certificate for the subdomain of your custom domain.










Exceptions

CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


    :return: {
        'DomainDescription': {
            'UserPoolId': 'string',
            'AWSAccountId': 'string',
            'Domain': 'string',
            'S3Bucket': 'string',
            'CloudFrontDistribution': 'string',
            'Version': 'string',
            'Status': 'CREATING'|'DELETING'|'UPDATING'|'ACTIVE'|'FAILED',
            'CustomDomainConfig': {
                'CertificateArn': 'string'
            }
        }
    }
    
    
    """
    pass

def forget_device(AccessToken=None, DeviceKey=None):
    """
    Forgets the specified device.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.forget_device(
        AccessToken='string',
        DeviceKey='string'
    )
    
    
    :type AccessToken: string
    :param AccessToken: The access token for the forgotten device request.

    :type DeviceKey: string
    :param DeviceKey: [REQUIRED]\nThe device key.\n

    :returns: 
    CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
    CognitoIdentityProvider.Client.exceptions.InvalidParameterException
    CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
    CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
    CognitoIdentityProvider.Client.exceptions.InvalidUserPoolConfigurationException
    CognitoIdentityProvider.Client.exceptions.PasswordResetRequiredException
    CognitoIdentityProvider.Client.exceptions.UserNotFoundException
    CognitoIdentityProvider.Client.exceptions.UserNotConfirmedException
    CognitoIdentityProvider.Client.exceptions.InternalErrorException
    
    """
    pass

def forgot_password(ClientId=None, SecretHash=None, UserContextData=None, Username=None, AnalyticsMetadata=None, ClientMetadata=None):
    """
    Calling this API causes a message to be sent to the end user with a confirmation code that is required to change the user\'s password. For the Username parameter, you can use the username or user alias. The method used to send the confirmation code is sent according to the specified AccountRecoverySetting. For more information, see Recovering User Accounts in the *Amazon Cognito Developer Guide* . If neither a verified phone number nor a verified email exists, an ``InvalidParameterException` is thrown. To use the confirmation code for resetting the password, call .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.forgot_password(
        ClientId='string',
        SecretHash='string',
        UserContextData={
            'EncodedData': 'string'
        },
        Username='string',
        AnalyticsMetadata={
            'AnalyticsEndpointId': 'string'
        },
        ClientMetadata={
            'string': 'string'
        }
    )
    
    
    :type ClientId: string
    :param ClientId: [REQUIRED]\nThe ID of the client associated with the user pool.\n

    :type SecretHash: string
    :param SecretHash: A keyed-hash message authentication code (HMAC) calculated using the secret key of a user pool client and username plus the client ID in the message.

    :type UserContextData: dict
    :param UserContextData: Contextual data such as the user\'s device fingerprint, IP address, or location used for evaluating the risk of an unexpected event by Amazon Cognito advanced security.\n\nEncodedData (string) --Contextual data such as the user\'s device fingerprint, IP address, or location used for evaluating the risk of an unexpected event by Amazon Cognito advanced security.\n\n\n

    :type Username: string
    :param Username: [REQUIRED]\nThe user name of the user for whom you want to enter a code to reset a forgotten password.\n

    :type AnalyticsMetadata: dict
    :param AnalyticsMetadata: The Amazon Pinpoint analytics metadata for collecting metrics for ForgotPassword calls.\n\nAnalyticsEndpointId (string) --The endpoint ID.\n\n\n

    :type ClientMetadata: dict
    :param ClientMetadata: A map of custom key-value pairs that you can provide as input for any custom workflows that this action triggers.\nYou create custom workflows by assigning AWS Lambda functions to user pool triggers. When you use the ForgotPassword API action, Amazon Cognito invokes any functions that are assigned to the following triggers: pre sign-up , custom message , and user migration . When Amazon Cognito invokes any of these functions, it passes a JSON payload, which the function receives as input. This payload contains a clientMetadata attribute, which provides the data that you assigned to the ClientMetadata parameter in your ForgotPassword request. In your function code in AWS Lambda, you can process the clientMetadata value to enhance your workflow for your specific needs.\nFor more information, see Customizing User Pool Workflows with Lambda Triggers in the Amazon Cognito Developer Guide .\n\nNote\nTake the following limitations into consideration when you use the ClientMetadata parameter:\n\nAmazon Cognito does not store the ClientMetadata value. This data is available only to AWS Lambda triggers that are assigned to a user pool to support custom workflows. If your user pool configuration does not include triggers, the ClientMetadata parameter serves no purpose.\nAmazon Cognito does not validate the ClientMetadata value.\nAmazon Cognito does not encrypt the the ClientMetadata value, so don\'t use it to provide sensitive information.\n\n\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'CodeDeliveryDetails': {
        'Destination': 'string',
        'DeliveryMedium': 'SMS'|'EMAIL',
        'AttributeName': 'string'
    }
}


Response Structure

(dict) --
Respresents the response from the server regarding the request to reset a password.

CodeDeliveryDetails (dict) --
The code delivery details returned by the server in response to the request to reset a password.

Destination (string) --
The destination for the code delivery details.

DeliveryMedium (string) --
The delivery medium (email message or phone number).

AttributeName (string) --
The attribute name.









Exceptions

CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.UnexpectedLambdaException
CognitoIdentityProvider.Client.exceptions.UserLambdaValidationException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.InvalidLambdaResponseException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.LimitExceededException
CognitoIdentityProvider.Client.exceptions.InvalidSmsRoleAccessPolicyException
CognitoIdentityProvider.Client.exceptions.InvalidSmsRoleTrustRelationshipException
CognitoIdentityProvider.Client.exceptions.InvalidEmailRoleAccessPolicyException
CognitoIdentityProvider.Client.exceptions.CodeDeliveryFailureException
CognitoIdentityProvider.Client.exceptions.UserNotFoundException
CognitoIdentityProvider.Client.exceptions.UserNotConfirmedException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


    :return: {
        'CodeDeliveryDetails': {
            'Destination': 'string',
            'DeliveryMedium': 'SMS'|'EMAIL',
            'AttributeName': 'string'
        }
    }
    
    
    :returns: 
    CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
    CognitoIdentityProvider.Client.exceptions.InvalidParameterException
    CognitoIdentityProvider.Client.exceptions.UnexpectedLambdaException
    CognitoIdentityProvider.Client.exceptions.UserLambdaValidationException
    CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
    CognitoIdentityProvider.Client.exceptions.InvalidLambdaResponseException
    CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
    CognitoIdentityProvider.Client.exceptions.LimitExceededException
    CognitoIdentityProvider.Client.exceptions.InvalidSmsRoleAccessPolicyException
    CognitoIdentityProvider.Client.exceptions.InvalidSmsRoleTrustRelationshipException
    CognitoIdentityProvider.Client.exceptions.InvalidEmailRoleAccessPolicyException
    CognitoIdentityProvider.Client.exceptions.CodeDeliveryFailureException
    CognitoIdentityProvider.Client.exceptions.UserNotFoundException
    CognitoIdentityProvider.Client.exceptions.UserNotConfirmedException
    CognitoIdentityProvider.Client.exceptions.InternalErrorException
    
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

def get_csv_header(UserPoolId=None):
    """
    Gets the header information for the .csv file to be used as input for the user import job.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_csv_header(
        UserPoolId='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID for the user pool that the users are to be imported into.\n

    :rtype: dict
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







Exceptions

CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


    :return: {
        'UserPoolId': 'string',
        'CSVHeader': [
            'string',
        ]
    }
    
    
    :returns: 
    CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
    CognitoIdentityProvider.Client.exceptions.InvalidParameterException
    CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
    CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
    CognitoIdentityProvider.Client.exceptions.InternalErrorException
    
    """
    pass

def get_device(DeviceKey=None, AccessToken=None):
    """
    Gets the device.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_device(
        DeviceKey='string',
        AccessToken='string'
    )
    
    
    :type DeviceKey: string
    :param DeviceKey: [REQUIRED]\nThe device key.\n

    :type AccessToken: string
    :param AccessToken: The access token.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --
Gets the device response.

Device (dict) --
The device.

DeviceKey (string) --
The device key.

DeviceAttributes (list) --
The device attributes.

(dict) --
Specifies whether the attribute is standard or custom.

Name (string) --
The name of the attribute.

Value (string) --
The value of the attribute.





DeviceCreateDate (datetime) --
The creation date of the device.

DeviceLastModifiedDate (datetime) --
The last modified date of the device.

DeviceLastAuthenticatedDate (datetime) --
The date in which the device was last authenticated.









Exceptions

CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.InvalidUserPoolConfigurationException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.PasswordResetRequiredException
CognitoIdentityProvider.Client.exceptions.UserNotFoundException
CognitoIdentityProvider.Client.exceptions.UserNotConfirmedException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


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
    
    
    :returns: 
    CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
    CognitoIdentityProvider.Client.exceptions.InvalidParameterException
    CognitoIdentityProvider.Client.exceptions.InvalidUserPoolConfigurationException
    CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
    CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
    CognitoIdentityProvider.Client.exceptions.PasswordResetRequiredException
    CognitoIdentityProvider.Client.exceptions.UserNotFoundException
    CognitoIdentityProvider.Client.exceptions.UserNotConfirmedException
    CognitoIdentityProvider.Client.exceptions.InternalErrorException
    
    """
    pass

def get_group(GroupName=None, UserPoolId=None):
    """
    Gets a group.
    Calling this action requires developer credentials.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_group(
        GroupName='string',
        UserPoolId='string'
    )
    
    
    :type GroupName: string
    :param GroupName: [REQUIRED]\nThe name of the group.\n

    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID for the user pool.\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

Group (dict) --
The group object for the group.

GroupName (string) --
The name of the group.

UserPoolId (string) --
The user pool ID for the user pool.

Description (string) --
A string containing the description of the group.

RoleArn (string) --
The role ARN for the group.

Precedence (integer) --
A nonnegative integer value that specifies the precedence of this group relative to the other groups that a user can belong to in the user pool. If a user belongs to two or more groups, it is the group with the highest precedence whose role ARN will be used in the cognito:roles and cognito:preferred_role claims in the user\'s tokens. Groups with higher Precedence values take precedence over groups with lower Precedence values or with null Precedence values.
Two groups can have the same Precedence value. If this happens, neither group takes precedence over the other. If two groups with the same Precedence have the same role ARN, that role is used in the cognito:preferred_role claim in tokens for users in each group. If the two groups have different role ARNs, the cognito:preferred_role claim is not set in users\' tokens.
The default Precedence value is null.

LastModifiedDate (datetime) --
The date the group was last modified.

CreationDate (datetime) --
The date the group was created.









Exceptions

CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


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
    
    
    :returns: 
    CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
    CognitoIdentityProvider.Client.exceptions.InvalidParameterException
    CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
    CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
    CognitoIdentityProvider.Client.exceptions.InternalErrorException
    
    """
    pass

def get_identity_provider_by_identifier(UserPoolId=None, IdpIdentifier=None):
    """
    Gets the specified identity provider.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_identity_provider_by_identifier(
        UserPoolId='string',
        IdpIdentifier='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID.\n

    :type IdpIdentifier: string
    :param IdpIdentifier: [REQUIRED]\nThe identity provider ID.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'IdentityProvider': {
        'UserPoolId': 'string',
        'ProviderName': 'string',
        'ProviderType': 'SAML'|'Facebook'|'Google'|'LoginWithAmazon'|'SignInWithApple'|'OIDC',
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


Response Structure

(dict) --

IdentityProvider (dict) --
The identity provider object.

UserPoolId (string) --
The user pool ID.

ProviderName (string) --
The identity provider name.

ProviderType (string) --
The identity provider type.

ProviderDetails (dict) --
The identity provider details. The following list describes the provider detail keys for each identity provider type.

For Google, Facebook and Login with Amazon:
client_id
client_secret
authorize_scopes


For Sign in with Apple:
client_id
team_id
key_id
private_key
authorize_scopes


For OIDC providers:
client_id
client_secret
attributes_request_method
oidc_issuer
authorize_scopes
authorize_url if not available from discovery URL specified by oidc_issuer key
token_url if not available from discovery URL specified by oidc_issuer key
attributes_url if not available from discovery URL specified by oidc_issuer key
jwks_uri if not available from discovery URL specified by oidc_issuer key
authorize_scopes


For SAML providers:
MetadataFile OR MetadataURL
IDPSignOut optional




(string) --
(string) --




AttributeMapping (dict) --
A mapping of identity provider attributes to standard and custom user pool attributes.

(string) --
(string) --




IdpIdentifiers (list) --
A list of identity provider identifiers.

(string) --


LastModifiedDate (datetime) --
The date the identity provider was last modified.

CreationDate (datetime) --
The date the identity provider was created.









Exceptions

CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


    :return: {
        'IdentityProvider': {
            'UserPoolId': 'string',
            'ProviderName': 'string',
            'ProviderType': 'SAML'|'Facebook'|'Google'|'LoginWithAmazon'|'SignInWithApple'|'OIDC',
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
    For Google, Facebook and Login with Amazon:
    client_id
    client_secret
    authorize_scopes
    
    
    For Sign in with Apple:
    client_id
    team_id
    key_id
    private_key
    authorize_scopes
    
    
    For OIDC providers:
    client_id
    client_secret
    attributes_request_method
    oidc_issuer
    authorize_scopes
    authorize_url if not available from discovery URL specified by oidc_issuer key
    token_url if not available from discovery URL specified by oidc_issuer key
    attributes_url if not available from discovery URL specified by oidc_issuer key
    jwks_uri if not available from discovery URL specified by oidc_issuer key
    authorize_scopes
    
    
    For SAML providers:
    MetadataFile OR MetadataURL
    IDPSignOut optional
    
    
    
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

def get_signing_certificate(UserPoolId=None):
    """
    This method takes a user pool ID, and returns the signing certificate.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_signing_certificate(
        UserPoolId='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Certificate': 'string'
}


Response Structure

(dict) --Response from Cognito for a signing certificate request.

Certificate (string) --The signing certificate.






Exceptions

CognitoIdentityProvider.Client.exceptions.InternalErrorException
CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException


    :return: {
        'Certificate': 'string'
    }
    
    
    """
    pass

def get_ui_customization(UserPoolId=None, ClientId=None):
    """
    Gets the UI Customization information for a particular app client\'s app UI, if there is something set. If nothing is set for the particular client, but there is an existing pool level customization (app clientId will be ALL ), then that is returned. If nothing is present, then an empty shape is returned.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_ui_customization(
        UserPoolId='string',
        ClientId='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID for the user pool.\n

    :type ClientId: string
    :param ClientId: The client ID for the client app.

    :rtype: dict

ReturnsResponse Syntax
{
    'UICustomization': {
        'UserPoolId': 'string',
        'ClientId': 'string',
        'ImageUrl': 'string',
        'CSS': 'string',
        'CSSVersion': 'string',
        'LastModifiedDate': datetime(2015, 1, 1),
        'CreationDate': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --

UICustomization (dict) --
The UI customization information.

UserPoolId (string) --
The user pool ID for the user pool.

ClientId (string) --
The client ID for the client app.

ImageUrl (string) --
The logo image for the UI customization.

CSS (string) --
The CSS values in the UI customization.

CSSVersion (string) --
The CSS version number.

LastModifiedDate (datetime) --
The last-modified date for the UI customization.

CreationDate (datetime) --
The creation date for the UI customization.









Exceptions

CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


    :return: {
        'UICustomization': {
            'UserPoolId': 'string',
            'ClientId': 'string',
            'ImageUrl': 'string',
            'CSS': 'string',
            'CSSVersion': 'string',
            'LastModifiedDate': datetime(2015, 1, 1),
            'CreationDate': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    CognitoIdentityProvider.Client.exceptions.InvalidParameterException
    CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
    CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
    CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
    CognitoIdentityProvider.Client.exceptions.InternalErrorException
    
    """
    pass

def get_user(AccessToken=None):
    """
    Gets the user attributes and metadata for a user.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_user(
        AccessToken='string'
    )
    
    
    :type AccessToken: string
    :param AccessToken: [REQUIRED]\nThe access token returned by the server response to get information about the user.\n

    :rtype: dict
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
    ],
    'PreferredMfaSetting': 'string',
    'UserMFASettingList': [
        'string',
    ]
}


Response Structure

(dict) --Represents the response from the server from the request to get information about the user.

Username (string) --The user name of the user you wish to retrieve from the get user request.

UserAttributes (list) --An array of name-value pairs representing user attributes.
For custom attributes, you must prepend the custom: prefix to the attribute name.

(dict) --Specifies whether the attribute is standard or custom.

Name (string) --The name of the attribute.

Value (string) --The value of the attribute.





MFAOptions (list) --
This response parameter is no longer supported. It provides information only about SMS MFA configurations. It doesn\'t provide information about TOTP software token MFA configurations. To look up information about either type of MFA configuration, use the use the  GetUserResponse$UserMFASettingList response instead.

(dict) --
This data type is no longer supported. You can use it only for SMS MFA configurations. You can\'t use it for TOTP software token MFA configurations.
To set either type of MFA configuration, use the  AdminSetUserMFAPreference or  SetUserMFAPreference actions.
To look up information about either type of MFA configuration, use the  AdminGetUserResponse$UserMFASettingList or  GetUserResponse$UserMFASettingList responses.

DeliveryMedium (string) --The delivery medium to send the MFA code. You can use this parameter to set only the SMS delivery medium value.

AttributeName (string) --The attribute name of the MFA option type. The only valid value is phone_number .





PreferredMfaSetting (string) --The user\'s preferred MFA setting.

UserMFASettingList (list) --The MFA options that are enabled for the user. The possible values in this list are SMS_MFA and SOFTWARE_TOKEN_MFA .

(string) --







Exceptions

CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.PasswordResetRequiredException
CognitoIdentityProvider.Client.exceptions.UserNotFoundException
CognitoIdentityProvider.Client.exceptions.UserNotConfirmedException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


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
        ],
        'PreferredMfaSetting': 'string',
        'UserMFASettingList': [
            'string',
        ]
    }
    
    
    :returns: 
    CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
    CognitoIdentityProvider.Client.exceptions.InvalidParameterException
    CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
    CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
    CognitoIdentityProvider.Client.exceptions.PasswordResetRequiredException
    CognitoIdentityProvider.Client.exceptions.UserNotFoundException
    CognitoIdentityProvider.Client.exceptions.UserNotConfirmedException
    CognitoIdentityProvider.Client.exceptions.InternalErrorException
    
    """
    pass

def get_user_attribute_verification_code(AccessToken=None, AttributeName=None, ClientMetadata=None):
    """
    Gets the user attribute verification code for the specified attribute name.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_user_attribute_verification_code(
        AccessToken='string',
        AttributeName='string',
        ClientMetadata={
            'string': 'string'
        }
    )
    
    
    :type AccessToken: string
    :param AccessToken: [REQUIRED]\nThe access token returned by the server response to get the user attribute verification code.\n

    :type AttributeName: string
    :param AttributeName: [REQUIRED]\nThe attribute name returned by the server response to get the user attribute verification code.\n

    :type ClientMetadata: dict
    :param ClientMetadata: A map of custom key-value pairs that you can provide as input for any custom workflows that this action triggers.\nYou create custom workflows by assigning AWS Lambda functions to user pool triggers. When you use the GetUserAttributeVerificationCode API action, Amazon Cognito invokes the function that is assigned to the custom message trigger. When Amazon Cognito invokes this function, it passes a JSON payload, which the function receives as input. This payload contains a clientMetadata attribute, which provides the data that you assigned to the ClientMetadata parameter in your GetUserAttributeVerificationCode request. In your function code in AWS Lambda, you can process the clientMetadata value to enhance your workflow for your specific needs.\nFor more information, see Customizing User Pool Workflows with Lambda Triggers in the Amazon Cognito Developer Guide .\n\nNote\nTake the following limitations into consideration when you use the ClientMetadata parameter:\n\nAmazon Cognito does not store the ClientMetadata value. This data is available only to AWS Lambda triggers that are assigned to a user pool to support custom workflows. If your user pool configuration does not include triggers, the ClientMetadata parameter serves no purpose.\nAmazon Cognito does not validate the ClientMetadata value.\nAmazon Cognito does not encrypt the the ClientMetadata value, so don\'t use it to provide sensitive information.\n\n\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'CodeDeliveryDetails': {
        'Destination': 'string',
        'DeliveryMedium': 'SMS'|'EMAIL',
        'AttributeName': 'string'
    }
}


Response Structure

(dict) --
The verification code response returned by the server response to get the user attribute verification code.

CodeDeliveryDetails (dict) --
The code delivery details returned by the server in response to the request to get the user attribute verification code.

Destination (string) --
The destination for the code delivery details.

DeliveryMedium (string) --
The delivery medium (email message or phone number).

AttributeName (string) --
The attribute name.









Exceptions

CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.UnexpectedLambdaException
CognitoIdentityProvider.Client.exceptions.UserLambdaValidationException
CognitoIdentityProvider.Client.exceptions.InvalidLambdaResponseException
CognitoIdentityProvider.Client.exceptions.InvalidSmsRoleAccessPolicyException
CognitoIdentityProvider.Client.exceptions.InvalidSmsRoleTrustRelationshipException
CognitoIdentityProvider.Client.exceptions.InvalidEmailRoleAccessPolicyException
CognitoIdentityProvider.Client.exceptions.CodeDeliveryFailureException
CognitoIdentityProvider.Client.exceptions.LimitExceededException
CognitoIdentityProvider.Client.exceptions.PasswordResetRequiredException
CognitoIdentityProvider.Client.exceptions.UserNotFoundException
CognitoIdentityProvider.Client.exceptions.UserNotConfirmedException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


    :return: {
        'CodeDeliveryDetails': {
            'Destination': 'string',
            'DeliveryMedium': 'SMS'|'EMAIL',
            'AttributeName': 'string'
        }
    }
    
    
    :returns: 
    CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
    CognitoIdentityProvider.Client.exceptions.InvalidParameterException
    CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
    CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
    CognitoIdentityProvider.Client.exceptions.UnexpectedLambdaException
    CognitoIdentityProvider.Client.exceptions.UserLambdaValidationException
    CognitoIdentityProvider.Client.exceptions.InvalidLambdaResponseException
    CognitoIdentityProvider.Client.exceptions.InvalidSmsRoleAccessPolicyException
    CognitoIdentityProvider.Client.exceptions.InvalidSmsRoleTrustRelationshipException
    CognitoIdentityProvider.Client.exceptions.InvalidEmailRoleAccessPolicyException
    CognitoIdentityProvider.Client.exceptions.CodeDeliveryFailureException
    CognitoIdentityProvider.Client.exceptions.LimitExceededException
    CognitoIdentityProvider.Client.exceptions.PasswordResetRequiredException
    CognitoIdentityProvider.Client.exceptions.UserNotFoundException
    CognitoIdentityProvider.Client.exceptions.UserNotConfirmedException
    CognitoIdentityProvider.Client.exceptions.InternalErrorException
    
    """
    pass

def get_user_pool_mfa_config(UserPoolId=None):
    """
    Gets the user pool multi-factor authentication (MFA) configuration.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_user_pool_mfa_config(
        UserPoolId='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID.\n

    :rtype: dict
ReturnsResponse Syntax{
    'SmsMfaConfiguration': {
        'SmsAuthenticationMessage': 'string',
        'SmsConfiguration': {
            'SnsCallerArn': 'string',
            'ExternalId': 'string'
        }
    },
    'SoftwareTokenMfaConfiguration': {
        'Enabled': True|False
    },
    'MfaConfiguration': 'OFF'|'ON'|'OPTIONAL'
}


Response Structure

(dict) --
SmsMfaConfiguration (dict) --The SMS text message multi-factor (MFA) configuration.

SmsAuthenticationMessage (string) --The SMS authentication message that will be sent to users with the code they need to sign in. The message must contain the \xe2\x80\x98{####}\xe2\x80\x99 placeholder, which will be replaced with the code. If the message is not included, and default message will be used.

SmsConfiguration (dict) --The SMS configuration.

SnsCallerArn (string) --The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) caller. This is the ARN of the IAM role in your AWS account which Cognito will use to send SMS messages.

ExternalId (string) --The external ID is a value that we recommend you use to add security to your IAM role which is used to call Amazon SNS to send SMS messages for your user pool. If you provide an ExternalId , the Cognito User Pool will include it when attempting to assume your IAM role, so that you can set your roles trust policy to require the ExternalID . If you use the Cognito Management Console to create a role for SMS MFA, Cognito will create a role with the required permissions and a trust policy that demonstrates use of the ExternalId .





SoftwareTokenMfaConfiguration (dict) --The software token multi-factor (MFA) configuration.

Enabled (boolean) --Specifies whether software token MFA is enabled.



MfaConfiguration (string) --The multi-factor (MFA) configuration. Valid values include:

OFF MFA will not be used for any users.
ON MFA is required for all users to sign in.
OPTIONAL MFA will be required only for individual users who have an MFA factor enabled.







Exceptions

CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


    :return: {
        'SmsMfaConfiguration': {
            'SmsAuthenticationMessage': 'string',
            'SmsConfiguration': {
                'SnsCallerArn': 'string',
                'ExternalId': 'string'
            }
        },
        'SoftwareTokenMfaConfiguration': {
            'Enabled': True|False
        },
        'MfaConfiguration': 'OFF'|'ON'|'OPTIONAL'
    }
    
    
    :returns: 
    CognitoIdentityProvider.Client.exceptions.InvalidParameterException
    CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
    CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
    CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
    CognitoIdentityProvider.Client.exceptions.InternalErrorException
    
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

def global_sign_out(AccessToken=None):
    """
    Signs out users from all devices. It also invalidates all refresh tokens issued to a user. The user\'s current access and Id tokens remain valid until their expiry. Access and Id tokens expire one hour after they are issued.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.global_sign_out(
        AccessToken='string'
    )
    
    
    :type AccessToken: string
    :param AccessToken: [REQUIRED]\nThe access token.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --The response to the request to sign out all devices.




Exceptions

CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.PasswordResetRequiredException
CognitoIdentityProvider.Client.exceptions.UserNotConfirmedException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


    :return: {}
    
    
    """
    pass

def initiate_auth(AuthFlow=None, AuthParameters=None, ClientMetadata=None, ClientId=None, AnalyticsMetadata=None, UserContextData=None):
    """
    Initiates the authentication flow.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.initiate_auth(
        AuthFlow='USER_SRP_AUTH'|'REFRESH_TOKEN_AUTH'|'REFRESH_TOKEN'|'CUSTOM_AUTH'|'ADMIN_NO_SRP_AUTH'|'USER_PASSWORD_AUTH'|'ADMIN_USER_PASSWORD_AUTH',
        AuthParameters={
            'string': 'string'
        },
        ClientMetadata={
            'string': 'string'
        },
        ClientId='string',
        AnalyticsMetadata={
            'AnalyticsEndpointId': 'string'
        },
        UserContextData={
            'EncodedData': 'string'
        }
    )
    
    
    :type AuthFlow: string
    :param AuthFlow: [REQUIRED]\nThe authentication flow for this call to execute. The API action will depend on this value. For example:\n\nREFRESH_TOKEN_AUTH will take in a valid refresh token and return new tokens.\nUSER_SRP_AUTH will take in USERNAME and SRP_A and return the SRP variables to be used for next challenge execution.\nUSER_PASSWORD_AUTH will take in USERNAME and PASSWORD and return the next challenge or tokens.\n\nValid values include:\n\nUSER_SRP_AUTH : Authentication flow for the Secure Remote Password (SRP) protocol.\nREFRESH_TOKEN_AUTH /REFRESH_TOKEN : Authentication flow for refreshing the access token and ID token by supplying a valid refresh token.\nCUSTOM_AUTH : Custom authentication flow.\nUSER_PASSWORD_AUTH : Non-SRP authentication flow; USERNAME and PASSWORD are passed directly. If a user migration Lambda trigger is set, this flow will invoke the user migration Lambda if the USERNAME is not found in the user pool.\nADMIN_USER_PASSWORD_AUTH : Admin-based user password authentication. This replaces the ADMIN_NO_SRP_AUTH authentication flow. In this flow, Cognito receives the password in the request instead of using the SRP process to verify passwords.\n\n\nADMIN_NO_SRP_AUTH is not a valid value.\n

    :type AuthParameters: dict
    :param AuthParameters: The authentication parameters. These are inputs corresponding to the AuthFlow that you are invoking. The required values depend on the value of AuthFlow :\n\nFor USER_SRP_AUTH : USERNAME (required), SRP_A (required), SECRET_HASH (required if the app client is configured with a client secret), DEVICE_KEY\nFor REFRESH_TOKEN_AUTH/REFRESH_TOKEN : REFRESH_TOKEN (required), SECRET_HASH (required if the app client is configured with a client secret), DEVICE_KEY\nFor CUSTOM_AUTH : USERNAME (required), SECRET_HASH (if app client is configured with client secret), DEVICE_KEY\n\n\n(string) --\n(string) --\n\n\n\n

    :type ClientMetadata: dict
    :param ClientMetadata: A map of custom key-value pairs that you can provide as input for certain custom workflows that this action triggers.\nYou create custom workflows by assigning AWS Lambda functions to user pool triggers. When you use the InitiateAuth API action, Amazon Cognito invokes the AWS Lambda functions that are specified for various triggers. The ClientMetadata value is passed as input to the functions for only the following triggers:\n\nPre signup\nPre authentication\nUser migration\n\nWhen Amazon Cognito invokes the functions for these triggers, it passes a JSON payload, which the function receives as input. This payload contains a validationData attribute, which provides the data that you assigned to the ClientMetadata parameter in your InitiateAuth request. In your function code in AWS Lambda, you can process the validationData value to enhance your workflow for your specific needs.\nWhen you use the InitiateAuth API action, Amazon Cognito also invokes the functions for the following triggers, but it does not provide the ClientMetadata value as input:\n\nPost authentication\nCustom message\nPre token generation\nCreate auth challenge\nDefine auth challenge\nVerify auth challenge\n\nFor more information, see Customizing User Pool Workflows with Lambda Triggers in the Amazon Cognito Developer Guide .\n\nNote\nTake the following limitations into consideration when you use the ClientMetadata parameter:\n\nAmazon Cognito does not store the ClientMetadata value. This data is available only to AWS Lambda triggers that are assigned to a user pool to support custom workflows. If your user pool configuration does not include triggers, the ClientMetadata parameter serves no purpose.\nAmazon Cognito does not validate the ClientMetadata value.\nAmazon Cognito does not encrypt the the ClientMetadata value, so don\'t use it to provide sensitive information.\n\n\n\n(string) --\n(string) --\n\n\n\n

    :type ClientId: string
    :param ClientId: [REQUIRED]\nThe app client ID.\n

    :type AnalyticsMetadata: dict
    :param AnalyticsMetadata: The Amazon Pinpoint analytics metadata for collecting metrics for InitiateAuth calls.\n\nAnalyticsEndpointId (string) --The endpoint ID.\n\n\n

    :type UserContextData: dict
    :param UserContextData: Contextual data such as the user\'s device fingerprint, IP address, or location used for evaluating the risk of an unexpected event by Amazon Cognito advanced security.\n\nEncodedData (string) --Contextual data such as the user\'s device fingerprint, IP address, or location used for evaluating the risk of an unexpected event by Amazon Cognito advanced security.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ChallengeName': 'SMS_MFA'|'SOFTWARE_TOKEN_MFA'|'SELECT_MFA_TYPE'|'MFA_SETUP'|'PASSWORD_VERIFIER'|'CUSTOM_CHALLENGE'|'DEVICE_SRP_AUTH'|'DEVICE_PASSWORD_VERIFIER'|'ADMIN_NO_SRP_AUTH'|'NEW_PASSWORD_REQUIRED',
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


Response Structure

(dict) --
Initiates the authentication response.

ChallengeName (string) --
The name of the challenge which you are responding to with this call. This is returned to you in the AdminInitiateAuth response if you need to pass another challenge.
Valid values include the following. Note that all of these challenges require USERNAME and SECRET_HASH (if applicable) in the parameters.

SMS_MFA : Next challenge is to supply an SMS_MFA_CODE , delivered via SMS.
PASSWORD_VERIFIER : Next challenge is to supply PASSWORD_CLAIM_SIGNATURE , PASSWORD_CLAIM_SECRET_BLOCK , and TIMESTAMP after the client-side SRP calculations.
CUSTOM_CHALLENGE : This is returned if your custom authentication flow determines that the user should pass another challenge before tokens are issued.
DEVICE_SRP_AUTH : If device tracking was enabled on your user pool and the previous challenges were passed, this challenge is returned so that Amazon Cognito can start tracking this device.
DEVICE_PASSWORD_VERIFIER : Similar to PASSWORD_VERIFIER , but for devices only.
NEW_PASSWORD_REQUIRED : For users which are required to change their passwords after successful first login. This challenge should be passed with NEW_PASSWORD and any other required attributes.


Session (string) --
The session which should be passed both ways in challenge-response calls to the service. If the or API call determines that the caller needs to go through another challenge, they return a session with other challenge parameters. This session should be passed as it is to the next RespondToAuthChallenge API call.

ChallengeParameters (dict) --
The challenge parameters. These are returned to you in the InitiateAuth response if you need to pass another challenge. The responses in this parameter should be used to compute inputs to the next call (RespondToAuthChallenge ).
All challenges require USERNAME and SECRET_HASH (if applicable).

(string) --
(string) --




AuthenticationResult (dict) --
The result of the authentication response. This is only returned if the caller does not need to pass another challenge. If the caller does need to pass another challenge before it gets tokens, ChallengeName , ChallengeParameters , and Session are returned.

AccessToken (string) --
The access token.

ExpiresIn (integer) --
The expiration period of the authentication result in seconds.

TokenType (string) --
The token type.

RefreshToken (string) --
The refresh token.

IdToken (string) --
The ID token.

NewDeviceMetadata (dict) --
The new device metadata from an authentication result.

DeviceKey (string) --
The device key.

DeviceGroupKey (string) --
The device group key.











Exceptions

CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.UnexpectedLambdaException
CognitoIdentityProvider.Client.exceptions.InvalidUserPoolConfigurationException
CognitoIdentityProvider.Client.exceptions.UserLambdaValidationException
CognitoIdentityProvider.Client.exceptions.InvalidLambdaResponseException
CognitoIdentityProvider.Client.exceptions.PasswordResetRequiredException
CognitoIdentityProvider.Client.exceptions.UserNotFoundException
CognitoIdentityProvider.Client.exceptions.UserNotConfirmedException
CognitoIdentityProvider.Client.exceptions.InternalErrorException
CognitoIdentityProvider.Client.exceptions.InvalidSmsRoleAccessPolicyException
CognitoIdentityProvider.Client.exceptions.InvalidSmsRoleTrustRelationshipException


    :return: {
        'ChallengeName': 'SMS_MFA'|'SOFTWARE_TOKEN_MFA'|'SELECT_MFA_TYPE'|'MFA_SETUP'|'PASSWORD_VERIFIER'|'CUSTOM_CHALLENGE'|'DEVICE_SRP_AUTH'|'DEVICE_PASSWORD_VERIFIER'|'ADMIN_NO_SRP_AUTH'|'NEW_PASSWORD_REQUIRED',
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
    
    Exceptions
    
    :example: response = client.list_devices(
        AccessToken='string',
        Limit=123,
        PaginationToken='string'
    )
    
    
    :type AccessToken: string
    :param AccessToken: [REQUIRED]\nThe access tokens for the request to list devices.\n

    :type Limit: integer
    :param Limit: The limit of the device request.

    :type PaginationToken: string
    :param PaginationToken: The pagination token for the list request.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --
Represents the response to list devices.

Devices (list) --
The devices returned in the list devices response.

(dict) --
The device type.

DeviceKey (string) --
The device key.

DeviceAttributes (list) --
The device attributes.

(dict) --
Specifies whether the attribute is standard or custom.

Name (string) --
The name of the attribute.

Value (string) --
The value of the attribute.





DeviceCreateDate (datetime) --
The creation date of the device.

DeviceLastModifiedDate (datetime) --
The last modified date of the device.

DeviceLastAuthenticatedDate (datetime) --
The date in which the device was last authenticated.





PaginationToken (string) --
The pagination token for the list device response.







Exceptions

CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.InvalidUserPoolConfigurationException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.PasswordResetRequiredException
CognitoIdentityProvider.Client.exceptions.UserNotFoundException
CognitoIdentityProvider.Client.exceptions.UserNotConfirmedException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


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
    
    
    :returns: 
    CognitoIdentityProvider.Client.exceptions.InvalidParameterException
    CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
    CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
    CognitoIdentityProvider.Client.exceptions.InvalidUserPoolConfigurationException
    CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
    CognitoIdentityProvider.Client.exceptions.PasswordResetRequiredException
    CognitoIdentityProvider.Client.exceptions.UserNotFoundException
    CognitoIdentityProvider.Client.exceptions.UserNotConfirmedException
    CognitoIdentityProvider.Client.exceptions.InternalErrorException
    
    """
    pass

def list_groups(UserPoolId=None, Limit=None, NextToken=None):
    """
    Lists the groups associated with a user pool.
    Calling this action requires developer credentials.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_groups(
        UserPoolId='string',
        Limit=123,
        NextToken='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID for the user pool.\n

    :type Limit: integer
    :param Limit: The limit of the request to list groups.

    :type NextToken: string
    :param NextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

Groups (list) --
The group objects for the groups.

(dict) --
The group type.

GroupName (string) --
The name of the group.

UserPoolId (string) --
The user pool ID for the user pool.

Description (string) --
A string containing the description of the group.

RoleArn (string) --
The role ARN for the group.

Precedence (integer) --
A nonnegative integer value that specifies the precedence of this group relative to the other groups that a user can belong to in the user pool. If a user belongs to two or more groups, it is the group with the highest precedence whose role ARN will be used in the cognito:roles and cognito:preferred_role claims in the user\'s tokens. Groups with higher Precedence values take precedence over groups with lower Precedence values or with null Precedence values.
Two groups can have the same Precedence value. If this happens, neither group takes precedence over the other. If two groups with the same Precedence have the same role ARN, that role is used in the cognito:preferred_role claim in tokens for users in each group. If the two groups have different role ARNs, the cognito:preferred_role claim is not set in users\' tokens.
The default Precedence value is null.

LastModifiedDate (datetime) --
The date the group was last modified.

CreationDate (datetime) --
The date the group was created.





NextToken (string) --
An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.







Exceptions

CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


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
    
    
    :returns: 
    CognitoIdentityProvider.Client.exceptions.InvalidParameterException
    CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
    CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
    CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
    CognitoIdentityProvider.Client.exceptions.InternalErrorException
    
    """
    pass

def list_identity_providers(UserPoolId=None, MaxResults=None, NextToken=None):
    """
    Lists information about all identity providers for a user pool.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_identity_providers(
        UserPoolId='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID.\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of identity providers to return.

    :type NextToken: string
    :param NextToken: A pagination token.

    :rtype: dict

ReturnsResponse Syntax
{
    'Providers': [
        {
            'ProviderName': 'string',
            'ProviderType': 'SAML'|'Facebook'|'Google'|'LoginWithAmazon'|'SignInWithApple'|'OIDC',
            'LastModifiedDate': datetime(2015, 1, 1),
            'CreationDate': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Providers (list) --
A list of identity provider objects.

(dict) --
A container for identity provider details.

ProviderName (string) --
The identity provider name.

ProviderType (string) --
The identity provider type.

LastModifiedDate (datetime) --
The date the provider was last modified.

CreationDate (datetime) --
The date the provider was added to the user pool.





NextToken (string) --
A pagination token.







Exceptions

CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


    :return: {
        'Providers': [
            {
                'ProviderName': 'string',
                'ProviderType': 'SAML'|'Facebook'|'Google'|'LoginWithAmazon'|'SignInWithApple'|'OIDC',
                'LastModifiedDate': datetime(2015, 1, 1),
                'CreationDate': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    CognitoIdentityProvider.Client.exceptions.InvalidParameterException
    CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
    CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
    CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
    CognitoIdentityProvider.Client.exceptions.InternalErrorException
    
    """
    pass

def list_resource_servers(UserPoolId=None, MaxResults=None, NextToken=None):
    """
    Lists the resource servers for a user pool.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_resource_servers(
        UserPoolId='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID for the user pool.\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of resource servers to return.

    :type NextToken: string
    :param NextToken: A pagination token.

    :rtype: dict

ReturnsResponse Syntax
{
    'ResourceServers': [
        {
            'UserPoolId': 'string',
            'Identifier': 'string',
            'Name': 'string',
            'Scopes': [
                {
                    'ScopeName': 'string',
                    'ScopeDescription': 'string'
                },
            ]
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

ResourceServers (list) --
The resource servers.

(dict) --
A container for information about a resource server for a user pool.

UserPoolId (string) --
The user pool ID for the user pool that hosts the resource server.

Identifier (string) --
The identifier for the resource server.

Name (string) --
The name of the resource server.

Scopes (list) --
A list of scopes that are defined for the resource server.

(dict) --
A resource server scope.

ScopeName (string) --
The name of the scope.

ScopeDescription (string) --
A description of the scope.









NextToken (string) --
A pagination token.







Exceptions

CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


    :return: {
        'ResourceServers': [
            {
                'UserPoolId': 'string',
                'Identifier': 'string',
                'Name': 'string',
                'Scopes': [
                    {
                        'ScopeName': 'string',
                        'ScopeDescription': 'string'
                    },
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    CognitoIdentityProvider.Client.exceptions.InvalidParameterException
    CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
    CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
    CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
    CognitoIdentityProvider.Client.exceptions.InternalErrorException
    
    """
    pass

def list_tags_for_resource(ResourceArn=None):
    """
    Lists the tags that are assigned to an Amazon Cognito user pool.
    A tag is a label that you can apply to user pools to categorize and manage them in different ways, such as by purpose, owner, environment, or other criteria.
    You can use this action up to 10 times per second, per account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        ResourceArn='string'
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the user pool that the tags are assigned to.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --
Tags (dict) --The tags that are assigned to the user pool.

(string) --
(string) --









Exceptions

CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


    :return: {
        'Tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
    CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
    CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
    CognitoIdentityProvider.Client.exceptions.InvalidParameterException
    CognitoIdentityProvider.Client.exceptions.InternalErrorException
    
    """
    pass

def list_user_import_jobs(UserPoolId=None, MaxResults=None, PaginationToken=None):
    """
    Lists the user import jobs.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_user_import_jobs(
        UserPoolId='string',
        MaxResults=123,
        PaginationToken='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID for the user pool that the users are being imported into.\n

    :type MaxResults: integer
    :param MaxResults: [REQUIRED]\nThe maximum number of import jobs you want the request to return.\n

    :type PaginationToken: string
    :param PaginationToken: An identifier that was returned from the previous call to ListUserImportJobs , which can be used to return the next set of import jobs in the list.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --
Represents the response from the server to the request to list the user import jobs.

UserImportJobs (list) --
The user import jobs.

(dict) --
The user import job type.

JobName (string) --
The job name for the user import job.

JobId (string) --
The job ID for the user import job.

UserPoolId (string) --
The user pool ID for the user pool that the users are being imported into.

PreSignedUrl (string) --
The pre-signed URL to be used to upload the .csv file.

CreationDate (datetime) --
The date the user import job was created.

StartDate (datetime) --
The date when the user import job was started.

CompletionDate (datetime) --
The date when the user import job was completed.

Status (string) --
The status of the user import job. One of the following:

Created - The job was created but not started.
Pending - A transition state. You have started the job, but it has not begun importing users yet.
InProgress - The job has started, and users are being imported.
Stopping - You have stopped the job, but the job has not stopped importing users yet.
Stopped - You have stopped the job, and the job has stopped importing users.
Succeeded - The job has completed successfully.
Failed - The job has stopped due to an error.
Expired - You created a job, but did not start the job within 24-48 hours. All data associated with the job was deleted, and the job cannot be started.


CloudWatchLogsRoleArn (string) --
The role ARN for the Amazon CloudWatch Logging role for the user import job. For more information, see "Creating the CloudWatch Logs IAM Role" in the Amazon Cognito Developer Guide.

ImportedUsers (integer) --
The number of users that were successfully imported.

SkippedUsers (integer) --
The number of users that were skipped.

FailedUsers (integer) --
The number of users that could not be imported.

CompletionMessage (string) --
The message returned when the user import job is completed.





PaginationToken (string) --
An identifier that can be used to return the next set of user import jobs in the list.







Exceptions

CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


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
    
    Exceptions
    
    :example: response = client.list_user_pool_clients(
        UserPoolId='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID for the user pool where you want to list user pool clients.\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of results you want the request to return when listing the user pool clients.

    :type NextToken: string
    :param NextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :rtype: dict

ReturnsResponse Syntax
{
    'UserPoolClients': [
        {
            'ClientId': 'string',
            'UserPoolId': 'string',
            'ClientName': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
Represents the response from the server that lists user pool clients.

UserPoolClients (list) --
The user pool clients in the response that lists user pool clients.

(dict) --
The description of the user pool client.

ClientId (string) --
The ID of the client associated with the user pool.

UserPoolId (string) --
The user pool ID for the user pool where you want to describe the user pool client.

ClientName (string) --
The client name from the user pool client description.





NextToken (string) --
An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.







Exceptions

CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


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
    
    
    :returns: 
    CognitoIdentityProvider.Client.exceptions.InvalidParameterException
    CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
    CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
    CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
    CognitoIdentityProvider.Client.exceptions.InternalErrorException
    
    """
    pass

def list_user_pools(NextToken=None, MaxResults=None):
    """
    Lists the user pools associated with an AWS account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_user_pools(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :type MaxResults: integer
    :param MaxResults: [REQUIRED]\nThe maximum number of results you want the request to return when listing the user pools.\n

    :rtype: dict

ReturnsResponse Syntax
{
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
                'VerifyAuthChallengeResponse': 'string',
                'PreTokenGeneration': 'string',
                'UserMigration': 'string'
            },
            'Status': 'Enabled'|'Disabled',
            'LastModifiedDate': datetime(2015, 1, 1),
            'CreationDate': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
Represents the response to list user pools.

UserPools (list) --
The user pools from the response to list users.

(dict) --
A user pool description.

Id (string) --
The ID in a user pool description.

Name (string) --
The name in a user pool description.

LambdaConfig (dict) --
The AWS Lambda configuration information in a user pool description.

PreSignUp (string) --
A pre-registration AWS Lambda trigger.

CustomMessage (string) --
A custom Message AWS Lambda trigger.

PostConfirmation (string) --
A post-confirmation AWS Lambda trigger.

PreAuthentication (string) --
A pre-authentication AWS Lambda trigger.

PostAuthentication (string) --
A post-authentication AWS Lambda trigger.

DefineAuthChallenge (string) --
Defines the authentication challenge.

CreateAuthChallenge (string) --
Creates an authentication challenge.

VerifyAuthChallengeResponse (string) --
Verifies the authentication challenge response.

PreTokenGeneration (string) --
A Lambda trigger that is invoked before token generation.

UserMigration (string) --
The user migration Lambda config type.



Status (string) --
The user pool status in a user pool description.

LastModifiedDate (datetime) --
The date the user pool description was last modified.

CreationDate (datetime) --
The date the user pool description was created.





NextToken (string) --
An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.







Exceptions

CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


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
                    'VerifyAuthChallengeResponse': 'string',
                    'PreTokenGeneration': 'string',
                    'UserMigration': 'string'
                },
                'Status': 'Enabled'|'Disabled',
                'LastModifiedDate': datetime(2015, 1, 1),
                'CreationDate': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    CognitoIdentityProvider.Client.exceptions.InvalidParameterException
    CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
    CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
    CognitoIdentityProvider.Client.exceptions.InternalErrorException
    
    """
    pass

def list_users(UserPoolId=None, AttributesToGet=None, Limit=None, PaginationToken=None, Filter=None):
    """
    Lists the users in the Amazon Cognito user pool.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param UserPoolId: [REQUIRED]\nThe user pool ID for the user pool on which the search should be performed.\n

    :type AttributesToGet: list
    :param AttributesToGet: An array of strings, where each string is the name of a user attribute to be returned for each user in the search results. If the array is null, all attributes are returned.\n\n(string) --\n\n

    :type Limit: integer
    :param Limit: Maximum number of users to be returned.

    :type PaginationToken: string
    :param PaginationToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :type Filter: string
    :param Filter: A filter string of the form 'AttributeName Filter-Type 'AttributeValue ''. Quotation marks within the filter string must be escaped using the backslash () character. For example, 'family_name = 'Reddy''.\n\nAttributeName : The name of the attribute to search for. You can only search for one attribute at a time.\nFilter-Type : For an exact match, use =, for example, 'given_name = 'Jon''. For a prefix ('starts with') match, use ^=, for example, 'given_name ^= 'Jon''.\nAttributeValue : The attribute value that must be matched for each user.\n\nIf the filter string is empty, ListUsers returns all users in the user pool.\nYou can only search for the following standard attributes:\n\nusername (case-sensitive)\nemail\nphone_number\nname\ngiven_name\nfamily_name\npreferred_username\ncognito:user_status (called Status in the Console) (case-insensitive)\nstatus (called **Enabled** in the Console) (case-sensitive)\nsub\n\nCustom attributes are not searchable.\nFor more information, see Searching for Users Using the ListUsers API and Examples of Using the ListUsers API in the Amazon Cognito Developer Guide .\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --
The response from the request to list users.

Users (list) --
The users returned in the request to list users.

(dict) --
The user type.

Username (string) --
The user name of the user you wish to describe.

Attributes (list) --
A container with information about the user type attributes.

(dict) --
Specifies whether the attribute is standard or custom.

Name (string) --
The name of the attribute.

Value (string) --
The value of the attribute.





UserCreateDate (datetime) --
The creation date of the user.

UserLastModifiedDate (datetime) --
The last modified date of the user.

Enabled (boolean) --
Specifies whether the user is enabled.

UserStatus (string) --
The user status. Can be one of the following:

UNCONFIRMED - User has been created but not confirmed.
CONFIRMED - User has been confirmed.
ARCHIVED - User is no longer active.
COMPROMISED - User is disabled due to a potential security threat.
UNKNOWN - User status is not known.
RESET_REQUIRED - User is confirmed, but the user must request a code and reset his or her password before he or she can sign in.
FORCE_CHANGE_PASSWORD - The user is confirmed and the user can sign in using a temporary password, but on first sign-in, the user must change his or her password to a new value before doing anything else.


MFAOptions (list) --
The MFA options for the user.

(dict) --

This data type is no longer supported. You can use it only for SMS MFA configurations. You can\'t use it for TOTP software token MFA configurations.

To set either type of MFA configuration, use the  AdminSetUserMFAPreference or  SetUserMFAPreference actions.
To look up information about either type of MFA configuration, use the  AdminGetUserResponse$UserMFASettingList or  GetUserResponse$UserMFASettingList responses.

DeliveryMedium (string) --
The delivery medium to send the MFA code. You can use this parameter to set only the SMS delivery medium value.

AttributeName (string) --
The attribute name of the MFA option type. The only valid value is phone_number .









PaginationToken (string) --
An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.







Exceptions

CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


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
    RESET_REQUIRED - User is confirmed, but the user must request a code and reset his or her password before he or she can sign in.
    FORCE_CHANGE_PASSWORD - The user is confirmed and the user can sign in using a temporary password, but on first sign-in, the user must change his or her password to a new value before doing anything else.
    
    """
    pass

def list_users_in_group(UserPoolId=None, GroupName=None, Limit=None, NextToken=None):
    """
    Lists the users in the specified group.
    Calling this action requires developer credentials.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_users_in_group(
        UserPoolId='string',
        GroupName='string',
        Limit=123,
        NextToken='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID for the user pool.\n

    :type GroupName: string
    :param GroupName: [REQUIRED]\nThe name of the group.\n

    :type Limit: integer
    :param Limit: The limit of the request to list users.

    :type NextToken: string
    :param NextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

Users (list) --
The users returned in the request to list users.

(dict) --
The user type.

Username (string) --
The user name of the user you wish to describe.

Attributes (list) --
A container with information about the user type attributes.

(dict) --
Specifies whether the attribute is standard or custom.

Name (string) --
The name of the attribute.

Value (string) --
The value of the attribute.





UserCreateDate (datetime) --
The creation date of the user.

UserLastModifiedDate (datetime) --
The last modified date of the user.

Enabled (boolean) --
Specifies whether the user is enabled.

UserStatus (string) --
The user status. Can be one of the following:

UNCONFIRMED - User has been created but not confirmed.
CONFIRMED - User has been confirmed.
ARCHIVED - User is no longer active.
COMPROMISED - User is disabled due to a potential security threat.
UNKNOWN - User status is not known.
RESET_REQUIRED - User is confirmed, but the user must request a code and reset his or her password before he or she can sign in.
FORCE_CHANGE_PASSWORD - The user is confirmed and the user can sign in using a temporary password, but on first sign-in, the user must change his or her password to a new value before doing anything else.


MFAOptions (list) --
The MFA options for the user.

(dict) --

This data type is no longer supported. You can use it only for SMS MFA configurations. You can\'t use it for TOTP software token MFA configurations.

To set either type of MFA configuration, use the  AdminSetUserMFAPreference or  SetUserMFAPreference actions.
To look up information about either type of MFA configuration, use the  AdminGetUserResponse$UserMFASettingList or  GetUserResponse$UserMFASettingList responses.

DeliveryMedium (string) --
The delivery medium to send the MFA code. You can use this parameter to set only the SMS delivery medium value.

AttributeName (string) --
The attribute name of the MFA option type. The only valid value is phone_number .









NextToken (string) --
An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.







Exceptions

CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


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
    RESET_REQUIRED - User is confirmed, but the user must request a code and reset his or her password before he or she can sign in.
    FORCE_CHANGE_PASSWORD - The user is confirmed and the user can sign in using a temporary password, but on first sign-in, the user must change his or her password to a new value before doing anything else.
    
    """
    pass

def resend_confirmation_code(ClientId=None, SecretHash=None, UserContextData=None, Username=None, AnalyticsMetadata=None, ClientMetadata=None):
    """
    Resends the confirmation (for confirmation of registration) to a specific user in the user pool.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.resend_confirmation_code(
        ClientId='string',
        SecretHash='string',
        UserContextData={
            'EncodedData': 'string'
        },
        Username='string',
        AnalyticsMetadata={
            'AnalyticsEndpointId': 'string'
        },
        ClientMetadata={
            'string': 'string'
        }
    )
    
    
    :type ClientId: string
    :param ClientId: [REQUIRED]\nThe ID of the client associated with the user pool.\n

    :type SecretHash: string
    :param SecretHash: A keyed-hash message authentication code (HMAC) calculated using the secret key of a user pool client and username plus the client ID in the message.

    :type UserContextData: dict
    :param UserContextData: Contextual data such as the user\'s device fingerprint, IP address, or location used for evaluating the risk of an unexpected event by Amazon Cognito advanced security.\n\nEncodedData (string) --Contextual data such as the user\'s device fingerprint, IP address, or location used for evaluating the risk of an unexpected event by Amazon Cognito advanced security.\n\n\n

    :type Username: string
    :param Username: [REQUIRED]\nThe user name of the user to whom you wish to resend a confirmation code.\n

    :type AnalyticsMetadata: dict
    :param AnalyticsMetadata: The Amazon Pinpoint analytics metadata for collecting metrics for ResendConfirmationCode calls.\n\nAnalyticsEndpointId (string) --The endpoint ID.\n\n\n

    :type ClientMetadata: dict
    :param ClientMetadata: A map of custom key-value pairs that you can provide as input for any custom workflows that this action triggers.\nYou create custom workflows by assigning AWS Lambda functions to user pool triggers. When you use the ResendConfirmationCode API action, Amazon Cognito invokes the function that is assigned to the custom message trigger. When Amazon Cognito invokes this function, it passes a JSON payload, which the function receives as input. This payload contains a clientMetadata attribute, which provides the data that you assigned to the ClientMetadata parameter in your ResendConfirmationCode request. In your function code in AWS Lambda, you can process the clientMetadata value to enhance your workflow for your specific needs.\nFor more information, see Customizing User Pool Workflows with Lambda Triggers in the Amazon Cognito Developer Guide .\n\nNote\nTake the following limitations into consideration when you use the ClientMetadata parameter:\n\nAmazon Cognito does not store the ClientMetadata value. This data is available only to AWS Lambda triggers that are assigned to a user pool to support custom workflows. If your user pool configuration does not include triggers, the ClientMetadata parameter serves no purpose.\nAmazon Cognito does not validate the ClientMetadata value.\nAmazon Cognito does not encrypt the the ClientMetadata value, so don\'t use it to provide sensitive information.\n\n\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'CodeDeliveryDetails': {
        'Destination': 'string',
        'DeliveryMedium': 'SMS'|'EMAIL',
        'AttributeName': 'string'
    }
}


Response Structure

(dict) --
The response from the server when the Amazon Cognito Your User Pools service makes the request to resend a confirmation code.

CodeDeliveryDetails (dict) --
The code delivery details returned by the server in response to the request to resend the confirmation code.

Destination (string) --
The destination for the code delivery details.

DeliveryMedium (string) --
The delivery medium (email message or phone number).

AttributeName (string) --
The attribute name.









Exceptions

CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.UnexpectedLambdaException
CognitoIdentityProvider.Client.exceptions.UserLambdaValidationException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.InvalidLambdaResponseException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.LimitExceededException
CognitoIdentityProvider.Client.exceptions.InvalidSmsRoleAccessPolicyException
CognitoIdentityProvider.Client.exceptions.InvalidSmsRoleTrustRelationshipException
CognitoIdentityProvider.Client.exceptions.InvalidEmailRoleAccessPolicyException
CognitoIdentityProvider.Client.exceptions.CodeDeliveryFailureException
CognitoIdentityProvider.Client.exceptions.UserNotFoundException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


    :return: {
        'CodeDeliveryDetails': {
            'Destination': 'string',
            'DeliveryMedium': 'SMS'|'EMAIL',
            'AttributeName': 'string'
        }
    }
    
    
    :returns: 
    CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
    CognitoIdentityProvider.Client.exceptions.InvalidParameterException
    CognitoIdentityProvider.Client.exceptions.UnexpectedLambdaException
    CognitoIdentityProvider.Client.exceptions.UserLambdaValidationException
    CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
    CognitoIdentityProvider.Client.exceptions.InvalidLambdaResponseException
    CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
    CognitoIdentityProvider.Client.exceptions.LimitExceededException
    CognitoIdentityProvider.Client.exceptions.InvalidSmsRoleAccessPolicyException
    CognitoIdentityProvider.Client.exceptions.InvalidSmsRoleTrustRelationshipException
    CognitoIdentityProvider.Client.exceptions.InvalidEmailRoleAccessPolicyException
    CognitoIdentityProvider.Client.exceptions.CodeDeliveryFailureException
    CognitoIdentityProvider.Client.exceptions.UserNotFoundException
    CognitoIdentityProvider.Client.exceptions.InternalErrorException
    
    """
    pass

def respond_to_auth_challenge(ClientId=None, ChallengeName=None, Session=None, ChallengeResponses=None, AnalyticsMetadata=None, UserContextData=None, ClientMetadata=None):
    """
    Responds to the authentication challenge.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.respond_to_auth_challenge(
        ClientId='string',
        ChallengeName='SMS_MFA'|'SOFTWARE_TOKEN_MFA'|'SELECT_MFA_TYPE'|'MFA_SETUP'|'PASSWORD_VERIFIER'|'CUSTOM_CHALLENGE'|'DEVICE_SRP_AUTH'|'DEVICE_PASSWORD_VERIFIER'|'ADMIN_NO_SRP_AUTH'|'NEW_PASSWORD_REQUIRED',
        Session='string',
        ChallengeResponses={
            'string': 'string'
        },
        AnalyticsMetadata={
            'AnalyticsEndpointId': 'string'
        },
        UserContextData={
            'EncodedData': 'string'
        },
        ClientMetadata={
            'string': 'string'
        }
    )
    
    
    :type ClientId: string
    :param ClientId: [REQUIRED]\nThe app client ID.\n

    :type ChallengeName: string
    :param ChallengeName: [REQUIRED]\nThe challenge name. For more information, see .\n\nADMIN_NO_SRP_AUTH is not a valid value.\n

    :type Session: string
    :param Session: The session which should be passed both ways in challenge-response calls to the service. If InitiateAuth or RespondToAuthChallenge API call determines that the caller needs to go through another challenge, they return a session with other challenge parameters. This session should be passed as it is to the next RespondToAuthChallenge API call.

    :type ChallengeResponses: dict
    :param ChallengeResponses: The challenge responses. These are inputs corresponding to the value of ChallengeName , for example:\n\nNote\nSECRET_HASH (if app client is configured with client secret) applies to all inputs below (including SOFTWARE_TOKEN_MFA ).\n\n\nSMS_MFA : SMS_MFA_CODE , USERNAME .\nPASSWORD_VERIFIER : PASSWORD_CLAIM_SIGNATURE , PASSWORD_CLAIM_SECRET_BLOCK , TIMESTAMP , USERNAME .\nNEW_PASSWORD_REQUIRED : NEW_PASSWORD , any other required attributes, USERNAME .\nSOFTWARE_TOKEN_MFA : USERNAME and SOFTWARE_TOKEN_MFA_CODE are required attributes.\nDEVICE_SRP_AUTH requires USERNAME , DEVICE_KEY , SRP_A (and SECRET_HASH ).\nDEVICE_PASSWORD_VERIFIER requires everything that PASSWORD_VERIFIER requires plus DEVICE_KEY .\n\n\n(string) --\n(string) --\n\n\n\n

    :type AnalyticsMetadata: dict
    :param AnalyticsMetadata: The Amazon Pinpoint analytics metadata for collecting metrics for RespondToAuthChallenge calls.\n\nAnalyticsEndpointId (string) --The endpoint ID.\n\n\n

    :type UserContextData: dict
    :param UserContextData: Contextual data such as the user\'s device fingerprint, IP address, or location used for evaluating the risk of an unexpected event by Amazon Cognito advanced security.\n\nEncodedData (string) --Contextual data such as the user\'s device fingerprint, IP address, or location used for evaluating the risk of an unexpected event by Amazon Cognito advanced security.\n\n\n

    :type ClientMetadata: dict
    :param ClientMetadata: A map of custom key-value pairs that you can provide as input for any custom workflows that this action triggers.\nYou create custom workflows by assigning AWS Lambda functions to user pool triggers. When you use the RespondToAuthChallenge API action, Amazon Cognito invokes any functions that are assigned to the following triggers: post authentication , pre token generation , define auth challenge , create auth challenge , and verify auth challenge . When Amazon Cognito invokes any of these functions, it passes a JSON payload, which the function receives as input. This payload contains a clientMetadata attribute, which provides the data that you assigned to the ClientMetadata parameter in your RespondToAuthChallenge request. In your function code in AWS Lambda, you can process the clientMetadata value to enhance your workflow for your specific needs.\nFor more information, see Customizing User Pool Workflows with Lambda Triggers in the Amazon Cognito Developer Guide .\n\nNote\nTake the following limitations into consideration when you use the ClientMetadata parameter:\n\nAmazon Cognito does not store the ClientMetadata value. This data is available only to AWS Lambda triggers that are assigned to a user pool to support custom workflows. If your user pool configuration does not include triggers, the ClientMetadata parameter serves no purpose.\nAmazon Cognito does not validate the ClientMetadata value.\nAmazon Cognito does not encrypt the the ClientMetadata value, so don\'t use it to provide sensitive information.\n\n\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ChallengeName': 'SMS_MFA'|'SOFTWARE_TOKEN_MFA'|'SELECT_MFA_TYPE'|'MFA_SETUP'|'PASSWORD_VERIFIER'|'CUSTOM_CHALLENGE'|'DEVICE_SRP_AUTH'|'DEVICE_PASSWORD_VERIFIER'|'ADMIN_NO_SRP_AUTH'|'NEW_PASSWORD_REQUIRED',
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


Response Structure

(dict) --
The response to respond to the authentication challenge.

ChallengeName (string) --
The challenge name. For more information, see .

Session (string) --
The session which should be passed both ways in challenge-response calls to the service. If the or API call determines that the caller needs to go through another challenge, they return a session with other challenge parameters. This session should be passed as it is to the next RespondToAuthChallenge API call.

ChallengeParameters (dict) --
The challenge parameters. For more information, see .

(string) --
(string) --




AuthenticationResult (dict) --
The result returned by the server in response to the request to respond to the authentication challenge.

AccessToken (string) --
The access token.

ExpiresIn (integer) --
The expiration period of the authentication result in seconds.

TokenType (string) --
The token type.

RefreshToken (string) --
The refresh token.

IdToken (string) --
The ID token.

NewDeviceMetadata (dict) --
The new device metadata from an authentication result.

DeviceKey (string) --
The device key.

DeviceGroupKey (string) --
The device group key.











Exceptions

CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.CodeMismatchException
CognitoIdentityProvider.Client.exceptions.ExpiredCodeException
CognitoIdentityProvider.Client.exceptions.UnexpectedLambdaException
CognitoIdentityProvider.Client.exceptions.UserLambdaValidationException
CognitoIdentityProvider.Client.exceptions.InvalidPasswordException
CognitoIdentityProvider.Client.exceptions.InvalidLambdaResponseException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.InvalidUserPoolConfigurationException
CognitoIdentityProvider.Client.exceptions.MFAMethodNotFoundException
CognitoIdentityProvider.Client.exceptions.PasswordResetRequiredException
CognitoIdentityProvider.Client.exceptions.UserNotFoundException
CognitoIdentityProvider.Client.exceptions.UserNotConfirmedException
CognitoIdentityProvider.Client.exceptions.InvalidSmsRoleAccessPolicyException
CognitoIdentityProvider.Client.exceptions.InvalidSmsRoleTrustRelationshipException
CognitoIdentityProvider.Client.exceptions.AliasExistsException
CognitoIdentityProvider.Client.exceptions.InternalErrorException
CognitoIdentityProvider.Client.exceptions.SoftwareTokenMFANotFoundException


    :return: {
        'ChallengeName': 'SMS_MFA'|'SOFTWARE_TOKEN_MFA'|'SELECT_MFA_TYPE'|'MFA_SETUP'|'PASSWORD_VERIFIER'|'CUSTOM_CHALLENGE'|'DEVICE_SRP_AUTH'|'DEVICE_PASSWORD_VERIFIER'|'ADMIN_NO_SRP_AUTH'|'NEW_PASSWORD_REQUIRED',
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

def set_risk_configuration(UserPoolId=None, ClientId=None, CompromisedCredentialsRiskConfiguration=None, AccountTakeoverRiskConfiguration=None, RiskExceptionConfiguration=None):
    """
    Configures actions on detected risks. To delete the risk configuration for UserPoolId or ClientId , pass null values for all four configuration types.
    To enable Amazon Cognito advanced security features, update the user pool to include the UserPoolAddOns key``AdvancedSecurityMode`` .
    See .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.set_risk_configuration(
        UserPoolId='string',
        ClientId='string',
        CompromisedCredentialsRiskConfiguration={
            'EventFilter': [
                'SIGN_IN'|'PASSWORD_CHANGE'|'SIGN_UP',
            ],
            'Actions': {
                'EventAction': 'BLOCK'|'NO_ACTION'
            }
        },
        AccountTakeoverRiskConfiguration={
            'NotifyConfiguration': {
                'From': 'string',
                'ReplyTo': 'string',
                'SourceArn': 'string',
                'BlockEmail': {
                    'Subject': 'string',
                    'HtmlBody': 'string',
                    'TextBody': 'string'
                },
                'NoActionEmail': {
                    'Subject': 'string',
                    'HtmlBody': 'string',
                    'TextBody': 'string'
                },
                'MfaEmail': {
                    'Subject': 'string',
                    'HtmlBody': 'string',
                    'TextBody': 'string'
                }
            },
            'Actions': {
                'LowAction': {
                    'Notify': True|False,
                    'EventAction': 'BLOCK'|'MFA_IF_CONFIGURED'|'MFA_REQUIRED'|'NO_ACTION'
                },
                'MediumAction': {
                    'Notify': True|False,
                    'EventAction': 'BLOCK'|'MFA_IF_CONFIGURED'|'MFA_REQUIRED'|'NO_ACTION'
                },
                'HighAction': {
                    'Notify': True|False,
                    'EventAction': 'BLOCK'|'MFA_IF_CONFIGURED'|'MFA_REQUIRED'|'NO_ACTION'
                }
            }
        },
        RiskExceptionConfiguration={
            'BlockedIPRangeList': [
                'string',
            ],
            'SkippedIPRangeList': [
                'string',
            ]
        }
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID.\n

    :type ClientId: string
    :param ClientId: The app client ID. If ClientId is null, then the risk configuration is mapped to userPoolId . When the client ID is null, the same risk configuration is applied to all the clients in the userPool.\nOtherwise, ClientId is mapped to the client. When the client ID is not null, the user pool configuration is overridden and the risk configuration for the client is used instead.\n

    :type CompromisedCredentialsRiskConfiguration: dict
    :param CompromisedCredentialsRiskConfiguration: The compromised credentials risk configuration.\n\nEventFilter (list) --Perform the action for these events. The default is to perform all events if no event filter is specified.\n\n(string) --\n\n\nActions (dict) -- [REQUIRED]The compromised credentials risk configuration actions.\n\nEventAction (string) -- [REQUIRED]The event action.\n\n\n\n\n

    :type AccountTakeoverRiskConfiguration: dict
    :param AccountTakeoverRiskConfiguration: The account takeover risk configuration.\n\nNotifyConfiguration (dict) --The notify configuration used to construct email notifications.\n\nFrom (string) --The email address that is sending the email. It must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES.\n\nReplyTo (string) --The destination to which the receiver of an email should reply to.\n\nSourceArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the identity that is associated with the sending authorization policy. It permits Amazon Cognito to send for the email address specified in the From parameter.\n\nBlockEmail (dict) --Email template used when a detected risk event is blocked.\n\nSubject (string) -- [REQUIRED]The subject.\n\nHtmlBody (string) --The HTML body.\n\nTextBody (string) --The text body.\n\n\n\nNoActionEmail (dict) --The email template used when a detected risk event is allowed.\n\nSubject (string) -- [REQUIRED]The subject.\n\nHtmlBody (string) --The HTML body.\n\nTextBody (string) --The text body.\n\n\n\nMfaEmail (dict) --The MFA email template used when MFA is challenged as part of a detected risk.\n\nSubject (string) -- [REQUIRED]The subject.\n\nHtmlBody (string) --The HTML body.\n\nTextBody (string) --The text body.\n\n\n\n\n\nActions (dict) -- [REQUIRED]Account takeover risk configuration actions\n\nLowAction (dict) --Action to take for a low risk.\n\nNotify (boolean) -- [REQUIRED]Flag specifying whether to send a notification.\n\nEventAction (string) -- [REQUIRED]The event action.\n\nBLOCK Choosing this action will block the request.\nMFA_IF_CONFIGURED Throw MFA challenge if user has configured it, else allow the request.\nMFA_REQUIRED Throw MFA challenge if user has configured it, else block the request.\nNO_ACTION Allow the user sign-in.\n\n\n\n\nMediumAction (dict) --Action to take for a medium risk.\n\nNotify (boolean) -- [REQUIRED]Flag specifying whether to send a notification.\n\nEventAction (string) -- [REQUIRED]The event action.\n\nBLOCK Choosing this action will block the request.\nMFA_IF_CONFIGURED Throw MFA challenge if user has configured it, else allow the request.\nMFA_REQUIRED Throw MFA challenge if user has configured it, else block the request.\nNO_ACTION Allow the user sign-in.\n\n\n\n\nHighAction (dict) --Action to take for a high risk.\n\nNotify (boolean) -- [REQUIRED]Flag specifying whether to send a notification.\n\nEventAction (string) -- [REQUIRED]The event action.\n\nBLOCK Choosing this action will block the request.\nMFA_IF_CONFIGURED Throw MFA challenge if user has configured it, else allow the request.\nMFA_REQUIRED Throw MFA challenge if user has configured it, else block the request.\nNO_ACTION Allow the user sign-in.\n\n\n\n\n\n\n\n

    :type RiskExceptionConfiguration: dict
    :param RiskExceptionConfiguration: The configuration to override the risk decision.\n\nBlockedIPRangeList (list) --Overrides the risk decision to always block the pre-authentication requests. The IP range is in CIDR notation: a compact representation of an IP address and its associated routing prefix.\n\n(string) --\n\n\nSkippedIPRangeList (list) --Risk detection is not performed on the IP addresses in the range list. The IP range is in CIDR notation.\n\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'RiskConfiguration': {
        'UserPoolId': 'string',
        'ClientId': 'string',
        'CompromisedCredentialsRiskConfiguration': {
            'EventFilter': [
                'SIGN_IN'|'PASSWORD_CHANGE'|'SIGN_UP',
            ],
            'Actions': {
                'EventAction': 'BLOCK'|'NO_ACTION'
            }
        },
        'AccountTakeoverRiskConfiguration': {
            'NotifyConfiguration': {
                'From': 'string',
                'ReplyTo': 'string',
                'SourceArn': 'string',
                'BlockEmail': {
                    'Subject': 'string',
                    'HtmlBody': 'string',
                    'TextBody': 'string'
                },
                'NoActionEmail': {
                    'Subject': 'string',
                    'HtmlBody': 'string',
                    'TextBody': 'string'
                },
                'MfaEmail': {
                    'Subject': 'string',
                    'HtmlBody': 'string',
                    'TextBody': 'string'
                }
            },
            'Actions': {
                'LowAction': {
                    'Notify': True|False,
                    'EventAction': 'BLOCK'|'MFA_IF_CONFIGURED'|'MFA_REQUIRED'|'NO_ACTION'
                },
                'MediumAction': {
                    'Notify': True|False,
                    'EventAction': 'BLOCK'|'MFA_IF_CONFIGURED'|'MFA_REQUIRED'|'NO_ACTION'
                },
                'HighAction': {
                    'Notify': True|False,
                    'EventAction': 'BLOCK'|'MFA_IF_CONFIGURED'|'MFA_REQUIRED'|'NO_ACTION'
                }
            }
        },
        'RiskExceptionConfiguration': {
            'BlockedIPRangeList': [
                'string',
            ],
            'SkippedIPRangeList': [
                'string',
            ]
        },
        'LastModifiedDate': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --

RiskConfiguration (dict) --
The risk configuration.

UserPoolId (string) --
The user pool ID.

ClientId (string) --
The app client ID.

CompromisedCredentialsRiskConfiguration (dict) --
The compromised credentials risk configuration object including the EventFilter and the EventAction

EventFilter (list) --
Perform the action for these events. The default is to perform all events if no event filter is specified.

(string) --


Actions (dict) --
The compromised credentials risk configuration actions.

EventAction (string) --
The event action.





AccountTakeoverRiskConfiguration (dict) --
The account takeover risk configuration object including the NotifyConfiguration object and Actions to take in the case of an account takeover.

NotifyConfiguration (dict) --
The notify configuration used to construct email notifications.

From (string) --
The email address that is sending the email. It must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES.

ReplyTo (string) --
The destination to which the receiver of an email should reply to.

SourceArn (string) --
The Amazon Resource Name (ARN) of the identity that is associated with the sending authorization policy. It permits Amazon Cognito to send for the email address specified in the From parameter.

BlockEmail (dict) --
Email template used when a detected risk event is blocked.

Subject (string) --
The subject.

HtmlBody (string) --
The HTML body.

TextBody (string) --
The text body.



NoActionEmail (dict) --
The email template used when a detected risk event is allowed.

Subject (string) --
The subject.

HtmlBody (string) --
The HTML body.

TextBody (string) --
The text body.



MfaEmail (dict) --
The MFA email template used when MFA is challenged as part of a detected risk.

Subject (string) --
The subject.

HtmlBody (string) --
The HTML body.

TextBody (string) --
The text body.





Actions (dict) --
Account takeover risk configuration actions

LowAction (dict) --
Action to take for a low risk.

Notify (boolean) --
Flag specifying whether to send a notification.

EventAction (string) --
The event action.

BLOCK Choosing this action will block the request.
MFA_IF_CONFIGURED Throw MFA challenge if user has configured it, else allow the request.
MFA_REQUIRED Throw MFA challenge if user has configured it, else block the request.
NO_ACTION Allow the user sign-in.




MediumAction (dict) --
Action to take for a medium risk.

Notify (boolean) --
Flag specifying whether to send a notification.

EventAction (string) --
The event action.

BLOCK Choosing this action will block the request.
MFA_IF_CONFIGURED Throw MFA challenge if user has configured it, else allow the request.
MFA_REQUIRED Throw MFA challenge if user has configured it, else block the request.
NO_ACTION Allow the user sign-in.




HighAction (dict) --
Action to take for a high risk.

Notify (boolean) --
Flag specifying whether to send a notification.

EventAction (string) --
The event action.

BLOCK Choosing this action will block the request.
MFA_IF_CONFIGURED Throw MFA challenge if user has configured it, else allow the request.
MFA_REQUIRED Throw MFA challenge if user has configured it, else block the request.
NO_ACTION Allow the user sign-in.








RiskExceptionConfiguration (dict) --
The configuration to override the risk decision.

BlockedIPRangeList (list) --
Overrides the risk decision to always block the pre-authentication requests. The IP range is in CIDR notation: a compact representation of an IP address and its associated routing prefix.

(string) --


SkippedIPRangeList (list) --
Risk detection is not performed on the IP addresses in the range list. The IP range is in CIDR notation.

(string) --




LastModifiedDate (datetime) --
The last modified date.









Exceptions

CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.UserPoolAddOnNotEnabledException
CognitoIdentityProvider.Client.exceptions.CodeDeliveryFailureException
CognitoIdentityProvider.Client.exceptions.InvalidEmailRoleAccessPolicyException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


    :return: {
        'RiskConfiguration': {
            'UserPoolId': 'string',
            'ClientId': 'string',
            'CompromisedCredentialsRiskConfiguration': {
                'EventFilter': [
                    'SIGN_IN'|'PASSWORD_CHANGE'|'SIGN_UP',
                ],
                'Actions': {
                    'EventAction': 'BLOCK'|'NO_ACTION'
                }
            },
            'AccountTakeoverRiskConfiguration': {
                'NotifyConfiguration': {
                    'From': 'string',
                    'ReplyTo': 'string',
                    'SourceArn': 'string',
                    'BlockEmail': {
                        'Subject': 'string',
                        'HtmlBody': 'string',
                        'TextBody': 'string'
                    },
                    'NoActionEmail': {
                        'Subject': 'string',
                        'HtmlBody': 'string',
                        'TextBody': 'string'
                    },
                    'MfaEmail': {
                        'Subject': 'string',
                        'HtmlBody': 'string',
                        'TextBody': 'string'
                    }
                },
                'Actions': {
                    'LowAction': {
                        'Notify': True|False,
                        'EventAction': 'BLOCK'|'MFA_IF_CONFIGURED'|'MFA_REQUIRED'|'NO_ACTION'
                    },
                    'MediumAction': {
                        'Notify': True|False,
                        'EventAction': 'BLOCK'|'MFA_IF_CONFIGURED'|'MFA_REQUIRED'|'NO_ACTION'
                    },
                    'HighAction': {
                        'Notify': True|False,
                        'EventAction': 'BLOCK'|'MFA_IF_CONFIGURED'|'MFA_REQUIRED'|'NO_ACTION'
                    }
                }
            },
            'RiskExceptionConfiguration': {
                'BlockedIPRangeList': [
                    'string',
                ],
                'SkippedIPRangeList': [
                    'string',
                ]
            },
            'LastModifiedDate': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def set_ui_customization(UserPoolId=None, ClientId=None, CSS=None, ImageFile=None):
    """
    Sets the UI customization information for a user pool\'s built-in app UI.
    You can specify app UI customization settings for a single client (with a specific clientId ) or for all clients (by setting the clientId to ALL ). If you specify ALL , the default configuration will be used for every client that has no UI customization set previously. If you specify UI customization settings for a particular client, it will no longer fall back to the ALL configuration.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.set_ui_customization(
        UserPoolId='string',
        ClientId='string',
        CSS='string',
        ImageFile=b'bytes'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID for the user pool.\n

    :type ClientId: string
    :param ClientId: The client ID for the client app.

    :type CSS: string
    :param CSS: The CSS values in the UI customization.

    :type ImageFile: bytes
    :param ImageFile: The uploaded logo image for the UI customization.

    :rtype: dict

ReturnsResponse Syntax
{
    'UICustomization': {
        'UserPoolId': 'string',
        'ClientId': 'string',
        'ImageUrl': 'string',
        'CSS': 'string',
        'CSSVersion': 'string',
        'LastModifiedDate': datetime(2015, 1, 1),
        'CreationDate': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --

UICustomization (dict) --
The UI customization information.

UserPoolId (string) --
The user pool ID for the user pool.

ClientId (string) --
The client ID for the client app.

ImageUrl (string) --
The logo image for the UI customization.

CSS (string) --
The CSS values in the UI customization.

CSSVersion (string) --
The CSS version number.

LastModifiedDate (datetime) --
The last-modified date for the UI customization.

CreationDate (datetime) --
The creation date for the UI customization.









Exceptions

CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


    :return: {
        'UICustomization': {
            'UserPoolId': 'string',
            'ClientId': 'string',
            'ImageUrl': 'string',
            'CSS': 'string',
            'CSSVersion': 'string',
            'LastModifiedDate': datetime(2015, 1, 1),
            'CreationDate': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    CognitoIdentityProvider.Client.exceptions.InvalidParameterException
    CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
    CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
    CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
    CognitoIdentityProvider.Client.exceptions.InternalErrorException
    
    """
    pass

def set_user_mfa_preference(SMSMfaSettings=None, SoftwareTokenMfaSettings=None, AccessToken=None):
    """
    Set the user\'s multi-factor authentication (MFA) method preference, including which MFA factors are enabled and if any are preferred. Only one factor can be set as preferred. The preferred MFA factor will be used to authenticate a user if multiple factors are enabled. If multiple options are enabled and no preference is set, a challenge to choose an MFA option will be returned during sign in.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.set_user_mfa_preference(
        SMSMfaSettings={
            'Enabled': True|False,
            'PreferredMfa': True|False
        },
        SoftwareTokenMfaSettings={
            'Enabled': True|False,
            'PreferredMfa': True|False
        },
        AccessToken='string'
    )
    
    
    :type SMSMfaSettings: dict
    :param SMSMfaSettings: The SMS text message multi-factor authentication (MFA) settings.\n\nEnabled (boolean) --Specifies whether SMS text message MFA is enabled.\n\nPreferredMfa (boolean) --Specifies whether SMS is the preferred MFA method.\n\n\n

    :type SoftwareTokenMfaSettings: dict
    :param SoftwareTokenMfaSettings: The time-based one-time password software token MFA settings.\n\nEnabled (boolean) --Specifies whether software token MFA is enabled.\n\nPreferredMfa (boolean) --Specifies whether software token MFA is the preferred MFA method.\n\n\n

    :type AccessToken: string
    :param AccessToken: [REQUIRED]\nThe access token for the user.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.PasswordResetRequiredException
CognitoIdentityProvider.Client.exceptions.UserNotFoundException
CognitoIdentityProvider.Client.exceptions.UserNotConfirmedException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def set_user_pool_mfa_config(UserPoolId=None, SmsMfaConfiguration=None, SoftwareTokenMfaConfiguration=None, MfaConfiguration=None):
    """
    Set the user pool multi-factor authentication (MFA) configuration.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.set_user_pool_mfa_config(
        UserPoolId='string',
        SmsMfaConfiguration={
            'SmsAuthenticationMessage': 'string',
            'SmsConfiguration': {
                'SnsCallerArn': 'string',
                'ExternalId': 'string'
            }
        },
        SoftwareTokenMfaConfiguration={
            'Enabled': True|False
        },
        MfaConfiguration='OFF'|'ON'|'OPTIONAL'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID.\n

    :type SmsMfaConfiguration: dict
    :param SmsMfaConfiguration: The SMS text message MFA configuration.\n\nSmsAuthenticationMessage (string) --The SMS authentication message that will be sent to users with the code they need to sign in. The message must contain the \xe2\x80\x98{####}\xe2\x80\x99 placeholder, which will be replaced with the code. If the message is not included, and default message will be used.\n\nSmsConfiguration (dict) --The SMS configuration.\n\nSnsCallerArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) caller. This is the ARN of the IAM role in your AWS account which Cognito will use to send SMS messages.\n\nExternalId (string) --The external ID is a value that we recommend you use to add security to your IAM role which is used to call Amazon SNS to send SMS messages for your user pool. If you provide an ExternalId , the Cognito User Pool will include it when attempting to assume your IAM role, so that you can set your roles trust policy to require the ExternalID . If you use the Cognito Management Console to create a role for SMS MFA, Cognito will create a role with the required permissions and a trust policy that demonstrates use of the ExternalId .\n\n\n\n\n

    :type SoftwareTokenMfaConfiguration: dict
    :param SoftwareTokenMfaConfiguration: The software token MFA configuration.\n\nEnabled (boolean) --Specifies whether software token MFA is enabled.\n\n\n

    :type MfaConfiguration: string
    :param MfaConfiguration: The MFA configuration. Valid values include:\n\nOFF MFA will not be used for any users.\nON MFA is required for all users to sign in.\nOPTIONAL MFA will be required only for individual users who have an MFA factor enabled.\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'SmsMfaConfiguration': {
        'SmsAuthenticationMessage': 'string',
        'SmsConfiguration': {
            'SnsCallerArn': 'string',
            'ExternalId': 'string'
        }
    },
    'SoftwareTokenMfaConfiguration': {
        'Enabled': True|False
    },
    'MfaConfiguration': 'OFF'|'ON'|'OPTIONAL'
}


Response Structure

(dict) --

SmsMfaConfiguration (dict) --
The SMS text message MFA configuration.

SmsAuthenticationMessage (string) --
The SMS authentication message that will be sent to users with the code they need to sign in. The message must contain the \xe2\x80\x98{####}\xe2\x80\x99 placeholder, which will be replaced with the code. If the message is not included, and default message will be used.

SmsConfiguration (dict) --
The SMS configuration.

SnsCallerArn (string) --
The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) caller. This is the ARN of the IAM role in your AWS account which Cognito will use to send SMS messages.

ExternalId (string) --
The external ID is a value that we recommend you use to add security to your IAM role which is used to call Amazon SNS to send SMS messages for your user pool. If you provide an ExternalId , the Cognito User Pool will include it when attempting to assume your IAM role, so that you can set your roles trust policy to require the ExternalID . If you use the Cognito Management Console to create a role for SMS MFA, Cognito will create a role with the required permissions and a trust policy that demonstrates use of the ExternalId .





SoftwareTokenMfaConfiguration (dict) --
The software token MFA configuration.

Enabled (boolean) --
Specifies whether software token MFA is enabled.



MfaConfiguration (string) --
The MFA configuration. Valid values include:

OFF MFA will not be used for any users.
ON MFA is required for all users to sign in.
OPTIONAL MFA will be required only for individual users who have an MFA factor enabled.








Exceptions

CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.InvalidSmsRoleAccessPolicyException
CognitoIdentityProvider.Client.exceptions.InvalidSmsRoleTrustRelationshipException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


    :return: {
        'SmsMfaConfiguration': {
            'SmsAuthenticationMessage': 'string',
            'SmsConfiguration': {
                'SnsCallerArn': 'string',
                'ExternalId': 'string'
            }
        },
        'SoftwareTokenMfaConfiguration': {
            'Enabled': True|False
        },
        'MfaConfiguration': 'OFF'|'ON'|'OPTIONAL'
    }
    
    
    :returns: 
    OFF MFA will not be used for any users.
    ON MFA is required for all users to sign in.
    OPTIONAL MFA will be required only for individual users who have an MFA factor enabled.
    
    """
    pass

def set_user_settings(AccessToken=None, MFAOptions=None):
    """
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param AccessToken: [REQUIRED]\nThe access token for the set user settings request.\n

    :type MFAOptions: list
    :param MFAOptions: [REQUIRED]\nYou can use this parameter only to set an SMS configuration that uses SMS for delivery.\n\n(dict) --\nThis data type is no longer supported. You can use it only for SMS MFA configurations. You can\'t use it for TOTP software token MFA configurations.\nTo set either type of MFA configuration, use the AdminSetUserMFAPreference or SetUserMFAPreference actions.\nTo look up information about either type of MFA configuration, use the AdminGetUserResponse$UserMFASettingList or GetUserResponse$UserMFASettingList responses.\n\nDeliveryMedium (string) --The delivery medium to send the MFA code. You can use this parameter to set only the SMS delivery medium value.\n\nAttributeName (string) --The attribute name of the MFA option type. The only valid value is phone_number .\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
The response from the server for a set user settings request.





Exceptions

CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.PasswordResetRequiredException
CognitoIdentityProvider.Client.exceptions.UserNotFoundException
CognitoIdentityProvider.Client.exceptions.UserNotConfirmedException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


    :return: {}
    
    
    :returns: 
    CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
    CognitoIdentityProvider.Client.exceptions.InvalidParameterException
    CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
    CognitoIdentityProvider.Client.exceptions.PasswordResetRequiredException
    CognitoIdentityProvider.Client.exceptions.UserNotFoundException
    CognitoIdentityProvider.Client.exceptions.UserNotConfirmedException
    CognitoIdentityProvider.Client.exceptions.InternalErrorException
    
    """
    pass

def sign_up(ClientId=None, SecretHash=None, Username=None, Password=None, UserAttributes=None, ValidationData=None, AnalyticsMetadata=None, UserContextData=None, ClientMetadata=None):
    """
    Registers the user in the specified user pool and creates a user name, password, and user attributes.
    See also: AWS API Documentation
    
    Exceptions
    
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
        ],
        AnalyticsMetadata={
            'AnalyticsEndpointId': 'string'
        },
        UserContextData={
            'EncodedData': 'string'
        },
        ClientMetadata={
            'string': 'string'
        }
    )
    
    
    :type ClientId: string
    :param ClientId: [REQUIRED]\nThe ID of the client associated with the user pool.\n

    :type SecretHash: string
    :param SecretHash: A keyed-hash message authentication code (HMAC) calculated using the secret key of a user pool client and username plus the client ID in the message.

    :type Username: string
    :param Username: [REQUIRED]\nThe user name of the user you wish to register.\n

    :type Password: string
    :param Password: [REQUIRED]\nThe password of the user you wish to register.\n

    :type UserAttributes: list
    :param UserAttributes: An array of name-value pairs representing user attributes.\nFor custom attributes, you must prepend the custom: prefix to the attribute name.\n\n(dict) --Specifies whether the attribute is standard or custom.\n\nName (string) -- [REQUIRED]The name of the attribute.\n\nValue (string) --The value of the attribute.\n\n\n\n\n

    :type ValidationData: list
    :param ValidationData: The validation data in the request to register a user.\n\n(dict) --Specifies whether the attribute is standard or custom.\n\nName (string) -- [REQUIRED]The name of the attribute.\n\nValue (string) --The value of the attribute.\n\n\n\n\n

    :type AnalyticsMetadata: dict
    :param AnalyticsMetadata: The Amazon Pinpoint analytics metadata for collecting metrics for SignUp calls.\n\nAnalyticsEndpointId (string) --The endpoint ID.\n\n\n

    :type UserContextData: dict
    :param UserContextData: Contextual data such as the user\'s device fingerprint, IP address, or location used for evaluating the risk of an unexpected event by Amazon Cognito advanced security.\n\nEncodedData (string) --Contextual data such as the user\'s device fingerprint, IP address, or location used for evaluating the risk of an unexpected event by Amazon Cognito advanced security.\n\n\n

    :type ClientMetadata: dict
    :param ClientMetadata: A map of custom key-value pairs that you can provide as input for any custom workflows that this action triggers.\nYou create custom workflows by assigning AWS Lambda functions to user pool triggers. When you use the SignUp API action, Amazon Cognito invokes any functions that are assigned to the following triggers: pre sign-up , custom message , and post confirmation . When Amazon Cognito invokes any of these functions, it passes a JSON payload, which the function receives as input. This payload contains a clientMetadata attribute, which provides the data that you assigned to the ClientMetadata parameter in your SignUp request. In your function code in AWS Lambda, you can process the clientMetadata value to enhance your workflow for your specific needs.\nFor more information, see Customizing User Pool Workflows with Lambda Triggers in the Amazon Cognito Developer Guide .\n\nNote\nTake the following limitations into consideration when you use the ClientMetadata parameter:\n\nAmazon Cognito does not store the ClientMetadata value. This data is available only to AWS Lambda triggers that are assigned to a user pool to support custom workflows. If your user pool configuration does not include triggers, the ClientMetadata parameter serves no purpose.\nAmazon Cognito does not validate the ClientMetadata value.\nAmazon Cognito does not encrypt the the ClientMetadata value, so don\'t use it to provide sensitive information.\n\n\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'UserConfirmed': True|False,
    'CodeDeliveryDetails': {
        'Destination': 'string',
        'DeliveryMedium': 'SMS'|'EMAIL',
        'AttributeName': 'string'
    },
    'UserSub': 'string'
}


Response Structure

(dict) --
The response from the server for a registration request.

UserConfirmed (boolean) --
A response from the server indicating that a user registration has been confirmed.

CodeDeliveryDetails (dict) --
The code delivery details returned by the server response to the user registration request.

Destination (string) --
The destination for the code delivery details.

DeliveryMedium (string) --
The delivery medium (email message or phone number).

AttributeName (string) --
The attribute name.



UserSub (string) --
The UUID of the authenticated user. This is not the same as username .







Exceptions

CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.UnexpectedLambdaException
CognitoIdentityProvider.Client.exceptions.UserLambdaValidationException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.InvalidPasswordException
CognitoIdentityProvider.Client.exceptions.InvalidLambdaResponseException
CognitoIdentityProvider.Client.exceptions.UsernameExistsException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.InternalErrorException
CognitoIdentityProvider.Client.exceptions.InvalidSmsRoleAccessPolicyException
CognitoIdentityProvider.Client.exceptions.InvalidSmsRoleTrustRelationshipException
CognitoIdentityProvider.Client.exceptions.InvalidEmailRoleAccessPolicyException
CognitoIdentityProvider.Client.exceptions.CodeDeliveryFailureException


    :return: {
        'UserConfirmed': True|False,
        'CodeDeliveryDetails': {
            'Destination': 'string',
            'DeliveryMedium': 'SMS'|'EMAIL',
            'AttributeName': 'string'
        },
        'UserSub': 'string'
    }
    
    
    :returns: 
    CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
    CognitoIdentityProvider.Client.exceptions.InvalidParameterException
    CognitoIdentityProvider.Client.exceptions.UnexpectedLambdaException
    CognitoIdentityProvider.Client.exceptions.UserLambdaValidationException
    CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
    CognitoIdentityProvider.Client.exceptions.InvalidPasswordException
    CognitoIdentityProvider.Client.exceptions.InvalidLambdaResponseException
    CognitoIdentityProvider.Client.exceptions.UsernameExistsException
    CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
    CognitoIdentityProvider.Client.exceptions.InternalErrorException
    CognitoIdentityProvider.Client.exceptions.InvalidSmsRoleAccessPolicyException
    CognitoIdentityProvider.Client.exceptions.InvalidSmsRoleTrustRelationshipException
    CognitoIdentityProvider.Client.exceptions.InvalidEmailRoleAccessPolicyException
    CognitoIdentityProvider.Client.exceptions.CodeDeliveryFailureException
    
    """
    pass

def start_user_import_job(UserPoolId=None, JobId=None):
    """
    Starts the user import.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_user_import_job(
        UserPoolId='string',
        JobId='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID for the user pool that the users are being imported into.\n

    :type JobId: string
    :param JobId: [REQUIRED]\nThe job ID for the user import job.\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --
Represents the response from the server to the request to start the user import job.

UserImportJob (dict) --
The job object that represents the user import job.

JobName (string) --
The job name for the user import job.

JobId (string) --
The job ID for the user import job.

UserPoolId (string) --
The user pool ID for the user pool that the users are being imported into.

PreSignedUrl (string) --
The pre-signed URL to be used to upload the .csv file.

CreationDate (datetime) --
The date the user import job was created.

StartDate (datetime) --
The date when the user import job was started.

CompletionDate (datetime) --
The date when the user import job was completed.

Status (string) --
The status of the user import job. One of the following:

Created - The job was created but not started.
Pending - A transition state. You have started the job, but it has not begun importing users yet.
InProgress - The job has started, and users are being imported.
Stopping - You have stopped the job, but the job has not stopped importing users yet.
Stopped - You have stopped the job, and the job has stopped importing users.
Succeeded - The job has completed successfully.
Failed - The job has stopped due to an error.
Expired - You created a job, but did not start the job within 24-48 hours. All data associated with the job was deleted, and the job cannot be started.


CloudWatchLogsRoleArn (string) --
The role ARN for the Amazon CloudWatch Logging role for the user import job. For more information, see "Creating the CloudWatch Logs IAM Role" in the Amazon Cognito Developer Guide.

ImportedUsers (integer) --
The number of users that were successfully imported.

SkippedUsers (integer) --
The number of users that were skipped.

FailedUsers (integer) --
The number of users that could not be imported.

CompletionMessage (string) --
The message returned when the user import job is completed.









Exceptions

CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.InternalErrorException
CognitoIdentityProvider.Client.exceptions.PreconditionNotMetException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException


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
    
    Exceptions
    
    :example: response = client.stop_user_import_job(
        UserPoolId='string',
        JobId='string'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID for the user pool that the users are being imported into.\n

    :type JobId: string
    :param JobId: [REQUIRED]\nThe job ID for the user import job.\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --
Represents the response from the server to the request to stop the user import job.

UserImportJob (dict) --
The job object that represents the user import job.

JobName (string) --
The job name for the user import job.

JobId (string) --
The job ID for the user import job.

UserPoolId (string) --
The user pool ID for the user pool that the users are being imported into.

PreSignedUrl (string) --
The pre-signed URL to be used to upload the .csv file.

CreationDate (datetime) --
The date the user import job was created.

StartDate (datetime) --
The date when the user import job was started.

CompletionDate (datetime) --
The date when the user import job was completed.

Status (string) --
The status of the user import job. One of the following:

Created - The job was created but not started.
Pending - A transition state. You have started the job, but it has not begun importing users yet.
InProgress - The job has started, and users are being imported.
Stopping - You have stopped the job, but the job has not stopped importing users yet.
Stopped - You have stopped the job, and the job has stopped importing users.
Succeeded - The job has completed successfully.
Failed - The job has stopped due to an error.
Expired - You created a job, but did not start the job within 24-48 hours. All data associated with the job was deleted, and the job cannot be started.


CloudWatchLogsRoleArn (string) --
The role ARN for the Amazon CloudWatch Logging role for the user import job. For more information, see "Creating the CloudWatch Logs IAM Role" in the Amazon Cognito Developer Guide.

ImportedUsers (integer) --
The number of users that were successfully imported.

SkippedUsers (integer) --
The number of users that were skipped.

FailedUsers (integer) --
The number of users that could not be imported.

CompletionMessage (string) --
The message returned when the user import job is completed.









Exceptions

CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.InternalErrorException
CognitoIdentityProvider.Client.exceptions.PreconditionNotMetException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException


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

def tag_resource(ResourceArn=None, Tags=None):
    """
    Assigns a set of tags to an Amazon Cognito user pool. A tag is a label that you can use to categorize and manage user pools in different ways, such as by purpose, owner, environment, or other criteria.
    Each tag consists of a key and value, both of which you define. A key is a general category for more specific values. For example, if you have two versions of a user pool, one for testing and another for production, you might assign an Environment tag key to both user pools. The value of this key might be Test for one user pool and Production for the other.
    Tags are useful for cost tracking and access control. You can activate your tags so that they appear on the Billing and Cost Management console, where you can track the costs associated with your user pools. In an IAM policy, you can constrain permissions for user pools based on specific tags or tag values.
    You can use this action up to 5 times per second, per account. A user pool can have as many as 50 tags.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        ResourceArn='string',
        Tags={
            'string': 'string'
        }
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the user pool to assign the tags to.\n

    :type Tags: dict
    :param Tags: [REQUIRED]\nThe tags to assign to the user pool.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_resource(ResourceArn=None, TagKeys=None):
    """
    Removes the specified tags from an Amazon Cognito user pool. You can use this action up to 5 times per second, per account
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        ResourceArn='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the user pool that the tags are assigned to.\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nThe keys of the tags to remove from the user pool.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_auth_event_feedback(UserPoolId=None, Username=None, EventId=None, FeedbackToken=None, FeedbackValue=None):
    """
    Provides the feedback for an authentication event whether it was from a valid user or not. This feedback is used for improving the risk evaluation decision for the user pool as part of Amazon Cognito advanced security.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_auth_event_feedback(
        UserPoolId='string',
        Username='string',
        EventId='string',
        FeedbackToken='string',
        FeedbackValue='Valid'|'Invalid'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID.\n

    :type Username: string
    :param Username: [REQUIRED]\nThe user pool username.\n

    :type EventId: string
    :param EventId: [REQUIRED]\nThe event ID.\n

    :type FeedbackToken: string
    :param FeedbackToken: [REQUIRED]\nThe feedback token.\n

    :type FeedbackValue: string
    :param FeedbackValue: [REQUIRED]\nThe authentication event feedback value.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.UserNotFoundException
CognitoIdentityProvider.Client.exceptions.UserPoolAddOnNotEnabledException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_device_status(AccessToken=None, DeviceKey=None, DeviceRememberedStatus=None):
    """
    Updates the device status.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_device_status(
        AccessToken='string',
        DeviceKey='string',
        DeviceRememberedStatus='remembered'|'not_remembered'
    )
    
    
    :type AccessToken: string
    :param AccessToken: [REQUIRED]\nThe access token.\n

    :type DeviceKey: string
    :param DeviceKey: [REQUIRED]\nThe device key.\n

    :type DeviceRememberedStatus: string
    :param DeviceRememberedStatus: The status of whether a device is remembered.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
The response to the request to update the device status.





Exceptions

CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.InvalidUserPoolConfigurationException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.PasswordResetRequiredException
CognitoIdentityProvider.Client.exceptions.UserNotFoundException
CognitoIdentityProvider.Client.exceptions.UserNotConfirmedException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


    :return: {}
    
    
    :returns: 
    CognitoIdentityProvider.Client.exceptions.InvalidParameterException
    CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
    CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
    CognitoIdentityProvider.Client.exceptions.InvalidUserPoolConfigurationException
    CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
    CognitoIdentityProvider.Client.exceptions.PasswordResetRequiredException
    CognitoIdentityProvider.Client.exceptions.UserNotFoundException
    CognitoIdentityProvider.Client.exceptions.UserNotConfirmedException
    CognitoIdentityProvider.Client.exceptions.InternalErrorException
    
    """
    pass

def update_group(GroupName=None, UserPoolId=None, Description=None, RoleArn=None, Precedence=None):
    """
    Updates the specified group with the specified attributes.
    Calling this action requires developer credentials.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_group(
        GroupName='string',
        UserPoolId='string',
        Description='string',
        RoleArn='string',
        Precedence=123
    )
    
    
    :type GroupName: string
    :param GroupName: [REQUIRED]\nThe name of the group.\n

    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID for the user pool.\n

    :type Description: string
    :param Description: A string containing the new description of the group.

    :type RoleArn: string
    :param RoleArn: The new role ARN for the group. This is used for setting the cognito:roles and cognito:preferred_role claims in the token.

    :type Precedence: integer
    :param Precedence: The new precedence value for the group. For more information about this parameter, see .

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

Group (dict) --
The group object for the group.

GroupName (string) --
The name of the group.

UserPoolId (string) --
The user pool ID for the user pool.

Description (string) --
A string containing the description of the group.

RoleArn (string) --
The role ARN for the group.

Precedence (integer) --
A nonnegative integer value that specifies the precedence of this group relative to the other groups that a user can belong to in the user pool. If a user belongs to two or more groups, it is the group with the highest precedence whose role ARN will be used in the cognito:roles and cognito:preferred_role claims in the user\'s tokens. Groups with higher Precedence values take precedence over groups with lower Precedence values or with null Precedence values.
Two groups can have the same Precedence value. If this happens, neither group takes precedence over the other. If two groups with the same Precedence have the same role ARN, that role is used in the cognito:preferred_role claim in tokens for users in each group. If the two groups have different role ARNs, the cognito:preferred_role claim is not set in users\' tokens.
The default Precedence value is null.

LastModifiedDate (datetime) --
The date the group was last modified.

CreationDate (datetime) --
The date the group was created.









Exceptions

CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


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
    
    
    :returns: 
    CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
    CognitoIdentityProvider.Client.exceptions.InvalidParameterException
    CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
    CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
    CognitoIdentityProvider.Client.exceptions.InternalErrorException
    
    """
    pass

def update_identity_provider(UserPoolId=None, ProviderName=None, ProviderDetails=None, AttributeMapping=None, IdpIdentifiers=None):
    """
    Updates identity provider information for a user pool.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param UserPoolId: [REQUIRED]\nThe user pool ID.\n

    :type ProviderName: string
    :param ProviderName: [REQUIRED]\nThe identity provider name.\n

    :type ProviderDetails: dict
    :param ProviderDetails: The identity provider details to be updated, such as MetadataURL and MetadataFile .\n\n(string) --\n(string) --\n\n\n\n

    :type AttributeMapping: dict
    :param AttributeMapping: The identity provider attribute mapping to be changed.\n\n(string) --\n(string) --\n\n\n\n

    :type IdpIdentifiers: list
    :param IdpIdentifiers: A list of identity provider identifiers.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'IdentityProvider': {
        'UserPoolId': 'string',
        'ProviderName': 'string',
        'ProviderType': 'SAML'|'Facebook'|'Google'|'LoginWithAmazon'|'SignInWithApple'|'OIDC',
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


Response Structure

(dict) --

IdentityProvider (dict) --
The identity provider object.

UserPoolId (string) --
The user pool ID.

ProviderName (string) --
The identity provider name.

ProviderType (string) --
The identity provider type.

ProviderDetails (dict) --
The identity provider details. The following list describes the provider detail keys for each identity provider type.

For Google, Facebook and Login with Amazon:
client_id
client_secret
authorize_scopes


For Sign in with Apple:
client_id
team_id
key_id
private_key
authorize_scopes


For OIDC providers:
client_id
client_secret
attributes_request_method
oidc_issuer
authorize_scopes
authorize_url if not available from discovery URL specified by oidc_issuer key
token_url if not available from discovery URL specified by oidc_issuer key
attributes_url if not available from discovery URL specified by oidc_issuer key
jwks_uri if not available from discovery URL specified by oidc_issuer key
authorize_scopes


For SAML providers:
MetadataFile OR MetadataURL
IDPSignOut optional




(string) --
(string) --




AttributeMapping (dict) --
A mapping of identity provider attributes to standard and custom user pool attributes.

(string) --
(string) --




IdpIdentifiers (list) --
A list of identity provider identifiers.

(string) --


LastModifiedDate (datetime) --
The date the identity provider was last modified.

CreationDate (datetime) --
The date the identity provider was created.









Exceptions

CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.UnsupportedIdentityProviderException
CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


    :return: {
        'IdentityProvider': {
            'UserPoolId': 'string',
            'ProviderName': 'string',
            'ProviderType': 'SAML'|'Facebook'|'Google'|'LoginWithAmazon'|'SignInWithApple'|'OIDC',
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
    For Google, Facebook and Login with Amazon:
    client_id
    client_secret
    authorize_scopes
    
    
    For Sign in with Apple:
    client_id
    team_id
    key_id
    private_key
    authorize_scopes
    
    
    For OIDC providers:
    client_id
    client_secret
    attributes_request_method
    oidc_issuer
    authorize_scopes
    authorize_url if not available from discovery URL specified by oidc_issuer key
    token_url if not available from discovery URL specified by oidc_issuer key
    attributes_url if not available from discovery URL specified by oidc_issuer key
    jwks_uri if not available from discovery URL specified by oidc_issuer key
    authorize_scopes
    
    
    For SAML providers:
    MetadataFile OR MetadataURL
    IDPSignOut optional
    
    
    
    """
    pass

def update_resource_server(UserPoolId=None, Identifier=None, Name=None, Scopes=None):
    """
    Updates the name and scopes of resource server. All other fields are read-only.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_resource_server(
        UserPoolId='string',
        Identifier='string',
        Name='string',
        Scopes=[
            {
                'ScopeName': 'string',
                'ScopeDescription': 'string'
            },
        ]
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID for the user pool.\n

    :type Identifier: string
    :param Identifier: [REQUIRED]\nThe identifier for the resource server.\n

    :type Name: string
    :param Name: [REQUIRED]\nThe name of the resource server.\n

    :type Scopes: list
    :param Scopes: The scope values to be set for the resource server.\n\n(dict) --A resource server scope.\n\nScopeName (string) -- [REQUIRED]The name of the scope.\n\nScopeDescription (string) -- [REQUIRED]A description of the scope.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ResourceServer': {
        'UserPoolId': 'string',
        'Identifier': 'string',
        'Name': 'string',
        'Scopes': [
            {
                'ScopeName': 'string',
                'ScopeDescription': 'string'
            },
        ]
    }
}


Response Structure

(dict) --

ResourceServer (dict) --
The resource server.

UserPoolId (string) --
The user pool ID for the user pool that hosts the resource server.

Identifier (string) --
The identifier for the resource server.

Name (string) --
The name of the resource server.

Scopes (list) --
A list of scopes that are defined for the resource server.

(dict) --
A resource server scope.

ScopeName (string) --
The name of the scope.

ScopeDescription (string) --
A description of the scope.













Exceptions

CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


    :return: {
        'ResourceServer': {
            'UserPoolId': 'string',
            'Identifier': 'string',
            'Name': 'string',
            'Scopes': [
                {
                    'ScopeName': 'string',
                    'ScopeDescription': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    CognitoIdentityProvider.Client.exceptions.InvalidParameterException
    CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
    CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
    CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
    CognitoIdentityProvider.Client.exceptions.InternalErrorException
    
    """
    pass

def update_user_attributes(UserAttributes=None, AccessToken=None, ClientMetadata=None):
    """
    Allows a user to update a specific attribute (one at a time).
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_user_attributes(
        UserAttributes=[
            {
                'Name': 'string',
                'Value': 'string'
            },
        ],
        AccessToken='string',
        ClientMetadata={
            'string': 'string'
        }
    )
    
    
    :type UserAttributes: list
    :param UserAttributes: [REQUIRED]\nAn array of name-value pairs representing user attributes.\nFor custom attributes, you must prepend the custom: prefix to the attribute name.\n\n(dict) --Specifies whether the attribute is standard or custom.\n\nName (string) -- [REQUIRED]The name of the attribute.\n\nValue (string) --The value of the attribute.\n\n\n\n\n

    :type AccessToken: string
    :param AccessToken: [REQUIRED]\nThe access token for the request to update user attributes.\n

    :type ClientMetadata: dict
    :param ClientMetadata: A map of custom key-value pairs that you can provide as input for any custom workflows that this action triggers.\nYou create custom workflows by assigning AWS Lambda functions to user pool triggers. When you use the UpdateUserAttributes API action, Amazon Cognito invokes the function that is assigned to the custom message trigger. When Amazon Cognito invokes this function, it passes a JSON payload, which the function receives as input. This payload contains a clientMetadata attribute, which provides the data that you assigned to the ClientMetadata parameter in your UpdateUserAttributes request. In your function code in AWS Lambda, you can process the clientMetadata value to enhance your workflow for your specific needs.\nFor more information, see Customizing User Pool Workflows with Lambda Triggers in the Amazon Cognito Developer Guide .\n\nNote\nTake the following limitations into consideration when you use the ClientMetadata parameter:\n\nAmazon Cognito does not store the ClientMetadata value. This data is available only to AWS Lambda triggers that are assigned to a user pool to support custom workflows. If your user pool configuration does not include triggers, the ClientMetadata parameter serves no purpose.\nAmazon Cognito does not validate the ClientMetadata value.\nAmazon Cognito does not encrypt the the ClientMetadata value, so don\'t use it to provide sensitive information.\n\n\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'CodeDeliveryDetailsList': [
        {
            'Destination': 'string',
            'DeliveryMedium': 'SMS'|'EMAIL',
            'AttributeName': 'string'
        },
    ]
}


Response Structure

(dict) --
Represents the response from the server for the request to update user attributes.

CodeDeliveryDetailsList (list) --
The code delivery details list from the server for the request to update user attributes.

(dict) --
The code delivery details being returned from the server.

Destination (string) --
The destination for the code delivery details.

DeliveryMedium (string) --
The delivery medium (email message or phone number).

AttributeName (string) --
The attribute name.











Exceptions

CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.CodeMismatchException
CognitoIdentityProvider.Client.exceptions.ExpiredCodeException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.UnexpectedLambdaException
CognitoIdentityProvider.Client.exceptions.UserLambdaValidationException
CognitoIdentityProvider.Client.exceptions.InvalidLambdaResponseException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.AliasExistsException
CognitoIdentityProvider.Client.exceptions.InvalidSmsRoleAccessPolicyException
CognitoIdentityProvider.Client.exceptions.InvalidSmsRoleTrustRelationshipException
CognitoIdentityProvider.Client.exceptions.InvalidEmailRoleAccessPolicyException
CognitoIdentityProvider.Client.exceptions.CodeDeliveryFailureException
CognitoIdentityProvider.Client.exceptions.PasswordResetRequiredException
CognitoIdentityProvider.Client.exceptions.UserNotFoundException
CognitoIdentityProvider.Client.exceptions.UserNotConfirmedException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


    :return: {
        'CodeDeliveryDetailsList': [
            {
                'Destination': 'string',
                'DeliveryMedium': 'SMS'|'EMAIL',
                'AttributeName': 'string'
            },
        ]
    }
    
    
    :returns: 
    CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
    CognitoIdentityProvider.Client.exceptions.InvalidParameterException
    CognitoIdentityProvider.Client.exceptions.CodeMismatchException
    CognitoIdentityProvider.Client.exceptions.ExpiredCodeException
    CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
    CognitoIdentityProvider.Client.exceptions.UnexpectedLambdaException
    CognitoIdentityProvider.Client.exceptions.UserLambdaValidationException
    CognitoIdentityProvider.Client.exceptions.InvalidLambdaResponseException
    CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
    CognitoIdentityProvider.Client.exceptions.AliasExistsException
    CognitoIdentityProvider.Client.exceptions.InvalidSmsRoleAccessPolicyException
    CognitoIdentityProvider.Client.exceptions.InvalidSmsRoleTrustRelationshipException
    CognitoIdentityProvider.Client.exceptions.InvalidEmailRoleAccessPolicyException
    CognitoIdentityProvider.Client.exceptions.CodeDeliveryFailureException
    CognitoIdentityProvider.Client.exceptions.PasswordResetRequiredException
    CognitoIdentityProvider.Client.exceptions.UserNotFoundException
    CognitoIdentityProvider.Client.exceptions.UserNotConfirmedException
    CognitoIdentityProvider.Client.exceptions.InternalErrorException
    
    """
    pass

def update_user_pool(UserPoolId=None, Policies=None, LambdaConfig=None, AutoVerifiedAttributes=None, SmsVerificationMessage=None, EmailVerificationMessage=None, EmailVerificationSubject=None, VerificationMessageTemplate=None, SmsAuthenticationMessage=None, MfaConfiguration=None, DeviceConfiguration=None, EmailConfiguration=None, SmsConfiguration=None, UserPoolTags=None, AdminCreateUserConfig=None, UserPoolAddOns=None, AccountRecoverySetting=None):
    """
    Updates the specified user pool with the specified attributes. You can get a list of the current user pool settings with .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_user_pool(
        UserPoolId='string',
        Policies={
            'PasswordPolicy': {
                'MinimumLength': 123,
                'RequireUppercase': True|False,
                'RequireLowercase': True|False,
                'RequireNumbers': True|False,
                'RequireSymbols': True|False,
                'TemporaryPasswordValidityDays': 123
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
            'VerifyAuthChallengeResponse': 'string',
            'PreTokenGeneration': 'string',
            'UserMigration': 'string'
        },
        AutoVerifiedAttributes=[
            'phone_number'|'email',
        ],
        SmsVerificationMessage='string',
        EmailVerificationMessage='string',
        EmailVerificationSubject='string',
        VerificationMessageTemplate={
            'SmsMessage': 'string',
            'EmailMessage': 'string',
            'EmailSubject': 'string',
            'EmailMessageByLink': 'string',
            'EmailSubjectByLink': 'string',
            'DefaultEmailOption': 'CONFIRM_WITH_LINK'|'CONFIRM_WITH_CODE'
        },
        SmsAuthenticationMessage='string',
        MfaConfiguration='OFF'|'ON'|'OPTIONAL',
        DeviceConfiguration={
            'ChallengeRequiredOnNewDevice': True|False,
            'DeviceOnlyRememberedOnUserPrompt': True|False
        },
        EmailConfiguration={
            'SourceArn': 'string',
            'ReplyToEmailAddress': 'string',
            'EmailSendingAccount': 'COGNITO_DEFAULT'|'DEVELOPER',
            'From': 'string',
            'ConfigurationSet': 'string'
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
        UserPoolAddOns={
            'AdvancedSecurityMode': 'OFF'|'AUDIT'|'ENFORCED'
        },
        AccountRecoverySetting={
            'RecoveryMechanisms': [
                {
                    'Priority': 123,
                    'Name': 'verified_email'|'verified_phone_number'|'admin_only'
                },
            ]
        }
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID for the user pool you want to update.\n

    :type Policies: dict
    :param Policies: A container with the policies you wish to update in a user pool.\n\nPasswordPolicy (dict) --The password policy.\n\nMinimumLength (integer) --The minimum length of the password policy that you have set. Cannot be less than 6.\n\nRequireUppercase (boolean) --In the password policy that you have set, refers to whether you have required users to use at least one uppercase letter in their password.\n\nRequireLowercase (boolean) --In the password policy that you have set, refers to whether you have required users to use at least one lowercase letter in their password.\n\nRequireNumbers (boolean) --In the password policy that you have set, refers to whether you have required users to use at least one number in their password.\n\nRequireSymbols (boolean) --In the password policy that you have set, refers to whether you have required users to use at least one symbol in their password.\n\nTemporaryPasswordValidityDays (integer) --In the password policy you have set, refers to the number of days a temporary password is valid. If the user does not sign-in during this time, their password will need to be reset by an administrator.\n\nNote\nWhen you set TemporaryPasswordValidityDays for a user pool, you will no longer be able to set the deprecated UnusedAccountValidityDays value for that user pool.\n\n\n\n\n\n

    :type LambdaConfig: dict
    :param LambdaConfig: The AWS Lambda configuration information from the request to update the user pool.\n\nPreSignUp (string) --A pre-registration AWS Lambda trigger.\n\nCustomMessage (string) --A custom Message AWS Lambda trigger.\n\nPostConfirmation (string) --A post-confirmation AWS Lambda trigger.\n\nPreAuthentication (string) --A pre-authentication AWS Lambda trigger.\n\nPostAuthentication (string) --A post-authentication AWS Lambda trigger.\n\nDefineAuthChallenge (string) --Defines the authentication challenge.\n\nCreateAuthChallenge (string) --Creates an authentication challenge.\n\nVerifyAuthChallengeResponse (string) --Verifies the authentication challenge response.\n\nPreTokenGeneration (string) --A Lambda trigger that is invoked before token generation.\n\nUserMigration (string) --The user migration Lambda config type.\n\n\n

    :type AutoVerifiedAttributes: list
    :param AutoVerifiedAttributes: The attributes that are automatically verified when the Amazon Cognito service makes a request to update user pools.\n\n(string) --\n\n

    :type SmsVerificationMessage: string
    :param SmsVerificationMessage: A container with information about the SMS verification message.

    :type EmailVerificationMessage: string
    :param EmailVerificationMessage: The contents of the email verification message.

    :type EmailVerificationSubject: string
    :param EmailVerificationSubject: The subject of the email verification message.

    :type VerificationMessageTemplate: dict
    :param VerificationMessageTemplate: The template for verification messages.\n\nSmsMessage (string) --The SMS message template.\n\nEmailMessage (string) --The email message template.\n\nEmailSubject (string) --The subject line for the email message template.\n\nEmailMessageByLink (string) --The email message template for sending a confirmation link to the user.\n\nEmailSubjectByLink (string) --The subject line for the email message template for sending a confirmation link to the user.\n\nDefaultEmailOption (string) --The default email option.\n\n\n

    :type SmsAuthenticationMessage: string
    :param SmsAuthenticationMessage: The contents of the SMS authentication message.

    :type MfaConfiguration: string
    :param MfaConfiguration: Can be one of the following values:\n\nOFF - MFA tokens are not required and cannot be specified during user registration.\nON - MFA tokens are required for all user registrations. You can only specify required when you are initially creating a user pool.\nOPTIONAL - Users have the option when registering to create an MFA token.\n\n

    :type DeviceConfiguration: dict
    :param DeviceConfiguration: Device configuration.\n\nChallengeRequiredOnNewDevice (boolean) --Indicates whether a challenge is required on a new device. Only applicable to a new device.\n\nDeviceOnlyRememberedOnUserPrompt (boolean) --If true, a device is only remembered on user prompt.\n\n\n

    :type EmailConfiguration: dict
    :param EmailConfiguration: Email configuration.\n\nSourceArn (string) --The Amazon Resource Name (ARN) of a verified email address in Amazon SES. This email address is used in one of the following ways, depending on the value that you specify for the EmailSendingAccount parameter:\n\nIf you specify COGNITO_DEFAULT , Amazon Cognito uses this address as the custom FROM address when it emails your users by using its built-in email account.\nIf you specify DEVELOPER , Amazon Cognito emails your users with this address by calling Amazon SES on your behalf.\n\n\nReplyToEmailAddress (string) --The destination to which the receiver of the email should reply to.\n\nEmailSendingAccount (string) --Specifies whether Amazon Cognito emails your users by using its built-in email functionality or your Amazon SES email configuration. Specify one of the following values:\n\nCOGNITO_DEFAULT\nWhen Amazon Cognito emails your users, it uses its built-in email functionality. When you use the default option, Amazon Cognito allows only a limited number of emails each day for your user pool. For typical production environments, the default email limit is below the required delivery volume. To achieve a higher delivery volume, specify DEVELOPER to use your Amazon SES email configuration.\nTo look up the email delivery limit for the default option, see Limits in Amazon Cognito in the Amazon Cognito Developer Guide .\nThe default FROM address is no-reply@verificationemail.com. To customize the FROM address, provide the ARN of an Amazon SES verified email address for the SourceArn parameter.\n\nDEVELOPER\nWhen Amazon Cognito emails your users, it uses your Amazon SES configuration. Amazon Cognito calls Amazon SES on your behalf to send email from your verified email address. When you use this option, the email delivery limits are the same limits that apply to your Amazon SES verified email address in your AWS account.\nIf you use this option, you must provide the ARN of an Amazon SES verified email address for the SourceArn parameter.\nBefore Amazon Cognito can email your users, it requires additional permissions to call Amazon SES on your behalf. When you update your user pool with this option, Amazon Cognito creates a service-linked role , which is a type of IAM role, in your AWS account. This role contains the permissions that allow Amazon Cognito to access Amazon SES and send email messages with your address. For more information about the service-linked role that Amazon Cognito creates, see Using Service-Linked Roles for Amazon Cognito in the Amazon Cognito Developer Guide .\n\nFrom (string) --Identifies either the sender\xe2\x80\x99s email address or the sender\xe2\x80\x99s name with their email address. For example, testuser@example.com or Test User <testuser@example.com> . This address will appear before the body of the email.\n\nConfigurationSet (string) --The set of configuration rules that can be applied to emails sent using Amazon SES. A configuration set is applied to an email by including a reference to the configuration set in the headers of the email. Once applied, all of the rules in that configuration set are applied to the email. Configuration sets can be used to apply the following types of rules to emails:\n\nEvent publishing \xe2\x80\x93 Amazon SES can track the number of send, delivery, open, click, bounce, and complaint events for each email sent. Use event publishing to send information about these events to other AWS services such as SNS and CloudWatch.\nIP pool management \xe2\x80\x93 When leasing dedicated IP addresses with Amazon SES, you can create groups of IP addresses, called dedicated IP pools. You can then associate the dedicated IP pools with configuration sets.\n\n\n\n

    :type SmsConfiguration: dict
    :param SmsConfiguration: SMS configuration.\n\nSnsCallerArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) caller. This is the ARN of the IAM role in your AWS account which Cognito will use to send SMS messages.\n\nExternalId (string) --The external ID is a value that we recommend you use to add security to your IAM role which is used to call Amazon SNS to send SMS messages for your user pool. If you provide an ExternalId , the Cognito User Pool will include it when attempting to assume your IAM role, so that you can set your roles trust policy to require the ExternalID . If you use the Cognito Management Console to create a role for SMS MFA, Cognito will create a role with the required permissions and a trust policy that demonstrates use of the ExternalId .\n\n\n

    :type UserPoolTags: dict
    :param UserPoolTags: The tag keys and values to assign to the user pool. A tag is a label that you can use to categorize and manage user pools in different ways, such as by purpose, owner, environment, or other criteria.\n\n(string) --\n(string) --\n\n\n\n

    :type AdminCreateUserConfig: dict
    :param AdminCreateUserConfig: The configuration for AdminCreateUser requests.\n\nAllowAdminCreateUserOnly (boolean) --Set to True if only the administrator is allowed to create user profiles. Set to False if users can sign themselves up via an app.\n\nUnusedAccountValidityDays (integer) --The user account expiration limit, in days, after which the account is no longer usable. To reset the account after that time limit, you must call AdminCreateUser again, specifying 'RESEND' for the MessageAction parameter. The default value for this parameter is 7.\n\nNote\nIf you set a value for TemporaryPasswordValidityDays in PasswordPolicy , that value will be used and UnusedAccountValidityDays will be deprecated for that user pool.\n\n\nInviteMessageTemplate (dict) --The message template to be used for the welcome message to new users.\nSee also Customizing User Invitation Messages .\n\nSMSMessage (string) --The message template for SMS messages.\n\nEmailMessage (string) --The message template for email messages.\n\nEmailSubject (string) --The subject line for email messages.\n\n\n\n\n

    :type UserPoolAddOns: dict
    :param UserPoolAddOns: Used to enable advanced security risk detection. Set the key AdvancedSecurityMode to the value 'AUDIT'.\n\nAdvancedSecurityMode (string) -- [REQUIRED]The advanced security mode.\n\n\n

    :type AccountRecoverySetting: dict
    :param AccountRecoverySetting: Use this setting to define which verified available method a user can use to recover their password when they call ForgotPassword . It allows you to define a preferred method when a user has more than one method available. With this setting, SMS does not qualify for a valid password recovery mechanism if the user also has SMS MFA enabled. In the absence of this setting, Cognito uses the legacy behavior to determine the recovery method where SMS is preferred over email.\n\nRecoveryMechanisms (list) --The list of RecoveryOptionTypes .\n\n(dict) --A map containing a priority as a key, and recovery method name as a value.\n\nPriority (integer) -- [REQUIRED]A positive integer specifying priority of a method with 1 being the highest priority.\n\nName (string) -- [REQUIRED]Specifies the recovery method for a user.\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
Represents the response from the server when you make a request to update the user pool.





Exceptions

CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.ConcurrentModificationException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.UserImportInProgressException
CognitoIdentityProvider.Client.exceptions.InternalErrorException
CognitoIdentityProvider.Client.exceptions.InvalidSmsRoleAccessPolicyException
CognitoIdentityProvider.Client.exceptions.InvalidSmsRoleTrustRelationshipException
CognitoIdentityProvider.Client.exceptions.UserPoolTaggingException
CognitoIdentityProvider.Client.exceptions.InvalidEmailRoleAccessPolicyException


    :return: {}
    
    
    :returns: 
    CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
    CognitoIdentityProvider.Client.exceptions.InvalidParameterException
    CognitoIdentityProvider.Client.exceptions.ConcurrentModificationException
    CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
    CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
    CognitoIdentityProvider.Client.exceptions.UserImportInProgressException
    CognitoIdentityProvider.Client.exceptions.InternalErrorException
    CognitoIdentityProvider.Client.exceptions.InvalidSmsRoleAccessPolicyException
    CognitoIdentityProvider.Client.exceptions.InvalidSmsRoleTrustRelationshipException
    CognitoIdentityProvider.Client.exceptions.UserPoolTaggingException
    CognitoIdentityProvider.Client.exceptions.InvalidEmailRoleAccessPolicyException
    
    """
    pass

def update_user_pool_client(UserPoolId=None, ClientId=None, ClientName=None, RefreshTokenValidity=None, ReadAttributes=None, WriteAttributes=None, ExplicitAuthFlows=None, SupportedIdentityProviders=None, CallbackURLs=None, LogoutURLs=None, DefaultRedirectURI=None, AllowedOAuthFlows=None, AllowedOAuthScopes=None, AllowedOAuthFlowsUserPoolClient=None, AnalyticsConfiguration=None, PreventUserExistenceErrors=None):
    """
    Updates the specified user pool app client with the specified attributes. You can get a list of the current user pool app client settings with .
    See also: AWS API Documentation
    
    Exceptions
    
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
            'ADMIN_NO_SRP_AUTH'|'CUSTOM_AUTH_FLOW_ONLY'|'USER_PASSWORD_AUTH'|'ALLOW_ADMIN_USER_PASSWORD_AUTH'|'ALLOW_CUSTOM_AUTH'|'ALLOW_USER_PASSWORD_AUTH'|'ALLOW_USER_SRP_AUTH'|'ALLOW_REFRESH_TOKEN_AUTH',
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
        AllowedOAuthFlowsUserPoolClient=True|False,
        AnalyticsConfiguration={
            'ApplicationId': 'string',
            'RoleArn': 'string',
            'ExternalId': 'string',
            'UserDataShared': True|False
        },
        PreventUserExistenceErrors='LEGACY'|'ENABLED'
    )
    
    
    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe user pool ID for the user pool where you want to update the user pool client.\n

    :type ClientId: string
    :param ClientId: [REQUIRED]\nThe ID of the client associated with the user pool.\n

    :type ClientName: string
    :param ClientName: The client name from the update user pool client request.

    :type RefreshTokenValidity: integer
    :param RefreshTokenValidity: The time limit, in days, after which the refresh token is no longer valid and cannot be used.

    :type ReadAttributes: list
    :param ReadAttributes: The read-only attributes of the user pool.\n\n(string) --\n\n

    :type WriteAttributes: list
    :param WriteAttributes: The writeable attributes of the user pool.\n\n(string) --\n\n

    :type ExplicitAuthFlows: list
    :param ExplicitAuthFlows: The authentication flows that are supported by the user pool clients. Flow names without the ALLOW_ prefix are deprecated in favor of new names with the ALLOW_ prefix. Note that values with ALLOW_ prefix cannot be used along with values without ALLOW_ prefix.\nValid values include:\n\nALLOW_ADMIN_USER_PASSWORD_AUTH : Enable admin based user password authentication flow ADMIN_USER_PASSWORD_AUTH . This setting replaces the ADMIN_NO_SRP_AUTH setting. With this authentication flow, Cognito receives the password in the request instead of using the SRP (Secure Remote Password protocol) protocol to verify passwords.\nALLOW_CUSTOM_AUTH : Enable Lambda trigger based authentication.\nALLOW_USER_PASSWORD_AUTH : Enable user password-based authentication. In this flow, Cognito receives the password in the request instead of using the SRP protocol to verify passwords.\nALLOW_USER_SRP_AUTH : Enable SRP based authentication.\nALLOW_REFRESH_TOKEN_AUTH : Enable authflow to refresh tokens.\n\n\n(string) --\n\n

    :type SupportedIdentityProviders: list
    :param SupportedIdentityProviders: A list of provider names for the identity providers that are supported on this client.\n\n(string) --\n\n

    :type CallbackURLs: list
    :param CallbackURLs: A list of allowed redirect (callback) URLs for the identity providers.\nA redirect URI must:\n\nBe an absolute URI.\nBe registered with the authorization server.\nNot include a fragment component.\n\nSee OAuth 2.0 - Redirection Endpoint .\nAmazon Cognito requires HTTPS over HTTP except for http://localhost for testing purposes only.\nApp callback URLs such as myapp://example are also supported.\n\n(string) --\n\n

    :type LogoutURLs: list
    :param LogoutURLs: A list of allowed logout URLs for the identity providers.\n\n(string) --\n\n

    :type DefaultRedirectURI: string
    :param DefaultRedirectURI: The default redirect URI. Must be in the CallbackURLs list.\nA redirect URI must:\n\nBe an absolute URI.\nBe registered with the authorization server.\nNot include a fragment component.\n\nSee OAuth 2.0 - Redirection Endpoint .\nAmazon Cognito requires HTTPS over HTTP except for http://localhost for testing purposes only.\nApp callback URLs such as myapp://example are also supported.\n

    :type AllowedOAuthFlows: list
    :param AllowedOAuthFlows: The allowed OAuth flows.\nSet to code to initiate a code grant flow, which provides an authorization code as the response. This code can be exchanged for access tokens with the token endpoint.\nSet to implicit to specify that the client should get the access token (and, optionally, ID token, based on scopes) directly.\nSet to client_credentials to specify that the client should get the access token (and, optionally, ID token, based on scopes) from the token endpoint using a combination of client and client_secret.\n\n(string) --\n\n

    :type AllowedOAuthScopes: list
    :param AllowedOAuthScopes: The allowed OAuth scopes. Possible values provided by OAuth are: phone , email , openid , and profile . Possible values provided by AWS are: aws.cognito.signin.user.admin . Custom scopes created in Resource Servers are also supported.\n\n(string) --\n\n

    :type AllowedOAuthFlowsUserPoolClient: boolean
    :param AllowedOAuthFlowsUserPoolClient: Set to true if the client is allowed to follow the OAuth protocol when interacting with Cognito user pools.

    :type AnalyticsConfiguration: dict
    :param AnalyticsConfiguration: The Amazon Pinpoint analytics configuration for collecting metrics for this user pool.\n\nNote\nCognito User Pools only supports sending events to Amazon Pinpoint projects in the US East (N. Virginia) us-east-1 Region, regardless of the region in which the user pool resides.\n\n\nApplicationId (string) -- [REQUIRED]The application ID for an Amazon Pinpoint application.\n\nRoleArn (string) -- [REQUIRED]The ARN of an IAM role that authorizes Amazon Cognito to publish events to Amazon Pinpoint analytics.\n\nExternalId (string) -- [REQUIRED]The external ID.\n\nUserDataShared (boolean) --If UserDataShared is true , Amazon Cognito will include user data in the events it publishes to Amazon Pinpoint analytics.\n\n\n

    :type PreventUserExistenceErrors: string
    :param PreventUserExistenceErrors: Use this setting to choose which errors and responses are returned by Cognito APIs during authentication, account confirmation, and password recovery when the user does not exist in the user pool. When set to ENABLED and the user does not exist, authentication returns an error indicating either the username or password was incorrect, and account confirmation and password recovery return a response indicating a code was sent to a simulated destination. When set to LEGACY , those APIs will return a UserNotFoundException exception if the user does not exist in the user pool.\nValid values include:\n\nENABLED - This prevents user existence-related errors.\nLEGACY - This represents the old behavior of Cognito where user existence related errors are not prevented.\n\nThis setting affects the behavior of following APIs:\n\nAdminInitiateAuth\nAdminRespondToAuthChallenge\nInitiateAuth\nRespondToAuthChallenge\nForgotPassword\nConfirmForgotPassword\nConfirmSignUp\nResendConfirmationCode\n\n\nNote\nAfter February 15th 2020, the value of PreventUserExistenceErrors will default to ENABLED for newly created user pool clients if no value is provided.\n\n

    :rtype: dict

ReturnsResponse Syntax
{
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
            'ADMIN_NO_SRP_AUTH'|'CUSTOM_AUTH_FLOW_ONLY'|'USER_PASSWORD_AUTH'|'ALLOW_ADMIN_USER_PASSWORD_AUTH'|'ALLOW_CUSTOM_AUTH'|'ALLOW_USER_PASSWORD_AUTH'|'ALLOW_USER_SRP_AUTH'|'ALLOW_REFRESH_TOKEN_AUTH',
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
        'AllowedOAuthFlowsUserPoolClient': True|False,
        'AnalyticsConfiguration': {
            'ApplicationId': 'string',
            'RoleArn': 'string',
            'ExternalId': 'string',
            'UserDataShared': True|False
        },
        'PreventUserExistenceErrors': 'LEGACY'|'ENABLED'
    }
}


Response Structure

(dict) --
Represents the response from the server to the request to update the user pool client.

UserPoolClient (dict) --
The user pool client value from the response from the server when an update user pool client request is made.

UserPoolId (string) --
The user pool ID for the user pool client.

ClientName (string) --
The client name from the user pool request of the client type.

ClientId (string) --
The ID of the client associated with the user pool.

ClientSecret (string) --
The client secret from the user pool request of the client type.

LastModifiedDate (datetime) --
The date the user pool client was last modified.

CreationDate (datetime) --
The date the user pool client was created.

RefreshTokenValidity (integer) --
The time limit, in days, after which the refresh token is no longer valid and cannot be used.

ReadAttributes (list) --
The Read-only attributes.

(string) --


WriteAttributes (list) --
The writeable attributes.

(string) --


ExplicitAuthFlows (list) --
The authentication flows that are supported by the user pool clients. Flow names without the ALLOW_ prefix are deprecated in favor of new names with the ALLOW_ prefix. Note that values with ALLOW_ prefix cannot be used along with values without ALLOW_ prefix.
Valid values include:

ALLOW_ADMIN_USER_PASSWORD_AUTH : Enable admin based user password authentication flow ADMIN_USER_PASSWORD_AUTH . This setting replaces the ADMIN_NO_SRP_AUTH setting. With this authentication flow, Cognito receives the password in the request instead of using the SRP (Secure Remote Password protocol) protocol to verify passwords.
ALLOW_CUSTOM_AUTH : Enable Lambda trigger based authentication.
ALLOW_USER_PASSWORD_AUTH : Enable user password-based authentication. In this flow, Cognito receives the password in the request instead of using the SRP protocol to verify passwords.
ALLOW_USER_SRP_AUTH : Enable SRP based authentication.
ALLOW_REFRESH_TOKEN_AUTH : Enable authflow to refresh tokens.


(string) --


SupportedIdentityProviders (list) --
A list of provider names for the identity providers that are supported on this client.

(string) --


CallbackURLs (list) --
A list of allowed redirect (callback) URLs for the identity providers.
A redirect URI must:

Be an absolute URI.
Be registered with the authorization server.
Not include a fragment component.

See OAuth 2.0 - Redirection Endpoint .
Amazon Cognito requires HTTPS over HTTP except for http://localhost for testing purposes only.
App callback URLs such as myapp://example are also supported.

(string) --


LogoutURLs (list) --
A list of allowed logout URLs for the identity providers.

(string) --


DefaultRedirectURI (string) --
The default redirect URI. Must be in the CallbackURLs list.
A redirect URI must:

Be an absolute URI.
Be registered with the authorization server.
Not include a fragment component.

See OAuth 2.0 - Redirection Endpoint .
Amazon Cognito requires HTTPS over HTTP except for http://localhost for testing purposes only.
App callback URLs such as myapp://example are also supported.

AllowedOAuthFlows (list) --
The allowed OAuth flows.
Set to code to initiate a code grant flow, which provides an authorization code as the response. This code can be exchanged for access tokens with the token endpoint.
Set to implicit to specify that the client should get the access token (and, optionally, ID token, based on scopes) directly.
Set to client_credentials to specify that the client should get the access token (and, optionally, ID token, based on scopes) from the token endpoint using a combination of client and client_secret.

(string) --


AllowedOAuthScopes (list) --
The allowed OAuth scopes. Possible values provided by OAuth are: phone , email , openid , and profile . Possible values provided by AWS are: aws.cognito.signin.user.admin . Custom scopes created in Resource Servers are also supported.

(string) --


AllowedOAuthFlowsUserPoolClient (boolean) --
Set to true if the client is allowed to follow the OAuth protocol when interacting with Cognito user pools.

AnalyticsConfiguration (dict) --
The Amazon Pinpoint analytics configuration for the user pool client.

Note
Cognito User Pools only supports sending events to Amazon Pinpoint projects in the US East (N. Virginia) us-east-1 Region, regardless of the region in which the user pool resides.


ApplicationId (string) --
The application ID for an Amazon Pinpoint application.

RoleArn (string) --
The ARN of an IAM role that authorizes Amazon Cognito to publish events to Amazon Pinpoint analytics.

ExternalId (string) --
The external ID.

UserDataShared (boolean) --
If UserDataShared is true , Amazon Cognito will include user data in the events it publishes to Amazon Pinpoint analytics.



PreventUserExistenceErrors (string) --
Use this setting to choose which errors and responses are returned by Cognito APIs during authentication, account confirmation, and password recovery when the user does not exist in the user pool. When set to ENABLED and the user does not exist, authentication returns an error indicating either the username or password was incorrect, and account confirmation and password recovery return a response indicating a code was sent to a simulated destination. When set to LEGACY , those APIs will return a UserNotFoundException exception if the user does not exist in the user pool.
Valid values include:

ENABLED - This prevents user existence-related errors.
LEGACY - This represents the old behavior of Cognito where user existence related errors are not prevented.

This setting affects the behavior of following APIs:

AdminInitiateAuth
AdminRespondToAuthChallenge
InitiateAuth
RespondToAuthChallenge
ForgotPassword
ConfirmForgotPassword
ConfirmSignUp
ResendConfirmationCode


Note
After February 15th 2020, the value of PreventUserExistenceErrors will default to ENABLED for newly created user pool clients if no value is provided.










Exceptions

CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.ConcurrentModificationException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.ScopeDoesNotExistException
CognitoIdentityProvider.Client.exceptions.InvalidOAuthFlowException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


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
                'ADMIN_NO_SRP_AUTH'|'CUSTOM_AUTH_FLOW_ONLY'|'USER_PASSWORD_AUTH'|'ALLOW_ADMIN_USER_PASSWORD_AUTH'|'ALLOW_CUSTOM_AUTH'|'ALLOW_USER_PASSWORD_AUTH'|'ALLOW_USER_SRP_AUTH'|'ALLOW_REFRESH_TOKEN_AUTH',
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
            'AllowedOAuthFlowsUserPoolClient': True|False,
            'AnalyticsConfiguration': {
                'ApplicationId': 'string',
                'RoleArn': 'string',
                'ExternalId': 'string',
                'UserDataShared': True|False
            },
            'PreventUserExistenceErrors': 'LEGACY'|'ENABLED'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def update_user_pool_domain(Domain=None, UserPoolId=None, CustomDomainConfig=None):
    """
    Updates the Secure Sockets Layer (SSL) certificate for the custom domain for your user pool.
    You can use this operation to provide the Amazon Resource Name (ARN) of a new certificate to Amazon Cognito. You cannot use it to change the domain for a user pool.
    A custom domain is used to host the Amazon Cognito hosted UI, which provides sign-up and sign-in pages for your application. When you set up a custom domain, you provide a certificate that you manage with AWS Certificate Manager (ACM). When necessary, you can use this operation to change the certificate that you applied to your custom domain.
    Usually, this is unnecessary following routine certificate renewal with ACM. When you renew your existing certificate in ACM, the ARN for your certificate remains the same, and your custom domain uses the new certificate automatically.
    However, if you replace your existing certificate with a new one, ACM gives the new certificate a new ARN. To apply the new certificate to your custom domain, you must provide this ARN to Amazon Cognito.
    When you add your new certificate in ACM, you must choose US East (N. Virginia) as the AWS Region.
    After you submit your request, Amazon Cognito requires up to 1 hour to distribute your new certificate to your custom domain.
    For more information about adding a custom domain to your user pool, see Using Your Own Domain for the Hosted UI .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_user_pool_domain(
        Domain='string',
        UserPoolId='string',
        CustomDomainConfig={
            'CertificateArn': 'string'
        }
    )
    
    
    :type Domain: string
    :param Domain: [REQUIRED]\nThe domain name for the custom domain that hosts the sign-up and sign-in pages for your application. For example: auth.example.com .\nThis string can include only lowercase letters, numbers, and hyphens. Do not use a hyphen for the first or last character. Use periods to separate subdomain names.\n

    :type UserPoolId: string
    :param UserPoolId: [REQUIRED]\nThe ID of the user pool that is associated with the custom domain that you are updating the certificate for.\n

    :type CustomDomainConfig: dict
    :param CustomDomainConfig: [REQUIRED]\nThe configuration for a custom domain that hosts the sign-up and sign-in pages for your application. Use this object to specify an SSL certificate that is managed by ACM.\n\nCertificateArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of an AWS Certificate Manager SSL certificate. You use this certificate for the subdomain of your custom domain.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'CloudFrontDomain': 'string'
}


Response Structure

(dict) --
The UpdateUserPoolDomain response output.

CloudFrontDomain (string) --
The Amazon CloudFront endpoint that Amazon Cognito set up when you added the custom domain to your user pool.







Exceptions

CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


    :return: {
        'CloudFrontDomain': 'string'
    }
    
    
    :returns: 
    CognitoIdentityProvider.Client.exceptions.InvalidParameterException
    CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
    CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
    CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
    CognitoIdentityProvider.Client.exceptions.InternalErrorException
    
    """
    pass

def verify_software_token(AccessToken=None, Session=None, UserCode=None, FriendlyDeviceName=None):
    """
    Use this API to register a user\'s entered TOTP code and mark the user\'s software token MFA status as "verified" if successful. The request takes an access token or a session string, but not both.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.verify_software_token(
        AccessToken='string',
        Session='string',
        UserCode='string',
        FriendlyDeviceName='string'
    )
    
    
    :type AccessToken: string
    :param AccessToken: The access token.

    :type Session: string
    :param Session: The session which should be passed both ways in challenge-response calls to the service.

    :type UserCode: string
    :param UserCode: [REQUIRED]\nThe one time password computed using the secret code returned by\n

    :type FriendlyDeviceName: string
    :param FriendlyDeviceName: The friendly device name.

    :rtype: dict

ReturnsResponse Syntax
{
    'Status': 'SUCCESS'|'ERROR',
    'Session': 'string'
}


Response Structure

(dict) --

Status (string) --
The status of the verify software token.

Session (string) --
The session which should be passed both ways in challenge-response calls to the service.







Exceptions

CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.InvalidUserPoolConfigurationException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.PasswordResetRequiredException
CognitoIdentityProvider.Client.exceptions.UserNotFoundException
CognitoIdentityProvider.Client.exceptions.UserNotConfirmedException
CognitoIdentityProvider.Client.exceptions.InternalErrorException
CognitoIdentityProvider.Client.exceptions.EnableSoftwareTokenMFAException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.SoftwareTokenMFANotFoundException
CognitoIdentityProvider.Client.exceptions.CodeMismatchException


    :return: {
        'Status': 'SUCCESS'|'ERROR',
        'Session': 'string'
    }
    
    
    :returns: 
    CognitoIdentityProvider.Client.exceptions.InvalidParameterException
    CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
    CognitoIdentityProvider.Client.exceptions.InvalidUserPoolConfigurationException
    CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
    CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
    CognitoIdentityProvider.Client.exceptions.PasswordResetRequiredException
    CognitoIdentityProvider.Client.exceptions.UserNotFoundException
    CognitoIdentityProvider.Client.exceptions.UserNotConfirmedException
    CognitoIdentityProvider.Client.exceptions.InternalErrorException
    CognitoIdentityProvider.Client.exceptions.EnableSoftwareTokenMFAException
    CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
    CognitoIdentityProvider.Client.exceptions.SoftwareTokenMFANotFoundException
    CognitoIdentityProvider.Client.exceptions.CodeMismatchException
    
    """
    pass

def verify_user_attribute(AccessToken=None, AttributeName=None, Code=None):
    """
    Verifies the specified user attributes in the user pool.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.verify_user_attribute(
        AccessToken='string',
        AttributeName='string',
        Code='string'
    )
    
    
    :type AccessToken: string
    :param AccessToken: [REQUIRED]\nRepresents the access token of the request to verify user attributes.\n

    :type AttributeName: string
    :param AttributeName: [REQUIRED]\nThe attribute name in the request to verify user attributes.\n

    :type Code: string
    :param Code: [REQUIRED]\nThe verification code in the request to verify user attributes.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
A container representing the response from the server from the request to verify user attributes.





Exceptions

CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
CognitoIdentityProvider.Client.exceptions.InvalidParameterException
CognitoIdentityProvider.Client.exceptions.CodeMismatchException
CognitoIdentityProvider.Client.exceptions.ExpiredCodeException
CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
CognitoIdentityProvider.Client.exceptions.LimitExceededException
CognitoIdentityProvider.Client.exceptions.PasswordResetRequiredException
CognitoIdentityProvider.Client.exceptions.UserNotFoundException
CognitoIdentityProvider.Client.exceptions.UserNotConfirmedException
CognitoIdentityProvider.Client.exceptions.InternalErrorException


    :return: {}
    
    
    :returns: 
    CognitoIdentityProvider.Client.exceptions.ResourceNotFoundException
    CognitoIdentityProvider.Client.exceptions.InvalidParameterException
    CognitoIdentityProvider.Client.exceptions.CodeMismatchException
    CognitoIdentityProvider.Client.exceptions.ExpiredCodeException
    CognitoIdentityProvider.Client.exceptions.NotAuthorizedException
    CognitoIdentityProvider.Client.exceptions.TooManyRequestsException
    CognitoIdentityProvider.Client.exceptions.LimitExceededException
    CognitoIdentityProvider.Client.exceptions.PasswordResetRequiredException
    CognitoIdentityProvider.Client.exceptions.UserNotFoundException
    CognitoIdentityProvider.Client.exceptions.UserNotConfirmedException
    CognitoIdentityProvider.Client.exceptions.InternalErrorException
    
    """
    pass

