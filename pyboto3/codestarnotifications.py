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

def create_notification_rule(Name=None, EventTypeIds=None, Resource=None, Targets=None, DetailType=None, ClientRequestToken=None, Tags=None, Status=None):
    """
    Creates a notification rule for a resource. The rule specifies the events you want notifications about and the targets (such as SNS topics) where you want to receive them.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_notification_rule(
        Name='string',
        EventTypeIds=[
            'string',
        ],
        Resource='string',
        Targets=[
            {
                'TargetType': 'string',
                'TargetAddress': 'string'
            },
        ],
        DetailType='BASIC'|'FULL',
        ClientRequestToken='string',
        Tags={
            'string': 'string'
        },
        Status='ENABLED'|'DISABLED'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name for the notification rule. Notifictaion rule names must be unique in your AWS account.\n

    :type EventTypeIds: list
    :param EventTypeIds: [REQUIRED]\nA list of event types associated with this notification rule. For a list of allowed events, see EventTypeSummary .\n\n(string) --\n\n

    :type Resource: string
    :param Resource: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource to associate with the notification rule. Supported resources include pipelines in AWS CodePipeline, repositories in AWS CodeCommit, and build projects in AWS CodeBuild.\n

    :type Targets: list
    :param Targets: [REQUIRED]\nA list of Amazon Resource Names (ARNs) of SNS topics to associate with the notification rule.\n\n(dict) --Information about the SNS topics associated with a notification rule.\n\nTargetType (string) --The target type. Can be an Amazon SNS topic.\n\nTargetAddress (string) --The Amazon Resource Name (ARN) of the SNS topic.\n\n\n\n\n

    :type DetailType: string
    :param DetailType: [REQUIRED]\nThe level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in AWS CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created.\n

    :type ClientRequestToken: string
    :param ClientRequestToken: A unique, client-generated idempotency token that, when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request with the same parameters is received and a token is included, the request returns information about the initial request that used that token.\n\nNote\nThe AWS SDKs prepopulate client request tokens. If you are using an AWS SDK, an idempotency token is created for you.\n\nThis field is autopopulated if not provided.\n

    :type Tags: dict
    :param Tags: A list of tags to apply to this notification rule. Key names cannot start with 'aws'.\n\n(string) --\n(string) --\n\n\n\n

    :type Status: string
    :param Status: The status of the notification rule. The default value is ENABLED. If the status is set to DISABLED, notifications aren\'t sent for the notification rule.

    :rtype: dict

ReturnsResponse Syntax
{
    'Arn': 'string'
}


Response Structure

(dict) --

Arn (string) --
The Amazon Resource Name (ARN) of the notification rule.







Exceptions

CodeStarNotifications.Client.exceptions.ResourceAlreadyExistsException
CodeStarNotifications.Client.exceptions.ValidationException
CodeStarNotifications.Client.exceptions.LimitExceededException
CodeStarNotifications.Client.exceptions.ConfigurationException
CodeStarNotifications.Client.exceptions.ConcurrentModificationException
CodeStarNotifications.Client.exceptions.AccessDeniedException


    :return: {
        'Arn': 'string'
    }
    
    
    :returns: 
    CodeStarNotifications.Client.exceptions.ResourceAlreadyExistsException
    CodeStarNotifications.Client.exceptions.ValidationException
    CodeStarNotifications.Client.exceptions.LimitExceededException
    CodeStarNotifications.Client.exceptions.ConfigurationException
    CodeStarNotifications.Client.exceptions.ConcurrentModificationException
    CodeStarNotifications.Client.exceptions.AccessDeniedException
    
    """
    pass

def delete_notification_rule(Arn=None):
    """
    Deletes a notification rule for a resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_notification_rule(
        Arn='string'
    )
    
    
    :type Arn: string
    :param Arn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the notification rule you want to delete.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Arn': 'string'
}


Response Structure

(dict) --
Arn (string) --The Amazon Resource Name (ARN) of the deleted notification rule.






Exceptions

CodeStarNotifications.Client.exceptions.ValidationException
CodeStarNotifications.Client.exceptions.LimitExceededException
CodeStarNotifications.Client.exceptions.ConcurrentModificationException


    :return: {
        'Arn': 'string'
    }
    
    
    """
    pass

