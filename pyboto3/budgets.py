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

def create_budget(AccountId=None, Budget=None, NotificationsWithSubscribers=None):
    """
    Creates a budget and, if included, notifications and subscribers.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_budget(
        AccountId='string',
        Budget={
            'BudgetName': 'string',
            'BudgetLimit': {
                'Amount': 'string',
                'Unit': 'string'
            },
            'PlannedBudgetLimits': {
                'string': {
                    'Amount': 'string',
                    'Unit': 'string'
                }
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
            'BudgetType': 'USAGE'|'COST'|'RI_UTILIZATION'|'RI_COVERAGE'|'SAVINGS_PLANS_UTILIZATION'|'SAVINGS_PLANS_COVERAGE',
            'LastUpdatedTime': datetime(2015, 1, 1)
        },
        NotificationsWithSubscribers=[
            {
                'Notification': {
                    'NotificationType': 'ACTUAL'|'FORECASTED',
                    'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
                    'Threshold': 123.0,
                    'ThresholdType': 'PERCENTAGE'|'ABSOLUTE_VALUE',
                    'NotificationState': 'OK'|'ALARM'
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
    :param AccountId: [REQUIRED]\nThe accountId that is associated with the budget.\n

    :type Budget: dict
    :param Budget: [REQUIRED]\nThe budget object that you want to create.\n\nBudgetName (string) -- [REQUIRED]The name of a budget. The name must be unique within an account. The : and \\ characters aren\'t allowed in BudgetName .\n\nBudgetLimit (dict) --The total amount of cost, usage, RI utilization, RI coverage, Savings Plans utilization, or Savings Plans coverage that you want to track with your budget.\n\nBudgetLimit is required for cost or usage budgets, but optional for RI or Savings Plans utilization or coverage budgets. RI and Savings Plans utilization or coverage budgets default to 100 , which is the only valid value for RI or Savings Plans utilization or coverage budgets. You can\'t use BudgetLimit with PlannedBudgetLimits for CreateBudget and UpdateBudget actions.\n\nAmount (string) -- [REQUIRED]The cost or usage amount that is associated with a budget forecast, actual spend, or budget threshold.\n\nUnit (string) -- [REQUIRED]The unit of measurement that is used for the budget forecast, actual spend, or budget threshold, such as dollars or GB.\n\n\n\nPlannedBudgetLimits (dict) --A map containing multiple BudgetLimit , including current or future limits.\n\nPlannedBudgetLimits is available for cost or usage budget and supports monthly and quarterly TimeUnit .\nFor monthly budgets, provide 12 months of PlannedBudgetLimits values. This must start from the current month and include the next 11 months. The key is the start of the month, UTC in epoch seconds.\nFor quarterly budgets, provide 4 quarters of PlannedBudgetLimits value entries in standard calendar quarter increments. This must start from the current quarter and include the next 3 quarters. The key is the start of the quarter, UTC in epoch seconds.\nIf the planned budget expires before 12 months for monthly or 4 quarters for quarterly, provide the PlannedBudgetLimits values only for the remaining periods.\nIf the budget begins at a date in the future, provide PlannedBudgetLimits values from the start date of the budget.\nAfter all of the BudgetLimit values in PlannedBudgetLimits are used, the budget continues to use the last limit as the BudgetLimit . At that point, the planned budget provides the same experience as a fixed budget.\n\nDescribeBudget and DescribeBudgets response along with PlannedBudgetLimits will also contain BudgetLimit representing the current month or quarter limit present in PlannedBudgetLimits . This only applies to budgets created with PlannedBudgetLimits . Budgets created without PlannedBudgetLimits will only contain BudgetLimit , and no PlannedBudgetLimits .\n\n(string) --A generic string.\n\n(dict) --The amount of cost or usage that is measured for a budget.\nFor example, a Spend for 3 GB of S3 usage would have the following parameters:\n\nAn Amount of 3\nA unit of GB\n\n\nAmount (string) -- [REQUIRED]The cost or usage amount that is associated with a budget forecast, actual spend, or budget threshold.\n\nUnit (string) -- [REQUIRED]The unit of measurement that is used for the budget forecast, actual spend, or budget threshold, such as dollars or GB.\n\n\n\n\n\n\n\nCostFilters (dict) --The cost filters, such as service or tag, that are applied to a budget.\nAWS Budgets supports the following services as a filter for RI budgets:\n\nAmazon Elastic Compute Cloud - Compute\nAmazon Redshift\nAmazon Relational Database Service\nAmazon ElastiCache\nAmazon Elasticsearch Service\n\n\n(string) --A generic string.\n\n(list) --\n(string) --A generic string.\n\n\n\n\n\n\n\nCostTypes (dict) --The types of costs that are included in this COST budget.\n\nUSAGE , RI_UTILIZATION , RI_COVERAGE , Savings_Plans_Utilization , and Savings_Plans_Coverage budgets do not have CostTypes .\n\nIncludeTax (boolean) --Specifies whether a budget includes taxes.\nThe default value is true .\n\nIncludeSubscription (boolean) --Specifies whether a budget includes subscriptions.\nThe default value is true .\n\nUseBlended (boolean) --Specifies whether a budget uses a blended rate.\nThe default value is false .\n\nIncludeRefund (boolean) --Specifies whether a budget includes refunds.\nThe default value is true .\n\nIncludeCredit (boolean) --Specifies whether a budget includes credits.\nThe default value is true .\n\nIncludeUpfront (boolean) --Specifies whether a budget includes upfront RI costs.\nThe default value is true .\n\nIncludeRecurring (boolean) --Specifies whether a budget includes recurring fees such as monthly RI fees.\nThe default value is true .\n\nIncludeOtherSubscription (boolean) --Specifies whether a budget includes non-RI subscription costs.\nThe default value is true .\n\nIncludeSupport (boolean) --Specifies whether a budget includes support subscription fees.\nThe default value is true .\n\nIncludeDiscount (boolean) --Specifies whether a budget includes discounts.\nThe default value is true .\n\nUseAmortized (boolean) --Specifies whether a budget uses the amortized rate.\nThe default value is false .\n\n\n\nTimeUnit (string) -- [REQUIRED]The length of time until a budget resets the actual and forecasted spend. DAILY is available only for RI_UTILIZATION , RI_COVERAGE , Savings_Plans_Utilization , and Savings_Plans_Coverage budgets.\n\nTimePeriod (dict) --The period of time that is covered by a budget. The period has a start date and an end date. The start date must come before the end date. The end date must come before 06/15/87 00:00 UTC .\nIf you create your budget and don\'t specify a start date, AWS defaults to the start of your chosen time period (DAILY, MONTHLY, QUARTERLY, or ANNUALLY). For example, if you created your budget on January 24, 2018, chose DAILY , and didn\'t set a start date, AWS set your start date to 01/24/18 00:00 UTC . If you chose MONTHLY , AWS set your start date to 01/01/18 00:00 UTC . If you didn\'t specify an end date, AWS set your end date to 06/15/87 00:00 UTC . The defaults are the same for the AWS Billing and Cost Management console and the API.\nYou can change either date with the UpdateBudget operation.\nAfter the end date, AWS deletes the budget and all associated notifications and subscribers.\n\nStart (datetime) --The start date for a budget. If you created your budget and didn\'t specify a start date, AWS defaults to the start of your chosen time period (DAILY, MONTHLY, QUARTERLY, or ANNUALLY). For example, if you created your budget on January 24, 2018, chose DAILY , and didn\'t set a start date, AWS set your start date to 01/24/18 00:00 UTC . If you chose MONTHLY , AWS set your start date to 01/01/18 00:00 UTC . The defaults are the same for the AWS Billing and Cost Management console and the API.\nYou can change your start date with the UpdateBudget operation.\n\nEnd (datetime) --The end date for a budget. If you didn\'t specify an end date, AWS set your end date to 06/15/87 00:00 UTC . The defaults are the same for the AWS Billing and Cost Management console and the API.\nAfter the end date, AWS deletes the budget and all associated notifications and subscribers. You can change your end date with the UpdateBudget operation.\n\n\n\nCalculatedSpend (dict) --The actual and forecasted cost or usage that the budget tracks.\n\nActualSpend (dict) -- [REQUIRED]The amount of cost, usage, or RI units that you have used.\n\nAmount (string) -- [REQUIRED]The cost or usage amount that is associated with a budget forecast, actual spend, or budget threshold.\n\nUnit (string) -- [REQUIRED]The unit of measurement that is used for the budget forecast, actual spend, or budget threshold, such as dollars or GB.\n\n\n\nForecastedSpend (dict) --The amount of cost, usage, or RI units that you are forecasted to use.\n\nAmount (string) -- [REQUIRED]The cost or usage amount that is associated with a budget forecast, actual spend, or budget threshold.\n\nUnit (string) -- [REQUIRED]The unit of measurement that is used for the budget forecast, actual spend, or budget threshold, such as dollars or GB.\n\n\n\n\n\nBudgetType (string) -- [REQUIRED]Whether this budget tracks costs, usage, RI utilization, RI coverage, Savings Plans utilization, or Savings Plans coverage.\n\nLastUpdatedTime (datetime) --The last time that you updated this budget.\n\n\n

    :type NotificationsWithSubscribers: list
    :param NotificationsWithSubscribers: A notification that you want to associate with a budget. A budget can have up to five notifications, and each notification can have one SNS subscriber and up to 10 email subscribers. If you include notifications and subscribers in your CreateBudget call, AWS creates the notifications and subscribers for you.\n\n(dict) --A notification with subscribers. A notification can have one SNS subscriber and up to 10 email subscribers, for a total of 11 subscribers.\n\nNotification (dict) -- [REQUIRED]The notification that is associated with a budget.\n\nNotificationType (string) -- [REQUIRED]Whether the notification is for how much you have spent (ACTUAL ) or for how much you\'re forecasted to spend (FORECASTED ).\n\nComparisonOperator (string) -- [REQUIRED]The comparison that is used for this notification.\n\nThreshold (float) -- [REQUIRED]The threshold that is associated with a notification. Thresholds are always a percentage.\n\nThresholdType (string) --The type of threshold for a notification. For ABSOLUTE_VALUE thresholds, AWS notifies you when you go over or are forecasted to go over your total cost threshold. For PERCENTAGE thresholds, AWS notifies you when you go over or are forecasted to go over a certain percentage of your forecasted spend. For example, if you have a budget for 200 dollars and you have a PERCENTAGE threshold of 80%, AWS notifies you when you go over 160 dollars.\n\nNotificationState (string) --Whether this notification is in alarm. If a budget notification is in the ALARM state, you have passed the set threshold for the budget.\n\n\n\nSubscribers (list) -- [REQUIRED]A list of subscribers who are subscribed to this notification.\n\n(dict) --The subscriber to a budget notification. The subscriber consists of a subscription type and either an Amazon SNS topic or an email address.\nFor example, an email subscriber would have the following parameters:\n\nA subscriptionType of EMAIL\nAn address of example@example.com\n\n\nSubscriptionType (string) -- [REQUIRED]The type of notification that AWS sends to a subscriber.\n\nAddress (string) -- [REQUIRED]The address that AWS sends budget notifications to, either an SNS topic or an email.\nWhen you create a subscriber, the value of Address can\'t contain line breaks.\n\n\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
Response of CreateBudget





Exceptions

Budgets.Client.exceptions.InvalidParameterException
Budgets.Client.exceptions.InternalErrorException
Budgets.Client.exceptions.CreationLimitExceededException
Budgets.Client.exceptions.DuplicateRecordException
Budgets.Client.exceptions.AccessDeniedException


    :return: {}
    
    
    :returns: 
    Budgets.Client.exceptions.InvalidParameterException
    Budgets.Client.exceptions.InternalErrorException
    Budgets.Client.exceptions.CreationLimitExceededException
    Budgets.Client.exceptions.DuplicateRecordException
    Budgets.Client.exceptions.AccessDeniedException
    
    """
    pass

