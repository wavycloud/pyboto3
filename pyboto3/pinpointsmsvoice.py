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

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def create_configuration_set(ConfigurationSetName=None):
    """
    Create a new configuration set. After you create the configuration set, you can add one or more event destinations to it.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_configuration_set(
        ConfigurationSetName='string'
    )
    
    
    :type ConfigurationSetName: string
    :param ConfigurationSetName: The name that you want to give the configuration set.

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) -- CreateConfigurationSetResponse



Exceptions

PinpointSMSVoice.Client.exceptions.TooManyRequestsException
PinpointSMSVoice.Client.exceptions.BadRequestException
PinpointSMSVoice.Client.exceptions.LimitExceededException
PinpointSMSVoice.Client.exceptions.InternalServiceErrorException
PinpointSMSVoice.Client.exceptions.AlreadyExistsException


    :return: {}
    
    
    :returns: 
    PinpointSMSVoice.Client.exceptions.TooManyRequestsException
    PinpointSMSVoice.Client.exceptions.BadRequestException
    PinpointSMSVoice.Client.exceptions.LimitExceededException
    PinpointSMSVoice.Client.exceptions.InternalServiceErrorException
    PinpointSMSVoice.Client.exceptions.AlreadyExistsException
    
    """
    pass

def create_configuration_set_event_destination(ConfigurationSetName=None, EventDestination=None, EventDestinationName=None):
    """
    Create a new event destination in a configuration set.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_configuration_set_event_destination(
        ConfigurationSetName='string',
        EventDestination={
            'CloudWatchLogsDestination': {
                'IamRoleArn': 'string',
                'LogGroupArn': 'string'
            },
            'Enabled': True|False,
            'KinesisFirehoseDestination': {
                'DeliveryStreamArn': 'string',
                'IamRoleArn': 'string'
            },
            'MatchingEventTypes': [
                'INITIATED_CALL'|'RINGING'|'ANSWERED'|'COMPLETED_CALL'|'BUSY'|'FAILED'|'NO_ANSWER',
            ],
            'SnsDestination': {
                'TopicArn': 'string'
            }
        },
        EventDestinationName='string'
    )
    
    
    :type ConfigurationSetName: string
    :param ConfigurationSetName: [REQUIRED] ConfigurationSetName

    :type EventDestination: dict
    :param EventDestination: An object that defines a single event destination.\n\nCloudWatchLogsDestination (dict) -- An object that contains information about an event destination that sends data to Amazon CloudWatch Logs.\nIamRoleArn (string) -- The Amazon Resource Name (ARN) of an Amazon Identity and Access Management (IAM) role that is able to write event data to an Amazon CloudWatch destination.\nLogGroupArn (string) -- The name of the Amazon CloudWatch Log Group that you want to record events in.\n\n\nEnabled (boolean) -- Indicates whether or not the event destination is enabled. If the event destination is enabled, then Amazon Pinpoint sends response data to the specified event destination.\nKinesisFirehoseDestination (dict) -- An object that contains information about an event destination that sends data to Amazon Kinesis Data Firehose.\nDeliveryStreamArn (string) -- The Amazon Resource Name (ARN) of an IAM role that can write data to an Amazon Kinesis Data Firehose stream.\nIamRoleArn (string) -- The Amazon Resource Name (ARN) of the Amazon Kinesis Data Firehose destination that you want to use in the event destination.\n\n\nMatchingEventTypes (list) -- An array of EventDestination objects. Each EventDestination object includes ARNs and other information that define an event destination.\n(string) -- The types of events that are sent to the event destination.\n\n\nSnsDestination (dict) -- An object that contains information about an event destination that sends data to Amazon SNS.\nTopicArn (string) -- The Amazon Resource Name (ARN) of the Amazon SNS topic that you want to publish events to.\n\n\n\n

    :type EventDestinationName: string
    :param EventDestinationName: A name that identifies the event destination.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) -- CreateConfigurationSetEventDestinationResponse




Exceptions

PinpointSMSVoice.Client.exceptions.BadRequestException
PinpointSMSVoice.Client.exceptions.LimitExceededException
PinpointSMSVoice.Client.exceptions.InternalServiceErrorException
PinpointSMSVoice.Client.exceptions.NotFoundException
PinpointSMSVoice.Client.exceptions.TooManyRequestsException
PinpointSMSVoice.Client.exceptions.AlreadyExistsException


    :return: {}
    
    
    :returns: 
    (dict) -- CreateConfigurationSetEventDestinationResponse
    
    """
    pass