def delete_target(TargetAddress=None, ForceUnsubscribeAll=None):
    """
    Deletes a specified target for notifications.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_target(
        TargetAddress='string',
        ForceUnsubscribeAll=True|False
    )
    
    
    :type TargetAddress: string
    :param TargetAddress: [REQUIRED]\nThe Amazon Resource Name (ARN) of the SNS topic to delete.\n

    :type ForceUnsubscribeAll: boolean
    :param ForceUnsubscribeAll: A Boolean value that can be used to delete all associations with this SNS topic. The default value is FALSE. If set to TRUE, all associations between that target and every notification rule in your AWS account are deleted.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

CodeStarNotifications.Client.exceptions.ValidationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def describe_notification_rule(Arn=None):
    """
    Returns information about a specified notification rule.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_notification_rule(
        Arn='string'
    )
    
    
    :type Arn: string
    :param Arn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the notification rule.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Arn': 'string',
    'Name': 'string',
    'EventTypes': [
        {
            'EventTypeId': 'string',
            'ServiceName': 'string',
            'EventTypeName': 'string',
            'ResourceType': 'string'
        },
    ],
    'Resource': 'string',
    'Targets': [
        {
            'TargetAddress': 'string',
            'TargetType': 'string',
            'TargetStatus': 'PENDING'|'ACTIVE'|'UNREACHABLE'|'INACTIVE'|'DEACTIVATED'
        },
    ],
    'DetailType': 'BASIC'|'FULL',
    'CreatedBy': 'string',
    'Status': 'ENABLED'|'DISABLED',
    'CreatedTimestamp': datetime(2015, 1, 1),
    'LastModifiedTimestamp': datetime(2015, 1, 1),
    'Tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --
Arn (string) --The Amazon Resource Name (ARN) of the notification rule.

Name (string) --The name of the notification rule.

EventTypes (list) --A list of the event types associated with the notification rule.

(dict) --Returns information about an event that has triggered a notification rule.

EventTypeId (string) --The system-generated ID of the event.

ServiceName (string) --The name of the service for which the event applies.

EventTypeName (string) --The name of the event.

ResourceType (string) --The resource type of the event.





Resource (string) --The Amazon Resource Name (ARN) of the resource associated with the notification rule.

Targets (list) --A list of the SNS topics associated with the notification rule.

(dict) --Information about the targets specified for a notification rule.

TargetAddress (string) --The Amazon Resource Name (ARN) of the SNS topic.

TargetType (string) --The type of the target (for example, SNS).

TargetStatus (string) --The status of the target.





DetailType (string) --The level of detail included in the notifications for this resource. BASIC will include only the contents of the event as it would appear in AWS CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created.

CreatedBy (string) --The name or email alias of the person who created the notification rule.

Status (string) --The status of the notification rule. Valid statuses are on (sending notifications) or off (not sending notifications).

CreatedTimestamp (datetime) --The date and time the notification rule was created, in timestamp format.

LastModifiedTimestamp (datetime) --The date and time the notification rule was most recently updated, in timestamp format.

Tags (dict) --The tags associated with the notification rule.

(string) --
(string) --









Exceptions

