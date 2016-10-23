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


def delete_scaling_policy(PolicyName=None, ServiceNamespace=None, ResourceId=None, ScalableDimension=None):
    """
    :param PolicyName: [REQUIRED]
            The name of the scaling policy to delete.
            
    :type PolicyName: string
    :param ServiceNamespace: [REQUIRED]
            The namespace for the AWS service that the scaling policy is associated with. For more information, see AWS Service Namespaces in the Amazon Web Services General Reference.
            
    :type ServiceNamespace: string
    :param ResourceId: [REQUIRED]
            The resource type and unique identifier string for the resource associated with the scaling policy. For Amazon ECS services, the resource type is services , and the identifier is the cluster name and service name; for example, service/default/sample-webapp . For Amazon EC2 Spot fleet requests, the resource type is spot-fleet-request , and the identifier is the Spot fleet request ID; for example, spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE .
            
    :type ResourceId: string
    :param ScalableDimension: [REQUIRED]
            The scalable dimension associated with the scaling policy. The scalable dimension contains the service namespace, resource type, and scaling property, such as ecs:service:DesiredCount for the desired task count of an Amazon ECS service, or ec2:spot-fleet-request:TargetCapacity for the target capacity of an Amazon EC2 Spot fleet request.
            
    :type ScalableDimension: string
    """
    pass


def deregister_scalable_target(ServiceNamespace=None, ResourceId=None, ScalableDimension=None):
    """
    :param ServiceNamespace: [REQUIRED]
            The namespace for the AWS service that the scalable target is associated with. For more information, see AWS Service Namespaces in the Amazon Web Services General Reference.
            
    :type ServiceNamespace: string
    :param ResourceId: [REQUIRED]
            The resource type and unique identifier string for the resource associated with the scalable target. For Amazon ECS services, the resource type is services , and the identifier is the cluster name and service name; for example, service/default/sample-webapp . For Amazon EC2 Spot fleet requests, the resource type is spot-fleet-request , and the identifier is the Spot fleet request ID; for example, spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE .
            
    :type ResourceId: string
    :param ScalableDimension: [REQUIRED]
            The scalable dimension associated with the scalable target. The scalable dimension contains the service namespace, resource type, and scaling property, such as ecs:service:DesiredCount for the desired task count of an Amazon ECS service, or ec2:spot-fleet-request:TargetCapacity for the target capacity of an Amazon EC2 Spot fleet request.
            
    :type ScalableDimension: string
    """
    pass


def describe_scalable_targets(ServiceNamespace=None, ResourceIds=None, ScalableDimension=None, MaxResults=None,
                              NextToken=None):
    """
    :param ServiceNamespace: [REQUIRED]
            The namespace for the AWS service that the scalable target is associated with. For more information, see AWS Service Namespaces in the Amazon Web Services General Reference.
            
    :type ServiceNamespace: string
    :param ResourceIds: The resource type and unique identifier string for the resource associated with the scalable target. For Amazon ECS services, the resource type is services , and the identifier is the cluster name and service name; for example, service/default/sample-webapp . For Amazon EC2 Spot fleet requests, the resource type is spot-fleet-request , and the identifier is the Spot fleet request ID; for example, spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE . If you specify a scalable dimension, you must also specify a resource ID.
            (string) --
            
    :type ResourceIds: list
    :param ScalableDimension: The scalable dimension associated with the scalable target. The scalable dimension contains the service namespace, resource type, and scaling property, such as ecs:service:DesiredCount for the desired task count of an Amazon ECS service, or ec2:spot-fleet-request:TargetCapacity for the target capacity of an Amazon EC2 Spot fleet request. If you specify a scalable dimension, you must also specify a resource ID.
    :type ScalableDimension: string
    :param MaxResults: The maximum number of scalable target results returned by DescribeScalableTargets in paginated output. When this parameter is used, DescribeScalableTargets returns up to MaxResults results in a single page along with a NextToken response element. The remaining results of the initial request can be seen by sending another DescribeScalableTargets request with the returned NextToken value. This value can be between 1 and 50. If this parameter is not used, then DescribeScalableTargets returns up to 50 results and a NextToken value, if applicable.
    :type MaxResults: integer
    :param NextToken: The NextToken value returned from a previous paginated DescribeScalableTargets request. Pagination continues from the end of the previous results that returned the NextToken value. This value is null when there are no more results to return.
    :type NextToken: string
    """
    pass