def delete_configuration_set(ConfigurationSetName=None):
    """
    Deletes an existing configuration set.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_configuration_set(
        ConfigurationSetName='string'
    )
    
    
    :type ConfigurationSetName: string
    :param ConfigurationSetName: [REQUIRED] ConfigurationSetName

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) -- DeleteConfigurationSetResponse



Exceptions

PinpointSMSVoice.Client.exceptions.NotFoundException
PinpointSMSVoice.Client.exceptions.TooManyRequestsException
PinpointSMSVoice.Client.exceptions.BadRequestException
PinpointSMSVoice.Client.exceptions.InternalServiceErrorException


    :return: {}
    
    
    :returns: 
    PinpointSMSVoice.Client.exceptions.NotFoundException
    PinpointSMSVoice.Client.exceptions.TooManyRequestsException
    PinpointSMSVoice.Client.exceptions.BadRequestException
    PinpointSMSVoice.Client.exceptions.InternalServiceErrorException
    
    """
    pass

def delete_configuration_set_event_destination(ConfigurationSetName=None, EventDestinationName=None):
    """
    Deletes an event destination in a configuration set.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_configuration_set_event_destination(
        ConfigurationSetName='string',
        EventDestinationName='string'
    )
    
    
    :type ConfigurationSetName: string
    :param ConfigurationSetName: [REQUIRED] ConfigurationSetName

    :type EventDestinationName: string
    :param EventDestinationName: [REQUIRED] EventDestinationName

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) -- DeleteConfigurationSetEventDestinationResponse




Exceptions

PinpointSMSVoice.Client.exceptions.NotFoundException
PinpointSMSVoice.Client.exceptions.TooManyRequestsException
PinpointSMSVoice.Client.exceptions.BadRequestException
PinpointSMSVoice.Client.exceptions.InternalServiceErrorException


    :return: {}
    
    
    :returns: 
    (dict) -- DeleteConfigurationSetEventDestinationResponse
    
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

def get_configuration_set_event_destinations(ConfigurationSetName=None):
    """
    Obtain information about an event destination, including the types of events it reports, the Amazon Resource Name (ARN) of the destination, and the name of the event destination.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_configuration_set_event_destinations(
        ConfigurationSetName='string'
    )
    
    
    :type ConfigurationSetName: string
    :param ConfigurationSetName: [REQUIRED] ConfigurationSetName

    :rtype: dict
ReturnsResponse Syntax{
    'EventDestinations': [
        {
            'CloudWatchLogsDestination': {
                'IamRoleArn': 'string',
                'LogGroupArn': 'string'
            },
            'Enabled': True|False,
            'KinesisFirehoseDestination': {
                'DeliveryStreamArn': 'string',
                'IamRoleArn': 'string'
            },
            'MatchingEventTypes': [
                'INITIATED_CALL'|'RINGING'|'ANSWERED'|'COMPLETED_CALL'|'BUSY'|'FAILED'|'NO_ANSWER',
            ],
            'Name': 'string',
            'SnsDestination': {
                'TopicArn': 'string'
            }
        },
    ]
}


Response Structure

(dict) -- GetConfigurationSetEventDestinationsResponse
EventDestinations (list) -- An array of EventDestination objects. Each EventDestination object includes ARNs and other information that define an event destination.
(dict) -- An object that defines an event destination.
CloudWatchLogsDestination (dict) -- An object that contains information about an event destination that sends data to Amazon CloudWatch Logs.
IamRoleArn (string) -- The Amazon Resource Name (ARN) of an Amazon Identity and Access Management (IAM) role that is able to write event data to an Amazon CloudWatch destination.
LogGroupArn (string) -- The name of the Amazon CloudWatch Log Group that you want to record events in.


Enabled (boolean) -- Indicates whether or not the event destination is enabled. If the event destination is enabled, then Amazon Pinpoint sends response data to the specified event destination.
KinesisFirehoseDestination (dict) -- An object that contains information about an event destination that sends data to Amazon Kinesis Data Firehose.
DeliveryStreamArn (string) -- The Amazon Resource Name (ARN) of an IAM role that can write data to an Amazon Kinesis Data Firehose stream.
IamRoleArn (string) -- The Amazon Resource Name (ARN) of the Amazon Kinesis Data Firehose destination that you want to use in the event destination.


MatchingEventTypes (list) -- An array of EventDestination objects. Each EventDestination object includes ARNs and other information that define an event destination.
(string) -- The types of events that are sent to the event destination.


Name (string) -- A name that identifies the event destination configuration.
SnsDestination (dict) -- An object that contains information about an event destination that sends data to Amazon SNS.
TopicArn (string) -- The Amazon Resource Name (ARN) of the Amazon SNS topic that you want to publish events to.











Exceptions

