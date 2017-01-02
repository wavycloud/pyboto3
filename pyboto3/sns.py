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
    Adds a statement to a topic's access control policy, granting access for the specified AWS accounts to the specified actions.
    See also: AWS API Documentation
    
    
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
    :param TopicArn: [REQUIRED]
            The ARN of the topic whose access control policy you wish to modify.
            

    :type Label: string
    :param Label: [REQUIRED]
            A unique identifier for the new policy statement.
            

    :type AWSAccountId: list
    :param AWSAccountId: [REQUIRED]
            The AWS account IDs of the users (principals) who will be given access to the specified actions. The users must have AWS accounts, but do not need to be signed up for this service.
            (string) --
            

    :type ActionName: list
    :param ActionName: [REQUIRED]
            The action you want to allow for the specified principal(s).
            Valid values: any Amazon SNS action name.
            (string) --
            

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

def check_if_phone_number_is_opted_out(phoneNumber=None):
    """
    Accepts a phone number and indicates whether the phone holder has opted out of receiving SMS messages from your account. You cannot send SMS messages to a number that is opted out.
    To resume sending messages, you can opt in the number by using the OptInPhoneNumber action.
    See also: AWS API Documentation
    
    
    :example: response = client.check_if_phone_number_is_opted_out(
        phoneNumber='string'
    )
    
    
    :type phoneNumber: string
    :param phoneNumber: [REQUIRED]
            The phone number for which you want to check the opt out status.
            

    :rtype: dict
    :return: {
        'isOptedOut': True|False
    }
    
    
    """
    pass

def confirm_subscription(TopicArn=None, Token=None, AuthenticateOnUnsubscribe=None):
    """
    Verifies an endpoint owner's intent to receive messages by validating the token sent to the endpoint by an earlier Subscribe action. If the token is valid, the action creates a new subscription and returns its Amazon Resource Name (ARN). This call requires an AWS signature only when the AuthenticateOnUnsubscribe flag is set to "true".
    See also: AWS API Documentation
    
    
    :example: response = client.confirm_subscription(
        TopicArn='string',
        Token='string',
        AuthenticateOnUnsubscribe='string'
    )
    
    
    :type TopicArn: string
    :param TopicArn: [REQUIRED]
            The ARN of the topic for which you wish to confirm a subscription.
            

    :type Token: string
    :param Token: [REQUIRED]
            Short-lived token sent to an endpoint during the Subscribe action.
            

    :type AuthenticateOnUnsubscribe: string
    :param AuthenticateOnUnsubscribe: Disallows unauthenticated unsubscribes of the subscription. If the value of this parameter is true and the request has an AWS signature, then only the topic owner and the subscription owner can unsubscribe the endpoint. The unsubscribe action requires AWS authentication.

    :rtype: dict
    :return: {
        'SubscriptionArn': 'string'
    }
    
    
    """
    pass

