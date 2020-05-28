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

def create_detector_model(detectorModelName=None, detectorModelDefinition=None, detectorModelDescription=None, key=None, roleArn=None, tags=None, evaluationMethod=None):
    """
    Creates a detector model.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_detector_model(
        detectorModelName='string',
        detectorModelDefinition={
            'states': [
                {
                    'stateName': 'string',
                    'onInput': {
                        'events': [
                            {
                                'eventName': 'string',
                                'condition': 'string',
                                'actions': [
                                    {
                                        'setVariable': {
                                            'variableName': 'string',
                                            'value': 'string'
                                        },
                                        'sns': {
                                            'targetArn': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'iotTopicPublish': {
                                            'mqttTopic': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'setTimer': {
                                            'timerName': 'string',
                                            'seconds': 123,
                                            'durationExpression': 'string'
                                        },
                                        'clearTimer': {
                                            'timerName': 'string'
                                        },
                                        'resetTimer': {
                                            'timerName': 'string'
                                        },
                                        'lambda': {
                                            'functionArn': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'iotEvents': {
                                            'inputName': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'sqs': {
                                            'queueUrl': 'string',
                                            'useBase64': True|False,
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'firehose': {
                                            'deliveryStreamName': 'string',
                                            'separator': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'dynamoDB': {
                                            'hashKeyType': 'string',
                                            'hashKeyField': 'string',
                                            'hashKeyValue': 'string',
                                            'rangeKeyType': 'string',
                                            'rangeKeyField': 'string',
                                            'rangeKeyValue': 'string',
                                            'operation': 'string',
                                            'payloadField': 'string',
                                            'tableName': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'dynamoDBv2': {
                                            'tableName': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'iotSiteWise': {
                                            'entryId': 'string',
                                            'assetId': 'string',
                                            'propertyId': 'string',
                                            'propertyAlias': 'string',
                                            'propertyValue': {
                                                'value': {
                                                    'stringValue': 'string',
                                                    'integerValue': 'string',
                                                    'doubleValue': 'string',
                                                    'booleanValue': 'string'
                                                },
                                                'timestamp': {
                                                    'timeInSeconds': 'string',
                                                    'offsetInNanos': 'string'
                                                },
                                                'quality': 'string'
                                            }
                                        }
                                    },
                                ]
                            },
                        ],
                        'transitionEvents': [
                            {
                                'eventName': 'string',
                                'condition': 'string',
                                'actions': [
                                    {
                                        'setVariable': {
                                            'variableName': 'string',
                                            'value': 'string'
                                        },
                                        'sns': {
                                            'targetArn': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'iotTopicPublish': {
                                            'mqttTopic': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'setTimer': {
                                            'timerName': 'string',
                                            'seconds': 123,
                                            'durationExpression': 'string'
                                        },
                                        'clearTimer': {
                                            'timerName': 'string'
                                        },
                                        'resetTimer': {
                                            'timerName': 'string'
                                        },
                                        'lambda': {
                                            'functionArn': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'iotEvents': {
                                            'inputName': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'sqs': {
                                            'queueUrl': 'string',
                                            'useBase64': True|False,
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'firehose': {
                                            'deliveryStreamName': 'string',
                                            'separator': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'dynamoDB': {
                                            'hashKeyType': 'string',
                                            'hashKeyField': 'string',
                                            'hashKeyValue': 'string',
                                            'rangeKeyType': 'string',
                                            'rangeKeyField': 'string',
                                            'rangeKeyValue': 'string',
                                            'operation': 'string',
                                            'payloadField': 'string',
                                            'tableName': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'dynamoDBv2': {
                                            'tableName': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'iotSiteWise': {
                                            'entryId': 'string',
                                            'assetId': 'string',
                                            'propertyId': 'string',
                                            'propertyAlias': 'string',
                                            'propertyValue': {
                                                'value': {
                                                    'stringValue': 'string',
                                                    'integerValue': 'string',
                                                    'doubleValue': 'string',
                                                    'booleanValue': 'string'
                                                },
                                                'timestamp': {
                                                    'timeInSeconds': 'string',
                                                    'offsetInNanos': 'string'
                                                },
                                                'quality': 'string'
                                            }
                                        }
                                    },
                                ],
                                'nextState': 'string'
                            },
                        ]
                    },
                    'onEnter': {
                        'events': [
                            {
                                'eventName': 'string',
                                'condition': 'string',
                                'actions': [
                                    {
                                        'setVariable': {
                                            'variableName': 'string',
                                            'value': 'string'
                                        },
                                        'sns': {
                                            'targetArn': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'iotTopicPublish': {
                                            'mqttTopic': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'setTimer': {
                                            'timerName': 'string',
                                            'seconds': 123,
                                            'durationExpression': 'string'
                                        },
                                        'clearTimer': {
                                            'timerName': 'string'
                                        },
                                        'resetTimer': {
                                            'timerName': 'string'
                                        },
                                        'lambda': {
                                            'functionArn': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'iotEvents': {
                                            'inputName': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'sqs': {
                                            'queueUrl': 'string',
                                            'useBase64': True|False,
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'firehose': {
                                            'deliveryStreamName': 'string',
                                            'separator': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'dynamoDB': {
                                            'hashKeyType': 'string',
                                            'hashKeyField': 'string',
                                            'hashKeyValue': 'string',
                                            'rangeKeyType': 'string',
                                            'rangeKeyField': 'string',
                                            'rangeKeyValue': 'string',
                                            'operation': 'string',
                                            'payloadField': 'string',
                                            'tableName': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'dynamoDBv2': {
                                            'tableName': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'iotSiteWise': {
                                            'entryId': 'string',
                                            'assetId': 'string',
                                            'propertyId': 'string',
                                            'propertyAlias': 'string',
                                            'propertyValue': {
                                                'value': {
                                                    'stringValue': 'string',
                                                    'integerValue': 'string',
                                                    'doubleValue': 'string',
                                                    'booleanValue': 'string'
                                                },
                                                'timestamp': {
                                                    'timeInSeconds': 'string',
                                                    'offsetInNanos': 'string'
                                                },
                                                'quality': 'string'
                                            }
                                        }
                                    },
                                ]
                            },
                        ]
                    },
                    'onExit': {
                        'events': [
                            {
                                'eventName': 'string',
                                'condition': 'string',
                                'actions': [
                                    {
                                        'setVariable': {
                                            'variableName': 'string',
                                            'value': 'string'
                                        },
                                        'sns': {
                                            'targetArn': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'iotTopicPublish': {
                                            'mqttTopic': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'setTimer': {
                                            'timerName': 'string',
                                            'seconds': 123,
                                            'durationExpression': 'string'
                                        },
                                        'clearTimer': {
                                            'timerName': 'string'
                                        },
                                        'resetTimer': {
                                            'timerName': 'string'
                                        },
                                        'lambda': {
                                            'functionArn': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'iotEvents': {
                                            'inputName': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'sqs': {
                                            'queueUrl': 'string',
                                            'useBase64': True|False,
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'firehose': {
                                            'deliveryStreamName': 'string',
                                            'separator': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'dynamoDB': {
                                            'hashKeyType': 'string',
                                            'hashKeyField': 'string',
                                            'hashKeyValue': 'string',
                                            'rangeKeyType': 'string',
                                            'rangeKeyField': 'string',
                                            'rangeKeyValue': 'string',
                                            'operation': 'string',
                                            'payloadField': 'string',
                                            'tableName': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'dynamoDBv2': {
                                            'tableName': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'iotSiteWise': {
                                            'entryId': 'string',
                                            'assetId': 'string',
                                            'propertyId': 'string',
                                            'propertyAlias': 'string',
                                            'propertyValue': {
                                                'value': {
                                                    'stringValue': 'string',
                                                    'integerValue': 'string',
                                                    'doubleValue': 'string',
                                                    'booleanValue': 'string'
                                                },
                                                'timestamp': {
                                                    'timeInSeconds': 'string',
                                                    'offsetInNanos': 'string'
                                                },
                                                'quality': 'string'
                                            }
                                        }
                                    },
                                ]
                            },
                        ]
                    }
                },
            ],
            'initialStateName': 'string'
        },
        detectorModelDescription='string',
        key='string',
        roleArn='string',
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ],
        evaluationMethod='BATCH'|'SERIAL'
    )
    
    
    :type detectorModelName: string
    :param detectorModelName: [REQUIRED]\nThe name of the detector model.\n

    :type detectorModelDefinition: dict
    :param detectorModelDefinition: [REQUIRED]\nInformation that defines how the detectors operate.\n\nstates (list) -- [REQUIRED]Information about the states of the detector.\n\n(dict) --Information that defines a state of a detector.\n\nstateName (string) -- [REQUIRED]The name of the state.\n\nonInput (dict) --When an input is received and the condition is TRUE, perform the specified actions .\n\nevents (list) --Specifies the actions performed when the condition evaluates to TRUE.\n\n(dict) --Specifies the actions to be performed when the condition evaluates to TRUE.\n\neventName (string) -- [REQUIRED]The name of the event.\n\ncondition (string) --Optional. The Boolean expression that, when TRUE, causes the actions to be performed. If not present, the actions are performed (=TRUE). If the expression result is not a Boolean value, the actions are not performed (=FALSE).\n\nactions (list) --The actions to be performed.\n\n(dict) --An action to be performed when the condition is TRUE.\n\nsetVariable (dict) --Sets a variable to a specified value.\n\nvariableName (string) -- [REQUIRED]The name of the variable.\n\nvalue (string) -- [REQUIRED]The new value of the variable.\n\n\n\nsns (dict) --Sends an Amazon SNS message.\n\ntargetArn (string) -- [REQUIRED]The ARN of the Amazon SNS target where the message is sent.\n\npayload (dict) --You can configure the action payload when you send a message as an Amazon SNS push notification.\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\niotTopicPublish (dict) --Publishes an MQTT message with the given topic to the AWS IoT message broker.\n\nmqttTopic (string) -- [REQUIRED]The MQTT topic of the message. You can use a string expression that includes variables ($variable.<variable-name> ) and input values ($input.<input-name>.<path-to-datum> ) as the topic string.\n\npayload (dict) --You can configure the action payload when you publish a message to an AWS IoT Core topic.\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\nsetTimer (dict) --Information needed to set the timer.\n\ntimerName (string) -- [REQUIRED]The name of the timer.\n\nseconds (integer) --The number of seconds until the timer expires. The minimum value is 60 seconds to ensure accuracy. The maximum value is 31622400 seconds.\n\ndurationExpression (string) --The duration of the timer, in seconds. You can use a string expression that includes numbers, variables ($variable.<variable-name> ), and input values ($input.<input-name>.<path-to-datum> ) as the duration. The range of the duration is 1-31622400 seconds. To ensure accuracy, the minimum duration is 60 seconds. The evaluated result of the duration is rounded down to the nearest whole number.\n\n\n\nclearTimer (dict) --Information needed to clear the timer.\n\ntimerName (string) -- [REQUIRED]The name of the timer to clear.\n\n\n\nresetTimer (dict) --Information needed to reset the timer.\n\ntimerName (string) -- [REQUIRED]The name of the timer to reset.\n\n\n\nlambda (dict) --Calls a Lambda function, passing in information about the detector model instance and the event that triggered the action.\n\nfunctionArn (string) -- [REQUIRED]The ARN of the Lambda function that is executed.\n\npayload (dict) --You can configure the action payload when you send a message to a Lambda function.\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\niotEvents (dict) --Sends AWS IoT Events input, which passes information about the detector model instance and the event that triggered the action.\n\ninputName (string) -- [REQUIRED]The name of the AWS IoT Events input where the data is sent.\n\npayload (dict) --You can configure the action payload when you send a message to an AWS IoT Events input.\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\nsqs (dict) --Sends information about the detector model instance and the event that triggered the action to an Amazon SQS queue.\n\nqueueUrl (string) -- [REQUIRED]The URL of the SQS queue where the data is written.\n\nuseBase64 (boolean) --Set this to TRUE if you want the data to be base-64 encoded before it is written to the queue. Otherwise, set this to FALSE.\n\npayload (dict) --You can configure the action payload when you send a message to an Amazon SQS queue.\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\nfirehose (dict) --Sends information about the detector model instance and the event that triggered the action to an Amazon Kinesis Data Firehose delivery stream.\n\ndeliveryStreamName (string) -- [REQUIRED]The name of the Kinesis Data Firehose delivery stream where the data is written.\n\nseparator (string) --A character separator that is used to separate records written to the Kinesis Data Firehose delivery stream. Valid values are: \'n\' (newline), \'t\' (tab), \'rn\' (Windows newline), \',\' (comma).\n\npayload (dict) --You can configure the action payload when you send a message to an Amazon Kinesis Data Firehose delivery stream.\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\ndynamoDB (dict) --Writes to the DynamoDB table that you created. The default action payload contains all attribute-value pairs that have the information about the detector model instance and the event that triggered the action. You can also customize the payload . One column of the DynamoDB table receives all attribute-value pairs in the payload that you specify. For more information, see Actions in AWS IoT Events Developer Guide .\n\nhashKeyType (string) --The data type for the hash key (also called the partition key). You can specify the following values:\n\nSTRING - The hash key is a string.\nNUMBER - The hash key is a number.\n\nIf you don\'t specify hashKeyType , the default value is STRING .\n\nhashKeyField (string) -- [REQUIRED]The name of the hash key (also called the partition key).\n\nhashKeyValue (string) -- [REQUIRED]The value of the hash key (also called the partition key).\n\nrangeKeyType (string) --The data type for the range key (also called the sort key), You can specify the following values:\n\nSTRING - The range key is a string.\nNUMBER - The range key is number.\n\nIf you don\'t specify rangeKeyField , the default value is STRING .\n\nrangeKeyField (string) --The name of the range key (also called the sort key).\n\nrangeKeyValue (string) --The value of the range key (also called the sort key).\n\noperation (string) --The type of operation to perform. You can specify the following values:\n\nINSERT - Insert data as a new item into the DynamoDB table. This item uses the specified hash key as a partition key. If you specified a range key, the item uses the range key as a sort key.\nUPDATE - Update an existing item of the DynamoDB table with new data. This item\'s partition key must match the specified hash key. If you specified a range key, the range key must match the item\'s sort key.\nDELETE - Delete an existing item of the DynamoDB table. This item\'s partition key must match the specified hash key. If you specified a range key, the range key must match the item\'s sort key.\n\nIf you don\'t specify this parameter, AWS IoT Events triggers the INSERT operation.\n\npayloadField (string) --The name of the DynamoDB column that receives the action payload.\nIf you don\'t specify this parameter, the name of the DynamoDB column is payload .\n\ntableName (string) -- [REQUIRED]The name of the DynamoDB table.\n\npayload (dict) --Information needed to configure the payload.\nBy default, AWS IoT Events generates a standard payload in JSON for any action. This action payload contains all attribute-value pairs that have the information about the detector model instance and the event triggered the action. To configure the action payload, you can use contentExpression .\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\ndynamoDBv2 (dict) --Writes to the DynamoDB table that you created. The default action payload contains all attribute-value pairs that have the information about the detector model instance and the event that triggered the action. You can also customize the payload . A separate column of the DynamoDB table receives one attribute-value pair in the payload that you specify. For more information, see Actions in AWS IoT Events Developer Guide .\n\ntableName (string) -- [REQUIRED]The name of the DynamoDB table.\n\npayload (dict) --Information needed to configure the payload.\nBy default, AWS IoT Events generates a standard payload in JSON for any action. This action payload contains all attribute-value pairs that have the information about the detector model instance and the event triggered the action. To configure the action payload, you can use contentExpression .\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\niotSiteWise (dict) --Sends information about the detector model instance and the event that triggered the action to an asset property in AWS IoT SiteWise .\n\nentryId (string) --A unique identifier for this entry. You can use the entry ID to track which data entry causes an error in case of failure. The default is a new unique identifier. You can also specify an expression.\n\nassetId (string) --The ID of the asset that has the specified property. You can specify an expression.\n\npropertyId (string) --The ID of the asset property. You can specify an expression.\n\npropertyAlias (string) --The alias of the asset property. You can also specify an expression.\n\npropertyValue (dict) -- [REQUIRED]The value to send to the asset property. This value contains timestamp, quality, and value (TQV) information.\n\nvalue (dict) -- [REQUIRED]The value to send to an asset property.\n\nstringValue (string) --The asset property value is a string. You can also specify an expression. If you use an expression, the evaluated result should be a string.\n\nintegerValue (string) --The asset property value is an integer. You can also specify an expression. If you use an expression, the evaluated result should be an integer.\n\ndoubleValue (string) --The asset property value is a double. You can also specify an expression. If you use an expression, the evaluated result should be a double.\n\nbooleanValue (string) --The asset property value is a Boolean value that must be TRUE or FALSE . You can also specify an expression. If you use an expression, the evaluated result should be a Boolean value.\n\n\n\ntimestamp (dict) --The timestamp associated with the asset property value. The default is the current event time.\n\ntimeInSeconds (string) -- [REQUIRED]The timestamp, in seconds, in the Unix epoch format. The valid range is between 1-31556889864403199. You can also specify an expression.\n\noffsetInNanos (string) --The nanosecond offset converted from timeInSeconds . The valid range is between 0-999999999. You can also specify an expression.\n\n\n\nquality (string) --The quality of the asset property value. The value must be GOOD , BAD , or UNCERTAIN . You can also specify an expression.\n\n\n\n\n\n\n\n\n\n\n\n\n\ntransitionEvents (list) --Specifies the actions performed, and the next state entered, when a condition evaluates to TRUE.\n\n(dict) --Specifies the actions performed and the next state entered when a condition evaluates to TRUE.\n\neventName (string) -- [REQUIRED]The name of the transition event.\n\ncondition (string) -- [REQUIRED]Required. A Boolean expression that when TRUE causes the actions to be performed and the nextState to be entered.\n\nactions (list) --The actions to be performed.\n\n(dict) --An action to be performed when the condition is TRUE.\n\nsetVariable (dict) --Sets a variable to a specified value.\n\nvariableName (string) -- [REQUIRED]The name of the variable.\n\nvalue (string) -- [REQUIRED]The new value of the variable.\n\n\n\nsns (dict) --Sends an Amazon SNS message.\n\ntargetArn (string) -- [REQUIRED]The ARN of the Amazon SNS target where the message is sent.\n\npayload (dict) --You can configure the action payload when you send a message as an Amazon SNS push notification.\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\niotTopicPublish (dict) --Publishes an MQTT message with the given topic to the AWS IoT message broker.\n\nmqttTopic (string) -- [REQUIRED]The MQTT topic of the message. You can use a string expression that includes variables ($variable.<variable-name> ) and input values ($input.<input-name>.<path-to-datum> ) as the topic string.\n\npayload (dict) --You can configure the action payload when you publish a message to an AWS IoT Core topic.\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\nsetTimer (dict) --Information needed to set the timer.\n\ntimerName (string) -- [REQUIRED]The name of the timer.\n\nseconds (integer) --The number of seconds until the timer expires. The minimum value is 60 seconds to ensure accuracy. The maximum value is 31622400 seconds.\n\ndurationExpression (string) --The duration of the timer, in seconds. You can use a string expression that includes numbers, variables ($variable.<variable-name> ), and input values ($input.<input-name>.<path-to-datum> ) as the duration. The range of the duration is 1-31622400 seconds. To ensure accuracy, the minimum duration is 60 seconds. The evaluated result of the duration is rounded down to the nearest whole number.\n\n\n\nclearTimer (dict) --Information needed to clear the timer.\n\ntimerName (string) -- [REQUIRED]The name of the timer to clear.\n\n\n\nresetTimer (dict) --Information needed to reset the timer.\n\ntimerName (string) -- [REQUIRED]The name of the timer to reset.\n\n\n\nlambda (dict) --Calls a Lambda function, passing in information about the detector model instance and the event that triggered the action.\n\nfunctionArn (string) -- [REQUIRED]The ARN of the Lambda function that is executed.\n\npayload (dict) --You can configure the action payload when you send a message to a Lambda function.\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\niotEvents (dict) --Sends AWS IoT Events input, which passes information about the detector model instance and the event that triggered the action.\n\ninputName (string) -- [REQUIRED]The name of the AWS IoT Events input where the data is sent.\n\npayload (dict) --You can configure the action payload when you send a message to an AWS IoT Events input.\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\nsqs (dict) --Sends information about the detector model instance and the event that triggered the action to an Amazon SQS queue.\n\nqueueUrl (string) -- [REQUIRED]The URL of the SQS queue where the data is written.\n\nuseBase64 (boolean) --Set this to TRUE if you want the data to be base-64 encoded before it is written to the queue. Otherwise, set this to FALSE.\n\npayload (dict) --You can configure the action payload when you send a message to an Amazon SQS queue.\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\nfirehose (dict) --Sends information about the detector model instance and the event that triggered the action to an Amazon Kinesis Data Firehose delivery stream.\n\ndeliveryStreamName (string) -- [REQUIRED]The name of the Kinesis Data Firehose delivery stream where the data is written.\n\nseparator (string) --A character separator that is used to separate records written to the Kinesis Data Firehose delivery stream. Valid values are: \'n\' (newline), \'t\' (tab), \'rn\' (Windows newline), \',\' (comma).\n\npayload (dict) --You can configure the action payload when you send a message to an Amazon Kinesis Data Firehose delivery stream.\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\ndynamoDB (dict) --Writes to the DynamoDB table that you created. The default action payload contains all attribute-value pairs that have the information about the detector model instance and the event that triggered the action. You can also customize the payload . One column of the DynamoDB table receives all attribute-value pairs in the payload that you specify. For more information, see Actions in AWS IoT Events Developer Guide .\n\nhashKeyType (string) --The data type for the hash key (also called the partition key). You can specify the following values:\n\nSTRING - The hash key is a string.\nNUMBER - The hash key is a number.\n\nIf you don\'t specify hashKeyType , the default value is STRING .\n\nhashKeyField (string) -- [REQUIRED]The name of the hash key (also called the partition key).\n\nhashKeyValue (string) -- [REQUIRED]The value of the hash key (also called the partition key).\n\nrangeKeyType (string) --The data type for the range key (also called the sort key), You can specify the following values:\n\nSTRING - The range key is a string.\nNUMBER - The range key is number.\n\nIf you don\'t specify rangeKeyField , the default value is STRING .\n\nrangeKeyField (string) --The name of the range key (also called the sort key).\n\nrangeKeyValue (string) --The value of the range key (also called the sort key).\n\noperation (string) --The type of operation to perform. You can specify the following values:\n\nINSERT - Insert data as a new item into the DynamoDB table. This item uses the specified hash key as a partition key. If you specified a range key, the item uses the range key as a sort key.\nUPDATE - Update an existing item of the DynamoDB table with new data. This item\'s partition key must match the specified hash key. If you specified a range key, the range key must match the item\'s sort key.\nDELETE - Delete an existing item of the DynamoDB table. This item\'s partition key must match the specified hash key. If you specified a range key, the range key must match the item\'s sort key.\n\nIf you don\'t specify this parameter, AWS IoT Events triggers the INSERT operation.\n\npayloadField (string) --The name of the DynamoDB column that receives the action payload.\nIf you don\'t specify this parameter, the name of the DynamoDB column is payload .\n\ntableName (string) -- [REQUIRED]The name of the DynamoDB table.\n\npayload (dict) --Information needed to configure the payload.\nBy default, AWS IoT Events generates a standard payload in JSON for any action. This action payload contains all attribute-value pairs that have the information about the detector model instance and the event triggered the action. To configure the action payload, you can use contentExpression .\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\ndynamoDBv2 (dict) --Writes to the DynamoDB table that you created. The default action payload contains all attribute-value pairs that have the information about the detector model instance and the event that triggered the action. You can also customize the payload . A separate column of the DynamoDB table receives one attribute-value pair in the payload that you specify. For more information, see Actions in AWS IoT Events Developer Guide .\n\ntableName (string) -- [REQUIRED]The name of the DynamoDB table.\n\npayload (dict) --Information needed to configure the payload.\nBy default, AWS IoT Events generates a standard payload in JSON for any action. This action payload contains all attribute-value pairs that have the information about the detector model instance and the event triggered the action. To configure the action payload, you can use contentExpression .\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\niotSiteWise (dict) --Sends information about the detector model instance and the event that triggered the action to an asset property in AWS IoT SiteWise .\n\nentryId (string) --A unique identifier for this entry. You can use the entry ID to track which data entry causes an error in case of failure. The default is a new unique identifier. You can also specify an expression.\n\nassetId (string) --The ID of the asset that has the specified property. You can specify an expression.\n\npropertyId (string) --The ID of the asset property. You can specify an expression.\n\npropertyAlias (string) --The alias of the asset property. You can also specify an expression.\n\npropertyValue (dict) -- [REQUIRED]The value to send to the asset property. This value contains timestamp, quality, and value (TQV) information.\n\nvalue (dict) -- [REQUIRED]The value to send to an asset property.\n\nstringValue (string) --The asset property value is a string. You can also specify an expression. If you use an expression, the evaluated result should be a string.\n\nintegerValue (string) --The asset property value is an integer. You can also specify an expression. If you use an expression, the evaluated result should be an integer.\n\ndoubleValue (string) --The asset property value is a double. You can also specify an expression. If you use an expression, the evaluated result should be a double.\n\nbooleanValue (string) --The asset property value is a Boolean value that must be TRUE or FALSE . You can also specify an expression. If you use an expression, the evaluated result should be a Boolean value.\n\n\n\ntimestamp (dict) --The timestamp associated with the asset property value. The default is the current event time.\n\ntimeInSeconds (string) -- [REQUIRED]The timestamp, in seconds, in the Unix epoch format. The valid range is between 1-31556889864403199. You can also specify an expression.\n\noffsetInNanos (string) --The nanosecond offset converted from timeInSeconds . The valid range is between 0-999999999. You can also specify an expression.\n\n\n\nquality (string) --The quality of the asset property value. The value must be GOOD , BAD , or UNCERTAIN . You can also specify an expression.\n\n\n\n\n\n\n\n\n\nnextState (string) -- [REQUIRED]The next state to enter.\n\n\n\n\n\n\n\nonEnter (dict) --When entering this state, perform these actions if the condition is TRUE.\n\nevents (list) --Specifies the actions that are performed when the state is entered and the condition is TRUE .\n\n(dict) --Specifies the actions to be performed when the condition evaluates to TRUE.\n\neventName (string) -- [REQUIRED]The name of the event.\n\ncondition (string) --Optional. The Boolean expression that, when TRUE, causes the actions to be performed. If not present, the actions are performed (=TRUE). If the expression result is not a Boolean value, the actions are not performed (=FALSE).\n\nactions (list) --The actions to be performed.\n\n(dict) --An action to be performed when the condition is TRUE.\n\nsetVariable (dict) --Sets a variable to a specified value.\n\nvariableName (string) -- [REQUIRED]The name of the variable.\n\nvalue (string) -- [REQUIRED]The new value of the variable.\n\n\n\nsns (dict) --Sends an Amazon SNS message.\n\ntargetArn (string) -- [REQUIRED]The ARN of the Amazon SNS target where the message is sent.\n\npayload (dict) --You can configure the action payload when you send a message as an Amazon SNS push notification.\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\niotTopicPublish (dict) --Publishes an MQTT message with the given topic to the AWS IoT message broker.\n\nmqttTopic (string) -- [REQUIRED]The MQTT topic of the message. You can use a string expression that includes variables ($variable.<variable-name> ) and input values ($input.<input-name>.<path-to-datum> ) as the topic string.\n\npayload (dict) --You can configure the action payload when you publish a message to an AWS IoT Core topic.\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\nsetTimer (dict) --Information needed to set the timer.\n\ntimerName (string) -- [REQUIRED]The name of the timer.\n\nseconds (integer) --The number of seconds until the timer expires. The minimum value is 60 seconds to ensure accuracy. The maximum value is 31622400 seconds.\n\ndurationExpression (string) --The duration of the timer, in seconds. You can use a string expression that includes numbers, variables ($variable.<variable-name> ), and input values ($input.<input-name>.<path-to-datum> ) as the duration. The range of the duration is 1-31622400 seconds. To ensure accuracy, the minimum duration is 60 seconds. The evaluated result of the duration is rounded down to the nearest whole number.\n\n\n\nclearTimer (dict) --Information needed to clear the timer.\n\ntimerName (string) -- [REQUIRED]The name of the timer to clear.\n\n\n\nresetTimer (dict) --Information needed to reset the timer.\n\ntimerName (string) -- [REQUIRED]The name of the timer to reset.\n\n\n\nlambda (dict) --Calls a Lambda function, passing in information about the detector model instance and the event that triggered the action.\n\nfunctionArn (string) -- [REQUIRED]The ARN of the Lambda function that is executed.\n\npayload (dict) --You can configure the action payload when you send a message to a Lambda function.\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\niotEvents (dict) --Sends AWS IoT Events input, which passes information about the detector model instance and the event that triggered the action.\n\ninputName (string) -- [REQUIRED]The name of the AWS IoT Events input where the data is sent.\n\npayload (dict) --You can configure the action payload when you send a message to an AWS IoT Events input.\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\nsqs (dict) --Sends information about the detector model instance and the event that triggered the action to an Amazon SQS queue.\n\nqueueUrl (string) -- [REQUIRED]The URL of the SQS queue where the data is written.\n\nuseBase64 (boolean) --Set this to TRUE if you want the data to be base-64 encoded before it is written to the queue. Otherwise, set this to FALSE.\n\npayload (dict) --You can configure the action payload when you send a message to an Amazon SQS queue.\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\nfirehose (dict) --Sends information about the detector model instance and the event that triggered the action to an Amazon Kinesis Data Firehose delivery stream.\n\ndeliveryStreamName (string) -- [REQUIRED]The name of the Kinesis Data Firehose delivery stream where the data is written.\n\nseparator (string) --A character separator that is used to separate records written to the Kinesis Data Firehose delivery stream. Valid values are: \'n\' (newline), \'t\' (tab), \'rn\' (Windows newline), \',\' (comma).\n\npayload (dict) --You can configure the action payload when you send a message to an Amazon Kinesis Data Firehose delivery stream.\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\ndynamoDB (dict) --Writes to the DynamoDB table that you created. The default action payload contains all attribute-value pairs that have the information about the detector model instance and the event that triggered the action. You can also customize the payload . One column of the DynamoDB table receives all attribute-value pairs in the payload that you specify. For more information, see Actions in AWS IoT Events Developer Guide .\n\nhashKeyType (string) --The data type for the hash key (also called the partition key). You can specify the following values:\n\nSTRING - The hash key is a string.\nNUMBER - The hash key is a number.\n\nIf you don\'t specify hashKeyType , the default value is STRING .\n\nhashKeyField (string) -- [REQUIRED]The name of the hash key (also called the partition key).\n\nhashKeyValue (string) -- [REQUIRED]The value of the hash key (also called the partition key).\n\nrangeKeyType (string) --The data type for the range key (also called the sort key), You can specify the following values:\n\nSTRING - The range key is a string.\nNUMBER - The range key is number.\n\nIf you don\'t specify rangeKeyField , the default value is STRING .\n\nrangeKeyField (string) --The name of the range key (also called the sort key).\n\nrangeKeyValue (string) --The value of the range key (also called the sort key).\n\noperation (string) --The type of operation to perform. You can specify the following values:\n\nINSERT - Insert data as a new item into the DynamoDB table. This item uses the specified hash key as a partition key. If you specified a range key, the item uses the range key as a sort key.\nUPDATE - Update an existing item of the DynamoDB table with new data. This item\'s partition key must match the specified hash key. If you specified a range key, the range key must match the item\'s sort key.\nDELETE - Delete an existing item of the DynamoDB table. This item\'s partition key must match the specified hash key. If you specified a range key, the range key must match the item\'s sort key.\n\nIf you don\'t specify this parameter, AWS IoT Events triggers the INSERT operation.\n\npayloadField (string) --The name of the DynamoDB column that receives the action payload.\nIf you don\'t specify this parameter, the name of the DynamoDB column is payload .\n\ntableName (string) -- [REQUIRED]The name of the DynamoDB table.\n\npayload (dict) --Information needed to configure the payload.\nBy default, AWS IoT Events generates a standard payload in JSON for any action. This action payload contains all attribute-value pairs that have the information about the detector model instance and the event triggered the action. To configure the action payload, you can use contentExpression .\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\ndynamoDBv2 (dict) --Writes to the DynamoDB table that you created. The default action payload contains all attribute-value pairs that have the information about the detector model instance and the event that triggered the action. You can also customize the payload . A separate column of the DynamoDB table receives one attribute-value pair in the payload that you specify. For more information, see Actions in AWS IoT Events Developer Guide .\n\ntableName (string) -- [REQUIRED]The name of the DynamoDB table.\n\npayload (dict) --Information needed to configure the payload.\nBy default, AWS IoT Events generates a standard payload in JSON for any action. This action payload contains all attribute-value pairs that have the information about the detector model instance and the event triggered the action. To configure the action payload, you can use contentExpression .\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\niotSiteWise (dict) --Sends information about the detector model instance and the event that triggered the action to an asset property in AWS IoT SiteWise .\n\nentryId (string) --A unique identifier for this entry. You can use the entry ID to track which data entry causes an error in case of failure. The default is a new unique identifier. You can also specify an expression.\n\nassetId (string) --The ID of the asset that has the specified property. You can specify an expression.\n\npropertyId (string) --The ID of the asset property. You can specify an expression.\n\npropertyAlias (string) --The alias of the asset property. You can also specify an expression.\n\npropertyValue (dict) -- [REQUIRED]The value to send to the asset property. This value contains timestamp, quality, and value (TQV) information.\n\nvalue (dict) -- [REQUIRED]The value to send to an asset property.\n\nstringValue (string) --The asset property value is a string. You can also specify an expression. If you use an expression, the evaluated result should be a string.\n\nintegerValue (string) --The asset property value is an integer. You can also specify an expression. If you use an expression, the evaluated result should be an integer.\n\ndoubleValue (string) --The asset property value is a double. You can also specify an expression. If you use an expression, the evaluated result should be a double.\n\nbooleanValue (string) --The asset property value is a Boolean value that must be TRUE or FALSE . You can also specify an expression. If you use an expression, the evaluated result should be a Boolean value.\n\n\n\ntimestamp (dict) --The timestamp associated with the asset property value. The default is the current event time.\n\ntimeInSeconds (string) -- [REQUIRED]The timestamp, in seconds, in the Unix epoch format. The valid range is between 1-31556889864403199. You can also specify an expression.\n\noffsetInNanos (string) --The nanosecond offset converted from timeInSeconds . The valid range is between 0-999999999. You can also specify an expression.\n\n\n\nquality (string) --The quality of the asset property value. The value must be GOOD , BAD , or UNCERTAIN . You can also specify an expression.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nonExit (dict) --When exiting this state, perform these actions if the specified condition is TRUE .\n\nevents (list) --Specifies the actions that are performed when the state is exited and the condition is TRUE .\n\n(dict) --Specifies the actions to be performed when the condition evaluates to TRUE.\n\neventName (string) -- [REQUIRED]The name of the event.\n\ncondition (string) --Optional. The Boolean expression that, when TRUE, causes the actions to be performed. If not present, the actions are performed (=TRUE). If the expression result is not a Boolean value, the actions are not performed (=FALSE).\n\nactions (list) --The actions to be performed.\n\n(dict) --An action to be performed when the condition is TRUE.\n\nsetVariable (dict) --Sets a variable to a specified value.\n\nvariableName (string) -- [REQUIRED]The name of the variable.\n\nvalue (string) -- [REQUIRED]The new value of the variable.\n\n\n\nsns (dict) --Sends an Amazon SNS message.\n\ntargetArn (string) -- [REQUIRED]The ARN of the Amazon SNS target where the message is sent.\n\npayload (dict) --You can configure the action payload when you send a message as an Amazon SNS push notification.\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\niotTopicPublish (dict) --Publishes an MQTT message with the given topic to the AWS IoT message broker.\n\nmqttTopic (string) -- [REQUIRED]The MQTT topic of the message. You can use a string expression that includes variables ($variable.<variable-name> ) and input values ($input.<input-name>.<path-to-datum> ) as the topic string.\n\npayload (dict) --You can configure the action payload when you publish a message to an AWS IoT Core topic.\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\nsetTimer (dict) --Information needed to set the timer.\n\ntimerName (string) -- [REQUIRED]The name of the timer.\n\nseconds (integer) --The number of seconds until the timer expires. The minimum value is 60 seconds to ensure accuracy. The maximum value is 31622400 seconds.\n\ndurationExpression (string) --The duration of the timer, in seconds. You can use a string expression that includes numbers, variables ($variable.<variable-name> ), and input values ($input.<input-name>.<path-to-datum> ) as the duration. The range of the duration is 1-31622400 seconds. To ensure accuracy, the minimum duration is 60 seconds. The evaluated result of the duration is rounded down to the nearest whole number.\n\n\n\nclearTimer (dict) --Information needed to clear the timer.\n\ntimerName (string) -- [REQUIRED]The name of the timer to clear.\n\n\n\nresetTimer (dict) --Information needed to reset the timer.\n\ntimerName (string) -- [REQUIRED]The name of the timer to reset.\n\n\n\nlambda (dict) --Calls a Lambda function, passing in information about the detector model instance and the event that triggered the action.\n\nfunctionArn (string) -- [REQUIRED]The ARN of the Lambda function that is executed.\n\npayload (dict) --You can configure the action payload when you send a message to a Lambda function.\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\niotEvents (dict) --Sends AWS IoT Events input, which passes information about the detector model instance and the event that triggered the action.\n\ninputName (string) -- [REQUIRED]The name of the AWS IoT Events input where the data is sent.\n\npayload (dict) --You can configure the action payload when you send a message to an AWS IoT Events input.\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\nsqs (dict) --Sends information about the detector model instance and the event that triggered the action to an Amazon SQS queue.\n\nqueueUrl (string) -- [REQUIRED]The URL of the SQS queue where the data is written.\n\nuseBase64 (boolean) --Set this to TRUE if you want the data to be base-64 encoded before it is written to the queue. Otherwise, set this to FALSE.\n\npayload (dict) --You can configure the action payload when you send a message to an Amazon SQS queue.\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\nfirehose (dict) --Sends information about the detector model instance and the event that triggered the action to an Amazon Kinesis Data Firehose delivery stream.\n\ndeliveryStreamName (string) -- [REQUIRED]The name of the Kinesis Data Firehose delivery stream where the data is written.\n\nseparator (string) --A character separator that is used to separate records written to the Kinesis Data Firehose delivery stream. Valid values are: \'n\' (newline), \'t\' (tab), \'rn\' (Windows newline), \',\' (comma).\n\npayload (dict) --You can configure the action payload when you send a message to an Amazon Kinesis Data Firehose delivery stream.\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\ndynamoDB (dict) --Writes to the DynamoDB table that you created. The default action payload contains all attribute-value pairs that have the information about the detector model instance and the event that triggered the action. You can also customize the payload . One column of the DynamoDB table receives all attribute-value pairs in the payload that you specify. For more information, see Actions in AWS IoT Events Developer Guide .\n\nhashKeyType (string) --The data type for the hash key (also called the partition key). You can specify the following values:\n\nSTRING - The hash key is a string.\nNUMBER - The hash key is a number.\n\nIf you don\'t specify hashKeyType , the default value is STRING .\n\nhashKeyField (string) -- [REQUIRED]The name of the hash key (also called the partition key).\n\nhashKeyValue (string) -- [REQUIRED]The value of the hash key (also called the partition key).\n\nrangeKeyType (string) --The data type for the range key (also called the sort key), You can specify the following values:\n\nSTRING - The range key is a string.\nNUMBER - The range key is number.\n\nIf you don\'t specify rangeKeyField , the default value is STRING .\n\nrangeKeyField (string) --The name of the range key (also called the sort key).\n\nrangeKeyValue (string) --The value of the range key (also called the sort key).\n\noperation (string) --The type of operation to perform. You can specify the following values:\n\nINSERT - Insert data as a new item into the DynamoDB table. This item uses the specified hash key as a partition key. If you specified a range key, the item uses the range key as a sort key.\nUPDATE - Update an existing item of the DynamoDB table with new data. This item\'s partition key must match the specified hash key. If you specified a range key, the range key must match the item\'s sort key.\nDELETE - Delete an existing item of the DynamoDB table. This item\'s partition key must match the specified hash key. If you specified a range key, the range key must match the item\'s sort key.\n\nIf you don\'t specify this parameter, AWS IoT Events triggers the INSERT operation.\n\npayloadField (string) --The name of the DynamoDB column that receives the action payload.\nIf you don\'t specify this parameter, the name of the DynamoDB column is payload .\n\ntableName (string) -- [REQUIRED]The name of the DynamoDB table.\n\npayload (dict) --Information needed to configure the payload.\nBy default, AWS IoT Events generates a standard payload in JSON for any action. This action payload contains all attribute-value pairs that have the information about the detector model instance and the event triggered the action. To configure the action payload, you can use contentExpression .\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\ndynamoDBv2 (dict) --Writes to the DynamoDB table that you created. The default action payload contains all attribute-value pairs that have the information about the detector model instance and the event that triggered the action. You can also customize the payload . A separate column of the DynamoDB table receives one attribute-value pair in the payload that you specify. For more information, see Actions in AWS IoT Events Developer Guide .\n\ntableName (string) -- [REQUIRED]The name of the DynamoDB table.\n\npayload (dict) --Information needed to configure the payload.\nBy default, AWS IoT Events generates a standard payload in JSON for any action. This action payload contains all attribute-value pairs that have the information about the detector model instance and the event triggered the action. To configure the action payload, you can use contentExpression .\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\niotSiteWise (dict) --Sends information about the detector model instance and the event that triggered the action to an asset property in AWS IoT SiteWise .\n\nentryId (string) --A unique identifier for this entry. You can use the entry ID to track which data entry causes an error in case of failure. The default is a new unique identifier. You can also specify an expression.\n\nassetId (string) --The ID of the asset that has the specified property. You can specify an expression.\n\npropertyId (string) --The ID of the asset property. You can specify an expression.\n\npropertyAlias (string) --The alias of the asset property. You can also specify an expression.\n\npropertyValue (dict) -- [REQUIRED]The value to send to the asset property. This value contains timestamp, quality, and value (TQV) information.\n\nvalue (dict) -- [REQUIRED]The value to send to an asset property.\n\nstringValue (string) --The asset property value is a string. You can also specify an expression. If you use an expression, the evaluated result should be a string.\n\nintegerValue (string) --The asset property value is an integer. You can also specify an expression. If you use an expression, the evaluated result should be an integer.\n\ndoubleValue (string) --The asset property value is a double. You can also specify an expression. If you use an expression, the evaluated result should be a double.\n\nbooleanValue (string) --The asset property value is a Boolean value that must be TRUE or FALSE . You can also specify an expression. If you use an expression, the evaluated result should be a Boolean value.\n\n\n\ntimestamp (dict) --The timestamp associated with the asset property value. The default is the current event time.\n\ntimeInSeconds (string) -- [REQUIRED]The timestamp, in seconds, in the Unix epoch format. The valid range is between 1-31556889864403199. You can also specify an expression.\n\noffsetInNanos (string) --The nanosecond offset converted from timeInSeconds . The valid range is between 0-999999999. You can also specify an expression.\n\n\n\nquality (string) --The quality of the asset property value. The value must be GOOD , BAD , or UNCERTAIN . You can also specify an expression.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\ninitialStateName (string) -- [REQUIRED]The state that is entered at the creation of each detector (instance).\n\n\n

    :type detectorModelDescription: string
    :param detectorModelDescription: A brief description of the detector model.

    :type key: string
    :param key: The input attribute key used to identify a device or system to create a detector (an instance of the detector model) and then to route each input received to the appropriate detector (instance). This parameter uses a JSON-path expression in the message payload of each input to specify the attribute-value pair that is used to identify the device associated with the input.

    :type roleArn: string
    :param roleArn: [REQUIRED]\nThe ARN of the role that grants permission to AWS IoT Events to perform its operations.\n

    :type tags: list
    :param tags: Metadata that can be used to manage the detector model.\n\n(dict) --Metadata that can be used to manage the resource.\n\nkey (string) -- [REQUIRED]The tag\'s key.\n\nvalue (string) -- [REQUIRED]The tag\'s value.\n\n\n\n\n

    :type evaluationMethod: string
    :param evaluationMethod: Information about the order in which events are evaluated and how actions are executed.

    :rtype: dict

ReturnsResponse Syntax
{
    'detectorModelConfiguration': {
        'detectorModelName': 'string',
        'detectorModelVersion': 'string',
        'detectorModelDescription': 'string',
        'detectorModelArn': 'string',
        'roleArn': 'string',
        'creationTime': datetime(2015, 1, 1),
        'lastUpdateTime': datetime(2015, 1, 1),
        'status': 'ACTIVE'|'ACTIVATING'|'INACTIVE'|'DEPRECATED'|'DRAFT'|'PAUSED'|'FAILED',
        'key': 'string',
        'evaluationMethod': 'BATCH'|'SERIAL'
    }
}


Response Structure

(dict) --

detectorModelConfiguration (dict) --
Information about how the detector model is configured.

detectorModelName (string) --
The name of the detector model.

detectorModelVersion (string) --
The version of the detector model.

detectorModelDescription (string) --
A brief description of the detector model.

detectorModelArn (string) --
The ARN of the detector model.

roleArn (string) --
The ARN of the role that grants permission to AWS IoT Events to perform its operations.

creationTime (datetime) --
The time the detector model was created.

lastUpdateTime (datetime) --
The time the detector model was last updated.

status (string) --
The status of the detector model.

key (string) --
The value used to identify a detector instance. When a device or system sends input, a new detector instance with a unique key value is created. AWS IoT Events can continue to route input to its corresponding detector instance based on this identifying information.
This parameter uses a JSON-path expression to select the attribute-value pair in the message payload that is used for identification. To route the message to the correct detector instance, the device must send a message payload that contains the same attribute-value.

evaluationMethod (string) --
Information about the order in which events are evaluated and how actions are executed.









Exceptions

IoTEvents.Client.exceptions.InvalidRequestException
IoTEvents.Client.exceptions.ResourceInUseException
IoTEvents.Client.exceptions.ResourceAlreadyExistsException
IoTEvents.Client.exceptions.LimitExceededException
IoTEvents.Client.exceptions.ThrottlingException
IoTEvents.Client.exceptions.InternalFailureException
IoTEvents.Client.exceptions.ServiceUnavailableException


    :return: {
        'detectorModelConfiguration': {
            'detectorModelName': 'string',
            'detectorModelVersion': 'string',
            'detectorModelDescription': 'string',
            'detectorModelArn': 'string',
            'roleArn': 'string',
            'creationTime': datetime(2015, 1, 1),
            'lastUpdateTime': datetime(2015, 1, 1),
            'status': 'ACTIVE'|'ACTIVATING'|'INACTIVE'|'DEPRECATED'|'DRAFT'|'PAUSED'|'FAILED',
            'key': 'string',
            'evaluationMethod': 'BATCH'|'SERIAL'
        }
    }
    
    
    :returns: 
    IoTEvents.Client.exceptions.InvalidRequestException
    IoTEvents.Client.exceptions.ResourceInUseException
    IoTEvents.Client.exceptions.ResourceAlreadyExistsException
    IoTEvents.Client.exceptions.LimitExceededException
    IoTEvents.Client.exceptions.ThrottlingException
    IoTEvents.Client.exceptions.InternalFailureException
    IoTEvents.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def create_input(inputName=None, inputDescription=None, inputDefinition=None, tags=None):
    """
    Creates an input.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_input(
        inputName='string',
        inputDescription='string',
        inputDefinition={
            'attributes': [
                {
                    'jsonPath': 'string'
                },
            ]
        },
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type inputName: string
    :param inputName: [REQUIRED]\nThe name you want to give to the input.\n

    :type inputDescription: string
    :param inputDescription: A brief description of the input.

    :type inputDefinition: dict
    :param inputDefinition: [REQUIRED]\nThe definition of the input.\n\nattributes (list) -- [REQUIRED]The attributes from the JSON payload that are made available by the input. Inputs are derived from messages sent to the AWS IoT Events system using BatchPutMessage . Each such message contains a JSON payload, and those attributes (and their paired values) specified here are available for use in the condition expressions used by detectors that monitor this input.\n\n(dict) --The attributes from the JSON payload that are made available by the input. Inputs are derived from messages sent to the AWS IoT Events system using BatchPutMessage . Each such message contains a JSON payload. Those attributes (and their paired values) specified here are available for use in the condition expressions used by detectors.\n\njsonPath (string) -- [REQUIRED]An expression that specifies an attribute-value pair in a JSON structure. Use this to specify an attribute from the JSON payload that is made available by the input. Inputs are derived from messages sent to AWS IoT Events (BatchPutMessage ). Each such message contains a JSON payload. The attribute (and its paired value) specified here are available for use in the condition expressions used by detectors.\nSyntax: <field-name>.<field-name>...\n\n\n\n\n\n\n

    :type tags: list
    :param tags: Metadata that can be used to manage the input.\n\n(dict) --Metadata that can be used to manage the resource.\n\nkey (string) -- [REQUIRED]The tag\'s key.\n\nvalue (string) -- [REQUIRED]The tag\'s value.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'inputConfiguration': {
        'inputName': 'string',
        'inputDescription': 'string',
        'inputArn': 'string',
        'creationTime': datetime(2015, 1, 1),
        'lastUpdateTime': datetime(2015, 1, 1),
        'status': 'CREATING'|'UPDATING'|'ACTIVE'|'DELETING'
    }
}


