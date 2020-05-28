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

def associate_service_quota_template():
    """
    Associates the Service Quotas template with your organization so that when new accounts are created in your organization, the template submits increase requests for the specified service quotas. Use the Service Quotas template to request an increase for any adjustable quota value. After you define the Service Quotas template, use this operation to associate, or enable, the template.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.associate_service_quota_template()
    
    
    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

ServiceQuotas.Client.exceptions.DependencyAccessDeniedException
ServiceQuotas.Client.exceptions.AccessDeniedException
ServiceQuotas.Client.exceptions.ServiceException
ServiceQuotas.Client.exceptions.TooManyRequestsException
ServiceQuotas.Client.exceptions.AWSServiceAccessNotEnabledException
ServiceQuotas.Client.exceptions.OrganizationNotInAllFeaturesModeException
ServiceQuotas.Client.exceptions.TemplatesNotAvailableInRegionException
ServiceQuotas.Client.exceptions.NoAvailableOrganizationException


    :return: {}
    
    
    :returns: 
    ServiceQuotas.Client.exceptions.DependencyAccessDeniedException
    ServiceQuotas.Client.exceptions.AccessDeniedException
    ServiceQuotas.Client.exceptions.ServiceException
    ServiceQuotas.Client.exceptions.TooManyRequestsException
    ServiceQuotas.Client.exceptions.AWSServiceAccessNotEnabledException
    ServiceQuotas.Client.exceptions.OrganizationNotInAllFeaturesModeException
    ServiceQuotas.Client.exceptions.TemplatesNotAvailableInRegionException
    ServiceQuotas.Client.exceptions.NoAvailableOrganizationException
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def delete_service_quota_increase_request_from_template(ServiceCode=None, QuotaCode=None, AwsRegion=None):
    """
    Removes a service quota increase request from the Service Quotas template.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_service_quota_increase_request_from_template(
        ServiceCode='string',
        QuotaCode='string',
        AwsRegion='string'
    )
    
    
    :type ServiceCode: string
    :param ServiceCode: [REQUIRED]\nSpecifies the code for the service that you want to delete.\n

    :type QuotaCode: string
    :param QuotaCode: [REQUIRED]\nSpecifies the code for the quota that you want to delete.\n

    :type AwsRegion: string
    :param AwsRegion: [REQUIRED]\nSpecifies the AWS Region for the quota that you want to delete.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

ServiceQuotas.Client.exceptions.AccessDeniedException
ServiceQuotas.Client.exceptions.ServiceException
ServiceQuotas.Client.exceptions.DependencyAccessDeniedException
ServiceQuotas.Client.exceptions.TooManyRequestsException
ServiceQuotas.Client.exceptions.NoSuchResourceException
ServiceQuotas.Client.exceptions.IllegalArgumentException
ServiceQuotas.Client.exceptions.AWSServiceAccessNotEnabledException
ServiceQuotas.Client.exceptions.TemplatesNotAvailableInRegionException
ServiceQuotas.Client.exceptions.NoAvailableOrganizationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def disassociate_service_quota_template():
    """
    Disables the Service Quotas template. Once the template is disabled, it does not request quota increases for new accounts in your organization. Disabling the quota template does not apply the quota increase requests from the template.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disassociate_service_quota_template()
    
    
    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

ServiceQuotas.Client.exceptions.DependencyAccessDeniedException
ServiceQuotas.Client.exceptions.ServiceQuotaTemplateNotInUseException
ServiceQuotas.Client.exceptions.AccessDeniedException
ServiceQuotas.Client.exceptions.ServiceException
ServiceQuotas.Client.exceptions.TooManyRequestsException
ServiceQuotas.Client.exceptions.AWSServiceAccessNotEnabledException
ServiceQuotas.Client.exceptions.TemplatesNotAvailableInRegionException
ServiceQuotas.Client.exceptions.NoAvailableOrganizationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
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

def get_association_for_service_quota_template():
    """
    Retrieves the ServiceQuotaTemplateAssociationStatus value from the service. Use this action to determine if the Service Quota template is associated, or enabled.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_association_for_service_quota_template()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'ServiceQuotaTemplateAssociationStatus': 'ASSOCIATED'|'DISASSOCIATED'
}


Response Structure

(dict) --
ServiceQuotaTemplateAssociationStatus (string) --Specifies whether the template is ASSOCIATED or DISASSOCIATED . If the template is ASSOCIATED , then it requests service quota increases for all new accounts created in your organization.






Exceptions

ServiceQuotas.Client.exceptions.DependencyAccessDeniedException
ServiceQuotas.Client.exceptions.ServiceQuotaTemplateNotInUseException
ServiceQuotas.Client.exceptions.AccessDeniedException
ServiceQuotas.Client.exceptions.ServiceException
ServiceQuotas.Client.exceptions.TooManyRequestsException
ServiceQuotas.Client.exceptions.AWSServiceAccessNotEnabledException
ServiceQuotas.Client.exceptions.TemplatesNotAvailableInRegionException
ServiceQuotas.Client.exceptions.NoAvailableOrganizationException


    :return: {
        'ServiceQuotaTemplateAssociationStatus': 'ASSOCIATED'|'DISASSOCIATED'
    }
    
    
    """
    pass

def get_aws_default_service_quota(ServiceCode=None, QuotaCode=None):
    """
    Retrieves the default service quotas values. The Value returned for each quota is the AWS default value, even if the quotas have been increased..
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_aws_default_service_quota(
        ServiceCode='string',
        QuotaCode='string'
    )
    
    
    :type ServiceCode: string
    :param ServiceCode: [REQUIRED]\nSpecifies the service that you want to use.\n

    :type QuotaCode: string
    :param QuotaCode: [REQUIRED]\nIdentifies the service quota you want to select.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Quota': {
        'ServiceCode': 'string',
        'ServiceName': 'string',
        'QuotaArn': 'string',
        'QuotaCode': 'string',
        'QuotaName': 'string',
        'Value': 123.0,
        'Unit': 'string',
        'Adjustable': True|False,
        'GlobalQuota': True|False,
        'UsageMetric': {
            'MetricNamespace': 'string',
            'MetricName': 'string',
            'MetricDimensions': {
                'string': 'string'
            },
            'MetricStatisticRecommendation': 'string'
        },
        'Period': {
            'PeriodValue': 123,
            'PeriodUnit': 'MICROSECOND'|'MILLISECOND'|'SECOND'|'MINUTE'|'HOUR'|'DAY'|'WEEK'
        },
        'ErrorReason': {
            'ErrorCode': 'DEPENDENCY_ACCESS_DENIED_ERROR'|'DEPENDENCY_THROTTLING_ERROR'|'DEPENDENCY_SERVICE_ERROR'|'SERVICE_QUOTA_NOT_AVAILABLE_ERROR',
            'ErrorMessage': 'string'
        }
    }
}


Response Structure

(dict) --

Quota (dict) --
Returns the  ServiceQuota object which contains all values for a quota.

ServiceCode (string) --
Specifies the service that you want to use.

ServiceName (string) --
The name of the AWS service specified in the increase request.

QuotaArn (string) --
The Amazon Resource Name (ARN) of the service quota.

QuotaCode (string) --
The code identifier for the service quota specified.

QuotaName (string) --
The name identifier of the service quota.

Value (float) --
The value of service quota.

Unit (string) --
The unit of measurement for the value of the service quota.

Adjustable (boolean) --
Specifies if the quota value can be increased.

GlobalQuota (boolean) --
Specifies if the quota is global.

UsageMetric (dict) --
Specifies the details about the measurement.

MetricNamespace (string) --
The namespace of the metric. The namespace is a container for CloudWatch metrics. You can specify a name for the namespace when you create a metric.

