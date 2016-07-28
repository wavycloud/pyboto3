"""
The MIT License (MIT)

Copyright (c) 2016 Gehad Shaat

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
"""

import boto3


class Marketplacecommerceanalytics(object):
    def __init__(self):
        self.client = boto3.client('Marketplacecommerceanalytics')

    def can_paginate(self, operation_name=None):
        """
        :param operation_name: The operation name. This is the same name
            as the method name on the client. For example, if the
            method name is create_foo, and you'd normally invoke the
            operation as client.create_foo(**kwargs), if the
            create_foo operation can be paginated, you can use the
            call client.get_paginator('create_foo').
            ReturnsTrue if the operation can be paginated,
            False otherwise.
            
        :type operation_name: string
        """
        self.client.can_paginate(operation_name=operation_name)

    def generate_data_set(self, dataSetType=None, dataSetPublicationDate=None, roleNameArn=None,
                          destinationS3BucketName=None, destinationS3Prefix=None, snsTopicArn=None,
                          customerDefinedValues=None):
        """
        :param dataSetType: [REQUIRED]
            The desired data set type.
            customer_subscriber_hourly_monthly_subscriptions - Available daily by 5:00 PM Pacific Time since 2014-07-21.
            customer_subscriber_annual_subscriptions - Available daily by 5:00 PM Pacific Time since 2014-07-21.
            daily_business_usage_by_instance_type - Available daily by 5:00 PM Pacific Time since 2015-01-26.
            daily_business_fees - Available daily by 5:00 PM Pacific Time since 2015-01-26.
            daily_business_free_trial_conversions - Available daily by 5:00 PM Pacific Time since 2015-01-26.
            daily_business_new_instances - Available daily by 5:00 PM Pacific Time since 2015-01-26.
            daily_business_new_product_subscribers - Available daily by 5:00 PM Pacific Time since 2015-01-26.
            daily_business_canceled_product_subscribers - Available daily by 5:00 PM Pacific Time since 2015-01-26.
            monthly_revenue_billing_and_revenue_data - Available monthly on the 4th day of the month by 5:00 PM Pacific Time since 2015-02.
            monthly_revenue_annual_subscriptions - Available monthly on the 4th day of the month by 5:00 PM Pacific Time since 2015-02.
            disbursed_amount_by_product - Available every 30 days by 5:00 PM Pacific Time since 2015-01-26.
            disbursed_amount_by_product_with_uncollected_funds -This data set is only available from 2012-04-19 until 2015-01-25. After 2015-01-25, this data set was split into three data sets: disbursed_amount_by_product, disbursed_amount_by_age_of_uncollected_funds, and disbursed_amount_by_age_of_disbursed_funds.
            disbursed_amount_by_customer_geo - Available every 30 days by 5:00 PM Pacific Time since 2012-04-19.
            disbursed_amount_by_age_of_uncollected_funds - Available every 30 days by 5:00 PM Pacific Time since 2015-01-26.
            disbursed_amount_by_age_of_disbursed_funds - Available every 30 days by 5:00 PM Pacific Time since 2015-01-26.
            customer_profile_by_industry - Available daily by 5:00 PM Pacific Time since 2015-10-01.
            customer_profile_by_revenue - Available daily by 5:00 PM Pacific Time since 2015-10-01.
            customer_profile_by_geography - Available daily by 5:00 PM Pacific Time since 2015-10-01.
            
        :type dataSetType: string
        :param dataSetPublicationDate: [REQUIRED] The date a data set was published. For daily data sets, provide a date with day-level granularity for the desired day. For weekly data sets, provide a date with day-level granularity within the desired week (the day value will be ignored). For monthly data sets, provide a date with month-level granularity for the desired month (the day value will be ignored).
        :type dataSetPublicationDate: datetime
        :param roleNameArn: [REQUIRED] The Amazon Resource Name (ARN) of the Role with an attached permissions policy to interact with the provided AWS services.
        :type roleNameArn: string
        :param destinationS3BucketName: [REQUIRED] The name (friendly name, not ARN) of the destination S3 bucket.
        :type destinationS3BucketName: string
        :param destinationS3Prefix: (Optional) The desired S3 prefix for the published data set, similar to a directory path in standard file systems. For example, if given the bucket name 'mybucket' and the prefix 'myprefix/mydatasets', the output file 'outputfile' would be published to 's3://mybucket/myprefix/mydatasets/outputfile'. If the prefix directory structure does not exist, it will be created. If no prefix is provided, the data set will be published to the S3 bucket root.
        :type destinationS3Prefix: string
        :param snsTopicArn: [REQUIRED] Amazon Resource Name (ARN) for the SNS Topic that will be notified when the data set has been published or if an error has occurred.
        :type snsTopicArn: string
        :param customerDefinedValues: (Optional) Key-value pairs which will be returned, unmodified, in the Amazon SNS notification message and the data set metadata file. These key-value pairs can be used to correlated responses with tracking information from other systems.
            (string) --
            (string) --
            
        :type customerDefinedValues: dict
        """
        self.client.generate_data_set(dataSetType=dataSetType, dataSetPublicationDate=dataSetPublicationDate,
                                      roleNameArn=roleNameArn, destinationS3BucketName=destinationS3BucketName,
                                      destinationS3Prefix=destinationS3Prefix, snsTopicArn=snsTopicArn,
                                      customerDefinedValues=customerDefinedValues)

    def generate_presigned_url(self, ClientMethod=None, Params=None, ExpiresIn=None, HttpMethod=None):
        """
        :param ClientMethod: The client method to presign for
        :type ClientMethod: string
        :param Params: The parameters normally passed to
            ClientMethod.
        :type Params: dict
        :param ExpiresIn: The number of seconds the presigned url is valid
            for. By default it expires in an hour (3600 seconds)
        :type ExpiresIn: int
        :param HttpMethod: The http method to use on the generated url. By
            default, the http method is whatever is used in the method's model.
        :type HttpMethod: string
        """
        self.client.generate_presigned_url(ClientMethod=ClientMethod, Params=Params, ExpiresIn=ExpiresIn,
                                           HttpMethod=HttpMethod)

    def get_paginator(self, operation_name=None):
        """
        :param operation_name: The operation name. This is the same name
            as the method name on the client. For example, if the
            method name is create_foo, and you'd normally invoke the
            operation as client.create_foo(**kwargs), if the
            create_foo operation can be paginated, you can use the
            call client.get_paginator('create_foo').
            Raises OperationNotPageableErrorRaised if the operation is not
            pageable. You can use the client.can_paginate method to
            check if an operation is pageable.
            Return typeL{botocore.paginate.Paginator}
            ReturnsA paginator object.
            
        :type operation_name: string
        """
        self.client.get_paginator(operation_name=operation_name)

    def get_waiter(self):
        """
        """
        self.client.get_waiter()