def create_platform_application(Name=None, Platform=None, Attributes=None):
    """
    Creates a platform application object for one of the supported push notification services, such as APNS and GCM, to which devices and mobile apps may register. You must specify PlatformPrincipal and PlatformCredential attributes when using the CreatePlatformApplication action. The PlatformPrincipal is received from the notification service. For APNS/APNS_SANDBOX, PlatformPrincipal is "SSL certificate". For GCM, PlatformPrincipal is not applicable. For ADM, PlatformPrincipal is "client id". The PlatformCredential is also received from the notification service. For WNS, PlatformPrincipal is "Package Security Identifier". For MPNS, PlatformPrincipal is "TLS certificate". For Baidu, PlatformPrincipal is "API key".
    For APNS/APNS_SANDBOX, PlatformCredential is "private key". For GCM, PlatformCredential is "API key". For ADM, PlatformCredential is "client secret". For WNS, PlatformCredential is "secret key". For MPNS, PlatformCredential is "private key". For Baidu, PlatformCredential is "secret key". The PlatformApplicationArn that is returned when using CreatePlatformApplication is then used as an attribute for the CreatePlatformEndpoint action. For more information, see Using Amazon SNS Mobile Push Notifications . For more information about obtaining the PlatformPrincipal and PlatformCredential for each of the supported push notification services, see Getting Started with Apple Push Notification Service , Getting Started with Amazon Device Messaging , Getting Started with Baidu Cloud Push , Getting Started with Google Cloud Messaging for Android , Getting Started with MPNS , or Getting Started with WNS .
    See also: AWS API Documentation
    
    
    :example: response = client.create_platform_application(
        Name='string',
        Platform='string',
        Attributes={
            'string': 'string'
        }
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            Application names must be made up of only uppercase and lowercase ASCII letters, numbers, underscores, hyphens, and periods, and must be between 1 and 256 characters long.
            

    :type Platform: string
    :param Platform: [REQUIRED]
            The following platforms are supported: ADM (Amazon Device Messaging), APNS (Apple Push Notification Service), APNS_SANDBOX, and GCM (Google Cloud Messaging).
            

    :type Attributes: dict
    :param Attributes: [REQUIRED]
            For a list of attributes, see SetPlatformApplicationAttributes
            (string) --
            (string) --
            

    :rtype: dict
    :return: {
        'PlatformApplicationArn': 'string'
    }
    
    
    """
    pass

def create_platform_endpoint(PlatformApplicationArn=None, Token=None, CustomUserData=None, Attributes=None):
    """
    Creates an endpoint for a device and mobile app on one of the supported push notification services, such as GCM and APNS. CreatePlatformEndpoint requires the PlatformApplicationArn that is returned from CreatePlatformApplication . The EndpointArn that is returned when using CreatePlatformEndpoint can then be used by the Publish action to send a message to a mobile app or by the Subscribe action for subscription to a topic. The CreatePlatformEndpoint action is idempotent, so if the requester already owns an endpoint with the same device token and attributes, that endpoint's ARN is returned without creating a new endpoint. For more information, see Using Amazon SNS Mobile Push Notifications .
    When using CreatePlatformEndpoint with Baidu, two attributes must be provided: ChannelId and UserId. The token field must also contain the ChannelId. For more information, see Creating an Amazon SNS Endpoint for Baidu .
    See also: AWS API Documentation
    
    
    :example: response = client.create_platform_endpoint(
        PlatformApplicationArn='string',
        Token='string',
        CustomUserData='string',
        Attributes={
            'string': 'string'
        }
    )
    
    
    :type PlatformApplicationArn: string
    :param PlatformApplicationArn: [REQUIRED]
            PlatformApplicationArn returned from CreatePlatformApplication is used to create a an endpoint.
            

    :type Token: string
    :param Token: [REQUIRED]
            Unique identifier created by the notification service for an app on a device. The specific name for Token will vary, depending on which notification service is being used. For example, when using APNS as the notification service, you need the device token. Alternatively, when using GCM or ADM, the device token equivalent is called the registration ID.
            

    :type CustomUserData: string
    :param CustomUserData: Arbitrary user data to associate with the endpoint. Amazon SNS does not use this data. The data must be in UTF-8 format and less than 2KB.

    :type Attributes: dict
    :param Attributes: For a list of attributes, see SetEndpointAttributes .
            (string) --
            (string) --
            

    :rtype: dict
    :return: {
        'EndpointArn': 'string'
    }
    
    
    """
    pass

def create_topic(Name=None):
    """
    Creates a topic to which notifications can be published. Users can create at most 100,000 topics. For more information, see http://aws.amazon.com/sns . This action is idempotent, so if the requester already owns a topic with the specified name, that topic's ARN is returned without creating a new topic.
    See also: AWS API Documentation
    
    
    :example: response = client.create_topic(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the topic you want to create.
            Constraints: Topic names must be made up of only uppercase and lowercase ASCII letters, numbers, underscores, and hyphens, and must be between 1 and 256 characters long.
            

    :rtype: dict
    :return: {
        'TopicArn': 'string'
    }
    
    
    """
    pass

