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

def clone_receipt_rule_set(RuleSetName=None, OriginalRuleSetName=None):
    """
    Creates a receipt rule set by cloning an existing one. All receipt rules and configurations are copied to the new receipt rule set and are completely independent of the source rule set.
    For information about setting up rule sets, see the Amazon SES Developer Guide .
    You can execute this operation no more than once per second.
    See also: AWS API Documentation
    
    Examples
    The following example creates a receipt rule set by cloning an existing one:
    Expected Output:
    
    :example: response = client.clone_receipt_rule_set(
        RuleSetName='string',
        OriginalRuleSetName='string'
    )
    
    
    :type RuleSetName: string
    :param RuleSetName: [REQUIRED]
            The name of the rule set to create. The name must:
            This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
            Start and end with a letter or number.
            Contain less than 64 characters.
            

    :type OriginalRuleSetName: string
    :param OriginalRuleSetName: [REQUIRED]
            The name of the rule set to clone.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def create_configuration_set(ConfigurationSet=None):
    """
    Creates a configuration set.
    Configuration sets enable you to publish email sending events. For information about using configuration sets, see the Amazon SES Developer Guide .
    You can execute this operation no more than once per second.
    See also: AWS API Documentation
    
    
    :example: response = client.create_configuration_set(
        ConfigurationSet={
            'Name': 'string'
        }
    )
    
    
    :type ConfigurationSet: dict
    :param ConfigurationSet: [REQUIRED]
            A data structure that contains the name of the configuration set.
            Name (string) -- [REQUIRED]The name of the configuration set. The name must meet the following requirements:
            Contain only letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
            Contain 64 characters or fewer.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def create_configuration_set_event_destination(ConfigurationSetName=None, EventDestination=None):
    """
    Creates a configuration set event destination.
    An event destination is the AWS service to which Amazon SES publishes the email sending events associated with a configuration set. For information about using configuration sets, see the Amazon SES Developer Guide .
    You can execute this operation no more than once per second.
    See also: AWS API Documentation
    
    
    :example: response = client.create_configuration_set_event_destination(
        ConfigurationSetName='string',
        EventDestination={
            'Name': 'string',
            'Enabled': True|False,
            'MatchingEventTypes': [
                'send'|'reject'|'bounce'|'complaint'|'delivery'|'open'|'click'|'renderingFailure',
            ],
            'KinesisFirehoseDestination': {
                'IAMRoleARN': 'string',
                'DeliveryStreamARN': 'string'
            },
            'CloudWatchDestination': {
                'DimensionConfigurations': [
                    {
                        'DimensionName': 'string',
                        'DimensionValueSource': 'messageTag'|'emailHeader'|'linkTag',
                        'DefaultDimensionValue': 'string'
                    },
                ]
            },
            'SNSDestination': {
                'TopicARN': 'string'
            }
        }
    )
    
    
    :type ConfigurationSetName: string
    :param ConfigurationSetName: [REQUIRED]
            The name of the configuration set that the event destination should be associated with.
            

    :type EventDestination: dict
    :param EventDestination: [REQUIRED]
            An object that describes the AWS service that email sending event information will be published to.
            Name (string) -- [REQUIRED]The name of the event destination. The name must:
            This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
            Contain less than 64 characters.
            Enabled (boolean) --Sets whether Amazon SES publishes events to this destination when you send an email with the associated configuration set. Set to true to enable publishing to this destination; set to false to prevent publishing to this destination. The default value is false .
            MatchingEventTypes (list) -- [REQUIRED]The type of email sending events to publish to the event destination.
            (string) --
            KinesisFirehoseDestination (dict) --An object that contains the delivery stream ARN and the IAM role ARN associated with an Amazon Kinesis Firehose event destination.
            IAMRoleARN (string) -- [REQUIRED]The ARN of the IAM role under which Amazon SES publishes email sending events to the Amazon Kinesis Firehose stream.
            DeliveryStreamARN (string) -- [REQUIRED]The ARN of the Amazon Kinesis Firehose stream that email sending events should be published to.
            CloudWatchDestination (dict) --An object that contains the names, default values, and sources of the dimensions associated with an Amazon CloudWatch event destination.
            DimensionConfigurations (list) -- [REQUIRED]A list of dimensions upon which to categorize your emails when you publish email sending events to Amazon CloudWatch.
            (dict) --Contains the dimension configuration to use when you publish email sending events to Amazon CloudWatch.
            For information about publishing email sending events to Amazon CloudWatch, see the Amazon SES Developer Guide .
            DimensionName (string) -- [REQUIRED]The name of an Amazon CloudWatch dimension associated with an email sending metric. The name must:
            This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
            Contain less than 256 characters.
            DimensionValueSource (string) -- [REQUIRED]The place where Amazon SES finds the value of a dimension to publish to Amazon CloudWatch. If you want Amazon SES to use the message tags that you specify using an X-SES-MESSAGE-TAGS header or a parameter to the SendEmail /SendRawEmail API, choose messageTag . If you want Amazon SES to use your own email headers, choose emailHeader .
            DefaultDimensionValue (string) -- [REQUIRED]The default value of the dimension that is published to Amazon CloudWatch if you do not provide the value of the dimension when you send an email. The default value must:
            This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
            Contain less than 256 characters.
            
            
            SNSDestination (dict) --An object that contains the topic ARN associated with an Amazon Simple Notification Service (Amazon SNS) event destination.
            TopicARN (string) -- [REQUIRED]The ARN of the Amazon SNS topic that email sending events will be published to. An example of an Amazon SNS topic ARN is arn:aws:sns:us-west-2:123456789012:MyTopic . For more information about Amazon SNS topics, see the Amazon SNS Developer Guide .
            
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def create_configuration_set_tracking_options(ConfigurationSetName=None, TrackingOptions=None):
    """
    Creates an association between a configuration set and a custom domain for open and click event tracking.
    By default, images and links used for tracking open and click events are hosted on domains operated by Amazon SES. You can configure a subdomain of your own to handle these events. For information about using configuration sets, see Configuring Custom Domains to Handle Open and Click Tracking in the Amazon SES Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.create_configuration_set_tracking_options(
        ConfigurationSetName='string',
        TrackingOptions={
            'CustomRedirectDomain': 'string'
        }
    )
    
    
    :type ConfigurationSetName: string
    :param ConfigurationSetName: [REQUIRED]
            The name of the configuration set that the tracking options should be associated with.
            

    :type TrackingOptions: dict
    :param TrackingOptions: [REQUIRED]
            A domain that is used to redirect email recipients to an Amazon SES-operated domain. This domain captures open and click events generated by Amazon SES emails.
            For more information, see Configuring Custom Domains to Handle Open and Click Tracking in the Amazon SES Developer Guide .
            CustomRedirectDomain (string) --The custom subdomain that will be used to redirect email recipients to the Amazon SES event tracking domain.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def create_custom_verification_email_template(TemplateName=None, FromEmailAddress=None, TemplateSubject=None, TemplateContent=None, SuccessRedirectionURL=None, FailureRedirectionURL=None):
    """
    Creates a new custom verification email template.
    For more information about custom verification email templates, see Using Custom Verification Email Templates in the Amazon SES Developer Guide .
    You can execute this operation no more than once per second.
    See also: AWS API Documentation
    
    
    :example: response = client.create_custom_verification_email_template(
        TemplateName='string',
        FromEmailAddress='string',
        TemplateSubject='string',
        TemplateContent='string',
        SuccessRedirectionURL='string',
        FailureRedirectionURL='string'
    )
    
    
    :type TemplateName: string
    :param TemplateName: [REQUIRED]
            The name of the custom verification email template.
            

    :type FromEmailAddress: string
    :param FromEmailAddress: [REQUIRED]
            The email address that the custom verification email is sent from.
            

    :type TemplateSubject: string
    :param TemplateSubject: [REQUIRED]
            The subject line of the custom verification email.
            

    :type TemplateContent: string
    :param TemplateContent: [REQUIRED]
            The content of the custom verification email. The total size of the email must be less than 10 MB. The message body may contain HTML, with some limitations. For more information, see Custom Verification Email Frequently Asked Questions in the Amazon SES Developer Guide .
            

    :type SuccessRedirectionURL: string
    :param SuccessRedirectionURL: [REQUIRED]
            The URL that the recipient of the verification email is sent to if his or her address is successfully verified.
            

    :type FailureRedirectionURL: string
    :param FailureRedirectionURL: [REQUIRED]
            The URL that the recipient of the verification email is sent to if his or her address is not successfully verified.
            

    """
    pass

