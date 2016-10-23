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


def delete_config_rule(ConfigRuleName=None):
    """
    :param ConfigRuleName: [REQUIRED]
            The name of the AWS Config rule that you want to delete.
            ReturnsNone
            
    :type ConfigRuleName: string
    """
    pass


def delete_configuration_recorder(ConfigurationRecorderName=None):
    """
    :param ConfigurationRecorderName: [REQUIRED]
            The name of the configuration recorder to be deleted. You can retrieve the name of your configuration recorder by using the DescribeConfigurationRecorders action.
            ReturnsNone
            
    :type ConfigurationRecorderName: string
    """
    pass


def delete_delivery_channel(DeliveryChannelName=None):
    """
    :param DeliveryChannelName: [REQUIRED]
            The name of the delivery channel to delete.
            ReturnsNone
            
    :type DeliveryChannelName: string
    """
    pass


def delete_evaluation_results(ConfigRuleName=None):
    """
    :param ConfigRuleName: [REQUIRED]
            The name of the Config rule for which you want to delete the evaluation results.
            Return typedict
            ReturnsResponse Syntax{}
            Response Structure
            (dict) --The output when you delete the evaluation results for the specified Config rule.
            
            
    :type ConfigRuleName: string
    """
    pass


def deliver_config_snapshot(deliveryChannelName=None):
    """
    :param deliveryChannelName: [REQUIRED]
            The name of the delivery channel through which the snapshot is delivered.
            Return typedict
            ReturnsResponse Syntax{
              'configSnapshotId': 'string'
            }
            Response Structure
            (dict) --The output for the DeliverConfigSnapshot action in JSON format.
            configSnapshotId (string) --The ID of the snapshot that is being created.
            
            
    :type deliveryChannelName: string
    """
    pass


def describe_compliance_by_config_rule(ConfigRuleNames=None, ComplianceTypes=None, NextToken=None):
    """
    :param ConfigRuleNames: Specify one or more AWS Config rule names to filter the results by rule.
            (string) --
            
    :type ConfigRuleNames: list
    :param ComplianceTypes: Filters the results by compliance.
            The allowed values are COMPLIANT , NON_COMPLIANT , and INSUFFICIENT_DATA .
            (string) --
            
    :type ComplianceTypes: list
    :param NextToken: The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.
    :type NextToken: string
    """
    pass


def describe_compliance_by_resource(ResourceType=None, ResourceId=None, ComplianceTypes=None, Limit=None,
                                    NextToken=None):
    """
    :param ResourceType: The types of AWS resources for which you want compliance information; for example, AWS::EC2::Instance . For this action, you can specify that the resource type is an AWS account by specifying AWS::::Account .
    :type ResourceType: string
    :param ResourceId: The ID of the AWS resource for which you want compliance information. You can specify only one resource ID. If you specify a resource ID, you must also specify a type for ResourceType .
    :type ResourceId: string
    :param ComplianceTypes: Filters the results by compliance.
            The allowed values are COMPLIANT , NON_COMPLIANT , and INSUFFICIENT_DATA .
            (string) --
            
    :type ComplianceTypes: list
    :param Limit: The maximum number of evaluation results returned on each page. The default is 10. You cannot specify a limit greater than 100. If you specify 0, AWS Config uses the default.
    :type Limit: integer
    :param NextToken: The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.
    :type NextToken: string
    """
    pass