def delete_endpoint(EndpointArn=None):
    """
    Deletes the endpoint for a device and mobile app from Amazon SNS. This action is idempotent. For more information, see Using Amazon SNS Mobile Push Notifications .
    When you delete an endpoint that is also subscribed to a topic, then you must also unsubscribe the endpoint from the topic.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_endpoint(
        EndpointArn='string'
    )
    
    
    :type EndpointArn: string
    :param EndpointArn: [REQUIRED]
            EndpointArn of endpoint to delete.
            

    """
    pass

def delete_platform_application(PlatformApplicationArn=None):
    """
    Deletes a platform application object for one of the supported push notification services, such as APNS and GCM. For more information, see Using Amazon SNS Mobile Push Notifications .
    See also: AWS API Documentation
    
    
    :example: response = client.delete_platform_application(
        PlatformApplicationArn='string'
    )
    
    
    :type PlatformApplicationArn: string
    :param PlatformApplicationArn: [REQUIRED]
            PlatformApplicationArn of platform application object to delete.
            

    """
    pass

def delete_topic(TopicArn=None):
    """
    Deletes a topic and all its subscriptions. Deleting a topic might prevent some messages previously sent to the topic from being delivered to subscribers. This action is idempotent, so deleting a topic that does not exist does not result in an error.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_topic(
        TopicArn='string'
    )
    
    
    :type TopicArn: string
    :param TopicArn: [REQUIRED]
            The ARN of the topic you want to delete.
            

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

def get_endpoint_attributes(EndpointArn=None):
    """
    Retrieves the endpoint attributes for a device on one of the supported push notification services, such as GCM and APNS. For more information, see Using Amazon SNS Mobile Push Notifications .
    See also: AWS API Documentation
    
    
    :example: response = client.get_endpoint_attributes(
        EndpointArn='string'
    )
    
    
    :type EndpointArn: string
    :param EndpointArn: [REQUIRED]
            EndpointArn for GetEndpointAttributes input.
            

    :rtype: dict
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
    :param operation_name: The operation name. This is the same name
            as the method name on the client. For example, if the
            method name is create_foo, and you'd normally invoke the
            operation as client.create_foo(**kwargs), if the
            create_foo operation can be paginated, you can use the
            call client.get_paginator('create_foo').

    :rtype: L{botocore.paginate.Paginator}
    """
    pass

def get_platform_application_attributes(PlatformApplicationArn=None):
    """
    Retrieves the attributes of the platform application object for the supported push notification services, such as APNS and GCM. For more information, see Using Amazon SNS Mobile Push Notifications .
    See also: AWS API Documentation
    
    
    :example: response = client.get_platform_application_attributes(
        PlatformApplicationArn='string'
    )
    
    
    :type PlatformApplicationArn: string
    :param PlatformApplicationArn: [REQUIRED]
            PlatformApplicationArn for GetPlatformApplicationAttributesInput.
            

    :rtype: dict
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
    
    
    :example: response = client.get_sms_attributes(
        attributes=[
            'string',
        ]
    )
    
    
    :type attributes: list
    :param attributes: A list of the individual attribute names, such as MonthlySpendLimit , for which you want values.
            For all attribute names, see SetSMSAttributes .
            If you don't use this parameter, Amazon SNS returns all SMS attributes.
            (string) --
            

    :rtype: dict
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
    
    
    :example: response = client.get_subscription_attributes(
        SubscriptionArn='string'
    )
    
    
    :type SubscriptionArn: string
    :param SubscriptionArn: [REQUIRED]
            The ARN of the subscription whose properties you want to get.
            

    :rtype: dict
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
    
    
    :example: response = client.get_topic_attributes(
        TopicArn='string'
    )
    
    
    :type TopicArn: string
    :param TopicArn: [REQUIRED]
            The ARN of the topic whose properties you want to get.
            

    :rtype: dict
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

