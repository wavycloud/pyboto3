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

def associate_drt_log_bucket(LogBucket=None):
    """
    Authorizes the DDoS Response team (DRT) to access the specified Amazon S3 bucket containing your AWS WAF logs. You can associate up to 10 Amazon S3 buckets with your subscription.
    To use the services of the DRT and make an AssociateDRTLogBucket request, you must be subscribed to the Business Support plan or the Enterprise Support plan .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.associate_drt_log_bucket(
        LogBucket='string'
    )
    
    
    :type LogBucket: string
    :param LogBucket: [REQUIRED]\nThe Amazon S3 bucket that contains your AWS WAF logs.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

Shield.Client.exceptions.InternalErrorException
Shield.Client.exceptions.InvalidOperationException
Shield.Client.exceptions.NoAssociatedRoleException
Shield.Client.exceptions.LimitsExceededException
Shield.Client.exceptions.InvalidParameterException
Shield.Client.exceptions.AccessDeniedForDependencyException
Shield.Client.exceptions.OptimisticLockException
Shield.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    Shield.Client.exceptions.InternalErrorException
    Shield.Client.exceptions.InvalidOperationException
    Shield.Client.exceptions.NoAssociatedRoleException
    Shield.Client.exceptions.LimitsExceededException
    Shield.Client.exceptions.InvalidParameterException
    Shield.Client.exceptions.AccessDeniedForDependencyException
    Shield.Client.exceptions.OptimisticLockException
    Shield.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def associate_drt_role(RoleArn=None):
    """
    Authorizes the DDoS Response team (DRT), using the specified role, to access your AWS account to assist with DDoS attack mitigation during potential attacks. This enables the DRT to inspect your AWS WAF configuration and create or update AWS WAF rules and web ACLs.
    You can associate only one RoleArn with your subscription. If you submit an AssociateDRTRole request for an account that already has an associated role, the new RoleArn will replace the existing RoleArn .
    Prior to making the AssociateDRTRole request, you must attach the AWSShieldDRTAccessPolicy managed policy to the role you will specify in the request. For more information see `Attaching and Detaching IAM Policies < https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html>`__ . The role must also trust the service principal drt.shield.amazonaws.com . For more information, see IAM JSON Policy Elements: Principal .
    The DRT will have access only to your AWS WAF and Shield resources. By submitting this request, you authorize the DRT to inspect your AWS WAF and Shield configuration and create and update AWS WAF rules and web ACLs on your behalf. The DRT takes these actions only if explicitly authorized by you.
    You must have the iam:PassRole permission to make an AssociateDRTRole request. For more information, see Granting a User Permissions to Pass a Role to an AWS Service .
    To use the services of the DRT and make an AssociateDRTRole request, you must be subscribed to the Business Support plan or the Enterprise Support plan .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.associate_drt_role(
        RoleArn='string'
    )
    
    
    :type RoleArn: string
    :param RoleArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the role the DRT will use to access your AWS account.\nPrior to making the AssociateDRTRole request, you must attach the AWSShieldDRTAccessPolicy managed policy to this role. For more information see `Attaching and Detaching IAM Policies < https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html>`__ .\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

