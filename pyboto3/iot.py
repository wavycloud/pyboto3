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


def accept_certificate_transfer(certificateId=None, setAsActive=None):
    """
    :param certificateId: [REQUIRED]
            The ID of the certificate.
            
    :type certificateId: string
    :param setAsActive: Specifies whether the certificate is active.
    :type setAsActive: boolean
    """
    pass


def attach_principal_policy(policyName=None, principal=None):
    """
    :param policyName: [REQUIRED]
            The policy name.
            
    :type policyName: string
    :param principal: [REQUIRED]
            The principal, which can be a certificate ARN (as returned from the CreateCertificate operation) or an Amazon Cognito ID.
            
    :type principal: string
    """
    pass


def attach_thing_principal(thingName=None, principal=None):
    """
    :param thingName: [REQUIRED]
            The name of the thing.
            
    :type thingName: string
    :param principal: [REQUIRED]
            The principal, such as a certificate or other credential.
            
    :type principal: string
    """
    pass


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


def cancel_certificate_transfer(certificateId=None):
    """
    :param certificateId: [REQUIRED]
            The ID of the certificate.
            ReturnsNone
            
    :type certificateId: string
    """
    pass


def create_certificate_from_csr(certificateSigningRequest=None, setAsActive=None):
    """
    :param certificateSigningRequest: [REQUIRED]
            The certificate signing request (CSR).
            
    :type certificateSigningRequest: string
    :param setAsActive: Specifies whether the certificate is active.
    :type setAsActive: boolean
    """
    pass


def create_keys_and_certificate(setAsActive=None):
    """
    :param setAsActive: Specifies whether the certificate is active.
            Return typedict
            ReturnsResponse Syntax{
              'certificateArn': 'string',
              'certificateId': 'string',
              'certificatePem': 'string',
              'keyPair': {
                'PublicKey': 'string',
                'PrivateKey': 'string'
              }
            }
            Response Structure
            (dict) --The output of the CreateKeysAndCertificate operation.
            certificateArn (string) --The ARN of the certificate.
            certificateId (string) --The ID of the certificate. AWS IoT issues a default subject name for the certificate (for example, AWS IoT Certificate).
            certificatePem (string) --The certificate data, in PEM format.
            keyPair (dict) --The generated key pair.
            PublicKey (string) --The public key.
            PrivateKey (string) --The private key.
            
            
            
    :type setAsActive: boolean
    """
    pass


def create_policy(policyName=None, policyDocument=None):
    """
    :param policyName: [REQUIRED]
            The policy name.
            
    :type policyName: string
    :param policyDocument: [REQUIRED]
            The JSON document that describes the policy. policyDocument must have a minimum length of 1, with a maximum length of 2048, excluding whitespace.
            
    :type policyDocument: string
    """
    pass


def create_policy_version(policyName=None, policyDocument=None, setAsDefault=None):
    """
    :param policyName: [REQUIRED]
            The policy name.
            
    :type policyName: string
    :param policyDocument: [REQUIRED]
            The JSON document that describes the policy. Minimum length of 1. Maximum length of 2048, excluding whitespaces
            
    :type policyDocument: string
    :param setAsDefault: Specifies whether the policy version is set as the default. When this parameter is true, the new policy version becomes the operative version (that is, the version that is in effect for the certificates to which the policy is attached).
    :type setAsDefault: boolean
    """
    pass


def create_thing(thingName=None, thingTypeName=None, attributePayload=None):
    """
    :param thingName: [REQUIRED]
            The name of the thing to create.
            
    :type thingName: string
    :param thingTypeName: The name of the thing type associated with the new thing.
    :type thingTypeName: string
    :param attributePayload: The attribute payload, which consists of up to three name/value pairs in a JSON document. For example:
            {\'attributes\':{\'string1\':\'string2\'}})
            attributes (dict) --A JSON string containing up to three key-value pair in JSON format. For example:
            {\'attributes\':{\'string1\':\'string2\'}})
            (string) --
            (string) -- An attribute value for an Thing. An empty or null value in Update means that existing value for that attribute should be deleted. Empty and null values in create are ignored.
            
            merge (boolean) --Specifies whether the list of attributes provided in the AttributePayload is merged with the attributes stored in the registry, instead of overwriting them.
            To remove an attribute, call UpdateThing with an empty attribute value.
            Note
            The merge attribute is only valid when calling UpdateThing .
            
    :type attributePayload: dict
    """
    pass


def create_thing_type(thingTypeName=None, thingTypeProperties=None):
    """
    :param thingTypeName: [REQUIRED]
            The name of the thing type.
            
    :type thingTypeName: string
    :param thingTypeProperties: The ThingTypeProperties for the thing type to create. It contains information about the new thing type including a description, and a list of searchable thing attribute names.
            thingTypeDescription (string) --The description of the thing type.
            searchableAttributes (list) --A list of searchable thing attribute names.
            (string) --
            
    :type thingTypeProperties: dict
    """
    pass


