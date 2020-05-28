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

def get_auto_scaling_group_recommendations(accountIds=None, autoScalingGroupArns=None, nextToken=None, maxResults=None, filters=None):
    """
    Returns Auto Scaling group recommendations.
    AWS Compute Optimizer currently generates recommendations for Auto Scaling groups that are configured to run instances of the M, C, R, T, and X instance families. The service does not generate recommendations for Auto Scaling groups that have a scaling policy attached to them, or that do not have the same values for desired, minimum, and maximum capacity. In order for Compute Optimizer to analyze your Auto Scaling groups, they must be of a fixed size. For more information, see the AWS Compute Optimizer User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_auto_scaling_group_recommendations(
        accountIds=[
            'string',
        ],
        autoScalingGroupArns=[
            'string',
        ],
        nextToken='string',
        maxResults=123,
        filters=[
            {
                'name': 'Finding'|'RecommendationSourceType',
                'values': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type accountIds: list
    :param accountIds: The AWS account IDs for which to return Auto Scaling group recommendations.\nOnly one account ID can be specified per request.\n\n(string) --\n\n

    :type autoScalingGroupArns: list
    :param autoScalingGroupArns: The Amazon Resource Name (ARN) of the Auto Scaling groups for which to return recommendations.\n\n(string) --\n\n

    :type nextToken: string
    :param nextToken: The token to advance to the next page of Auto Scaling group recommendations.

    :type maxResults: integer
    :param maxResults: The maximum number of Auto Scaling group recommendations to return with a single call.\nTo retrieve the remaining results, make another call with the returned NextToken value.\n

    :type filters: list
    :param filters: An array of objects that describe a filter that returns a more specific list of Auto Scaling group recommendations.\n\n(dict) --Describes a filter that returns a more specific list of recommendations.\n\nname (string) --The name of the filter.\nSpecify Finding to filter the results to a specific findings classification.\nSpecify RecommendationSourceType to filter the results to a specific resource type.\n\nvalues (list) --The value of the filter.\nIf you specify the name parameter as Finding , and you\'re recommendations for an instance , then the valid values are Underprovisioned , Overprovisioned , NotOptimized , or Optimized .\nIf you specify the name parameter as Finding , and you\'re recommendations for an Auto Scaling group , then the valid values are Optimized , or NotOptimized .\nIf you specify the name parameter as RecommendationSourceType , then the valid values are EC2Instance , or AutoScalingGroup .\n\n(string) --\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'nextToken': 'string',
    'autoScalingGroupRecommendations': [
        {
            'accountId': 'string',
            'autoScalingGroupArn': 'string',
            'autoScalingGroupName': 'string',
            'finding': 'Underprovisioned'|'Overprovisioned'|'Optimized'|'NotOptimized',
            'utilizationMetrics': [
                {
                    'name': 'Cpu'|'Memory',
                    'statistic': 'Maximum'|'Average',
                    'value': 123.0
                },
            ],
            'lookBackPeriodInDays': 123.0,
            'currentConfiguration': {
                'desiredCapacity': 123,
                'minSize': 123,
                'maxSize': 123,
                'instanceType': 'string'
            },
            'recommendationOptions': [
                {
                    'configuration': {
                        'desiredCapacity': 123,
                        'minSize': 123,
                        'maxSize': 123,
                        'instanceType': 'string'
                    },
                    'projectedUtilizationMetrics': [
                        {
                            'name': 'Cpu'|'Memory',
                            'statistic': 'Maximum'|'Average',
                            'value': 123.0
                        },
                    ],
                    'performanceRisk': 123.0,
                    'rank': 123
                },
            ],
            'lastRefreshTimestamp': datetime(2015, 1, 1)
        },
    ],
    'errors': [
        {
            'identifier': 'string',
            'code': 'string',
            'message': 'string'
        },
    ]
}


Response Structure

(dict) --

nextToken (string) --
The token to use to advance to the next page of Auto Scaling group recommendations.
This value is null when there are no more pages of Auto Scaling group recommendations to return.

autoScalingGroupRecommendations (list) --
An array of objects that describe Auto Scaling group recommendations.

(dict) --
Describes an Auto Scaling group recommendation.

accountId (string) --
The AWS account ID of the Auto Scaling group.

autoScalingGroupArn (string) --
The Amazon Resource Name (ARN) of the Auto Scaling group.

autoScalingGroupName (string) --
The name of the Auto Scaling group.

finding (string) --
The finding classification for the Auto Scaling group.
Findings for Auto Scaling groups include:

**NotOptimized ** \xe2\x80\x94An Auto Scaling group is considered not optimized when AWS Compute Optimizer identifies a recommendation that can provide better performance for your workload.
**Optimized ** \xe2\x80\x94An Auto Scaling group is considered optimized when Compute Optimizer determines that the group is correctly provisioned to run your workload based on the chosen instance type. For optimized resources, Compute Optimizer might recommend a new generation instance type.


Note
The values that are returned might be NOT_OPTIMIZED or OPTIMIZED .


utilizationMetrics (list) --
An array of objects that describe the utilization metrics of the Auto Scaling group.

(dict) --
Describes a utilization metric of a resource, such as an Amazon EC2 instance.

name (string) --
The name of the utilization metric.

Note
Memory metrics are only returned for resources that have the unified CloudWatch agent installed on them. For more information, see Enabling Memory Utilization with the CloudWatch Agent .


statistic (string) --
The statistic of the utilization metric.

value (float) --
The value of the utilization metric.





lookBackPeriodInDays (float) --
The number of days for which utilization metrics were analyzed for the Auto Scaling group.

currentConfiguration (dict) --
An array of objects that describe the current configuration of the Auto Scaling group.

desiredCapacity (integer) --
The desired capacity, or number of instances, for the Auto Scaling group.

minSize (integer) --
The minimum size, or minimum number of instances, for the Auto Scaling group.

maxSize (integer) --
The maximum size, or maximum number of instances, for the Auto Scaling group.

instanceType (string) --
The instance type for the Auto Scaling group.



recommendationOptions (list) --
An array of objects that describe the recommendation options for the Auto Scaling group.

(dict) --
Describes a recommendation option for an Auto Scaling group.

configuration (dict) --
An array of objects that describe an Auto Scaling group configuration.

desiredCapacity (integer) --
The desired capacity, or number of instances, for the Auto Scaling group.

minSize (integer) --
The minimum size, or minimum number of instances, for the Auto Scaling group.

maxSize (integer) --
The maximum size, or maximum number of instances, for the Auto Scaling group.

instanceType (string) --
The instance type for the Auto Scaling group.



projectedUtilizationMetrics (list) --
An array of objects that describe the projected utilization metrics of the Auto Scaling group recommendation option.

(dict) --
Describes a utilization metric of a resource, such as an Amazon EC2 instance.

name (string) --
The name of the utilization metric.

Note
Memory metrics are only returned for resources that have the unified CloudWatch agent installed on them. For more information, see Enabling Memory Utilization with the CloudWatch Agent .


statistic (string) --
The statistic of the utilization metric.

value (float) --
The value of the utilization metric.





performanceRisk (float) --
The performance risk of the Auto Scaling group configuration recommendation.
Performance risk is the likelihood of the recommended instance type not meeting the performance requirement of your workload.
The lowest performance risk is categorized as 0 , and the highest as 5 .

rank (integer) --
The rank of the Auto Scaling group recommendation option.
The top recommendation option is ranked as 1 .





lastRefreshTimestamp (datetime) --
The time stamp of when the Auto Scaling group recommendation was last refreshed.





errors (list) --
An array of objects that describe errors of the request.
For example, an error is returned if you request recommendations for an unsupported Auto Scaling group.

(dict) --
Describes an error experienced when getting recommendations.
For example, an error is returned if you request recommendations for an unsupported Auto Scaling group, or if you request recommendations for an instance of an unsupported instance family.

identifier (string) --
The ID of the error.

code (string) --
The error code.

message (string) --
The message, or reason, for the error.











Exceptions

ComputeOptimizer.Client.exceptions.OptInRequiredException
ComputeOptimizer.Client.exceptions.InternalServerException
ComputeOptimizer.Client.exceptions.ServiceUnavailableException
ComputeOptimizer.Client.exceptions.AccessDeniedException
ComputeOptimizer.Client.exceptions.InvalidParameterValueException
ComputeOptimizer.Client.exceptions.ResourceNotFoundException
ComputeOptimizer.Client.exceptions.MissingAuthenticationToken
ComputeOptimizer.Client.exceptions.ThrottlingException


    :return: {
        'nextToken': 'string',
        'autoScalingGroupRecommendations': [
            {
                'accountId': 'string',
                'autoScalingGroupArn': 'string',
                'autoScalingGroupName': 'string',
                'finding': 'Underprovisioned'|'Overprovisioned'|'Optimized'|'NotOptimized',
                'utilizationMetrics': [
                    {
                        'name': 'Cpu'|'Memory',
                        'statistic': 'Maximum'|'Average',
                        'value': 123.0
                    },
                ],
                'lookBackPeriodInDays': 123.0,
                'currentConfiguration': {
                    'desiredCapacity': 123,
                    'minSize': 123,
                    'maxSize': 123,
                    'instanceType': 'string'
                },
                'recommendationOptions': [
                    {
                        'configuration': {
                            'desiredCapacity': 123,
                            'minSize': 123,
                            'maxSize': 123,
                            'instanceType': 'string'
                        },
                        'projectedUtilizationMetrics': [
                            {
                                'name': 'Cpu'|'Memory',
                                'statistic': 'Maximum'|'Average',
                                'value': 123.0
                            },
                        ],
                        'performanceRisk': 123.0,
                        'rank': 123
                    },
                ],
                'lastRefreshTimestamp': datetime(2015, 1, 1)
            },
        ],
        'errors': [
            {
                'identifier': 'string',
                'code': 'string',
                'message': 'string'
            },
        ]
    }
    
    
    :returns: 
    **NotOptimized ** \xe2\x80\x94An Auto Scaling group is considered not optimized when AWS Compute Optimizer identifies a recommendation that can provide better performance for your workload.
    **Optimized ** \xe2\x80\x94An Auto Scaling group is considered optimized when Compute Optimizer determines that the group is correctly provisioned to run your workload based on the chosen instance type. For optimized resources, Compute Optimizer might recommend a new generation instance type.
    
    """
    pass

