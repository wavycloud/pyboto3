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

def delete_rule(Name=None):
    """
    Deletes the specified rule.
    You must remove all targets from a rule using  RemoveTargets before you can delete the rule.
    When you delete a rule, incoming events might continue to match to the deleted rule. Please allow a short period of time for changes to take effect.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_rule(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the rule.
            

    """
    pass

def describe_event_bus():
    """
    Displays the external AWS accounts that are permitted to write events to your account using your account's event bus, and the associated policy. To enable your account to receive events from other accounts, use  PutPermission .
    See also: AWS API Documentation
    
    
    :example: response = client.describe_event_bus()
    
    
    :rtype: dict
    :return: {
        'Name': 'string',
        'Arn': 'string',
        'Policy': 'string'
    }
    
    
    """
    pass

def describe_rule(Name=None):
    """
    Describes the specified rule.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_rule(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the rule.
            

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
    Disables the specified rule. A disabled rule won't match any events, and won't self-trigger if it has a schedule expression.
    When you disable a rule, incoming events might continue to match to the disabled rule. Please allow a short period of time for changes to take effect.
    See also: AWS API Documentation
    
    
    :example: response = client.disable_rule(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the rule.
            

    """
    pass

def enable_rule(Name=None):
    """
    Enables the specified rule. If the rule does not exist, the operation fails.
    When you enable a rule, incoming events might not immediately start matching to a newly enabled rule. Please allow a short period of time for changes to take effect.
    See also: AWS API Documentation
    
    
    :example: response = client.enable_rule(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the rule.
            

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

def get_waiter(waiter_name=None):
    """
    
    :type waiter_name: 
    :param waiter_name: 

    """
    pass

def list_rule_names_by_target(TargetArn=None, NextToken=None, Limit=None):
    """
    Lists the rules for the specified target. You can see which of the rules in Amazon CloudWatch Events can invoke a specific target in your account.
    See also: AWS API Documentation
    
    
    :example: response = client.list_rule_names_by_target(
        TargetArn='string',
        NextToken='string',
        Limit=123
    )
    
    
    :type TargetArn: string
    :param TargetArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the target resource.
            

    :type NextToken: string
    :param NextToken: The token returned by a previous call to retrieve the next set of results.

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
    Lists your Amazon CloudWatch Events rules. You can either list all the rules or you can provide a prefix to match to the rule names.
    See also: AWS API Documentation
    
    
    :example: response = client.list_rules(
        NamePrefix='string',
        NextToken='string',
        Limit=123
    )
    
    
    :type NamePrefix: string
    :param NamePrefix: The prefix matching the rule name.

    :type NextToken: string
    :param NextToken: The token returned by a previous call to retrieve the next set of results.

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
    Lists the targets assigned to the specified rule.
    See also: AWS API Documentation
    
    
    :example: response = client.list_targets_by_rule(
        Rule='string',
        NextToken='string',
        Limit=123
    )
    
    
    :type Rule: string
    :param Rule: [REQUIRED]
            The name of the rule.
            

    :type NextToken: string
    :param NextToken: The token returned by a previous call to retrieve the next set of results.

    :type Limit: integer
    :param Limit: The maximum number of results to return.

    :rtype: dict
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
                    'TaskCount': 123
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
    Sends custom events to Amazon CloudWatch Events so that they can be matched to rules.
    See also: AWS API Documentation
    
    
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
            (dict) --Represents an event to be submitted.
            Time (datetime) --The timestamp of the event, per RFC3339 . If no timestamp is provided, the timestamp of the PutEvents call is used.
            Source (string) --The source of the event.
            Resources (list) --AWS resources, identified by Amazon Resource Name (ARN), which the event primarily concerns. Any number, including zero, may be present.
            (string) --
            DetailType (string) --Free-form string used to decide what fields to expect in the event detail.
            Detail (string) --A valid JSON string. There is no other schema imposed. The JSON string may contain fields and nested subobjects.
            
            

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