def create_topic_rule(ruleName=None, topicRulePayload=None):
    """
    :param ruleName: [REQUIRED]
            The name of the rule.
            
    :type ruleName: string
    :param topicRulePayload: [REQUIRED]
            The rule payload.
            sql (string) -- [REQUIRED]The SQL statement used to query the topic. For more information, see AWS IoT SQL Reference in the AWS IoT Developer Guide .
            description (string) --The description of the rule.
            actions (list) -- [REQUIRED]The actions associated with the rule.
            (dict) --Describes the actions associated with a rule.
            dynamoDB (dict) --Write to a DynamoDB table.
            tableName (string) -- [REQUIRED]The name of the DynamoDB table.
            roleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access to the DynamoDB table.
            operation (string) --The type of operation to be performed. This follows the substitution template, so it can be ${operation} , but the substitution must result in one of the following: INSERT , UPDATE , or DELETE .
            hashKeyField (string) -- [REQUIRED]The hash key name.
            hashKeyValue (string) -- [REQUIRED]The hash key value.
            hashKeyType (string) --The hash key type. Valid values are 'STRING' or 'NUMBER'
            rangeKeyField (string) --The range key name.
            rangeKeyValue (string) --The range key value.
            rangeKeyType (string) --The range key type. Valid values are 'STRING' or 'NUMBER'
            payloadField (string) --The action payload. This name can be customized.
            dynamoDBv2 (dict) --Write to a DynamoDB table. This is a new version of the DynamoDB action. It allows you to write each attribute in an MQTT message payload into a separate DynamoDB column.
            roleArn (string) --The ARN of the IAM role that grants access to the DynamoDB table.
            putItem (dict) --Specifies the DynamoDB table to which the message data will be written. For example:
            { 'dynamoDBv2': { 'roleArn': 'aws:iam:12341251:my-role' 'putItem': { 'tableName': 'my-table' } } }
            Each attribute in the message payload will be written to a separate column in the DynamoDB database.
            tableName (string) -- [REQUIRED]The table where the message data will be written
            
            lambda (dict) --Invoke a Lambda function.
            functionArn (string) -- [REQUIRED]The ARN of the Lambda function.
            sns (dict) --Publish to an Amazon SNS topic.
            targetArn (string) -- [REQUIRED]The ARN of the SNS topic.
            roleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access.
            messageFormat (string) --The message format of the message to publish. Optional. Accepted values are 'JSON' and 'RAW'. The default value of the attribute is 'RAW'. SNS uses this setting to determine if the payload should be parsed and relevant platform-specific bits of the payload should be extracted. To read more about SNS message formats, see http://docs.aws.amazon.com/sns/latest/dg/json-formats.html refer to their official documentation.
            sqs (dict) --Publish to an Amazon SQS queue.
            roleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access.
            queueUrl (string) -- [REQUIRED]The URL of the Amazon SQS queue.
            useBase64 (boolean) --Specifies whether to use Base64 encoding.
            kinesis (dict) --Write data to an Amazon Kinesis stream.
            roleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access to the Amazon Kinesis stream.
            streamName (string) -- [REQUIRED]The name of the Amazon Kinesis stream.
            partitionKey (string) --The partition key.
            republish (dict) --Publish to another MQTT topic.
            roleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access.
            topic (string) -- [REQUIRED]The name of the MQTT topic.
            s3 (dict) --Write to an Amazon S3 bucket.
            roleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access.
            bucketName (string) -- [REQUIRED]The Amazon S3 bucket.
            key (string) -- [REQUIRED]The object key.
            cannedAcl (string) --The Amazon S3 canned ACL that controls access to the object identified by the object key. For more information, see S3 canned ACLs .
            firehose (dict) --Write to an Amazon Kinesis Firehose stream.
            roleArn (string) -- [REQUIRED]The IAM role that grants access to the Amazon Kinesis Firehost stream.
            deliveryStreamName (string) -- [REQUIRED]The delivery stream name.
            separator (string) --A character separator that will be used to separate records written to the Firehose stream. Valid values are: 'n' (newline), 't' (tab), 'rn' (Windows newline), ',' (comma).
            cloudwatchMetric (dict) --Capture a CloudWatch metric.
            roleArn (string) -- [REQUIRED]The IAM role that allows access to the CloudWatch metric.
            metricNamespace (string) -- [REQUIRED]The CloudWatch metric namespace name.
            metricName (string) -- [REQUIRED]The CloudWatch metric name.
            metricValue (string) -- [REQUIRED]The CloudWatch metric value.
            metricUnit (string) -- [REQUIRED]The metric unit supported by CloudWatch.
            metricTimestamp (string) --An optional Unix timestamp .
            cloudwatchAlarm (dict) --Change the state of a CloudWatch alarm.
            roleArn (string) -- [REQUIRED]The IAM role that allows access to the CloudWatch alarm.
            alarmName (string) -- [REQUIRED]The CloudWatch alarm name.
            stateReason (string) -- [REQUIRED]The reason for the alarm change.
            stateValue (string) -- [REQUIRED]The value of the alarm state. Acceptable values are: OK, ALARM, INSUFFICIENT_DATA.
            elasticsearch (dict) --Write data to an Amazon Elasticsearch Service domain.
            roleArn (string) -- [REQUIRED]The IAM role ARN that has access to Elasticsearch.
            endpoint (string) -- [REQUIRED]The endpoint of your Elasticsearch domain.
            index (string) -- [REQUIRED]The Elasticsearch index where you want to store your data.
            type (string) -- [REQUIRED]The type of document you are storing.
            id (string) -- [REQUIRED]The unique identifier for the document you are storing.
            
            ruleDisabled (boolean) --Specifies whether the rule is disabled.
            awsIotSqlVersion (string) --The version of the SQL rules engine to use when evaluating the rule.
            
    :type topicRulePayload: dict
    """
    pass


def delete_ca_certificate(certificateId=None):
    """
    :param certificateId: [REQUIRED]
            The ID of the certificate to delete.
            Return typedict
            ReturnsResponse Syntax{}
            Response Structure
            (dict) --The output for the DeleteCACertificate operation.
            
            
    :type certificateId: string
    """
    pass


def delete_certificate(certificateId=None):
    """
    :param certificateId: [REQUIRED]
            The ID of the certificate.
            ReturnsNone
            
    :type certificateId: string
    """
    pass


def delete_policy(policyName=None):
    """
    :param policyName: [REQUIRED]
            The name of the policy to delete.
            ReturnsNone
            
    :type policyName: string
    """
    pass


