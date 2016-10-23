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


def can_paginate(operation_name=None):
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
    pass


def create_budget(AccountId=None, Budget=None, NotificationsWithSubscribers=None):
    """
    :param AccountId: [REQUIRED] Account Id of the customer. It should be a 12 digit number.
    :type AccountId: string
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
            
    :type Budget: dict
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
            
            
    :type NotificationsWithSubscribers: list
    """
    pass


def create_notification(AccountId=None, BudgetName=None, Notification=None, Subscribers=None):
    """
    :param AccountId: [REQUIRED] Account Id of the customer. It should be a 12 digit number.
    :type AccountId: string
    :param BudgetName: [REQUIRED] A string represents the budget name. No ':' character is allowed.
    :type BudgetName: string
    :param Notification: [REQUIRED] Notification model. Each budget may contain multiple notifications with different settings.
            NotificationType (string) -- [REQUIRED] The type of a notification. It should be ACTUAL or FORECASTED.
            ComparisonOperator (string) -- [REQUIRED] The comparison operator of a notification. Currently we support less than, equal to and greater than.
            Threshold (float) -- [REQUIRED] The threshold of the a notification. It should be a number between 0 and 100.
            
    :type Notification: dict
    :param Subscribers: [REQUIRED] A list of subscribers.
            (dict) -- Subscriber model. Each notification may contain multiple subscribers with different addresses.
            SubscriptionType (string) -- [REQUIRED] The subscription type of the subscriber. It can be SMS or EMAIL.
            Address (string) -- [REQUIRED] A generic String.
            
    :type Subscribers: list
    """
    pass


def create_subscriber(AccountId=None, BudgetName=None, Notification=None, Subscriber=None):
    """
    :param AccountId: [REQUIRED] Account Id of the customer. It should be a 12 digit number.
    :type AccountId: string
    :param BudgetName: [REQUIRED] A string represents the budget name. No ':' character is allowed.
    :type BudgetName: string
    :param Notification: [REQUIRED] Notification model. Each budget may contain multiple notifications with different settings.
            NotificationType (string) -- [REQUIRED] The type of a notification. It should be ACTUAL or FORECASTED.
            ComparisonOperator (string) -- [REQUIRED] The comparison operator of a notification. Currently we support less than, equal to and greater than.
            Threshold (float) -- [REQUIRED] The threshold of the a notification. It should be a number between 0 and 100.
            
    :type Notification: dict
    :param Subscriber: [REQUIRED] Subscriber model. Each notification may contain multiple subscribers with different addresses.
            SubscriptionType (string) -- [REQUIRED] The subscription type of the subscriber. It can be SMS or EMAIL.
            Address (string) -- [REQUIRED] A generic String.
            
    :type Subscriber: dict
    """
    pass


def delete_budget(AccountId=None, BudgetName=None):
    """
    :param AccountId: [REQUIRED] Account Id of the customer. It should be a 12 digit number.
    :type AccountId: string
    :param BudgetName: [REQUIRED] A string represents the budget name. No ':' character is allowed.
    :type BudgetName: string
    """
    pass


def delete_notification(AccountId=None, BudgetName=None, Notification=None):
    """
    :param AccountId: [REQUIRED] Account Id of the customer. It should be a 12 digit number.
    :type AccountId: string
    :param BudgetName: [REQUIRED] A string represents the budget name. No ':' character is allowed.
    :type BudgetName: string
    :param Notification: [REQUIRED] Notification model. Each budget may contain multiple notifications with different settings.
            NotificationType (string) -- [REQUIRED] The type of a notification. It should be ACTUAL or FORECASTED.
            ComparisonOperator (string) -- [REQUIRED] The comparison operator of a notification. Currently we support less than, equal to and greater than.
            Threshold (float) -- [REQUIRED] The threshold of the a notification. It should be a number between 0 and 100.
            
    :type Notification: dict
    """
    pass


def delete_subscriber(AccountId=None, BudgetName=None, Notification=None, Subscriber=None):
    """
    :param AccountId: [REQUIRED] Account Id of the customer. It should be a 12 digit number.
    :type AccountId: string
    :param BudgetName: [REQUIRED] A string represents the budget name. No ':' character is allowed.
    :type BudgetName: string
    :param Notification: [REQUIRED] Notification model. Each budget may contain multiple notifications with different settings.
            NotificationType (string) -- [REQUIRED] The type of a notification. It should be ACTUAL or FORECASTED.
            ComparisonOperator (string) -- [REQUIRED] The comparison operator of a notification. Currently we support less than, equal to and greater than.
            Threshold (float) -- [REQUIRED] The threshold of the a notification. It should be a number between 0 and 100.
            
    :type Notification: dict
    :param Subscriber: [REQUIRED] Subscriber model. Each notification may contain multiple subscribers with different addresses.
            SubscriptionType (string) -- [REQUIRED] The subscription type of the subscriber. It can be SMS or EMAIL.
            Address (string) -- [REQUIRED] A generic String.
            
    :type Subscriber: dict
    """
    pass


def describe_budget(AccountId=None, BudgetName=None):
    """
    :param AccountId: [REQUIRED] Account Id of the customer. It should be a 12 digit number.
    :type AccountId: string
    :param BudgetName: [REQUIRED] A string represents the budget name. No ':' character is allowed.
    :type BudgetName: string
    """
    pass


