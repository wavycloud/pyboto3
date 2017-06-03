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

def create_bot_version(name=None, checksum=None):
    """
    Creates a new version of the bot based on the $LATEST version. If the $LATEST version of this resource hasn't changed since you created the last version, Amazon Lex doesn't create a new version. It returns the last created version.
    When you create the first version of a bot, Amazon Lex sets the version to 1. Subsequent versions increment by 1. For more information, see  versioning-intro .
    This operation requires permission for the lex:CreateBotVersion action.
    See also: AWS API Documentation
    
    
    :example: response = client.create_bot_version(
        name='string',
        checksum='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            The name of the bot that you want to create a new version of. The name is case sensitive.
            

    :type checksum: string
    :param checksum: Identifies a specific revision of the $LATEST version of the bot. If you specify a checksum and the $LATEST version of the bot has a different checksum, a PreconditionFailedException exception is returned and Amazon Lex doesn't publish a new version. If you don't specify a checksum, Amazon Lex publishes the $LATEST version.

    :rtype: dict
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
                    'contentType': 'PlainText'|'SSML',
                    'content': 'string'
                },
            ],
            'maxAttempts': 123,
            'responseCard': 'string'
        },
        'abortStatement': {
            'messages': [
                {
                    'contentType': 'PlainText'|'SSML',
                    'content': 'string'
                },
            ],
            'responseCard': 'string'
        },
        'status': 'BUILDING'|'READY'|'FAILED'|'NOT_BUILT',
        'failureReason': 'string',
        'lastUpdatedDate': datetime(2015, 1, 1),
        'createdDate': datetime(2015, 1, 1),
        'idleSessionTTLInSeconds': 123,
        'voiceId': 'string',
        'checksum': 'string',
        'version': 'string',
        'locale': 'en-US',
        'childDirected': True|False
    }
    
    
    """
    pass

def create_intent_version(name=None, checksum=None):
    """
    Creates a new version of an intent based on the $LATEST version of the intent. If the $LATEST version of this intent hasn't changed since you last updated it, Amazon Lex doesn't create a new version. It returns the last version you created.
    When you create a version of an intent, Amazon Lex sets the version to 1. Subsequent versions increment by 1. For more information, see  versioning-intro .
    This operation requires permissions to perform the lex:CreateIntentVersion action.
    See also: AWS API Documentation
    
    
    :example: response = client.create_intent_version(
        name='string',
        checksum='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            The name of the intent that you want to create a new version of. The name is case sensitive.
            

    :type checksum: string
    :param checksum: Checksum of the $LATEST version of the intent that should be used to create the new version. If you specify a checksum and the $LATEST version of the intent has a different checksum, Amazon Lex returns a PreconditionFailedException exception and doesn't publish a new version. If you don't specify a checksum, Amazon Lex publishes the $LATEST version.

    :rtype: dict
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
                            'contentType': 'PlainText'|'SSML',
                            'content': 'string'
                        },
                    ],
                    'maxAttempts': 123,
                    'responseCard': 'string'
                },
                'priority': 123,
                'sampleUtterances': [
                    'string',
                ],
                'responseCard': 'string'
            },
        ],
        'sampleUtterances': [
            'string',
        ],
        'confirmationPrompt': {
            'messages': [
                {
                    'contentType': 'PlainText'|'SSML',
                    'content': 'string'
                },
            ],
            'maxAttempts': 123,
            'responseCard': 'string'
        },
        'rejectionStatement': {
            'messages': [
                {
                    'contentType': 'PlainText'|'SSML',
                    'content': 'string'
                },
            ],
            'responseCard': 'string'
        },
        'followUpPrompt': {
            'prompt': {
                'messages': [
                    {
                        'contentType': 'PlainText'|'SSML',
                        'content': 'string'
                    },
                ],
                'maxAttempts': 123,
                'responseCard': 'string'
            },
            'rejectionStatement': {
                'messages': [
                    {
                        'contentType': 'PlainText'|'SSML',
                        'content': 'string'
                    },
                ],
                'responseCard': 'string'
            }
        },
        'conclusionStatement': {
            'messages': [
                {
                    'contentType': 'PlainText'|'SSML',
                    'content': 'string'
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
    Creates a new version of a slot type based on the $LATEST version of the specified slot type. If the $LATEST version of this resource has not changed since the last version that you created, Amazon Lex doesn't create a new version. It returns the last version that you created.
    When you create a version of a slot type, Amazon Lex sets the version to 1. Subsequent versions increment by 1. For more information, see  versioning-intro .
    This operation requires permissions for the lex:CreateSlotTypeVersion action.
    See also: AWS API Documentation
    
    
    :example: response = client.create_slot_type_version(
        name='string',
        checksum='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            The name of the slot type that you want to create a new version for. The name is case sensitive.
            

    :type checksum: string
    :param checksum: Checksum for the $LATEST version of the slot type that you want to publish. If you specify a checksum and the $LATEST version of the slot type has a different checksum, Amazon Lex returns a PreconditionFailedException exception and doesn't publish the new version. If you don't specify a checksum, Amazon Lex publishes the $LATEST version.

    :rtype: dict
    :return: {
        'name': 'string',
        'description': 'string',
        'enumerationValues': [
            {
                'value': 'string'
            },
        ],
        'lastUpdatedDate': datetime(2015, 1, 1),
        'createdDate': datetime(2015, 1, 1),
        'version': 'string',
        'checksum': 'string'
    }
    
    
    :returns: 
    thick
    thin
    stuffed
    
    """
    pass

def delete_bot(name=None):
    """
    Deletes all versions of the bot, including the $LATEST version. To delete a specific version of the bot, use the operation.
    If a bot has an alias, you can't delete it. Instead, the DeleteBot operation returns a ResourceInUseException exception that includes a reference to the alias that refers to the bot. To remove the reference to the bot, delete the alias. If you get the same exception again, delete the referring alias until the DeleteBot operation is successful.
    This operation requires permissions for the lex:DeleteBot action.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_bot(
        name='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            The name of the bot. The name is case sensitive.
            

    """
    pass

