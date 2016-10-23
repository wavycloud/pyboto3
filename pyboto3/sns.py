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


def add_permission(TopicArn=None, Label=None, AWSAccountId=None, ActionName=None):
    """
    :param TopicArn: [REQUIRED]
            The ARN of the topic whose access control policy you wish to modify.
            
    :type TopicArn: string
    :param Label: [REQUIRED]
            A unique identifier for the new policy statement.
            
    :type Label: string
    :param AWSAccountId: [REQUIRED]
            The AWS account IDs of the users (principals) who will be given access to the specified actions. The users must have AWS accounts, but do not need to be signed up for this service.
            (string) --
            
    :type AWSAccountId: list
    :param ActionName: [REQUIRED]
            The action you want to allow for the specified principal(s).
            Valid values: any Amazon SNS action name.
            (string) --
            
    :type ActionName: list
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


def check_if_phone_number_is_opted_out(phoneNumber=None):
    """
    :param phoneNumber: [REQUIRED]
            The phone number for which you want to check the opt out status.
            Return typedict
            ReturnsResponse Syntax{
              'isOptedOut': True|False
            }
            Response Structure
            (dict) --The response from the CheckIfPhoneNumberIsOptedOut action.
            isOptedOut (boolean) --Indicates whether the phone number is opted out:
            true   The phone number is opted out, meaning you cannot publish SMS messages to it.
            false   The phone number is opted in, meaning you can publish SMS messages to it.
            
            
    :type phoneNumber: string
    """
    pass


def confirm_subscription(TopicArn=None, Token=None, AuthenticateOnUnsubscribe=None):
    """
    :param TopicArn: [REQUIRED]
            The ARN of the topic for which you wish to confirm a subscription.
            
    :type TopicArn: string
    :param Token: [REQUIRED]
            Short-lived token sent to an endpoint during the Subscribe action.
            
    :type Token: string
    :param AuthenticateOnUnsubscribe: Disallows unauthenticated unsubscribes of the subscription. If the value of this parameter is true and the request has an AWS signature, then only the topic owner and the subscription owner can unsubscribe the endpoint. The unsubscribe action requires AWS authentication.
    :type AuthenticateOnUnsubscribe: string
    """
    pass


def create_platform_application(Name=None, Platform=None, Attributes=None):
    """
    :param Name: [REQUIRED]
            Application names must be made up of only uppercase and lowercase ASCII letters, numbers, underscores, hyphens, and periods, and must be between 1 and 256 characters long.
            
    :type Name: string
    :param Platform: [REQUIRED]
            The following platforms are supported: ADM (Amazon Device Messaging), APNS (Apple Push Notification Service), APNS_SANDBOX, and GCM (Google Cloud Messaging).
            
    :type Platform: string
    :param Attributes: [REQUIRED]
            For a list of attributes, see SetPlatformApplicationAttributes
            (string) --
            (string) --
            
    :type Attributes: dict
    """
    pass


def create_platform_endpoint(PlatformApplicationArn=None, Token=None, CustomUserData=None, Attributes=None):
    """
    :param PlatformApplicationArn: [REQUIRED]
            PlatformApplicationArn returned from CreatePlatformApplication is used to create a an endpoint.
            
    :type PlatformApplicationArn: string
    :param Token: [REQUIRED]
            Unique identifier created by the notification service for an app on a device. The specific name for Token will vary, depending on which notification service is being used. For example, when using APNS as the notification service, you need the device token. Alternatively, when using GCM or ADM, the device token equivalent is called the registration ID.
            
    :type Token: string
    :param CustomUserData: Arbitrary user data to associate with the endpoint. Amazon SNS does not use this data. The data must be in UTF-8 format and less than 2KB.
    :type CustomUserData: string
    :param Attributes: For a list of attributes, see SetEndpointAttributes .
            (string) --
            (string) --
            
    :type Attributes: dict
    """
    pass


def create_topic(Name=None):
    """
    :param Name: [REQUIRED]
            The name of the topic you want to create.
            Constraints: Topic names must be made up of only uppercase and lowercase ASCII letters, numbers, underscores, and hyphens, and must be between 1 and 256 characters long.
            Return typedict
            ReturnsResponse Syntax{
              'TopicArn': 'string'
            }
            Response Structure
            (dict) --Response from CreateTopic action.
            TopicArn (string) --The Amazon Resource Name (ARN) assigned to the created topic.
            
            
    :type Name: string
    """
    pass


def delete_endpoint(EndpointArn=None):
    """
    :param EndpointArn: [REQUIRED]
            EndpointArn of endpoint to delete.
            ReturnsNone
            
    :type EndpointArn: string
    """
    pass


def delete_platform_application(PlatformApplicationArn=None):
    """
    :param PlatformApplicationArn: [REQUIRED]
            PlatformApplicationArn of platform application object to delete.
            ReturnsNone
            
    :type PlatformApplicationArn: string
    """
    pass


def delete_topic(TopicArn=None):
    """
    :param TopicArn: [REQUIRED]
            The ARN of the topic you want to delete.
            ReturnsNone
            
    :type TopicArn: string
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