def delete_policy_version(policyName=None, policyVersionId=None):
    """
    :param policyName: [REQUIRED]
            The name of the policy.
            
    :type policyName: string
    :param policyVersionId: [REQUIRED]
            The policy version ID.
            
    :type policyVersionId: string
    """
    pass


def delete_registration_code():
    """
    """
    pass


def delete_thing(thingName=None, expectedVersion=None):
    """
    :param thingName: [REQUIRED]
            The name of the thing to delete.
            
    :type thingName: string
    :param expectedVersion: The expected version of the thing record in the registry. If the version of the record in the registry does not match the expected version specified in the request, the DeleteThing request is rejected with a VersionConflictException .
    :type expectedVersion: integer
    """
    pass


def delete_thing_type(thingTypeName=None):
    """
    :param thingTypeName: [REQUIRED]
            The name of the thing type.
            Return typedict
            ReturnsResponse Syntax{}
            Response Structure
            (dict) --The output for the DeleteThingType operation.
            
            
    :type thingTypeName: string
    """
    pass


def delete_topic_rule(ruleName=None):
    """
    :param ruleName: [REQUIRED]
            The name of the rule.
            ReturnsNone
            
    :type ruleName: string
    """
    pass


def deprecate_thing_type(thingTypeName=None, undoDeprecate=None):
    """
    :param thingTypeName: [REQUIRED]
            The name of the thing type to deprecate.
            
    :type thingTypeName: string
    :param undoDeprecate: Whether to undeprecate a deprecated thing type. If true , the thing type will not be deprecated anymore and you can associate it with things.
    :type undoDeprecate: boolean
    """
    pass


def describe_ca_certificate(certificateId=None):
    """
    :param certificateId: [REQUIRED]
            The CA certificate identifier.
            Return typedict
            ReturnsResponse Syntax{
              'certificateDescription': {
                'certificateArn': 'string',
                'certificateId': 'string',
                'status': 'ACTIVE'|'INACTIVE',
                'certificatePem': 'string',
                'ownedBy': 'string',
                'creationDate': datetime(2015, 1, 1),
                'autoRegistrationStatus': 'ENABLE'|'DISABLE'
              }
            }
            Response Structure
            (dict) --The output from the DescribeCACertificate operation.
            certificateDescription (dict) --The CA certificate description.
            certificateArn (string) --The CA certificate ARN.
            certificateId (string) --The CA certificate ID.
            status (string) --The status of a CA certificate.
            certificatePem (string) --The CA certificate data, in PEM format.
            ownedBy (string) --The owner of the CA certificate.
            creationDate (datetime) --The date the CA certificate was created.
            autoRegistrationStatus (string) --Whether the CA certificate configured for auto registration of device certificates. Valid values are 'ENABLE' and 'DISABLE'
            
            
            
    :type certificateId: string
    """
    pass


def describe_certificate(certificateId=None):
    """
    :param certificateId: [REQUIRED]
            The ID of the certificate.
            Return typedict
            ReturnsResponse Syntax{
              'certificateDescription': {
                'certificateArn': 'string',
                'certificateId': 'string',
                'caCertificateId': 'string',
                'status': 'ACTIVE'|'INACTIVE'|'REVOKED'|'PENDING_TRANSFER'|'REGISTER_INACTIVE'|'PENDING_ACTIVATION',
                'certificatePem': 'string',
                'ownedBy': 'string',
                'previousOwnedBy': 'string',
                'creationDate': datetime(2015, 1, 1),
                'lastModifiedDate': datetime(2015, 1, 1),
                'transferData': {
                  'transferMessage': 'string',
                  'rejectReason': 'string',
                  'transferDate': datetime(2015, 1, 1),
                  'acceptDate': datetime(2015, 1, 1),
                  'rejectDate': datetime(2015, 1, 1)
                }
              }
            }
            Response Structure
            (dict) --The output of the DescribeCertificate operation.
            certificateDescription (dict) --The description of the certificate.
            certificateArn (string) --The ARN of the certificate.
            certificateId (string) --The ID of the certificate.
            caCertificateId (string) --The certificate ID of the CA certificate used to sign this certificate.
            status (string) --The status of the certificate.
            certificatePem (string) --The certificate data, in PEM format.
            ownedBy (string) --The ID of the AWS account that owns the certificate.
            previousOwnedBy (string) --The ID of the AWS account of the previous owner of the certificate.
            creationDate (datetime) --The date and time the certificate was created.
            lastModifiedDate (datetime) --The date and time the certificate was last modified.
            transferData (dict) --The transfer data.
            transferMessage (string) --The transfer message.
            rejectReason (string) --The reason why the transfer was rejected.
            transferDate (datetime) --The date the transfer took place.
            acceptDate (datetime) --The date the transfer was accepted.
            rejectDate (datetime) --The date the transfer was rejected.
            
            
            
    :type certificateId: string
    """
    pass


def describe_endpoint():
    """
    """
    pass


def describe_thing(thingName=None):
    """
    :param thingName: [REQUIRED]
            The name of the thing.
            Return typedict
            ReturnsResponse Syntax{
              'defaultClientId': 'string',
              'thingName': 'string',
              'thingTypeName': 'string',
              'attributes': {
                'string': 'string'
              },
              'version': 123
            }
            Response Structure
            (dict) --The output from the DescribeThing operation.
            defaultClientId (string) --The default client ID.
            thingName (string) --The name of the thing.
            thingTypeName (string) --The thing type name.
            attributes (dict) --The thing attributes.
            (string) --
            (string) -- An attribute value for an Thing. An empty or null value in Update means that existing value for that attribute should be deleted. Empty and null values in create are ignored.
            
            version (integer) --The current version of the thing record in the registry.
            Note
            To avoid unintentional changes to the information in the registry, you can pass the version information in the expectedVersion parameter of the UpdateThing and DeleteThing calls.
            
            
    :type thingName: string
    """
    pass


