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

def batch_get_aggregate_resource_config(ConfigurationAggregatorName=None, ResourceIdentifiers=None):
    """
    Returns the current configuration items for resources that are present in your AWS Config aggregator. The operation also returns a list of resources that are not processed in the current request. If there are no unprocessed resources, the operation returns an empty unprocessedResourceIdentifiers list.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_get_aggregate_resource_config(
        ConfigurationAggregatorName='string',
        ResourceIdentifiers=[
            {
                'SourceAccountId': 'string',
                'SourceRegion': 'string',
                'ResourceId': 'string',
                'ResourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::EC2::RegisteredHAInstance'|'AWS::EC2::NatGateway'|'AWS::EC2::EgressOnlyInternetGateway'|'AWS::EC2::VPCEndpoint'|'AWS::EC2::VPCEndpointService'|'AWS::EC2::FlowLog'|'AWS::EC2::VPCPeeringConnection'|'AWS::Elasticsearch::Domain'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::DBCluster'|'AWS::RDS::DBClusterSnapshot'|'AWS::RDS::EventSubscription'|'AWS::S3::Bucket'|'AWS::S3::AccountPublicAccessBlock'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::SSM::ManagedInstanceInventory'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::DynamoDB::Table'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::RuleGroup'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::RuleGroup'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::WAFv2::WebACL'|'AWS::WAFv2::RuleGroup'|'AWS::WAFv2::IPSet'|'AWS::WAFv2::RegexPatternSet'|'AWS::WAFv2::ManagedRuleSet'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::ApiGateway::Stage'|'AWS::ApiGateway::RestApi'|'AWS::ApiGatewayV2::Stage'|'AWS::ApiGatewayV2::Api'|'AWS::CodePipeline::Pipeline'|'AWS::ServiceCatalog::CloudFormationProvisionedProduct'|'AWS::ServiceCatalog::CloudFormationProduct'|'AWS::ServiceCatalog::Portfolio'|'AWS::SQS::Queue'|'AWS::KMS::Key'|'AWS::QLDB::Ledger',
                'ResourceName': 'string'
            },
        ]
    )
    
    
    :type ConfigurationAggregatorName: string
    :param ConfigurationAggregatorName: [REQUIRED]\nThe name of the configuration aggregator.\n

    :type ResourceIdentifiers: list
    :param ResourceIdentifiers: [REQUIRED]\nA list of aggregate ResourceIdentifiers objects.\n\n(dict) --The details that identify a resource that is collected by AWS Config aggregator, including the resource type, ID, (if available) the custom resource name, the source account, and source region.\n\nSourceAccountId (string) -- [REQUIRED]The 12-digit account ID of the source account.\n\nSourceRegion (string) -- [REQUIRED]The source region where data is aggregated.\n\nResourceId (string) -- [REQUIRED]The ID of the AWS resource.\n\nResourceType (string) -- [REQUIRED]The type of the AWS resource.\n\nResourceName (string) --The name of the AWS resource.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'BaseConfigurationItems': [
        {
            'version': 'string',
            'accountId': 'string',
            'configurationItemCaptureTime': datetime(2015, 1, 1),
            'configurationItemStatus': 'OK'|'ResourceDiscovered'|'ResourceNotRecorded'|'ResourceDeleted'|'ResourceDeletedNotRecorded',
            'configurationStateId': 'string',
            'arn': 'string',
            'resourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::EC2::RegisteredHAInstance'|'AWS::EC2::NatGateway'|'AWS::EC2::EgressOnlyInternetGateway'|'AWS::EC2::VPCEndpoint'|'AWS::EC2::VPCEndpointService'|'AWS::EC2::FlowLog'|'AWS::EC2::VPCPeeringConnection'|'AWS::Elasticsearch::Domain'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::DBCluster'|'AWS::RDS::DBClusterSnapshot'|'AWS::RDS::EventSubscription'|'AWS::S3::Bucket'|'AWS::S3::AccountPublicAccessBlock'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::SSM::ManagedInstanceInventory'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::DynamoDB::Table'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::RuleGroup'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::RuleGroup'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::WAFv2::WebACL'|'AWS::WAFv2::RuleGroup'|'AWS::WAFv2::IPSet'|'AWS::WAFv2::RegexPatternSet'|'AWS::WAFv2::ManagedRuleSet'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::ApiGateway::Stage'|'AWS::ApiGateway::RestApi'|'AWS::ApiGatewayV2::Stage'|'AWS::ApiGatewayV2::Api'|'AWS::CodePipeline::Pipeline'|'AWS::ServiceCatalog::CloudFormationProvisionedProduct'|'AWS::ServiceCatalog::CloudFormationProduct'|'AWS::ServiceCatalog::Portfolio'|'AWS::SQS::Queue'|'AWS::KMS::Key'|'AWS::QLDB::Ledger',
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
    'UnprocessedResourceIdentifiers': [
        {
            'SourceAccountId': 'string',
            'SourceRegion': 'string',
            'ResourceId': 'string',
            'ResourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::EC2::RegisteredHAInstance'|'AWS::EC2::NatGateway'|'AWS::EC2::EgressOnlyInternetGateway'|'AWS::EC2::VPCEndpoint'|'AWS::EC2::VPCEndpointService'|'AWS::EC2::FlowLog'|'AWS::EC2::VPCPeeringConnection'|'AWS::Elasticsearch::Domain'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::DBCluster'|'AWS::RDS::DBClusterSnapshot'|'AWS::RDS::EventSubscription'|'AWS::S3::Bucket'|'AWS::S3::AccountPublicAccessBlock'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::SSM::ManagedInstanceInventory'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::DynamoDB::Table'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::RuleGroup'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::RuleGroup'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::WAFv2::WebACL'|'AWS::WAFv2::RuleGroup'|'AWS::WAFv2::IPSet'|'AWS::WAFv2::RegexPatternSet'|'AWS::WAFv2::ManagedRuleSet'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::ApiGateway::Stage'|'AWS::ApiGateway::RestApi'|'AWS::ApiGatewayV2::Stage'|'AWS::ApiGatewayV2::Api'|'AWS::CodePipeline::Pipeline'|'AWS::ServiceCatalog::CloudFormationProvisionedProduct'|'AWS::ServiceCatalog::CloudFormationProduct'|'AWS::ServiceCatalog::Portfolio'|'AWS::SQS::Queue'|'AWS::KMS::Key'|'AWS::QLDB::Ledger',
            'ResourceName': 'string'
        },
    ]
}


Response Structure

(dict) --

BaseConfigurationItems (list) --
A list that contains the current configuration of one or more resources.

(dict) --
The detailed configuration of a specified resource.

version (string) --
The version number of the resource configuration.

accountId (string) --
The 12-digit AWS account ID associated with the resource.

configurationItemCaptureTime (datetime) --
The time when the configuration recording was initiated.

configurationItemStatus (string) --
The configuration item status.

configurationStateId (string) --
An identifier that indicates the ordering of the configuration items of a resource.

arn (string) --
The Amazon Resource Name (ARN) of the resource.

resourceType (string) --
The type of AWS resource.

resourceId (string) --
The ID of the resource (for example., sg-xxxxxx).

resourceName (string) --
The custom name of the resource, if available.

awsRegion (string) --
The region where the resource resides.

availabilityZone (string) --
The Availability Zone associated with the resource.

resourceCreationTime (datetime) --
The time stamp when the resource was created.

configuration (string) --
The description of the resource configuration.

supplementaryConfiguration (dict) --
Configuration attributes that AWS Config returns for certain resource types to supplement the information returned for the configuration parameter.

(string) --
(string) --








UnprocessedResourceIdentifiers (list) --
A list of resource identifiers that were not processed with current scope. The list is empty if all the resources are processed.

(dict) --
The details that identify a resource that is collected by AWS Config aggregator, including the resource type, ID, (if available) the custom resource name, the source account, and source region.

SourceAccountId (string) --
The 12-digit account ID of the source account.

SourceRegion (string) --
The source region where data is aggregated.

ResourceId (string) --
The ID of the AWS resource.

ResourceType (string) --
The type of the AWS resource.

ResourceName (string) --
The name of the AWS resource.











Exceptions

ConfigService.Client.exceptions.ValidationException
ConfigService.Client.exceptions.NoSuchConfigurationAggregatorException


    :return: {
        'BaseConfigurationItems': [
            {
                'version': 'string',
                'accountId': 'string',
                'configurationItemCaptureTime': datetime(2015, 1, 1),
                'configurationItemStatus': 'OK'|'ResourceDiscovered'|'ResourceNotRecorded'|'ResourceDeleted'|'ResourceDeletedNotRecorded',
                'configurationStateId': 'string',
                'arn': 'string',
                'resourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::EC2::RegisteredHAInstance'|'AWS::EC2::NatGateway'|'AWS::EC2::EgressOnlyInternetGateway'|'AWS::EC2::VPCEndpoint'|'AWS::EC2::VPCEndpointService'|'AWS::EC2::FlowLog'|'AWS::EC2::VPCPeeringConnection'|'AWS::Elasticsearch::Domain'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::DBCluster'|'AWS::RDS::DBClusterSnapshot'|'AWS::RDS::EventSubscription'|'AWS::S3::Bucket'|'AWS::S3::AccountPublicAccessBlock'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::SSM::ManagedInstanceInventory'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::DynamoDB::Table'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::RuleGroup'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::RuleGroup'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::WAFv2::WebACL'|'AWS::WAFv2::RuleGroup'|'AWS::WAFv2::IPSet'|'AWS::WAFv2::RegexPatternSet'|'AWS::WAFv2::ManagedRuleSet'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::ApiGateway::Stage'|'AWS::ApiGateway::RestApi'|'AWS::ApiGatewayV2::Stage'|'AWS::ApiGatewayV2::Api'|'AWS::CodePipeline::Pipeline'|'AWS::ServiceCatalog::CloudFormationProvisionedProduct'|'AWS::ServiceCatalog::CloudFormationProduct'|'AWS::ServiceCatalog::Portfolio'|'AWS::SQS::Queue'|'AWS::KMS::Key'|'AWS::QLDB::Ledger',
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
        'UnprocessedResourceIdentifiers': [
            {
                'SourceAccountId': 'string',
                'SourceRegion': 'string',
                'ResourceId': 'string',
                'ResourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::EC2::RegisteredHAInstance'|'AWS::EC2::NatGateway'|'AWS::EC2::EgressOnlyInternetGateway'|'AWS::EC2::VPCEndpoint'|'AWS::EC2::VPCEndpointService'|'AWS::EC2::FlowLog'|'AWS::EC2::VPCPeeringConnection'|'AWS::Elasticsearch::Domain'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::DBCluster'|'AWS::RDS::DBClusterSnapshot'|'AWS::RDS::EventSubscription'|'AWS::S3::Bucket'|'AWS::S3::AccountPublicAccessBlock'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::SSM::ManagedInstanceInventory'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::DynamoDB::Table'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::RuleGroup'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::RuleGroup'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::WAFv2::WebACL'|'AWS::WAFv2::RuleGroup'|'AWS::WAFv2::IPSet'|'AWS::WAFv2::RegexPatternSet'|'AWS::WAFv2::ManagedRuleSet'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::ApiGateway::Stage'|'AWS::ApiGateway::RestApi'|'AWS::ApiGatewayV2::Stage'|'AWS::ApiGatewayV2::Api'|'AWS::CodePipeline::Pipeline'|'AWS::ServiceCatalog::CloudFormationProvisionedProduct'|'AWS::ServiceCatalog::CloudFormationProduct'|'AWS::ServiceCatalog::Portfolio'|'AWS::SQS::Queue'|'AWS::KMS::Key'|'AWS::QLDB::Ledger',
                'ResourceName': 'string'
            },
        ]
    }
    
    
    :returns: 
    ConfigurationAggregatorName (string) -- [REQUIRED]
    The name of the configuration aggregator.
    
    ResourceIdentifiers (list) -- [REQUIRED]
    A list of aggregate ResourceIdentifiers objects.
    
    (dict) --The details that identify a resource that is collected by AWS Config aggregator, including the resource type, ID, (if available) the custom resource name, the source account, and source region.
    
    SourceAccountId (string) -- [REQUIRED]The 12-digit account ID of the source account.
    
    SourceRegion (string) -- [REQUIRED]The source region where data is aggregated.
    
    ResourceId (string) -- [REQUIRED]The ID of the AWS resource.
    
    ResourceType (string) -- [REQUIRED]The type of the AWS resource.
    
    ResourceName (string) --The name of the AWS resource.
    
    
    
    
    
    
    """
    pass

def batch_get_resource_config(resourceKeys=None):
    """
    Returns the current configuration for one or more requested resources. The operation also returns a list of resources that are not processed in the current request. If there are no unprocessed resources, the operation returns an empty unprocessedResourceKeys list.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_get_resource_config(
        resourceKeys=[
            {
                'resourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::EC2::RegisteredHAInstance'|'AWS::EC2::NatGateway'|'AWS::EC2::EgressOnlyInternetGateway'|'AWS::EC2::VPCEndpoint'|'AWS::EC2::VPCEndpointService'|'AWS::EC2::FlowLog'|'AWS::EC2::VPCPeeringConnection'|'AWS::Elasticsearch::Domain'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::DBCluster'|'AWS::RDS::DBClusterSnapshot'|'AWS::RDS::EventSubscription'|'AWS::S3::Bucket'|'AWS::S3::AccountPublicAccessBlock'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::SSM::ManagedInstanceInventory'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::DynamoDB::Table'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::RuleGroup'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::RuleGroup'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::WAFv2::WebACL'|'AWS::WAFv2::RuleGroup'|'AWS::WAFv2::IPSet'|'AWS::WAFv2::RegexPatternSet'|'AWS::WAFv2::ManagedRuleSet'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::ApiGateway::Stage'|'AWS::ApiGateway::RestApi'|'AWS::ApiGatewayV2::Stage'|'AWS::ApiGatewayV2::Api'|'AWS::CodePipeline::Pipeline'|'AWS::ServiceCatalog::CloudFormationProvisionedProduct'|'AWS::ServiceCatalog::CloudFormationProduct'|'AWS::ServiceCatalog::Portfolio'|'AWS::SQS::Queue'|'AWS::KMS::Key'|'AWS::QLDB::Ledger',
                'resourceId': 'string'
            },
        ]
    )
    
    
    :type resourceKeys: list
    :param resourceKeys: [REQUIRED]\nA list of resource keys to be processed with the current request. Each element in the list consists of the resource type and resource ID.\n\n(dict) --The details that identify a resource within AWS Config, including the resource type and resource ID.\n\nresourceType (string) -- [REQUIRED]The resource type.\n\nresourceId (string) -- [REQUIRED]The ID of the resource (for example., sg-xxxxxx).\n\n\n\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'baseConfigurationItems': [
        {
            'version': 'string',
            'accountId': 'string',
            'configurationItemCaptureTime': datetime(2015, 1, 1),
            'configurationItemStatus': 'OK'|'ResourceDiscovered'|'ResourceNotRecorded'|'ResourceDeleted'|'ResourceDeletedNotRecorded',
            'configurationStateId': 'string',
            'arn': 'string',
            'resourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::EC2::RegisteredHAInstance'|'AWS::EC2::NatGateway'|'AWS::EC2::EgressOnlyInternetGateway'|'AWS::EC2::VPCEndpoint'|'AWS::EC2::VPCEndpointService'|'AWS::EC2::FlowLog'|'AWS::EC2::VPCPeeringConnection'|'AWS::Elasticsearch::Domain'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::DBCluster'|'AWS::RDS::DBClusterSnapshot'|'AWS::RDS::EventSubscription'|'AWS::S3::Bucket'|'AWS::S3::AccountPublicAccessBlock'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::SSM::ManagedInstanceInventory'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::DynamoDB::Table'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::RuleGroup'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::RuleGroup'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::WAFv2::WebACL'|'AWS::WAFv2::RuleGroup'|'AWS::WAFv2::IPSet'|'AWS::WAFv2::RegexPatternSet'|'AWS::WAFv2::ManagedRuleSet'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::ApiGateway::Stage'|'AWS::ApiGateway::RestApi'|'AWS::ApiGatewayV2::Stage'|'AWS::ApiGatewayV2::Api'|'AWS::CodePipeline::Pipeline'|'AWS::ServiceCatalog::CloudFormationProvisionedProduct'|'AWS::ServiceCatalog::CloudFormationProduct'|'AWS::ServiceCatalog::Portfolio'|'AWS::SQS::Queue'|'AWS::KMS::Key'|'AWS::QLDB::Ledger',
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
            'resourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::EC2::RegisteredHAInstance'|'AWS::EC2::NatGateway'|'AWS::EC2::EgressOnlyInternetGateway'|'AWS::EC2::VPCEndpoint'|'AWS::EC2::VPCEndpointService'|'AWS::EC2::FlowLog'|'AWS::EC2::VPCPeeringConnection'|'AWS::Elasticsearch::Domain'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::DBCluster'|'AWS::RDS::DBClusterSnapshot'|'AWS::RDS::EventSubscription'|'AWS::S3::Bucket'|'AWS::S3::AccountPublicAccessBlock'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::SSM::ManagedInstanceInventory'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::DynamoDB::Table'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::RuleGroup'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::RuleGroup'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::WAFv2::WebACL'|'AWS::WAFv2::RuleGroup'|'AWS::WAFv2::IPSet'|'AWS::WAFv2::RegexPatternSet'|'AWS::WAFv2::ManagedRuleSet'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::ApiGateway::Stage'|'AWS::ApiGateway::RestApi'|'AWS::ApiGatewayV2::Stage'|'AWS::ApiGatewayV2::Api'|'AWS::CodePipeline::Pipeline'|'AWS::ServiceCatalog::CloudFormationProvisionedProduct'|'AWS::ServiceCatalog::CloudFormationProduct'|'AWS::ServiceCatalog::Portfolio'|'AWS::SQS::Queue'|'AWS::KMS::Key'|'AWS::QLDB::Ledger',
            'resourceId': 'string'
        },
    ]
}


Response Structure

(dict) --
baseConfigurationItems (list) --A list that contains the current configuration of one or more resources.

(dict) --The detailed configuration of a specified resource.

version (string) --The version number of the resource configuration.

accountId (string) --The 12-digit AWS account ID associated with the resource.

configurationItemCaptureTime (datetime) --The time when the configuration recording was initiated.

configurationItemStatus (string) --The configuration item status.

configurationStateId (string) --An identifier that indicates the ordering of the configuration items of a resource.

arn (string) --The Amazon Resource Name (ARN) of the resource.

resourceType (string) --The type of AWS resource.

resourceId (string) --The ID of the resource (for example., sg-xxxxxx).

resourceName (string) --The custom name of the resource, if available.

awsRegion (string) --The region where the resource resides.

availabilityZone (string) --The Availability Zone associated with the resource.

resourceCreationTime (datetime) --The time stamp when the resource was created.

configuration (string) --The description of the resource configuration.

supplementaryConfiguration (dict) --Configuration attributes that AWS Config returns for certain resource types to supplement the information returned for the configuration parameter.

(string) --
(string) --








unprocessedResourceKeys (list) --A list of resource keys that were not processed with the current response. The unprocessesResourceKeys value is in the same form as ResourceKeys, so the value can be directly provided to a subsequent BatchGetResourceConfig operation. If there are no unprocessed resource keys, the response contains an empty unprocessedResourceKeys list.

(dict) --The details that identify a resource within AWS Config, including the resource type and resource ID.

resourceType (string) --The resource type.

resourceId (string) --The ID of the resource (for example., sg-xxxxxx).










Exceptions

ConfigService.Client.exceptions.ValidationException
ConfigService.Client.exceptions.NoAvailableConfigurationRecorderException


    :return: {
        'baseConfigurationItems': [
            {
                'version': 'string',
                'accountId': 'string',
                'configurationItemCaptureTime': datetime(2015, 1, 1),
                'configurationItemStatus': 'OK'|'ResourceDiscovered'|'ResourceNotRecorded'|'ResourceDeleted'|'ResourceDeletedNotRecorded',
                'configurationStateId': 'string',
                'arn': 'string',
                'resourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::EC2::RegisteredHAInstance'|'AWS::EC2::NatGateway'|'AWS::EC2::EgressOnlyInternetGateway'|'AWS::EC2::VPCEndpoint'|'AWS::EC2::VPCEndpointService'|'AWS::EC2::FlowLog'|'AWS::EC2::VPCPeeringConnection'|'AWS::Elasticsearch::Domain'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::DBCluster'|'AWS::RDS::DBClusterSnapshot'|'AWS::RDS::EventSubscription'|'AWS::S3::Bucket'|'AWS::S3::AccountPublicAccessBlock'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::SSM::ManagedInstanceInventory'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::DynamoDB::Table'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::RuleGroup'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::RuleGroup'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::WAFv2::WebACL'|'AWS::WAFv2::RuleGroup'|'AWS::WAFv2::IPSet'|'AWS::WAFv2::RegexPatternSet'|'AWS::WAFv2::ManagedRuleSet'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::ApiGateway::Stage'|'AWS::ApiGateway::RestApi'|'AWS::ApiGatewayV2::Stage'|'AWS::ApiGatewayV2::Api'|'AWS::CodePipeline::Pipeline'|'AWS::ServiceCatalog::CloudFormationProvisionedProduct'|'AWS::ServiceCatalog::CloudFormationProduct'|'AWS::ServiceCatalog::Portfolio'|'AWS::SQS::Queue'|'AWS::KMS::Key'|'AWS::QLDB::Ledger',
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
                'resourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::EC2::RegisteredHAInstance'|'AWS::EC2::NatGateway'|'AWS::EC2::EgressOnlyInternetGateway'|'AWS::EC2::VPCEndpoint'|'AWS::EC2::VPCEndpointService'|'AWS::EC2::FlowLog'|'AWS::EC2::VPCPeeringConnection'|'AWS::Elasticsearch::Domain'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::DBCluster'|'AWS::RDS::DBClusterSnapshot'|'AWS::RDS::EventSubscription'|'AWS::S3::Bucket'|'AWS::S3::AccountPublicAccessBlock'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::SSM::ManagedInstanceInventory'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::DynamoDB::Table'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::RuleGroup'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::RuleGroup'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::WAFv2::WebACL'|'AWS::WAFv2::RuleGroup'|'AWS::WAFv2::IPSet'|'AWS::WAFv2::RegexPatternSet'|'AWS::WAFv2::ManagedRuleSet'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::ApiGateway::Stage'|'AWS::ApiGateway::RestApi'|'AWS::ApiGatewayV2::Stage'|'AWS::ApiGatewayV2::Api'|'AWS::CodePipeline::Pipeline'|'AWS::ServiceCatalog::CloudFormationProvisionedProduct'|'AWS::ServiceCatalog::CloudFormationProduct'|'AWS::ServiceCatalog::Portfolio'|'AWS::SQS::Queue'|'AWS::KMS::Key'|'AWS::QLDB::Ledger',
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
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def delete_aggregation_authorization(AuthorizedAccountId=None, AuthorizedAwsRegion=None):
    """
    Deletes the authorization granted to the specified configuration aggregator account in a specified region.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_aggregation_authorization(
        AuthorizedAccountId='string',
        AuthorizedAwsRegion='string'
    )
    
    
    :type AuthorizedAccountId: string
    :param AuthorizedAccountId: [REQUIRED]\nThe 12-digit account ID of the account authorized to aggregate data.\n

    :type AuthorizedAwsRegion: string
    :param AuthorizedAwsRegion: [REQUIRED]\nThe region authorized to collect aggregated data.\n

    :returns: 
    ConfigService.Client.exceptions.InvalidParameterValueException
    
    """
    pass

def delete_config_rule(ConfigRuleName=None):
    """
    Deletes the specified AWS Config rule and all of its evaluation results.
    AWS Config sets the state of a rule to DELETING until the deletion is complete. You cannot update a rule while it is in this state. If you make a PutConfigRule or DeleteConfigRule request for the rule, you will receive a ResourceInUseException .
    You can check the state of a rule by using the DescribeConfigRules request.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_config_rule(
        ConfigRuleName='string'
    )
    
    
    :type ConfigRuleName: string
    :param ConfigRuleName: [REQUIRED]\nThe name of the AWS Config rule that you want to delete.\n

    """
    pass

def delete_configuration_aggregator(ConfigurationAggregatorName=None):
    """
    Deletes the specified configuration aggregator and the aggregated data associated with the aggregator.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_configuration_aggregator(
        ConfigurationAggregatorName='string'
    )
    
    
    :type ConfigurationAggregatorName: string
    :param ConfigurationAggregatorName: [REQUIRED]\nThe name of the configuration aggregator.\n

    """
    pass

def delete_configuration_recorder(ConfigurationRecorderName=None):
    """
    Deletes the configuration recorder.
    After the configuration recorder is deleted, AWS Config will not record resource configuration changes until you create a new configuration recorder.
    This action does not delete the configuration information that was previously recorded. You will be able to access the previously recorded information by using the GetResourceConfigHistory action, but you will not be able to access this information in the AWS Config console until you create a new configuration recorder.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_configuration_recorder(
        ConfigurationRecorderName='string'
    )
    
    
    :type ConfigurationRecorderName: string
    :param ConfigurationRecorderName: [REQUIRED]\nThe name of the configuration recorder to be deleted. You can retrieve the name of your configuration recorder by using the DescribeConfigurationRecorders action.\n

    """
    pass

def delete_conformance_pack(ConformancePackName=None):
    """
    Deletes the specified conformance pack and all the AWS Config rules, remediation actions, and all evaluation results within that conformance pack.
    AWS Config sets the conformance pack to DELETE_IN_PROGRESS until the deletion is complete. You cannot update a conformance pack while it is in this state.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_conformance_pack(
        ConformancePackName='string'
    )
    
    
    :type ConformancePackName: string
    :param ConformancePackName: [REQUIRED]\nName of the conformance pack you want to delete.\n

    """
    pass

def delete_delivery_channel(DeliveryChannelName=None):
    """
    Deletes the delivery channel.
    Before you can delete the delivery channel, you must stop the configuration recorder by using the  StopConfigurationRecorder action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_delivery_channel(
        DeliveryChannelName='string'
    )
    
    
    :type DeliveryChannelName: string
    :param DeliveryChannelName: [REQUIRED]\nThe name of the delivery channel to delete.\n

    """
    pass

def delete_evaluation_results(ConfigRuleName=None):
    """
    Deletes the evaluation results for the specified AWS Config rule. You can specify one AWS Config rule per request. After you delete the evaluation results, you can call the  StartConfigRulesEvaluation API to start evaluating your AWS resources against the rule.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_evaluation_results(
        ConfigRuleName='string'
    )
    
    
    :type ConfigRuleName: string
    :param ConfigRuleName: [REQUIRED]\nThe name of the AWS Config rule for which you want to delete the evaluation results.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --The output when you delete the evaluation results for the specified AWS Config rule.




Exceptions

ConfigService.Client.exceptions.NoSuchConfigRuleException
ConfigService.Client.exceptions.ResourceInUseException


    :return: {}
    
    
    """
    pass

def delete_organization_config_rule(OrganizationConfigRuleName=None):
    """
    Deletes the specified organization config rule and all of its evaluation results from all member accounts in that organization. Only a master account can delete an organization config rule.
    AWS Config sets the state of a rule to DELETE_IN_PROGRESS until the deletion is complete. You cannot update a rule while it is in this state.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_organization_config_rule(
        OrganizationConfigRuleName='string'
    )
    
    
    :type OrganizationConfigRuleName: string
    :param OrganizationConfigRuleName: [REQUIRED]\nThe name of organization config rule that you want to delete.\n

    """
    pass

def delete_organization_conformance_pack(OrganizationConformancePackName=None):
    """
    Deletes the specified organization conformance pack and all of the config rules and remediation actions from all member accounts in that organization. Only a master account can delete an organization conformance pack.
    AWS Config sets the state of a conformance pack to DELETE_IN_PROGRESS until the deletion is complete. You cannot update a conformance pack while it is in this state.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_organization_conformance_pack(
        OrganizationConformancePackName='string'
    )
    
    
    :type OrganizationConformancePackName: string
    :param OrganizationConformancePackName: [REQUIRED]\nThe name of organization conformance pack that you want to delete.\n

    """
    pass

def delete_pending_aggregation_request(RequesterAccountId=None, RequesterAwsRegion=None):
    """
    Deletes pending authorization requests for a specified aggregator account in a specified region.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_pending_aggregation_request(
        RequesterAccountId='string',
        RequesterAwsRegion='string'
    )
    
    
    :type RequesterAccountId: string
    :param RequesterAccountId: [REQUIRED]\nThe 12-digit account ID of the account requesting to aggregate data.\n

    :type RequesterAwsRegion: string
    :param RequesterAwsRegion: [REQUIRED]\nThe region requesting to aggregate data.\n

    :returns: 
    ConfigService.Client.exceptions.InvalidParameterValueException
    
    """
    pass

def delete_remediation_configuration(ConfigRuleName=None, ResourceType=None):
    """
    Deletes the remediation configuration.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_remediation_configuration(
        ConfigRuleName='string',
        ResourceType='string'
    )
    
    
    :type ConfigRuleName: string
    :param ConfigRuleName: [REQUIRED]\nThe name of the AWS Config rule for which you want to delete remediation configuration.\n

    :type ResourceType: string
    :param ResourceType: The type of a resource.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

ConfigService.Client.exceptions.NoSuchRemediationConfigurationException
ConfigService.Client.exceptions.RemediationInProgressException
ConfigService.Client.exceptions.InsufficientPermissionsException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_remediation_exceptions(ConfigRuleName=None, ResourceKeys=None):
    """
    Deletes one or more remediation exceptions mentioned in the resource keys.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_remediation_exceptions(
        ConfigRuleName='string',
        ResourceKeys=[
            {
                'ResourceType': 'string',
                'ResourceId': 'string'
            },
        ]
    )
    
    
    :type ConfigRuleName: string
    :param ConfigRuleName: [REQUIRED]\nThe name of the AWS Config rule for which you want to delete remediation exception configuration.\n

    :type ResourceKeys: list
    :param ResourceKeys: [REQUIRED]\nAn exception list of resource exception keys to be processed with the current request. AWS Config adds exception for each resource key. For example, AWS Config adds 3 exceptions for 3 resource keys.\n\n(dict) --The details that identify a resource within AWS Config, including the resource type and resource ID.\n\nResourceType (string) --The type of a resource.\n\nResourceId (string) --The ID of the resource (for example., sg-xxxxxx).\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'FailedBatches': [
        {
            'FailureMessage': 'string',
            'FailedItems': [
                {
                    'ResourceType': 'string',
                    'ResourceId': 'string'
                },
            ]
        },
    ]
}


Response Structure

(dict) --

FailedBatches (list) --
Returns a list of failed delete remediation exceptions batch objects. Each object in the batch consists of a list of failed items and failure messages.

(dict) --
List of each of the failed delete remediation exceptions with specific reasons.

FailureMessage (string) --
Returns a failure message for delete remediation exception. For example, AWS Config creates an exception due to an internal error.

FailedItems (list) --
Returns remediation exception resource key object of the failed items.

(dict) --
The details that identify a resource within AWS Config, including the resource type and resource ID.

ResourceType (string) --
The type of a resource.

ResourceId (string) --
The ID of the resource (for example., sg-xxxxxx).















Exceptions

ConfigService.Client.exceptions.NoSuchRemediationExceptionException


    :return: {
        'FailedBatches': [
            {
                'FailureMessage': 'string',
                'FailedItems': [
                    {
                        'ResourceType': 'string',
                        'ResourceId': 'string'
                    },
                ]
            },
        ]
    }
    
    
    :returns: 
    ConfigService.Client.exceptions.NoSuchRemediationExceptionException
    
    """
    pass

def delete_resource_config(ResourceType=None, ResourceId=None):
    """
    Records the configuration state for a custom resource that has been deleted. This API records a new ConfigurationItem with a ResourceDeleted status. You can retrieve the ConfigurationItems recorded for this resource in your AWS Config History.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_resource_config(
        ResourceType='string',
        ResourceId='string'
    )
    
    
    :type ResourceType: string
    :param ResourceType: [REQUIRED]\nThe type of the resource.\n

    :type ResourceId: string
    :param ResourceId: [REQUIRED]\nUnique identifier of the resource.\n

    :returns: 
    ConfigService.Client.exceptions.ValidationException
    ConfigService.Client.exceptions.NoRunningConfigurationRecorderException
    
    """
    pass

def delete_retention_configuration(RetentionConfigurationName=None):
    """
    Deletes the retention configuration.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_retention_configuration(
        RetentionConfigurationName='string'
    )
    
    
    :type RetentionConfigurationName: string
    :param RetentionConfigurationName: [REQUIRED]\nThe name of the retention configuration to delete.\n

    """
    pass