def create_notification(AccountId=None, BudgetName=None, Notification=None, Subscribers=None):
    """
    Creates a notification. You must create the budget before you create the associated notification.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_notification(
        AccountId='string',
        BudgetName='string',
        Notification={
            'NotificationType': 'ACTUAL'|'FORECASTED',
            'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
            'Threshold': 123.0,
            'ThresholdType': 'PERCENTAGE'|'ABSOLUTE_VALUE',
            'NotificationState': 'OK'|'ALARM'
        },
        Subscribers=[
            {
                'SubscriptionType': 'SNS'|'EMAIL',
                'Address': 'string'
            },
        ]
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe accountId that is associated with the budget that you want to create a notification for.\n

    :type BudgetName: string
    :param BudgetName: [REQUIRED]\nThe name of the budget that you want AWS to notify you about. Budget names must be unique within an account.\n

    :type Notification: dict
    :param Notification: [REQUIRED]\nThe notification that you want to create.\n\nNotificationType (string) -- [REQUIRED]Whether the notification is for how much you have spent (ACTUAL ) or for how much you\'re forecasted to spend (FORECASTED ).\n\nComparisonOperator (string) -- [REQUIRED]The comparison that is used for this notification.\n\nThreshold (float) -- [REQUIRED]The threshold that is associated with a notification. Thresholds are always a percentage.\n\nThresholdType (string) --The type of threshold for a notification. For ABSOLUTE_VALUE thresholds, AWS notifies you when you go over or are forecasted to go over your total cost threshold. For PERCENTAGE thresholds, AWS notifies you when you go over or are forecasted to go over a certain percentage of your forecasted spend. For example, if you have a budget for 200 dollars and you have a PERCENTAGE threshold of 80%, AWS notifies you when you go over 160 dollars.\n\nNotificationState (string) --Whether this notification is in alarm. If a budget notification is in the ALARM state, you have passed the set threshold for the budget.\n\n\n

    :type Subscribers: list
    :param Subscribers: [REQUIRED]\nA list of subscribers that you want to associate with the notification. Each notification can have one SNS subscriber and up to 10 email subscribers.\n\n(dict) --The subscriber to a budget notification. The subscriber consists of a subscription type and either an Amazon SNS topic or an email address.\nFor example, an email subscriber would have the following parameters:\n\nA subscriptionType of EMAIL\nAn address of example@example.com\n\n\nSubscriptionType (string) -- [REQUIRED]The type of notification that AWS sends to a subscriber.\n\nAddress (string) -- [REQUIRED]The address that AWS sends budget notifications to, either an SNS topic or an email.\nWhen you create a subscriber, the value of Address can\'t contain line breaks.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
Response of CreateNotification





Exceptions

Budgets.Client.exceptions.InternalErrorException
Budgets.Client.exceptions.InvalidParameterException
Budgets.Client.exceptions.NotFoundException
Budgets.Client.exceptions.CreationLimitExceededException
Budgets.Client.exceptions.DuplicateRecordException
Budgets.Client.exceptions.AccessDeniedException


    :return: {}
    
    
    :returns: 
    Budgets.Client.exceptions.InternalErrorException
    Budgets.Client.exceptions.InvalidParameterException
    Budgets.Client.exceptions.NotFoundException
    Budgets.Client.exceptions.CreationLimitExceededException
    Budgets.Client.exceptions.DuplicateRecordException
    Budgets.Client.exceptions.AccessDeniedException
    
    """
    pass

def create_subscriber(AccountId=None, BudgetName=None, Notification=None, Subscriber=None):
    """
    Creates a subscriber. You must create the associated budget and notification before you create the subscriber.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_subscriber(
        AccountId='string',
        BudgetName='string',
        Notification={
            'NotificationType': 'ACTUAL'|'FORECASTED',
            'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
            'Threshold': 123.0,
            'ThresholdType': 'PERCENTAGE'|'ABSOLUTE_VALUE',
            'NotificationState': 'OK'|'ALARM'
        },
        Subscriber={
            'SubscriptionType': 'SNS'|'EMAIL',
            'Address': 'string'
        }
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe accountId that is associated with the budget that you want to create a subscriber for.\n

    :type BudgetName: string
    :param BudgetName: [REQUIRED]\nThe name of the budget that you want to subscribe to. Budget names must be unique within an account.\n

    :type Notification: dict
    :param Notification: [REQUIRED]\nThe notification that you want to create a subscriber for.\n\nNotificationType (string) -- [REQUIRED]Whether the notification is for how much you have spent (ACTUAL ) or for how much you\'re forecasted to spend (FORECASTED ).\n\nComparisonOperator (string) -- [REQUIRED]The comparison that is used for this notification.\n\nThreshold (float) -- [REQUIRED]The threshold that is associated with a notification. Thresholds are always a percentage.\n\nThresholdType (string) --The type of threshold for a notification. For ABSOLUTE_VALUE thresholds, AWS notifies you when you go over or are forecasted to go over your total cost threshold. For PERCENTAGE thresholds, AWS notifies you when you go over or are forecasted to go over a certain percentage of your forecasted spend. For example, if you have a budget for 200 dollars and you have a PERCENTAGE threshold of 80%, AWS notifies you when you go over 160 dollars.\n\nNotificationState (string) --Whether this notification is in alarm. If a budget notification is in the ALARM state, you have passed the set threshold for the budget.\n\n\n

    :type Subscriber: dict
    :param Subscriber: [REQUIRED]\nThe subscriber that you want to associate with a budget notification.\n\nSubscriptionType (string) -- [REQUIRED]The type of notification that AWS sends to a subscriber.\n\nAddress (string) -- [REQUIRED]The address that AWS sends budget notifications to, either an SNS topic or an email.\nWhen you create a subscriber, the value of Address can\'t contain line breaks.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
Response of CreateSubscriber





Exceptions

Budgets.Client.exceptions.InternalErrorException
Budgets.Client.exceptions.InvalidParameterException
Budgets.Client.exceptions.CreationLimitExceededException
Budgets.Client.exceptions.DuplicateRecordException
Budgets.Client.exceptions.NotFoundException
Budgets.Client.exceptions.AccessDeniedException


    :return: {}
    
    
    :returns: 
    Budgets.Client.exceptions.InternalErrorException
    Budgets.Client.exceptions.InvalidParameterException
    Budgets.Client.exceptions.CreationLimitExceededException
    Budgets.Client.exceptions.DuplicateRecordException
    Budgets.Client.exceptions.NotFoundException
    Budgets.Client.exceptions.AccessDeniedException
    
    """
    pass