def describe_thing_type(thingTypeName=None):
    """
    :param thingTypeName: [REQUIRED]
            The name of the thing type.
            Return typedict
            ReturnsResponse Syntax{
              'thingTypeName': 'string',
              'thingTypeProperties': {
                'thingTypeDescription': 'string',
                'searchableAttributes': [
                  'string',
                ]
              },
              'thingTypeMetadata': {
                'deprecated': True|False,
                'deprecationDate': datetime(2015, 1, 1),
                'creationDate': datetime(2015, 1, 1)
              }
            }
            Response Structure
            (dict) --The output for the DescribeThingType operation.
            thingTypeName (string) --The name of the thing type.
            thingTypeProperties (dict) --The ThingTypeProperties contains information about the thing type including description, and a list of searchable thing attribute names.
            thingTypeDescription (string) --The description of the thing type.
            searchableAttributes (list) --A list of searchable thing attribute names.
            (string) --
            
            thingTypeMetadata (dict) --The ThingTypeMetadata contains additional information about the thing type including: creation date and time, a value indicating whether the thing type is deprecated, and a date and time when time was deprecated.
            deprecated (boolean) --Whether the thing type is deprecated. If true , no new things could be associated with this type.
            deprecationDate (datetime) --The date and time when the thing type was deprecated.
            creationDate (datetime) --The date and time when the thing type was created.
            
            
            
    :type thingTypeName: string
    """
    pass


def detach_principal_policy(policyName=None, principal=None):
    """
    :param policyName: [REQUIRED]
            The name of the policy to detach.
            
    :type policyName: string
    :param principal: [REQUIRED]
            The principal.
            If the principal is a certificate, specify the certificate ARN. If the principal is an Amazon Cognito identity, specify the identity ID.
            
    :type principal: string
    """
    pass


def detach_thing_principal(thingName=None, principal=None):
    """
    :param thingName: [REQUIRED]
            The name of the thing.
            
    :type thingName: string
    :param principal: [REQUIRED]
            If the principal is a certificate, this value must be ARN of the certificate. If the principal is an Amazon Cognito identity, this value must be the ID of the Amazon Cognito identity.
            
    :type principal: string
    """
    pass


def disable_topic_rule(ruleName=None):
    """
    :param ruleName: [REQUIRED]
            The name of the rule to disable.
            ReturnsNone
            
    :type ruleName: string
    """
    pass


def enable_topic_rule(ruleName=None):
    """
    :param ruleName: [REQUIRED]
            The name of the topic rule to enable.
            ReturnsNone
            
    :type ruleName: string
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


def get_logging_options():
    """
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


def get_policy(policyName=None):
    """
    :param policyName: [REQUIRED]
            The name of the policy.
            Return typedict
            ReturnsResponse Syntax{
              'policyName': 'string',
              'policyArn': 'string',
              'policyDocument': 'string',
              'defaultVersionId': 'string'
            }
            Response Structure
            (dict) --The output from the GetPolicy operation.
            policyName (string) --The policy name.
            policyArn (string) --The policy ARN.
            policyDocument (string) --The JSON document that describes the policy.
            defaultVersionId (string) --The default policy version ID.
            
            
    :type policyName: string
    """
    pass


def get_policy_version(policyName=None, policyVersionId=None):
    """
    :param policyName: [REQUIRED]
            The name of the policy.
            
    :type policyName: string
    :param policyVersionId: [REQUIRED]
            The policy version ID.
            
    :type policyVersionId: string
    """
    pass


def get_registration_code():
    """
    """
    pass


