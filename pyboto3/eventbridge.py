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

def activate_event_source(Name=None):
    """
    Activates a partner event source that has been deactivated. Once activated, your matching event bus will start receiving events from the event source.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.activate_event_source(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the partner event source to activate.\n

    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def create_event_bus(Name=None, EventSourceName=None, Tags=None):
    """
    Creates a new event bus within your account. This can be a custom event bus which you can use to receive events from your custom applications and services, or it can be a partner event bus which can be matched to a partner event source.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_event_bus(
        Name='string',
        EventSourceName='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the new event bus.\nEvent bus names cannot contain the / character. You can\'t use the name default for a custom event bus, as this name is already used for your account\'s default event bus.\nIf this is a partner event bus, the name must exactly match the name of the partner event source that this event bus is matched to.\n

    :type EventSourceName: string
    :param EventSourceName: If you are creating a partner event bus, this specifies the partner event source that the new event bus will be matched with.

    :type Tags: list
    :param Tags: Tags to associate with the event bus.\n\n(dict) --A key-value pair associated with an AWS resource. In EventBridge, rules and event buses support tagging.\n\nKey (string) -- [REQUIRED]A string you can use to assign a value. The combination of tag keys and values can help you organize and categorize your resources.\n\nValue (string) -- [REQUIRED]The value for the specified tag key.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'EventBusArn': 'string'
}


Response Structure

(dict) --

EventBusArn (string) --
The ARN of the new event bus.







Exceptions

EventBridge.Client.exceptions.ResourceAlreadyExistsException
EventBridge.Client.exceptions.ResourceNotFoundException
EventBridge.Client.exceptions.InvalidStateException
EventBridge.Client.exceptions.InternalException
EventBridge.Client.exceptions.ConcurrentModificationException
EventBridge.Client.exceptions.LimitExceededException


    :return: {
        'EventBusArn': 'string'
    }
    
    
    :returns: 
    EventBridge.Client.exceptions.ResourceAlreadyExistsException
    EventBridge.Client.exceptions.ResourceNotFoundException
    EventBridge.Client.exceptions.InvalidStateException
    EventBridge.Client.exceptions.InternalException
    EventBridge.Client.exceptions.ConcurrentModificationException
    EventBridge.Client.exceptions.LimitExceededException
    
    """
    pass

def create_partner_event_source(Name=None, Account=None):
    """
    Called by an SaaS partner to create a partner event source. This operation is not used by AWS customers.
    Each partner event source can be used by one AWS account to create a matching partner event bus in that AWS account. A SaaS partner must create one partner event source for each AWS account that wants to receive those event types.
    A partner event source creates events based on resources within the SaaS partner\'s service or application.
    An AWS account that creates a partner event bus that matches the partner event source can use that event bus to receive events from the partner, and then process them using AWS Events rules and targets.
    Partner event source names follow this format:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_partner_event_source(
        Name='string',
        Account='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the partner event source. This name must be unique and must be in the format `` partner_name /event_namespace /event_name `` . The AWS account that wants to use this partner event source must create a partner event bus with a name that matches the name of the partner event source.\n

    :type Account: string
    :param Account: [REQUIRED]\nThe AWS account ID that is permitted to create a matching partner event bus for this partner event source.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'EventSourceArn': 'string'
}


Response Structure

(dict) --

EventSourceArn (string) --
The ARN of the partner event source.







Exceptions

