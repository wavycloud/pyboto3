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


def clone_receipt_rule_set(RuleSetName=None, OriginalRuleSetName=None):
    """
    :param RuleSetName: [REQUIRED]
            The name of the rule set to create. The name must:
            Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (_), or dashes (-).
            Start and end with a letter or number.
            Contain less than 64 characters.
            
    :type RuleSetName: string
    :param OriginalRuleSetName: [REQUIRED]
            The name of the rule set to clone.
            
    :type OriginalRuleSetName: string
    """
    pass


def create_receipt_filter(Filter=None):
    """
    :param Filter: [REQUIRED]
            A data structure that describes the IP address filter to create, which consists of a name, an IP address range, and whether to allow or block mail from it.
            Name (string) -- [REQUIRED]The name of the IP address filter. The name must:
            Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (_), or dashes (-).
            Start and end with a letter or number.
            Contain less than 64 characters.
            IpFilter (dict) -- [REQUIRED]A structure that provides the IP addresses to block or allow, and whether to block or allow incoming mail from them.
            Policy (string) -- [REQUIRED]Indicates whether to block or allow incoming mail from the specified IP addresses.
            Cidr (string) -- [REQUIRED]A single IP address or a range of IP addresses that you want to block or allow, specified in Classless Inter-Domain Routing (CIDR) notation. An example of a single email address is 10.0.0.1. An example of a range of IP addresses is 10.0.0.1/24. For more information about CIDR notation, see RFC 2317 .
            
            Return typedict
            ReturnsResponse Syntax{}
            Response Structure
            (dict) --An empty element returned on a successful request.
            
            
    :type Filter: dict
    """
    pass


def create_receipt_rule(RuleSetName=None, After=None, Rule=None):
    """
    :param RuleSetName: [REQUIRED]
            The name of the rule set to which to add the rule.
            
    :type RuleSetName: string
    :param After: The name of an existing rule after which the new rule will be placed. If this parameter is null, the new rule will be inserted at the beginning of the rule list.
    :type After: string
    :param Rule: [REQUIRED]
            A data structure that contains the specified rule's name, actions, recipients, domains, enabled status, scan status, and TLS policy.
            Name (string) -- [REQUIRED]The name of the receipt rule. The name must:
            Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (_), or dashes (-).
            Start and end with a letter or number.
            Contain less than 64 characters.
            Enabled (boolean) --If true , the receipt rule is active. The default value is false .
            TlsPolicy (string) --Specifies whether Amazon SES should require that incoming email is delivered over a connection encrypted with Transport Layer Security (TLS). If this parameter is set to Require , Amazon SES will bounce emails that are not received over TLS. The default is Optional .
            Recipients (list) --The recipient domains and email addresses to which the receipt rule applies. If this field is not specified, this rule will match all recipients under all verified domains.
            (string) --
            Actions (list) --An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule.
            (dict) --An action that Amazon SES can take when it receives an email on behalf of one or more email addresses or domains that you own. An instance of this data type can represent only one action.
            For information about setting up receipt rules, see the Amazon SES Developer Guide .
            S3Action (dict) --Saves the received message to an Amazon Simple Storage Service (Amazon S3) bucket and, optionally, publishes a notification to Amazon SNS.
            TopicArn (string) --The ARN of the Amazon SNS topic to notify when the message is saved to the Amazon S3 bucket. An example of an Amazon SNS topic ARN is arn:aws:sns:us-west-2:123456789012:MyTopic . For more information about Amazon SNS topics, see the Amazon SNS Developer Guide .
            BucketName (string) -- [REQUIRED]The name of the Amazon S3 bucket to which to save the received email.
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
            Scope (string) -- [REQUIRED]The scope to which the Stop action applies. That is, what is being stopped.
            TopicArn (string) --The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the stop action is taken. An example of an Amazon SNS topic ARN is arn:aws:sns:us-west-2:123456789012:MyTopic . For more information about Amazon SNS topics, see the Amazon SNS Developer Guide .
            AddHeaderAction (dict) --Adds a header to the received email.
            HeaderName (string) -- [REQUIRED]The name of the header to add. Must be between 1 and 50 characters, inclusive, and consist of alphanumeric (a-z, A-Z, 0-9) characters and dashes only.
            HeaderValue (string) -- [REQUIRED]Must be less than 2048 characters, and must not contain newline characters ('r' or 'n').
            SNSAction (dict) --Publishes the email content within a notification to Amazon SNS.
            TopicArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the Amazon SNS topic to notify. An example of an Amazon SNS topic ARN is arn:aws:sns:us-west-2:123456789012:MyTopic . For more information about Amazon SNS topics, see the Amazon SNS Developer Guide .
            Encoding (string) --The encoding to use for the email within the Amazon SNS notification. UTF-8 is easier to use, but may not preserve all special characters when a message was encoded with a different encoding format. Base64 preserves all special characters. The default value is UTF-8.
            
            ScanEnabled (boolean) --If true , then messages to which this receipt rule applies are scanned for spam and viruses. The default value is false .
            
    :type Rule: dict
    """
    pass


def create_receipt_rule_set(RuleSetName=None):
    """
    :param RuleSetName: [REQUIRED]
            The name of the rule set to create. The name must:
            Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (_), or dashes (-).
            Start and end with a letter or number.
            Contain less than 64 characters.
            Return typedict
            ReturnsResponse Syntax{}
            Response Structure
            (dict) --An empty element returned on a successful request.
            
            
    :type RuleSetName: string
    """
    pass


def delete_identity(Identity=None):
    """
    :param Identity: [REQUIRED]
            The identity to be removed from the list of identities for the AWS Account.
            Return typedict
            ReturnsResponse Syntax{}
            Response Structure
            (dict) --An empty element returned on a successful request.
            
            
    :type Identity: string
    """
    pass