def get_topic_rule(ruleName=None):
    """
    :param ruleName: [REQUIRED]
            The name of the rule.
            Return typedict
            ReturnsResponse Syntax{
              'ruleArn': 'string',
              'rule': {
                'ruleName': 'string',
                'sql': 'string',
                'description': 'string',
                'createdAt': datetime(2015, 1, 1),
                'actions': [
                  {
                    'dynamoDB': {
                      'tableName': 'string',
                      'roleArn': 'string',
                      'operation': 'string',
                      'hashKeyField': 'string',
                      'hashKeyValue': 'string',
                      'hashKeyType': 'STRING'|'NUMBER',
                      'rangeKeyField': 'string',
                      'rangeKeyValue': 'string',
                      'rangeKeyType': 'STRING'|'NUMBER',
                      'payloadField': 'string'
                    },
                    'dynamoDBv2': {
                      'roleArn': 'string',
                      'putItem': {
                        'tableName': 'string'
                      }
                    },
                    'lambda': {
                      'functionArn': 'string'
                    },
                    'sns': {
                      'targetArn': 'string',
                      'roleArn': 'string',
                      'messageFormat': 'RAW'|'JSON'
                    },
                    'sqs': {
                      'roleArn': 'string',
                      'queueUrl': 'string',
                      'useBase64': True|False
                    },
                    'kinesis': {
                      'roleArn': 'string',
                      'streamName': 'string',
                      'partitionKey': 'string'
                    },
                    'republish': {
                      'roleArn': 'string',
                      'topic': 'string'
                    },
                    's3': {
                      'roleArn': 'string',
                      'bucketName': 'string',
                      'key': 'string',
                      'cannedAcl': 'private'|'public-read'|'public-read-write'|'aws-exec-read'|'authenticated-read'|'bucket-owner-read'|'bucket-owner-full-control'|'log-delivery-write'
                    },
                    'firehose': {
                      'roleArn': 'string',
                      'deliveryStreamName': 'string',
                      'separator': 'string'
                    },
                    'cloudwatchMetric': {
                      'roleArn': 'string',
                      'metricNamespace': 'string',
                      'metricName': 'string',
                      'metricValue': 'string',
                      'metricUnit': 'string',
                      'metricTimestamp': 'string'
                    },
                    'cloudwatchAlarm': {
                      'roleArn': 'string',
                      'alarmName': 'string',
                      'stateReason': 'string',
                      'stateValue': 'string'
                    },
                    'elasticsearch': {
                      'roleArn': 'string',
                      'endpoint': 'string',
                      'index': 'string',
                      'type': 'string',
                      'id': 'string'
                    }
                  },
                ],
                'ruleDisabled': True|False,
                'awsIotSqlVersion': 'string'
              }
            }
            Response Structure
            (dict) --The output from the GetTopicRule operation.
            ruleArn (string) --The rule ARN.
            rule (dict) --The rule.
            ruleName (string) --The name of the rule.
            sql (string) --The SQL statement used to query the topic. When using a SQL query with multiple lines, be sure to escape the newline characters.
            description (string) --The description of the rule.
            createdAt (datetime) --The date and time the rule was created.
            actions (list) --The actions associated with the rule.
            (dict) --Describes the actions associated with a rule.
            dynamoDB (dict) --Write to a DynamoDB table.
            tableName (string) --The name of the DynamoDB table.
            roleArn (string) --The ARN of the IAM role that grants access to the DynamoDB table.
            operation (string) --The type of operation to be performed. This follows the substitution template, so it can be ${operation} , but the substitution must result in one of the following: INSERT , UPDATE , or DELETE .
            hashKeyField (string) --The hash key name.
            hashKeyValue (string) --The hash key value.
            hashKeyType (string) --The hash key type. Valid values are 'STRING' or 'NUMBER'
            rangeKeyField (string) --The range key name.
            rangeKeyValue (string) --The range key value.
            rangeKeyType (string) --The range key type. Valid values are 'STRING' or 'NUMBER'
            payloadField (string) --The action payload. This name can be customized.
            dynamoDBv2 (dict) --Write to a DynamoDB table. This is a new version of the DynamoDB action. It allows you to write each attribute in an MQTT message payload into a separate DynamoDB column.
            roleArn (string) --The ARN of the IAM role that grants access to the DynamoDB table.
            putItem (dict) --Specifies the DynamoDB table to which the message data will be written. For example:
            { 'dynamoDBv2': { 'roleArn': 'aws:iam:12341251:my-role' 'putItem': { 'tableName': 'my-table' } } }
            Each attribute in the message payload will be written to a separate column in the DynamoDB database.
            tableName (string) --The table where the message data will be written
            
            lambda (dict) --Invoke a Lambda function.
            functionArn (string) --The ARN of the Lambda function.
            sns (dict) --Publish to an Amazon SNS topic.
            targetArn (string) --The ARN of the SNS topic.
            roleArn (string) --The ARN of the IAM role that grants access.
            messageFormat (string) --The message format of the message to publish. Optional. Accepted values are 'JSON' and 'RAW'. The default value of the attribute is 'RAW'. SNS uses this setting to determine if the payload should be parsed and relevant platform-specific bits of the payload should be extracted. To read more about SNS message formats, see http://docs.aws.amazon.com/sns/latest/dg/json-formats.html refer to their official documentation.
            sqs (dict) --Publish to an Amazon SQS queue.
            roleArn (string) --The ARN of the IAM role that grants access.
            queueUrl (string) --The URL of the Amazon SQS queue.
            useBase64 (boolean) --Specifies whether to use Base64 encoding.
            kinesis (dict) --Write data to an Amazon Kinesis stream.
            roleArn (string) --The ARN of the IAM role that grants access to the Amazon Kinesis stream.
            streamName (string) --The name of the Amazon Kinesis stream.
            partitionKey (string) --The partition key.
            republish (dict) --Publish to another MQTT topic.
            roleArn (string) --The ARN of the IAM role that grants access.
            topic (string) --The name of the MQTT topic.
            s3 (dict) --Write to an Amazon S3 bucket.
            roleArn (string) --The ARN of the IAM role that grants access.
            bucketName (string) --The Amazon S3 bucket.
            key (string) --The object key.
            cannedAcl (string) --The Amazon S3 canned ACL that controls access to the object identified by the object key. For more information, see S3 canned ACLs .
            firehose (dict) --Write to an Amazon Kinesis Firehose stream.
            roleArn (string) --The IAM role that grants access to the Amazon Kinesis Firehost stream.
            deliveryStreamName (string) --The delivery stream name.
            separator (string) --A character separator that will be used to separate records written to the Firehose stream. Valid values are: 'n' (newline), 't' (tab), 'rn' (Windows newline), ',' (comma).
            cloudwatchMetric (dict) --Capture a CloudWatch metric.
            roleArn (string) --The IAM role that allows access to the CloudWatch metric.
            metricNamespace (string) --The CloudWatch metric namespace name.
            metricName (string) --The CloudWatch metric name.
            metricValue (string) --The CloudWatch metric value.
            metricUnit (string) --The metric unit supported by CloudWatch.
            metricTimestamp (string) --An optional Unix timestamp .
            cloudwatchAlarm (dict) --Change the state of a CloudWatch alarm.
            roleArn (string) --The IAM role that allows access to the CloudWatch alarm.
            alarmName (string) --The CloudWatch alarm name.
            stateReason (string) --The reason for the alarm change.
            stateValue (string) --The value of the alarm state. Acceptable values are: OK, ALARM, INSUFFICIENT_DATA.
            elasticsearch (dict) --Write data to an Amazon Elasticsearch Service domain.
            roleArn (string) --The IAM role ARN that has access to Elasticsearch.
            endpoint (string) --The endpoint of your Elasticsearch domain.
            index (string) --The Elasticsearch index where you want to store your data.
            type (string) --The type of document you are storing.
            id (string) --The unique identifier for the document you are storing.
            
            ruleDisabled (boolean) --Specifies whether the rule is disabled.
            awsIotSqlVersion (string) --The version of the SQL rules engine to use when evaluating the rule.
            
            
            
    :type ruleName: string
    """
    pass