def deliver_config_snapshot(deliveryChannelName=None):
    """
    Schedules delivery of a configuration snapshot to the Amazon S3 bucket in the specified delivery channel. After the delivery has started, AWS Config sends the following notifications using an Amazon SNS topic that you have specified.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.deliver_config_snapshot(
        deliveryChannelName='string'
    )
    
    
    :type deliveryChannelName: string
    :param deliveryChannelName: [REQUIRED]\nThe name of the delivery channel through which the snapshot is delivered.\n

    :rtype: dict
ReturnsResponse Syntax{
    'configSnapshotId': 'string'
}


Response Structure

(dict) --The output for the  DeliverConfigSnapshot action, in JSON format.

configSnapshotId (string) --The ID of the snapshot that is being created.






Exceptions

ConfigService.Client.exceptions.NoSuchDeliveryChannelException
ConfigService.Client.exceptions.NoAvailableConfigurationRecorderException
ConfigService.Client.exceptions.NoRunningConfigurationRecorderException


    :return: {
        'configSnapshotId': 'string'
    }
    
    
    :returns: 
    ConfigService.Client.exceptions.NoSuchDeliveryChannelException
    ConfigService.Client.exceptions.NoAvailableConfigurationRecorderException
    ConfigService.Client.exceptions.NoRunningConfigurationRecorderException
    
    """
    pass

def describe_aggregate_compliance_by_config_rules(ConfigurationAggregatorName=None, Filters=None, Limit=None, NextToken=None):
    """
    Returns a list of compliant and noncompliant rules with the number of resources for compliant and noncompliant rules.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param ConfigurationAggregatorName: [REQUIRED]\nThe name of the configuration aggregator.\n

    :type Filters: dict
    :param Filters: Filters the results by ConfigRuleComplianceFilters object.\n\nConfigRuleName (string) --The name of the AWS Config rule.\n\nComplianceType (string) --The rule compliance status.\nFor the ConfigRuleComplianceFilters data type, AWS Config supports only COMPLIANT and NON_COMPLIANT . AWS Config does not support the NOT_APPLICABLE and the INSUFFICIENT_DATA values.\n\nAccountId (string) --The 12-digit account ID of the source account.\n\nAwsRegion (string) --The source region where the data is aggregated.\n\n\n

    :type Limit: integer
    :param Limit: The maximum number of evaluation results returned on each page. The default is maximum. If you specify 0, AWS Config uses the default.

    :type NextToken: string
    :param NextToken: The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

AggregateComplianceByConfigRules (list) --
Returns a list of AggregateComplianceByConfigRule object.

(dict) --
Indicates whether an AWS Config rule is compliant based on account ID, region, compliance, and rule name.
A rule is compliant if all of the resources that the rule evaluated comply with it. It is noncompliant if any of these resources do not comply.

ConfigRuleName (string) --
The name of the AWS Config rule.

Compliance (dict) --
Indicates whether an AWS resource or AWS Config rule is compliant and provides the number of contributors that affect the compliance.

ComplianceType (string) --
Indicates whether an AWS resource or AWS Config rule is compliant.
A resource is compliant if it complies with all of the AWS Config rules that evaluate it. A resource is noncompliant if it does not comply with one or more of these rules.
A rule is compliant if all of the resources that the rule evaluates comply with it. A rule is noncompliant if any of these resources do not comply.
AWS Config returns the INSUFFICIENT_DATA value when no evaluation results are available for the AWS resource or AWS Config rule.
For the Compliance data type, AWS Config supports only COMPLIANT , NON_COMPLIANT , and INSUFFICIENT_DATA values. AWS Config does not support the NOT_APPLICABLE value for the Compliance data type.

ComplianceContributorCount (dict) --
The number of AWS resources or AWS Config rules that cause a result of NON_COMPLIANT , up to a maximum number.

CappedCount (integer) --
The number of AWS resources or AWS Config rules responsible for the current compliance of the item.

CapExceeded (boolean) --
Indicates whether the maximum count is reached.





AccountId (string) --
The 12-digit account ID of the source account.

AwsRegion (string) --
The source region from where the data is aggregated.





NextToken (string) --
The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.







Exceptions

ConfigService.Client.exceptions.ValidationException
ConfigService.Client.exceptions.InvalidLimitException
ConfigService.Client.exceptions.InvalidNextTokenException
ConfigService.Client.exceptions.NoSuchConfigurationAggregatorException


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
    
    
    :returns: 
    ConfigService.Client.exceptions.ValidationException
    ConfigService.Client.exceptions.InvalidLimitException
    ConfigService.Client.exceptions.InvalidNextTokenException
    ConfigService.Client.exceptions.NoSuchConfigurationAggregatorException
    
    """
    pass

def describe_aggregation_authorizations(Limit=None, NextToken=None):
    """
    Returns a list of authorizations granted to various aggregator accounts and regions.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_aggregation_authorizations(
        Limit=123,
        NextToken='string'
    )
    
    
    :type Limit: integer
    :param Limit: The maximum number of AggregationAuthorizations returned on each page. The default is maximum. If you specify 0, AWS Config uses the default.

    :type NextToken: string
    :param NextToken: The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

AggregationAuthorizations (list) --
Returns a list of authorizations granted to various aggregator accounts and regions.

(dict) --
An object that represents the authorizations granted to aggregator accounts and regions.

AggregationAuthorizationArn (string) --
The Amazon Resource Name (ARN) of the aggregation object.

AuthorizedAccountId (string) --
The 12-digit account ID of the account authorized to aggregate data.

AuthorizedAwsRegion (string) --
The region authorized to collect aggregated data.

CreationTime (datetime) --
The time stamp when the aggregation authorization was created.





NextToken (string) --
The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.







Exceptions

ConfigService.Client.exceptions.InvalidParameterValueException
ConfigService.Client.exceptions.InvalidNextTokenException
ConfigService.Client.exceptions.InvalidLimitException


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
    
    
    :returns: 
    ConfigService.Client.exceptions.InvalidParameterValueException
    ConfigService.Client.exceptions.InvalidNextTokenException
    ConfigService.Client.exceptions.InvalidLimitException
    
    """
    pass

def describe_compliance_by_config_rule(ConfigRuleNames=None, ComplianceTypes=None, NextToken=None):
    """
    Indicates whether the specified AWS Config rules are compliant. If a rule is noncompliant, this action returns the number of AWS resources that do not comply with the rule.
    A rule is compliant if all of the evaluated resources comply with it. It is noncompliant if any of these resources do not comply.
    If AWS Config has no current evaluation results for the rule, it returns INSUFFICIENT_DATA . This result might indicate one of the following conditions:
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param ConfigRuleNames: Specify one or more AWS Config rule names to filter the results by rule.\n\n(string) --\n\n

    :type ComplianceTypes: list
    :param ComplianceTypes: Filters the results by compliance.\nThe allowed values are COMPLIANT and NON_COMPLIANT .\n\n(string) --\n\n

    :type NextToken: string
    :param NextToken: The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

ComplianceByConfigRules (list) --
Indicates whether each of the specified AWS Config rules is compliant.

(dict) --
Indicates whether an AWS Config rule is compliant. A rule is compliant if all of the resources that the rule evaluated comply with it. A rule is noncompliant if any of these resources do not comply.

ConfigRuleName (string) --
The name of the AWS Config rule.

Compliance (dict) --
Indicates whether the AWS Config rule is compliant.

ComplianceType (string) --
Indicates whether an AWS resource or AWS Config rule is compliant.
A resource is compliant if it complies with all of the AWS Config rules that evaluate it. A resource is noncompliant if it does not comply with one or more of these rules.
A rule is compliant if all of the resources that the rule evaluates comply with it. A rule is noncompliant if any of these resources do not comply.
AWS Config returns the INSUFFICIENT_DATA value when no evaluation results are available for the AWS resource or AWS Config rule.
For the Compliance data type, AWS Config supports only COMPLIANT , NON_COMPLIANT , and INSUFFICIENT_DATA values. AWS Config does not support the NOT_APPLICABLE value for the Compliance data type.

ComplianceContributorCount (dict) --
The number of AWS resources or AWS Config rules that cause a result of NON_COMPLIANT , up to a maximum number.

CappedCount (integer) --
The number of AWS resources or AWS Config rules responsible for the current compliance of the item.

CapExceeded (boolean) --
Indicates whether the maximum count is reached.









NextToken (string) --
The string that you use in a subsequent request to get the next page of results in a paginated response.







Exceptions

ConfigService.Client.exceptions.InvalidParameterValueException
ConfigService.Client.exceptions.NoSuchConfigRuleException
ConfigService.Client.exceptions.InvalidNextTokenException


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
    The allowed values are COMPLIANT and NON_COMPLIANT .
    
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
    
    Exceptions
    
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
    :param ComplianceTypes: Filters the results by compliance.\nThe allowed values are COMPLIANT , NON_COMPLIANT , and INSUFFICIENT_DATA .\n\n(string) --\n\n

    :type Limit: integer
    :param Limit: The maximum number of evaluation results returned on each page. The default is 10. You cannot specify a number greater than 100. If you specify 0, AWS Config uses the default.

    :type NextToken: string
    :param NextToken: The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

ComplianceByResources (list) --
Indicates whether the specified AWS resource complies with all of the AWS Config rules that evaluate it.

(dict) --
Indicates whether an AWS resource that is evaluated according to one or more AWS Config rules is compliant. A resource is compliant if it complies with all of the rules that evaluate it. A resource is noncompliant if it does not comply with one or more of these rules.

ResourceType (string) --
The type of the AWS resource that was evaluated.

ResourceId (string) --
The ID of the AWS resource that was evaluated.

Compliance (dict) --
Indicates whether the AWS resource complies with all of the AWS Config rules that evaluated it.

ComplianceType (string) --
Indicates whether an AWS resource or AWS Config rule is compliant.
A resource is compliant if it complies with all of the AWS Config rules that evaluate it. A resource is noncompliant if it does not comply with one or more of these rules.
A rule is compliant if all of the resources that the rule evaluates comply with it. A rule is noncompliant if any of these resources do not comply.
AWS Config returns the INSUFFICIENT_DATA value when no evaluation results are available for the AWS resource or AWS Config rule.
For the Compliance data type, AWS Config supports only COMPLIANT , NON_COMPLIANT , and INSUFFICIENT_DATA values. AWS Config does not support the NOT_APPLICABLE value for the Compliance data type.

ComplianceContributorCount (dict) --
The number of AWS resources or AWS Config rules that cause a result of NON_COMPLIANT , up to a maximum number.

CappedCount (integer) --
The number of AWS resources or AWS Config rules responsible for the current compliance of the item.

CapExceeded (boolean) --
Indicates whether the maximum count is reached.









NextToken (string) --
The string that you use in a subsequent request to get the next page of results in a paginated response.







Exceptions

ConfigService.Client.exceptions.InvalidParameterValueException
ConfigService.Client.exceptions.InvalidNextTokenException


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
    The allowed values are COMPLIANT , NON_COMPLIANT , and INSUFFICIENT_DATA .
    
    (string) --
    
    
    Limit (integer) -- The maximum number of evaluation results returned on each page. The default is 10. You cannot specify a number greater than 100. If you specify 0, AWS Config uses the default.
    NextToken (string) -- The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.
    
    """
    pass

def describe_config_rule_evaluation_status(ConfigRuleNames=None, NextToken=None, Limit=None):
    """
    Returns status information for each of your AWS managed Config rules. The status includes information such as the last time AWS Config invoked the rule, the last time AWS Config failed to invoke the rule, and the related error for the last failure.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_config_rule_evaluation_status(
        ConfigRuleNames=[
            'string',
        ],
        NextToken='string',
        Limit=123
    )
    
    
    :type ConfigRuleNames: list
    :param ConfigRuleNames: The name of the AWS managed Config rules for which you want status information. If you do not specify any names, AWS Config returns status information for all AWS managed Config rules that you use.\n\n(string) --\n\n

    :type NextToken: string
    :param NextToken: The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.

    :type Limit: integer
    :param Limit: The number of rule evaluation results that you want returned.\nThis parameter is required if the rule limit for your account is more than the default of 150 rules.\nFor information about requesting a rule limit increase, see AWS Config Limits in the AWS General Reference Guide .\n

    :rtype: dict

ReturnsResponse Syntax
{
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
            'LastDeactivatedTime': datetime(2015, 1, 1),
            'LastErrorCode': 'string',
            'LastErrorMessage': 'string',
            'FirstEvaluationStarted': True|False
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

ConfigRulesEvaluationStatus (list) --
Status information about your AWS managed Config rules.

(dict) --
Status information for your AWS managed Config rules. The status includes information such as the last time the rule ran, the last time it failed, and the related error for the last failure.
This action does not return status information about custom AWS Config rules.

ConfigRuleName (string) --
The name of the AWS Config rule.

ConfigRuleArn (string) --
The Amazon Resource Name (ARN) of the AWS Config rule.

ConfigRuleId (string) --
The ID of the AWS Config rule.

LastSuccessfulInvocationTime (datetime) --
The time that AWS Config last successfully invoked the AWS Config rule to evaluate your AWS resources.

LastFailedInvocationTime (datetime) --
The time that AWS Config last failed to invoke the AWS Config rule to evaluate your AWS resources.

LastSuccessfulEvaluationTime (datetime) --
The time that AWS Config last successfully evaluated your AWS resources against the rule.

LastFailedEvaluationTime (datetime) --
The time that AWS Config last failed to evaluate your AWS resources against the rule.

FirstActivatedTime (datetime) --
The time that you first activated the AWS Config rule.

LastDeactivatedTime (datetime) --

LastErrorCode (string) --
The error code that AWS Config returned when the rule last failed.

LastErrorMessage (string) --
The error message that AWS Config returned when the rule last failed.

FirstEvaluationStarted (boolean) --
Indicates whether AWS Config has evaluated your resources against the rule at least once.

true - AWS Config has evaluated your AWS resources against the rule at least once.
false - AWS Config has not once finished evaluating your AWS resources against the rule.






NextToken (string) --
The string that you use in a subsequent request to get the next page of results in a paginated response.







Exceptions

ConfigService.Client.exceptions.NoSuchConfigRuleException
ConfigService.Client.exceptions.InvalidParameterValueException
ConfigService.Client.exceptions.InvalidNextTokenException


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
                'LastDeactivatedTime': datetime(2015, 1, 1),
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
    
    Exceptions
    
    :example: response = client.describe_config_rules(
        ConfigRuleNames=[
            'string',
        ],
        NextToken='string'
    )
    
    
    :type ConfigRuleNames: list
    :param ConfigRuleNames: The names of the AWS Config rules for which you want details. If you do not specify any names, AWS Config returns details for all your rules.\n\n(string) --\n\n

    :type NextToken: string
    :param NextToken: The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.

    :rtype: dict

ReturnsResponse Syntax
{
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
            'ConfigRuleState': 'ACTIVE'|'DELETING'|'DELETING_RESULTS'|'EVALUATING',
            'CreatedBy': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

ConfigRules (list) --
The details about your AWS Config rules.

(dict) --
An AWS Config rule represents an AWS Lambda function that you create for a custom rule or a predefined function for an AWS managed rule. The function evaluates configuration items to assess whether your AWS resources comply with your desired configurations. This function can run when AWS Config detects a configuration change to an AWS resource and at a periodic frequency that you choose (for example, every 24 hours).

Note
You can use the AWS CLI and AWS SDKs if you want to create a rule that triggers evaluations for your resources when AWS Config delivers the configuration snapshot. For more information, see  ConfigSnapshotDeliveryProperties .

For more information about developing and using AWS Config rules, see Evaluating AWS Resource Configurations with AWS Config in the AWS Config Developer Guide .

ConfigRuleName (string) --
The name that you assign to the AWS Config rule. The name is required if you are adding a new rule.

ConfigRuleArn (string) --
The Amazon Resource Name (ARN) of the AWS Config rule.

ConfigRuleId (string) --
The ID of the AWS Config rule.

Description (string) --
The description that you provide for the AWS Config rule.

Scope (dict) --
Defines which resources can trigger an evaluation for the rule. The scope can include one or more resource types, a combination of one resource type and one resource ID, or a combination of a tag key and value. Specify a scope to constrain the resources that can trigger an evaluation for the rule. If you do not specify a scope, evaluations are triggered when any resource in the recording group changes.

ComplianceResourceTypes (list) --
The resource types of only those AWS resources that you want to trigger an evaluation for the rule. You can only specify one type if you also specify a resource ID for ComplianceResourceId .

(string) --


TagKey (string) --
The tag key that is applied to only those AWS resources that you want to trigger an evaluation for the rule.

TagValue (string) --
The tag value applied to only those AWS resources that you want to trigger an evaluation for the rule. If you specify a value for TagValue , you must also specify a value for TagKey .

ComplianceResourceId (string) --
The ID of the only AWS resource that you want to trigger an evaluation for the rule. If you specify a resource ID, you must specify one resource type for ComplianceResourceTypes .



Source (dict) --
Provides the rule owner (AWS or customer), the rule identifier, and the notifications that cause the function to evaluate your AWS resources.

Owner (string) --
Indicates whether AWS or the customer owns and manages the AWS Config rule.

SourceIdentifier (string) --
For AWS Config managed rules, a predefined identifier from a list. For example, IAM_PASSWORD_POLICY is a managed rule. To reference a managed rule, see Using AWS Managed Config Rules .
For custom rules, the identifier is the Amazon Resource Name (ARN) of the rule\'s AWS Lambda function, such as arn:aws:lambda:us-east-2:123456789012:function:custom_rule_name .

SourceDetails (list) --
Provides the source and type of the event that causes AWS Config to evaluate your AWS resources.

(dict) --
Provides the source and the message types that trigger AWS Config to evaluate your AWS resources against a rule. It also provides the frequency with which you want AWS Config to run evaluations for the rule if the trigger type is periodic. You can specify the parameter values for SourceDetail only for custom rules.

EventSource (string) --
The source of the event, such as an AWS service, that triggers AWS Config to evaluate your AWS resources.

MessageType (string) --
The type of notification that triggers AWS Config to run an evaluation for a rule. You can specify the following notification types:

ConfigurationItemChangeNotification - Triggers an evaluation when AWS Config delivers a configuration item as a result of a resource change.
OversizedConfigurationItemChangeNotification - Triggers an evaluation when AWS Config delivers an oversized configuration item. AWS Config may generate this notification type when a resource changes and the notification exceeds the maximum size allowed by Amazon SNS.
ScheduledNotification - Triggers a periodic evaluation at the frequency specified for MaximumExecutionFrequency .
ConfigurationSnapshotDeliveryCompleted - Triggers a periodic evaluation when AWS Config delivers a configuration snapshot.

If you want your custom rule to be triggered by configuration changes, specify two SourceDetail objects, one for ConfigurationItemChangeNotification and one for OversizedConfigurationItemChangeNotification .

MaximumExecutionFrequency (string) --
The frequency at which you want AWS Config to run evaluations for a custom rule with a periodic trigger. If you specify a value for MaximumExecutionFrequency , then MessageType must use the ScheduledNotification value.

Note
By default, rules with a periodic trigger are evaluated every 24 hours. To change the frequency, specify a valid value for the MaximumExecutionFrequency parameter.
Based on the valid value you choose, AWS Config runs evaluations once for each valid value. For example, if you choose Three_Hours , AWS Config runs evaluations once every three hours. In this case, Three_Hours is the frequency of this rule.








InputParameters (string) --
A string, in JSON format, that is passed to the AWS Config rule Lambda function.

MaximumExecutionFrequency (string) --
The maximum frequency with which AWS Config runs evaluations for a rule. You can specify a value for MaximumExecutionFrequency when:

You are using an AWS managed rule that is triggered at a periodic frequency.
Your custom rule is triggered when AWS Config delivers the configuration snapshot. For more information, see  ConfigSnapshotDeliveryProperties .


Note
By default, rules with a periodic trigger are evaluated every 24 hours. To change the frequency, specify a valid value for the MaximumExecutionFrequency parameter.


ConfigRuleState (string) --
Indicates whether the AWS Config rule is active or is currently being deleted by AWS Config. It can also indicate the evaluation status for the AWS Config rule.
AWS Config sets the state of the rule to EVALUATING temporarily after you use the StartConfigRulesEvaluation request to evaluate your resources against the AWS Config rule.
AWS Config sets the state of the rule to DELETING_RESULTS temporarily after you use the DeleteEvaluationResults request to delete the current evaluation results for the AWS Config rule.
AWS Config temporarily sets the state of a rule to DELETING after you use the DeleteConfigRule request to delete the rule. After AWS Config deletes the rule, the rule and all of its evaluations are erased and are no longer available.

CreatedBy (string) --
Service principal name of the service that created the rule.

Note
The field is populated only if the service linked rule is created by a service. The field is empty if you create your own rule.






NextToken (string) --
The string that you use in a subsequent request to get the next page of results in a paginated response.







Exceptions

ConfigService.Client.exceptions.NoSuchConfigRuleException
ConfigService.Client.exceptions.InvalidNextTokenException


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
                'ConfigRuleState': 'ACTIVE'|'DELETING'|'DELETING_RESULTS'|'EVALUATING',
                'CreatedBy': 'string'
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
    Returns status information for sources within an aggregator. The status includes information about the last time AWS Config verified authorization between the source account and an aggregator account. In case of a failure, the status contains the related error code or message.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_configuration_aggregator_sources_status(
        ConfigurationAggregatorName='string',
        UpdateStatus=[
            'FAILED'|'SUCCEEDED'|'OUTDATED',
        ],
        NextToken='string',
        Limit=123
    )
    
    
    :type ConfigurationAggregatorName: string
    :param ConfigurationAggregatorName: [REQUIRED]\nThe name of the configuration aggregator.\n

    :type UpdateStatus: list
    :param UpdateStatus: Filters the status type.\n\nValid value FAILED indicates errors while moving data.\nValid value SUCCEEDED indicates the data was successfully moved.\nValid value OUTDATED indicates the data is not the most recent.\n\n\n(string) --\n\n

    :type NextToken: string
    :param NextToken: The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.

    :type Limit: integer
    :param Limit: The maximum number of AggregatorSourceStatus returned on each page. The default is maximum. If you specify 0, AWS Config uses the default.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

AggregatedSourceStatusList (list) --
Returns an AggregatedSourceStatus object.

(dict) --
The current sync status between the source and the aggregator account.

SourceId (string) --
The source account ID or an organization.

SourceType (string) --
The source account or an organization.

AwsRegion (string) --
The region authorized to collect aggregated data.

LastUpdateStatus (string) --
Filters the last updated status type.

Valid value FAILED indicates errors while moving data.
Valid value SUCCEEDED indicates the data was successfully moved.
Valid value OUTDATED indicates the data is not the most recent.


LastUpdateTime (datetime) --
The time of the last update.

LastErrorCode (string) --
The error code that AWS Config returned when the source account aggregation last failed.

LastErrorMessage (string) --
The message indicating that the source account aggregation failed due to an error.





NextToken (string) --
The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.







Exceptions

ConfigService.Client.exceptions.InvalidParameterValueException
ConfigService.Client.exceptions.NoSuchConfigurationAggregatorException
ConfigService.Client.exceptions.InvalidNextTokenException
ConfigService.Client.exceptions.InvalidLimitException


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
    
    Exceptions
    
    :example: response = client.describe_configuration_aggregators(
        ConfigurationAggregatorNames=[
            'string',
        ],
        NextToken='string',
        Limit=123
    )
    
    
    :type ConfigurationAggregatorNames: list
    :param ConfigurationAggregatorNames: The name of the configuration aggregators.\n\n(string) --\n\n

    :type NextToken: string
    :param NextToken: The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.

    :type Limit: integer
    :param Limit: The maximum number of configuration aggregators returned on each page. The default is maximum. If you specify 0, AWS Config uses the default.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

ConfigurationAggregators (list) --
Returns a ConfigurationAggregators object.

(dict) --
The details about the configuration aggregator, including information about source accounts, regions, and metadata of the aggregator.

ConfigurationAggregatorName (string) --
The name of the aggregator.

ConfigurationAggregatorArn (string) --
The Amazon Resource Name (ARN) of the aggregator.

AccountAggregationSources (list) --
Provides a list of source accounts and regions to be aggregated.

(dict) --
A collection of accounts and regions.

AccountIds (list) --
The 12-digit account ID of the account being aggregated.

(string) --


AllAwsRegions (boolean) --
If true, aggregate existing AWS Config regions and future regions.

AwsRegions (list) --
The source regions being aggregated.

(string) --






OrganizationAggregationSource (dict) --
Provides an organization and list of regions to be aggregated.

RoleArn (string) --
ARN of the IAM role used to retrieve AWS Organization details associated with the aggregator account.

AwsRegions (list) --
The source regions being aggregated.

(string) --


AllAwsRegions (boolean) --
If true, aggregate existing AWS Config regions and future regions.



CreationTime (datetime) --
The time stamp when the configuration aggregator was created.

LastUpdatedTime (datetime) --
The time of the last update.





NextToken (string) --
The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.







Exceptions

ConfigService.Client.exceptions.InvalidParameterValueException
ConfigService.Client.exceptions.NoSuchConfigurationAggregatorException
ConfigService.Client.exceptions.InvalidNextTokenException
ConfigService.Client.exceptions.InvalidLimitException


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
    
    Exceptions
    
    :example: response = client.describe_configuration_recorder_status(
        ConfigurationRecorderNames=[
            'string',
        ]
    )
    
    
    :type ConfigurationRecorderNames: list
    :param ConfigurationRecorderNames: The name(s) of the configuration recorder. If the name is not specified, the action returns the current status of all the configuration recorders associated with the account.\n\n(string) --\n\n

    :rtype: dict
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

(dict) --The output for the  DescribeConfigurationRecorderStatus action, in JSON format.

ConfigurationRecordersStatus (list) --A list that contains status of the specified recorders.

(dict) --The current status of the configuration recorder.

name (string) --The name of the configuration recorder.

lastStartTime (datetime) --The time the recorder was last started.

lastStopTime (datetime) --The time the recorder was last stopped.

recording (boolean) --Specifies whether or not the recorder is currently recording.

lastStatus (string) --The last (previous) status of the recorder.

lastErrorCode (string) --The error code indicating that the recording failed.

lastErrorMessage (string) --The message indicating that the recording failed due to an error.

lastStatusChangeTime (datetime) --The time when the status was last changed.










Exceptions

ConfigService.Client.exceptions.NoSuchConfigurationRecorderException


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
    
    
    :returns: 
    ConfigService.Client.exceptions.NoSuchConfigurationRecorderException
    
    """
    pass

def describe_configuration_recorders(ConfigurationRecorderNames=None):
    """
    Returns the details for the specified configuration recorders. If the configuration recorder is not specified, this action returns the details for all configuration recorders associated with the account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_configuration_recorders(
        ConfigurationRecorderNames=[
            'string',
        ]
    )
    
    
    :type ConfigurationRecorderNames: list
    :param ConfigurationRecorderNames: A list of configuration recorder names.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'ConfigurationRecorders': [
        {
            'name': 'string',
            'roleARN': 'string',
            'recordingGroup': {
                'allSupported': True|False,
                'includeGlobalResourceTypes': True|False,
                'resourceTypes': [
                    'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::EC2::RegisteredHAInstance'|'AWS::EC2::NatGateway'|'AWS::EC2::EgressOnlyInternetGateway'|'AWS::EC2::VPCEndpoint'|'AWS::EC2::VPCEndpointService'|'AWS::EC2::FlowLog'|'AWS::EC2::VPCPeeringConnection'|'AWS::Elasticsearch::Domain'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::DBCluster'|'AWS::RDS::DBClusterSnapshot'|'AWS::RDS::EventSubscription'|'AWS::S3::Bucket'|'AWS::S3::AccountPublicAccessBlock'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::SSM::ManagedInstanceInventory'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::DynamoDB::Table'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::RuleGroup'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::RuleGroup'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::WAFv2::WebACL'|'AWS::WAFv2::RuleGroup'|'AWS::WAFv2::IPSet'|'AWS::WAFv2::RegexPatternSet'|'AWS::WAFv2::ManagedRuleSet'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::ApiGateway::Stage'|'AWS::ApiGateway::RestApi'|'AWS::ApiGatewayV2::Stage'|'AWS::ApiGatewayV2::Api'|'AWS::CodePipeline::Pipeline'|'AWS::ServiceCatalog::CloudFormationProvisionedProduct'|'AWS::ServiceCatalog::CloudFormationProduct'|'AWS::ServiceCatalog::Portfolio'|'AWS::SQS::Queue'|'AWS::KMS::Key'|'AWS::QLDB::Ledger',
                ]
            }
        },
    ]
}


Response Structure

(dict) --The output for the  DescribeConfigurationRecorders action.

ConfigurationRecorders (list) --A list that contains the descriptions of the specified configuration recorders.

(dict) --An object that represents the recording of configuration changes of an AWS resource.

name (string) --The name of the recorder. By default, AWS Config automatically assigns the name "default" when creating the configuration recorder. You cannot change the assigned name.

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













Exceptions

ConfigService.Client.exceptions.NoSuchConfigurationRecorderException


    :return: {
        'ConfigurationRecorders': [
            {
                'name': 'string',
                'roleARN': 'string',
                'recordingGroup': {
                    'allSupported': True|False,
                    'includeGlobalResourceTypes': True|False,
                    'resourceTypes': [
                        'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::EC2::RegisteredHAInstance'|'AWS::EC2::NatGateway'|'AWS::EC2::EgressOnlyInternetGateway'|'AWS::EC2::VPCEndpoint'|'AWS::EC2::VPCEndpointService'|'AWS::EC2::FlowLog'|'AWS::EC2::VPCPeeringConnection'|'AWS::Elasticsearch::Domain'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::DBCluster'|'AWS::RDS::DBClusterSnapshot'|'AWS::RDS::EventSubscription'|'AWS::S3::Bucket'|'AWS::S3::AccountPublicAccessBlock'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::SSM::ManagedInstanceInventory'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::DynamoDB::Table'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::RuleGroup'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::RuleGroup'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::WAFv2::WebACL'|'AWS::WAFv2::RuleGroup'|'AWS::WAFv2::IPSet'|'AWS::WAFv2::RegexPatternSet'|'AWS::WAFv2::ManagedRuleSet'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::ApiGateway::Stage'|'AWS::ApiGateway::RestApi'|'AWS::ApiGatewayV2::Stage'|'AWS::ApiGatewayV2::Api'|'AWS::CodePipeline::Pipeline'|'AWS::ServiceCatalog::CloudFormationProvisionedProduct'|'AWS::ServiceCatalog::CloudFormationProduct'|'AWS::ServiceCatalog::Portfolio'|'AWS::SQS::Queue'|'AWS::KMS::Key'|'AWS::QLDB::Ledger',
                    ]
                }
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_conformance_pack_compliance(ConformancePackName=None, Filters=None, Limit=None, NextToken=None):
    """
    Returns compliance details for each rule in that conformance pack.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_conformance_pack_compliance(
        ConformancePackName='string',
        Filters={
            'ConfigRuleNames': [
                'string',
            ],
            'ComplianceType': 'COMPLIANT'|'NON_COMPLIANT'
        },
        Limit=123,
        NextToken='string'
    )
    
    
    :type ConformancePackName: string
    :param ConformancePackName: [REQUIRED]\nName of the conformance pack.\n

    :type Filters: dict
    :param Filters: A ConformancePackComplianceFilters object.\n\nConfigRuleNames (list) --Filters the results by AWS Config rule names.\n\n(string) --\n\n\nComplianceType (string) --Filters the results by compliance.\nThe allowed values are COMPLIANT and NON_COMPLIANT .\n\n\n

    :type Limit: integer
    :param Limit: The maximum number of AWS Config rules within a conformance pack are returned on each page.

    :type NextToken: string
    :param NextToken: The nextToken string returned in a previous request that you use to request the next page of results in a paginated response.

    :rtype: dict

