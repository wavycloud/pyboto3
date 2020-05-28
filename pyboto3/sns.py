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

def add_permission(TopicArn=None, Label=None, AWSAccountId=None, ActionName=None):
    """
    Adds a statement to a topic\'s access control policy, granting access for the specified AWS accounts to the specified actions.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.add_permission(
        TopicArn='string',
        Label='string',
        AWSAccountId=[
            'string',
        ],
        ActionName=[
            'string',
        ]
    )
    
    
    :type TopicArn: string
    :param TopicArn: [REQUIRED]\nThe ARN of the topic whose access control policy you wish to modify.\n

    :type Label: string
    :param Label: [REQUIRED]\nA unique identifier for the new policy statement.\n

    :type AWSAccountId: list
    :param AWSAccountId: [REQUIRED]\nThe AWS account IDs of the users (principals) who will be given access to the specified actions. The users must have AWS accounts, but do not need to be signed up for this service.\n\n(string) --\n\n

    :type ActionName: list
    :param ActionName: [REQUIRED]\nThe action you want to allow for the specified principal(s).\nValid values: Any Amazon SNS action name, for example Publish .\n\n(string) --\n\n

    :returns: 
    SNS.Client.exceptions.InvalidParameterException
    SNS.Client.exceptions.InternalErrorException
    SNS.Client.exceptions.AuthorizationErrorException
    SNS.Client.exceptions.NotFoundException
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def check_if_phone_number_is_opted_out(phoneNumber=None):
    """
    Accepts a phone number and indicates whether the phone holder has opted out of receiving SMS messages from your account. You cannot send SMS messages to a number that is opted out.
    To resume sending messages, you can opt in the number by using the OptInPhoneNumber action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.check_if_phone_number_is_opted_out(
        phoneNumber='string'
    )
    
    
    :type phoneNumber: string
    :param phoneNumber: [REQUIRED]\nThe phone number for which you want to check the opt out status.\n

    :rtype: dict
ReturnsResponse Syntax{
    'isOptedOut': True|False
}


Response Structure

(dict) --The response from the CheckIfPhoneNumberIsOptedOut action.

isOptedOut (boolean) --Indicates whether the phone number is opted out:

true \xe2\x80\x93 The phone number is opted out, meaning you cannot publish SMS messages to it.
false \xe2\x80\x93 The phone number is opted in, meaning you can publish SMS messages to it.







Exceptions

SNS.Client.exceptions.ThrottledException
SNS.Client.exceptions.InternalErrorException
SNS.Client.exceptions.AuthorizationErrorException
SNS.Client.exceptions.InvalidParameterException


    :return: {
        'isOptedOut': True|False
    }
    
    
    :returns: 
    SNS.Client.exceptions.ThrottledException
    SNS.Client.exceptions.InternalErrorException
    SNS.Client.exceptions.AuthorizationErrorException
    SNS.Client.exceptions.InvalidParameterException
    
    """
    pass

def confirm_subscription(TopicArn=None, Token=None, AuthenticateOnUnsubscribe=None):
    """
    Verifies an endpoint owner\'s intent to receive messages by validating the token sent to the endpoint by an earlier Subscribe action. If the token is valid, the action creates a new subscription and returns its Amazon Resource Name (ARN). This call requires an AWS signature only when the AuthenticateOnUnsubscribe flag is set to "true".
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.confirm_subscription(
        TopicArn='string',
        Token='string',
        AuthenticateOnUnsubscribe='string'
    )
    
    
    :type TopicArn: string
    :param TopicArn: [REQUIRED]\nThe ARN of the topic for which you wish to confirm a subscription.\n

    :type Token: string
    :param Token: [REQUIRED]\nShort-lived token sent to an endpoint during the Subscribe action.\n

    :type AuthenticateOnUnsubscribe: string
    :param AuthenticateOnUnsubscribe: Disallows unauthenticated unsubscribes of the subscription. If the value of this parameter is true and the request has an AWS signature, then only the topic owner and the subscription owner can unsubscribe the endpoint. The unsubscribe action requires AWS authentication.

    :rtype: dict

ReturnsResponse Syntax
{
    'SubscriptionArn': 'string'
}


Response Structure

(dict) --
Response for ConfirmSubscriptions action.

SubscriptionArn (string) --
The ARN of the created subscription.







Exceptions

SNS.Client.exceptions.SubscriptionLimitExceededException
SNS.Client.exceptions.InvalidParameterException
SNS.Client.exceptions.NotFoundException
SNS.Client.exceptions.InternalErrorException
SNS.Client.exceptions.AuthorizationErrorException
SNS.Client.exceptions.FilterPolicyLimitExceededException


    :return: {
        'SubscriptionArn': 'string'
    }
    
    
    :returns: 
    SNS.Client.exceptions.SubscriptionLimitExceededException
    SNS.Client.exceptions.InvalidParameterException
    SNS.Client.exceptions.NotFoundException
    SNS.Client.exceptions.InternalErrorException
    SNS.Client.exceptions.AuthorizationErrorException
    SNS.Client.exceptions.FilterPolicyLimitExceededException
    
    """
    pass

def create_platform_application(Name=None, Platform=None, Attributes=None):
    """
    Creates a platform application object for one of the supported push notification services, such as APNS and FCM, to which devices and mobile apps may register. You must specify PlatformPrincipal and PlatformCredential attributes when using the CreatePlatformApplication action. The PlatformPrincipal is received from the notification service. For APNS/APNS_SANDBOX, PlatformPrincipal is "SSL certificate". For FCM, PlatformPrincipal is not applicable. For ADM, PlatformPrincipal is "client id". The PlatformCredential is also received from the notification service. For WNS, PlatformPrincipal is "Package Security Identifier". For MPNS, PlatformPrincipal is "TLS certificate". For Baidu, PlatformPrincipal is "API key".
    For APNS/APNS_SANDBOX, PlatformCredential is "private key". For FCM, PlatformCredential is "API key". For ADM, PlatformCredential is "client secret". For WNS, PlatformCredential is "secret key". For MPNS, PlatformCredential is "private key". For Baidu, PlatformCredential is "secret key". The PlatformApplicationArn that is returned when using CreatePlatformApplication is then used as an attribute for the CreatePlatformEndpoint action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_platform_application(
        Name='string',
        Platform='string',
        Attributes={
            'string': 'string'
        }
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nApplication names must be made up of only uppercase and lowercase ASCII letters, numbers, underscores, hyphens, and periods, and must be between 1 and 256 characters long.\n

    :type Platform: string
    :param Platform: [REQUIRED]\nThe following platforms are supported: ADM (Amazon Device Messaging), APNS (Apple Push Notification Service), APNS_SANDBOX, and FCM (Firebase Cloud Messaging).\n

    :type Attributes: dict
    :param Attributes: [REQUIRED]\nFor a list of attributes, see SetPlatformApplicationAttributes\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'PlatformApplicationArn': 'string'
}


Response Structure

(dict) --
Response from CreatePlatformApplication action.

PlatformApplicationArn (string) --
PlatformApplicationArn is returned.







Exceptions