Response Structure

(dict) --

inputConfiguration (dict) --
Information about the configuration of the input.

inputName (string) --
The name of the input.

inputDescription (string) --
A brief description of the input.

inputArn (string) --
The ARN of the input.

creationTime (datetime) --
The time the input was created.

lastUpdateTime (datetime) --
The last time the input was updated.

status (string) --
The status of the input.









Exceptions

IoTEvents.Client.exceptions.InvalidRequestException
IoTEvents.Client.exceptions.ThrottlingException
IoTEvents.Client.exceptions.InternalFailureException
IoTEvents.Client.exceptions.ServiceUnavailableException
IoTEvents.Client.exceptions.ResourceAlreadyExistsException


    :return: {
        'inputConfiguration': {
            'inputName': 'string',
            'inputDescription': 'string',
            'inputArn': 'string',
            'creationTime': datetime(2015, 1, 1),
            'lastUpdateTime': datetime(2015, 1, 1),
            'status': 'CREATING'|'UPDATING'|'ACTIVE'|'DELETING'
        }
    }
    
    
    :returns: 
    IoTEvents.Client.exceptions.InvalidRequestException
    IoTEvents.Client.exceptions.ThrottlingException
    IoTEvents.Client.exceptions.InternalFailureException
    IoTEvents.Client.exceptions.ServiceUnavailableException
    IoTEvents.Client.exceptions.ResourceAlreadyExistsException
    
    """
    pass

def delete_detector_model(detectorModelName=None):
    """
    Deletes a detector model. Any active instances of the detector model are also deleted.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_detector_model(
        detectorModelName='string'
    )
    
    
    :type detectorModelName: string
    :param detectorModelName: [REQUIRED]\nThe name of the detector model to be deleted.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