ReturnsResponse Syntax
{
    'ConformancePackName': 'string',
    'ConformancePackRuleComplianceList': [
        {
            'ConfigRuleName': 'string',
            'ComplianceType': 'COMPLIANT'|'NON_COMPLIANT'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

ConformancePackName (string) --
Name of the conformance pack.

ConformancePackRuleComplianceList (list) --
Returns a list of ConformancePackRuleCompliance objects.

(dict) --
Compliance information of one or more AWS Config rules within a conformance pack. You can filter using AWS Config rule names and compliance types.

ConfigRuleName (string) --
Name of the config rule.

ComplianceType (string) --
Compliance of the AWS Config rule
The allowed values are COMPLIANT and NON_COMPLIANT .





NextToken (string) --
The nextToken string returned in a previous request that you use to request the next page of results in a paginated response.







Exceptions

ConfigService.Client.exceptions.InvalidLimitException
ConfigService.Client.exceptions.InvalidNextTokenException
ConfigService.Client.exceptions.InvalidParameterValueException
ConfigService.Client.exceptions.NoSuchConfigRuleInConformancePackException
ConfigService.Client.exceptions.NoSuchConformancePackException


    :return: {
        'ConformancePackName': 'string',
        'ConformancePackRuleComplianceList': [
            {
                'ConfigRuleName': 'string',
                'ComplianceType': 'COMPLIANT'|'NON_COMPLIANT'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    ConfigService.Client.exceptions.InvalidLimitException
    ConfigService.Client.exceptions.InvalidNextTokenException
    ConfigService.Client.exceptions.InvalidParameterValueException
    ConfigService.Client.exceptions.NoSuchConfigRuleInConformancePackException
    ConfigService.Client.exceptions.NoSuchConformancePackException
    
    """
    pass

def describe_conformance_pack_status(ConformancePackNames=None, Limit=None, NextToken=None):
    """
    Provides one or more conformance packs deployment status.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_conformance_pack_status(
        ConformancePackNames=[
            'string',
        ],
        Limit=123,
        NextToken='string'
    )
    
    
    :type ConformancePackNames: list
    :param ConformancePackNames: Comma-separated list of conformance pack names.\n\n(string) --\n\n

    :type Limit: integer
    :param Limit: The maximum number of conformance packs status returned on each page.

    :type NextToken: string
    :param NextToken: The nextToken string returned in a previous request that you use to request the next page of results in a paginated response.

    :rtype: dict

ReturnsResponse Syntax
{
    'ConformancePackStatusDetails': [
        {
            'ConformancePackName': 'string',
            'ConformancePackId': 'string',
            'ConformancePackArn': 'string',
            'ConformancePackState': 'CREATE_IN_PROGRESS'|'CREATE_COMPLETE'|'CREATE_FAILED'|'DELETE_IN_PROGRESS'|'DELETE_FAILED',
            'StackArn': 'string',
            'ConformancePackStatusReason': 'string',
            'LastUpdateRequestedTime': datetime(2015, 1, 1),
            'LastUpdateCompletedTime': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

ConformancePackStatusDetails (list) --
A list of ConformancePackStatusDetail objects.

(dict) --
Status details of a conformance pack.

ConformancePackName (string) --
Name of the conformance pack.

ConformancePackId (string) --
ID of the conformance pack.

ConformancePackArn (string) --
Amazon Resource Name (ARN) of comformance pack.

ConformancePackState (string) --
Indicates deployment status of conformance pack.
AWS Config sets the state of the conformance pack to:

CREATE_IN_PROGRESS when a conformance pack creation is in progress for an account.
CREATE_COMPLETE when a conformance pack has been successfully created in your account.
CREATE_FAILED when a conformance pack creation failed in your account.
DELETE_IN_PROGRESS when a conformance pack deletion is in progress.
DELETE_FAILED when a conformance pack deletion failed in your account.


StackArn (string) --
Amazon Resource Name (ARN) of AWS CloudFormation stack.

ConformancePackStatusReason (string) --
The reason of conformance pack creation failure.

LastUpdateRequestedTime (datetime) --
Last time when conformation pack creation and update was requested.

LastUpdateCompletedTime (datetime) --
Last time when conformation pack creation and update was successful.





NextToken (string) --
The nextToken string returned in a previous request that you use to request the next page of results in a paginated response.







Exceptions

ConfigService.Client.exceptions.InvalidLimitException
ConfigService.Client.exceptions.InvalidNextTokenException


    :return: {
        'ConformancePackStatusDetails': [
            {
                'ConformancePackName': 'string',
                'ConformancePackId': 'string',
                'ConformancePackArn': 'string',
                'ConformancePackState': 'CREATE_IN_PROGRESS'|'CREATE_COMPLETE'|'CREATE_FAILED'|'DELETE_IN_PROGRESS'|'DELETE_FAILED',
                'StackArn': 'string',
                'ConformancePackStatusReason': 'string',
                'LastUpdateRequestedTime': datetime(2015, 1, 1),
                'LastUpdateCompletedTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    CREATE_IN_PROGRESS when a conformance pack creation is in progress for an account.
    CREATE_COMPLETE when a conformance pack has been successfully created in your account.
    CREATE_FAILED when a conformance pack creation failed in your account.
    DELETE_IN_PROGRESS when a conformance pack deletion is in progress.
    DELETE_FAILED when a conformance pack deletion failed in your account.
    
    """
    pass

def describe_conformance_packs(ConformancePackNames=None, Limit=None, NextToken=None):
    """
    Returns a list of one or more conformance packs.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_conformance_packs(
        ConformancePackNames=[
            'string',
        ],
        Limit=123,
        NextToken='string'
    )
    
    
    :type ConformancePackNames: list
    :param ConformancePackNames: Comma-separated list of conformance pack names for which you want details. If you do not specify any names, AWS Config returns details for all your conformance packs.\n\n(string) --\n\n

    :type Limit: integer
    :param Limit: The maximum number of conformance packs returned on each page.

    :type NextToken: string
    :param NextToken: The nextToken string returned in a previous request that you use to request the next page of results in a paginated response.

    :rtype: dict

ReturnsResponse Syntax
{
    'ConformancePackDetails': [
        {
            'ConformancePackName': 'string',
            'ConformancePackArn': 'string',
            'ConformancePackId': 'string',
            'DeliveryS3Bucket': 'string',
            'DeliveryS3KeyPrefix': 'string',
            'ConformancePackInputParameters': [
                {
                    'ParameterName': 'string',
                    'ParameterValue': 'string'
                },
            ],
            'LastUpdateRequestedTime': datetime(2015, 1, 1),
            'CreatedBy': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

ConformancePackDetails (list) --
Returns a list of ConformancePackDetail objects.

(dict) --
Returns details of a conformance pack. A conformance pack is a collection of AWS Config rules and remediation actions that can be easily deployed in an account and a region.

ConformancePackName (string) --
Name of the conformance pack.

ConformancePackArn (string) --
Amazon Resource Name (ARN) of the conformance pack.

ConformancePackId (string) --
ID of the conformance pack.

DeliveryS3Bucket (string) --
Conformance pack template that is used to create a pack. The delivery bucket name should start with awsconfigconforms. For example: "Resource": "arn:aws:s3:::your_bucket_name/*".

DeliveryS3KeyPrefix (string) --
The prefix for the Amazon S3 bucket.

ConformancePackInputParameters (list) --
A list of ConformancePackInputParameter objects.

(dict) --
Input parameters in the form of key-value pairs for the conformance pack, both of which you define. Keys can have a maximum character length of 128 characters, and values can have a maximum length of 256 characters.

ParameterName (string) --
One part of a key-value pair.

ParameterValue (string) --
Another part of the key-value pair.





LastUpdateRequestedTime (datetime) --
Last time when conformation pack update was requested.

CreatedBy (string) --
AWS service that created the conformance pack.





NextToken (string) --
The nextToken string returned in a previous request that you use to request the next page of results in a paginated response.







Exceptions

ConfigService.Client.exceptions.NoSuchConformancePackException
ConfigService.Client.exceptions.InvalidLimitException
ConfigService.Client.exceptions.InvalidNextTokenException


    :return: {
        'ConformancePackDetails': [
            {
                'ConformancePackName': 'string',
                'ConformancePackArn': 'string',
                'ConformancePackId': 'string',
                'DeliveryS3Bucket': 'string',
                'DeliveryS3KeyPrefix': 'string',
                'ConformancePackInputParameters': [
                    {
                        'ParameterName': 'string',
                        'ParameterValue': 'string'
                    },
                ],
                'LastUpdateRequestedTime': datetime(2015, 1, 1),
                'CreatedBy': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    ConfigService.Client.exceptions.NoSuchConformancePackException
    ConfigService.Client.exceptions.InvalidLimitException
    ConfigService.Client.exceptions.InvalidNextTokenException
    
    """
    pass

def describe_delivery_channel_status(DeliveryChannelNames=None):
    """
    Returns the current status of the specified delivery channel. If a delivery channel is not specified, this action returns the current status of all delivery channels associated with the account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_delivery_channel_status(
        DeliveryChannelNames=[
            'string',
        ]
    )
    
    
    :type DeliveryChannelNames: list
    :param DeliveryChannelNames: A list of delivery channel names.\n\n(string) --\n\n

    :rtype: dict
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

(dict) --The output for the  DescribeDeliveryChannelStatus action.

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












Exceptions

ConfigService.Client.exceptions.NoSuchDeliveryChannelException


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
    
    
    :returns: 
    ConfigService.Client.exceptions.NoSuchDeliveryChannelException
    
    """
    pass

def describe_delivery_channels(DeliveryChannelNames=None):
    """
    Returns details about the specified delivery channel. If a delivery channel is not specified, this action returns the details of all delivery channels associated with the account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_delivery_channels(
        DeliveryChannelNames=[
            'string',
        ]
    )
    
    
    :type DeliveryChannelNames: list
    :param DeliveryChannelNames: A list of delivery channel names.\n\n(string) --\n\n

    :rtype: dict
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

(dict) --The output for the  DescribeDeliveryChannels action.

DeliveryChannels (list) --A list that contains the descriptions of the specified delivery channel.

(dict) --The channel through which AWS Config delivers notifications and updated configuration states.

name (string) --The name of the delivery channel. By default, AWS Config assigns the name "default" when creating the delivery channel. To change the delivery channel name, you must use the DeleteDeliveryChannel action to delete your current delivery channel, and then you must use the PutDeliveryChannel command to create a delivery channel that has the desired name.

s3BucketName (string) --The name of the Amazon S3 bucket to which AWS Config delivers configuration snapshots and configuration history files.
If you specify a bucket that belongs to another AWS account, that bucket must have policies that grant access permissions to AWS Config. For more information, see Permissions for the Amazon S3 Bucket in the AWS Config Developer Guide.

s3KeyPrefix (string) --The prefix for the specified Amazon S3 bucket.

snsTopicARN (string) --The Amazon Resource Name (ARN) of the Amazon SNS topic to which AWS Config sends notifications about configuration changes.
If you choose a topic from another account, the topic must have policies that grant access permissions to AWS Config. For more information, see Permissions for the Amazon SNS Topic in the AWS Config Developer Guide.

configSnapshotDeliveryProperties (dict) --The options for how often AWS Config delivers configuration snapshots to the Amazon S3 bucket.

deliveryFrequency (string) --The frequency with which AWS Config delivers configuration snapshots.












Exceptions

ConfigService.Client.exceptions.NoSuchDeliveryChannelException


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
    
    
    :returns: 
    ConfigService.Client.exceptions.NoSuchDeliveryChannelException
    
    """
    pass

def describe_organization_config_rule_statuses(OrganizationConfigRuleNames=None, Limit=None, NextToken=None):
    """
    Provides organization config rule deployment status for an organization.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_organization_config_rule_statuses(
        OrganizationConfigRuleNames=[
            'string',
        ],
        Limit=123,
        NextToken='string'
    )
    
    
    :type OrganizationConfigRuleNames: list
    :param OrganizationConfigRuleNames: The names of organization config rules for which you want status details. If you do not specify any names, AWS Config returns details for all your organization AWS Confg rules.\n\n(string) --\n\n

    :type Limit: integer
    :param Limit: The maximum number of OrganizationConfigRuleStatuses returned on each page. If you do no specify a number, AWS Config uses the default. The default is 100.

    :type NextToken: string
    :param NextToken: The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.

    :rtype: dict

ReturnsResponse Syntax
{
    'OrganizationConfigRuleStatuses': [
        {
            'OrganizationConfigRuleName': 'string',
            'OrganizationRuleStatus': 'CREATE_SUCCESSFUL'|'CREATE_IN_PROGRESS'|'CREATE_FAILED'|'DELETE_SUCCESSFUL'|'DELETE_FAILED'|'DELETE_IN_PROGRESS'|'UPDATE_SUCCESSFUL'|'UPDATE_IN_PROGRESS'|'UPDATE_FAILED',
            'ErrorCode': 'string',
            'ErrorMessage': 'string',
            'LastUpdateTime': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

OrganizationConfigRuleStatuses (list) --
A list of OrganizationConfigRuleStatus objects.

(dict) --
Returns the status for an organization config rule in an organization.

OrganizationConfigRuleName (string) --
The name that you assign to organization config rule.

OrganizationRuleStatus (string) --
Indicates deployment status of an organization config rule. When master account calls PutOrganizationConfigRule action for the first time, config rule status is created in all the member accounts. When master account calls PutOrganizationConfigRule action for the second time, config rule status is updated in all the member accounts. Additionally, config rule status is updated when one or more member accounts join or leave an organization. Config rule status is deleted when the master account deletes OrganizationConfigRule in all the member accounts and disables service access for config-multiaccountsetup.amazonaws.com .
AWS Config sets the state of the rule to:

CREATE_SUCCESSFUL when an organization config rule has been successfully created in all the member accounts.
CREATE_IN_PROGRESS when an organization config rule creation is in progress.
CREATE_FAILED when an organization config rule creation failed in one or more member accounts within that organization.
DELETE_FAILED when an organization config rule deletion failed in one or more member accounts within that organization.
DELETE_IN_PROGRESS when an organization config rule deletion is in progress.
DELETE_SUCCESSFUL when an organization config rule has been successfully deleted from all the member accounts.
UPDATE_SUCCESSFUL when an organization config rule has been successfully updated in all the member accounts.
UPDATE_IN_PROGRESS when an organization config rule update is in progress.
UPDATE_FAILED when an organization config rule update failed in one or more member accounts within that organization.


ErrorCode (string) --
An error code that is returned when organization config rule creation or deletion has failed.

ErrorMessage (string) --
An error message indicating that organization config rule creation or deletion failed due to an error.

LastUpdateTime (datetime) --
The timestamp of the last update.





NextToken (string) --
The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.







Exceptions

ConfigService.Client.exceptions.NoSuchOrganizationConfigRuleException
ConfigService.Client.exceptions.InvalidLimitException
ConfigService.Client.exceptions.InvalidNextTokenException
ConfigService.Client.exceptions.OrganizationAccessDeniedException


    :return: {
        'OrganizationConfigRuleStatuses': [
            {
                'OrganizationConfigRuleName': 'string',
                'OrganizationRuleStatus': 'CREATE_SUCCESSFUL'|'CREATE_IN_PROGRESS'|'CREATE_FAILED'|'DELETE_SUCCESSFUL'|'DELETE_FAILED'|'DELETE_IN_PROGRESS'|'UPDATE_SUCCESSFUL'|'UPDATE_IN_PROGRESS'|'UPDATE_FAILED',
                'ErrorCode': 'string',
                'ErrorMessage': 'string',
                'LastUpdateTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    CREATE_SUCCESSFUL when an organization config rule has been successfully created in all the member accounts.
    CREATE_IN_PROGRESS when an organization config rule creation is in progress.
    CREATE_FAILED when an organization config rule creation failed in one or more member accounts within that organization.
    DELETE_FAILED when an organization config rule deletion failed in one or more member accounts within that organization.
    DELETE_IN_PROGRESS when an organization config rule deletion is in progress.
    DELETE_SUCCESSFUL when an organization config rule has been successfully deleted from all the member accounts.
    UPDATE_SUCCESSFUL when an organization config rule has been successfully updated in all the member accounts.
    UPDATE_IN_PROGRESS when an organization config rule update is in progress.
    UPDATE_FAILED when an organization config rule update failed in one or more member accounts within that organization.
    
    """
    pass

def describe_organization_config_rules(OrganizationConfigRuleNames=None, Limit=None, NextToken=None):
    """
    Returns a list of organization config rules.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_organization_config_rules(
        OrganizationConfigRuleNames=[
            'string',
        ],
        Limit=123,
        NextToken='string'
    )
    
    
    :type OrganizationConfigRuleNames: list
    :param OrganizationConfigRuleNames: The names of organization config rules for which you want details. If you do not specify any names, AWS Config returns details for all your organization config rules.\n\n(string) --\n\n

    :type Limit: integer
    :param Limit: The maximum number of organization config rules returned on each page. If you do no specify a number, AWS Config uses the default. The default is 100.

    :type NextToken: string
    :param NextToken: The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.

    :rtype: dict

ReturnsResponse Syntax
{
    'OrganizationConfigRules': [
        {
            'OrganizationConfigRuleName': 'string',
            'OrganizationConfigRuleArn': 'string',
            'OrganizationManagedRuleMetadata': {
                'Description': 'string',
                'RuleIdentifier': 'string',
                'InputParameters': 'string',
                'MaximumExecutionFrequency': 'One_Hour'|'Three_Hours'|'Six_Hours'|'Twelve_Hours'|'TwentyFour_Hours',
                'ResourceTypesScope': [
                    'string',
                ],
                'ResourceIdScope': 'string',
                'TagKeyScope': 'string',
                'TagValueScope': 'string'
            },
            'OrganizationCustomRuleMetadata': {
                'Description': 'string',
                'LambdaFunctionArn': 'string',
                'OrganizationConfigRuleTriggerTypes': [
                    'ConfigurationItemChangeNotification'|'OversizedConfigurationItemChangeNotification'|'ScheduledNotification',
                ],
                'InputParameters': 'string',
                'MaximumExecutionFrequency': 'One_Hour'|'Three_Hours'|'Six_Hours'|'Twelve_Hours'|'TwentyFour_Hours',
                'ResourceTypesScope': [
                    'string',
                ],
                'ResourceIdScope': 'string',
                'TagKeyScope': 'string',
                'TagValueScope': 'string'
            },
            'ExcludedAccounts': [
                'string',
            ],
            'LastUpdateTime': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

OrganizationConfigRules (list) --
Returns a list of OrganizationConfigRule objects.

(dict) --
An organization config rule that has information about config rules that AWS Config creates in member accounts.

OrganizationConfigRuleName (string) --
The name that you assign to organization config rule.

OrganizationConfigRuleArn (string) --
Amazon Resource Name (ARN) of organization config rule.

OrganizationManagedRuleMetadata (dict) --
An OrganizationManagedRuleMetadata object.

Description (string) --
The description that you provide for organization config rule.

RuleIdentifier (string) --
For organization config managed rules, a predefined identifier from a list. For example, IAM_PASSWORD_POLICY is a managed rule. To reference a managed rule, see Using AWS Managed Config Rules .

InputParameters (string) --
A string, in JSON format, that is passed to organization config rule Lambda function.

MaximumExecutionFrequency (string) --
The maximum frequency with which AWS Config runs evaluations for a rule. You are using an AWS managed rule that is triggered at a periodic frequency.

Note
By default, rules with a periodic trigger are evaluated every 24 hours. To change the frequency, specify a valid value for the MaximumExecutionFrequency parameter.


ResourceTypesScope (list) --
The type of the AWS resource that was evaluated.

(string) --


ResourceIdScope (string) --
The ID of the AWS resource that was evaluated.

TagKeyScope (string) --
One part of a key-value pair that make up a tag. A key is a general label that acts like a category for more specific tag values.

TagValueScope (string) --
The optional part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key).



OrganizationCustomRuleMetadata (dict) --
An OrganizationCustomRuleMetadata object.

Description (string) --
The description that you provide for organization config rule.

LambdaFunctionArn (string) --
The lambda function ARN.

OrganizationConfigRuleTriggerTypes (list) --
The type of notification that triggers AWS Config to run an evaluation for a rule. You can specify the following notification types:

ConfigurationItemChangeNotification - Triggers an evaluation when AWS Config delivers a configuration item as a result of a resource change.
OversizedConfigurationItemChangeNotification - Triggers an evaluation when AWS Config delivers an oversized configuration item. AWS Config may generate this notification type when a resource changes and the notification exceeds the maximum size allowed by Amazon SNS.
ScheduledNotification - Triggers a periodic evaluation at the frequency specified for MaximumExecutionFrequency .


(string) --


InputParameters (string) --
A string, in JSON format, that is passed to organization config rule Lambda function.

MaximumExecutionFrequency (string) --
The maximum frequency with which AWS Config runs evaluations for a rule. Your custom rule is triggered when AWS Config delivers the configuration snapshot. For more information, see  ConfigSnapshotDeliveryProperties .

Note
By default, rules with a periodic trigger are evaluated every 24 hours. To change the frequency, specify a valid value for the MaximumExecutionFrequency parameter.


ResourceTypesScope (list) --
The type of the AWS resource that was evaluated.

(string) --


ResourceIdScope (string) --
The ID of the AWS resource that was evaluated.

TagKeyScope (string) --
One part of a key-value pair that make up a tag. A key is a general label that acts like a category for more specific tag values.

TagValueScope (string) --
The optional part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key).



ExcludedAccounts (list) --
A comma-separated list of accounts excluded from organization config rule.

(string) --


LastUpdateTime (datetime) --
The timestamp of the last update.





NextToken (string) --
The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.







Exceptions

ConfigService.Client.exceptions.NoSuchOrganizationConfigRuleException
ConfigService.Client.exceptions.InvalidNextTokenException
ConfigService.Client.exceptions.InvalidLimitException
ConfigService.Client.exceptions.OrganizationAccessDeniedException


    :return: {
        'OrganizationConfigRules': [
            {
                'OrganizationConfigRuleName': 'string',
                'OrganizationConfigRuleArn': 'string',
                'OrganizationManagedRuleMetadata': {
                    'Description': 'string',
                    'RuleIdentifier': 'string',
                    'InputParameters': 'string',
                    'MaximumExecutionFrequency': 'One_Hour'|'Three_Hours'|'Six_Hours'|'Twelve_Hours'|'TwentyFour_Hours',
                    'ResourceTypesScope': [
                        'string',
                    ],
                    'ResourceIdScope': 'string',
                    'TagKeyScope': 'string',
                    'TagValueScope': 'string'
                },
                'OrganizationCustomRuleMetadata': {
                    'Description': 'string',
                    'LambdaFunctionArn': 'string',
                    'OrganizationConfigRuleTriggerTypes': [
                        'ConfigurationItemChangeNotification'|'OversizedConfigurationItemChangeNotification'|'ScheduledNotification',
                    ],
                    'InputParameters': 'string',
                    'MaximumExecutionFrequency': 'One_Hour'|'Three_Hours'|'Six_Hours'|'Twelve_Hours'|'TwentyFour_Hours',
                    'ResourceTypesScope': [
                        'string',
                    ],
                    'ResourceIdScope': 'string',
                    'TagKeyScope': 'string',
                    'TagValueScope': 'string'
                },
                'ExcludedAccounts': [
                    'string',
                ],
                'LastUpdateTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_organization_conformance_pack_statuses(OrganizationConformancePackNames=None, Limit=None, NextToken=None):
    """
    Provides organization conformance pack deployment status for an organization.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_organization_conformance_pack_statuses(
        OrganizationConformancePackNames=[
            'string',
        ],
        Limit=123,
        NextToken='string'
    )
    
    
    :type OrganizationConformancePackNames: list
    :param OrganizationConformancePackNames: The names of organization conformance packs for which you want status details. If you do not specify any names, AWS Config returns details for all your organization conformance packs.\n\n(string) --\n\n

    :type Limit: integer
    :param Limit: The maximum number of OrganizationConformancePackStatuses returned on each page. If you do no specify a number, AWS Config uses the default. The default is 100.

    :type NextToken: string
    :param NextToken: The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.

    :rtype: dict

ReturnsResponse Syntax
{
    'OrganizationConformancePackStatuses': [
        {
            'OrganizationConformancePackName': 'string',
            'Status': 'CREATE_SUCCESSFUL'|'CREATE_IN_PROGRESS'|'CREATE_FAILED'|'DELETE_SUCCESSFUL'|'DELETE_FAILED'|'DELETE_IN_PROGRESS'|'UPDATE_SUCCESSFUL'|'UPDATE_IN_PROGRESS'|'UPDATE_FAILED',
            'ErrorCode': 'string',
            'ErrorMessage': 'string',
            'LastUpdateTime': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

OrganizationConformancePackStatuses (list) --
A list of OrganizationConformancePackStatus objects.

(dict) --
Returns the status for an organization conformance pack in an organization.

OrganizationConformancePackName (string) --
The name that you assign to organization conformance pack.

Status (string) --
Indicates deployment status of an organization conformance pack. When master account calls PutOrganizationConformancePack for the first time, conformance pack status is created in all the member accounts. When master account calls PutOrganizationConformancePack for the second time, conformance pack status is updated in all the member accounts. Additionally, conformance pack status is updated when one or more member accounts join or leave an organization. Conformance pack status is deleted when the master account deletes OrganizationConformancePack in all the member accounts and disables service access for config-multiaccountsetup.amazonaws.com .
AWS Config sets the state of the conformance pack to:

CREATE_SUCCESSFUL when an organization conformance pack has been successfully created in all the member accounts.
CREATE_IN_PROGRESS when an organization conformance pack creation is in progress.
CREATE_FAILED when an organization conformance pack creation failed in one or more member accounts within that organization.
DELETE_FAILED when an organization conformance pack deletion failed in one or more member accounts within that organization.
DELETE_IN_PROGRESS when an organization conformance pack deletion is in progress.
DELETE_SUCCESSFUL when an organization conformance pack has been successfully deleted from all the member accounts.
UPDATE_SUCCESSFUL when an organization conformance pack has been successfully updated in all the member accounts.
UPDATE_IN_PROGRESS when an organization conformance pack update is in progress.
UPDATE_FAILED when an organization conformance pack update failed in one or more member accounts within that organization.


ErrorCode (string) --
An error code that is returned when organization conformance pack creation or deletion has failed in a member account.

ErrorMessage (string) --
An error message indicating that organization conformance pack creation or deletion failed due to an error.

LastUpdateTime (datetime) --
The timestamp of the last update.





NextToken (string) --
The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.







Exceptions

ConfigService.Client.exceptions.NoSuchOrganizationConformancePackException
ConfigService.Client.exceptions.InvalidLimitException
ConfigService.Client.exceptions.InvalidNextTokenException
ConfigService.Client.exceptions.OrganizationAccessDeniedException


    :return: {
        'OrganizationConformancePackStatuses': [
            {
                'OrganizationConformancePackName': 'string',
                'Status': 'CREATE_SUCCESSFUL'|'CREATE_IN_PROGRESS'|'CREATE_FAILED'|'DELETE_SUCCESSFUL'|'DELETE_FAILED'|'DELETE_IN_PROGRESS'|'UPDATE_SUCCESSFUL'|'UPDATE_IN_PROGRESS'|'UPDATE_FAILED',
                'ErrorCode': 'string',
                'ErrorMessage': 'string',
                'LastUpdateTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    CREATE_SUCCESSFUL when an organization conformance pack has been successfully created in all the member accounts.
    CREATE_IN_PROGRESS when an organization conformance pack creation is in progress.
    CREATE_FAILED when an organization conformance pack creation failed in one or more member accounts within that organization.
    DELETE_FAILED when an organization conformance pack deletion failed in one or more member accounts within that organization.
    DELETE_IN_PROGRESS when an organization conformance pack deletion is in progress.
    DELETE_SUCCESSFUL when an organization conformance pack has been successfully deleted from all the member accounts.
    UPDATE_SUCCESSFUL when an organization conformance pack has been successfully updated in all the member accounts.
    UPDATE_IN_PROGRESS when an organization conformance pack update is in progress.
    UPDATE_FAILED when an organization conformance pack update failed in one or more member accounts within that organization.
    
    """
    pass

def describe_organization_conformance_packs(OrganizationConformancePackNames=None, Limit=None, NextToken=None):
    """
    Returns a list of organization conformance packs.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_organization_conformance_packs(
        OrganizationConformancePackNames=[
            'string',
        ],
        Limit=123,
        NextToken='string'
    )
    
    
    :type OrganizationConformancePackNames: list
    :param OrganizationConformancePackNames: The name that you assign to an organization conformance pack.\n\n(string) --\n\n

    :type Limit: integer
    :param Limit: The maximum number of organization config packs returned on each page. If you do no specify a number, AWS Config uses the default. The default is 100.

    :type NextToken: string
    :param NextToken: The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.

    :rtype: dict

ReturnsResponse Syntax
{
    'OrganizationConformancePacks': [
        {
            'OrganizationConformancePackName': 'string',
            'OrganizationConformancePackArn': 'string',
            'DeliveryS3Bucket': 'string',
            'DeliveryS3KeyPrefix': 'string',
            'ConformancePackInputParameters': [
                {
                    'ParameterName': 'string',
                    'ParameterValue': 'string'
                },
            ],
            'ExcludedAccounts': [
                'string',
            ],
            'LastUpdateTime': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

OrganizationConformancePacks (list) --
Returns a list of OrganizationConformancePacks objects.

(dict) --
An organization conformance pack that has information about conformance packs that AWS Config creates in member accounts.

OrganizationConformancePackName (string) --
The name you assign to an organization conformance pack.

OrganizationConformancePackArn (string) --
Amazon Resource Name (ARN) of organization conformance pack.

DeliveryS3Bucket (string) --
Location of an Amazon S3 bucket where AWS Config can deliver evaluation results and conformance pack template that is used to create a pack.

DeliveryS3KeyPrefix (string) --
Any folder structure you want to add to an Amazon S3 bucket.

ConformancePackInputParameters (list) --
A list of ConformancePackInputParameter objects.

(dict) --
Input parameters in the form of key-value pairs for the conformance pack, both of which you define. Keys can have a maximum character length of 128 characters, and values can have a maximum length of 256 characters.

ParameterName (string) --
One part of a key-value pair.

ParameterValue (string) --
Another part of the key-value pair.





ExcludedAccounts (list) --
A comma-separated list of accounts excluded from organization conformance pack.

(string) --


LastUpdateTime (datetime) --
Last time when organization conformation pack was updated.





NextToken (string) --
The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.







Exceptions

ConfigService.Client.exceptions.NoSuchOrganizationConformancePackException
ConfigService.Client.exceptions.InvalidNextTokenException
ConfigService.Client.exceptions.InvalidLimitException
ConfigService.Client.exceptions.OrganizationAccessDeniedException


    :return: {
        'OrganizationConformancePacks': [
            {
                'OrganizationConformancePackName': 'string',
                'OrganizationConformancePackArn': 'string',
                'DeliveryS3Bucket': 'string',
                'DeliveryS3KeyPrefix': 'string',
                'ConformancePackInputParameters': [
                    {
                        'ParameterName': 'string',
                        'ParameterValue': 'string'
                    },
                ],
                'ExcludedAccounts': [
                    'string',
                ],
                'LastUpdateTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_pending_aggregation_requests(Limit=None, NextToken=None):
    """
    Returns a list of all pending aggregation requests.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_pending_aggregation_requests(
        Limit=123,
        NextToken='string'
    )
    
    
    :type Limit: integer
    :param Limit: The maximum number of evaluation results returned on each page. The default is maximum. If you specify 0, AWS Config uses the default.

    :type NextToken: string
    :param NextToken: The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.

    :rtype: dict

ReturnsResponse Syntax
{
    'PendingAggregationRequests': [
        {
            'RequesterAccountId': 'string',
            'RequesterAwsRegion': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

PendingAggregationRequests (list) --
Returns a PendingAggregationRequests object.

(dict) --
An object that represents the account ID and region of an aggregator account that is requesting authorization but is not yet authorized.

RequesterAccountId (string) --
The 12-digit account ID of the account requesting to aggregate data.

RequesterAwsRegion (string) --
The region requesting to aggregate data.





NextToken (string) --
The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.







Exceptions

ConfigService.Client.exceptions.InvalidParameterValueException
ConfigService.Client.exceptions.InvalidNextTokenException
ConfigService.Client.exceptions.InvalidLimitException


    :return: {
        'PendingAggregationRequests': [
            {
                'RequesterAccountId': 'string',
                'RequesterAwsRegion': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    ConfigService.Client.exceptions.InvalidParameterValueException
    ConfigService.Client.exceptions.InvalidNextTokenException
    ConfigService.Client.exceptions.InvalidLimitException
    
    """
    pass

def describe_remediation_configurations(ConfigRuleNames=None):
    """
    Returns the details of one or more remediation configurations.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_remediation_configurations(
        ConfigRuleNames=[
            'string',
        ]
    )
    
    
    :type ConfigRuleNames: list
    :param ConfigRuleNames: [REQUIRED]\nA list of AWS Config rule names of remediation configurations for which you want details.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'RemediationConfigurations': [
        {
            'ConfigRuleName': 'string',
            'TargetType': 'SSM_DOCUMENT',
            'TargetId': 'string',
            'TargetVersion': 'string',
            'Parameters': {
                'string': {
                    'ResourceValue': {
                        'Value': 'RESOURCE_ID'
                    },
                    'StaticValue': {
                        'Values': [
                            'string',
                        ]
                    }
                }
            },
            'ResourceType': 'string',
            'Automatic': True|False,
            'ExecutionControls': {
                'SsmControls': {
                    'ConcurrentExecutionRatePercentage': 123,
                    'ErrorPercentage': 123
                }
            },
            'MaximumAutomaticAttempts': 123,
            'RetryAttemptSeconds': 123,
            'Arn': 'string',
            'CreatedByService': 'string'
        },
    ]
}


Response Structure

(dict) --
RemediationConfigurations (list) --Returns a remediation configuration object.

(dict) --An object that represents the details about the remediation configuration that includes the remediation action, parameters, and data to execute the action.

ConfigRuleName (string) --The name of the AWS Config rule.

TargetType (string) --The type of the target. Target executes remediation. For example, SSM document.

TargetId (string) --Target ID is the name of the public document.

TargetVersion (string) --Version of the target. For example, version of the SSM document.

Parameters (dict) --An object of the RemediationParameterValue.

(string) --
(dict) --The value is either a dynamic (resource) value or a static value. You must select either a dynamic value or a static value.

ResourceValue (dict) --The value is dynamic and changes at run-time.

Value (string) --The value is a resource ID.



StaticValue (dict) --The value is static and does not change at run-time.

Values (list) --A list of values. For example, the ARN of the assumed role.

(string) --










ResourceType (string) --The type of a resource.

Automatic (boolean) --The remediation is triggered automatically.

ExecutionControls (dict) --An ExecutionControls object.

SsmControls (dict) --A SsmControls object.

ConcurrentExecutionRatePercentage (integer) --The maximum percentage of remediation actions allowed to run in parallel on the non-compliant resources for that specific rule. You can specify a percentage, such as 10%. The default value is 10.

ErrorPercentage (integer) --The percentage of errors that are allowed before SSM stops running automations on non-compliant resources for that specific rule. You can specify a percentage of errors, for example 10%. If you do not specifiy a percentage, the default is 50%. For example, if you set the ErrorPercentage to 40% for 10 non-compliant resources, then SSM stops running the automations when the fifth error is received.





MaximumAutomaticAttempts (integer) --The maximum number of failed attempts for auto-remediation. If you do not select a number, the default is 5.
For example, if you specify MaximumAutomaticAttempts as 5 with RetryAttemptsSeconds as 50 seconds, AWS Config throws an exception after the 5th failed attempt within 50 seconds.

RetryAttemptSeconds (integer) --Maximum time in seconds that AWS Config runs auto-remediation. If you do not select a number, the default is 60 seconds.
For example, if you specify RetryAttemptsSeconds as 50 seconds and MaximumAutomaticAttempts as 5, AWS Config will run auto-remediations 5 times within 50 seconds before throwing an exception.

Arn (string) --Amazon Resource Name (ARN) of remediation configuration.

CreatedByService (string) --Name of the service that owns the service linked rule, if applicable.











    :return: {
        'RemediationConfigurations': [
            {
                'ConfigRuleName': 'string',
                'TargetType': 'SSM_DOCUMENT',
                'TargetId': 'string',
                'TargetVersion': 'string',
                'Parameters': {
                    'string': {
                        'ResourceValue': {
                            'Value': 'RESOURCE_ID'
                        },
                        'StaticValue': {
                            'Values': [
                                'string',
                            ]
                        }
                    }
                },
                'ResourceType': 'string',
                'Automatic': True|False,
                'ExecutionControls': {
                    'SsmControls': {
                        'ConcurrentExecutionRatePercentage': 123,
                        'ErrorPercentage': 123
                    }
                },
                'MaximumAutomaticAttempts': 123,
                'RetryAttemptSeconds': 123,
                'Arn': 'string',
                'CreatedByService': 'string'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_remediation_exceptions(ConfigRuleName=None, ResourceKeys=None, Limit=None, NextToken=None):
    """
    Returns the details of one or more remediation exceptions. A detailed view of a remediation exception for a set of resources that includes an explanation of an exception and the time when the exception will be deleted. When you specify the limit and the next token, you receive a paginated response.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_remediation_exceptions(
        ConfigRuleName='string',
        ResourceKeys=[
            {
                'ResourceType': 'string',
                'ResourceId': 'string'
            },
        ],
        Limit=123,
        NextToken='string'
    )
    
    
    :type ConfigRuleName: string
    :param ConfigRuleName: [REQUIRED]\nThe name of the AWS Config rule.\n

    :type ResourceKeys: list
    :param ResourceKeys: An exception list of resource exception keys to be processed with the current request. AWS Config adds exception for each resource key. For example, AWS Config adds 3 exceptions for 3 resource keys.\n\n(dict) --The details that identify a resource within AWS Config, including the resource type and resource ID.\n\nResourceType (string) --The type of a resource.\n\nResourceId (string) --The ID of the resource (for example., sg-xxxxxx).\n\n\n\n\n

    :type Limit: integer
    :param Limit: The maximum number of RemediationExceptionResourceKey returned on each page. The default is 25. If you specify 0, AWS Config uses the default.

    :type NextToken: string
    :param NextToken: The nextToken string returned in a previous request that you use to request the next page of results in a paginated response.

    :rtype: dict

ReturnsResponse Syntax
{
    'RemediationExceptions': [
        {
            'ConfigRuleName': 'string',
            'ResourceType': 'string',
            'ResourceId': 'string',
            'Message': 'string',
            'ExpirationTime': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

RemediationExceptions (list) --
Returns a list of remediation exception objects.

(dict) --
An object that represents the details about the remediation exception. The details include the rule name, an explanation of an exception, the time when the exception will be deleted, the resource ID, and resource type.

ConfigRuleName (string) --
The name of the AWS Config rule.

ResourceType (string) --
The type of a resource.

ResourceId (string) --
The ID of the resource (for example., sg-xxxxxx).

Message (string) --
An explanation of an remediation exception.

ExpirationTime (datetime) --
The time when the remediation exception will be deleted.





NextToken (string) --
The nextToken string returned in a previous request that you use to request the next page of results in a paginated response.







Exceptions

ConfigService.Client.exceptions.InvalidNextTokenException
ConfigService.Client.exceptions.InvalidParameterValueException


    :return: {
        'RemediationExceptions': [
            {
                'ConfigRuleName': 'string',
                'ResourceType': 'string',
                'ResourceId': 'string',
                'Message': 'string',
                'ExpirationTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    ConfigService.Client.exceptions.InvalidNextTokenException
    ConfigService.Client.exceptions.InvalidParameterValueException
    
    """
    pass

def describe_remediation_execution_status(ConfigRuleName=None, ResourceKeys=None, Limit=None, NextToken=None):
    """
    Provides a detailed view of a Remediation Execution for a set of resources including state, timestamps for when steps for the remediation execution occur, and any error messages for steps that have failed. When you specify the limit and the next token, you receive a paginated response.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_remediation_execution_status(
        ConfigRuleName='string',
        ResourceKeys=[
            {
                'resourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::EC2::RegisteredHAInstance'|'AWS::EC2::NatGateway'|'AWS::EC2::EgressOnlyInternetGateway'|'AWS::EC2::VPCEndpoint'|'AWS::EC2::VPCEndpointService'|'AWS::EC2::FlowLog'|'AWS::EC2::VPCPeeringConnection'|'AWS::Elasticsearch::Domain'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::DBCluster'|'AWS::RDS::DBClusterSnapshot'|'AWS::RDS::EventSubscription'|'AWS::S3::Bucket'|'AWS::S3::AccountPublicAccessBlock'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::SSM::ManagedInstanceInventory'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::DynamoDB::Table'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::RuleGroup'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::RuleGroup'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::WAFv2::WebACL'|'AWS::WAFv2::RuleGroup'|'AWS::WAFv2::IPSet'|'AWS::WAFv2::RegexPatternSet'|'AWS::WAFv2::ManagedRuleSet'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::ApiGateway::Stage'|'AWS::ApiGateway::RestApi'|'AWS::ApiGatewayV2::Stage'|'AWS::ApiGatewayV2::Api'|'AWS::CodePipeline::Pipeline'|'AWS::ServiceCatalog::CloudFormationProvisionedProduct'|'AWS::ServiceCatalog::CloudFormationProduct'|'AWS::ServiceCatalog::Portfolio'|'AWS::SQS::Queue'|'AWS::KMS::Key'|'AWS::QLDB::Ledger',
                'resourceId': 'string'
            },
        ],
        Limit=123,
        NextToken='string'
    )
    
    
    :type ConfigRuleName: string
    :param ConfigRuleName: [REQUIRED]\nA list of AWS Config rule names.\n

    :type ResourceKeys: list
    :param ResourceKeys: A list of resource keys to be processed with the current request. Each element in the list consists of the resource type and resource ID.\n\n(dict) --The details that identify a resource within AWS Config, including the resource type and resource ID.\n\nresourceType (string) -- [REQUIRED]The resource type.\n\nresourceId (string) -- [REQUIRED]The ID of the resource (for example., sg-xxxxxx).\n\n\n\n\n

    :type Limit: integer
    :param Limit: The maximum number of RemediationExecutionStatuses returned on each page. The default is maximum. If you specify 0, AWS Config uses the default.

    :type NextToken: string
    :param NextToken: The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.

    :rtype: dict

ReturnsResponse Syntax
{
    'RemediationExecutionStatuses': [
        {
            'ResourceKey': {
                'resourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::EC2::RegisteredHAInstance'|'AWS::EC2::NatGateway'|'AWS::EC2::EgressOnlyInternetGateway'|'AWS::EC2::VPCEndpoint'|'AWS::EC2::VPCEndpointService'|'AWS::EC2::FlowLog'|'AWS::EC2::VPCPeeringConnection'|'AWS::Elasticsearch::Domain'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::DBCluster'|'AWS::RDS::DBClusterSnapshot'|'AWS::RDS::EventSubscription'|'AWS::S3::Bucket'|'AWS::S3::AccountPublicAccessBlock'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::SSM::ManagedInstanceInventory'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::DynamoDB::Table'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::RuleGroup'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::RuleGroup'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::WAFv2::WebACL'|'AWS::WAFv2::RuleGroup'|'AWS::WAFv2::IPSet'|'AWS::WAFv2::RegexPatternSet'|'AWS::WAFv2::ManagedRuleSet'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::ApiGateway::Stage'|'AWS::ApiGateway::RestApi'|'AWS::ApiGatewayV2::Stage'|'AWS::ApiGatewayV2::Api'|'AWS::CodePipeline::Pipeline'|'AWS::ServiceCatalog::CloudFormationProvisionedProduct'|'AWS::ServiceCatalog::CloudFormationProduct'|'AWS::ServiceCatalog::Portfolio'|'AWS::SQS::Queue'|'AWS::KMS::Key'|'AWS::QLDB::Ledger',
                'resourceId': 'string'
            },
            'State': 'QUEUED'|'IN_PROGRESS'|'SUCCEEDED'|'FAILED',
            'StepDetails': [
                {
                    'Name': 'string',
                    'State': 'SUCCEEDED'|'PENDING'|'FAILED',
                    'ErrorMessage': 'string',
                    'StartTime': datetime(2015, 1, 1),
                    'StopTime': datetime(2015, 1, 1)
                },
            ],
            'InvocationTime': datetime(2015, 1, 1),
            'LastUpdatedTime': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

RemediationExecutionStatuses (list) --
Returns a list of remediation execution statuses objects.

(dict) --
Provides details of the current status of the invoked remediation action for that resource.

ResourceKey (dict) --
The details that identify a resource within AWS Config, including the resource type and resource ID.

resourceType (string) --
The resource type.

resourceId (string) --
The ID of the resource (for example., sg-xxxxxx).



State (string) --
ENUM of the values.

StepDetails (list) --
Details of every step.

(dict) --
Name of the step from the SSM document.

Name (string) --
The details of the step.

State (string) --
The valid status of the step.

ErrorMessage (string) --
An error message if the step was interrupted during execution.

StartTime (datetime) --
The time when the step started.

StopTime (datetime) --
The time when the step stopped.





InvocationTime (datetime) --
Start time when the remediation was executed.

LastUpdatedTime (datetime) --
The time when the remediation execution was last updated.





NextToken (string) --
The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.







Exceptions

ConfigService.Client.exceptions.NoSuchRemediationConfigurationException
ConfigService.Client.exceptions.InvalidNextTokenException


    :return: {
        'RemediationExecutionStatuses': [
            {
                'ResourceKey': {
                    'resourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::EC2::RegisteredHAInstance'|'AWS::EC2::NatGateway'|'AWS::EC2::EgressOnlyInternetGateway'|'AWS::EC2::VPCEndpoint'|'AWS::EC2::VPCEndpointService'|'AWS::EC2::FlowLog'|'AWS::EC2::VPCPeeringConnection'|'AWS::Elasticsearch::Domain'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::DBCluster'|'AWS::RDS::DBClusterSnapshot'|'AWS::RDS::EventSubscription'|'AWS::S3::Bucket'|'AWS::S3::AccountPublicAccessBlock'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::SSM::ManagedInstanceInventory'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::DynamoDB::Table'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::RuleGroup'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::RuleGroup'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::WAFv2::WebACL'|'AWS::WAFv2::RuleGroup'|'AWS::WAFv2::IPSet'|'AWS::WAFv2::RegexPatternSet'|'AWS::WAFv2::ManagedRuleSet'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::ApiGateway::Stage'|'AWS::ApiGateway::RestApi'|'AWS::ApiGatewayV2::Stage'|'AWS::ApiGatewayV2::Api'|'AWS::CodePipeline::Pipeline'|'AWS::ServiceCatalog::CloudFormationProvisionedProduct'|'AWS::ServiceCatalog::CloudFormationProduct'|'AWS::ServiceCatalog::Portfolio'|'AWS::SQS::Queue'|'AWS::KMS::Key'|'AWS::QLDB::Ledger',
                    'resourceId': 'string'
                },
                'State': 'QUEUED'|'IN_PROGRESS'|'SUCCEEDED'|'FAILED',
                'StepDetails': [
                    {
                        'Name': 'string',
                        'State': 'SUCCEEDED'|'PENDING'|'FAILED',
                        'ErrorMessage': 'string',
                        'StartTime': datetime(2015, 1, 1),
                        'StopTime': datetime(2015, 1, 1)
                    },
                ],
                'InvocationTime': datetime(2015, 1, 1),
                'LastUpdatedTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    ConfigService.Client.exceptions.NoSuchRemediationConfigurationException
    ConfigService.Client.exceptions.InvalidNextTokenException
    
    """
    pass

def describe_retention_configurations(RetentionConfigurationNames=None, NextToken=None):
    """
    Returns the details of one or more retention configurations. If the retention configuration name is not specified, this action returns the details for all the retention configurations for that account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_retention_configurations(
        RetentionConfigurationNames=[
            'string',
        ],
        NextToken='string'
    )
    
    
    :type RetentionConfigurationNames: list
    :param RetentionConfigurationNames: A list of names of retention configurations for which you want details. If you do not specify a name, AWS Config returns details for all the retention configurations for that account.\n\nNote\nCurrently, AWS Config supports only one retention configuration per region in your account.\n\n\n(string) --\n\n

    :type NextToken: string
    :param NextToken: The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.

    :rtype: dict

ReturnsResponse Syntax
{
    'RetentionConfigurations': [
        {
            'Name': 'string',
            'RetentionPeriodInDays': 123
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

RetentionConfigurations (list) --
Returns a retention configuration object.

(dict) --
An object with the name of the retention configuration and the retention period in days. The object stores the configuration for data retention in AWS Config.

Name (string) --
The name of the retention configuration object.

RetentionPeriodInDays (integer) --
Number of days AWS Config stores your historical information.

Note
Currently, only applicable to the configuration item history.






NextToken (string) --
The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.







Exceptions

ConfigService.Client.exceptions.InvalidParameterValueException
ConfigService.Client.exceptions.NoSuchRetentionConfigurationException
ConfigService.Client.exceptions.InvalidNextTokenException


    :return: {
        'RetentionConfigurations': [
            {
                'Name': 'string',
                'RetentionPeriodInDays': 123
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    ConfigService.Client.exceptions.InvalidParameterValueException
    ConfigService.Client.exceptions.NoSuchRetentionConfigurationException
    ConfigService.Client.exceptions.InvalidNextTokenException
    
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

def get_aggregate_compliance_details_by_config_rule(ConfigurationAggregatorName=None, ConfigRuleName=None, AccountId=None, AwsRegion=None, ComplianceType=None, Limit=None, NextToken=None):
    """
    Returns the evaluation results for the specified AWS Config rule for a specific resource in a rule. The results indicate which AWS resources were evaluated by the rule, when each resource was last evaluated, and whether each resource complies with the rule.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param ConfigurationAggregatorName: [REQUIRED]\nThe name of the configuration aggregator.\n

    :type ConfigRuleName: string
    :param ConfigRuleName: [REQUIRED]\nThe name of the AWS Config rule for which you want compliance information.\n

    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe 12-digit account ID of the source account.\n

    :type AwsRegion: string
    :param AwsRegion: [REQUIRED]\nThe source region from where the data is aggregated.\n

    :type ComplianceType: string
    :param ComplianceType: The resource compliance status.\n\nNote\nFor the GetAggregateComplianceDetailsByConfigRuleRequest data type, AWS Config supports only the COMPLIANT and NON_COMPLIANT . AWS Config does not support the NOT_APPLICABLE and INSUFFICIENT_DATA values.\n\n

    :type Limit: integer
    :param Limit: The maximum number of evaluation results returned on each page. The default is 50. You cannot specify a number greater than 100. If you specify 0, AWS Config uses the default.

    :type NextToken: string
    :param NextToken: The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

AggregateEvaluationResults (list) --
Returns an AggregateEvaluationResults object.

(dict) --
The details of an AWS Config evaluation for an account ID and region in an aggregator. Provides the AWS resource that was evaluated, the compliance of the resource, related time stamps, and supplementary information.

EvaluationResultIdentifier (dict) --
Uniquely identifies the evaluation result.

EvaluationResultQualifier (dict) --
Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type and ID of the evaluated resource.

ConfigRuleName (string) --
The name of the AWS Config rule that was used in the evaluation.

ResourceType (string) --
The type of AWS resource that was evaluated.

ResourceId (string) --
The ID of the evaluated AWS resource.



OrderingTimestamp (datetime) --
The time of the event that triggered the evaluation of your AWS resources. The time can indicate when AWS Config delivered a configuration item change notification, or it can indicate when AWS Config delivered the configuration snapshot, depending on which event triggered the evaluation.



ComplianceType (string) --
The resource compliance status.
For the AggregationEvaluationResult data type, AWS Config supports only the COMPLIANT and NON_COMPLIANT . AWS Config does not support the NOT_APPLICABLE and INSUFFICIENT_DATA value.

ResultRecordedTime (datetime) --
The time when AWS Config recorded the aggregate evaluation result.

ConfigRuleInvokedTime (datetime) --
The time when the AWS Config rule evaluated the AWS resource.

Annotation (string) --
Supplementary information about how the agrregate evaluation determined the compliance.

AccountId (string) --
The 12-digit account ID of the source account.

AwsRegion (string) --
The source region from where the data is aggregated.





NextToken (string) --
The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.







Exceptions

ConfigService.Client.exceptions.ValidationException
ConfigService.Client.exceptions.InvalidLimitException
ConfigService.Client.exceptions.InvalidNextTokenException
ConfigService.Client.exceptions.NoSuchConfigurationAggregatorException


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
    
    
    :returns: 
    ConfigService.Client.exceptions.ValidationException
    ConfigService.Client.exceptions.InvalidLimitException
    ConfigService.Client.exceptions.InvalidNextTokenException
    ConfigService.Client.exceptions.NoSuchConfigurationAggregatorException
    
    """
    pass

def get_aggregate_config_rule_compliance_summary(ConfigurationAggregatorName=None, Filters=None, GroupByKey=None, Limit=None, NextToken=None):
    """
    Returns the number of compliant and noncompliant rules for one or more accounts and regions in an aggregator.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param ConfigurationAggregatorName: [REQUIRED]\nThe name of the configuration aggregator.\n

    :type Filters: dict
    :param Filters: Filters the results based on the ConfigRuleComplianceSummaryFilters object.\n\nAccountId (string) --The 12-digit account ID of the source account.\n\nAwsRegion (string) --The source region where the data is aggregated.\n\n\n

    :type GroupByKey: string
    :param GroupByKey: Groups the result based on ACCOUNT_ID or AWS_REGION.

    :type Limit: integer
    :param Limit: The maximum number of evaluation results returned on each page. The default is 1000. You cannot specify a number greater than 1000. If you specify 0, AWS Config uses the default.

    :type NextToken: string
    :param NextToken: The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

GroupByKey (string) --
Groups the result based on ACCOUNT_ID or AWS_REGION.

AggregateComplianceCounts (list) --
Returns a list of AggregateComplianceCounts object.

(dict) --
Returns the number of compliant and noncompliant rules for one or more accounts and regions in an aggregator.

GroupName (string) --
The 12-digit account ID or region based on the GroupByKey value.

ComplianceSummary (dict) --
The number of compliant and noncompliant AWS Config rules.

CompliantResourceCount (dict) --
The number of AWS Config rules or AWS resources that are compliant, up to a maximum of 25 for rules and 100 for resources.

CappedCount (integer) --
The number of AWS resources or AWS Config rules responsible for the current compliance of the item.

CapExceeded (boolean) --
Indicates whether the maximum count is reached.



NonCompliantResourceCount (dict) --
The number of AWS Config rules or AWS resources that are noncompliant, up to a maximum of 25 for rules and 100 for resources.

CappedCount (integer) --
The number of AWS resources or AWS Config rules responsible for the current compliance of the item.

CapExceeded (boolean) --
Indicates whether the maximum count is reached.



ComplianceSummaryTimestamp (datetime) --
The time that AWS Config created the compliance summary.







NextToken (string) --
The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.







Exceptions

ConfigService.Client.exceptions.ValidationException
ConfigService.Client.exceptions.InvalidLimitException
ConfigService.Client.exceptions.InvalidNextTokenException
ConfigService.Client.exceptions.NoSuchConfigurationAggregatorException


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
    
    
    :returns: 
    ConfigService.Client.exceptions.ValidationException
    ConfigService.Client.exceptions.InvalidLimitException
    ConfigService.Client.exceptions.InvalidNextTokenException
    ConfigService.Client.exceptions.NoSuchConfigurationAggregatorException
    
    """
    pass

def get_aggregate_discovered_resource_counts(ConfigurationAggregatorName=None, Filters=None, GroupByKey=None, Limit=None, NextToken=None):
    """
    Returns the resource counts across accounts and regions that are present in your AWS Config aggregator. You can request the resource counts by providing filters and GroupByKey.
    For example, if the input contains accountID 12345678910 and region us-east-1 in filters, the API returns the count of resources in account ID 12345678910 and region us-east-1. If the input contains ACCOUNT_ID as a GroupByKey, the API returns resource counts for all source accounts that are present in your aggregator.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_aggregate_discovered_resource_counts(
        ConfigurationAggregatorName='string',
        Filters={
            'ResourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::EC2::RegisteredHAInstance'|'AWS::EC2::NatGateway'|'AWS::EC2::EgressOnlyInternetGateway'|'AWS::EC2::VPCEndpoint'|'AWS::EC2::VPCEndpointService'|'AWS::EC2::FlowLog'|'AWS::EC2::VPCPeeringConnection'|'AWS::Elasticsearch::Domain'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::DBCluster'|'AWS::RDS::DBClusterSnapshot'|'AWS::RDS::EventSubscription'|'AWS::S3::Bucket'|'AWS::S3::AccountPublicAccessBlock'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::SSM::ManagedInstanceInventory'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::DynamoDB::Table'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::RuleGroup'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::RuleGroup'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::WAFv2::WebACL'|'AWS::WAFv2::RuleGroup'|'AWS::WAFv2::IPSet'|'AWS::WAFv2::RegexPatternSet'|'AWS::WAFv2::ManagedRuleSet'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::ApiGateway::Stage'|'AWS::ApiGateway::RestApi'|'AWS::ApiGatewayV2::Stage'|'AWS::ApiGatewayV2::Api'|'AWS::CodePipeline::Pipeline'|'AWS::ServiceCatalog::CloudFormationProvisionedProduct'|'AWS::ServiceCatalog::CloudFormationProduct'|'AWS::ServiceCatalog::Portfolio'|'AWS::SQS::Queue'|'AWS::KMS::Key'|'AWS::QLDB::Ledger',
            'AccountId': 'string',
            'Region': 'string'
        },
        GroupByKey='RESOURCE_TYPE'|'ACCOUNT_ID'|'AWS_REGION',
        Limit=123,
        NextToken='string'
    )
    
    
    :type ConfigurationAggregatorName: string
    :param ConfigurationAggregatorName: [REQUIRED]\nThe name of the configuration aggregator.\n

    :type Filters: dict
    :param Filters: Filters the results based on the ResourceCountFilters object.\n\nResourceType (string) --The type of the AWS resource.\n\nAccountId (string) --The 12-digit ID of the account.\n\nRegion (string) --The region where the account is located.\n\n\n

    :type GroupByKey: string
    :param GroupByKey: The key to group the resource counts.

    :type Limit: integer
    :param Limit: The maximum number of GroupedResourceCount objects returned on each page. The default is 1000. You cannot specify a number greater than 1000. If you specify 0, AWS Config uses the default.

    :type NextToken: string
    :param NextToken: The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.

    :rtype: dict

ReturnsResponse Syntax
{
    'TotalDiscoveredResources': 123,
    'GroupByKey': 'string',
    'GroupedResourceCounts': [
        {
            'GroupName': 'string',
            'ResourceCount': 123
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

TotalDiscoveredResources (integer) --
The total number of resources that are present in an aggregator with the filters that you provide.

GroupByKey (string) --
The key passed into the request object. If GroupByKey is not provided, the result will be empty.

GroupedResourceCounts (list) --
Returns a list of GroupedResourceCount objects.

(dict) --
The count of resources that are grouped by the group name.

GroupName (string) --
The name of the group that can be region, account ID, or resource type. For example, region1, region2 if the region was chosen as GroupByKey .

ResourceCount (integer) --
The number of resources in the group.





NextToken (string) --
The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.







Exceptions

ConfigService.Client.exceptions.ValidationException
ConfigService.Client.exceptions.InvalidLimitException
ConfigService.Client.exceptions.InvalidNextTokenException
ConfigService.Client.exceptions.NoSuchConfigurationAggregatorException


    :return: {
        'TotalDiscoveredResources': 123,
        'GroupByKey': 'string',
        'GroupedResourceCounts': [
            {
                'GroupName': 'string',
                'ResourceCount': 123
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    ConfigService.Client.exceptions.ValidationException
    ConfigService.Client.exceptions.InvalidLimitException
    ConfigService.Client.exceptions.InvalidNextTokenException
    ConfigService.Client.exceptions.NoSuchConfigurationAggregatorException
    
    """
    pass

def get_aggregate_resource_config(ConfigurationAggregatorName=None, ResourceIdentifier=None):
    """
    Returns configuration item that is aggregated for your specific resource in a specific source account and region.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_aggregate_resource_config(
        ConfigurationAggregatorName='string',
        ResourceIdentifier={
            'SourceAccountId': 'string',
            'SourceRegion': 'string',
            'ResourceId': 'string',
            'ResourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::EC2::RegisteredHAInstance'|'AWS::EC2::NatGateway'|'AWS::EC2::EgressOnlyInternetGateway'|'AWS::EC2::VPCEndpoint'|'AWS::EC2::VPCEndpointService'|'AWS::EC2::FlowLog'|'AWS::EC2::VPCPeeringConnection'|'AWS::Elasticsearch::Domain'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::DBCluster'|'AWS::RDS::DBClusterSnapshot'|'AWS::RDS::EventSubscription'|'AWS::S3::Bucket'|'AWS::S3::AccountPublicAccessBlock'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::SSM::ManagedInstanceInventory'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::DynamoDB::Table'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::RuleGroup'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::RuleGroup'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::WAFv2::WebACL'|'AWS::WAFv2::RuleGroup'|'AWS::WAFv2::IPSet'|'AWS::WAFv2::RegexPatternSet'|'AWS::WAFv2::ManagedRuleSet'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::ApiGateway::Stage'|'AWS::ApiGateway::RestApi'|'AWS::ApiGatewayV2::Stage'|'AWS::ApiGatewayV2::Api'|'AWS::CodePipeline::Pipeline'|'AWS::ServiceCatalog::CloudFormationProvisionedProduct'|'AWS::ServiceCatalog::CloudFormationProduct'|'AWS::ServiceCatalog::Portfolio'|'AWS::SQS::Queue'|'AWS::KMS::Key'|'AWS::QLDB::Ledger',
            'ResourceName': 'string'
        }
    )
    
    
    :type ConfigurationAggregatorName: string
    :param ConfigurationAggregatorName: [REQUIRED]\nThe name of the configuration aggregator.\n

    :type ResourceIdentifier: dict
    :param ResourceIdentifier: [REQUIRED]\nAn object that identifies aggregate resource.\n\nSourceAccountId (string) -- [REQUIRED]The 12-digit account ID of the source account.\n\nSourceRegion (string) -- [REQUIRED]The source region where data is aggregated.\n\nResourceId (string) -- [REQUIRED]The ID of the AWS resource.\n\nResourceType (string) -- [REQUIRED]The type of the AWS resource.\n\nResourceName (string) --The name of the AWS resource.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ConfigurationItem': {
        'version': 'string',
        'accountId': 'string',
        'configurationItemCaptureTime': datetime(2015, 1, 1),
        'configurationItemStatus': 'OK'|'ResourceDiscovered'|'ResourceNotRecorded'|'ResourceDeleted'|'ResourceDeletedNotRecorded',
        'configurationStateId': 'string',
        'configurationItemMD5Hash': 'string',
        'arn': 'string',
        'resourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::EC2::RegisteredHAInstance'|'AWS::EC2::NatGateway'|'AWS::EC2::EgressOnlyInternetGateway'|'AWS::EC2::VPCEndpoint'|'AWS::EC2::VPCEndpointService'|'AWS::EC2::FlowLog'|'AWS::EC2::VPCPeeringConnection'|'AWS::Elasticsearch::Domain'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::DBCluster'|'AWS::RDS::DBClusterSnapshot'|'AWS::RDS::EventSubscription'|'AWS::S3::Bucket'|'AWS::S3::AccountPublicAccessBlock'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::SSM::ManagedInstanceInventory'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::DynamoDB::Table'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::RuleGroup'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::RuleGroup'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::WAFv2::WebACL'|'AWS::WAFv2::RuleGroup'|'AWS::WAFv2::IPSet'|'AWS::WAFv2::RegexPatternSet'|'AWS::WAFv2::ManagedRuleSet'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::ApiGateway::Stage'|'AWS::ApiGateway::RestApi'|'AWS::ApiGatewayV2::Stage'|'AWS::ApiGatewayV2::Api'|'AWS::CodePipeline::Pipeline'|'AWS::ServiceCatalog::CloudFormationProvisionedProduct'|'AWS::ServiceCatalog::CloudFormationProduct'|'AWS::ServiceCatalog::Portfolio'|'AWS::SQS::Queue'|'AWS::KMS::Key'|'AWS::QLDB::Ledger',
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
                'resourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::EC2::RegisteredHAInstance'|'AWS::EC2::NatGateway'|'AWS::EC2::EgressOnlyInternetGateway'|'AWS::EC2::VPCEndpoint'|'AWS::EC2::VPCEndpointService'|'AWS::EC2::FlowLog'|'AWS::EC2::VPCPeeringConnection'|'AWS::Elasticsearch::Domain'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::DBCluster'|'AWS::RDS::DBClusterSnapshot'|'AWS::RDS::EventSubscription'|'AWS::S3::Bucket'|'AWS::S3::AccountPublicAccessBlock'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::SSM::ManagedInstanceInventory'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::DynamoDB::Table'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::RuleGroup'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::RuleGroup'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::WAFv2::WebACL'|'AWS::WAFv2::RuleGroup'|'AWS::WAFv2::IPSet'|'AWS::WAFv2::RegexPatternSet'|'AWS::WAFv2::ManagedRuleSet'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::ApiGateway::Stage'|'AWS::ApiGateway::RestApi'|'AWS::ApiGatewayV2::Stage'|'AWS::ApiGatewayV2::Api'|'AWS::CodePipeline::Pipeline'|'AWS::ServiceCatalog::CloudFormationProvisionedProduct'|'AWS::ServiceCatalog::CloudFormationProduct'|'AWS::ServiceCatalog::Portfolio'|'AWS::SQS::Queue'|'AWS::KMS::Key'|'AWS::QLDB::Ledger',
                'resourceId': 'string',
                'resourceName': 'string',
                'relationshipName': 'string'
            },
        ],
        'configuration': 'string',
        'supplementaryConfiguration': {
            'string': 'string'
        }
    }
}


Response Structure

(dict) --

ConfigurationItem (dict) --
Returns a ConfigurationItem object.

version (string) --
The version number of the resource configuration.

accountId (string) --
The 12-digit AWS account ID associated with the resource.

configurationItemCaptureTime (datetime) --
The time when the configuration recording was initiated.

configurationItemStatus (string) --
The configuration item status.

configurationStateId (string) --
An identifier that indicates the ordering of the configuration items of a resource.

configurationItemMD5Hash (string) --
Unique MD5 hash that represents the configuration item\'s state.
You can use MD5 hash to compare the states of two or more configuration items that are associated with the same resource.

arn (string) --
accoun

resourceType (string) --
The type of AWS resource.

resourceId (string) --
The ID of the resource (for example, sg-xxxxxx ).

resourceName (string) --
The custom name of the resource, if available.

awsRegion (string) --
The region where the resource resides.

availabilityZone (string) --
The Availability Zone associated with the resource.

resourceCreationTime (datetime) --
The time stamp when the resource was created.

tags (dict) --
A mapping of key value tags associated with the resource.

(string) --
(string) --




relatedEvents (list) --
A list of CloudTrail event IDs.
A populated field indicates that the current configuration was initiated by the events recorded in the CloudTrail log. For more information about CloudTrail, see What Is AWS CloudTrail .
An empty field indicates that the current configuration was not initiated by any event. As of Version 1.3, the relatedEvents field is empty. You can access the LookupEvents API in the AWS CloudTrail API Reference to retrieve the events for the resource.

(string) --


relationships (list) --
A list of related AWS resources.

(dict) --
The relationship of the related resource to the main resource.

resourceType (string) --
The resource type of the related resource.

resourceId (string) --
The ID of the related resource (for example, sg-xxxxxx ).

resourceName (string) --
The custom name of the related resource, if available.

relationshipName (string) --
The type of relationship with the related resource.





configuration (string) --
The description of the resource configuration.

supplementaryConfiguration (dict) --
Configuration attributes that AWS Config returns for certain resource types to supplement the information returned for the configuration parameter.

(string) --
(string) --












Exceptions

ConfigService.Client.exceptions.ValidationException
ConfigService.Client.exceptions.NoSuchConfigurationAggregatorException
ConfigService.Client.exceptions.OversizedConfigurationItemException
ConfigService.Client.exceptions.ResourceNotDiscoveredException


    :return: {
        'ConfigurationItem': {
            'version': 'string',
            'accountId': 'string',
            'configurationItemCaptureTime': datetime(2015, 1, 1),
            'configurationItemStatus': 'OK'|'ResourceDiscovered'|'ResourceNotRecorded'|'ResourceDeleted'|'ResourceDeletedNotRecorded',
            'configurationStateId': 'string',
            'configurationItemMD5Hash': 'string',
            'arn': 'string',
            'resourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::EC2::RegisteredHAInstance'|'AWS::EC2::NatGateway'|'AWS::EC2::EgressOnlyInternetGateway'|'AWS::EC2::VPCEndpoint'|'AWS::EC2::VPCEndpointService'|'AWS::EC2::FlowLog'|'AWS::EC2::VPCPeeringConnection'|'AWS::Elasticsearch::Domain'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::DBCluster'|'AWS::RDS::DBClusterSnapshot'|'AWS::RDS::EventSubscription'|'AWS::S3::Bucket'|'AWS::S3::AccountPublicAccessBlock'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::SSM::ManagedInstanceInventory'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::DynamoDB::Table'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::RuleGroup'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::RuleGroup'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::WAFv2::WebACL'|'AWS::WAFv2::RuleGroup'|'AWS::WAFv2::IPSet'|'AWS::WAFv2::RegexPatternSet'|'AWS::WAFv2::ManagedRuleSet'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::ApiGateway::Stage'|'AWS::ApiGateway::RestApi'|'AWS::ApiGatewayV2::Stage'|'AWS::ApiGatewayV2::Api'|'AWS::CodePipeline::Pipeline'|'AWS::ServiceCatalog::CloudFormationProvisionedProduct'|'AWS::ServiceCatalog::CloudFormationProduct'|'AWS::ServiceCatalog::Portfolio'|'AWS::SQS::Queue'|'AWS::KMS::Key'|'AWS::QLDB::Ledger',
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
                    'resourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::EC2::RegisteredHAInstance'|'AWS::EC2::NatGateway'|'AWS::EC2::EgressOnlyInternetGateway'|'AWS::EC2::VPCEndpoint'|'AWS::EC2::VPCEndpointService'|'AWS::EC2::FlowLog'|'AWS::EC2::VPCPeeringConnection'|'AWS::Elasticsearch::Domain'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::DBCluster'|'AWS::RDS::DBClusterSnapshot'|'AWS::RDS::EventSubscription'|'AWS::S3::Bucket'|'AWS::S3::AccountPublicAccessBlock'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::SSM::ManagedInstanceInventory'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::DynamoDB::Table'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::RuleGroup'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::RuleGroup'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::WAFv2::WebACL'|'AWS::WAFv2::RuleGroup'|'AWS::WAFv2::IPSet'|'AWS::WAFv2::RegexPatternSet'|'AWS::WAFv2::ManagedRuleSet'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::ApiGateway::Stage'|'AWS::ApiGateway::RestApi'|'AWS::ApiGatewayV2::Stage'|'AWS::ApiGatewayV2::Api'|'AWS::CodePipeline::Pipeline'|'AWS::ServiceCatalog::CloudFormationProvisionedProduct'|'AWS::ServiceCatalog::CloudFormationProduct'|'AWS::ServiceCatalog::Portfolio'|'AWS::SQS::Queue'|'AWS::KMS::Key'|'AWS::QLDB::Ledger',
                    'resourceId': 'string',
                    'resourceName': 'string',
                    'relationshipName': 'string'
                },
            ],
            'configuration': 'string',
            'supplementaryConfiguration': {
                'string': 'string'
            }
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def get_compliance_details_by_config_rule(ConfigRuleName=None, ComplianceTypes=None, Limit=None, NextToken=None):
    """
    Returns the evaluation results for the specified AWS Config rule. The results indicate which AWS resources were evaluated by the rule, when each resource was last evaluated, and whether each resource complies with the rule.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_compliance_details_by_config_rule(
        ConfigRuleName='string',
        ComplianceTypes=[
            'COMPLIANT'|'NON_COMPLIANT'|'NOT_APPLICABLE'|'INSUFFICIENT_DATA',
        ],
        Limit=123,
        NextToken='string'
    )
    
    
    :type ConfigRuleName: string
    :param ConfigRuleName: [REQUIRED]\nThe name of the AWS Config rule for which you want compliance information.\n

    :type ComplianceTypes: list
    :param ComplianceTypes: Filters the results by compliance.\nThe allowed values are COMPLIANT , NON_COMPLIANT , and NOT_APPLICABLE .\n\n(string) --\n\n

    :type Limit: integer
    :param Limit: The maximum number of evaluation results returned on each page. The default is 10. You cannot specify a number greater than 100. If you specify 0, AWS Config uses the default.

    :type NextToken: string
    :param NextToken: The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

EvaluationResults (list) --
Indicates whether the AWS resource complies with the specified AWS Config rule.

(dict) --
The details of an AWS Config evaluation. Provides the AWS resource that was evaluated, the compliance of the resource, related time stamps, and supplementary information.

EvaluationResultIdentifier (dict) --
Uniquely identifies the evaluation result.

EvaluationResultQualifier (dict) --
Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type and ID of the evaluated resource.

ConfigRuleName (string) --
The name of the AWS Config rule that was used in the evaluation.

ResourceType (string) --
The type of AWS resource that was evaluated.

ResourceId (string) --
The ID of the evaluated AWS resource.



OrderingTimestamp (datetime) --
The time of the event that triggered the evaluation of your AWS resources. The time can indicate when AWS Config delivered a configuration item change notification, or it can indicate when AWS Config delivered the configuration snapshot, depending on which event triggered the evaluation.



ComplianceType (string) --
Indicates whether the AWS resource complies with the AWS Config rule that evaluated it.
For the EvaluationResult data type, AWS Config supports only the COMPLIANT , NON_COMPLIANT , and NOT_APPLICABLE values. AWS Config does not support the INSUFFICIENT_DATA value for the EvaluationResult data type.

ResultRecordedTime (datetime) --
The time when AWS Config recorded the evaluation result.

ConfigRuleInvokedTime (datetime) --
The time when the AWS Config rule evaluated the AWS resource.

Annotation (string) --
Supplementary information about how the evaluation determined the compliance.

ResultToken (string) --
An encrypted token that associates an evaluation with an AWS Config rule. The token identifies the rule, the AWS resource being evaluated, and the event that triggered the evaluation.





NextToken (string) --
The string that you use in a subsequent request to get the next page of results in a paginated response.







Exceptions

ConfigService.Client.exceptions.InvalidParameterValueException
ConfigService.Client.exceptions.InvalidNextTokenException
ConfigService.Client.exceptions.NoSuchConfigRuleException


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
    
    
    :returns: 
    ConfigService.Client.exceptions.InvalidParameterValueException
    ConfigService.Client.exceptions.InvalidNextTokenException
    ConfigService.Client.exceptions.NoSuchConfigRuleException
    
    """
    pass

def get_compliance_details_by_resource(ResourceType=None, ResourceId=None, ComplianceTypes=None, NextToken=None):
    """
    Returns the evaluation results for the specified AWS resource. The results indicate which AWS Config rules were used to evaluate the resource, when each rule was last used, and whether the resource complies with each rule.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_compliance_details_by_resource(
        ResourceType='string',
        ResourceId='string',
        ComplianceTypes=[
            'COMPLIANT'|'NON_COMPLIANT'|'NOT_APPLICABLE'|'INSUFFICIENT_DATA',
        ],
        NextToken='string'
    )
    
    
    :type ResourceType: string
    :param ResourceType: [REQUIRED]\nThe type of the AWS resource for which you want compliance information.\n

    :type ResourceId: string
    :param ResourceId: [REQUIRED]\nThe ID of the AWS resource for which you want compliance information.\n

    :type ComplianceTypes: list
    :param ComplianceTypes: Filters the results by compliance.\nThe allowed values are COMPLIANT , NON_COMPLIANT , and NOT_APPLICABLE .\n\n(string) --\n\n

    :type NextToken: string
    :param NextToken: The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

EvaluationResults (list) --
Indicates whether the specified AWS resource complies each AWS Config rule.

(dict) --
The details of an AWS Config evaluation. Provides the AWS resource that was evaluated, the compliance of the resource, related time stamps, and supplementary information.

EvaluationResultIdentifier (dict) --
Uniquely identifies the evaluation result.

EvaluationResultQualifier (dict) --
Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type and ID of the evaluated resource.

ConfigRuleName (string) --
The name of the AWS Config rule that was used in the evaluation.

ResourceType (string) --
The type of AWS resource that was evaluated.

ResourceId (string) --
The ID of the evaluated AWS resource.



OrderingTimestamp (datetime) --
The time of the event that triggered the evaluation of your AWS resources. The time can indicate when AWS Config delivered a configuration item change notification, or it can indicate when AWS Config delivered the configuration snapshot, depending on which event triggered the evaluation.



ComplianceType (string) --
Indicates whether the AWS resource complies with the AWS Config rule that evaluated it.
For the EvaluationResult data type, AWS Config supports only the COMPLIANT , NON_COMPLIANT , and NOT_APPLICABLE values. AWS Config does not support the INSUFFICIENT_DATA value for the EvaluationResult data type.

ResultRecordedTime (datetime) --
The time when AWS Config recorded the evaluation result.

ConfigRuleInvokedTime (datetime) --
The time when the AWS Config rule evaluated the AWS resource.

Annotation (string) --
Supplementary information about how the evaluation determined the compliance.

ResultToken (string) --
An encrypted token that associates an evaluation with an AWS Config rule. The token identifies the rule, the AWS resource being evaluated, and the event that triggered the evaluation.





NextToken (string) --
The string that you use in a subsequent request to get the next page of results in a paginated response.







Exceptions

ConfigService.Client.exceptions.InvalidParameterValueException


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
    
    
    :returns: 
    ConfigService.Client.exceptions.InvalidParameterValueException
    
    """
    pass

def get_compliance_summary_by_config_rule():
    """
    Returns the number of AWS Config rules that are compliant and noncompliant, up to a maximum of 25 for each.
    See also: AWS API Documentation
    
    
    :example: response = client.get_compliance_summary_by_config_rule()
    
    
    :rtype: dict
ReturnsResponse Syntax{
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


Response Structure

(dict) --
ComplianceSummary (dict) --The number of AWS Config rules that are compliant and the number that are noncompliant, up to a maximum of 25 for each.

CompliantResourceCount (dict) --The number of AWS Config rules or AWS resources that are compliant, up to a maximum of 25 for rules and 100 for resources.

CappedCount (integer) --The number of AWS resources or AWS Config rules responsible for the current compliance of the item.

CapExceeded (boolean) --Indicates whether the maximum count is reached.



NonCompliantResourceCount (dict) --The number of AWS Config rules or AWS resources that are noncompliant, up to a maximum of 25 for rules and 100 for resources.

CappedCount (integer) --The number of AWS resources or AWS Config rules responsible for the current compliance of the item.

CapExceeded (boolean) --Indicates whether the maximum count is reached.



ComplianceSummaryTimestamp (datetime) --The time that AWS Config created the compliance summary.









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
    
    Exceptions
    
    :example: response = client.get_compliance_summary_by_resource_type(
        ResourceTypes=[
            'string',
        ]
    )
    
    
    :type ResourceTypes: list
    :param ResourceTypes: Specify one or more resource types to get the number of resources that are compliant and the number that are noncompliant for each resource type.\nFor this request, you can specify an AWS resource type such as AWS::EC2::Instance . You can specify that the resource type is an AWS account by specifying AWS::::Account .\n\n(string) --\n\n

    :rtype: dict
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

(dict) --The number of AWS resources of a specific type that are compliant or noncompliant, up to a maximum of 100 for each.

ResourceType (string) --The type of AWS resource.

ComplianceSummary (dict) --The number of AWS resources that are compliant or noncompliant, up to a maximum of 100 for each.

CompliantResourceCount (dict) --The number of AWS Config rules or AWS resources that are compliant, up to a maximum of 25 for rules and 100 for resources.

CappedCount (integer) --The number of AWS resources or AWS Config rules responsible for the current compliance of the item.

CapExceeded (boolean) --Indicates whether the maximum count is reached.



NonCompliantResourceCount (dict) --The number of AWS Config rules or AWS resources that are noncompliant, up to a maximum of 25 for rules and 100 for resources.

CappedCount (integer) --The number of AWS resources or AWS Config rules responsible for the current compliance of the item.

CapExceeded (boolean) --Indicates whether the maximum count is reached.



ComplianceSummaryTimestamp (datetime) --The time that AWS Config created the compliance summary.












Exceptions

ConfigService.Client.exceptions.InvalidParameterValueException


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
    
    
    :returns: 
    ConfigService.Client.exceptions.InvalidParameterValueException
    
    """
    pass

def get_conformance_pack_compliance_details(ConformancePackName=None, Filters=None, Limit=None, NextToken=None):
    """
    Returns compliance details of a conformance pack for all AWS resources that are monitered by conformance pack.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_conformance_pack_compliance_details(
        ConformancePackName='string',
        Filters={
            'ConfigRuleNames': [
                'string',
            ],
            'ComplianceType': 'COMPLIANT'|'NON_COMPLIANT',
            'ResourceType': 'string',
            'ResourceIds': [
                'string',
            ]
        },
        Limit=123,
        NextToken='string'
    )
    
    
    :type ConformancePackName: string
    :param ConformancePackName: [REQUIRED]\nName of the conformance pack.\n

    :type Filters: dict
    :param Filters: A ConformancePackEvaluationFilters object.\n\nConfigRuleNames (list) --Filters the results by AWS Config rule names.\n\n(string) --\n\n\nComplianceType (string) --Filters the results by compliance.\nThe allowed values are COMPLIANT and NON_COMPLIANT .\n\nResourceType (string) --Filters the results by the resource type (for example, 'AWS::EC2::Instance' ).\n\nResourceIds (list) --Filters the results by resource IDs.\n\nNote\nThis is valid only when you provide resource type. If there is no resource type, you will see an error.\n\n\n(string) --\n\n\n\n

    :type Limit: integer
    :param Limit: The maximum number of evaluation results returned on each page. If you do no specify a number, AWS Config uses the default. The default is 100.

    :type NextToken: string
    :param NextToken: The nextToken string returned in a previous request that you use to request the next page of results in a paginated response.

    :rtype: dict

ReturnsResponse Syntax
{
    'ConformancePackName': 'string',
    'ConformancePackRuleEvaluationResults': [
        {
            'ComplianceType': 'COMPLIANT'|'NON_COMPLIANT',
            'EvaluationResultIdentifier': {
                'EvaluationResultQualifier': {
                    'ConfigRuleName': 'string',
                    'ResourceType': 'string',
                    'ResourceId': 'string'
                },
                'OrderingTimestamp': datetime(2015, 1, 1)
            },
            'ConfigRuleInvokedTime': datetime(2015, 1, 1),
            'ResultRecordedTime': datetime(2015, 1, 1),
            'Annotation': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

ConformancePackName (string) --
Name of the conformance pack.

ConformancePackRuleEvaluationResults (list) --
Returns a list of ConformancePackEvaluationResult objects.

(dict) --
The details of a conformance pack evaluation. Provides AWS Config rule and AWS resource type that was evaluated, the compliance of the conformance pack, related time stamps, and supplementary information.

ComplianceType (string) --
The compliance type. The allowed values are COMPLIANT and NON_COMPLIANT .

EvaluationResultIdentifier (dict) --
Uniquely identifies an evaluation result.

EvaluationResultQualifier (dict) --
Identifies an AWS Config rule used to evaluate an AWS resource, and provides the type and ID of the evaluated resource.

ConfigRuleName (string) --
The name of the AWS Config rule that was used in the evaluation.

ResourceType (string) --
The type of AWS resource that was evaluated.

ResourceId (string) --
The ID of the evaluated AWS resource.



OrderingTimestamp (datetime) --
The time of the event that triggered the evaluation of your AWS resources. The time can indicate when AWS Config delivered a configuration item change notification, or it can indicate when AWS Config delivered the configuration snapshot, depending on which event triggered the evaluation.



ConfigRuleInvokedTime (datetime) --
The time when AWS Config rule evaluated AWS resource.

ResultRecordedTime (datetime) --
The time when AWS Config recorded the evaluation result.

Annotation (string) --
Supplementary information about how the evaluation determined the compliance.





NextToken (string) --
The nextToken string returned in a previous request that you use to request the next page of results in a paginated response.







Exceptions

ConfigService.Client.exceptions.InvalidLimitException
ConfigService.Client.exceptions.InvalidNextTokenException
ConfigService.Client.exceptions.NoSuchConformancePackException
ConfigService.Client.exceptions.NoSuchConfigRuleInConformancePackException
ConfigService.Client.exceptions.InvalidParameterValueException


    :return: {
        'ConformancePackName': 'string',
        'ConformancePackRuleEvaluationResults': [
            {
                'ComplianceType': 'COMPLIANT'|'NON_COMPLIANT',
                'EvaluationResultIdentifier': {
                    'EvaluationResultQualifier': {
                        'ConfigRuleName': 'string',
                        'ResourceType': 'string',
                        'ResourceId': 'string'
                    },
                    'OrderingTimestamp': datetime(2015, 1, 1)
                },
                'ConfigRuleInvokedTime': datetime(2015, 1, 1),
                'ResultRecordedTime': datetime(2015, 1, 1),
                'Annotation': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    ConfigService.Client.exceptions.InvalidLimitException
    ConfigService.Client.exceptions.InvalidNextTokenException
    ConfigService.Client.exceptions.NoSuchConformancePackException
    ConfigService.Client.exceptions.NoSuchConfigRuleInConformancePackException
    ConfigService.Client.exceptions.InvalidParameterValueException
    
    """
    pass

def get_conformance_pack_compliance_summary(ConformancePackNames=None, Limit=None, NextToken=None):
    """
    Returns compliance details for the conformance pack based on the cumulative compliance results of all the rules in that conformance pack.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_conformance_pack_compliance_summary(
        ConformancePackNames=[
            'string',
        ],
        Limit=123,
        NextToken='string'
    )
    
    
    :type ConformancePackNames: list
    :param ConformancePackNames: [REQUIRED]\nNames of conformance packs.\n\n(string) --\n\n

    :type Limit: integer
    :param Limit: The maximum number of conformance packs returned on each page.

    :type NextToken: string
    :param NextToken: The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.

    :rtype: dict

ReturnsResponse Syntax
{
    'ConformancePackComplianceSummaryList': [
        {
            'ConformancePackName': 'string',
            'ConformancePackComplianceStatus': 'COMPLIANT'|'NON_COMPLIANT'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

ConformancePackComplianceSummaryList (list) --
A list of ConformancePackComplianceSummary objects.

(dict) --
Summary includes the name and status of the conformance pack.

ConformancePackName (string) --
The name of the conformance pack name.

ConformancePackComplianceStatus (string) --
The status of the conformance pack. The allowed values are COMPLIANT and NON_COMPLIANT.





NextToken (string) --
The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.







Exceptions

ConfigService.Client.exceptions.NoSuchConformancePackException
ConfigService.Client.exceptions.InvalidLimitException
ConfigService.Client.exceptions.InvalidNextTokenException


    :return: {
        'ConformancePackComplianceSummaryList': [
            {
                'ConformancePackName': 'string',
                'ConformancePackComplianceStatus': 'COMPLIANT'|'NON_COMPLIANT'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    ConfigService.Client.exceptions.NoSuchConformancePackException
    ConfigService.Client.exceptions.InvalidLimitException
    ConfigService.Client.exceptions.InvalidNextTokenException
    
    """
    pass

def get_discovered_resource_counts(resourceTypes=None, limit=None, nextToken=None):
    """
    Returns the resource types, the number of each resource type, and the total number of resources that AWS Config is recording in this region for your AWS account.
    The response is paginated. By default, AWS Config lists 100  ResourceCount objects on each page. You can customize this number with the limit parameter. The response includes a nextToken string. To get the next page of results, run the request again and specify the string for the nextToken parameter.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_discovered_resource_counts(
        resourceTypes=[
            'string',
        ],
        limit=123,
        nextToken='string'
    )
    
    
    :type resourceTypes: list
    :param resourceTypes: The comma-separated list that specifies the resource types that you want AWS Config to return (for example, 'AWS::EC2::Instance' , 'AWS::IAM::User' ).\nIf a value for resourceTypes is not specified, AWS Config returns all resource types that AWS Config is recording in the region for your account.\n\nNote\nIf the configuration recorder is turned off, AWS Config returns an empty list of ResourceCount objects. If the configuration recorder is not recording a specific resource type (for example, S3 buckets), that resource type is not returned in the list of ResourceCount objects.\n\n\n(string) --\n\n

    :type limit: integer
    :param limit: The maximum number of ResourceCount objects returned on each page. The default is 100. You cannot specify a number greater than 100. If you specify 0, AWS Config uses the default.

    :type nextToken: string
    :param nextToken: The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.

    :rtype: dict

ReturnsResponse Syntax
{
    'totalDiscoveredResources': 123,
    'resourceCounts': [
        {
            'resourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::EC2::RegisteredHAInstance'|'AWS::EC2::NatGateway'|'AWS::EC2::EgressOnlyInternetGateway'|'AWS::EC2::VPCEndpoint'|'AWS::EC2::VPCEndpointService'|'AWS::EC2::FlowLog'|'AWS::EC2::VPCPeeringConnection'|'AWS::Elasticsearch::Domain'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::DBCluster'|'AWS::RDS::DBClusterSnapshot'|'AWS::RDS::EventSubscription'|'AWS::S3::Bucket'|'AWS::S3::AccountPublicAccessBlock'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::SSM::ManagedInstanceInventory'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::DynamoDB::Table'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::RuleGroup'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::RuleGroup'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::WAFv2::WebACL'|'AWS::WAFv2::RuleGroup'|'AWS::WAFv2::IPSet'|'AWS::WAFv2::RegexPatternSet'|'AWS::WAFv2::ManagedRuleSet'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::ApiGateway::Stage'|'AWS::ApiGateway::RestApi'|'AWS::ApiGatewayV2::Stage'|'AWS::ApiGatewayV2::Api'|'AWS::CodePipeline::Pipeline'|'AWS::ServiceCatalog::CloudFormationProvisionedProduct'|'AWS::ServiceCatalog::CloudFormationProduct'|'AWS::ServiceCatalog::Portfolio'|'AWS::SQS::Queue'|'AWS::KMS::Key'|'AWS::QLDB::Ledger',
            'count': 123
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

totalDiscoveredResources (integer) --
The total number of resources that AWS Config is recording in the region for your account. If you specify resource types in the request, AWS Config returns only the total number of resources for those resource types.

Example


AWS Config is recording three resource types in the US East (Ohio) Region for your account: 25 EC2 instances, 20 IAM users, and 15 S3 buckets, for a total of 60 resources.
You make a call to the GetDiscoveredResourceCounts action and specify the resource type, "AWS::EC2::Instances" , in the request.
AWS Config returns 25 for totalDiscoveredResources .


resourceCounts (list) --
The list of ResourceCount objects. Each object is listed in descending order by the number of resources.

(dict) --
An object that contains the resource type and the number of resources.

resourceType (string) --
The resource type (for example, "AWS::EC2::Instance" ).

count (integer) --
The number of resources.





nextToken (string) --
The string that you use in a subsequent request to get the next page of results in a paginated response.







Exceptions

ConfigService.Client.exceptions.ValidationException
ConfigService.Client.exceptions.InvalidLimitException
ConfigService.Client.exceptions.InvalidNextTokenException


    :return: {
        'totalDiscoveredResources': 123,
        'resourceCounts': [
            {
                'resourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::EC2::RegisteredHAInstance'|'AWS::EC2::NatGateway'|'AWS::EC2::EgressOnlyInternetGateway'|'AWS::EC2::VPCEndpoint'|'AWS::EC2::VPCEndpointService'|'AWS::EC2::FlowLog'|'AWS::EC2::VPCPeeringConnection'|'AWS::Elasticsearch::Domain'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::DBCluster'|'AWS::RDS::DBClusterSnapshot'|'AWS::RDS::EventSubscription'|'AWS::S3::Bucket'|'AWS::S3::AccountPublicAccessBlock'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::SSM::ManagedInstanceInventory'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::DynamoDB::Table'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::RuleGroup'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::RuleGroup'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::WAFv2::WebACL'|'AWS::WAFv2::RuleGroup'|'AWS::WAFv2::IPSet'|'AWS::WAFv2::RegexPatternSet'|'AWS::WAFv2::ManagedRuleSet'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::ApiGateway::Stage'|'AWS::ApiGateway::RestApi'|'AWS::ApiGatewayV2::Stage'|'AWS::ApiGatewayV2::Api'|'AWS::CodePipeline::Pipeline'|'AWS::ServiceCatalog::CloudFormationProvisionedProduct'|'AWS::ServiceCatalog::CloudFormationProduct'|'AWS::ServiceCatalog::Portfolio'|'AWS::SQS::Queue'|'AWS::KMS::Key'|'AWS::QLDB::Ledger',
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

def get_organization_config_rule_detailed_status(OrganizationConfigRuleName=None, Filters=None, Limit=None, NextToken=None):
    """
    Returns detailed status for each member account within an organization for a given organization config rule.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_organization_config_rule_detailed_status(
        OrganizationConfigRuleName='string',
        Filters={
            'AccountId': 'string',
            'MemberAccountRuleStatus': 'CREATE_SUCCESSFUL'|'CREATE_IN_PROGRESS'|'CREATE_FAILED'|'DELETE_SUCCESSFUL'|'DELETE_FAILED'|'DELETE_IN_PROGRESS'|'UPDATE_SUCCESSFUL'|'UPDATE_IN_PROGRESS'|'UPDATE_FAILED'
        },
        Limit=123,
        NextToken='string'
    )
    
    
    :type OrganizationConfigRuleName: string
    :param OrganizationConfigRuleName: [REQUIRED]\nThe name of organization config rule for which you want status details for member accounts.\n

    :type Filters: dict
    :param Filters: A StatusDetailFilters object.\n\nAccountId (string) --The 12-digit account ID of the member account within an organization.\n\nMemberAccountRuleStatus (string) --Indicates deployment status for config rule in the member account. When master account calls PutOrganizationConfigRule action for the first time, config rule status is created in the member account. When master account calls PutOrganizationConfigRule action for the second time, config rule status is updated in the member account. Config rule status is deleted when the master account deletes OrganizationConfigRule and disables service access for config-multiaccountsetup.amazonaws.com .\nAWS Config sets the state of the rule to:\n\nCREATE_SUCCESSFUL when config rule has been created in the member account.\nCREATE_IN_PROGRESS when config rule is being created in the member account.\nCREATE_FAILED when config rule creation has failed in the member account.\nDELETE_FAILED when config rule deletion has failed in the member account.\nDELETE_IN_PROGRESS when config rule is being deleted in the member account.\nDELETE_SUCCESSFUL when config rule has been deleted in the member account.\nUPDATE_SUCCESSFUL when config rule has been updated in the member account.\nUPDATE_IN_PROGRESS when config rule is being updated in the member account.\nUPDATE_FAILED when config rule deletion has failed in the member account.\n\n\n\n

    :type Limit: integer
    :param Limit: The maximum number of OrganizationConfigRuleDetailedStatus returned on each page. If you do not specify a number, AWS Config uses the default. The default is 100.

    :type NextToken: string
    :param NextToken: The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.

    :rtype: dict

ReturnsResponse Syntax
{
    'OrganizationConfigRuleDetailedStatus': [
        {
            'AccountId': 'string',
            'ConfigRuleName': 'string',
            'MemberAccountRuleStatus': 'CREATE_SUCCESSFUL'|'CREATE_IN_PROGRESS'|'CREATE_FAILED'|'DELETE_SUCCESSFUL'|'DELETE_FAILED'|'DELETE_IN_PROGRESS'|'UPDATE_SUCCESSFUL'|'UPDATE_IN_PROGRESS'|'UPDATE_FAILED',
            'ErrorCode': 'string',
            'ErrorMessage': 'string',
            'LastUpdateTime': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

OrganizationConfigRuleDetailedStatus (list) --
A list of MemberAccountStatus objects.

(dict) --
Organization config rule creation or deletion status in each member account. This includes the name of the rule, the status, error code and error message when the rule creation or deletion failed.

AccountId (string) --
The 12-digit account ID of a member account.

ConfigRuleName (string) --
The name of config rule deployed in the member account.

MemberAccountRuleStatus (string) --
Indicates deployment status for config rule in the member account. When master account calls PutOrganizationConfigRule action for the first time, config rule status is created in the member account. When master account calls PutOrganizationConfigRule action for the second time, config rule status is updated in the member account. Config rule status is deleted when the master account deletes OrganizationConfigRule and disables service access for config-multiaccountsetup.amazonaws.com .
AWS Config sets the state of the rule to:

CREATE_SUCCESSFUL when config rule has been created in the member account.
CREATE_IN_PROGRESS when config rule is being created in the member account.
CREATE_FAILED when config rule creation has failed in the member account.
DELETE_FAILED when config rule deletion has failed in the member account.
DELETE_IN_PROGRESS when config rule is being deleted in the member account.
DELETE_SUCCESSFUL when config rule has been deleted in the member account.
UPDATE_SUCCESSFUL when config rule has been updated in the member account.
UPDATE_IN_PROGRESS when config rule is being updated in the member account.
UPDATE_FAILED when config rule deletion has failed in the member account.


ErrorCode (string) --
An error code that is returned when config rule creation or deletion failed in the member account.

ErrorMessage (string) --
An error message indicating that config rule account creation or deletion has failed due to an error in the member account.

LastUpdateTime (datetime) --
The timestamp of the last status update.





NextToken (string) --
The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.







Exceptions

ConfigService.Client.exceptions.NoSuchOrganizationConfigRuleException
ConfigService.Client.exceptions.InvalidLimitException
ConfigService.Client.exceptions.InvalidNextTokenException
ConfigService.Client.exceptions.OrganizationAccessDeniedException


    :return: {
        'OrganizationConfigRuleDetailedStatus': [
            {
                'AccountId': 'string',
                'ConfigRuleName': 'string',
                'MemberAccountRuleStatus': 'CREATE_SUCCESSFUL'|'CREATE_IN_PROGRESS'|'CREATE_FAILED'|'DELETE_SUCCESSFUL'|'DELETE_FAILED'|'DELETE_IN_PROGRESS'|'UPDATE_SUCCESSFUL'|'UPDATE_IN_PROGRESS'|'UPDATE_FAILED',
                'ErrorCode': 'string',
                'ErrorMessage': 'string',
                'LastUpdateTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    CREATE_SUCCESSFUL when config rule has been created in the member account.
    CREATE_IN_PROGRESS when config rule is being created in the member account.
    CREATE_FAILED when config rule creation has failed in the member account.
    DELETE_FAILED when config rule deletion has failed in the member account.
    DELETE_IN_PROGRESS when config rule is being deleted in the member account.
    DELETE_SUCCESSFUL when config rule has been deleted in the member account.
    UPDATE_SUCCESSFUL when config rule has been updated in the member account.
    UPDATE_IN_PROGRESS when config rule is being updated in the member account.
    UPDATE_FAILED when config rule deletion has failed in the member account.
    
    """
    pass

def get_organization_conformance_pack_detailed_status(OrganizationConformancePackName=None, Filters=None, Limit=None, NextToken=None):
    """
    Returns detailed status for each member account within an organization for a given organization conformance pack.
    Only a master account can call this API.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_organization_conformance_pack_detailed_status(
        OrganizationConformancePackName='string',
        Filters={
            'AccountId': 'string',
            'Status': 'CREATE_SUCCESSFUL'|'CREATE_IN_PROGRESS'|'CREATE_FAILED'|'DELETE_SUCCESSFUL'|'DELETE_FAILED'|'DELETE_IN_PROGRESS'|'UPDATE_SUCCESSFUL'|'UPDATE_IN_PROGRESS'|'UPDATE_FAILED'
        },
        Limit=123,
        NextToken='string'
    )
    
    
    :type OrganizationConformancePackName: string
    :param OrganizationConformancePackName: [REQUIRED]\nThe name of organization conformance pack for which you want status details for member accounts.\n

    :type Filters: dict
    :param Filters: An OrganizationResourceDetailedStatusFilters object.\n\nAccountId (string) --The 12-digit account ID of the member account within an organization.\n\nStatus (string) --Indicates deployment status for conformance pack in a member account. When master account calls PutOrganizationConformancePack action for the first time, conformance pack status is created in the member account. When master account calls PutOrganizationConformancePack action for the second time, conformance pack status is updated in the member account. Conformance pack status is deleted when the master account deletes OrganizationConformancePack and disables service access for config-multiaccountsetup.amazonaws.com .\nAWS Config sets the state of the conformance pack to:\n\nCREATE_SUCCESSFUL when conformance pack has been created in the member account.\nCREATE_IN_PROGRESS when conformance pack is being created in the member account.\nCREATE_FAILED when conformance pack creation has failed in the member account.\nDELETE_FAILED when conformance pack deletion has failed in the member account.\nDELETE_IN_PROGRESS when conformance pack is being deleted in the member account.\nDELETE_SUCCESSFUL when conformance pack has been deleted in the member account.\nUPDATE_SUCCESSFUL when conformance pack has been updated in the member account.\nUPDATE_IN_PROGRESS when conformance pack is being updated in the member account.\nUPDATE_FAILED when conformance pack deletion has failed in the member account.\n\n\n\n

    :type Limit: integer
    :param Limit: The maximum number of OrganizationConformancePackDetailedStatuses returned on each page. If you do not specify a number, AWS Config uses the default. The default is 100.

    :type NextToken: string
    :param NextToken: The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.

    :rtype: dict

ReturnsResponse Syntax
{
    'OrganizationConformancePackDetailedStatuses': [
        {
            'AccountId': 'string',
            'ConformancePackName': 'string',
            'Status': 'CREATE_SUCCESSFUL'|'CREATE_IN_PROGRESS'|'CREATE_FAILED'|'DELETE_SUCCESSFUL'|'DELETE_FAILED'|'DELETE_IN_PROGRESS'|'UPDATE_SUCCESSFUL'|'UPDATE_IN_PROGRESS'|'UPDATE_FAILED',
            'ErrorCode': 'string',
            'ErrorMessage': 'string',
            'LastUpdateTime': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

OrganizationConformancePackDetailedStatuses (list) --
A list of OrganizationConformancePackDetailedStatus objects.

(dict) --
Organization conformance pack creation or deletion status in each member account. This includes the name of the conformance pack, the status, error code and error message when the conformance pack creation or deletion failed.

AccountId (string) --
The 12-digit account ID of a member account.

ConformancePackName (string) --
The name of conformance pack deployed in the member account.

Status (string) --
Indicates deployment status for conformance pack in a member account. When master account calls PutOrganizationConformancePack action for the first time, conformance pack status is created in the member account. When master account calls PutOrganizationConformancePack action for the second time, conformance pack status is updated in the member account. Conformance pack status is deleted when the master account deletes OrganizationConformancePack and disables service access for config-multiaccountsetup.amazonaws.com .
AWS Config sets the state of the conformance pack to:

CREATE_SUCCESSFUL when conformance pack has been created in the member account.
CREATE_IN_PROGRESS when conformance pack is being created in the member account.
CREATE_FAILED when conformance pack creation has failed in the member account.
DELETE_FAILED when conformance pack deletion has failed in the member account.
DELETE_IN_PROGRESS when conformance pack is being deleted in the member account.
DELETE_SUCCESSFUL when conformance pack has been deleted in the member account.
UPDATE_SUCCESSFUL when conformance pack has been updated in the member account.
UPDATE_IN_PROGRESS when conformance pack is being updated in the member account.
UPDATE_FAILED when conformance pack deletion has failed in the member account.


ErrorCode (string) --
An error code that is returned when conformance pack creation or deletion failed in the member account.

ErrorMessage (string) --
An error message indicating that conformance pack account creation or deletion has failed due to an error in the member account.

LastUpdateTime (datetime) --
The timestamp of the last status update.





NextToken (string) --
The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.







Exceptions

ConfigService.Client.exceptions.NoSuchOrganizationConformancePackException
ConfigService.Client.exceptions.InvalidLimitException
ConfigService.Client.exceptions.InvalidNextTokenException
ConfigService.Client.exceptions.OrganizationAccessDeniedException


    :return: {
        'OrganizationConformancePackDetailedStatuses': [
            {
                'AccountId': 'string',
                'ConformancePackName': 'string',
                'Status': 'CREATE_SUCCESSFUL'|'CREATE_IN_PROGRESS'|'CREATE_FAILED'|'DELETE_SUCCESSFUL'|'DELETE_FAILED'|'DELETE_IN_PROGRESS'|'UPDATE_SUCCESSFUL'|'UPDATE_IN_PROGRESS'|'UPDATE_FAILED',
                'ErrorCode': 'string',
                'ErrorMessage': 'string',
                'LastUpdateTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    CREATE_SUCCESSFUL when conformance pack has been created in the member account.
    CREATE_IN_PROGRESS when conformance pack is being created in the member account.
    CREATE_FAILED when conformance pack creation has failed in the member account.
    DELETE_FAILED when conformance pack deletion has failed in the member account.
    DELETE_IN_PROGRESS when conformance pack is being deleted in the member account.
    DELETE_SUCCESSFUL when conformance pack has been deleted in the member account.
    UPDATE_SUCCESSFUL when conformance pack has been updated in the member account.
    UPDATE_IN_PROGRESS when conformance pack is being updated in the member account.
    UPDATE_FAILED when conformance pack deletion has failed in the member account.
    
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

def get_resource_config_history(resourceType=None, resourceId=None, laterTime=None, earlierTime=None, chronologicalOrder=None, limit=None, nextToken=None):
    """
    Returns a list of configuration items for the specified resource. The list contains details about each state of the resource during the specified time interval. If you specified a retention period to retain your ConfigurationItems between a minimum of 30 days and a maximum of 7 years (2557 days), AWS Config returns the ConfigurationItems for the specified retention period.
    The response is paginated. By default, AWS Config returns a limit of 10 configuration items per page. You can customize this number with the limit parameter. The response includes a nextToken string. To get the next page of results, run the request again and specify the string for the nextToken parameter.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_resource_config_history(
        resourceType='AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::EC2::RegisteredHAInstance'|'AWS::EC2::NatGateway'|'AWS::EC2::EgressOnlyInternetGateway'|'AWS::EC2::VPCEndpoint'|'AWS::EC2::VPCEndpointService'|'AWS::EC2::FlowLog'|'AWS::EC2::VPCPeeringConnection'|'AWS::Elasticsearch::Domain'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::DBCluster'|'AWS::RDS::DBClusterSnapshot'|'AWS::RDS::EventSubscription'|'AWS::S3::Bucket'|'AWS::S3::AccountPublicAccessBlock'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::SSM::ManagedInstanceInventory'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::DynamoDB::Table'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::RuleGroup'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::RuleGroup'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::WAFv2::WebACL'|'AWS::WAFv2::RuleGroup'|'AWS::WAFv2::IPSet'|'AWS::WAFv2::RegexPatternSet'|'AWS::WAFv2::ManagedRuleSet'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::ApiGateway::Stage'|'AWS::ApiGateway::RestApi'|'AWS::ApiGatewayV2::Stage'|'AWS::ApiGatewayV2::Api'|'AWS::CodePipeline::Pipeline'|'AWS::ServiceCatalog::CloudFormationProvisionedProduct'|'AWS::ServiceCatalog::CloudFormationProduct'|'AWS::ServiceCatalog::Portfolio'|'AWS::SQS::Queue'|'AWS::KMS::Key'|'AWS::QLDB::Ledger',
        resourceId='string',
        laterTime=datetime(2015, 1, 1),
        earlierTime=datetime(2015, 1, 1),
        chronologicalOrder='Reverse'|'Forward',
        limit=123,
        nextToken='string'
    )
    
    
    :type resourceType: string
    :param resourceType: [REQUIRED]\nThe resource type.\n

    :type resourceId: string
    :param resourceId: [REQUIRED]\nThe ID of the resource (for example., sg-xxxxxx ).\n

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

ReturnsResponse Syntax
{
    'configurationItems': [
        {
            'version': 'string',
            'accountId': 'string',
            'configurationItemCaptureTime': datetime(2015, 1, 1),
            'configurationItemStatus': 'OK'|'ResourceDiscovered'|'ResourceNotRecorded'|'ResourceDeleted'|'ResourceDeletedNotRecorded',
            'configurationStateId': 'string',
            'configurationItemMD5Hash': 'string',
            'arn': 'string',
            'resourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::EC2::RegisteredHAInstance'|'AWS::EC2::NatGateway'|'AWS::EC2::EgressOnlyInternetGateway'|'AWS::EC2::VPCEndpoint'|'AWS::EC2::VPCEndpointService'|'AWS::EC2::FlowLog'|'AWS::EC2::VPCPeeringConnection'|'AWS::Elasticsearch::Domain'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::DBCluster'|'AWS::RDS::DBClusterSnapshot'|'AWS::RDS::EventSubscription'|'AWS::S3::Bucket'|'AWS::S3::AccountPublicAccessBlock'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::SSM::ManagedInstanceInventory'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::DynamoDB::Table'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::RuleGroup'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::RuleGroup'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::WAFv2::WebACL'|'AWS::WAFv2::RuleGroup'|'AWS::WAFv2::IPSet'|'AWS::WAFv2::RegexPatternSet'|'AWS::WAFv2::ManagedRuleSet'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::ApiGateway::Stage'|'AWS::ApiGateway::RestApi'|'AWS::ApiGatewayV2::Stage'|'AWS::ApiGatewayV2::Api'|'AWS::CodePipeline::Pipeline'|'AWS::ServiceCatalog::CloudFormationProvisionedProduct'|'AWS::ServiceCatalog::CloudFormationProduct'|'AWS::ServiceCatalog::Portfolio'|'AWS::SQS::Queue'|'AWS::KMS::Key'|'AWS::QLDB::Ledger',
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
                    'resourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::EC2::RegisteredHAInstance'|'AWS::EC2::NatGateway'|'AWS::EC2::EgressOnlyInternetGateway'|'AWS::EC2::VPCEndpoint'|'AWS::EC2::VPCEndpointService'|'AWS::EC2::FlowLog'|'AWS::EC2::VPCPeeringConnection'|'AWS::Elasticsearch::Domain'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::DBCluster'|'AWS::RDS::DBClusterSnapshot'|'AWS::RDS::EventSubscription'|'AWS::S3::Bucket'|'AWS::S3::AccountPublicAccessBlock'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::SSM::ManagedInstanceInventory'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::DynamoDB::Table'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::RuleGroup'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::RuleGroup'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::WAFv2::WebACL'|'AWS::WAFv2::RuleGroup'|'AWS::WAFv2::IPSet'|'AWS::WAFv2::RegexPatternSet'|'AWS::WAFv2::ManagedRuleSet'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::ApiGateway::Stage'|'AWS::ApiGateway::RestApi'|'AWS::ApiGatewayV2::Stage'|'AWS::ApiGatewayV2::Api'|'AWS::CodePipeline::Pipeline'|'AWS::ServiceCatalog::CloudFormationProvisionedProduct'|'AWS::ServiceCatalog::CloudFormationProduct'|'AWS::ServiceCatalog::Portfolio'|'AWS::SQS::Queue'|'AWS::KMS::Key'|'AWS::QLDB::Ledger',
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


Response Structure

(dict) --
The output for the  GetResourceConfigHistory action.

configurationItems (list) --
A list that contains the configuration history of one or more resources.

(dict) --
A list that contains detailed configurations of a specified resource.

version (string) --
The version number of the resource configuration.

accountId (string) --
The 12-digit AWS account ID associated with the resource.

configurationItemCaptureTime (datetime) --
The time when the configuration recording was initiated.

configurationItemStatus (string) --
The configuration item status.

configurationStateId (string) --
An identifier that indicates the ordering of the configuration items of a resource.

configurationItemMD5Hash (string) --
Unique MD5 hash that represents the configuration item\'s state.
You can use MD5 hash to compare the states of two or more configuration items that are associated with the same resource.

arn (string) --
accoun

resourceType (string) --
The type of AWS resource.

resourceId (string) --
The ID of the resource (for example, sg-xxxxxx ).

resourceName (string) --
The custom name of the resource, if available.

awsRegion (string) --
The region where the resource resides.

availabilityZone (string) --
The Availability Zone associated with the resource.

resourceCreationTime (datetime) --
The time stamp when the resource was created.

tags (dict) --
A mapping of key value tags associated with the resource.

(string) --
(string) --




relatedEvents (list) --
A list of CloudTrail event IDs.
A populated field indicates that the current configuration was initiated by the events recorded in the CloudTrail log. For more information about CloudTrail, see What Is AWS CloudTrail .
An empty field indicates that the current configuration was not initiated by any event. As of Version 1.3, the relatedEvents field is empty. You can access the LookupEvents API in the AWS CloudTrail API Reference to retrieve the events for the resource.

(string) --


relationships (list) --
A list of related AWS resources.

(dict) --
The relationship of the related resource to the main resource.

resourceType (string) --
The resource type of the related resource.

resourceId (string) --
The ID of the related resource (for example, sg-xxxxxx ).

resourceName (string) --
The custom name of the related resource, if available.

relationshipName (string) --
The type of relationship with the related resource.





configuration (string) --
The description of the resource configuration.

supplementaryConfiguration (dict) --
Configuration attributes that AWS Config returns for certain resource types to supplement the information returned for the configuration parameter.

(string) --
(string) --








nextToken (string) --
The string that you use in a subsequent request to get the next page of results in a paginated response.







Exceptions

ConfigService.Client.exceptions.ValidationException
ConfigService.Client.exceptions.InvalidTimeRangeException
ConfigService.Client.exceptions.InvalidLimitException
ConfigService.Client.exceptions.InvalidNextTokenException
ConfigService.Client.exceptions.NoAvailableConfigurationRecorderException
ConfigService.Client.exceptions.ResourceNotDiscoveredException


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
                'resourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::EC2::RegisteredHAInstance'|'AWS::EC2::NatGateway'|'AWS::EC2::EgressOnlyInternetGateway'|'AWS::EC2::VPCEndpoint'|'AWS::EC2::VPCEndpointService'|'AWS::EC2::FlowLog'|'AWS::EC2::VPCPeeringConnection'|'AWS::Elasticsearch::Domain'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::DBCluster'|'AWS::RDS::DBClusterSnapshot'|'AWS::RDS::EventSubscription'|'AWS::S3::Bucket'|'AWS::S3::AccountPublicAccessBlock'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::SSM::ManagedInstanceInventory'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::DynamoDB::Table'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::RuleGroup'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::RuleGroup'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::WAFv2::WebACL'|'AWS::WAFv2::RuleGroup'|'AWS::WAFv2::IPSet'|'AWS::WAFv2::RegexPatternSet'|'AWS::WAFv2::ManagedRuleSet'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::ApiGateway::Stage'|'AWS::ApiGateway::RestApi'|'AWS::ApiGatewayV2::Stage'|'AWS::ApiGatewayV2::Api'|'AWS::CodePipeline::Pipeline'|'AWS::ServiceCatalog::CloudFormationProvisionedProduct'|'AWS::ServiceCatalog::CloudFormationProduct'|'AWS::ServiceCatalog::Portfolio'|'AWS::SQS::Queue'|'AWS::KMS::Key'|'AWS::QLDB::Ledger',
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
                        'resourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::EC2::RegisteredHAInstance'|'AWS::EC2::NatGateway'|'AWS::EC2::EgressOnlyInternetGateway'|'AWS::EC2::VPCEndpoint'|'AWS::EC2::VPCEndpointService'|'AWS::EC2::FlowLog'|'AWS::EC2::VPCPeeringConnection'|'AWS::Elasticsearch::Domain'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::DBCluster'|'AWS::RDS::DBClusterSnapshot'|'AWS::RDS::EventSubscription'|'AWS::S3::Bucket'|'AWS::S3::AccountPublicAccessBlock'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::SSM::ManagedInstanceInventory'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::DynamoDB::Table'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::RuleGroup'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::RuleGroup'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::WAFv2::WebACL'|'AWS::WAFv2::RuleGroup'|'AWS::WAFv2::IPSet'|'AWS::WAFv2::RegexPatternSet'|'AWS::WAFv2::ManagedRuleSet'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::ApiGateway::Stage'|'AWS::ApiGateway::RestApi'|'AWS::ApiGatewayV2::Stage'|'AWS::ApiGatewayV2::Api'|'AWS::CodePipeline::Pipeline'|'AWS::ServiceCatalog::CloudFormationProvisionedProduct'|'AWS::ServiceCatalog::CloudFormationProduct'|'AWS::ServiceCatalog::Portfolio'|'AWS::SQS::Queue'|'AWS::KMS::Key'|'AWS::QLDB::Ledger',
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
    Returns an object that can wait for some condition.
    
    :type waiter_name: str
    :param waiter_name: The name of the waiter to get. See the waiters\nsection of the service docs for a list of available waiters.

    :rtype: botocore.waiter.Waiter


    """
    pass

def list_aggregate_discovered_resources(ConfigurationAggregatorName=None, ResourceType=None, Filters=None, Limit=None, NextToken=None):
    """
    Accepts a resource type and returns a list of resource identifiers that are aggregated for a specific resource type across accounts and regions. A resource identifier includes the resource type, ID, (if available) the custom resource name, source account, and source region. You can narrow the results to include only resources that have specific resource IDs, or a resource name, or source account ID, or source region.
    For example, if the input consists of accountID 12345678910 and the region is us-east-1 for resource type AWS::EC2::Instance then the API returns all the EC2 instance identifiers of accountID 12345678910 and region us-east-1.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_aggregate_discovered_resources(
        ConfigurationAggregatorName='string',
        ResourceType='AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::EC2::RegisteredHAInstance'|'AWS::EC2::NatGateway'|'AWS::EC2::EgressOnlyInternetGateway'|'AWS::EC2::VPCEndpoint'|'AWS::EC2::VPCEndpointService'|'AWS::EC2::FlowLog'|'AWS::EC2::VPCPeeringConnection'|'AWS::Elasticsearch::Domain'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::DBCluster'|'AWS::RDS::DBClusterSnapshot'|'AWS::RDS::EventSubscription'|'AWS::S3::Bucket'|'AWS::S3::AccountPublicAccessBlock'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::SSM::ManagedInstanceInventory'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::DynamoDB::Table'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::RuleGroup'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::RuleGroup'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::WAFv2::WebACL'|'AWS::WAFv2::RuleGroup'|'AWS::WAFv2::IPSet'|'AWS::WAFv2::RegexPatternSet'|'AWS::WAFv2::ManagedRuleSet'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::ApiGateway::Stage'|'AWS::ApiGateway::RestApi'|'AWS::ApiGatewayV2::Stage'|'AWS::ApiGatewayV2::Api'|'AWS::CodePipeline::Pipeline'|'AWS::ServiceCatalog::CloudFormationProvisionedProduct'|'AWS::ServiceCatalog::CloudFormationProduct'|'AWS::ServiceCatalog::Portfolio'|'AWS::SQS::Queue'|'AWS::KMS::Key'|'AWS::QLDB::Ledger',
        Filters={
            'AccountId': 'string',
            'ResourceId': 'string',
            'ResourceName': 'string',
            'Region': 'string'
        },
        Limit=123,
        NextToken='string'
    )
    
    
    :type ConfigurationAggregatorName: string
    :param ConfigurationAggregatorName: [REQUIRED]\nThe name of the configuration aggregator.\n

    :type ResourceType: string
    :param ResourceType: [REQUIRED]\nThe type of resources that you want AWS Config to list in the response.\n

    :type Filters: dict
    :param Filters: Filters the results based on the ResourceFilters object.\n\nAccountId (string) --The 12-digit source account ID.\n\nResourceId (string) --The ID of the resource.\n\nResourceName (string) --The name of the resource.\n\nRegion (string) --The source region.\n\n\n

    :type Limit: integer
    :param Limit: The maximum number of resource identifiers returned on each page. The default is 100. You cannot specify a number greater than 100. If you specify 0, AWS Config uses the default.

    :type NextToken: string
    :param NextToken: The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.

    :rtype: dict

ReturnsResponse Syntax
{
    'ResourceIdentifiers': [
        {
            'SourceAccountId': 'string',
            'SourceRegion': 'string',
            'ResourceId': 'string',
            'ResourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::EC2::RegisteredHAInstance'|'AWS::EC2::NatGateway'|'AWS::EC2::EgressOnlyInternetGateway'|'AWS::EC2::VPCEndpoint'|'AWS::EC2::VPCEndpointService'|'AWS::EC2::FlowLog'|'AWS::EC2::VPCPeeringConnection'|'AWS::Elasticsearch::Domain'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::DBCluster'|'AWS::RDS::DBClusterSnapshot'|'AWS::RDS::EventSubscription'|'AWS::S3::Bucket'|'AWS::S3::AccountPublicAccessBlock'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::SSM::ManagedInstanceInventory'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::DynamoDB::Table'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::RuleGroup'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::RuleGroup'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::WAFv2::WebACL'|'AWS::WAFv2::RuleGroup'|'AWS::WAFv2::IPSet'|'AWS::WAFv2::RegexPatternSet'|'AWS::WAFv2::ManagedRuleSet'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::ApiGateway::Stage'|'AWS::ApiGateway::RestApi'|'AWS::ApiGatewayV2::Stage'|'AWS::ApiGatewayV2::Api'|'AWS::CodePipeline::Pipeline'|'AWS::ServiceCatalog::CloudFormationProvisionedProduct'|'AWS::ServiceCatalog::CloudFormationProduct'|'AWS::ServiceCatalog::Portfolio'|'AWS::SQS::Queue'|'AWS::KMS::Key'|'AWS::QLDB::Ledger',
            'ResourceName': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

ResourceIdentifiers (list) --
Returns a list of ResourceIdentifiers objects.

(dict) --
The details that identify a resource that is collected by AWS Config aggregator, including the resource type, ID, (if available) the custom resource name, the source account, and source region.

SourceAccountId (string) --
The 12-digit account ID of the source account.

SourceRegion (string) --
The source region where data is aggregated.

ResourceId (string) --
The ID of the AWS resource.

ResourceType (string) --
The type of the AWS resource.

ResourceName (string) --
The name of the AWS resource.





NextToken (string) --
The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.







Exceptions

ConfigService.Client.exceptions.ValidationException
ConfigService.Client.exceptions.InvalidLimitException
ConfigService.Client.exceptions.InvalidNextTokenException
ConfigService.Client.exceptions.NoSuchConfigurationAggregatorException


    :return: {
        'ResourceIdentifiers': [
            {
                'SourceAccountId': 'string',
                'SourceRegion': 'string',
                'ResourceId': 'string',
                'ResourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::EC2::RegisteredHAInstance'|'AWS::EC2::NatGateway'|'AWS::EC2::EgressOnlyInternetGateway'|'AWS::EC2::VPCEndpoint'|'AWS::EC2::VPCEndpointService'|'AWS::EC2::FlowLog'|'AWS::EC2::VPCPeeringConnection'|'AWS::Elasticsearch::Domain'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::DBCluster'|'AWS::RDS::DBClusterSnapshot'|'AWS::RDS::EventSubscription'|'AWS::S3::Bucket'|'AWS::S3::AccountPublicAccessBlock'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::SSM::ManagedInstanceInventory'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::DynamoDB::Table'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::RuleGroup'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::RuleGroup'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::WAFv2::WebACL'|'AWS::WAFv2::RuleGroup'|'AWS::WAFv2::IPSet'|'AWS::WAFv2::RegexPatternSet'|'AWS::WAFv2::ManagedRuleSet'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::ApiGateway::Stage'|'AWS::ApiGateway::RestApi'|'AWS::ApiGatewayV2::Stage'|'AWS::ApiGatewayV2::Api'|'AWS::CodePipeline::Pipeline'|'AWS::ServiceCatalog::CloudFormationProvisionedProduct'|'AWS::ServiceCatalog::CloudFormationProduct'|'AWS::ServiceCatalog::Portfolio'|'AWS::SQS::Queue'|'AWS::KMS::Key'|'AWS::QLDB::Ledger',
                'ResourceName': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    ConfigService.Client.exceptions.ValidationException
    ConfigService.Client.exceptions.InvalidLimitException
    ConfigService.Client.exceptions.InvalidNextTokenException
    ConfigService.Client.exceptions.NoSuchConfigurationAggregatorException
    
    """
    pass

def list_discovered_resources(resourceType=None, resourceIds=None, resourceName=None, limit=None, includeDeletedResources=None, nextToken=None):
    """
    Accepts a resource type and returns a list of resource identifiers for the resources of that type. A resource identifier includes the resource type, ID, and (if available) the custom resource name. The results consist of resources that AWS Config has discovered, including those that AWS Config is not currently recording. You can narrow the results to include only resources that have specific resource IDs or a resource name.
    The response is paginated. By default, AWS Config lists 100 resource identifiers on each page. You can customize this number with the limit parameter. The response includes a nextToken string. To get the next page of results, run the request again and specify the string for the nextToken parameter.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_discovered_resources(
        resourceType='AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::EC2::RegisteredHAInstance'|'AWS::EC2::NatGateway'|'AWS::EC2::EgressOnlyInternetGateway'|'AWS::EC2::VPCEndpoint'|'AWS::EC2::VPCEndpointService'|'AWS::EC2::FlowLog'|'AWS::EC2::VPCPeeringConnection'|'AWS::Elasticsearch::Domain'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::DBCluster'|'AWS::RDS::DBClusterSnapshot'|'AWS::RDS::EventSubscription'|'AWS::S3::Bucket'|'AWS::S3::AccountPublicAccessBlock'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::SSM::ManagedInstanceInventory'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::DynamoDB::Table'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::RuleGroup'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::RuleGroup'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::WAFv2::WebACL'|'AWS::WAFv2::RuleGroup'|'AWS::WAFv2::IPSet'|'AWS::WAFv2::RegexPatternSet'|'AWS::WAFv2::ManagedRuleSet'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::ApiGateway::Stage'|'AWS::ApiGateway::RestApi'|'AWS::ApiGatewayV2::Stage'|'AWS::ApiGatewayV2::Api'|'AWS::CodePipeline::Pipeline'|'AWS::ServiceCatalog::CloudFormationProvisionedProduct'|'AWS::ServiceCatalog::CloudFormationProduct'|'AWS::ServiceCatalog::Portfolio'|'AWS::SQS::Queue'|'AWS::KMS::Key'|'AWS::QLDB::Ledger',
        resourceIds=[
            'string',
        ],
        resourceName='string',
        limit=123,
        includeDeletedResources=True|False,
        nextToken='string'
    )
    
    
    :type resourceType: string
    :param resourceType: [REQUIRED]\nThe type of resources that you want AWS Config to list in the response.\n

    :type resourceIds: list
    :param resourceIds: The IDs of only those resources that you want AWS Config to list in the response. If you do not specify this parameter, AWS Config lists all resources of the specified type that it has discovered.\n\n(string) --\n\n

    :type resourceName: string
    :param resourceName: The custom name of only those resources that you want AWS Config to list in the response. If you do not specify this parameter, AWS Config lists all resources of the specified type that it has discovered.

    :type limit: integer
    :param limit: The maximum number of resource identifiers returned on each page. The default is 100. You cannot specify a number greater than 100. If you specify 0, AWS Config uses the default.

    :type includeDeletedResources: boolean
    :param includeDeletedResources: Specifies whether AWS Config includes deleted resources in the results. By default, deleted resources are not included.

    :type nextToken: string
    :param nextToken: The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.

    :rtype: dict

ReturnsResponse Syntax
{
    'resourceIdentifiers': [
        {
            'resourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::EC2::RegisteredHAInstance'|'AWS::EC2::NatGateway'|'AWS::EC2::EgressOnlyInternetGateway'|'AWS::EC2::VPCEndpoint'|'AWS::EC2::VPCEndpointService'|'AWS::EC2::FlowLog'|'AWS::EC2::VPCPeeringConnection'|'AWS::Elasticsearch::Domain'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::DBCluster'|'AWS::RDS::DBClusterSnapshot'|'AWS::RDS::EventSubscription'|'AWS::S3::Bucket'|'AWS::S3::AccountPublicAccessBlock'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::SSM::ManagedInstanceInventory'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::DynamoDB::Table'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::RuleGroup'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::RuleGroup'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::WAFv2::WebACL'|'AWS::WAFv2::RuleGroup'|'AWS::WAFv2::IPSet'|'AWS::WAFv2::RegexPatternSet'|'AWS::WAFv2::ManagedRuleSet'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::ApiGateway::Stage'|'AWS::ApiGateway::RestApi'|'AWS::ApiGatewayV2::Stage'|'AWS::ApiGatewayV2::Api'|'AWS::CodePipeline::Pipeline'|'AWS::ServiceCatalog::CloudFormationProvisionedProduct'|'AWS::ServiceCatalog::CloudFormationProduct'|'AWS::ServiceCatalog::Portfolio'|'AWS::SQS::Queue'|'AWS::KMS::Key'|'AWS::QLDB::Ledger',
            'resourceId': 'string',
            'resourceName': 'string',
            'resourceDeletionTime': datetime(2015, 1, 1)
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

resourceIdentifiers (list) --
The details that identify a resource that is discovered by AWS Config, including the resource type, ID, and (if available) the custom resource name.

(dict) --
The details that identify a resource that is discovered by AWS Config, including the resource type, ID, and (if available) the custom resource name.

resourceType (string) --
The type of resource.

resourceId (string) --
The ID of the resource (for example, sg-xxxxxx ).

resourceName (string) --
The custom name of the resource (if available).

resourceDeletionTime (datetime) --
The time that the resource was deleted.





nextToken (string) --
The string that you use in a subsequent request to get the next page of results in a paginated response.







Exceptions

ConfigService.Client.exceptions.ValidationException
ConfigService.Client.exceptions.InvalidLimitException
ConfigService.Client.exceptions.InvalidNextTokenException
ConfigService.Client.exceptions.NoAvailableConfigurationRecorderException


    :return: {
        'resourceIdentifiers': [
            {
                'resourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::EC2::RegisteredHAInstance'|'AWS::EC2::NatGateway'|'AWS::EC2::EgressOnlyInternetGateway'|'AWS::EC2::VPCEndpoint'|'AWS::EC2::VPCEndpointService'|'AWS::EC2::FlowLog'|'AWS::EC2::VPCPeeringConnection'|'AWS::Elasticsearch::Domain'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::DBCluster'|'AWS::RDS::DBClusterSnapshot'|'AWS::RDS::EventSubscription'|'AWS::S3::Bucket'|'AWS::S3::AccountPublicAccessBlock'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::SSM::ManagedInstanceInventory'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::DynamoDB::Table'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::RuleGroup'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::RuleGroup'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::WAFv2::WebACL'|'AWS::WAFv2::RuleGroup'|'AWS::WAFv2::IPSet'|'AWS::WAFv2::RegexPatternSet'|'AWS::WAFv2::ManagedRuleSet'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::ApiGateway::Stage'|'AWS::ApiGateway::RestApi'|'AWS::ApiGatewayV2::Stage'|'AWS::ApiGatewayV2::Api'|'AWS::CodePipeline::Pipeline'|'AWS::ServiceCatalog::CloudFormationProvisionedProduct'|'AWS::ServiceCatalog::CloudFormationProduct'|'AWS::ServiceCatalog::Portfolio'|'AWS::SQS::Queue'|'AWS::KMS::Key'|'AWS::QLDB::Ledger',
                'resourceId': 'string',
                'resourceName': 'string',
                'resourceDeletionTime': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    ConfigService.Client.exceptions.ValidationException
    ConfigService.Client.exceptions.InvalidLimitException
    ConfigService.Client.exceptions.InvalidNextTokenException
    ConfigService.Client.exceptions.NoAvailableConfigurationRecorderException
    
    """
    pass

def list_tags_for_resource(ResourceArn=None, Limit=None, NextToken=None):
    """
    List the tags for AWS Config resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        ResourceArn='string',
        Limit=123,
        NextToken='string'
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that identifies the resource for which to list the tags. Currently, the supported resources are ConfigRule , ConfigurationAggregator and AggregatorAuthorization .\n

    :type Limit: integer
    :param Limit: The maximum number of tags returned on each page. The limit maximum is 50. You cannot specify a number greater than 50. If you specify 0, AWS Config uses the default.

    :type NextToken: string
    :param NextToken: The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.

    :rtype: dict

ReturnsResponse Syntax
{
    'Tags': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Tags (list) --
The tags for the resource.

(dict) --
The tags for the resource. The metadata that you apply to a resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.

Key (string) --
One part of a key-value pair that make up a tag. A key is a general label that acts like a category for more specific tag values.

Value (string) --
The optional part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key).





NextToken (string) --
The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.







Exceptions

ConfigService.Client.exceptions.ResourceNotFoundException
ConfigService.Client.exceptions.ValidationException
ConfigService.Client.exceptions.InvalidLimitException
ConfigService.Client.exceptions.InvalidNextTokenException


    :return: {
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    ConfigService.Client.exceptions.ResourceNotFoundException
    ConfigService.Client.exceptions.ValidationException
    ConfigService.Client.exceptions.InvalidLimitException
    ConfigService.Client.exceptions.InvalidNextTokenException
    
    """
    pass

def put_aggregation_authorization(AuthorizedAccountId=None, AuthorizedAwsRegion=None, Tags=None):
    """
    Authorizes the aggregator account and region to collect data from the source account and region.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_aggregation_authorization(
        AuthorizedAccountId='string',
        AuthorizedAwsRegion='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type AuthorizedAccountId: string
    :param AuthorizedAccountId: [REQUIRED]\nThe 12-digit account ID of the account authorized to aggregate data.\n

    :type AuthorizedAwsRegion: string
    :param AuthorizedAwsRegion: [REQUIRED]\nThe region authorized to collect aggregated data.\n

    :type Tags: list
    :param Tags: An array of tag object.\n\n(dict) --The tags for the resource. The metadata that you apply to a resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.\n\nKey (string) --One part of a key-value pair that make up a tag. A key is a general label that acts like a category for more specific tag values.\n\nValue (string) --The optional part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key).\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'AggregationAuthorization': {
        'AggregationAuthorizationArn': 'string',
        'AuthorizedAccountId': 'string',
        'AuthorizedAwsRegion': 'string',
        'CreationTime': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --

AggregationAuthorization (dict) --
Returns an AggregationAuthorization object.

AggregationAuthorizationArn (string) --
The Amazon Resource Name (ARN) of the aggregation object.

AuthorizedAccountId (string) --
The 12-digit account ID of the account authorized to aggregate data.

AuthorizedAwsRegion (string) --
The region authorized to collect aggregated data.

CreationTime (datetime) --
The time stamp when the aggregation authorization was created.









Exceptions

ConfigService.Client.exceptions.InvalidParameterValueException


    :return: {
        'AggregationAuthorization': {
            'AggregationAuthorizationArn': 'string',
            'AuthorizedAccountId': 'string',
            'AuthorizedAwsRegion': 'string',
            'CreationTime': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    ConfigService.Client.exceptions.InvalidParameterValueException
    
    """
    pass

def put_config_rule(ConfigRule=None, Tags=None):
    """
    Adds or updates an AWS Config rule for evaluating whether your AWS resources comply with your desired configurations.
    You can use this action for custom AWS Config rules and AWS managed Config rules. A custom AWS Config rule is a rule that you develop and maintain. An AWS managed Config rule is a customizable, predefined rule that AWS Config provides.
    If you are adding a new custom AWS Config rule, you must first create the AWS Lambda function that the rule invokes to evaluate your resources. When you use the PutConfigRule action to add the rule to AWS Config, you must specify the Amazon Resource Name (ARN) that AWS Lambda assigns to the function. Specify the ARN for the SourceIdentifier key. This key is part of the Source object, which is part of the ConfigRule object.
    If you are adding an AWS managed Config rule, specify the rule\'s identifier for the SourceIdentifier key. To reference AWS managed Config rule identifiers, see About AWS Managed Config Rules .
    For any new rule that you add, specify the ConfigRuleName in the ConfigRule object. Do not specify the ConfigRuleArn or the ConfigRuleId . These values are generated by AWS Config for new rules.
    If you are updating a rule that you added previously, you can specify the rule by ConfigRuleName , ConfigRuleId , or ConfigRuleArn in the ConfigRule data type that you use in this request.
    The maximum number of rules that AWS Config supports is 150.
    For information about requesting a rule limit increase, see AWS Config Limits in the AWS General Reference Guide .
    For more information about developing and using AWS Config rules, see Evaluating AWS Resource Configurations with AWS Config in the AWS Config Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
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
            'ConfigRuleState': 'ACTIVE'|'DELETING'|'DELETING_RESULTS'|'EVALUATING',
            'CreatedBy': 'string'
        },
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ConfigRule: dict
    :param ConfigRule: [REQUIRED]\nThe rule that you want to add to your account.\n\nConfigRuleName (string) --The name that you assign to the AWS Config rule. The name is required if you are adding a new rule.\n\nConfigRuleArn (string) --The Amazon Resource Name (ARN) of the AWS Config rule.\n\nConfigRuleId (string) --The ID of the AWS Config rule.\n\nDescription (string) --The description that you provide for the AWS Config rule.\n\nScope (dict) --Defines which resources can trigger an evaluation for the rule. The scope can include one or more resource types, a combination of one resource type and one resource ID, or a combination of a tag key and value. Specify a scope to constrain the resources that can trigger an evaluation for the rule. If you do not specify a scope, evaluations are triggered when any resource in the recording group changes.\n\nComplianceResourceTypes (list) --The resource types of only those AWS resources that you want to trigger an evaluation for the rule. You can only specify one type if you also specify a resource ID for ComplianceResourceId .\n\n(string) --\n\n\nTagKey (string) --The tag key that is applied to only those AWS resources that you want to trigger an evaluation for the rule.\n\nTagValue (string) --The tag value applied to only those AWS resources that you want to trigger an evaluation for the rule. If you specify a value for TagValue , you must also specify a value for TagKey .\n\nComplianceResourceId (string) --The ID of the only AWS resource that you want to trigger an evaluation for the rule. If you specify a resource ID, you must specify one resource type for ComplianceResourceTypes .\n\n\n\nSource (dict) -- [REQUIRED]Provides the rule owner (AWS or customer), the rule identifier, and the notifications that cause the function to evaluate your AWS resources.\n\nOwner (string) -- [REQUIRED]Indicates whether AWS or the customer owns and manages the AWS Config rule.\n\nSourceIdentifier (string) -- [REQUIRED]For AWS Config managed rules, a predefined identifier from a list. For example, IAM_PASSWORD_POLICY is a managed rule. To reference a managed rule, see Using AWS Managed Config Rules .\nFor custom rules, the identifier is the Amazon Resource Name (ARN) of the rule\'s AWS Lambda function, such as arn:aws:lambda:us-east-2:123456789012:function:custom_rule_name .\n\nSourceDetails (list) --Provides the source and type of the event that causes AWS Config to evaluate your AWS resources.\n\n(dict) --Provides the source and the message types that trigger AWS Config to evaluate your AWS resources against a rule. It also provides the frequency with which you want AWS Config to run evaluations for the rule if the trigger type is periodic. You can specify the parameter values for SourceDetail only for custom rules.\n\nEventSource (string) --The source of the event, such as an AWS service, that triggers AWS Config to evaluate your AWS resources.\n\nMessageType (string) --The type of notification that triggers AWS Config to run an evaluation for a rule. You can specify the following notification types:\n\nConfigurationItemChangeNotification - Triggers an evaluation when AWS Config delivers a configuration item as a result of a resource change.\nOversizedConfigurationItemChangeNotification - Triggers an evaluation when AWS Config delivers an oversized configuration item. AWS Config may generate this notification type when a resource changes and the notification exceeds the maximum size allowed by Amazon SNS.\nScheduledNotification - Triggers a periodic evaluation at the frequency specified for MaximumExecutionFrequency .\nConfigurationSnapshotDeliveryCompleted - Triggers a periodic evaluation when AWS Config delivers a configuration snapshot.\n\nIf you want your custom rule to be triggered by configuration changes, specify two SourceDetail objects, one for ConfigurationItemChangeNotification and one for OversizedConfigurationItemChangeNotification .\n\nMaximumExecutionFrequency (string) --The frequency at which you want AWS Config to run evaluations for a custom rule with a periodic trigger. If you specify a value for MaximumExecutionFrequency , then MessageType must use the ScheduledNotification value.\n\nNote\nBy default, rules with a periodic trigger are evaluated every 24 hours. To change the frequency, specify a valid value for the MaximumExecutionFrequency parameter.\nBased on the valid value you choose, AWS Config runs evaluations once for each valid value. For example, if you choose Three_Hours , AWS Config runs evaluations once every three hours. In this case, Three_Hours is the frequency of this rule.\n\n\n\n\n\n\n\n\nInputParameters (string) --A string, in JSON format, that is passed to the AWS Config rule Lambda function.\n\nMaximumExecutionFrequency (string) --The maximum frequency with which AWS Config runs evaluations for a rule. You can specify a value for MaximumExecutionFrequency when:\n\nYou are using an AWS managed rule that is triggered at a periodic frequency.\nYour custom rule is triggered when AWS Config delivers the configuration snapshot. For more information, see ConfigSnapshotDeliveryProperties .\n\n\nNote\nBy default, rules with a periodic trigger are evaluated every 24 hours. To change the frequency, specify a valid value for the MaximumExecutionFrequency parameter.\n\n\nConfigRuleState (string) --Indicates whether the AWS Config rule is active or is currently being deleted by AWS Config. It can also indicate the evaluation status for the AWS Config rule.\nAWS Config sets the state of the rule to EVALUATING temporarily after you use the StartConfigRulesEvaluation request to evaluate your resources against the AWS Config rule.\nAWS Config sets the state of the rule to DELETING_RESULTS temporarily after you use the DeleteEvaluationResults request to delete the current evaluation results for the AWS Config rule.\nAWS Config temporarily sets the state of a rule to DELETING after you use the DeleteConfigRule request to delete the rule. After AWS Config deletes the rule, the rule and all of its evaluations are erased and are no longer available.\n\nCreatedBy (string) --Service principal name of the service that created the rule.\n\nNote\nThe field is populated only if the service linked rule is created by a service. The field is empty if you create your own rule.\n\n\n\n

    :type Tags: list
    :param Tags: An array of tag object.\n\n(dict) --The tags for the resource. The metadata that you apply to a resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.\n\nKey (string) --One part of a key-value pair that make up a tag. A key is a general label that acts like a category for more specific tag values.\n\nValue (string) --The optional part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key).\n\n\n\n\n

    :returns: 
    ConfigService.Client.exceptions.InvalidParameterValueException
    ConfigService.Client.exceptions.MaxNumberOfConfigRulesExceededException
    ConfigService.Client.exceptions.ResourceInUseException
    ConfigService.Client.exceptions.InsufficientPermissionsException
    ConfigService.Client.exceptions.NoAvailableConfigurationRecorderException
    
    """
    pass

def put_configuration_aggregator(ConfigurationAggregatorName=None, AccountAggregationSources=None, OrganizationAggregationSource=None, Tags=None):
    """
    Creates and updates the configuration aggregator with the selected source accounts and regions. The source account can be individual account(s) or an organization.
    See also: AWS API Documentation
    
    Exceptions
    
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
        },
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ConfigurationAggregatorName: string
    :param ConfigurationAggregatorName: [REQUIRED]\nThe name of the configuration aggregator.\n

    :type AccountAggregationSources: list
    :param AccountAggregationSources: A list of AccountAggregationSource object.\n\n(dict) --A collection of accounts and regions.\n\nAccountIds (list) -- [REQUIRED]The 12-digit account ID of the account being aggregated.\n\n(string) --\n\n\nAllAwsRegions (boolean) --If true, aggregate existing AWS Config regions and future regions.\n\nAwsRegions (list) --The source regions being aggregated.\n\n(string) --\n\n\n\n\n\n

    :type OrganizationAggregationSource: dict
    :param OrganizationAggregationSource: An OrganizationAggregationSource object.\n\nRoleArn (string) -- [REQUIRED]ARN of the IAM role used to retrieve AWS Organization details associated with the aggregator account.\n\nAwsRegions (list) --The source regions being aggregated.\n\n(string) --\n\n\nAllAwsRegions (boolean) --If true, aggregate existing AWS Config regions and future regions.\n\n\n

    :type Tags: list
    :param Tags: An array of tag object.\n\n(dict) --The tags for the resource. The metadata that you apply to a resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.\n\nKey (string) --One part of a key-value pair that make up a tag. A key is a general label that acts like a category for more specific tag values.\n\nValue (string) --The optional part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key).\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

ConfigurationAggregator (dict) --
Returns a ConfigurationAggregator object.

ConfigurationAggregatorName (string) --
The name of the aggregator.

ConfigurationAggregatorArn (string) --
The Amazon Resource Name (ARN) of the aggregator.

AccountAggregationSources (list) --
Provides a list of source accounts and regions to be aggregated.

(dict) --
A collection of accounts and regions.

AccountIds (list) --
The 12-digit account ID of the account being aggregated.

(string) --


AllAwsRegions (boolean) --
If true, aggregate existing AWS Config regions and future regions.

AwsRegions (list) --
The source regions being aggregated.

(string) --






OrganizationAggregationSource (dict) --
Provides an organization and list of regions to be aggregated.

RoleArn (string) --
ARN of the IAM role used to retrieve AWS Organization details associated with the aggregator account.

AwsRegions (list) --
The source regions being aggregated.

(string) --


AllAwsRegions (boolean) --
If true, aggregate existing AWS Config regions and future regions.



CreationTime (datetime) --
The time stamp when the configuration aggregator was created.

LastUpdatedTime (datetime) --
The time of the last update.









Exceptions

ConfigService.Client.exceptions.InvalidParameterValueException
ConfigService.Client.exceptions.LimitExceededException
ConfigService.Client.exceptions.InvalidRoleException
ConfigService.Client.exceptions.OrganizationAccessDeniedException
ConfigService.Client.exceptions.NoAvailableOrganizationException
ConfigService.Client.exceptions.OrganizationAllFeaturesNotEnabledException


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
    
    Exceptions
    
    :example: response = client.put_configuration_recorder(
        ConfigurationRecorder={
            'name': 'string',
            'roleARN': 'string',
            'recordingGroup': {
                'allSupported': True|False,
                'includeGlobalResourceTypes': True|False,
                'resourceTypes': [
                    'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::EC2::RegisteredHAInstance'|'AWS::EC2::NatGateway'|'AWS::EC2::EgressOnlyInternetGateway'|'AWS::EC2::VPCEndpoint'|'AWS::EC2::VPCEndpointService'|'AWS::EC2::FlowLog'|'AWS::EC2::VPCPeeringConnection'|'AWS::Elasticsearch::Domain'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::DBCluster'|'AWS::RDS::DBClusterSnapshot'|'AWS::RDS::EventSubscription'|'AWS::S3::Bucket'|'AWS::S3::AccountPublicAccessBlock'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::SSM::ManagedInstanceInventory'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::DynamoDB::Table'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::RuleGroup'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::RuleGroup'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::WAFv2::WebACL'|'AWS::WAFv2::RuleGroup'|'AWS::WAFv2::IPSet'|'AWS::WAFv2::RegexPatternSet'|'AWS::WAFv2::ManagedRuleSet'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::ApiGateway::Stage'|'AWS::ApiGateway::RestApi'|'AWS::ApiGatewayV2::Stage'|'AWS::ApiGatewayV2::Api'|'AWS::CodePipeline::Pipeline'|'AWS::ServiceCatalog::CloudFormationProvisionedProduct'|'AWS::ServiceCatalog::CloudFormationProduct'|'AWS::ServiceCatalog::Portfolio'|'AWS::SQS::Queue'|'AWS::KMS::Key'|'AWS::QLDB::Ledger',
                ]
            }
        }
    )
    
    
    :type ConfigurationRecorder: dict
    :param ConfigurationRecorder: [REQUIRED]\nThe configuration recorder object that records each configuration change made to the resources.\n\nname (string) --The name of the recorder. By default, AWS Config automatically assigns the name 'default' when creating the configuration recorder. You cannot change the assigned name.\n\nroleARN (string) --Amazon Resource Name (ARN) of the IAM role used to describe the AWS resources associated with the account.\n\nrecordingGroup (dict) --Specifies the types of AWS resources for which AWS Config records configuration changes.\n\nallSupported (boolean) --Specifies whether AWS Config records configuration changes for every supported type of regional resource.\nIf you set this option to true , when AWS Config adds support for a new type of regional resource, it starts recording resources of that type automatically.\nIf you set this option to true , you cannot enumerate a list of resourceTypes .\n\nincludeGlobalResourceTypes (boolean) --Specifies whether AWS Config includes all supported types of global resources (for example, IAM resources) with the resources that it records.\nBefore you can set this option to true , you must set the allSupported option to true .\nIf you set this option to true , when AWS Config adds support for a new type of global resource, it starts recording resources of that type automatically.\nThe configuration details for any global resource are the same in all regions. To prevent duplicate configuration items, you should consider customizing AWS Config in only one region to record global resources.\n\nresourceTypes (list) --A comma-separated list that specifies the types of AWS resources for which AWS Config records configuration changes (for example, AWS::EC2::Instance or AWS::CloudTrail::Trail ).\nBefore you can set this option to true , you must set the allSupported option to false .\nIf you set this option to true , when AWS Config adds support for a new type of resource, it will not record resources of that type unless you manually add that type to your recording group.\nFor a list of valid resourceTypes values, see the resourceType Value column in Supported AWS Resource Types .\n\n(string) --\n\n\n\n\n\n

    :returns: 
    ConfigService.Client.exceptions.MaxNumberOfConfigurationRecordersExceededException
    ConfigService.Client.exceptions.InvalidConfigurationRecorderNameException
    ConfigService.Client.exceptions.InvalidRoleException
    ConfigService.Client.exceptions.InvalidRecordingGroupException
    
    """
    pass

def put_conformance_pack(ConformancePackName=None, TemplateS3Uri=None, TemplateBody=None, DeliveryS3Bucket=None, DeliveryS3KeyPrefix=None, ConformancePackInputParameters=None):
    """
    Creates or updates a conformance pack. A conformance pack is a collection of AWS Config rules that can be easily deployed in an account and a region and across AWS Organization.
    This API creates a service linked role AWSServiceRoleForConfigConforms in your account. The service linked role is created only when the role does not exist in your account. AWS Config verifies the existence of role with GetRole action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_conformance_pack(
        ConformancePackName='string',
        TemplateS3Uri='string',
        TemplateBody='string',
        DeliveryS3Bucket='string',
        DeliveryS3KeyPrefix='string',
        ConformancePackInputParameters=[
            {
                'ParameterName': 'string',
                'ParameterValue': 'string'
            },
        ]
    )
    
    
    :type ConformancePackName: string
    :param ConformancePackName: [REQUIRED]\nName of the conformance pack you want to create.\n

    :type TemplateS3Uri: string
    :param TemplateS3Uri: Location of file containing the template body (s3://bucketname/prefix ). The uri must point to the conformance pack template (max size: 300 KB) that is located in an Amazon S3 bucket in the same region as the conformance pack.\n\nNote\nYou must have access to read Amazon S3 bucket.\n\n

    :type TemplateBody: string
    :param TemplateBody: A string containing full conformance pack template body. Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes.\n\nNote\nYou can only use a YAML template with one resource type, that is, config rule and a remediation action.\n\n

    :type DeliveryS3Bucket: string
    :param DeliveryS3Bucket: [REQUIRED]\nAWS Config stores intermediate files while processing conformance pack template.\n

    :type DeliveryS3KeyPrefix: string
    :param DeliveryS3KeyPrefix: The prefix for the Amazon S3 bucket.

    :type ConformancePackInputParameters: list
    :param ConformancePackInputParameters: A list of ConformancePackInputParameter objects.\n\n(dict) --Input parameters in the form of key-value pairs for the conformance pack, both of which you define. Keys can have a maximum character length of 128 characters, and values can have a maximum length of 256 characters.\n\nParameterName (string) -- [REQUIRED]One part of a key-value pair.\n\nParameterValue (string) -- [REQUIRED]Another part of the key-value pair.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ConformancePackArn': 'string'
}


Response Structure

(dict) --

ConformancePackArn (string) --
ARN of the conformance pack.







Exceptions

ConfigService.Client.exceptions.InsufficientPermissionsException
ConfigService.Client.exceptions.ConformancePackTemplateValidationException
ConfigService.Client.exceptions.ResourceInUseException
ConfigService.Client.exceptions.InvalidParameterValueException
ConfigService.Client.exceptions.MaxNumberOfConformancePacksExceededException


    :return: {
        'ConformancePackArn': 'string'
    }
    
    
    :returns: 
    ConfigService.Client.exceptions.InsufficientPermissionsException
    ConfigService.Client.exceptions.ConformancePackTemplateValidationException
    ConfigService.Client.exceptions.ResourceInUseException
    ConfigService.Client.exceptions.InvalidParameterValueException
    ConfigService.Client.exceptions.MaxNumberOfConformancePacksExceededException
    
    """
    pass

def put_delivery_channel(DeliveryChannel=None):
    """
    Creates a delivery channel object to deliver configuration information to an Amazon S3 bucket and Amazon SNS topic.
    Before you can create a delivery channel, you must create a configuration recorder.
    You can use this action to change the Amazon S3 bucket or an Amazon SNS topic of the existing delivery channel. To change the Amazon S3 bucket or an Amazon SNS topic, call this action and specify the changed values for the S3 bucket and the SNS topic. If you specify a different value for either the S3 bucket or the SNS topic, this action will keep the existing value for the parameter that is not changed.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param DeliveryChannel: [REQUIRED]\nThe configuration delivery channel object that delivers the configuration information to an Amazon S3 bucket and to an Amazon SNS topic.\n\nname (string) --The name of the delivery channel. By default, AWS Config assigns the name 'default' when creating the delivery channel. To change the delivery channel name, you must use the DeleteDeliveryChannel action to delete your current delivery channel, and then you must use the PutDeliveryChannel command to create a delivery channel that has the desired name.\n\ns3BucketName (string) --The name of the Amazon S3 bucket to which AWS Config delivers configuration snapshots and configuration history files.\nIf you specify a bucket that belongs to another AWS account, that bucket must have policies that grant access permissions to AWS Config. For more information, see Permissions for the Amazon S3 Bucket in the AWS Config Developer Guide.\n\ns3KeyPrefix (string) --The prefix for the specified Amazon S3 bucket.\n\nsnsTopicARN (string) --The Amazon Resource Name (ARN) of the Amazon SNS topic to which AWS Config sends notifications about configuration changes.\nIf you choose a topic from another account, the topic must have policies that grant access permissions to AWS Config. For more information, see Permissions for the Amazon SNS Topic in the AWS Config Developer Guide.\n\nconfigSnapshotDeliveryProperties (dict) --The options for how often AWS Config delivers configuration snapshots to the Amazon S3 bucket.\n\ndeliveryFrequency (string) --The frequency with which AWS Config delivers configuration snapshots.\n\n\n\n\n

    """
    pass

def put_evaluations(Evaluations=None, ResultToken=None, TestMode=None):
    """
    Used by an AWS Lambda function to deliver evaluation results to AWS Config. This action is required in every AWS Lambda function that is invoked by an AWS Config rule.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param Evaluations: The assessments that the AWS Lambda function performs. Each evaluation identifies an AWS resource and indicates whether it complies with the AWS Config rule that invokes the AWS Lambda function.\n\n(dict) --Identifies an AWS resource and indicates whether it complies with the AWS Config rule that it was evaluated against.\n\nComplianceResourceType (string) -- [REQUIRED]The type of AWS resource that was evaluated.\n\nComplianceResourceId (string) -- [REQUIRED]The ID of the AWS resource that was evaluated.\n\nComplianceType (string) -- [REQUIRED]Indicates whether the AWS resource complies with the AWS Config rule that it was evaluated against.\nFor the Evaluation data type, AWS Config supports only the COMPLIANT , NON_COMPLIANT , and NOT_APPLICABLE values. AWS Config does not support the INSUFFICIENT_DATA value for this data type.\nSimilarly, AWS Config does not accept INSUFFICIENT_DATA as the value for ComplianceType from a PutEvaluations request. For example, an AWS Lambda function for a custom AWS Config rule cannot pass an INSUFFICIENT_DATA value to AWS Config.\n\nAnnotation (string) --Supplementary information about how the evaluation determined the compliance.\n\nOrderingTimestamp (datetime) -- [REQUIRED]The time of the event in AWS Config that triggered the evaluation. For event-based evaluations, the time indicates when AWS Config created the configuration item that triggered the evaluation. For periodic evaluations, the time indicates when AWS Config triggered the evaluation at the frequency that you specified (for example, every 24 hours).\n\n\n\n\n

    :type ResultToken: string
    :param ResultToken: [REQUIRED]\nAn encrypted token that associates an evaluation with an AWS Config rule. Identifies the rule and the event that triggered the evaluation.\n

    :type TestMode: boolean
    :param TestMode: Use this parameter to specify a test run for PutEvaluations . You can verify whether your AWS Lambda function will deliver evaluation results to AWS Config. No updates occur to your existing evaluations, and evaluation results are not sent to AWS Config.\n\nNote\nWhen TestMode is true , PutEvaluations doesn\'t require a valid value for the ResultToken parameter, but the value cannot be null.\n\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

FailedEvaluations (list) --
Requests that failed because of a client or server error.

(dict) --
Identifies an AWS resource and indicates whether it complies with the AWS Config rule that it was evaluated against.

ComplianceResourceType (string) --
The type of AWS resource that was evaluated.

ComplianceResourceId (string) --
The ID of the AWS resource that was evaluated.

ComplianceType (string) --
Indicates whether the AWS resource complies with the AWS Config rule that it was evaluated against.
For the Evaluation data type, AWS Config supports only the COMPLIANT , NON_COMPLIANT , and NOT_APPLICABLE values. AWS Config does not support the INSUFFICIENT_DATA value for this data type.
Similarly, AWS Config does not accept INSUFFICIENT_DATA as the value for ComplianceType from a PutEvaluations request. For example, an AWS Lambda function for a custom AWS Config rule cannot pass an INSUFFICIENT_DATA value to AWS Config.

Annotation (string) --
Supplementary information about how the evaluation determined the compliance.

OrderingTimestamp (datetime) --
The time of the event in AWS Config that triggered the evaluation. For event-based evaluations, the time indicates when AWS Config created the configuration item that triggered the evaluation. For periodic evaluations, the time indicates when AWS Config triggered the evaluation at the frequency that you specified (for example, every 24 hours).











Exceptions

ConfigService.Client.exceptions.InvalidParameterValueException
ConfigService.Client.exceptions.InvalidResultTokenException
ConfigService.Client.exceptions.NoSuchConfigRuleException


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
    
    
    :returns: 
    ConfigService.Client.exceptions.InvalidParameterValueException
    ConfigService.Client.exceptions.InvalidResultTokenException
    ConfigService.Client.exceptions.NoSuchConfigRuleException
    
    """
    pass

def put_organization_config_rule(OrganizationConfigRuleName=None, OrganizationManagedRuleMetadata=None, OrganizationCustomRuleMetadata=None, ExcludedAccounts=None):
    """
    Adds or updates organization config rule for your entire organization evaluating whether your AWS resources comply with your desired configurations. Only a master account can create or update an organization config rule.
    This API enables organization service access through the EnableAWSServiceAccess action and creates a service linked role AWSServiceRoleForConfigMultiAccountSetup in the master account of your organization. The service linked role is created only when the role does not exist in the master account. AWS Config verifies the existence of role with GetRole action.
    You can use this action to create both custom AWS Config rules and AWS managed Config rules. If you are adding a new custom AWS Config rule, you must first create AWS Lambda function in the master account that the rule invokes to evaluate your resources. When you use the PutOrganizationConfigRule action to add the rule to AWS Config, you must specify the Amazon Resource Name (ARN) that AWS Lambda assigns to the function. If you are adding an AWS managed Config rule, specify the rule\'s identifier for the RuleIdentifier key.
    The maximum number of organization config rules that AWS Config supports is 150.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_organization_config_rule(
        OrganizationConfigRuleName='string',
        OrganizationManagedRuleMetadata={
            'Description': 'string',
            'RuleIdentifier': 'string',
            'InputParameters': 'string',
            'MaximumExecutionFrequency': 'One_Hour'|'Three_Hours'|'Six_Hours'|'Twelve_Hours'|'TwentyFour_Hours',
            'ResourceTypesScope': [
                'string',
            ],
            'ResourceIdScope': 'string',
            'TagKeyScope': 'string',
            'TagValueScope': 'string'
        },
        OrganizationCustomRuleMetadata={
            'Description': 'string',
            'LambdaFunctionArn': 'string',
            'OrganizationConfigRuleTriggerTypes': [
                'ConfigurationItemChangeNotification'|'OversizedConfigurationItemChangeNotification'|'ScheduledNotification',
            ],
            'InputParameters': 'string',
            'MaximumExecutionFrequency': 'One_Hour'|'Three_Hours'|'Six_Hours'|'Twelve_Hours'|'TwentyFour_Hours',
            'ResourceTypesScope': [
                'string',
            ],
            'ResourceIdScope': 'string',
            'TagKeyScope': 'string',
            'TagValueScope': 'string'
        },
        ExcludedAccounts=[
            'string',
        ]
    )
    
    
    :type OrganizationConfigRuleName: string
    :param OrganizationConfigRuleName: [REQUIRED]\nThe name that you assign to an organization config rule.\n

    :type OrganizationManagedRuleMetadata: dict
    :param OrganizationManagedRuleMetadata: An OrganizationManagedRuleMetadata object.\n\nDescription (string) --The description that you provide for organization config rule.\n\nRuleIdentifier (string) -- [REQUIRED]For organization config managed rules, a predefined identifier from a list. For example, IAM_PASSWORD_POLICY is a managed rule. To reference a managed rule, see Using AWS Managed Config Rules .\n\nInputParameters (string) --A string, in JSON format, that is passed to organization config rule Lambda function.\n\nMaximumExecutionFrequency (string) --The maximum frequency with which AWS Config runs evaluations for a rule. You are using an AWS managed rule that is triggered at a periodic frequency.\n\nNote\nBy default, rules with a periodic trigger are evaluated every 24 hours. To change the frequency, specify a valid value for the MaximumExecutionFrequency parameter.\n\n\nResourceTypesScope (list) --The type of the AWS resource that was evaluated.\n\n(string) --\n\n\nResourceIdScope (string) --The ID of the AWS resource that was evaluated.\n\nTagKeyScope (string) --One part of a key-value pair that make up a tag. A key is a general label that acts like a category for more specific tag values.\n\nTagValueScope (string) --The optional part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key).\n\n\n

    :type OrganizationCustomRuleMetadata: dict
    :param OrganizationCustomRuleMetadata: An OrganizationCustomRuleMetadata object.\n\nDescription (string) --The description that you provide for organization config rule.\n\nLambdaFunctionArn (string) -- [REQUIRED]The lambda function ARN.\n\nOrganizationConfigRuleTriggerTypes (list) -- [REQUIRED]The type of notification that triggers AWS Config to run an evaluation for a rule. You can specify the following notification types:\n\nConfigurationItemChangeNotification - Triggers an evaluation when AWS Config delivers a configuration item as a result of a resource change.\nOversizedConfigurationItemChangeNotification - Triggers an evaluation when AWS Config delivers an oversized configuration item. AWS Config may generate this notification type when a resource changes and the notification exceeds the maximum size allowed by Amazon SNS.\nScheduledNotification - Triggers a periodic evaluation at the frequency specified for MaximumExecutionFrequency .\n\n\n(string) --\n\n\nInputParameters (string) --A string, in JSON format, that is passed to organization config rule Lambda function.\n\nMaximumExecutionFrequency (string) --The maximum frequency with which AWS Config runs evaluations for a rule. Your custom rule is triggered when AWS Config delivers the configuration snapshot. For more information, see ConfigSnapshotDeliveryProperties .\n\nNote\nBy default, rules with a periodic trigger are evaluated every 24 hours. To change the frequency, specify a valid value for the MaximumExecutionFrequency parameter.\n\n\nResourceTypesScope (list) --The type of the AWS resource that was evaluated.\n\n(string) --\n\n\nResourceIdScope (string) --The ID of the AWS resource that was evaluated.\n\nTagKeyScope (string) --One part of a key-value pair that make up a tag. A key is a general label that acts like a category for more specific tag values.\n\nTagValueScope (string) --The optional part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key).\n\n\n

    :type ExcludedAccounts: list
    :param ExcludedAccounts: A comma-separated list of accounts that you want to exclude from an organization config rule.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'OrganizationConfigRuleArn': 'string'
}


Response Structure

(dict) --

OrganizationConfigRuleArn (string) --
The Amazon Resource Name (ARN) of an organization config rule.







Exceptions

ConfigService.Client.exceptions.MaxNumberOfOrganizationConfigRulesExceededException
ConfigService.Client.exceptions.ResourceInUseException
ConfigService.Client.exceptions.InvalidParameterValueException
ConfigService.Client.exceptions.ValidationException
ConfigService.Client.exceptions.OrganizationAccessDeniedException
ConfigService.Client.exceptions.NoAvailableOrganizationException
ConfigService.Client.exceptions.OrganizationAllFeaturesNotEnabledException
ConfigService.Client.exceptions.InsufficientPermissionsException


    :return: {
        'OrganizationConfigRuleArn': 'string'
    }
    
    
    :returns: 
    ConfigService.Client.exceptions.MaxNumberOfOrganizationConfigRulesExceededException
    ConfigService.Client.exceptions.ResourceInUseException
    ConfigService.Client.exceptions.InvalidParameterValueException
    ConfigService.Client.exceptions.ValidationException
    ConfigService.Client.exceptions.OrganizationAccessDeniedException
    ConfigService.Client.exceptions.NoAvailableOrganizationException
    ConfigService.Client.exceptions.OrganizationAllFeaturesNotEnabledException
    ConfigService.Client.exceptions.InsufficientPermissionsException
    
    """
    pass

def put_organization_conformance_pack(OrganizationConformancePackName=None, TemplateS3Uri=None, TemplateBody=None, DeliveryS3Bucket=None, DeliveryS3KeyPrefix=None, ConformancePackInputParameters=None, ExcludedAccounts=None):
    """
    Deploys conformance packs across member accounts in an AWS Organization.
    This API enables organization service access for config-multiaccountsetup.amazonaws.com through the EnableAWSServiceAccess action and creates a service linked role AWSServiceRoleForConfigMultiAccountSetup in the master account of your organization. The service linked role is created only when the role does not exist in the master account. AWS Config verifies the existence of role with GetRole action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_organization_conformance_pack(
        OrganizationConformancePackName='string',
        TemplateS3Uri='string',
        TemplateBody='string',
        DeliveryS3Bucket='string',
        DeliveryS3KeyPrefix='string',
        ConformancePackInputParameters=[
            {
                'ParameterName': 'string',
                'ParameterValue': 'string'
            },
        ],
        ExcludedAccounts=[
            'string',
        ]
    )
    
    
    :type OrganizationConformancePackName: string
    :param OrganizationConformancePackName: [REQUIRED]\nName of the organization conformance pack you want to create.\n

    :type TemplateS3Uri: string
    :param TemplateS3Uri: Location of file containing the template body. The uri must point to the conformance pack template (max size: 300 KB).\n\nNote\nYou must have access to read Amazon S3 bucket.\n\n

    :type TemplateBody: string
    :param TemplateBody: A string containing full conformance pack template body. Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes.

    :type DeliveryS3Bucket: string
    :param DeliveryS3Bucket: [REQUIRED]\nLocation of an Amazon S3 bucket where AWS Config can deliver evaluation results. AWS Config stores intermediate files while processing conformance pack template.\nThe delivery bucket name should start with awsconfigconforms. For example: 'Resource': 'arn:aws:s3:::your_bucket_name/*'. For more information, see Permissions for cross account bucket access .\n

    :type DeliveryS3KeyPrefix: string
    :param DeliveryS3KeyPrefix: The prefix for the Amazon S3 bucket.

    :type ConformancePackInputParameters: list
    :param ConformancePackInputParameters: A list of ConformancePackInputParameter objects.\n\n(dict) --Input parameters in the form of key-value pairs for the conformance pack, both of which you define. Keys can have a maximum character length of 128 characters, and values can have a maximum length of 256 characters.\n\nParameterName (string) -- [REQUIRED]One part of a key-value pair.\n\nParameterValue (string) -- [REQUIRED]Another part of the key-value pair.\n\n\n\n\n

    :type ExcludedAccounts: list
    :param ExcludedAccounts: A list of AWS accounts to be excluded from an organization conformance pack while deploying a conformance pack.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'OrganizationConformancePackArn': 'string'
}


Response Structure

(dict) --

OrganizationConformancePackArn (string) --
ARN of the organization conformance pack.







Exceptions

ConfigService.Client.exceptions.MaxNumberOfOrganizationConformancePacksExceededException
ConfigService.Client.exceptions.ResourceInUseException
ConfigService.Client.exceptions.ValidationException
ConfigService.Client.exceptions.OrganizationAccessDeniedException
ConfigService.Client.exceptions.InsufficientPermissionsException
ConfigService.Client.exceptions.OrganizationConformancePackTemplateValidationException
ConfigService.Client.exceptions.OrganizationAllFeaturesNotEnabledException
ConfigService.Client.exceptions.NoAvailableOrganizationException


    :return: {
        'OrganizationConformancePackArn': 'string'
    }
    
    
    :returns: 
    ConfigService.Client.exceptions.MaxNumberOfOrganizationConformancePacksExceededException
    ConfigService.Client.exceptions.ResourceInUseException
    ConfigService.Client.exceptions.ValidationException
    ConfigService.Client.exceptions.OrganizationAccessDeniedException
    ConfigService.Client.exceptions.InsufficientPermissionsException
    ConfigService.Client.exceptions.OrganizationConformancePackTemplateValidationException
    ConfigService.Client.exceptions.OrganizationAllFeaturesNotEnabledException
    ConfigService.Client.exceptions.NoAvailableOrganizationException
    
    """
    pass

def put_remediation_configurations(RemediationConfigurations=None):
    """
    Adds or updates the remediation configuration with a specific AWS Config rule with the selected target or action. The API creates the RemediationConfiguration object for the AWS Config rule. The AWS Config rule must already exist for you to add a remediation configuration. The target (SSM document) must exist and have permissions to use the target.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_remediation_configurations(
        RemediationConfigurations=[
            {
                'ConfigRuleName': 'string',
                'TargetType': 'SSM_DOCUMENT',
                'TargetId': 'string',
                'TargetVersion': 'string',
                'Parameters': {
                    'string': {
                        'ResourceValue': {
                            'Value': 'RESOURCE_ID'
                        },
                        'StaticValue': {
                            'Values': [
                                'string',
                            ]
                        }
                    }
                },
                'ResourceType': 'string',
                'Automatic': True|False,
                'ExecutionControls': {
                    'SsmControls': {
                        'ConcurrentExecutionRatePercentage': 123,
                        'ErrorPercentage': 123
                    }
                },
                'MaximumAutomaticAttempts': 123,
                'RetryAttemptSeconds': 123,
                'Arn': 'string',
                'CreatedByService': 'string'
            },
        ]
    )
    
    
    :type RemediationConfigurations: list
    :param RemediationConfigurations: [REQUIRED]\nA list of remediation configuration objects.\n\n(dict) --An object that represents the details about the remediation configuration that includes the remediation action, parameters, and data to execute the action.\n\nConfigRuleName (string) -- [REQUIRED]The name of the AWS Config rule.\n\nTargetType (string) -- [REQUIRED]The type of the target. Target executes remediation. For example, SSM document.\n\nTargetId (string) -- [REQUIRED]Target ID is the name of the public document.\n\nTargetVersion (string) --Version of the target. For example, version of the SSM document.\n\nParameters (dict) --An object of the RemediationParameterValue.\n\n(string) --\n(dict) --The value is either a dynamic (resource) value or a static value. You must select either a dynamic value or a static value.\n\nResourceValue (dict) --The value is dynamic and changes at run-time.\n\nValue (string) -- [REQUIRED]The value is a resource ID.\n\n\n\nStaticValue (dict) --The value is static and does not change at run-time.\n\nValues (list) -- [REQUIRED]A list of values. For example, the ARN of the assumed role.\n\n(string) --\n\n\n\n\n\n\n\n\n\n\nResourceType (string) --The type of a resource.\n\nAutomatic (boolean) --The remediation is triggered automatically.\n\nExecutionControls (dict) --An ExecutionControls object.\n\nSsmControls (dict) --A SsmControls object.\n\nConcurrentExecutionRatePercentage (integer) --The maximum percentage of remediation actions allowed to run in parallel on the non-compliant resources for that specific rule. You can specify a percentage, such as 10%. The default value is 10.\n\nErrorPercentage (integer) --The percentage of errors that are allowed before SSM stops running automations on non-compliant resources for that specific rule. You can specify a percentage of errors, for example 10%. If you do not specifiy a percentage, the default is 50%. For example, if you set the ErrorPercentage to 40% for 10 non-compliant resources, then SSM stops running the automations when the fifth error is received.\n\n\n\n\n\nMaximumAutomaticAttempts (integer) --The maximum number of failed attempts for auto-remediation. If you do not select a number, the default is 5.\nFor example, if you specify MaximumAutomaticAttempts as 5 with RetryAttemptsSeconds as 50 seconds, AWS Config throws an exception after the 5th failed attempt within 50 seconds.\n\nRetryAttemptSeconds (integer) --Maximum time in seconds that AWS Config runs auto-remediation. If you do not select a number, the default is 60 seconds.\nFor example, if you specify RetryAttemptsSeconds as 50 seconds and MaximumAutomaticAttempts as 5, AWS Config will run auto-remediations 5 times within 50 seconds before throwing an exception.\n\nArn (string) --Amazon Resource Name (ARN) of remediation configuration.\n\nCreatedByService (string) --Name of the service that owns the service linked rule, if applicable.\n\n\n\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'FailedBatches': [
        {
            'FailureMessage': 'string',
            'FailedItems': [
                {
                    'ConfigRuleName': 'string',
                    'TargetType': 'SSM_DOCUMENT',
                    'TargetId': 'string',
                    'TargetVersion': 'string',
                    'Parameters': {
                        'string': {
                            'ResourceValue': {
                                'Value': 'RESOURCE_ID'
                            },
                            'StaticValue': {
                                'Values': [
                                    'string',
                                ]
                            }
                        }
                    },
                    'ResourceType': 'string',
                    'Automatic': True|False,
                    'ExecutionControls': {
                        'SsmControls': {
                            'ConcurrentExecutionRatePercentage': 123,
                            'ErrorPercentage': 123
                        }
                    },
                    'MaximumAutomaticAttempts': 123,
                    'RetryAttemptSeconds': 123,
                    'Arn': 'string',
                    'CreatedByService': 'string'
                },
            ]
        },
    ]
}


Response Structure

(dict) --
FailedBatches (list) --Returns a list of failed remediation batch objects.

(dict) --List of each of the failed remediations with specific reasons.

FailureMessage (string) --Returns a failure message. For example, the resource is already compliant.

FailedItems (list) --Returns remediation configurations of the failed items.

(dict) --An object that represents the details about the remediation configuration that includes the remediation action, parameters, and data to execute the action.

ConfigRuleName (string) --The name of the AWS Config rule.

TargetType (string) --The type of the target. Target executes remediation. For example, SSM document.

TargetId (string) --Target ID is the name of the public document.

TargetVersion (string) --Version of the target. For example, version of the SSM document.

Parameters (dict) --An object of the RemediationParameterValue.

(string) --
(dict) --The value is either a dynamic (resource) value or a static value. You must select either a dynamic value or a static value.

ResourceValue (dict) --The value is dynamic and changes at run-time.

Value (string) --The value is a resource ID.



StaticValue (dict) --The value is static and does not change at run-time.

Values (list) --A list of values. For example, the ARN of the assumed role.

(string) --










ResourceType (string) --The type of a resource.

Automatic (boolean) --The remediation is triggered automatically.

ExecutionControls (dict) --An ExecutionControls object.

SsmControls (dict) --A SsmControls object.

ConcurrentExecutionRatePercentage (integer) --The maximum percentage of remediation actions allowed to run in parallel on the non-compliant resources for that specific rule. You can specify a percentage, such as 10%. The default value is 10.

ErrorPercentage (integer) --The percentage of errors that are allowed before SSM stops running automations on non-compliant resources for that specific rule. You can specify a percentage of errors, for example 10%. If you do not specifiy a percentage, the default is 50%. For example, if you set the ErrorPercentage to 40% for 10 non-compliant resources, then SSM stops running the automations when the fifth error is received.





MaximumAutomaticAttempts (integer) --The maximum number of failed attempts for auto-remediation. If you do not select a number, the default is 5.
For example, if you specify MaximumAutomaticAttempts as 5 with RetryAttemptsSeconds as 50 seconds, AWS Config throws an exception after the 5th failed attempt within 50 seconds.

RetryAttemptSeconds (integer) --Maximum time in seconds that AWS Config runs auto-remediation. If you do not select a number, the default is 60 seconds.
For example, if you specify RetryAttemptsSeconds as 50 seconds and MaximumAutomaticAttempts as 5, AWS Config will run auto-remediations 5 times within 50 seconds before throwing an exception.

Arn (string) --Amazon Resource Name (ARN) of remediation configuration.

CreatedByService (string) --Name of the service that owns the service linked rule, if applicable.














Exceptions

ConfigService.Client.exceptions.InsufficientPermissionsException
ConfigService.Client.exceptions.InvalidParameterValueException


    :return: {
        'FailedBatches': [
            {
                'FailureMessage': 'string',
                'FailedItems': [
                    {
                        'ConfigRuleName': 'string',
                        'TargetType': 'SSM_DOCUMENT',
                        'TargetId': 'string',
                        'TargetVersion': 'string',
                        'Parameters': {
                            'string': {
                                'ResourceValue': {
                                    'Value': 'RESOURCE_ID'
                                },
                                'StaticValue': {
                                    'Values': [
                                        'string',
                                    ]
                                }
                            }
                        },
                        'ResourceType': 'string',
                        'Automatic': True|False,
                        'ExecutionControls': {
                            'SsmControls': {
                                'ConcurrentExecutionRatePercentage': 123,
                                'ErrorPercentage': 123
                            }
                        },
                        'MaximumAutomaticAttempts': 123,
                        'RetryAttemptSeconds': 123,
                        'Arn': 'string',
                        'CreatedByService': 'string'
                    },
                ]
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def put_remediation_exceptions(ConfigRuleName=None, ResourceKeys=None, Message=None, ExpirationTime=None):
    """
    A remediation exception is when a specific resource is no longer considered for auto-remediation. This API adds a new exception or updates an exisiting exception for a specific resource with a specific AWS Config rule.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_remediation_exceptions(
        ConfigRuleName='string',
        ResourceKeys=[
            {
                'ResourceType': 'string',
                'ResourceId': 'string'
            },
        ],
        Message='string',
        ExpirationTime=datetime(2015, 1, 1)
    )
    
    
    :type ConfigRuleName: string
    :param ConfigRuleName: [REQUIRED]\nThe name of the AWS Config rule for which you want to create remediation exception.\n

    :type ResourceKeys: list
    :param ResourceKeys: [REQUIRED]\nAn exception list of resource exception keys to be processed with the current request. AWS Config adds exception for each resource key. For example, AWS Config adds 3 exceptions for 3 resource keys.\n\n(dict) --The details that identify a resource within AWS Config, including the resource type and resource ID.\n\nResourceType (string) --The type of a resource.\n\nResourceId (string) --The ID of the resource (for example., sg-xxxxxx).\n\n\n\n\n

    :type Message: string
    :param Message: The message contains an explanation of the exception.

    :type ExpirationTime: datetime
    :param ExpirationTime: The exception is automatically deleted after the expiration date.

    :rtype: dict

ReturnsResponse Syntax
{
    'FailedBatches': [
        {
            'FailureMessage': 'string',
            'FailedItems': [
                {
                    'ConfigRuleName': 'string',
                    'ResourceType': 'string',
                    'ResourceId': 'string',
                    'Message': 'string',
                    'ExpirationTime': datetime(2015, 1, 1)
                },
            ]
        },
    ]
}


Response Structure

(dict) --

FailedBatches (list) --
Returns a list of failed remediation exceptions batch objects. Each object in the batch consists of a list of failed items and failure messages.

(dict) --
List of each of the failed remediation exceptions with specific reasons.

FailureMessage (string) --
Returns a failure message. For example, the auto-remediation has failed.

FailedItems (list) --
Returns remediation exception resource key object of the failed items.

(dict) --
An object that represents the details about the remediation exception. The details include the rule name, an explanation of an exception, the time when the exception will be deleted, the resource ID, and resource type.

ConfigRuleName (string) --
The name of the AWS Config rule.

ResourceType (string) --
The type of a resource.

ResourceId (string) --
The ID of the resource (for example., sg-xxxxxx).

Message (string) --
An explanation of an remediation exception.

ExpirationTime (datetime) --
The time when the remediation exception will be deleted.















Exceptions

ConfigService.Client.exceptions.InvalidParameterValueException


    :return: {
        'FailedBatches': [
            {
                'FailureMessage': 'string',
                'FailedItems': [
                    {
                        'ConfigRuleName': 'string',
                        'ResourceType': 'string',
                        'ResourceId': 'string',
                        'Message': 'string',
                        'ExpirationTime': datetime(2015, 1, 1)
                    },
                ]
            },
        ]
    }
    
    
    :returns: 
    ConfigService.Client.exceptions.InvalidParameterValueException
    
    """
    pass

def put_resource_config(ResourceType=None, SchemaVersionId=None, ResourceId=None, ResourceName=None, Configuration=None, Tags=None):
    """
    Records the configuration state for the resource provided in the request. The configuration state of a resource is represented in AWS Config as Configuration Items. Once this API records the configuration item, you can retrieve the list of configuration items for the custom resource type using existing AWS Config APIs.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_resource_config(
        ResourceType='string',
        SchemaVersionId='string',
        ResourceId='string',
        ResourceName='string',
        Configuration='string',
        Tags={
            'string': 'string'
        }
    )
    
    
    :type ResourceType: string
    :param ResourceType: [REQUIRED]\nThe type of the resource. The custom resource type must be registered with AWS CloudFormation.\n\nNote\nYou cannot use the organization names \xe2\x80\x9caws\xe2\x80\x9d, \xe2\x80\x9camzn\xe2\x80\x9d, \xe2\x80\x9camazon\xe2\x80\x9d, \xe2\x80\x9calexa\xe2\x80\x9d, \xe2\x80\x9ccustom\xe2\x80\x9d with custom resource types. It is the first part of the ResourceType up to the first ::.\n\n

    :type SchemaVersionId: string
    :param SchemaVersionId: [REQUIRED]\nVersion of the schema registered for the ResourceType in AWS CloudFormation.\n

    :type ResourceId: string
    :param ResourceId: [REQUIRED]\nUnique identifier of the resource.\n

    :type ResourceName: string
    :param ResourceName: Name of the resource.

    :type Configuration: string
    :param Configuration: [REQUIRED]\nThe configuration object of the resource in valid JSON format. It must match the schema registered with AWS CloudFormation.\n\nNote\nThe configuration JSON must not exceed 64 KB.\n\n

    :type Tags: dict
    :param Tags: Tags associated with the resource.\n\n(string) --\n(string) --\n\n\n\n

    :returns: 
    ConfigService.Client.exceptions.ValidationException
    ConfigService.Client.exceptions.InsufficientPermissionsException
    ConfigService.Client.exceptions.NoRunningConfigurationRecorderException
    ConfigService.Client.exceptions.MaxActiveResourcesExceededException
    
    """
    pass

def put_retention_configuration(RetentionPeriodInDays=None):
    """
    Creates and updates the retention configuration with details about retention period (number of days) that AWS Config stores your historical information. The API creates the RetentionConfiguration object and names the object as default . When you have a RetentionConfiguration object named default , calling the API modifies the default object.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_retention_configuration(
        RetentionPeriodInDays=123
    )
    
    
    :type RetentionPeriodInDays: integer
    :param RetentionPeriodInDays: [REQUIRED]\nNumber of days AWS Config stores your historical information.\n\nNote\nCurrently, only applicable to the configuration item history.\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'RetentionConfiguration': {
        'Name': 'string',
        'RetentionPeriodInDays': 123
    }
}


Response Structure

(dict) --
RetentionConfiguration (dict) --Returns a retention configuration object.

Name (string) --The name of the retention configuration object.

RetentionPeriodInDays (integer) --Number of days AWS Config stores your historical information.

Note
Currently, only applicable to the configuration item history.









Exceptions

ConfigService.Client.exceptions.InvalidParameterValueException
ConfigService.Client.exceptions.MaxNumberOfRetentionConfigurationsExceededException


    :return: {
        'RetentionConfiguration': {
            'Name': 'string',
            'RetentionPeriodInDays': 123
        }
    }
    
    
    """
    pass

def select_aggregate_resource_config(Expression=None, ConfigurationAggregatorName=None, Limit=None, MaxResults=None, NextToken=None):
    """
    Accepts a structured query language (SQL) SELECT command and an aggregator to query configuration state of AWS resources across multiple accounts and regions, performs the corresponding search, and returns resource configurations matching the properties.
    For more information about query components, see the ` Query Components https://docs.aws.amazon.com/config/latest/developerguide/query-components.html`__ section in the AWS Config Developer Guide.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.select_aggregate_resource_config(
        Expression='string',
        ConfigurationAggregatorName='string',
        Limit=123,
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type Expression: string
    :param Expression: [REQUIRED]\nThe SQL query SELECT command.\n

    :type ConfigurationAggregatorName: string
    :param ConfigurationAggregatorName: [REQUIRED]\nThe name of the configuration aggregator.\n

    :type Limit: integer
    :param Limit: The maximum number of query results returned on each page.

    :type MaxResults: integer
    :param MaxResults: 

    :type NextToken: string
    :param NextToken: The nextToken string returned in a previous request that you use to request the next page of results in a paginated response.

    :rtype: dict

ReturnsResponse Syntax
{
    'Results': [
        'string',
    ],
    'QueryInfo': {
        'SelectFields': [
            {
                'Name': 'string'
            },
        ]
    },
    'NextToken': 'string'
}


Response Structure

(dict) --

Results (list) --
Returns the results for the SQL query.

(string) --


QueryInfo (dict) --
Details about the query.

SelectFields (list) --
Returns a FieldInfo object.

(dict) --
Details about the fields such as name of the field.

Name (string) --
Name of the field.







NextToken (string) --
The nextToken string returned in a previous request that you use to request the next page of results in a paginated response.







Exceptions

ConfigService.Client.exceptions.InvalidExpressionException
ConfigService.Client.exceptions.NoSuchConfigurationAggregatorException
ConfigService.Client.exceptions.InvalidLimitException
ConfigService.Client.exceptions.InvalidNextTokenException


    :return: {
        'Results': [
            'string',
        ],
        'QueryInfo': {
            'SelectFields': [
                {
                    'Name': 'string'
                },
            ]
        },
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def select_resource_config(Expression=None, Limit=None, NextToken=None):
    """
    Accepts a structured query language (SQL) SELECT command, performs the corresponding search, and returns resource configurations matching the properties.
    For more information about query components, see the ` Query Components https://docs.aws.amazon.com/config/latest/developerguide/query-components.html`__ section in the AWS Config Developer Guide.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.select_resource_config(
        Expression='string',
        Limit=123,
        NextToken='string'
    )
    
    
    :type Expression: string
    :param Expression: [REQUIRED]\nThe SQL query SELECT command.\n

    :type Limit: integer
    :param Limit: The maximum number of query results returned on each page.

    :type NextToken: string
    :param NextToken: The nextToken string returned in a previous request that you use to request the next page of results in a paginated response.

    :rtype: dict

ReturnsResponse Syntax
{
    'Results': [
        'string',
    ],
    'QueryInfo': {
        'SelectFields': [
            {
                'Name': 'string'
            },
        ]
    },
    'NextToken': 'string'
}


Response Structure

(dict) --

Results (list) --
Returns the results for the SQL query.

(string) --


QueryInfo (dict) --
Returns the QueryInfo object.

SelectFields (list) --
Returns a FieldInfo object.

(dict) --
Details about the fields such as name of the field.

Name (string) --
Name of the field.







NextToken (string) --
The nextToken string returned in a previous request that you use to request the next page of results in a paginated response.







Exceptions

ConfigService.Client.exceptions.InvalidExpressionException
ConfigService.Client.exceptions.InvalidLimitException
ConfigService.Client.exceptions.InvalidNextTokenException


    :return: {
        'Results': [
            'string',
        ],
        'QueryInfo': {
            'SelectFields': [
                {
                    'Name': 'string'
                },
            ]
        },
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def start_config_rules_evaluation(ConfigRuleNames=None):
    """
    Runs an on-demand evaluation for the specified AWS Config rules against the last known configuration state of the resources. Use StartConfigRulesEvaluation when you want to test that a rule you updated is working as expected. StartConfigRulesEvaluation does not re-record the latest configuration state for your resources. It re-runs an evaluation against the last known state of your resources.
    You can specify up to 25 AWS Config rules per request.
    An existing StartConfigRulesEvaluation call for the specified rules must complete before you can call the API again. If you chose to have AWS Config stream to an Amazon SNS topic, you will receive a ConfigRuleEvaluationStarted notification when the evaluation starts.
    The StartConfigRulesEvaluation API is useful if you want to run on-demand evaluations, such as the following example:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_config_rules_evaluation(
        ConfigRuleNames=[
            'string',
        ]
    )
    
    
    :type ConfigRuleNames: list
    :param ConfigRuleNames: The list of names of AWS Config rules that you want to run evaluations for.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --The output when you start the evaluation for the specified AWS Config rule.




Exceptions

ConfigService.Client.exceptions.NoSuchConfigRuleException
ConfigService.Client.exceptions.LimitExceededException
ConfigService.Client.exceptions.ResourceInUseException
ConfigService.Client.exceptions.InvalidParameterValueException


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
    
    Exceptions
    
    :example: response = client.start_configuration_recorder(
        ConfigurationRecorderName='string'
    )
    
    
    :type ConfigurationRecorderName: string
    :param ConfigurationRecorderName: [REQUIRED]\nThe name of the recorder object that records each configuration change made to the resources.\n

    """
    pass

def start_remediation_execution(ConfigRuleName=None, ResourceKeys=None):
    """
    Runs an on-demand remediation for the specified AWS Config rules against the last known remediation configuration. It runs an execution against the current state of your resources. Remediation execution is asynchronous.
    You can specify up to 100 resource keys per request. An existing StartRemediationExecution call for the specified resource keys must complete before you can call the API again.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_remediation_execution(
        ConfigRuleName='string',
        ResourceKeys=[
            {
                'resourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::EC2::RegisteredHAInstance'|'AWS::EC2::NatGateway'|'AWS::EC2::EgressOnlyInternetGateway'|'AWS::EC2::VPCEndpoint'|'AWS::EC2::VPCEndpointService'|'AWS::EC2::FlowLog'|'AWS::EC2::VPCPeeringConnection'|'AWS::Elasticsearch::Domain'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::DBCluster'|'AWS::RDS::DBClusterSnapshot'|'AWS::RDS::EventSubscription'|'AWS::S3::Bucket'|'AWS::S3::AccountPublicAccessBlock'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::SSM::ManagedInstanceInventory'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::DynamoDB::Table'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::RuleGroup'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::RuleGroup'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::WAFv2::WebACL'|'AWS::WAFv2::RuleGroup'|'AWS::WAFv2::IPSet'|'AWS::WAFv2::RegexPatternSet'|'AWS::WAFv2::ManagedRuleSet'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::ApiGateway::Stage'|'AWS::ApiGateway::RestApi'|'AWS::ApiGatewayV2::Stage'|'AWS::ApiGatewayV2::Api'|'AWS::CodePipeline::Pipeline'|'AWS::ServiceCatalog::CloudFormationProvisionedProduct'|'AWS::ServiceCatalog::CloudFormationProduct'|'AWS::ServiceCatalog::Portfolio'|'AWS::SQS::Queue'|'AWS::KMS::Key'|'AWS::QLDB::Ledger',
                'resourceId': 'string'
            },
        ]
    )
    
    
    :type ConfigRuleName: string
    :param ConfigRuleName: [REQUIRED]\nThe list of names of AWS Config rules that you want to run remediation execution for.\n

    :type ResourceKeys: list
    :param ResourceKeys: [REQUIRED]\nA list of resource keys to be processed with the current request. Each element in the list consists of the resource type and resource ID.\n\n(dict) --The details that identify a resource within AWS Config, including the resource type and resource ID.\n\nresourceType (string) -- [REQUIRED]The resource type.\n\nresourceId (string) -- [REQUIRED]The ID of the resource (for example., sg-xxxxxx).\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'FailureMessage': 'string',
    'FailedItems': [
        {
            'resourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::EC2::RegisteredHAInstance'|'AWS::EC2::NatGateway'|'AWS::EC2::EgressOnlyInternetGateway'|'AWS::EC2::VPCEndpoint'|'AWS::EC2::VPCEndpointService'|'AWS::EC2::FlowLog'|'AWS::EC2::VPCPeeringConnection'|'AWS::Elasticsearch::Domain'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::DBCluster'|'AWS::RDS::DBClusterSnapshot'|'AWS::RDS::EventSubscription'|'AWS::S3::Bucket'|'AWS::S3::AccountPublicAccessBlock'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::SSM::ManagedInstanceInventory'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::DynamoDB::Table'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::RuleGroup'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::RuleGroup'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::WAFv2::WebACL'|'AWS::WAFv2::RuleGroup'|'AWS::WAFv2::IPSet'|'AWS::WAFv2::RegexPatternSet'|'AWS::WAFv2::ManagedRuleSet'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::ApiGateway::Stage'|'AWS::ApiGateway::RestApi'|'AWS::ApiGatewayV2::Stage'|'AWS::ApiGatewayV2::Api'|'AWS::CodePipeline::Pipeline'|'AWS::ServiceCatalog::CloudFormationProvisionedProduct'|'AWS::ServiceCatalog::CloudFormationProduct'|'AWS::ServiceCatalog::Portfolio'|'AWS::SQS::Queue'|'AWS::KMS::Key'|'AWS::QLDB::Ledger',
            'resourceId': 'string'
        },
    ]
}


Response Structure

(dict) --

FailureMessage (string) --
Returns a failure message. For example, the resource is already compliant.

FailedItems (list) --
For resources that have failed to start execution, the API returns a resource key object.

(dict) --
The details that identify a resource within AWS Config, including the resource type and resource ID.

resourceType (string) --
The resource type.

resourceId (string) --
The ID of the resource (for example., sg-xxxxxx).











Exceptions

ConfigService.Client.exceptions.InvalidParameterValueException
ConfigService.Client.exceptions.InsufficientPermissionsException
ConfigService.Client.exceptions.NoSuchRemediationConfigurationException


    :return: {
        'FailureMessage': 'string',
        'FailedItems': [
            {
                'resourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::EC2::RegisteredHAInstance'|'AWS::EC2::NatGateway'|'AWS::EC2::EgressOnlyInternetGateway'|'AWS::EC2::VPCEndpoint'|'AWS::EC2::VPCEndpointService'|'AWS::EC2::FlowLog'|'AWS::EC2::VPCPeeringConnection'|'AWS::Elasticsearch::Domain'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::DBCluster'|'AWS::RDS::DBClusterSnapshot'|'AWS::RDS::EventSubscription'|'AWS::S3::Bucket'|'AWS::S3::AccountPublicAccessBlock'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::SSM::ManagedInstanceInventory'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::DynamoDB::Table'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::RuleGroup'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::RuleGroup'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::Lambda::Function'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::WAFv2::WebACL'|'AWS::WAFv2::RuleGroup'|'AWS::WAFv2::IPSet'|'AWS::WAFv2::RegexPatternSet'|'AWS::WAFv2::ManagedRuleSet'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ResourceCompliance'|'AWS::ApiGateway::Stage'|'AWS::ApiGateway::RestApi'|'AWS::ApiGatewayV2::Stage'|'AWS::ApiGatewayV2::Api'|'AWS::CodePipeline::Pipeline'|'AWS::ServiceCatalog::CloudFormationProvisionedProduct'|'AWS::ServiceCatalog::CloudFormationProduct'|'AWS::ServiceCatalog::Portfolio'|'AWS::SQS::Queue'|'AWS::KMS::Key'|'AWS::QLDB::Ledger',
                'resourceId': 'string'
            },
        ]
    }
    
    
    :returns: 
    ConfigService.Client.exceptions.InvalidParameterValueException
    ConfigService.Client.exceptions.InsufficientPermissionsException
    ConfigService.Client.exceptions.NoSuchRemediationConfigurationException
    
    """
    pass

def stop_configuration_recorder(ConfigurationRecorderName=None):
    """
    Stops recording configurations of the AWS resources you have selected to record in your AWS account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.stop_configuration_recorder(
        ConfigurationRecorderName='string'
    )
    
    
    :type ConfigurationRecorderName: string
    :param ConfigurationRecorderName: [REQUIRED]\nThe name of the recorder object that records each configuration change made to the resources.\n

    """
    pass

def tag_resource(ResourceArn=None, Tags=None):
    """
    Associates the specified tags to a resource with the specified resourceArn. If existing tags on a resource are not specified in the request parameters, they are not changed. When a resource is deleted, the tags associated with that resource are deleted as well.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        ResourceArn='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that identifies the resource for which to list the tags. Currently, the supported resources are ConfigRule , ConfigurationAggregator and AggregatorAuthorization .\n

    :type Tags: list
    :param Tags: [REQUIRED]\nAn array of tag object.\n\n(dict) --The tags for the resource. The metadata that you apply to a resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.\n\nKey (string) --One part of a key-value pair that make up a tag. A key is a general label that acts like a category for more specific tag values.\n\nValue (string) --The optional part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key).\n\n\n\n\n

    :returns: 
    ConfigService.Client.exceptions.ValidationException
    ConfigService.Client.exceptions.ResourceNotFoundException
    ConfigService.Client.exceptions.TooManyTagsException
    
    """
    pass

def untag_resource(ResourceArn=None, TagKeys=None):
    """
    Deletes specified tags from a resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        ResourceArn='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that identifies the resource for which to list the tags. Currently, the supported resources are ConfigRule , ConfigurationAggregator and AggregatorAuthorization .\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nThe keys of the tags to be removed.\n\n(string) --\n\n

    :returns: 
    ConfigService.Client.exceptions.ValidationException
    ConfigService.Client.exceptions.ResourceNotFoundException
    
    """
    pass

