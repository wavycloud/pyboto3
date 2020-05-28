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

def accept_invitation(MasterId=None, InvitationId=None):
    """
    Accepts the invitation to be a member account and be monitored by the Security Hub master account that the invitation was sent from.
    When the member account accepts the invitation, permission is granted to the master account to view findings generated in the member account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.accept_invitation(
        MasterId='string',
        InvitationId='string'
    )
    
    
    :type MasterId: string
    :param MasterId: [REQUIRED]\nThe account ID of the Security Hub master account that sent the invitation.\n

    :type InvitationId: string
    :param InvitationId: [REQUIRED]\nThe ID of the invitation sent from the Security Hub master account.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

SecurityHub.Client.exceptions.InternalException
SecurityHub.Client.exceptions.InvalidInputException
SecurityHub.Client.exceptions.LimitExceededException
SecurityHub.Client.exceptions.ResourceNotFoundException
SecurityHub.Client.exceptions.InvalidAccessException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def batch_disable_standards(StandardsSubscriptionArns=None):
    """
    Disables the standards specified by the provided StandardsSubscriptionArns .
    For more information, see Security Standards section of the AWS Security Hub User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_disable_standards(
        StandardsSubscriptionArns=[
            'string',
        ]
    )
    
    
    :type StandardsSubscriptionArns: list
    :param StandardsSubscriptionArns: [REQUIRED]\nThe ARNs of the standards subscriptions to disable.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'StandardsSubscriptions': [
        {
            'StandardsSubscriptionArn': 'string',
            'StandardsArn': 'string',
            'StandardsInput': {
                'string': 'string'
            },
            'StandardsStatus': 'PENDING'|'READY'|'FAILED'|'DELETING'|'INCOMPLETE'
        },
    ]
}


Response Structure

(dict) --
StandardsSubscriptions (list) --The details of the standards subscriptions that were disabled.

(dict) --A resource that represents your subscription to a supported standard.

StandardsSubscriptionArn (string) --The ARN of a resource that represents your subscription to a supported standard.

StandardsArn (string) --The ARN of a standard.

StandardsInput (dict) --A key-value pair of input for the standard.

(string) --
(string) --




StandardsStatus (string) --The status of the standards subscription.










Exceptions

SecurityHub.Client.exceptions.InternalException
SecurityHub.Client.exceptions.InvalidInputException
SecurityHub.Client.exceptions.InvalidAccessException
SecurityHub.Client.exceptions.LimitExceededException


    :return: {
        'StandardsSubscriptions': [
            {
                'StandardsSubscriptionArn': 'string',
                'StandardsArn': 'string',
                'StandardsInput': {
                    'string': 'string'
                },
                'StandardsStatus': 'PENDING'|'READY'|'FAILED'|'DELETING'|'INCOMPLETE'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def batch_enable_standards(StandardsSubscriptionRequests=None):
    """
    Enables the standards specified by the provided StandardsArn . To obtain the ARN for a standard, use the ``  DescribeStandards `` operation.
    For more information, see the Security Standards section of the AWS Security Hub User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_enable_standards(
        StandardsSubscriptionRequests=[
            {
                'StandardsArn': 'string',
                'StandardsInput': {
                    'string': 'string'
                }
            },
        ]
    )
    
    
    :type StandardsSubscriptionRequests: list
    :param StandardsSubscriptionRequests: [REQUIRED]\nThe list of standards checks to enable.\n\n(dict) --The standard that you want to enable.\n\nStandardsArn (string) -- [REQUIRED]The ARN of the standard that you want to enable. To view the list of available standards and their ARNs, use the `` DescribeStandards `` operation.\n\nStandardsInput (dict) --A key-value pair of input for the standard.\n\n(string) --\n(string) --\n\n\n\n\n\n\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'StandardsSubscriptions': [
        {
            'StandardsSubscriptionArn': 'string',
            'StandardsArn': 'string',
            'StandardsInput': {
                'string': 'string'
            },
            'StandardsStatus': 'PENDING'|'READY'|'FAILED'|'DELETING'|'INCOMPLETE'
        },
    ]
}


Response Structure

(dict) --
StandardsSubscriptions (list) --The details of the standards subscriptions that were enabled.

(dict) --A resource that represents your subscription to a supported standard.

StandardsSubscriptionArn (string) --The ARN of a resource that represents your subscription to a supported standard.

StandardsArn (string) --The ARN of a standard.

StandardsInput (dict) --A key-value pair of input for the standard.

(string) --
(string) --




StandardsStatus (string) --The status of the standards subscription.










Exceptions

SecurityHub.Client.exceptions.InternalException
SecurityHub.Client.exceptions.InvalidInputException
SecurityHub.Client.exceptions.InvalidAccessException
SecurityHub.Client.exceptions.LimitExceededException


    :return: {
        'StandardsSubscriptions': [
            {
                'StandardsSubscriptionArn': 'string',
                'StandardsArn': 'string',
                'StandardsInput': {
                    'string': 'string'
                },
                'StandardsStatus': 'PENDING'|'READY'|'FAILED'|'DELETING'|'INCOMPLETE'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def batch_import_findings(Findings=None):
    """
    Imports security findings generated from an integrated third-party product into Security Hub. This action is requested by the integrated product to import its findings into Security Hub.
    The maximum allowed size for a finding is 240 Kb. An error is returned for any finding larger than 240 Kb.
    After a finding is created, BatchImportFindings cannot be used to update the following finding fields and objects, which Security Hub customers use to manage their investigation workflow.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_import_findings(
        Findings=[
            {
                'SchemaVersion': 'string',
                'Id': 'string',
                'ProductArn': 'string',
                'GeneratorId': 'string',
                'AwsAccountId': 'string',
                'Types': [
                    'string',
                ],
                'FirstObservedAt': 'string',
                'LastObservedAt': 'string',
                'CreatedAt': 'string',
                'UpdatedAt': 'string',
                'Severity': {
                    'Product': 123.0,
                    'Label': 'INFORMATIONAL'|'LOW'|'MEDIUM'|'HIGH'|'CRITICAL',
                    'Normalized': 123,
                    'Original': 'string'
                },
                'Confidence': 123,
                'Criticality': 123,
                'Title': 'string',
                'Description': 'string',
                'Remediation': {
                    'Recommendation': {
                        'Text': 'string',
                        'Url': 'string'
                    }
                },
                'SourceUrl': 'string',
                'ProductFields': {
                    'string': 'string'
                },
                'UserDefinedFields': {
                    'string': 'string'
                },
                'Malware': [
                    {
                        'Name': 'string',
                        'Type': 'ADWARE'|'BLENDED_THREAT'|'BOTNET_AGENT'|'COIN_MINER'|'EXPLOIT_KIT'|'KEYLOGGER'|'MACRO'|'POTENTIALLY_UNWANTED'|'SPYWARE'|'RANSOMWARE'|'REMOTE_ACCESS'|'ROOTKIT'|'TROJAN'|'VIRUS'|'WORM',
                        'Path': 'string',
                        'State': 'OBSERVED'|'REMOVAL_FAILED'|'REMOVED'
                    },
                ],
                'Network': {
                    'Direction': 'IN'|'OUT',
                    'Protocol': 'string',
                    'SourceIpV4': 'string',
                    'SourceIpV6': 'string',
                    'SourcePort': 123,
                    'SourceDomain': 'string',
                    'SourceMac': 'string',
                    'DestinationIpV4': 'string',
                    'DestinationIpV6': 'string',
                    'DestinationPort': 123,
                    'DestinationDomain': 'string'
                },
                'Process': {
                    'Name': 'string',
                    'Path': 'string',
                    'Pid': 123,
                    'ParentPid': 123,
                    'LaunchedAt': 'string',
                    'TerminatedAt': 'string'
                },
                'ThreatIntelIndicators': [
                    {
                        'Type': 'DOMAIN'|'EMAIL_ADDRESS'|'HASH_MD5'|'HASH_SHA1'|'HASH_SHA256'|'HASH_SHA512'|'IPV4_ADDRESS'|'IPV6_ADDRESS'|'MUTEX'|'PROCESS'|'URL',
                        'Value': 'string',
                        'Category': 'BACKDOOR'|'CARD_STEALER'|'COMMAND_AND_CONTROL'|'DROP_SITE'|'EXPLOIT_SITE'|'KEYLOGGER',
                        'LastObservedAt': 'string',
                        'Source': 'string',
                        'SourceUrl': 'string'
                    },
                ],
                'Resources': [
                    {
                        'Type': 'string',
                        'Id': 'string',
                        'Partition': 'aws'|'aws-cn'|'aws-us-gov',
                        'Region': 'string',
                        'Tags': {
                            'string': 'string'
                        },
                        'Details': {
                            'AwsCodeBuildProject': {
                                'EncryptionKey': 'string',
                                'Environment': {
                                    'Certificate': 'string',
                                    'ImagePullCredentialsType': 'string',
                                    'RegistryCredential': {
                                        'Credential': 'string',
                                        'CredentialProvider': 'string'
                                    },
                                    'Type': 'string'
                                },
                                'Name': 'string',
                                'Source': {
                                    'Type': 'string',
                                    'Location': 'string',
                                    'GitCloneDepth': 123,
                                    'InsecureSsl': True|False
                                },
                                'ServiceRole': 'string',
                                'VpcConfig': {
                                    'VpcId': 'string',
                                    'Subnets': [
                                        'string',
                                    ],
                                    'SecurityGroupIds': [
                                        'string',
                                    ]
                                }
                            },
                            'AwsCloudFrontDistribution': {
                                'DomainName': 'string',
                                'ETag': 'string',
                                'LastModifiedTime': 'string',
                                'Logging': {
                                    'Bucket': 'string',
                                    'Enabled': True|False,
                                    'IncludeCookies': True|False,
                                    'Prefix': 'string'
                                },
                                'Origins': {
                                    'Items': [
                                        {
                                            'DomainName': 'string',
                                            'Id': 'string',
                                            'OriginPath': 'string'
                                        },
                                    ]
                                },
                                'Status': 'string',
                                'WebAclId': 'string'
                            },
                            'AwsEc2Instance': {
                                'Type': 'string',
                                'ImageId': 'string',
                                'IpV4Addresses': [
                                    'string',
                                ],
                                'IpV6Addresses': [
                                    'string',
                                ],
                                'KeyName': 'string',
                                'IamInstanceProfileArn': 'string',
                                'VpcId': 'string',
                                'SubnetId': 'string',
                                'LaunchedAt': 'string'
                            },
                            'AwsEc2NetworkInterface': {
                                'Attachment': {
                                    'AttachTime': 'string',
                                    'AttachmentId': 'string',
                                    'DeleteOnTermination': True|False,
                                    'DeviceIndex': 123,
                                    'InstanceId': 'string',
                                    'InstanceOwnerId': 'string',
                                    'Status': 'string'
                                },
                                'NetworkInterfaceId': 'string',
                                'SecurityGroups': [
                                    {
                                        'GroupName': 'string',
                                        'GroupId': 'string'
                                    },
                                ],
                                'SourceDestCheck': True|False
                            },
                            'AwsEc2SecurityGroup': {
                                'GroupName': 'string',
                                'GroupId': 'string',
                                'OwnerId': 'string',
                                'VpcId': 'string',
                                'IpPermissions': [
                                    {
                                        'IpProtocol': 'string',
                                        'FromPort': 123,
                                        'ToPort': 123,
                                        'UserIdGroupPairs': [
                                            {
                                                'GroupId': 'string',
                                                'GroupName': 'string',
                                                'PeeringStatus': 'string',
                                                'UserId': 'string',
                                                'VpcId': 'string',
                                                'VpcPeeringConnectionId': 'string'
                                            },
                                        ],
                                        'IpRanges': [
                                            {
                                                'CidrIp': 'string'
                                            },
                                        ],
                                        'Ipv6Ranges': [
                                            {
                                                'CidrIpv6': 'string'
                                            },
                                        ],
                                        'PrefixListIds': [
                                            {
                                                'PrefixListId': 'string'
                                            },
                                        ]
                                    },
                                ],
                                'IpPermissionsEgress': [
                                    {
                                        'IpProtocol': 'string',
                                        'FromPort': 123,
                                        'ToPort': 123,
                                        'UserIdGroupPairs': [
                                            {
                                                'GroupId': 'string',
                                                'GroupName': 'string',
                                                'PeeringStatus': 'string',
                                                'UserId': 'string',
                                                'VpcId': 'string',
                                                'VpcPeeringConnectionId': 'string'
                                            },
                                        ],
                                        'IpRanges': [
                                            {
                                                'CidrIp': 'string'
                                            },
                                        ],
                                        'Ipv6Ranges': [
                                            {
                                                'CidrIpv6': 'string'
                                            },
                                        ],
                                        'PrefixListIds': [
                                            {
                                                'PrefixListId': 'string'
                                            },
                                        ]
                                    },
                                ]
                            },
                            'AwsElbv2LoadBalancer': {
                                'AvailabilityZones': [
                                    {
                                        'ZoneName': 'string',
                                        'SubnetId': 'string'
                                    },
                                ],
                                'CanonicalHostedZoneId': 'string',
                                'CreatedTime': 'string',
                                'DNSName': 'string',
                                'IpAddressType': 'string',
                                'Scheme': 'string',
                                'SecurityGroups': [
                                    'string',
                                ],
                                'State': {
                                    'Code': 'string',
                                    'Reason': 'string'
                                },
                                'Type': 'string',
                                'VpcId': 'string'
                            },
                            'AwsElasticsearchDomain': {
                                'AccessPolicies': 'string',
                                'DomainEndpointOptions': {
                                    'EnforceHTTPS': True|False,
                                    'TLSSecurityPolicy': 'string'
                                },
                                'DomainId': 'string',
                                'DomainName': 'string',
                                'Endpoint': 'string',
                                'Endpoints': {
                                    'string': 'string'
                                },
                                'ElasticsearchVersion': 'string',
                                'EncryptionAtRestOptions': {
                                    'Enabled': True|False,
                                    'KmsKeyId': 'string'
                                },
                                'NodeToNodeEncryptionOptions': {
                                    'Enabled': True|False
                                },
                                'VPCOptions': {
                                    'AvailabilityZones': [
                                        'string',
                                    ],
                                    'SecurityGroupIds': [
                                        'string',
                                    ],
                                    'SubnetIds': [
                                        'string',
                                    ],
                                    'VPCId': 'string'
                                }
                            },
                            'AwsS3Bucket': {
                                'OwnerId': 'string',
                                'OwnerName': 'string',
                                'CreatedAt': 'string',
                                'ServerSideEncryptionConfiguration': {
                                    'Rules': [
                                        {
                                            'ApplyServerSideEncryptionByDefault': {
                                                'SSEAlgorithm': 'string',
                                                'KMSMasterKeyID': 'string'
                                            }
                                        },
                                    ]
                                }
                            },
                            'AwsS3Object': {
                                'LastModified': 'string',
                                'ETag': 'string',
                                'VersionId': 'string',
                                'ContentType': 'string',
                                'ServerSideEncryption': 'string',
                                'SSEKMSKeyId': 'string'
                            },
                            'AwsIamAccessKey': {
                                'UserName': 'string',
                                'Status': 'Active'|'Inactive',
                                'CreatedAt': 'string',
                                'PrincipalId': 'string',
                                'PrincipalType': 'string',
                                'PrincipalName': 'string'
                            },
                            'AwsIamRole': {
                                'AssumeRolePolicyDocument': 'string',
                                'CreateDate': 'string',
                                'RoleId': 'string',
                                'RoleName': 'string',
                                'MaxSessionDuration': 123,
                                'Path': 'string'
                            },
                            'AwsKmsKey': {
                                'AWSAccountId': 'string',
                                'CreationDate': 123.0,
                                'KeyId': 'string',
                                'KeyManager': 'string',
                                'KeyState': 'string',
                                'Origin': 'string'
                            },
                            'AwsLambdaFunction': {
                                'Code': {
                                    'S3Bucket': 'string',
                                    'S3Key': 'string',
                                    'S3ObjectVersion': 'string',
                                    'ZipFile': 'string'
                                },
                                'CodeSha256': 'string',
                                'DeadLetterConfig': {
                                    'TargetArn': 'string'
                                },
                                'Environment': {
                                    'Variables': {
                                        'string': 'string'
                                    },
                                    'Error': {
                                        'ErrorCode': 'string',
                                        'Message': 'string'
                                    }
                                },
                                'FunctionName': 'string',
                                'Handler': 'string',
                                'KmsKeyArn': 'string',
                                'LastModified': 'string',
                                'Layers': [
                                    {
                                        'Arn': 'string',
                                        'CodeSize': 123
                                    },
                                ],
                                'MasterArn': 'string',
                                'MemorySize': 123,
                                'RevisionId': 'string',
                                'Role': 'string',
                                'Runtime': 'string',
                                'Timeout': 123,
                                'TracingConfig': {
                                    'Mode': 'string'
                                },
                                'VpcConfig': {
                                    'SecurityGroupIds': [
                                        'string',
                                    ],
                                    'SubnetIds': [
                                        'string',
                                    ],
                                    'VpcId': 'string'
                                },
                                'Version': 'string'
                            },
                            'AwsLambdaLayerVersion': {
                                'Version': 123,
                                'CompatibleRuntimes': [
                                    'string',
                                ],
                                'CreatedDate': 'string'
                            },
                            'AwsRdsDbInstance': {
                                'AssociatedRoles': [
                                    {
                                        'RoleArn': 'string',
                                        'FeatureName': 'string',
                                        'Status': 'string'
                                    },
                                ],
                                'CACertificateIdentifier': 'string',
                                'DBClusterIdentifier': 'string',
                                'DBInstanceIdentifier': 'string',
                                'DBInstanceClass': 'string',
                                'DbInstancePort': 123,
                                'DbiResourceId': 'string',
                                'DBName': 'string',
                                'DeletionProtection': True|False,
                                'Endpoint': {
                                    'Address': 'string',
                                    'Port': 123,
                                    'HostedZoneId': 'string'
                                },
                                'Engine': 'string',
                                'EngineVersion': 'string',
                                'IAMDatabaseAuthenticationEnabled': True|False,
                                'InstanceCreateTime': 'string',
                                'KmsKeyId': 'string',
                                'PubliclyAccessible': True|False,
                                'StorageEncrypted': True|False,
                                'TdeCredentialArn': 'string',
                                'VpcSecurityGroups': [
                                    {
                                        'VpcSecurityGroupId': 'string',
                                        'Status': 'string'
                                    },
                                ]
                            },
                            'AwsSnsTopic': {
                                'KmsMasterKeyId': 'string',
                                'Subscription': [
                                    {
                                        'Endpoint': 'string',
                                        'Protocol': 'string'
                                    },
                                ],
                                'TopicName': 'string',
                                'Owner': 'string'
                            },
                            'AwsSqsQueue': {
                                'KmsDataKeyReusePeriodSeconds': 123,
                                'KmsMasterKeyId': 'string',
                                'QueueName': 'string',
                                'DeadLetterTargetArn': 'string'
                            },
                            'AwsWafWebAcl': {
                                'Name': 'string',
                                'DefaultAction': 'string',
                                'Rules': [
                                    {
                                        'Action': {
                                            'Type': 'string'
                                        },
                                        'ExcludedRules': [
                                            {
                                                'RuleId': 'string'
                                            },
                                        ],
                                        'OverrideAction': {
                                            'Type': 'string'
                                        },
                                        'Priority': 123,
                                        'RuleId': 'string',
                                        'Type': 'string'
                                    },
                                ],
                                'WebAclId': 'string'
                            },
                            'Container': {
                                'Name': 'string',
                                'ImageId': 'string',
                                'ImageName': 'string',
                                'LaunchedAt': 'string'
                            },
                            'Other': {
                                'string': 'string'
                            }
                        }
                    },
                ],
                'Compliance': {
                    'Status': 'PASSED'|'WARNING'|'FAILED'|'NOT_AVAILABLE',
                    'RelatedRequirements': [
                        'string',
                    ],
                    'StatusReasons': [
                        {
                            'ReasonCode': 'string',
                            'Description': 'string'
                        },
                    ]
                },
                'VerificationState': 'UNKNOWN'|'TRUE_POSITIVE'|'FALSE_POSITIVE'|'BENIGN_POSITIVE',
                'WorkflowState': 'NEW'|'ASSIGNED'|'IN_PROGRESS'|'DEFERRED'|'RESOLVED',
                'Workflow': {
                    'Status': 'NEW'|'NOTIFIED'|'RESOLVED'|'SUPPRESSED'
                },
                'RecordState': 'ACTIVE'|'ARCHIVED',
                'RelatedFindings': [
                    {
                        'ProductArn': 'string',
                        'Id': 'string'
                    },
                ],
                'Note': {
                    'Text': 'string',
                    'UpdatedBy': 'string',
                    'UpdatedAt': 'string'
                }
            },
        ]
    )
    
    
    :type Findings: list
    :param Findings: [REQUIRED]\nA list of findings to import. To successfully import a finding, it must follow the AWS Security Finding Format . Maximum of 100 findings per request.\n\n(dict) --Provides consistent format for the contents of the Security Hub-aggregated findings. AwsSecurityFinding format enables you to share findings between AWS security services and third-party solutions, and security standards checks.\n\nNote\nA finding is a potential security issue generated either by AWS services (Amazon GuardDuty, Amazon Inspector, and Amazon Macie) or by the integrated third-party solutions and standards checks.\n\n\nSchemaVersion (string) -- [REQUIRED]The schema version that a finding is formatted for.\n\nId (string) -- [REQUIRED]The security findings provider-specific identifier for a finding.\n\nProductArn (string) -- [REQUIRED]The ARN generated by Security Hub that uniquely identifies a product that generates findings. This can be the ARN for a third-party product that is integrated with Security Hub, or the ARN for a custom integration.\n\nGeneratorId (string) -- [REQUIRED]The identifier for the solution-specific component (a discrete unit of logic) that generated a finding. In various security-findings providers\' solutions, this generator can be called a rule, a check, a detector, a plugin, etc.\n\nAwsAccountId (string) -- [REQUIRED]The AWS account ID that a finding is generated in.\n\nTypes (list) -- [REQUIRED]One or more finding types in the format of namespace/category/classifier that classify a finding.\nValid namespace values are: Software and Configuration Checks | TTPs | Effects | Unusual Behaviors | Sensitive Data Identifications\n\n(string) --\n\n\nFirstObservedAt (string) --An ISO8601-formatted timestamp that indicates when the security-findings provider first observed the potential security issue that a finding captured.\n\nLastObservedAt (string) --An ISO8601-formatted timestamp that indicates when the security-findings provider most recently observed the potential security issue that a finding captured.\n\nCreatedAt (string) -- [REQUIRED]An ISO8601-formatted timestamp that indicates when the security-findings provider created the potential security issue that a finding captured.\n\nUpdatedAt (string) -- [REQUIRED]An ISO8601-formatted timestamp that indicates when the security-findings provider last updated the finding record.\n\nSeverity (dict) -- [REQUIRED]A finding\'s severity.\n\nProduct (float) --Deprecated. This attribute is being deprecated. Instead of providing Product , provide Original .\nThe native severity as defined by the AWS service or integrated partner product that generated the finding.\n\nLabel (string) --The severity value of the finding. The allowed values are the following.\n\nINFORMATIONAL - No issue was found.\nLOW - The issue does not require action on its own.\nMEDIUM - The issue must be addressed but not urgently.\nHIGH - The issue must be addressed as a priority.\nCRITICAL - The issue must be remediated immediately to avoid it escalating.\n\n\nNormalized (integer) --Deprecated. This attribute is being deprecated. Instead of providing Normalized , provide Label .\nIf you provide Normalized and do not provide Label , Label is set automatically as follows.\n\n0 - INFORMATIONAL\n1\xe2\x80\x9339 - LOW\n40\xe2\x80\x9369 - MEDIUM\n70\xe2\x80\x9389 - HIGH\n90\xe2\x80\x93100 - CRITICAL\n\n\nOriginal (string) --The native severity from the finding product that generated the finding.\n\n\n\nConfidence (integer) --A finding\'s confidence. Confidence is defined as the likelihood that a finding accurately identifies the behavior or issue that it was intended to identify.\nConfidence is scored on a 0-100 basis using a ratio scale, where 0 means zero percent confidence and 100 means 100 percent confidence.\n\nCriticality (integer) --The level of importance assigned to the resources associated with the finding.\nA score of 0 means that the underlying resources have no criticality, and a score of 100 is reserved for the most critical resources.\n\nTitle (string) -- [REQUIRED]A finding\'s title.\n\nNote\nIn this release, Title is a required property.\n\n\nDescription (string) -- [REQUIRED]A finding\'s description.\n\nNote\nIn this release, Description is a required property.\n\n\nRemediation (dict) --A data type that describes the remediation options for a finding.\n\nRecommendation (dict) --A recommendation on the steps to take to remediate the issue identified by a finding.\n\nText (string) --Describes the recommended steps to take to remediate an issue identified in a finding.\n\nUrl (string) --A URL to a page or site that contains information about how to remediate a finding.\n\n\n\n\n\nSourceUrl (string) --A URL that links to a page about the current finding in the security-findings provider\'s solution.\n\nProductFields (dict) --A data type where security-findings providers can include additional solution-specific details that aren\'t part of the defined AwsSecurityFinding format.\n\n(string) --\n(string) --\n\n\n\n\nUserDefinedFields (dict) --A list of name/value string pairs associated with the finding. These are custom, user-defined fields added to a finding.\n\n(string) --\n(string) --\n\n\n\n\nMalware (list) --A list of malware related to a finding.\n\n(dict) --A list of malware related to a finding.\n\nName (string) -- [REQUIRED]The name of the malware that was observed.\n\nType (string) --The type of the malware that was observed.\n\nPath (string) --The file system path of the malware that was observed.\n\nState (string) --The state of the malware that was observed.\n\n\n\n\n\nNetwork (dict) --The details of network-related information about a finding.\n\nDirection (string) --The direction of network traffic associated with a finding.\n\nProtocol (string) --The protocol of network-related information about a finding.\n\nSourceIpV4 (string) --The source IPv4 address of network-related information about a finding.\n\nSourceIpV6 (string) --The source IPv6 address of network-related information about a finding.\n\nSourcePort (integer) --The source port of network-related information about a finding.\n\nSourceDomain (string) --The source domain of network-related information about a finding.\n\nSourceMac (string) --The source media access control (MAC) address of network-related information about a finding.\n\nDestinationIpV4 (string) --The destination IPv4 address of network-related information about a finding.\n\nDestinationIpV6 (string) --The destination IPv6 address of network-related information about a finding.\n\nDestinationPort (integer) --The destination port of network-related information about a finding.\n\nDestinationDomain (string) --The destination domain of network-related information about a finding.\n\n\n\nProcess (dict) --The details of process-related information about a finding.\n\nName (string) --The name of the process.\n\nPath (string) --The path to the process executable.\n\nPid (integer) --The process ID.\n\nParentPid (integer) --The parent process ID.\n\nLaunchedAt (string) --The date/time that the process was launched.\n\nTerminatedAt (string) --The date and time when the process was terminated.\n\n\n\nThreatIntelIndicators (list) --Threat intelligence details related to a finding.\n\n(dict) --Details about the threat intelligence related to a finding.\n\nType (string) --The type of threat intelligence indicator.\n\nValue (string) --The value of a threat intelligence indicator.\n\nCategory (string) --The category of a threat intelligence indicator.\n\nLastObservedAt (string) --The date and time when the most recent instance of a threat intelligence indicator was observed.\n\nSource (string) --The source of the threat intelligence indicator.\n\nSourceUrl (string) --The URL to the page or site where you can get more information about the threat intelligence indicator.\n\n\n\n\n\nResources (list) -- [REQUIRED]A set of resource data types that describe the resources that the finding refers to.\n\n(dict) --A resource related to a finding.\n\nType (string) -- [REQUIRED]The type of the resource that details are provided for. If possible, set Type to one of the supported resource types. For example, if the resource is an EC2 instance, then set Type to AwsEc2Instance .\nIf the resource does not match any of the provided types, then set Type to Other .\n\nId (string) -- [REQUIRED]The canonical identifier for the given resource type.\n\nPartition (string) --The canonical AWS partition name that the Region is assigned to.\n\nRegion (string) --The canonical AWS external Region name where this resource is located.\n\nTags (dict) --A list of AWS tags associated with a resource at the time the finding was processed.\n\n(string) --\n(string) --\n\n\n\n\nDetails (dict) --Additional details about the resource related to a finding.\n\nAwsCodeBuildProject (dict) --Details for an AWS CodeBuild project.\n\nEncryptionKey (string) --The AWS Key Management Service (AWS KMS) customer master key (CMK) used to encrypt the build output artifacts.\nYou can specify either the Amazon Resource Name (ARN) of the CMK or, if available, the CMK alias (using the format alias/alias-name).\n\nEnvironment (dict) --Information about the build environment for this build project.\n\nCertificate (string) --The certificate to use with this build project.\n\nImagePullCredentialsType (string) --The type of credentials AWS CodeBuild uses to pull images in your build.\nValid values:\n\nCODEBUILD specifies that AWS CodeBuild uses its own credentials. This requires that you modify your ECR repository policy to trust the AWS CodeBuild service principal.\nSERVICE_ROLE specifies that AWS CodeBuild uses your build project\'s service role.\n\nWhen you use a cross-account or private registry image, you must use SERVICE_ROLE credentials. When you use an AWS CodeBuild curated image, you must use CODEBUILD credentials.\n\nRegistryCredential (dict) --The credentials for access to a private registry.\n\nCredential (string) --The Amazon Resource Name (ARN) or name of credentials created using AWS Secrets Manager.\n\nNote\nThe credential can use the name of the credentials only if they exist in your current AWS Region.\n\n\nCredentialProvider (string) --The service that created the credentials to access a private Docker registry.\nThe valid value,``SECRETS_MANAGER`` , is for AWS Secrets Manager.\n\n\n\nType (string) --The type of build environment to use for related builds.\nThe environment type ARM_CONTAINER is available only in Regions US East (N. Virginia), US East (Ohio), US West (Oregon), Europe (Ireland), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Sydney), and Europe (Frankfurt).\nThe environment type LINUX_CONTAINER with compute type build.general1.2xlarge is available only in Regions US East (N. Virginia), US East (N. Virginia), US West (Oregon), Canada (Central), Europe (Ireland), Europe (London), Europe (Frankfurt), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), China (Beijing), and China (Ningxia).\nThe environment type LINUX_GPU_CONTAINER is available only in Regions US East (N. Virginia), US East (N. Virginia), US West (Oregon), Canada (Central), Europe (Ireland), Europe (London), Europe (Frankfurt), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), China (Beijing), and China (Ningxia).\nValid values: WINDOWS_CONTAINER | LINUX_CONTAINER | LINUX_GPU_CONTAINER | ARM_CONTAINER\n\n\n\nName (string) --The name of the build project.\n\nSource (dict) --Information about the build input source code for this build project.\n\nType (string) --The type of repository that contains the source code to be built. Valid values are:\n\nBITBUCKET - The source code is in a Bitbucket repository.\nCODECOMMIT - The source code is in an AWS CodeCommit repository.\nCODEPIPELINE - The source code settings are specified in the source action of a pipeline in AWS CodePipeline.\nGITHUB - The source code is in a GitHub repository.\nGITHUB_ENTERPRISE - The source code is in a GitHub Enterprise repository.\nNO_SOURCE - The project does not have input source code.\nS3 - The source code is in an S3 input bucket.\n\n\nLocation (string) --Information about the location of the source code to be built.\nValid values include:\n\nFor source code settings that are specified in the source action of a pipeline in AWS CodePipeline, location should not be specified. If it is specified, AWS CodePipeline ignores it. This is because AWS CodePipeline uses the settings in a pipeline\'s source action instead of this value.\nFor source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository that contains the source code and the build spec file (for example, https://git-codecommit.region-ID.amazonaws.com/v1/repos/repo-name ).\nFor source code in an S3 input bucket, one of the following.\nThe path to the ZIP file that contains the source code (for example, bucket-name/path/to/object-name.zip ).\nThe path to the folder that contains the source code (for example, bucket-name/path/to/source-code/folder/ ).\n\n\nFor source code in a GitHub repository, the HTTPS clone URL to the repository that contains the source and the build spec file.\nFor source code in a Bitbucket repository, the HTTPS clone URL to the repository that contains the source and the build spec file.\n\n\nGitCloneDepth (integer) --Information about the Git clone depth for the build project.\n\nInsecureSsl (boolean) --Whether to ignore SSL warnings while connecting to the project source code.\n\n\n\nServiceRole (string) --The ARN of the IAM role that enables AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account.\n\nVpcConfig (dict) --Information about the VPC configuration that AWS CodeBuild accesses.\n\nVpcId (string) --The ID of the VPC.\n\nSubnets (list) --A list of one or more subnet IDs in your Amazon VPC.\n\n(string) --\n\n\nSecurityGroupIds (list) --A list of one or more security group IDs in your Amazon VPC.\n\n(string) --\n\n\n\n\n\n\nAwsCloudFrontDistribution (dict) --Details about a CloudFront distribution.\n\nDomainName (string) --The domain name corresponding to the distribution.\n\nETag (string) --The entity tag is a hash of the object.\n\nLastModifiedTime (string) --The date and time that the distribution was last modified.\n\nLogging (dict) --A complex type that controls whether access logs are written for the distribution.\n\nBucket (string) --The Amazon S3 bucket to store the access logs in.\n\nEnabled (boolean) --With this field, you can enable or disable the selected distribution.\n\nIncludeCookies (boolean) --Specifies whether you want CloudFront to include cookies in access logs.\n\nPrefix (string) --An optional string that you want CloudFront to use as a prefix to the access log filenames for this distribution.\n\n\n\nOrigins (dict) --A complex type that contains information about origins for this distribution.\n\nItems (list) --A complex type that contains origins or origin groups for this distribution.\n\n(dict) --A complex type that describes the Amazon S3 bucket, HTTP server (for example, a web server), Amazon Elemental MediaStore, or other server from which CloudFront gets your files.\n\nDomainName (string) --Amazon S3 origins: The DNS name of the Amazon S3 bucket from which you want CloudFront to get objects for this origin.\n\nId (string) --A unique identifier for the origin or origin group.\n\nOriginPath (string) --An optional element that causes CloudFront to request your content from a directory in your Amazon S3 bucket or your custom origin.\n\n\n\n\n\n\n\nStatus (string) --Indicates the current status of the distribution.\n\nWebAclId (string) --A unique identifier that specifies the AWS WAF web ACL, if any, to associate with this distribution.\n\n\n\nAwsEc2Instance (dict) --Details about an Amazon EC2 instance related to a finding.\n\nType (string) --The instance type of the instance.\n\nImageId (string) --The Amazon Machine Image (AMI) ID of the instance.\n\nIpV4Addresses (list) --The IPv4 addresses associated with the instance.\n\n(string) --\n\n\nIpV6Addresses (list) --The IPv6 addresses associated with the instance.\n\n(string) --\n\n\nKeyName (string) --The key name associated with the instance.\n\nIamInstanceProfileArn (string) --The IAM profile ARN of the instance.\n\nVpcId (string) --The identifier of the VPC that the instance was launched in.\n\nSubnetId (string) --The identifier of the subnet that the instance was launched in.\n\nLaunchedAt (string) --The date/time the instance was launched.\n\n\n\nAwsEc2NetworkInterface (dict) --Details for an Amazon EC2 network interface.\n\nAttachment (dict) --The network interface attachment.\n\nAttachTime (string) --The timestamp indicating when the attachment initiated.\n\nAttachmentId (string) --The identifier of the network interface attachment\n\nDeleteOnTermination (boolean) --Indicates whether the network interface is deleted when the instance is terminated.\n\nDeviceIndex (integer) --The device index of the network interface attachment on the instance.\n\nInstanceId (string) --The ID of the instance.\n\nInstanceOwnerId (string) --The AWS account ID of the owner of the instance.\n\nStatus (string) --The attachment state.\nValid values: attaching | attached | detaching | detached\n\n\n\nNetworkInterfaceId (string) --The ID of the network interface.\n\nSecurityGroups (list) --Security groups for the network interface.\n\n(dict) --A security group associated with the network interface.\n\nGroupName (string) --The name of the security group.\n\nGroupId (string) --The ID of the security group.\n\n\n\n\n\nSourceDestCheck (boolean) --Indicates whether traffic to or from the instance is validated.\n\n\n\nAwsEc2SecurityGroup (dict) --Details for an EC2 security group.\n\nGroupName (string) --The name of the security group.\n\nGroupId (string) --The ID of the security group.\n\nOwnerId (string) --The AWS account ID of the owner of the security group.\n\nVpcId (string) --[VPC only] The ID of the VPC for the security group.\n\nIpPermissions (list) --The inbound rules associated with the security group.\n\n(dict) --An IP permission for an EC2 security group.\n\nIpProtocol (string) --The IP protocol name (tcp , udp , icmp , icmpv6 ) or number.\n[VPC only] Use -1 to specify all protocols.\nWhen authorizing security group rules, specifying -1 or a protocol number other than tcp , udp , icmp , or icmpv6 allows traffic on all ports, regardless of any port range you specify.\nFor tcp , udp , and icmp , you must specify a port range.\nFor icmpv6 , the port range is optional. If you omit the port range, traffic for all types and codes is allowed.\n\nFromPort (integer) --The start of the port range for the TCP and UDP protocols, or an ICMP/ICMPv6 type number.\nA value of -1 indicates all ICMP/ICMPv6 types. If you specify all ICMP/ICMPv6 types, you must specify all codes.\n\nToPort (integer) --The end of the port range for the TCP and UDP protocols, or an ICMP/ICMPv6 code.\nA value of -1 indicates all ICMP/ICMPv6 codes. If you specify all ICMP/ICMPv6 types, you must specify all codes.\n\nUserIdGroupPairs (list) --The security group and AWS account ID pairs.\n\n(dict) --A relationship between a security group and a user.\n\nGroupId (string) --The ID of the security group.\n\nGroupName (string) --The name of the security group.\n\nPeeringStatus (string) --The status of a VPC peering connection, if applicable.\n\nUserId (string) --The ID of an AWS account.\nFor a referenced security group in another VPC, the account ID of the referenced security group is returned in the response. If the referenced security group is deleted, this value is not returned.\n[EC2-Classic] Required when adding or removing rules that reference a security group in another AWS.\n\nVpcId (string) --The ID of the VPC for the referenced security group, if applicable.\n\nVpcPeeringConnectionId (string) --The ID of the VPC peering connection, if applicable.\n\n\n\n\n\nIpRanges (list) --The IPv4 ranges.\n\n(dict) --A range of IPv4 addresses.\n\nCidrIp (string) --The IPv4 CIDR range. You can specify either a CIDR range or a source security group, but not both. To specify a single IPv4 address, use the /32 prefix length.\n\n\n\n\n\nIpv6Ranges (list) --The IPv6 ranges.\n\n(dict) --A range of IPv6 addresses.\n\nCidrIpv6 (string) --The IPv6 CIDR range. You can specify either a CIDR range or a source security group, but not both. To specify a single IPv6 address, use the /128 prefix length.\n\n\n\n\n\nPrefixListIds (list) --[VPC only] The prefix list IDs for an AWS service. With outbound rules, this is the AWS service to access through a VPC endpoint from instances associated with the security group.\n\n(dict) --A prefix list ID.\n\nPrefixListId (string) --The ID of the prefix.\n\n\n\n\n\n\n\n\n\nIpPermissionsEgress (list) --[VPC only] The outbound rules associated with the security group.\n\n(dict) --An IP permission for an EC2 security group.\n\nIpProtocol (string) --The IP protocol name (tcp , udp , icmp , icmpv6 ) or number.\n[VPC only] Use -1 to specify all protocols.\nWhen authorizing security group rules, specifying -1 or a protocol number other than tcp , udp , icmp , or icmpv6 allows traffic on all ports, regardless of any port range you specify.\nFor tcp , udp , and icmp , you must specify a port range.\nFor icmpv6 , the port range is optional. If you omit the port range, traffic for all types and codes is allowed.\n\nFromPort (integer) --The start of the port range for the TCP and UDP protocols, or an ICMP/ICMPv6 type number.\nA value of -1 indicates all ICMP/ICMPv6 types. If you specify all ICMP/ICMPv6 types, you must specify all codes.\n\nToPort (integer) --The end of the port range for the TCP and UDP protocols, or an ICMP/ICMPv6 code.\nA value of -1 indicates all ICMP/ICMPv6 codes. If you specify all ICMP/ICMPv6 types, you must specify all codes.\n\nUserIdGroupPairs (list) --The security group and AWS account ID pairs.\n\n(dict) --A relationship between a security group and a user.\n\nGroupId (string) --The ID of the security group.\n\nGroupName (string) --The name of the security group.\n\nPeeringStatus (string) --The status of a VPC peering connection, if applicable.\n\nUserId (string) --The ID of an AWS account.\nFor a referenced security group in another VPC, the account ID of the referenced security group is returned in the response. If the referenced security group is deleted, this value is not returned.\n[EC2-Classic] Required when adding or removing rules that reference a security group in another AWS.\n\nVpcId (string) --The ID of the VPC for the referenced security group, if applicable.\n\nVpcPeeringConnectionId (string) --The ID of the VPC peering connection, if applicable.\n\n\n\n\n\nIpRanges (list) --The IPv4 ranges.\n\n(dict) --A range of IPv4 addresses.\n\nCidrIp (string) --The IPv4 CIDR range. You can specify either a CIDR range or a source security group, but not both. To specify a single IPv4 address, use the /32 prefix length.\n\n\n\n\n\nIpv6Ranges (list) --The IPv6 ranges.\n\n(dict) --A range of IPv6 addresses.\n\nCidrIpv6 (string) --The IPv6 CIDR range. You can specify either a CIDR range or a source security group, but not both. To specify a single IPv6 address, use the /128 prefix length.\n\n\n\n\n\nPrefixListIds (list) --[VPC only] The prefix list IDs for an AWS service. With outbound rules, this is the AWS service to access through a VPC endpoint from instances associated with the security group.\n\n(dict) --A prefix list ID.\n\nPrefixListId (string) --The ID of the prefix.\n\n\n\n\n\n\n\n\n\n\n\nAwsElbv2LoadBalancer (dict) --Details about a load balancer.\n\nAvailabilityZones (list) --The Availability Zones for the load balancer.\n\n(dict) --Information about an Availability Zone.\n\nZoneName (string) --The name of the Availability Zone.\n\nSubnetId (string) --The ID of the subnet. You can specify one subnet per Availability Zone.\n\n\n\n\n\nCanonicalHostedZoneId (string) --The ID of the Amazon Route 53 hosted zone associated with the load balancer.\n\nCreatedTime (string) --The date and time the load balancer was created.\n\nDNSName (string) --The public DNS name of the load balancer.\n\nIpAddressType (string) --The type of IP addresses used by the subnets for your load balancer. The possible values are ipv4 (for IPv4 addresses) and dualstack (for IPv4 and IPv6 addresses).\n\nScheme (string) --The nodes of an Internet-facing load balancer have public IP addresses.\n\nSecurityGroups (list) --The IDs of the security groups for the load balancer.\n\n(string) --\n\n\nState (dict) --The state of the load balancer.\n\nCode (string) --The state code. The initial state of the load balancer is provisioning.\nAfter the load balancer is fully set up and ready to route traffic, its state is active.\nIf the load balancer could not be set up, its state is failed.\n\nReason (string) --A description of the state.\n\n\n\nType (string) --The type of load balancer.\n\nVpcId (string) --The ID of the VPC for the load balancer.\n\n\n\nAwsElasticsearchDomain (dict) --Details for an Elasticsearch domain.\n\nAccessPolicies (string) --IAM policy document specifying the access policies for the new Amazon ES domain.\n\nDomainEndpointOptions (dict) --Additional options for the domain endpoint.\n\nEnforceHTTPS (boolean) --Whether to require that all traffic to the domain arrive over HTTPS.\n\nTLSSecurityPolicy (string) --The TLS security policy to apply to the HTTPS endpoint of the Elasticsearch domain.\nValid values:\n\nPolicy-Min-TLS-1-0-2019-07 , which supports TLSv1.0 and higher\nPolicy-Min-TLS-1-2-2019-07 , which only supports TLSv1.2\n\n\n\n\nDomainId (string) --Unique identifier for an Amazon ES domain.\n\nDomainName (string) --Name of an Amazon ES domain.\nDomain names are unique across all domains owned by the same account within an AWS Region.\nDomain names must start with a lowercase letter and must be between 3 and 28 characters.\nValid characters are a-z (lowercase only), 0-9, and \xe2\x80\x93 (hyphen).\n\nEndpoint (string) --Domain-specific endpoint used to submit index, search, and data upload requests to an Amazon ES domain.\nThe endpoint is a service URL.\n\nEndpoints (dict) --The key-value pair that exists if the Amazon ES domain uses VPC endpoints.\n\n(string) --\n(string) --\n\n\n\n\nElasticsearchVersion (string) --Elasticsearch version.\n\nEncryptionAtRestOptions (dict) --Details about the configuration for encryption at rest.\n\nEnabled (boolean) --Whether encryption at rest is enabled.\n\nKmsKeyId (string) --The KMS key ID. Takes the form 1a2a3a4-1a2a-3a4a-5a6a-1a2a3a4a5a6a.\n\n\n\nNodeToNodeEncryptionOptions (dict) --Details about the configuration for node-to-node encryption.\n\nEnabled (boolean) --Whether node-to-node encryption is enabled.\n\n\n\nVPCOptions (dict) --Information that Amazon ES derives based on VPCOptions for the domain.\n\nAvailabilityZones (list) --The list of Availability Zones associated with the VPC subnets.\n\n(string) --\n\n\nSecurityGroupIds (list) --The list of security group IDs associated with the VPC endpoints for the domain.\n\n(string) --\n\n\nSubnetIds (list) --A list of subnet IDs associated with the VPC endpoints for the domain.\n\n(string) --\n\n\nVPCId (string) --ID for the VPC.\n\n\n\n\n\nAwsS3Bucket (dict) --Details about an Amazon S3 bucket related to a finding.\n\nOwnerId (string) --The canonical user ID of the owner of the S3 bucket.\n\nOwnerName (string) --The display name of the owner of the S3 bucket.\n\nCreatedAt (string) --The date and time when the S3 bucket was created.\n\nServerSideEncryptionConfiguration (dict) --The encryption rules that are applied to the S3 bucket.\n\nRules (list) --The encryption rules that are applied to the S3 bucket.\n\n(dict) --An encryption rule to apply to the S3 bucket.\n\nApplyServerSideEncryptionByDefault (dict) --Specifies the default server-side encryption to apply to new objects in the bucket. If a PUT object request doesn\'t specify any server-side encryption, this default encryption is applied.\n\nSSEAlgorithm (string) --Server-side encryption algorithm to use for the default encryption.\n\nKMSMasterKeyID (string) --AWS KMS customer master key (CMK) ID to use for the default encryption.\n\n\n\n\n\n\n\n\n\n\n\nAwsS3Object (dict) --Details about an Amazon S3 object related to a finding.\n\nLastModified (string) --The date and time when the object was last modified.\n\nETag (string) --The opaque identifier assigned by a web server to a specific version of a resource found at a URL.\n\nVersionId (string) --The version of the object.\n\nContentType (string) --A standard MIME type describing the format of the object data.\n\nServerSideEncryption (string) --If the object is stored using server-side encryption, the value of the server-side encryption algorithm used when storing this object in Amazon S3.\n\nSSEKMSKeyId (string) --The identifier of the AWS Key Management Service (AWS KMS) symmetric customer managed customer master key (CMK) that was used for the object.\n\n\n\nAwsIamAccessKey (dict) --Details about an IAM access key related to a finding.\n\nUserName (string) --The user associated with the IAM access key related to a finding.\nThe UserName parameter has been replaced with the PrincipalName parameter because access keys can also be assigned to principals that are not IAM users.\n\nStatus (string) --The status of the IAM access key related to a finding.\n\nCreatedAt (string) --The creation date/time of the IAM access key related to a finding.\n\nPrincipalId (string) --The ID of the principal associated with an access key.\n\nPrincipalType (string) --The type of principal associated with an access key.\n\nPrincipalName (string) --The name of the principal.\n\n\n\nAwsIamRole (dict) --Details about an IAM role.\n\nAssumeRolePolicyDocument (string) --The trust policy that grants permission to assume the role.\n\nCreateDate (string) --The date and time, in ISO 8601 date-time format, when the role was created.\n\nRoleId (string) --The stable and unique string identifying the role.\n\nRoleName (string) --The friendly name that identifies the role.\n\nMaxSessionDuration (integer) --The maximum session duration (in seconds) that you want to set for the specified role.\n\nPath (string) --The path to the role.\n\n\n\nAwsKmsKey (dict) --Details about a KMS key.\n\nAWSAccountId (string) --The twelve-digit account ID of the AWS account that owns the CMK.\n\nCreationDate (float) --The date and time when the CMK was created.\n\nKeyId (string) --The globally unique identifier for the CMK.\n\nKeyManager (string) --The manager of the CMK. CMKs in your AWS account are either customer managed or AWS managed.\n\nKeyState (string) --The state of the CMK.\n\nOrigin (string) --The source of the CMK\'s key material.\nWhen this value is AWS_KMS , AWS KMS created the key material.\nWhen this value is EXTERNAL , the key material was imported from your existing key management infrastructure or the CMK lacks key material.\nWhen this value is AWS_CLOUDHSM , the key material was created in the AWS CloudHSM cluster associated with a custom key store.\n\n\n\nAwsLambdaFunction (dict) --Details about a Lambda function.\n\nCode (dict) --An AwsLambdaFunctionCode object.\n\nS3Bucket (string) --An Amazon S3 bucket in the same AWS Region as your function. The bucket can be in a different AWS account.\n\nS3Key (string) --The Amazon S3 key of the deployment package.\n\nS3ObjectVersion (string) --For versioned objects, the version of the deployment package object to use.\n\nZipFile (string) --The base64-encoded contents of the deployment package. AWS SDK and AWS CLI clients handle the encoding for you.\n\n\n\nCodeSha256 (string) --The SHA256 hash of the function\'s deployment package.\n\nDeadLetterConfig (dict) --The function\'s dead letter queue.\n\nTargetArn (string) --The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.\n\n\n\nEnvironment (dict) --The function\'s environment variables.\n\nVariables (dict) --Environment variable key-value pairs.\n\n(string) --\n(string) --\n\n\n\n\nError (dict) --An AwsLambdaFunctionEnvironmentError object.\n\nErrorCode (string) --The error code.\n\nMessage (string) --The error message.\n\n\n\n\n\nFunctionName (string) --The name of the function.\n\nHandler (string) --The function that Lambda calls to begin executing your function.\n\nKmsKeyArn (string) --The KMS key that\'s used to encrypt the function\'s environment variables. This key is only returned if you\'ve configured a customer managed CMK.\n\nLastModified (string) --The date and time that the function was last updated, in ISO-8601 format (YYYY-MM-DDThh:mm:ss.sTZD).\n\nLayers (list) --The function\'s layers.\n\n(dict) --An AWS Lambda layer.\n\nArn (string) --The Amazon Resource Name (ARN) of the function layer.\n\nCodeSize (integer) --The size of the layer archive in bytes.\n\n\n\n\n\nMasterArn (string) --For Lambda@Edge functions, the ARN of the master function.\n\nMemorySize (integer) --The memory that\'s allocated to the function.\n\nRevisionId (string) --The latest updated revision of the function or alias.\n\nRole (string) --The function\'s execution role.\n\nRuntime (string) --The runtime environment for the Lambda function.\n\nTimeout (integer) --The amount of time that Lambda allows a function to run before stopping it.\n\nTracingConfig (dict) --The function\'s AWS X-Ray tracing configuration.\n\nMode (string) --The tracing mode.\n\n\n\nVpcConfig (dict) --The function\'s networking configuration.\n\nSecurityGroupIds (list) --A list of VPC security groups IDs.\n\n(string) --\n\n\nSubnetIds (list) --A list of VPC subnet IDs.\n\n(string) --\n\n\nVpcId (string) --The ID of the VPC.\n\n\n\nVersion (string) --The version of the Lambda function.\n\n\n\nAwsLambdaLayerVersion (dict) --Details for a Lambda layer version.\n\nVersion (integer) --The version number.\n\nCompatibleRuntimes (list) --The layer\'s compatible runtimes. Maximum number of five items.\nValid values: nodejs10.x | nodejs12.x | java8 | java11 | python2.7 | python3.6 | python3.7 | python3.8 | dotnetcore1.0 | dotnetcore2.1 | go1.x | ruby2.5 | provided\n\n(string) --\n\n\nCreatedDate (string) --The date that the version was created, in ISO 8601 format. For example, 2018-11-27T15:10:45.123+0000.\n\n\n\nAwsRdsDbInstance (dict) --Details for an Amazon RDS database instance.\n\nAssociatedRoles (list) --The AWS Identity and Access Management (IAM) roles associated with the DB instance.\n\n(dict) --An AWS Identity and Access Management (IAM) role associated with the DB instance.\n\nRoleArn (string) --The Amazon Resource Name (ARN) of the IAM role that is associated with the DB instance.\n\nFeatureName (string) --The name of the feature associated with the IAM)role.\n\nStatus (string) --Describes the state of the association between the IAM role and the DB instance. The Status property returns one of the following values:\n\nACTIVE - The IAM role ARN is associated with the DB instance and can be used to access other AWS services on your behalf.\nPENDING - The IAM role ARN is being associated with the DB instance.\nINVALID - The IAM role ARN is associated with the DB instance. But the DB instance is unable to assume the IAM role in order to access other AWS services on your behalf.\n\n\n\n\n\n\nCACertificateIdentifier (string) --The identifier of the CA certificate for this DB instance.\n\nDBClusterIdentifier (string) --If the DB instance is a member of a DB cluster, contains the name of the DB cluster that the DB instance is a member of.\n\nDBInstanceIdentifier (string) --Contains a user-supplied database identifier. This identifier is the unique key that identifies a DB instance.\n\nDBInstanceClass (string) --Contains the name of the compute and memory capacity class of the DB instance.\n\nDbInstancePort (integer) --Specifies the port that the DB instance listens on. If the DB instance is part of a DB cluster, this can be a different port than the DB cluster port.\n\nDbiResourceId (string) --The AWS Region-unique, immutable identifier for the DB instance. This identifier is found in AWS CloudTrail log entries whenever the AWS KMS key for the DB instance is accessed.\n\nDBName (string) --The meaning of this parameter differs according to the database engine you use.\n\nMySQL, MariaDB, SQL Server, PostgreSQL\nContains the name of the initial database of this instance that was provided at create time, if one was specified when the DB instance was created. This same name is returned for the life of the DB instance.\n\nOracle\nContains the Oracle System ID (SID) of the created DB instance. Not shown when the returned parameters do not apply to an Oracle DB instance.\n\nDeletionProtection (boolean) --Indicates whether the DB instance has deletion protection enabled.\nWhen deletion protection is enabled, the database cannot be deleted.\n\nEndpoint (dict) --Specifies the connection endpoint.\n\nAddress (string) --Specifies the DNS address of the DB instance.\n\nPort (integer) --Specifies the port that the database engine is listening on.\n\nHostedZoneId (string) --Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.\n\n\n\nEngine (string) --Provides the name of the database engine to use for this DB instance.\n\nEngineVersion (string) --Indicates the database engine version.\n\nIAMDatabaseAuthenticationEnabled (boolean) --True if mapping of AWS Identity and Access Management (IAM) accounts to database accounts is enabled, and otherwise false.\nIAM database authentication can be enabled for the following database engines.\n\nFor MySQL 5.6, minor version 5.6.34 or higher\nFor MySQL 5.7, minor version 5.7.16 or higher\nAurora 5.6 or higher\n\n\nInstanceCreateTime (string) --Provides the date and time the DB instance was created.\n\nKmsKeyId (string) --If StorageEncrypted is true, the AWS KMS key identifier for the encrypted DB instance.\n\nPubliclyAccessible (boolean) --Specifies the accessibility options for the DB instance.\nA value of true specifies an Internet-facing instance with a publicly resolvable DNS name, which resolves to a public IP address.\nA value of false specifies an internal instance with a DNS name that resolves to a private IP address.\n\nStorageEncrypted (boolean) --Specifies whether the DB instance is encrypted.\n\nTdeCredentialArn (string) --The ARN from the key store with which the instance is associated for TDE encryption.\n\nVpcSecurityGroups (list) --A list of VPC security groups that the DB instance belongs to.\n\n(dict) --A VPC security groups that the DB instance belongs to.\n\nVpcSecurityGroupId (string) --The name of the VPC security group.\n\nStatus (string) --The status of the VPC security group.\n\n\n\n\n\n\n\nAwsSnsTopic (dict) --Details about an SNS topic.\n\nKmsMasterKeyId (string) --The ID of an AWS managed customer master key (CMK) for Amazon SNS or a custom CMK.\n\nSubscription (list) --Subscription is an embedded property that describes the subscription endpoints of an Amazon SNS topic.\n\n(dict) --A wrapper type for the attributes of an Amazon SNS subscription.\n\nEndpoint (string) --The subscription\'s endpoint (format depends on the protocol).\n\nProtocol (string) --The subscription\'s protocol.\n\n\n\n\n\nTopicName (string) --The name of the topic.\n\nOwner (string) --The subscription\'s owner.\n\n\n\nAwsSqsQueue (dict) --Details about an SQS queue.\n\nKmsDataKeyReusePeriodSeconds (integer) --The length of time, in seconds, for which Amazon SQS can reuse a data key to encrypt or decrypt messages before calling AWS KMS again.\n\nKmsMasterKeyId (string) --The ID of an AWS managed customer master key (CMK) for Amazon SQS or a custom CMK.\n\nQueueName (string) --The name of the new queue.\n\nDeadLetterTargetArn (string) --The Amazon Resource Name (ARN) of the dead-letter queue to which Amazon SQS moves messages after the value of maxReceiveCount is exceeded.\n\n\n\nAwsWafWebAcl (dict) --Details for a WAF WebACL.\n\nName (string) --A friendly name or description of the WebACL. You can\'t change the name of a WebACL after you create it.\n\nDefaultAction (string) --The action to perform if none of the rules contained in the WebACL match.\n\nRules (list) --An array that contains the action for each rule in a WebACL, the priority of the rule, and the ID of the rule.\n\n(dict) --Details for a rule in a WAF WebACL.\n\nAction (dict) --Specifies the action that CloudFront or AWS WAF takes when a web request matches the conditions in the rule.\n\nType (string) --Specifies how you want AWS WAF to respond to requests that match the settings in a rule.\nValid settings include the following:\n\nALLOW - AWS WAF allows requests\nBLOCK - AWS WAF blocks requests\nCOUNT - AWS WAF increments a counter of the requests that match all of the conditions in the rule. AWS WAF then continues to inspect the web request based on the remaining rules in the web ACL. You can\'t specify COUNT for the default action for a WebACL.\n\n\n\n\nExcludedRules (list) --Rules to exclude from a rule group.\n\n(dict) --Details about a rule to exclude from a rule group.\n\nRuleId (string) --The unique identifier for the rule to exclude from the rule group.\n\n\n\n\n\nOverrideAction (dict) --Use the OverrideAction to test your RuleGroup.\nAny rule in a RuleGroup can potentially block a request. If you set the OverrideAction to None , the RuleGroup blocks a request if any individual rule in the RuleGroup matches the request and is configured to block that request.\nHowever, if you first want to test the RuleGroup, set the OverrideAction to Count . The RuleGroup then overrides any block action specified by individual rules contained within the group. Instead of blocking matching requests, those requests are counted.\n\nActivatedRule |OverrideAction applies only when updating or adding a RuleGroup to a WebACL. In this case you do not use ActivatedRule |Action . For all other update requests, ActivatedRule |Action is used instead of ActivatedRule |OverrideAction .\n\nType (string) --\nCOUNT overrides the action specified by the individual rule within a RuleGroup .\nIf set to NONE , the rule\'s action takes place.\n\n\n\nPriority (integer) --Specifies the order in which the rules in a WebACL are evaluated. Rules with a lower value for Priority are evaluated before rules with a higher value. The value must be a unique integer. If you add multiple rules to a WebACL, the values do not need to be consecutive.\n\nRuleId (string) --The identifier for a rule.\n\nType (string) --The rule type.\nValid values: REGULAR | RATE_BASED | GROUP\nThe default is REGULAR .\n\n\n\n\n\nWebAclId (string) --A unique identifier for a WebACL.\n\n\n\nContainer (dict) --Details about a container resource related to a finding.\n\nName (string) --The name of the container related to a finding.\n\nImageId (string) --The identifier of the image related to a finding.\n\nImageName (string) --The name of the image related to a finding.\n\nLaunchedAt (string) --The date and time when the container started.\n\n\n\nOther (dict) --Details about a resource that are not available in a type-specific details object. Use the Other object in the following cases.\n\nThe type-specific object does not contain all of the fields that you want to populate. In this case, first use the type-specific object to populate those fields. Use the Other object to populate the fields that are missing from the type-specific object.\nThe resource type does not have a corresponding object. This includes resources for which the type is Other .\n\n\n(string) --\n(string) --\n\n\n\n\n\n\n\n\n\n\nCompliance (dict) --This data type is exclusive to findings that are generated as the result of a check run against a specific rule in a supported security standard, such as CIS AWS Foundations. Contains security standard-related finding details.\n\nStatus (string) --The result of a standards check.\nThe valid values for Status are as follows.\n\n\nPASSED - Standards check passed for all evaluated resources.\nWARNING - Some information is missing or this check is not supported for your configuration.\nFAILED - Standards check failed for at least one evaluated resource.\nNOT_AVAILABLE - Check could not be performed due to a service outage, API error, or because the result of the AWS Config evaluation was NOT_APPLICABLE . If the AWS Config evaluation result was NOT_APPLICABLE , then after 3 days, Security Hub automatically archives the finding.\n\n\n\n\nRelatedRequirements (list) --For a control, the industry or regulatory framework requirements that are related to the control. The check for that control is aligned with these requirements.\n\n(string) --\n\n\nStatusReasons (list) --For findings generated from controls, a list of reasons behind the value of Status . For the list of status reason codes and their meanings, see Standards-related information in the ASFF in the AWS Security Hub User Guide .\n\n(dict) --Provides additional context for the value of Compliance.Status .\n\nReasonCode (string) -- [REQUIRED]A code that represents a reason for the control status. For the list of status reason codes and their meanings, see Standards-related information in the ASFF in the AWS Security Hub User Guide .\n\nDescription (string) --The corresponding description for the status reason code.\n\n\n\n\n\n\n\nVerificationState (string) --Indicates the veracity of a finding.\n\nWorkflowState (string) --The workflow state of a finding.\n\nWorkflow (dict) --Provides information about the status of the investigation into a finding.\n\nStatus (string) --The status of the investigation into the finding. The allowed values are the following.\n\nNEW - The initial state of a finding, before it is reviewed.\nNOTIFIED - Indicates that you notified the resource owner about the security issue. Used when the initial reviewer is not the resource owner, and needs intervention from the resource owner.\nSUPPRESSED - The finding will not be reviewed again and will not be acted upon.\nRESOLVED - The finding was reviewed and remediated and is now considered resolved.\n\n\n\n\nRecordState (string) --The record state of a finding.\n\nRelatedFindings (list) --A list of related findings.\n\n(dict) --Details about a related finding.\n\nProductArn (string) -- [REQUIRED]The ARN of the product that generated a related finding.\n\nId (string) -- [REQUIRED]The product-generated identifier for a related finding.\n\n\n\n\n\nNote (dict) --A user-defined note added to a finding.\n\nText (string) -- [REQUIRED]The text of a note.\n\nUpdatedBy (string) -- [REQUIRED]The principal that created a note.\n\nUpdatedAt (string) -- [REQUIRED]The timestamp of when the note was updated.\n\n\n\n\n\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'FailedCount': 123,
    'SuccessCount': 123,
    'FailedFindings': [
        {
            'Id': 'string',
            'ErrorCode': 'string',
            'ErrorMessage': 'string'
        },
    ]
}


Response Structure

(dict) --
FailedCount (integer) --The number of findings that failed to import.

SuccessCount (integer) --The number of findings that were successfully imported.

FailedFindings (list) --The list of findings that failed to import.

(dict) --The list of the findings that cannot be imported. For each finding, the list provides the error.

Id (string) --The identifier of the finding that could not be updated.

ErrorCode (string) --The code of the error returned by the BatchImportFindings operation.

ErrorMessage (string) --The message of the error returned by the BatchImportFindings operation.










Exceptions

SecurityHub.Client.exceptions.InternalException
SecurityHub.Client.exceptions.InvalidInputException
SecurityHub.Client.exceptions.LimitExceededException
SecurityHub.Client.exceptions.InvalidAccessException


    :return: {
        'FailedCount': 123,
        'SuccessCount': 123,
        'FailedFindings': [
            {
                'Id': 'string',
                'ErrorCode': 'string',
                'ErrorMessage': 'string'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def batch_update_findings(FindingIdentifiers=None, Note=None, Severity=None, VerificationState=None, Confidence=None, Criticality=None, Types=None, UserDefinedFields=None, Workflow=None, RelatedFindings=None):
    """
    Used by Security Hub customers to update information about their investigation into a finding. Requested by master accounts or member accounts. Master accounts can update findings for their account and their member accounts. Member accounts can update findings for their account.
    Updates from BatchUpdateFindings do not affect the value of UpdatedAt for a finding.
    Master accounts can use BatchUpdateFindings to update the following finding fields and objects.
    Member accounts can only use BatchUpdateFindings to update the Note object.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_update_findings(
        FindingIdentifiers=[
            {
                'Id': 'string',
                'ProductArn': 'string'
            },
        ],
        Note={
            'Text': 'string',
            'UpdatedBy': 'string'
        },
        Severity={
            'Normalized': 123,
            'Product': 123.0,
            'Label': 'INFORMATIONAL'|'LOW'|'MEDIUM'|'HIGH'|'CRITICAL'
        },
        VerificationState='UNKNOWN'|'TRUE_POSITIVE'|'FALSE_POSITIVE'|'BENIGN_POSITIVE',
        Confidence=123,
        Criticality=123,
        Types=[
            'string',
        ],
        UserDefinedFields={
            'string': 'string'
        },
        Workflow={
            'Status': 'NEW'|'NOTIFIED'|'RESOLVED'|'SUPPRESSED'
        },
        RelatedFindings=[
            {
                'ProductArn': 'string',
                'Id': 'string'
            },
        ]
    )
    
    
    :type FindingIdentifiers: list
    :param FindingIdentifiers: [REQUIRED]\nThe list of findings to update. BatchUpdateFindings can be used to update up to 100 findings at a time.\nFor each finding, the list provides the finding identifier and the ARN of the finding provider.\n\n(dict) --Identifies a finding to update using BatchUpdateFindings .\n\nId (string) -- [REQUIRED]The identifier of the finding that was specified by the finding provider.\n\nProductArn (string) -- [REQUIRED]The ARN generated by Security Hub that uniquely identifies a product that generates findings. This can be the ARN for a third-party product that is integrated with Security Hub, or the ARN for a custom integration.\n\n\n\n\n

    :type Note: dict
    :param Note: The updated note.\n\nText (string) -- [REQUIRED]The updated note text.\n\nUpdatedBy (string) -- [REQUIRED]The principal that updated the note.\n\n\n

    :type Severity: dict
    :param Severity: Used to update the finding severity.\n\nNormalized (integer) --The normalized severity for the finding. This attribute is to be deprecated in favor of Label .\nIf you provide Normalized and do not provide Label , Label is set automatically as follows.\n\n0 - INFORMATIONAL\n1\xe2\x80\x9339 - LOW\n40\xe2\x80\x9369 - MEDIUM\n70\xe2\x80\x9389 - HIGH\n90\xe2\x80\x93100 - CRITICAL\n\n\nProduct (float) --The native severity as defined by the AWS service or integrated partner product that generated the finding.\n\nLabel (string) --The severity value of the finding. The allowed values are the following.\n\nINFORMATIONAL - No issue was found.\nLOW - The issue does not require action on its own.\nMEDIUM - The issue must be addressed but not urgently.\nHIGH - The issue must be addressed as a priority.\nCRITICAL - The issue must be remediated immediately to avoid it escalating.\n\n\n\n

    :type VerificationState: string
    :param VerificationState: Indicates the veracity of a finding.\nThe available values for VerificationState are as follows.\n\nUNKNOWN \xe2\x80\x93 The default disposition of a security finding\nTRUE_POSITIVE \xe2\x80\x93 The security finding is confirmed\nFALSE_POSITIVE \xe2\x80\x93 The security finding was determined to be a false alarm\nBENIGN_POSITIVE \xe2\x80\x93 A special case of TRUE_POSITIVE where the finding doesn\'t pose any threat, is expected, or both\n\n

    :type Confidence: integer
    :param Confidence: The updated value for the finding confidence. Confidence is defined as the likelihood that a finding accurately identifies the behavior or issue that it was intended to identify.\nConfidence is scored on a 0-100 basis using a ratio scale, where 0 means zero percent confidence and 100 means 100 percent confidence.\n

    :type Criticality: integer
    :param Criticality: The updated value for the level of importance assigned to the resources associated with the findings.\nA score of 0 means that the underlying resources have no criticality, and a score of 100 is reserved for the most critical resources.\n

    :type Types: list
    :param Types: One or more finding types in the format of namespace/category/classifier that classify a finding.\nValid namespace values are as follows.\n\nSoftware and Configuration Checks\nTTPs\nEffects\nUnusual Behaviors\nSensitive Data Identifications\n\n\n(string) --\n\n

    :type UserDefinedFields: dict
    :param UserDefinedFields: A list of name/value string pairs associated with the finding. These are custom, user-defined fields added to a finding.\n\n(string) --\n(string) --\n\n\n\n

    :type Workflow: dict
    :param Workflow: Used to update the workflow status of a finding.\nThe workflow status indicates the progress of the investigation into the finding.\n\nStatus (string) --The status of the investigation into the finding. The allowed values are the following.\n\nNEW - The initial state of a finding, before it is reviewed.\nNOTIFIED - Indicates that you notified the resource owner about the security issue. Used when the initial reviewer is not the resource owner, and needs intervention from the resource owner.\nRESOLVED - The finding was reviewed and remediated and is now considered resolved.\nSUPPRESSED - The finding will not be reviewed again and will not be acted upon.\n\n\n\n

    :type RelatedFindings: list
    :param RelatedFindings: A list of findings that are related to the updated findings.\n\n(dict) --Details about a related finding.\n\nProductArn (string) -- [REQUIRED]The ARN of the product that generated a related finding.\n\nId (string) -- [REQUIRED]The product-generated identifier for a related finding.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ProcessedFindings': [
        {
            'Id': 'string',
            'ProductArn': 'string'
        },
    ],
    'UnprocessedFindings': [
        {
            'FindingIdentifier': {
                'Id': 'string',
                'ProductArn': 'string'
            },
            'ErrorCode': 'string',
            'ErrorMessage': 'string'
        },
    ]
}


Response Structure

(dict) --

ProcessedFindings (list) --
The list of findings that were updated successfully.

(dict) --
Identifies a finding to update using BatchUpdateFindings .

Id (string) --
The identifier of the finding that was specified by the finding provider.

ProductArn (string) --
The ARN generated by Security Hub that uniquely identifies a product that generates findings. This can be the ARN for a third-party product that is integrated with Security Hub, or the ARN for a custom integration.





UnprocessedFindings (list) --
The list of findings that were not updated.

(dict) --
A finding from a BatchUpdateFindings request that Security Hub was unable to update.

FindingIdentifier (dict) --
The identifier of the finding that was not updated.

Id (string) --
The identifier of the finding that was specified by the finding provider.

ProductArn (string) --
The ARN generated by Security Hub that uniquely identifies a product that generates findings. This can be the ARN for a third-party product that is integrated with Security Hub, or the ARN for a custom integration.



ErrorCode (string) --
The code associated with the error.

ErrorMessage (string) --
The message associated with the error.











Exceptions

SecurityHub.Client.exceptions.InternalException
SecurityHub.Client.exceptions.InvalidInputException
SecurityHub.Client.exceptions.LimitExceededException
SecurityHub.Client.exceptions.InvalidAccessException


    :return: {
        'ProcessedFindings': [
            {
                'Id': 'string',
                'ProductArn': 'string'
            },
        ],
        'UnprocessedFindings': [
            {
                'FindingIdentifier': {
                    'Id': 'string',
                    'ProductArn': 'string'
                },
                'ErrorCode': 'string',
                'ErrorMessage': 'string'
            },
        ]
    }
    
    
    :returns: 
    FindingIdentifiers (list) -- [REQUIRED]
    The list of findings to update. BatchUpdateFindings can be used to update up to 100 findings at a time.
    For each finding, the list provides the finding identifier and the ARN of the finding provider.
    
    (dict) --Identifies a finding to update using BatchUpdateFindings .
    
    Id (string) -- [REQUIRED]The identifier of the finding that was specified by the finding provider.
    
    ProductArn (string) -- [REQUIRED]The ARN generated by Security Hub that uniquely identifies a product that generates findings. This can be the ARN for a third-party product that is integrated with Security Hub, or the ARN for a custom integration.
    
    
    
    
    
    Note (dict) -- The updated note.
    
    Text (string) -- [REQUIRED]The updated note text.
    
    UpdatedBy (string) -- [REQUIRED]The principal that updated the note.
    
    
    
    Severity (dict) -- Used to update the finding severity.
    
    Normalized (integer) --The normalized severity for the finding. This attribute is to be deprecated in favor of Label .
    If you provide Normalized and do not provide Label , Label is set automatically as follows.
    
    0 - INFORMATIONAL
    1\xe2\x80\x9339 - LOW
    40\xe2\x80\x9369 - MEDIUM
    70\xe2\x80\x9389 - HIGH
    90\xe2\x80\x93100 - CRITICAL
    
    
    Product (float) --The native severity as defined by the AWS service or integrated partner product that generated the finding.
    
    Label (string) --The severity value of the finding. The allowed values are the following.
    
    INFORMATIONAL - No issue was found.
    LOW - The issue does not require action on its own.
    MEDIUM - The issue must be addressed but not urgently.
    HIGH - The issue must be addressed as a priority.
    CRITICAL - The issue must be remediated immediately to avoid it escalating.
    
    
    
    
    VerificationState (string) -- Indicates the veracity of a finding.
    The available values for VerificationState are as follows.
    
    UNKNOWN \xe2\x80\x93 The default disposition of a security finding
    TRUE_POSITIVE \xe2\x80\x93 The security finding is confirmed
    FALSE_POSITIVE \xe2\x80\x93 The security finding was determined to be a false alarm
    BENIGN_POSITIVE \xe2\x80\x93 A special case of TRUE_POSITIVE where the finding doesn\'t pose any threat, is expected, or both
    
    
    Confidence (integer) -- The updated value for the finding confidence. Confidence is defined as the likelihood that a finding accurately identifies the behavior or issue that it was intended to identify.
    Confidence is scored on a 0-100 basis using a ratio scale, where 0 means zero percent confidence and 100 means 100 percent confidence.
    
    Criticality (integer) -- The updated value for the level of importance assigned to the resources associated with the findings.
    A score of 0 means that the underlying resources have no criticality, and a score of 100 is reserved for the most critical resources.
    
    Types (list) -- One or more finding types in the format of namespace/category/classifier that classify a finding.
    Valid namespace values are as follows.
    
    Software and Configuration Checks
    TTPs
    Effects
    Unusual Behaviors
    Sensitive Data Identifications
    
    
    (string) --
    
    
    UserDefinedFields (dict) -- A list of name/value string pairs associated with the finding. These are custom, user-defined fields added to a finding.
    
    (string) --
    (string) --
    
    
    
    
    Workflow (dict) -- Used to update the workflow status of a finding.
    The workflow status indicates the progress of the investigation into the finding.
    
    Status (string) --The status of the investigation into the finding. The allowed values are the following.
    
    NEW - The initial state of a finding, before it is reviewed.
    NOTIFIED - Indicates that you notified the resource owner about the security issue. Used when the initial reviewer is not the resource owner, and needs intervention from the resource owner.
    RESOLVED - The finding was reviewed and remediated and is now considered resolved.
    SUPPRESSED - The finding will not be reviewed again and will not be acted upon.
    
    
    
    
    RelatedFindings (list) -- A list of findings that are related to the updated findings.
    
    (dict) --Details about a related finding.
    
    ProductArn (string) -- [REQUIRED]The ARN of the product that generated a related finding.
    
    Id (string) -- [REQUIRED]The product-generated identifier for a related finding.
    
    
    
    
    
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def create_action_target(Name=None, Description=None, Id=None):
    """
    Creates a custom action target in Security Hub.
    You can use custom actions on findings and insights in Security Hub to trigger target actions in Amazon CloudWatch Events.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_action_target(
        Name='string',
        Description='string',
        Id='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the custom action target.\n

    :type Description: string
    :param Description: [REQUIRED]\nThe description for the custom action target.\n

    :type Id: string
    :param Id: [REQUIRED]\nThe ID for the custom action target.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ActionTargetArn': 'string'
}


Response Structure

(dict) --

ActionTargetArn (string) --
The ARN for the custom action target.







Exceptions

SecurityHub.Client.exceptions.InternalException
SecurityHub.Client.exceptions.InvalidInputException
SecurityHub.Client.exceptions.InvalidAccessException
SecurityHub.Client.exceptions.LimitExceededException
SecurityHub.Client.exceptions.ResourceConflictException


    :return: {
        'ActionTargetArn': 'string'
    }
    
    
    :returns: 
    SecurityHub.Client.exceptions.InternalException
    SecurityHub.Client.exceptions.InvalidInputException
    SecurityHub.Client.exceptions.InvalidAccessException
    SecurityHub.Client.exceptions.LimitExceededException
    SecurityHub.Client.exceptions.ResourceConflictException
    
    """
    pass

def create_insight(Name=None, Filters=None, GroupByAttribute=None):
    """
    Creates a custom insight in Security Hub. An insight is a consolidation of findings that relate to a security issue that requires attention or remediation.
    To group the related findings in the insight, use the GroupByAttribute .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_insight(
        Name='string',
        Filters={
            'ProductArn': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'AwsAccountId': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'Id': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'GeneratorId': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'Type': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'FirstObservedAt': [
                {
                    'Start': 'string',
                    'End': 'string',
                    'DateRange': {
                        'Value': 123,
                        'Unit': 'DAYS'
                    }
                },
            ],
            'LastObservedAt': [
                {
                    'Start': 'string',
                    'End': 'string',
                    'DateRange': {
                        'Value': 123,
                        'Unit': 'DAYS'
                    }
                },
            ],
            'CreatedAt': [
                {
                    'Start': 'string',
                    'End': 'string',
                    'DateRange': {
                        'Value': 123,
                        'Unit': 'DAYS'
                    }
                },
            ],
            'UpdatedAt': [
                {
                    'Start': 'string',
                    'End': 'string',
                    'DateRange': {
                        'Value': 123,
                        'Unit': 'DAYS'
                    }
                },
            ],
            'SeverityProduct': [
                {
                    'Gte': 123.0,
                    'Lte': 123.0,
                    'Eq': 123.0
                },
            ],
            'SeverityNormalized': [
                {
                    'Gte': 123.0,
                    'Lte': 123.0,
                    'Eq': 123.0
                },
            ],
            'SeverityLabel': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'Confidence': [
                {
                    'Gte': 123.0,
                    'Lte': 123.0,
                    'Eq': 123.0
                },
            ],
            'Criticality': [
                {
                    'Gte': 123.0,
                    'Lte': 123.0,
                    'Eq': 123.0
                },
            ],
            'Title': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'Description': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'RecommendationText': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'SourceUrl': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ProductFields': [
                {
                    'Key': 'string',
                    'Value': 'string',
                    'Comparison': 'EQUALS'
                },
            ],
            'ProductName': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'CompanyName': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'UserDefinedFields': [
                {
                    'Key': 'string',
                    'Value': 'string',
                    'Comparison': 'EQUALS'
                },
            ],
            'MalwareName': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'MalwareType': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'MalwarePath': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'MalwareState': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'NetworkDirection': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'NetworkProtocol': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'NetworkSourceIpV4': [
                {
                    'Cidr': 'string'
                },
            ],
            'NetworkSourceIpV6': [
                {
                    'Cidr': 'string'
                },
            ],
            'NetworkSourcePort': [
                {
                    'Gte': 123.0,
                    'Lte': 123.0,
                    'Eq': 123.0
                },
            ],
            'NetworkSourceDomain': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'NetworkSourceMac': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'NetworkDestinationIpV4': [
                {
                    'Cidr': 'string'
                },
            ],
            'NetworkDestinationIpV6': [
                {
                    'Cidr': 'string'
                },
            ],
            'NetworkDestinationPort': [
                {
                    'Gte': 123.0,
                    'Lte': 123.0,
                    'Eq': 123.0
                },
            ],
            'NetworkDestinationDomain': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ProcessName': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ProcessPath': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ProcessPid': [
                {
                    'Gte': 123.0,
                    'Lte': 123.0,
                    'Eq': 123.0
                },
            ],
            'ProcessParentPid': [
                {
                    'Gte': 123.0,
                    'Lte': 123.0,
                    'Eq': 123.0
                },
            ],
            'ProcessLaunchedAt': [
                {
                    'Start': 'string',
                    'End': 'string',
                    'DateRange': {
                        'Value': 123,
                        'Unit': 'DAYS'
                    }
                },
            ],
            'ProcessTerminatedAt': [
                {
                    'Start': 'string',
                    'End': 'string',
                    'DateRange': {
                        'Value': 123,
                        'Unit': 'DAYS'
                    }
                },
            ],
            'ThreatIntelIndicatorType': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ThreatIntelIndicatorValue': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ThreatIntelIndicatorCategory': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ThreatIntelIndicatorLastObservedAt': [
                {
                    'Start': 'string',
                    'End': 'string',
                    'DateRange': {
                        'Value': 123,
                        'Unit': 'DAYS'
                    }
                },
            ],
            'ThreatIntelIndicatorSource': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ThreatIntelIndicatorSourceUrl': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceType': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceId': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourcePartition': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceRegion': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceTags': [
                {
                    'Key': 'string',
                    'Value': 'string',
                    'Comparison': 'EQUALS'
                },
            ],
            'ResourceAwsEc2InstanceType': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceAwsEc2InstanceImageId': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceAwsEc2InstanceIpV4Addresses': [
                {
                    'Cidr': 'string'
                },
            ],
            'ResourceAwsEc2InstanceIpV6Addresses': [
                {
                    'Cidr': 'string'
                },
            ],
            'ResourceAwsEc2InstanceKeyName': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceAwsEc2InstanceIamInstanceProfileArn': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceAwsEc2InstanceVpcId': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceAwsEc2InstanceSubnetId': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceAwsEc2InstanceLaunchedAt': [
                {
                    'Start': 'string',
                    'End': 'string',
                    'DateRange': {
                        'Value': 123,
                        'Unit': 'DAYS'
                    }
                },
            ],
            'ResourceAwsS3BucketOwnerId': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceAwsS3BucketOwnerName': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceAwsIamAccessKeyUserName': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceAwsIamAccessKeyStatus': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceAwsIamAccessKeyCreatedAt': [
                {
                    'Start': 'string',
                    'End': 'string',
                    'DateRange': {
                        'Value': 123,
                        'Unit': 'DAYS'
                    }
                },
            ],
            'ResourceContainerName': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceContainerImageId': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceContainerImageName': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceContainerLaunchedAt': [
                {
                    'Start': 'string',
                    'End': 'string',
                    'DateRange': {
                        'Value': 123,
                        'Unit': 'DAYS'
                    }
                },
            ],
            'ResourceDetailsOther': [
                {
                    'Key': 'string',
                    'Value': 'string',
                    'Comparison': 'EQUALS'
                },
            ],
            'ComplianceStatus': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'VerificationState': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'WorkflowState': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'WorkflowStatus': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'RecordState': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'RelatedFindingsProductArn': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'RelatedFindingsId': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'NoteText': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'NoteUpdatedAt': [
                {
                    'Start': 'string',
                    'End': 'string',
                    'DateRange': {
                        'Value': 123,
                        'Unit': 'DAYS'
                    }
                },
            ],
            'NoteUpdatedBy': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'Keyword': [
                {
                    'Value': 'string'
                },
            ]
        },
        GroupByAttribute='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the custom insight to create.\n

    :type Filters: dict
    :param Filters: [REQUIRED]\nOne or more attributes used to filter the findings included in the insight. The insight only includes findings that match the criteria defined in the filters.\n\nProductArn (list) --The ARN generated by Security Hub that uniquely identifies a third-party company (security findings provider) after this provider\'s product (solution that generates findings) is registered with Security Hub.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nAwsAccountId (list) --The AWS account ID that a finding is generated in.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nId (list) --The security findings provider-specific identifier for a finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nGeneratorId (list) --The identifier for the solution-specific component (a discrete unit of logic) that generated a finding. In various security-findings providers\' solutions, this generator can be called a rule, a check, a detector, a plugin, etc.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nType (list) --A finding type in the format of namespace/category/classifier that classifies a finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nFirstObservedAt (list) --An ISO8601-formatted timestamp that indicates when the security-findings provider first observed the potential security issue that a finding captured.\n\n(dict) --A date filter for querying findings.\n\nStart (string) --A start date for the date filter.\n\nEnd (string) --An end date for the date filter.\n\nDateRange (dict) --A date range for the date filter.\n\nValue (integer) --A date range value for the date filter.\n\nUnit (string) --A date range unit for the date filter.\n\n\n\n\n\n\n\nLastObservedAt (list) --An ISO8601-formatted timestamp that indicates when the security-findings provider most recently observed the potential security issue that a finding captured.\n\n(dict) --A date filter for querying findings.\n\nStart (string) --A start date for the date filter.\n\nEnd (string) --An end date for the date filter.\n\nDateRange (dict) --A date range for the date filter.\n\nValue (integer) --A date range value for the date filter.\n\nUnit (string) --A date range unit for the date filter.\n\n\n\n\n\n\n\nCreatedAt (list) --An ISO8601-formatted timestamp that indicates when the security-findings provider captured the potential security issue that a finding captured.\n\n(dict) --A date filter for querying findings.\n\nStart (string) --A start date for the date filter.\n\nEnd (string) --An end date for the date filter.\n\nDateRange (dict) --A date range for the date filter.\n\nValue (integer) --A date range value for the date filter.\n\nUnit (string) --A date range unit for the date filter.\n\n\n\n\n\n\n\nUpdatedAt (list) --An ISO8601-formatted timestamp that indicates when the security-findings provider last updated the finding record.\n\n(dict) --A date filter for querying findings.\n\nStart (string) --A start date for the date filter.\n\nEnd (string) --An end date for the date filter.\n\nDateRange (dict) --A date range for the date filter.\n\nValue (integer) --A date range value for the date filter.\n\nUnit (string) --A date range unit for the date filter.\n\n\n\n\n\n\n\nSeverityProduct (list) --The native severity as defined by the security-findings provider\'s solution that generated the finding.\n\n(dict) --A number filter for querying findings.\n\nGte (float) --The greater-than-equal condition to be applied to a single field when querying for findings.\n\nLte (float) --The less-than-equal condition to be applied to a single field when querying for findings.\n\nEq (float) --The equal-to condition to be applied to a single field when querying for findings.\n\n\n\n\n\nSeverityNormalized (list) --The normalized severity of a finding.\n\n(dict) --A number filter for querying findings.\n\nGte (float) --The greater-than-equal condition to be applied to a single field when querying for findings.\n\nLte (float) --The less-than-equal condition to be applied to a single field when querying for findings.\n\nEq (float) --The equal-to condition to be applied to a single field when querying for findings.\n\n\n\n\n\nSeverityLabel (list) --The label of a finding\'s severity.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nConfidence (list) --A finding\'s confidence. Confidence is defined as the likelihood that a finding accurately identifies the behavior or issue that it was intended to identify.\nConfidence is scored on a 0-100 basis using a ratio scale, where 0 means zero percent confidence and 100 means 100 percent confidence.\n\n(dict) --A number filter for querying findings.\n\nGte (float) --The greater-than-equal condition to be applied to a single field when querying for findings.\n\nLte (float) --The less-than-equal condition to be applied to a single field when querying for findings.\n\nEq (float) --The equal-to condition to be applied to a single field when querying for findings.\n\n\n\n\n\nCriticality (list) --The level of importance assigned to the resources associated with the finding.\nA score of 0 means that the underlying resources have no criticality, and a score of 100 is reserved for the most critical resources.\n\n(dict) --A number filter for querying findings.\n\nGte (float) --The greater-than-equal condition to be applied to a single field when querying for findings.\n\nLte (float) --The less-than-equal condition to be applied to a single field when querying for findings.\n\nEq (float) --The equal-to condition to be applied to a single field when querying for findings.\n\n\n\n\n\nTitle (list) --A finding\'s title.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nDescription (list) --A finding\'s description.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nRecommendationText (list) --The recommendation of what to do about the issue described in a finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nSourceUrl (list) --A URL that links to a page about the current finding in the security-findings provider\'s solution.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nProductFields (list) --A data type where security-findings providers can include additional solution-specific details that aren\'t part of the defined AwsSecurityFinding format.\n\n(dict) --The map filter for querying findings.\n\nKey (string) --The key of the map filter.\n\nValue (string) --The value for the key in the map filter.\n\nComparison (string) --The condition to apply to a key value when querying for findings with a map filter.\n\n\n\n\n\nProductName (list) --The name of the solution (product) that generates findings.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nCompanyName (list) --The name of the findings provider (company) that owns the solution (product) that generates findings.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nUserDefinedFields (list) --A list of name/value string pairs associated with the finding. These are custom, user-defined fields added to a finding.\n\n(dict) --The map filter for querying findings.\n\nKey (string) --The key of the map filter.\n\nValue (string) --The value for the key in the map filter.\n\nComparison (string) --The condition to apply to a key value when querying for findings with a map filter.\n\n\n\n\n\nMalwareName (list) --The name of the malware that was observed.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nMalwareType (list) --The type of the malware that was observed.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nMalwarePath (list) --The filesystem path of the malware that was observed.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nMalwareState (list) --The state of the malware that was observed.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nNetworkDirection (list) --Indicates the direction of network traffic associated with a finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nNetworkProtocol (list) --The protocol of network-related information about a finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nNetworkSourceIpV4 (list) --The source IPv4 address of network-related information about a finding.\n\n(dict) --The IP filter for querying findings.\n\nCidr (string) --A finding\'s CIDR value.\n\n\n\n\n\nNetworkSourceIpV6 (list) --The source IPv6 address of network-related information about a finding.\n\n(dict) --The IP filter for querying findings.\n\nCidr (string) --A finding\'s CIDR value.\n\n\n\n\n\nNetworkSourcePort (list) --The source port of network-related information about a finding.\n\n(dict) --A number filter for querying findings.\n\nGte (float) --The greater-than-equal condition to be applied to a single field when querying for findings.\n\nLte (float) --The less-than-equal condition to be applied to a single field when querying for findings.\n\nEq (float) --The equal-to condition to be applied to a single field when querying for findings.\n\n\n\n\n\nNetworkSourceDomain (list) --The source domain of network-related information about a finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nNetworkSourceMac (list) --The source media access control (MAC) address of network-related information about a finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nNetworkDestinationIpV4 (list) --The destination IPv4 address of network-related information about a finding.\n\n(dict) --The IP filter for querying findings.\n\nCidr (string) --A finding\'s CIDR value.\n\n\n\n\n\nNetworkDestinationIpV6 (list) --The destination IPv6 address of network-related information about a finding.\n\n(dict) --The IP filter for querying findings.\n\nCidr (string) --A finding\'s CIDR value.\n\n\n\n\n\nNetworkDestinationPort (list) --The destination port of network-related information about a finding.\n\n(dict) --A number filter for querying findings.\n\nGte (float) --The greater-than-equal condition to be applied to a single field when querying for findings.\n\nLte (float) --The less-than-equal condition to be applied to a single field when querying for findings.\n\nEq (float) --The equal-to condition to be applied to a single field when querying for findings.\n\n\n\n\n\nNetworkDestinationDomain (list) --The destination domain of network-related information about a finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nProcessName (list) --The name of the process.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nProcessPath (list) --The path to the process executable.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nProcessPid (list) --The process ID.\n\n(dict) --A number filter for querying findings.\n\nGte (float) --The greater-than-equal condition to be applied to a single field when querying for findings.\n\nLte (float) --The less-than-equal condition to be applied to a single field when querying for findings.\n\nEq (float) --The equal-to condition to be applied to a single field when querying for findings.\n\n\n\n\n\nProcessParentPid (list) --The parent process ID.\n\n(dict) --A number filter for querying findings.\n\nGte (float) --The greater-than-equal condition to be applied to a single field when querying for findings.\n\nLte (float) --The less-than-equal condition to be applied to a single field when querying for findings.\n\nEq (float) --The equal-to condition to be applied to a single field when querying for findings.\n\n\n\n\n\nProcessLaunchedAt (list) --The date/time that the process was launched.\n\n(dict) --A date filter for querying findings.\n\nStart (string) --A start date for the date filter.\n\nEnd (string) --An end date for the date filter.\n\nDateRange (dict) --A date range for the date filter.\n\nValue (integer) --A date range value for the date filter.\n\nUnit (string) --A date range unit for the date filter.\n\n\n\n\n\n\n\nProcessTerminatedAt (list) --The date/time that the process was terminated.\n\n(dict) --A date filter for querying findings.\n\nStart (string) --A start date for the date filter.\n\nEnd (string) --An end date for the date filter.\n\nDateRange (dict) --A date range for the date filter.\n\nValue (integer) --A date range value for the date filter.\n\nUnit (string) --A date range unit for the date filter.\n\n\n\n\n\n\n\nThreatIntelIndicatorType (list) --The type of a threat intelligence indicator.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nThreatIntelIndicatorValue (list) --The value of a threat intelligence indicator.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nThreatIntelIndicatorCategory (list) --The category of a threat intelligence indicator.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nThreatIntelIndicatorLastObservedAt (list) --The date/time of the last observation of a threat intelligence indicator.\n\n(dict) --A date filter for querying findings.\n\nStart (string) --A start date for the date filter.\n\nEnd (string) --An end date for the date filter.\n\nDateRange (dict) --A date range for the date filter.\n\nValue (integer) --A date range value for the date filter.\n\nUnit (string) --A date range unit for the date filter.\n\n\n\n\n\n\n\nThreatIntelIndicatorSource (list) --The source of the threat intelligence.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nThreatIntelIndicatorSourceUrl (list) --The URL for more details from the source of the threat intelligence.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceType (list) --Specifies the type of the resource that details are provided for.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceId (list) --The canonical identifier for the given resource type.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourcePartition (list) --The canonical AWS partition name that the Region is assigned to.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceRegion (list) --The canonical AWS external Region name where this resource is located.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceTags (list) --A list of AWS tags associated with a resource at the time the finding was processed.\n\n(dict) --The map filter for querying findings.\n\nKey (string) --The key of the map filter.\n\nValue (string) --The value for the key in the map filter.\n\nComparison (string) --The condition to apply to a key value when querying for findings with a map filter.\n\n\n\n\n\nResourceAwsEc2InstanceType (list) --The instance type of the instance.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceAwsEc2InstanceImageId (list) --The Amazon Machine Image (AMI) ID of the instance.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceAwsEc2InstanceIpV4Addresses (list) --The IPv4 addresses associated with the instance.\n\n(dict) --The IP filter for querying findings.\n\nCidr (string) --A finding\'s CIDR value.\n\n\n\n\n\nResourceAwsEc2InstanceIpV6Addresses (list) --The IPv6 addresses associated with the instance.\n\n(dict) --The IP filter for querying findings.\n\nCidr (string) --A finding\'s CIDR value.\n\n\n\n\n\nResourceAwsEc2InstanceKeyName (list) --The key name associated with the instance.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceAwsEc2InstanceIamInstanceProfileArn (list) --The IAM profile ARN of the instance.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceAwsEc2InstanceVpcId (list) --The identifier of the VPC that the instance was launched in.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceAwsEc2InstanceSubnetId (list) --The identifier of the subnet that the instance was launched in.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceAwsEc2InstanceLaunchedAt (list) --The date and time the instance was launched.\n\n(dict) --A date filter for querying findings.\n\nStart (string) --A start date for the date filter.\n\nEnd (string) --An end date for the date filter.\n\nDateRange (dict) --A date range for the date filter.\n\nValue (integer) --A date range value for the date filter.\n\nUnit (string) --A date range unit for the date filter.\n\n\n\n\n\n\n\nResourceAwsS3BucketOwnerId (list) --The canonical user ID of the owner of the S3 bucket.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceAwsS3BucketOwnerName (list) --The display name of the owner of the S3 bucket.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceAwsIamAccessKeyUserName (list) --The user associated with the IAM access key related to a finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceAwsIamAccessKeyStatus (list) --The status of the IAM access key related to a finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceAwsIamAccessKeyCreatedAt (list) --The creation date/time of the IAM access key related to a finding.\n\n(dict) --A date filter for querying findings.\n\nStart (string) --A start date for the date filter.\n\nEnd (string) --An end date for the date filter.\n\nDateRange (dict) --A date range for the date filter.\n\nValue (integer) --A date range value for the date filter.\n\nUnit (string) --A date range unit for the date filter.\n\n\n\n\n\n\n\nResourceContainerName (list) --The name of the container related to a finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceContainerImageId (list) --The identifier of the image related to a finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceContainerImageName (list) --The name of the image related to a finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceContainerLaunchedAt (list) --The date/time that the container was started.\n\n(dict) --A date filter for querying findings.\n\nStart (string) --A start date for the date filter.\n\nEnd (string) --An end date for the date filter.\n\nDateRange (dict) --A date range for the date filter.\n\nValue (integer) --A date range value for the date filter.\n\nUnit (string) --A date range unit for the date filter.\n\n\n\n\n\n\n\nResourceDetailsOther (list) --The details of a resource that doesn\'t have a specific subfield for the resource type defined.\n\n(dict) --The map filter for querying findings.\n\nKey (string) --The key of the map filter.\n\nValue (string) --The value for the key in the map filter.\n\nComparison (string) --The condition to apply to a key value when querying for findings with a map filter.\n\n\n\n\n\nComplianceStatus (list) --Exclusive to findings that are generated as the result of a check run against a specific rule in a supported standard, such as CIS AWS Foundations. Contains security standard-related finding details.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nVerificationState (list) --The veracity of a finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nWorkflowState (list) --The workflow state of a finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nWorkflowStatus (list) --The status of the investigation into a finding. Allowed values are the following.\n\nNEW - The initial state of a finding, before it is reviewed.\nNOTIFIED - Indicates that the resource owner has been notified about the security issue. Used when the initial reviewer is not the resource owner, and needs intervention from the resource owner.\nSUPPRESSED - The finding will not be reviewed again and will not be acted upon.\nRESOLVED - The finding was reviewed and remediated and is now considered resolved.\n\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nRecordState (list) --The updated record state for the finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nRelatedFindingsProductArn (list) --The ARN of the solution that generated a related finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nRelatedFindingsId (list) --The solution-generated identifier for a related finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nNoteText (list) --The text of a note.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nNoteUpdatedAt (list) --The timestamp of when the note was updated.\n\n(dict) --A date filter for querying findings.\n\nStart (string) --A start date for the date filter.\n\nEnd (string) --An end date for the date filter.\n\nDateRange (dict) --A date range for the date filter.\n\nValue (integer) --A date range value for the date filter.\n\nUnit (string) --A date range unit for the date filter.\n\n\n\n\n\n\n\nNoteUpdatedBy (list) --The principal that created a note.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nKeyword (list) --A keyword for a finding.\n\n(dict) --A keyword filter for querying findings.\n\nValue (string) --A value for the keyword.\n\n\n\n\n\n\n

    :type GroupByAttribute: string
    :param GroupByAttribute: [REQUIRED]\nThe attribute used to group the findings for the insight. The grouping attribute identifies the type of item that the insight applies to. For example, if an insight is grouped by resource identifier, then the insight produces a list of resource identifiers.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'InsightArn': 'string'
}


Response Structure

(dict) --

InsightArn (string) --
The ARN of the insight created.







Exceptions

SecurityHub.Client.exceptions.InternalException
SecurityHub.Client.exceptions.InvalidInputException
SecurityHub.Client.exceptions.LimitExceededException
SecurityHub.Client.exceptions.InvalidAccessException
SecurityHub.Client.exceptions.ResourceConflictException


    :return: {
        'InsightArn': 'string'
    }
    
    
    :returns: 
    SecurityHub.Client.exceptions.InternalException
    SecurityHub.Client.exceptions.InvalidInputException
    SecurityHub.Client.exceptions.LimitExceededException
    SecurityHub.Client.exceptions.InvalidAccessException
    SecurityHub.Client.exceptions.ResourceConflictException
    
    """
    pass

def create_members(AccountDetails=None):
    """
    Creates a member association in Security Hub between the specified accounts and the account used to make the request, which is the master account. To successfully create a member, you must use this action from an account that already has Security Hub enabled. To enable Security Hub, you can use the ``  EnableSecurityHub `` operation.
    After you use CreateMembers to create member account associations in Security Hub, you must use the ``  InviteMembers `` operation to invite the accounts to enable Security Hub and become member accounts in Security Hub.
    If the account owner accepts the invitation, the account becomes a member account in Security Hub. A permissions policy is added that permits the master account to view the findings generated in the member account. When Security Hub is enabled in the invited account, findings start to be sent to both the member and master accounts.
    To remove the association between the master and member accounts, use the ``  DisassociateFromMasterAccount `` or ``  DisassociateMembers `` operation.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_members(
        AccountDetails=[
            {
                'AccountId': 'string',
                'Email': 'string'
            },
        ]
    )
    
    
    :type AccountDetails: list
    :param AccountDetails: The list of accounts to associate with the Security Hub master account. For each account, the list includes the account ID and the email address.\n\n(dict) --The details of an AWS account.\n\nAccountId (string) --The ID of an AWS account.\n\nEmail (string) --The email of an AWS account.\n\n\n\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'UnprocessedAccounts': [
        {
            'AccountId': 'string',
            'ProcessingResult': 'string'
        },
    ]
}


Response Structure

(dict) --
UnprocessedAccounts (list) --The list of AWS accounts that were not processed. For each account, the list includes the account ID and the email address.

(dict) --Details about the account that was not processed.

AccountId (string) --An AWS account ID of the account that was not processed.

ProcessingResult (string) --The reason that the account was not processed.










Exceptions

SecurityHub.Client.exceptions.InternalException
SecurityHub.Client.exceptions.InvalidInputException
SecurityHub.Client.exceptions.LimitExceededException
SecurityHub.Client.exceptions.InvalidAccessException
SecurityHub.Client.exceptions.ResourceConflictException


    :return: {
        'UnprocessedAccounts': [
            {
                'AccountId': 'string',
                'ProcessingResult': 'string'
            },
        ]
    }
    
    
    """
    pass

def decline_invitations(AccountIds=None):
    """
    Declines invitations to become a member account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.decline_invitations(
        AccountIds=[
            'string',
        ]
    )
    
    
    :type AccountIds: list
    :param AccountIds: [REQUIRED]\nThe list of account IDs for the accounts from which to decline the invitations to Security Hub.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'UnprocessedAccounts': [
        {
            'AccountId': 'string',
            'ProcessingResult': 'string'
        },
    ]
}


Response Structure

(dict) --
UnprocessedAccounts (list) --The list of AWS accounts that were not processed. For each account, the list includes the account ID and the email address.

(dict) --Details about the account that was not processed.

AccountId (string) --An AWS account ID of the account that was not processed.

ProcessingResult (string) --The reason that the account was not processed.










Exceptions

SecurityHub.Client.exceptions.InternalException
SecurityHub.Client.exceptions.InvalidInputException
SecurityHub.Client.exceptions.InvalidAccessException
SecurityHub.Client.exceptions.ResourceNotFoundException


    :return: {
        'UnprocessedAccounts': [
            {
                'AccountId': 'string',
                'ProcessingResult': 'string'
            },
        ]
    }
    
    
    :returns: 
    SecurityHub.Client.exceptions.InternalException
    SecurityHub.Client.exceptions.InvalidInputException
    SecurityHub.Client.exceptions.InvalidAccessException
    SecurityHub.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def delete_action_target(ActionTargetArn=None):
    """
    Deletes a custom action target from Security Hub.
    Deleting a custom action target does not affect any findings or insights that were already sent to Amazon CloudWatch Events using the custom action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_action_target(
        ActionTargetArn='string'
    )
    
    
    :type ActionTargetArn: string
    :param ActionTargetArn: [REQUIRED]\nThe ARN of the custom action target to delete.\n

    :rtype: dict
ReturnsResponse Syntax{
    'ActionTargetArn': 'string'
}


Response Structure

(dict) --
ActionTargetArn (string) --The ARN of the custom action target that was deleted.






Exceptions

SecurityHub.Client.exceptions.InternalException
SecurityHub.Client.exceptions.InvalidInputException
SecurityHub.Client.exceptions.InvalidAccessException
SecurityHub.Client.exceptions.ResourceNotFoundException


    :return: {
        'ActionTargetArn': 'string'
    }
    
    
    """
    pass

def delete_insight(InsightArn=None):
    """
    Deletes the insight specified by the InsightArn .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_insight(
        InsightArn='string'
    )
    
    
    :type InsightArn: string
    :param InsightArn: [REQUIRED]\nThe ARN of the insight to delete.\n

    :rtype: dict
ReturnsResponse Syntax{
    'InsightArn': 'string'
}


Response Structure

(dict) --
InsightArn (string) --The ARN of the insight that was deleted.






Exceptions

SecurityHub.Client.exceptions.InternalException
SecurityHub.Client.exceptions.InvalidInputException
SecurityHub.Client.exceptions.InvalidAccessException
SecurityHub.Client.exceptions.LimitExceededException
SecurityHub.Client.exceptions.ResourceNotFoundException


    :return: {
        'InsightArn': 'string'
    }
    
    
    """
    pass

def delete_invitations(AccountIds=None):
    """
    Deletes invitations received by the AWS account to become a member account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_invitations(
        AccountIds=[
            'string',
        ]
    )
    
    
    :type AccountIds: list
    :param AccountIds: [REQUIRED]\nThe list of the account IDs that sent the invitations to delete.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'UnprocessedAccounts': [
        {
            'AccountId': 'string',
            'ProcessingResult': 'string'
        },
    ]
}


Response Structure

(dict) --
UnprocessedAccounts (list) --The list of AWS accounts for which the invitations were not deleted. For each account, the list includes the account ID and the email address.

(dict) --Details about the account that was not processed.

AccountId (string) --An AWS account ID of the account that was not processed.

ProcessingResult (string) --The reason that the account was not processed.










Exceptions

SecurityHub.Client.exceptions.InternalException
SecurityHub.Client.exceptions.InvalidInputException
SecurityHub.Client.exceptions.LimitExceededException
SecurityHub.Client.exceptions.ResourceNotFoundException
SecurityHub.Client.exceptions.InvalidAccessException


    :return: {
        'UnprocessedAccounts': [
            {
                'AccountId': 'string',
                'ProcessingResult': 'string'
            },
        ]
    }
    
    
    :returns: 
    SecurityHub.Client.exceptions.InternalException
    SecurityHub.Client.exceptions.InvalidInputException
    SecurityHub.Client.exceptions.LimitExceededException
    SecurityHub.Client.exceptions.ResourceNotFoundException
    SecurityHub.Client.exceptions.InvalidAccessException
    
    """
    pass

def delete_members(AccountIds=None):
    """
    Deletes the specified member accounts from Security Hub.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_members(
        AccountIds=[
            'string',
        ]
    )
    
    
    :type AccountIds: list
    :param AccountIds: The list of account IDs for the member accounts to delete.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'UnprocessedAccounts': [
        {
            'AccountId': 'string',
            'ProcessingResult': 'string'
        },
    ]
}


Response Structure

(dict) --
UnprocessedAccounts (list) --The list of AWS accounts that were not deleted. For each account, the list includes the account ID and the email address.

(dict) --Details about the account that was not processed.

AccountId (string) --An AWS account ID of the account that was not processed.

ProcessingResult (string) --The reason that the account was not processed.










Exceptions

SecurityHub.Client.exceptions.InternalException
SecurityHub.Client.exceptions.InvalidInputException
SecurityHub.Client.exceptions.InvalidAccessException
SecurityHub.Client.exceptions.LimitExceededException
SecurityHub.Client.exceptions.ResourceNotFoundException


    :return: {
        'UnprocessedAccounts': [
            {
                'AccountId': 'string',
                'ProcessingResult': 'string'
            },
        ]
    }
    
    
    :returns: 
    SecurityHub.Client.exceptions.InternalException
    SecurityHub.Client.exceptions.InvalidInputException
    SecurityHub.Client.exceptions.InvalidAccessException
    SecurityHub.Client.exceptions.LimitExceededException
    SecurityHub.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def describe_action_targets(ActionTargetArns=None, NextToken=None, MaxResults=None):
    """
    Returns a list of the custom action targets in Security Hub in your account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_action_targets(
        ActionTargetArns=[
            'string',
        ],
        NextToken='string',
        MaxResults=123
    )
    
    
    :type ActionTargetArns: list
    :param ActionTargetArns: A list of custom action target ARNs for the custom action targets to retrieve.\n\n(string) --\n\n

    :type NextToken: string
    :param NextToken: The token that is required for pagination. On your first call to the DescribeActionTargets operation, set the value of this parameter to NULL .\nFor subsequent calls to the operation, to continue listing data, set the value of this parameter to the value returned from the previous response.\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return.

    :rtype: dict

ReturnsResponse Syntax
{
    'ActionTargets': [
        {
            'ActionTargetArn': 'string',
            'Name': 'string',
            'Description': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

ActionTargets (list) --
A list of ActionTarget objects. Each object includes the ActionTargetArn , Description , and Name of a custom action target available in Security Hub.

(dict) --
An ActionTarget object.

ActionTargetArn (string) --
The ARN for the target action.

Name (string) --
The name of the action target.

Description (string) --
The description of the target action.





NextToken (string) --
The pagination token to use to request the next page of results.







Exceptions

SecurityHub.Client.exceptions.InternalException
SecurityHub.Client.exceptions.InvalidInputException
SecurityHub.Client.exceptions.InvalidAccessException
SecurityHub.Client.exceptions.ResourceNotFoundException


    :return: {
        'ActionTargets': [
            {
                'ActionTargetArn': 'string',
                'Name': 'string',
                'Description': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    SecurityHub.Client.exceptions.InternalException
    SecurityHub.Client.exceptions.InvalidInputException
    SecurityHub.Client.exceptions.InvalidAccessException
    SecurityHub.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def describe_hub(HubArn=None):
    """
    Returns details about the Hub resource in your account, including the HubArn and the time when you enabled Security Hub.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_hub(
        HubArn='string'
    )
    
    
    :type HubArn: string
    :param HubArn: The ARN of the Hub resource to retrieve.

    :rtype: dict
ReturnsResponse Syntax{
    'HubArn': 'string',
    'SubscribedAt': 'string'
}


Response Structure

(dict) --
HubArn (string) --The ARN of the Hub resource that was retrieved.

SubscribedAt (string) --The date and time when Security Hub was enabled in the account.






Exceptions

SecurityHub.Client.exceptions.InternalException
SecurityHub.Client.exceptions.LimitExceededException
SecurityHub.Client.exceptions.InvalidAccessException
SecurityHub.Client.exceptions.InvalidInputException
SecurityHub.Client.exceptions.ResourceNotFoundException


    :return: {
        'HubArn': 'string',
        'SubscribedAt': 'string'
    }
    
    
    """
    pass

def describe_products(NextToken=None, MaxResults=None):
    """
    Returns information about the available products that you can subscribe to and integrate with Security Hub in order to consolidate findings.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_products(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: The token that is required for pagination. On your first call to the DescribeProducts operation, set the value of this parameter to NULL .\nFor subsequent calls to the operation, to continue listing data, set the value of this parameter to the value returned from the previous response.\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return.

    :rtype: dict

ReturnsResponse Syntax
{
    'Products': [
        {
            'ProductArn': 'string',
            'ProductName': 'string',
            'CompanyName': 'string',
            'Description': 'string',
            'Categories': [
                'string',
            ],
            'IntegrationTypes': [
                'SEND_FINDINGS_TO_SECURITY_HUB'|'RECEIVE_FINDINGS_FROM_SECURITY_HUB',
            ],
            'MarketplaceUrl': 'string',
            'ActivationUrl': 'string',
            'ProductSubscriptionResourcePolicy': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Products (list) --
A list of products, including details for each product.

(dict) --
Contains details about a product.

ProductArn (string) --
The ARN assigned to the product.

ProductName (string) --
The name of the product.

CompanyName (string) --
The name of the company that provides the product.

Description (string) --
A description of the product.

Categories (list) --
The categories assigned to the product.

(string) --


IntegrationTypes (list) --
The types of integration that the product supports. Available values are the following.

SEND_FINDINGS_TO_SECURITY_HUB - Indicates that the integration sends findings to Security Hub.
RECEIVE_FINDINGS_FROM_SECURITY_HUB - Indicates that the integration receives findings from Security Hub.


(string) --


MarketplaceUrl (string) --
The URL for the page that contains more information about the product.

ActivationUrl (string) --
The URL used to activate the product.

ProductSubscriptionResourcePolicy (string) --
The resource policy associated with the product.





NextToken (string) --
The pagination token to use to request the next page of results.







Exceptions

SecurityHub.Client.exceptions.InternalException
SecurityHub.Client.exceptions.LimitExceededException
SecurityHub.Client.exceptions.InvalidAccessException
SecurityHub.Client.exceptions.InvalidInputException


    :return: {
        'Products': [
            {
                'ProductArn': 'string',
                'ProductName': 'string',
                'CompanyName': 'string',
                'Description': 'string',
                'Categories': [
                    'string',
                ],
                'IntegrationTypes': [
                    'SEND_FINDINGS_TO_SECURITY_HUB'|'RECEIVE_FINDINGS_FROM_SECURITY_HUB',
                ],
                'MarketplaceUrl': 'string',
                'ActivationUrl': 'string',
                'ProductSubscriptionResourcePolicy': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_standards(NextToken=None, MaxResults=None):
    """
    Returns a list of the available standards in Security Hub.
    For each standard, the results include the standard ARN, the name, and a description.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_standards(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: The token that is required for pagination. On your first call to the DescribeStandards operation, set the value of this parameter to NULL .\nFor subsequent calls to the operation, to continue listing data, set the value of this parameter to the value returned from the previous response.\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of standards to return.

    :rtype: dict

ReturnsResponse Syntax
{
    'Standards': [
        {
            'StandardsArn': 'string',
            'Name': 'string',
            'Description': 'string',
            'EnabledByDefault': True|False
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Standards (list) --
A list of available standards.

(dict) --
Provides information about a specific standard.

StandardsArn (string) --
The ARN of a standard.

Name (string) --
The name of the standard.

Description (string) --
A description of the standard.

EnabledByDefault (boolean) --
Whether the standard is enabled by default. When Security Hub is enabled from the console, if a standard is enabled by default, the check box for that standard is selected by default.
When Security Hub is enabled using the EnableSecurityHub API operation, the standard is enabled by default unless EnableDefaultStandards is set to false .





NextToken (string) --
The pagination token to use to request the next page of results.







Exceptions

SecurityHub.Client.exceptions.InternalException
SecurityHub.Client.exceptions.InvalidInputException
SecurityHub.Client.exceptions.InvalidAccessException


    :return: {
        'Standards': [
            {
                'StandardsArn': 'string',
                'Name': 'string',
                'Description': 'string',
                'EnabledByDefault': True|False
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    SecurityHub.Client.exceptions.InternalException
    SecurityHub.Client.exceptions.InvalidInputException
    SecurityHub.Client.exceptions.InvalidAccessException
    
    """
    pass

def describe_standards_controls(StandardsSubscriptionArn=None, NextToken=None, MaxResults=None):
    """
    Returns a list of security standards controls.
    For each control, the results include information about whether it is currently enabled, the severity, and a link to remediation information.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_standards_controls(
        StandardsSubscriptionArn='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type StandardsSubscriptionArn: string
    :param StandardsSubscriptionArn: [REQUIRED]\nThe ARN of a resource that represents your subscription to a supported standard.\n

    :type NextToken: string
    :param NextToken: The token that is required for pagination. On your first call to the DescribeStandardsControls operation, set the value of this parameter to NULL .\nFor subsequent calls to the operation, to continue listing data, set the value of this parameter to the value returned from the previous response.\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of security standard controls to return.

    :rtype: dict

ReturnsResponse Syntax
{
    'Controls': [
        {
            'StandardsControlArn': 'string',
            'ControlStatus': 'ENABLED'|'DISABLED',
            'DisabledReason': 'string',
            'ControlStatusUpdatedAt': datetime(2015, 1, 1),
            'ControlId': 'string',
            'Title': 'string',
            'Description': 'string',
            'RemediationUrl': 'string',
            'SeverityRating': 'LOW'|'MEDIUM'|'HIGH'|'CRITICAL',
            'RelatedRequirements': [
                'string',
            ]
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Controls (list) --
A list of security standards controls.

(dict) --
Details for an individual security standard control.

StandardsControlArn (string) --
The ARN of the security standard control.

ControlStatus (string) --
The current status of the security standard control. Indicates whether the control is enabled or disabled. Security Hub does not check against disabled controls.

DisabledReason (string) --
The reason provided for the most recent change in status for the control.

ControlStatusUpdatedAt (datetime) --
The date and time that the status of the security standard control was most recently updated.

ControlId (string) --
The identifier of the security standard control.

Title (string) --
The title of the security standard control.

Description (string) --
The longer description of the security standard control. Provides information about what the control is checking for.

RemediationUrl (string) --
A link to remediation information for the control in the Security Hub user documentation.

SeverityRating (string) --
The severity of findings generated from this security standard control.
The finding severity is based on an assessment of how easy it would be to compromise AWS resources if the issue is detected.

RelatedRequirements (list) --
The list of requirements that are related to this control.

(string) --






NextToken (string) --
The pagination token to use to request the next page of results.







Exceptions

SecurityHub.Client.exceptions.InternalException
SecurityHub.Client.exceptions.InvalidInputException
SecurityHub.Client.exceptions.InvalidAccessException
SecurityHub.Client.exceptions.ResourceNotFoundException


    :return: {
        'Controls': [
            {
                'StandardsControlArn': 'string',
                'ControlStatus': 'ENABLED'|'DISABLED',
                'DisabledReason': 'string',
                'ControlStatusUpdatedAt': datetime(2015, 1, 1),
                'ControlId': 'string',
                'Title': 'string',
                'Description': 'string',
                'RemediationUrl': 'string',
                'SeverityRating': 'LOW'|'MEDIUM'|'HIGH'|'CRITICAL',
                'RelatedRequirements': [
                    'string',
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def disable_import_findings_for_product(ProductSubscriptionArn=None):
    """
    Disables the integration of the specified product with Security Hub. After the integration is disabled, findings from that product are no longer sent to Security Hub.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disable_import_findings_for_product(
        ProductSubscriptionArn='string'
    )
    
    
    :type ProductSubscriptionArn: string
    :param ProductSubscriptionArn: [REQUIRED]\nThe ARN of the integrated product to disable the integration for.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

SecurityHub.Client.exceptions.InternalException
SecurityHub.Client.exceptions.InvalidInputException
SecurityHub.Client.exceptions.ResourceNotFoundException
SecurityHub.Client.exceptions.InvalidAccessException
SecurityHub.Client.exceptions.LimitExceededException


    :return: {}
    
    
    :returns: 
    SecurityHub.Client.exceptions.InternalException
    SecurityHub.Client.exceptions.InvalidInputException
    SecurityHub.Client.exceptions.ResourceNotFoundException
    SecurityHub.Client.exceptions.InvalidAccessException
    SecurityHub.Client.exceptions.LimitExceededException
    
    """
    pass

def disable_security_hub():
    """
    Disables Security Hub in your account only in the current Region. To disable Security Hub in all Regions, you must submit one request per Region where you have enabled Security Hub.
    When you disable Security Hub for a master account, it doesn\'t disable Security Hub for any associated member accounts.
    When you disable Security Hub, your existing findings and insights and any Security Hub configuration settings are deleted after 90 days and cannot be recovered. Any standards that were enabled are disabled, and your master and member account associations are removed.
    If you want to save your existing findings, you must export them before you disable Security Hub.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disable_security_hub()
    
    
    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

SecurityHub.Client.exceptions.InternalException
SecurityHub.Client.exceptions.LimitExceededException
SecurityHub.Client.exceptions.InvalidAccessException
SecurityHub.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    SecurityHub.Client.exceptions.InternalException
    SecurityHub.Client.exceptions.LimitExceededException
    SecurityHub.Client.exceptions.InvalidAccessException
    SecurityHub.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def disassociate_from_master_account():
    """
    Disassociates the current Security Hub member account from the associated master account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disassociate_from_master_account()
    
    
    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

SecurityHub.Client.exceptions.InternalException
SecurityHub.Client.exceptions.InvalidInputException
SecurityHub.Client.exceptions.InvalidAccessException
SecurityHub.Client.exceptions.LimitExceededException
SecurityHub.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    SecurityHub.Client.exceptions.InternalException
    SecurityHub.Client.exceptions.InvalidInputException
    SecurityHub.Client.exceptions.InvalidAccessException
    SecurityHub.Client.exceptions.LimitExceededException
    SecurityHub.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def disassociate_members(AccountIds=None):
    """
    Disassociates the specified member accounts from the associated master account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disassociate_members(
        AccountIds=[
            'string',
        ]
    )
    
    
    :type AccountIds: list
    :param AccountIds: The account IDs of the member accounts to disassociate from the master account.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

SecurityHub.Client.exceptions.InternalException
SecurityHub.Client.exceptions.InvalidInputException
SecurityHub.Client.exceptions.InvalidAccessException
SecurityHub.Client.exceptions.LimitExceededException
SecurityHub.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def enable_import_findings_for_product(ProductArn=None):
    """
    Enables the integration of a partner product with Security Hub. Integrated products send findings to Security Hub.
    When you enable a product integration, a permissions policy that grants permission for the product to send findings to Security Hub is applied.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.enable_import_findings_for_product(
        ProductArn='string'
    )
    
    
    :type ProductArn: string
    :param ProductArn: [REQUIRED]\nThe ARN of the product to enable the integration for.\n

    :rtype: dict
ReturnsResponse Syntax{
    'ProductSubscriptionArn': 'string'
}


Response Structure

(dict) --
ProductSubscriptionArn (string) --The ARN of your subscription to the product to enable integrations for.






Exceptions

SecurityHub.Client.exceptions.InternalException
SecurityHub.Client.exceptions.InvalidInputException
SecurityHub.Client.exceptions.InvalidAccessException
SecurityHub.Client.exceptions.ResourceConflictException
SecurityHub.Client.exceptions.LimitExceededException


    :return: {
        'ProductSubscriptionArn': 'string'
    }
    
    
    """
    pass

def enable_security_hub(Tags=None, EnableDefaultStandards=None):
    """
    Enables Security Hub for your account in the current Region or the Region you specify in the request.
    When you enable Security Hub, you grant to Security Hub the permissions necessary to gather findings from other services that are integrated with Security Hub.
    When you use the EnableSecurityHub operation to enable Security Hub, you also automatically enable the following standards.
    You do not enable the Payment Card Industry Data Security Standard (PCI DSS) standard.
    To not enable the automatically enabled standards, set EnableDefaultStandards to false .
    After you enable Security Hub, to enable a standard, use the ``  BatchEnableStandards `` operation. To disable a standard, use the ``  BatchDisableStandards `` operation.
    To learn more, see Setting Up AWS Security Hub in the AWS Security Hub User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.enable_security_hub(
        Tags={
            'string': 'string'
        },
        EnableDefaultStandards=True|False
    )
    
    
    :type Tags: dict
    :param Tags: The tags to add to the hub resource when you enable Security Hub.\n\n(string) --\n(string) --\n\n\n\n

    :type EnableDefaultStandards: boolean
    :param EnableDefaultStandards: Whether to enable the security standards that Security Hub has designated as automatically enabled. If you do not provide a value for EnableDefaultStandards , it is set to true . To not enable the automatically enabled standards, set EnableDefaultStandards to false .

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

SecurityHub.Client.exceptions.InternalException
SecurityHub.Client.exceptions.LimitExceededException
SecurityHub.Client.exceptions.InvalidAccessException
SecurityHub.Client.exceptions.ResourceConflictException
SecurityHub.Client.exceptions.AccessDeniedException


    :return: {}
    
    
    :returns: 
    Tags (dict) -- The tags to add to the hub resource when you enable Security Hub.
    
    (string) --
    (string) --
    
    
    
    
    EnableDefaultStandards (boolean) -- Whether to enable the security standards that Security Hub has designated as automatically enabled. If you do not provide a value for EnableDefaultStandards , it is set to true . To not enable the automatically enabled standards, set EnableDefaultStandards to false .
    
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

def get_enabled_standards(StandardsSubscriptionArns=None, NextToken=None, MaxResults=None):
    """
    Returns a list of the standards that are currently enabled.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_enabled_standards(
        StandardsSubscriptionArns=[
            'string',
        ],
        NextToken='string',
        MaxResults=123
    )
    
    
    :type StandardsSubscriptionArns: list
    :param StandardsSubscriptionArns: The list of the standards subscription ARNs for the standards to retrieve.\n\n(string) --\n\n

    :type NextToken: string
    :param NextToken: The token that is required for pagination. On your first call to the GetEnabledStandards operation, set the value of this parameter to NULL .\nFor subsequent calls to the operation, to continue listing data, set the value of this parameter to the value returned from the previous response.\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in the response.

    :rtype: dict

ReturnsResponse Syntax
{
    'StandardsSubscriptions': [
        {
            'StandardsSubscriptionArn': 'string',
            'StandardsArn': 'string',
            'StandardsInput': {
                'string': 'string'
            },
            'StandardsStatus': 'PENDING'|'READY'|'FAILED'|'DELETING'|'INCOMPLETE'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

StandardsSubscriptions (list) --
The list of StandardsSubscriptions objects that include information about the enabled standards.

(dict) --
A resource that represents your subscription to a supported standard.

StandardsSubscriptionArn (string) --
The ARN of a resource that represents your subscription to a supported standard.

StandardsArn (string) --
The ARN of a standard.

StandardsInput (dict) --
A key-value pair of input for the standard.

(string) --
(string) --




StandardsStatus (string) --
The status of the standards subscription.





NextToken (string) --
The pagination token to use to request the next page of results.







Exceptions

SecurityHub.Client.exceptions.InternalException
SecurityHub.Client.exceptions.InvalidInputException
SecurityHub.Client.exceptions.InvalidAccessException
SecurityHub.Client.exceptions.LimitExceededException


    :return: {
        'StandardsSubscriptions': [
            {
                'StandardsSubscriptionArn': 'string',
                'StandardsArn': 'string',
                'StandardsInput': {
                    'string': 'string'
                },
                'StandardsStatus': 'PENDING'|'READY'|'FAILED'|'DELETING'|'INCOMPLETE'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def get_findings(Filters=None, SortCriteria=None, NextToken=None, MaxResults=None):
    """
    Returns a list of findings that match the specified criteria.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_findings(
        Filters={
            'ProductArn': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'AwsAccountId': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'Id': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'GeneratorId': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'Type': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'FirstObservedAt': [
                {
                    'Start': 'string',
                    'End': 'string',
                    'DateRange': {
                        'Value': 123,
                        'Unit': 'DAYS'
                    }
                },
            ],
            'LastObservedAt': [
                {
                    'Start': 'string',
                    'End': 'string',
                    'DateRange': {
                        'Value': 123,
                        'Unit': 'DAYS'
                    }
                },
            ],
            'CreatedAt': [
                {
                    'Start': 'string',
                    'End': 'string',
                    'DateRange': {
                        'Value': 123,
                        'Unit': 'DAYS'
                    }
                },
            ],
            'UpdatedAt': [
                {
                    'Start': 'string',
                    'End': 'string',
                    'DateRange': {
                        'Value': 123,
                        'Unit': 'DAYS'
                    }
                },
            ],
            'SeverityProduct': [
                {
                    'Gte': 123.0,
                    'Lte': 123.0,
                    'Eq': 123.0
                },
            ],
            'SeverityNormalized': [
                {
                    'Gte': 123.0,
                    'Lte': 123.0,
                    'Eq': 123.0
                },
            ],
            'SeverityLabel': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'Confidence': [
                {
                    'Gte': 123.0,
                    'Lte': 123.0,
                    'Eq': 123.0
                },
            ],
            'Criticality': [
                {
                    'Gte': 123.0,
                    'Lte': 123.0,
                    'Eq': 123.0
                },
            ],
            'Title': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'Description': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'RecommendationText': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'SourceUrl': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ProductFields': [
                {
                    'Key': 'string',
                    'Value': 'string',
                    'Comparison': 'EQUALS'
                },
            ],
            'ProductName': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'CompanyName': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'UserDefinedFields': [
                {
                    'Key': 'string',
                    'Value': 'string',
                    'Comparison': 'EQUALS'
                },
            ],
            'MalwareName': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'MalwareType': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'MalwarePath': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'MalwareState': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'NetworkDirection': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'NetworkProtocol': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'NetworkSourceIpV4': [
                {
                    'Cidr': 'string'
                },
            ],
            'NetworkSourceIpV6': [
                {
                    'Cidr': 'string'
                },
            ],
            'NetworkSourcePort': [
                {
                    'Gte': 123.0,
                    'Lte': 123.0,
                    'Eq': 123.0
                },
            ],
            'NetworkSourceDomain': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'NetworkSourceMac': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'NetworkDestinationIpV4': [
                {
                    'Cidr': 'string'
                },
            ],
            'NetworkDestinationIpV6': [
                {
                    'Cidr': 'string'
                },
            ],
            'NetworkDestinationPort': [
                {
                    'Gte': 123.0,
                    'Lte': 123.0,
                    'Eq': 123.0
                },
            ],
            'NetworkDestinationDomain': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ProcessName': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ProcessPath': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ProcessPid': [
                {
                    'Gte': 123.0,
                    'Lte': 123.0,
                    'Eq': 123.0
                },
            ],
            'ProcessParentPid': [
                {
                    'Gte': 123.0,
                    'Lte': 123.0,
                    'Eq': 123.0
                },
            ],
            'ProcessLaunchedAt': [
                {
                    'Start': 'string',
                    'End': 'string',
                    'DateRange': {
                        'Value': 123,
                        'Unit': 'DAYS'
                    }
                },
            ],
            'ProcessTerminatedAt': [
                {
                    'Start': 'string',
                    'End': 'string',
                    'DateRange': {
                        'Value': 123,
                        'Unit': 'DAYS'
                    }
                },
            ],
            'ThreatIntelIndicatorType': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ThreatIntelIndicatorValue': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ThreatIntelIndicatorCategory': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ThreatIntelIndicatorLastObservedAt': [
                {
                    'Start': 'string',
                    'End': 'string',
                    'DateRange': {
                        'Value': 123,
                        'Unit': 'DAYS'
                    }
                },
            ],
            'ThreatIntelIndicatorSource': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ThreatIntelIndicatorSourceUrl': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceType': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceId': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourcePartition': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceRegion': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceTags': [
                {
                    'Key': 'string',
                    'Value': 'string',
                    'Comparison': 'EQUALS'
                },
            ],
            'ResourceAwsEc2InstanceType': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceAwsEc2InstanceImageId': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceAwsEc2InstanceIpV4Addresses': [
                {
                    'Cidr': 'string'
                },
            ],
            'ResourceAwsEc2InstanceIpV6Addresses': [
                {
                    'Cidr': 'string'
                },
            ],
            'ResourceAwsEc2InstanceKeyName': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceAwsEc2InstanceIamInstanceProfileArn': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceAwsEc2InstanceVpcId': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceAwsEc2InstanceSubnetId': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceAwsEc2InstanceLaunchedAt': [
                {
                    'Start': 'string',
                    'End': 'string',
                    'DateRange': {
                        'Value': 123,
                        'Unit': 'DAYS'
                    }
                },
            ],
            'ResourceAwsS3BucketOwnerId': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceAwsS3BucketOwnerName': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceAwsIamAccessKeyUserName': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceAwsIamAccessKeyStatus': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceAwsIamAccessKeyCreatedAt': [
                {
                    'Start': 'string',
                    'End': 'string',
                    'DateRange': {
                        'Value': 123,
                        'Unit': 'DAYS'
                    }
                },
            ],
            'ResourceContainerName': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceContainerImageId': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceContainerImageName': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceContainerLaunchedAt': [
                {
                    'Start': 'string',
                    'End': 'string',
                    'DateRange': {
                        'Value': 123,
                        'Unit': 'DAYS'
                    }
                },
            ],
            'ResourceDetailsOther': [
                {
                    'Key': 'string',
                    'Value': 'string',
                    'Comparison': 'EQUALS'
                },
            ],
            'ComplianceStatus': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'VerificationState': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'WorkflowState': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'WorkflowStatus': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'RecordState': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'RelatedFindingsProductArn': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'RelatedFindingsId': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'NoteText': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'NoteUpdatedAt': [
                {
                    'Start': 'string',
                    'End': 'string',
                    'DateRange': {
                        'Value': 123,
                        'Unit': 'DAYS'
                    }
                },
            ],
            'NoteUpdatedBy': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'Keyword': [
                {
                    'Value': 'string'
                },
            ]
        },
        SortCriteria=[
            {
                'Field': 'string',
                'SortOrder': 'asc'|'desc'
            },
        ],
        NextToken='string',
        MaxResults=123
    )
    
    
    :type Filters: dict
    :param Filters: The finding attributes used to define a condition to filter the returned findings.\n\nProductArn (list) --The ARN generated by Security Hub that uniquely identifies a third-party company (security findings provider) after this provider\'s product (solution that generates findings) is registered with Security Hub.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nAwsAccountId (list) --The AWS account ID that a finding is generated in.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nId (list) --The security findings provider-specific identifier for a finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nGeneratorId (list) --The identifier for the solution-specific component (a discrete unit of logic) that generated a finding. In various security-findings providers\' solutions, this generator can be called a rule, a check, a detector, a plugin, etc.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nType (list) --A finding type in the format of namespace/category/classifier that classifies a finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nFirstObservedAt (list) --An ISO8601-formatted timestamp that indicates when the security-findings provider first observed the potential security issue that a finding captured.\n\n(dict) --A date filter for querying findings.\n\nStart (string) --A start date for the date filter.\n\nEnd (string) --An end date for the date filter.\n\nDateRange (dict) --A date range for the date filter.\n\nValue (integer) --A date range value for the date filter.\n\nUnit (string) --A date range unit for the date filter.\n\n\n\n\n\n\n\nLastObservedAt (list) --An ISO8601-formatted timestamp that indicates when the security-findings provider most recently observed the potential security issue that a finding captured.\n\n(dict) --A date filter for querying findings.\n\nStart (string) --A start date for the date filter.\n\nEnd (string) --An end date for the date filter.\n\nDateRange (dict) --A date range for the date filter.\n\nValue (integer) --A date range value for the date filter.\n\nUnit (string) --A date range unit for the date filter.\n\n\n\n\n\n\n\nCreatedAt (list) --An ISO8601-formatted timestamp that indicates when the security-findings provider captured the potential security issue that a finding captured.\n\n(dict) --A date filter for querying findings.\n\nStart (string) --A start date for the date filter.\n\nEnd (string) --An end date for the date filter.\n\nDateRange (dict) --A date range for the date filter.\n\nValue (integer) --A date range value for the date filter.\n\nUnit (string) --A date range unit for the date filter.\n\n\n\n\n\n\n\nUpdatedAt (list) --An ISO8601-formatted timestamp that indicates when the security-findings provider last updated the finding record.\n\n(dict) --A date filter for querying findings.\n\nStart (string) --A start date for the date filter.\n\nEnd (string) --An end date for the date filter.\n\nDateRange (dict) --A date range for the date filter.\n\nValue (integer) --A date range value for the date filter.\n\nUnit (string) --A date range unit for the date filter.\n\n\n\n\n\n\n\nSeverityProduct (list) --The native severity as defined by the security-findings provider\'s solution that generated the finding.\n\n(dict) --A number filter for querying findings.\n\nGte (float) --The greater-than-equal condition to be applied to a single field when querying for findings.\n\nLte (float) --The less-than-equal condition to be applied to a single field when querying for findings.\n\nEq (float) --The equal-to condition to be applied to a single field when querying for findings.\n\n\n\n\n\nSeverityNormalized (list) --The normalized severity of a finding.\n\n(dict) --A number filter for querying findings.\n\nGte (float) --The greater-than-equal condition to be applied to a single field when querying for findings.\n\nLte (float) --The less-than-equal condition to be applied to a single field when querying for findings.\n\nEq (float) --The equal-to condition to be applied to a single field when querying for findings.\n\n\n\n\n\nSeverityLabel (list) --The label of a finding\'s severity.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nConfidence (list) --A finding\'s confidence. Confidence is defined as the likelihood that a finding accurately identifies the behavior or issue that it was intended to identify.\nConfidence is scored on a 0-100 basis using a ratio scale, where 0 means zero percent confidence and 100 means 100 percent confidence.\n\n(dict) --A number filter for querying findings.\n\nGte (float) --The greater-than-equal condition to be applied to a single field when querying for findings.\n\nLte (float) --The less-than-equal condition to be applied to a single field when querying for findings.\n\nEq (float) --The equal-to condition to be applied to a single field when querying for findings.\n\n\n\n\n\nCriticality (list) --The level of importance assigned to the resources associated with the finding.\nA score of 0 means that the underlying resources have no criticality, and a score of 100 is reserved for the most critical resources.\n\n(dict) --A number filter for querying findings.\n\nGte (float) --The greater-than-equal condition to be applied to a single field when querying for findings.\n\nLte (float) --The less-than-equal condition to be applied to a single field when querying for findings.\n\nEq (float) --The equal-to condition to be applied to a single field when querying for findings.\n\n\n\n\n\nTitle (list) --A finding\'s title.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nDescription (list) --A finding\'s description.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nRecommendationText (list) --The recommendation of what to do about the issue described in a finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nSourceUrl (list) --A URL that links to a page about the current finding in the security-findings provider\'s solution.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nProductFields (list) --A data type where security-findings providers can include additional solution-specific details that aren\'t part of the defined AwsSecurityFinding format.\n\n(dict) --The map filter for querying findings.\n\nKey (string) --The key of the map filter.\n\nValue (string) --The value for the key in the map filter.\n\nComparison (string) --The condition to apply to a key value when querying for findings with a map filter.\n\n\n\n\n\nProductName (list) --The name of the solution (product) that generates findings.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nCompanyName (list) --The name of the findings provider (company) that owns the solution (product) that generates findings.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nUserDefinedFields (list) --A list of name/value string pairs associated with the finding. These are custom, user-defined fields added to a finding.\n\n(dict) --The map filter for querying findings.\n\nKey (string) --The key of the map filter.\n\nValue (string) --The value for the key in the map filter.\n\nComparison (string) --The condition to apply to a key value when querying for findings with a map filter.\n\n\n\n\n\nMalwareName (list) --The name of the malware that was observed.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nMalwareType (list) --The type of the malware that was observed.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nMalwarePath (list) --The filesystem path of the malware that was observed.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nMalwareState (list) --The state of the malware that was observed.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nNetworkDirection (list) --Indicates the direction of network traffic associated with a finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nNetworkProtocol (list) --The protocol of network-related information about a finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nNetworkSourceIpV4 (list) --The source IPv4 address of network-related information about a finding.\n\n(dict) --The IP filter for querying findings.\n\nCidr (string) --A finding\'s CIDR value.\n\n\n\n\n\nNetworkSourceIpV6 (list) --The source IPv6 address of network-related information about a finding.\n\n(dict) --The IP filter for querying findings.\n\nCidr (string) --A finding\'s CIDR value.\n\n\n\n\n\nNetworkSourcePort (list) --The source port of network-related information about a finding.\n\n(dict) --A number filter for querying findings.\n\nGte (float) --The greater-than-equal condition to be applied to a single field when querying for findings.\n\nLte (float) --The less-than-equal condition to be applied to a single field when querying for findings.\n\nEq (float) --The equal-to condition to be applied to a single field when querying for findings.\n\n\n\n\n\nNetworkSourceDomain (list) --The source domain of network-related information about a finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nNetworkSourceMac (list) --The source media access control (MAC) address of network-related information about a finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nNetworkDestinationIpV4 (list) --The destination IPv4 address of network-related information about a finding.\n\n(dict) --The IP filter for querying findings.\n\nCidr (string) --A finding\'s CIDR value.\n\n\n\n\n\nNetworkDestinationIpV6 (list) --The destination IPv6 address of network-related information about a finding.\n\n(dict) --The IP filter for querying findings.\n\nCidr (string) --A finding\'s CIDR value.\n\n\n\n\n\nNetworkDestinationPort (list) --The destination port of network-related information about a finding.\n\n(dict) --A number filter for querying findings.\n\nGte (float) --The greater-than-equal condition to be applied to a single field when querying for findings.\n\nLte (float) --The less-than-equal condition to be applied to a single field when querying for findings.\n\nEq (float) --The equal-to condition to be applied to a single field when querying for findings.\n\n\n\n\n\nNetworkDestinationDomain (list) --The destination domain of network-related information about a finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nProcessName (list) --The name of the process.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nProcessPath (list) --The path to the process executable.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nProcessPid (list) --The process ID.\n\n(dict) --A number filter for querying findings.\n\nGte (float) --The greater-than-equal condition to be applied to a single field when querying for findings.\n\nLte (float) --The less-than-equal condition to be applied to a single field when querying for findings.\n\nEq (float) --The equal-to condition to be applied to a single field when querying for findings.\n\n\n\n\n\nProcessParentPid (list) --The parent process ID.\n\n(dict) --A number filter for querying findings.\n\nGte (float) --The greater-than-equal condition to be applied to a single field when querying for findings.\n\nLte (float) --The less-than-equal condition to be applied to a single field when querying for findings.\n\nEq (float) --The equal-to condition to be applied to a single field when querying for findings.\n\n\n\n\n\nProcessLaunchedAt (list) --The date/time that the process was launched.\n\n(dict) --A date filter for querying findings.\n\nStart (string) --A start date for the date filter.\n\nEnd (string) --An end date for the date filter.\n\nDateRange (dict) --A date range for the date filter.\n\nValue (integer) --A date range value for the date filter.\n\nUnit (string) --A date range unit for the date filter.\n\n\n\n\n\n\n\nProcessTerminatedAt (list) --The date/time that the process was terminated.\n\n(dict) --A date filter for querying findings.\n\nStart (string) --A start date for the date filter.\n\nEnd (string) --An end date for the date filter.\n\nDateRange (dict) --A date range for the date filter.\n\nValue (integer) --A date range value for the date filter.\n\nUnit (string) --A date range unit for the date filter.\n\n\n\n\n\n\n\nThreatIntelIndicatorType (list) --The type of a threat intelligence indicator.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nThreatIntelIndicatorValue (list) --The value of a threat intelligence indicator.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nThreatIntelIndicatorCategory (list) --The category of a threat intelligence indicator.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nThreatIntelIndicatorLastObservedAt (list) --The date/time of the last observation of a threat intelligence indicator.\n\n(dict) --A date filter for querying findings.\n\nStart (string) --A start date for the date filter.\n\nEnd (string) --An end date for the date filter.\n\nDateRange (dict) --A date range for the date filter.\n\nValue (integer) --A date range value for the date filter.\n\nUnit (string) --A date range unit for the date filter.\n\n\n\n\n\n\n\nThreatIntelIndicatorSource (list) --The source of the threat intelligence.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nThreatIntelIndicatorSourceUrl (list) --The URL for more details from the source of the threat intelligence.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceType (list) --Specifies the type of the resource that details are provided for.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceId (list) --The canonical identifier for the given resource type.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourcePartition (list) --The canonical AWS partition name that the Region is assigned to.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceRegion (list) --The canonical AWS external Region name where this resource is located.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceTags (list) --A list of AWS tags associated with a resource at the time the finding was processed.\n\n(dict) --The map filter for querying findings.\n\nKey (string) --The key of the map filter.\n\nValue (string) --The value for the key in the map filter.\n\nComparison (string) --The condition to apply to a key value when querying for findings with a map filter.\n\n\n\n\n\nResourceAwsEc2InstanceType (list) --The instance type of the instance.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceAwsEc2InstanceImageId (list) --The Amazon Machine Image (AMI) ID of the instance.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceAwsEc2InstanceIpV4Addresses (list) --The IPv4 addresses associated with the instance.\n\n(dict) --The IP filter for querying findings.\n\nCidr (string) --A finding\'s CIDR value.\n\n\n\n\n\nResourceAwsEc2InstanceIpV6Addresses (list) --The IPv6 addresses associated with the instance.\n\n(dict) --The IP filter for querying findings.\n\nCidr (string) --A finding\'s CIDR value.\n\n\n\n\n\nResourceAwsEc2InstanceKeyName (list) --The key name associated with the instance.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceAwsEc2InstanceIamInstanceProfileArn (list) --The IAM profile ARN of the instance.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceAwsEc2InstanceVpcId (list) --The identifier of the VPC that the instance was launched in.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceAwsEc2InstanceSubnetId (list) --The identifier of the subnet that the instance was launched in.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceAwsEc2InstanceLaunchedAt (list) --The date and time the instance was launched.\n\n(dict) --A date filter for querying findings.\n\nStart (string) --A start date for the date filter.\n\nEnd (string) --An end date for the date filter.\n\nDateRange (dict) --A date range for the date filter.\n\nValue (integer) --A date range value for the date filter.\n\nUnit (string) --A date range unit for the date filter.\n\n\n\n\n\n\n\nResourceAwsS3BucketOwnerId (list) --The canonical user ID of the owner of the S3 bucket.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceAwsS3BucketOwnerName (list) --The display name of the owner of the S3 bucket.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceAwsIamAccessKeyUserName (list) --The user associated with the IAM access key related to a finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceAwsIamAccessKeyStatus (list) --The status of the IAM access key related to a finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceAwsIamAccessKeyCreatedAt (list) --The creation date/time of the IAM access key related to a finding.\n\n(dict) --A date filter for querying findings.\n\nStart (string) --A start date for the date filter.\n\nEnd (string) --An end date for the date filter.\n\nDateRange (dict) --A date range for the date filter.\n\nValue (integer) --A date range value for the date filter.\n\nUnit (string) --A date range unit for the date filter.\n\n\n\n\n\n\n\nResourceContainerName (list) --The name of the container related to a finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceContainerImageId (list) --The identifier of the image related to a finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceContainerImageName (list) --The name of the image related to a finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceContainerLaunchedAt (list) --The date/time that the container was started.\n\n(dict) --A date filter for querying findings.\n\nStart (string) --A start date for the date filter.\n\nEnd (string) --An end date for the date filter.\n\nDateRange (dict) --A date range for the date filter.\n\nValue (integer) --A date range value for the date filter.\n\nUnit (string) --A date range unit for the date filter.\n\n\n\n\n\n\n\nResourceDetailsOther (list) --The details of a resource that doesn\'t have a specific subfield for the resource type defined.\n\n(dict) --The map filter for querying findings.\n\nKey (string) --The key of the map filter.\n\nValue (string) --The value for the key in the map filter.\n\nComparison (string) --The condition to apply to a key value when querying for findings with a map filter.\n\n\n\n\n\nComplianceStatus (list) --Exclusive to findings that are generated as the result of a check run against a specific rule in a supported standard, such as CIS AWS Foundations. Contains security standard-related finding details.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nVerificationState (list) --The veracity of a finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nWorkflowState (list) --The workflow state of a finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nWorkflowStatus (list) --The status of the investigation into a finding. Allowed values are the following.\n\nNEW - The initial state of a finding, before it is reviewed.\nNOTIFIED - Indicates that the resource owner has been notified about the security issue. Used when the initial reviewer is not the resource owner, and needs intervention from the resource owner.\nSUPPRESSED - The finding will not be reviewed again and will not be acted upon.\nRESOLVED - The finding was reviewed and remediated and is now considered resolved.\n\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nRecordState (list) --The updated record state for the finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nRelatedFindingsProductArn (list) --The ARN of the solution that generated a related finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nRelatedFindingsId (list) --The solution-generated identifier for a related finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nNoteText (list) --The text of a note.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nNoteUpdatedAt (list) --The timestamp of when the note was updated.\n\n(dict) --A date filter for querying findings.\n\nStart (string) --A start date for the date filter.\n\nEnd (string) --An end date for the date filter.\n\nDateRange (dict) --A date range for the date filter.\n\nValue (integer) --A date range value for the date filter.\n\nUnit (string) --A date range unit for the date filter.\n\n\n\n\n\n\n\nNoteUpdatedBy (list) --The principal that created a note.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nKeyword (list) --A keyword for a finding.\n\n(dict) --A keyword filter for querying findings.\n\nValue (string) --A value for the keyword.\n\n\n\n\n\n\n

    :type SortCriteria: list
    :param SortCriteria: The finding attributes used to sort the list of returned findings.\n\n(dict) --A collection of finding attributes used to sort findings.\n\nField (string) --The finding attribute used to sort findings.\n\nSortOrder (string) --The order used to sort findings.\n\n\n\n\n

    :type NextToken: string
    :param NextToken: The token that is required for pagination. On your first call to the GetFindings operation, set the value of this parameter to NULL .\nFor subsequent calls to the operation, to continue listing data, set the value of this parameter to the value returned from the previous response.\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of findings to return.

    :rtype: dict

ReturnsResponse Syntax
{
    'Findings': [
        {
            'SchemaVersion': 'string',
            'Id': 'string',
            'ProductArn': 'string',
            'GeneratorId': 'string',
            'AwsAccountId': 'string',
            'Types': [
                'string',
            ],
            'FirstObservedAt': 'string',
            'LastObservedAt': 'string',
            'CreatedAt': 'string',
            'UpdatedAt': 'string',
            'Severity': {
                'Product': 123.0,
                'Label': 'INFORMATIONAL'|'LOW'|'MEDIUM'|'HIGH'|'CRITICAL',
                'Normalized': 123,
                'Original': 'string'
            },
            'Confidence': 123,
            'Criticality': 123,
            'Title': 'string',
            'Description': 'string',
            'Remediation': {
                'Recommendation': {
                    'Text': 'string',
                    'Url': 'string'
                }
            },
            'SourceUrl': 'string',
            'ProductFields': {
                'string': 'string'
            },
            'UserDefinedFields': {
                'string': 'string'
            },
            'Malware': [
                {
                    'Name': 'string',
                    'Type': 'ADWARE'|'BLENDED_THREAT'|'BOTNET_AGENT'|'COIN_MINER'|'EXPLOIT_KIT'|'KEYLOGGER'|'MACRO'|'POTENTIALLY_UNWANTED'|'SPYWARE'|'RANSOMWARE'|'REMOTE_ACCESS'|'ROOTKIT'|'TROJAN'|'VIRUS'|'WORM',
                    'Path': 'string',
                    'State': 'OBSERVED'|'REMOVAL_FAILED'|'REMOVED'
                },
            ],
            'Network': {
                'Direction': 'IN'|'OUT',
                'Protocol': 'string',
                'SourceIpV4': 'string',
                'SourceIpV6': 'string',
                'SourcePort': 123,
                'SourceDomain': 'string',
                'SourceMac': 'string',
                'DestinationIpV4': 'string',
                'DestinationIpV6': 'string',
                'DestinationPort': 123,
                'DestinationDomain': 'string'
            },
            'Process': {
                'Name': 'string',
                'Path': 'string',
                'Pid': 123,
                'ParentPid': 123,
                'LaunchedAt': 'string',
                'TerminatedAt': 'string'
            },
            'ThreatIntelIndicators': [
                {
                    'Type': 'DOMAIN'|'EMAIL_ADDRESS'|'HASH_MD5'|'HASH_SHA1'|'HASH_SHA256'|'HASH_SHA512'|'IPV4_ADDRESS'|'IPV6_ADDRESS'|'MUTEX'|'PROCESS'|'URL',
                    'Value': 'string',
                    'Category': 'BACKDOOR'|'CARD_STEALER'|'COMMAND_AND_CONTROL'|'DROP_SITE'|'EXPLOIT_SITE'|'KEYLOGGER',
                    'LastObservedAt': 'string',
                    'Source': 'string',
                    'SourceUrl': 'string'
                },
            ],
            'Resources': [
                {
                    'Type': 'string',
                    'Id': 'string',
                    'Partition': 'aws'|'aws-cn'|'aws-us-gov',
                    'Region': 'string',
                    'Tags': {
                        'string': 'string'
                    },
                    'Details': {
                        'AwsCodeBuildProject': {
                            'EncryptionKey': 'string',
                            'Environment': {
                                'Certificate': 'string',
                                'ImagePullCredentialsType': 'string',
                                'RegistryCredential': {
                                    'Credential': 'string',
                                    'CredentialProvider': 'string'
                                },
                                'Type': 'string'
                            },
                            'Name': 'string',
                            'Source': {
                                'Type': 'string',
                                'Location': 'string',
                                'GitCloneDepth': 123,
                                'InsecureSsl': True|False
                            },
                            'ServiceRole': 'string',
                            'VpcConfig': {
                                'VpcId': 'string',
                                'Subnets': [
                                    'string',
                                ],
                                'SecurityGroupIds': [
                                    'string',
                                ]
                            }
                        },
                        'AwsCloudFrontDistribution': {
                            'DomainName': 'string',
                            'ETag': 'string',
                            'LastModifiedTime': 'string',
                            'Logging': {
                                'Bucket': 'string',
                                'Enabled': True|False,
                                'IncludeCookies': True|False,
                                'Prefix': 'string'
                            },
                            'Origins': {
                                'Items': [
                                    {
                                        'DomainName': 'string',
                                        'Id': 'string',
                                        'OriginPath': 'string'
                                    },
                                ]
                            },
                            'Status': 'string',
                            'WebAclId': 'string'
                        },
                        'AwsEc2Instance': {
                            'Type': 'string',
                            'ImageId': 'string',
                            'IpV4Addresses': [
                                'string',
                            ],
                            'IpV6Addresses': [
                                'string',
                            ],
                            'KeyName': 'string',
                            'IamInstanceProfileArn': 'string',
                            'VpcId': 'string',
                            'SubnetId': 'string',
                            'LaunchedAt': 'string'
                        },
                        'AwsEc2NetworkInterface': {
                            'Attachment': {
                                'AttachTime': 'string',
                                'AttachmentId': 'string',
                                'DeleteOnTermination': True|False,
                                'DeviceIndex': 123,
                                'InstanceId': 'string',
                                'InstanceOwnerId': 'string',
                                'Status': 'string'
                            },
                            'NetworkInterfaceId': 'string',
                            'SecurityGroups': [
                                {
                                    'GroupName': 'string',
                                    'GroupId': 'string'
                                },
                            ],
                            'SourceDestCheck': True|False
                        },
                        'AwsEc2SecurityGroup': {
                            'GroupName': 'string',
                            'GroupId': 'string',
                            'OwnerId': 'string',
                            'VpcId': 'string',
                            'IpPermissions': [
                                {
                                    'IpProtocol': 'string',
                                    'FromPort': 123,
                                    'ToPort': 123,
                                    'UserIdGroupPairs': [
                                        {
                                            'GroupId': 'string',
                                            'GroupName': 'string',
                                            'PeeringStatus': 'string',
                                            'UserId': 'string',
                                            'VpcId': 'string',
                                            'VpcPeeringConnectionId': 'string'
                                        },
                                    ],
                                    'IpRanges': [
                                        {
                                            'CidrIp': 'string'
                                        },
                                    ],
                                    'Ipv6Ranges': [
                                        {
                                            'CidrIpv6': 'string'
                                        },
                                    ],
                                    'PrefixListIds': [
                                        {
                                            'PrefixListId': 'string'
                                        },
                                    ]
                                },
                            ],
                            'IpPermissionsEgress': [
                                {
                                    'IpProtocol': 'string',
                                    'FromPort': 123,
                                    'ToPort': 123,
                                    'UserIdGroupPairs': [
                                        {
                                            'GroupId': 'string',
                                            'GroupName': 'string',
                                            'PeeringStatus': 'string',
                                            'UserId': 'string',
                                            'VpcId': 'string',
                                            'VpcPeeringConnectionId': 'string'
                                        },
                                    ],
                                    'IpRanges': [
                                        {
                                            'CidrIp': 'string'
                                        },
                                    ],
                                    'Ipv6Ranges': [
                                        {
                                            'CidrIpv6': 'string'
                                        },
                                    ],
                                    'PrefixListIds': [
                                        {
                                            'PrefixListId': 'string'
                                        },
                                    ]
                                },
                            ]
                        },
                        'AwsElbv2LoadBalancer': {
                            'AvailabilityZones': [
                                {
                                    'ZoneName': 'string',
                                    'SubnetId': 'string'
                                },
                            ],
                            'CanonicalHostedZoneId': 'string',
                            'CreatedTime': 'string',
                            'DNSName': 'string',
                            'IpAddressType': 'string',
                            'Scheme': 'string',
                            'SecurityGroups': [
                                'string',
                            ],
                            'State': {
                                'Code': 'string',
                                'Reason': 'string'
                            },
                            'Type': 'string',
                            'VpcId': 'string'
                        },
                        'AwsElasticsearchDomain': {
                            'AccessPolicies': 'string',
                            'DomainEndpointOptions': {
                                'EnforceHTTPS': True|False,
                                'TLSSecurityPolicy': 'string'
                            },
                            'DomainId': 'string',
                            'DomainName': 'string',
                            'Endpoint': 'string',
                            'Endpoints': {
                                'string': 'string'
                            },
                            'ElasticsearchVersion': 'string',
                            'EncryptionAtRestOptions': {
                                'Enabled': True|False,
                                'KmsKeyId': 'string'
                            },
                            'NodeToNodeEncryptionOptions': {
                                'Enabled': True|False
                            },
                            'VPCOptions': {
                                'AvailabilityZones': [
                                    'string',
                                ],
                                'SecurityGroupIds': [
                                    'string',
                                ],
                                'SubnetIds': [
                                    'string',
                                ],
                                'VPCId': 'string'
                            }
                        },
                        'AwsS3Bucket': {
                            'OwnerId': 'string',
                            'OwnerName': 'string',
                            'CreatedAt': 'string',
                            'ServerSideEncryptionConfiguration': {
                                'Rules': [
                                    {
                                        'ApplyServerSideEncryptionByDefault': {
                                            'SSEAlgorithm': 'string',
                                            'KMSMasterKeyID': 'string'
                                        }
                                    },
                                ]
                            }
                        },
                        'AwsS3Object': {
                            'LastModified': 'string',
                            'ETag': 'string',
                            'VersionId': 'string',
                            'ContentType': 'string',
                            'ServerSideEncryption': 'string',
                            'SSEKMSKeyId': 'string'
                        },
                        'AwsIamAccessKey': {
                            'UserName': 'string',
                            'Status': 'Active'|'Inactive',
                            'CreatedAt': 'string',
                            'PrincipalId': 'string',
                            'PrincipalType': 'string',
                            'PrincipalName': 'string'
                        },
                        'AwsIamRole': {
                            'AssumeRolePolicyDocument': 'string',
                            'CreateDate': 'string',
                            'RoleId': 'string',
                            'RoleName': 'string',
                            'MaxSessionDuration': 123,
                            'Path': 'string'
                        },
                        'AwsKmsKey': {
                            'AWSAccountId': 'string',
                            'CreationDate': 123.0,
                            'KeyId': 'string',
                            'KeyManager': 'string',
                            'KeyState': 'string',
                            'Origin': 'string'
                        },
                        'AwsLambdaFunction': {
                            'Code': {
                                'S3Bucket': 'string',
                                'S3Key': 'string',
                                'S3ObjectVersion': 'string',
                                'ZipFile': 'string'
                            },
                            'CodeSha256': 'string',
                            'DeadLetterConfig': {
                                'TargetArn': 'string'
                            },
                            'Environment': {
                                'Variables': {
                                    'string': 'string'
                                },
                                'Error': {
                                    'ErrorCode': 'string',
                                    'Message': 'string'
                                }
                            },
                            'FunctionName': 'string',
                            'Handler': 'string',
                            'KmsKeyArn': 'string',
                            'LastModified': 'string',
                            'Layers': [
                                {
                                    'Arn': 'string',
                                    'CodeSize': 123
                                },
                            ],
                            'MasterArn': 'string',
                            'MemorySize': 123,
                            'RevisionId': 'string',
                            'Role': 'string',
                            'Runtime': 'string',
                            'Timeout': 123,
                            'TracingConfig': {
                                'Mode': 'string'
                            },
                            'VpcConfig': {
                                'SecurityGroupIds': [
                                    'string',
                                ],
                                'SubnetIds': [
                                    'string',
                                ],
                                'VpcId': 'string'
                            },
                            'Version': 'string'
                        },
                        'AwsLambdaLayerVersion': {
                            'Version': 123,
                            'CompatibleRuntimes': [
                                'string',
                            ],
                            'CreatedDate': 'string'
                        },
                        'AwsRdsDbInstance': {
                            'AssociatedRoles': [
                                {
                                    'RoleArn': 'string',
                                    'FeatureName': 'string',
                                    'Status': 'string'
                                },
                            ],
                            'CACertificateIdentifier': 'string',
                            'DBClusterIdentifier': 'string',
                            'DBInstanceIdentifier': 'string',
                            'DBInstanceClass': 'string',
                            'DbInstancePort': 123,
                            'DbiResourceId': 'string',
                            'DBName': 'string',
                            'DeletionProtection': True|False,
                            'Endpoint': {
                                'Address': 'string',
                                'Port': 123,
                                'HostedZoneId': 'string'
                            },
                            'Engine': 'string',
                            'EngineVersion': 'string',
                            'IAMDatabaseAuthenticationEnabled': True|False,
                            'InstanceCreateTime': 'string',
                            'KmsKeyId': 'string',
                            'PubliclyAccessible': True|False,
                            'StorageEncrypted': True|False,
                            'TdeCredentialArn': 'string',
                            'VpcSecurityGroups': [
                                {
                                    'VpcSecurityGroupId': 'string',
                                    'Status': 'string'
                                },
                            ]
                        },
                        'AwsSnsTopic': {
                            'KmsMasterKeyId': 'string',
                            'Subscription': [
                                {
                                    'Endpoint': 'string',
                                    'Protocol': 'string'
                                },
                            ],
                            'TopicName': 'string',
                            'Owner': 'string'
                        },
                        'AwsSqsQueue': {
                            'KmsDataKeyReusePeriodSeconds': 123,
                            'KmsMasterKeyId': 'string',
                            'QueueName': 'string',
                            'DeadLetterTargetArn': 'string'
                        },
                        'AwsWafWebAcl': {
                            'Name': 'string',
                            'DefaultAction': 'string',
                            'Rules': [
                                {
                                    'Action': {
                                        'Type': 'string'
                                    },
                                    'ExcludedRules': [
                                        {
                                            'RuleId': 'string'
                                        },
                                    ],
                                    'OverrideAction': {
                                        'Type': 'string'
                                    },
                                    'Priority': 123,
                                    'RuleId': 'string',
                                    'Type': 'string'
                                },
                            ],
                            'WebAclId': 'string'
                        },
                        'Container': {
                            'Name': 'string',
                            'ImageId': 'string',
                            'ImageName': 'string',
                            'LaunchedAt': 'string'
                        },
                        'Other': {
                            'string': 'string'
                        }
                    }
                },
            ],
            'Compliance': {
                'Status': 'PASSED'|'WARNING'|'FAILED'|'NOT_AVAILABLE',
                'RelatedRequirements': [
                    'string',
                ],
                'StatusReasons': [
                    {
                        'ReasonCode': 'string',
                        'Description': 'string'
                    },
                ]
            },
            'VerificationState': 'UNKNOWN'|'TRUE_POSITIVE'|'FALSE_POSITIVE'|'BENIGN_POSITIVE',
            'WorkflowState': 'NEW'|'ASSIGNED'|'IN_PROGRESS'|'DEFERRED'|'RESOLVED',
            'Workflow': {
                'Status': 'NEW'|'NOTIFIED'|'RESOLVED'|'SUPPRESSED'
            },
            'RecordState': 'ACTIVE'|'ARCHIVED',
            'RelatedFindings': [
                {
                    'ProductArn': 'string',
                    'Id': 'string'
                },
            ],
            'Note': {
                'Text': 'string',
                'UpdatedBy': 'string',
                'UpdatedAt': 'string'
            }
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Findings (list) --
The findings that matched the filters specified in the request.

(dict) --
Provides consistent format for the contents of the Security Hub-aggregated findings. AwsSecurityFinding format enables you to share findings between AWS security services and third-party solutions, and security standards checks.

Note
A finding is a potential security issue generated either by AWS services (Amazon GuardDuty, Amazon Inspector, and Amazon Macie) or by the integrated third-party solutions and standards checks.


SchemaVersion (string) --
The schema version that a finding is formatted for.

Id (string) --
The security findings provider-specific identifier for a finding.

ProductArn (string) --
The ARN generated by Security Hub that uniquely identifies a product that generates findings. This can be the ARN for a third-party product that is integrated with Security Hub, or the ARN for a custom integration.

GeneratorId (string) --
The identifier for the solution-specific component (a discrete unit of logic) that generated a finding. In various security-findings providers\' solutions, this generator can be called a rule, a check, a detector, a plugin, etc.

AwsAccountId (string) --
The AWS account ID that a finding is generated in.

Types (list) --
One or more finding types in the format of namespace/category/classifier that classify a finding.
Valid namespace values are: Software and Configuration Checks | TTPs | Effects | Unusual Behaviors | Sensitive Data Identifications

(string) --


FirstObservedAt (string) --
An ISO8601-formatted timestamp that indicates when the security-findings provider first observed the potential security issue that a finding captured.

LastObservedAt (string) --
An ISO8601-formatted timestamp that indicates when the security-findings provider most recently observed the potential security issue that a finding captured.

CreatedAt (string) --
An ISO8601-formatted timestamp that indicates when the security-findings provider created the potential security issue that a finding captured.

UpdatedAt (string) --
An ISO8601-formatted timestamp that indicates when the security-findings provider last updated the finding record.

Severity (dict) --
A finding\'s severity.

Product (float) --
Deprecated. This attribute is being deprecated. Instead of providing Product , provide Original .
The native severity as defined by the AWS service or integrated partner product that generated the finding.

Label (string) --
The severity value of the finding. The allowed values are the following.

INFORMATIONAL - No issue was found.
LOW - The issue does not require action on its own.
MEDIUM - The issue must be addressed but not urgently.
HIGH - The issue must be addressed as a priority.
CRITICAL - The issue must be remediated immediately to avoid it escalating.


Normalized (integer) --
Deprecated. This attribute is being deprecated. Instead of providing Normalized , provide Label .
If you provide Normalized and do not provide Label , Label is set automatically as follows.

0 - INFORMATIONAL
1\xe2\x80\x9339 - LOW
40\xe2\x80\x9369 - MEDIUM
70\xe2\x80\x9389 - HIGH
90\xe2\x80\x93100 - CRITICAL


Original (string) --
The native severity from the finding product that generated the finding.



Confidence (integer) --
A finding\'s confidence. Confidence is defined as the likelihood that a finding accurately identifies the behavior or issue that it was intended to identify.
Confidence is scored on a 0-100 basis using a ratio scale, where 0 means zero percent confidence and 100 means 100 percent confidence.

Criticality (integer) --
The level of importance assigned to the resources associated with the finding.
A score of 0 means that the underlying resources have no criticality, and a score of 100 is reserved for the most critical resources.

Title (string) --
A finding\'s title.

Note
In this release, Title is a required property.


Description (string) --
A finding\'s description.

Note
In this release, Description is a required property.


Remediation (dict) --
A data type that describes the remediation options for a finding.

Recommendation (dict) --
A recommendation on the steps to take to remediate the issue identified by a finding.

Text (string) --
Describes the recommended steps to take to remediate an issue identified in a finding.

Url (string) --
A URL to a page or site that contains information about how to remediate a finding.





SourceUrl (string) --
A URL that links to a page about the current finding in the security-findings provider\'s solution.

ProductFields (dict) --
A data type where security-findings providers can include additional solution-specific details that aren\'t part of the defined AwsSecurityFinding format.

(string) --
(string) --




UserDefinedFields (dict) --
A list of name/value string pairs associated with the finding. These are custom, user-defined fields added to a finding.

(string) --
(string) --




Malware (list) --
A list of malware related to a finding.

(dict) --
A list of malware related to a finding.

Name (string) --
The name of the malware that was observed.

Type (string) --
The type of the malware that was observed.

Path (string) --
The file system path of the malware that was observed.

State (string) --
The state of the malware that was observed.





Network (dict) --
The details of network-related information about a finding.

Direction (string) --
The direction of network traffic associated with a finding.

Protocol (string) --
The protocol of network-related information about a finding.

SourceIpV4 (string) --
The source IPv4 address of network-related information about a finding.

SourceIpV6 (string) --
The source IPv6 address of network-related information about a finding.

SourcePort (integer) --
The source port of network-related information about a finding.

SourceDomain (string) --
The source domain of network-related information about a finding.

SourceMac (string) --
The source media access control (MAC) address of network-related information about a finding.

DestinationIpV4 (string) --
The destination IPv4 address of network-related information about a finding.

DestinationIpV6 (string) --
The destination IPv6 address of network-related information about a finding.

DestinationPort (integer) --
The destination port of network-related information about a finding.

DestinationDomain (string) --
The destination domain of network-related information about a finding.



Process (dict) --
The details of process-related information about a finding.

Name (string) --
The name of the process.

Path (string) --
The path to the process executable.

Pid (integer) --
The process ID.

ParentPid (integer) --
The parent process ID.

LaunchedAt (string) --
The date/time that the process was launched.

TerminatedAt (string) --
The date and time when the process was terminated.



ThreatIntelIndicators (list) --
Threat intelligence details related to a finding.

(dict) --
Details about the threat intelligence related to a finding.

Type (string) --
The type of threat intelligence indicator.

Value (string) --
The value of a threat intelligence indicator.

Category (string) --
The category of a threat intelligence indicator.

LastObservedAt (string) --
The date and time when the most recent instance of a threat intelligence indicator was observed.

Source (string) --
The source of the threat intelligence indicator.

SourceUrl (string) --
The URL to the page or site where you can get more information about the threat intelligence indicator.





Resources (list) --
A set of resource data types that describe the resources that the finding refers to.

(dict) --
A resource related to a finding.

Type (string) --
The type of the resource that details are provided for. If possible, set Type to one of the supported resource types. For example, if the resource is an EC2 instance, then set Type to AwsEc2Instance .
If the resource does not match any of the provided types, then set Type to Other .

Id (string) --
The canonical identifier for the given resource type.

Partition (string) --
The canonical AWS partition name that the Region is assigned to.

Region (string) --
The canonical AWS external Region name where this resource is located.

Tags (dict) --
A list of AWS tags associated with a resource at the time the finding was processed.

(string) --
(string) --




Details (dict) --
Additional details about the resource related to a finding.

AwsCodeBuildProject (dict) --
Details for an AWS CodeBuild project.

EncryptionKey (string) --
The AWS Key Management Service (AWS KMS) customer master key (CMK) used to encrypt the build output artifacts.
You can specify either the Amazon Resource Name (ARN) of the CMK or, if available, the CMK alias (using the format alias/alias-name).

Environment (dict) --
Information about the build environment for this build project.

Certificate (string) --
The certificate to use with this build project.

ImagePullCredentialsType (string) --
The type of credentials AWS CodeBuild uses to pull images in your build.
Valid values:

CODEBUILD specifies that AWS CodeBuild uses its own credentials. This requires that you modify your ECR repository policy to trust the AWS CodeBuild service principal.
SERVICE_ROLE specifies that AWS CodeBuild uses your build project\'s service role.

When you use a cross-account or private registry image, you must use SERVICE_ROLE credentials. When you use an AWS CodeBuild curated image, you must use CODEBUILD credentials.

RegistryCredential (dict) --
The credentials for access to a private registry.

Credential (string) --
The Amazon Resource Name (ARN) or name of credentials created using AWS Secrets Manager.

Note
The credential can use the name of the credentials only if they exist in your current AWS Region.


CredentialProvider (string) --
The service that created the credentials to access a private Docker registry.
The valid value,``SECRETS_MANAGER`` , is for AWS Secrets Manager.



Type (string) --
The type of build environment to use for related builds.
The environment type ARM_CONTAINER is available only in Regions US East (N. Virginia), US East (Ohio), US West (Oregon), Europe (Ireland), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Sydney), and Europe (Frankfurt).
The environment type LINUX_CONTAINER with compute type build.general1.2xlarge is available only in Regions US East (N. Virginia), US East (N. Virginia), US West (Oregon), Canada (Central), Europe (Ireland), Europe (London), Europe (Frankfurt), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), China (Beijing), and China (Ningxia).
The environment type LINUX_GPU_CONTAINER is available only in Regions US East (N. Virginia), US East (N. Virginia), US West (Oregon), Canada (Central), Europe (Ireland), Europe (London), Europe (Frankfurt), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), China (Beijing), and China (Ningxia).
Valid values: WINDOWS_CONTAINER | LINUX_CONTAINER | LINUX_GPU_CONTAINER | ARM_CONTAINER



Name (string) --
The name of the build project.

Source (dict) --
Information about the build input source code for this build project.

Type (string) --
The type of repository that contains the source code to be built. Valid values are:

BITBUCKET - The source code is in a Bitbucket repository.
CODECOMMIT - The source code is in an AWS CodeCommit repository.
CODEPIPELINE - The source code settings are specified in the source action of a pipeline in AWS CodePipeline.
GITHUB - The source code is in a GitHub repository.
GITHUB_ENTERPRISE - The source code is in a GitHub Enterprise repository.
NO_SOURCE - The project does not have input source code.
S3 - The source code is in an S3 input bucket.


Location (string) --
Information about the location of the source code to be built.
Valid values include:

For source code settings that are specified in the source action of a pipeline in AWS CodePipeline, location should not be specified. If it is specified, AWS CodePipeline ignores it. This is because AWS CodePipeline uses the settings in a pipeline\'s source action instead of this value.
For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository that contains the source code and the build spec file (for example, https://git-codecommit.region-ID.amazonaws.com/v1/repos/repo-name ).
For source code in an S3 input bucket, one of the following.
The path to the ZIP file that contains the source code (for example, bucket-name/path/to/object-name.zip ).
The path to the folder that contains the source code (for example, bucket-name/path/to/source-code/folder/ ).


For source code in a GitHub repository, the HTTPS clone URL to the repository that contains the source and the build spec file.
For source code in a Bitbucket repository, the HTTPS clone URL to the repository that contains the source and the build spec file.


GitCloneDepth (integer) --
Information about the Git clone depth for the build project.

InsecureSsl (boolean) --
Whether to ignore SSL warnings while connecting to the project source code.



ServiceRole (string) --
The ARN of the IAM role that enables AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account.

VpcConfig (dict) --
Information about the VPC configuration that AWS CodeBuild accesses.

VpcId (string) --
The ID of the VPC.

Subnets (list) --
A list of one or more subnet IDs in your Amazon VPC.

(string) --


SecurityGroupIds (list) --
A list of one or more security group IDs in your Amazon VPC.

(string) --






AwsCloudFrontDistribution (dict) --
Details about a CloudFront distribution.

DomainName (string) --
The domain name corresponding to the distribution.

ETag (string) --
The entity tag is a hash of the object.

LastModifiedTime (string) --
The date and time that the distribution was last modified.

Logging (dict) --
A complex type that controls whether access logs are written for the distribution.

Bucket (string) --
The Amazon S3 bucket to store the access logs in.

Enabled (boolean) --
With this field, you can enable or disable the selected distribution.

IncludeCookies (boolean) --
Specifies whether you want CloudFront to include cookies in access logs.

Prefix (string) --
An optional string that you want CloudFront to use as a prefix to the access log filenames for this distribution.



Origins (dict) --
A complex type that contains information about origins for this distribution.

Items (list) --
A complex type that contains origins or origin groups for this distribution.

(dict) --
A complex type that describes the Amazon S3 bucket, HTTP server (for example, a web server), Amazon Elemental MediaStore, or other server from which CloudFront gets your files.

DomainName (string) --
Amazon S3 origins: The DNS name of the Amazon S3 bucket from which you want CloudFront to get objects for this origin.

Id (string) --
A unique identifier for the origin or origin group.

OriginPath (string) --
An optional element that causes CloudFront to request your content from a directory in your Amazon S3 bucket or your custom origin.







Status (string) --
Indicates the current status of the distribution.

WebAclId (string) --
A unique identifier that specifies the AWS WAF web ACL, if any, to associate with this distribution.



AwsEc2Instance (dict) --
Details about an Amazon EC2 instance related to a finding.

Type (string) --
The instance type of the instance.

ImageId (string) --
The Amazon Machine Image (AMI) ID of the instance.

IpV4Addresses (list) --
The IPv4 addresses associated with the instance.

(string) --


IpV6Addresses (list) --
The IPv6 addresses associated with the instance.

(string) --


KeyName (string) --
The key name associated with the instance.

IamInstanceProfileArn (string) --
The IAM profile ARN of the instance.

VpcId (string) --
The identifier of the VPC that the instance was launched in.

SubnetId (string) --
The identifier of the subnet that the instance was launched in.

LaunchedAt (string) --
The date/time the instance was launched.



AwsEc2NetworkInterface (dict) --
Details for an Amazon EC2 network interface.

Attachment (dict) --
The network interface attachment.

AttachTime (string) --
The timestamp indicating when the attachment initiated.

AttachmentId (string) --
The identifier of the network interface attachment

DeleteOnTermination (boolean) --
Indicates whether the network interface is deleted when the instance is terminated.

DeviceIndex (integer) --
The device index of the network interface attachment on the instance.

InstanceId (string) --
The ID of the instance.

InstanceOwnerId (string) --
The AWS account ID of the owner of the instance.

Status (string) --
The attachment state.
Valid values: attaching | attached | detaching | detached



NetworkInterfaceId (string) --
The ID of the network interface.

SecurityGroups (list) --
Security groups for the network interface.

(dict) --
A security group associated with the network interface.

GroupName (string) --
The name of the security group.

GroupId (string) --
The ID of the security group.





SourceDestCheck (boolean) --
Indicates whether traffic to or from the instance is validated.



AwsEc2SecurityGroup (dict) --
Details for an EC2 security group.

GroupName (string) --
The name of the security group.

GroupId (string) --
The ID of the security group.

OwnerId (string) --
The AWS account ID of the owner of the security group.

VpcId (string) --
[VPC only] The ID of the VPC for the security group.

IpPermissions (list) --
The inbound rules associated with the security group.

(dict) --
An IP permission for an EC2 security group.

IpProtocol (string) --
The IP protocol name (tcp , udp , icmp , icmpv6 ) or number.
[VPC only] Use -1 to specify all protocols.
When authorizing security group rules, specifying -1 or a protocol number other than tcp , udp , icmp , or icmpv6 allows traffic on all ports, regardless of any port range you specify.
For tcp , udp , and icmp , you must specify a port range.
For icmpv6 , the port range is optional. If you omit the port range, traffic for all types and codes is allowed.

FromPort (integer) --
The start of the port range for the TCP and UDP protocols, or an ICMP/ICMPv6 type number.
A value of -1 indicates all ICMP/ICMPv6 types. If you specify all ICMP/ICMPv6 types, you must specify all codes.

ToPort (integer) --
The end of the port range for the TCP and UDP protocols, or an ICMP/ICMPv6 code.
A value of -1 indicates all ICMP/ICMPv6 codes. If you specify all ICMP/ICMPv6 types, you must specify all codes.

UserIdGroupPairs (list) --
The security group and AWS account ID pairs.

(dict) --
A relationship between a security group and a user.

GroupId (string) --
The ID of the security group.

GroupName (string) --
The name of the security group.

PeeringStatus (string) --
The status of a VPC peering connection, if applicable.

UserId (string) --
The ID of an AWS account.
For a referenced security group in another VPC, the account ID of the referenced security group is returned in the response. If the referenced security group is deleted, this value is not returned.
[EC2-Classic] Required when adding or removing rules that reference a security group in another AWS.

VpcId (string) --
The ID of the VPC for the referenced security group, if applicable.

VpcPeeringConnectionId (string) --
The ID of the VPC peering connection, if applicable.





IpRanges (list) --
The IPv4 ranges.

(dict) --
A range of IPv4 addresses.

CidrIp (string) --
The IPv4 CIDR range. You can specify either a CIDR range or a source security group, but not both. To specify a single IPv4 address, use the /32 prefix length.





Ipv6Ranges (list) --
The IPv6 ranges.

(dict) --
A range of IPv6 addresses.

CidrIpv6 (string) --
The IPv6 CIDR range. You can specify either a CIDR range or a source security group, but not both. To specify a single IPv6 address, use the /128 prefix length.





PrefixListIds (list) --
[VPC only] The prefix list IDs for an AWS service. With outbound rules, this is the AWS service to access through a VPC endpoint from instances associated with the security group.

(dict) --
A prefix list ID.

PrefixListId (string) --
The ID of the prefix.









IpPermissionsEgress (list) --
[VPC only] The outbound rules associated with the security group.

(dict) --
An IP permission for an EC2 security group.

IpProtocol (string) --
The IP protocol name (tcp , udp , icmp , icmpv6 ) or number.
[VPC only] Use -1 to specify all protocols.
When authorizing security group rules, specifying -1 or a protocol number other than tcp , udp , icmp , or icmpv6 allows traffic on all ports, regardless of any port range you specify.
For tcp , udp , and icmp , you must specify a port range.
For icmpv6 , the port range is optional. If you omit the port range, traffic for all types and codes is allowed.

FromPort (integer) --
The start of the port range for the TCP and UDP protocols, or an ICMP/ICMPv6 type number.
A value of -1 indicates all ICMP/ICMPv6 types. If you specify all ICMP/ICMPv6 types, you must specify all codes.

ToPort (integer) --
The end of the port range for the TCP and UDP protocols, or an ICMP/ICMPv6 code.
A value of -1 indicates all ICMP/ICMPv6 codes. If you specify all ICMP/ICMPv6 types, you must specify all codes.

UserIdGroupPairs (list) --
The security group and AWS account ID pairs.

(dict) --
A relationship between a security group and a user.

GroupId (string) --
The ID of the security group.

GroupName (string) --
The name of the security group.

PeeringStatus (string) --
The status of a VPC peering connection, if applicable.

UserId (string) --
The ID of an AWS account.
For a referenced security group in another VPC, the account ID of the referenced security group is returned in the response. If the referenced security group is deleted, this value is not returned.
[EC2-Classic] Required when adding or removing rules that reference a security group in another AWS.

VpcId (string) --
The ID of the VPC for the referenced security group, if applicable.

VpcPeeringConnectionId (string) --
The ID of the VPC peering connection, if applicable.





IpRanges (list) --
The IPv4 ranges.

(dict) --
A range of IPv4 addresses.

CidrIp (string) --
The IPv4 CIDR range. You can specify either a CIDR range or a source security group, but not both. To specify a single IPv4 address, use the /32 prefix length.





Ipv6Ranges (list) --
The IPv6 ranges.

(dict) --
A range of IPv6 addresses.

CidrIpv6 (string) --
The IPv6 CIDR range. You can specify either a CIDR range or a source security group, but not both. To specify a single IPv6 address, use the /128 prefix length.





PrefixListIds (list) --
[VPC only] The prefix list IDs for an AWS service. With outbound rules, this is the AWS service to access through a VPC endpoint from instances associated with the security group.

(dict) --
A prefix list ID.

PrefixListId (string) --
The ID of the prefix.











AwsElbv2LoadBalancer (dict) --
Details about a load balancer.

AvailabilityZones (list) --
The Availability Zones for the load balancer.

(dict) --
Information about an Availability Zone.

ZoneName (string) --
The name of the Availability Zone.

SubnetId (string) --
The ID of the subnet. You can specify one subnet per Availability Zone.





CanonicalHostedZoneId (string) --
The ID of the Amazon Route 53 hosted zone associated with the load balancer.

CreatedTime (string) --
The date and time the load balancer was created.

DNSName (string) --
The public DNS name of the load balancer.

IpAddressType (string) --
The type of IP addresses used by the subnets for your load balancer. The possible values are ipv4 (for IPv4 addresses) and dualstack (for IPv4 and IPv6 addresses).

Scheme (string) --
The nodes of an Internet-facing load balancer have public IP addresses.

SecurityGroups (list) --
The IDs of the security groups for the load balancer.

(string) --


State (dict) --
The state of the load balancer.

Code (string) --
The state code. The initial state of the load balancer is provisioning.
After the load balancer is fully set up and ready to route traffic, its state is active.
If the load balancer could not be set up, its state is failed.

Reason (string) --
A description of the state.



Type (string) --
The type of load balancer.

VpcId (string) --
The ID of the VPC for the load balancer.



AwsElasticsearchDomain (dict) --
Details for an Elasticsearch domain.

AccessPolicies (string) --
IAM policy document specifying the access policies for the new Amazon ES domain.

DomainEndpointOptions (dict) --
Additional options for the domain endpoint.

EnforceHTTPS (boolean) --
Whether to require that all traffic to the domain arrive over HTTPS.

TLSSecurityPolicy (string) --
The TLS security policy to apply to the HTTPS endpoint of the Elasticsearch domain.
Valid values:

Policy-Min-TLS-1-0-2019-07 , which supports TLSv1.0 and higher
Policy-Min-TLS-1-2-2019-07 , which only supports TLSv1.2




DomainId (string) --
Unique identifier for an Amazon ES domain.

DomainName (string) --
Name of an Amazon ES domain.
Domain names are unique across all domains owned by the same account within an AWS Region.
Domain names must start with a lowercase letter and must be between 3 and 28 characters.
Valid characters are a-z (lowercase only), 0-9, and \xe2\x80\x93 (hyphen).

Endpoint (string) --
Domain-specific endpoint used to submit index, search, and data upload requests to an Amazon ES domain.
The endpoint is a service URL.

Endpoints (dict) --
The key-value pair that exists if the Amazon ES domain uses VPC endpoints.

(string) --
(string) --




ElasticsearchVersion (string) --
Elasticsearch version.

EncryptionAtRestOptions (dict) --
Details about the configuration for encryption at rest.

Enabled (boolean) --
Whether encryption at rest is enabled.

KmsKeyId (string) --
The KMS key ID. Takes the form 1a2a3a4-1a2a-3a4a-5a6a-1a2a3a4a5a6a.



NodeToNodeEncryptionOptions (dict) --
Details about the configuration for node-to-node encryption.

Enabled (boolean) --
Whether node-to-node encryption is enabled.



VPCOptions (dict) --
Information that Amazon ES derives based on VPCOptions for the domain.

AvailabilityZones (list) --
The list of Availability Zones associated with the VPC subnets.

(string) --


SecurityGroupIds (list) --
The list of security group IDs associated with the VPC endpoints for the domain.

(string) --


SubnetIds (list) --
A list of subnet IDs associated with the VPC endpoints for the domain.

(string) --


VPCId (string) --
ID for the VPC.





AwsS3Bucket (dict) --
Details about an Amazon S3 bucket related to a finding.

OwnerId (string) --
The canonical user ID of the owner of the S3 bucket.

OwnerName (string) --
The display name of the owner of the S3 bucket.

CreatedAt (string) --
The date and time when the S3 bucket was created.

ServerSideEncryptionConfiguration (dict) --
The encryption rules that are applied to the S3 bucket.

Rules (list) --
The encryption rules that are applied to the S3 bucket.

(dict) --
An encryption rule to apply to the S3 bucket.

ApplyServerSideEncryptionByDefault (dict) --
Specifies the default server-side encryption to apply to new objects in the bucket. If a PUT object request doesn\'t specify any server-side encryption, this default encryption is applied.

SSEAlgorithm (string) --
Server-side encryption algorithm to use for the default encryption.

KMSMasterKeyID (string) --
AWS KMS customer master key (CMK) ID to use for the default encryption.











AwsS3Object (dict) --
Details about an Amazon S3 object related to a finding.

LastModified (string) --
The date and time when the object was last modified.

ETag (string) --
The opaque identifier assigned by a web server to a specific version of a resource found at a URL.

VersionId (string) --
The version of the object.

ContentType (string) --
A standard MIME type describing the format of the object data.

ServerSideEncryption (string) --
If the object is stored using server-side encryption, the value of the server-side encryption algorithm used when storing this object in Amazon S3.

SSEKMSKeyId (string) --
The identifier of the AWS Key Management Service (AWS KMS) symmetric customer managed customer master key (CMK) that was used for the object.



AwsIamAccessKey (dict) --
Details about an IAM access key related to a finding.

UserName (string) --
The user associated with the IAM access key related to a finding.
The UserName parameter has been replaced with the PrincipalName parameter because access keys can also be assigned to principals that are not IAM users.

Status (string) --
The status of the IAM access key related to a finding.

CreatedAt (string) --
The creation date/time of the IAM access key related to a finding.

PrincipalId (string) --
The ID of the principal associated with an access key.

PrincipalType (string) --
The type of principal associated with an access key.

PrincipalName (string) --
The name of the principal.



AwsIamRole (dict) --
Details about an IAM role.

AssumeRolePolicyDocument (string) --
The trust policy that grants permission to assume the role.

CreateDate (string) --
The date and time, in ISO 8601 date-time format, when the role was created.

RoleId (string) --
The stable and unique string identifying the role.

RoleName (string) --
The friendly name that identifies the role.

MaxSessionDuration (integer) --
The maximum session duration (in seconds) that you want to set for the specified role.

Path (string) --
The path to the role.



AwsKmsKey (dict) --
Details about a KMS key.

AWSAccountId (string) --
The twelve-digit account ID of the AWS account that owns the CMK.

CreationDate (float) --
The date and time when the CMK was created.

KeyId (string) --
The globally unique identifier for the CMK.

KeyManager (string) --
The manager of the CMK. CMKs in your AWS account are either customer managed or AWS managed.

KeyState (string) --
The state of the CMK.

Origin (string) --
The source of the CMK\'s key material.
When this value is AWS_KMS , AWS KMS created the key material.
When this value is EXTERNAL , the key material was imported from your existing key management infrastructure or the CMK lacks key material.
When this value is AWS_CLOUDHSM , the key material was created in the AWS CloudHSM cluster associated with a custom key store.



AwsLambdaFunction (dict) --
Details about a Lambda function.

Code (dict) --
An AwsLambdaFunctionCode object.

S3Bucket (string) --
An Amazon S3 bucket in the same AWS Region as your function. The bucket can be in a different AWS account.

S3Key (string) --
The Amazon S3 key of the deployment package.

S3ObjectVersion (string) --
For versioned objects, the version of the deployment package object to use.

ZipFile (string) --
The base64-encoded contents of the deployment package. AWS SDK and AWS CLI clients handle the encoding for you.



CodeSha256 (string) --
The SHA256 hash of the function\'s deployment package.

DeadLetterConfig (dict) --
The function\'s dead letter queue.

TargetArn (string) --
The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.



Environment (dict) --
The function\'s environment variables.

Variables (dict) --
Environment variable key-value pairs.

(string) --
(string) --




Error (dict) --
An AwsLambdaFunctionEnvironmentError object.

ErrorCode (string) --
The error code.

Message (string) --
The error message.





FunctionName (string) --
The name of the function.

Handler (string) --
The function that Lambda calls to begin executing your function.

KmsKeyArn (string) --
The KMS key that\'s used to encrypt the function\'s environment variables. This key is only returned if you\'ve configured a customer managed CMK.

LastModified (string) --
The date and time that the function was last updated, in ISO-8601 format (YYYY-MM-DDThh:mm:ss.sTZD).

Layers (list) --
The function\'s layers.

(dict) --
An AWS Lambda layer.

Arn (string) --
The Amazon Resource Name (ARN) of the function layer.

CodeSize (integer) --
The size of the layer archive in bytes.





MasterArn (string) --
For Lambda@Edge functions, the ARN of the master function.

MemorySize (integer) --
The memory that\'s allocated to the function.

RevisionId (string) --
The latest updated revision of the function or alias.

Role (string) --
The function\'s execution role.

Runtime (string) --
The runtime environment for the Lambda function.

Timeout (integer) --
The amount of time that Lambda allows a function to run before stopping it.

TracingConfig (dict) --
The function\'s AWS X-Ray tracing configuration.

Mode (string) --
The tracing mode.



VpcConfig (dict) --
The function\'s networking configuration.

SecurityGroupIds (list) --
A list of VPC security groups IDs.

(string) --


SubnetIds (list) --
A list of VPC subnet IDs.

(string) --


VpcId (string) --
The ID of the VPC.



Version (string) --
The version of the Lambda function.



AwsLambdaLayerVersion (dict) --
Details for a Lambda layer version.

Version (integer) --
The version number.

CompatibleRuntimes (list) --
The layer\'s compatible runtimes. Maximum number of five items.
Valid values: nodejs10.x | nodejs12.x | java8 | java11 | python2.7 | python3.6 | python3.7 | python3.8 | dotnetcore1.0 | dotnetcore2.1 | go1.x | ruby2.5 | provided

(string) --


CreatedDate (string) --
The date that the version was created, in ISO 8601 format. For example, 2018-11-27T15:10:45.123+0000.



AwsRdsDbInstance (dict) --
Details for an Amazon RDS database instance.

AssociatedRoles (list) --
The AWS Identity and Access Management (IAM) roles associated with the DB instance.

(dict) --
An AWS Identity and Access Management (IAM) role associated with the DB instance.

RoleArn (string) --
The Amazon Resource Name (ARN) of the IAM role that is associated with the DB instance.

FeatureName (string) --
The name of the feature associated with the IAM)role.

Status (string) --
Describes the state of the association between the IAM role and the DB instance. The Status property returns one of the following values:

ACTIVE - The IAM role ARN is associated with the DB instance and can be used to access other AWS services on your behalf.
PENDING - The IAM role ARN is being associated with the DB instance.
INVALID - The IAM role ARN is associated with the DB instance. But the DB instance is unable to assume the IAM role in order to access other AWS services on your behalf.






CACertificateIdentifier (string) --
The identifier of the CA certificate for this DB instance.

DBClusterIdentifier (string) --
If the DB instance is a member of a DB cluster, contains the name of the DB cluster that the DB instance is a member of.

DBInstanceIdentifier (string) --
Contains a user-supplied database identifier. This identifier is the unique key that identifies a DB instance.

DBInstanceClass (string) --
Contains the name of the compute and memory capacity class of the DB instance.

DbInstancePort (integer) --
Specifies the port that the DB instance listens on. If the DB instance is part of a DB cluster, this can be a different port than the DB cluster port.

DbiResourceId (string) --
The AWS Region-unique, immutable identifier for the DB instance. This identifier is found in AWS CloudTrail log entries whenever the AWS KMS key for the DB instance is accessed.

DBName (string) --
The meaning of this parameter differs according to the database engine you use.

MySQL, MariaDB, SQL Server, PostgreSQL

Contains the name of the initial database of this instance that was provided at create time, if one was specified when the DB instance was created. This same name is returned for the life of the DB instance.

Oracle

Contains the Oracle System ID (SID) of the created DB instance. Not shown when the returned parameters do not apply to an Oracle DB instance.

DeletionProtection (boolean) --
Indicates whether the DB instance has deletion protection enabled.
When deletion protection is enabled, the database cannot be deleted.

Endpoint (dict) --
Specifies the connection endpoint.

Address (string) --
Specifies the DNS address of the DB instance.

Port (integer) --
Specifies the port that the database engine is listening on.

HostedZoneId (string) --
Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.



Engine (string) --
Provides the name of the database engine to use for this DB instance.

EngineVersion (string) --
Indicates the database engine version.

IAMDatabaseAuthenticationEnabled (boolean) --
True if mapping of AWS Identity and Access Management (IAM) accounts to database accounts is enabled, and otherwise false.
IAM database authentication can be enabled for the following database engines.

For MySQL 5.6, minor version 5.6.34 or higher
For MySQL 5.7, minor version 5.7.16 or higher
Aurora 5.6 or higher


InstanceCreateTime (string) --
Provides the date and time the DB instance was created.

KmsKeyId (string) --
If StorageEncrypted is true, the AWS KMS key identifier for the encrypted DB instance.

PubliclyAccessible (boolean) --
Specifies the accessibility options for the DB instance.
A value of true specifies an Internet-facing instance with a publicly resolvable DNS name, which resolves to a public IP address.
A value of false specifies an internal instance with a DNS name that resolves to a private IP address.

StorageEncrypted (boolean) --
Specifies whether the DB instance is encrypted.

TdeCredentialArn (string) --
The ARN from the key store with which the instance is associated for TDE encryption.

VpcSecurityGroups (list) --
A list of VPC security groups that the DB instance belongs to.

(dict) --
A VPC security groups that the DB instance belongs to.

VpcSecurityGroupId (string) --
The name of the VPC security group.

Status (string) --
The status of the VPC security group.







AwsSnsTopic (dict) --
Details about an SNS topic.

KmsMasterKeyId (string) --
The ID of an AWS managed customer master key (CMK) for Amazon SNS or a custom CMK.

Subscription (list) --
Subscription is an embedded property that describes the subscription endpoints of an Amazon SNS topic.

(dict) --
A wrapper type for the attributes of an Amazon SNS subscription.

Endpoint (string) --
The subscription\'s endpoint (format depends on the protocol).

Protocol (string) --
The subscription\'s protocol.





TopicName (string) --
The name of the topic.

Owner (string) --
The subscription\'s owner.



AwsSqsQueue (dict) --
Details about an SQS queue.

KmsDataKeyReusePeriodSeconds (integer) --
The length of time, in seconds, for which Amazon SQS can reuse a data key to encrypt or decrypt messages before calling AWS KMS again.

KmsMasterKeyId (string) --
The ID of an AWS managed customer master key (CMK) for Amazon SQS or a custom CMK.

QueueName (string) --
The name of the new queue.

DeadLetterTargetArn (string) --
The Amazon Resource Name (ARN) of the dead-letter queue to which Amazon SQS moves messages after the value of maxReceiveCount is exceeded.



AwsWafWebAcl (dict) --
Details for a WAF WebACL.

Name (string) --
A friendly name or description of the WebACL. You can\'t change the name of a WebACL after you create it.

DefaultAction (string) --
The action to perform if none of the rules contained in the WebACL match.

Rules (list) --
An array that contains the action for each rule in a WebACL, the priority of the rule, and the ID of the rule.

(dict) --
Details for a rule in a WAF WebACL.

Action (dict) --
Specifies the action that CloudFront or AWS WAF takes when a web request matches the conditions in the rule.

Type (string) --
Specifies how you want AWS WAF to respond to requests that match the settings in a rule.
Valid settings include the following:

ALLOW - AWS WAF allows requests
BLOCK - AWS WAF blocks requests
COUNT - AWS WAF increments a counter of the requests that match all of the conditions in the rule. AWS WAF then continues to inspect the web request based on the remaining rules in the web ACL. You can\'t specify COUNT for the default action for a WebACL.




ExcludedRules (list) --
Rules to exclude from a rule group.

(dict) --
Details about a rule to exclude from a rule group.

RuleId (string) --
The unique identifier for the rule to exclude from the rule group.





OverrideAction (dict) --
Use the OverrideAction to test your RuleGroup.
Any rule in a RuleGroup can potentially block a request. If you set the OverrideAction to None , the RuleGroup blocks a request if any individual rule in the RuleGroup matches the request and is configured to block that request.
However, if you first want to test the RuleGroup, set the OverrideAction to Count . The RuleGroup then overrides any block action specified by individual rules contained within the group. Instead of blocking matching requests, those requests are counted.

ActivatedRule |OverrideAction applies only when updating or adding a RuleGroup to a WebACL. In this case you do not use ActivatedRule |Action . For all other update requests, ActivatedRule |Action is used instead of ActivatedRule |OverrideAction .


Type (string) --

COUNT overrides the action specified by the individual rule within a RuleGroup .

If set to NONE , the rule\'s action takes place.



Priority (integer) --
Specifies the order in which the rules in a WebACL are evaluated. Rules with a lower value for Priority are evaluated before rules with a higher value. The value must be a unique integer. If you add multiple rules to a WebACL, the values do not need to be consecutive.

RuleId (string) --
The identifier for a rule.

Type (string) --
The rule type.
Valid values: REGULAR | RATE_BASED | GROUP
The default is REGULAR .





WebAclId (string) --
A unique identifier for a WebACL.



Container (dict) --
Details about a container resource related to a finding.

Name (string) --
The name of the container related to a finding.

ImageId (string) --
The identifier of the image related to a finding.

ImageName (string) --
The name of the image related to a finding.

LaunchedAt (string) --
The date and time when the container started.



Other (dict) --
Details about a resource that are not available in a type-specific details object. Use the Other object in the following cases.

The type-specific object does not contain all of the fields that you want to populate. In this case, first use the type-specific object to populate those fields. Use the Other object to populate the fields that are missing from the type-specific object.
The resource type does not have a corresponding object. This includes resources for which the type is Other .


(string) --
(string) --










Compliance (dict) --
This data type is exclusive to findings that are generated as the result of a check run against a specific rule in a supported security standard, such as CIS AWS Foundations. Contains security standard-related finding details.

Status (string) --
The result of a standards check.
The valid values for Status are as follows.


PASSED - Standards check passed for all evaluated resources.
WARNING - Some information is missing or this check is not supported for your configuration.
FAILED - Standards check failed for at least one evaluated resource.
NOT_AVAILABLE - Check could not be performed due to a service outage, API error, or because the result of the AWS Config evaluation was NOT_APPLICABLE . If the AWS Config evaluation result was NOT_APPLICABLE , then after 3 days, Security Hub automatically archives the finding.




RelatedRequirements (list) --
For a control, the industry or regulatory framework requirements that are related to the control. The check for that control is aligned with these requirements.

(string) --


StatusReasons (list) --
For findings generated from controls, a list of reasons behind the value of Status . For the list of status reason codes and their meanings, see Standards-related information in the ASFF in the AWS Security Hub User Guide .

(dict) --
Provides additional context for the value of Compliance.Status .

ReasonCode (string) --
A code that represents a reason for the control status. For the list of status reason codes and their meanings, see Standards-related information in the ASFF in the AWS Security Hub User Guide .

Description (string) --
The corresponding description for the status reason code.







VerificationState (string) --
Indicates the veracity of a finding.

WorkflowState (string) --
The workflow state of a finding.

Workflow (dict) --
Provides information about the status of the investigation into a finding.

Status (string) --
The status of the investigation into the finding. The allowed values are the following.

NEW - The initial state of a finding, before it is reviewed.
NOTIFIED - Indicates that you notified the resource owner about the security issue. Used when the initial reviewer is not the resource owner, and needs intervention from the resource owner.
SUPPRESSED - The finding will not be reviewed again and will not be acted upon.
RESOLVED - The finding was reviewed and remediated and is now considered resolved.




RecordState (string) --
The record state of a finding.

RelatedFindings (list) --
A list of related findings.

(dict) --
Details about a related finding.

ProductArn (string) --
The ARN of the product that generated a related finding.

Id (string) --
The product-generated identifier for a related finding.





Note (dict) --
A user-defined note added to a finding.

Text (string) --
The text of a note.

UpdatedBy (string) --
The principal that created a note.

UpdatedAt (string) --
The timestamp of when the note was updated.







NextToken (string) --
The pagination token to use to request the next page of results.







Exceptions

SecurityHub.Client.exceptions.InternalException
SecurityHub.Client.exceptions.InvalidInputException
SecurityHub.Client.exceptions.InvalidAccessException
SecurityHub.Client.exceptions.LimitExceededException


    :return: {
        'Findings': [
            {
                'SchemaVersion': 'string',
                'Id': 'string',
                'ProductArn': 'string',
                'GeneratorId': 'string',
                'AwsAccountId': 'string',
                'Types': [
                    'string',
                ],
                'FirstObservedAt': 'string',
                'LastObservedAt': 'string',
                'CreatedAt': 'string',
                'UpdatedAt': 'string',
                'Severity': {
                    'Product': 123.0,
                    'Label': 'INFORMATIONAL'|'LOW'|'MEDIUM'|'HIGH'|'CRITICAL',
                    'Normalized': 123,
                    'Original': 'string'
                },
                'Confidence': 123,
                'Criticality': 123,
                'Title': 'string',
                'Description': 'string',
                'Remediation': {
                    'Recommendation': {
                        'Text': 'string',
                        'Url': 'string'
                    }
                },
                'SourceUrl': 'string',
                'ProductFields': {
                    'string': 'string'
                },
                'UserDefinedFields': {
                    'string': 'string'
                },
                'Malware': [
                    {
                        'Name': 'string',
                        'Type': 'ADWARE'|'BLENDED_THREAT'|'BOTNET_AGENT'|'COIN_MINER'|'EXPLOIT_KIT'|'KEYLOGGER'|'MACRO'|'POTENTIALLY_UNWANTED'|'SPYWARE'|'RANSOMWARE'|'REMOTE_ACCESS'|'ROOTKIT'|'TROJAN'|'VIRUS'|'WORM',
                        'Path': 'string',
                        'State': 'OBSERVED'|'REMOVAL_FAILED'|'REMOVED'
                    },
                ],
                'Network': {
                    'Direction': 'IN'|'OUT',
                    'Protocol': 'string',
                    'SourceIpV4': 'string',
                    'SourceIpV6': 'string',
                    'SourcePort': 123,
                    'SourceDomain': 'string',
                    'SourceMac': 'string',
                    'DestinationIpV4': 'string',
                    'DestinationIpV6': 'string',
                    'DestinationPort': 123,
                    'DestinationDomain': 'string'
                },
                'Process': {
                    'Name': 'string',
                    'Path': 'string',
                    'Pid': 123,
                    'ParentPid': 123,
                    'LaunchedAt': 'string',
                    'TerminatedAt': 'string'
                },
                'ThreatIntelIndicators': [
                    {
                        'Type': 'DOMAIN'|'EMAIL_ADDRESS'|'HASH_MD5'|'HASH_SHA1'|'HASH_SHA256'|'HASH_SHA512'|'IPV4_ADDRESS'|'IPV6_ADDRESS'|'MUTEX'|'PROCESS'|'URL',
                        'Value': 'string',
                        'Category': 'BACKDOOR'|'CARD_STEALER'|'COMMAND_AND_CONTROL'|'DROP_SITE'|'EXPLOIT_SITE'|'KEYLOGGER',
                        'LastObservedAt': 'string',
                        'Source': 'string',
                        'SourceUrl': 'string'
                    },
                ],
                'Resources': [
                    {
                        'Type': 'string',
                        'Id': 'string',
                        'Partition': 'aws'|'aws-cn'|'aws-us-gov',
                        'Region': 'string',
                        'Tags': {
                            'string': 'string'
                        },
                        'Details': {
                            'AwsCodeBuildProject': {
                                'EncryptionKey': 'string',
                                'Environment': {
                                    'Certificate': 'string',
                                    'ImagePullCredentialsType': 'string',
                                    'RegistryCredential': {
                                        'Credential': 'string',
                                        'CredentialProvider': 'string'
                                    },
                                    'Type': 'string'
                                },
                                'Name': 'string',
                                'Source': {
                                    'Type': 'string',
                                    'Location': 'string',
                                    'GitCloneDepth': 123,
                                    'InsecureSsl': True|False
                                },
                                'ServiceRole': 'string',
                                'VpcConfig': {
                                    'VpcId': 'string',
                                    'Subnets': [
                                        'string',
                                    ],
                                    'SecurityGroupIds': [
                                        'string',
                                    ]
                                }
                            },
                            'AwsCloudFrontDistribution': {
                                'DomainName': 'string',
                                'ETag': 'string',
                                'LastModifiedTime': 'string',
                                'Logging': {
                                    'Bucket': 'string',
                                    'Enabled': True|False,
                                    'IncludeCookies': True|False,
                                    'Prefix': 'string'
                                },
                                'Origins': {
                                    'Items': [
                                        {
                                            'DomainName': 'string',
                                            'Id': 'string',
                                            'OriginPath': 'string'
                                        },
                                    ]
                                },
                                'Status': 'string',
                                'WebAclId': 'string'
                            },
                            'AwsEc2Instance': {
                                'Type': 'string',
                                'ImageId': 'string',
                                'IpV4Addresses': [
                                    'string',
                                ],
                                'IpV6Addresses': [
                                    'string',
                                ],
                                'KeyName': 'string',
                                'IamInstanceProfileArn': 'string',
                                'VpcId': 'string',
                                'SubnetId': 'string',
                                'LaunchedAt': 'string'
                            },
                            'AwsEc2NetworkInterface': {
                                'Attachment': {
                                    'AttachTime': 'string',
                                    'AttachmentId': 'string',
                                    'DeleteOnTermination': True|False,
                                    'DeviceIndex': 123,
                                    'InstanceId': 'string',
                                    'InstanceOwnerId': 'string',
                                    'Status': 'string'
                                },
                                'NetworkInterfaceId': 'string',
                                'SecurityGroups': [
                                    {
                                        'GroupName': 'string',
                                        'GroupId': 'string'
                                    },
                                ],
                                'SourceDestCheck': True|False
                            },
                            'AwsEc2SecurityGroup': {
                                'GroupName': 'string',
                                'GroupId': 'string',
                                'OwnerId': 'string',
                                'VpcId': 'string',
                                'IpPermissions': [
                                    {
                                        'IpProtocol': 'string',
                                        'FromPort': 123,
                                        'ToPort': 123,
                                        'UserIdGroupPairs': [
                                            {
                                                'GroupId': 'string',
                                                'GroupName': 'string',
                                                'PeeringStatus': 'string',
                                                'UserId': 'string',
                                                'VpcId': 'string',
                                                'VpcPeeringConnectionId': 'string'
                                            },
                                        ],
                                        'IpRanges': [
                                            {
                                                'CidrIp': 'string'
                                            },
                                        ],
                                        'Ipv6Ranges': [
                                            {
                                                'CidrIpv6': 'string'
                                            },
                                        ],
                                        'PrefixListIds': [
                                            {
                                                'PrefixListId': 'string'
                                            },
                                        ]
                                    },
                                ],
                                'IpPermissionsEgress': [
                                    {
                                        'IpProtocol': 'string',
                                        'FromPort': 123,
                                        'ToPort': 123,
                                        'UserIdGroupPairs': [
                                            {
                                                'GroupId': 'string',
                                                'GroupName': 'string',
                                                'PeeringStatus': 'string',
                                                'UserId': 'string',
                                                'VpcId': 'string',
                                                'VpcPeeringConnectionId': 'string'
                                            },
                                        ],
                                        'IpRanges': [
                                            {
                                                'CidrIp': 'string'
                                            },
                                        ],
                                        'Ipv6Ranges': [
                                            {
                                                'CidrIpv6': 'string'
                                            },
                                        ],
                                        'PrefixListIds': [
                                            {
                                                'PrefixListId': 'string'
                                            },
                                        ]
                                    },
                                ]
                            },
                            'AwsElbv2LoadBalancer': {
                                'AvailabilityZones': [
                                    {
                                        'ZoneName': 'string',
                                        'SubnetId': 'string'
                                    },
                                ],
                                'CanonicalHostedZoneId': 'string',
                                'CreatedTime': 'string',
                                'DNSName': 'string',
                                'IpAddressType': 'string',
                                'Scheme': 'string',
                                'SecurityGroups': [
                                    'string',
                                ],
                                'State': {
                                    'Code': 'string',
                                    'Reason': 'string'
                                },
                                'Type': 'string',
                                'VpcId': 'string'
                            },
                            'AwsElasticsearchDomain': {
                                'AccessPolicies': 'string',
                                'DomainEndpointOptions': {
                                    'EnforceHTTPS': True|False,
                                    'TLSSecurityPolicy': 'string'
                                },
                                'DomainId': 'string',
                                'DomainName': 'string',
                                'Endpoint': 'string',
                                'Endpoints': {
                                    'string': 'string'
                                },
                                'ElasticsearchVersion': 'string',
                                'EncryptionAtRestOptions': {
                                    'Enabled': True|False,
                                    'KmsKeyId': 'string'
                                },
                                'NodeToNodeEncryptionOptions': {
                                    'Enabled': True|False
                                },
                                'VPCOptions': {
                                    'AvailabilityZones': [
                                        'string',
                                    ],
                                    'SecurityGroupIds': [
                                        'string',
                                    ],
                                    'SubnetIds': [
                                        'string',
                                    ],
                                    'VPCId': 'string'
                                }
                            },
                            'AwsS3Bucket': {
                                'OwnerId': 'string',
                                'OwnerName': 'string',
                                'CreatedAt': 'string',
                                'ServerSideEncryptionConfiguration': {
                                    'Rules': [
                                        {
                                            'ApplyServerSideEncryptionByDefault': {
                                                'SSEAlgorithm': 'string',
                                                'KMSMasterKeyID': 'string'
                                            }
                                        },
                                    ]
                                }
                            },
                            'AwsS3Object': {
                                'LastModified': 'string',
                                'ETag': 'string',
                                'VersionId': 'string',
                                'ContentType': 'string',
                                'ServerSideEncryption': 'string',
                                'SSEKMSKeyId': 'string'
                            },
                            'AwsIamAccessKey': {
                                'UserName': 'string',
                                'Status': 'Active'|'Inactive',
                                'CreatedAt': 'string',
                                'PrincipalId': 'string',
                                'PrincipalType': 'string',
                                'PrincipalName': 'string'
                            },
                            'AwsIamRole': {
                                'AssumeRolePolicyDocument': 'string',
                                'CreateDate': 'string',
                                'RoleId': 'string',
                                'RoleName': 'string',
                                'MaxSessionDuration': 123,
                                'Path': 'string'
                            },
                            'AwsKmsKey': {
                                'AWSAccountId': 'string',
                                'CreationDate': 123.0,
                                'KeyId': 'string',
                                'KeyManager': 'string',
                                'KeyState': 'string',
                                'Origin': 'string'
                            },
                            'AwsLambdaFunction': {
                                'Code': {
                                    'S3Bucket': 'string',
                                    'S3Key': 'string',
                                    'S3ObjectVersion': 'string',
                                    'ZipFile': 'string'
                                },
                                'CodeSha256': 'string',
                                'DeadLetterConfig': {
                                    'TargetArn': 'string'
                                },
                                'Environment': {
                                    'Variables': {
                                        'string': 'string'
                                    },
                                    'Error': {
                                        'ErrorCode': 'string',
                                        'Message': 'string'
                                    }
                                },
                                'FunctionName': 'string',
                                'Handler': 'string',
                                'KmsKeyArn': 'string',
                                'LastModified': 'string',
                                'Layers': [
                                    {
                                        'Arn': 'string',
                                        'CodeSize': 123
                                    },
                                ],
                                'MasterArn': 'string',
                                'MemorySize': 123,
                                'RevisionId': 'string',
                                'Role': 'string',
                                'Runtime': 'string',
                                'Timeout': 123,
                                'TracingConfig': {
                                    'Mode': 'string'
                                },
                                'VpcConfig': {
                                    'SecurityGroupIds': [
                                        'string',
                                    ],
                                    'SubnetIds': [
                                        'string',
                                    ],
                                    'VpcId': 'string'
                                },
                                'Version': 'string'
                            },
                            'AwsLambdaLayerVersion': {
                                'Version': 123,
                                'CompatibleRuntimes': [
                                    'string',
                                ],
                                'CreatedDate': 'string'
                            },
                            'AwsRdsDbInstance': {
                                'AssociatedRoles': [
                                    {
                                        'RoleArn': 'string',
                                        'FeatureName': 'string',
                                        'Status': 'string'
                                    },
                                ],
                                'CACertificateIdentifier': 'string',
                                'DBClusterIdentifier': 'string',
                                'DBInstanceIdentifier': 'string',
                                'DBInstanceClass': 'string',
                                'DbInstancePort': 123,
                                'DbiResourceId': 'string',
                                'DBName': 'string',
                                'DeletionProtection': True|False,
                                'Endpoint': {
                                    'Address': 'string',
                                    'Port': 123,
                                    'HostedZoneId': 'string'
                                },
                                'Engine': 'string',
                                'EngineVersion': 'string',
                                'IAMDatabaseAuthenticationEnabled': True|False,
                                'InstanceCreateTime': 'string',
                                'KmsKeyId': 'string',
                                'PubliclyAccessible': True|False,
                                'StorageEncrypted': True|False,
                                'TdeCredentialArn': 'string',
                                'VpcSecurityGroups': [
                                    {
                                        'VpcSecurityGroupId': 'string',
                                        'Status': 'string'
                                    },
                                ]
                            },
                            'AwsSnsTopic': {
                                'KmsMasterKeyId': 'string',
                                'Subscription': [
                                    {
                                        'Endpoint': 'string',
                                        'Protocol': 'string'
                                    },
                                ],
                                'TopicName': 'string',
                                'Owner': 'string'
                            },
                            'AwsSqsQueue': {
                                'KmsDataKeyReusePeriodSeconds': 123,
                                'KmsMasterKeyId': 'string',
                                'QueueName': 'string',
                                'DeadLetterTargetArn': 'string'
                            },
                            'AwsWafWebAcl': {
                                'Name': 'string',
                                'DefaultAction': 'string',
                                'Rules': [
                                    {
                                        'Action': {
                                            'Type': 'string'
                                        },
                                        'ExcludedRules': [
                                            {
                                                'RuleId': 'string'
                                            },
                                        ],
                                        'OverrideAction': {
                                            'Type': 'string'
                                        },
                                        'Priority': 123,
                                        'RuleId': 'string',
                                        'Type': 'string'
                                    },
                                ],
                                'WebAclId': 'string'
                            },
                            'Container': {
                                'Name': 'string',
                                'ImageId': 'string',
                                'ImageName': 'string',
                                'LaunchedAt': 'string'
                            },
                            'Other': {
                                'string': 'string'
                            }
                        }
                    },
                ],
                'Compliance': {
                    'Status': 'PASSED'|'WARNING'|'FAILED'|'NOT_AVAILABLE',
                    'RelatedRequirements': [
                        'string',
                    ],
                    'StatusReasons': [
                        {
                            'ReasonCode': 'string',
                            'Description': 'string'
                        },
                    ]
                },
                'VerificationState': 'UNKNOWN'|'TRUE_POSITIVE'|'FALSE_POSITIVE'|'BENIGN_POSITIVE',
                'WorkflowState': 'NEW'|'ASSIGNED'|'IN_PROGRESS'|'DEFERRED'|'RESOLVED',
                'Workflow': {
                    'Status': 'NEW'|'NOTIFIED'|'RESOLVED'|'SUPPRESSED'
                },
                'RecordState': 'ACTIVE'|'ARCHIVED',
                'RelatedFindings': [
                    {
                        'ProductArn': 'string',
                        'Id': 'string'
                    },
                ],
                'Note': {
                    'Text': 'string',
                    'UpdatedBy': 'string',
                    'UpdatedAt': 'string'
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_insight_results(InsightArn=None):
    """
    Lists the results of the Security Hub insight specified by the insight ARN.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_insight_results(
        InsightArn='string'
    )
    
    
    :type InsightArn: string
    :param InsightArn: [REQUIRED]\nThe ARN of the insight for which to return results.\n

    :rtype: dict
ReturnsResponse Syntax{
    'InsightResults': {
        'InsightArn': 'string',
        'GroupByAttribute': 'string',
        'ResultValues': [
            {
                'GroupByAttributeValue': 'string',
                'Count': 123
            },
        ]
    }
}


Response Structure

(dict) --
InsightResults (dict) --The insight results returned by the operation.

InsightArn (string) --The ARN of the insight whose results are returned by the GetInsightResults operation.

GroupByAttribute (string) --The attribute that the findings are grouped by for the insight whose results are returned by the GetInsightResults operation.

ResultValues (list) --The list of insight result values returned by the GetInsightResults operation.

(dict) --The insight result values returned by the GetInsightResults operation.

GroupByAttributeValue (string) --The value of the attribute that the findings are grouped by for the insight whose results are returned by the GetInsightResults operation.

Count (integer) --The number of findings returned for each GroupByAttributeValue .












Exceptions

SecurityHub.Client.exceptions.InternalException
SecurityHub.Client.exceptions.InvalidInputException
SecurityHub.Client.exceptions.InvalidAccessException
SecurityHub.Client.exceptions.LimitExceededException
SecurityHub.Client.exceptions.ResourceNotFoundException


    :return: {
        'InsightResults': {
            'InsightArn': 'string',
            'GroupByAttribute': 'string',
            'ResultValues': [
                {
                    'GroupByAttributeValue': 'string',
                    'Count': 123
                },
            ]
        }
    }
    
    
    """
    pass

def get_insights(InsightArns=None, NextToken=None, MaxResults=None):
    """
    Lists and describes insights for the specified insight ARNs.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_insights(
        InsightArns=[
            'string',
        ],
        NextToken='string',
        MaxResults=123
    )
    
    
    :type InsightArns: list
    :param InsightArns: The ARNs of the insights to describe. If you do not provide any insight ARNs, then GetInsights returns all of your custom insights. It does not return any managed insights.\n\n(string) --\n\n

    :type NextToken: string
    :param NextToken: The token that is required for pagination. On your first call to the GetInsights operation, set the value of this parameter to NULL .\nFor subsequent calls to the operation, to continue listing data, set the value of this parameter to the value returned from the previous response.\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return in the response.

    :rtype: dict

ReturnsResponse Syntax
{
    'Insights': [
        {
            'InsightArn': 'string',
            'Name': 'string',
            'Filters': {
                'ProductArn': [
                    {
                        'Value': 'string',
                        'Comparison': 'EQUALS'|'PREFIX'
                    },
                ],
                'AwsAccountId': [
                    {
                        'Value': 'string',
                        'Comparison': 'EQUALS'|'PREFIX'
                    },
                ],
                'Id': [
                    {
                        'Value': 'string',
                        'Comparison': 'EQUALS'|'PREFIX'
                    },
                ],
                'GeneratorId': [
                    {
                        'Value': 'string',
                        'Comparison': 'EQUALS'|'PREFIX'
                    },
                ],
                'Type': [
                    {
                        'Value': 'string',
                        'Comparison': 'EQUALS'|'PREFIX'
                    },
                ],
                'FirstObservedAt': [
                    {
                        'Start': 'string',
                        'End': 'string',
                        'DateRange': {
                            'Value': 123,
                            'Unit': 'DAYS'
                        }
                    },
                ],
                'LastObservedAt': [
                    {
                        'Start': 'string',
                        'End': 'string',
                        'DateRange': {
                            'Value': 123,
                            'Unit': 'DAYS'
                        }
                    },
                ],
                'CreatedAt': [
                    {
                        'Start': 'string',
                        'End': 'string',
                        'DateRange': {
                            'Value': 123,
                            'Unit': 'DAYS'
                        }
                    },
                ],
                'UpdatedAt': [
                    {
                        'Start': 'string',
                        'End': 'string',
                        'DateRange': {
                            'Value': 123,
                            'Unit': 'DAYS'
                        }
                    },
                ],
                'SeverityProduct': [
                    {
                        'Gte': 123.0,
                        'Lte': 123.0,
                        'Eq': 123.0
                    },
                ],
                'SeverityNormalized': [
                    {
                        'Gte': 123.0,
                        'Lte': 123.0,
                        'Eq': 123.0
                    },
                ],
                'SeverityLabel': [
                    {
                        'Value': 'string',
                        'Comparison': 'EQUALS'|'PREFIX'
                    },
                ],
                'Confidence': [
                    {
                        'Gte': 123.0,
                        'Lte': 123.0,
                        'Eq': 123.0
                    },
                ],
                'Criticality': [
                    {
                        'Gte': 123.0,
                        'Lte': 123.0,
                        'Eq': 123.0
                    },
                ],
                'Title': [
                    {
                        'Value': 'string',
                        'Comparison': 'EQUALS'|'PREFIX'
                    },
                ],
                'Description': [
                    {
                        'Value': 'string',
                        'Comparison': 'EQUALS'|'PREFIX'
                    },
                ],
                'RecommendationText': [
                    {
                        'Value': 'string',
                        'Comparison': 'EQUALS'|'PREFIX'
                    },
                ],
                'SourceUrl': [
                    {
                        'Value': 'string',
                        'Comparison': 'EQUALS'|'PREFIX'
                    },
                ],
                'ProductFields': [
                    {
                        'Key': 'string',
                        'Value': 'string',
                        'Comparison': 'EQUALS'
                    },
                ],
                'ProductName': [
                    {
                        'Value': 'string',
                        'Comparison': 'EQUALS'|'PREFIX'
                    },
                ],
                'CompanyName': [
                    {
                        'Value': 'string',
                        'Comparison': 'EQUALS'|'PREFIX'
                    },
                ],
                'UserDefinedFields': [
                    {
                        'Key': 'string',
                        'Value': 'string',
                        'Comparison': 'EQUALS'
                    },
                ],
                'MalwareName': [
                    {
                        'Value': 'string',
                        'Comparison': 'EQUALS'|'PREFIX'
                    },
                ],
                'MalwareType': [
                    {
                        'Value': 'string',
                        'Comparison': 'EQUALS'|'PREFIX'
                    },
                ],
                'MalwarePath': [
                    {
                        'Value': 'string',
                        'Comparison': 'EQUALS'|'PREFIX'
                    },
                ],
                'MalwareState': [
                    {
                        'Value': 'string',
                        'Comparison': 'EQUALS'|'PREFIX'
                    },
                ],
                'NetworkDirection': [
                    {
                        'Value': 'string',
                        'Comparison': 'EQUALS'|'PREFIX'
                    },
                ],
                'NetworkProtocol': [
                    {
                        'Value': 'string',
                        'Comparison': 'EQUALS'|'PREFIX'
                    },
                ],
                'NetworkSourceIpV4': [
                    {
                        'Cidr': 'string'
                    },
                ],
                'NetworkSourceIpV6': [
                    {
                        'Cidr': 'string'
                    },
                ],
                'NetworkSourcePort': [
                    {
                        'Gte': 123.0,
                        'Lte': 123.0,
                        'Eq': 123.0
                    },
                ],
                'NetworkSourceDomain': [
                    {
                        'Value': 'string',
                        'Comparison': 'EQUALS'|'PREFIX'
                    },
                ],
                'NetworkSourceMac': [
                    {
                        'Value': 'string',
                        'Comparison': 'EQUALS'|'PREFIX'
                    },
                ],
                'NetworkDestinationIpV4': [
                    {
                        'Cidr': 'string'
                    },
                ],
                'NetworkDestinationIpV6': [
                    {
                        'Cidr': 'string'
                    },
                ],
                'NetworkDestinationPort': [
                    {
                        'Gte': 123.0,
                        'Lte': 123.0,
                        'Eq': 123.0
                    },
                ],
                'NetworkDestinationDomain': [
                    {
                        'Value': 'string',
                        'Comparison': 'EQUALS'|'PREFIX'
                    },
                ],
                'ProcessName': [
                    {
                        'Value': 'string',
                        'Comparison': 'EQUALS'|'PREFIX'
                    },
                ],
                'ProcessPath': [
                    {
                        'Value': 'string',
                        'Comparison': 'EQUALS'|'PREFIX'
                    },
                ],
                'ProcessPid': [
                    {
                        'Gte': 123.0,
                        'Lte': 123.0,
                        'Eq': 123.0
                    },
                ],
                'ProcessParentPid': [
                    {
                        'Gte': 123.0,
                        'Lte': 123.0,
                        'Eq': 123.0
                    },
                ],
                'ProcessLaunchedAt': [
                    {
                        'Start': 'string',
                        'End': 'string',
                        'DateRange': {
                            'Value': 123,
                            'Unit': 'DAYS'
                        }
                    },
                ],
                'ProcessTerminatedAt': [
                    {
                        'Start': 'string',
                        'End': 'string',
                        'DateRange': {
                            'Value': 123,
                            'Unit': 'DAYS'
                        }
                    },
                ],
                'ThreatIntelIndicatorType': [
                    {
                        'Value': 'string',
                        'Comparison': 'EQUALS'|'PREFIX'
                    },
                ],
                'ThreatIntelIndicatorValue': [
                    {
                        'Value': 'string',
                        'Comparison': 'EQUALS'|'PREFIX'
                    },
                ],
                'ThreatIntelIndicatorCategory': [
                    {
                        'Value': 'string',
                        'Comparison': 'EQUALS'|'PREFIX'
                    },
                ],
                'ThreatIntelIndicatorLastObservedAt': [
                    {
                        'Start': 'string',
                        'End': 'string',
                        'DateRange': {
                            'Value': 123,
                            'Unit': 'DAYS'
                        }
                    },
                ],
                'ThreatIntelIndicatorSource': [
                    {
                        'Value': 'string',
                        'Comparison': 'EQUALS'|'PREFIX'
                    },
                ],
                'ThreatIntelIndicatorSourceUrl': [
                    {
                        'Value': 'string',
                        'Comparison': 'EQUALS'|'PREFIX'
                    },
                ],
                'ResourceType': [
                    {
                        'Value': 'string',
                        'Comparison': 'EQUALS'|'PREFIX'
                    },
                ],
                'ResourceId': [
                    {
                        'Value': 'string',
                        'Comparison': 'EQUALS'|'PREFIX'
                    },
                ],
                'ResourcePartition': [
                    {
                        'Value': 'string',
                        'Comparison': 'EQUALS'|'PREFIX'
                    },
                ],
                'ResourceRegion': [
                    {
                        'Value': 'string',
                        'Comparison': 'EQUALS'|'PREFIX'
                    },
                ],
                'ResourceTags': [
                    {
                        'Key': 'string',
                        'Value': 'string',
                        'Comparison': 'EQUALS'
                    },
                ],
                'ResourceAwsEc2InstanceType': [
                    {
                        'Value': 'string',
                        'Comparison': 'EQUALS'|'PREFIX'
                    },
                ],
                'ResourceAwsEc2InstanceImageId': [
                    {
                        'Value': 'string',
                        'Comparison': 'EQUALS'|'PREFIX'
                    },
                ],
                'ResourceAwsEc2InstanceIpV4Addresses': [
                    {
                        'Cidr': 'string'
                    },
                ],
                'ResourceAwsEc2InstanceIpV6Addresses': [
                    {
                        'Cidr': 'string'
                    },
                ],
                'ResourceAwsEc2InstanceKeyName': [
                    {
                        'Value': 'string',
                        'Comparison': 'EQUALS'|'PREFIX'
                    },
                ],
                'ResourceAwsEc2InstanceIamInstanceProfileArn': [
                    {
                        'Value': 'string',
                        'Comparison': 'EQUALS'|'PREFIX'
                    },
                ],
                'ResourceAwsEc2InstanceVpcId': [
                    {
                        'Value': 'string',
                        'Comparison': 'EQUALS'|'PREFIX'
                    },
                ],
                'ResourceAwsEc2InstanceSubnetId': [
                    {
                        'Value': 'string',
                        'Comparison': 'EQUALS'|'PREFIX'
                    },
                ],
                'ResourceAwsEc2InstanceLaunchedAt': [
                    {
                        'Start': 'string',
                        'End': 'string',
                        'DateRange': {
                            'Value': 123,
                            'Unit': 'DAYS'
                        }
                    },
                ],
                'ResourceAwsS3BucketOwnerId': [
                    {
                        'Value': 'string',
                        'Comparison': 'EQUALS'|'PREFIX'
                    },
                ],
                'ResourceAwsS3BucketOwnerName': [
                    {
                        'Value': 'string',
                        'Comparison': 'EQUALS'|'PREFIX'
                    },
                ],
                'ResourceAwsIamAccessKeyUserName': [
                    {
                        'Value': 'string',
                        'Comparison': 'EQUALS'|'PREFIX'
                    },
                ],
                'ResourceAwsIamAccessKeyStatus': [
                    {
                        'Value': 'string',
                        'Comparison': 'EQUALS'|'PREFIX'
                    },
                ],
                'ResourceAwsIamAccessKeyCreatedAt': [
                    {
                        'Start': 'string',
                        'End': 'string',
                        'DateRange': {
                            'Value': 123,
                            'Unit': 'DAYS'
                        }
                    },
                ],
                'ResourceContainerName': [
                    {
                        'Value': 'string',
                        'Comparison': 'EQUALS'|'PREFIX'
                    },
                ],
                'ResourceContainerImageId': [
                    {
                        'Value': 'string',
                        'Comparison': 'EQUALS'|'PREFIX'
                    },
                ],
                'ResourceContainerImageName': [
                    {
                        'Value': 'string',
                        'Comparison': 'EQUALS'|'PREFIX'
                    },
                ],
                'ResourceContainerLaunchedAt': [
                    {
                        'Start': 'string',
                        'End': 'string',
                        'DateRange': {
                            'Value': 123,
                            'Unit': 'DAYS'
                        }
                    },
                ],
                'ResourceDetailsOther': [
                    {
                        'Key': 'string',
                        'Value': 'string',
                        'Comparison': 'EQUALS'
                    },
                ],
                'ComplianceStatus': [
                    {
                        'Value': 'string',
                        'Comparison': 'EQUALS'|'PREFIX'
                    },
                ],
                'VerificationState': [
                    {
                        'Value': 'string',
                        'Comparison': 'EQUALS'|'PREFIX'
                    },
                ],
                'WorkflowState': [
                    {
                        'Value': 'string',
                        'Comparison': 'EQUALS'|'PREFIX'
                    },
                ],
                'WorkflowStatus': [
                    {
                        'Value': 'string',
                        'Comparison': 'EQUALS'|'PREFIX'
                    },
                ],
                'RecordState': [
                    {
                        'Value': 'string',
                        'Comparison': 'EQUALS'|'PREFIX'
                    },
                ],
                'RelatedFindingsProductArn': [
                    {
                        'Value': 'string',
                        'Comparison': 'EQUALS'|'PREFIX'
                    },
                ],
                'RelatedFindingsId': [
                    {
                        'Value': 'string',
                        'Comparison': 'EQUALS'|'PREFIX'
                    },
                ],
                'NoteText': [
                    {
                        'Value': 'string',
                        'Comparison': 'EQUALS'|'PREFIX'
                    },
                ],
                'NoteUpdatedAt': [
                    {
                        'Start': 'string',
                        'End': 'string',
                        'DateRange': {
                            'Value': 123,
                            'Unit': 'DAYS'
                        }
                    },
                ],
                'NoteUpdatedBy': [
                    {
                        'Value': 'string',
                        'Comparison': 'EQUALS'|'PREFIX'
                    },
                ],
                'Keyword': [
                    {
                        'Value': 'string'
                    },
                ]
            },
            'GroupByAttribute': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Insights (list) --
The insights returned by the operation.

(dict) --
Contains information about a Security Hub insight.

InsightArn (string) --
The ARN of a Security Hub insight.

Name (string) --
The name of a Security Hub insight.

Filters (dict) --
One or more attributes used to filter the findings included in the insight. The insight only includes findings that match the criteria defined in the filters.

ProductArn (list) --
The ARN generated by Security Hub that uniquely identifies a third-party company (security findings provider) after this provider\'s product (solution that generates findings) is registered with Security Hub.

(dict) --
A string filter for querying findings.

Value (string) --
The string filter value.

Comparison (string) --
The condition to be applied to a string value when querying for findings.





AwsAccountId (list) --
The AWS account ID that a finding is generated in.

(dict) --
A string filter for querying findings.

Value (string) --
The string filter value.

Comparison (string) --
The condition to be applied to a string value when querying for findings.





Id (list) --
The security findings provider-specific identifier for a finding.

(dict) --
A string filter for querying findings.

Value (string) --
The string filter value.

Comparison (string) --
The condition to be applied to a string value when querying for findings.





GeneratorId (list) --
The identifier for the solution-specific component (a discrete unit of logic) that generated a finding. In various security-findings providers\' solutions, this generator can be called a rule, a check, a detector, a plugin, etc.

(dict) --
A string filter for querying findings.

Value (string) --
The string filter value.

Comparison (string) --
The condition to be applied to a string value when querying for findings.





Type (list) --
A finding type in the format of namespace/category/classifier that classifies a finding.

(dict) --
A string filter for querying findings.

Value (string) --
The string filter value.

Comparison (string) --
The condition to be applied to a string value when querying for findings.





FirstObservedAt (list) --
An ISO8601-formatted timestamp that indicates when the security-findings provider first observed the potential security issue that a finding captured.

(dict) --
A date filter for querying findings.

Start (string) --
A start date for the date filter.

End (string) --
An end date for the date filter.

DateRange (dict) --
A date range for the date filter.

Value (integer) --
A date range value for the date filter.

Unit (string) --
A date range unit for the date filter.







LastObservedAt (list) --
An ISO8601-formatted timestamp that indicates when the security-findings provider most recently observed the potential security issue that a finding captured.

(dict) --
A date filter for querying findings.

Start (string) --
A start date for the date filter.

End (string) --
An end date for the date filter.

DateRange (dict) --
A date range for the date filter.

Value (integer) --
A date range value for the date filter.

Unit (string) --
A date range unit for the date filter.







CreatedAt (list) --
An ISO8601-formatted timestamp that indicates when the security-findings provider captured the potential security issue that a finding captured.

(dict) --
A date filter for querying findings.

Start (string) --
A start date for the date filter.

End (string) --
An end date for the date filter.

DateRange (dict) --
A date range for the date filter.

Value (integer) --
A date range value for the date filter.

Unit (string) --
A date range unit for the date filter.







UpdatedAt (list) --
An ISO8601-formatted timestamp that indicates when the security-findings provider last updated the finding record.

(dict) --
A date filter for querying findings.

Start (string) --
A start date for the date filter.

End (string) --
An end date for the date filter.

DateRange (dict) --
A date range for the date filter.

Value (integer) --
A date range value for the date filter.

Unit (string) --
A date range unit for the date filter.







SeverityProduct (list) --
The native severity as defined by the security-findings provider\'s solution that generated the finding.

(dict) --
A number filter for querying findings.

Gte (float) --
The greater-than-equal condition to be applied to a single field when querying for findings.

Lte (float) --
The less-than-equal condition to be applied to a single field when querying for findings.

Eq (float) --
The equal-to condition to be applied to a single field when querying for findings.





SeverityNormalized (list) --
The normalized severity of a finding.

(dict) --
A number filter for querying findings.

Gte (float) --
The greater-than-equal condition to be applied to a single field when querying for findings.

Lte (float) --
The less-than-equal condition to be applied to a single field when querying for findings.

Eq (float) --
The equal-to condition to be applied to a single field when querying for findings.





SeverityLabel (list) --
The label of a finding\'s severity.

(dict) --
A string filter for querying findings.

Value (string) --
The string filter value.

Comparison (string) --
The condition to be applied to a string value when querying for findings.





Confidence (list) --
A finding\'s confidence. Confidence is defined as the likelihood that a finding accurately identifies the behavior or issue that it was intended to identify.
Confidence is scored on a 0-100 basis using a ratio scale, where 0 means zero percent confidence and 100 means 100 percent confidence.

(dict) --
A number filter for querying findings.

Gte (float) --
The greater-than-equal condition to be applied to a single field when querying for findings.

Lte (float) --
The less-than-equal condition to be applied to a single field when querying for findings.

Eq (float) --
The equal-to condition to be applied to a single field when querying for findings.





Criticality (list) --
The level of importance assigned to the resources associated with the finding.
A score of 0 means that the underlying resources have no criticality, and a score of 100 is reserved for the most critical resources.

(dict) --
A number filter for querying findings.

Gte (float) --
The greater-than-equal condition to be applied to a single field when querying for findings.

Lte (float) --
The less-than-equal condition to be applied to a single field when querying for findings.

Eq (float) --
The equal-to condition to be applied to a single field when querying for findings.





Title (list) --
A finding\'s title.

(dict) --
A string filter for querying findings.

Value (string) --
The string filter value.

Comparison (string) --
The condition to be applied to a string value when querying for findings.





Description (list) --
A finding\'s description.

(dict) --
A string filter for querying findings.

Value (string) --
The string filter value.

Comparison (string) --
The condition to be applied to a string value when querying for findings.





RecommendationText (list) --
The recommendation of what to do about the issue described in a finding.

(dict) --
A string filter for querying findings.

Value (string) --
The string filter value.

Comparison (string) --
The condition to be applied to a string value when querying for findings.





SourceUrl (list) --
A URL that links to a page about the current finding in the security-findings provider\'s solution.

(dict) --
A string filter for querying findings.

Value (string) --
The string filter value.

Comparison (string) --
The condition to be applied to a string value when querying for findings.





ProductFields (list) --
A data type where security-findings providers can include additional solution-specific details that aren\'t part of the defined AwsSecurityFinding format.

(dict) --
The map filter for querying findings.

Key (string) --
The key of the map filter.

Value (string) --
The value for the key in the map filter.

Comparison (string) --
The condition to apply to a key value when querying for findings with a map filter.





ProductName (list) --
The name of the solution (product) that generates findings.

(dict) --
A string filter for querying findings.

Value (string) --
The string filter value.

Comparison (string) --
The condition to be applied to a string value when querying for findings.





CompanyName (list) --
The name of the findings provider (company) that owns the solution (product) that generates findings.

(dict) --
A string filter for querying findings.

Value (string) --
The string filter value.

Comparison (string) --
The condition to be applied to a string value when querying for findings.





UserDefinedFields (list) --
A list of name/value string pairs associated with the finding. These are custom, user-defined fields added to a finding.

(dict) --
The map filter for querying findings.

Key (string) --
The key of the map filter.

Value (string) --
The value for the key in the map filter.

Comparison (string) --
The condition to apply to a key value when querying for findings with a map filter.





MalwareName (list) --
The name of the malware that was observed.

(dict) --
A string filter for querying findings.

Value (string) --
The string filter value.

Comparison (string) --
The condition to be applied to a string value when querying for findings.





MalwareType (list) --
The type of the malware that was observed.

(dict) --
A string filter for querying findings.

Value (string) --
The string filter value.

Comparison (string) --
The condition to be applied to a string value when querying for findings.





MalwarePath (list) --
The filesystem path of the malware that was observed.

(dict) --
A string filter for querying findings.

Value (string) --
The string filter value.

Comparison (string) --
The condition to be applied to a string value when querying for findings.





MalwareState (list) --
The state of the malware that was observed.

(dict) --
A string filter for querying findings.

Value (string) --
The string filter value.

Comparison (string) --
The condition to be applied to a string value when querying for findings.





NetworkDirection (list) --
Indicates the direction of network traffic associated with a finding.

(dict) --
A string filter for querying findings.

Value (string) --
The string filter value.

Comparison (string) --
The condition to be applied to a string value when querying for findings.





NetworkProtocol (list) --
The protocol of network-related information about a finding.

(dict) --
A string filter for querying findings.

Value (string) --
The string filter value.

Comparison (string) --
The condition to be applied to a string value when querying for findings.





NetworkSourceIpV4 (list) --
The source IPv4 address of network-related information about a finding.

(dict) --
The IP filter for querying findings.

Cidr (string) --
A finding\'s CIDR value.





NetworkSourceIpV6 (list) --
The source IPv6 address of network-related information about a finding.

(dict) --
The IP filter for querying findings.

Cidr (string) --
A finding\'s CIDR value.





NetworkSourcePort (list) --
The source port of network-related information about a finding.

(dict) --
A number filter for querying findings.

Gte (float) --
The greater-than-equal condition to be applied to a single field when querying for findings.

Lte (float) --
The less-than-equal condition to be applied to a single field when querying for findings.

Eq (float) --
The equal-to condition to be applied to a single field when querying for findings.





NetworkSourceDomain (list) --
The source domain of network-related information about a finding.

(dict) --
A string filter for querying findings.

Value (string) --
The string filter value.

Comparison (string) --
The condition to be applied to a string value when querying for findings.





NetworkSourceMac (list) --
The source media access control (MAC) address of network-related information about a finding.

(dict) --
A string filter for querying findings.

Value (string) --
The string filter value.

Comparison (string) --
The condition to be applied to a string value when querying for findings.





NetworkDestinationIpV4 (list) --
The destination IPv4 address of network-related information about a finding.

(dict) --
The IP filter for querying findings.

Cidr (string) --
A finding\'s CIDR value.





NetworkDestinationIpV6 (list) --
The destination IPv6 address of network-related information about a finding.

(dict) --
The IP filter for querying findings.

Cidr (string) --
A finding\'s CIDR value.





NetworkDestinationPort (list) --
The destination port of network-related information about a finding.

(dict) --
A number filter for querying findings.

Gte (float) --
The greater-than-equal condition to be applied to a single field when querying for findings.

Lte (float) --
The less-than-equal condition to be applied to a single field when querying for findings.

Eq (float) --
The equal-to condition to be applied to a single field when querying for findings.





NetworkDestinationDomain (list) --
The destination domain of network-related information about a finding.

(dict) --
A string filter for querying findings.

Value (string) --
The string filter value.

Comparison (string) --
The condition to be applied to a string value when querying for findings.





ProcessName (list) --
The name of the process.

(dict) --
A string filter for querying findings.

Value (string) --
The string filter value.

Comparison (string) --
The condition to be applied to a string value when querying for findings.





ProcessPath (list) --
The path to the process executable.

(dict) --
A string filter for querying findings.

Value (string) --
The string filter value.

Comparison (string) --
The condition to be applied to a string value when querying for findings.





ProcessPid (list) --
The process ID.

(dict) --
A number filter for querying findings.

Gte (float) --
The greater-than-equal condition to be applied to a single field when querying for findings.

Lte (float) --
The less-than-equal condition to be applied to a single field when querying for findings.

Eq (float) --
The equal-to condition to be applied to a single field when querying for findings.





ProcessParentPid (list) --
The parent process ID.

(dict) --
A number filter for querying findings.

Gte (float) --
The greater-than-equal condition to be applied to a single field when querying for findings.

Lte (float) --
The less-than-equal condition to be applied to a single field when querying for findings.

Eq (float) --
The equal-to condition to be applied to a single field when querying for findings.





ProcessLaunchedAt (list) --
The date/time that the process was launched.

(dict) --
A date filter for querying findings.

Start (string) --
A start date for the date filter.

End (string) --
An end date for the date filter.

DateRange (dict) --
A date range for the date filter.

Value (integer) --
A date range value for the date filter.

Unit (string) --
A date range unit for the date filter.







ProcessTerminatedAt (list) --
The date/time that the process was terminated.

(dict) --
A date filter for querying findings.

Start (string) --
A start date for the date filter.

End (string) --
An end date for the date filter.

DateRange (dict) --
A date range for the date filter.

Value (integer) --
A date range value for the date filter.

Unit (string) --
A date range unit for the date filter.







ThreatIntelIndicatorType (list) --
The type of a threat intelligence indicator.

(dict) --
A string filter for querying findings.

Value (string) --
The string filter value.

Comparison (string) --
The condition to be applied to a string value when querying for findings.





ThreatIntelIndicatorValue (list) --
The value of a threat intelligence indicator.

(dict) --
A string filter for querying findings.

Value (string) --
The string filter value.

Comparison (string) --
The condition to be applied to a string value when querying for findings.





ThreatIntelIndicatorCategory (list) --
The category of a threat intelligence indicator.

(dict) --
A string filter for querying findings.

Value (string) --
The string filter value.

Comparison (string) --
The condition to be applied to a string value when querying for findings.





ThreatIntelIndicatorLastObservedAt (list) --
The date/time of the last observation of a threat intelligence indicator.

(dict) --
A date filter for querying findings.

Start (string) --
A start date for the date filter.

End (string) --
An end date for the date filter.

DateRange (dict) --
A date range for the date filter.

Value (integer) --
A date range value for the date filter.

Unit (string) --
A date range unit for the date filter.







ThreatIntelIndicatorSource (list) --
The source of the threat intelligence.

(dict) --
A string filter for querying findings.

Value (string) --
The string filter value.

Comparison (string) --
The condition to be applied to a string value when querying for findings.





ThreatIntelIndicatorSourceUrl (list) --
The URL for more details from the source of the threat intelligence.

(dict) --
A string filter for querying findings.

Value (string) --
The string filter value.

Comparison (string) --
The condition to be applied to a string value when querying for findings.





ResourceType (list) --
Specifies the type of the resource that details are provided for.

(dict) --
A string filter for querying findings.

Value (string) --
The string filter value.

Comparison (string) --
The condition to be applied to a string value when querying for findings.





ResourceId (list) --
The canonical identifier for the given resource type.

(dict) --
A string filter for querying findings.

Value (string) --
The string filter value.

Comparison (string) --
The condition to be applied to a string value when querying for findings.





ResourcePartition (list) --
The canonical AWS partition name that the Region is assigned to.

(dict) --
A string filter for querying findings.

Value (string) --
The string filter value.

Comparison (string) --
The condition to be applied to a string value when querying for findings.





ResourceRegion (list) --
The canonical AWS external Region name where this resource is located.

(dict) --
A string filter for querying findings.

Value (string) --
The string filter value.

Comparison (string) --
The condition to be applied to a string value when querying for findings.





ResourceTags (list) --
A list of AWS tags associated with a resource at the time the finding was processed.

(dict) --
The map filter for querying findings.

Key (string) --
The key of the map filter.

Value (string) --
The value for the key in the map filter.

Comparison (string) --
The condition to apply to a key value when querying for findings with a map filter.





ResourceAwsEc2InstanceType (list) --
The instance type of the instance.

(dict) --
A string filter for querying findings.

Value (string) --
The string filter value.

Comparison (string) --
The condition to be applied to a string value when querying for findings.





ResourceAwsEc2InstanceImageId (list) --
The Amazon Machine Image (AMI) ID of the instance.

(dict) --
A string filter for querying findings.

Value (string) --
The string filter value.

Comparison (string) --
The condition to be applied to a string value when querying for findings.





ResourceAwsEc2InstanceIpV4Addresses (list) --
The IPv4 addresses associated with the instance.

(dict) --
The IP filter for querying findings.

Cidr (string) --
A finding\'s CIDR value.





ResourceAwsEc2InstanceIpV6Addresses (list) --
The IPv6 addresses associated with the instance.

(dict) --
The IP filter for querying findings.

Cidr (string) --
A finding\'s CIDR value.





ResourceAwsEc2InstanceKeyName (list) --
The key name associated with the instance.

(dict) --
A string filter for querying findings.

Value (string) --
The string filter value.

Comparison (string) --
The condition to be applied to a string value when querying for findings.





ResourceAwsEc2InstanceIamInstanceProfileArn (list) --
The IAM profile ARN of the instance.

(dict) --
A string filter for querying findings.

Value (string) --
The string filter value.

Comparison (string) --
The condition to be applied to a string value when querying for findings.





ResourceAwsEc2InstanceVpcId (list) --
The identifier of the VPC that the instance was launched in.

(dict) --
A string filter for querying findings.

Value (string) --
The string filter value.

Comparison (string) --
The condition to be applied to a string value when querying for findings.





ResourceAwsEc2InstanceSubnetId (list) --
The identifier of the subnet that the instance was launched in.

(dict) --
A string filter for querying findings.

Value (string) --
The string filter value.

Comparison (string) --
The condition to be applied to a string value when querying for findings.





ResourceAwsEc2InstanceLaunchedAt (list) --
The date and time the instance was launched.

(dict) --
A date filter for querying findings.

Start (string) --
A start date for the date filter.

End (string) --
An end date for the date filter.

DateRange (dict) --
A date range for the date filter.

Value (integer) --
A date range value for the date filter.

Unit (string) --
A date range unit for the date filter.







ResourceAwsS3BucketOwnerId (list) --
The canonical user ID of the owner of the S3 bucket.

(dict) --
A string filter for querying findings.

Value (string) --
The string filter value.

Comparison (string) --
The condition to be applied to a string value when querying for findings.





ResourceAwsS3BucketOwnerName (list) --
The display name of the owner of the S3 bucket.

(dict) --
A string filter for querying findings.

Value (string) --
The string filter value.

Comparison (string) --
The condition to be applied to a string value when querying for findings.





ResourceAwsIamAccessKeyUserName (list) --
The user associated with the IAM access key related to a finding.

(dict) --
A string filter for querying findings.

Value (string) --
The string filter value.

Comparison (string) --
The condition to be applied to a string value when querying for findings.





ResourceAwsIamAccessKeyStatus (list) --
The status of the IAM access key related to a finding.

(dict) --
A string filter for querying findings.

Value (string) --
The string filter value.

Comparison (string) --
The condition to be applied to a string value when querying for findings.





ResourceAwsIamAccessKeyCreatedAt (list) --
The creation date/time of the IAM access key related to a finding.

(dict) --
A date filter for querying findings.

Start (string) --
A start date for the date filter.

End (string) --
An end date for the date filter.

DateRange (dict) --
A date range for the date filter.

Value (integer) --
A date range value for the date filter.

Unit (string) --
A date range unit for the date filter.







ResourceContainerName (list) --
The name of the container related to a finding.

(dict) --
A string filter for querying findings.

Value (string) --
The string filter value.

Comparison (string) --
The condition to be applied to a string value when querying for findings.





ResourceContainerImageId (list) --
The identifier of the image related to a finding.

(dict) --
A string filter for querying findings.

Value (string) --
The string filter value.

Comparison (string) --
The condition to be applied to a string value when querying for findings.





ResourceContainerImageName (list) --
The name of the image related to a finding.

(dict) --
A string filter for querying findings.

Value (string) --
The string filter value.

Comparison (string) --
The condition to be applied to a string value when querying for findings.





ResourceContainerLaunchedAt (list) --
The date/time that the container was started.

(dict) --
A date filter for querying findings.

Start (string) --
A start date for the date filter.

End (string) --
An end date for the date filter.

DateRange (dict) --
A date range for the date filter.

Value (integer) --
A date range value for the date filter.

Unit (string) --
A date range unit for the date filter.







ResourceDetailsOther (list) --
The details of a resource that doesn\'t have a specific subfield for the resource type defined.

(dict) --
The map filter for querying findings.

Key (string) --
The key of the map filter.

Value (string) --
The value for the key in the map filter.

Comparison (string) --
The condition to apply to a key value when querying for findings with a map filter.





ComplianceStatus (list) --
Exclusive to findings that are generated as the result of a check run against a specific rule in a supported standard, such as CIS AWS Foundations. Contains security standard-related finding details.

(dict) --
A string filter for querying findings.

Value (string) --
The string filter value.

Comparison (string) --
The condition to be applied to a string value when querying for findings.





VerificationState (list) --
The veracity of a finding.

(dict) --
A string filter for querying findings.

Value (string) --
The string filter value.

Comparison (string) --
The condition to be applied to a string value when querying for findings.





WorkflowState (list) --
The workflow state of a finding.

(dict) --
A string filter for querying findings.

Value (string) --
The string filter value.

Comparison (string) --
The condition to be applied to a string value when querying for findings.





WorkflowStatus (list) --
The status of the investigation into a finding. Allowed values are the following.

NEW - The initial state of a finding, before it is reviewed.
NOTIFIED - Indicates that the resource owner has been notified about the security issue. Used when the initial reviewer is not the resource owner, and needs intervention from the resource owner.
SUPPRESSED - The finding will not be reviewed again and will not be acted upon.
RESOLVED - The finding was reviewed and remediated and is now considered resolved.


(dict) --
A string filter for querying findings.

Value (string) --
The string filter value.

Comparison (string) --
The condition to be applied to a string value when querying for findings.





RecordState (list) --
The updated record state for the finding.

(dict) --
A string filter for querying findings.

Value (string) --
The string filter value.

Comparison (string) --
The condition to be applied to a string value when querying for findings.





RelatedFindingsProductArn (list) --
The ARN of the solution that generated a related finding.

(dict) --
A string filter for querying findings.

Value (string) --
The string filter value.

Comparison (string) --
The condition to be applied to a string value when querying for findings.





RelatedFindingsId (list) --
The solution-generated identifier for a related finding.

(dict) --
A string filter for querying findings.

Value (string) --
The string filter value.

Comparison (string) --
The condition to be applied to a string value when querying for findings.





NoteText (list) --
The text of a note.

(dict) --
A string filter for querying findings.

Value (string) --
The string filter value.

Comparison (string) --
The condition to be applied to a string value when querying for findings.





NoteUpdatedAt (list) --
The timestamp of when the note was updated.

(dict) --
A date filter for querying findings.

Start (string) --
A start date for the date filter.

End (string) --
An end date for the date filter.

DateRange (dict) --
A date range for the date filter.

Value (integer) --
A date range value for the date filter.

Unit (string) --
A date range unit for the date filter.







NoteUpdatedBy (list) --
The principal that created a note.

(dict) --
A string filter for querying findings.

Value (string) --
The string filter value.

Comparison (string) --
The condition to be applied to a string value when querying for findings.





Keyword (list) --
A keyword for a finding.

(dict) --
A keyword filter for querying findings.

Value (string) --
A value for the keyword.







GroupByAttribute (string) --
The grouping attribute for the insight\'s findings. Indicates how to group the matching findings, and identifies the type of item that the insight applies to. For example, if an insight is grouped by resource identifier, then the insight produces a list of resource identifiers.





NextToken (string) --
The pagination token to use to request the next page of results.







Exceptions

SecurityHub.Client.exceptions.InternalException
SecurityHub.Client.exceptions.InvalidInputException
SecurityHub.Client.exceptions.InvalidAccessException
SecurityHub.Client.exceptions.LimitExceededException
SecurityHub.Client.exceptions.ResourceNotFoundException


    :return: {
        'Insights': [
            {
                'InsightArn': 'string',
                'Name': 'string',
                'Filters': {
                    'ProductArn': [
                        {
                            'Value': 'string',
                            'Comparison': 'EQUALS'|'PREFIX'
                        },
                    ],
                    'AwsAccountId': [
                        {
                            'Value': 'string',
                            'Comparison': 'EQUALS'|'PREFIX'
                        },
                    ],
                    'Id': [
                        {
                            'Value': 'string',
                            'Comparison': 'EQUALS'|'PREFIX'
                        },
                    ],
                    'GeneratorId': [
                        {
                            'Value': 'string',
                            'Comparison': 'EQUALS'|'PREFIX'
                        },
                    ],
                    'Type': [
                        {
                            'Value': 'string',
                            'Comparison': 'EQUALS'|'PREFIX'
                        },
                    ],
                    'FirstObservedAt': [
                        {
                            'Start': 'string',
                            'End': 'string',
                            'DateRange': {
                                'Value': 123,
                                'Unit': 'DAYS'
                            }
                        },
                    ],
                    'LastObservedAt': [
                        {
                            'Start': 'string',
                            'End': 'string',
                            'DateRange': {
                                'Value': 123,
                                'Unit': 'DAYS'
                            }
                        },
                    ],
                    'CreatedAt': [
                        {
                            'Start': 'string',
                            'End': 'string',
                            'DateRange': {
                                'Value': 123,
                                'Unit': 'DAYS'
                            }
                        },
                    ],
                    'UpdatedAt': [
                        {
                            'Start': 'string',
                            'End': 'string',
                            'DateRange': {
                                'Value': 123,
                                'Unit': 'DAYS'
                            }
                        },
                    ],
                    'SeverityProduct': [
                        {
                            'Gte': 123.0,
                            'Lte': 123.0,
                            'Eq': 123.0
                        },
                    ],
                    'SeverityNormalized': [
                        {
                            'Gte': 123.0,
                            'Lte': 123.0,
                            'Eq': 123.0
                        },
                    ],
                    'SeverityLabel': [
                        {
                            'Value': 'string',
                            'Comparison': 'EQUALS'|'PREFIX'
                        },
                    ],
                    'Confidence': [
                        {
                            'Gte': 123.0,
                            'Lte': 123.0,
                            'Eq': 123.0
                        },
                    ],
                    'Criticality': [
                        {
                            'Gte': 123.0,
                            'Lte': 123.0,
                            'Eq': 123.0
                        },
                    ],
                    'Title': [
                        {
                            'Value': 'string',
                            'Comparison': 'EQUALS'|'PREFIX'
                        },
                    ],
                    'Description': [
                        {
                            'Value': 'string',
                            'Comparison': 'EQUALS'|'PREFIX'
                        },
                    ],
                    'RecommendationText': [
                        {
                            'Value': 'string',
                            'Comparison': 'EQUALS'|'PREFIX'
                        },
                    ],
                    'SourceUrl': [
                        {
                            'Value': 'string',
                            'Comparison': 'EQUALS'|'PREFIX'
                        },
                    ],
                    'ProductFields': [
                        {
                            'Key': 'string',
                            'Value': 'string',
                            'Comparison': 'EQUALS'
                        },
                    ],
                    'ProductName': [
                        {
                            'Value': 'string',
                            'Comparison': 'EQUALS'|'PREFIX'
                        },
                    ],
                    'CompanyName': [
                        {
                            'Value': 'string',
                            'Comparison': 'EQUALS'|'PREFIX'
                        },
                    ],
                    'UserDefinedFields': [
                        {
                            'Key': 'string',
                            'Value': 'string',
                            'Comparison': 'EQUALS'
                        },
                    ],
                    'MalwareName': [
                        {
                            'Value': 'string',
                            'Comparison': 'EQUALS'|'PREFIX'
                        },
                    ],
                    'MalwareType': [
                        {
                            'Value': 'string',
                            'Comparison': 'EQUALS'|'PREFIX'
                        },
                    ],
                    'MalwarePath': [
                        {
                            'Value': 'string',
                            'Comparison': 'EQUALS'|'PREFIX'
                        },
                    ],
                    'MalwareState': [
                        {
                            'Value': 'string',
                            'Comparison': 'EQUALS'|'PREFIX'
                        },
                    ],
                    'NetworkDirection': [
                        {
                            'Value': 'string',
                            'Comparison': 'EQUALS'|'PREFIX'
                        },
                    ],
                    'NetworkProtocol': [
                        {
                            'Value': 'string',
                            'Comparison': 'EQUALS'|'PREFIX'
                        },
                    ],
                    'NetworkSourceIpV4': [
                        {
                            'Cidr': 'string'
                        },
                    ],
                    'NetworkSourceIpV6': [
                        {
                            'Cidr': 'string'
                        },
                    ],
                    'NetworkSourcePort': [
                        {
                            'Gte': 123.0,
                            'Lte': 123.0,
                            'Eq': 123.0
                        },
                    ],
                    'NetworkSourceDomain': [
                        {
                            'Value': 'string',
                            'Comparison': 'EQUALS'|'PREFIX'
                        },
                    ],
                    'NetworkSourceMac': [
                        {
                            'Value': 'string',
                            'Comparison': 'EQUALS'|'PREFIX'
                        },
                    ],
                    'NetworkDestinationIpV4': [
                        {
                            'Cidr': 'string'
                        },
                    ],
                    'NetworkDestinationIpV6': [
                        {
                            'Cidr': 'string'
                        },
                    ],
                    'NetworkDestinationPort': [
                        {
                            'Gte': 123.0,
                            'Lte': 123.0,
                            'Eq': 123.0
                        },
                    ],
                    'NetworkDestinationDomain': [
                        {
                            'Value': 'string',
                            'Comparison': 'EQUALS'|'PREFIX'
                        },
                    ],
                    'ProcessName': [
                        {
                            'Value': 'string',
                            'Comparison': 'EQUALS'|'PREFIX'
                        },
                    ],
                    'ProcessPath': [
                        {
                            'Value': 'string',
                            'Comparison': 'EQUALS'|'PREFIX'
                        },
                    ],
                    'ProcessPid': [
                        {
                            'Gte': 123.0,
                            'Lte': 123.0,
                            'Eq': 123.0
                        },
                    ],
                    'ProcessParentPid': [
                        {
                            'Gte': 123.0,
                            'Lte': 123.0,
                            'Eq': 123.0
                        },
                    ],
                    'ProcessLaunchedAt': [
                        {
                            'Start': 'string',
                            'End': 'string',
                            'DateRange': {
                                'Value': 123,
                                'Unit': 'DAYS'
                            }
                        },
                    ],
                    'ProcessTerminatedAt': [
                        {
                            'Start': 'string',
                            'End': 'string',
                            'DateRange': {
                                'Value': 123,
                                'Unit': 'DAYS'
                            }
                        },
                    ],
                    'ThreatIntelIndicatorType': [
                        {
                            'Value': 'string',
                            'Comparison': 'EQUALS'|'PREFIX'
                        },
                    ],
                    'ThreatIntelIndicatorValue': [
                        {
                            'Value': 'string',
                            'Comparison': 'EQUALS'|'PREFIX'
                        },
                    ],
                    'ThreatIntelIndicatorCategory': [
                        {
                            'Value': 'string',
                            'Comparison': 'EQUALS'|'PREFIX'
                        },
                    ],
                    'ThreatIntelIndicatorLastObservedAt': [
                        {
                            'Start': 'string',
                            'End': 'string',
                            'DateRange': {
                                'Value': 123,
                                'Unit': 'DAYS'
                            }
                        },
                    ],
                    'ThreatIntelIndicatorSource': [
                        {
                            'Value': 'string',
                            'Comparison': 'EQUALS'|'PREFIX'
                        },
                    ],
                    'ThreatIntelIndicatorSourceUrl': [
                        {
                            'Value': 'string',
                            'Comparison': 'EQUALS'|'PREFIX'
                        },
                    ],
                    'ResourceType': [
                        {
                            'Value': 'string',
                            'Comparison': 'EQUALS'|'PREFIX'
                        },
                    ],
                    'ResourceId': [
                        {
                            'Value': 'string',
                            'Comparison': 'EQUALS'|'PREFIX'
                        },
                    ],
                    'ResourcePartition': [
                        {
                            'Value': 'string',
                            'Comparison': 'EQUALS'|'PREFIX'
                        },
                    ],
                    'ResourceRegion': [
                        {
                            'Value': 'string',
                            'Comparison': 'EQUALS'|'PREFIX'
                        },
                    ],
                    'ResourceTags': [
                        {
                            'Key': 'string',
                            'Value': 'string',
                            'Comparison': 'EQUALS'
                        },
                    ],
                    'ResourceAwsEc2InstanceType': [
                        {
                            'Value': 'string',
                            'Comparison': 'EQUALS'|'PREFIX'
                        },
                    ],
                    'ResourceAwsEc2InstanceImageId': [
                        {
                            'Value': 'string',
                            'Comparison': 'EQUALS'|'PREFIX'
                        },
                    ],
                    'ResourceAwsEc2InstanceIpV4Addresses': [
                        {
                            'Cidr': 'string'
                        },
                    ],
                    'ResourceAwsEc2InstanceIpV6Addresses': [
                        {
                            'Cidr': 'string'
                        },
                    ],
                    'ResourceAwsEc2InstanceKeyName': [
                        {
                            'Value': 'string',
                            'Comparison': 'EQUALS'|'PREFIX'
                        },
                    ],
                    'ResourceAwsEc2InstanceIamInstanceProfileArn': [
                        {
                            'Value': 'string',
                            'Comparison': 'EQUALS'|'PREFIX'
                        },
                    ],
                    'ResourceAwsEc2InstanceVpcId': [
                        {
                            'Value': 'string',
                            'Comparison': 'EQUALS'|'PREFIX'
                        },
                    ],
                    'ResourceAwsEc2InstanceSubnetId': [
                        {
                            'Value': 'string',
                            'Comparison': 'EQUALS'|'PREFIX'
                        },
                    ],
                    'ResourceAwsEc2InstanceLaunchedAt': [
                        {
                            'Start': 'string',
                            'End': 'string',
                            'DateRange': {
                                'Value': 123,
                                'Unit': 'DAYS'
                            }
                        },
                    ],
                    'ResourceAwsS3BucketOwnerId': [
                        {
                            'Value': 'string',
                            'Comparison': 'EQUALS'|'PREFIX'
                        },
                    ],
                    'ResourceAwsS3BucketOwnerName': [
                        {
                            'Value': 'string',
                            'Comparison': 'EQUALS'|'PREFIX'
                        },
                    ],
                    'ResourceAwsIamAccessKeyUserName': [
                        {
                            'Value': 'string',
                            'Comparison': 'EQUALS'|'PREFIX'
                        },
                    ],
                    'ResourceAwsIamAccessKeyStatus': [
                        {
                            'Value': 'string',
                            'Comparison': 'EQUALS'|'PREFIX'
                        },
                    ],
                    'ResourceAwsIamAccessKeyCreatedAt': [
                        {
                            'Start': 'string',
                            'End': 'string',
                            'DateRange': {
                                'Value': 123,
                                'Unit': 'DAYS'
                            }
                        },
                    ],
                    'ResourceContainerName': [
                        {
                            'Value': 'string',
                            'Comparison': 'EQUALS'|'PREFIX'
                        },
                    ],
                    'ResourceContainerImageId': [
                        {
                            'Value': 'string',
                            'Comparison': 'EQUALS'|'PREFIX'
                        },
                    ],
                    'ResourceContainerImageName': [
                        {
                            'Value': 'string',
                            'Comparison': 'EQUALS'|'PREFIX'
                        },
                    ],
                    'ResourceContainerLaunchedAt': [
                        {
                            'Start': 'string',
                            'End': 'string',
                            'DateRange': {
                                'Value': 123,
                                'Unit': 'DAYS'
                            }
                        },
                    ],
                    'ResourceDetailsOther': [
                        {
                            'Key': 'string',
                            'Value': 'string',
                            'Comparison': 'EQUALS'
                        },
                    ],
                    'ComplianceStatus': [
                        {
                            'Value': 'string',
                            'Comparison': 'EQUALS'|'PREFIX'
                        },
                    ],
                    'VerificationState': [
                        {
                            'Value': 'string',
                            'Comparison': 'EQUALS'|'PREFIX'
                        },
                    ],
                    'WorkflowState': [
                        {
                            'Value': 'string',
                            'Comparison': 'EQUALS'|'PREFIX'
                        },
                    ],
                    'WorkflowStatus': [
                        {
                            'Value': 'string',
                            'Comparison': 'EQUALS'|'PREFIX'
                        },
                    ],
                    'RecordState': [
                        {
                            'Value': 'string',
                            'Comparison': 'EQUALS'|'PREFIX'
                        },
                    ],
                    'RelatedFindingsProductArn': [
                        {
                            'Value': 'string',
                            'Comparison': 'EQUALS'|'PREFIX'
                        },
                    ],
                    'RelatedFindingsId': [
                        {
                            'Value': 'string',
                            'Comparison': 'EQUALS'|'PREFIX'
                        },
                    ],
                    'NoteText': [
                        {
                            'Value': 'string',
                            'Comparison': 'EQUALS'|'PREFIX'
                        },
                    ],
                    'NoteUpdatedAt': [
                        {
                            'Start': 'string',
                            'End': 'string',
                            'DateRange': {
                                'Value': 123,
                                'Unit': 'DAYS'
                            }
                        },
                    ],
                    'NoteUpdatedBy': [
                        {
                            'Value': 'string',
                            'Comparison': 'EQUALS'|'PREFIX'
                        },
                    ],
                    'Keyword': [
                        {
                            'Value': 'string'
                        },
                    ]
                },
                'GroupByAttribute': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    NEW - The initial state of a finding, before it is reviewed.
    NOTIFIED - Indicates that the resource owner has been notified about the security issue. Used when the initial reviewer is not the resource owner, and needs intervention from the resource owner.
    SUPPRESSED - The finding will not be reviewed again and will not be acted upon.
    RESOLVED - The finding was reviewed and remediated and is now considered resolved.
    
    """
    pass

def get_invitations_count():
    """
    Returns the count of all Security Hub membership invitations that were sent to the current member account, not including the currently accepted invitation.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_invitations_count()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'InvitationsCount': 123
}


Response Structure

(dict) --
InvitationsCount (integer) --The number of all membership invitations sent to this Security Hub member account, not including the currently accepted invitation.






Exceptions

SecurityHub.Client.exceptions.InternalException
SecurityHub.Client.exceptions.InvalidInputException
SecurityHub.Client.exceptions.InvalidAccessException
SecurityHub.Client.exceptions.LimitExceededException


    :return: {
        'InvitationsCount': 123
    }
    
    
    """
    pass

def get_master_account():
    """
    Provides the details for the Security Hub master account for the current member account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_master_account()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'Master': {
        'AccountId': 'string',
        'InvitationId': 'string',
        'InvitedAt': datetime(2015, 1, 1),
        'MemberStatus': 'string'
    }
}


Response Structure

(dict) --
Master (dict) --A list of details about the Security Hub master account for the current member account.

AccountId (string) --The account ID of the Security Hub master account that the invitation was sent from.

InvitationId (string) --The ID of the invitation sent to the member account.

InvitedAt (datetime) --The timestamp of when the invitation was sent.

MemberStatus (string) --The current status of the association between the member and master accounts.








Exceptions

SecurityHub.Client.exceptions.InternalException
SecurityHub.Client.exceptions.InvalidInputException
SecurityHub.Client.exceptions.InvalidAccessException
SecurityHub.Client.exceptions.LimitExceededException
SecurityHub.Client.exceptions.ResourceNotFoundException


    :return: {
        'Master': {
            'AccountId': 'string',
            'InvitationId': 'string',
            'InvitedAt': datetime(2015, 1, 1),
            'MemberStatus': 'string'
        }
    }
    
    
    """
    pass

def get_members(AccountIds=None):
    """
    Returns the details for the Security Hub member accounts for the specified account IDs.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_members(
        AccountIds=[
            'string',
        ]
    )
    
    
    :type AccountIds: list
    :param AccountIds: [REQUIRED]\nThe list of account IDs for the Security Hub member accounts to return the details for.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'Members': [
        {
            'AccountId': 'string',
            'Email': 'string',
            'MasterId': 'string',
            'MemberStatus': 'string',
            'InvitedAt': datetime(2015, 1, 1),
            'UpdatedAt': datetime(2015, 1, 1)
        },
    ],
    'UnprocessedAccounts': [
        {
            'AccountId': 'string',
            'ProcessingResult': 'string'
        },
    ]
}


Response Structure

(dict) --
Members (list) --The list of details about the Security Hub member accounts.

(dict) --The details about a member account.

AccountId (string) --The AWS account ID of the member account.

Email (string) --The email address of the member account.

MasterId (string) --The AWS account ID of the Security Hub master account associated with this member account.

MemberStatus (string) --The status of the relationship between the member account and its master account.

InvitedAt (datetime) --A timestamp for the date and time when the invitation was sent to the member account.

UpdatedAt (datetime) --The timestamp for the date and time when the member account was updated.





UnprocessedAccounts (list) --The list of AWS accounts that could not be processed. For each account, the list includes the account ID and the email address.

(dict) --Details about the account that was not processed.

AccountId (string) --An AWS account ID of the account that was not processed.

ProcessingResult (string) --The reason that the account was not processed.










Exceptions

SecurityHub.Client.exceptions.InternalException
SecurityHub.Client.exceptions.InvalidInputException
SecurityHub.Client.exceptions.InvalidAccessException
SecurityHub.Client.exceptions.LimitExceededException
SecurityHub.Client.exceptions.ResourceNotFoundException


    :return: {
        'Members': [
            {
                'AccountId': 'string',
                'Email': 'string',
                'MasterId': 'string',
                'MemberStatus': 'string',
                'InvitedAt': datetime(2015, 1, 1),
                'UpdatedAt': datetime(2015, 1, 1)
            },
        ],
        'UnprocessedAccounts': [
            {
                'AccountId': 'string',
                'ProcessingResult': 'string'
            },
        ]
    }
    
    
    :returns: 
    SecurityHub.Client.exceptions.InternalException
    SecurityHub.Client.exceptions.InvalidInputException
    SecurityHub.Client.exceptions.InvalidAccessException
    SecurityHub.Client.exceptions.LimitExceededException
    SecurityHub.Client.exceptions.ResourceNotFoundException
    
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

def invite_members(AccountIds=None):
    """
    Invites other AWS accounts to become member accounts for the Security Hub master account that the invitation is sent from.
    Before you can use this action to invite a member, you must first use the ``  CreateMembers `` action to create the member account in Security Hub.
    When the account owner accepts the invitation to become a member account and enables Security Hub, the master account can view the findings generated from the member account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.invite_members(
        AccountIds=[
            'string',
        ]
    )
    
    
    :type AccountIds: list
    :param AccountIds: The list of account IDs of the AWS accounts to invite to Security Hub as members.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'UnprocessedAccounts': [
        {
            'AccountId': 'string',
            'ProcessingResult': 'string'
        },
    ]
}


Response Structure

(dict) --
UnprocessedAccounts (list) --The list of AWS accounts that could not be processed. For each account, the list includes the account ID and the email address.

(dict) --Details about the account that was not processed.

AccountId (string) --An AWS account ID of the account that was not processed.

ProcessingResult (string) --The reason that the account was not processed.










Exceptions

SecurityHub.Client.exceptions.InternalException
SecurityHub.Client.exceptions.InvalidInputException
SecurityHub.Client.exceptions.InvalidAccessException
SecurityHub.Client.exceptions.LimitExceededException
SecurityHub.Client.exceptions.ResourceNotFoundException


    :return: {
        'UnprocessedAccounts': [
            {
                'AccountId': 'string',
                'ProcessingResult': 'string'
            },
        ]
    }
    
    
    :returns: 
    SecurityHub.Client.exceptions.InternalException
    SecurityHub.Client.exceptions.InvalidInputException
    SecurityHub.Client.exceptions.InvalidAccessException
    SecurityHub.Client.exceptions.LimitExceededException
    SecurityHub.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def list_enabled_products_for_import(NextToken=None, MaxResults=None):
    """
    Lists all findings-generating solutions (products) that you are subscribed to receive findings from in Security Hub.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_enabled_products_for_import(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: The token that is required for pagination. On your first call to the ListEnabledProductsForImport operation, set the value of this parameter to NULL .\nFor subsequent calls to the operation, to continue listing data, set the value of this parameter to the value returned from the previous response.\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return in the response.

    :rtype: dict

ReturnsResponse Syntax
{
    'ProductSubscriptions': [
        'string',
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

ProductSubscriptions (list) --
The list of ARNs for the resources that represent your subscriptions to products.

(string) --


NextToken (string) --
The pagination token to use to request the next page of results.







Exceptions

SecurityHub.Client.exceptions.InternalException
SecurityHub.Client.exceptions.LimitExceededException
SecurityHub.Client.exceptions.InvalidAccessException


    :return: {
        'ProductSubscriptions': [
            'string',
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_invitations(MaxResults=None, NextToken=None):
    """
    Lists all Security Hub membership invitations that were sent to the current AWS account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_invitations(
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return in the response.

    :type NextToken: string
    :param NextToken: The token that is required for pagination. On your first call to the ListInvitations operation, set the value of this parameter to NULL .\nFor subsequent calls to the operation, to continue listing data, set the value of this parameter to the value returned from the previous response.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Invitations': [
        {
            'AccountId': 'string',
            'InvitationId': 'string',
            'InvitedAt': datetime(2015, 1, 1),
            'MemberStatus': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Invitations (list) --
The details of the invitations returned by the operation.

(dict) --
Details about an invitation.

AccountId (string) --
The account ID of the Security Hub master account that the invitation was sent from.

InvitationId (string) --
The ID of the invitation sent to the member account.

InvitedAt (datetime) --
The timestamp of when the invitation was sent.

MemberStatus (string) --
The current status of the association between the member and master accounts.





NextToken (string) --
The pagination token to use to request the next page of results.







Exceptions

SecurityHub.Client.exceptions.InternalException
SecurityHub.Client.exceptions.InvalidInputException
SecurityHub.Client.exceptions.InvalidAccessException
SecurityHub.Client.exceptions.LimitExceededException


    :return: {
        'Invitations': [
            {
                'AccountId': 'string',
                'InvitationId': 'string',
                'InvitedAt': datetime(2015, 1, 1),
                'MemberStatus': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    SecurityHub.Client.exceptions.InternalException
    SecurityHub.Client.exceptions.InvalidInputException
    SecurityHub.Client.exceptions.InvalidAccessException
    SecurityHub.Client.exceptions.LimitExceededException
    
    """
    pass

def list_members(OnlyAssociated=None, MaxResults=None, NextToken=None):
    """
    Lists details about all member accounts for the current Security Hub master account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_members(
        OnlyAssociated=True|False,
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type OnlyAssociated: boolean
    :param OnlyAssociated: Specifies which member accounts to include in the response based on their relationship status with the master account. The default value is TRUE .\nIf OnlyAssociated is set to TRUE , the response includes member accounts whose relationship status with the master is set to ENABLED or DISABLED .\nIf OnlyAssociated is set to FALSE , the response includes all existing member accounts.\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return in the response.

    :type NextToken: string
    :param NextToken: The token that is required for pagination. On your first call to the ListMembers operation, set the value of this parameter to NULL .\nFor subsequent calls to the operation, to continue listing data, set the value of this parameter to the value returned from the previous response.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Members': [
        {
            'AccountId': 'string',
            'Email': 'string',
            'MasterId': 'string',
            'MemberStatus': 'string',
            'InvitedAt': datetime(2015, 1, 1),
            'UpdatedAt': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Members (list) --
Member details returned by the operation.

(dict) --
The details about a member account.

AccountId (string) --
The AWS account ID of the member account.

Email (string) --
The email address of the member account.

MasterId (string) --
The AWS account ID of the Security Hub master account associated with this member account.

MemberStatus (string) --
The status of the relationship between the member account and its master account.

InvitedAt (datetime) --
A timestamp for the date and time when the invitation was sent to the member account.

UpdatedAt (datetime) --
The timestamp for the date and time when the member account was updated.





NextToken (string) --
The pagination token to use to request the next page of results.







Exceptions

SecurityHub.Client.exceptions.InternalException
SecurityHub.Client.exceptions.InvalidInputException
SecurityHub.Client.exceptions.InvalidAccessException
SecurityHub.Client.exceptions.LimitExceededException


    :return: {
        'Members': [
            {
                'AccountId': 'string',
                'Email': 'string',
                'MasterId': 'string',
                'MemberStatus': 'string',
                'InvitedAt': datetime(2015, 1, 1),
                'UpdatedAt': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    SecurityHub.Client.exceptions.InternalException
    SecurityHub.Client.exceptions.InvalidInputException
    SecurityHub.Client.exceptions.InvalidAccessException
    SecurityHub.Client.exceptions.LimitExceededException
    
    """
    pass

def list_tags_for_resource(ResourceArn=None):
    """
    Returns a list of tags associated with a resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        ResourceArn='string'
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe ARN of the resource to retrieve tags for.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --
Tags (dict) --The tags associated with a resource.

(string) --
(string) --









Exceptions

SecurityHub.Client.exceptions.InternalException
SecurityHub.Client.exceptions.InvalidInputException
SecurityHub.Client.exceptions.ResourceNotFoundException


    :return: {
        'Tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    SecurityHub.Client.exceptions.InternalException
    SecurityHub.Client.exceptions.InvalidInputException
    SecurityHub.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def tag_resource(ResourceArn=None, Tags=None):
    """
    Adds one or more tags to a resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        ResourceArn='string',
        Tags={
            'string': 'string'
        }
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe ARN of the resource to apply the tags to.\n

    :type Tags: dict
    :param Tags: [REQUIRED]\nThe tags to add to the resource.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

SecurityHub.Client.exceptions.InternalException
SecurityHub.Client.exceptions.InvalidInputException
SecurityHub.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_resource(ResourceArn=None, TagKeys=None):
    """
    Removes one or more tags from a resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        ResourceArn='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe ARN of the resource to remove the tags from.\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nThe tag keys associated with the tags to remove from the resource.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

SecurityHub.Client.exceptions.InternalException
SecurityHub.Client.exceptions.InvalidInputException
SecurityHub.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_action_target(ActionTargetArn=None, Name=None, Description=None):
    """
    Updates the name and description of a custom action target in Security Hub.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_action_target(
        ActionTargetArn='string',
        Name='string',
        Description='string'
    )
    
    
    :type ActionTargetArn: string
    :param ActionTargetArn: [REQUIRED]\nThe ARN of the custom action target to update.\n

    :type Name: string
    :param Name: The updated name of the custom action target.

    :type Description: string
    :param Description: The updated description for the custom action target.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

SecurityHub.Client.exceptions.InternalException
SecurityHub.Client.exceptions.InvalidInputException
SecurityHub.Client.exceptions.ResourceNotFoundException
SecurityHub.Client.exceptions.InvalidAccessException
SecurityHub.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_findings(Filters=None, Note=None, RecordState=None):
    """
    Updates the Note and RecordState of the Security Hub-aggregated findings that the filter attributes specify. Any member account that can view the finding also sees the update to the finding.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_findings(
        Filters={
            'ProductArn': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'AwsAccountId': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'Id': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'GeneratorId': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'Type': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'FirstObservedAt': [
                {
                    'Start': 'string',
                    'End': 'string',
                    'DateRange': {
                        'Value': 123,
                        'Unit': 'DAYS'
                    }
                },
            ],
            'LastObservedAt': [
                {
                    'Start': 'string',
                    'End': 'string',
                    'DateRange': {
                        'Value': 123,
                        'Unit': 'DAYS'
                    }
                },
            ],
            'CreatedAt': [
                {
                    'Start': 'string',
                    'End': 'string',
                    'DateRange': {
                        'Value': 123,
                        'Unit': 'DAYS'
                    }
                },
            ],
            'UpdatedAt': [
                {
                    'Start': 'string',
                    'End': 'string',
                    'DateRange': {
                        'Value': 123,
                        'Unit': 'DAYS'
                    }
                },
            ],
            'SeverityProduct': [
                {
                    'Gte': 123.0,
                    'Lte': 123.0,
                    'Eq': 123.0
                },
            ],
            'SeverityNormalized': [
                {
                    'Gte': 123.0,
                    'Lte': 123.0,
                    'Eq': 123.0
                },
            ],
            'SeverityLabel': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'Confidence': [
                {
                    'Gte': 123.0,
                    'Lte': 123.0,
                    'Eq': 123.0
                },
            ],
            'Criticality': [
                {
                    'Gte': 123.0,
                    'Lte': 123.0,
                    'Eq': 123.0
                },
            ],
            'Title': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'Description': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'RecommendationText': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'SourceUrl': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ProductFields': [
                {
                    'Key': 'string',
                    'Value': 'string',
                    'Comparison': 'EQUALS'
                },
            ],
            'ProductName': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'CompanyName': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'UserDefinedFields': [
                {
                    'Key': 'string',
                    'Value': 'string',
                    'Comparison': 'EQUALS'
                },
            ],
            'MalwareName': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'MalwareType': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'MalwarePath': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'MalwareState': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'NetworkDirection': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'NetworkProtocol': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'NetworkSourceIpV4': [
                {
                    'Cidr': 'string'
                },
            ],
            'NetworkSourceIpV6': [
                {
                    'Cidr': 'string'
                },
            ],
            'NetworkSourcePort': [
                {
                    'Gte': 123.0,
                    'Lte': 123.0,
                    'Eq': 123.0
                },
            ],
            'NetworkSourceDomain': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'NetworkSourceMac': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'NetworkDestinationIpV4': [
                {
                    'Cidr': 'string'
                },
            ],
            'NetworkDestinationIpV6': [
                {
                    'Cidr': 'string'
                },
            ],
            'NetworkDestinationPort': [
                {
                    'Gte': 123.0,
                    'Lte': 123.0,
                    'Eq': 123.0
                },
            ],
            'NetworkDestinationDomain': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ProcessName': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ProcessPath': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ProcessPid': [
                {
                    'Gte': 123.0,
                    'Lte': 123.0,
                    'Eq': 123.0
                },
            ],
            'ProcessParentPid': [
                {
                    'Gte': 123.0,
                    'Lte': 123.0,
                    'Eq': 123.0
                },
            ],
            'ProcessLaunchedAt': [
                {
                    'Start': 'string',
                    'End': 'string',
                    'DateRange': {
                        'Value': 123,
                        'Unit': 'DAYS'
                    }
                },
            ],
            'ProcessTerminatedAt': [
                {
                    'Start': 'string',
                    'End': 'string',
                    'DateRange': {
                        'Value': 123,
                        'Unit': 'DAYS'
                    }
                },
            ],
            'ThreatIntelIndicatorType': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ThreatIntelIndicatorValue': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ThreatIntelIndicatorCategory': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ThreatIntelIndicatorLastObservedAt': [
                {
                    'Start': 'string',
                    'End': 'string',
                    'DateRange': {
                        'Value': 123,
                        'Unit': 'DAYS'
                    }
                },
            ],
            'ThreatIntelIndicatorSource': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ThreatIntelIndicatorSourceUrl': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceType': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceId': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourcePartition': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceRegion': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceTags': [
                {
                    'Key': 'string',
                    'Value': 'string',
                    'Comparison': 'EQUALS'
                },
            ],
            'ResourceAwsEc2InstanceType': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceAwsEc2InstanceImageId': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceAwsEc2InstanceIpV4Addresses': [
                {
                    'Cidr': 'string'
                },
            ],
            'ResourceAwsEc2InstanceIpV6Addresses': [
                {
                    'Cidr': 'string'
                },
            ],
            'ResourceAwsEc2InstanceKeyName': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceAwsEc2InstanceIamInstanceProfileArn': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceAwsEc2InstanceVpcId': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceAwsEc2InstanceSubnetId': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceAwsEc2InstanceLaunchedAt': [
                {
                    'Start': 'string',
                    'End': 'string',
                    'DateRange': {
                        'Value': 123,
                        'Unit': 'DAYS'
                    }
                },
            ],
            'ResourceAwsS3BucketOwnerId': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceAwsS3BucketOwnerName': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceAwsIamAccessKeyUserName': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceAwsIamAccessKeyStatus': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceAwsIamAccessKeyCreatedAt': [
                {
                    'Start': 'string',
                    'End': 'string',
                    'DateRange': {
                        'Value': 123,
                        'Unit': 'DAYS'
                    }
                },
            ],
            'ResourceContainerName': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceContainerImageId': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceContainerImageName': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceContainerLaunchedAt': [
                {
                    'Start': 'string',
                    'End': 'string',
                    'DateRange': {
                        'Value': 123,
                        'Unit': 'DAYS'
                    }
                },
            ],
            'ResourceDetailsOther': [
                {
                    'Key': 'string',
                    'Value': 'string',
                    'Comparison': 'EQUALS'
                },
            ],
            'ComplianceStatus': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'VerificationState': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'WorkflowState': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'WorkflowStatus': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'RecordState': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'RelatedFindingsProductArn': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'RelatedFindingsId': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'NoteText': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'NoteUpdatedAt': [
                {
                    'Start': 'string',
                    'End': 'string',
                    'DateRange': {
                        'Value': 123,
                        'Unit': 'DAYS'
                    }
                },
            ],
            'NoteUpdatedBy': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'Keyword': [
                {
                    'Value': 'string'
                },
            ]
        },
        Note={
            'Text': 'string',
            'UpdatedBy': 'string'
        },
        RecordState='ACTIVE'|'ARCHIVED'
    )
    
    
    :type Filters: dict
    :param Filters: [REQUIRED]\nA collection of attributes that specify which findings you want to update.\n\nProductArn (list) --The ARN generated by Security Hub that uniquely identifies a third-party company (security findings provider) after this provider\'s product (solution that generates findings) is registered with Security Hub.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nAwsAccountId (list) --The AWS account ID that a finding is generated in.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nId (list) --The security findings provider-specific identifier for a finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nGeneratorId (list) --The identifier for the solution-specific component (a discrete unit of logic) that generated a finding. In various security-findings providers\' solutions, this generator can be called a rule, a check, a detector, a plugin, etc.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nType (list) --A finding type in the format of namespace/category/classifier that classifies a finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nFirstObservedAt (list) --An ISO8601-formatted timestamp that indicates when the security-findings provider first observed the potential security issue that a finding captured.\n\n(dict) --A date filter for querying findings.\n\nStart (string) --A start date for the date filter.\n\nEnd (string) --An end date for the date filter.\n\nDateRange (dict) --A date range for the date filter.\n\nValue (integer) --A date range value for the date filter.\n\nUnit (string) --A date range unit for the date filter.\n\n\n\n\n\n\n\nLastObservedAt (list) --An ISO8601-formatted timestamp that indicates when the security-findings provider most recently observed the potential security issue that a finding captured.\n\n(dict) --A date filter for querying findings.\n\nStart (string) --A start date for the date filter.\n\nEnd (string) --An end date for the date filter.\n\nDateRange (dict) --A date range for the date filter.\n\nValue (integer) --A date range value for the date filter.\n\nUnit (string) --A date range unit for the date filter.\n\n\n\n\n\n\n\nCreatedAt (list) --An ISO8601-formatted timestamp that indicates when the security-findings provider captured the potential security issue that a finding captured.\n\n(dict) --A date filter for querying findings.\n\nStart (string) --A start date for the date filter.\n\nEnd (string) --An end date for the date filter.\n\nDateRange (dict) --A date range for the date filter.\n\nValue (integer) --A date range value for the date filter.\n\nUnit (string) --A date range unit for the date filter.\n\n\n\n\n\n\n\nUpdatedAt (list) --An ISO8601-formatted timestamp that indicates when the security-findings provider last updated the finding record.\n\n(dict) --A date filter for querying findings.\n\nStart (string) --A start date for the date filter.\n\nEnd (string) --An end date for the date filter.\n\nDateRange (dict) --A date range for the date filter.\n\nValue (integer) --A date range value for the date filter.\n\nUnit (string) --A date range unit for the date filter.\n\n\n\n\n\n\n\nSeverityProduct (list) --The native severity as defined by the security-findings provider\'s solution that generated the finding.\n\n(dict) --A number filter for querying findings.\n\nGte (float) --The greater-than-equal condition to be applied to a single field when querying for findings.\n\nLte (float) --The less-than-equal condition to be applied to a single field when querying for findings.\n\nEq (float) --The equal-to condition to be applied to a single field when querying for findings.\n\n\n\n\n\nSeverityNormalized (list) --The normalized severity of a finding.\n\n(dict) --A number filter for querying findings.\n\nGte (float) --The greater-than-equal condition to be applied to a single field when querying for findings.\n\nLte (float) --The less-than-equal condition to be applied to a single field when querying for findings.\n\nEq (float) --The equal-to condition to be applied to a single field when querying for findings.\n\n\n\n\n\nSeverityLabel (list) --The label of a finding\'s severity.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nConfidence (list) --A finding\'s confidence. Confidence is defined as the likelihood that a finding accurately identifies the behavior or issue that it was intended to identify.\nConfidence is scored on a 0-100 basis using a ratio scale, where 0 means zero percent confidence and 100 means 100 percent confidence.\n\n(dict) --A number filter for querying findings.\n\nGte (float) --The greater-than-equal condition to be applied to a single field when querying for findings.\n\nLte (float) --The less-than-equal condition to be applied to a single field when querying for findings.\n\nEq (float) --The equal-to condition to be applied to a single field when querying for findings.\n\n\n\n\n\nCriticality (list) --The level of importance assigned to the resources associated with the finding.\nA score of 0 means that the underlying resources have no criticality, and a score of 100 is reserved for the most critical resources.\n\n(dict) --A number filter for querying findings.\n\nGte (float) --The greater-than-equal condition to be applied to a single field when querying for findings.\n\nLte (float) --The less-than-equal condition to be applied to a single field when querying for findings.\n\nEq (float) --The equal-to condition to be applied to a single field when querying for findings.\n\n\n\n\n\nTitle (list) --A finding\'s title.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nDescription (list) --A finding\'s description.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nRecommendationText (list) --The recommendation of what to do about the issue described in a finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nSourceUrl (list) --A URL that links to a page about the current finding in the security-findings provider\'s solution.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nProductFields (list) --A data type where security-findings providers can include additional solution-specific details that aren\'t part of the defined AwsSecurityFinding format.\n\n(dict) --The map filter for querying findings.\n\nKey (string) --The key of the map filter.\n\nValue (string) --The value for the key in the map filter.\n\nComparison (string) --The condition to apply to a key value when querying for findings with a map filter.\n\n\n\n\n\nProductName (list) --The name of the solution (product) that generates findings.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nCompanyName (list) --The name of the findings provider (company) that owns the solution (product) that generates findings.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nUserDefinedFields (list) --A list of name/value string pairs associated with the finding. These are custom, user-defined fields added to a finding.\n\n(dict) --The map filter for querying findings.\n\nKey (string) --The key of the map filter.\n\nValue (string) --The value for the key in the map filter.\n\nComparison (string) --The condition to apply to a key value when querying for findings with a map filter.\n\n\n\n\n\nMalwareName (list) --The name of the malware that was observed.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nMalwareType (list) --The type of the malware that was observed.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nMalwarePath (list) --The filesystem path of the malware that was observed.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nMalwareState (list) --The state of the malware that was observed.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nNetworkDirection (list) --Indicates the direction of network traffic associated with a finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nNetworkProtocol (list) --The protocol of network-related information about a finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nNetworkSourceIpV4 (list) --The source IPv4 address of network-related information about a finding.\n\n(dict) --The IP filter for querying findings.\n\nCidr (string) --A finding\'s CIDR value.\n\n\n\n\n\nNetworkSourceIpV6 (list) --The source IPv6 address of network-related information about a finding.\n\n(dict) --The IP filter for querying findings.\n\nCidr (string) --A finding\'s CIDR value.\n\n\n\n\n\nNetworkSourcePort (list) --The source port of network-related information about a finding.\n\n(dict) --A number filter for querying findings.\n\nGte (float) --The greater-than-equal condition to be applied to a single field when querying for findings.\n\nLte (float) --The less-than-equal condition to be applied to a single field when querying for findings.\n\nEq (float) --The equal-to condition to be applied to a single field when querying for findings.\n\n\n\n\n\nNetworkSourceDomain (list) --The source domain of network-related information about a finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nNetworkSourceMac (list) --The source media access control (MAC) address of network-related information about a finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nNetworkDestinationIpV4 (list) --The destination IPv4 address of network-related information about a finding.\n\n(dict) --The IP filter for querying findings.\n\nCidr (string) --A finding\'s CIDR value.\n\n\n\n\n\nNetworkDestinationIpV6 (list) --The destination IPv6 address of network-related information about a finding.\n\n(dict) --The IP filter for querying findings.\n\nCidr (string) --A finding\'s CIDR value.\n\n\n\n\n\nNetworkDestinationPort (list) --The destination port of network-related information about a finding.\n\n(dict) --A number filter for querying findings.\n\nGte (float) --The greater-than-equal condition to be applied to a single field when querying for findings.\n\nLte (float) --The less-than-equal condition to be applied to a single field when querying for findings.\n\nEq (float) --The equal-to condition to be applied to a single field when querying for findings.\n\n\n\n\n\nNetworkDestinationDomain (list) --The destination domain of network-related information about a finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nProcessName (list) --The name of the process.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nProcessPath (list) --The path to the process executable.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nProcessPid (list) --The process ID.\n\n(dict) --A number filter for querying findings.\n\nGte (float) --The greater-than-equal condition to be applied to a single field when querying for findings.\n\nLte (float) --The less-than-equal condition to be applied to a single field when querying for findings.\n\nEq (float) --The equal-to condition to be applied to a single field when querying for findings.\n\n\n\n\n\nProcessParentPid (list) --The parent process ID.\n\n(dict) --A number filter for querying findings.\n\nGte (float) --The greater-than-equal condition to be applied to a single field when querying for findings.\n\nLte (float) --The less-than-equal condition to be applied to a single field when querying for findings.\n\nEq (float) --The equal-to condition to be applied to a single field when querying for findings.\n\n\n\n\n\nProcessLaunchedAt (list) --The date/time that the process was launched.\n\n(dict) --A date filter for querying findings.\n\nStart (string) --A start date for the date filter.\n\nEnd (string) --An end date for the date filter.\n\nDateRange (dict) --A date range for the date filter.\n\nValue (integer) --A date range value for the date filter.\n\nUnit (string) --A date range unit for the date filter.\n\n\n\n\n\n\n\nProcessTerminatedAt (list) --The date/time that the process was terminated.\n\n(dict) --A date filter for querying findings.\n\nStart (string) --A start date for the date filter.\n\nEnd (string) --An end date for the date filter.\n\nDateRange (dict) --A date range for the date filter.\n\nValue (integer) --A date range value for the date filter.\n\nUnit (string) --A date range unit for the date filter.\n\n\n\n\n\n\n\nThreatIntelIndicatorType (list) --The type of a threat intelligence indicator.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nThreatIntelIndicatorValue (list) --The value of a threat intelligence indicator.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nThreatIntelIndicatorCategory (list) --The category of a threat intelligence indicator.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nThreatIntelIndicatorLastObservedAt (list) --The date/time of the last observation of a threat intelligence indicator.\n\n(dict) --A date filter for querying findings.\n\nStart (string) --A start date for the date filter.\n\nEnd (string) --An end date for the date filter.\n\nDateRange (dict) --A date range for the date filter.\n\nValue (integer) --A date range value for the date filter.\n\nUnit (string) --A date range unit for the date filter.\n\n\n\n\n\n\n\nThreatIntelIndicatorSource (list) --The source of the threat intelligence.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nThreatIntelIndicatorSourceUrl (list) --The URL for more details from the source of the threat intelligence.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceType (list) --Specifies the type of the resource that details are provided for.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceId (list) --The canonical identifier for the given resource type.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourcePartition (list) --The canonical AWS partition name that the Region is assigned to.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceRegion (list) --The canonical AWS external Region name where this resource is located.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceTags (list) --A list of AWS tags associated with a resource at the time the finding was processed.\n\n(dict) --The map filter for querying findings.\n\nKey (string) --The key of the map filter.\n\nValue (string) --The value for the key in the map filter.\n\nComparison (string) --The condition to apply to a key value when querying for findings with a map filter.\n\n\n\n\n\nResourceAwsEc2InstanceType (list) --The instance type of the instance.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceAwsEc2InstanceImageId (list) --The Amazon Machine Image (AMI) ID of the instance.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceAwsEc2InstanceIpV4Addresses (list) --The IPv4 addresses associated with the instance.\n\n(dict) --The IP filter for querying findings.\n\nCidr (string) --A finding\'s CIDR value.\n\n\n\n\n\nResourceAwsEc2InstanceIpV6Addresses (list) --The IPv6 addresses associated with the instance.\n\n(dict) --The IP filter for querying findings.\n\nCidr (string) --A finding\'s CIDR value.\n\n\n\n\n\nResourceAwsEc2InstanceKeyName (list) --The key name associated with the instance.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceAwsEc2InstanceIamInstanceProfileArn (list) --The IAM profile ARN of the instance.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceAwsEc2InstanceVpcId (list) --The identifier of the VPC that the instance was launched in.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceAwsEc2InstanceSubnetId (list) --The identifier of the subnet that the instance was launched in.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceAwsEc2InstanceLaunchedAt (list) --The date and time the instance was launched.\n\n(dict) --A date filter for querying findings.\n\nStart (string) --A start date for the date filter.\n\nEnd (string) --An end date for the date filter.\n\nDateRange (dict) --A date range for the date filter.\n\nValue (integer) --A date range value for the date filter.\n\nUnit (string) --A date range unit for the date filter.\n\n\n\n\n\n\n\nResourceAwsS3BucketOwnerId (list) --The canonical user ID of the owner of the S3 bucket.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceAwsS3BucketOwnerName (list) --The display name of the owner of the S3 bucket.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceAwsIamAccessKeyUserName (list) --The user associated with the IAM access key related to a finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceAwsIamAccessKeyStatus (list) --The status of the IAM access key related to a finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceAwsIamAccessKeyCreatedAt (list) --The creation date/time of the IAM access key related to a finding.\n\n(dict) --A date filter for querying findings.\n\nStart (string) --A start date for the date filter.\n\nEnd (string) --An end date for the date filter.\n\nDateRange (dict) --A date range for the date filter.\n\nValue (integer) --A date range value for the date filter.\n\nUnit (string) --A date range unit for the date filter.\n\n\n\n\n\n\n\nResourceContainerName (list) --The name of the container related to a finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceContainerImageId (list) --The identifier of the image related to a finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceContainerImageName (list) --The name of the image related to a finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceContainerLaunchedAt (list) --The date/time that the container was started.\n\n(dict) --A date filter for querying findings.\n\nStart (string) --A start date for the date filter.\n\nEnd (string) --An end date for the date filter.\n\nDateRange (dict) --A date range for the date filter.\n\nValue (integer) --A date range value for the date filter.\n\nUnit (string) --A date range unit for the date filter.\n\n\n\n\n\n\n\nResourceDetailsOther (list) --The details of a resource that doesn\'t have a specific subfield for the resource type defined.\n\n(dict) --The map filter for querying findings.\n\nKey (string) --The key of the map filter.\n\nValue (string) --The value for the key in the map filter.\n\nComparison (string) --The condition to apply to a key value when querying for findings with a map filter.\n\n\n\n\n\nComplianceStatus (list) --Exclusive to findings that are generated as the result of a check run against a specific rule in a supported standard, such as CIS AWS Foundations. Contains security standard-related finding details.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nVerificationState (list) --The veracity of a finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nWorkflowState (list) --The workflow state of a finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nWorkflowStatus (list) --The status of the investigation into a finding. Allowed values are the following.\n\nNEW - The initial state of a finding, before it is reviewed.\nNOTIFIED - Indicates that the resource owner has been notified about the security issue. Used when the initial reviewer is not the resource owner, and needs intervention from the resource owner.\nSUPPRESSED - The finding will not be reviewed again and will not be acted upon.\nRESOLVED - The finding was reviewed and remediated and is now considered resolved.\n\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nRecordState (list) --The updated record state for the finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nRelatedFindingsProductArn (list) --The ARN of the solution that generated a related finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nRelatedFindingsId (list) --The solution-generated identifier for a related finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nNoteText (list) --The text of a note.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nNoteUpdatedAt (list) --The timestamp of when the note was updated.\n\n(dict) --A date filter for querying findings.\n\nStart (string) --A start date for the date filter.\n\nEnd (string) --An end date for the date filter.\n\nDateRange (dict) --A date range for the date filter.\n\nValue (integer) --A date range value for the date filter.\n\nUnit (string) --A date range unit for the date filter.\n\n\n\n\n\n\n\nNoteUpdatedBy (list) --The principal that created a note.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nKeyword (list) --A keyword for a finding.\n\n(dict) --A keyword filter for querying findings.\n\nValue (string) --A value for the keyword.\n\n\n\n\n\n\n

    :type Note: dict
    :param Note: The updated note for the finding.\n\nText (string) -- [REQUIRED]The updated note text.\n\nUpdatedBy (string) -- [REQUIRED]The principal that updated the note.\n\n\n

    :type RecordState: string
    :param RecordState: The updated record state for the finding.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

SecurityHub.Client.exceptions.InternalException
SecurityHub.Client.exceptions.InvalidInputException
SecurityHub.Client.exceptions.LimitExceededException
SecurityHub.Client.exceptions.InvalidAccessException
SecurityHub.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_insight(InsightArn=None, Name=None, Filters=None, GroupByAttribute=None):
    """
    Updates the Security Hub insight identified by the specified insight ARN.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_insight(
        InsightArn='string',
        Name='string',
        Filters={
            'ProductArn': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'AwsAccountId': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'Id': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'GeneratorId': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'Type': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'FirstObservedAt': [
                {
                    'Start': 'string',
                    'End': 'string',
                    'DateRange': {
                        'Value': 123,
                        'Unit': 'DAYS'
                    }
                },
            ],
            'LastObservedAt': [
                {
                    'Start': 'string',
                    'End': 'string',
                    'DateRange': {
                        'Value': 123,
                        'Unit': 'DAYS'
                    }
                },
            ],
            'CreatedAt': [
                {
                    'Start': 'string',
                    'End': 'string',
                    'DateRange': {
                        'Value': 123,
                        'Unit': 'DAYS'
                    }
                },
            ],
            'UpdatedAt': [
                {
                    'Start': 'string',
                    'End': 'string',
                    'DateRange': {
                        'Value': 123,
                        'Unit': 'DAYS'
                    }
                },
            ],
            'SeverityProduct': [
                {
                    'Gte': 123.0,
                    'Lte': 123.0,
                    'Eq': 123.0
                },
            ],
            'SeverityNormalized': [
                {
                    'Gte': 123.0,
                    'Lte': 123.0,
                    'Eq': 123.0
                },
            ],
            'SeverityLabel': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'Confidence': [
                {
                    'Gte': 123.0,
                    'Lte': 123.0,
                    'Eq': 123.0
                },
            ],
            'Criticality': [
                {
                    'Gte': 123.0,
                    'Lte': 123.0,
                    'Eq': 123.0
                },
            ],
            'Title': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'Description': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'RecommendationText': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'SourceUrl': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ProductFields': [
                {
                    'Key': 'string',
                    'Value': 'string',
                    'Comparison': 'EQUALS'
                },
            ],
            'ProductName': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'CompanyName': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'UserDefinedFields': [
                {
                    'Key': 'string',
                    'Value': 'string',
                    'Comparison': 'EQUALS'
                },
            ],
            'MalwareName': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'MalwareType': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'MalwarePath': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'MalwareState': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'NetworkDirection': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'NetworkProtocol': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'NetworkSourceIpV4': [
                {
                    'Cidr': 'string'
                },
            ],
            'NetworkSourceIpV6': [
                {
                    'Cidr': 'string'
                },
            ],
            'NetworkSourcePort': [
                {
                    'Gte': 123.0,
                    'Lte': 123.0,
                    'Eq': 123.0
                },
            ],
            'NetworkSourceDomain': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'NetworkSourceMac': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'NetworkDestinationIpV4': [
                {
                    'Cidr': 'string'
                },
            ],
            'NetworkDestinationIpV6': [
                {
                    'Cidr': 'string'
                },
            ],
            'NetworkDestinationPort': [
                {
                    'Gte': 123.0,
                    'Lte': 123.0,
                    'Eq': 123.0
                },
            ],
            'NetworkDestinationDomain': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ProcessName': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ProcessPath': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ProcessPid': [
                {
                    'Gte': 123.0,
                    'Lte': 123.0,
                    'Eq': 123.0
                },
            ],
            'ProcessParentPid': [
                {
                    'Gte': 123.0,
                    'Lte': 123.0,
                    'Eq': 123.0
                },
            ],
            'ProcessLaunchedAt': [
                {
                    'Start': 'string',
                    'End': 'string',
                    'DateRange': {
                        'Value': 123,
                        'Unit': 'DAYS'
                    }
                },
            ],
            'ProcessTerminatedAt': [
                {
                    'Start': 'string',
                    'End': 'string',
                    'DateRange': {
                        'Value': 123,
                        'Unit': 'DAYS'
                    }
                },
            ],
            'ThreatIntelIndicatorType': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ThreatIntelIndicatorValue': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ThreatIntelIndicatorCategory': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ThreatIntelIndicatorLastObservedAt': [
                {
                    'Start': 'string',
                    'End': 'string',
                    'DateRange': {
                        'Value': 123,
                        'Unit': 'DAYS'
                    }
                },
            ],
            'ThreatIntelIndicatorSource': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ThreatIntelIndicatorSourceUrl': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceType': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceId': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourcePartition': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceRegion': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceTags': [
                {
                    'Key': 'string',
                    'Value': 'string',
                    'Comparison': 'EQUALS'
                },
            ],
            'ResourceAwsEc2InstanceType': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceAwsEc2InstanceImageId': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceAwsEc2InstanceIpV4Addresses': [
                {
                    'Cidr': 'string'
                },
            ],
            'ResourceAwsEc2InstanceIpV6Addresses': [
                {
                    'Cidr': 'string'
                },
            ],
            'ResourceAwsEc2InstanceKeyName': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceAwsEc2InstanceIamInstanceProfileArn': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceAwsEc2InstanceVpcId': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceAwsEc2InstanceSubnetId': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceAwsEc2InstanceLaunchedAt': [
                {
                    'Start': 'string',
                    'End': 'string',
                    'DateRange': {
                        'Value': 123,
                        'Unit': 'DAYS'
                    }
                },
            ],
            'ResourceAwsS3BucketOwnerId': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceAwsS3BucketOwnerName': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceAwsIamAccessKeyUserName': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceAwsIamAccessKeyStatus': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceAwsIamAccessKeyCreatedAt': [
                {
                    'Start': 'string',
                    'End': 'string',
                    'DateRange': {
                        'Value': 123,
                        'Unit': 'DAYS'
                    }
                },
            ],
            'ResourceContainerName': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceContainerImageId': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceContainerImageName': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'ResourceContainerLaunchedAt': [
                {
                    'Start': 'string',
                    'End': 'string',
                    'DateRange': {
                        'Value': 123,
                        'Unit': 'DAYS'
                    }
                },
            ],
            'ResourceDetailsOther': [
                {
                    'Key': 'string',
                    'Value': 'string',
                    'Comparison': 'EQUALS'
                },
            ],
            'ComplianceStatus': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'VerificationState': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'WorkflowState': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'WorkflowStatus': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'RecordState': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'RelatedFindingsProductArn': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'RelatedFindingsId': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'NoteText': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'NoteUpdatedAt': [
                {
                    'Start': 'string',
                    'End': 'string',
                    'DateRange': {
                        'Value': 123,
                        'Unit': 'DAYS'
                    }
                },
            ],
            'NoteUpdatedBy': [
                {
                    'Value': 'string',
                    'Comparison': 'EQUALS'|'PREFIX'
                },
            ],
            'Keyword': [
                {
                    'Value': 'string'
                },
            ]
        },
        GroupByAttribute='string'
    )
    
    
    :type InsightArn: string
    :param InsightArn: [REQUIRED]\nThe ARN of the insight that you want to update.\n

    :type Name: string
    :param Name: The updated name for the insight.

    :type Filters: dict
    :param Filters: The updated filters that define this insight.\n\nProductArn (list) --The ARN generated by Security Hub that uniquely identifies a third-party company (security findings provider) after this provider\'s product (solution that generates findings) is registered with Security Hub.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nAwsAccountId (list) --The AWS account ID that a finding is generated in.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nId (list) --The security findings provider-specific identifier for a finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nGeneratorId (list) --The identifier for the solution-specific component (a discrete unit of logic) that generated a finding. In various security-findings providers\' solutions, this generator can be called a rule, a check, a detector, a plugin, etc.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nType (list) --A finding type in the format of namespace/category/classifier that classifies a finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nFirstObservedAt (list) --An ISO8601-formatted timestamp that indicates when the security-findings provider first observed the potential security issue that a finding captured.\n\n(dict) --A date filter for querying findings.\n\nStart (string) --A start date for the date filter.\n\nEnd (string) --An end date for the date filter.\n\nDateRange (dict) --A date range for the date filter.\n\nValue (integer) --A date range value for the date filter.\n\nUnit (string) --A date range unit for the date filter.\n\n\n\n\n\n\n\nLastObservedAt (list) --An ISO8601-formatted timestamp that indicates when the security-findings provider most recently observed the potential security issue that a finding captured.\n\n(dict) --A date filter for querying findings.\n\nStart (string) --A start date for the date filter.\n\nEnd (string) --An end date for the date filter.\n\nDateRange (dict) --A date range for the date filter.\n\nValue (integer) --A date range value for the date filter.\n\nUnit (string) --A date range unit for the date filter.\n\n\n\n\n\n\n\nCreatedAt (list) --An ISO8601-formatted timestamp that indicates when the security-findings provider captured the potential security issue that a finding captured.\n\n(dict) --A date filter for querying findings.\n\nStart (string) --A start date for the date filter.\n\nEnd (string) --An end date for the date filter.\n\nDateRange (dict) --A date range for the date filter.\n\nValue (integer) --A date range value for the date filter.\n\nUnit (string) --A date range unit for the date filter.\n\n\n\n\n\n\n\nUpdatedAt (list) --An ISO8601-formatted timestamp that indicates when the security-findings provider last updated the finding record.\n\n(dict) --A date filter for querying findings.\n\nStart (string) --A start date for the date filter.\n\nEnd (string) --An end date for the date filter.\n\nDateRange (dict) --A date range for the date filter.\n\nValue (integer) --A date range value for the date filter.\n\nUnit (string) --A date range unit for the date filter.\n\n\n\n\n\n\n\nSeverityProduct (list) --The native severity as defined by the security-findings provider\'s solution that generated the finding.\n\n(dict) --A number filter for querying findings.\n\nGte (float) --The greater-than-equal condition to be applied to a single field when querying for findings.\n\nLte (float) --The less-than-equal condition to be applied to a single field when querying for findings.\n\nEq (float) --The equal-to condition to be applied to a single field when querying for findings.\n\n\n\n\n\nSeverityNormalized (list) --The normalized severity of a finding.\n\n(dict) --A number filter for querying findings.\n\nGte (float) --The greater-than-equal condition to be applied to a single field when querying for findings.\n\nLte (float) --The less-than-equal condition to be applied to a single field when querying for findings.\n\nEq (float) --The equal-to condition to be applied to a single field when querying for findings.\n\n\n\n\n\nSeverityLabel (list) --The label of a finding\'s severity.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nConfidence (list) --A finding\'s confidence. Confidence is defined as the likelihood that a finding accurately identifies the behavior or issue that it was intended to identify.\nConfidence is scored on a 0-100 basis using a ratio scale, where 0 means zero percent confidence and 100 means 100 percent confidence.\n\n(dict) --A number filter for querying findings.\n\nGte (float) --The greater-than-equal condition to be applied to a single field when querying for findings.\n\nLte (float) --The less-than-equal condition to be applied to a single field when querying for findings.\n\nEq (float) --The equal-to condition to be applied to a single field when querying for findings.\n\n\n\n\n\nCriticality (list) --The level of importance assigned to the resources associated with the finding.\nA score of 0 means that the underlying resources have no criticality, and a score of 100 is reserved for the most critical resources.\n\n(dict) --A number filter for querying findings.\n\nGte (float) --The greater-than-equal condition to be applied to a single field when querying for findings.\n\nLte (float) --The less-than-equal condition to be applied to a single field when querying for findings.\n\nEq (float) --The equal-to condition to be applied to a single field when querying for findings.\n\n\n\n\n\nTitle (list) --A finding\'s title.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nDescription (list) --A finding\'s description.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nRecommendationText (list) --The recommendation of what to do about the issue described in a finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nSourceUrl (list) --A URL that links to a page about the current finding in the security-findings provider\'s solution.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nProductFields (list) --A data type where security-findings providers can include additional solution-specific details that aren\'t part of the defined AwsSecurityFinding format.\n\n(dict) --The map filter for querying findings.\n\nKey (string) --The key of the map filter.\n\nValue (string) --The value for the key in the map filter.\n\nComparison (string) --The condition to apply to a key value when querying for findings with a map filter.\n\n\n\n\n\nProductName (list) --The name of the solution (product) that generates findings.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nCompanyName (list) --The name of the findings provider (company) that owns the solution (product) that generates findings.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nUserDefinedFields (list) --A list of name/value string pairs associated with the finding. These are custom, user-defined fields added to a finding.\n\n(dict) --The map filter for querying findings.\n\nKey (string) --The key of the map filter.\n\nValue (string) --The value for the key in the map filter.\n\nComparison (string) --The condition to apply to a key value when querying for findings with a map filter.\n\n\n\n\n\nMalwareName (list) --The name of the malware that was observed.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nMalwareType (list) --The type of the malware that was observed.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nMalwarePath (list) --The filesystem path of the malware that was observed.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nMalwareState (list) --The state of the malware that was observed.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nNetworkDirection (list) --Indicates the direction of network traffic associated with a finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nNetworkProtocol (list) --The protocol of network-related information about a finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nNetworkSourceIpV4 (list) --The source IPv4 address of network-related information about a finding.\n\n(dict) --The IP filter for querying findings.\n\nCidr (string) --A finding\'s CIDR value.\n\n\n\n\n\nNetworkSourceIpV6 (list) --The source IPv6 address of network-related information about a finding.\n\n(dict) --The IP filter for querying findings.\n\nCidr (string) --A finding\'s CIDR value.\n\n\n\n\n\nNetworkSourcePort (list) --The source port of network-related information about a finding.\n\n(dict) --A number filter for querying findings.\n\nGte (float) --The greater-than-equal condition to be applied to a single field when querying for findings.\n\nLte (float) --The less-than-equal condition to be applied to a single field when querying for findings.\n\nEq (float) --The equal-to condition to be applied to a single field when querying for findings.\n\n\n\n\n\nNetworkSourceDomain (list) --The source domain of network-related information about a finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nNetworkSourceMac (list) --The source media access control (MAC) address of network-related information about a finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nNetworkDestinationIpV4 (list) --The destination IPv4 address of network-related information about a finding.\n\n(dict) --The IP filter for querying findings.\n\nCidr (string) --A finding\'s CIDR value.\n\n\n\n\n\nNetworkDestinationIpV6 (list) --The destination IPv6 address of network-related information about a finding.\n\n(dict) --The IP filter for querying findings.\n\nCidr (string) --A finding\'s CIDR value.\n\n\n\n\n\nNetworkDestinationPort (list) --The destination port of network-related information about a finding.\n\n(dict) --A number filter for querying findings.\n\nGte (float) --The greater-than-equal condition to be applied to a single field when querying for findings.\n\nLte (float) --The less-than-equal condition to be applied to a single field when querying for findings.\n\nEq (float) --The equal-to condition to be applied to a single field when querying for findings.\n\n\n\n\n\nNetworkDestinationDomain (list) --The destination domain of network-related information about a finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nProcessName (list) --The name of the process.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nProcessPath (list) --The path to the process executable.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nProcessPid (list) --The process ID.\n\n(dict) --A number filter for querying findings.\n\nGte (float) --The greater-than-equal condition to be applied to a single field when querying for findings.\n\nLte (float) --The less-than-equal condition to be applied to a single field when querying for findings.\n\nEq (float) --The equal-to condition to be applied to a single field when querying for findings.\n\n\n\n\n\nProcessParentPid (list) --The parent process ID.\n\n(dict) --A number filter for querying findings.\n\nGte (float) --The greater-than-equal condition to be applied to a single field when querying for findings.\n\nLte (float) --The less-than-equal condition to be applied to a single field when querying for findings.\n\nEq (float) --The equal-to condition to be applied to a single field when querying for findings.\n\n\n\n\n\nProcessLaunchedAt (list) --The date/time that the process was launched.\n\n(dict) --A date filter for querying findings.\n\nStart (string) --A start date for the date filter.\n\nEnd (string) --An end date for the date filter.\n\nDateRange (dict) --A date range for the date filter.\n\nValue (integer) --A date range value for the date filter.\n\nUnit (string) --A date range unit for the date filter.\n\n\n\n\n\n\n\nProcessTerminatedAt (list) --The date/time that the process was terminated.\n\n(dict) --A date filter for querying findings.\n\nStart (string) --A start date for the date filter.\n\nEnd (string) --An end date for the date filter.\n\nDateRange (dict) --A date range for the date filter.\n\nValue (integer) --A date range value for the date filter.\n\nUnit (string) --A date range unit for the date filter.\n\n\n\n\n\n\n\nThreatIntelIndicatorType (list) --The type of a threat intelligence indicator.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nThreatIntelIndicatorValue (list) --The value of a threat intelligence indicator.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nThreatIntelIndicatorCategory (list) --The category of a threat intelligence indicator.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nThreatIntelIndicatorLastObservedAt (list) --The date/time of the last observation of a threat intelligence indicator.\n\n(dict) --A date filter for querying findings.\n\nStart (string) --A start date for the date filter.\n\nEnd (string) --An end date for the date filter.\n\nDateRange (dict) --A date range for the date filter.\n\nValue (integer) --A date range value for the date filter.\n\nUnit (string) --A date range unit for the date filter.\n\n\n\n\n\n\n\nThreatIntelIndicatorSource (list) --The source of the threat intelligence.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nThreatIntelIndicatorSourceUrl (list) --The URL for more details from the source of the threat intelligence.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceType (list) --Specifies the type of the resource that details are provided for.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceId (list) --The canonical identifier for the given resource type.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourcePartition (list) --The canonical AWS partition name that the Region is assigned to.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceRegion (list) --The canonical AWS external Region name where this resource is located.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceTags (list) --A list of AWS tags associated with a resource at the time the finding was processed.\n\n(dict) --The map filter for querying findings.\n\nKey (string) --The key of the map filter.\n\nValue (string) --The value for the key in the map filter.\n\nComparison (string) --The condition to apply to a key value when querying for findings with a map filter.\n\n\n\n\n\nResourceAwsEc2InstanceType (list) --The instance type of the instance.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceAwsEc2InstanceImageId (list) --The Amazon Machine Image (AMI) ID of the instance.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceAwsEc2InstanceIpV4Addresses (list) --The IPv4 addresses associated with the instance.\n\n(dict) --The IP filter for querying findings.\n\nCidr (string) --A finding\'s CIDR value.\n\n\n\n\n\nResourceAwsEc2InstanceIpV6Addresses (list) --The IPv6 addresses associated with the instance.\n\n(dict) --The IP filter for querying findings.\n\nCidr (string) --A finding\'s CIDR value.\n\n\n\n\n\nResourceAwsEc2InstanceKeyName (list) --The key name associated with the instance.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceAwsEc2InstanceIamInstanceProfileArn (list) --The IAM profile ARN of the instance.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceAwsEc2InstanceVpcId (list) --The identifier of the VPC that the instance was launched in.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceAwsEc2InstanceSubnetId (list) --The identifier of the subnet that the instance was launched in.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceAwsEc2InstanceLaunchedAt (list) --The date and time the instance was launched.\n\n(dict) --A date filter for querying findings.\n\nStart (string) --A start date for the date filter.\n\nEnd (string) --An end date for the date filter.\n\nDateRange (dict) --A date range for the date filter.\n\nValue (integer) --A date range value for the date filter.\n\nUnit (string) --A date range unit for the date filter.\n\n\n\n\n\n\n\nResourceAwsS3BucketOwnerId (list) --The canonical user ID of the owner of the S3 bucket.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceAwsS3BucketOwnerName (list) --The display name of the owner of the S3 bucket.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceAwsIamAccessKeyUserName (list) --The user associated with the IAM access key related to a finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceAwsIamAccessKeyStatus (list) --The status of the IAM access key related to a finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceAwsIamAccessKeyCreatedAt (list) --The creation date/time of the IAM access key related to a finding.\n\n(dict) --A date filter for querying findings.\n\nStart (string) --A start date for the date filter.\n\nEnd (string) --An end date for the date filter.\n\nDateRange (dict) --A date range for the date filter.\n\nValue (integer) --A date range value for the date filter.\n\nUnit (string) --A date range unit for the date filter.\n\n\n\n\n\n\n\nResourceContainerName (list) --The name of the container related to a finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceContainerImageId (list) --The identifier of the image related to a finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceContainerImageName (list) --The name of the image related to a finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nResourceContainerLaunchedAt (list) --The date/time that the container was started.\n\n(dict) --A date filter for querying findings.\n\nStart (string) --A start date for the date filter.\n\nEnd (string) --An end date for the date filter.\n\nDateRange (dict) --A date range for the date filter.\n\nValue (integer) --A date range value for the date filter.\n\nUnit (string) --A date range unit for the date filter.\n\n\n\n\n\n\n\nResourceDetailsOther (list) --The details of a resource that doesn\'t have a specific subfield for the resource type defined.\n\n(dict) --The map filter for querying findings.\n\nKey (string) --The key of the map filter.\n\nValue (string) --The value for the key in the map filter.\n\nComparison (string) --The condition to apply to a key value when querying for findings with a map filter.\n\n\n\n\n\nComplianceStatus (list) --Exclusive to findings that are generated as the result of a check run against a specific rule in a supported standard, such as CIS AWS Foundations. Contains security standard-related finding details.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nVerificationState (list) --The veracity of a finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nWorkflowState (list) --The workflow state of a finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nWorkflowStatus (list) --The status of the investigation into a finding. Allowed values are the following.\n\nNEW - The initial state of a finding, before it is reviewed.\nNOTIFIED - Indicates that the resource owner has been notified about the security issue. Used when the initial reviewer is not the resource owner, and needs intervention from the resource owner.\nSUPPRESSED - The finding will not be reviewed again and will not be acted upon.\nRESOLVED - The finding was reviewed and remediated and is now considered resolved.\n\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nRecordState (list) --The updated record state for the finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nRelatedFindingsProductArn (list) --The ARN of the solution that generated a related finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nRelatedFindingsId (list) --The solution-generated identifier for a related finding.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nNoteText (list) --The text of a note.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nNoteUpdatedAt (list) --The timestamp of when the note was updated.\n\n(dict) --A date filter for querying findings.\n\nStart (string) --A start date for the date filter.\n\nEnd (string) --An end date for the date filter.\n\nDateRange (dict) --A date range for the date filter.\n\nValue (integer) --A date range value for the date filter.\n\nUnit (string) --A date range unit for the date filter.\n\n\n\n\n\n\n\nNoteUpdatedBy (list) --The principal that created a note.\n\n(dict) --A string filter for querying findings.\n\nValue (string) --The string filter value.\n\nComparison (string) --The condition to be applied to a string value when querying for findings.\n\n\n\n\n\nKeyword (list) --A keyword for a finding.\n\n(dict) --A keyword filter for querying findings.\n\nValue (string) --A value for the keyword.\n\n\n\n\n\n\n

    :type GroupByAttribute: string
    :param GroupByAttribute: The updated GroupBy attribute that defines this insight.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

SecurityHub.Client.exceptions.InternalException
SecurityHub.Client.exceptions.InvalidInputException
SecurityHub.Client.exceptions.InvalidAccessException
SecurityHub.Client.exceptions.LimitExceededException
SecurityHub.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_standards_control(StandardsControlArn=None, ControlStatus=None, DisabledReason=None):
    """
    Used to control whether an individual security standard control is enabled or disabled.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_standards_control(
        StandardsControlArn='string',
        ControlStatus='ENABLED'|'DISABLED',
        DisabledReason='string'
    )
    
    
    :type StandardsControlArn: string
    :param StandardsControlArn: [REQUIRED]\nThe ARN of the security standard control to enable or disable.\n

    :type ControlStatus: string
    :param ControlStatus: The updated status of the security standard control.

    :type DisabledReason: string
    :param DisabledReason: A description of the reason why you are disabling a security standard control.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

SecurityHub.Client.exceptions.InternalException
SecurityHub.Client.exceptions.InvalidInputException
SecurityHub.Client.exceptions.InvalidAccessException
SecurityHub.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