def get_waiter():
    """
    
    """
    pass

def list_endpoints_by_platform_application(PlatformApplicationArn=None, NextToken=None):
    """
    Lists the endpoints and endpoint attributes for devices in a supported push notification service, such as GCM and APNS. The results for ListEndpointsByPlatformApplication are paginated and return a limited list of endpoints, up to 100. If additional records are available after the first page results, then a NextToken string will be returned. To receive the next page, you call ListEndpointsByPlatformApplication again using the NextToken string received from the previous call. When there are no more records to return, NextToken will be null. For more information, see Using Amazon SNS Mobile Push Notifications .
    See also: AWS API Documentation
    
    
    :example: response = client.list_endpoints_by_platform_application(
        PlatformApplicationArn='string',
        NextToken='string'
    )
    
    
    :type PlatformApplicationArn: string
    :param PlatformApplicationArn: [REQUIRED]
            PlatformApplicationArn for ListEndpointsByPlatformApplicationInput action.
            

    :type NextToken: string
    :param NextToken: NextToken string is used when calling ListEndpointsByPlatformApplication action to retrieve additional records that are available after the first page results.

    :rtype: dict
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
    
    
    :example: response = client.list_phone_numbers_opted_out(
        nextToken='string'
    )
    
    
    :type nextToken: string
    :param nextToken: A NextToken string is used when you call the ListPhoneNumbersOptedOut action to retrieve additional records that are available after the first page of results.

    :rtype: dict
    :return: {
        'phoneNumbers': [
            'string',
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def list_platform_applications(NextToken=None):
    """
    Lists the platform application objects for the supported push notification services, such as APNS and GCM. The results for ListPlatformApplications are paginated and return a limited list of applications, up to 100. If additional records are available after the first page results, then a NextToken string will be returned. To receive the next page, you call ListPlatformApplications using the NextToken string received from the previous call. When there are no more records to return, NextToken will be null. For more information, see Using Amazon SNS Mobile Push Notifications .
    See also: AWS API Documentation
    
    
    :example: response = client.list_platform_applications(
        NextToken='string'
    )
    
    
    :type NextToken: string
    :param NextToken: NextToken string is used when calling ListPlatformApplications action to retrieve additional records that are available after the first page results.

    :rtype: dict
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
    
    
    """
    pass

def list_subscriptions(NextToken=None):
    """
    Returns a list of the requester's subscriptions. Each call returns a limited list of subscriptions, up to 100. If there are more subscriptions, a NextToken is also returned. Use the NextToken parameter in a new ListSubscriptions call to get further results.
    See also: AWS API Documentation
    
    
    :example: response = client.list_subscriptions(
        NextToken='string'
    )
    
    
    :type NextToken: string
    :param NextToken: Token returned by the previous ListSubscriptions request.

    :rtype: dict
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
    See also: AWS API Documentation
    
    
    :example: response = client.list_subscriptions_by_topic(
        TopicArn='string',
        NextToken='string'
    )
    
    
    :type TopicArn: string
    :param TopicArn: [REQUIRED]
            The ARN of the topic for which you wish to find subscriptions.
            

    :type NextToken: string
    :param NextToken: Token returned by the previous ListSubscriptionsByTopic request.

    :rtype: dict
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

