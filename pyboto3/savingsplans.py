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

def create_savings_plan(savingsPlanOfferingId=None, commitment=None, upfrontPaymentAmount=None, clientToken=None, tags=None):
    """
    Creates a Savings Plan.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_savings_plan(
        savingsPlanOfferingId='string',
        commitment='string',
        upfrontPaymentAmount='string',
        clientToken='string',
        tags={
            'string': 'string'
        }
    )
    
    
    :type savingsPlanOfferingId: string
    :param savingsPlanOfferingId: [REQUIRED]\nThe ID of the offering.\n

    :type commitment: string
    :param commitment: [REQUIRED]\nThe hourly commitment, in USD. This is a value between 0.001 and 1 million. You cannot specify more than three digits after the decimal point.\n

    :type upfrontPaymentAmount: string
    :param upfrontPaymentAmount: The up-front payment amount. This is a whole number between 50 and 99 percent of the total value of the Savings Plan. This parameter is supported only if the payment option is Partial Upfront .

    :type clientToken: string
    :param clientToken: Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.\nThis field is autopopulated if not provided.\n

    :type tags: dict
    :param tags: One or more tags.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'savingsPlanId': 'string'
}


Response Structure

(dict) --

savingsPlanId (string) --
The ID of the Savings Plan.







Exceptions

SavingsPlans.Client.exceptions.ResourceNotFoundException
SavingsPlans.Client.exceptions.ValidationException
SavingsPlans.Client.exceptions.InternalServerException
SavingsPlans.Client.exceptions.ServiceQuotaExceededException


    :return: {
        'savingsPlanId': 'string'
    }
    
    
    :returns: 
    SavingsPlans.Client.exceptions.ResourceNotFoundException
    SavingsPlans.Client.exceptions.ValidationException
    SavingsPlans.Client.exceptions.InternalServerException
    SavingsPlans.Client.exceptions.ServiceQuotaExceededException
    
    """
    pass

def describe_savings_plan_rates(savingsPlanId=None, filters=None, nextToken=None, maxResults=None):
    """
    Describes the specified Savings Plans rates.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_savings_plan_rates(
        savingsPlanId='string',
        filters=[
            {
                'name': 'region'|'instanceType'|'productDescription'|'tenancy'|'productType'|'serviceCode'|'usageType'|'operation',
                'values': [
                    'string',
                ]
            },
        ],
        nextToken='string',
        maxResults=123
    )
    
    
    :type savingsPlanId: string
    :param savingsPlanId: [REQUIRED]\nThe ID of the Savings Plan.\n

    :type filters: list
    :param filters: The filters.\n\n(dict) --Information about a filter.\n\nname (string) --The filter name.\n\nvalues (list) --The filter values.\n\n(string) --\n\n\n\n\n\n

    :type nextToken: string
    :param nextToken: The token for the next page of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return with a single call. To retrieve additional results, make another call with the returned token value.

    :rtype: dict

ReturnsResponse Syntax
{
    'savingsPlanId': 'string',
    'searchResults': [
        {
            'rate': 'string',
            'currency': 'CNY'|'USD',
            'unit': 'Hrs'|'Lambda-GB-Second'|'Request',
            'productType': 'EC2'|'Fargate'|'Lambda',
            'serviceCode': 'AmazonEC2'|'AmazonECS'|'AWSLambda',
            'usageType': 'string',
            'operation': 'string',
            'properties': [
                {
                    'name': 'region'|'instanceType'|'instanceFamily'|'productDescription'|'tenancy',
                    'value': 'string'
                },
            ]
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

savingsPlanId (string) --
The ID of the Savings Plan.

searchResults (list) --
Information about the Savings Plans rates.

(dict) --
Information about a Savings Plan rate.

rate (string) --
The rate.

currency (string) --
The currency.

unit (string) --
The unit.

productType (string) --
The product type.

serviceCode (string) --
The service.

usageType (string) --
The usage details of the line item in the billing report.

operation (string) --
The specific AWS operation for the line item in the billing report.

properties (list) --
The properties.

(dict) --
Information about a property.

name (string) --
The property name.

value (string) --
The property value.









nextToken (string) --
The token to use to retrieve the next page of results. This value is null when there are no more results to return.







Exceptions

SavingsPlans.Client.exceptions.ResourceNotFoundException
SavingsPlans.Client.exceptions.ValidationException


    :return: {
        'savingsPlanId': 'string',
        'searchResults': [
            {
                'rate': 'string',
                'currency': 'CNY'|'USD',
                'unit': 'Hrs'|'Lambda-GB-Second'|'Request',
                'productType': 'EC2'|'Fargate'|'Lambda',
                'serviceCode': 'AmazonEC2'|'AmazonECS'|'AWSLambda',
                'usageType': 'string',
                'operation': 'string',
                'properties': [
                    {
                        'name': 'region'|'instanceType'|'instanceFamily'|'productDescription'|'tenancy',
                        'value': 'string'
                    },
                ]
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    SavingsPlans.Client.exceptions.ResourceNotFoundException
    SavingsPlans.Client.exceptions.ValidationException
    
    """
    pass