def put_permission(Action=None, Principal=None, StatementId=None):
    """
    Running PutPermission permits the specified AWS account to put events to your account's default event bus . CloudWatch Events rules in your account are triggered by these events arriving to your default event bus.
    For another account to send events to your account, that external account must have a CloudWatch Events rule with your account's default event bus as a target.
    To enable multiple AWS accounts to put events to your default event bus, run PutPermission once for each of these accounts.
    The permission policy on the default event bus cannot exceed 10KB in size.
    See also: AWS API Documentation
    
    
    :example: response = client.put_permission(
        Action='string',
        Principal='string',
        StatementId='string'
    )
    
    
    :type Action: string
    :param Action: [REQUIRED]
            The action that you are enabling the other account to perform. Currently, this must be events:PutEvents .
            

    :type Principal: string
    :param Principal: [REQUIRED]
            The 12-digit AWS account ID that you are permitting to put events to your default event bus. Specify '*' to permit any account to put events to your default event bus.
            If you specify '*', avoid creating rules that may match undesirable events. To create more secure rules, make sure that the event pattern for each rule contains an account field with a specific account ID from which to receive events. Rules with an account field do not match any events sent from other accounts.
            

    :type StatementId: string
    :param StatementId: [REQUIRED]
            An identifier string for the external account that you are granting permissions to. If you later want to revoke the permission for this external account, specify this StatementId when you run RemovePermission .
            

    """
    pass

