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

def accept_certificate_transfer(certificateId=None, setAsActive=None):
    """
    Accepts a pending certificate transfer. The default state of the certificate is INACTIVE.
    To check for pending certificate transfers, call  ListCertificates to enumerate your certificates.
    See also: AWS API Documentation
    
    
    :example: response = client.accept_certificate_transfer(
        certificateId='string',
        setAsActive=True|False
    )
    
    
    :type certificateId: string
    :param certificateId: [REQUIRED]
            The ID of the certificate.
            

    :type setAsActive: boolean
    :param setAsActive: Specifies whether the certificate is active.

    """
    pass

def attach_principal_policy(policyName=None, principal=None):
    """
    Attaches the specified policy to the specified principal (certificate or other credential).
    See also: AWS API Documentation
    
    
    :example: response = client.attach_principal_policy(
        policyName='string',
        principal='string'
    )
    
    
    :type policyName: string
    :param policyName: [REQUIRED]
            The policy name.
            

    :type principal: string
    :param principal: [REQUIRED]
            The principal, which can be a certificate ARN (as returned from the CreateCertificate operation) or an Amazon Cognito ID.
            

    """
    pass

def attach_thing_principal(thingName=None, principal=None):
    """
    Attaches the specified principal to the specified thing.
    See also: AWS API Documentation
    
    
    :example: response = client.attach_thing_principal(
        thingName='string',
        principal='string'
    )
    
    
    :type thingName: string
    :param thingName: [REQUIRED]
            The name of the thing.
            

    :type principal: string
    :param principal: [REQUIRED]
            The principal, such as a certificate or other credential.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

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

def cancel_certificate_transfer(certificateId=None):
    """
    Cancels a pending transfer for the specified certificate.
    Note Only the transfer source account can use this operation to cancel a transfer. (Transfer destinations can use  RejectCertificateTransfer instead.) After transfer, AWS IoT returns the certificate to the source account in the INACTIVE state. After the destination account has accepted the transfer, the transfer cannot be cancelled.
    After a certificate transfer is cancelled, the status of the certificate changes from PENDING_TRANSFER to INACTIVE.
    See also: AWS API Documentation
    
    
    :example: response = client.cancel_certificate_transfer(
        certificateId='string'
    )
    
    
    :type certificateId: string
    :param certificateId: [REQUIRED]
            The ID of the certificate.
            

    """
    pass

def create_certificate_from_csr(certificateSigningRequest=None, setAsActive=None):
    """
    Creates an X.509 certificate using the specified certificate signing request.
    Note Reusing the same certificate signing request (CSR) results in a distinct certificate.
    You can create multiple certificates in a batch by creating a directory, copying multiple .csr files into that directory, and then specifying that directory on the command line. The following commands show how to create a batch of certificates given a batch of CSRs.
    Assuming a set of CSRs are located inside of the directory my-csr-directory:
    On Linux and OS X, the command is:
    $ ls my-csr-directory/ | xargs -I {} aws iot create-certificate-from-csr --certificate-signing-request file://my-csr-directory/{}
    This command lists all of the CSRs in my-csr-directory and pipes each CSR file name to the aws iot create-certificate-from-csr AWS CLI command to create a certificate for the corresponding CSR.
    The aws iot create-certificate-from-csr part of the command can also be run in parallel to speed up the certificate creation process:
    $ ls my-csr-directory/ | xargs -P 10 -I {} aws iot create-certificate-from-csr --certificate-signing-request file://my-csr-directory/{}
    On Windows PowerShell, the command to create certificates for all CSRs in my-csr-directory is:
    On a Windows command prompt, the command to create certificates for all CSRs in my-csr-directory is:
    See also: AWS API Documentation
    
    
    :example: response = client.create_certificate_from_csr(
        certificateSigningRequest='string',
        setAsActive=True|False
    )
    
    
    :type certificateSigningRequest: string
    :param certificateSigningRequest: [REQUIRED]
            The certificate signing request (CSR).
            

    :type setAsActive: boolean
    :param setAsActive: Specifies whether the certificate is active.

    :rtype: dict
    :return: {
        'certificateArn': 'string',
        'certificateId': 'string',
        'certificatePem': 'string'
    }
    
    
    """
    pass

def create_keys_and_certificate(setAsActive=None):
    """
    Creates a 2048-bit RSA key pair and issues an X.509 certificate using the issued public key.
    Note This is the only time AWS IoT issues the private key for this certificate, so it is important to keep it in a secure location.
    See also: AWS API Documentation
    
    
    :example: response = client.create_keys_and_certificate(
        setAsActive=True|False
    )
    
    
    :type setAsActive: boolean
    :param setAsActive: Specifies whether the certificate is active.

    :rtype: dict
    :return: {
        'certificateArn': 'string',
        'certificateId': 'string',
        'certificatePem': 'string',
        'keyPair': {
            'PublicKey': 'string',
            'PrivateKey': 'string'
        }
    }
    
    
    """
    pass

def create_policy(policyName=None, policyDocument=None):
    """
    Creates an AWS IoT policy.
    The created policy is the default version for the policy. This operation creates a policy version with a version identifier of 1 and sets 1 as the policy's default version.
    See also: AWS API Documentation
    
    
    :example: response = client.create_policy(
        policyName='string',
        policyDocument='string'
    )
    
    
    :type policyName: string
    :param policyName: [REQUIRED]
            The policy name.
            

    :type policyDocument: string
    :param policyDocument: [REQUIRED]
            The JSON document that describes the policy. policyDocument must have a minimum length of 1, with a maximum length of 2048, excluding whitespace.
            

    :rtype: dict
    :return: {
        'policyName': 'string',
        'policyArn': 'string',
        'policyDocument': 'string',
        'policyVersionId': 'string'
    }
    
    
    """
    pass

def create_policy_version(policyName=None, policyDocument=None, setAsDefault=None):
    """
    Creates a new version of the specified AWS IoT policy. To update a policy, create a new policy version. A managed policy can have up to five versions. If the policy has five versions, you must use  DeletePolicyVersion to delete an existing version before you create a new one.
    Optionally, you can set the new version as the policy's default version. The default version is the operative version (that is, the version that is in effect for the certificates to which the policy is attached).
    See also: AWS API Documentation
    
    
    :example: response = client.create_policy_version(
        policyName='string',
        policyDocument='string',
        setAsDefault=True|False
    )
    
    
    :type policyName: string
    :param policyName: [REQUIRED]
            The policy name.
            

    :type policyDocument: string
    :param policyDocument: [REQUIRED]
            The JSON document that describes the policy. Minimum length of 1. Maximum length of 2048, excluding whitespaces
            

    :type setAsDefault: boolean
    :param setAsDefault: Specifies whether the policy version is set as the default. When this parameter is true, the new policy version becomes the operative version (that is, the version that is in effect for the certificates to which the policy is attached).

    :rtype: dict
    :return: {
        'policyArn': 'string',
        'policyDocument': 'string',
        'policyVersionId': 'string',
        'isDefaultVersion': True|False
    }
    
    
    """
    pass

def create_thing(thingName=None, thingTypeName=None, attributePayload=None):
    """
    Creates a thing record in the thing registry.
    See also: AWS API Documentation
    
    
    :example: response = client.create_thing(
        thingName='string',
        thingTypeName='string',
        attributePayload={
            'attributes': {
                'string': 'string'
            },
            'merge': True|False
        }
    )
    
    
    :type thingName: string
    :param thingName: [REQUIRED]
            The name of the thing to create.
            

    :type thingTypeName: string
    :param thingTypeName: The name of the thing type associated with the new thing.

    :type attributePayload: dict
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
            

    :rtype: dict
    :return: {
        'thingName': 'string',
        'thingArn': 'string'
    }
    
    
    """
    pass

def create_thing_type(thingTypeName=None, thingTypeProperties=None):
    """
    Creates a new thing type.
    See also: AWS API Documentation
    
    
    :example: response = client.create_thing_type(
        thingTypeName='string',
        thingTypeProperties={
            'thingTypeDescription': 'string',
            'searchableAttributes': [
                'string',
            ]
        }
    )
    
    
    :type thingTypeName: string
    :param thingTypeName: [REQUIRED]
            The name of the thing type.
            

    :type thingTypeProperties: dict
    :param thingTypeProperties: The ThingTypeProperties for the thing type to create. It contains information about the new thing type including a description, and a list of searchable thing attribute names.
            thingTypeDescription (string) --The description of the thing type.
            searchableAttributes (list) --A list of searchable thing attribute names.
            (string) --
            

    :rtype: dict
    :return: {
        'thingTypeName': 'string',
        'thingTypeArn': 'string'
    }
    
    
    """
    pass

def create_topic_rule(ruleName=None, topicRulePayload=None):
    """
    Creates a rule. Creating rules is an administrator-level action. Any user who has permission to create rules will be able to access data processed by the rule.
    See also: AWS API Documentation
    
    
    :example: response = client.create_topic_rule(
        ruleName='string',
        topicRulePayload={
            'sql': 'string',
            'description': 'string',
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
    )
    
    
    :type ruleName: string
    :param ruleName: [REQUIRED]
            The name of the rule.
            

    :type topicRulePayload: dict
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
            

    """
    pass

def delete_ca_certificate(certificateId=None):
    """
    Deletes a registered CA certificate.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_ca_certificate(
        certificateId='string'
    )
    
    
    :type certificateId: string
    :param certificateId: [REQUIRED]
            The ID of the certificate to delete.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_certificate(certificateId=None):
    """
    Deletes the specified certificate.
    A certificate cannot be deleted if it has a policy attached to it or if its status is set to ACTIVE. To delete a certificate, first use the  DetachPrincipalPolicy API to detach all policies. Next, use the  UpdateCertificate API to set the certificate to the INACTIVE status.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_certificate(
        certificateId='string'
    )
    
    
    :type certificateId: string
    :param certificateId: [REQUIRED]
            The ID of the certificate.
            

    """
    pass

def delete_policy(policyName=None):
    """
    Deletes the specified policy.
    A policy cannot be deleted if it has non-default versions or it is attached to any certificate.
    To delete a policy, use the DeletePolicyVersion API to delete all non-default versions of the policy; use the DetachPrincipalPolicy API to detach the policy from any certificate; and then use the DeletePolicy API to delete the policy.
    When a policy is deleted using DeletePolicy, its default version is deleted with it.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_policy(
        policyName='string'
    )
    
    
    :type policyName: string
    :param policyName: [REQUIRED]
            The name of the policy to delete.
            

    """
    pass

def delete_policy_version(policyName=None, policyVersionId=None):
    """
    Deletes the specified version of the specified policy. You cannot delete the default version of a policy using this API. To delete the default version of a policy, use  DeletePolicy . To find out which version of a policy is marked as the default version, use ListPolicyVersions.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_policy_version(
        policyName='string',
        policyVersionId='string'
    )
    
    
    :type policyName: string
    :param policyName: [REQUIRED]
            The name of the policy.
            

    :type policyVersionId: string
    :param policyVersionId: [REQUIRED]
            The policy version ID.
            

    """
    pass

def delete_registration_code():
    """
    Deletes a CA certificate registration code.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_registration_code()
    
    
    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_thing(thingName=None, expectedVersion=None):
    """
    Deletes the specified thing.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_thing(
        thingName='string',
        expectedVersion=123
    )
    
    
    :type thingName: string
    :param thingName: [REQUIRED]
            The name of the thing to delete.
            

    :type expectedVersion: integer
    :param expectedVersion: The expected version of the thing record in the registry. If the version of the record in the registry does not match the expected version specified in the request, the DeleteThing request is rejected with a VersionConflictException .

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_thing_type(thingTypeName=None):
    """
    Deletes the specified thing type . You cannot delete a thing type if it has things associated with it. To delete a thing type, first mark it as deprecated by calling  DeprecateThingType , then remove any associated things by calling  UpdateThing to change the thing type on any associated thing, and finally use  DeleteThingType to delete the thing type.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_thing_type(
        thingTypeName='string'
    )
    
    
    :type thingTypeName: string
    :param thingTypeName: [REQUIRED]
            The name of the thing type.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_topic_rule(ruleName=None):
    """
    Deletes the specified rule.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_topic_rule(
        ruleName='string'
    )
    
    
    :type ruleName: string
    :param ruleName: [REQUIRED]
            The name of the rule.
            

    """
    pass

def deprecate_thing_type(thingTypeName=None, undoDeprecate=None):
    """
    Deprecates a thing type. You can not associate new things with deprecated thing type.
    See also: AWS API Documentation
    
    
    :example: response = client.deprecate_thing_type(
        thingTypeName='string',
        undoDeprecate=True|False
    )
    
    
    :type thingTypeName: string
    :param thingTypeName: [REQUIRED]
            The name of the thing type to deprecate.
            

    :type undoDeprecate: boolean
    :param undoDeprecate: Whether to undeprecate a deprecated thing type. If true , the thing type will not be deprecated anymore and you can associate it with things.

    :rtype: dict
    :return: {}
    
    
    """
    pass

def describe_ca_certificate(certificateId=None):
    """
    Describes a registered CA certificate.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_ca_certificate(
        certificateId='string'
    )
    
    
    :type certificateId: string
    :param certificateId: [REQUIRED]
            The CA certificate identifier.
            

    :rtype: dict
    :return: {
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
    
    
    """
    pass

def describe_certificate(certificateId=None):
    """
    Gets information about the specified certificate.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_certificate(
        certificateId='string'
    )
    
    
    :type certificateId: string
    :param certificateId: [REQUIRED]
            The ID of the certificate.
            

    :rtype: dict
    :return: {
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
    
    
    """
    pass

def describe_endpoint():
    """
    Returns a unique endpoint specific to the AWS account making the call.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_endpoint()
    
    
    :rtype: dict
    :return: {
        'endpointAddress': 'string'
    }
    
    
    """
    pass

def describe_thing(thingName=None):
    """
    Gets information about the specified thing.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_thing(
        thingName='string'
    )
    
    
    :type thingName: string
    :param thingName: [REQUIRED]
            The name of the thing.
            

    :rtype: dict
    :return: {
        'defaultClientId': 'string',
        'thingName': 'string',
        'thingTypeName': 'string',
        'attributes': {
            'string': 'string'
        },
        'version': 123
    }
    
    
    """
    pass

def describe_thing_type(thingTypeName=None):
    """
    Gets information about the specified thing type.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_thing_type(
        thingTypeName='string'
    )
    
    
    :type thingTypeName: string
    :param thingTypeName: [REQUIRED]
            The name of the thing type.
            

    :rtype: dict
    :return: {
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
    
    
    """
    pass

def detach_principal_policy(policyName=None, principal=None):
    """
    Removes the specified policy from the specified certificate.
    See also: AWS API Documentation
    
    
    :example: response = client.detach_principal_policy(
        policyName='string',
        principal='string'
    )
    
    
    :type policyName: string
    :param policyName: [REQUIRED]
            The name of the policy to detach.
            

    :type principal: string
    :param principal: [REQUIRED]
            The principal.
            If the principal is a certificate, specify the certificate ARN. If the principal is an Amazon Cognito identity, specify the identity ID.
            

    """
    pass

def detach_thing_principal(thingName=None, principal=None):
    """
    Detaches the specified principal from the specified thing.
    See also: AWS API Documentation
    
    
    :example: response = client.detach_thing_principal(
        thingName='string',
        principal='string'
    )
    
    
    :type thingName: string
    :param thingName: [REQUIRED]
            The name of the thing.
            

    :type principal: string
    :param principal: [REQUIRED]
            If the principal is a certificate, this value must be ARN of the certificate. If the principal is an Amazon Cognito identity, this value must be the ID of the Amazon Cognito identity.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def disable_topic_rule(ruleName=None):
    """
    Disables the specified rule.
    See also: AWS API Documentation
    
    
    :example: response = client.disable_topic_rule(
        ruleName='string'
    )
    
    
    :type ruleName: string
    :param ruleName: [REQUIRED]
            The name of the rule to disable.
            

    """
    pass

def enable_topic_rule(ruleName=None):
    """
    Enables the specified rule.
    See also: AWS API Documentation
    
    
    :example: response = client.enable_topic_rule(
        ruleName='string'
    )
    
    
    :type ruleName: string
    :param ruleName: [REQUIRED]
            The name of the topic rule to enable.
            

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

def get_logging_options():
    """
    Gets the logging options.
    See also: AWS API Documentation
    
    
    :example: response = client.get_logging_options()
    
    
    :rtype: dict
    :return: {
        'roleArn': 'string',
        'logLevel': 'DEBUG'|'INFO'|'ERROR'|'WARN'|'DISABLED'
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

def get_policy(policyName=None):
    """
    Gets information about the specified policy with the policy document of the default version.
    See also: AWS API Documentation
    
    
    :example: response = client.get_policy(
        policyName='string'
    )
    
    
    :type policyName: string
    :param policyName: [REQUIRED]
            The name of the policy.
            

    :rtype: dict
    :return: {
        'policyName': 'string',
        'policyArn': 'string',
        'policyDocument': 'string',
        'defaultVersionId': 'string'
    }
    
    
    """
    pass

def get_policy_version(policyName=None, policyVersionId=None):
    """
    Gets information about the specified policy version.
    See also: AWS API Documentation
    
    
    :example: response = client.get_policy_version(
        policyName='string',
        policyVersionId='string'
    )
    
    
    :type policyName: string
    :param policyName: [REQUIRED]
            The name of the policy.
            

    :type policyVersionId: string
    :param policyVersionId: [REQUIRED]
            The policy version ID.
            

    :rtype: dict
    :return: {
        'policyArn': 'string',
        'policyName': 'string',
        'policyDocument': 'string',
        'policyVersionId': 'string',
        'isDefaultVersion': True|False
    }
    
    
    """
    pass

def get_registration_code():
    """
    Gets a registration code used to register a CA certificate with AWS IoT.
    See also: AWS API Documentation
    
    
    :example: response = client.get_registration_code()
    
    
    :rtype: dict
    :return: {
        'registrationCode': 'string'
    }
    
    
    """
    pass

def get_topic_rule(ruleName=None):
    """
    Gets information about the specified rule.
    See also: AWS API Documentation
    
    
    :example: response = client.get_topic_rule(
        ruleName='string'
    )
    
    
    :type ruleName: string
    :param ruleName: [REQUIRED]
            The name of the rule.
            

    :rtype: dict
    :return: {
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
    
    
    """
    pass

def get_waiter():
    """
    
    """
    pass

def list_ca_certificates(pageSize=None, marker=None, ascendingOrder=None):
    """
    Lists the CA certificates registered for your AWS account.
    The results are paginated with a default page size of 25. You can use the returned marker to retrieve additional results.
    See also: AWS API Documentation
    
    
    :example: response = client.list_ca_certificates(
        pageSize=123,
        marker='string',
        ascendingOrder=True|False
    )
    
    
    :type pageSize: integer
    :param pageSize: The result page size.

    :type marker: string
    :param marker: The marker for the next set of results.

    :type ascendingOrder: boolean
    :param ascendingOrder: Determines the order of the results.

    :rtype: dict
    :return: {
        'certificates': [
            {
                'certificateArn': 'string',
                'certificateId': 'string',
                'status': 'ACTIVE'|'INACTIVE',
                'creationDate': datetime(2015, 1, 1)
            },
        ],
        'nextMarker': 'string'
    }
    
    
    """
    pass

def list_certificates(pageSize=None, marker=None, ascendingOrder=None):
    """
    Lists the certificates registered in your AWS account.
    The results are paginated with a default page size of 25. You can use the returned marker to retrieve additional results.
    See also: AWS API Documentation
    
    
    :example: response = client.list_certificates(
        pageSize=123,
        marker='string',
        ascendingOrder=True|False
    )
    
    
    :type pageSize: integer
    :param pageSize: The result page size.

    :type marker: string
    :param marker: The marker for the next set of results.

    :type ascendingOrder: boolean
    :param ascendingOrder: Specifies the order for results. If True, the results are returned in ascending order, based on the creation date.

    :rtype: dict
    :return: {
        'certificates': [
            {
                'certificateArn': 'string',
                'certificateId': 'string',
                'status': 'ACTIVE'|'INACTIVE'|'REVOKED'|'PENDING_TRANSFER'|'REGISTER_INACTIVE'|'PENDING_ACTIVATION',
                'creationDate': datetime(2015, 1, 1)
            },
        ],
        'nextMarker': 'string'
    }
    
    
    """
    pass

def list_certificates_by_ca(caCertificateId=None, pageSize=None, marker=None, ascendingOrder=None):
    """
    List the device certificates signed by the specified CA certificate.
    See also: AWS API Documentation
    
    
    :example: response = client.list_certificates_by_ca(
        caCertificateId='string',
        pageSize=123,
        marker='string',
        ascendingOrder=True|False
    )
    
    
    :type caCertificateId: string
    :param caCertificateId: [REQUIRED]
            The ID of the CA certificate. This operation will list all registered device certificate that were signed by this CA certificate.
            

    :type pageSize: integer
    :param pageSize: The result page size.

    :type marker: string
    :param marker: The marker for the next set of results.

    :type ascendingOrder: boolean
    :param ascendingOrder: Specifies the order for results. If True, the results are returned in ascending order, based on the creation date.

    :rtype: dict
    :return: {
        'certificates': [
            {
                'certificateArn': 'string',
                'certificateId': 'string',
                'status': 'ACTIVE'|'INACTIVE'|'REVOKED'|'PENDING_TRANSFER'|'REGISTER_INACTIVE'|'PENDING_ACTIVATION',
                'creationDate': datetime(2015, 1, 1)
            },
        ],
        'nextMarker': 'string'
    }
    
    
    """
    pass

def list_outgoing_certificates(pageSize=None, marker=None, ascendingOrder=None):
    """
    Lists certificates that are being transfered but not yet accepted.
    See also: AWS API Documentation
    
    
    :example: response = client.list_outgoing_certificates(
        pageSize=123,
        marker='string',
        ascendingOrder=True|False
    )
    
    
    :type pageSize: integer
    :param pageSize: The result page size.

    :type marker: string
    :param marker: The marker for the next set of results.

    :type ascendingOrder: boolean
    :param ascendingOrder: Specifies the order for results. If True, the results are returned in ascending order, based on the creation date.

    :rtype: dict
    :return: {
        'outgoingCertificates': [
            {
                'certificateArn': 'string',
                'certificateId': 'string',
                'transferredTo': 'string',
                'transferDate': datetime(2015, 1, 1),
                'transferMessage': 'string',
                'creationDate': datetime(2015, 1, 1)
            },
        ],
        'nextMarker': 'string'
    }
    
    
    """
    pass

def list_policies(marker=None, pageSize=None, ascendingOrder=None):
    """
    Lists your policies.
    See also: AWS API Documentation
    
    
    :example: response = client.list_policies(
        marker='string',
        pageSize=123,
        ascendingOrder=True|False
    )
    
    
    :type marker: string
    :param marker: The marker for the next set of results.

    :type pageSize: integer
    :param pageSize: The result page size.

    :type ascendingOrder: boolean
    :param ascendingOrder: Specifies the order for results. If true, the results are returned in ascending creation order.

    :rtype: dict
    :return: {
        'policies': [
            {
                'policyName': 'string',
                'policyArn': 'string'
            },
        ],
        'nextMarker': 'string'
    }
    
    
    """
    pass

def list_policy_principals(policyName=None, marker=None, pageSize=None, ascendingOrder=None):
    """
    Lists the principals associated with the specified policy.
    See also: AWS API Documentation
    
    
    :example: response = client.list_policy_principals(
        policyName='string',
        marker='string',
        pageSize=123,
        ascendingOrder=True|False
    )
    
    
    :type policyName: string
    :param policyName: [REQUIRED]
            The policy name.
            

    :type marker: string
    :param marker: The marker for the next set of results.

    :type pageSize: integer
    :param pageSize: The result page size.

    :type ascendingOrder: boolean
    :param ascendingOrder: Specifies the order for results. If true, the results are returned in ascending creation order.

    :rtype: dict
    :return: {
        'principals': [
            'string',
        ],
        'nextMarker': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_policy_versions(policyName=None):
    """
    Lists the versions of the specified policy and identifies the default version.
    See also: AWS API Documentation
    
    
    :example: response = client.list_policy_versions(
        policyName='string'
    )
    
    
    :type policyName: string
    :param policyName: [REQUIRED]
            The policy name.
            

    :rtype: dict
    :return: {
        'policyVersions': [
            {
                'versionId': 'string',
                'isDefaultVersion': True|False,
                'createDate': datetime(2015, 1, 1)
            },
        ]
    }
    
    
    """
    pass

def list_principal_policies(principal=None, marker=None, pageSize=None, ascendingOrder=None):
    """
    Lists the policies attached to the specified principal. If you use an Cognito identity, the ID must be in AmazonCognito Identity format .
    See also: AWS API Documentation
    
    
    :example: response = client.list_principal_policies(
        principal='string',
        marker='string',
        pageSize=123,
        ascendingOrder=True|False
    )
    
    
    :type principal: string
    :param principal: [REQUIRED]
            The principal.
            

    :type marker: string
    :param marker: The marker for the next set of results.

    :type pageSize: integer
    :param pageSize: The result page size.

    :type ascendingOrder: boolean
    :param ascendingOrder: Specifies the order for results. If true, results are returned in ascending creation order.

    :rtype: dict
    :return: {
        'policies': [
            {
                'policyName': 'string',
                'policyArn': 'string'
            },
        ],
        'nextMarker': 'string'
    }
    
    
    """
    pass

def list_principal_things(nextToken=None, maxResults=None, principal=None):
    """
    Lists the things associated with the specified principal.
    See also: AWS API Documentation
    
    
    :example: response = client.list_principal_things(
        nextToken='string',
        maxResults=123,
        principal='string'
    )
    
    
    :type nextToken: string
    :param nextToken: The token for the next set of results, or null if there are no additional results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return in this operation.

    :type principal: string
    :param principal: [REQUIRED]
            The principal.
            

    :rtype: dict
    :return: {
        'things': [
            'string',
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_thing_principals(thingName=None):
    """
    Lists the principals associated with the specified thing.
    See also: AWS API Documentation
    
    
    :example: response = client.list_thing_principals(
        thingName='string'
    )
    
    
    :type thingName: string
    :param thingName: [REQUIRED]
            The name of the thing.
            

    :rtype: dict
    :return: {
        'principals': [
            'string',
        ]
    }
    
    
    """
    pass

def list_thing_types(nextToken=None, maxResults=None, thingTypeName=None):
    """
    Lists the existing thing types.
    See also: AWS API Documentation
    
    
    :example: response = client.list_thing_types(
        nextToken='string',
        maxResults=123,
        thingTypeName='string'
    )
    
    
    :type nextToken: string
    :param nextToken: The token for the next set of results, or null if there are no additional results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return in this operation.

    :type thingTypeName: string
    :param thingTypeName: The name of the thing type.

    :rtype: dict
    :return: {
        'thingTypes': [
            {
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
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_things(nextToken=None, maxResults=None, attributeName=None, attributeValue=None, thingTypeName=None):
    """
    Lists your things. Use the attributeName and attributeValue parameters to filter your things. For example, calling ListThings with attributeName=Color and attributeValue=Red retrieves all things in the registry that contain an attribute Color with the value Red .
    See also: AWS API Documentation
    
    
    :example: response = client.list_things(
        nextToken='string',
        maxResults=123,
        attributeName='string',
        attributeValue='string',
        thingTypeName='string'
    )
    
    
    :type nextToken: string
    :param nextToken: The token for the next set of results, or null if there are no additional results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return in this operation.

    :type attributeName: string
    :param attributeName: The attribute name used to search for things.

    :type attributeValue: string
    :param attributeValue: The attribute value used to search for things.

    :type thingTypeName: string
    :param thingTypeName: The name of the thing type used to search for things.

    :rtype: dict
    :return: {
        'things': [
            {
                'thingName': 'string',
                'thingTypeName': 'string',
                'attributes': {
                    'string': 'string'
                },
                'version': 123
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) -- An attribute value for an Thing. An empty or null value in Update means that existing value for that attribute should be deleted. Empty and null values in create are ignored.
    
    
    
    """
    pass

def list_topic_rules(topic=None, maxResults=None, nextToken=None, ruleDisabled=None):
    """
    Lists the rules for the specific topic.
    See also: AWS API Documentation
    
    
    :example: response = client.list_topic_rules(
        topic='string',
        maxResults=123,
        nextToken='string',
        ruleDisabled=True|False
    )
    
    
    :type topic: string
    :param topic: The topic.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return.

    :type nextToken: string
    :param nextToken: A token used to retrieve the next value.

    :type ruleDisabled: boolean
    :param ruleDisabled: Specifies whether the rule is disabled.

    :rtype: dict
    :return: {
        'rules': [
            {
                'ruleArn': 'string',
                'ruleName': 'string',
                'topicPattern': 'string',
                'createdAt': datetime(2015, 1, 1),
                'ruleDisabled': True|False
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def register_ca_certificate(caCertificate=None, verificationCertificate=None, setAsActive=None, allowAutoRegistration=None):
    """
    Registers a CA certificate with AWS IoT. This CA certificate can then be used to sign device certificates, which can be then registered with AWS IoT. You can register up to 10 CA certificates per AWS account that have the same subject field and public key. This enables you to have up to 10 certificate authorities sign your device certificates. If you have more than one CA certificate registered, make sure you pass the CA certificate when you register your device certificates with the RegisterCertificate API.
    See also: AWS API Documentation
    
    
    :example: response = client.register_ca_certificate(
        caCertificate='string',
        verificationCertificate='string',
        setAsActive=True|False,
        allowAutoRegistration=True|False
    )
    
    
    :type caCertificate: string
    :param caCertificate: [REQUIRED]
            The CA certificate.
            

    :type verificationCertificate: string
    :param verificationCertificate: [REQUIRED]
            The private key verification certificate.
            

    :type setAsActive: boolean
    :param setAsActive: A boolean value that specifies if the CA certificate is set to active.

    :type allowAutoRegistration: boolean
    :param allowAutoRegistration: Allows this CA certificate to be used for auto registration of device certificates.

    :rtype: dict
    :return: {
        'certificateArn': 'string',
        'certificateId': 'string'
    }
    
    
    """
    pass

def register_certificate(certificatePem=None, caCertificatePem=None, setAsActive=None, status=None):
    """
    Registers a device certificate with AWS IoT. If you have more than one CA certificate that has the same subject field, you must specify the CA certificate that was used to sign the device certificate being registered.
    See also: AWS API Documentation
    
    
    :example: response = client.register_certificate(
        certificatePem='string',
        caCertificatePem='string',
        setAsActive=True|False,
        status='ACTIVE'|'INACTIVE'|'REVOKED'|'PENDING_TRANSFER'|'REGISTER_INACTIVE'|'PENDING_ACTIVATION'
    )
    
    
    :type certificatePem: string
    :param certificatePem: [REQUIRED]
            The certificate data, in PEM format.
            

    :type caCertificatePem: string
    :param caCertificatePem: The CA certificate used to sign the device certificate being registered.

    :type setAsActive: boolean
    :param setAsActive: A boolean value that specifies if the CA certificate is set to active.

    :type status: string
    :param status: 

    :rtype: dict
    :return: {
        'certificateArn': 'string',
        'certificateId': 'string'
    }
    
    
    """
    pass

def reject_certificate_transfer(certificateId=None, rejectReason=None):
    """
    Rejects a pending certificate transfer. After AWS IoT rejects a certificate transfer, the certificate status changes from PENDING_TRANSFER to INACTIVE .
    To check for pending certificate transfers, call  ListCertificates to enumerate your certificates.
    This operation can only be called by the transfer destination. After it is called, the certificate will be returned to the source's account in the INACTIVE state.
    See also: AWS API Documentation
    
    
    :example: response = client.reject_certificate_transfer(
        certificateId='string',
        rejectReason='string'
    )
    
    
    :type certificateId: string
    :param certificateId: [REQUIRED]
            The ID of the certificate.
            

    :type rejectReason: string
    :param rejectReason: The reason the certificate transfer was rejected.

    """
    pass

def replace_topic_rule(ruleName=None, topicRulePayload=None):
    """
    Replaces the specified rule. You must specify all parameters for the new rule. Creating rules is an administrator-level action. Any user who has permission to create rules will be able to access data processed by the rule.
    See also: AWS API Documentation
    
    
    :example: response = client.replace_topic_rule(
        ruleName='string',
        topicRulePayload={
            'sql': 'string',
            'description': 'string',
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
    )
    
    
    :type ruleName: string
    :param ruleName: [REQUIRED]
            The name of the rule.
            

    :type topicRulePayload: dict
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
            

    """
    pass

def set_default_policy_version(policyName=None, policyVersionId=None):
    """
    Sets the specified version of the specified policy as the policy's default (operative) version. This action affects all certificates to which the policy is attached. To list the principals the policy is attached to, use the ListPrincipalPolicy API.
    See also: AWS API Documentation
    
    
    :example: response = client.set_default_policy_version(
        policyName='string',
        policyVersionId='string'
    )
    
    
    :type policyName: string
    :param policyName: [REQUIRED]
            The policy name.
            

    :type policyVersionId: string
    :param policyVersionId: [REQUIRED]
            The policy version ID.
            

    """
    pass

def set_logging_options(loggingOptionsPayload=None):
    """
    Sets the logging options.
    See also: AWS API Documentation
    
    
    :example: response = client.set_logging_options(
        loggingOptionsPayload={
            'roleArn': 'string',
            'logLevel': 'DEBUG'|'INFO'|'ERROR'|'WARN'|'DISABLED'
        }
    )
    
    
    :type loggingOptionsPayload: dict
    :param loggingOptionsPayload: [REQUIRED]
            The logging options payload.
            roleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access.
            logLevel (string) --The logging level.
            

    """
    pass

def transfer_certificate(certificateId=None, targetAwsAccount=None, transferMessage=None):
    """
    Transfers the specified certificate to the specified AWS account.
    You can cancel the transfer until it is acknowledged by the recipient.
    No notification is sent to the transfer destination's account. It is up to the caller to notify the transfer target.
    The certificate being transferred must not be in the ACTIVE state. You can use the UpdateCertificate API to deactivate it.
    The certificate must not have any policies attached to it. You can use the DetachPrincipalPolicy API to detach them.
    See also: AWS API Documentation
    
    
    :example: response = client.transfer_certificate(
        certificateId='string',
        targetAwsAccount='string',
        transferMessage='string'
    )
    
    
    :type certificateId: string
    :param certificateId: [REQUIRED]
            The ID of the certificate.
            

    :type targetAwsAccount: string
    :param targetAwsAccount: [REQUIRED]
            The AWS account.
            

    :type transferMessage: string
    :param transferMessage: The transfer message.

    :rtype: dict
    :return: {
        'transferredCertificateArn': 'string'
    }
    
    
    """
    pass

def update_ca_certificate(certificateId=None, newStatus=None, newAutoRegistrationStatus=None):
    """
    Updates a registered CA certificate.
    See also: AWS API Documentation
    
    
    :example: response = client.update_ca_certificate(
        certificateId='string',
        newStatus='ACTIVE'|'INACTIVE',
        newAutoRegistrationStatus='ENABLE'|'DISABLE'
    )
    
    
    :type certificateId: string
    :param certificateId: [REQUIRED]
            The CA certificate identifier.
            

    :type newStatus: string
    :param newStatus: The updated status of the CA certificate.
            Note: The status value REGISTER_INACTIVE is deprecated and should not be used.
            

    :type newAutoRegistrationStatus: string
    :param newAutoRegistrationStatus: The new value for the auto registration status. Valid values are: 'ENABLE' or 'DISABLE'.

    """
    pass

def update_certificate(certificateId=None, newStatus=None):
    """
    Updates the status of the specified certificate. This operation is idempotent.
    Moving a certificate from the ACTIVE state (including REVOKED) will not disconnect currently connected devices, but these devices will be unable to reconnect.
    The ACTIVE state is required to authenticate devices connecting to AWS IoT using a certificate.
    See also: AWS API Documentation
    
    
    :example: response = client.update_certificate(
        certificateId='string',
        newStatus='ACTIVE'|'INACTIVE'|'REVOKED'|'PENDING_TRANSFER'|'REGISTER_INACTIVE'|'PENDING_ACTIVATION'
    )
    
    
    :type certificateId: string
    :param certificateId: [REQUIRED]
            The ID of the certificate.
            

    :type newStatus: string
    :param newStatus: [REQUIRED]
            The new status.
            Note: Setting the status to PENDING_TRANSFER will result in an exception being thrown. PENDING_TRANSFER is a status used internally by AWS IoT. It is not intended for developer use.
            Note: The status value REGISTER_INACTIVE is deprecated and should not be used.
            

    """
    pass

def update_thing(thingName=None, thingTypeName=None, attributePayload=None, expectedVersion=None, removeThingType=None):
    """
    Updates the data for a thing.
    See also: AWS API Documentation
    
    
    :example: response = client.update_thing(
        thingName='string',
        thingTypeName='string',
        attributePayload={
            'attributes': {
                'string': 'string'
            },
            'merge': True|False
        },
        expectedVersion=123,
        removeThingType=True|False
    )
    
    
    :type thingName: string
    :param thingName: [REQUIRED]
            The name of the thing to update.
            

    :type thingTypeName: string
    :param thingTypeName: The name of the thing type.

    :type attributePayload: dict
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
            

    :type expectedVersion: integer
    :param expectedVersion: The expected version of the thing record in the registry. If the version of the record in the registry does not match the expected version specified in the request, the UpdateThing request is rejected with a VersionConflictException .

    :type removeThingType: boolean
    :param removeThingType: Remove a thing type association. If true , the assocation is removed.

    :rtype: dict
    :return: {}
    
    
    """
    pass

