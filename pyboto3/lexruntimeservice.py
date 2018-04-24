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
    :param operation_name: The operation name. This is the same name
            as the method name on the client. For example, if the
            method name is create_foo, and you'd normally invoke the
            operation as client.create_foo(**kwargs), if the
            create_foo operation can be paginated, you can use the
            call client.get_paginator('create_foo').

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

def get_waiter():
    """
    
    """
    pass

def post_content(botName=None, botAlias=None, userId=None, sessionAttributes=None, requestAttributes=None, contentType=None, accept=None, inputStream=None):
    """
    Sends user input (text or speech) to Amazon Lex. Clients use this API to send text and audio requests to Amazon Lex at runtime. Amazon Lex interprets the user input using the machine learning model that it built for the bot.
    The PostContent operation supports audio input at 8kHz and 16kHz. You can use 8kHz audio to achieve higher speech recognition accuracy in telephone audio applications.
    In response, Amazon Lex returns the next message to convey to the user. Consider the following example messages:
    Not all Amazon Lex messages require a response from the user. For example, conclusion statements do not require a response. Some messages require only a yes or no response. In addition to the message , Amazon Lex provides additional context about the message in the response that you can use to enhance client behavior, such as displaying the appropriate client user interface. Consider the following examples:
    In addition, Amazon Lex also returns your application-specific sessionAttributes . For more information, see Managing Conversation Context .
    See also: AWS API Documentation
    
    
    :example: response = client.post_content(
        botName='string',
        botAlias='string',
        userId='string',
        sessionAttributes={...}|[...]|123|123.4|'string'|True|None,
        requestAttributes={...}|[...]|123|123.4|'string'|True|None,
        contentType='string',
        accept='string',
        inputStream=b'bytes'|file
    )
    
    
    :type botName: string
    :param botName: [REQUIRED]
            Name of the Amazon Lex bot.
            

    :type botAlias: string
    :param botAlias: [REQUIRED]
            Alias of the Amazon Lex bot.
            

    :type userId: string
    :param userId: [REQUIRED]
            The ID of the client application user. Amazon Lex uses this to identify a user's conversation with your bot. At runtime, each request must contain the userID field.
            To decide the user ID to use for your application, consider the following factors.
            The userID field must not contain any personally identifiable information of the user, for example, name, personal identification numbers, or other end user personal information.
            If you want a user to start a conversation on one device and continue on another device, use a user-specific identifier.
            If you want the same user to be able to have two independent conversations on two different devices, choose a device-specific identifier.
            A user can't have two independent conversations with two different versions of the same bot. For example, a user can't have a conversation with the PROD and BETA versions of the same bot. If you anticipate that a user will need to have conversation with two different versions, for example, while testing, include the bot alias in the user ID to separate the two conversations.
            

    :type sessionAttributes: JSON serializable
    :param sessionAttributes: You pass this value as the x-amz-lex-session-attributes HTTP header.
            Application-specific information passed between Amazon Lex and a client application. The value must be a JSON serialized and base64 encoded map with string keys and values. The total size of the sessionAttributes and requestAttributes headers is limited to 12 KB.
            For more information, see Setting Session Attributes .
            

    :type requestAttributes: JSON serializable
    :param requestAttributes: You pass this value as the x-amz-lex-request-attributes HTTP header.
            Request-specific information passed between Amazon Lex and a client application. The value must be a JSON serialized and base64 encoded map with string keys and values. The total size of the requestAttributes and sessionAttributes headers is limited to 12 KB.
            The namespace x-amz-lex: is reserved for special attributes. Don't create any request attributes with the prefix x-amz-lex: .
            For more information, see Setting Request Attributes .
            

    :type contentType: string
    :param contentType: [REQUIRED]
            You pass this value as the Content-Type HTTP header.
            Indicates the audio format or text. The header value must start with one of the following prefixes:
            PCM format, audio data must be in little-endian byte order.
            audio/l16; rate=16000; channels=1
            audio/x-l16; sample-rate=16000; channel-count=1
            audio/lpcm; sample-rate=8000; sample-size-bits=16; channel-count=1; is-big-endian=false
            Opus format
            audio/x-cbr-opus-with-preamble; preamble-size=0; bit-rate=256000; frame-size-milliseconds=4
            Text format
            text/plain; charset=utf-8
            

    :type accept: string
    :param accept: You pass this value as the Accept HTTP header.
            The message Amazon Lex returns in the response can be either text or speech based on the Accept HTTP header value in the request.
            If the value is text/plain; charset=utf-8 , Amazon Lex returns text in the response.
            If the value begins with audio/ , Amazon Lex returns speech in the response. Amazon Lex uses Amazon Polly to generate the speech (using the configuration you specified in the Accept header). For example, if you specify audio/mpeg as the value, Amazon Lex returns speech in the MPEG format. The following are the accepted values:
            audio/mpeg
            audio/ogg
            audio/pcm
            text/plain; charset=utf-8
            audio/* (defaults to mpeg)
            

    :type inputStream: bytes or seekable file-like object
    :param inputStream: [REQUIRED]
            User input in PCM or Opus audio format or text format as described in the Content-Type HTTP header.
            You can stream audio data to Amazon Lex or you can create a local buffer that captures all of the audio data before sending. In general, you get better performance if you stream audio data rather than buffering the data locally.
            

    :rtype: dict
    :return: {
        'contentType': 'string',
        'intentName': 'string',
        'slots': {...}|[...]|123|123.4|'string'|True|None,
        'sessionAttributes': {...}|[...]|123|123.4|'string'|True|None,
        'message': 'string',
        'messageFormat': 'PlainText'|'CustomPayload'|'SSML'|'Composite',
        'dialogState': 'ElicitIntent'|'ConfirmIntent'|'ElicitSlot'|'Fulfilled'|'ReadyForFulfillment'|'Failed',
        'slotToElicit': 'string',
        'inputTranscript': 'string',
        'audioStream': StreamingBody()
    }
    
    
    :returns: 
    If the message is to elicit slot data, Amazon Lex returns the following context information:
    x-amz-lex-dialog-state header set to ElicitSlot
    x-amz-lex-intent-name header set to the intent name in the current context
    x-amz-lex-slot-to-elicit header set to the slot name for which the message is eliciting information
    x-amz-lex-slots header set to a map of slots configured for the intent with their current values
    
    
    If the message is a confirmation prompt, the x-amz-lex-dialog-state header is set to Confirmation and the x-amz-lex-slot-to-elicit header is omitted.
    If the message is a clarification prompt configured for the intent, indicating that the user intent is not understood, the x-amz-dialog-state header is set to ElicitIntent and the x-amz-slot-to-elicit header is omitted.
    
    """
    pass