def delete_bot_alias(name=None, botName=None):
    """
    Deletes an alias for the specified bot.
    You can't delete an alias that is used in the association between a bot and a messaging channel. If an alias is used in a channel association, the DeleteBot operation returns a ResourceInUseException exception that includes a reference to the channel association that refers to the bot. You can remove the reference to the alias by deleting the channel association. If you get the same exception again, delete the referring association until the DeleteBotAlias operation is successful.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_bot_alias(
        name='string',
        botName='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            The name of the alias to delete. The name is case sensitive.
            

    :type botName: string
    :param botName: [REQUIRED]
            The name of the bot that the alias points to.
            

    """
    pass

def delete_bot_channel_association(name=None, botName=None, botAlias=None):
    """
    Deletes the association between an Amazon Lex bot and a messaging platform.
    This operation requires permission for the lex:DeleteBotChannelAssociation action.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_bot_channel_association(
        name='string',
        botName='string',
        botAlias='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            The name of the association. The name is case sensitive.
            

    :type botName: string
    :param botName: [REQUIRED]
            The name of the Amazon Lex bot.
            

    :type botAlias: string
    :param botAlias: [REQUIRED]
            An alias that points to the specific version of the Amazon Lex bot to which this association is being made.
            

    """
    pass

def delete_bot_version(name=None, version=None):
    """
    Deletes a specific version of a bot. To delete all versions of a bot, use the operation.
    This operation requires permissions for the lex:DeleteBotVersion action.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_bot_version(
        name='string',
        version='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            The name of the bot.
            

    :type version: string
    :param version: [REQUIRED]
            The version of the bot to delete. You cannot delete the $LATEST version of the bot. To delete the $LATEST version, use the operation.
            

    """
    pass

def delete_intent(name=None):
    """
    Deletes all versions of the intent, including the $LATEST version. To delete a specific version of the intent, use the operation.
    You can delete a version of an intent only if it is not referenced. To delete an intent that is referred to in one or more bots (see  how-it-works ), you must remove those references first.
    This operation requires permission for the lex:DeleteIntent action.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_intent(
        name='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            The name of the intent. The name is case sensitive.
            

    """
    pass

def delete_intent_version(name=None, version=None):
    """
    Deletes a specific version of an intent. To delete all versions of a intent, use the operation.
    This operation requires permissions for the lex:DeleteIntentVersion action.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_intent_version(
        name='string',
        version='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            The name of the intent.
            

    :type version: string
    :param version: [REQUIRED]
            The version of the intent to delete. You cannot delete the $LATEST version of the intent. To delete the $LATEST version, use the operation.
            

    """
    pass

def delete_slot_type(name=None):
    """
    Deletes all versions of the slot type, including the $LATEST version. To delete a specific version of the slot type, use the operation.
    You can delete a version of a slot type only if it is not referenced. To delete a slot type that is referred to in one or more intents, you must remove those references first.
    This operation requires permission for the lex:DeleteSlotType action.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_slot_type(
        name='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            The name of the slot type. The name is case sensitive.
            

    """
    pass

def delete_slot_type_version(name=None, version=None):
    """
    Deletes a specific version of a slot type. To delete all versions of a slot type, use the operation.
    This operation requires permissions for the lex:DeleteSlotTypeVersion action.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_slot_type_version(
        name='string',
        version='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            The name of the slot type.
            

    :type version: string
    :param version: [REQUIRED]
            The version of the slot type to delete. You cannot delete the $LATEST version of the slot type. To delete the $LATEST version, use the operation.
            

    """
    pass