def delete_identity_policy(Identity=None, PolicyName=None):
    """
    :param Identity: [REQUIRED]
            The identity that is associated with the policy that you want to delete. You can specify the identity by using its name or by using its Amazon Resource Name (ARN). Examples: user@example.com , example.com , arn:aws:ses:us-east-1:123456789012:identity/example.com .
            To successfully call this API, you must own the identity.
            
    :type Identity: string
    :param PolicyName: [REQUIRED]
            The name of the policy to be deleted.
            
    :type PolicyName: string
    """
    pass


def delete_receipt_filter(FilterName=None):
    """
    :param FilterName: [REQUIRED]
            The name of the IP address filter to delete.
            Return typedict
            ReturnsResponse Syntax{}
            Response Structure
            (dict) --An empty element returned on a successful request.
            
            
    :type FilterName: string
    """
    pass


def delete_receipt_rule(RuleSetName=None, RuleName=None):
    """
    :param RuleSetName: [REQUIRED]
            The name of the receipt rule set that contains the receipt rule to delete.
            
    :type RuleSetName: string
    :param RuleName: [REQUIRED]
            The name of the receipt rule to delete.
            
    :type RuleName: string
    """
    pass


def delete_receipt_rule_set(RuleSetName=None):
    """
    :param RuleSetName: [REQUIRED]
            The name of the receipt rule set to delete.
            Return typedict
            ReturnsResponse Syntax{}
            Response Structure
            (dict) --An empty element returned on a successful request.
            
            
    :type RuleSetName: string
    """
    pass


def delete_verified_email_address(EmailAddress=None):
    """
    :param EmailAddress: [REQUIRED]
            An email address to be removed from the list of verified addresses.
            ReturnsNone
            
    :type EmailAddress: string
    """
    pass


def describe_active_receipt_rule_set():
    """
    """
    pass


def describe_receipt_rule(RuleSetName=None, RuleName=None):
    """
    :param RuleSetName: [REQUIRED]
            The name of the receipt rule set to which the receipt rule belongs.
            
    :type RuleSetName: string
    :param RuleName: [REQUIRED]
            The name of the receipt rule.
            
    :type RuleName: string
    """
    pass