def describe_config_rule_evaluation_status(ConfigRuleNames=None):
    """
    :param ConfigRuleNames: The name of the AWS managed Config rules for which you want status information. If you do not specify any names, AWS Config returns status information for all AWS managed Config rules that you use.
            (string) --
            Return typedict
            ReturnsResponse Syntax{
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
              ]
            }
            Response Structure
            (dict) --
            ConfigRulesEvaluationStatus (list) --Status information about your AWS managed Config rules.
            (dict) --Status information for your AWS managed Config rules. The status includes information such as the last time the rule ran, the last time it failed, and the related error for the last failure.
            This action does not return status information about custom Config rules.
            ConfigRuleName (string) --The name of the AWS Config rule.
            ConfigRuleArn (string) --The Amazon Resource Name (ARN) of the AWS Config rule.
            ConfigRuleId (string) --The ID of the AWS Config rule.
            LastSuccessfulInvocationTime (datetime) --The time that AWS Config last successfully invoked the AWS Config rule to evaluate your AWS resources.
            LastFailedInvocationTime (datetime) --The time that AWS Config last failed to invoke the AWS Config rule to evaluate your AWS resources.
            LastSuccessfulEvaluationTime (datetime) --The time that AWS Config last successfully evaluated your AWS resources against the rule.
            LastFailedEvaluationTime (datetime) --The time that AWS Config last failed to evaluate your AWS resources against the rule.
            FirstActivatedTime (datetime) --The time that you first activated the AWS Config rule.
            LastErrorCode (string) --The error code that AWS Config returned when the rule last failed.
            LastErrorMessage (string) --The error message that AWS Config returned when the rule last failed.
            FirstEvaluationStarted (boolean) --Indicates whether AWS Config has evaluated your resources against the rule at least once.
            true - AWS Config has evaluated your AWS resources against the rule at least once.
            false - AWS Config has not once finished evaluating your AWS resources against the rule.
            
            
            
    :type ConfigRuleNames: list
    """
    pass


def describe_config_rules(ConfigRuleNames=None, NextToken=None):
    """
    :param ConfigRuleNames: The names of the AWS Config rules for which you want details. If you do not specify any names, AWS Config returns details for all your rules.
            (string) --
            
    :type ConfigRuleNames: list
    :param NextToken: The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.
    :type NextToken: string
    """
    pass


def describe_configuration_recorder_status(ConfigurationRecorderNames=None):
    """
    :param ConfigurationRecorderNames: The name(s) of the configuration recorder. If the name is not specified, the action returns the current status of all the configuration recorders associated with the account.
            (string) --
            Return typedict
            ReturnsResponse Syntax{
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
            Response Structure
            (dict) --The output for the DescribeConfigurationRecorderStatus action in JSON format.
            ConfigurationRecordersStatus (list) --A list that contains status of the specified recorders.
            (dict) --The current status of the configuration recorder.
            name (string) --The name of the configuration recorder.
            lastStartTime (datetime) --The time the recorder was last started.
            lastStopTime (datetime) --The time the recorder was last stopped.
            recording (boolean) --Specifies whether the recorder is currently recording or not.
            lastStatus (string) --The last (previous) status of the recorder.
            lastErrorCode (string) --The error code indicating that the recording failed.
            lastErrorMessage (string) --The message indicating that the recording failed due to an error.
            lastStatusChangeTime (datetime) --The time when the status was last changed.
            
            
            
    :type ConfigurationRecorderNames: list
    """
    pass


def describe_configuration_recorders(ConfigurationRecorderNames=None):
    """
    :param ConfigurationRecorderNames: A list of configuration recorder names.
            (string) --
            Return typedict
            ReturnsResponse Syntax{
              'ConfigurationRecorders': [
                {
                  'name': 'string',
                  'roleARN': 'string',
                  'recordingGroup': {
                    'allSupported': True|False,
                    'includeGlobalResourceTypes': True|False,
                    'resourceTypes': [
                      'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::EventSubscription'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::S3::Bucket',
                    ]
                  }
                },
              ]
            }
            Response Structure
            (dict) --The output for the DescribeConfigurationRecorders action.
            ConfigurationRecorders (list) --A list that contains the descriptions of the specified configuration recorders.
            (dict) --An object that represents the recording of configuration changes of an AWS resource.
            name (string) --The name of the recorder. By default, AWS Config automatically assigns the name 'default' when creating the configuration recorder. You cannot change the assigned name.
            roleARN (string) --Amazon Resource Name (ARN) of the IAM role used to describe the AWS resources associated with the account.
            recordingGroup (dict) --Specifies the types of AWS resource for which AWS Config records configuration changes.
            allSupported (boolean) --Specifies whether AWS Config records configuration changes for every supported type of regional resource.
            If you set this option to true , when AWS Config adds support for a new type of regional resource, it automatically starts recording resources of that type.
            If you set this option to true , you cannot enumerate a list of resourceTypes .
            includeGlobalResourceTypes (boolean) --Specifies whether AWS Config includes all supported types of global resources (for example, IAM resources) with the resources that it records.
            Before you can set this option to true , you must set the allSupported option to true .
            If you set this option to true , when AWS Config adds support for a new type of global resource, it automatically starts recording resources of that type.
            The configuration details for any global resource are the same in all regions. To prevent duplicate configuration items, you should consider customizing AWS Config in only one region to record global resources.
            resourceTypes (list) --A comma-separated list that specifies the types of AWS resources for which AWS Config records configuration changes (for example, AWS::EC2::Instance or AWS::CloudTrail::Trail ).
            Before you can set this option to true , you must set the allSupported option to false .
            If you set this option to true , when AWS Config adds support for a new type of resource, it will not record resources of that type unless you manually add that type to your recording group.
            For a list of valid resourceTypes values, see the resourceType Value column in Supported AWS Resource Types .
            (string) --
            
            
            
            
    :type ConfigurationRecorderNames: list
    """
    pass


