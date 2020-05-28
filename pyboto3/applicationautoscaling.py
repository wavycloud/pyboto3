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

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def delete_scaling_policy(PolicyName=None, ServiceNamespace=None, ResourceId=None, ScalableDimension=None):
    """
    Deletes the specified scaling policy for an Application Auto Scaling scalable target.
    Deleting a step scaling policy deletes the underlying alarm action, but does not delete the CloudWatch alarm associated with the scaling policy, even if it no longer has an associated action.
    For more information, see Delete a Step Scaling Policy and Delete a Target Tracking Scaling Policy in the Application Auto Scaling User Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example deletes a scaling policy for the Amazon ECS service called web-app, which is running in the default cluster.
    Expected Output:
    
    :example: response = client.delete_scaling_policy(
        PolicyName='string',
        ServiceNamespace='ecs'|'elasticmapreduce'|'ec2'|'appstream'|'dynamodb'|'rds'|'sagemaker'|'custom-resource'|'comprehend'|'lambda'|'cassandra',
        ResourceId='string',
        ScalableDimension='ecs:service:DesiredCount'|'ec2:spot-fleet-request:TargetCapacity'|'elasticmapreduce:instancegroup:InstanceCount'|'appstream:fleet:DesiredCapacity'|'dynamodb:table:ReadCapacityUnits'|'dynamodb:table:WriteCapacityUnits'|'dynamodb:index:ReadCapacityUnits'|'dynamodb:index:WriteCapacityUnits'|'rds:cluster:ReadReplicaCount'|'sagemaker:variant:DesiredInstanceCount'|'custom-resource:ResourceType:Property'|'comprehend:document-classifier-endpoint:DesiredInferenceUnits'|'lambda:function:ProvisionedConcurrency'|'cassandra:table:ReadCapacityUnits'|'cassandra:table:WriteCapacityUnits'
    )
    
    
    :type PolicyName: string
    :param PolicyName: [REQUIRED]\nThe name of the scaling policy.\n

    :type ServiceNamespace: string
    :param ServiceNamespace: [REQUIRED]\nThe namespace of the AWS service that provides the resource. For a resource provided by your own application or service, use custom-resource instead.\n

    :type ResourceId: string
    :param ResourceId: [REQUIRED]\nThe identifier of the resource associated with the scalable target. This string consists of the resource type and unique identifier.\n\nECS service - The resource type is service and the unique identifier is the cluster name and service name. Example: service/default/sample-webapp .\nSpot Fleet request - The resource type is spot-fleet-request and the unique identifier is the Spot Fleet request ID. Example: spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE .\nEMR cluster - The resource type is instancegroup and the unique identifier is the cluster ID and instance group ID. Example: instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0 .\nAppStream 2.0 fleet - The resource type is fleet and the unique identifier is the fleet name. Example: fleet/sample-fleet .\nDynamoDB table - The resource type is table and the unique identifier is the table name. Example: table/my-table .\nDynamoDB global secondary index - The resource type is index and the unique identifier is the index name. Example: table/my-table/index/my-table-index .\nAurora DB cluster - The resource type is cluster and the unique identifier is the cluster name. Example: cluster:my-db-cluster .\nAmazon SageMaker endpoint variant - The resource type is variant and the unique identifier is the resource ID. Example: endpoint/my-end-point/variant/KMeansClustering .\nCustom resources are not supported with a resource type. This parameter must specify the OutputValue from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider. More information is available in our GitHub repository .\nAmazon Comprehend document classification endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE .\nLambda provisioned concurrency - The resource type is function and the unique identifier is the function name with a function version or alias name suffix that is not $LATEST . Example: function:my-function:prod or function:my-function:1 .\nAmazon Keyspaces table - The resource type is table and the unique identifier is the table name. Example: keyspace/mykeyspace/table/mytable .\n\n

    :type ScalableDimension: string
    :param ScalableDimension: [REQUIRED]\nThe scalable dimension. This string consists of the service namespace, resource type, and scaling property.\n\necs:service:DesiredCount - The desired task count of an ECS service.\nec2:spot-fleet-request:TargetCapacity - The target capacity of a Spot Fleet request.\nelasticmapreduce:instancegroup:InstanceCount - The instance count of an EMR Instance Group.\nappstream:fleet:DesiredCapacity - The desired capacity of an AppStream 2.0 fleet.\ndynamodb:table:ReadCapacityUnits - The provisioned read capacity for a DynamoDB table.\ndynamodb:table:WriteCapacityUnits - The provisioned write capacity for a DynamoDB table.\ndynamodb:index:ReadCapacityUnits - The provisioned read capacity for a DynamoDB global secondary index.\ndynamodb:index:WriteCapacityUnits - The provisioned write capacity for a DynamoDB global secondary index.\nrds:cluster:ReadReplicaCount - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition.\nsagemaker:variant:DesiredInstanceCount - The number of EC2 instances for an Amazon SageMaker model endpoint variant.\ncustom-resource:ResourceType:Property - The scalable dimension for a custom resource provided by your own application or service.\ncomprehend:document-classifier-endpoint:DesiredInferenceUnits - The number of inference units for an Amazon Comprehend document classification endpoint.\nlambda:function:ProvisionedConcurrency - The provisioned concurrency for a Lambda function.\ncassandra:table:ReadCapacityUnits - The provisioned read capacity for an Amazon Keyspaces table.\ncassandra:table:WriteCapacityUnits - The provisioned write capacity for an Amazon Keyspaces table.\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

ApplicationAutoScaling.Client.exceptions.ValidationException
ApplicationAutoScaling.Client.exceptions.ObjectNotFoundException
ApplicationAutoScaling.Client.exceptions.ConcurrentUpdateException
ApplicationAutoScaling.Client.exceptions.InternalServiceException

Examples
This example deletes a scaling policy for the Amazon ECS service called web-app, which is running in the default cluster.
response = client.delete_scaling_policy(
    PolicyName='web-app-cpu-lt-25',
    ResourceId='service/default/web-app',
    ScalableDimension='ecs:service:DesiredCount',
    ServiceNamespace='ecs',
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_scheduled_action(ServiceNamespace=None, ScheduledActionName=None, ResourceId=None, ScalableDimension=None):
    """
    Deletes the specified scheduled action for an Application Auto Scaling scalable target.
    For more information, see Delete a Scheduled Action in the Application Auto Scaling User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_scheduled_action(
        ServiceNamespace='ecs'|'elasticmapreduce'|'ec2'|'appstream'|'dynamodb'|'rds'|'sagemaker'|'custom-resource'|'comprehend'|'lambda'|'cassandra',
        ScheduledActionName='string',
        ResourceId='string',
        ScalableDimension='ecs:service:DesiredCount'|'ec2:spot-fleet-request:TargetCapacity'|'elasticmapreduce:instancegroup:InstanceCount'|'appstream:fleet:DesiredCapacity'|'dynamodb:table:ReadCapacityUnits'|'dynamodb:table:WriteCapacityUnits'|'dynamodb:index:ReadCapacityUnits'|'dynamodb:index:WriteCapacityUnits'|'rds:cluster:ReadReplicaCount'|'sagemaker:variant:DesiredInstanceCount'|'custom-resource:ResourceType:Property'|'comprehend:document-classifier-endpoint:DesiredInferenceUnits'|'lambda:function:ProvisionedConcurrency'|'cassandra:table:ReadCapacityUnits'|'cassandra:table:WriteCapacityUnits'
    )
    
    
    :type ServiceNamespace: string
    :param ServiceNamespace: [REQUIRED]\nThe namespace of the AWS service that provides the resource. For a resource provided by your own application or service, use custom-resource instead.\n

    :type ScheduledActionName: string
    :param ScheduledActionName: [REQUIRED]\nThe name of the scheduled action.\n

    :type ResourceId: string
    :param ResourceId: [REQUIRED]\nThe identifier of the resource associated with the scheduled action. This string consists of the resource type and unique identifier.\n\nECS service - The resource type is service and the unique identifier is the cluster name and service name. Example: service/default/sample-webapp .\nSpot Fleet request - The resource type is spot-fleet-request and the unique identifier is the Spot Fleet request ID. Example: spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE .\nEMR cluster - The resource type is instancegroup and the unique identifier is the cluster ID and instance group ID. Example: instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0 .\nAppStream 2.0 fleet - The resource type is fleet and the unique identifier is the fleet name. Example: fleet/sample-fleet .\nDynamoDB table - The resource type is table and the unique identifier is the table name. Example: table/my-table .\nDynamoDB global secondary index - The resource type is index and the unique identifier is the index name. Example: table/my-table/index/my-table-index .\nAurora DB cluster - The resource type is cluster and the unique identifier is the cluster name. Example: cluster:my-db-cluster .\nAmazon SageMaker endpoint variant - The resource type is variant and the unique identifier is the resource ID. Example: endpoint/my-end-point/variant/KMeansClustering .\nCustom resources are not supported with a resource type. This parameter must specify the OutputValue from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider. More information is available in our GitHub repository .\nAmazon Comprehend document classification endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE .\nLambda provisioned concurrency - The resource type is function and the unique identifier is the function name with a function version or alias name suffix that is not $LATEST . Example: function:my-function:prod or function:my-function:1 .\nAmazon Keyspaces table - The resource type is table and the unique identifier is the table name. Example: keyspace/mykeyspace/table/mytable .\n\n

    :type ScalableDimension: string
    :param ScalableDimension: [REQUIRED]\nThe scalable dimension. This string consists of the service namespace, resource type, and scaling property.\n\necs:service:DesiredCount - The desired task count of an ECS service.\nec2:spot-fleet-request:TargetCapacity - The target capacity of a Spot Fleet request.\nelasticmapreduce:instancegroup:InstanceCount - The instance count of an EMR Instance Group.\nappstream:fleet:DesiredCapacity - The desired capacity of an AppStream 2.0 fleet.\ndynamodb:table:ReadCapacityUnits - The provisioned read capacity for a DynamoDB table.\ndynamodb:table:WriteCapacityUnits - The provisioned write capacity for a DynamoDB table.\ndynamodb:index:ReadCapacityUnits - The provisioned read capacity for a DynamoDB global secondary index.\ndynamodb:index:WriteCapacityUnits - The provisioned write capacity for a DynamoDB global secondary index.\nrds:cluster:ReadReplicaCount - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition.\nsagemaker:variant:DesiredInstanceCount - The number of EC2 instances for an Amazon SageMaker model endpoint variant.\ncustom-resource:ResourceType:Property - The scalable dimension for a custom resource provided by your own application or service.\ncomprehend:document-classifier-endpoint:DesiredInferenceUnits - The number of inference units for an Amazon Comprehend document classification endpoint.\nlambda:function:ProvisionedConcurrency - The provisioned concurrency for a Lambda function.\ncassandra:table:ReadCapacityUnits - The provisioned read capacity for an Amazon Keyspaces table.\ncassandra:table:WriteCapacityUnits - The provisioned write capacity for an Amazon Keyspaces table.\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

