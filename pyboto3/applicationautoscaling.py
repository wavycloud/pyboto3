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
    :param operation_name: The operation name. This is the same name
            as the method name on the client. For example, if the
            method name is create_foo, and you'd normally invoke the
            operation as client.create_foo(**kwargs), if the
            create_foo operation can be paginated, you can use the
            call client.get_paginator('create_foo').

    """
    pass

def delete_scaling_policy(PolicyName=None, ServiceNamespace=None, ResourceId=None, ScalableDimension=None):
    """
    Deletes the specified Application Auto Scaling scaling policy.
    Deleting a policy deletes the underlying alarm action, but does not delete the CloudWatch alarm associated with the scaling policy, even if it no longer has an associated action.
    To create a scaling policy or update an existing one, see  PutScalingPolicy .
    See also: AWS API Documentation
    
    Examples
    This example deletes a scaling policy for the Amazon ECS service called web-app, which is running in the default cluster.
    Expected Output:
    
    :example: response = client.delete_scaling_policy(
        PolicyName='string',
        ServiceNamespace='ecs'|'elasticmapreduce'|'ec2'|'appstream'|'dynamodb'|'rds'|'sagemaker',
        ResourceId='string',
        ScalableDimension='ecs:service:DesiredCount'|'ec2:spot-fleet-request:TargetCapacity'|'elasticmapreduce:instancegroup:InstanceCount'|'appstream:fleet:DesiredCapacity'|'dynamodb:table:ReadCapacityUnits'|'dynamodb:table:WriteCapacityUnits'|'dynamodb:index:ReadCapacityUnits'|'dynamodb:index:WriteCapacityUnits'|'rds:cluster:ReadReplicaCount'|'sagemaker:variant:DesiredInstanceCount'
    )
    
    
    :type PolicyName: string
    :param PolicyName: [REQUIRED]
            The name of the scaling policy.
            

    :type ServiceNamespace: string
    :param ServiceNamespace: [REQUIRED]
            The namespace of the AWS service. For more information, see AWS Service Namespaces in the Amazon Web Services General Reference .
            

    :type ResourceId: string
    :param ResourceId: [REQUIRED]
            The identifier of the resource associated with the scalable target. This string consists of the resource type and unique identifier.
            ECS service - The resource type is service and the unique identifier is the cluster name and service name. Example: service/default/sample-webapp .
            Spot fleet request - The resource type is spot-fleet-request and the unique identifier is the Spot fleet request ID. Example: spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE .
            EMR cluster - The resource type is instancegroup and the unique identifier is the cluster ID and instance group ID. Example: instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0 .
            AppStream 2.0 fleet - The resource type is fleet and the unique identifier is the fleet name. Example: fleet/sample-fleet .
            DynamoDB table - The resource type is table and the unique identifier is the resource ID. Example: table/my-table .
            DynamoDB global secondary index - The resource type is index and the unique identifier is the resource ID. Example: table/my-table/index/my-table-index .
            Aurora DB cluster - The resource type is cluster and the unique identifier is the cluster name. Example: cluster:my-db-cluster .
            Amazon SageMaker endpoint variants - The resource type is variant and the unique identifier is the resource ID. Example: endpoint/my-end-point/variant/KMeansClustering .
            

    :type ScalableDimension: string
    :param ScalableDimension: [REQUIRED]
            The scalable dimension. This string consists of the service namespace, resource type, and scaling property.
            ecs:service:DesiredCount - The desired task count of an ECS service.
            ec2:spot-fleet-request:TargetCapacity - The target capacity of a Spot fleet request.
            elasticmapreduce:instancegroup:InstanceCount - The instance count of an EMR Instance Group.
            appstream:fleet:DesiredCapacity - The desired capacity of an AppStream 2.0 fleet.
            dynamodb:table:ReadCapacityUnits - The provisioned read capacity for a DynamoDB table.
            dynamodb:table:WriteCapacityUnits - The provisioned write capacity for a DynamoDB table.
            dynamodb:index:ReadCapacityUnits - The provisioned read capacity for a DynamoDB global secondary index.
            dynamodb:index:WriteCapacityUnits - The provisioned write capacity for a DynamoDB global secondary index.
            rds:cluster:ReadReplicaCount - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition.
            sagemaker:variant:DesiredInstanceCount - The number of EC2 instances for an Amazon SageMaker model endpoint variant.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_scheduled_action(ServiceNamespace=None, ScheduledActionName=None, ResourceId=None, ScalableDimension=None):
    """
    Deletes the specified Application Auto Scaling scheduled action.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_scheduled_action(
        ServiceNamespace='ecs'|'elasticmapreduce'|'ec2'|'appstream'|'dynamodb'|'rds'|'sagemaker',
        ScheduledActionName='string',
        ResourceId='string',
        ScalableDimension='ecs:service:DesiredCount'|'ec2:spot-fleet-request:TargetCapacity'|'elasticmapreduce:instancegroup:InstanceCount'|'appstream:fleet:DesiredCapacity'|'dynamodb:table:ReadCapacityUnits'|'dynamodb:table:WriteCapacityUnits'|'dynamodb:index:ReadCapacityUnits'|'dynamodb:index:WriteCapacityUnits'|'rds:cluster:ReadReplicaCount'|'sagemaker:variant:DesiredInstanceCount'
    )
    
    
    :type ServiceNamespace: string
    :param ServiceNamespace: [REQUIRED]
            The namespace of the AWS service. For more information, see AWS Service Namespaces in the Amazon Web Services General Reference .
            

    :type ScheduledActionName: string
    :param ScheduledActionName: [REQUIRED]
            The name of the scheduled action.
            

    :type ResourceId: string
    :param ResourceId: [REQUIRED]
            The identifier of the resource associated with the scheduled action. This string consists of the resource type and unique identifier.
            ECS service - The resource type is service and the unique identifier is the cluster name and service name. Example: service/default/sample-webapp .
            Spot fleet request - The resource type is spot-fleet-request and the unique identifier is the Spot fleet request ID. Example: spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE .
            EMR cluster - The resource type is instancegroup and the unique identifier is the cluster ID and instance group ID. Example: instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0 .
            AppStream 2.0 fleet - The resource type is fleet and the unique identifier is the fleet name. Example: fleet/sample-fleet .
            DynamoDB table - The resource type is table and the unique identifier is the resource ID. Example: table/my-table .
            DynamoDB global secondary index - The resource type is index and the unique identifier is the resource ID. Example: table/my-table/index/my-table-index .
            Aurora DB cluster - The resource type is cluster and the unique identifier is the cluster name. Example: cluster:my-db-cluster .
            Amazon SageMaker endpoint variants - The resource type is variant and the unique identifier is the resource ID. Example: endpoint/my-end-point/variant/KMeansClustering .
            

    :type ScalableDimension: string
    :param ScalableDimension: The scalable dimension. This string consists of the service namespace, resource type, and scaling property.
            ecs:service:DesiredCount - The desired task count of an ECS service.
            ec2:spot-fleet-request:TargetCapacity - The target capacity of a Spot fleet request.
            elasticmapreduce:instancegroup:InstanceCount - The instance count of an EMR Instance Group.
            appstream:fleet:DesiredCapacity - The desired capacity of an AppStream 2.0 fleet.
            dynamodb:table:ReadCapacityUnits - The provisioned read capacity for a DynamoDB table.
            dynamodb:table:WriteCapacityUnits - The provisioned write capacity for a DynamoDB table.
            dynamodb:index:ReadCapacityUnits - The provisioned read capacity for a DynamoDB global secondary index.
            dynamodb:index:WriteCapacityUnits - The provisioned write capacity for a DynamoDB global secondary index.
            rds:cluster:ReadReplicaCount - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition.
            sagemaker:variant:DesiredInstanceCount - The number of EC2 instances for an Amazon SageMaker model endpoint variant.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def deregister_scalable_target(ServiceNamespace=None, ResourceId=None, ScalableDimension=None):
    """
    Deregisters a scalable target.
    Deregistering a scalable target deletes the scaling policies that are associated with it.
    To create a scalable target or update an existing one, see  RegisterScalableTarget .
    See also: AWS API Documentation
    
    Examples
    This example deregisters a scalable target for an Amazon ECS service called web-app that is running in the default cluster.
    Expected Output:
    
    :example: response = client.deregister_scalable_target(
        ServiceNamespace='ecs'|'elasticmapreduce'|'ec2'|'appstream'|'dynamodb'|'rds'|'sagemaker',
        ResourceId='string',
        ScalableDimension='ecs:service:DesiredCount'|'ec2:spot-fleet-request:TargetCapacity'|'elasticmapreduce:instancegroup:InstanceCount'|'appstream:fleet:DesiredCapacity'|'dynamodb:table:ReadCapacityUnits'|'dynamodb:table:WriteCapacityUnits'|'dynamodb:index:ReadCapacityUnits'|'dynamodb:index:WriteCapacityUnits'|'rds:cluster:ReadReplicaCount'|'sagemaker:variant:DesiredInstanceCount'
    )
    
    
    :type ServiceNamespace: string
    :param ServiceNamespace: [REQUIRED]
            The namespace of the AWS service. For more information, see AWS Service Namespaces in the Amazon Web Services General Reference .
            

    :type ResourceId: string
    :param ResourceId: [REQUIRED]
            The identifier of the resource associated with the scalable target. This string consists of the resource type and unique identifier.
            ECS service - The resource type is service and the unique identifier is the cluster name and service name. Example: service/default/sample-webapp .
            Spot fleet request - The resource type is spot-fleet-request and the unique identifier is the Spot fleet request ID. Example: spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE .
            EMR cluster - The resource type is instancegroup and the unique identifier is the cluster ID and instance group ID. Example: instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0 .
            AppStream 2.0 fleet - The resource type is fleet and the unique identifier is the fleet name. Example: fleet/sample-fleet .
            DynamoDB table - The resource type is table and the unique identifier is the resource ID. Example: table/my-table .
            DynamoDB global secondary index - The resource type is index and the unique identifier is the resource ID. Example: table/my-table/index/my-table-index .
            Aurora DB cluster - The resource type is cluster and the unique identifier is the cluster name. Example: cluster:my-db-cluster .
            Amazon SageMaker endpoint variants - The resource type is variant and the unique identifier is the resource ID. Example: endpoint/my-end-point/variant/KMeansClustering .
            

    :type ScalableDimension: string
    :param ScalableDimension: [REQUIRED]
            The scalable dimension associated with the scalable target. This string consists of the service namespace, resource type, and scaling property.
            ecs:service:DesiredCount - The desired task count of an ECS service.
            ec2:spot-fleet-request:TargetCapacity - The target capacity of a Spot fleet request.
            elasticmapreduce:instancegroup:InstanceCount - The instance count of an EMR Instance Group.
            appstream:fleet:DesiredCapacity - The desired capacity of an AppStream 2.0 fleet.
            dynamodb:table:ReadCapacityUnits - The provisioned read capacity for a DynamoDB table.
            dynamodb:table:WriteCapacityUnits - The provisioned write capacity for a DynamoDB table.
            dynamodb:index:ReadCapacityUnits - The provisioned read capacity for a DynamoDB global secondary index.
            dynamodb:index:WriteCapacityUnits - The provisioned write capacity for a DynamoDB global secondary index.
            rds:cluster:ReadReplicaCount - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition.
            sagemaker:variant:DesiredInstanceCount - The number of EC2 instances for an Amazon SageMaker model endpoint variant.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def describe_scalable_targets(ServiceNamespace=None, ResourceIds=None, ScalableDimension=None, MaxResults=None, NextToken=None):
    """
    Gets information about the scalable targets in the specified namespace.
    You can filter the results using the ResourceIds and ScalableDimension parameters.
    To create a scalable target or update an existing one, see  RegisterScalableTarget . If you are no longer using a scalable target, you can deregister it using  DeregisterScalableTarget .
    See also: AWS API Documentation
    
    Examples
    This example describes the scalable targets for the ecs service namespace.
    Expected Output:
    
    :example: response = client.describe_scalable_targets(
        ServiceNamespace='ecs'|'elasticmapreduce'|'ec2'|'appstream'|'dynamodb'|'rds'|'sagemaker',
        ResourceIds=[
            'string',
        ],
        ScalableDimension='ecs:service:DesiredCount'|'ec2:spot-fleet-request:TargetCapacity'|'elasticmapreduce:instancegroup:InstanceCount'|'appstream:fleet:DesiredCapacity'|'dynamodb:table:ReadCapacityUnits'|'dynamodb:table:WriteCapacityUnits'|'dynamodb:index:ReadCapacityUnits'|'dynamodb:index:WriteCapacityUnits'|'rds:cluster:ReadReplicaCount'|'sagemaker:variant:DesiredInstanceCount',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type ServiceNamespace: string
    :param ServiceNamespace: [REQUIRED]
            The namespace of the AWS service. For more information, see AWS Service Namespaces in the Amazon Web Services General Reference .
            

    :type ResourceIds: list
    :param ResourceIds: The identifier of the resource associated with the scalable target. This string consists of the resource type and unique identifier. If you specify a scalable dimension, you must also specify a resource ID.
            ECS service - The resource type is service and the unique identifier is the cluster name and service name. Example: service/default/sample-webapp .
            Spot fleet request - The resource type is spot-fleet-request and the unique identifier is the Spot fleet request ID. Example: spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE .
            EMR cluster - The resource type is instancegroup and the unique identifier is the cluster ID and instance group ID. Example: instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0 .
            AppStream 2.0 fleet - The resource type is fleet and the unique identifier is the fleet name. Example: fleet/sample-fleet .
            DynamoDB table - The resource type is table and the unique identifier is the resource ID. Example: table/my-table .
            DynamoDB global secondary index - The resource type is index and the unique identifier is the resource ID. Example: table/my-table/index/my-table-index .
            Aurora DB cluster - The resource type is cluster and the unique identifier is the cluster name. Example: cluster:my-db-cluster .
            Amazon SageMaker endpoint variants - The resource type is variant and the unique identifier is the resource ID. Example: endpoint/my-end-point/variant/KMeansClustering .
            (string) --
            

    :type ScalableDimension: string
    :param ScalableDimension: The scalable dimension associated with the scalable target. This string consists of the service namespace, resource type, and scaling property. If you specify a scalable dimension, you must also specify a resource ID.
            ecs:service:DesiredCount - The desired task count of an ECS service.
            ec2:spot-fleet-request:TargetCapacity - The target capacity of a Spot fleet request.
            elasticmapreduce:instancegroup:InstanceCount - The instance count of an EMR Instance Group.
            appstream:fleet:DesiredCapacity - The desired capacity of an AppStream 2.0 fleet.
            dynamodb:table:ReadCapacityUnits - The provisioned read capacity for a DynamoDB table.
            dynamodb:table:WriteCapacityUnits - The provisioned write capacity for a DynamoDB table.
            dynamodb:index:ReadCapacityUnits - The provisioned read capacity for a DynamoDB global secondary index.
            dynamodb:index:WriteCapacityUnits - The provisioned write capacity for a DynamoDB global secondary index.
            rds:cluster:ReadReplicaCount - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition.
            sagemaker:variant:DesiredInstanceCount - The number of EC2 instances for an Amazon SageMaker model endpoint variant.
            

    :type MaxResults: integer
    :param MaxResults: The maximum number of scalable targets. This value can be between 1 and 50. The default value is 50.
            If this parameter is used, the operation returns up to MaxResults results at a time, along with a NextToken value. To get the next set of results, include the NextToken value in a subsequent call. If this parameter is not used, the operation returns up to 50 results and a NextToken value, if applicable.
            

    :type NextToken: string
    :param NextToken: The token for the next set of results.

    :rtype: dict
    :return: {
        'ScalableTargets': [
            {
                'ServiceNamespace': 'ecs'|'elasticmapreduce'|'ec2'|'appstream'|'dynamodb'|'rds'|'sagemaker',
                'ResourceId': 'string',
                'ScalableDimension': 'ecs:service:DesiredCount'|'ec2:spot-fleet-request:TargetCapacity'|'elasticmapreduce:instancegroup:InstanceCount'|'appstream:fleet:DesiredCapacity'|'dynamodb:table:ReadCapacityUnits'|'dynamodb:table:WriteCapacityUnits'|'dynamodb:index:ReadCapacityUnits'|'dynamodb:index:WriteCapacityUnits'|'rds:cluster:ReadReplicaCount'|'sagemaker:variant:DesiredInstanceCount',
                'MinCapacity': 123,
                'MaxCapacity': 123,
                'RoleARN': 'string',
                'CreationTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    ECS service - The resource type is service and the unique identifier is the cluster name and service name. Example: service/default/sample-webapp .
    Spot fleet request - The resource type is spot-fleet-request and the unique identifier is the Spot fleet request ID. Example: spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE .
    EMR cluster - The resource type is instancegroup and the unique identifier is the cluster ID and instance group ID. Example: instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0 .
    AppStream 2.0 fleet - The resource type is fleet and the unique identifier is the fleet name. Example: fleet/sample-fleet .
    DynamoDB table - The resource type is table and the unique identifier is the resource ID. Example: table/my-table .
    DynamoDB global secondary index - The resource type is index and the unique identifier is the resource ID. Example: table/my-table/index/my-table-index .
    Aurora DB cluster - The resource type is cluster and the unique identifier is the cluster name. Example: cluster:my-db-cluster .
    Amazon SageMaker endpoint variants - The resource type is variant and the unique identifier is the resource ID. Example: endpoint/my-end-point/variant/KMeansClustering .
    
    """
    pass

