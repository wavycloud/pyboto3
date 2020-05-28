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

def create_cost_category_definition(Name=None, RuleVersion=None, Rules=None):
    """
    Creates a new Cost Category with the requested name and rules.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_cost_category_definition(
        Name='string',
        RuleVersion='CostCategoryExpression.v1',
        Rules=[
            {
                'Value': 'string',
                'Rule': {
                    'Or': [
                        {'... recursive ...'},
                    ],
                    'And': [
                        {'... recursive ...'},
                    ],
                    'Not': {'... recursive ...'},
                    'Dimensions': {
                        'Key': 'AZ'|'INSTANCE_TYPE'|'LINKED_ACCOUNT'|'LINKED_ACCOUNT_NAME'|'OPERATION'|'PURCHASE_TYPE'|'REGION'|'SERVICE'|'SERVICE_CODE'|'USAGE_TYPE'|'USAGE_TYPE_GROUP'|'RECORD_TYPE'|'OPERATING_SYSTEM'|'TENANCY'|'SCOPE'|'PLATFORM'|'SUBSCRIPTION_ID'|'LEGAL_ENTITY_NAME'|'DEPLOYMENT_OPTION'|'DATABASE_ENGINE'|'CACHE_ENGINE'|'INSTANCE_TYPE_FAMILY'|'BILLING_ENTITY'|'RESERVATION_ID'|'RESOURCE_ID'|'RIGHTSIZING_TYPE'|'SAVINGS_PLANS_TYPE'|'SAVINGS_PLAN_ARN'|'PAYMENT_OPTION',
                        'Values': [
                            'string',
                        ],
                        'MatchOptions': [
                            'EQUALS'|'STARTS_WITH'|'ENDS_WITH'|'CONTAINS'|'CASE_SENSITIVE'|'CASE_INSENSITIVE',
                        ]
                    },
                    'Tags': {
                        'Key': 'string',
                        'Values': [
                            'string',
                        ],
                        'MatchOptions': [
                            'EQUALS'|'STARTS_WITH'|'ENDS_WITH'|'CONTAINS'|'CASE_SENSITIVE'|'CASE_INSENSITIVE',
                        ]
                    },
                    'CostCategories': {
                        'Key': 'string',
                        'Values': [
                            'string',
                        ]
                    }
                }
            },
        ]
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe unique name of the Cost Category.\n

    :type RuleVersion: string
    :param RuleVersion: [REQUIRED]\nThe rule schema version in this particular Cost Category.\n

    :type Rules: list
    :param Rules: [REQUIRED]\nThe Cost Category rules used to categorize costs. For more information, see CostCategoryRule .\n\n(dict) --Rules are processed in order. If there are multiple rules that match the line item, then the first rule to match is used to determine that Cost Category value.\n\nValue (string) -- [REQUIRED]The value a line item will be categorized as, if it matches the rule.\n\nRule (dict) -- [REQUIRED]An Expression object used to categorize costs. This supports dimensions, Tags, and nested expressions. Currently the only dimensions supported are LINKED_ACCOUNT , SERVICE_CODE , RECORD_TYPE , and LINKED_ACCOUNT_NAME .\nRoot level OR is not supported. We recommend that you create a separate rule instead.\n\nRECORD_TYPE is a dimension used for Cost Explorer APIs, and is also supported for Cost Category expressions. This dimension uses different terms, depending on whether you\'re using the console or API/JSON editor. For a detailed comparison, see Term Comparisons in the AWS Billing and Cost Management User Guide .\n\nOr (list) --Return results that match either Dimension object.\n\n(dict) --Use Expression to filter by cost or by usage. There are two patterns:\n\nSimple dimension values - You can set the dimension name and values for the filters that you plan to use. For example, you can filter for REGION==us-east-1 OR REGION==us-west-1 . The Expression for that looks like this: { 'Dimensions': { 'Key': 'REGION', 'Values': [ 'us-east-1', \xe2\x80\x9cus-west-1\xe2\x80\x9d ] } }  The list of dimension values are OR\'d together to retrieve cost or usage data. You can create Expression and DimensionValues objects using either with* methods or set* methods in multiple lines.\nCompound dimension values with logical operations - You can use multiple Expression types and the logical operators AND/OR/NOT to create a list of one or more Expression objects. This allows you to filter on more advanced options. For example, you can filter on ((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE != DataTransfer) . The Expression for that looks like this: { 'And': [ {'Or': [ {'Dimensions': { 'Key': 'REGION', 'Values': [ 'us-east-1', 'us-west-1' ] }}, {'Tags': { 'Key': 'TagName', 'Values': ['Value1'] } } ]}, {'Not': {'Dimensions': { 'Key': 'USAGE_TYPE', 'Values': ['DataTransfer'] }}} ] }\n\n\nNote\n\nBecause each Expression can have only one operator, the service returns an error if more than one is specified. The following example shows an Expression object that creates an error.\n{ 'And': [ ... ], 'DimensionValues': { 'Dimension': 'USAGE_TYPE', 'Values': [ 'DataTransfer' ] } }\n\n\nNote\nFor GetRightsizingRecommendation action, a combination of OR and NOT is not supported. OR is not supported between different dimensions, or dimensions and tags. NOT operators aren\'t supported. Dimensions are also limited to LINKED_ACCOUNT , REGION , or RIGHTSIZING_TYPE .\n\n\n\n\nAnd (list) --Return results that match both Dimension objects.\n\n(dict) --Use Expression to filter by cost or by usage. There are two patterns:\n\nSimple dimension values - You can set the dimension name and values for the filters that you plan to use. For example, you can filter for REGION==us-east-1 OR REGION==us-west-1 . The Expression for that looks like this: { 'Dimensions': { 'Key': 'REGION', 'Values': [ 'us-east-1', \xe2\x80\x9cus-west-1\xe2\x80\x9d ] } }  The list of dimension values are OR\'d together to retrieve cost or usage data. You can create Expression and DimensionValues objects using either with* methods or set* methods in multiple lines.\nCompound dimension values with logical operations - You can use multiple Expression types and the logical operators AND/OR/NOT to create a list of one or more Expression objects. This allows you to filter on more advanced options. For example, you can filter on ((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE != DataTransfer) . The Expression for that looks like this: { 'And': [ {'Or': [ {'Dimensions': { 'Key': 'REGION', 'Values': [ 'us-east-1', 'us-west-1' ] }}, {'Tags': { 'Key': 'TagName', 'Values': ['Value1'] } } ]}, {'Not': {'Dimensions': { 'Key': 'USAGE_TYPE', 'Values': ['DataTransfer'] }}} ] }\n\n\nNote\n\nBecause each Expression can have only one operator, the service returns an error if more than one is specified. The following example shows an Expression object that creates an error.\n{ 'And': [ ... ], 'DimensionValues': { 'Dimension': 'USAGE_TYPE', 'Values': [ 'DataTransfer' ] } }\n\n\nNote\nFor GetRightsizingRecommendation action, a combination of OR and NOT is not supported. OR is not supported between different dimensions, or dimensions and tags. NOT operators aren\'t supported. Dimensions are also limited to LINKED_ACCOUNT , REGION , or RIGHTSIZING_TYPE .\n\n\n\n\nNot (dict) --Return results that don\'t match a Dimension object.\n\nDimensions (dict) --The specific Dimension to use for Expression .\n\nKey (string) --The names of the metadata types that you can use to filter and group your results. For example, AZ returns a list of Availability Zones.\n\nValues (list) --The metadata values that you can use to filter and group your results. You can use GetDimensionValues to find specific values.\n\n(string) --\n\n\nMatchOptions (list) --The match options that you can use to filter your results. MatchOptions is only applicable for actions related to Cost Category. The default values for MatchOptions is EQUALS and CASE_SENSITIVE .\n\n(string) --\n\n\n\n\nTags (dict) --The specific Tag to use for Expression .\n\nKey (string) --The key for the tag.\n\nValues (list) --The specific value of the tag.\n\n(string) --\n\n\nMatchOptions (list) --The match options that you can use to filter your results. MatchOptions is only applicable for only applicable for actions related to Cost Category. The default values for MatchOptions is EQUALS and CASE_SENSITIVE .\n\n(string) --\n\n\n\n\nCostCategories (dict) --The filter based on CostCategory values.\n\nKey (string) --The unique name of the Cost Category.\n\nValues (list) --The specific value of the Cost Category.\n\n(string) --\n\n\n\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'CostCategoryArn': 'string',
    'EffectiveStart': 'string'
}


Response Structure

(dict) --

CostCategoryArn (string) --
The unique identifier for your newly created Cost Category.

EffectiveStart (string) --
The Cost Category\'s effective start date.







Exceptions

CostExplorer.Client.exceptions.ServiceQuotaExceededException
CostExplorer.Client.exceptions.LimitExceededException


    :return: {
        'CostCategoryArn': 'string',
        'EffectiveStart': 'string'
    }
    
    
    :returns: 
    CostExplorer.Client.exceptions.ServiceQuotaExceededException
    CostExplorer.Client.exceptions.LimitExceededException
    
    """
    pass

def delete_cost_category_definition(CostCategoryArn=None):
    """
    Deletes a Cost Category. Expenses from this month going forward will no longer be categorized with this Cost Category.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_cost_category_definition(
        CostCategoryArn='string'
    )
    
    
    :type CostCategoryArn: string
    :param CostCategoryArn: [REQUIRED]\nThe unique identifier for your Cost Category.\n

    :rtype: dict
ReturnsResponse Syntax{
    'CostCategoryArn': 'string',
    'EffectiveEnd': 'string'
}


Response Structure

(dict) --
CostCategoryArn (string) --The unique identifier for your Cost Category.

EffectiveEnd (string) --The effective end date of the Cost Category as a result of deleting it. No costs after this date will be categorized by the deleted Cost Category.






Exceptions

CostExplorer.Client.exceptions.ResourceNotFoundException
CostExplorer.Client.exceptions.LimitExceededException


    :return: {
        'CostCategoryArn': 'string',
        'EffectiveEnd': 'string'
    }
    
    
    """
    pass

def describe_cost_category_definition(CostCategoryArn=None, EffectiveOn=None):
    """
    Returns the name, ARN, rules, definition, and effective dates of a Cost Category that\'s defined in the account.
    You have the option to use EffectiveOn to return a Cost Category that is active on a specific date. If there is no EffectiveOn specified, you\xe2\x80\x99ll see a Cost Category that is effective on the current date. If Cost Category is still effective, EffectiveEnd is omitted in the response.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_cost_category_definition(
        CostCategoryArn='string',
        EffectiveOn='string'
    )
    
    
    :type CostCategoryArn: string
    :param CostCategoryArn: [REQUIRED]\nThe unique identifier for your Cost Category.\n

    :type EffectiveOn: string
    :param EffectiveOn: The date when the Cost Category was effective.

    :rtype: dict

ReturnsResponse Syntax
{
    'CostCategory': {
        'CostCategoryArn': 'string',
        'EffectiveStart': 'string',
        'EffectiveEnd': 'string',
        'Name': 'string',
        'RuleVersion': 'CostCategoryExpression.v1',
        'Rules': [
            {
                'Value': 'string',
                'Rule': {
                    'Or': [
                        {'... recursive ...'},
                    ],
                    'And': [
                        {'... recursive ...'},
                    ],
                    'Not': {'... recursive ...'},
                    'Dimensions': {
                        'Key': 'AZ'|'INSTANCE_TYPE'|'LINKED_ACCOUNT'|'LINKED_ACCOUNT_NAME'|'OPERATION'|'PURCHASE_TYPE'|'REGION'|'SERVICE'|'SERVICE_CODE'|'USAGE_TYPE'|'USAGE_TYPE_GROUP'|'RECORD_TYPE'|'OPERATING_SYSTEM'|'TENANCY'|'SCOPE'|'PLATFORM'|'SUBSCRIPTION_ID'|'LEGAL_ENTITY_NAME'|'DEPLOYMENT_OPTION'|'DATABASE_ENGINE'|'CACHE_ENGINE'|'INSTANCE_TYPE_FAMILY'|'BILLING_ENTITY'|'RESERVATION_ID'|'RESOURCE_ID'|'RIGHTSIZING_TYPE'|'SAVINGS_PLANS_TYPE'|'SAVINGS_PLAN_ARN'|'PAYMENT_OPTION',
                        'Values': [
                            'string',
                        ],
                        'MatchOptions': [
                            'EQUALS'|'STARTS_WITH'|'ENDS_WITH'|'CONTAINS'|'CASE_SENSITIVE'|'CASE_INSENSITIVE',
                        ]
                    },
                    'Tags': {
                        'Key': 'string',
                        'Values': [
                            'string',
                        ],
                        'MatchOptions': [
                            'EQUALS'|'STARTS_WITH'|'ENDS_WITH'|'CONTAINS'|'CASE_SENSITIVE'|'CASE_INSENSITIVE',
                        ]
                    },
                    'CostCategories': {
                        'Key': 'string',
                        'Values': [
                            'string',
                        ]
                    }
                }
            },
        ]
    }
}


Response Structure

(dict) --

CostCategory (dict) --
The structure of Cost Categories. This includes detailed metadata and the set of rules for the CostCategory object.

CostCategoryArn (string) --
The unique identifier for your Cost Category.

EffectiveStart (string) --
The Cost Category\'s effective start date.

EffectiveEnd (string) --
The Cost Category\'s effective end date.

Name (string) --
The unique name of the Cost Category.

RuleVersion (string) --
The rule schema version in this particular Cost Category.

Rules (list) --
Rules are processed in order. If there are multiple rules that match the line item, then the first rule to match is used to determine that Cost Category value.

(dict) --
Rules are processed in order. If there are multiple rules that match the line item, then the first rule to match is used to determine that Cost Category value.

Value (string) --
The value a line item will be categorized as, if it matches the rule.

Rule (dict) --
An Expression object used to categorize costs. This supports dimensions, Tags, and nested expressions. Currently the only dimensions supported are LINKED_ACCOUNT , SERVICE_CODE , RECORD_TYPE , and LINKED_ACCOUNT_NAME .
Root level OR is not supported. We recommend that you create a separate rule instead.

RECORD_TYPE is a dimension used for Cost Explorer APIs, and is also supported for Cost Category expressions. This dimension uses different terms, depending on whether you\'re using the console or API/JSON editor. For a detailed comparison, see Term Comparisons in the AWS Billing and Cost Management User Guide .


Or (list) --
Return results that match either Dimension object.

(dict) --
Use Expression to filter by cost or by usage. There are two patterns:

Simple dimension values - You can set the dimension name and values for the filters that you plan to use. For example, you can filter for REGION==us-east-1 OR REGION==us-west-1 . The Expression for that looks like this:  { "Dimensions": { "Key": "REGION", "Values": [ "us-east-1", \xe2\x80\x9cus-west-1\xe2\x80\x9d ] } }   The list of dimension values are OR\'d together to retrieve cost or usage data. You can create Expression and DimensionValues objects using either with* methods or set* methods in multiple lines.
Compound dimension values with logical operations - You can use multiple Expression types and the logical operators AND/OR/NOT to create a list of one or more Expression objects. This allows you to filter on more advanced options. For example, you can filter on ((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE != DataTransfer) . The Expression for that looks like this:  { "And": [ {"Or": [ {"Dimensions": { "Key": "REGION", "Values": [ "us-east-1", "us-west-1" ] }}, {"Tags": { "Key": "TagName", "Values": ["Value1"] } } ]}, {"Not": {"Dimensions": { "Key": "USAGE_TYPE", "Values": ["DataTransfer"] }}} ] }


Note

Because each Expression can have only one operator, the service returns an error if more than one is specified. The following example shows an Expression object that creates an error.

{ "And": [ ... ], "DimensionValues": { "Dimension": "USAGE_TYPE", "Values": [ "DataTransfer" ] } }


Note
For GetRightsizingRecommendation action, a combination of OR and NOT is not supported. OR is not supported between different dimensions, or dimensions and tags. NOT operators aren\'t supported. Dimensions are also limited to LINKED_ACCOUNT , REGION , or RIGHTSIZING_TYPE .




And (list) --
Return results that match both Dimension objects.

(dict) --
Use Expression to filter by cost or by usage. There are two patterns:

Simple dimension values - You can set the dimension name and values for the filters that you plan to use. For example, you can filter for REGION==us-east-1 OR REGION==us-west-1 . The Expression for that looks like this:  { "Dimensions": { "Key": "REGION", "Values": [ "us-east-1", \xe2\x80\x9cus-west-1\xe2\x80\x9d ] } }   The list of dimension values are OR\'d together to retrieve cost or usage data. You can create Expression and DimensionValues objects using either with* methods or set* methods in multiple lines.
Compound dimension values with logical operations - You can use multiple Expression types and the logical operators AND/OR/NOT to create a list of one or more Expression objects. This allows you to filter on more advanced options. For example, you can filter on ((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE != DataTransfer) . The Expression for that looks like this:  { "And": [ {"Or": [ {"Dimensions": { "Key": "REGION", "Values": [ "us-east-1", "us-west-1" ] }}, {"Tags": { "Key": "TagName", "Values": ["Value1"] } } ]}, {"Not": {"Dimensions": { "Key": "USAGE_TYPE", "Values": ["DataTransfer"] }}} ] }


Note

Because each Expression can have only one operator, the service returns an error if more than one is specified. The following example shows an Expression object that creates an error.

{ "And": [ ... ], "DimensionValues": { "Dimension": "USAGE_TYPE", "Values": [ "DataTransfer" ] } }


Note
For GetRightsizingRecommendation action, a combination of OR and NOT is not supported. OR is not supported between different dimensions, or dimensions and tags. NOT operators aren\'t supported. Dimensions are also limited to LINKED_ACCOUNT , REGION , or RIGHTSIZING_TYPE .




Not (dict) --
Return results that don\'t match a Dimension object.

Dimensions (dict) --
The specific Dimension to use for Expression .

Key (string) --
The names of the metadata types that you can use to filter and group your results. For example, AZ returns a list of Availability Zones.

Values (list) --
The metadata values that you can use to filter and group your results. You can use GetDimensionValues to find specific values.

(string) --


MatchOptions (list) --
The match options that you can use to filter your results. MatchOptions is only applicable for actions related to Cost Category. The default values for MatchOptions is EQUALS and CASE_SENSITIVE .

(string) --




Tags (dict) --
The specific Tag to use for Expression .

Key (string) --
The key for the tag.

Values (list) --
The specific value of the tag.

(string) --


MatchOptions (list) --
The match options that you can use to filter your results. MatchOptions is only applicable for only applicable for actions related to Cost Category. The default values for MatchOptions is EQUALS and CASE_SENSITIVE .

(string) --




CostCategories (dict) --
The filter based on CostCategory values.

Key (string) --
The unique name of the Cost Category.

Values (list) --
The specific value of the Cost Category.

(string) --


















Exceptions

CostExplorer.Client.exceptions.ResourceNotFoundException
CostExplorer.Client.exceptions.LimitExceededException


    :return: {
        'CostCategory': {
            'CostCategoryArn': 'string',
            'EffectiveStart': 'string',
            'EffectiveEnd': 'string',
            'Name': 'string',
            'RuleVersion': 'CostCategoryExpression.v1',
            'Rules': [
                {
                    'Value': 'string',
                    'Rule': {
                        'Or': [
                            {'... recursive ...'},
                        ],
                        'And': [
                            {'... recursive ...'},
                        ],
                        'Not': {'... recursive ...'},
                        'Dimensions': {
                            'Key': 'AZ'|'INSTANCE_TYPE'|'LINKED_ACCOUNT'|'LINKED_ACCOUNT_NAME'|'OPERATION'|'PURCHASE_TYPE'|'REGION'|'SERVICE'|'SERVICE_CODE'|'USAGE_TYPE'|'USAGE_TYPE_GROUP'|'RECORD_TYPE'|'OPERATING_SYSTEM'|'TENANCY'|'SCOPE'|'PLATFORM'|'SUBSCRIPTION_ID'|'LEGAL_ENTITY_NAME'|'DEPLOYMENT_OPTION'|'DATABASE_ENGINE'|'CACHE_ENGINE'|'INSTANCE_TYPE_FAMILY'|'BILLING_ENTITY'|'RESERVATION_ID'|'RESOURCE_ID'|'RIGHTSIZING_TYPE'|'SAVINGS_PLANS_TYPE'|'SAVINGS_PLAN_ARN'|'PAYMENT_OPTION',
                            'Values': [
                                'string',
                            ],
                            'MatchOptions': [
                                'EQUALS'|'STARTS_WITH'|'ENDS_WITH'|'CONTAINS'|'CASE_SENSITIVE'|'CASE_INSENSITIVE',
                            ]
                        },
                        'Tags': {
                            'Key': 'string',
                            'Values': [
                                'string',
                            ],
                            'MatchOptions': [
                                'EQUALS'|'STARTS_WITH'|'ENDS_WITH'|'CONTAINS'|'CASE_SENSITIVE'|'CASE_INSENSITIVE',
                            ]
                        },
                        'CostCategories': {
                            'Key': 'string',
                            'Values': [
                                'string',
                            ]
                        }
                    }
                },
            ]
        }
    }
    
    
    :returns: 
    Simple dimension values - You can set the dimension name and values for the filters that you plan to use. For example, you can filter for REGION==us-east-1 OR REGION==us-west-1 . The Expression for that looks like this:  { "Dimensions": { "Key": "REGION", "Values": [ "us-east-1", \xe2\x80\x9cus-west-1\xe2\x80\x9d ] } }   The list of dimension values are OR\'d together to retrieve cost or usage data. You can create Expression and DimensionValues objects using either with* methods or set* methods in multiple lines.
    Compound dimension values with logical operations - You can use multiple Expression types and the logical operators AND/OR/NOT to create a list of one or more Expression objects. This allows you to filter on more advanced options. For example, you can filter on ((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE != DataTransfer) . The Expression for that looks like this:  { "And": [ {"Or": [ {"Dimensions": { "Key": "REGION", "Values": [ "us-east-1", "us-west-1" ] }}, {"Tags": { "Key": "TagName", "Values": ["Value1"] } } ]}, {"Not": {"Dimensions": { "Key": "USAGE_TYPE", "Values": ["DataTransfer"] }}} ] }
    
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

def get_cost_and_usage(TimePeriod=None, Granularity=None, Filter=None, Metrics=None, GroupBy=None, NextPageToken=None):
    """
    Retrieves cost and usage metrics for your account. You can specify which cost and usage-related metric, such as BlendedCosts or Quantity , that you want the request to return. You can also filter and group your data by various dimensions, such as SERVICE or AZ , in a specific time range. For a complete list of valid dimensions, see the GetDimensionValues operation. Master accounts in an organization in AWS Organizations have access to all member accounts.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_cost_and_usage(
        TimePeriod={
            'Start': 'string',
            'End': 'string'
        },
        Granularity='DAILY'|'MONTHLY'|'HOURLY',
        Filter={
            'Or': [
                {'... recursive ...'},
            ],
            'And': [
                {'... recursive ...'},
            ],
            'Not': {'... recursive ...'},
            'Dimensions': {
                'Key': 'AZ'|'INSTANCE_TYPE'|'LINKED_ACCOUNT'|'LINKED_ACCOUNT_NAME'|'OPERATION'|'PURCHASE_TYPE'|'REGION'|'SERVICE'|'SERVICE_CODE'|'USAGE_TYPE'|'USAGE_TYPE_GROUP'|'RECORD_TYPE'|'OPERATING_SYSTEM'|'TENANCY'|'SCOPE'|'PLATFORM'|'SUBSCRIPTION_ID'|'LEGAL_ENTITY_NAME'|'DEPLOYMENT_OPTION'|'DATABASE_ENGINE'|'CACHE_ENGINE'|'INSTANCE_TYPE_FAMILY'|'BILLING_ENTITY'|'RESERVATION_ID'|'RESOURCE_ID'|'RIGHTSIZING_TYPE'|'SAVINGS_PLANS_TYPE'|'SAVINGS_PLAN_ARN'|'PAYMENT_OPTION',
                'Values': [
                    'string',
                ],
                'MatchOptions': [
                    'EQUALS'|'STARTS_WITH'|'ENDS_WITH'|'CONTAINS'|'CASE_SENSITIVE'|'CASE_INSENSITIVE',
                ]
            },
            'Tags': {
                'Key': 'string',
                'Values': [
                    'string',
                ],
                'MatchOptions': [
                    'EQUALS'|'STARTS_WITH'|'ENDS_WITH'|'CONTAINS'|'CASE_SENSITIVE'|'CASE_INSENSITIVE',
                ]
            },
            'CostCategories': {
                'Key': 'string',
                'Values': [
                    'string',
                ]
            }
        },
        Metrics=[
            'string',
        ],
        GroupBy=[
            {
                'Type': 'DIMENSION'|'TAG'|'COST_CATEGORY',
                'Key': 'string'
            },
        ],
        NextPageToken='string'
    )
    
    
    :type TimePeriod: dict
    :param TimePeriod: [REQUIRED]\nSets the start and end dates for retrieving AWS costs. The start date is inclusive, but the end date is exclusive. For example, if start is 2017-01-01 and end is 2017-05-01 , then the cost and usage data is retrieved from 2017-01-01 up to and including 2017-04-30 but not including 2017-05-01 .\n\nStart (string) -- [REQUIRED]The beginning of the time period that you want the usage and costs for. The start date is inclusive. For example, if start is 2017-01-01 , AWS retrieves cost and usage data starting at 2017-01-01 up to the end date.\n\nEnd (string) -- [REQUIRED]The end of the time period that you want the usage and costs for. The end date is exclusive. For example, if end is 2017-05-01 , AWS retrieves cost and usage data from the start date up to, but not including, 2017-05-01 .\n\n\n

    :type Granularity: string
    :param Granularity: Sets the AWS cost granularity to MONTHLY or DAILY , or HOURLY . If Granularity isn\'t set, the response object doesn\'t include the Granularity , either MONTHLY or DAILY , or HOURLY .

    :type Filter: dict
    :param Filter: Filters AWS costs by different dimensions. For example, you can specify SERVICE and LINKED_ACCOUNT and get the costs that are associated with that account\'s usage of that service. You can nest Expression objects to define any combination of dimension filters. For more information, see Expression .\n\nOr (list) --Return results that match either Dimension object.\n\n(dict) --Use Expression to filter by cost or by usage. There are two patterns:\n\nSimple dimension values - You can set the dimension name and values for the filters that you plan to use. For example, you can filter for REGION==us-east-1 OR REGION==us-west-1 . The Expression for that looks like this: { 'Dimensions': { 'Key': 'REGION', 'Values': [ 'us-east-1', \xe2\x80\x9cus-west-1\xe2\x80\x9d ] } }  The list of dimension values are OR\'d together to retrieve cost or usage data. You can create Expression and DimensionValues objects using either with* methods or set* methods in multiple lines.\nCompound dimension values with logical operations - You can use multiple Expression types and the logical operators AND/OR/NOT to create a list of one or more Expression objects. This allows you to filter on more advanced options. For example, you can filter on ((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE != DataTransfer) . The Expression for that looks like this: { 'And': [ {'Or': [ {'Dimensions': { 'Key': 'REGION', 'Values': [ 'us-east-1', 'us-west-1' ] }}, {'Tags': { 'Key': 'TagName', 'Values': ['Value1'] } } ]}, {'Not': {'Dimensions': { 'Key': 'USAGE_TYPE', 'Values': ['DataTransfer'] }}} ] }\n\n\nNote\n\nBecause each Expression can have only one operator, the service returns an error if more than one is specified. The following example shows an Expression object that creates an error.\n{ 'And': [ ... ], 'DimensionValues': { 'Dimension': 'USAGE_TYPE', 'Values': [ 'DataTransfer' ] } }\n\n\nNote\nFor GetRightsizingRecommendation action, a combination of OR and NOT is not supported. OR is not supported between different dimensions, or dimensions and tags. NOT operators aren\'t supported. Dimensions are also limited to LINKED_ACCOUNT , REGION , or RIGHTSIZING_TYPE .\n\n\n\n\nAnd (list) --Return results that match both Dimension objects.\n\n(dict) --Use Expression to filter by cost or by usage. There are two patterns:\n\nSimple dimension values - You can set the dimension name and values for the filters that you plan to use. For example, you can filter for REGION==us-east-1 OR REGION==us-west-1 . The Expression for that looks like this: { 'Dimensions': { 'Key': 'REGION', 'Values': [ 'us-east-1', \xe2\x80\x9cus-west-1\xe2\x80\x9d ] } }  The list of dimension values are OR\'d together to retrieve cost or usage data. You can create Expression and DimensionValues objects using either with* methods or set* methods in multiple lines.\nCompound dimension values with logical operations - You can use multiple Expression types and the logical operators AND/OR/NOT to create a list of one or more Expression objects. This allows you to filter on more advanced options. For example, you can filter on ((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE != DataTransfer) . The Expression for that looks like this: { 'And': [ {'Or': [ {'Dimensions': { 'Key': 'REGION', 'Values': [ 'us-east-1', 'us-west-1' ] }}, {'Tags': { 'Key': 'TagName', 'Values': ['Value1'] } } ]}, {'Not': {'Dimensions': { 'Key': 'USAGE_TYPE', 'Values': ['DataTransfer'] }}} ] }\n\n\nNote\n\nBecause each Expression can have only one operator, the service returns an error if more than one is specified. The following example shows an Expression object that creates an error.\n{ 'And': [ ... ], 'DimensionValues': { 'Dimension': 'USAGE_TYPE', 'Values': [ 'DataTransfer' ] } }\n\n\nNote\nFor GetRightsizingRecommendation action, a combination of OR and NOT is not supported. OR is not supported between different dimensions, or dimensions and tags. NOT operators aren\'t supported. Dimensions are also limited to LINKED_ACCOUNT , REGION , or RIGHTSIZING_TYPE .\n\n\n\n\nNot (dict) --Return results that don\'t match a Dimension object.\n\nDimensions (dict) --The specific Dimension to use for Expression .\n\nKey (string) --The names of the metadata types that you can use to filter and group your results. For example, AZ returns a list of Availability Zones.\n\nValues (list) --The metadata values that you can use to filter and group your results. You can use GetDimensionValues to find specific values.\n\n(string) --\n\n\nMatchOptions (list) --The match options that you can use to filter your results. MatchOptions is only applicable for actions related to Cost Category. The default values for MatchOptions is EQUALS and CASE_SENSITIVE .\n\n(string) --\n\n\n\n\nTags (dict) --The specific Tag to use for Expression .\n\nKey (string) --The key for the tag.\n\nValues (list) --The specific value of the tag.\n\n(string) --\n\n\nMatchOptions (list) --The match options that you can use to filter your results. MatchOptions is only applicable for only applicable for actions related to Cost Category. The default values for MatchOptions is EQUALS and CASE_SENSITIVE .\n\n(string) --\n\n\n\n\nCostCategories (dict) --The filter based on CostCategory values.\n\nKey (string) --The unique name of the Cost Category.\n\nValues (list) --The specific value of the Cost Category.\n\n(string) --\n\n\n\n\n\n

    :type Metrics: list
    :param Metrics: Which metrics are returned in the query. For more information about blended and unblended rates, see Why does the 'blended' annotation appear on some line items in my bill? .\nValid values are AmortizedCost , BlendedCost , NetAmortizedCost , NetUnblendedCost , NormalizedUsageAmount , UnblendedCost , and UsageQuantity .\n\nNote\n\nIf you return the UsageQuantity metric, the service aggregates all usage numbers without taking into account the units. For example, if you aggregate usageQuantity across all of Amazon EC2, the results aren\'t meaningful because Amazon EC2 compute hours and data transfer are measured in different units (for example, hours vs. GB). To get more meaningful UsageQuantity metrics, filter by UsageType or UsageTypeGroups .\nMetrics is required for GetCostAndUsage requests.\n\n\n(string) --\n\n

    :type GroupBy: list
    :param GroupBy: You can group AWS costs using up to two different groups, either dimensions, tag keys, or both.\nWhen you group by tag key, you get all tag values, including empty strings.\nValid values are AZ , INSTANCE_TYPE , LEGAL_ENTITY_NAME , LINKED_ACCOUNT , OPERATION , PLATFORM , PURCHASE_TYPE , SERVICE , TAGS , TENANCY , RECORD_TYPE , and USAGE_TYPE .\n\n(dict) --Represents a group when you specify a group by criteria or in the response to a query with a specific grouping.\n\nType (string) --The string that represents the type of group.\n\nKey (string) --The string that represents a key for a specified group.\n\n\n\n\n

    :type NextPageToken: string
    :param NextPageToken: The token to retrieve the next set of results. AWS provides the token when the response from a previous call has more results than the maximum page size.

    :rtype: dict