ApplicationAutoScaling.Client.exceptions.ValidationException
ApplicationAutoScaling.Client.exceptions.ObjectNotFoundException
ApplicationAutoScaling.Client.exceptions.ConcurrentUpdateException
ApplicationAutoScaling.Client.exceptions.InternalServiceException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def deregister_scalable_target(ServiceNamespace=None, ResourceId=None, ScalableDimension=None):
    """
    Deregisters an Application Auto Scaling scalable target when you have finished using it. To see which resources have been registered, use DescribeScalableTargets .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example deregisters a scalable target for an Amazon ECS service called web-app that is running in the default cluster.
    Expected Output:
    
    :example: response = client.deregister_scalable_target(
        ServiceNamespace='ecs'|'elasticmapreduce'|'ec2'|'appstream'|'dynamodb'|'rds'|'sagemaker'|'custom-resource'|'comprehend'|'lambda'|'cassandra',
        ResourceId='string',
        ScalableDimension='ecs:service:DesiredCount'|'ec2:spot-fleet-request:TargetCapacity'|'elasticmapreduce:instancegroup:InstanceCount'|'appstream:fleet:DesiredCapacity'|'dynamodb:table:ReadCapacityUnits'|'dynamodb:table:WriteCapacityUnits'|'dynamodb:index:ReadCapacityUnits'|'dynamodb:index:WriteCapacityUnits'|'rds:cluster:ReadReplicaCount'|'sagemaker:variant:DesiredInstanceCount'|'custom-resource:ResourceType:Property'|'comprehend:document-classifier-endpoint:DesiredInferenceUnits'|'lambda:function:ProvisionedConcurrency'|'cassandra:table:ReadCapacityUnits'|'cassandra:table:WriteCapacityUnits'
    )
    
    
    :type ServiceNamespace: string
    :param ServiceNamespace: [REQUIRED]\nThe namespace of the AWS service that provides the resource. For a resource provided by your own application or service, use custom-resource instead.\n

    :type ResourceId: string
    :param ResourceId: [REQUIRED]\nThe identifier of the resource associated with the scalable target. This string consists of the resource type and unique identifier.\n\nECS service - The resource type is service and the unique identifier is the cluster name and service name. Example: service/default/sample-webapp .\nSpot Fleet request - The resource type is spot-fleet-request and the unique identifier is the Spot Fleet request ID. Example: spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE .\nEMR cluster - The resource type is instancegroup and the unique identifier is the cluster ID and instance group ID. Example: instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0 .\nAppStream 2.0 fleet - The resource type is fleet and the unique identifier is the fleet name. Example: fleet/sample-fleet .\nDynamoDB table - The resource type is table and the unique identifier is the table name. Example: table/my-table .\nDynamoDB global secondary index - The resource type is index and the unique identifier is the index name. Example: table/my-table/index/my-table-index .\nAurora DB cluster - The resource type is cluster and the unique identifier is the cluster name. Example: cluster:my-db-cluster .\nAmazon SageMaker endpoint variant - The resource type is variant and the unique identifier is the resource ID. Example: endpoint/my-end-point/variant/KMeansClustering .\nCustom resources are not supported with a resource type. This parameter must specify the OutputValue from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider. More information is available in our GitHub repository .\nAmazon Comprehend document classification endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE .\nLambda provisioned concurrency - The resource type is function and the unique identifier is the function name with a function version or alias name suffix that is not $LATEST . Example: function:my-function:prod or function:my-function:1 .\nAmazon Keyspaces table - The resource type is table and the unique identifier is the table name. Example: keyspace/mykeyspace/table/mytable .\n\n

    :type ScalableDimension: string
    :param ScalableDimension: [REQUIRED]\nThe scalable dimension associated with the scalable target. This string consists of the service namespace, resource type, and scaling property.\n\necs:service:DesiredCount - The desired task count of an ECS service.\nec2:spot-fleet-request:TargetCapacity - The target capacity of a Spot Fleet request.\nelasticmapreduce:instancegroup:InstanceCount - The instance count of an EMR Instance Group.\nappstream:fleet:DesiredCapacity - The desired capacity of an AppStream 2.0 fleet.\ndynamodb:table:ReadCapacityUnits - The provisioned read capacity for a DynamoDB table.\ndynamodb:table:WriteCapacityUnits - The provisioned write capacity for a DynamoDB table.\ndynamodb:index:ReadCapacityUnits - The provisioned read capacity for a DynamoDB global secondary index.\ndynamodb:index:WriteCapacityUnits - The provisioned write capacity for a DynamoDB global secondary index.\nrds:cluster:ReadReplicaCount - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition.\nsagemaker:variant:DesiredInstanceCount - The number of EC2 instances for an Amazon SageMaker model endpoint variant.\ncustom-resource:ResourceType:Property - The scalable dimension for a custom resource provided by your own application or service.\ncomprehend:document-classifier-endpoint:DesiredInferenceUnits - The number of inference units for an Amazon Comprehend document classification endpoint.\nlambda:function:ProvisionedConcurrency - The provisioned concurrency for a Lambda function.\ncassandra:table:ReadCapacityUnits - The provisioned read capacity for an Amazon Keyspaces table.\ncassandra:table:WriteCapacityUnits - The provisioned write capacity for an Amazon Keyspaces table.\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

ApplicationAutoScaling.Client.exceptions.ValidationException
ApplicationAutoScaling.Client.exceptions.ObjectNotFoundException
ApplicationAutoScaling.Client.exceptions.ConcurrentUpdateException
ApplicationAutoScaling.Client.exceptions.InternalServiceException

Examples
This example deregisters a scalable target for an Amazon ECS service called web-app that is running in the default cluster.
response = client.deregister_scalable_target(
    ResourceId='service/default/web-app',
    ScalableDimension='ecs:service:DesiredCount',
    ServiceNamespace='ecs',
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def describe_scalable_targets(ServiceNamespace=None, ResourceIds=None, ScalableDimension=None, MaxResults=None, NextToken=None):
    """
    Gets information about the scalable targets in the specified namespace.
    You can filter the results using ResourceIds and ScalableDimension .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example describes the scalable targets for the ecs service namespace.
    Expected Output:
    
    :example: response = client.describe_scalable_targets(
        ServiceNamespace='ecs'|'elasticmapreduce'|'ec2'|'appstream'|'dynamodb'|'rds'|'sagemaker'|'custom-resource'|'comprehend'|'lambda'|'cassandra',
        ResourceIds=[
            'string',
        ],
        ScalableDimension='ecs:service:DesiredCount'|'ec2:spot-fleet-request:TargetCapacity'|'elasticmapreduce:instancegroup:InstanceCount'|'appstream:fleet:DesiredCapacity'|'dynamodb:table:ReadCapacityUnits'|'dynamodb:table:WriteCapacityUnits'|'dynamodb:index:ReadCapacityUnits'|'dynamodb:index:WriteCapacityUnits'|'rds:cluster:ReadReplicaCount'|'sagemaker:variant:DesiredInstanceCount'|'custom-resource:ResourceType:Property'|'comprehend:document-classifier-endpoint:DesiredInferenceUnits'|'lambda:function:ProvisionedConcurrency'|'cassandra:table:ReadCapacityUnits'|'cassandra:table:WriteCapacityUnits',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type ServiceNamespace: string
    :param ServiceNamespace: [REQUIRED]\nThe namespace of the AWS service that provides the resource. For a resource provided by your own application or service, use custom-resource instead.\n

    :type ResourceIds: list
    :param ResourceIds: The identifier of the resource associated with the scalable target. This string consists of the resource type and unique identifier. If you specify a scalable dimension, you must also specify a resource ID.\n\nECS service - The resource type is service and the unique identifier is the cluster name and service name. Example: service/default/sample-webapp .\nSpot Fleet request - The resource type is spot-fleet-request and the unique identifier is the Spot Fleet request ID. Example: spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE .\nEMR cluster - The resource type is instancegroup and the unique identifier is the cluster ID and instance group ID. Example: instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0 .\nAppStream 2.0 fleet - The resource type is fleet and the unique identifier is the fleet name. Example: fleet/sample-fleet .\nDynamoDB table - The resource type is table and the unique identifier is the table name. Example: table/my-table .\nDynamoDB global secondary index - The resource type is index and the unique identifier is the index name. Example: table/my-table/index/my-table-index .\nAurora DB cluster - The resource type is cluster and the unique identifier is the cluster name. Example: cluster:my-db-cluster .\nAmazon SageMaker endpoint variant - The resource type is variant and the unique identifier is the resource ID. Example: endpoint/my-end-point/variant/KMeansClustering .\nCustom resources are not supported with a resource type. This parameter must specify the OutputValue from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider. More information is available in our GitHub repository .\nAmazon Comprehend document classification endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE .\nLambda provisioned concurrency - The resource type is function and the unique identifier is the function name with a function version or alias name suffix that is not $LATEST . Example: function:my-function:prod or function:my-function:1 .\nAmazon Keyspaces table - The resource type is table and the unique identifier is the table name. Example: keyspace/mykeyspace/table/mytable .\n\n\n(string) --\n\n

    :type ScalableDimension: string
    :param ScalableDimension: The scalable dimension associated with the scalable target. This string consists of the service namespace, resource type, and scaling property. If you specify a scalable dimension, you must also specify a resource ID.\n\necs:service:DesiredCount - The desired task count of an ECS service.\nec2:spot-fleet-request:TargetCapacity - The target capacity of a Spot Fleet request.\nelasticmapreduce:instancegroup:InstanceCount - The instance count of an EMR Instance Group.\nappstream:fleet:DesiredCapacity - The desired capacity of an AppStream 2.0 fleet.\ndynamodb:table:ReadCapacityUnits - The provisioned read capacity for a DynamoDB table.\ndynamodb:table:WriteCapacityUnits - The provisioned write capacity for a DynamoDB table.\ndynamodb:index:ReadCapacityUnits - The provisioned read capacity for a DynamoDB global secondary index.\ndynamodb:index:WriteCapacityUnits - The provisioned write capacity for a DynamoDB global secondary index.\nrds:cluster:ReadReplicaCount - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition.\nsagemaker:variant:DesiredInstanceCount - The number of EC2 instances for an Amazon SageMaker model endpoint variant.\ncustom-resource:ResourceType:Property - The scalable dimension for a custom resource provided by your own application or service.\ncomprehend:document-classifier-endpoint:DesiredInferenceUnits - The number of inference units for an Amazon Comprehend document classification endpoint.\nlambda:function:ProvisionedConcurrency - The provisioned concurrency for a Lambda function.\ncassandra:table:ReadCapacityUnits - The provisioned read capacity for an Amazon Keyspaces table.\ncassandra:table:WriteCapacityUnits - The provisioned write capacity for an Amazon Keyspaces table.\n\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of scalable targets. This value can be between 1 and 50. The default value is 50.\nIf this parameter is used, the operation returns up to MaxResults results at a time, along with a NextToken value. To get the next set of results, include the NextToken value in a subsequent call. If this parameter is not used, the operation returns up to 50 results and a NextToken value, if applicable.\n

    :type NextToken: string
    :param NextToken: The token for the next set of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'ScalableTargets': [
        {
            'ServiceNamespace': 'ecs'|'elasticmapreduce'|'ec2'|'appstream'|'dynamodb'|'rds'|'sagemaker'|'custom-resource'|'comprehend'|'lambda'|'cassandra',
            'ResourceId': 'string',
            'ScalableDimension': 'ecs:service:DesiredCount'|'ec2:spot-fleet-request:TargetCapacity'|'elasticmapreduce:instancegroup:InstanceCount'|'appstream:fleet:DesiredCapacity'|'dynamodb:table:ReadCapacityUnits'|'dynamodb:table:WriteCapacityUnits'|'dynamodb:index:ReadCapacityUnits'|'dynamodb:index:WriteCapacityUnits'|'rds:cluster:ReadReplicaCount'|'sagemaker:variant:DesiredInstanceCount'|'custom-resource:ResourceType:Property'|'comprehend:document-classifier-endpoint:DesiredInferenceUnits'|'lambda:function:ProvisionedConcurrency'|'cassandra:table:ReadCapacityUnits'|'cassandra:table:WriteCapacityUnits',
            'MinCapacity': 123,
            'MaxCapacity': 123,
            'RoleARN': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'SuspendedState': {
                'DynamicScalingInSuspended': True|False,
                'DynamicScalingOutSuspended': True|False,
                'ScheduledScalingSuspended': True|False
            }
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

ScalableTargets (list) --
The scalable targets that match the request parameters.

(dict) --
Represents a scalable target.

ServiceNamespace (string) --
The namespace of the AWS service that provides the resource, or a custom-resource .

ResourceId (string) --
The identifier of the resource associated with the scalable target. This string consists of the resource type and unique identifier.

ECS service - The resource type is service and the unique identifier is the cluster name and service name. Example: service/default/sample-webapp .
Spot Fleet request - The resource type is spot-fleet-request and the unique identifier is the Spot Fleet request ID. Example: spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE .
EMR cluster - The resource type is instancegroup and the unique identifier is the cluster ID and instance group ID. Example: instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0 .
AppStream 2.0 fleet - The resource type is fleet and the unique identifier is the fleet name. Example: fleet/sample-fleet .
DynamoDB table - The resource type is table and the unique identifier is the table name. Example: table/my-table .
DynamoDB global secondary index - The resource type is index and the unique identifier is the index name. Example: table/my-table/index/my-table-index .
Aurora DB cluster - The resource type is cluster and the unique identifier is the cluster name. Example: cluster:my-db-cluster .
Amazon SageMaker endpoint variant - The resource type is variant and the unique identifier is the resource ID. Example: endpoint/my-end-point/variant/KMeansClustering .
Custom resources are not supported with a resource type. This parameter must specify the OutputValue from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider. More information is available in our GitHub repository .
Amazon Comprehend document classification endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE .
Lambda provisioned concurrency - The resource type is function and the unique identifier is the function name with a function version or alias name suffix that is not $LATEST . Example: function:my-function:prod or function:my-function:1 .
Amazon Keyspaces table - The resource type is table and the unique identifier is the table name. Example: keyspace/mykeyspace/table/mytable .


ScalableDimension (string) --
The scalable dimension associated with the scalable target. This string consists of the service namespace, resource type, and scaling property.

ecs:service:DesiredCount - The desired task count of an ECS service.
ec2:spot-fleet-request:TargetCapacity - The target capacity of a Spot Fleet request.
elasticmapreduce:instancegroup:InstanceCount - The instance count of an EMR Instance Group.
appstream:fleet:DesiredCapacity - The desired capacity of an AppStream 2.0 fleet.
dynamodb:table:ReadCapacityUnits - The provisioned read capacity for a DynamoDB table.
dynamodb:table:WriteCapacityUnits - The provisioned write capacity for a DynamoDB table.
dynamodb:index:ReadCapacityUnits - The provisioned read capacity for a DynamoDB global secondary index.
dynamodb:index:WriteCapacityUnits - The provisioned write capacity for a DynamoDB global secondary index.
rds:cluster:ReadReplicaCount - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition.
sagemaker:variant:DesiredInstanceCount - The number of EC2 instances for an Amazon SageMaker model endpoint variant.
custom-resource:ResourceType:Property - The scalable dimension for a custom resource provided by your own application or service.
comprehend:document-classifier-endpoint:DesiredInferenceUnits - The number of inference units for an Amazon Comprehend document classification endpoint.
lambda:function:ProvisionedConcurrency - The provisioned concurrency for a Lambda function.
cassandra:table:ReadCapacityUnits - The provisioned read capacity for an Amazon Keyspaces table.
cassandra:table:WriteCapacityUnits - The provisioned write capacity for an Amazon Keyspaces table.


MinCapacity (integer) --
The minimum value to scale to in response to a scale-in activity.

MaxCapacity (integer) --
The maximum value to scale to in response to a scale-out activity.

RoleARN (string) --
The ARN of an IAM role that allows Application Auto Scaling to modify the scalable target on your behalf.

CreationTime (datetime) --
The Unix timestamp for when the scalable target was created.

SuspendedState (dict) --
Specifies whether the scaling activities for a scalable target are in a suspended state.

DynamicScalingInSuspended (boolean) --
Whether scale in by a target tracking scaling policy or a step scaling policy is suspended. Set the value to true if you don\'t want Application Auto Scaling to remove capacity when a scaling policy is triggered. The default is false .

DynamicScalingOutSuspended (boolean) --
Whether scale out by a target tracking scaling policy or a step scaling policy is suspended. Set the value to true if you don\'t want Application Auto Scaling to add capacity when a scaling policy is triggered. The default is false .

ScheduledScalingSuspended (boolean) --
Whether scheduled scaling is suspended. Set the value to true if you don\'t want Application Auto Scaling to add or remove capacity by initiating scheduled actions. The default is false .







NextToken (string) --
The token required to get the next set of results. This value is null if there are no more results to return.







Exceptions

ApplicationAutoScaling.Client.exceptions.ValidationException
ApplicationAutoScaling.Client.exceptions.InvalidNextTokenException
ApplicationAutoScaling.Client.exceptions.ConcurrentUpdateException
ApplicationAutoScaling.Client.exceptions.InternalServiceException

Examples
This example describes the scalable targets for the ecs service namespace.
response = client.describe_scalable_targets(
    ServiceNamespace='ecs',
)

print(response)


Expected Output:
{
    'ScalableTargets': [
        {
            'CreationTime': datetime(2016, 5, 6, 11, 21, 46, 4, 127, 0),
            'MaxCapacity': 10,
            'MinCapacity': 1,
            'ResourceId': 'service/default/web-app',
            'RoleARN': 'arn:aws:iam::012345678910:role/ApplicationAutoscalingECSRole',
            'ScalableDimension': 'ecs:service:DesiredCount',
            'ServiceNamespace': 'ecs',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ScalableTargets': [
            {
                'ServiceNamespace': 'ecs'|'elasticmapreduce'|'ec2'|'appstream'|'dynamodb'|'rds'|'sagemaker'|'custom-resource'|'comprehend'|'lambda'|'cassandra',
                'ResourceId': 'string',
                'ScalableDimension': 'ecs:service:DesiredCount'|'ec2:spot-fleet-request:TargetCapacity'|'elasticmapreduce:instancegroup:InstanceCount'|'appstream:fleet:DesiredCapacity'|'dynamodb:table:ReadCapacityUnits'|'dynamodb:table:WriteCapacityUnits'|'dynamodb:index:ReadCapacityUnits'|'dynamodb:index:WriteCapacityUnits'|'rds:cluster:ReadReplicaCount'|'sagemaker:variant:DesiredInstanceCount'|'custom-resource:ResourceType:Property'|'comprehend:document-classifier-endpoint:DesiredInferenceUnits'|'lambda:function:ProvisionedConcurrency'|'cassandra:table:ReadCapacityUnits'|'cassandra:table:WriteCapacityUnits',
                'MinCapacity': 123,
                'MaxCapacity': 123,
                'RoleARN': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'SuspendedState': {
                    'DynamicScalingInSuspended': True|False,
                    'DynamicScalingOutSuspended': True|False,
                    'ScheduledScalingSuspended': True|False
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    ECS service - The resource type is service and the unique identifier is the cluster name and service name. Example: service/default/sample-webapp .
    Spot Fleet request - The resource type is spot-fleet-request and the unique identifier is the Spot Fleet request ID. Example: spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE .
    EMR cluster - The resource type is instancegroup and the unique identifier is the cluster ID and instance group ID. Example: instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0 .
    AppStream 2.0 fleet - The resource type is fleet and the unique identifier is the fleet name. Example: fleet/sample-fleet .
    DynamoDB table - The resource type is table and the unique identifier is the table name. Example: table/my-table .
    DynamoDB global secondary index - The resource type is index and the unique identifier is the index name. Example: table/my-table/index/my-table-index .
    Aurora DB cluster - The resource type is cluster and the unique identifier is the cluster name. Example: cluster:my-db-cluster .
    Amazon SageMaker endpoint variant - The resource type is variant and the unique identifier is the resource ID. Example: endpoint/my-end-point/variant/KMeansClustering .
    Custom resources are not supported with a resource type. This parameter must specify the OutputValue from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider. More information is available in our GitHub repository .
    Amazon Comprehend document classification endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE .
    Lambda provisioned concurrency - The resource type is function and the unique identifier is the function name with a function version or alias name suffix that is not $LATEST . Example: function:my-function:prod or function:my-function:1 .
    Amazon Keyspaces table - The resource type is table and the unique identifier is the table name. Example: keyspace/mykeyspace/table/mytable .
    
    """
    pass

def describe_scaling_activities(ServiceNamespace=None, ResourceId=None, ScalableDimension=None, MaxResults=None, NextToken=None):
    """
    Provides descriptive information about the scaling activities in the specified namespace from the previous six weeks.
    You can filter the results using ResourceId and ScalableDimension .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example describes the scaling activities for an Amazon ECS service called web-app that is running in the default cluster.
    Expected Output:
    
    :example: response = client.describe_scaling_activities(
        ServiceNamespace='ecs'|'elasticmapreduce'|'ec2'|'appstream'|'dynamodb'|'rds'|'sagemaker'|'custom-resource'|'comprehend'|'lambda'|'cassandra',
        ResourceId='string',
        ScalableDimension='ecs:service:DesiredCount'|'ec2:spot-fleet-request:TargetCapacity'|'elasticmapreduce:instancegroup:InstanceCount'|'appstream:fleet:DesiredCapacity'|'dynamodb:table:ReadCapacityUnits'|'dynamodb:table:WriteCapacityUnits'|'dynamodb:index:ReadCapacityUnits'|'dynamodb:index:WriteCapacityUnits'|'rds:cluster:ReadReplicaCount'|'sagemaker:variant:DesiredInstanceCount'|'custom-resource:ResourceType:Property'|'comprehend:document-classifier-endpoint:DesiredInferenceUnits'|'lambda:function:ProvisionedConcurrency'|'cassandra:table:ReadCapacityUnits'|'cassandra:table:WriteCapacityUnits',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type ServiceNamespace: string
    :param ServiceNamespace: [REQUIRED]\nThe namespace of the AWS service that provides the resource. For a resource provided by your own application or service, use custom-resource instead.\n

    :type ResourceId: string
    :param ResourceId: The identifier of the resource associated with the scaling activity. This string consists of the resource type and unique identifier. If you specify a scalable dimension, you must also specify a resource ID.\n\nECS service - The resource type is service and the unique identifier is the cluster name and service name. Example: service/default/sample-webapp .\nSpot Fleet request - The resource type is spot-fleet-request and the unique identifier is the Spot Fleet request ID. Example: spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE .\nEMR cluster - The resource type is instancegroup and the unique identifier is the cluster ID and instance group ID. Example: instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0 .\nAppStream 2.0 fleet - The resource type is fleet and the unique identifier is the fleet name. Example: fleet/sample-fleet .\nDynamoDB table - The resource type is table and the unique identifier is the table name. Example: table/my-table .\nDynamoDB global secondary index - The resource type is index and the unique identifier is the index name. Example: table/my-table/index/my-table-index .\nAurora DB cluster - The resource type is cluster and the unique identifier is the cluster name. Example: cluster:my-db-cluster .\nAmazon SageMaker endpoint variant - The resource type is variant and the unique identifier is the resource ID. Example: endpoint/my-end-point/variant/KMeansClustering .\nCustom resources are not supported with a resource type. This parameter must specify the OutputValue from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider. More information is available in our GitHub repository .\nAmazon Comprehend document classification endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE .\nLambda provisioned concurrency - The resource type is function and the unique identifier is the function name with a function version or alias name suffix that is not $LATEST . Example: function:my-function:prod or function:my-function:1 .\nAmazon Keyspaces table - The resource type is table and the unique identifier is the table name. Example: keyspace/mykeyspace/table/mytable .\n\n

    :type ScalableDimension: string
    :param ScalableDimension: The scalable dimension. This string consists of the service namespace, resource type, and scaling property. If you specify a scalable dimension, you must also specify a resource ID.\n\necs:service:DesiredCount - The desired task count of an ECS service.\nec2:spot-fleet-request:TargetCapacity - The target capacity of a Spot Fleet request.\nelasticmapreduce:instancegroup:InstanceCount - The instance count of an EMR Instance Group.\nappstream:fleet:DesiredCapacity - The desired capacity of an AppStream 2.0 fleet.\ndynamodb:table:ReadCapacityUnits - The provisioned read capacity for a DynamoDB table.\ndynamodb:table:WriteCapacityUnits - The provisioned write capacity for a DynamoDB table.\ndynamodb:index:ReadCapacityUnits - The provisioned read capacity for a DynamoDB global secondary index.\ndynamodb:index:WriteCapacityUnits - The provisioned write capacity for a DynamoDB global secondary index.\nrds:cluster:ReadReplicaCount - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition.\nsagemaker:variant:DesiredInstanceCount - The number of EC2 instances for an Amazon SageMaker model endpoint variant.\ncustom-resource:ResourceType:Property - The scalable dimension for a custom resource provided by your own application or service.\ncomprehend:document-classifier-endpoint:DesiredInferenceUnits - The number of inference units for an Amazon Comprehend document classification endpoint.\nlambda:function:ProvisionedConcurrency - The provisioned concurrency for a Lambda function.\ncassandra:table:ReadCapacityUnits - The provisioned read capacity for an Amazon Keyspaces table.\ncassandra:table:WriteCapacityUnits - The provisioned write capacity for an Amazon Keyspaces table.\n\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of scalable targets. This value can be between 1 and 50. The default value is 50.\nIf this parameter is used, the operation returns up to MaxResults results at a time, along with a NextToken value. To get the next set of results, include the NextToken value in a subsequent call. If this parameter is not used, the operation returns up to 50 results and a NextToken value, if applicable.\n

    :type NextToken: string
    :param NextToken: The token for the next set of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'ScalingActivities': [
        {
            'ActivityId': 'string',
            'ServiceNamespace': 'ecs'|'elasticmapreduce'|'ec2'|'appstream'|'dynamodb'|'rds'|'sagemaker'|'custom-resource'|'comprehend'|'lambda'|'cassandra',
            'ResourceId': 'string',
            'ScalableDimension': 'ecs:service:DesiredCount'|'ec2:spot-fleet-request:TargetCapacity'|'elasticmapreduce:instancegroup:InstanceCount'|'appstream:fleet:DesiredCapacity'|'dynamodb:table:ReadCapacityUnits'|'dynamodb:table:WriteCapacityUnits'|'dynamodb:index:ReadCapacityUnits'|'dynamodb:index:WriteCapacityUnits'|'rds:cluster:ReadReplicaCount'|'sagemaker:variant:DesiredInstanceCount'|'custom-resource:ResourceType:Property'|'comprehend:document-classifier-endpoint:DesiredInferenceUnits'|'lambda:function:ProvisionedConcurrency'|'cassandra:table:ReadCapacityUnits'|'cassandra:table:WriteCapacityUnits',
            'Description': 'string',
            'Cause': 'string',
            'StartTime': datetime(2015, 1, 1),
            'EndTime': datetime(2015, 1, 1),
            'StatusCode': 'Pending'|'InProgress'|'Successful'|'Overridden'|'Unfulfilled'|'Failed',
            'StatusMessage': 'string',
            'Details': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

ScalingActivities (list) --
A list of scaling activity objects.

(dict) --
Represents a scaling activity.

ActivityId (string) --
The unique identifier of the scaling activity.

ServiceNamespace (string) --
The namespace of the AWS service that provides the resource, or a custom-resource .

ResourceId (string) --
The identifier of the resource associated with the scaling activity. This string consists of the resource type and unique identifier.

ECS service - The resource type is service and the unique identifier is the cluster name and service name. Example: service/default/sample-webapp .
Spot Fleet request - The resource type is spot-fleet-request and the unique identifier is the Spot Fleet request ID. Example: spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE .
EMR cluster - The resource type is instancegroup and the unique identifier is the cluster ID and instance group ID. Example: instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0 .
AppStream 2.0 fleet - The resource type is fleet and the unique identifier is the fleet name. Example: fleet/sample-fleet .
DynamoDB table - The resource type is table and the unique identifier is the table name. Example: table/my-table .
DynamoDB global secondary index - The resource type is index and the unique identifier is the index name. Example: table/my-table/index/my-table-index .
Aurora DB cluster - The resource type is cluster and the unique identifier is the cluster name. Example: cluster:my-db-cluster .
Amazon SageMaker endpoint variant - The resource type is variant and the unique identifier is the resource ID. Example: endpoint/my-end-point/variant/KMeansClustering .
Custom resources are not supported with a resource type. This parameter must specify the OutputValue from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider. More information is available in our GitHub repository .
Amazon Comprehend document classification endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE .
Lambda provisioned concurrency - The resource type is function and the unique identifier is the function name with a function version or alias name suffix that is not $LATEST . Example: function:my-function:prod or function:my-function:1 .
Amazon Keyspaces table - The resource type is table and the unique identifier is the table name. Example: keyspace/mykeyspace/table/mytable .


ScalableDimension (string) --
The scalable dimension. This string consists of the service namespace, resource type, and scaling property.

ecs:service:DesiredCount - The desired task count of an ECS service.
ec2:spot-fleet-request:TargetCapacity - The target capacity of a Spot Fleet request.
elasticmapreduce:instancegroup:InstanceCount - The instance count of an EMR Instance Group.
appstream:fleet:DesiredCapacity - The desired capacity of an AppStream 2.0 fleet.
dynamodb:table:ReadCapacityUnits - The provisioned read capacity for a DynamoDB table.
dynamodb:table:WriteCapacityUnits - The provisioned write capacity for a DynamoDB table.
dynamodb:index:ReadCapacityUnits - The provisioned read capacity for a DynamoDB global secondary index.
dynamodb:index:WriteCapacityUnits - The provisioned write capacity for a DynamoDB global secondary index.
rds:cluster:ReadReplicaCount - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition.
sagemaker:variant:DesiredInstanceCount - The number of EC2 instances for an Amazon SageMaker model endpoint variant.
custom-resource:ResourceType:Property - The scalable dimension for a custom resource provided by your own application or service.
comprehend:document-classifier-endpoint:DesiredInferenceUnits - The number of inference units for an Amazon Comprehend document classification endpoint.
lambda:function:ProvisionedConcurrency - The provisioned concurrency for a Lambda function.
cassandra:table:ReadCapacityUnits - The provisioned read capacity for an Amazon Keyspaces table.
cassandra:table:WriteCapacityUnits - The provisioned write capacity for an Amazon Keyspaces table.


Description (string) --
A simple description of what action the scaling activity intends to accomplish.

Cause (string) --
A simple description of what caused the scaling activity to happen.

StartTime (datetime) --
The Unix timestamp for when the scaling activity began.

EndTime (datetime) --
The Unix timestamp for when the scaling activity ended.

StatusCode (string) --
Indicates the status of the scaling activity.

StatusMessage (string) --
A simple message about the current status of the scaling activity.

Details (string) --
The details about the scaling activity.





NextToken (string) --
The token required to get the next set of results. This value is null if there are no more results to return.







Exceptions

ApplicationAutoScaling.Client.exceptions.ValidationException
ApplicationAutoScaling.Client.exceptions.InvalidNextTokenException
ApplicationAutoScaling.Client.exceptions.ConcurrentUpdateException
ApplicationAutoScaling.Client.exceptions.InternalServiceException

Examples
This example describes the scaling activities for an Amazon ECS service called web-app that is running in the default cluster.
response = client.describe_scaling_activities(
    ResourceId='service/default/web-app',
    ScalableDimension='ecs:service:DesiredCount',
    ServiceNamespace='ecs',
)

print(response)


Expected Output:
{
    'ScalingActivities': [
        {
            'ActivityId': 'e6c5f7d1-dbbb-4a3f-89b2-51f33e766399',
            'Cause': 'monitor alarm web-app-cpu-lt-25 in state ALARM triggered policy web-app-cpu-lt-25',
            'Description': 'Setting desired count to 1.',
            'EndTime': datetime(2016, 5, 6, 16, 4, 32, 4, 127, 0),
            'ResourceId': 'service/default/web-app',
            'ScalableDimension': 'ecs:service:DesiredCount',
            'ServiceNamespace': 'ecs',
            'StartTime': datetime(2016, 5, 6, 16, 3, 58, 4, 127, 0),
            'StatusCode': 'Successful',
            'StatusMessage': 'Successfully set desired count to 1. Change successfully fulfilled by ecs.',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ScalingActivities': [
            {
                'ActivityId': 'string',
                'ServiceNamespace': 'ecs'|'elasticmapreduce'|'ec2'|'appstream'|'dynamodb'|'rds'|'sagemaker'|'custom-resource'|'comprehend'|'lambda'|'cassandra',
                'ResourceId': 'string',
                'ScalableDimension': 'ecs:service:DesiredCount'|'ec2:spot-fleet-request:TargetCapacity'|'elasticmapreduce:instancegroup:InstanceCount'|'appstream:fleet:DesiredCapacity'|'dynamodb:table:ReadCapacityUnits'|'dynamodb:table:WriteCapacityUnits'|'dynamodb:index:ReadCapacityUnits'|'dynamodb:index:WriteCapacityUnits'|'rds:cluster:ReadReplicaCount'|'sagemaker:variant:DesiredInstanceCount'|'custom-resource:ResourceType:Property'|'comprehend:document-classifier-endpoint:DesiredInferenceUnits'|'lambda:function:ProvisionedConcurrency'|'cassandra:table:ReadCapacityUnits'|'cassandra:table:WriteCapacityUnits',
                'Description': 'string',
                'Cause': 'string',
                'StartTime': datetime(2015, 1, 1),
                'EndTime': datetime(2015, 1, 1),
                'StatusCode': 'Pending'|'InProgress'|'Successful'|'Overridden'|'Unfulfilled'|'Failed',
                'StatusMessage': 'string',
                'Details': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    ECS service - The resource type is service and the unique identifier is the cluster name and service name. Example: service/default/sample-webapp .
    Spot Fleet request - The resource type is spot-fleet-request and the unique identifier is the Spot Fleet request ID. Example: spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE .
    EMR cluster - The resource type is instancegroup and the unique identifier is the cluster ID and instance group ID. Example: instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0 .
    AppStream 2.0 fleet - The resource type is fleet and the unique identifier is the fleet name. Example: fleet/sample-fleet .
    DynamoDB table - The resource type is table and the unique identifier is the table name. Example: table/my-table .
    DynamoDB global secondary index - The resource type is index and the unique identifier is the index name. Example: table/my-table/index/my-table-index .
    Aurora DB cluster - The resource type is cluster and the unique identifier is the cluster name. Example: cluster:my-db-cluster .
    Amazon SageMaker endpoint variant - The resource type is variant and the unique identifier is the resource ID. Example: endpoint/my-end-point/variant/KMeansClustering .
    Custom resources are not supported with a resource type. This parameter must specify the OutputValue from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider. More information is available in our GitHub repository .
    Amazon Comprehend document classification endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE .
    Lambda provisioned concurrency - The resource type is function and the unique identifier is the function name with a function version or alias name suffix that is not $LATEST . Example: function:my-function:prod or function:my-function:1 .
    Amazon Keyspaces table - The resource type is table and the unique identifier is the table name. Example: keyspace/mykeyspace/table/mytable .
    
    """
    pass

def describe_scaling_policies(PolicyNames=None, ServiceNamespace=None, ResourceId=None, ScalableDimension=None, MaxResults=None, NextToken=None):
    """
    Describes the Application Auto Scaling scaling policies for the specified service namespace.
    You can filter the results using ResourceId , ScalableDimension , and PolicyNames .
    For more information, see Target Tracking Scaling Policies and Step Scaling Policies in the Application Auto Scaling User Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example describes the scaling policies for the ecs service namespace.
    Expected Output:
    
    :example: response = client.describe_scaling_policies(
        PolicyNames=[
            'string',
        ],
        ServiceNamespace='ecs'|'elasticmapreduce'|'ec2'|'appstream'|'dynamodb'|'rds'|'sagemaker'|'custom-resource'|'comprehend'|'lambda'|'cassandra',
        ResourceId='string',
        ScalableDimension='ecs:service:DesiredCount'|'ec2:spot-fleet-request:TargetCapacity'|'elasticmapreduce:instancegroup:InstanceCount'|'appstream:fleet:DesiredCapacity'|'dynamodb:table:ReadCapacityUnits'|'dynamodb:table:WriteCapacityUnits'|'dynamodb:index:ReadCapacityUnits'|'dynamodb:index:WriteCapacityUnits'|'rds:cluster:ReadReplicaCount'|'sagemaker:variant:DesiredInstanceCount'|'custom-resource:ResourceType:Property'|'comprehend:document-classifier-endpoint:DesiredInferenceUnits'|'lambda:function:ProvisionedConcurrency'|'cassandra:table:ReadCapacityUnits'|'cassandra:table:WriteCapacityUnits',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type PolicyNames: list
    :param PolicyNames: The names of the scaling policies to describe.\n\n(string) --\n\n

    :type ServiceNamespace: string
    :param ServiceNamespace: [REQUIRED]\nThe namespace of the AWS service that provides the resource. For a resource provided by your own application or service, use custom-resource instead.\n

    :type ResourceId: string
    :param ResourceId: The identifier of the resource associated with the scaling policy. This string consists of the resource type and unique identifier. If you specify a scalable dimension, you must also specify a resource ID.\n\nECS service - The resource type is service and the unique identifier is the cluster name and service name. Example: service/default/sample-webapp .\nSpot Fleet request - The resource type is spot-fleet-request and the unique identifier is the Spot Fleet request ID. Example: spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE .\nEMR cluster - The resource type is instancegroup and the unique identifier is the cluster ID and instance group ID. Example: instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0 .\nAppStream 2.0 fleet - The resource type is fleet and the unique identifier is the fleet name. Example: fleet/sample-fleet .\nDynamoDB table - The resource type is table and the unique identifier is the table name. Example: table/my-table .\nDynamoDB global secondary index - The resource type is index and the unique identifier is the index name. Example: table/my-table/index/my-table-index .\nAurora DB cluster - The resource type is cluster and the unique identifier is the cluster name. Example: cluster:my-db-cluster .\nAmazon SageMaker endpoint variant - The resource type is variant and the unique identifier is the resource ID. Example: endpoint/my-end-point/variant/KMeansClustering .\nCustom resources are not supported with a resource type. This parameter must specify the OutputValue from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider. More information is available in our GitHub repository .\nAmazon Comprehend document classification endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE .\nLambda provisioned concurrency - The resource type is function and the unique identifier is the function name with a function version or alias name suffix that is not $LATEST . Example: function:my-function:prod or function:my-function:1 .\nAmazon Keyspaces table - The resource type is table and the unique identifier is the table name. Example: keyspace/mykeyspace/table/mytable .\n\n

    :type ScalableDimension: string
    :param ScalableDimension: The scalable dimension. This string consists of the service namespace, resource type, and scaling property. If you specify a scalable dimension, you must also specify a resource ID.\n\necs:service:DesiredCount - The desired task count of an ECS service.\nec2:spot-fleet-request:TargetCapacity - The target capacity of a Spot Fleet request.\nelasticmapreduce:instancegroup:InstanceCount - The instance count of an EMR Instance Group.\nappstream:fleet:DesiredCapacity - The desired capacity of an AppStream 2.0 fleet.\ndynamodb:table:ReadCapacityUnits - The provisioned read capacity for a DynamoDB table.\ndynamodb:table:WriteCapacityUnits - The provisioned write capacity for a DynamoDB table.\ndynamodb:index:ReadCapacityUnits - The provisioned read capacity for a DynamoDB global secondary index.\ndynamodb:index:WriteCapacityUnits - The provisioned write capacity for a DynamoDB global secondary index.\nrds:cluster:ReadReplicaCount - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition.\nsagemaker:variant:DesiredInstanceCount - The number of EC2 instances for an Amazon SageMaker model endpoint variant.\ncustom-resource:ResourceType:Property - The scalable dimension for a custom resource provided by your own application or service.\ncomprehend:document-classifier-endpoint:DesiredInferenceUnits - The number of inference units for an Amazon Comprehend document classification endpoint.\nlambda:function:ProvisionedConcurrency - The provisioned concurrency for a Lambda function.\ncassandra:table:ReadCapacityUnits - The provisioned read capacity for an Amazon Keyspaces table.\ncassandra:table:WriteCapacityUnits - The provisioned write capacity for an Amazon Keyspaces table.\n\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of scalable targets. This value can be between 1 and 50. The default value is 50.\nIf this parameter is used, the operation returns up to MaxResults results at a time, along with a NextToken value. To get the next set of results, include the NextToken value in a subsequent call. If this parameter is not used, the operation returns up to 50 results and a NextToken value, if applicable.\n

    :type NextToken: string
    :param NextToken: The token for the next set of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'ScalingPolicies': [
        {
            'PolicyARN': 'string',
            'PolicyName': 'string',
            'ServiceNamespace': 'ecs'|'elasticmapreduce'|'ec2'|'appstream'|'dynamodb'|'rds'|'sagemaker'|'custom-resource'|'comprehend'|'lambda'|'cassandra',
            'ResourceId': 'string',
            'ScalableDimension': 'ecs:service:DesiredCount'|'ec2:spot-fleet-request:TargetCapacity'|'elasticmapreduce:instancegroup:InstanceCount'|'appstream:fleet:DesiredCapacity'|'dynamodb:table:ReadCapacityUnits'|'dynamodb:table:WriteCapacityUnits'|'dynamodb:index:ReadCapacityUnits'|'dynamodb:index:WriteCapacityUnits'|'rds:cluster:ReadReplicaCount'|'sagemaker:variant:DesiredInstanceCount'|'custom-resource:ResourceType:Property'|'comprehend:document-classifier-endpoint:DesiredInferenceUnits'|'lambda:function:ProvisionedConcurrency'|'cassandra:table:ReadCapacityUnits'|'cassandra:table:WriteCapacityUnits',
            'PolicyType': 'StepScaling'|'TargetTrackingScaling',
            'StepScalingPolicyConfiguration': {
                'AdjustmentType': 'ChangeInCapacity'|'PercentChangeInCapacity'|'ExactCapacity',
                'StepAdjustments': [
                    {
                        'MetricIntervalLowerBound': 123.0,
                        'MetricIntervalUpperBound': 123.0,
                        'ScalingAdjustment': 123
                    },
                ],
                'MinAdjustmentMagnitude': 123,
                'Cooldown': 123,
                'MetricAggregationType': 'Average'|'Minimum'|'Maximum'
            },
            'TargetTrackingScalingPolicyConfiguration': {
                'TargetValue': 123.0,
                'PredefinedMetricSpecification': {
                    'PredefinedMetricType': 'DynamoDBReadCapacityUtilization'|'DynamoDBWriteCapacityUtilization'|'ALBRequestCountPerTarget'|'RDSReaderAverageCPUUtilization'|'RDSReaderAverageDatabaseConnections'|'EC2SpotFleetRequestAverageCPUUtilization'|'EC2SpotFleetRequestAverageNetworkIn'|'EC2SpotFleetRequestAverageNetworkOut'|'SageMakerVariantInvocationsPerInstance'|'ECSServiceAverageCPUUtilization'|'ECSServiceAverageMemoryUtilization'|'AppStreamAverageCapacityUtilization'|'ComprehendInferenceUtilization'|'LambdaProvisionedConcurrencyUtilization'|'CassandraReadCapacityUtilization'|'CassandraWriteCapacityUtilization',
                    'ResourceLabel': 'string'
                },
                'CustomizedMetricSpecification': {
                    'MetricName': 'string',
                    'Namespace': 'string',
                    'Dimensions': [
                        {
                            'Name': 'string',
                            'Value': 'string'
                        },
                    ],
                    'Statistic': 'Average'|'Minimum'|'Maximum'|'SampleCount'|'Sum',
                    'Unit': 'string'
                },
                'ScaleOutCooldown': 123,
                'ScaleInCooldown': 123,
                'DisableScaleIn': True|False
            },
            'Alarms': [
                {
                    'AlarmName': 'string',
                    'AlarmARN': 'string'
                },
            ],
            'CreationTime': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

ScalingPolicies (list) --
Information about the scaling policies.

(dict) --
Represents a scaling policy to use with Application Auto Scaling.

PolicyARN (string) --
The Amazon Resource Name (ARN) of the scaling policy.

PolicyName (string) --
The name of the scaling policy.

ServiceNamespace (string) --
The namespace of the AWS service that provides the resource, or a custom-resource .

ResourceId (string) --
The identifier of the resource associated with the scaling policy. This string consists of the resource type and unique identifier.

ECS service - The resource type is service and the unique identifier is the cluster name and service name. Example: service/default/sample-webapp .
Spot Fleet request - The resource type is spot-fleet-request and the unique identifier is the Spot Fleet request ID. Example: spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE .
EMR cluster - The resource type is instancegroup and the unique identifier is the cluster ID and instance group ID. Example: instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0 .
AppStream 2.0 fleet - The resource type is fleet and the unique identifier is the fleet name. Example: fleet/sample-fleet .
DynamoDB table - The resource type is table and the unique identifier is the table name. Example: table/my-table .
DynamoDB global secondary index - The resource type is index and the unique identifier is the index name. Example: table/my-table/index/my-table-index .
Aurora DB cluster - The resource type is cluster and the unique identifier is the cluster name. Example: cluster:my-db-cluster .
Amazon SageMaker endpoint variant - The resource type is variant and the unique identifier is the resource ID. Example: endpoint/my-end-point/variant/KMeansClustering .
Custom resources are not supported with a resource type. This parameter must specify the OutputValue from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider. More information is available in our GitHub repository .
Amazon Comprehend document classification endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE .
Lambda provisioned concurrency - The resource type is function and the unique identifier is the function name with a function version or alias name suffix that is not $LATEST . Example: function:my-function:prod or function:my-function:1 .
Amazon Keyspaces table - The resource type is table and the unique identifier is the table name. Example: keyspace/mykeyspace/table/mytable .


ScalableDimension (string) --
The scalable dimension. This string consists of the service namespace, resource type, and scaling property.

ecs:service:DesiredCount - The desired task count of an ECS service.
ec2:spot-fleet-request:TargetCapacity - The target capacity of a Spot Fleet request.
elasticmapreduce:instancegroup:InstanceCount - The instance count of an EMR Instance Group.
appstream:fleet:DesiredCapacity - The desired capacity of an AppStream 2.0 fleet.
dynamodb:table:ReadCapacityUnits - The provisioned read capacity for a DynamoDB table.
dynamodb:table:WriteCapacityUnits - The provisioned write capacity for a DynamoDB table.
dynamodb:index:ReadCapacityUnits - The provisioned read capacity for a DynamoDB global secondary index.
dynamodb:index:WriteCapacityUnits - The provisioned write capacity for a DynamoDB global secondary index.
rds:cluster:ReadReplicaCount - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition.
sagemaker:variant:DesiredInstanceCount - The number of EC2 instances for an Amazon SageMaker model endpoint variant.
custom-resource:ResourceType:Property - The scalable dimension for a custom resource provided by your own application or service.
comprehend:document-classifier-endpoint:DesiredInferenceUnits - The number of inference units for an Amazon Comprehend document classification endpoint.
lambda:function:ProvisionedConcurrency - The provisioned concurrency for a Lambda function.
cassandra:table:ReadCapacityUnits - The provisioned read capacity for an Amazon Keyspaces table.
cassandra:table:WriteCapacityUnits - The provisioned write capacity for an Amazon Keyspaces table.


PolicyType (string) --
The scaling policy type.

StepScalingPolicyConfiguration (dict) --
A step scaling policy.

AdjustmentType (string) --
Specifies whether the ScalingAdjustment value in a StepAdjustment is an absolute number or a percentage of the current capacity.

AdjustmentType is required if you are adding a new step scaling policy configuration.


StepAdjustments (list) --
A set of adjustments that enable you to scale based on the size of the alarm breach.
At least one step adjustment is required if you are adding a new step scaling policy configuration.

(dict) --
Represents a step adjustment for a StepScalingPolicyConfiguration . Describes an adjustment based on the difference between the value of the aggregated CloudWatch metric and the breach threshold that you\'ve defined for the alarm.
For the following examples, suppose that you have an alarm with a breach threshold of 50:

To trigger the adjustment when the metric is greater than or equal to 50 and less than 60, specify a lower bound of 0 and an upper bound of 10.
To trigger the adjustment when the metric is greater than 40 and less than or equal to 50, specify a lower bound of -10 and an upper bound of 0.

There are a few rules for the step adjustments for your step policy:

The ranges of your step adjustments can\'t overlap or have a gap.
At most one step adjustment can have a null lower bound. If one step adjustment has a negative lower bound, then there must be a step adjustment with a null lower bound.
At most one step adjustment can have a null upper bound. If one step adjustment has a positive upper bound, then there must be a step adjustment with a null upper bound.
The upper and lower bound can\'t be null in the same step adjustment.


MetricIntervalLowerBound (float) --
The lower bound for the difference between the alarm threshold and the CloudWatch metric. If the metric value is above the breach threshold, the lower bound is inclusive (the metric must be greater than or equal to the threshold plus the lower bound). Otherwise, it is exclusive (the metric must be greater than the threshold plus the lower bound). A null value indicates negative infinity.

MetricIntervalUpperBound (float) --
The upper bound for the difference between the alarm threshold and the CloudWatch metric. If the metric value is above the breach threshold, the upper bound is exclusive (the metric must be less than the threshold plus the upper bound). Otherwise, it is inclusive (the metric must be less than or equal to the threshold plus the upper bound). A null value indicates positive infinity.
The upper bound must be greater than the lower bound.

ScalingAdjustment (integer) --
The amount by which to scale, based on the specified adjustment type. A positive value adds to the current capacity while a negative number removes from the current capacity.





MinAdjustmentMagnitude (integer) --
The minimum value to scale by when scaling by percentages. For example, suppose that you create a step scaling policy to scale out an Amazon ECS service by 25 percent and you specify a MinAdjustmentMagnitude of 2. If the service has 4 tasks and the scaling policy is performed, 25 percent of 4 is 1. However, because you specified a MinAdjustmentMagnitude of 2, Application Auto Scaling scales out the service by 2 tasks.
Valid only if the adjustment type is PercentChangeInCapacity .

Cooldown (integer) --
The amount of time, in seconds, to wait for a previous scaling activity to take effect.
With scale-out policies, the intention is to continuously (but not excessively) scale out. After Application Auto Scaling successfully scales out using a step scaling policy, it starts to calculate the cooldown time. While the cooldown period is in effect, capacity added by the initiating scale-out activity is calculated as part of the desired capacity for the next scale-out activity. For example, when an alarm triggers a step scaling policy to increase the capacity by 2, the scaling activity completes successfully, and a cooldown period starts. If the alarm triggers again during the cooldown period but at a more aggressive step adjustment of 3, the previous increase of 2 is considered part of the current capacity. Therefore, only 1 is added to the capacity.
With scale-in policies, the intention is to scale in conservatively to protect your application\xe2\x80\x99s availability, so scale-in activities are blocked until the cooldown period has expired. However, if another alarm triggers a scale-out activity during the cooldown period after a scale-in activity, Application Auto Scaling scales out the target immediately. In this case, the cooldown period for the scale-in activity stops and doesn\'t complete.
Application Auto Scaling provides a default value of 300 for the following scalable targets:

ECS services
Spot Fleet requests
EMR clusters
AppStream 2.0 fleets
Aurora DB clusters
Amazon SageMaker endpoint variants
Custom resources

For all other scalable targets, the default value is 0:

DynamoDB tables
DynamoDB global secondary indexes
Amazon Comprehend document classification endpoints
Lambda provisioned concurrency
Amazon Keyspaces tables


MetricAggregationType (string) --
The aggregation type for the CloudWatch metrics. Valid values are Minimum , Maximum , and Average . If the aggregation type is null, the value is treated as Average .



TargetTrackingScalingPolicyConfiguration (dict) --
A target tracking scaling policy.

TargetValue (float) --
The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2).

PredefinedMetricSpecification (dict) --
A predefined metric. You can specify either a predefined metric or a customized metric.

PredefinedMetricType (string) --
The metric type. The ALBRequestCountPerTarget metric type applies only to Spot Fleet requests and ECS services.

ResourceLabel (string) --
Identifies the resource associated with the metric type. You can\'t specify a resource label unless the metric type is ALBRequestCountPerTarget and there is a target group attached to the Spot Fleet request or ECS service.
The format is app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>, where:

app/<load-balancer-name>/<load-balancer-id> is the final portion of the load balancer ARN
targetgroup/<target-group-name>/<target-group-id> is the final portion of the target group ARN.




CustomizedMetricSpecification (dict) --
A customized metric. You can specify either a predefined metric or a customized metric.

MetricName (string) --
The name of the metric.

Namespace (string) --
The namespace of the metric.

Dimensions (list) --
The dimensions of the metric.
Conditional: If you published your metric with dimensions, you must specify the same dimensions in your scaling policy.

(dict) --
Describes the dimension names and values associated with a metric.

Name (string) --
The name of the dimension.

Value (string) --
The value of the dimension.





Statistic (string) --
The statistic of the metric.

Unit (string) --
The unit of the metric.



ScaleOutCooldown (integer) --
The amount of time, in seconds, to wait for a previous scale-out activity to take effect.
With the scale-out cooldown period , the intention is to continuously (but not excessively) scale out. After Application Auto Scaling successfully scales out using a target tracking scaling policy, it starts to calculate the cooldown time. While the scale-out cooldown period is in effect, the capacity added by the initiating scale-out activity is calculated as part of the desired capacity for the next scale-out activity.
Application Auto Scaling provides a default value of 300 for the following scalable targets:

ECS services
Spot Fleet requests
EMR clusters
AppStream 2.0 fleets
Aurora DB clusters
Amazon SageMaker endpoint variants
Custom resources

For all other scalable targets, the default value is 0:

DynamoDB tables
DynamoDB global secondary indexes
Amazon Comprehend document classification endpoints
Lambda provisioned concurrency
Amazon Keyspaces tables


ScaleInCooldown (integer) --
The amount of time, in seconds, after a scale-in activity completes before another scale-in activity can start.
With the scale-in cooldown period , the intention is to scale in conservatively to protect your application\xe2\x80\x99s availability, so scale-in activities are blocked until the cooldown period has expired. However, if another alarm triggers a scale-out activity during the scale-in cooldown period, Application Auto Scaling scales out the target immediately. In this case, the scale-in cooldown period stops and doesn\'t complete.
Application Auto Scaling provides a default value of 300 for the following scalable targets:

ECS services
Spot Fleet requests
EMR clusters
AppStream 2.0 fleets
Aurora DB clusters
Amazon SageMaker endpoint variants
Custom resources

For all other scalable targets, the default value is 0:

DynamoDB tables
DynamoDB global secondary indexes
Amazon Comprehend document classification endpoints
Lambda provisioned concurrency
Amazon Keyspaces tables


DisableScaleIn (boolean) --
Indicates whether scale in by the target tracking scaling policy is disabled. If the value is true , scale in is disabled and the target tracking scaling policy won\'t remove capacity from the scalable target. Otherwise, scale in is enabled and the target tracking scaling policy can remove capacity from the scalable target. The default value is false .



Alarms (list) --
The CloudWatch alarms associated with the scaling policy.

(dict) --
Represents a CloudWatch alarm associated with a scaling policy.

AlarmName (string) --
The name of the alarm.

AlarmARN (string) --
The Amazon Resource Name (ARN) of the alarm.





CreationTime (datetime) --
The Unix timestamp for when the scaling policy was created.





NextToken (string) --
The token required to get the next set of results. This value is null if there are no more results to return.







Exceptions

ApplicationAutoScaling.Client.exceptions.ValidationException
ApplicationAutoScaling.Client.exceptions.FailedResourceAccessException
ApplicationAutoScaling.Client.exceptions.InvalidNextTokenException
ApplicationAutoScaling.Client.exceptions.ConcurrentUpdateException
ApplicationAutoScaling.Client.exceptions.InternalServiceException

Examples
This example describes the scaling policies for the ecs service namespace.
response = client.describe_scaling_policies(
    ServiceNamespace='ecs',
)

print(response)


Expected Output:
{
    'NextToken': '',
    'ScalingPolicies': [
        {
            'Alarms': [
                {
                    'AlarmARN': 'arn:aws:cloudwatch:us-west-2:012345678910:alarm:web-app-cpu-gt-75',
                    'AlarmName': 'web-app-cpu-gt-75',
                },
            ],
            'CreationTime': datetime(2016, 5, 6, 12, 11, 39, 4, 127, 0),
            'PolicyARN': 'arn:aws:autoscaling:us-west-2:012345678910:scalingPolicy:6d8972f3-efc8-437c-92d1-6270f29a66e7:resource/ecs/service/default/web-app:policyName/web-app-cpu-gt-75',
            'PolicyName': 'web-app-cpu-gt-75',
            'PolicyType': 'StepScaling',
            'ResourceId': 'service/default/web-app',
            'ScalableDimension': 'ecs:service:DesiredCount',
            'ServiceNamespace': 'ecs',
            'StepScalingPolicyConfiguration': {
                'AdjustmentType': 'PercentChangeInCapacity',
                'Cooldown': 60,
                'StepAdjustments': [
                    {
                        'MetricIntervalLowerBound': 0,
                        'ScalingAdjustment': 200,
                    },
                ],
            },
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ScalingPolicies': [
            {
                'PolicyARN': 'string',
                'PolicyName': 'string',
                'ServiceNamespace': 'ecs'|'elasticmapreduce'|'ec2'|'appstream'|'dynamodb'|'rds'|'sagemaker'|'custom-resource'|'comprehend'|'lambda'|'cassandra',
                'ResourceId': 'string',
                'ScalableDimension': 'ecs:service:DesiredCount'|'ec2:spot-fleet-request:TargetCapacity'|'elasticmapreduce:instancegroup:InstanceCount'|'appstream:fleet:DesiredCapacity'|'dynamodb:table:ReadCapacityUnits'|'dynamodb:table:WriteCapacityUnits'|'dynamodb:index:ReadCapacityUnits'|'dynamodb:index:WriteCapacityUnits'|'rds:cluster:ReadReplicaCount'|'sagemaker:variant:DesiredInstanceCount'|'custom-resource:ResourceType:Property'|'comprehend:document-classifier-endpoint:DesiredInferenceUnits'|'lambda:function:ProvisionedConcurrency'|'cassandra:table:ReadCapacityUnits'|'cassandra:table:WriteCapacityUnits',
                'PolicyType': 'StepScaling'|'TargetTrackingScaling',
                'StepScalingPolicyConfiguration': {
                    'AdjustmentType': 'ChangeInCapacity'|'PercentChangeInCapacity'|'ExactCapacity',
                    'StepAdjustments': [
                        {
                            'MetricIntervalLowerBound': 123.0,
                            'MetricIntervalUpperBound': 123.0,
                            'ScalingAdjustment': 123
                        },
                    ],
                    'MinAdjustmentMagnitude': 123,
                    'Cooldown': 123,
                    'MetricAggregationType': 'Average'|'Minimum'|'Maximum'
                },
                'TargetTrackingScalingPolicyConfiguration': {
                    'TargetValue': 123.0,
                    'PredefinedMetricSpecification': {
                        'PredefinedMetricType': 'DynamoDBReadCapacityUtilization'|'DynamoDBWriteCapacityUtilization'|'ALBRequestCountPerTarget'|'RDSReaderAverageCPUUtilization'|'RDSReaderAverageDatabaseConnections'|'EC2SpotFleetRequestAverageCPUUtilization'|'EC2SpotFleetRequestAverageNetworkIn'|'EC2SpotFleetRequestAverageNetworkOut'|'SageMakerVariantInvocationsPerInstance'|'ECSServiceAverageCPUUtilization'|'ECSServiceAverageMemoryUtilization'|'AppStreamAverageCapacityUtilization'|'ComprehendInferenceUtilization'|'LambdaProvisionedConcurrencyUtilization'|'CassandraReadCapacityUtilization'|'CassandraWriteCapacityUtilization',
                        'ResourceLabel': 'string'
                    },
                    'CustomizedMetricSpecification': {
                        'MetricName': 'string',
                        'Namespace': 'string',
                        'Dimensions': [
                            {
                                'Name': 'string',
                                'Value': 'string'
                            },
                        ],
                        'Statistic': 'Average'|'Minimum'|'Maximum'|'SampleCount'|'Sum',
                        'Unit': 'string'
                    },
                    'ScaleOutCooldown': 123,
                    'ScaleInCooldown': 123,
                    'DisableScaleIn': True|False
                },
                'Alarms': [
                    {
                        'AlarmName': 'string',
                        'AlarmARN': 'string'
                    },
                ],
                'CreationTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    ECS service - The resource type is service and the unique identifier is the cluster name and service name. Example: service/default/sample-webapp .
    Spot Fleet request - The resource type is spot-fleet-request and the unique identifier is the Spot Fleet request ID. Example: spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE .
    EMR cluster - The resource type is instancegroup and the unique identifier is the cluster ID and instance group ID. Example: instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0 .
    AppStream 2.0 fleet - The resource type is fleet and the unique identifier is the fleet name. Example: fleet/sample-fleet .
    DynamoDB table - The resource type is table and the unique identifier is the table name. Example: table/my-table .
    DynamoDB global secondary index - The resource type is index and the unique identifier is the index name. Example: table/my-table/index/my-table-index .
    Aurora DB cluster - The resource type is cluster and the unique identifier is the cluster name. Example: cluster:my-db-cluster .
    Amazon SageMaker endpoint variant - The resource type is variant and the unique identifier is the resource ID. Example: endpoint/my-end-point/variant/KMeansClustering .
    Custom resources are not supported with a resource type. This parameter must specify the OutputValue from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider. More information is available in our GitHub repository .
    Amazon Comprehend document classification endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE .
    Lambda provisioned concurrency - The resource type is function and the unique identifier is the function name with a function version or alias name suffix that is not $LATEST . Example: function:my-function:prod or function:my-function:1 .
    Amazon Keyspaces table - The resource type is table and the unique identifier is the table name. Example: keyspace/mykeyspace/table/mytable .
    
    """
    pass

def describe_scheduled_actions(ScheduledActionNames=None, ServiceNamespace=None, ResourceId=None, ScalableDimension=None, MaxResults=None, NextToken=None):
    """
    Describes the Application Auto Scaling scheduled actions for the specified service namespace.
    You can filter the results using the ResourceId , ScalableDimension , and ScheduledActionNames parameters.
    For more information, see Scheduled Scaling in the Application Auto Scaling User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_scheduled_actions(
        ScheduledActionNames=[
            'string',
        ],
        ServiceNamespace='ecs'|'elasticmapreduce'|'ec2'|'appstream'|'dynamodb'|'rds'|'sagemaker'|'custom-resource'|'comprehend'|'lambda'|'cassandra',
        ResourceId='string',
        ScalableDimension='ecs:service:DesiredCount'|'ec2:spot-fleet-request:TargetCapacity'|'elasticmapreduce:instancegroup:InstanceCount'|'appstream:fleet:DesiredCapacity'|'dynamodb:table:ReadCapacityUnits'|'dynamodb:table:WriteCapacityUnits'|'dynamodb:index:ReadCapacityUnits'|'dynamodb:index:WriteCapacityUnits'|'rds:cluster:ReadReplicaCount'|'sagemaker:variant:DesiredInstanceCount'|'custom-resource:ResourceType:Property'|'comprehend:document-classifier-endpoint:DesiredInferenceUnits'|'lambda:function:ProvisionedConcurrency'|'cassandra:table:ReadCapacityUnits'|'cassandra:table:WriteCapacityUnits',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type ScheduledActionNames: list
    :param ScheduledActionNames: The names of the scheduled actions to describe.\n\n(string) --\n\n

    :type ServiceNamespace: string
    :param ServiceNamespace: [REQUIRED]\nThe namespace of the AWS service that provides the resource. For a resource provided by your own application or service, use custom-resource instead.\n

    :type ResourceId: string
    :param ResourceId: The identifier of the resource associated with the scheduled action. This string consists of the resource type and unique identifier. If you specify a scalable dimension, you must also specify a resource ID.\n\nECS service - The resource type is service and the unique identifier is the cluster name and service name. Example: service/default/sample-webapp .\nSpot Fleet request - The resource type is spot-fleet-request and the unique identifier is the Spot Fleet request ID. Example: spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE .\nEMR cluster - The resource type is instancegroup and the unique identifier is the cluster ID and instance group ID. Example: instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0 .\nAppStream 2.0 fleet - The resource type is fleet and the unique identifier is the fleet name. Example: fleet/sample-fleet .\nDynamoDB table - The resource type is table and the unique identifier is the table name. Example: table/my-table .\nDynamoDB global secondary index - The resource type is index and the unique identifier is the index name. Example: table/my-table/index/my-table-index .\nAurora DB cluster - The resource type is cluster and the unique identifier is the cluster name. Example: cluster:my-db-cluster .\nAmazon SageMaker endpoint variant - The resource type is variant and the unique identifier is the resource ID. Example: endpoint/my-end-point/variant/KMeansClustering .\nCustom resources are not supported with a resource type. This parameter must specify the OutputValue from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider. More information is available in our GitHub repository .\nAmazon Comprehend document classification endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE .\nLambda provisioned concurrency - The resource type is function and the unique identifier is the function name with a function version or alias name suffix that is not $LATEST . Example: function:my-function:prod or function:my-function:1 .\nAmazon Keyspaces table - The resource type is table and the unique identifier is the table name. Example: keyspace/mykeyspace/table/mytable .\n\n

    :type ScalableDimension: string
    :param ScalableDimension: The scalable dimension. This string consists of the service namespace, resource type, and scaling property. If you specify a scalable dimension, you must also specify a resource ID.\n\necs:service:DesiredCount - The desired task count of an ECS service.\nec2:spot-fleet-request:TargetCapacity - The target capacity of a Spot Fleet request.\nelasticmapreduce:instancegroup:InstanceCount - The instance count of an EMR Instance Group.\nappstream:fleet:DesiredCapacity - The desired capacity of an AppStream 2.0 fleet.\ndynamodb:table:ReadCapacityUnits - The provisioned read capacity for a DynamoDB table.\ndynamodb:table:WriteCapacityUnits - The provisioned write capacity for a DynamoDB table.\ndynamodb:index:ReadCapacityUnits - The provisioned read capacity for a DynamoDB global secondary index.\ndynamodb:index:WriteCapacityUnits - The provisioned write capacity for a DynamoDB global secondary index.\nrds:cluster:ReadReplicaCount - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition.\nsagemaker:variant:DesiredInstanceCount - The number of EC2 instances for an Amazon SageMaker model endpoint variant.\ncustom-resource:ResourceType:Property - The scalable dimension for a custom resource provided by your own application or service.\ncomprehend:document-classifier-endpoint:DesiredInferenceUnits - The number of inference units for an Amazon Comprehend document classification endpoint.\nlambda:function:ProvisionedConcurrency - The provisioned concurrency for a Lambda function.\ncassandra:table:ReadCapacityUnits - The provisioned read capacity for an Amazon Keyspaces table.\ncassandra:table:WriteCapacityUnits - The provisioned write capacity for an Amazon Keyspaces table.\n\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of scheduled action results. This value can be between 1 and 50. The default value is 50.\nIf this parameter is used, the operation returns up to MaxResults results at a time, along with a NextToken value. To get the next set of results, include the NextToken value in a subsequent call. If this parameter is not used, the operation returns up to 50 results and a NextToken value, if applicable.\n

    :type NextToken: string
    :param NextToken: The token for the next set of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'ScheduledActions': [
        {
            'ScheduledActionName': 'string',
            'ScheduledActionARN': 'string',
            'ServiceNamespace': 'ecs'|'elasticmapreduce'|'ec2'|'appstream'|'dynamodb'|'rds'|'sagemaker'|'custom-resource'|'comprehend'|'lambda'|'cassandra',
            'Schedule': 'string',
            'ResourceId': 'string',
            'ScalableDimension': 'ecs:service:DesiredCount'|'ec2:spot-fleet-request:TargetCapacity'|'elasticmapreduce:instancegroup:InstanceCount'|'appstream:fleet:DesiredCapacity'|'dynamodb:table:ReadCapacityUnits'|'dynamodb:table:WriteCapacityUnits'|'dynamodb:index:ReadCapacityUnits'|'dynamodb:index:WriteCapacityUnits'|'rds:cluster:ReadReplicaCount'|'sagemaker:variant:DesiredInstanceCount'|'custom-resource:ResourceType:Property'|'comprehend:document-classifier-endpoint:DesiredInferenceUnits'|'lambda:function:ProvisionedConcurrency'|'cassandra:table:ReadCapacityUnits'|'cassandra:table:WriteCapacityUnits',
            'StartTime': datetime(2015, 1, 1),
            'EndTime': datetime(2015, 1, 1),
            'ScalableTargetAction': {
                'MinCapacity': 123,
                'MaxCapacity': 123
            },
            'CreationTime': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

ScheduledActions (list) --
Information about the scheduled actions.

(dict) --
Represents a scheduled action.

ScheduledActionName (string) --
The name of the scheduled action.

ScheduledActionARN (string) --
The Amazon Resource Name (ARN) of the scheduled action.

ServiceNamespace (string) --
The namespace of the AWS service that provides the resource, or a custom-resource .

Schedule (string) --
The schedule for this action. The following formats are supported:

At expressions - "at(*yyyy* -*mm* -*dd* T*hh* :*mm* :*ss* ) "
Rate expressions - "rate(*value* *unit* ) "
Cron expressions - "cron(*fields* ) "

At expressions are useful for one-time schedules. Specify the time in UTC.
For rate expressions, value is a positive integer and unit is minute | minutes | hour | hours | day | days .
For more information about cron expressions, see Cron Expressions in the Amazon CloudWatch Events User Guide .
For examples of using these expressions, see Scheduled Scaling in the Application Auto Scaling User Guide .

ResourceId (string) --
The identifier of the resource associated with the scaling policy. This string consists of the resource type and unique identifier.

ECS service - The resource type is service and the unique identifier is the cluster name and service name. Example: service/default/sample-webapp .
Spot Fleet request - The resource type is spot-fleet-request and the unique identifier is the Spot Fleet request ID. Example: spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE .
EMR cluster - The resource type is instancegroup and the unique identifier is the cluster ID and instance group ID. Example: instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0 .
AppStream 2.0 fleet - The resource type is fleet and the unique identifier is the fleet name. Example: fleet/sample-fleet .
DynamoDB table - The resource type is table and the unique identifier is the table name. Example: table/my-table .
DynamoDB global secondary index - The resource type is index and the unique identifier is the index name. Example: table/my-table/index/my-table-index .
Aurora DB cluster - The resource type is cluster and the unique identifier is the cluster name. Example: cluster:my-db-cluster .
Amazon SageMaker endpoint variant - The resource type is variant and the unique identifier is the resource ID. Example: endpoint/my-end-point/variant/KMeansClustering .
Custom resources are not supported with a resource type. This parameter must specify the OutputValue from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider. More information is available in our GitHub repository .
Amazon Comprehend document classification endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE .
Lambda provisioned concurrency - The resource type is function and the unique identifier is the function name with a function version or alias name suffix that is not $LATEST . Example: function:my-function:prod or function:my-function:1 .
Amazon Keyspaces table - The resource type is table and the unique identifier is the table name. Example: keyspace/mykeyspace/table/mytable .


ScalableDimension (string) --
The scalable dimension. This string consists of the service namespace, resource type, and scaling property.

ecs:service:DesiredCount - The desired task count of an ECS service.
ec2:spot-fleet-request:TargetCapacity - The target capacity of a Spot Fleet request.
elasticmapreduce:instancegroup:InstanceCount - The instance count of an EMR Instance Group.
appstream:fleet:DesiredCapacity - The desired capacity of an AppStream 2.0 fleet.
dynamodb:table:ReadCapacityUnits - The provisioned read capacity for a DynamoDB table.
dynamodb:table:WriteCapacityUnits - The provisioned write capacity for a DynamoDB table.
dynamodb:index:ReadCapacityUnits - The provisioned read capacity for a DynamoDB global secondary index.
dynamodb:index:WriteCapacityUnits - The provisioned write capacity for a DynamoDB global secondary index.
rds:cluster:ReadReplicaCount - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition.
sagemaker:variant:DesiredInstanceCount - The number of EC2 instances for an Amazon SageMaker model endpoint variant.
custom-resource:ResourceType:Property - The scalable dimension for a custom resource provided by your own application or service.
comprehend:document-classifier-endpoint:DesiredInferenceUnits - The number of inference units for an Amazon Comprehend document classification endpoint.
lambda:function:ProvisionedConcurrency - The provisioned concurrency for a Lambda function.
cassandra:table:ReadCapacityUnits - The provisioned read capacity for an Amazon Keyspaces table.
cassandra:table:WriteCapacityUnits - The provisioned write capacity for an Amazon Keyspaces table.


StartTime (datetime) --
The date and time that the action is scheduled to begin.

EndTime (datetime) --
The date and time that the action is scheduled to end.

ScalableTargetAction (dict) --
The new minimum and maximum capacity. You can set both values or just one. At the scheduled time, if the current capacity is below the minimum capacity, Application Auto Scaling scales out to the minimum capacity. If the current capacity is above the maximum capacity, Application Auto Scaling scales in to the maximum capacity.

MinCapacity (integer) --
The minimum capacity.
For Lambda provisioned concurrency, the minimum value allowed is 0. For all other resources, the minimum value allowed is 1.

MaxCapacity (integer) --
The maximum capacity.



CreationTime (datetime) --
The date and time that the scheduled action was created.





NextToken (string) --
The token required to get the next set of results. This value is null if there are no more results to return.







Exceptions

ApplicationAutoScaling.Client.exceptions.ValidationException
ApplicationAutoScaling.Client.exceptions.InvalidNextTokenException
ApplicationAutoScaling.Client.exceptions.ConcurrentUpdateException
ApplicationAutoScaling.Client.exceptions.InternalServiceException


    :return: {
        'ScheduledActions': [
            {
                'ScheduledActionName': 'string',
                'ScheduledActionARN': 'string',
                'ServiceNamespace': 'ecs'|'elasticmapreduce'|'ec2'|'appstream'|'dynamodb'|'rds'|'sagemaker'|'custom-resource'|'comprehend'|'lambda'|'cassandra',
                'Schedule': 'string',
                'ResourceId': 'string',
                'ScalableDimension': 'ecs:service:DesiredCount'|'ec2:spot-fleet-request:TargetCapacity'|'elasticmapreduce:instancegroup:InstanceCount'|'appstream:fleet:DesiredCapacity'|'dynamodb:table:ReadCapacityUnits'|'dynamodb:table:WriteCapacityUnits'|'dynamodb:index:ReadCapacityUnits'|'dynamodb:index:WriteCapacityUnits'|'rds:cluster:ReadReplicaCount'|'sagemaker:variant:DesiredInstanceCount'|'custom-resource:ResourceType:Property'|'comprehend:document-classifier-endpoint:DesiredInferenceUnits'|'lambda:function:ProvisionedConcurrency'|'cassandra:table:ReadCapacityUnits'|'cassandra:table:WriteCapacityUnits',
                'StartTime': datetime(2015, 1, 1),
                'EndTime': datetime(2015, 1, 1),
                'ScalableTargetAction': {
                    'MinCapacity': 123,
                    'MaxCapacity': 123
                },
                'CreationTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    At expressions - "at(*yyyy* -*mm* -*dd* T*hh* :*mm* :*ss* ) "
    Rate expressions - "rate(*value* *unit* ) "
    Cron expressions - "cron(*fields* ) "
    
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

def get_waiter(waiter_name=None):
    """
    Returns an object that can wait for some condition.
    
    :type waiter_name: str
    :param waiter_name: The name of the waiter to get. See the waiters\nsection of the service docs for a list of available waiters.

    :rtype: botocore.waiter.Waiter


    """
    pass

def put_scaling_policy(PolicyName=None, ServiceNamespace=None, ResourceId=None, ScalableDimension=None, PolicyType=None, StepScalingPolicyConfiguration=None, TargetTrackingScalingPolicyConfiguration=None):
    """
    Creates or updates a scaling policy for an Application Auto Scaling scalable target.
    Each scalable target is identified by a service namespace, resource ID, and scalable dimension. A scaling policy applies to the scalable target identified by those three attributes. You cannot create a scaling policy until you have registered the resource as a scalable target.
    Multiple scaling policies can be in force at the same time for the same scalable target. You can have one or more target tracking scaling policies, one or more step scaling policies, or both. However, there is a chance that multiple policies could conflict, instructing the scalable target to scale out or in at the same time. Application Auto Scaling gives precedence to the policy that provides the largest capacity for both scale out and scale in. For example, if one policy increases capacity by 3, another policy increases capacity by 200 percent, and the current capacity is 10, Application Auto Scaling uses the policy with the highest calculated capacity (200% of 10 = 20) and scales out to 30.
    We recommend caution, however, when using target tracking scaling policies with step scaling policies because conflicts between these policies can cause undesirable behavior. For example, if the step scaling policy initiates a scale-in activity before the target tracking policy is ready to scale in, the scale-in activity will not be blocked. After the scale-in activity completes, the target tracking policy could instruct the scalable target to scale out again.
    For more information, see Target Tracking Scaling Policies and Step Scaling Policies in the Application Auto Scaling User Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example applies a scaling policy to an Amazon ECS service called web-app in the default cluster. The policy increases the desired count of the service by 200%, with a cool down period of 60 seconds.
    Expected Output:
    This example applies a scaling policy to an Amazon EC2 Spot fleet. The policy increases the target capacity of the spot fleet by 200%, with a cool down period of 180 seconds.",
    Expected Output:
    
    :example: response = client.put_scaling_policy(
        PolicyName='string',
        ServiceNamespace='ecs'|'elasticmapreduce'|'ec2'|'appstream'|'dynamodb'|'rds'|'sagemaker'|'custom-resource'|'comprehend'|'lambda'|'cassandra',
        ResourceId='string',
        ScalableDimension='ecs:service:DesiredCount'|'ec2:spot-fleet-request:TargetCapacity'|'elasticmapreduce:instancegroup:InstanceCount'|'appstream:fleet:DesiredCapacity'|'dynamodb:table:ReadCapacityUnits'|'dynamodb:table:WriteCapacityUnits'|'dynamodb:index:ReadCapacityUnits'|'dynamodb:index:WriteCapacityUnits'|'rds:cluster:ReadReplicaCount'|'sagemaker:variant:DesiredInstanceCount'|'custom-resource:ResourceType:Property'|'comprehend:document-classifier-endpoint:DesiredInferenceUnits'|'lambda:function:ProvisionedConcurrency'|'cassandra:table:ReadCapacityUnits'|'cassandra:table:WriteCapacityUnits',
        PolicyType='StepScaling'|'TargetTrackingScaling',
        StepScalingPolicyConfiguration={
            'AdjustmentType': 'ChangeInCapacity'|'PercentChangeInCapacity'|'ExactCapacity',
            'StepAdjustments': [
                {
                    'MetricIntervalLowerBound': 123.0,
                    'MetricIntervalUpperBound': 123.0,
                    'ScalingAdjustment': 123
                },
            ],
            'MinAdjustmentMagnitude': 123,
            'Cooldown': 123,
            'MetricAggregationType': 'Average'|'Minimum'|'Maximum'
        },
        TargetTrackingScalingPolicyConfiguration={
            'TargetValue': 123.0,
            'PredefinedMetricSpecification': {
                'PredefinedMetricType': 'DynamoDBReadCapacityUtilization'|'DynamoDBWriteCapacityUtilization'|'ALBRequestCountPerTarget'|'RDSReaderAverageCPUUtilization'|'RDSReaderAverageDatabaseConnections'|'EC2SpotFleetRequestAverageCPUUtilization'|'EC2SpotFleetRequestAverageNetworkIn'|'EC2SpotFleetRequestAverageNetworkOut'|'SageMakerVariantInvocationsPerInstance'|'ECSServiceAverageCPUUtilization'|'ECSServiceAverageMemoryUtilization'|'AppStreamAverageCapacityUtilization'|'ComprehendInferenceUtilization'|'LambdaProvisionedConcurrencyUtilization'|'CassandraReadCapacityUtilization'|'CassandraWriteCapacityUtilization',
                'ResourceLabel': 'string'
            },
            'CustomizedMetricSpecification': {
                'MetricName': 'string',
                'Namespace': 'string',
                'Dimensions': [
                    {
                        'Name': 'string',
                        'Value': 'string'
                    },
                ],
                'Statistic': 'Average'|'Minimum'|'Maximum'|'SampleCount'|'Sum',
                'Unit': 'string'
            },
            'ScaleOutCooldown': 123,
            'ScaleInCooldown': 123,
            'DisableScaleIn': True|False
        }
    )
    
    
    :type PolicyName: string
    :param PolicyName: [REQUIRED]\nThe name of the scaling policy.\n

    :type ServiceNamespace: string
    :param ServiceNamespace: [REQUIRED]\nThe namespace of the AWS service that provides the resource. For a resource provided by your own application or service, use custom-resource instead.\n

    :type ResourceId: string
    :param ResourceId: [REQUIRED]\nThe identifier of the resource associated with the scaling policy. This string consists of the resource type and unique identifier.\n\nECS service - The resource type is service and the unique identifier is the cluster name and service name. Example: service/default/sample-webapp .\nSpot Fleet request - The resource type is spot-fleet-request and the unique identifier is the Spot Fleet request ID. Example: spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE .\nEMR cluster - The resource type is instancegroup and the unique identifier is the cluster ID and instance group ID. Example: instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0 .\nAppStream 2.0 fleet - The resource type is fleet and the unique identifier is the fleet name. Example: fleet/sample-fleet .\nDynamoDB table - The resource type is table and the unique identifier is the table name. Example: table/my-table .\nDynamoDB global secondary index - The resource type is index and the unique identifier is the index name. Example: table/my-table/index/my-table-index .\nAurora DB cluster - The resource type is cluster and the unique identifier is the cluster name. Example: cluster:my-db-cluster .\nAmazon SageMaker endpoint variant - The resource type is variant and the unique identifier is the resource ID. Example: endpoint/my-end-point/variant/KMeansClustering .\nCustom resources are not supported with a resource type. This parameter must specify the OutputValue from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider. More information is available in our GitHub repository .\nAmazon Comprehend document classification endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE .\nLambda provisioned concurrency - The resource type is function and the unique identifier is the function name with a function version or alias name suffix that is not $LATEST . Example: function:my-function:prod or function:my-function:1 .\nAmazon Keyspaces table - The resource type is table and the unique identifier is the table name. Example: keyspace/mykeyspace/table/mytable .\n\n

    :type ScalableDimension: string
    :param ScalableDimension: [REQUIRED]\nThe scalable dimension. This string consists of the service namespace, resource type, and scaling property.\n\necs:service:DesiredCount - The desired task count of an ECS service.\nec2:spot-fleet-request:TargetCapacity - The target capacity of a Spot Fleet request.\nelasticmapreduce:instancegroup:InstanceCount - The instance count of an EMR Instance Group.\nappstream:fleet:DesiredCapacity - The desired capacity of an AppStream 2.0 fleet.\ndynamodb:table:ReadCapacityUnits - The provisioned read capacity for a DynamoDB table.\ndynamodb:table:WriteCapacityUnits - The provisioned write capacity for a DynamoDB table.\ndynamodb:index:ReadCapacityUnits - The provisioned read capacity for a DynamoDB global secondary index.\ndynamodb:index:WriteCapacityUnits - The provisioned write capacity for a DynamoDB global secondary index.\nrds:cluster:ReadReplicaCount - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition.\nsagemaker:variant:DesiredInstanceCount - The number of EC2 instances for an Amazon SageMaker model endpoint variant.\ncustom-resource:ResourceType:Property - The scalable dimension for a custom resource provided by your own application or service.\ncomprehend:document-classifier-endpoint:DesiredInferenceUnits - The number of inference units for an Amazon Comprehend document classification endpoint.\nlambda:function:ProvisionedConcurrency - The provisioned concurrency for a Lambda function.\ncassandra:table:ReadCapacityUnits - The provisioned read capacity for an Amazon Keyspaces table.\ncassandra:table:WriteCapacityUnits - The provisioned write capacity for an Amazon Keyspaces table.\n\n

    :type PolicyType: string
    :param PolicyType: The policy type. This parameter is required if you are creating a scaling policy.\nThe following policy types are supported:\n\nTargetTrackingScaling \xe2\x80\x94Not supported for Amazon EMRStepScaling \xe2\x80\x94Not supported for DynamoDB, Amazon Comprehend, Lambda, or Amazon Keyspaces (for Apache Cassandra).\n\nFor more information, see Target Tracking Scaling Policies and Step Scaling Policies in the Application Auto Scaling User Guide .\n

    :type StepScalingPolicyConfiguration: dict
    :param StepScalingPolicyConfiguration: A step scaling policy.\nThis parameter is required if you are creating a policy and the policy type is StepScaling .\n\nAdjustmentType (string) --Specifies whether the ScalingAdjustment value in a StepAdjustment is an absolute number or a percentage of the current capacity.\n\nAdjustmentType is required if you are adding a new step scaling policy configuration.\n\nStepAdjustments (list) --A set of adjustments that enable you to scale based on the size of the alarm breach.\nAt least one step adjustment is required if you are adding a new step scaling policy configuration.\n\n(dict) --Represents a step adjustment for a StepScalingPolicyConfiguration . Describes an adjustment based on the difference between the value of the aggregated CloudWatch metric and the breach threshold that you\'ve defined for the alarm.\nFor the following examples, suppose that you have an alarm with a breach threshold of 50:\n\nTo trigger the adjustment when the metric is greater than or equal to 50 and less than 60, specify a lower bound of 0 and an upper bound of 10.\nTo trigger the adjustment when the metric is greater than 40 and less than or equal to 50, specify a lower bound of -10 and an upper bound of 0.\n\nThere are a few rules for the step adjustments for your step policy:\n\nThe ranges of your step adjustments can\'t overlap or have a gap.\nAt most one step adjustment can have a null lower bound. If one step adjustment has a negative lower bound, then there must be a step adjustment with a null lower bound.\nAt most one step adjustment can have a null upper bound. If one step adjustment has a positive upper bound, then there must be a step adjustment with a null upper bound.\nThe upper and lower bound can\'t be null in the same step adjustment.\n\n\nMetricIntervalLowerBound (float) --The lower bound for the difference between the alarm threshold and the CloudWatch metric. If the metric value is above the breach threshold, the lower bound is inclusive (the metric must be greater than or equal to the threshold plus the lower bound). Otherwise, it is exclusive (the metric must be greater than the threshold plus the lower bound). A null value indicates negative infinity.\n\nMetricIntervalUpperBound (float) --The upper bound for the difference between the alarm threshold and the CloudWatch metric. If the metric value is above the breach threshold, the upper bound is exclusive (the metric must be less than the threshold plus the upper bound). Otherwise, it is inclusive (the metric must be less than or equal to the threshold plus the upper bound). A null value indicates positive infinity.\nThe upper bound must be greater than the lower bound.\n\nScalingAdjustment (integer) -- [REQUIRED]The amount by which to scale, based on the specified adjustment type. A positive value adds to the current capacity while a negative number removes from the current capacity.\n\n\n\n\n\nMinAdjustmentMagnitude (integer) --The minimum value to scale by when scaling by percentages. For example, suppose that you create a step scaling policy to scale out an Amazon ECS service by 25 percent and you specify a MinAdjustmentMagnitude of 2. If the service has 4 tasks and the scaling policy is performed, 25 percent of 4 is 1. However, because you specified a MinAdjustmentMagnitude of 2, Application Auto Scaling scales out the service by 2 tasks.\nValid only if the adjustment type is PercentChangeInCapacity .\n\nCooldown (integer) --The amount of time, in seconds, to wait for a previous scaling activity to take effect.\nWith scale-out policies, the intention is to continuously (but not excessively) scale out. After Application Auto Scaling successfully scales out using a step scaling policy, it starts to calculate the cooldown time. While the cooldown period is in effect, capacity added by the initiating scale-out activity is calculated as part of the desired capacity for the next scale-out activity. For example, when an alarm triggers a step scaling policy to increase the capacity by 2, the scaling activity completes successfully, and a cooldown period starts. If the alarm triggers again during the cooldown period but at a more aggressive step adjustment of 3, the previous increase of 2 is considered part of the current capacity. Therefore, only 1 is added to the capacity.\nWith scale-in policies, the intention is to scale in conservatively to protect your application\xe2\x80\x99s availability, so scale-in activities are blocked until the cooldown period has expired. However, if another alarm triggers a scale-out activity during the cooldown period after a scale-in activity, Application Auto Scaling scales out the target immediately. In this case, the cooldown period for the scale-in activity stops and doesn\'t complete.\nApplication Auto Scaling provides a default value of 300 for the following scalable targets:\n\nECS services\nSpot Fleet requests\nEMR clusters\nAppStream 2.0 fleets\nAurora DB clusters\nAmazon SageMaker endpoint variants\nCustom resources\n\nFor all other scalable targets, the default value is 0:\n\nDynamoDB tables\nDynamoDB global secondary indexes\nAmazon Comprehend document classification endpoints\nLambda provisioned concurrency\nAmazon Keyspaces tables\n\n\nMetricAggregationType (string) --The aggregation type for the CloudWatch metrics. Valid values are Minimum , Maximum , and Average . If the aggregation type is null, the value is treated as Average .\n\n\n

    :type TargetTrackingScalingPolicyConfiguration: dict
    :param TargetTrackingScalingPolicyConfiguration: A target tracking scaling policy. Includes support for predefined or customized metrics.\nThis parameter is required if you are creating a policy and the policy type is TargetTrackingScaling .\n\nTargetValue (float) -- [REQUIRED]The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2).\n\nPredefinedMetricSpecification (dict) --A predefined metric. You can specify either a predefined metric or a customized metric.\n\nPredefinedMetricType (string) -- [REQUIRED]The metric type. The ALBRequestCountPerTarget metric type applies only to Spot Fleet requests and ECS services.\n\nResourceLabel (string) --Identifies the resource associated with the metric type. You can\'t specify a resource label unless the metric type is ALBRequestCountPerTarget and there is a target group attached to the Spot Fleet request or ECS service.\nThe format is app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>, where:\n\napp/<load-balancer-name>/<load-balancer-id> is the final portion of the load balancer ARN\ntargetgroup/<target-group-name>/<target-group-id> is the final portion of the target group ARN.\n\n\n\n\nCustomizedMetricSpecification (dict) --A customized metric. You can specify either a predefined metric or a customized metric.\n\nMetricName (string) -- [REQUIRED]The name of the metric.\n\nNamespace (string) -- [REQUIRED]The namespace of the metric.\n\nDimensions (list) --The dimensions of the metric.\nConditional: If you published your metric with dimensions, you must specify the same dimensions in your scaling policy.\n\n(dict) --Describes the dimension names and values associated with a metric.\n\nName (string) -- [REQUIRED]The name of the dimension.\n\nValue (string) -- [REQUIRED]The value of the dimension.\n\n\n\n\n\nStatistic (string) -- [REQUIRED]The statistic of the metric.\n\nUnit (string) --The unit of the metric.\n\n\n\nScaleOutCooldown (integer) --The amount of time, in seconds, to wait for a previous scale-out activity to take effect.\nWith the scale-out cooldown period , the intention is to continuously (but not excessively) scale out. After Application Auto Scaling successfully scales out using a target tracking scaling policy, it starts to calculate the cooldown time. While the scale-out cooldown period is in effect, the capacity added by the initiating scale-out activity is calculated as part of the desired capacity for the next scale-out activity.\nApplication Auto Scaling provides a default value of 300 for the following scalable targets:\n\nECS services\nSpot Fleet requests\nEMR clusters\nAppStream 2.0 fleets\nAurora DB clusters\nAmazon SageMaker endpoint variants\nCustom resources\n\nFor all other scalable targets, the default value is 0:\n\nDynamoDB tables\nDynamoDB global secondary indexes\nAmazon Comprehend document classification endpoints\nLambda provisioned concurrency\nAmazon Keyspaces tables\n\n\nScaleInCooldown (integer) --The amount of time, in seconds, after a scale-in activity completes before another scale-in activity can start.\nWith the scale-in cooldown period , the intention is to scale in conservatively to protect your application\xe2\x80\x99s availability, so scale-in activities are blocked until the cooldown period has expired. However, if another alarm triggers a scale-out activity during the scale-in cooldown period, Application Auto Scaling scales out the target immediately. In this case, the scale-in cooldown period stops and doesn\'t complete.\nApplication Auto Scaling provides a default value of 300 for the following scalable targets:\n\nECS services\nSpot Fleet requests\nEMR clusters\nAppStream 2.0 fleets\nAurora DB clusters\nAmazon SageMaker endpoint variants\nCustom resources\n\nFor all other scalable targets, the default value is 0:\n\nDynamoDB tables\nDynamoDB global secondary indexes\nAmazon Comprehend document classification endpoints\nLambda provisioned concurrency\nAmazon Keyspaces tables\n\n\nDisableScaleIn (boolean) --Indicates whether scale in by the target tracking scaling policy is disabled. If the value is true , scale in is disabled and the target tracking scaling policy won\'t remove capacity from the scalable target. Otherwise, scale in is enabled and the target tracking scaling policy can remove capacity from the scalable target. The default value is false .\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'PolicyARN': 'string',
    'Alarms': [
        {
            'AlarmName': 'string',
            'AlarmARN': 'string'
        },
    ]
}


Response Structure

(dict) --

PolicyARN (string) --
The Amazon Resource Name (ARN) of the resulting scaling policy.

Alarms (list) --
The CloudWatch alarms created for the target tracking scaling policy.

(dict) --
Represents a CloudWatch alarm associated with a scaling policy.

AlarmName (string) --
The name of the alarm.

AlarmARN (string) --
The Amazon Resource Name (ARN) of the alarm.











Exceptions

ApplicationAutoScaling.Client.exceptions.ValidationException
ApplicationAutoScaling.Client.exceptions.LimitExceededException
ApplicationAutoScaling.Client.exceptions.ObjectNotFoundException
ApplicationAutoScaling.Client.exceptions.ConcurrentUpdateException
ApplicationAutoScaling.Client.exceptions.FailedResourceAccessException
ApplicationAutoScaling.Client.exceptions.InternalServiceException

Examples
This example applies a scaling policy to an Amazon ECS service called web-app in the default cluster. The policy increases the desired count of the service by 200%, with a cool down period of 60 seconds.
response = client.put_scaling_policy(
    PolicyName='web-app-cpu-gt-75',
    PolicyType='StepScaling',
    ResourceId='service/default/web-app',
    ScalableDimension='ecs:service:DesiredCount',
    ServiceNamespace='ecs',
    StepScalingPolicyConfiguration={
        'AdjustmentType': 'PercentChangeInCapacity',
        'Cooldown': 60,
        'StepAdjustments': [
            {
                'MetricIntervalLowerBound': 0,
                'ScalingAdjustment': 200,
            },
        ],
    },
)

print(response)


Expected Output:
{
    'PolicyARN': 'arn:aws:autoscaling:us-west-2:012345678910:scalingPolicy:6d8972f3-efc8-437c-92d1-6270f29a66e7:resource/ecs/service/default/web-app:policyName/web-app-cpu-gt-75',
    'ResponseMetadata': {
        '...': '...',
    },
}


This example applies a scaling policy to an Amazon EC2 Spot fleet. The policy increases the target capacity of the spot fleet by 200%, with a cool down period of 180 seconds.",
response = client.put_scaling_policy(
    PolicyName='fleet-cpu-gt-75',
    PolicyType='StepScaling',
    ResourceId='spot-fleet-request/sfr-45e69d8a-be48-4539-bbf3-3464e99c50c3',
    ScalableDimension='ec2:spot-fleet-request:TargetCapacity',
    ServiceNamespace='ec2',
    StepScalingPolicyConfiguration={
        'AdjustmentType': 'PercentChangeInCapacity',
        'Cooldown': 180,
        'StepAdjustments': [
            {
                'MetricIntervalLowerBound': 0,
                'ScalingAdjustment': 200,
            },
        ],
    },
)

print(response)


Expected Output:
{
    'PolicyARN': 'arn:aws:autoscaling:us-east-1:012345678910:scalingPolicy:89406401-0cb7-4130-b770-d97cca0e446b:resource/ec2/spot-fleet-request/sfr-45e69d8a-be48-4539-bbf3-3464e99c50c3:policyName/fleet-cpu-gt-75',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'PolicyARN': 'string',
        'Alarms': [
            {
                'AlarmName': 'string',
                'AlarmARN': 'string'
            },
        ]
    }
    
    
    :returns: 
    ApplicationAutoScaling.Client.exceptions.ValidationException
    ApplicationAutoScaling.Client.exceptions.LimitExceededException
    ApplicationAutoScaling.Client.exceptions.ObjectNotFoundException
    ApplicationAutoScaling.Client.exceptions.ConcurrentUpdateException
    ApplicationAutoScaling.Client.exceptions.FailedResourceAccessException
    ApplicationAutoScaling.Client.exceptions.InternalServiceException
    
    """
    pass

def put_scheduled_action(ServiceNamespace=None, Schedule=None, ScheduledActionName=None, ResourceId=None, ScalableDimension=None, StartTime=None, EndTime=None, ScalableTargetAction=None):
    """
    Creates or updates a scheduled action for an Application Auto Scaling scalable target.
    Each scalable target is identified by a service namespace, resource ID, and scalable dimension. A scheduled action applies to the scalable target identified by those three attributes. You cannot create a scheduled action until you have registered the resource as a scalable target.
    When start and end times are specified with a recurring schedule using a cron expression or rates, they form the boundaries of when the recurring action starts and stops.
    To update a scheduled action, specify the parameters that you want to change. If you don\'t specify start and end times, the old values are deleted.
    For more information, see Scheduled Scaling in the Application Auto Scaling User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_scheduled_action(
        ServiceNamespace='ecs'|'elasticmapreduce'|'ec2'|'appstream'|'dynamodb'|'rds'|'sagemaker'|'custom-resource'|'comprehend'|'lambda'|'cassandra',
        Schedule='string',
        ScheduledActionName='string',
        ResourceId='string',
        ScalableDimension='ecs:service:DesiredCount'|'ec2:spot-fleet-request:TargetCapacity'|'elasticmapreduce:instancegroup:InstanceCount'|'appstream:fleet:DesiredCapacity'|'dynamodb:table:ReadCapacityUnits'|'dynamodb:table:WriteCapacityUnits'|'dynamodb:index:ReadCapacityUnits'|'dynamodb:index:WriteCapacityUnits'|'rds:cluster:ReadReplicaCount'|'sagemaker:variant:DesiredInstanceCount'|'custom-resource:ResourceType:Property'|'comprehend:document-classifier-endpoint:DesiredInferenceUnits'|'lambda:function:ProvisionedConcurrency'|'cassandra:table:ReadCapacityUnits'|'cassandra:table:WriteCapacityUnits',
        StartTime=datetime(2015, 1, 1),
        EndTime=datetime(2015, 1, 1),
        ScalableTargetAction={
            'MinCapacity': 123,
            'MaxCapacity': 123
        }
    )
    
    
    :type ServiceNamespace: string
    :param ServiceNamespace: [REQUIRED]\nThe namespace of the AWS service that provides the resource. For a resource provided by your own application or service, use custom-resource instead.\n

    :type Schedule: string
    :param Schedule: The schedule for this action. The following formats are supported:\n\nAt expressions - 'at(*yyyy* -*mm* -*dd* T*hh* :*mm* :*ss* ) '\nRate expressions - 'rate(*value*  *unit* ) '\nCron expressions - 'cron(*fields* ) '\n\nAt expressions are useful for one-time schedules. Specify the time in UTC.\nFor rate expressions, value is a positive integer and unit is minute | minutes | hour | hours | day | days .\nFor more information about cron expressions, see Cron Expressions in the Amazon CloudWatch Events User Guide .\nFor examples of using these expressions, see Scheduled Scaling in the Application Auto Scaling User Guide .\n

    :type ScheduledActionName: string
    :param ScheduledActionName: [REQUIRED]\nThe name of the scheduled action. This name must be unique among all other scheduled actions on the specified scalable target.\n

    :type ResourceId: string
    :param ResourceId: [REQUIRED]\nThe identifier of the resource associated with the scheduled action. This string consists of the resource type and unique identifier.\n\nECS service - The resource type is service and the unique identifier is the cluster name and service name. Example: service/default/sample-webapp .\nSpot Fleet request - The resource type is spot-fleet-request and the unique identifier is the Spot Fleet request ID. Example: spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE .\nEMR cluster - The resource type is instancegroup and the unique identifier is the cluster ID and instance group ID. Example: instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0 .\nAppStream 2.0 fleet - The resource type is fleet and the unique identifier is the fleet name. Example: fleet/sample-fleet .\nDynamoDB table - The resource type is table and the unique identifier is the table name. Example: table/my-table .\nDynamoDB global secondary index - The resource type is index and the unique identifier is the index name. Example: table/my-table/index/my-table-index .\nAurora DB cluster - The resource type is cluster and the unique identifier is the cluster name. Example: cluster:my-db-cluster .\nAmazon SageMaker endpoint variant - The resource type is variant and the unique identifier is the resource ID. Example: endpoint/my-end-point/variant/KMeansClustering .\nCustom resources are not supported with a resource type. This parameter must specify the OutputValue from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider. More information is available in our GitHub repository .\nAmazon Comprehend document classification endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE .\nLambda provisioned concurrency - The resource type is function and the unique identifier is the function name with a function version or alias name suffix that is not $LATEST . Example: function:my-function:prod or function:my-function:1 .\nAmazon Keyspaces table - The resource type is table and the unique identifier is the table name. Example: keyspace/mykeyspace/table/mytable .\n\n

    :type ScalableDimension: string
    :param ScalableDimension: [REQUIRED]\nThe scalable dimension. This string consists of the service namespace, resource type, and scaling property.\n\necs:service:DesiredCount - The desired task count of an ECS service.\nec2:spot-fleet-request:TargetCapacity - The target capacity of a Spot Fleet request.\nelasticmapreduce:instancegroup:InstanceCount - The instance count of an EMR Instance Group.\nappstream:fleet:DesiredCapacity - The desired capacity of an AppStream 2.0 fleet.\ndynamodb:table:ReadCapacityUnits - The provisioned read capacity for a DynamoDB table.\ndynamodb:table:WriteCapacityUnits - The provisioned write capacity for a DynamoDB table.\ndynamodb:index:ReadCapacityUnits - The provisioned read capacity for a DynamoDB global secondary index.\ndynamodb:index:WriteCapacityUnits - The provisioned write capacity for a DynamoDB global secondary index.\nrds:cluster:ReadReplicaCount - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition.\nsagemaker:variant:DesiredInstanceCount - The number of EC2 instances for an Amazon SageMaker model endpoint variant.\ncustom-resource:ResourceType:Property - The scalable dimension for a custom resource provided by your own application or service.\ncomprehend:document-classifier-endpoint:DesiredInferenceUnits - The number of inference units for an Amazon Comprehend document classification endpoint.\nlambda:function:ProvisionedConcurrency - The provisioned concurrency for a Lambda function.\ncassandra:table:ReadCapacityUnits - The provisioned read capacity for an Amazon Keyspaces table.\ncassandra:table:WriteCapacityUnits - The provisioned write capacity for an Amazon Keyspaces table.\n\n

    :type StartTime: datetime
    :param StartTime: The date and time for this scheduled action to start.

    :type EndTime: datetime
    :param EndTime: The date and time for the recurring schedule to end.

    :type ScalableTargetAction: dict
    :param ScalableTargetAction: The new minimum and maximum capacity. You can set both values or just one. At the scheduled time, if the current capacity is below the minimum capacity, Application Auto Scaling scales out to the minimum capacity. If the current capacity is above the maximum capacity, Application Auto Scaling scales in to the maximum capacity.\n\nMinCapacity (integer) --The minimum capacity.\nFor Lambda provisioned concurrency, the minimum value allowed is 0. For all other resources, the minimum value allowed is 1.\n\nMaxCapacity (integer) --The maximum capacity.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

ApplicationAutoScaling.Client.exceptions.ValidationException
ApplicationAutoScaling.Client.exceptions.LimitExceededException
ApplicationAutoScaling.Client.exceptions.ObjectNotFoundException
ApplicationAutoScaling.Client.exceptions.ConcurrentUpdateException
ApplicationAutoScaling.Client.exceptions.InternalServiceException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def register_scalable_target(ServiceNamespace=None, ResourceId=None, ScalableDimension=None, MinCapacity=None, MaxCapacity=None, RoleARN=None, SuspendedState=None):
    """
    Registers or updates a scalable target.
    A scalable target is a resource that Application Auto Scaling can scale out and scale in. Scalable targets are uniquely identified by the combination of resource ID, scalable dimension, and namespace.
    When you register a new scalable target, you must specify values for minimum and maximum capacity. Application Auto Scaling scaling policies will not scale capacity to values that are outside of this range.
    After you register a scalable target, you do not need to register it again to use other Application Auto Scaling operations. To see which resources have been registered, use DescribeScalableTargets . You can also view the scaling policies for a service namespace by using DescribeScalableTargets . If you no longer need a scalable target, you can deregister it by using DeregisterScalableTarget .
    To update a scalable target, specify the parameters that you want to change. Include the parameters that identify the scalable target: resource ID, scalable dimension, and namespace. Any parameters that you don\'t specify are not changed by this update request.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example registers a scalable target from an Amazon ECS service called web-app that is running on the default cluster, with a minimum desired count of 1 task and a maximum desired count of 10 tasks.
    Expected Output:
    This example registers a scalable target from an Amazon EC2 Spot fleet with a minimum target capacity of 1 and a maximum of 10.
    Expected Output:
    
    :example: response = client.register_scalable_target(
        ServiceNamespace='ecs'|'elasticmapreduce'|'ec2'|'appstream'|'dynamodb'|'rds'|'sagemaker'|'custom-resource'|'comprehend'|'lambda'|'cassandra',
        ResourceId='string',
        ScalableDimension='ecs:service:DesiredCount'|'ec2:spot-fleet-request:TargetCapacity'|'elasticmapreduce:instancegroup:InstanceCount'|'appstream:fleet:DesiredCapacity'|'dynamodb:table:ReadCapacityUnits'|'dynamodb:table:WriteCapacityUnits'|'dynamodb:index:ReadCapacityUnits'|'dynamodb:index:WriteCapacityUnits'|'rds:cluster:ReadReplicaCount'|'sagemaker:variant:DesiredInstanceCount'|'custom-resource:ResourceType:Property'|'comprehend:document-classifier-endpoint:DesiredInferenceUnits'|'lambda:function:ProvisionedConcurrency'|'cassandra:table:ReadCapacityUnits'|'cassandra:table:WriteCapacityUnits',
        MinCapacity=123,
        MaxCapacity=123,
        RoleARN='string',
        SuspendedState={
            'DynamicScalingInSuspended': True|False,
            'DynamicScalingOutSuspended': True|False,
            'ScheduledScalingSuspended': True|False
        }
    )
    
    
    :type ServiceNamespace: string
    :param ServiceNamespace: [REQUIRED]\nThe namespace of the AWS service that provides the resource. For a resource provided by your own application or service, use custom-resource instead.\n

    :type ResourceId: string
    :param ResourceId: [REQUIRED]\nThe identifier of the resource that is associated with the scalable target. This string consists of the resource type and unique identifier.\n\nECS service - The resource type is service and the unique identifier is the cluster name and service name. Example: service/default/sample-webapp .\nSpot Fleet request - The resource type is spot-fleet-request and the unique identifier is the Spot Fleet request ID. Example: spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE .\nEMR cluster - The resource type is instancegroup and the unique identifier is the cluster ID and instance group ID. Example: instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0 .\nAppStream 2.0 fleet - The resource type is fleet and the unique identifier is the fleet name. Example: fleet/sample-fleet .\nDynamoDB table - The resource type is table and the unique identifier is the table name. Example: table/my-table .\nDynamoDB global secondary index - The resource type is index and the unique identifier is the index name. Example: table/my-table/index/my-table-index .\nAurora DB cluster - The resource type is cluster and the unique identifier is the cluster name. Example: cluster:my-db-cluster .\nAmazon SageMaker endpoint variant - The resource type is variant and the unique identifier is the resource ID. Example: endpoint/my-end-point/variant/KMeansClustering .\nCustom resources are not supported with a resource type. This parameter must specify the OutputValue from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider. More information is available in our GitHub repository .\nAmazon Comprehend document classification endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE .\nLambda provisioned concurrency - The resource type is function and the unique identifier is the function name with a function version or alias name suffix that is not $LATEST . Example: function:my-function:prod or function:my-function:1 .\nAmazon Keyspaces table - The resource type is table and the unique identifier is the table name. Example: keyspace/mykeyspace/table/mytable .\n\n

    :type ScalableDimension: string
    :param ScalableDimension: [REQUIRED]\nThe scalable dimension associated with the scalable target. This string consists of the service namespace, resource type, and scaling property.\n\necs:service:DesiredCount - The desired task count of an ECS service.\nec2:spot-fleet-request:TargetCapacity - The target capacity of a Spot Fleet request.\nelasticmapreduce:instancegroup:InstanceCount - The instance count of an EMR Instance Group.\nappstream:fleet:DesiredCapacity - The desired capacity of an AppStream 2.0 fleet.\ndynamodb:table:ReadCapacityUnits - The provisioned read capacity for a DynamoDB table.\ndynamodb:table:WriteCapacityUnits - The provisioned write capacity for a DynamoDB table.\ndynamodb:index:ReadCapacityUnits - The provisioned read capacity for a DynamoDB global secondary index.\ndynamodb:index:WriteCapacityUnits - The provisioned write capacity for a DynamoDB global secondary index.\nrds:cluster:ReadReplicaCount - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition.\nsagemaker:variant:DesiredInstanceCount - The number of EC2 instances for an Amazon SageMaker model endpoint variant.\ncustom-resource:ResourceType:Property - The scalable dimension for a custom resource provided by your own application or service.\ncomprehend:document-classifier-endpoint:DesiredInferenceUnits - The number of inference units for an Amazon Comprehend document classification endpoint.\nlambda:function:ProvisionedConcurrency - The provisioned concurrency for a Lambda function.\ncassandra:table:ReadCapacityUnits - The provisioned read capacity for an Amazon Keyspaces table.\ncassandra:table:WriteCapacityUnits - The provisioned write capacity for an Amazon Keyspaces table.\n\n

    :type MinCapacity: integer
    :param MinCapacity: The minimum value that you plan to scale in to. When a scaling policy is in effect, Application Auto Scaling can scale in (contract) as needed to the minimum capacity limit in response to changing demand.\nThis parameter is required if you are registering a scalable target. For Lambda provisioned concurrency, the minimum value allowed is 0. For all other resources, the minimum value allowed is 1.\n

    :type MaxCapacity: integer
    :param MaxCapacity: The maximum value that you plan to scale out to. When a scaling policy is in effect, Application Auto Scaling can scale out (expand) as needed to the maximum capacity limit in response to changing demand.\nThis parameter is required if you are registering a scalable target.\n

    :type RoleARN: string
    :param RoleARN: This parameter is required for services that do not support service-linked roles (such as Amazon EMR), and it must specify the ARN of an IAM role that allows Application Auto Scaling to modify the scalable target on your behalf.\nIf the service supports service-linked roles, Application Auto Scaling uses a service-linked role, which it creates if it does not yet exist. For more information, see Application Auto Scaling IAM Roles .\n

    :type SuspendedState: dict
    :param SuspendedState: An embedded object that contains attributes and attribute values that are used to suspend and resume automatic scaling. Setting the value of an attribute to true suspends the specified scaling activities. Setting it to false (default) resumes the specified scaling activities.\n\nSuspension Outcomes\n\nFor DynamicScalingInSuspended , while a suspension is in effect, all scale-in activities that are triggered by a scaling policy are suspended.\nFor DynamicScalingOutSuspended , while a suspension is in effect, all scale-out activities that are triggered by a scaling policy are suspended.\nFor ScheduledScalingSuspended , while a suspension is in effect, all scaling activities that involve scheduled actions are suspended.\n\nFor more information, see Suspending and Resuming Scaling in the Application Auto Scaling User Guide .\n\nDynamicScalingInSuspended (boolean) --Whether scale in by a target tracking scaling policy or a step scaling policy is suspended. Set the value to true if you don\'t want Application Auto Scaling to remove capacity when a scaling policy is triggered. The default is false .\n\nDynamicScalingOutSuspended (boolean) --Whether scale out by a target tracking scaling policy or a step scaling policy is suspended. Set the value to true if you don\'t want Application Auto Scaling to add capacity when a scaling policy is triggered. The default is false .\n\nScheduledScalingSuspended (boolean) --Whether scheduled scaling is suspended. Set the value to true if you don\'t want Application Auto Scaling to add or remove capacity by initiating scheduled actions. The default is false .\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

ApplicationAutoScaling.Client.exceptions.ValidationException
ApplicationAutoScaling.Client.exceptions.LimitExceededException
ApplicationAutoScaling.Client.exceptions.ConcurrentUpdateException
ApplicationAutoScaling.Client.exceptions.InternalServiceException

Examples
This example registers a scalable target from an Amazon ECS service called web-app that is running on the default cluster, with a minimum desired count of 1 task and a maximum desired count of 10 tasks.
response = client.register_scalable_target(
    MaxCapacity=10,
    MinCapacity=1,
    ResourceId='service/default/web-app',
    RoleARN='arn:aws:iam::012345678910:role/ApplicationAutoscalingECSRole',
    ScalableDimension='ecs:service:DesiredCount',
    ServiceNamespace='ecs',
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}


This example registers a scalable target from an Amazon EC2 Spot fleet with a minimum target capacity of 1 and a maximum of 10.
response = client.register_scalable_target(
    MaxCapacity=10,
    MinCapacity=1,
    ResourceId='spot-fleet-request/sfr-45e69d8a-be48-4539-bbf3-3464e99c50c3',
    RoleARN='arn:aws:iam::012345678910:role/ApplicationAutoscalingSpotRole',
    ScalableDimension='ec2:spot-fleet-request:TargetCapacity',
    ServiceNamespace='ec2',
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