def describe_scaling_activities(ServiceNamespace=None, ResourceId=None, ScalableDimension=None, MaxResults=None,
                                NextToken=None):
    """
    :param ServiceNamespace: [REQUIRED]
            The namespace for the AWS service that the scaling activity is associated with. For more information, see AWS Service Namespaces in the Amazon Web Services General Reference.
            
    :type ServiceNamespace: string
    :param ResourceId: The resource type and unique identifier string for the resource associated with the scaling activity. For Amazon ECS services, the resource type is services , and the identifier is the cluster name and service name; for example, service/default/sample-webapp . For Amazon EC2 Spot fleet requests, the resource type is spot-fleet-request , and the identifier is the Spot fleet request ID; for example, spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE . If you specify a scalable dimension, you must also specify a resource ID.
    :type ResourceId: string
    :param ScalableDimension: The scalable dimension associated with the scaling activity. The scalable dimension contains the service namespace, resource type, and scaling property, such as ecs:service:DesiredCount for the desired task count of an Amazon ECS service, or ec2:spot-fleet-request:TargetCapacity for the target capacity of an Amazon EC2 Spot fleet request. If you specify a scalable dimension, you must also specify a resource ID.
    :type ScalableDimension: string
    :param MaxResults: The maximum number of scaling activity results returned by DescribeScalingActivities in paginated output. When this parameter is used, DescribeScalingActivities returns up to MaxResults results in a single page along with a NextToken response element. The remaining results of the initial request can be seen by sending another DescribeScalingActivities request with the returned NextToken value. This value can be between 1 and 50. If this parameter is not used, then DescribeScalingActivities returns up to 50 results and a NextToken value, if applicable.
    :type MaxResults: integer
    :param NextToken: The NextToken value returned from a previous paginated DescribeScalingActivities request. Pagination continues from the end of the previous results that returned the NextToken value. This value is null when there are no more results to return.
    :type NextToken: string
    """
    pass


