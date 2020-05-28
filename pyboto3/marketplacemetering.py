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

def batch_meter_usage(UsageRecords=None, ProductCode=None):
    """
    BatchMeter is called from a SaaS application listed on the AWS Marketplace to post metering records for a set of customers.
    For identical requests, the API is idempotent; requests can be retried with the same records or a subset of the input records.
    Every request to BatchMeter is for one product. If you need to meter usage for multiple products, you must make multiple calls to BatchMeterUsage.
    BatchMeterUsage can process up to 25 UsageRecords at a time.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_meter_usage(
        UsageRecords=[
            {
                'Timestamp': datetime(2015, 1, 1),
                'CustomerIdentifier': 'string',
                'Dimension': 'string',
                'Quantity': 123
            },
        ],
        ProductCode='string'
    )
    
    
    :type UsageRecords: list
    :param UsageRecords: [REQUIRED]\nThe set of UsageRecords to submit. BatchMeterUsage accepts up to 25 UsageRecords at a time.\n\n(dict) --A UsageRecord indicates a quantity of usage for a given product, customer, dimension and time.\nMultiple requests with the same UsageRecords as input will be deduplicated to prevent double charges.\n\nTimestamp (datetime) -- [REQUIRED]Timestamp, in UTC, for which the usage is being reported.\nYour application can meter usage for up to one hour in the past. Make sure the timestamp value is not before the start of the software usage.\n\nCustomerIdentifier (string) -- [REQUIRED]The CustomerIdentifier is obtained through the ResolveCustomer operation and represents an individual buyer in your application.\n\nDimension (string) -- [REQUIRED]During the process of registering a product on AWS Marketplace, up to eight dimensions are specified. These represent different units of value in your application.\n\nQuantity (integer) --The quantity of usage consumed by the customer for the given dimension and time. Defaults to 0 if not specified.\n\n\n\n\n

    :type ProductCode: string
    :param ProductCode: [REQUIRED]\nProduct code is used to uniquely identify a product in AWS Marketplace. The product code should be the same as the one used during the publishing of a new product.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Results': [
        {
            'UsageRecord': {
                'Timestamp': datetime(2015, 1, 1),
                'CustomerIdentifier': 'string',
                'Dimension': 'string',
                'Quantity': 123
            },
            'MeteringRecordId': 'string',
            'Status': 'Success'|'CustomerNotSubscribed'|'DuplicateRecord'
        },
    ],
    'UnprocessedRecords': [
        {
            'Timestamp': datetime(2015, 1, 1),
            'CustomerIdentifier': 'string',
            'Dimension': 'string',
            'Quantity': 123
        },
    ]
}


Response Structure

(dict) --
Contains the UsageRecords processed by BatchMeterUsage and any records that have failed due to transient error.

Results (list) --
Contains all UsageRecords processed by BatchMeterUsage. These records were either honored by AWS Marketplace Metering Service or were invalid.

(dict) --
A UsageRecordResult indicates the status of a given UsageRecord processed by BatchMeterUsage.

UsageRecord (dict) --
The UsageRecord that was part of the BatchMeterUsage request.

Timestamp (datetime) --
Timestamp, in UTC, for which the usage is being reported.
Your application can meter usage for up to one hour in the past. Make sure the timestamp value is not before the start of the software usage.

CustomerIdentifier (string) --
The CustomerIdentifier is obtained through the ResolveCustomer operation and represents an individual buyer in your application.

Dimension (string) --
During the process of registering a product on AWS Marketplace, up to eight dimensions are specified. These represent different units of value in your application.

Quantity (integer) --
The quantity of usage consumed by the customer for the given dimension and time. Defaults to 0 if not specified.



MeteringRecordId (string) --
The MeteringRecordId is a unique identifier for this metering event.

Status (string) --
The UsageRecordResult Status indicates the status of an individual UsageRecord processed by BatchMeterUsage.

Success - The UsageRecord was accepted and honored by BatchMeterUsage.
CustomerNotSubscribed - The CustomerIdentifier specified is not subscribed to your product. The UsageRecord was not honored. Future UsageRecords for this customer will fail until the customer subscribes to your product.
DuplicateRecord - Indicates that the UsageRecord was invalid and not honored. A previously metered UsageRecord had the same customer, dimension, and time, but a different quantity.






UnprocessedRecords (list) --
Contains all UsageRecords that were not processed by BatchMeterUsage. This is a list of UsageRecords. You can retry the failed request by making another BatchMeterUsage call with this list as input in the BatchMeterUsageRequest.

(dict) --
A UsageRecord indicates a quantity of usage for a given product, customer, dimension and time.
Multiple requests with the same UsageRecords as input will be deduplicated to prevent double charges.

Timestamp (datetime) --
Timestamp, in UTC, for which the usage is being reported.
Your application can meter usage for up to one hour in the past. Make sure the timestamp value is not before the start of the software usage.

CustomerIdentifier (string) --
The CustomerIdentifier is obtained through the ResolveCustomer operation and represents an individual buyer in your application.

Dimension (string) --
During the process of registering a product on AWS Marketplace, up to eight dimensions are specified. These represent different units of value in your application.

Quantity (integer) --
The quantity of usage consumed by the customer for the given dimension and time. Defaults to 0 if not specified.











Exceptions

MarketplaceMetering.Client.exceptions.InternalServiceErrorException
MarketplaceMetering.Client.exceptions.InvalidProductCodeException
MarketplaceMetering.Client.exceptions.InvalidUsageDimensionException
MarketplaceMetering.Client.exceptions.InvalidCustomerIdentifierException
MarketplaceMetering.Client.exceptions.TimestampOutOfBoundsException
MarketplaceMetering.Client.exceptions.ThrottlingException
MarketplaceMetering.Client.exceptions.DisabledApiException


    :return: {
        'Results': [
            {
                'UsageRecord': {
                    'Timestamp': datetime(2015, 1, 1),
                    'CustomerIdentifier': 'string',
                    'Dimension': 'string',
                    'Quantity': 123
                },
                'MeteringRecordId': 'string',
                'Status': 'Success'|'CustomerNotSubscribed'|'DuplicateRecord'
            },
        ],
        'UnprocessedRecords': [
            {
                'Timestamp': datetime(2015, 1, 1),
                'CustomerIdentifier': 'string',
                'Dimension': 'string',
                'Quantity': 123
            },
        ]
    }
    
    
    :returns: 
    Success - The UsageRecord was accepted and honored by BatchMeterUsage.
    CustomerNotSubscribed - The CustomerIdentifier specified is not subscribed to your product. The UsageRecord was not honored. Future UsageRecords for this customer will fail until the customer subscribes to your product.
    DuplicateRecord - Indicates that the UsageRecord was invalid and not honored. A previously metered UsageRecord had the same customer, dimension, and time, but a different quantity.
    
    """
    pass

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