IoTEvents.Client.exceptions.InvalidRequestException
IoTEvents.Client.exceptions.ResourceInUseException
IoTEvents.Client.exceptions.ResourceNotFoundException
IoTEvents.Client.exceptions.ThrottlingException
IoTEvents.Client.exceptions.InternalFailureException
IoTEvents.Client.exceptions.ServiceUnavailableException


    :return: {}
    
    
    :returns: 
    IoTEvents.Client.exceptions.InvalidRequestException
    IoTEvents.Client.exceptions.ResourceInUseException
    IoTEvents.Client.exceptions.ResourceNotFoundException
    IoTEvents.Client.exceptions.ThrottlingException
    IoTEvents.Client.exceptions.InternalFailureException
    IoTEvents.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def delete_input(inputName=None):
    """
    Deletes an input.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_input(
        inputName='string'
    )
    
    
    :type inputName: string
    :param inputName: [REQUIRED]\nThe name of the input to delete.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

IoTEvents.Client.exceptions.InvalidRequestException
IoTEvents.Client.exceptions.ResourceNotFoundException
IoTEvents.Client.exceptions.ThrottlingException
IoTEvents.Client.exceptions.InternalFailureException
IoTEvents.Client.exceptions.ServiceUnavailableException
IoTEvents.Client.exceptions.ResourceInUseException


    :return: {}
    
    
    :returns: 
    IoTEvents.Client.exceptions.InvalidRequestException
    IoTEvents.Client.exceptions.ResourceNotFoundException
    IoTEvents.Client.exceptions.ThrottlingException
    IoTEvents.Client.exceptions.InternalFailureException
    IoTEvents.Client.exceptions.ServiceUnavailableException
    IoTEvents.Client.exceptions.ResourceInUseException
    
    """
    pass