ReturnsResponse Syntax
{
    'NextPageToken': 'string',
    'GroupDefinitions': [
        {
            'Type': 'DIMENSION'|'TAG'|'COST_CATEGORY',
            'Key': 'string'
        },
    ],
    'ResultsByTime': [
        {
            'TimePeriod': {
                'Start': 'string',
                'End': 'string'
            },
            'Total': {
                'string': {
                    'Amount': 'string',
                    'Unit': 'string'
                }
            },
            'Groups': [
                {
                    'Keys': [
                        'string',
                    ],
                    'Metrics': {
                        'string': {
                            'Amount': 'string',
                            'Unit': 'string'
                        }
                    }
                },
            ],
            'Estimated': True|False
        },
    ]
}


Response Structure

(dict) --

NextPageToken (string) --
The token for the next set of retrievable results. AWS provides the token when the response from a previous call has more results than the maximum page size.

GroupDefinitions (list) --
The groups that are specified by the Filter or GroupBy parameters in the request.

(dict) --
Represents a group when you specify a group by criteria or in the response to a query with a specific grouping.

Type (string) --
The string that represents the type of group.

Key (string) --
The string that represents a key for a specified group.





ResultsByTime (list) --
The time period that is covered by the results in the response.

(dict) --
The result that is associated with a time period.

TimePeriod (dict) --
The time period that the result covers.

Start (string) --
The beginning of the time period that you want the usage and costs for. The start date is inclusive. For example, if start is 2017-01-01 , AWS retrieves cost and usage data starting at 2017-01-01 up to the end date.

End (string) --
The end of the time period that you want the usage and costs for. The end date is exclusive. For example, if end is 2017-05-01 , AWS retrieves cost and usage data from the start date up to, but not including, 2017-05-01 .



Total (dict) --
The total amount of cost or usage accrued during the time period.

(string) --

(dict) --
The aggregated value for a metric.

Amount (string) --
The actual number that represents the metric.

Unit (string) --
The unit that the metric is given in.







Groups (list) --
The groups that this time period includes.

(dict) --
One level of grouped data in the results.

Keys (list) --
The keys that are included in this group.

(string) --


Metrics (dict) --
The metrics that are included in this group.

(string) --

(dict) --
The aggregated value for a metric.

Amount (string) --
The actual number that represents the metric.

Unit (string) --
The unit that the metric is given in.











Estimated (boolean) --
Whether the result is estimated.











Exceptions

