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

def delete_human_loop(HumanLoopName=None):
    """
    Deletes the specified human loop for a flow definition.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_human_loop(
        HumanLoopName='string'
    )
    
    
    :type HumanLoopName: string
    :param HumanLoopName: [REQUIRED]\nThe name of the human loop that you want to delete.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

AugmentedAIRuntime.Client.exceptions.ValidationException
AugmentedAIRuntime.Client.exceptions.ResourceNotFoundException
AugmentedAIRuntime.Client.exceptions.ThrottlingException
AugmentedAIRuntime.Client.exceptions.InternalServerException


    :return: {}
    
    
    :returns: 
    AugmentedAIRuntime.Client.exceptions.ValidationException
    AugmentedAIRuntime.Client.exceptions.ResourceNotFoundException
    AugmentedAIRuntime.Client.exceptions.ThrottlingException
    AugmentedAIRuntime.Client.exceptions.InternalServerException
    
    """
    pass

def describe_human_loop(HumanLoopName=None):
    """
    Returns information about the specified human loop.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_human_loop(
        HumanLoopName='string'
    )
    
    
    :type HumanLoopName: string
    :param HumanLoopName: [REQUIRED]\nThe name of the human loop that you want information about.\n

    :rtype: dict
ReturnsResponse Syntax{
    'CreationTime': datetime(2015, 1, 1),
    'FailureReason': 'string',
    'FailureCode': 'string',
    'HumanLoopStatus': 'InProgress'|'Failed'|'Completed'|'Stopped'|'Stopping',
    'HumanLoopName': 'string',
    'HumanLoopArn': 'string',
    'FlowDefinitionArn': 'string',
    'HumanLoopOutput': {
        'OutputS3Uri': 'string'
    }
}


Response Structure

(dict) --
CreationTime (datetime) --The creation time when Amazon Augmented AI created the human loop.

FailureReason (string) --The reason why a human loop failed. The failure reason is returned when the status of the human loop is Failed .

FailureCode (string) --A failure code that identifies the type of failure.

HumanLoopStatus (string) --The status of the human loop.

HumanLoopName (string) --The name of the human loop. The name must be lowercase, unique within the Region in your account, and can have up to 63 characters. Valid characters: a-z, 0-9, and - (hyphen).

HumanLoopArn (string) --The Amazon Resource Name (ARN) of the human loop.

FlowDefinitionArn (string) --The Amazon Resource Name (ARN) of the flow definition.

HumanLoopOutput (dict) --An object that contains information about the output of the human loop.

OutputS3Uri (string) --The location of the Amazon S3 object where Amazon Augmented AI stores your human loop output.








Exceptions

AugmentedAIRuntime.Client.exceptions.ValidationException
AugmentedAIRuntime.Client.exceptions.ResourceNotFoundException
AugmentedAIRuntime.Client.exceptions.ThrottlingException
AugmentedAIRuntime.Client.exceptions.InternalServerException


    :return: {
        'CreationTime': datetime(2015, 1, 1),
        'FailureReason': 'string',
        'FailureCode': 'string',
        'HumanLoopStatus': 'InProgress'|'Failed'|'Completed'|'Stopped'|'Stopping',
        'HumanLoopName': 'string',
        'HumanLoopArn': 'string',
        'FlowDefinitionArn': 'string',
        'HumanLoopOutput': {
            'OutputS3Uri': 'string'
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

def list_human_loops(CreationTimeAfter=None, CreationTimeBefore=None, FlowDefinitionArn=None, SortOrder=None, NextToken=None, MaxResults=None):
    """
    Returns information about human loops, given the specified parameters. If a human loop was deleted, it will not be included.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_human_loops(
        CreationTimeAfter=datetime(2015, 1, 1),
        CreationTimeBefore=datetime(2015, 1, 1),
        FlowDefinitionArn='string',
        SortOrder='Ascending'|'Descending',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type CreationTimeAfter: datetime
    :param CreationTimeAfter: (Optional) The timestamp of the date when you want the human loops to begin in ISO 8601 format. For example, 2020-02-24 .

    :type CreationTimeBefore: datetime
    :param CreationTimeBefore: (Optional) The timestamp of the date before which you want the human loops to begin in ISO 8601 format. For example, 2020-02-24 .

    :type FlowDefinitionArn: string
    :param FlowDefinitionArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of a flow definition.\n

    :type SortOrder: string
    :param SortOrder: Optional. The order for displaying results. Valid values: Ascending and Descending .

    :type NextToken: string
    :param NextToken: A token to display the next page of results.

    :type MaxResults: integer
    :param MaxResults: The total number of items to return. If the total number of available items is more than the value specified in MaxResults , then a NextToken is returned in the output. You can use this token to display the next page of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'HumanLoopSummaries': [
        {
            'HumanLoopName': 'string',
            'HumanLoopStatus': 'InProgress'|'Failed'|'Completed'|'Stopped'|'Stopping',
            'CreationTime': datetime(2015, 1, 1),
            'FailureReason': 'string',
            'FlowDefinitionArn': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

HumanLoopSummaries (list) --
An array of objects that contain information about the human loops.

(dict) --
Summary information about the human loop.

HumanLoopName (string) --
The name of the human loop.

HumanLoopStatus (string) --
The status of the human loop.

CreationTime (datetime) --
When Amazon Augmented AI created the human loop.

FailureReason (string) --
The reason why the human loop failed. A failure reason is returned when the status of the human loop is Failed .

FlowDefinitionArn (string) --
The Amazon Resource Name (ARN) of the flow definition used to configure the human loop.





NextToken (string) --
A token to display the next page of results.







Exceptions

AugmentedAIRuntime.Client.exceptions.ValidationException
AugmentedAIRuntime.Client.exceptions.ResourceNotFoundException
AugmentedAIRuntime.Client.exceptions.ThrottlingException
AugmentedAIRuntime.Client.exceptions.InternalServerException


    :return: {
        'HumanLoopSummaries': [
            {
                'HumanLoopName': 'string',
                'HumanLoopStatus': 'InProgress'|'Failed'|'Completed'|'Stopped'|'Stopping',
                'CreationTime': datetime(2015, 1, 1),
                'FailureReason': 'string',
                'FlowDefinitionArn': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    AugmentedAIRuntime.Client.exceptions.ValidationException
    AugmentedAIRuntime.Client.exceptions.ResourceNotFoundException
    AugmentedAIRuntime.Client.exceptions.ThrottlingException
    AugmentedAIRuntime.Client.exceptions.InternalServerException
    
    """
    pass

def start_human_loop(HumanLoopName=None, FlowDefinitionArn=None, HumanLoopInput=None, DataAttributes=None):
    """
    Starts a human loop, provided that at least one activation condition is met.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_human_loop(
        HumanLoopName='string',
        FlowDefinitionArn='string',
        HumanLoopInput={
            'InputContent': 'string'
        },
        DataAttributes={
            'ContentClassifiers': [
                'FreeOfPersonallyIdentifiableInformation'|'FreeOfAdultContent',
            ]
        }
    )
    
    
    :type HumanLoopName: string
    :param HumanLoopName: [REQUIRED]\nThe name of the human loop.\n

    :type FlowDefinitionArn: string
    :param FlowDefinitionArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the flow definition associated with this human loop.\n

    :type HumanLoopInput: dict
    :param HumanLoopInput: [REQUIRED]\nAn object that contains information about the human loop.\n\nInputContent (string) -- [REQUIRED]Serialized input from the human loop. The input must be a string representation of a file in JSON format.\n\n\n

    :type DataAttributes: dict
    :param DataAttributes: Attributes of the specified data. Use DataAttributes to specify if your data is free of personally identifiable information and/or free of adult content.\n\nContentClassifiers (list) -- [REQUIRED]Declares that your content is free of personally identifiable information or adult content.\nAmazon SageMaker can restrict the Amazon Mechanical Turk workers who can view your task based on this information.\n\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'HumanLoopArn': 'string'
}


Response Structure

(dict) --

HumanLoopArn (string) --
The Amazon Resource Name (ARN) of the human loop.







Exceptions

AugmentedAIRuntime.Client.exceptions.ValidationException
AugmentedAIRuntime.Client.exceptions.ThrottlingException
AugmentedAIRuntime.Client.exceptions.ServiceQuotaExceededException
AugmentedAIRuntime.Client.exceptions.InternalServerException
AugmentedAIRuntime.Client.exceptions.ConflictException


    :return: {
        'HumanLoopArn': 'string'
    }
    
    
    :returns: 
    AugmentedAIRuntime.Client.exceptions.ValidationException
    AugmentedAIRuntime.Client.exceptions.ThrottlingException
    AugmentedAIRuntime.Client.exceptions.ServiceQuotaExceededException
    AugmentedAIRuntime.Client.exceptions.InternalServerException
    AugmentedAIRuntime.Client.exceptions.ConflictException
    
    """
    pass

def stop_human_loop(HumanLoopName=None):
    """
    Stops the specified human loop.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.stop_human_loop(
        HumanLoopName='string'
    )
    
    
    :type HumanLoopName: string
    :param HumanLoopName: [REQUIRED]\nThe name of the human loop that you want to stop.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

AugmentedAIRuntime.Client.exceptions.ValidationException
AugmentedAIRuntime.Client.exceptions.ResourceNotFoundException
AugmentedAIRuntime.Client.exceptions.ThrottlingException
AugmentedAIRuntime.Client.exceptions.InternalServerException


    :return: {}
    
    
    :returns: 
    AugmentedAIRuntime.Client.exceptions.ValidationException
    AugmentedAIRuntime.Client.exceptions.ResourceNotFoundException
    AugmentedAIRuntime.Client.exceptions.ThrottlingException
    AugmentedAIRuntime.Client.exceptions.InternalServerException
    
    """
    pass

