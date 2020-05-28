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

def get_waiter(waiter_name=None):
    """
    Returns an object that can wait for some condition.
    
    :type waiter_name: str
    :param waiter_name: The name of the waiter to get. See the waiters\nsection of the service docs for a list of available waiters.

    :rtype: botocore.waiter.Waiter


    """
    pass

def query_forecast(ForecastArn=None, StartDate=None, EndDate=None, Filters=None, NextToken=None):
    """
    Retrieves a forecast for a single item, filtered by the supplied criteria.
    The criteria is a key-value pair. The key is either item_id (or the equivalent non-timestamp, non-target field) from the TARGET_TIME_SERIES dataset, or one of the forecast dimensions specified as part of the FeaturizationConfig object.
    By default, QueryForecast returns the complete date range for the filtered forecast. You can request a specific date range.
    To get the full forecast, use the CreateForecastExportJob operation.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.query_forecast(
        ForecastArn='string',
        StartDate='string',
        EndDate='string',
        Filters={
            'string': 'string'
        },
        NextToken='string'
    )
    
    
    :type ForecastArn: string
    :param ForecastArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the forecast to query.\n

    :type StartDate: string
    :param StartDate: The start date for the forecast. Specify the date using this format: yyyy-MM-dd\'T\'HH:mm:ss (ISO 8601 format). For example, 2015-01-01T08:00:00.

    :type EndDate: string
    :param EndDate: The end date for the forecast. Specify the date using this format: yyyy-MM-dd\'T\'HH:mm:ss (ISO 8601 format). For example, 2015-01-01T20:00:00.

    :type Filters: dict
    :param Filters: [REQUIRED]\nThe filtering criteria to apply when retrieving the forecast. For example, to get the forecast for client_21 in the electricity usage dataset, specify the following:\n\n{'item_id' : 'client_21'}\nTo get the full forecast, use the CreateForecastExportJob operation.\n\n(string) --\n(string) --\n\n\n\n

    :type NextToken: string
    :param NextToken: If the result of the previous request was truncated, the response includes a NextToken . To retrieve the next set of results, use the token in the next request. Tokens expire after 24 hours.

    :rtype: dict

ReturnsResponse Syntax
{
    'Forecast': {
        'Predictions': {
            'string': [
                {
                    'Timestamp': 'string',
                    'Value': 123.0
                },
            ]
        }
    }
}


Response Structure

(dict) --

Forecast (dict) --
The forecast.

Predictions (dict) --
The forecast.
The string of the string-to-array map is one of the following values:

p10
p50
p90


(string) --

(list) --

(dict) --
The forecast value for a specific date. Part of the  Forecast object.

Timestamp (string) --
The timestamp of the specific forecast.

Value (float) --
The forecast value.

















Exceptions

ForecastQueryService.Client.exceptions.ResourceNotFoundException
ForecastQueryService.Client.exceptions.ResourceInUseException
ForecastQueryService.Client.exceptions.InvalidInputException
ForecastQueryService.Client.exceptions.LimitExceededException
ForecastQueryService.Client.exceptions.InvalidNextTokenException


    :return: {
        'Forecast': {
            'Predictions': {
                'string': [
                    {
                        'Timestamp': 'string',
                        'Value': 123.0
                    },
                ]
            }
        }
    }
    
    
    :returns: 
    p10
    p50
    p90
    
    """
    pass