Shield.Client.exceptions.InternalErrorException
Shield.Client.exceptions.InvalidOperationException
Shield.Client.exceptions.InvalidParameterException
Shield.Client.exceptions.AccessDeniedForDependencyException
Shield.Client.exceptions.OptimisticLockException
Shield.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    Shield.Client.exceptions.InternalErrorException
    Shield.Client.exceptions.InvalidOperationException
    Shield.Client.exceptions.InvalidParameterException
    Shield.Client.exceptions.AccessDeniedForDependencyException
    Shield.Client.exceptions.OptimisticLockException
    Shield.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def associate_health_check(ProtectionId=None, HealthCheckArn=None):
    """
    Adds health-based detection to the Shield Advanced protection for a resource. Shield Advanced health-based detection uses the health of your AWS resource to improve responsiveness and accuracy in attack detection and mitigation.
    You define the health check in Route 53 and then associate it with your Shield Advanced protection. For more information, see Shield Advanced Health-Based Detection in the AWS WAF and AWS Shield Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.associate_health_check(
        ProtectionId='string',
        HealthCheckArn='string'
    )
    
    
    :type ProtectionId: string
    :param ProtectionId: [REQUIRED]\nThe unique identifier (ID) for the Protection object to add the health check association to.\n

    :type HealthCheckArn: string
    :param HealthCheckArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the health check to associate with the protection.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Shield.Client.exceptions.InternalErrorException
Shield.Client.exceptions.LimitsExceededException
Shield.Client.exceptions.ResourceNotFoundException
Shield.Client.exceptions.InvalidParameterException
Shield.Client.exceptions.OptimisticLockException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def create_protection(Name=None, ResourceArn=None):
    """
    Enables AWS Shield Advanced for a specific AWS resource. The resource can be an Amazon CloudFront distribution, Elastic Load Balancing load balancer, AWS Global Accelerator accelerator, Elastic IP Address, or an Amazon Route 53 hosted zone.
    You can add protection to only a single resource with each CreateProtection request. If you want to add protection to multiple resources at once, use the AWS WAF console . For more information see Getting Started with AWS Shield Advanced and Add AWS Shield Advanced Protection to more AWS Resources .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_protection(
        Name='string',
        ResourceArn='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nFriendly name for the Protection you are creating.\n

    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe ARN (Amazon Resource Name) of the resource to be protected.\nThe ARN should be in one of the following formats:\n\nFor an Application Load Balancer: ``arn:aws:elasticloadbalancing:region :account-id :loadbalancer/app/load-balancer-name /load-balancer-id ``\nFor an Elastic Load Balancer (Classic Load Balancer): ``arn:aws:elasticloadbalancing:region :account-id :loadbalancer/load-balancer-name ``\nFor an AWS CloudFront distribution: ``arn:aws:cloudfront::account-id :distribution/distribution-id ``\nFor an AWS Global Accelerator accelerator: ``arn:aws:globalaccelerator::account-id :accelerator/accelerator-id ``\nFor Amazon Route 53: ``arn:aws:route53:::hostedzone/hosted-zone-id ``\nFor an Elastic IP address: ``arn:aws:ec2:region :account-id :eip-allocation/allocation-id ``\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ProtectionId': 'string'
}


Response Structure

(dict) --

ProtectionId (string) --
The unique identifier (ID) for the  Protection object that is created.







Exceptions

Shield.Client.exceptions.InternalErrorException
Shield.Client.exceptions.InvalidResourceException
Shield.Client.exceptions.InvalidOperationException
Shield.Client.exceptions.LimitsExceededException
Shield.Client.exceptions.ResourceAlreadyExistsException
Shield.Client.exceptions.OptimisticLockException
Shield.Client.exceptions.ResourceNotFoundException


    :return: {
        'ProtectionId': 'string'
    }
    
    
    :returns: 
    Shield.Client.exceptions.InternalErrorException
    Shield.Client.exceptions.InvalidResourceException
    Shield.Client.exceptions.InvalidOperationException
    Shield.Client.exceptions.LimitsExceededException
    Shield.Client.exceptions.ResourceAlreadyExistsException
    Shield.Client.exceptions.OptimisticLockException
    Shield.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def create_subscription():
    """
    Activates AWS Shield Advanced for an account.
    As part of this request you can specify EmergencySettings that automaticaly grant the DDoS response team (DRT) needed permissions to assist you during a suspected DDoS attack. For more information see Authorize the DDoS Response Team to Create Rules and Web ACLs on Your Behalf .
    To use the services of the DRT, you must be subscribed to the Business Support plan or the Enterprise Support plan .
    When you initally create a subscription, your subscription is set to be automatically renewed at the end of the existing subscription period. You can change this by submitting an UpdateSubscription request.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_subscription()
    
    
    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

Shield.Client.exceptions.InternalErrorException
Shield.Client.exceptions.ResourceAlreadyExistsException


    :return: {}
    
    
    :returns: 
    Shield.Client.exceptions.InternalErrorException
    Shield.Client.exceptions.ResourceAlreadyExistsException
    
    """
    pass

def delete_protection(ProtectionId=None):
    """
    Deletes an AWS Shield Advanced  Protection .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_protection(
        ProtectionId='string'
    )
    
    
    :type ProtectionId: string
    :param ProtectionId: [REQUIRED]\nThe unique identifier (ID) for the Protection object to be deleted.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

Shield.Client.exceptions.InternalErrorException
Shield.Client.exceptions.ResourceNotFoundException
Shield.Client.exceptions.OptimisticLockException


    :return: {}
    
    
    :returns: 
    Shield.Client.exceptions.InternalErrorException
    Shield.Client.exceptions.ResourceNotFoundException
    Shield.Client.exceptions.OptimisticLockException
    
    """
    pass