def describe_delivery_channel_status(DeliveryChannelNames=None):
    """
    :param DeliveryChannelNames: A list of delivery channel names.
            (string) --
            Return typedict
            ReturnsResponse Syntax{
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
            Response Structure
            (dict) --The output for the DescribeDeliveryChannelStatus action.
            DeliveryChannelsStatus (list) --A list that contains the status of a specified delivery channel.
            (dict) --The status of a specified delivery channel.
            Valid values: Success | Failure
            name (string) --The name of the delivery channel.
            configSnapshotDeliveryInfo (dict) --A list containing the status of the delivery of the snapshot to the specified Amazon S3 bucket.
            lastStatus (string) --Status of the last attempted delivery.
            lastErrorCode (string) --The error code from the last attempted delivery.
            lastErrorMessage (string) --The error message from the last attempted delivery.
            lastAttemptTime (datetime) --The time of the last attempted delivery.
            lastSuccessfulTime (datetime) --The time of the last successful delivery.
            nextDeliveryTime (datetime) --The time that the next delivery occurs.
            configHistoryDeliveryInfo (dict) --A list that contains the status of the delivery of the configuration history to the specified Amazon S3 bucket.
            lastStatus (string) --Status of the last attempted delivery.
            lastErrorCode (string) --The error code from the last attempted delivery.
            lastErrorMessage (string) --The error message from the last attempted delivery.
            lastAttemptTime (datetime) --The time of the last attempted delivery.
            lastSuccessfulTime (datetime) --The time of the last successful delivery.
            nextDeliveryTime (datetime) --The time that the next delivery occurs.
            configStreamDeliveryInfo (dict) --A list containing the status of the delivery of the configuration stream notification to the specified Amazon SNS topic.
            lastStatus (string) --Status of the last attempted delivery.
            Note Providing an SNS topic on a DeliveryChannel for AWS Config is optional. If the SNS delivery is turned off, the last status will be Not_Applicable .
            lastErrorCode (string) --The error code from the last attempted delivery.
            lastErrorMessage (string) --The error message from the last attempted delivery.
            lastStatusChangeTime (datetime) --The time from the last status change.
            
            
            
            
    :type DeliveryChannelNames: list
    """
    pass


