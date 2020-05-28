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

def batch_put_message(messages=None):
    """
    Sends a set of messages to the AWS IoT Events system. Each message payload is transformed into the input you specify ("inputName" ) and ingested into any detectors that monitor that input. If multiple messages are sent, the order in which the messages are processed isn\'t guaranteed. To guarantee ordering, you must send messages one at a time and wait for a successful response.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_put_message(
        messages=[
            {
                'messageId': 'string',
                'inputName': 'string',
                'payload': b'bytes'
            },
        ]
    )
    
    
    :type messages: list
    :param messages: [REQUIRED]\nThe list of messages to send. Each message has the following format: \'{ 'messageId': 'string', 'inputName': 'string', 'payload': 'string'}\'\n\n(dict) --Information about a message.\n\nmessageId (string) -- [REQUIRED]The ID to assign to the message. Within each batch sent, each 'messageId' must be unique.\n\ninputName (string) -- [REQUIRED]The name of the input into which the message payload is transformed.\n\npayload (bytes) -- [REQUIRED]The payload of the message. This can be a JSON string or a Base-64-encoded string representing binary data (in which case you must decode it).\n\n\n\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'BatchPutMessageErrorEntries': [
        {
            'messageId': 'string',
            'errorCode': 'ResourceNotFoundException'|'InvalidRequestException'|'InternalFailureException'|'ServiceUnavailableException'|'ThrottlingException',
            'errorMessage': 'string'
        },
    ]
}


Response Structure

(dict) --
BatchPutMessageErrorEntries (list) --A list of any errors encountered when sending the messages.

(dict) --Contains information about the errors encountered.

messageId (string) --The ID of the message that caused the error. (See the value corresponding to the "messageId" key in the "message" object.)

errorCode (string) --The code associated with the error.

errorMessage (string) --More information about the error.










Exceptions

IoTEventsData.Client.exceptions.InvalidRequestException
IoTEventsData.Client.exceptions.InternalFailureException
IoTEventsData.Client.exceptions.ServiceUnavailableException
IoTEventsData.Client.exceptions.ThrottlingException


    :return: {
        'BatchPutMessageErrorEntries': [
            {
                'messageId': 'string',
                'errorCode': 'ResourceNotFoundException'|'InvalidRequestException'|'InternalFailureException'|'ServiceUnavailableException'|'ThrottlingException',
                'errorMessage': 'string'
            },
        ]
    }
    
    
    """
    pass

def batch_update_detector(detectors=None):
    """
    Updates the state, variable values, and timer settings of one or more detectors (instances) of a specified detector model.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_update_detector(
        detectors=[
            {
                'messageId': 'string',
                'detectorModelName': 'string',
                'keyValue': 'string',
                'state': {
                    'stateName': 'string',
                    'variables': [
                        {
                            'name': 'string',
                            'value': 'string'
                        },
                    ],
                    'timers': [
                        {
                            'name': 'string',
                            'seconds': 123
                        },
                    ]
                }
            },
        ]
    )
    
    
    :type detectors: list
    :param detectors: [REQUIRED]\nThe list of detectors (instances) to update, along with the values to update.\n\n(dict) --Information used to update the detector (instance).\n\nmessageId (string) -- [REQUIRED]The ID to assign to the detector update 'message' . Each 'messageId' must be unique within each batch sent.\n\ndetectorModelName (string) -- [REQUIRED]The name of the detector model that created the detectors (instances).\n\nkeyValue (string) --The value of the input key attribute (identifying the device or system) that caused the creation of this detector (instance).\n\nstate (dict) -- [REQUIRED]The new state, variable values, and timer settings of the detector (instance).\n\nstateName (string) -- [REQUIRED]The name of the new state of the detector (instance).\n\nvariables (list) -- [REQUIRED]The new values of the detector\'s variables. Any variable whose value isn\'t specified is cleared.\n\n(dict) --The new value of the variable.\n\nname (string) -- [REQUIRED]The name of the variable.\n\nvalue (string) -- [REQUIRED]The new value of the variable.\n\n\n\n\n\ntimers (list) -- [REQUIRED]The new values of the detector\'s timers. Any timer whose value isn\'t specified is cleared, and its timeout event won\'t occur.\n\n(dict) --The new setting of a timer.\n\nname (string) -- [REQUIRED]The name of the timer.\n\nseconds (integer) -- [REQUIRED]The new setting of the timer (the number of seconds before the timer elapses).\n\n\n\n\n\n\n\n\n\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'batchUpdateDetectorErrorEntries': [
        {
            'messageId': 'string',
            'errorCode': 'ResourceNotFoundException'|'InvalidRequestException'|'InternalFailureException'|'ServiceUnavailableException'|'ThrottlingException',
            'errorMessage': 'string'
        },
    ]
}


Response Structure

(dict) --
batchUpdateDetectorErrorEntries (list) --A list of those detector updates that resulted in errors. (If an error is listed here, the specific update did not occur.)

(dict) --Information about the error that occured when attempting to update a detector.

messageId (string) --The "messageId" of the update request that caused the error. (The value of the "messageId" in the update request "Detector" object.)

errorCode (string) --The code of the error.

errorMessage (string) --A message describing the error.










Exceptions

IoTEventsData.Client.exceptions.InvalidRequestException
IoTEventsData.Client.exceptions.InternalFailureException
IoTEventsData.Client.exceptions.ServiceUnavailableException
IoTEventsData.Client.exceptions.ThrottlingException


    :return: {
        'batchUpdateDetectorErrorEntries': [
            {
                'messageId': 'string',
                'errorCode': 'ResourceNotFoundException'|'InvalidRequestException'|'InternalFailureException'|'ServiceUnavailableException'|'ThrottlingException',
                'errorMessage': 'string'
            },
        ]
    }
    
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def describe_detector(detectorModelName=None, keyValue=None):
    """
    Returns information about the specified detector (instance).
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_detector(
        detectorModelName='string',
        keyValue='string'
    )
    
    
    :type detectorModelName: string
    :param detectorModelName: [REQUIRED]\nThe name of the detector model whose detectors (instances) you want information about.\n

    :type keyValue: string
    :param keyValue: A filter used to limit results to detectors (instances) created because of the given key ID.

    :rtype: dict