MetricName (string) --
The name of the CloudWatch metric that measures usage of a service quota. This is a required field.

MetricDimensions (dict) --
A dimension is a name/value pair that is part of the identity of a metric. Every metric has specific characteristics that describe it, and you can think of dimensions as categories for those characteristics. These dimensions are part of the CloudWatch Metric Identity that measures usage against a particular service quota.

(string) --
(string) --




MetricStatisticRecommendation (string) --
Statistics are metric data aggregations over specified periods of time. This is the recommended statistic to use when comparing usage in the CloudWatch Metric against your Service Quota.



Period (dict) --
Identifies the unit and value of how time is measured.

PeriodValue (integer) --
The value of a period.

PeriodUnit (string) --
The time unit of a period.



ErrorReason (dict) --
Specifies the ErrorCode and ErrorMessage when success isn\'t achieved.

ErrorCode (string) --
Service Quotas returns the following error values.

DEPENDENCY_ACCESS_DENIED_ERROR is returned when the caller does not have permission to call the service or service quota. To resolve the error, you need permission to access the service or service quota.
DEPENDENCY_THROTTLING_ERROR is returned when the service being called is throttling Service Quotas.
DEPENDENCY_SERVICE_ERROR is returned when the service being called has availability issues.
SERVICE_QUOTA_NOT_AVAILABLE_ERROR is returned when there was an error in Service Quotas.


ErrorMessage (string) --
The error message that provides more detail.











Exceptions

ServiceQuotas.Client.exceptions.AccessDeniedException
ServiceQuotas.Client.exceptions.NoSuchResourceException
ServiceQuotas.Client.exceptions.IllegalArgumentException
ServiceQuotas.Client.exceptions.ServiceException
ServiceQuotas.Client.exceptions.TooManyRequestsException


    :return: {
        'Quota': {
            'ServiceCode': 'string',
            'ServiceName': 'string',
            'QuotaArn': 'string',
            'QuotaCode': 'string',
            'QuotaName': 'string',
            'Value': 123.0,
            'Unit': 'string',
            'Adjustable': True|False,
            'GlobalQuota': True|False,
            'UsageMetric': {
                'MetricNamespace': 'string',
                'MetricName': 'string',
                'MetricDimensions': {
                    'string': 'string'
                },
                'MetricStatisticRecommendation': 'string'
            },
            'Period': {
                'PeriodValue': 123,
                'PeriodUnit': 'MICROSECOND'|'MILLISECOND'|'SECOND'|'MINUTE'|'HOUR'|'DAY'|'WEEK'
            },
            'ErrorReason': {
                'ErrorCode': 'DEPENDENCY_ACCESS_DENIED_ERROR'|'DEPENDENCY_THROTTLING_ERROR'|'DEPENDENCY_SERVICE_ERROR'|'SERVICE_QUOTA_NOT_AVAILABLE_ERROR',
                'ErrorMessage': 'string'
            }
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
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

def get_requested_service_quota_change(RequestId=None):
    """
    Retrieves the details for a particular increase request.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_requested_service_quota_change(
        RequestId='string'
    )
    
    
    :type RequestId: string
    :param RequestId: [REQUIRED]\nIdentifies the quota increase request.\n

    :rtype: dict
ReturnsResponse Syntax{
    'RequestedQuota': {
        'Id': 'string',
        'CaseId': 'string',
        'ServiceCode': 'string',
        'ServiceName': 'string',
        'QuotaCode': 'string',
        'QuotaName': 'string',
        'DesiredValue': 123.0,
        'Status': 'PENDING'|'CASE_OPENED'|'APPROVED'|'DENIED'|'CASE_CLOSED',
        'Created': datetime(2015, 1, 1),
        'LastUpdated': datetime(2015, 1, 1),
        'Requester': 'string',
        'QuotaArn': 'string',
        'GlobalQuota': True|False,
        'Unit': 'string'
    }
}


Response Structure

(dict) --
RequestedQuota (dict) --Returns the RequestedServiceQuotaChange object for the specific increase request.

Id (string) --The unique identifier of a requested service quota change.

CaseId (string) --The case Id for the service quota increase request.

ServiceCode (string) --Specifies the service that you want to use.

ServiceName (string) --The name of the AWS service specified in the increase request.

QuotaCode (string) --Specifies the service quota that you want to use.

QuotaName (string) --Name of the service quota.

DesiredValue (float) --New increased value for the service quota.

Status (string) --State of the service quota increase request.

Created (datetime) --The date and time when the service quota increase request was received and the case Id was created.

LastUpdated (datetime) --The date and time of the most recent change in the service quota increase request.

Requester (string) --The IAM identity who submitted the service quota increase request.

QuotaArn (string) --The Amazon Resource Name (ARN) of the service quota.

GlobalQuota (boolean) --Identifies if the quota is global.

Unit (string) --Specifies the unit used for the quota.








Exceptions

ServiceQuotas.Client.exceptions.AccessDeniedException
ServiceQuotas.Client.exceptions.NoSuchResourceException
ServiceQuotas.Client.exceptions.IllegalArgumentException
ServiceQuotas.Client.exceptions.ServiceException
ServiceQuotas.Client.exceptions.TooManyRequestsException


    :return: {
        'RequestedQuota': {
            'Id': 'string',
            'CaseId': 'string',
            'ServiceCode': 'string',
            'ServiceName': 'string',
            'QuotaCode': 'string',
            'QuotaName': 'string',
            'DesiredValue': 123.0,
            'Status': 'PENDING'|'CASE_OPENED'|'APPROVED'|'DENIED'|'CASE_CLOSED',
            'Created': datetime(2015, 1, 1),
            'LastUpdated': datetime(2015, 1, 1),
            'Requester': 'string',
            'QuotaArn': 'string',
            'GlobalQuota': True|False,
            'Unit': 'string'
        }
    }
    
    
    """
    pass

def get_service_quota(ServiceCode=None, QuotaCode=None):
    """
    Returns the details for the specified service quota. This operation provides a different Value than the GetAWSDefaultServiceQuota operation. This operation returns the applied value for each quota. GetAWSDefaultServiceQuota returns the default AWS value for each quota.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_service_quota(
        ServiceCode='string',
        QuotaCode='string'
    )
    
    
    :type ServiceCode: string
    :param ServiceCode: [REQUIRED]\nSpecifies the service that you want to use.\n

    :type QuotaCode: string
    :param QuotaCode: [REQUIRED]\nIdentifies the service quota you want to select.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Quota': {
        'ServiceCode': 'string',
        'ServiceName': 'string',
        'QuotaArn': 'string',
        'QuotaCode': 'string',
        'QuotaName': 'string',
        'Value': 123.0,
        'Unit': 'string',
        'Adjustable': True|False,
        'GlobalQuota': True|False,
        'UsageMetric': {
            'MetricNamespace': 'string',
            'MetricName': 'string',
            'MetricDimensions': {
                'string': 'string'
            },
            'MetricStatisticRecommendation': 'string'
        },
        'Period': {
            'PeriodValue': 123,
            'PeriodUnit': 'MICROSECOND'|'MILLISECOND'|'SECOND'|'MINUTE'|'HOUR'|'DAY'|'WEEK'
        },
        'ErrorReason': {
            'ErrorCode': 'DEPENDENCY_ACCESS_DENIED_ERROR'|'DEPENDENCY_THROTTLING_ERROR'|'DEPENDENCY_SERVICE_ERROR'|'SERVICE_QUOTA_NOT_AVAILABLE_ERROR',
            'ErrorMessage': 'string'
        }
    }
}


Response Structure

(dict) --

Quota (dict) --
Returns the  ServiceQuota object which contains all values for a quota.

ServiceCode (string) --
Specifies the service that you want to use.

ServiceName (string) --
The name of the AWS service specified in the increase request.

QuotaArn (string) --
The Amazon Resource Name (ARN) of the service quota.

QuotaCode (string) --
The code identifier for the service quota specified.

QuotaName (string) --
The name identifier of the service quota.

Value (float) --
The value of service quota.

Unit (string) --
The unit of measurement for the value of the service quota.

Adjustable (boolean) --
Specifies if the quota value can be increased.

GlobalQuota (boolean) --
Specifies if the quota is global.

UsageMetric (dict) --
Specifies the details about the measurement.

MetricNamespace (string) --
The namespace of the metric. The namespace is a container for CloudWatch metrics. You can specify a name for the namespace when you create a metric.

MetricName (string) --
The name of the CloudWatch metric that measures usage of a service quota. This is a required field.

MetricDimensions (dict) --
A dimension is a name/value pair that is part of the identity of a metric. Every metric has specific characteristics that describe it, and you can think of dimensions as categories for those characteristics. These dimensions are part of the CloudWatch Metric Identity that measures usage against a particular service quota.

(string) --
(string) --




MetricStatisticRecommendation (string) --
Statistics are metric data aggregations over specified periods of time. This is the recommended statistic to use when comparing usage in the CloudWatch Metric against your Service Quota.



Period (dict) --
Identifies the unit and value of how time is measured.

PeriodValue (integer) --
The value of a period.

PeriodUnit (string) --
The time unit of a period.



ErrorReason (dict) --
Specifies the ErrorCode and ErrorMessage when success isn\'t achieved.

ErrorCode (string) --
Service Quotas returns the following error values.

DEPENDENCY_ACCESS_DENIED_ERROR is returned when the caller does not have permission to call the service or service quota. To resolve the error, you need permission to access the service or service quota.
DEPENDENCY_THROTTLING_ERROR is returned when the service being called is throttling Service Quotas.
DEPENDENCY_SERVICE_ERROR is returned when the service being called has availability issues.
SERVICE_QUOTA_NOT_AVAILABLE_ERROR is returned when there was an error in Service Quotas.


ErrorMessage (string) --
The error message that provides more detail.











Exceptions

ServiceQuotas.Client.exceptions.AccessDeniedException
ServiceQuotas.Client.exceptions.NoSuchResourceException
ServiceQuotas.Client.exceptions.IllegalArgumentException
ServiceQuotas.Client.exceptions.ServiceException
ServiceQuotas.Client.exceptions.TooManyRequestsException


    :return: {
        'Quota': {
            'ServiceCode': 'string',
            'ServiceName': 'string',
            'QuotaArn': 'string',
            'QuotaCode': 'string',
            'QuotaName': 'string',
            'Value': 123.0,
            'Unit': 'string',
            'Adjustable': True|False,
            'GlobalQuota': True|False,
            'UsageMetric': {
                'MetricNamespace': 'string',
                'MetricName': 'string',
                'MetricDimensions': {
                    'string': 'string'
                },
                'MetricStatisticRecommendation': 'string'
            },
            'Period': {
                'PeriodValue': 123,
                'PeriodUnit': 'MICROSECOND'|'MILLISECOND'|'SECOND'|'MINUTE'|'HOUR'|'DAY'|'WEEK'
            },
            'ErrorReason': {
                'ErrorCode': 'DEPENDENCY_ACCESS_DENIED_ERROR'|'DEPENDENCY_THROTTLING_ERROR'|'DEPENDENCY_SERVICE_ERROR'|'SERVICE_QUOTA_NOT_AVAILABLE_ERROR',
                'ErrorMessage': 'string'
            }
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def get_service_quota_increase_request_from_template(ServiceCode=None, QuotaCode=None, AwsRegion=None):
    """
    Returns the details of the service quota increase request in your template.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_service_quota_increase_request_from_template(
        ServiceCode='string',
        QuotaCode='string',
        AwsRegion='string'
    )
    
    
    :type ServiceCode: string
    :param ServiceCode: [REQUIRED]\nSpecifies the service that you want to use.\n

    :type QuotaCode: string
    :param QuotaCode: [REQUIRED]\nSpecifies the quota you want.\n

    :type AwsRegion: string
    :param AwsRegion: [REQUIRED]\nSpecifies the AWS Region for the quota that you want to use.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ServiceQuotaIncreaseRequestInTemplate': {
        'ServiceCode': 'string',
        'ServiceName': 'string',
        'QuotaCode': 'string',
        'QuotaName': 'string',
        'DesiredValue': 123.0,
        'AwsRegion': 'string',
        'Unit': 'string',
        'GlobalQuota': True|False
    }
}