def describe_receipt_rule_set(RuleSetName=None):
    """
    :param RuleSetName: [REQUIRED]
            The name of the receipt rule set to describe.
            Return typedict
            ReturnsResponse Syntax{
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
            Response Structure
            (dict) --Represents the details of the specified receipt rule set.
            Metadata (dict) --The metadata for the receipt rule set, which consists of the rule set name and the timestamp of when the rule set was created.
            Name (string) --The name of the receipt rule set. The name must:
            Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (_), or dashes (-).
            Start and end with a letter or number.
            Contain less than 64 characters.
            CreatedTimestamp (datetime) --The date and time the receipt rule set was created.
            Rules (list) --A list of the receipt rules that belong to the specified receipt rule set.
            (dict) --Receipt rules enable you to specify which actions Amazon SES should take when it receives mail on behalf of one or more email addresses or domains that you own.
            Each receipt rule defines a set of email addresses or domains to which it applies. If the email addresses or domains match at least one recipient address of the message, Amazon SES executes all of the receipt rule's actions on the message.
            For information about setting up receipt rules, see the Amazon SES Developer Guide .
            Name (string) --The name of the receipt rule. The name must:
            Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (_), or dashes (-).
            Start and end with a letter or number.
            Contain less than 64 characters.
            Enabled (boolean) --If true , the receipt rule is active. The default value is false .
            TlsPolicy (string) --Specifies whether Amazon SES should require that incoming email is delivered over a connection encrypted with Transport Layer Security (TLS). If this parameter is set to Require , Amazon SES will bounce emails that are not received over TLS. The default is Optional .
            Recipients (list) --The recipient domains and email addresses to which the receipt rule applies. If this field is not specified, this rule will match all recipients under all verified domains.
            (string) --
            Actions (list) --An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule.
            (dict) --An action that Amazon SES can take when it receives an email on behalf of one or more email addresses or domains that you own. An instance of this data type can represent only one action.
            For information about setting up receipt rules, see the Amazon SES Developer Guide .
            S3Action (dict) --Saves the received message to an Amazon Simple Storage Service (Amazon S3) bucket and, optionally, publishes a notification to Amazon SNS.
            TopicArn (string) --The ARN of the Amazon SNS topic to notify when the message is saved to the Amazon S3 bucket. An example of an Amazon SNS topic ARN is arn:aws:sns:us-west-2:123456789012:MyTopic . For more information about Amazon SNS topics, see the Amazon SNS Developer Guide .
            BucketName (string) --The name of the Amazon S3 bucket to which to save the received email.
            ObjectKeyPrefix (string) --The key prefix of the Amazon S3 bucket. The key prefix is similar to a directory name that enables you to store similar data under the same directory in a bucket.
            KmsKeyArn (string) --The customer master key that Amazon SES should use to encrypt your emails before saving them to the Amazon S3 bucket. You can use the default master key or a custom master key you created in AWS KMS as follows:
            To use the default master key, provide an ARN in the form of arn:aws:kms:REGION:ACCOUNT-ID-WITHOUT-HYPHENS:alias/aws/ses . For example, if your AWS account ID is 123456789012 and you want to use the default master key in the US West (Oregon) region, the ARN of the default master key would be arn:aws:kms:us-west-2:123456789012:alias/aws/ses . If you use the default master key, you don't need to perform any extra steps to give Amazon SES permission to use the key.
            To use a custom master key you created in AWS KMS, provide the ARN of the master key and ensure that you add a statement to your key's policy to give Amazon SES permission to use it. For more information about giving permissions, see the Amazon SES Developer Guide .
            For more information about key policies, see the AWS KMS Developer Guide . If you do not specify a master key, Amazon SES will not encrypt your emails.
            Warning
            Your mail is encrypted by Amazon SES using the Amazon S3 encryption client before the mail is submitted to Amazon S3 for storage. It is not encrypted using Amazon S3 server-side encryption. This means that you must use the Amazon S3 encryption client to decrypt the email after retrieving it from Amazon S3, as the service has no access to use your AWS KMS keys for decryption. This encryption client is currently available with the AWS Java SDK and AWS Ruby SDK only. For more information about client-side encryption using AWS KMS master keys, see the Amazon S3 Developer Guide .
            
            BounceAction (dict) --Rejects the received email by returning a bounce response to the sender and, optionally, publishes a notification to Amazon Simple Notification Service (Amazon SNS).
            TopicArn (string) --The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the bounce action is taken. An example of an Amazon SNS topic ARN is arn:aws:sns:us-west-2:123456789012:MyTopic . For more information about Amazon SNS topics, see the Amazon SNS Developer Guide .
            SmtpReplyCode (string) --The SMTP reply code, as defined by RFC 5321 .
            StatusCode (string) --The SMTP enhanced status code, as defined by RFC 3463 .
            Message (string) --Human-readable text to include in the bounce message.
            Sender (string) --The email address of the sender of the bounced email. This is the address from which the bounce message will be sent.
            WorkmailAction (dict) --Calls Amazon WorkMail and, optionally, publishes a notification to Amazon SNS.
            TopicArn (string) --The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the WorkMail action is called. An example of an Amazon SNS topic ARN is arn:aws:sns:us-west-2:123456789012:MyTopic . For more information about Amazon SNS topics, see the Amazon SNS Developer Guide .
            OrganizationArn (string) --The ARN of the Amazon WorkMail organization. An example of an Amazon WorkMail organization ARN is arn:aws:workmail:us-west-2:123456789012:organization/m-68755160c4cb4e29a2b2f8fb58f359d7 . For information about Amazon WorkMail organizations, see the Amazon WorkMail Administrator Guide .
            LambdaAction (dict) --Calls an AWS Lambda function, and optionally, publishes a notification to Amazon SNS.
            TopicArn (string) --The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the Lambda action is taken. An example of an Amazon SNS topic ARN is arn:aws:sns:us-west-2:123456789012:MyTopic . For more information about Amazon SNS topics, see the Amazon SNS Developer Guide .
            FunctionArn (string) --The Amazon Resource Name (ARN) of the AWS Lambda function. An example of an AWS Lambda function ARN is arn:aws:lambda:us-west-2:account-id:function:MyFunction . For more information about AWS Lambda, see the AWS Lambda Developer Guide .
            InvocationType (string) --The invocation type of the AWS Lambda function. An invocation type of RequestResponse means that the execution of the function will immediately result in a response, and a value of Event means that the function will be invoked asynchronously. The default value is Event . For information about AWS Lambda invocation types, see the AWS Lambda Developer Guide .
            Warning
            There is a 30-second timeout on RequestResponse invocations. You should use Event invocation in most cases. Use RequestResponse only when you want to make a mail flow decision, such as whether to stop the receipt rule or the receipt rule set.
            
            StopAction (dict) --Terminates the evaluation of the receipt rule set and optionally publishes a notification to Amazon SNS.
            Scope (string) --The scope to which the Stop action applies. That is, what is being stopped.
            TopicArn (string) --The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the stop action is taken. An example of an Amazon SNS topic ARN is arn:aws:sns:us-west-2:123456789012:MyTopic . For more information about Amazon SNS topics, see the Amazon SNS Developer Guide .
            AddHeaderAction (dict) --Adds a header to the received email.
            HeaderName (string) --The name of the header to add. Must be between 1 and 50 characters, inclusive, and consist of alphanumeric (a-z, A-Z, 0-9) characters and dashes only.
            HeaderValue (string) --Must be less than 2048 characters, and must not contain newline characters ('r' or 'n').
            SNSAction (dict) --Publishes the email content within a notification to Amazon SNS.
            TopicArn (string) --The Amazon Resource Name (ARN) of the Amazon SNS topic to notify. An example of an Amazon SNS topic ARN is arn:aws:sns:us-west-2:123456789012:MyTopic . For more information about Amazon SNS topics, see the Amazon SNS Developer Guide .
            Encoding (string) --The encoding to use for the email within the Amazon SNS notification. UTF-8 is easier to use, but may not preserve all special characters when a message was encoded with a different encoding format. Base64 preserves all special characters. The default value is UTF-8.
            
            ScanEnabled (boolean) --If true , then messages to which this receipt rule applies are scanned for spam and viruses. The default value is false .
            
            
            
    :type RuleSetName: string
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


def get_identity_dkim_attributes(Identities=None):
    """
    :param Identities: [REQUIRED]
            A list of one or more verified identities - email addresses, domains, or both.
            (string) --
            Return typedict
            ReturnsResponse Syntax{
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
            Response Structure
            (dict) --Represents the status of Amazon SES Easy DKIM signing for an identity. For domain identities, this response also contains the DKIM tokens that are required for Easy DKIM signing, and whether Amazon SES successfully verified that these tokens were published.
            DkimAttributes (dict) --The DKIM attributes for an email address or a domain.
            (string) --
            (dict) --Represents the DKIM attributes of a verified email address or a domain.
            DkimEnabled (boolean) --True if DKIM signing is enabled for email sent from the identity; false otherwise.
            DkimVerificationStatus (string) --Describes whether Amazon SES has successfully verified the DKIM DNS records (tokens) published in the domain name's DNS. (This only applies to domain identities, not email address identities.)
            DkimTokens (list) --A set of character strings that represent the domain's identity. Using these tokens, you will need to create DNS CNAME records that point to DKIM public keys hosted by Amazon SES. Amazon Web Services will eventually detect that you have updated your DNS records; this detection process may take up to 72 hours. Upon successful detection, Amazon SES will be able to DKIM-sign email originating from that domain. (This only applies to domain identities, not email address identities.)
            For more information about creating DNS records using DKIM tokens, go to the Amazon SES Developer Guide .
            (string) --
            
            
            
            
    :type Identities: list
    """
    pass


def get_identity_mail_from_domain_attributes(Identities=None):
    """
    :param Identities: [REQUIRED]
            A list of one or more identities.
            (string) --
            Return typedict
            ReturnsResponse Syntax{
              'MailFromDomainAttributes': {
                'string': {
                  'MailFromDomain': 'string',
                  'MailFromDomainStatus': 'Pending'|'Success'|'Failed'|'TemporaryFailure',
                  'BehaviorOnMXFailure': 'UseDefaultValue'|'RejectMessage'
                }
              }
            }
            Response Structure
            (dict) --Represents the custom MAIL FROM attributes for a list of identities.
            MailFromDomainAttributes (dict) --A map of identities to custom MAIL FROM attributes.
            (string) --
            (dict) --Represents the custom MAIL FROM domain attributes of a verified identity (email address or domain).
            MailFromDomain (string) --The custom MAIL FROM domain that the identity is configured to use.
            MailFromDomainStatus (string) --The state that indicates whether Amazon SES has successfully read the MX record required for custom MAIL FROM domain setup. If the state is Success , Amazon SES uses the specified custom MAIL FROM domain when the verified identity sends an email. All other states indicate that Amazon SES takes the action described by BehaviorOnMXFailure .
            BehaviorOnMXFailure (string) --The action that Amazon SES takes if it cannot successfully read the required MX record when you send an email. A value of UseDefaultValue indicates that if Amazon SES cannot read the required MX record, it uses amazonses.com (or a subdomain of that) as the MAIL FROM domain. A value of RejectMessage indicates that if Amazon SES cannot read the required MX record, Amazon SES returns a MailFromDomainNotVerified error and does not send the email.
            The custom MAIL FROM setup states that result in this behavior are Pending , Failed , and TemporaryFailure .
            
            
            
            
    :type Identities: list
    """
    pass


def get_identity_notification_attributes(Identities=None):
    """
    :param Identities: [REQUIRED]
            A list of one or more identities. You can specify an identity by using its name or by using its Amazon Resource Name (ARN). Examples: user@example.com , example.com , arn:aws:ses:us-east-1:123456789012:identity/example.com .
            (string) --
            Return typedict
            ReturnsResponse Syntax{
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
            Response Structure
            (dict) --Represents the notification attributes for a list of identities.
            NotificationAttributes (dict) --A map of Identity to IdentityNotificationAttributes.
            (string) --
            (dict) --Represents the notification attributes of an identity, including whether an identity has Amazon Simple Notification Service (Amazon SNS) topics set for bounce, complaint, and/or delivery notifications, and whether feedback forwarding is enabled for bounce and complaint notifications.
            BounceTopic (string) --The Amazon Resource Name (ARN) of the Amazon SNS topic where Amazon SES will publish bounce notifications.
            ComplaintTopic (string) --The Amazon Resource Name (ARN) of the Amazon SNS topic where Amazon SES will publish complaint notifications.
            DeliveryTopic (string) --The Amazon Resource Name (ARN) of the Amazon SNS topic where Amazon SES will publish delivery notifications.
            ForwardingEnabled (boolean) --Describes whether Amazon SES will forward bounce and complaint notifications as email. true indicates that Amazon SES will forward bounce and complaint notifications as email, while false indicates that bounce and complaint notifications will be published only to the specified bounce and complaint Amazon SNS topics.
            HeadersInBounceNotificationsEnabled (boolean) --Describes whether Amazon SES includes the original email headers in Amazon SNS notifications of type Bounce . A value of true specifies that Amazon SES will include headers in bounce notifications, and a value of false specifies that Amazon SES will not include headers in bounce notifications.
            HeadersInComplaintNotificationsEnabled (boolean) --Describes whether Amazon SES includes the original email headers in Amazon SNS notifications of type Complaint . A value of true specifies that Amazon SES will include headers in complaint notifications, and a value of false specifies that Amazon SES will not include headers in complaint notifications.
            HeadersInDeliveryNotificationsEnabled (boolean) --Describes whether Amazon SES includes the original email headers in Amazon SNS notifications of type Delivery . A value of true specifies that Amazon SES will include headers in delivery notifications, and a value of false specifies that Amazon SES will not include headers in delivery notifications.
            
            
            
            
    :type Identities: list
    """
    pass


def get_identity_policies(Identity=None, PolicyNames=None):
    """
    :param Identity: [REQUIRED]
            The identity for which the policies will be retrieved. You can specify an identity by using its name or by using its Amazon Resource Name (ARN). Examples: user@example.com , example.com , arn:aws:ses:us-east-1:123456789012:identity/example.com .
            To successfully call this API, you must own the identity.
            
    :type Identity: string
    :param PolicyNames: [REQUIRED]
            A list of the names of policies to be retrieved. You can retrieve a maximum of 20 policies at a time. If you do not know the names of the policies that are attached to the identity, you can use ListIdentityPolicies .
            (string) --
            
    :type PolicyNames: list
    """
    pass


def get_identity_verification_attributes(Identities=None):
    """
    :param Identities: [REQUIRED]
            A list of identities.
            (string) --
            Return typedict
            ReturnsResponse Syntax{
              'VerificationAttributes': {
                'string': {
                  'VerificationStatus': 'Pending'|'Success'|'Failed'|'TemporaryFailure'|'NotStarted',
                  'VerificationToken': 'string'
                }
              }
            }
            Response Structure
            (dict) --The Amazon SES verification status of a list of identities. For domain identities, this response also contains the verification token.
            VerificationAttributes (dict) --A map of Identities to IdentityVerificationAttributes objects.
            (string) --
            (dict) --Represents the verification attributes of a single identity.
            VerificationStatus (string) --The verification status of the identity: 'Pending', 'Success', 'Failed', or 'TemporaryFailure'.
            VerificationToken (string) --The verification token for a domain identity. Null for email address identities.
            
            
            
            
    :type Identities: list
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


def get_send_quota():
    """
    """
    pass


def get_send_statistics():
    """
    """
    pass


def get_waiter():
    """
    """
    pass


def list_identities(IdentityType=None, NextToken=None, MaxItems=None):
    """
    :param IdentityType: The type of the identities to list. Possible values are 'EmailAddress' and 'Domain'. If this parameter is omitted, then all identities will be listed.
    :type IdentityType: string
    :param NextToken: The token to use for pagination.
    :type NextToken: string
    :param MaxItems: The maximum number of identities per page. Possible values are 1-1000 inclusive.
    :type MaxItems: integer
    """
    pass


def list_identity_policies(Identity=None):
    """
    :param Identity: [REQUIRED]
            The identity that is associated with the policy for which the policies will be listed. You can specify an identity by using its name or by using its Amazon Resource Name (ARN). Examples: user@example.com , example.com , arn:aws:ses:us-east-1:123456789012:identity/example.com .
            To successfully call this API, you must own the identity.
            Return typedict
            ReturnsResponse Syntax{
              'PolicyNames': [
                'string',
              ]
            }
            Response Structure
            (dict) --A list of names of sending authorization policies that apply to an identity.
            PolicyNames (list) --A list of names of policies that apply to the specified identity.
            (string) --
            
            
    :type Identity: string
    """
    pass


def list_receipt_filters():
    """
    """
    pass


def list_receipt_rule_sets(NextToken=None):
    """
    :param NextToken: A token returned from a previous call to ListReceiptRuleSets to indicate the position in the receipt rule set list.
            Return typedict
            ReturnsResponse Syntax{
              'RuleSets': [
                {
                  'Name': 'string',
                  'CreatedTimestamp': datetime(2015, 1, 1)
                },
              ],
              'NextToken': 'string'
            }
            Response Structure
            (dict) --A list of receipt rule sets that exist under your AWS account.
            RuleSets (list) --The metadata for the currently active receipt rule set. The metadata consists of the rule set name and the timestamp of when the rule set was created.
            (dict) --Information about a receipt rule set.
            A receipt rule set is a collection of rules that specify what Amazon SES should do with mail it receives on behalf of your account's verified domains.
            For information about setting up receipt rule sets, see the Amazon SES Developer Guide .
            Name (string) --The name of the receipt rule set. The name must:
            Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (_), or dashes (-).
            Start and end with a letter or number.
            Contain less than 64 characters.
            CreatedTimestamp (datetime) --The date and time the receipt rule set was created.
            
            NextToken (string) --A token indicating that there are additional receipt rule sets available to be listed. Pass this token to successive calls of ListReceiptRuleSets to retrieve up to 100 receipt rule sets at a time.
            
            
    :type NextToken: string
    """
    pass


def list_verified_email_addresses():
    """
    """
    pass


def put_identity_policy(Identity=None, PolicyName=None, Policy=None):
    """
    :param Identity: [REQUIRED]
            The identity to which the policy will apply. You can specify an identity by using its name or by using its Amazon Resource Name (ARN). Examples: user@example.com , example.com , arn:aws:ses:us-east-1:123456789012:identity/example.com .
            To successfully call this API, you must own the identity.
            
    :type Identity: string
    :param PolicyName: [REQUIRED]
            The name of the policy.
            The policy name cannot exceed 64 characters and can only include alphanumeric characters, dashes, and underscores.
            
    :type PolicyName: string
    :param Policy: [REQUIRED]
            The text of the policy in JSON format. The policy cannot exceed 4 KB.
            For information about the syntax of sending authorization policies, see the Amazon SES Developer Guide .
            
    :type Policy: string
    """
    pass


def reorder_receipt_rule_set(RuleSetName=None, RuleNames=None):
    """
    :param RuleSetName: [REQUIRED]
            The name of the receipt rule set to reorder.
            
    :type RuleSetName: string
    :param RuleNames: [REQUIRED]
            A list of the specified receipt rule set's receipt rules in the order that you want to put them.
            (string) --
            
    :type RuleNames: list
    """
    pass


def send_bounce(OriginalMessageId=None, BounceSender=None, Explanation=None, MessageDsn=None,
                BouncedRecipientInfoList=None, BounceSenderArn=None):
    """
    :param OriginalMessageId: [REQUIRED]
            The message ID of the message to be bounced.
            
    :type OriginalMessageId: string
    :param BounceSender: [REQUIRED]
            The address to use in the 'From' header of the bounce message. This must be an identity that you have verified with Amazon SES.
            
    :type BounceSender: string
    :param Explanation: Human-readable text for the bounce message to explain the failure. If not specified, the text will be auto-generated based on the bounced recipient information.
    :type Explanation: string
    :param MessageDsn: Message-related DSN fields. If not specified, Amazon SES will choose the values.
            ReportingMta (string) -- [REQUIRED]The reporting MTA that attempted to deliver the message, formatted as specified in RFC 3464 (mta-name-type; mta-name ). The default value is dns; inbound-smtp.[region].amazonaws.com .
            ArrivalDate (datetime) --When the message was received by the reporting mail transfer agent (MTA), in RFC 822 date-time format.
            ExtensionFields (list) --Additional X-headers to include in the DSN.
            (dict) --Additional X-headers to include in the Delivery Status Notification (DSN) when an email that Amazon SES receives on your behalf bounces.
            For information about receiving email through Amazon SES, see the Amazon SES Developer Guide .
            Name (string) -- [REQUIRED]The name of the header to add. Must be between 1 and 50 characters, inclusive, and consist of alphanumeric (a-z, A-Z, 0-9) characters and dashes only.
            Value (string) -- [REQUIRED]The value of the header to add. Must be less than 2048 characters, and must not contain newline characters ('r' or 'n').
            
            
    :type MessageDsn: dict
    :param BouncedRecipientInfoList: [REQUIRED]
            A list of recipients of the bounced message, including the information required to create the Delivery Status Notifications (DSNs) for the recipients. You must specify at least one BouncedRecipientInfo in the list.
            (dict) --Recipient-related information to include in the Delivery Status Notification (DSN) when an email that Amazon SES receives on your behalf bounces.
            For information about receiving email through Amazon SES, see the Amazon SES Developer Guide .
            Recipient (string) -- [REQUIRED]The email address of the recipient of the bounced email.
            RecipientArn (string) --This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to receive email for the recipient of the bounced email. For more information about sending authorization, see the Amazon SES Developer Guide .
            BounceType (string) --The reason for the bounce. You must provide either this parameter or RecipientDsnFields .
            RecipientDsnFields (dict) --Recipient-related DSN fields, most of which would normally be filled in automatically when provided with a BounceType . You must provide either this parameter or BounceType .
            FinalRecipient (string) --The email address to which the message was ultimately delivered. This corresponds to the Final-Recipient in the DSN. If not specified, FinalRecipient will be set to the Recipient specified in the BouncedRecipientInfo structure. Either FinalRecipient or the recipient in BouncedRecipientInfo must be a recipient of the original bounced message.
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
            
            
            
    :type BouncedRecipientInfoList: list
    :param BounceSenderArn: This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the address in the 'From' header of the bounce. For more information about sending authorization, see the Amazon SES Developer Guide .
    :type BounceSenderArn: string
    """
    pass


def send_email(Source=None, Destination=None, Message=None, ReplyToAddresses=None, ReturnPath=None, SourceArn=None,
               ReturnPathArn=None):
    """
    :param Source: [REQUIRED]
            The email address that is sending the email. This email address must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES. For information about verifying identities, see the Amazon SES Developer Guide .
            If you are sending on behalf of another user and have been permitted to do so by a sending authorization policy, then you must also specify the SourceArn parameter. For more information about sending authorization, see the Amazon SES Developer Guide .
            In all cases, the email address must be 7-bit ASCII. If the text must contain any other characters, then you must use MIME encoded-word syntax (RFC 2047) instead of a literal string. MIME encoded-word syntax uses the following form: =?charset?encoding?encoded-text?= . For more information, see RFC 2047 .
            
    :type Source: string
    :param Destination: [REQUIRED]
            The destination for this email, composed of To:, CC:, and BCC: fields.
            ToAddresses (list) --The To: field(s) of the message.
            (string) --
            CcAddresses (list) --The CC: field(s) of the message.
            (string) --
            BccAddresses (list) --The BCC: field(s) of the message.
            (string) --
            
    :type Destination: dict
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
            
            
    :type Message: dict
    :param ReplyToAddresses: The reply-to email address(es) for the message. If the recipient replies to the message, each reply-to address will receive the reply.
            (string) --
            
    :type ReplyToAddresses: list
    :param ReturnPath: The email address to which bounces and complaints are to be forwarded when feedback forwarding is enabled. If the message cannot be delivered to the recipient, then an error message will be returned from the recipient's ISP; this message will then be forwarded to the email address specified by the ReturnPath parameter. The ReturnPath parameter is never overwritten. This email address must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES.
    :type ReturnPath: string
    :param SourceArn: This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to send for the email address specified in the Source parameter.
            For example, if the owner of example.com (which has ARN arn:aws:ses:us-east-1:123456789012:identity/example.com ) attaches a policy to it that authorizes you to send from user@example.com , then you would specify the SourceArn to be arn:aws:ses:us-east-1:123456789012:identity/example.com , and the Source to be user@example.com .
            For more information about sending authorization, see the Amazon SES Developer Guide .
            
    :type SourceArn: string
    :param ReturnPathArn: This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the email address specified in the ReturnPath parameter.
            For example, if the owner of example.com (which has ARN arn:aws:ses:us-east-1:123456789012:identity/example.com ) attaches a policy to it that authorizes you to use feedback@example.com , then you would specify the ReturnPathArn to be arn:aws:ses:us-east-1:123456789012:identity/example.com , and the ReturnPath to be feedback@example.com .
            For more information about sending authorization, see the Amazon SES Developer Guide .
            
    :type ReturnPathArn: string
    """
    pass


def send_raw_email(Source=None, Destinations=None, RawMessage=None, FromArn=None, SourceArn=None, ReturnPathArn=None):
    """
    :param Source: The identity's email address. If you do not provide a value for this parameter, you must specify a 'From' address in the raw text of the message. (You can also specify both.)
            By default, the string must be 7-bit ASCII. If the text must contain any other characters, then you must use MIME encoded-word syntax (RFC 2047) instead of a literal string. MIME encoded-word syntax uses the following form: =?charset?encoding?encoded-text?= . For more information, see RFC 2047 .
            Note
            If you specify the Source parameter and have feedback forwarding enabled, then bounces and complaints will be sent to this email address. This takes precedence over any Return-Path header that you might include in the raw text of the message.
            
    :type Source: string
    :param Destinations: A list of destinations for the message, consisting of To:, CC:, and BCC: addresses.
            (string) --
            
    :type Destinations: list
    :param RawMessage: [REQUIRED]
            The raw text of the message. The client is responsible for ensuring the following:
            Message must contain a header and a body, separated by a blank line.
            All required header fields must be present.
            Each part of a multipart MIME message must be formatted properly.
            MIME content types must be among those supported by Amazon SES. For more information, go to the Amazon SES Developer Guide .
            Must be base64-encoded.
            Data (bytes) -- [REQUIRED]The raw data of the message. The client must ensure that the message format complies with Internet email standards regarding email header fields, MIME types, MIME encoding, and base64 encoding.
            The To:, CC:, and BCC: headers in the raw message can contain a group list.
            If you are using SendRawEmail with sending authorization, you can include X-headers in the raw message to specify the 'Source,' 'From,' and 'Return-Path' addresses. For more information, see the documentation for SendRawEmail .
            Warning
            Do not include these X-headers in the DKIM signature, because they are removed by Amazon SES before sending the email.
            For more information, go to the Amazon SES Developer Guide .
            
    :type RawMessage: dict
    :param FromArn: This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to specify a particular 'From' address in the header of the raw email.
            Instead of using this parameter, you can use the X-header X-SES-FROM-ARN in the raw message of the email. If you use both the FromArn parameter and the corresponding X-header, Amazon SES uses the value of the FromArn parameter.
            Note
            For information about when to use this parameter, see the description of SendRawEmail in this guide, or see the Amazon SES Developer Guide .
            
    :type FromArn: string
    :param SourceArn: This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to send for the email address specified in the Source parameter.
            For example, if the owner of example.com (which has ARN arn:aws:ses:us-east-1:123456789012:identity/example.com ) attaches a policy to it that authorizes you to send from user@example.com , then you would specify the SourceArn to be arn:aws:ses:us-east-1:123456789012:identity/example.com , and the Source to be user@example.com .
            Instead of using this parameter, you can use the X-header X-SES-SOURCE-ARN in the raw message of the email. If you use both the SourceArn parameter and the corresponding X-header, Amazon SES uses the value of the SourceArn parameter.
            Note
            For information about when to use this parameter, see the description of SendRawEmail in this guide, or see the Amazon SES Developer Guide .
            
    :type SourceArn: string
    :param ReturnPathArn: This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the email address specified in the ReturnPath parameter.
            For example, if the owner of example.com (which has ARN arn:aws:ses:us-east-1:123456789012:identity/example.com ) attaches a policy to it that authorizes you to use feedback@example.com , then you would specify the ReturnPathArn to be arn:aws:ses:us-east-1:123456789012:identity/example.com , and the ReturnPath to be feedback@example.com .
            Instead of using this parameter, you can use the X-header X-SES-RETURN-PATH-ARN in the raw message of the email. If you use both the ReturnPathArn parameter and the corresponding X-header, Amazon SES uses the value of the ReturnPathArn parameter.
            Note
            For information about when to use this parameter, see the description of SendRawEmail in this guide, or see the Amazon SES Developer Guide .
            
    :type ReturnPathArn: string
    """
    pass


def set_active_receipt_rule_set(RuleSetName=None):
    """
    :param RuleSetName: The name of the receipt rule set to make active. Setting this value to null disables all email receiving.
            Return typedict
            ReturnsResponse Syntax{}
            Response Structure
            (dict) --An empty element returned on a successful request.
            
            
    :type RuleSetName: string
    """
    pass


def set_identity_dkim_enabled(Identity=None, DkimEnabled=None):
    """
    :param Identity: [REQUIRED]
            The identity for which DKIM signing should be enabled or disabled.
            
    :type Identity: string
    :param DkimEnabled: [REQUIRED]
            Sets whether DKIM signing is enabled for an identity. Set to true to enable DKIM signing for this identity; false to disable it.
            
    :type DkimEnabled: boolean
    """
    pass


def set_identity_feedback_forwarding_enabled(Identity=None, ForwardingEnabled=None):
    """
    :param Identity: [REQUIRED]
            The identity for which to set bounce and complaint notification forwarding. Examples: user@example.com , example.com .
            
    :type Identity: string
    :param ForwardingEnabled: [REQUIRED]
            Sets whether Amazon SES will forward bounce and complaint notifications as email. true specifies that Amazon SES will forward bounce and complaint notifications as email, in addition to any Amazon SNS topic publishing otherwise specified. false specifies that Amazon SES will publish bounce and complaint notifications only through Amazon SNS. This value can only be set to false when Amazon SNS topics are set for both Bounce and Complaint notification types.
            
    :type ForwardingEnabled: boolean
    """
    pass


def set_identity_headers_in_notifications_enabled(Identity=None, NotificationType=None, Enabled=None):
    """
    :param Identity: [REQUIRED]
            The identity for which to enable or disable headers in notifications. Examples: user@example.com , example.com .
            
    :type Identity: string
    :param NotificationType: [REQUIRED]
            The notification type for which to enable or disable headers in notifications.
            
    :type NotificationType: string
    :param Enabled: [REQUIRED]
            Sets whether Amazon SES includes the original email headers in Amazon SNS notifications of the specified notification type. A value of true specifies that Amazon SES will include headers in notifications, and a value of false specifies that Amazon SES will not include headers in notifications.
            This value can only be set when NotificationType is already set to use a particular Amazon SNS topic.
            
    :type Enabled: boolean
    """
    pass


def set_identity_mail_from_domain(Identity=None, MailFromDomain=None, BehaviorOnMXFailure=None):
    """
    :param Identity: [REQUIRED]
            The verified identity for which you want to enable or disable the specified custom MAIL FROM domain.
            
    :type Identity: string
    :param MailFromDomain: The custom MAIL FROM domain that you want the verified identity to use. The MAIL FROM domain must 1) be a subdomain of the verified identity, 2) not be used in a 'From' address if the MAIL FROM domain is the destination of email feedback forwarding (for more information, see the Amazon SES Developer Guide ), and 3) not be used to receive emails. A value of null disables the custom MAIL FROM setting for the identity.
    :type MailFromDomain: string
    :param BehaviorOnMXFailure: The action that you want Amazon SES to take if it cannot successfully read the required MX record when you send an email. If you choose UseDefaultValue , Amazon SES will use amazonses.com (or a subdomain of that) as the MAIL FROM domain. If you choose RejectMessage , Amazon SES will return a MailFromDomainNotVerified error and not send the email.
            The action specified in BehaviorOnMXFailure is taken when the custom MAIL FROM domain setup is in the Pending , Failed , and TemporaryFailure states.
            
    :type BehaviorOnMXFailure: string
    """
    pass


def set_identity_notification_topic(Identity=None, NotificationType=None, SnsTopic=None):
    """
    :param Identity: [REQUIRED]
            The identity for which the Amazon SNS topic will be set. You can specify an identity by using its name or by using its Amazon Resource Name (ARN). Examples: user@example.com , example.com , arn:aws:ses:us-east-1:123456789012:identity/example.com .
            
    :type Identity: string
    :param NotificationType: [REQUIRED]
            The type of notifications that will be published to the specified Amazon SNS topic.
            
    :type NotificationType: string
    :param SnsTopic: The Amazon Resource Name (ARN) of the Amazon SNS topic. If the parameter is omitted from the request or a null value is passed, SnsTopic is cleared and publishing is disabled.
    :type SnsTopic: string
    """
    pass


def set_receipt_rule_position(RuleSetName=None, RuleName=None, After=None):
    """
    :param RuleSetName: [REQUIRED]
            The name of the receipt rule set that contains the receipt rule to reposition.
            
    :type RuleSetName: string
    :param RuleName: [REQUIRED]
            The name of the receipt rule to reposition.
            
    :type RuleName: string
    :param After: The name of the receipt rule after which to place the specified receipt rule.
    :type After: string
    """
    pass


def update_receipt_rule(RuleSetName=None, Rule=None):
    """
    :param RuleSetName: [REQUIRED]
            The name of the receipt rule set to which the receipt rule belongs.
            
    :type RuleSetName: string
    :param Rule: [REQUIRED]
            A data structure that contains the updated receipt rule information.
            Name (string) -- [REQUIRED]The name of the receipt rule. The name must:
            Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (_), or dashes (-).
            Start and end with a letter or number.
            Contain less than 64 characters.
            Enabled (boolean) --If true , the receipt rule is active. The default value is false .
            TlsPolicy (string) --Specifies whether Amazon SES should require that incoming email is delivered over a connection encrypted with Transport Layer Security (TLS). If this parameter is set to Require , Amazon SES will bounce emails that are not received over TLS. The default is Optional .
            Recipients (list) --The recipient domains and email addresses to which the receipt rule applies. If this field is not specified, this rule will match all recipients under all verified domains.
            (string) --
            Actions (list) --An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule.
            (dict) --An action that Amazon SES can take when it receives an email on behalf of one or more email addresses or domains that you own. An instance of this data type can represent only one action.
            For information about setting up receipt rules, see the Amazon SES Developer Guide .
            S3Action (dict) --Saves the received message to an Amazon Simple Storage Service (Amazon S3) bucket and, optionally, publishes a notification to Amazon SNS.
            TopicArn (string) --The ARN of the Amazon SNS topic to notify when the message is saved to the Amazon S3 bucket. An example of an Amazon SNS topic ARN is arn:aws:sns:us-west-2:123456789012:MyTopic . For more information about Amazon SNS topics, see the Amazon SNS Developer Guide .
            BucketName (string) -- [REQUIRED]The name of the Amazon S3 bucket to which to save the received email.
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
            Scope (string) -- [REQUIRED]The scope to which the Stop action applies. That is, what is being stopped.
            TopicArn (string) --The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the stop action is taken. An example of an Amazon SNS topic ARN is arn:aws:sns:us-west-2:123456789012:MyTopic . For more information about Amazon SNS topics, see the Amazon SNS Developer Guide .
            AddHeaderAction (dict) --Adds a header to the received email.
            HeaderName (string) -- [REQUIRED]The name of the header to add. Must be between 1 and 50 characters, inclusive, and consist of alphanumeric (a-z, A-Z, 0-9) characters and dashes only.
            HeaderValue (string) -- [REQUIRED]Must be less than 2048 characters, and must not contain newline characters ('r' or 'n').
            SNSAction (dict) --Publishes the email content within a notification to Amazon SNS.
            TopicArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the Amazon SNS topic to notify. An example of an Amazon SNS topic ARN is arn:aws:sns:us-west-2:123456789012:MyTopic . For more information about Amazon SNS topics, see the Amazon SNS Developer Guide .
            Encoding (string) --The encoding to use for the email within the Amazon SNS notification. UTF-8 is easier to use, but may not preserve all special characters when a message was encoded with a different encoding format. Base64 preserves all special characters. The default value is UTF-8.
            
            ScanEnabled (boolean) --If true , then messages to which this receipt rule applies are scanned for spam and viruses. The default value is false .
            
    :type Rule: dict
    """
    pass


def verify_domain_dkim(Domain=None):
    """
    :param Domain: [REQUIRED]
            The name of the domain to be verified for Easy DKIM signing.
            Return typedict
            ReturnsResponse Syntax{
              'DkimTokens': [
                'string',
              ]
            }
            Response Structure
            (dict) --Returns CNAME records that you must publish to the DNS server of your domain to set up Easy DKIM with Amazon SES.
            DkimTokens (list) --A set of character strings that represent the domain's identity. If the identity is an email address, the tokens represent the domain of that address.
            Using these tokens, you will need to create DNS CNAME records that point to DKIM public keys hosted by Amazon SES. Amazon Web Services will eventually detect that you have updated your DNS records; this detection process may take up to 72 hours. Upon successful detection, Amazon SES will be able to DKIM-sign emails originating from that domain.
            For more information about creating DNS records using DKIM tokens, go to the Amazon SES Developer Guide .
            (string) --
            
            
    :type Domain: string
    """
    pass


def verify_domain_identity(Domain=None):
    """
    :param Domain: [REQUIRED]
            The domain to be verified.
            Return typedict
            ReturnsResponse Syntax{
              'VerificationToken': 'string'
            }
            Response Structure
            (dict) --Returns a TXT record that you must publish to the DNS server of your domain to complete domain verification with Amazon SES.
            VerificationToken (string) --A TXT record that must be placed in the DNS settings for the domain, in order to complete domain verification.
            
            
    :type Domain: string
    """
    pass


def verify_email_address(EmailAddress=None):
    """
    :param EmailAddress: [REQUIRED]
            The email address to be verified.
            ReturnsNone
            
    :type EmailAddress: string
    """
    pass


def verify_email_identity(EmailAddress=None):
    """
    :param EmailAddress: [REQUIRED]
            The email address to be verified.
            Return typedict
            ReturnsResponse Syntax{}
            Response Structure
            (dict) --An empty element returned on a successful request.
            
            
    :type EmailAddress: string
    """
    pass
