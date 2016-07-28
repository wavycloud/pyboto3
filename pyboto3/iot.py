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

import boto3


class Iot(object):
    def __init__(self):
        self.client = boto3.client('Iot')

    def accept_certificate_transfer(self, certificateId=None, setAsActive=None):
        """
        :param certificateId: [REQUIRED]
            The ID of the certificate.
            
        :type certificateId: string
        :param setAsActive: Specifies whether the certificate is active.
        :type setAsActive: boolean
        """
        self.client.accept_certificate_transfer(certificateId=certificateId, setAsActive=setAsActive)

    def attach_principal_policy(self, policyName=None, principal=None):
        """
        :param policyName: [REQUIRED]
            The policy name.
            
        :type policyName: string
        :param principal: [REQUIRED]
            The principal, which can be a certificate ARN (as returned from the CreateCertificate operation) or an Amazon Cognito ID.
            
        :type principal: string
        """
        self.client.attach_principal_policy(policyName=policyName, principal=principal)

    def attach_thing_principal(self, thingName=None, principal=None):
        """
        :param thingName: [REQUIRED]
            The name of the thing.
            
        :type thingName: string
        :param principal: [REQUIRED]
            The principal, such as a certificate or other credential.
            
        :type principal: string
        """
        self.client.attach_thing_principal(thingName=thingName, principal=principal)

    def can_paginate(self, operation_name=None):
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
        self.client.can_paginate(operation_name=operation_name)

    def cancel_certificate_transfer(self, certificateId=None):
        """
        :param certificateId: [REQUIRED]
            The ID of the certificate.
            ReturnsNone
            
        :type certificateId: string
        """
        self.client.cancel_certificate_transfer(certificateId=certificateId)

    def create_certificate_from_csr(self, certificateSigningRequest=None, setAsActive=None):
        """
        :param certificateSigningRequest: [REQUIRED]
            The certificate signing request (CSR).
            
        :type certificateSigningRequest: string
        :param setAsActive: Specifies whether the certificate is active.
        :type setAsActive: boolean
        """
        self.client.create_certificate_from_csr(certificateSigningRequest=certificateSigningRequest,
                                                setAsActive=setAsActive)

    def create_keys_and_certificate(self, setAsActive=None):
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
        self.client.create_keys_and_certificate(setAsActive=setAsActive)

    def create_policy(self, policyName=None, policyDocument=None):
        """
        :param policyName: [REQUIRED]
            The policy name.
            
        :type policyName: string
        :param policyDocument: [REQUIRED]
            The JSON document that describes the policy. policyDocument must have a minimum length of 1, with a maximum length of 2048, excluding whitespace.
            
        :type policyDocument: string
        """
        self.client.create_policy(policyName=policyName, policyDocument=policyDocument)

    def create_policy_version(self, policyName=None, policyDocument=None, setAsDefault=None):
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
        self.client.create_policy_version(policyName=policyName, policyDocument=policyDocument,
                                          setAsDefault=setAsDefault)

    def create_thing(self, thingName=None, thingTypeName=None, attributePayload=None):
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
        self.client.create_thing(thingName=thingName, thingTypeName=thingTypeName, attributePayload=attributePayload)

    def create_thing_type(self, thingTypeName=None, thingTypeProperties=None):
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
        self.client.create_thing_type(thingTypeName=thingTypeName, thingTypeProperties=thingTypeProperties)

    def create_topic_rule(self, ruleName=None, topicRulePayload=None):
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
            firehose (dict) --Write to an Amazon Kinesis Firehose stream.
            roleArn (string) -- [REQUIRED]The IAM role that grants access to the Amazon Kinesis Firehost stream.
            deliveryStreamName (string) -- [REQUIRED]The delivery stream name.
            separator (string) --A character separator that will be used to separate records written to the firehose stream. Valid values are: 'n' (newline), 't' (tab), 'rn' (Windows newline), ',' (comma).
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
            elasticsearch (dict) --Write data to an Amazon Elasticsearch Service; domain.
            roleArn (string) -- [REQUIRED]The IAM role ARN that has access to Elasticsearch.
            endpoint (string) -- [REQUIRED]The endpoint of your Elasticsearch domain.
            index (string) -- [REQUIRED]The Elasticsearch index where you want to store your data.
            type (string) -- [REQUIRED]The type of document you are storing.
            id (string) -- [REQUIRED]The unique identifier for the document you are storing.
            
            ruleDisabled (boolean) --Specifies whether the rule is disabled.
            awsIotSqlVersion (string) --The version of the SQL rules engine to use when evaluating the rule.
            
        :type topicRulePayload: dict
        """
        self.client.create_topic_rule(ruleName=ruleName, topicRulePayload=topicRulePayload)

    def delete_ca_certificate(self, certificateId=None):
        """
        :param certificateId: [REQUIRED]
            The ID of the certificate to delete.
            Return typedict
            ReturnsResponse Syntax{}
            Response Structure
            (dict) --The output for the DeleteCACertificate operation.
            
            
        :type certificateId: string
        """
        self.client.delete_ca_certificate(certificateId=certificateId)

    def delete_certificate(self, certificateId=None):
        """
        :param certificateId: [REQUIRED]
            The ID of the certificate.
            ReturnsNone
            
        :type certificateId: string
        """
        self.client.delete_certificate(certificateId=certificateId)

    def delete_policy(self, policyName=None):
        """
        :param policyName: [REQUIRED]
            The name of the policy to delete.
            ReturnsNone
            
        :type policyName: string
        """
        self.client.delete_policy(policyName=policyName)

    def delete_policy_version(self, policyName=None, policyVersionId=None):
        """
        :param policyName: [REQUIRED]
            The name of the policy.
            
        :type policyName: string
        :param policyVersionId: [REQUIRED]
            The policy version ID.
            
        :type policyVersionId: string
        """
        self.client.delete_policy_version(policyName=policyName, policyVersionId=policyVersionId)

    def delete_registration_code(self):
        """
        """
        self.client.delete_registration_code()

    def delete_thing(self, thingName=None, expectedVersion=None):
        """
        :param thingName: [REQUIRED]
            The name of the thing to delete.
            
        :type thingName: string
        :param expectedVersion: The expected version of the thing record in the registry. If the version of the record in the registry does not match the expected version specified in the request, the DeleteThing request is rejected with a VersionConflictException .
        :type expectedVersion: integer
        """
        self.client.delete_thing(thingName=thingName, expectedVersion=expectedVersion)

    def delete_thing_type(self, thingTypeName=None):
        """
        :param thingTypeName: [REQUIRED]
            The name of the thing type.
            Return typedict
            ReturnsResponse Syntax{}
            Response Structure
            (dict) --The output for the DeleteThingType operation.
            
            
        :type thingTypeName: string
        """
        self.client.delete_thing_type(thingTypeName=thingTypeName)

    def delete_topic_rule(self, ruleName=None):
        """
        :param ruleName: [REQUIRED]
            The name of the rule.
            ReturnsNone
            
        :type ruleName: string
        """
        self.client.delete_topic_rule(ruleName=ruleName)

    def deprecate_thing_type(self, thingTypeName=None, undoDeprecate=None):
        """
        :param thingTypeName: [REQUIRED]
            The name of the thing type to deprecate.
            
        :type thingTypeName: string
        :param undoDeprecate: Whether to undeprecate a deprecated thing type. If true , the thing type will not be deprecated anymore and you can associate it with things.
        :type undoDeprecate: boolean
        """
        self.client.deprecate_thing_type(thingTypeName=thingTypeName, undoDeprecate=undoDeprecate)

    def describe_ca_certificate(self, certificateId=None):
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
                'creationDate': datetime(2015, 1, 1)
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
            
            
            
        :type certificateId: string
        """
        self.client.describe_ca_certificate(certificateId=certificateId)

    def describe_certificate(self, certificateId=None):
        """
        :param certificateId: [REQUIRED]
            The ID of the certificate.
            Return typedict
            ReturnsResponse Syntax{
              'certificateDescription': {
                'certificateArn': 'string',
                'certificateId': 'string',
                'caCertificateId': 'string',
                'status': 'ACTIVE'|'INACTIVE'|'REVOKED'|'PENDING_TRANSFER'|'REGISTER_INACTIVE',
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
        self.client.describe_certificate(certificateId=certificateId)

    def describe_endpoint(self):
        """
        """
        self.client.describe_endpoint()

    def describe_thing(self, thingName=None):
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
        self.client.describe_thing(thingName=thingName)

    def describe_thing_type(self, thingTypeName=None):
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
        self.client.describe_thing_type(thingTypeName=thingTypeName)

    def detach_principal_policy(self, policyName=None, principal=None):
        """
        :param policyName: [REQUIRED]
            The name of the policy to detach.
            
        :type policyName: string
        :param principal: [REQUIRED]
            The principal.
            If the principal is a certificate, specify the certificate ARN. If the principal is an Amazon Cognito identity, specify the identity ID.
            
        :type principal: string
        """
        self.client.detach_principal_policy(policyName=policyName, principal=principal)

    def detach_thing_principal(self, thingName=None, principal=None):
        """
        :param thingName: [REQUIRED]
            The name of the thing.
            
        :type thingName: string
        :param principal: [REQUIRED]
            If the principal is a certificate, this value must be ARN of the certificate. If the principal is an Amazon Cognito identity, this value must be the ID of the Amazon Cognito identity.
            
        :type principal: string
        """
        self.client.detach_thing_principal(thingName=thingName, principal=principal)

    def disable_topic_rule(self, ruleName=None):
        """
        :param ruleName: [REQUIRED]
            The name of the rule to disable.
            ReturnsNone
            
        :type ruleName: string
        """
        self.client.disable_topic_rule(ruleName=ruleName)

    def enable_topic_rule(self, ruleName=None):
        """
        :param ruleName: [REQUIRED]
            The name of the topic rule to enable.
            ReturnsNone
            
        :type ruleName: string
        """
        self.client.enable_topic_rule(ruleName=ruleName)

    def generate_presigned_url(self, ClientMethod=None, Params=None, ExpiresIn=None, HttpMethod=None):
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
        self.client.generate_presigned_url(ClientMethod=ClientMethod, Params=Params, ExpiresIn=ExpiresIn,
                                           HttpMethod=HttpMethod)

    def get_logging_options(self):
        """
        """
        self.client.get_logging_options()

    def get_paginator(self, operation_name=None):
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
        self.client.get_paginator(operation_name=operation_name)

    def get_policy(self, policyName=None):
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
        self.client.get_policy(policyName=policyName)

    def get_policy_version(self, policyName=None, policyVersionId=None):
        """
        :param policyName: [REQUIRED]
            The name of the policy.
            
        :type policyName: string
        :param policyVersionId: [REQUIRED]
            The policy version ID.
            
        :type policyVersionId: string
        """
        self.client.get_policy_version(policyName=policyName, policyVersionId=policyVersionId)

    def get_registration_code(self):
        """
        """
        self.client.get_registration_code()

    def get_topic_rule(self, ruleName=None):
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
                      'key': 'string'
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
            firehose (dict) --Write to an Amazon Kinesis Firehose stream.
            roleArn (string) --The IAM role that grants access to the Amazon Kinesis Firehost stream.
            deliveryStreamName (string) --The delivery stream name.
            separator (string) --A character separator that will be used to separate records written to the firehose stream. Valid values are: 'n' (newline), 't' (tab), 'rn' (Windows newline), ',' (comma).
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
            elasticsearch (dict) --Write data to an Amazon Elasticsearch Service; domain.
            roleArn (string) --The IAM role ARN that has access to Elasticsearch.
            endpoint (string) --The endpoint of your Elasticsearch domain.
            index (string) --The Elasticsearch index where you want to store your data.
            type (string) --The type of document you are storing.
            id (string) --The unique identifier for the document you are storing.
            
            ruleDisabled (boolean) --Specifies whether the rule is disabled.
            awsIotSqlVersion (string) --The version of the SQL rules engine to use when evaluating the rule.
            
            
            
        :type ruleName: string
        """
        self.client.get_topic_rule(ruleName=ruleName)

    def get_waiter(self):
        """
        """
        self.client.get_waiter()

    def list_ca_certificates(self, pageSize=None, marker=None, ascendingOrder=None):
        """
        :param pageSize: The result page size.
        :type pageSize: integer
        :param marker: The marker for the next set of results.
        :type marker: string
        :param ascendingOrder: Determines the order of the results.
        :type ascendingOrder: boolean
        """
        self.client.list_ca_certificates(pageSize=pageSize, marker=marker, ascendingOrder=ascendingOrder)

    def list_certificates(self, pageSize=None, marker=None, ascendingOrder=None):
        """
        :param pageSize: The result page size.
        :type pageSize: integer
        :param marker: The marker for the next set of results.
        :type marker: string
        :param ascendingOrder: Specifies the order for results. If True, the results are returned in ascending order, based on the creation date.
        :type ascendingOrder: boolean
        """
        self.client.list_certificates(pageSize=pageSize, marker=marker, ascendingOrder=ascendingOrder)

    def list_certificates_by_ca(self, caCertificateId=None, pageSize=None, marker=None, ascendingOrder=None):
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
        self.client.list_certificates_by_ca(caCertificateId=caCertificateId, pageSize=pageSize, marker=marker,
                                            ascendingOrder=ascendingOrder)

    def list_policies(self, marker=None, pageSize=None, ascendingOrder=None):
        """
        :param marker: The marker for the next set of results.
        :type marker: string
        :param pageSize: The result page size.
        :type pageSize: integer
        :param ascendingOrder: Specifies the order for results. If true, the results are returned in ascending creation order.
        :type ascendingOrder: boolean
        """
        self.client.list_policies(marker=marker, pageSize=pageSize, ascendingOrder=ascendingOrder)

    def list_policy_principals(self, policyName=None, marker=None, pageSize=None, ascendingOrder=None):
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
        self.client.list_policy_principals(policyName=policyName, marker=marker, pageSize=pageSize,
                                           ascendingOrder=ascendingOrder)

    def list_policy_versions(self, policyName=None):
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
        self.client.list_policy_versions(policyName=policyName)

    def list_principal_policies(self, principal=None, marker=None, pageSize=None, ascendingOrder=None):
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
        self.client.list_principal_policies(principal=principal, marker=marker, pageSize=pageSize,
                                            ascendingOrder=ascendingOrder)

    def list_principal_things(self, nextToken=None, maxResults=None, principal=None):
        """
        :param nextToken: The token for the next set of results, or null if there are no additional results.
        :type nextToken: string
        :param maxResults: The maximum number of results to return in this operation.
        :type maxResults: integer
        :param principal: [REQUIRED]
            The principal.
            
        :type principal: string
        """
        self.client.list_principal_things(nextToken=nextToken, maxResults=maxResults, principal=principal)

    def list_thing_principals(self, thingName=None):
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
        self.client.list_thing_principals(thingName=thingName)

    def list_thing_types(self, nextToken=None, maxResults=None, thingTypeName=None):
        """
        :param nextToken: The token for the next set of results, or null if there are no additional results.
        :type nextToken: string
        :param maxResults: The maximum number of results to return in this operation.
        :type maxResults: integer
        :param thingTypeName: The name of the thing type.
        :type thingTypeName: string
        """
        self.client.list_thing_types(nextToken=nextToken, maxResults=maxResults, thingTypeName=thingTypeName)

    def list_things(self, nextToken=None, maxResults=None, attributeName=None, attributeValue=None, thingTypeName=None):
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
        self.client.list_things(nextToken=nextToken, maxResults=maxResults, attributeName=attributeName,
                                attributeValue=attributeValue, thingTypeName=thingTypeName)

    def list_topic_rules(self, topic=None, maxResults=None, nextToken=None, ruleDisabled=None):
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
        self.client.list_topic_rules(topic=topic, maxResults=maxResults, nextToken=nextToken, ruleDisabled=ruleDisabled)

    def register_ca_certificate(self, caCertificate=None, verificationCertificate=None, setAsActive=None):
        """
        :param caCertificate: [REQUIRED]
            The CA certificate.
            
        :type caCertificate: string
        :param verificationCertificate: [REQUIRED]
            The private key verification certificate.
            
        :type verificationCertificate: string
        :param setAsActive: A boolean value that specifies if the CA certificate is set to active.
        :type setAsActive: boolean
        """
        self.client.register_ca_certificate(caCertificate=caCertificate,
                                            verificationCertificate=verificationCertificate, setAsActive=setAsActive)

    def register_certificate(self, certificatePem=None, caCertificatePem=None, setAsActive=None):
        """
        :param certificatePem: [REQUIRED]
            The certificate data, in PEM format.
            
        :type certificatePem: string
        :param caCertificatePem: The CA certificate used to sign the device certificate being registered.
        :type caCertificatePem: string
        :param setAsActive: A boolean value that specifies if the CA certificate is set to active.
        :type setAsActive: boolean
        """
        self.client.register_certificate(certificatePem=certificatePem, caCertificatePem=caCertificatePem,
                                         setAsActive=setAsActive)

    def reject_certificate_transfer(self, certificateId=None, rejectReason=None):
        """
        :param certificateId: [REQUIRED]
            The ID of the certificate.
            
        :type certificateId: string
        :param rejectReason: The reason the certificate transfer was rejected.
        :type rejectReason: string
        """
        self.client.reject_certificate_transfer(certificateId=certificateId, rejectReason=rejectReason)

    def replace_topic_rule(self, ruleName=None, topicRulePayload=None):
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
            firehose (dict) --Write to an Amazon Kinesis Firehose stream.
            roleArn (string) -- [REQUIRED]The IAM role that grants access to the Amazon Kinesis Firehost stream.
            deliveryStreamName (string) -- [REQUIRED]The delivery stream name.
            separator (string) --A character separator that will be used to separate records written to the firehose stream. Valid values are: 'n' (newline), 't' (tab), 'rn' (Windows newline), ',' (comma).
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
            elasticsearch (dict) --Write data to an Amazon Elasticsearch Service; domain.
            roleArn (string) -- [REQUIRED]The IAM role ARN that has access to Elasticsearch.
            endpoint (string) -- [REQUIRED]The endpoint of your Elasticsearch domain.
            index (string) -- [REQUIRED]The Elasticsearch index where you want to store your data.
            type (string) -- [REQUIRED]The type of document you are storing.
            id (string) -- [REQUIRED]The unique identifier for the document you are storing.
            
            ruleDisabled (boolean) --Specifies whether the rule is disabled.
            awsIotSqlVersion (string) --The version of the SQL rules engine to use when evaluating the rule.
            
        :type topicRulePayload: dict
        """
        self.client.replace_topic_rule(ruleName=ruleName, topicRulePayload=topicRulePayload)

    def set_default_policy_version(self, policyName=None, policyVersionId=None):
        """
        :param policyName: [REQUIRED]
            The policy name.
            
        :type policyName: string
        :param policyVersionId: [REQUIRED]
            The policy version ID.
            
        :type policyVersionId: string
        """
        self.client.set_default_policy_version(policyName=policyName, policyVersionId=policyVersionId)

    def set_logging_options(self, loggingOptionsPayload=None):
        """
        :param loggingOptionsPayload: [REQUIRED]
            The logging options payload.
            roleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access.
            logLevel (string) --The logging level.
            ReturnsNone
            
        :type loggingOptionsPayload: dict
        """
        self.client.set_logging_options(loggingOptionsPayload=loggingOptionsPayload)

    def transfer_certificate(self, certificateId=None, targetAwsAccount=None, transferMessage=None):
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
        self.client.transfer_certificate(certificateId=certificateId, targetAwsAccount=targetAwsAccount,
                                         transferMessage=transferMessage)

    def update_ca_certificate(self, certificateId=None, newStatus=None):
        """
        :param certificateId: [REQUIRED]
            The CA certificate identifier.
            
        :type certificateId: string
        :param newStatus: [REQUIRED]
            The updated status of the CA certificate.
            Note: The status value REGISTER_INACTIVE is deprecated and should not be used.
            
        :type newStatus: string
        """
        self.client.update_ca_certificate(certificateId=certificateId, newStatus=newStatus)

    def update_certificate(self, certificateId=None, newStatus=None):
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
        self.client.update_certificate(certificateId=certificateId, newStatus=newStatus)

    def update_thing(self, thingName=None, thingTypeName=None, attributePayload=None, expectedVersion=None,
                     removeThingType=None):
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
        self.client.update_thing(thingName=thingName, thingTypeName=thingTypeName, attributePayload=attributePayload,
                                 expectedVersion=expectedVersion, removeThingType=removeThingType)