def list_topics(NextToken=None):
    """
    Returns a list of the requester's topics. Each call returns a limited list of topics, up to 100. If there are more topics, a NextToken is also returned. Use the NextToken parameter in a new ListTopics call to get further results.
    See also: AWS API Documentation
    
    
    :example: response = client.list_topics(
        NextToken='string'
    )
    
    
    :type NextToken: string
    :param NextToken: Token returned by the previous ListTopics request.

    :rtype: dict
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
    
    
    :example: response = client.opt_in_phone_number(
        phoneNumber='string'
    )
    
    
    :type phoneNumber: string
    :param phoneNumber: [REQUIRED]
            The phone number to opt in.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def publish(TopicArn=None, TargetArn=None, PhoneNumber=None, Message=None, Subject=None, MessageStructure=None, MessageAttributes=None):
    """
    Sends a message to all of a topic's subscribed endpoints. When a messageId is returned, the message has been saved and Amazon SNS will attempt to deliver it to the topic's subscribers shortly. The format of the outgoing message to each subscribed endpoint depends on the notification protocol.
    To use the Publish action for sending a message to a mobile endpoint, such as an app on a Kindle device or mobile phone, you must specify the EndpointArn for the TargetArn parameter. The EndpointArn is returned when making a call with the CreatePlatformEndpoint action.
    For more information about formatting messages, see Send Custom Platform-Specific Payloads in Messages to Mobile Devices .
    See also: AWS API Documentation
    
    
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
    :param TopicArn: The topic you want to publish to.
            If you don't specify a value for the TopicArn parameter, you must specify a value for the PhoneNumber or TargetArn parameters.
            

    :type TargetArn: string
    :param TargetArn: Either TopicArn or EndpointArn, but not both.
            If you don't specify a value for the TargetArn parameter, you must specify a value for the PhoneNumber or TopicArn parameters.
            

    :type PhoneNumber: string
    :param PhoneNumber: The phone number to which you want to deliver an SMS message. Use E.164 format.
            If you don't specify a value for the PhoneNumber parameter, you must specify a value for the TargetArn or TopicArn parameters.
            

    :type Message: string
    :param Message: [REQUIRED]
            The message you want to send to the topic.
            If you want to send the same message to all transport protocols, include the text of the message as a String value.
            If you want to send different messages for each transport protocol, set the value of the MessageStructure parameter to json and use a JSON object for the Message parameter.
            Constraints: Messages must be UTF-8 encoded strings at most 256 KB in size (262144 bytes, not 262144 characters).
            JSON-specific constraints:
            Keys in the JSON object that correspond to supported transport protocols must have simple JSON string values.
            The values will be parsed (unescaped) before they are used in outgoing messages.
            Outbound notifications are JSON encoded (meaning that the characters will be reescaped for sending).
            Values have a minimum length of 0 (the empty string, '', is allowed).
            Values have a maximum length bounded by the overall message size (so, including multiple protocols may limit message sizes).
            Non-string values will cause the key to be ignored.
            Keys that do not correspond to supported transport protocols are ignored.
            Duplicate keys are not allowed.
            Failure to parse or validate any key or value in the message will cause the Publish call to return an error (no partial delivery).
            

    :type Subject: string
    :param Subject: Optional parameter to be used as the 'Subject' line when the message is delivered to email endpoints. This field will also be included, if present, in the standard JSON messages delivered to other endpoints.
            Constraints: Subjects must be ASCII text that begins with a letter, number, or punctuation mark; must not include line breaks or control characters; and must be less than 100 characters long.
            

    :type MessageStructure: string
    :param MessageStructure: Set MessageStructure to json if you want to send a different message for each protocol. For example, using one publish action, you can send a short message to your SMS subscribers and a longer message to your email subscribers. If you set MessageStructure to json , the value of the Message parameter must:
            be a syntactically valid JSON object; and
            contain at least a top-level JSON key of 'default' with a value that is a string.
            You can define other top-level keys that define the message you want to send to a specific transport protocol (e.g., 'http').
            For information about sending different messages for each protocol using the AWS Management Console, go to Create Different Messages for Each Protocol in the Amazon Simple Notification Service Getting Started Guide .
            Valid value: json
            

    :type MessageAttributes: dict
    :param MessageAttributes: Message attributes for Publish action.
            (string) --
            (dict) --The user-specified message attribute value. For string data types, the value attribute has the same restrictions on the content as the message body. For more information, see Publish .
            Name, type, and value must not be empty or null. In addition, the message body should not be empty or null. All parts of the message attribute, including name, type, and value, are included in the message size restriction, which is currently 256 KB (262,144 bytes). For more information, see Using Amazon SNS Message Attributes .
            DataType (string) -- [REQUIRED]Amazon SNS supports the following logical data types: String, Number, and Binary. For more information, see Message Attribute Data Types .
            StringValue (string) --Strings are Unicode with UTF8 binary encoding. For a list of code values, see http://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters .
            BinaryValue (bytes) --Binary type attributes can store any binary data, for example, compressed data, encrypted data, or images.
            
            

    :rtype: dict
    :return: {
        'MessageId': 'string'
    }
    
    
    """
    pass

def remove_permission(TopicArn=None, Label=None):
    """
    Removes a statement from a topic's access control policy.
    See also: AWS API Documentation
    
    
    :example: response = client.remove_permission(
        TopicArn='string',
        Label='string'
    )
    
    
    :type TopicArn: string
    :param TopicArn: [REQUIRED]
            The ARN of the topic whose access control policy you wish to modify.
            

    :type Label: string
    :param Label: [REQUIRED]
            The unique label of the statement you want to remove.
            

    """
    pass

def set_endpoint_attributes(EndpointArn=None, Attributes=None):
    """
    Sets the attributes for an endpoint for a device on one of the supported push notification services, such as GCM and APNS. For more information, see Using Amazon SNS Mobile Push Notifications .
    See also: AWS API Documentation
    
    
    :example: response = client.set_endpoint_attributes(
        EndpointArn='string',
        Attributes={
            'string': 'string'
        }
    )
    
    
    :type EndpointArn: string
    :param EndpointArn: [REQUIRED]
            EndpointArn used for SetEndpointAttributes action.
            

    :type Attributes: dict
    :param Attributes: [REQUIRED]
            A map of the endpoint attributes. Attributes in this map include the following:
            CustomUserData -- arbitrary user data to associate with the endpoint. Amazon SNS does not use this data. The data must be in UTF-8 format and less than 2KB.
            Enabled -- flag that enables/disables delivery to the endpoint. Amazon SNS will set this to false when a notification service indicates to Amazon SNS that the endpoint is invalid. Users can set it back to true, typically after updating Token.
            Token -- device token, also referred to as a registration id, for an app and mobile device. This is returned from the notification service when an app and mobile device are registered with the notification service.
            (string) --
            (string) --
            

    """
    pass

def set_platform_application_attributes(PlatformApplicationArn=None, Attributes=None):
    """
    Sets the attributes of the platform application object for the supported push notification services, such as APNS and GCM. For more information, see Using Amazon SNS Mobile Push Notifications . For information on configuring attributes for message delivery status, see Using Amazon SNS Application Attributes for Message Delivery Status .
    See also: AWS API Documentation
    
    
    :example: response = client.set_platform_application_attributes(
        PlatformApplicationArn='string',
        Attributes={
            'string': 'string'
        }
    )
    
    
    :type PlatformApplicationArn: string
    :param PlatformApplicationArn: [REQUIRED]
            PlatformApplicationArn for SetPlatformApplicationAttributes action.
            

    :type Attributes: dict
    :param Attributes: [REQUIRED]
            A map of the platform application attributes. Attributes in this map include the following:
            PlatformCredential -- The credential received from the notification service. For APNS/APNS_SANDBOX, PlatformCredential is private key. For GCM, PlatformCredential is 'API key'. For ADM, PlatformCredential is 'client secret'.
            PlatformPrincipal -- The principal received from the notification service. For APNS/APNS_SANDBOX, PlatformPrincipal is SSL certificate. For GCM, PlatformPrincipal is not applicable. For ADM, PlatformPrincipal is 'client id'.
            EventEndpointCreated -- Topic ARN to which EndpointCreated event notifications should be sent.
            EventEndpointDeleted -- Topic ARN to which EndpointDeleted event notifications should be sent.
            EventEndpointUpdated -- Topic ARN to which EndpointUpdate event notifications should be sent.
            EventDeliveryFailure -- Topic ARN to which DeliveryFailure event notifications should be sent upon Direct Publish delivery failure (permanent) to one of the application's endpoints.
            SuccessFeedbackRoleArn -- IAM role ARN used to give Amazon SNS write access to use CloudWatch Logs on your behalf.
            FailureFeedbackRoleArn -- IAM role ARN used to give Amazon SNS write access to use CloudWatch Logs on your behalf.
            SuccessFeedbackSampleRate -- Sample rate percentage (0-100) of successfully delivered messages.
            (string) --
            (string) --
            

    """
    pass

def set_sms_attributes(attributes=None):
    """
    Use this request to set the default settings for sending SMS messages and receiving daily SMS usage reports.
    You can override some of these settings for a single message when you use the Publish action with the MessageAttributes.entry.N parameter. For more information, see Sending an SMS Message in the Amazon SNS Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.set_sms_attributes(
        attributes={
            'string': 'string'
        }
    )
    
    
    :type attributes: dict
    :param attributes: [REQUIRED]
            The default settings for sending SMS messages from your account. You can set values for the following attribute names:
            MonthlySpendLimit   The maximum amount in USD that you are willing to spend each month to send SMS messages. When Amazon SNS determines that sending an SMS message would incur a cost that exceeds this limit, it stops sending SMS messages within minutes.
            Warning
            Amazon SNS stops sending SMS messages within minutes of the limit being crossed. During that interval, if you continue to send SMS messages, you will incur costs that exceed your limit.
            By default, the spend limit is set to the maximum allowed by Amazon SNS. If you want to exceed the maximum, contact AWS Support or your AWS sales representative for a service limit increase.
            DeliveryStatusIAMRole   The ARN of the IAM role that allows Amazon SNS to write logs about SMS deliveries in CloudWatch Logs. For each SMS message that you send, Amazon SNS writes a log that includes the message price, the success or failure status, the reason for failure (if the message failed), the message dwell time, and other information.DeliveryStatusSuccessSamplingRate   The percentage of successful SMS deliveries for which Amazon SNS will write logs in CloudWatch Logs. The value can be an integer from 0 - 100. For example, to write logs only for failed deliveries, set this value to 0 . To write logs for 10% of your successful deliveries, set it to 10 .
            DefaultSenderID   A string, such as your business brand, that is displayed as the sender on the receiving device. Support for sender IDs varies by country. The sender ID can be 1 - 11 alphanumeric characters, and it must contain at least one letter.
            DefaultSMSType   The type of SMS message that you will send by default. You can assign the following values:
            Promotional   (Default) Noncritical messages, such as marketing messages. Amazon SNS optimizes the message delivery to incur the lowest cost.
            Transactional   Critical messages that support customer transactions, such as one-time passcodes for multi-factor authentication. Amazon SNS optimizes the message delivery to achieve the highest reliability.
            UsageReportS3Bucket   The name of the Amazon S3 bucket to receive daily SMS usage reports from Amazon SNS. Each day, Amazon SNS will deliver a usage report as a CSV file to the bucket. The report includes the following information for each SMS message that was successfully delivered by your account:
            Time that the message was published (in UTC)
            Message ID
            Destination phone number
            Message type
            Delivery status
            Message price (in USD)
            Part number (a message is split into multiple parts if it is too long for a single message)
            Total number of parts
            To receive the report, the bucket must have a policy that allows the Amazon SNS service principle to perform the s3:PutObject and s3:GetBucketLocation actions.
            For an example bucket policy and usage report, see Monitoring SMS Activity in the Amazon SNS Developer Guide .
            (string) --
            (string) --
            

    :rtype: dict
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
    Allows a subscription owner to set an attribute of the topic to a new value.
    See also: AWS API Documentation
    
    
    :example: response = client.set_subscription_attributes(
        SubscriptionArn='string',
        AttributeName='string',
        AttributeValue='string'
    )
    
    
    :type SubscriptionArn: string
    :param SubscriptionArn: [REQUIRED]
            The ARN of the subscription to modify.
            

    :type AttributeName: string
    :param AttributeName: [REQUIRED]
            The name of the attribute you want to set. Only a subset of the subscriptions attributes are mutable.
            Valid values: DeliveryPolicy | RawMessageDelivery
            

    :type AttributeValue: string
    :param AttributeValue: The new value for the attribute in JSON format.

    """
    pass

def set_topic_attributes(TopicArn=None, AttributeName=None, AttributeValue=None):
    """
    Allows a topic owner to set an attribute of the topic to a new value.
    See also: AWS API Documentation
    
    
    :example: response = client.set_topic_attributes(
        TopicArn='string',
        AttributeName='string',
        AttributeValue='string'
    )
    
    
    :type TopicArn: string
    :param TopicArn: [REQUIRED]
            The ARN of the topic to modify.
            

    :type AttributeName: string
    :param AttributeName: [REQUIRED]
            The name of the attribute you want to set. Only a subset of the topic's attributes are mutable.
            Valid values: Policy | DisplayName | DeliveryPolicy
            

    :type AttributeValue: string
    :param AttributeValue: The new value for the attribute.

    """
    pass

def subscribe(TopicArn=None, Protocol=None, Endpoint=None):
    """
    Prepares to subscribe an endpoint by sending the endpoint a confirmation message. To actually create a subscription, the endpoint owner must call the ConfirmSubscription action with the token from the confirmation message. Confirmation tokens are valid for three days.
    See also: AWS API Documentation
    
    
    :example: response = client.subscribe(
        TopicArn='string',
        Protocol='string',
        Endpoint='string'
    )
    
    
    :type TopicArn: string
    :param TopicArn: [REQUIRED]
            The ARN of the topic you want to subscribe to.
            

    :type Protocol: string
    :param Protocol: [REQUIRED]
            The protocol you want to use. Supported protocols include:
            http -- delivery of JSON-encoded message via HTTP POST
            https -- delivery of JSON-encoded message via HTTPS POST
            email -- delivery of message via SMTP
            email-json -- delivery of JSON-encoded message via SMTP
            sms -- delivery of message via SMS
            sqs -- delivery of JSON-encoded message to an Amazon SQS queue
            application -- delivery of JSON-encoded message to an EndpointArn for a mobile app and device.
            lambda -- delivery of JSON-encoded message to an AWS Lambda function.
            

    :type Endpoint: string
    :param Endpoint: The endpoint that you want to receive notifications. Endpoints vary by protocol:
            For the http protocol, the endpoint is an URL beginning with 'http://'
            For the https protocol, the endpoint is a URL beginning with 'https://'
            For the email protocol, the endpoint is an email address
            For the email-json protocol, the endpoint is an email address
            For the sms protocol, the endpoint is a phone number of an SMS-enabled device
            For the sqs protocol, the endpoint is the ARN of an Amazon SQS queue
            For the application protocol, the endpoint is the EndpointArn of a mobile app and device.
            For the lambda protocol, the endpoint is the ARN of an AWS Lambda function.
            

    :rtype: dict
    :return: {
        'SubscriptionArn': 'string'
    }
    
    
    """
    pass

def unsubscribe(SubscriptionArn=None):
    """
    Deletes a subscription. If the subscription requires authentication for deletion, only the owner of the subscription or the topic's owner can unsubscribe, and an AWS signature is required. If the Unsubscribe call does not require authentication and the requester is not the subscription owner, a final cancellation message is delivered to the endpoint, so that the endpoint owner can easily resubscribe to the topic if the Unsubscribe request was unintended.
    See also: AWS API Documentation
    
    
    :example: response = client.unsubscribe(
        SubscriptionArn='string'
    )
    
    
    :type SubscriptionArn: string
    :param SubscriptionArn: [REQUIRED]
            The ARN of the subscription to be deleted.
            

    """
    pass