def delete_subscription():
    """
    Removes AWS Shield Advanced from an account. AWS Shield Advanced requires a 1-year subscription commitment. You cannot delete a subscription prior to the completion of that commitment.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_subscription()
    
    
    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

Shield.Client.exceptions.InternalErrorException
Shield.Client.exceptions.LockedSubscriptionException
Shield.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    Shield.Client.exceptions.InternalErrorException
    Shield.Client.exceptions.LockedSubscriptionException
    Shield.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def describe_attack(AttackId=None):
    """
    Describes the details of a DDoS attack.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_attack(
        AttackId='string'
    )
    
    
    :type AttackId: string
    :param AttackId: [REQUIRED]\nThe unique identifier (ID) for the attack that to be described.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Attack': {
        'AttackId': 'string',
        'ResourceArn': 'string',
        'SubResources': [
            {
                'Type': 'IP'|'URL',
                'Id': 'string',
                'AttackVectors': [
                    {
                        'VectorType': 'string',
                        'VectorCounters': [
                            {
                                'Name': 'string',
                                'Max': 123.0,
                                'Average': 123.0,
                                'Sum': 123.0,
                                'N': 123,
                                'Unit': 'string'
                            },
                        ]
                    },
                ],
                'Counters': [
                    {
                        'Name': 'string',
                        'Max': 123.0,
                        'Average': 123.0,
                        'Sum': 123.0,
                        'N': 123,
                        'Unit': 'string'
                    },
                ]
            },
        ],
        'StartTime': datetime(2015, 1, 1),
        'EndTime': datetime(2015, 1, 1),
        'AttackCounters': [
            {
                'Name': 'string',
                'Max': 123.0,
                'Average': 123.0,
                'Sum': 123.0,
                'N': 123,
                'Unit': 'string'
            },
        ],
        'AttackProperties': [
            {
                'AttackLayer': 'NETWORK'|'APPLICATION',
                'AttackPropertyIdentifier': 'DESTINATION_URL'|'REFERRER'|'SOURCE_ASN'|'SOURCE_COUNTRY'|'SOURCE_IP_ADDRESS'|'SOURCE_USER_AGENT'|'WORDPRESS_PINGBACK_REFLECTOR'|'WORDPRESS_PINGBACK_SOURCE',
                'TopContributors': [
                    {
                        'Name': 'string',
                        'Value': 123
                    },
                ],
                'Unit': 'BITS'|'BYTES'|'PACKETS'|'REQUESTS',
                'Total': 123
            },
        ],
        'Mitigations': [
            {
                'MitigationName': 'string'
            },
        ]
    }
}


Response Structure

(dict) --
Attack (dict) --The attack that is described.

AttackId (string) --The unique identifier (ID) of the attack.

ResourceArn (string) --The ARN (Amazon Resource Name) of the resource that was attacked.

SubResources (list) --If applicable, additional detail about the resource being attacked, for example, IP address or URL.

(dict) --The attack information for the specified SubResource.

Type (string) --The SubResource type.

Id (string) --The unique identifier (ID) of the SubResource .

AttackVectors (list) --The list of attack types and associated counters.

(dict) --A summary of information about the attack.

VectorType (string) --The attack type, for example, SNMP reflection or SYN flood.

VectorCounters (list) --The list of counters that describe the details of the attack.

(dict) --The counter that describes a DDoS attack.

Name (string) --The counter name.

Max (float) --The maximum value of the counter for a specified time period.

Average (float) --The average value of the counter for a specified time period.

Sum (float) --The total of counter values for a specified time period.

N (integer) --The number of counters for a specified time period.

Unit (string) --The unit of the counters.









Counters (list) --The counters that describe the details of the attack.

(dict) --The counter that describes a DDoS attack.

Name (string) --The counter name.

Max (float) --The maximum value of the counter for a specified time period.

Average (float) --The average value of the counter for a specified time period.

Sum (float) --The total of counter values for a specified time period.

N (integer) --The number of counters for a specified time period.

Unit (string) --The unit of the counters.









StartTime (datetime) --The time the attack started, in Unix time in seconds. For more information see timestamp .

EndTime (datetime) --The time the attack ended, in Unix time in seconds. For more information see timestamp .