Response Structure

(dict) --

ServiceQuotaIncreaseRequestInTemplate (dict) --
This object contains the details about the quota increase request.

ServiceCode (string) --
The code identifier for the AWS service specified in the increase request.

ServiceName (string) --
The name of the AWS service specified in the increase request.

QuotaCode (string) --
The code identifier for the service quota specified in the increase request.

QuotaName (string) --
The name of the service quota in the increase request.

DesiredValue (float) --
Identifies the new, increased value of the service quota in the increase request.

AwsRegion (string) --
The AWS Region where the increase request occurs.

Unit (string) --
The unit of measure for the increase request.

GlobalQuota (boolean) --
Specifies if the quota is a global quota.









Exceptions

ServiceQuotas.Client.exceptions.AccessDeniedException
ServiceQuotas.Client.exceptions.DependencyAccessDeniedException
ServiceQuotas.Client.exceptions.ServiceException
ServiceQuotas.Client.exceptions.TooManyRequestsException
ServiceQuotas.Client.exceptions.NoSuchResourceException
ServiceQuotas.Client.exceptions.IllegalArgumentException
ServiceQuotas.Client.exceptions.AWSServiceAccessNotEnabledException
ServiceQuotas.Client.exceptions.TemplatesNotAvailableInRegionException
ServiceQuotas.Client.exceptions.NoAvailableOrganizationException


    :return: {
        'ServiceQuotaIncreaseRequestInTemplate': {
            'ServiceCode': 'string',
            'ServiceName': 'string',
            'QuotaCode': 'string',
            'QuotaName': 'string',
            'DesiredValue': 123.0,
            'AwsRegion': 'string',
            'Unit': 'string',
            'GlobalQuota': True|False
        }
    }
    
    
    :returns: 
    ServiceQuotas.Client.exceptions.AccessDeniedException
    ServiceQuotas.Client.exceptions.DependencyAccessDeniedException
    ServiceQuotas.Client.exceptions.ServiceException
    ServiceQuotas.Client.exceptions.TooManyRequestsException
    ServiceQuotas.Client.exceptions.NoSuchResourceException
    ServiceQuotas.Client.exceptions.IllegalArgumentException
    ServiceQuotas.Client.exceptions.AWSServiceAccessNotEnabledException
    ServiceQuotas.Client.exceptions.TemplatesNotAvailableInRegionException
    ServiceQuotas.Client.exceptions.NoAvailableOrganizationException
    
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