def delete_utterances(botName=None, userId=None):
    """
    Deletes stored utterances.
    Amazon Lex stores the utterances that users send to your bot unless the childDirected field in the bot is set to true . Utterances are stored for 15 days for use with the operation, and then stored indefinately for use in improving the ability of your bot to respond to user input.
    Use the DeleteStoredUtterances operation to manually delete stored utterances for a specific user.
    This operation requires permissions for the lex:DeleteUtterances action.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_utterances(
        botName='string',
        userId='string'
    )
    
    
    :type botName: string
    :param botName: [REQUIRED]
            The name of the bot that stored the utterances.
            

    :type userId: string
    :param userId: [REQUIRED]
            The unique identifier for the user that made the utterances. This is the user ID that was sent in the or operation request that contained the utterance.
            

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

def get_bot(name=None, versionOrAlias=None):
    """
    Returns metadata information for a specific bot. You must provide the bot name and the bot version or alias.
    The GetBot operation requires permissions for the lex:GetBot action.
    See also: AWS API Documentation
    
    
    :example: response = client.get_bot(
        name='string',
        versionOrAlias='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            The name of the bot. The name is case sensitive.
            

    :type versionOrAlias: string
    :param versionOrAlias: [REQUIRED]
            The version or alias of the bot.
            

    :rtype: dict
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
                    'contentType': 'PlainText'|'SSML',
                    'content': 'string'
                },
            ],
            'maxAttempts': 123,
            'responseCard': 'string'
        },
        'abortStatement': {
            'messages': [
                {
                    'contentType': 'PlainText'|'SSML',
                    'content': 'string'
                },
            ],
            'responseCard': 'string'
        },
        'status': 'BUILDING'|'READY'|'FAILED'|'NOT_BUILT',
        'failureReason': 'string',
        'lastUpdatedDate': datetime(2015, 1, 1),
        'createdDate': datetime(2015, 1, 1),
        'idleSessionTTLInSeconds': 123,
        'voiceId': 'string',
        'checksum': 'string',
        'version': 'string',
        'locale': 'en-US',
        'childDirected': True|False
    }
    
    
    """
    pass

def get_bot_alias(name=None, botName=None):
    """
    Returns information about an Amazon Lex bot alias. For more information about aliases, see  versioning-aliases .
    This operation requires permissions for the lex:GetBotAlias action.
    See also: AWS API Documentation
    
    
    :example: response = client.get_bot_alias(
        name='string',
        botName='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            The name of the bot alias. The name is case sensitive.
            

    :type botName: string
    :param botName: [REQUIRED]
            The name of the bot.
            

    :rtype: dict
    :return: {
        'name': 'string',
        'description': 'string',
        'botVersion': 'string',
        'botName': 'string',
        'lastUpdatedDate': datetime(2015, 1, 1),
        'createdDate': datetime(2015, 1, 1),
        'checksum': 'string'
    }
    
    
    """
    pass

def get_bot_aliases(botName=None, nextToken=None, maxResults=None, nameContains=None):
    """
    Returns a list of aliases for a specified Amazon Lex bot.
    This operation requires permissions for the lex:GetBotAliases action.
    See also: AWS API Documentation
    
    
    :example: response = client.get_bot_aliases(
        botName='string',
        nextToken='string',
        maxResults=123,
        nameContains='string'
    )
    
    
    :type botName: string
    :param botName: [REQUIRED]
            The name of the bot.
            

    :type nextToken: string
    :param nextToken: A pagination token for fetching the next page of aliases. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of aliases, specify the pagination token in the next request.

    :type maxResults: integer
    :param maxResults: The maximum number of aliases to return in the response. The default is 50. .

    :type nameContains: string
    :param nameContains: Substring to match in bot alias names. An alias will be returned if any part of its name matches the substring. For example, 'xyz' matches both 'xyzabc' and 'abcxyz.'

    :rtype: dict
    :return: {
        'BotAliases': [
            {
                'name': 'string',
                'description': 'string',
                'botVersion': 'string',
                'botName': 'string',
                'lastUpdatedDate': datetime(2015, 1, 1),
                'createdDate': datetime(2015, 1, 1),
                'checksum': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def get_bot_channel_association(name=None, botName=None, botAlias=None):
    """
    Returns information about the association between an Amazon Lex bot and a messaging platform.
    This operation requires permissions for the lex:GetBotChannelAssociation action.
    See also: AWS API Documentation
    
    
    :example: response = client.get_bot_channel_association(
        name='string',
        botName='string',
        botAlias='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            The name of the association between the bot and the channel. The name is case sensitive.
            

    :type botName: string
    :param botName: [REQUIRED]
            The name of the Amazon Lex bot.
            

    :type botAlias: string
    :param botAlias: [REQUIRED]
            An alias pointing to the specific version of the Amazon Lex bot to which this association is being made.
            

    :rtype: dict
    :return: {
        'name': 'string',
        'description': 'string',
        'botAlias': 'string',
        'botName': 'string',
        'createdDate': datetime(2015, 1, 1),
        'type': 'Facebook'|'Slack'|'Twilio-Sms',
        'botConfiguration': {
            'string': 'string'
        }
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
    
    
    :example: response = client.get_bot_channel_associations(
        botName='string',
        botAlias='string',
        nextToken='string',
        maxResults=123,
        nameContains='string'
    )
    
    
    :type botName: string
    :param botName: [REQUIRED]
            The name of the Amazon Lex bot in the association.
            

    :type botAlias: string
    :param botAlias: [REQUIRED]
            An alias pointing to the specific version of the Amazon Lex bot to which this association is being made.
            

    :type nextToken: string
    :param nextToken: A pagination token for fetching the next page of associations. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of associations, specify the pagination token in the next request.

    :type maxResults: integer
    :param maxResults: The maximum number of associations to return in the response. The default is 50.

    :type nameContains: string
    :param nameContains: Substring to match in channel association names. An association will be returned if any part of its name matches the substring. For example, 'xyz' matches both 'xyzabc' and 'abcxyz.' To return all bot channel associations, use a hyphen ('-') as the nameContains parameter.

    :rtype: dict
    :return: {
        'botChannelAssociations': [
            {
                'name': 'string',
                'description': 'string',
                'botAlias': 'string',
                'botName': 'string',
                'createdDate': datetime(2015, 1, 1),
                'type': 'Facebook'|'Slack'|'Twilio-Sms',
                'botConfiguration': {
                    'string': 'string'
                }
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
    
    
    :example: response = client.get_bot_versions(
        name='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            The name of the bot for which versions should be returned.
            

    :type nextToken: string
    :param nextToken: A pagination token for fetching the next page of bot versions. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of versions, specify the pagination token in the next request.

    :type maxResults: integer
    :param maxResults: The maximum number of bot versions to return in the response. The default is 10.

    :rtype: dict
    :return: {
        'bots': [
            {
                'name': 'string',
                'description': 'string',
                'status': 'BUILDING'|'READY'|'FAILED'|'NOT_BUILT',
                'lastUpdatedDate': datetime(2015, 1, 1),
                'createdDate': datetime(2015, 1, 1),
                'version': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def get_bots(nextToken=None, maxResults=None, nameContains=None):
    """
    Returns bot information as follows:
    This operation requires permission for the lex:GetBots action.
    See also: AWS API Documentation
    
    
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
    :return: {
        'bots': [
            {
                'name': 'string',
                'description': 'string',
                'status': 'BUILDING'|'READY'|'FAILED'|'NOT_BUILT',
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
    
    
    :example: response = client.get_builtin_intent(
        signature='string'
    )
    
    
    :type signature: string
    :param signature: [REQUIRED]
            The unique identifier for a built-in intent. To find the signature for an intent, see Standard Built-in Intents in the Alexa Skills Kit .
            

    :rtype: dict
    :return: {
        'signature': 'string',
        'supportedLocales': [
            'en-US',
        ],
        'slots': [
            {
                'name': 'string'
            },
        ]
    }
    
    
    """
    pass

def get_builtin_intents(locale=None, signatureContains=None, nextToken=None, maxResults=None):
    """
    Gets a list of built-in intents that meet the specified criteria.
    This operation requires permission for the lex:GetBuiltinIntents action.
    See also: AWS API Documentation
    
    
    :example: response = client.get_builtin_intents(
        locale='en-US',
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
    :return: {
        'intents': [
            {
                'signature': 'string',
                'supportedLocales': [
                    'en-US',
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
    
    
    :example: response = client.get_builtin_slot_types(
        locale='en-US',
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
    :return: {
        'slotTypes': [
            {
                'signature': 'string',
                'supportedLocales': [
                    'en-US',
                ]
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_intent(name=None, version=None):
    """
    Returns information about an intent. In addition to the intent name, you must specify the intent version.
    This operation requires permissions to perform the lex:GetIntent action.
    See also: AWS API Documentation
    
    
    :example: response = client.get_intent(
        name='string',
        version='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            The name of the intent. The name is case sensitive.
            

    :type version: string
    :param version: [REQUIRED]
            The version of the intent.
            

    :rtype: dict
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
                            'contentType': 'PlainText'|'SSML',
                            'content': 'string'
                        },
                    ],
                    'maxAttempts': 123,
                    'responseCard': 'string'
                },
                'priority': 123,
                'sampleUtterances': [
                    'string',
                ],
                'responseCard': 'string'
            },
        ],
        'sampleUtterances': [
            'string',
        ],
        'confirmationPrompt': {
            'messages': [
                {
                    'contentType': 'PlainText'|'SSML',
                    'content': 'string'
                },
            ],
            'maxAttempts': 123,
            'responseCard': 'string'
        },
        'rejectionStatement': {
            'messages': [
                {
                    'contentType': 'PlainText'|'SSML',
                    'content': 'string'
                },
            ],
            'responseCard': 'string'
        },
        'followUpPrompt': {
            'prompt': {
                'messages': [
                    {
                        'contentType': 'PlainText'|'SSML',
                        'content': 'string'
                    },
                ],
                'maxAttempts': 123,
                'responseCard': 'string'
            },
            'rejectionStatement': {
                'messages': [
                    {
                        'contentType': 'PlainText'|'SSML',
                        'content': 'string'
                    },
                ],
                'responseCard': 'string'
            }
        },
        'conclusionStatement': {
            'messages': [
                {
                    'contentType': 'PlainText'|'SSML',
                    'content': 'string'
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
    
    
    :example: response = client.get_intent_versions(
        name='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            The name of the intent for which versions should be returned.
            

    :type nextToken: string
    :param nextToken: A pagination token for fetching the next page of intent versions. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of versions, specify the pagination token in the next request.

    :type maxResults: integer
    :param maxResults: The maximum number of intent versions to return in the response. The default is 10.

    :rtype: dict
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
    
    
    """
    pass

def get_intents(nextToken=None, maxResults=None, nameContains=None):
    """
    Returns intent information as follows:
    The operation requires permission for the lex:GetIntents action.
    See also: AWS API Documentation
    
    
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
    :param operation_name: The operation name. This is the same name
            as the method name on the client. For example, if the
            method name is create_foo, and you'd normally invoke the
            operation as client.create_foo(**kwargs), if the
            create_foo operation can be paginated, you can use the
            call client.get_paginator('create_foo').

    :rtype: L{botocore.paginate.Paginator}
    """
    pass

def get_slot_type(name=None, version=None):
    """
    Returns information about a specific version of a slot type. In addition to specifying the slot type name, you must specify the slot type version.
    This operation requires permissions for the lex:GetSlotType action.
    See also: AWS API Documentation
    
    
    :example: response = client.get_slot_type(
        name='string',
        version='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            The name of the slot type. The name is case sensitive.
            

    :type version: string
    :param version: [REQUIRED]
            The version of the slot type.
            

    :rtype: dict
    :return: {
        'name': 'string',
        'description': 'string',
        'enumerationValues': [
            {
                'value': 'string'
            },
        ],
        'lastUpdatedDate': datetime(2015, 1, 1),
        'createdDate': datetime(2015, 1, 1),
        'version': 'string',
        'checksum': 'string'
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
    
    
    :example: response = client.get_slot_type_versions(
        name='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            The name of the slot type for which versions should be returned.
            

    :type nextToken: string
    :param nextToken: A pagination token for fetching the next page of slot type versions. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of versions, specify the pagination token in the next request.

    :type maxResults: integer
    :param maxResults: The maximum number of slot type versions to return in the response. The default is 10.

    :rtype: dict
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
    
    
    """
    pass

def get_slot_types(nextToken=None, maxResults=None, nameContains=None):
    """
    Returns slot type information as follows:
    The operation requires permission for the lex:GetSlotTypes action.
    See also: AWS API Documentation
    
    
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
    Data is available for the last 15 days. You can request information for up to 5 versions in each request. The response contains information about a maximum of 100 utterances for each version.
    If the bot's childDirected field is set to true , utterances for the bot are not stored and cannot be retrieved with the GetUtterancesView operation. For more information, see .
    This operation requires permissions for the lex:GetUtterancesView action.
    See also: AWS API Documentation
    
    
    :example: response = client.get_utterances_view(
        botName='string',
        botVersions=[
            'string',
        ],
        statusType='Detected'|'Missed'
    )
    
    
    :type botName: string
    :param botName: [REQUIRED]
            The name of the bot for which utterance information should be returned.
            

    :type botVersions: list
    :param botVersions: [REQUIRED]
            An array of bot versions for which utterance information should be returned. The limit is 5 versions per request.
            (string) --
            

    :type statusType: string
    :param statusType: [REQUIRED]
            To return utterances that were recognized and handled, use``Detected`` . To return utterances that were not recognized, use Missed .
            

    :rtype: dict
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
    
    
    """
    pass

def get_waiter():
    """
    
    """
    pass

def put_bot(name=None, description=None, intents=None, clarificationPrompt=None, abortStatement=None, idleSessionTTLInSeconds=None, voiceId=None, checksum=None, processBehavior=None, locale=None, childDirected=None):
    """
    Creates an Amazon Lex conversational bot or replaces an existing bot. When you create or update a bot you only required to specify a name. You can use this to add intents later, or to remove intents from an existing bot. When you create a bot with a name only, the bot is created or updated but Amazon Lex returns the ```` response FAILED . You can build the bot after you add one or more intents. For more information about Amazon Lex bots, see  how-it-works .
    If you specify the name of an existing bot, the fields in the request replace the existing values in the $LATEST version of the bot. Amazon Lex removes any fields that you don't provide values for in the request, except for the idleTTLInSeconds and privacySettings fields, which are set to their default values. If you don't specify values for required fields, Amazon Lex throws an exception.
    This operation requires permissions for the lex:PutBot action. For more information, see  auth-and-access-control .
    See also: AWS API Documentation
    
    
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
                    'contentType': 'PlainText'|'SSML',
                    'content': 'string'
                },
            ],
            'maxAttempts': 123,
            'responseCard': 'string'
        },
        abortStatement={
            'messages': [
                {
                    'contentType': 'PlainText'|'SSML',
                    'content': 'string'
                },
            ],
            'responseCard': 'string'
        },
        idleSessionTTLInSeconds=123,
        voiceId='string',
        checksum='string',
        processBehavior='SAVE'|'BUILD',
        locale='en-US',
        childDirected=True|False
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            The name of the bot. The name is not case sensitive.
            

    :type description: string
    :param description: A description of the bot.

    :type intents: list
    :param intents: An array of Intent objects. Each intent represents a command that a user can express. For example, a pizza ordering bot might support an OrderPizza intent. For more information, see how-it-works .
            (dict) --Identifies the specific version of an intent.
            intentName (string) -- [REQUIRED]The name of the intent.
            intentVersion (string) -- [REQUIRED]The version of the intent.
            
            

    :type clarificationPrompt: dict
    :param clarificationPrompt: When Amazon Lex doesn't understand the user's intent, it uses one of these messages to get clarification. For example, 'Sorry, I didn't understand. Please repeat.' Amazon Lex repeats the clarification prompt the number of times specified in maxAttempts . If Amazon Lex still can't understand, it sends the message specified in abortStatement .
            messages (list) -- [REQUIRED]An array of objects, each of which provides a message string and its type. You can specify the message string in plain text or in Speech Synthesis Markup Language (SSML).
            (dict) --The message object that provides the message text and its type.
            contentType (string) -- [REQUIRED]The content type of the message string.
            content (string) -- [REQUIRED]The text of the message.
            
            maxAttempts (integer) -- [REQUIRED]The number of times to prompt the user for information.
            responseCard (string) --A response card. Amazon Lex uses this prompt at runtime, in the PostText API response. It substitutes session attributes and slot values for placeholders in the response card. For more information, see ex-resp-card .
            

    :type abortStatement: dict
    :param abortStatement: When Amazon Lex can't understand the user's input in context, it tries to elicit the information a few times. After that, Amazon Lex sends the message defined in abortStatement to the user, and then aborts the conversation. To set the number of retries, use the valueElicitationPrompt field for the slot type.
            For example, in a pizza ordering bot, Amazon Lex might ask a user 'What type of crust would you like?' If the user's response is not one of the expected responses (for example, 'thin crust, 'deep dish,' etc.), Amazon Lex tries to elicit a correct response a few more times.
            For example, in a pizza ordering application, OrderPizza might be one of the intents. This intent might require the CrustType slot. You specify the valueElicitationPrompt field when you create the CrustType slot.
            messages (list) -- [REQUIRED]A collection of message objects.
            (dict) --The message object that provides the message text and its type.
            contentType (string) -- [REQUIRED]The content type of the message string.
            content (string) -- [REQUIRED]The text of the message.
            
            responseCard (string) --At runtime, if the client is using the API, Amazon Lex includes the response card in the response. It substitutes all of the session attributes and slot values for placeholders in the response card.
            

    :type idleSessionTTLInSeconds: integer
    :param idleSessionTTLInSeconds: The maximum time in seconds that Amazon Lex retains the data gathered in a conversation.
            A user interaction session remains active for the amount of time specified. If no conversation occurs during this time, the session expires and Amazon Lex deletes any data provided before the timeout.
            For example, suppose that a user chooses the OrderPizza intent, but gets sidetracked halfway through placing an order. If the user doesn't complete the order within the specified time, Amazon Lex discards the slot information that it gathered, and the user must start over.
            If you don't include the idleSessionTTLInSeconds element in a PutBot operation request, Amazon Lex uses the default value. This is also true if the request replaces an existing bot.
            The default is 300 seconds (5 minutes).
            

    :type voiceId: string
    :param voiceId: The Amazon Polly voice ID that you want Amazon Lex to use for voice interactions with the user. The locale configured for the voice must match the locale of the bot. For more information, see Voice in the Amazon Polly Developer Guide .

    :type checksum: string
    :param checksum: Identifies a specific revision of the $LATEST version.
            When you create a new bot, leave the checksum field blank. If you specify a checksum you get a BadRequestException exception.
            When you want to update a bot, set the checksum field to the checksum of the most recent revision of the $LATEST version. If you don't specify the checksum field, or if the checksum does not match the $LATEST version, you get a PreconditionFailedException exception.
            

    :type processBehavior: string
    :param processBehavior: If you set the processBehavior element to Build , Amazon Lex builds the bot so that it can be run. If you set the element to Save Amazon Lex saves the bot, but doesn't build it.
            If you don't specify this value, the default value is Save .
            

    :type locale: string
    :param locale: [REQUIRED]
            Specifies the target locale for the bot. Any intent used in the bot must be compatible with the locale of the bot.
            The default is en-US .
            

    :type childDirected: boolean
    :param childDirected: [REQUIRED]
            For each Amazon Lex bot created with the Amazon Lex Model Building Service, you must specify whether your use of Amazon Lex is related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to the Children's Online Privacy Protection Act (COPPA) by specifying true or false in the childDirected field. By specifying true in the childDirected field, you confirm that your use of Amazon Lex is related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA. By specifying false in the childDirected field, you confirm that your use of Amazon Lex is not related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA. You may not specify a default value for the childDirected field that does not accurately reflect whether your use of Amazon Lex is related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA.
            If your use of Amazon Lex relates to a website, program, or other application that is directed in whole or in part, to children under age 13, you must obtain any required verifiable parental consent under COPPA. For information regarding the use of Amazon Lex in connection with websites, programs, or other applications that are directed or targeted, in whole or in part, to children under age 13, see the Amazon Lex FAQ.
            

    :rtype: dict
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
                    'contentType': 'PlainText'|'SSML',
                    'content': 'string'
                },
            ],
            'maxAttempts': 123,
            'responseCard': 'string'
        },
        'abortStatement': {
            'messages': [
                {
                    'contentType': 'PlainText'|'SSML',
                    'content': 'string'
                },
            ],
            'responseCard': 'string'
        },
        'status': 'BUILDING'|'READY'|'FAILED'|'NOT_BUILT',
        'failureReason': 'string',
        'lastUpdatedDate': datetime(2015, 1, 1),
        'createdDate': datetime(2015, 1, 1),
        'idleSessionTTLInSeconds': 123,
        'voiceId': 'string',
        'checksum': 'string',
        'version': 'string',
        'locale': 'en-US',
        'childDirected': True|False
    }
    
    
    """
    pass

def put_bot_alias(name=None, description=None, botVersion=None, botName=None, checksum=None):
    """
    Creates an alias for the specified version of the bot or replaces an alias for the specified bot. To change the version of the bot that the alias points to, replace the alias. For more information about aliases, see  versioning-aliases .
    This operation requires permissions for the lex:PutBotAlias action.
    See also: AWS API Documentation
    
    
    :example: response = client.put_bot_alias(
        name='string',
        description='string',
        botVersion='string',
        botName='string',
        checksum='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            The name of the alias. The name is not case sensitive.
            

    :type description: string
    :param description: A description of the alias.

    :type botVersion: string
    :param botVersion: [REQUIRED]
            The version of the bot.
            

    :type botName: string
    :param botName: [REQUIRED]
            The name of the bot.
            

    :type checksum: string
    :param checksum: Identifies a specific revision of the $LATEST version.
            When you create a new bot alias, leave the checksum field blank. If you specify a checksum you get a BadRequestException exception.
            When you want to update a bot alias, set the checksum field to the checksum of the most recent revision of the $LATEST version. If you don't specify the checksum field, or if the checksum does not match the $LATEST version, you get a PreconditionFailedException exception.
            

    :rtype: dict
    :return: {
        'name': 'string',
        'description': 'string',
        'botVersion': 'string',
        'botName': 'string',
        'lastUpdatedDate': datetime(2015, 1, 1),
        'createdDate': datetime(2015, 1, 1),
        'checksum': 'string'
    }
    
    
    """
    pass

def put_intent(name=None, description=None, slots=None, sampleUtterances=None, confirmationPrompt=None, rejectionStatement=None, followUpPrompt=None, conclusionStatement=None, dialogCodeHook=None, fulfillmentActivity=None, parentIntentSignature=None, checksum=None):
    """
    Creates an intent or replaces an existing intent.
    To define the interaction between the user and your bot, you use one or more intents. For a pizza ordering bot, for example, you would create an OrderPizza intent.
    To create an intent or replace an existing intent, you must provide the following:
    You can specify other optional information in the request, such as:
    If you specify an existing intent name to update the intent, Amazon Lex replaces the values in the $LATEST version of the slot type with the values in the request. Amazon Lex removes fields that you don't provide in the request. If you don't specify the required fields, Amazon Lex throws an exception.
    For more information, see  how-it-works .
    This operation requires permissions for the lex:PutIntent action.
    See also: AWS API Documentation
    
    
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
                            'contentType': 'PlainText'|'SSML',
                            'content': 'string'
                        },
                    ],
                    'maxAttempts': 123,
                    'responseCard': 'string'
                },
                'priority': 123,
                'sampleUtterances': [
                    'string',
                ],
                'responseCard': 'string'
            },
        ],
        sampleUtterances=[
            'string',
        ],
        confirmationPrompt={
            'messages': [
                {
                    'contentType': 'PlainText'|'SSML',
                    'content': 'string'
                },
            ],
            'maxAttempts': 123,
            'responseCard': 'string'
        },
        rejectionStatement={
            'messages': [
                {
                    'contentType': 'PlainText'|'SSML',
                    'content': 'string'
                },
            ],
            'responseCard': 'string'
        },
        followUpPrompt={
            'prompt': {
                'messages': [
                    {
                        'contentType': 'PlainText'|'SSML',
                        'content': 'string'
                    },
                ],
                'maxAttempts': 123,
                'responseCard': 'string'
            },
            'rejectionStatement': {
                'messages': [
                    {
                        'contentType': 'PlainText'|'SSML',
                        'content': 'string'
                    },
                ],
                'responseCard': 'string'
            }
        },
        conclusionStatement={
            'messages': [
                {
                    'contentType': 'PlainText'|'SSML',
                    'content': 'string'
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
        checksum='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            The name of the intent. The name is not case sensitive.
            The name can't match a built-in intent name, or a built-in intent name with 'AMAZON.' removed. For example, because there is a built-in intent called AMAZON.HelpIntent , you can't create a custom intent called HelpIntent .
            For a list of built-in intents, see Standard Built-in Intents in the Alexa Skills Kit .
            

    :type description: string
    :param description: A description of the intent.

    :type slots: list
    :param slots: An array of intent slots. At runtime, Amazon Lex elicits required slot values from the user using prompts defined in the slots. For more information, see xref linkend='how-it-works'/.
            (dict) --Identifies the version of a specific slot.
            name (string) -- [REQUIRED]The name of the slot.
            description (string) --A description of the slot.
            slotConstraint (string) -- [REQUIRED]Specifies whether the slot is required or optional.
            slotType (string) --The type of the slot, either a custom slot type that you defined or one of the built-in slot types.
            slotTypeVersion (string) --The version of the slot type.
            valueElicitationPrompt (dict) --The prompt that Amazon Lex uses to elicit the slot value from the user.
            messages (list) -- [REQUIRED]An array of objects, each of which provides a message string and its type. You can specify the message string in plain text or in Speech Synthesis Markup Language (SSML).
            (dict) --The message object that provides the message text and its type.
            contentType (string) -- [REQUIRED]The content type of the message string.
            content (string) -- [REQUIRED]The text of the message.
            
            maxAttempts (integer) -- [REQUIRED]The number of times to prompt the user for information.
            responseCard (string) --A response card. Amazon Lex uses this prompt at runtime, in the PostText API response. It substitutes session attributes and slot values for placeholders in the response card. For more information, see ex-resp-card .
            priority (integer) --Directs Lex the order in which to elicit this slot value from the user. For example, if the intent has two slots with priorities 1 and 2, AWS Lex first elicits a value for the slot with priority 1.
            If multiple slots share the same priority, the order in which Lex elicits values is arbitrary.
            sampleUtterances (list) --If you know a specific pattern with which users might respond to an Amazon Lex request for a slot value, you can provide those utterances to improve accuracy. This is optional. In most cases, Amazon Lex is capable of understanding user utterances.
            (string) --
            responseCard (string) --A set of possible responses for the slot type used by text-based clients. A user chooses an option from the response card, instead of using text to reply.
            
            

    :type sampleUtterances: list
    :param sampleUtterances: An array of utterances (strings) that a user might say to signal the intent. For example, 'I want {PizzaSize} pizza', 'Order {Quantity} {PizzaSize} pizzas'.
            In each utterance, a slot name is enclosed in curly braces.
            (string) --
            

    :type confirmationPrompt: dict
    :param confirmationPrompt: Prompts the user to confirm the intent. This question should have a yes or no answer.
            Amazon Lex uses this prompt to ensure that the user acknowledges that the intent is ready for fulfillment. For example, with the OrderPizza intent, you might want to confirm that the order is correct before placing it. For other intents, such as intents that simply respond to user questions, you might not need to ask the user for confirmation before providing the information.
            Note
            You you must provide both the rejectionStatement and the confirmationPrompt , or neither.
            messages (list) -- [REQUIRED]An array of objects, each of which provides a message string and its type. You can specify the message string in plain text or in Speech Synthesis Markup Language (SSML).
            (dict) --The message object that provides the message text and its type.
            contentType (string) -- [REQUIRED]The content type of the message string.
            content (string) -- [REQUIRED]The text of the message.
            
            maxAttempts (integer) -- [REQUIRED]The number of times to prompt the user for information.
            responseCard (string) --A response card. Amazon Lex uses this prompt at runtime, in the PostText API response. It substitutes session attributes and slot values for placeholders in the response card. For more information, see ex-resp-card .
            

    :type rejectionStatement: dict
    :param rejectionStatement: When the user answers 'no' to the question defined in confirmationPrompt , Amazon Lex responds with this statement to acknowledge that the intent was canceled.
            Note
            You must provide both the rejectionStatement and the confirmationPrompt , or neither.
            messages (list) -- [REQUIRED]A collection of message objects.
            (dict) --The message object that provides the message text and its type.
            contentType (string) -- [REQUIRED]The content type of the message string.
            content (string) -- [REQUIRED]The text of the message.
            
            responseCard (string) --At runtime, if the client is using the API, Amazon Lex includes the response card in the response. It substitutes all of the session attributes and slot values for placeholders in the response card.
            

    :type followUpPrompt: dict
    :param followUpPrompt: A user prompt for additional activity after an intent is fulfilled. For example, after the OrderPizza intent is fulfilled (your Lambda function placed an order with a pizzeria), you might prompt the user to find if they want to order a drink (assuming that you have defined an OrderDrink intent in your bot).
            Note
            The followUpPrompt and conclusionStatement are mutually exclusive. You can specify only one. For example, your bot may not solicit both the following:
            Follow up prompt - '$session.FirstName , your pizza order has been placed. Would you like to order a drink or a dessert?'
            Conclusion statement - '$session.FirstName , your pizza order has been placed.'
            prompt (dict) -- [REQUIRED]Obtains information from the user.
            messages (list) -- [REQUIRED]An array of objects, each of which provides a message string and its type. You can specify the message string in plain text or in Speech Synthesis Markup Language (SSML).
            (dict) --The message object that provides the message text and its type.
            contentType (string) -- [REQUIRED]The content type of the message string.
            content (string) -- [REQUIRED]The text of the message.
            
            maxAttempts (integer) -- [REQUIRED]The number of times to prompt the user for information.
            responseCard (string) --A response card. Amazon Lex uses this prompt at runtime, in the PostText API response. It substitutes session attributes and slot values for placeholders in the response card. For more information, see ex-resp-card .
            rejectionStatement (dict) -- [REQUIRED]If the user answers 'no' to the question defined in confirmationPrompt , Amazon Lex responds with this statement to acknowledge that the intent was canceled.
            messages (list) -- [REQUIRED]A collection of message objects.
            (dict) --The message object that provides the message text and its type.
            contentType (string) -- [REQUIRED]The content type of the message string.
            content (string) -- [REQUIRED]The text of the message.
            
            responseCard (string) --At runtime, if the client is using the API, Amazon Lex includes the response card in the response. It substitutes all of the session attributes and slot values for placeholders in the response card.
            
            

    :type conclusionStatement: dict
    :param conclusionStatement: The statement that you want Amazon Lex to convey to the user after the intent is successfully fulfilled by the Lambda function.
            This element is relevant only if you provide a Lambda function in the fulfillmentActivity . If you return the intent to the client application, you can't specify this element.
            Note
            The followUpPrompt and conclusionStatement are mutually exclusive. You can specify only one.
            messages (list) -- [REQUIRED]A collection of message objects.
            (dict) --The message object that provides the message text and its type.
            contentType (string) -- [REQUIRED]The content type of the message string.
            content (string) -- [REQUIRED]The text of the message.
            
            responseCard (string) --At runtime, if the client is using the API, Amazon Lex includes the response card in the response. It substitutes all of the session attributes and slot values for placeholders in the response card.
            

    :type dialogCodeHook: dict
    :param dialogCodeHook: Specifies a Lambda function to invoke for each user input. You can invoke this Lambda function to personalize user interaction.
            For example, suppose your bot determines that the user is John. Your Lambda function might retrieve John's information from a backend database and prepopulate some of the values. For example, if you find that John is gluten intolerant, you might set the corresponding intent slot, GlutenIntolerant , to true. You might find John's phone number and set the corresponding session attribute.
            uri (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the Lambda function.
            messageVersion (string) -- [REQUIRED]The version of the request-response that you want Amazon Lex to use to invoke your Lambda function. For more information, see using-lambda .
            

    :type fulfillmentActivity: dict
    :param fulfillmentActivity: Describes how the intent is fulfilled. For example, after a user provides all of the information for a pizza order, fulfillmentActivity defines how the bot places an order with a local pizza store.
            You might configure Amazon Lex to return all of the intent information to the client application, or direct it to invoke a Lambda function that can process the intent (for example, place an order with a pizzeria).
            type (string) -- [REQUIRED]How the intent should be fulfilled, either by running a Lambda function or by returning the slot data to the client application.
            codeHook (dict) --A description of the Lambda function that is run to fulfill the intent.
            uri (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the Lambda function.
            messageVersion (string) -- [REQUIRED]The version of the request-response that you want Amazon Lex to use to invoke your Lambda function. For more information, see using-lambda .
            
            

    :type parentIntentSignature: string
    :param parentIntentSignature: A unique identifier for the built-in intent to base this intent on. To find the signature for an intent, see Standard Built-in Intents in the Alexa Skills Kit .

    :type checksum: string
    :param checksum: Identifies a specific revision of the $LATEST version.
            When you create a new intent, leave the checksum field blank. If you specify a checksum you get a BadRequestException exception.
            When you want to update a intent, set the checksum field to the checksum of the most recent revision of the $LATEST version. If you don't specify the checksum field, or if the checksum does not match the $LATEST version, you get a PreconditionFailedException exception.
            

    :rtype: dict
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
                            'contentType': 'PlainText'|'SSML',
                            'content': 'string'
                        },
                    ],
                    'maxAttempts': 123,
                    'responseCard': 'string'
                },
                'priority': 123,
                'sampleUtterances': [
                    'string',
                ],
                'responseCard': 'string'
            },
        ],
        'sampleUtterances': [
            'string',
        ],
        'confirmationPrompt': {
            'messages': [
                {
                    'contentType': 'PlainText'|'SSML',
                    'content': 'string'
                },
            ],
            'maxAttempts': 123,
            'responseCard': 'string'
        },
        'rejectionStatement': {
            'messages': [
                {
                    'contentType': 'PlainText'|'SSML',
                    'content': 'string'
                },
            ],
            'responseCard': 'string'
        },
        'followUpPrompt': {
            'prompt': {
                'messages': [
                    {
                        'contentType': 'PlainText'|'SSML',
                        'content': 'string'
                    },
                ],
                'maxAttempts': 123,
                'responseCard': 'string'
            },
            'rejectionStatement': {
                'messages': [
                    {
                        'contentType': 'PlainText'|'SSML',
                        'content': 'string'
                    },
                ],
                'responseCard': 'string'
            }
        },
        'conclusionStatement': {
            'messages': [
                {
                    'contentType': 'PlainText'|'SSML',
                    'content': 'string'
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
    A confirmation prompt to ask the user to confirm an intent. For example, "Shall I order your pizza?"
    A conclusion statement to send to the user after the intent has been fulfilled. For example, "I placed your pizza order."
    A follow-up prompt that asks the user for additional activity. For example, asking "Do you want to order a drink with your pizza?"
    
    """
    pass

def put_slot_type(name=None, description=None, enumerationValues=None, checksum=None):
    """
    Creates a custom slot type or replaces an existing custom slot type.
    To create a custom slot type, specify a name for the slot type and a set of enumeration values, which are the values that a slot of this type can assume. For more information, see  how-it-works .
    If you specify the name of an existing slot type, the fields in the request replace the existing values in the $LATEST version of the slot type. Amazon Lex removes the fields that you don't provide in the request. If you don't specify required fields, Amazon Lex throws an exception.
    This operation requires permissions for the lex:PutSlotType action.
    See also: AWS API Documentation
    
    
    :example: response = client.put_slot_type(
        name='string',
        description='string',
        enumerationValues=[
            {
                'value': 'string'
            },
        ],
        checksum='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            The name of the slot type. The name is not case sensitive.
            The name can't match a built-in slot type name, or a built-in slot type name with 'AMAZON.' removed. For example, because there is a built-in slot type called AMAZON.DATE , you can't create a custom slot type called DATE .
            For a list of built-in slot types, see Slot Type Reference in the Alexa Skills Kit .
            

    :type description: string
    :param description: A description of the slot type.

    :type enumerationValues: list
    :param enumerationValues: A list of EnumerationValue objects that defines the values that the slot type can take.
            (dict) --Each slot type can have a set of values. Each enumeration value represents a value the slot type can take.
            For example, a pizza ordering bot could have a slot type that specifies the type of crust that the pizza should have. The slot type could include the values
            thick
            thin
            stuffed
            value (string) -- [REQUIRED]The value of the slot type.
            
            

    :type checksum: string
    :param checksum: Identifies a specific revision of the $LATEST version.
            When you create a new slot type, leave the checksum field blank. If you specify a checksum you get a BadRequestException exception.
            When you want to update a slot type, set the checksum field to the checksum of the most recent revision of the $LATEST version. If you don't specify the checksum field, or if the checksum does not match the $LATEST version, you get a PreconditionFailedException exception.
            

    :rtype: dict
    :return: {
        'name': 'string',
        'description': 'string',
        'enumerationValues': [
            {
                'value': 'string'
            },
        ],
        'lastUpdatedDate': datetime(2015, 1, 1),
        'createdDate': datetime(2015, 1, 1),
        'version': 'string',
        'checksum': 'string'
    }
    
    
    :returns: 
    thick
    thin
    stuffed
    
    """
    pass

