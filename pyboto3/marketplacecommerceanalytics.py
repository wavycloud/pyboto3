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

def generate_data_set(dataSetType=None, dataSetPublicationDate=None, roleNameArn=None, destinationS3BucketName=None, destinationS3Prefix=None, snsTopicArn=None, customerDefinedValues=None):
    """
    Given a data set type and data set publication date, asynchronously publishes the requested data set to the specified S3 bucket and notifies the specified SNS topic once the data is available. Returns a unique request identifier that can be used to correlate requests with notifications from the SNS topic. Data sets will be published in comma-separated values (CSV) format with the file name {data_set_type}_YYYY-MM-DD.csv. If a file with the same name already exists (e.g. if the same data set is requested twice), the original file will be overwritten by the new file. Requires a Role with an attached permissions policy providing Allow permissions for the following actions: s3:PutObject, s3:GetBucketLocation, sns:GetTopicAttributes, sns:Publish, iam:GetRolePolicy.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.generate_data_set(
        dataSetType='customer_subscriber_hourly_monthly_subscriptions'|'customer_subscriber_annual_subscriptions'|'daily_business_usage_by_instance_type'|'daily_business_fees'|'daily_business_free_trial_conversions'|'daily_business_new_instances'|'daily_business_new_product_subscribers'|'daily_business_canceled_product_subscribers'|'monthly_revenue_billing_and_revenue_data'|'monthly_revenue_annual_subscriptions'|'monthly_revenue_field_demonstration_usage'|'monthly_revenue_flexible_payment_schedule'|'disbursed_amount_by_product'|'disbursed_amount_by_product_with_uncollected_funds'|'disbursed_amount_by_instance_hours'|'disbursed_amount_by_customer_geo'|'disbursed_amount_by_age_of_uncollected_funds'|'disbursed_amount_by_age_of_disbursed_funds'|'disbursed_amount_by_age_of_past_due_funds'|'disbursed_amount_by_uncollected_funds_breakdown'|'customer_profile_by_industry'|'customer_profile_by_revenue'|'customer_profile_by_geography'|'sales_compensation_billed_revenue'|'us_sales_and_use_tax_records',
        dataSetPublicationDate=datetime(2015, 1, 1),
        roleNameArn='string',
        destinationS3BucketName='string',
        destinationS3Prefix='string',
        snsTopicArn='string',
        customerDefinedValues={
            'string': 'string'
        }
    )
    
    
    :type dataSetType: string
    :param dataSetType: [REQUIRED]\nThe desired data set type.\n\ncustomer_subscriber_hourly_monthly_subscriptions From 2017-09-15 to present: Available daily by 24:00 UTC.\ncustomer_subscriber_annual_subscriptions From 2017-09-15 to present: Available daily by 24:00 UTC.\ndaily_business_usage_by_instance_type From 2017-09-15 to present: Available daily by 24:00 UTC.\ndaily_business_fees From 2017-09-15 to present: Available daily by 24:00 UTC.\ndaily_business_free_trial_conversions From 2017-09-15 to present: Available daily by 24:00 UTC.\ndaily_business_new_instances From 2017-09-15 to present: Available daily by 24:00 UTC.\ndaily_business_new_product_subscribers From 2017-09-15 to present: Available daily by 24:00 UTC.\ndaily_business_canceled_product_subscribers From 2017-09-15 to present: Available daily by 24:00 UTC.\nmonthly_revenue_billing_and_revenue_data From 2017-09-15 to present: Available monthly on the 15th day of the month by 24:00 UTC. Data includes metered transactions (e.g. hourly) from one month prior.\nmonthly_revenue_annual_subscriptions From 2017-09-15 to present: Available monthly on the 15th day of the month by 24:00 UTC. Data includes up-front software charges (e.g. annual) from one month prior.\nmonthly_revenue_field_demonstration_usage From 2018-03-15 to present: Available monthly on the 15th day of the month by 24:00 UTC.\nmonthly_revenue_flexible_payment_schedule From 2018-11-15 to present: Available monthly on the 15th day of the month by 24:00 UTC.\ndisbursed_amount_by_product From 2017-09-15 to present: Available every 30 days by 24:00 UTC.\ndisbursed_amount_by_instance_hours From 2017-09-15 to present: Available every 30 days by 24:00 UTC.\ndisbursed_amount_by_customer_geo From 2017-09-15 to present: Available every 30 days by 24:00 UTC.\ndisbursed_amount_by_age_of_uncollected_funds From 2017-09-15 to present: Available every 30 days by 24:00 UTC.\ndisbursed_amount_by_age_of_disbursed_funds From 2017-09-15 to present: Available every 30 days by 24:00 UTC.\ndisbursed_amount_by_age_of_past_due_funds From 2018-04-07 to present: Available every 30 days by 24:00 UTC.\ndisbursed_amount_by_uncollected_funds_breakdown From 2019-10-04 to present: Available every 30 days by 24:00 UTC.\nsales_compensation_billed_revenue From 2017-09-15 to present: Available monthly on the 15th day of the month by 24:00 UTC. Data includes metered transactions (e.g. hourly) from one month prior, and up-front software charges (e.g. annual) from one month prior.\nus_sales_and_use_tax_records From 2017-09-15 to present: Available monthly on the 15th day of the month by 24:00 UTC.\n\n

    :type dataSetPublicationDate: datetime
    :param dataSetPublicationDate: [REQUIRED] The date a data set was published. For daily data sets, provide a date with day-level granularity for the desired day. For monthly data sets except those with prefix disbursed_amount, provide a date with month-level granularity for the desired month (the day value will be ignored). For data sets with prefix disbursed_amount, provide a date with day-level granularity for the desired day. For these data sets we will look backwards in time over the range of 31 days until the first data set is found (the latest one).

    :type roleNameArn: string
    :param roleNameArn: [REQUIRED] The Amazon Resource Name (ARN) of the Role with an attached permissions policy to interact with the provided AWS services.

    :type destinationS3BucketName: string
    :param destinationS3BucketName: [REQUIRED] The name (friendly name, not ARN) of the destination S3 bucket.

    :type destinationS3Prefix: string
    :param destinationS3Prefix: (Optional) The desired S3 prefix for the published data set, similar to a directory path in standard file systems. For example, if given the bucket name 'mybucket' and the prefix 'myprefix/mydatasets', the output file 'outputfile' would be published to 's3://mybucket/myprefix/mydatasets/outputfile'. If the prefix directory structure does not exist, it will be created. If no prefix is provided, the data set will be published to the S3 bucket root.

    :type snsTopicArn: string
    :param snsTopicArn: [REQUIRED] Amazon Resource Name (ARN) for the SNS Topic that will be notified when the data set has been published or if an error has occurred.

    :type customerDefinedValues: dict
    :param customerDefinedValues: (Optional) Key-value pairs which will be returned, unmodified, in the Amazon SNS notification message and the data set metadata file. These key-value pairs can be used to correlated responses with tracking information from other systems.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'dataSetRequestId': 'string'
}


Response Structure

(dict) -- Container for the result of the GenerateDataSet operation.
dataSetRequestId (string) -- A unique identifier representing a specific request to the GenerateDataSet operation. This identifier can be used to correlate a request with notifications from the SNS topic.






Exceptions

MarketplaceCommerceAnalytics.Client.exceptions.MarketplaceCommerceAnalyticsException


    :return: {
        'dataSetRequestId': 'string'
    }
    
    
    :returns: 
    (dict) -- Container for the result of the GenerateDataSet operation.
    dataSetRequestId (string) -- A unique identifier representing a specific request to the GenerateDataSet operation. This identifier can be used to correlate a request with notifications from the SNS topic.
    
    
    
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

def start_support_data_export(dataSetType=None, fromDate=None, roleNameArn=None, destinationS3BucketName=None, destinationS3Prefix=None, snsTopicArn=None, customerDefinedValues=None):
    """
    Given a data set type and a from date, asynchronously publishes the requested customer support data to the specified S3 bucket and notifies the specified SNS topic once the data is available. Returns a unique request identifier that can be used to correlate requests with notifications from the SNS topic. Data sets will be published in comma-separated values (CSV) format with the file name {data_set_type}_YYYY-MM-DD\'T\'HH-mm-ss\'Z\'.csv. If a file with the same name already exists (e.g. if the same data set is requested twice), the original file will be overwritten by the new file. Requires a Role with an attached permissions policy providing Allow permissions for the following actions: s3:PutObject, s3:GetBucketLocation, sns:GetTopicAttributes, sns:Publish, iam:GetRolePolicy.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_support_data_export(
        dataSetType='customer_support_contacts_data'|'test_customer_support_contacts_data',
        fromDate=datetime(2015, 1, 1),
        roleNameArn='string',
        destinationS3BucketName='string',
        destinationS3Prefix='string',
        snsTopicArn='string',
        customerDefinedValues={
            'string': 'string'
        }
    )
    
    
    :type dataSetType: string
    :param dataSetType: [REQUIRED]\nSpecifies the data set type to be written to the output csv file. The data set types customer_support_contacts_data and test_customer_support_contacts_data both result in a csv file containing the following fields: Product Id, Product Code, Customer Guid, Subscription Guid, Subscription Start Date, Organization, AWS Account Id, Given Name, Surname, Telephone Number, Email, Title, Country Code, ZIP Code, Operation Type, and Operation Time.\n\ncustomer_support_contacts_data Customer support contact data. The data set will contain all changes (Creates, Updates, and Deletes) to customer support contact data from the date specified in the from_date parameter.\ntest_customer_support_contacts_data An example data set containing static test data in the same format as customer_support_contacts_data\n\n

    :type fromDate: datetime
    :param fromDate: [REQUIRED] The start date from which to retrieve the data set in UTC. This parameter only affects the customer_support_contacts_data data set type.

    :type roleNameArn: string
    :param roleNameArn: [REQUIRED] The Amazon Resource Name (ARN) of the Role with an attached permissions policy to interact with the provided AWS services.

    :type destinationS3BucketName: string
    :param destinationS3BucketName: [REQUIRED] The name (friendly name, not ARN) of the destination S3 bucket.

    :type destinationS3Prefix: string
    :param destinationS3Prefix: (Optional) The desired S3 prefix for the published data set, similar to a directory path in standard file systems. For example, if given the bucket name 'mybucket' and the prefix 'myprefix/mydatasets', the output file 'outputfile' would be published to 's3://mybucket/myprefix/mydatasets/outputfile'. If the prefix directory structure does not exist, it will be created. If no prefix is provided, the data set will be published to the S3 bucket root.

    :type snsTopicArn: string
    :param snsTopicArn: [REQUIRED] Amazon Resource Name (ARN) for the SNS Topic that will be notified when the data set has been published or if an error has occurred.

    :type customerDefinedValues: dict
    :param customerDefinedValues: (Optional) Key-value pairs which will be returned, unmodified, in the Amazon SNS notification message and the data set metadata file.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'dataSetRequestId': 'string'
}


Response Structure

(dict) -- Container for the result of the StartSupportDataExport operation.
dataSetRequestId (string) -- A unique identifier representing a specific request to the StartSupportDataExport operation. This identifier can be used to correlate a request with notifications from the SNS topic.






Exceptions

MarketplaceCommerceAnalytics.Client.exceptions.MarketplaceCommerceAnalyticsException


    :return: {
        'dataSetRequestId': 'string'
    }
    
    
    :returns: 
    (dict) -- Container for the result of the StartSupportDataExport operation.
    dataSetRequestId (string) -- A unique identifier representing a specific request to the StartSupportDataExport operation. This identifier can be used to correlate a request with notifications from the SNS topic.
    
    
    
    """
    pass