def get_ec2_instance_recommendations(instanceArns=None, nextToken=None, maxResults=None, filters=None, accountIds=None):
    """
    Returns Amazon EC2 instance recommendations.
    AWS Compute Optimizer currently generates recommendations for Amazon Elastic Compute Cloud (Amazon EC2) and Amazon EC2 Auto Scaling. It generates recommendations for M, C, R, T, and X instance families. For more information, see the AWS Compute Optimizer User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_ec2_instance_recommendations(
        instanceArns=[
            'string',
        ],
        nextToken='string',
        maxResults=123,
        filters=[
            {
                'name': 'Finding'|'RecommendationSourceType',
                'values': [
                    'string',
                ]
            },
        ],
        accountIds=[
            'string',
        ]
    )
    
    
    :type instanceArns: list
    :param instanceArns: The Amazon Resource Name (ARN) of the instances for which to return recommendations.\n\n(string) --\n\n

    :type nextToken: string
    :param nextToken: The token to advance to the next page of instance recommendations.

    :type maxResults: integer
    :param maxResults: The maximum number of instance recommendations to return with a single call.\nTo retrieve the remaining results, make another call with the returned NextToken value.\n

    :type filters: list
    :param filters: An array of objects that describe a filter that returns a more specific list of instance recommendations.\n\n(dict) --Describes a filter that returns a more specific list of recommendations.\n\nname (string) --The name of the filter.\nSpecify Finding to filter the results to a specific findings classification.\nSpecify RecommendationSourceType to filter the results to a specific resource type.\n\nvalues (list) --The value of the filter.\nIf you specify the name parameter as Finding , and you\'re recommendations for an instance , then the valid values are Underprovisioned , Overprovisioned , NotOptimized , or Optimized .\nIf you specify the name parameter as Finding , and you\'re recommendations for an Auto Scaling group , then the valid values are Optimized , or NotOptimized .\nIf you specify the name parameter as RecommendationSourceType , then the valid values are EC2Instance , or AutoScalingGroup .\n\n(string) --\n\n\n\n\n\n

    :type accountIds: list
    :param accountIds: The AWS account IDs for which to return instance recommendations.\nOnly one account ID can be specified per request.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'nextToken': 'string',
    'instanceRecommendations': [
        {
            'instanceArn': 'string',
            'accountId': 'string',
            'instanceName': 'string',
            'currentInstanceType': 'string',
            'finding': 'Underprovisioned'|'Overprovisioned'|'Optimized'|'NotOptimized',
            'utilizationMetrics': [
                {
                    'name': 'Cpu'|'Memory',
                    'statistic': 'Maximum'|'Average',
                    'value': 123.0
                },
            ],
            'lookBackPeriodInDays': 123.0,
            'recommendationOptions': [
                {
                    'instanceType': 'string',
                    'projectedUtilizationMetrics': [
                        {
                            'name': 'Cpu'|'Memory',
                            'statistic': 'Maximum'|'Average',
                            'value': 123.0
                        },
                    ],
                    'performanceRisk': 123.0,
                    'rank': 123
                },
            ],
            'recommendationSources': [
                {
                    'recommendationSourceArn': 'string',
                    'recommendationSourceType': 'Ec2Instance'|'AutoScalingGroup'
                },
            ],
            'lastRefreshTimestamp': datetime(2015, 1, 1)
        },
    ],
    'errors': [
        {
            'identifier': 'string',
            'code': 'string',
            'message': 'string'
        },
    ]
}


Response Structure

(dict) --

nextToken (string) --
The token to use to advance to the next page of instance recommendations.
This value is null when there are no more pages of instance recommendations to return.

instanceRecommendations (list) --
An array of objects that describe instance recommendations.

(dict) --
Describes an Amazon EC2 instance recommendation.

instanceArn (string) --
The Amazon Resource Name (ARN) of the current instance.

accountId (string) --
The AWS account ID of the instance recommendation.

instanceName (string) --
The name of the current instance.

currentInstanceType (string) --
The instance type of the current instance.

finding (string) --
The finding classification for the instance.
Findings for instances include:

**Underprovisioned ** \xe2\x80\x94An instance is considered under-provisioned when at least one specification of your instance, such as CPU, memory, or network, does not meet the performance requirements of your workload. Under-provisioned instances may lead to poor application performance.
**Overprovisioned ** \xe2\x80\x94An instance is considered over-provisioned when at least one specification of your instance, such as CPU, memory, or network, can be sized down while still meeting the performance requirements of your workload, and no specification is under-provisioned. Over-provisioned instances may lead to unnecessary infrastructure cost.
**Optimized ** \xe2\x80\x94An instance is considered optimized when all specifications of your instance, such as CPU, memory, and network, meet the performance requirements of your workload and is not over provisioned. An optimized instance runs your workloads with optimal performance and infrastructure cost. For optimized resources, AWS Compute Optimizer might recommend a new generation instance type.


Note
The values that are returned might be UNDER_PROVISIONED , OVER_PROVISIONED , or OPTIMIZED .


utilizationMetrics (list) --
An array of objects that describe the utilization metrics of the instance.

(dict) --
Describes a utilization metric of a resource, such as an Amazon EC2 instance.

name (string) --
The name of the utilization metric.

Note
Memory metrics are only returned for resources that have the unified CloudWatch agent installed on them. For more information, see Enabling Memory Utilization with the CloudWatch Agent .


statistic (string) --
The statistic of the utilization metric.

value (float) --
The value of the utilization metric.





lookBackPeriodInDays (float) --
The number of days for which utilization metrics were analyzed for the instance.

recommendationOptions (list) --
An array of objects that describe the recommendation options for the instance.

(dict) --
Describes a recommendation option for an Amazon EC2 instance.

instanceType (string) --
The instance type of the instance recommendation.

projectedUtilizationMetrics (list) --
An array of objects that describe the projected utilization metrics of the instance recommendation option.

(dict) --
Describes a utilization metric of a resource, such as an Amazon EC2 instance.

name (string) --
The name of the utilization metric.

Note
Memory metrics are only returned for resources that have the unified CloudWatch agent installed on them. For more information, see Enabling Memory Utilization with the CloudWatch Agent .


statistic (string) --
The statistic of the utilization metric.

value (float) --
The value of the utilization metric.





performanceRisk (float) --
The performance risk of the instance recommendation option.
Performance risk is the likelihood of the recommended instance type not meeting the performance requirement of your workload.
The lowest performance risk is categorized as 0 , and the highest as 5 .

rank (integer) --
The rank of the instance recommendation option.
The top recommendation option is ranked as 1 .





recommendationSources (list) --
An array of objects that describe the source resource of the recommendation.

(dict) --
Describes the source of a recommendation, such as an Amazon EC2 instance or Auto Scaling group.

recommendationSourceArn (string) --
The Amazon Resource Name (ARN) of the recommendation source.

recommendationSourceType (string) --
The resource type of the recommendation source.





lastRefreshTimestamp (datetime) --
The time stamp of when the instance recommendation was last refreshed.





errors (list) --
An array of objects that describe errors of the request.
For example, an error is returned if you request recommendations for an instance of an unsupported instance family.

(dict) --
Describes an error experienced when getting recommendations.
For example, an error is returned if you request recommendations for an unsupported Auto Scaling group, or if you request recommendations for an instance of an unsupported instance family.

identifier (string) --
The ID of the error.

code (string) --
The error code.

message (string) --
The message, or reason, for the error.











Exceptions

ComputeOptimizer.Client.exceptions.OptInRequiredException
ComputeOptimizer.Client.exceptions.InternalServerException
ComputeOptimizer.Client.exceptions.ServiceUnavailableException
ComputeOptimizer.Client.exceptions.AccessDeniedException
ComputeOptimizer.Client.exceptions.InvalidParameterValueException
ComputeOptimizer.Client.exceptions.ResourceNotFoundException
ComputeOptimizer.Client.exceptions.MissingAuthenticationToken
ComputeOptimizer.Client.exceptions.ThrottlingException


    :return: {
        'nextToken': 'string',
        'instanceRecommendations': [
            {
                'instanceArn': 'string',
                'accountId': 'string',
                'instanceName': 'string',
                'currentInstanceType': 'string',
                'finding': 'Underprovisioned'|'Overprovisioned'|'Optimized'|'NotOptimized',
                'utilizationMetrics': [
                    {
                        'name': 'Cpu'|'Memory',
                        'statistic': 'Maximum'|'Average',
                        'value': 123.0
                    },
                ],
                'lookBackPeriodInDays': 123.0,
                'recommendationOptions': [
                    {
                        'instanceType': 'string',
                        'projectedUtilizationMetrics': [
                            {
                                'name': 'Cpu'|'Memory',
                                'statistic': 'Maximum'|'Average',
                                'value': 123.0
                            },
                        ],
                        'performanceRisk': 123.0,
                        'rank': 123
                    },
                ],
                'recommendationSources': [
                    {
                        'recommendationSourceArn': 'string',
                        'recommendationSourceType': 'Ec2Instance'|'AutoScalingGroup'
                    },
                ],
                'lastRefreshTimestamp': datetime(2015, 1, 1)
            },
        ],
        'errors': [
            {
                'identifier': 'string',
                'code': 'string',
                'message': 'string'
            },
        ]
    }
    
    
    :returns: 
    **Underprovisioned ** \xe2\x80\x94An instance is considered under-provisioned when at least one specification of your instance, such as CPU, memory, or network, does not meet the performance requirements of your workload. Under-provisioned instances may lead to poor application performance.
    **Overprovisioned ** \xe2\x80\x94An instance is considered over-provisioned when at least one specification of your instance, such as CPU, memory, or network, can be sized down while still meeting the performance requirements of your workload, and no specification is under-provisioned. Over-provisioned instances may lead to unnecessary infrastructure cost.
    **Optimized ** \xe2\x80\x94An instance is considered optimized when all specifications of your instance, such as CPU, memory, and network, meet the performance requirements of your workload and is not over provisioned. An optimized instance runs your workloads with optimal performance and infrastructure cost. For optimized resources, AWS Compute Optimizer might recommend a new generation instance type.
    
    """
    pass