PinpointSMSVoice.Client.exceptions.NotFoundException
PinpointSMSVoice.Client.exceptions.TooManyRequestsException
PinpointSMSVoice.Client.exceptions.BadRequestException
PinpointSMSVoice.Client.exceptions.InternalServiceErrorException


    :return: {
        'EventDestinations': [
            {
                'CloudWatchLogsDestination': {
                    'IamRoleArn': 'string',
                    'LogGroupArn': 'string'
                },
                'Enabled': True|False,
                'KinesisFirehoseDestination': {
                    'DeliveryStreamArn': 'string',
                    'IamRoleArn': 'string'
                },
                'MatchingEventTypes': [
                    'INITIATED_CALL'|'RINGING'|'ANSWERED'|'COMPLETED_CALL'|'BUSY'|'FAILED'|'NO_ANSWER',
                ],
                'Name': 'string',
                'SnsDestination': {
                    'TopicArn': 'string'
                }
            },
        ]
    }
    
    
    :returns: 
    PinpointSMSVoice.Client.exceptions.NotFoundException
    PinpointSMSVoice.Client.exceptions.TooManyRequestsException
    PinpointSMSVoice.Client.exceptions.BadRequestException
    PinpointSMSVoice.Client.exceptions.InternalServiceErrorException
    
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

def list_configuration_sets(NextToken=None, PageSize=None):
    """
    List all of the configuration sets associated with your Amazon Pinpoint account in the current region.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_configuration_sets(
        NextToken='string',
        PageSize='string'
    )
    
    
    :type NextToken: string
    :param NextToken: A token returned from a previous call to the API that indicates the position in the list of results.

    :type PageSize: string
    :param PageSize: Used to specify the number of items that should be returned in the response.

    :rtype: dict

ReturnsResponse Syntax
{
    'ConfigurationSets': [
        'string',
    ],
    'NextToken': 'string'
}


Response Structure

(dict) -- ListConfigurationSetsResponse
ConfigurationSets (list) -- An object that contains a list of configuration sets for your account in the current region.
(string) --


NextToken (string) -- A token returned from a previous call to ListConfigurationSets to indicate the position in the list of configuration sets.






Exceptions

PinpointSMSVoice.Client.exceptions.TooManyRequestsException
PinpointSMSVoice.Client.exceptions.BadRequestException
PinpointSMSVoice.Client.exceptions.InternalServiceErrorException


    :return: {
        'ConfigurationSets': [
            'string',
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (dict) -- ListConfigurationSetsResponse
    ConfigurationSets (list) -- An object that contains a list of configuration sets for your account in the current region.
    (string) --
    
    
    NextToken (string) -- A token returned from a previous call to ListConfigurationSets to indicate the position in the list of configuration sets.
    
    
    
    """
    pass

def send_voice_message(CallerId=None, ConfigurationSetName=None, Content=None, DestinationPhoneNumber=None, OriginationPhoneNumber=None):
    """
    Create a new voice message and send it to a recipient\'s phone number.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.send_voice_message(
        CallerId='string',
        ConfigurationSetName='string',
        Content={
            'CallInstructionsMessage': {
                'Text': 'string'
            },
            'PlainTextMessage': {
                'LanguageCode': 'string',
                'Text': 'string',
                'VoiceId': 'string'
            },
            'SSMLMessage': {
                'LanguageCode': 'string',
                'Text': 'string',
                'VoiceId': 'string'
            }
        },
        DestinationPhoneNumber='string',
        OriginationPhoneNumber='string'
    )
    
    
    :type CallerId: string
    :param CallerId: The phone number that appears on recipients\' devices when they receive the message.

    :type ConfigurationSetName: string
    :param ConfigurationSetName: The name of the configuration set that you want to use to send the message.

    :type Content: dict
    :param Content: An object that contains a voice message and information about the recipient that you want to send it to.\n\nCallInstructionsMessage (dict) -- An object that defines a message that contains text formatted using Amazon Pinpoint Voice Instructions markup.\nText (string) -- The language to use when delivering the message. For a complete list of supported languages, see the Amazon Polly Developer Guide.\n\n\nPlainTextMessage (dict) -- An object that defines a message that contains unformatted text.\nLanguageCode (string) -- The language to use when delivering the message. For a complete list of supported languages, see the Amazon Polly Developer Guide.\nText (string) -- The plain (not SSML-formatted) text to deliver to the recipient.\nVoiceId (string) -- The name of the voice that you want to use to deliver the message. For a complete list of supported voices, see the Amazon Polly Developer Guide.\n\n\nSSMLMessage (dict) -- An object that defines a message that contains SSML-formatted text.\nLanguageCode (string) -- The language to use when delivering the message. For a complete list of supported languages, see the Amazon Polly Developer Guide.\nText (string) -- The SSML-formatted text to deliver to the recipient.\nVoiceId (string) -- The name of the voice that you want to use to deliver the message. For a complete list of supported voices, see the Amazon Polly Developer Guide.\n\n\n\n

    :type DestinationPhoneNumber: string
    :param DestinationPhoneNumber: The phone number that you want to send the voice message to.

    :type OriginationPhoneNumber: string
    :param OriginationPhoneNumber: The phone number that Amazon Pinpoint should use to send the voice message. This isn\'t necessarily the phone number that appears on recipients\' devices when they receive the message, because you can specify a CallerId parameter in the request.

    :rtype: dict

ReturnsResponse Syntax
{
    'MessageId': 'string'
}


Response Structure

(dict) -- SendVoiceMessageResponse
MessageId (string) -- A unique identifier for the voice message.






Exceptions

PinpointSMSVoice.Client.exceptions.TooManyRequestsException
PinpointSMSVoice.Client.exceptions.BadRequestException
PinpointSMSVoice.Client.exceptions.InternalServiceErrorException


    :return: {
        'MessageId': 'string'
    }
    
    
    :returns: 
    (dict) -- SendVoiceMessageResponse
    MessageId (string) -- A unique identifier for the voice message.
    
    
    
    """
    pass

