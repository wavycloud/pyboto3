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
    Create a new budget
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
                'UseBlended': True|False
            },
            'TimeUnit': 'MONTHLY'|'QUARTERLY'|'ANNUALLY',
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
            'BudgetType': 'USAGE'|'COST'
        },
        NotificationsWithSubscribers=[
            {
                'Notification': {
                    'NotificationType': 'ACTUAL'|'FORECASTED',
                    'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
                    'Threshold': 123.0
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
    :param AccountId: [REQUIRED] Account Id of the customer. It should be a 12 digit number.

    :type Budget: dict
    :param Budget: [REQUIRED] AWS Budget model
            BudgetName (string) -- [REQUIRED] A string represents the budget name. No ':' character is allowed.
            BudgetLimit (dict) -- [REQUIRED] A structure represent either a cost spend or usage spend. Contains an amount and a unit.
            Amount (string) -- [REQUIRED] A string to represent NumericValue.
            Unit (string) -- [REQUIRED] A generic String.
            CostFilters (dict) -- A map represents the cost filters applied to the budget.
            (string) -- A generic String.
            (list) --
            (string) -- A generic String.
            
            CostTypes (dict) -- [REQUIRED] This includes the options for getting the cost of a budget.
            IncludeTax (boolean) -- [REQUIRED] A generic boolean value.
            IncludeSubscription (boolean) -- [REQUIRED] A generic boolean value.
            UseBlended (boolean) -- [REQUIRED] A generic boolean value.
            TimeUnit (string) -- [REQUIRED] The time unit of the budget. e.g. weekly, monthly, etc.
            TimePeriod (dict) -- [REQUIRED] A time period indicated the start date and end date of a budget.
            Start (datetime) -- [REQUIRED] A generic timestamp. In Java it is transformed to a Date object.
            End (datetime) -- [REQUIRED] A generic timestamp. In Java it is transformed to a Date object.
            CalculatedSpend (dict) -- A structure holds the actual and forecasted spend for a budget.
            ActualSpend (dict) -- [REQUIRED] A structure represent either a cost spend or usage spend. Contains an amount and a unit.
            Amount (string) -- [REQUIRED] A string to represent NumericValue.
            Unit (string) -- [REQUIRED] A generic String.
            ForecastedSpend (dict) -- A structure represent either a cost spend or usage spend. Contains an amount and a unit.
            Amount (string) -- [REQUIRED] A string to represent NumericValue.
            Unit (string) -- [REQUIRED] A generic String.
            
            BudgetType (string) -- [REQUIRED] The type of a budget. Can be COST or USAGE.
            

    :type NotificationsWithSubscribers: list
    :param NotificationsWithSubscribers: A list of Notifications, each with a list of subscribers.
            (dict) -- A structure to relate notification and a list of subscribers who belong to the notification.
            Notification (dict) -- [REQUIRED] Notification model. Each budget may contain multiple notifications with different settings.
            NotificationType (string) -- [REQUIRED] The type of a notification. It should be ACTUAL or FORECASTED.
            ComparisonOperator (string) -- [REQUIRED] The comparison operator of a notification. Currently we support less than, equal to and greater than.
            Threshold (float) -- [REQUIRED] The threshold of the a notification. It should be a number between 0 and 100.
            Subscribers (list) -- [REQUIRED] A list of subscribers.
            (dict) -- Subscriber model. Each notification may contain multiple subscribers with different addresses.
            SubscriptionType (string) -- [REQUIRED] The subscription type of the subscriber. It can be SMS or EMAIL.
            Address (string) -- [REQUIRED] A generic String.
            
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) -- Response of CreateBudget
    
    """
    pass

def create_notification(AccountId=None, BudgetName=None, Notification=None, Subscribers=None):
    """
    Create a new Notification with subscribers for a budget
    See also: AWS API Documentation
    
    
    :example: response = client.create_notification(
        AccountId='string',
        BudgetName='string',
        Notification={
            'NotificationType': 'ACTUAL'|'FORECASTED',
            'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
            'Threshold': 123.0
        },
        Subscribers=[
            {
                'SubscriptionType': 'SNS'|'EMAIL',
                'Address': 'string'
            },
        ]
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED] Account Id of the customer. It should be a 12 digit number.

    :type BudgetName: string
    :param BudgetName: [REQUIRED] A string represents the budget name. No ':' character is allowed.

    :type Notification: dict
    :param Notification: [REQUIRED] Notification model. Each budget may contain multiple notifications with different settings.
            NotificationType (string) -- [REQUIRED] The type of a notification. It should be ACTUAL or FORECASTED.
            ComparisonOperator (string) -- [REQUIRED] The comparison operator of a notification. Currently we support less than, equal to and greater than.
            Threshold (float) -- [REQUIRED] The threshold of the a notification. It should be a number between 0 and 100.
            

    :type Subscribers: list
    :param Subscribers: [REQUIRED] A list of subscribers.
            (dict) -- Subscriber model. Each notification may contain multiple subscribers with different addresses.
            SubscriptionType (string) -- [REQUIRED] The subscription type of the subscriber. It can be SMS or EMAIL.
            Address (string) -- [REQUIRED] A generic String.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) -- Response of CreateNotification
    
    """
    pass

def create_subscriber(AccountId=None, BudgetName=None, Notification=None, Subscriber=None):
    """
    Create a new Subscriber for a notification
    See also: AWS API Documentation
    
    
    :example: response = client.create_subscriber(
        AccountId='string',
        BudgetName='string',
        Notification={
            'NotificationType': 'ACTUAL'|'FORECASTED',
            'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
            'Threshold': 123.0
        },
        Subscriber={
            'SubscriptionType': 'SNS'|'EMAIL',
            'Address': 'string'
        }
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED] Account Id of the customer. It should be a 12 digit number.

    :type BudgetName: string
    :param BudgetName: [REQUIRED] A string represents the budget name. No ':' character is allowed.

    :type Notification: dict
    :param Notification: [REQUIRED] Notification model. Each budget may contain multiple notifications with different settings.
            NotificationType (string) -- [REQUIRED] The type of a notification. It should be ACTUAL or FORECASTED.
            ComparisonOperator (string) -- [REQUIRED] The comparison operator of a notification. Currently we support less than, equal to and greater than.
            Threshold (float) -- [REQUIRED] The threshold of the a notification. It should be a number between 0 and 100.
            

    :type Subscriber: dict
    :param Subscriber: [REQUIRED] Subscriber model. Each notification may contain multiple subscribers with different addresses.
            SubscriptionType (string) -- [REQUIRED] The subscription type of the subscriber. It can be SMS or EMAIL.
            Address (string) -- [REQUIRED] A generic String.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) -- Response of CreateSubscriber
    
    """
    pass

def delete_budget(AccountId=None, BudgetName=None):
    """
    Delete a budget and related notifications
    See also: AWS API Documentation
    
    
    :example: response = client.delete_budget(
        AccountId='string',
        BudgetName='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED] Account Id of the customer. It should be a 12 digit number.

    :type BudgetName: string
    :param BudgetName: [REQUIRED] A string represents the budget name. No ':' character is allowed.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) -- Response of DeleteBudget
    
    """
    pass

def delete_notification(AccountId=None, BudgetName=None, Notification=None):
    """
    Delete a notification and related subscribers
    See also: AWS API Documentation
    
    
    :example: response = client.delete_notification(
        AccountId='string',
        BudgetName='string',
        Notification={
            'NotificationType': 'ACTUAL'|'FORECASTED',
            'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
            'Threshold': 123.0
        }
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED] Account Id of the customer. It should be a 12 digit number.

    :type BudgetName: string
    :param BudgetName: [REQUIRED] A string represents the budget name. No ':' character is allowed.

    :type Notification: dict
    :param Notification: [REQUIRED] Notification model. Each budget may contain multiple notifications with different settings.
            NotificationType (string) -- [REQUIRED] The type of a notification. It should be ACTUAL or FORECASTED.
            ComparisonOperator (string) -- [REQUIRED] The comparison operator of a notification. Currently we support less than, equal to and greater than.
            Threshold (float) -- [REQUIRED] The threshold of the a notification. It should be a number between 0 and 100.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) -- Response of DeleteNotification
    
    """
    pass

def delete_subscriber(AccountId=None, BudgetName=None, Notification=None, Subscriber=None):
    """
    Delete a Subscriber for a notification
    See also: AWS API Documentation
    
    
    :example: response = client.delete_subscriber(
        AccountId='string',
        BudgetName='string',
        Notification={
            'NotificationType': 'ACTUAL'|'FORECASTED',
            'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
            'Threshold': 123.0
        },
        Subscriber={
            'SubscriptionType': 'SNS'|'EMAIL',
            'Address': 'string'
        }
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED] Account Id of the customer. It should be a 12 digit number.

    :type BudgetName: string
    :param BudgetName: [REQUIRED] A string represents the budget name. No ':' character is allowed.

    :type Notification: dict
    :param Notification: [REQUIRED] Notification model. Each budget may contain multiple notifications with different settings.
            NotificationType (string) -- [REQUIRED] The type of a notification. It should be ACTUAL or FORECASTED.
            ComparisonOperator (string) -- [REQUIRED] The comparison operator of a notification. Currently we support less than, equal to and greater than.
            Threshold (float) -- [REQUIRED] The threshold of the a notification. It should be a number between 0 and 100.
            

    :type Subscriber: dict
    :param Subscriber: [REQUIRED] Subscriber model. Each notification may contain multiple subscribers with different addresses.
            SubscriptionType (string) -- [REQUIRED] The subscription type of the subscriber. It can be SMS or EMAIL.
            Address (string) -- [REQUIRED] A generic String.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) -- Response of DeleteSubscriber
    
    """
    pass

def describe_budget(AccountId=None, BudgetName=None):
    """
    Get a single budget
    See also: AWS API Documentation
    
    
    :example: response = client.describe_budget(
        AccountId='string',
        BudgetName='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED] Account Id of the customer. It should be a 12 digit number.

    :type BudgetName: string
    :param BudgetName: [REQUIRED] A string represents the budget name. No ':' character is allowed.

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
                'UseBlended': True|False
            },
            'TimeUnit': 'MONTHLY'|'QUARTERLY'|'ANNUALLY',
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
            'BudgetType': 'USAGE'|'COST'
        }
    }
    
    
    :returns: 
    (dict) -- Response of DescribeBudget
    Budget (dict) -- AWS Budget model
    BudgetName (string) -- A string represents the budget name. No ":" character is allowed.
    BudgetLimit (dict) -- A structure represent either a cost spend or usage spend. Contains an amount and a unit.
    Amount (string) -- A string to represent NumericValue.
    Unit (string) -- A generic String.
    
    
    CostFilters (dict) -- A map represents the cost filters applied to the budget.
    (string) -- A generic String.
    (list) --
    (string) -- A generic String.
    
    
    
    
    
    
    CostTypes (dict) -- This includes the options for getting the cost of a budget.
    IncludeTax (boolean) -- A generic boolean value.
    IncludeSubscription (boolean) -- A generic boolean value.
    UseBlended (boolean) -- A generic boolean value.
    
    
    TimeUnit (string) -- The time unit of the budget. e.g. weekly, monthly, etc.
    TimePeriod (dict) -- A time period indicated the start date and end date of a budget.
    Start (datetime) -- A generic timestamp. In Java it is transformed to a Date object.
    End (datetime) -- A generic timestamp. In Java it is transformed to a Date object.
    
    
    CalculatedSpend (dict) -- A structure holds the actual and forecasted spend for a budget.
    ActualSpend (dict) -- A structure represent either a cost spend or usage spend. Contains an amount and a unit.
    Amount (string) -- A string to represent NumericValue.
    Unit (string) -- A generic String.
    
    
    ForecastedSpend (dict) -- A structure represent either a cost spend or usage spend. Contains an amount and a unit.
    Amount (string) -- A string to represent NumericValue.
    Unit (string) -- A generic String.
    
    
    
    
    BudgetType (string) -- The type of a budget. Can be COST or USAGE.
    
    
    
    
    
    """
    pass

def describe_budgets(AccountId=None, MaxResults=None, NextToken=None):
    """
    Get all budgets for an account
    See also: AWS API Documentation
    
    
    :example: response = client.describe_budgets(
        AccountId='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED] Account Id of the customer. It should be a 12 digit number.

    :type MaxResults: integer
    :param MaxResults: An integer to represent how many entries should a pagianted response contains. Maxium is set to 100.

    :type NextToken: string
    :param NextToken: A generic String.

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
                    'UseBlended': True|False
                },
                'TimeUnit': 'MONTHLY'|'QUARTERLY'|'ANNUALLY',
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
                'BudgetType': 'USAGE'|'COST'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (dict) -- Response of DescribeBudgets
    Budgets (list) -- A list of budgets
    (dict) -- AWS Budget model
    BudgetName (string) -- A string represents the budget name. No ":" character is allowed.
    BudgetLimit (dict) -- A structure represent either a cost spend or usage spend. Contains an amount and a unit.
    Amount (string) -- A string to represent NumericValue.
    Unit (string) -- A generic String.
    
    
    CostFilters (dict) -- A map represents the cost filters applied to the budget.
    (string) -- A generic String.
    (list) --
    (string) -- A generic String.
    
    
    
    
    
    
    CostTypes (dict) -- This includes the options for getting the cost of a budget.
    IncludeTax (boolean) -- A generic boolean value.
    IncludeSubscription (boolean) -- A generic boolean value.
    UseBlended (boolean) -- A generic boolean value.
    
    
    TimeUnit (string) -- The time unit of the budget. e.g. weekly, monthly, etc.
    TimePeriod (dict) -- A time period indicated the start date and end date of a budget.
    Start (datetime) -- A generic timestamp. In Java it is transformed to a Date object.
    End (datetime) -- A generic timestamp. In Java it is transformed to a Date object.
    
    
    CalculatedSpend (dict) -- A structure holds the actual and forecasted spend for a budget.
    ActualSpend (dict) -- A structure represent either a cost spend or usage spend. Contains an amount and a unit.
    Amount (string) -- A string to represent NumericValue.
    Unit (string) -- A generic String.
    
    
    ForecastedSpend (dict) -- A structure represent either a cost spend or usage spend. Contains an amount and a unit.
    Amount (string) -- A string to represent NumericValue.
    Unit (string) -- A generic String.
    
    
    
    
    BudgetType (string) -- The type of a budget. Can be COST or USAGE.
    
    
    
    
    NextToken (string) -- A generic String.
    
    
    
    """
    pass

def describe_notifications_for_budget(AccountId=None, BudgetName=None, MaxResults=None, NextToken=None):
    """
    Get notifications of a budget
    See also: AWS API Documentation
    
    
    :example: response = client.describe_notifications_for_budget(
        AccountId='string',
        BudgetName='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED] Account Id of the customer. It should be a 12 digit number.

    :type BudgetName: string
    :param BudgetName: [REQUIRED] A string represents the budget name. No ':' character is allowed.

    :type MaxResults: integer
    :param MaxResults: An integer to represent how many entries should a pagianted response contains. Maxium is set to 100.

    :type NextToken: string
    :param NextToken: A generic String.

    :rtype: dict
    :return: {
        'Notifications': [
            {
                'NotificationType': 'ACTUAL'|'FORECASTED',
                'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
                'Threshold': 123.0
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (dict) -- Response of GetNotificationsForBudget
    Notifications (list) -- A list of notifications.
    (dict) -- Notification model. Each budget may contain multiple notifications with different settings.
    NotificationType (string) -- The type of a notification. It should be ACTUAL or FORECASTED.
    ComparisonOperator (string) -- The comparison operator of a notification. Currently we support less than, equal to and greater than.
    Threshold (float) -- The threshold of the a notification. It should be a number between 0 and 100.
    
    
    
    
    NextToken (string) -- A generic String.
    
    
    
    """
    pass

def describe_subscribers_for_notification(AccountId=None, BudgetName=None, Notification=None, MaxResults=None, NextToken=None):
    """
    Get subscribers of a notification
    See also: AWS API Documentation
    
    
    :example: response = client.describe_subscribers_for_notification(
        AccountId='string',
        BudgetName='string',
        Notification={
            'NotificationType': 'ACTUAL'|'FORECASTED',
            'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
            'Threshold': 123.0
        },
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED] Account Id of the customer. It should be a 12 digit number.

    :type BudgetName: string
    :param BudgetName: [REQUIRED] A string represents the budget name. No ':' character is allowed.

    :type Notification: dict
    :param Notification: [REQUIRED] Notification model. Each budget may contain multiple notifications with different settings.
            NotificationType (string) -- [REQUIRED] The type of a notification. It should be ACTUAL or FORECASTED.
            ComparisonOperator (string) -- [REQUIRED] The comparison operator of a notification. Currently we support less than, equal to and greater than.
            Threshold (float) -- [REQUIRED] The threshold of the a notification. It should be a number between 0 and 100.
            

    :type MaxResults: integer
    :param MaxResults: An integer to represent how many entries should a pagianted response contains. Maxium is set to 100.

    :type NextToken: string
    :param NextToken: A generic String.

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
    (dict) -- Response of DescribeSubscribersForNotification
    Subscribers (list) -- A list of subscribers.
    (dict) -- Subscriber model. Each notification may contain multiple subscribers with different addresses.
    SubscriptionType (string) -- The subscription type of the subscriber. It can be SMS or EMAIL.
    Address (string) -- A generic String.
    
    
    
    
    NextToken (string) -- A generic String.
    
    
    
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
    Update the information of a budget already created
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
                'UseBlended': True|False
            },
            'TimeUnit': 'MONTHLY'|'QUARTERLY'|'ANNUALLY',
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
            'BudgetType': 'USAGE'|'COST'
        }
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED] Account Id of the customer. It should be a 12 digit number.

    :type NewBudget: dict
    :param NewBudget: [REQUIRED] AWS Budget model
            BudgetName (string) -- [REQUIRED] A string represents the budget name. No ':' character is allowed.
            BudgetLimit (dict) -- [REQUIRED] A structure represent either a cost spend or usage spend. Contains an amount and a unit.
            Amount (string) -- [REQUIRED] A string to represent NumericValue.
            Unit (string) -- [REQUIRED] A generic String.
            CostFilters (dict) -- A map represents the cost filters applied to the budget.
            (string) -- A generic String.
            (list) --
            (string) -- A generic String.
            
            CostTypes (dict) -- [REQUIRED] This includes the options for getting the cost of a budget.
            IncludeTax (boolean) -- [REQUIRED] A generic boolean value.
            IncludeSubscription (boolean) -- [REQUIRED] A generic boolean value.
            UseBlended (boolean) -- [REQUIRED] A generic boolean value.
            TimeUnit (string) -- [REQUIRED] The time unit of the budget. e.g. weekly, monthly, etc.
            TimePeriod (dict) -- [REQUIRED] A time period indicated the start date and end date of a budget.
            Start (datetime) -- [REQUIRED] A generic timestamp. In Java it is transformed to a Date object.
            End (datetime) -- [REQUIRED] A generic timestamp. In Java it is transformed to a Date object.
            CalculatedSpend (dict) -- A structure holds the actual and forecasted spend for a budget.
            ActualSpend (dict) -- [REQUIRED] A structure represent either a cost spend or usage spend. Contains an amount and a unit.
            Amount (string) -- [REQUIRED] A string to represent NumericValue.
            Unit (string) -- [REQUIRED] A generic String.
            ForecastedSpend (dict) -- A structure represent either a cost spend or usage spend. Contains an amount and a unit.
            Amount (string) -- [REQUIRED] A string to represent NumericValue.
            Unit (string) -- [REQUIRED] A generic String.
            
            BudgetType (string) -- [REQUIRED] The type of a budget. Can be COST or USAGE.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) -- Response of UpdateBudget
    
    """
    pass

def update_notification(AccountId=None, BudgetName=None, OldNotification=None, NewNotification=None):
    """
    Update the information about a notification already created
    See also: AWS API Documentation
    
    
    :example: response = client.update_notification(
        AccountId='string',
        BudgetName='string',
        OldNotification={
            'NotificationType': 'ACTUAL'|'FORECASTED',
            'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
            'Threshold': 123.0
        },
        NewNotification={
            'NotificationType': 'ACTUAL'|'FORECASTED',
            'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
            'Threshold': 123.0
        }
    )
    
    
    :type AccountId: string
    :param AccountId: [REQUIRED] Account Id of the customer. It should be a 12 digit number.

    :type BudgetName: string
    :param BudgetName: [REQUIRED] A string represents the budget name. No ':' character is allowed.

    :type OldNotification: dict
    :param OldNotification: [REQUIRED] Notification model. Each budget may contain multiple notifications with different settings.
            NotificationType (string) -- [REQUIRED] The type of a notification. It should be ACTUAL or FORECASTED.
            ComparisonOperator (string) -- [REQUIRED] The comparison operator of a notification. Currently we support less than, equal to and greater than.
            Threshold (float) -- [REQUIRED] The threshold of the a notification. It should be a number between 0 and 100.
            

    :type NewNotification: dict
    :param NewNotification: [REQUIRED] Notification model. Each budget may contain multiple notifications with different settings.
            NotificationType (string) -- [REQUIRED] The type of a notification. It should be ACTUAL or FORECASTED.
            ComparisonOperator (string) -- [REQUIRED] The comparison operator of a notification. Currently we support less than, equal to and greater than.
            Threshold (float) -- [REQUIRED] The threshold of the a notification. It should be a number between 0 and 100.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) -- Response of UpdateNotification
    
    """
    pass

def update_subscriber(AccountId=None, BudgetName=None, Notification=None, OldSubscriber=None, NewSubscriber=None):
    """
    Update a subscriber
    See also: AWS API Documentation
    
    
    :example: response = client.update_subscriber(
        AccountId='string',
        BudgetName='string',
        Notification={
            'NotificationType': 'ACTUAL'|'FORECASTED',
            'ComparisonOperator': 'GREATER_THAN'|'LESS_THAN'|'EQUAL_TO',
            'Threshold': 123.0
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
    :param AccountId: [REQUIRED] Account Id of the customer. It should be a 12 digit number.

    :type BudgetName: string
    :param BudgetName: [REQUIRED] A string represents the budget name. No ':' character is allowed.

    :type Notification: dict
    :param Notification: [REQUIRED] Notification model. Each budget may contain multiple notifications with different settings.
            NotificationType (string) -- [REQUIRED] The type of a notification. It should be ACTUAL or FORECASTED.
            ComparisonOperator (string) -- [REQUIRED] The comparison operator of a notification. Currently we support less than, equal to and greater than.
            Threshold (float) -- [REQUIRED] The threshold of the a notification. It should be a number between 0 and 100.
            

    :type OldSubscriber: dict
    :param OldSubscriber: [REQUIRED] Subscriber model. Each notification may contain multiple subscribers with different addresses.
            SubscriptionType (string) -- [REQUIRED] The subscription type of the subscriber. It can be SMS or EMAIL.
            Address (string) -- [REQUIRED] A generic String.
            

    :type NewSubscriber: dict
    :param NewSubscriber: [REQUIRED] Subscriber model. Each notification may contain multiple subscribers with different addresses.
            SubscriptionType (string) -- [REQUIRED] The subscription type of the subscriber. It can be SMS or EMAIL.
            Address (string) -- [REQUIRED] A generic String.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) -- Response of UpdateSubscriber
    
    """
    pass

