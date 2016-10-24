'''

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

def delete_rule(Name=None):
    """
    Deletes a rule. You must remove all targets from a rule using  RemoveTargets before you can delete the rule.
    
    
    :example: response = client.delete_rule(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the rule to be deleted.
            

    """
    pass

def describe_rule(Name=None):
    """
    Describes the details of the specified rule.
    
    
    :example: response = client.describe_rule(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the rule you want to describe details for.
            

    :rtype: dict
    :return: {
        'Name': 'string',
        'Arn': 'string',
        'EventPattern': 'string',
        'ScheduleExpression': 'string',
        'State': 'ENABLED'|'DISABLED',
        'Description': 'string',
        'RoleArn': 'string'
    }
    
    
    """
    pass

def disable_rule(Name=None):
    """
    Disables a rule. A disabled rule won't match any events, and won't self-trigger if it has a schedule expression.
    
    
    :example: response = client.disable_rule(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the rule you want to disable.
            

    """
    pass

def enable_rule(Name=None):
    """
    Enables a rule. If the rule does not exist, the operation fails.
    
    
    :example: response = client.enable_rule(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the rule that you want to enable.
            

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

def list_rule_names_by_target(TargetArn=None, NextToken=None, Limit=None):
    """
    Lists the names of the rules that the given target is put to. You can see which of the rules in Amazon CloudWatch Events can invoke a specific target in your account. If you have more rules in your account than the given limit, the results will be paginated. In that case, use the next token returned in the response and repeat ListRulesByTarget until the NextToken in the response is returned as null.
    
    
    :example: response = client.list_rule_names_by_target(
        TargetArn='string',
        NextToken='string',
        Limit=123
    )
    
    
    :type TargetArn: string
    :param TargetArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the target resource that you want to list the rules for.
            

    :type NextToken: string
    :param NextToken: The token returned by a previous call to indicate that there is more data available.

    :type Limit: integer
    :param Limit: The maximum number of results to return.

    :rtype: dict
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

def list_rules(NamePrefix=None, NextToken=None, Limit=None):
    """
    Lists the Amazon CloudWatch Events rules in your account. You can either list all the rules or you can provide a prefix to match to the rule names. If you have more rules in your account than the given limit, the results will be paginated. In that case, use the next token returned in the response and repeat ListRules until the NextToken in the response is returned as null.
    
    
    :example: response = client.list_rules(
        NamePrefix='string',
        NextToken='string',
        Limit=123
    )
    
    
    :type NamePrefix: string
    :param NamePrefix: The prefix matching the rule name.

    :type NextToken: string
    :param NextToken: The token returned by a previous call to indicate that there is more data available.

    :type Limit: integer
    :param Limit: The maximum number of results to return.

    :rtype: dict
    :return: {
        'Rules': [
            {
                'Name': 'string',
                'Arn': 'string',
                'EventPattern': 'string',
                'State': 'ENABLED'|'DISABLED',
                'Description': 'string',
                'ScheduleExpression': 'string',
                'RoleArn': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_targets_by_rule(Rule=None, NextToken=None, Limit=None):
    """
    Lists of targets assigned to the rule.
    
    
    :example: response = client.list_targets_by_rule(
        Rule='string',
        NextToken='string',
        Limit=123
    )
    
    
    :type Rule: string
    :param Rule: [REQUIRED]
            The name of the rule whose targets you want to list.
            

    :type NextToken: string
    :param NextToken: The token returned by a previous call to indicate that there is more data available.

    :type Limit: integer
    :param Limit: The maximum number of results to return.

    :rtype: dict
    :return: {
        'Targets': [
            {
                'Id': 'string',
                'Arn': 'string',
                'Input': 'string',
                'InputPath': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Neither Input nor InputPath is specified, then the entire event is passed to the target in JSON form.
    InputPath is specified in the form of JSONPath (e.g. $.detail ), then only the part of the event specified in the path is passed to the target (e.g. only the detail part of the event is passed).
    Input is specified in the form of a valid JSON, then the matched event is overridden with this constant.
    
    """
    pass

def put_events(Entries=None):
    """
    Sends custom events to Amazon CloudWatch Events so that they can be matched to rules.
    
    
    :example: response = client.put_events(
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
    :param Entries: [REQUIRED]
            The entry that defines an event in your system. You can specify several parameters for the entry such as the source and type of the event, resources associated with the event, and so on.
            (dict) --Contains information about the event to be used in PutEvents.
            Time (datetime) --Timestamp of event, per RFC3339 . If no timestamp is provided, the timestamp of the PutEvents call will be used.
            Source (string) --The source of the event.
            Resources (list) --AWS resources, identified by Amazon Resource Name (ARN), which the event primarily concerns. Any number, including zero, may be present.
            (string) --
            DetailType (string) --Free-form string used to decide what fields to expect in the event detail.
            Detail (string) --In the JSON sense, an object containing fields, which may also contain nested sub-objects. No constraints are imposed on its contents.
            
            

    :rtype: dict
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
    
    
    """
    pass

def put_rule(Name=None, ScheduleExpression=None, EventPattern=None, State=None, Description=None, RoleArn=None):
    """
    Creates or updates a rule. Rules are enabled by default, or based on value of the State parameter. You can disable a rule using  DisableRule .
    A rule must contain at least an EventPattern or ScheduleExpression. Rules with EventPatterns are triggered when a matching event is observed. Rules with ScheduleExpressions self-trigger based on the given schedule. A rule can have both an EventPattern and a ScheduleExpression, in which case the rule will trigger on matching events as well as on a schedule.
    
    
    :example: response = client.put_rule(
        Name='string',
        ScheduleExpression='string',
        EventPattern='string',
        State='ENABLED'|'DISABLED',
        Description='string',
        RoleArn='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the rule that you are creating or updating.
            

    :type ScheduleExpression: string
    :param ScheduleExpression: The scheduling expression. For example, 'cron(0 20 * * ? *)', 'rate(5 minutes)'.

    :type EventPattern: string
    :param EventPattern: The event pattern.

    :type State: string
    :param State: Indicates whether the rule is enabled or disabled.

    :type Description: string
    :param Description: A description of the rule.

    :type RoleArn: string
    :param RoleArn: The Amazon Resource Name (ARN) of the IAM role associated with the rule.

    :rtype: dict
    :return: {
        'RuleArn': 'string'
    }
    
    
    """
    pass

def put_targets(Rule=None, Targets=None):
    """
    Adds target(s) to a rule. Targets are the resources that can be invoked when a rule is triggered. For example, AWS Lambda functions, Amazon Kinesis streams, and built-in targets. Updates the target(s) if they are already associated with the role. In other words, if there is already a target with the given target ID, then the target associated with that ID is updated.
    In order to be able to make API calls against the resources you own, Amazon CloudWatch Events needs the appropriate permissions. For AWS Lambda and Amazon SNS resources, CloudWatch Events relies on resource-based policies. For Amazon Kinesis streams, CloudWatch Events relies on IAM roles. For more information, see Permissions for Sending Events to Targets in the *Amazon CloudWatch Developer Guide* .
    Input and InputPath are mutually-exclusive and optional parameters of a target. When a rule is triggered due to a matched event, if for a target:
    
    
    :example: response = client.put_targets(
        Rule='string',
        Targets=[
            {
                'Id': 'string',
                'Arn': 'string',
                'Input': 'string',
                'InputPath': 'string'
            },
        ]
    )
    
    
    :type Rule: string
    :param Rule: [REQUIRED]
            The name of the rule you want to add targets to.
            

    :type Targets: list
    :param Targets: [REQUIRED]
            List of targets you want to update or add to the rule.
            (dict) --Targets are the resources that can be invoked when a rule is triggered. For example, AWS Lambda functions, Amazon Kinesis streams, and built-in targets.
            Input and InputPath are mutually-exclusive and optional parameters of a target. When a rule is triggered due to a matched event, if for a target:
            Neither Input nor InputPath is specified, then the entire event is passed to the target in JSON form.
            InputPath is specified in the form of JSONPath (e.g. $.detail ), then only the part of the event specified in the path is passed to the target (e.g. only the detail part of the event is passed).
            Input is specified in the form of a valid JSON, then the matched event is overridden with this constant.
            Id (string) -- [REQUIRED]The unique target assignment ID.
            Arn (string) -- [REQUIRED]The Amazon Resource Name (ARN) associated of the target.
            Input (string) --Valid JSON text passed to the target. For more information about JSON text, see The JavaScript Object Notation (JSON) Data Interchange Format .
            InputPath (string) --The value of the JSONPath that is used for extracting part of the matched event when passing it to the target. For more information about JSON paths, see JSONPath .
            
            

    :rtype: dict
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
    Rule (string) -- [REQUIRED]
    The name of the rule you want to add targets to.
    
    Targets (list) -- [REQUIRED]
    List of targets you want to update or add to the rule.
    
    (dict) --Targets are the resources that can be invoked when a rule is triggered. For example, AWS Lambda functions, Amazon Kinesis streams, and built-in targets.
    Input and InputPath are mutually-exclusive and optional parameters of a target. When a rule is triggered due to a matched event, if for a target:
    
    Neither Input nor InputPath is specified, then the entire event is passed to the target in JSON form.
    InputPath is specified in the form of JSONPath (e.g. $.detail ), then only the part of the event specified in the path is passed to the target (e.g. only the detail part of the event is passed).
    Input is specified in the form of a valid JSON, then the matched event is overridden with this constant.
    
    
    Id (string) -- [REQUIRED]The unique target assignment ID.
    
    Arn (string) -- [REQUIRED]The Amazon Resource Name (ARN) associated of the target.
    
    Input (string) --Valid JSON text passed to the target. For more information about JSON text, see The JavaScript Object Notation (JSON) Data Interchange Format .
    
    InputPath (string) --The value of the JSONPath that is used for extracting part of the matched event when passing it to the target. For more information about JSON paths, see JSONPath .
    
    
    
    
    
    
    """
    pass

def remove_targets(Rule=None, Ids=None):
    """
    Removes target(s) from a rule so that when the rule is triggered, those targets will no longer be invoked.
    
    
    :example: response = client.remove_targets(
        Rule='string',
        Ids=[
            'string',
        ]
    )
    
    
    :type Rule: string
    :param Rule: [REQUIRED]
            The name of the rule you want to remove targets from.
            

    :type Ids: list
    :param Ids: [REQUIRED]
            The list of target IDs to remove from the rule.
            (string) --
            

    :rtype: dict
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
    
    
    """
    pass

def test_event_pattern(EventPattern=None, Event=None):
    """
    Tests whether an event pattern matches the provided event.
    
    
    :example: response = client.test_event_pattern(
        EventPattern='string',
        Event='string'
    )
    
    
    :type EventPattern: string
    :param EventPattern: [REQUIRED]
            The event pattern you want to test.
            

    :type Event: string
    :param Event: [REQUIRED]
            The event in the JSON format to test against the event pattern.
            

    :rtype: dict
    :return: {
        'Result': True|False
    }
    
    
    """
    pass

