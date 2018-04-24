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

def create_scaling_plan(ScalingPlanName=None, ApplicationSource=None, ScalingInstructions=None):
    """
    Creates a scaling plan.
    A scaling plan contains a set of instructions used to configure dynamic scaling for the scalable resources in your application. AWS Auto Scaling creates target tracking scaling policies based on the scaling instructions in your scaling plan.
    See also: AWS API Documentation
    
    
    :example: response = client.create_scaling_plan(
        ScalingPlanName='string',
        ApplicationSource={
            'CloudFormationStackARN': 'string'
        },
        ScalingInstructions=[
            {
                'ServiceNamespace': 'autoscaling'|'ecs'|'ec2'|'rds'|'dynamodb',
                'ResourceId': 'string',
                'ScalableDimension': 'autoscaling:autoScalingGroup:DesiredCapacity'|'ecs:service:DesiredCount'|'ec2:spot-fleet-request:TargetCapacity'|'rds:cluster:ReadReplicaCount'|'dynamodb:table:ReadCapacityUnits'|'dynamodb:table:WriteCapacityUnits'|'dynamodb:index:ReadCapacityUnits'|'dynamodb:index:WriteCapacityUnits',
                'MinCapacity': 123,
                'MaxCapacity': 123,
                'TargetTrackingConfigurations': [
                    {
                        'PredefinedScalingMetricSpecification': {
                            'PredefinedScalingMetricType': 'ASGAverageCPUUtilization'|'ASGAverageNetworkIn'|'ASGAverageNetworkOut'|'DynamoDBReadCapacityUtilization'|'DynamoDBWriteCapacityUtilization'|'ECSServiceAverageCPUUtilization'|'ECSServiceAverageMemoryUtilization'|'ALBRequestCountPerTarget'|'RDSReaderAverageCPUUtilization'|'RDSReaderAverageDatabaseConnections'|'EC2SpotFleetRequestAverageCPUUtilization'|'EC2SpotFleetRequestAverageNetworkIn'|'EC2SpotFleetRequestAverageNetworkOut',
                            'ResourceLabel': 'string'
                        },
                        'CustomizedScalingMetricSpecification': {
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
                        'TargetValue': 123.0,
                        'DisableScaleIn': True|False,
                        'ScaleOutCooldown': 123,
                        'ScaleInCooldown': 123,
                        'EstimatedInstanceWarmup': 123
                    },
                ]
            },
        ]
    )
    
    
    :type ScalingPlanName: string
    :param ScalingPlanName: [REQUIRED]
            The name of the scaling plan.
            

    :type ApplicationSource: dict
    :param ApplicationSource: [REQUIRED]
            The source for the application.
            CloudFormationStackARN (string) --The Amazon Resource Name (ARN) of a CloudFormation stack.
            

    :type ScalingInstructions: list
    :param ScalingInstructions: [REQUIRED]
            The scaling instructions.
            (dict) --Specifies the scaling configuration for a scalable resource.
            ServiceNamespace (string) -- [REQUIRED]The namespace of the AWS service.
            ResourceId (string) -- [REQUIRED]The ID of the resource. This string consists of the resource type and unique identifier.
            Auto Scaling group - The resource type is autoScalingGroup and the unique identifier is the name of the Auto Scaling group. Example: autoScalingGroup/my-asg .
            ECS service - The resource type is service and the unique identifier is the cluster name and service name. Example: service/default/sample-webapp .
            Spot fleet request - The resource type is spot-fleet-request and the unique identifier is the Spot fleet request ID. Example: spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE .
            DynamoDB table - The resource type is table and the unique identifier is the resource ID. Example: table/my-table .
            DynamoDB global secondary index - The resource type is index and the unique identifier is the resource ID. Example: table/my-table/index/my-table-index .
            Aurora DB cluster - The resource type is cluster and the unique identifier is the cluster name. Example: cluster:my-db-cluster .
            ScalableDimension (string) -- [REQUIRED]The scalable dimension associated with the resource.
            autoscaling:autoScalingGroup:DesiredCapacity - The desired capacity of an Auto Scaling group.
            ecs:service:DesiredCount - The desired task count of an ECS service.
            ec2:spot-fleet-request:TargetCapacity - The target capacity of a Spot fleet request.
            dynamodb:table:ReadCapacityUnits - The provisioned read capacity for a DynamoDB table.
            dynamodb:table:WriteCapacityUnits - The provisioned write capacity for a DynamoDB table.
            dynamodb:index:ReadCapacityUnits - The provisioned read capacity for a DynamoDB global secondary index.
            dynamodb:index:WriteCapacityUnits - The provisioned write capacity for a DynamoDB global secondary index.
            rds:cluster:ReadReplicaCount - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition.
            MinCapacity (integer) -- [REQUIRED]The minimum value to scale to in response to a scale in event.
            MaxCapacity (integer) -- [REQUIRED]The maximum value to scale to in response to a scale out event.
            TargetTrackingConfigurations (list) -- [REQUIRED]The target tracking scaling policies (up to 10).
            (dict) --Represents a target tracking scaling policy.
            PredefinedScalingMetricSpecification (dict) --A predefined metric.
            PredefinedScalingMetricType (string) -- [REQUIRED]The metric type. The ALBRequestCountPerTarget metric type applies only to Auto Scaling groups, Sport Fleet requests, and ECS services.
            ResourceLabel (string) --Identifies the resource associated with the metric type. You can't specify a resource label unless the metric type is ALBRequestCountPerTarget and there is a target group attached to the Auto Scaling group, Spot Fleet request, or ECS service.
            The format is app/load-balancer-name/load-balancer-id/targetgroup/target-group-name/target-group-id, where:
            app/load-balancer-name/load-balancer-idis the final portion of the load balancer ARN
            targetgroup/target-group-name/target-group-idis the final portion of the target group ARN.
            
            CustomizedScalingMetricSpecification (dict) --A customized metric.
            MetricName (string) -- [REQUIRED]The name of the metric.
            Namespace (string) -- [REQUIRED]The namespace of the metric.
            Dimensions (list) --The dimensions of the metric.
            (dict) --Represents a dimension for a customized metric.
            Name (string) -- [REQUIRED]The name of the dimension.
            Value (string) -- [REQUIRED]The value of the dimension.
            
            Statistic (string) -- [REQUIRED]The statistic of the metric.
            Unit (string) --The unit of the metric.
            TargetValue (float) -- [REQUIRED]The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2).
            DisableScaleIn (boolean) --Indicates whether scale in by the target tracking policy is disabled. If the value is true , scale in is disabled and the target tracking policy won't remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. The default value is false .
            ScaleOutCooldown (integer) --The amount of time, in seconds, after a scale out activity completes before another scale out activity can start. This value is not used if the scalable resource is an Auto Scaling group.
            While the cooldown period is in effect, the capacity that has been added by the previous scale out event that initiated the cooldown is calculated as part of the desired capacity for the next scale out. The intention is to continuously (but not excessively) scale out.
            ScaleInCooldown (integer) --The amount of time, in seconds, after a scale in activity completes before another scale in activity can start. This value is not used if the scalable resource is an Auto Scaling group.
            The cooldown period is used to block subsequent scale in requests until it has expired. The intention is to scale in conservatively to protect your application's availability. However, if another alarm triggers a scale out policy during the cooldown period after a scale-in, AWS Auto Scaling scales out your scalable target immediately.
            EstimatedInstanceWarmup (integer) --The estimated time, in seconds, until a newly launched instance can contribute to the CloudWatch metrics. This value is used only if the resource is an Auto Scaling group.
            
            
            

    :rtype: dict
    :return: {
        'ScalingPlanVersion': 123
    }
    
    
    """
    pass