ReturnsResponse Syntax
{
    'detector': {
        'detectorModelName': 'string',
        'keyValue': 'string',
        'detectorModelVersion': 'string',
        'state': {
            'stateName': 'string',
            'variables': [
                {
                    'name': 'string',
                    'value': 'string'
                },
            ],
            'timers': [
                {
                    'name': 'string',
                    'timestamp': datetime(2015, 1, 1)
                },
            ]
        },
        'creationTime': datetime(2015, 1, 1),
        'lastUpdateTime': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --

detector (dict) --
Information about the detector (instance).

detectorModelName (string) --
The name of the detector model that created this detector (instance).

keyValue (string) --
The value of the key (identifying the device or system) that caused the creation of this detector (instance).

detectorModelVersion (string) --
The version of the detector model that created this detector (instance).

state (dict) --
The current state of the detector (instance).

stateName (string) --
The name of the state.

variables (list) --
The current values of the detector\'s variables.

(dict) --
The current state of the variable.

name (string) --
The name of the variable.

value (string) --
The current value of the variable.





timers (list) --
The current state of the detector\'s timers.

(dict) --
The current state of a timer.

name (string) --
The name of the timer.

timestamp (datetime) --
The number of seconds which have elapsed on the timer.







creationTime (datetime) --
The time the detector (instance) was created.

lastUpdateTime (datetime) --
The time the detector (instance) was last updated.









Exceptions

IoTEventsData.Client.exceptions.InvalidRequestException
IoTEventsData.Client.exceptions.ResourceNotFoundException
IoTEventsData.Client.exceptions.ThrottlingException
IoTEventsData.Client.exceptions.InternalFailureException
IoTEventsData.Client.exceptions.ServiceUnavailableException


    :return: {
        'detector': {
            'detectorModelName': 'string',
            'keyValue': 'string',
            'detectorModelVersion': 'string',
            'state': {
                'stateName': 'string',
                'variables': [
                    {
                        'name': 'string',
                        'value': 'string'
                    },
                ],
                'timers': [
                    {
                        'name': 'string',
                        'timestamp': datetime(2015, 1, 1)
                    },
                ]
            },
            'creationTime': datetime(2015, 1, 1),
            'lastUpdateTime': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    IoTEventsData.Client.exceptions.InvalidRequestException
    IoTEventsData.Client.exceptions.ResourceNotFoundException
    IoTEventsData.Client.exceptions.ThrottlingException
    IoTEventsData.Client.exceptions.InternalFailureException
    IoTEventsData.Client.exceptions.ServiceUnavailableException
    
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

def list_detectors(detectorModelName=None, stateName=None, nextToken=None, maxResults=None):
    """
    Lists detectors (the instances of a detector model).
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_detectors(
        detectorModelName='string',
        stateName='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type detectorModelName: string
    :param detectorModelName: [REQUIRED]\nThe name of the detector model whose detectors (instances) are listed.\n

    :type stateName: string
    :param stateName: A filter that limits results to those detectors (instances) in the given state.

    :type nextToken: string
    :param nextToken: The token for the next set of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return at one time.

    :rtype: dict

ReturnsResponse Syntax
{
    'detectorSummaries': [
        {
            'detectorModelName': 'string',
            'keyValue': 'string',
            'detectorModelVersion': 'string',
            'state': {
                'stateName': 'string'
            },
            'creationTime': datetime(2015, 1, 1),
            'lastUpdateTime': datetime(2015, 1, 1)
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

detectorSummaries (list) --
A list of summary information about the detectors (instances).

(dict) --
Information about the detector (instance).

detectorModelName (string) --
The name of the detector model that created this detector (instance).

keyValue (string) --
The value of the key (identifying the device or system) that caused the creation of this detector (instance).

detectorModelVersion (string) --
The version of the detector model that created this detector (instance).

state (dict) --
The current state of the detector (instance).

stateName (string) --
The name of the state.



creationTime (datetime) --
The time the detector (instance) was created.

lastUpdateTime (datetime) --
The time the detector (instance) was last updated.





nextToken (string) --
A token to retrieve the next set of results, or null if there are no additional results.







Exceptions

IoTEventsData.Client.exceptions.InvalidRequestException
IoTEventsData.Client.exceptions.ResourceNotFoundException
IoTEventsData.Client.exceptions.ThrottlingException
IoTEventsData.Client.exceptions.InternalFailureException
IoTEventsData.Client.exceptions.ServiceUnavailableException


    :return: {
        'detectorSummaries': [
            {
                'detectorModelName': 'string',
                'keyValue': 'string',
                'detectorModelVersion': 'string',
                'state': {
                    'stateName': 'string'
                },
                'creationTime': datetime(2015, 1, 1),
                'lastUpdateTime': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    IoTEventsData.Client.exceptions.InvalidRequestException
    IoTEventsData.Client.exceptions.ResourceNotFoundException
    IoTEventsData.Client.exceptions.ThrottlingException
    IoTEventsData.Client.exceptions.InternalFailureException
    IoTEventsData.Client.exceptions.ServiceUnavailableException
    
    """
    pass