def get_ec2_recommendation_projected_metrics(instanceArn=None, stat=None, period=None, startTime=None, endTime=None):
    """
    Returns the projected utilization metrics of Amazon EC2 instance recommendations.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_ec2_recommendation_projected_metrics(
        instanceArn='string',
        stat='Maximum'|'Average',
        period=123,
        startTime=datetime(2015, 1, 1),
        endTime=datetime(2015, 1, 1)
    )
    
    
    :type instanceArn: string
    :param instanceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the instances for which to return recommendation projected metrics.\n

    :type stat: string
    :param stat: [REQUIRED]\nThe statistic of the projected metrics.\n

    :type period: integer
    :param period: [REQUIRED]\nThe granularity, in seconds, of the projected metrics data points.\n

    :type startTime: datetime
    :param startTime: [REQUIRED]\nThe time stamp of the first projected metrics data point to return.\n

    :type endTime: datetime
    :param endTime: [REQUIRED]\nThe time stamp of the last projected metrics data point to return.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'recommendedOptionProjectedMetrics': [
        {
            'recommendedInstanceType': 'string',
            'rank': 123,
            'projectedMetrics': [
                {
                    'name': 'Cpu'|'Memory',
                    'timestamps': [
                        datetime(2015, 1, 1),
                    ],
                    'values': [
                        123.0,
                    ]
                },
            ]
        },
    ]
}


Response Structure

(dict) --

recommendedOptionProjectedMetrics (list) --
An array of objects that describe a projected metrics.

(dict) --
Describes a projected utilization metric of a recommendation option.

recommendedInstanceType (string) --
The recommended instance type.

rank (integer) --
The rank of the recommendation option projected metric.
The top recommendation option is ranked as 1 .
The projected metric rank correlates to the recommendation option rank. For example, the projected metric ranked as 1 is related to the recommendation option that is also ranked as 1 in the same response.

projectedMetrics (list) --
An array of objects that describe a projected utilization metric.

(dict) --
Describes a projected utilization metric of a recommendation option, such as an Amazon EC2 instance.

name (string) --
The name of the projected utilization metric.

Note
Memory metrics are only returned for resources that have the unified CloudWatch agent installed on them. For more information, see Enabling Memory Utilization with the CloudWatch Agent .


timestamps (list) --
The time stamps of the projected utilization metric.

(datetime) --


values (list) --
The values of the projected utilization metrics.

(float) --
















Exceptions

ComputeOptimizer.Client.exceptions.OptInRequiredException
ComputeOptimizer.Client.exceptions.InternalServerException
ComputeOptimizer.Client.exceptions.ServiceUnavailableException
ComputeOptimizer.Client.exceptions.AccessDeniedException
ComputeOptimizer.Client.exceptions.InvalidParameterValueException
ComputeOptimizer.Client.exceptions.ResourceNotFoundException
ComputeOptimizer.Client.exceptions.MissingAuthenticationToken
ComputeOptimizer.Client.exceptions.ThrottlingException


    :return: {
        'recommendedOptionProjectedMetrics': [
            {
                'recommendedInstanceType': 'string',
                'rank': 123,
                'projectedMetrics': [
                    {
                        'name': 'Cpu'|'Memory',
                        'timestamps': [
                            datetime(2015, 1, 1),
                        ],
                        'values': [
                            123.0,
                        ]
                    },
                ]
            },
        ]
    }
    
    
    :returns: 
    (datetime) --
    
    """
    pass