def describe_budgets(AccountId=None, MaxResults=None, NextToken=None):
    """
    :param AccountId: [REQUIRED] Account Id of the customer. It should be a 12 digit number.
    :type AccountId: string
    :param MaxResults: An integer to represent how many entries should a pagianted response contains. Maxium is set to 100.
    :type MaxResults: integer
    :param NextToken: A generic String.
    :type NextToken: string
    """
    pass


def describe_notifications_for_budget(AccountId=None, BudgetName=None, MaxResults=None, NextToken=None):
    """
    :param AccountId: [REQUIRED] Account Id of the customer. It should be a 12 digit number.
    :type AccountId: string
    :param BudgetName: [REQUIRED] A string represents the budget name. No ':' character is allowed.
    :type BudgetName: string
    :param MaxResults: An integer to represent how many entries should a pagianted response contains. Maxium is set to 100.
    :type MaxResults: integer
    :param NextToken: A generic String.
    :type NextToken: string
    """
    pass


def describe_subscribers_for_notification(AccountId=None, BudgetName=None, Notification=None, MaxResults=None,
                                          NextToken=None):
    """
    :param AccountId: [REQUIRED] Account Id of the customer. It should be a 12 digit number.
    :type AccountId: string
    :param BudgetName: [REQUIRED] A string represents the budget name. No ':' character is allowed.
    :type BudgetName: string
    :param Notification: [REQUIRED] Notification model. Each budget may contain multiple notifications with different settings.
            NotificationType (string) -- [REQUIRED] The type of a notification. It should be ACTUAL or FORECASTED.
            ComparisonOperator (string) -- [REQUIRED] The comparison operator of a notification. Currently we support less than, equal to and greater than.
            Threshold (float) -- [REQUIRED] The threshold of the a notification. It should be a number between 0 and 100.
            
    :type Notification: dict
    :param MaxResults: An integer to represent how many entries should a pagianted response contains. Maxium is set to 100.
    :type MaxResults: integer
    :param NextToken: A generic String.
    :type NextToken: string
    """
    pass


def generate_presigned_url(ClientMethod=None, Params=None, ExpiresIn=None, HttpMethod=None):
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
    pass


def get_paginator(operation_name=None):
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
    pass


def get_waiter():
    """
    """
    pass


def update_budget(AccountId=None, NewBudget=None):
    """
    :param AccountId: [REQUIRED] Account Id of the customer. It should be a 12 digit number.
    :type AccountId: string
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
            
    :type NewBudget: dict
    """
    pass


def update_notification(AccountId=None, BudgetName=None, OldNotification=None, NewNotification=None):
    """
    :param AccountId: [REQUIRED] Account Id of the customer. It should be a 12 digit number.
    :type AccountId: string
    :param BudgetName: [REQUIRED] A string represents the budget name. No ':' character is allowed.
    :type BudgetName: string
    :param OldNotification: [REQUIRED] Notification model. Each budget may contain multiple notifications with different settings.
            NotificationType (string) -- [REQUIRED] The type of a notification. It should be ACTUAL or FORECASTED.
            ComparisonOperator (string) -- [REQUIRED] The comparison operator of a notification. Currently we support less than, equal to and greater than.
            Threshold (float) -- [REQUIRED] The threshold of the a notification. It should be a number between 0 and 100.
            
    :type OldNotification: dict
    :param NewNotification: [REQUIRED] Notification model. Each budget may contain multiple notifications with different settings.
            NotificationType (string) -- [REQUIRED] The type of a notification. It should be ACTUAL or FORECASTED.
            ComparisonOperator (string) -- [REQUIRED] The comparison operator of a notification. Currently we support less than, equal to and greater than.
            Threshold (float) -- [REQUIRED] The threshold of the a notification. It should be a number between 0 and 100.
            
    :type NewNotification: dict
    """
    pass


def update_subscriber(AccountId=None, BudgetName=None, Notification=None, OldSubscriber=None, NewSubscriber=None):
    """
    :param AccountId: [REQUIRED] Account Id of the customer. It should be a 12 digit number.
    :type AccountId: string
    :param BudgetName: [REQUIRED] A string represents the budget name. No ':' character is allowed.
    :type BudgetName: string
    :param Notification: [REQUIRED] Notification model. Each budget may contain multiple notifications with different settings.
            NotificationType (string) -- [REQUIRED] The type of a notification. It should be ACTUAL or FORECASTED.
            ComparisonOperator (string) -- [REQUIRED] The comparison operator of a notification. Currently we support less than, equal to and greater than.
            Threshold (float) -- [REQUIRED] The threshold of the a notification. It should be a number between 0 and 100.
            
    :type Notification: dict
    :param OldSubscriber: [REQUIRED] Subscriber model. Each notification may contain multiple subscribers with different addresses.
            SubscriptionType (string) -- [REQUIRED] The subscription type of the subscriber. It can be SMS or EMAIL.
            Address (string) -- [REQUIRED] A generic String.
            
    :type OldSubscriber: dict
    :param NewSubscriber: [REQUIRED] Subscriber model. Each notification may contain multiple subscribers with different addresses.
            SubscriptionType (string) -- [REQUIRED] The subscription type of the subscriber. It can be SMS or EMAIL.
            Address (string) -- [REQUIRED] A generic String.
            
    :type NewSubscriber: dict
    """
    pass