AttackCounters (list) --List of counters that describe the attack for the specified time period.

(dict) --The counter that describes a DDoS attack.

Name (string) --The counter name.

Max (float) --The maximum value of the counter for a specified time period.

Average (float) --The average value of the counter for a specified time period.

Sum (float) --The total of counter values for a specified time period.

N (integer) --The number of counters for a specified time period.

Unit (string) --The unit of the counters.





AttackProperties (list) --The array of  AttackProperty objects.

(dict) --Details of the described attack.

AttackLayer (string) --The type of distributed denial of service (DDoS) event that was observed. NETWORK indicates layer 3 and layer 4 events and APPLICATION indicates layer 7 events.

AttackPropertyIdentifier (string) --Defines the DDoS attack property information that is provided. The WORDPRESS_PINGBACK_REFLECTOR and WORDPRESS_PINGBACK_SOURCE values are valid only for WordPress reflective pingback DDoS attacks.

TopContributors (list) --The array of  Contributor objects that includes the top five contributors to an attack.

(dict) --A contributor to the attack and their contribution.

Name (string) --The name of the contributor. This is dependent on the AttackPropertyIdentifier . For example, if the AttackPropertyIdentifier is SOURCE_COUNTRY , the Name could be United States .

Value (integer) --The contribution of this contributor expressed in  Protection units. For example 10,000 .





Unit (string) --The unit of the Value of the contributions.

Total (integer) --The total contributions made to this attack by all contributors, not just the five listed in the TopContributors list.





Mitigations (list) --List of mitigation actions taken for the attack.

(dict) --The mitigation applied to a DDoS attack.

MitigationName (string) --The name of the mitigation taken for this attack.












Exceptions

Shield.Client.exceptions.InternalErrorException
Shield.Client.exceptions.AccessDeniedException


    :return: {
        'Attack': {
            'AttackId': 'string',
            'ResourceArn': 'string',
            'SubResources': [
                {
                    'Type': 'IP'|'URL',
                    'Id': 'string',
                    'AttackVectors': [
                        {
                            'VectorType': 'string',
                            'VectorCounters': [
                                {
                                    'Name': 'string',
                                    'Max': 123.0,
                                    'Average': 123.0,
                                    'Sum': 123.0,
                                    'N': 123,
                                    'Unit': 'string'
                                },
                            ]
                        },
                    ],
                    'Counters': [
                        {
                            'Name': 'string',
                            'Max': 123.0,
                            'Average': 123.0,
                            'Sum': 123.0,
                            'N': 123,
                            'Unit': 'string'
                        },
                    ]
                },
            ],
            'StartTime': datetime(2015, 1, 1),
            'EndTime': datetime(2015, 1, 1),
            'AttackCounters': [
                {
                    'Name': 'string',
                    'Max': 123.0,
                    'Average': 123.0,
                    'Sum': 123.0,
                    'N': 123,
                    'Unit': 'string'
                },
            ],
            'AttackProperties': [
                {
                    'AttackLayer': 'NETWORK'|'APPLICATION',
                    'AttackPropertyIdentifier': 'DESTINATION_URL'|'REFERRER'|'SOURCE_ASN'|'SOURCE_COUNTRY'|'SOURCE_IP_ADDRESS'|'SOURCE_USER_AGENT'|'WORDPRESS_PINGBACK_REFLECTOR'|'WORDPRESS_PINGBACK_SOURCE',
                    'TopContributors': [
                        {
                            'Name': 'string',
                            'Value': 123
                        },
                    ],
                    'Unit': 'BITS'|'BYTES'|'PACKETS'|'REQUESTS',
                    'Total': 123
                },
            ],
            'Mitigations': [
                {
                    'MitigationName': 'string'
                },
            ]
        }
    }
    
    
    """
    pass

def describe_drt_access():
    """
    Returns the current role and list of Amazon S3 log buckets used by the DDoS Response team (DRT) to access your AWS account while assisting with attack mitigation.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_drt_access()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'RoleArn': 'string',
    'LogBucketList': [
        'string',
    ]
}


Response Structure

(dict) --
RoleArn (string) --The Amazon Resource Name (ARN) of the role the DRT used to access your AWS account.

LogBucketList (list) --The list of Amazon S3 buckets accessed by the DRT.

(string) --







Exceptions

