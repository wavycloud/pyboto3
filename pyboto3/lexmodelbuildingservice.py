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

def create_bot_version(name=None, checksum=None):
    """
    Creates a new version of the bot based on the $LATEST version. If the $LATEST version of this resource hasn\'t changed since you created the last version, Amazon Lex doesn\'t create a new version. It returns the last created version.
    When you create the first version of a bot, Amazon Lex sets the version to 1. Subsequent versions increment by 1. For more information, see  versioning-intro .
    This operation requires permission for the lex:CreateBotVersion action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_bot_version(
        name='string',
        checksum='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name of the bot that you want to create a new version of. The name is case sensitive.\n

    :type checksum: string
    :param checksum: Identifies a specific revision of the $LATEST version of the bot. If you specify a checksum and the $LATEST version of the bot has a different checksum, a PreconditionFailedException exception is returned and Amazon Lex doesn\'t publish a new version. If you don\'t specify a checksum, Amazon Lex publishes the $LATEST version.

    :rtype: dict

ReturnsResponse Syntax
{
    'name': 'string',
    'description': 'string',
    'intents': [
        {
            'intentName': 'string',
            'intentVersion': 'string'
        },
    ],
    'clarificationPrompt': {
        'messages': [
            {
                'contentType': 'PlainText'|'SSML'|'CustomPayload',
                'content': 'string',
                'groupNumber': 123
            },
        ],
        'maxAttempts': 123,
        'responseCard': 'string'
    },
    'abortStatement': {
        'messages': [
            {
                'contentType': 'PlainText'|'SSML'|'CustomPayload',
                'content': 'string',
                'groupNumber': 123
            },
        ],
        'responseCard': 'string'
    },
    'status': 'BUILDING'|'READY'|'READY_BASIC_TESTING'|'FAILED'|'NOT_BUILT',
    'failureReason': 'string',
    'lastUpdatedDate': datetime(2015, 1, 1),
    'createdDate': datetime(2015, 1, 1),
    'idleSessionTTLInSeconds': 123,
    'voiceId': 'string',
    'checksum': 'string',
    'version': 'string',
    'locale': 'en-US'|'en-GB'|'de-DE',
    'childDirected': True|False,
    'detectSentiment': True|False
}


Response Structure

(dict) --

name (string) --
The name of the bot.

description (string) --
A description of the bot.

intents (list) --
An array of Intent objects. For more information, see  PutBot .

(dict) --
Identifies the specific version of an intent.

intentName (string) --
The name of the intent.

intentVersion (string) --
The version of the intent.





clarificationPrompt (dict) --
The message that Amazon Lex uses when it doesn\'t understand the user\'s request. For more information, see  PutBot .

messages (list) --
An array of objects, each of which provides a message string and its type. You can specify the message string in plain text or in Speech Synthesis Markup Language (SSML).

(dict) --
The message object that provides the message text and its type.

contentType (string) --
The content type of the message string.

content (string) --
The text of the message.

groupNumber (integer) --
Identifies the message group that the message belongs to. When a group is assigned to a message, Amazon Lex returns one message from each group in the response.





maxAttempts (integer) --
The number of times to prompt the user for information.

responseCard (string) --
A response card. Amazon Lex uses this prompt at runtime, in the PostText API response. It substitutes session attributes and slot values for placeholders in the response card. For more information, see  ex-resp-card .



abortStatement (dict) --
The message that Amazon Lex uses to abort a conversation. For more information, see  PutBot .

messages (list) --
A collection of message objects.

(dict) --
The message object that provides the message text and its type.

contentType (string) --
The content type of the message string.

content (string) --
The text of the message.

groupNumber (integer) --
Identifies the message group that the message belongs to. When a group is assigned to a message, Amazon Lex returns one message from each group in the response.





responseCard (string) --
At runtime, if the client is using the PostText API, Amazon Lex includes the response card in the response. It substitutes all of the session attributes and slot values for placeholders in the response card.



status (string) --
When you send a request to create or update a bot, Amazon Lex sets the status response element to BUILDING . After Amazon Lex builds the bot, it sets status to READY . If Amazon Lex can\'t build the bot, it sets status to FAILED . Amazon Lex returns the reason for the failure in the failureReason response element.

failureReason (string) --
If status is FAILED , Amazon Lex provides the reason that it failed to build the bot.

lastUpdatedDate (datetime) --
The date when the $LATEST version of this bot was updated.

createdDate (datetime) --
The date when the bot version was created.

idleSessionTTLInSeconds (integer) --
The maximum time in seconds that Amazon Lex retains the data gathered in a conversation. For more information, see  PutBot .

voiceId (string) --
The Amazon Polly voice ID that Amazon Lex uses for voice interactions with the user.

checksum (string) --
Checksum identifying the version of the bot that was created.

version (string) --
The version of the bot.

locale (string) --
Specifies the target locale for the bot.

childDirected (boolean) --
For each Amazon Lex bot created with the Amazon Lex Model Building Service, you must specify whether your use of Amazon Lex is related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to the Children\'s Online Privacy Protection Act (COPPA) by specifying true or false in the childDirected field. By specifying true in the childDirected field, you confirm that your use of Amazon Lex is related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA. By specifying false in the childDirected field, you confirm that your use of Amazon Lex is not related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA. You may not specify a default value for the childDirected field that does not accurately reflect whether your use of Amazon Lex is related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA.
If your use of Amazon Lex relates to a website, program, or other application that is directed in whole or in part, to children under age 13, you must obtain any required verifiable parental consent under COPPA. For information regarding the use of Amazon Lex in connection with websites, programs, or other applications that are directed or targeted, in whole or in part, to children under age 13, see the Amazon Lex FAQ.

detectSentiment (boolean) --
Indicates whether utterances entered by the user should be sent to Amazon Comprehend for sentiment analysis.







Exceptions

LexModelBuildingService.Client.exceptions.NotFoundException
LexModelBuildingService.Client.exceptions.ConflictException
LexModelBuildingService.Client.exceptions.LimitExceededException
LexModelBuildingService.Client.exceptions.InternalFailureException
LexModelBuildingService.Client.exceptions.BadRequestException
LexModelBuildingService.Client.exceptions.PreconditionFailedException


    :return: {
        'name': 'string',
        'description': 'string',
        'intents': [
            {
                'intentName': 'string',
                'intentVersion': 'string'
            },
        ],
        'clarificationPrompt': {
            'messages': [
                {
                    'contentType': 'PlainText'|'SSML'|'CustomPayload',
                    'content': 'string',
                    'groupNumber': 123
                },
            ],
            'maxAttempts': 123,
            'responseCard': 'string'
        },
        'abortStatement': {
            'messages': [
                {
                    'contentType': 'PlainText'|'SSML'|'CustomPayload',
                    'content': 'string',
                    'groupNumber': 123
                },
            ],
            'responseCard': 'string'
        },
        'status': 'BUILDING'|'READY'|'READY_BASIC_TESTING'|'FAILED'|'NOT_BUILT',
        'failureReason': 'string',
        'lastUpdatedDate': datetime(2015, 1, 1),
        'createdDate': datetime(2015, 1, 1),
        'idleSessionTTLInSeconds': 123,
        'voiceId': 'string',
        'checksum': 'string',
        'version': 'string',
        'locale': 'en-US'|'en-GB'|'de-DE',
        'childDirected': True|False,
        'detectSentiment': True|False
    }
    
    
    :returns: 
    LexModelBuildingService.Client.exceptions.NotFoundException
    LexModelBuildingService.Client.exceptions.ConflictException
    LexModelBuildingService.Client.exceptions.LimitExceededException
    LexModelBuildingService.Client.exceptions.InternalFailureException
    LexModelBuildingService.Client.exceptions.BadRequestException
    LexModelBuildingService.Client.exceptions.PreconditionFailedException
    
    """
    pass