def describe_delivery_channels(DeliveryChannelNames=None):
    """
    :param DeliveryChannelNames: A list of delivery channel names.
            (string) --
            Return typedict
            ReturnsResponse Syntax{
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
            Response Structure
            (dict) --The output for the DescribeDeliveryChannels action.
            DeliveryChannels (list) --A list that contains the descriptions of the specified delivery channel.
            (dict) --The channel through which AWS Config delivers notifications and updated configuration states.
            name (string) --The name of the delivery channel. By default, AWS Config assigns the name 'default' when creating the delivery channel. To change the delivery channel name, you must use the DeleteDeliveryChannel action to delete your current delivery channel, and then you must use the PutDeliveryChannel command to create a delivery channel that has the desired name.
            s3BucketName (string) --The name of the Amazon S3 bucket to which AWS Config delivers configuration snapshots and configuration history files.
            If you specify a bucket that belongs to another AWS account, that bucket must have policies that grant access permissions to AWS Config. For more information, see Permissions for the Amazon S3 Bucket in the AWS Config Developer Guide.
            s3KeyPrefix (string) --The prefix for the specified Amazon S3 bucket.
            snsTopicARN (string) --The Amazon Resource Name (ARN) of the Amazon SNS topic to which AWS Config sends notifications about configuration changes.
            If you choose a topic from another account, the topic must have policies that grant access permissions to AWS Config. For more information, see Permissions for the Amazon SNS Topic in the AWS Config Developer Guide.
            configSnapshotDeliveryProperties (dict) --Provides options for how often AWS Config delivers configuration snapshots to the Amazon S3 bucket in your delivery channel.
            Note
            If you want to create a rule that triggers evaluations for your resources when AWS Config delivers the configuration snapshot, see the following:
            The frequency for a rule that triggers evaluations for your resources when AWS Config delivers the configuration snapshot is set by one of two values, depending on which is less frequent:
            The value for the deliveryFrequency parameter within the delivery channel configuration, which sets how often AWS Config delivers configuration snapshots. This value also sets how often AWS Config invokes evaluations for Config rules.
            The value for the MaximumExecutionFrequency parameter, which sets the maximum frequency with which AWS Config invokes evaluations for the rule. For more information, see ConfigRule .
            If the deliveryFrequency value is less frequent than the MaximumExecutionFrequency value for a rule, AWS Config invokes the rule only as often as the deliveryFrequency value.
            For example, you want your rule to run evaluations when AWS Config delivers the configuration snapshot.
            You specify the MaximumExecutionFrequency value for Six_Hours .
            You then specify the delivery channel deliveryFrequency value for TwentyFour_Hours .
            Because the value for deliveryFrequency is less frequent than MaximumExecutionFrequency , AWS Config invokes evaluations for the rule every 24 hours.
            You should set the MaximumExecutionFrequency value to be at least as frequent as the deliveryFrequency value. You can view the deliveryFrequency value by using the DescribeDeliveryChannnels action.
            To update the deliveryFrequency with which AWS Config delivers your configuration snapshots, use the PutDeliveryChannel action.
            deliveryFrequency (string) --The frequency with which AWS Config delivers configuration snapshots.
            
            
            
            
    :type DeliveryChannelNames: list
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


def get_compliance_details_by_config_rule(ConfigRuleName=None, ComplianceTypes=None, Limit=None, NextToken=None):
    """
    :param ConfigRuleName: [REQUIRED]
            The name of the AWS Config rule for which you want compliance information.
            
    :type ConfigRuleName: string
    :param ComplianceTypes: Filters the results by compliance.
            The allowed values are COMPLIANT , NON_COMPLIANT , and NOT_APPLICABLE .
            (string) --
            
    :type ComplianceTypes: list
    :param Limit: The maximum number of evaluation results returned on each page. The default is 10. You cannot specify a limit greater than 100. If you specify 0, AWS Config uses the default.
    :type Limit: integer
    :param NextToken: The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.
    :type NextToken: string
    """
    pass


def get_compliance_details_by_resource(ResourceType=None, ResourceId=None, ComplianceTypes=None, NextToken=None):
    """
    :param ResourceType: [REQUIRED]
            The type of the AWS resource for which you want compliance information.
            
    :type ResourceType: string
    :param ResourceId: [REQUIRED]
            The ID of the AWS resource for which you want compliance information.
            
    :type ResourceId: string
    :param ComplianceTypes: Filters the results by compliance.
            The allowed values are COMPLIANT , NON_COMPLIANT , and NOT_APPLICABLE .
            (string) --
            
    :type ComplianceTypes: list
    :param NextToken: The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.
    :type NextToken: string
    """
    pass


def get_compliance_summary_by_config_rule():
    """
    """
    pass


def get_compliance_summary_by_resource_type(ResourceTypes=None):
    """
    :param ResourceTypes: Specify one or more resource types to get the number of resources that are compliant and the number that are noncompliant for each resource type.
            For this request, you can specify an AWS resource type such as AWS::EC2::Instance , and you can specify that the resource type is an AWS account by specifying AWS::::Account .
            (string) --
            Return typedict
            ReturnsResponse Syntax{
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
            Response Structure
            (dict) --
            ComplianceSummariesByResourceType (list) --The number of resources that are compliant and the number that are noncompliant. If one or more resource types were provided with the request, the numbers are returned for each resource type. The maximum number returned is 100.
            (dict) --The number of AWS resources of a specific type that are compliant or noncompliant, up to a maximum of 100 for each compliance.
            ResourceType (string) --The type of AWS resource.
            ComplianceSummary (dict) --The number of AWS resources that are compliant or noncompliant, up to a maximum of 100 for each compliance.
            CompliantResourceCount (dict) --The number of AWS Config rules or AWS resources that are compliant, up to a maximum of 25 for rules and 100 for resources.
            CappedCount (integer) --The number of AWS resources or AWS Config rules responsible for the current compliance of the item.
            CapExceeded (boolean) --Indicates whether the maximum count is reached.
            NonCompliantResourceCount (dict) --The number of AWS Config rules or AWS resources that are noncompliant, up to a maximum of 25 for rules and 100 for resources.
            CappedCount (integer) --The number of AWS resources or AWS Config rules responsible for the current compliance of the item.
            CapExceeded (boolean) --Indicates whether the maximum count is reached.
            ComplianceSummaryTimestamp (datetime) --The time that AWS Config created the compliance summary.
            
            
            
            
    :type ResourceTypes: list
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


def get_resource_config_history(resourceType=None, resourceId=None, laterTime=None, earlierTime=None,
                                chronologicalOrder=None, limit=None, nextToken=None):
    """
    :param resourceType: [REQUIRED]
            The resource type.
            
    :type resourceType: string
    :param resourceId: [REQUIRED]
            The ID of the resource (for example., sg-xxxxxx ).
            
    :type resourceId: string
    :param laterTime: The time stamp that indicates a later time. If not specified, current time is taken.
    :type laterTime: datetime
    :param earlierTime: The time stamp that indicates an earlier time. If not specified, the action returns paginated results that contain configuration items that start from when the first configuration item was recorded.
    :type earlierTime: datetime
    :param chronologicalOrder: The chronological order for configuration items listed. By default the results are listed in reverse chronological order.
    :type chronologicalOrder: string
    :param limit: The maximum number of configuration items returned on each page. The default is 10. You cannot specify a limit greater than 100. If you specify 0, AWS Config uses the default.
    :type limit: integer
    :param nextToken: The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.
    :type nextToken: string
    """
    pass


def get_waiter():
    """
    """
    pass


def list_discovered_resources(resourceType=None, resourceIds=None, resourceName=None, limit=None,
                              includeDeletedResources=None, nextToken=None):
    """
    :param resourceType: [REQUIRED]
            The type of resources that you want AWS Config to list in the response.
            
    :type resourceType: string
    :param resourceIds: The IDs of only those resources that you want AWS Config to list in the response. If you do not specify this parameter, AWS Config lists all resources of the specified type that it has discovered.
            (string) --
            
    :type resourceIds: list
    :param resourceName: The custom name of only those resources that you want AWS Config to list in the response. If you do not specify this parameter, AWS Config lists all resources of the specified type that it has discovered.
    :type resourceName: string
    :param limit: The maximum number of resource identifiers returned on each page. The default is 100. You cannot specify a limit greater than 100. If you specify 0, AWS Config uses the default.
    :type limit: integer
    :param includeDeletedResources: Specifies whether AWS Config includes deleted resources in the results. By default, deleted resources are not included.
    :type includeDeletedResources: boolean
    :param nextToken: The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.
    :type nextToken: string
    """
    pass


def put_config_rule(ConfigRule=None):
    """
    :param ConfigRule: [REQUIRED]
            An AWS Config rule represents an AWS Lambda function that you create for a custom rule or a predefined function for an AWS managed rule. The function evaluates configuration items to assess whether your AWS resources comply with your desired configurations. This function can run when AWS Config detects a configuration change to an AWS resource and at a periodic frequency that you choose (for example, every 24 hours).
            Note
            You can use the AWS CLI and AWS SDKs if you want to create a rule that triggers evaluations for your resources when AWS Config delivers the configuration snapshot. For more information, see ConfigSnapshotDeliveryProperties .
            For more information about developing and using AWS Config rules, see Evaluating AWS Resource Configurations with AWS Config in the AWS Config Developer Guide .
            ConfigRuleName (string) --The name that you assign to the AWS Config rule. The name is required if you are adding a new rule.
            ConfigRuleArn (string) --The Amazon Resource Name (ARN) of the AWS Config rule.
            ConfigRuleId (string) --The ID of the AWS Config rule.
            Description (string) --The description that you provide for the AWS Config rule.
            Scope (dict) --Defines which resources can trigger an evaluation for the rule. The scope can include one or more resource types, a combination of one resource type and one resource ID, or a combination of a tag key and value. Specify a scope to constrain the resources that can trigger an evaluation for the rule. If you do not specify a scope, evaluations are triggered when any resource in the recording group changes.
            ComplianceResourceTypes (list) --The resource types of only those AWS resources that you want to trigger an evaluation for the rule. You can only specify one type if you also specify a resource ID for ComplianceResourceId .
            (string) --
            TagKey (string) --The tag key that is applied to only those AWS resources that you want you want to trigger an evaluation for the rule.
            TagValue (string) --The tag value applied to only those AWS resources that you want to trigger an evaluation for the rule. If you specify a value for TagValue , you must also specify a value for TagKey .
            ComplianceResourceId (string) --The IDs of the only AWS resource that you want to trigger an evaluation for the rule. If you specify a resource ID, you must specify one resource type for ComplianceResourceTypes .
            Source (dict) -- [REQUIRED]Provides the rule owner (AWS or customer), the rule identifier, and the notifications that cause the function to evaluate your AWS resources.
            Owner (string) --Indicates whether AWS or the customer owns and manages the AWS Config rule.
            SourceIdentifier (string) --For AWS Config managed rules, a predefined identifier from a list. For example, IAM_PASSWORD_POLICY is a managed rule. To reference a managed rule, see Using AWS Managed Config Rules .
            For custom rules, the identifier is the Amazon Resource Name (ARN) of the rule's AWS Lambda function, such as arn:aws:lambda:us-east-1:123456789012:function:custom_rule_name .
            SourceDetails (list) --Provides the source and type of the event that causes AWS Config to evaluate your AWS resources.
            (dict) --Provides the source and the message types that trigger AWS Config to evaluate your AWS resources against a rule. It also provides the frequency with which you want AWS Config to run evaluations for the rule if the trigger type is periodic. You can specify the parameter values for SourceDetail only for custom rules.
            EventSource (string) --The source of the event, such as an AWS service, that triggers AWS Config to evaluate your AWS resources.
            MessageType (string) --The type of notification that triggers AWS Config to run an evaluation. You can specify the following notification types:
            ConfigurationItemChangeNotification - Triggers an evaluation when AWS Config delivers a configuration item change notification.ScheduledNotification - Triggers a periodic evaluation at the frequency specified for MaximumExecutionFrequency .
            ConfigurationSnapshotDeliveryCompleted - Triggers a periodic evaluation when AWS Config delivers a configuration snapshot.
            MaximumExecutionFrequency (string) --The frequency that you want AWS Config to run evaluations for a rule that is triggered periodically. If you specify a value for MaximumExecutionFrequency , then MessageType must use the ScheduledNotification value.
            
            InputParameters (string) --A string in JSON format that is passed to the AWS Config rule Lambda function.
            MaximumExecutionFrequency (string) --The maximum frequency with which AWS Config runs evaluations for a rule. You can specify a value for MaximumExecutionFrequency when:
            You are using an AWS managed rule that is triggered at a periodic frequency.
            Your custom rule is triggered when AWS Config delivers the configuration snapshot.
            For more information, see ConfigSnapshotDeliveryProperties .
            ConfigRuleState (string) --Indicates whether the AWS Config rule is active or is currently being deleted by AWS Config. It can also indicate the evaluation status for the Config rule.
            AWS Config sets the state of the rule to EVALUATING temporarily after you use the StartConfigRulesEvaluation request to evaluate your resources against the Config rule.
            AWS Config sets the state of the rule to DELETING_RESULTS temporarily after you use the DeleteEvaluationResults request to delete the current evaluation results for the Config rule.
            AWS Config sets the state of a rule to DELETING temporarily after you use the DeleteConfigRule request to delete the rule. After AWS Config deletes the rule, the rule and all of its evaluations are erased and are no longer available.
            ReturnsNone
            
    :type ConfigRule: dict
    """
    pass


def put_configuration_recorder(ConfigurationRecorder=None):
    """
    :param ConfigurationRecorder: [REQUIRED]
            The configuration recorder object that records each configuration change made to the resources.
            name (string) --The name of the recorder. By default, AWS Config automatically assigns the name 'default' when creating the configuration recorder. You cannot change the assigned name.
            roleARN (string) --Amazon Resource Name (ARN) of the IAM role used to describe the AWS resources associated with the account.
            recordingGroup (dict) --Specifies the types of AWS resource for which AWS Config records configuration changes.
            allSupported (boolean) --Specifies whether AWS Config records configuration changes for every supported type of regional resource.
            If you set this option to true , when AWS Config adds support for a new type of regional resource, it automatically starts recording resources of that type.
            If you set this option to true , you cannot enumerate a list of resourceTypes .
            includeGlobalResourceTypes (boolean) --Specifies whether AWS Config includes all supported types of global resources (for example, IAM resources) with the resources that it records.
            Before you can set this option to true , you must set the allSupported option to true .
            If you set this option to true , when AWS Config adds support for a new type of global resource, it automatically starts recording resources of that type.
            The configuration details for any global resource are the same in all regions. To prevent duplicate configuration items, you should consider customizing AWS Config in only one region to record global resources.
            resourceTypes (list) --A comma-separated list that specifies the types of AWS resources for which AWS Config records configuration changes (for example, AWS::EC2::Instance or AWS::CloudTrail::Trail ).
            Before you can set this option to true , you must set the allSupported option to false .
            If you set this option to true , when AWS Config adds support for a new type of resource, it will not record resources of that type unless you manually add that type to your recording group.
            For a list of valid resourceTypes values, see the resourceType Value column in Supported AWS Resource Types .
            (string) --
            
            ReturnsNone
            
    :type ConfigurationRecorder: dict
    """
    pass


def put_delivery_channel(DeliveryChannel=None):
    """
    :param DeliveryChannel: [REQUIRED]
            The configuration delivery channel object that delivers the configuration information to an Amazon S3 bucket, and to an Amazon SNS topic.
            name (string) --The name of the delivery channel. By default, AWS Config assigns the name 'default' when creating the delivery channel. To change the delivery channel name, you must use the DeleteDeliveryChannel action to delete your current delivery channel, and then you must use the PutDeliveryChannel command to create a delivery channel that has the desired name.
            s3BucketName (string) --The name of the Amazon S3 bucket to which AWS Config delivers configuration snapshots and configuration history files.
            If you specify a bucket that belongs to another AWS account, that bucket must have policies that grant access permissions to AWS Config. For more information, see Permissions for the Amazon S3 Bucket in the AWS Config Developer Guide.
            s3KeyPrefix (string) --The prefix for the specified Amazon S3 bucket.
            snsTopicARN (string) --The Amazon Resource Name (ARN) of the Amazon SNS topic to which AWS Config sends notifications about configuration changes.
            If you choose a topic from another account, the topic must have policies that grant access permissions to AWS Config. For more information, see Permissions for the Amazon SNS Topic in the AWS Config Developer Guide.
            configSnapshotDeliveryProperties (dict) --Provides options for how often AWS Config delivers configuration snapshots to the Amazon S3 bucket in your delivery channel.
            Note
            If you want to create a rule that triggers evaluations for your resources when AWS Config delivers the configuration snapshot, see the following:
            The frequency for a rule that triggers evaluations for your resources when AWS Config delivers the configuration snapshot is set by one of two values, depending on which is less frequent:
            The value for the deliveryFrequency parameter within the delivery channel configuration, which sets how often AWS Config delivers configuration snapshots. This value also sets how often AWS Config invokes evaluations for Config rules.
            The value for the MaximumExecutionFrequency parameter, which sets the maximum frequency with which AWS Config invokes evaluations for the rule. For more information, see ConfigRule .
            If the deliveryFrequency value is less frequent than the MaximumExecutionFrequency value for a rule, AWS Config invokes the rule only as often as the deliveryFrequency value.
            For example, you want your rule to run evaluations when AWS Config delivers the configuration snapshot.
            You specify the MaximumExecutionFrequency value for Six_Hours .
            You then specify the delivery channel deliveryFrequency value for TwentyFour_Hours .
            Because the value for deliveryFrequency is less frequent than MaximumExecutionFrequency , AWS Config invokes evaluations for the rule every 24 hours.
            You should set the MaximumExecutionFrequency value to be at least as frequent as the deliveryFrequency value. You can view the deliveryFrequency value by using the DescribeDeliveryChannnels action.
            To update the deliveryFrequency with which AWS Config delivers your configuration snapshots, use the PutDeliveryChannel action.
            deliveryFrequency (string) --The frequency with which AWS Config delivers configuration snapshots.
            
            ReturnsNone
            
    :type DeliveryChannel: dict
    """
    pass


def put_evaluations(Evaluations=None, ResultToken=None):
    """
    :param Evaluations: The assessments that the AWS Lambda function performs. Each evaluation identifies an AWS resource and indicates whether it complies with the AWS Config rule that invokes the AWS Lambda function.
            (dict) --Identifies an AWS resource and indicates whether it complies with the AWS Config rule that it was evaluated against.
            ComplianceResourceType (string) -- [REQUIRED]The type of AWS resource that was evaluated.
            ComplianceResourceId (string) -- [REQUIRED]The ID of the AWS resource that was evaluated.
            ComplianceType (string) -- [REQUIRED]Indicates whether the AWS resource complies with the AWS Config rule that it was evaluated against.
            For the Evaluation data type, AWS Config supports only the COMPLIANT , NON_COMPLIANT , and NOT_APPLICABLE values. AWS Config does not support the INSUFFICIENT_DATA value for this data type.
            Similarly, AWS Config does not accept INSUFFICIENT_DATA as the value for ComplianceType from a PutEvaluations request. For example, an AWS Lambda function for a custom Config rule cannot pass an INSUFFICIENT_DATA value to AWS Config.
            Annotation (string) --Supplementary information about how the evaluation determined the compliance.
            OrderingTimestamp (datetime) -- [REQUIRED]The time of the event in AWS Config that triggered the evaluation. For event-based evaluations, the time indicates when AWS Config created the configuration item that triggered the evaluation. For periodic evaluations, the time indicates when AWS Config delivered the configuration snapshot that triggered the evaluation.
            
            
    :type Evaluations: list
    :param ResultToken: [REQUIRED]
            An encrypted token that associates an evaluation with an AWS Config rule. Identifies the rule and the event that triggered the evaluation
            
    :type ResultToken: string
    """
    pass


def start_config_rules_evaluation(ConfigRuleNames=None):
    """
    :param ConfigRuleNames: The list of names of Config rules that you want to run evaluations for.
            (string) --
            Return typedict
            ReturnsResponse Syntax{}
            Response Structure
            (dict) --The output when you start the evaluation for the specified Config rule.
            
            
    :type ConfigRuleNames: list
    """
    pass


def start_configuration_recorder(ConfigurationRecorderName=None):
    """
    :param ConfigurationRecorderName: [REQUIRED]
            The name of the recorder object that records each configuration change made to the resources.
            ReturnsNone
            
    :type ConfigurationRecorderName: string
    """
    pass


def stop_configuration_recorder(ConfigurationRecorderName=None):
    """
    :param ConfigurationRecorderName: [REQUIRED]
            The name of the recorder object that records each configuration change made to the resources.
            ReturnsNone
            
    :type ConfigurationRecorderName: string
    """
    pass