def get_enrollment_status():
    """
    Returns the enrollment (opt in) status of an account to the AWS Compute Optimizer service.
    If the account is a master account of an organization, this operation also confirms the enrollment status of member accounts within the organization.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_enrollment_status()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'status': 'Active'|'Inactive'|'Pending'|'Failed',
    'statusReason': 'string',
    'memberAccountsEnrolled': True|False
}


Response Structure

(dict) --
status (string) --The enrollment status of the account.

statusReason (string) --The reason for the enrollment status of the account.
For example, an account might show a status of Pending because member accounts of an organization require more time to be enrolled in the service.

memberAccountsEnrolled (boolean) --Confirms the enrollment status of member accounts within the organization, if the account is a master account of an organization.






Exceptions

ComputeOptimizer.Client.exceptions.InternalServerException
ComputeOptimizer.Client.exceptions.ServiceUnavailableException
ComputeOptimizer.Client.exceptions.AccessDeniedException
ComputeOptimizer.Client.exceptions.InvalidParameterValueException
ComputeOptimizer.Client.exceptions.MissingAuthenticationToken
ComputeOptimizer.Client.exceptions.ThrottlingException


    :return: {
        'status': 'Active'|'Inactive'|'Pending'|'Failed',
        'statusReason': 'string',
        'memberAccountsEnrolled': True|False
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

def get_recommendation_summaries(accountIds=None, nextToken=None, maxResults=None):
    """
    Returns the optimization findings for an account.
    For example, it returns the number of Amazon EC2 instances in an account that are under-provisioned, over-provisioned, or optimized. It also returns the number of Auto Scaling groups in an account that are not optimized, or optimized.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_recommendation_summaries(
        accountIds=[
            'string',
        ],
        nextToken='string',
        maxResults=123
    )
    
    
    :type accountIds: list
    :param accountIds: The AWS account IDs for which to return recommendation summaries.\nOnly one account ID can be specified per request.\n\n(string) --\n\n

    :type nextToken: string
    :param nextToken: The token to advance to the next page of recommendation summaries.

    :type maxResults: integer
    :param maxResults: The maximum number of recommendation summaries to return with a single call.\nTo retrieve the remaining results, make another call with the returned NextToken value.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'nextToken': 'string',
    'recommendationSummaries': [
        {
            'summaries': [
                {
                    'name': 'Underprovisioned'|'Overprovisioned'|'Optimized'|'NotOptimized',
                    'value': 123.0
                },
            ],
            'recommendationResourceType': 'Ec2Instance'|'AutoScalingGroup',
            'accountId': 'string'
        },
    ]
}


