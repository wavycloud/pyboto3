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

def batch_get_resource_config(resourceKeys=None):
    """
    Returns the current configuration for one or more requested resources. The operation also returns a list of resources that are not processed in the current request. If there are no unprocessed resources, the operation returns an empty unprocessedResourceKeys list.
    See also: AWS API Documentation
    
    
    :example: response = client.batch_get_resource_config(
        resourceKeys=[
            {
                'resourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::EventSubscription'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::S3::Bucket'|'AWS::SSM::ManagedInstanceInventory'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::DynamoDB::Table'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution',
                'resourceId': 'string'
            },
        ]
    )
    
    
    :type resourceKeys: list
    :param resourceKeys: [REQUIRED]
            A list of resource keys to be processed with the current request. Each element in the list consists of the resource type and resource ID.
            (dict) --The details that identify a resource within AWS Config, including the resource type and resource ID.
            resourceType (string) -- [REQUIRED]The resource type.
            resourceId (string) -- [REQUIRED]The ID of the resource (for example., sg-xxxxxx).
            
            

    :rtype: dict
    :return: {
        'baseConfigurationItems': [
            {
                'version': 'string',
                'accountId': 'string',
                'configurationItemCaptureTime': datetime(2015, 1, 1),
                'configurationItemStatus': 'OK'|'ResourceDiscovered'|'ResourceNotRecorded'|'ResourceDeleted'|'ResourceDeletedNotRecorded',
                'configurationStateId': 'string',
                'arn': 'string',
                'resourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::EventSubscription'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::S3::Bucket'|'AWS::SSM::ManagedInstanceInventory'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::DynamoDB::Table'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution',
                'resourceId': 'string',
                'resourceName': 'string',
                'awsRegion': 'string',
                'availabilityZone': 'string',
                'resourceCreationTime': datetime(2015, 1, 1),
                'configuration': 'string',
                'supplementaryConfiguration': {
                    'string': 'string'
                }
            },
        ],
        'unprocessedResourceKeys': [
            {
                'resourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::EventSubscription'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::S3::Bucket'|'AWS::SSM::ManagedInstanceInventory'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::DynamoDB::Table'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution',
                'resourceId': 'string'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
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

def delete_aggregation_authorization(AuthorizedAccountId=None, AuthorizedAwsRegion=None):
    """
    Deletes the authorization granted to the specified configuration aggregator account in a specified region.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_aggregation_authorization(
        AuthorizedAccountId='string',
        AuthorizedAwsRegion='string'
    )
    
    
    :type AuthorizedAccountId: string
    :param AuthorizedAccountId: [REQUIRED]
            The 12-digit account ID of the account authorized to aggregate data.
            

    :type AuthorizedAwsRegion: string
    :param AuthorizedAwsRegion: [REQUIRED]
            The region authorized to collect aggregated data.
            

    """
    pass

def delete_config_rule(ConfigRuleName=None):
    """
    Deletes the specified AWS Config rule and all of its evaluation results.
    AWS Config sets the state of a rule to DELETING until the deletion is complete. You cannot update a rule while it is in this state. If you make a PutConfigRule or DeleteConfigRule request for the rule, you will receive a ResourceInUseException .
    You can check the state of a rule by using the DescribeConfigRules request.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_config_rule(
        ConfigRuleName='string'
    )
    
    
    :type ConfigRuleName: string
    :param ConfigRuleName: [REQUIRED]
            The name of the AWS Config rule that you want to delete.
            

    """
    pass

def delete_configuration_aggregator(ConfigurationAggregatorName=None):
    """
    Deletes the specified configuration aggregator and the aggregated data associated with the aggregator.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_configuration_aggregator(
        ConfigurationAggregatorName='string'
    )
    
    
    :type ConfigurationAggregatorName: string
    :param ConfigurationAggregatorName: [REQUIRED]
            The name of the configuration aggregator.
            

    """
    pass

def delete_configuration_recorder(ConfigurationRecorderName=None):
    """
    Deletes the configuration recorder.
    After the configuration recorder is deleted, AWS Config will not record resource configuration changes until you create a new configuration recorder.
    This action does not delete the configuration information that was previously recorded. You will be able to access the previously recorded information by using the GetResourceConfigHistory action, but you will not be able to access this information in the AWS Config console until you create a new configuration recorder.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_configuration_recorder(
        ConfigurationRecorderName='string'
    )
    
    
    :type ConfigurationRecorderName: string
    :param ConfigurationRecorderName: [REQUIRED]
            The name of the configuration recorder to be deleted. You can retrieve the name of your configuration recorder by using the DescribeConfigurationRecorders action.
            

    """
    pass

def delete_delivery_channel(DeliveryChannelName=None):
    """
    Deletes the delivery channel.
    Before you can delete the delivery channel, you must stop the configuration recorder by using the  StopConfigurationRecorder action.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_delivery_channel(
        DeliveryChannelName='string'
    )
    
    
    :type DeliveryChannelName: string
    :param DeliveryChannelName: [REQUIRED]
            The name of the delivery channel to delete.
            

    """
    pass

def delete_evaluation_results(ConfigRuleName=None):
    """
    Deletes the evaluation results for the specified AWS Config rule. You can specify one AWS Config rule per request. After you delete the evaluation results, you can call the  StartConfigRulesEvaluation API to start evaluating your AWS resources against the rule.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_evaluation_results(
        ConfigRuleName='string'
    )
    
    
    :type ConfigRuleName: string
    :param ConfigRuleName: [REQUIRED]
            The name of the AWS Config rule for which you want to delete the evaluation results.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_pending_aggregation_request(RequesterAccountId=None, RequesterAwsRegion=None):
    """
    Deletes pending authorization requests for a specified aggregator account in a specified region.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_pending_aggregation_request(
        RequesterAccountId='string',
        RequesterAwsRegion='string'
    )
    
    
    :type RequesterAccountId: string
    :param RequesterAccountId: [REQUIRED]
            The 12-digit account ID of the account requesting to aggregate data.
            

    :type RequesterAwsRegion: string
    :param RequesterAwsRegion: [REQUIRED]
            The region requesting to aggregate data.
            

    """
    pass

def deliver_config_snapshot(deliveryChannelName=None):
    """
    Schedules delivery of a configuration snapshot to the Amazon S3 bucket in the specified delivery channel. After the delivery has started, AWS Config sends the following notifications using an Amazon SNS topic that you have specified.
    See also: AWS API Documentation
    
    
    :example: response = client.deliver_config_snapshot(
        deliveryChannelName='string'
    )
    
    
    :type deliveryChannelName: string
    :param deliveryChannelName: [REQUIRED]
            The name of the delivery channel through which the snapshot is delivered.
            

    :rtype: dict
    :return: {
        'configSnapshotId': 'string'
    }
    
    
    """
    pass