Shield.Client.exceptions.InternalErrorException
Shield.Client.exceptions.ResourceNotFoundException


    :return: {
        'RoleArn': 'string',
        'LogBucketList': [
            'string',
        ]
    }
    
    
    :returns: 
    Shield.Client.exceptions.InternalErrorException
    Shield.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def describe_emergency_contact_settings():
    """
    Lists the email addresses that the DRT can use to contact you during a suspected attack.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_emergency_contact_settings()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'EmergencyContactList': [
        {
            'EmailAddress': 'string'
        },
    ]
}


Response Structure

(dict) --
EmergencyContactList (list) --A list of email addresses that the DRT can use to contact you during a suspected attack.

(dict) --Contact information that the DRT can use to contact you during a suspected attack.

EmailAddress (string) --An email address that the DRT can use to contact you during a suspected attack.










Exceptions

Shield.Client.exceptions.InternalErrorException
Shield.Client.exceptions.ResourceNotFoundException


    :return: {
        'EmergencyContactList': [
            {
                'EmailAddress': 'string'
            },
        ]
    }
    
    
    """
    pass

def describe_protection(ProtectionId=None, ResourceArn=None):
    """
    Lists the details of a  Protection object.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_protection(
        ProtectionId='string',
        ResourceArn='string'
    )
    
    
    :type ProtectionId: string
    :param ProtectionId: The unique identifier (ID) for the Protection object that is described. When submitting the DescribeProtection request you must provide either the ResourceArn or the ProtectionID , but not both.

    :type ResourceArn: string
    :param ResourceArn: The ARN (Amazon Resource Name) of the AWS resource for the Protection object that is described. When submitting the DescribeProtection request you must provide either the ResourceArn or the ProtectionID , but not both.

    :rtype: dict

ReturnsResponse Syntax
{
    'Protection': {
        'Id': 'string',
        'Name': 'string',
        'ResourceArn': 'string',
        'HealthCheckIds': [
            'string',
        ]
    }
}


Response Structure

(dict) --

Protection (dict) --
The  Protection object that is described.

Id (string) --
The unique identifier (ID) of the protection.

Name (string) --
The friendly name of the protection. For example, My CloudFront distributions .

ResourceArn (string) --
The ARN (Amazon Resource Name) of the AWS resource that is protected.

HealthCheckIds (list) --
The unique identifier (ID) for the Route 53 health check that\'s associated with the protection.

(string) --










Exceptions

Shield.Client.exceptions.InternalErrorException
Shield.Client.exceptions.InvalidParameterException
Shield.Client.exceptions.ResourceNotFoundException


    :return: {
        'Protection': {
            'Id': 'string',
            'Name': 'string',
            'ResourceArn': 'string',
            'HealthCheckIds': [
                'string',
            ]
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_subscription():
    """
    Provides details about the AWS Shield Advanced subscription for an account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_subscription()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'Subscription': {
        'StartTime': datetime(2015, 1, 1),
        'EndTime': datetime(2015, 1, 1),
        'TimeCommitmentInSeconds': 123,
        'AutoRenew': 'ENABLED'|'DISABLED',
        'Limits': [
            {
                'Type': 'string',
                'Max': 123
            },
        ]
    }
}


Response Structure

(dict) --
Subscription (dict) --The AWS Shield Advanced subscription details for an account.

StartTime (datetime) --The start time of the subscription, in Unix time in seconds. For more information see timestamp .

EndTime (datetime) --The date and time your subscription will end.

TimeCommitmentInSeconds (integer) --The length, in seconds, of the AWS Shield Advanced subscription for the account.

AutoRenew (string) --If ENABLED , the subscription will be automatically renewed at the end of the existing subscription period.
When you initally create a subscription, AutoRenew is set to ENABLED . You can change this by submitting an UpdateSubscription request. If the UpdateSubscription request does not included a value for AutoRenew , the existing value for AutoRenew remains unchanged.

Limits (list) --Specifies how many protections of a given type you can create.

(dict) --Specifies how many protections of a given type you can create.

Type (string) --The type of protection.

Max (integer) --The maximum number of protections that can be created for the specified Type .












Exceptions

