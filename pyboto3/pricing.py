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

def describe_services(ServiceCode=None, FormatVersion=None, NextToken=None, MaxResults=None):
    """
    Returns the metadata for one service or a list of the metadata for all services. Use this without a service code to get the service codes for all services. Use it with a service code, such as AmazonEC2 , to get information specific to that service, such as the attribute names available for that service. For example, some of the attribute names available for EC2 are volumeType , maxIopsVolume , operation , locationType , and instanceCapacity10xlarge .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Expected Output:
    
    :example: response = client.describe_services(
        ServiceCode='string',
        FormatVersion='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type ServiceCode: string
    :param ServiceCode: The code for the service whose information you want to retrieve, such as AmazonEC2 . You can use the ServiceCode to filter the results in a GetProducts call. To retrieve a list of all services, leave this blank.

    :type FormatVersion: string
    :param FormatVersion: The format version that you want the response to be in.\nValid values are: aws_v1\n

    :type NextToken: string
    :param NextToken: The pagination token that indicates the next set of results that you want to retrieve.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results that you want returned in the response.

    :rtype: dict

ReturnsResponse Syntax
{
    'Services': [
        {
            'ServiceCode': 'string',
            'AttributeNames': [
                'string',
            ]
        },
    ],
    'FormatVersion': 'string',
    'NextToken': 'string'
}


Response Structure

(dict) --

Services (list) --
The service metadata for the service or services in the response.

(dict) --
The metadata for a service, such as the service code and available attribute names.

ServiceCode (string) --
The code for the AWS service.

AttributeNames (list) --
The attributes that are available for this service.

(string) --






FormatVersion (string) --
The format version of the response. For example, aws_v1 .

NextToken (string) --
The pagination token for the next set of retreivable results.







Exceptions

Pricing.Client.exceptions.InternalErrorException
Pricing.Client.exceptions.InvalidParameterException
Pricing.Client.exceptions.NotFoundException
Pricing.Client.exceptions.InvalidNextTokenException
Pricing.Client.exceptions.ExpiredNextTokenException

Examples
response = client.describe_services(
    FormatVersion='aws_v1',
    MaxResults=1,
    ServiceCode='AmazonEC2',
)

print(response)


Expected Output:
{
    'FormatVersion': 'aws_v1',
    'NextToken': 'abcdefg123',
    'Services': [
        {
            'AttributeNames': [
                'volumeType',
                'maxIopsvolume',
                'instanceCapacity10xlarge',
                'locationType',
                'operation',
            ],
            'ServiceCode': 'AmazonEC2',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Services': [
            {
                'ServiceCode': 'string',
                'AttributeNames': [
                    'string',
                ]
            },
        ],
        'FormatVersion': 'string',
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
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

def get_attribute_values(ServiceCode=None, AttributeName=None, NextToken=None, MaxResults=None):
    """
    Returns a list of attribute values. Attibutes are similar to the details in a Price List API offer file. For a list of available attributes, see Offer File Definitions in the AWS Billing and Cost Management User Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This operation returns a list of values available for the given attribute.
    Expected Output:
    
    :example: response = client.get_attribute_values(
        ServiceCode='string',
        AttributeName='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type ServiceCode: string
    :param ServiceCode: [REQUIRED]\nThe service code for the service whose attributes you want to retrieve. For example, if you want the retrieve an EC2 attribute, use AmazonEC2 .\n

    :type AttributeName: string
    :param AttributeName: [REQUIRED]\nThe name of the attribute that you want to retrieve the values for, such as volumeType .\n

    :type NextToken: string
    :param NextToken: The pagination token that indicates the next set of results that you want to retrieve.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in response.

    :rtype: dict

ReturnsResponse Syntax
{
    'AttributeValues': [
        {
            'Value': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

AttributeValues (list) --
The list of values for an attribute. For example, Throughput Optimized HDD and Provisioned IOPS are two available values for the AmazonEC2 volumeType .

(dict) --
The values of a given attribute, such as Throughput Optimized HDD or Provisioned IOPS for the Amazon EC2 volumeType attribute.

Value (string) --
The specific value of an attributeName .





NextToken (string) --
The pagination token that indicates the next set of results to retrieve.







Exceptions

Pricing.Client.exceptions.InternalErrorException
Pricing.Client.exceptions.InvalidParameterException
Pricing.Client.exceptions.NotFoundException
Pricing.Client.exceptions.InvalidNextTokenException
Pricing.Client.exceptions.ExpiredNextTokenException

Examples
This operation returns a list of values available for the given attribute.
response = client.get_attribute_values(
    AttributeName='volumeType',
    MaxResults=2,
    ServiceCode='AmazonEC2',
)

print(response)


Expected Output:
{
    'AttributeValues': [
        {
            'Value': 'Throughput Optimized HDD',
        },
        {
            'Value': 'Provisioned IOPS',
        },
    ],
    'NextToken': 'GpgauEXAMPLEezucl5LV0w==:7GzYJ0nw0DBTJ2J66EoTIIynE6O1uXwQtTRqioJzQadBnDVgHPzI1en4BUQnPCLpzeBk9RQQAWaFieA4+DapFAGLgk+Z/9/cTw9GldnPOHN98+FdmJP7wKU3QQpQ8MQr5KOeBkIsAqvAQYdL0DkL7tHwPtE5iCEByAmg9gcC/yBU1vAOsf7R3VaNN4M5jMDv3woSWqASSIlBVB6tgW78YL22KhssoItM/jWW+aP6Jqtq4mldxp/ct6DWAl+xLFwHU/CbketimPPXyqHF3/UXDw==',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'AttributeValues': [
            {
                'Value': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Pricing.Client.exceptions.InternalErrorException
    Pricing.Client.exceptions.InvalidParameterException
    Pricing.Client.exceptions.NotFoundException
    Pricing.Client.exceptions.InvalidNextTokenException
    Pricing.Client.exceptions.ExpiredNextTokenException
    
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

def get_products(ServiceCode=None, Filters=None, FormatVersion=None, NextToken=None, MaxResults=None):
    """
    Returns a list of all products that match the filter criteria.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This operation returns a list of products that match the given criteria.
    Expected Output:
    
    :example: response = client.get_products(
        ServiceCode='string',
        Filters=[
            {
                'Type': 'TERM_MATCH',
                'Field': 'string',
                'Value': 'string'
            },
        ],
        FormatVersion='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type ServiceCode: string
    :param ServiceCode: The code for the service whose products you want to retrieve.

    :type Filters: list
    :param Filters: The list of filters that limit the returned products. only products that match all filters are returned.\n\n(dict) --The constraints that you want all returned products to match.\n\nType (string) -- [REQUIRED]The type of filter that you want to use.\nValid values are: TERM_MATCH . TERM_MATCH returns only products that match both the given filter field and the given value.\n\nField (string) -- [REQUIRED]The product metadata field that you want to filter on. You can filter by just the service code to see all products for a specific service, filter by just the attribute name to see a specific attribute for multiple services, or use both a service code and an attribute name to retrieve only products that match both fields.\nValid values include: ServiceCode , and all attribute names\nFor example, you can filter by the AmazonEC2 service code and the volumeType attribute name to get the prices for only Amazon EC2 volumes.\n\nValue (string) -- [REQUIRED]The service code or attribute value that you want to filter by. If you are filtering by service code this is the actual service code, such as AmazonEC2 . If you are filtering by attribute name, this is the attribute value that you want the returned products to match, such as a Provisioned IOPS volume.\n\n\n\n\n

    :type FormatVersion: string
    :param FormatVersion: The format version that you want the response to be in.\nValid values are: aws_v1\n

    :type NextToken: string
    :param NextToken: The pagination token that indicates the next set of results that you want to retrieve.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in the response.

    :rtype: dict

ReturnsResponse Syntax
{
    'FormatVersion': 'string',
    'PriceList': [
        'string',
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

FormatVersion (string) --
The format version of the response. For example, aws_v1.

PriceList (list) --
The list of products that match your filters. The list contains both the product metadata and the price information.

(string) --


NextToken (string) --
The pagination token that indicates the next set of results to retrieve.







Exceptions

Pricing.Client.exceptions.InternalErrorException
Pricing.Client.exceptions.InvalidParameterException
Pricing.Client.exceptions.NotFoundException
Pricing.Client.exceptions.InvalidNextTokenException
Pricing.Client.exceptions.ExpiredNextTokenException

Examples
This operation returns a list of products that match the given criteria.
response = client.get_products(
    Filters=[
        {
            'Field': 'ServiceCode',
            'Type': 'TERM_MATCH',
            'Value': 'AmazonEC2',
        },
        {
            'Field': 'volumeType',
            'Type': 'TERM_MATCH',
            'Value': 'Provisioned IOPS',
        },
    ],
    FormatVersion='aws_v1',
    MaxResults=1,
)

print(response)


Expected Output:
{
    'FormatVersion': 'aws_v1',
    'NextToken': '57r3EXAMPLEujbzWfHF7Ciw==:ywSmZsD3mtpQmQLQ5XfOsIMkYybSj+vAT+kGmwMFq+K9DGmIoJkz7lunVeamiOPgthdWSO2a7YKojCO+zY4dJmuNl2QvbNhXs+AJ2Ufn7xGmJncNI2TsEuAsVCUfTAvAQNcwwamtk6XuZ4YdNnooV62FjkV3ZAn40d9+wAxV7+FImvhUHi/+f8afgZdGh2zPUlH8jlV9uUtj0oHp8+DhPUuHXh+WBII1E/aoKpPSm3c=',
    'PriceList': [
        '{"product":{"productFamily":"Storage","attributes":{"storageMedia":"SSD-backed","maxThroughputvolume":"320 MB/sec","volumeType":"Provisioned IOPS","maxIopsvolume":"20000","servicecode":"AmazonEC2","usagetype":"CAN1-EBS:VolumeUsage.piops","locationType":"AWS Region","location":"Canada (Central)","servicename":"Amazon Elastic Compute Cloud","maxVolumeSize":"16 TiB","operation":""},"sku":"WQGC34PB2AWS8R4U"},"serviceCode":"AmazonEC2","terms":{"OnDemand":{"WQGC34PB2AWS8R4U.JRTCKXETXF":{"priceDimensions":{"WQGC34PB2AWS8R4U.JRTCKXETXF.6YS6EN2CT7":{"unit":"GB-Mo","endRange":"Inf","description":"$0.138 per GB-month of Provisioned IOPS SSD (io1)  provisioned storage - Canada (Central)","appliesTo":[],"rateCode":"WQGC34PB2AWS8R4U.JRTCKXETXF.6YS6EN2CT7","beginRange":"0","pricePerUnit":{"USD":"0.1380000000"}}},"sku":"WQGC34PB2AWS8R4U","effectiveDate":"2017-08-01T00:00:00Z","offerTermCode":"JRTCKXETXF","termAttributes":{}}}},"version":"20170901182201","publicationDate":"2017-09-01T18:22:01Z"}',
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'FormatVersion': 'string',
        'PriceList': [
            'string',
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
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