def describe_scaling_activities(ServiceNamespace=None, ResourceId=None, ScalableDimension=None, MaxResults=None, NextToken=None):
    """
    Provides descriptive information about the scaling activities in the specified namespace from the previous six weeks.
    You can filter the results using the ResourceId and ScalableDimension parameters.
    Scaling activities are triggered by CloudWatch alarms that are associated with scaling policies. To view the scaling policies for a service namespace, see  DescribeScalingPolicies . To create a scaling policy or update an existing one, see  PutScalingPolicy .
    See also: AWS API Documentation
    
    Examples
    This example describes the scaling activities for an Amazon ECS service called web-app that is running in the default cluster.
    Expected Output:
    
    :example: response = client.describe_scaling_activities(
        ServiceNamespace='ecs'|'elasticmapreduce'|'ec2'|'appstream'|'dynamodb'|'rds'|'sagemaker',
        ResourceId='string',
        ScalableDimension='ecs:service:DesiredCount'|'ec2:spot-fleet-request:TargetCapacity'|'elasticmapreduce:instancegroup:InstanceCount'|'appstream:fleet:DesiredCapacity'|'dynamodb:table:ReadCapacityUnits'|'dynamodb:table:WriteCapacityUnits'|'dynamodb:index:ReadCapacityUnits'|'dynamodb:index:WriteCapacityUnits'|'rds:cluster:ReadReplicaCount'|'sagemaker:variant:DesiredInstanceCount',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type ServiceNamespace: string
    :param ServiceNamespace: [REQUIRED]
            The namespace of the AWS service. For more information, see AWS Service Namespaces in the Amazon Web Services General Reference .
            

    :type ResourceId: string
    :param ResourceId: The identifier of the resource associated with the scaling activity. This string consists of the resource type and unique identifier. If you specify a scalable dimension, you must also specify a resource ID.
            ECS service - The resource type is service and the unique identifier is the cluster name and service name. Example: service/default/sample-webapp .
            Spot fleet request - The resource type is spot-fleet-request and the unique identifier is the Spot fleet request ID. Example: spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE .
            EMR cluster - The resource type is instancegroup and the unique identifier is the cluster ID and instance group ID. Example: instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0 .
            AppStream 2.0 fleet - The resource type is fleet and the unique identifier is the fleet name. Example: fleet/sample-fleet .
            DynamoDB table - The resource type is table and the unique identifier is the resource ID. Example: table/my-table .
            DynamoDB global secondary index - The resource type is index and the unique identifier is the resource ID. Example: table/my-table/index/my-table-index .
            Aurora DB cluster - The resource type is cluster and the unique identifier is the cluster name. Example: cluster:my-db-cluster .
            Amazon SageMaker endpoint variants - The resource type is variant and the unique identifier is the resource ID. Example: endpoint/my-end-point/variant/KMeansClustering .
            

    :type ScalableDimension: string
    :param ScalableDimension: The scalable dimension. This string consists of the service namespace, resource type, and scaling property. If you specify a scalable dimension, you must also specify a resource ID.
            ecs:service:DesiredCount - The desired task count of an ECS service.
            ec2:spot-fleet-request:TargetCapacity - The target capacity of a Spot fleet request.
            elasticmapreduce:instancegroup:InstanceCount - The instance count of an EMR Instance Group.
            appstream:fleet:DesiredCapacity - The desired capacity of an AppStream 2.0 fleet.
            dynamodb:table:ReadCapacityUnits - The provisioned read capacity for a DynamoDB table.
            dynamodb:table:WriteCapacityUnits - The provisioned write capacity for a DynamoDB table.
            dynamodb:index:ReadCapacityUnits - The provisioned read capacity for a DynamoDB global secondary index.
            dynamodb:index:WriteCapacityUnits - The provisioned write capacity for a DynamoDB global secondary index.
            rds:cluster:ReadReplicaCount - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition.
            sagemaker:variant:DesiredInstanceCount - The number of EC2 instances for an Amazon SageMaker model endpoint variant.
            

    :type MaxResults: integer
    :param MaxResults: The maximum number of scalable targets. This value can be between 1 and 50. The default value is 50.
            If this parameter is used, the operation returns up to MaxResults results at a time, along with a NextToken value. To get the next set of results, include the NextToken value in a subsequent call. If this parameter is not used, the operation returns up to 50 results and a NextToken value, if applicable.
            

    :type NextToken: string
    :param NextToken: The token for the next set of results.

    :rtype: dict
    :return: {
        'ScalingActivities': [
            {
                'ActivityId': 'string',
                'ServiceNamespace': 'ecs'|'elasticmapreduce'|'ec2'|'appstream'|'dynamodb'|'rds'|'sagemaker',
                'ResourceId': 'string',
                'ScalableDimension': 'ecs:service:DesiredCount'|'ec2:spot-fleet-request:TargetCapacity'|'elasticmapreduce:instancegroup:InstanceCount'|'appstream:fleet:DesiredCapacity'|'dynamodb:table:ReadCapacityUnits'|'dynamodb:table:WriteCapacityUnits'|'dynamodb:index:ReadCapacityUnits'|'dynamodb:index:WriteCapacityUnits'|'rds:cluster:ReadReplicaCount'|'sagemaker:variant:DesiredInstanceCount',
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
    Spot fleet request - The resource type is spot-fleet-request and the unique identifier is the Spot fleet request ID. Example: spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE .
    EMR cluster - The resource type is instancegroup and the unique identifier is the cluster ID and instance group ID. Example: instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0 .
    AppStream 2.0 fleet - The resource type is fleet and the unique identifier is the fleet name. Example: fleet/sample-fleet .
    DynamoDB table - The resource type is table and the unique identifier is the resource ID. Example: table/my-table .
    DynamoDB global secondary index - The resource type is index and the unique identifier is the resource ID. Example: table/my-table/index/my-table-index .
    Aurora DB cluster - The resource type is cluster and the unique identifier is the cluster name. Example: cluster:my-db-cluster .
    Amazon SageMaker endpoint variants - The resource type is variant and the unique identifier is the resource ID. Example: endpoint/my-end-point/variant/KMeansClustering .
    
    """
    pass