def get_waiter():
    """
    """
    pass


def list_ca_certificates(pageSize=None, marker=None, ascendingOrder=None):
    """
    :param pageSize: The result page size.
    :type pageSize: integer
    :param marker: The marker for the next set of results.
    :type marker: string
    :param ascendingOrder: Determines the order of the results.
    :type ascendingOrder: boolean
    """
    pass


def list_certificates(pageSize=None, marker=None, ascendingOrder=None):
    """
    :param pageSize: The result page size.
    :type pageSize: integer
    :param marker: The marker for the next set of results.
    :type marker: string
    :param ascendingOrder: Specifies the order for results. If True, the results are returned in ascending order, based on the creation date.
    :type ascendingOrder: boolean
    """
    pass


def list_certificates_by_ca(caCertificateId=None, pageSize=None, marker=None, ascendingOrder=None):
    """
    :param caCertificateId: [REQUIRED]
            The ID of the CA certificate. This operation will list all registered device certificate that were signed by this CA certificate.
            
    :type caCertificateId: string
    :param pageSize: The result page size.
    :type pageSize: integer
    :param marker: The marker for the next set of results.
    :type marker: string
    :param ascendingOrder: Specifies the order for results. If True, the results are returned in ascending order, based on the creation date.
    :type ascendingOrder: boolean
    """
    pass


def list_outgoing_certificates(pageSize=None, marker=None, ascendingOrder=None):
    """
    :param pageSize: The result page size.
    :type pageSize: integer
    :param marker: The marker for the next set of results.
    :type marker: string
    :param ascendingOrder: Specifies the order for results. If True, the results are returned in ascending order, based on the creation date.
    :type ascendingOrder: boolean
    """
    pass


def list_policies(marker=None, pageSize=None, ascendingOrder=None):
    """
    :param marker: The marker for the next set of results.
    :type marker: string
    :param pageSize: The result page size.
    :type pageSize: integer
    :param ascendingOrder: Specifies the order for results. If true, the results are returned in ascending creation order.
    :type ascendingOrder: boolean
    """
    pass


def list_policy_principals(policyName=None, marker=None, pageSize=None, ascendingOrder=None):
    """
    :param policyName: [REQUIRED]
            The policy name.
            
    :type policyName: string
    :param marker: The marker for the next set of results.
    :type marker: string
    :param pageSize: The result page size.
    :type pageSize: integer
    :param ascendingOrder: Specifies the order for results. If true, the results are returned in ascending creation order.
    :type ascendingOrder: boolean
    """
    pass


def list_policy_versions(policyName=None):
    """
    :param policyName: [REQUIRED]
            The policy name.
            Return typedict
            ReturnsResponse Syntax{
              'policyVersions': [
                {
                  'versionId': 'string',
                  'isDefaultVersion': True|False,
                  'createDate': datetime(2015, 1, 1)
                },
              ]
            }
            Response Structure
            (dict) --The output from the ListPolicyVersions operation.
            policyVersions (list) --The policy versions.
            (dict) --Describes a policy version.
            versionId (string) --The policy version ID.
            isDefaultVersion (boolean) --Specifies whether the policy version is the default.
            createDate (datetime) --The date and time the policy was created.
            
            
            
    :type policyName: string
    """
    pass


def list_principal_policies(principal=None, marker=None, pageSize=None, ascendingOrder=None):
    """
    :param principal: [REQUIRED]
            The principal.
            
    :type principal: string
    :param marker: The marker for the next set of results.
    :type marker: string
    :param pageSize: The result page size.
    :type pageSize: integer
    :param ascendingOrder: Specifies the order for results. If true, results are returned in ascending creation order.
    :type ascendingOrder: boolean
    """
    pass


def list_principal_things(nextToken=None, maxResults=None, principal=None):
    """
    :param nextToken: The token for the next set of results, or null if there are no additional results.
    :type nextToken: string
    :param maxResults: The maximum number of results to return in this operation.
    :type maxResults: integer
    :param principal: [REQUIRED]
            The principal.
            
    :type principal: string
    """
    pass


def list_thing_principals(thingName=None):
    """
    :param thingName: [REQUIRED]
            The name of the thing.
            Return typedict
            ReturnsResponse Syntax{
              'principals': [
                'string',
              ]
            }
            Response Structure
            (dict) --The output from the ListThingPrincipals operation.
            principals (list) --The principals associated with the thing.
            (string) --
            
            
    :type thingName: string
    """
    pass


def list_thing_types(nextToken=None, maxResults=None, thingTypeName=None):
    """
    :param nextToken: The token for the next set of results, or null if there are no additional results.
    :type nextToken: string
    :param maxResults: The maximum number of results to return in this operation.
    :type maxResults: integer
    :param thingTypeName: The name of the thing type.
    :type thingTypeName: string
    """
    pass


def list_things(nextToken=None, maxResults=None, attributeName=None, attributeValue=None, thingTypeName=None):
    """
    :param nextToken: The token for the next set of results, or null if there are no additional results.
    :type nextToken: string
    :param maxResults: The maximum number of results to return in this operation.
    :type maxResults: integer
    :param attributeName: The attribute name used to search for things.
    :type attributeName: string
    :param attributeValue: The attribute value used to search for things.
    :type attributeValue: string
    :param thingTypeName: The name of the thing type used to search for things.
    :type thingTypeName: string
    """
    pass


