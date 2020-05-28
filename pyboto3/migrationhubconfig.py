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

def create_home_region_control(HomeRegion=None, Target=None, DryRun=None):
    """
    This API sets up the home region for the calling account only.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_home_region_control(
        HomeRegion='string',
        Target={
            'Type': 'ACCOUNT',
            'Id': 'string'
        },
        DryRun=True|False
    )
    
    
    :type HomeRegion: string
    :param HomeRegion: [REQUIRED]\nThe name of the home region of the calling account.\n

    :type Target: dict
    :param Target: [REQUIRED]\nThe account for which this command sets up a home region control. The Target is always of type ACCOUNT .\n\nType (string) -- [REQUIRED]The target type is always an ACCOUNT .\n\nId (string) --The TargetID is a 12-character identifier of the ACCOUNT for which the control was created. (This must be the current account.)\n\n\n

    :type DryRun: boolean
    :param DryRun: Optional Boolean flag to indicate whether any effect should take place. It tests whether the caller has permission to make the call.

    :rtype: dict

ReturnsResponse Syntax
{
    'HomeRegionControl': {
        'ControlId': 'string',
        'HomeRegion': 'string',
        'Target': {
            'Type': 'ACCOUNT',
            'Id': 'string'
        },
        'RequestedTime': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --

HomeRegionControl (dict) --
This object is the HomeRegionControl object that\'s returned by a successful call to CreateHomeRegionControl .

ControlId (string) --
A unique identifier that\'s generated for each home region control. It\'s always a string that begins with "hrc-" followed by 12 lowercase letters and numbers.

HomeRegion (string) --
The AWS Region that\'s been set as home region. For example, "us-west-2" or "eu-central-1" are valid home regions.

Target (dict) --
The target parameter specifies the identifier to which the home region is applied, which is always an ACCOUNT . It applies the home region to the current ACCOUNT .

Type (string) --
The target type is always an ACCOUNT .

Id (string) --
The TargetID is a 12-character identifier of the ACCOUNT for which the control was created. (This must be the current account.)



RequestedTime (datetime) --
A timestamp representing the time when the customer called CreateHomeregionControl and set the home region for the account.









Exceptions

MigrationHubConfig.Client.exceptions.InternalServerError
MigrationHubConfig.Client.exceptions.ServiceUnavailableException
MigrationHubConfig.Client.exceptions.AccessDeniedException
MigrationHubConfig.Client.exceptions.ThrottlingException
MigrationHubConfig.Client.exceptions.DryRunOperation
MigrationHubConfig.Client.exceptions.InvalidInputException


    :return: {
        'HomeRegionControl': {
            'ControlId': 'string',
            'HomeRegion': 'string',
            'Target': {
                'Type': 'ACCOUNT',
                'Id': 'string'
            },
            'RequestedTime': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    MigrationHubConfig.Client.exceptions.InternalServerError
    MigrationHubConfig.Client.exceptions.ServiceUnavailableException
    MigrationHubConfig.Client.exceptions.AccessDeniedException
    MigrationHubConfig.Client.exceptions.ThrottlingException
    MigrationHubConfig.Client.exceptions.DryRunOperation
    MigrationHubConfig.Client.exceptions.InvalidInputException
    
    """
    pass

def describe_home_region_controls(ControlId=None, HomeRegion=None, Target=None, MaxResults=None, NextToken=None):
    """
    This API permits filtering on the ControlId and HomeRegion fields.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_home_region_controls(
        ControlId='string',
        HomeRegion='string',
        Target={
            'Type': 'ACCOUNT',
            'Id': 'string'
        },
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type ControlId: string
    :param ControlId: The ControlID is a unique identifier string of your HomeRegionControl object.

    :type HomeRegion: string
    :param HomeRegion: The name of the home region you\'d like to view.

    :type Target: dict
    :param Target: The target parameter specifies the identifier to which the home region is applied, which is always of type ACCOUNT . It applies the home region to the current ACCOUNT .\n\nType (string) -- [REQUIRED]The target type is always an ACCOUNT .\n\nId (string) --The TargetID is a 12-character identifier of the ACCOUNT for which the control was created. (This must be the current account.)\n\n\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of filtering results to display per page.

    :type NextToken: string
    :param NextToken: If a NextToken was returned by a previous call, more results are available. To retrieve the next page of results, make the call again using the returned token in NextToken .

    :rtype: dict

ReturnsResponse Syntax
{
    'HomeRegionControls': [
        {
            'ControlId': 'string',
            'HomeRegion': 'string',
            'Target': {
                'Type': 'ACCOUNT',
                'Id': 'string'
            },
            'RequestedTime': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

HomeRegionControls (list) --
An array that contains your HomeRegionControl objects.

(dict) --
A home region control is an object that specifies the home region for an account, with some additional information. It contains a target (always of type ACCOUNT ), an ID, and a time at which the home region was set.

ControlId (string) --
A unique identifier that\'s generated for each home region control. It\'s always a string that begins with "hrc-" followed by 12 lowercase letters and numbers.

HomeRegion (string) --
The AWS Region that\'s been set as home region. For example, "us-west-2" or "eu-central-1" are valid home regions.

Target (dict) --
The target parameter specifies the identifier to which the home region is applied, which is always an ACCOUNT . It applies the home region to the current ACCOUNT .

Type (string) --
The target type is always an ACCOUNT .

Id (string) --
The TargetID is a 12-character identifier of the ACCOUNT for which the control was created. (This must be the current account.)



RequestedTime (datetime) --
A timestamp representing the time when the customer called CreateHomeregionControl and set the home region for the account.





NextToken (string) --
If a NextToken was returned by a previous call, more results are available. To retrieve the next page of results, make the call again using the returned token in NextToken .







Exceptions

MigrationHubConfig.Client.exceptions.InternalServerError
MigrationHubConfig.Client.exceptions.ServiceUnavailableException
MigrationHubConfig.Client.exceptions.AccessDeniedException
MigrationHubConfig.Client.exceptions.ThrottlingException
MigrationHubConfig.Client.exceptions.InvalidInputException


    :return: {
        'HomeRegionControls': [
            {
                'ControlId': 'string',
                'HomeRegion': 'string',
                'Target': {
                    'Type': 'ACCOUNT',
                    'Id': 'string'
                },
                'RequestedTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    MigrationHubConfig.Client.exceptions.InternalServerError
    MigrationHubConfig.Client.exceptions.ServiceUnavailableException
    MigrationHubConfig.Client.exceptions.AccessDeniedException
    MigrationHubConfig.Client.exceptions.ThrottlingException
    MigrationHubConfig.Client.exceptions.InvalidInputException
    
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

def get_home_region():
    """
    Returns the calling account\xe2\x80\x99s home region, if configured. This API is used by other AWS services to determine the regional endpoint for calling AWS Application Discovery Service and Migration Hub. You must call GetHomeRegion at least once before you call any other AWS Application Discovery Service and AWS Migration Hub APIs, to obtain the account\'s Migration Hub home region.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_home_region()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'HomeRegion': 'string'
}


Response Structure

(dict) --
HomeRegion (string) --The name of the home region of the calling account.






Exceptions

MigrationHubConfig.Client.exceptions.InternalServerError
MigrationHubConfig.Client.exceptions.ServiceUnavailableException
MigrationHubConfig.Client.exceptions.AccessDeniedException
MigrationHubConfig.Client.exceptions.ThrottlingException
MigrationHubConfig.Client.exceptions.InvalidInputException


    :return: {
        'HomeRegion': 'string'
    }
    
    
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