def delete_budget(AccountId=None, BudgetName=None):
    """
    Deletes a budget. You can delete your budget at any time.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_budget(
        AccountId='string',
        BudgetName='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe accountId that is associated with the budget that you want to delete.\n

    :type BudgetName: string
    :param BudgetName: [REQUIRED]\nThe name of the budget that you want to delete.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
Response of DeleteBudget





Exceptions

Budgets.Client.exceptions.InternalErrorException
Budgets.Client.exceptions.InvalidParameterException
Budgets.Client.exceptions.NotFoundException
Budgets.Client.exceptions.AccessDeniedException


    :return: {}
    
    
    :returns: 
    Budgets.Client.exceptions.InternalErrorException
    Budgets.Client.exceptions.InvalidParameterException
    Budgets.Client.exceptions.NotFoundException
    Budgets.Client.exceptions.AccessDeniedException
    
    """
    pass

def delete_notification(AccountId=None, BudgetName=None, Notification=None):
    """
    Deletes a notification.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_notification(
        AccountId='string',
        BudgetName='string',
        Notification={
            'NotificationType': 'ACTUAL'|'FORECASTED',
            'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
            'Threshold': 123.0,
            'ThresholdType': 'PERCENTAGE'|'ABSOLUTE_VALUE',
            'NotificationState': 'OK'|'ALARM'
        }
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe accountId that is associated with the budget whose notification you want to delete.\n

    :type BudgetName: string
    :param BudgetName: [REQUIRED]\nThe name of the budget whose notification you want to delete.\n

    :type Notification: dict
    :param Notification: [REQUIRED]\nThe notification that you want to delete.\n\nNotificationType (string) -- [REQUIRED]Whether the notification is for how much you have spent (ACTUAL ) or for how much you\'re forecasted to spend (FORECASTED ).\n\nComparisonOperator (string) -- [REQUIRED]The comparison that is used for this notification.\n\nThreshold (float) -- [REQUIRED]The threshold that is associated with a notification. Thresholds are always a percentage.\n\nThresholdType (string) --The type of threshold for a notification. For ABSOLUTE_VALUE thresholds, AWS notifies you when you go over or are forecasted to go over your total cost threshold. For PERCENTAGE thresholds, AWS notifies you when you go over or are forecasted to go over a certain percentage of your forecasted spend. For example, if you have a budget for 200 dollars and you have a PERCENTAGE threshold of 80%, AWS notifies you when you go over 160 dollars.\n\nNotificationState (string) --Whether this notification is in alarm. If a budget notification is in the ALARM state, you have passed the set threshold for the budget.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
Response of DeleteNotification





Exceptions

Budgets.Client.exceptions.InvalidParameterException
Budgets.Client.exceptions.InternalErrorException
Budgets.Client.exceptions.NotFoundException
Budgets.Client.exceptions.AccessDeniedException


    :return: {}
    
    
    :returns: 
    Budgets.Client.exceptions.InvalidParameterException
    Budgets.Client.exceptions.InternalErrorException
    Budgets.Client.exceptions.NotFoundException
    Budgets.Client.exceptions.AccessDeniedException
    
    """
    pass

def delete_subscriber(AccountId=None, BudgetName=None, Notification=None, Subscriber=None):
    """
    Deletes a subscriber.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_subscriber(
        AccountId='string',
        BudgetName='string',
        Notification={
            'NotificationType': 'ACTUAL'|'FORECASTED',
            'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
            'Threshold': 123.0,
            'ThresholdType': 'PERCENTAGE'|'ABSOLUTE_VALUE',
            'NotificationState': 'OK'|'ALARM'
        },
        Subscriber={
            'SubscriptionType': 'SNS'|'EMAIL',
            'Address': 'string'
        }
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe accountId that is associated with the budget whose subscriber you want to delete.\n

    :type BudgetName: string
    :param BudgetName: [REQUIRED]\nThe name of the budget whose subscriber you want to delete.\n

    :type Notification: dict
    :param Notification: [REQUIRED]\nThe notification whose subscriber you want to delete.\n\nNotificationType (string) -- [REQUIRED]Whether the notification is for how much you have spent (ACTUAL ) or for how much you\'re forecasted to spend (FORECASTED ).\n\nComparisonOperator (string) -- [REQUIRED]The comparison that is used for this notification.\n\nThreshold (float) -- [REQUIRED]The threshold that is associated with a notification. Thresholds are always a percentage.\n\nThresholdType (string) --The type of threshold for a notification. For ABSOLUTE_VALUE thresholds, AWS notifies you when you go over or are forecasted to go over your total cost threshold. For PERCENTAGE thresholds, AWS notifies you when you go over or are forecasted to go over a certain percentage of your forecasted spend. For example, if you have a budget for 200 dollars and you have a PERCENTAGE threshold of 80%, AWS notifies you when you go over 160 dollars.\n\nNotificationState (string) --Whether this notification is in alarm. If a budget notification is in the ALARM state, you have passed the set threshold for the budget.\n\n\n

    :type Subscriber: dict
    :param Subscriber: [REQUIRED]\nThe subscriber that you want to delete.\n\nSubscriptionType (string) -- [REQUIRED]The type of notification that AWS sends to a subscriber.\n\nAddress (string) -- [REQUIRED]The address that AWS sends budget notifications to, either an SNS topic or an email.\nWhen you create a subscriber, the value of Address can\'t contain line breaks.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
Response of DeleteSubscriber





Exceptions

Budgets.Client.exceptions.InternalErrorException
Budgets.Client.exceptions.InvalidParameterException
Budgets.Client.exceptions.NotFoundException
Budgets.Client.exceptions.AccessDeniedException


    :return: {}
    
    
    :returns: 
    Budgets.Client.exceptions.InternalErrorException
    Budgets.Client.exceptions.InvalidParameterException
    Budgets.Client.exceptions.NotFoundException
    Budgets.Client.exceptions.AccessDeniedException
    
    """
    pass