def list_topic_rules(topic=None, maxResults=None, nextToken=None, ruleDisabled=None):
    """
    :param topic: The topic.
    :type topic: string
    :param maxResults: The maximum number of results to return.
    :type maxResults: integer
    :param nextToken: A token used to retrieve the next value.
    :type nextToken: string
    :param ruleDisabled: Specifies whether the rule is disabled.
    :type ruleDisabled: boolean
    """
    pass


def register_ca_certificate(caCertificate=None, verificationCertificate=None, setAsActive=None,
                            allowAutoRegistration=None):
    """
    :param caCertificate: [REQUIRED]
            The CA certificate.
            
    :type caCertificate: string
    :param verificationCertificate: [REQUIRED]
            The private key verification certificate.
            
    :type verificationCertificate: string
    :param setAsActive: A boolean value that specifies if the CA certificate is set to active.
    :type setAsActive: boolean
    :param allowAutoRegistration: Allows this CA certificate to be used for auto registration of device certificates.
    :type allowAutoRegistration: boolean
    """
    pass


def register_certificate(certificatePem=None, caCertificatePem=None, setAsActive=None, status=None):
    """
    :param certificatePem: [REQUIRED]
            The certificate data, in PEM format.
            
    :type certificatePem: string
    :param caCertificatePem: The CA certificate used to sign the device certificate being registered.
    :type caCertificatePem: string
    :param setAsActive: A boolean value that specifies if the CA certificate is set to active.
    :type setAsActive: boolean
    :param status: 
    :type status: string
    """
    pass


def reject_certificate_transfer(certificateId=None, rejectReason=None):
    """
    :param certificateId: [REQUIRED]
            The ID of the certificate.
            
    :type certificateId: string
    :param rejectReason: The reason the certificate transfer was rejected.
    :type rejectReason: string
    """
    pass


def replace_topic_rule(ruleName=None, topicRulePayload=None):
    """
    :param ruleName: [REQUIRED]
            The name of the rule.
            
    :type ruleName: string
    :param topicRulePayload: [REQUIRED]
            The rule payload.
            sql (string) -- [REQUIRED]The SQL statement used to query the topic. For more information, see AWS IoT SQL Reference in the AWS IoT Developer Guide .
            description (string) --The description of the rule.
            actions (list) -- [REQUIRED]The actions associated with the rule.
            (dict) --Describes the actions associated with a rule.
            dynamoDB (dict) --Write to a DynamoDB table.
            tableName (string) -- [REQUIRED]The name of the DynamoDB table.
            roleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access to the DynamoDB table.
            operation (string) --The type of operation to be performed. This follows the substitution template, so it can be ${operation} , but the substitution must result in one of the following: INSERT , UPDATE , or DELETE .
            hashKeyField (string) -- [REQUIRED]The hash key name.
            hashKeyValue (string) -- [REQUIRED]The hash key value.
            hashKeyType (string) --The hash key type. Valid values are 'STRING' or 'NUMBER'
            rangeKeyField (string) --The range key name.
            rangeKeyValue (string) --The range key value.
            rangeKeyType (string) --The range key type. Valid values are 'STRING' or 'NUMBER'
            payloadField (string) --The action payload. This name can be customized.
            dynamoDBv2 (dict) --Write to a DynamoDB table. This is a new version of the DynamoDB action. It allows you to write each attribute in an MQTT message payload into a separate DynamoDB column.
            roleArn (string) --The ARN of the IAM role that grants access to the DynamoDB table.
            putItem (dict) --Specifies the DynamoDB table to which the message data will be written. For example:
            { 'dynamoDBv2': { 'roleArn': 'aws:iam:12341251:my-role' 'putItem': { 'tableName': 'my-table' } } }
            Each attribute in the message payload will be written to a separate column in the DynamoDB database.
            tableName (string) -- [REQUIRED]The table where the message data will be written
            
            lambda (dict) --Invoke a Lambda function.
            functionArn (string) -- [REQUIRED]The ARN of the Lambda function.
            sns (dict) --Publish to an Amazon SNS topic.
            targetArn (string) -- [REQUIRED]The ARN of the SNS topic.
            roleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access.
            messageFormat (string) --The message format of the message to publish. Optional. Accepted values are 'JSON' and 'RAW'. The default value of the attribute is 'RAW'. SNS uses this setting to determine if the payload should be parsed and relevant platform-specific bits of the payload should be extracted. To read more about SNS message formats, see http://docs.aws.amazon.com/sns/latest/dg/json-formats.html refer to their official documentation.
            sqs (dict) --Publish to an Amazon SQS queue.
            roleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access.
            queueUrl (string) -- [REQUIRED]The URL of the Amazon SQS queue.
            useBase64 (boolean) --Specifies whether to use Base64 encoding.
            kinesis (dict) --Write data to an Amazon Kinesis stream.
            roleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access to the Amazon Kinesis stream.
            streamName (string) -- [REQUIRED]The name of the Amazon Kinesis stream.
            partitionKey (string) --The partition key.
            republish (dict) --Publish to another MQTT topic.
            roleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access.
            topic (string) -- [REQUIRED]The name of the MQTT topic.
            s3 (dict) --Write to an Amazon S3 bucket.
            roleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access.
            bucketName (string) -- [REQUIRED]The Amazon S3 bucket.
            key (string) -- [REQUIRED]The object key.
            cannedAcl (string) --The Amazon S3 canned ACL that controls access to the object identified by the object key. For more information, see S3 canned ACLs .
            firehose (dict) --Write to an Amazon Kinesis Firehose stream.
            roleArn (string) -- [REQUIRED]The IAM role that grants access to the Amazon Kinesis Firehost stream.
            deliveryStreamName (string) -- [REQUIRED]The delivery stream name.
            separator (string) --A character separator that will be used to separate records written to the Firehose stream. Valid values are: 'n' (newline), 't' (tab), 'rn' (Windows newline), ',' (comma).
            cloudwatchMetric (dict) --Capture a CloudWatch metric.
            roleArn (string) -- [REQUIRED]The IAM role that allows access to the CloudWatch metric.
            metricNamespace (string) -- [REQUIRED]The CloudWatch metric namespace name.
            metricName (string) -- [REQUIRED]The CloudWatch metric name.
            metricValue (string) -- [REQUIRED]The CloudWatch metric value.
            metricUnit (string) -- [REQUIRED]The metric unit supported by CloudWatch.
            metricTimestamp (string) --An optional Unix timestamp .
            cloudwatchAlarm (dict) --Change the state of a CloudWatch alarm.
            roleArn (string) -- [REQUIRED]The IAM role that allows access to the CloudWatch alarm.
            alarmName (string) -- [REQUIRED]The CloudWatch alarm name.
            stateReason (string) -- [REQUIRED]The reason for the alarm change.
            stateValue (string) -- [REQUIRED]The value of the alarm state. Acceptable values are: OK, ALARM, INSUFFICIENT_DATA.
            elasticsearch (dict) --Write data to an Amazon Elasticsearch Service domain.
            roleArn (string) -- [REQUIRED]The IAM role ARN that has access to Elasticsearch.
            endpoint (string) -- [REQUIRED]The endpoint of your Elasticsearch domain.
            index (string) -- [REQUIRED]The Elasticsearch index where you want to store your data.
            type (string) -- [REQUIRED]The type of document you are storing.
            id (string) -- [REQUIRED]The unique identifier for the document you are storing.
            
            ruleDisabled (boolean) --Specifies whether the rule is disabled.
            awsIotSqlVersion (string) --The version of the SQL rules engine to use when evaluating the rule.
            
    :type topicRulePayload: dict
    """
    pass