SNS.Client.exceptions.InvalidParameterException
SNS.Client.exceptions.InternalErrorException
SNS.Client.exceptions.AuthorizationErrorException


    :return: {
        'PlatformApplicationArn': 'string'
    }
    
    
    :returns: 
    SNS.Client.exceptions.InvalidParameterException
    SNS.Client.exceptions.InternalErrorException
    SNS.Client.exceptions.AuthorizationErrorException
    
    """
    pass

def create_platform_endpoint(PlatformApplicationArn=None, Token=None, CustomUserData=None, Attributes=None):
    """
    Creates an endpoint for a device and mobile app on one of the supported push notification services, such as FCM and APNS. CreatePlatformEndpoint requires the PlatformApplicationArn that is returned from CreatePlatformApplication . The EndpointArn that is returned when using CreatePlatformEndpoint can then be used by the Publish action to send a message to a mobile app or by the Subscribe action for subscription to a topic. The CreatePlatformEndpoint action is idempotent, so if the requester already owns an endpoint with the same device token and attributes, that endpoint\'s ARN is returned without creating a new endpoint. For more information, see Using Amazon SNS Mobile Push Notifications .
    When using CreatePlatformEndpoint with Baidu, two attributes must be provided: ChannelId and UserId. The token field must also contain the ChannelId. For more information, see Creating an Amazon SNS Endpoint for Baidu .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_platform_endpoint(
        PlatformApplicationArn='string',
        Token='string',
        CustomUserData='string',
        Attributes={
            'string': 'string'
        }
    )
    
    
    :type PlatformApplicationArn: string
    :param PlatformApplicationArn: [REQUIRED]\nPlatformApplicationArn returned from CreatePlatformApplication is used to create a an endpoint.\n

    :type Token: string
    :param Token: [REQUIRED]\nUnique identifier created by the notification service for an app on a device. The specific name for Token will vary, depending on which notification service is being used. For example, when using APNS as the notification service, you need the device token. Alternatively, when using FCM or ADM, the device token equivalent is called the registration ID.\n

    :type CustomUserData: string
    :param CustomUserData: Arbitrary user data to associate with the endpoint. Amazon SNS does not use this data. The data must be in UTF-8 format and less than 2KB.

    :type Attributes: dict
    :param Attributes: For a list of attributes, see SetEndpointAttributes .\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'EndpointArn': 'string'
}


Response Structure

(dict) --
Response from CreateEndpoint action.

EndpointArn (string) --
EndpointArn returned from CreateEndpoint action.







Exceptions

SNS.Client.exceptions.InvalidParameterException
SNS.Client.exceptions.InternalErrorException
SNS.Client.exceptions.AuthorizationErrorException
SNS.Client.exceptions.NotFoundException


    :return: {
        'EndpointArn': 'string'
    }
    
    
    :returns: 
    SNS.Client.exceptions.InvalidParameterException
    SNS.Client.exceptions.InternalErrorException
    SNS.Client.exceptions.AuthorizationErrorException
    SNS.Client.exceptions.NotFoundException
    
    """
    pass

def create_topic(Name=None, Attributes=None, Tags=None):
    """
    Creates a topic to which notifications can be published. Users can create at most 100,000 topics. For more information, see https://aws.amazon.com/sns . This action is idempotent, so if the requester already owns a topic with the specified name, that topic\'s ARN is returned without creating a new topic.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_topic(
        Name='string',
        Attributes={
            'string': 'string'
        },
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the topic you want to create.\nConstraints: Topic names must be made up of only uppercase and lowercase ASCII letters, numbers, underscores, and hyphens, and must be between 1 and 256 characters long.\n

    :type Attributes: dict
    :param Attributes: A map of attributes with their corresponding values.\nThe following lists the names, descriptions, and values of the special request parameters that the CreateTopic action uses:\n\nDeliveryPolicy \xe2\x80\x93 The policy that defines how Amazon SNS retries failed deliveries to HTTP/S endpoints.\nDisplayName \xe2\x80\x93 The display name to use for a topic with SMS subscriptions.\nPolicy \xe2\x80\x93 The policy that defines who can access your topic. By default, only the topic owner can publish or subscribe to the topic.\n\nThe following attribute applies only to server-side-encryption :\n\nKmsMasterKeyId - The ID of an AWS-managed customer master key (CMK) for Amazon SNS or a custom CMK. For more information, see Key Terms . For more examples, see KeyId in the AWS Key Management Service API Reference .\n\n\n(string) --\n(string) --\n\n\n\n

    :type Tags: list
    :param Tags: The list of tags to add to a new topic.\n\nNote\nTo be able to tag a topic on creation, you must have the sns:CreateTopic and sns:TagResource permissions.\n\n\n(dict) --The list of tags to be added to the specified topic.\n\nKey (string) -- [REQUIRED]The required key portion of the tag.\n\nValue (string) -- [REQUIRED]The optional value portion of the tag.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'TopicArn': 'string'
}


Response Structure

(dict) --
Response from CreateTopic action.

TopicArn (string) --
The Amazon Resource Name (ARN) assigned to the created topic.







Exceptions

SNS.Client.exceptions.InvalidParameterException
SNS.Client.exceptions.TopicLimitExceededException
SNS.Client.exceptions.InternalErrorException
SNS.Client.exceptions.AuthorizationErrorException
SNS.Client.exceptions.InvalidSecurityException
SNS.Client.exceptions.TagLimitExceededException
SNS.Client.exceptions.StaleTagException
SNS.Client.exceptions.TagPolicyException
SNS.Client.exceptions.ConcurrentAccessException


    :return: {
        'TopicArn': 'string'
    }
    
    
    :returns: 
    SNS.Client.exceptions.InvalidParameterException
    SNS.Client.exceptions.TopicLimitExceededException
    SNS.Client.exceptions.InternalErrorException
    SNS.Client.exceptions.AuthorizationErrorException
    SNS.Client.exceptions.InvalidSecurityException
    SNS.Client.exceptions.TagLimitExceededException
    SNS.Client.exceptions.StaleTagException
    SNS.Client.exceptions.TagPolicyException
    SNS.Client.exceptions.ConcurrentAccessException
    
    """
    pass

def delete_endpoint(EndpointArn=None):
    """
    Deletes the endpoint for a device and mobile app from Amazon SNS. This action is idempotent. For more information, see Using Amazon SNS Mobile Push Notifications .
    When you delete an endpoint that is also subscribed to a topic, then you must also unsubscribe the endpoint from the topic.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_endpoint(
        EndpointArn='string'
    )
    
    
    :type EndpointArn: string
    :param EndpointArn: [REQUIRED]\nEndpointArn of endpoint to delete.\n

    """
    pass

def delete_platform_application(PlatformApplicationArn=None):
    """
    Deletes a platform application object for one of the supported push notification services, such as APNS and FCM. For more information, see Using Amazon SNS Mobile Push Notifications .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_platform_application(
        PlatformApplicationArn='string'
    )
    
    
    :type PlatformApplicationArn: string
    :param PlatformApplicationArn: [REQUIRED]\nPlatformApplicationArn of platform application object to delete.\n

    """
    pass

def delete_topic(TopicArn=None):
    """
    Deletes a topic and all its subscriptions. Deleting a topic might prevent some messages previously sent to the topic from being delivered to subscribers. This action is idempotent, so deleting a topic that does not exist does not result in an error.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_topic(
        TopicArn='string'
    )
    
    
    :type TopicArn: string
    :param TopicArn: [REQUIRED]\nThe ARN of the topic you want to delete.\n

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

def get_endpoint_attributes(EndpointArn=None):
    """
    Retrieves the endpoint attributes for a device on one of the supported push notification services, such as FCM and APNS. For more information, see Using Amazon SNS Mobile Push Notifications .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_endpoint_attributes(
        EndpointArn='string'
    )
    
    
    :type EndpointArn: string
    :param EndpointArn: [REQUIRED]\nEndpointArn for GetEndpointAttributes input.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Attributes': {
        'string': 'string'
    }
}


Response Structure

(dict) --Response from GetEndpointAttributes of the EndpointArn.

Attributes (dict) --Attributes include the following:

CustomUserData \xe2\x80\x93 arbitrary user data to associate with the endpoint. Amazon SNS does not use this data. The data must be in UTF-8 format and less than 2KB.
Enabled \xe2\x80\x93 flag that enables/disables delivery to the endpoint. Amazon SNS will set this to false when a notification service indicates to Amazon SNS that the endpoint is invalid. Users can set it back to true, typically after updating Token.
Token \xe2\x80\x93 device token, also referred to as a registration id, for an app and mobile device. This is returned from the notification service when an app and mobile device are registered with the notification service.


Note
The device token for the iOS platform is returned in lowercase.


(string) --
(string) --









Exceptions

SNS.Client.exceptions.InvalidParameterException
SNS.Client.exceptions.InternalErrorException
SNS.Client.exceptions.AuthorizationErrorException
SNS.Client.exceptions.NotFoundException


    :return: {
        'Attributes': {
            'string': 'string'
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
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    :rtype: L{botocore.paginate.Paginator}
ReturnsA paginator object.


    """
    pass