def describe_budget(AccountId=None, BudgetName=None):
    """
    Describes a budget.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_budget(
        AccountId='string',
        BudgetName='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe accountId that is associated with the budget that you want a description of.\n

    :type BudgetName: string
    :param BudgetName: [REQUIRED]\nThe name of the budget that you want a description of.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Budget': {
        'BudgetName': 'string',
        'BudgetLimit': {
            'Amount': 'string',
            'Unit': 'string'
        },
        'PlannedBudgetLimits': {
            'string': {
                'Amount': 'string',
                'Unit': 'string'
            }
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
        'BudgetType': 'USAGE'|'COST'|'RI_UTILIZATION'|'RI_COVERAGE'|'SAVINGS_PLANS_UTILIZATION'|'SAVINGS_PLANS_COVERAGE',
        'LastUpdatedTime': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --
Response of DescribeBudget

Budget (dict) --
The description of the budget.

BudgetName (string) --
The name of a budget. The name must be unique within an account. The : and \\ characters aren\'t allowed in BudgetName .

BudgetLimit (dict) --
The total amount of cost, usage, RI utilization, RI coverage, Savings Plans utilization, or Savings Plans coverage that you want to track with your budget.

BudgetLimit is required for cost or usage budgets, but optional for RI or Savings Plans utilization or coverage budgets. RI and Savings Plans utilization or coverage budgets default to 100 , which is the only valid value for RI or Savings Plans utilization or coverage budgets. You can\'t use BudgetLimit with PlannedBudgetLimits for CreateBudget and UpdateBudget actions.


Amount (string) --
The cost or usage amount that is associated with a budget forecast, actual spend, or budget threshold.

Unit (string) --
The unit of measurement that is used for the budget forecast, actual spend, or budget threshold, such as dollars or GB.



PlannedBudgetLimits (dict) --
A map containing multiple BudgetLimit , including current or future limits.

PlannedBudgetLimits is available for cost or usage budget and supports monthly and quarterly TimeUnit .

For monthly budgets, provide 12 months of PlannedBudgetLimits values. This must start from the current month and include the next 11 months. The key is the start of the month, UTC in epoch seconds.
For quarterly budgets, provide 4 quarters of PlannedBudgetLimits value entries in standard calendar quarter increments. This must start from the current quarter and include the next 3 quarters. The key is the start of the quarter, UTC in epoch seconds.
If the planned budget expires before 12 months for monthly or 4 quarters for quarterly, provide the PlannedBudgetLimits values only for the remaining periods.
If the budget begins at a date in the future, provide PlannedBudgetLimits values from the start date of the budget.
After all of the BudgetLimit values in PlannedBudgetLimits are used, the budget continues to use the last limit as the BudgetLimit . At that point, the planned budget provides the same experience as a fixed budget.

DescribeBudget and DescribeBudgets response along with PlannedBudgetLimits will also contain BudgetLimit representing the current month or quarter limit present in PlannedBudgetLimits . This only applies to budgets created with PlannedBudgetLimits . Budgets created without PlannedBudgetLimits will only contain BudgetLimit , and no PlannedBudgetLimits .


(string) --
A generic string.

(dict) --
The amount of cost or usage that is measured for a budget.
For example, a Spend for 3 GB of S3 usage would have the following parameters:

An Amount of 3
A unit of GB


Amount (string) --
The cost or usage amount that is associated with a budget forecast, actual spend, or budget threshold.

Unit (string) --
The unit of measurement that is used for the budget forecast, actual spend, or budget threshold, such as dollars or GB.







CostFilters (dict) --
The cost filters, such as service or tag, that are applied to a budget.
AWS Budgets supports the following services as a filter for RI budgets:

Amazon Elastic Compute Cloud - Compute
Amazon Redshift
Amazon Relational Database Service
Amazon ElastiCache
Amazon Elasticsearch Service


(string) --
A generic string.

(list) --

(string) --
A generic string.







CostTypes (dict) --
The types of costs that are included in this COST budget.

USAGE , RI_UTILIZATION , RI_COVERAGE , Savings_Plans_Utilization , and Savings_Plans_Coverage budgets do not have CostTypes .


IncludeTax (boolean) --
Specifies whether a budget includes taxes.
The default value is true .

IncludeSubscription (boolean) --
Specifies whether a budget includes subscriptions.
The default value is true .

UseBlended (boolean) --
Specifies whether a budget uses a blended rate.
The default value is false .

IncludeRefund (boolean) --
Specifies whether a budget includes refunds.
The default value is true .

IncludeCredit (boolean) --
Specifies whether a budget includes credits.
The default value is true .

IncludeUpfront (boolean) --
Specifies whether a budget includes upfront RI costs.
The default value is true .

IncludeRecurring (boolean) --
Specifies whether a budget includes recurring fees such as monthly RI fees.
The default value is true .

IncludeOtherSubscription (boolean) --
Specifies whether a budget includes non-RI subscription costs.
The default value is true .

IncludeSupport (boolean) --
Specifies whether a budget includes support subscription fees.
The default value is true .

IncludeDiscount (boolean) --
Specifies whether a budget includes discounts.
The default value is true .

UseAmortized (boolean) --
Specifies whether a budget uses the amortized rate.
The default value is false .



TimeUnit (string) --
The length of time until a budget resets the actual and forecasted spend. DAILY is available only for RI_UTILIZATION , RI_COVERAGE , Savings_Plans_Utilization , and Savings_Plans_Coverage budgets.

TimePeriod (dict) --
The period of time that is covered by a budget. The period has a start date and an end date. The start date must come before the end date. The end date must come before 06/15/87 00:00 UTC .
If you create your budget and don\'t specify a start date, AWS defaults to the start of your chosen time period (DAILY, MONTHLY, QUARTERLY, or ANNUALLY). For example, if you created your budget on January 24, 2018, chose DAILY , and didn\'t set a start date, AWS set your start date to 01/24/18 00:00 UTC . If you chose MONTHLY , AWS set your start date to 01/01/18 00:00 UTC . If you didn\'t specify an end date, AWS set your end date to 06/15/87 00:00 UTC . The defaults are the same for the AWS Billing and Cost Management console and the API.
You can change either date with the UpdateBudget operation.
After the end date, AWS deletes the budget and all associated notifications and subscribers.

Start (datetime) --
The start date for a budget. If you created your budget and didn\'t specify a start date, AWS defaults to the start of your chosen time period (DAILY, MONTHLY, QUARTERLY, or ANNUALLY). For example, if you created your budget on January 24, 2018, chose DAILY , and didn\'t set a start date, AWS set your start date to 01/24/18 00:00 UTC . If you chose MONTHLY , AWS set your start date to 01/01/18 00:00 UTC . The defaults are the same for the AWS Billing and Cost Management console and the API.
You can change your start date with the UpdateBudget operation.

End (datetime) --
The end date for a budget. If you didn\'t specify an end date, AWS set your end date to 06/15/87 00:00 UTC . The defaults are the same for the AWS Billing and Cost Management console and the API.
After the end date, AWS deletes the budget and all associated notifications and subscribers. You can change your end date with the UpdateBudget operation.



CalculatedSpend (dict) --
The actual and forecasted cost or usage that the budget tracks.

ActualSpend (dict) --
The amount of cost, usage, or RI units that you have used.

Amount (string) --
The cost or usage amount that is associated with a budget forecast, actual spend, or budget threshold.

Unit (string) --
The unit of measurement that is used for the budget forecast, actual spend, or budget threshold, such as dollars or GB.



ForecastedSpend (dict) --
The amount of cost, usage, or RI units that you are forecasted to use.

Amount (string) --
The cost or usage amount that is associated with a budget forecast, actual spend, or budget threshold.

Unit (string) --
The unit of measurement that is used for the budget forecast, actual spend, or budget threshold, such as dollars or GB.





BudgetType (string) --
Whether this budget tracks costs, usage, RI utilization, RI coverage, Savings Plans utilization, or Savings Plans coverage.

LastUpdatedTime (datetime) --
The last time that you updated this budget.









Exceptions

Budgets.Client.exceptions.InternalErrorException
Budgets.Client.exceptions.InvalidParameterException
Budgets.Client.exceptions.NotFoundException
Budgets.Client.exceptions.AccessDeniedException


    :return: {
        'Budget': {
            'BudgetName': 'string',
            'BudgetLimit': {
                'Amount': 'string',
                'Unit': 'string'
            },
            'PlannedBudgetLimits': {
                'string': {
                    'Amount': 'string',
                    'Unit': 'string'
                }
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
            'BudgetType': 'USAGE'|'COST'|'RI_UTILIZATION'|'RI_COVERAGE'|'SAVINGS_PLANS_UTILIZATION'|'SAVINGS_PLANS_COVERAGE',
            'LastUpdatedTime': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    An Amount of 3
    A unit of GB
    
    """
    pass