CodeStarNotifications.Client.exceptions.ResourceNotFoundException
CodeStarNotifications.Client.exceptions.ValidationException


    :return: {
        'Arn': 'string',
        'Name': 'string',
        'EventTypes': [
            {
                'EventTypeId': 'string',
                'ServiceName': 'string',
                'EventTypeName': 'string',
                'ResourceType': 'string'
            },
        ],
        'Resource': 'string',
        'Targets': [
            {
                'TargetAddress': 'string',
                'TargetType': 'string',
                'TargetStatus': 'PENDING'|'ACTIVE'|'UNREACHABLE'|'INACTIVE'|'DEACTIVATED'
            },
        ],
        'DetailType': 'BASIC'|'FULL',
        'CreatedBy': 'string',
        'Status': 'ENABLED'|'DISABLED',
        'CreatedTimestamp': datetime(2015, 1, 1),
        'LastModifiedTimestamp': datetime(2015, 1, 1),
        'Tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    CodeStarNotifications.Client.exceptions.ResourceNotFoundException
    CodeStarNotifications.Client.exceptions.ValidationException
    
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

def list_event_types(Filters=None, NextToken=None, MaxResults=None):
    """
    Returns information about the event types available for configuring notifications.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_event_types(
        Filters=[
            {
                'Name': 'RESOURCE_TYPE'|'SERVICE_NAME',
                'Value': 'string'
            },
        ],
        NextToken='string',
        MaxResults=123
    )
    
    
    :type Filters: list
    :param Filters: The filters to use to return information by service or resource type.\n\n(dict) --Information about a filter to apply to the list of returned event types. You can filter by resource type or service name.\n\nName (string) -- [REQUIRED]The system-generated name of the filter type you want to filter by.\n\nValue (string) -- [REQUIRED]The name of the resource type (for example, pipeline) or service name (for example, CodePipeline) that you want to filter by.\n\n\n\n\n

    :type NextToken: string
    :param NextToken: An enumeration token that, when provided in a request, returns the next batch of the results.

    :type MaxResults: integer
    :param MaxResults: A non-negative integer used to limit the number of returned results. The default number is 50. The maximum number of results that can be returned is 100.

    :rtype: dict

ReturnsResponse Syntax
{
    'EventTypes': [
        {
            'EventTypeId': 'string',
            'ServiceName': 'string',
            'EventTypeName': 'string',
            'ResourceType': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

EventTypes (list) --
Information about each event, including service name, resource type, event ID, and event name.

(dict) --
Returns information about an event that has triggered a notification rule.

EventTypeId (string) --
The system-generated ID of the event.

ServiceName (string) --
The name of the service for which the event applies.

EventTypeName (string) --
The name of the event.

ResourceType (string) --
The resource type of the event.





NextToken (string) --
An enumeration token that can be used in a request to return the next batch of the results.







Exceptions

CodeStarNotifications.Client.exceptions.InvalidNextTokenException
CodeStarNotifications.Client.exceptions.ValidationException


    :return: {
        'EventTypes': [
            {
                'EventTypeId': 'string',
                'ServiceName': 'string',
                'EventTypeName': 'string',
                'ResourceType': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    CodeStarNotifications.Client.exceptions.InvalidNextTokenException
    CodeStarNotifications.Client.exceptions.ValidationException
    
    """
    pass

def list_notification_rules(Filters=None, NextToken=None, MaxResults=None):
    """
    Returns a list of the notification rules for an AWS account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_notification_rules(
        Filters=[
            {
                'Name': 'EVENT_TYPE_ID'|'CREATED_BY'|'RESOURCE'|'TARGET_ADDRESS',
                'Value': 'string'
            },
        ],
        NextToken='string',
        MaxResults=123
    )
    
    
    :type Filters: list
    :param Filters: The filters to use to return information by service or resource type. For valid values, see ListNotificationRulesFilter .\n\nNote\nA filter with the same name can appear more than once when used with OR statements. Filters with different names should be applied with AND statements.\n\n\n(dict) --Information about a filter to apply to the list of returned notification rules. You can filter by event type, owner, resource, or target.\n\nName (string) -- [REQUIRED]The name of the attribute you want to use to filter the returned notification rules.\n\nValue (string) -- [REQUIRED]The value of the attribute you want to use to filter the returned notification rules. For example, if you specify filtering by RESOURCE in Name, you might specify the ARN of a pipeline in AWS CodePipeline for the value.\n\n\n\n\n

    :type NextToken: string
    :param NextToken: An enumeration token that, when provided in a request, returns the next batch of the results.

    :type MaxResults: integer
    :param MaxResults: A non-negative integer used to limit the number of returned results. The maximum number of results that can be returned is 100.

    :rtype: dict

ReturnsResponse Syntax
{
    'NextToken': 'string',
    'NotificationRules': [
        {
            'Id': 'string',
            'Arn': 'string'
        },
    ]
}


Response Structure

(dict) --

NextToken (string) --
An enumeration token that can be used in a request to return the next batch of the results.

NotificationRules (list) --
The list of notification rules for the AWS account, by Amazon Resource Name (ARN) and ID.

(dict) --
Information about a specified notification rule.

Id (string) --
The unique ID of the notification rule.

Arn (string) --
The Amazon Resource Name (ARN) of the notification rule.











Exceptions

CodeStarNotifications.Client.exceptions.InvalidNextTokenException
CodeStarNotifications.Client.exceptions.ValidationException


    :return: {
        'NextToken': 'string',
        'NotificationRules': [
            {
                'Id': 'string',
                'Arn': 'string'
            },
        ]
    }
    
    
    :returns: 
    CodeStarNotifications.Client.exceptions.InvalidNextTokenException
    CodeStarNotifications.Client.exceptions.ValidationException
    
    """
    pass

def list_tags_for_resource(Arn=None):
    """
    Returns a list of the tags associated with a notification rule.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        Arn='string'
    )
    
    
    :type Arn: string
    :param Arn: [REQUIRED]\nThe Amazon Resource Name (ARN) for the notification rule.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --
Tags (dict) --The tags associated with the notification rule.

(string) --
(string) --









Exceptions

CodeStarNotifications.Client.exceptions.ResourceNotFoundException
CodeStarNotifications.Client.exceptions.ValidationException


    :return: {
        'Tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    CodeStarNotifications.Client.exceptions.ResourceNotFoundException
    CodeStarNotifications.Client.exceptions.ValidationException
    
    """
    pass

def list_targets(Filters=None, NextToken=None, MaxResults=None):
    """
    Returns a list of the notification rule targets for an AWS account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_targets(
        Filters=[
            {
                'Name': 'TARGET_TYPE'|'TARGET_ADDRESS'|'TARGET_STATUS',
                'Value': 'string'
            },
        ],
        NextToken='string',
        MaxResults=123
    )
    
    
    :type Filters: list
    :param Filters: The filters to use to return information by service or resource type. Valid filters include target type, target address, and target status.\n\nNote\nA filter with the same name can appear more than once when used with OR statements. Filters with different names should be applied with AND statements.\n\n\n(dict) --Information about a filter to apply to the list of returned targets. You can filter by target type, address, or status. For example, to filter results to notification rules that have active Amazon SNS topics as targets, you could specify a ListTargetsFilter Name as TargetType and a Value of SNS, and a Name of TARGET_STATUS and a Value of ACTIVE.\n\nName (string) -- [REQUIRED]The name of the attribute you want to use to filter the returned targets.\n\nValue (string) -- [REQUIRED]The value of the attribute you want to use to filter the returned targets. For example, if you specify SNS for the Target type, you could specify an Amazon Resource Name (ARN) for a topic as the value.\n\n\n\n\n

    :type NextToken: string
    :param NextToken: An enumeration token that, when provided in a request, returns the next batch of the results.

    :type MaxResults: integer
    :param MaxResults: A non-negative integer used to limit the number of returned results. The maximum number of results that can be returned is 100.

    :rtype: dict

ReturnsResponse Syntax
{
    'Targets': [
        {
            'TargetAddress': 'string',
            'TargetType': 'string',
            'TargetStatus': 'PENDING'|'ACTIVE'|'UNREACHABLE'|'INACTIVE'|'DEACTIVATED'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Targets (list) --
The list of notification rule targets.

(dict) --
Information about the targets specified for a notification rule.

TargetAddress (string) --
The Amazon Resource Name (ARN) of the SNS topic.

TargetType (string) --
The type of the target (for example, SNS).

TargetStatus (string) --
The status of the target.





NextToken (string) --
An enumeration token that can be used in a request to return the next batch of results.







Exceptions

CodeStarNotifications.Client.exceptions.InvalidNextTokenException
CodeStarNotifications.Client.exceptions.ValidationException


    :return: {
        'Targets': [
            {
                'TargetAddress': 'string',
                'TargetType': 'string',
                'TargetStatus': 'PENDING'|'ACTIVE'|'UNREACHABLE'|'INACTIVE'|'DEACTIVATED'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    CodeStarNotifications.Client.exceptions.InvalidNextTokenException
    CodeStarNotifications.Client.exceptions.ValidationException
    
    """
    pass

def subscribe(Arn=None, Target=None, ClientRequestToken=None):
    """
    Creates an association between a notification rule and an SNS topic so that the associated target can receive notifications when the events described in the rule are triggered.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.subscribe(
        Arn='string',
        Target={
            'TargetType': 'string',
            'TargetAddress': 'string'
        },
        ClientRequestToken='string'
    )
    
    
    :type Arn: string
    :param Arn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the notification rule for which you want to create the association.\n

    :type Target: dict
    :param Target: [REQUIRED]\nInformation about the SNS topics associated with a notification rule.\n\nTargetType (string) --The target type. Can be an Amazon SNS topic.\n\nTargetAddress (string) --The Amazon Resource Name (ARN) of the SNS topic.\n\n\n

    :type ClientRequestToken: string
    :param ClientRequestToken: An enumeration token that, when provided in a request, returns the next batch of the results.

    :rtype: dict

ReturnsResponse Syntax
{
    'Arn': 'string'
}


Response Structure

(dict) --

Arn (string) --
The Amazon Resource Name (ARN) of the notification rule for which you have created assocations.







Exceptions

CodeStarNotifications.Client.exceptions.ValidationException
CodeStarNotifications.Client.exceptions.ResourceNotFoundException


    :return: {
        'Arn': 'string'
    }
    
    
    :returns: 
    CodeStarNotifications.Client.exceptions.ValidationException
    CodeStarNotifications.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def tag_resource(Arn=None, Tags=None):
    """
    Associates a set of provided tags with a notification rule.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        Arn='string',
        Tags={
            'string': 'string'
        }
    )
    
    
    :type Arn: string
    :param Arn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the notification rule to tag.\n

    :type Tags: dict
    :param Tags: [REQUIRED]\nThe list of tags to associate with the resource. Tag key names cannot start with 'aws'.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --

