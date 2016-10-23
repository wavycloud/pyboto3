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


def delete_rule(Name=None):
    """
    :param Name: [REQUIRED]
            The name of the rule to be deleted.
            ReturnsNone
            
    :type Name: string
    """
    pass


def describe_rule(Name=None):
    """
    :param Name: [REQUIRED]
            The name of the rule you want to describe details for.
            Return typedict
            ReturnsResponse Syntax{
              'Name': 'string',
              'Arn': 'string',
              'EventPattern': 'string',
              'ScheduleExpression': 'string',
              'State': 'ENABLED'|'DISABLED',
              'Description': 'string',
              'RoleArn': 'string'
            }
            Response Structure
            (dict) --The result of the DescribeRule operation.
            Name (string) --The rule's name.
            Arn (string) --The Amazon Resource Name (ARN) associated with the rule.
            EventPattern (string) --The event pattern.
            ScheduleExpression (string) --The scheduling expression. For example, 'cron(0 20 * * ? *)', 'rate(5 minutes)'.
            State (string) --Specifies whether the rule is enabled or disabled.
            Description (string) --The rule's description.
            RoleArn (string) --The Amazon Resource Name (ARN) of the IAM role associated with the rule.
            
            
    :type Name: string
    """
    pass


def disable_rule(Name=None):
    """
    :param Name: [REQUIRED]
            The name of the rule you want to disable.
            ReturnsNone
            
    :type Name: string
    """
    pass


def enable_rule(Name=None):
    """
    :param Name: [REQUIRED]
            The name of the rule that you want to enable.
            ReturnsNone
            
    :type Name: string
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


def list_rule_names_by_target(TargetArn=None, NextToken=None, Limit=None):
    """
    :param TargetArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the target resource that you want to list the rules for.
            
    :type TargetArn: string
    :param NextToken: The token returned by a previous call to indicate that there is more data available.
    :type NextToken: string
    :param Limit: The maximum number of results to return.
    :type Limit: integer
    """
    pass


def list_rules(NamePrefix=None, NextToken=None, Limit=None):
    """
    :param NamePrefix: The prefix matching the rule name.
    :type NamePrefix: string
    :param NextToken: The token returned by a previous call to indicate that there is more data available.
    :type NextToken: string
    :param Limit: The maximum number of results to return.
    :type Limit: integer
    """
    pass


def list_targets_by_rule(Rule=None, NextToken=None, Limit=None):
    """
    :param Rule: [REQUIRED]
            The name of the rule whose targets you want to list.
            
    :type Rule: string
    :param NextToken: The token returned by a previous call to indicate that there is more data available.
    :type NextToken: string
    :param Limit: The maximum number of results to return.
    :type Limit: integer
    """
    pass


def put_events(Entries=None):
    """
    :param Entries: [REQUIRED]
            The entry that defines an event in your system. You can specify several parameters for the entry such as the source and type of the event, resources associated with the event, and so on.
            (dict) --Contains information about the event to be used in PutEvents.
            Time (datetime) --Timestamp of event, per RFC3339 . If no timestamp is provided, the timestamp of the PutEvents call will be used.
            Source (string) --The source of the event.
            Resources (list) --AWS resources, identified by Amazon Resource Name (ARN), which the event primarily concerns. Any number, including zero, may be present.
            (string) --
            DetailType (string) --Free-form string used to decide what fields to expect in the event detail.
            Detail (string) --In the JSON sense, an object containing fields, which may also contain nested sub-objects. No constraints are imposed on its contents.
            
            Return typedict
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
            (dict) --The result of the PutEvents operation.
            FailedEntryCount (integer) --The number of failed entries.
            Entries (list) --A list of successfully and unsuccessfully ingested events results. If the ingestion was successful, the entry will have the event ID in it. If not, then the ErrorCode and ErrorMessage can be used to identify the problem with the entry.
            (dict) --A PutEventsResult contains a list of PutEventsResultEntry.
            EventId (string) --The ID of the event submitted to Amazon CloudWatch Events.
            ErrorCode (string) --The error code representing why the event submission failed on this entry.
            ErrorMessage (string) --The error message explaining why the event submission failed on this entry.
            
            
            
    :type Entries: list
    """
    pass


def put_rule(Name=None, ScheduleExpression=None, EventPattern=None, State=None, Description=None, RoleArn=None):
    """
    :param Name: [REQUIRED]
            The name of the rule that you are creating or updating.
            
    :type Name: string
    :param ScheduleExpression: The scheduling expression. For example, 'cron(0 20 * * ? *)', 'rate(5 minutes)'.
    :type ScheduleExpression: string
    :param EventPattern: The event pattern.
    :type EventPattern: string
    :param State: Indicates whether the rule is enabled or disabled.
    :type State: string
    :param Description: A description of the rule.
    :type Description: string
    :param RoleArn: The Amazon Resource Name (ARN) of the IAM role associated with the rule.
    :type RoleArn: string
    """
    pass


def put_targets(Rule=None, Targets=None):
    """
    :param Rule: [REQUIRED]
            The name of the rule you want to add targets to.
            
    :type Rule: string
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
            
            
    :type Targets: list
    """
    pass


def remove_targets(Rule=None, Ids=None):
    """
    :param Rule: [REQUIRED]
            The name of the rule you want to remove targets from.
            
    :type Rule: string
    :param Ids: [REQUIRED]
            The list of target IDs to remove from the rule.
            (string) --
            
    :type Ids: list
    """
    pass


def test_event_pattern(EventPattern=None, Event=None):
    """
    :param EventPattern: [REQUIRED]
            The event pattern you want to test.
            
    :type EventPattern: string
    :param Event: [REQUIRED]
            The event in the JSON format to test against the event pattern.
            
    :type Event: string
    """
    pass