def put_rule(Name=None, ScheduleExpression=None, EventPattern=None, State=None, Description=None, RoleArn=None):
    """
    Creates or updates the specified rule. Rules are enabled by default, or based on value of the state. You can disable a rule using  DisableRule .
    If you are updating an existing rule, the rule is completely replaced with what you specify in this PutRule command. If you omit arguments in PutRule , the old values for those arguments are not kept. Instead, they are replaced with null values.
    When you create or update a rule, incoming events might not immediately start matching to new or updated rules. Please allow a short period of time for changes to take effect.
    A rule must contain at least an EventPattern or ScheduleExpression. Rules with EventPatterns are triggered when a matching event is observed. Rules with ScheduleExpressions self-trigger based on the given schedule. A rule can have both an EventPattern and a ScheduleExpression, in which case the rule triggers on matching events as well as on a schedule.
    Most services in AWS treat : or / as the same character in Amazon Resource Names (ARNs). However, CloudWatch Events uses an exact match in event patterns and rules. Be sure to use the correct ARN characters when creating event patterns so that they match the ARN syntax in the event you want to match.
    See also: AWS API Documentation
    
    
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
    :param ScheduleExpression: The scheduling expression. For example, 'cron(0 20 * * ? *)' or 'rate(5 minutes)'.

    :type EventPattern: string
    :param EventPattern: The event pattern. For more information, see Events and Event Patterns in the Amazon CloudWatch Events User Guide .

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
    Adds the specified targets to the specified rule, or updates the targets if they are already associated with the rule.
    Targets are the resources that are invoked when a rule is triggered.
    You can configure the following as targets for CloudWatch Events:
    Note that creating rules with built-in targets is supported only in the AWS Management Console.
    For some target types, PutTargets provides target-specific parameters. If the target is an Amazon Kinesis stream, you can optionally specify which shard the event goes to by using the KinesisParameters argument. To invoke a command on multiple EC2 instances with one rule, you can use the RunCommandParameters field.
    To be able to make API calls against the resources that you own, Amazon CloudWatch Events needs the appropriate permissions. For AWS Lambda and Amazon SNS resources, CloudWatch Events relies on resource-based policies. For EC2 instances, Amazon Kinesis streams, and AWS Step Functions state machines, CloudWatch Events relies on IAM roles that you specify in the RoleARN argument in PutTargets . For more information, see Authentication and Access Control in the Amazon CloudWatch Events User Guide .
    If another AWS account is in the same region and has granted you permission (using PutPermission ), you can send events to that account by setting that account's event bus as a target of the rules in your account. To send the matched events to the other account, specify that account's event bus as the Arn when you run PutTargets . If your account sends events to another account, your account is charged for each sent event. Each event sent to antoher account is charged as a custom event. The account receiving the event is not charged. For more information on pricing, see Amazon CloudWatch Pricing .
    For more information about enabling cross-account events, see  PutPermission .
    When you specify InputPath or InputTransformer , you must use JSON dot notation, not bracket notation.
    When you add targets to a rule and the associated rule triggers soon after, new or updated targets might not be immediately invoked. Please allow a short period of time for changes to take effect.
    This action can partially fail if too many requests are made at the same time. If that happens, FailedEntryCount is non-zero in the response and each entry in FailedEntries provides the ID of the failed target and the error code.
    See also: AWS API Documentation
    
    
    :example: response = client.put_targets(
        Rule='string',
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
                    'TaskCount': 123
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
    :param Rule: [REQUIRED]
            The name of the rule.
            

    :type Targets: list
    :param Targets: [REQUIRED]
            The targets to update or add to the rule.
            (dict) --Targets are the resources to be invoked when a rule is triggered. Target types include EC2 instances, AWS Lambda functions, Amazon Kinesis streams, Amazon ECS tasks, AWS Step Functions state machines, Run Command, and built-in targets.
            Id (string) -- [REQUIRED]The ID of the target.
            Arn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the target.
            RoleArn (string) --The Amazon Resource Name (ARN) of the IAM role to be used for this target when the rule is triggered. If one rule triggers multiple targets, you can use a different IAM role for each target.
            Input (string) --Valid JSON text passed to the target. In this case, nothing from the event itself is passed to the target. For more information, see The JavaScript Object Notation (JSON) Data Interchange Format .
            InputPath (string) --The value of the JSONPath that is used for extracting part of the matched event when passing it to the target. You must use JSON dot notation, not bracket notation. For more information about JSON paths, see JSONPath .
            InputTransformer (dict) --Settings to enable you to provide custom input to a target based on certain event data. You can extract one or more key-value pairs from the event and then use that data to send customized input to the target.
            InputPathsMap (dict) --Map of JSON paths to be extracted from the event. These are key-value pairs, where each value is a JSON path. You must use JSON dot notation, not bracket notation.
            (string) --
            (string) --
            
            InputTemplate (string) -- [REQUIRED]Input template where you can use the values of the keys from InputPathsMap to customize the data sent to the target.
            KinesisParameters (dict) --The custom parameter you can use to control shard assignment, when the target is an Amazon Kinesis stream. If you do not include this parameter, the default is to use the eventId as the partition key.
            PartitionKeyPath (string) -- [REQUIRED]The JSON path to be extracted from the event and used as the partition key. For more information, see Amazon Kinesis Streams Key Concepts in the Amazon Kinesis Streams Developer Guide .
            RunCommandParameters (dict) --Parameters used when you are using the rule to invoke Amazon EC2 Run Command.
            RunCommandTargets (list) -- [REQUIRED]Currently, we support including only one RunCommandTarget block, which specifies either an array of InstanceIds or a tag.
            (dict) --Information about the EC2 instances that are to be sent the command, specified as key-value pairs. Each RunCommandTarget block can include only one key, but this key may specify multiple values.
            Key (string) -- [REQUIRED]Can be either tag: tag-key or InstanceIds .
            Values (list) -- [REQUIRED]If Key is tag: tag-key , Values is a list of tag values. If Key is InstanceIds , Values is a list of Amazon EC2 instance IDs.
            (string) --
            
            
            EcsParameters (dict) --Contains the Amazon ECS task definition and task count to be used, if the event target is an Amazon ECS task. For more information about Amazon ECS tasks, see Task Definitions in the Amazon EC2 Container Service Developer Guide .
            TaskDefinitionArn (string) -- [REQUIRED]The ARN of the task definition to use if the event target is an Amazon ECS cluster.
            TaskCount (integer) --The number of tasks to create based on the TaskDefinition . The default is one.
            BatchParameters (dict) --Contains the job definition, job name, and other parameters if the event target is an AWS Batch job. For more information about AWS Batch, see Jobs in the AWS Batch User Guide .
            JobDefinition (string) -- [REQUIRED]The ARN or name of the job definition to use if the event target is an AWS Batch job. This job definition must already exist.
            JobName (string) -- [REQUIRED]The name to use for this execution of the job, if the target is an AWS Batch job.
            ArrayProperties (dict) --The array properties for the submitted job, such as the size of the array. The array size can be between 2 and 10,000. If you specify array properties for a job, it becomes an array job. This parameter is used only if the target is an AWS Batch job.
            Size (integer) --The size of the array, if this is an array batch job. Valid values are integers between 2 and 10,000.
            RetryStrategy (dict) --The retry strategy to use for failed jobs, if the target is an AWS Batch job. The retry strategy is the number of times to retry the failed job execution. Valid values are 1 to 10. When you specify a retry strategy here, it overrides the retry strategy defined in the job definition.
            Attempts (integer) --The number of times to attempt to retry, if the job fails. Valid values are 1 to 10.
            
            SqsParameters (dict) --Contains the message group ID to use when the target is a FIFO queue.
            MessageGroupId (string) --The FIFO message group ID to use as the target.
            
            

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
    If none of the following arguments are specified for a target, then the entire event is passed to the target in JSON form (unless the target is Amazon EC2 Run Command or Amazon ECS task, in which case nothing from the event is passed to the target).
    If Input is specified in the form of valid JSON, then the matched event is overridden with this constant.
    If InputPath is specified in the form of JSONPath (for example, $.detail ), then only the part of the event specified in the path is passed to the target (for example, only the detail part of the event is passed).
    If InputTransformer is specified, then one or more specified JSONPaths are extracted from the event and used as values in a template that you specify as the input to the target.
    
    """
    pass