Response Structure

(dict) --

nextToken (string) --
The token to use to advance to the next page of recommendation summaries.
This value is null when there are no more pages of recommendation summaries to return.

recommendationSummaries (list) --
An array of objects that summarize a recommendation.

(dict) --
A summary of a recommendation.

summaries (list) --
An array of objects that describe a recommendation summary.

(dict) --
The summary of a recommendation.

name (string) --
The finding classification of the recommendation.

value (float) --
The value of the recommendation summary.





recommendationResourceType (string) --
The resource type of the recommendation.

accountId (string) --
The AWS account ID of the recommendation summary.











Exceptions

ComputeOptimizer.Client.exceptions.OptInRequiredException
ComputeOptimizer.Client.exceptions.InternalServerException
ComputeOptimizer.Client.exceptions.ServiceUnavailableException
ComputeOptimizer.Client.exceptions.AccessDeniedException
ComputeOptimizer.Client.exceptions.InvalidParameterValueException
ComputeOptimizer.Client.exceptions.MissingAuthenticationToken
ComputeOptimizer.Client.exceptions.ThrottlingException


    :return: {
        'nextToken': 'string',
        'recommendationSummaries': [
            {
                'summaries': [
                    {
                        'name': 'Underprovisioned'|'Overprovisioned'|'Optimized'|'NotOptimized',
                        'value': 123.0
                    },
                ],
                'recommendationResourceType': 'Ec2Instance'|'AutoScalingGroup',
                'accountId': 'string'
            },
        ]
    }
    
    
    :returns: 
    ComputeOptimizer.Client.exceptions.OptInRequiredException
    ComputeOptimizer.Client.exceptions.InternalServerException
    ComputeOptimizer.Client.exceptions.ServiceUnavailableException
    ComputeOptimizer.Client.exceptions.AccessDeniedException
    ComputeOptimizer.Client.exceptions.InvalidParameterValueException
    ComputeOptimizer.Client.exceptions.MissingAuthenticationToken
    ComputeOptimizer.Client.exceptions.ThrottlingException
    
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