def get_platform_application_attributes(PlatformApplicationArn=None):
    """
    Retrieves the attributes of the platform application object for the supported push notification services, such as APNS and FCM. For more information, see Using Amazon SNS Mobile Push Notifications .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_platform_application_attributes(
        PlatformApplicationArn='string'
    )
    
    
    :type PlatformApplicationArn: string
    :param PlatformApplicationArn: [REQUIRED]\nPlatformApplicationArn for GetPlatformApplicationAttributesInput.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Attributes': {
        'string': 'string'
    }
}


Response Structure

(dict) --Response for GetPlatformApplicationAttributes action.

Attributes (dict) --Attributes include the following:

EventEndpointCreated \xe2\x80\x93 Topic ARN to which EndpointCreated event notifications should be sent.
EventEndpointDeleted \xe2\x80\x93 Topic ARN to which EndpointDeleted event notifications should be sent.
EventEndpointUpdated \xe2\x80\x93 Topic ARN to which EndpointUpdate event notifications should be sent.
EventDeliveryFailure \xe2\x80\x93 Topic ARN to which DeliveryFailure event notifications should be sent upon Direct Publish delivery failure (permanent) to one of the application\'s endpoints.


(string) --
(string) --









Exceptions

SNS.Client.exceptions.InvalidParameterException
SNS.Client.exceptions.InternalErrorException
SNS.Client.exceptions.AuthorizationErrorException
SNS.Client.exceptions.NotFoundException


    :return: {
        'Attributes': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def get_sms_attributes(attributes=None):
    """
    Returns the settings for sending SMS messages from your account.
    These settings are set with the SetSMSAttributes action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_sms_attributes(
        attributes=[
            'string',
        ]
    )
    
    
    :type attributes: list
    :param attributes: A list of the individual attribute names, such as MonthlySpendLimit , for which you want values.\nFor all attribute names, see SetSMSAttributes .\nIf you don\'t use this parameter, Amazon SNS returns all SMS attributes.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'attributes': {
        'string': 'string'
    }
}


Response Structure

(dict) --The response from the GetSMSAttributes request.

attributes (dict) --The SMS attribute names and their values.

(string) --
(string) --









Exceptions

SNS.Client.exceptions.ThrottledException
SNS.Client.exceptions.InternalErrorException
SNS.Client.exceptions.AuthorizationErrorException
SNS.Client.exceptions.InvalidParameterException


    :return: {
        'attributes': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def get_subscription_attributes(SubscriptionArn=None):
    """
    Returns all of the properties of a subscription.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_subscription_attributes(
        SubscriptionArn='string'
    )
    
    
    :type SubscriptionArn: string
    :param SubscriptionArn: [REQUIRED]\nThe ARN of the subscription whose properties you want to get.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Attributes': {
        'string': 'string'
    }
}


Response Structure

(dict) --Response for GetSubscriptionAttributes action.

Attributes (dict) --A map of the subscription\'s attributes. Attributes in this map include the following:

ConfirmationWasAuthenticated \xe2\x80\x93 true if the subscription confirmation request was authenticated.
DeliveryPolicy \xe2\x80\x93 The JSON serialization of the subscription\'s delivery policy.
EffectiveDeliveryPolicy \xe2\x80\x93 The JSON serialization of the effective delivery policy that takes into account the topic delivery policy and account system defaults.
FilterPolicy \xe2\x80\x93 The filter policy JSON that is assigned to the subscription.
Owner \xe2\x80\x93 The AWS account ID of the subscription\'s owner.
PendingConfirmation \xe2\x80\x93 true if the subscription hasn\'t been confirmed. To confirm a pending subscription, call the ConfirmSubscription action with a confirmation token.
RawMessageDelivery \xe2\x80\x93 true if raw message delivery is enabled for the subscription. Raw messages are free of JSON formatting and can be sent to HTTP/S and Amazon SQS endpoints.
RedrivePolicy \xe2\x80\x93 When specified, sends undeliverable messages to the specified Amazon SQS dead-letter queue. Messages that can\'t be delivered due to client errors (for example, when the subscribed endpoint is unreachable) or server errors (for example, when the service that powers the subscribed endpoint becomes unavailable) are held in the dead-letter queue for further analysis or reprocessing.
SubscriptionArn \xe2\x80\x93 The subscription\'s ARN.
TopicArn \xe2\x80\x93 The topic ARN that the subscription is associated with.


(string) --
(string) --









Exceptions

SNS.Client.exceptions.InvalidParameterException
SNS.Client.exceptions.InternalErrorException
SNS.Client.exceptions.NotFoundException
SNS.Client.exceptions.AuthorizationErrorException


    :return: {
        'Attributes': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def get_topic_attributes(TopicArn=None):
    """
    Returns all of the properties of a topic. Topic properties returned might differ based on the authorization of the user.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_topic_attributes(
        TopicArn='string'
    )
    
    
    :type TopicArn: string
    :param TopicArn: [REQUIRED]\nThe ARN of the topic whose properties you want to get.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Attributes': {
        'string': 'string'
    }
}


Response Structure

(dict) --Response for GetTopicAttributes action.

Attributes (dict) --A map of the topic\'s attributes. Attributes in this map include the following:

DeliveryPolicy \xe2\x80\x93 The JSON serialization of the topic\'s delivery policy.
DisplayName \xe2\x80\x93 The human-readable name used in the From field for notifications to email and email-json endpoints.
Owner \xe2\x80\x93 The AWS account ID of the topic\'s owner.
Policy \xe2\x80\x93 The JSON serialization of the topic\'s access control policy.
SubscriptionsConfirmed \xe2\x80\x93 The number of confirmed subscriptions for the topic.
SubscriptionsDeleted \xe2\x80\x93 The number of deleted subscriptions for the topic.
SubscriptionsPending \xe2\x80\x93 The number of subscriptions pending confirmation for the topic.
TopicArn \xe2\x80\x93 The topic\'s ARN.
EffectiveDeliveryPolicy \xe2\x80\x93 Yhe JSON serialization of the effective delivery policy, taking system defaults into account.

The following attribute applies only to server-side-encryption :

KmsMasterKeyId - The ID of an AWS-managed customer master key (CMK) for Amazon SNS or a custom CMK. For more information, see Key Terms . For more examples, see KeyId in the AWS Key Management Service API Reference .


(string) --
(string) --









Exceptions

