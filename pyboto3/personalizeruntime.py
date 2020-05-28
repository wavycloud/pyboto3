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

def get_personalized_ranking(campaignArn=None, inputList=None, userId=None, context=None):
    """
    Re-ranks a list of recommended items for the given user. The first item in the list is deemed the most likely item to be of interest to the user.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_personalized_ranking(
        campaignArn='string',
        inputList=[
            'string',
        ],
        userId='string',
        context={
            'string': 'string'
        }
    )
    
    
    :type campaignArn: string
    :param campaignArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the campaign to use for generating the personalized ranking.\n

    :type inputList: list
    :param inputList: [REQUIRED]\nA list of items (itemId\'s) to rank. If an item was not included in the training dataset, the item is appended to the end of the reranked list. The maximum is 500.\n\n(string) --\n\n

    :type userId: string
    :param userId: [REQUIRED]\nThe user for which you want the campaign to provide a personalized ranking.\n

    :type context: dict
    :param context: The contextual metadata to use when getting recommendations. Contextual metadata includes any interaction information that might be relevant when getting a user\'s recommendations, such as the user\'s current location or device type.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'personalizedRanking': [
        {
            'itemId': 'string',
            'score': 123.0
        },
    ]
}


Response Structure

(dict) --

personalizedRanking (list) --
A list of items in order of most likely interest to the user. The maximum is 500.

(dict) --
An object that identifies an item.
The and APIs return a list of PredictedItem s.

itemId (string) --
The recommended item ID.

score (float) --
A numeric representation of the model\'s certainty in the item\'s suitability. For more information on scoring logic, see  how-scores-work .











Exceptions

PersonalizeRuntime.Client.exceptions.InvalidInputException
PersonalizeRuntime.Client.exceptions.ResourceNotFoundException


    :return: {
        'personalizedRanking': [
            {
                'itemId': 'string',
                'score': 123.0
            },
        ]
    }
    
    
    :returns: 
    PersonalizeRuntime.Client.exceptions.InvalidInputException
    PersonalizeRuntime.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def get_recommendations(campaignArn=None, itemId=None, userId=None, numResults=None, context=None):
    """
    Returns a list of recommended items. The required input depends on the recipe type used to create the solution backing the campaign, as follows:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_recommendations(
        campaignArn='string',
        itemId='string',
        userId='string',
        numResults=123,
        context={
            'string': 'string'
        }
    )
    
    
    :type campaignArn: string
    :param campaignArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the campaign to use for getting recommendations.\n

    :type itemId: string
    :param itemId: The item ID to provide recommendations for.\nRequired for RELATED_ITEMS recipe type.\n

    :type userId: string
    :param userId: The user ID to provide recommendations for.\nRequired for USER_PERSONALIZATION recipe type.\n

    :type numResults: integer
    :param numResults: The number of results to return. The default is 25. The maximum is 500.

    :type context: dict
    :param context: The contextual metadata to use when getting recommendations. Contextual metadata includes any interaction information that might be relevant when getting a user\'s recommendations, such as the user\'s current location or device type.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'itemList': [
        {
            'itemId': 'string',
            'score': 123.0
        },
    ]
}


Response Structure

(dict) --

itemList (list) --
A list of recommendations sorted in ascending order by prediction score. There can be a maximum of 500 items in the list.

(dict) --
An object that identifies an item.
The and APIs return a list of PredictedItem s.

itemId (string) --
The recommended item ID.

score (float) --
A numeric representation of the model\'s certainty in the item\'s suitability. For more information on scoring logic, see  how-scores-work .











Exceptions

PersonalizeRuntime.Client.exceptions.InvalidInputException
PersonalizeRuntime.Client.exceptions.ResourceNotFoundException


    :return: {
        'itemList': [
            {
                'itemId': 'string',
                'score': 123.0
            },
        ]
    }
    
    
    :returns: 
    campaignArn (string) -- [REQUIRED]
    The Amazon Resource Name (ARN) of the campaign to use for getting recommendations.
    
    itemId (string) -- The item ID to provide recommendations for.
    Required for RELATED_ITEMS recipe type.
    
    userId (string) -- The user ID to provide recommendations for.
    Required for USER_PERSONALIZATION recipe type.
    
    numResults (integer) -- The number of results to return. The default is 25. The maximum is 500.
    context (dict) -- The contextual metadata to use when getting recommendations. Contextual metadata includes any interaction information that might be relevant when getting a user\'s recommendations, such as the user\'s current location or device type.
    
    (string) --
    (string) --
    
    
    
    
    
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