Shield.Client.exceptions.InternalErrorException
Shield.Client.exceptions.ResourceNotFoundException


    :return: {
        'Subscription': {
            'StartTime': datetime(2015, 1, 1),
            'EndTime': datetime(2015, 1, 1),
            'TimeCommitmentInSeconds': 123,
            'AutoRenew': 'ENABLED'|'DISABLED',
            'Limits': [
                {
                    'Type': 'string',
                    'Max': 123
                },
            ]
        }
    }
    
    
    """
    pass

def disassociate_drt_log_bucket(LogBucket=None):
    """
    Removes the DDoS Response team\'s (DRT) access to the specified Amazon S3 bucket containing your AWS WAF logs.
    To make a DisassociateDRTLogBucket request, you must be subscribed to the Business Support plan or the Enterprise Support plan . However, if you are not subscribed to one of these support plans, but had been previously and had granted the DRT access to your account, you can submit a DisassociateDRTLogBucket request to remove this access.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disassociate_drt_log_bucket(
        LogBucket='string'
    )
    
    
    :type LogBucket: string
    :param LogBucket: [REQUIRED]\nThe Amazon S3 bucket that contains your AWS WAF logs.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

Shield.Client.exceptions.InternalErrorException
Shield.Client.exceptions.InvalidOperationException
Shield.Client.exceptions.NoAssociatedRoleException
Shield.Client.exceptions.AccessDeniedForDependencyException
Shield.Client.exceptions.OptimisticLockException
Shield.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    Shield.Client.exceptions.InternalErrorException
    Shield.Client.exceptions.InvalidOperationException
    Shield.Client.exceptions.NoAssociatedRoleException
    Shield.Client.exceptions.AccessDeniedForDependencyException
    Shield.Client.exceptions.OptimisticLockException
    Shield.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def disassociate_drt_role():
    """
    Removes the DDoS Response team\'s (DRT) access to your AWS account.
    To make a DisassociateDRTRole request, you must be subscribed to the Business Support plan or the Enterprise Support plan . However, if you are not subscribed to one of these support plans, but had been previously and had granted the DRT access to your account, you can submit a DisassociateDRTRole request to remove this access.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disassociate_drt_role()
    
    
    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

Shield.Client.exceptions.InternalErrorException
Shield.Client.exceptions.InvalidOperationException
Shield.Client.exceptions.OptimisticLockException
Shield.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    Shield.Client.exceptions.InternalErrorException
    Shield.Client.exceptions.InvalidOperationException
    Shield.Client.exceptions.OptimisticLockException
    Shield.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def disassociate_health_check(ProtectionId=None, HealthCheckArn=None):
    """
    Removes health-based detection from the Shield Advanced protection for a resource. Shield Advanced health-based detection uses the health of your AWS resource to improve responsiveness and accuracy in attack detection and mitigation.
    You define the health check in Route 53 and then associate or disassociate it with your Shield Advanced protection. For more information, see Shield Advanced Health-Based Detection in the AWS WAF and AWS Shield Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disassociate_health_check(
        ProtectionId='string',
        HealthCheckArn='string'
    )
    
    
    :type ProtectionId: string
    :param ProtectionId: [REQUIRED]\nThe unique identifier (ID) for the Protection object to remove the health check association from.\n

    :type HealthCheckArn: string
    :param HealthCheckArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the health check that is associated with the protection.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Shield.Client.exceptions.InternalErrorException
Shield.Client.exceptions.InvalidParameterException
Shield.Client.exceptions.ResourceNotFoundException
Shield.Client.exceptions.OptimisticLockException


    :return: {}
    
    
    :returns: 
    (dict) --
    
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