EventBridge.Client.exceptions.ResourceAlreadyExistsException
EventBridge.Client.exceptions.InternalException
EventBridge.Client.exceptions.ConcurrentModificationException
EventBridge.Client.exceptions.LimitExceededException


    :return: {
        'EventSourceArn': 'string'
    }
    
    
    :returns: 
    EventBridge.Client.exceptions.ResourceAlreadyExistsException
    EventBridge.Client.exceptions.InternalException
    EventBridge.Client.exceptions.ConcurrentModificationException
    EventBridge.Client.exceptions.LimitExceededException
    
    """
    pass

def deactivate_event_source(Name=None):
    """
    You can use this operation to temporarily stop receiving events from the specified partner event source. The matching event bus is not deleted.
    When you deactivate a partner event source, the source goes into PENDING state. If it remains in PENDING state for more than two weeks, it is deleted.
    To activate a deactivated partner event source, use  ActivateEventSource .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.deactivate_event_source(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the partner event source to deactivate.\n

    """
    pass

def delete_event_bus(Name=None):
    """
    Deletes the specified custom event bus or partner event bus. All rules associated with this event bus need to be deleted. You can\'t delete your account\'s default event bus.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_event_bus(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the event bus to delete.\n

    """
    pass

def delete_partner_event_source(Name=None, Account=None):
    """
    This operation is used by SaaS partners to delete a partner event source. This operation is not used by AWS customers.
    When you delete an event source, the status of the corresponding partner event bus in the AWS customer account becomes DELETED.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_partner_event_source(
        Name='string',
        Account='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the event source to delete.\n

    :type Account: string
    :param Account: [REQUIRED]\nThe AWS account ID of the AWS customer that the event source was created for.\n

    :returns: 
    EventBridge.Client.exceptions.InternalException
    EventBridge.Client.exceptions.ConcurrentModificationException
    
    """
    pass

def delete_rule(Name=None, EventBusName=None, Force=None):
    """
    Deletes the specified rule.
    Before you can delete the rule, you must remove all targets, using  RemoveTargets .
    When you delete a rule, incoming events might continue to match to the deleted rule. Allow a short period of time for changes to take effect.
    Managed rules are rules created and managed by another AWS service on your behalf. These rules are created by those other AWS services to support functionality in those services. You can delete these rules using the Force option, but you should do so only if you are sure the other service is not still using that rule.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_rule(
        Name='string',
        EventBusName='string',
        Force=True|False
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the rule.\n

    :type EventBusName: string
    :param EventBusName: The event bus associated with the rule. If you omit this, the default event bus is used.

    :type Force: boolean
    :param Force: If this is a managed rule, created by an AWS service on your behalf, you must specify Force as True to delete the rule. This parameter is ignored for rules that are not managed rules. You can check whether a rule is a managed rule by using DescribeRule or ListRules and checking the ManagedBy field of the response.

    :returns: 
    EventBridge.Client.exceptions.ConcurrentModificationException
    EventBridge.Client.exceptions.ManagedRuleException
    EventBridge.Client.exceptions.InternalException
    EventBridge.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def describe_event_bus(Name=None):
    """
    Displays details about an event bus in your account. This can include the external AWS accounts that are permitted to write events to your default event bus, and the associated policy. For custom event buses and partner event buses, it displays the name, ARN, policy, state, and creation time.
    To enable your account to receive events from other accounts on its default event bus, use  PutPermission .
    For more information about partner event buses, see  CreateEventBus .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_event_bus(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: The name of the event bus to show details for. If you omit this, the default event bus is displayed.

    :rtype: dict
ReturnsResponse Syntax{
    'Name': 'string',
    'Arn': 'string',
    'Policy': 'string'
}


Response Structure

(dict) --
Name (string) --The name of the event bus. Currently, this is always default .

Arn (string) --The Amazon Resource Name (ARN) of the account permitted to write events to the current account.

Policy (string) --The policy that enables the external account to send events to your account.






Exceptions

EventBridge.Client.exceptions.ResourceNotFoundException
EventBridge.Client.exceptions.InternalException


    :return: {
        'Name': 'string',
        'Arn': 'string',
        'Policy': 'string'
    }
    
    
    """
    pass

def describe_event_source(Name=None):
    """
    This operation lists details about a partner event source that is shared with your account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_event_source(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the partner event source to display the details of.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Arn': 'string',
    'CreatedBy': 'string',
    'CreationTime': datetime(2015, 1, 1),
    'ExpirationTime': datetime(2015, 1, 1),
    'Name': 'string',
    'State': 'PENDING'|'ACTIVE'|'DELETED'
}


Response Structure

(dict) --
Arn (string) --The ARN of the partner event source.

CreatedBy (string) --The name of the SaaS partner that created the event source.

CreationTime (datetime) --The date and time that the event source was created.

ExpirationTime (datetime) --The date and time that the event source will expire if you do not create a matching event bus.

Name (string) --The name of the partner event source.

State (string) --The state of the event source. If it is ACTIVE, you have already created a matching event bus for this event source, and that event bus is active. If it is PENDING, either you haven\'t yet created a matching event bus, or that event bus is deactivated. If it is DELETED, you have created a matching event bus, but the event source has since been deleted.






Exceptions

EventBridge.Client.exceptions.ResourceNotFoundException
EventBridge.Client.exceptions.InternalException


    :return: {
        'Arn': 'string',
        'CreatedBy': 'string',
        'CreationTime': datetime(2015, 1, 1),
        'ExpirationTime': datetime(2015, 1, 1),
        'Name': 'string',
        'State': 'PENDING'|'ACTIVE'|'DELETED'
    }
    
    
    """
    pass

def describe_partner_event_source(Name=None):
    """
    An SaaS partner can use this operation to list details about a partner event source that they have created. AWS customers do not use this operation. Instead, AWS customers can use  DescribeEventSource to see details about a partner event source that is shared with them.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_partner_event_source(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the event source to display.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Arn': 'string',
    'Name': 'string'
}


Response Structure

(dict) --
Arn (string) --The ARN of the event source.

Name (string) --The name of the event source.






Exceptions

EventBridge.Client.exceptions.ResourceNotFoundException
EventBridge.Client.exceptions.InternalException


    :return: {
        'Arn': 'string',
        'Name': 'string'
    }
    
    
    """
    pass

def describe_rule(Name=None, EventBusName=None):
    """
    Describes the specified rule.
    DescribeRule does not list the targets of a rule. To see the targets associated with a rule, use  ListTargetsByRule .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_rule(
        Name='string',
        EventBusName='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the rule.\n

    :type EventBusName: string
    :param EventBusName: The event bus associated with the rule. If you omit this, the default event bus is used.

    :rtype: dict

ReturnsResponse Syntax
{
    'Name': 'string',
    'Arn': 'string',
    'EventPattern': 'string',
    'ScheduleExpression': 'string',
    'State': 'ENABLED'|'DISABLED',
    'Description': 'string',
    'RoleArn': 'string',
    'ManagedBy': 'string',
    'EventBusName': 'string'
}


Response Structure

(dict) --

Name (string) --
The name of the rule.

Arn (string) --
The Amazon Resource Name (ARN) of the rule.

EventPattern (string) --
The event pattern. For more information, see Events and Event Patterns in the Amazon EventBridge User Guide .

ScheduleExpression (string) --
The scheduling expression. For example, "cron(0 20 * * ? *)", "rate(5 minutes)".

State (string) --
Specifies whether the rule is enabled or disabled.

Description (string) --
The description of the rule.

RoleArn (string) --
The Amazon Resource Name (ARN) of the IAM role associated with the rule.

ManagedBy (string) --
If this is a managed rule, created by an AWS service on your behalf, this field displays the principal name of the AWS service that created the rule.

EventBusName (string) --
The event bus associated with the rule.







Exceptions

EventBridge.Client.exceptions.ResourceNotFoundException
EventBridge.Client.exceptions.InternalException


    :return: {
        'Name': 'string',
        'Arn': 'string',
        'EventPattern': 'string',
        'ScheduleExpression': 'string',
        'State': 'ENABLED'|'DISABLED',
        'Description': 'string',
        'RoleArn': 'string',
        'ManagedBy': 'string',
        'EventBusName': 'string'
    }
    
    
    :returns: 
    EventBridge.Client.exceptions.ResourceNotFoundException
    EventBridge.Client.exceptions.InternalException
    
    """
    pass

def disable_rule(Name=None, EventBusName=None):
    """
    Disables the specified rule. A disabled rule won\'t match any events, and won\'t self-trigger if it has a schedule expression.
    When you disable a rule, incoming events might continue to match to the disabled rule. Allow a short period of time for changes to take effect.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disable_rule(
        Name='string',
        EventBusName='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the rule.\n

    :type EventBusName: string
    :param EventBusName: The event bus associated with the rule. If you omit this, the default event bus is used.

    :returns: 
    EventBridge.Client.exceptions.ResourceNotFoundException
    EventBridge.Client.exceptions.ConcurrentModificationException
    EventBridge.Client.exceptions.ManagedRuleException
    EventBridge.Client.exceptions.InternalException
    
    """
    pass

def enable_rule(Name=None, EventBusName=None):
    """
    Enables the specified rule. If the rule does not exist, the operation fails.
    When you enable a rule, incoming events might not immediately start matching to a newly enabled rule. Allow a short period of time for changes to take effect.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.enable_rule(
        Name='string',
        EventBusName='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the rule.\n

    :type EventBusName: string
    :param EventBusName: The event bus associated with the rule. If you omit this, the default event bus is used.

    :returns: 
    EventBridge.Client.exceptions.ResourceNotFoundException
    EventBridge.Client.exceptions.ConcurrentModificationException
    EventBridge.Client.exceptions.ManagedRuleException
    EventBridge.Client.exceptions.InternalException
    
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

def list_event_buses(NamePrefix=None, NextToken=None, Limit=None):
    """
    Lists all the event buses in your account, including the default event bus, custom event buses, and partner event buses.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_event_buses(
        NamePrefix='string',
        NextToken='string',
        Limit=123
    )
    
    
    :type NamePrefix: string
    :param NamePrefix: Specifying this limits the results to only those event buses with names that start with the specified prefix.

    :type NextToken: string
    :param NextToken: The token returned by a previous call to retrieve the next set of results.

    :type Limit: integer
    :param Limit: Specifying this limits the number of results returned by this operation. The operation also returns a NextToken which you can use in a subsequent operation to retrieve the next set of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'EventBuses': [
        {
            'Name': 'string',
            'Arn': 'string',
            'Policy': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

EventBuses (list) --
This list of event buses.

(dict) --
An event bus receives events from a source and routes them to rules associated with that event bus. Your account\'s default event bus receives rules from AWS services. A custom event bus can receive rules from AWS services as well as your custom applications and services. A partner event bus receives events from an event source created by an SaaS partner. These events come from the partners services or applications.

Name (string) --
The name of the event bus.

Arn (string) --
The ARN of the event bus.

Policy (string) --
The permissions policy of the event bus, describing which other AWS accounts can write events to this event bus.





NextToken (string) --
A token you can use in a subsequent operation to retrieve the next set of results.







Exceptions

EventBridge.Client.exceptions.InternalException


    :return: {
        'EventBuses': [
            {
                'Name': 'string',
                'Arn': 'string',
                'Policy': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    EventBridge.Client.exceptions.InternalException
    
    """
    pass

def list_event_sources(NamePrefix=None, NextToken=None, Limit=None):
    """
    You can use this to see all the partner event sources that have been shared with your AWS account. For more information about partner event sources, see  CreateEventBus .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_event_sources(
        NamePrefix='string',
        NextToken='string',
        Limit=123
    )
    
    
    :type NamePrefix: string
    :param NamePrefix: Specifying this limits the results to only those partner event sources with names that start with the specified prefix.

    :type NextToken: string
    :param NextToken: The token returned by a previous call to retrieve the next set of results.

    :type Limit: integer
    :param Limit: Specifying this limits the number of results returned by this operation. The operation also returns a NextToken which you can use in a subsequent operation to retrieve the next set of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'EventSources': [
        {
            'Arn': 'string',
            'CreatedBy': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'ExpirationTime': datetime(2015, 1, 1),
            'Name': 'string',
            'State': 'PENDING'|'ACTIVE'|'DELETED'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

EventSources (list) --
The list of event sources.

(dict) --
A partner event source is created by an SaaS partner. If a customer creates a partner event bus that matches this event source, that AWS account can receive events from the partner\'s applications or services.

Arn (string) --
The ARN of the event source.

CreatedBy (string) --
The name of the partner that created the event source.

CreationTime (datetime) --
The date and time the event source was created.

ExpirationTime (datetime) --
The date and time that the event source will expire, if the AWS account doesn\'t create a matching event bus for it.

Name (string) --
The name of the event source.

State (string) --
The state of the event source. If it is ACTIVE, you have already created a matching event bus for this event source, and that event bus is active. If it is PENDING, either you haven\'t yet created a matching event bus, or that event bus is deactivated. If it is DELETED, you have created a matching event bus, but the event source has since been deleted.





NextToken (string) --
A token you can use in a subsequent operation to retrieve the next set of results.







Exceptions

EventBridge.Client.exceptions.InternalException


    :return: {
        'EventSources': [
            {
                'Arn': 'string',
                'CreatedBy': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'ExpirationTime': datetime(2015, 1, 1),
                'Name': 'string',
                'State': 'PENDING'|'ACTIVE'|'DELETED'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    EventBridge.Client.exceptions.InternalException
    
    """
    pass

def list_partner_event_source_accounts(EventSourceName=None, NextToken=None, Limit=None):
    """
    An SaaS partner can use this operation to display the AWS account ID that a particular partner event source name is associated with. This operation is not used by AWS customers.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_partner_event_source_accounts(
        EventSourceName='string',
        NextToken='string',
        Limit=123
    )
    
    
    :type EventSourceName: string
    :param EventSourceName: [REQUIRED]\nThe name of the partner event source to display account information about.\n

    :type NextToken: string
    :param NextToken: The token returned by a previous call to this operation. Specifying this retrieves the next set of results.

    :type Limit: integer
    :param Limit: Specifying this limits the number of results returned by this operation. The operation also returns a NextToken which you can use in a subsequent operation to retrieve the next set of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'PartnerEventSourceAccounts': [
        {
            'Account': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'ExpirationTime': datetime(2015, 1, 1),
            'State': 'PENDING'|'ACTIVE'|'DELETED'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

PartnerEventSourceAccounts (list) --
The list of partner event sources returned by the operation.

(dict) --
The AWS account that a partner event source has been offered to.

Account (string) --
The AWS account ID that the partner event source was offered to.

CreationTime (datetime) --
The date and time the event source was created.

ExpirationTime (datetime) --
The date and time that the event source will expire, if the AWS account doesn\'t create a matching event bus for it.

State (string) --
The state of the event source. If it is ACTIVE, you have already created a matching event bus for this event source, and that event bus is active. If it is PENDING, either you haven\'t yet created a matching event bus, or that event bus is deactivated. If it is DELETED, you have created a matching event bus, but the event source has since been deleted.





NextToken (string) --
A token you can use in a subsequent operation to retrieve the next set of results.







Exceptions

EventBridge.Client.exceptions.ResourceNotFoundException
EventBridge.Client.exceptions.InternalException


    :return: {
        'PartnerEventSourceAccounts': [
            {
                'Account': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'ExpirationTime': datetime(2015, 1, 1),
                'State': 'PENDING'|'ACTIVE'|'DELETED'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    EventBridge.Client.exceptions.ResourceNotFoundException
    EventBridge.Client.exceptions.InternalException
    
    """
    pass

def list_partner_event_sources(NamePrefix=None, NextToken=None, Limit=None):
    """
    An SaaS partner can use this operation to list all the partner event source names that they have created. This operation is not used by AWS customers.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_partner_event_sources(
        NamePrefix='string',
        NextToken='string',
        Limit=123
    )
    
    
    :type NamePrefix: string
    :param NamePrefix: [REQUIRED]\nIf you specify this, the results are limited to only those partner event sources that start with the string you specify.\n

    :type NextToken: string
    :param NextToken: The token returned by a previous call to this operation. Specifying this retrieves the next set of results.

    :type Limit: integer
    :param Limit: pecifying this limits the number of results returned by this operation. The operation also returns a NextToken which you can use in a subsequent operation to retrieve the next set of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'PartnerEventSources': [
        {
            'Arn': 'string',
            'Name': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

PartnerEventSources (list) --
The list of partner event sources returned by the operation.

(dict) --
A partner event source is created by an SaaS partner. If a customer creates a partner event bus that matches this event source, that AWS account can receive events from the partner\'s applications or services.

Arn (string) --
The ARN of the partner event source.

Name (string) --
The name of the partner event source.





NextToken (string) --
A token you can use in a subsequent operation to retrieve the next set of results.







Exceptions

EventBridge.Client.exceptions.InternalException


    :return: {
        'PartnerEventSources': [
            {
                'Arn': 'string',
                'Name': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    EventBridge.Client.exceptions.InternalException
    
    """
    pass

def list_rule_names_by_target(TargetArn=None, EventBusName=None, NextToken=None, Limit=None):
    """
    Lists the rules for the specified target. You can see which of the rules in Amazon EventBridge can invoke a specific target in your account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_rule_names_by_target(
        TargetArn='string',
        EventBusName='string',
        NextToken='string',
        Limit=123
    )
    
    
    :type TargetArn: string
    :param TargetArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the target resource.\n

    :type EventBusName: string
    :param EventBusName: Limits the results to show only the rules associated with the specified event bus.

    :type NextToken: string
    :param NextToken: The token returned by a previous call to retrieve the next set of results.

    :type Limit: integer
    :param Limit: The maximum number of results to return.

    :rtype: dict

ReturnsResponse Syntax
{
    'RuleNames': [
        'string',
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

RuleNames (list) --
The names of the rules that can invoke the given target.

(string) --


NextToken (string) --
Indicates whether there are additional results to retrieve. If there are no more results, the value is null.







Exceptions

EventBridge.Client.exceptions.InternalException
EventBridge.Client.exceptions.ResourceNotFoundException


    :return: {
        'RuleNames': [
            'string',
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_rules(NamePrefix=None, EventBusName=None, NextToken=None, Limit=None):
    """
    Lists your Amazon EventBridge rules. You can either list all the rules or you can provide a prefix to match to the rule names.
    ListRules does not list the targets of a rule. To see the targets associated with a rule, use  ListTargetsByRule .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_rules(
        NamePrefix='string',
        EventBusName='string',
        NextToken='string',
        Limit=123
    )
    
    
    :type NamePrefix: string
    :param NamePrefix: The prefix matching the rule name.

    :type EventBusName: string
    :param EventBusName: Limits the results to show only the rules associated with the specified event bus.

    :type NextToken: string
    :param NextToken: The token returned by a previous call to retrieve the next set of results.

    :type Limit: integer
    :param Limit: The maximum number of results to return.

    :rtype: dict

ReturnsResponse Syntax
{
    'Rules': [
        {
            'Name': 'string',
            'Arn': 'string',
            'EventPattern': 'string',
            'State': 'ENABLED'|'DISABLED',
            'Description': 'string',
            'ScheduleExpression': 'string',
            'RoleArn': 'string',
            'ManagedBy': 'string',
            'EventBusName': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Rules (list) --
The rules that match the specified criteria.

(dict) --
Contains information about a rule in Amazon EventBridge.

Name (string) --
The name of the rule.

Arn (string) --
The Amazon Resource Name (ARN) of the rule.

EventPattern (string) --
The event pattern of the rule. For more information, see Events and Event Patterns in the Amazon EventBridge User Guide .

State (string) --
The state of the rule.

Description (string) --
The description of the rule.

ScheduleExpression (string) --
The scheduling expression. For example, "cron(0 20 * * ? *)", "rate(5 minutes)".

RoleArn (string) --
The Amazon Resource Name (ARN) of the role that is used for target invocation.

ManagedBy (string) --
If the rule was created on behalf of your account by an AWS service, this field displays the principal name of the service that created the rule.

EventBusName (string) --
The event bus associated with the rule.





NextToken (string) --
Indicates whether there are additional results to retrieve. If there are no more results, the value is null.







Exceptions

EventBridge.Client.exceptions.InternalException
EventBridge.Client.exceptions.ResourceNotFoundException


    :return: {
        'Rules': [
            {
                'Name': 'string',
                'Arn': 'string',
                'EventPattern': 'string',
                'State': 'ENABLED'|'DISABLED',
                'Description': 'string',
                'ScheduleExpression': 'string',
                'RoleArn': 'string',
                'ManagedBy': 'string',
                'EventBusName': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    EventBridge.Client.exceptions.InternalException
    EventBridge.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def list_tags_for_resource(ResourceARN=None):
    """
    Displays the tags associated with an EventBridge resource. In EventBridge, rules and event buses can be tagged.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        ResourceARN='string'
    )
    
    
    :type ResourceARN: string
    :param ResourceARN: [REQUIRED]\nThe ARN of the EventBridge resource for which you want to view tags.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Tags': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ]
}


Response Structure

(dict) --
Tags (list) --The list of tag keys and values associated with the resource you specified

(dict) --A key-value pair associated with an AWS resource. In EventBridge, rules and event buses support tagging.

Key (string) --A string you can use to assign a value. The combination of tag keys and values can help you organize and categorize your resources.

Value (string) --The value for the specified tag key.










Exceptions

EventBridge.Client.exceptions.ResourceNotFoundException
EventBridge.Client.exceptions.InternalException


    :return: {
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    """
    pass

def list_targets_by_rule(Rule=None, EventBusName=None, NextToken=None, Limit=None):
    """
    Lists the targets assigned to the specified rule.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_targets_by_rule(
        Rule='string',
        EventBusName='string',
        NextToken='string',
        Limit=123
    )
    
    
    :type Rule: string
    :param Rule: [REQUIRED]\nThe name of the rule.\n

    :type EventBusName: string
    :param EventBusName: The event bus associated with the rule. If you omit this, the default event bus is used.

    :type NextToken: string
    :param NextToken: The token returned by a previous call to retrieve the next set of results.

    :type Limit: integer
    :param Limit: The maximum number of results to return.

    :rtype: dict

ReturnsResponse Syntax
{
    'Targets': [
        {
            'Id': 'string',
            'Arn': 'string',
            'RoleArn': 'string',
            'Input': 'string',
            'InputPath': 'string',
            'InputTransformer': {
                'InputPathsMap': {
                    'string': 'string'
                },
                'InputTemplate': 'string'
            },
            'KinesisParameters': {
                'PartitionKeyPath': 'string'
            },
            'RunCommandParameters': {
                'RunCommandTargets': [
                    {
                        'Key': 'string',
                        'Values': [
                            'string',
                        ]
                    },
                ]
            },
            'EcsParameters': {
                'TaskDefinitionArn': 'string',
                'TaskCount': 123,
                'LaunchType': 'EC2'|'FARGATE',
                'NetworkConfiguration': {
                    'awsvpcConfiguration': {
                        'Subnets': [
                            'string',
                        ],
                        'SecurityGroups': [
                            'string',
                        ],
                        'AssignPublicIp': 'ENABLED'|'DISABLED'
                    }
                },
                'PlatformVersion': 'string',
                'Group': 'string'
            },
            'BatchParameters': {
                'JobDefinition': 'string',
                'JobName': 'string',
                'ArrayProperties': {
                    'Size': 123
                },
                'RetryStrategy': {
                    'Attempts': 123
                }
            },
            'SqsParameters': {
                'MessageGroupId': 'string'
            }
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Targets (list) --
The targets assigned to the rule.

(dict) --
Targets are the resources to be invoked when a rule is triggered. For a complete list of services and resources that can be set as a target, see  PutTargets .
If you are setting the event bus of another account as the target, and that account granted permission to your account through an organization instead of directly by the account ID, then you must specify a RoleArn with proper permissions in the Target structure. For more information, see Sending and Receiving Events Between AWS Accounts in the Amazon EventBridge User Guide .

Id (string) --
The ID of the target.

Arn (string) --
The Amazon Resource Name (ARN) of the target.

RoleArn (string) --
The Amazon Resource Name (ARN) of the IAM role to be used for this target when the rule is triggered. If one rule triggers multiple targets, you can use a different IAM role for each target.

Input (string) --
Valid JSON text passed to the target. In this case, nothing from the event itself is passed to the target. For more information, see The JavaScript Object Notation (JSON) Data Interchange Format .

InputPath (string) --
The value of the JSONPath that is used for extracting part of the matched event when passing it to the target. You must use JSON dot notation, not bracket notation. For more information about JSON paths, see JSONPath .

InputTransformer (dict) --
Settings to enable you to provide custom input to a target based on certain event data. You can extract one or more key-value pairs from the event and then use that data to send customized input to the target.

InputPathsMap (dict) --
Map of JSON paths to be extracted from the event. You can then insert these in the template in InputTemplate to produce the output you want to be sent to the target.

InputPathsMap is an array key-value pairs, where each value is a valid JSON path. You can have as many as 10 key-value pairs. You must use JSON dot notation, not bracket notation.

The keys cannot start with "AWS."

(string) --
(string) --




InputTemplate (string) --
Input template where you specify placeholders that will be filled with the values of the keys from InputPathsMap to customize the data sent to the target. Enclose each InputPathsMaps value in brackets: <value > The InputTemplate must be valid JSON.
If InputTemplate is a JSON object (surrounded by curly braces), the following restrictions apply:

The placeholder cannot be used as an object key.
Object values cannot include quote marks.

The following example shows the syntax for using InputPathsMap and InputTemplate .

"InputTransformer":
{
"InputPathsMap": {"instance": "$.detail.instance","status": "$.detail.status"},
"InputTemplate": "<instance> is in state <status>"
}

To have the InputTemplate include quote marks within a JSON string, escape each quote marks with a slash, as in the following example:

"InputTransformer":
{
"InputPathsMap": {"instance": "$.detail.instance","status": "$.detail.status"},
"InputTemplate": "<instance> is in state \\"<status>\\""
}




KinesisParameters (dict) --
The custom parameter you can use to control the shard assignment, when the target is a Kinesis data stream. If you do not include this parameter, the default is to use the eventId as the partition key.

PartitionKeyPath (string) --
The JSON path to be extracted from the event and used as the partition key. For more information, see Amazon Kinesis Streams Key Concepts in the Amazon Kinesis Streams Developer Guide .



RunCommandParameters (dict) --
Parameters used when you are using the rule to invoke Amazon EC2 Run Command.

RunCommandTargets (list) --
Currently, we support including only one RunCommandTarget block, which specifies either an array of InstanceIds or a tag.

(dict) --
Information about the EC2 instances that are to be sent the command, specified as key-value pairs. Each RunCommandTarget block can include only one key, but this key may specify multiple values.

Key (string) --
Can be either tag: tag-key or InstanceIds .

Values (list) --
If Key is tag: tag-key , Values is a list of tag values. If Key is InstanceIds , Values is a list of Amazon EC2 instance IDs.

(string) --








EcsParameters (dict) --
Contains the Amazon ECS task definition and task count to be used, if the event target is an Amazon ECS task. For more information about Amazon ECS tasks, see Task Definitions in the Amazon EC2 Container Service Developer Guide .

TaskDefinitionArn (string) --
The ARN of the task definition to use if the event target is an Amazon ECS task.

TaskCount (integer) --
The number of tasks to create based on TaskDefinition . The default is 1.

LaunchType (string) --
Specifies the launch type on which your task is running. The launch type that you specify here must match one of the launch type (compatibilities) of the target task. The FARGATE value is supported only in the Regions where AWS Fargate with Amazon ECS is supported. For more information, see AWS Fargate on Amazon ECS in the Amazon Elastic Container Service Developer Guide .

NetworkConfiguration (dict) --
Use this structure if the ECS task uses the awsvpc network mode. This structure specifies the VPC subnets and security groups associated with the task, and whether a public IP address is to be used. This structure is required if LaunchType is FARGATE because the awsvpc mode is required for Fargate tasks.
If you specify NetworkConfiguration when the target ECS task does not use the awsvpc network mode, the task fails.

awsvpcConfiguration (dict) --
Use this structure to specify the VPC subnets and security groups for the task, and whether a public IP address is to be used. This structure is relevant only for ECS tasks that use the awsvpc network mode.

Subnets (list) --
Specifies the subnets associated with the task. These subnets must all be in the same VPC. You can specify as many as 16 subnets.

(string) --


SecurityGroups (list) --
Specifies the security groups associated with the task. These security groups must all be in the same VPC. You can specify as many as five security groups. If you do not specify a security group, the default security group for the VPC is used.

(string) --


AssignPublicIp (string) --
Specifies whether the task\'s elastic network interface receives a public IP address. You can specify ENABLED only when LaunchType in EcsParameters is set to FARGATE .





PlatformVersion (string) --
Specifies the platform version for the task. Specify only the numeric portion of the platform version, such as 1.1.0 .
This structure is used only if LaunchType is FARGATE . For more information about valid platform versions, see AWS Fargate Platform Versions in the Amazon Elastic Container Service Developer Guide .

Group (string) --
Specifies an ECS task group for the task. The maximum length is 255 characters.



BatchParameters (dict) --
If the event target is an AWS Batch job, this contains the job definition, job name, and other parameters. For more information, see Jobs in the AWS Batch User Guide .

JobDefinition (string) --
The ARN or name of the job definition to use if the event target is an AWS Batch job. This job definition must already exist.

JobName (string) --
The name to use for this execution of the job, if the target is an AWS Batch job.

ArrayProperties (dict) --
The array properties for the submitted job, such as the size of the array. The array size can be between 2 and 10,000. If you specify array properties for a job, it becomes an array job. This parameter is used only if the target is an AWS Batch job.

Size (integer) --
The size of the array, if this is an array batch job. Valid values are integers between 2 and 10,000.



RetryStrategy (dict) --
The retry strategy to use for failed jobs, if the target is an AWS Batch job. The retry strategy is the number of times to retry the failed job execution. Valid values are 1\xe2\x80\x9310. When you specify a retry strategy here, it overrides the retry strategy defined in the job definition.

Attempts (integer) --
The number of times to attempt to retry, if the job fails. Valid values are 1\xe2\x80\x9310.





SqsParameters (dict) --
Contains the message group ID to use when the target is a FIFO queue.
If you specify an SQS FIFO queue as a target, the queue must have content-based deduplication enabled.

MessageGroupId (string) --
The FIFO message group ID to use as the target.







NextToken (string) --
Indicates whether there are additional results to retrieve. If there are no more results, the value is null.







Exceptions

EventBridge.Client.exceptions.ResourceNotFoundException
EventBridge.Client.exceptions.InternalException


    :return: {
        'Targets': [
            {
                'Id': 'string',
                'Arn': 'string',
                'RoleArn': 'string',
                'Input': 'string',
                'InputPath': 'string',
                'InputTransformer': {
                    'InputPathsMap': {
                        'string': 'string'
                    },
                    'InputTemplate': 'string'
                },
                'KinesisParameters': {
                    'PartitionKeyPath': 'string'
                },
                'RunCommandParameters': {
                    'RunCommandTargets': [
                        {
                            'Key': 'string',
                            'Values': [
                                'string',
                            ]
                        },
                    ]
                },
                'EcsParameters': {
                    'TaskDefinitionArn': 'string',
                    'TaskCount': 123,
                    'LaunchType': 'EC2'|'FARGATE',
                    'NetworkConfiguration': {
                        'awsvpcConfiguration': {
                            'Subnets': [
                                'string',
                            ],
                            'SecurityGroups': [
                                'string',
                            ],
                            'AssignPublicIp': 'ENABLED'|'DISABLED'
                        }
                    },
                    'PlatformVersion': 'string',
                    'Group': 'string'
                },
                'BatchParameters': {
                    'JobDefinition': 'string',
                    'JobName': 'string',
                    'ArrayProperties': {
                        'Size': 123
                    },
                    'RetryStrategy': {
                        'Attempts': 123
                    }
                },
                'SqsParameters': {
                    'MessageGroupId': 'string'
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def put_events(Entries=None):
    """
    Sends custom events to Amazon EventBridge so that they can be matched to rules.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_events(
        Entries=[
            {
                'Time': datetime(2015, 1, 1),
                'Source': 'string',
                'Resources': [
                    'string',
                ],
                'DetailType': 'string',
                'Detail': 'string',
                'EventBusName': 'string'
            },
        ]
    )
    
    
    :type Entries: list
    :param Entries: [REQUIRED]\nThe entry that defines an event in your system. You can specify several parameters for the entry such as the source and type of the event, resources associated with the event, and so on.\n\n(dict) --Represents an event to be submitted.\n\nTime (datetime) --The time stamp of the event, per RFC3339 . If no time stamp is provided, the time stamp of the PutEvents call is used.\n\nSource (string) --The source of the event.\n\nResources (list) --AWS resources, identified by Amazon Resource Name (ARN), which the event primarily concerns. Any number, including zero, may be present.\n\n(string) --\n\n\nDetailType (string) --Free-form string used to decide what fields to expect in the event detail.\n\nDetail (string) --A valid JSON string. There is no other schema imposed. The JSON string may contain fields and nested subobjects.\n\nEventBusName (string) --The event bus that will receive the event. Only the rules that are associated with this event bus will be able to match the event.\n\n\n\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'FailedEntryCount': 123,
    'Entries': [
        {
            'EventId': 'string',
            'ErrorCode': 'string',
            'ErrorMessage': 'string'
        },
    ]
}


Response Structure

(dict) --
FailedEntryCount (integer) --The number of failed entries.

Entries (list) --The successfully and unsuccessfully ingested events results. If the ingestion was successful, the entry has the event ID in it. Otherwise, you can use the error code and error message to identify the problem with the entry.

(dict) --Represents an event that failed to be submitted.

EventId (string) --The ID of the event.

ErrorCode (string) --The error code that indicates why the event submission failed.

ErrorMessage (string) --The error message that explains why the event submission failed.










Exceptions

EventBridge.Client.exceptions.InternalException


    :return: {
        'FailedEntryCount': 123,
        'Entries': [
            {
                'EventId': 'string',
                'ErrorCode': 'string',
                'ErrorMessage': 'string'
            },
        ]
    }
    
    
    :returns: 
    EventBridge.Client.exceptions.InternalException
    
    """
    pass

def put_partner_events(Entries=None):
    """
    This is used by SaaS partners to write events to a customer\'s partner event bus. AWS customers do not use this operation.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_partner_events(
        Entries=[
            {
                'Time': datetime(2015, 1, 1),
                'Source': 'string',
                'Resources': [
                    'string',
                ],
                'DetailType': 'string',
                'Detail': 'string'
            },
        ]
    )
    
    
    :type Entries: list
    :param Entries: [REQUIRED]\nThe list of events to write to the event bus.\n\n(dict) --The details about an event generated by an SaaS partner.\n\nTime (datetime) --The date and time of the event.\n\nSource (string) --The event source that is generating the evntry.\n\nResources (list) --AWS resources, identified by Amazon Resource Name (ARN), which the event primarily concerns. Any number, including zero, may be present.\n\n(string) --\n\n\nDetailType (string) --A free-form string used to decide what fields to expect in the event detail.\n\nDetail (string) --A valid JSON string. There is no other schema imposed. The JSON string may contain fields and nested subobjects.\n\n\n\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'FailedEntryCount': 123,
    'Entries': [
        {
            'EventId': 'string',
            'ErrorCode': 'string',
            'ErrorMessage': 'string'
        },
    ]
}


Response Structure

(dict) --
FailedEntryCount (integer) --The number of events from this operation that could not be written to the partner event bus.

Entries (list) --The list of events from this operation that were successfully written to the partner event bus.

(dict) --Represents an event that a partner tried to generate, but failed.

EventId (string) --The ID of the event.

ErrorCode (string) --The error code that indicates why the event submission failed.

ErrorMessage (string) --The error message that explains why the event submission failed.










Exceptions

EventBridge.Client.exceptions.InternalException


    :return: {
        'FailedEntryCount': 123,
        'Entries': [
            {
                'EventId': 'string',
                'ErrorCode': 'string',
                'ErrorMessage': 'string'
            },
        ]
    }
    
    
    :returns: 
    EventBridge.Client.exceptions.InternalException
    
    """
    pass

def put_permission(EventBusName=None, Action=None, Principal=None, StatementId=None, Condition=None):
    """
    Running PutPermission permits the specified AWS account or AWS organization to put events to the specified event bus . CloudWatch Events rules in your account are triggered by these events arriving to an event bus in your account.
    For another account to send events to your account, that external account must have an EventBridge rule with your account\'s event bus as a target.
    To enable multiple AWS accounts to put events to your event bus, run PutPermission once for each of these accounts. Or, if all the accounts are members of the same AWS organization, you can run PutPermission once specifying Principal as "*" and specifying the AWS organization ID in Condition , to grant permissions to all accounts in that organization.
    If you grant permissions using an organization, then accounts in that organization must specify a RoleArn with proper permissions when they use PutTarget to add your account\'s event bus as a target. For more information, see Sending and Receiving Events Between AWS Accounts in the Amazon EventBridge User Guide .
    The permission policy on the default event bus cannot exceed 10 KB in size.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_permission(
        EventBusName='string',
        Action='string',
        Principal='string',
        StatementId='string',
        Condition={
            'Type': 'string',
            'Key': 'string',
            'Value': 'string'
        }
    )
    
    
    :type EventBusName: string
    :param EventBusName: The event bus associated with the rule. If you omit this, the default event bus is used.

    :type Action: string
    :param Action: [REQUIRED]\nThe action that you are enabling the other account to perform. Currently, this must be events:PutEvents .\n

    :type Principal: string
    :param Principal: [REQUIRED]\nThe 12-digit AWS account ID that you are permitting to put events to your default event bus. Specify '*' to permit any account to put events to your default event bus.\nIf you specify '*' without specifying Condition , avoid creating rules that may match undesirable events. To create more secure rules, make sure that the event pattern for each rule contains an account field with a specific account ID from which to receive events. Rules with an account field do not match any events sent from other accounts.\n

    :type StatementId: string
    :param StatementId: [REQUIRED]\nAn identifier string for the external account that you are granting permissions to. If you later want to revoke the permission for this external account, specify this StatementId when you run RemovePermission .\n

    :type Condition: dict
    :param Condition: This parameter enables you to limit the permission to accounts that fulfill a certain condition, such as being a member of a certain AWS organization. For more information about AWS Organizations, see What Is AWS Organizations in the AWS Organizations User Guide .\nIf you specify Condition with an AWS organization ID, and specify '*' as the value for Principal , you grant permission to all the accounts in the named organization.\nThe Condition is a JSON string which must contain Type , Key , and Value fields.\n\nType (string) -- [REQUIRED]Specifies the type of condition. Currently the only supported value is StringEquals .\n\nKey (string) -- [REQUIRED]Specifies the key for the condition. Currently the only supported key is aws:PrincipalOrgID .\n\nValue (string) -- [REQUIRED]Specifies the value for the key. Currently, this must be the ID of the organization.\n\n\n

    :returns: 
    EventBridge.Client.exceptions.ResourceNotFoundException
    EventBridge.Client.exceptions.PolicyLengthExceededException
    EventBridge.Client.exceptions.InternalException
    EventBridge.Client.exceptions.ConcurrentModificationException
    
    """
    pass

def put_rule(Name=None, ScheduleExpression=None, EventPattern=None, State=None, Description=None, RoleArn=None, Tags=None, EventBusName=None):
    """
    Creates or updates the specified rule. Rules are enabled by default, or based on value of the state. You can disable a rule using  DisableRule .
    A single rule watches for events from a single event bus. Events generated by AWS services go to your account\'s default event bus. Events generated by SaaS partner services or applications go to the matching partner event bus. If you have custom applications or services, you can specify whether their events go to your default event bus or a custom event bus that you have created. For more information, see  CreateEventBus .
    If you are updating an existing rule, the rule is replaced with what you specify in this PutRule command. If you omit arguments in PutRule , the old values for those arguments are not kept. Instead, they are replaced with null values.
    When you create or update a rule, incoming events might not immediately start matching to new or updated rules. Allow a short period of time for changes to take effect.
    A rule must contain at least an EventPattern or ScheduleExpression. Rules with EventPatterns are triggered when a matching event is observed. Rules with ScheduleExpressions self-trigger based on the given schedule. A rule can have both an EventPattern and a ScheduleExpression, in which case the rule triggers on matching events as well as on a schedule.
    When you initially create a rule, you can optionally assign one or more tags to the rule. Tags can help you organize and categorize your resources. You can also use them to scope user permissions, by granting a user permission to access or change only rules with certain tag values. To use the PutRule operation and assign tags, you must have both the events:PutRule and events:TagResource permissions.
    If you are updating an existing rule, any tags you specify in the PutRule operation are ignored. To update the tags of an existing rule, use  TagResource and  UntagResource .
    Most services in AWS treat : or / as the same character in Amazon Resource Names (ARNs). However, EventBridge uses an exact match in event patterns and rules. Be sure to use the correct ARN characters when creating event patterns so that they match the ARN syntax in the event you want to match.
    In EventBridge, it is possible to create rules that lead to infinite loops, where a rule is fired repeatedly. For example, a rule might detect that ACLs have changed on an S3 bucket, and trigger software to change them to the desired state. If the rule is not written carefully, the subsequent change to the ACLs fires the rule again, creating an infinite loop.
    To prevent this, write the rules so that the triggered actions do not re-fire the same rule. For example, your rule could fire only if ACLs are found to be in a bad state, instead of after any change.
    An infinite loop can quickly cause higher than expected charges. We recommend that you use budgeting, which alerts you when charges exceed your specified limit. For more information, see Managing Your Costs with Budgets .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_rule(
        Name='string',
        ScheduleExpression='string',
        EventPattern='string',
        State='ENABLED'|'DISABLED',
        Description='string',
        RoleArn='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        EventBusName='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the rule that you are creating or updating.\n

    :type ScheduleExpression: string
    :param ScheduleExpression: The scheduling expression. For example, 'cron(0 20 * * ? *)' or 'rate(5 minutes)'.

    :type EventPattern: string
    :param EventPattern: The event pattern. For more information, see Events and Event Patterns in the Amazon EventBridge User Guide .

    :type State: string
    :param State: Indicates whether the rule is enabled or disabled.

    :type Description: string
    :param Description: A description of the rule.

    :type RoleArn: string
    :param RoleArn: The Amazon Resource Name (ARN) of the IAM role associated with the rule.

    :type Tags: list
    :param Tags: The list of key-value pairs to associate with the rule.\n\n(dict) --A key-value pair associated with an AWS resource. In EventBridge, rules and event buses support tagging.\n\nKey (string) -- [REQUIRED]A string you can use to assign a value. The combination of tag keys and values can help you organize and categorize your resources.\n\nValue (string) -- [REQUIRED]The value for the specified tag key.\n\n\n\n\n

    :type EventBusName: string
    :param EventBusName: The event bus to associate with this rule. If you omit this, the default event bus is used.

    :rtype: dict

ReturnsResponse Syntax
{
    'RuleArn': 'string'
}


Response Structure

(dict) --

RuleArn (string) --
The Amazon Resource Name (ARN) of the rule.







Exceptions

EventBridge.Client.exceptions.InvalidEventPatternException
EventBridge.Client.exceptions.LimitExceededException
EventBridge.Client.exceptions.ConcurrentModificationException
EventBridge.Client.exceptions.ManagedRuleException
EventBridge.Client.exceptions.InternalException
EventBridge.Client.exceptions.ResourceNotFoundException


    :return: {
        'RuleArn': 'string'
    }
    
    
    :returns: 
    EventBridge.Client.exceptions.InvalidEventPatternException
    EventBridge.Client.exceptions.LimitExceededException
    EventBridge.Client.exceptions.ConcurrentModificationException
    EventBridge.Client.exceptions.ManagedRuleException
    EventBridge.Client.exceptions.InternalException
    EventBridge.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def put_targets(Rule=None, EventBusName=None, Targets=None):
    """
    Adds the specified targets to the specified rule, or updates the targets if they are already associated with the rule.
    Targets are the resources that are invoked when a rule is triggered.
    You can configure the following as targets for Events:
    Creating rules with built-in targets is supported only in the AWS Management Console. The built-in targets are EC2 CreateSnapshot API call , EC2 RebootInstances API call , EC2 StopInstances API call , and EC2 TerminateInstances API call .
    For some target types, PutTargets provides target-specific parameters. If the target is a Kinesis data stream, you can optionally specify which shard the event goes to by using the KinesisParameters argument. To invoke a command on multiple EC2 instances with one rule, you can use the RunCommandParameters field.
    To be able to make API calls against the resources that you own, Amazon CloudWatch Events needs the appropriate permissions. For AWS Lambda and Amazon SNS resources, EventBridge relies on resource-based policies. For EC2 instances, Kinesis data streams, and AWS Step Functions state machines, EventBridge relies on IAM roles that you specify in the RoleARN argument in PutTargets . For more information, see Authentication and Access Control in the Amazon EventBridge User Guide .
    If another AWS account is in the same region and has granted you permission (using PutPermission ), you can send events to that account. Set that account\'s event bus as a target of the rules in your account. To send the matched events to the other account, specify that account\'s event bus as the Arn value when you run PutTargets . If your account sends events to another account, your account is charged for each sent event. Each event sent to another account is charged as a custom event. The account receiving the event is not charged. For more information, see Amazon CloudWatch Pricing .
    If you are setting the event bus of another account as the target, and that account granted permission to your account through an organization instead of directly by the account ID, then you must specify a RoleArn with proper permissions in the Target structure. For more information, see Sending and Receiving Events Between AWS Accounts in the Amazon EventBridge User Guide .
    For more information about enabling cross-account events, see  PutPermission .
    When you specify InputPath or InputTransformer , you must use JSON dot notation, not bracket notation.
    When you add targets to a rule and the associated rule triggers soon after, new or updated targets might not be immediately invoked. Allow a short period of time for changes to take effect.
    This action can partially fail if too many requests are made at the same time. If that happens, FailedEntryCount is non-zero in the response and each entry in FailedEntries provides the ID of the failed target and the error code.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_targets(
        Rule='string',
        EventBusName='string',
        Targets=[
            {
                'Id': 'string',
                'Arn': 'string',
                'RoleArn': 'string',
                'Input': 'string',
                'InputPath': 'string',
                'InputTransformer': {
                    'InputPathsMap': {
                        'string': 'string'
                    },
                    'InputTemplate': 'string'
                },
                'KinesisParameters': {
                    'PartitionKeyPath': 'string'
                },
                'RunCommandParameters': {
                    'RunCommandTargets': [
                        {
                            'Key': 'string',
                            'Values': [
                                'string',
                            ]
                        },
                    ]
                },
                'EcsParameters': {
                    'TaskDefinitionArn': 'string',
                    'TaskCount': 123,
                    'LaunchType': 'EC2'|'FARGATE',
                    'NetworkConfiguration': {
                        'awsvpcConfiguration': {
                            'Subnets': [
                                'string',
                            ],
                            'SecurityGroups': [
                                'string',
                            ],
                            'AssignPublicIp': 'ENABLED'|'DISABLED'
                        }
                    },
                    'PlatformVersion': 'string',
                    'Group': 'string'
                },
                'BatchParameters': {
                    'JobDefinition': 'string',
                    'JobName': 'string',
                    'ArrayProperties': {
                        'Size': 123
                    },
                    'RetryStrategy': {
                        'Attempts': 123
                    }
                },
                'SqsParameters': {
                    'MessageGroupId': 'string'
                }
            },
        ]
    )
    
    
    :type Rule: string
    :param Rule: [REQUIRED]\nThe name of the rule.\n

    :type EventBusName: string
    :param EventBusName: The name of the event bus associated with the rule. If you omit this, the default event bus is used.

    :type Targets: list
    :param Targets: [REQUIRED]\nThe targets to update or add to the rule.\n\n(dict) --Targets are the resources to be invoked when a rule is triggered. For a complete list of services and resources that can be set as a target, see PutTargets .\nIf you are setting the event bus of another account as the target, and that account granted permission to your account through an organization instead of directly by the account ID, then you must specify a RoleArn with proper permissions in the Target structure. For more information, see Sending and Receiving Events Between AWS Accounts in the Amazon EventBridge User Guide .\n\nId (string) -- [REQUIRED]The ID of the target.\n\nArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the target.\n\nRoleArn (string) --The Amazon Resource Name (ARN) of the IAM role to be used for this target when the rule is triggered. If one rule triggers multiple targets, you can use a different IAM role for each target.\n\nInput (string) --Valid JSON text passed to the target. In this case, nothing from the event itself is passed to the target. For more information, see The JavaScript Object Notation (JSON) Data Interchange Format .\n\nInputPath (string) --The value of the JSONPath that is used for extracting part of the matched event when passing it to the target. You must use JSON dot notation, not bracket notation. For more information about JSON paths, see JSONPath .\n\nInputTransformer (dict) --Settings to enable you to provide custom input to a target based on certain event data. You can extract one or more key-value pairs from the event and then use that data to send customized input to the target.\n\nInputPathsMap (dict) --Map of JSON paths to be extracted from the event. You can then insert these in the template in InputTemplate to produce the output you want to be sent to the target.\n\nInputPathsMap is an array key-value pairs, where each value is a valid JSON path. You can have as many as 10 key-value pairs. You must use JSON dot notation, not bracket notation.\nThe keys cannot start with 'AWS.'\n\n(string) --\n(string) --\n\n\n\n\nInputTemplate (string) -- [REQUIRED]Input template where you specify placeholders that will be filled with the values of the keys from InputPathsMap to customize the data sent to the target. Enclose each InputPathsMaps value in brackets: <value > The InputTemplate must be valid JSON.\nIf InputTemplate is a JSON object (surrounded by curly braces), the following restrictions apply:\n\nThe placeholder cannot be used as an object key.\nObject values cannot include quote marks.\n\nThe following example shows the syntax for using InputPathsMap and InputTemplate .\n\n'InputTransformer':{\n'InputPathsMap': {'instance': '$.detail.instance','status': '$.detail.status'},\n'InputTemplate': '<instance> is in state <status>'\n}\n\nTo have the InputTemplate include quote marks within a JSON string, escape each quote marks with a slash, as in the following example:\n\n'InputTransformer':{\n'InputPathsMap': {'instance': '$.detail.instance','status': '$.detail.status'},\n'InputTemplate': '<instance> is in state \\'<status>\\''\n}\n\n\n\n\nKinesisParameters (dict) --The custom parameter you can use to control the shard assignment, when the target is a Kinesis data stream. If you do not include this parameter, the default is to use the eventId as the partition key.\n\nPartitionKeyPath (string) -- [REQUIRED]The JSON path to be extracted from the event and used as the partition key. For more information, see Amazon Kinesis Streams Key Concepts in the Amazon Kinesis Streams Developer Guide .\n\n\n\nRunCommandParameters (dict) --Parameters used when you are using the rule to invoke Amazon EC2 Run Command.\n\nRunCommandTargets (list) -- [REQUIRED]Currently, we support including only one RunCommandTarget block, which specifies either an array of InstanceIds or a tag.\n\n(dict) --Information about the EC2 instances that are to be sent the command, specified as key-value pairs. Each RunCommandTarget block can include only one key, but this key may specify multiple values.\n\nKey (string) -- [REQUIRED]Can be either tag: tag-key or InstanceIds .\n\nValues (list) -- [REQUIRED]If Key is tag: tag-key , Values is a list of tag values. If Key is InstanceIds , Values is a list of Amazon EC2 instance IDs.\n\n(string) --\n\n\n\n\n\n\n\n\nEcsParameters (dict) --Contains the Amazon ECS task definition and task count to be used, if the event target is an Amazon ECS task. For more information about Amazon ECS tasks, see Task Definitions in the Amazon EC2 Container Service Developer Guide .\n\nTaskDefinitionArn (string) -- [REQUIRED]The ARN of the task definition to use if the event target is an Amazon ECS task.\n\nTaskCount (integer) --The number of tasks to create based on TaskDefinition . The default is 1.\n\nLaunchType (string) --Specifies the launch type on which your task is running. The launch type that you specify here must match one of the launch type (compatibilities) of the target task. The FARGATE value is supported only in the Regions where AWS Fargate with Amazon ECS is supported. For more information, see AWS Fargate on Amazon ECS in the Amazon Elastic Container Service Developer Guide .\n\nNetworkConfiguration (dict) --Use this structure if the ECS task uses the awsvpc network mode. This structure specifies the VPC subnets and security groups associated with the task, and whether a public IP address is to be used. This structure is required if LaunchType is FARGATE because the awsvpc mode is required for Fargate tasks.\nIf you specify NetworkConfiguration when the target ECS task does not use the awsvpc network mode, the task fails.\n\nawsvpcConfiguration (dict) --Use this structure to specify the VPC subnets and security groups for the task, and whether a public IP address is to be used. This structure is relevant only for ECS tasks that use the awsvpc network mode.\n\nSubnets (list) -- [REQUIRED]Specifies the subnets associated with the task. These subnets must all be in the same VPC. You can specify as many as 16 subnets.\n\n(string) --\n\n\nSecurityGroups (list) --Specifies the security groups associated with the task. These security groups must all be in the same VPC. You can specify as many as five security groups. If you do not specify a security group, the default security group for the VPC is used.\n\n(string) --\n\n\nAssignPublicIp (string) --Specifies whether the task\'s elastic network interface receives a public IP address. You can specify ENABLED only when LaunchType in EcsParameters is set to FARGATE .\n\n\n\n\n\nPlatformVersion (string) --Specifies the platform version for the task. Specify only the numeric portion of the platform version, such as 1.1.0 .\nThis structure is used only if LaunchType is FARGATE . For more information about valid platform versions, see AWS Fargate Platform Versions in the Amazon Elastic Container Service Developer Guide .\n\nGroup (string) --Specifies an ECS task group for the task. The maximum length is 255 characters.\n\n\n\nBatchParameters (dict) --If the event target is an AWS Batch job, this contains the job definition, job name, and other parameters. For more information, see Jobs in the AWS Batch User Guide .\n\nJobDefinition (string) -- [REQUIRED]The ARN or name of the job definition to use if the event target is an AWS Batch job. This job definition must already exist.\n\nJobName (string) -- [REQUIRED]The name to use for this execution of the job, if the target is an AWS Batch job.\n\nArrayProperties (dict) --The array properties for the submitted job, such as the size of the array. The array size can be between 2 and 10,000. If you specify array properties for a job, it becomes an array job. This parameter is used only if the target is an AWS Batch job.\n\nSize (integer) --The size of the array, if this is an array batch job. Valid values are integers between 2 and 10,000.\n\n\n\nRetryStrategy (dict) --The retry strategy to use for failed jobs, if the target is an AWS Batch job. The retry strategy is the number of times to retry the failed job execution. Valid values are 1\xe2\x80\x9310. When you specify a retry strategy here, it overrides the retry strategy defined in the job definition.\n\nAttempts (integer) --The number of times to attempt to retry, if the job fails. Valid values are 1\xe2\x80\x9310.\n\n\n\n\n\nSqsParameters (dict) --Contains the message group ID to use when the target is a FIFO queue.\nIf you specify an SQS FIFO queue as a target, the queue must have content-based deduplication enabled.\n\nMessageGroupId (string) --The FIFO message group ID to use as the target.\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'FailedEntryCount': 123,
    'FailedEntries': [
        {
            'TargetId': 'string',
            'ErrorCode': 'string',
            'ErrorMessage': 'string'
        },
    ]
}


Response Structure

(dict) --

FailedEntryCount (integer) --
The number of failed entries.

FailedEntries (list) --
The failed target entries.

(dict) --
Represents a target that failed to be added to a rule.

TargetId (string) --
The ID of the target.

ErrorCode (string) --
The error code that indicates why the target addition failed. If the value is ConcurrentModificationException , too many requests were made at the same time.

ErrorMessage (string) --
The error message that explains why the target addition failed.











Exceptions

EventBridge.Client.exceptions.ResourceNotFoundException
EventBridge.Client.exceptions.ConcurrentModificationException
EventBridge.Client.exceptions.LimitExceededException
EventBridge.Client.exceptions.ManagedRuleException
EventBridge.Client.exceptions.InternalException


    :return: {
        'FailedEntryCount': 123,
        'FailedEntries': [
            {
                'TargetId': 'string',
                'ErrorCode': 'string',
                'ErrorMessage': 'string'
            },
        ]
    }
    
    
    :returns: 
    If none of the following arguments are specified for a target, then the entire event is passed to the target in JSON format (unless the target is Amazon EC2 Run Command or Amazon ECS task, in which case nothing from the event is passed to the target).
    If Input is specified in the form of valid JSON, then the matched event is overridden with this constant.
    If InputPath is specified in the form of JSONPath (for example, $.detail ), then only the part of the event specified in the path is passed to the target (for example, only the detail part of the event is passed).
    If InputTransformer is specified, then one or more specified JSONPaths are extracted from the event and used as values in a template that you specify as the input to the target.
    
    """
    pass

def remove_permission(StatementId=None, EventBusName=None):
    """
    Revokes the permission of another AWS account to be able to put events to the specified event bus. Specify the account to revoke by the StatementId value that you associated with the account when you granted it permission with PutPermission . You can find the StatementId by using  DescribeEventBus .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.remove_permission(
        StatementId='string',
        EventBusName='string'
    )
    
    
    :type StatementId: string
    :param StatementId: [REQUIRED]\nThe statement ID corresponding to the account that is no longer allowed to put events to the default event bus.\n

    :type EventBusName: string
    :param EventBusName: The name of the event bus to revoke permissions for. If you omit this, the default event bus is used.

    :returns: 
    EventBridge.Client.exceptions.ResourceNotFoundException
    EventBridge.Client.exceptions.InternalException
    EventBridge.Client.exceptions.ConcurrentModificationException
    
    """
    pass

def remove_targets(Rule=None, EventBusName=None, Ids=None, Force=None):
    """
    Removes the specified targets from the specified rule. When the rule is triggered, those targets are no longer be invoked.
    When you remove a target, when the associated rule triggers, removed targets might continue to be invoked. Allow a short period of time for changes to take effect.
    This action can partially fail if too many requests are made at the same time. If that happens, FailedEntryCount is non-zero in the response and each entry in FailedEntries provides the ID of the failed target and the error code.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.remove_targets(
        Rule='string',
        EventBusName='string',
        Ids=[
            'string',
        ],
        Force=True|False
    )
    
    
    :type Rule: string
    :param Rule: [REQUIRED]\nThe name of the rule.\n

    :type EventBusName: string
    :param EventBusName: The name of the event bus associated with the rule.

    :type Ids: list
    :param Ids: [REQUIRED]\nThe IDs of the targets to remove from the rule.\n\n(string) --\n\n

    :type Force: boolean
    :param Force: If this is a managed rule, created by an AWS service on your behalf, you must specify Force as True to remove targets. This parameter is ignored for rules that are not managed rules. You can check whether a rule is a managed rule by using DescribeRule or ListRules and checking the ManagedBy field of the response.

    :rtype: dict

ReturnsResponse Syntax
{
    'FailedEntryCount': 123,
    'FailedEntries': [
        {
            'TargetId': 'string',
            'ErrorCode': 'string',
            'ErrorMessage': 'string'
        },
    ]
}


Response Structure

(dict) --

FailedEntryCount (integer) --
The number of failed entries.

FailedEntries (list) --
The failed target entries.

(dict) --
Represents a target that failed to be removed from a rule.

TargetId (string) --
The ID of the target.

ErrorCode (string) --
The error code that indicates why the target removal failed. If the value is ConcurrentModificationException , too many requests were made at the same time.

ErrorMessage (string) --
The error message that explains why the target removal failed.











Exceptions

EventBridge.Client.exceptions.ResourceNotFoundException
EventBridge.Client.exceptions.ConcurrentModificationException
EventBridge.Client.exceptions.ManagedRuleException
EventBridge.Client.exceptions.InternalException


    :return: {
        'FailedEntryCount': 123,
        'FailedEntries': [
            {
                'TargetId': 'string',
                'ErrorCode': 'string',
                'ErrorMessage': 'string'
            },
        ]
    }
    
    
    :returns: 
    EventBridge.Client.exceptions.ResourceNotFoundException
    EventBridge.Client.exceptions.ConcurrentModificationException
    EventBridge.Client.exceptions.ManagedRuleException
    EventBridge.Client.exceptions.InternalException
    
    """
    pass

def tag_resource(ResourceARN=None, Tags=None):
    """
    Assigns one or more tags (key-value pairs) to the specified EventBridge resource. Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values. In EventBridge, rules and event buses can be tagged.
    Tags don\'t have any semantic meaning to AWS and are interpreted strictly as strings of characters.
    You can use the TagResource action with a resource that already has tags. If you specify a new tag key, this tag is appended to the list of tags associated with the resource. If you specify a tag key that is already associated with the resource, the new tag value that you specify replaces the previous value for that tag.
    You can associate as many as 50 tags with a resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        ResourceARN='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ResourceARN: string
    :param ResourceARN: [REQUIRED]\nThe ARN of the EventBridge resource that you\'re adding tags to.\n

    :type Tags: list
    :param Tags: [REQUIRED]\nThe list of key-value pairs to associate with the resource.\n\n(dict) --A key-value pair associated with an AWS resource. In EventBridge, rules and event buses support tagging.\n\nKey (string) -- [REQUIRED]A string you can use to assign a value. The combination of tag keys and values can help you organize and categorize your resources.\n\nValue (string) -- [REQUIRED]The value for the specified tag key.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

EventBridge.Client.exceptions.ResourceNotFoundException
EventBridge.Client.exceptions.ConcurrentModificationException
EventBridge.Client.exceptions.InternalException
EventBridge.Client.exceptions.ManagedRuleException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def test_event_pattern(EventPattern=None, Event=None):
    """
    Tests whether the specified event pattern matches the provided event.
    Most services in AWS treat : or / as the same character in Amazon Resource Names (ARNs). However, EventBridge uses an exact match in event patterns and rules. Be sure to use the correct ARN characters when creating event patterns so that they match the ARN syntax in the event you want to match.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.test_event_pattern(
        EventPattern='string',
        Event='string'
    )
    
    
    :type EventPattern: string
    :param EventPattern: [REQUIRED]\nThe event pattern. For more information, see Events and Event Patterns in the Amazon EventBridge User Guide .\n

    :type Event: string
    :param Event: [REQUIRED]\nThe event, in JSON format, to test against the event pattern.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Result': True|False
}


Response Structure

(dict) --

Result (boolean) --
Indicates whether the event matches the event pattern.







Exceptions

EventBridge.Client.exceptions.InvalidEventPatternException
EventBridge.Client.exceptions.InternalException


    :return: {
        'Result': True|False
    }
    
    
    :returns: 
    EventBridge.Client.exceptions.InvalidEventPatternException
    EventBridge.Client.exceptions.InternalException
    
    """
    pass

def untag_resource(ResourceARN=None, TagKeys=None):
    """
    Removes one or more tags from the specified EventBridge resource. In CloudWatch Events, rules and event buses can be tagged.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        ResourceARN='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceARN: string
    :param ResourceARN: [REQUIRED]\nThe ARN of the EventBridge resource from which you are removing tags.\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nThe list of tag keys to remove from the resource.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

EventBridge.Client.exceptions.ResourceNotFoundException
EventBridge.Client.exceptions.InternalException
EventBridge.Client.exceptions.ConcurrentModificationException
EventBridge.Client.exceptions.ManagedRuleException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