def describe_detector_model(detectorModelName=None, detectorModelVersion=None):
    """
    Describes a detector model. If the version parameter is not specified, information about the latest version is returned.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_detector_model(
        detectorModelName='string',
        detectorModelVersion='string'
    )
    
    
    :type detectorModelName: string
    :param detectorModelName: [REQUIRED]\nThe name of the detector model.\n

    :type detectorModelVersion: string
    :param detectorModelVersion: The version of the detector model.

    :rtype: dict

ReturnsResponse Syntax
{
    'detectorModel': {
        'detectorModelDefinition': {
            'states': [
                {
                    'stateName': 'string',
                    'onInput': {
                        'events': [
                            {
                                'eventName': 'string',
                                'condition': 'string',
                                'actions': [
                                    {
                                        'setVariable': {
                                            'variableName': 'string',
                                            'value': 'string'
                                        },
                                        'sns': {
                                            'targetArn': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'iotTopicPublish': {
                                            'mqttTopic': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'setTimer': {
                                            'timerName': 'string',
                                            'seconds': 123,
                                            'durationExpression': 'string'
                                        },
                                        'clearTimer': {
                                            'timerName': 'string'
                                        },
                                        'resetTimer': {
                                            'timerName': 'string'
                                        },
                                        'lambda': {
                                            'functionArn': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'iotEvents': {
                                            'inputName': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'sqs': {
                                            'queueUrl': 'string',
                                            'useBase64': True|False,
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'firehose': {
                                            'deliveryStreamName': 'string',
                                            'separator': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'dynamoDB': {
                                            'hashKeyType': 'string',
                                            'hashKeyField': 'string',
                                            'hashKeyValue': 'string',
                                            'rangeKeyType': 'string',
                                            'rangeKeyField': 'string',
                                            'rangeKeyValue': 'string',
                                            'operation': 'string',
                                            'payloadField': 'string',
                                            'tableName': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'dynamoDBv2': {
                                            'tableName': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'iotSiteWise': {
                                            'entryId': 'string',
                                            'assetId': 'string',
                                            'propertyId': 'string',
                                            'propertyAlias': 'string',
                                            'propertyValue': {
                                                'value': {
                                                    'stringValue': 'string',
                                                    'integerValue': 'string',
                                                    'doubleValue': 'string',
                                                    'booleanValue': 'string'
                                                },
                                                'timestamp': {
                                                    'timeInSeconds': 'string',
                                                    'offsetInNanos': 'string'
                                                },
                                                'quality': 'string'
                                            }
                                        }
                                    },
                                ]
                            },
                        ],
                        'transitionEvents': [
                            {
                                'eventName': 'string',
                                'condition': 'string',
                                'actions': [
                                    {
                                        'setVariable': {
                                            'variableName': 'string',
                                            'value': 'string'
                                        },
                                        'sns': {
                                            'targetArn': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'iotTopicPublish': {
                                            'mqttTopic': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'setTimer': {
                                            'timerName': 'string',
                                            'seconds': 123,
                                            'durationExpression': 'string'
                                        },
                                        'clearTimer': {
                                            'timerName': 'string'
                                        },
                                        'resetTimer': {
                                            'timerName': 'string'
                                        },
                                        'lambda': {
                                            'functionArn': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'iotEvents': {
                                            'inputName': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'sqs': {
                                            'queueUrl': 'string',
                                            'useBase64': True|False,
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'firehose': {
                                            'deliveryStreamName': 'string',
                                            'separator': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'dynamoDB': {
                                            'hashKeyType': 'string',
                                            'hashKeyField': 'string',
                                            'hashKeyValue': 'string',
                                            'rangeKeyType': 'string',
                                            'rangeKeyField': 'string',
                                            'rangeKeyValue': 'string',
                                            'operation': 'string',
                                            'payloadField': 'string',
                                            'tableName': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'dynamoDBv2': {
                                            'tableName': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'iotSiteWise': {
                                            'entryId': 'string',
                                            'assetId': 'string',
                                            'propertyId': 'string',
                                            'propertyAlias': 'string',
                                            'propertyValue': {
                                                'value': {
                                                    'stringValue': 'string',
                                                    'integerValue': 'string',
                                                    'doubleValue': 'string',
                                                    'booleanValue': 'string'
                                                },
                                                'timestamp': {
                                                    'timeInSeconds': 'string',
                                                    'offsetInNanos': 'string'
                                                },
                                                'quality': 'string'
                                            }
                                        }
                                    },
                                ],
                                'nextState': 'string'
                            },
                        ]
                    },
                    'onEnter': {
                        'events': [
                            {
                                'eventName': 'string',
                                'condition': 'string',
                                'actions': [
                                    {
                                        'setVariable': {
                                            'variableName': 'string',
                                            'value': 'string'
                                        },
                                        'sns': {
                                            'targetArn': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'iotTopicPublish': {
                                            'mqttTopic': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'setTimer': {
                                            'timerName': 'string',
                                            'seconds': 123,
                                            'durationExpression': 'string'
                                        },
                                        'clearTimer': {
                                            'timerName': 'string'
                                        },
                                        'resetTimer': {
                                            'timerName': 'string'
                                        },
                                        'lambda': {
                                            'functionArn': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'iotEvents': {
                                            'inputName': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'sqs': {
                                            'queueUrl': 'string',
                                            'useBase64': True|False,
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'firehose': {
                                            'deliveryStreamName': 'string',
                                            'separator': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'dynamoDB': {
                                            'hashKeyType': 'string',
                                            'hashKeyField': 'string',
                                            'hashKeyValue': 'string',
                                            'rangeKeyType': 'string',
                                            'rangeKeyField': 'string',
                                            'rangeKeyValue': 'string',
                                            'operation': 'string',
                                            'payloadField': 'string',
                                            'tableName': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'dynamoDBv2': {
                                            'tableName': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'iotSiteWise': {
                                            'entryId': 'string',
                                            'assetId': 'string',
                                            'propertyId': 'string',
                                            'propertyAlias': 'string',
                                            'propertyValue': {
                                                'value': {
                                                    'stringValue': 'string',
                                                    'integerValue': 'string',
                                                    'doubleValue': 'string',
                                                    'booleanValue': 'string'
                                                },
                                                'timestamp': {
                                                    'timeInSeconds': 'string',
                                                    'offsetInNanos': 'string'
                                                },
                                                'quality': 'string'
                                            }
                                        }
                                    },
                                ]
                            },
                        ]
                    },
                    'onExit': {
                        'events': [
                            {
                                'eventName': 'string',
                                'condition': 'string',
                                'actions': [
                                    {
                                        'setVariable': {
                                            'variableName': 'string',
                                            'value': 'string'
                                        },
                                        'sns': {
                                            'targetArn': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'iotTopicPublish': {
                                            'mqttTopic': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'setTimer': {
                                            'timerName': 'string',
                                            'seconds': 123,
                                            'durationExpression': 'string'
                                        },
                                        'clearTimer': {
                                            'timerName': 'string'
                                        },
                                        'resetTimer': {
                                            'timerName': 'string'
                                        },
                                        'lambda': {
                                            'functionArn': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'iotEvents': {
                                            'inputName': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'sqs': {
                                            'queueUrl': 'string',
                                            'useBase64': True|False,
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'firehose': {
                                            'deliveryStreamName': 'string',
                                            'separator': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'dynamoDB': {
                                            'hashKeyType': 'string',
                                            'hashKeyField': 'string',
                                            'hashKeyValue': 'string',
                                            'rangeKeyType': 'string',
                                            'rangeKeyField': 'string',
                                            'rangeKeyValue': 'string',
                                            'operation': 'string',
                                            'payloadField': 'string',
                                            'tableName': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'dynamoDBv2': {
                                            'tableName': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'iotSiteWise': {
                                            'entryId': 'string',
                                            'assetId': 'string',
                                            'propertyId': 'string',
                                            'propertyAlias': 'string',
                                            'propertyValue': {
                                                'value': {
                                                    'stringValue': 'string',
                                                    'integerValue': 'string',
                                                    'doubleValue': 'string',
                                                    'booleanValue': 'string'
                                                },
                                                'timestamp': {
                                                    'timeInSeconds': 'string',
                                                    'offsetInNanos': 'string'
                                                },
                                                'quality': 'string'
                                            }
                                        }
                                    },
                                ]
                            },
                        ]
                    }
                },
            ],
            'initialStateName': 'string'
        },
        'detectorModelConfiguration': {
            'detectorModelName': 'string',
            'detectorModelVersion': 'string',
            'detectorModelDescription': 'string',
            'detectorModelArn': 'string',
            'roleArn': 'string',
            'creationTime': datetime(2015, 1, 1),
            'lastUpdateTime': datetime(2015, 1, 1),
            'status': 'ACTIVE'|'ACTIVATING'|'INACTIVE'|'DEPRECATED'|'DRAFT'|'PAUSED'|'FAILED',
            'key': 'string',
            'evaluationMethod': 'BATCH'|'SERIAL'
        }
    }
}


Response Structure

(dict) --

detectorModel (dict) --
Information about the detector model.

detectorModelDefinition (dict) --
Information that defines how a detector operates.

states (list) --
Information about the states of the detector.

(dict) --
Information that defines a state of a detector.

stateName (string) --
The name of the state.

onInput (dict) --
When an input is received and the condition is TRUE, perform the specified actions .

events (list) --
Specifies the actions performed when the condition evaluates to TRUE.

(dict) --
Specifies the actions to be performed when the condition evaluates to TRUE.

eventName (string) --
The name of the event.

condition (string) --
Optional. The Boolean expression that, when TRUE, causes the actions to be performed. If not present, the actions are performed (=TRUE). If the expression result is not a Boolean value, the actions are not performed (=FALSE).

actions (list) --
The actions to be performed.

(dict) --
An action to be performed when the condition is TRUE.

setVariable (dict) --
Sets a variable to a specified value.

variableName (string) --
The name of the variable.

value (string) --
The new value of the variable.



sns (dict) --
Sends an Amazon SNS message.

targetArn (string) --
The ARN of the Amazon SNS target where the message is sent.

payload (dict) --
You can configure the action payload when you send a message as an Amazon SNS push notification.

contentExpression (string) --
The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.

type (string) --
The value of the payload type can be either STRING or JSON .





iotTopicPublish (dict) --
Publishes an MQTT message with the given topic to the AWS IoT message broker.

mqttTopic (string) --
The MQTT topic of the message. You can use a string expression that includes variables ($variable.<variable-name> ) and input values ($input.<input-name>.<path-to-datum> ) as the topic string.

payload (dict) --
You can configure the action payload when you publish a message to an AWS IoT Core topic.

contentExpression (string) --
The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.

type (string) --
The value of the payload type can be either STRING or JSON .





setTimer (dict) --
Information needed to set the timer.

timerName (string) --
The name of the timer.

seconds (integer) --
The number of seconds until the timer expires. The minimum value is 60 seconds to ensure accuracy. The maximum value is 31622400 seconds.

durationExpression (string) --
The duration of the timer, in seconds. You can use a string expression that includes numbers, variables ($variable.<variable-name> ), and input values ($input.<input-name>.<path-to-datum> ) as the duration. The range of the duration is 1-31622400 seconds. To ensure accuracy, the minimum duration is 60 seconds. The evaluated result of the duration is rounded down to the nearest whole number.



clearTimer (dict) --
Information needed to clear the timer.

timerName (string) --
The name of the timer to clear.



resetTimer (dict) --
Information needed to reset the timer.

timerName (string) --
The name of the timer to reset.



lambda (dict) --
Calls a Lambda function, passing in information about the detector model instance and the event that triggered the action.

functionArn (string) --
The ARN of the Lambda function that is executed.

payload (dict) --
You can configure the action payload when you send a message to a Lambda function.

contentExpression (string) --
The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.

type (string) --
The value of the payload type can be either STRING or JSON .





iotEvents (dict) --
Sends AWS IoT Events input, which passes information about the detector model instance and the event that triggered the action.

inputName (string) --
The name of the AWS IoT Events input where the data is sent.

payload (dict) --
You can configure the action payload when you send a message to an AWS IoT Events input.

contentExpression (string) --
The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.

type (string) --
The value of the payload type can be either STRING or JSON .





sqs (dict) --
Sends information about the detector model instance and the event that triggered the action to an Amazon SQS queue.

queueUrl (string) --
The URL of the SQS queue where the data is written.

useBase64 (boolean) --
Set this to TRUE if you want the data to be base-64 encoded before it is written to the queue. Otherwise, set this to FALSE.

payload (dict) --
You can configure the action payload when you send a message to an Amazon SQS queue.

contentExpression (string) --
The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.

type (string) --
The value of the payload type can be either STRING or JSON .





firehose (dict) --
Sends information about the detector model instance and the event that triggered the action to an Amazon Kinesis Data Firehose delivery stream.

deliveryStreamName (string) --
The name of the Kinesis Data Firehose delivery stream where the data is written.

separator (string) --
A character separator that is used to separate records written to the Kinesis Data Firehose delivery stream. Valid values are: \'n\' (newline), \'t\' (tab), \'rn\' (Windows newline), \',\' (comma).

payload (dict) --
You can configure the action payload when you send a message to an Amazon Kinesis Data Firehose delivery stream.

contentExpression (string) --
The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.

type (string) --
The value of the payload type can be either STRING or JSON .





dynamoDB (dict) --
Writes to the DynamoDB table that you created. The default action payload contains all attribute-value pairs that have the information about the detector model instance and the event that triggered the action. You can also customize the payload . One column of the DynamoDB table receives all attribute-value pairs in the payload that you specify. For more information, see Actions in AWS IoT Events Developer Guide .

hashKeyType (string) --
The data type for the hash key (also called the partition key). You can specify the following values:

STRING - The hash key is a string.
NUMBER - The hash key is a number.

If you don\'t specify hashKeyType , the default value is STRING .

hashKeyField (string) --
The name of the hash key (also called the partition key).

hashKeyValue (string) --
The value of the hash key (also called the partition key).

rangeKeyType (string) --
The data type for the range key (also called the sort key), You can specify the following values:

STRING - The range key is a string.
NUMBER - The range key is number.

If you don\'t specify rangeKeyField , the default value is STRING .

rangeKeyField (string) --
The name of the range key (also called the sort key).

rangeKeyValue (string) --
The value of the range key (also called the sort key).

operation (string) --
The type of operation to perform. You can specify the following values:

INSERT - Insert data as a new item into the DynamoDB table. This item uses the specified hash key as a partition key. If you specified a range key, the item uses the range key as a sort key.
UPDATE - Update an existing item of the DynamoDB table with new data. This item\'s partition key must match the specified hash key. If you specified a range key, the range key must match the item\'s sort key.
DELETE - Delete an existing item of the DynamoDB table. This item\'s partition key must match the specified hash key. If you specified a range key, the range key must match the item\'s sort key.

If you don\'t specify this parameter, AWS IoT Events triggers the INSERT operation.

payloadField (string) --
The name of the DynamoDB column that receives the action payload.
If you don\'t specify this parameter, the name of the DynamoDB column is payload .

tableName (string) --
The name of the DynamoDB table.

payload (dict) --
Information needed to configure the payload.
By default, AWS IoT Events generates a standard payload in JSON for any action. This action payload contains all attribute-value pairs that have the information about the detector model instance and the event triggered the action. To configure the action payload, you can use contentExpression .

contentExpression (string) --
The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.

type (string) --
The value of the payload type can be either STRING or JSON .





dynamoDBv2 (dict) --
Writes to the DynamoDB table that you created. The default action payload contains all attribute-value pairs that have the information about the detector model instance and the event that triggered the action. You can also customize the payload . A separate column of the DynamoDB table receives one attribute-value pair in the payload that you specify. For more information, see Actions in AWS IoT Events Developer Guide .

tableName (string) --
The name of the DynamoDB table.

payload (dict) --
Information needed to configure the payload.
By default, AWS IoT Events generates a standard payload in JSON for any action. This action payload contains all attribute-value pairs that have the information about the detector model instance and the event triggered the action. To configure the action payload, you can use contentExpression .

contentExpression (string) --
The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.

type (string) --
The value of the payload type can be either STRING or JSON .





iotSiteWise (dict) --
Sends information about the detector model instance and the event that triggered the action to an asset property in AWS IoT SiteWise .

entryId (string) --
A unique identifier for this entry. You can use the entry ID to track which data entry causes an error in case of failure. The default is a new unique identifier. You can also specify an expression.

assetId (string) --
The ID of the asset that has the specified property. You can specify an expression.

propertyId (string) --
The ID of the asset property. You can specify an expression.

propertyAlias (string) --
The alias of the asset property. You can also specify an expression.

propertyValue (dict) --
The value to send to the asset property. This value contains timestamp, quality, and value (TQV) information.

value (dict) --
The value to send to an asset property.

stringValue (string) --
The asset property value is a string. You can also specify an expression. If you use an expression, the evaluated result should be a string.

integerValue (string) --
The asset property value is an integer. You can also specify an expression. If you use an expression, the evaluated result should be an integer.

doubleValue (string) --
The asset property value is a double. You can also specify an expression. If you use an expression, the evaluated result should be a double.

booleanValue (string) --
The asset property value is a Boolean value that must be TRUE or FALSE . You can also specify an expression. If you use an expression, the evaluated result should be a Boolean value.



timestamp (dict) --
The timestamp associated with the asset property value. The default is the current event time.

timeInSeconds (string) --
The timestamp, in seconds, in the Unix epoch format. The valid range is between 1-31556889864403199. You can also specify an expression.

offsetInNanos (string) --
The nanosecond offset converted from timeInSeconds . The valid range is between 0-999999999. You can also specify an expression.



quality (string) --
The quality of the asset property value. The value must be GOOD , BAD , or UNCERTAIN . You can also specify an expression.













transitionEvents (list) --
Specifies the actions performed, and the next state entered, when a condition evaluates to TRUE.

(dict) --
Specifies the actions performed and the next state entered when a condition evaluates to TRUE.

eventName (string) --
The name of the transition event.

condition (string) --
Required. A Boolean expression that when TRUE causes the actions to be performed and the nextState to be entered.

actions (list) --
The actions to be performed.

(dict) --
An action to be performed when the condition is TRUE.

setVariable (dict) --
Sets a variable to a specified value.

variableName (string) --
The name of the variable.

value (string) --
The new value of the variable.



sns (dict) --
Sends an Amazon SNS message.

targetArn (string) --
The ARN of the Amazon SNS target where the message is sent.

payload (dict) --
You can configure the action payload when you send a message as an Amazon SNS push notification.

contentExpression (string) --
The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.

type (string) --
The value of the payload type can be either STRING or JSON .





iotTopicPublish (dict) --
Publishes an MQTT message with the given topic to the AWS IoT message broker.

mqttTopic (string) --
The MQTT topic of the message. You can use a string expression that includes variables ($variable.<variable-name> ) and input values ($input.<input-name>.<path-to-datum> ) as the topic string.

payload (dict) --
You can configure the action payload when you publish a message to an AWS IoT Core topic.

contentExpression (string) --
The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.

type (string) --
The value of the payload type can be either STRING or JSON .





setTimer (dict) --
Information needed to set the timer.

timerName (string) --
The name of the timer.

seconds (integer) --
The number of seconds until the timer expires. The minimum value is 60 seconds to ensure accuracy. The maximum value is 31622400 seconds.

durationExpression (string) --
The duration of the timer, in seconds. You can use a string expression that includes numbers, variables ($variable.<variable-name> ), and input values ($input.<input-name>.<path-to-datum> ) as the duration. The range of the duration is 1-31622400 seconds. To ensure accuracy, the minimum duration is 60 seconds. The evaluated result of the duration is rounded down to the nearest whole number.



clearTimer (dict) --
Information needed to clear the timer.

timerName (string) --
The name of the timer to clear.



resetTimer (dict) --
Information needed to reset the timer.

timerName (string) --
The name of the timer to reset.



lambda (dict) --
Calls a Lambda function, passing in information about the detector model instance and the event that triggered the action.

functionArn (string) --
The ARN of the Lambda function that is executed.

payload (dict) --
You can configure the action payload when you send a message to a Lambda function.

contentExpression (string) --
The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.

type (string) --
The value of the payload type can be either STRING or JSON .





iotEvents (dict) --
Sends AWS IoT Events input, which passes information about the detector model instance and the event that triggered the action.

inputName (string) --
The name of the AWS IoT Events input where the data is sent.

payload (dict) --
You can configure the action payload when you send a message to an AWS IoT Events input.

contentExpression (string) --
The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.

type (string) --
The value of the payload type can be either STRING or JSON .





sqs (dict) --
Sends information about the detector model instance and the event that triggered the action to an Amazon SQS queue.

queueUrl (string) --
The URL of the SQS queue where the data is written.

useBase64 (boolean) --
Set this to TRUE if you want the data to be base-64 encoded before it is written to the queue. Otherwise, set this to FALSE.

payload (dict) --
You can configure the action payload when you send a message to an Amazon SQS queue.

contentExpression (string) --
The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.

type (string) --
The value of the payload type can be either STRING or JSON .





firehose (dict) --
Sends information about the detector model instance and the event that triggered the action to an Amazon Kinesis Data Firehose delivery stream.

deliveryStreamName (string) --
The name of the Kinesis Data Firehose delivery stream where the data is written.

separator (string) --
A character separator that is used to separate records written to the Kinesis Data Firehose delivery stream. Valid values are: \'n\' (newline), \'t\' (tab), \'rn\' (Windows newline), \',\' (comma).

payload (dict) --
You can configure the action payload when you send a message to an Amazon Kinesis Data Firehose delivery stream.

contentExpression (string) --
The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.

type (string) --
The value of the payload type can be either STRING or JSON .





dynamoDB (dict) --
Writes to the DynamoDB table that you created. The default action payload contains all attribute-value pairs that have the information about the detector model instance and the event that triggered the action. You can also customize the payload . One column of the DynamoDB table receives all attribute-value pairs in the payload that you specify. For more information, see Actions in AWS IoT Events Developer Guide .

hashKeyType (string) --
The data type for the hash key (also called the partition key). You can specify the following values:

STRING - The hash key is a string.
NUMBER - The hash key is a number.

If you don\'t specify hashKeyType , the default value is STRING .

hashKeyField (string) --
The name of the hash key (also called the partition key).

hashKeyValue (string) --
The value of the hash key (also called the partition key).

rangeKeyType (string) --
The data type for the range key (also called the sort key), You can specify the following values:

STRING - The range key is a string.
NUMBER - The range key is number.

If you don\'t specify rangeKeyField , the default value is STRING .

rangeKeyField (string) --
The name of the range key (also called the sort key).

rangeKeyValue (string) --
The value of the range key (also called the sort key).

operation (string) --
The type of operation to perform. You can specify the following values:

INSERT - Insert data as a new item into the DynamoDB table. This item uses the specified hash key as a partition key. If you specified a range key, the item uses the range key as a sort key.
UPDATE - Update an existing item of the DynamoDB table with new data. This item\'s partition key must match the specified hash key. If you specified a range key, the range key must match the item\'s sort key.
DELETE - Delete an existing item of the DynamoDB table. This item\'s partition key must match the specified hash key. If you specified a range key, the range key must match the item\'s sort key.

If you don\'t specify this parameter, AWS IoT Events triggers the INSERT operation.

payloadField (string) --
The name of the DynamoDB column that receives the action payload.
If you don\'t specify this parameter, the name of the DynamoDB column is payload .

tableName (string) --
The name of the DynamoDB table.

payload (dict) --
Information needed to configure the payload.
By default, AWS IoT Events generates a standard payload in JSON for any action. This action payload contains all attribute-value pairs that have the information about the detector model instance and the event triggered the action. To configure the action payload, you can use contentExpression .

contentExpression (string) --
The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.

type (string) --
The value of the payload type can be either STRING or JSON .





dynamoDBv2 (dict) --
Writes to the DynamoDB table that you created. The default action payload contains all attribute-value pairs that have the information about the detector model instance and the event that triggered the action. You can also customize the payload . A separate column of the DynamoDB table receives one attribute-value pair in the payload that you specify. For more information, see Actions in AWS IoT Events Developer Guide .

tableName (string) --
The name of the DynamoDB table.

payload (dict) --
Information needed to configure the payload.
By default, AWS IoT Events generates a standard payload in JSON for any action. This action payload contains all attribute-value pairs that have the information about the detector model instance and the event triggered the action. To configure the action payload, you can use contentExpression .

contentExpression (string) --
The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.

type (string) --
The value of the payload type can be either STRING or JSON .





iotSiteWise (dict) --
Sends information about the detector model instance and the event that triggered the action to an asset property in AWS IoT SiteWise .

entryId (string) --
A unique identifier for this entry. You can use the entry ID to track which data entry causes an error in case of failure. The default is a new unique identifier. You can also specify an expression.

assetId (string) --
The ID of the asset that has the specified property. You can specify an expression.

propertyId (string) --
The ID of the asset property. You can specify an expression.

propertyAlias (string) --
The alias of the asset property. You can also specify an expression.

propertyValue (dict) --
The value to send to the asset property. This value contains timestamp, quality, and value (TQV) information.

value (dict) --
The value to send to an asset property.

stringValue (string) --
The asset property value is a string. You can also specify an expression. If you use an expression, the evaluated result should be a string.

integerValue (string) --
The asset property value is an integer. You can also specify an expression. If you use an expression, the evaluated result should be an integer.

doubleValue (string) --
The asset property value is a double. You can also specify an expression. If you use an expression, the evaluated result should be a double.

booleanValue (string) --
The asset property value is a Boolean value that must be TRUE or FALSE . You can also specify an expression. If you use an expression, the evaluated result should be a Boolean value.



timestamp (dict) --
The timestamp associated with the asset property value. The default is the current event time.

timeInSeconds (string) --
The timestamp, in seconds, in the Unix epoch format. The valid range is between 1-31556889864403199. You can also specify an expression.

offsetInNanos (string) --
The nanosecond offset converted from timeInSeconds . The valid range is between 0-999999999. You can also specify an expression.



quality (string) --
The quality of the asset property value. The value must be GOOD , BAD , or UNCERTAIN . You can also specify an expression.









nextState (string) --
The next state to enter.







onEnter (dict) --
When entering this state, perform these actions if the condition is TRUE.

events (list) --
Specifies the actions that are performed when the state is entered and the condition is TRUE .

(dict) --
Specifies the actions to be performed when the condition evaluates to TRUE.

eventName (string) --
The name of the event.

condition (string) --
Optional. The Boolean expression that, when TRUE, causes the actions to be performed. If not present, the actions are performed (=TRUE). If the expression result is not a Boolean value, the actions are not performed (=FALSE).

actions (list) --
The actions to be performed.

(dict) --
An action to be performed when the condition is TRUE.

setVariable (dict) --
Sets a variable to a specified value.

variableName (string) --
The name of the variable.

value (string) --
The new value of the variable.



sns (dict) --
Sends an Amazon SNS message.

targetArn (string) --
The ARN of the Amazon SNS target where the message is sent.

payload (dict) --
You can configure the action payload when you send a message as an Amazon SNS push notification.

contentExpression (string) --
The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.

type (string) --
The value of the payload type can be either STRING or JSON .





iotTopicPublish (dict) --
Publishes an MQTT message with the given topic to the AWS IoT message broker.

mqttTopic (string) --
The MQTT topic of the message. You can use a string expression that includes variables ($variable.<variable-name> ) and input values ($input.<input-name>.<path-to-datum> ) as the topic string.

payload (dict) --
You can configure the action payload when you publish a message to an AWS IoT Core topic.

contentExpression (string) --
The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.

type (string) --
The value of the payload type can be either STRING or JSON .





setTimer (dict) --
Information needed to set the timer.

timerName (string) --
The name of the timer.

seconds (integer) --
The number of seconds until the timer expires. The minimum value is 60 seconds to ensure accuracy. The maximum value is 31622400 seconds.

durationExpression (string) --
The duration of the timer, in seconds. You can use a string expression that includes numbers, variables ($variable.<variable-name> ), and input values ($input.<input-name>.<path-to-datum> ) as the duration. The range of the duration is 1-31622400 seconds. To ensure accuracy, the minimum duration is 60 seconds. The evaluated result of the duration is rounded down to the nearest whole number.



clearTimer (dict) --
Information needed to clear the timer.

timerName (string) --
The name of the timer to clear.



resetTimer (dict) --
Information needed to reset the timer.

timerName (string) --
The name of the timer to reset.



lambda (dict) --
Calls a Lambda function, passing in information about the detector model instance and the event that triggered the action.

functionArn (string) --
The ARN of the Lambda function that is executed.

payload (dict) --
You can configure the action payload when you send a message to a Lambda function.

contentExpression (string) --
The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.

type (string) --
The value of the payload type can be either STRING or JSON .





iotEvents (dict) --
Sends AWS IoT Events input, which passes information about the detector model instance and the event that triggered the action.

inputName (string) --
The name of the AWS IoT Events input where the data is sent.

payload (dict) --
You can configure the action payload when you send a message to an AWS IoT Events input.

contentExpression (string) --
The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.

type (string) --
The value of the payload type can be either STRING or JSON .





sqs (dict) --
Sends information about the detector model instance and the event that triggered the action to an Amazon SQS queue.

queueUrl (string) --
The URL of the SQS queue where the data is written.

useBase64 (boolean) --
Set this to TRUE if you want the data to be base-64 encoded before it is written to the queue. Otherwise, set this to FALSE.

payload (dict) --
You can configure the action payload when you send a message to an Amazon SQS queue.

contentExpression (string) --
The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.

type (string) --
The value of the payload type can be either STRING or JSON .





firehose (dict) --
Sends information about the detector model instance and the event that triggered the action to an Amazon Kinesis Data Firehose delivery stream.

deliveryStreamName (string) --
The name of the Kinesis Data Firehose delivery stream where the data is written.

separator (string) --
A character separator that is used to separate records written to the Kinesis Data Firehose delivery stream. Valid values are: \'n\' (newline), \'t\' (tab), \'rn\' (Windows newline), \',\' (comma).

payload (dict) --
You can configure the action payload when you send a message to an Amazon Kinesis Data Firehose delivery stream.

contentExpression (string) --
The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.

type (string) --
The value of the payload type can be either STRING or JSON .





dynamoDB (dict) --
Writes to the DynamoDB table that you created. The default action payload contains all attribute-value pairs that have the information about the detector model instance and the event that triggered the action. You can also customize the payload . One column of the DynamoDB table receives all attribute-value pairs in the payload that you specify. For more information, see Actions in AWS IoT Events Developer Guide .

hashKeyType (string) --
The data type for the hash key (also called the partition key). You can specify the following values:

STRING - The hash key is a string.
NUMBER - The hash key is a number.

If you don\'t specify hashKeyType , the default value is STRING .

hashKeyField (string) --
The name of the hash key (also called the partition key).

hashKeyValue (string) --
The value of the hash key (also called the partition key).

rangeKeyType (string) --
The data type for the range key (also called the sort key), You can specify the following values:

STRING - The range key is a string.
NUMBER - The range key is number.

If you don\'t specify rangeKeyField , the default value is STRING .

rangeKeyField (string) --
The name of the range key (also called the sort key).

rangeKeyValue (string) --
The value of the range key (also called the sort key).

operation (string) --
The type of operation to perform. You can specify the following values:

INSERT - Insert data as a new item into the DynamoDB table. This item uses the specified hash key as a partition key. If you specified a range key, the item uses the range key as a sort key.
UPDATE - Update an existing item of the DynamoDB table with new data. This item\'s partition key must match the specified hash key. If you specified a range key, the range key must match the item\'s sort key.
DELETE - Delete an existing item of the DynamoDB table. This item\'s partition key must match the specified hash key. If you specified a range key, the range key must match the item\'s sort key.

If you don\'t specify this parameter, AWS IoT Events triggers the INSERT operation.

payloadField (string) --
The name of the DynamoDB column that receives the action payload.
If you don\'t specify this parameter, the name of the DynamoDB column is payload .

tableName (string) --
The name of the DynamoDB table.

payload (dict) --
Information needed to configure the payload.
By default, AWS IoT Events generates a standard payload in JSON for any action. This action payload contains all attribute-value pairs that have the information about the detector model instance and the event triggered the action. To configure the action payload, you can use contentExpression .

contentExpression (string) --
The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.

type (string) --
The value of the payload type can be either STRING or JSON .





dynamoDBv2 (dict) --
Writes to the DynamoDB table that you created. The default action payload contains all attribute-value pairs that have the information about the detector model instance and the event that triggered the action. You can also customize the payload . A separate column of the DynamoDB table receives one attribute-value pair in the payload that you specify. For more information, see Actions in AWS IoT Events Developer Guide .

tableName (string) --
The name of the DynamoDB table.

payload (dict) --
Information needed to configure the payload.
By default, AWS IoT Events generates a standard payload in JSON for any action. This action payload contains all attribute-value pairs that have the information about the detector model instance and the event triggered the action. To configure the action payload, you can use contentExpression .

contentExpression (string) --
The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.

type (string) --
The value of the payload type can be either STRING or JSON .





iotSiteWise (dict) --
Sends information about the detector model instance and the event that triggered the action to an asset property in AWS IoT SiteWise .

entryId (string) --
A unique identifier for this entry. You can use the entry ID to track which data entry causes an error in case of failure. The default is a new unique identifier. You can also specify an expression.

assetId (string) --
The ID of the asset that has the specified property. You can specify an expression.

propertyId (string) --
The ID of the asset property. You can specify an expression.

propertyAlias (string) --
The alias of the asset property. You can also specify an expression.

propertyValue (dict) --
The value to send to the asset property. This value contains timestamp, quality, and value (TQV) information.

value (dict) --
The value to send to an asset property.

stringValue (string) --
The asset property value is a string. You can also specify an expression. If you use an expression, the evaluated result should be a string.

integerValue (string) --
The asset property value is an integer. You can also specify an expression. If you use an expression, the evaluated result should be an integer.

doubleValue (string) --
The asset property value is a double. You can also specify an expression. If you use an expression, the evaluated result should be a double.

booleanValue (string) --
The asset property value is a Boolean value that must be TRUE or FALSE . You can also specify an expression. If you use an expression, the evaluated result should be a Boolean value.



timestamp (dict) --
The timestamp associated with the asset property value. The default is the current event time.

timeInSeconds (string) --
The timestamp, in seconds, in the Unix epoch format. The valid range is between 1-31556889864403199. You can also specify an expression.

offsetInNanos (string) --
The nanosecond offset converted from timeInSeconds . The valid range is between 0-999999999. You can also specify an expression.



quality (string) --
The quality of the asset property value. The value must be GOOD , BAD , or UNCERTAIN . You can also specify an expression.















onExit (dict) --
When exiting this state, perform these actions if the specified condition is TRUE .

events (list) --
Specifies the actions that are performed when the state is exited and the condition is TRUE .

(dict) --
Specifies the actions to be performed when the condition evaluates to TRUE.

eventName (string) --
The name of the event.

condition (string) --
Optional. The Boolean expression that, when TRUE, causes the actions to be performed. If not present, the actions are performed (=TRUE). If the expression result is not a Boolean value, the actions are not performed (=FALSE).

actions (list) --
The actions to be performed.

(dict) --
An action to be performed when the condition is TRUE.

setVariable (dict) --
Sets a variable to a specified value.

variableName (string) --
The name of the variable.

value (string) --
The new value of the variable.



sns (dict) --
Sends an Amazon SNS message.

targetArn (string) --
The ARN of the Amazon SNS target where the message is sent.

payload (dict) --
You can configure the action payload when you send a message as an Amazon SNS push notification.

contentExpression (string) --
The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.

type (string) --
The value of the payload type can be either STRING or JSON .





iotTopicPublish (dict) --
Publishes an MQTT message with the given topic to the AWS IoT message broker.

mqttTopic (string) --
The MQTT topic of the message. You can use a string expression that includes variables ($variable.<variable-name> ) and input values ($input.<input-name>.<path-to-datum> ) as the topic string.

payload (dict) --
You can configure the action payload when you publish a message to an AWS IoT Core topic.

contentExpression (string) --
The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.

type (string) --
The value of the payload type can be either STRING or JSON .





setTimer (dict) --
Information needed to set the timer.

timerName (string) --
The name of the timer.

seconds (integer) --
The number of seconds until the timer expires. The minimum value is 60 seconds to ensure accuracy. The maximum value is 31622400 seconds.

durationExpression (string) --
The duration of the timer, in seconds. You can use a string expression that includes numbers, variables ($variable.<variable-name> ), and input values ($input.<input-name>.<path-to-datum> ) as the duration. The range of the duration is 1-31622400 seconds. To ensure accuracy, the minimum duration is 60 seconds. The evaluated result of the duration is rounded down to the nearest whole number.



clearTimer (dict) --
Information needed to clear the timer.

timerName (string) --
The name of the timer to clear.



resetTimer (dict) --
Information needed to reset the timer.

timerName (string) --
The name of the timer to reset.



lambda (dict) --
Calls a Lambda function, passing in information about the detector model instance and the event that triggered the action.

functionArn (string) --
The ARN of the Lambda function that is executed.

payload (dict) --
You can configure the action payload when you send a message to a Lambda function.

contentExpression (string) --
The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.

type (string) --
The value of the payload type can be either STRING or JSON .





iotEvents (dict) --
Sends AWS IoT Events input, which passes information about the detector model instance and the event that triggered the action.

inputName (string) --
The name of the AWS IoT Events input where the data is sent.

payload (dict) --
You can configure the action payload when you send a message to an AWS IoT Events input.

contentExpression (string) --
The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.

type (string) --
The value of the payload type can be either STRING or JSON .





sqs (dict) --
Sends information about the detector model instance and the event that triggered the action to an Amazon SQS queue.

queueUrl (string) --
The URL of the SQS queue where the data is written.

useBase64 (boolean) --
Set this to TRUE if you want the data to be base-64 encoded before it is written to the queue. Otherwise, set this to FALSE.

payload (dict) --
You can configure the action payload when you send a message to an Amazon SQS queue.

contentExpression (string) --
The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.

type (string) --
The value of the payload type can be either STRING or JSON .





firehose (dict) --
Sends information about the detector model instance and the event that triggered the action to an Amazon Kinesis Data Firehose delivery stream.

deliveryStreamName (string) --
The name of the Kinesis Data Firehose delivery stream where the data is written.

separator (string) --
A character separator that is used to separate records written to the Kinesis Data Firehose delivery stream. Valid values are: \'n\' (newline), \'t\' (tab), \'rn\' (Windows newline), \',\' (comma).

payload (dict) --
You can configure the action payload when you send a message to an Amazon Kinesis Data Firehose delivery stream.

contentExpression (string) --
The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.

type (string) --
The value of the payload type can be either STRING or JSON .





dynamoDB (dict) --
Writes to the DynamoDB table that you created. The default action payload contains all attribute-value pairs that have the information about the detector model instance and the event that triggered the action. You can also customize the payload . One column of the DynamoDB table receives all attribute-value pairs in the payload that you specify. For more information, see Actions in AWS IoT Events Developer Guide .

hashKeyType (string) --
The data type for the hash key (also called the partition key). You can specify the following values:

STRING - The hash key is a string.
NUMBER - The hash key is a number.

If you don\'t specify hashKeyType , the default value is STRING .

hashKeyField (string) --
The name of the hash key (also called the partition key).

hashKeyValue (string) --
The value of the hash key (also called the partition key).

rangeKeyType (string) --
The data type for the range key (also called the sort key), You can specify the following values:

STRING - The range key is a string.
NUMBER - The range key is number.

If you don\'t specify rangeKeyField , the default value is STRING .

rangeKeyField (string) --
The name of the range key (also called the sort key).

rangeKeyValue (string) --
The value of the range key (also called the sort key).

operation (string) --
The type of operation to perform. You can specify the following values:

INSERT - Insert data as a new item into the DynamoDB table. This item uses the specified hash key as a partition key. If you specified a range key, the item uses the range key as a sort key.
UPDATE - Update an existing item of the DynamoDB table with new data. This item\'s partition key must match the specified hash key. If you specified a range key, the range key must match the item\'s sort key.
DELETE - Delete an existing item of the DynamoDB table. This item\'s partition key must match the specified hash key. If you specified a range key, the range key must match the item\'s sort key.

If you don\'t specify this parameter, AWS IoT Events triggers the INSERT operation.

payloadField (string) --
The name of the DynamoDB column that receives the action payload.
If you don\'t specify this parameter, the name of the DynamoDB column is payload .

tableName (string) --
The name of the DynamoDB table.

payload (dict) --
Information needed to configure the payload.
By default, AWS IoT Events generates a standard payload in JSON for any action. This action payload contains all attribute-value pairs that have the information about the detector model instance and the event triggered the action. To configure the action payload, you can use contentExpression .

contentExpression (string) --
The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.

type (string) --
The value of the payload type can be either STRING or JSON .





dynamoDBv2 (dict) --
Writes to the DynamoDB table that you created. The default action payload contains all attribute-value pairs that have the information about the detector model instance and the event that triggered the action. You can also customize the payload . A separate column of the DynamoDB table receives one attribute-value pair in the payload that you specify. For more information, see Actions in AWS IoT Events Developer Guide .

tableName (string) --
The name of the DynamoDB table.

payload (dict) --
Information needed to configure the payload.
By default, AWS IoT Events generates a standard payload in JSON for any action. This action payload contains all attribute-value pairs that have the information about the detector model instance and the event triggered the action. To configure the action payload, you can use contentExpression .

contentExpression (string) --
The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.

type (string) --
The value of the payload type can be either STRING or JSON .





iotSiteWise (dict) --
Sends information about the detector model instance and the event that triggered the action to an asset property in AWS IoT SiteWise .

entryId (string) --
A unique identifier for this entry. You can use the entry ID to track which data entry causes an error in case of failure. The default is a new unique identifier. You can also specify an expression.

assetId (string) --
The ID of the asset that has the specified property. You can specify an expression.

propertyId (string) --
The ID of the asset property. You can specify an expression.

propertyAlias (string) --
The alias of the asset property. You can also specify an expression.

propertyValue (dict) --
The value to send to the asset property. This value contains timestamp, quality, and value (TQV) information.

value (dict) --
The value to send to an asset property.

stringValue (string) --
The asset property value is a string. You can also specify an expression. If you use an expression, the evaluated result should be a string.

integerValue (string) --
The asset property value is an integer. You can also specify an expression. If you use an expression, the evaluated result should be an integer.

doubleValue (string) --
The asset property value is a double. You can also specify an expression. If you use an expression, the evaluated result should be a double.

booleanValue (string) --
The asset property value is a Boolean value that must be TRUE or FALSE . You can also specify an expression. If you use an expression, the evaluated result should be a Boolean value.



timestamp (dict) --
The timestamp associated with the asset property value. The default is the current event time.

timeInSeconds (string) --
The timestamp, in seconds, in the Unix epoch format. The valid range is between 1-31556889864403199. You can also specify an expression.

offsetInNanos (string) --
The nanosecond offset converted from timeInSeconds . The valid range is between 0-999999999. You can also specify an expression.



quality (string) --
The quality of the asset property value. The value must be GOOD , BAD , or UNCERTAIN . You can also specify an expression.



















initialStateName (string) --
The state that is entered at the creation of each detector (instance).



detectorModelConfiguration (dict) --
Information about how the detector is configured.

detectorModelName (string) --
The name of the detector model.

detectorModelVersion (string) --
The version of the detector model.

detectorModelDescription (string) --
A brief description of the detector model.

detectorModelArn (string) --
The ARN of the detector model.

roleArn (string) --
The ARN of the role that grants permission to AWS IoT Events to perform its operations.

creationTime (datetime) --
The time the detector model was created.

lastUpdateTime (datetime) --
The time the detector model was last updated.

status (string) --
The status of the detector model.

key (string) --
The value used to identify a detector instance. When a device or system sends input, a new detector instance with a unique key value is created. AWS IoT Events can continue to route input to its corresponding detector instance based on this identifying information.
This parameter uses a JSON-path expression to select the attribute-value pair in the message payload that is used for identification. To route the message to the correct detector instance, the device must send a message payload that contains the same attribute-value.

evaluationMethod (string) --
Information about the order in which events are evaluated and how actions are executed.











Exceptions

IoTEvents.Client.exceptions.InvalidRequestException
IoTEvents.Client.exceptions.ResourceNotFoundException
IoTEvents.Client.exceptions.ThrottlingException
IoTEvents.Client.exceptions.InternalFailureException
IoTEvents.Client.exceptions.ServiceUnavailableException


    :return: {
        'detectorModel': {
            'detectorModelDefinition': {
                'states': [
                    {
                        'stateName': 'string',
                        'onInput': {
                            'events': [
                                {
                                    'eventName': 'string',
                                    'condition': 'string',
                                    'actions': [
                                        {
                                            'setVariable': {
                                                'variableName': 'string',
                                                'value': 'string'
                                            },
                                            'sns': {
                                                'targetArn': 'string',
                                                'payload': {
                                                    'contentExpression': 'string',
                                                    'type': 'STRING'|'JSON'
                                                }
                                            },
                                            'iotTopicPublish': {
                                                'mqttTopic': 'string',
                                                'payload': {
                                                    'contentExpression': 'string',
                                                    'type': 'STRING'|'JSON'
                                                }
                                            },
                                            'setTimer': {
                                                'timerName': 'string',
                                                'seconds': 123,
                                                'durationExpression': 'string'
                                            },
                                            'clearTimer': {
                                                'timerName': 'string'
                                            },
                                            'resetTimer': {
                                                'timerName': 'string'
                                            },
                                            'lambda': {
                                                'functionArn': 'string',
                                                'payload': {
                                                    'contentExpression': 'string',
                                                    'type': 'STRING'|'JSON'
                                                }
                                            },
                                            'iotEvents': {
                                                'inputName': 'string',
                                                'payload': {
                                                    'contentExpression': 'string',
                                                    'type': 'STRING'|'JSON'
                                                }
                                            },
                                            'sqs': {
                                                'queueUrl': 'string',
                                                'useBase64': True|False,
                                                'payload': {
                                                    'contentExpression': 'string',
                                                    'type': 'STRING'|'JSON'
                                                }
                                            },
                                            'firehose': {
                                                'deliveryStreamName': 'string',
                                                'separator': 'string',
                                                'payload': {
                                                    'contentExpression': 'string',
                                                    'type': 'STRING'|'JSON'
                                                }
                                            },
                                            'dynamoDB': {
                                                'hashKeyType': 'string',
                                                'hashKeyField': 'string',
                                                'hashKeyValue': 'string',
                                                'rangeKeyType': 'string',
                                                'rangeKeyField': 'string',
                                                'rangeKeyValue': 'string',
                                                'operation': 'string',
                                                'payloadField': 'string',
                                                'tableName': 'string',
                                                'payload': {
                                                    'contentExpression': 'string',
                                                    'type': 'STRING'|'JSON'
                                                }
                                            },
                                            'dynamoDBv2': {
                                                'tableName': 'string',
                                                'payload': {
                                                    'contentExpression': 'string',
                                                    'type': 'STRING'|'JSON'
                                                }
                                            },
                                            'iotSiteWise': {
                                                'entryId': 'string',
                                                'assetId': 'string',
                                                'propertyId': 'string',
                                                'propertyAlias': 'string',
                                                'propertyValue': {
                                                    'value': {
                                                        'stringValue': 'string',
                                                        'integerValue': 'string',
                                                        'doubleValue': 'string',
                                                        'booleanValue': 'string'
                                                    },
                                                    'timestamp': {
                                                        'timeInSeconds': 'string',
                                                        'offsetInNanos': 'string'
                                                    },
                                                    'quality': 'string'
                                                }
                                            }
                                        },
                                    ]
                                },
                            ],
                            'transitionEvents': [
                                {
                                    'eventName': 'string',
                                    'condition': 'string',
                                    'actions': [
                                        {
                                            'setVariable': {
                                                'variableName': 'string',
                                                'value': 'string'
                                            },
                                            'sns': {
                                                'targetArn': 'string',
                                                'payload': {
                                                    'contentExpression': 'string',
                                                    'type': 'STRING'|'JSON'
                                                }
                                            },
                                            'iotTopicPublish': {
                                                'mqttTopic': 'string',
                                                'payload': {
                                                    'contentExpression': 'string',
                                                    'type': 'STRING'|'JSON'
                                                }
                                            },
                                            'setTimer': {
                                                'timerName': 'string',
                                                'seconds': 123,
                                                'durationExpression': 'string'
                                            },
                                            'clearTimer': {
                                                'timerName': 'string'
                                            },
                                            'resetTimer': {
                                                'timerName': 'string'
                                            },
                                            'lambda': {
                                                'functionArn': 'string',
                                                'payload': {
                                                    'contentExpression': 'string',
                                                    'type': 'STRING'|'JSON'
                                                }
                                            },
                                            'iotEvents': {
                                                'inputName': 'string',
                                                'payload': {
                                                    'contentExpression': 'string',
                                                    'type': 'STRING'|'JSON'
                                                }
                                            },
                                            'sqs': {
                                                'queueUrl': 'string',
                                                'useBase64': True|False,
                                                'payload': {
                                                    'contentExpression': 'string',
                                                    'type': 'STRING'|'JSON'
                                                }
                                            },
                                            'firehose': {
                                                'deliveryStreamName': 'string',
                                                'separator': 'string',
                                                'payload': {
                                                    'contentExpression': 'string',
                                                    'type': 'STRING'|'JSON'
                                                }
                                            },
                                            'dynamoDB': {
                                                'hashKeyType': 'string',
                                                'hashKeyField': 'string',
                                                'hashKeyValue': 'string',
                                                'rangeKeyType': 'string',
                                                'rangeKeyField': 'string',
                                                'rangeKeyValue': 'string',
                                                'operation': 'string',
                                                'payloadField': 'string',
                                                'tableName': 'string',
                                                'payload': {
                                                    'contentExpression': 'string',
                                                    'type': 'STRING'|'JSON'
                                                }
                                            },
                                            'dynamoDBv2': {
                                                'tableName': 'string',
                                                'payload': {
                                                    'contentExpression': 'string',
                                                    'type': 'STRING'|'JSON'
                                                }
                                            },
                                            'iotSiteWise': {
                                                'entryId': 'string',
                                                'assetId': 'string',
                                                'propertyId': 'string',
                                                'propertyAlias': 'string',
                                                'propertyValue': {
                                                    'value': {
                                                        'stringValue': 'string',
                                                        'integerValue': 'string',
                                                        'doubleValue': 'string',
                                                        'booleanValue': 'string'
                                                    },
                                                    'timestamp': {
                                                        'timeInSeconds': 'string',
                                                        'offsetInNanos': 'string'
                                                    },
                                                    'quality': 'string'
                                                }
                                            }
                                        },
                                    ],
                                    'nextState': 'string'
                                },
                            ]
                        },
                        'onEnter': {
                            'events': [
                                {
                                    'eventName': 'string',
                                    'condition': 'string',
                                    'actions': [
                                        {
                                            'setVariable': {
                                                'variableName': 'string',
                                                'value': 'string'
                                            },
                                            'sns': {
                                                'targetArn': 'string',
                                                'payload': {
                                                    'contentExpression': 'string',
                                                    'type': 'STRING'|'JSON'
                                                }
                                            },
                                            'iotTopicPublish': {
                                                'mqttTopic': 'string',
                                                'payload': {
                                                    'contentExpression': 'string',
                                                    'type': 'STRING'|'JSON'
                                                }
                                            },
                                            'setTimer': {
                                                'timerName': 'string',
                                                'seconds': 123,
                                                'durationExpression': 'string'
                                            },
                                            'clearTimer': {
                                                'timerName': 'string'
                                            },
                                            'resetTimer': {
                                                'timerName': 'string'
                                            },
                                            'lambda': {
                                                'functionArn': 'string',
                                                'payload': {
                                                    'contentExpression': 'string',
                                                    'type': 'STRING'|'JSON'
                                                }
                                            },
                                            'iotEvents': {
                                                'inputName': 'string',
                                                'payload': {
                                                    'contentExpression': 'string',
                                                    'type': 'STRING'|'JSON'
                                                }
                                            },
                                            'sqs': {
                                                'queueUrl': 'string',
                                                'useBase64': True|False,
                                                'payload': {
                                                    'contentExpression': 'string',
                                                    'type': 'STRING'|'JSON'
                                                }
                                            },
                                            'firehose': {
                                                'deliveryStreamName': 'string',
                                                'separator': 'string',
                                                'payload': {
                                                    'contentExpression': 'string',
                                                    'type': 'STRING'|'JSON'
                                                }
                                            },
                                            'dynamoDB': {
                                                'hashKeyType': 'string',
                                                'hashKeyField': 'string',
                                                'hashKeyValue': 'string',
                                                'rangeKeyType': 'string',
                                                'rangeKeyField': 'string',
                                                'rangeKeyValue': 'string',
                                                'operation': 'string',
                                                'payloadField': 'string',
                                                'tableName': 'string',
                                                'payload': {
                                                    'contentExpression': 'string',
                                                    'type': 'STRING'|'JSON'
                                                }
                                            },
                                            'dynamoDBv2': {
                                                'tableName': 'string',
                                                'payload': {
                                                    'contentExpression': 'string',
                                                    'type': 'STRING'|'JSON'
                                                }
                                            },
                                            'iotSiteWise': {
                                                'entryId': 'string',
                                                'assetId': 'string',
                                                'propertyId': 'string',
                                                'propertyAlias': 'string',
                                                'propertyValue': {
                                                    'value': {
                                                        'stringValue': 'string',
                                                        'integerValue': 'string',
                                                        'doubleValue': 'string',
                                                        'booleanValue': 'string'
                                                    },
                                                    'timestamp': {
                                                        'timeInSeconds': 'string',
                                                        'offsetInNanos': 'string'
                                                    },
                                                    'quality': 'string'
                                                }
                                            }
                                        },
                                    ]
                                },
                            ]
                        },
                        'onExit': {
                            'events': [
                                {
                                    'eventName': 'string',
                                    'condition': 'string',
                                    'actions': [
                                        {
                                            'setVariable': {
                                                'variableName': 'string',
                                                'value': 'string'
                                            },
                                            'sns': {
                                                'targetArn': 'string',
                                                'payload': {
                                                    'contentExpression': 'string',
                                                    'type': 'STRING'|'JSON'
                                                }
                                            },
                                            'iotTopicPublish': {
                                                'mqttTopic': 'string',
                                                'payload': {
                                                    'contentExpression': 'string',
                                                    'type': 'STRING'|'JSON'
                                                }
                                            },
                                            'setTimer': {
                                                'timerName': 'string',
                                                'seconds': 123,
                                                'durationExpression': 'string'
                                            },
                                            'clearTimer': {
                                                'timerName': 'string'
                                            },
                                            'resetTimer': {
                                                'timerName': 'string'
                                            },
                                            'lambda': {
                                                'functionArn': 'string',
                                                'payload': {
                                                    'contentExpression': 'string',
                                                    'type': 'STRING'|'JSON'
                                                }
                                            },
                                            'iotEvents': {
                                                'inputName': 'string',
                                                'payload': {
                                                    'contentExpression': 'string',
                                                    'type': 'STRING'|'JSON'
                                                }
                                            },
                                            'sqs': {
                                                'queueUrl': 'string',
                                                'useBase64': True|False,
                                                'payload': {
                                                    'contentExpression': 'string',
                                                    'type': 'STRING'|'JSON'
                                                }
                                            },
                                            'firehose': {
                                                'deliveryStreamName': 'string',
                                                'separator': 'string',
                                                'payload': {
                                                    'contentExpression': 'string',
                                                    'type': 'STRING'|'JSON'
                                                }
                                            },
                                            'dynamoDB': {
                                                'hashKeyType': 'string',
                                                'hashKeyField': 'string',
                                                'hashKeyValue': 'string',
                                                'rangeKeyType': 'string',
                                                'rangeKeyField': 'string',
                                                'rangeKeyValue': 'string',
                                                'operation': 'string',
                                                'payloadField': 'string',
                                                'tableName': 'string',
                                                'payload': {
                                                    'contentExpression': 'string',
                                                    'type': 'STRING'|'JSON'
                                                }
                                            },
                                            'dynamoDBv2': {
                                                'tableName': 'string',
                                                'payload': {
                                                    'contentExpression': 'string',
                                                    'type': 'STRING'|'JSON'
                                                }
                                            },
                                            'iotSiteWise': {
                                                'entryId': 'string',
                                                'assetId': 'string',
                                                'propertyId': 'string',
                                                'propertyAlias': 'string',
                                                'propertyValue': {
                                                    'value': {
                                                        'stringValue': 'string',
                                                        'integerValue': 'string',
                                                        'doubleValue': 'string',
                                                        'booleanValue': 'string'
                                                    },
                                                    'timestamp': {
                                                        'timeInSeconds': 'string',
                                                        'offsetInNanos': 'string'
                                                    },
                                                    'quality': 'string'
                                                }
                                            }
                                        },
                                    ]
                                },
                            ]
                        }
                    },
                ],
                'initialStateName': 'string'
            },
            'detectorModelConfiguration': {
                'detectorModelName': 'string',
                'detectorModelVersion': 'string',
                'detectorModelDescription': 'string',
                'detectorModelArn': 'string',
                'roleArn': 'string',
                'creationTime': datetime(2015, 1, 1),
                'lastUpdateTime': datetime(2015, 1, 1),
                'status': 'ACTIVE'|'ACTIVATING'|'INACTIVE'|'DEPRECATED'|'DRAFT'|'PAUSED'|'FAILED',
                'key': 'string',
                'evaluationMethod': 'BATCH'|'SERIAL'
            }
        }
    }
    
    
    :returns: 
    STRING - The hash key is a string.
    NUMBER - The hash key is a number.
    
    """
    pass