def update_configuration_set_event_destination(ConfigurationSetName=None, EventDestination=None, EventDestinationName=None):
    """
    Update an event destination in a configuration set. An event destination is a location that you publish information about your voice calls to. For example, you can log an event to an Amazon CloudWatch destination when a call fails.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_configuration_set_event_destination(
        ConfigurationSetName='string',
        EventDestination={
            'CloudWatchLogsDestination': {
                'IamRoleArn': 'string',
                'LogGroupArn': 'string'
            },
            'Enabled': True|False,
            'KinesisFirehoseDestination': {
                'DeliveryStreamArn': 'string',
                'IamRoleArn': 'string'
            },
            'MatchingEventTypes': [
                'INITIATED_CALL'|'RINGING'|'ANSWERED'|'COMPLETED_CALL'|'BUSY'|'FAILED'|'NO_ANSWER',
            ],
            'SnsDestination': {
                'TopicArn': 'string'
            }
        },
        EventDestinationName='string'
    )
    
    
    :type ConfigurationSetName: string
    :param ConfigurationSetName: [REQUIRED] ConfigurationSetName

    :type EventDestination: dict
    :param EventDestination: An object that defines a single event destination.\n\nCloudWatchLogsDestination (dict) -- An object that contains information about an event destination that sends data to Amazon CloudWatch Logs.\nIamRoleArn (string) -- The Amazon Resource Name (ARN) of an Amazon Identity and Access Management (IAM) role that is able to write event data to an Amazon CloudWatch destination.\nLogGroupArn (string) -- The name of the Amazon CloudWatch Log Group that you want to record events in.\n\n\nEnabled (boolean) -- Indicates whether or not the event destination is enabled. If the event destination is enabled, then Amazon Pinpoint sends response data to the specified event destination.\nKinesisFirehoseDestination (dict) -- An object that contains information about an event destination that sends data to Amazon Kinesis Data Firehose.\nDeliveryStreamArn (string) -- The Amazon Resource Name (ARN) of an IAM role that can write data to an Amazon Kinesis Data Firehose stream.\nIamRoleArn (string) -- The Amazon Resource Name (ARN) of the Amazon Kinesis Data Firehose destination that you want to use in the event destination.\n\n\nMatchingEventTypes (list) -- An array of EventDestination objects. Each EventDestination object includes ARNs and other information that define an event destination.\n(string) -- The types of events that are sent to the event destination.\n\n\nSnsDestination (dict) -- An object that contains information about an event destination that sends data to Amazon SNS.\nTopicArn (string) -- The Amazon Resource Name (ARN) of the Amazon SNS topic that you want to publish events to.\n\n\n\n

    :type EventDestinationName: string
    :param EventDestinationName: [REQUIRED] EventDestinationName

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) -- UpdateConfigurationSetEventDestinationResponse




Exceptions

PinpointSMSVoice.Client.exceptions.NotFoundException
PinpointSMSVoice.Client.exceptions.TooManyRequestsException
PinpointSMSVoice.Client.exceptions.BadRequestException
PinpointSMSVoice.Client.exceptions.InternalServiceErrorException


    :return: {}
    
    
    :returns: 
    (dict) -- UpdateConfigurationSetEventDestinationResponse
    
    """
    pass