def delete_scaling_plan(ScalingPlanName=None, ScalingPlanVersion=None):
    """
    Deletes the specified scaling plan.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_scaling_plan(
        ScalingPlanName='string',
        ScalingPlanVersion=123
    )
    
    
    :type ScalingPlanName: string
    :param ScalingPlanName: [REQUIRED]
            The name of the scaling plan.
            

    :type ScalingPlanVersion: integer
    :param ScalingPlanVersion: [REQUIRED]
            The version of the scaling plan.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def describe_scaling_plan_resources(ScalingPlanName=None, ScalingPlanVersion=None, MaxResults=None, NextToken=None):
    """
    Describes the scalable resources in the specified scaling plan.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_scaling_plan_resources(
        ScalingPlanName='string',
        ScalingPlanVersion=123,
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type ScalingPlanName: string
    :param ScalingPlanName: [REQUIRED]
            The name of the scaling plan.
            

    :type ScalingPlanVersion: integer
    :param ScalingPlanVersion: [REQUIRED]
            The version of the scaling plan.
            

    :type MaxResults: integer
    :param MaxResults: The maximum number of scalable resources to return. This value can be between 1 and 50. The default value is 50.

    :type NextToken: string
    :param NextToken: The token for the next set of results.

    :rtype: dict
    :return: {
        'ScalingPlanResources': [
            {
                'ScalingPlanName': 'string',
                'ScalingPlanVersion': 123,
                'ServiceNamespace': 'autoscaling'|'ecs'|'ec2'|'rds'|'dynamodb',
                'ResourceId': 'string',
                'ScalableDimension': 'autoscaling:autoScalingGroup:DesiredCapacity'|'ecs:service:DesiredCount'|'ec2:spot-fleet-request:TargetCapacity'|'rds:cluster:ReadReplicaCount'|'dynamodb:table:ReadCapacityUnits'|'dynamodb:table:WriteCapacityUnits'|'dynamodb:index:ReadCapacityUnits'|'dynamodb:index:WriteCapacityUnits',
                'ScalingPolicies': [
                    {
                        'PolicyName': 'string',
                        'PolicyType': 'TargetTrackingScaling',
                        'TargetTrackingConfiguration': {
                            'PredefinedScalingMetricSpecification': {
                                'PredefinedScalingMetricType': 'ASGAverageCPUUtilization'|'ASGAverageNetworkIn'|'ASGAverageNetworkOut'|'DynamoDBReadCapacityUtilization'|'DynamoDBWriteCapacityUtilization'|'ECSServiceAverageCPUUtilization'|'ECSServiceAverageMemoryUtilization'|'ALBRequestCountPerTarget'|'RDSReaderAverageCPUUtilization'|'RDSReaderAverageDatabaseConnections'|'EC2SpotFleetRequestAverageCPUUtilization'|'EC2SpotFleetRequestAverageNetworkIn'|'EC2SpotFleetRequestAverageNetworkOut',
                                'ResourceLabel': 'string'
                            },
                            'CustomizedScalingMetricSpecification': {
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
                            'TargetValue': 123.0,
                            'DisableScaleIn': True|False,
                            'ScaleOutCooldown': 123,
                            'ScaleInCooldown': 123,
                            'EstimatedInstanceWarmup': 123
                        }
                    },
                ],
                'ScalingStatusCode': 'Inactive'|'PartiallyActive'|'Active',
                'ScalingStatusMessage': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Auto Scaling group - The resource type is autoScalingGroup and the unique identifier is the name of the Auto Scaling group. Example: autoScalingGroup/my-asg .
    ECS service - The resource type is service and the unique identifier is the cluster name and service name. Example: service/default/sample-webapp .
    Spot fleet request - The resource type is spot-fleet-request and the unique identifier is the Spot fleet request ID. Example: spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE .
    DynamoDB table - The resource type is table and the unique identifier is the resource ID. Example: table/my-table .
    DynamoDB global secondary index - The resource type is index and the unique identifier is the resource ID. Example: table/my-table/index/my-table-index .
    Aurora DB cluster - The resource type is cluster and the unique identifier is the cluster name. Example: cluster:my-db-cluster .
    
    """
    pass

def describe_scaling_plans(ScalingPlanNames=None, ScalingPlanVersion=None, ApplicationSources=None, MaxResults=None, NextToken=None):
    """
    Describes the specified scaling plans or all of your scaling plans.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_scaling_plans(
        ScalingPlanNames=[
            'string',
        ],
        ScalingPlanVersion=123,
        ApplicationSources=[
            {
                'CloudFormationStackARN': 'string'
            },
        ],
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type ScalingPlanNames: list
    :param ScalingPlanNames: The names of the scaling plans (up to 10). If you specify application sources, you cannot specify scaling plan names.
            (string) --
            

    :type ScalingPlanVersion: integer
    :param ScalingPlanVersion: The version of the scaling plan. If you specify a scaling plan version, you must also specify a scaling plan name.

    :type ApplicationSources: list
    :param ApplicationSources: The sources for the applications (up to 10). If you specify scaling plan names, you cannot specify application sources.
            (dict) --Represents an application source.
            CloudFormationStackARN (string) --The Amazon Resource Name (ARN) of a CloudFormation stack.
            
            

    :type MaxResults: integer
    :param MaxResults: The maximum number of scalable resources to return. This value can be between 1 and 50. The default value is 50.

    :type NextToken: string
    :param NextToken: The token for the next set of results.

    :rtype: dict
    :return: {
        'ScalingPlans': [
            {
                'ScalingPlanName': 'string',
                'ScalingPlanVersion': 123,
                'ApplicationSource': {
                    'CloudFormationStackARN': 'string'
                },
                'ScalingInstructions': [
                    {
                        'ServiceNamespace': 'autoscaling'|'ecs'|'ec2'|'rds'|'dynamodb',
                        'ResourceId': 'string',
                        'ScalableDimension': 'autoscaling:autoScalingGroup:DesiredCapacity'|'ecs:service:DesiredCount'|'ec2:spot-fleet-request:TargetCapacity'|'rds:cluster:ReadReplicaCount'|'dynamodb:table:ReadCapacityUnits'|'dynamodb:table:WriteCapacityUnits'|'dynamodb:index:ReadCapacityUnits'|'dynamodb:index:WriteCapacityUnits',
                        'MinCapacity': 123,
                        'MaxCapacity': 123,
                        'TargetTrackingConfigurations': [
                            {
                                'PredefinedScalingMetricSpecification': {
                                    'PredefinedScalingMetricType': 'ASGAverageCPUUtilization'|'ASGAverageNetworkIn'|'ASGAverageNetworkOut'|'DynamoDBReadCapacityUtilization'|'DynamoDBWriteCapacityUtilization'|'ECSServiceAverageCPUUtilization'|'ECSServiceAverageMemoryUtilization'|'ALBRequestCountPerTarget'|'RDSReaderAverageCPUUtilization'|'RDSReaderAverageDatabaseConnections'|'EC2SpotFleetRequestAverageCPUUtilization'|'EC2SpotFleetRequestAverageNetworkIn'|'EC2SpotFleetRequestAverageNetworkOut',
                                    'ResourceLabel': 'string'
                                },
                                'CustomizedScalingMetricSpecification': {
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
                                'TargetValue': 123.0,
                                'DisableScaleIn': True|False,
                                'ScaleOutCooldown': 123,
                                'ScaleInCooldown': 123,
                                'EstimatedInstanceWarmup': 123
                            },
                        ]
                    },
                ],
                'StatusCode': 'Active'|'ActiveWithProblems'|'CreationInProgress'|'CreationFailed'|'DeletionInProgress'|'DeletionFailed',
                'StatusMessage': 'string',
                'CreationTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Auto Scaling group - The resource type is autoScalingGroup and the unique identifier is the name of the Auto Scaling group. Example: autoScalingGroup/my-asg .
    ECS service - The resource type is service and the unique identifier is the cluster name and service name. Example: service/default/sample-webapp .
    Spot fleet request - The resource type is spot-fleet-request and the unique identifier is the Spot fleet request ID. Example: spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE .
    DynamoDB table - The resource type is table and the unique identifier is the resource ID. Example: table/my-table .
    DynamoDB global secondary index - The resource type is index and the unique identifier is the resource ID. Example: table/my-table/index/my-table-index .
    Aurora DB cluster - The resource type is cluster and the unique identifier is the cluster name. Example: cluster:my-db-cluster .
    
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