def meter_usage(ProductCode=None, Timestamp=None, UsageDimension=None, UsageQuantity=None, DryRun=None):
    """
    API to emit metering records. For identical requests, the API is idempotent. It simply returns the metering record ID.
    Meter is authenticated on the buyer\'s AWS account using credentials from the EC2 instance, ECS task, or EKS pod.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.meter_usage(
        ProductCode='string',
        Timestamp=datetime(2015, 1, 1),
        UsageDimension='string',
        UsageQuantity=123,
        DryRun=True|False
    )
    
    
    :type ProductCode: string
    :param ProductCode: [REQUIRED]\nProduct code is used to uniquely identify a product in AWS Marketplace. The product code should be the same as the one used during the publishing of a new product.\n

    :type Timestamp: datetime
    :param Timestamp: [REQUIRED]\nTimestamp, in UTC, for which the usage is being reported. Your application can meter usage for up to one hour in the past. Make sure the timestamp value is not before the start of the software usage.\n

    :type UsageDimension: string
    :param UsageDimension: [REQUIRED]\nIt will be one of the fcp dimension name provided during the publishing of the product.\n

    :type UsageQuantity: integer
    :param UsageQuantity: Consumption value for the hour. Defaults to 0 if not specified.

    :type DryRun: boolean
    :param DryRun: Checks whether you have the permissions required for the action, but does not make the request. If you have the permissions, the request returns DryRunOperation; otherwise, it returns UnauthorizedException. Defaults to false if not specified.

    :rtype: dict

ReturnsResponse Syntax
{
    'MeteringRecordId': 'string'
}


Response Structure

(dict) --

MeteringRecordId (string) --
Metering record id.







Exceptions

MarketplaceMetering.Client.exceptions.InternalServiceErrorException
MarketplaceMetering.Client.exceptions.InvalidProductCodeException
MarketplaceMetering.Client.exceptions.InvalidUsageDimensionException
MarketplaceMetering.Client.exceptions.InvalidEndpointRegionException
MarketplaceMetering.Client.exceptions.TimestampOutOfBoundsException
MarketplaceMetering.Client.exceptions.DuplicateRequestException
MarketplaceMetering.Client.exceptions.ThrottlingException
MarketplaceMetering.Client.exceptions.CustomerNotEntitledException


    :return: {
        'MeteringRecordId': 'string'
    }
    
    
    :returns: 
    MarketplaceMetering.Client.exceptions.InternalServiceErrorException
    MarketplaceMetering.Client.exceptions.InvalidProductCodeException
    MarketplaceMetering.Client.exceptions.InvalidUsageDimensionException
    MarketplaceMetering.Client.exceptions.InvalidEndpointRegionException
    MarketplaceMetering.Client.exceptions.TimestampOutOfBoundsException
    MarketplaceMetering.Client.exceptions.DuplicateRequestException
    MarketplaceMetering.Client.exceptions.ThrottlingException
    MarketplaceMetering.Client.exceptions.CustomerNotEntitledException
    
    """
    pass