CostExplorer.Client.exceptions.LimitExceededException
CostExplorer.Client.exceptions.BillExpirationException
CostExplorer.Client.exceptions.DataUnavailableException
CostExplorer.Client.exceptions.InvalidNextTokenException
CostExplorer.Client.exceptions.RequestChangedException


    :return: {
        'NextPageToken': 'string',
        'GroupDefinitions': [
            {
                'Type': 'DIMENSION'|'TAG'|'COST_CATEGORY',
                'Key': 'string'
            },
        ],
        'ResultsByTime': [
            {
                'TimePeriod': {
                    'Start': 'string',
                    'End': 'string'
                },
                'Total': {
                    'string': {
                        'Amount': 'string',
                        'Unit': 'string'
                    }
                },
                'Groups': [
                    {
                        'Keys': [
                            'string',
                        ],
                        'Metrics': {
                            'string': {
                                'Amount': 'string',
                                'Unit': 'string'
                            }
                        }
                    },
                ],
                'Estimated': True|False
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_cost_and_usage_with_resources(TimePeriod=None, Granularity=None, Filter=None, Metrics=None, GroupBy=None, NextPageToken=None):
    """
    Retrieves cost and usage metrics with resources for your account. You can specify which cost and usage-related metric, such as BlendedCosts or Quantity , that you want the request to return. You can also filter and group your data by various dimensions, such as SERVICE or AZ , in a specific time range. For a complete list of valid dimensions, see the GetDimensionValues operation. Master accounts in an organization in AWS Organizations have access to all member accounts. This API is currently available for the Amazon Elastic Compute Cloud \xe2\x80\x93 Compute service only.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_cost_and_usage_with_resources(
        TimePeriod={
            'Start': 'string',
            'End': 'string'
        },
        Granularity='DAILY'|'MONTHLY'|'HOURLY',
        Filter={
            'Or': [
                {'... recursive ...'},
            ],
            'And': [
                {'... recursive ...'},
            ],
            'Not': {'... recursive ...'},
            'Dimensions': {
                'Key': 'AZ'|'INSTANCE_TYPE'|'LINKED_ACCOUNT'|'LINKED_ACCOUNT_NAME'|'OPERATION'|'PURCHASE_TYPE'|'REGION'|'SERVICE'|'SERVICE_CODE'|'USAGE_TYPE'|'USAGE_TYPE_GROUP'|'RECORD_TYPE'|'OPERATING_SYSTEM'|'TENANCY'|'SCOPE'|'PLATFORM'|'SUBSCRIPTION_ID'|'LEGAL_ENTITY_NAME'|'DEPLOYMENT_OPTION'|'DATABASE_ENGINE'|'CACHE_ENGINE'|'INSTANCE_TYPE_FAMILY'|'BILLING_ENTITY'|'RESERVATION_ID'|'RESOURCE_ID'|'RIGHTSIZING_TYPE'|'SAVINGS_PLANS_TYPE'|'SAVINGS_PLAN_ARN'|'PAYMENT_OPTION',
                'Values': [
                    'string',
                ],
                'MatchOptions': [
                    'EQUALS'|'STARTS_WITH'|'ENDS_WITH'|'CONTAINS'|'CASE_SENSITIVE'|'CASE_INSENSITIVE',
                ]
            },
            'Tags': {
                'Key': 'string',
                'Values': [
                    'string',
                ],
                'MatchOptions': [
                    'EQUALS'|'STARTS_WITH'|'ENDS_WITH'|'CONTAINS'|'CASE_SENSITIVE'|'CASE_INSENSITIVE',
                ]
            },
            'CostCategories': {
                'Key': 'string',
                'Values': [
                    'string',
                ]
            }
        },
        Metrics=[
            'string',
        ],
        GroupBy=[
            {
                'Type': 'DIMENSION'|'TAG'|'COST_CATEGORY',
                'Key': 'string'
            },
        ],
        NextPageToken='string'
    )
    
    
    :type TimePeriod: dict
    :param TimePeriod: [REQUIRED]\nSets the start and end dates for retrieving Amazon Web Services costs. The range must be within the last 14 days (the start date cannot be earlier than 14 days ago). The start date is inclusive, but the end date is exclusive. For example, if start is 2017-01-01 and end is 2017-05-01 , then the cost and usage data is retrieved from 2017-01-01 up to and including 2017-04-30 but not including 2017-05-01 .\n\nStart (string) -- [REQUIRED]The beginning of the time period that you want the usage and costs for. The start date is inclusive. For example, if start is 2017-01-01 , AWS retrieves cost and usage data starting at 2017-01-01 up to the end date.\n\nEnd (string) -- [REQUIRED]The end of the time period that you want the usage and costs for. The end date is exclusive. For example, if end is 2017-05-01 , AWS retrieves cost and usage data from the start date up to, but not including, 2017-05-01 .\n\n\n

    :type Granularity: string
    :param Granularity: Sets the AWS cost granularity to MONTHLY , DAILY , or HOURLY . If Granularity isn\'t set, the response object doesn\'t include the Granularity , MONTHLY , DAILY , or HOURLY .

    :type Filter: dict
    :param Filter: Filters Amazon Web Services costs by different dimensions. For example, you can specify SERVICE and LINKED_ACCOUNT and get the costs that are associated with that account\'s usage of that service. You can nest Expression objects to define any combination of dimension filters. For more information, see Expression .\nThe GetCostAndUsageWithResources operation requires that you either group by or filter by a ResourceId .\n\nOr (list) --Return results that match either Dimension object.\n\n(dict) --Use Expression to filter by cost or by usage. There are two patterns:\n\nSimple dimension values - You can set the dimension name and values for the filters that you plan to use. For example, you can filter for REGION==us-east-1 OR REGION==us-west-1 . The Expression for that looks like this: { 'Dimensions': { 'Key': 'REGION', 'Values': [ 'us-east-1', \xe2\x80\x9cus-west-1\xe2\x80\x9d ] } }  The list of dimension values are OR\'d together to retrieve cost or usage data. You can create Expression and DimensionValues objects using either with* methods or set* methods in multiple lines.\nCompound dimension values with logical operations - You can use multiple Expression types and the logical operators AND/OR/NOT to create a list of one or more Expression objects. This allows you to filter on more advanced options. For example, you can filter on ((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE != DataTransfer) . The Expression for that looks like this: { 'And': [ {'Or': [ {'Dimensions': { 'Key': 'REGION', 'Values': [ 'us-east-1', 'us-west-1' ] }}, {'Tags': { 'Key': 'TagName', 'Values': ['Value1'] } } ]}, {'Not': {'Dimensions': { 'Key': 'USAGE_TYPE', 'Values': ['DataTransfer'] }}} ] }\n\n\nNote\n\nBecause each Expression can have only one operator, the service returns an error if more than one is specified. The following example shows an Expression object that creates an error.\n{ 'And': [ ... ], 'DimensionValues': { 'Dimension': 'USAGE_TYPE', 'Values': [ 'DataTransfer' ] } }\n\n\nNote\nFor GetRightsizingRecommendation action, a combination of OR and NOT is not supported. OR is not supported between different dimensions, or dimensions and tags. NOT operators aren\'t supported. Dimensions are also limited to LINKED_ACCOUNT , REGION , or RIGHTSIZING_TYPE .\n\n\n\n\nAnd (list) --Return results that match both Dimension objects.\n\n(dict) --Use Expression to filter by cost or by usage. There are two patterns:\n\nSimple dimension values - You can set the dimension name and values for the filters that you plan to use. For example, you can filter for REGION==us-east-1 OR REGION==us-west-1 . The Expression for that looks like this: { 'Dimensions': { 'Key': 'REGION', 'Values': [ 'us-east-1', \xe2\x80\x9cus-west-1\xe2\x80\x9d ] } }  The list of dimension values are OR\'d together to retrieve cost or usage data. You can create Expression and DimensionValues objects using either with* methods or set* methods in multiple lines.\nCompound dimension values with logical operations - You can use multiple Expression types and the logical operators AND/OR/NOT to create a list of one or more Expression objects. This allows you to filter on more advanced options. For example, you can filter on ((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE != DataTransfer) . The Expression for that looks like this: { 'And': [ {'Or': [ {'Dimensions': { 'Key': 'REGION', 'Values': [ 'us-east-1', 'us-west-1' ] }}, {'Tags': { 'Key': 'TagName', 'Values': ['Value1'] } } ]}, {'Not': {'Dimensions': { 'Key': 'USAGE_TYPE', 'Values': ['DataTransfer'] }}} ] }\n\n\nNote\n\nBecause each Expression can have only one operator, the service returns an error if more than one is specified. The following example shows an Expression object that creates an error.\n{ 'And': [ ... ], 'DimensionValues': { 'Dimension': 'USAGE_TYPE', 'Values': [ 'DataTransfer' ] } }\n\n\nNote\nFor GetRightsizingRecommendation action, a combination of OR and NOT is not supported. OR is not supported between different dimensions, or dimensions and tags. NOT operators aren\'t supported. Dimensions are also limited to LINKED_ACCOUNT , REGION , or RIGHTSIZING_TYPE .\n\n\n\n\nNot (dict) --Return results that don\'t match a Dimension object.\n\nDimensions (dict) --The specific Dimension to use for Expression .\n\nKey (string) --The names of the metadata types that you can use to filter and group your results. For example, AZ returns a list of Availability Zones.\n\nValues (list) --The metadata values that you can use to filter and group your results. You can use GetDimensionValues to find specific values.\n\n(string) --\n\n\nMatchOptions (list) --The match options that you can use to filter your results. MatchOptions is only applicable for actions related to Cost Category. The default values for MatchOptions is EQUALS and CASE_SENSITIVE .\n\n(string) --\n\n\n\n\nTags (dict) --The specific Tag to use for Expression .\n\nKey (string) --The key for the tag.\n\nValues (list) --The specific value of the tag.\n\n(string) --\n\n\nMatchOptions (list) --The match options that you can use to filter your results. MatchOptions is only applicable for only applicable for actions related to Cost Category. The default values for MatchOptions is EQUALS and CASE_SENSITIVE .\n\n(string) --\n\n\n\n\nCostCategories (dict) --The filter based on CostCategory values.\n\nKey (string) --The unique name of the Cost Category.\n\nValues (list) --The specific value of the Cost Category.\n\n(string) --\n\n\n\n\n\n

    :type Metrics: list
    :param Metrics: Which metrics are returned in the query. For more information about blended and unblended rates, see Why does the 'blended' annotation appear on some line items in my bill? .\nValid values are AmortizedCost , BlendedCost , NetAmortizedCost , NetUnblendedCost , NormalizedUsageAmount , UnblendedCost , and UsageQuantity .\n\nNote\n\nIf you return the UsageQuantity metric, the service aggregates all usage numbers without taking the units into account. For example, if you aggregate usageQuantity across all of Amazon EC2, the results aren\'t meaningful because Amazon EC2 compute hours and data transfer are measured in different units (for example, hours vs. GB). To get more meaningful UsageQuantity metrics, filter by UsageType or UsageTypeGroups .\nMetrics is required for GetCostAndUsageWithResources requests.\n\n\n(string) --\n\n

    :type GroupBy: list
    :param GroupBy: You can group Amazon Web Services costs using up to two different groups: either dimensions, tag keys, or both.\n\n(dict) --Represents a group when you specify a group by criteria or in the response to a query with a specific grouping.\n\nType (string) --The string that represents the type of group.\n\nKey (string) --The string that represents a key for a specified group.\n\n\n\n\n

    :type NextPageToken: string
    :param NextPageToken: The token to retrieve the next set of results. AWS provides the token when the response from a previous call has more results than the maximum page size.

    :rtype: dict

ReturnsResponse Syntax
{
    'NextPageToken': 'string',
    'GroupDefinitions': [
        {
            'Type': 'DIMENSION'|'TAG'|'COST_CATEGORY',
            'Key': 'string'
        },
    ],
    'ResultsByTime': [
        {
            'TimePeriod': {
                'Start': 'string',
                'End': 'string'
            },
            'Total': {
                'string': {
                    'Amount': 'string',
                    'Unit': 'string'
                }
            },
            'Groups': [
                {
                    'Keys': [
                        'string',
                    ],
                    'Metrics': {
                        'string': {
                            'Amount': 'string',
                            'Unit': 'string'
                        }
                    }
                },
            ],
            'Estimated': True|False
        },
    ]
}


Response Structure

(dict) --

NextPageToken (string) --
The token for the next set of retrievable results. AWS provides the token when the response from a previous call has more results than the maximum page size.

GroupDefinitions (list) --
The groups that are specified by the Filter or GroupBy parameters in the request.

(dict) --
Represents a group when you specify a group by criteria or in the response to a query with a specific grouping.

Type (string) --
The string that represents the type of group.

Key (string) --
The string that represents a key for a specified group.





ResultsByTime (list) --
The time period that is covered by the results in the response.

(dict) --
The result that is associated with a time period.

TimePeriod (dict) --
The time period that the result covers.

Start (string) --
The beginning of the time period that you want the usage and costs for. The start date is inclusive. For example, if start is 2017-01-01 , AWS retrieves cost and usage data starting at 2017-01-01 up to the end date.

End (string) --
The end of the time period that you want the usage and costs for. The end date is exclusive. For example, if end is 2017-05-01 , AWS retrieves cost and usage data from the start date up to, but not including, 2017-05-01 .



Total (dict) --
The total amount of cost or usage accrued during the time period.

(string) --

(dict) --
The aggregated value for a metric.

Amount (string) --
The actual number that represents the metric.

Unit (string) --
The unit that the metric is given in.







Groups (list) --
The groups that this time period includes.

(dict) --
One level of grouped data in the results.

Keys (list) --
The keys that are included in this group.

(string) --


Metrics (dict) --
The metrics that are included in this group.

(string) --

(dict) --
The aggregated value for a metric.

Amount (string) --
The actual number that represents the metric.

Unit (string) --
The unit that the metric is given in.











Estimated (boolean) --
Whether the result is estimated.











Exceptions

CostExplorer.Client.exceptions.DataUnavailableException
CostExplorer.Client.exceptions.LimitExceededException
CostExplorer.Client.exceptions.BillExpirationException
CostExplorer.Client.exceptions.InvalidNextTokenException
CostExplorer.Client.exceptions.RequestChangedException


    :return: {
        'NextPageToken': 'string',
        'GroupDefinitions': [
            {
                'Type': 'DIMENSION'|'TAG'|'COST_CATEGORY',
                'Key': 'string'
            },
        ],
        'ResultsByTime': [
            {
                'TimePeriod': {
                    'Start': 'string',
                    'End': 'string'
                },
                'Total': {
                    'string': {
                        'Amount': 'string',
                        'Unit': 'string'
                    }
                },
                'Groups': [
                    {
                        'Keys': [
                            'string',
                        ],
                        'Metrics': {
                            'string': {
                                'Amount': 'string',
                                'Unit': 'string'
                            }
                        }
                    },
                ],
                'Estimated': True|False
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_cost_forecast(TimePeriod=None, Metric=None, Granularity=None, Filter=None, PredictionIntervalLevel=None):
    """
    Retrieves a forecast for how much Amazon Web Services predicts that you will spend over the forecast time period that you select, based on your past costs.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_cost_forecast(
        TimePeriod={
            'Start': 'string',
            'End': 'string'
        },
        Metric='BLENDED_COST'|'UNBLENDED_COST'|'AMORTIZED_COST'|'NET_UNBLENDED_COST'|'NET_AMORTIZED_COST'|'USAGE_QUANTITY'|'NORMALIZED_USAGE_AMOUNT',
        Granularity='DAILY'|'MONTHLY'|'HOURLY',
        Filter={
            'Or': [
                {'... recursive ...'},
            ],
            'And': [
                {'... recursive ...'},
            ],
            'Not': {'... recursive ...'},
            'Dimensions': {
                'Key': 'AZ'|'INSTANCE_TYPE'|'LINKED_ACCOUNT'|'LINKED_ACCOUNT_NAME'|'OPERATION'|'PURCHASE_TYPE'|'REGION'|'SERVICE'|'SERVICE_CODE'|'USAGE_TYPE'|'USAGE_TYPE_GROUP'|'RECORD_TYPE'|'OPERATING_SYSTEM'|'TENANCY'|'SCOPE'|'PLATFORM'|'SUBSCRIPTION_ID'|'LEGAL_ENTITY_NAME'|'DEPLOYMENT_OPTION'|'DATABASE_ENGINE'|'CACHE_ENGINE'|'INSTANCE_TYPE_FAMILY'|'BILLING_ENTITY'|'RESERVATION_ID'|'RESOURCE_ID'|'RIGHTSIZING_TYPE'|'SAVINGS_PLANS_TYPE'|'SAVINGS_PLAN_ARN'|'PAYMENT_OPTION',
                'Values': [
                    'string',
                ],
                'MatchOptions': [
                    'EQUALS'|'STARTS_WITH'|'ENDS_WITH'|'CONTAINS'|'CASE_SENSITIVE'|'CASE_INSENSITIVE',
                ]
            },
            'Tags': {
                'Key': 'string',
                'Values': [
                    'string',
                ],
                'MatchOptions': [
                    'EQUALS'|'STARTS_WITH'|'ENDS_WITH'|'CONTAINS'|'CASE_SENSITIVE'|'CASE_INSENSITIVE',
                ]
            },
            'CostCategories': {
                'Key': 'string',
                'Values': [
                    'string',
                ]
            }
        },
        PredictionIntervalLevel=123
    )
    
    
    :type TimePeriod: dict
    :param TimePeriod: [REQUIRED]\nThe period of time that you want the forecast to cover.\n\nStart (string) -- [REQUIRED]The beginning of the time period that you want the usage and costs for. The start date is inclusive. For example, if start is 2017-01-01 , AWS retrieves cost and usage data starting at 2017-01-01 up to the end date.\n\nEnd (string) -- [REQUIRED]The end of the time period that you want the usage and costs for. The end date is exclusive. For example, if end is 2017-05-01 , AWS retrieves cost and usage data from the start date up to, but not including, 2017-05-01 .\n\n\n

    :type Metric: string
    :param Metric: [REQUIRED]\nWhich metric Cost Explorer uses to create your forecast. For more information about blended and unblended rates, see Why does the 'blended' annotation appear on some line items in my bill? .\nValid values for a GetCostForecast call are the following:\n\nAMORTIZED_COST\nBLENDED_COST\nNET_AMORTIZED_COST\nNET_UNBLENDED_COST\nUNBLENDED_COST\n\n

    :type Granularity: string
    :param Granularity: [REQUIRED]\nHow granular you want the forecast to be. You can get 3 months of DAILY forecasts or 12 months of MONTHLY forecasts.\nThe GetCostForecast operation supports only DAILY and MONTHLY granularities.\n

    :type Filter: dict
    :param Filter: The filters that you want to use to filter your forecast. Cost Explorer API supports all of the Cost Explorer filters.\n\nOr (list) --Return results that match either Dimension object.\n\n(dict) --Use Expression to filter by cost or by usage. There are two patterns:\n\nSimple dimension values - You can set the dimension name and values for the filters that you plan to use. For example, you can filter for REGION==us-east-1 OR REGION==us-west-1 . The Expression for that looks like this: { 'Dimensions': { 'Key': 'REGION', 'Values': [ 'us-east-1', \xe2\x80\x9cus-west-1\xe2\x80\x9d ] } }  The list of dimension values are OR\'d together to retrieve cost or usage data. You can create Expression and DimensionValues objects using either with* methods or set* methods in multiple lines.\nCompound dimension values with logical operations - You can use multiple Expression types and the logical operators AND/OR/NOT to create a list of one or more Expression objects. This allows you to filter on more advanced options. For example, you can filter on ((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE != DataTransfer) . The Expression for that looks like this: { 'And': [ {'Or': [ {'Dimensions': { 'Key': 'REGION', 'Values': [ 'us-east-1', 'us-west-1' ] }}, {'Tags': { 'Key': 'TagName', 'Values': ['Value1'] } } ]}, {'Not': {'Dimensions': { 'Key': 'USAGE_TYPE', 'Values': ['DataTransfer'] }}} ] }\n\n\nNote\n\nBecause each Expression can have only one operator, the service returns an error if more than one is specified. The following example shows an Expression object that creates an error.\n{ 'And': [ ... ], 'DimensionValues': { 'Dimension': 'USAGE_TYPE', 'Values': [ 'DataTransfer' ] } }\n\n\nNote\nFor GetRightsizingRecommendation action, a combination of OR and NOT is not supported. OR is not supported between different dimensions, or dimensions and tags. NOT operators aren\'t supported. Dimensions are also limited to LINKED_ACCOUNT , REGION , or RIGHTSIZING_TYPE .\n\n\n\n\nAnd (list) --Return results that match both Dimension objects.\n\n(dict) --Use Expression to filter by cost or by usage. There are two patterns:\n\nSimple dimension values - You can set the dimension name and values for the filters that you plan to use. For example, you can filter for REGION==us-east-1 OR REGION==us-west-1 . The Expression for that looks like this: { 'Dimensions': { 'Key': 'REGION', 'Values': [ 'us-east-1', \xe2\x80\x9cus-west-1\xe2\x80\x9d ] } }  The list of dimension values are OR\'d together to retrieve cost or usage data. You can create Expression and DimensionValues objects using either with* methods or set* methods in multiple lines.\nCompound dimension values with logical operations - You can use multiple Expression types and the logical operators AND/OR/NOT to create a list of one or more Expression objects. This allows you to filter on more advanced options. For example, you can filter on ((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE != DataTransfer) . The Expression for that looks like this: { 'And': [ {'Or': [ {'Dimensions': { 'Key': 'REGION', 'Values': [ 'us-east-1', 'us-west-1' ] }}, {'Tags': { 'Key': 'TagName', 'Values': ['Value1'] } } ]}, {'Not': {'Dimensions': { 'Key': 'USAGE_TYPE', 'Values': ['DataTransfer'] }}} ] }\n\n\nNote\n\nBecause each Expression can have only one operator, the service returns an error if more than one is specified. The following example shows an Expression object that creates an error.\n{ 'And': [ ... ], 'DimensionValues': { 'Dimension': 'USAGE_TYPE', 'Values': [ 'DataTransfer' ] } }\n\n\nNote\nFor GetRightsizingRecommendation action, a combination of OR and NOT is not supported. OR is not supported between different dimensions, or dimensions and tags. NOT operators aren\'t supported. Dimensions are also limited to LINKED_ACCOUNT , REGION , or RIGHTSIZING_TYPE .\n\n\n\n\nNot (dict) --Return results that don\'t match a Dimension object.\n\nDimensions (dict) --The specific Dimension to use for Expression .\n\nKey (string) --The names of the metadata types that you can use to filter and group your results. For example, AZ returns a list of Availability Zones.\n\nValues (list) --The metadata values that you can use to filter and group your results. You can use GetDimensionValues to find specific values.\n\n(string) --\n\n\nMatchOptions (list) --The match options that you can use to filter your results. MatchOptions is only applicable for actions related to Cost Category. The default values for MatchOptions is EQUALS and CASE_SENSITIVE .\n\n(string) --\n\n\n\n\nTags (dict) --The specific Tag to use for Expression .\n\nKey (string) --The key for the tag.\n\nValues (list) --The specific value of the tag.\n\n(string) --\n\n\nMatchOptions (list) --The match options that you can use to filter your results. MatchOptions is only applicable for only applicable for actions related to Cost Category. The default values for MatchOptions is EQUALS and CASE_SENSITIVE .\n\n(string) --\n\n\n\n\nCostCategories (dict) --The filter based on CostCategory values.\n\nKey (string) --The unique name of the Cost Category.\n\nValues (list) --The specific value of the Cost Category.\n\n(string) --\n\n\n\n\n\n

    :type PredictionIntervalLevel: integer
    :param PredictionIntervalLevel: Cost Explorer always returns the mean forecast as a single point. You can request a prediction interval around the mean by specifying a confidence level. The higher the confidence level, the more confident Cost Explorer is about the actual value falling in the prediction interval. Higher confidence levels result in wider prediction intervals.

    :rtype: dict

ReturnsResponse Syntax
{
    'Total': {
        'Amount': 'string',
        'Unit': 'string'
    },
    'ForecastResultsByTime': [
        {
            'TimePeriod': {
                'Start': 'string',
                'End': 'string'
            },
            'MeanValue': 'string',
            'PredictionIntervalLowerBound': 'string',
            'PredictionIntervalUpperBound': 'string'
        },
    ]
}


Response Structure

(dict) --

Total (dict) --
How much you are forecasted to spend over the forecast period, in USD .

Amount (string) --
The actual number that represents the metric.

Unit (string) --
The unit that the metric is given in.



ForecastResultsByTime (list) --
The forecasts for your query, in order. For DAILY forecasts, this is a list of days. For MONTHLY forecasts, this is a list of months.

(dict) --
The forecast created for your query.

TimePeriod (dict) --
The period of time that the forecast covers.

Start (string) --
The beginning of the time period that you want the usage and costs for. The start date is inclusive. For example, if start is 2017-01-01 , AWS retrieves cost and usage data starting at 2017-01-01 up to the end date.

End (string) --
The end of the time period that you want the usage and costs for. The end date is exclusive. For example, if end is 2017-05-01 , AWS retrieves cost and usage data from the start date up to, but not including, 2017-05-01 .



MeanValue (string) --
The mean value of the forecast.

PredictionIntervalLowerBound (string) --
The lower limit for the prediction interval.

PredictionIntervalUpperBound (string) --
The upper limit for the prediction interval.











Exceptions

CostExplorer.Client.exceptions.LimitExceededException
CostExplorer.Client.exceptions.DataUnavailableException


    :return: {
        'Total': {
            'Amount': 'string',
            'Unit': 'string'
        },
        'ForecastResultsByTime': [
            {
                'TimePeriod': {
                    'Start': 'string',
                    'End': 'string'
                },
                'MeanValue': 'string',
                'PredictionIntervalLowerBound': 'string',
                'PredictionIntervalUpperBound': 'string'
            },
        ]
    }
    
    
    :returns: 
    CostExplorer.Client.exceptions.LimitExceededException
    CostExplorer.Client.exceptions.DataUnavailableException
    
    """
    pass

def get_dimension_values(SearchString=None, TimePeriod=None, Dimension=None, Context=None, NextPageToken=None):
    """
    Retrieves all available filter values for a specified filter over a period of time. You can search the dimension values for an arbitrary string.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_dimension_values(
        SearchString='string',
        TimePeriod={
            'Start': 'string',
            'End': 'string'
        },
        Dimension='AZ'|'INSTANCE_TYPE'|'LINKED_ACCOUNT'|'LINKED_ACCOUNT_NAME'|'OPERATION'|'PURCHASE_TYPE'|'REGION'|'SERVICE'|'SERVICE_CODE'|'USAGE_TYPE'|'USAGE_TYPE_GROUP'|'RECORD_TYPE'|'OPERATING_SYSTEM'|'TENANCY'|'SCOPE'|'PLATFORM'|'SUBSCRIPTION_ID'|'LEGAL_ENTITY_NAME'|'DEPLOYMENT_OPTION'|'DATABASE_ENGINE'|'CACHE_ENGINE'|'INSTANCE_TYPE_FAMILY'|'BILLING_ENTITY'|'RESERVATION_ID'|'RESOURCE_ID'|'RIGHTSIZING_TYPE'|'SAVINGS_PLANS_TYPE'|'SAVINGS_PLAN_ARN'|'PAYMENT_OPTION',
        Context='COST_AND_USAGE'|'RESERVATIONS'|'SAVINGS_PLANS',
        NextPageToken='string'
    )
    
    
    :type SearchString: string
    :param SearchString: The value that you want to search the filter values for.

    :type TimePeriod: dict
    :param TimePeriod: [REQUIRED]\nThe start and end dates for retrieving the dimension values. The start date is inclusive, but the end date is exclusive. For example, if start is 2017-01-01 and end is 2017-05-01 , then the cost and usage data is retrieved from 2017-01-01 up to and including 2017-04-30 but not including 2017-05-01 .\n\nStart (string) -- [REQUIRED]The beginning of the time period that you want the usage and costs for. The start date is inclusive. For example, if start is 2017-01-01 , AWS retrieves cost and usage data starting at 2017-01-01 up to the end date.\n\nEnd (string) -- [REQUIRED]The end of the time period that you want the usage and costs for. The end date is exclusive. For example, if end is 2017-05-01 , AWS retrieves cost and usage data from the start date up to, but not including, 2017-05-01 .\n\n\n

    :type Dimension: string
    :param Dimension: [REQUIRED]\nThe name of the dimension. Each Dimension is available for a different Context . For more information, see Context .\n

    :type Context: string
    :param Context: The context for the call to GetDimensionValues . This can be RESERVATIONS or COST_AND_USAGE . The default value is COST_AND_USAGE . If the context is set to RESERVATIONS , the resulting dimension values can be used in the GetReservationUtilization operation. If the context is set to COST_AND_USAGE , the resulting dimension values can be used in the GetCostAndUsage operation.\nIf you set the context to COST_AND_USAGE , you can use the following dimensions for searching:\n\nAZ - The Availability Zone. An example is us-east-1a .\nDATABASE_ENGINE - The Amazon Relational Database Service database. Examples are Aurora or MySQL.\nINSTANCE_TYPE - The type of Amazon EC2 instance. An example is m4.xlarge .\nLEGAL_ENTITY_NAME - The name of the organization that sells you AWS services, such as Amazon Web Services.\nLINKED_ACCOUNT - The description in the attribute map that includes the full name of the member account. The value field contains the AWS ID of the member account.\nOPERATING_SYSTEM - The operating system. Examples are Windows or Linux.\nOPERATION - The action performed. Examples include RunInstance and CreateBucket .\nPLATFORM - The Amazon EC2 operating system. Examples are Windows or Linux.\nPURCHASE_TYPE - The reservation type of the purchase to which this usage is related. Examples include On-Demand Instances and Standard Reserved Instances.\nSERVICE - The AWS service such as Amazon DynamoDB.\nUSAGE_TYPE - The type of usage. An example is DataTransfer-In-Bytes. The response for the GetDimensionValues operation includes a unit attribute. Examples include GB and Hrs.\nUSAGE_TYPE_GROUP - The grouping of common usage types. An example is Amazon EC2: CloudWatch \xe2\x80\x93 Alarms. The response for this operation includes a unit attribute.\nRECORD_TYPE - The different types of charges such as RI fees, usage costs, tax refunds, and credits.\nRESOURCE_ID - The unique identifier of the resource. ResourceId is an opt-in feature only available for last 14 days for EC2-Compute Service.\n\nIf you set the context to RESERVATIONS , you can use the following dimensions for searching:\n\nAZ - The Availability Zone. An example is us-east-1a .\nCACHE_ENGINE - The Amazon ElastiCache operating system. Examples are Windows or Linux.\nDEPLOYMENT_OPTION - The scope of Amazon Relational Database Service deployments. Valid values are SingleAZ and MultiAZ .\nINSTANCE_TYPE - The type of Amazon EC2 instance. An example is m4.xlarge .\nLINKED_ACCOUNT - The description in the attribute map that includes the full name of the member account. The value field contains the AWS ID of the member account.\nPLATFORM - The Amazon EC2 operating system. Examples are Windows or Linux.\nREGION - The AWS Region.\nSCOPE (Utilization only) - The scope of a Reserved Instance (RI). Values are regional or a single Availability Zone.\nTAG (Coverage only) - The tags that are associated with a Reserved Instance (RI).\nTENANCY - The tenancy of a resource. Examples are shared or dedicated.\n\nIf you set the context to SAVINGS_PLANS , you can use the following dimensions for searching:\n\nSAVINGS_PLANS_TYPE - Type of Savings Plans (EC2 Instance or Compute)\nPAYMENT_OPTION - Payment option for the given Savings Plans (for example, All Upfront)\nREGION - The AWS Region.\nINSTANCE_TYPE_FAMILY - The family of instances (For example, m5 )\nLINKED_ACCOUNT - The description in the attribute map that includes the full name of the member account. The value field contains the AWS ID of the member account.\nSAVINGS_PLAN_ARN - The unique identifier for your Savings Plan\n\n

    :type NextPageToken: string
    :param NextPageToken: The token to retrieve the next set of results. AWS provides the token when the response from a previous call has more results than the maximum page size.

    :rtype: dict

ReturnsResponse Syntax
{
    'DimensionValues': [
        {
            'Value': 'string',
            'Attributes': {
                'string': 'string'
            }
        },
    ],
    'ReturnSize': 123,
    'TotalSize': 123,
    'NextPageToken': 'string'
}


Response Structure

(dict) --

DimensionValues (list) --
The filters that you used to filter your request. Some dimensions are available only for a specific context.
If you set the context to COST_AND_USAGE , you can use the following dimensions for searching:

AZ - The Availability Zone. An example is us-east-1a .
DATABASE_ENGINE - The Amazon Relational Database Service database. Examples are Aurora or MySQL.
INSTANCE_TYPE - The type of Amazon EC2 instance. An example is m4.xlarge .
LEGAL_ENTITY_NAME - The name of the organization that sells you AWS services, such as Amazon Web Services.
LINKED_ACCOUNT - The description in the attribute map that includes the full name of the member account. The value field contains the AWS ID of the member account.
OPERATING_SYSTEM - The operating system. Examples are Windows or Linux.
OPERATION - The action performed. Examples include RunInstance and CreateBucket .
PLATFORM - The Amazon EC2 operating system. Examples are Windows or Linux.
PURCHASE_TYPE - The reservation type of the purchase to which this usage is related. Examples include On-Demand Instances and Standard Reserved Instances.
SERVICE - The AWS service such as Amazon DynamoDB.
USAGE_TYPE - The type of usage. An example is DataTransfer-In-Bytes. The response for the GetDimensionValues operation includes a unit attribute. Examples include GB and Hrs.
USAGE_TYPE_GROUP - The grouping of common usage types. An example is Amazon EC2: CloudWatch \xe2\x80\x93 Alarms. The response for this operation includes a unit attribute.
RECORD_TYPE - The different types of charges such as RI fees, usage costs, tax refunds, and credits.
RESOURCE_ID - The unique identifier of the resource. ResourceId is an opt-in feature only available for last 14 days for EC2-Compute Service.

If you set the context to RESERVATIONS , you can use the following dimensions for searching:

AZ - The Availability Zone. An example is us-east-1a .
CACHE_ENGINE - The Amazon ElastiCache operating system. Examples are Windows or Linux.
DEPLOYMENT_OPTION - The scope of Amazon Relational Database Service deployments. Valid values are SingleAZ and MultiAZ .
INSTANCE_TYPE - The type of Amazon EC2 instance. An example is m4.xlarge .
LINKED_ACCOUNT - The description in the attribute map that includes the full name of the member account. The value field contains the AWS ID of the member account.
PLATFORM - The Amazon EC2 operating system. Examples are Windows or Linux.
REGION - The AWS Region.
SCOPE (Utilization only) - The scope of a Reserved Instance (RI). Values are regional or a single Availability Zone.
TAG (Coverage only) - The tags that are associated with a Reserved Instance (RI).
TENANCY - The tenancy of a resource. Examples are shared or dedicated.

If you set the context to SAVINGS_PLANS , you can use the following dimensions for searching:

SAVINGS_PLANS_TYPE - Type of Savings Plans (EC2 Instance or Compute)
PAYMENT_OPTION - Payment option for the given Savings Plans (for example, All Upfront)
REGION - The AWS Region.
INSTANCE_TYPE_FAMILY - The family of instances (For example, m5 )
LINKED_ACCOUNT - The description in the attribute map that includes the full name of the member account. The value field contains the AWS ID of the member account.
SAVINGS_PLAN_ARN - The unique identifier for your Savings Plan


(dict) --
The metadata of a specific type that you can use to filter and group your results. You can use GetDimensionValues to find specific values.

Value (string) --
The value of a dimension with a specific attribute.

Attributes (dict) --
The attribute that applies to a specific Dimension .

(string) --
(string) --








ReturnSize (integer) --
The number of results that AWS returned at one time.

TotalSize (integer) --
The total number of search results.

NextPageToken (string) --
The token for the next set of retrievable results. AWS provides the token when the response from a previous call has more results than the maximum page size.







Exceptions

CostExplorer.Client.exceptions.LimitExceededException
CostExplorer.Client.exceptions.BillExpirationException
CostExplorer.Client.exceptions.DataUnavailableException
CostExplorer.Client.exceptions.InvalidNextTokenException
CostExplorer.Client.exceptions.RequestChangedException


    :return: {
        'DimensionValues': [
            {
                'Value': 'string',
                'Attributes': {
                    'string': 'string'
                }
            },
        ],
        'ReturnSize': 123,
        'TotalSize': 123,
        'NextPageToken': 'string'
    }
    
    
    :returns: 
    AZ - The Availability Zone. An example is us-east-1a .
    DATABASE_ENGINE - The Amazon Relational Database Service database. Examples are Aurora or MySQL.
    INSTANCE_TYPE - The type of Amazon EC2 instance. An example is m4.xlarge .
    LEGAL_ENTITY_NAME - The name of the organization that sells you AWS services, such as Amazon Web Services.
    LINKED_ACCOUNT - The description in the attribute map that includes the full name of the member account. The value field contains the AWS ID of the member account.
    OPERATING_SYSTEM - The operating system. Examples are Windows or Linux.
    OPERATION - The action performed. Examples include RunInstance and CreateBucket .
    PLATFORM - The Amazon EC2 operating system. Examples are Windows or Linux.
    PURCHASE_TYPE - The reservation type of the purchase to which this usage is related. Examples include On-Demand Instances and Standard Reserved Instances.
    SERVICE - The AWS service such as Amazon DynamoDB.
    USAGE_TYPE - The type of usage. An example is DataTransfer-In-Bytes. The response for the GetDimensionValues operation includes a unit attribute. Examples include GB and Hrs.
    USAGE_TYPE_GROUP - The grouping of common usage types. An example is Amazon EC2: CloudWatch \xe2\x80\x93 Alarms. The response for this operation includes a unit attribute.
    RECORD_TYPE - The different types of charges such as RI fees, usage costs, tax refunds, and credits.
    RESOURCE_ID - The unique identifier of the resource. ResourceId is an opt-in feature only available for last 14 days for EC2-Compute Service.
    
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

def get_reservation_coverage(TimePeriod=None, GroupBy=None, Granularity=None, Filter=None, Metrics=None, NextPageToken=None):
    """
    Retrieves the reservation coverage for your account. This enables you to see how much of your Amazon Elastic Compute Cloud, Amazon ElastiCache, Amazon Relational Database Service, or Amazon Redshift usage is covered by a reservation. An organization\'s master account can see the coverage of the associated member accounts. This supports dimensions, Cost Categories, and nested expressions. For any time period, you can filter data about reservation usage by the following dimensions:
    To determine valid values for a dimension, use the GetDimensionValues operation.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_reservation_coverage(
        TimePeriod={
            'Start': 'string',
            'End': 'string'
        },
        GroupBy=[
            {
                'Type': 'DIMENSION'|'TAG'|'COST_CATEGORY',
                'Key': 'string'
            },
        ],
        Granularity='DAILY'|'MONTHLY'|'HOURLY',
        Filter={
            'Or': [
                {'... recursive ...'},
            ],
            'And': [
                {'... recursive ...'},
            ],
            'Not': {'... recursive ...'},
            'Dimensions': {
                'Key': 'AZ'|'INSTANCE_TYPE'|'LINKED_ACCOUNT'|'LINKED_ACCOUNT_NAME'|'OPERATION'|'PURCHASE_TYPE'|'REGION'|'SERVICE'|'SERVICE_CODE'|'USAGE_TYPE'|'USAGE_TYPE_GROUP'|'RECORD_TYPE'|'OPERATING_SYSTEM'|'TENANCY'|'SCOPE'|'PLATFORM'|'SUBSCRIPTION_ID'|'LEGAL_ENTITY_NAME'|'DEPLOYMENT_OPTION'|'DATABASE_ENGINE'|'CACHE_ENGINE'|'INSTANCE_TYPE_FAMILY'|'BILLING_ENTITY'|'RESERVATION_ID'|'RESOURCE_ID'|'RIGHTSIZING_TYPE'|'SAVINGS_PLANS_TYPE'|'SAVINGS_PLAN_ARN'|'PAYMENT_OPTION',
                'Values': [
                    'string',
                ],
                'MatchOptions': [
                    'EQUALS'|'STARTS_WITH'|'ENDS_WITH'|'CONTAINS'|'CASE_SENSITIVE'|'CASE_INSENSITIVE',
                ]
            },
            'Tags': {
                'Key': 'string',
                'Values': [
                    'string',
                ],
                'MatchOptions': [
                    'EQUALS'|'STARTS_WITH'|'ENDS_WITH'|'CONTAINS'|'CASE_SENSITIVE'|'CASE_INSENSITIVE',
                ]
            },
            'CostCategories': {
                'Key': 'string',
                'Values': [
                    'string',
                ]
            }
        },
        Metrics=[
            'string',
        ],
        NextPageToken='string'
    )
    
    
    :type TimePeriod: dict
    :param TimePeriod: [REQUIRED]\nThe start and end dates of the period that you want to retrieve data about reservation coverage for. You can retrieve data for a maximum of 13 months: the last 12 months and the current month. The start date is inclusive, but the end date is exclusive. For example, if start is 2017-01-01 and end is 2017-05-01 , then the cost and usage data is retrieved from 2017-01-01 up to and including 2017-04-30 but not including 2017-05-01 .\n\nStart (string) -- [REQUIRED]The beginning of the time period that you want the usage and costs for. The start date is inclusive. For example, if start is 2017-01-01 , AWS retrieves cost and usage data starting at 2017-01-01 up to the end date.\n\nEnd (string) -- [REQUIRED]The end of the time period that you want the usage and costs for. The end date is exclusive. For example, if end is 2017-05-01 , AWS retrieves cost and usage data from the start date up to, but not including, 2017-05-01 .\n\n\n

    :type GroupBy: list
    :param GroupBy: You can group the data by the following attributes:\n\nAZ\nCACHE_ENGINE\nDATABASE_ENGINE\nDEPLOYMENT_OPTION\nINSTANCE_TYPE\nLINKED_ACCOUNT\nOPERATING_SYSTEM\nPLATFORM\nREGION\nTENANCY\n\n\n(dict) --Represents a group when you specify a group by criteria or in the response to a query with a specific grouping.\n\nType (string) --The string that represents the type of group.\n\nKey (string) --The string that represents a key for a specified group.\n\n\n\n\n

    :type Granularity: string
    :param Granularity: The granularity of the AWS cost data for the reservation. Valid values are MONTHLY and DAILY .\nIf GroupBy is set, Granularity can\'t be set. If Granularity isn\'t set, the response object doesn\'t include Granularity , either MONTHLY or DAILY .\nThe GetReservationCoverage operation supports only DAILY and MONTHLY granularities.\n

    :type Filter: dict
    :param Filter: Filters utilization data by dimensions. You can filter by the following dimensions:\n\nAZ\nCACHE_ENGINE\nDATABASE_ENGINE\nDEPLOYMENT_OPTION\nINSTANCE_TYPE\nLINKED_ACCOUNT\nOPERATING_SYSTEM\nPLATFORM\nREGION\nSERVICE\nTAG\nTENANCY\n\n\nGetReservationCoverage uses the same Expression object as the other operations, but only AND is supported among each dimension. You can nest only one level deep. If there are multiple values for a dimension, they are OR\'d together.\nIf you don\'t provide a SERVICE filter, Cost Explorer defaults to EC2.\nCost category is also supported.\n\nOr (list) --Return results that match either Dimension object.\n\n(dict) --Use Expression to filter by cost or by usage. There are two patterns:\n\nSimple dimension values - You can set the dimension name and values for the filters that you plan to use. For example, you can filter for REGION==us-east-1 OR REGION==us-west-1 . The Expression for that looks like this: { 'Dimensions': { 'Key': 'REGION', 'Values': [ 'us-east-1', \xe2\x80\x9cus-west-1\xe2\x80\x9d ] } }  The list of dimension values are OR\'d together to retrieve cost or usage data. You can create Expression and DimensionValues objects using either with* methods or set* methods in multiple lines.\nCompound dimension values with logical operations - You can use multiple Expression types and the logical operators AND/OR/NOT to create a list of one or more Expression objects. This allows you to filter on more advanced options. For example, you can filter on ((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE != DataTransfer) . The Expression for that looks like this: { 'And': [ {'Or': [ {'Dimensions': { 'Key': 'REGION', 'Values': [ 'us-east-1', 'us-west-1' ] }}, {'Tags': { 'Key': 'TagName', 'Values': ['Value1'] } } ]}, {'Not': {'Dimensions': { 'Key': 'USAGE_TYPE', 'Values': ['DataTransfer'] }}} ] }\n\n\nNote\n\nBecause each Expression can have only one operator, the service returns an error if more than one is specified. The following example shows an Expression object that creates an error.\n{ 'And': [ ... ], 'DimensionValues': { 'Dimension': 'USAGE_TYPE', 'Values': [ 'DataTransfer' ] } }\n\n\nNote\nFor GetRightsizingRecommendation action, a combination of OR and NOT is not supported. OR is not supported between different dimensions, or dimensions and tags. NOT operators aren\'t supported. Dimensions are also limited to LINKED_ACCOUNT , REGION , or RIGHTSIZING_TYPE .\n\n\n\n\nAnd (list) --Return results that match both Dimension objects.\n\n(dict) --Use Expression to filter by cost or by usage. There are two patterns:\n\nSimple dimension values - You can set the dimension name and values for the filters that you plan to use. For example, you can filter for REGION==us-east-1 OR REGION==us-west-1 . The Expression for that looks like this: { 'Dimensions': { 'Key': 'REGION', 'Values': [ 'us-east-1', \xe2\x80\x9cus-west-1\xe2\x80\x9d ] } }  The list of dimension values are OR\'d together to retrieve cost or usage data. You can create Expression and DimensionValues objects using either with* methods or set* methods in multiple lines.\nCompound dimension values with logical operations - You can use multiple Expression types and the logical operators AND/OR/NOT to create a list of one or more Expression objects. This allows you to filter on more advanced options. For example, you can filter on ((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE != DataTransfer) . The Expression for that looks like this: { 'And': [ {'Or': [ {'Dimensions': { 'Key': 'REGION', 'Values': [ 'us-east-1', 'us-west-1' ] }}, {'Tags': { 'Key': 'TagName', 'Values': ['Value1'] } } ]}, {'Not': {'Dimensions': { 'Key': 'USAGE_TYPE', 'Values': ['DataTransfer'] }}} ] }\n\n\nNote\n\nBecause each Expression can have only one operator, the service returns an error if more than one is specified. The following example shows an Expression object that creates an error.\n{ 'And': [ ... ], 'DimensionValues': { 'Dimension': 'USAGE_TYPE', 'Values': [ 'DataTransfer' ] } }\n\n\nNote\nFor GetRightsizingRecommendation action, a combination of OR and NOT is not supported. OR is not supported between different dimensions, or dimensions and tags. NOT operators aren\'t supported. Dimensions are also limited to LINKED_ACCOUNT , REGION , or RIGHTSIZING_TYPE .\n\n\n\n\nNot (dict) --Return results that don\'t match a Dimension object.\n\nDimensions (dict) --The specific Dimension to use for Expression .\n\nKey (string) --The names of the metadata types that you can use to filter and group your results. For example, AZ returns a list of Availability Zones.\n\nValues (list) --The metadata values that you can use to filter and group your results. You can use GetDimensionValues to find specific values.\n\n(string) --\n\n\nMatchOptions (list) --The match options that you can use to filter your results. MatchOptions is only applicable for actions related to Cost Category. The default values for MatchOptions is EQUALS and CASE_SENSITIVE .\n\n(string) --\n\n\n\n\nTags (dict) --The specific Tag to use for Expression .\n\nKey (string) --The key for the tag.\n\nValues (list) --The specific value of the tag.\n\n(string) --\n\n\nMatchOptions (list) --The match options that you can use to filter your results. MatchOptions is only applicable for only applicable for actions related to Cost Category. The default values for MatchOptions is EQUALS and CASE_SENSITIVE .\n\n(string) --\n\n\n\n\nCostCategories (dict) --The filter based on CostCategory values.\n\nKey (string) --The unique name of the Cost Category.\n\nValues (list) --The specific value of the Cost Category.\n\n(string) --\n\n\n\n\n\n

    :type Metrics: list
    :param Metrics: The measurement that you want your reservation coverage reported in.\nValid values are Hour , Unit , and Cost . You can use multiple values in a request.\n\n(string) --\n\n

    :type NextPageToken: string
    :param NextPageToken: The token to retrieve the next set of results. AWS provides the token when the response from a previous call has more results than the maximum page size.

    :rtype: dict

ReturnsResponse Syntax
{
    'CoveragesByTime': [
        {
            'TimePeriod': {
                'Start': 'string',
                'End': 'string'
            },
            'Groups': [
                {
                    'Attributes': {
                        'string': 'string'
                    },
                    'Coverage': {
                        'CoverageHours': {
                            'OnDemandHours': 'string',
                            'ReservedHours': 'string',
                            'TotalRunningHours': 'string',
                            'CoverageHoursPercentage': 'string'
                        },
                        'CoverageNormalizedUnits': {
                            'OnDemandNormalizedUnits': 'string',
                            'ReservedNormalizedUnits': 'string',
                            'TotalRunningNormalizedUnits': 'string',
                            'CoverageNormalizedUnitsPercentage': 'string'
                        },
                        'CoverageCost': {
                            'OnDemandCost': 'string'
                        }
                    }
                },
            ],
            'Total': {
                'CoverageHours': {
                    'OnDemandHours': 'string',
                    'ReservedHours': 'string',
                    'TotalRunningHours': 'string',
                    'CoverageHoursPercentage': 'string'
                },
                'CoverageNormalizedUnits': {
                    'OnDemandNormalizedUnits': 'string',
                    'ReservedNormalizedUnits': 'string',
                    'TotalRunningNormalizedUnits': 'string',
                    'CoverageNormalizedUnitsPercentage': 'string'
                },
                'CoverageCost': {
                    'OnDemandCost': 'string'
                }
            }
        },
    ],
    'Total': {
        'CoverageHours': {
            'OnDemandHours': 'string',
            'ReservedHours': 'string',
            'TotalRunningHours': 'string',
            'CoverageHoursPercentage': 'string'
        },
        'CoverageNormalizedUnits': {
            'OnDemandNormalizedUnits': 'string',
            'ReservedNormalizedUnits': 'string',
            'TotalRunningNormalizedUnits': 'string',
            'CoverageNormalizedUnitsPercentage': 'string'
        },
        'CoverageCost': {
            'OnDemandCost': 'string'
        }
    },
    'NextPageToken': 'string'
}


Response Structure

(dict) --

CoveragesByTime (list) --
The amount of time that your reservations covered.

(dict) --
Reservation coverage for a specified period, in hours.

TimePeriod (dict) --
The period that this coverage was used over.

Start (string) --
The beginning of the time period that you want the usage and costs for. The start date is inclusive. For example, if start is 2017-01-01 , AWS retrieves cost and usage data starting at 2017-01-01 up to the end date.

End (string) --
The end of the time period that you want the usage and costs for. The end date is exclusive. For example, if end is 2017-05-01 , AWS retrieves cost and usage data from the start date up to, but not including, 2017-05-01 .



Groups (list) --
The groups of instances that the reservation covered.

(dict) --
A group of reservations that share a set of attributes.

Attributes (dict) --
The attributes for this group of reservations.

(string) --
(string) --




Coverage (dict) --
How much instance usage this group of reservations covered.

CoverageHours (dict) --
The amount of instance usage that the reservation covered, in hours.

OnDemandHours (string) --
The number of instance running hours that On-Demand Instances covered.

ReservedHours (string) --
The number of instance running hours that reservations covered.

TotalRunningHours (string) --
The total instance usage, in hours.

CoverageHoursPercentage (string) --
The percentage of instance hours that a reservation covered.



CoverageNormalizedUnits (dict) --
The amount of instance usage that the reservation covered, in normalized units.

OnDemandNormalizedUnits (string) --
The number of normalized units that are covered by On-Demand Instances instead of a reservation.

ReservedNormalizedUnits (string) --
The number of normalized units that a reservation covers.

TotalRunningNormalizedUnits (string) --
The total number of normalized units that you used.

CoverageNormalizedUnitsPercentage (string) --
The percentage of your used instance normalized units that a reservation covers.



CoverageCost (dict) --
The amount of cost that the reservation covered.

OnDemandCost (string) --
How much an On-Demand Instance costs.









Total (dict) --
The total reservation coverage, in hours.

CoverageHours (dict) --
The amount of instance usage that the reservation covered, in hours.

OnDemandHours (string) --
The number of instance running hours that On-Demand Instances covered.

ReservedHours (string) --
The number of instance running hours that reservations covered.

TotalRunningHours (string) --
The total instance usage, in hours.

CoverageHoursPercentage (string) --
The percentage of instance hours that a reservation covered.



CoverageNormalizedUnits (dict) --
The amount of instance usage that the reservation covered, in normalized units.

OnDemandNormalizedUnits (string) --
The number of normalized units that are covered by On-Demand Instances instead of a reservation.

ReservedNormalizedUnits (string) --
The number of normalized units that a reservation covers.

TotalRunningNormalizedUnits (string) --
The total number of normalized units that you used.

CoverageNormalizedUnitsPercentage (string) --
The percentage of your used instance normalized units that a reservation covers.



CoverageCost (dict) --
The amount of cost that the reservation covered.

OnDemandCost (string) --
How much an On-Demand Instance costs.









Total (dict) --
The total amount of instance usage that a reservation covered.

CoverageHours (dict) --
The amount of instance usage that the reservation covered, in hours.

OnDemandHours (string) --
The number of instance running hours that On-Demand Instances covered.

ReservedHours (string) --
The number of instance running hours that reservations covered.

TotalRunningHours (string) --
The total instance usage, in hours.

CoverageHoursPercentage (string) --
The percentage of instance hours that a reservation covered.



CoverageNormalizedUnits (dict) --
The amount of instance usage that the reservation covered, in normalized units.

OnDemandNormalizedUnits (string) --
The number of normalized units that are covered by On-Demand Instances instead of a reservation.

ReservedNormalizedUnits (string) --
The number of normalized units that a reservation covers.

TotalRunningNormalizedUnits (string) --
The total number of normalized units that you used.

CoverageNormalizedUnitsPercentage (string) --
The percentage of your used instance normalized units that a reservation covers.



CoverageCost (dict) --
The amount of cost that the reservation covered.

OnDemandCost (string) --
How much an On-Demand Instance costs.





NextPageToken (string) --
The token for the next set of retrievable results. AWS provides the token when the response from a previous call has more results than the maximum page size.







Exceptions

CostExplorer.Client.exceptions.LimitExceededException
CostExplorer.Client.exceptions.DataUnavailableException
CostExplorer.Client.exceptions.InvalidNextTokenException


    :return: {
        'CoveragesByTime': [
            {
                'TimePeriod': {
                    'Start': 'string',
                    'End': 'string'
                },
                'Groups': [
                    {
                        'Attributes': {
                            'string': 'string'
                        },
                        'Coverage': {
                            'CoverageHours': {
                                'OnDemandHours': 'string',
                                'ReservedHours': 'string',
                                'TotalRunningHours': 'string',
                                'CoverageHoursPercentage': 'string'
                            },
                            'CoverageNormalizedUnits': {
                                'OnDemandNormalizedUnits': 'string',
                                'ReservedNormalizedUnits': 'string',
                                'TotalRunningNormalizedUnits': 'string',
                                'CoverageNormalizedUnitsPercentage': 'string'
                            },
                            'CoverageCost': {
                                'OnDemandCost': 'string'
                            }
                        }
                    },
                ],
                'Total': {
                    'CoverageHours': {
                        'OnDemandHours': 'string',
                        'ReservedHours': 'string',
                        'TotalRunningHours': 'string',
                        'CoverageHoursPercentage': 'string'
                    },
                    'CoverageNormalizedUnits': {
                        'OnDemandNormalizedUnits': 'string',
                        'ReservedNormalizedUnits': 'string',
                        'TotalRunningNormalizedUnits': 'string',
                        'CoverageNormalizedUnitsPercentage': 'string'
                    },
                    'CoverageCost': {
                        'OnDemandCost': 'string'
                    }
                }
            },
        ],
        'Total': {
            'CoverageHours': {
                'OnDemandHours': 'string',
                'ReservedHours': 'string',
                'TotalRunningHours': 'string',
                'CoverageHoursPercentage': 'string'
            },
            'CoverageNormalizedUnits': {
                'OnDemandNormalizedUnits': 'string',
                'ReservedNormalizedUnits': 'string',
                'TotalRunningNormalizedUnits': 'string',
                'CoverageNormalizedUnitsPercentage': 'string'
            },
            'CoverageCost': {
                'OnDemandCost': 'string'
            }
        },
        'NextPageToken': 'string'
    }
    
    
    :returns: 
    TimePeriod (dict) -- [REQUIRED]
    The start and end dates of the period that you want to retrieve data about reservation coverage for. You can retrieve data for a maximum of 13 months: the last 12 months and the current month. The start date is inclusive, but the end date is exclusive. For example, if start is 2017-01-01 and end is 2017-05-01 , then the cost and usage data is retrieved from 2017-01-01 up to and including 2017-04-30 but not including 2017-05-01 .
    
    Start (string) -- [REQUIRED]The beginning of the time period that you want the usage and costs for. The start date is inclusive. For example, if start is 2017-01-01 , AWS retrieves cost and usage data starting at 2017-01-01 up to the end date.
    
    End (string) -- [REQUIRED]The end of the time period that you want the usage and costs for. The end date is exclusive. For example, if end is 2017-05-01 , AWS retrieves cost and usage data from the start date up to, but not including, 2017-05-01 .
    
    
    
    GroupBy (list) -- You can group the data by the following attributes:
    
    AZ
    CACHE_ENGINE
    DATABASE_ENGINE
    DEPLOYMENT_OPTION
    INSTANCE_TYPE
    LINKED_ACCOUNT
    OPERATING_SYSTEM
    PLATFORM
    REGION
    TENANCY
    
    
    (dict) --Represents a group when you specify a group by criteria or in the response to a query with a specific grouping.
    
    Type (string) --The string that represents the type of group.
    
    Key (string) --The string that represents a key for a specified group.
    
    
    
    
    
    Granularity (string) -- The granularity of the AWS cost data for the reservation. Valid values are MONTHLY and DAILY .
    If GroupBy is set, Granularity can\'t be set. If Granularity isn\'t set, the response object doesn\'t include Granularity , either MONTHLY or DAILY .
    The GetReservationCoverage operation supports only DAILY and MONTHLY granularities.
    
    Filter (dict) -- Filters utilization data by dimensions. You can filter by the following dimensions:
    
    AZ
    CACHE_ENGINE
    DATABASE_ENGINE
    DEPLOYMENT_OPTION
    INSTANCE_TYPE
    LINKED_ACCOUNT
    OPERATING_SYSTEM
    PLATFORM
    REGION
    SERVICE
    TAG
    TENANCY
    
    
    GetReservationCoverage uses the same Expression object as the other operations, but only AND is supported among each dimension. You can nest only one level deep. If there are multiple values for a dimension, they are OR\'d together.
    If you don\'t provide a SERVICE filter, Cost Explorer defaults to EC2.
    Cost category is also supported.
    
    Or (list) --Return results that match either Dimension object.
    
    (dict) --Use Expression to filter by cost or by usage. There are two patterns:
    
    Simple dimension values - You can set the dimension name and values for the filters that you plan to use. For example, you can filter for REGION==us-east-1 OR REGION==us-west-1 . The Expression for that looks like this:  { "Dimensions": { "Key": "REGION", "Values": [ "us-east-1", \xe2\x80\x9cus-west-1\xe2\x80\x9d ] } }   The list of dimension values are OR\'d together to retrieve cost or usage data. You can create Expression and DimensionValues objects using either with* methods or set* methods in multiple lines.
    Compound dimension values with logical operations - You can use multiple Expression types and the logical operators AND/OR/NOT to create a list of one or more Expression objects. This allows you to filter on more advanced options. For example, you can filter on ((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE != DataTransfer) . The Expression for that looks like this:  { "And": [ {"Or": [ {"Dimensions": { "Key": "REGION", "Values": [ "us-east-1", "us-west-1" ] }}, {"Tags": { "Key": "TagName", "Values": ["Value1"] } } ]}, {"Not": {"Dimensions": { "Key": "USAGE_TYPE", "Values": ["DataTransfer"] }}} ] }
    
    
    Note
    
    Because each Expression can have only one operator, the service returns an error if more than one is specified. The following example shows an Expression object that creates an error.
    { "And": [ ... ], "DimensionValues": { "Dimension": "USAGE_TYPE", "Values": [ "DataTransfer" ] } }
    
    
    Note
    For GetRightsizingRecommendation action, a combination of OR and NOT is not supported. OR is not supported between different dimensions, or dimensions and tags. NOT operators aren\'t supported. Dimensions are also limited to LINKED_ACCOUNT , REGION , or RIGHTSIZING_TYPE .
    
    
    
    
    And (list) --Return results that match both Dimension objects.
    
    (dict) --Use Expression to filter by cost or by usage. There are two patterns:
    
    Simple dimension values - You can set the dimension name and values for the filters that you plan to use. For example, you can filter for REGION==us-east-1 OR REGION==us-west-1 . The Expression for that looks like this:  { "Dimensions": { "Key": "REGION", "Values": [ "us-east-1", \xe2\x80\x9cus-west-1\xe2\x80\x9d ] } }   The list of dimension values are OR\'d together to retrieve cost or usage data. You can create Expression and DimensionValues objects using either with* methods or set* methods in multiple lines.
    Compound dimension values with logical operations - You can use multiple Expression types and the logical operators AND/OR/NOT to create a list of one or more Expression objects. This allows you to filter on more advanced options. For example, you can filter on ((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE != DataTransfer) . The Expression for that looks like this:  { "And": [ {"Or": [ {"Dimensions": { "Key": "REGION", "Values": [ "us-east-1", "us-west-1" ] }}, {"Tags": { "Key": "TagName", "Values": ["Value1"] } } ]}, {"Not": {"Dimensions": { "Key": "USAGE_TYPE", "Values": ["DataTransfer"] }}} ] }
    
    
    Note
    
    Because each Expression can have only one operator, the service returns an error if more than one is specified. The following example shows an Expression object that creates an error.
    { "And": [ ... ], "DimensionValues": { "Dimension": "USAGE_TYPE", "Values": [ "DataTransfer" ] } }
    
    
    Note
    For GetRightsizingRecommendation action, a combination of OR and NOT is not supported. OR is not supported between different dimensions, or dimensions and tags. NOT operators aren\'t supported. Dimensions are also limited to LINKED_ACCOUNT , REGION , or RIGHTSIZING_TYPE .
    
    
    
    
    Not (dict) --Return results that don\'t match a Dimension object.
    
    Dimensions (dict) --The specific Dimension to use for Expression .
    
    Key (string) --The names of the metadata types that you can use to filter and group your results. For example, AZ returns a list of Availability Zones.
    
    Values (list) --The metadata values that you can use to filter and group your results. You can use GetDimensionValues to find specific values.
    
    (string) --
    
    
    MatchOptions (list) --The match options that you can use to filter your results. MatchOptions is only applicable for actions related to Cost Category. The default values for MatchOptions is EQUALS and CASE_SENSITIVE .
    
    (string) --
    
    
    
    
    Tags (dict) --The specific Tag to use for Expression .
    
    Key (string) --The key for the tag.
    
    Values (list) --The specific value of the tag.
    
    (string) --
    
    
    MatchOptions (list) --The match options that you can use to filter your results. MatchOptions is only applicable for only applicable for actions related to Cost Category. The default values for MatchOptions is EQUALS and CASE_SENSITIVE .
    
    (string) --
    
    
    
    
    CostCategories (dict) --The filter based on CostCategory values.
    
    Key (string) --The unique name of the Cost Category.
    
    Values (list) --The specific value of the Cost Category.
    
    (string) --
    
    
    
    
    
    
    Metrics (list) -- The measurement that you want your reservation coverage reported in.
    Valid values are Hour , Unit , and Cost . You can use multiple values in a request.
    
    (string) --
    
    
    NextPageToken (string) -- The token to retrieve the next set of results. AWS provides the token when the response from a previous call has more results than the maximum page size.
    
    """
    pass

def get_reservation_purchase_recommendation(AccountId=None, Service=None, AccountScope=None, LookbackPeriodInDays=None, TermInYears=None, PaymentOption=None, ServiceSpecification=None, PageSize=None, NextPageToken=None):
    """
    Gets recommendations for which reservations to purchase. These recommendations could help you reduce your costs. Reservations provide a discounted hourly rate (up to 75%) compared to On-Demand pricing.
    AWS generates your recommendations by identifying your On-Demand usage during a specific time period and collecting your usage into categories that are eligible for a reservation. After AWS has these categories, it simulates every combination of reservations in each category of usage to identify the best number of each type of RI to purchase to maximize your estimated savings.
    For example, AWS automatically aggregates your Amazon EC2 Linux, shared tenancy, and c4 family usage in the US West (Oregon) Region and recommends that you buy size-flexible regional reservations to apply to the c4 family usage. AWS recommends the smallest size instance in an instance family. This makes it easier to purchase a size-flexible RI. AWS also shows the equal number of normalized units so that you can purchase any instance size that you want. For this example, your RI recommendation would be for c4.large because that is the smallest size instance in the c4 instance family.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_reservation_purchase_recommendation(
        AccountId='string',
        Service='string',
        AccountScope='PAYER'|'LINKED',
        LookbackPeriodInDays='SEVEN_DAYS'|'THIRTY_DAYS'|'SIXTY_DAYS',
        TermInYears='ONE_YEAR'|'THREE_YEARS',
        PaymentOption='NO_UPFRONT'|'PARTIAL_UPFRONT'|'ALL_UPFRONT'|'LIGHT_UTILIZATION'|'MEDIUM_UTILIZATION'|'HEAVY_UTILIZATION',
        ServiceSpecification={
            'EC2Specification': {
                'OfferingClass': 'STANDARD'|'CONVERTIBLE'
            }
        },
        PageSize=123,
        NextPageToken='string'
    )
    
    
    :type AccountId: string
    :param AccountId: The account ID that is associated with the recommendation.

    :type Service: string
    :param Service: [REQUIRED]\nThe specific service that you want recommendations for.\n

    :type AccountScope: string
    :param AccountScope: The account scope that you want your recommendations for. Amazon Web Services calculates recommendations including the payer account and linked accounts if the value is set to PAYER . If the value is LINKED , recommendations are calculated for individual linked accounts only.

    :type LookbackPeriodInDays: string
    :param LookbackPeriodInDays: The number of previous days that you want AWS to consider when it calculates your recommendations.

    :type TermInYears: string
    :param TermInYears: The reservation term that you want recommendations for.

    :type PaymentOption: string
    :param PaymentOption: The reservation purchase option that you want recommendations for.

    :type ServiceSpecification: dict
    :param ServiceSpecification: The hardware specifications for the service instances that you want recommendations for, such as standard or convertible Amazon EC2 instances.\n\nEC2Specification (dict) --The Amazon EC2 hardware specifications that you want AWS to provide recommendations for.\n\nOfferingClass (string) --Whether you want a recommendation for standard or convertible reservations.\n\n\n\n\n

    :type PageSize: integer
    :param PageSize: The number of recommendations that you want returned in a single response object.

    :type NextPageToken: string
    :param NextPageToken: The pagination token that indicates the next set of results that you want to retrieve.

    :rtype: dict

ReturnsResponse Syntax
{
    'Metadata': {
        'RecommendationId': 'string',
        'GenerationTimestamp': 'string'
    },
    'Recommendations': [
        {
            'AccountScope': 'PAYER'|'LINKED',
            'LookbackPeriodInDays': 'SEVEN_DAYS'|'THIRTY_DAYS'|'SIXTY_DAYS',
            'TermInYears': 'ONE_YEAR'|'THREE_YEARS',
            'PaymentOption': 'NO_UPFRONT'|'PARTIAL_UPFRONT'|'ALL_UPFRONT'|'LIGHT_UTILIZATION'|'MEDIUM_UTILIZATION'|'HEAVY_UTILIZATION',
            'ServiceSpecification': {
                'EC2Specification': {
                    'OfferingClass': 'STANDARD'|'CONVERTIBLE'
                }
            },
            'RecommendationDetails': [
                {
                    'AccountId': 'string',
                    'InstanceDetails': {
                        'EC2InstanceDetails': {
                            'Family': 'string',
                            'InstanceType': 'string',
                            'Region': 'string',
                            'AvailabilityZone': 'string',
                            'Platform': 'string',
                            'Tenancy': 'string',
                            'CurrentGeneration': True|False,
                            'SizeFlexEligible': True|False
                        },
                        'RDSInstanceDetails': {
                            'Family': 'string',
                            'InstanceType': 'string',
                            'Region': 'string',
                            'DatabaseEngine': 'string',
                            'DatabaseEdition': 'string',
                            'DeploymentOption': 'string',
                            'LicenseModel': 'string',
                            'CurrentGeneration': True|False,
                            'SizeFlexEligible': True|False
                        },
                        'RedshiftInstanceDetails': {
                            'Family': 'string',
                            'NodeType': 'string',
                            'Region': 'string',
                            'CurrentGeneration': True|False,
                            'SizeFlexEligible': True|False
                        },
                        'ElastiCacheInstanceDetails': {
                            'Family': 'string',
                            'NodeType': 'string',
                            'Region': 'string',
                            'ProductDescription': 'string',
                            'CurrentGeneration': True|False,
                            'SizeFlexEligible': True|False
                        },
                        'ESInstanceDetails': {
                            'InstanceClass': 'string',
                            'InstanceSize': 'string',
                            'Region': 'string',
                            'CurrentGeneration': True|False,
                            'SizeFlexEligible': True|False
                        }
                    },
                    'RecommendedNumberOfInstancesToPurchase': 'string',
                    'RecommendedNormalizedUnitsToPurchase': 'string',
                    'MinimumNumberOfInstancesUsedPerHour': 'string',
                    'MinimumNormalizedUnitsUsedPerHour': 'string',
                    'MaximumNumberOfInstancesUsedPerHour': 'string',
                    'MaximumNormalizedUnitsUsedPerHour': 'string',
                    'AverageNumberOfInstancesUsedPerHour': 'string',
                    'AverageNormalizedUnitsUsedPerHour': 'string',
                    'AverageUtilization': 'string',
                    'EstimatedBreakEvenInMonths': 'string',
                    'CurrencyCode': 'string',
                    'EstimatedMonthlySavingsAmount': 'string',
                    'EstimatedMonthlySavingsPercentage': 'string',
                    'EstimatedMonthlyOnDemandCost': 'string',
                    'EstimatedReservationCostForLookbackPeriod': 'string',
                    'UpfrontCost': 'string',
                    'RecurringStandardMonthlyCost': 'string'
                },
            ],
            'RecommendationSummary': {
                'TotalEstimatedMonthlySavingsAmount': 'string',
                'TotalEstimatedMonthlySavingsPercentage': 'string',
                'CurrencyCode': 'string'
            }
        },
    ],
    'NextPageToken': 'string'
}


Response Structure

(dict) --

Metadata (dict) --
Information about this specific recommendation call, such as the time stamp for when Cost Explorer generated this recommendation.

RecommendationId (string) --
The ID for this specific recommendation.

GenerationTimestamp (string) --
The timestamp for when AWS made this recommendation.



Recommendations (list) --
Recommendations for reservations to purchase.

(dict) --
A specific reservation that AWS recommends for purchase.

AccountScope (string) --
The account scope that AWS recommends that you purchase this instance for. For example, you can purchase this reservation for an entire organization in AWS Organizations.

LookbackPeriodInDays (string) --
How many days of previous usage that AWS considers when making this recommendation.

TermInYears (string) --
The term of the reservation that you want recommendations for, in years.

PaymentOption (string) --
The payment option for the reservation. For example, AllUpfront or NoUpfront .

ServiceSpecification (dict) --
Hardware specifications for the service that you want recommendations for.

EC2Specification (dict) --
The Amazon EC2 hardware specifications that you want AWS to provide recommendations for.

OfferingClass (string) --
Whether you want a recommendation for standard or convertible reservations.





RecommendationDetails (list) --
Details about the recommended purchases.

(dict) --
Details about your recommended reservation purchase.

AccountId (string) --
The account that this RI recommendation is for.

InstanceDetails (dict) --
Details about the instances that AWS recommends that you purchase.

EC2InstanceDetails (dict) --
The Amazon EC2 instances that AWS recommends that you purchase.

Family (string) --
The instance family of the recommended reservation.

InstanceType (string) --
The type of instance that AWS recommends.

Region (string) --
The AWS Region of the recommended reservation.

AvailabilityZone (string) --
The Availability Zone of the recommended reservation.

Platform (string) --
The platform of the recommended reservation. The platform is the specific combination of operating system, license model, and software on an instance.

Tenancy (string) --
Whether the recommended reservation is dedicated or shared.

CurrentGeneration (boolean) --
Whether the recommendation is for a current-generation instance.

SizeFlexEligible (boolean) --
Whether the recommended reservation is size flexible.



RDSInstanceDetails (dict) --
The Amazon RDS instances that AWS recommends that you purchase.

Family (string) --
The instance family of the recommended reservation.

InstanceType (string) --
The type of instance that AWS recommends.

Region (string) --
The AWS Region of the recommended reservation.

DatabaseEngine (string) --
The database engine that the recommended reservation supports.

DatabaseEdition (string) --
The database edition that the recommended reservation supports.

DeploymentOption (string) --
Whether the recommendation is for a reservation in a single Availability Zone or a reservation with a backup in a second Availability Zone.

LicenseModel (string) --
The license model that the recommended reservation supports.

CurrentGeneration (boolean) --
Whether the recommendation is for a current-generation instance.

SizeFlexEligible (boolean) --
Whether the recommended reservation is size flexible.



RedshiftInstanceDetails (dict) --
The Amazon Redshift instances that AWS recommends that you purchase.

Family (string) --
The instance family of the recommended reservation.

NodeType (string) --
The type of node that AWS recommends.

Region (string) --
The AWS Region of the recommended reservation.

CurrentGeneration (boolean) --
Whether the recommendation is for a current-generation instance.

SizeFlexEligible (boolean) --
Whether the recommended reservation is size flexible.



ElastiCacheInstanceDetails (dict) --
The ElastiCache instances that AWS recommends that you purchase.

Family (string) --
The instance family of the recommended reservation.

NodeType (string) --
The type of node that AWS recommends.

Region (string) --
The AWS Region of the recommended reservation.

ProductDescription (string) --
The description of the recommended reservation.

CurrentGeneration (boolean) --
Whether the recommendation is for a current generation instance.

SizeFlexEligible (boolean) --
Whether the recommended reservation is size flexible.



ESInstanceDetails (dict) --
The Amazon ES instances that AWS recommends that you purchase.

InstanceClass (string) --
The class of instance that AWS recommends.

InstanceSize (string) --
The size of instance that AWS recommends.

Region (string) --
The AWS Region of the recommended reservation.

CurrentGeneration (boolean) --
Whether the recommendation is for a current-generation instance.

SizeFlexEligible (boolean) --
Whether the recommended reservation is size flexible.





RecommendedNumberOfInstancesToPurchase (string) --
The number of instances that AWS recommends that you purchase.

RecommendedNormalizedUnitsToPurchase (string) --
The number of normalized units that AWS recommends that you purchase.

MinimumNumberOfInstancesUsedPerHour (string) --
The minimum number of instances that you used in an hour during the historical period. AWS uses this to calculate your recommended reservation purchases.

MinimumNormalizedUnitsUsedPerHour (string) --
The minimum number of normalized units that you used in an hour during the historical period. AWS uses this to calculate your recommended reservation purchases.

MaximumNumberOfInstancesUsedPerHour (string) --
The maximum number of instances that you used in an hour during the historical period. AWS uses this to calculate your recommended reservation purchases.

MaximumNormalizedUnitsUsedPerHour (string) --
The maximum number of normalized units that you used in an hour during the historical period. AWS uses this to calculate your recommended reservation purchases.

AverageNumberOfInstancesUsedPerHour (string) --
The average number of instances that you used in an hour during the historical period. AWS uses this to calculate your recommended reservation purchases.

AverageNormalizedUnitsUsedPerHour (string) --
The average number of normalized units that you used in an hour during the historical period. AWS uses this to calculate your recommended reservation purchases.

AverageUtilization (string) --
The average utilization of your instances. AWS uses this to calculate your recommended reservation purchases.

EstimatedBreakEvenInMonths (string) --
How long AWS estimates that it takes for this instance to start saving you money, in months.

CurrencyCode (string) --
The currency code that AWS used to calculate the costs for this instance.

EstimatedMonthlySavingsAmount (string) --
How much AWS estimates that this specific recommendation could save you in a month.

EstimatedMonthlySavingsPercentage (string) --
How much AWS estimates that this specific recommendation could save you in a month, as a percentage of your overall costs.

EstimatedMonthlyOnDemandCost (string) --
How much AWS estimates that you spend on On-Demand Instances in a month.

EstimatedReservationCostForLookbackPeriod (string) --
How much AWS estimates that you would have spent for all usage during the specified historical period if you had a reservation.

UpfrontCost (string) --
How much purchasing this instance costs you upfront.

RecurringStandardMonthlyCost (string) --
How much purchasing this instance costs you on a monthly basis.





RecommendationSummary (dict) --
A summary about the recommended purchase.

TotalEstimatedMonthlySavingsAmount (string) --
The total amount that AWS estimates that this recommendation could save you in a month.

TotalEstimatedMonthlySavingsPercentage (string) --
The total amount that AWS estimates that this recommendation could save you in a month, as a percentage of your costs.

CurrencyCode (string) --
The currency code used for this recommendation.







NextPageToken (string) --
The pagination token for the next set of retrievable results.







Exceptions

CostExplorer.Client.exceptions.LimitExceededException
CostExplorer.Client.exceptions.DataUnavailableException
CostExplorer.Client.exceptions.InvalidNextTokenException


    :return: {
        'Metadata': {
            'RecommendationId': 'string',
            'GenerationTimestamp': 'string'
        },
        'Recommendations': [
            {
                'AccountScope': 'PAYER'|'LINKED',
                'LookbackPeriodInDays': 'SEVEN_DAYS'|'THIRTY_DAYS'|'SIXTY_DAYS',
                'TermInYears': 'ONE_YEAR'|'THREE_YEARS',
                'PaymentOption': 'NO_UPFRONT'|'PARTIAL_UPFRONT'|'ALL_UPFRONT'|'LIGHT_UTILIZATION'|'MEDIUM_UTILIZATION'|'HEAVY_UTILIZATION',
                'ServiceSpecification': {
                    'EC2Specification': {
                        'OfferingClass': 'STANDARD'|'CONVERTIBLE'
                    }
                },
                'RecommendationDetails': [
                    {
                        'AccountId': 'string',
                        'InstanceDetails': {
                            'EC2InstanceDetails': {
                                'Family': 'string',
                                'InstanceType': 'string',
                                'Region': 'string',
                                'AvailabilityZone': 'string',
                                'Platform': 'string',
                                'Tenancy': 'string',
                                'CurrentGeneration': True|False,
                                'SizeFlexEligible': True|False
                            },
                            'RDSInstanceDetails': {
                                'Family': 'string',
                                'InstanceType': 'string',
                                'Region': 'string',
                                'DatabaseEngine': 'string',
                                'DatabaseEdition': 'string',
                                'DeploymentOption': 'string',
                                'LicenseModel': 'string',
                                'CurrentGeneration': True|False,
                                'SizeFlexEligible': True|False
                            },
                            'RedshiftInstanceDetails': {
                                'Family': 'string',
                                'NodeType': 'string',
                                'Region': 'string',
                                'CurrentGeneration': True|False,
                                'SizeFlexEligible': True|False
                            },
                            'ElastiCacheInstanceDetails': {
                                'Family': 'string',
                                'NodeType': 'string',
                                'Region': 'string',
                                'ProductDescription': 'string',
                                'CurrentGeneration': True|False,
                                'SizeFlexEligible': True|False
                            },
                            'ESInstanceDetails': {
                                'InstanceClass': 'string',
                                'InstanceSize': 'string',
                                'Region': 'string',
                                'CurrentGeneration': True|False,
                                'SizeFlexEligible': True|False
                            }
                        },
                        'RecommendedNumberOfInstancesToPurchase': 'string',
                        'RecommendedNormalizedUnitsToPurchase': 'string',
                        'MinimumNumberOfInstancesUsedPerHour': 'string',
                        'MinimumNormalizedUnitsUsedPerHour': 'string',
                        'MaximumNumberOfInstancesUsedPerHour': 'string',
                        'MaximumNormalizedUnitsUsedPerHour': 'string',
                        'AverageNumberOfInstancesUsedPerHour': 'string',
                        'AverageNormalizedUnitsUsedPerHour': 'string',
                        'AverageUtilization': 'string',
                        'EstimatedBreakEvenInMonths': 'string',
                        'CurrencyCode': 'string',
                        'EstimatedMonthlySavingsAmount': 'string',
                        'EstimatedMonthlySavingsPercentage': 'string',
                        'EstimatedMonthlyOnDemandCost': 'string',
                        'EstimatedReservationCostForLookbackPeriod': 'string',
                        'UpfrontCost': 'string',
                        'RecurringStandardMonthlyCost': 'string'
                    },
                ],
                'RecommendationSummary': {
                    'TotalEstimatedMonthlySavingsAmount': 'string',
                    'TotalEstimatedMonthlySavingsPercentage': 'string',
                    'CurrencyCode': 'string'
                }
            },
        ],
        'NextPageToken': 'string'
    }
    
    
    :returns: 
    CostExplorer.Client.exceptions.LimitExceededException
    CostExplorer.Client.exceptions.DataUnavailableException
    CostExplorer.Client.exceptions.InvalidNextTokenException
    
    """
    pass

def get_reservation_utilization(TimePeriod=None, GroupBy=None, Granularity=None, Filter=None, NextPageToken=None):
    """
    Retrieves the reservation utilization for your account. Master accounts in an organization have access to member accounts. You can filter data by dimensions in a time period. You can use GetDimensionValues to determine the possible dimension values. Currently, you can group only by SUBSCRIPTION_ID .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_reservation_utilization(
        TimePeriod={
            'Start': 'string',
            'End': 'string'
        },
        GroupBy=[
            {
                'Type': 'DIMENSION'|'TAG'|'COST_CATEGORY',
                'Key': 'string'
            },
        ],
        Granularity='DAILY'|'MONTHLY'|'HOURLY',
        Filter={
            'Or': [
                {'... recursive ...'},
            ],
            'And': [
                {'... recursive ...'},
            ],
            'Not': {'... recursive ...'},
            'Dimensions': {
                'Key': 'AZ'|'INSTANCE_TYPE'|'LINKED_ACCOUNT'|'LINKED_ACCOUNT_NAME'|'OPERATION'|'PURCHASE_TYPE'|'REGION'|'SERVICE'|'SERVICE_CODE'|'USAGE_TYPE'|'USAGE_TYPE_GROUP'|'RECORD_TYPE'|'OPERATING_SYSTEM'|'TENANCY'|'SCOPE'|'PLATFORM'|'SUBSCRIPTION_ID'|'LEGAL_ENTITY_NAME'|'DEPLOYMENT_OPTION'|'DATABASE_ENGINE'|'CACHE_ENGINE'|'INSTANCE_TYPE_FAMILY'|'BILLING_ENTITY'|'RESERVATION_ID'|'RESOURCE_ID'|'RIGHTSIZING_TYPE'|'SAVINGS_PLANS_TYPE'|'SAVINGS_PLAN_ARN'|'PAYMENT_OPTION',
                'Values': [
                    'string',
                ],
                'MatchOptions': [
                    'EQUALS'|'STARTS_WITH'|'ENDS_WITH'|'CONTAINS'|'CASE_SENSITIVE'|'CASE_INSENSITIVE',
                ]
            },
            'Tags': {
                'Key': 'string',
                'Values': [
                    'string',
                ],
                'MatchOptions': [
                    'EQUALS'|'STARTS_WITH'|'ENDS_WITH'|'CONTAINS'|'CASE_SENSITIVE'|'CASE_INSENSITIVE',
                ]
            },
            'CostCategories': {
                'Key': 'string',
                'Values': [
                    'string',
                ]
            }
        },
        NextPageToken='string'
    )
    
    
    :type TimePeriod: dict
    :param TimePeriod: [REQUIRED]\nSets the start and end dates for retrieving RI utilization. The start date is inclusive, but the end date is exclusive. For example, if start is 2017-01-01 and end is 2017-05-01 , then the cost and usage data is retrieved from 2017-01-01 up to and including 2017-04-30 but not including 2017-05-01 .\n\nStart (string) -- [REQUIRED]The beginning of the time period that you want the usage and costs for. The start date is inclusive. For example, if start is 2017-01-01 , AWS retrieves cost and usage data starting at 2017-01-01 up to the end date.\n\nEnd (string) -- [REQUIRED]The end of the time period that you want the usage and costs for. The end date is exclusive. For example, if end is 2017-05-01 , AWS retrieves cost and usage data from the start date up to, but not including, 2017-05-01 .\n\n\n

    :type GroupBy: list
    :param GroupBy: Groups only by SUBSCRIPTION_ID . Metadata is included.\n\n(dict) --Represents a group when you specify a group by criteria or in the response to a query with a specific grouping.\n\nType (string) --The string that represents the type of group.\n\nKey (string) --The string that represents a key for a specified group.\n\n\n\n\n

    :type Granularity: string
    :param Granularity: If GroupBy is set, Granularity can\'t be set. If Granularity isn\'t set, the response object doesn\'t include Granularity , either MONTHLY or DAILY . If both GroupBy and Granularity aren\'t set, GetReservationUtilization defaults to DAILY .\nThe GetReservationUtilization operation supports only DAILY and MONTHLY granularities.\n

    :type Filter: dict
    :param Filter: Filters utilization data by dimensions. You can filter by the following dimensions:\n\nAZ\nCACHE_ENGINE\nDEPLOYMENT_OPTION\nINSTANCE_TYPE\nLINKED_ACCOUNT\nOPERATING_SYSTEM\nPLATFORM\nREGION\nSERVICE\nSCOPE\nTENANCY\n\n\nGetReservationUtilization uses the same Expression object as the other operations, but only AND is supported among each dimension, and nesting is supported up to only one level deep. If there are multiple values for a dimension, they are OR\'d together.\n\nOr (list) --Return results that match either Dimension object.\n\n(dict) --Use Expression to filter by cost or by usage. There are two patterns:\n\nSimple dimension values - You can set the dimension name and values for the filters that you plan to use. For example, you can filter for REGION==us-east-1 OR REGION==us-west-1 . The Expression for that looks like this: { 'Dimensions': { 'Key': 'REGION', 'Values': [ 'us-east-1', \xe2\x80\x9cus-west-1\xe2\x80\x9d ] } }  The list of dimension values are OR\'d together to retrieve cost or usage data. You can create Expression and DimensionValues objects using either with* methods or set* methods in multiple lines.\nCompound dimension values with logical operations - You can use multiple Expression types and the logical operators AND/OR/NOT to create a list of one or more Expression objects. This allows you to filter on more advanced options. For example, you can filter on ((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE != DataTransfer) . The Expression for that looks like this: { 'And': [ {'Or': [ {'Dimensions': { 'Key': 'REGION', 'Values': [ 'us-east-1', 'us-west-1' ] }}, {'Tags': { 'Key': 'TagName', 'Values': ['Value1'] } } ]}, {'Not': {'Dimensions': { 'Key': 'USAGE_TYPE', 'Values': ['DataTransfer'] }}} ] }\n\n\nNote\n\nBecause each Expression can have only one operator, the service returns an error if more than one is specified. The following example shows an Expression object that creates an error.\n{ 'And': [ ... ], 'DimensionValues': { 'Dimension': 'USAGE_TYPE', 'Values': [ 'DataTransfer' ] } }\n\n\nNote\nFor GetRightsizingRecommendation action, a combination of OR and NOT is not supported. OR is not supported between different dimensions, or dimensions and tags. NOT operators aren\'t supported. Dimensions are also limited to LINKED_ACCOUNT , REGION , or RIGHTSIZING_TYPE .\n\n\n\n\nAnd (list) --Return results that match both Dimension objects.\n\n(dict) --Use Expression to filter by cost or by usage. There are two patterns:\n\nSimple dimension values - You can set the dimension name and values for the filters that you plan to use. For example, you can filter for REGION==us-east-1 OR REGION==us-west-1 . The Expression for that looks like this: { 'Dimensions': { 'Key': 'REGION', 'Values': [ 'us-east-1', \xe2\x80\x9cus-west-1\xe2\x80\x9d ] } }  The list of dimension values are OR\'d together to retrieve cost or usage data. You can create Expression and DimensionValues objects using either with* methods or set* methods in multiple lines.\nCompound dimension values with logical operations - You can use multiple Expression types and the logical operators AND/OR/NOT to create a list of one or more Expression objects. This allows you to filter on more advanced options. For example, you can filter on ((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE != DataTransfer) . The Expression for that looks like this: { 'And': [ {'Or': [ {'Dimensions': { 'Key': 'REGION', 'Values': [ 'us-east-1', 'us-west-1' ] }}, {'Tags': { 'Key': 'TagName', 'Values': ['Value1'] } } ]}, {'Not': {'Dimensions': { 'Key': 'USAGE_TYPE', 'Values': ['DataTransfer'] }}} ] }\n\n\nNote\n\nBecause each Expression can have only one operator, the service returns an error if more than one is specified. The following example shows an Expression object that creates an error.\n{ 'And': [ ... ], 'DimensionValues': { 'Dimension': 'USAGE_TYPE', 'Values': [ 'DataTransfer' ] } }\n\n\nNote\nFor GetRightsizingRecommendation action, a combination of OR and NOT is not supported. OR is not supported between different dimensions, or dimensions and tags. NOT operators aren\'t supported. Dimensions are also limited to LINKED_ACCOUNT , REGION , or RIGHTSIZING_TYPE .\n\n\n\n\nNot (dict) --Return results that don\'t match a Dimension object.\n\nDimensions (dict) --The specific Dimension to use for Expression .\n\nKey (string) --The names of the metadata types that you can use to filter and group your results. For example, AZ returns a list of Availability Zones.\n\nValues (list) --The metadata values that you can use to filter and group your results. You can use GetDimensionValues to find specific values.\n\n(string) --\n\n\nMatchOptions (list) --The match options that you can use to filter your results. MatchOptions is only applicable for actions related to Cost Category. The default values for MatchOptions is EQUALS and CASE_SENSITIVE .\n\n(string) --\n\n\n\n\nTags (dict) --The specific Tag to use for Expression .\n\nKey (string) --The key for the tag.\n\nValues (list) --The specific value of the tag.\n\n(string) --\n\n\nMatchOptions (list) --The match options that you can use to filter your results. MatchOptions is only applicable for only applicable for actions related to Cost Category. The default values for MatchOptions is EQUALS and CASE_SENSITIVE .\n\n(string) --\n\n\n\n\nCostCategories (dict) --The filter based on CostCategory values.\n\nKey (string) --The unique name of the Cost Category.\n\nValues (list) --The specific value of the Cost Category.\n\n(string) --\n\n\n\n\n\n

    :type NextPageToken: string
    :param NextPageToken: The token to retrieve the next set of results. AWS provides the token when the response from a previous call has more results than the maximum page size.

    :rtype: dict

ReturnsResponse Syntax
{
    'UtilizationsByTime': [
        {
            'TimePeriod': {
                'Start': 'string',
                'End': 'string'
            },
            'Groups': [
                {
                    'Key': 'string',
                    'Value': 'string',
                    'Attributes': {
                        'string': 'string'
                    },
                    'Utilization': {
                        'UtilizationPercentage': 'string',
                        'UtilizationPercentageInUnits': 'string',
                        'PurchasedHours': 'string',
                        'PurchasedUnits': 'string',
                        'TotalActualHours': 'string',
                        'TotalActualUnits': 'string',
                        'UnusedHours': 'string',
                        'UnusedUnits': 'string',
                        'OnDemandCostOfRIHoursUsed': 'string',
                        'NetRISavings': 'string',
                        'TotalPotentialRISavings': 'string',
                        'AmortizedUpfrontFee': 'string',
                        'AmortizedRecurringFee': 'string',
                        'TotalAmortizedFee': 'string'
                    }
                },
            ],
            'Total': {
                'UtilizationPercentage': 'string',
                'UtilizationPercentageInUnits': 'string',
                'PurchasedHours': 'string',
                'PurchasedUnits': 'string',
                'TotalActualHours': 'string',
                'TotalActualUnits': 'string',
                'UnusedHours': 'string',
                'UnusedUnits': 'string',
                'OnDemandCostOfRIHoursUsed': 'string',
                'NetRISavings': 'string',
                'TotalPotentialRISavings': 'string',
                'AmortizedUpfrontFee': 'string',
                'AmortizedRecurringFee': 'string',
                'TotalAmortizedFee': 'string'
            }
        },
    ],
    'Total': {
        'UtilizationPercentage': 'string',
        'UtilizationPercentageInUnits': 'string',
        'PurchasedHours': 'string',
        'PurchasedUnits': 'string',
        'TotalActualHours': 'string',
        'TotalActualUnits': 'string',
        'UnusedHours': 'string',
        'UnusedUnits': 'string',
        'OnDemandCostOfRIHoursUsed': 'string',
        'NetRISavings': 'string',
        'TotalPotentialRISavings': 'string',
        'AmortizedUpfrontFee': 'string',
        'AmortizedRecurringFee': 'string',
        'TotalAmortizedFee': 'string'
    },
    'NextPageToken': 'string'
}


Response Structure

(dict) --

UtilizationsByTime (list) --
The amount of time that you used your RIs.

(dict) --
The amount of utilization, in hours.

TimePeriod (dict) --
The period of time that this utilization was used for.

Start (string) --
The beginning of the time period that you want the usage and costs for. The start date is inclusive. For example, if start is 2017-01-01 , AWS retrieves cost and usage data starting at 2017-01-01 up to the end date.

End (string) --
The end of the time period that you want the usage and costs for. The end date is exclusive. For example, if end is 2017-05-01 , AWS retrieves cost and usage data from the start date up to, but not including, 2017-05-01 .



Groups (list) --
The groups that this utilization result uses.

(dict) --
A group of reservations that share a set of attributes.

Key (string) --
The key for a specific reservation attribute.

Value (string) --
The value of a specific reservation attribute.

Attributes (dict) --
The attributes for this group of reservations.

(string) --
(string) --




Utilization (dict) --
How much you used this group of reservations.

UtilizationPercentage (string) --
The percentage of reservation time that you used.

UtilizationPercentageInUnits (string) --
The percentage of Amazon EC2 reservation time that you used, converted to normalized units. Normalized units are available only for Amazon EC2 usage after November 11, 2017.

PurchasedHours (string) --
How many reservation hours that you purchased.

PurchasedUnits (string) --
How many Amazon EC2 reservation hours that you purchased, converted to normalized units. Normalized units are available only for Amazon EC2 usage after November 11, 2017.

TotalActualHours (string) --
The total number of reservation hours that you used.

TotalActualUnits (string) --
The total number of Amazon EC2 reservation hours that you used, converted to normalized units. Normalized units are available only for Amazon EC2 usage after November 11, 2017.

UnusedHours (string) --
The number of reservation hours that you didn\'t use.

UnusedUnits (string) --
The number of Amazon EC2 reservation hours that you didn\'t use, converted to normalized units. Normalized units are available only for Amazon EC2 usage after November 11, 2017.

OnDemandCostOfRIHoursUsed (string) --
How much your reservation would cost if charged On-Demand rates.

NetRISavings (string) --
How much you saved due to purchasing and utilizing reservation. AWS calculates this by subtracting TotalAmortizedFee from OnDemandCostOfRIHoursUsed .

TotalPotentialRISavings (string) --
How much you could save if you use your entire reservation.

AmortizedUpfrontFee (string) --
The upfront cost of your reservation, amortized over the reservation period.

AmortizedRecurringFee (string) --
The monthly cost of your reservation, amortized over the reservation period.

TotalAmortizedFee (string) --
The total cost of your reservation, amortized over the reservation period.







Total (dict) --
The total number of reservation hours that were used.

UtilizationPercentage (string) --
The percentage of reservation time that you used.

UtilizationPercentageInUnits (string) --
The percentage of Amazon EC2 reservation time that you used, converted to normalized units. Normalized units are available only for Amazon EC2 usage after November 11, 2017.

PurchasedHours (string) --
How many reservation hours that you purchased.

PurchasedUnits (string) --
How many Amazon EC2 reservation hours that you purchased, converted to normalized units. Normalized units are available only for Amazon EC2 usage after November 11, 2017.

TotalActualHours (string) --
The total number of reservation hours that you used.

TotalActualUnits (string) --
The total number of Amazon EC2 reservation hours that you used, converted to normalized units. Normalized units are available only for Amazon EC2 usage after November 11, 2017.

UnusedHours (string) --
The number of reservation hours that you didn\'t use.

UnusedUnits (string) --
The number of Amazon EC2 reservation hours that you didn\'t use, converted to normalized units. Normalized units are available only for Amazon EC2 usage after November 11, 2017.

OnDemandCostOfRIHoursUsed (string) --
How much your reservation would cost if charged On-Demand rates.

NetRISavings (string) --
How much you saved due to purchasing and utilizing reservation. AWS calculates this by subtracting TotalAmortizedFee from OnDemandCostOfRIHoursUsed .

TotalPotentialRISavings (string) --
How much you could save if you use your entire reservation.

AmortizedUpfrontFee (string) --
The upfront cost of your reservation, amortized over the reservation period.

AmortizedRecurringFee (string) --
The monthly cost of your reservation, amortized over the reservation period.

TotalAmortizedFee (string) --
The total cost of your reservation, amortized over the reservation period.







Total (dict) --
The total amount of time that you used your RIs.

UtilizationPercentage (string) --
The percentage of reservation time that you used.

UtilizationPercentageInUnits (string) --
The percentage of Amazon EC2 reservation time that you used, converted to normalized units. Normalized units are available only for Amazon EC2 usage after November 11, 2017.

PurchasedHours (string) --
How many reservation hours that you purchased.

PurchasedUnits (string) --
How many Amazon EC2 reservation hours that you purchased, converted to normalized units. Normalized units are available only for Amazon EC2 usage after November 11, 2017.

TotalActualHours (string) --
The total number of reservation hours that you used.

TotalActualUnits (string) --
The total number of Amazon EC2 reservation hours that you used, converted to normalized units. Normalized units are available only for Amazon EC2 usage after November 11, 2017.

UnusedHours (string) --
The number of reservation hours that you didn\'t use.

UnusedUnits (string) --
The number of Amazon EC2 reservation hours that you didn\'t use, converted to normalized units. Normalized units are available only for Amazon EC2 usage after November 11, 2017.

OnDemandCostOfRIHoursUsed (string) --
How much your reservation would cost if charged On-Demand rates.

NetRISavings (string) --
How much you saved due to purchasing and utilizing reservation. AWS calculates this by subtracting TotalAmortizedFee from OnDemandCostOfRIHoursUsed .

TotalPotentialRISavings (string) --
How much you could save if you use your entire reservation.

AmortizedUpfrontFee (string) --
The upfront cost of your reservation, amortized over the reservation period.

AmortizedRecurringFee (string) --
The monthly cost of your reservation, amortized over the reservation period.

TotalAmortizedFee (string) --
The total cost of your reservation, amortized over the reservation period.



NextPageToken (string) --
The token for the next set of retrievable results. AWS provides the token when the response from a previous call has more results than the maximum page size.







Exceptions

CostExplorer.Client.exceptions.LimitExceededException
CostExplorer.Client.exceptions.DataUnavailableException
CostExplorer.Client.exceptions.InvalidNextTokenException


    :return: {
        'UtilizationsByTime': [
            {
                'TimePeriod': {
                    'Start': 'string',
                    'End': 'string'
                },
                'Groups': [
                    {
                        'Key': 'string',
                        'Value': 'string',
                        'Attributes': {
                            'string': 'string'
                        },
                        'Utilization': {
                            'UtilizationPercentage': 'string',
                            'UtilizationPercentageInUnits': 'string',
                            'PurchasedHours': 'string',
                            'PurchasedUnits': 'string',
                            'TotalActualHours': 'string',
                            'TotalActualUnits': 'string',
                            'UnusedHours': 'string',
                            'UnusedUnits': 'string',
                            'OnDemandCostOfRIHoursUsed': 'string',
                            'NetRISavings': 'string',
                            'TotalPotentialRISavings': 'string',
                            'AmortizedUpfrontFee': 'string',
                            'AmortizedRecurringFee': 'string',
                            'TotalAmortizedFee': 'string'
                        }
                    },
                ],
                'Total': {
                    'UtilizationPercentage': 'string',
                    'UtilizationPercentageInUnits': 'string',
                    'PurchasedHours': 'string',
                    'PurchasedUnits': 'string',
                    'TotalActualHours': 'string',
                    'TotalActualUnits': 'string',
                    'UnusedHours': 'string',
                    'UnusedUnits': 'string',
                    'OnDemandCostOfRIHoursUsed': 'string',
                    'NetRISavings': 'string',
                    'TotalPotentialRISavings': 'string',
                    'AmortizedUpfrontFee': 'string',
                    'AmortizedRecurringFee': 'string',
                    'TotalAmortizedFee': 'string'
                }
            },
        ],
        'Total': {
            'UtilizationPercentage': 'string',
            'UtilizationPercentageInUnits': 'string',
            'PurchasedHours': 'string',
            'PurchasedUnits': 'string',
            'TotalActualHours': 'string',
            'TotalActualUnits': 'string',
            'UnusedHours': 'string',
            'UnusedUnits': 'string',
            'OnDemandCostOfRIHoursUsed': 'string',
            'NetRISavings': 'string',
            'TotalPotentialRISavings': 'string',
            'AmortizedUpfrontFee': 'string',
            'AmortizedRecurringFee': 'string',
            'TotalAmortizedFee': 'string'
        },
        'NextPageToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def get_rightsizing_recommendation(Filter=None, Configuration=None, Service=None, PageSize=None, NextPageToken=None):
    """
    Creates recommendations that helps you save cost by identifying idle and underutilized Amazon EC2 instances.
    Recommendations are generated to either downsize or terminate instances, along with providing savings detail and metrics. For details on calculation and function, see Optimizing Your Cost with Rightsizing Recommendations .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_rightsizing_recommendation(
        Filter={
            'Or': [
                {'... recursive ...'},
            ],
            'And': [
                {'... recursive ...'},
            ],
            'Not': {'... recursive ...'},
            'Dimensions': {
                'Key': 'AZ'|'INSTANCE_TYPE'|'LINKED_ACCOUNT'|'LINKED_ACCOUNT_NAME'|'OPERATION'|'PURCHASE_TYPE'|'REGION'|'SERVICE'|'SERVICE_CODE'|'USAGE_TYPE'|'USAGE_TYPE_GROUP'|'RECORD_TYPE'|'OPERATING_SYSTEM'|'TENANCY'|'SCOPE'|'PLATFORM'|'SUBSCRIPTION_ID'|'LEGAL_ENTITY_NAME'|'DEPLOYMENT_OPTION'|'DATABASE_ENGINE'|'CACHE_ENGINE'|'INSTANCE_TYPE_FAMILY'|'BILLING_ENTITY'|'RESERVATION_ID'|'RESOURCE_ID'|'RIGHTSIZING_TYPE'|'SAVINGS_PLANS_TYPE'|'SAVINGS_PLAN_ARN'|'PAYMENT_OPTION',
                'Values': [
                    'string',
                ],
                'MatchOptions': [
                    'EQUALS'|'STARTS_WITH'|'ENDS_WITH'|'CONTAINS'|'CASE_SENSITIVE'|'CASE_INSENSITIVE',
                ]
            },
            'Tags': {
                'Key': 'string',
                'Values': [
                    'string',
                ],
                'MatchOptions': [
                    'EQUALS'|'STARTS_WITH'|'ENDS_WITH'|'CONTAINS'|'CASE_SENSITIVE'|'CASE_INSENSITIVE',
                ]
            },
            'CostCategories': {
                'Key': 'string',
                'Values': [
                    'string',
                ]
            }
        },
        Configuration={
            'RecommendationTarget': 'SAME_INSTANCE_FAMILY'|'CROSS_INSTANCE_FAMILY',
            'BenefitsConsidered': True|False
        },
        Service='string',
        PageSize=123,
        NextPageToken='string'
    )
    
    
    :type Filter: dict
    :param Filter: Use Expression to filter by cost or by usage. There are two patterns:\n\nSimple dimension values - You can set the dimension name and values for the filters that you plan to use. For example, you can filter for REGION==us-east-1 OR REGION==us-west-1 . The Expression for that looks like this: { 'Dimensions': { 'Key': 'REGION', 'Values': [ 'us-east-1', \xe2\x80\x9cus-west-1\xe2\x80\x9d ] } }  The list of dimension values are OR\'d together to retrieve cost or usage data. You can create Expression and DimensionValues objects using either with* methods or set* methods in multiple lines.\nCompound dimension values with logical operations - You can use multiple Expression types and the logical operators AND/OR/NOT to create a list of one or more Expression objects. This allows you to filter on more advanced options. For example, you can filter on ((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE != DataTransfer) . The Expression for that looks like this: { 'And': [ {'Or': [ {'Dimensions': { 'Key': 'REGION', 'Values': [ 'us-east-1', 'us-west-1' ] }}, {'Tags': { 'Key': 'TagName', 'Values': ['Value1'] } } ]}, {'Not': {'Dimensions': { 'Key': 'USAGE_TYPE', 'Values': ['DataTransfer'] }}} ] }\n\n\nNote\n\nBecause each Expression can have only one operator, the service returns an error if more than one is specified. The following example shows an Expression object that creates an error.\n{ 'And': [ ... ], 'DimensionValues': { 'Dimension': 'USAGE_TYPE', 'Values': [ 'DataTransfer' ] } }\n\n\nNote\nFor GetRightsizingRecommendation action, a combination of OR and NOT is not supported. OR is not supported between different dimensions, or dimensions and tags. NOT operators aren\'t supported. Dimensions are also limited to LINKED_ACCOUNT , REGION , or RIGHTSIZING_TYPE .\n\n\nOr (list) --Return results that match either Dimension object.\n\n(dict) --Use Expression to filter by cost or by usage. There are two patterns:\n\nSimple dimension values - You can set the dimension name and values for the filters that you plan to use. For example, you can filter for REGION==us-east-1 OR REGION==us-west-1 . The Expression for that looks like this: { 'Dimensions': { 'Key': 'REGION', 'Values': [ 'us-east-1', \xe2\x80\x9cus-west-1\xe2\x80\x9d ] } }  The list of dimension values are OR\'d together to retrieve cost or usage data. You can create Expression and DimensionValues objects using either with* methods or set* methods in multiple lines.\nCompound dimension values with logical operations - You can use multiple Expression types and the logical operators AND/OR/NOT to create a list of one or more Expression objects. This allows you to filter on more advanced options. For example, you can filter on ((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE != DataTransfer) . The Expression for that looks like this: { 'And': [ {'Or': [ {'Dimensions': { 'Key': 'REGION', 'Values': [ 'us-east-1', 'us-west-1' ] }}, {'Tags': { 'Key': 'TagName', 'Values': ['Value1'] } } ]}, {'Not': {'Dimensions': { 'Key': 'USAGE_TYPE', 'Values': ['DataTransfer'] }}} ] }\n\n\nNote\n\nBecause each Expression can have only one operator, the service returns an error if more than one is specified. The following example shows an Expression object that creates an error.\n{ 'And': [ ... ], 'DimensionValues': { 'Dimension': 'USAGE_TYPE', 'Values': [ 'DataTransfer' ] } }\n\n\nNote\nFor GetRightsizingRecommendation action, a combination of OR and NOT is not supported. OR is not supported between different dimensions, or dimensions and tags. NOT operators aren\'t supported. Dimensions are also limited to LINKED_ACCOUNT , REGION , or RIGHTSIZING_TYPE .\n\n\n\n\nAnd (list) --Return results that match both Dimension objects.\n\n(dict) --Use Expression to filter by cost or by usage. There are two patterns:\n\nSimple dimension values - You can set the dimension name and values for the filters that you plan to use. For example, you can filter for REGION==us-east-1 OR REGION==us-west-1 . The Expression for that looks like this: { 'Dimensions': { 'Key': 'REGION', 'Values': [ 'us-east-1', \xe2\x80\x9cus-west-1\xe2\x80\x9d ] } }  The list of dimension values are OR\'d together to retrieve cost or usage data. You can create Expression and DimensionValues objects using either with* methods or set* methods in multiple lines.\nCompound dimension values with logical operations - You can use multiple Expression types and the logical operators AND/OR/NOT to create a list of one or more Expression objects. This allows you to filter on more advanced options. For example, you can filter on ((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE != DataTransfer) . The Expression for that looks like this: { 'And': [ {'Or': [ {'Dimensions': { 'Key': 'REGION', 'Values': [ 'us-east-1', 'us-west-1' ] }}, {'Tags': { 'Key': 'TagName', 'Values': ['Value1'] } } ]}, {'Not': {'Dimensions': { 'Key': 'USAGE_TYPE', 'Values': ['DataTransfer'] }}} ] }\n\n\nNote\n\nBecause each Expression can have only one operator, the service returns an error if more than one is specified. The following example shows an Expression object that creates an error.\n{ 'And': [ ... ], 'DimensionValues': { 'Dimension': 'USAGE_TYPE', 'Values': [ 'DataTransfer' ] } }\n\n\nNote\nFor GetRightsizingRecommendation action, a combination of OR and NOT is not supported. OR is not supported between different dimensions, or dimensions and tags. NOT operators aren\'t supported. Dimensions are also limited to LINKED_ACCOUNT , REGION , or RIGHTSIZING_TYPE .\n\n\n\n\nNot (dict) --Return results that don\'t match a Dimension object.\n\nDimensions (dict) --The specific Dimension to use for Expression .\n\nKey (string) --The names of the metadata types that you can use to filter and group your results. For example, AZ returns a list of Availability Zones.\n\nValues (list) --The metadata values that you can use to filter and group your results. You can use GetDimensionValues to find specific values.\n\n(string) --\n\n\nMatchOptions (list) --The match options that you can use to filter your results. MatchOptions is only applicable for actions related to Cost Category. The default values for MatchOptions is EQUALS and CASE_SENSITIVE .\n\n(string) --\n\n\n\n\nTags (dict) --The specific Tag to use for Expression .\n\nKey (string) --The key for the tag.\n\nValues (list) --The specific value of the tag.\n\n(string) --\n\n\nMatchOptions (list) --The match options that you can use to filter your results. MatchOptions is only applicable for only applicable for actions related to Cost Category. The default values for MatchOptions is EQUALS and CASE_SENSITIVE .\n\n(string) --\n\n\n\n\nCostCategories (dict) --The filter based on CostCategory values.\n\nKey (string) --The unique name of the Cost Category.\n\nValues (list) --The specific value of the Cost Category.\n\n(string) --\n\n\n\n\n\n

    :type Configuration: dict
    :param Configuration: Enables you to customize recommendations across two attributes. You can choose to view recommendations for instances within the same instance families or across different instance families. You can also choose to view your estimated savings associated with recommendations with consideration of existing Savings Plans or RI benefits, or niether.\n\nRecommendationTarget (string) -- [REQUIRED]The option to see recommendations within the same instance family, or recommendations for instances across other families. The default value is SAME_INSTANCE_FAMILY .\n\nBenefitsConsidered (boolean) -- [REQUIRED]The option to consider RI or Savings Plans discount benefits in your savings calculation. The default value is TRUE .\n\n\n

    :type Service: string
    :param Service: [REQUIRED]\nThe specific service that you want recommendations for. The only valid value for GetRightsizingRecommendation is 'AmazonEC2 '.\n

    :type PageSize: integer
    :param PageSize: The number of recommendations that you want returned in a single response object.

    :type NextPageToken: string
    :param NextPageToken: The pagination token that indicates the next set of results that you want to retrieve.

    :rtype: dict

ReturnsResponse Syntax
{
    'Metadata': {
        'RecommendationId': 'string',
        'GenerationTimestamp': 'string',
        'LookbackPeriodInDays': 'SEVEN_DAYS'|'THIRTY_DAYS'|'SIXTY_DAYS'
    },
    'Summary': {
        'TotalRecommendationCount': 'string',
        'EstimatedTotalMonthlySavingsAmount': 'string',
        'SavingsCurrencyCode': 'string',
        'SavingsPercentage': 'string'
    },
    'RightsizingRecommendations': [
        {
            'AccountId': 'string',
            'CurrentInstance': {
                'ResourceId': 'string',
                'Tags': [
                    {
                        'Key': 'string',
                        'Values': [
                            'string',
                        ],
                        'MatchOptions': [
                            'EQUALS'|'STARTS_WITH'|'ENDS_WITH'|'CONTAINS'|'CASE_SENSITIVE'|'CASE_INSENSITIVE',
                        ]
                    },
                ],
                'ResourceDetails': {
                    'EC2ResourceDetails': {
                        'HourlyOnDemandRate': 'string',
                        'InstanceType': 'string',
                        'Platform': 'string',
                        'Region': 'string',
                        'Sku': 'string',
                        'Memory': 'string',
                        'NetworkPerformance': 'string',
                        'Storage': 'string',
                        'Vcpu': 'string'
                    }
                },
                'ResourceUtilization': {
                    'EC2ResourceUtilization': {
                        'MaxCpuUtilizationPercentage': 'string',
                        'MaxMemoryUtilizationPercentage': 'string',
                        'MaxStorageUtilizationPercentage': 'string'
                    }
                },
                'ReservationCoveredHoursInLookbackPeriod': 'string',
                'SavingsPlansCoveredHoursInLookbackPeriod': 'string',
                'OnDemandHoursInLookbackPeriod': 'string',
                'TotalRunningHoursInLookbackPeriod': 'string',
                'MonthlyCost': 'string',
                'CurrencyCode': 'string'
            },
            'RightsizingType': 'TERMINATE'|'MODIFY',
            'ModifyRecommendationDetail': {
                'TargetInstances': [
                    {
                        'EstimatedMonthlyCost': 'string',
                        'EstimatedMonthlySavings': 'string',
                        'CurrencyCode': 'string',
                        'DefaultTargetInstance': True|False,
                        'ResourceDetails': {
                            'EC2ResourceDetails': {
                                'HourlyOnDemandRate': 'string',
                                'InstanceType': 'string',
                                'Platform': 'string',
                                'Region': 'string',
                                'Sku': 'string',
                                'Memory': 'string',
                                'NetworkPerformance': 'string',
                                'Storage': 'string',
                                'Vcpu': 'string'
                            }
                        },
                        'ExpectedResourceUtilization': {
                            'EC2ResourceUtilization': {
                                'MaxCpuUtilizationPercentage': 'string',
                                'MaxMemoryUtilizationPercentage': 'string',
                                'MaxStorageUtilizationPercentage': 'string'
                            }
                        }
                    },
                ]
            },
            'TerminateRecommendationDetail': {
                'EstimatedMonthlySavings': 'string',
                'CurrencyCode': 'string'
            }
        },
    ],
    'NextPageToken': 'string',
    'Configuration': {
        'RecommendationTarget': 'SAME_INSTANCE_FAMILY'|'CROSS_INSTANCE_FAMILY',
        'BenefitsConsidered': True|False
    }
}


Response Structure

(dict) --

Metadata (dict) --
Information regarding this specific recommendation set.

RecommendationId (string) --
The ID for this specific recommendation.

GenerationTimestamp (string) --
The time stamp for when Amazon Web Services made this recommendation.

LookbackPeriodInDays (string) --
How many days of previous usage that Amazon Web Services considers when making this recommendation.



Summary (dict) --
Summary of this recommendation set.

TotalRecommendationCount (string) --
Total number of instance recommendations.

EstimatedTotalMonthlySavingsAmount (string) --
Estimated total savings resulting from modifications, on a monthly basis.

SavingsCurrencyCode (string) --
The currency code that Amazon Web Services used to calculate the savings.

SavingsPercentage (string) --
Savings percentage based on the recommended modifications, relative to the total On Demand costs associated with these instances.



RightsizingRecommendations (list) --
Recommendations to rightsize resources.

(dict) --
Recommendations to rightsize resources.

AccountId (string) --
The account that this recommendation is for.

CurrentInstance (dict) --
Context regarding the current instance.

ResourceId (string) --
Resource ID of the current instance.

Tags (list) --
Cost allocation resource tags applied to the instance.

(dict) --
The values that are available for a tag.

Key (string) --
The key for the tag.

Values (list) --
The specific value of the tag.

(string) --


MatchOptions (list) --
The match options that you can use to filter your results. MatchOptions is only applicable for only applicable for actions related to Cost Category. The default values for MatchOptions is EQUALS and CASE_SENSITIVE .

(string) --






ResourceDetails (dict) --
Details about the resource and utilization.

EC2ResourceDetails (dict) --
Details on the Amazon EC2 resource.

HourlyOnDemandRate (string) --
Hourly public On Demand rate for the instance type.

InstanceType (string) --
The type of Amazon Web Services instance.

Platform (string) --
The platform of the Amazon Web Services instance. The platform is the specific combination of operating system, license model, and software on an instance.

Region (string) --
The Amazon Web Services Region of the instance.

Sku (string) --
The SKU of the product.

Memory (string) --
Memory capacity of Amazon Web Services instance.

NetworkPerformance (string) --
Network performance capacity of the Amazon Web Services instance.

Storage (string) --
The disk storage of the Amazon Web Services instance (Not EBS storage).

Vcpu (string) --
Number of VCPU cores in the Amazon Web Services instance type.





ResourceUtilization (dict) --
Utilization information of the current instance during the lookback period.

EC2ResourceUtilization (dict) --
Utilization of current Amazon EC2 Instance

MaxCpuUtilizationPercentage (string) --
Maximum observed or expected CPU utilization of the instance.

MaxMemoryUtilizationPercentage (string) --
Maximum observed or expected memory utilization of the instance.

MaxStorageUtilizationPercentage (string) --
Maximum observed or expected storage utilization of the instance (does not measure EBS storage).





ReservationCoveredHoursInLookbackPeriod (string) --
Number of hours during the lookback period covered by reservations.

SavingsPlansCoveredHoursInLookbackPeriod (string) --
Number of hours during the lookback period covered by Savings Plans.

OnDemandHoursInLookbackPeriod (string) --
Number of hours during the lookback period billed at On Demand rates.

TotalRunningHoursInLookbackPeriod (string) --
The total number of hours the instance ran during the lookback period.

MonthlyCost (string) --
Current On Demand cost of operating this instance on a monthly basis.

CurrencyCode (string) --
The currency code that Amazon Web Services used to calculate the costs for this instance.



RightsizingType (string) --
Recommendation to either terminate or modify the resource.

ModifyRecommendationDetail (dict) --
Details for modification recommendations.

TargetInstances (list) --
Identifies whether this instance type is the Amazon Web Services default recommendation.

(dict) --
Details on recommended instance.

EstimatedMonthlyCost (string) --
Expected cost to operate this instance type on a monthly basis.

EstimatedMonthlySavings (string) --
Estimated savings resulting from modification, on a monthly basis.

CurrencyCode (string) --
The currency code that Amazon Web Services used to calculate the costs for this instance.

DefaultTargetInstance (boolean) --
Indicates whether or not this recommendation is the defaulted Amazon Web Services recommendation.

ResourceDetails (dict) --
Details on the target instance type.

EC2ResourceDetails (dict) --
Details on the Amazon EC2 resource.

HourlyOnDemandRate (string) --
Hourly public On Demand rate for the instance type.

InstanceType (string) --
The type of Amazon Web Services instance.

Platform (string) --
The platform of the Amazon Web Services instance. The platform is the specific combination of operating system, license model, and software on an instance.

Region (string) --
The Amazon Web Services Region of the instance.

Sku (string) --
The SKU of the product.

Memory (string) --
Memory capacity of Amazon Web Services instance.

NetworkPerformance (string) --
Network performance capacity of the Amazon Web Services instance.

Storage (string) --
The disk storage of the Amazon Web Services instance (Not EBS storage).

Vcpu (string) --
Number of VCPU cores in the Amazon Web Services instance type.





ExpectedResourceUtilization (dict) --
Expected utilization metrics for target instance type.

EC2ResourceUtilization (dict) --
Utilization of current Amazon EC2 Instance

MaxCpuUtilizationPercentage (string) --
Maximum observed or expected CPU utilization of the instance.

MaxMemoryUtilizationPercentage (string) --
Maximum observed or expected memory utilization of the instance.

MaxStorageUtilizationPercentage (string) --
Maximum observed or expected storage utilization of the instance (does not measure EBS storage).











TerminateRecommendationDetail (dict) --
Details for termination recommendations.

EstimatedMonthlySavings (string) --
Estimated savings resulting from modification, on a monthly basis.

CurrencyCode (string) --
The currency code that Amazon Web Services used to calculate the costs for this instance.







NextPageToken (string) --
The token to retrieve the next set of results.

Configuration (dict) --
Enables you to customize recommendations across two attributes. You can choose to view recommendations for instances within the same instance families or across different instance families. You can also choose to view your estimated savings associated with recommendations with consideration of existing Savings Plans or RI benefits, or niether.

RecommendationTarget (string) --
The option to see recommendations within the same instance family, or recommendations for instances across other families. The default value is SAME_INSTANCE_FAMILY .

BenefitsConsidered (boolean) --
The option to consider RI or Savings Plans discount benefits in your savings calculation. The default value is TRUE .









Exceptions

CostExplorer.Client.exceptions.LimitExceededException
CostExplorer.Client.exceptions.InvalidNextTokenException


    :return: {
        'Metadata': {
            'RecommendationId': 'string',
            'GenerationTimestamp': 'string',
            'LookbackPeriodInDays': 'SEVEN_DAYS'|'THIRTY_DAYS'|'SIXTY_DAYS'
        },
        'Summary': {
            'TotalRecommendationCount': 'string',
            'EstimatedTotalMonthlySavingsAmount': 'string',
            'SavingsCurrencyCode': 'string',
            'SavingsPercentage': 'string'
        },
        'RightsizingRecommendations': [
            {
                'AccountId': 'string',
                'CurrentInstance': {
                    'ResourceId': 'string',
                    'Tags': [
                        {
                            'Key': 'string',
                            'Values': [
                                'string',
                            ],
                            'MatchOptions': [
                                'EQUALS'|'STARTS_WITH'|'ENDS_WITH'|'CONTAINS'|'CASE_SENSITIVE'|'CASE_INSENSITIVE',
                            ]
                        },
                    ],
                    'ResourceDetails': {
                        'EC2ResourceDetails': {
                            'HourlyOnDemandRate': 'string',
                            'InstanceType': 'string',
                            'Platform': 'string',
                            'Region': 'string',
                            'Sku': 'string',
                            'Memory': 'string',
                            'NetworkPerformance': 'string',
                            'Storage': 'string',
                            'Vcpu': 'string'
                        }
                    },
                    'ResourceUtilization': {
                        'EC2ResourceUtilization': {
                            'MaxCpuUtilizationPercentage': 'string',
                            'MaxMemoryUtilizationPercentage': 'string',
                            'MaxStorageUtilizationPercentage': 'string'
                        }
                    },
                    'ReservationCoveredHoursInLookbackPeriod': 'string',
                    'SavingsPlansCoveredHoursInLookbackPeriod': 'string',
                    'OnDemandHoursInLookbackPeriod': 'string',
                    'TotalRunningHoursInLookbackPeriod': 'string',
                    'MonthlyCost': 'string',
                    'CurrencyCode': 'string'
                },
                'RightsizingType': 'TERMINATE'|'MODIFY',
                'ModifyRecommendationDetail': {
                    'TargetInstances': [
                        {
                            'EstimatedMonthlyCost': 'string',
                            'EstimatedMonthlySavings': 'string',
                            'CurrencyCode': 'string',
                            'DefaultTargetInstance': True|False,
                            'ResourceDetails': {
                                'EC2ResourceDetails': {
                                    'HourlyOnDemandRate': 'string',
                                    'InstanceType': 'string',
                                    'Platform': 'string',
                                    'Region': 'string',
                                    'Sku': 'string',
                                    'Memory': 'string',
                                    'NetworkPerformance': 'string',
                                    'Storage': 'string',
                                    'Vcpu': 'string'
                                }
                            },
                            'ExpectedResourceUtilization': {
                                'EC2ResourceUtilization': {
                                    'MaxCpuUtilizationPercentage': 'string',
                                    'MaxMemoryUtilizationPercentage': 'string',
                                    'MaxStorageUtilizationPercentage': 'string'
                                }
                            }
                        },
                    ]
                },
                'TerminateRecommendationDetail': {
                    'EstimatedMonthlySavings': 'string',
                    'CurrencyCode': 'string'
                }
            },
        ],
        'NextPageToken': 'string',
        'Configuration': {
            'RecommendationTarget': 'SAME_INSTANCE_FAMILY'|'CROSS_INSTANCE_FAMILY',
            'BenefitsConsidered': True|False
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_savings_plans_coverage(TimePeriod=None, GroupBy=None, Granularity=None, Filter=None, Metrics=None, NextToken=None, MaxResults=None):
    """
    Retrieves the Savings Plans covered for your account. This enables you to see how much of your cost is covered by a Savings Plan. An organization\xe2\x80\x99s master account can see the coverage of the associated member accounts. This supports dimensions, Cost Categories, and nested expressions. For any time period, you can filter data for Savings Plans usage with the following dimensions:
    To determine valid values for a dimension, use the GetDimensionValues operation.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_savings_plans_coverage(
        TimePeriod={
            'Start': 'string',
            'End': 'string'
        },
        GroupBy=[
            {
                'Type': 'DIMENSION'|'TAG'|'COST_CATEGORY',
                'Key': 'string'
            },
        ],
        Granularity='DAILY'|'MONTHLY'|'HOURLY',
        Filter={
            'Or': [
                {'... recursive ...'},
            ],
            'And': [
                {'... recursive ...'},
            ],
            'Not': {'... recursive ...'},
            'Dimensions': {
                'Key': 'AZ'|'INSTANCE_TYPE'|'LINKED_ACCOUNT'|'LINKED_ACCOUNT_NAME'|'OPERATION'|'PURCHASE_TYPE'|'REGION'|'SERVICE'|'SERVICE_CODE'|'USAGE_TYPE'|'USAGE_TYPE_GROUP'|'RECORD_TYPE'|'OPERATING_SYSTEM'|'TENANCY'|'SCOPE'|'PLATFORM'|'SUBSCRIPTION_ID'|'LEGAL_ENTITY_NAME'|'DEPLOYMENT_OPTION'|'DATABASE_ENGINE'|'CACHE_ENGINE'|'INSTANCE_TYPE_FAMILY'|'BILLING_ENTITY'|'RESERVATION_ID'|'RESOURCE_ID'|'RIGHTSIZING_TYPE'|'SAVINGS_PLANS_TYPE'|'SAVINGS_PLAN_ARN'|'PAYMENT_OPTION',
                'Values': [
                    'string',
                ],
                'MatchOptions': [
                    'EQUALS'|'STARTS_WITH'|'ENDS_WITH'|'CONTAINS'|'CASE_SENSITIVE'|'CASE_INSENSITIVE',
                ]
            },
            'Tags': {
                'Key': 'string',
                'Values': [
                    'string',
                ],
                'MatchOptions': [
                    'EQUALS'|'STARTS_WITH'|'ENDS_WITH'|'CONTAINS'|'CASE_SENSITIVE'|'CASE_INSENSITIVE',
                ]
            },
            'CostCategories': {
                'Key': 'string',
                'Values': [
                    'string',
                ]
            }
        },
        Metrics=[
            'string',
        ],
        NextToken='string',
        MaxResults=123
    )
    
    
    :type TimePeriod: dict
    :param TimePeriod: [REQUIRED]\nThe time period that you want the usage and costs for. The Start date must be within 13 months. The End date must be after the Start date, and before the current date. Future dates can\'t be used as an End date.\n\nStart (string) -- [REQUIRED]The beginning of the time period that you want the usage and costs for. The start date is inclusive. For example, if start is 2017-01-01 , AWS retrieves cost and usage data starting at 2017-01-01 up to the end date.\n\nEnd (string) -- [REQUIRED]The end of the time period that you want the usage and costs for. The end date is exclusive. For example, if end is 2017-05-01 , AWS retrieves cost and usage data from the start date up to, but not including, 2017-05-01 .\n\n\n

    :type GroupBy: list
    :param GroupBy: You can group the data using the attributes INSTANCE_FAMILY , REGION , or SERVICE .\n\n(dict) --Represents a group when you specify a group by criteria or in the response to a query with a specific grouping.\n\nType (string) --The string that represents the type of group.\n\nKey (string) --The string that represents a key for a specified group.\n\n\n\n\n

    :type Granularity: string
    :param Granularity: The granularity of the Amazon Web Services cost data for your Savings Plans. Granularity can\'t be set if GroupBy is set.\nThe GetSavingsPlansCoverage operation supports only DAILY and MONTHLY granularities.\n

    :type Filter: dict
    :param Filter: Filters Savings Plans coverage data by dimensions. You can filter data for Savings Plans usage with the following dimensions:\n\nLINKED_ACCOUNT\nREGION\nSERVICE\nINSTANCE_FAMILY\n\n\nGetSavingsPlansCoverage uses the same Expression object as the other operations, but only AND is supported among each dimension. If there are multiple values for a dimension, they are OR\'d together.\nCost category is also supported.\n\nOr (list) --Return results that match either Dimension object.\n\n(dict) --Use Expression to filter by cost or by usage. There are two patterns:\n\nSimple dimension values - You can set the dimension name and values for the filters that you plan to use. For example, you can filter for REGION==us-east-1 OR REGION==us-west-1 . The Expression for that looks like this: { 'Dimensions': { 'Key': 'REGION', 'Values': [ 'us-east-1', \xe2\x80\x9cus-west-1\xe2\x80\x9d ] } }  The list of dimension values are OR\'d together to retrieve cost or usage data. You can create Expression and DimensionValues objects using either with* methods or set* methods in multiple lines.\nCompound dimension values with logical operations - You can use multiple Expression types and the logical operators AND/OR/NOT to create a list of one or more Expression objects. This allows you to filter on more advanced options. For example, you can filter on ((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE != DataTransfer) . The Expression for that looks like this: { 'And': [ {'Or': [ {'Dimensions': { 'Key': 'REGION', 'Values': [ 'us-east-1', 'us-west-1' ] }}, {'Tags': { 'Key': 'TagName', 'Values': ['Value1'] } } ]}, {'Not': {'Dimensions': { 'Key': 'USAGE_TYPE', 'Values': ['DataTransfer'] }}} ] }\n\n\nNote\n\nBecause each Expression can have only one operator, the service returns an error if more than one is specified. The following example shows an Expression object that creates an error.\n{ 'And': [ ... ], 'DimensionValues': { 'Dimension': 'USAGE_TYPE', 'Values': [ 'DataTransfer' ] } }\n\n\nNote\nFor GetRightsizingRecommendation action, a combination of OR and NOT is not supported. OR is not supported between different dimensions, or dimensions and tags. NOT operators aren\'t supported. Dimensions are also limited to LINKED_ACCOUNT , REGION , or RIGHTSIZING_TYPE .\n\n\n\n\nAnd (list) --Return results that match both Dimension objects.\n\n(dict) --Use Expression to filter by cost or by usage. There are two patterns:\n\nSimple dimension values - You can set the dimension name and values for the filters that you plan to use. For example, you can filter for REGION==us-east-1 OR REGION==us-west-1 . The Expression for that looks like this: { 'Dimensions': { 'Key': 'REGION', 'Values': [ 'us-east-1', \xe2\x80\x9cus-west-1\xe2\x80\x9d ] } }  The list of dimension values are OR\'d together to retrieve cost or usage data. You can create Expression and DimensionValues objects using either with* methods or set* methods in multiple lines.\nCompound dimension values with logical operations - You can use multiple Expression types and the logical operators AND/OR/NOT to create a list of one or more Expression objects. This allows you to filter on more advanced options. For example, you can filter on ((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE != DataTransfer) . The Expression for that looks like this: { 'And': [ {'Or': [ {'Dimensions': { 'Key': 'REGION', 'Values': [ 'us-east-1', 'us-west-1' ] }}, {'Tags': { 'Key': 'TagName', 'Values': ['Value1'] } } ]}, {'Not': {'Dimensions': { 'Key': 'USAGE_TYPE', 'Values': ['DataTransfer'] }}} ] }\n\n\nNote\n\nBecause each Expression can have only one operator, the service returns an error if more than one is specified. The following example shows an Expression object that creates an error.\n{ 'And': [ ... ], 'DimensionValues': { 'Dimension': 'USAGE_TYPE', 'Values': [ 'DataTransfer' ] } }\n\n\nNote\nFor GetRightsizingRecommendation action, a combination of OR and NOT is not supported. OR is not supported between different dimensions, or dimensions and tags. NOT operators aren\'t supported. Dimensions are also limited to LINKED_ACCOUNT , REGION , or RIGHTSIZING_TYPE .\n\n\n\n\nNot (dict) --Return results that don\'t match a Dimension object.\n\nDimensions (dict) --The specific Dimension to use for Expression .\n\nKey (string) --The names of the metadata types that you can use to filter and group your results. For example, AZ returns a list of Availability Zones.\n\nValues (list) --The metadata values that you can use to filter and group your results. You can use GetDimensionValues to find specific values.\n\n(string) --\n\n\nMatchOptions (list) --The match options that you can use to filter your results. MatchOptions is only applicable for actions related to Cost Category. The default values for MatchOptions is EQUALS and CASE_SENSITIVE .\n\n(string) --\n\n\n\n\nTags (dict) --The specific Tag to use for Expression .\n\nKey (string) --The key for the tag.\n\nValues (list) --The specific value of the tag.\n\n(string) --\n\n\nMatchOptions (list) --The match options that you can use to filter your results. MatchOptions is only applicable for only applicable for actions related to Cost Category. The default values for MatchOptions is EQUALS and CASE_SENSITIVE .\n\n(string) --\n\n\n\n\nCostCategories (dict) --The filter based on CostCategory values.\n\nKey (string) --The unique name of the Cost Category.\n\nValues (list) --The specific value of the Cost Category.\n\n(string) --\n\n\n\n\n\n

    :type Metrics: list
    :param Metrics: The measurement that you want your Savings Plans coverage reported in. The only valid value is SpendCoveredBySavingsPlans .\n\n(string) --\n\n

    :type NextToken: string
    :param NextToken: The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size.

    :type MaxResults: integer
    :param MaxResults: The number of items to be returned in a response. The default is 20 , with a minimum value of 1 .

    :rtype: dict

ReturnsResponse Syntax
{
    'SavingsPlansCoverages': [
        {
            'Attributes': {
                'string': 'string'
            },
            'Coverage': {
                'SpendCoveredBySavingsPlans': 'string',
                'OnDemandCost': 'string',
                'TotalCost': 'string',
                'CoveragePercentage': 'string'
            },
            'TimePeriod': {
                'Start': 'string',
                'End': 'string'
            }
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

SavingsPlansCoverages (list) --
The amount of spend that your Savings Plans covered.

(dict) --
The amount of Savings Plans eligible usage that is covered by Savings Plans. All calculations consider the On-Demand equivalent of your Savings Plans usage.

Attributes (dict) --
The attribute that applies to a specific Dimension .

(string) --
(string) --




Coverage (dict) --
The amount of Savings Plans eligible usage that the Savings Plans covered.

SpendCoveredBySavingsPlans (string) --
The amount of your Amazon Web Services usage that is covered by a Savings Plans.

OnDemandCost (string) --
The cost of your Amazon Web Services usage at the public On-Demand rate.

TotalCost (string) --
The total cost of your Amazon Web Services usage, regardless of your purchase option.

CoveragePercentage (string) --
The percentage of your existing Savings Plans covered usage, divided by all of your eligible Savings Plans usage in an account(or set of accounts).



TimePeriod (dict) --
The time period that you want the usage and costs for.

Start (string) --
The beginning of the time period that you want the usage and costs for. The start date is inclusive. For example, if start is 2017-01-01 , AWS retrieves cost and usage data starting at 2017-01-01 up to the end date.

End (string) --
The end of the time period that you want the usage and costs for. The end date is exclusive. For example, if end is 2017-05-01 , AWS retrieves cost and usage data from the start date up to, but not including, 2017-05-01 .







NextToken (string) --
The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size.







Exceptions

CostExplorer.Client.exceptions.LimitExceededException
CostExplorer.Client.exceptions.DataUnavailableException
CostExplorer.Client.exceptions.InvalidNextTokenException


    :return: {
        'SavingsPlansCoverages': [
            {
                'Attributes': {
                    'string': 'string'
                },
                'Coverage': {
                    'SpendCoveredBySavingsPlans': 'string',
                    'OnDemandCost': 'string',
                    'TotalCost': 'string',
                    'CoveragePercentage': 'string'
                },
                'TimePeriod': {
                    'Start': 'string',
                    'End': 'string'
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    TimePeriod (dict) -- [REQUIRED]
    The time period that you want the usage and costs for. The Start date must be within 13 months. The End date must be after the Start date, and before the current date. Future dates can\'t be used as an End date.
    
    Start (string) -- [REQUIRED]The beginning of the time period that you want the usage and costs for. The start date is inclusive. For example, if start is 2017-01-01 , AWS retrieves cost and usage data starting at 2017-01-01 up to the end date.
    
    End (string) -- [REQUIRED]The end of the time period that you want the usage and costs for. The end date is exclusive. For example, if end is 2017-05-01 , AWS retrieves cost and usage data from the start date up to, but not including, 2017-05-01 .
    
    
    
    GroupBy (list) -- You can group the data using the attributes INSTANCE_FAMILY , REGION , or SERVICE .
    
    (dict) --Represents a group when you specify a group by criteria or in the response to a query with a specific grouping.
    
    Type (string) --The string that represents the type of group.
    
    Key (string) --The string that represents a key for a specified group.
    
    
    
    
    
    Granularity (string) -- The granularity of the Amazon Web Services cost data for your Savings Plans. Granularity can\'t be set if GroupBy is set.
    The GetSavingsPlansCoverage operation supports only DAILY and MONTHLY granularities.
    
    Filter (dict) -- Filters Savings Plans coverage data by dimensions. You can filter data for Savings Plans usage with the following dimensions:
    
    LINKED_ACCOUNT
    REGION
    SERVICE
    INSTANCE_FAMILY
    
    
    GetSavingsPlansCoverage uses the same Expression object as the other operations, but only AND is supported among each dimension. If there are multiple values for a dimension, they are OR\'d together.
    Cost category is also supported.
    
    Or (list) --Return results that match either Dimension object.
    
    (dict) --Use Expression to filter by cost or by usage. There are two patterns:
    
    Simple dimension values - You can set the dimension name and values for the filters that you plan to use. For example, you can filter for REGION==us-east-1 OR REGION==us-west-1 . The Expression for that looks like this:  { "Dimensions": { "Key": "REGION", "Values": [ "us-east-1", \xe2\x80\x9cus-west-1\xe2\x80\x9d ] } }   The list of dimension values are OR\'d together to retrieve cost or usage data. You can create Expression and DimensionValues objects using either with* methods or set* methods in multiple lines.
    Compound dimension values with logical operations - You can use multiple Expression types and the logical operators AND/OR/NOT to create a list of one or more Expression objects. This allows you to filter on more advanced options. For example, you can filter on ((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE != DataTransfer) . The Expression for that looks like this:  { "And": [ {"Or": [ {"Dimensions": { "Key": "REGION", "Values": [ "us-east-1", "us-west-1" ] }}, {"Tags": { "Key": "TagName", "Values": ["Value1"] } } ]}, {"Not": {"Dimensions": { "Key": "USAGE_TYPE", "Values": ["DataTransfer"] }}} ] }
    
    
    Note
    
    Because each Expression can have only one operator, the service returns an error if more than one is specified. The following example shows an Expression object that creates an error.
    { "And": [ ... ], "DimensionValues": { "Dimension": "USAGE_TYPE", "Values": [ "DataTransfer" ] } }
    
    
    Note
    For GetRightsizingRecommendation action, a combination of OR and NOT is not supported. OR is not supported between different dimensions, or dimensions and tags. NOT operators aren\'t supported. Dimensions are also limited to LINKED_ACCOUNT , REGION , or RIGHTSIZING_TYPE .
    
    
    
    
    And (list) --Return results that match both Dimension objects.
    
    (dict) --Use Expression to filter by cost or by usage. There are two patterns:
    
    Simple dimension values - You can set the dimension name and values for the filters that you plan to use. For example, you can filter for REGION==us-east-1 OR REGION==us-west-1 . The Expression for that looks like this:  { "Dimensions": { "Key": "REGION", "Values": [ "us-east-1", \xe2\x80\x9cus-west-1\xe2\x80\x9d ] } }   The list of dimension values are OR\'d together to retrieve cost or usage data. You can create Expression and DimensionValues objects using either with* methods or set* methods in multiple lines.
    Compound dimension values with logical operations - You can use multiple Expression types and the logical operators AND/OR/NOT to create a list of one or more Expression objects. This allows you to filter on more advanced options. For example, you can filter on ((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE != DataTransfer) . The Expression for that looks like this:  { "And": [ {"Or": [ {"Dimensions": { "Key": "REGION", "Values": [ "us-east-1", "us-west-1" ] }}, {"Tags": { "Key": "TagName", "Values": ["Value1"] } } ]}, {"Not": {"Dimensions": { "Key": "USAGE_TYPE", "Values": ["DataTransfer"] }}} ] }
    
    
    Note
    
    Because each Expression can have only one operator, the service returns an error if more than one is specified. The following example shows an Expression object that creates an error.
    { "And": [ ... ], "DimensionValues": { "Dimension": "USAGE_TYPE", "Values": [ "DataTransfer" ] } }
    
    
    Note
    For GetRightsizingRecommendation action, a combination of OR and NOT is not supported. OR is not supported between different dimensions, or dimensions and tags. NOT operators aren\'t supported. Dimensions are also limited to LINKED_ACCOUNT , REGION , or RIGHTSIZING_TYPE .
    
    
    
    
    Not (dict) --Return results that don\'t match a Dimension object.
    
    Dimensions (dict) --The specific Dimension to use for Expression .
    
    Key (string) --The names of the metadata types that you can use to filter and group your results. For example, AZ returns a list of Availability Zones.
    
    Values (list) --The metadata values that you can use to filter and group your results. You can use GetDimensionValues to find specific values.
    
    (string) --
    
    
    MatchOptions (list) --The match options that you can use to filter your results. MatchOptions is only applicable for actions related to Cost Category. The default values for MatchOptions is EQUALS and CASE_SENSITIVE .
    
    (string) --
    
    
    
    
    Tags (dict) --The specific Tag to use for Expression .
    
    Key (string) --The key for the tag.
    
    Values (list) --The specific value of the tag.
    
    (string) --
    
    
    MatchOptions (list) --The match options that you can use to filter your results. MatchOptions is only applicable for only applicable for actions related to Cost Category. The default values for MatchOptions is EQUALS and CASE_SENSITIVE .
    
    (string) --
    
    
    
    
    CostCategories (dict) --The filter based on CostCategory values.
    
    Key (string) --The unique name of the Cost Category.
    
    Values (list) --The specific value of the Cost Category.
    
    (string) --
    
    
    
    
    
    
    Metrics (list) -- The measurement that you want your Savings Plans coverage reported in. The only valid value is SpendCoveredBySavingsPlans .
    
    (string) --
    
    
    NextToken (string) -- The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size.
    MaxResults (integer) -- The number of items to be returned in a response. The default is 20 , with a minimum value of 1 .
    
    """
    pass

def get_savings_plans_purchase_recommendation(SavingsPlansType=None, TermInYears=None, PaymentOption=None, AccountScope=None, NextPageToken=None, PageSize=None, LookbackPeriodInDays=None, Filter=None):
    """
    Retrieves your request parameters, Savings Plan Recommendations Summary and Details.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_savings_plans_purchase_recommendation(
        SavingsPlansType='COMPUTE_SP'|'EC2_INSTANCE_SP',
        TermInYears='ONE_YEAR'|'THREE_YEARS',
        PaymentOption='NO_UPFRONT'|'PARTIAL_UPFRONT'|'ALL_UPFRONT'|'LIGHT_UTILIZATION'|'MEDIUM_UTILIZATION'|'HEAVY_UTILIZATION',
        AccountScope='PAYER'|'LINKED',
        NextPageToken='string',
        PageSize=123,
        LookbackPeriodInDays='SEVEN_DAYS'|'THIRTY_DAYS'|'SIXTY_DAYS',
        Filter={
            'Or': [
                {'... recursive ...'},
            ],
            'And': [
                {'... recursive ...'},
            ],
            'Not': {'... recursive ...'},
            'Dimensions': {
                'Key': 'AZ'|'INSTANCE_TYPE'|'LINKED_ACCOUNT'|'LINKED_ACCOUNT_NAME'|'OPERATION'|'PURCHASE_TYPE'|'REGION'|'SERVICE'|'SERVICE_CODE'|'USAGE_TYPE'|'USAGE_TYPE_GROUP'|'RECORD_TYPE'|'OPERATING_SYSTEM'|'TENANCY'|'SCOPE'|'PLATFORM'|'SUBSCRIPTION_ID'|'LEGAL_ENTITY_NAME'|'DEPLOYMENT_OPTION'|'DATABASE_ENGINE'|'CACHE_ENGINE'|'INSTANCE_TYPE_FAMILY'|'BILLING_ENTITY'|'RESERVATION_ID'|'RESOURCE_ID'|'RIGHTSIZING_TYPE'|'SAVINGS_PLANS_TYPE'|'SAVINGS_PLAN_ARN'|'PAYMENT_OPTION',
                'Values': [
                    'string',
                ],
                'MatchOptions': [
                    'EQUALS'|'STARTS_WITH'|'ENDS_WITH'|'CONTAINS'|'CASE_SENSITIVE'|'CASE_INSENSITIVE',
                ]
            },
            'Tags': {
                'Key': 'string',
                'Values': [
                    'string',
                ],
                'MatchOptions': [
                    'EQUALS'|'STARTS_WITH'|'ENDS_WITH'|'CONTAINS'|'CASE_SENSITIVE'|'CASE_INSENSITIVE',
                ]
            },
            'CostCategories': {
                'Key': 'string',
                'Values': [
                    'string',
                ]
            }
        }
    )
    
    
    :type SavingsPlansType: string
    :param SavingsPlansType: [REQUIRED]\nThe Savings Plans recommendation type requested.\n

    :type TermInYears: string
    :param TermInYears: [REQUIRED]\nThe savings plan recommendation term used to generated these recommendations.\n

    :type PaymentOption: string
    :param PaymentOption: [REQUIRED]\nThe payment option used to generate these recommendations.\n

    :type AccountScope: string
    :param AccountScope: The account scope that you want your recommendations for. Amazon Web Services calculates recommendations including the payer account and linked accounts if the value is set to PAYER . If the value is LINKED , recommendations are calculated for individual linked accounts only.

    :type NextPageToken: string
    :param NextPageToken: The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size.

    :type PageSize: integer
    :param PageSize: The number of recommendations that you want returned in a single response object.

    :type LookbackPeriodInDays: string
    :param LookbackPeriodInDays: [REQUIRED]\nThe lookback period used to generate the recommendation.\n

    :type Filter: dict
    :param Filter: You can filter your recommendations by Account ID with the LINKED_ACCOUNT dimension. To filter your recommendations by Account ID, specify Key as LINKED_ACCOUNT and Value as the comma-separated Acount ID(s) for which you want to see Savings Plans purchase recommendations.\nFor GetSavingsPlansPurchaseRecommendation, the Filter does not include CostCategories or Tags . It only includes Dimensions . With Dimensions , Key must be LINKED_ACCOUNT and Value can be a single Account ID or multiple comma-separated Account IDs for which you want to see Savings Plans Purchase Recommendations. AND and OR operators are not supported.\n\nOr (list) --Return results that match either Dimension object.\n\n(dict) --Use Expression to filter by cost or by usage. There are two patterns:\n\nSimple dimension values - You can set the dimension name and values for the filters that you plan to use. For example, you can filter for REGION==us-east-1 OR REGION==us-west-1 . The Expression for that looks like this: { 'Dimensions': { 'Key': 'REGION', 'Values': [ 'us-east-1', \xe2\x80\x9cus-west-1\xe2\x80\x9d ] } }  The list of dimension values are OR\'d together to retrieve cost or usage data. You can create Expression and DimensionValues objects using either with* methods or set* methods in multiple lines.\nCompound dimension values with logical operations - You can use multiple Expression types and the logical operators AND/OR/NOT to create a list of one or more Expression objects. This allows you to filter on more advanced options. For example, you can filter on ((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE != DataTransfer) . The Expression for that looks like this: { 'And': [ {'Or': [ {'Dimensions': { 'Key': 'REGION', 'Values': [ 'us-east-1', 'us-west-1' ] }}, {'Tags': { 'Key': 'TagName', 'Values': ['Value1'] } } ]}, {'Not': {'Dimensions': { 'Key': 'USAGE_TYPE', 'Values': ['DataTransfer'] }}} ] }\n\n\nNote\n\nBecause each Expression can have only one operator, the service returns an error if more than one is specified. The following example shows an Expression object that creates an error.\n{ 'And': [ ... ], 'DimensionValues': { 'Dimension': 'USAGE_TYPE', 'Values': [ 'DataTransfer' ] } }\n\n\nNote\nFor GetRightsizingRecommendation action, a combination of OR and NOT is not supported. OR is not supported between different dimensions, or dimensions and tags. NOT operators aren\'t supported. Dimensions are also limited to LINKED_ACCOUNT , REGION , or RIGHTSIZING_TYPE .\n\n\n\n\nAnd (list) --Return results that match both Dimension objects.\n\n(dict) --Use Expression to filter by cost or by usage. There are two patterns:\n\nSimple dimension values - You can set the dimension name and values for the filters that you plan to use. For example, you can filter for REGION==us-east-1 OR REGION==us-west-1 . The Expression for that looks like this: { 'Dimensions': { 'Key': 'REGION', 'Values': [ 'us-east-1', \xe2\x80\x9cus-west-1\xe2\x80\x9d ] } }  The list of dimension values are OR\'d together to retrieve cost or usage data. You can create Expression and DimensionValues objects using either with* methods or set* methods in multiple lines.\nCompound dimension values with logical operations - You can use multiple Expression types and the logical operators AND/OR/NOT to create a list of one or more Expression objects. This allows you to filter on more advanced options. For example, you can filter on ((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE != DataTransfer) . The Expression for that looks like this: { 'And': [ {'Or': [ {'Dimensions': { 'Key': 'REGION', 'Values': [ 'us-east-1', 'us-west-1' ] }}, {'Tags': { 'Key': 'TagName', 'Values': ['Value1'] } } ]}, {'Not': {'Dimensions': { 'Key': 'USAGE_TYPE', 'Values': ['DataTransfer'] }}} ] }\n\n\nNote\n\nBecause each Expression can have only one operator, the service returns an error if more than one is specified. The following example shows an Expression object that creates an error.\n{ 'And': [ ... ], 'DimensionValues': { 'Dimension': 'USAGE_TYPE', 'Values': [ 'DataTransfer' ] } }\n\n\nNote\nFor GetRightsizingRecommendation action, a combination of OR and NOT is not supported. OR is not supported between different dimensions, or dimensions and tags. NOT operators aren\'t supported. Dimensions are also limited to LINKED_ACCOUNT , REGION , or RIGHTSIZING_TYPE .\n\n\n\n\nNot (dict) --Return results that don\'t match a Dimension object.\n\nDimensions (dict) --The specific Dimension to use for Expression .\n\nKey (string) --The names of the metadata types that you can use to filter and group your results. For example, AZ returns a list of Availability Zones.\n\nValues (list) --The metadata values that you can use to filter and group your results. You can use GetDimensionValues to find specific values.\n\n(string) --\n\n\nMatchOptions (list) --The match options that you can use to filter your results. MatchOptions is only applicable for actions related to Cost Category. The default values for MatchOptions is EQUALS and CASE_SENSITIVE .\n\n(string) --\n\n\n\n\nTags (dict) --The specific Tag to use for Expression .\n\nKey (string) --The key for the tag.\n\nValues (list) --The specific value of the tag.\n\n(string) --\n\n\nMatchOptions (list) --The match options that you can use to filter your results. MatchOptions is only applicable for only applicable for actions related to Cost Category. The default values for MatchOptions is EQUALS and CASE_SENSITIVE .\n\n(string) --\n\n\n\n\nCostCategories (dict) --The filter based on CostCategory values.\n\nKey (string) --The unique name of the Cost Category.\n\nValues (list) --The specific value of the Cost Category.\n\n(string) --\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Metadata': {
        'RecommendationId': 'string',
        'GenerationTimestamp': 'string'
    },
    'SavingsPlansPurchaseRecommendation': {
        'AccountScope': 'PAYER'|'LINKED',
        'SavingsPlansType': 'COMPUTE_SP'|'EC2_INSTANCE_SP',
        'TermInYears': 'ONE_YEAR'|'THREE_YEARS',
        'PaymentOption': 'NO_UPFRONT'|'PARTIAL_UPFRONT'|'ALL_UPFRONT'|'LIGHT_UTILIZATION'|'MEDIUM_UTILIZATION'|'HEAVY_UTILIZATION',
        'LookbackPeriodInDays': 'SEVEN_DAYS'|'THIRTY_DAYS'|'SIXTY_DAYS',
        'SavingsPlansPurchaseRecommendationDetails': [
            {
                'SavingsPlansDetails': {
                    'Region': 'string',
                    'InstanceFamily': 'string',
                    'OfferingId': 'string'
                },
                'AccountId': 'string',
                'UpfrontCost': 'string',
                'EstimatedROI': 'string',
                'CurrencyCode': 'string',
                'EstimatedSPCost': 'string',
                'EstimatedOnDemandCost': 'string',
                'EstimatedOnDemandCostWithCurrentCommitment': 'string',
                'EstimatedSavingsAmount': 'string',
                'EstimatedSavingsPercentage': 'string',
                'HourlyCommitmentToPurchase': 'string',
                'EstimatedAverageUtilization': 'string',
                'EstimatedMonthlySavingsAmount': 'string',
                'CurrentMinimumHourlyOnDemandSpend': 'string',
                'CurrentMaximumHourlyOnDemandSpend': 'string',
                'CurrentAverageHourlyOnDemandSpend': 'string'
            },
        ],
        'SavingsPlansPurchaseRecommendationSummary': {
            'EstimatedROI': 'string',
            'CurrencyCode': 'string',
            'EstimatedTotalCost': 'string',
            'CurrentOnDemandSpend': 'string',
            'EstimatedSavingsAmount': 'string',
            'TotalRecommendationCount': 'string',
            'DailyCommitmentToPurchase': 'string',
            'HourlyCommitmentToPurchase': 'string',
            'EstimatedSavingsPercentage': 'string',
            'EstimatedMonthlySavingsAmount': 'string',
            'EstimatedOnDemandCostWithCurrentCommitment': 'string'
        }
    },
    'NextPageToken': 'string'
}


Response Structure

(dict) --

Metadata (dict) --
Information regarding this specific recommendation set.

RecommendationId (string) --
The unique identifier for the recommendation set.

GenerationTimestamp (string) --
The timestamp showing when the recommendations were generated.



SavingsPlansPurchaseRecommendation (dict) --
Contains your request parameters, Savings Plan Recommendations Summary, and Details.

AccountScope (string) --
The account scope that you want your recommendations for. Amazon Web Services calculates recommendations including the payer account and linked accounts if the value is set to PAYER . If the value is LINKED , recommendations are calculated for individual linked accounts only.

SavingsPlansType (string) --
The requested Savings Plans recommendation type.

TermInYears (string) --
The Savings Plans recommendation term in years, used to generate the recommendation.

PaymentOption (string) --
The payment option used to generate the recommendation.

LookbackPeriodInDays (string) --
The lookback period in days, used to generate the recommendation.

SavingsPlansPurchaseRecommendationDetails (list) --
Details for the Savings Plans we recommend that you purchase to cover existing Savings Plans eligible workloads.

(dict) --
Details for your recommended Savings Plans.

SavingsPlansDetails (dict) --
Details for your recommended Savings Plans.

Region (string) --
A collection of AWS resources in a geographic area. Each AWS Region is isolated and independent of the other Regions.

InstanceFamily (string) --
A group of instance types that Savings Plans applies to.

OfferingId (string) --
The unique ID used to distinguish Savings Plans from one another.



AccountId (string) --
The AccountID the recommendation is generated for.

UpfrontCost (string) --
The upfront cost of the recommended Savings Plans, based on the selected payment option.

EstimatedROI (string) --
The estimated return on investment based on the recommended Savings Plans purchased. This is calculated as estimatedSavingsAmount / estimatedSPCost *100.

CurrencyCode (string) --
The currency code Amazon Web Services used to generate the recommendations and present potential savings.

EstimatedSPCost (string) --
The cost of the recommended Savings Plans over the length of the lookback period.

EstimatedOnDemandCost (string) --
The remaining On-Demand cost estimated to not be covered by the recommended Savings Plans, over the length of the lookback period.

EstimatedOnDemandCostWithCurrentCommitment (string) --
The estimated On-Demand costs you would expect with no additional commitment, based on your usage of the selected time period and the Savings Plans you own.

EstimatedSavingsAmount (string) --
The estimated savings amount based on the recommended Savings Plans over the length of the lookback period.

EstimatedSavingsPercentage (string) --
The estimated savings percentage relative to the total cost of applicable On-Demand usage over the lookback period.

HourlyCommitmentToPurchase (string) --
The recommended hourly commitment level for the Savings Plans type, and configuration based on the usage during the lookback period.

EstimatedAverageUtilization (string) --
The estimated utilization of the recommended Savings Plans.

EstimatedMonthlySavingsAmount (string) --
The estimated monthly savings amount, based on the recommended Savings Plans.

CurrentMinimumHourlyOnDemandSpend (string) --
The lowest value of hourly On-Demand spend over the lookback period of the applicable usage type.

CurrentMaximumHourlyOnDemandSpend (string) --
The highest value of hourly On-Demand spend over the lookback period of the applicable usage type.

CurrentAverageHourlyOnDemandSpend (string) --
The average value of hourly On-Demand spend over the lookback period of the applicable usage type.





SavingsPlansPurchaseRecommendationSummary (dict) --
Summary metrics for your Savings Plans Recommendations.

EstimatedROI (string) --
The estimated return on investment based on the recommended Savings Plans and estimated savings.

CurrencyCode (string) --
The currency code Amazon Web Services used to generate the recommendations and present potential savings.

EstimatedTotalCost (string) --
The estimated total cost of the usage after purchasing the recommended Savings Plans. This is a sum of the cost of Savings Plans during this term, and the remaining On-Demand usage.

CurrentOnDemandSpend (string) --
The current total on demand spend of the applicable usage types over the lookback period.

EstimatedSavingsAmount (string) --
The estimated total savings over the lookback period, based on the purchase of the recommended Savings Plans.

TotalRecommendationCount (string) --
The aggregate number of Savings Plans recommendations that exist for your account.

DailyCommitmentToPurchase (string) --
The recommended Savings Plans cost on a daily (24 hourly) basis.

HourlyCommitmentToPurchase (string) --
The recommended hourly commitment based on the recommendation parameters.

EstimatedSavingsPercentage (string) --
The estimated savings relative to the total cost of On-Demand usage, over the lookback period. This is calculated as estimatedSavingsAmount / CurrentOnDemandSpend *100.

EstimatedMonthlySavingsAmount (string) --
The estimated monthly savings amount, based on the recommended Savings Plans purchase.

EstimatedOnDemandCostWithCurrentCommitment (string) --
The estimated On-Demand costs you would expect with no additional commitment, based on your usage of the selected time period and the Savings Plans you own.





NextPageToken (string) --
The token for the next set of retrievable results. AWS provides the token when the response from a previous call has more results than the maximum page size.







Exceptions

CostExplorer.Client.exceptions.LimitExceededException
CostExplorer.Client.exceptions.InvalidNextTokenException


    :return: {
        'Metadata': {
            'RecommendationId': 'string',
            'GenerationTimestamp': 'string'
        },
        'SavingsPlansPurchaseRecommendation': {
            'AccountScope': 'PAYER'|'LINKED',
            'SavingsPlansType': 'COMPUTE_SP'|'EC2_INSTANCE_SP',
            'TermInYears': 'ONE_YEAR'|'THREE_YEARS',
            'PaymentOption': 'NO_UPFRONT'|'PARTIAL_UPFRONT'|'ALL_UPFRONT'|'LIGHT_UTILIZATION'|'MEDIUM_UTILIZATION'|'HEAVY_UTILIZATION',
            'LookbackPeriodInDays': 'SEVEN_DAYS'|'THIRTY_DAYS'|'SIXTY_DAYS',
            'SavingsPlansPurchaseRecommendationDetails': [
                {
                    'SavingsPlansDetails': {
                        'Region': 'string',
                        'InstanceFamily': 'string',
                        'OfferingId': 'string'
                    },
                    'AccountId': 'string',
                    'UpfrontCost': 'string',
                    'EstimatedROI': 'string',
                    'CurrencyCode': 'string',
                    'EstimatedSPCost': 'string',
                    'EstimatedOnDemandCost': 'string',
                    'EstimatedOnDemandCostWithCurrentCommitment': 'string',
                    'EstimatedSavingsAmount': 'string',
                    'EstimatedSavingsPercentage': 'string',
                    'HourlyCommitmentToPurchase': 'string',
                    'EstimatedAverageUtilization': 'string',
                    'EstimatedMonthlySavingsAmount': 'string',
                    'CurrentMinimumHourlyOnDemandSpend': 'string',
                    'CurrentMaximumHourlyOnDemandSpend': 'string',
                    'CurrentAverageHourlyOnDemandSpend': 'string'
                },
            ],
            'SavingsPlansPurchaseRecommendationSummary': {
                'EstimatedROI': 'string',
                'CurrencyCode': 'string',
                'EstimatedTotalCost': 'string',
                'CurrentOnDemandSpend': 'string',
                'EstimatedSavingsAmount': 'string',
                'TotalRecommendationCount': 'string',
                'DailyCommitmentToPurchase': 'string',
                'HourlyCommitmentToPurchase': 'string',
                'EstimatedSavingsPercentage': 'string',
                'EstimatedMonthlySavingsAmount': 'string',
                'EstimatedOnDemandCostWithCurrentCommitment': 'string'
            }
        },
        'NextPageToken': 'string'
    }
    
    
    :returns: 
    CostExplorer.Client.exceptions.LimitExceededException
    CostExplorer.Client.exceptions.InvalidNextTokenException
    
    """
    pass

def get_savings_plans_utilization(TimePeriod=None, Granularity=None, Filter=None):
    """
    Retrieves the Savings Plans utilization for your account across date ranges with daily or monthly granularity. Master accounts in an organization have access to member accounts. You can use GetDimensionValues in SAVINGS_PLANS to determine the possible dimension values.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_savings_plans_utilization(
        TimePeriod={
            'Start': 'string',
            'End': 'string'
        },
        Granularity='DAILY'|'MONTHLY'|'HOURLY',
        Filter={
            'Or': [
                {'... recursive ...'},
            ],
            'And': [
                {'... recursive ...'},
            ],
            'Not': {'... recursive ...'},
            'Dimensions': {
                'Key': 'AZ'|'INSTANCE_TYPE'|'LINKED_ACCOUNT'|'LINKED_ACCOUNT_NAME'|'OPERATION'|'PURCHASE_TYPE'|'REGION'|'SERVICE'|'SERVICE_CODE'|'USAGE_TYPE'|'USAGE_TYPE_GROUP'|'RECORD_TYPE'|'OPERATING_SYSTEM'|'TENANCY'|'SCOPE'|'PLATFORM'|'SUBSCRIPTION_ID'|'LEGAL_ENTITY_NAME'|'DEPLOYMENT_OPTION'|'DATABASE_ENGINE'|'CACHE_ENGINE'|'INSTANCE_TYPE_FAMILY'|'BILLING_ENTITY'|'RESERVATION_ID'|'RESOURCE_ID'|'RIGHTSIZING_TYPE'|'SAVINGS_PLANS_TYPE'|'SAVINGS_PLAN_ARN'|'PAYMENT_OPTION',
                'Values': [
                    'string',
                ],
                'MatchOptions': [
                    'EQUALS'|'STARTS_WITH'|'ENDS_WITH'|'CONTAINS'|'CASE_SENSITIVE'|'CASE_INSENSITIVE',
                ]
            },
            'Tags': {
                'Key': 'string',
                'Values': [
                    'string',
                ],
                'MatchOptions': [
                    'EQUALS'|'STARTS_WITH'|'ENDS_WITH'|'CONTAINS'|'CASE_SENSITIVE'|'CASE_INSENSITIVE',
                ]
            },
            'CostCategories': {
                'Key': 'string',
                'Values': [
                    'string',
                ]
            }
        }
    )
    
    
    :type TimePeriod: dict
    :param TimePeriod: [REQUIRED]\nThe time period that you want the usage and costs for. The Start date must be within 13 months. The End date must be after the Start date, and before the current date. Future dates can\'t be used as an End date.\n\nStart (string) -- [REQUIRED]The beginning of the time period that you want the usage and costs for. The start date is inclusive. For example, if start is 2017-01-01 , AWS retrieves cost and usage data starting at 2017-01-01 up to the end date.\n\nEnd (string) -- [REQUIRED]The end of the time period that you want the usage and costs for. The end date is exclusive. For example, if end is 2017-05-01 , AWS retrieves cost and usage data from the start date up to, but not including, 2017-05-01 .\n\n\n

    :type Granularity: string
    :param Granularity: The granularity of the Amazon Web Services utillization data for your Savings Plans.\nThe GetSavingsPlansUtilization operation supports only DAILY and MONTHLY granularities.\n

    :type Filter: dict
    :param Filter: Filters Savings Plans utilization coverage data for active Savings Plans dimensions. You can filter data with the following dimensions:\n\nLINKED_ACCOUNT\nSAVINGS_PLAN_ARN\nSAVINGS_PLANS_TYPE\nREGION\nPAYMENT_OPTION\nINSTANCE_TYPE_FAMILY\n\n\nGetSavingsPlansUtilization uses the same Expression object as the other operations, but only AND is supported among each dimension.\n\nOr (list) --Return results that match either Dimension object.\n\n(dict) --Use Expression to filter by cost or by usage. There are two patterns:\n\nSimple dimension values - You can set the dimension name and values for the filters that you plan to use. For example, you can filter for REGION==us-east-1 OR REGION==us-west-1 . The Expression for that looks like this: { 'Dimensions': { 'Key': 'REGION', 'Values': [ 'us-east-1', \xe2\x80\x9cus-west-1\xe2\x80\x9d ] } }  The list of dimension values are OR\'d together to retrieve cost or usage data. You can create Expression and DimensionValues objects using either with* methods or set* methods in multiple lines.\nCompound dimension values with logical operations - You can use multiple Expression types and the logical operators AND/OR/NOT to create a list of one or more Expression objects. This allows you to filter on more advanced options. For example, you can filter on ((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE != DataTransfer) . The Expression for that looks like this: { 'And': [ {'Or': [ {'Dimensions': { 'Key': 'REGION', 'Values': [ 'us-east-1', 'us-west-1' ] }}, {'Tags': { 'Key': 'TagName', 'Values': ['Value1'] } } ]}, {'Not': {'Dimensions': { 'Key': 'USAGE_TYPE', 'Values': ['DataTransfer'] }}} ] }\n\n\nNote\n\nBecause each Expression can have only one operator, the service returns an error if more than one is specified. The following example shows an Expression object that creates an error.\n{ 'And': [ ... ], 'DimensionValues': { 'Dimension': 'USAGE_TYPE', 'Values': [ 'DataTransfer' ] } }\n\n\nNote\nFor GetRightsizingRecommendation action, a combination of OR and NOT is not supported. OR is not supported between different dimensions, or dimensions and tags. NOT operators aren\'t supported. Dimensions are also limited to LINKED_ACCOUNT , REGION , or RIGHTSIZING_TYPE .\n\n\n\n\nAnd (list) --Return results that match both Dimension objects.\n\n(dict) --Use Expression to filter by cost or by usage. There are two patterns:\n\nSimple dimension values - You can set the dimension name and values for the filters that you plan to use. For example, you can filter for REGION==us-east-1 OR REGION==us-west-1 . The Expression for that looks like this: { 'Dimensions': { 'Key': 'REGION', 'Values': [ 'us-east-1', \xe2\x80\x9cus-west-1\xe2\x80\x9d ] } }  The list of dimension values are OR\'d together to retrieve cost or usage data. You can create Expression and DimensionValues objects using either with* methods or set* methods in multiple lines.\nCompound dimension values with logical operations - You can use multiple Expression types and the logical operators AND/OR/NOT to create a list of one or more Expression objects. This allows you to filter on more advanced options. For example, you can filter on ((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE != DataTransfer) . The Expression for that looks like this: { 'And': [ {'Or': [ {'Dimensions': { 'Key': 'REGION', 'Values': [ 'us-east-1', 'us-west-1' ] }}, {'Tags': { 'Key': 'TagName', 'Values': ['Value1'] } } ]}, {'Not': {'Dimensions': { 'Key': 'USAGE_TYPE', 'Values': ['DataTransfer'] }}} ] }\n\n\nNote\n\nBecause each Expression can have only one operator, the service returns an error if more than one is specified. The following example shows an Expression object that creates an error.\n{ 'And': [ ... ], 'DimensionValues': { 'Dimension': 'USAGE_TYPE', 'Values': [ 'DataTransfer' ] } }\n\n\nNote\nFor GetRightsizingRecommendation action, a combination of OR and NOT is not supported. OR is not supported between different dimensions, or dimensions and tags. NOT operators aren\'t supported. Dimensions are also limited to LINKED_ACCOUNT , REGION , or RIGHTSIZING_TYPE .\n\n\n\n\nNot (dict) --Return results that don\'t match a Dimension object.\n\nDimensions (dict) --The specific Dimension to use for Expression .\n\nKey (string) --The names of the metadata types that you can use to filter and group your results. For example, AZ returns a list of Availability Zones.\n\nValues (list) --The metadata values that you can use to filter and group your results. You can use GetDimensionValues to find specific values.\n\n(string) --\n\n\nMatchOptions (list) --The match options that you can use to filter your results. MatchOptions is only applicable for actions related to Cost Category. The default values for MatchOptions is EQUALS and CASE_SENSITIVE .\n\n(string) --\n\n\n\n\nTags (dict) --The specific Tag to use for Expression .\n\nKey (string) --The key for the tag.\n\nValues (list) --The specific value of the tag.\n\n(string) --\n\n\nMatchOptions (list) --The match options that you can use to filter your results. MatchOptions is only applicable for only applicable for actions related to Cost Category. The default values for MatchOptions is EQUALS and CASE_SENSITIVE .\n\n(string) --\n\n\n\n\nCostCategories (dict) --The filter based on CostCategory values.\n\nKey (string) --The unique name of the Cost Category.\n\nValues (list) --The specific value of the Cost Category.\n\n(string) --\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'SavingsPlansUtilizationsByTime': [
        {
            'TimePeriod': {
                'Start': 'string',
                'End': 'string'
            },
            'Utilization': {
                'TotalCommitment': 'string',
                'UsedCommitment': 'string',
                'UnusedCommitment': 'string',
                'UtilizationPercentage': 'string'
            },
            'Savings': {
                'NetSavings': 'string',
                'OnDemandCostEquivalent': 'string'
            },
            'AmortizedCommitment': {
                'AmortizedRecurringCommitment': 'string',
                'AmortizedUpfrontCommitment': 'string',
                'TotalAmortizedCommitment': 'string'
            }
        },
    ],
    'Total': {
        'Utilization': {
            'TotalCommitment': 'string',
            'UsedCommitment': 'string',
            'UnusedCommitment': 'string',
            'UtilizationPercentage': 'string'
        },
        'Savings': {
            'NetSavings': 'string',
            'OnDemandCostEquivalent': 'string'
        },
        'AmortizedCommitment': {
            'AmortizedRecurringCommitment': 'string',
            'AmortizedUpfrontCommitment': 'string',
            'TotalAmortizedCommitment': 'string'
        }
    }
}


Response Structure

(dict) --

SavingsPlansUtilizationsByTime (list) --
The amount of cost/commitment you used your Savings Plans. This allows you to specify date ranges.

(dict) --
The amount of Savings Plans utilization, in hours.

TimePeriod (dict) --
The time period that you want the usage and costs for.

Start (string) --
The beginning of the time period that you want the usage and costs for. The start date is inclusive. For example, if start is 2017-01-01 , AWS retrieves cost and usage data starting at 2017-01-01 up to the end date.

End (string) --
The end of the time period that you want the usage and costs for. The end date is exclusive. For example, if end is 2017-05-01 , AWS retrieves cost and usage data from the start date up to, but not including, 2017-05-01 .



Utilization (dict) --
A ratio of your effectiveness of using existing Savings Plans to apply to workloads that are Savings Plans eligible.

TotalCommitment (string) --
The total amount of Savings Plans commitment that\'s been purchased in an account (or set of accounts).

UsedCommitment (string) --
The amount of your Savings Plans commitment that was consumed from Savings Plans eligible usage in a specific period.

UnusedCommitment (string) --
The amount of your Savings Plans commitment that was not consumed from Savings Plans eligible usage in a specific period.

UtilizationPercentage (string) --
The amount of UsedCommitment divided by the TotalCommitment for your Savings Plans.



Savings (dict) --
The amount saved by using existing Savings Plans. Savings returns both net savings from Savings Plans as well as the onDemandCostEquivalent of the Savings Plans when considering the utilization rate.

NetSavings (string) --
The savings amount that you are accumulating for the usage that is covered by a Savings Plans, when compared to the On-Demand equivalent of the same usage.

OnDemandCostEquivalent (string) --
How much the amount that the usage would have cost if it was accrued at the On-Demand rate.



AmortizedCommitment (dict) --
The total amortized commitment for a Savings Plans. This includes the sum of the upfront and recurring Savings Plans fees.

AmortizedRecurringCommitment (string) --
The amortized amount of your Savings Plans commitment that was purchased with either a Partial or a NoUpfront .

AmortizedUpfrontCommitment (string) --
The amortized amount of your Savings Plans commitment that was purchased with an Upfront or PartialUpfront Savings Plans.

TotalAmortizedCommitment (string) --
The total amortized amount of your Savings Plans commitment, regardless of your Savings Plans purchase method.







Total (dict) --
The total amount of cost/commitment that you used your Savings Plans, regardless of date ranges.

Utilization (dict) --
A ratio of your effectiveness of using existing Savings Plans to apply to workloads that are Savings Plans eligible.

TotalCommitment (string) --
The total amount of Savings Plans commitment that\'s been purchased in an account (or set of accounts).

UsedCommitment (string) --
The amount of your Savings Plans commitment that was consumed from Savings Plans eligible usage in a specific period.

UnusedCommitment (string) --
The amount of your Savings Plans commitment that was not consumed from Savings Plans eligible usage in a specific period.

UtilizationPercentage (string) --
The amount of UsedCommitment divided by the TotalCommitment for your Savings Plans.



Savings (dict) --
The amount saved by using existing Savings Plans. Savings returns both net savings from Savings Plans, as well as the onDemandCostEquivalent of the Savings Plans when considering the utilization rate.

NetSavings (string) --
The savings amount that you are accumulating for the usage that is covered by a Savings Plans, when compared to the On-Demand equivalent of the same usage.

OnDemandCostEquivalent (string) --
How much the amount that the usage would have cost if it was accrued at the On-Demand rate.



AmortizedCommitment (dict) --
The total amortized commitment for a Savings Plans. This includes the sum of the upfront and recurring Savings Plans fees.

AmortizedRecurringCommitment (string) --
The amortized amount of your Savings Plans commitment that was purchased with either a Partial or a NoUpfront .

AmortizedUpfrontCommitment (string) --
The amortized amount of your Savings Plans commitment that was purchased with an Upfront or PartialUpfront Savings Plans.

TotalAmortizedCommitment (string) --
The total amortized amount of your Savings Plans commitment, regardless of your Savings Plans purchase method.











Exceptions

CostExplorer.Client.exceptions.LimitExceededException
CostExplorer.Client.exceptions.DataUnavailableException


    :return: {
        'SavingsPlansUtilizationsByTime': [
            {
                'TimePeriod': {
                    'Start': 'string',
                    'End': 'string'
                },
                'Utilization': {
                    'TotalCommitment': 'string',
                    'UsedCommitment': 'string',
                    'UnusedCommitment': 'string',
                    'UtilizationPercentage': 'string'
                },
                'Savings': {
                    'NetSavings': 'string',
                    'OnDemandCostEquivalent': 'string'
                },
                'AmortizedCommitment': {
                    'AmortizedRecurringCommitment': 'string',
                    'AmortizedUpfrontCommitment': 'string',
                    'TotalAmortizedCommitment': 'string'
                }
            },
        ],
        'Total': {
            'Utilization': {
                'TotalCommitment': 'string',
                'UsedCommitment': 'string',
                'UnusedCommitment': 'string',
                'UtilizationPercentage': 'string'
            },
            'Savings': {
                'NetSavings': 'string',
                'OnDemandCostEquivalent': 'string'
            },
            'AmortizedCommitment': {
                'AmortizedRecurringCommitment': 'string',
                'AmortizedUpfrontCommitment': 'string',
                'TotalAmortizedCommitment': 'string'
            }
        }
    }
    
    
    :returns: 
    CostExplorer.Client.exceptions.LimitExceededException
    CostExplorer.Client.exceptions.DataUnavailableException
    
    """
    pass

def get_savings_plans_utilization_details(TimePeriod=None, Filter=None, NextToken=None, MaxResults=None):
    """
    Retrieves attribute data along with aggregate utilization and savings data for a given time period. This doesn\'t support granular or grouped data (daily/monthly) in response. You can\'t retrieve data by dates in a single response similar to GetSavingsPlanUtilization , but you have the option to make multiple calls to GetSavingsPlanUtilizationDetails by providing individual dates. You can use GetDimensionValues in SAVINGS_PLANS to determine the possible dimension values.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_savings_plans_utilization_details(
        TimePeriod={
            'Start': 'string',
            'End': 'string'
        },
        Filter={
            'Or': [
                {'... recursive ...'},
            ],
            'And': [
                {'... recursive ...'},
            ],
            'Not': {'... recursive ...'},
            'Dimensions': {
                'Key': 'AZ'|'INSTANCE_TYPE'|'LINKED_ACCOUNT'|'LINKED_ACCOUNT_NAME'|'OPERATION'|'PURCHASE_TYPE'|'REGION'|'SERVICE'|'SERVICE_CODE'|'USAGE_TYPE'|'USAGE_TYPE_GROUP'|'RECORD_TYPE'|'OPERATING_SYSTEM'|'TENANCY'|'SCOPE'|'PLATFORM'|'SUBSCRIPTION_ID'|'LEGAL_ENTITY_NAME'|'DEPLOYMENT_OPTION'|'DATABASE_ENGINE'|'CACHE_ENGINE'|'INSTANCE_TYPE_FAMILY'|'BILLING_ENTITY'|'RESERVATION_ID'|'RESOURCE_ID'|'RIGHTSIZING_TYPE'|'SAVINGS_PLANS_TYPE'|'SAVINGS_PLAN_ARN'|'PAYMENT_OPTION',
                'Values': [
                    'string',
                ],
                'MatchOptions': [
                    'EQUALS'|'STARTS_WITH'|'ENDS_WITH'|'CONTAINS'|'CASE_SENSITIVE'|'CASE_INSENSITIVE',
                ]
            },
            'Tags': {
                'Key': 'string',
                'Values': [
                    'string',
                ],
                'MatchOptions': [
                    'EQUALS'|'STARTS_WITH'|'ENDS_WITH'|'CONTAINS'|'CASE_SENSITIVE'|'CASE_INSENSITIVE',
                ]
            },
            'CostCategories': {
                'Key': 'string',
                'Values': [
                    'string',
                ]
            }
        },
        NextToken='string',
        MaxResults=123
    )
    
    
    :type TimePeriod: dict
    :param TimePeriod: [REQUIRED]\nThe time period that you want the usage and costs for. The Start date must be within 13 months. The End date must be after the Start date, and before the current date. Future dates can\'t be used as an End date.\n\nStart (string) -- [REQUIRED]The beginning of the time period that you want the usage and costs for. The start date is inclusive. For example, if start is 2017-01-01 , AWS retrieves cost and usage data starting at 2017-01-01 up to the end date.\n\nEnd (string) -- [REQUIRED]The end of the time period that you want the usage and costs for. The end date is exclusive. For example, if end is 2017-05-01 , AWS retrieves cost and usage data from the start date up to, but not including, 2017-05-01 .\n\n\n

    :type Filter: dict
    :param Filter: Filters Savings Plans utilization coverage data for active Savings Plans dimensions. You can filter data with the following dimensions:\n\nLINKED_ACCOUNT\nSAVINGS_PLAN_ARN\nREGION\nPAYMENT_OPTION\nINSTANCE_TYPE_FAMILY\n\n\nGetSavingsPlansUtilizationDetails uses the same Expression object as the other operations, but only AND is supported among each dimension.\n\nOr (list) --Return results that match either Dimension object.\n\n(dict) --Use Expression to filter by cost or by usage. There are two patterns:\n\nSimple dimension values - You can set the dimension name and values for the filters that you plan to use. For example, you can filter for REGION==us-east-1 OR REGION==us-west-1 . The Expression for that looks like this: { 'Dimensions': { 'Key': 'REGION', 'Values': [ 'us-east-1', \xe2\x80\x9cus-west-1\xe2\x80\x9d ] } }  The list of dimension values are OR\'d together to retrieve cost or usage data. You can create Expression and DimensionValues objects using either with* methods or set* methods in multiple lines.\nCompound dimension values with logical operations - You can use multiple Expression types and the logical operators AND/OR/NOT to create a list of one or more Expression objects. This allows you to filter on more advanced options. For example, you can filter on ((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE != DataTransfer) . The Expression for that looks like this: { 'And': [ {'Or': [ {'Dimensions': { 'Key': 'REGION', 'Values': [ 'us-east-1', 'us-west-1' ] }}, {'Tags': { 'Key': 'TagName', 'Values': ['Value1'] } } ]}, {'Not': {'Dimensions': { 'Key': 'USAGE_TYPE', 'Values': ['DataTransfer'] }}} ] }\n\n\nNote\n\nBecause each Expression can have only one operator, the service returns an error if more than one is specified. The following example shows an Expression object that creates an error.\n{ 'And': [ ... ], 'DimensionValues': { 'Dimension': 'USAGE_TYPE', 'Values': [ 'DataTransfer' ] } }\n\n\nNote\nFor GetRightsizingRecommendation action, a combination of OR and NOT is not supported. OR is not supported between different dimensions, or dimensions and tags. NOT operators aren\'t supported. Dimensions are also limited to LINKED_ACCOUNT , REGION , or RIGHTSIZING_TYPE .\n\n\n\n\nAnd (list) --Return results that match both Dimension objects.\n\n(dict) --Use Expression to filter by cost or by usage. There are two patterns:\n\nSimple dimension values - You can set the dimension name and values for the filters that you plan to use. For example, you can filter for REGION==us-east-1 OR REGION==us-west-1 . The Expression for that looks like this: { 'Dimensions': { 'Key': 'REGION', 'Values': [ 'us-east-1', \xe2\x80\x9cus-west-1\xe2\x80\x9d ] } }  The list of dimension values are OR\'d together to retrieve cost or usage data. You can create Expression and DimensionValues objects using either with* methods or set* methods in multiple lines.\nCompound dimension values with logical operations - You can use multiple Expression types and the logical operators AND/OR/NOT to create a list of one or more Expression objects. This allows you to filter on more advanced options. For example, you can filter on ((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE != DataTransfer) . The Expression for that looks like this: { 'And': [ {'Or': [ {'Dimensions': { 'Key': 'REGION', 'Values': [ 'us-east-1', 'us-west-1' ] }}, {'Tags': { 'Key': 'TagName', 'Values': ['Value1'] } } ]}, {'Not': {'Dimensions': { 'Key': 'USAGE_TYPE', 'Values': ['DataTransfer'] }}} ] }\n\n\nNote\n\nBecause each Expression can have only one operator, the service returns an error if more than one is specified. The following example shows an Expression object that creates an error.\n{ 'And': [ ... ], 'DimensionValues': { 'Dimension': 'USAGE_TYPE', 'Values': [ 'DataTransfer' ] } }\n\n\nNote\nFor GetRightsizingRecommendation action, a combination of OR and NOT is not supported. OR is not supported between different dimensions, or dimensions and tags. NOT operators aren\'t supported. Dimensions are also limited to LINKED_ACCOUNT , REGION , or RIGHTSIZING_TYPE .\n\n\n\n\nNot (dict) --Return results that don\'t match a Dimension object.\n\nDimensions (dict) --The specific Dimension to use for Expression .\n\nKey (string) --The names of the metadata types that you can use to filter and group your results. For example, AZ returns a list of Availability Zones.\n\nValues (list) --The metadata values that you can use to filter and group your results. You can use GetDimensionValues to find specific values.\n\n(string) --\n\n\nMatchOptions (list) --The match options that you can use to filter your results. MatchOptions is only applicable for actions related to Cost Category. The default values for MatchOptions is EQUALS and CASE_SENSITIVE .\n\n(string) --\n\n\n\n\nTags (dict) --The specific Tag to use for Expression .\n\nKey (string) --The key for the tag.\n\nValues (list) --The specific value of the tag.\n\n(string) --\n\n\nMatchOptions (list) --The match options that you can use to filter your results. MatchOptions is only applicable for only applicable for actions related to Cost Category. The default values for MatchOptions is EQUALS and CASE_SENSITIVE .\n\n(string) --\n\n\n\n\nCostCategories (dict) --The filter based on CostCategory values.\n\nKey (string) --The unique name of the Cost Category.\n\nValues (list) --The specific value of the Cost Category.\n\n(string) --\n\n\n\n\n\n

    :type NextToken: string
    :param NextToken: The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size.

    :type MaxResults: integer
    :param MaxResults: The number of items to be returned in a response. The default is 20 , with a minimum value of 1 .

    :rtype: dict

ReturnsResponse Syntax
{
    'SavingsPlansUtilizationDetails': [
        {
            'SavingsPlanArn': 'string',
            'Attributes': {
                'string': 'string'
            },
            'Utilization': {
                'TotalCommitment': 'string',
                'UsedCommitment': 'string',
                'UnusedCommitment': 'string',
                'UtilizationPercentage': 'string'
            },
            'Savings': {
                'NetSavings': 'string',
                'OnDemandCostEquivalent': 'string'
            },
            'AmortizedCommitment': {
                'AmortizedRecurringCommitment': 'string',
                'AmortizedUpfrontCommitment': 'string',
                'TotalAmortizedCommitment': 'string'
            }
        },
    ],
    'Total': {
        'Utilization': {
            'TotalCommitment': 'string',
            'UsedCommitment': 'string',
            'UnusedCommitment': 'string',
            'UtilizationPercentage': 'string'
        },
        'Savings': {
            'NetSavings': 'string',
            'OnDemandCostEquivalent': 'string'
        },
        'AmortizedCommitment': {
            'AmortizedRecurringCommitment': 'string',
            'AmortizedUpfrontCommitment': 'string',
            'TotalAmortizedCommitment': 'string'
        }
    },
    'TimePeriod': {
        'Start': 'string',
        'End': 'string'
    },
    'NextToken': 'string'
}


Response Structure

(dict) --

SavingsPlansUtilizationDetails (list) --
Retrieves a single daily or monthly Savings Plans utilization rate and details for your account.

(dict) --
A single daily or monthly Savings Plans utilization rate, and details for your account. Master accounts in an organization have access to member accounts. You can use GetDimensionValues to determine the possible dimension values.

SavingsPlanArn (string) --
The unique Amazon Resource Name (ARN) for a particular Savings Plan.

Attributes (dict) --
The attribute that applies to a specific Dimension .

(string) --
(string) --




Utilization (dict) --
A ratio of your effectiveness of using existing Savings Plans to apply to workloads that are Savings Plans eligible.

TotalCommitment (string) --
The total amount of Savings Plans commitment that\'s been purchased in an account (or set of accounts).

UsedCommitment (string) --
The amount of your Savings Plans commitment that was consumed from Savings Plans eligible usage in a specific period.

UnusedCommitment (string) --
The amount of your Savings Plans commitment that was not consumed from Savings Plans eligible usage in a specific period.

UtilizationPercentage (string) --
The amount of UsedCommitment divided by the TotalCommitment for your Savings Plans.



Savings (dict) --
The amount saved by using existing Savings Plans. Savings returns both net savings from savings plans as well as the onDemandCostEquivalent of the Savings Plans when considering the utilization rate.

NetSavings (string) --
The savings amount that you are accumulating for the usage that is covered by a Savings Plans, when compared to the On-Demand equivalent of the same usage.

OnDemandCostEquivalent (string) --
How much the amount that the usage would have cost if it was accrued at the On-Demand rate.



AmortizedCommitment (dict) --
The total amortized commitment for a Savings Plans. Includes the sum of the upfront and recurring Savings Plans fees.

AmortizedRecurringCommitment (string) --
The amortized amount of your Savings Plans commitment that was purchased with either a Partial or a NoUpfront .

AmortizedUpfrontCommitment (string) --
The amortized amount of your Savings Plans commitment that was purchased with an Upfront or PartialUpfront Savings Plans.

TotalAmortizedCommitment (string) --
The total amortized amount of your Savings Plans commitment, regardless of your Savings Plans purchase method.







Total (dict) --
The total Savings Plans utilization, regardless of time period.

Utilization (dict) --
A ratio of your effectiveness of using existing Savings Plans to apply to workloads that are Savings Plans eligible.

TotalCommitment (string) --
The total amount of Savings Plans commitment that\'s been purchased in an account (or set of accounts).

UsedCommitment (string) --
The amount of your Savings Plans commitment that was consumed from Savings Plans eligible usage in a specific period.

UnusedCommitment (string) --
The amount of your Savings Plans commitment that was not consumed from Savings Plans eligible usage in a specific period.

UtilizationPercentage (string) --
The amount of UsedCommitment divided by the TotalCommitment for your Savings Plans.



Savings (dict) --
The amount saved by using existing Savings Plans. Savings returns both net savings from Savings Plans, as well as the onDemandCostEquivalent of the Savings Plans when considering the utilization rate.

NetSavings (string) --
The savings amount that you are accumulating for the usage that is covered by a Savings Plans, when compared to the On-Demand equivalent of the same usage.

OnDemandCostEquivalent (string) --
How much the amount that the usage would have cost if it was accrued at the On-Demand rate.



AmortizedCommitment (dict) --
The total amortized commitment for a Savings Plans. This includes the sum of the upfront and recurring Savings Plans fees.

AmortizedRecurringCommitment (string) --
The amortized amount of your Savings Plans commitment that was purchased with either a Partial or a NoUpfront .

AmortizedUpfrontCommitment (string) --
The amortized amount of your Savings Plans commitment that was purchased with an Upfront or PartialUpfront Savings Plans.

TotalAmortizedCommitment (string) --
The total amortized amount of your Savings Plans commitment, regardless of your Savings Plans purchase method.





TimePeriod (dict) --
The time period that you want the usage and costs for.

Start (string) --
The beginning of the time period that you want the usage and costs for. The start date is inclusive. For example, if start is 2017-01-01 , AWS retrieves cost and usage data starting at 2017-01-01 up to the end date.

End (string) --
The end of the time period that you want the usage and costs for. The end date is exclusive. For example, if end is 2017-05-01 , AWS retrieves cost and usage data from the start date up to, but not including, 2017-05-01 .



NextToken (string) --
The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size.







Exceptions

CostExplorer.Client.exceptions.LimitExceededException
CostExplorer.Client.exceptions.DataUnavailableException
CostExplorer.Client.exceptions.InvalidNextTokenException


    :return: {
        'SavingsPlansUtilizationDetails': [
            {
                'SavingsPlanArn': 'string',
                'Attributes': {
                    'string': 'string'
                },
                'Utilization': {
                    'TotalCommitment': 'string',
                    'UsedCommitment': 'string',
                    'UnusedCommitment': 'string',
                    'UtilizationPercentage': 'string'
                },
                'Savings': {
                    'NetSavings': 'string',
                    'OnDemandCostEquivalent': 'string'
                },
                'AmortizedCommitment': {
                    'AmortizedRecurringCommitment': 'string',
                    'AmortizedUpfrontCommitment': 'string',
                    'TotalAmortizedCommitment': 'string'
                }
            },
        ],
        'Total': {
            'Utilization': {
                'TotalCommitment': 'string',
                'UsedCommitment': 'string',
                'UnusedCommitment': 'string',
                'UtilizationPercentage': 'string'
            },
            'Savings': {
                'NetSavings': 'string',
                'OnDemandCostEquivalent': 'string'
            },
            'AmortizedCommitment': {
                'AmortizedRecurringCommitment': 'string',
                'AmortizedUpfrontCommitment': 'string',
                'TotalAmortizedCommitment': 'string'
            }
        },
        'TimePeriod': {
            'Start': 'string',
            'End': 'string'
        },
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def get_tags(SearchString=None, TimePeriod=None, TagKey=None, NextPageToken=None):
    """
    Queries for available tag keys and tag values for a specified period. You can search the tag values for an arbitrary string.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_tags(
        SearchString='string',
        TimePeriod={
            'Start': 'string',
            'End': 'string'
        },
        TagKey='string',
        NextPageToken='string'
    )
    
    
    :type SearchString: string
    :param SearchString: The value that you want to search for.

    :type TimePeriod: dict
    :param TimePeriod: [REQUIRED]\nThe start and end dates for retrieving the dimension values. The start date is inclusive, but the end date is exclusive. For example, if start is 2017-01-01 and end is 2017-05-01 , then the cost and usage data is retrieved from 2017-01-01 up to and including 2017-04-30 but not including 2017-05-01 .\n\nStart (string) -- [REQUIRED]The beginning of the time period that you want the usage and costs for. The start date is inclusive. For example, if start is 2017-01-01 , AWS retrieves cost and usage data starting at 2017-01-01 up to the end date.\n\nEnd (string) -- [REQUIRED]The end of the time period that you want the usage and costs for. The end date is exclusive. For example, if end is 2017-05-01 , AWS retrieves cost and usage data from the start date up to, but not including, 2017-05-01 .\n\n\n

    :type TagKey: string
    :param TagKey: The key of the tag that you want to return values for.

    :type NextPageToken: string
    :param NextPageToken: The token to retrieve the next set of results. AWS provides the token when the response from a previous call has more results than the maximum page size.

    :rtype: dict

ReturnsResponse Syntax
{
    'NextPageToken': 'string',
    'Tags': [
        'string',
    ],
    'ReturnSize': 123,
    'TotalSize': 123
}


Response Structure

(dict) --

NextPageToken (string) --
The token for the next set of retrievable results. AWS provides the token when the response from a previous call has more results than the maximum page size.

Tags (list) --
The tags that match your request.

(string) --


ReturnSize (integer) --
The number of query results that AWS returns at a time.

TotalSize (integer) --
The total number of query results.







Exceptions

CostExplorer.Client.exceptions.LimitExceededException
CostExplorer.Client.exceptions.BillExpirationException
CostExplorer.Client.exceptions.DataUnavailableException
CostExplorer.Client.exceptions.InvalidNextTokenException
CostExplorer.Client.exceptions.RequestChangedException


    :return: {
        'NextPageToken': 'string',
        'Tags': [
            'string',
        ],
        'ReturnSize': 123,
        'TotalSize': 123
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_usage_forecast(TimePeriod=None, Metric=None, Granularity=None, Filter=None, PredictionIntervalLevel=None):
    """
    Retrieves a forecast for how much Amazon Web Services predicts that you will use over the forecast time period that you select, based on your past usage.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_usage_forecast(
        TimePeriod={
            'Start': 'string',
            'End': 'string'
        },
        Metric='BLENDED_COST'|'UNBLENDED_COST'|'AMORTIZED_COST'|'NET_UNBLENDED_COST'|'NET_AMORTIZED_COST'|'USAGE_QUANTITY'|'NORMALIZED_USAGE_AMOUNT',
        Granularity='DAILY'|'MONTHLY'|'HOURLY',
        Filter={
            'Or': [
                {'... recursive ...'},
            ],
            'And': [
                {'... recursive ...'},
            ],
            'Not': {'... recursive ...'},
            'Dimensions': {
                'Key': 'AZ'|'INSTANCE_TYPE'|'LINKED_ACCOUNT'|'LINKED_ACCOUNT_NAME'|'OPERATION'|'PURCHASE_TYPE'|'REGION'|'SERVICE'|'SERVICE_CODE'|'USAGE_TYPE'|'USAGE_TYPE_GROUP'|'RECORD_TYPE'|'OPERATING_SYSTEM'|'TENANCY'|'SCOPE'|'PLATFORM'|'SUBSCRIPTION_ID'|'LEGAL_ENTITY_NAME'|'DEPLOYMENT_OPTION'|'DATABASE_ENGINE'|'CACHE_ENGINE'|'INSTANCE_TYPE_FAMILY'|'BILLING_ENTITY'|'RESERVATION_ID'|'RESOURCE_ID'|'RIGHTSIZING_TYPE'|'SAVINGS_PLANS_TYPE'|'SAVINGS_PLAN_ARN'|'PAYMENT_OPTION',
                'Values': [
                    'string',
                ],
                'MatchOptions': [
                    'EQUALS'|'STARTS_WITH'|'ENDS_WITH'|'CONTAINS'|'CASE_SENSITIVE'|'CASE_INSENSITIVE',
                ]
            },
            'Tags': {
                'Key': 'string',
                'Values': [
                    'string',
                ],
                'MatchOptions': [
                    'EQUALS'|'STARTS_WITH'|'ENDS_WITH'|'CONTAINS'|'CASE_SENSITIVE'|'CASE_INSENSITIVE',
                ]
            },
            'CostCategories': {
                'Key': 'string',
                'Values': [
                    'string',
                ]
            }
        },
        PredictionIntervalLevel=123
    )
    
    
    :type TimePeriod: dict
    :param TimePeriod: [REQUIRED]\nThe start and end dates of the period that you want to retrieve usage forecast for. The start date is inclusive, but the end date is exclusive. For example, if start is 2017-01-01 and end is 2017-05-01 , then the cost and usage data is retrieved from 2017-01-01 up to and including 2017-04-30 but not including 2017-05-01 .\n\nStart (string) -- [REQUIRED]The beginning of the time period that you want the usage and costs for. The start date is inclusive. For example, if start is 2017-01-01 , AWS retrieves cost and usage data starting at 2017-01-01 up to the end date.\n\nEnd (string) -- [REQUIRED]The end of the time period that you want the usage and costs for. The end date is exclusive. For example, if end is 2017-05-01 , AWS retrieves cost and usage data from the start date up to, but not including, 2017-05-01 .\n\n\n

    :type Metric: string
    :param Metric: [REQUIRED]\nWhich metric Cost Explorer uses to create your forecast.\nValid values for a GetUsageForecast call are the following:\n\nUSAGE_QUANTITY\nNORMALIZED_USAGE_AMOUNT\n\n

    :type Granularity: string
    :param Granularity: [REQUIRED]\nHow granular you want the forecast to be. You can get 3 months of DAILY forecasts or 12 months of MONTHLY forecasts.\nThe GetUsageForecast operation supports only DAILY and MONTHLY granularities.\n

    :type Filter: dict
    :param Filter: The filters that you want to use to filter your forecast. Cost Explorer API supports all of the Cost Explorer filters.\n\nOr (list) --Return results that match either Dimension object.\n\n(dict) --Use Expression to filter by cost or by usage. There are two patterns:\n\nSimple dimension values - You can set the dimension name and values for the filters that you plan to use. For example, you can filter for REGION==us-east-1 OR REGION==us-west-1 . The Expression for that looks like this: { 'Dimensions': { 'Key': 'REGION', 'Values': [ 'us-east-1', \xe2\x80\x9cus-west-1\xe2\x80\x9d ] } }  The list of dimension values are OR\'d together to retrieve cost or usage data. You can create Expression and DimensionValues objects using either with* methods or set* methods in multiple lines.\nCompound dimension values with logical operations - You can use multiple Expression types and the logical operators AND/OR/NOT to create a list of one or more Expression objects. This allows you to filter on more advanced options. For example, you can filter on ((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE != DataTransfer) . The Expression for that looks like this: { 'And': [ {'Or': [ {'Dimensions': { 'Key': 'REGION', 'Values': [ 'us-east-1', 'us-west-1' ] }}, {'Tags': { 'Key': 'TagName', 'Values': ['Value1'] } } ]}, {'Not': {'Dimensions': { 'Key': 'USAGE_TYPE', 'Values': ['DataTransfer'] }}} ] }\n\n\nNote\n\nBecause each Expression can have only one operator, the service returns an error if more than one is specified. The following example shows an Expression object that creates an error.\n{ 'And': [ ... ], 'DimensionValues': { 'Dimension': 'USAGE_TYPE', 'Values': [ 'DataTransfer' ] } }\n\n\nNote\nFor GetRightsizingRecommendation action, a combination of OR and NOT is not supported. OR is not supported between different dimensions, or dimensions and tags. NOT operators aren\'t supported. Dimensions are also limited to LINKED_ACCOUNT , REGION , or RIGHTSIZING_TYPE .\n\n\n\n\nAnd (list) --Return results that match both Dimension objects.\n\n(dict) --Use Expression to filter by cost or by usage. There are two patterns:\n\nSimple dimension values - You can set the dimension name and values for the filters that you plan to use. For example, you can filter for REGION==us-east-1 OR REGION==us-west-1 . The Expression for that looks like this: { 'Dimensions': { 'Key': 'REGION', 'Values': [ 'us-east-1', \xe2\x80\x9cus-west-1\xe2\x80\x9d ] } }  The list of dimension values are OR\'d together to retrieve cost or usage data. You can create Expression and DimensionValues objects using either with* methods or set* methods in multiple lines.\nCompound dimension values with logical operations - You can use multiple Expression types and the logical operators AND/OR/NOT to create a list of one or more Expression objects. This allows you to filter on more advanced options. For example, you can filter on ((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE != DataTransfer) . The Expression for that looks like this: { 'And': [ {'Or': [ {'Dimensions': { 'Key': 'REGION', 'Values': [ 'us-east-1', 'us-west-1' ] }}, {'Tags': { 'Key': 'TagName', 'Values': ['Value1'] } } ]}, {'Not': {'Dimensions': { 'Key': 'USAGE_TYPE', 'Values': ['DataTransfer'] }}} ] }\n\n\nNote\n\nBecause each Expression can have only one operator, the service returns an error if more than one is specified. The following example shows an Expression object that creates an error.\n{ 'And': [ ... ], 'DimensionValues': { 'Dimension': 'USAGE_TYPE', 'Values': [ 'DataTransfer' ] } }\n\n\nNote\nFor GetRightsizingRecommendation action, a combination of OR and NOT is not supported. OR is not supported between different dimensions, or dimensions and tags. NOT operators aren\'t supported. Dimensions are also limited to LINKED_ACCOUNT , REGION , or RIGHTSIZING_TYPE .\n\n\n\n\nNot (dict) --Return results that don\'t match a Dimension object.\n\nDimensions (dict) --The specific Dimension to use for Expression .\n\nKey (string) --The names of the metadata types that you can use to filter and group your results. For example, AZ returns a list of Availability Zones.\n\nValues (list) --The metadata values that you can use to filter and group your results. You can use GetDimensionValues to find specific values.\n\n(string) --\n\n\nMatchOptions (list) --The match options that you can use to filter your results. MatchOptions is only applicable for actions related to Cost Category. The default values for MatchOptions is EQUALS and CASE_SENSITIVE .\n\n(string) --\n\n\n\n\nTags (dict) --The specific Tag to use for Expression .\n\nKey (string) --The key for the tag.\n\nValues (list) --The specific value of the tag.\n\n(string) --\n\n\nMatchOptions (list) --The match options that you can use to filter your results. MatchOptions is only applicable for only applicable for actions related to Cost Category. The default values for MatchOptions is EQUALS and CASE_SENSITIVE .\n\n(string) --\n\n\n\n\nCostCategories (dict) --The filter based on CostCategory values.\n\nKey (string) --The unique name of the Cost Category.\n\nValues (list) --The specific value of the Cost Category.\n\n(string) --\n\n\n\n\n\n

    :type PredictionIntervalLevel: integer
    :param PredictionIntervalLevel: Cost Explorer always returns the mean forecast as a single point. You can request a prediction interval around the mean by specifying a confidence level. The higher the confidence level, the more confident Cost Explorer is about the actual value falling in the prediction interval. Higher confidence levels result in wider prediction intervals.

    :rtype: dict

ReturnsResponse Syntax
{
    'Total': {
        'Amount': 'string',
        'Unit': 'string'
    },
    'ForecastResultsByTime': [
        {
            'TimePeriod': {
                'Start': 'string',
                'End': 'string'
            },
            'MeanValue': 'string',
            'PredictionIntervalLowerBound': 'string',
            'PredictionIntervalUpperBound': 'string'
        },
    ]
}


Response Structure

(dict) --

Total (dict) --
How much you\'re forecasted to use over the forecast period.

Amount (string) --
The actual number that represents the metric.

Unit (string) --
The unit that the metric is given in.



ForecastResultsByTime (list) --
The forecasts for your query, in order. For DAILY forecasts, this is a list of days. For MONTHLY forecasts, this is a list of months.

(dict) --
The forecast created for your query.

TimePeriod (dict) --
The period of time that the forecast covers.

Start (string) --
The beginning of the time period that you want the usage and costs for. The start date is inclusive. For example, if start is 2017-01-01 , AWS retrieves cost and usage data starting at 2017-01-01 up to the end date.

End (string) --
The end of the time period that you want the usage and costs for. The end date is exclusive. For example, if end is 2017-05-01 , AWS retrieves cost and usage data from the start date up to, but not including, 2017-05-01 .



MeanValue (string) --
The mean value of the forecast.

PredictionIntervalLowerBound (string) --
The lower limit for the prediction interval.

PredictionIntervalUpperBound (string) --
The upper limit for the prediction interval.











Exceptions

CostExplorer.Client.exceptions.LimitExceededException
CostExplorer.Client.exceptions.DataUnavailableException
CostExplorer.Client.exceptions.UnresolvableUsageUnitException


    :return: {
        'Total': {
            'Amount': 'string',
            'Unit': 'string'
        },
        'ForecastResultsByTime': [
            {
                'TimePeriod': {
                    'Start': 'string',
                    'End': 'string'
                },
                'MeanValue': 'string',
                'PredictionIntervalLowerBound': 'string',
                'PredictionIntervalUpperBound': 'string'
            },
        ]
    }
    
    
    :returns: 
    CostExplorer.Client.exceptions.LimitExceededException
    CostExplorer.Client.exceptions.DataUnavailableException
    CostExplorer.Client.exceptions.UnresolvableUsageUnitException
    
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

def list_cost_category_definitions(EffectiveOn=None, NextToken=None, MaxResults=None):
    """
    Returns the name, ARN, NumberOfRules and effective dates of all Cost Categories defined in the account. You have the option to use EffectiveOn to return a list of Cost Categories that were active on a specific date. If there is no EffectiveOn specified, you\xe2\x80\x99ll see Cost Categories that are effective on the current date. If Cost Category is still effective, EffectiveEnd is omitted in the response. ListCostCategoryDefinitions supports pagination. The request can have a MaxResults range up to 100.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_cost_category_definitions(
        EffectiveOn='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type EffectiveOn: string
    :param EffectiveOn: The date when the Cost Category was effective.

    :type NextToken: string
    :param NextToken: The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size.

    :type MaxResults: integer
    :param MaxResults: The number of entries a paginated response contains.

    :rtype: dict

ReturnsResponse Syntax
{
    'CostCategoryReferences': [
        {
            'CostCategoryArn': 'string',
            'Name': 'string',
            'EffectiveStart': 'string',
            'EffectiveEnd': 'string',
            'NumberOfRules': 123
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

CostCategoryReferences (list) --
A reference to a Cost Category containing enough information to identify the Cost Category.

(dict) --
A reference to a Cost Category containing only enough information to identify the Cost Category.
You can use this information to retrieve the full Cost Category information using DescribeCostCategory .

CostCategoryArn (string) --
The unique identifier for your Cost Category.

Name (string) --
The unique name of the Cost Category.

EffectiveStart (string) --
The Cost Category\'s effective start date.

EffectiveEnd (string) --
The Cost Category\'s effective end date.

NumberOfRules (integer) --
The number of rules associated with a specific Cost Category.





NextToken (string) --
The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size.







Exceptions

CostExplorer.Client.exceptions.LimitExceededException


    :return: {
        'CostCategoryReferences': [
            {
                'CostCategoryArn': 'string',
                'Name': 'string',
                'EffectiveStart': 'string',
                'EffectiveEnd': 'string',
                'NumberOfRules': 123
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    CostExplorer.Client.exceptions.LimitExceededException
    
    """
    pass

def update_cost_category_definition(CostCategoryArn=None, RuleVersion=None, Rules=None):
    """
    Updates an existing Cost Category. Changes made to the Cost Category rules will be used to categorize the current month\xe2\x80\x99s expenses and future expenses. This won\xe2\x80\x99t change categorization for the previous months.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_cost_category_definition(
        CostCategoryArn='string',
        RuleVersion='CostCategoryExpression.v1',
        Rules=[
            {
                'Value': 'string',
                'Rule': {
                    'Or': [
                        {'... recursive ...'},
                    ],
                    'And': [
                        {'... recursive ...'},
                    ],
                    'Not': {'... recursive ...'},
                    'Dimensions': {
                        'Key': 'AZ'|'INSTANCE_TYPE'|'LINKED_ACCOUNT'|'LINKED_ACCOUNT_NAME'|'OPERATION'|'PURCHASE_TYPE'|'REGION'|'SERVICE'|'SERVICE_CODE'|'USAGE_TYPE'|'USAGE_TYPE_GROUP'|'RECORD_TYPE'|'OPERATING_SYSTEM'|'TENANCY'|'SCOPE'|'PLATFORM'|'SUBSCRIPTION_ID'|'LEGAL_ENTITY_NAME'|'DEPLOYMENT_OPTION'|'DATABASE_ENGINE'|'CACHE_ENGINE'|'INSTANCE_TYPE_FAMILY'|'BILLING_ENTITY'|'RESERVATION_ID'|'RESOURCE_ID'|'RIGHTSIZING_TYPE'|'SAVINGS_PLANS_TYPE'|'SAVINGS_PLAN_ARN'|'PAYMENT_OPTION',
                        'Values': [
                            'string',
                        ],
                        'MatchOptions': [
                            'EQUALS'|'STARTS_WITH'|'ENDS_WITH'|'CONTAINS'|'CASE_SENSITIVE'|'CASE_INSENSITIVE',
                        ]
                    },
                    'Tags': {
                        'Key': 'string',
                        'Values': [
                            'string',
                        ],
                        'MatchOptions': [
                            'EQUALS'|'STARTS_WITH'|'ENDS_WITH'|'CONTAINS'|'CASE_SENSITIVE'|'CASE_INSENSITIVE',
                        ]
                    },
                    'CostCategories': {
                        'Key': 'string',
                        'Values': [
                            'string',
                        ]
                    }
                }
            },
        ]
    )
    
    
    :type CostCategoryArn: string
    :param CostCategoryArn: [REQUIRED]\nThe unique identifier for your Cost Category.\n

    :type RuleVersion: string
    :param RuleVersion: [REQUIRED]\nThe rule schema version in this particular Cost Category.\n

    :type Rules: list
    :param Rules: [REQUIRED]\nThe Expression object used to categorize costs. For more information, see CostCategoryRule .\n\n(dict) --Rules are processed in order. If there are multiple rules that match the line item, then the first rule to match is used to determine that Cost Category value.\n\nValue (string) -- [REQUIRED]The value a line item will be categorized as, if it matches the rule.\n\nRule (dict) -- [REQUIRED]An Expression object used to categorize costs. This supports dimensions, Tags, and nested expressions. Currently the only dimensions supported are LINKED_ACCOUNT , SERVICE_CODE , RECORD_TYPE , and LINKED_ACCOUNT_NAME .\nRoot level OR is not supported. We recommend that you create a separate rule instead.\n\nRECORD_TYPE is a dimension used for Cost Explorer APIs, and is also supported for Cost Category expressions. This dimension uses different terms, depending on whether you\'re using the console or API/JSON editor. For a detailed comparison, see Term Comparisons in the AWS Billing and Cost Management User Guide .\n\nOr (list) --Return results that match either Dimension object.\n\n(dict) --Use Expression to filter by cost or by usage. There are two patterns:\n\nSimple dimension values - You can set the dimension name and values for the filters that you plan to use. For example, you can filter for REGION==us-east-1 OR REGION==us-west-1 . The Expression for that looks like this: { 'Dimensions': { 'Key': 'REGION', 'Values': [ 'us-east-1', \xe2\x80\x9cus-west-1\xe2\x80\x9d ] } }  The list of dimension values are OR\'d together to retrieve cost or usage data. You can create Expression and DimensionValues objects using either with* methods or set* methods in multiple lines.\nCompound dimension values with logical operations - You can use multiple Expression types and the logical operators AND/OR/NOT to create a list of one or more Expression objects. This allows you to filter on more advanced options. For example, you can filter on ((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE != DataTransfer) . The Expression for that looks like this: { 'And': [ {'Or': [ {'Dimensions': { 'Key': 'REGION', 'Values': [ 'us-east-1', 'us-west-1' ] }}, {'Tags': { 'Key': 'TagName', 'Values': ['Value1'] } } ]}, {'Not': {'Dimensions': { 'Key': 'USAGE_TYPE', 'Values': ['DataTransfer'] }}} ] }\n\n\nNote\n\nBecause each Expression can have only one operator, the service returns an error if more than one is specified. The following example shows an Expression object that creates an error.\n{ 'And': [ ... ], 'DimensionValues': { 'Dimension': 'USAGE_TYPE', 'Values': [ 'DataTransfer' ] } }\n\n\nNote\nFor GetRightsizingRecommendation action, a combination of OR and NOT is not supported. OR is not supported between different dimensions, or dimensions and tags. NOT operators aren\'t supported. Dimensions are also limited to LINKED_ACCOUNT , REGION , or RIGHTSIZING_TYPE .\n\n\n\n\nAnd (list) --Return results that match both Dimension objects.\n\n(dict) --Use Expression to filter by cost or by usage. There are two patterns:\n\nSimple dimension values - You can set the dimension name and values for the filters that you plan to use. For example, you can filter for REGION==us-east-1 OR REGION==us-west-1 . The Expression for that looks like this: { 'Dimensions': { 'Key': 'REGION', 'Values': [ 'us-east-1', \xe2\x80\x9cus-west-1\xe2\x80\x9d ] } }  The list of dimension values are OR\'d together to retrieve cost or usage data. You can create Expression and DimensionValues objects using either with* methods or set* methods in multiple lines.\nCompound dimension values with logical operations - You can use multiple Expression types and the logical operators AND/OR/NOT to create a list of one or more Expression objects. This allows you to filter on more advanced options. For example, you can filter on ((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE != DataTransfer) . The Expression for that looks like this: { 'And': [ {'Or': [ {'Dimensions': { 'Key': 'REGION', 'Values': [ 'us-east-1', 'us-west-1' ] }}, {'Tags': { 'Key': 'TagName', 'Values': ['Value1'] } } ]}, {'Not': {'Dimensions': { 'Key': 'USAGE_TYPE', 'Values': ['DataTransfer'] }}} ] }\n\n\nNote\n\nBecause each Expression can have only one operator, the service returns an error if more than one is specified. The following example shows an Expression object that creates an error.\n{ 'And': [ ... ], 'DimensionValues': { 'Dimension': 'USAGE_TYPE', 'Values': [ 'DataTransfer' ] } }\n\n\nNote\nFor GetRightsizingRecommendation action, a combination of OR and NOT is not supported. OR is not supported between different dimensions, or dimensions and tags. NOT operators aren\'t supported. Dimensions are also limited to LINKED_ACCOUNT , REGION , or RIGHTSIZING_TYPE .\n\n\n\n\nNot (dict) --Return results that don\'t match a Dimension object.\n\nDimensions (dict) --The specific Dimension to use for Expression .\n\nKey (string) --The names of the metadata types that you can use to filter and group your results. For example, AZ returns a list of Availability Zones.\n\nValues (list) --The metadata values that you can use to filter and group your results. You can use GetDimensionValues to find specific values.\n\n(string) --\n\n\nMatchOptions (list) --The match options that you can use to filter your results. MatchOptions is only applicable for actions related to Cost Category. The default values for MatchOptions is EQUALS and CASE_SENSITIVE .\n\n(string) --\n\n\n\n\nTags (dict) --The specific Tag to use for Expression .\n\nKey (string) --The key for the tag.\n\nValues (list) --The specific value of the tag.\n\n(string) --\n\n\nMatchOptions (list) --The match options that you can use to filter your results. MatchOptions is only applicable for only applicable for actions related to Cost Category. The default values for MatchOptions is EQUALS and CASE_SENSITIVE .\n\n(string) --\n\n\n\n\nCostCategories (dict) --The filter based on CostCategory values.\n\nKey (string) --The unique name of the Cost Category.\n\nValues (list) --The specific value of the Cost Category.\n\n(string) --\n\n\n\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'CostCategoryArn': 'string',
    'EffectiveStart': 'string'
}


Response Structure

(dict) --

CostCategoryArn (string) --
The unique identifier for your Cost Category.

EffectiveStart (string) --
The Cost Category\'s effective start date.







Exceptions

CostExplorer.Client.exceptions.ResourceNotFoundException
CostExplorer.Client.exceptions.ServiceQuotaExceededException
CostExplorer.Client.exceptions.LimitExceededException


    :return: {
        'CostCategoryArn': 'string',
        'EffectiveStart': 'string'
    }
    
    
    :returns: 
    CostExplorer.Client.exceptions.ResourceNotFoundException
    CostExplorer.Client.exceptions.ServiceQuotaExceededException
    CostExplorer.Client.exceptions.LimitExceededException
    
    """
    pass

