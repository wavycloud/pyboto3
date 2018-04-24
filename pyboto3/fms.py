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

def associate_admin_account(AdminAccount=None):
    """
    Sets the AWS Firewall Manager administrator account. AWS Firewall Manager must be associated with a master account in AWS Organizations or associated with a member account that has the appropriate permissions. If the account ID that you submit is not an AWS Organizations master account, AWS Firewall Manager will set the appropriate permissions for the given member account.
    The account that you associate with AWS Firewall Manager is called the AWS Firewall manager administrator account.
    See also: AWS API Documentation
    
    
    :example: response = client.associate_admin_account(
        AdminAccount='string'
    )
    
    
    :type AdminAccount: string
    :param AdminAccount: [REQUIRED]
            The AWS account ID to associate with AWS Firewall Manager as the AWS Firewall Manager administrator account. This can be an AWS Organizations master account or a member account. For more information about AWS Organizations and master accounts, see Managing the AWS Accounts in Your Organization .
            

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

def delete_notification_channel():
    """
    Deletes an AWS Firewall Manager association with the IAM role and the Amazon Simple Notification Service (SNS) topic that is used to record AWS Firewall Manager SNS logs.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_notification_channel()
    
    
    """
    pass

def delete_policy(PolicyId=None):
    """
    Permanently deletes an AWS Firewall Manager policy.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_policy(
        PolicyId='string'
    )
    
    
    :type PolicyId: string
    :param PolicyId: [REQUIRED]
            The ID of the policy that you want to delete. PolicyId is returned by PutPolicy and by ListPolicies .
            

    """
    pass

def disassociate_admin_account():
    """
    Disassociates the account that has been set as the AWS Firewall Manager administrator account. You will need to submit an AssociateAdminAccount request to set a new account as the AWS Firewall administrator.
    See also: AWS API Documentation
    
    
    :example: response = client.disassociate_admin_account()
    
    
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

def get_admin_account():
    """
    Returns the AWS Organizations master account that is associated with AWS Firewall Manager as the AWS Firewall Manager administrator.
    See also: AWS API Documentation
    
    
    :example: response = client.get_admin_account()
    
    
    :rtype: dict
    :return: {
        'AdminAccount': 'string'
    }
    
    
    """
    pass

def get_compliance_detail(PolicyId=None, MemberAccount=None):
    """
    Returns detailed compliance information about the specified member account. Details include resources that are in and out of compliance with the specified policy. Resources are considered non-compliant if the specified policy has not been applied to them.
    See also: AWS API Documentation
    
    
    :example: response = client.get_compliance_detail(
        PolicyId='string',
        MemberAccount='string'
    )
    
    
    :type PolicyId: string
    :param PolicyId: [REQUIRED]
            The ID of the policy that you want to get the details for. PolicyId is returned by PutPolicy and by ListPolicies .
            

    :type MemberAccount: string
    :param MemberAccount: [REQUIRED]
            The AWS account that owns the resources that you want to get the details for.
            

    :rtype: dict
    :return: {
        'PolicyComplianceDetail': {
            'PolicyOwner': 'string',
            'PolicyId': 'string',
            'MemberAccount': 'string',
            'Violators': [
                {
                    'ResourceId': 'string',
                    'ViolationReason': 'WEB_ACL_MISSING_RULE_GROUP'|'RESOURCE_MISSING_WEB_ACL'|'RESOURCE_INCORRECT_WEB_ACL',
                    'ResourceType': 'string'
                },
            ],
            'EvaluationLimitExceeded': True|False,
            'ExpiredAt': datetime(2015, 1, 1)
        }
    }
    
    
    """
    pass