def describe_scaling_policies(PolicyNames=None, ServiceNamespace=None, ResourceId=None, ScalableDimension=None, MaxResults=None, NextToken=None):
    """
    Describes the scaling policies for the specified service namespace.
    You can filter the results using the ResourceId , ScalableDimension , and PolicyNames parameters.
    To create a scaling policy or update an existing one, see  PutScalingPolicy . If you are no longer using a scaling policy, you can delete it using  DeleteScalingPolicy .
    See also: AWS API Documentation
    
    Examples
    This example describes the scaling policies for the ecs service namespace.
    Expected Output:
    
    :example: response = client.describe_scaling_policies(
        PolicyNames=[
            'string',
        ],
        ServiceNamespace='ecs'|'elasticmapreduce'|'ec2'|'appstream'|'dynamodb'|'rds'|'sagemaker',
        ResourceId='string',
        ScalableDimension='ecs:service:DesiredCount'|'ec2:spot-fleet-request:TargetCapacity'|'elasticmapreduce:instancegroup:InstanceCount'|'appstream:fleet:DesiredCapacity'|'dynamodb:table:ReadCapacityUnits'|'dynamodb:table:WriteCapacityUnits'|'dynamodb:index:ReadCapacityUnits'|'dynamodb:index:WriteCapacityUnits'|'rds:cluster:ReadReplicaCount'|'sagemaker:variant:DesiredInstanceCount',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type PolicyNames: list
    :param PolicyNames: The names of the scaling policies to describe.
            (string) --
            

    :type ServiceNamespace: string
    :param ServiceNamespace: [REQUIRED]
            The namespace of the AWS service. For more information, see AWS Service Namespaces in the Amazon Web Services General Reference .
            

    :type ResourceId: string
    :param ResourceId: The identifier of the resource associated with the scaling policy. This string consists of the resource type and unique identifier. If you specify a scalable dimension, you must also specify a resource ID.
            ECS service - The resource type is service and the unique identifier is the cluster name and service name. Example: service/default/sample-webapp .
            Spot fleet request - The resource type is spot-fleet-request and the unique identifier is the Spot fleet request ID. Example: spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE .
            EMR cluster - The resource type is instancegroup and the unique identifier is the cluster ID and instance group ID. Example: instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0 .
            AppStream 2.0 fleet - The resource type is fleet and the unique identifier is the fleet name. Example: fleet/sample-fleet .
            DynamoDB table - The resource type is table and the unique identifier is the resource ID. Example: table/my-table .
            DynamoDB global secondary index - The resource type is index and the unique identifier is the resource ID. Example: table/my-table/index/my-table-index .
            Aurora DB cluster - The resource type is cluster and the unique identifier is the cluster name. Example: cluster:my-db-cluster .
            Amazon SageMaker endpoint variants - The resource type is variant and the unique identifier is the resource ID. Example: endpoint/my-end-point/variant/KMeansClustering .
            

    :type ScalableDimension: string
    :param ScalableDimension: The scalable dimension. This string consists of the service namespace, resource type, and scaling property. If you specify a scalable dimension, you must also specify a resource ID.
            ecs:service:DesiredCount - The desired task count of an ECS service.
            ec2:spot-fleet-request:TargetCapacity - The target capacity of a Spot fleet request.
            elasticmapreduce:instancegroup:InstanceCount - The instance count of an EMR Instance Group.
            appstream:fleet:DesiredCapacity - The desired capacity of an AppStream 2.0 fleet.
            dynamodb:table:ReadCapacityUnits - The provisioned read capacity for a DynamoDB table.
            dynamodb:table:WriteCapacityUnits - The provisioned write capacity for a DynamoDB table.
            dynamodb:index:ReadCapacityUnits - The provisioned read capacity for a DynamoDB global secondary index.
            dynamodb:index:WriteCapacityUnits - The provisioned write capacity for a DynamoDB global secondary index.
            rds:cluster:ReadReplicaCount - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition.
            sagemaker:variant:DesiredInstanceCount - The number of EC2 instances for an Amazon SageMaker model endpoint variant.
            

    :type MaxResults: integer
    :param MaxResults: The maximum number of scalable targets. This value can be between 1 and 50. The default value is 50.
            If this parameter is used, the operation returns up to MaxResults results at a time, along with a NextToken value. To get the next set of results, include the NextToken value in a subsequent call. If this parameter is not used, the operation returns up to 50 results and a NextToken value, if applicable.
            

    :type NextToken: string
    :param NextToken: The token for the next set of results.

    :rtype: dict
    :return: {
        'ScalingPolicies': [
            {
                'PolicyARN': 'string',
                'PolicyName': 'string',
                'ServiceNamespace': 'ecs'|'elasticmapreduce'|'ec2'|'appstream'|'dynamodb'|'rds'|'sagemaker',
                'ResourceId': 'string',
                'ScalableDimension': 'ecs:service:DesiredCount'|'ec2:spot-fleet-request:TargetCapacity'|'elasticmapreduce:instancegroup:InstanceCount'|'appstream:fleet:DesiredCapacity'|'dynamodb:table:ReadCapacityUnits'|'dynamodb:table:WriteCapacityUnits'|'dynamodb:index:ReadCapacityUnits'|'dynamodb:index:WriteCapacityUnits'|'rds:cluster:ReadReplicaCount'|'sagemaker:variant:DesiredInstanceCount',
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
                        'PredefinedMetricType': 'DynamoDBReadCapacityUtilization'|'DynamoDBWriteCapacityUtilization'|'ALBRequestCountPerTarget'|'RDSReaderAverageCPUUtilization'|'RDSReaderAverageDatabaseConnections'|'EC2SpotFleetRequestAverageCPUUtilization'|'EC2SpotFleetRequestAverageNetworkIn'|'EC2SpotFleetRequestAverageNetworkOut'|'SageMakerVariantInvocationsPerInstance'|'ECSServiceAverageCPUUtilization'|'ECSServiceAverageMemoryUtilization',
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
    Spot fleet request - The resource type is spot-fleet-request and the unique identifier is the Spot fleet request ID. Example: spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE .
    EMR cluster - The resource type is instancegroup and the unique identifier is the cluster ID and instance group ID. Example: instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0 .
    AppStream 2.0 fleet - The resource type is fleet and the unique identifier is the fleet name. Example: fleet/sample-fleet .
    DynamoDB table - The resource type is table and the unique identifier is the resource ID. Example: table/my-table .
    DynamoDB global secondary index - The resource type is index and the unique identifier is the resource ID. Example: table/my-table/index/my-table-index .
    Aurora DB cluster - The resource type is cluster and the unique identifier is the cluster name. Example: cluster:my-db-cluster .
    Amazon SageMaker endpoint variants - The resource type is variant and the unique identifier is the resource ID. Example: endpoint/my-end-point/variant/KMeansClustering .
    
    """
    pass