SNS.Client.exceptions.InvalidParameterException
SNS.Client.exceptions.InternalErrorException
SNS.Client.exceptions.NotFoundException
SNS.Client.exceptions.AuthorizationErrorException
SNS.Client.exceptions.InvalidSecurityException


    :return: {
        'Attributes': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    KmsMasterKeyId - The ID of an AWS-managed customer master key (CMK) for Amazon SNS or a custom CMK. For more information, see Key Terms . For more examples, see KeyId in the AWS Key Management Service API Reference .
    
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

def list_endpoints_by_platform_application(PlatformApplicationArn=None, NextToken=None):
    """
    Lists the endpoints and endpoint attributes for devices in a supported push notification service, such as FCM and APNS. The results for ListEndpointsByPlatformApplication are paginated and return a limited list of endpoints, up to 100. If additional records are available after the first page results, then a NextToken string will be returned. To receive the next page, you call ListEndpointsByPlatformApplication again using the NextToken string received from the previous call. When there are no more records to return, NextToken will be null. For more information, see Using Amazon SNS Mobile Push Notifications .
    This action is throttled at 30 transactions per second (TPS).
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_endpoints_by_platform_application(
        PlatformApplicationArn='string',
        NextToken='string'
    )
    
    
    :type PlatformApplicationArn: string
    :param PlatformApplicationArn: [REQUIRED]\nPlatformApplicationArn for ListEndpointsByPlatformApplicationInput action.\n

    :type NextToken: string
    :param NextToken: NextToken string is used when calling ListEndpointsByPlatformApplication action to retrieve additional records that are available after the first page results.

    :rtype: dict

ReturnsResponse Syntax
{
    'Endpoints': [
        {
            'EndpointArn': 'string',
            'Attributes': {
                'string': 'string'
            }
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
Response for ListEndpointsByPlatformApplication action.

Endpoints (list) --
Endpoints returned for ListEndpointsByPlatformApplication action.

(dict) --
Endpoint for mobile app and device.

EndpointArn (string) --
EndpointArn for mobile app and device.

Attributes (dict) --
Attributes for endpoint.

(string) --
(string) --








NextToken (string) --
NextToken string is returned when calling ListEndpointsByPlatformApplication action if additional records are available after the first page results.







Exceptions

SNS.Client.exceptions.InvalidParameterException
SNS.Client.exceptions.InternalErrorException
SNS.Client.exceptions.AuthorizationErrorException
SNS.Client.exceptions.NotFoundException


    :return: {
        'Endpoints': [
            {
                'EndpointArn': 'string',
                'Attributes': {
                    'string': 'string'
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def list_phone_numbers_opted_out(nextToken=None):
    """
    Returns a list of phone numbers that are opted out, meaning you cannot send SMS messages to them.
    The results for ListPhoneNumbersOptedOut are paginated, and each page returns up to 100 phone numbers. If additional phone numbers are available after the first page of results, then a NextToken string will be returned. To receive the next page, you call ListPhoneNumbersOptedOut again using the NextToken string received from the previous call. When there are no more records to return, NextToken will be null.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_phone_numbers_opted_out(
        nextToken='string'
    )
    
    
    :type nextToken: string
    :param nextToken: A NextToken string is used when you call the ListPhoneNumbersOptedOut action to retrieve additional records that are available after the first page of results.

    :rtype: dict
ReturnsResponse Syntax{
    'phoneNumbers': [
        'string',
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --The response from the ListPhoneNumbersOptedOut action.

phoneNumbers (list) --A list of phone numbers that are opted out of receiving SMS messages. The list is paginated, and each page can contain up to 100 phone numbers.

(string) --


nextToken (string) --A NextToken string is returned when you call the ListPhoneNumbersOptedOut action if additional records are available after the first page of results.






Exceptions

SNS.Client.exceptions.ThrottledException
SNS.Client.exceptions.InternalErrorException
SNS.Client.exceptions.AuthorizationErrorException
SNS.Client.exceptions.InvalidParameterException


    :return: {
        'phoneNumbers': [
            'string',
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    SNS.Client.exceptions.ThrottledException
    SNS.Client.exceptions.InternalErrorException
    SNS.Client.exceptions.AuthorizationErrorException
    SNS.Client.exceptions.InvalidParameterException
    
    """
    pass

def list_platform_applications(NextToken=None):
    """
    Lists the platform application objects for the supported push notification services, such as APNS and FCM. The results for ListPlatformApplications are paginated and return a limited list of applications, up to 100. If additional records are available after the first page results, then a NextToken string will be returned. To receive the next page, you call ListPlatformApplications using the NextToken string received from the previous call. When there are no more records to return, NextToken will be null. For more information, see Using Amazon SNS Mobile Push Notifications .
    This action is throttled at 15 transactions per second (TPS).
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_platform_applications(
        NextToken='string'
    )
    
    
    :type NextToken: string
    :param NextToken: NextToken string is used when calling ListPlatformApplications action to retrieve additional records that are available after the first page results.

    :rtype: dict
ReturnsResponse Syntax{
    'PlatformApplications': [
        {
            'PlatformApplicationArn': 'string',
            'Attributes': {
                'string': 'string'
            }
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --Response for ListPlatformApplications action.

PlatformApplications (list) --Platform applications returned when calling ListPlatformApplications action.

(dict) --Platform application object.

PlatformApplicationArn (string) --PlatformApplicationArn for platform application object.

Attributes (dict) --Attributes for platform application object.

(string) --
(string) --








NextToken (string) --NextToken string is returned when calling ListPlatformApplications action if additional records are available after the first page results.






Exceptions

SNS.Client.exceptions.InvalidParameterException
SNS.Client.exceptions.InternalErrorException
SNS.Client.exceptions.AuthorizationErrorException


    :return: {
        'PlatformApplications': [
            {
                'PlatformApplicationArn': 'string',
                'Attributes': {
                    'string': 'string'
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    SNS.Client.exceptions.InvalidParameterException
    SNS.Client.exceptions.InternalErrorException
    SNS.Client.exceptions.AuthorizationErrorException
    
    """
    pass

def list_subscriptions(NextToken=None):
    """
    Returns a list of the requester\'s subscriptions. Each call returns a limited list of subscriptions, up to 100. If there are more subscriptions, a NextToken is also returned. Use the NextToken parameter in a new ListSubscriptions call to get further results.
    This action is throttled at 30 transactions per second (TPS).
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_subscriptions(
        NextToken='string'
    )
    
    
    :type NextToken: string
    :param NextToken: Token returned by the previous ListSubscriptions request.

    :rtype: dict
ReturnsResponse Syntax{
    'Subscriptions': [
        {
            'SubscriptionArn': 'string',
            'Owner': 'string',
            'Protocol': 'string',
            'Endpoint': 'string',
            'TopicArn': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --Response for ListSubscriptions action

Subscriptions (list) --A list of subscriptions.

(dict) --A wrapper type for the attributes of an Amazon SNS subscription.

SubscriptionArn (string) --The subscription\'s ARN.

Owner (string) --The subscription\'s owner.

Protocol (string) --The subscription\'s protocol.

Endpoint (string) --The subscription\'s endpoint (format depends on the protocol).

TopicArn (string) --The ARN of the subscription\'s topic.





NextToken (string) --Token to pass along to the next ListSubscriptions request. This element is returned if there are more subscriptions to retrieve.






Exceptions

SNS.Client.exceptions.InvalidParameterException
SNS.Client.exceptions.InternalErrorException
SNS.Client.exceptions.AuthorizationErrorException


    :return: {
        'Subscriptions': [
            {
                'SubscriptionArn': 'string',
                'Owner': 'string',
                'Protocol': 'string',
                'Endpoint': 'string',
                'TopicArn': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_subscriptions_by_topic(TopicArn=None, NextToken=None):
    """
    Returns a list of the subscriptions to a specific topic. Each call returns a limited list of subscriptions, up to 100. If there are more subscriptions, a NextToken is also returned. Use the NextToken parameter in a new ListSubscriptionsByTopic call to get further results.
    This action is throttled at 30 transactions per second (TPS).
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_subscriptions_by_topic(
        TopicArn='string',
        NextToken='string'
    )
    
    
    :type TopicArn: string
    :param TopicArn: [REQUIRED]\nThe ARN of the topic for which you wish to find subscriptions.\n

    :type NextToken: string
    :param NextToken: Token returned by the previous ListSubscriptionsByTopic request.

    :rtype: dict

ReturnsResponse Syntax
{
    'Subscriptions': [
        {
            'SubscriptionArn': 'string',
            'Owner': 'string',
            'Protocol': 'string',
            'Endpoint': 'string',
            'TopicArn': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
Response for ListSubscriptionsByTopic action.

Subscriptions (list) --
A list of subscriptions.

(dict) --
A wrapper type for the attributes of an Amazon SNS subscription.

SubscriptionArn (string) --
The subscription\'s ARN.

Owner (string) --
The subscription\'s owner.

Protocol (string) --
The subscription\'s protocol.

Endpoint (string) --
The subscription\'s endpoint (format depends on the protocol).

TopicArn (string) --
The ARN of the subscription\'s topic.





NextToken (string) --
Token to pass along to the next ListSubscriptionsByTopic request. This element is returned if there are more subscriptions to retrieve.







Exceptions

SNS.Client.exceptions.InvalidParameterException
SNS.Client.exceptions.InternalErrorException
SNS.Client.exceptions.NotFoundException
SNS.Client.exceptions.AuthorizationErrorException


    :return: {
        'Subscriptions': [
            {
                'SubscriptionArn': 'string',
                'Owner': 'string',
                'Protocol': 'string',
                'Endpoint': 'string',
                'TopicArn': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    SNS.Client.exceptions.InvalidParameterException
    SNS.Client.exceptions.InternalErrorException
    SNS.Client.exceptions.NotFoundException
    SNS.Client.exceptions.AuthorizationErrorException
    
    """
    pass

def list_tags_for_resource(ResourceArn=None):
    """
    List all tags added to the specified Amazon SNS topic. For an overview, see Amazon SNS Tags in the Amazon Simple Notification Service Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        ResourceArn='string'
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe ARN of the topic for which to list tags.\n

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
Tags (list) --The tags associated with the specified topic.

(dict) --The list of tags to be added to the specified topic.

Key (string) --The required key portion of the tag.

Value (string) --The optional value portion of the tag.










Exceptions

SNS.Client.exceptions.ResourceNotFoundException
SNS.Client.exceptions.TagPolicyException
SNS.Client.exceptions.InvalidParameterException
SNS.Client.exceptions.AuthorizationErrorException
SNS.Client.exceptions.ConcurrentAccessException


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

def list_topics(NextToken=None):
    """
    Returns a list of the requester\'s topics. Each call returns a limited list of topics, up to 100. If there are more topics, a NextToken is also returned. Use the NextToken parameter in a new ListTopics call to get further results.
    This action is throttled at 30 transactions per second (TPS).
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_topics(
        NextToken='string'
    )
    
    
    :type NextToken: string
    :param NextToken: Token returned by the previous ListTopics request.

    :rtype: dict
ReturnsResponse Syntax{
    'Topics': [
        {
            'TopicArn': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --Response for ListTopics action.

Topics (list) --A list of topic ARNs.

(dict) --A wrapper type for the topic\'s Amazon Resource Name (ARN). To retrieve a topic\'s attributes, use GetTopicAttributes .

TopicArn (string) --The topic\'s ARN.





NextToken (string) --Token to pass along to the next ListTopics request. This element is returned if there are additional topics to retrieve.






Exceptions

SNS.Client.exceptions.InvalidParameterException
SNS.Client.exceptions.InternalErrorException
SNS.Client.exceptions.AuthorizationErrorException


    :return: {
        'Topics': [
            {
                'TopicArn': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def opt_in_phone_number(phoneNumber=None):
    """
    Use this request to opt in a phone number that is opted out, which enables you to resume sending SMS messages to the number.
    You can opt in a phone number only once every 30 days.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.opt_in_phone_number(
        phoneNumber='string'
    )
    
    
    :type phoneNumber: string
    :param phoneNumber: [REQUIRED]\nThe phone number to opt in.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --The response for the OptInPhoneNumber action.




Exceptions

SNS.Client.exceptions.ThrottledException
SNS.Client.exceptions.InternalErrorException
SNS.Client.exceptions.AuthorizationErrorException
SNS.Client.exceptions.InvalidParameterException


    :return: {}
    
    
    """
    pass

def publish(TopicArn=None, TargetArn=None, PhoneNumber=None, Message=None, Subject=None, MessageStructure=None, MessageAttributes=None):
    """
    Sends a message to an Amazon SNS topic or sends a text message (SMS message) directly to a phone number.
    If you send a message to a topic, Amazon SNS delivers the message to each endpoint that is subscribed to the topic. The format of the message depends on the notification protocol for each subscribed endpoint.
    When a messageId is returned, the message has been saved and Amazon SNS will attempt to deliver it shortly.
    To use the Publish action for sending a message to a mobile endpoint, such as an app on a Kindle device or mobile phone, you must specify the EndpointArn for the TargetArn parameter. The EndpointArn is returned when making a call with the CreatePlatformEndpoint action.
    For more information about formatting messages, see Send Custom Platform-Specific Payloads in Messages to Mobile Devices .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.publish(
        TopicArn='string',
        TargetArn='string',
        PhoneNumber='string',
        Message='string',
        Subject='string',
        MessageStructure='string',
        MessageAttributes={
            'string': {
                'DataType': 'string',
                'StringValue': 'string',
                'BinaryValue': b'bytes'
            }
        }
    )
    
    
    :type TopicArn: string
    :param TopicArn: The topic you want to publish to.\nIf you don\'t specify a value for the TopicArn parameter, you must specify a value for the PhoneNumber or TargetArn parameters.\n

    :type TargetArn: string
    :param TargetArn: If you don\'t specify a value for the TargetArn parameter, you must specify a value for the PhoneNumber or TopicArn parameters.

    :type PhoneNumber: string
    :param PhoneNumber: The phone number to which you want to deliver an SMS message. Use E.164 format.\nIf you don\'t specify a value for the PhoneNumber parameter, you must specify a value for the TargetArn or TopicArn parameters.\n

    :type Message: string
    :param Message: [REQUIRED]\nThe message you want to send.\nIf you are publishing to a topic and you want to send the same message to all transport protocols, include the text of the message as a String value. If you want to send different messages for each transport protocol, set the value of the MessageStructure parameter to json and use a JSON object for the Message parameter.\nConstraints:\n\nWith the exception of SMS, messages must be UTF-8 encoded strings and at most 256 KB in size (262,144 bytes, not 262,144 characters).\nFor SMS, each message can contain up to 140 characters. This character limit depends on the encoding schema. For example, an SMS message can contain 160 GSM characters, 140 ASCII characters, or 70 UCS-2 characters. If you publish a message that exceeds this size limit, Amazon SNS sends the message as multiple messages, each fitting within the size limit. Messages aren\'t truncated mid-word but are cut off at whole-word boundaries. The total size limit for a single SMS Publish action is 1,600 characters.\n\nJSON-specific constraints:\n\nKeys in the JSON object that correspond to supported transport protocols must have simple JSON string values.\nThe values will be parsed (unescaped) before they are used in outgoing messages.\nOutbound notifications are JSON encoded (meaning that the characters will be reescaped for sending).\nValues have a minimum length of 0 (the empty string, '', is allowed).\nValues have a maximum length bounded by the overall message size (so, including multiple protocols may limit message sizes).\nNon-string values will cause the key to be ignored.\nKeys that do not correspond to supported transport protocols are ignored.\nDuplicate keys are not allowed.\nFailure to parse or validate any key or value in the message will cause the Publish call to return an error (no partial delivery).\n\n

    :type Subject: string
    :param Subject: Optional parameter to be used as the 'Subject' line when the message is delivered to email endpoints. This field will also be included, if present, in the standard JSON messages delivered to other endpoints.\nConstraints: Subjects must be ASCII text that begins with a letter, number, or punctuation mark; must not include line breaks or control characters; and must be less than 100 characters long.\n

    :type MessageStructure: string
    :param MessageStructure: Set MessageStructure to json if you want to send a different message for each protocol. For example, using one publish action, you can send a short message to your SMS subscribers and a longer message to your email subscribers. If you set MessageStructure to json , the value of the Message parameter must:\n\nbe a syntactically valid JSON object; and\ncontain at least a top-level JSON key of 'default' with a value that is a string.\n\nYou can define other top-level keys that define the message you want to send to a specific transport protocol (e.g., 'http').\nValid value: json\n

    :type MessageAttributes: dict
    :param MessageAttributes: Message attributes for Publish action.\n\n(string) --\n(dict) --The user-specified message attribute value. For string data types, the value attribute has the same restrictions on the content as the message body. For more information, see Publish .\nName, type, and value must not be empty or null. In addition, the message body should not be empty or null. All parts of the message attribute, including name, type, and value, are included in the message size restriction, which is currently 256 KB (262,144 bytes). For more information, see Using Amazon SNS Message Attributes .\n\nDataType (string) -- [REQUIRED]Amazon SNS supports the following logical data types: String, String.Array, Number, and Binary. For more information, see Message Attribute Data Types .\n\nStringValue (string) --Strings are Unicode with UTF8 binary encoding. For a list of code values, see ASCII Printable Characters .\n\nBinaryValue (bytes) --Binary type attributes can store any binary data, for example, compressed data, encrypted data, or images.\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'MessageId': 'string'
}


Response Structure

(dict) --
Response for Publish action.

MessageId (string) --
Unique identifier assigned to the published message.
Length Constraint: Maximum 100 characters







Exceptions

SNS.Client.exceptions.InvalidParameterException
SNS.Client.exceptions.InvalidParameterValueException
SNS.Client.exceptions.InternalErrorException
SNS.Client.exceptions.NotFoundException
SNS.Client.exceptions.EndpointDisabledException
SNS.Client.exceptions.PlatformApplicationDisabledException
SNS.Client.exceptions.AuthorizationErrorException
SNS.Client.exceptions.KMSDisabledException
SNS.Client.exceptions.KMSInvalidStateException
SNS.Client.exceptions.KMSNotFoundException
SNS.Client.exceptions.KMSOptInRequired
SNS.Client.exceptions.KMSThrottlingException
SNS.Client.exceptions.KMSAccessDeniedException
SNS.Client.exceptions.InvalidSecurityException


    :return: {
        'MessageId': 'string'
    }
    
    
    :returns: 
    SNS.Client.exceptions.InvalidParameterException
    SNS.Client.exceptions.InvalidParameterValueException
    SNS.Client.exceptions.InternalErrorException
    SNS.Client.exceptions.NotFoundException
    SNS.Client.exceptions.EndpointDisabledException
    SNS.Client.exceptions.PlatformApplicationDisabledException
    SNS.Client.exceptions.AuthorizationErrorException
    SNS.Client.exceptions.KMSDisabledException
    SNS.Client.exceptions.KMSInvalidStateException
    SNS.Client.exceptions.KMSNotFoundException
    SNS.Client.exceptions.KMSOptInRequired
    SNS.Client.exceptions.KMSThrottlingException
    SNS.Client.exceptions.KMSAccessDeniedException
    SNS.Client.exceptions.InvalidSecurityException
    
    """
    pass

def remove_permission(TopicArn=None, Label=None):
    """
    Removes a statement from a topic\'s access control policy.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.remove_permission(
        TopicArn='string',
        Label='string'
    )
    
    
    :type TopicArn: string
    :param TopicArn: [REQUIRED]\nThe ARN of the topic whose access control policy you wish to modify.\n

    :type Label: string
    :param Label: [REQUIRED]\nThe unique label of the statement you want to remove.\n

    :returns: 
    SNS.Client.exceptions.InvalidParameterException
    SNS.Client.exceptions.InternalErrorException
    SNS.Client.exceptions.AuthorizationErrorException
    SNS.Client.exceptions.NotFoundException
    
    """
    pass

def set_endpoint_attributes(EndpointArn=None, Attributes=None):
    """
    Sets the attributes for an endpoint for a device on one of the supported push notification services, such as FCM and APNS. For more information, see Using Amazon SNS Mobile Push Notifications .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.set_endpoint_attributes(
        EndpointArn='string',
        Attributes={
            'string': 'string'
        }
    )
    
    
    :type EndpointArn: string
    :param EndpointArn: [REQUIRED]\nEndpointArn used for SetEndpointAttributes action.\n

    :type Attributes: dict
    :param Attributes: [REQUIRED]\nA map of the endpoint attributes. Attributes in this map include the following:\n\nCustomUserData \xe2\x80\x93 arbitrary user data to associate with the endpoint. Amazon SNS does not use this data. The data must be in UTF-8 format and less than 2KB.\nEnabled \xe2\x80\x93 flag that enables/disables delivery to the endpoint. Amazon SNS will set this to false when a notification service indicates to Amazon SNS that the endpoint is invalid. Users can set it back to true, typically after updating Token.\nToken \xe2\x80\x93 device token, also referred to as a registration id, for an app and mobile device. This is returned from the notification service when an app and mobile device are registered with the notification service.\n\n\n(string) --\n(string) --\n\n\n\n

    :returns: 
    SNS.Client.exceptions.InvalidParameterException
    SNS.Client.exceptions.InternalErrorException
    SNS.Client.exceptions.AuthorizationErrorException
    SNS.Client.exceptions.NotFoundException
    
    """
    pass

def set_platform_application_attributes(PlatformApplicationArn=None, Attributes=None):
    """
    Sets the attributes of the platform application object for the supported push notification services, such as APNS and FCM. For more information, see Using Amazon SNS Mobile Push Notifications . For information on configuring attributes for message delivery status, see Using Amazon SNS Application Attributes for Message Delivery Status .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.set_platform_application_attributes(
        PlatformApplicationArn='string',
        Attributes={
            'string': 'string'
        }
    )
    
    
    :type PlatformApplicationArn: string
    :param PlatformApplicationArn: [REQUIRED]\nPlatformApplicationArn for SetPlatformApplicationAttributes action.\n

    :type Attributes: dict
    :param Attributes: [REQUIRED]\nA map of the platform application attributes. Attributes in this map include the following:\n\nPlatformCredential \xe2\x80\x93 The credential received from the notification service. For APNS/APNS_SANDBOX, PlatformCredential is private key. For FCM, PlatformCredential is 'API key'. For ADM, PlatformCredential is 'client secret'.\nPlatformPrincipal \xe2\x80\x93 The principal received from the notification service. For APNS/APNS_SANDBOX, PlatformPrincipal is SSL certificate. For FCM, PlatformPrincipal is not applicable. For ADM, PlatformPrincipal is 'client id'.\nEventEndpointCreated \xe2\x80\x93 Topic ARN to which EndpointCreated event notifications should be sent.\nEventEndpointDeleted \xe2\x80\x93 Topic ARN to which EndpointDeleted event notifications should be sent.\nEventEndpointUpdated \xe2\x80\x93 Topic ARN to which EndpointUpdate event notifications should be sent.\nEventDeliveryFailure \xe2\x80\x93 Topic ARN to which DeliveryFailure event notifications should be sent upon Direct Publish delivery failure (permanent) to one of the application\'s endpoints.\nSuccessFeedbackRoleArn \xe2\x80\x93 IAM role ARN used to give Amazon SNS write access to use CloudWatch Logs on your behalf.\nFailureFeedbackRoleArn \xe2\x80\x93 IAM role ARN used to give Amazon SNS write access to use CloudWatch Logs on your behalf.\nSuccessFeedbackSampleRate \xe2\x80\x93 Sample rate percentage (0-100) of successfully delivered messages.\n\n\n(string) --\n(string) --\n\n\n\n

    :returns: 
    SNS.Client.exceptions.InvalidParameterException
    SNS.Client.exceptions.InternalErrorException
    SNS.Client.exceptions.AuthorizationErrorException
    SNS.Client.exceptions.NotFoundException
    
    """
    pass

def set_sms_attributes(attributes=None):
    """
    Use this request to set the default settings for sending SMS messages and receiving daily SMS usage reports.
    You can override some of these settings for a single message when you use the Publish action with the MessageAttributes.entry.N parameter. For more information, see Sending an SMS Message in the Amazon SNS Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.set_sms_attributes(
        attributes={
            'string': 'string'
        }
    )
    
    
    :type attributes: dict
    :param attributes: [REQUIRED]\nThe default settings for sending SMS messages from your account. You can set values for the following attribute names:\n\nMonthlySpendLimit \xe2\x80\x93 The maximum amount in USD that you are willing to spend each month to send SMS messages. When Amazon SNS determines that sending an SMS message would incur a cost that exceeds this limit, it stops sending SMS messages within minutes.\n\nWarning\nAmazon SNS stops sending SMS messages within minutes of the limit being crossed. During that interval, if you continue to send SMS messages, you will incur costs that exceed your limit.\n\nBy default, the spend limit is set to the maximum allowed by Amazon SNS. If you want to raise the limit, submit an SNS Limit Increase case . For New limit value , enter your desired monthly spend limit. In the Use Case Description field, explain that you are requesting an SMS monthly spend limit increase.\n\nDeliveryStatusIAMRole \xe2\x80\x93 The ARN of the IAM role that allows Amazon SNS to write logs about SMS deliveries in CloudWatch Logs. For each SMS message that you send, Amazon SNS writes a log that includes the message price, the success or failure status, the reason for failure (if the message failed), the message dwell time, and other information.DeliveryStatusSuccessSamplingRate \xe2\x80\x93 The percentage of successful SMS deliveries for which Amazon SNS will write logs in CloudWatch Logs. The value can be an integer from 0 - 100. For example, to write logs only for failed deliveries, set this value to 0 . To write logs for 10% of your successful deliveries, set it to 10 .\nDefaultSenderID \xe2\x80\x93 A string, such as your business brand, that is displayed as the sender on the receiving device. Support for sender IDs varies by country. The sender ID can be 1 - 11 alphanumeric characters, and it must contain at least one letter.\nDefaultSMSType \xe2\x80\x93 The type of SMS message that you will send by default. You can assign the following values:\n\n\nPromotional \xe2\x80\x93 (Default) Noncritical messages, such as marketing messages. Amazon SNS optimizes the message delivery to incur the lowest cost.\nTransactional \xe2\x80\x93 Critical messages that support customer transactions, such as one-time passcodes for multi-factor authentication. Amazon SNS optimizes the message delivery to achieve the highest reliability.\n\n\nUsageReportS3Bucket \xe2\x80\x93 The name of the Amazon S3 bucket to receive daily SMS usage reports from Amazon SNS. Each day, Amazon SNS will deliver a usage report as a CSV file to the bucket. The report includes the following information for each SMS message that was successfully delivered by your account:\n\nTime that the message was published (in UTC)\nMessage ID\nDestination phone number\nMessage type\nDelivery status\nMessage price (in USD)\nPart number (a message is split into multiple parts if it is too long for a single message)\nTotal number of parts\n\nTo receive the report, the bucket must have a policy that allows the Amazon SNS service principle to perform the s3:PutObject and s3:GetBucketLocation actions.\nFor an example bucket policy and usage report, see Monitoring SMS Activity in the Amazon SNS Developer Guide .\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --The response for the SetSMSAttributes action.




Exceptions

SNS.Client.exceptions.InvalidParameterException
SNS.Client.exceptions.ThrottledException
SNS.Client.exceptions.InternalErrorException
SNS.Client.exceptions.AuthorizationErrorException


    :return: {}
    
    
    :returns: 
    Time that the message was published (in UTC)
    Message ID
    Destination phone number
    Message type
    Delivery status
    Message price (in USD)
    Part number (a message is split into multiple parts if it is too long for a single message)
    Total number of parts
    
    """
    pass

def set_subscription_attributes(SubscriptionArn=None, AttributeName=None, AttributeValue=None):
    """
    Allows a subscription owner to set an attribute of the subscription to a new value.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.set_subscription_attributes(
        SubscriptionArn='string',
        AttributeName='string',
        AttributeValue='string'
    )
    
    
    :type SubscriptionArn: string
    :param SubscriptionArn: [REQUIRED]\nThe ARN of the subscription to modify.\n

    :type AttributeName: string
    :param AttributeName: [REQUIRED]\nA map of attributes with their corresponding values.\nThe following lists the names, descriptions, and values of the special request parameters that the SetTopicAttributes action uses:\n\nDeliveryPolicy \xe2\x80\x93 The policy that defines how Amazon SNS retries failed deliveries to HTTP/S endpoints.\nFilterPolicy \xe2\x80\x93 The simple JSON object that lets your subscriber receive only a subset of messages, rather than receiving every message published to the topic.\nRawMessageDelivery \xe2\x80\x93 When set to true , enables raw message delivery to Amazon SQS or HTTP/S endpoints. This eliminates the need for the endpoints to process JSON formatting, which is otherwise created for Amazon SNS metadata.\nRedrivePolicy \xe2\x80\x93 When specified, sends undeliverable messages to the specified Amazon SQS dead-letter queue. Messages that can\'t be delivered due to client errors (for example, when the subscribed endpoint is unreachable) or server errors (for example, when the service that powers the subscribed endpoint becomes unavailable) are held in the dead-letter queue for further analysis or reprocessing.\n\n

    :type AttributeValue: string
    :param AttributeValue: The new value for the attribute in JSON format.

    :returns: 
    SNS.Client.exceptions.InvalidParameterException
    SNS.Client.exceptions.FilterPolicyLimitExceededException
    SNS.Client.exceptions.InternalErrorException
    SNS.Client.exceptions.NotFoundException
    SNS.Client.exceptions.AuthorizationErrorException
    
    """
    pass

def set_topic_attributes(TopicArn=None, AttributeName=None, AttributeValue=None):
    """
    Allows a topic owner to set an attribute of the topic to a new value.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.set_topic_attributes(
        TopicArn='string',
        AttributeName='string',
        AttributeValue='string'
    )
    
    
    :type TopicArn: string
    :param TopicArn: [REQUIRED]\nThe ARN of the topic to modify.\n

    :type AttributeName: string
    :param AttributeName: [REQUIRED]\nA map of attributes with their corresponding values.\nThe following lists the names, descriptions, and values of the special request parameters that the SetTopicAttributes action uses:\n\nDeliveryPolicy \xe2\x80\x93 The policy that defines how Amazon SNS retries failed deliveries to HTTP/S endpoints.\nDisplayName \xe2\x80\x93 The display name to use for a topic with SMS subscriptions.\nPolicy \xe2\x80\x93 The policy that defines who can access your topic. By default, only the topic owner can publish or subscribe to the topic.\n\nThe following attribute applies only to server-side-encryption :\n\nKmsMasterKeyId - The ID of an AWS-managed customer master key (CMK) for Amazon SNS or a custom CMK. For more information, see Key Terms . For more examples, see KeyId in the AWS Key Management Service API Reference .\n\n

    :type AttributeValue: string
    :param AttributeValue: The new value for the attribute.

    :returns: 
    SNS.Client.exceptions.InvalidParameterException
    SNS.Client.exceptions.InternalErrorException
    SNS.Client.exceptions.NotFoundException
    SNS.Client.exceptions.AuthorizationErrorException
    SNS.Client.exceptions.InvalidSecurityException
    
    """
    pass

def subscribe(TopicArn=None, Protocol=None, Endpoint=None, Attributes=None, ReturnSubscriptionArn=None):
    """
    Prepares to subscribe an endpoint by sending the endpoint a confirmation message. To actually create a subscription, the endpoint owner must call the ConfirmSubscription action with the token from the confirmation message. Confirmation tokens are valid for three days.
    This action is throttled at 100 transactions per second (TPS).
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.subscribe(
        TopicArn='string',
        Protocol='string',
        Endpoint='string',
        Attributes={
            'string': 'string'
        },
        ReturnSubscriptionArn=True|False
    )
    
    
    :type TopicArn: string
    :param TopicArn: [REQUIRED]\nThe ARN of the topic you want to subscribe to.\n

    :type Protocol: string
    :param Protocol: [REQUIRED]\nThe protocol you want to use. Supported protocols include:\n\nhttp \xe2\x80\x93 delivery of JSON-encoded message via HTTP POST\nhttps \xe2\x80\x93 delivery of JSON-encoded message via HTTPS POST\nemail \xe2\x80\x93 delivery of message via SMTP\nemail-json \xe2\x80\x93 delivery of JSON-encoded message via SMTP\nsms \xe2\x80\x93 delivery of message via SMS\nsqs \xe2\x80\x93 delivery of JSON-encoded message to an Amazon SQS queue\napplication \xe2\x80\x93 delivery of JSON-encoded message to an EndpointArn for a mobile app and device.\nlambda \xe2\x80\x93 delivery of JSON-encoded message to an Amazon Lambda function.\n\n

    :type Endpoint: string
    :param Endpoint: The endpoint that you want to receive notifications. Endpoints vary by protocol:\n\nFor the http protocol, the endpoint is an URL beginning with http://\nFor the https protocol, the endpoint is a URL beginning with https://\nFor the email protocol, the endpoint is an email address\nFor the email-json protocol, the endpoint is an email address\nFor the sms protocol, the endpoint is a phone number of an SMS-enabled device\nFor the sqs protocol, the endpoint is the ARN of an Amazon SQS queue\nFor the application protocol, the endpoint is the EndpointArn of a mobile app and device.\nFor the lambda protocol, the endpoint is the ARN of an Amazon Lambda function.\n\n

    :type Attributes: dict
    :param Attributes: A map of attributes with their corresponding values.\nThe following lists the names, descriptions, and values of the special request parameters that the SetTopicAttributes action uses:\n\nDeliveryPolicy \xe2\x80\x93 The policy that defines how Amazon SNS retries failed deliveries to HTTP/S endpoints.\nFilterPolicy \xe2\x80\x93 The simple JSON object that lets your subscriber receive only a subset of messages, rather than receiving every message published to the topic.\nRawMessageDelivery \xe2\x80\x93 When set to true , enables raw message delivery to Amazon SQS or HTTP/S endpoints. This eliminates the need for the endpoints to process JSON formatting, which is otherwise created for Amazon SNS metadata.\nRedrivePolicy \xe2\x80\x93 When specified, sends undeliverable messages to the specified Amazon SQS dead-letter queue. Messages that can\'t be delivered due to client errors (for example, when the subscribed endpoint is unreachable) or server errors (for example, when the service that powers the subscribed endpoint becomes unavailable) are held in the dead-letter queue for further analysis or reprocessing.\n\n\n(string) --\n(string) --\n\n\n\n

    :type ReturnSubscriptionArn: boolean
    :param ReturnSubscriptionArn: Sets whether the response from the Subscribe request includes the subscription ARN, even if the subscription is not yet confirmed.\n\nIf you have the subscription ARN returned, the response includes the ARN in all cases, even if the subscription is not yet confirmed.\nIf you don\'t have the subscription ARN returned, in addition to the ARN for confirmed subscriptions, the response also includes the pending subscription ARN value for subscriptions that aren\'t yet confirmed. A subscription becomes confirmed when the subscriber calls the ConfirmSubscription action with a confirmation token.\n\nIf you set this parameter to true , .\nThe default value is false .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'SubscriptionArn': 'string'
}


Response Structure

(dict) --
Response for Subscribe action.

SubscriptionArn (string) --
The ARN of the subscription if it is confirmed, or the string "pending confirmation" if the subscription requires confirmation. However, if the API request parameter ReturnSubscriptionArn is true, then the value is always the subscription ARN, even if the subscription requires confirmation.







Exceptions

SNS.Client.exceptions.SubscriptionLimitExceededException
SNS.Client.exceptions.FilterPolicyLimitExceededException
SNS.Client.exceptions.InvalidParameterException
SNS.Client.exceptions.InternalErrorException
SNS.Client.exceptions.NotFoundException
SNS.Client.exceptions.AuthorizationErrorException
SNS.Client.exceptions.InvalidSecurityException


    :return: {
        'SubscriptionArn': 'string'
    }
    
    
    :returns: 
    SNS.Client.exceptions.SubscriptionLimitExceededException
    SNS.Client.exceptions.FilterPolicyLimitExceededException
    SNS.Client.exceptions.InvalidParameterException
    SNS.Client.exceptions.InternalErrorException
    SNS.Client.exceptions.NotFoundException
    SNS.Client.exceptions.AuthorizationErrorException
    SNS.Client.exceptions.InvalidSecurityException
    
    """
    pass

def tag_resource(ResourceArn=None, Tags=None):
    """
    Add tags to the specified Amazon SNS topic. For an overview, see Amazon SNS Tags in the Amazon SNS Developer Guide .
    When you use topic tags, keep the following guidelines in mind:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        ResourceArn='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe ARN of the topic to which to add tags.\n

    :type Tags: list
    :param Tags: [REQUIRED]\nThe tags to be added to the specified topic. A tag consists of a required key and an optional value.\n\n(dict) --The list of tags to be added to the specified topic.\n\nKey (string) -- [REQUIRED]The required key portion of the tag.\n\nValue (string) -- [REQUIRED]The optional value portion of the tag.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

SNS.Client.exceptions.ResourceNotFoundException
SNS.Client.exceptions.TagLimitExceededException
SNS.Client.exceptions.StaleTagException
SNS.Client.exceptions.TagPolicyException
SNS.Client.exceptions.InvalidParameterException
SNS.Client.exceptions.AuthorizationErrorException
SNS.Client.exceptions.ConcurrentAccessException


    :return: {}
    
    
    :returns: 
    ResourceArn (string) -- [REQUIRED]
    The ARN of the topic to which to add tags.
    
    Tags (list) -- [REQUIRED]
    The tags to be added to the specified topic. A tag consists of a required key and an optional value.
    
    (dict) --The list of tags to be added to the specified topic.
    
    Key (string) -- [REQUIRED]The required key portion of the tag.
    
    Value (string) -- [REQUIRED]The optional value portion of the tag.
    
    
    
    
    
    
    """
    pass

def unsubscribe(SubscriptionArn=None):
    """
    Deletes a subscription. If the subscription requires authentication for deletion, only the owner of the subscription or the topic\'s owner can unsubscribe, and an AWS signature is required. If the Unsubscribe call does not require authentication and the requester is not the subscription owner, a final cancellation message is delivered to the endpoint, so that the endpoint owner can easily resubscribe to the topic if the Unsubscribe request was unintended.
    This action is throttled at 100 transactions per second (TPS).
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.unsubscribe(
        SubscriptionArn='string'
    )
    
    
    :type SubscriptionArn: string
    :param SubscriptionArn: [REQUIRED]\nThe ARN of the subscription to be deleted.\n

    """
    pass

def untag_resource(ResourceArn=None, TagKeys=None):
    """
    Remove tags from the specified Amazon SNS topic. For an overview, see Amazon SNS Tags in the Amazon SNS Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        ResourceArn='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe ARN of the topic from which to remove tags.\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nThe list of tag keys to remove from the specified topic.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

SNS.Client.exceptions.ResourceNotFoundException
SNS.Client.exceptions.TagLimitExceededException
SNS.Client.exceptions.StaleTagException
SNS.Client.exceptions.TagPolicyException
SNS.Client.exceptions.InvalidParameterException
SNS.Client.exceptions.AuthorizationErrorException
SNS.Client.exceptions.ConcurrentAccessException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