Tags (dict) --
The list of tags associated with the resource.

(string) --
(string) --










Exceptions

CodeStarNotifications.Client.exceptions.ResourceNotFoundException
CodeStarNotifications.Client.exceptions.ValidationException
CodeStarNotifications.Client.exceptions.ConcurrentModificationException


    :return: {
        'Tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def unsubscribe(Arn=None, TargetAddress=None):
    """
    Removes an association between a notification rule and an Amazon SNS topic so that subscribers to that topic stop receiving notifications when the events described in the rule are triggered.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.unsubscribe(
        Arn='string',
        TargetAddress='string'
    )
    
    
    :type Arn: string
    :param Arn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the notification rule.\n

    :type TargetAddress: string
    :param TargetAddress: [REQUIRED]\nThe ARN of the SNS topic to unsubscribe from the notification rule.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Arn': 'string'
}


Response Structure

(dict) --

Arn (string) --
The Amazon Resource Name (ARN) of the the notification rule from which you have removed a subscription.







Exceptions

CodeStarNotifications.Client.exceptions.ValidationException


    :return: {
        'Arn': 'string'
    }
    
    
    :returns: 
    CodeStarNotifications.Client.exceptions.ValidationException
    
    """
    pass

def untag_resource(Arn=None, TagKeys=None):
    """
    Removes the association between one or more provided tags and a notification rule.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        Arn='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type Arn: string
    :param Arn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the notification rule from which to remove the tags.\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nThe key names of the tags to remove.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

CodeStarNotifications.Client.exceptions.ResourceNotFoundException
CodeStarNotifications.Client.exceptions.ValidationException
CodeStarNotifications.Client.exceptions.ConcurrentModificationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_notification_rule(Arn=None, Name=None, Status=None, EventTypeIds=None, Targets=None, DetailType=None):
    """
    Updates a notification rule for a resource. You can change the events that trigger the notification rule, the status of the rule, and the targets that receive the notifications.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_notification_rule(
        Arn='string',
        Name='string',
        Status='ENABLED'|'DISABLED',
        EventTypeIds=[
            'string',
        ],
        Targets=[
            {
                'TargetType': 'string',
                'TargetAddress': 'string'
            },
        ],
        DetailType='BASIC'|'FULL'
    )
    
    
    :type Arn: string
    :param Arn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the notification rule.\n

    :type Name: string
    :param Name: The name of the notification rule.

    :type Status: string
    :param Status: The status of the notification rule. Valid statuses include enabled (sending notifications) or disabled (not sending notifications).

    :type EventTypeIds: list
    :param EventTypeIds: A list of event types associated with this notification rule.\n\n(string) --\n\n

    :type Targets: list
    :param Targets: The address and type of the targets to receive notifications from this notification rule.\n\n(dict) --Information about the SNS topics associated with a notification rule.\n\nTargetType (string) --The target type. Can be an Amazon SNS topic.\n\nTargetAddress (string) --The Amazon Resource Name (ARN) of the SNS topic.\n\n\n\n\n

    :type DetailType: string
    :param DetailType: The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in AWS CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

CodeStarNotifications.Client.exceptions.ValidationException
CodeStarNotifications.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