def describe_budget_performance_history(AccountId=None, BudgetName=None, TimePeriod=None, MaxResults=None, NextToken=None):
    """
    Describes the history for DAILY , MONTHLY , and QUARTERLY budgets. Budget history isn\'t available for ANNUAL budgets.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_budget_performance_history(
        AccountId='string',
        BudgetName='string',
        TimePeriod={
            'Start': datetime(2015, 1, 1),
            'End': datetime(2015, 1, 1)
        },
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe account ID of the user. It should be a 12-digit number.\n

    :type BudgetName: string
    :param BudgetName: [REQUIRED]\nA string that represents the budget name. The ':' and '' characters aren\'t allowed.\n

    :type TimePeriod: dict
    :param TimePeriod: Retrieves how often the budget went into an ALARM state for the specified time period.\n\nStart (datetime) --The start date for a budget. If you created your budget and didn\'t specify a start date, AWS defaults to the start of your chosen time period (DAILY, MONTHLY, QUARTERLY, or ANNUALLY). For example, if you created your budget on January 24, 2018, chose DAILY , and didn\'t set a start date, AWS set your start date to 01/24/18 00:00 UTC . If you chose MONTHLY , AWS set your start date to 01/01/18 00:00 UTC . The defaults are the same for the AWS Billing and Cost Management console and the API.\nYou can change your start date with the UpdateBudget operation.\n\nEnd (datetime) --The end date for a budget. If you didn\'t specify an end date, AWS set your end date to 06/15/87 00:00 UTC . The defaults are the same for the AWS Billing and Cost Management console and the API.\nAfter the end date, AWS deletes the budget and all associated notifications and subscribers. You can change your end date with the UpdateBudget operation.\n\n\n

    :type MaxResults: integer
    :param MaxResults: An integer that represents how many entries a paginated response contains. The maximum is 100.

    :type NextToken: string
    :param NextToken: A generic string.

    :rtype: dict

ReturnsResponse Syntax
{
    'BudgetPerformanceHistory': {
        'BudgetName': 'string',
        'BudgetType': 'USAGE'|'COST'|'RI_UTILIZATION'|'RI_COVERAGE'|'SAVINGS_PLANS_UTILIZATION'|'SAVINGS_PLANS_COVERAGE',
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
        'BudgetedAndActualAmountsList': [
            {
                'BudgetedAmount': {
                    'Amount': 'string',
                    'Unit': 'string'
                },
                'ActualAmount': {
                    'Amount': 'string',
                    'Unit': 'string'
                },
                'TimePeriod': {
                    'Start': datetime(2015, 1, 1),
                    'End': datetime(2015, 1, 1)
                }
            },
        ]
    },
    'NextToken': 'string'
}


Response Structure

(dict) --

BudgetPerformanceHistory (dict) --
The history of how often the budget has gone into an ALARM state.
For DAILY budgets, the history saves the state of the budget for the last 60 days. For MONTHLY budgets, the history saves the state of the budget for the current month plus the last 12 months. For QUARTERLY budgets, the history saves the state of the budget for the last four quarters.

BudgetName (string) --
A string that represents the budget name. The ":" and "" characters aren\'t allowed.

BudgetType (string) --
The type of a budget. It must be one of the following types:

COST , USAGE , RI_UTILIZATION , or RI_COVERAGE .


CostFilters (dict) --
The history of the cost filters for a budget during the specified time period.

(string) --
A generic string.

(list) --

(string) --
A generic string.







CostTypes (dict) --
The history of the cost types for a budget during the specified time period.

IncludeTax (boolean) --
Specifies whether a budget includes taxes.
The default value is true .

IncludeSubscription (boolean) --
Specifies whether a budget includes subscriptions.
The default value is true .

UseBlended (boolean) --
Specifies whether a budget uses a blended rate.
The default value is false .

IncludeRefund (boolean) --
Specifies whether a budget includes refunds.
The default value is true .

IncludeCredit (boolean) --
Specifies whether a budget includes credits.
The default value is true .

IncludeUpfront (boolean) --
Specifies whether a budget includes upfront RI costs.
The default value is true .

IncludeRecurring (boolean) --
Specifies whether a budget includes recurring fees such as monthly RI fees.
The default value is true .

IncludeOtherSubscription (boolean) --
Specifies whether a budget includes non-RI subscription costs.
The default value is true .

IncludeSupport (boolean) --
Specifies whether a budget includes support subscription fees.
The default value is true .

IncludeDiscount (boolean) --
Specifies whether a budget includes discounts.
The default value is true .

UseAmortized (boolean) --
Specifies whether a budget uses the amortized rate.
The default value is false .



TimeUnit (string) --
The time unit of the budget, such as MONTHLY or QUARTERLY.

BudgetedAndActualAmountsList (list) --
A list of amounts of cost or usage that you created budgets for, compared to your actual costs or usage.

(dict) --
The amount of cost or usage that you created the budget for, compared to your actual costs or usage.

BudgetedAmount (dict) --
The amount of cost or usage that you created the budget for.

Amount (string) --
The cost or usage amount that is associated with a budget forecast, actual spend, or budget threshold.

Unit (string) --
The unit of measurement that is used for the budget forecast, actual spend, or budget threshold, such as dollars or GB.



ActualAmount (dict) --
Your actual costs or usage for a budget period.

Amount (string) --
The cost or usage amount that is associated with a budget forecast, actual spend, or budget threshold.

Unit (string) --
The unit of measurement that is used for the budget forecast, actual spend, or budget threshold, such as dollars or GB.



TimePeriod (dict) --
The time period covered by this budget comparison.

Start (datetime) --
The start date for a budget. If you created your budget and didn\'t specify a start date, AWS defaults to the start of your chosen time period (DAILY, MONTHLY, QUARTERLY, or ANNUALLY). For example, if you created your budget on January 24, 2018, chose DAILY , and didn\'t set a start date, AWS set your start date to 01/24/18 00:00 UTC . If you chose MONTHLY , AWS set your start date to 01/01/18 00:00 UTC . The defaults are the same for the AWS Billing and Cost Management console and the API.
You can change your start date with the UpdateBudget operation.

End (datetime) --
The end date for a budget. If you didn\'t specify an end date, AWS set your end date to 06/15/87 00:00 UTC . The defaults are the same for the AWS Billing and Cost Management console and the API.
After the end date, AWS deletes the budget and all associated notifications and subscribers. You can change your end date with the UpdateBudget operation.









NextToken (string) --
A generic string.







Exceptions

Budgets.Client.exceptions.InternalErrorException
Budgets.Client.exceptions.InvalidParameterException
Budgets.Client.exceptions.NotFoundException
Budgets.Client.exceptions.InvalidNextTokenException
Budgets.Client.exceptions.ExpiredNextTokenException
Budgets.Client.exceptions.AccessDeniedException


    :return: {
        'BudgetPerformanceHistory': {
            'BudgetName': 'string',
            'BudgetType': 'USAGE'|'COST'|'RI_UTILIZATION'|'RI_COVERAGE'|'SAVINGS_PLANS_UTILIZATION'|'SAVINGS_PLANS_COVERAGE',
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
            'BudgetedAndActualAmountsList': [
                {
                    'BudgetedAmount': {
                        'Amount': 'string',
                        'Unit': 'string'
                    },
                    'ActualAmount': {
                        'Amount': 'string',
                        'Unit': 'string'
                    },
                    'TimePeriod': {
                        'Start': datetime(2015, 1, 1),
                        'End': datetime(2015, 1, 1)
                    }
                },
            ]
        },
        'NextToken': 'string'
    }
    
    
    :returns: 
    Budgets.Client.exceptions.InternalErrorException
    Budgets.Client.exceptions.InvalidParameterException
    Budgets.Client.exceptions.NotFoundException
    Budgets.Client.exceptions.InvalidNextTokenException
    Budgets.Client.exceptions.ExpiredNextTokenException
    Budgets.Client.exceptions.AccessDeniedException
    
    """
    pass

def describe_budgets(AccountId=None, MaxResults=None, NextToken=None):
    """
    Lists the budgets that are associated with an account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_budgets(
        AccountId='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe accountId that is associated with the budgets that you want descriptions of.\n

    :type MaxResults: integer
    :param MaxResults: An optional integer that represents how many entries a paginated response contains. The maximum is 100.

    :type NextToken: string
    :param NextToken: The pagination token that you include in your request to indicate the next set of results that you want to retrieve.

    :rtype: dict

ReturnsResponse Syntax
{
    'Budgets': [
        {
            'BudgetName': 'string',
            'BudgetLimit': {
                'Amount': 'string',
                'Unit': 'string'
            },
            'PlannedBudgetLimits': {
                'string': {
                    'Amount': 'string',
                    'Unit': 'string'
                }
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
            'BudgetType': 'USAGE'|'COST'|'RI_UTILIZATION'|'RI_COVERAGE'|'SAVINGS_PLANS_UTILIZATION'|'SAVINGS_PLANS_COVERAGE',
            'LastUpdatedTime': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
Response of DescribeBudgets

Budgets (list) --
A list of budgets.

(dict) --
Represents the output of the CreateBudget operation. The content consists of the detailed metadata and data file information, and the current status of the budget object.
This is the ARN pattern for a budget:

arn:aws:budgetservice::AccountId:budget/budgetName


BudgetName (string) --
The name of a budget. The name must be unique within an account. The : and \\ characters aren\'t allowed in BudgetName .

BudgetLimit (dict) --
The total amount of cost, usage, RI utilization, RI coverage, Savings Plans utilization, or Savings Plans coverage that you want to track with your budget.

BudgetLimit is required for cost or usage budgets, but optional for RI or Savings Plans utilization or coverage budgets. RI and Savings Plans utilization or coverage budgets default to 100 , which is the only valid value for RI or Savings Plans utilization or coverage budgets. You can\'t use BudgetLimit with PlannedBudgetLimits for CreateBudget and UpdateBudget actions.


Amount (string) --
The cost or usage amount that is associated with a budget forecast, actual spend, or budget threshold.

Unit (string) --
The unit of measurement that is used for the budget forecast, actual spend, or budget threshold, such as dollars or GB.



PlannedBudgetLimits (dict) --
A map containing multiple BudgetLimit , including current or future limits.

PlannedBudgetLimits is available for cost or usage budget and supports monthly and quarterly TimeUnit .

For monthly budgets, provide 12 months of PlannedBudgetLimits values. This must start from the current month and include the next 11 months. The key is the start of the month, UTC in epoch seconds.
For quarterly budgets, provide 4 quarters of PlannedBudgetLimits value entries in standard calendar quarter increments. This must start from the current quarter and include the next 3 quarters. The key is the start of the quarter, UTC in epoch seconds.
If the planned budget expires before 12 months for monthly or 4 quarters for quarterly, provide the PlannedBudgetLimits values only for the remaining periods.
If the budget begins at a date in the future, provide PlannedBudgetLimits values from the start date of the budget.
After all of the BudgetLimit values in PlannedBudgetLimits are used, the budget continues to use the last limit as the BudgetLimit . At that point, the planned budget provides the same experience as a fixed budget.

DescribeBudget and DescribeBudgets response along with PlannedBudgetLimits will also contain BudgetLimit representing the current month or quarter limit present in PlannedBudgetLimits . This only applies to budgets created with PlannedBudgetLimits . Budgets created without PlannedBudgetLimits will only contain BudgetLimit , and no PlannedBudgetLimits .


(string) --
A generic string.

(dict) --
The amount of cost or usage that is measured for a budget.
For example, a Spend for 3 GB of S3 usage would have the following parameters:

An Amount of 3
A unit of GB


Amount (string) --
The cost or usage amount that is associated with a budget forecast, actual spend, or budget threshold.

Unit (string) --
The unit of measurement that is used for the budget forecast, actual spend, or budget threshold, such as dollars or GB.







CostFilters (dict) --
The cost filters, such as service or tag, that are applied to a budget.
AWS Budgets supports the following services as a filter for RI budgets:

Amazon Elastic Compute Cloud - Compute
Amazon Redshift
Amazon Relational Database Service
Amazon ElastiCache
Amazon Elasticsearch Service


(string) --
A generic string.

(list) --

(string) --
A generic string.







CostTypes (dict) --
The types of costs that are included in this COST budget.

USAGE , RI_UTILIZATION , RI_COVERAGE , Savings_Plans_Utilization , and Savings_Plans_Coverage budgets do not have CostTypes .


IncludeTax (boolean) --
Specifies whether a budget includes taxes.
The default value is true .

IncludeSubscription (boolean) --
Specifies whether a budget includes subscriptions.
The default value is true .

UseBlended (boolean) --
Specifies whether a budget uses a blended rate.
The default value is false .

IncludeRefund (boolean) --
Specifies whether a budget includes refunds.
The default value is true .

IncludeCredit (boolean) --
Specifies whether a budget includes credits.
The default value is true .

IncludeUpfront (boolean) --
Specifies whether a budget includes upfront RI costs.
The default value is true .

IncludeRecurring (boolean) --
Specifies whether a budget includes recurring fees such as monthly RI fees.
The default value is true .

IncludeOtherSubscription (boolean) --
Specifies whether a budget includes non-RI subscription costs.
The default value is true .

IncludeSupport (boolean) --
Specifies whether a budget includes support subscription fees.
The default value is true .

IncludeDiscount (boolean) --
Specifies whether a budget includes discounts.
The default value is true .

UseAmortized (boolean) --
Specifies whether a budget uses the amortized rate.
The default value is false .



TimeUnit (string) --
The length of time until a budget resets the actual and forecasted spend. DAILY is available only for RI_UTILIZATION , RI_COVERAGE , Savings_Plans_Utilization , and Savings_Plans_Coverage budgets.

TimePeriod (dict) --
The period of time that is covered by a budget. The period has a start date and an end date. The start date must come before the end date. The end date must come before 06/15/87 00:00 UTC .
If you create your budget and don\'t specify a start date, AWS defaults to the start of your chosen time period (DAILY, MONTHLY, QUARTERLY, or ANNUALLY). For example, if you created your budget on January 24, 2018, chose DAILY , and didn\'t set a start date, AWS set your start date to 01/24/18 00:00 UTC . If you chose MONTHLY , AWS set your start date to 01/01/18 00:00 UTC . If you didn\'t specify an end date, AWS set your end date to 06/15/87 00:00 UTC . The defaults are the same for the AWS Billing and Cost Management console and the API.
You can change either date with the UpdateBudget operation.
After the end date, AWS deletes the budget and all associated notifications and subscribers.

Start (datetime) --
The start date for a budget. If you created your budget and didn\'t specify a start date, AWS defaults to the start of your chosen time period (DAILY, MONTHLY, QUARTERLY, or ANNUALLY). For example, if you created your budget on January 24, 2018, chose DAILY , and didn\'t set a start date, AWS set your start date to 01/24/18 00:00 UTC . If you chose MONTHLY , AWS set your start date to 01/01/18 00:00 UTC . The defaults are the same for the AWS Billing and Cost Management console and the API.
You can change your start date with the UpdateBudget operation.

End (datetime) --
The end date for a budget. If you didn\'t specify an end date, AWS set your end date to 06/15/87 00:00 UTC . The defaults are the same for the AWS Billing and Cost Management console and the API.
After the end date, AWS deletes the budget and all associated notifications and subscribers. You can change your end date with the UpdateBudget operation.



CalculatedSpend (dict) --
The actual and forecasted cost or usage that the budget tracks.

ActualSpend (dict) --
The amount of cost, usage, or RI units that you have used.

Amount (string) --
The cost or usage amount that is associated with a budget forecast, actual spend, or budget threshold.

Unit (string) --
The unit of measurement that is used for the budget forecast, actual spend, or budget threshold, such as dollars or GB.



ForecastedSpend (dict) --
The amount of cost, usage, or RI units that you are forecasted to use.

Amount (string) --
The cost or usage amount that is associated with a budget forecast, actual spend, or budget threshold.

Unit (string) --
The unit of measurement that is used for the budget forecast, actual spend, or budget threshold, such as dollars or GB.





BudgetType (string) --
Whether this budget tracks costs, usage, RI utilization, RI coverage, Savings Plans utilization, or Savings Plans coverage.

LastUpdatedTime (datetime) --
The last time that you updated this budget.





NextToken (string) --
The pagination token in the service response that indicates the next set of results that you can retrieve.







Exceptions

Budgets.Client.exceptions.InternalErrorException
Budgets.Client.exceptions.InvalidParameterException
Budgets.Client.exceptions.NotFoundException
Budgets.Client.exceptions.InvalidNextTokenException
Budgets.Client.exceptions.ExpiredNextTokenException
Budgets.Client.exceptions.AccessDeniedException


    :return: {
        'Budgets': [
            {
                'BudgetName': 'string',
                'BudgetLimit': {
                    'Amount': 'string',
                    'Unit': 'string'
                },
                'PlannedBudgetLimits': {
                    'string': {
                        'Amount': 'string',
                        'Unit': 'string'
                    }
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
                'BudgetType': 'USAGE'|'COST'|'RI_UTILIZATION'|'RI_COVERAGE'|'SAVINGS_PLANS_UTILIZATION'|'SAVINGS_PLANS_COVERAGE',
                'LastUpdatedTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    An Amount of 3
    A unit of GB
    
    """
    pass