def describe_input(inputName=None):
    """
    Describes an input.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_input(
        inputName='string'
    )
    
    
    :type inputName: string
    :param inputName: [REQUIRED]\nThe name of the input.\n

    :rtype: dict
ReturnsResponse Syntax{
    'input': {
        'inputConfiguration': {
            'inputName': 'string',
            'inputDescription': 'string',
            'inputArn': 'string',
            'creationTime': datetime(2015, 1, 1),
            'lastUpdateTime': datetime(2015, 1, 1),
            'status': 'CREATING'|'UPDATING'|'ACTIVE'|'DELETING'
        },
        'inputDefinition': {
            'attributes': [
                {
                    'jsonPath': 'string'
                },
            ]
        }
    }
}


Response Structure

(dict) --
input (dict) --Information about the input.

inputConfiguration (dict) --Information about the configuration of an input.

inputName (string) --The name of the input.

inputDescription (string) --A brief description of the input.

inputArn (string) --The ARN of the input.

creationTime (datetime) --The time the input was created.

lastUpdateTime (datetime) --The last time the input was updated.

status (string) --The status of the input.



inputDefinition (dict) --The definition of the input.

attributes (list) --The attributes from the JSON payload that are made available by the input. Inputs are derived from messages sent to the AWS IoT Events system using BatchPutMessage . Each such message contains a JSON payload, and those attributes (and their paired values) specified here are available for use in the condition expressions used by detectors that monitor this input.

(dict) --The attributes from the JSON payload that are made available by the input. Inputs are derived from messages sent to the AWS IoT Events system using BatchPutMessage . Each such message contains a JSON payload. Those attributes (and their paired values) specified here are available for use in the condition expressions used by detectors.

jsonPath (string) --An expression that specifies an attribute-value pair in a JSON structure. Use this to specify an attribute from the JSON payload that is made available by the input. Inputs are derived from messages sent to AWS IoT Events (BatchPutMessage ). Each such message contains a JSON payload. The attribute (and its paired value) specified here are available for use in the condition expressions used by detectors.
Syntax: <field-name>.<field-name>...














Exceptions

IoTEvents.Client.exceptions.InvalidRequestException
IoTEvents.Client.exceptions.ResourceNotFoundException
IoTEvents.Client.exceptions.ThrottlingException
IoTEvents.Client.exceptions.InternalFailureException
IoTEvents.Client.exceptions.ServiceUnavailableException


    :return: {
        'input': {
            'inputConfiguration': {
                'inputName': 'string',
                'inputDescription': 'string',
                'inputArn': 'string',
                'creationTime': datetime(2015, 1, 1),
                'lastUpdateTime': datetime(2015, 1, 1),
                'status': 'CREATING'|'UPDATING'|'ACTIVE'|'DELETING'
            },
            'inputDefinition': {
                'attributes': [
                    {
                        'jsonPath': 'string'
                    },
                ]
            }
        }
    }
    
    
    """
    pass