def describe_aggregate_compliance_by_config_rules(ConfigurationAggregatorName=None, Filters=None, Limit=None, NextToken=None):
    """
    Returns a list of compliant and noncompliant rules with the number of resources for compliant and noncompliant rules.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_aggregate_compliance_by_config_rules(
        ConfigurationAggregatorName='string',
        Filters={
            'ConfigRuleName': 'string',
            'ComplianceType': 'COMPLIANT'|'NON_COMPLIANT'|'NOT_APPLICABLE'|'INSUFFICIENT_DATA',
            'AccountId': 'string',
            'AwsRegion': 'string'
        },
        Limit=123,
        NextToken='string'
    )
    
    
    :type ConfigurationAggregatorName: string
    :param ConfigurationAggregatorName: [REQUIRED]
            The name of the configuration aggregator.
            

    :type Filters: dict
    :param Filters: Filters the results by ConfigRuleComplianceFilters object.
            ConfigRuleName (string) --The name of the AWS Config rule.
            ComplianceType (string) --The rule compliance status.
            For the ConfigRuleComplianceFilters data type, AWS Config supports only COMPLIANT and NON_COMPLIANT . AWS Config does not support the NOT_APPLICABLE and the INSUFFICIENT_DATA values.
            AccountId (string) --The 12-digit account ID of the source account.
            AwsRegion (string) --The source region where the data is aggregated.
            

    :type Limit: integer
    :param Limit: The maximum number of evaluation results returned on each page. The default is maximum. If you specify 0, AWS Config uses the default.

    :type NextToken: string
    :param NextToken: The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.

    :rtype: dict
    :return: {
        'AggregateComplianceByConfigRules': [
            {
                'ConfigRuleName': 'string',
                'Compliance': {
                    'ComplianceType': 'COMPLIANT'|'NON_COMPLIANT'|'NOT_APPLICABLE'|'INSUFFICIENT_DATA',
                    'ComplianceContributorCount': {
                        'CappedCount': 123,
                        'CapExceeded': True|False
                    }
                },
                'AccountId': 'string',
                'AwsRegion': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def describe_aggregation_authorizations(Limit=None, NextToken=None):
    """
    Returns a list of authorizations granted to various aggregator accounts and regions.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_aggregation_authorizations(
        Limit=123,
        NextToken='string'
    )
    
    
    :type Limit: integer
    :param Limit: The maximum number of AggregationAuthorizations returned on each page. The default is maximum. If you specify 0, AWS Config uses the default.

    :type NextToken: string
    :param NextToken: The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.

    :rtype: dict
    :return: {
        'AggregationAuthorizations': [
            {
                'AggregationAuthorizationArn': 'string',
                'AuthorizedAccountId': 'string',
                'AuthorizedAwsRegion': 'string',
                'CreationTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def describe_compliance_by_config_rule(ConfigRuleNames=None, ComplianceTypes=None, NextToken=None):
    """
    Indicates whether the specified AWS Config rules are compliant. If a rule is noncompliant, this action returns the number of AWS resources that do not comply with the rule.
    A rule is compliant if all of the evaluated resources comply with it. It is noncompliant if any of these resources do not comply.
    If AWS Config has no current evaluation results for the rule, it returns INSUFFICIENT_DATA . This result might indicate one of the following conditions:
    See also: AWS API Documentation
    
    
    :example: response = client.describe_compliance_by_config_rule(
        ConfigRuleNames=[
            'string',
        ],
        ComplianceTypes=[
            'COMPLIANT'|'NON_COMPLIANT'|'NOT_APPLICABLE'|'INSUFFICIENT_DATA',
        ],
        NextToken='string'
    )
    
    
    :type ConfigRuleNames: list
    :param ConfigRuleNames: Specify one or more AWS Config rule names to filter the results by rule.
            (string) --
            

    :type ComplianceTypes: list
    :param ComplianceTypes: Filters the results by compliance.
            The allowed values are COMPLIANT , NON_COMPLIANT , and INSUFFICIENT_DATA .
            (string) --
            

    :type NextToken: string
    :param NextToken: The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.

    :rtype: dict
    :return: {
        'ComplianceByConfigRules': [
            {
                'ConfigRuleName': 'string',
                'Compliance': {
                    'ComplianceType': 'COMPLIANT'|'NON_COMPLIANT'|'NOT_APPLICABLE'|'INSUFFICIENT_DATA',
                    'ComplianceContributorCount': {
                        'CappedCount': 123,
                        'CapExceeded': True|False
                    }
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    ConfigRuleNames (list) -- Specify one or more AWS Config rule names to filter the results by rule.
    
    (string) --
    
    
    ComplianceTypes (list) -- Filters the results by compliance.
    The allowed values are COMPLIANT , NON_COMPLIANT , and INSUFFICIENT_DATA .
    
    (string) --
    
    
    NextToken (string) -- The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.
    
    """
    pass

def describe_compliance_by_resource(ResourceType=None, ResourceId=None, ComplianceTypes=None, Limit=None, NextToken=None):
    """
    Indicates whether the specified AWS resources are compliant. If a resource is noncompliant, this action returns the number of AWS Config rules that the resource does not comply with.
    A resource is compliant if it complies with all the AWS Config rules that evaluate it. It is noncompliant if it does not comply with one or more of these rules.
    If AWS Config has no current evaluation results for the resource, it returns INSUFFICIENT_DATA . This result might indicate one of the following conditions about the rules that evaluate the resource:
    See also: AWS API Documentation
    
    
    :example: response = client.describe_compliance_by_resource(
        ResourceType='string',
        ResourceId='string',
        ComplianceTypes=[
            'COMPLIANT'|'NON_COMPLIANT'|'NOT_APPLICABLE'|'INSUFFICIENT_DATA',
        ],
        Limit=123,
        NextToken='string'
    )
    
    
    :type ResourceType: string
    :param ResourceType: The types of AWS resources for which you want compliance information (for example, AWS::EC2::Instance ). For this action, you can specify that the resource type is an AWS account by specifying AWS::::Account .

    :type ResourceId: string
    :param ResourceId: The ID of the AWS resource for which you want compliance information. You can specify only one resource ID. If you specify a resource ID, you must also specify a type for ResourceType .

    :type ComplianceTypes: list
    :param ComplianceTypes: Filters the results by compliance.
            The allowed values are COMPLIANT and NON_COMPLIANT .
            (string) --
            

    :type Limit: integer
    :param Limit: The maximum number of evaluation results returned on each page. The default is 10. You cannot specify a number greater than 100. If you specify 0, AWS Config uses the default.

    :type NextToken: string
    :param NextToken: The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.

    :rtype: dict
    :return: {
        'ComplianceByResources': [
            {
                'ResourceType': 'string',
                'ResourceId': 'string',
                'Compliance': {
                    'ComplianceType': 'COMPLIANT'|'NON_COMPLIANT'|'NOT_APPLICABLE'|'INSUFFICIENT_DATA',
                    'ComplianceContributorCount': {
                        'CappedCount': 123,
                        'CapExceeded': True|False
                    }
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    ResourceType (string) -- The types of AWS resources for which you want compliance information (for example, AWS::EC2::Instance ). For this action, you can specify that the resource type is an AWS account by specifying AWS::::Account .
    ResourceId (string) -- The ID of the AWS resource for which you want compliance information. You can specify only one resource ID. If you specify a resource ID, you must also specify a type for ResourceType .
    ComplianceTypes (list) -- Filters the results by compliance.
    The allowed values are COMPLIANT and NON_COMPLIANT .
    
    (string) --
    
    
    Limit (integer) -- The maximum number of evaluation results returned on each page. The default is 10. You cannot specify a number greater than 100. If you specify 0, AWS Config uses the default.
    NextToken (string) -- The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.
    
    """
    pass

def describe_config_rule_evaluation_status(ConfigRuleNames=None, NextToken=None, Limit=None):
    """
    Returns status information for each of your AWS managed Config rules. The status includes information such as the last time AWS Config invoked the rule, the last time AWS Config failed to invoke the rule, and the related error for the last failure.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_config_rule_evaluation_status(
        ConfigRuleNames=[
            'string',
        ],
        NextToken='string',
        Limit=123
    )
    
    
    :type ConfigRuleNames: list
    :param ConfigRuleNames: The name of the AWS managed Config rules for which you want status information. If you do not specify any names, AWS Config returns status information for all AWS managed Config rules that you use.
            (string) --
            

    :type NextToken: string
    :param NextToken: The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.

    :type Limit: integer
    :param Limit: The number of rule evaluation results that you want returned.
            This parameter is required if the rule limit for your account is more than the default of 50 rules.
            For information about requesting a rule limit increase, see AWS Config Limits in the AWS General Reference Guide .
            

    :rtype: dict
    :return: {
        'ConfigRulesEvaluationStatus': [
            {
                'ConfigRuleName': 'string',
                'ConfigRuleArn': 'string',
                'ConfigRuleId': 'string',
                'LastSuccessfulInvocationTime': datetime(2015, 1, 1),
                'LastFailedInvocationTime': datetime(2015, 1, 1),
                'LastSuccessfulEvaluationTime': datetime(2015, 1, 1),
                'LastFailedEvaluationTime': datetime(2015, 1, 1),
                'FirstActivatedTime': datetime(2015, 1, 1),
                'LastErrorCode': 'string',
                'LastErrorMessage': 'string',
                'FirstEvaluationStarted': True|False
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    true - AWS Config has evaluated your AWS resources against the rule at least once.
    false - AWS Config has not once finished evaluating your AWS resources against the rule.
    
    """
    pass

def describe_config_rules(ConfigRuleNames=None, NextToken=None):
    """
    Returns details about your AWS Config rules.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_config_rules(
        ConfigRuleNames=[
            'string',
        ],
        NextToken='string'
    )
    
    
    :type ConfigRuleNames: list
    :param ConfigRuleNames: The names of the AWS Config rules for which you want details. If you do not specify any names, AWS Config returns details for all your rules.
            (string) --
            

    :type NextToken: string
    :param NextToken: The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.

    :rtype: dict
    :return: {
        'ConfigRules': [
            {
                'ConfigRuleName': 'string',
                'ConfigRuleArn': 'string',
                'ConfigRuleId': 'string',
                'Description': 'string',
                'Scope': {
                    'ComplianceResourceTypes': [
                        'string',
                    ],
                    'TagKey': 'string',
                    'TagValue': 'string',
                    'ComplianceResourceId': 'string'
                },
                'Source': {
                    'Owner': 'CUSTOM_LAMBDA'|'AWS',
                    'SourceIdentifier': 'string',
                    'SourceDetails': [
                        {
                            'EventSource': 'aws.config',
                            'MessageType': 'ConfigurationItemChangeNotification'|'ConfigurationSnapshotDeliveryCompleted'|'ScheduledNotification'|'OversizedConfigurationItemChangeNotification',
                            'MaximumExecutionFrequency': 'One_Hour'|'Three_Hours'|'Six_Hours'|'Twelve_Hours'|'TwentyFour_Hours'
                        },
                    ]
                },
                'InputParameters': 'string',
                'MaximumExecutionFrequency': 'One_Hour'|'Three_Hours'|'Six_Hours'|'Twelve_Hours'|'TwentyFour_Hours',
                'ConfigRuleState': 'ACTIVE'|'DELETING'|'DELETING_RESULTS'|'EVALUATING'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_configuration_aggregator_sources_status(ConfigurationAggregatorName=None, UpdateStatus=None, NextToken=None, Limit=None):
    """
    Returns status information for sources within an aggregator. The status includes information about the last time AWS Config aggregated data from source accounts or AWS Config failed to aggregate data from source accounts with the related error code or message.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_configuration_aggregator_sources_status(
        ConfigurationAggregatorName='string',
        UpdateStatus=[
            'FAILED'|'SUCCEEDED'|'OUTDATED',
        ],
        NextToken='string',
        Limit=123
    )
    
    
    :type ConfigurationAggregatorName: string
    :param ConfigurationAggregatorName: [REQUIRED]
            The name of the configuration aggregator.
            

    :type UpdateStatus: list
    :param UpdateStatus: Filters the status type.
            Valid value FAILED indicates errors while moving data.
            Valid value SUCCEEDED indicates the data was successfully moved.
            Valid value OUTDATED indicates the data is not the most recent.
            (string) --
            

    :type NextToken: string
    :param NextToken: The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.

    :type Limit: integer
    :param Limit: The maximum number of AggregatorSourceStatus returned on each page. The default is maximum. If you specify 0, AWS Config uses the default.

    :rtype: dict
    :return: {
        'AggregatedSourceStatusList': [
            {
                'SourceId': 'string',
                'SourceType': 'ACCOUNT'|'ORGANIZATION',
                'AwsRegion': 'string',
                'LastUpdateStatus': 'FAILED'|'SUCCEEDED'|'OUTDATED',
                'LastUpdateTime': datetime(2015, 1, 1),
                'LastErrorCode': 'string',
                'LastErrorMessage': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Valid value FAILED indicates errors while moving data.
    Valid value SUCCEEDED indicates the data was successfully moved.
    Valid value OUTDATED indicates the data is not the most recent.
    
    """
    pass

def describe_configuration_aggregators(ConfigurationAggregatorNames=None, NextToken=None, Limit=None):
    """
    Returns the details of one or more configuration aggregators. If the configuration aggregator is not specified, this action returns the details for all the configuration aggregators associated with the account.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_configuration_aggregators(
        ConfigurationAggregatorNames=[
            'string',
        ],
        NextToken='string',
        Limit=123
    )
    
    
    :type ConfigurationAggregatorNames: list
    :param ConfigurationAggregatorNames: The name of the configuration aggregators.
            (string) --
            

    :type NextToken: string
    :param NextToken: The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.

    :type Limit: integer
    :param Limit: The maximum number of configuration aggregators returned on each page. The default is maximum. If you specify 0, AWS Config uses the default.

    :rtype: dict
    :return: {
        'ConfigurationAggregators': [
            {
                'ConfigurationAggregatorName': 'string',
                'ConfigurationAggregatorArn': 'string',
                'AccountAggregationSources': [
                    {
                        'AccountIds': [
                            'string',
                        ],
                        'AllAwsRegions': True|False,
                        'AwsRegions': [
                            'string',
                        ]
                    },
                ],
                'OrganizationAggregationSource': {
                    'RoleArn': 'string',
                    'AwsRegions': [
                        'string',
                    ],
                    'AllAwsRegions': True|False
                },
                'CreationTime': datetime(2015, 1, 1),
                'LastUpdatedTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_configuration_recorder_status(ConfigurationRecorderNames=None):
    """
    Returns the current status of the specified configuration recorder. If a configuration recorder is not specified, this action returns the status of all configuration recorders associated with the account.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_configuration_recorder_status(
        ConfigurationRecorderNames=[
            'string',
        ]
    )
    
    
    :type ConfigurationRecorderNames: list
    :param ConfigurationRecorderNames: The name(s) of the configuration recorder. If the name is not specified, the action returns the current status of all the configuration recorders associated with the account.
            (string) --
            

    :rtype: dict
    :return: {
        'ConfigurationRecordersStatus': [
            {
                'name': 'string',
                'lastStartTime': datetime(2015, 1, 1),
                'lastStopTime': datetime(2015, 1, 1),
                'recording': True|False,
                'lastStatus': 'Pending'|'Success'|'Failure',
                'lastErrorCode': 'string',
                'lastErrorMessage': 'string',
                'lastStatusChangeTime': datetime(2015, 1, 1)
            },
        ]
    }
    
    
    """
    pass

def describe_configuration_recorders(ConfigurationRecorderNames=None):
    """
    Returns the details for the specified configuration recorders. If the configuration recorder is not specified, this action returns the details for all configuration recorders associated with the account.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_configuration_recorders(
        ConfigurationRecorderNames=[
            'string',
        ]
    )
    
    
    :type ConfigurationRecorderNames: list
    :param ConfigurationRecorderNames: A list of configuration recorder names.
            (string) --
            

    :rtype: dict
    :return: {
        'ConfigurationRecorders': [
            {
                'name': 'string',
                'roleARN': 'string',
                'recordingGroup': {
                    'allSupported': True|False,
                    'includeGlobalResourceTypes': True|False,
                    'resourceTypes': [
                        'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::EventSubscription'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::S3::Bucket'|'AWS::SSM::ManagedInstanceInventory'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::DynamoDB::Table'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution',
                    ]
                }
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_delivery_channel_status(DeliveryChannelNames=None):
    """
    Returns the current status of the specified delivery channel. If a delivery channel is not specified, this action returns the current status of all delivery channels associated with the account.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_delivery_channel_status(
        DeliveryChannelNames=[
            'string',
        ]
    )
    
    
    :type DeliveryChannelNames: list
    :param DeliveryChannelNames: A list of delivery channel names.
            (string) --
            

    :rtype: dict
    :return: {
        'DeliveryChannelsStatus': [
            {
                'name': 'string',
                'configSnapshotDeliveryInfo': {
                    'lastStatus': 'Success'|'Failure'|'Not_Applicable',
                    'lastErrorCode': 'string',
                    'lastErrorMessage': 'string',
                    'lastAttemptTime': datetime(2015, 1, 1),
                    'lastSuccessfulTime': datetime(2015, 1, 1),
                    'nextDeliveryTime': datetime(2015, 1, 1)
                },
                'configHistoryDeliveryInfo': {
                    'lastStatus': 'Success'|'Failure'|'Not_Applicable',
                    'lastErrorCode': 'string',
                    'lastErrorMessage': 'string',
                    'lastAttemptTime': datetime(2015, 1, 1),
                    'lastSuccessfulTime': datetime(2015, 1, 1),
                    'nextDeliveryTime': datetime(2015, 1, 1)
                },
                'configStreamDeliveryInfo': {
                    'lastStatus': 'Success'|'Failure'|'Not_Applicable',
                    'lastErrorCode': 'string',
                    'lastErrorMessage': 'string',
                    'lastStatusChangeTime': datetime(2015, 1, 1)
                }
            },
        ]
    }
    
    
    """
    pass

def describe_delivery_channels(DeliveryChannelNames=None):
    """
    Returns details about the specified delivery channel. If a delivery channel is not specified, this action returns the details of all delivery channels associated with the account.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_delivery_channels(
        DeliveryChannelNames=[
            'string',
        ]
    )
    
    
    :type DeliveryChannelNames: list
    :param DeliveryChannelNames: A list of delivery channel names.
            (string) --
            

    :rtype: dict
    :return: {
        'DeliveryChannels': [
            {
                'name': 'string',
                's3BucketName': 'string',
                's3KeyPrefix': 'string',
                'snsTopicARN': 'string',
                'configSnapshotDeliveryProperties': {
                    'deliveryFrequency': 'One_Hour'|'Three_Hours'|'Six_Hours'|'Twelve_Hours'|'TwentyFour_Hours'
                }
            },
        ]
    }
    
    
    """
    pass

def describe_pending_aggregation_requests(Limit=None, NextToken=None):
    """
    Returns a list of all pending aggregation requests.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_pending_aggregation_requests(
        Limit=123,
        NextToken='string'
    )
    
    
    :type Limit: integer
    :param Limit: The maximum number of evaluation results returned on each page. The default is maximum. If you specify 0, AWS Config uses the default.

    :type NextToken: string
    :param NextToken: The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.

    :rtype: dict
    :return: {
        'PendingAggregationRequests': [
            {
                'RequesterAccountId': 'string',
                'RequesterAwsRegion': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
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

def get_aggregate_compliance_details_by_config_rule(ConfigurationAggregatorName=None, ConfigRuleName=None, AccountId=None, AwsRegion=None, ComplianceType=None, Limit=None, NextToken=None):
    """
    Returns the evaluation results for the specified AWS Config rule for a specific resource in a rule. The results indicate which AWS resources were evaluated by the rule, when each resource was last evaluated, and whether each resource complies with the rule.
    See also: AWS API Documentation
    
    
    :example: response = client.get_aggregate_compliance_details_by_config_rule(
        ConfigurationAggregatorName='string',
        ConfigRuleName='string',
        AccountId='string',
        AwsRegion='string',
        ComplianceType='COMPLIANT'|'NON_COMPLIANT'|'NOT_APPLICABLE'|'INSUFFICIENT_DATA',
        Limit=123,
        NextToken='string'
    )
    
    
    :type ConfigurationAggregatorName: string
    :param ConfigurationAggregatorName: [REQUIRED]
            The name of the configuration aggregator.
            

    :type ConfigRuleName: string
    :param ConfigRuleName: [REQUIRED]
            The name of the AWS Config rule for which you want compliance information.
            

    :type AccountId: string
    :param AccountId: [REQUIRED]
            The 12-digit account ID of the source account.
            

    :type AwsRegion: string
    :param AwsRegion: [REQUIRED]
            The source region from where the data is aggregated.
            

    :type ComplianceType: string
    :param ComplianceType: The resource compliance status.
            Note
            For the GetAggregateComplianceDetailsByConfigRuleRequest data type, AWS Config supports only the COMPLIANT and NON_COMPLIANT . AWS Config does not support the NOT_APPLICABLE and INSUFFICIENT_DATA values.
            

    :type Limit: integer
    :param Limit: The maximum number of evaluation results returned on each page. The default is 50. You cannot specify a number greater than 100. If you specify 0, AWS Config uses the default.

    :type NextToken: string
    :param NextToken: The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.

    :rtype: dict
    :return: {
        'AggregateEvaluationResults': [
            {
                'EvaluationResultIdentifier': {
                    'EvaluationResultQualifier': {
                        'ConfigRuleName': 'string',
                        'ResourceType': 'string',
                        'ResourceId': 'string'
                    },
                    'OrderingTimestamp': datetime(2015, 1, 1)
                },
                'ComplianceType': 'COMPLIANT'|'NON_COMPLIANT'|'NOT_APPLICABLE'|'INSUFFICIENT_DATA',
                'ResultRecordedTime': datetime(2015, 1, 1),
                'ConfigRuleInvokedTime': datetime(2015, 1, 1),
                'Annotation': 'string',
                'AccountId': 'string',
                'AwsRegion': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def get_aggregate_config_rule_compliance_summary(ConfigurationAggregatorName=None, Filters=None, GroupByKey=None, Limit=None, NextToken=None):
    """
    Returns the number of compliant and noncompliant rules for one or more accounts and regions in an aggregator.
    See also: AWS API Documentation
    
    
    :example: response = client.get_aggregate_config_rule_compliance_summary(
        ConfigurationAggregatorName='string',
        Filters={
            'AccountId': 'string',
            'AwsRegion': 'string'
        },
        GroupByKey='ACCOUNT_ID'|'AWS_REGION',
        Limit=123,
        NextToken='string'
    )
    
    
    :type ConfigurationAggregatorName: string
    :param ConfigurationAggregatorName: [REQUIRED]
            The name of the configuration aggregator.
            

    :type Filters: dict
    :param Filters: Filters the results based on the ConfigRuleComplianceSummaryFilters object.
            AccountId (string) --The 12-digit account ID of the source account.
            AwsRegion (string) --The source region where the data is aggregated.
            

    :type GroupByKey: string
    :param GroupByKey: Groups the result based on ACCOUNT_ID or AWS_REGION.

    :type Limit: integer
    :param Limit: The maximum number of evaluation results returned on each page. The default is 1000. You cannot specify a number greater than 1000. If you specify 0, AWS Config uses the default.

    :type NextToken: string
    :param NextToken: The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.

    :rtype: dict
    :return: {
        'GroupByKey': 'string',
        'AggregateComplianceCounts': [
            {
                'GroupName': 'string',
                'ComplianceSummary': {
                    'CompliantResourceCount': {
                        'CappedCount': 123,
                        'CapExceeded': True|False
                    },
                    'NonCompliantResourceCount': {
                        'CappedCount': 123,
                        'CapExceeded': True|False
                    },
                    'ComplianceSummaryTimestamp': datetime(2015, 1, 1)
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def get_compliance_details_by_config_rule(ConfigRuleName=None, ComplianceTypes=None, Limit=None, NextToken=None):
    """
    Returns the evaluation results for the specified AWS Config rule. The results indicate which AWS resources were evaluated by the rule, when each resource was last evaluated, and whether each resource complies with the rule.
    See also: AWS API Documentation
    
    
    :example: response = client.get_compliance_details_by_config_rule(
        ConfigRuleName='string',
        ComplianceTypes=[
            'COMPLIANT'|'NON_COMPLIANT'|'NOT_APPLICABLE'|'INSUFFICIENT_DATA',
        ],
        Limit=123,
        NextToken='string'
    )
    
    
    :type ConfigRuleName: string
    :param ConfigRuleName: [REQUIRED]
            The name of the AWS Config rule for which you want compliance information.
            

    :type ComplianceTypes: list
    :param ComplianceTypes: Filters the results by compliance.
            The allowed values are COMPLIANT , NON_COMPLIANT , and NOT_APPLICABLE .
            (string) --
            

    :type Limit: integer
    :param Limit: The maximum number of evaluation results returned on each page. The default is 10. You cannot specify a number greater than 100. If you specify 0, AWS Config uses the default.

    :type NextToken: string
    :param NextToken: The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.

    :rtype: dict
    :return: {
        'EvaluationResults': [
            {
                'EvaluationResultIdentifier': {
                    'EvaluationResultQualifier': {
                        'ConfigRuleName': 'string',
                        'ResourceType': 'string',
                        'ResourceId': 'string'
                    },
                    'OrderingTimestamp': datetime(2015, 1, 1)
                },
                'ComplianceType': 'COMPLIANT'|'NON_COMPLIANT'|'NOT_APPLICABLE'|'INSUFFICIENT_DATA',
                'ResultRecordedTime': datetime(2015, 1, 1),
                'ConfigRuleInvokedTime': datetime(2015, 1, 1),
                'Annotation': 'string',
                'ResultToken': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def get_compliance_details_by_resource(ResourceType=None, ResourceId=None, ComplianceTypes=None, NextToken=None):
    """
    Returns the evaluation results for the specified AWS resource. The results indicate which AWS Config rules were used to evaluate the resource, when each rule was last used, and whether the resource complies with each rule.
    See also: AWS API Documentation
    
    
    :example: response = client.get_compliance_details_by_resource(
        ResourceType='string',
        ResourceId='string',
        ComplianceTypes=[
            'COMPLIANT'|'NON_COMPLIANT'|'NOT_APPLICABLE'|'INSUFFICIENT_DATA',
        ],
        NextToken='string'
    )
    
    
    :type ResourceType: string
    :param ResourceType: [REQUIRED]
            The type of the AWS resource for which you want compliance information.
            

    :type ResourceId: string
    :param ResourceId: [REQUIRED]
            The ID of the AWS resource for which you want compliance information.
            

    :type ComplianceTypes: list
    :param ComplianceTypes: Filters the results by compliance.
            The allowed values are COMPLIANT , NON_COMPLIANT , and NOT_APPLICABLE .
            (string) --
            

    :type NextToken: string
    :param NextToken: The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.

    :rtype: dict
    :return: {
        'EvaluationResults': [
            {
                'EvaluationResultIdentifier': {
                    'EvaluationResultQualifier': {
                        'ConfigRuleName': 'string',
                        'ResourceType': 'string',
                        'ResourceId': 'string'
                    },
                    'OrderingTimestamp': datetime(2015, 1, 1)
                },
                'ComplianceType': 'COMPLIANT'|'NON_COMPLIANT'|'NOT_APPLICABLE'|'INSUFFICIENT_DATA',
                'ResultRecordedTime': datetime(2015, 1, 1),
                'ConfigRuleInvokedTime': datetime(2015, 1, 1),
                'Annotation': 'string',
                'ResultToken': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def get_compliance_summary_by_config_rule():
    """
    Returns the number of AWS Config rules that are compliant and noncompliant, up to a maximum of 25 for each.
    See also: AWS API Documentation
    
    
    :example: response = client.get_compliance_summary_by_config_rule()
    
    
    :rtype: dict
    :return: {
        'ComplianceSummary': {
            'CompliantResourceCount': {
                'CappedCount': 123,
                'CapExceeded': True|False
            },
            'NonCompliantResourceCount': {
                'CappedCount': 123,
                'CapExceeded': True|False
            },
            'ComplianceSummaryTimestamp': datetime(2015, 1, 1)
        }
    }
    
    
    """
    pass

def get_compliance_summary_by_resource_type(ResourceTypes=None):
    """
    Returns the number of resources that are compliant and the number that are noncompliant. You can specify one or more resource types to get these numbers for each resource type. The maximum number returned is 100.
    See also: AWS API Documentation
    
    
    :example: response = client.get_compliance_summary_by_resource_type(
        ResourceTypes=[
            'string',
        ]
    )
    
    
    :type ResourceTypes: list
    :param ResourceTypes: Specify one or more resource types to get the number of resources that are compliant and the number that are noncompliant for each resource type.
            For this request, you can specify an AWS resource type such as AWS::EC2::Instance . You can specify that the resource type is an AWS account by specifying AWS::::Account .
            (string) --
            

    :rtype: dict
    :return: {
        'ComplianceSummariesByResourceType': [
            {
                'ResourceType': 'string',
                'ComplianceSummary': {
                    'CompliantResourceCount': {
                        'CappedCount': 123,
                        'CapExceeded': True|False
                    },
                    'NonCompliantResourceCount': {
                        'CappedCount': 123,
                        'CapExceeded': True|False
                    },
                    'ComplianceSummaryTimestamp': datetime(2015, 1, 1)
                }
            },
        ]
    }
    
    
    """
    pass

def get_discovered_resource_counts(resourceTypes=None, limit=None, nextToken=None):
    """
    Returns the resource types, the number of each resource type, and the total number of resources that AWS Config is recording in this region for your AWS account.
    The response is paginated. By default, AWS Config lists 100  ResourceCount objects on each page. You can customize this number with the limit parameter. The response includes a nextToken string. To get the next page of results, run the request again and specify the string for the nextToken parameter.
    See also: AWS API Documentation
    
    
    :example: response = client.get_discovered_resource_counts(
        resourceTypes=[
            'string',
        ],
        limit=123,
        nextToken='string'
    )
    
    
    :type resourceTypes: list
    :param resourceTypes: The comma-separated list that specifies the resource types that you want AWS Config to return (for example, 'AWS::EC2::Instance' , 'AWS::IAM::User' ).
            If a value for resourceTypes is not specified, AWS Config returns all resource types that AWS Config is recording in the region for your account.
            Note
            If the configuration recorder is turned off, AWS Config returns an empty list of ResourceCount objects. If the configuration recorder is not recording a specific resource type (for example, S3 buckets), that resource type is not returned in the list of ResourceCount objects.
            (string) --
            

    :type limit: integer
    :param limit: The maximum number of ResourceCount objects returned on each page. The default is 100. You cannot specify a number greater than 100. If you specify 0, AWS Config uses the default.

    :type nextToken: string
    :param nextToken: The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.

    :rtype: dict
    :return: {
        'totalDiscoveredResources': 123,
        'resourceCounts': [
            {
                'resourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::EventSubscription'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::S3::Bucket'|'AWS::SSM::ManagedInstanceInventory'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::DynamoDB::Table'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution',
                'count': 123
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    You are a new AWS Config customer.
    You just enabled resource recording.
    
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

def get_resource_config_history(resourceType=None, resourceId=None, laterTime=None, earlierTime=None, chronologicalOrder=None, limit=None, nextToken=None):
    """
    Returns a list of configuration items for the specified resource. The list contains details about each state of the resource during the specified time interval.
    The response is paginated. By default, AWS Config returns a limit of 10 configuration items per page. You can customize this number with the limit parameter. The response includes a nextToken string. To get the next page of results, run the request again and specify the string for the nextToken parameter.
    See also: AWS API Documentation
    
    
    :example: response = client.get_resource_config_history(
        resourceType='AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::EventSubscription'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::S3::Bucket'|'AWS::SSM::ManagedInstanceInventory'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::DynamoDB::Table'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution',
        resourceId='string',
        laterTime=datetime(2015, 1, 1),
        earlierTime=datetime(2015, 1, 1),
        chronologicalOrder='Reverse'|'Forward',
        limit=123,
        nextToken='string'
    )
    
    
    :type resourceType: string
    :param resourceType: [REQUIRED]
            The resource type.
            

    :type resourceId: string
    :param resourceId: [REQUIRED]
            The ID of the resource (for example., sg-xxxxxx ).
            

    :type laterTime: datetime
    :param laterTime: The time stamp that indicates a later time. If not specified, current time is taken.

    :type earlierTime: datetime
    :param earlierTime: The time stamp that indicates an earlier time. If not specified, the action returns paginated results that contain configuration items that start when the first configuration item was recorded.

    :type chronologicalOrder: string
    :param chronologicalOrder: The chronological order for configuration items listed. By default, the results are listed in reverse chronological order.

    :type limit: integer
    :param limit: The maximum number of configuration items returned on each page. The default is 10. You cannot specify a number greater than 100. If you specify 0, AWS Config uses the default.

    :type nextToken: string
    :param nextToken: The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.

    :rtype: dict
    :return: {
        'configurationItems': [
            {
                'version': 'string',
                'accountId': 'string',
                'configurationItemCaptureTime': datetime(2015, 1, 1),
                'configurationItemStatus': 'OK'|'ResourceDiscovered'|'ResourceNotRecorded'|'ResourceDeleted'|'ResourceDeletedNotRecorded',
                'configurationStateId': 'string',
                'configurationItemMD5Hash': 'string',
                'arn': 'string',
                'resourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::EventSubscription'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::S3::Bucket'|'AWS::SSM::ManagedInstanceInventory'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::DynamoDB::Table'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution',
                'resourceId': 'string',
                'resourceName': 'string',
                'awsRegion': 'string',
                'availabilityZone': 'string',
                'resourceCreationTime': datetime(2015, 1, 1),
                'tags': {
                    'string': 'string'
                },
                'relatedEvents': [
                    'string',
                ],
                'relationships': [
                    {
                        'resourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::EventSubscription'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::S3::Bucket'|'AWS::SSM::ManagedInstanceInventory'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::DynamoDB::Table'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution',
                        'resourceId': 'string',
                        'resourceName': 'string',
                        'relationshipName': 'string'
                    },
                ],
                'configuration': 'string',
                'supplementaryConfiguration': {
                    'string': 'string'
                }
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def get_waiter(waiter_name=None):
    """
    
    :type waiter_name: 
    :param waiter_name: 

    """
    pass

def list_discovered_resources(resourceType=None, resourceIds=None, resourceName=None, limit=None, includeDeletedResources=None, nextToken=None):
    """
    Accepts a resource type and returns a list of resource identifiers for the resources of that type. A resource identifier includes the resource type, ID, and (if available) the custom resource name. The results consist of resources that AWS Config has discovered, including those that AWS Config is not currently recording. You can narrow the results to include only resources that have specific resource IDs or a resource name.
    The response is paginated. By default, AWS Config lists 100 resource identifiers on each page. You can customize this number with the limit parameter. The response includes a nextToken string. To get the next page of results, run the request again and specify the string for the nextToken parameter.
    See also: AWS API Documentation
    
    
    :example: response = client.list_discovered_resources(
        resourceType='AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::EventSubscription'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::S3::Bucket'|'AWS::SSM::ManagedInstanceInventory'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::DynamoDB::Table'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution',
        resourceIds=[
            'string',
        ],
        resourceName='string',
        limit=123,
        includeDeletedResources=True|False,
        nextToken='string'
    )
    
    
    :type resourceType: string
    :param resourceType: [REQUIRED]
            The type of resources that you want AWS Config to list in the response.
            

    :type resourceIds: list
    :param resourceIds: The IDs of only those resources that you want AWS Config to list in the response. If you do not specify this parameter, AWS Config lists all resources of the specified type that it has discovered.
            (string) --
            

    :type resourceName: string
    :param resourceName: The custom name of only those resources that you want AWS Config to list in the response. If you do not specify this parameter, AWS Config lists all resources of the specified type that it has discovered.

    :type limit: integer
    :param limit: The maximum number of resource identifiers returned on each page. The default is 100. You cannot specify a number greater than 100. If you specify 0, AWS Config uses the default.

    :type includeDeletedResources: boolean
    :param includeDeletedResources: Specifies whether AWS Config includes deleted resources in the results. By default, deleted resources are not included.

    :type nextToken: string
    :param nextToken: The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.

    :rtype: dict
    :return: {
        'resourceIdentifiers': [
            {
                'resourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::EventSubscription'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::S3::Bucket'|'AWS::SSM::ManagedInstanceInventory'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::DynamoDB::Table'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution',
                'resourceId': 'string',
                'resourceName': 'string',
                'resourceDeletionTime': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def put_aggregation_authorization(AuthorizedAccountId=None, AuthorizedAwsRegion=None):
    """
    Authorizes the aggregator account and region to collect data from the source account and region.
    See also: AWS API Documentation
    
    
    :example: response = client.put_aggregation_authorization(
        AuthorizedAccountId='string',
        AuthorizedAwsRegion='string'
    )
    
    
    :type AuthorizedAccountId: string
    :param AuthorizedAccountId: [REQUIRED]
            The 12-digit account ID of the account authorized to aggregate data.
            

    :type AuthorizedAwsRegion: string
    :param AuthorizedAwsRegion: [REQUIRED]
            The region authorized to collect aggregated data.
            

    :rtype: dict
    :return: {
        'AggregationAuthorization': {
            'AggregationAuthorizationArn': 'string',
            'AuthorizedAccountId': 'string',
            'AuthorizedAwsRegion': 'string',
            'CreationTime': datetime(2015, 1, 1)
        }
    }
    
    
    """
    pass

def put_config_rule(ConfigRule=None):
    """
    Adds or updates an AWS Config rule for evaluating whether your AWS resources comply with your desired configurations.
    You can use this action for custom AWS Config rules and AWS managed Config rules. A custom AWS Config rule is a rule that you develop and maintain. An AWS managed Config rule is a customizable, predefined rule that AWS Config provides.
    If you are adding a new custom AWS Config rule, you must first create the AWS Lambda function that the rule invokes to evaluate your resources. When you use the PutConfigRule action to add the rule to AWS Config, you must specify the Amazon Resource Name (ARN) that AWS Lambda assigns to the function. Specify the ARN for the SourceIdentifier key. This key is part of the Source object, which is part of the ConfigRule object.
    If you are adding an AWS managed Config rule, specify the rule's identifier for the SourceIdentifier key. To reference AWS managed Config rule identifiers, see About AWS Managed Config Rules .
    For any new rule that you add, specify the ConfigRuleName in the ConfigRule object. Do not specify the ConfigRuleArn or the ConfigRuleId . These values are generated by AWS Config for new rules.
    If you are updating a rule that you added previously, you can specify the rule by ConfigRuleName , ConfigRuleId , or ConfigRuleArn in the ConfigRule data type that you use in this request.
    The maximum number of rules that AWS Config supports is 50.
    For information about requesting a rule limit increase, see AWS Config Limits in the AWS General Reference Guide .
    For more information about developing and using AWS Config rules, see Evaluating AWS Resource Configurations with AWS Config in the AWS Config Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.put_config_rule(
        ConfigRule={
            'ConfigRuleName': 'string',
            'ConfigRuleArn': 'string',
            'ConfigRuleId': 'string',
            'Description': 'string',
            'Scope': {
                'ComplianceResourceTypes': [
                    'string',
                ],
                'TagKey': 'string',
                'TagValue': 'string',
                'ComplianceResourceId': 'string'
            },
            'Source': {
                'Owner': 'CUSTOM_LAMBDA'|'AWS',
                'SourceIdentifier': 'string',
                'SourceDetails': [
                    {
                        'EventSource': 'aws.config',
                        'MessageType': 'ConfigurationItemChangeNotification'|'ConfigurationSnapshotDeliveryCompleted'|'ScheduledNotification'|'OversizedConfigurationItemChangeNotification',
                        'MaximumExecutionFrequency': 'One_Hour'|'Three_Hours'|'Six_Hours'|'Twelve_Hours'|'TwentyFour_Hours'
                    },
                ]
            },
            'InputParameters': 'string',
            'MaximumExecutionFrequency': 'One_Hour'|'Three_Hours'|'Six_Hours'|'Twelve_Hours'|'TwentyFour_Hours',
            'ConfigRuleState': 'ACTIVE'|'DELETING'|'DELETING_RESULTS'|'EVALUATING'
        }
    )
    
    
    :type ConfigRule: dict
    :param ConfigRule: [REQUIRED]
            The rule that you want to add to your account.
            ConfigRuleName (string) --The name that you assign to the AWS Config rule. The name is required if you are adding a new rule.
            ConfigRuleArn (string) --The Amazon Resource Name (ARN) of the AWS Config rule.
            ConfigRuleId (string) --The ID of the AWS Config rule.
            Description (string) --The description that you provide for the AWS Config rule.
            Scope (dict) --Defines which resources can trigger an evaluation for the rule. The scope can include one or more resource types, a combination of one resource type and one resource ID, or a combination of a tag key and value. Specify a scope to constrain the resources that can trigger an evaluation for the rule. If you do not specify a scope, evaluations are triggered when any resource in the recording group changes.
            ComplianceResourceTypes (list) --The resource types of only those AWS resources that you want to trigger an evaluation for the rule. You can only specify one type if you also specify a resource ID for ComplianceResourceId .
            (string) --
            TagKey (string) --The tag key that is applied to only those AWS resources that you want to trigger an evaluation for the rule.
            TagValue (string) --The tag value applied to only those AWS resources that you want to trigger an evaluation for the rule. If you specify a value for TagValue , you must also specify a value for TagKey .
            ComplianceResourceId (string) --The ID of the only AWS resource that you want to trigger an evaluation for the rule. If you specify a resource ID, you must specify one resource type for ComplianceResourceTypes .
            Source (dict) -- [REQUIRED]Provides the rule owner (AWS or customer), the rule identifier, and the notifications that cause the function to evaluate your AWS resources.
            Owner (string) -- [REQUIRED]Indicates whether AWS or the customer owns and manages the AWS Config rule.
            SourceIdentifier (string) -- [REQUIRED]For AWS Config managed rules, a predefined identifier from a list. For example, IAM_PASSWORD_POLICY is a managed rule. To reference a managed rule, see Using AWS Managed Config Rules .
            For custom rules, the identifier is the Amazon Resource Name (ARN) of the rule's AWS Lambda function, such as arn:aws:lambda:us-east-2:123456789012:function:custom_rule_name .
            SourceDetails (list) --Provides the source and type of the event that causes AWS Config to evaluate your AWS resources.
            (dict) --Provides the source and the message types that trigger AWS Config to evaluate your AWS resources against a rule. It also provides the frequency with which you want AWS Config to run evaluations for the rule if the trigger type is periodic. You can specify the parameter values for SourceDetail only for custom rules.
            EventSource (string) --The source of the event, such as an AWS service, that triggers AWS Config to evaluate your AWS resources.
            MessageType (string) --The type of notification that triggers AWS Config to run an evaluation for a rule. You can specify the following notification types:
            ConfigurationItemChangeNotification - Triggers an evaluation when AWS Config delivers a configuration item as a result of a resource change.
            OversizedConfigurationItemChangeNotification - Triggers an evaluation when AWS Config delivers an oversized configuration item. AWS Config may generate this notification type when a resource changes and the notification exceeds the maximum size allowed by Amazon SNS.
            ScheduledNotification - Triggers a periodic evaluation at the frequency specified for MaximumExecutionFrequency .
            ConfigurationSnapshotDeliveryCompleted - Triggers a periodic evaluation when AWS Config delivers a configuration snapshot.
            If you want your custom rule to be triggered by configuration changes, specify both ConfigurationItemChangeNotification and OversizedConfigurationItemChangeNotification .
            MaximumExecutionFrequency (string) --The frequency at which you want AWS Config to run evaluations for a custom rule with a periodic trigger. If you specify a value for MaximumExecutionFrequency , then MessageType must use the ScheduledNotification value.
            Note
            By default, rules with a periodic trigger are evaluated every 24 hours. To change the frequency, specify a valid value for the MaximumExecutionFrequency parameter.
            Based on the valid value you choose, AWS Config runs evaluations once for each valid value. For example, if you choose Three_Hours , AWS Config runs evaluations once every three hours. In this case, Three_Hours is the frequency of this rule.
            
            
            InputParameters (string) --A string, in JSON format, that is passed to the AWS Config rule Lambda function.
            MaximumExecutionFrequency (string) --The maximum frequency with which AWS Config runs evaluations for a rule. You can specify a value for MaximumExecutionFrequency when:
            You are using an AWS managed rule that is triggered at a periodic frequency.
            Your custom rule is triggered when AWS Config delivers the configuration snapshot. For more information, see ConfigSnapshotDeliveryProperties .
            Note
            By default, rules with a periodic trigger are evaluated every 24 hours. To change the frequency, specify a valid value for the MaximumExecutionFrequency parameter.
            ConfigRuleState (string) --Indicates whether the AWS Config rule is active or is currently being deleted by AWS Config. It can also indicate the evaluation status for the AWS Config rule.
            AWS Config sets the state of the rule to EVALUATING temporarily after you use the StartConfigRulesEvaluation request to evaluate your resources against the AWS Config rule.
            AWS Config sets the state of the rule to DELETING_RESULTS temporarily after you use the DeleteEvaluationResults request to delete the current evaluation results for the AWS Config rule.
            AWS Config temporarily sets the state of a rule to DELETING after you use the DeleteConfigRule request to delete the rule. After AWS Config deletes the rule, the rule and all of its evaluations are erased and are no longer available.
            

    :returns: 
    ConfigurationItemChangeNotification - Triggers an evaluation when AWS Config delivers a configuration item as a result of a resource change.
    OversizedConfigurationItemChangeNotification - Triggers an evaluation when AWS Config delivers an oversized configuration item. AWS Config may generate this notification type when a resource changes and the notification exceeds the maximum size allowed by Amazon SNS.
    ScheduledNotification - Triggers a periodic evaluation at the frequency specified for MaximumExecutionFrequency .
    ConfigurationSnapshotDeliveryCompleted - Triggers a periodic evaluation when AWS Config delivers a configuration snapshot.
    
    """
    pass

def put_configuration_aggregator(ConfigurationAggregatorName=None, AccountAggregationSources=None, OrganizationAggregationSource=None):
    """
    Creates and updates the configuration aggregator with the selected source accounts and regions.
    See also: AWS API Documentation
    
    
    :example: response = client.put_configuration_aggregator(
        ConfigurationAggregatorName='string',
        AccountAggregationSources=[
            {
                'AccountIds': [
                    'string',
                ],
                'AllAwsRegions': True|False,
                'AwsRegions': [
                    'string',
                ]
            },
        ],
        OrganizationAggregationSource={
            'RoleArn': 'string',
            'AwsRegions': [
                'string',
            ],
            'AllAwsRegions': True|False
        }
    )
    
    
    :type ConfigurationAggregatorName: string
    :param ConfigurationAggregatorName: [REQUIRED]
            The name of the configuration aggregator.
            

    :type AccountAggregationSources: list
    :param AccountAggregationSources: A list of AccountAggregationSource object.
            (dict) --A collection of accounts and regions.
            AccountIds (list) -- [REQUIRED]The 12-digit account ID of the account being aggregated.
            (string) --
            AllAwsRegions (boolean) --If true, aggreagate existing AWS Config regions and future regions.
            AwsRegions (list) --The source regions being aggregated.
            (string) --
            
            

    :type OrganizationAggregationSource: dict
    :param OrganizationAggregationSource: An OrganizationAggregationSource object.
            RoleArn (string) -- [REQUIRED]ARN of the IAM role used to retreive AWS Organization details associated with the aggregator account.
            AwsRegions (list) --The source regions being aggregated.
            (string) --
            AllAwsRegions (boolean) --If true, aggreagate existing AWS Config regions and future regions.
            

    :rtype: dict
    :return: {
        'ConfigurationAggregator': {
            'ConfigurationAggregatorName': 'string',
            'ConfigurationAggregatorArn': 'string',
            'AccountAggregationSources': [
                {
                    'AccountIds': [
                        'string',
                    ],
                    'AllAwsRegions': True|False,
                    'AwsRegions': [
                        'string',
                    ]
                },
            ],
            'OrganizationAggregationSource': {
                'RoleArn': 'string',
                'AwsRegions': [
                    'string',
                ],
                'AllAwsRegions': True|False
            },
            'CreationTime': datetime(2015, 1, 1),
            'LastUpdatedTime': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def put_configuration_recorder(ConfigurationRecorder=None):
    """
    Creates a new configuration recorder to record the selected resource configurations.
    You can use this action to change the role roleARN or the recordingGroup of an existing recorder. To change the role, call the action on the existing configuration recorder and specify a role.
    See also: AWS API Documentation
    
    
    :example: response = client.put_configuration_recorder(
        ConfigurationRecorder={
            'name': 'string',
            'roleARN': 'string',
            'recordingGroup': {
                'allSupported': True|False,
                'includeGlobalResourceTypes': True|False,
                'resourceTypes': [
                    'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::EventSubscription'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::S3::Bucket'|'AWS::SSM::ManagedInstanceInventory'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::DynamoDB::Table'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution',
                ]
            }
        }
    )
    
    
    :type ConfigurationRecorder: dict
    :param ConfigurationRecorder: [REQUIRED]
            The configuration recorder object that records each configuration change made to the resources.
            name (string) --The name of the recorder. By default, AWS Config automatically assigns the name 'default' when creating the configuration recorder. You cannot change the assigned name.
            roleARN (string) --Amazon Resource Name (ARN) of the IAM role used to describe the AWS resources associated with the account.
            recordingGroup (dict) --Specifies the types of AWS resources for which AWS Config records configuration changes.
            allSupported (boolean) --Specifies whether AWS Config records configuration changes for every supported type of regional resource.
            If you set this option to true , when AWS Config adds support for a new type of regional resource, it starts recording resources of that type automatically.
            If you set this option to true , you cannot enumerate a list of resourceTypes .
            includeGlobalResourceTypes (boolean) --Specifies whether AWS Config includes all supported types of global resources (for example, IAM resources) with the resources that it records.
            Before you can set this option to true , you must set the allSupported option to true .
            If you set this option to true , when AWS Config adds support for a new type of global resource, it starts recording resources of that type automatically.
            The configuration details for any global resource are the same in all regions. To prevent duplicate configuration items, you should consider customizing AWS Config in only one region to record global resources.
            resourceTypes (list) --A comma-separated list that specifies the types of AWS resources for which AWS Config records configuration changes (for example, AWS::EC2::Instance or AWS::CloudTrail::Trail ).
            Before you can set this option to true , you must set the allSupported option to false .
            If you set this option to true , when AWS Config adds support for a new type of resource, it will not record resources of that type unless you manually add that type to your recording group.
            For a list of valid resourceTypes values, see the resourceType Value column in Supported AWS Resource Types .
            (string) --
            
            

    """
    pass

def put_delivery_channel(DeliveryChannel=None):
    """
    Creates a delivery channel object to deliver configuration information to an Amazon S3 bucket and Amazon SNS topic.
    Before you can create a delivery channel, you must create a configuration recorder.
    You can use this action to change the Amazon S3 bucket or an Amazon SNS topic of the existing delivery channel. To change the Amazon S3 bucket or an Amazon SNS topic, call this action and specify the changed values for the S3 bucket and the SNS topic. If you specify a different value for either the S3 bucket or the SNS topic, this action will keep the existing value for the parameter that is not changed.
    See also: AWS API Documentation
    
    
    :example: response = client.put_delivery_channel(
        DeliveryChannel={
            'name': 'string',
            's3BucketName': 'string',
            's3KeyPrefix': 'string',
            'snsTopicARN': 'string',
            'configSnapshotDeliveryProperties': {
                'deliveryFrequency': 'One_Hour'|'Three_Hours'|'Six_Hours'|'Twelve_Hours'|'TwentyFour_Hours'
            }
        }
    )
    
    
    :type DeliveryChannel: dict
    :param DeliveryChannel: [REQUIRED]
            The configuration delivery channel object that delivers the configuration information to an Amazon S3 bucket and to an Amazon SNS topic.
            name (string) --The name of the delivery channel. By default, AWS Config assigns the name 'default' when creating the delivery channel. To change the delivery channel name, you must use the DeleteDeliveryChannel action to delete your current delivery channel, and then you must use the PutDeliveryChannel command to create a delivery channel that has the desired name.
            s3BucketName (string) --The name of the Amazon S3 bucket to which AWS Config delivers configuration snapshots and configuration history files.
            If you specify a bucket that belongs to another AWS account, that bucket must have policies that grant access permissions to AWS Config. For more information, see Permissions for the Amazon S3 Bucket in the AWS Config Developer Guide.
            s3KeyPrefix (string) --The prefix for the specified Amazon S3 bucket.
            snsTopicARN (string) --The Amazon Resource Name (ARN) of the Amazon SNS topic to which AWS Config sends notifications about configuration changes.
            If you choose a topic from another account, the topic must have policies that grant access permissions to AWS Config. For more information, see Permissions for the Amazon SNS Topic in the AWS Config Developer Guide.
            configSnapshotDeliveryProperties (dict) --The options for how often AWS Config delivers configuration snapshots to the Amazon S3 bucket.
            deliveryFrequency (string) --The frequency with which AWS Config delivers configuration snapshots.
            
            

    """
    pass

def put_evaluations(Evaluations=None, ResultToken=None, TestMode=None):
    """
    Used by an AWS Lambda function to deliver evaluation results to AWS Config. This action is required in every AWS Lambda function that is invoked by an AWS Config rule.
    See also: AWS API Documentation
    
    
    :example: response = client.put_evaluations(
        Evaluations=[
            {
                'ComplianceResourceType': 'string',
                'ComplianceResourceId': 'string',
                'ComplianceType': 'COMPLIANT'|'NON_COMPLIANT'|'NOT_APPLICABLE'|'INSUFFICIENT_DATA',
                'Annotation': 'string',
                'OrderingTimestamp': datetime(2015, 1, 1)
            },
        ],
        ResultToken='string',
        TestMode=True|False
    )
    
    
    :type Evaluations: list
    :param Evaluations: The assessments that the AWS Lambda function performs. Each evaluation identifies an AWS resource and indicates whether it complies with the AWS Config rule that invokes the AWS Lambda function.
            (dict) --Identifies an AWS resource and indicates whether it complies with the AWS Config rule that it was evaluated against.
            ComplianceResourceType (string) -- [REQUIRED]The type of AWS resource that was evaluated.
            ComplianceResourceId (string) -- [REQUIRED]The ID of the AWS resource that was evaluated.
            ComplianceType (string) -- [REQUIRED]Indicates whether the AWS resource complies with the AWS Config rule that it was evaluated against.
            For the Evaluation data type, AWS Config supports only the COMPLIANT , NON_COMPLIANT , and NOT_APPLICABLE values. AWS Config does not support the INSUFFICIENT_DATA value for this data type.
            Similarly, AWS Config does not accept INSUFFICIENT_DATA as the value for ComplianceType from a PutEvaluations request. For example, an AWS Lambda function for a custom AWS Config rule cannot pass an INSUFFICIENT_DATA value to AWS Config.
            Annotation (string) --Supplementary information about how the evaluation determined the compliance.
            OrderingTimestamp (datetime) -- [REQUIRED]The time of the event in AWS Config that triggered the evaluation. For event-based evaluations, the time indicates when AWS Config created the configuration item that triggered the evaluation. For periodic evaluations, the time indicates when AWS Config triggered the evaluation at the frequency that you specified (for example, every 24 hours).
            
            

    :type ResultToken: string
    :param ResultToken: [REQUIRED]
            An encrypted token that associates an evaluation with an AWS Config rule. Identifies the rule and the event that triggered the evaluation.
            

    :type TestMode: boolean
    :param TestMode: Use this parameter to specify a test run for PutEvaluations . You can verify whether your AWS Lambda function will deliver evaluation results to AWS Config. No updates occur to your existing evaluations, and evaluation results are not sent to AWS Config.
            Note
            When TestMode is true , PutEvaluations doesn't require a valid value for the ResultToken parameter, but the value cannot be null.
            

    :rtype: dict
    :return: {
        'FailedEvaluations': [
            {
                'ComplianceResourceType': 'string',
                'ComplianceResourceId': 'string',
                'ComplianceType': 'COMPLIANT'|'NON_COMPLIANT'|'NOT_APPLICABLE'|'INSUFFICIENT_DATA',
                'Annotation': 'string',
                'OrderingTimestamp': datetime(2015, 1, 1)
            },
        ]
    }
    
    
    """
    pass

def start_config_rules_evaluation(ConfigRuleNames=None):
    """
    Runs an on-demand evaluation for the specified AWS Config rules against the last known configuration state of the resources. Use StartConfigRulesEvaluation when you want to test that a rule you updated is working as expected. StartConfigRulesEvaluation does not re-record the latest configuration state for your resources. It re-runs an evaluation against the last known state of your resources.
    You can specify up to 25 AWS Config rules per request.
    An existing StartConfigRulesEvaluation call for the specified rules must complete before you can call the API again. If you chose to have AWS Config stream to an Amazon SNS topic, you will receive a ConfigRuleEvaluationStarted notification when the evaluation starts.
    The StartConfigRulesEvaluation API is useful if you want to run on-demand evaluations, such as the following example:
    See also: AWS API Documentation
    
    
    :example: response = client.start_config_rules_evaluation(
        ConfigRuleNames=[
            'string',
        ]
    )
    
    
    :type ConfigRuleNames: list
    :param ConfigRuleNames: The list of names of AWS Config rules that you want to run evaluations for.
            (string) --
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (string) --
    
    """
    pass

def start_configuration_recorder(ConfigurationRecorderName=None):
    """
    Starts recording configurations of the AWS resources you have selected to record in your AWS account.
    You must have created at least one delivery channel to successfully start the configuration recorder.
    See also: AWS API Documentation
    
    
    :example: response = client.start_configuration_recorder(
        ConfigurationRecorderName='string'
    )
    
    
    :type ConfigurationRecorderName: string
    :param ConfigurationRecorderName: [REQUIRED]
            The name of the recorder object that records each configuration change made to the resources.
            

    """
    pass

def stop_configuration_recorder(ConfigurationRecorderName=None):
    """
    Stops recording configurations of the AWS resources you have selected to record in your AWS account.
    See also: AWS API Documentation
    
    
    :example: response = client.stop_configuration_recorder(
        ConfigurationRecorderName='string'
    )
    
    
    :type ConfigurationRecorderName: string
    :param ConfigurationRecorderName: [REQUIRED]
            The name of the recorder object that records each configuration change made to the resources.
            

    """
    pass