def get_endpoint_attributes(EndpointArn=None):
    """
    :param EndpointArn: [REQUIRED]
            EndpointArn for GetEndpointAttributes input.
            Return typedict
            ReturnsResponse Syntax{
              'Attributes': {
                'string': 'string'
              }
            }
            Response Structure
            (dict) --Response from GetEndpointAttributes of the EndpointArn.
            Attributes (dict) --Attributes include the following:
            CustomUserData -- arbitrary user data to associate with the endpoint. Amazon SNS does not use this data. The data must be in UTF-8 format and less than 2KB.
            Enabled -- flag that enables/disables delivery to the endpoint. Amazon SNS will set this to false when a notification service indicates to Amazon SNS that the endpoint is invalid. Users can set it back to true, typically after updating Token.
            Token -- device token, also referred to as a registration id, for an app and mobile device. This is returned from the notification service when an app and mobile device are registered with the notification service.
            (string) --
            (string) --
            
            
            
    :type EndpointArn: string
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


def get_platform_application_attributes(PlatformApplicationArn=None):
    """
    :param PlatformApplicationArn: [REQUIRED]
            PlatformApplicationArn for GetPlatformApplicationAttributesInput.
            Return typedict
            ReturnsResponse Syntax{
              'Attributes': {
                'string': 'string'
              }
            }
            Response Structure
            (dict) --Response for GetPlatformApplicationAttributes action.
            Attributes (dict) --Attributes include the following:
            EventEndpointCreated -- Topic ARN to which EndpointCreated event notifications should be sent.
            EventEndpointDeleted -- Topic ARN to which EndpointDeleted event notifications should be sent.
            EventEndpointUpdated -- Topic ARN to which EndpointUpdate event notifications should be sent.
            EventDeliveryFailure -- Topic ARN to which DeliveryFailure event notifications should be sent upon Direct Publish delivery failure (permanent) to one of the application's endpoints.
            (string) --
            (string) --
            
            
            
    :type PlatformApplicationArn: string
    """
    pass


def get_sms_attributes(attributes=None):
    """
    :param attributes: A list of the individual attribute names, such as MonthlySpendLimit , for which you want values.
            For all attribute names, see SetSMSAttributes .
            If you don't use this parameter, Amazon SNS returns all SMS attributes.
            (string) --
            Return typedict
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
            
            
            
    :type attributes: list
    """
    pass


def get_subscription_attributes(SubscriptionArn=None):
    """
    :param SubscriptionArn: [REQUIRED]
            The ARN of the subscription whose properties you want to get.
            Return typedict
            ReturnsResponse Syntax{
              'Attributes': {
                'string': 'string'
              }
            }
            Response Structure
            (dict) --Response for GetSubscriptionAttributes action.
            Attributes (dict) --A map of the subscription's attributes. Attributes in this map include the following:
            SubscriptionArn -- the subscription's ARN
            TopicArn -- the topic ARN that the subscription is associated with
            Owner -- the AWS account ID of the subscription's owner
            ConfirmationWasAuthenticated -- true if the subscription confirmation request was authenticated
            DeliveryPolicy -- the JSON serialization of the subscription's delivery policy
            EffectiveDeliveryPolicy -- the JSON serialization of the effective delivery policy that takes into account the topic delivery policy and account system defaults
            (string) --
            (string) --
            
            
            
    :type SubscriptionArn: string
    """
    pass


def get_topic_attributes(TopicArn=None):
    """
    :param TopicArn: [REQUIRED]
            The ARN of the topic whose properties you want to get.
            Return typedict
            ReturnsResponse Syntax{
              'Attributes': {
                'string': 'string'
              }
            }
            Response Structure
            (dict) --Response for GetTopicAttributes action.
            Attributes (dict) --A map of the topic's attributes. Attributes in this map include the following:
            TopicArn -- the topic's ARN
            Owner -- the AWS account ID of the topic's owner
            Policy -- the JSON serialization of the topic's access control policy
            DisplayName -- the human-readable name used in the 'From' field for notifications to email and email-json endpoints
            SubscriptionsPending -- the number of subscriptions pending confirmation on this topic
            SubscriptionsConfirmed -- the number of confirmed subscriptions on this topic
            SubscriptionsDeleted -- the number of deleted subscriptions on this topic
            DeliveryPolicy -- the JSON serialization of the topic's delivery policy
            EffectiveDeliveryPolicy -- the JSON serialization of the effective delivery policy that takes into account system defaults
            (string) --
            (string) --
            
            
            
    :type TopicArn: string
    """
    pass


def get_waiter():
    """
    """
    pass


def list_endpoints_by_platform_application(PlatformApplicationArn=None, NextToken=None):
    """
    :param PlatformApplicationArn: [REQUIRED]
            PlatformApplicationArn for ListEndpointsByPlatformApplicationInput action.
            
    :type PlatformApplicationArn: string
    :param NextToken: NextToken string is used when calling ListEndpointsByPlatformApplication action to retrieve additional records that are available after the first page results.
    :type NextToken: string
    """
    pass


def list_phone_numbers_opted_out(nextToken=None):
    """
    :param nextToken: A NextToken string is used when you call the ListPhoneNumbersOptedOut action to retrieve additional records that are available after the first page of results.
            Return typedict
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
            
            
    :type nextToken: string
    """
    pass


def list_platform_applications(NextToken=None):
    """
    :param NextToken: NextToken string is used when calling ListPlatformApplications action to retrieve additional records that are available after the first page results.
            Return typedict
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
            
            
    :type NextToken: string
    """
    pass


def list_subscriptions(NextToken=None):
    """
    :param NextToken: Token returned by the previous ListSubscriptions request.
            Return typedict
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
            SubscriptionArn (string) --The subscription's ARN.
            Owner (string) --The subscription's owner.
            Protocol (string) --The subscription's protocol.
            Endpoint (string) --The subscription's endpoint (format depends on the protocol).
            TopicArn (string) --The ARN of the subscription's topic.
            
            NextToken (string) --Token to pass along to the next ListSubscriptions request. This element is returned if there are more subscriptions to retrieve.
            
            
    :type NextToken: string
    """
    pass


def list_subscriptions_by_topic(TopicArn=None, NextToken=None):
    """
    :param TopicArn: [REQUIRED]
            The ARN of the topic for which you wish to find subscriptions.
            
    :type TopicArn: string
    :param NextToken: Token returned by the previous ListSubscriptionsByTopic request.
    :type NextToken: string
    """
    pass


def list_topics(NextToken=None):
    """
    :param NextToken: Token returned by the previous ListTopics request.
            Return typedict
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
            (dict) --A wrapper type for the topic's Amazon Resource Name (ARN). To retrieve a topic's attributes, use GetTopicAttributes .
            TopicArn (string) --The topic's ARN.
            
            NextToken (string) --Token to pass along to the next ListTopics request. This element is returned if there are additional topics to retrieve.
            
            
    :type NextToken: string
    """
    pass


def opt_in_phone_number(phoneNumber=None):
    """
    :param phoneNumber: [REQUIRED]
            The phone number to opt in.
            Return typedict
            ReturnsResponse Syntax{}
            Response Structure
            (dict) --The response for the OptInPhoneNumber action.
            
            
    :type phoneNumber: string
    """
    pass


def publish(TopicArn=None, TargetArn=None, PhoneNumber=None, Message=None, Subject=None, MessageStructure=None,
            MessageAttributes=None):
    """
    :param TopicArn: The topic you want to publish to.
            If you don't specify a value for the TopicArn parameter, you must specify a value for the PhoneNumber or TargetArn parameters.
            
    :type TopicArn: string
    :param TargetArn: Either TopicArn or EndpointArn, but not both.
            If you don't specify a value for the TargetArn parameter, you must specify a value for the PhoneNumber or TopicArn parameters.
            
    :type TargetArn: string
    :param PhoneNumber: The phone number to which you want to deliver an SMS message. Use E.164 format.
            If you don't specify a value for the PhoneNumber parameter, you must specify a value for the TargetArn or TopicArn parameters.
            
    :type PhoneNumber: string
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
            
    :type Message: string
    :param Subject: Optional parameter to be used as the 'Subject' line when the message is delivered to email endpoints. This field will also be included, if present, in the standard JSON messages delivered to other endpoints.
            Constraints: Subjects must be ASCII text that begins with a letter, number, or punctuation mark; must not include line breaks or control characters; and must be less than 100 characters long.
            
    :type Subject: string
    :param MessageStructure: Set MessageStructure to json if you want to send a different message for each protocol. For example, using one publish action, you can send a short message to your SMS subscribers and a longer message to your email subscribers. If you set MessageStructure to json , the value of the Message parameter must:
            be a syntactically valid JSON object; and
            contain at least a top-level JSON key of 'default' with a value that is a string.
            You can define other top-level keys that define the message you want to send to a specific transport protocol (e.g., 'http').
            For information about sending different messages for each protocol using the AWS Management Console, go to Create Different Messages for Each Protocol in the Amazon Simple Notification Service Getting Started Guide .
            Valid value: json
            
    :type MessageStructure: string
    :param MessageAttributes: Message attributes for Publish action.
            (string) --
            (dict) --The user-specified message attribute value. For string data types, the value attribute has the same restrictions on the content as the message body. For more information, see Publish .
            Name, type, and value must not be empty or null. In addition, the message body should not be empty or null. All parts of the message attribute, including name, type, and value, are included in the message size restriction, which is currently 256 KB (262,144 bytes). For more information, see Using Amazon SNS Message Attributes .
            DataType (string) -- [REQUIRED]Amazon SNS supports the following logical data types: String, Number, and Binary. For more information, see Message Attribute Data Types .
            StringValue (string) --Strings are Unicode with UTF8 binary encoding. For a list of code values, see http://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters .
            BinaryValue (bytes) --Binary type attributes can store any binary data, for example, compressed data, encrypted data, or images.
            
            
    :type MessageAttributes: dict
    """
    pass


def remove_permission(TopicArn=None, Label=None):
    """
    :param TopicArn: [REQUIRED]
            The ARN of the topic whose access control policy you wish to modify.
            
    :type TopicArn: string
    :param Label: [REQUIRED]
            The unique label of the statement you want to remove.
            
    :type Label: string
    """
    pass


def set_endpoint_attributes(EndpointArn=None, Attributes=None):
    """
    :param EndpointArn: [REQUIRED]
            EndpointArn used for SetEndpointAttributes action.
            
    :type EndpointArn: string
    :param Attributes: [REQUIRED]
            A map of the endpoint attributes. Attributes in this map include the following:
            CustomUserData -- arbitrary user data to associate with the endpoint. Amazon SNS does not use this data. The data must be in UTF-8 format and less than 2KB.
            Enabled -- flag that enables/disables delivery to the endpoint. Amazon SNS will set this to false when a notification service indicates to Amazon SNS that the endpoint is invalid. Users can set it back to true, typically after updating Token.
            Token -- device token, also referred to as a registration id, for an app and mobile device. This is returned from the notification service when an app and mobile device are registered with the notification service.
            (string) --
            (string) --
            
    :type Attributes: dict
    """
    pass


def set_platform_application_attributes(PlatformApplicationArn=None, Attributes=None):
    """
    :param PlatformApplicationArn: [REQUIRED]
            PlatformApplicationArn for SetPlatformApplicationAttributes action.
            
    :type PlatformApplicationArn: string
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
            
    :type Attributes: dict
    """
    pass


def set_sms_attributes(attributes=None):
    """
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
            
            Return typedict
            ReturnsResponse Syntax{}
            Response Structure
            (dict) --The response for the SetSMSAttributes action.
            
            
    :type attributes: dict
    """
    pass


def set_subscription_attributes(SubscriptionArn=None, AttributeName=None, AttributeValue=None):
    """
    :param SubscriptionArn: [REQUIRED]
            The ARN of the subscription to modify.
            
    :type SubscriptionArn: string
    :param AttributeName: [REQUIRED]
            The name of the attribute you want to set. Only a subset of the subscriptions attributes are mutable.
            Valid values: DeliveryPolicy | RawMessageDelivery
            
    :type AttributeName: string
    :param AttributeValue: The new value for the attribute in JSON format.
    :type AttributeValue: string
    """
    pass


def set_topic_attributes(TopicArn=None, AttributeName=None, AttributeValue=None):
    """
    :param TopicArn: [REQUIRED]
            The ARN of the topic to modify.
            
    :type TopicArn: string
    :param AttributeName: [REQUIRED]
            The name of the attribute you want to set. Only a subset of the topic's attributes are mutable.
            Valid values: Policy | DisplayName | DeliveryPolicy
            
    :type AttributeName: string
    :param AttributeValue: The new value for the attribute.
    :type AttributeValue: string
    """
    pass


def subscribe(TopicArn=None, Protocol=None, Endpoint=None):
    """
    :param TopicArn: [REQUIRED]
            The ARN of the topic you want to subscribe to.
            
    :type TopicArn: string
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
            
    :type Protocol: string
    :param Endpoint: The endpoint that you want to receive notifications. Endpoints vary by protocol:
            For the http protocol, the endpoint is an URL beginning with 'http://'
            For the https protocol, the endpoint is a URL beginning with 'https://'
            For the email protocol, the endpoint is an email address
            For the email-json protocol, the endpoint is an email address
            For the sms protocol, the endpoint is a phone number of an SMS-enabled device
            For the sqs protocol, the endpoint is the ARN of an Amazon SQS queue
            For the application protocol, the endpoint is the EndpointArn of a mobile app and device.
            For the lambda protocol, the endpoint is the ARN of an AWS Lambda function.
            
    :type Endpoint: string
    """
    pass


def unsubscribe(SubscriptionArn=None):
    """
    :param SubscriptionArn: [REQUIRED]
            The ARN of the subscription to be deleted.
            ReturnsNone
            
    :type SubscriptionArn: string
    """
    pass
