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

def create_outpost(Name=None, Description=None, SiteId=None, AvailabilityZone=None, AvailabilityZoneId=None):
    """
    Creates an Outpost.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_outpost(
        Name='string',
        Description='string',
        SiteId='string',
        AvailabilityZone='string',
        AvailabilityZoneId='string'
    )
    
    
    :type Name: string
    :param Name: The name of the Outpost.

    :type Description: string
    :param Description: The Outpost description.

    :type SiteId: string
    :param SiteId: [REQUIRED]\nThe ID of the site.\n

    :type AvailabilityZone: string
    :param AvailabilityZone: The Availability Zone.\nYou must specify AvailabilityZone or AvailabilityZoneId .\n

    :type AvailabilityZoneId: string
    :param AvailabilityZoneId: The ID of the Availability Zone.\nYou must specify AvailabilityZone or AvailabilityZoneId .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Outpost': {
        'OutpostId': 'string',
        'OwnerId': 'string',
        'OutpostArn': 'string',
        'SiteId': 'string',
        'Name': 'string',
        'Description': 'string',
        'LifeCycleStatus': 'string',
        'AvailabilityZone': 'string',
        'AvailabilityZoneId': 'string'
    }
}


Response Structure

(dict) --

Outpost (dict) --
Information about an Outpost.

OutpostId (string) --
The ID of the Outpost.

OwnerId (string) --
The AWS account ID of the Outpost owner.

OutpostArn (string) --
The Amazon Resource Name (ARN) of the Outpost.

SiteId (string) --
The ID of the site.

Name (string) --
The name of the Outpost.

Description (string) --
The Outpost description.

LifeCycleStatus (string) --
The life cycle status.

AvailabilityZone (string) --
The Availability Zone.
You must specify AvailabilityZone or AvailabilityZoneId .

AvailabilityZoneId (string) --
The ID of the Availability Zone.
You must specify AvailabilityZone or AvailabilityZoneId .









Exceptions

Outposts.Client.exceptions.ValidationException
Outposts.Client.exceptions.NotFoundException
Outposts.Client.exceptions.AccessDeniedException
Outposts.Client.exceptions.InternalServerException
Outposts.Client.exceptions.ServiceQuotaExceededException


    :return: {
        'Outpost': {
            'OutpostId': 'string',
            'OwnerId': 'string',
            'OutpostArn': 'string',
            'SiteId': 'string',
            'Name': 'string',
            'Description': 'string',
            'LifeCycleStatus': 'string',
            'AvailabilityZone': 'string',
            'AvailabilityZoneId': 'string'
        }
    }
    
    
    :returns: 
    Outposts.Client.exceptions.ValidationException
    Outposts.Client.exceptions.NotFoundException
    Outposts.Client.exceptions.AccessDeniedException
    Outposts.Client.exceptions.InternalServerException
    Outposts.Client.exceptions.ServiceQuotaExceededException
    
    """
    pass

def delete_outpost(OutpostId=None):
    """
    Deletes the Outpost.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_outpost(
        OutpostId='string'
    )
    
    
    :type OutpostId: string
    :param OutpostId: [REQUIRED]\nThe ID of the Outpost.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

Outposts.Client.exceptions.ValidationException
Outposts.Client.exceptions.NotFoundException
Outposts.Client.exceptions.AccessDeniedException
Outposts.Client.exceptions.InternalServerException


    :return: {}
    
    
    :returns: 
    Outposts.Client.exceptions.ValidationException
    Outposts.Client.exceptions.NotFoundException
    Outposts.Client.exceptions.AccessDeniedException
    Outposts.Client.exceptions.InternalServerException
    
    """
    pass

def delete_site(SiteId=None):
    """
    Deletes the site.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_site(
        SiteId='string'
    )
    
    
    :type SiteId: string
    :param SiteId: [REQUIRED]\nThe ID of the site.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

Outposts.Client.exceptions.ValidationException
Outposts.Client.exceptions.NotFoundException
Outposts.Client.exceptions.AccessDeniedException
Outposts.Client.exceptions.InternalServerException


    :return: {}
    
    
    :returns: 
    Outposts.Client.exceptions.ValidationException
    Outposts.Client.exceptions.NotFoundException
    Outposts.Client.exceptions.AccessDeniedException
    Outposts.Client.exceptions.InternalServerException
    
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

def get_outpost(OutpostId=None):
    """
    Gets information about the specified Outpost.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_outpost(
        OutpostId='string'
    )
    
    
    :type OutpostId: string
    :param OutpostId: [REQUIRED]\nThe ID of the Outpost.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Outpost': {
        'OutpostId': 'string',
        'OwnerId': 'string',
        'OutpostArn': 'string',
        'SiteId': 'string',
        'Name': 'string',
        'Description': 'string',
        'LifeCycleStatus': 'string',
        'AvailabilityZone': 'string',
        'AvailabilityZoneId': 'string'
    }
}


Response Structure

(dict) --
Outpost (dict) --Information about an Outpost.

OutpostId (string) --The ID of the Outpost.

OwnerId (string) --The AWS account ID of the Outpost owner.

OutpostArn (string) --The Amazon Resource Name (ARN) of the Outpost.

SiteId (string) --The ID of the site.

Name (string) --The name of the Outpost.

Description (string) --The Outpost description.

LifeCycleStatus (string) --The life cycle status.

AvailabilityZone (string) --The Availability Zone.
You must specify AvailabilityZone or AvailabilityZoneId .

AvailabilityZoneId (string) --The ID of the Availability Zone.
You must specify AvailabilityZone or AvailabilityZoneId .