def describe_notifications_for_budget(AccountId=None, BudgetName=None, MaxResults=None, NextToken=None):
    """
    Lists the notifications that are associated with a budget.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_notifications_for_budget(
        AccountId='string',
        BudgetName='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe accountId that is associated with the budget whose notifications you want descriptions of.\n

    :type BudgetName: string
    :param BudgetName: [REQUIRED]\nThe name of the budget whose notifications you want descriptions of.\n

    :type MaxResults: integer
    :param MaxResults: An optional integer that represents how many entries a paginated response contains. The maximum is 100.

    :type NextToken: string
    :param NextToken: The pagination token that you include in your request to indicate the next set of results that you want to retrieve.

    :rtype: dict

ReturnsResponse Syntax
{
    'Notifications': [
        {
            'NotificationType': 'ACTUAL'|'FORECASTED',
            'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
            'Threshold': 123.0,
            'ThresholdType': 'PERCENTAGE'|'ABSOLUTE_VALUE',
            'NotificationState': 'OK'|'ALARM'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
Response of GetNotificationsForBudget

Notifications (list) --
A list of notifications that are associated with a budget.

(dict) --
A notification that is associated with a budget. A budget can have up to five notifications.
Each notification must have at least one subscriber. A notification can have one SNS subscriber and up to 10 email subscribers, for a total of 11 subscribers.
For example, if you have a budget for 200 dollars and you want to be notified when you go over 160 dollars, create a notification with the following parameters:

A notificationType of ACTUAL
A thresholdType of PERCENTAGE
A comparisonOperator of GREATER_THAN
A notification threshold of 80


NotificationType (string) --
Whether the notification is for how much you have spent (ACTUAL ) or for how much you\'re forecasted to spend (FORECASTED ).

ComparisonOperator (string) --
The comparison that is used for this notification.

Threshold (float) --
The threshold that is associated with a notification. Thresholds are always a percentage.

ThresholdType (string) --
The type of threshold for a notification. For ABSOLUTE_VALUE thresholds, AWS notifies you when you go over or are forecasted to go over your total cost threshold. For PERCENTAGE thresholds, AWS notifies you when you go over or are forecasted to go over a certain percentage of your forecasted spend. For example, if you have a budget for 200 dollars and you have a PERCENTAGE threshold of 80%, AWS notifies you when you go over 160 dollars.

NotificationState (string) --
Whether this notification is in alarm. If a budget notification is in the ALARM state, you have passed the set threshold for the budget.





NextToken (string) --
The pagination token in the service response that indicates the next set of results that you can retrieve.







Exceptions

Budgets.Client.exceptions.InternalErrorException
Budgets.Client.exceptions.InvalidParameterException
Budgets.Client.exceptions.NotFoundException
Budgets.Client.exceptions.InvalidNextTokenException
Budgets.Client.exceptions.ExpiredNextTokenException
Budgets.Client.exceptions.AccessDeniedException


    :return: {
        'Notifications': [
            {
                'NotificationType': 'ACTUAL'|'FORECASTED',
                'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
                'Threshold': 123.0,
                'ThresholdType': 'PERCENTAGE'|'ABSOLUTE_VALUE',
                'NotificationState': 'OK'|'ALARM'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    A notificationType of ACTUAL
    A thresholdType of PERCENTAGE
    A comparisonOperator of GREATER_THAN
    A notification threshold of 80
    
    """
    pass

