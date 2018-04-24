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

def create_budget(AccountId=None, Budget=None, NotificationsWithSubscribers=None):
    """
    Creates a budget and, if included, notifications and subscribers.
    See also: AWS API Documentation
    
    
    :example: response = client.create_budget(
        AccountId='string',
        Budget={
            'BudgetName': 'string',
            'BudgetLimit': {
                'Amount': 'string',
                'Unit': 'string'
            },
            'CostFilters': {
                'string': [
                    'string',
                ]
            },
            'CostTypes': {
                'IncludeTax': True|False,
                'IncludeSubscription': True|False,
                'UseBlended': True|False,
                'IncludeRefund': True|False,
                'IncludeCredit': True|False,
                'IncludeUpfront': True|False,
                'IncludeRecurring': True|False,
                'IncludeOtherSubscription': True|False,
                'IncludeSupport': True|False,
                'IncludeDiscount': True|False,
                'UseAmortized': True|False
            },
            'TimeUnit': 'DAILY'|'MONTHLY'|'QUARTERLY'|'ANNUALLY',
            'TimePeriod': {
                'Start': datetime(2015, 1, 1),
                'End': datetime(2015, 1, 1)
            },
            'CalculatedSpend': {
                'ActualSpend': {
                    'Amount': 'string',
                    'Unit': 'string'
                },
                'ForecastedSpend': {
                    'Amount': 'string',
                    'Unit': 'string'
                }
            },
            'BudgetType': 'USAGE'|'COST'|'RI_UTILIZATION'
        },
        NotificationsWithSubscribers=[
            {
                'Notification': {
                    'NotificationType': 'ACTUAL'|'FORECASTED',
                    'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
                    'Threshold': 123.0,
                    'ThresholdType': 'PERCENTAGE'|'ABSOLUTE_VALUE'
                },
                'Subscribers': [
                    {
                        'SubscriptionType': 'SNS'|'EMAIL',
                        'Address': 'string'
                    },
                ]
            },
        ]
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]
            The accountId that is associated with the budget.
            

    :type Budget: dict
    :param Budget: [REQUIRED]
            The budget object that you want to create.
            BudgetName (string) -- [REQUIRED]The name of a budget. Unique within accounts. : and \ characters are not allowed in the BudgetName .
            BudgetLimit (dict) --The total amount of cost, usage, or RI utilization that you want to track with your budget.
            BudgetLimit is required for cost or usage budgets, but optional for RI utilization budgets. RI utilization budgets default to the only valid value for RI utilization budgets, which is 100 .
            Amount (string) -- [REQUIRED]The cost or usage amount associated with a budget forecast, actual spend, or budget threshold.
            Unit (string) -- [REQUIRED]The unit of measurement used for the budget forecast, actual spend, or budget threshold, such as dollars or GB.
            CostFilters (dict) --The cost filters applied to a budget, such as service or region.
            (string) --A generic String.
            (list) --
            (string) --A generic String.
            
            CostTypes (dict) --The types of costs included in this budget.
            IncludeTax (boolean) --Specifies whether a budget includes taxes.
            The default value is true .
            IncludeSubscription (boolean) --Specifies whether a budget includes subscriptions.
            The default value is true .
            UseBlended (boolean) --Specifies whether a budget uses blended rate.
            The default value is false .
            IncludeRefund (boolean) --Specifies whether a budget includes refunds.
            The default value is true .
            IncludeCredit (boolean) --Specifies whether a budget includes credits.
            The default value is true .
            IncludeUpfront (boolean) --Specifies whether a budget includes upfront RI costs.
            The default value is true .
            IncludeRecurring (boolean) --Specifies whether a budget includes recurring fees such as monthly RI fees.
            The default value is true .
            IncludeOtherSubscription (boolean) --Specifies whether a budget includes non-RI subscription costs.
            The default value is true .
            IncludeSupport (boolean) --Specifies whether a budget includes support subscription fees.
            The default value is true .
            IncludeDiscount (boolean) --Specifies whether a budget includes discounts.
            The default value is true .
            UseAmortized (boolean) --Specifies whether a budget uses the amortized rate.
            The default value is false .
            TimeUnit (string) -- [REQUIRED]The length of time until a budget resets the actual and forecasted spend.
            TimePeriod (dict) --The period of time covered by a budget. Has a start date and an end date. The start date must come before the end date. There are no restrictions on the end date.
            If you created your budget and didn't specify a start date, AWS defaults to the start of your chosen time period (i.e. DAILY, MONTHLY, QUARTERLY, ANNUALLY). For example, if you created your budget on January 24th 2018, chose DAILY , and didn't set a start date, AWS set your start date to 01/24/18 00:00 UTC . If you chose MONTHLY , AWS set your start date to 01/01/18 00:00 UTC . If you didn't specify an end date, AWS set your end date to 06/15/87 00:00 UTC . The defaults are the same for the AWS Billing and Cost Management console and the API.
            You can change either date with the UpdateBudget operation.
            After the end date, AWS deletes the budget and all associated notifications and subscribers.
            Start (datetime) --The start date for a budget. If you created your budget and didn't specify a start date, AWS defaults to the start of your chosen time period (i.e. DAILY, MONTHLY, QUARTERLY, ANNUALLY). For example, if you created your budget on January 24th 2018, chose DAILY , and didn't set a start date, AWS set your start date to 01/24/18 00:00 UTC . If you chose MONTHLY , AWS set your start date to 01/01/18 00:00 UTC . The defaults are the same for the AWS Billing and Cost Management console and the API.
            You can change your start date with the UpdateBudget operation.
            End (datetime) --The end date for a budget. If you didn't specify an end date, AWS set your end date to 06/15/87 00:00 UTC . The defaults are the same for the AWS Billing and Cost Management console and the API.
            After the end date, AWS deletes the budget and all associated notifications and subscribers. You can change your end date with the UpdateBudget operation.
            CalculatedSpend (dict) --The actual and forecasted cost or usage being tracked by a budget.
            ActualSpend (dict) -- [REQUIRED]The amount of cost, usage, or RI units that you have used.
            Amount (string) -- [REQUIRED]The cost or usage amount associated with a budget forecast, actual spend, or budget threshold.
            Unit (string) -- [REQUIRED]The unit of measurement used for the budget forecast, actual spend, or budget threshold, such as dollars or GB.
            ForecastedSpend (dict) --The amount of cost, usage, or RI units that you are forecasted to use.
            Amount (string) -- [REQUIRED]The cost or usage amount associated with a budget forecast, actual spend, or budget threshold.
            Unit (string) -- [REQUIRED]The unit of measurement used for the budget forecast, actual spend, or budget threshold, such as dollars or GB.
            
            BudgetType (string) -- [REQUIRED]Whether this budget tracks monetary costs, usage, or RI utilization.
            

    :type NotificationsWithSubscribers: list
    :param NotificationsWithSubscribers: A notification that you want to associate with a budget. A budget can have up to five notifications, and each notification can have one SNS subscriber and up to ten email subscribers. If you include notifications and subscribers in your CreateBudget call, AWS creates the notifications and subscribers for you.
            (dict) --A notification with subscribers. A notification can have one SNS subscriber and up to ten email subscribers, for a total of 11 subscribers.
            Notification (dict) -- [REQUIRED]The notification associated with a budget.
            NotificationType (string) -- [REQUIRED]Whether the notification is for how much you have spent (ACTUAL ) or for how much you are forecasted to spend (FORECASTED ).
            ComparisonOperator (string) -- [REQUIRED]The comparison used for this notification.
            Threshold (float) -- [REQUIRED]The threshold associated with a notification. Thresholds are always a percentage.
            ThresholdType (string) --The type of threshold for a notification. For ACTUAL thresholds, AWS notifies you when you go over the threshold, and for FORECASTED thresholds AWS notifies you when you are forecasted to go over the threshold.
            Subscribers (list) -- [REQUIRED]A list of subscribers who are subscribed to this notification.
            (dict) --The subscriber to a budget notification. The subscriber consists of a subscription type and either an Amazon Simple Notification Service topic or an email address.
            For example, an email subscriber would have the following parameters:
            A subscriptionType of EMAIL
            An address of example@example.com
            SubscriptionType (string) -- [REQUIRED]The type of notification that AWS sends to a subscriber.
            Address (string) -- [REQUIRED]The address that AWS sends budget notifications to, either an SNS topic or an email.
            
            
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def create_notification(AccountId=None, BudgetName=None, Notification=None, Subscribers=None):
    """
    Creates a notification. You must create the budget before you create the associated notification.
    See also: AWS API Documentation
    
    
    :example: response = client.create_notification(
        AccountId='string',
        BudgetName='string',
        Notification={
            'NotificationType': 'ACTUAL'|'FORECASTED',
            'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
            'Threshold': 123.0,
            'ThresholdType': 'PERCENTAGE'|'ABSOLUTE_VALUE'
        },
        Subscribers=[
            {
                'SubscriptionType': 'SNS'|'EMAIL',
                'Address': 'string'
            },
        ]
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]
            The accountId that is associated with the budget that you want to create a notification for.
            

    :type BudgetName: string
    :param BudgetName: [REQUIRED]
            The name of the budget that you want AWS to notified you about. Budget names must be unique within an account.
            

    :type Notification: dict
    :param Notification: [REQUIRED]
            The notification that you want to create.
            NotificationType (string) -- [REQUIRED]Whether the notification is for how much you have spent (ACTUAL ) or for how much you are forecasted to spend (FORECASTED ).
            ComparisonOperator (string) -- [REQUIRED]The comparison used for this notification.
            Threshold (float) -- [REQUIRED]The threshold associated with a notification. Thresholds are always a percentage.
            ThresholdType (string) --The type of threshold for a notification. For ACTUAL thresholds, AWS notifies you when you go over the threshold, and for FORECASTED thresholds AWS notifies you when you are forecasted to go over the threshold.
            

    :type Subscribers: list
    :param Subscribers: [REQUIRED]
            A list of subscribers that you want to associate with the notification. Each notification can have one SNS subscriber and up to ten email subscribers.
            (dict) --The subscriber to a budget notification. The subscriber consists of a subscription type and either an Amazon Simple Notification Service topic or an email address.
            For example, an email subscriber would have the following parameters:
            A subscriptionType of EMAIL
            An address of example@example.com
            SubscriptionType (string) -- [REQUIRED]The type of notification that AWS sends to a subscriber.
            Address (string) -- [REQUIRED]The address that AWS sends budget notifications to, either an SNS topic or an email.
            
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def create_subscriber(AccountId=None, BudgetName=None, Notification=None, Subscriber=None):
    """
    Creates a subscriber. You must create the associated budget and notification before you create the subscriber.
    See also: AWS API Documentation
    
    
    :example: response = client.create_subscriber(
        AccountId='string',
        BudgetName='string',
        Notification={
            'NotificationType': 'ACTUAL'|'FORECASTED',
            'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
            'Threshold': 123.0,
            'ThresholdType': 'PERCENTAGE'|'ABSOLUTE_VALUE'
        },
        Subscriber={
            'SubscriptionType': 'SNS'|'EMAIL',
            'Address': 'string'
        }
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]
            The accountId associated with the budget that you want to create a subscriber for.
            

    :type BudgetName: string
    :param BudgetName: [REQUIRED]
            The name of the budget that you want to subscribe to. Budget names must be unique within an account.
            

    :type Notification: dict
    :param Notification: [REQUIRED]
            The notification that you want to create a subscriber for.
            NotificationType (string) -- [REQUIRED]Whether the notification is for how much you have spent (ACTUAL ) or for how much you are forecasted to spend (FORECASTED ).
            ComparisonOperator (string) -- [REQUIRED]The comparison used for this notification.
            Threshold (float) -- [REQUIRED]The threshold associated with a notification. Thresholds are always a percentage.
            ThresholdType (string) --The type of threshold for a notification. For ACTUAL thresholds, AWS notifies you when you go over the threshold, and for FORECASTED thresholds AWS notifies you when you are forecasted to go over the threshold.
            

    :type Subscriber: dict
    :param Subscriber: [REQUIRED]
            The subscriber that you want to associate with a budget notification.
            SubscriptionType (string) -- [REQUIRED]The type of notification that AWS sends to a subscriber.
            Address (string) -- [REQUIRED]The address that AWS sends budget notifications to, either an SNS topic or an email.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_budget(AccountId=None, BudgetName=None):
    """
    Deletes a budget. You can delete your budget at any time.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_budget(
        AccountId='string',
        BudgetName='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]
            The accountId that is associated with the budget that you want to delete.
            

    :type BudgetName: string
    :param BudgetName: [REQUIRED]
            The name of the budget that you want to delete.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_notification(AccountId=None, BudgetName=None, Notification=None):
    """
    Deletes a notification.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_notification(
        AccountId='string',
        BudgetName='string',
        Notification={
            'NotificationType': 'ACTUAL'|'FORECASTED',
            'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
            'Threshold': 123.0,
            'ThresholdType': 'PERCENTAGE'|'ABSOLUTE_VALUE'
        }
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]
            The accountId that is associated with the budget whose notification you want to delete.
            

    :type BudgetName: string
    :param BudgetName: [REQUIRED]
            The name of the budget whose notification you want to delete.
            

    :type Notification: dict
    :param Notification: [REQUIRED]
            The notification that you want to delete.
            NotificationType (string) -- [REQUIRED]Whether the notification is for how much you have spent (ACTUAL ) or for how much you are forecasted to spend (FORECASTED ).
            ComparisonOperator (string) -- [REQUIRED]The comparison used for this notification.
            Threshold (float) -- [REQUIRED]The threshold associated with a notification. Thresholds are always a percentage.
            ThresholdType (string) --The type of threshold for a notification. For ACTUAL thresholds, AWS notifies you when you go over the threshold, and for FORECASTED thresholds AWS notifies you when you are forecasted to go over the threshold.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_subscriber(AccountId=None, BudgetName=None, Notification=None, Subscriber=None):
    """
    Deletes a subscriber.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_subscriber(
        AccountId='string',
        BudgetName='string',
        Notification={
            'NotificationType': 'ACTUAL'|'FORECASTED',
            'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
            'Threshold': 123.0,
            'ThresholdType': 'PERCENTAGE'|'ABSOLUTE_VALUE'
        },
        Subscriber={
            'SubscriptionType': 'SNS'|'EMAIL',
            'Address': 'string'
        }
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]
            The accountId that is associated with the budget whose subscriber you want to delete.
            

    :type BudgetName: string
    :param BudgetName: [REQUIRED]
            The name of the budget whose subscriber you want to delete.
            

    :type Notification: dict
    :param Notification: [REQUIRED]
            The notification whose subscriber you want to delete.
            NotificationType (string) -- [REQUIRED]Whether the notification is for how much you have spent (ACTUAL ) or for how much you are forecasted to spend (FORECASTED ).
            ComparisonOperator (string) -- [REQUIRED]The comparison used for this notification.
            Threshold (float) -- [REQUIRED]The threshold associated with a notification. Thresholds are always a percentage.
            ThresholdType (string) --The type of threshold for a notification. For ACTUAL thresholds, AWS notifies you when you go over the threshold, and for FORECASTED thresholds AWS notifies you when you are forecasted to go over the threshold.
            

    :type Subscriber: dict
    :param Subscriber: [REQUIRED]
            The subscriber that you want to delete.
            SubscriptionType (string) -- [REQUIRED]The type of notification that AWS sends to a subscriber.
            Address (string) -- [REQUIRED]The address that AWS sends budget notifications to, either an SNS topic or an email.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def describe_budget(AccountId=None, BudgetName=None):
    """
    Describes a budget.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_budget(
        AccountId='string',
        BudgetName='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]
            The accountId that is associated with the budget that you want a description of.
            

    :type BudgetName: string
    :param BudgetName: [REQUIRED]
            The name of the budget that you want a description of.
            

    :rtype: dict
    :return: {
        'Budget': {
            'BudgetName': 'string',
            'BudgetLimit': {
                'Amount': 'string',
                'Unit': 'string'
            },
            'CostFilters': {
                'string': [
                    'string',
                ]
            },
            'CostTypes': {
                'IncludeTax': True|False,
                'IncludeSubscription': True|False,
                'UseBlended': True|False,
                'IncludeRefund': True|False,
                'IncludeCredit': True|False,
                'IncludeUpfront': True|False,
                'IncludeRecurring': True|False,
                'IncludeOtherSubscription': True|False,
                'IncludeSupport': True|False,
                'IncludeDiscount': True|False,
                'UseAmortized': True|False
            },
            'TimeUnit': 'DAILY'|'MONTHLY'|'QUARTERLY'|'ANNUALLY',
            'TimePeriod': {
                'Start': datetime(2015, 1, 1),
                'End': datetime(2015, 1, 1)
            },
            'CalculatedSpend': {
                'ActualSpend': {
                    'Amount': 'string',
                    'Unit': 'string'
                },
                'ForecastedSpend': {
                    'Amount': 'string',
                    'Unit': 'string'
                }
            },
            'BudgetType': 'USAGE'|'COST'|'RI_UTILIZATION'
        }
    }
    
    
    """
    pass

def describe_budgets(AccountId=None, MaxResults=None, NextToken=None):
    """
    Lists the budgets associated with an account.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_budgets(
        AccountId='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]
            The accountId that is associated with the budgets that you want descriptions of.
            

    :type MaxResults: integer
    :param MaxResults: Optional integer. Specifies the maximum number of results to return in response.

    :type NextToken: string
    :param NextToken: The pagination token that indicates the next set of results to retrieve.

    :rtype: dict
    :return: {
        'Budgets': [
            {
                'BudgetName': 'string',
                'BudgetLimit': {
                    'Amount': 'string',
                    'Unit': 'string'
                },
                'CostFilters': {
                    'string': [
                        'string',
                    ]
                },
                'CostTypes': {
                    'IncludeTax': True|False,
                    'IncludeSubscription': True|False,
                    'UseBlended': True|False,
                    'IncludeRefund': True|False,
                    'IncludeCredit': True|False,
                    'IncludeUpfront': True|False,
                    'IncludeRecurring': True|False,
                    'IncludeOtherSubscription': True|False,
                    'IncludeSupport': True|False,
                    'IncludeDiscount': True|False,
                    'UseAmortized': True|False
                },
                'TimeUnit': 'DAILY'|'MONTHLY'|'QUARTERLY'|'ANNUALLY',
                'TimePeriod': {
                    'Start': datetime(2015, 1, 1),
                    'End': datetime(2015, 1, 1)
                },
                'CalculatedSpend': {
                    'ActualSpend': {
                        'Amount': 'string',
                        'Unit': 'string'
                    },
                    'ForecastedSpend': {
                        'Amount': 'string',
                        'Unit': 'string'
                    }
                },
                'BudgetType': 'USAGE'|'COST'|'RI_UTILIZATION'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def describe_notifications_for_budget(AccountId=None, BudgetName=None, MaxResults=None, NextToken=None):
    """
    Lists the notifications associated with a budget.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_notifications_for_budget(
        AccountId='string',
        BudgetName='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]
            The accountId that is associated with the budget whose notifications you want descriptions of.
            

    :type BudgetName: string
    :param BudgetName: [REQUIRED]
            The name of the budget whose notifications you want descriptions of.
            

    :type MaxResults: integer
    :param MaxResults: Optional integer. Specifies the maximum number of results to return in response.

    :type NextToken: string
    :param NextToken: The pagination token that indicates the next set of results to retrieve.

    :rtype: dict
    :return: {
        'Notifications': [
            {
                'NotificationType': 'ACTUAL'|'FORECASTED',
                'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
                'Threshold': 123.0,
                'ThresholdType': 'PERCENTAGE'|'ABSOLUTE_VALUE'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    A notificationType of ACTUAL
    A comparisonOperator of GREATER_THAN
    A notification threshold of 80
    
    """
    pass

def describe_subscribers_for_notification(AccountId=None, BudgetName=None, Notification=None, MaxResults=None, NextToken=None):
    """
    Lists the subscribers associated with a notification.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_subscribers_for_notification(
        AccountId='string',
        BudgetName='string',
        Notification={
            'NotificationType': 'ACTUAL'|'FORECASTED',
            'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
            'Threshold': 123.0,
            'ThresholdType': 'PERCENTAGE'|'ABSOLUTE_VALUE'
        },
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]
            The accountId that is associated with the budget whose subscribers you want descriptions of.
            

    :type BudgetName: string
    :param BudgetName: [REQUIRED]
            The name of the budget whose subscribers you want descriptions of.
            

    :type Notification: dict
    :param Notification: [REQUIRED]
            The notification whose subscribers you want to list.
            NotificationType (string) -- [REQUIRED]Whether the notification is for how much you have spent (ACTUAL ) or for how much you are forecasted to spend (FORECASTED ).
            ComparisonOperator (string) -- [REQUIRED]The comparison used for this notification.
            Threshold (float) -- [REQUIRED]The threshold associated with a notification. Thresholds are always a percentage.
            ThresholdType (string) --The type of threshold for a notification. For ACTUAL thresholds, AWS notifies you when you go over the threshold, and for FORECASTED thresholds AWS notifies you when you are forecasted to go over the threshold.
            

    :type MaxResults: integer
    :param MaxResults: Optional integer. Specifies the maximum number of results to return in response.

    :type NextToken: string
    :param NextToken: The pagination token that indicates the next set of results to retrieve.

    :rtype: dict
    :return: {
        'Subscribers': [
            {
                'SubscriptionType': 'SNS'|'EMAIL',
                'Address': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    A subscriptionType of EMAIL
    An address of example@example.com
    
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

def get_waiter():
    """
    
    """
    pass

def update_budget(AccountId=None, NewBudget=None):
    """
    Updates a budget. You can change every part of a budget except for the budgetName and the calculatedSpend . When a budget is modified, the calculatedSpend drops to zero until AWS has new usage data to use for forecasting.
    See also: AWS API Documentation
    
    
    :example: response = client.update_budget(
        AccountId='string',
        NewBudget={
            'BudgetName': 'string',
            'BudgetLimit': {
                'Amount': 'string',
                'Unit': 'string'
            },
            'CostFilters': {
                'string': [
                    'string',
                ]
            },
            'CostTypes': {
                'IncludeTax': True|False,
                'IncludeSubscription': True|False,
                'UseBlended': True|False,
                'IncludeRefund': True|False,
                'IncludeCredit': True|False,
                'IncludeUpfront': True|False,
                'IncludeRecurring': True|False,
                'IncludeOtherSubscription': True|False,
                'IncludeSupport': True|False,
                'IncludeDiscount': True|False,
                'UseAmortized': True|False
            },
            'TimeUnit': 'DAILY'|'MONTHLY'|'QUARTERLY'|'ANNUALLY',
            'TimePeriod': {
                'Start': datetime(2015, 1, 1),
                'End': datetime(2015, 1, 1)
            },
            'CalculatedSpend': {
                'ActualSpend': {
                    'Amount': 'string',
                    'Unit': 'string'
                },
                'ForecastedSpend': {
                    'Amount': 'string',
                    'Unit': 'string'
                }
            },
            'BudgetType': 'USAGE'|'COST'|'RI_UTILIZATION'
        }
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]
            The accountId that is associated with the budget that you want to update.
            

    :type NewBudget: dict
    :param NewBudget: [REQUIRED]
            The budget that you want to update your budget to.
            BudgetName (string) -- [REQUIRED]The name of a budget. Unique within accounts. : and \ characters are not allowed in the BudgetName .
            BudgetLimit (dict) --The total amount of cost, usage, or RI utilization that you want to track with your budget.
            BudgetLimit is required for cost or usage budgets, but optional for RI utilization budgets. RI utilization budgets default to the only valid value for RI utilization budgets, which is 100 .
            Amount (string) -- [REQUIRED]The cost or usage amount associated with a budget forecast, actual spend, or budget threshold.
            Unit (string) -- [REQUIRED]The unit of measurement used for the budget forecast, actual spend, or budget threshold, such as dollars or GB.
            CostFilters (dict) --The cost filters applied to a budget, such as service or region.
            (string) --A generic String.
            (list) --
            (string) --A generic String.
            
            CostTypes (dict) --The types of costs included in this budget.
            IncludeTax (boolean) --Specifies whether a budget includes taxes.
            The default value is true .
            IncludeSubscription (boolean) --Specifies whether a budget includes subscriptions.
            The default value is true .
            UseBlended (boolean) --Specifies whether a budget uses blended rate.
            The default value is false .
            IncludeRefund (boolean) --Specifies whether a budget includes refunds.
            The default value is true .
            IncludeCredit (boolean) --Specifies whether a budget includes credits.
            The default value is true .
            IncludeUpfront (boolean) --Specifies whether a budget includes upfront RI costs.
            The default value is true .
            IncludeRecurring (boolean) --Specifies whether a budget includes recurring fees such as monthly RI fees.
            The default value is true .
            IncludeOtherSubscription (boolean) --Specifies whether a budget includes non-RI subscription costs.
            The default value is true .
            IncludeSupport (boolean) --Specifies whether a budget includes support subscription fees.
            The default value is true .
            IncludeDiscount (boolean) --Specifies whether a budget includes discounts.
            The default value is true .
            UseAmortized (boolean) --Specifies whether a budget uses the amortized rate.
            The default value is false .
            TimeUnit (string) -- [REQUIRED]The length of time until a budget resets the actual and forecasted spend.
            TimePeriod (dict) --The period of time covered by a budget. Has a start date and an end date. The start date must come before the end date. There are no restrictions on the end date.
            If you created your budget and didn't specify a start date, AWS defaults to the start of your chosen time period (i.e. DAILY, MONTHLY, QUARTERLY, ANNUALLY). For example, if you created your budget on January 24th 2018, chose DAILY , and didn't set a start date, AWS set your start date to 01/24/18 00:00 UTC . If you chose MONTHLY , AWS set your start date to 01/01/18 00:00 UTC . If you didn't specify an end date, AWS set your end date to 06/15/87 00:00 UTC . The defaults are the same for the AWS Billing and Cost Management console and the API.
            You can change either date with the UpdateBudget operation.
            After the end date, AWS deletes the budget and all associated notifications and subscribers.
            Start (datetime) --The start date for a budget. If you created your budget and didn't specify a start date, AWS defaults to the start of your chosen time period (i.e. DAILY, MONTHLY, QUARTERLY, ANNUALLY). For example, if you created your budget on January 24th 2018, chose DAILY , and didn't set a start date, AWS set your start date to 01/24/18 00:00 UTC . If you chose MONTHLY , AWS set your start date to 01/01/18 00:00 UTC . The defaults are the same for the AWS Billing and Cost Management console and the API.
            You can change your start date with the UpdateBudget operation.
            End (datetime) --The end date for a budget. If you didn't specify an end date, AWS set your end date to 06/15/87 00:00 UTC . The defaults are the same for the AWS Billing and Cost Management console and the API.
            After the end date, AWS deletes the budget and all associated notifications and subscribers. You can change your end date with the UpdateBudget operation.
            CalculatedSpend (dict) --The actual and forecasted cost or usage being tracked by a budget.
            ActualSpend (dict) -- [REQUIRED]The amount of cost, usage, or RI units that you have used.
            Amount (string) -- [REQUIRED]The cost or usage amount associated with a budget forecast, actual spend, or budget threshold.
            Unit (string) -- [REQUIRED]The unit of measurement used for the budget forecast, actual spend, or budget threshold, such as dollars or GB.
            ForecastedSpend (dict) --The amount of cost, usage, or RI units that you are forecasted to use.
            Amount (string) -- [REQUIRED]The cost or usage amount associated with a budget forecast, actual spend, or budget threshold.
            Unit (string) -- [REQUIRED]The unit of measurement used for the budget forecast, actual spend, or budget threshold, such as dollars or GB.
            
            BudgetType (string) -- [REQUIRED]Whether this budget tracks monetary costs, usage, or RI utilization.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def update_notification(AccountId=None, BudgetName=None, OldNotification=None, NewNotification=None):
    """
    Updates a notification.
    See also: AWS API Documentation
    
    
    :example: response = client.update_notification(
        AccountId='string',
        BudgetName='string',
        OldNotification={
            'NotificationType': 'ACTUAL'|'FORECASTED',
            'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
            'Threshold': 123.0,
            'ThresholdType': 'PERCENTAGE'|'ABSOLUTE_VALUE'
        },
        NewNotification={
            'NotificationType': 'ACTUAL'|'FORECASTED',
            'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
            'Threshold': 123.0,
            'ThresholdType': 'PERCENTAGE'|'ABSOLUTE_VALUE'
        }
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]
            The accountId that is associated with the budget whose notification you want to update.
            

    :type BudgetName: string
    :param BudgetName: [REQUIRED]
            The name of the budget whose notification you want to update.
            

    :type OldNotification: dict
    :param OldNotification: [REQUIRED]
            The previous notification associated with a budget.
            NotificationType (string) -- [REQUIRED]Whether the notification is for how much you have spent (ACTUAL ) or for how much you are forecasted to spend (FORECASTED ).
            ComparisonOperator (string) -- [REQUIRED]The comparison used for this notification.
            Threshold (float) -- [REQUIRED]The threshold associated with a notification. Thresholds are always a percentage.
            ThresholdType (string) --The type of threshold for a notification. For ACTUAL thresholds, AWS notifies you when you go over the threshold, and for FORECASTED thresholds AWS notifies you when you are forecasted to go over the threshold.
            

    :type NewNotification: dict
    :param NewNotification: [REQUIRED]
            The updated notification to be associated with a budget.
            NotificationType (string) -- [REQUIRED]Whether the notification is for how much you have spent (ACTUAL ) or for how much you are forecasted to spend (FORECASTED ).
            ComparisonOperator (string) -- [REQUIRED]The comparison used for this notification.
            Threshold (float) -- [REQUIRED]The threshold associated with a notification. Thresholds are always a percentage.
            ThresholdType (string) --The type of threshold for a notification. For ACTUAL thresholds, AWS notifies you when you go over the threshold, and for FORECASTED thresholds AWS notifies you when you are forecasted to go over the threshold.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def update_subscriber(AccountId=None, BudgetName=None, Notification=None, OldSubscriber=None, NewSubscriber=None):
    """
    Updates a subscriber.
    See also: AWS API Documentation
    
    
    :example: response = client.update_subscriber(
        AccountId='string',
        BudgetName='string',
        Notification={
            'NotificationType': 'ACTUAL'|'FORECASTED',
            'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
            'Threshold': 123.0,
            'ThresholdType': 'PERCENTAGE'|'ABSOLUTE_VALUE'
        },
        OldSubscriber={
            'SubscriptionType': 'SNS'|'EMAIL',
            'Address': 'string'
        },
        NewSubscriber={
            'SubscriptionType': 'SNS'|'EMAIL',
            'Address': 'string'
        }
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]
            The accountId that is associated with the budget whose subscriber you want to update.
            

    :type BudgetName: string
    :param BudgetName: [REQUIRED]
            The name of the budget whose subscriber you want to update.
            

    :type Notification: dict
    :param Notification: [REQUIRED]
            The notification whose subscriber you want to update.
            NotificationType (string) -- [REQUIRED]Whether the notification is for how much you have spent (ACTUAL ) or for how much you are forecasted to spend (FORECASTED ).
            ComparisonOperator (string) -- [REQUIRED]The comparison used for this notification.
            Threshold (float) -- [REQUIRED]The threshold associated with a notification. Thresholds are always a percentage.
            ThresholdType (string) --The type of threshold for a notification. For ACTUAL thresholds, AWS notifies you when you go over the threshold, and for FORECASTED thresholds AWS notifies you when you are forecasted to go over the threshold.
            

    :type OldSubscriber: dict
    :param OldSubscriber: [REQUIRED]
            The previous subscriber associated with a budget notification.
            SubscriptionType (string) -- [REQUIRED]The type of notification that AWS sends to a subscriber.
            Address (string) -- [REQUIRED]The address that AWS sends budget notifications to, either an SNS topic or an email.
            

    :type NewSubscriber: dict
    :param NewSubscriber: [REQUIRED]
            The updated subscriber associated with a budget notification.
            SubscriptionType (string) -- [REQUIRED]The type of notification that AWS sends to a subscriber.
            Address (string) -- [REQUIRED]The address that AWS sends budget notifications to, either an SNS topic or an email.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

