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

def get_entitlements(ProductCode=None, Filter=None, NextToken=None, MaxResults=None):
    """
    GetEntitlements retrieves entitlement values for a given product. The results can be filtered based on customer identifier or product dimensions.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_entitlements(
        ProductCode='string',
        Filter={
            'string': [
                'string',
            ]
        },
        NextToken='string',
        MaxResults=123
    )
    
    
    :type ProductCode: string
    :param ProductCode: [REQUIRED]\nProduct code is used to uniquely identify a product in AWS Marketplace. The product code will be provided by AWS Marketplace when the product listing is created.\n

    :type Filter: dict
    :param Filter: Filter is used to return entitlements for a specific customer or for a specific dimension. Filters are described as keys mapped to a lists of values. Filtered requests are unioned for each value in the value list, and then intersected for each filter key.\n\n(string) --\n(list) --\n(string) --\n\n\n\n\n\n

    :type NextToken: string
    :param NextToken: For paginated calls to GetEntitlements, pass the NextToken from the previous GetEntitlementsResult.

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to retrieve from the GetEntitlements operation. For pagination, use the NextToken field in subsequent calls to GetEntitlements.

    :rtype: dict

ReturnsResponse Syntax
{
    'Entitlements': [
        {
            'ProductCode': 'string',
            'Dimension': 'string',
            'CustomerIdentifier': 'string',
            'Value': {
                'IntegerValue': 123,
                'DoubleValue': 123.0,
                'BooleanValue': True|False,
                'StringValue': 'string'
            },
            'ExpirationDate': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
The GetEntitlementsRequest contains results from the GetEntitlements operation.

Entitlements (list) --
The set of entitlements found through the GetEntitlements operation. If the result contains an empty set of entitlements, NextToken might still be present and should be used.

(dict) --
An entitlement represents capacity in a product owned by the customer. For example, a customer might own some number of users or seats in an SaaS application or some amount of data capacity in a multi-tenant database.

ProductCode (string) --
The product code for which the given entitlement applies. Product codes are provided by AWS Marketplace when the product listing is created.

Dimension (string) --
The dimension for which the given entitlement applies. Dimensions represent categories of capacity in a product and are specified when the product is listed in AWS Marketplace.

CustomerIdentifier (string) --
The customer identifier is a handle to each unique customer in an application. Customer identifiers are obtained through the ResolveCustomer operation in AWS Marketplace Metering Service.

Value (dict) --
The EntitlementValue represents the amount of capacity that the customer is entitled to for the product.

IntegerValue (integer) --
The IntegerValue field will be populated with an integer value when the entitlement is an integer type. Otherwise, the field will not be set.

DoubleValue (float) --
The DoubleValue field will be populated with a double value when the entitlement is a double type. Otherwise, the field will not be set.

BooleanValue (boolean) --
The BooleanValue field will be populated with a boolean value when the entitlement is a boolean type. Otherwise, the field will not be set.

StringValue (string) --
The StringValue field will be populated with a string value when the entitlement is a string type. Otherwise, the field will not be set.



ExpirationDate (datetime) --
The expiration date represents the minimum date through which this entitlement is expected to remain valid. For contractual products listed on AWS Marketplace, the expiration date is the date at which the customer will renew or cancel their contract. Customers who are opting to renew their contract will still have entitlements with an expiration date.





NextToken (string) --
For paginated results, use NextToken in subsequent calls to GetEntitlements. If the result contains an empty set of entitlements, NextToken might still be present and should be used.







Exceptions

MarketplaceEntitlementService.Client.exceptions.InvalidParameterException
MarketplaceEntitlementService.Client.exceptions.ThrottlingException
MarketplaceEntitlementService.Client.exceptions.InternalServiceErrorException


    :return: {
        'Entitlements': [
            {
                'ProductCode': 'string',
                'Dimension': 'string',
                'CustomerIdentifier': 'string',
                'Value': {
                    'IntegerValue': 123,
                    'DoubleValue': 123.0,
                    'BooleanValue': True|False,
                    'StringValue': 'string'
                },
                'ExpirationDate': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    MarketplaceEntitlementService.Client.exceptions.InvalidParameterException
    MarketplaceEntitlementService.Client.exceptions.ThrottlingException
    MarketplaceEntitlementService.Client.exceptions.InternalServiceErrorException
    
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