def create_intent_version(name=None, checksum=None):
    """
    Creates a new version of an intent based on the $LATEST version of the intent. If the $LATEST version of this intent hasn\'t changed since you last updated it, Amazon Lex doesn\'t create a new version. It returns the last version you created.
    When you create a version of an intent, Amazon Lex sets the version to 1. Subsequent versions increment by 1. For more information, see  versioning-intro .
    This operation requires permissions to perform the lex:CreateIntentVersion action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_intent_version(
        name='string',
        checksum='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name of the intent that you want to create a new version of. The name is case sensitive.\n

    :type checksum: string
    :param checksum: Checksum of the $LATEST version of the intent that should be used to create the new version. If you specify a checksum and the $LATEST version of the intent has a different checksum, Amazon Lex returns a PreconditionFailedException exception and doesn\'t publish a new version. If you don\'t specify a checksum, Amazon Lex publishes the $LATEST version.

    :rtype: dict

ReturnsResponse Syntax
{
    'name': 'string',
    'description': 'string',
    'slots': [
        {
            'name': 'string',
            'description': 'string',
            'slotConstraint': 'Required'|'Optional',
            'slotType': 'string',
            'slotTypeVersion': 'string',
            'valueElicitationPrompt': {
                'messages': [
                    {
                        'contentType': 'PlainText'|'SSML'|'CustomPayload',
                        'content': 'string',
                        'groupNumber': 123
                    },
                ],
                'maxAttempts': 123,
                'responseCard': 'string'
            },
            'priority': 123,
            'sampleUtterances': [
                'string',
            ],
            'responseCard': 'string',
            'obfuscationSetting': 'NONE'|'DEFAULT_OBFUSCATION'
        },
    ],
    'sampleUtterances': [
        'string',
    ],
    'confirmationPrompt': {
        'messages': [
            {
                'contentType': 'PlainText'|'SSML'|'CustomPayload',
                'content': 'string',
                'groupNumber': 123
            },
        ],
        'maxAttempts': 123,
        'responseCard': 'string'
    },
    'rejectionStatement': {
        'messages': [
            {
                'contentType': 'PlainText'|'SSML'|'CustomPayload',
                'content': 'string',
                'groupNumber': 123
            },
        ],
        'responseCard': 'string'
    },
    'followUpPrompt': {
        'prompt': {
            'messages': [
                {
                    'contentType': 'PlainText'|'SSML'|'CustomPayload',
                    'content': 'string',
                    'groupNumber': 123
                },
            ],
            'maxAttempts': 123,
            'responseCard': 'string'
        },
        'rejectionStatement': {
            'messages': [
                {
                    'contentType': 'PlainText'|'SSML'|'CustomPayload',
                    'content': 'string',
                    'groupNumber': 123
                },
            ],
            'responseCard': 'string'
        }
    },
    'conclusionStatement': {
        'messages': [
            {
                'contentType': 'PlainText'|'SSML'|'CustomPayload',
                'content': 'string',
                'groupNumber': 123
            },
        ],
        'responseCard': 'string'
    },
    'dialogCodeHook': {
        'uri': 'string',
        'messageVersion': 'string'
    },
    'fulfillmentActivity': {
        'type': 'ReturnIntent'|'CodeHook',
        'codeHook': {
            'uri': 'string',
            'messageVersion': 'string'
        }
    },
    'parentIntentSignature': 'string',
    'lastUpdatedDate': datetime(2015, 1, 1),
    'createdDate': datetime(2015, 1, 1),
    'version': 'string',
    'checksum': 'string'
}


Response Structure

(dict) --

name (string) --
The name of the intent.

description (string) --
A description of the intent.

slots (list) --
An array of slot types that defines the information required to fulfill the intent.

(dict) --
Identifies the version of a specific slot.

name (string) --
The name of the slot.

description (string) --
A description of the slot.

slotConstraint (string) --
Specifies whether the slot is required or optional.

slotType (string) --
The type of the slot, either a custom slot type that you defined or one of the built-in slot types.

slotTypeVersion (string) --
The version of the slot type.

valueElicitationPrompt (dict) --
The prompt that Amazon Lex uses to elicit the slot value from the user.

messages (list) --
An array of objects, each of which provides a message string and its type. You can specify the message string in plain text or in Speech Synthesis Markup Language (SSML).

(dict) --
The message object that provides the message text and its type.

contentType (string) --
The content type of the message string.

content (string) --
The text of the message.

groupNumber (integer) --
Identifies the message group that the message belongs to. When a group is assigned to a message, Amazon Lex returns one message from each group in the response.





maxAttempts (integer) --
The number of times to prompt the user for information.

responseCard (string) --
A response card. Amazon Lex uses this prompt at runtime, in the PostText API response. It substitutes session attributes and slot values for placeholders in the response card. For more information, see  ex-resp-card .



priority (integer) --
Directs Lex the order in which to elicit this slot value from the user. For example, if the intent has two slots with priorities 1 and 2, AWS Lex first elicits a value for the slot with priority 1.
If multiple slots share the same priority, the order in which Lex elicits values is arbitrary.

sampleUtterances (list) --
If you know a specific pattern with which users might respond to an Amazon Lex request for a slot value, you can provide those utterances to improve accuracy. This is optional. In most cases, Amazon Lex is capable of understanding user utterances.

(string) --


responseCard (string) --
A set of possible responses for the slot type used by text-based clients. A user chooses an option from the response card, instead of using text to reply.

obfuscationSetting (string) --
Determines whether a slot is obfuscated in conversation logs and stored utterances. When you obfuscate a slot, the value is replaced by the slot name in curly braces ({}). For example, if the slot name is "full_name", obfuscated values are replaced with "{full_name}". For more information, see Slot Obfuscation .





sampleUtterances (list) --
An array of sample utterances configured for the intent.

(string) --


confirmationPrompt (dict) --
If defined, the prompt that Amazon Lex uses to confirm the user\'s intent before fulfilling it.

messages (list) --
An array of objects, each of which provides a message string and its type. You can specify the message string in plain text or in Speech Synthesis Markup Language (SSML).

(dict) --
The message object that provides the message text and its type.

contentType (string) --
The content type of the message string.

content (string) --
The text of the message.

groupNumber (integer) --
Identifies the message group that the message belongs to. When a group is assigned to a message, Amazon Lex returns one message from each group in the response.





maxAttempts (integer) --
The number of times to prompt the user for information.

responseCard (string) --
A response card. Amazon Lex uses this prompt at runtime, in the PostText API response. It substitutes session attributes and slot values for placeholders in the response card. For more information, see  ex-resp-card .



rejectionStatement (dict) --
If the user answers "no" to the question defined in confirmationPrompt , Amazon Lex responds with this statement to acknowledge that the intent was canceled.

messages (list) --
A collection of message objects.

(dict) --
The message object that provides the message text and its type.

contentType (string) --
The content type of the message string.

content (string) --
The text of the message.

groupNumber (integer) --
Identifies the message group that the message belongs to. When a group is assigned to a message, Amazon Lex returns one message from each group in the response.





responseCard (string) --
At runtime, if the client is using the PostText API, Amazon Lex includes the response card in the response. It substitutes all of the session attributes and slot values for placeholders in the response card.



followUpPrompt (dict) --
If defined, Amazon Lex uses this prompt to solicit additional user activity after the intent is fulfilled.

prompt (dict) --
Prompts for information from the user.

messages (list) --
An array of objects, each of which provides a message string and its type. You can specify the message string in plain text or in Speech Synthesis Markup Language (SSML).

(dict) --
The message object that provides the message text and its type.

contentType (string) --
The content type of the message string.

content (string) --
The text of the message.

groupNumber (integer) --
Identifies the message group that the message belongs to. When a group is assigned to a message, Amazon Lex returns one message from each group in the response.





maxAttempts (integer) --
The number of times to prompt the user for information.

responseCard (string) --
A response card. Amazon Lex uses this prompt at runtime, in the PostText API response. It substitutes session attributes and slot values for placeholders in the response card. For more information, see  ex-resp-card .



rejectionStatement (dict) --
If the user answers "no" to the question defined in the prompt field, Amazon Lex responds with this statement to acknowledge that the intent was canceled.

messages (list) --
A collection of message objects.

(dict) --
The message object that provides the message text and its type.

contentType (string) --
The content type of the message string.

content (string) --
The text of the message.

groupNumber (integer) --
Identifies the message group that the message belongs to. When a group is assigned to a message, Amazon Lex returns one message from each group in the response.





responseCard (string) --
At runtime, if the client is using the PostText API, Amazon Lex includes the response card in the response. It substitutes all of the session attributes and slot values for placeholders in the response card.





conclusionStatement (dict) --
After the Lambda function specified in the fulfillmentActivity field fulfills the intent, Amazon Lex conveys this statement to the user.

messages (list) --
A collection of message objects.

(dict) --
The message object that provides the message text and its type.

contentType (string) --
The content type of the message string.

content (string) --
The text of the message.

groupNumber (integer) --
Identifies the message group that the message belongs to. When a group is assigned to a message, Amazon Lex returns one message from each group in the response.





responseCard (string) --
At runtime, if the client is using the PostText API, Amazon Lex includes the response card in the response. It substitutes all of the session attributes and slot values for placeholders in the response card.



dialogCodeHook (dict) --
If defined, Amazon Lex invokes this Lambda function for each user input.

uri (string) --
The Amazon Resource Name (ARN) of the Lambda function.

messageVersion (string) --
The version of the request-response that you want Amazon Lex to use to invoke your Lambda function. For more information, see  using-lambda .



fulfillmentActivity (dict) --
Describes how the intent is fulfilled.

type (string) --
How the intent should be fulfilled, either by running a Lambda function or by returning the slot data to the client application.

codeHook (dict) --
A description of the Lambda function that is run to fulfill the intent.

uri (string) --
The Amazon Resource Name (ARN) of the Lambda function.

messageVersion (string) --
The version of the request-response that you want Amazon Lex to use to invoke your Lambda function. For more information, see  using-lambda .





parentIntentSignature (string) --
A unique identifier for a built-in intent.

lastUpdatedDate (datetime) --
The date that the intent was updated.

createdDate (datetime) --
The date that the intent was created.

version (string) --
The version number assigned to the new version of the intent.

checksum (string) --
Checksum of the intent version created.







Exceptions

LexModelBuildingService.Client.exceptions.NotFoundException
LexModelBuildingService.Client.exceptions.ConflictException
LexModelBuildingService.Client.exceptions.LimitExceededException
LexModelBuildingService.Client.exceptions.InternalFailureException
LexModelBuildingService.Client.exceptions.BadRequestException
LexModelBuildingService.Client.exceptions.PreconditionFailedException


    :return: {
        'name': 'string',
        'description': 'string',
        'slots': [
            {
                'name': 'string',
                'description': 'string',
                'slotConstraint': 'Required'|'Optional',
                'slotType': 'string',
                'slotTypeVersion': 'string',
                'valueElicitationPrompt': {
                    'messages': [
                        {
                            'contentType': 'PlainText'|'SSML'|'CustomPayload',
                            'content': 'string',
                            'groupNumber': 123
                        },
                    ],
                    'maxAttempts': 123,
                    'responseCard': 'string'
                },
                'priority': 123,
                'sampleUtterances': [
                    'string',
                ],
                'responseCard': 'string',
                'obfuscationSetting': 'NONE'|'DEFAULT_OBFUSCATION'
            },
        ],
        'sampleUtterances': [
            'string',
        ],
        'confirmationPrompt': {
            'messages': [
                {
                    'contentType': 'PlainText'|'SSML'|'CustomPayload',
                    'content': 'string',
                    'groupNumber': 123
                },
            ],
            'maxAttempts': 123,
            'responseCard': 'string'
        },
        'rejectionStatement': {
            'messages': [
                {
                    'contentType': 'PlainText'|'SSML'|'CustomPayload',
                    'content': 'string',
                    'groupNumber': 123
                },
            ],
            'responseCard': 'string'
        },
        'followUpPrompt': {
            'prompt': {
                'messages': [
                    {
                        'contentType': 'PlainText'|'SSML'|'CustomPayload',
                        'content': 'string',
                        'groupNumber': 123
                    },
                ],
                'maxAttempts': 123,
                'responseCard': 'string'
            },
            'rejectionStatement': {
                'messages': [
                    {
                        'contentType': 'PlainText'|'SSML'|'CustomPayload',
                        'content': 'string',
                        'groupNumber': 123
                    },
                ],
                'responseCard': 'string'
            }
        },
        'conclusionStatement': {
            'messages': [
                {
                    'contentType': 'PlainText'|'SSML'|'CustomPayload',
                    'content': 'string',
                    'groupNumber': 123
                },
            ],
            'responseCard': 'string'
        },
        'dialogCodeHook': {
            'uri': 'string',
            'messageVersion': 'string'
        },
        'fulfillmentActivity': {
            'type': 'ReturnIntent'|'CodeHook',
            'codeHook': {
                'uri': 'string',
                'messageVersion': 'string'
            }
        },
        'parentIntentSignature': 'string',
        'lastUpdatedDate': datetime(2015, 1, 1),
        'createdDate': datetime(2015, 1, 1),
        'version': 'string',
        'checksum': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_slot_type_version(name=None, checksum=None):
    """
    Creates a new version of a slot type based on the $LATEST version of the specified slot type. If the $LATEST version of this resource has not changed since the last version that you created, Amazon Lex doesn\'t create a new version. It returns the last version that you created.
    When you create a version of a slot type, Amazon Lex sets the version to 1. Subsequent versions increment by 1. For more information, see  versioning-intro .
    This operation requires permissions for the lex:CreateSlotTypeVersion action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_slot_type_version(
        name='string',
        checksum='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name of the slot type that you want to create a new version for. The name is case sensitive.\n

    :type checksum: string
    :param checksum: Checksum for the $LATEST version of the slot type that you want to publish. If you specify a checksum and the $LATEST version of the slot type has a different checksum, Amazon Lex returns a PreconditionFailedException exception and doesn\'t publish the new version. If you don\'t specify a checksum, Amazon Lex publishes the $LATEST version.

    :rtype: dict

ReturnsResponse Syntax
{
    'name': 'string',
    'description': 'string',
    'enumerationValues': [
        {
            'value': 'string',
            'synonyms': [
                'string',
            ]
        },
    ],
    'lastUpdatedDate': datetime(2015, 1, 1),
    'createdDate': datetime(2015, 1, 1),
    'version': 'string',
    'checksum': 'string',
    'valueSelectionStrategy': 'ORIGINAL_VALUE'|'TOP_RESOLUTION',
    'parentSlotTypeSignature': 'string',
    'slotTypeConfigurations': [
        {
            'regexConfiguration': {
                'pattern': 'string'
            }
        },
    ]
}


Response Structure

(dict) --

name (string) --
The name of the slot type.

description (string) --
A description of the slot type.

enumerationValues (list) --
A list of EnumerationValue objects that defines the values that the slot type can take.

(dict) --
Each slot type can have a set of values. Each enumeration value represents a value the slot type can take.
For example, a pizza ordering bot could have a slot type that specifies the type of crust that the pizza should have. The slot type could include the values

thick
thin
stuffed


value (string) --
The value of the slot type.

synonyms (list) --
Additional values related to the slot type value.

(string) --






lastUpdatedDate (datetime) --
The date that the slot type was updated. When you create a resource, the creation date and last update date are the same.

createdDate (datetime) --
The date that the slot type was created.

version (string) --
The version assigned to the new slot type version.

checksum (string) --
Checksum of the $LATEST version of the slot type.

valueSelectionStrategy (string) --
The strategy that Amazon Lex uses to determine the value of the slot. For more information, see  PutSlotType .

parentSlotTypeSignature (string) --
The built-in slot type used a the parent of the slot type.

slotTypeConfigurations (list) --
Configuration information that extends the parent built-in slot type.

(dict) --
Provides configuration information for a slot type.

regexConfiguration (dict) --
A regular expression used to validate the value of a slot.

pattern (string) --
A regular expression used to validate the value of a slot.
Use a standard regular expression. Amazon Lex supports the following characters in the regular expression:

A-Z, a-z
0-9
Unicode characters ("u<Unicode>")

Represent Unicode characters with four digits, for example "u0041" or "u005A".
The following regular expression operators are not supported:

Infinite repeaters: *, +, or {x,} with no upper bound.
Wild card (.)














Exceptions

LexModelBuildingService.Client.exceptions.NotFoundException
LexModelBuildingService.Client.exceptions.ConflictException
LexModelBuildingService.Client.exceptions.LimitExceededException
LexModelBuildingService.Client.exceptions.InternalFailureException
LexModelBuildingService.Client.exceptions.BadRequestException
LexModelBuildingService.Client.exceptions.PreconditionFailedException


    :return: {
        'name': 'string',
        'description': 'string',
        'enumerationValues': [
            {
                'value': 'string',
                'synonyms': [
                    'string',
                ]
            },
        ],
        'lastUpdatedDate': datetime(2015, 1, 1),
        'createdDate': datetime(2015, 1, 1),
        'version': 'string',
        'checksum': 'string',
        'valueSelectionStrategy': 'ORIGINAL_VALUE'|'TOP_RESOLUTION',
        'parentSlotTypeSignature': 'string',
        'slotTypeConfigurations': [
            {
                'regexConfiguration': {
                    'pattern': 'string'
                }
            },
        ]
    }
    
    
    :returns: 
    thick
    thin
    stuffed
    
    """
    pass

def delete_bot(name=None):
    """
    Deletes all versions of the bot, including the $LATEST version. To delete a specific version of the bot, use the  DeleteBotVersion operation. The DeleteBot operation doesn\'t immediately remove the bot schema. Instead, it is marked for deletion and removed later.
    Amazon Lex stores utterances indefinitely for improving the ability of your bot to respond to user inputs. These utterances are not removed when the bot is deleted. To remove the utterances, use the  DeleteUtterances operation.
    If a bot has an alias, you can\'t delete it. Instead, the DeleteBot operation returns a ResourceInUseException exception that includes a reference to the alias that refers to the bot. To remove the reference to the bot, delete the alias. If you get the same exception again, delete the referring alias until the DeleteBot operation is successful.
    This operation requires permissions for the lex:DeleteBot action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_bot(
        name='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name of the bot. The name is case sensitive.\n

    """
    pass

def delete_bot_alias(name=None, botName=None):
    """
    Deletes an alias for the specified bot.
    You can\'t delete an alias that is used in the association between a bot and a messaging channel. If an alias is used in a channel association, the DeleteBot operation returns a ResourceInUseException exception that includes a reference to the channel association that refers to the bot. You can remove the reference to the alias by deleting the channel association. If you get the same exception again, delete the referring association until the DeleteBotAlias operation is successful.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_bot_alias(
        name='string',
        botName='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name of the alias to delete. The name is case sensitive.\n

    :type botName: string
    :param botName: [REQUIRED]\nThe name of the bot that the alias points to.\n

    :returns: 
    LexModelBuildingService.Client.exceptions.NotFoundException
    LexModelBuildingService.Client.exceptions.ConflictException
    LexModelBuildingService.Client.exceptions.LimitExceededException
    LexModelBuildingService.Client.exceptions.InternalFailureException
    LexModelBuildingService.Client.exceptions.BadRequestException
    LexModelBuildingService.Client.exceptions.ResourceInUseException
    
    """
    pass

def delete_bot_channel_association(name=None, botName=None, botAlias=None):
    """
    Deletes the association between an Amazon Lex bot and a messaging platform.
    This operation requires permission for the lex:DeleteBotChannelAssociation action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_bot_channel_association(
        name='string',
        botName='string',
        botAlias='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name of the association. The name is case sensitive.\n

    :type botName: string
    :param botName: [REQUIRED]\nThe name of the Amazon Lex bot.\n

    :type botAlias: string
    :param botAlias: [REQUIRED]\nAn alias that points to the specific version of the Amazon Lex bot to which this association is being made.\n

    :returns: 
    LexModelBuildingService.Client.exceptions.NotFoundException
    LexModelBuildingService.Client.exceptions.ConflictException
    LexModelBuildingService.Client.exceptions.LimitExceededException
    LexModelBuildingService.Client.exceptions.InternalFailureException
    LexModelBuildingService.Client.exceptions.BadRequestException
    
    """
    pass

def delete_bot_version(name=None, version=None):
    """
    Deletes a specific version of a bot. To delete all versions of a bot, use the  DeleteBot operation.
    This operation requires permissions for the lex:DeleteBotVersion action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_bot_version(
        name='string',
        version='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name of the bot.\n

    :type version: string
    :param version: [REQUIRED]\nThe version of the bot to delete. You cannot delete the $LATEST version of the bot. To delete the $LATEST version, use the DeleteBot operation.\n

    :returns: 
    LexModelBuildingService.Client.exceptions.NotFoundException
    LexModelBuildingService.Client.exceptions.ConflictException
    LexModelBuildingService.Client.exceptions.LimitExceededException
    LexModelBuildingService.Client.exceptions.InternalFailureException
    LexModelBuildingService.Client.exceptions.BadRequestException
    LexModelBuildingService.Client.exceptions.ResourceInUseException
    
    """
    pass

def delete_intent(name=None):
    """
    Deletes all versions of the intent, including the $LATEST version. To delete a specific version of the intent, use the  DeleteIntentVersion operation.
    You can delete a version of an intent only if it is not referenced. To delete an intent that is referred to in one or more bots (see  how-it-works ), you must remove those references first.
    This operation requires permission for the lex:DeleteIntent action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_intent(
        name='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name of the intent. The name is case sensitive.\n

    """
    pass

def delete_intent_version(name=None, version=None):
    """
    Deletes a specific version of an intent. To delete all versions of a intent, use the  DeleteIntent operation.
    This operation requires permissions for the lex:DeleteIntentVersion action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_intent_version(
        name='string',
        version='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name of the intent.\n

    :type version: string
    :param version: [REQUIRED]\nThe version of the intent to delete. You cannot delete the $LATEST version of the intent. To delete the $LATEST version, use the DeleteIntent operation.\n

    :returns: 
    LexModelBuildingService.Client.exceptions.NotFoundException
    LexModelBuildingService.Client.exceptions.ConflictException
    LexModelBuildingService.Client.exceptions.LimitExceededException
    LexModelBuildingService.Client.exceptions.InternalFailureException
    LexModelBuildingService.Client.exceptions.BadRequestException
    LexModelBuildingService.Client.exceptions.ResourceInUseException
    
    """
    pass

def delete_slot_type(name=None):
    """
    Deletes all versions of the slot type, including the $LATEST version. To delete a specific version of the slot type, use the  DeleteSlotTypeVersion operation.
    You can delete a version of a slot type only if it is not referenced. To delete a slot type that is referred to in one or more intents, you must remove those references first.
    This operation requires permission for the lex:DeleteSlotType action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_slot_type(
        name='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name of the slot type. The name is case sensitive.\n

    """
    pass

def delete_slot_type_version(name=None, version=None):
    """
    Deletes a specific version of a slot type. To delete all versions of a slot type, use the  DeleteSlotType operation.
    This operation requires permissions for the lex:DeleteSlotTypeVersion action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_slot_type_version(
        name='string',
        version='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name of the slot type.\n

    :type version: string
    :param version: [REQUIRED]\nThe version of the slot type to delete. You cannot delete the $LATEST version of the slot type. To delete the $LATEST version, use the DeleteSlotType operation.\n

    :returns: 
    LexModelBuildingService.Client.exceptions.NotFoundException
    LexModelBuildingService.Client.exceptions.ConflictException
    LexModelBuildingService.Client.exceptions.LimitExceededException
    LexModelBuildingService.Client.exceptions.InternalFailureException
    LexModelBuildingService.Client.exceptions.BadRequestException
    LexModelBuildingService.Client.exceptions.ResourceInUseException
    
    """
    pass

def delete_utterances(botName=None, userId=None):
    """
    Deletes stored utterances.
    Amazon Lex stores the utterances that users send to your bot. Utterances are stored for 15 days for use with the  GetUtterancesView operation, and then stored indefinitely for use in improving the ability of your bot to respond to user input.
    Use the DeleteUtterances operation to manually delete stored utterances for a specific user. When you use the DeleteUtterances operation, utterances stored for improving your bot\'s ability to respond to user input are deleted immediately. Utterances stored for use with the GetUtterancesView operation are deleted after 15 days.
    This operation requires permissions for the lex:DeleteUtterances action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_utterances(
        botName='string',
        userId='string'
    )
    
    
    :type botName: string
    :param botName: [REQUIRED]\nThe name of the bot that stored the utterances.\n

    :type userId: string
    :param userId: [REQUIRED]\nThe unique identifier for the user that made the utterances. This is the user ID that was sent in the PostContent or PostText operation request that contained the utterance.\n

    :returns: 
    LexModelBuildingService.Client.exceptions.NotFoundException
    LexModelBuildingService.Client.exceptions.LimitExceededException
    LexModelBuildingService.Client.exceptions.InternalFailureException
    LexModelBuildingService.Client.exceptions.BadRequestException
    
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

def get_bot(name=None, versionOrAlias=None):
    """
    Returns metadata information for a specific bot. You must provide the bot name and the bot version or alias.
    This operation requires permissions for the lex:GetBot action.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example shows how to get configuration information for a bot.
    Expected Output:
    
    :example: response = client.get_bot(
        name='string',
        versionOrAlias='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name of the bot. The name is case sensitive.\n

    :type versionOrAlias: string
    :param versionOrAlias: [REQUIRED]\nThe version or alias of the bot.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'name': 'string',
    'description': 'string',
    'intents': [
        {
            'intentName': 'string',
            'intentVersion': 'string'
        },
    ],
    'clarificationPrompt': {
        'messages': [
            {
                'contentType': 'PlainText'|'SSML'|'CustomPayload',
                'content': 'string',
                'groupNumber': 123
            },
        ],
        'maxAttempts': 123,
        'responseCard': 'string'
    },
    'abortStatement': {
        'messages': [
            {
                'contentType': 'PlainText'|'SSML'|'CustomPayload',
                'content': 'string',
                'groupNumber': 123
            },
        ],
        'responseCard': 'string'
    },
    'status': 'BUILDING'|'READY'|'READY_BASIC_TESTING'|'FAILED'|'NOT_BUILT',
    'failureReason': 'string',
    'lastUpdatedDate': datetime(2015, 1, 1),
    'createdDate': datetime(2015, 1, 1),
    'idleSessionTTLInSeconds': 123,
    'voiceId': 'string',
    'checksum': 'string',
    'version': 'string',
    'locale': 'en-US'|'en-GB'|'de-DE',
    'childDirected': True|False,
    'detectSentiment': True|False
}


Response Structure

(dict) --

name (string) --
The name of the bot.

description (string) --
A description of the bot.

intents (list) --
An array of intent objects. For more information, see  PutBot .

(dict) --
Identifies the specific version of an intent.

intentName (string) --
The name of the intent.

intentVersion (string) --
The version of the intent.





clarificationPrompt (dict) --
The message Amazon Lex uses when it doesn\'t understand the user\'s request. For more information, see  PutBot .

messages (list) --
An array of objects, each of which provides a message string and its type. You can specify the message string in plain text or in Speech Synthesis Markup Language (SSML).

(dict) --
The message object that provides the message text and its type.

contentType (string) --
The content type of the message string.

content (string) --
The text of the message.

groupNumber (integer) --
Identifies the message group that the message belongs to. When a group is assigned to a message, Amazon Lex returns one message from each group in the response.





maxAttempts (integer) --
The number of times to prompt the user for information.

responseCard (string) --
A response card. Amazon Lex uses this prompt at runtime, in the PostText API response. It substitutes session attributes and slot values for placeholders in the response card. For more information, see  ex-resp-card .



abortStatement (dict) --
The message that Amazon Lex returns when the user elects to end the conversation without completing it. For more information, see  PutBot .

messages (list) --
A collection of message objects.

(dict) --
The message object that provides the message text and its type.

contentType (string) --
The content type of the message string.

content (string) --
The text of the message.

groupNumber (integer) --
Identifies the message group that the message belongs to. When a group is assigned to a message, Amazon Lex returns one message from each group in the response.





responseCard (string) --
At runtime, if the client is using the PostText API, Amazon Lex includes the response card in the response. It substitutes all of the session attributes and slot values for placeholders in the response card.



status (string) --
The status of the bot.
When the status is BUILDING Amazon Lex is building the bot for testing and use.
If the status of the bot is READY_BASIC_TESTING , you can test the bot using the exact utterances specified in the bot\'s intents. When the bot is ready for full testing or to run, the status is READY .
If there was a problem with building the bot, the status is FAILED and the failureReason field explains why the bot did not build.
If the bot was saved but not built, the status is NOT_BUILT .

failureReason (string) --
If status is FAILED , Amazon Lex explains why it failed to build the bot.

lastUpdatedDate (datetime) --
The date that the bot was updated. When you create a resource, the creation date and last updated date are the same.

createdDate (datetime) --
The date that the bot was created.

idleSessionTTLInSeconds (integer) --
The maximum time in seconds that Amazon Lex retains the data gathered in a conversation. For more information, see  PutBot .

voiceId (string) --
The Amazon Polly voice ID that Amazon Lex uses for voice interaction with the user. For more information, see  PutBot .

checksum (string) --
Checksum of the bot used to identify a specific revision of the bot\'s $LATEST version.

version (string) --
The version of the bot. For a new bot, the version is always $LATEST .

locale (string) --
The target locale for the bot.

childDirected (boolean) --
For each Amazon Lex bot created with the Amazon Lex Model Building Service, you must specify whether your use of Amazon Lex is related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to the Children\'s Online Privacy Protection Act (COPPA) by specifying true or false in the childDirected field. By specifying true in the childDirected field, you confirm that your use of Amazon Lex is related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA. By specifying false in the childDirected field, you confirm that your use of Amazon Lex is not related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA. You may not specify a default value for the childDirected field that does not accurately reflect whether your use of Amazon Lex is related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA.
If your use of Amazon Lex relates to a website, program, or other application that is directed in whole or in part, to children under age 13, you must obtain any required verifiable parental consent under COPPA. For information regarding the use of Amazon Lex in connection with websites, programs, or other applications that are directed or targeted, in whole or in part, to children under age 13, see the Amazon Lex FAQ.

detectSentiment (boolean) --
Indicates whether user utterances should be sent to Amazon Comprehend for sentiment analysis.







Exceptions

LexModelBuildingService.Client.exceptions.NotFoundException
LexModelBuildingService.Client.exceptions.LimitExceededException
LexModelBuildingService.Client.exceptions.InternalFailureException
LexModelBuildingService.Client.exceptions.BadRequestException

Examples
This example shows how to get configuration information for a bot.
response = client.get_bot(
    name='DocOrderPizza',
    versionOrAlias='$LATEST',
)

print(response)


Expected Output:
{
    'version': '$LATEST',
    'name': 'DocOrderPizzaBot',
    'abortStatement': {
        'messages': [
            {
                'content': 'I don't understand. Can you try again?',
                'contentType': 'PlainText',
            },
            {
                'content': 'I'm sorry, I don't understand.',
                'contentType': 'PlainText',
            },
        ],
    },
    'checksum': '20172ee3-fa06-49b2-bbc5-667c090303e9',
    'childDirected': True,
    'clarificationPrompt': {
        'maxAttempts': 1,
        'messages': [
            {
                'content': 'I'm sorry, I didn't hear that. Can you repeate what you just said?',
                'contentType': 'PlainText',
            },
            {
                'content': 'Can you say that again?',
                'contentType': 'PlainText',
            },
        ],
    },
    'createdDate': 1494360160.133,
    'description': 'Orders a pizza from a local pizzeria.',
    'idleSessionTTLInSeconds': 300,
    'intents': [
        {
            'intentName': 'DocOrderPizza',
            'intentVersion': '$LATEST',
        },
    ],
    'lastUpdatedDate': 1494360160.133,
    'locale': 'en-US',
    'status': 'NOT_BUILT',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'name': 'string',
        'description': 'string',
        'intents': [
            {
                'intentName': 'string',
                'intentVersion': 'string'
            },
        ],
        'clarificationPrompt': {
            'messages': [
                {
                    'contentType': 'PlainText'|'SSML'|'CustomPayload',
                    'content': 'string',
                    'groupNumber': 123
                },
            ],
            'maxAttempts': 123,
            'responseCard': 'string'
        },
        'abortStatement': {
            'messages': [
                {
                    'contentType': 'PlainText'|'SSML'|'CustomPayload',
                    'content': 'string',
                    'groupNumber': 123
                },
            ],
            'responseCard': 'string'
        },
        'status': 'BUILDING'|'READY'|'READY_BASIC_TESTING'|'FAILED'|'NOT_BUILT',
        'failureReason': 'string',
        'lastUpdatedDate': datetime(2015, 1, 1),
        'createdDate': datetime(2015, 1, 1),
        'idleSessionTTLInSeconds': 123,
        'voiceId': 'string',
        'checksum': 'string',
        'version': 'string',
        'locale': 'en-US'|'en-GB'|'de-DE',
        'childDirected': True|False,
        'detectSentiment': True|False
    }
    
    
    :returns: 
    LexModelBuildingService.Client.exceptions.NotFoundException
    LexModelBuildingService.Client.exceptions.LimitExceededException
    LexModelBuildingService.Client.exceptions.InternalFailureException
    LexModelBuildingService.Client.exceptions.BadRequestException
    
    """
    pass

def get_bot_alias(name=None, botName=None):
    """
    Returns information about an Amazon Lex bot alias. For more information about aliases, see  versioning-aliases .
    This operation requires permissions for the lex:GetBotAlias action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_bot_alias(
        name='string',
        botName='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name of the bot alias. The name is case sensitive.\n

    :type botName: string
    :param botName: [REQUIRED]\nThe name of the bot.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'name': 'string',
    'description': 'string',
    'botVersion': 'string',
    'botName': 'string',
    'lastUpdatedDate': datetime(2015, 1, 1),
    'createdDate': datetime(2015, 1, 1),
    'checksum': 'string',
    'conversationLogs': {
        'logSettings': [
            {
                'logType': 'AUDIO'|'TEXT',
                'destination': 'CLOUDWATCH_LOGS'|'S3',
                'kmsKeyArn': 'string',
                'resourceArn': 'string',
                'resourcePrefix': 'string'
            },
        ],
        'iamRoleArn': 'string'
    }
}


Response Structure

(dict) --

name (string) --
The name of the bot alias.

description (string) --
A description of the bot alias.

botVersion (string) --
The version of the bot that the alias points to.

botName (string) --
The name of the bot that the alias points to.

lastUpdatedDate (datetime) --
The date that the bot alias was updated. When you create a resource, the creation date and the last updated date are the same.

createdDate (datetime) --
The date that the bot alias was created.

checksum (string) --
Checksum of the bot alias.

conversationLogs (dict) --
The settings that determine how Amazon Lex uses conversation logs for the alias.

logSettings (list) --
The settings for your conversation logs. You can log text, audio, or both.

(dict) --
The settings for conversation logs.

logType (string) --
The type of logging that is enabled.

destination (string) --
The destination where logs are delivered.

kmsKeyArn (string) --
The Amazon Resource Name (ARN) of the key used to encrypt audio logs in an S3 bucket.

resourceArn (string) --
The Amazon Resource Name (ARN) of the CloudWatch Logs log group or S3 bucket where the logs are delivered.

resourcePrefix (string) --
The resource prefix is the first part of the S3 object key within the S3 bucket that you specified to contain audio logs. For CloudWatch Logs it is the prefix of the log stream name within the log group that you specified.





iamRoleArn (string) --
The Amazon Resource Name (ARN) of the IAM role used to write your logs to CloudWatch Logs or an S3 bucket.









Exceptions

LexModelBuildingService.Client.exceptions.NotFoundException
LexModelBuildingService.Client.exceptions.LimitExceededException
LexModelBuildingService.Client.exceptions.InternalFailureException
LexModelBuildingService.Client.exceptions.BadRequestException


    :return: {
        'name': 'string',
        'description': 'string',
        'botVersion': 'string',
        'botName': 'string',
        'lastUpdatedDate': datetime(2015, 1, 1),
        'createdDate': datetime(2015, 1, 1),
        'checksum': 'string',
        'conversationLogs': {
            'logSettings': [
                {
                    'logType': 'AUDIO'|'TEXT',
                    'destination': 'CLOUDWATCH_LOGS'|'S3',
                    'kmsKeyArn': 'string',
                    'resourceArn': 'string',
                    'resourcePrefix': 'string'
                },
            ],
            'iamRoleArn': 'string'
        }
    }
    
    
    :returns: 
    LexModelBuildingService.Client.exceptions.NotFoundException
    LexModelBuildingService.Client.exceptions.LimitExceededException
    LexModelBuildingService.Client.exceptions.InternalFailureException
    LexModelBuildingService.Client.exceptions.BadRequestException
    
    """
    pass

def get_bot_aliases(botName=None, nextToken=None, maxResults=None, nameContains=None):
    """
    Returns a list of aliases for a specified Amazon Lex bot.
    This operation requires permissions for the lex:GetBotAliases action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_bot_aliases(
        botName='string',
        nextToken='string',
        maxResults=123,
        nameContains='string'
    )
    
    
    :type botName: string
    :param botName: [REQUIRED]\nThe name of the bot.\n

    :type nextToken: string
    :param nextToken: A pagination token for fetching the next page of aliases. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of aliases, specify the pagination token in the next request.

    :type maxResults: integer
    :param maxResults: The maximum number of aliases to return in the response. The default is 50. .

    :type nameContains: string
    :param nameContains: Substring to match in bot alias names. An alias will be returned if any part of its name matches the substring. For example, 'xyz' matches both 'xyzabc' and 'abcxyz.'

    :rtype: dict

ReturnsResponse Syntax
{
    'BotAliases': [
        {
            'name': 'string',
            'description': 'string',
            'botVersion': 'string',
            'botName': 'string',
            'lastUpdatedDate': datetime(2015, 1, 1),
            'createdDate': datetime(2015, 1, 1),
            'checksum': 'string',
            'conversationLogs': {
                'logSettings': [
                    {
                        'logType': 'AUDIO'|'TEXT',
                        'destination': 'CLOUDWATCH_LOGS'|'S3',
                        'kmsKeyArn': 'string',
                        'resourceArn': 'string',
                        'resourcePrefix': 'string'
                    },
                ],
                'iamRoleArn': 'string'
            }
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

BotAliases (list) --
An array of BotAliasMetadata objects, each describing a bot alias.

(dict) --
Provides information about a bot alias.

name (string) --
The name of the bot alias.

description (string) --
A description of the bot alias.

botVersion (string) --
The version of the Amazon Lex bot to which the alias points.

botName (string) --
The name of the bot to which the alias points.

lastUpdatedDate (datetime) --
The date that the bot alias was updated. When you create a resource, the creation date and last updated date are the same.

createdDate (datetime) --
The date that the bot alias was created.

checksum (string) --
Checksum of the bot alias.

conversationLogs (dict) --
Settings that determine how Amazon Lex uses conversation logs for the alias.

logSettings (list) --
The settings for your conversation logs. You can log text, audio, or both.

(dict) --
The settings for conversation logs.

logType (string) --
The type of logging that is enabled.

destination (string) --
The destination where logs are delivered.

kmsKeyArn (string) --
The Amazon Resource Name (ARN) of the key used to encrypt audio logs in an S3 bucket.

resourceArn (string) --
The Amazon Resource Name (ARN) of the CloudWatch Logs log group or S3 bucket where the logs are delivered.

resourcePrefix (string) --
The resource prefix is the first part of the S3 object key within the S3 bucket that you specified to contain audio logs. For CloudWatch Logs it is the prefix of the log stream name within the log group that you specified.





iamRoleArn (string) --
The Amazon Resource Name (ARN) of the IAM role used to write your logs to CloudWatch Logs or an S3 bucket.







nextToken (string) --
A pagination token for fetching next page of aliases. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of aliases, specify the pagination token in the next request.







Exceptions

LexModelBuildingService.Client.exceptions.LimitExceededException
LexModelBuildingService.Client.exceptions.InternalFailureException
LexModelBuildingService.Client.exceptions.BadRequestException


    :return: {
        'BotAliases': [
            {
                'name': 'string',
                'description': 'string',
                'botVersion': 'string',
                'botName': 'string',
                'lastUpdatedDate': datetime(2015, 1, 1),
                'createdDate': datetime(2015, 1, 1),
                'checksum': 'string',
                'conversationLogs': {
                    'logSettings': [
                        {
                            'logType': 'AUDIO'|'TEXT',
                            'destination': 'CLOUDWATCH_LOGS'|'S3',
                            'kmsKeyArn': 'string',
                            'resourceArn': 'string',
                            'resourcePrefix': 'string'
                        },
                    ],
                    'iamRoleArn': 'string'
                }
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    LexModelBuildingService.Client.exceptions.LimitExceededException
    LexModelBuildingService.Client.exceptions.InternalFailureException
    LexModelBuildingService.Client.exceptions.BadRequestException
    
    """
    pass

def get_bot_channel_association(name=None, botName=None, botAlias=None):
    """
    Returns information about the association between an Amazon Lex bot and a messaging platform.
    This operation requires permissions for the lex:GetBotChannelAssociation action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_bot_channel_association(
        name='string',
        botName='string',
        botAlias='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name of the association between the bot and the channel. The name is case sensitive.\n

    :type botName: string
    :param botName: [REQUIRED]\nThe name of the Amazon Lex bot.\n

    :type botAlias: string
    :param botAlias: [REQUIRED]\nAn alias pointing to the specific version of the Amazon Lex bot to which this association is being made.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'name': 'string',
    'description': 'string',
    'botAlias': 'string',
    'botName': 'string',
    'createdDate': datetime(2015, 1, 1),
    'type': 'Facebook'|'Slack'|'Twilio-Sms'|'Kik',
    'botConfiguration': {
        'string': 'string'
    },
    'status': 'IN_PROGRESS'|'CREATED'|'FAILED',
    'failureReason': 'string'
}


Response Structure

(dict) --

name (string) --
The name of the association between the bot and the channel.

description (string) --
A description of the association between the bot and the channel.

botAlias (string) --
An alias pointing to the specific version of the Amazon Lex bot to which this association is being made.

botName (string) --
The name of the Amazon Lex bot.

createdDate (datetime) --
The date that the association between the bot and the channel was created.

type (string) --
The type of the messaging platform.

botConfiguration (dict) --
Provides information that the messaging platform needs to communicate with the Amazon Lex bot.

(string) --
(string) --




status (string) --
The status of the bot channel.

CREATED - The channel has been created and is ready for use.
IN_PROGRESS - Channel creation is in progress.
FAILED - There was an error creating the channel. For information about the reason for the failure, see the failureReason field.


failureReason (string) --
If status is FAILED , Amazon Lex provides the reason that it failed to create the association.







Exceptions

LexModelBuildingService.Client.exceptions.NotFoundException
LexModelBuildingService.Client.exceptions.LimitExceededException
LexModelBuildingService.Client.exceptions.InternalFailureException
LexModelBuildingService.Client.exceptions.BadRequestException


    :return: {
        'name': 'string',
        'description': 'string',
        'botAlias': 'string',
        'botName': 'string',
        'createdDate': datetime(2015, 1, 1),
        'type': 'Facebook'|'Slack'|'Twilio-Sms'|'Kik',
        'botConfiguration': {
            'string': 'string'
        },
        'status': 'IN_PROGRESS'|'CREATED'|'FAILED',
        'failureReason': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def get_bot_channel_associations(botName=None, botAlias=None, nextToken=None, maxResults=None, nameContains=None):
    """
    Returns a list of all of the channels associated with the specified bot.
    The GetBotChannelAssociations operation requires permissions for the lex:GetBotChannelAssociations action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_bot_channel_associations(
        botName='string',
        botAlias='string',
        nextToken='string',
        maxResults=123,
        nameContains='string'
    )
    
    
    :type botName: string
    :param botName: [REQUIRED]\nThe name of the Amazon Lex bot in the association.\n

    :type botAlias: string
    :param botAlias: [REQUIRED]\nAn alias pointing to the specific version of the Amazon Lex bot to which this association is being made.\n

    :type nextToken: string
    :param nextToken: A pagination token for fetching the next page of associations. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of associations, specify the pagination token in the next request.

    :type maxResults: integer
    :param maxResults: The maximum number of associations to return in the response. The default is 50.

    :type nameContains: string
    :param nameContains: Substring to match in channel association names. An association will be returned if any part of its name matches the substring. For example, 'xyz' matches both 'xyzabc' and 'abcxyz.' To return all bot channel associations, use a hyphen ('-') as the nameContains parameter.

    :rtype: dict

ReturnsResponse Syntax
{
    'botChannelAssociations': [
        {
            'name': 'string',
            'description': 'string',
            'botAlias': 'string',
            'botName': 'string',
            'createdDate': datetime(2015, 1, 1),
            'type': 'Facebook'|'Slack'|'Twilio-Sms'|'Kik',
            'botConfiguration': {
                'string': 'string'
            },
            'status': 'IN_PROGRESS'|'CREATED'|'FAILED',
            'failureReason': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

botChannelAssociations (list) --
An array of objects, one for each association, that provides information about the Amazon Lex bot and its association with the channel.

(dict) --
Represents an association between an Amazon Lex bot and an external messaging platform.

name (string) --
The name of the association between the bot and the channel.

description (string) --
A text description of the association you are creating.

botAlias (string) --
An alias pointing to the specific version of the Amazon Lex bot to which this association is being made.

botName (string) --
The name of the Amazon Lex bot to which this association is being made.

Note
Currently, Amazon Lex supports associations with Facebook and Slack, and Twilio.


createdDate (datetime) --
The date that the association between the Amazon Lex bot and the channel was created.

type (string) --
Specifies the type of association by indicating the type of channel being established between the Amazon Lex bot and the external messaging platform.

botConfiguration (dict) --
Provides information necessary to communicate with the messaging platform.

(string) --
(string) --




status (string) --
The status of the bot channel.

CREATED - The channel has been created and is ready for use.
IN_PROGRESS - Channel creation is in progress.
FAILED - There was an error creating the channel. For information about the reason for the failure, see the failureReason field.


failureReason (string) --
If status is FAILED , Amazon Lex provides the reason that it failed to create the association.





nextToken (string) --
A pagination token that fetches the next page of associations. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of associations, specify the pagination token in the next request.







Exceptions

LexModelBuildingService.Client.exceptions.LimitExceededException
LexModelBuildingService.Client.exceptions.InternalFailureException
LexModelBuildingService.Client.exceptions.BadRequestException


    :return: {
        'botChannelAssociations': [
            {
                'name': 'string',
                'description': 'string',
                'botAlias': 'string',
                'botName': 'string',
                'createdDate': datetime(2015, 1, 1),
                'type': 'Facebook'|'Slack'|'Twilio-Sms'|'Kik',
                'botConfiguration': {
                    'string': 'string'
                },
                'status': 'IN_PROGRESS'|'CREATED'|'FAILED',
                'failureReason': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def get_bot_versions(name=None, nextToken=None, maxResults=None):
    """
    Gets information about all of the versions of a bot.
    The GetBotVersions operation returns a BotMetadata object for each version of a bot. For example, if a bot has three numbered versions, the GetBotVersions operation returns four BotMetadata objects in the response, one for each numbered version and one for the $LATEST version.
    The GetBotVersions operation always returns at least one version, the $LATEST version.
    This operation requires permissions for the lex:GetBotVersions action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_bot_versions(
        name='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name of the bot for which versions should be returned.\n

    :type nextToken: string
    :param nextToken: A pagination token for fetching the next page of bot versions. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of versions, specify the pagination token in the next request.

    :type maxResults: integer
    :param maxResults: The maximum number of bot versions to return in the response. The default is 10.

    :rtype: dict

ReturnsResponse Syntax
{
    'bots': [
        {
            'name': 'string',
            'description': 'string',
            'status': 'BUILDING'|'READY'|'READY_BASIC_TESTING'|'FAILED'|'NOT_BUILT',
            'lastUpdatedDate': datetime(2015, 1, 1),
            'createdDate': datetime(2015, 1, 1),
            'version': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

bots (list) --
An array of BotMetadata objects, one for each numbered version of the bot plus one for the $LATEST version.

(dict) --
Provides information about a bot. .

name (string) --
The name of the bot.

description (string) --
A description of the bot.

status (string) --
The status of the bot.

lastUpdatedDate (datetime) --
The date that the bot was updated. When you create a bot, the creation date and last updated date are the same.

createdDate (datetime) --
The date that the bot was created.

version (string) --
The version of the bot. For a new bot, the version is always $LATEST .





nextToken (string) --
A pagination token for fetching the next page of bot versions. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of versions, specify the pagination token in the next request.







Exceptions

LexModelBuildingService.Client.exceptions.NotFoundException
LexModelBuildingService.Client.exceptions.LimitExceededException
LexModelBuildingService.Client.exceptions.InternalFailureException
LexModelBuildingService.Client.exceptions.BadRequestException


    :return: {
        'bots': [
            {
                'name': 'string',
                'description': 'string',
                'status': 'BUILDING'|'READY'|'READY_BASIC_TESTING'|'FAILED'|'NOT_BUILT',
                'lastUpdatedDate': datetime(2015, 1, 1),
                'createdDate': datetime(2015, 1, 1),
                'version': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    LexModelBuildingService.Client.exceptions.NotFoundException
    LexModelBuildingService.Client.exceptions.LimitExceededException
    LexModelBuildingService.Client.exceptions.InternalFailureException
    LexModelBuildingService.Client.exceptions.BadRequestException
    
    """
    pass

def get_bots(nextToken=None, maxResults=None, nameContains=None):
    """
    Returns bot information as follows:
    This operation requires permission for the lex:GetBots action.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example shows how to get a list of all of the bots in your account.
    Expected Output:
    
    :example: response = client.get_bots(
        nextToken='string',
        maxResults=123,
        nameContains='string'
    )
    
    
    :type nextToken: string
    :param nextToken: A pagination token that fetches the next page of bots. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of bots, specify the pagination token in the next request.

    :type maxResults: integer
    :param maxResults: The maximum number of bots to return in the response that the request will return. The default is 10.

    :type nameContains: string
    :param nameContains: Substring to match in bot names. A bot will be returned if any part of its name matches the substring. For example, 'xyz' matches both 'xyzabc' and 'abcxyz.'

    :rtype: dict

ReturnsResponse Syntax
{
    'bots': [
        {
            'name': 'string',
            'description': 'string',
            'status': 'BUILDING'|'READY'|'READY_BASIC_TESTING'|'FAILED'|'NOT_BUILT',
            'lastUpdatedDate': datetime(2015, 1, 1),
            'createdDate': datetime(2015, 1, 1),
            'version': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

bots (list) --
An array of botMetadata objects, with one entry for each bot.

(dict) --
Provides information about a bot. .

name (string) --
The name of the bot.

description (string) --
A description of the bot.

status (string) --
The status of the bot.

lastUpdatedDate (datetime) --
The date that the bot was updated. When you create a bot, the creation date and last updated date are the same.

createdDate (datetime) --
The date that the bot was created.

version (string) --
The version of the bot. For a new bot, the version is always $LATEST .





nextToken (string) --
If the response is truncated, it includes a pagination token that you can specify in your next request to fetch the next page of bots.







Exceptions

LexModelBuildingService.Client.exceptions.NotFoundException
LexModelBuildingService.Client.exceptions.LimitExceededException
LexModelBuildingService.Client.exceptions.InternalFailureException
LexModelBuildingService.Client.exceptions.BadRequestException

Examples
This example shows how to get a list of all of the bots in your account.
response = client.get_bots(
    maxResults=5,
    nextToken='',
)

print(response)


Expected Output:
{
    'bots': [
        {
            'version': '$LATEST',
            'name': 'DocOrderPizzaBot',
            'createdDate': 1494360160.133,
            'description': 'Orders a pizza from a local pizzeria.',
            'lastUpdatedDate': 1494360160.133,
            'status': 'NOT_BUILT',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'bots': [
            {
                'name': 'string',
                'description': 'string',
                'status': 'BUILDING'|'READY'|'READY_BASIC_TESTING'|'FAILED'|'NOT_BUILT',
                'lastUpdatedDate': datetime(2015, 1, 1),
                'createdDate': datetime(2015, 1, 1),
                'version': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    nextToken (string) -- A pagination token that fetches the next page of bots. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of bots, specify the pagination token in the next request.
    maxResults (integer) -- The maximum number of bots to return in the response that the request will return. The default is 10.
    nameContains (string) -- Substring to match in bot names. A bot will be returned if any part of its name matches the substring. For example, "xyz" matches both "xyzabc" and "abcxyz."
    
    """
    pass

def get_builtin_intent(signature=None):
    """
    Returns information about a built-in intent.
    This operation requires permission for the lex:GetBuiltinIntent action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_builtin_intent(
        signature='string'
    )
    
    
    :type signature: string
    :param signature: [REQUIRED]\nThe unique identifier for a built-in intent. To find the signature for an intent, see Standard Built-in Intents in the Alexa Skills Kit .\n

    :rtype: dict
ReturnsResponse Syntax{
    'signature': 'string',
    'supportedLocales': [
        'en-US'|'en-GB'|'de-DE',
    ],
    'slots': [
        {
            'name': 'string'
        },
    ]
}


Response Structure

(dict) --
signature (string) --The unique identifier for a built-in intent.

supportedLocales (list) --A list of locales that the intent supports.

(string) --


slots (list) --An array of BuiltinIntentSlot objects, one entry for each slot type in the intent.

(dict) --Provides information about a slot used in a built-in intent.

name (string) --A list of the slots defined for the intent.










Exceptions

LexModelBuildingService.Client.exceptions.NotFoundException
LexModelBuildingService.Client.exceptions.LimitExceededException
LexModelBuildingService.Client.exceptions.InternalFailureException
LexModelBuildingService.Client.exceptions.BadRequestException


    :return: {
        'signature': 'string',
        'supportedLocales': [
            'en-US'|'en-GB'|'de-DE',
        ],
        'slots': [
            {
                'name': 'string'
            },
        ]
    }
    
    
    :returns: 
    LexModelBuildingService.Client.exceptions.NotFoundException
    LexModelBuildingService.Client.exceptions.LimitExceededException
    LexModelBuildingService.Client.exceptions.InternalFailureException
    LexModelBuildingService.Client.exceptions.BadRequestException
    
    """
    pass

def get_builtin_intents(locale=None, signatureContains=None, nextToken=None, maxResults=None):
    """
    Gets a list of built-in intents that meet the specified criteria.
    This operation requires permission for the lex:GetBuiltinIntents action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_builtin_intents(
        locale='en-US'|'en-GB'|'de-DE',
        signatureContains='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type locale: string
    :param locale: A list of locales that the intent supports.

    :type signatureContains: string
    :param signatureContains: Substring to match in built-in intent signatures. An intent will be returned if any part of its signature matches the substring. For example, 'xyz' matches both 'xyzabc' and 'abcxyz.' To find the signature for an intent, see Standard Built-in Intents in the Alexa Skills Kit .

    :type nextToken: string
    :param nextToken: A pagination token that fetches the next page of intents. If this API call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of intents, use the pagination token in the next request.

    :type maxResults: integer
    :param maxResults: The maximum number of intents to return in the response. The default is 10.

    :rtype: dict

ReturnsResponse Syntax
{
    'intents': [
        {
            'signature': 'string',
            'supportedLocales': [
                'en-US'|'en-GB'|'de-DE',
            ]
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

intents (list) --
An array of builtinIntentMetadata objects, one for each intent in the response.

(dict) --
Provides metadata for a built-in intent.

signature (string) --
A unique identifier for the built-in intent. To find the signature for an intent, see Standard Built-in Intents in the Alexa Skills Kit .

supportedLocales (list) --
A list of identifiers for the locales that the intent supports.

(string) --






nextToken (string) --
A pagination token that fetches the next page of intents. If the response to this API call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of intents, specify the pagination token in the next request.







Exceptions

LexModelBuildingService.Client.exceptions.LimitExceededException
LexModelBuildingService.Client.exceptions.InternalFailureException
LexModelBuildingService.Client.exceptions.BadRequestException


    :return: {
        'intents': [
            {
                'signature': 'string',
                'supportedLocales': [
                    'en-US'|'en-GB'|'de-DE',
                ]
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_builtin_slot_types(locale=None, signatureContains=None, nextToken=None, maxResults=None):
    """
    Gets a list of built-in slot types that meet the specified criteria.
    For a list of built-in slot types, see Slot Type Reference in the Alexa Skills Kit .
    This operation requires permission for the lex:GetBuiltInSlotTypes action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_builtin_slot_types(
        locale='en-US'|'en-GB'|'de-DE',
        signatureContains='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type locale: string
    :param locale: A list of locales that the slot type supports.

    :type signatureContains: string
    :param signatureContains: Substring to match in built-in slot type signatures. A slot type will be returned if any part of its signature matches the substring. For example, 'xyz' matches both 'xyzabc' and 'abcxyz.'

    :type nextToken: string
    :param nextToken: A pagination token that fetches the next page of slot types. If the response to this API call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of slot types, specify the pagination token in the next request.

    :type maxResults: integer
    :param maxResults: The maximum number of slot types to return in the response. The default is 10.

    :rtype: dict

ReturnsResponse Syntax
{
    'slotTypes': [
        {
            'signature': 'string',
            'supportedLocales': [
                'en-US'|'en-GB'|'de-DE',
            ]
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

slotTypes (list) --
An array of BuiltInSlotTypeMetadata objects, one entry for each slot type returned.

(dict) --
Provides information about a built in slot type.

signature (string) --
A unique identifier for the built-in slot type. To find the signature for a slot type, see Slot Type Reference in the Alexa Skills Kit .

supportedLocales (list) --
A list of target locales for the slot.

(string) --






nextToken (string) --
If the response is truncated, the response includes a pagination token that you can use in your next request to fetch the next page of slot types.







Exceptions

LexModelBuildingService.Client.exceptions.LimitExceededException
LexModelBuildingService.Client.exceptions.InternalFailureException
LexModelBuildingService.Client.exceptions.BadRequestException


    :return: {
        'slotTypes': [
            {
                'signature': 'string',
                'supportedLocales': [
                    'en-US'|'en-GB'|'de-DE',
                ]
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_export(name=None, version=None, resourceType=None, exportType=None):
    """
    Exports the contents of a Amazon Lex resource in a specified format.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_export(
        name='string',
        version='string',
        resourceType='BOT'|'INTENT'|'SLOT_TYPE',
        exportType='ALEXA_SKILLS_KIT'|'LEX'
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name of the bot to export.\n

    :type version: string
    :param version: [REQUIRED]\nThe version of the bot to export.\n

    :type resourceType: string
    :param resourceType: [REQUIRED]\nThe type of resource to export.\n

    :type exportType: string
    :param exportType: [REQUIRED]\nThe format of the exported data.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'name': 'string',
    'version': 'string',
    'resourceType': 'BOT'|'INTENT'|'SLOT_TYPE',
    'exportType': 'ALEXA_SKILLS_KIT'|'LEX',
    'exportStatus': 'IN_PROGRESS'|'READY'|'FAILED',
    'failureReason': 'string',
    'url': 'string'
}


Response Structure

(dict) --

name (string) --
The name of the bot being exported.

version (string) --
The version of the bot being exported.

resourceType (string) --
The type of the exported resource.

exportType (string) --
The format of the exported data.

exportStatus (string) --
The status of the export.

IN_PROGRESS - The export is in progress.
READY - The export is complete.
FAILED - The export could not be completed.


failureReason (string) --
If status is FAILED , Amazon Lex provides the reason that it failed to export the resource.

url (string) --
An S3 pre-signed URL that provides the location of the exported resource. The exported resource is a ZIP archive that contains the exported resource in JSON format. The structure of the archive may change. Your code should not rely on the archive structure.







Exceptions

LexModelBuildingService.Client.exceptions.NotFoundException
LexModelBuildingService.Client.exceptions.LimitExceededException
LexModelBuildingService.Client.exceptions.InternalFailureException
LexModelBuildingService.Client.exceptions.BadRequestException


    :return: {
        'name': 'string',
        'version': 'string',
        'resourceType': 'BOT'|'INTENT'|'SLOT_TYPE',
        'exportType': 'ALEXA_SKILLS_KIT'|'LEX',
        'exportStatus': 'IN_PROGRESS'|'READY'|'FAILED',
        'failureReason': 'string',
        'url': 'string'
    }
    
    
    :returns: 
    IN_PROGRESS - The export is in progress.
    READY - The export is complete.
    FAILED - The export could not be completed.
    
    """
    pass

def get_import(importId=None):
    """
    Gets information about an import job started with the StartImport operation.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_import(
        importId='string'
    )
    
    
    :type importId: string
    :param importId: [REQUIRED]\nThe identifier of the import job information to return.\n

    :rtype: dict
ReturnsResponse Syntax{
    'name': 'string',
    'resourceType': 'BOT'|'INTENT'|'SLOT_TYPE',
    'mergeStrategy': 'OVERWRITE_LATEST'|'FAIL_ON_CONFLICT',
    'importId': 'string',
    'importStatus': 'IN_PROGRESS'|'COMPLETE'|'FAILED',
    'failureReason': [
        'string',
    ],
    'createdDate': datetime(2015, 1, 1)
}


Response Structure

(dict) --
name (string) --The name given to the import job.

resourceType (string) --The type of resource imported.

mergeStrategy (string) --The action taken when there was a conflict between an existing resource and a resource in the import file.

importId (string) --The identifier for the specific import job.

importStatus (string) --The status of the import job. If the status is FAILED , you can get the reason for the failure from the failureReason field.

failureReason (list) --A string that describes why an import job failed to complete.

(string) --


createdDate (datetime) --A timestamp for the date and time that the import job was created.






Exceptions

LexModelBuildingService.Client.exceptions.NotFoundException
LexModelBuildingService.Client.exceptions.LimitExceededException
LexModelBuildingService.Client.exceptions.InternalFailureException
LexModelBuildingService.Client.exceptions.BadRequestException


    :return: {
        'name': 'string',
        'resourceType': 'BOT'|'INTENT'|'SLOT_TYPE',
        'mergeStrategy': 'OVERWRITE_LATEST'|'FAIL_ON_CONFLICT',
        'importId': 'string',
        'importStatus': 'IN_PROGRESS'|'COMPLETE'|'FAILED',
        'failureReason': [
            'string',
        ],
        'createdDate': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    LexModelBuildingService.Client.exceptions.NotFoundException
    LexModelBuildingService.Client.exceptions.LimitExceededException
    LexModelBuildingService.Client.exceptions.InternalFailureException
    LexModelBuildingService.Client.exceptions.BadRequestException
    
    """
    pass

def get_intent(name=None, version=None):
    """
    Returns information about an intent. In addition to the intent name, you must specify the intent version.
    This operation requires permissions to perform the lex:GetIntent action.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example shows how to get information about an intent.
    Expected Output:
    
    :example: response = client.get_intent(
        name='string',
        version='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name of the intent. The name is case sensitive.\n

    :type version: string
    :param version: [REQUIRED]\nThe version of the intent.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'name': 'string',
    'description': 'string',
    'slots': [
        {
            'name': 'string',
            'description': 'string',
            'slotConstraint': 'Required'|'Optional',
            'slotType': 'string',
            'slotTypeVersion': 'string',
            'valueElicitationPrompt': {
                'messages': [
                    {
                        'contentType': 'PlainText'|'SSML'|'CustomPayload',
                        'content': 'string',
                        'groupNumber': 123
                    },
                ],
                'maxAttempts': 123,
                'responseCard': 'string'
            },
            'priority': 123,
            'sampleUtterances': [
                'string',
            ],
            'responseCard': 'string',
            'obfuscationSetting': 'NONE'|'DEFAULT_OBFUSCATION'
        },
    ],
    'sampleUtterances': [
        'string',
    ],
    'confirmationPrompt': {
        'messages': [
            {
                'contentType': 'PlainText'|'SSML'|'CustomPayload',
                'content': 'string',
                'groupNumber': 123
            },
        ],
        'maxAttempts': 123,
        'responseCard': 'string'
    },
    'rejectionStatement': {
        'messages': [
            {
                'contentType': 'PlainText'|'SSML'|'CustomPayload',
                'content': 'string',
                'groupNumber': 123
            },
        ],
        'responseCard': 'string'
    },
    'followUpPrompt': {
        'prompt': {
            'messages': [
                {
                    'contentType': 'PlainText'|'SSML'|'CustomPayload',
                    'content': 'string',
                    'groupNumber': 123
                },
            ],
            'maxAttempts': 123,
            'responseCard': 'string'
        },
        'rejectionStatement': {
            'messages': [
                {
                    'contentType': 'PlainText'|'SSML'|'CustomPayload',
                    'content': 'string',
                    'groupNumber': 123
                },
            ],
            'responseCard': 'string'
        }
    },
    'conclusionStatement': {
        'messages': [
            {
                'contentType': 'PlainText'|'SSML'|'CustomPayload',
                'content': 'string',
                'groupNumber': 123
            },
        ],
        'responseCard': 'string'
    },
    'dialogCodeHook': {
        'uri': 'string',
        'messageVersion': 'string'
    },
    'fulfillmentActivity': {
        'type': 'ReturnIntent'|'CodeHook',
        'codeHook': {
            'uri': 'string',
            'messageVersion': 'string'
        }
    },
    'parentIntentSignature': 'string',
    'lastUpdatedDate': datetime(2015, 1, 1),
    'createdDate': datetime(2015, 1, 1),
    'version': 'string',
    'checksum': 'string'
}


Response Structure

(dict) --

name (string) --
The name of the intent.

description (string) --
A description of the intent.

slots (list) --
An array of intent slots configured for the intent.

(dict) --
Identifies the version of a specific slot.

name (string) --
The name of the slot.

description (string) --
A description of the slot.

slotConstraint (string) --
Specifies whether the slot is required or optional.

slotType (string) --
The type of the slot, either a custom slot type that you defined or one of the built-in slot types.

slotTypeVersion (string) --
The version of the slot type.

valueElicitationPrompt (dict) --
The prompt that Amazon Lex uses to elicit the slot value from the user.

messages (list) --
An array of objects, each of which provides a message string and its type. You can specify the message string in plain text or in Speech Synthesis Markup Language (SSML).

(dict) --
The message object that provides the message text and its type.

contentType (string) --
The content type of the message string.

content (string) --
The text of the message.

groupNumber (integer) --
Identifies the message group that the message belongs to. When a group is assigned to a message, Amazon Lex returns one message from each group in the response.





maxAttempts (integer) --
The number of times to prompt the user for information.

responseCard (string) --
A response card. Amazon Lex uses this prompt at runtime, in the PostText API response. It substitutes session attributes and slot values for placeholders in the response card. For more information, see  ex-resp-card .



priority (integer) --
Directs Lex the order in which to elicit this slot value from the user. For example, if the intent has two slots with priorities 1 and 2, AWS Lex first elicits a value for the slot with priority 1.
If multiple slots share the same priority, the order in which Lex elicits values is arbitrary.

sampleUtterances (list) --
If you know a specific pattern with which users might respond to an Amazon Lex request for a slot value, you can provide those utterances to improve accuracy. This is optional. In most cases, Amazon Lex is capable of understanding user utterances.

(string) --


responseCard (string) --
A set of possible responses for the slot type used by text-based clients. A user chooses an option from the response card, instead of using text to reply.

obfuscationSetting (string) --
Determines whether a slot is obfuscated in conversation logs and stored utterances. When you obfuscate a slot, the value is replaced by the slot name in curly braces ({}). For example, if the slot name is "full_name", obfuscated values are replaced with "{full_name}". For more information, see Slot Obfuscation .





sampleUtterances (list) --
An array of sample utterances configured for the intent.

(string) --


confirmationPrompt (dict) --
If defined in the bot, Amazon Lex uses prompt to confirm the intent before fulfilling the user\'s request. For more information, see  PutIntent .

messages (list) --
An array of objects, each of which provides a message string and its type. You can specify the message string in plain text or in Speech Synthesis Markup Language (SSML).

(dict) --
The message object that provides the message text and its type.

contentType (string) --
The content type of the message string.

content (string) --
The text of the message.

groupNumber (integer) --
Identifies the message group that the message belongs to. When a group is assigned to a message, Amazon Lex returns one message from each group in the response.





maxAttempts (integer) --
The number of times to prompt the user for information.

responseCard (string) --
A response card. Amazon Lex uses this prompt at runtime, in the PostText API response. It substitutes session attributes and slot values for placeholders in the response card. For more information, see  ex-resp-card .



rejectionStatement (dict) --
If the user answers "no" to the question defined in confirmationPrompt , Amazon Lex responds with this statement to acknowledge that the intent was canceled.

messages (list) --
A collection of message objects.

(dict) --
The message object that provides the message text and its type.

contentType (string) --
The content type of the message string.

content (string) --
The text of the message.

groupNumber (integer) --
Identifies the message group that the message belongs to. When a group is assigned to a message, Amazon Lex returns one message from each group in the response.





responseCard (string) --
At runtime, if the client is using the PostText API, Amazon Lex includes the response card in the response. It substitutes all of the session attributes and slot values for placeholders in the response card.



followUpPrompt (dict) --
If defined in the bot, Amazon Lex uses this prompt to solicit additional user activity after the intent is fulfilled. For more information, see  PutIntent .

prompt (dict) --
Prompts for information from the user.

messages (list) --
An array of objects, each of which provides a message string and its type. You can specify the message string in plain text or in Speech Synthesis Markup Language (SSML).

(dict) --
The message object that provides the message text and its type.

contentType (string) --
The content type of the message string.

content (string) --
The text of the message.

groupNumber (integer) --
Identifies the message group that the message belongs to. When a group is assigned to a message, Amazon Lex returns one message from each group in the response.





maxAttempts (integer) --
The number of times to prompt the user for information.

responseCard (string) --
A response card. Amazon Lex uses this prompt at runtime, in the PostText API response. It substitutes session attributes and slot values for placeholders in the response card. For more information, see  ex-resp-card .



rejectionStatement (dict) --
If the user answers "no" to the question defined in the prompt field, Amazon Lex responds with this statement to acknowledge that the intent was canceled.

messages (list) --
A collection of message objects.

(dict) --
The message object that provides the message text and its type.

contentType (string) --
The content type of the message string.

content (string) --
The text of the message.

groupNumber (integer) --
Identifies the message group that the message belongs to. When a group is assigned to a message, Amazon Lex returns one message from each group in the response.





responseCard (string) --
At runtime, if the client is using the PostText API, Amazon Lex includes the response card in the response. It substitutes all of the session attributes and slot values for placeholders in the response card.





conclusionStatement (dict) --
After the Lambda function specified in the fulfillmentActivity element fulfills the intent, Amazon Lex conveys this statement to the user.

messages (list) --
A collection of message objects.

(dict) --
The message object that provides the message text and its type.

contentType (string) --
The content type of the message string.

content (string) --
The text of the message.

groupNumber (integer) --
Identifies the message group that the message belongs to. When a group is assigned to a message, Amazon Lex returns one message from each group in the response.





responseCard (string) --
At runtime, if the client is using the PostText API, Amazon Lex includes the response card in the response. It substitutes all of the session attributes and slot values for placeholders in the response card.



dialogCodeHook (dict) --
If defined in the bot, Amazon Amazon Lex invokes this Lambda function for each user input. For more information, see  PutIntent .

uri (string) --
The Amazon Resource Name (ARN) of the Lambda function.

messageVersion (string) --
The version of the request-response that you want Amazon Lex to use to invoke your Lambda function. For more information, see  using-lambda .



fulfillmentActivity (dict) --
Describes how the intent is fulfilled. For more information, see  PutIntent .

type (string) --
How the intent should be fulfilled, either by running a Lambda function or by returning the slot data to the client application.

codeHook (dict) --
A description of the Lambda function that is run to fulfill the intent.

uri (string) --
The Amazon Resource Name (ARN) of the Lambda function.

messageVersion (string) --
The version of the request-response that you want Amazon Lex to use to invoke your Lambda function. For more information, see  using-lambda .





parentIntentSignature (string) --
A unique identifier for a built-in intent.

lastUpdatedDate (datetime) --
The date that the intent was updated. When you create a resource, the creation date and the last updated date are the same.

createdDate (datetime) --
The date that the intent was created.

version (string) --
The version of the intent.

checksum (string) --
Checksum of the intent.







Exceptions

LexModelBuildingService.Client.exceptions.NotFoundException
LexModelBuildingService.Client.exceptions.LimitExceededException
LexModelBuildingService.Client.exceptions.InternalFailureException
LexModelBuildingService.Client.exceptions.BadRequestException

Examples
This example shows how to get information about an intent.
response = client.get_intent(
    version='$LATEST',
    name='DocOrderPizza',
)

print(response)


Expected Output:
{
    'version': '$LATEST',
    'name': 'DocOrderPizza',
    'checksum': 'ca9bc13d-afc8-4706-bbaf-091f7a5935d6',
    'conclusionStatement': {
        'messages': [
            {
                'content': 'All right, I ordered  you a {Crust} crust {Type} pizza with {Sauce} sauce.',
                'contentType': 'PlainText',
            },
            {
                'content': 'OK, your {Crust} crust {Type} pizza with {Sauce} sauce is on the way.',
                'contentType': 'PlainText',
            },
        ],
        'responseCard': 'foo',
    },
    'confirmationPrompt': {
        'maxAttempts': 1,
        'messages': [
            {
                'content': 'Should I order  your {Crust} crust {Type} pizza with {Sauce} sauce?',
                'contentType': 'PlainText',
            },
        ],
    },
    'createdDate': 1494359783.453,
    'description': 'Order a pizza from a local pizzeria.',
    'fulfillmentActivity': {
        'type': 'ReturnIntent',
    },
    'lastUpdatedDate': 1494359783.453,
    'rejectionStatement': {
        'messages': [
            {
                'content': 'Ok, I'll cancel your order.',
                'contentType': 'PlainText',
            },
            {
                'content': 'I cancelled your order.',
                'contentType': 'PlainText',
            },
        ],
    },
    'sampleUtterances': [
        'Order me a pizza.',
        'Order me a {Type} pizza.',
        'I want a {Crust} crust {Type} pizza',
        'I want a {Crust} crust {Type} pizza with {Sauce} sauce.',
    ],
    'slots': [
        {
            'name': 'Type',
            'description': 'The type of pizza to order.',
            'priority': 1,
            'sampleUtterances': [
                'Get me a {Type} pizza.',
                'A {Type} pizza please.',
                'I'd like a {Type} pizza.',
            ],
            'slotConstraint': 'Required',
            'slotType': 'DocPizzaType',
            'slotTypeVersion': '$LATEST',
            'valueElicitationPrompt': {
                'maxAttempts': 1,
                'messages': [
                    {
                        'content': 'What type of pizza would you like?',
                        'contentType': 'PlainText',
                    },
                    {
                        'content': 'Vegie or cheese pizza?',
                        'contentType': 'PlainText',
                    },
                    {
                        'content': 'I can get you a vegie or a cheese pizza.',
                        'contentType': 'PlainText',
                    },
                ],
            },
        },
        {
            'name': 'Crust',
            'description': 'The type of pizza crust to order.',
            'priority': 2,
            'sampleUtterances': [
                'Make it a {Crust} crust.',
                'I'd like a {Crust} crust.',
            ],
            'slotConstraint': 'Required',
            'slotType': 'DocPizzaCrustType',
            'slotTypeVersion': '$LATEST',
            'valueElicitationPrompt': {
                'maxAttempts': 1,
                'messages': [
                    {
                        'content': 'What type of crust would you like?',
                        'contentType': 'PlainText',
                    },
                    {
                        'content': 'Thick or thin crust?',
                        'contentType': 'PlainText',
                    },
                ],
            },
        },
        {
            'name': 'Sauce',
            'description': 'The type of sauce to use on the pizza.',
            'priority': 3,
            'sampleUtterances': [
                'Make it {Sauce} sauce.',
                'I'd like {Sauce} sauce.',
            ],
            'slotConstraint': 'Required',
            'slotType': 'DocPizzaSauceType',
            'slotTypeVersion': '$LATEST',
            'valueElicitationPrompt': {
                'maxAttempts': 1,
                'messages': [
                    {
                        'content': 'White or red sauce?',
                        'contentType': 'PlainText',
                    },
                    {
                        'content': 'Garlic or tomato sauce?',
                        'contentType': 'PlainText',
                    },
                ],
            },
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'name': 'string',
        'description': 'string',
        'slots': [
            {
                'name': 'string',
                'description': 'string',
                'slotConstraint': 'Required'|'Optional',
                'slotType': 'string',
                'slotTypeVersion': 'string',
                'valueElicitationPrompt': {
                    'messages': [
                        {
                            'contentType': 'PlainText'|'SSML'|'CustomPayload',
                            'content': 'string',
                            'groupNumber': 123
                        },
                    ],
                    'maxAttempts': 123,
                    'responseCard': 'string'
                },
                'priority': 123,
                'sampleUtterances': [
                    'string',
                ],
                'responseCard': 'string',
                'obfuscationSetting': 'NONE'|'DEFAULT_OBFUSCATION'
            },
        ],
        'sampleUtterances': [
            'string',
        ],
        'confirmationPrompt': {
            'messages': [
                {
                    'contentType': 'PlainText'|'SSML'|'CustomPayload',
                    'content': 'string',
                    'groupNumber': 123
                },
            ],
            'maxAttempts': 123,
            'responseCard': 'string'
        },
        'rejectionStatement': {
            'messages': [
                {
                    'contentType': 'PlainText'|'SSML'|'CustomPayload',
                    'content': 'string',
                    'groupNumber': 123
                },
            ],
            'responseCard': 'string'
        },
        'followUpPrompt': {
            'prompt': {
                'messages': [
                    {
                        'contentType': 'PlainText'|'SSML'|'CustomPayload',
                        'content': 'string',
                        'groupNumber': 123
                    },
                ],
                'maxAttempts': 123,
                'responseCard': 'string'
            },
            'rejectionStatement': {
                'messages': [
                    {
                        'contentType': 'PlainText'|'SSML'|'CustomPayload',
                        'content': 'string',
                        'groupNumber': 123
                    },
                ],
                'responseCard': 'string'
            }
        },
        'conclusionStatement': {
            'messages': [
                {
                    'contentType': 'PlainText'|'SSML'|'CustomPayload',
                    'content': 'string',
                    'groupNumber': 123
                },
            ],
            'responseCard': 'string'
        },
        'dialogCodeHook': {
            'uri': 'string',
            'messageVersion': 'string'
        },
        'fulfillmentActivity': {
            'type': 'ReturnIntent'|'CodeHook',
            'codeHook': {
                'uri': 'string',
                'messageVersion': 'string'
            }
        },
        'parentIntentSignature': 'string',
        'lastUpdatedDate': datetime(2015, 1, 1),
        'createdDate': datetime(2015, 1, 1),
        'version': 'string',
        'checksum': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_intent_versions(name=None, nextToken=None, maxResults=None):
    """
    Gets information about all of the versions of an intent.
    The GetIntentVersions operation returns an IntentMetadata object for each version of an intent. For example, if an intent has three numbered versions, the GetIntentVersions operation returns four IntentMetadata objects in the response, one for each numbered version and one for the $LATEST version.
    The GetIntentVersions operation always returns at least one version, the $LATEST version.
    This operation requires permissions for the lex:GetIntentVersions action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_intent_versions(
        name='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name of the intent for which versions should be returned.\n

    :type nextToken: string
    :param nextToken: A pagination token for fetching the next page of intent versions. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of versions, specify the pagination token in the next request.

    :type maxResults: integer
    :param maxResults: The maximum number of intent versions to return in the response. The default is 10.

    :rtype: dict

ReturnsResponse Syntax
{
    'intents': [
        {
            'name': 'string',
            'description': 'string',
            'lastUpdatedDate': datetime(2015, 1, 1),
            'createdDate': datetime(2015, 1, 1),
            'version': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

intents (list) --
An array of IntentMetadata objects, one for each numbered version of the intent plus one for the $LATEST version.

(dict) --
Provides information about an intent.

name (string) --
The name of the intent.

description (string) --
A description of the intent.

lastUpdatedDate (datetime) --
The date that the intent was updated. When you create an intent, the creation date and last updated date are the same.

createdDate (datetime) --
The date that the intent was created.

version (string) --
The version of the intent.





nextToken (string) --
A pagination token for fetching the next page of intent versions. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of versions, specify the pagination token in the next request.







Exceptions

LexModelBuildingService.Client.exceptions.NotFoundException
LexModelBuildingService.Client.exceptions.LimitExceededException
LexModelBuildingService.Client.exceptions.InternalFailureException
LexModelBuildingService.Client.exceptions.BadRequestException


    :return: {
        'intents': [
            {
                'name': 'string',
                'description': 'string',
                'lastUpdatedDate': datetime(2015, 1, 1),
                'createdDate': datetime(2015, 1, 1),
                'version': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    LexModelBuildingService.Client.exceptions.NotFoundException
    LexModelBuildingService.Client.exceptions.LimitExceededException
    LexModelBuildingService.Client.exceptions.InternalFailureException
    LexModelBuildingService.Client.exceptions.BadRequestException
    
    """
    pass

def get_intents(nextToken=None, maxResults=None, nameContains=None):
    """
    Returns intent information as follows:
    The operation requires permission for the lex:GetIntents action.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example shows how to get a list of all of the intents in your account.
    Expected Output:
    
    :example: response = client.get_intents(
        nextToken='string',
        maxResults=123,
        nameContains='string'
    )
    
    
    :type nextToken: string
    :param nextToken: A pagination token that fetches the next page of intents. If the response to this API call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of intents, specify the pagination token in the next request.

    :type maxResults: integer
    :param maxResults: The maximum number of intents to return in the response. The default is 10.

    :type nameContains: string
    :param nameContains: Substring to match in intent names. An intent will be returned if any part of its name matches the substring. For example, 'xyz' matches both 'xyzabc' and 'abcxyz.'

    :rtype: dict

ReturnsResponse Syntax
{
    'intents': [
        {
            'name': 'string',
            'description': 'string',
            'lastUpdatedDate': datetime(2015, 1, 1),
            'createdDate': datetime(2015, 1, 1),
            'version': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

intents (list) --
An array of Intent objects. For more information, see  PutBot .

(dict) --
Provides information about an intent.

name (string) --
The name of the intent.

description (string) --
A description of the intent.

lastUpdatedDate (datetime) --
The date that the intent was updated. When you create an intent, the creation date and last updated date are the same.

createdDate (datetime) --
The date that the intent was created.

version (string) --
The version of the intent.





nextToken (string) --
If the response is truncated, the response includes a pagination token that you can specify in your next request to fetch the next page of intents.







Exceptions

LexModelBuildingService.Client.exceptions.NotFoundException
LexModelBuildingService.Client.exceptions.LimitExceededException
LexModelBuildingService.Client.exceptions.InternalFailureException
LexModelBuildingService.Client.exceptions.BadRequestException

Examples
This example shows how to get a list of all of the intents in your account.
response = client.get_intents(
    maxResults=10,
    nextToken='',
)

print(response)


Expected Output:
{
    'intents': [
        {
            'version': '$LATEST',
            'name': 'DocOrderPizza',
            'createdDate': 1494359783.453,
            'description': 'Order a pizza from a local pizzeria.',
            'lastUpdatedDate': 1494359783.453,
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'intents': [
            {
                'name': 'string',
                'description': 'string',
                'lastUpdatedDate': datetime(2015, 1, 1),
                'createdDate': datetime(2015, 1, 1),
                'version': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    nextToken (string) -- A pagination token that fetches the next page of intents. If the response to this API call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of intents, specify the pagination token in the next request.
    maxResults (integer) -- The maximum number of intents to return in the response. The default is 10.
    nameContains (string) -- Substring to match in intent names. An intent will be returned if any part of its name matches the substring. For example, "xyz" matches both "xyzabc" and "abcxyz."
    
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

def get_slot_type(name=None, version=None):
    """
    Returns information about a specific version of a slot type. In addition to specifying the slot type name, you must specify the slot type version.
    This operation requires permissions for the lex:GetSlotType action.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example shows how to get information about a slot type.
    Expected Output:
    
    :example: response = client.get_slot_type(
        name='string',
        version='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name of the slot type. The name is case sensitive.\n

    :type version: string
    :param version: [REQUIRED]\nThe version of the slot type.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'name': 'string',
    'description': 'string',
    'enumerationValues': [
        {
            'value': 'string',
            'synonyms': [
                'string',
            ]
        },
    ],
    'lastUpdatedDate': datetime(2015, 1, 1),
    'createdDate': datetime(2015, 1, 1),
    'version': 'string',
    'checksum': 'string',
    'valueSelectionStrategy': 'ORIGINAL_VALUE'|'TOP_RESOLUTION',
    'parentSlotTypeSignature': 'string',
    'slotTypeConfigurations': [
        {
            'regexConfiguration': {
                'pattern': 'string'
            }
        },
    ]
}


Response Structure

(dict) --

name (string) --
The name of the slot type.

description (string) --
A description of the slot type.

enumerationValues (list) --
A list of EnumerationValue objects that defines the values that the slot type can take.

(dict) --
Each slot type can have a set of values. Each enumeration value represents a value the slot type can take.
For example, a pizza ordering bot could have a slot type that specifies the type of crust that the pizza should have. The slot type could include the values

thick
thin
stuffed


value (string) --
The value of the slot type.

synonyms (list) --
Additional values related to the slot type value.

(string) --






lastUpdatedDate (datetime) --
The date that the slot type was updated. When you create a resource, the creation date and last update date are the same.

createdDate (datetime) --
The date that the slot type was created.

version (string) --
The version of the slot type.

checksum (string) --
Checksum of the $LATEST version of the slot type.

valueSelectionStrategy (string) --
The strategy that Amazon Lex uses to determine the value of the slot. For more information, see  PutSlotType .

parentSlotTypeSignature (string) --
The built-in slot type used as a parent for the slot type.

slotTypeConfigurations (list) --
Configuration information that extends the parent built-in slot type.

(dict) --
Provides configuration information for a slot type.

regexConfiguration (dict) --
A regular expression used to validate the value of a slot.

pattern (string) --
A regular expression used to validate the value of a slot.
Use a standard regular expression. Amazon Lex supports the following characters in the regular expression:

A-Z, a-z
0-9
Unicode characters ("u<Unicode>")

Represent Unicode characters with four digits, for example "u0041" or "u005A".
The following regular expression operators are not supported:

Infinite repeaters: *, +, or {x,} with no upper bound.
Wild card (.)














Exceptions

LexModelBuildingService.Client.exceptions.NotFoundException
LexModelBuildingService.Client.exceptions.LimitExceededException
LexModelBuildingService.Client.exceptions.InternalFailureException
LexModelBuildingService.Client.exceptions.BadRequestException

Examples
This example shows how to get information about a slot type.
response = client.get_slot_type(
    version='$LATEST',
    name='DocPizzaCrustType',
)

print(response)


Expected Output:
{
    'version': '$LATEST',
    'name': 'DocPizzaCrustType',
    'checksum': '210b3d5a-90a3-4b22-ac7e-f50c2c71095f',
    'createdDate': 1494359274.403,
    'description': 'Available crust types',
    'enumerationValues': [
        {
            'value': 'thick',
        },
        {
            'value': 'thin',
        },
    ],
    'lastUpdatedDate': 1494359274.403,
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'name': 'string',
        'description': 'string',
        'enumerationValues': [
            {
                'value': 'string',
                'synonyms': [
                    'string',
                ]
            },
        ],
        'lastUpdatedDate': datetime(2015, 1, 1),
        'createdDate': datetime(2015, 1, 1),
        'version': 'string',
        'checksum': 'string',
        'valueSelectionStrategy': 'ORIGINAL_VALUE'|'TOP_RESOLUTION',
        'parentSlotTypeSignature': 'string',
        'slotTypeConfigurations': [
            {
                'regexConfiguration': {
                    'pattern': 'string'
                }
            },
        ]
    }
    
    
    :returns: 
    thick
    thin
    stuffed
    
    """
    pass

def get_slot_type_versions(name=None, nextToken=None, maxResults=None):
    """
    Gets information about all versions of a slot type.
    The GetSlotTypeVersions operation returns a SlotTypeMetadata object for each version of a slot type. For example, if a slot type has three numbered versions, the GetSlotTypeVersions operation returns four SlotTypeMetadata objects in the response, one for each numbered version and one for the $LATEST version.
    The GetSlotTypeVersions operation always returns at least one version, the $LATEST version.
    This operation requires permissions for the lex:GetSlotTypeVersions action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_slot_type_versions(
        name='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name of the slot type for which versions should be returned.\n

    :type nextToken: string
    :param nextToken: A pagination token for fetching the next page of slot type versions. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of versions, specify the pagination token in the next request.

    :type maxResults: integer
    :param maxResults: The maximum number of slot type versions to return in the response. The default is 10.

    :rtype: dict

ReturnsResponse Syntax
{
    'slotTypes': [
        {
            'name': 'string',
            'description': 'string',
            'lastUpdatedDate': datetime(2015, 1, 1),
            'createdDate': datetime(2015, 1, 1),
            'version': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

slotTypes (list) --
An array of SlotTypeMetadata objects, one for each numbered version of the slot type plus one for the $LATEST version.

(dict) --
Provides information about a slot type..

name (string) --
The name of the slot type.

description (string) --
A description of the slot type.

lastUpdatedDate (datetime) --
The date that the slot type was updated. When you create a resource, the creation date and last updated date are the same.

createdDate (datetime) --
The date that the slot type was created.

version (string) --
The version of the slot type.





nextToken (string) --
A pagination token for fetching the next page of slot type versions. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of versions, specify the pagination token in the next request.







Exceptions

LexModelBuildingService.Client.exceptions.NotFoundException
LexModelBuildingService.Client.exceptions.LimitExceededException
LexModelBuildingService.Client.exceptions.InternalFailureException
LexModelBuildingService.Client.exceptions.BadRequestException


    :return: {
        'slotTypes': [
            {
                'name': 'string',
                'description': 'string',
                'lastUpdatedDate': datetime(2015, 1, 1),
                'createdDate': datetime(2015, 1, 1),
                'version': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    LexModelBuildingService.Client.exceptions.NotFoundException
    LexModelBuildingService.Client.exceptions.LimitExceededException
    LexModelBuildingService.Client.exceptions.InternalFailureException
    LexModelBuildingService.Client.exceptions.BadRequestException
    
    """
    pass

def get_slot_types(nextToken=None, maxResults=None, nameContains=None):
    """
    Returns slot type information as follows:
    The operation requires permission for the lex:GetSlotTypes action.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example shows how to get a list of all of the slot types in your account.
    Expected Output:
    
    :example: response = client.get_slot_types(
        nextToken='string',
        maxResults=123,
        nameContains='string'
    )
    
    
    :type nextToken: string
    :param nextToken: A pagination token that fetches the next page of slot types. If the response to this API call is truncated, Amazon Lex returns a pagination token in the response. To fetch next page of slot types, specify the pagination token in the next request.

    :type maxResults: integer
    :param maxResults: The maximum number of slot types to return in the response. The default is 10.

    :type nameContains: string
    :param nameContains: Substring to match in slot type names. A slot type will be returned if any part of its name matches the substring. For example, 'xyz' matches both 'xyzabc' and 'abcxyz.'

    :rtype: dict

ReturnsResponse Syntax
{
    'slotTypes': [
        {
            'name': 'string',
            'description': 'string',
            'lastUpdatedDate': datetime(2015, 1, 1),
            'createdDate': datetime(2015, 1, 1),
            'version': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

slotTypes (list) --
An array of objects, one for each slot type, that provides information such as the name of the slot type, the version, and a description.

(dict) --
Provides information about a slot type..

name (string) --
The name of the slot type.

description (string) --
A description of the slot type.

lastUpdatedDate (datetime) --
The date that the slot type was updated. When you create a resource, the creation date and last updated date are the same.

createdDate (datetime) --
The date that the slot type was created.

version (string) --
The version of the slot type.





nextToken (string) --
If the response is truncated, it includes a pagination token that you can specify in your next request to fetch the next page of slot types.







Exceptions

LexModelBuildingService.Client.exceptions.NotFoundException
LexModelBuildingService.Client.exceptions.LimitExceededException
LexModelBuildingService.Client.exceptions.InternalFailureException
LexModelBuildingService.Client.exceptions.BadRequestException

Examples
This example shows how to get a list of all of the slot types in your account.
response = client.get_slot_types(
    maxResults=10,
    nextToken='',
)

print(response)


Expected Output:
{
    'slotTypes': [
        {
            'version': '$LATEST',
            'name': 'DocPizzaCrustType',
            'createdDate': 1494359274.403,
            'description': 'Available crust types',
            'lastUpdatedDate': 1494359274.403,
        },
        {
            'version': '$LATEST',
            'name': 'DocPizzaSauceType',
            'createdDate': 1494356442.23,
            'description': 'Available pizza sauces',
            'lastUpdatedDate': 1494356442.23,
        },
        {
            'version': '$LATEST',
            'name': 'DocPizzaType',
            'createdDate': 1494359198.656,
            'description': 'Available pizzas',
            'lastUpdatedDate': 1494359198.656,
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'slotTypes': [
            {
                'name': 'string',
                'description': 'string',
                'lastUpdatedDate': datetime(2015, 1, 1),
                'createdDate': datetime(2015, 1, 1),
                'version': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    nextToken (string) -- A pagination token that fetches the next page of slot types. If the response to this API call is truncated, Amazon Lex returns a pagination token in the response. To fetch next page of slot types, specify the pagination token in the next request.
    maxResults (integer) -- The maximum number of slot types to return in the response. The default is 10.
    nameContains (string) -- Substring to match in slot type names. A slot type will be returned if any part of its name matches the substring. For example, "xyz" matches both "xyzabc" and "abcxyz."
    
    """
    pass

def get_utterances_view(botName=None, botVersions=None, statusType=None):
    """
    Use the GetUtterancesView operation to get information about the utterances that your users have made to your bot. You can use this list to tune the utterances that your bot responds to.
    For example, say that you have created a bot to order flowers. After your users have used your bot for a while, use the GetUtterancesView operation to see the requests that they have made and whether they have been successful. You might find that the utterance "I want flowers" is not being recognized. You could add this utterance to the OrderFlowers intent so that your bot recognizes that utterance.
    After you publish a new version of a bot, you can get information about the old version and the new so that you can compare the performance across the two versions.
    Utterance statistics are generated once a day. Data is available for the last 15 days. You can request information for up to 5 versions of your bot in each request. Amazon Lex returns the most frequent utterances received by the bot in the last 15 days. The response contains information about a maximum of 100 utterances for each version.
    If you set childDirected field to true when you created your bot, or if you opted out of participating in improving Amazon Lex, utterances are not available.
    This operation requires permissions for the lex:GetUtterancesView action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_utterances_view(
        botName='string',
        botVersions=[
            'string',
        ],
        statusType='Detected'|'Missed'
    )
    
    
    :type botName: string
    :param botName: [REQUIRED]\nThe name of the bot for which utterance information should be returned.\n

    :type botVersions: list
    :param botVersions: [REQUIRED]\nAn array of bot versions for which utterance information should be returned. The limit is 5 versions per request.\n\n(string) --\n\n

    :type statusType: string
    :param statusType: [REQUIRED]\nTo return utterances that were recognized and handled, use Detected . To return utterances that were not recognized, use Missed .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'botName': 'string',
    'utterances': [
        {
            'botVersion': 'string',
            'utterances': [
                {
                    'utteranceString': 'string',
                    'count': 123,
                    'distinctUsers': 123,
                    'firstUtteredDate': datetime(2015, 1, 1),
                    'lastUtteredDate': datetime(2015, 1, 1)
                },
            ]
        },
    ]
}


Response Structure

(dict) --

botName (string) --
The name of the bot for which utterance information was returned.

utterances (list) --
An array of  UtteranceList objects, each containing a list of  UtteranceData objects describing the utterances that were processed by your bot. The response contains a maximum of 100 UtteranceData objects for each version. Amazon Lex returns the most frequent utterances received by the bot in the last 15 days.

(dict) --
Provides a list of utterances that have been made to a specific version of your bot. The list contains a maximum of 100 utterances.

botVersion (string) --
The version of the bot that processed the list.

utterances (list) --
One or more  UtteranceData objects that contain information about the utterances that have been made to a bot. The maximum number of object is 100.

(dict) --
Provides information about a single utterance that was made to your bot.

utteranceString (string) --
The text that was entered by the user or the text representation of an audio clip.

count (integer) --
The number of times that the utterance was processed.

distinctUsers (integer) --
The total number of individuals that used the utterance.

firstUtteredDate (datetime) --
The date that the utterance was first recorded.

lastUtteredDate (datetime) --
The date that the utterance was last recorded.















Exceptions

LexModelBuildingService.Client.exceptions.LimitExceededException
LexModelBuildingService.Client.exceptions.InternalFailureException
LexModelBuildingService.Client.exceptions.BadRequestException


    :return: {
        'botName': 'string',
        'utterances': [
            {
                'botVersion': 'string',
                'utterances': [
                    {
                        'utteranceString': 'string',
                        'count': 123,
                        'distinctUsers': 123,
                        'firstUtteredDate': datetime(2015, 1, 1),
                        'lastUtteredDate': datetime(2015, 1, 1)
                    },
                ]
            },
        ]
    }
    
    
    :returns: 
    LexModelBuildingService.Client.exceptions.LimitExceededException
    LexModelBuildingService.Client.exceptions.InternalFailureException
    LexModelBuildingService.Client.exceptions.BadRequestException
    
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

def list_tags_for_resource(resourceArn=None):
    """
    Gets a list of tags associated with the specified resource. Only bots, bot aliases, and bot channels can have tags associated with them.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        resourceArn='string'
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource to get a list of tags for.\n

    :rtype: dict
ReturnsResponse Syntax{
    'tags': [
        {
            'key': 'string',
            'value': 'string'
        },
    ]
}


Response Structure

(dict) --
tags (list) --The tags associated with a resource.

(dict) --A list of key/value pairs that identify a bot, bot alias, or bot channel. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.

key (string) --The key for the tag. Keys are not case-sensitive and must be unique.

value (string) --The value associated with a key. The value may be an empty string but it can\'t be null.










Exceptions

LexModelBuildingService.Client.exceptions.NotFoundException
LexModelBuildingService.Client.exceptions.BadRequestException
LexModelBuildingService.Client.exceptions.InternalFailureException
LexModelBuildingService.Client.exceptions.LimitExceededException


    :return: {
        'tags': [
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    }
    
    
    """
    pass

def put_bot(name=None, description=None, intents=None, clarificationPrompt=None, abortStatement=None, idleSessionTTLInSeconds=None, voiceId=None, checksum=None, processBehavior=None, locale=None, childDirected=None, detectSentiment=None, createVersion=None, tags=None):
    """
    Creates an Amazon Lex conversational bot or replaces an existing bot. When you create or update a bot you are only required to specify a name, a locale, and whether the bot is directed toward children under age 13. You can use this to add intents later, or to remove intents from an existing bot. When you create a bot with the minimum information, the bot is created or updated but Amazon Lex returns the response FAILED . You can build the bot after you add one or more intents. For more information about Amazon Lex bots, see  how-it-works .
    If you specify the name of an existing bot, the fields in the request replace the existing values in the $LATEST version of the bot. Amazon Lex removes any fields that you don\'t provide values for in the request, except for the idleTTLInSeconds and privacySettings fields, which are set to their default values. If you don\'t specify values for required fields, Amazon Lex throws an exception.
    This operation requires permissions for the lex:PutBot action. For more information, see  security-iam .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example shows how to create a bot for ordering pizzas.
    Expected Output:
    
    :example: response = client.put_bot(
        name='string',
        description='string',
        intents=[
            {
                'intentName': 'string',
                'intentVersion': 'string'
            },
        ],
        clarificationPrompt={
            'messages': [
                {
                    'contentType': 'PlainText'|'SSML'|'CustomPayload',
                    'content': 'string',
                    'groupNumber': 123
                },
            ],
            'maxAttempts': 123,
            'responseCard': 'string'
        },
        abortStatement={
            'messages': [
                {
                    'contentType': 'PlainText'|'SSML'|'CustomPayload',
                    'content': 'string',
                    'groupNumber': 123
                },
            ],
            'responseCard': 'string'
        },
        idleSessionTTLInSeconds=123,
        voiceId='string',
        checksum='string',
        processBehavior='SAVE'|'BUILD',
        locale='en-US'|'en-GB'|'de-DE',
        childDirected=True|False,
        detectSentiment=True|False,
        createVersion=True|False,
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name of the bot. The name is not case sensitive.\n

    :type description: string
    :param description: A description of the bot.

    :type intents: list
    :param intents: An array of Intent objects. Each intent represents a command that a user can express. For example, a pizza ordering bot might support an OrderPizza intent. For more information, see how-it-works .\n\n(dict) --Identifies the specific version of an intent.\n\nintentName (string) -- [REQUIRED]The name of the intent.\n\nintentVersion (string) -- [REQUIRED]The version of the intent.\n\n\n\n\n

    :type clarificationPrompt: dict
    :param clarificationPrompt: When Amazon Lex doesn\'t understand the user\'s intent, it uses this message to get clarification. To specify how many times Amazon Lex should repeat the clarification prompt, use the maxAttempts field. If Amazon Lex still doesn\'t understand, it sends the message in the abortStatement field.\nWhen you create a clarification prompt, make sure that it suggests the correct response from the user. for example, for a bot that orders pizza and drinks, you might create this clarification prompt: 'What would you like to do? You can say \'Order a pizza\' or \'Order a drink.\''\nIf you have defined a fallback intent, it will be invoked if the clarification prompt is repeated the number of times defined in the maxAttempts field. For more information, see AMAZON.FallbackIntent .\nIf you don\'t define a clarification prompt, at runtime Amazon Lex will return a 400 Bad Request exception in three cases:\n\nFollow-up prompt - When the user responds to a follow-up prompt but does not provide an intent. For example, in response to a follow-up prompt that says 'Would you like anything else today?' the user says 'Yes.' Amazon Lex will return a 400 Bad Request exception because it does not have a clarification prompt to send to the user to get an intent.\nLambda function - When using a Lambda function, you return an ElicitIntent dialog type. Since Amazon Lex does not have a clarification prompt to get an intent from the user, it returns a 400 Bad Request exception.\nPutSession operation - When using the PutSession operation, you send an ElicitIntent dialog type. Since Amazon Lex does not have a clarification prompt to get an intent from the user, it returns a 400 Bad Request exception.\n\n\nmessages (list) -- [REQUIRED]An array of objects, each of which provides a message string and its type. You can specify the message string in plain text or in Speech Synthesis Markup Language (SSML).\n\n(dict) --The message object that provides the message text and its type.\n\ncontentType (string) -- [REQUIRED]The content type of the message string.\n\ncontent (string) -- [REQUIRED]The text of the message.\n\ngroupNumber (integer) --Identifies the message group that the message belongs to. When a group is assigned to a message, Amazon Lex returns one message from each group in the response.\n\n\n\n\n\nmaxAttempts (integer) -- [REQUIRED]The number of times to prompt the user for information.\n\nresponseCard (string) --A response card. Amazon Lex uses this prompt at runtime, in the PostText API response. It substitutes session attributes and slot values for placeholders in the response card. For more information, see ex-resp-card .\n\n\n

    :type abortStatement: dict
    :param abortStatement: When Amazon Lex can\'t understand the user\'s input in context, it tries to elicit the information a few times. After that, Amazon Lex sends the message defined in abortStatement to the user, and then aborts the conversation. To set the number of retries, use the valueElicitationPrompt field for the slot type.\nFor example, in a pizza ordering bot, Amazon Lex might ask a user 'What type of crust would you like?' If the user\'s response is not one of the expected responses (for example, 'thin crust, 'deep dish,' etc.), Amazon Lex tries to elicit a correct response a few more times.\nFor example, in a pizza ordering application, OrderPizza might be one of the intents. This intent might require the CrustType slot. You specify the valueElicitationPrompt field when you create the CrustType slot.\nIf you have defined a fallback intent the abort statement will not be sent to the user, the fallback intent is used instead. For more information, see AMAZON.FallbackIntent .\n\nmessages (list) -- [REQUIRED]A collection of message objects.\n\n(dict) --The message object that provides the message text and its type.\n\ncontentType (string) -- [REQUIRED]The content type of the message string.\n\ncontent (string) -- [REQUIRED]The text of the message.\n\ngroupNumber (integer) --Identifies the message group that the message belongs to. When a group is assigned to a message, Amazon Lex returns one message from each group in the response.\n\n\n\n\n\nresponseCard (string) --At runtime, if the client is using the PostText API, Amazon Lex includes the response card in the response. It substitutes all of the session attributes and slot values for placeholders in the response card.\n\n\n

    :type idleSessionTTLInSeconds: integer
    :param idleSessionTTLInSeconds: The maximum time in seconds that Amazon Lex retains the data gathered in a conversation.\nA user interaction session remains active for the amount of time specified. If no conversation occurs during this time, the session expires and Amazon Lex deletes any data provided before the timeout.\nFor example, suppose that a user chooses the OrderPizza intent, but gets sidetracked halfway through placing an order. If the user doesn\'t complete the order within the specified time, Amazon Lex discards the slot information that it gathered, and the user must start over.\nIf you don\'t include the idleSessionTTLInSeconds element in a PutBot operation request, Amazon Lex uses the default value. This is also true if the request replaces an existing bot.\nThe default is 300 seconds (5 minutes).\n

    :type voiceId: string
    :param voiceId: The Amazon Polly voice ID that you want Amazon Lex to use for voice interactions with the user. The locale configured for the voice must match the locale of the bot. For more information, see Voices in Amazon Polly in the Amazon Polly Developer Guide .

    :type checksum: string
    :param checksum: Identifies a specific revision of the $LATEST version.\nWhen you create a new bot, leave the checksum field blank. If you specify a checksum you get a BadRequestException exception.\nWhen you want to update a bot, set the checksum field to the checksum of the most recent revision of the $LATEST version. If you don\'t specify the checksum field, or if the checksum does not match the $LATEST version, you get a PreconditionFailedException exception.\n

    :type processBehavior: string
    :param processBehavior: If you set the processBehavior element to BUILD , Amazon Lex builds the bot so that it can be run. If you set the element to SAVE Amazon Lex saves the bot, but doesn\'t build it.\nIf you don\'t specify this value, the default value is BUILD .\n

    :type locale: string
    :param locale: [REQUIRED]\nSpecifies the target locale for the bot. Any intent used in the bot must be compatible with the locale of the bot.\nThe default is en-US .\n

    :type childDirected: boolean
    :param childDirected: [REQUIRED]\nFor each Amazon Lex bot created with the Amazon Lex Model Building Service, you must specify whether your use of Amazon Lex is related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to the Children\'s Online Privacy Protection Act (COPPA) by specifying true or false in the childDirected field. By specifying true in the childDirected field, you confirm that your use of Amazon Lex is related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA. By specifying false in the childDirected field, you confirm that your use of Amazon Lex is not related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA. You may not specify a default value for the childDirected field that does not accurately reflect whether your use of Amazon Lex is related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA.\nIf your use of Amazon Lex relates to a website, program, or other application that is directed in whole or in part, to children under age 13, you must obtain any required verifiable parental consent under COPPA. For information regarding the use of Amazon Lex in connection with websites, programs, or other applications that are directed or targeted, in whole or in part, to children under age 13, see the Amazon Lex FAQ.\n

    :type detectSentiment: boolean
    :param detectSentiment: When set to true user utterances are sent to Amazon Comprehend for sentiment analysis. If you don\'t specify detectSentiment , the default is false .

    :type createVersion: boolean
    :param createVersion: When set to true a new numbered version of the bot is created. This is the same as calling the CreateBotVersion operation. If you don\'t specify createVersion , the default is false .

    :type tags: list
    :param tags: A list of tags to add to the bot. You can only add tags when you create a bot, you can\'t use the PutBot operation to update the tags on a bot. To update tags, use the TagResource operation.\n\n(dict) --A list of key/value pairs that identify a bot, bot alias, or bot channel. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.\n\nkey (string) -- [REQUIRED]The key for the tag. Keys are not case-sensitive and must be unique.\n\nvalue (string) -- [REQUIRED]The value associated with a key. The value may be an empty string but it can\'t be null.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'name': 'string',
    'description': 'string',
    'intents': [
        {
            'intentName': 'string',
            'intentVersion': 'string'
        },
    ],
    'clarificationPrompt': {
        'messages': [
            {
                'contentType': 'PlainText'|'SSML'|'CustomPayload',
                'content': 'string',
                'groupNumber': 123
            },
        ],
        'maxAttempts': 123,
        'responseCard': 'string'
    },
    'abortStatement': {
        'messages': [
            {
                'contentType': 'PlainText'|'SSML'|'CustomPayload',
                'content': 'string',
                'groupNumber': 123
            },
        ],
        'responseCard': 'string'
    },
    'status': 'BUILDING'|'READY'|'READY_BASIC_TESTING'|'FAILED'|'NOT_BUILT',
    'failureReason': 'string',
    'lastUpdatedDate': datetime(2015, 1, 1),
    'createdDate': datetime(2015, 1, 1),
    'idleSessionTTLInSeconds': 123,
    'voiceId': 'string',
    'checksum': 'string',
    'version': 'string',
    'locale': 'en-US'|'en-GB'|'de-DE',
    'childDirected': True|False,
    'createVersion': True|False,
    'detectSentiment': True|False,
    'tags': [
        {
            'key': 'string',
            'value': 'string'
        },
    ]
}


Response Structure

(dict) --

name (string) --
The name of the bot.

description (string) --
A description of the bot.

intents (list) --
An array of Intent objects. For more information, see  PutBot .

(dict) --
Identifies the specific version of an intent.

intentName (string) --
The name of the intent.

intentVersion (string) --
The version of the intent.





clarificationPrompt (dict) --
The prompts that Amazon Lex uses when it doesn\'t understand the user\'s intent. For more information, see  PutBot .

messages (list) --
An array of objects, each of which provides a message string and its type. You can specify the message string in plain text or in Speech Synthesis Markup Language (SSML).

(dict) --
The message object that provides the message text and its type.

contentType (string) --
The content type of the message string.

content (string) --
The text of the message.

groupNumber (integer) --
Identifies the message group that the message belongs to. When a group is assigned to a message, Amazon Lex returns one message from each group in the response.





maxAttempts (integer) --
The number of times to prompt the user for information.

responseCard (string) --
A response card. Amazon Lex uses this prompt at runtime, in the PostText API response. It substitutes session attributes and slot values for placeholders in the response card. For more information, see  ex-resp-card .



abortStatement (dict) --
The message that Amazon Lex uses to abort a conversation. For more information, see  PutBot .

messages (list) --
A collection of message objects.

(dict) --
The message object that provides the message text and its type.

contentType (string) --
The content type of the message string.

content (string) --
The text of the message.

groupNumber (integer) --
Identifies the message group that the message belongs to. When a group is assigned to a message, Amazon Lex returns one message from each group in the response.





responseCard (string) --
At runtime, if the client is using the PostText API, Amazon Lex includes the response card in the response. It substitutes all of the session attributes and slot values for placeholders in the response card.



status (string) --
When you send a request to create a bot with processBehavior set to BUILD , Amazon Lex sets the status response element to BUILDING .
In the READY_BASIC_TESTING state you can test the bot with user inputs that exactly match the utterances configured for the bot\'s intents and values in the slot types.
If Amazon Lex can\'t build the bot, Amazon Lex sets status to FAILED . Amazon Lex returns the reason for the failure in the failureReason response element.
When you set processBehavior to SAVE , Amazon Lex sets the status code to NOT BUILT .
When the bot is in the READY state you can test and publish the bot.

failureReason (string) --
If status is FAILED , Amazon Lex provides the reason that it failed to build the bot.

lastUpdatedDate (datetime) --
The date that the bot was updated. When you create a resource, the creation date and last updated date are the same.

createdDate (datetime) --
The date that the bot was created.

idleSessionTTLInSeconds (integer) --
The maximum length of time that Amazon Lex retains the data gathered in a conversation. For more information, see  PutBot .

voiceId (string) --
The Amazon Polly voice ID that Amazon Lex uses for voice interaction with the user. For more information, see  PutBot .

checksum (string) --
Checksum of the bot that you created.

version (string) --
The version of the bot. For a new bot, the version is always $LATEST .

locale (string) --
The target locale for the bot.

childDirected (boolean) --
For each Amazon Lex bot created with the Amazon Lex Model Building Service, you must specify whether your use of Amazon Lex is related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to the Children\'s Online Privacy Protection Act (COPPA) by specifying true or false in the childDirected field. By specifying true in the childDirected field, you confirm that your use of Amazon Lex is related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA. By specifying false in the childDirected field, you confirm that your use of Amazon Lex is not related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA. You may not specify a default value for the childDirected field that does not accurately reflect whether your use of Amazon Lex is related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA.
If your use of Amazon Lex relates to a website, program, or other application that is directed in whole or in part, to children under age 13, you must obtain any required verifiable parental consent under COPPA. For information regarding the use of Amazon Lex in connection with websites, programs, or other applications that are directed or targeted, in whole or in part, to children under age 13, see the Amazon Lex FAQ.

createVersion (boolean) --

True if a new version of the bot was created. If the createVersion field was not specified in the request, the createVersion field is set to false in the response.


detectSentiment (boolean) --

true if the bot is configured to send user utterances to Amazon Comprehend for sentiment analysis. If the detectSentiment field was not specified in the request, the detectSentiment field is false in the response.


tags (list) --
A list of tags associated with the bot.

(dict) --
A list of key/value pairs that identify a bot, bot alias, or bot channel. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.

key (string) --
The key for the tag. Keys are not case-sensitive and must be unique.

value (string) --
The value associated with a key. The value may be an empty string but it can\'t be null.











Exceptions

LexModelBuildingService.Client.exceptions.ConflictException
LexModelBuildingService.Client.exceptions.LimitExceededException
LexModelBuildingService.Client.exceptions.InternalFailureException
LexModelBuildingService.Client.exceptions.BadRequestException
LexModelBuildingService.Client.exceptions.PreconditionFailedException

Examples
This example shows how to create a bot for ordering pizzas.
response = client.put_bot(
    name='DocOrderPizzaBot',
    abortStatement={
        'messages': [
            {
                'content': 'I don't understand. Can you try again?',
                'contentType': 'PlainText',
            },
            {
                'content': 'I'm sorry, I don't understand.',
                'contentType': 'PlainText',
            },
        ],
    },
    childDirected=True,
    clarificationPrompt={
        'maxAttempts': 1,
        'messages': [
            {
                'content': 'I'm sorry, I didn't hear that. Can you repeate what you just said?',
                'contentType': 'PlainText',
            },
            {
                'content': 'Can you say that again?',
                'contentType': 'PlainText',
            },
        ],
    },
    description='Orders a pizza from a local pizzeria.',
    idleSessionTTLInSeconds=300,
    intents=[
        {
            'intentName': 'DocOrderPizza',
            'intentVersion': '$LATEST',
        },
    ],
    locale='en-US',
    processBehavior='SAVE',
)

print(response)


Expected Output:
{
    'version': '$LATEST',
    'name': 'DocOrderPizzaBot',
    'abortStatement': {
        'messages': [
            {
                'content': 'I don't understand. Can you try again?',
                'contentType': 'PlainText',
            },
            {
                'content': 'I'm sorry, I don't understand.',
                'contentType': 'PlainText',
            },
        ],
    },
    'checksum': '20172ee3-fa06-49b2-bbc5-667c090303e9',
    'childDirected': True,
    'clarificationPrompt': {
        'maxAttempts': 1,
        'messages': [
            {
                'content': 'I'm sorry, I didn't hear that. Can you repeate what you just said?',
                'contentType': 'PlainText',
            },
            {
                'content': 'Can you say that again?',
                'contentType': 'PlainText',
            },
        ],
    },
    'createdDate': 1494360160.133,
    'description': 'Orders a pizza from a local pizzeria.',
    'idleSessionTTLInSeconds': 300,
    'intents': [
        {
            'intentName': 'DocOrderPizza',
            'intentVersion': '$LATEST',
        },
    ],
    'lastUpdatedDate': 1494360160.133,
    'locale': 'en-US',
    'status': 'NOT_BUILT',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'name': 'string',
        'description': 'string',
        'intents': [
            {
                'intentName': 'string',
                'intentVersion': 'string'
            },
        ],
        'clarificationPrompt': {
            'messages': [
                {
                    'contentType': 'PlainText'|'SSML'|'CustomPayload',
                    'content': 'string',
                    'groupNumber': 123
                },
            ],
            'maxAttempts': 123,
            'responseCard': 'string'
        },
        'abortStatement': {
            'messages': [
                {
                    'contentType': 'PlainText'|'SSML'|'CustomPayload',
                    'content': 'string',
                    'groupNumber': 123
                },
            ],
            'responseCard': 'string'
        },
        'status': 'BUILDING'|'READY'|'READY_BASIC_TESTING'|'FAILED'|'NOT_BUILT',
        'failureReason': 'string',
        'lastUpdatedDate': datetime(2015, 1, 1),
        'createdDate': datetime(2015, 1, 1),
        'idleSessionTTLInSeconds': 123,
        'voiceId': 'string',
        'checksum': 'string',
        'version': 'string',
        'locale': 'en-US'|'en-GB'|'de-DE',
        'childDirected': True|False,
        'createVersion': True|False,
        'detectSentiment': True|False,
        'tags': [
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    }
    
    
    :returns: 
    LexModelBuildingService.Client.exceptions.ConflictException
    LexModelBuildingService.Client.exceptions.LimitExceededException
    LexModelBuildingService.Client.exceptions.InternalFailureException
    LexModelBuildingService.Client.exceptions.BadRequestException
    LexModelBuildingService.Client.exceptions.PreconditionFailedException
    
    """
    pass

def put_bot_alias(name=None, description=None, botVersion=None, botName=None, checksum=None, conversationLogs=None, tags=None):
    """
    Creates an alias for the specified version of the bot or replaces an alias for the specified bot. To change the version of the bot that the alias points to, replace the alias. For more information about aliases, see  versioning-aliases .
    This operation requires permissions for the lex:PutBotAlias action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_bot_alias(
        name='string',
        description='string',
        botVersion='string',
        botName='string',
        checksum='string',
        conversationLogs={
            'logSettings': [
                {
                    'logType': 'AUDIO'|'TEXT',
                    'destination': 'CLOUDWATCH_LOGS'|'S3',
                    'kmsKeyArn': 'string',
                    'resourceArn': 'string'
                },
            ],
            'iamRoleArn': 'string'
        },
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name of the alias. The name is not case sensitive.\n

    :type description: string
    :param description: A description of the alias.

    :type botVersion: string
    :param botVersion: [REQUIRED]\nThe version of the bot.\n

    :type botName: string
    :param botName: [REQUIRED]\nThe name of the bot.\n

    :type checksum: string
    :param checksum: Identifies a specific revision of the $LATEST version.\nWhen you create a new bot alias, leave the checksum field blank. If you specify a checksum you get a BadRequestException exception.\nWhen you want to update a bot alias, set the checksum field to the checksum of the most recent revision of the $LATEST version. If you don\'t specify the checksum field, or if the checksum does not match the $LATEST version, you get a PreconditionFailedException exception.\n

    :type conversationLogs: dict
    :param conversationLogs: Settings for conversation logs for the alias.\n\nlogSettings (list) -- [REQUIRED]The settings for your conversation logs. You can log the conversation text, conversation audio, or both.\n\n(dict) --Settings used to configure delivery mode and destination for conversation logs.\n\nlogType (string) -- [REQUIRED]The type of logging to enable. Text logs are delivered to a CloudWatch Logs log group. Audio logs are delivered to an S3 bucket.\n\ndestination (string) -- [REQUIRED]Where the logs will be delivered. Text logs are delivered to a CloudWatch Logs log group. Audio logs are delivered to an S3 bucket.\n\nkmsKeyArn (string) --The Amazon Resource Name (ARN) of the AWS KMS customer managed key for encrypting audio logs delivered to an S3 bucket. The key does not apply to CloudWatch Logs and is optional for S3 buckets.\n\nresourceArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the CloudWatch Logs log group or S3 bucket where the logs should be delivered.\n\n\n\n\n\niamRoleArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of an IAM role with permission to write to your CloudWatch Logs for text logs and your S3 bucket for audio logs. If audio encryption is enabled, this role also provides access permission for the AWS KMS key used for encrypting audio logs. For more information, see Creating an IAM Role and Policy for Conversation Logs .\n\n\n

    :type tags: list
    :param tags: A list of tags to add to the bot alias. You can only add tags when you create an alias, you can\'t use the PutBotAlias operation to update the tags on a bot alias. To update tags, use the TagResource operation.\n\n(dict) --A list of key/value pairs that identify a bot, bot alias, or bot channel. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.\n\nkey (string) -- [REQUIRED]The key for the tag. Keys are not case-sensitive and must be unique.\n\nvalue (string) -- [REQUIRED]The value associated with a key. The value may be an empty string but it can\'t be null.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'name': 'string',
    'description': 'string',
    'botVersion': 'string',
    'botName': 'string',
    'lastUpdatedDate': datetime(2015, 1, 1),
    'createdDate': datetime(2015, 1, 1),
    'checksum': 'string',
    'conversationLogs': {
        'logSettings': [
            {
                'logType': 'AUDIO'|'TEXT',
                'destination': 'CLOUDWATCH_LOGS'|'S3',
                'kmsKeyArn': 'string',
                'resourceArn': 'string',
                'resourcePrefix': 'string'
            },
        ],
        'iamRoleArn': 'string'
    },
    'tags': [
        {
            'key': 'string',
            'value': 'string'
        },
    ]
}


Response Structure

(dict) --

name (string) --
The name of the alias.

description (string) --
A description of the alias.

botVersion (string) --
The version of the bot that the alias points to.

botName (string) --
The name of the bot that the alias points to.

lastUpdatedDate (datetime) --
The date that the bot alias was updated. When you create a resource, the creation date and the last updated date are the same.

createdDate (datetime) --
The date that the bot alias was created.

checksum (string) --
The checksum for the current version of the alias.

conversationLogs (dict) --
The settings that determine how Amazon Lex uses conversation logs for the alias.

logSettings (list) --
The settings for your conversation logs. You can log text, audio, or both.

(dict) --
The settings for conversation logs.

logType (string) --
The type of logging that is enabled.

destination (string) --
The destination where logs are delivered.

kmsKeyArn (string) --
The Amazon Resource Name (ARN) of the key used to encrypt audio logs in an S3 bucket.

resourceArn (string) --
The Amazon Resource Name (ARN) of the CloudWatch Logs log group or S3 bucket where the logs are delivered.

resourcePrefix (string) --
The resource prefix is the first part of the S3 object key within the S3 bucket that you specified to contain audio logs. For CloudWatch Logs it is the prefix of the log stream name within the log group that you specified.





iamRoleArn (string) --
The Amazon Resource Name (ARN) of the IAM role used to write your logs to CloudWatch Logs or an S3 bucket.



tags (list) --
A list of tags associated with a bot.

(dict) --
A list of key/value pairs that identify a bot, bot alias, or bot channel. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.

key (string) --
The key for the tag. Keys are not case-sensitive and must be unique.

value (string) --
The value associated with a key. The value may be an empty string but it can\'t be null.











Exceptions

LexModelBuildingService.Client.exceptions.ConflictException
LexModelBuildingService.Client.exceptions.LimitExceededException
LexModelBuildingService.Client.exceptions.InternalFailureException
LexModelBuildingService.Client.exceptions.BadRequestException
LexModelBuildingService.Client.exceptions.PreconditionFailedException


    :return: {
        'name': 'string',
        'description': 'string',
        'botVersion': 'string',
        'botName': 'string',
        'lastUpdatedDate': datetime(2015, 1, 1),
        'createdDate': datetime(2015, 1, 1),
        'checksum': 'string',
        'conversationLogs': {
            'logSettings': [
                {
                    'logType': 'AUDIO'|'TEXT',
                    'destination': 'CLOUDWATCH_LOGS'|'S3',
                    'kmsKeyArn': 'string',
                    'resourceArn': 'string',
                    'resourcePrefix': 'string'
                },
            ],
            'iamRoleArn': 'string'
        },
        'tags': [
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    }
    
    
    :returns: 
    LexModelBuildingService.Client.exceptions.ConflictException
    LexModelBuildingService.Client.exceptions.LimitExceededException
    LexModelBuildingService.Client.exceptions.InternalFailureException
    LexModelBuildingService.Client.exceptions.BadRequestException
    LexModelBuildingService.Client.exceptions.PreconditionFailedException
    
    """
    pass

def put_intent(name=None, description=None, slots=None, sampleUtterances=None, confirmationPrompt=None, rejectionStatement=None, followUpPrompt=None, conclusionStatement=None, dialogCodeHook=None, fulfillmentActivity=None, parentIntentSignature=None, checksum=None, createVersion=None):
    """
    Creates an intent or replaces an existing intent.
    To define the interaction between the user and your bot, you use one or more intents. For a pizza ordering bot, for example, you would create an OrderPizza intent.
    To create an intent or replace an existing intent, you must provide the following:
    You can specify other optional information in the request, such as:
    If you specify an existing intent name to update the intent, Amazon Lex replaces the values in the $LATEST version of the intent with the values in the request. Amazon Lex removes fields that you don\'t provide in the request. If you don\'t specify the required fields, Amazon Lex throws an exception. When you update the $LATEST version of an intent, the status field of any bot that uses the $LATEST version of the intent is set to NOT_BUILT .
    For more information, see  how-it-works .
    This operation requires permissions for the lex:PutIntent action.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example shows how to create an intent for ordering pizzas.
    Expected Output:
    
    :example: response = client.put_intent(
        name='string',
        description='string',
        slots=[
            {
                'name': 'string',
                'description': 'string',
                'slotConstraint': 'Required'|'Optional',
                'slotType': 'string',
                'slotTypeVersion': 'string',
                'valueElicitationPrompt': {
                    'messages': [
                        {
                            'contentType': 'PlainText'|'SSML'|'CustomPayload',
                            'content': 'string',
                            'groupNumber': 123
                        },
                    ],
                    'maxAttempts': 123,
                    'responseCard': 'string'
                },
                'priority': 123,
                'sampleUtterances': [
                    'string',
                ],
                'responseCard': 'string',
                'obfuscationSetting': 'NONE'|'DEFAULT_OBFUSCATION'
            },
        ],
        sampleUtterances=[
            'string',
        ],
        confirmationPrompt={
            'messages': [
                {
                    'contentType': 'PlainText'|'SSML'|'CustomPayload',
                    'content': 'string',
                    'groupNumber': 123
                },
            ],
            'maxAttempts': 123,
            'responseCard': 'string'
        },
        rejectionStatement={
            'messages': [
                {
                    'contentType': 'PlainText'|'SSML'|'CustomPayload',
                    'content': 'string',
                    'groupNumber': 123
                },
            ],
            'responseCard': 'string'
        },
        followUpPrompt={
            'prompt': {
                'messages': [
                    {
                        'contentType': 'PlainText'|'SSML'|'CustomPayload',
                        'content': 'string',
                        'groupNumber': 123
                    },
                ],
                'maxAttempts': 123,
                'responseCard': 'string'
            },
            'rejectionStatement': {
                'messages': [
                    {
                        'contentType': 'PlainText'|'SSML'|'CustomPayload',
                        'content': 'string',
                        'groupNumber': 123
                    },
                ],
                'responseCard': 'string'
            }
        },
        conclusionStatement={
            'messages': [
                {
                    'contentType': 'PlainText'|'SSML'|'CustomPayload',
                    'content': 'string',
                    'groupNumber': 123
                },
            ],
            'responseCard': 'string'
        },
        dialogCodeHook={
            'uri': 'string',
            'messageVersion': 'string'
        },
        fulfillmentActivity={
            'type': 'ReturnIntent'|'CodeHook',
            'codeHook': {
                'uri': 'string',
                'messageVersion': 'string'
            }
        },
        parentIntentSignature='string',
        checksum='string',
        createVersion=True|False
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name of the intent. The name is not case sensitive.\nThe name can\'t match a built-in intent name, or a built-in intent name with 'AMAZON.' removed. For example, because there is a built-in intent called AMAZON.HelpIntent , you can\'t create a custom intent called HelpIntent .\nFor a list of built-in intents, see Standard Built-in Intents in the Alexa Skills Kit .\n

    :type description: string
    :param description: A description of the intent.

    :type slots: list
    :param slots: An array of intent slots. At runtime, Amazon Lex elicits required slot values from the user using prompts defined in the slots. For more information, see how-it-works .\n\n(dict) --Identifies the version of a specific slot.\n\nname (string) -- [REQUIRED]The name of the slot.\n\ndescription (string) --A description of the slot.\n\nslotConstraint (string) -- [REQUIRED]Specifies whether the slot is required or optional.\n\nslotType (string) --The type of the slot, either a custom slot type that you defined or one of the built-in slot types.\n\nslotTypeVersion (string) --The version of the slot type.\n\nvalueElicitationPrompt (dict) --The prompt that Amazon Lex uses to elicit the slot value from the user.\n\nmessages (list) -- [REQUIRED]An array of objects, each of which provides a message string and its type. You can specify the message string in plain text or in Speech Synthesis Markup Language (SSML).\n\n(dict) --The message object that provides the message text and its type.\n\ncontentType (string) -- [REQUIRED]The content type of the message string.\n\ncontent (string) -- [REQUIRED]The text of the message.\n\ngroupNumber (integer) --Identifies the message group that the message belongs to. When a group is assigned to a message, Amazon Lex returns one message from each group in the response.\n\n\n\n\n\nmaxAttempts (integer) -- [REQUIRED]The number of times to prompt the user for information.\n\nresponseCard (string) --A response card. Amazon Lex uses this prompt at runtime, in the PostText API response. It substitutes session attributes and slot values for placeholders in the response card. For more information, see ex-resp-card .\n\n\n\npriority (integer) --Directs Lex the order in which to elicit this slot value from the user. For example, if the intent has two slots with priorities 1 and 2, AWS Lex first elicits a value for the slot with priority 1.\nIf multiple slots share the same priority, the order in which Lex elicits values is arbitrary.\n\nsampleUtterances (list) --If you know a specific pattern with which users might respond to an Amazon Lex request for a slot value, you can provide those utterances to improve accuracy. This is optional. In most cases, Amazon Lex is capable of understanding user utterances.\n\n(string) --\n\n\nresponseCard (string) --A set of possible responses for the slot type used by text-based clients. A user chooses an option from the response card, instead of using text to reply.\n\nobfuscationSetting (string) --Determines whether a slot is obfuscated in conversation logs and stored utterances. When you obfuscate a slot, the value is replaced by the slot name in curly braces ({}). For example, if the slot name is 'full_name', obfuscated values are replaced with '{full_name}'. For more information, see Slot Obfuscation .\n\n\n\n\n

    :type sampleUtterances: list
    :param sampleUtterances: An array of utterances (strings) that a user might say to signal the intent. For example, 'I want {PizzaSize} pizza', 'Order {Quantity} {PizzaSize} pizzas'.\nIn each utterance, a slot name is enclosed in curly braces.\n\n(string) --\n\n

    :type confirmationPrompt: dict
    :param confirmationPrompt: Prompts the user to confirm the intent. This question should have a yes or no answer.\nAmazon Lex uses this prompt to ensure that the user acknowledges that the intent is ready for fulfillment. For example, with the OrderPizza intent, you might want to confirm that the order is correct before placing it. For other intents, such as intents that simply respond to user questions, you might not need to ask the user for confirmation before providing the information.\n\nNote\nYou you must provide both the rejectionStatement and the confirmationPrompt , or neither.\n\n\nmessages (list) -- [REQUIRED]An array of objects, each of which provides a message string and its type. You can specify the message string in plain text or in Speech Synthesis Markup Language (SSML).\n\n(dict) --The message object that provides the message text and its type.\n\ncontentType (string) -- [REQUIRED]The content type of the message string.\n\ncontent (string) -- [REQUIRED]The text of the message.\n\ngroupNumber (integer) --Identifies the message group that the message belongs to. When a group is assigned to a message, Amazon Lex returns one message from each group in the response.\n\n\n\n\n\nmaxAttempts (integer) -- [REQUIRED]The number of times to prompt the user for information.\n\nresponseCard (string) --A response card. Amazon Lex uses this prompt at runtime, in the PostText API response. It substitutes session attributes and slot values for placeholders in the response card. For more information, see ex-resp-card .\n\n\n

    :type rejectionStatement: dict
    :param rejectionStatement: When the user answers 'no' to the question defined in confirmationPrompt , Amazon Lex responds with this statement to acknowledge that the intent was canceled.\n\nNote\nYou must provide both the rejectionStatement and the confirmationPrompt , or neither.\n\n\nmessages (list) -- [REQUIRED]A collection of message objects.\n\n(dict) --The message object that provides the message text and its type.\n\ncontentType (string) -- [REQUIRED]The content type of the message string.\n\ncontent (string) -- [REQUIRED]The text of the message.\n\ngroupNumber (integer) --Identifies the message group that the message belongs to. When a group is assigned to a message, Amazon Lex returns one message from each group in the response.\n\n\n\n\n\nresponseCard (string) --At runtime, if the client is using the PostText API, Amazon Lex includes the response card in the response. It substitutes all of the session attributes and slot values for placeholders in the response card.\n\n\n

    :type followUpPrompt: dict
    :param followUpPrompt: Amazon Lex uses this prompt to solicit additional activity after fulfilling an intent. For example, after the OrderPizza intent is fulfilled, you might prompt the user to order a drink.\nThe action that Amazon Lex takes depends on the user\'s response, as follows:\n\nIf the user says 'Yes' it responds with the clarification prompt that is configured for the bot.\nif the user says 'Yes' and continues with an utterance that triggers an intent it starts a conversation for the intent.\nIf the user says 'No' it responds with the rejection statement configured for the the follow-up prompt.\nIf it doesn\'t recognize the utterance it repeats the follow-up prompt again.\n\nThe followUpPrompt field and the conclusionStatement field are mutually exclusive. You can specify only one.\n\nprompt (dict) -- [REQUIRED]Prompts for information from the user.\n\nmessages (list) -- [REQUIRED]An array of objects, each of which provides a message string and its type. You can specify the message string in plain text or in Speech Synthesis Markup Language (SSML).\n\n(dict) --The message object that provides the message text and its type.\n\ncontentType (string) -- [REQUIRED]The content type of the message string.\n\ncontent (string) -- [REQUIRED]The text of the message.\n\ngroupNumber (integer) --Identifies the message group that the message belongs to. When a group is assigned to a message, Amazon Lex returns one message from each group in the response.\n\n\n\n\n\nmaxAttempts (integer) -- [REQUIRED]The number of times to prompt the user for information.\n\nresponseCard (string) --A response card. Amazon Lex uses this prompt at runtime, in the PostText API response. It substitutes session attributes and slot values for placeholders in the response card. For more information, see ex-resp-card .\n\n\n\nrejectionStatement (dict) -- [REQUIRED]If the user answers 'no' to the question defined in the prompt field, Amazon Lex responds with this statement to acknowledge that the intent was canceled.\n\nmessages (list) -- [REQUIRED]A collection of message objects.\n\n(dict) --The message object that provides the message text and its type.\n\ncontentType (string) -- [REQUIRED]The content type of the message string.\n\ncontent (string) -- [REQUIRED]The text of the message.\n\ngroupNumber (integer) --Identifies the message group that the message belongs to. When a group is assigned to a message, Amazon Lex returns one message from each group in the response.\n\n\n\n\n\nresponseCard (string) --At runtime, if the client is using the PostText API, Amazon Lex includes the response card in the response. It substitutes all of the session attributes and slot values for placeholders in the response card.\n\n\n\n\n

    :type conclusionStatement: dict
    :param conclusionStatement: The statement that you want Amazon Lex to convey to the user after the intent is successfully fulfilled by the Lambda function.\nThis element is relevant only if you provide a Lambda function in the fulfillmentActivity . If you return the intent to the client application, you can\'t specify this element.\n\nNote\nThe followUpPrompt and conclusionStatement are mutually exclusive. You can specify only one.\n\n\nmessages (list) -- [REQUIRED]A collection of message objects.\n\n(dict) --The message object that provides the message text and its type.\n\ncontentType (string) -- [REQUIRED]The content type of the message string.\n\ncontent (string) -- [REQUIRED]The text of the message.\n\ngroupNumber (integer) --Identifies the message group that the message belongs to. When a group is assigned to a message, Amazon Lex returns one message from each group in the response.\n\n\n\n\n\nresponseCard (string) --At runtime, if the client is using the PostText API, Amazon Lex includes the response card in the response. It substitutes all of the session attributes and slot values for placeholders in the response card.\n\n\n

    :type dialogCodeHook: dict
    :param dialogCodeHook: Specifies a Lambda function to invoke for each user input. You can invoke this Lambda function to personalize user interaction.\nFor example, suppose your bot determines that the user is John. Your Lambda function might retrieve John\'s information from a backend database and prepopulate some of the values. For example, if you find that John is gluten intolerant, you might set the corresponding intent slot, GlutenIntolerant , to true. You might find John\'s phone number and set the corresponding session attribute.\n\nuri (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the Lambda function.\n\nmessageVersion (string) -- [REQUIRED]The version of the request-response that you want Amazon Lex to use to invoke your Lambda function. For more information, see using-lambda .\n\n\n

    :type fulfillmentActivity: dict
    :param fulfillmentActivity: Required. Describes how the intent is fulfilled. For example, after a user provides all of the information for a pizza order, fulfillmentActivity defines how the bot places an order with a local pizza store.\nYou might configure Amazon Lex to return all of the intent information to the client application, or direct it to invoke a Lambda function that can process the intent (for example, place an order with a pizzeria).\n\ntype (string) -- [REQUIRED]How the intent should be fulfilled, either by running a Lambda function or by returning the slot data to the client application.\n\ncodeHook (dict) --A description of the Lambda function that is run to fulfill the intent.\n\nuri (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the Lambda function.\n\nmessageVersion (string) -- [REQUIRED]The version of the request-response that you want Amazon Lex to use to invoke your Lambda function. For more information, see using-lambda .\n\n\n\n\n

    :type parentIntentSignature: string
    :param parentIntentSignature: A unique identifier for the built-in intent to base this intent on. To find the signature for an intent, see Standard Built-in Intents in the Alexa Skills Kit .

    :type checksum: string
    :param checksum: Identifies a specific revision of the $LATEST version.\nWhen you create a new intent, leave the checksum field blank. If you specify a checksum you get a BadRequestException exception.\nWhen you want to update a intent, set the checksum field to the checksum of the most recent revision of the $LATEST version. If you don\'t specify the checksum field, or if the checksum does not match the $LATEST version, you get a PreconditionFailedException exception.\n

    :type createVersion: boolean
    :param createVersion: When set to true a new numbered version of the intent is created. This is the same as calling the CreateIntentVersion operation. If you do not specify createVersion , the default is false .

    :rtype: dict

ReturnsResponse Syntax
{
    'name': 'string',
    'description': 'string',
    'slots': [
        {
            'name': 'string',
            'description': 'string',
            'slotConstraint': 'Required'|'Optional',
            'slotType': 'string',
            'slotTypeVersion': 'string',
            'valueElicitationPrompt': {
                'messages': [
                    {
                        'contentType': 'PlainText'|'SSML'|'CustomPayload',
                        'content': 'string',
                        'groupNumber': 123
                    },
                ],
                'maxAttempts': 123,
                'responseCard': 'string'
            },
            'priority': 123,
            'sampleUtterances': [
                'string',
            ],
            'responseCard': 'string',
            'obfuscationSetting': 'NONE'|'DEFAULT_OBFUSCATION'
        },
    ],
    'sampleUtterances': [
        'string',
    ],
    'confirmationPrompt': {
        'messages': [
            {
                'contentType': 'PlainText'|'SSML'|'CustomPayload',
                'content': 'string',
                'groupNumber': 123
            },
        ],
        'maxAttempts': 123,
        'responseCard': 'string'
    },
    'rejectionStatement': {
        'messages': [
            {
                'contentType': 'PlainText'|'SSML'|'CustomPayload',
                'content': 'string',
                'groupNumber': 123
            },
        ],
        'responseCard': 'string'
    },
    'followUpPrompt': {
        'prompt': {
            'messages': [
                {
                    'contentType': 'PlainText'|'SSML'|'CustomPayload',
                    'content': 'string',
                    'groupNumber': 123
                },
            ],
            'maxAttempts': 123,
            'responseCard': 'string'
        },
        'rejectionStatement': {
            'messages': [
                {
                    'contentType': 'PlainText'|'SSML'|'CustomPayload',
                    'content': 'string',
                    'groupNumber': 123
                },
            ],
            'responseCard': 'string'
        }
    },
    'conclusionStatement': {
        'messages': [
            {
                'contentType': 'PlainText'|'SSML'|'CustomPayload',
                'content': 'string',
                'groupNumber': 123
            },
        ],
        'responseCard': 'string'
    },
    'dialogCodeHook': {
        'uri': 'string',
        'messageVersion': 'string'
    },
    'fulfillmentActivity': {
        'type': 'ReturnIntent'|'CodeHook',
        'codeHook': {
            'uri': 'string',
            'messageVersion': 'string'
        }
    },
    'parentIntentSignature': 'string',
    'lastUpdatedDate': datetime(2015, 1, 1),
    'createdDate': datetime(2015, 1, 1),
    'version': 'string',
    'checksum': 'string',
    'createVersion': True|False
}


Response Structure

(dict) --

name (string) --
The name of the intent.

description (string) --
A description of the intent.

slots (list) --
An array of intent slots that are configured for the intent.

(dict) --
Identifies the version of a specific slot.

name (string) --
The name of the slot.

description (string) --
A description of the slot.

slotConstraint (string) --
Specifies whether the slot is required or optional.

slotType (string) --
The type of the slot, either a custom slot type that you defined or one of the built-in slot types.

slotTypeVersion (string) --
The version of the slot type.

valueElicitationPrompt (dict) --
The prompt that Amazon Lex uses to elicit the slot value from the user.

messages (list) --
An array of objects, each of which provides a message string and its type. You can specify the message string in plain text or in Speech Synthesis Markup Language (SSML).

(dict) --
The message object that provides the message text and its type.

contentType (string) --
The content type of the message string.

content (string) --
The text of the message.

groupNumber (integer) --
Identifies the message group that the message belongs to. When a group is assigned to a message, Amazon Lex returns one message from each group in the response.





maxAttempts (integer) --
The number of times to prompt the user for information.

responseCard (string) --
A response card. Amazon Lex uses this prompt at runtime, in the PostText API response. It substitutes session attributes and slot values for placeholders in the response card. For more information, see  ex-resp-card .



priority (integer) --
Directs Lex the order in which to elicit this slot value from the user. For example, if the intent has two slots with priorities 1 and 2, AWS Lex first elicits a value for the slot with priority 1.
If multiple slots share the same priority, the order in which Lex elicits values is arbitrary.

sampleUtterances (list) --
If you know a specific pattern with which users might respond to an Amazon Lex request for a slot value, you can provide those utterances to improve accuracy. This is optional. In most cases, Amazon Lex is capable of understanding user utterances.

(string) --


responseCard (string) --
A set of possible responses for the slot type used by text-based clients. A user chooses an option from the response card, instead of using text to reply.

obfuscationSetting (string) --
Determines whether a slot is obfuscated in conversation logs and stored utterances. When you obfuscate a slot, the value is replaced by the slot name in curly braces ({}). For example, if the slot name is "full_name", obfuscated values are replaced with "{full_name}". For more information, see Slot Obfuscation .





sampleUtterances (list) --
An array of sample utterances that are configured for the intent.

(string) --


confirmationPrompt (dict) --
If defined in the intent, Amazon Lex prompts the user to confirm the intent before fulfilling it.

messages (list) --
An array of objects, each of which provides a message string and its type. You can specify the message string in plain text or in Speech Synthesis Markup Language (SSML).

(dict) --
The message object that provides the message text and its type.

contentType (string) --
The content type of the message string.

content (string) --
The text of the message.

groupNumber (integer) --
Identifies the message group that the message belongs to. When a group is assigned to a message, Amazon Lex returns one message from each group in the response.





maxAttempts (integer) --
The number of times to prompt the user for information.

responseCard (string) --
A response card. Amazon Lex uses this prompt at runtime, in the PostText API response. It substitutes session attributes and slot values for placeholders in the response card. For more information, see  ex-resp-card .



rejectionStatement (dict) --
If the user answers "no" to the question defined in confirmationPrompt Amazon Lex responds with this statement to acknowledge that the intent was canceled.

messages (list) --
A collection of message objects.

(dict) --
The message object that provides the message text and its type.

contentType (string) --
The content type of the message string.

content (string) --
The text of the message.

groupNumber (integer) --
Identifies the message group that the message belongs to. When a group is assigned to a message, Amazon Lex returns one message from each group in the response.





responseCard (string) --
At runtime, if the client is using the PostText API, Amazon Lex includes the response card in the response. It substitutes all of the session attributes and slot values for placeholders in the response card.



followUpPrompt (dict) --
If defined in the intent, Amazon Lex uses this prompt to solicit additional user activity after the intent is fulfilled.

prompt (dict) --
Prompts for information from the user.

messages (list) --
An array of objects, each of which provides a message string and its type. You can specify the message string in plain text or in Speech Synthesis Markup Language (SSML).

(dict) --
The message object that provides the message text and its type.

contentType (string) --
The content type of the message string.

content (string) --
The text of the message.

groupNumber (integer) --
Identifies the message group that the message belongs to. When a group is assigned to a message, Amazon Lex returns one message from each group in the response.





maxAttempts (integer) --
The number of times to prompt the user for information.

responseCard (string) --
A response card. Amazon Lex uses this prompt at runtime, in the PostText API response. It substitutes session attributes and slot values for placeholders in the response card. For more information, see  ex-resp-card .



rejectionStatement (dict) --
If the user answers "no" to the question defined in the prompt field, Amazon Lex responds with this statement to acknowledge that the intent was canceled.

messages (list) --
A collection of message objects.

(dict) --
The message object that provides the message text and its type.

contentType (string) --
The content type of the message string.

content (string) --
The text of the message.

groupNumber (integer) --
Identifies the message group that the message belongs to. When a group is assigned to a message, Amazon Lex returns one message from each group in the response.





responseCard (string) --
At runtime, if the client is using the PostText API, Amazon Lex includes the response card in the response. It substitutes all of the session attributes and slot values for placeholders in the response card.





conclusionStatement (dict) --
After the Lambda function specified in the``fulfillmentActivity`` intent fulfills the intent, Amazon Lex conveys this statement to the user.

messages (list) --
A collection of message objects.

(dict) --
The message object that provides the message text and its type.

contentType (string) --
The content type of the message string.

content (string) --
The text of the message.

groupNumber (integer) --
Identifies the message group that the message belongs to. When a group is assigned to a message, Amazon Lex returns one message from each group in the response.





responseCard (string) --
At runtime, if the client is using the PostText API, Amazon Lex includes the response card in the response. It substitutes all of the session attributes and slot values for placeholders in the response card.



dialogCodeHook (dict) --
If defined in the intent, Amazon Lex invokes this Lambda function for each user input.

uri (string) --
The Amazon Resource Name (ARN) of the Lambda function.

messageVersion (string) --
The version of the request-response that you want Amazon Lex to use to invoke your Lambda function. For more information, see  using-lambda .



fulfillmentActivity (dict) --
If defined in the intent, Amazon Lex invokes this Lambda function to fulfill the intent after the user provides all of the information required by the intent.

type (string) --
How the intent should be fulfilled, either by running a Lambda function or by returning the slot data to the client application.

codeHook (dict) --
A description of the Lambda function that is run to fulfill the intent.

uri (string) --
The Amazon Resource Name (ARN) of the Lambda function.

messageVersion (string) --
The version of the request-response that you want Amazon Lex to use to invoke your Lambda function. For more information, see  using-lambda .





parentIntentSignature (string) --
A unique identifier for the built-in intent that this intent is based on.

lastUpdatedDate (datetime) --
The date that the intent was updated. When you create a resource, the creation date and last update dates are the same.

createdDate (datetime) --
The date that the intent was created.

version (string) --
The version of the intent. For a new intent, the version is always $LATEST .

checksum (string) --
Checksum of the $LATEST version of the intent created or updated.

createVersion (boolean) --

True if a new version of the intent was created. If the createVersion field was not specified in the request, the createVersion field is set to false in the response.








Exceptions

LexModelBuildingService.Client.exceptions.ConflictException
LexModelBuildingService.Client.exceptions.LimitExceededException
LexModelBuildingService.Client.exceptions.InternalFailureException
LexModelBuildingService.Client.exceptions.BadRequestException
LexModelBuildingService.Client.exceptions.PreconditionFailedException

Examples
This example shows how to create an intent for ordering pizzas.
response = client.put_intent(
    name='DocOrderPizza',
    conclusionStatement={
        'messages': [
            {
                'content': 'All right, I ordered  you a {Crust} crust {Type} pizza with {Sauce} sauce.',
                'contentType': 'PlainText',
            },
            {
                'content': 'OK, your {Crust} crust {Type} pizza with {Sauce} sauce is on the way.',
                'contentType': 'PlainText',
            },
        ],
        'responseCard': 'foo',
    },
    confirmationPrompt={
        'maxAttempts': 1,
        'messages': [
            {
                'content': 'Should I order  your {Crust} crust {Type} pizza with {Sauce} sauce?',
                'contentType': 'PlainText',
            },
        ],
    },
    description='Order a pizza from a local pizzeria.',
    fulfillmentActivity={
        'type': 'ReturnIntent',
    },
    rejectionStatement={
        'messages': [
            {
                'content': 'Ok, I'll cancel your order.',
                'contentType': 'PlainText',
            },
            {
                'content': 'I cancelled your order.',
                'contentType': 'PlainText',
            },
        ],
    },
    sampleUtterances=[
        'Order me a pizza.',
        'Order me a {Type} pizza.',
        'I want a {Crust} crust {Type} pizza',
        'I want a {Crust} crust {Type} pizza with {Sauce} sauce.',
    ],
    slots=[
        {
            'name': 'Type',
            'description': 'The type of pizza to order.',
            'priority': 1,
            'sampleUtterances': [
                'Get me a {Type} pizza.',
                'A {Type} pizza please.',
                'I'd like a {Type} pizza.',
            ],
            'slotConstraint': 'Required',
            'slotType': 'DocPizzaType',
            'slotTypeVersion': '$LATEST',
            'valueElicitationPrompt': {
                'maxAttempts': 1,
                'messages': [
                    {
                        'content': 'What type of pizza would you like?',
                        'contentType': 'PlainText',
                    },
                    {
                        'content': 'Vegie or cheese pizza?',
                        'contentType': 'PlainText',
                    },
                    {
                        'content': 'I can get you a vegie or a cheese pizza.',
                        'contentType': 'PlainText',
                    },
                ],
            },
        },
        {
            'name': 'Crust',
            'description': 'The type of pizza crust to order.',
            'priority': 2,
            'sampleUtterances': [
                'Make it a {Crust} crust.',
                'I'd like a {Crust} crust.',
            ],
            'slotConstraint': 'Required',
            'slotType': 'DocPizzaCrustType',
            'slotTypeVersion': '$LATEST',
            'valueElicitationPrompt': {
                'maxAttempts': 1,
                'messages': [
                    {
                        'content': 'What type of crust would you like?',
                        'contentType': 'PlainText',
                    },
                    {
                        'content': 'Thick or thin crust?',
                        'contentType': 'PlainText',
                    },
                ],
            },
        },
        {
            'name': 'Sauce',
            'description': 'The type of sauce to use on the pizza.',
            'priority': 3,
            'sampleUtterances': [
                'Make it {Sauce} sauce.',
                'I'd like {Sauce} sauce.',
            ],
            'slotConstraint': 'Required',
            'slotType': 'DocPizzaSauceType',
            'slotTypeVersion': '$LATEST',
            'valueElicitationPrompt': {
                'maxAttempts': 1,
                'messages': [
                    {
                        'content': 'White or red sauce?',
                        'contentType': 'PlainText',
                    },
                    {
                        'content': 'Garlic or tomato sauce?',
                        'contentType': 'PlainText',
                    },
                ],
            },
        },
    ],
)

print(response)


Expected Output:
{
    'version': '$LATEST',
    'name': 'DocOrderPizza',
    'checksum': 'ca9bc13d-afc8-4706-bbaf-091f7a5935d6',
    'conclusionStatement': {
        'messages': [
            {
                'content': 'All right, I ordered  you a {Crust} crust {Type} pizza with {Sauce} sauce.',
                'contentType': 'PlainText',
            },
            {
                'content': 'OK, your {Crust} crust {Type} pizza with {Sauce} sauce is on the way.',
                'contentType': 'PlainText',
            },
        ],
        'responseCard': 'foo',
    },
    'confirmationPrompt': {
        'maxAttempts': 1,
        'messages': [
            {
                'content': 'Should I order  your {Crust} crust {Type} pizza with {Sauce} sauce?',
                'contentType': 'PlainText',
            },
        ],
    },
    'createdDate': 1494359783.453,
    'description': 'Order a pizza from a local pizzeria.',
    'fulfillmentActivity': {
        'type': 'ReturnIntent',
    },
    'lastUpdatedDate': 1494359783.453,
    'rejectionStatement': {
        'messages': [
            {
                'content': 'Ok, I'll cancel your order.',
                'contentType': 'PlainText',
            },
            {
                'content': 'I cancelled your order.',
                'contentType': 'PlainText',
            },
        ],
    },
    'sampleUtterances': [
        'Order me a pizza.',
        'Order me a {Type} pizza.',
        'I want a {Crust} crust {Type} pizza',
        'I want a {Crust} crust {Type} pizza with {Sauce} sauce.',
    ],
    'slots': [
        {
            'name': 'Sauce',
            'description': 'The type of sauce to use on the pizza.',
            'priority': 3,
            'sampleUtterances': [
                'Make it {Sauce} sauce.',
                'I'd like {Sauce} sauce.',
            ],
            'slotConstraint': 'Required',
            'slotType': 'DocPizzaSauceType',
            'slotTypeVersion': '$LATEST',
            'valueElicitationPrompt': {
                'maxAttempts': 1,
                'messages': [
                    {
                        'content': 'White or red sauce?',
                        'contentType': 'PlainText',
                    },
                    {
                        'content': 'Garlic or tomato sauce?',
                        'contentType': 'PlainText',
                    },
                ],
            },
        },
        {
            'name': 'Type',
            'description': 'The type of pizza to order.',
            'priority': 1,
            'sampleUtterances': [
                'Get me a {Type} pizza.',
                'A {Type} pizza please.',
                'I'd like a {Type} pizza.',
            ],
            'slotConstraint': 'Required',
            'slotType': 'DocPizzaType',
            'slotTypeVersion': '$LATEST',
            'valueElicitationPrompt': {
                'maxAttempts': 1,
                'messages': [
                    {
                        'content': 'What type of pizza would you like?',
                        'contentType': 'PlainText',
                    },
                    {
                        'content': 'Vegie or cheese pizza?',
                        'contentType': 'PlainText',
                    },
                    {
                        'content': 'I can get you a vegie or a cheese pizza.',
                        'contentType': 'PlainText',
                    },
                ],
            },
        },
        {
            'name': 'Crust',
            'description': 'The type of pizza crust to order.',
            'priority': 2,
            'sampleUtterances': [
                'Make it a {Crust} crust.',
                'I'd like a {Crust} crust.',
            ],
            'slotConstraint': 'Required',
            'slotType': 'DocPizzaCrustType',
            'slotTypeVersion': '$LATEST',
            'valueElicitationPrompt': {
                'maxAttempts': 1,
                'messages': [
                    {
                        'content': 'What type of crust would you like?',
                        'contentType': 'PlainText',
                    },
                    {
                        'content': 'Thick or thin crust?',
                        'contentType': 'PlainText',
                    },
                ],
            },
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'name': 'string',
        'description': 'string',
        'slots': [
            {
                'name': 'string',
                'description': 'string',
                'slotConstraint': 'Required'|'Optional',
                'slotType': 'string',
                'slotTypeVersion': 'string',
                'valueElicitationPrompt': {
                    'messages': [
                        {
                            'contentType': 'PlainText'|'SSML'|'CustomPayload',
                            'content': 'string',
                            'groupNumber': 123
                        },
                    ],
                    'maxAttempts': 123,
                    'responseCard': 'string'
                },
                'priority': 123,
                'sampleUtterances': [
                    'string',
                ],
                'responseCard': 'string',
                'obfuscationSetting': 'NONE'|'DEFAULT_OBFUSCATION'
            },
        ],
        'sampleUtterances': [
            'string',
        ],
        'confirmationPrompt': {
            'messages': [
                {
                    'contentType': 'PlainText'|'SSML'|'CustomPayload',
                    'content': 'string',
                    'groupNumber': 123
                },
            ],
            'maxAttempts': 123,
            'responseCard': 'string'
        },
        'rejectionStatement': {
            'messages': [
                {
                    'contentType': 'PlainText'|'SSML'|'CustomPayload',
                    'content': 'string',
                    'groupNumber': 123
                },
            ],
            'responseCard': 'string'
        },
        'followUpPrompt': {
            'prompt': {
                'messages': [
                    {
                        'contentType': 'PlainText'|'SSML'|'CustomPayload',
                        'content': 'string',
                        'groupNumber': 123
                    },
                ],
                'maxAttempts': 123,
                'responseCard': 'string'
            },
            'rejectionStatement': {
                'messages': [
                    {
                        'contentType': 'PlainText'|'SSML'|'CustomPayload',
                        'content': 'string',
                        'groupNumber': 123
                    },
                ],
                'responseCard': 'string'
            }
        },
        'conclusionStatement': {
            'messages': [
                {
                    'contentType': 'PlainText'|'SSML'|'CustomPayload',
                    'content': 'string',
                    'groupNumber': 123
                },
            ],
            'responseCard': 'string'
        },
        'dialogCodeHook': {
            'uri': 'string',
            'messageVersion': 'string'
        },
        'fulfillmentActivity': {
            'type': 'ReturnIntent'|'CodeHook',
            'codeHook': {
                'uri': 'string',
                'messageVersion': 'string'
            }
        },
        'parentIntentSignature': 'string',
        'lastUpdatedDate': datetime(2015, 1, 1),
        'createdDate': datetime(2015, 1, 1),
        'version': 'string',
        'checksum': 'string',
        'createVersion': True|False
    }
    
    
    :returns: 
    A confirmation prompt to ask the user to confirm an intent. For example, "Shall I order your pizza?"
    A conclusion statement to send to the user after the intent has been fulfilled. For example, "I placed your pizza order."
    A follow-up prompt that asks the user for additional activity. For example, asking "Do you want to order a drink with your pizza?"
    
    """
    pass

def put_slot_type(name=None, description=None, enumerationValues=None, checksum=None, valueSelectionStrategy=None, createVersion=None, parentSlotTypeSignature=None, slotTypeConfigurations=None):
    """
    Creates a custom slot type or replaces an existing custom slot type.
    To create a custom slot type, specify a name for the slot type and a set of enumeration values, which are the values that a slot of this type can assume. For more information, see  how-it-works .
    If you specify the name of an existing slot type, the fields in the request replace the existing values in the $LATEST version of the slot type. Amazon Lex removes the fields that you don\'t provide in the request. If you don\'t specify required fields, Amazon Lex throws an exception. When you update the $LATEST version of a slot type, if a bot uses the $LATEST version of an intent that contains the slot type, the bot\'s status field is set to NOT_BUILT .
    This operation requires permissions for the lex:PutSlotType action.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example shows how to create a slot type that describes pizza sauces.
    Expected Output:
    
    :example: response = client.put_slot_type(
        name='string',
        description='string',
        enumerationValues=[
            {
                'value': 'string',
                'synonyms': [
                    'string',
                ]
            },
        ],
        checksum='string',
        valueSelectionStrategy='ORIGINAL_VALUE'|'TOP_RESOLUTION',
        createVersion=True|False,
        parentSlotTypeSignature='string',
        slotTypeConfigurations=[
            {
                'regexConfiguration': {
                    'pattern': 'string'
                }
            },
        ]
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name of the slot type. The name is not case sensitive.\nThe name can\'t match a built-in slot type name, or a built-in slot type name with 'AMAZON.' removed. For example, because there is a built-in slot type called AMAZON.DATE , you can\'t create a custom slot type called DATE .\nFor a list of built-in slot types, see Slot Type Reference in the Alexa Skills Kit .\n

    :type description: string
    :param description: A description of the slot type.

    :type enumerationValues: list
    :param enumerationValues: A list of EnumerationValue objects that defines the values that the slot type can take. Each value can have a list of synonyms , which are additional values that help train the machine learning model about the values that it resolves for a slot.\nWhen Amazon Lex resolves a slot value, it generates a resolution list that contains up to five possible values for the slot. If you are using a Lambda function, this resolution list is passed to the function. If you are not using a Lambda function you can choose to return the value that the user entered or the first value in the resolution list as the slot value. The valueSelectionStrategy field indicates the option to use.\n\n(dict) --Each slot type can have a set of values. Each enumeration value represents a value the slot type can take.\nFor example, a pizza ordering bot could have a slot type that specifies the type of crust that the pizza should have. The slot type could include the values\n\nthick\nthin\nstuffed\n\n\nvalue (string) -- [REQUIRED]The value of the slot type.\n\nsynonyms (list) --Additional values related to the slot type value.\n\n(string) --\n\n\n\n\n\n

    :type checksum: string
    :param checksum: Identifies a specific revision of the $LATEST version.\nWhen you create a new slot type, leave the checksum field blank. If you specify a checksum you get a BadRequestException exception.\nWhen you want to update a slot type, set the checksum field to the checksum of the most recent revision of the $LATEST version. If you don\'t specify the checksum field, or if the checksum does not match the $LATEST version, you get a PreconditionFailedException exception.\n

    :type valueSelectionStrategy: string
    :param valueSelectionStrategy: Determines the slot resolution strategy that Amazon Lex uses to return slot type values. The field can be set to one of the following values:\n\nORIGINAL_VALUE - Returns the value entered by the user, if the user value is similar to the slot value.\nTOP_RESOLUTION - If there is a resolution list for the slot, return the first value in the resolution list as the slot type value. If there is no resolution list, null is returned.\n\nIf you don\'t specify the valueSelectionStrategy , the default is ORIGINAL_VALUE .\n

    :type createVersion: boolean
    :param createVersion: When set to true a new numbered version of the slot type is created. This is the same as calling the CreateSlotTypeVersion operation. If you do not specify createVersion , the default is false .

    :type parentSlotTypeSignature: string
    :param parentSlotTypeSignature: The built-in slot type used as the parent of the slot type. When you define a parent slot type, the new slot type has all of the same configuration as the parent.\nOnly AMAZON.AlphaNumeric is supported.\n

    :type slotTypeConfigurations: list
    :param slotTypeConfigurations: Configuration information that extends the parent built-in slot type. The configuration is added to the settings for the parent slot type.\n\n(dict) --Provides configuration information for a slot type.\n\nregexConfiguration (dict) --A regular expression used to validate the value of a slot.\n\npattern (string) -- [REQUIRED]A regular expression used to validate the value of a slot.\nUse a standard regular expression. Amazon Lex supports the following characters in the regular expression:\n\nA-Z, a-z\n0-9\nUnicode characters ('u<Unicode>')\n\nRepresent Unicode characters with four digits, for example 'u0041' or 'u005A'.\nThe following regular expression operators are not supported:\n\nInfinite repeaters: *, +, or {x,} with no upper bound.\nWild card (.)\n\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'name': 'string',
    'description': 'string',
    'enumerationValues': [
        {
            'value': 'string',
            'synonyms': [
                'string',
            ]
        },
    ],
    'lastUpdatedDate': datetime(2015, 1, 1),
    'createdDate': datetime(2015, 1, 1),
    'version': 'string',
    'checksum': 'string',
    'valueSelectionStrategy': 'ORIGINAL_VALUE'|'TOP_RESOLUTION',
    'createVersion': True|False,
    'parentSlotTypeSignature': 'string',
    'slotTypeConfigurations': [
        {
            'regexConfiguration': {
                'pattern': 'string'
            }
        },
    ]
}


Response Structure

(dict) --

name (string) --
The name of the slot type.

description (string) --
A description of the slot type.

enumerationValues (list) --
A list of EnumerationValue objects that defines the values that the slot type can take.

(dict) --
Each slot type can have a set of values. Each enumeration value represents a value the slot type can take.
For example, a pizza ordering bot could have a slot type that specifies the type of crust that the pizza should have. The slot type could include the values

thick
thin
stuffed


value (string) --
The value of the slot type.

synonyms (list) --
Additional values related to the slot type value.

(string) --






lastUpdatedDate (datetime) --
The date that the slot type was updated. When you create a slot type, the creation date and last update date are the same.

createdDate (datetime) --
The date that the slot type was created.

version (string) --
The version of the slot type. For a new slot type, the version is always $LATEST .

checksum (string) --
Checksum of the $LATEST version of the slot type.

valueSelectionStrategy (string) --
The slot resolution strategy that Amazon Lex uses to determine the value of the slot. For more information, see  PutSlotType .

createVersion (boolean) --

True if a new version of the slot type was created. If the createVersion field was not specified in the request, the createVersion field is set to false in the response.


parentSlotTypeSignature (string) --
The built-in slot type used as the parent of the slot type.

slotTypeConfigurations (list) --
Configuration information that extends the parent built-in slot type.

(dict) --
Provides configuration information for a slot type.

regexConfiguration (dict) --
A regular expression used to validate the value of a slot.

pattern (string) --
A regular expression used to validate the value of a slot.
Use a standard regular expression. Amazon Lex supports the following characters in the regular expression:

A-Z, a-z
0-9
Unicode characters ("u<Unicode>")

Represent Unicode characters with four digits, for example "u0041" or "u005A".
The following regular expression operators are not supported:

Infinite repeaters: *, +, or {x,} with no upper bound.
Wild card (.)














Exceptions

LexModelBuildingService.Client.exceptions.ConflictException
LexModelBuildingService.Client.exceptions.LimitExceededException
LexModelBuildingService.Client.exceptions.InternalFailureException
LexModelBuildingService.Client.exceptions.BadRequestException
LexModelBuildingService.Client.exceptions.PreconditionFailedException

Examples
This example shows how to create a slot type that describes pizza sauces.
response = client.put_slot_type(
    name='PizzaSauceType',
    description='Available pizza sauces',
    enumerationValues=[
        {
            'value': 'red',
        },
        {
            'value': 'white',
        },
    ],
)

print(response)


Expected Output:
{
    'version': '$LATEST',
    'name': 'DocPizzaSauceType',
    'checksum': 'cfd00ed1-775d-4357-947c-aca7e73b44ba',
    'createdDate': 1494356442.23,
    'description': 'Available pizza sauces',
    'enumerationValues': [
        {
            'value': 'red',
        },
        {
            'value': 'white',
        },
    ],
    'lastUpdatedDate': 1494356442.23,
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'name': 'string',
        'description': 'string',
        'enumerationValues': [
            {
                'value': 'string',
                'synonyms': [
                    'string',
                ]
            },
        ],
        'lastUpdatedDate': datetime(2015, 1, 1),
        'createdDate': datetime(2015, 1, 1),
        'version': 'string',
        'checksum': 'string',
        'valueSelectionStrategy': 'ORIGINAL_VALUE'|'TOP_RESOLUTION',
        'createVersion': True|False,
        'parentSlotTypeSignature': 'string',
        'slotTypeConfigurations': [
            {
                'regexConfiguration': {
                    'pattern': 'string'
                }
            },
        ]
    }
    
    
    :returns: 
    thick
    thin
    stuffed
    
    """
    pass

def start_import(payload=None, resourceType=None, mergeStrategy=None, tags=None):
    """
    Starts a job to import a resource to Amazon Lex.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_import(
        payload=b'bytes',
        resourceType='BOT'|'INTENT'|'SLOT_TYPE',
        mergeStrategy='OVERWRITE_LATEST'|'FAIL_ON_CONFLICT',
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type payload: bytes
    :param payload: [REQUIRED]\nA zip archive in binary format. The archive should contain one file, a JSON file containing the resource to import. The resource should match the type specified in the resourceType field.\n

    :type resourceType: string
    :param resourceType: [REQUIRED]\nSpecifies the type of resource to export. Each resource also exports any resources that it depends on.\n\nA bot exports dependent intents.\nAn intent exports dependent slot types.\n\n

    :type mergeStrategy: string
    :param mergeStrategy: [REQUIRED]\nSpecifies the action that the StartImport operation should take when there is an existing resource with the same name.\n\nFAIL_ON_CONFLICT - The import operation is stopped on the first conflict between a resource in the import file and an existing resource. The name of the resource causing the conflict is in the failureReason field of the response to the GetImport operation. OVERWRITE_LATEST - The import operation proceeds even if there is a conflict with an existing resource. The $LASTEST version of the existing resource is overwritten with the data from the import file.\n\n

    :type tags: list
    :param tags: A list of tags to add to the imported bot. You can only add tags when you import a bot, you can\'t add tags to an intent or slot type.\n\n(dict) --A list of key/value pairs that identify a bot, bot alias, or bot channel. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.\n\nkey (string) -- [REQUIRED]The key for the tag. Keys are not case-sensitive and must be unique.\n\nvalue (string) -- [REQUIRED]The value associated with a key. The value may be an empty string but it can\'t be null.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'name': 'string',
    'resourceType': 'BOT'|'INTENT'|'SLOT_TYPE',
    'mergeStrategy': 'OVERWRITE_LATEST'|'FAIL_ON_CONFLICT',
    'importId': 'string',
    'importStatus': 'IN_PROGRESS'|'COMPLETE'|'FAILED',
    'tags': [
        {
            'key': 'string',
            'value': 'string'
        },
    ],
    'createdDate': datetime(2015, 1, 1)
}


Response Structure

(dict) --

name (string) --
The name given to the import job.

resourceType (string) --
The type of resource to import.

mergeStrategy (string) --
The action to take when there is a merge conflict.

importId (string) --
The identifier for the specific import job.

importStatus (string) --
The status of the import job. If the status is FAILED , you can get the reason for the failure using the GetImport operation.

tags (list) --
A list of tags added to the imported bot.

(dict) --
A list of key/value pairs that identify a bot, bot alias, or bot channel. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.

key (string) --
The key for the tag. Keys are not case-sensitive and must be unique.

value (string) --
The value associated with a key. The value may be an empty string but it can\'t be null.





createdDate (datetime) --
A timestamp for the date and time that the import job was requested.







Exceptions

LexModelBuildingService.Client.exceptions.LimitExceededException
LexModelBuildingService.Client.exceptions.InternalFailureException
LexModelBuildingService.Client.exceptions.BadRequestException


    :return: {
        'name': 'string',
        'resourceType': 'BOT'|'INTENT'|'SLOT_TYPE',
        'mergeStrategy': 'OVERWRITE_LATEST'|'FAIL_ON_CONFLICT',
        'importId': 'string',
        'importStatus': 'IN_PROGRESS'|'COMPLETE'|'FAILED',
        'tags': [
            {
                'key': 'string',
                'value': 'string'
            },
        ],
        'createdDate': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    LexModelBuildingService.Client.exceptions.LimitExceededException
    LexModelBuildingService.Client.exceptions.InternalFailureException
    LexModelBuildingService.Client.exceptions.BadRequestException
    
    """
    pass

def tag_resource(resourceArn=None, tags=None):
    """
    Adds the specified tags to the specified resource. If a tag key already exists, the existing value is replaced with the new value.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        resourceArn='string',
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the bot, bot alias, or bot channel to tag.\n

    :type tags: list
    :param tags: [REQUIRED]\nA list of tag keys to add to the resource. If a tag key already exists, the existing value is replaced with the new value.\n\n(dict) --A list of key/value pairs that identify a bot, bot alias, or bot channel. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.\n\nkey (string) -- [REQUIRED]The key for the tag. Keys are not case-sensitive and must be unique.\n\nvalue (string) -- [REQUIRED]The value associated with a key. The value may be an empty string but it can\'t be null.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

LexModelBuildingService.Client.exceptions.NotFoundException
LexModelBuildingService.Client.exceptions.BadRequestException
LexModelBuildingService.Client.exceptions.ConflictException
LexModelBuildingService.Client.exceptions.InternalFailureException
LexModelBuildingService.Client.exceptions.LimitExceededException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_resource(resourceArn=None, tagKeys=None):
    """
    Removes tags from a bot, bot alias or bot channel.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        resourceArn='string',
        tagKeys=[
            'string',
        ]
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource to remove the tags from.\n

    :type tagKeys: list
    :param tagKeys: [REQUIRED]\nA list of tag keys to remove from the resource. If a tag key does not exist on the resource, it is ignored.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

LexModelBuildingService.Client.exceptions.NotFoundException
LexModelBuildingService.Client.exceptions.BadRequestException
LexModelBuildingService.Client.exceptions.ConflictException
LexModelBuildingService.Client.exceptions.InternalFailureException
LexModelBuildingService.Client.exceptions.LimitExceededException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