Exceptions

Outposts.Client.exceptions.ValidationException
Outposts.Client.exceptions.NotFoundException
Outposts.Client.exceptions.AccessDeniedException
Outposts.Client.exceptions.InternalServerException


    :return: {
        'Outpost': {
            'OutpostId': 'string',
            'OwnerId': 'string',
            'OutpostArn': 'string',
            'SiteId': 'string',
            'Name': 'string',
            'Description': 'string',
            'LifeCycleStatus': 'string',
            'AvailabilityZone': 'string',
            'AvailabilityZoneId': 'string'
        }
    }
    
    
    """
    pass

def get_outpost_instance_types(OutpostId=None, NextToken=None, MaxResults=None):
    """
    Lists the instance types for the specified Outpost.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_outpost_instance_types(
        OutpostId='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type OutpostId: string
    :param OutpostId: [REQUIRED]\nThe ID of the Outpost.\n

    :type NextToken: string
    :param NextToken: The pagination token.

    :type MaxResults: integer
    :param MaxResults: The maximum page size.

    :rtype: dict

ReturnsResponse Syntax
{
    'InstanceTypes': [
        {
            'InstanceType': 'string'
        },
    ],
    'NextToken': 'string',
    'OutpostId': 'string',
    'OutpostArn': 'string'
}


Response Structure

(dict) --

InstanceTypes (list) --
Information about the instance types.

(dict) --
Information about an instance type.

InstanceType (string) --
The instance type.





NextToken (string) --
The pagination token.

OutpostId (string) --
The ID of the Outpost.

OutpostArn (string) --
The Amazon Resource Name (ARN) of the Outpost.







Exceptions

Outposts.Client.exceptions.ValidationException
Outposts.Client.exceptions.NotFoundException
Outposts.Client.exceptions.AccessDeniedException
Outposts.Client.exceptions.InternalServerException


    :return: {
        'InstanceTypes': [
            {
                'InstanceType': 'string'
            },
        ],
        'NextToken': 'string',
        'OutpostId': 'string',
        'OutpostArn': 'string'
    }
    
    
    :returns: 
    Outposts.Client.exceptions.ValidationException
    Outposts.Client.exceptions.NotFoundException
    Outposts.Client.exceptions.AccessDeniedException
    Outposts.Client.exceptions.InternalServerException
    
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

def list_outposts(NextToken=None, MaxResults=None):
    """
    List the Outposts for your AWS account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_outposts(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: The pagination token.

    :type MaxResults: integer
    :param MaxResults: The maximum page size.

    :rtype: dict

ReturnsResponse Syntax
{
    'Outposts': [
        {
            'OutpostId': 'string',
            'OwnerId': 'string',
            'OutpostArn': 'string',
            'SiteId': 'string',
            'Name': 'string',
            'Description': 'string',
            'LifeCycleStatus': 'string',
            'AvailabilityZone': 'string',
            'AvailabilityZoneId': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Outposts (list) --
Information about the Outposts.

(dict) --
Information about an Outpost.

OutpostId (string) --
The ID of the Outpost.

OwnerId (string) --
The AWS account ID of the Outpost owner.

OutpostArn (string) --
The Amazon Resource Name (ARN) of the Outpost.

SiteId (string) --
The ID of the site.

Name (string) --
The name of the Outpost.

Description (string) --
The Outpost description.

LifeCycleStatus (string) --
The life cycle status.

AvailabilityZone (string) --
The Availability Zone.
You must specify AvailabilityZone or AvailabilityZoneId .

AvailabilityZoneId (string) --
The ID of the Availability Zone.
You must specify AvailabilityZone or AvailabilityZoneId .





NextToken (string) --
The pagination token.







Exceptions

Outposts.Client.exceptions.ValidationException
Outposts.Client.exceptions.AccessDeniedException
Outposts.Client.exceptions.InternalServerException


    :return: {
        'Outposts': [
            {
                'OutpostId': 'string',
                'OwnerId': 'string',
                'OutpostArn': 'string',
                'SiteId': 'string',
                'Name': 'string',
                'Description': 'string',
                'LifeCycleStatus': 'string',
                'AvailabilityZone': 'string',
                'AvailabilityZoneId': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Outposts.Client.exceptions.ValidationException
    Outposts.Client.exceptions.AccessDeniedException
    Outposts.Client.exceptions.InternalServerException
    
    """
    pass

def list_sites(NextToken=None, MaxResults=None):
    """
    Lists the sites for the specified AWS account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_sites(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: The pagination token.

    :type MaxResults: integer
    :param MaxResults: The maximum page size.

    :rtype: dict

ReturnsResponse Syntax
{
    'Sites': [
        {
            'SiteId': 'string',
            'AccountId': 'string',
            'Name': 'string',
            'Description': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Sites (list) --
Information about the sites.

(dict) --
Information about a site.

SiteId (string) --
The ID of the site.

AccountId (string) --
The ID of the AWS account.

Name (string) --
The name of the site.

Description (string) --
The description of the site.





NextToken (string) --
The pagination token.







Exceptions

Outposts.Client.exceptions.ValidationException
Outposts.Client.exceptions.AccessDeniedException
Outposts.Client.exceptions.InternalServerException


    :return: {
        'Sites': [
            {
                'SiteId': 'string',
                'AccountId': 'string',
                'Name': 'string',
                'Description': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Outposts.Client.exceptions.ValidationException
    Outposts.Client.exceptions.AccessDeniedException
    Outposts.Client.exceptions.InternalServerException
    
    """
    pass