def describe_savings_plans(savingsPlanArns=None, savingsPlanIds=None, nextToken=None, maxResults=None, states=None, filters=None):
    """
    Describes the specified Savings Plans.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_savings_plans(
        savingsPlanArns=[
            'string',
        ],
        savingsPlanIds=[
            'string',
        ],
        nextToken='string',
        maxResults=123,
        states=[
            'payment-pending'|'payment-failed'|'active'|'retired',
        ],
        filters=[
            {
                'name': 'region'|'ec2-instance-family'|'commitment'|'upfront'|'term'|'savings-plan-type'|'payment-option'|'start'|'end',
                'values': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type savingsPlanArns: list
    :param savingsPlanArns: The Amazon Resource Names (ARN) of the Savings Plans.\n\n(string) --\n\n

    :type savingsPlanIds: list
    :param savingsPlanIds: The IDs of the Savings Plans.\n\n(string) --\n\n

    :type nextToken: string
    :param nextToken: The token for the next page of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return with a single call. To retrieve additional results, make another call with the returned token value.

    :type states: list
    :param states: The states.\n\n(string) --\n\n

    :type filters: list
    :param filters: The filters.\n\n(dict) --Information about a filter.\n\nname (string) --The filter name.\n\nvalues (list) --The filter value.\n\n(string) --\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'savingsPlans': [
        {
            'offeringId': 'string',
            'savingsPlanId': 'string',
            'savingsPlanArn': 'string',
            'description': 'string',
            'start': 'string',
            'end': 'string',
            'state': 'payment-pending'|'payment-failed'|'active'|'retired',
            'region': 'string',
            'ec2InstanceFamily': 'string',
            'savingsPlanType': 'Compute'|'EC2Instance',
            'paymentOption': 'All Upfront'|'Partial Upfront'|'No Upfront',
            'productTypes': [
                'EC2'|'Fargate'|'Lambda',
            ],
            'currency': 'CNY'|'USD',
            'commitment': 'string',
            'upfrontPaymentAmount': 'string',
            'recurringPaymentAmount': 'string',
            'termDurationInSeconds': 123,
            'tags': {
                'string': 'string'
            }
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

savingsPlans (list) --
Information about the Savings Plans.

(dict) --
Information about a Savings Plan.

offeringId (string) --
The ID of the offering.

savingsPlanId (string) --
The ID of the Savings Plan.

savingsPlanArn (string) --
The Amazon Resource Name (ARN) of the Savings Plan.

description (string) --
The description.

start (string) --
The start time.

end (string) --
The end time.

state (string) --
The state.

region (string) --
The AWS Region.

ec2InstanceFamily (string) --
The EC2 instance family.

savingsPlanType (string) --
The plan type.

paymentOption (string) --
The payment option.

productTypes (list) --
The product types.

(string) --


currency (string) --
The currency.

commitment (string) --
The hourly commitment, in USD.

upfrontPaymentAmount (string) --
The up-front payment amount.

recurringPaymentAmount (string) --
The recurring payment amount.

termDurationInSeconds (integer) --
The duration of the term, in seconds.

tags (dict) --
One or more tags.

(string) --
(string) --








nextToken (string) --
The token to use to retrieve the next page of results. This value is null when there are no more results to return.







Exceptions

SavingsPlans.Client.exceptions.InternalServerException
SavingsPlans.Client.exceptions.ValidationException


    :return: {
        'savingsPlans': [
            {
                'offeringId': 'string',
                'savingsPlanId': 'string',
                'savingsPlanArn': 'string',
                'description': 'string',
                'start': 'string',
                'end': 'string',
                'state': 'payment-pending'|'payment-failed'|'active'|'retired',
                'region': 'string',
                'ec2InstanceFamily': 'string',
                'savingsPlanType': 'Compute'|'EC2Instance',
                'paymentOption': 'All Upfront'|'Partial Upfront'|'No Upfront',
                'productTypes': [
                    'EC2'|'Fargate'|'Lambda',
                ],
                'currency': 'CNY'|'USD',
                'commitment': 'string',
                'upfrontPaymentAmount': 'string',
                'recurringPaymentAmount': 'string',
                'termDurationInSeconds': 123,
                'tags': {
                    'string': 'string'
                }
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_savings_plans_offering_rates(savingsPlanOfferingIds=None, savingsPlanPaymentOptions=None, savingsPlanTypes=None, products=None, serviceCodes=None, usageTypes=None, operations=None, filters=None, nextToken=None, maxResults=None):
    """
    Describes the specified Savings Plans offering rates.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_savings_plans_offering_rates(
        savingsPlanOfferingIds=[
            'string',
        ],
        savingsPlanPaymentOptions=[
            'All Upfront'|'Partial Upfront'|'No Upfront',
        ],
        savingsPlanTypes=[
            'Compute'|'EC2Instance',
        ],
        products=[
            'EC2'|'Fargate'|'Lambda',
        ],
        serviceCodes=[
            'AmazonEC2'|'AmazonECS'|'AWSLambda',
        ],
        usageTypes=[
            'string',
        ],
        operations=[
            'string',
        ],
        filters=[
            {
                'name': 'region'|'instanceFamily'|'instanceType'|'productDescription'|'tenancy'|'productId',
                'values': [
                    'string',
                ]
            },
        ],
        nextToken='string',
        maxResults=123
    )
    
    
    :type savingsPlanOfferingIds: list
    :param savingsPlanOfferingIds: The IDs of the offerings.\n\n(string) --\n\n

    :type savingsPlanPaymentOptions: list
    :param savingsPlanPaymentOptions: The payment options.\n\n(string) --\n\n

    :type savingsPlanTypes: list
    :param savingsPlanTypes: The plan types.\n\n(string) --\n\n

    :type products: list
    :param products: The AWS products.\n\n(string) --\n\n

    :type serviceCodes: list
    :param serviceCodes: The services.\n\n(string) --\n\n

    :type usageTypes: list
    :param usageTypes: The usage details of the line item in the billing report.\n\n(string) --\n\n

    :type operations: list
    :param operations: The specific AWS operation for the line item in the billing report.\n\n(string) --\n\n

    :type filters: list
    :param filters: The filters.\n\n(dict) --Information about a filter.\n\nname (string) --The filter name.\n\nvalues (list) --The filter values.\n\n(string) --\n\n\n\n\n\n

    :type nextToken: string
    :param nextToken: The token for the next page of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return with a single call. To retrieve additional results, make another call with the returned token value.

    :rtype: dict

