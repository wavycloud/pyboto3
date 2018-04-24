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

def describe_services(ServiceCode=None, FormatVersion=None, NextToken=None, MaxResults=None):
    """
    Returns the metadata for one service or a list of the metadata for all services. Use this without a service code to get the service codes for all services. Use it with a service code, such as AmazonEC2 , to get information specific to that service, such as the attribute names available for that service. For example, some of the attribute names available for EC2 are volumeType , maxIopsVolume , operation , locationType , and instanceCapacity10xlarge .
    See also: AWS API Documentation
    
    
    :example: response = client.describe_services(
        ServiceCode='string',
        FormatVersion='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type ServiceCode: string
    :param ServiceCode: The code for the service whose information you want to retrieve, such as AmazonEC2 . You can use the ServiceCode to filter the results in a GetProducts call. To retrieve a list of all services, leave this blank.

    :type FormatVersion: string
    :param FormatVersion: The format version that you want the response to be in.
            Valid values are: aws_v1
            

    :type NextToken: string
    :param NextToken: The pagination token that indicates the next set of results that you want to retrieve.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results that you want returned in the response.

    :rtype: dict
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

def get_attribute_values(ServiceCode=None, AttributeName=None, NextToken=None, MaxResults=None):
    """
    Returns a list of attribute values. Attibutes are similar to the details in a Price List API offer file. For a list of available attributes, see Offer File Definitions in the AWS Billing and Cost Management User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.get_attribute_values(
        ServiceCode='string',
        AttributeName='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type ServiceCode: string
    :param ServiceCode: [REQUIRED]
            The service code for the service whose attributes you want to retrieve. For example, if you want the retrieve an EC2 attribute, use AmazonEC2 .
            

    :type AttributeName: string
    :param AttributeName: [REQUIRED]
            The name of the attribute that you want to retrieve the values for, such as volumeType .
            

    :type NextToken: string
    :param NextToken: The pagination token that indicates the next set of results that you want to retrieve.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in response.

    :rtype: dict
    :return: {
        'AttributeValues': [
            {
                'Value': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
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

def get_products(ServiceCode=None, Filters=None, FormatVersion=None, NextToken=None, MaxResults=None):
    """
    Returns a list of all products that match the filter criteria.
    See also: AWS API Documentation
    
    
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
    :param Filters: The list of filters that limit the returned products. only products that match all filters are returned.
            (dict) --The constraints that you want all returned products to match.
            Type (string) -- [REQUIRED]The type of filter that you want to use.
            Valid values are: TERM_MATCH . TERM_MATCH returns only products that match both the given filter field and the given value.
            Field (string) -- [REQUIRED]The product metadata field that you want to filter on. You can filter by just the service code to see all products for a specific service, filter by just the attribute name to see a specific attribute for multiple services, or use both a service code and an attribute name to retrieve only products that match both fields.
            Valid values include: ServiceCode , and all attribute names
            For example, you can filter by the AmazonEC2 service code and the volumeType attribute name to get the prices for only Amazon EC2 volumes.
            Value (string) -- [REQUIRED]The service code or attribute value that you want to filter by. If you are filtering by service code this is the actual service code, such as AmazonEC2 . If you are filtering by attribute name, this is the attribute value that you want the returned products to match, such as a Provisioned IOPS volume.
            
            

    :type FormatVersion: string
    :param FormatVersion: The format version that you want the response to be in.
            Valid values are: aws_v1
            

    :type NextToken: string
    :param NextToken: The pagination token that indicates the next set of results that you want to retrieve.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in the response.

    :rtype: dict
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

def get_waiter():
    """
    
    """
    pass