def register_usage(ProductCode=None, PublicKeyVersion=None, Nonce=None):
    """
    Paid container software products sold through AWS Marketplace must integrate with the AWS Marketplace Metering Service and call the Register operation for software entitlement and metering. Free and BYOL products for Amazon ECS or Amazon EKS aren\'t required to call Register, but you may choose to do so if you would like to receive usage data in your seller reports. The sections below explain the behavior of RegisterUsage. RegisterUsage performs two primary functions: metering and entitlement.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.register_usage(
        ProductCode='string',
        PublicKeyVersion=123,
        Nonce='string'
    )
    
    
    :type ProductCode: string
    :param ProductCode: [REQUIRED]\nProduct code is used to uniquely identify a product in AWS Marketplace. The product code should be the same as the one used during the publishing of a new product.\n

    :type PublicKeyVersion: integer
    :param PublicKeyVersion: [REQUIRED]\nPublic Key Version provided by AWS Marketplace\n

    :type Nonce: string
    :param Nonce: (Optional) To scope down the registration to a specific running software instance and guard against replay attacks.

    :rtype: dict

ReturnsResponse Syntax
{
    'PublicKeyRotationTimestamp': datetime(2015, 1, 1),
    'Signature': 'string'
}


Response Structure

(dict) --

PublicKeyRotationTimestamp (datetime) --
(Optional) Only included when public key version has expired

Signature (string) --
JWT Token







Exceptions

MarketplaceMetering.Client.exceptions.InvalidProductCodeException
MarketplaceMetering.Client.exceptions.InvalidRegionException
MarketplaceMetering.Client.exceptions.InvalidPublicKeyVersionException
MarketplaceMetering.Client.exceptions.PlatformNotSupportedException
MarketplaceMetering.Client.exceptions.CustomerNotEntitledException
MarketplaceMetering.Client.exceptions.ThrottlingException
MarketplaceMetering.Client.exceptions.InternalServiceErrorException
MarketplaceMetering.Client.exceptions.DisabledApiException


    :return: {
        'PublicKeyRotationTimestamp': datetime(2015, 1, 1),
        'Signature': 'string'
    }
    
    
    :returns: 
    ProductCode (string) -- [REQUIRED]
    Product code is used to uniquely identify a product in AWS Marketplace. The product code should be the same as the one used during the publishing of a new product.
    
    PublicKeyVersion (integer) -- [REQUIRED]
    Public Key Version provided by AWS Marketplace
    
    Nonce (string) -- (Optional) To scope down the registration to a specific running software instance and guard against replay attacks.
    
    """
    pass

def resolve_customer(RegistrationToken=None):
    """
    ResolveCustomer is called by a SaaS application during the registration process. When a buyer visits your website during the registration process, the buyer submits a registration token through their browser. The registration token is resolved through this API to obtain a CustomerIdentifier and product code.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.resolve_customer(
        RegistrationToken='string'
    )
    
    
    :type RegistrationToken: string
    :param RegistrationToken: [REQUIRED]\nWhen a buyer visits your website during the registration process, the buyer submits a registration token through the browser. The registration token is resolved to obtain a CustomerIdentifier and product code.\n

    :rtype: dict
ReturnsResponse Syntax{
    'CustomerIdentifier': 'string',
    'ProductCode': 'string'
}


Response Structure

(dict) --The result of the ResolveCustomer operation. Contains the CustomerIdentifier and product code.

CustomerIdentifier (string) --The CustomerIdentifier is used to identify an individual customer in your application. Calls to BatchMeterUsage require CustomerIdentifiers for each UsageRecord.

ProductCode (string) --The product code is returned to confirm that the buyer is registering for your product. Subsequent BatchMeterUsage calls should be made using this product code.






Exceptions

MarketplaceMetering.Client.exceptions.InvalidTokenException
MarketplaceMetering.Client.exceptions.ExpiredTokenException
MarketplaceMetering.Client.exceptions.ThrottlingException
MarketplaceMetering.Client.exceptions.InternalServiceErrorException
MarketplaceMetering.Client.exceptions.DisabledApiException


    :return: {
        'CustomerIdentifier': 'string',
        'ProductCode': 'string'
    }
    
    
    """
    pass