def remove_permission(StatementId=None):
    """
    Revokes the permission of another AWS account to be able to put events to your default event bus. Specify the account to revoke by the StatementId value that you associated with the account when you granted it permission with PutPermission . You can find the StatementId by using  DescribeEventBus .
    See also: AWS API Documentation
    
    
    :example: response = client.remove_permission(
        StatementId='string'
    )
    
    
    :type StatementId: string
    :param StatementId: [REQUIRED]
            The statement ID corresponding to the account that is no longer allowed to put events to the default event bus.
            

    """
    pass

def remove_targets(Rule=None, Ids=None):
    """
    Removes the specified targets from the specified rule. When the rule is triggered, those targets are no longer be invoked.
    When you remove a target, when the associated rule triggers, removed targets might continue to be invoked. Please allow a short period of time for changes to take effect.
    This action can partially fail if too many requests are made at the same time. If that happens, FailedEntryCount is non-zero in the response and each entry in FailedEntries provides the ID of the failed target and the error code.
    See also: AWS API Documentation
    
    
    :example: response = client.remove_targets(
        Rule='string',
        Ids=[
            'string',
        ]
    )
    
    
    :type Rule: string
    :param Rule: [REQUIRED]
            The name of the rule.
            

    :type Ids: list
    :param Ids: [REQUIRED]
            The IDs of the targets to remove from the rule.
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
    Tests whether the specified event pattern matches the provided event.
    Most services in AWS treat : or / as the same character in Amazon Resource Names (ARNs). However, CloudWatch Events uses an exact match in event patterns and rules. Be sure to use the correct ARN characters when creating event patterns so that they match the ARN syntax in the event you want to match.
    See also: AWS API Documentation
    
    
    :example: response = client.test_event_pattern(
        EventPattern='string',
        Event='string'
    )
    
    
    :type EventPattern: string
    :param EventPattern: [REQUIRED]
            The event pattern. For more information, see Events and Event Patterns in the Amazon CloudWatch Events User Guide .
            

    :type Event: string
    :param Event: [REQUIRED]
            The event, in JSON format, to test against the event pattern.
            

    :rtype: dict
    :return: {
        'Result': True|False
    }
    
    
    """
    pass