def get_notification_channel():
    """
    Returns information about the Amazon Simple Notification Service (SNS) topic that is used to record AWS Firewall Manager SNS logs.
    See also: AWS API Documentation
    
    
    :example: response = client.get_notification_channel()
    
    
    :rtype: dict
    :return: {
        'SnsTopicArn': 'string',
        'SnsRoleName': 'string'
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

def get_policy(PolicyId=None):
    """
    Returns information about the specified AWS Firewall Manager policy.
    See also: AWS API Documentation
    
    
    :example: response = client.get_policy(
        PolicyId='string'
    )
    
    
    :type PolicyId: string
    :param PolicyId: [REQUIRED]
            The ID of the AWS Firewall Manager policy that you want the details for.
            

    :rtype: dict
    :return: {
        'Policy': {
            'PolicyId': 'string',
            'PolicyName': 'string',
            'PolicyUpdateToken': 'string',
            'SecurityServicePolicyData': {
                'Type': 'WAF',
                'ManagedServiceData': 'string'
            },
            'ResourceType': 'string',
            'ResourceTags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'ExcludeResourceTags': True|False,
            'RemediationEnabled': True|False
        },
        'PolicyArn': 'string'
    }
    
    
    """
    pass

def get_waiter():
    """
    
    """
    pass

def list_compliance_status(PolicyId=None, NextToken=None, MaxResults=None):
    """
    Returns an array of PolicyComplianceStatus objects in the response. Use PolicyComplianceStatus to get a summary of which member accounts are protected by the specified policy.
    See also: AWS API Documentation
    
    
    :example: response = client.list_compliance_status(
        PolicyId='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type PolicyId: string
    :param PolicyId: [REQUIRED]
            The ID of the AWS Firewall Manager policy that you want the details for.
            

    :type NextToken: string
    :param NextToken: If you specify a value for MaxResults and you have more PolicyComplianceStatus objects than the number that you specify for MaxResults , AWS Firewall Manager returns a NextToken value in the response that allows you to list another group of PolicyComplianceStatus objects. For the second and subsequent ListComplianceStatus requests, specify the value of NextToken from the previous response to get information about another batch of PolicyComplianceStatus objects.

    :type MaxResults: integer
    :param MaxResults: Specifies the number of PolicyComplianceStatus objects that you want AWS Firewall Manager to return for this request. If you have more PolicyComplianceStatus objects than the number that you specify for MaxResults , the response includes a NextToken value that you can use to get another batch of PolicyComplianceStatus objects.

    :rtype: dict
    :return: {
        'PolicyComplianceStatusList': [
            {
                'PolicyOwner': 'string',
                'PolicyId': 'string',
                'PolicyName': 'string',
                'MemberAccount': 'string',
                'EvaluationResults': [
                    {
                        'ComplianceStatus': 'COMPLIANT'|'NON_COMPLIANT',
                        'ViolatorCount': 123,
                        'EvaluationLimitExceeded': True|False
                    },
                ],
                'LastUpdated': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_policies(NextToken=None, MaxResults=None):
    """
    Returns an array of PolicySummary objects in the response.
    See also: AWS API Documentation
    
    
    :example: response = client.list_policies(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: If you specify a value for MaxResults and you have more PolicySummary objects than the number that you specify for MaxResults , AWS Firewall Manager returns a NextToken value in the response that allows you to list another group of PolicySummary objects. For the second and subsequent ListPolicies requests, specify the value of NextToken from the previous response to get information about another batch of PolicySummary objects.

    :type MaxResults: integer
    :param MaxResults: Specifies the number of PolicySummary objects that you want AWS Firewall Manager to return for this request. If you have more PolicySummary objects than the number that you specify for MaxResults , the response includes a NextToken value that you can use to get another batch of PolicySummary objects.

    :rtype: dict
    :return: {
        'PolicyList': [
            {
                'PolicyArn': 'string',
                'PolicyId': 'string',
                'PolicyName': 'string',
                'ResourceType': 'string',
                'SecurityServiceType': 'WAF',
                'RemediationEnabled': True|False
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def put_notification_channel(SnsTopicArn=None, SnsRoleName=None):
    """
    Designates the IAM role and Amazon Simple Notification Service (SNS) topic that AWS Firewall Manager uses to record SNS logs.
    See also: AWS API Documentation
    
    
    :example: response = client.put_notification_channel(
        SnsTopicArn='string',
        SnsRoleName='string'
    )
    
    
    :type SnsTopicArn: string
    :param SnsTopicArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the SNS topic that collects notifications from AWS Firewall Manager.
            

    :type SnsRoleName: string
    :param SnsRoleName: [REQUIRED]
            The Amazon Resource Name (ARN) of the IAM role that allows Amazon SNS to record AWS Firewall Manager activity.
            

    """
    pass

def put_policy(Policy=None):
    """
    Creates an AWS Firewall Manager policy.
    See also: AWS API Documentation
    
    
    :example: response = client.put_policy(
        Policy={
            'PolicyId': 'string',
            'PolicyName': 'string',
            'PolicyUpdateToken': 'string',
            'SecurityServicePolicyData': {
                'Type': 'WAF',
                'ManagedServiceData': 'string'
            },
            'ResourceType': 'string',
            'ResourceTags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'ExcludeResourceTags': True|False,
            'RemediationEnabled': True|False
        }
    )
    
    
    :type Policy: dict
    :param Policy: [REQUIRED]
            The details of the AWS Firewall Manager policy to be created.
            PolicyId (string) --The ID of the AWS Firewall Manager policy.
            PolicyName (string) -- [REQUIRED]The friendly name of the AWS Firewall Manager policy.
            PolicyUpdateToken (string) --A unique identifier for each update to the policy. When issuing a PutPolicy request, the PolicyUpdateToken in the request must match the PolicyUpdateToken of the current policy version. To get the PolicyUpdateToken of the current policy version, use a GetPolicy request.
            SecurityServicePolicyData (dict) -- [REQUIRED]Details about the security service that is being used to protect the resources.
            Type (string) -- [REQUIRED]The service that the policy is using to protect the resources. This value is WAF .
            ManagedServiceData (string) --Details about the service. This contains WAF data in JSON format, as shown in the following example:
            ManagedServiceData': '{\'type\': \'WAF\', \'ruleGroups\': [{\'id\': \'12345678-1bcd-9012-efga-0987654321ab\', \'overrideAction\' : {\'type\': \'COUNT\'}}], \'defaultAction\': {\'type\': \'BLOCK\'}}
            ResourceType (string) -- [REQUIRED]The type of resource to protect with the policy, either an Application Load Balancer or a CloudFront distribution. This is in the format shown in AWS Resource Types Reference . Valid values are AWS::ElasticLoadBalancingV2::LoadBalancer or AWS::CloudFront::Distribution .
            ResourceTags (list) --An array of ResourceTag objects.
            (dict) --The resource tags that AWS Firewall Manager uses to determine if a particular resource should be included or excluded from protection by the AWS Firewall Manager policy. Tags enable you to categorize your AWS resources in different ways, for example, by purpose, owner, or environment. Each tag consists of a key and an optional value, both of which you define. Tags are combined with an 'OR.' That is, if you add more than one tag, if any of the tags matches, the resource is considered a match for the include or exclude. Working with Tag Editor .
            Key (string) -- [REQUIRED]The resource tag key.
            Value (string) --The resource tag value.
            
            ExcludeResourceTags (boolean) -- [REQUIRED]If set to True , resources with the tags that are specified in the ResourceTag array are not protected by the policy. If set to False , and the ResourceTag array is not null, only resources with the specified tags are associated with the policy.
            RemediationEnabled (boolean) -- [REQUIRED]Indicates if the policy should be automatically applied to new resources.
            

    :rtype: dict
    :return: {
        'Policy': {
            'PolicyId': 'string',
            'PolicyName': 'string',
            'PolicyUpdateToken': 'string',
            'SecurityServicePolicyData': {
                'Type': 'WAF',
                'ManagedServiceData': 'string'
            },
            'ResourceType': 'string',
            'ResourceTags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'ExcludeResourceTags': True|False,
            'RemediationEnabled': True|False
        },
        'PolicyArn': 'string'
    }
    
    
    """
    pass