def get_subscription_state():
    """
    Returns the SubscriptionState , either Active or Inactive .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_subscription_state()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'SubscriptionState': 'ACTIVE'|'INACTIVE'
}


Response Structure

(dict) --
SubscriptionState (string) --The status of the subscription.






Exceptions

Shield.Client.exceptions.InternalErrorException


    :return: {
        'SubscriptionState': 'ACTIVE'|'INACTIVE'
    }
    
    
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

def list_attacks(ResourceArns=None, StartTime=None, EndTime=None, NextToken=None, MaxResults=None):
    """
    Returns all ongoing DDoS attacks or all DDoS attacks during a specified time period.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_attacks(
        ResourceArns=[
            'string',
        ],
        StartTime={
            'FromInclusive': datetime(2015, 1, 1),
            'ToExclusive': datetime(2015, 1, 1)
        },
        EndTime={
            'FromInclusive': datetime(2015, 1, 1),
            'ToExclusive': datetime(2015, 1, 1)
        },
        NextToken='string',
        MaxResults=123
    )
    
    
    :type ResourceArns: list
    :param ResourceArns: The ARN (Amazon Resource Name) of the resource that was attacked. If this is left blank, all applicable resources for this account will be included.\n\n(string) --\n\n

    :type StartTime: dict
    :param StartTime: The start of the time period for the attacks. This is a timestamp type. The sample request above indicates a number type because the default used by WAF is Unix time in seconds. However any valid timestamp format is allowed.\n\nFromInclusive (datetime) --The start time, in Unix time in seconds. For more information see timestamp .\n\nToExclusive (datetime) --The end time, in Unix time in seconds. For more information see timestamp .\n\n\n

    :type EndTime: dict
    :param EndTime: The end of the time period for the attacks. This is a timestamp type. The sample request above indicates a number type because the default used by WAF is Unix time in seconds. However any valid timestamp format is allowed.\n\nFromInclusive (datetime) --The start time, in Unix time in seconds. For more information see timestamp .\n\nToExclusive (datetime) --The end time, in Unix time in seconds. For more information see timestamp .\n\n\n

    :type NextToken: string
    :param NextToken: The ListAttacksRequest.NextMarker value from a previous call to ListAttacksRequest . Pass null if this is the first call.

    :type MaxResults: integer
    :param MaxResults: The maximum number of AttackSummary objects to be returned. If this is left blank, the first 20 results will be returned.\nThis is a maximum value; it is possible that AWS WAF will return the results in smaller batches. That is, the number of AttackSummary objects returned could be less than MaxResults , even if there are still more AttackSummary objects yet to return. If there are more AttackSummary objects to return, AWS WAF will always also return a NextToken .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'AttackSummaries': [
        {
            'AttackId': 'string',
            'ResourceArn': 'string',
            'StartTime': datetime(2015, 1, 1),
            'EndTime': datetime(2015, 1, 1),
            'AttackVectors': [
                {
                    'VectorType': 'string'
                },
            ]
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

AttackSummaries (list) --
The attack information for the specified time range.

(dict) --
Summarizes all DDoS attacks for a specified time period.

AttackId (string) --
The unique identifier (ID) of the attack.

ResourceArn (string) --
The ARN (Amazon Resource Name) of the resource that was attacked.

StartTime (datetime) --
The start time of the attack, in Unix time in seconds. For more information see timestamp .

EndTime (datetime) --
The end time of the attack, in Unix time in seconds. For more information see timestamp .

AttackVectors (list) --
The list of attacks for a specified time period.

(dict) --
Describes the attack.

VectorType (string) --
The attack type. Valid values:

UDP_TRAFFIC
UDP_FRAGMENT
GENERIC_UDP_REFLECTION
DNS_REFLECTION
NTP_REFLECTION
CHARGEN_REFLECTION
SSDP_REFLECTION
PORT_MAPPER
RIP_REFLECTION
SNMP_REFLECTION
MSSQL_REFLECTION
NET_BIOS_REFLECTION
SYN_FLOOD
ACK_FLOOD
REQUEST_FLOOD
HTTP_REFLECTION
UDS_REFLECTION
MEMCACHED_REFLECTION










NextToken (string) --
The token returned by a previous call to indicate that there is more data available. If not null, more results are available. Pass this value for the NextMarker parameter in a subsequent call to ListAttacks to retrieve the next set of items.
AWS WAF might return the list of  AttackSummary objects in batches smaller than the number specified by MaxResults. If there are more  AttackSummary objects to return, AWS WAF will always also return a NextToken .







Exceptions

Shield.Client.exceptions.InternalErrorException
Shield.Client.exceptions.InvalidParameterException
Shield.Client.exceptions.InvalidOperationException


    :return: {
        'AttackSummaries': [
            {
                'AttackId': 'string',
                'ResourceArn': 'string',
                'StartTime': datetime(2015, 1, 1),
                'EndTime': datetime(2015, 1, 1),
                'AttackVectors': [
                    {
                        'VectorType': 'string'
                    },
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    UDP_TRAFFIC
    UDP_FRAGMENT
    GENERIC_UDP_REFLECTION
    DNS_REFLECTION
    NTP_REFLECTION
    CHARGEN_REFLECTION
    SSDP_REFLECTION
    PORT_MAPPER
    RIP_REFLECTION
    SNMP_REFLECTION
    MSSQL_REFLECTION
    NET_BIOS_REFLECTION
    SYN_FLOOD
    ACK_FLOOD
    REQUEST_FLOOD
    HTTP_REFLECTION
    UDS_REFLECTION
    MEMCACHED_REFLECTION
    
    """
    pass

def list_protections(NextToken=None, MaxResults=None):
    """
    Lists all  Protection objects for the account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_protections(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: The ListProtectionsRequest.NextToken value from a previous call to ListProtections . Pass null if this is the first call.

    :type MaxResults: integer
    :param MaxResults: The maximum number of Protection objects to be returned. If this is left blank the first 20 results will be returned.\nThis is a maximum value; it is possible that AWS WAF will return the results in smaller batches. That is, the number of Protection objects returned could be less than MaxResults , even if there are still more Protection objects yet to return. If there are more Protection objects to return, AWS WAF will always also return a NextToken .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Protections': [
        {
            'Id': 'string',
            'Name': 'string',
            'ResourceArn': 'string',
            'HealthCheckIds': [
                'string',
            ]
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Protections (list) --
The array of enabled  Protection objects.

(dict) --
An object that represents a resource that is under DDoS protection.

Id (string) --
The unique identifier (ID) of the protection.

Name (string) --
The friendly name of the protection. For example, My CloudFront distributions .

ResourceArn (string) --
The ARN (Amazon Resource Name) of the AWS resource that is protected.

HealthCheckIds (list) --
The unique identifier (ID) for the Route 53 health check that\'s associated with the protection.

(string) --






NextToken (string) --
If you specify a value for MaxResults and you have more Protections than the value of MaxResults, AWS Shield Advanced returns a NextToken value in the response that allows you to list another group of Protections. For the second and subsequent ListProtections requests, specify the value of NextToken from the previous response to get information about another batch of Protections.
AWS WAF might return the list of  Protection objects in batches smaller than the number specified by MaxResults. If there are more  Protection objects to return, AWS WAF will always also return a NextToken .







Exceptions

Shield.Client.exceptions.InternalErrorException
Shield.Client.exceptions.ResourceNotFoundException
Shield.Client.exceptions.InvalidPaginationTokenException


    :return: {
        'Protections': [
            {
                'Id': 'string',
                'Name': 'string',
                'ResourceArn': 'string',
                'HealthCheckIds': [
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

def update_emergency_contact_settings(EmergencyContactList=None):
    """
    Updates the details of the list of email addresses that the DRT can use to contact you during a suspected attack.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_emergency_contact_settings(
        EmergencyContactList=[
            {
                'EmailAddress': 'string'
            },
        ]
    )
    
    
    :type EmergencyContactList: list
    :param EmergencyContactList: A list of email addresses that the DRT can use to contact you during a suspected attack.\n\n(dict) --Contact information that the DRT can use to contact you during a suspected attack.\n\nEmailAddress (string) -- [REQUIRED]An email address that the DRT can use to contact you during a suspected attack.\n\n\n\n\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

Shield.Client.exceptions.InternalErrorException
Shield.Client.exceptions.InvalidParameterException
Shield.Client.exceptions.OptimisticLockException
Shield.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    Shield.Client.exceptions.InternalErrorException
    Shield.Client.exceptions.InvalidParameterException
    Shield.Client.exceptions.OptimisticLockException
    Shield.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def update_subscription(AutoRenew=None):
    """
    Updates the details of an existing subscription. Only enter values for parameters you want to change. Empty parameters are not updated.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_subscription(
        AutoRenew='ENABLED'|'DISABLED'
    )
    
    
    :type AutoRenew: string
    :param AutoRenew: When you initally create a subscription, AutoRenew is set to ENABLED . If ENABLED , the subscription will be automatically renewed at the end of the existing subscription period. You can change this by submitting an UpdateSubscription request. If the UpdateSubscription request does not included a value for AutoRenew , the existing value for AutoRenew remains unchanged.

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

Shield.Client.exceptions.InternalErrorException
Shield.Client.exceptions.LockedSubscriptionException
Shield.Client.exceptions.ResourceNotFoundException
Shield.Client.exceptions.InvalidParameterException
Shield.Client.exceptions.OptimisticLockException


    :return: {}
    
    
    :returns: 
    Shield.Client.exceptions.InternalErrorException
    Shield.Client.exceptions.LockedSubscriptionException
    Shield.Client.exceptions.ResourceNotFoundException
    Shield.Client.exceptions.InvalidParameterException
    Shield.Client.exceptions.OptimisticLockException
    
    """
    pass