def describe_scheduled_actions(ScheduledActionNames=None, ServiceNamespace=None, ResourceId=None, ScalableDimension=None, MaxResults=None, NextToken=None):
    """
    Describes the scheduled actions for the specified service namespace.
    You can filter the results using the ResourceId , ScalableDimension , and ScheduledActionNames parameters.
    To create a scheduled action or update an existing one, see  PutScheduledAction . If you are no longer using a scheduled action, you can delete it using  DeleteScheduledAction .
    See also: AWS API Documentation
    
    
    :example: response = client.describe_scheduled_actions(
        ScheduledActionNames=[
            'string',
        ],
        ServiceNamespace='ecs'|'elasticmapreduce'|'ec2'|'appstream'|'dynamodb'|'rds'|'sagemaker',
        ResourceId='string',
        ScalableDimension='ecs:service:DesiredCount'|'ec2:spot-fleet-request:TargetCapacity'|'elasticmapreduce:instancegroup:InstanceCount'|'appstream:fleet:DesiredCapacity'|'dynamodb:table:ReadCapacityUnits'|'dynamodb:table:WriteCapacityUnits'|'dynamodb:index:ReadCapacityUnits'|'dynamodb:index:WriteCapacityUnits'|'rds:cluster:ReadReplicaCount'|'sagemaker:variant:DesiredInstanceCount',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type ScheduledActionNames: list
    :param ScheduledActionNames: The names of the scheduled actions to describe.
            (string) --
            

    :type ServiceNamespace: string
    :param ServiceNamespace: [REQUIRED]
            The namespace of the AWS service. For more information, see AWS Service Namespaces in the Amazon Web Services General Reference .
            

    :type ResourceId: string
    :param ResourceId: The identifier of the resource associated with the scheduled action. This string consists of the resource type and unique identifier. If you specify a scalable dimension, you must also specify a resource ID.
            ECS service - The resource type is service and the unique identifier is the cluster name and service name. Example: service/default/sample-webapp .
            Spot fleet request - The resource type is spot-fleet-request and the unique identifier is the Spot fleet request ID. Example: spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE .
            EMR cluster - The resource type is instancegroup and the unique identifier is the cluster ID and instance group ID. Example: instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0 .
            AppStream 2.0 fleet - The resource type is fleet and the unique identifier is the fleet name. Example: fleet/sample-fleet .
            DynamoDB table - The resource type is table and the unique identifier is the resource ID. Example: table/my-table .
            DynamoDB global secondary index - The resource type is index and the unique identifier is the resource ID. Example: table/my-table/index/my-table-index .
            Aurora DB cluster - The resource type is cluster and the unique identifier is the cluster name. Example: cluster:my-db-cluster .
            Amazon SageMaker endpoint variants - The resource type is variant and the unique identifier is the resource ID. Example: endpoint/my-end-point/variant/KMeansClustering .
            

    :type ScalableDimension: string
    :param ScalableDimension: The scalable dimension. This string consists of the service namespace, resource type, and scaling property. If you specify a scalable dimension, you must also specify a resource ID.
            ecs:service:DesiredCount - The desired task count of an ECS service.
            ec2:spot-fleet-request:TargetCapacity - The target capacity of a Spot fleet request.
            elasticmapreduce:instancegroup:InstanceCount - The instance count of an EMR Instance Group.
            appstream:fleet:DesiredCapacity - The desired capacity of an AppStream 2.0 fleet.
            dynamodb:table:ReadCapacityUnits - The provisioned read capacity for a DynamoDB table.
            dynamodb:table:WriteCapacityUnits - The provisioned write capacity for a DynamoDB table.
            dynamodb:index:ReadCapacityUnits - The provisioned read capacity for a DynamoDB global secondary index.
            dynamodb:index:WriteCapacityUnits - The provisioned write capacity for a DynamoDB global secondary index.
            rds:cluster:ReadReplicaCount - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition.
            sagemaker:variant:DesiredInstanceCount - The number of EC2 instances for an Amazon SageMaker model endpoint variant.
            

    :type MaxResults: integer
    :param MaxResults: The maximum number of scheduled action results. This value can be between 1 and 50. The default value is 50.
            If this parameter is used, the operation returns up to MaxResults results at a time, along with a NextToken value. To get the next set of results, include the NextToken value in a subsequent call. If this parameter is not used, the operation returns up to 50 results and a NextToken value, if applicable.
            

    :type NextToken: string
    :param NextToken: The token for the next set of results.

    :rtype: dict
    :return: {
        'ScheduledActions': [
            {
                'ScheduledActionName': 'string',
                'ScheduledActionARN': 'string',
                'ServiceNamespace': 'ecs'|'elasticmapreduce'|'ec2'|'appstream'|'dynamodb'|'rds'|'sagemaker',
                'Schedule': 'string',
                'ResourceId': 'string',
                'ScalableDimension': 'ecs:service:DesiredCount'|'ec2:spot-fleet-request:TargetCapacity'|'elasticmapreduce:instancegroup:InstanceCount'|'appstream:fleet:DesiredCapacity'|'dynamodb:table:ReadCapacityUnits'|'dynamodb:table:WriteCapacityUnits'|'dynamodb:index:ReadCapacityUnits'|'dynamodb:index:WriteCapacityUnits'|'rds:cluster:ReadReplicaCount'|'sagemaker:variant:DesiredInstanceCount',
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
    At expressions - at(*yyyy* -*mm* -*dd* T*hh* :*mm* :*ss* )
    Rate expressions - rate(*value* *unit* )
    Cron expressions - cron(*fields* )
    
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

def get_waiter(waiter_name=None):
    """
    
    :type waiter_name: 
    :param waiter_name: 

    """
    pass

def put_scaling_policy(PolicyName=None, ServiceNamespace=None, ResourceId=None, ScalableDimension=None, PolicyType=None, StepScalingPolicyConfiguration=None, TargetTrackingScalingPolicyConfiguration=None):
    """
    Creates or updates a policy for an Application Auto Scaling scalable target.
    Each scalable target is identified by a service namespace, resource ID, and scalable dimension. A scaling policy applies to the scalable target identified by those three attributes. You cannot create a scaling policy until you register the scalable target using  RegisterScalableTarget .
    To update a policy, specify its policy name and the parameters that you want to change. Any parameters that you don't specify are not changed by this update request.
    You can view the scaling policies for a service namespace using  DescribeScalingPolicies . If you are no longer using a scaling policy, you can delete it using  DeleteScalingPolicy .
    See also: AWS API Documentation
    
    Examples
    This example applies a scaling policy to an Amazon ECS service called web-app in the default cluster. The policy increases the desired count of the service by 200%, with a cool down period of 60 seconds.
    Expected Output:
    This example applies a scaling policy to an Amazon EC2 Spot fleet. The policy increases the target capacity of the spot fleet by 200%, with a cool down period of 180 seconds.",
    Expected Output:
    
    :example: response = client.put_scaling_policy(
        PolicyName='string',
        ServiceNamespace='ecs'|'elasticmapreduce'|'ec2'|'appstream'|'dynamodb'|'rds'|'sagemaker',
        ResourceId='string',
        ScalableDimension='ecs:service:DesiredCount'|'ec2:spot-fleet-request:TargetCapacity'|'elasticmapreduce:instancegroup:InstanceCount'|'appstream:fleet:DesiredCapacity'|'dynamodb:table:ReadCapacityUnits'|'dynamodb:table:WriteCapacityUnits'|'dynamodb:index:ReadCapacityUnits'|'dynamodb:index:WriteCapacityUnits'|'rds:cluster:ReadReplicaCount'|'sagemaker:variant:DesiredInstanceCount',
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
                'PredefinedMetricType': 'DynamoDBReadCapacityUtilization'|'DynamoDBWriteCapacityUtilization'|'ALBRequestCountPerTarget'|'RDSReaderAverageCPUUtilization'|'RDSReaderAverageDatabaseConnections'|'EC2SpotFleetRequestAverageCPUUtilization'|'EC2SpotFleetRequestAverageNetworkIn'|'EC2SpotFleetRequestAverageNetworkOut'|'SageMakerVariantInvocationsPerInstance'|'ECSServiceAverageCPUUtilization'|'ECSServiceAverageMemoryUtilization',
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
    :param PolicyName: [REQUIRED]
            The name of the scaling policy.
            

    :type ServiceNamespace: string
    :param ServiceNamespace: [REQUIRED]
            The namespace of the AWS service. For more information, see AWS Service Namespaces in the Amazon Web Services General Reference .
            

    :type ResourceId: string
    :param ResourceId: [REQUIRED]
            The identifier of the resource associated with the scaling policy. This string consists of the resource type and unique identifier.
            ECS service - The resource type is service and the unique identifier is the cluster name and service name. Example: service/default/sample-webapp .
            Spot fleet request - The resource type is spot-fleet-request and the unique identifier is the Spot fleet request ID. Example: spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE .
            EMR cluster - The resource type is instancegroup and the unique identifier is the cluster ID and instance group ID. Example: instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0 .
            AppStream 2.0 fleet - The resource type is fleet and the unique identifier is the fleet name. Example: fleet/sample-fleet .
            DynamoDB table - The resource type is table and the unique identifier is the resource ID. Example: table/my-table .
            DynamoDB global secondary index - The resource type is index and the unique identifier is the resource ID. Example: table/my-table/index/my-table-index .
            Aurora DB cluster - The resource type is cluster and the unique identifier is the cluster name. Example: cluster:my-db-cluster .
            Amazon SageMaker endpoint variants - The resource type is variant and the unique identifier is the resource ID. Example: endpoint/my-end-point/variant/KMeansClustering .
            

    :type ScalableDimension: string
    :param ScalableDimension: [REQUIRED]
            The scalable dimension. This string consists of the service namespace, resource type, and scaling property.
            ecs:service:DesiredCount - The desired task count of an ECS service.
            ec2:spot-fleet-request:TargetCapacity - The target capacity of a Spot fleet request.
            elasticmapreduce:instancegroup:InstanceCount - The instance count of an EMR Instance Group.
            appstream:fleet:DesiredCapacity - The desired capacity of an AppStream 2.0 fleet.
            dynamodb:table:ReadCapacityUnits - The provisioned read capacity for a DynamoDB table.
            dynamodb:table:WriteCapacityUnits - The provisioned write capacity for a DynamoDB table.
            dynamodb:index:ReadCapacityUnits - The provisioned read capacity for a DynamoDB global secondary index.
            dynamodb:index:WriteCapacityUnits - The provisioned write capacity for a DynamoDB global secondary index.
            rds:cluster:ReadReplicaCount - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition.
            sagemaker:variant:DesiredInstanceCount - The number of EC2 instances for an Amazon SageMaker model endpoint variant.
            

    :type PolicyType: string
    :param PolicyType: The policy type. This parameter is required if you are creating a policy.
            For DynamoDB, only TargetTrackingScaling is supported. For Amazon ECS, Spot Fleet, and Amazon RDS, both StepScaling and TargetTrackingScaling are supported. For any other service, only StepScaling is supported.
            

    :type StepScalingPolicyConfiguration: dict
    :param StepScalingPolicyConfiguration: A step scaling policy.
            This parameter is required if you are creating a policy and the policy type is StepScaling .
            AdjustmentType (string) --The adjustment type, which specifies how the ScalingAdjustment parameter in a StepAdjustment is interpreted.
            StepAdjustments (list) --A set of adjustments that enable you to scale based on the size of the alarm breach.
            (dict) --Represents a step adjustment for a StepScalingPolicyConfiguration . Describes an adjustment based on the difference between the value of the aggregated CloudWatch metric and the breach threshold that you've defined for the alarm.
            For the following examples, suppose that you have an alarm with a breach threshold of 50:
            To trigger the adjustment when the metric is greater than or equal to 50 and less than 60, specify a lower bound of 0 and an upper bound of 10.
            To trigger the adjustment when the metric is greater than 40 and less than or equal to 50, specify a lower bound of -10 and an upper bound of 0.
            There are a few rules for the step adjustments for your step policy:
            The ranges of your step adjustments can't overlap or have a gap.
            At most one step adjustment can have a null lower bound. If one step adjustment has a negative lower bound, then there must be a step adjustment with a null lower bound.
            At most one step adjustment can have a null upper bound. If one step adjustment has a positive upper bound, then there must be a step adjustment with a null upper bound.
            The upper and lower bound can't be null in the same step adjustment.
            MetricIntervalLowerBound (float) --The lower bound for the difference between the alarm threshold and the CloudWatch metric. If the metric value is above the breach threshold, the lower bound is inclusive (the metric must be greater than or equal to the threshold plus the lower bound). Otherwise, it is exclusive (the metric must be greater than the threshold plus the lower bound). A null value indicates negative infinity.
            MetricIntervalUpperBound (float) --The upper bound for the difference between the alarm threshold and the CloudWatch metric. If the metric value is above the breach threshold, the upper bound is exclusive (the metric must be less than the threshold plus the upper bound). Otherwise, it is inclusive (the metric must be less than or equal to the threshold plus the upper bound). A null value indicates positive infinity.
            The upper bound must be greater than the lower bound.
            ScalingAdjustment (integer) -- [REQUIRED]The amount by which to scale, based on the specified adjustment type. A positive value adds to the current scalable dimension while a negative number removes from the current scalable dimension.
            
            MinAdjustmentMagnitude (integer) --The minimum number to adjust your scalable dimension as a result of a scaling activity. If the adjustment type is PercentChangeInCapacity , the scaling policy changes the scalable dimension of the scalable target by this amount.
            Cooldown (integer) --The amount of time, in seconds, after a scaling activity completes where previous trigger-related scaling activities can influence future scaling events.
            For scale out policies, while the cooldown period is in effect, the capacity that has been added by the previous scale out event that initiated the cooldown is calculated as part of the desired capacity for the next scale out. The intention is to continuously (but not excessively) scale out. For example, an alarm triggers a step scaling policy to scale out an Amazon ECS service by 2 tasks, the scaling activity completes successfully, and a cooldown period of 5 minutes starts. During the Cooldown period, if the alarm triggers the same policy again but at a more aggressive step adjustment to scale out the service by 3 tasks, the 2 tasks that were added in the previous scale out event are considered part of that capacity and only 1 additional task is added to the desired count.
            For scale in policies, the cooldown period is used to block subsequent scale in requests until it has expired. The intention is to scale in conservatively to protect your application's availability. However, if another alarm triggers a scale out policy during the cooldown period after a scale-in, Application Auto Scaling scales out your scalable target immediately.
            MetricAggregationType (string) --The aggregation type for the CloudWatch metrics. Valid values are Minimum , Maximum , and Average .
            

    :type TargetTrackingScalingPolicyConfiguration: dict
    :param TargetTrackingScalingPolicyConfiguration: A target tracking policy.
            This parameter is required if you are creating a policy and the policy type is TargetTrackingScaling .
            TargetValue (float) -- [REQUIRED]The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2).
            PredefinedMetricSpecification (dict) --A predefined metric.
            PredefinedMetricType (string) -- [REQUIRED]The metric type. The ALBRequestCountPerTarget metric type applies only to Spot fleet requests and ECS services.
            ResourceLabel (string) --Identifies the resource associated with the metric type. You can't specify a resource label unless the metric type is ALBRequestCountPerTarget and there is a target group attached to the Spot fleet request or ECS service.
            The format is app/load-balancer-name/load-balancer-id/targetgroup/target-group-name/target-group-id, where:
            app/load-balancer-name/load-balancer-idis the final portion of the load balancer ARN
            targetgroup/target-group-name/target-group-idis the final portion of the target group ARN.
            
            CustomizedMetricSpecification (dict) --A customized metric.
            MetricName (string) -- [REQUIRED]The name of the metric.
            Namespace (string) -- [REQUIRED]The namespace of the metric.
            Dimensions (list) --The dimensions of the metric.
            (dict) --Describes the dimension of a metric.
            Name (string) -- [REQUIRED]The name of the dimension.
            Value (string) -- [REQUIRED]The value of the dimension.
            
            Statistic (string) -- [REQUIRED]The statistic of the metric.
            Unit (string) --The unit of the metric.
            ScaleOutCooldown (integer) --The amount of time, in seconds, after a scale out activity completes before another scale out activity can start.
            While the cooldown period is in effect, the capacity that has been added by the previous scale out event that initiated the cooldown is calculated as part of the desired capacity for the next scale out. The intention is to continuously (but not excessively) scale out.
            ScaleInCooldown (integer) --The amount of time, in seconds, after a scale in activity completes before another scale in activity can start.
            The cooldown period is used to block subsequent scale in requests until it has expired. The intention is to scale in conservatively to protect your application's availability. However, if another alarm triggers a scale out policy during the cooldown period after a scale-in, Application Auto Scaling scales out your scalable target immediately.
            DisableScaleIn (boolean) --Indicates whether scale in by the target tracking policy is disabled. If the value is true , scale in is disabled and the target tracking policy won't remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. The default value is false .
            

    :rtype: dict
    :return: {
        'PolicyARN': 'string',
        'Alarms': [
            {
                'AlarmName': 'string',
                'AlarmARN': 'string'
            },
        ]
    }
    
    
    """
    pass

def put_scheduled_action(ServiceNamespace=None, Schedule=None, ScheduledActionName=None, ResourceId=None, ScalableDimension=None, StartTime=None, EndTime=None, ScalableTargetAction=None):
    """
    Creates or updates a scheduled action for an Application Auto Scaling scalable target.
    Each scalable target is identified by a service namespace, resource ID, and scalable dimension. A scheduled action applies to the scalable target identified by those three attributes. You cannot create a scheduled action until you register the scalable target using  RegisterScalableTarget .
    To update an action, specify its name and the parameters that you want to change. If you don't specify start and end times, the old values are deleted. Any other parameters that you don't specify are not changed by this update request.
    You can view the scheduled actions using  DescribeScheduledActions . If you are no longer using a scheduled action, you can delete it using  DeleteScheduledAction .
    See also: AWS API Documentation
    
    
    :example: response = client.put_scheduled_action(
        ServiceNamespace='ecs'|'elasticmapreduce'|'ec2'|'appstream'|'dynamodb'|'rds'|'sagemaker',
        Schedule='string',
        ScheduledActionName='string',
        ResourceId='string',
        ScalableDimension='ecs:service:DesiredCount'|'ec2:spot-fleet-request:TargetCapacity'|'elasticmapreduce:instancegroup:InstanceCount'|'appstream:fleet:DesiredCapacity'|'dynamodb:table:ReadCapacityUnits'|'dynamodb:table:WriteCapacityUnits'|'dynamodb:index:ReadCapacityUnits'|'dynamodb:index:WriteCapacityUnits'|'rds:cluster:ReadReplicaCount'|'sagemaker:variant:DesiredInstanceCount',
        StartTime=datetime(2015, 1, 1),
        EndTime=datetime(2015, 1, 1),
        ScalableTargetAction={
            'MinCapacity': 123,
            'MaxCapacity': 123
        }
    )
    
    
    :type ServiceNamespace: string
    :param ServiceNamespace: [REQUIRED]
            The namespace of the AWS service. For more information, see AWS Service Namespaces in the Amazon Web Services General Reference .
            

    :type Schedule: string
    :param Schedule: The schedule for this action. The following formats are supported:
            At expressions - at(*yyyy* -*mm* -*dd* T*hh* :*mm* :*ss* )
            Rate expressions - rate(*value*  *unit* )
            Cron expressions - cron(*fields* )
            At expressions are useful for one-time schedules. Specify the time, in UTC.
            For rate expressions, value is a positive integer and unit is minute | minutes | hour | hours | day | days .
            For more information about cron expressions, see Cron .
            

    :type ScheduledActionName: string
    :param ScheduledActionName: [REQUIRED]
            The name of the scheduled action.
            

    :type ResourceId: string
    :param ResourceId: [REQUIRED]
            The identifier of the resource associated with the scheduled action. This string consists of the resource type and unique identifier.
            ECS service - The resource type is service and the unique identifier is the cluster name and service name. Example: service/default/sample-webapp .
            Spot fleet request - The resource type is spot-fleet-request and the unique identifier is the Spot fleet request ID. Example: spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE .
            EMR cluster - The resource type is instancegroup and the unique identifier is the cluster ID and instance group ID. Example: instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0 .
            AppStream 2.0 fleet - The resource type is fleet and the unique identifier is the fleet name. Example: fleet/sample-fleet .
            DynamoDB table - The resource type is table and the unique identifier is the resource ID. Example: table/my-table .
            DynamoDB global secondary index - The resource type is index and the unique identifier is the resource ID. Example: table/my-table/index/my-table-index .
            Aurora DB cluster - The resource type is cluster and the unique identifier is the cluster name. Example: cluster:my-db-cluster .
            Amazon SageMaker endpoint variants - The resource type is variant and the unique identifier is the resource ID. Example: endpoint/my-end-point/variant/KMeansClustering .
            

    :type ScalableDimension: string
    :param ScalableDimension: The scalable dimension. This parameter is required if you are creating a scheduled action. This string consists of the service namespace, resource type, and scaling property.
            ecs:service:DesiredCount - The desired task count of an ECS service.
            ec2:spot-fleet-request:TargetCapacity - The target capacity of a Spot fleet request.
            elasticmapreduce:instancegroup:InstanceCount - The instance count of an EMR Instance Group.
            appstream:fleet:DesiredCapacity - The desired capacity of an AppStream 2.0 fleet.
            dynamodb:table:ReadCapacityUnits - The provisioned read capacity for a DynamoDB table.
            dynamodb:table:WriteCapacityUnits - The provisioned write capacity for a DynamoDB table.
            dynamodb:index:ReadCapacityUnits - The provisioned read capacity for a DynamoDB global secondary index.
            dynamodb:index:WriteCapacityUnits - The provisioned write capacity for a DynamoDB global secondary index.
            rds:cluster:ReadReplicaCount - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition.
            sagemaker:variant:DesiredInstanceCount - The number of EC2 instances for an Amazon SageMaker model endpoint variant.
            

    :type StartTime: datetime
    :param StartTime: The date and time for the scheduled action to start.

    :type EndTime: datetime
    :param EndTime: The date and time for the scheduled action to end.

    :type ScalableTargetAction: dict
    :param ScalableTargetAction: The new minimum and maximum capacity. You can set both values or just one. During the scheduled time, if the current capacity is below the minimum capacity, Application Auto Scaling scales out to the minimum capacity. If the current capacity is above the maximum capacity, Application Auto Scaling scales in to the maximum capacity.
            MinCapacity (integer) --The minimum capacity.
            MaxCapacity (integer) --The maximum capacity.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def register_scalable_target(ServiceNamespace=None, ResourceId=None, ScalableDimension=None, MinCapacity=None, MaxCapacity=None, RoleARN=None):
    """
    Registers or updates a scalable target. A scalable target is a resource that Application Auto Scaling can scale out or scale in. After you have registered a scalable target, you can use this operation to update the minimum and maximum values for its scalable dimension.
    After you register a scalable target, you can create and apply scaling policies using  PutScalingPolicy . You can view the scaling policies for a service namespace using  DescribeScalableTargets . If you no longer need a scalable target, you can deregister it using  DeregisterScalableTarget .
    See also: AWS API Documentation
    
    Examples
    This example registers a scalable target from an Amazon ECS service called web-app that is running on the default cluster, with a minimum desired count of 1 task and a maximum desired count of 10 tasks.
    Expected Output:
    This example registers a scalable target from an Amazon EC2 Spot fleet with a minimum target capacity of 1 and a maximum of 10.
    Expected Output:
    
    :example: response = client.register_scalable_target(
        ServiceNamespace='ecs'|'elasticmapreduce'|'ec2'|'appstream'|'dynamodb'|'rds'|'sagemaker',
        ResourceId='string',
        ScalableDimension='ecs:service:DesiredCount'|'ec2:spot-fleet-request:TargetCapacity'|'elasticmapreduce:instancegroup:InstanceCount'|'appstream:fleet:DesiredCapacity'|'dynamodb:table:ReadCapacityUnits'|'dynamodb:table:WriteCapacityUnits'|'dynamodb:index:ReadCapacityUnits'|'dynamodb:index:WriteCapacityUnits'|'rds:cluster:ReadReplicaCount'|'sagemaker:variant:DesiredInstanceCount',
        MinCapacity=123,
        MaxCapacity=123,
        RoleARN='string'
    )
    
    
    :type ServiceNamespace: string
    :param ServiceNamespace: [REQUIRED]
            The namespace of the AWS service. For more information, see AWS Service Namespaces in the Amazon Web Services General Reference .
            

    :type ResourceId: string
    :param ResourceId: [REQUIRED]
            The identifier of the resource associated with the scalable target. This string consists of the resource type and unique identifier.
            ECS service - The resource type is service and the unique identifier is the cluster name and service name. Example: service/default/sample-webapp .
            Spot fleet request - The resource type is spot-fleet-request and the unique identifier is the Spot fleet request ID. Example: spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE .
            EMR cluster - The resource type is instancegroup and the unique identifier is the cluster ID and instance group ID. Example: instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0 .
            AppStream 2.0 fleet - The resource type is fleet and the unique identifier is the fleet name. Example: fleet/sample-fleet .
            DynamoDB table - The resource type is table and the unique identifier is the resource ID. Example: table/my-table .
            DynamoDB global secondary index - The resource type is index and the unique identifier is the resource ID. Example: table/my-table/index/my-table-index .
            Aurora DB cluster - The resource type is cluster and the unique identifier is the cluster name. Example: cluster:my-db-cluster .
            Amazon SageMaker endpoint variants - The resource type is variant and the unique identifier is the resource ID. Example: endpoint/my-end-point/variant/KMeansClustering .
            

    :type ScalableDimension: string
    :param ScalableDimension: [REQUIRED]
            The scalable dimension associated with the scalable target. This string consists of the service namespace, resource type, and scaling property.
            ecs:service:DesiredCount - The desired task count of an ECS service.
            ec2:spot-fleet-request:TargetCapacity - The target capacity of a Spot fleet request.
            elasticmapreduce:instancegroup:InstanceCount - The instance count of an EMR Instance Group.
            appstream:fleet:DesiredCapacity - The desired capacity of an AppStream 2.0 fleet.
            dynamodb:table:ReadCapacityUnits - The provisioned read capacity for a DynamoDB table.
            dynamodb:table:WriteCapacityUnits - The provisioned write capacity for a DynamoDB table.
            dynamodb:index:ReadCapacityUnits - The provisioned read capacity for a DynamoDB global secondary index.
            dynamodb:index:WriteCapacityUnits - The provisioned write capacity for a DynamoDB global secondary index.
            rds:cluster:ReadReplicaCount - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition.
            sagemaker:variant:DesiredInstanceCount - The number of EC2 instances for an Amazon SageMaker model endpoint variant.
            

    :type MinCapacity: integer
    :param MinCapacity: The minimum value to scale to in response to a scale in event. This parameter is required if you are registering a scalable target.

    :type MaxCapacity: integer
    :param MaxCapacity: The maximum value to scale to in response to a scale out event. This parameter is required if you are registering a scalable target.

    :type RoleARN: string
    :param RoleARN: Application Auto Scaling creates a service-linked role that grants it permissions to modify the scalable target on your behalf. For more information, see Service-Linked Roles for Application Auto Scaling .
            For resources that are not supported using a service-linked role, this parameter is required and must specify the ARN of an IAM role that allows Application Auto Scaling to modify the scalable target on your behalf.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