def set_default_policy_version(policyName=None, policyVersionId=None):
    """
    :param policyName: [REQUIRED]
            The policy name.
            
    :type policyName: string
    :param policyVersionId: [REQUIRED]
            The policy version ID.
            
    :type policyVersionId: string
    """
    pass


def set_logging_options(loggingOptionsPayload=None):
    """
    :param loggingOptionsPayload: [REQUIRED]
            The logging options payload.
            roleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access.
            logLevel (string) --The logging level.
            ReturnsNone
            
    :type loggingOptionsPayload: dict
    """
    pass


def transfer_certificate(certificateId=None, targetAwsAccount=None, transferMessage=None):
    """
    :param certificateId: [REQUIRED]
            The ID of the certificate.
            
    :type certificateId: string
    :param targetAwsAccount: [REQUIRED]
            The AWS account.
            
    :type targetAwsAccount: string
    :param transferMessage: The transfer message.
    :type transferMessage: string
    """
    pass


def update_ca_certificate(certificateId=None, newStatus=None, newAutoRegistrationStatus=None):
    """
    :param certificateId: [REQUIRED]
            The CA certificate identifier.
            
    :type certificateId: string
    :param newStatus: The updated status of the CA certificate.
            Note: The status value REGISTER_INACTIVE is deprecated and should not be used.
            
    :type newStatus: string
    :param newAutoRegistrationStatus: The new value for the auto registration status. Valid values are: 'ENABLE' or 'DISABLE'.
    :type newAutoRegistrationStatus: string
    """
    pass


def update_certificate(certificateId=None, newStatus=None):
    """
    :param certificateId: [REQUIRED]
            The ID of the certificate.
            
    :type certificateId: string
    :param newStatus: [REQUIRED]
            The new status.
            Note: Setting the status to PENDING_TRANSFER will result in an exception being thrown. PENDING_TRANSFER is a status used internally by AWS IoT. It is not intended for developer use.
            Note: The status value REGISTER_INACTIVE is deprecated and should not be used.
            
    :type newStatus: string
    """
    pass


def update_thing(thingName=None, thingTypeName=None, attributePayload=None, expectedVersion=None, removeThingType=None):
    """
    :param thingName: [REQUIRED]
            The name of the thing to update.
            
    :type thingName: string
    :param thingTypeName: The name of the thing type.
    :type thingTypeName: string
    :param attributePayload: A list of thing attributes, a JSON string containing name-value pairs. For example:
            {\'attributes\':{\'name1\':\'value2\'}})
            This data is used to add new attributes or update existing attributes.
            attributes (dict) --A JSON string containing up to three key-value pair in JSON format. For example:
            {\'attributes\':{\'string1\':\'string2\'}})
            (string) --
            (string) -- An attribute value for an Thing. An empty or null value in Update means that existing value for that attribute should be deleted. Empty and null values in create are ignored.
            
            merge (boolean) --Specifies whether the list of attributes provided in the AttributePayload is merged with the attributes stored in the registry, instead of overwriting them.
            To remove an attribute, call UpdateThing with an empty attribute value.
            Note
            The merge attribute is only valid when calling UpdateThing .
            
    :type attributePayload: dict
    :param expectedVersion: The expected version of the thing record in the registry. If the version of the record in the registry does not match the expected version specified in the request, the UpdateThing request is rejected with a VersionConflictException .
    :type expectedVersion: integer
    :param removeThingType: Remove a thing type association. If true , the assocation is removed.
    :type removeThingType: boolean
    """
    pass