def describe_logging_options():
    """
    Retrieves the current settings of the AWS IoT Events logging options.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_logging_options()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'loggingOptions': {
        'roleArn': 'string',
        'level': 'ERROR'|'INFO'|'DEBUG',
        'enabled': True|False,
        'detectorDebugOptions': [
            {
                'detectorModelName': 'string',
                'keyValue': 'string'
            },
        ]
    }
}


Response Structure

(dict) --
loggingOptions (dict) --The current settings of the AWS IoT Events logging options.

roleArn (string) --The ARN of the role that grants permission to AWS IoT Events to perform logging.

level (string) --The logging level.

enabled (boolean) --If TRUE, logging is enabled for AWS IoT Events.

detectorDebugOptions (list) --Information that identifies those detector models and their detectors (instances) for which the logging level is given.

(dict) --The detector model and the specific detectors (instances) for which the logging level is given.

detectorModelName (string) --The name of the detector model.

keyValue (string) --The value of the input attribute key used to create the detector (the instance of the detector model).












Exceptions

IoTEvents.Client.exceptions.InvalidRequestException
IoTEvents.Client.exceptions.ThrottlingException
IoTEvents.Client.exceptions.InternalFailureException
IoTEvents.Client.exceptions.ResourceNotFoundException
IoTEvents.Client.exceptions.ServiceUnavailableException
IoTEvents.Client.exceptions.UnsupportedOperationException


    :return: {
        'loggingOptions': {
            'roleArn': 'string',
            'level': 'ERROR'|'INFO'|'DEBUG',
            'enabled': True|False,
            'detectorDebugOptions': [
                {
                    'detectorModelName': 'string',
                    'keyValue': 'string'
                },
            ]
        }
    }
    
    
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

def list_detector_model_versions(detectorModelName=None, nextToken=None, maxResults=None):
    """
    Lists all the versions of a detector model. Only the metadata associated with each detector model version is returned.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_detector_model_versions(
        detectorModelName='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type detectorModelName: string
    :param detectorModelName: [REQUIRED]\nThe name of the detector model whose versions are returned.\n

    :type nextToken: string
    :param nextToken: The token for the next set of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return at one time.

    :rtype: dict

ReturnsResponse Syntax
{
    'detectorModelVersionSummaries': [
        {
            'detectorModelName': 'string',
            'detectorModelVersion': 'string',
            'detectorModelArn': 'string',
            'roleArn': 'string',
            'creationTime': datetime(2015, 1, 1),
            'lastUpdateTime': datetime(2015, 1, 1),
            'status': 'ACTIVE'|'ACTIVATING'|'INACTIVE'|'DEPRECATED'|'DRAFT'|'PAUSED'|'FAILED',
            'evaluationMethod': 'BATCH'|'SERIAL'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

detectorModelVersionSummaries (list) --
Summary information about the detector model versions.

(dict) --
Information about the detector model version.

detectorModelName (string) --
The name of the detector model.

detectorModelVersion (string) --
The ID of the detector model version.

detectorModelArn (string) --
The ARN of the detector model version.

roleArn (string) --
The ARN of the role that grants the detector model permission to perform its tasks.

creationTime (datetime) --
The time the detector model version was created.

lastUpdateTime (datetime) --
The last time the detector model version was updated.

status (string) --
The status of the detector model version.

evaluationMethod (string) --
Information about the order in which events are evaluated and how actions are executed.





nextToken (string) --
A token to retrieve the next set of results, or null if there are no additional results.







Exceptions

IoTEvents.Client.exceptions.InvalidRequestException
IoTEvents.Client.exceptions.ResourceNotFoundException
IoTEvents.Client.exceptions.ThrottlingException
IoTEvents.Client.exceptions.InternalFailureException
IoTEvents.Client.exceptions.ServiceUnavailableException


    :return: {
        'detectorModelVersionSummaries': [
            {
                'detectorModelName': 'string',
                'detectorModelVersion': 'string',
                'detectorModelArn': 'string',
                'roleArn': 'string',
                'creationTime': datetime(2015, 1, 1),
                'lastUpdateTime': datetime(2015, 1, 1),
                'status': 'ACTIVE'|'ACTIVATING'|'INACTIVE'|'DEPRECATED'|'DRAFT'|'PAUSED'|'FAILED',
                'evaluationMethod': 'BATCH'|'SERIAL'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    IoTEvents.Client.exceptions.InvalidRequestException
    IoTEvents.Client.exceptions.ResourceNotFoundException
    IoTEvents.Client.exceptions.ThrottlingException
    IoTEvents.Client.exceptions.InternalFailureException
    IoTEvents.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def list_detector_models(nextToken=None, maxResults=None):
    """
    Lists the detector models you have created. Only the metadata associated with each detector model is returned.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_detector_models(
        nextToken='string',
        maxResults=123
    )
    
    
    :type nextToken: string
    :param nextToken: The token for the next set of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return at one time.

    :rtype: dict

ReturnsResponse Syntax
{
    'detectorModelSummaries': [
        {
            'detectorModelName': 'string',
            'detectorModelDescription': 'string',
            'creationTime': datetime(2015, 1, 1)
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

detectorModelSummaries (list) --
Summary information about the detector models.

(dict) --
Information about the detector model.

detectorModelName (string) --
The name of the detector model.

detectorModelDescription (string) --
A brief description of the detector model.

creationTime (datetime) --
The time the detector model was created.





nextToken (string) --
A token to retrieve the next set of results, or null if there are no additional results.







Exceptions

IoTEvents.Client.exceptions.InvalidRequestException
IoTEvents.Client.exceptions.ThrottlingException
IoTEvents.Client.exceptions.InternalFailureException
IoTEvents.Client.exceptions.ServiceUnavailableException


    :return: {
        'detectorModelSummaries': [
            {
                'detectorModelName': 'string',
                'detectorModelDescription': 'string',
                'creationTime': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    IoTEvents.Client.exceptions.InvalidRequestException
    IoTEvents.Client.exceptions.ThrottlingException
    IoTEvents.Client.exceptions.InternalFailureException
    IoTEvents.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def list_inputs(nextToken=None, maxResults=None):
    """
    Lists the inputs you have created.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_inputs(
        nextToken='string',
        maxResults=123
    )
    
    
    :type nextToken: string
    :param nextToken: The token for the next set of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return at one time.

    :rtype: dict

ReturnsResponse Syntax
{
    'inputSummaries': [
        {
            'inputName': 'string',
            'inputDescription': 'string',
            'inputArn': 'string',
            'creationTime': datetime(2015, 1, 1),
            'lastUpdateTime': datetime(2015, 1, 1),
            'status': 'CREATING'|'UPDATING'|'ACTIVE'|'DELETING'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

inputSummaries (list) --
Summary information about the inputs.

(dict) --
Information about the input.

inputName (string) --
The name of the input.

inputDescription (string) --
A brief description of the input.

inputArn (string) --
The ARN of the input.

creationTime (datetime) --
The time the input was created.

lastUpdateTime (datetime) --
The last time the input was updated.

status (string) --
The status of the input.





nextToken (string) --
A token to retrieve the next set of results, or null if there are no additional results.







Exceptions

IoTEvents.Client.exceptions.InvalidRequestException
IoTEvents.Client.exceptions.ThrottlingException
IoTEvents.Client.exceptions.InternalFailureException
IoTEvents.Client.exceptions.ServiceUnavailableException


    :return: {
        'inputSummaries': [
            {
                'inputName': 'string',
                'inputDescription': 'string',
                'inputArn': 'string',
                'creationTime': datetime(2015, 1, 1),
                'lastUpdateTime': datetime(2015, 1, 1),
                'status': 'CREATING'|'UPDATING'|'ACTIVE'|'DELETING'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    IoTEvents.Client.exceptions.InvalidRequestException
    IoTEvents.Client.exceptions.ThrottlingException
    IoTEvents.Client.exceptions.InternalFailureException
    IoTEvents.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def list_tags_for_resource(resourceArn=None):
    """
    Lists the tags (metadata) you have assigned to the resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        resourceArn='string'
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe ARN of the resource.\n

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
tags (list) --The list of tags assigned to the resource.

(dict) --Metadata that can be used to manage the resource.

key (string) --The tag\'s key.

value (string) --The tag\'s value.










Exceptions

IoTEvents.Client.exceptions.InvalidRequestException
IoTEvents.Client.exceptions.ResourceNotFoundException
IoTEvents.Client.exceptions.ResourceInUseException
IoTEvents.Client.exceptions.ThrottlingException
IoTEvents.Client.exceptions.InternalFailureException


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

def put_logging_options(loggingOptions=None):
    """
    Sets or updates the AWS IoT Events logging options.
    If you update the value of any loggingOptions field, it takes up to one minute for the change to take effect. If you change the policy attached to the role you specified in the roleArn field (for example, to correct an invalid policy), it takes up to five minutes for that change to take effect.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_logging_options(
        loggingOptions={
            'roleArn': 'string',
            'level': 'ERROR'|'INFO'|'DEBUG',
            'enabled': True|False,
            'detectorDebugOptions': [
                {
                    'detectorModelName': 'string',
                    'keyValue': 'string'
                },
            ]
        }
    )
    
    
    :type loggingOptions: dict
    :param loggingOptions: [REQUIRED]\nThe new values of the AWS IoT Events logging options.\n\nroleArn (string) -- [REQUIRED]The ARN of the role that grants permission to AWS IoT Events to perform logging.\n\nlevel (string) -- [REQUIRED]The logging level.\n\nenabled (boolean) -- [REQUIRED]If TRUE, logging is enabled for AWS IoT Events.\n\ndetectorDebugOptions (list) --Information that identifies those detector models and their detectors (instances) for which the logging level is given.\n\n(dict) --The detector model and the specific detectors (instances) for which the logging level is given.\n\ndetectorModelName (string) -- [REQUIRED]The name of the detector model.\n\nkeyValue (string) --The value of the input attribute key used to create the detector (the instance of the detector model).\n\n\n\n\n\n\n

    """
    pass

def tag_resource(resourceArn=None, tags=None):
    """
    Adds to or modifies the tags of the given resource. Tags are metadata that can be used to manage a resource.
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
    :param resourceArn: [REQUIRED]\nThe ARN of the resource.\n

    :type tags: list
    :param tags: [REQUIRED]\nThe new or modified tags for the resource.\n\n(dict) --Metadata that can be used to manage the resource.\n\nkey (string) -- [REQUIRED]The tag\'s key.\n\nvalue (string) -- [REQUIRED]The tag\'s value.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

IoTEvents.Client.exceptions.InvalidRequestException
IoTEvents.Client.exceptions.ResourceNotFoundException
IoTEvents.Client.exceptions.ResourceInUseException
IoTEvents.Client.exceptions.ThrottlingException
IoTEvents.Client.exceptions.LimitExceededException
IoTEvents.Client.exceptions.InternalFailureException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_resource(resourceArn=None, tagKeys=None):
    """
    Removes the given tags (metadata) from the resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        resourceArn='string',
        tagKeys=[
            'string',
        ]
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe ARN of the resource.\n

    :type tagKeys: list
    :param tagKeys: [REQUIRED]\nA list of the keys of the tags to be removed from the resource.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

IoTEvents.Client.exceptions.InvalidRequestException
IoTEvents.Client.exceptions.ResourceNotFoundException
IoTEvents.Client.exceptions.ResourceInUseException
IoTEvents.Client.exceptions.ThrottlingException
IoTEvents.Client.exceptions.InternalFailureException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_detector_model(detectorModelName=None, detectorModelDefinition=None, detectorModelDescription=None, roleArn=None, evaluationMethod=None):
    """
    Updates a detector model. Detectors (instances) spawned by the previous version are deleted and then re-created as new inputs arrive.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_detector_model(
        detectorModelName='string',
        detectorModelDefinition={
            'states': [
                {
                    'stateName': 'string',
                    'onInput': {
                        'events': [
                            {
                                'eventName': 'string',
                                'condition': 'string',
                                'actions': [
                                    {
                                        'setVariable': {
                                            'variableName': 'string',
                                            'value': 'string'
                                        },
                                        'sns': {
                                            'targetArn': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'iotTopicPublish': {
                                            'mqttTopic': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'setTimer': {
                                            'timerName': 'string',
                                            'seconds': 123,
                                            'durationExpression': 'string'
                                        },
                                        'clearTimer': {
                                            'timerName': 'string'
                                        },
                                        'resetTimer': {
                                            'timerName': 'string'
                                        },
                                        'lambda': {
                                            'functionArn': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'iotEvents': {
                                            'inputName': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'sqs': {
                                            'queueUrl': 'string',
                                            'useBase64': True|False,
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'firehose': {
                                            'deliveryStreamName': 'string',
                                            'separator': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'dynamoDB': {
                                            'hashKeyType': 'string',
                                            'hashKeyField': 'string',
                                            'hashKeyValue': 'string',
                                            'rangeKeyType': 'string',
                                            'rangeKeyField': 'string',
                                            'rangeKeyValue': 'string',
                                            'operation': 'string',
                                            'payloadField': 'string',
                                            'tableName': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'dynamoDBv2': {
                                            'tableName': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'iotSiteWise': {
                                            'entryId': 'string',
                                            'assetId': 'string',
                                            'propertyId': 'string',
                                            'propertyAlias': 'string',
                                            'propertyValue': {
                                                'value': {
                                                    'stringValue': 'string',
                                                    'integerValue': 'string',
                                                    'doubleValue': 'string',
                                                    'booleanValue': 'string'
                                                },
                                                'timestamp': {
                                                    'timeInSeconds': 'string',
                                                    'offsetInNanos': 'string'
                                                },
                                                'quality': 'string'
                                            }
                                        }
                                    },
                                ]
                            },
                        ],
                        'transitionEvents': [
                            {
                                'eventName': 'string',
                                'condition': 'string',
                                'actions': [
                                    {
                                        'setVariable': {
                                            'variableName': 'string',
                                            'value': 'string'
                                        },
                                        'sns': {
                                            'targetArn': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'iotTopicPublish': {
                                            'mqttTopic': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'setTimer': {
                                            'timerName': 'string',
                                            'seconds': 123,
                                            'durationExpression': 'string'
                                        },
                                        'clearTimer': {
                                            'timerName': 'string'
                                        },
                                        'resetTimer': {
                                            'timerName': 'string'
                                        },
                                        'lambda': {
                                            'functionArn': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'iotEvents': {
                                            'inputName': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'sqs': {
                                            'queueUrl': 'string',
                                            'useBase64': True|False,
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'firehose': {
                                            'deliveryStreamName': 'string',
                                            'separator': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'dynamoDB': {
                                            'hashKeyType': 'string',
                                            'hashKeyField': 'string',
                                            'hashKeyValue': 'string',
                                            'rangeKeyType': 'string',
                                            'rangeKeyField': 'string',
                                            'rangeKeyValue': 'string',
                                            'operation': 'string',
                                            'payloadField': 'string',
                                            'tableName': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'dynamoDBv2': {
                                            'tableName': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'iotSiteWise': {
                                            'entryId': 'string',
                                            'assetId': 'string',
                                            'propertyId': 'string',
                                            'propertyAlias': 'string',
                                            'propertyValue': {
                                                'value': {
                                                    'stringValue': 'string',
                                                    'integerValue': 'string',
                                                    'doubleValue': 'string',
                                                    'booleanValue': 'string'
                                                },
                                                'timestamp': {
                                                    'timeInSeconds': 'string',
                                                    'offsetInNanos': 'string'
                                                },
                                                'quality': 'string'
                                            }
                                        }
                                    },
                                ],
                                'nextState': 'string'
                            },
                        ]
                    },
                    'onEnter': {
                        'events': [
                            {
                                'eventName': 'string',
                                'condition': 'string',
                                'actions': [
                                    {
                                        'setVariable': {
                                            'variableName': 'string',
                                            'value': 'string'
                                        },
                                        'sns': {
                                            'targetArn': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'iotTopicPublish': {
                                            'mqttTopic': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'setTimer': {
                                            'timerName': 'string',
                                            'seconds': 123,
                                            'durationExpression': 'string'
                                        },
                                        'clearTimer': {
                                            'timerName': 'string'
                                        },
                                        'resetTimer': {
                                            'timerName': 'string'
                                        },
                                        'lambda': {
                                            'functionArn': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'iotEvents': {
                                            'inputName': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'sqs': {
                                            'queueUrl': 'string',
                                            'useBase64': True|False,
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'firehose': {
                                            'deliveryStreamName': 'string',
                                            'separator': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'dynamoDB': {
                                            'hashKeyType': 'string',
                                            'hashKeyField': 'string',
                                            'hashKeyValue': 'string',
                                            'rangeKeyType': 'string',
                                            'rangeKeyField': 'string',
                                            'rangeKeyValue': 'string',
                                            'operation': 'string',
                                            'payloadField': 'string',
                                            'tableName': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'dynamoDBv2': {
                                            'tableName': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'iotSiteWise': {
                                            'entryId': 'string',
                                            'assetId': 'string',
                                            'propertyId': 'string',
                                            'propertyAlias': 'string',
                                            'propertyValue': {
                                                'value': {
                                                    'stringValue': 'string',
                                                    'integerValue': 'string',
                                                    'doubleValue': 'string',
                                                    'booleanValue': 'string'
                                                },
                                                'timestamp': {
                                                    'timeInSeconds': 'string',
                                                    'offsetInNanos': 'string'
                                                },
                                                'quality': 'string'
                                            }
                                        }
                                    },
                                ]
                            },
                        ]
                    },
                    'onExit': {
                        'events': [
                            {
                                'eventName': 'string',
                                'condition': 'string',
                                'actions': [
                                    {
                                        'setVariable': {
                                            'variableName': 'string',
                                            'value': 'string'
                                        },
                                        'sns': {
                                            'targetArn': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'iotTopicPublish': {
                                            'mqttTopic': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'setTimer': {
                                            'timerName': 'string',
                                            'seconds': 123,
                                            'durationExpression': 'string'
                                        },
                                        'clearTimer': {
                                            'timerName': 'string'
                                        },
                                        'resetTimer': {
                                            'timerName': 'string'
                                        },
                                        'lambda': {
                                            'functionArn': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'iotEvents': {
                                            'inputName': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'sqs': {
                                            'queueUrl': 'string',
                                            'useBase64': True|False,
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'firehose': {
                                            'deliveryStreamName': 'string',
                                            'separator': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'dynamoDB': {
                                            'hashKeyType': 'string',
                                            'hashKeyField': 'string',
                                            'hashKeyValue': 'string',
                                            'rangeKeyType': 'string',
                                            'rangeKeyField': 'string',
                                            'rangeKeyValue': 'string',
                                            'operation': 'string',
                                            'payloadField': 'string',
                                            'tableName': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'dynamoDBv2': {
                                            'tableName': 'string',
                                            'payload': {
                                                'contentExpression': 'string',
                                                'type': 'STRING'|'JSON'
                                            }
                                        },
                                        'iotSiteWise': {
                                            'entryId': 'string',
                                            'assetId': 'string',
                                            'propertyId': 'string',
                                            'propertyAlias': 'string',
                                            'propertyValue': {
                                                'value': {
                                                    'stringValue': 'string',
                                                    'integerValue': 'string',
                                                    'doubleValue': 'string',
                                                    'booleanValue': 'string'
                                                },
                                                'timestamp': {
                                                    'timeInSeconds': 'string',
                                                    'offsetInNanos': 'string'
                                                },
                                                'quality': 'string'
                                            }
                                        }
                                    },
                                ]
                            },
                        ]
                    }
                },
            ],
            'initialStateName': 'string'
        },
        detectorModelDescription='string',
        roleArn='string',
        evaluationMethod='BATCH'|'SERIAL'
    )
    
    
    :type detectorModelName: string
    :param detectorModelName: [REQUIRED]\nThe name of the detector model that is updated.\n

    :type detectorModelDefinition: dict
    :param detectorModelDefinition: [REQUIRED]\nInformation that defines how a detector operates.\n\nstates (list) -- [REQUIRED]Information about the states of the detector.\n\n(dict) --Information that defines a state of a detector.\n\nstateName (string) -- [REQUIRED]The name of the state.\n\nonInput (dict) --When an input is received and the condition is TRUE, perform the specified actions .\n\nevents (list) --Specifies the actions performed when the condition evaluates to TRUE.\n\n(dict) --Specifies the actions to be performed when the condition evaluates to TRUE.\n\neventName (string) -- [REQUIRED]The name of the event.\n\ncondition (string) --Optional. The Boolean expression that, when TRUE, causes the actions to be performed. If not present, the actions are performed (=TRUE). If the expression result is not a Boolean value, the actions are not performed (=FALSE).\n\nactions (list) --The actions to be performed.\n\n(dict) --An action to be performed when the condition is TRUE.\n\nsetVariable (dict) --Sets a variable to a specified value.\n\nvariableName (string) -- [REQUIRED]The name of the variable.\n\nvalue (string) -- [REQUIRED]The new value of the variable.\n\n\n\nsns (dict) --Sends an Amazon SNS message.\n\ntargetArn (string) -- [REQUIRED]The ARN of the Amazon SNS target where the message is sent.\n\npayload (dict) --You can configure the action payload when you send a message as an Amazon SNS push notification.\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\niotTopicPublish (dict) --Publishes an MQTT message with the given topic to the AWS IoT message broker.\n\nmqttTopic (string) -- [REQUIRED]The MQTT topic of the message. You can use a string expression that includes variables ($variable.<variable-name> ) and input values ($input.<input-name>.<path-to-datum> ) as the topic string.\n\npayload (dict) --You can configure the action payload when you publish a message to an AWS IoT Core topic.\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\nsetTimer (dict) --Information needed to set the timer.\n\ntimerName (string) -- [REQUIRED]The name of the timer.\n\nseconds (integer) --The number of seconds until the timer expires. The minimum value is 60 seconds to ensure accuracy. The maximum value is 31622400 seconds.\n\ndurationExpression (string) --The duration of the timer, in seconds. You can use a string expression that includes numbers, variables ($variable.<variable-name> ), and input values ($input.<input-name>.<path-to-datum> ) as the duration. The range of the duration is 1-31622400 seconds. To ensure accuracy, the minimum duration is 60 seconds. The evaluated result of the duration is rounded down to the nearest whole number.\n\n\n\nclearTimer (dict) --Information needed to clear the timer.\n\ntimerName (string) -- [REQUIRED]The name of the timer to clear.\n\n\n\nresetTimer (dict) --Information needed to reset the timer.\n\ntimerName (string) -- [REQUIRED]The name of the timer to reset.\n\n\n\nlambda (dict) --Calls a Lambda function, passing in information about the detector model instance and the event that triggered the action.\n\nfunctionArn (string) -- [REQUIRED]The ARN of the Lambda function that is executed.\n\npayload (dict) --You can configure the action payload when you send a message to a Lambda function.\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\niotEvents (dict) --Sends AWS IoT Events input, which passes information about the detector model instance and the event that triggered the action.\n\ninputName (string) -- [REQUIRED]The name of the AWS IoT Events input where the data is sent.\n\npayload (dict) --You can configure the action payload when you send a message to an AWS IoT Events input.\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\nsqs (dict) --Sends information about the detector model instance and the event that triggered the action to an Amazon SQS queue.\n\nqueueUrl (string) -- [REQUIRED]The URL of the SQS queue where the data is written.\n\nuseBase64 (boolean) --Set this to TRUE if you want the data to be base-64 encoded before it is written to the queue. Otherwise, set this to FALSE.\n\npayload (dict) --You can configure the action payload when you send a message to an Amazon SQS queue.\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\nfirehose (dict) --Sends information about the detector model instance and the event that triggered the action to an Amazon Kinesis Data Firehose delivery stream.\n\ndeliveryStreamName (string) -- [REQUIRED]The name of the Kinesis Data Firehose delivery stream where the data is written.\n\nseparator (string) --A character separator that is used to separate records written to the Kinesis Data Firehose delivery stream. Valid values are: \'n\' (newline), \'t\' (tab), \'rn\' (Windows newline), \',\' (comma).\n\npayload (dict) --You can configure the action payload when you send a message to an Amazon Kinesis Data Firehose delivery stream.\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\ndynamoDB (dict) --Writes to the DynamoDB table that you created. The default action payload contains all attribute-value pairs that have the information about the detector model instance and the event that triggered the action. You can also customize the payload . One column of the DynamoDB table receives all attribute-value pairs in the payload that you specify. For more information, see Actions in AWS IoT Events Developer Guide .\n\nhashKeyType (string) --The data type for the hash key (also called the partition key). You can specify the following values:\n\nSTRING - The hash key is a string.\nNUMBER - The hash key is a number.\n\nIf you don\'t specify hashKeyType , the default value is STRING .\n\nhashKeyField (string) -- [REQUIRED]The name of the hash key (also called the partition key).\n\nhashKeyValue (string) -- [REQUIRED]The value of the hash key (also called the partition key).\n\nrangeKeyType (string) --The data type for the range key (also called the sort key), You can specify the following values:\n\nSTRING - The range key is a string.\nNUMBER - The range key is number.\n\nIf you don\'t specify rangeKeyField , the default value is STRING .\n\nrangeKeyField (string) --The name of the range key (also called the sort key).\n\nrangeKeyValue (string) --The value of the range key (also called the sort key).\n\noperation (string) --The type of operation to perform. You can specify the following values:\n\nINSERT - Insert data as a new item into the DynamoDB table. This item uses the specified hash key as a partition key. If you specified a range key, the item uses the range key as a sort key.\nUPDATE - Update an existing item of the DynamoDB table with new data. This item\'s partition key must match the specified hash key. If you specified a range key, the range key must match the item\'s sort key.\nDELETE - Delete an existing item of the DynamoDB table. This item\'s partition key must match the specified hash key. If you specified a range key, the range key must match the item\'s sort key.\n\nIf you don\'t specify this parameter, AWS IoT Events triggers the INSERT operation.\n\npayloadField (string) --The name of the DynamoDB column that receives the action payload.\nIf you don\'t specify this parameter, the name of the DynamoDB column is payload .\n\ntableName (string) -- [REQUIRED]The name of the DynamoDB table.\n\npayload (dict) --Information needed to configure the payload.\nBy default, AWS IoT Events generates a standard payload in JSON for any action. This action payload contains all attribute-value pairs that have the information about the detector model instance and the event triggered the action. To configure the action payload, you can use contentExpression .\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\ndynamoDBv2 (dict) --Writes to the DynamoDB table that you created. The default action payload contains all attribute-value pairs that have the information about the detector model instance and the event that triggered the action. You can also customize the payload . A separate column of the DynamoDB table receives one attribute-value pair in the payload that you specify. For more information, see Actions in AWS IoT Events Developer Guide .\n\ntableName (string) -- [REQUIRED]The name of the DynamoDB table.\n\npayload (dict) --Information needed to configure the payload.\nBy default, AWS IoT Events generates a standard payload in JSON for any action. This action payload contains all attribute-value pairs that have the information about the detector model instance and the event triggered the action. To configure the action payload, you can use contentExpression .\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\niotSiteWise (dict) --Sends information about the detector model instance and the event that triggered the action to an asset property in AWS IoT SiteWise .\n\nentryId (string) --A unique identifier for this entry. You can use the entry ID to track which data entry causes an error in case of failure. The default is a new unique identifier. You can also specify an expression.\n\nassetId (string) --The ID of the asset that has the specified property. You can specify an expression.\n\npropertyId (string) --The ID of the asset property. You can specify an expression.\n\npropertyAlias (string) --The alias of the asset property. You can also specify an expression.\n\npropertyValue (dict) -- [REQUIRED]The value to send to the asset property. This value contains timestamp, quality, and value (TQV) information.\n\nvalue (dict) -- [REQUIRED]The value to send to an asset property.\n\nstringValue (string) --The asset property value is a string. You can also specify an expression. If you use an expression, the evaluated result should be a string.\n\nintegerValue (string) --The asset property value is an integer. You can also specify an expression. If you use an expression, the evaluated result should be an integer.\n\ndoubleValue (string) --The asset property value is a double. You can also specify an expression. If you use an expression, the evaluated result should be a double.\n\nbooleanValue (string) --The asset property value is a Boolean value that must be TRUE or FALSE . You can also specify an expression. If you use an expression, the evaluated result should be a Boolean value.\n\n\n\ntimestamp (dict) --The timestamp associated with the asset property value. The default is the current event time.\n\ntimeInSeconds (string) -- [REQUIRED]The timestamp, in seconds, in the Unix epoch format. The valid range is between 1-31556889864403199. You can also specify an expression.\n\noffsetInNanos (string) --The nanosecond offset converted from timeInSeconds . The valid range is between 0-999999999. You can also specify an expression.\n\n\n\nquality (string) --The quality of the asset property value. The value must be GOOD , BAD , or UNCERTAIN . You can also specify an expression.\n\n\n\n\n\n\n\n\n\n\n\n\n\ntransitionEvents (list) --Specifies the actions performed, and the next state entered, when a condition evaluates to TRUE.\n\n(dict) --Specifies the actions performed and the next state entered when a condition evaluates to TRUE.\n\neventName (string) -- [REQUIRED]The name of the transition event.\n\ncondition (string) -- [REQUIRED]Required. A Boolean expression that when TRUE causes the actions to be performed and the nextState to be entered.\n\nactions (list) --The actions to be performed.\n\n(dict) --An action to be performed when the condition is TRUE.\n\nsetVariable (dict) --Sets a variable to a specified value.\n\nvariableName (string) -- [REQUIRED]The name of the variable.\n\nvalue (string) -- [REQUIRED]The new value of the variable.\n\n\n\nsns (dict) --Sends an Amazon SNS message.\n\ntargetArn (string) -- [REQUIRED]The ARN of the Amazon SNS target where the message is sent.\n\npayload (dict) --You can configure the action payload when you send a message as an Amazon SNS push notification.\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\niotTopicPublish (dict) --Publishes an MQTT message with the given topic to the AWS IoT message broker.\n\nmqttTopic (string) -- [REQUIRED]The MQTT topic of the message. You can use a string expression that includes variables ($variable.<variable-name> ) and input values ($input.<input-name>.<path-to-datum> ) as the topic string.\n\npayload (dict) --You can configure the action payload when you publish a message to an AWS IoT Core topic.\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\nsetTimer (dict) --Information needed to set the timer.\n\ntimerName (string) -- [REQUIRED]The name of the timer.\n\nseconds (integer) --The number of seconds until the timer expires. The minimum value is 60 seconds to ensure accuracy. The maximum value is 31622400 seconds.\n\ndurationExpression (string) --The duration of the timer, in seconds. You can use a string expression that includes numbers, variables ($variable.<variable-name> ), and input values ($input.<input-name>.<path-to-datum> ) as the duration. The range of the duration is 1-31622400 seconds. To ensure accuracy, the minimum duration is 60 seconds. The evaluated result of the duration is rounded down to the nearest whole number.\n\n\n\nclearTimer (dict) --Information needed to clear the timer.\n\ntimerName (string) -- [REQUIRED]The name of the timer to clear.\n\n\n\nresetTimer (dict) --Information needed to reset the timer.\n\ntimerName (string) -- [REQUIRED]The name of the timer to reset.\n\n\n\nlambda (dict) --Calls a Lambda function, passing in information about the detector model instance and the event that triggered the action.\n\nfunctionArn (string) -- [REQUIRED]The ARN of the Lambda function that is executed.\n\npayload (dict) --You can configure the action payload when you send a message to a Lambda function.\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\niotEvents (dict) --Sends AWS IoT Events input, which passes information about the detector model instance and the event that triggered the action.\n\ninputName (string) -- [REQUIRED]The name of the AWS IoT Events input where the data is sent.\n\npayload (dict) --You can configure the action payload when you send a message to an AWS IoT Events input.\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\nsqs (dict) --Sends information about the detector model instance and the event that triggered the action to an Amazon SQS queue.\n\nqueueUrl (string) -- [REQUIRED]The URL of the SQS queue where the data is written.\n\nuseBase64 (boolean) --Set this to TRUE if you want the data to be base-64 encoded before it is written to the queue. Otherwise, set this to FALSE.\n\npayload (dict) --You can configure the action payload when you send a message to an Amazon SQS queue.\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\nfirehose (dict) --Sends information about the detector model instance and the event that triggered the action to an Amazon Kinesis Data Firehose delivery stream.\n\ndeliveryStreamName (string) -- [REQUIRED]The name of the Kinesis Data Firehose delivery stream where the data is written.\n\nseparator (string) --A character separator that is used to separate records written to the Kinesis Data Firehose delivery stream. Valid values are: \'n\' (newline), \'t\' (tab), \'rn\' (Windows newline), \',\' (comma).\n\npayload (dict) --You can configure the action payload when you send a message to an Amazon Kinesis Data Firehose delivery stream.\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\ndynamoDB (dict) --Writes to the DynamoDB table that you created. The default action payload contains all attribute-value pairs that have the information about the detector model instance and the event that triggered the action. You can also customize the payload . One column of the DynamoDB table receives all attribute-value pairs in the payload that you specify. For more information, see Actions in AWS IoT Events Developer Guide .\n\nhashKeyType (string) --The data type for the hash key (also called the partition key). You can specify the following values:\n\nSTRING - The hash key is a string.\nNUMBER - The hash key is a number.\n\nIf you don\'t specify hashKeyType , the default value is STRING .\n\nhashKeyField (string) -- [REQUIRED]The name of the hash key (also called the partition key).\n\nhashKeyValue (string) -- [REQUIRED]The value of the hash key (also called the partition key).\n\nrangeKeyType (string) --The data type for the range key (also called the sort key), You can specify the following values:\n\nSTRING - The range key is a string.\nNUMBER - The range key is number.\n\nIf you don\'t specify rangeKeyField , the default value is STRING .\n\nrangeKeyField (string) --The name of the range key (also called the sort key).\n\nrangeKeyValue (string) --The value of the range key (also called the sort key).\n\noperation (string) --The type of operation to perform. You can specify the following values:\n\nINSERT - Insert data as a new item into the DynamoDB table. This item uses the specified hash key as a partition key. If you specified a range key, the item uses the range key as a sort key.\nUPDATE - Update an existing item of the DynamoDB table with new data. This item\'s partition key must match the specified hash key. If you specified a range key, the range key must match the item\'s sort key.\nDELETE - Delete an existing item of the DynamoDB table. This item\'s partition key must match the specified hash key. If you specified a range key, the range key must match the item\'s sort key.\n\nIf you don\'t specify this parameter, AWS IoT Events triggers the INSERT operation.\n\npayloadField (string) --The name of the DynamoDB column that receives the action payload.\nIf you don\'t specify this parameter, the name of the DynamoDB column is payload .\n\ntableName (string) -- [REQUIRED]The name of the DynamoDB table.\n\npayload (dict) --Information needed to configure the payload.\nBy default, AWS IoT Events generates a standard payload in JSON for any action. This action payload contains all attribute-value pairs that have the information about the detector model instance and the event triggered the action. To configure the action payload, you can use contentExpression .\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\ndynamoDBv2 (dict) --Writes to the DynamoDB table that you created. The default action payload contains all attribute-value pairs that have the information about the detector model instance and the event that triggered the action. You can also customize the payload . A separate column of the DynamoDB table receives one attribute-value pair in the payload that you specify. For more information, see Actions in AWS IoT Events Developer Guide .\n\ntableName (string) -- [REQUIRED]The name of the DynamoDB table.\n\npayload (dict) --Information needed to configure the payload.\nBy default, AWS IoT Events generates a standard payload in JSON for any action. This action payload contains all attribute-value pairs that have the information about the detector model instance and the event triggered the action. To configure the action payload, you can use contentExpression .\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\niotSiteWise (dict) --Sends information about the detector model instance and the event that triggered the action to an asset property in AWS IoT SiteWise .\n\nentryId (string) --A unique identifier for this entry. You can use the entry ID to track which data entry causes an error in case of failure. The default is a new unique identifier. You can also specify an expression.\n\nassetId (string) --The ID of the asset that has the specified property. You can specify an expression.\n\npropertyId (string) --The ID of the asset property. You can specify an expression.\n\npropertyAlias (string) --The alias of the asset property. You can also specify an expression.\n\npropertyValue (dict) -- [REQUIRED]The value to send to the asset property. This value contains timestamp, quality, and value (TQV) information.\n\nvalue (dict) -- [REQUIRED]The value to send to an asset property.\n\nstringValue (string) --The asset property value is a string. You can also specify an expression. If you use an expression, the evaluated result should be a string.\n\nintegerValue (string) --The asset property value is an integer. You can also specify an expression. If you use an expression, the evaluated result should be an integer.\n\ndoubleValue (string) --The asset property value is a double. You can also specify an expression. If you use an expression, the evaluated result should be a double.\n\nbooleanValue (string) --The asset property value is a Boolean value that must be TRUE or FALSE . You can also specify an expression. If you use an expression, the evaluated result should be a Boolean value.\n\n\n\ntimestamp (dict) --The timestamp associated with the asset property value. The default is the current event time.\n\ntimeInSeconds (string) -- [REQUIRED]The timestamp, in seconds, in the Unix epoch format. The valid range is between 1-31556889864403199. You can also specify an expression.\n\noffsetInNanos (string) --The nanosecond offset converted from timeInSeconds . The valid range is between 0-999999999. You can also specify an expression.\n\n\n\nquality (string) --The quality of the asset property value. The value must be GOOD , BAD , or UNCERTAIN . You can also specify an expression.\n\n\n\n\n\n\n\n\n\nnextState (string) -- [REQUIRED]The next state to enter.\n\n\n\n\n\n\n\nonEnter (dict) --When entering this state, perform these actions if the condition is TRUE.\n\nevents (list) --Specifies the actions that are performed when the state is entered and the condition is TRUE .\n\n(dict) --Specifies the actions to be performed when the condition evaluates to TRUE.\n\neventName (string) -- [REQUIRED]The name of the event.\n\ncondition (string) --Optional. The Boolean expression that, when TRUE, causes the actions to be performed. If not present, the actions are performed (=TRUE). If the expression result is not a Boolean value, the actions are not performed (=FALSE).\n\nactions (list) --The actions to be performed.\n\n(dict) --An action to be performed when the condition is TRUE.\n\nsetVariable (dict) --Sets a variable to a specified value.\n\nvariableName (string) -- [REQUIRED]The name of the variable.\n\nvalue (string) -- [REQUIRED]The new value of the variable.\n\n\n\nsns (dict) --Sends an Amazon SNS message.\n\ntargetArn (string) -- [REQUIRED]The ARN of the Amazon SNS target where the message is sent.\n\npayload (dict) --You can configure the action payload when you send a message as an Amazon SNS push notification.\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\niotTopicPublish (dict) --Publishes an MQTT message with the given topic to the AWS IoT message broker.\n\nmqttTopic (string) -- [REQUIRED]The MQTT topic of the message. You can use a string expression that includes variables ($variable.<variable-name> ) and input values ($input.<input-name>.<path-to-datum> ) as the topic string.\n\npayload (dict) --You can configure the action payload when you publish a message to an AWS IoT Core topic.\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\nsetTimer (dict) --Information needed to set the timer.\n\ntimerName (string) -- [REQUIRED]The name of the timer.\n\nseconds (integer) --The number of seconds until the timer expires. The minimum value is 60 seconds to ensure accuracy. The maximum value is 31622400 seconds.\n\ndurationExpression (string) --The duration of the timer, in seconds. You can use a string expression that includes numbers, variables ($variable.<variable-name> ), and input values ($input.<input-name>.<path-to-datum> ) as the duration. The range of the duration is 1-31622400 seconds. To ensure accuracy, the minimum duration is 60 seconds. The evaluated result of the duration is rounded down to the nearest whole number.\n\n\n\nclearTimer (dict) --Information needed to clear the timer.\n\ntimerName (string) -- [REQUIRED]The name of the timer to clear.\n\n\n\nresetTimer (dict) --Information needed to reset the timer.\n\ntimerName (string) -- [REQUIRED]The name of the timer to reset.\n\n\n\nlambda (dict) --Calls a Lambda function, passing in information about the detector model instance and the event that triggered the action.\n\nfunctionArn (string) -- [REQUIRED]The ARN of the Lambda function that is executed.\n\npayload (dict) --You can configure the action payload when you send a message to a Lambda function.\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\niotEvents (dict) --Sends AWS IoT Events input, which passes information about the detector model instance and the event that triggered the action.\n\ninputName (string) -- [REQUIRED]The name of the AWS IoT Events input where the data is sent.\n\npayload (dict) --You can configure the action payload when you send a message to an AWS IoT Events input.\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\nsqs (dict) --Sends information about the detector model instance and the event that triggered the action to an Amazon SQS queue.\n\nqueueUrl (string) -- [REQUIRED]The URL of the SQS queue where the data is written.\n\nuseBase64 (boolean) --Set this to TRUE if you want the data to be base-64 encoded before it is written to the queue. Otherwise, set this to FALSE.\n\npayload (dict) --You can configure the action payload when you send a message to an Amazon SQS queue.\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\nfirehose (dict) --Sends information about the detector model instance and the event that triggered the action to an Amazon Kinesis Data Firehose delivery stream.\n\ndeliveryStreamName (string) -- [REQUIRED]The name of the Kinesis Data Firehose delivery stream where the data is written.\n\nseparator (string) --A character separator that is used to separate records written to the Kinesis Data Firehose delivery stream. Valid values are: \'n\' (newline), \'t\' (tab), \'rn\' (Windows newline), \',\' (comma).\n\npayload (dict) --You can configure the action payload when you send a message to an Amazon Kinesis Data Firehose delivery stream.\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\ndynamoDB (dict) --Writes to the DynamoDB table that you created. The default action payload contains all attribute-value pairs that have the information about the detector model instance and the event that triggered the action. You can also customize the payload . One column of the DynamoDB table receives all attribute-value pairs in the payload that you specify. For more information, see Actions in AWS IoT Events Developer Guide .\n\nhashKeyType (string) --The data type for the hash key (also called the partition key). You can specify the following values:\n\nSTRING - The hash key is a string.\nNUMBER - The hash key is a number.\n\nIf you don\'t specify hashKeyType , the default value is STRING .\n\nhashKeyField (string) -- [REQUIRED]The name of the hash key (also called the partition key).\n\nhashKeyValue (string) -- [REQUIRED]The value of the hash key (also called the partition key).\n\nrangeKeyType (string) --The data type for the range key (also called the sort key), You can specify the following values:\n\nSTRING - The range key is a string.\nNUMBER - The range key is number.\n\nIf you don\'t specify rangeKeyField , the default value is STRING .\n\nrangeKeyField (string) --The name of the range key (also called the sort key).\n\nrangeKeyValue (string) --The value of the range key (also called the sort key).\n\noperation (string) --The type of operation to perform. You can specify the following values:\n\nINSERT - Insert data as a new item into the DynamoDB table. This item uses the specified hash key as a partition key. If you specified a range key, the item uses the range key as a sort key.\nUPDATE - Update an existing item of the DynamoDB table with new data. This item\'s partition key must match the specified hash key. If you specified a range key, the range key must match the item\'s sort key.\nDELETE - Delete an existing item of the DynamoDB table. This item\'s partition key must match the specified hash key. If you specified a range key, the range key must match the item\'s sort key.\n\nIf you don\'t specify this parameter, AWS IoT Events triggers the INSERT operation.\n\npayloadField (string) --The name of the DynamoDB column that receives the action payload.\nIf you don\'t specify this parameter, the name of the DynamoDB column is payload .\n\ntableName (string) -- [REQUIRED]The name of the DynamoDB table.\n\npayload (dict) --Information needed to configure the payload.\nBy default, AWS IoT Events generates a standard payload in JSON for any action. This action payload contains all attribute-value pairs that have the information about the detector model instance and the event triggered the action. To configure the action payload, you can use contentExpression .\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\ndynamoDBv2 (dict) --Writes to the DynamoDB table that you created. The default action payload contains all attribute-value pairs that have the information about the detector model instance and the event that triggered the action. You can also customize the payload . A separate column of the DynamoDB table receives one attribute-value pair in the payload that you specify. For more information, see Actions in AWS IoT Events Developer Guide .\n\ntableName (string) -- [REQUIRED]The name of the DynamoDB table.\n\npayload (dict) --Information needed to configure the payload.\nBy default, AWS IoT Events generates a standard payload in JSON for any action. This action payload contains all attribute-value pairs that have the information about the detector model instance and the event triggered the action. To configure the action payload, you can use contentExpression .\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\niotSiteWise (dict) --Sends information about the detector model instance and the event that triggered the action to an asset property in AWS IoT SiteWise .\n\nentryId (string) --A unique identifier for this entry. You can use the entry ID to track which data entry causes an error in case of failure. The default is a new unique identifier. You can also specify an expression.\n\nassetId (string) --The ID of the asset that has the specified property. You can specify an expression.\n\npropertyId (string) --The ID of the asset property. You can specify an expression.\n\npropertyAlias (string) --The alias of the asset property. You can also specify an expression.\n\npropertyValue (dict) -- [REQUIRED]The value to send to the asset property. This value contains timestamp, quality, and value (TQV) information.\n\nvalue (dict) -- [REQUIRED]The value to send to an asset property.\n\nstringValue (string) --The asset property value is a string. You can also specify an expression. If you use an expression, the evaluated result should be a string.\n\nintegerValue (string) --The asset property value is an integer. You can also specify an expression. If you use an expression, the evaluated result should be an integer.\n\ndoubleValue (string) --The asset property value is a double. You can also specify an expression. If you use an expression, the evaluated result should be a double.\n\nbooleanValue (string) --The asset property value is a Boolean value that must be TRUE or FALSE . You can also specify an expression. If you use an expression, the evaluated result should be a Boolean value.\n\n\n\ntimestamp (dict) --The timestamp associated with the asset property value. The default is the current event time.\n\ntimeInSeconds (string) -- [REQUIRED]The timestamp, in seconds, in the Unix epoch format. The valid range is between 1-31556889864403199. You can also specify an expression.\n\noffsetInNanos (string) --The nanosecond offset converted from timeInSeconds . The valid range is between 0-999999999. You can also specify an expression.\n\n\n\nquality (string) --The quality of the asset property value. The value must be GOOD , BAD , or UNCERTAIN . You can also specify an expression.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nonExit (dict) --When exiting this state, perform these actions if the specified condition is TRUE .\n\nevents (list) --Specifies the actions that are performed when the state is exited and the condition is TRUE .\n\n(dict) --Specifies the actions to be performed when the condition evaluates to TRUE.\n\neventName (string) -- [REQUIRED]The name of the event.\n\ncondition (string) --Optional. The Boolean expression that, when TRUE, causes the actions to be performed. If not present, the actions are performed (=TRUE). If the expression result is not a Boolean value, the actions are not performed (=FALSE).\n\nactions (list) --The actions to be performed.\n\n(dict) --An action to be performed when the condition is TRUE.\n\nsetVariable (dict) --Sets a variable to a specified value.\n\nvariableName (string) -- [REQUIRED]The name of the variable.\n\nvalue (string) -- [REQUIRED]The new value of the variable.\n\n\n\nsns (dict) --Sends an Amazon SNS message.\n\ntargetArn (string) -- [REQUIRED]The ARN of the Amazon SNS target where the message is sent.\n\npayload (dict) --You can configure the action payload when you send a message as an Amazon SNS push notification.\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\niotTopicPublish (dict) --Publishes an MQTT message with the given topic to the AWS IoT message broker.\n\nmqttTopic (string) -- [REQUIRED]The MQTT topic of the message. You can use a string expression that includes variables ($variable.<variable-name> ) and input values ($input.<input-name>.<path-to-datum> ) as the topic string.\n\npayload (dict) --You can configure the action payload when you publish a message to an AWS IoT Core topic.\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\nsetTimer (dict) --Information needed to set the timer.\n\ntimerName (string) -- [REQUIRED]The name of the timer.\n\nseconds (integer) --The number of seconds until the timer expires. The minimum value is 60 seconds to ensure accuracy. The maximum value is 31622400 seconds.\n\ndurationExpression (string) --The duration of the timer, in seconds. You can use a string expression that includes numbers, variables ($variable.<variable-name> ), and input values ($input.<input-name>.<path-to-datum> ) as the duration. The range of the duration is 1-31622400 seconds. To ensure accuracy, the minimum duration is 60 seconds. The evaluated result of the duration is rounded down to the nearest whole number.\n\n\n\nclearTimer (dict) --Information needed to clear the timer.\n\ntimerName (string) -- [REQUIRED]The name of the timer to clear.\n\n\n\nresetTimer (dict) --Information needed to reset the timer.\n\ntimerName (string) -- [REQUIRED]The name of the timer to reset.\n\n\n\nlambda (dict) --Calls a Lambda function, passing in information about the detector model instance and the event that triggered the action.\n\nfunctionArn (string) -- [REQUIRED]The ARN of the Lambda function that is executed.\n\npayload (dict) --You can configure the action payload when you send a message to a Lambda function.\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\niotEvents (dict) --Sends AWS IoT Events input, which passes information about the detector model instance and the event that triggered the action.\n\ninputName (string) -- [REQUIRED]The name of the AWS IoT Events input where the data is sent.\n\npayload (dict) --You can configure the action payload when you send a message to an AWS IoT Events input.\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\nsqs (dict) --Sends information about the detector model instance and the event that triggered the action to an Amazon SQS queue.\n\nqueueUrl (string) -- [REQUIRED]The URL of the SQS queue where the data is written.\n\nuseBase64 (boolean) --Set this to TRUE if you want the data to be base-64 encoded before it is written to the queue. Otherwise, set this to FALSE.\n\npayload (dict) --You can configure the action payload when you send a message to an Amazon SQS queue.\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\nfirehose (dict) --Sends information about the detector model instance and the event that triggered the action to an Amazon Kinesis Data Firehose delivery stream.\n\ndeliveryStreamName (string) -- [REQUIRED]The name of the Kinesis Data Firehose delivery stream where the data is written.\n\nseparator (string) --A character separator that is used to separate records written to the Kinesis Data Firehose delivery stream. Valid values are: \'n\' (newline), \'t\' (tab), \'rn\' (Windows newline), \',\' (comma).\n\npayload (dict) --You can configure the action payload when you send a message to an Amazon Kinesis Data Firehose delivery stream.\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\ndynamoDB (dict) --Writes to the DynamoDB table that you created. The default action payload contains all attribute-value pairs that have the information about the detector model instance and the event that triggered the action. You can also customize the payload . One column of the DynamoDB table receives all attribute-value pairs in the payload that you specify. For more information, see Actions in AWS IoT Events Developer Guide .\n\nhashKeyType (string) --The data type for the hash key (also called the partition key). You can specify the following values:\n\nSTRING - The hash key is a string.\nNUMBER - The hash key is a number.\n\nIf you don\'t specify hashKeyType , the default value is STRING .\n\nhashKeyField (string) -- [REQUIRED]The name of the hash key (also called the partition key).\n\nhashKeyValue (string) -- [REQUIRED]The value of the hash key (also called the partition key).\n\nrangeKeyType (string) --The data type for the range key (also called the sort key), You can specify the following values:\n\nSTRING - The range key is a string.\nNUMBER - The range key is number.\n\nIf you don\'t specify rangeKeyField , the default value is STRING .\n\nrangeKeyField (string) --The name of the range key (also called the sort key).\n\nrangeKeyValue (string) --The value of the range key (also called the sort key).\n\noperation (string) --The type of operation to perform. You can specify the following values:\n\nINSERT - Insert data as a new item into the DynamoDB table. This item uses the specified hash key as a partition key. If you specified a range key, the item uses the range key as a sort key.\nUPDATE - Update an existing item of the DynamoDB table with new data. This item\'s partition key must match the specified hash key. If you specified a range key, the range key must match the item\'s sort key.\nDELETE - Delete an existing item of the DynamoDB table. This item\'s partition key must match the specified hash key. If you specified a range key, the range key must match the item\'s sort key.\n\nIf you don\'t specify this parameter, AWS IoT Events triggers the INSERT operation.\n\npayloadField (string) --The name of the DynamoDB column that receives the action payload.\nIf you don\'t specify this parameter, the name of the DynamoDB column is payload .\n\ntableName (string) -- [REQUIRED]The name of the DynamoDB table.\n\npayload (dict) --Information needed to configure the payload.\nBy default, AWS IoT Events generates a standard payload in JSON for any action. This action payload contains all attribute-value pairs that have the information about the detector model instance and the event triggered the action. To configure the action payload, you can use contentExpression .\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\ndynamoDBv2 (dict) --Writes to the DynamoDB table that you created. The default action payload contains all attribute-value pairs that have the information about the detector model instance and the event that triggered the action. You can also customize the payload . A separate column of the DynamoDB table receives one attribute-value pair in the payload that you specify. For more information, see Actions in AWS IoT Events Developer Guide .\n\ntableName (string) -- [REQUIRED]The name of the DynamoDB table.\n\npayload (dict) --Information needed to configure the payload.\nBy default, AWS IoT Events generates a standard payload in JSON for any action. This action payload contains all attribute-value pairs that have the information about the detector model instance and the event triggered the action. To configure the action payload, you can use contentExpression .\n\ncontentExpression (string) -- [REQUIRED]The content of the payload. You can use a string expression that includes quoted strings (\'<string>\' ), variables ($variable.<variable-name> ), input values ($input.<input-name>.<path-to-datum> ), string concatenations, and quoted strings that contain ${} as the content. The recommended maximum size of a content expression is 1 KB.\n\ntype (string) -- [REQUIRED]The value of the payload type can be either STRING or JSON .\n\n\n\n\n\niotSiteWise (dict) --Sends information about the detector model instance and the event that triggered the action to an asset property in AWS IoT SiteWise .\n\nentryId (string) --A unique identifier for this entry. You can use the entry ID to track which data entry causes an error in case of failure. The default is a new unique identifier. You can also specify an expression.\n\nassetId (string) --The ID of the asset that has the specified property. You can specify an expression.\n\npropertyId (string) --The ID of the asset property. You can specify an expression.\n\npropertyAlias (string) --The alias of the asset property. You can also specify an expression.\n\npropertyValue (dict) -- [REQUIRED]The value to send to the asset property. This value contains timestamp, quality, and value (TQV) information.\n\nvalue (dict) -- [REQUIRED]The value to send to an asset property.\n\nstringValue (string) --The asset property value is a string. You can also specify an expression. If you use an expression, the evaluated result should be a string.\n\nintegerValue (string) --The asset property value is an integer. You can also specify an expression. If you use an expression, the evaluated result should be an integer.\n\ndoubleValue (string) --The asset property value is a double. You can also specify an expression. If you use an expression, the evaluated result should be a double.\n\nbooleanValue (string) --The asset property value is a Boolean value that must be TRUE or FALSE . You can also specify an expression. If you use an expression, the evaluated result should be a Boolean value.\n\n\n\ntimestamp (dict) --The timestamp associated with the asset property value. The default is the current event time.\n\ntimeInSeconds (string) -- [REQUIRED]The timestamp, in seconds, in the Unix epoch format. The valid range is between 1-31556889864403199. You can also specify an expression.\n\noffsetInNanos (string) --The nanosecond offset converted from timeInSeconds . The valid range is between 0-999999999. You can also specify an expression.\n\n\n\nquality (string) --The quality of the asset property value. The value must be GOOD , BAD , or UNCERTAIN . You can also specify an expression.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\ninitialStateName (string) -- [REQUIRED]The state that is entered at the creation of each detector (instance).\n\n\n

    :type detectorModelDescription: string
    :param detectorModelDescription: A brief description of the detector model.

    :type roleArn: string
    :param roleArn: [REQUIRED]\nThe ARN of the role that grants permission to AWS IoT Events to perform its operations.\n

    :type evaluationMethod: string
    :param evaluationMethod: Information about the order in which events are evaluated and how actions are executed.

    :rtype: dict

ReturnsResponse Syntax
{
    'detectorModelConfiguration': {
        'detectorModelName': 'string',
        'detectorModelVersion': 'string',
        'detectorModelDescription': 'string',
        'detectorModelArn': 'string',
        'roleArn': 'string',
        'creationTime': datetime(2015, 1, 1),
        'lastUpdateTime': datetime(2015, 1, 1),
        'status': 'ACTIVE'|'ACTIVATING'|'INACTIVE'|'DEPRECATED'|'DRAFT'|'PAUSED'|'FAILED',
        'key': 'string',
        'evaluationMethod': 'BATCH'|'SERIAL'
    }
}


Response Structure

(dict) --

detectorModelConfiguration (dict) --
Information about how the detector model is configured.

detectorModelName (string) --
The name of the detector model.

detectorModelVersion (string) --
The version of the detector model.

detectorModelDescription (string) --
A brief description of the detector model.

detectorModelArn (string) --
The ARN of the detector model.

roleArn (string) --
The ARN of the role that grants permission to AWS IoT Events to perform its operations.

creationTime (datetime) --
The time the detector model was created.

lastUpdateTime (datetime) --
The time the detector model was last updated.

status (string) --
The status of the detector model.

key (string) --
The value used to identify a detector instance. When a device or system sends input, a new detector instance with a unique key value is created. AWS IoT Events can continue to route input to its corresponding detector instance based on this identifying information.
This parameter uses a JSON-path expression to select the attribute-value pair in the message payload that is used for identification. To route the message to the correct detector instance, the device must send a message payload that contains the same attribute-value.

evaluationMethod (string) --
Information about the order in which events are evaluated and how actions are executed.









Exceptions

IoTEvents.Client.exceptions.InvalidRequestException
IoTEvents.Client.exceptions.ResourceInUseException
IoTEvents.Client.exceptions.ResourceNotFoundException
IoTEvents.Client.exceptions.ThrottlingException
IoTEvents.Client.exceptions.InternalFailureException
IoTEvents.Client.exceptions.ServiceUnavailableException


    :return: {
        'detectorModelConfiguration': {
            'detectorModelName': 'string',
            'detectorModelVersion': 'string',
            'detectorModelDescription': 'string',
            'detectorModelArn': 'string',
            'roleArn': 'string',
            'creationTime': datetime(2015, 1, 1),
            'lastUpdateTime': datetime(2015, 1, 1),
            'status': 'ACTIVE'|'ACTIVATING'|'INACTIVE'|'DEPRECATED'|'DRAFT'|'PAUSED'|'FAILED',
            'key': 'string',
            'evaluationMethod': 'BATCH'|'SERIAL'
        }
    }
    
    
    :returns: 
    IoTEvents.Client.exceptions.InvalidRequestException
    IoTEvents.Client.exceptions.ResourceInUseException
    IoTEvents.Client.exceptions.ResourceNotFoundException
    IoTEvents.Client.exceptions.ThrottlingException
    IoTEvents.Client.exceptions.InternalFailureException
    IoTEvents.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def update_input(inputName=None, inputDescription=None, inputDefinition=None):
    """
    Updates an input.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_input(
        inputName='string',
        inputDescription='string',
        inputDefinition={
            'attributes': [
                {
                    'jsonPath': 'string'
                },
            ]
        }
    )
    
    
    :type inputName: string
    :param inputName: [REQUIRED]\nThe name of the input you want to update.\n

    :type inputDescription: string
    :param inputDescription: A brief description of the input.

    :type inputDefinition: dict
    :param inputDefinition: [REQUIRED]\nThe definition of the input.\n\nattributes (list) -- [REQUIRED]The attributes from the JSON payload that are made available by the input. Inputs are derived from messages sent to the AWS IoT Events system using BatchPutMessage . Each such message contains a JSON payload, and those attributes (and their paired values) specified here are available for use in the condition expressions used by detectors that monitor this input.\n\n(dict) --The attributes from the JSON payload that are made available by the input. Inputs are derived from messages sent to the AWS IoT Events system using BatchPutMessage . Each such message contains a JSON payload. Those attributes (and their paired values) specified here are available for use in the condition expressions used by detectors.\n\njsonPath (string) -- [REQUIRED]An expression that specifies an attribute-value pair in a JSON structure. Use this to specify an attribute from the JSON payload that is made available by the input. Inputs are derived from messages sent to AWS IoT Events (BatchPutMessage ). Each such message contains a JSON payload. The attribute (and its paired value) specified here are available for use in the condition expressions used by detectors.\nSyntax: <field-name>.<field-name>...\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'inputConfiguration': {
        'inputName': 'string',
        'inputDescription': 'string',
        'inputArn': 'string',
        'creationTime': datetime(2015, 1, 1),
        'lastUpdateTime': datetime(2015, 1, 1),
        'status': 'CREATING'|'UPDATING'|'ACTIVE'|'DELETING'
    }
}


Response Structure

(dict) --

inputConfiguration (dict) --
Information about the configuration of the input.

inputName (string) --
The name of the input.

inputDescription (string) --
A brief description of the input.

inputArn (string) --
The ARN of the input.

creationTime (datetime) --
The time the input was created.

lastUpdateTime (datetime) --
The last time the input was updated.

status (string) --
The status of the input.









Exceptions

IoTEvents.Client.exceptions.InvalidRequestException
IoTEvents.Client.exceptions.ThrottlingException
IoTEvents.Client.exceptions.ResourceNotFoundException
IoTEvents.Client.exceptions.InternalFailureException
IoTEvents.Client.exceptions.ServiceUnavailableException
IoTEvents.Client.exceptions.ResourceInUseException


    :return: {
        'inputConfiguration': {
            'inputName': 'string',
            'inputDescription': 'string',
            'inputArn': 'string',
            'creationTime': datetime(2015, 1, 1),
            'lastUpdateTime': datetime(2015, 1, 1),
            'status': 'CREATING'|'UPDATING'|'ACTIVE'|'DELETING'
        }
    }
    
    
    :returns: 
    IoTEvents.Client.exceptions.InvalidRequestException
    IoTEvents.Client.exceptions.ThrottlingException
    IoTEvents.Client.exceptions.ResourceNotFoundException
    IoTEvents.Client.exceptions.InternalFailureException
    IoTEvents.Client.exceptions.ServiceUnavailableException
    IoTEvents.Client.exceptions.ResourceInUseException
    
    """
    pass