ReturnsResponse Syntax
{
    'searchResults': [
        {
            'savingsPlanOffering': {
                'offeringId': 'string',
                'paymentOption': 'All Upfront'|'Partial Upfront'|'No Upfront',
                'planType': 'Compute'|'EC2Instance',
                'durationSeconds': 123,
                'currency': 'CNY'|'USD',
                'planDescription': 'string'
            },
            'rate': 'string',
            'unit': 'Hrs'|'Lambda-GB-Second'|'Request',
            'productType': 'EC2'|'Fargate'|'Lambda',
            'serviceCode': 'AmazonEC2'|'AmazonECS'|'AWSLambda',
            'usageType': 'string',
            'operation': 'string',
            'properties': [
                {
                    'name': 'string',
                    'value': 'string'
                },
            ]
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

searchResults (list) --
Information about the Savings Plans offering rates.

(dict) --
Information about a Savings Plan offering rate.

savingsPlanOffering (dict) --
The Savings Plan offering.

offeringId (string) --
The ID of the offering.

paymentOption (string) --
The payment option.

planType (string) --
The plan type.

durationSeconds (integer) --
The duration, in seconds.

currency (string) --
The currency.

planDescription (string) --
The description.



rate (string) --
The Savings Plan rate.

unit (string) --
The unit.

productType (string) --
The product type.

serviceCode (string) --
The service.

usageType (string) --
The usage details of the line item in the billing report.

operation (string) --
The specific AWS operation for the line item in the billing report.

properties (list) --
The properties.

(dict) --
Information about a property.

name (string) --
The property name.

value (string) --
The property value.









nextToken (string) --
The token to use to retrieve the next page of results. This value is null when there are no more results to return.







Exceptions

SavingsPlans.Client.exceptions.ValidationException
SavingsPlans.Client.exceptions.InternalServerException


    :return: {
        'searchResults': [
            {
                'savingsPlanOffering': {
                    'offeringId': 'string',
                    'paymentOption': 'All Upfront'|'Partial Upfront'|'No Upfront',
                    'planType': 'Compute'|'EC2Instance',
                    'durationSeconds': 123,
                    'currency': 'CNY'|'USD',
                    'planDescription': 'string'
                },
                'rate': 'string',
                'unit': 'Hrs'|'Lambda-GB-Second'|'Request',
                'productType': 'EC2'|'Fargate'|'Lambda',
                'serviceCode': 'AmazonEC2'|'AmazonECS'|'AWSLambda',
                'usageType': 'string',
                'operation': 'string',
                'properties': [
                    {
                        'name': 'string',
                        'value': 'string'
                    },
                ]
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    SavingsPlans.Client.exceptions.ValidationException
    SavingsPlans.Client.exceptions.InternalServerException
    
    """
    pass

def describe_savings_plans_offerings(offeringIds=None, paymentOptions=None, productType=None, planTypes=None, durations=None, currencies=None, descriptions=None, serviceCodes=None, usageTypes=None, operations=None, filters=None, nextToken=None, maxResults=None):
    """
    Describes the specified Savings Plans offerings.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_savings_plans_offerings(
        offeringIds=[
            'string',
        ],
        paymentOptions=[
            'All Upfront'|'Partial Upfront'|'No Upfront',
        ],
        productType='EC2'|'Fargate'|'Lambda',
        planTypes=[
            'Compute'|'EC2Instance',
        ],
        durations=[
            123,
        ],
        currencies=[
            'CNY'|'USD',
        ],
        descriptions=[
            'string',
        ],
        serviceCodes=[
            'string',
        ],
        usageTypes=[
            'string',
        ],
        operations=[
            'string',
        ],
        filters=[
            {
                'name': 'region'|'instanceFamily',
                'values': [
                    'string',
                ]
            },
        ],
        nextToken='string',
        maxResults=123
    )
    
    
    :type offeringIds: list
    :param offeringIds: The IDs of the offerings.\n\n(string) --\n\n

    :type paymentOptions: list
    :param paymentOptions: The payment options.\n\n(string) --\n\n

    :type productType: string
    :param productType: The product type.

    :type planTypes: list
    :param planTypes: The plan type.\n\n(string) --\n\n

    :type durations: list
    :param durations: The durations, in seconds.\n\n(integer) --\n\n

    :type currencies: list
    :param currencies: The currencies.\n\n(string) --\n\n

    :type descriptions: list
    :param descriptions: The descriptions.\n\n(string) --\n\n

    :type serviceCodes: list
    :param serviceCodes: The services.\n\n(string) --\n\n

    :type usageTypes: list
    :param usageTypes: The usage details of the line item in the billing report.\n\n(string) --\n\n

    :type operations: list
    :param operations: The specific AWS operation for the line item in the billing report.\n\n(string) --\n\n

    :type filters: list
    :param filters: The filters.\n\n(dict) --Information about a filter.\n\nname (string) --The filter name.\n\nvalues (list) --The filter values.\n\n(string) --\n\n\n\n\n\n

    :type nextToken: string
    :param nextToken: The token for the next page of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return with a single call. To retrieve additional results, make another call with the returned token value.

    :rtype: dict

ReturnsResponse Syntax
{
    'searchResults': [
        {
            'offeringId': 'string',
            'productTypes': [
                'EC2'|'Fargate'|'Lambda',
            ],
            'planType': 'Compute'|'EC2Instance',
            'description': 'string',
            'paymentOption': 'All Upfront'|'Partial Upfront'|'No Upfront',
            'durationSeconds': 123,
            'currency': 'CNY'|'USD',
            'serviceCode': 'string',
            'usageType': 'string',
            'operation': 'string',
            'properties': [
                {
                    'name': 'region'|'instanceFamily',
                    'value': 'string'
                },
            ]
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

searchResults (list) --
Information about the Savings Plans offerings.

(dict) --
Information about a Savings Plan offering.

offeringId (string) --
The ID of the offering.

productTypes (list) --
The product type.

(string) --


planType (string) --
The plan type.

description (string) --
The description.

paymentOption (string) --
The payment option.

durationSeconds (integer) --
The duration, in seconds.

currency (string) --
The currency.

serviceCode (string) --
The service.

usageType (string) --
The usage details of the line item in the billing report.

operation (string) --
The specific AWS operation for the line item in the billing report.

properties (list) --
The properties.

(dict) --
Information about a property.

name (string) --
The property name.

value (string) --
The property value.









nextToken (string) --
The token to use to retrieve the next page of results. This value is null when there are no more results to return.







Exceptions

SavingsPlans.Client.exceptions.ValidationException
SavingsPlans.Client.exceptions.InternalServerException


    :return: {
        'searchResults': [
            {
                'offeringId': 'string',
                'productTypes': [
                    'EC2'|'Fargate'|'Lambda',
                ],
                'planType': 'Compute'|'EC2Instance',
                'description': 'string',
                'paymentOption': 'All Upfront'|'Partial Upfront'|'No Upfront',
                'durationSeconds': 123,
                'currency': 'CNY'|'USD',
                'serviceCode': 'string',
                'usageType': 'string',
                'operation': 'string',
                'properties': [
                    {
                        'name': 'region'|'instanceFamily',
                        'value': 'string'
                    },
                ]
            },
        ],
        'nextToken': 'string'
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

def list_tags_for_resource(resourceArn=None):
    """
    Lists the tags for the specified resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        resourceArn='string'
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource.\n

    :rtype: dict
ReturnsResponse Syntax{
    'tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --
tags (dict) --Information about the tags.

(string) --
(string) --









Exceptions

SavingsPlans.Client.exceptions.ResourceNotFoundException
SavingsPlans.Client.exceptions.ValidationException
SavingsPlans.Client.exceptions.InternalServerException


    :return: {
        'tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    SavingsPlans.Client.exceptions.ResourceNotFoundException
    SavingsPlans.Client.exceptions.ValidationException
    SavingsPlans.Client.exceptions.InternalServerException
    
    """
    pass

def tag_resource(resourceArn=None, tags=None):
    """
    Adds the specified tags to the specified resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        resourceArn='string',
        tags={
            'string': 'string'
        }
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource.\n

    :type tags: dict
    :param tags: [REQUIRED]\nOne or more tags. For example, { 'tags': {'key1':'value1', 'key2':'value2'} }.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

SavingsPlans.Client.exceptions.ResourceNotFoundException
SavingsPlans.Client.exceptions.ServiceQuotaExceededException
SavingsPlans.Client.exceptions.ValidationException
SavingsPlans.Client.exceptions.InternalServerException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_resource(resourceArn=None, tagKeys=None):
    """
    Removes the specified tags from the specified resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        resourceArn='string',
        tagKeys=[
            'string',
        ]
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource.\n

    :type tagKeys: list
    :param tagKeys: [REQUIRED]\nThe tag keys.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

SavingsPlans.Client.exceptions.ResourceNotFoundException
SavingsPlans.Client.exceptions.ValidationException
SavingsPlans.Client.exceptions.InternalServerException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