def update_enrollment_status(status=None, includeMemberAccounts=None):
    """
    Updates the enrollment (opt in) status of an account to the AWS Compute Optimizer service.
    If the account is a master account of an organization, this operation can also enroll member accounts within the organization.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_enrollment_status(
        status='Active'|'Inactive'|'Pending'|'Failed',
        includeMemberAccounts=True|False
    )
    
    
    :type status: string
    :param status: [REQUIRED]\nThe new enrollment status of the account.\nAccepted options are Active or Inactive . You will get an error if Pending or Failed are specified.\n

    :type includeMemberAccounts: boolean
    :param includeMemberAccounts: Indicates whether to enroll member accounts within the organization, if the account is a master account of an organization.

    :rtype: dict

ReturnsResponse Syntax
{
    'status': 'Active'|'Inactive'|'Pending'|'Failed',
    'statusReason': 'string'
}


Response Structure

(dict) --

status (string) --
The enrollment status of the account.

statusReason (string) --
The reason for the enrollment status of the account. For example, an account might show a status of Pending because member accounts of an organization require more time to be enrolled in the service.







Exceptions

ComputeOptimizer.Client.exceptions.InternalServerException
ComputeOptimizer.Client.exceptions.ServiceUnavailableException
ComputeOptimizer.Client.exceptions.AccessDeniedException
ComputeOptimizer.Client.exceptions.InvalidParameterValueException
ComputeOptimizer.Client.exceptions.MissingAuthenticationToken
ComputeOptimizer.Client.exceptions.ThrottlingException


    :return: {
        'status': 'Active'|'Inactive'|'Pending'|'Failed',
        'statusReason': 'string'
    }
    
    
    :returns: 
    ComputeOptimizer.Client.exceptions.InternalServerException
    ComputeOptimizer.Client.exceptions.ServiceUnavailableException
    ComputeOptimizer.Client.exceptions.AccessDeniedException
    ComputeOptimizer.Client.exceptions.InvalidParameterValueException
    ComputeOptimizer.Client.exceptions.MissingAuthenticationToken
    ComputeOptimizer.Client.exceptions.ThrottlingException
    
    """
    pass