def describe_subscribers_for_notification(AccountId=None, BudgetName=None, Notification=None, MaxResults=None, NextToken=None):
    """
    Lists the subscribers that are associated with a notification.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_subscribers_for_notification(
        AccountId='string',
        BudgetName='string',
        Notification={
            'NotificationType': 'ACTUAL'|'FORECASTED',
            'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
            'Threshold': 123.0,
            'ThresholdType': 'PERCENTAGE'|'ABSOLUTE_VALUE',
            'NotificationState': 'OK'|'ALARM'
        },
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe accountId that is associated with the budget whose subscribers you want descriptions of.\n

    :type BudgetName: string
    :param BudgetName: [REQUIRED]\nThe name of the budget whose subscribers you want descriptions of.\n

    :type Notification: dict
    :param Notification: [REQUIRED]\nThe notification whose subscribers you want to list.\n\nNotificationType (string) -- [REQUIRED]Whether the notification is for how much you have spent (ACTUAL ) or for how much you\'re forecasted to spend (FORECASTED ).\n\nComparisonOperator (string) -- [REQUIRED]The comparison that is used for this notification.\n\nThreshold (float) -- [REQUIRED]The threshold that is associated with a notification. Thresholds are always a percentage.\n\nThresholdType (string) --The type of threshold for a notification. For ABSOLUTE_VALUE thresholds, AWS notifies you when you go over or are forecasted to go over your total cost threshold. For PERCENTAGE thresholds, AWS notifies you when you go over or are forecasted to go over a certain percentage of your forecasted spend. For example, if you have a budget for 200 dollars and you have a PERCENTAGE threshold of 80%, AWS notifies you when you go over 160 dollars.\n\nNotificationState (string) --Whether this notification is in alarm. If a budget notification is in the ALARM state, you have passed the set threshold for the budget.\n\n\n

    :type MaxResults: integer
    :param MaxResults: An optional integer that represents how many entries a paginated response contains. The maximum is 100.

    :type NextToken: string
    :param NextToken: The pagination token that you include in your request to indicate the next set of results that you want to retrieve.

    :rtype: dict

ReturnsResponse Syntax
{
    'Subscribers': [
        {
            'SubscriptionType': 'SNS'|'EMAIL',
            'Address': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
Response of DescribeSubscribersForNotification

Subscribers (list) --
A list of subscribers that are associated with a notification.

(dict) --
The subscriber to a budget notification. The subscriber consists of a subscription type and either an Amazon SNS topic or an email address.
For example, an email subscriber would have the following parameters:

A subscriptionType of EMAIL
An address of example@example.com


SubscriptionType (string) --
The type of notification that AWS sends to a subscriber.

Address (string) --
The address that AWS sends budget notifications to, either an SNS topic or an email.
When you create a subscriber, the value of Address can\'t contain line breaks.





NextToken (string) --
The pagination token in the service response that indicates the next set of results that you can retrieve.







Exceptions

Budgets.Client.exceptions.InternalErrorException
Budgets.Client.exceptions.NotFoundException
Budgets.Client.exceptions.InvalidParameterException
Budgets.Client.exceptions.InvalidNextTokenException
Budgets.Client.exceptions.ExpiredNextTokenException
Budgets.Client.exceptions.AccessDeniedException


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

def update_budget(AccountId=None, NewBudget=None):
    """
    Updates a budget. You can change every part of a budget except for the budgetName and the calculatedSpend . When you modify a budget, the calculatedSpend drops to zero until AWS has new usage data to use for forecasting.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_budget(
        AccountId='string',
        NewBudget={
            'BudgetName': 'string',
            'BudgetLimit': {
                'Amount': 'string',
                'Unit': 'string'
            },
            'PlannedBudgetLimits': {
                'string': {
                    'Amount': 'string',
                    'Unit': 'string'
                }
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
            'BudgetType': 'USAGE'|'COST'|'RI_UTILIZATION'|'RI_COVERAGE'|'SAVINGS_PLANS_UTILIZATION'|'SAVINGS_PLANS_COVERAGE',
            'LastUpdatedTime': datetime(2015, 1, 1)
        }
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe accountId that is associated with the budget that you want to update.\n

    :type NewBudget: dict
    :param NewBudget: [REQUIRED]\nThe budget that you want to update your budget to.\n\nBudgetName (string) -- [REQUIRED]The name of a budget. The name must be unique within an account. The : and \\ characters aren\'t allowed in BudgetName .\n\nBudgetLimit (dict) --The total amount of cost, usage, RI utilization, RI coverage, Savings Plans utilization, or Savings Plans coverage that you want to track with your budget.\n\nBudgetLimit is required for cost or usage budgets, but optional for RI or Savings Plans utilization or coverage budgets. RI and Savings Plans utilization or coverage budgets default to 100 , which is the only valid value for RI or Savings Plans utilization or coverage budgets. You can\'t use BudgetLimit with PlannedBudgetLimits for CreateBudget and UpdateBudget actions.\n\nAmount (string) -- [REQUIRED]The cost or usage amount that is associated with a budget forecast, actual spend, or budget threshold.\n\nUnit (string) -- [REQUIRED]The unit of measurement that is used for the budget forecast, actual spend, or budget threshold, such as dollars or GB.\n\n\n\nPlannedBudgetLimits (dict) --A map containing multiple BudgetLimit , including current or future limits.\n\nPlannedBudgetLimits is available for cost or usage budget and supports monthly and quarterly TimeUnit .\nFor monthly budgets, provide 12 months of PlannedBudgetLimits values. This must start from the current month and include the next 11 months. The key is the start of the month, UTC in epoch seconds.\nFor quarterly budgets, provide 4 quarters of PlannedBudgetLimits value entries in standard calendar quarter increments. This must start from the current quarter and include the next 3 quarters. The key is the start of the quarter, UTC in epoch seconds.\nIf the planned budget expires before 12 months for monthly or 4 quarters for quarterly, provide the PlannedBudgetLimits values only for the remaining periods.\nIf the budget begins at a date in the future, provide PlannedBudgetLimits values from the start date of the budget.\nAfter all of the BudgetLimit values in PlannedBudgetLimits are used, the budget continues to use the last limit as the BudgetLimit . At that point, the planned budget provides the same experience as a fixed budget.\n\nDescribeBudget and DescribeBudgets response along with PlannedBudgetLimits will also contain BudgetLimit representing the current month or quarter limit present in PlannedBudgetLimits . This only applies to budgets created with PlannedBudgetLimits . Budgets created without PlannedBudgetLimits will only contain BudgetLimit , and no PlannedBudgetLimits .\n\n(string) --A generic string.\n\n(dict) --The amount of cost or usage that is measured for a budget.\nFor example, a Spend for 3 GB of S3 usage would have the following parameters:\n\nAn Amount of 3\nA unit of GB\n\n\nAmount (string) -- [REQUIRED]The cost or usage amount that is associated with a budget forecast, actual spend, or budget threshold.\n\nUnit (string) -- [REQUIRED]The unit of measurement that is used for the budget forecast, actual spend, or budget threshold, such as dollars or GB.\n\n\n\n\n\n\n\nCostFilters (dict) --The cost filters, such as service or tag, that are applied to a budget.\nAWS Budgets supports the following services as a filter for RI budgets:\n\nAmazon Elastic Compute Cloud - Compute\nAmazon Redshift\nAmazon Relational Database Service\nAmazon ElastiCache\nAmazon Elasticsearch Service\n\n\n(string) --A generic string.\n\n(list) --\n(string) --A generic string.\n\n\n\n\n\n\n\nCostTypes (dict) --The types of costs that are included in this COST budget.\n\nUSAGE , RI_UTILIZATION , RI_COVERAGE , Savings_Plans_Utilization , and Savings_Plans_Coverage budgets do not have CostTypes .\n\nIncludeTax (boolean) --Specifies whether a budget includes taxes.\nThe default value is true .\n\nIncludeSubscription (boolean) --Specifies whether a budget includes subscriptions.\nThe default value is true .\n\nUseBlended (boolean) --Specifies whether a budget uses a blended rate.\nThe default value is false .\n\nIncludeRefund (boolean) --Specifies whether a budget includes refunds.\nThe default value is true .\n\nIncludeCredit (boolean) --Specifies whether a budget includes credits.\nThe default value is true .\n\nIncludeUpfront (boolean) --Specifies whether a budget includes upfront RI costs.\nThe default value is true .\n\nIncludeRecurring (boolean) --Specifies whether a budget includes recurring fees such as monthly RI fees.\nThe default value is true .\n\nIncludeOtherSubscription (boolean) --Specifies whether a budget includes non-RI subscription costs.\nThe default value is true .\n\nIncludeSupport (boolean) --Specifies whether a budget includes support subscription fees.\nThe default value is true .\n\nIncludeDiscount (boolean) --Specifies whether a budget includes discounts.\nThe default value is true .\n\nUseAmortized (boolean) --Specifies whether a budget uses the amortized rate.\nThe default value is false .\n\n\n\nTimeUnit (string) -- [REQUIRED]The length of time until a budget resets the actual and forecasted spend. DAILY is available only for RI_UTILIZATION , RI_COVERAGE , Savings_Plans_Utilization , and Savings_Plans_Coverage budgets.\n\nTimePeriod (dict) --The period of time that is covered by a budget. The period has a start date and an end date. The start date must come before the end date. The end date must come before 06/15/87 00:00 UTC .\nIf you create your budget and don\'t specify a start date, AWS defaults to the start of your chosen time period (DAILY, MONTHLY, QUARTERLY, or ANNUALLY). For example, if you created your budget on January 24, 2018, chose DAILY , and didn\'t set a start date, AWS set your start date to 01/24/18 00:00 UTC . If you chose MONTHLY , AWS set your start date to 01/01/18 00:00 UTC . If you didn\'t specify an end date, AWS set your end date to 06/15/87 00:00 UTC . The defaults are the same for the AWS Billing and Cost Management console and the API.\nYou can change either date with the UpdateBudget operation.\nAfter the end date, AWS deletes the budget and all associated notifications and subscribers.\n\nStart (datetime) --The start date for a budget. If you created your budget and didn\'t specify a start date, AWS defaults to the start of your chosen time period (DAILY, MONTHLY, QUARTERLY, or ANNUALLY). For example, if you created your budget on January 24, 2018, chose DAILY , and didn\'t set a start date, AWS set your start date to 01/24/18 00:00 UTC . If you chose MONTHLY , AWS set your start date to 01/01/18 00:00 UTC . The defaults are the same for the AWS Billing and Cost Management console and the API.\nYou can change your start date with the UpdateBudget operation.\n\nEnd (datetime) --The end date for a budget. If you didn\'t specify an end date, AWS set your end date to 06/15/87 00:00 UTC . The defaults are the same for the AWS Billing and Cost Management console and the API.\nAfter the end date, AWS deletes the budget and all associated notifications and subscribers. You can change your end date with the UpdateBudget operation.\n\n\n\nCalculatedSpend (dict) --The actual and forecasted cost or usage that the budget tracks.\n\nActualSpend (dict) -- [REQUIRED]The amount of cost, usage, or RI units that you have used.\n\nAmount (string) -- [REQUIRED]The cost or usage amount that is associated with a budget forecast, actual spend, or budget threshold.\n\nUnit (string) -- [REQUIRED]The unit of measurement that is used for the budget forecast, actual spend, or budget threshold, such as dollars or GB.\n\n\n\nForecastedSpend (dict) --The amount of cost, usage, or RI units that you are forecasted to use.\n\nAmount (string) -- [REQUIRED]The cost or usage amount that is associated with a budget forecast, actual spend, or budget threshold.\n\nUnit (string) -- [REQUIRED]The unit of measurement that is used for the budget forecast, actual spend, or budget threshold, such as dollars or GB.\n\n\n\n\n\nBudgetType (string) -- [REQUIRED]Whether this budget tracks costs, usage, RI utilization, RI coverage, Savings Plans utilization, or Savings Plans coverage.\n\nLastUpdatedTime (datetime) --The last time that you updated this budget.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
Response of UpdateBudget





Exceptions

Budgets.Client.exceptions.InternalErrorException
Budgets.Client.exceptions.InvalidParameterException
Budgets.Client.exceptions.NotFoundException
Budgets.Client.exceptions.AccessDeniedException


    :return: {}
    
    
    :returns: 
    Budgets.Client.exceptions.InternalErrorException
    Budgets.Client.exceptions.InvalidParameterException
    Budgets.Client.exceptions.NotFoundException
    Budgets.Client.exceptions.AccessDeniedException
    
    """
    pass

def update_notification(AccountId=None, BudgetName=None, OldNotification=None, NewNotification=None):
    """
    Updates a notification.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_notification(
        AccountId='string',
        BudgetName='string',
        OldNotification={
            'NotificationType': 'ACTUAL'|'FORECASTED',
            'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
            'Threshold': 123.0,
            'ThresholdType': 'PERCENTAGE'|'ABSOLUTE_VALUE',
            'NotificationState': 'OK'|'ALARM'
        },
        NewNotification={
            'NotificationType': 'ACTUAL'|'FORECASTED',
            'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
            'Threshold': 123.0,
            'ThresholdType': 'PERCENTAGE'|'ABSOLUTE_VALUE',
            'NotificationState': 'OK'|'ALARM'
        }
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe accountId that is associated with the budget whose notification you want to update.\n

    :type BudgetName: string
    :param BudgetName: [REQUIRED]\nThe name of the budget whose notification you want to update.\n

    :type OldNotification: dict
    :param OldNotification: [REQUIRED]\nThe previous notification that is associated with a budget.\n\nNotificationType (string) -- [REQUIRED]Whether the notification is for how much you have spent (ACTUAL ) or for how much you\'re forecasted to spend (FORECASTED ).\n\nComparisonOperator (string) -- [REQUIRED]The comparison that is used for this notification.\n\nThreshold (float) -- [REQUIRED]The threshold that is associated with a notification. Thresholds are always a percentage.\n\nThresholdType (string) --The type of threshold for a notification. For ABSOLUTE_VALUE thresholds, AWS notifies you when you go over or are forecasted to go over your total cost threshold. For PERCENTAGE thresholds, AWS notifies you when you go over or are forecasted to go over a certain percentage of your forecasted spend. For example, if you have a budget for 200 dollars and you have a PERCENTAGE threshold of 80%, AWS notifies you when you go over 160 dollars.\n\nNotificationState (string) --Whether this notification is in alarm. If a budget notification is in the ALARM state, you have passed the set threshold for the budget.\n\n\n

    :type NewNotification: dict
    :param NewNotification: [REQUIRED]\nThe updated notification to be associated with a budget.\n\nNotificationType (string) -- [REQUIRED]Whether the notification is for how much you have spent (ACTUAL ) or for how much you\'re forecasted to spend (FORECASTED ).\n\nComparisonOperator (string) -- [REQUIRED]The comparison that is used for this notification.\n\nThreshold (float) -- [REQUIRED]The threshold that is associated with a notification. Thresholds are always a percentage.\n\nThresholdType (string) --The type of threshold for a notification. For ABSOLUTE_VALUE thresholds, AWS notifies you when you go over or are forecasted to go over your total cost threshold. For PERCENTAGE thresholds, AWS notifies you when you go over or are forecasted to go over a certain percentage of your forecasted spend. For example, if you have a budget for 200 dollars and you have a PERCENTAGE threshold of 80%, AWS notifies you when you go over 160 dollars.\n\nNotificationState (string) --Whether this notification is in alarm. If a budget notification is in the ALARM state, you have passed the set threshold for the budget.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
Response of UpdateNotification





Exceptions

Budgets.Client.exceptions.InternalErrorException
Budgets.Client.exceptions.InvalidParameterException
Budgets.Client.exceptions.NotFoundException
Budgets.Client.exceptions.DuplicateRecordException
Budgets.Client.exceptions.AccessDeniedException


    :return: {}
    
    
    :returns: 
    Budgets.Client.exceptions.InternalErrorException
    Budgets.Client.exceptions.InvalidParameterException
    Budgets.Client.exceptions.NotFoundException
    Budgets.Client.exceptions.DuplicateRecordException
    Budgets.Client.exceptions.AccessDeniedException
    
    """
    pass

def update_subscriber(AccountId=None, BudgetName=None, Notification=None, OldSubscriber=None, NewSubscriber=None):
    """
    Updates a subscriber.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_subscriber(
        AccountId='string',
        BudgetName='string',
        Notification={
            'NotificationType': 'ACTUAL'|'FORECASTED',
            'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
            'Threshold': 123.0,
            'ThresholdType': 'PERCENTAGE'|'ABSOLUTE_VALUE',
            'NotificationState': 'OK'|'ALARM'
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
    :param AccountId: [REQUIRED]\nThe accountId that is associated with the budget whose subscriber you want to update.\n

    :type BudgetName: string
    :param BudgetName: [REQUIRED]\nThe name of the budget whose subscriber you want to update.\n

    :type Notification: dict
    :param Notification: [REQUIRED]\nThe notification whose subscriber you want to update.\n\nNotificationType (string) -- [REQUIRED]Whether the notification is for how much you have spent (ACTUAL ) or for how much you\'re forecasted to spend (FORECASTED ).\n\nComparisonOperator (string) -- [REQUIRED]The comparison that is used for this notification.\n\nThreshold (float) -- [REQUIRED]The threshold that is associated with a notification. Thresholds are always a percentage.\n\nThresholdType (string) --The type of threshold for a notification. For ABSOLUTE_VALUE thresholds, AWS notifies you when you go over or are forecasted to go over your total cost threshold. For PERCENTAGE thresholds, AWS notifies you when you go over or are forecasted to go over a certain percentage of your forecasted spend. For example, if you have a budget for 200 dollars and you have a PERCENTAGE threshold of 80%, AWS notifies you when you go over 160 dollars.\n\nNotificationState (string) --Whether this notification is in alarm. If a budget notification is in the ALARM state, you have passed the set threshold for the budget.\n\n\n

    :type OldSubscriber: dict
    :param OldSubscriber: [REQUIRED]\nThe previous subscriber that is associated with a budget notification.\n\nSubscriptionType (string) -- [REQUIRED]The type of notification that AWS sends to a subscriber.\n\nAddress (string) -- [REQUIRED]The address that AWS sends budget notifications to, either an SNS topic or an email.\nWhen you create a subscriber, the value of Address can\'t contain line breaks.\n\n\n

    :type NewSubscriber: dict
    :param NewSubscriber: [REQUIRED]\nThe updated subscriber that is associated with a budget notification.\n\nSubscriptionType (string) -- [REQUIRED]The type of notification that AWS sends to a subscriber.\n\nAddress (string) -- [REQUIRED]The address that AWS sends budget notifications to, either an SNS topic or an email.\nWhen you create a subscriber, the value of Address can\'t contain line breaks.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
Response of UpdateSubscriber





Exceptions

Budgets.Client.exceptions.InternalErrorException
Budgets.Client.exceptions.InvalidParameterException
Budgets.Client.exceptions.NotFoundException
Budgets.Client.exceptions.DuplicateRecordException
Budgets.Client.exceptions.AccessDeniedException


    :return: {}
    
    
    :returns: 
    Budgets.Client.exceptions.InternalErrorException
    Budgets.Client.exceptions.InvalidParameterException
    Budgets.Client.exceptions.NotFoundException
    Budgets.Client.exceptions.DuplicateRecordException
    Budgets.Client.exceptions.AccessDeniedException
    
    """
    pass