def post_text(botName=None, botAlias=None, userId=None, sessionAttributes=None, requestAttributes=None, inputText=None):
    """
    Sends user input (text-only) to Amazon Lex. Client applications can use this API to send requests to Amazon Lex at runtime. Amazon Lex then interprets the user input using the machine learning model it built for the bot.
    In response, Amazon Lex returns the next message to convey to the user an optional responseCard to display. Consider the following example messages:
    Not all Amazon Lex messages require a user response. For example, a conclusion statement does not require a response. Some messages require only a "yes" or "no" user response. In addition to the message , Amazon Lex provides additional context about the message in the response that you might use to enhance client behavior, for example, to display the appropriate client user interface. These are the slotToElicit , dialogState , intentName , and slots fields in the response. Consider the following examples:
    In addition, Amazon Lex also returns your application-specific sessionAttributes . For more information, see Managing Conversation Context .
    See also: AWS API Documentation
    
    
    :example: response = client.post_text(
        botName='string',
        botAlias='string',
        userId='string',
        sessionAttributes={
            'string': 'string'
        },
        requestAttributes={
            'string': 'string'
        },
        inputText='string'
    )
    
    
    :type botName: string
    :param botName: [REQUIRED]
            The name of the Amazon Lex bot.
            

    :type botAlias: string
    :param botAlias: [REQUIRED]
            The alias of the Amazon Lex bot.
            

    :type userId: string
    :param userId: [REQUIRED]
            The ID of the client application user. Amazon Lex uses this to identify a user's conversation with your bot. At runtime, each request must contain the userID field.
            To decide the user ID to use for your application, consider the following factors.
            The userID field must not contain any personally identifiable information of the user, for example, name, personal identification numbers, or other end user personal information.
            If you want a user to start a conversation on one device and continue on another device, use a user-specific identifier.
            If you want the same user to be able to have two independent conversations on two different devices, choose a device-specific identifier.
            A user can't have two independent conversations with two different versions of the same bot. For example, a user can't have a conversation with the PROD and BETA versions of the same bot. If you anticipate that a user will need to have conversation with two different versions, for example, while testing, include the bot alias in the user ID to separate the two conversations.
            

    :type sessionAttributes: dict
    :param sessionAttributes: Application-specific information passed between Amazon Lex and a client application.
            For more information, see Setting Session Attributes .
            (string) --
            (string) --
            

    :type requestAttributes: dict
    :param requestAttributes: Request-specific information passed between Amazon Lex and a client application.
            The namespace x-amz-lex: is reserved for special attributes. Don't create any request attributes with the prefix x-amz-lex: .
            For more information, see Setting Request Attributes .
            (string) --
            (string) --
            

    :type inputText: string
    :param inputText: [REQUIRED]
            The text that the user entered (Amazon Lex interprets this text).
            

    :rtype: dict
    :return: {
        'intentName': 'string',
        'slots': {
            'string': 'string'
        },
        'sessionAttributes': {
            'string': 'string'
        },
        'message': 'string',
        'messageFormat': 'PlainText'|'CustomPayload'|'SSML'|'Composite',
        'dialogState': 'ElicitIntent'|'ConfirmIntent'|'ElicitSlot'|'Fulfilled'|'ReadyForFulfillment'|'Failed',
        'slotToElicit': 'string',
        'responseCard': {
            'version': 'string',
            'contentType': 'application/vnd.amazonaws.card.generic',
            'genericAttachments': [
                {
                    'title': 'string',
                    'subTitle': 'string',
                    'attachmentLinkUrl': 'string',
                    'imageUrl': 'string',
                    'buttons': [
                        {
                            'text': 'string',
                            'value': 'string'
                        },
                    ]
                },
            ]
        }
    }
    
    
    :returns: 
    If the message is to elicit slot data, Amazon Lex returns the following context information:
    dialogState set to ElicitSlot
    intentName set to the intent name in the current context
    slotToElicit set to the slot name for which the message is eliciting information
    slots set to a map of slots, configured for the intent, with currently known values
    
    
    If the message is a confirmation prompt, the dialogState is set to ConfirmIntent and SlotToElicit is set to null.
    If the message is a clarification prompt (configured for the intent) that indicates that user intent is not understood, the dialogState is set to ElicitIntent and slotToElicit is set to null.
    
    """
    pass

