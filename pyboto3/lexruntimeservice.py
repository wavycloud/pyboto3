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

def post_content(botName=None, botAlias=None, userId=None, sessionAttributes=None, contentType=None, accept=None, inputStream=None):
    """
    Sends user input (text or speech) to Amazon Lex. Clients use this API to send requests to Amazon Lex at runtime. Amazon Lex interprets the user input using the machine learning model that it built for the bot.
    In response, Amazon Lex returns the next message to convey to the user. Consider the following example messages:
    Not all Amazon Lex messages require a response from the user. For example, conclusion statements do not require a response. Some messages require only a yes or no response. In addition to the message , Amazon Lex provides additional context about the message in the response that you can use to enhance client behavior, such as displaying the appropriate client user interface. Consider the following examples:
    In addition, Amazon Lex also returns your application-specific sessionAttributes . For more information, see Managing Conversation Context .
    See also: AWS API Documentation
    
    
    :example: response = client.post_content(
        botName='string',
        botAlias='string',
        userId='string',
        sessionAttributes={...}|[...]|123|123.4|'string'|True|None,
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
            ID of the client application user. Typically, each of your application users should have a unique ID. The application developer decides the user IDs. At runtime, each request must include the user ID. Note the following considerations:
            If you want a user to start conversation on one device and continue the conversation on another device, you might choose a user-specific identifier, such as the user's login, or Amazon Cognito user ID (assuming your application is using Amazon Cognito).
            If you want the same user to be able to have two independent conversations on two different devices, you might choose device-specific identifier, such as device ID, or some globally unique identifier.
            

    :type sessionAttributes: JSON serializable
    :param sessionAttributes: You pass this value in the x-amz-lex-session-attributes HTTP header. The value must be map (keys and values must be strings) that is JSON serialized and then base64 encoded.
            A session represents dialog between a user and Amazon Lex. At runtime, a client application can pass contextual information, in the request to Amazon Lex. For example,
            You might use session attributes to track the requestID of user requests.
            In Getting Started Exercise 1, the example bot uses the price session attribute to maintain the price of flowers ordered (for example, 'price':25). The code hook (Lambda function) sets this attribute based on the type of flowers ordered. For more information, see Review the Details of Information Flow .
            In the BookTrip bot exercise, the bot uses the currentReservation session attribute to maintains the slot data during the in-progress conversation to book a hotel or book a car. For more information, see Details of Information Flow .
            Amazon Lex passes these session attributes to the Lambda functions configured for the intent In the your Lambda function, you can use the session attributes for initialization and customization (prompts). Some examples are:
            Initialization - In a pizza ordering bot, if you pass user location (for example, 'Location : 111 Maple Street' ), then your Lambda function might use this information to determine the closest pizzeria to place the order (and perhaps set the storeAddress slot value as well). Personalized prompts - For example, you can configure prompts to refer to the user by name (for example, 'Hey [firstName], what toppings would you like?'). You can pass the user's name as a session attribute ('firstName': 'Joe') so that Amazon Lex can substitute the placeholder to provide a personalized prompt to the user ('Hey Joe, what toppings would you like?').
            Note
            Amazon Lex does not persist session attributes.
            If you configured a code hook for the intent, Amazon Lex passes the incoming session attributes to the Lambda function. The Lambda function must return these session attributes if you want Amazon Lex to return them to the client.
            If there is no code hook configured for the intent Amazon Lex simply returns the session attributes to the client application.
            

    :type contentType: string
    :param contentType: [REQUIRED]
            You pass this values as the Content-Type HTTP header.
            Indicates the audio format or text. The header value must start with one of the following prefixes:
            PCM format
            audio/l16; rate=16000; channels=1
            audio/x-l16; sample-rate=16000; channel-count=1
            Opus format
            audio/x-cbr-opus-with-preamble; preamble-size=0; bit-rate=1; frame-size-milliseconds=1.1
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
            

    :rtype: dict
    :return: {
        'contentType': 'string',
        'intentName': 'string',
        'slots': {...}|[...]|123|123.4|'string'|True|None,
        'sessionAttributes': {...}|[...]|123|123.4|'string'|True|None,
        'message': 'string',
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

def post_text(botName=None, botAlias=None, userId=None, sessionAttributes=None, inputText=None):
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
            The ID of the client application user. The application developer decides the user IDs. At runtime, each request must include the user ID. Typically, each of your application users should have a unique ID. Note the following considerations:
            If you want a user to start a conversation on one device and continue the conversation on another device, you might choose a user-specific identifier, such as a login or Amazon Cognito user ID (assuming your application is using Amazon Cognito).
            If you want the same user to be able to have two independent conversations on two different devices, you might choose a device-specific identifier, such as device ID, or some globally unique identifier.
            

    :type sessionAttributes: dict
    :param sessionAttributes: By using session attributes, a client application can pass contextual information in the request to Amazon Lex For example,
            In Getting Started Exercise 1, the example bot uses the price session attribute to maintain the price of the flowers ordered (for example, 'Price':25). The code hook (the Lambda function) sets this attribute based on the type of flowers ordered. For more information, see Review the Details of Information Flow .
            In the BookTrip bot exercise, the bot uses the currentReservation session attribute to maintain slot data during the in-progress conversation to book a hotel or book a car. For more information, see Details of Information Flow .
            You might use the session attributes (key, value pairs) to track the requestID of user requests.
            Amazon Lex simply passes these session attributes to the Lambda functions configured for the intent.
            In your Lambda function, you can also use the session attributes for initialization and customization (prompts and response cards). Some examples are:
            Initialization - In a pizza ordering bot, if you can pass the user location as a session attribute (for example, 'Location' : '111 Maple street' ), then your Lambda function might use this information to determine the closest pizzeria to place the order (perhaps to set the storeAddress slot value).
            Personalize prompts - For example, you can configure prompts to refer to the user name. (For example, 'Hey [FirstName], what toppings would you like?'). You can pass the user name as a session attribute ('FirstName' : 'Joe' ) so that Amazon Lex can substitute the placeholder to provide a personalize prompt to the user ('Hey Joe, what toppings would you like?').
            Note
            Amazon Lex does not persist session attributes.
            If you configure a code hook for the intent, Amazon Lex passes the incoming session attributes to the Lambda function. If you want Amazon Lex to return these session attributes back to the client, the Lambda function must return them.
            If there is no code hook configured for the intent, Amazon Lex simply returns the session attributes back to the client application.
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