def list_aws_default_service_quotas(ServiceCode=None, NextToken=None, MaxResults=None):
    """
    Lists all default service quotas for the specified AWS service or all AWS services. ListAWSDefaultServiceQuotas is similar to  ListServiceQuotas except for the Value object. The Value object returned by ListAWSDefaultServiceQuotas is the default value assigned by AWS. This request returns a list of all service quotas for the specified service. The listing of each you\'ll see the default values are the values that AWS provides for the quotas.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_aws_default_service_quotas(
        ServiceCode='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type ServiceCode: string
    :param ServiceCode: [REQUIRED]\nSpecifies the service that you want to use.\n

    :type NextToken: string
    :param NextToken: (Optional) Use this parameter in a request if you receive a NextToken response in a previous request that indicates that there\'s more output available. In a subsequent call, set it to the value of the previous call\'s NextToken response to indicate where the output should continue from. If additional items exist beyond the specified maximum, the NextToken element is present and has a value (isn\'t null). Include that value as the NextToken request parameter in the call to the operation to get the next part of the results. You should check NextToken after every operation to ensure that you receive all of the results.

    :type MaxResults: integer
    :param MaxResults: (Optional) Limits the number of results that you want to include in the response. If you don\'t include this parameter, the response defaults to a value that\'s specific to the operation. If additional items exist beyond the specified maximum, the NextToken element is present and has a value (isn\'t null). Include that value as the NextToken request parameter in the call to the operation to get the next part of the results. You should check NextToken after every operation to ensure that you receive all of the results.

    :rtype: dict

ReturnsResponse Syntax
{
    'NextToken': 'string',
    'Quotas': [
        {
            'ServiceCode': 'string',
            'ServiceName': 'string',
            'QuotaArn': 'string',
            'QuotaCode': 'string',
            'QuotaName': 'string',
            'Value': 123.0,
            'Unit': 'string',
            'Adjustable': True|False,
            'GlobalQuota': True|False,
            'UsageMetric': {
                'MetricNamespace': 'string',
                'MetricName': 'string',
                'MetricDimensions': {
                    'string': 'string'
                },
                'MetricStatisticRecommendation': 'string'
            },
            'Period': {
                'PeriodValue': 123,
                'PeriodUnit': 'MICROSECOND'|'MILLISECOND'|'SECOND'|'MINUTE'|'HOUR'|'DAY'|'WEEK'
            },
            'ErrorReason': {
                'ErrorCode': 'DEPENDENCY_ACCESS_DENIED_ERROR'|'DEPENDENCY_THROTTLING_ERROR'|'DEPENDENCY_SERVICE_ERROR'|'SERVICE_QUOTA_NOT_AVAILABLE_ERROR',
                'ErrorMessage': 'string'
            }
        },
    ]
}


Response Structure

(dict) --

NextToken (string) --
(Optional) Use this parameter in a request if you receive a NextToken response in a previous request that indicates that there\'s more output available. In a subsequent call, set it to the value of the previous call\'s NextToken response to indicate where the output should continue from.

Quotas (list) --
A list of the quotas in the account with the AWS default values.

(dict) --
A structure that contains the full set of details that define the service quota.

ServiceCode (string) --
Specifies the service that you want to use.

ServiceName (string) --
The name of the AWS service specified in the increase request.

QuotaArn (string) --
The Amazon Resource Name (ARN) of the service quota.

QuotaCode (string) --
The code identifier for the service quota specified.

QuotaName (string) --
The name identifier of the service quota.

Value (float) --
The value of service quota.

Unit (string) --
The unit of measurement for the value of the service quota.

Adjustable (boolean) --
Specifies if the quota value can be increased.

GlobalQuota (boolean) --
Specifies if the quota is global.

UsageMetric (dict) --
Specifies the details about the measurement.

MetricNamespace (string) --
The namespace of the metric. The namespace is a container for CloudWatch metrics. You can specify a name for the namespace when you create a metric.

MetricName (string) --
The name of the CloudWatch metric that measures usage of a service quota. This is a required field.

MetricDimensions (dict) --
A dimension is a name/value pair that is part of the identity of a metric. Every metric has specific characteristics that describe it, and you can think of dimensions as categories for those characteristics. These dimensions are part of the CloudWatch Metric Identity that measures usage against a particular service quota.

(string) --
(string) --




MetricStatisticRecommendation (string) --
Statistics are metric data aggregations over specified periods of time. This is the recommended statistic to use when comparing usage in the CloudWatch Metric against your Service Quota.



Period (dict) --
Identifies the unit and value of how time is measured.

PeriodValue (integer) --
The value of a period.

PeriodUnit (string) --
The time unit of a period.



ErrorReason (dict) --
Specifies the ErrorCode and ErrorMessage when success isn\'t achieved.

ErrorCode (string) --
Service Quotas returns the following error values.

DEPENDENCY_ACCESS_DENIED_ERROR is returned when the caller does not have permission to call the service or service quota. To resolve the error, you need permission to access the service or service quota.
DEPENDENCY_THROTTLING_ERROR is returned when the service being called is throttling Service Quotas.
DEPENDENCY_SERVICE_ERROR is returned when the service being called has availability issues.
SERVICE_QUOTA_NOT_AVAILABLE_ERROR is returned when there was an error in Service Quotas.


ErrorMessage (string) --
The error message that provides more detail.













Exceptions

ServiceQuotas.Client.exceptions.AccessDeniedException
ServiceQuotas.Client.exceptions.NoSuchResourceException
ServiceQuotas.Client.exceptions.IllegalArgumentException
ServiceQuotas.Client.exceptions.InvalidPaginationTokenException
ServiceQuotas.Client.exceptions.ServiceException
ServiceQuotas.Client.exceptions.TooManyRequestsException


    :return: {
        'NextToken': 'string',
        'Quotas': [
            {
                'ServiceCode': 'string',
                'ServiceName': 'string',
                'QuotaArn': 'string',
                'QuotaCode': 'string',
                'QuotaName': 'string',
                'Value': 123.0,
                'Unit': 'string',
                'Adjustable': True|False,
                'GlobalQuota': True|False,
                'UsageMetric': {
                    'MetricNamespace': 'string',
                    'MetricName': 'string',
                    'MetricDimensions': {
                        'string': 'string'
                    },
                    'MetricStatisticRecommendation': 'string'
                },
                'Period': {
                    'PeriodValue': 123,
                    'PeriodUnit': 'MICROSECOND'|'MILLISECOND'|'SECOND'|'MINUTE'|'HOUR'|'DAY'|'WEEK'
                },
                'ErrorReason': {
                    'ErrorCode': 'DEPENDENCY_ACCESS_DENIED_ERROR'|'DEPENDENCY_THROTTLING_ERROR'|'DEPENDENCY_SERVICE_ERROR'|'SERVICE_QUOTA_NOT_AVAILABLE_ERROR',
                    'ErrorMessage': 'string'
                }
            },
        ]
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def list_requested_service_quota_change_history(ServiceCode=None, Status=None, NextToken=None, MaxResults=None):
    """
    Requests a list of the changes to quotas for a service.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_requested_service_quota_change_history(
        ServiceCode='string',
        Status='PENDING'|'CASE_OPENED'|'APPROVED'|'DENIED'|'CASE_CLOSED',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type ServiceCode: string
    :param ServiceCode: Specifies the service that you want to use.

    :type Status: string
    :param Status: Specifies the status value of the quota increase request.

    :type NextToken: string
    :param NextToken: (Optional) Use this parameter in a request if you receive a NextToken response in a previous request that indicates that there\'s more output available. In a subsequent call, set it to the value of the previous call\'s NextToken response to indicate where the output should continue from.

    :type MaxResults: integer
    :param MaxResults: (Optional) Limits the number of results that you want to include in the response. If you don\'t include this parameter, the response defaults to a value that\'s specific to the operation. If additional items exist beyond the specified maximum, the NextToken element is present and has a value (isn\'t null). Include that value as the NextToken request parameter in the call to the operation to get the next part of the results. You should check NextToken after every operation to ensure that you receive all of the results.

    :rtype: dict

ReturnsResponse Syntax
{
    'NextToken': 'string',
    'RequestedQuotas': [
        {
            'Id': 'string',
            'CaseId': 'string',
            'ServiceCode': 'string',
            'ServiceName': 'string',
            'QuotaCode': 'string',
            'QuotaName': 'string',
            'DesiredValue': 123.0,
            'Status': 'PENDING'|'CASE_OPENED'|'APPROVED'|'DENIED'|'CASE_CLOSED',
            'Created': datetime(2015, 1, 1),
            'LastUpdated': datetime(2015, 1, 1),
            'Requester': 'string',
            'QuotaArn': 'string',
            'GlobalQuota': True|False,
            'Unit': 'string'
        },
    ]
}


Response Structure

(dict) --

NextToken (string) --
If present in the response, this value indicates there\'s more output available that what\'s included in the current response. This can occur even when the response includes no values at all, such as when you ask for a filtered view of a very long list. Use this value in the NextToken request parameter in a subsequent call to the operation to continue processing and get the next part of the output. You should repeat this until the NextToken response element comes back empty (as null ).

RequestedQuotas (list) --
Returns a list of service quota requests.

(dict) --
A structure that contains information about a requested change for a quota.

Id (string) --
The unique identifier of a requested service quota change.

CaseId (string) --
The case Id for the service quota increase request.

ServiceCode (string) --
Specifies the service that you want to use.

ServiceName (string) --
The name of the AWS service specified in the increase request.

QuotaCode (string) --
Specifies the service quota that you want to use.

QuotaName (string) --
Name of the service quota.

DesiredValue (float) --
New increased value for the service quota.

Status (string) --
State of the service quota increase request.

Created (datetime) --
The date and time when the service quota increase request was received and the case Id was created.

LastUpdated (datetime) --
The date and time of the most recent change in the service quota increase request.

Requester (string) --
The IAM identity who submitted the service quota increase request.

QuotaArn (string) --
The Amazon Resource Name (ARN) of the service quota.

GlobalQuota (boolean) --
Identifies if the quota is global.

Unit (string) --
Specifies the unit used for the quota.











Exceptions

ServiceQuotas.Client.exceptions.AccessDeniedException
ServiceQuotas.Client.exceptions.NoSuchResourceException
ServiceQuotas.Client.exceptions.IllegalArgumentException
ServiceQuotas.Client.exceptions.InvalidPaginationTokenException
ServiceQuotas.Client.exceptions.ServiceException
ServiceQuotas.Client.exceptions.TooManyRequestsException


    :return: {
        'NextToken': 'string',
        'RequestedQuotas': [
            {
                'Id': 'string',
                'CaseId': 'string',
                'ServiceCode': 'string',
                'ServiceName': 'string',
                'QuotaCode': 'string',
                'QuotaName': 'string',
                'DesiredValue': 123.0,
                'Status': 'PENDING'|'CASE_OPENED'|'APPROVED'|'DENIED'|'CASE_CLOSED',
                'Created': datetime(2015, 1, 1),
                'LastUpdated': datetime(2015, 1, 1),
                'Requester': 'string',
                'QuotaArn': 'string',
                'GlobalQuota': True|False,
                'Unit': 'string'
            },
        ]
    }
    
    
    :returns: 
    ServiceQuotas.Client.exceptions.AccessDeniedException
    ServiceQuotas.Client.exceptions.NoSuchResourceException
    ServiceQuotas.Client.exceptions.IllegalArgumentException
    ServiceQuotas.Client.exceptions.InvalidPaginationTokenException
    ServiceQuotas.Client.exceptions.ServiceException
    ServiceQuotas.Client.exceptions.TooManyRequestsException
    
    """
    pass

def list_requested_service_quota_change_history_by_quota(ServiceCode=None, QuotaCode=None, Status=None, NextToken=None, MaxResults=None):
    """
    Requests a list of the changes to specific service quotas. This command provides additional granularity over the ListRequestedServiceQuotaChangeHistory command. Once a quota change request has reached CASE_CLOSED, APPROVED, or DENIED , the history has been kept for 90 days.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_requested_service_quota_change_history_by_quota(
        ServiceCode='string',
        QuotaCode='string',
        Status='PENDING'|'CASE_OPENED'|'APPROVED'|'DENIED'|'CASE_CLOSED',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type ServiceCode: string
    :param ServiceCode: [REQUIRED]\nSpecifies the service that you want to use.\n

    :type QuotaCode: string
    :param QuotaCode: [REQUIRED]\nSpecifies the service quota that you want to use\n

    :type Status: string
    :param Status: Specifies the status value of the quota increase request.

    :type NextToken: string
    :param NextToken: (Optional) Use this parameter in a request if you receive a NextToken response in a previous request that indicates that there\'s more output available. In a subsequent call, set it to the value of the previous call\'s NextToken response to indicate where the output should continue from.

    :type MaxResults: integer
    :param MaxResults: (Optional) Limits the number of results that you want to include in the response. If you don\'t include this parameter, the response defaults to a value that\'s specific to the operation. If additional items exist beyond the specified maximum, the NextToken element is present and has a value (isn\'t null). Include that value as the NextToken request parameter in the call to the operation to get the next part of the results. You should check NextToken after every operation to ensure that you receive all of the results.

    :rtype: dict

ReturnsResponse Syntax
{
    'NextToken': 'string',
    'RequestedQuotas': [
        {
            'Id': 'string',
            'CaseId': 'string',
            'ServiceCode': 'string',
            'ServiceName': 'string',
            'QuotaCode': 'string',
            'QuotaName': 'string',
            'DesiredValue': 123.0,
            'Status': 'PENDING'|'CASE_OPENED'|'APPROVED'|'DENIED'|'CASE_CLOSED',
            'Created': datetime(2015, 1, 1),
            'LastUpdated': datetime(2015, 1, 1),
            'Requester': 'string',
            'QuotaArn': 'string',
            'GlobalQuota': True|False,
            'Unit': 'string'
        },
    ]
}


Response Structure

(dict) --

NextToken (string) --
If present in the response, this value indicates there\'s more output available that what\'s included in the current response. This can occur even when the response includes no values at all, such as when you ask for a filtered view of a very long list. Use this value in the NextToken request parameter in a subsequent call to the operation to continue processing and get the next part of the output. You should repeat this until the NextToken response element comes back empty (as null ).

RequestedQuotas (list) --
Returns a list of service quota requests.

(dict) --
A structure that contains information about a requested change for a quota.

Id (string) --
The unique identifier of a requested service quota change.

CaseId (string) --
The case Id for the service quota increase request.

ServiceCode (string) --
Specifies the service that you want to use.

ServiceName (string) --
The name of the AWS service specified in the increase request.

QuotaCode (string) --
Specifies the service quota that you want to use.

QuotaName (string) --
Name of the service quota.

DesiredValue (float) --
New increased value for the service quota.

Status (string) --
State of the service quota increase request.

Created (datetime) --
The date and time when the service quota increase request was received and the case Id was created.

LastUpdated (datetime) --
The date and time of the most recent change in the service quota increase request.

Requester (string) --
The IAM identity who submitted the service quota increase request.

QuotaArn (string) --
The Amazon Resource Name (ARN) of the service quota.

GlobalQuota (boolean) --
Identifies if the quota is global.

Unit (string) --
Specifies the unit used for the quota.











Exceptions

ServiceQuotas.Client.exceptions.AccessDeniedException
ServiceQuotas.Client.exceptions.NoSuchResourceException
ServiceQuotas.Client.exceptions.IllegalArgumentException
ServiceQuotas.Client.exceptions.InvalidPaginationTokenException
ServiceQuotas.Client.exceptions.ServiceException
ServiceQuotas.Client.exceptions.TooManyRequestsException


    :return: {
        'NextToken': 'string',
        'RequestedQuotas': [
            {
                'Id': 'string',
                'CaseId': 'string',
                'ServiceCode': 'string',
                'ServiceName': 'string',
                'QuotaCode': 'string',
                'QuotaName': 'string',
                'DesiredValue': 123.0,
                'Status': 'PENDING'|'CASE_OPENED'|'APPROVED'|'DENIED'|'CASE_CLOSED',
                'Created': datetime(2015, 1, 1),
                'LastUpdated': datetime(2015, 1, 1),
                'Requester': 'string',
                'QuotaArn': 'string',
                'GlobalQuota': True|False,
                'Unit': 'string'
            },
        ]
    }
    
    
    :returns: 
    ServiceQuotas.Client.exceptions.AccessDeniedException
    ServiceQuotas.Client.exceptions.NoSuchResourceException
    ServiceQuotas.Client.exceptions.IllegalArgumentException
    ServiceQuotas.Client.exceptions.InvalidPaginationTokenException
    ServiceQuotas.Client.exceptions.ServiceException
    ServiceQuotas.Client.exceptions.TooManyRequestsException
    
    """
    pass

def list_service_quota_increase_requests_in_template(ServiceCode=None, AwsRegion=None, NextToken=None, MaxResults=None):
    """
    Returns a list of the quota increase requests in the template.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_service_quota_increase_requests_in_template(
        ServiceCode='string',
        AwsRegion='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type ServiceCode: string
    :param ServiceCode: The identifier for a service. When performing an operation, use the ServiceCode to specify a particular service.

    :type AwsRegion: string
    :param AwsRegion: Specifies the AWS Region for the quota that you want to use.

    :type NextToken: string
    :param NextToken: (Optional) Use this parameter in a request if you receive a NextToken response in a previous request that indicates that there\'s more output available. In a subsequent call, set it to the value of the previous call\'s NextToken response to indicate where the output should continue from.

    :type MaxResults: integer
    :param MaxResults: (Optional) Limits the number of results that you want to include in the response. If you don\'t include this parameter, the response defaults to a value that\'s specific to the operation. If additional items exist beyond the specified maximum, the NextToken element is present and has a value (isn\'t null). Include that value as the NextToken request parameter in the call to the operation to get the next part of the results. You should check NextToken after every operation to ensure that you receive all of the results.

    :rtype: dict

ReturnsResponse Syntax
{
    'ServiceQuotaIncreaseRequestInTemplateList': [
        {
            'ServiceCode': 'string',
            'ServiceName': 'string',
            'QuotaCode': 'string',
            'QuotaName': 'string',
            'DesiredValue': 123.0,
            'AwsRegion': 'string',
            'Unit': 'string',
            'GlobalQuota': True|False
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

ServiceQuotaIncreaseRequestInTemplateList (list) --
Returns the list of values of the quota increase request in the template.

(dict) --
A structure that contains information about one service quota increase request.

ServiceCode (string) --
The code identifier for the AWS service specified in the increase request.

ServiceName (string) --
The name of the AWS service specified in the increase request.

QuotaCode (string) --
The code identifier for the service quota specified in the increase request.

QuotaName (string) --
The name of the service quota in the increase request.

DesiredValue (float) --
Identifies the new, increased value of the service quota in the increase request.

AwsRegion (string) --
The AWS Region where the increase request occurs.

Unit (string) --
The unit of measure for the increase request.

GlobalQuota (boolean) --
Specifies if the quota is a global quota.





NextToken (string) --
If present in the response, this value indicates there\'s more output available that what\'s included in the current response. This can occur even when the response includes no values at all, such as when you ask for a filtered view of a very long list. Use this value in the NextToken request parameter in a subsequent call to the operation to continue processing and get the next part of the output. You should repeat this until the NextToken response element comes back empty (as null ).







Exceptions

ServiceQuotas.Client.exceptions.AccessDeniedException
ServiceQuotas.Client.exceptions.DependencyAccessDeniedException
ServiceQuotas.Client.exceptions.ServiceException
ServiceQuotas.Client.exceptions.TooManyRequestsException
ServiceQuotas.Client.exceptions.IllegalArgumentException
ServiceQuotas.Client.exceptions.AWSServiceAccessNotEnabledException
ServiceQuotas.Client.exceptions.TemplatesNotAvailableInRegionException
ServiceQuotas.Client.exceptions.NoAvailableOrganizationException


    :return: {
        'ServiceQuotaIncreaseRequestInTemplateList': [
            {
                'ServiceCode': 'string',
                'ServiceName': 'string',
                'QuotaCode': 'string',
                'QuotaName': 'string',
                'DesiredValue': 123.0,
                'AwsRegion': 'string',
                'Unit': 'string',
                'GlobalQuota': True|False
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    ServiceQuotas.Client.exceptions.AccessDeniedException
    ServiceQuotas.Client.exceptions.DependencyAccessDeniedException
    ServiceQuotas.Client.exceptions.ServiceException
    ServiceQuotas.Client.exceptions.TooManyRequestsException
    ServiceQuotas.Client.exceptions.IllegalArgumentException
    ServiceQuotas.Client.exceptions.AWSServiceAccessNotEnabledException
    ServiceQuotas.Client.exceptions.TemplatesNotAvailableInRegionException
    ServiceQuotas.Client.exceptions.NoAvailableOrganizationException
    
    """
    pass

def list_service_quotas(ServiceCode=None, NextToken=None, MaxResults=None):
    """
    Lists all service quotas for the specified AWS service. This request returns a list of the service quotas for the specified service. you\'ll see the default values are the values that AWS provides for the quotas.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_service_quotas(
        ServiceCode='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type ServiceCode: string
    :param ServiceCode: [REQUIRED]\nThe identifier for a service. When performing an operation, use the ServiceCode to specify a particular service.\n

    :type NextToken: string
    :param NextToken: (Optional) Use this parameter in a request if you receive a NextToken response in a previous request that indicates that there\'s more output available. In a subsequent call, set it to the value of the previous call\'s NextToken response to indicate where the output should continue from.

    :type MaxResults: integer
    :param MaxResults: (Optional) Limits the number of results that you want to include in the response. If you don\'t include this parameter, the response defaults to a value that\'s specific to the operation. If additional items exist beyond the specified maximum, the NextToken element is present and has a value (isn\'t null). Include that value as the NextToken request parameter in the call to the operation to get the next part of the results. You should check NextToken after every operation to ensure that you receive all of the results.

    :rtype: dict

ReturnsResponse Syntax
{
    'NextToken': 'string',
    'Quotas': [
        {
            'ServiceCode': 'string',
            'ServiceName': 'string',
            'QuotaArn': 'string',
            'QuotaCode': 'string',
            'QuotaName': 'string',
            'Value': 123.0,
            'Unit': 'string',
            'Adjustable': True|False,
            'GlobalQuota': True|False,
            'UsageMetric': {
                'MetricNamespace': 'string',
                'MetricName': 'string',
                'MetricDimensions': {
                    'string': 'string'
                },
                'MetricStatisticRecommendation': 'string'
            },
            'Period': {
                'PeriodValue': 123,
                'PeriodUnit': 'MICROSECOND'|'MILLISECOND'|'SECOND'|'MINUTE'|'HOUR'|'DAY'|'WEEK'
            },
            'ErrorReason': {
                'ErrorCode': 'DEPENDENCY_ACCESS_DENIED_ERROR'|'DEPENDENCY_THROTTLING_ERROR'|'DEPENDENCY_SERVICE_ERROR'|'SERVICE_QUOTA_NOT_AVAILABLE_ERROR',
                'ErrorMessage': 'string'
            }
        },
    ]
}


Response Structure

(dict) --

NextToken (string) --
If present in the response, this value indicates there\'s more output available that what\'s included in the current response. This can occur even when the response includes no values at all, such as when you ask for a filtered view of a very long list. Use this value in the NextToken request parameter in a subsequent call to the operation to continue processing and get the next part of the output. You should repeat this until the NextToken response element comes back empty (as null ).

Quotas (list) --
The response information for a quota lists all attribute information for the quota.

(dict) --
A structure that contains the full set of details that define the service quota.

ServiceCode (string) --
Specifies the service that you want to use.

ServiceName (string) --
The name of the AWS service specified in the increase request.

QuotaArn (string) --
The Amazon Resource Name (ARN) of the service quota.

QuotaCode (string) --
The code identifier for the service quota specified.

QuotaName (string) --
The name identifier of the service quota.

Value (float) --
The value of service quota.

Unit (string) --
The unit of measurement for the value of the service quota.

Adjustable (boolean) --
Specifies if the quota value can be increased.

GlobalQuota (boolean) --
Specifies if the quota is global.

UsageMetric (dict) --
Specifies the details about the measurement.

MetricNamespace (string) --
The namespace of the metric. The namespace is a container for CloudWatch metrics. You can specify a name for the namespace when you create a metric.

MetricName (string) --
The name of the CloudWatch metric that measures usage of a service quota. This is a required field.

MetricDimensions (dict) --
A dimension is a name/value pair that is part of the identity of a metric. Every metric has specific characteristics that describe it, and you can think of dimensions as categories for those characteristics. These dimensions are part of the CloudWatch Metric Identity that measures usage against a particular service quota.

(string) --
(string) --




MetricStatisticRecommendation (string) --
Statistics are metric data aggregations over specified periods of time. This is the recommended statistic to use when comparing usage in the CloudWatch Metric against your Service Quota.



Period (dict) --
Identifies the unit and value of how time is measured.

PeriodValue (integer) --
The value of a period.

PeriodUnit (string) --
The time unit of a period.



ErrorReason (dict) --
Specifies the ErrorCode and ErrorMessage when success isn\'t achieved.

ErrorCode (string) --
Service Quotas returns the following error values.

DEPENDENCY_ACCESS_DENIED_ERROR is returned when the caller does not have permission to call the service or service quota. To resolve the error, you need permission to access the service or service quota.
DEPENDENCY_THROTTLING_ERROR is returned when the service being called is throttling Service Quotas.
DEPENDENCY_SERVICE_ERROR is returned when the service being called has availability issues.
SERVICE_QUOTA_NOT_AVAILABLE_ERROR is returned when there was an error in Service Quotas.


ErrorMessage (string) --
The error message that provides more detail.













Exceptions

ServiceQuotas.Client.exceptions.AccessDeniedException
ServiceQuotas.Client.exceptions.NoSuchResourceException
ServiceQuotas.Client.exceptions.IllegalArgumentException
ServiceQuotas.Client.exceptions.InvalidPaginationTokenException
ServiceQuotas.Client.exceptions.ServiceException
ServiceQuotas.Client.exceptions.TooManyRequestsException


    :return: {
        'NextToken': 'string',
        'Quotas': [
            {
                'ServiceCode': 'string',
                'ServiceName': 'string',
                'QuotaArn': 'string',
                'QuotaCode': 'string',
                'QuotaName': 'string',
                'Value': 123.0,
                'Unit': 'string',
                'Adjustable': True|False,
                'GlobalQuota': True|False,
                'UsageMetric': {
                    'MetricNamespace': 'string',
                    'MetricName': 'string',
                    'MetricDimensions': {
                        'string': 'string'
                    },
                    'MetricStatisticRecommendation': 'string'
                },
                'Period': {
                    'PeriodValue': 123,
                    'PeriodUnit': 'MICROSECOND'|'MILLISECOND'|'SECOND'|'MINUTE'|'HOUR'|'DAY'|'WEEK'
                },
                'ErrorReason': {
                    'ErrorCode': 'DEPENDENCY_ACCESS_DENIED_ERROR'|'DEPENDENCY_THROTTLING_ERROR'|'DEPENDENCY_SERVICE_ERROR'|'SERVICE_QUOTA_NOT_AVAILABLE_ERROR',
                    'ErrorMessage': 'string'
                }
            },
        ]
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def list_services(NextToken=None, MaxResults=None):
    """
    Lists the AWS services available in Service Quotas. Not all AWS services are available in Service Quotas. To list the see the list of the service quotas for a specific service, use  ListServiceQuotas .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_services(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: (Optional) Use this parameter in a request if you receive a NextToken response in a previous request that indicates that there\'s more output available. In a subsequent call, set it to the value of the previous call\'s NextToken response to indicate where the output should continue from.

    :type MaxResults: integer
    :param MaxResults: (Optional) Limits the number of results that you want to include in the response. If you don\'t include this parameter, the response defaults to a value that\'s specific to the operation. If additional items exist beyond the specified maximum, the NextToken element is present and has a value (isn\'t null). Include that value as the NextToken request parameter in the call to the operation to get the next part of the results. You should check NextToken after every operation to ensure that you receive all of the results.

    :rtype: dict

ReturnsResponse Syntax
{
    'NextToken': 'string',
    'Services': [
        {
            'ServiceCode': 'string',
            'ServiceName': 'string'
        },
    ]
}


Response Structure

(dict) --

NextToken (string) --
If present in the response, this value indicates there\'s more output available that what\'s included in the current response. This can occur even when the response includes no values at all, such as when you ask for a filtered view of a very long list. Use this value in the NextToken request parameter in a subsequent call to the operation to continue processing and get the next part of the output. You should repeat this until the NextToken response element comes back empty (as null ).

Services (list) --
Returns a list of services.

(dict) --
A structure that contains the ServiceName and ServiceCode . It does not include all details of the service quota. To get those values, use the  ListServiceQuotas operation.

ServiceCode (string) --
Specifies the service that you want to use.

ServiceName (string) --
The name of the AWS service specified in the increase request.











Exceptions

ServiceQuotas.Client.exceptions.AccessDeniedException
ServiceQuotas.Client.exceptions.IllegalArgumentException
ServiceQuotas.Client.exceptions.InvalidPaginationTokenException
ServiceQuotas.Client.exceptions.ServiceException
ServiceQuotas.Client.exceptions.TooManyRequestsException


    :return: {
        'NextToken': 'string',
        'Services': [
            {
                'ServiceCode': 'string',
                'ServiceName': 'string'
            },
        ]
    }
    
    
    :returns: 
    ServiceQuotas.Client.exceptions.AccessDeniedException
    ServiceQuotas.Client.exceptions.IllegalArgumentException
    ServiceQuotas.Client.exceptions.InvalidPaginationTokenException
    ServiceQuotas.Client.exceptions.ServiceException
    ServiceQuotas.Client.exceptions.TooManyRequestsException
    
    """
    pass

def put_service_quota_increase_request_into_template(QuotaCode=None, ServiceCode=None, AwsRegion=None, DesiredValue=None):
    """
    Defines and adds a quota to the service quota template. To add a quota to the template, you must provide the ServiceCode , QuotaCode , AwsRegion , and DesiredValue . Once you add a quota to the template, use  ListServiceQuotaIncreaseRequestsInTemplate to see the list of quotas in the template.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_service_quota_increase_request_into_template(
        QuotaCode='string',
        ServiceCode='string',
        AwsRegion='string',
        DesiredValue=123.0
    )
    
    
    :type QuotaCode: string
    :param QuotaCode: [REQUIRED]\nSpecifies the service quota that you want to use.\n

    :type ServiceCode: string
    :param ServiceCode: [REQUIRED]\nSpecifies the service that you want to use.\n

    :type AwsRegion: string
    :param AwsRegion: [REQUIRED]\nSpecifies the AWS Region for the quota.\n

    :type DesiredValue: float
    :param DesiredValue: [REQUIRED]\nSpecifies the new, increased value for the quota.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ServiceQuotaIncreaseRequestInTemplate': {
        'ServiceCode': 'string',
        'ServiceName': 'string',
        'QuotaCode': 'string',
        'QuotaName': 'string',
        'DesiredValue': 123.0,
        'AwsRegion': 'string',
        'Unit': 'string',
        'GlobalQuota': True|False
    }
}


Response Structure

(dict) --

ServiceQuotaIncreaseRequestInTemplate (dict) --
A structure that contains information about one service quota increase request.

ServiceCode (string) --
The code identifier for the AWS service specified in the increase request.

ServiceName (string) --
The name of the AWS service specified in the increase request.

QuotaCode (string) --
The code identifier for the service quota specified in the increase request.

QuotaName (string) --
The name of the service quota in the increase request.

DesiredValue (float) --
Identifies the new, increased value of the service quota in the increase request.

AwsRegion (string) --
The AWS Region where the increase request occurs.

Unit (string) --
The unit of measure for the increase request.

GlobalQuota (boolean) --
Specifies if the quota is a global quota.









Exceptions

ServiceQuotas.Client.exceptions.AccessDeniedException
ServiceQuotas.Client.exceptions.DependencyAccessDeniedException
ServiceQuotas.Client.exceptions.ServiceException
ServiceQuotas.Client.exceptions.TooManyRequestsException
ServiceQuotas.Client.exceptions.IllegalArgumentException
ServiceQuotas.Client.exceptions.QuotaExceededException
ServiceQuotas.Client.exceptions.NoSuchResourceException
ServiceQuotas.Client.exceptions.AWSServiceAccessNotEnabledException
ServiceQuotas.Client.exceptions.TemplatesNotAvailableInRegionException
ServiceQuotas.Client.exceptions.NoAvailableOrganizationException


    :return: {
        'ServiceQuotaIncreaseRequestInTemplate': {
            'ServiceCode': 'string',
            'ServiceName': 'string',
            'QuotaCode': 'string',
            'QuotaName': 'string',
            'DesiredValue': 123.0,
            'AwsRegion': 'string',
            'Unit': 'string',
            'GlobalQuota': True|False
        }
    }
    
    
    :returns: 
    ServiceQuotas.Client.exceptions.AccessDeniedException
    ServiceQuotas.Client.exceptions.DependencyAccessDeniedException
    ServiceQuotas.Client.exceptions.ServiceException
    ServiceQuotas.Client.exceptions.TooManyRequestsException
    ServiceQuotas.Client.exceptions.IllegalArgumentException
    ServiceQuotas.Client.exceptions.QuotaExceededException
    ServiceQuotas.Client.exceptions.NoSuchResourceException
    ServiceQuotas.Client.exceptions.AWSServiceAccessNotEnabledException
    ServiceQuotas.Client.exceptions.TemplatesNotAvailableInRegionException
    ServiceQuotas.Client.exceptions.NoAvailableOrganizationException
    
    """
    pass

def request_service_quota_increase(ServiceCode=None, QuotaCode=None, DesiredValue=None):
    """
    Retrieves the details of a service quota increase request. The response to this command provides the details in the  RequestedServiceQuotaChange object.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.request_service_quota_increase(
        ServiceCode='string',
        QuotaCode='string',
        DesiredValue=123.0
    )
    
    
    :type ServiceCode: string
    :param ServiceCode: [REQUIRED]\nSpecifies the service that you want to use.\n

    :type QuotaCode: string
    :param QuotaCode: [REQUIRED]\nSpecifies the service quota that you want to use.\n

    :type DesiredValue: float
    :param DesiredValue: [REQUIRED]\nSpecifies the value submitted in the service quota increase request.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'RequestedQuota': {
        'Id': 'string',
        'CaseId': 'string',
        'ServiceCode': 'string',
        'ServiceName': 'string',
        'QuotaCode': 'string',
        'QuotaName': 'string',
        'DesiredValue': 123.0,
        'Status': 'PENDING'|'CASE_OPENED'|'APPROVED'|'DENIED'|'CASE_CLOSED',
        'Created': datetime(2015, 1, 1),
        'LastUpdated': datetime(2015, 1, 1),
        'Requester': 'string',
        'QuotaArn': 'string',
        'GlobalQuota': True|False,
        'Unit': 'string'
    }
}


Response Structure

(dict) --

RequestedQuota (dict) --
Returns a list of service quota requests.

Id (string) --
The unique identifier of a requested service quota change.

CaseId (string) --
The case Id for the service quota increase request.

ServiceCode (string) --
Specifies the service that you want to use.

ServiceName (string) --
The name of the AWS service specified in the increase request.

QuotaCode (string) --
Specifies the service quota that you want to use.

QuotaName (string) --
Name of the service quota.

DesiredValue (float) --
New increased value for the service quota.

Status (string) --
State of the service quota increase request.

Created (datetime) --
The date and time when the service quota increase request was received and the case Id was created.

LastUpdated (datetime) --
The date and time of the most recent change in the service quota increase request.

Requester (string) --
The IAM identity who submitted the service quota increase request.

QuotaArn (string) --
The Amazon Resource Name (ARN) of the service quota.

GlobalQuota (boolean) --
Identifies if the quota is global.

Unit (string) --
Specifies the unit used for the quota.









Exceptions

ServiceQuotas.Client.exceptions.DependencyAccessDeniedException
ServiceQuotas.Client.exceptions.QuotaExceededException
ServiceQuotas.Client.exceptions.ResourceAlreadyExistsException
ServiceQuotas.Client.exceptions.AccessDeniedException
ServiceQuotas.Client.exceptions.NoSuchResourceException
ServiceQuotas.Client.exceptions.IllegalArgumentException
ServiceQuotas.Client.exceptions.InvalidResourceStateException
ServiceQuotas.Client.exceptions.ServiceException
ServiceQuotas.Client.exceptions.TooManyRequestsException


    :return: {
        'RequestedQuota': {
            'Id': 'string',
            'CaseId': 'string',
            'ServiceCode': 'string',
            'ServiceName': 'string',
            'QuotaCode': 'string',
            'QuotaName': 'string',
            'DesiredValue': 123.0,
            'Status': 'PENDING'|'CASE_OPENED'|'APPROVED'|'DENIED'|'CASE_CLOSED',
            'Created': datetime(2015, 1, 1),
            'LastUpdated': datetime(2015, 1, 1),
            'Requester': 'string',
            'QuotaArn': 'string',
            'GlobalQuota': True|False,
            'Unit': 'string'
        }
    }
    
    
    :returns: 
    ServiceQuotas.Client.exceptions.DependencyAccessDeniedException
    ServiceQuotas.Client.exceptions.QuotaExceededException
    ServiceQuotas.Client.exceptions.ResourceAlreadyExistsException
    ServiceQuotas.Client.exceptions.AccessDeniedException
    ServiceQuotas.Client.exceptions.NoSuchResourceException
    ServiceQuotas.Client.exceptions.IllegalArgumentException
    ServiceQuotas.Client.exceptions.InvalidResourceStateException
    ServiceQuotas.Client.exceptions.ServiceException
    ServiceQuotas.Client.exceptions.TooManyRequestsException
    
    """
    pass

