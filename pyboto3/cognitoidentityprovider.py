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

import boto3


class Cognitoidp(object):
    def __init__(self):
        self.client = boto3.client('Cognitoidp')

    def add_custom_attributes(self, UserPoolId=None, CustomAttributes=None):
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
        self.client.add_custom_attributes(UserPoolId=UserPoolId, CustomAttributes=CustomAttributes)

    def admin_confirm_sign_up(self, UserPoolId=None, Username=None):
        """
        :param UserPoolId: [REQUIRED]
            The user pool ID for which you want to confirm user registration.
            
        :type UserPoolId: string
        :param Username: [REQUIRED]
            The user name for which you want to confirm user registration.
            
        :type Username: string
        """
        self.client.admin_confirm_sign_up(UserPoolId=UserPoolId, Username=Username)

    def admin_delete_user(self, UserPoolId=None, Username=None):
        """
        :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool where you want to delete the user.
            
        :type UserPoolId: string
        :param Username: [REQUIRED]
            The user name of the user you wish to delete.
            
        :type Username: string
        """
        self.client.admin_delete_user(UserPoolId=UserPoolId, Username=Username)

    def admin_delete_user_attributes(self, UserPoolId=None, Username=None, UserAttributeNames=None):
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
        self.client.admin_delete_user_attributes(UserPoolId=UserPoolId, Username=Username,
                                                 UserAttributeNames=UserAttributeNames)

    def admin_disable_user(self, UserPoolId=None, Username=None):
        """
        :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool where you want to disable the user.
            
        :type UserPoolId: string
        :param Username: [REQUIRED]
            The user name of the user you wish to disable.
            
        :type Username: string
        """
        self.client.admin_disable_user(UserPoolId=UserPoolId, Username=Username)

    def admin_enable_user(self, UserPoolId=None, Username=None):
        """
        :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool where you want to enable the user.
            
        :type UserPoolId: string
        :param Username: [REQUIRED]
            The user name of the user you wish to ebable.
            
        :type Username: string
        """
        self.client.admin_enable_user(UserPoolId=UserPoolId, Username=Username)

    def admin_get_user(self, UserPoolId=None, Username=None):
        """
        :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool where you want to get information about the user.
            
        :type UserPoolId: string
        :param Username: [REQUIRED]
            The user name of the user you wish to retrieve.
            
        :type Username: string
        """
        self.client.admin_get_user(UserPoolId=UserPoolId, Username=Username)

    def admin_reset_user_password(self, UserPoolId=None, Username=None):
        """
        :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool where you want to reset the user's password.
            
        :type UserPoolId: string
        :param Username: [REQUIRED]
            The user name of the user whose password you wish to reset.
            
        :type Username: string
        """
        self.client.admin_reset_user_password(UserPoolId=UserPoolId, Username=Username)

    def admin_set_user_settings(self, UserPoolId=None, Username=None, MFAOptions=None):
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
        self.client.admin_set_user_settings(UserPoolId=UserPoolId, Username=Username, MFAOptions=MFAOptions)

    def admin_update_user_attributes(self, UserPoolId=None, Username=None, UserAttributes=None):
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
        self.client.admin_update_user_attributes(UserPoolId=UserPoolId, Username=Username,
                                                 UserAttributes=UserAttributes)

    def can_paginate(self, operation_name=None):
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
        self.client.can_paginate(operation_name=operation_name)

    def change_password(self, PreviousPassword=None, ProposedPassword=None, AccessToken=None):
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
        self.client.change_password(PreviousPassword=PreviousPassword, ProposedPassword=ProposedPassword,
                                    AccessToken=AccessToken)

    def confirm_forgot_password(self, ClientId=None, SecretHash=None, Username=None, ConfirmationCode=None,
                                Password=None):
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
        self.client.confirm_forgot_password(ClientId=ClientId, SecretHash=SecretHash, Username=Username,
                                            ConfirmationCode=ConfirmationCode, Password=Password)

    def confirm_sign_up(self, ClientId=None, SecretHash=None, Username=None, ConfirmationCode=None,
                        ForceAliasCreation=None):
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
        self.client.confirm_sign_up(ClientId=ClientId, SecretHash=SecretHash, Username=Username,
                                    ConfirmationCode=ConfirmationCode, ForceAliasCreation=ForceAliasCreation)

    def create_user_pool(self, PoolName=None, Policies=None, LambdaConfig=None, AutoVerifiedAttributes=None,
                         AliasAttributes=None, SmsVerificationMessage=None, EmailVerificationMessage=None,
                         EmailVerificationSubject=None, SmsAuthenticationMessage=None, MfaConfiguration=None):
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
        """
        self.client.create_user_pool(PoolName=PoolName, Policies=Policies, LambdaConfig=LambdaConfig,
                                     AutoVerifiedAttributes=AutoVerifiedAttributes, AliasAttributes=AliasAttributes,
                                     SmsVerificationMessage=SmsVerificationMessage,
                                     EmailVerificationMessage=EmailVerificationMessage,
                                     EmailVerificationSubject=EmailVerificationSubject,
                                     SmsAuthenticationMessage=SmsAuthenticationMessage,
                                     MfaConfiguration=MfaConfiguration)

    def create_user_pool_client(self, UserPoolId=None, ClientName=None, GenerateSecret=None):
        """
        :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool where you want to create a user pool client.
            
        :type UserPoolId: string
        :param ClientName: [REQUIRED]
            The client name for the user pool client you would like to create.
            
        :type ClientName: string
        :param GenerateSecret: Boolean to specify whether you want to generate a secret for the user pool client being created.
        :type GenerateSecret: boolean
        """
        self.client.create_user_pool_client(UserPoolId=UserPoolId, ClientName=ClientName, GenerateSecret=GenerateSecret)

    def delete_user(self, AccessToken=None):
        """
        :param AccessToken: The access token from a request to delete a user.
            ReturnsNone
            
        :type AccessToken: string
        """
        self.client.delete_user(AccessToken=AccessToken)

    def delete_user_attributes(self, UserAttributeNames=None, AccessToken=None):
        """
        :param UserAttributeNames: [REQUIRED]
            An array of strings representing the user attribute names you wish to delete.
            (string) --
            
        :type UserAttributeNames: list
        :param AccessToken: The access token used in the request to delete user attributes.
        :type AccessToken: string
        """
        self.client.delete_user_attributes(UserAttributeNames=UserAttributeNames, AccessToken=AccessToken)

    def delete_user_pool(self, UserPoolId=None):
        """
        :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool you want to delete.
            ReturnsNone
            
        :type UserPoolId: string
        """
        self.client.delete_user_pool(UserPoolId=UserPoolId)

    def delete_user_pool_client(self, UserPoolId=None, ClientId=None):
        """
        :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool where you want to delete the client.
            
        :type UserPoolId: string
        :param ClientId: [REQUIRED]
            The ID of the client associated with the user pool.
            
        :type ClientId: string
        """
        self.client.delete_user_pool_client(UserPoolId=UserPoolId, ClientId=ClientId)

    def describe_user_pool(self, UserPoolId=None):
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
                  'PostAuthentication': 'string'
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
                'EstimatedNumberOfUsers': 123
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
            EstimatedNumberOfUsers (integer) --A number estimating the size of the user pool.
            
            
            
        :type UserPoolId: string
        """
        self.client.describe_user_pool(UserPoolId=UserPoolId)

    def describe_user_pool_client(self, UserPoolId=None, ClientId=None):
        """
        :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool you want to describe.
            
        :type UserPoolId: string
        :param ClientId: [REQUIRED]
            The ID of the client associated with the user pool.
            
        :type ClientId: string
        """
        self.client.describe_user_pool_client(UserPoolId=UserPoolId, ClientId=ClientId)

    def forgot_password(self, ClientId=None, SecretHash=None, Username=None):
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
        self.client.forgot_password(ClientId=ClientId, SecretHash=SecretHash, Username=Username)

    def generate_presigned_url(self, ClientMethod=None, Params=None, ExpiresIn=None, HttpMethod=None):
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
        self.client.generate_presigned_url(ClientMethod=ClientMethod, Params=Params, ExpiresIn=ExpiresIn,
                                           HttpMethod=HttpMethod)

    def get_paginator(self, operation_name=None):
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
        self.client.get_paginator(operation_name=operation_name)

    def get_user(self, AccessToken=None):
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
        self.client.get_user(AccessToken=AccessToken)

    def get_user_attribute_verification_code(self, AccessToken=None, AttributeName=None):
        """
        :param AccessToken: The access token returned by the server response to get the user attribute verification code.
        :type AccessToken: string
        :param AttributeName: [REQUIRED]
            The attribute name returned by the server response to get the user attribute verification code.
            
        :type AttributeName: string
        """
        self.client.get_user_attribute_verification_code(AccessToken=AccessToken, AttributeName=AttributeName)

    def get_waiter(self):
        """
        """
        self.client.get_waiter()

    def list_user_pool_clients(self, UserPoolId=None, MaxResults=None, NextToken=None):
        """
        :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool where you want to list user pool clients.
            
        :type UserPoolId: string
        :param MaxResults: The maximum number of results you want the request to return when listing the user pool clients.
        :type MaxResults: integer
        :param NextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
        :type NextToken: string
        """
        self.client.list_user_pool_clients(UserPoolId=UserPoolId, MaxResults=MaxResults, NextToken=NextToken)

    def list_user_pools(self, NextToken=None, MaxResults=None):
        """
        :param NextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
        :type NextToken: string
        :param MaxResults: [REQUIRED]
            The maximum number of results you want the request to return when listing the user pools.
            
        :type MaxResults: integer
        """
        self.client.list_user_pools(NextToken=NextToken, MaxResults=MaxResults)

    def list_users(self, UserPoolId=None, AttributesToGet=None, Limit=None, PaginationToken=None, UserStatus=None):
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
        :param UserStatus: The user status. Can be one of the following:
            UNCONFIRMED - User has been created but not confirmed.
            CONFIRMED - User has been confirmed.
            ARCHIVED - User is no longer active.
            COMPROMISED - User is disabled due to a potential security threat.
            UNKNOWN - User status is not known.
            
        :type UserStatus: string
        """
        self.client.list_users(UserPoolId=UserPoolId, AttributesToGet=AttributesToGet, Limit=Limit,
                               PaginationToken=PaginationToken, UserStatus=UserStatus)

    def resend_confirmation_code(self, ClientId=None, SecretHash=None, Username=None):
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
        self.client.resend_confirmation_code(ClientId=ClientId, SecretHash=SecretHash, Username=Username)

    def set_user_settings(self, AccessToken=None, MFAOptions=None):
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
        self.client.set_user_settings(AccessToken=AccessToken, MFAOptions=MFAOptions)

    def sign_up(self, ClientId=None, SecretHash=None, Username=None, Password=None, UserAttributes=None,
                ValidationData=None):
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
        self.client.sign_up(ClientId=ClientId, SecretHash=SecretHash, Username=Username, Password=Password,
                            UserAttributes=UserAttributes, ValidationData=ValidationData)

    def update_user_attributes(self, UserAttributes=None, AccessToken=None):
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
        self.client.update_user_attributes(UserAttributes=UserAttributes, AccessToken=AccessToken)

    def update_user_pool(self, UserPoolId=None, Policies=None, LambdaConfig=None, AutoVerifiedAttributes=None,
                         SmsVerificationMessage=None, EmailVerificationMessage=None, EmailVerificationSubject=None,
                         SmsAuthenticationMessage=None, MfaConfiguration=None):
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
            
        :type LambdaConfig: dict
        :param AutoVerifiedAttributes: The attributes that are automatically verified when the Amazon Cognito service makes a request to update user pools.
            (string) --
            
        :type AutoVerifiedAttributes: list
        :param SmsVerificationMessage: A container with information about the SMS verification message.
        :type SmsVerificationMessage: string
        :param EmailVerificationMessage: The contents of the email verification message.
        :type EmailVerificationMessage: string
        :param EmailVerificationSubject: The subject of the email verfication message
        :type EmailVerificationSubject: string
        :param SmsAuthenticationMessage: The contents of the SMS authentication message.
        :type SmsAuthenticationMessage: string
        :param MfaConfiguration: Can be one of the following values:
            OFF - MFA tokens are not required and cannot be specified during user registration.
            ON - MFA tokens are required for all user registrations. You can only specify required when you are initially creating a user pool.
            OPTIONAL - Users have the option when registering to create an MFA token.
            
        :type MfaConfiguration: string
        """
        self.client.update_user_pool(UserPoolId=UserPoolId, Policies=Policies, LambdaConfig=LambdaConfig,
                                     AutoVerifiedAttributes=AutoVerifiedAttributes,
                                     SmsVerificationMessage=SmsVerificationMessage,
                                     EmailVerificationMessage=EmailVerificationMessage,
                                     EmailVerificationSubject=EmailVerificationSubject,
                                     SmsAuthenticationMessage=SmsAuthenticationMessage,
                                     MfaConfiguration=MfaConfiguration)

    def update_user_pool_client(self, UserPoolId=None, ClientId=None, ClientName=None):
        """
        :param UserPoolId: [REQUIRED]
            The user pool ID for the user pool where you want to update the user pool client.
            
        :type UserPoolId: string
        :param ClientId: [REQUIRED]
            The ID of the client associated with the user pool.
            
        :type ClientId: string
        :param ClientName: The client name from the update user pool client request.
        :type ClientName: string
        """
        self.client.update_user_pool_client(UserPoolId=UserPoolId, ClientId=ClientId, ClientName=ClientName)

    def verify_user_attribute(self, AccessToken=None, AttributeName=None, Code=None):
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
        self.client.verify_user_attribute(AccessToken=AccessToken, AttributeName=AttributeName, Code=Code)