def create_receipt_filter(Filter=None):
    """
    Creates a new IP address filter.
    For information about setting up IP address filters, see the Amazon SES Developer Guide .
    You can execute this operation no more than once per second.
    See also: AWS API Documentation
    
    Examples
    The following example creates a new IP address filter:
    Expected Output:
    
    :example: response = client.create_receipt_filter(
        Filter={
            'Name': 'string',
            'IpFilter': {
                'Policy': 'Block'|'Allow',
                'Cidr': 'string'
            }
        }
    )
    
    
    :type Filter: dict
    :param Filter: [REQUIRED]
            A data structure that describes the IP address filter to create, which consists of a name, an IP address range, and whether to allow or block mail from it.
            Name (string) -- [REQUIRED]The name of the IP address filter. The name must:
            This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
            Start and end with a letter or number.
            Contain less than 64 characters.
            IpFilter (dict) -- [REQUIRED]A structure that provides the IP addresses to block or allow, and whether to block or allow incoming mail from them.
            Policy (string) -- [REQUIRED]Indicates whether to block or allow incoming mail from the specified IP addresses.
            Cidr (string) -- [REQUIRED]A single IP address or a range of IP addresses that you want to block or allow, specified in Classless Inter-Domain Routing (CIDR) notation. An example of a single email address is 10.0.0.1. An example of a range of IP addresses is 10.0.0.1/24. For more information about CIDR notation, see RFC 2317 .
            
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def create_receipt_rule(RuleSetName=None, After=None, Rule=None):
    """
    Creates a receipt rule.
    For information about setting up receipt rules, see the Amazon SES Developer Guide .
    You can execute this operation no more than once per second.
    See also: AWS API Documentation
    
    Examples
    The following example creates a new receipt rule:
    Expected Output:
    
    :example: response = client.create_receipt_rule(
        RuleSetName='string',
        After='string',
        Rule={
            'Name': 'string',
            'Enabled': True|False,
            'TlsPolicy': 'Require'|'Optional',
            'Recipients': [
                'string',
            ],
            'Actions': [
                {
                    'S3Action': {
                        'TopicArn': 'string',
                        'BucketName': 'string',
                        'ObjectKeyPrefix': 'string',
                        'KmsKeyArn': 'string'
                    },
                    'BounceAction': {
                        'TopicArn': 'string',
                        'SmtpReplyCode': 'string',
                        'StatusCode': 'string',
                        'Message': 'string',
                        'Sender': 'string'
                    },
                    'WorkmailAction': {
                        'TopicArn': 'string',
                        'OrganizationArn': 'string'
                    },
                    'LambdaAction': {
                        'TopicArn': 'string',
                        'FunctionArn': 'string',
                        'InvocationType': 'Event'|'RequestResponse'
                    },
                    'StopAction': {
                        'Scope': 'RuleSet',
                        'TopicArn': 'string'
                    },
                    'AddHeaderAction': {
                        'HeaderName': 'string',
                        'HeaderValue': 'string'
                    },
                    'SNSAction': {
                        'TopicArn': 'string',
                        'Encoding': 'UTF-8'|'Base64'
                    }
                },
            ],
            'ScanEnabled': True|False
        }
    )
    
    
    :type RuleSetName: string
    :param RuleSetName: [REQUIRED]
            The name of the rule set that the receipt rule will be added to.
            

    :type After: string
    :param After: The name of an existing rule after which the new rule will be placed. If this parameter is null, the new rule will be inserted at the beginning of the rule list.

    :type Rule: dict
    :param Rule: [REQUIRED]
            A data structure that contains the specified rule's name, actions, recipients, domains, enabled status, scan status, and TLS policy.
            Name (string) -- [REQUIRED]The name of the receipt rule. The name must:
            This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
            Start and end with a letter or number.
            Contain less than 64 characters.
            Enabled (boolean) --If true , the receipt rule is active. The default value is false .
            TlsPolicy (string) --Specifies whether Amazon SES should require that incoming email is delivered over a connection encrypted with Transport Layer Security (TLS). If this parameter is set to Require , Amazon SES will bounce emails that are not received over TLS. The default is Optional .
            Recipients (list) --The recipient domains and email addresses that the receipt rule applies to. If this field is not specified, this rule will match all recipients under all verified domains.
            (string) --
            Actions (list) --An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule.
            (dict) --An action that Amazon SES can take when it receives an email on behalf of one or more email addresses or domains that you own. An instance of this data type can represent only one action.
            For information about setting up receipt rules, see the Amazon SES Developer Guide .
            S3Action (dict) --Saves the received message to an Amazon Simple Storage Service (Amazon S3) bucket and, optionally, publishes a notification to Amazon SNS.
            TopicArn (string) --The ARN of the Amazon SNS topic to notify when the message is saved to the Amazon S3 bucket. An example of an Amazon SNS topic ARN is arn:aws:sns:us-west-2:123456789012:MyTopic . For more information about Amazon SNS topics, see the Amazon SNS Developer Guide .
            BucketName (string) -- [REQUIRED]The name of the Amazon S3 bucket that incoming email will be saved to.
            ObjectKeyPrefix (string) --The key prefix of the Amazon S3 bucket. The key prefix is similar to a directory name that enables you to store similar data under the same directory in a bucket.
            KmsKeyArn (string) --The customer master key that Amazon SES should use to encrypt your emails before saving them to the Amazon S3 bucket. You can use the default master key or a custom master key you created in AWS KMS as follows:
            To use the default master key, provide an ARN in the form of arn:aws:kms:REGION:ACCOUNT-ID-WITHOUT-HYPHENS:alias/aws/ses . For example, if your AWS account ID is 123456789012 and you want to use the default master key in the US West (Oregon) region, the ARN of the default master key would be arn:aws:kms:us-west-2:123456789012:alias/aws/ses . If you use the default master key, you don't need to perform any extra steps to give Amazon SES permission to use the key.
            To use a custom master key you created in AWS KMS, provide the ARN of the master key and ensure that you add a statement to your key's policy to give Amazon SES permission to use it. For more information about giving permissions, see the Amazon SES Developer Guide .
            For more information about key policies, see the AWS KMS Developer Guide . If you do not specify a master key, Amazon SES will not encrypt your emails.
            Warning
            Your mail is encrypted by Amazon SES using the Amazon S3 encryption client before the mail is submitted to Amazon S3 for storage. It is not encrypted using Amazon S3 server-side encryption. This means that you must use the Amazon S3 encryption client to decrypt the email after retrieving it from Amazon S3, as the service has no access to use your AWS KMS keys for decryption. This encryption client is currently available with the AWS Java SDK and AWS Ruby SDK only. For more information about client-side encryption using AWS KMS master keys, see the Amazon S3 Developer Guide .
            
            BounceAction (dict) --Rejects the received email by returning a bounce response to the sender and, optionally, publishes a notification to Amazon Simple Notification Service (Amazon SNS).
            TopicArn (string) --The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the bounce action is taken. An example of an Amazon SNS topic ARN is arn:aws:sns:us-west-2:123456789012:MyTopic . For more information about Amazon SNS topics, see the Amazon SNS Developer Guide .
            SmtpReplyCode (string) -- [REQUIRED]The SMTP reply code, as defined by RFC 5321 .
            StatusCode (string) --The SMTP enhanced status code, as defined by RFC 3463 .
            Message (string) -- [REQUIRED]Human-readable text to include in the bounce message.
            Sender (string) -- [REQUIRED]The email address of the sender of the bounced email. This is the address from which the bounce message will be sent.
            WorkmailAction (dict) --Calls Amazon WorkMail and, optionally, publishes a notification to Amazon SNS.
            TopicArn (string) --The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the WorkMail action is called. An example of an Amazon SNS topic ARN is arn:aws:sns:us-west-2:123456789012:MyTopic . For more information about Amazon SNS topics, see the Amazon SNS Developer Guide .
            OrganizationArn (string) -- [REQUIRED]The ARN of the Amazon WorkMail organization. An example of an Amazon WorkMail organization ARN is arn:aws:workmail:us-west-2:123456789012:organization/m-68755160c4cb4e29a2b2f8fb58f359d7 . For information about Amazon WorkMail organizations, see the Amazon WorkMail Administrator Guide .
            LambdaAction (dict) --Calls an AWS Lambda function, and optionally, publishes a notification to Amazon SNS.
            TopicArn (string) --The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the Lambda action is taken. An example of an Amazon SNS topic ARN is arn:aws:sns:us-west-2:123456789012:MyTopic . For more information about Amazon SNS topics, see the Amazon SNS Developer Guide .
            FunctionArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the AWS Lambda function. An example of an AWS Lambda function ARN is arn:aws:lambda:us-west-2:account-id:function:MyFunction . For more information about AWS Lambda, see the AWS Lambda Developer Guide .
            InvocationType (string) --The invocation type of the AWS Lambda function. An invocation type of RequestResponse means that the execution of the function will immediately result in a response, and a value of Event means that the function will be invoked asynchronously. The default value is Event . For information about AWS Lambda invocation types, see the AWS Lambda Developer Guide .
            Warning
            There is a 30-second timeout on RequestResponse invocations. You should use Event invocation in most cases. Use RequestResponse only when you want to make a mail flow decision, such as whether to stop the receipt rule or the receipt rule set.
            
            StopAction (dict) --Terminates the evaluation of the receipt rule set and optionally publishes a notification to Amazon SNS.
            Scope (string) -- [REQUIRED]The name of the RuleSet that is being stopped.
            TopicArn (string) --The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the stop action is taken. An example of an Amazon SNS topic ARN is arn:aws:sns:us-west-2:123456789012:MyTopic . For more information about Amazon SNS topics, see the Amazon SNS Developer Guide .
            AddHeaderAction (dict) --Adds a header to the received email.
            HeaderName (string) -- [REQUIRED]The name of the header to add. Must be between 1 and 50 characters, inclusive, and consist of alphanumeric (a-z, A-Z, 0-9) characters and dashes only.
            HeaderValue (string) -- [REQUIRED]Must be less than 2048 characters, and must not contain newline characters ('r' or 'n').
            SNSAction (dict) --Publishes the email content within a notification to Amazon SNS.
            TopicArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the Amazon SNS topic to notify. An example of an Amazon SNS topic ARN is arn:aws:sns:us-west-2:123456789012:MyTopic . For more information about Amazon SNS topics, see the Amazon SNS Developer Guide .
            Encoding (string) --The encoding to use for the email within the Amazon SNS notification. UTF-8 is easier to use, but may not preserve all special characters when a message was encoded with a different encoding format. Base64 preserves all special characters. The default value is UTF-8.
            
            ScanEnabled (boolean) --If true , then messages that this receipt rule applies to are scanned for spam and viruses. The default value is false .
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def create_receipt_rule_set(RuleSetName=None):
    """
    Creates an empty receipt rule set.
    For information about setting up receipt rule sets, see the Amazon SES Developer Guide .
    You can execute this operation no more than once per second.
    See also: AWS API Documentation
    
    Examples
    The following example creates an empty receipt rule set:
    Expected Output:
    
    :example: response = client.create_receipt_rule_set(
        RuleSetName='string'
    )
    
    
    :type RuleSetName: string
    :param RuleSetName: [REQUIRED]
            The name of the rule set to create. The name must:
            This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
            Start and end with a letter or number.
            Contain less than 64 characters.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def create_template(Template=None):
    """
    Creates an email template. Email templates enable you to send personalized email to one or more destinations in a single API operation. For more information, see the Amazon SES Developer Guide .
    You can execute this operation no more than once per second.
    See also: AWS API Documentation
    
    
    :example: response = client.create_template(
        Template={
            'TemplateName': 'string',
            'SubjectPart': 'string',
            'TextPart': 'string',
            'HtmlPart': 'string'
        }
    )
    
    
    :type Template: dict
    :param Template: [REQUIRED]
            The content of the email, composed of a subject line, an HTML part, and a text-only part.
            TemplateName (string) -- [REQUIRED]The name of the template. You will refer to this name when you send email using the SendTemplatedEmail or SendBulkTemplatedEmail operations.
            SubjectPart (string) --The subject line of the email.
            TextPart (string) --The email body that will be visible to recipients whose email clients do not display HTML.
            HtmlPart (string) --The HTML body of the email.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_configuration_set(ConfigurationSetName=None):
    """
    Deletes a configuration set. Configuration sets enable you to publish email sending events. For information about using configuration sets, see the Amazon SES Developer Guide .
    You can execute this operation no more than once per second.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_configuration_set(
        ConfigurationSetName='string'
    )
    
    
    :type ConfigurationSetName: string
    :param ConfigurationSetName: [REQUIRED]
            The name of the configuration set to delete.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_configuration_set_event_destination(ConfigurationSetName=None, EventDestinationName=None):
    """
    Deletes a configuration set event destination. Configuration set event destinations are associated with configuration sets, which enable you to publish email sending events. For information about using configuration sets, see the Amazon SES Developer Guide .
    You can execute this operation no more than once per second.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_configuration_set_event_destination(
        ConfigurationSetName='string',
        EventDestinationName='string'
    )
    
    
    :type ConfigurationSetName: string
    :param ConfigurationSetName: [REQUIRED]
            The name of the configuration set from which to delete the event destination.
            

    :type EventDestinationName: string
    :param EventDestinationName: [REQUIRED]
            The name of the event destination to delete.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_configuration_set_tracking_options(ConfigurationSetName=None):
    """
    Deletes an association between a configuration set and a custom domain for open and click event tracking.
    By default, images and links used for tracking open and click events are hosted on domains operated by Amazon SES. You can configure a subdomain of your own to handle these events. For information about using configuration sets, see Configuring Custom Domains to Handle Open and Click Tracking in the Amazon SES Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.delete_configuration_set_tracking_options(
        ConfigurationSetName='string'
    )
    
    
    :type ConfigurationSetName: string
    :param ConfigurationSetName: [REQUIRED]
            The name of the configuration set from which you want to delete the tracking options.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_custom_verification_email_template(TemplateName=None):
    """
    Deletes an existing custom verification email template.
    For more information about custom verification email templates, see Using Custom Verification Email Templates in the Amazon SES Developer Guide .
    You can execute this operation no more than once per second.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_custom_verification_email_template(
        TemplateName='string'
    )
    
    
    :type TemplateName: string
    :param TemplateName: [REQUIRED]
            The name of the custom verification email template that you want to delete.
            

    """
    pass

def delete_identity(Identity=None):
    """
    Deletes the specified identity (an email address or a domain) from the list of verified identities.
    You can execute this operation no more than once per second.
    See also: AWS API Documentation
    
    Examples
    The following example deletes an identity from the list of identities that have been submitted for verification with Amazon SES:
    Expected Output:
    
    :example: response = client.delete_identity(
        Identity='string'
    )
    
    
    :type Identity: string
    :param Identity: [REQUIRED]
            The identity to be removed from the list of identities for the AWS Account.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_identity_policy(Identity=None, PolicyName=None):
    """
    Deletes the specified sending authorization policy for the given identity (an email address or a domain). This API returns successfully even if a policy with the specified name does not exist.
    Sending authorization is a feature that enables an identity owner to authorize other senders to use its identities. For information about using sending authorization, see the Amazon SES Developer Guide .
    You can execute this operation no more than once per second.
    See also: AWS API Documentation
    
    Examples
    The following example deletes a sending authorization policy for an identity:
    Expected Output:
    
    :example: response = client.delete_identity_policy(
        Identity='string',
        PolicyName='string'
    )
    
    
    :type Identity: string
    :param Identity: [REQUIRED]
            The identity that is associated with the policy that you want to delete. You can specify the identity by using its name or by using its Amazon Resource Name (ARN). Examples: user@example.com , example.com , arn:aws:ses:us-east-1:123456789012:identity/example.com .
            To successfully call this API, you must own the identity.
            

    :type PolicyName: string
    :param PolicyName: [REQUIRED]
            The name of the policy to be deleted.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_receipt_filter(FilterName=None):
    """
    Deletes the specified IP address filter.
    For information about managing IP address filters, see the Amazon SES Developer Guide .
    You can execute this operation no more than once per second.
    See also: AWS API Documentation
    
    Examples
    The following example deletes an IP address filter:
    Expected Output:
    
    :example: response = client.delete_receipt_filter(
        FilterName='string'
    )
    
    
    :type FilterName: string
    :param FilterName: [REQUIRED]
            The name of the IP address filter to delete.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_receipt_rule(RuleSetName=None, RuleName=None):
    """
    Deletes the specified receipt rule.
    For information about managing receipt rules, see the Amazon SES Developer Guide .
    You can execute this operation no more than once per second.
    See also: AWS API Documentation
    
    Examples
    The following example deletes a receipt rule:
    Expected Output:
    
    :example: response = client.delete_receipt_rule(
        RuleSetName='string',
        RuleName='string'
    )
    
    
    :type RuleSetName: string
    :param RuleSetName: [REQUIRED]
            The name of the receipt rule set that contains the receipt rule to delete.
            

    :type RuleName: string
    :param RuleName: [REQUIRED]
            The name of the receipt rule to delete.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_receipt_rule_set(RuleSetName=None):
    """
    Deletes the specified receipt rule set and all of the receipt rules it contains.
    For information about managing receipt rule sets, see the Amazon SES Developer Guide .
    You can execute this operation no more than once per second.
    See also: AWS API Documentation
    
    Examples
    The following example deletes a receipt rule set:
    Expected Output:
    
    :example: response = client.delete_receipt_rule_set(
        RuleSetName='string'
    )
    
    
    :type RuleSetName: string
    :param RuleSetName: [REQUIRED]
            The name of the receipt rule set to delete.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_template(TemplateName=None):
    """
    Deletes an email template.
    You can execute this operation no more than once per second.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_template(
        TemplateName='string'
    )
    
    
    :type TemplateName: string
    :param TemplateName: [REQUIRED]
            The name of the template to be deleted.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_verified_email_address(EmailAddress=None):
    """
    Deprecated. Use the DeleteIdentity operation to delete email addresses and domains.
    See also: AWS API Documentation
    
    Examples
    The following example deletes an email address from the list of identities that have been submitted for verification with Amazon SES:
    Expected Output:
    
    :example: response = client.delete_verified_email_address(
        EmailAddress='string'
    )
    
    
    :type EmailAddress: string
    :param EmailAddress: [REQUIRED]
            An email address to be removed from the list of verified addresses.
            

    :return: response = client.delete_verified_email_address(
        EmailAddress='user@example.com',
    )
    
    print(response)
    
    
    """
    pass

def describe_active_receipt_rule_set():
    """
    Returns the metadata and receipt rules for the receipt rule set that is currently active.
    For information about setting up receipt rule sets, see the Amazon SES Developer Guide .
    You can execute this operation no more than once per second.
    See also: AWS API Documentation
    
    Examples
    The following example returns the metadata and receipt rules for the receipt rule set that is currently active:
    Expected Output:
    
    :example: response = client.describe_active_receipt_rule_set()
    
    
    :rtype: dict
    :return: {
        'Metadata': {
            'Name': 'string',
            'CreatedTimestamp': datetime(2015, 1, 1)
        },
        'Rules': [
            {
                'Name': 'string',
                'Enabled': True|False,
                'TlsPolicy': 'Require'|'Optional',
                'Recipients': [
                    'string',
                ],
                'Actions': [
                    {
                        'S3Action': {
                            'TopicArn': 'string',
                            'BucketName': 'string',
                            'ObjectKeyPrefix': 'string',
                            'KmsKeyArn': 'string'
                        },
                        'BounceAction': {
                            'TopicArn': 'string',
                            'SmtpReplyCode': 'string',
                            'StatusCode': 'string',
                            'Message': 'string',
                            'Sender': 'string'
                        },
                        'WorkmailAction': {
                            'TopicArn': 'string',
                            'OrganizationArn': 'string'
                        },
                        'LambdaAction': {
                            'TopicArn': 'string',
                            'FunctionArn': 'string',
                            'InvocationType': 'Event'|'RequestResponse'
                        },
                        'StopAction': {
                            'Scope': 'RuleSet',
                            'TopicArn': 'string'
                        },
                        'AddHeaderAction': {
                            'HeaderName': 'string',
                            'HeaderValue': 'string'
                        },
                        'SNSAction': {
                            'TopicArn': 'string',
                            'Encoding': 'UTF-8'|'Base64'
                        }
                    },
                ],
                'ScanEnabled': True|False
            },
        ]
    }
    
    
    :returns: 
    This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
    Start and end with a letter or number.
    Contain less than 64 characters.
    
    """
    pass

def describe_configuration_set(ConfigurationSetName=None, ConfigurationSetAttributeNames=None):
    """
    Returns the details of the specified configuration set. For information about using configuration sets, see the Amazon SES Developer Guide .
    You can execute this operation no more than once per second.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_configuration_set(
        ConfigurationSetName='string',
        ConfigurationSetAttributeNames=[
            'eventDestinations'|'trackingOptions'|'reputationOptions',
        ]
    )
    
    
    :type ConfigurationSetName: string
    :param ConfigurationSetName: [REQUIRED]
            The name of the configuration set to describe.
            

    :type ConfigurationSetAttributeNames: list
    :param ConfigurationSetAttributeNames: A list of configuration set attributes to return.
            (string) --
            

    :rtype: dict
    :return: {
        'ConfigurationSet': {
            'Name': 'string'
        },
        'EventDestinations': [
            {
                'Name': 'string',
                'Enabled': True|False,
                'MatchingEventTypes': [
                    'send'|'reject'|'bounce'|'complaint'|'delivery'|'open'|'click'|'renderingFailure',
                ],
                'KinesisFirehoseDestination': {
                    'IAMRoleARN': 'string',
                    'DeliveryStreamARN': 'string'
                },
                'CloudWatchDestination': {
                    'DimensionConfigurations': [
                        {
                            'DimensionName': 'string',
                            'DimensionValueSource': 'messageTag'|'emailHeader'|'linkTag',
                            'DefaultDimensionValue': 'string'
                        },
                    ]
                },
                'SNSDestination': {
                    'TopicARN': 'string'
                }
            },
        ],
        'TrackingOptions': {
            'CustomRedirectDomain': 'string'
        },
        'ReputationOptions': {
            'SendingEnabled': True|False,
            'ReputationMetricsEnabled': True|False,
            'LastFreshStart': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    Contain only letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
    Contain 64 characters or fewer.
    
    """
    pass

def describe_receipt_rule(RuleSetName=None, RuleName=None):
    """
    Returns the details of the specified receipt rule.
    For information about setting up receipt rules, see the Amazon SES Developer Guide .
    You can execute this operation no more than once per second.
    See also: AWS API Documentation
    
    Examples
    The following example returns the details of a receipt rule:
    Expected Output:
    
    :example: response = client.describe_receipt_rule(
        RuleSetName='string',
        RuleName='string'
    )
    
    
    :type RuleSetName: string
    :param RuleSetName: [REQUIRED]
            The name of the receipt rule set that the receipt rule belongs to.
            

    :type RuleName: string
    :param RuleName: [REQUIRED]
            The name of the receipt rule.
            

    :rtype: dict
    :return: {
        'Rule': {
            'Name': 'string',
            'Enabled': True|False,
            'TlsPolicy': 'Require'|'Optional',
            'Recipients': [
                'string',
            ],
            'Actions': [
                {
                    'S3Action': {
                        'TopicArn': 'string',
                        'BucketName': 'string',
                        'ObjectKeyPrefix': 'string',
                        'KmsKeyArn': 'string'
                    },
                    'BounceAction': {
                        'TopicArn': 'string',
                        'SmtpReplyCode': 'string',
                        'StatusCode': 'string',
                        'Message': 'string',
                        'Sender': 'string'
                    },
                    'WorkmailAction': {
                        'TopicArn': 'string',
                        'OrganizationArn': 'string'
                    },
                    'LambdaAction': {
                        'TopicArn': 'string',
                        'FunctionArn': 'string',
                        'InvocationType': 'Event'|'RequestResponse'
                    },
                    'StopAction': {
                        'Scope': 'RuleSet',
                        'TopicArn': 'string'
                    },
                    'AddHeaderAction': {
                        'HeaderName': 'string',
                        'HeaderValue': 'string'
                    },
                    'SNSAction': {
                        'TopicArn': 'string',
                        'Encoding': 'UTF-8'|'Base64'
                    }
                },
            ],
            'ScanEnabled': True|False
        }
    }
    
    
    :returns: 
    This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
    Start and end with a letter or number.
    Contain less than 64 characters.
    
    """
    pass

def describe_receipt_rule_set(RuleSetName=None):
    """
    Returns the details of the specified receipt rule set.
    For information about managing receipt rule sets, see the Amazon SES Developer Guide .
    You can execute this operation no more than once per second.
    See also: AWS API Documentation
    
    Examples
    The following example returns the metadata and receipt rules of a receipt rule set:
    Expected Output:
    
    :example: response = client.describe_receipt_rule_set(
        RuleSetName='string'
    )
    
    
    :type RuleSetName: string
    :param RuleSetName: [REQUIRED]
            The name of the receipt rule set to describe.
            

    :rtype: dict
    :return: {
        'Metadata': {
            'Name': 'string',
            'CreatedTimestamp': datetime(2015, 1, 1)
        },
        'Rules': [
            {
                'Name': 'string',
                'Enabled': True|False,
                'TlsPolicy': 'Require'|'Optional',
                'Recipients': [
                    'string',
                ],
                'Actions': [
                    {
                        'S3Action': {
                            'TopicArn': 'string',
                            'BucketName': 'string',
                            'ObjectKeyPrefix': 'string',
                            'KmsKeyArn': 'string'
                        },
                        'BounceAction': {
                            'TopicArn': 'string',
                            'SmtpReplyCode': 'string',
                            'StatusCode': 'string',
                            'Message': 'string',
                            'Sender': 'string'
                        },
                        'WorkmailAction': {
                            'TopicArn': 'string',
                            'OrganizationArn': 'string'
                        },
                        'LambdaAction': {
                            'TopicArn': 'string',
                            'FunctionArn': 'string',
                            'InvocationType': 'Event'|'RequestResponse'
                        },
                        'StopAction': {
                            'Scope': 'RuleSet',
                            'TopicArn': 'string'
                        },
                        'AddHeaderAction': {
                            'HeaderName': 'string',
                            'HeaderValue': 'string'
                        },
                        'SNSAction': {
                            'TopicArn': 'string',
                            'Encoding': 'UTF-8'|'Base64'
                        }
                    },
                ],
                'ScanEnabled': True|False
            },
        ]
    }
    
    
    :returns: 
    This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
    Start and end with a letter or number.
    Contain less than 64 characters.
    
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

def get_account_sending_enabled():
    """
    Returns the email sending status of the Amazon SES account.
    You can execute this operation no more than once per second.
    See also: AWS API Documentation
    
    
    :example: response = client.get_account_sending_enabled()
    
    
    :rtype: dict
    :return: {
        'Enabled': True|False
    }
    
    
    """
    pass

def get_custom_verification_email_template(TemplateName=None):
    """
    Returns the custom email verification template for the template name you specify.
    For more information about custom verification email templates, see Using Custom Verification Email Templates in the Amazon SES Developer Guide .
    You can execute this operation no more than once per second.
    See also: AWS API Documentation
    
    
    :example: response = client.get_custom_verification_email_template(
        TemplateName='string'
    )
    
    
    :type TemplateName: string
    :param TemplateName: [REQUIRED]
            The name of the custom verification email template that you want to retrieve.
            

    :rtype: dict
    :return: {
        'TemplateName': 'string',
        'FromEmailAddress': 'string',
        'TemplateSubject': 'string',
        'TemplateContent': 'string',
        'SuccessRedirectionURL': 'string',
        'FailureRedirectionURL': 'string'
    }
    
    
    """
    pass

def get_identity_dkim_attributes(Identities=None):
    """
    Returns the current status of Easy DKIM signing for an entity. For domain name identities, this operation also returns the DKIM tokens that are required for Easy DKIM signing, and whether Amazon SES has successfully verified that these tokens have been published.
    This operation takes a list of identities as input and returns the following information for each:
    This operation is throttled at one request per second and can only get DKIM attributes for up to 100 identities at a time.
    For more information about creating DNS records using DKIM tokens, go to the Amazon SES Developer Guide .
    See also: AWS API Documentation
    
    Examples
    The following example retrieves the Amazon SES Easy DKIM attributes for a list of identities:
    Expected Output:
    
    :example: response = client.get_identity_dkim_attributes(
        Identities=[
            'string',
        ]
    )
    
    
    :type Identities: list
    :param Identities: [REQUIRED]
            A list of one or more verified identities - email addresses, domains, or both.
            (string) --
            

    :rtype: dict
    :return: {
        'DkimAttributes': {
            'string': {
                'DkimEnabled': True|False,
                'DkimVerificationStatus': 'Pending'|'Success'|'Failed'|'TemporaryFailure'|'NotStarted',
                'DkimTokens': [
                    'string',
                ]
            }
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_identity_mail_from_domain_attributes(Identities=None):
    """
    Returns the custom MAIL FROM attributes for a list of identities (email addresses : domains).
    This operation is throttled at one request per second and can only get custom MAIL FROM attributes for up to 100 identities at a time.
    See also: AWS API Documentation
    
    Examples
    The following example returns the custom MAIL FROM attributes for an identity:
    Expected Output:
    
    :example: response = client.get_identity_mail_from_domain_attributes(
        Identities=[
            'string',
        ]
    )
    
    
    :type Identities: list
    :param Identities: [REQUIRED]
            A list of one or more identities.
            (string) --
            

    :rtype: dict
    :return: {
        'MailFromDomainAttributes': {
            'string': {
                'MailFromDomain': 'string',
                'MailFromDomainStatus': 'Pending'|'Success'|'Failed'|'TemporaryFailure',
                'BehaviorOnMXFailure': 'UseDefaultValue'|'RejectMessage'
            }
        }
    }
    
    
    """
    pass

def get_identity_notification_attributes(Identities=None):
    """
    Given a list of verified identities (email addresses and/or domains), returns a structure describing identity notification attributes.
    This operation is throttled at one request per second and can only get notification attributes for up to 100 identities at a time.
    For more information about using notifications with Amazon SES, see the Amazon SES Developer Guide .
    See also: AWS API Documentation
    
    Examples
    The following example returns the notification attributes for an identity:
    Expected Output:
    
    :example: response = client.get_identity_notification_attributes(
        Identities=[
            'string',
        ]
    )
    
    
    :type Identities: list
    :param Identities: [REQUIRED]
            A list of one or more identities. You can specify an identity by using its name or by using its Amazon Resource Name (ARN). Examples: user@example.com , example.com , arn:aws:ses:us-east-1:123456789012:identity/example.com .
            (string) --
            

    :rtype: dict
    :return: {
        'NotificationAttributes': {
            'string': {
                'BounceTopic': 'string',
                'ComplaintTopic': 'string',
                'DeliveryTopic': 'string',
                'ForwardingEnabled': True|False,
                'HeadersInBounceNotificationsEnabled': True|False,
                'HeadersInComplaintNotificationsEnabled': True|False,
                'HeadersInDeliveryNotificationsEnabled': True|False
            }
        }
    }
    
    
    """
    pass

def get_identity_policies(Identity=None, PolicyNames=None):
    """
    Returns the requested sending authorization policies for the given identity (an email address or a domain). The policies are returned as a map of policy names to policy contents. You can retrieve a maximum of 20 policies at a time.
    Sending authorization is a feature that enables an identity owner to authorize other senders to use its identities. For information about using sending authorization, see the Amazon SES Developer Guide .
    You can execute this operation no more than once per second.
    See also: AWS API Documentation
    
    Examples
    The following example returns a sending authorization policy for an identity:
    Expected Output:
    
    :example: response = client.get_identity_policies(
        Identity='string',
        PolicyNames=[
            'string',
        ]
    )
    
    
    :type Identity: string
    :param Identity: [REQUIRED]
            The identity for which the policies will be retrieved. You can specify an identity by using its name or by using its Amazon Resource Name (ARN). Examples: user@example.com , example.com , arn:aws:ses:us-east-1:123456789012:identity/example.com .
            To successfully call this API, you must own the identity.
            

    :type PolicyNames: list
    :param PolicyNames: [REQUIRED]
            A list of the names of policies to be retrieved. You can retrieve a maximum of 20 policies at a time. If you do not know the names of the policies that are attached to the identity, you can use ListIdentityPolicies .
            (string) --
            

    :rtype: dict
    :return: {
        'Policies': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def get_identity_verification_attributes(Identities=None):
    """
    Given a list of identities (email addresses and/or domains), returns the verification status and (for domain identities) the verification token for each identity.
    The verification status of an email address is "Pending" until the email address owner clicks the link within the verification email that Amazon SES sent to that address. If the email address owner clicks the link within 24 hours, the verification status of the email address changes to "Success". If the link is not clicked within 24 hours, the verification status changes to "Failed." In that case, if you still want to verify the email address, you must restart the verification process from the beginning.
    For domain identities, the domain's verification status is "Pending" as Amazon SES searches for the required TXT record in the DNS settings of the domain. When Amazon SES detects the record, the domain's verification status changes to "Success". If Amazon SES is unable to detect the record within 72 hours, the domain's verification status changes to "Failed." In that case, if you still want to verify the domain, you must restart the verification process from the beginning.
    This operation is throttled at one request per second and can only get verification attributes for up to 100 identities at a time.
    See also: AWS API Documentation
    
    Examples
    The following example returns the verification status and the verification token for a domain identity:
    Expected Output:
    
    :example: response = client.get_identity_verification_attributes(
        Identities=[
            'string',
        ]
    )
    
    
    :type Identities: list
    :param Identities: [REQUIRED]
            A list of identities.
            (string) --
            

    :rtype: dict
    :return: {
        'VerificationAttributes': {
            'string': {
                'VerificationStatus': 'Pending'|'Success'|'Failed'|'TemporaryFailure'|'NotStarted',
                'VerificationToken': 'string'
            }
        }
    }
    
    
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

def get_send_quota():
    """
    Provides the sending limits for the Amazon SES account.
    You can execute this operation no more than once per second.
    See also: AWS API Documentation
    
    Examples
    The following example returns the Amazon SES sending limits for an AWS account:
    Expected Output:
    
    :example: response = client.get_send_quota()
    
    
    :rtype: dict
    :return: {
        'Max24HourSend': 123.0,
        'MaxSendRate': 123.0,
        'SentLast24Hours': 123.0
    }
    
    
    """
    pass

def get_send_statistics():
    """
    Provides sending statistics for the Amazon SES account. The result is a list of data points, representing the last two weeks of sending activity. Each data point in the list contains statistics for a 15-minute period of time.
    You can execute this operation no more than once per second.
    See also: AWS API Documentation
    
    Examples
    The following example returns Amazon SES sending statistics:
    Expected Output:
    
    :example: response = client.get_send_statistics()
    
    
    :rtype: dict
    :return: {
        'SendDataPoints': [
            {
                'Timestamp': datetime(2015, 1, 1),
                'DeliveryAttempts': 123,
                'Bounces': 123,
                'Complaints': 123,
                'Rejects': 123
            },
        ]
    }
    
    
    """
    pass

def get_template(TemplateName=None):
    """
    Displays the template object (which includes the Subject line, HTML part and text part) for the template you specify.
    You can execute this operation no more than once per second.
    See also: AWS API Documentation
    
    
    :example: response = client.get_template(
        TemplateName='string'
    )
    
    
    :type TemplateName: string
    :param TemplateName: [REQUIRED]
            The name of the template you want to retrieve.
            

    :rtype: dict
    :return: {
        'Template': {
            'TemplateName': 'string',
            'SubjectPart': 'string',
            'TextPart': 'string',
            'HtmlPart': 'string'
        }
    }
    
    
    """
    pass

def get_waiter():
    """
    
    """
    pass

def list_configuration_sets(NextToken=None, MaxItems=None):
    """
    Provides a list of the configuration sets associated with your Amazon SES account. For information about using configuration sets, see Monitoring Your Amazon SES Sending Activity in the Amazon SES Developer Guide.
    You can execute this operation no more than once per second. This operation will return up to 1,000 configuration sets each time it is run. If your Amazon SES account has more than 1,000 configuration sets, this operation will also return a NextToken element. You can then execute the ListConfigurationSets operation again, passing the NextToken parameter and the value of the NextToken element to retrieve additional results.
    See also: AWS API Documentation
    
    
    :example: response = client.list_configuration_sets(
        NextToken='string',
        MaxItems=123
    )
    
    
    :type NextToken: string
    :param NextToken: A token returned from a previous call to ListConfigurationSets to indicate the position of the configuration set in the configuration set list.

    :type MaxItems: integer
    :param MaxItems: The number of configuration sets to return.

    :rtype: dict
    :return: {
        'ConfigurationSets': [
            {
                'Name': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Contain only letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
    Contain 64 characters or fewer.
    
    """
    pass

def list_custom_verification_email_templates(NextToken=None, MaxResults=None):
    """
    Lists the existing custom verification email templates for your account.
    For more information about custom verification email templates, see Using Custom Verification Email Templates in the Amazon SES Developer Guide .
    You can execute this operation no more than once per second.
    See also: AWS API Documentation
    
    
    :example: response = client.list_custom_verification_email_templates(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: An array the contains the name and creation time stamp for each template in your Amazon SES account.

    :type MaxResults: integer
    :param MaxResults: The maximum number of custom verification email templates to return. This value must be at least 1 and less than or equal to 50. If you do not specify a value, or if you specify a value less than 1 or greater than 50, the operation will return up to 50 results.

    :rtype: dict
    :return: {
        'CustomVerificationEmailTemplates': [
            {
                'TemplateName': 'string',
                'FromEmailAddress': 'string',
                'TemplateSubject': 'string',
                'SuccessRedirectionURL': 'string',
                'FailureRedirectionURL': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_identities(IdentityType=None, NextToken=None, MaxItems=None):
    """
    Returns a list containing all of the identities (email addresses and domains) for your AWS account, regardless of verification status.
    You can execute this operation no more than once per second.
    See also: AWS API Documentation
    
    Examples
    The following example lists the email address identities that have been submitted for verification with Amazon SES:
    Expected Output:
    
    :example: response = client.list_identities(
        IdentityType='EmailAddress'|'Domain',
        NextToken='string',
        MaxItems=123
    )
    
    
    :type IdentityType: string
    :param IdentityType: The type of the identities to list. Possible values are 'EmailAddress' and 'Domain'. If this parameter is omitted, then all identities will be listed.

    :type NextToken: string
    :param NextToken: The token to use for pagination.

    :type MaxItems: integer
    :param MaxItems: The maximum number of identities per page. Possible values are 1-1000 inclusive.

    :rtype: dict
    :return: {
        'Identities': [
            'string',
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_identity_policies(Identity=None):
    """
    Returns a list of sending authorization policies that are attached to the given identity (an email address or a domain). This API returns only a list. If you want the actual policy content, you can use GetIdentityPolicies .
    Sending authorization is a feature that enables an identity owner to authorize other senders to use its identities. For information about using sending authorization, see the Amazon SES Developer Guide .
    You can execute this operation no more than once per second.
    See also: AWS API Documentation
    
    Examples
    The following example returns a list of sending authorization policies that are attached to an identity:
    Expected Output:
    
    :example: response = client.list_identity_policies(
        Identity='string'
    )
    
    
    :type Identity: string
    :param Identity: [REQUIRED]
            The identity that is associated with the policy for which the policies will be listed. You can specify an identity by using its name or by using its Amazon Resource Name (ARN). Examples: user@example.com , example.com , arn:aws:ses:us-east-1:123456789012:identity/example.com .
            To successfully call this API, you must own the identity.
            

    :rtype: dict
    :return: {
        'PolicyNames': [
            'string',
        ]
    }
    
    
    """
    pass

def list_receipt_filters():
    """
    Lists the IP address filters associated with your AWS account.
    For information about managing IP address filters, see the Amazon SES Developer Guide .
    You can execute this operation no more than once per second.
    See also: AWS API Documentation
    
    Examples
    The following example lists the IP address filters that are associated with an AWS account:
    Expected Output:
    
    :example: response = client.list_receipt_filters()
    
    
    :rtype: dict
    :return: {
        'Filters': [
            {
                'Name': 'string',
                'IpFilter': {
                    'Policy': 'Block'|'Allow',
                    'Cidr': 'string'
                }
            },
        ]
    }
    
    
    """
    pass

def list_receipt_rule_sets(NextToken=None):
    """
    Lists the receipt rule sets that exist under your AWS account. If there are additional receipt rule sets to be retrieved, you will receive a NextToken that you can provide to the next call to ListReceiptRuleSets to retrieve the additional entries.
    For information about managing receipt rule sets, see the Amazon SES Developer Guide .
    You can execute this operation no more than once per second.
    See also: AWS API Documentation
    
    Examples
    The following example lists the receipt rule sets that exist under an AWS account:
    Expected Output:
    
    :example: response = client.list_receipt_rule_sets(
        NextToken='string'
    )
    
    
    :type NextToken: string
    :param NextToken: A token returned from a previous call to ListReceiptRuleSets to indicate the position in the receipt rule set list.

    :rtype: dict
    :return: {
        'RuleSets': [
            {
                'Name': 'string',
                'CreatedTimestamp': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_templates(NextToken=None, MaxItems=None):
    """
    Lists the email templates present in your Amazon SES account.
    You can execute this operation no more than once per second.
    See also: AWS API Documentation
    
    
    :example: response = client.list_templates(
        NextToken='string',
        MaxItems=123
    )
    
    
    :type NextToken: string
    :param NextToken: A token returned from a previous call to ListTemplates to indicate the position in the list of email templates.

    :type MaxItems: integer
    :param MaxItems: The maximum number of templates to return. This value must be at least 1 and less than or equal to 10. If you do not specify a value, or if you specify a value less than 1 or greater than 10, the operation will return up to 10 results.

    :rtype: dict
    :return: {
        'TemplatesMetadata': [
            {
                'Name': 'string',
                'CreatedTimestamp': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_verified_email_addresses():
    """
    Deprecated. Use the ListIdentities operation to list the email addresses and domains associated with your account.
    See also: AWS API Documentation
    
    Examples
    The following example lists all email addresses that have been submitted for verification with Amazon SES:
    Expected Output:
    
    :example: response = client.list_verified_email_addresses()
    
    
    :rtype: dict
    :return: {
        'VerifiedEmailAddresses': [
            'string',
        ]
    }
    
    
    """
    pass

def put_identity_policy(Identity=None, PolicyName=None, Policy=None):
    """
    Adds or updates a sending authorization policy for the specified identity (an email address or a domain).
    Sending authorization is a feature that enables an identity owner to authorize other senders to use its identities. For information about using sending authorization, see the Amazon SES Developer Guide .
    You can execute this operation no more than once per second.
    See also: AWS API Documentation
    
    Examples
    The following example adds a sending authorization policy to an identity:
    Expected Output:
    
    :example: response = client.put_identity_policy(
        Identity='string',
        PolicyName='string',
        Policy='string'
    )
    
    
    :type Identity: string
    :param Identity: [REQUIRED]
            The identity that the policy will apply to. You can specify an identity by using its name or by using its Amazon Resource Name (ARN). Examples: user@example.com , example.com , arn:aws:ses:us-east-1:123456789012:identity/example.com .
            To successfully call this API, you must own the identity.
            

    :type PolicyName: string
    :param PolicyName: [REQUIRED]
            The name of the policy.
            The policy name cannot exceed 64 characters and can only include alphanumeric characters, dashes, and underscores.
            

    :type Policy: string
    :param Policy: [REQUIRED]
            The text of the policy in JSON format. The policy cannot exceed 4 KB.
            For information about the syntax of sending authorization policies, see the Amazon SES Developer Guide .
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def reorder_receipt_rule_set(RuleSetName=None, RuleNames=None):
    """
    Reorders the receipt rules within a receipt rule set.
    For information about managing receipt rule sets, see the Amazon SES Developer Guide .
    You can execute this operation no more than once per second.
    See also: AWS API Documentation
    
    Examples
    The following example reorders the receipt rules within a receipt rule set:
    Expected Output:
    
    :example: response = client.reorder_receipt_rule_set(
        RuleSetName='string',
        RuleNames=[
            'string',
        ]
    )
    
    
    :type RuleSetName: string
    :param RuleSetName: [REQUIRED]
            The name of the receipt rule set to reorder.
            

    :type RuleNames: list
    :param RuleNames: [REQUIRED]
            A list of the specified receipt rule set's receipt rules in the order that you want to put them.
            (string) --
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def send_bounce(OriginalMessageId=None, BounceSender=None, Explanation=None, MessageDsn=None, BouncedRecipientInfoList=None, BounceSenderArn=None):
    """
    Generates and sends a bounce message to the sender of an email you received through Amazon SES. You can only use this API on an email up to 24 hours after you receive it.
    For information about receiving email through Amazon SES, see the Amazon SES Developer Guide .
    You can execute this operation no more than once per second.
    See also: AWS API Documentation
    
    
    :example: response = client.send_bounce(
        OriginalMessageId='string',
        BounceSender='string',
        Explanation='string',
        MessageDsn={
            'ReportingMta': 'string',
            'ArrivalDate': datetime(2015, 1, 1),
            'ExtensionFields': [
                {
                    'Name': 'string',
                    'Value': 'string'
                },
            ]
        },
        BouncedRecipientInfoList=[
            {
                'Recipient': 'string',
                'RecipientArn': 'string',
                'BounceType': 'DoesNotExist'|'MessageTooLarge'|'ExceededQuota'|'ContentRejected'|'Undefined'|'TemporaryFailure',
                'RecipientDsnFields': {
                    'FinalRecipient': 'string',
                    'Action': 'failed'|'delayed'|'delivered'|'relayed'|'expanded',
                    'RemoteMta': 'string',
                    'Status': 'string',
                    'DiagnosticCode': 'string',
                    'LastAttemptDate': datetime(2015, 1, 1),
                    'ExtensionFields': [
                        {
                            'Name': 'string',
                            'Value': 'string'
                        },
                    ]
                }
            },
        ],
        BounceSenderArn='string'
    )
    
    
    :type OriginalMessageId: string
    :param OriginalMessageId: [REQUIRED]
            The message ID of the message to be bounced.
            

    :type BounceSender: string
    :param BounceSender: [REQUIRED]
            The address to use in the 'From' header of the bounce message. This must be an identity that you have verified with Amazon SES.
            

    :type Explanation: string
    :param Explanation: Human-readable text for the bounce message to explain the failure. If not specified, the text will be auto-generated based on the bounced recipient information.

    :type MessageDsn: dict
    :param MessageDsn: Message-related DSN fields. If not specified, Amazon SES will choose the values.
            ReportingMta (string) -- [REQUIRED]The reporting MTA that attempted to deliver the message, formatted as specified in RFC 3464 (mta-name-type; mta-name ). The default value is dns; inbound-smtp.[region].amazonaws.com .
            ArrivalDate (datetime) --When the message was received by the reporting mail transfer agent (MTA), in RFC 822 date-time format.
            ExtensionFields (list) --Additional X-headers to include in the DSN.
            (dict) --Additional X-headers to include in the Delivery Status Notification (DSN) when an email that Amazon SES receives on your behalf bounces.
            For information about receiving email through Amazon SES, see the Amazon SES Developer Guide .
            Name (string) -- [REQUIRED]The name of the header to add. Must be between 1 and 50 characters, inclusive, and consist of alphanumeric (a-z, A-Z, 0-9) characters and dashes only.
            Value (string) -- [REQUIRED]The value of the header to add. Must be less than 2048 characters, and must not contain newline characters ('r' or 'n').
            
            

    :type BouncedRecipientInfoList: list
    :param BouncedRecipientInfoList: [REQUIRED]
            A list of recipients of the bounced message, including the information required to create the Delivery Status Notifications (DSNs) for the recipients. You must specify at least one BouncedRecipientInfo in the list.
            (dict) --Recipient-related information to include in the Delivery Status Notification (DSN) when an email that Amazon SES receives on your behalf bounces.
            For information about receiving email through Amazon SES, see the Amazon SES Developer Guide .
            Recipient (string) -- [REQUIRED]The email address of the recipient of the bounced email.
            RecipientArn (string) --This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to receive email for the recipient of the bounced email. For more information about sending authorization, see the Amazon SES Developer Guide .
            BounceType (string) --The reason for the bounce. You must provide either this parameter or RecipientDsnFields .
            RecipientDsnFields (dict) --Recipient-related DSN fields, most of which would normally be filled in automatically when provided with a BounceType . You must provide either this parameter or BounceType .
            FinalRecipient (string) --The email address that the message was ultimately delivered to. This corresponds to the Final-Recipient in the DSN. If not specified, FinalRecipient will be set to the Recipient specified in the BouncedRecipientInfo structure. Either FinalRecipient or the recipient in BouncedRecipientInfo must be a recipient of the original bounced message.
            Note
            Do not prepend the FinalRecipient email address with rfc 822; , as described in RFC 3798 .
            Action (string) -- [REQUIRED]The action performed by the reporting mail transfer agent (MTA) as a result of its attempt to deliver the message to the recipient address. This is required by RFC 3464 .
            RemoteMta (string) --The MTA to which the remote MTA attempted to deliver the message, formatted as specified in RFC 3464 (mta-name-type; mta-name ). This parameter typically applies only to propagating synchronous bounces.
            Status (string) -- [REQUIRED]The status code that indicates what went wrong. This is required by RFC 3464 .
            DiagnosticCode (string) --An extended explanation of what went wrong; this is usually an SMTP response. See RFC 3463 for the correct formatting of this parameter.
            LastAttemptDate (datetime) --The time the final delivery attempt was made, in RFC 822 date-time format.
            ExtensionFields (list) --Additional X-headers to include in the DSN.
            (dict) --Additional X-headers to include in the Delivery Status Notification (DSN) when an email that Amazon SES receives on your behalf bounces.
            For information about receiving email through Amazon SES, see the Amazon SES Developer Guide .
            Name (string) -- [REQUIRED]The name of the header to add. Must be between 1 and 50 characters, inclusive, and consist of alphanumeric (a-z, A-Z, 0-9) characters and dashes only.
            Value (string) -- [REQUIRED]The value of the header to add. Must be less than 2048 characters, and must not contain newline characters ('r' or 'n').
            
            
            

    :type BounceSenderArn: string
    :param BounceSenderArn: This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the address in the 'From' header of the bounce. For more information about sending authorization, see the Amazon SES Developer Guide .

    :rtype: dict
    :return: {
        'MessageId': 'string'
    }
    
    
    """
    pass

def send_bulk_templated_email(Source=None, SourceArn=None, ReplyToAddresses=None, ReturnPath=None, ReturnPathArn=None, ConfigurationSetName=None, DefaultTags=None, Template=None, TemplateArn=None, DefaultTemplateData=None, Destinations=None):
    """
    Composes an email message to multiple destinations. The message body is created using an email template.
    In order to send email using the SendBulkTemplatedEmail operation, your call to the API must meet the following requirements:
    See also: AWS API Documentation
    
    
    :example: response = client.send_bulk_templated_email(
        Source='string',
        SourceArn='string',
        ReplyToAddresses=[
            'string',
        ],
        ReturnPath='string',
        ReturnPathArn='string',
        ConfigurationSetName='string',
        DefaultTags=[
            {
                'Name': 'string',
                'Value': 'string'
            },
        ],
        Template='string',
        TemplateArn='string',
        DefaultTemplateData='string',
        Destinations=[
            {
                'Destination': {
                    'ToAddresses': [
                        'string',
                    ],
                    'CcAddresses': [
                        'string',
                    ],
                    'BccAddresses': [
                        'string',
                    ]
                },
                'ReplacementTags': [
                    {
                        'Name': 'string',
                        'Value': 'string'
                    },
                ],
                'ReplacementTemplateData': 'string'
            },
        ]
    )
    
    
    :type Source: string
    :param Source: [REQUIRED]
            The email address that is sending the email. This email address must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES. For information about verifying identities, see the Amazon SES Developer Guide .
            If you are sending on behalf of another user and have been permitted to do so by a sending authorization policy, then you must also specify the SourceArn parameter. For more information about sending authorization, see the Amazon SES Developer Guide .
            Note
            Amazon SES does not support the SMTPUTF8 extension, as described in RFC6531 . For this reason, the local part of a source email address (the part of the email address that precedes the @ sign) may only contain 7-bit ASCII characters . If the domain part of an address (the part after the @ sign) contains non-ASCII characters, they must be encoded using Punycode, as described in RFC3492 . The sender name (also known as the friendly name ) may contain non-ASCII characters. These characters must be encoded using MIME encoded-word syntax, as described in RFC 2047 . MIME encoded-word syntax uses the following form: =?charset?encoding?encoded-text?= .
            

    :type SourceArn: string
    :param SourceArn: This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to send for the email address specified in the Source parameter.
            For example, if the owner of example.com (which has ARN arn:aws:ses:us-east-1:123456789012:identity/example.com ) attaches a policy to it that authorizes you to send from user@example.com , then you would specify the SourceArn to be arn:aws:ses:us-east-1:123456789012:identity/example.com , and the Source to be user@example.com .
            For more information about sending authorization, see the Amazon SES Developer Guide .
            

    :type ReplyToAddresses: list
    :param ReplyToAddresses: The reply-to email address(es) for the message. If the recipient replies to the message, each reply-to address will receive the reply.
            (string) --
            

    :type ReturnPath: string
    :param ReturnPath: The email address that bounces and complaints will be forwarded to when feedback forwarding is enabled. If the message cannot be delivered to the recipient, then an error message will be returned from the recipient's ISP; this message will then be forwarded to the email address specified by the ReturnPath parameter. The ReturnPath parameter is never overwritten. This email address must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES.

    :type ReturnPathArn: string
    :param ReturnPathArn: This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the email address specified in the ReturnPath parameter.
            For example, if the owner of example.com (which has ARN arn:aws:ses:us-east-1:123456789012:identity/example.com ) attaches a policy to it that authorizes you to use feedback@example.com , then you would specify the ReturnPathArn to be arn:aws:ses:us-east-1:123456789012:identity/example.com , and the ReturnPath to be feedback@example.com .
            For more information about sending authorization, see the Amazon SES Developer Guide .
            

    :type ConfigurationSetName: string
    :param ConfigurationSetName: The name of the configuration set to use when you send an email using SendBulkTemplatedEmail .

    :type DefaultTags: list
    :param DefaultTags: A list of tags, in the form of name/value pairs, to apply to an email that you send to a destination using SendBulkTemplatedEmail .
            (dict) --Contains the name and value of a tag that you can provide to SendEmail or SendRawEmail to apply to an email.
            Message tags, which you use with configuration sets, enable you to publish email sending events. For information about using configuration sets, see the Amazon SES Developer Guide .
            Name (string) -- [REQUIRED]The name of the tag. The name must:
            This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
            Contain less than 256 characters.
            Value (string) -- [REQUIRED]The value of the tag. The value must:
            This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
            Contain less than 256 characters.
            
            

    :type Template: string
    :param Template: [REQUIRED]
            The template to use when sending this email.
            

    :type TemplateArn: string
    :param TemplateArn: The ARN of the template to use when sending this email.

    :type DefaultTemplateData: string
    :param DefaultTemplateData: A list of replacement values to apply to the template when replacement data is not specified in a Destination object. These values act as a default or fallback option when no other data is available.
            The template data is a JSON object, typically consisting of key-value pairs in which the keys correspond to replacement tags in the email template.
            

    :type Destinations: list
    :param Destinations: [REQUIRED]
            One or more Destination objects. All of the recipients in a Destination will receive the same version of the email. You can specify up to 50 Destination objects within a Destinations array.
            (dict) --An array that contains one or more Destinations, as well as the tags and replacement data associated with each of those Destinations.
            Destination (dict) -- [REQUIRED]Represents the destination of the message, consisting of To:, CC:, and BCC: fields.
            Note
            Amazon SES does not support the SMTPUTF8 extension, as described in RFC6531 . For this reason, the local part of a destination email address (the part of the email address that precedes the @ sign) may only contain 7-bit ASCII characters . If the domain part of an address (the part after the @ sign) contains non-ASCII characters, they must be encoded using Punycode, as described in RFC3492 .
            ToAddresses (list) --The To: field(s) of the message.
            (string) --
            CcAddresses (list) --The CC: field(s) of the message.
            (string) --
            BccAddresses (list) --The BCC: field(s) of the message.
            (string) --
            
            ReplacementTags (list) --A list of tags, in the form of name/value pairs, to apply to an email that you send using SendBulkTemplatedEmail . Tags correspond to characteristics of the email that you define, so that you can publish email sending events.
            (dict) --Contains the name and value of a tag that you can provide to SendEmail or SendRawEmail to apply to an email.
            Message tags, which you use with configuration sets, enable you to publish email sending events. For information about using configuration sets, see the Amazon SES Developer Guide .
            Name (string) -- [REQUIRED]The name of the tag. The name must:
            This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
            Contain less than 256 characters.
            Value (string) -- [REQUIRED]The value of the tag. The value must:
            This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
            Contain less than 256 characters.
            
            ReplacementTemplateData (string) --A list of replacement values to apply to the template. This parameter is a JSON object, typically consisting of key-value pairs in which the keys correspond to replacement tags in the email template.
            
            

    :rtype: dict
    :return: {
        'Status': [
            {
                'Status': 'Success'|'MessageRejected'|'MailFromDomainNotVerified'|'ConfigurationSetDoesNotExist'|'TemplateDoesNotExist'|'AccountSuspended'|'AccountThrottled'|'AccountDailyQuotaExceeded'|'InvalidSendingPoolName'|'AccountSendingPaused'|'ConfigurationSetSendingPaused'|'InvalidParameterValue'|'TransientFailure'|'Failed',
                'Error': 'string',
                'MessageId': 'string'
            },
        ]
    }
    
    
    :returns: 
    Source (string) -- [REQUIRED]
    The email address that is sending the email. This email address must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES. For information about verifying identities, see the Amazon SES Developer Guide .
    If you are sending on behalf of another user and have been permitted to do so by a sending authorization policy, then you must also specify the SourceArn parameter. For more information about sending authorization, see the Amazon SES Developer Guide .
    
    Note
    Amazon SES does not support the SMTPUTF8 extension, as described in RFC6531 . For this reason, the local part of a source email address (the part of the email address that precedes the @ sign) may only contain 7-bit ASCII characters . If the domain part of an address (the part after the @ sign) contains non-ASCII characters, they must be encoded using Punycode, as described in RFC3492 . The sender name (also known as the friendly name ) may contain non-ASCII characters. These characters must be encoded using MIME encoded-word syntax, as described in RFC 2047 . MIME encoded-word syntax uses the following form: =?charset?encoding?encoded-text?= .
    
    
    SourceArn (string) -- This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to send for the email address specified in the Source parameter.
    For example, if the owner of example.com (which has ARN arn:aws:ses:us-east-1:123456789012:identity/example.com ) attaches a policy to it that authorizes you to send from user@example.com , then you would specify the SourceArn to be arn:aws:ses:us-east-1:123456789012:identity/example.com , and the Source to be user@example.com .
    For more information about sending authorization, see the Amazon SES Developer Guide .
    
    ReplyToAddresses (list) -- The reply-to email address(es) for the message. If the recipient replies to the message, each reply-to address will receive the reply.
    
    (string) --
    
    
    ReturnPath (string) -- The email address that bounces and complaints will be forwarded to when feedback forwarding is enabled. If the message cannot be delivered to the recipient, then an error message will be returned from the recipient's ISP; this message will then be forwarded to the email address specified by the ReturnPath parameter. The ReturnPath parameter is never overwritten. This email address must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES.
    ReturnPathArn (string) -- This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the email address specified in the ReturnPath parameter.
    For example, if the owner of example.com (which has ARN arn:aws:ses:us-east-1:123456789012:identity/example.com ) attaches a policy to it that authorizes you to use feedback@example.com , then you would specify the ReturnPathArn to be arn:aws:ses:us-east-1:123456789012:identity/example.com , and the ReturnPath to be feedback@example.com .
    For more information about sending authorization, see the Amazon SES Developer Guide .
    
    ConfigurationSetName (string) -- The name of the configuration set to use when you send an email using SendBulkTemplatedEmail .
    DefaultTags (list) -- A list of tags, in the form of name/value pairs, to apply to an email that you send to a destination using SendBulkTemplatedEmail .
    
    (dict) --Contains the name and value of a tag that you can provide to SendEmail or SendRawEmail to apply to an email.
    Message tags, which you use with configuration sets, enable you to publish email sending events. For information about using configuration sets, see the Amazon SES Developer Guide .
    
    Name (string) -- [REQUIRED]The name of the tag. The name must:
    
    This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
    Contain less than 256 characters.
    
    
    Value (string) -- [REQUIRED]The value of the tag. The value must:
    
    This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
    Contain less than 256 characters.
    
    
    
    
    
    
    Template (string) -- [REQUIRED]
    The template to use when sending this email.
    
    TemplateArn (string) -- The ARN of the template to use when sending this email.
    DefaultTemplateData (string) -- A list of replacement values to apply to the template when replacement data is not specified in a Destination object. These values act as a default or fallback option when no other data is available.
    The template data is a JSON object, typically consisting of key-value pairs in which the keys correspond to replacement tags in the email template.
    
    Destinations (list) -- [REQUIRED]
    One or more Destination objects. All of the recipients in a Destination will receive the same version of the email. You can specify up to 50 Destination objects within a Destinations array.
    
    (dict) --An array that contains one or more Destinations, as well as the tags and replacement data associated with each of those Destinations.
    
    Destination (dict) -- [REQUIRED]Represents the destination of the message, consisting of To:, CC:, and BCC: fields.
    
    Note
    Amazon SES does not support the SMTPUTF8 extension, as described in RFC6531 . For this reason, the local part of a destination email address (the part of the email address that precedes the @ sign) may only contain 7-bit ASCII characters . If the domain part of an address (the part after the @ sign) contains non-ASCII characters, they must be encoded using Punycode, as described in RFC3492 .
    
    
    ToAddresses (list) --The To: field(s) of the message.
    
    (string) --
    
    
    CcAddresses (list) --The CC: field(s) of the message.
    
    (string) --
    
    
    BccAddresses (list) --The BCC: field(s) of the message.
    
    (string) --
    
    
    
    
    ReplacementTags (list) --A list of tags, in the form of name/value pairs, to apply to an email that you send using SendBulkTemplatedEmail . Tags correspond to characteristics of the email that you define, so that you can publish email sending events.
    
    (dict) --Contains the name and value of a tag that you can provide to SendEmail or SendRawEmail to apply to an email.
    Message tags, which you use with configuration sets, enable you to publish email sending events. For information about using configuration sets, see the Amazon SES Developer Guide .
    
    Name (string) -- [REQUIRED]The name of the tag. The name must:
    
    This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
    Contain less than 256 characters.
    
    
    Value (string) -- [REQUIRED]The value of the tag. The value must:
    
    This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
    Contain less than 256 characters.
    
    
    
    
    
    
    ReplacementTemplateData (string) --A list of replacement values to apply to the template. This parameter is a JSON object, typically consisting of key-value pairs in which the keys correspond to replacement tags in the email template.
    
    
    
    
    
    
    """
    pass

def send_custom_verification_email(EmailAddress=None, TemplateName=None, ConfigurationSetName=None):
    """
    Adds an email address to the list of identities for your Amazon SES account and attempts to verify it. As a result of executing this operation, a customized verification email is sent to the specified address.
    To use this operation, you must first create a custom verification email template. For more information about creating and using custom verification email templates, see Using Custom Verification Email Templates in the Amazon SES Developer Guide .
    You can execute this operation no more than once per second.
    See also: AWS API Documentation
    
    
    :example: response = client.send_custom_verification_email(
        EmailAddress='string',
        TemplateName='string',
        ConfigurationSetName='string'
    )
    
    
    :type EmailAddress: string
    :param EmailAddress: [REQUIRED]
            The email address to verify.
            

    :type TemplateName: string
    :param TemplateName: [REQUIRED]
            The name of the custom verification email template to use when sending the verification email.
            

    :type ConfigurationSetName: string
    :param ConfigurationSetName: Name of a configuration set to use when sending the verification email.

    :rtype: dict
    :return: {
        'MessageId': 'string'
    }
    
    
    """
    pass

def send_email(Source=None, Destination=None, Message=None, ReplyToAddresses=None, ReturnPath=None, SourceArn=None, ReturnPathArn=None, Tags=None, ConfigurationSetName=None):
    """
    Composes an email message and immediately queues it for sending. In order to send email using the SendEmail operation, your message must meet the following requirements:
    See also: AWS API Documentation
    
    Examples
    The following example sends a formatted email:
    Expected Output:
    
    :example: response = client.send_email(
        Source='string',
        Destination={
            'ToAddresses': [
                'string',
            ],
            'CcAddresses': [
                'string',
            ],
            'BccAddresses': [
                'string',
            ]
        },
        Message={
            'Subject': {
                'Data': 'string',
                'Charset': 'string'
            },
            'Body': {
                'Text': {
                    'Data': 'string',
                    'Charset': 'string'
                },
                'Html': {
                    'Data': 'string',
                    'Charset': 'string'
                }
            }
        },
        ReplyToAddresses=[
            'string',
        ],
        ReturnPath='string',
        SourceArn='string',
        ReturnPathArn='string',
        Tags=[
            {
                'Name': 'string',
                'Value': 'string'
            },
        ],
        ConfigurationSetName='string'
    )
    
    
    :type Source: string
    :param Source: [REQUIRED]
            The email address that is sending the email. This email address must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES. For information about verifying identities, see the Amazon SES Developer Guide .
            If you are sending on behalf of another user and have been permitted to do so by a sending authorization policy, then you must also specify the SourceArn parameter. For more information about sending authorization, see the Amazon SES Developer Guide .
            Note
            Amazon SES does not support the SMTPUTF8 extension, as described in RFC6531 . For this reason, the local part of a source email address (the part of the email address that precedes the @ sign) may only contain 7-bit ASCII characters . If the domain part of an address (the part after the @ sign) contains non-ASCII characters, they must be encoded using Punycode, as described in RFC3492 . The sender name (also known as the friendly name ) may contain non-ASCII characters. These characters must be encoded using MIME encoded-word syntax, as described in RFC 2047 . MIME encoded-word syntax uses the following form: =?charset?encoding?encoded-text?= .
            

    :type Destination: dict
    :param Destination: [REQUIRED]
            The destination for this email, composed of To:, CC:, and BCC: fields.
            ToAddresses (list) --The To: field(s) of the message.
            (string) --
            CcAddresses (list) --The CC: field(s) of the message.
            (string) --
            BccAddresses (list) --The BCC: field(s) of the message.
            (string) --
            

    :type Message: dict
    :param Message: [REQUIRED]
            The message to be sent.
            Subject (dict) -- [REQUIRED]The subject of the message: A short summary of the content, which will appear in the recipient's inbox.
            Data (string) -- [REQUIRED]The textual data of the content.
            Charset (string) --The character set of the content.
            Body (dict) -- [REQUIRED]The message body.
            Text (dict) --The content of the message, in text format. Use this for text-based email clients, or clients on high-latency networks (such as mobile devices).
            Data (string) -- [REQUIRED]The textual data of the content.
            Charset (string) --The character set of the content.
            Html (dict) --The content of the message, in HTML format. Use this for email clients that can process HTML. You can include clickable links, formatted text, and much more in an HTML message.
            Data (string) -- [REQUIRED]The textual data of the content.
            Charset (string) --The character set of the content.
            
            

    :type ReplyToAddresses: list
    :param ReplyToAddresses: The reply-to email address(es) for the message. If the recipient replies to the message, each reply-to address will receive the reply.
            (string) --
            

    :type ReturnPath: string
    :param ReturnPath: The email address that bounces and complaints will be forwarded to when feedback forwarding is enabled. If the message cannot be delivered to the recipient, then an error message will be returned from the recipient's ISP; this message will then be forwarded to the email address specified by the ReturnPath parameter. The ReturnPath parameter is never overwritten. This email address must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES.

    :type SourceArn: string
    :param SourceArn: This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to send for the email address specified in the Source parameter.
            For example, if the owner of example.com (which has ARN arn:aws:ses:us-east-1:123456789012:identity/example.com ) attaches a policy to it that authorizes you to send from user@example.com , then you would specify the SourceArn to be arn:aws:ses:us-east-1:123456789012:identity/example.com , and the Source to be user@example.com .
            For more information about sending authorization, see the Amazon SES Developer Guide .
            

    :type ReturnPathArn: string
    :param ReturnPathArn: This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the email address specified in the ReturnPath parameter.
            For example, if the owner of example.com (which has ARN arn:aws:ses:us-east-1:123456789012:identity/example.com ) attaches a policy to it that authorizes you to use feedback@example.com , then you would specify the ReturnPathArn to be arn:aws:ses:us-east-1:123456789012:identity/example.com , and the ReturnPath to be feedback@example.com .
            For more information about sending authorization, see the Amazon SES Developer Guide .
            

    :type Tags: list
    :param Tags: A list of tags, in the form of name/value pairs, to apply to an email that you send using SendEmail . Tags correspond to characteristics of the email that you define, so that you can publish email sending events.
            (dict) --Contains the name and value of a tag that you can provide to SendEmail or SendRawEmail to apply to an email.
            Message tags, which you use with configuration sets, enable you to publish email sending events. For information about using configuration sets, see the Amazon SES Developer Guide .
            Name (string) -- [REQUIRED]The name of the tag. The name must:
            This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
            Contain less than 256 characters.
            Value (string) -- [REQUIRED]The value of the tag. The value must:
            This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
            Contain less than 256 characters.
            
            

    :type ConfigurationSetName: string
    :param ConfigurationSetName: The name of the configuration set to use when you send an email using SendEmail .

    :rtype: dict
    :return: {
        'MessageId': 'string'
    }
    
    
    :returns: 
    Source (string) -- [REQUIRED]
    The email address that is sending the email. This email address must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES. For information about verifying identities, see the Amazon SES Developer Guide .
    If you are sending on behalf of another user and have been permitted to do so by a sending authorization policy, then you must also specify the SourceArn parameter. For more information about sending authorization, see the Amazon SES Developer Guide .
    
    Note
    Amazon SES does not support the SMTPUTF8 extension, as described in RFC6531 . For this reason, the local part of a source email address (the part of the email address that precedes the @ sign) may only contain 7-bit ASCII characters . If the domain part of an address (the part after the @ sign) contains non-ASCII characters, they must be encoded using Punycode, as described in RFC3492 . The sender name (also known as the friendly name ) may contain non-ASCII characters. These characters must be encoded using MIME encoded-word syntax, as described in RFC 2047 . MIME encoded-word syntax uses the following form: =?charset?encoding?encoded-text?= .
    
    
    Destination (dict) -- [REQUIRED]
    The destination for this email, composed of To:, CC:, and BCC: fields.
    
    ToAddresses (list) --The To: field(s) of the message.
    
    (string) --
    
    
    CcAddresses (list) --The CC: field(s) of the message.
    
    (string) --
    
    
    BccAddresses (list) --The BCC: field(s) of the message.
    
    (string) --
    
    
    
    
    Message (dict) -- [REQUIRED]
    The message to be sent.
    
    Subject (dict) -- [REQUIRED]The subject of the message: A short summary of the content, which will appear in the recipient's inbox.
    
    Data (string) -- [REQUIRED]The textual data of the content.
    
    Charset (string) --The character set of the content.
    
    
    
    Body (dict) -- [REQUIRED]The message body.
    
    Text (dict) --The content of the message, in text format. Use this for text-based email clients, or clients on high-latency networks (such as mobile devices).
    
    Data (string) -- [REQUIRED]The textual data of the content.
    
    Charset (string) --The character set of the content.
    
    
    
    Html (dict) --The content of the message, in HTML format. Use this for email clients that can process HTML. You can include clickable links, formatted text, and much more in an HTML message.
    
    Data (string) -- [REQUIRED]The textual data of the content.
    
    Charset (string) --The character set of the content.
    
    
    
    
    
    
    
    ReplyToAddresses (list) -- The reply-to email address(es) for the message. If the recipient replies to the message, each reply-to address will receive the reply.
    
    (string) --
    
    
    ReturnPath (string) -- The email address that bounces and complaints will be forwarded to when feedback forwarding is enabled. If the message cannot be delivered to the recipient, then an error message will be returned from the recipient's ISP; this message will then be forwarded to the email address specified by the ReturnPath parameter. The ReturnPath parameter is never overwritten. This email address must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES.
    SourceArn (string) -- This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to send for the email address specified in the Source parameter.
    For example, if the owner of example.com (which has ARN arn:aws:ses:us-east-1:123456789012:identity/example.com ) attaches a policy to it that authorizes you to send from user@example.com , then you would specify the SourceArn to be arn:aws:ses:us-east-1:123456789012:identity/example.com , and the Source to be user@example.com .
    For more information about sending authorization, see the Amazon SES Developer Guide .
    
    ReturnPathArn (string) -- This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the email address specified in the ReturnPath parameter.
    For example, if the owner of example.com (which has ARN arn:aws:ses:us-east-1:123456789012:identity/example.com ) attaches a policy to it that authorizes you to use feedback@example.com , then you would specify the ReturnPathArn to be arn:aws:ses:us-east-1:123456789012:identity/example.com , and the ReturnPath to be feedback@example.com .
    For more information about sending authorization, see the Amazon SES Developer Guide .
    
    Tags (list) -- A list of tags, in the form of name/value pairs, to apply to an email that you send using SendEmail . Tags correspond to characteristics of the email that you define, so that you can publish email sending events.
    
    (dict) --Contains the name and value of a tag that you can provide to SendEmail or SendRawEmail to apply to an email.
    Message tags, which you use with configuration sets, enable you to publish email sending events. For information about using configuration sets, see the Amazon SES Developer Guide .
    
    Name (string) -- [REQUIRED]The name of the tag. The name must:
    
    This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
    Contain less than 256 characters.
    
    
    Value (string) -- [REQUIRED]The value of the tag. The value must:
    
    This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
    Contain less than 256 characters.
    
    
    
    
    
    
    ConfigurationSetName (string) -- The name of the configuration set to use when you send an email using SendEmail .
    
    """
    pass

def send_raw_email(Source=None, Destinations=None, RawMessage=None, FromArn=None, SourceArn=None, ReturnPathArn=None, Tags=None, ConfigurationSetName=None):
    """
    Composes an email message and immediately queues it for sending. When calling this operation, you may specify the message headers as well as the content. The SendRawEmail operation is particularly useful for sending multipart MIME emails (such as those that contain both a plain-text and an HTML version).
    In order to send email using the SendRawEmail operation, your message must meet the following requirements:
    Additionally, keep the following considerations in mind when using the SendRawEmail operation:
    For most common sending authorization scenarios, we recommend that you specify the SourceIdentityArn parameter and not the FromIdentityArn or ReturnPathIdentityArn parameters. If you only specify the SourceIdentityArn parameter, Amazon SES will set the From and Return Path addresses to the identity specified in SourceIdentityArn . For more information about sending authorization, see the Using Sending Authorization with Amazon SES in the Amazon SES Developer Guide.
    See also: AWS API Documentation
    
    Examples
    The following example sends an email with an attachment:
    Expected Output:
    
    :example: response = client.send_raw_email(
        Source='string',
        Destinations=[
            'string',
        ],
        RawMessage={
            'Data': b'bytes'
        },
        FromArn='string',
        SourceArn='string',
        ReturnPathArn='string',
        Tags=[
            {
                'Name': 'string',
                'Value': 'string'
            },
        ],
        ConfigurationSetName='string'
    )
    
    
    :type Source: string
    :param Source: The identity's email address. If you do not provide a value for this parameter, you must specify a 'From' address in the raw text of the message. (You can also specify both.)
            Note
            Amazon SES does not support the SMTPUTF8 extension, as described in`RFC6531 <https://tools.ietf.org/html/rfc6531>`__ . For this reason, the local part of a source email address (the part of the email address that precedes the @ sign) may only contain 7-bit ASCII characters . If the domain part of an address (the part after the @ sign) contains non-ASCII characters, they must be encoded using Punycode, as described in RFC3492 . The sender name (also known as the friendly name ) may contain non-ASCII characters. These characters must be encoded using MIME encoded-word syntax, as described in RFC 2047 . MIME encoded-word syntax uses the following form: =?charset?encoding?encoded-text?= .
            If you specify the Source parameter and have feedback forwarding enabled, then bounces and complaints will be sent to this email address. This takes precedence over any Return-Path header that you might include in the raw text of the message.
            

    :type Destinations: list
    :param Destinations: A list of destinations for the message, consisting of To:, CC:, and BCC: addresses.
            (string) --
            

    :type RawMessage: dict
    :param RawMessage: [REQUIRED]
            The raw text of the message. The client is responsible for ensuring the following:
            Message must contain a header and a body, separated by a blank line.
            All required header fields must be present.
            Each part of a multipart MIME message must be formatted properly.
            MIME content types must be among those supported by Amazon SES. For more information, go to the Amazon SES Developer Guide .
            Must be base64-encoded.
            Per RFC 5321 , the maximum length of each line of text, including the CRLF, must not exceed 1,000 characters.
            Data (bytes) -- [REQUIRED]The raw data of the message. This data needs to base64-encoded if you are accessing Amazon SES directly through the HTTPS interface. If you are accessing Amazon SES using an AWS SDK, the SDK takes care of the base 64-encoding for you. In all cases, the client must ensure that the message format complies with Internet email standards regarding email header fields, MIME types, and MIME encoding.
            The To:, CC:, and BCC: headers in the raw message can contain a group list.
            If you are using SendRawEmail with sending authorization, you can include X-headers in the raw message to specify the 'Source,' 'From,' and 'Return-Path' addresses. For more information, see the documentation for SendRawEmail .
            Warning
            Do not include these X-headers in the DKIM signature, because they are removed by Amazon SES before sending the email.
            For more information, go to the Amazon SES Developer Guide .
            

    :type FromArn: string
    :param FromArn: This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to specify a particular 'From' address in the header of the raw email.
            Instead of using this parameter, you can use the X-header X-SES-FROM-ARN in the raw message of the email. If you use both the FromArn parameter and the corresponding X-header, Amazon SES uses the value of the FromArn parameter.
            Note
            For information about when to use this parameter, see the description of SendRawEmail in this guide, or see the Amazon SES Developer Guide .
            

    :type SourceArn: string
    :param SourceArn: This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to send for the email address specified in the Source parameter.
            For example, if the owner of example.com (which has ARN arn:aws:ses:us-east-1:123456789012:identity/example.com ) attaches a policy to it that authorizes you to send from user@example.com , then you would specify the SourceArn to be arn:aws:ses:us-east-1:123456789012:identity/example.com , and the Source to be user@example.com .
            Instead of using this parameter, you can use the X-header X-SES-SOURCE-ARN in the raw message of the email. If you use both the SourceArn parameter and the corresponding X-header, Amazon SES uses the value of the SourceArn parameter.
            Note
            For information about when to use this parameter, see the description of SendRawEmail in this guide, or see the Amazon SES Developer Guide .
            

    :type ReturnPathArn: string
    :param ReturnPathArn: This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the email address specified in the ReturnPath parameter.
            For example, if the owner of example.com (which has ARN arn:aws:ses:us-east-1:123456789012:identity/example.com ) attaches a policy to it that authorizes you to use feedback@example.com , then you would specify the ReturnPathArn to be arn:aws:ses:us-east-1:123456789012:identity/example.com , and the ReturnPath to be feedback@example.com .
            Instead of using this parameter, you can use the X-header X-SES-RETURN-PATH-ARN in the raw message of the email. If you use both the ReturnPathArn parameter and the corresponding X-header, Amazon SES uses the value of the ReturnPathArn parameter.
            Note
            For information about when to use this parameter, see the description of SendRawEmail in this guide, or see the Amazon SES Developer Guide .
            

    :type Tags: list
    :param Tags: A list of tags, in the form of name/value pairs, to apply to an email that you send using SendRawEmail . Tags correspond to characteristics of the email that you define, so that you can publish email sending events.
            (dict) --Contains the name and value of a tag that you can provide to SendEmail or SendRawEmail to apply to an email.
            Message tags, which you use with configuration sets, enable you to publish email sending events. For information about using configuration sets, see the Amazon SES Developer Guide .
            Name (string) -- [REQUIRED]The name of the tag. The name must:
            This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
            Contain less than 256 characters.
            Value (string) -- [REQUIRED]The value of the tag. The value must:
            This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
            Contain less than 256 characters.
            
            

    :type ConfigurationSetName: string
    :param ConfigurationSetName: The name of the configuration set to use when you send an email using SendRawEmail .

    :rtype: dict
    :return: {
        'MessageId': 'string'
    }
    
    
    :returns: 
    Although you can customize the message headers when using the SendRawEmail operation, Amazon SES will automatically apply its own Message-ID and Date headers; if you passed these headers when creating the message, they will be overwritten by the values that Amazon SES provides.
    If you are using sending authorization to send on behalf of another user, SendRawEmail enables you to specify the cross-account identity for the email's Source, From, and Return-Path parameters in one of two ways: you can pass optional parameters SourceArn , FromArn , and/or ReturnPathArn to the API, or you can include the following X-headers in the header of your raw email:
    X-SES-SOURCE-ARN
    X-SES-FROM-ARN
    X-SES-RETURN-PATH-ARN
    
    
    
    """
    pass

def send_templated_email(Source=None, Destination=None, ReplyToAddresses=None, ReturnPath=None, SourceArn=None, ReturnPathArn=None, Tags=None, ConfigurationSetName=None, Template=None, TemplateArn=None, TemplateData=None):
    """
    Composes an email message using an email template and immediately queues it for sending.
    In order to send email using the SendTemplatedEmail operation, your call to the API must meet the following requirements:
    See also: AWS API Documentation
    
    
    :example: response = client.send_templated_email(
        Source='string',
        Destination={
            'ToAddresses': [
                'string',
            ],
            'CcAddresses': [
                'string',
            ],
            'BccAddresses': [
                'string',
            ]
        },
        ReplyToAddresses=[
            'string',
        ],
        ReturnPath='string',
        SourceArn='string',
        ReturnPathArn='string',
        Tags=[
            {
                'Name': 'string',
                'Value': 'string'
            },
        ],
        ConfigurationSetName='string',
        Template='string',
        TemplateArn='string',
        TemplateData='string'
    )
    
    
    :type Source: string
    :param Source: [REQUIRED]
            The email address that is sending the email. This email address must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES. For information about verifying identities, see the Amazon SES Developer Guide .
            If you are sending on behalf of another user and have been permitted to do so by a sending authorization policy, then you must also specify the SourceArn parameter. For more information about sending authorization, see the Amazon SES Developer Guide .
            Note
            Amazon SES does not support the SMTPUTF8 extension, as described in RFC6531 . For this reason, the local part of a source email address (the part of the email address that precedes the @ sign) may only contain 7-bit ASCII characters . If the domain part of an address (the part after the @ sign) contains non-ASCII characters, they must be encoded using Punycode, as described in RFC3492 . The sender name (also known as the friendly name ) may contain non-ASCII characters. These characters must be encoded using MIME encoded-word syntax, as described in`RFC 2047 <https://tools.ietf.org/html/rfc2047>`__ . MIME encoded-word syntax uses the following form: =?charset?encoding?encoded-text?= .
            

    :type Destination: dict
    :param Destination: [REQUIRED]
            The destination for this email, composed of To:, CC:, and BCC: fields. A Destination can include up to 50 recipients across these three fields.
            ToAddresses (list) --The To: field(s) of the message.
            (string) --
            CcAddresses (list) --The CC: field(s) of the message.
            (string) --
            BccAddresses (list) --The BCC: field(s) of the message.
            (string) --
            

    :type ReplyToAddresses: list
    :param ReplyToAddresses: The reply-to email address(es) for the message. If the recipient replies to the message, each reply-to address will receive the reply.
            (string) --
            

    :type ReturnPath: string
    :param ReturnPath: The email address that bounces and complaints will be forwarded to when feedback forwarding is enabled. If the message cannot be delivered to the recipient, then an error message will be returned from the recipient's ISP; this message will then be forwarded to the email address specified by the ReturnPath parameter. The ReturnPath parameter is never overwritten. This email address must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES.

    :type SourceArn: string
    :param SourceArn: This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to send for the email address specified in the Source parameter.
            For example, if the owner of example.com (which has ARN arn:aws:ses:us-east-1:123456789012:identity/example.com ) attaches a policy to it that authorizes you to send from user@example.com , then you would specify the SourceArn to be arn:aws:ses:us-east-1:123456789012:identity/example.com , and the Source to be user@example.com .
            For more information about sending authorization, see the Amazon SES Developer Guide .
            

    :type ReturnPathArn: string
    :param ReturnPathArn: This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the email address specified in the ReturnPath parameter.
            For example, if the owner of example.com (which has ARN arn:aws:ses:us-east-1:123456789012:identity/example.com ) attaches a policy to it that authorizes you to use feedback@example.com , then you would specify the ReturnPathArn to be arn:aws:ses:us-east-1:123456789012:identity/example.com , and the ReturnPath to be feedback@example.com .
            For more information about sending authorization, see the Amazon SES Developer Guide .
            

    :type Tags: list
    :param Tags: A list of tags, in the form of name/value pairs, to apply to an email that you send using SendTemplatedEmail . Tags correspond to characteristics of the email that you define, so that you can publish email sending events.
            (dict) --Contains the name and value of a tag that you can provide to SendEmail or SendRawEmail to apply to an email.
            Message tags, which you use with configuration sets, enable you to publish email sending events. For information about using configuration sets, see the Amazon SES Developer Guide .
            Name (string) -- [REQUIRED]The name of the tag. The name must:
            This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
            Contain less than 256 characters.
            Value (string) -- [REQUIRED]The value of the tag. The value must:
            This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
            Contain less than 256 characters.
            
            

    :type ConfigurationSetName: string
    :param ConfigurationSetName: The name of the configuration set to use when you send an email using SendTemplatedEmail .

    :type Template: string
    :param Template: [REQUIRED]
            The template to use when sending this email.
            

    :type TemplateArn: string
    :param TemplateArn: The ARN of the template to use when sending this email.

    :type TemplateData: string
    :param TemplateData: [REQUIRED]
            A list of replacement values to apply to the template. This parameter is a JSON object, typically consisting of key-value pairs in which the keys correspond to replacement tags in the email template.
            

    :rtype: dict
    :return: {
        'MessageId': 'string'
    }
    
    
    :returns: 
    Source (string) -- [REQUIRED]
    The email address that is sending the email. This email address must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES. For information about verifying identities, see the Amazon SES Developer Guide .
    If you are sending on behalf of another user and have been permitted to do so by a sending authorization policy, then you must also specify the SourceArn parameter. For more information about sending authorization, see the Amazon SES Developer Guide .
    
    Note
    Amazon SES does not support the SMTPUTF8 extension, as described in RFC6531 . For this reason, the local part of a source email address (the part of the email address that precedes the @ sign) may only contain 7-bit ASCII characters . If the domain part of an address (the part after the @ sign) contains non-ASCII characters, they must be encoded using Punycode, as described in RFC3492 . The sender name (also known as the friendly name ) may contain non-ASCII characters. These characters must be encoded using MIME encoded-word syntax, as described in`RFC 2047 <https://tools.ietf.org/html/rfc2047>`__ . MIME encoded-word syntax uses the following form: =?charset?encoding?encoded-text?= .
    
    
    Destination (dict) -- [REQUIRED]
    The destination for this email, composed of To:, CC:, and BCC: fields. A Destination can include up to 50 recipients across these three fields.
    
    ToAddresses (list) --The To: field(s) of the message.
    
    (string) --
    
    
    CcAddresses (list) --The CC: field(s) of the message.
    
    (string) --
    
    
    BccAddresses (list) --The BCC: field(s) of the message.
    
    (string) --
    
    
    
    
    ReplyToAddresses (list) -- The reply-to email address(es) for the message. If the recipient replies to the message, each reply-to address will receive the reply.
    
    (string) --
    
    
    ReturnPath (string) -- The email address that bounces and complaints will be forwarded to when feedback forwarding is enabled. If the message cannot be delivered to the recipient, then an error message will be returned from the recipient's ISP; this message will then be forwarded to the email address specified by the ReturnPath parameter. The ReturnPath parameter is never overwritten. This email address must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES.
    SourceArn (string) -- This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to send for the email address specified in the Source parameter.
    For example, if the owner of example.com (which has ARN arn:aws:ses:us-east-1:123456789012:identity/example.com ) attaches a policy to it that authorizes you to send from user@example.com , then you would specify the SourceArn to be arn:aws:ses:us-east-1:123456789012:identity/example.com , and the Source to be user@example.com .
    For more information about sending authorization, see the Amazon SES Developer Guide .
    
    ReturnPathArn (string) -- This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the email address specified in the ReturnPath parameter.
    For example, if the owner of example.com (which has ARN arn:aws:ses:us-east-1:123456789012:identity/example.com ) attaches a policy to it that authorizes you to use feedback@example.com , then you would specify the ReturnPathArn to be arn:aws:ses:us-east-1:123456789012:identity/example.com , and the ReturnPath to be feedback@example.com .
    For more information about sending authorization, see the Amazon SES Developer Guide .
    
    Tags (list) -- A list of tags, in the form of name/value pairs, to apply to an email that you send using SendTemplatedEmail . Tags correspond to characteristics of the email that you define, so that you can publish email sending events.
    
    (dict) --Contains the name and value of a tag that you can provide to SendEmail or SendRawEmail to apply to an email.
    Message tags, which you use with configuration sets, enable you to publish email sending events. For information about using configuration sets, see the Amazon SES Developer Guide .
    
    Name (string) -- [REQUIRED]The name of the tag. The name must:
    
    This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
    Contain less than 256 characters.
    
    
    Value (string) -- [REQUIRED]The value of the tag. The value must:
    
    This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
    Contain less than 256 characters.
    
    
    
    
    
    
    ConfigurationSetName (string) -- The name of the configuration set to use when you send an email using SendTemplatedEmail .
    Template (string) -- [REQUIRED]
    The template to use when sending this email.
    
    TemplateArn (string) -- The ARN of the template to use when sending this email.
    TemplateData (string) -- [REQUIRED]
    A list of replacement values to apply to the template. This parameter is a JSON object, typically consisting of key-value pairs in which the keys correspond to replacement tags in the email template.
    
    
    """
    pass

def set_active_receipt_rule_set(RuleSetName=None):
    """
    Sets the specified receipt rule set as the active receipt rule set.
    For information about managing receipt rule sets, see the Amazon SES Developer Guide .
    You can execute this operation no more than once per second.
    See also: AWS API Documentation
    
    Examples
    The following example sets the active receipt rule set:
    Expected Output:
    
    :example: response = client.set_active_receipt_rule_set(
        RuleSetName='string'
    )
    
    
    :type RuleSetName: string
    :param RuleSetName: The name of the receipt rule set to make active. Setting this value to null disables all email receiving.

    :rtype: dict
    :return: {}
    
    
    """
    pass

def set_identity_dkim_enabled(Identity=None, DkimEnabled=None):
    """
    Enables or disables Easy DKIM signing of email sent from an identity:
    For email addresses (for example, user@example.com ), you can only enable Easy DKIM signing if the corresponding domain (in this case, example.com ) has been set up for Easy DKIM using the AWS Console or the VerifyDomainDkim operation.
    You can execute this operation no more than once per second.
    For more information about Easy DKIM signing, go to the Amazon SES Developer Guide .
    See also: AWS API Documentation
    
    Examples
    The following example configures Amazon SES to Easy DKIM-sign the email sent from an identity:
    Expected Output:
    
    :example: response = client.set_identity_dkim_enabled(
        Identity='string',
        DkimEnabled=True|False
    )
    
    
    :type Identity: string
    :param Identity: [REQUIRED]
            The identity for which DKIM signing should be enabled or disabled.
            

    :type DkimEnabled: boolean
    :param DkimEnabled: [REQUIRED]
            Sets whether DKIM signing is enabled for an identity. Set to true to enable DKIM signing for this identity; false to disable it.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    Identity (string) -- [REQUIRED]
    The identity for which DKIM signing should be enabled or disabled.
    
    DkimEnabled (boolean) -- [REQUIRED]
    Sets whether DKIM signing is enabled for an identity. Set to true to enable DKIM signing for this identity; false to disable it.
    
    
    """
    pass

def set_identity_feedback_forwarding_enabled(Identity=None, ForwardingEnabled=None):
    """
    Given an identity (an email address or a domain), enables or disables whether Amazon SES forwards bounce and complaint notifications as email. Feedback forwarding can only be disabled when Amazon Simple Notification Service (Amazon SNS) topics are specified for both bounces and complaints.
    You can execute this operation no more than once per second.
    For more information about using notifications with Amazon SES, see the Amazon SES Developer Guide .
    See also: AWS API Documentation
    
    Examples
    The following example configures Amazon SES to forward an identity's bounces and complaints via email:
    Expected Output:
    
    :example: response = client.set_identity_feedback_forwarding_enabled(
        Identity='string',
        ForwardingEnabled=True|False
    )
    
    
    :type Identity: string
    :param Identity: [REQUIRED]
            The identity for which to set bounce and complaint notification forwarding. Examples: user@example.com , example.com .
            

    :type ForwardingEnabled: boolean
    :param ForwardingEnabled: [REQUIRED]
            Sets whether Amazon SES will forward bounce and complaint notifications as email. true specifies that Amazon SES will forward bounce and complaint notifications as email, in addition to any Amazon SNS topic publishing otherwise specified. false specifies that Amazon SES will publish bounce and complaint notifications only through Amazon SNS. This value can only be set to false when Amazon SNS topics are set for both Bounce and Complaint notification types.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def set_identity_headers_in_notifications_enabled(Identity=None, NotificationType=None, Enabled=None):
    """
    Given an identity (an email address or a domain), sets whether Amazon SES includes the original email headers in the Amazon Simple Notification Service (Amazon SNS) notifications of a specified type.
    You can execute this operation no more than once per second.
    For more information about using notifications with Amazon SES, see the Amazon SES Developer Guide .
    See also: AWS API Documentation
    
    Examples
    The following example configures Amazon SES to include the original email headers in the Amazon SNS bounce notifications for an identity:
    Expected Output:
    
    :example: response = client.set_identity_headers_in_notifications_enabled(
        Identity='string',
        NotificationType='Bounce'|'Complaint'|'Delivery',
        Enabled=True|False
    )
    
    
    :type Identity: string
    :param Identity: [REQUIRED]
            The identity for which to enable or disable headers in notifications. Examples: user@example.com , example.com .
            

    :type NotificationType: string
    :param NotificationType: [REQUIRED]
            The notification type for which to enable or disable headers in notifications.
            

    :type Enabled: boolean
    :param Enabled: [REQUIRED]
            Sets whether Amazon SES includes the original email headers in Amazon SNS notifications of the specified notification type. A value of true specifies that Amazon SES will include headers in notifications, and a value of false specifies that Amazon SES will not include headers in notifications.
            This value can only be set when NotificationType is already set to use a particular Amazon SNS topic.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def set_identity_mail_from_domain(Identity=None, MailFromDomain=None, BehaviorOnMXFailure=None):
    """
    Enables or disables the custom MAIL FROM domain setup for a verified identity (an email address or a domain).
    You can execute this operation no more than once per second.
    See also: AWS API Documentation
    
    Examples
    The following example configures Amazon SES to use a custom MAIL FROM domain for an identity:
    Expected Output:
    
    :example: response = client.set_identity_mail_from_domain(
        Identity='string',
        MailFromDomain='string',
        BehaviorOnMXFailure='UseDefaultValue'|'RejectMessage'
    )
    
    
    :type Identity: string
    :param Identity: [REQUIRED]
            The verified identity for which you want to enable or disable the specified custom MAIL FROM domain.
            

    :type MailFromDomain: string
    :param MailFromDomain: The custom MAIL FROM domain that you want the verified identity to use. The MAIL FROM domain must 1) be a subdomain of the verified identity, 2) not be used in a 'From' address if the MAIL FROM domain is the destination of email feedback forwarding (for more information, see the Amazon SES Developer Guide ), and 3) not be used to receive emails. A value of null disables the custom MAIL FROM setting for the identity.

    :type BehaviorOnMXFailure: string
    :param BehaviorOnMXFailure: The action that you want Amazon SES to take if it cannot successfully read the required MX record when you send an email. If you choose UseDefaultValue , Amazon SES will use amazonses.com (or a subdomain of that) as the MAIL FROM domain. If you choose RejectMessage , Amazon SES will return a MailFromDomainNotVerified error and not send the email.
            The action specified in BehaviorOnMXFailure is taken when the custom MAIL FROM domain setup is in the Pending , Failed , and TemporaryFailure states.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def set_identity_notification_topic(Identity=None, NotificationType=None, SnsTopic=None):
    """
    Given an identity (an email address or a domain), sets the Amazon Simple Notification Service (Amazon SNS) topic to which Amazon SES will publish bounce, complaint, and/or delivery notifications for emails sent with that identity as the Source .
    You can execute this operation no more than once per second.
    For more information about feedback notification, see the Amazon SES Developer Guide .
    See also: AWS API Documentation
    
    Examples
    The following example sets the Amazon SNS topic to which Amazon SES will publish bounce, complaint, and/or delivery notifications for emails sent with the specified identity as the Source:
    Expected Output:
    
    :example: response = client.set_identity_notification_topic(
        Identity='string',
        NotificationType='Bounce'|'Complaint'|'Delivery',
        SnsTopic='string'
    )
    
    
    :type Identity: string
    :param Identity: [REQUIRED]
            The identity for which the Amazon SNS topic will be set. You can specify an identity by using its name or by using its Amazon Resource Name (ARN). Examples: user@example.com , example.com , arn:aws:ses:us-east-1:123456789012:identity/example.com .
            

    :type NotificationType: string
    :param NotificationType: [REQUIRED]
            The type of notifications that will be published to the specified Amazon SNS topic.
            

    :type SnsTopic: string
    :param SnsTopic: The Amazon Resource Name (ARN) of the Amazon SNS topic. If the parameter is omitted from the request or a null value is passed, SnsTopic is cleared and publishing is disabled.

    :rtype: dict
    :return: {}
    
    
    """
    pass

def set_receipt_rule_position(RuleSetName=None, RuleName=None, After=None):
    """
    Sets the position of the specified receipt rule in the receipt rule set.
    For information about managing receipt rules, see the Amazon SES Developer Guide .
    You can execute this operation no more than once per second.
    See also: AWS API Documentation
    
    Examples
    The following example sets the position of a receipt rule in a receipt rule set:
    Expected Output:
    
    :example: response = client.set_receipt_rule_position(
        RuleSetName='string',
        RuleName='string',
        After='string'
    )
    
    
    :type RuleSetName: string
    :param RuleSetName: [REQUIRED]
            The name of the receipt rule set that contains the receipt rule to reposition.
            

    :type RuleName: string
    :param RuleName: [REQUIRED]
            The name of the receipt rule to reposition.
            

    :type After: string
    :param After: The name of the receipt rule after which to place the specified receipt rule.

    :rtype: dict
    :return: {}
    
    
    """
    pass

def test_render_template(TemplateName=None, TemplateData=None):
    """
    Creates a preview of the MIME content of an email when provided with a template and a set of replacement data.
    You can execute this operation no more than once per second.
    See also: AWS API Documentation
    
    
    :example: response = client.test_render_template(
        TemplateName='string',
        TemplateData='string'
    )
    
    
    :type TemplateName: string
    :param TemplateName: [REQUIRED]
            The name of the template that you want to render.
            

    :type TemplateData: string
    :param TemplateData: [REQUIRED]
            A list of replacement values to apply to the template. This parameter is a JSON object, typically consisting of key-value pairs in which the keys correspond to replacement tags in the email template.
            

    :rtype: dict
    :return: {
        'RenderedTemplate': 'string'
    }
    
    
    """
    pass

def update_account_sending_enabled(Enabled=None):
    """
    Enables or disables email sending across your entire Amazon SES account. You can use this operation in conjunction with Amazon CloudWatch alarms to temporarily pause email sending across your Amazon SES account when reputation metrics (such as your bounce on complaint rate) reach certain thresholds.
    You can execute this operation no more than once per second.
    See also: AWS API Documentation
    
    
    :example: response = client.update_account_sending_enabled(
        Enabled=True|False
    )
    
    
    :type Enabled: boolean
    :param Enabled: Describes whether email sending is enabled or disabled for your Amazon SES account.

    """
    pass

def update_configuration_set_event_destination(ConfigurationSetName=None, EventDestination=None):
    """
    Updates the event destination of a configuration set. Event destinations are associated with configuration sets, which enable you to publish email sending events to Amazon CloudWatch, Amazon Kinesis Firehose, or Amazon Simple Notification Service (Amazon SNS). For information about using configuration sets, see Monitoring Your Amazon SES Sending Activity in the Amazon SES Developer Guide.
    You can execute this operation no more than once per second.
    See also: AWS API Documentation
    
    
    :example: response = client.update_configuration_set_event_destination(
        ConfigurationSetName='string',
        EventDestination={
            'Name': 'string',
            'Enabled': True|False,
            'MatchingEventTypes': [
                'send'|'reject'|'bounce'|'complaint'|'delivery'|'open'|'click'|'renderingFailure',
            ],
            'KinesisFirehoseDestination': {
                'IAMRoleARN': 'string',
                'DeliveryStreamARN': 'string'
            },
            'CloudWatchDestination': {
                'DimensionConfigurations': [
                    {
                        'DimensionName': 'string',
                        'DimensionValueSource': 'messageTag'|'emailHeader'|'linkTag',
                        'DefaultDimensionValue': 'string'
                    },
                ]
            },
            'SNSDestination': {
                'TopicARN': 'string'
            }
        }
    )
    
    
    :type ConfigurationSetName: string
    :param ConfigurationSetName: [REQUIRED]
            The name of the configuration set that contains the event destination that you want to update.
            

    :type EventDestination: dict
    :param EventDestination: [REQUIRED]
            The event destination object that you want to apply to the specified configuration set.
            Name (string) -- [REQUIRED]The name of the event destination. The name must:
            This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
            Contain less than 64 characters.
            Enabled (boolean) --Sets whether Amazon SES publishes events to this destination when you send an email with the associated configuration set. Set to true to enable publishing to this destination; set to false to prevent publishing to this destination. The default value is false .
            MatchingEventTypes (list) -- [REQUIRED]The type of email sending events to publish to the event destination.
            (string) --
            KinesisFirehoseDestination (dict) --An object that contains the delivery stream ARN and the IAM role ARN associated with an Amazon Kinesis Firehose event destination.
            IAMRoleARN (string) -- [REQUIRED]The ARN of the IAM role under which Amazon SES publishes email sending events to the Amazon Kinesis Firehose stream.
            DeliveryStreamARN (string) -- [REQUIRED]The ARN of the Amazon Kinesis Firehose stream that email sending events should be published to.
            CloudWatchDestination (dict) --An object that contains the names, default values, and sources of the dimensions associated with an Amazon CloudWatch event destination.
            DimensionConfigurations (list) -- [REQUIRED]A list of dimensions upon which to categorize your emails when you publish email sending events to Amazon CloudWatch.
            (dict) --Contains the dimension configuration to use when you publish email sending events to Amazon CloudWatch.
            For information about publishing email sending events to Amazon CloudWatch, see the Amazon SES Developer Guide .
            DimensionName (string) -- [REQUIRED]The name of an Amazon CloudWatch dimension associated with an email sending metric. The name must:
            This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
            Contain less than 256 characters.
            DimensionValueSource (string) -- [REQUIRED]The place where Amazon SES finds the value of a dimension to publish to Amazon CloudWatch. If you want Amazon SES to use the message tags that you specify using an X-SES-MESSAGE-TAGS header or a parameter to the SendEmail /SendRawEmail API, choose messageTag . If you want Amazon SES to use your own email headers, choose emailHeader .
            DefaultDimensionValue (string) -- [REQUIRED]The default value of the dimension that is published to Amazon CloudWatch if you do not provide the value of the dimension when you send an email. The default value must:
            This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
            Contain less than 256 characters.
            
            
            SNSDestination (dict) --An object that contains the topic ARN associated with an Amazon Simple Notification Service (Amazon SNS) event destination.
            TopicARN (string) -- [REQUIRED]The ARN of the Amazon SNS topic that email sending events will be published to. An example of an Amazon SNS topic ARN is arn:aws:sns:us-west-2:123456789012:MyTopic . For more information about Amazon SNS topics, see the Amazon SNS Developer Guide .
            
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def update_configuration_set_reputation_metrics_enabled(ConfigurationSetName=None, Enabled=None):
    """
    Enables or disables the publishing of reputation metrics for emails sent using a specific configuration set. Reputation metrics include bounce and complaint rates. These metrics are published to Amazon CloudWatch. By using Amazon CloudWatch, you can create alarms when bounce or complaint rates exceed a certain threshold.
    You can execute this operation no more than once per second.
    See also: AWS API Documentation
    
    
    :example: response = client.update_configuration_set_reputation_metrics_enabled(
        ConfigurationSetName='string',
        Enabled=True|False
    )
    
    
    :type ConfigurationSetName: string
    :param ConfigurationSetName: [REQUIRED]
            The name of the configuration set that you want to update.
            

    :type Enabled: boolean
    :param Enabled: [REQUIRED]
            Describes whether or not Amazon SES will publish reputation metrics for the configuration set, such as bounce and complaint rates, to Amazon CloudWatch.
            

    """
    pass

def update_configuration_set_sending_enabled(ConfigurationSetName=None, Enabled=None):
    """
    Enables or disables email sending for messages sent using a specific configuration set. You can use this operation in conjunction with Amazon CloudWatch alarms to temporarily pause email sending for a configuration set when the reputation metrics for that configuration set (such as your bounce on complaint rate) reach certain thresholds.
    You can execute this operation no more than once per second.
    See also: AWS API Documentation
    
    
    :example: response = client.update_configuration_set_sending_enabled(
        ConfigurationSetName='string',
        Enabled=True|False
    )
    
    
    :type ConfigurationSetName: string
    :param ConfigurationSetName: [REQUIRED]
            The name of the configuration set that you want to update.
            

    :type Enabled: boolean
    :param Enabled: [REQUIRED]
            Describes whether email sending is enabled or disabled for the configuration set.
            

    """
    pass

def update_configuration_set_tracking_options(ConfigurationSetName=None, TrackingOptions=None):
    """
    Modifies an association between a configuration set and a custom domain for open and click event tracking.
    By default, images and links used for tracking open and click events are hosted on domains operated by Amazon SES. You can configure a subdomain of your own to handle these events. For information about using configuration sets, see Configuring Custom Domains to Handle Open and Click Tracking in the Amazon SES Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.update_configuration_set_tracking_options(
        ConfigurationSetName='string',
        TrackingOptions={
            'CustomRedirectDomain': 'string'
        }
    )
    
    
    :type ConfigurationSetName: string
    :param ConfigurationSetName: [REQUIRED]
            The name of the configuration set for which you want to update the custom tracking domain.
            

    :type TrackingOptions: dict
    :param TrackingOptions: [REQUIRED]
            A domain that is used to redirect email recipients to an Amazon SES-operated domain. This domain captures open and click events generated by Amazon SES emails.
            For more information, see Configuring Custom Domains to Handle Open and Click Tracking in the Amazon SES Developer Guide .
            CustomRedirectDomain (string) --The custom subdomain that will be used to redirect email recipients to the Amazon SES event tracking domain.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def update_custom_verification_email_template(TemplateName=None, FromEmailAddress=None, TemplateSubject=None, TemplateContent=None, SuccessRedirectionURL=None, FailureRedirectionURL=None):
    """
    Updates an existing custom verification email template.
    For more information about custom verification email templates, see Using Custom Verification Email Templates in the Amazon SES Developer Guide .
    You can execute this operation no more than once per second.
    See also: AWS API Documentation
    
    
    :example: response = client.update_custom_verification_email_template(
        TemplateName='string',
        FromEmailAddress='string',
        TemplateSubject='string',
        TemplateContent='string',
        SuccessRedirectionURL='string',
        FailureRedirectionURL='string'
    )
    
    
    :type TemplateName: string
    :param TemplateName: [REQUIRED]
            The name of the custom verification email template that you want to update.
            

    :type FromEmailAddress: string
    :param FromEmailAddress: The email address that the custom verification email is sent from.

    :type TemplateSubject: string
    :param TemplateSubject: The subject line of the custom verification email.

    :type TemplateContent: string
    :param TemplateContent: The content of the custom verification email. The total size of the email must be less than 10 MB. The message body may contain HTML, with some limitations. For more information, see Custom Verification Email Frequently Asked Questions in the Amazon SES Developer Guide .

    :type SuccessRedirectionURL: string
    :param SuccessRedirectionURL: The URL that the recipient of the verification email is sent to if his or her address is successfully verified.

    :type FailureRedirectionURL: string
    :param FailureRedirectionURL: The URL that the recipient of the verification email is sent to if his or her address is not successfully verified.

    """
    pass

def update_receipt_rule(RuleSetName=None, Rule=None):
    """
    Updates a receipt rule.
    For information about managing receipt rules, see the Amazon SES Developer Guide .
    You can execute this operation no more than once per second.
    See also: AWS API Documentation
    
    Examples
    The following example updates a receipt rule to use an Amazon S3 action:
    Expected Output:
    
    :example: response = client.update_receipt_rule(
        RuleSetName='string',
        Rule={
            'Name': 'string',
            'Enabled': True|False,
            'TlsPolicy': 'Require'|'Optional',
            'Recipients': [
                'string',
            ],
            'Actions': [
                {
                    'S3Action': {
                        'TopicArn': 'string',
                        'BucketName': 'string',
                        'ObjectKeyPrefix': 'string',
                        'KmsKeyArn': 'string'
                    },
                    'BounceAction': {
                        'TopicArn': 'string',
                        'SmtpReplyCode': 'string',
                        'StatusCode': 'string',
                        'Message': 'string',
                        'Sender': 'string'
                    },
                    'WorkmailAction': {
                        'TopicArn': 'string',
                        'OrganizationArn': 'string'
                    },
                    'LambdaAction': {
                        'TopicArn': 'string',
                        'FunctionArn': 'string',
                        'InvocationType': 'Event'|'RequestResponse'
                    },
                    'StopAction': {
                        'Scope': 'RuleSet',
                        'TopicArn': 'string'
                    },
                    'AddHeaderAction': {
                        'HeaderName': 'string',
                        'HeaderValue': 'string'
                    },
                    'SNSAction': {
                        'TopicArn': 'string',
                        'Encoding': 'UTF-8'|'Base64'
                    }
                },
            ],
            'ScanEnabled': True|False
        }
    )
    
    
    :type RuleSetName: string
    :param RuleSetName: [REQUIRED]
            The name of the receipt rule set that the receipt rule belongs to.
            

    :type Rule: dict
    :param Rule: [REQUIRED]
            A data structure that contains the updated receipt rule information.
            Name (string) -- [REQUIRED]The name of the receipt rule. The name must:
            This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
            Start and end with a letter or number.
            Contain less than 64 characters.
            Enabled (boolean) --If true , the receipt rule is active. The default value is false .
            TlsPolicy (string) --Specifies whether Amazon SES should require that incoming email is delivered over a connection encrypted with Transport Layer Security (TLS). If this parameter is set to Require , Amazon SES will bounce emails that are not received over TLS. The default is Optional .
            Recipients (list) --The recipient domains and email addresses that the receipt rule applies to. If this field is not specified, this rule will match all recipients under all verified domains.
            (string) --
            Actions (list) --An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule.
            (dict) --An action that Amazon SES can take when it receives an email on behalf of one or more email addresses or domains that you own. An instance of this data type can represent only one action.
            For information about setting up receipt rules, see the Amazon SES Developer Guide .
            S3Action (dict) --Saves the received message to an Amazon Simple Storage Service (Amazon S3) bucket and, optionally, publishes a notification to Amazon SNS.
            TopicArn (string) --The ARN of the Amazon SNS topic to notify when the message is saved to the Amazon S3 bucket. An example of an Amazon SNS topic ARN is arn:aws:sns:us-west-2:123456789012:MyTopic . For more information about Amazon SNS topics, see the Amazon SNS Developer Guide .
            BucketName (string) -- [REQUIRED]The name of the Amazon S3 bucket that incoming email will be saved to.
            ObjectKeyPrefix (string) --The key prefix of the Amazon S3 bucket. The key prefix is similar to a directory name that enables you to store similar data under the same directory in a bucket.
            KmsKeyArn (string) --The customer master key that Amazon SES should use to encrypt your emails before saving them to the Amazon S3 bucket. You can use the default master key or a custom master key you created in AWS KMS as follows:
            To use the default master key, provide an ARN in the form of arn:aws:kms:REGION:ACCOUNT-ID-WITHOUT-HYPHENS:alias/aws/ses . For example, if your AWS account ID is 123456789012 and you want to use the default master key in the US West (Oregon) region, the ARN of the default master key would be arn:aws:kms:us-west-2:123456789012:alias/aws/ses . If you use the default master key, you don't need to perform any extra steps to give Amazon SES permission to use the key.
            To use a custom master key you created in AWS KMS, provide the ARN of the master key and ensure that you add a statement to your key's policy to give Amazon SES permission to use it. For more information about giving permissions, see the Amazon SES Developer Guide .
            For more information about key policies, see the AWS KMS Developer Guide . If you do not specify a master key, Amazon SES will not encrypt your emails.
            Warning
            Your mail is encrypted by Amazon SES using the Amazon S3 encryption client before the mail is submitted to Amazon S3 for storage. It is not encrypted using Amazon S3 server-side encryption. This means that you must use the Amazon S3 encryption client to decrypt the email after retrieving it from Amazon S3, as the service has no access to use your AWS KMS keys for decryption. This encryption client is currently available with the AWS Java SDK and AWS Ruby SDK only. For more information about client-side encryption using AWS KMS master keys, see the Amazon S3 Developer Guide .
            
            BounceAction (dict) --Rejects the received email by returning a bounce response to the sender and, optionally, publishes a notification to Amazon Simple Notification Service (Amazon SNS).
            TopicArn (string) --The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the bounce action is taken. An example of an Amazon SNS topic ARN is arn:aws:sns:us-west-2:123456789012:MyTopic . For more information about Amazon SNS topics, see the Amazon SNS Developer Guide .
            SmtpReplyCode (string) -- [REQUIRED]The SMTP reply code, as defined by RFC 5321 .
            StatusCode (string) --The SMTP enhanced status code, as defined by RFC 3463 .
            Message (string) -- [REQUIRED]Human-readable text to include in the bounce message.
            Sender (string) -- [REQUIRED]The email address of the sender of the bounced email. This is the address from which the bounce message will be sent.
            WorkmailAction (dict) --Calls Amazon WorkMail and, optionally, publishes a notification to Amazon SNS.
            TopicArn (string) --The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the WorkMail action is called. An example of an Amazon SNS topic ARN is arn:aws:sns:us-west-2:123456789012:MyTopic . For more information about Amazon SNS topics, see the Amazon SNS Developer Guide .
            OrganizationArn (string) -- [REQUIRED]The ARN of the Amazon WorkMail organization. An example of an Amazon WorkMail organization ARN is arn:aws:workmail:us-west-2:123456789012:organization/m-68755160c4cb4e29a2b2f8fb58f359d7 . For information about Amazon WorkMail organizations, see the Amazon WorkMail Administrator Guide .
            LambdaAction (dict) --Calls an AWS Lambda function, and optionally, publishes a notification to Amazon SNS.
            TopicArn (string) --The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the Lambda action is taken. An example of an Amazon SNS topic ARN is arn:aws:sns:us-west-2:123456789012:MyTopic . For more information about Amazon SNS topics, see the Amazon SNS Developer Guide .
            FunctionArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the AWS Lambda function. An example of an AWS Lambda function ARN is arn:aws:lambda:us-west-2:account-id:function:MyFunction . For more information about AWS Lambda, see the AWS Lambda Developer Guide .
            InvocationType (string) --The invocation type of the AWS Lambda function. An invocation type of RequestResponse means that the execution of the function will immediately result in a response, and a value of Event means that the function will be invoked asynchronously. The default value is Event . For information about AWS Lambda invocation types, see the AWS Lambda Developer Guide .
            Warning
            There is a 30-second timeout on RequestResponse invocations. You should use Event invocation in most cases. Use RequestResponse only when you want to make a mail flow decision, such as whether to stop the receipt rule or the receipt rule set.
            
            StopAction (dict) --Terminates the evaluation of the receipt rule set and optionally publishes a notification to Amazon SNS.
            Scope (string) -- [REQUIRED]The name of the RuleSet that is being stopped.
            TopicArn (string) --The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the stop action is taken. An example of an Amazon SNS topic ARN is arn:aws:sns:us-west-2:123456789012:MyTopic . For more information about Amazon SNS topics, see the Amazon SNS Developer Guide .
            AddHeaderAction (dict) --Adds a header to the received email.
            HeaderName (string) -- [REQUIRED]The name of the header to add. Must be between 1 and 50 characters, inclusive, and consist of alphanumeric (a-z, A-Z, 0-9) characters and dashes only.
            HeaderValue (string) -- [REQUIRED]Must be less than 2048 characters, and must not contain newline characters ('r' or 'n').
            SNSAction (dict) --Publishes the email content within a notification to Amazon SNS.
            TopicArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the Amazon SNS topic to notify. An example of an Amazon SNS topic ARN is arn:aws:sns:us-west-2:123456789012:MyTopic . For more information about Amazon SNS topics, see the Amazon SNS Developer Guide .
            Encoding (string) --The encoding to use for the email within the Amazon SNS notification. UTF-8 is easier to use, but may not preserve all special characters when a message was encoded with a different encoding format. Base64 preserves all special characters. The default value is UTF-8.
            
            ScanEnabled (boolean) --If true , then messages that this receipt rule applies to are scanned for spam and viruses. The default value is false .
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def update_template(Template=None):
    """
    Updates an email template. Email templates enable you to send personalized email to one or more destinations in a single API operation. For more information, see the Amazon SES Developer Guide .
    You can execute this operation no more than once per second.
    See also: AWS API Documentation
    
    
    :example: response = client.update_template(
        Template={
            'TemplateName': 'string',
            'SubjectPart': 'string',
            'TextPart': 'string',
            'HtmlPart': 'string'
        }
    )
    
    
    :type Template: dict
    :param Template: [REQUIRED]
            The content of the email, composed of a subject line, an HTML part, and a text-only part.
            TemplateName (string) -- [REQUIRED]The name of the template. You will refer to this name when you send email using the SendTemplatedEmail or SendBulkTemplatedEmail operations.
            SubjectPart (string) --The subject line of the email.
            TextPart (string) --The email body that will be visible to recipients whose email clients do not display HTML.
            HtmlPart (string) --The HTML body of the email.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def verify_domain_dkim(Domain=None):
    """
    Returns a set of DKIM tokens for a domain. DKIM tokens are character strings that represent your domain's identity. Using these tokens, you will need to create DNS CNAME records that point to DKIM public keys hosted by Amazon SES. Amazon Web Services will eventually detect that you have updated your DNS records; this detection process may take up to 72 hours. Upon successful detection, Amazon SES will be able to DKIM-sign email originating from that domain.
    You can execute this operation no more than once per second.
    To enable or disable Easy DKIM signing for a domain, use the SetIdentityDkimEnabled operation.
    For more information about creating DNS records using DKIM tokens, go to the Amazon SES Developer Guide .
    See also: AWS API Documentation
    
    Examples
    The following example generates DKIM tokens for a domain that has been verified with Amazon SES:
    Expected Output:
    
    :example: response = client.verify_domain_dkim(
        Domain='string'
    )
    
    
    :type Domain: string
    :param Domain: [REQUIRED]
            The name of the domain to be verified for Easy DKIM signing.
            

    :rtype: dict
    :return: {
        'DkimTokens': [
            'string',
        ]
    }
    
    
    """
    pass

def verify_domain_identity(Domain=None):
    """
    Adds a domain to the list of identities for your Amazon SES account and attempts to verify it. For more information about verifying domains, see Verifying Email Addresses and Domains in the Amazon SES Developer Guide.
    You can execute this operation no more than once per second.
    See also: AWS API Documentation
    
    Examples
    The following example starts the domain verification process with Amazon SES:
    Expected Output:
    
    :example: response = client.verify_domain_identity(
        Domain='string'
    )
    
    
    :type Domain: string
    :param Domain: [REQUIRED]
            The domain to be verified.
            

    :rtype: dict
    :return: {
        'VerificationToken': 'string'
    }
    
    
    """
    pass

def verify_email_address(EmailAddress=None):
    """
    Deprecated. Use the VerifyEmailIdentity operation to verify a new email address.
    See also: AWS API Documentation
    
    Examples
    The following example starts the email address verification process with Amazon SES:
    Expected Output:
    
    :example: response = client.verify_email_address(
        EmailAddress='string'
    )
    
    
    :type EmailAddress: string
    :param EmailAddress: [REQUIRED]
            The email address to be verified.
            

    :return: response = client.verify_email_address(
        EmailAddress='user@example.com',
    )
    
    print(response)
    
    
    """
    pass

def verify_email_identity(EmailAddress=None):
    """
    Adds an email address to the list of identities for your Amazon SES account and attempts to verify it. As a result of executing this operation, a verification email is sent to the specified address.
    You can execute this operation no more than once per second.
    See also: AWS API Documentation
    
    Examples
    The following example starts the email address verification process with Amazon SES:
    Expected Output:
    
    :example: response = client.verify_email_identity(
        EmailAddress='string'
    )
    
    
    :type EmailAddress: string
    :param EmailAddress: [REQUIRED]
            The email address to be verified.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