def describe_scaling_policies(PolicyNames=None, ServiceNamespace=None, ResourceId=None, ScalableDimension=None,
                              MaxResults=None, NextToken=None):
    """
    :param PolicyNames: The names of the scaling policies to describe.
            (string) --
            
    :type PolicyNames: list
    :param ServiceNamespace: [REQUIRED]
            The AWS service namespace of the scalable target that the scaling policy is associated with. For more information, see AWS Service Namespaces in the Amazon Web Services General Reference.
            
    :type ServiceNamespace: string
    :param ResourceId: The unique resource identifier string of the scalable target that the scaling policy is associated with. For Amazon ECS services, the resource type is services , and the identifier is the cluster name and service name; for example, service/default/sample-webapp . For Amazon EC2 Spot fleet requests, the resource type is spot-fleet-request , and the identifier is the Spot fleet request ID; for example, spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE . If you specify a scalable dimension, you must also specify a resource ID.
    :type ResourceId: string
    :param ScalableDimension: The scalable dimension of the scalable target that the scaling policy is associated with. The scalable dimension contains the service namespace, resource type, and scaling property, such as ecs:service:DesiredCount for the desired task count of an Amazon ECS service, or ec2:spot-fleet-request:TargetCapacity for the target capacity of an Amazon EC2 Spot fleet request. If you specify a scalable dimension, you must also specify a resource ID.
    :type ScalableDimension: string
    :param MaxResults: The maximum number of scaling policy results returned by DescribeScalingPolicies in paginated output. When this parameter is used, DescribeScalingPolicies returns up to MaxResults results in a single page along with a NextToken response element. The remaining results of the initial request can be seen by sending another DescribeScalingPolicies request with the returned NextToken value. This value can be between 1 and 50. If this parameter is not used, then DescribeScalingPolicies returns up to 50 results and a NextToken value, if applicable.
    :type MaxResults: integer
    :param NextToken: The NextToken value returned from a previous paginated DescribeScalingPolicies request. Pagination continues from the end of the previous results that returned the NextToken value. This value is null when there are no more results to return.
    :type NextToken: string
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


def get_waiter():
    """
    """
    pass


def put_scaling_policy(PolicyName=None, ServiceNamespace=None, ResourceId=None, ScalableDimension=None, PolicyType=None,
                       StepScalingPolicyConfiguration=None):
    """
    :param PolicyName: [REQUIRED]
            The name of the scaling policy.
            
    :type PolicyName: string
    :param ServiceNamespace: [REQUIRED]
            The AWS service namespace of the scalable target that this scaling policy applies to. For more information, see AWS Service Namespaces in the Amazon Web Services General Reference.
            
    :type ServiceNamespace: string
    :param ResourceId: [REQUIRED]
            The unique resource identifier string for the scalable target that this scaling policy applies to. For Amazon ECS services, the resource type is services , and the identifier is the cluster name and service name; for example, service/default/sample-webapp . For Amazon EC2 Spot fleet requests, the resource type is spot-fleet-request , and the identifier is the Spot fleet request ID; for example, spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE .
            
    :type ResourceId: string
    :param ScalableDimension: [REQUIRED]
            The scalable dimension of the scalable target that this scaling policy applies to. The scalable dimension contains the service namespace, resource type, and scaling property, such as ecs:service:DesiredCount for the desired task count of an Amazon ECS service, or ec2:spot-fleet-request:TargetCapacity for the target capacity of an Amazon EC2 Spot fleet request.
            
    :type ScalableDimension: string
    :param PolicyType: The policy type. If you are creating a new policy, this parameter is required. If you are updating an existing policy, this parameter is not required.
    :type PolicyType: string
    :param StepScalingPolicyConfiguration: The configuration for the step scaling policy. If you are creating a new policy, this parameter is required. If you are updating an existing policy, this parameter is not required. For more information, see StepScalingPolicyConfiguration and StepAdjustment .
            AdjustmentType (string) --The adjustment type, which specifies how the ScalingAdjustment parameter in a StepAdjustment is interpreted.
            StepAdjustments (list) --A set of adjustments that enable you to scale based on the size of the alarm breach.
            (dict) --An object representing a step adjustment for a StepScalingPolicyConfiguration . Describes an adjustment based on the difference between the value of the aggregated CloudWatch metric and the breach threshold that you've defined for the alarm.
            For the following examples, suppose that you have an alarm with a breach threshold of 50:
            If you want the adjustment to be triggered when the metric is greater than or equal to 50 and less than 60, specify a lower bound of 0 and an upper bound of 10.
            If you want the adjustment to be triggered when the metric is greater than 40 and less than or equal to 50, specify a lower bound of -10 and an upper bound of 0.
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
            For scale out policies, while Cooldown is in effect, the capacity that has been added by the previous scale out event that initiated the Cooldown is calculated as part of the desired capacity for the next scale out. The intention is to continuously (but not excessively) scale out. For example, an alarm triggers a step scaling policy to scale out an Amazon ECS service by 2 tasks, the scaling activity completes successfully, and a Cooldown period of 5 minutes starts. During the Cooldown period, if the alarm triggers the same policy again but at a more aggressive step adjustment to scale out the service by 3 tasks, the 2 tasks that were added in the previous scale out event are considered part of that capacity and only 1 additional task is added to the desired count.
            For scale in policies, the Cooldown period is used to block subsequent scale in requests until it has expired. The intention is to scale in conservatively to protect your application's availability. However, if another alarm triggers a scale out policy during the Cooldown period after a scale-in, Application Auto Scaling scales out your scalable target immediately.
            MetricAggregationType (string) --The aggregation type for the CloudWatch metrics. Valid values are Minimum , Maximum , and Average .
            
    :type StepScalingPolicyConfiguration: dict
    """
    pass


def register_scalable_target(ServiceNamespace=None, ResourceId=None, ScalableDimension=None, MinCapacity=None,
                             MaxCapacity=None, RoleARN=None):
    """
    :param ServiceNamespace: [REQUIRED]
            The namespace for the AWS service that the scalable target is associated with. For Amazon ECS services, the namespace value is ecs . For more information, see AWS Service Namespaces in the Amazon Web Services General Reference.
            
    :type ServiceNamespace: string
    :param ResourceId: [REQUIRED]
            The resource type and unique identifier string for the resource to associate with the scalable target. For Amazon ECS services, the resource type is services , and the identifier is the cluster name and service name; for example, service/default/sample-webapp . For Amazon EC2 Spot fleet requests, the resource type is spot-fleet-request , and the identifier is the Spot fleet request ID; for example, spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE .
            
    :type ResourceId: string
    :param ScalableDimension: [REQUIRED]
            The scalable dimension associated with the scalable target. The scalable dimension contains the service namespace, resource type, and scaling property, such as ecs:service:DesiredCount for the desired task count of an Amazon ECS service, or ec2:spot-fleet-request:TargetCapacity for the target capacity of an Amazon EC2 Spot fleet request.
            
    :type ScalableDimension: string
    :param MinCapacity: The minimum value for this scalable target to scale in to in response to scaling activities. This parameter is required if you are registering a new scalable target, and it is optional if you are updating an existing one.
    :type MinCapacity: integer
    :param MaxCapacity: The maximum value for this scalable target to scale out to in response to scaling activities. This parameter is required if you are registering a new scalable target, and it is optional if you are updating an existing one.
    :type MaxCapacity: integer
    :param RoleARN: The ARN of the IAM role that allows Application Auto Scaling to modify your scalable target on your behalf. This parameter is required if you are registering a new scalable target, and it is optional if you are updating an existing one.
    :type RoleARN: string
    """
    pass
