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

def attach_instances(InstanceIds=None, AutoScalingGroupName=None):
    """
    Attaches one or more EC2 instances to the specified Auto Scaling group.
    When you attach instances, Amazon EC2 Auto Scaling increases the desired capacity of the group by the number of instances being attached. If the number of instances being attached plus the desired capacity of the group exceeds the maximum size of the group, the operation fails.
    If there is a Classic Load Balancer attached to your Auto Scaling group, the instances are also registered with the load balancer. If there are target groups attached to your Auto Scaling group, the instances are also registered with the target groups.
    For more information, see Attach EC2 Instances to Your Auto Scaling Group in the Amazon EC2 Auto Scaling User Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example attaches the specified instance to the specified Auto Scaling group.
    Expected Output:
    
    :example: response = client.attach_instances(
        InstanceIds=[
            'string',
        ],
        AutoScalingGroupName='string'
    )
    
    
    :type InstanceIds: list
    :param InstanceIds: The IDs of the instances. You can specify up to 20 instances.\n\n(string) --\n\n

    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: [REQUIRED]\nThe name of the Auto Scaling group.\n

    :return: response = client.attach_instances(
        AutoScalingGroupName='my-auto-scaling-group',
        InstanceIds=[
            'i-93633f9b',
        ],
    )
    
    print(response)
    
    
    :returns: 
    AutoScaling.Client.exceptions.ResourceContentionFault
    AutoScaling.Client.exceptions.ServiceLinkedRoleFailure
    
    """
    pass

def attach_load_balancer_target_groups(AutoScalingGroupName=None, TargetGroupARNs=None):
    """
    Attaches one or more target groups to the specified Auto Scaling group.
    To describe the target groups for an Auto Scaling group, call the  DescribeLoadBalancerTargetGroups API. To detach the target group from the Auto Scaling group, call the  DetachLoadBalancerTargetGroups API.
    With Application Load Balancers and Network Load Balancers, instances are registered as targets with a target group. With Classic Load Balancers, instances are registered with the load balancer. For more information, see Attaching a Load Balancer to Your Auto Scaling Group in the Amazon EC2 Auto Scaling User Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example attaches the specified target group to the specified Auto Scaling group.
    Expected Output:
    
    :example: response = client.attach_load_balancer_target_groups(
        AutoScalingGroupName='string',
        TargetGroupARNs=[
            'string',
        ]
    )
    
    
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: [REQUIRED]\nThe name of the Auto Scaling group.\n

    :type TargetGroupARNs: list
    :param TargetGroupARNs: [REQUIRED]\nThe Amazon Resource Names (ARN) of the target groups. You can specify up to 10 target groups.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

AutoScaling.Client.exceptions.ResourceContentionFault
AutoScaling.Client.exceptions.ServiceLinkedRoleFailure

Examples
This example attaches the specified target group to the specified Auto Scaling group.
response = client.attach_load_balancer_target_groups(
    AutoScalingGroupName='my-auto-scaling-group',
    TargetGroupARNs=[
        'arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067',
    ],
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

def attach_load_balancers(AutoScalingGroupName=None, LoadBalancerNames=None):
    """
    Attaches one or more Classic Load Balancers to the specified Auto Scaling group. Amazon EC2 Auto Scaling registers the running instances with these Classic Load Balancers.
    To describe the load balancers for an Auto Scaling group, call the  DescribeLoadBalancers API. To detach the load balancer from the Auto Scaling group, call the  DetachLoadBalancers API.
    For more information, see Attaching a Load Balancer to Your Auto Scaling Group in the Amazon EC2 Auto Scaling User Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example attaches the specified load balancer to the specified Auto Scaling group.
    Expected Output:
    
    :example: response = client.attach_load_balancers(
        AutoScalingGroupName='string',
        LoadBalancerNames=[
            'string',
        ]
    )
    
    
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: [REQUIRED]\nThe name of the Auto Scaling group.\n

    :type LoadBalancerNames: list
    :param LoadBalancerNames: [REQUIRED]\nThe names of the load balancers. You can specify up to 10 load balancers.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

AutoScaling.Client.exceptions.ResourceContentionFault
AutoScaling.Client.exceptions.ServiceLinkedRoleFailure

Examples
This example attaches the specified load balancer to the specified Auto Scaling group.
response = client.attach_load_balancers(
    AutoScalingGroupName='my-auto-scaling-group',
    LoadBalancerNames=[
        'my-load-balancer',
    ],
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

def batch_delete_scheduled_action(AutoScalingGroupName=None, ScheduledActionNames=None):
    """
    Deletes one or more scheduled actions for the specified Auto Scaling group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_delete_scheduled_action(
        AutoScalingGroupName='string',
        ScheduledActionNames=[
            'string',
        ]
    )
    
    
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: [REQUIRED]\nThe name of the Auto Scaling group.\n

    :type ScheduledActionNames: list
    :param ScheduledActionNames: [REQUIRED]\nThe names of the scheduled actions to delete. The maximum number allowed is 50.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'FailedScheduledActions': [
        {
            'ScheduledActionName': 'string',
            'ErrorCode': 'string',
            'ErrorMessage': 'string'
        },
    ]
}


Response Structure

(dict) --

FailedScheduledActions (list) --
The names of the scheduled actions that could not be deleted, including an error message.

(dict) --
Describes a scheduled action that could not be created, updated, or deleted.

ScheduledActionName (string) --
The name of the scheduled action.

ErrorCode (string) --
The error code.

ErrorMessage (string) --
The error message accompanying the error code.











Exceptions

AutoScaling.Client.exceptions.ResourceContentionFault


    :return: {
        'FailedScheduledActions': [
            {
                'ScheduledActionName': 'string',
                'ErrorCode': 'string',
                'ErrorMessage': 'string'
            },
        ]
    }
    
    
    :returns: 
    AutoScaling.Client.exceptions.ResourceContentionFault
    
    """
    pass

def batch_put_scheduled_update_group_action(AutoScalingGroupName=None, ScheduledUpdateGroupActions=None):
    """
    Creates or updates one or more scheduled scaling actions for an Auto Scaling group. If you leave a parameter unspecified when updating a scheduled scaling action, the corresponding value remains unchanged.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_put_scheduled_update_group_action(
        AutoScalingGroupName='string',
        ScheduledUpdateGroupActions=[
            {
                'ScheduledActionName': 'string',
                'StartTime': datetime(2015, 1, 1),
                'EndTime': datetime(2015, 1, 1),
                'Recurrence': 'string',
                'MinSize': 123,
                'MaxSize': 123,
                'DesiredCapacity': 123
            },
        ]
    )
    
    
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: [REQUIRED]\nThe name of the Auto Scaling group.\n

    :type ScheduledUpdateGroupActions: list
    :param ScheduledUpdateGroupActions: [REQUIRED]\nOne or more scheduled actions. The maximum number allowed is 50.\n\n(dict) --Describes information used for one or more scheduled scaling action updates in a BatchPutScheduledUpdateGroupAction operation.\nWhen updating a scheduled scaling action, all optional parameters are left unchanged if not specified.\n\nScheduledActionName (string) -- [REQUIRED]The name of the scaling action.\n\nStartTime (datetime) --The date and time for the action to start, in YYYY-MM-DDThh:mm:ssZ format in UTC/GMT only and in quotes (for example, '2019-06-01T00:00:00Z' ).\nIf you specify Recurrence and StartTime , Amazon EC2 Auto Scaling performs the action at this time, and then performs the action based on the specified recurrence.\nIf you try to schedule the action in the past, Amazon EC2 Auto Scaling returns an error message.\n\nEndTime (datetime) --The date and time for the recurring schedule to end. Amazon EC2 Auto Scaling does not perform the action after this time.\n\nRecurrence (string) --The recurring schedule for the action, in Unix cron syntax format. This format consists of five fields separated by white spaces: [Minute] [Hour] [Day_of_Month] [Month_of_Year] [Day_of_Week]. The value must be in quotes (for example, '30 0 1 1,6,12 *' ). For more information about this format, see Crontab .\nWhen StartTime and EndTime are specified with Recurrence , they form the boundaries of when the recurring action starts and stops.\n\nMinSize (integer) --The minimum size of the Auto Scaling group.\n\nMaxSize (integer) --The maximum size of the Auto Scaling group.\n\nDesiredCapacity (integer) --The desired capacity is the initial capacity of the Auto Scaling group after the scheduled action runs and the capacity it attempts to maintain.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'FailedScheduledUpdateGroupActions': [
        {
            'ScheduledActionName': 'string',
            'ErrorCode': 'string',
            'ErrorMessage': 'string'
        },
    ]
}


Response Structure

(dict) --

FailedScheduledUpdateGroupActions (list) --
The names of the scheduled actions that could not be created or updated, including an error message.

(dict) --
Describes a scheduled action that could not be created, updated, or deleted.

ScheduledActionName (string) --
The name of the scheduled action.

ErrorCode (string) --
The error code.

ErrorMessage (string) --
The error message accompanying the error code.











Exceptions

AutoScaling.Client.exceptions.AlreadyExistsFault
AutoScaling.Client.exceptions.LimitExceededFault
AutoScaling.Client.exceptions.ResourceContentionFault


    :return: {
        'FailedScheduledUpdateGroupActions': [
            {
                'ScheduledActionName': 'string',
                'ErrorCode': 'string',
                'ErrorMessage': 'string'
            },
        ]
    }
    
    
    :returns: 
    AutoScaling.Client.exceptions.AlreadyExistsFault
    AutoScaling.Client.exceptions.LimitExceededFault
    AutoScaling.Client.exceptions.ResourceContentionFault
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def complete_lifecycle_action(LifecycleHookName=None, AutoScalingGroupName=None, LifecycleActionToken=None, LifecycleActionResult=None, InstanceId=None):
    """
    Completes the lifecycle action for the specified token or instance with the specified result.
    This step is a part of the procedure for adding a lifecycle hook to an Auto Scaling group:
    For more information, see Amazon EC2 Auto Scaling Lifecycle Hooks in the Amazon EC2 Auto Scaling User Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example notifies Auto Scaling that the specified lifecycle action is complete so that it can finish launching or terminating the instance.
    Expected Output:
    
    :example: response = client.complete_lifecycle_action(
        LifecycleHookName='string',
        AutoScalingGroupName='string',
        LifecycleActionToken='string',
        LifecycleActionResult='string',
        InstanceId='string'
    )
    
    
    :type LifecycleHookName: string
    :param LifecycleHookName: [REQUIRED]\nThe name of the lifecycle hook.\n

    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: [REQUIRED]\nThe name of the Auto Scaling group.\n

    :type LifecycleActionToken: string
    :param LifecycleActionToken: A universally unique identifier (UUID) that identifies a specific lifecycle action associated with an instance. Amazon EC2 Auto Scaling sends this token to the notification target you specified when you created the lifecycle hook.

    :type LifecycleActionResult: string
    :param LifecycleActionResult: [REQUIRED]\nThe action for the group to take. This parameter can be either CONTINUE or ABANDON .\n

    :type InstanceId: string
    :param InstanceId: The ID of the instance.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

AutoScaling.Client.exceptions.ResourceContentionFault

Examples
This example notifies Auto Scaling that the specified lifecycle action is complete so that it can finish launching or terminating the instance.
response = client.complete_lifecycle_action(
    AutoScalingGroupName='my-auto-scaling-group',
    LifecycleActionResult='CONTINUE',
    LifecycleActionToken='bcd2f1b8-9a78-44d3-8a7a-4dd07d7cf635',
    LifecycleHookName='my-lifecycle-hook',
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
    LifecycleHookName (string) -- [REQUIRED]
    The name of the lifecycle hook.
    
    AutoScalingGroupName (string) -- [REQUIRED]
    The name of the Auto Scaling group.
    
    LifecycleActionToken (string) -- A universally unique identifier (UUID) that identifies a specific lifecycle action associated with an instance. Amazon EC2 Auto Scaling sends this token to the notification target you specified when you created the lifecycle hook.
    LifecycleActionResult (string) -- [REQUIRED]
    The action for the group to take. This parameter can be either CONTINUE or ABANDON .
    
    InstanceId (string) -- The ID of the instance.
    
    """
    pass

def create_auto_scaling_group(AutoScalingGroupName=None, LaunchConfigurationName=None, LaunchTemplate=None, MixedInstancesPolicy=None, InstanceId=None, MinSize=None, MaxSize=None, DesiredCapacity=None, DefaultCooldown=None, AvailabilityZones=None, LoadBalancerNames=None, TargetGroupARNs=None, HealthCheckType=None, HealthCheckGracePeriod=None, PlacementGroup=None, VPCZoneIdentifier=None, TerminationPolicies=None, NewInstancesProtectedFromScaleIn=None, LifecycleHookSpecificationList=None, Tags=None, ServiceLinkedRoleARN=None, MaxInstanceLifetime=None):
    """
    Creates an Auto Scaling group with the specified name and attributes.
    If you exceed your maximum limit of Auto Scaling groups, the call fails. To query this limit, call the  DescribeAccountLimits API. For information about updating this limit, see Amazon EC2 Auto Scaling Service Quotas in the Amazon EC2 Auto Scaling User Guide .
    For introductory exercises for creating an Auto Scaling group, see Getting Started with Amazon EC2 Auto Scaling and Tutorial: Set Up a Scaled and Load-Balanced Application in the Amazon EC2 Auto Scaling User Guide . For more information, see Auto Scaling Groups in the Amazon EC2 Auto Scaling User Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example creates an Auto Scaling group.
    Expected Output:
    This example creates an Auto Scaling group and attaches the specified Classic Load Balancer.
    Expected Output:
    This example creates an Auto Scaling group and attaches the specified target group.
    Expected Output:
    
    :example: response = client.create_auto_scaling_group(
        AutoScalingGroupName='string',
        LaunchConfigurationName='string',
        LaunchTemplate={
            'LaunchTemplateId': 'string',
            'LaunchTemplateName': 'string',
            'Version': 'string'
        },
        MixedInstancesPolicy={
            'LaunchTemplate': {
                'LaunchTemplateSpecification': {
                    'LaunchTemplateId': 'string',
                    'LaunchTemplateName': 'string',
                    'Version': 'string'
                },
                'Overrides': [
                    {
                        'InstanceType': 'string',
                        'WeightedCapacity': 'string'
                    },
                ]
            },
            'InstancesDistribution': {
                'OnDemandAllocationStrategy': 'string',
                'OnDemandBaseCapacity': 123,
                'OnDemandPercentageAboveBaseCapacity': 123,
                'SpotAllocationStrategy': 'string',
                'SpotInstancePools': 123,
                'SpotMaxPrice': 'string'
            }
        },
        InstanceId='string',
        MinSize=123,
        MaxSize=123,
        DesiredCapacity=123,
        DefaultCooldown=123,
        AvailabilityZones=[
            'string',
        ],
        LoadBalancerNames=[
            'string',
        ],
        TargetGroupARNs=[
            'string',
        ],
        HealthCheckType='string',
        HealthCheckGracePeriod=123,
        PlacementGroup='string',
        VPCZoneIdentifier='string',
        TerminationPolicies=[
            'string',
        ],
        NewInstancesProtectedFromScaleIn=True|False,
        LifecycleHookSpecificationList=[
            {
                'LifecycleHookName': 'string',
                'LifecycleTransition': 'string',
                'NotificationMetadata': 'string',
                'HeartbeatTimeout': 123,
                'DefaultResult': 'string',
                'NotificationTargetARN': 'string',
                'RoleARN': 'string'
            },
        ],
        Tags=[
            {
                'ResourceId': 'string',
                'ResourceType': 'string',
                'Key': 'string',
                'Value': 'string',
                'PropagateAtLaunch': True|False
            },
        ],
        ServiceLinkedRoleARN='string',
        MaxInstanceLifetime=123
    )
    
    
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: [REQUIRED]\nThe name of the Auto Scaling group. This name must be unique per Region per account.\n

    :type LaunchConfigurationName: string
    :param LaunchConfigurationName: The name of the launch configuration to use when an instance is launched. To get the launch configuration name, use the DescribeLaunchConfigurations API operation. New launch configurations can be created with the CreateLaunchConfiguration API.\nYou must specify one of the following parameters in your request: LaunchConfigurationName , LaunchTemplate , InstanceId , or MixedInstancesPolicy .\n

    :type LaunchTemplate: dict
    :param LaunchTemplate: Parameters used to specify the launch template and version to use when an instance is launched.\nFor more information, see LaunchTemplateSpecification in the Amazon EC2 Auto Scaling API Reference .\nYou can alternatively associate a launch template to the Auto Scaling group by using the MixedInstancesPolicy parameter.\nYou must specify one of the following parameters in your request: LaunchConfigurationName , LaunchTemplate , InstanceId , or MixedInstancesPolicy .\n\nLaunchTemplateId (string) --The ID of the launch template. To get the template ID, use the Amazon EC2 DescribeLaunchTemplates API operation. New launch templates can be created using the Amazon EC2 CreateLaunchTemplate API.\nYou must specify either a template ID or a template name.\n\nLaunchTemplateName (string) --The name of the launch template. To get the template name, use the Amazon EC2 DescribeLaunchTemplates API operation. New launch templates can be created using the Amazon EC2 CreateLaunchTemplate API.\nYou must specify either a template ID or a template name.\n\nVersion (string) --The version number, $Latest , or $Default . To get the version number, use the Amazon EC2 DescribeLaunchTemplateVersions API operation. New launch template versions can be created using the Amazon EC2 CreateLaunchTemplateVersion API.\nIf the value is $Latest , Amazon EC2 Auto Scaling selects the latest version of the launch template when launching instances. If the value is $Default , Amazon EC2 Auto Scaling selects the default version of the launch template when launching instances. The default value is $Default .\n\n\n

    :type MixedInstancesPolicy: dict
    :param MixedInstancesPolicy: An embedded object that specifies a mixed instances policy. The required parameters must be specified. If optional parameters are unspecified, their default values are used.\nThe policy includes parameters that not only define the distribution of On-Demand Instances and Spot Instances, the maximum price to pay for Spot Instances, and how the Auto Scaling group allocates instance types to fulfill On-Demand and Spot capacity, but also the parameters that specify the instance configuration information\xe2\x80\x94the launch template and instance types.\nFor more information, see MixedInstancesPolicy in the Amazon EC2 Auto Scaling API Reference and Auto Scaling Groups with Multiple Instance Types and Purchase Options in the Amazon EC2 Auto Scaling User Guide .\nYou must specify one of the following parameters in your request: LaunchConfigurationName , LaunchTemplate , InstanceId , or MixedInstancesPolicy .\n\nLaunchTemplate (dict) --The launch template and instance types (overrides).\nThis parameter must be specified when creating a mixed instances policy.\n\nLaunchTemplateSpecification (dict) --The launch template to use. You must specify either the launch template ID or launch template name in the request.\n\nLaunchTemplateId (string) --The ID of the launch template. To get the template ID, use the Amazon EC2 DescribeLaunchTemplates API operation. New launch templates can be created using the Amazon EC2 CreateLaunchTemplate API.\nYou must specify either a template ID or a template name.\n\nLaunchTemplateName (string) --The name of the launch template. To get the template name, use the Amazon EC2 DescribeLaunchTemplates API operation. New launch templates can be created using the Amazon EC2 CreateLaunchTemplate API.\nYou must specify either a template ID or a template name.\n\nVersion (string) --The version number, $Latest , or $Default . To get the version number, use the Amazon EC2 DescribeLaunchTemplateVersions API operation. New launch template versions can be created using the Amazon EC2 CreateLaunchTemplateVersion API.\nIf the value is $Latest , Amazon EC2 Auto Scaling selects the latest version of the launch template when launching instances. If the value is $Default , Amazon EC2 Auto Scaling selects the default version of the launch template when launching instances. The default value is $Default .\n\n\n\nOverrides (list) --Any parameters that you specify override the same parameters in the launch template. Currently, the only supported override is instance type. You can specify between 1 and 20 instance types.\nIf not provided, Amazon EC2 Auto Scaling will use the instance type specified in the launch template to launch instances.\n\n(dict) --Describes an override for a launch template. Currently, the only supported override is instance type.\nThe maximum number of instance type overrides that can be associated with an Auto Scaling group is 20.\n\nInstanceType (string) --The instance type. You must use an instance type that is supported in your requested Region and Availability Zones.\nFor information about available instance types, see Available Instance Types in the Amazon Elastic Compute Cloud User Guide.\n\nWeightedCapacity (string) --The number of capacity units, which gives the instance type a proportional weight to other instance types. For example, larger instance types are generally weighted more than smaller instance types. These are the same units that you chose to set the desired capacity in terms of instances, or a performance attribute such as vCPUs, memory, or I/O.\nFor more information, see Instance Weighting for Amazon EC2 Auto Scaling in the Amazon EC2 Auto Scaling User Guide .\nValid Range: Minimum value of 1. Maximum value of 999.\n\n\n\n\n\n\n\nInstancesDistribution (dict) --The instances distribution to use.\nIf you leave this parameter unspecified, the value for each parameter in InstancesDistribution uses a default value.\n\nOnDemandAllocationStrategy (string) --Indicates how to allocate instance types to fulfill On-Demand capacity.\nThe only valid value is prioritized , which is also the default value. This strategy uses the order of instance type overrides for the LaunchTemplate to define the launch priority of each instance type. The first instance type in the array is prioritized higher than the last. If all your On-Demand capacity cannot be fulfilled using your highest priority instance, then the Auto Scaling groups launches the remaining capacity using the second priority instance type, and so on.\n\nOnDemandBaseCapacity (integer) --The minimum amount of the Auto Scaling group\'s capacity that must be fulfilled by On-Demand Instances. This base portion is provisioned first as your group scales.\nDefault if not set is 0. If you leave it set to 0, On-Demand Instances are launched as a percentage of the Auto Scaling group\'s desired capacity, per the OnDemandPercentageAboveBaseCapacity setting.\n\nNote\nAn update to this setting means a gradual replacement of instances to maintain the specified number of On-Demand Instances for your base capacity. When replacing instances, Amazon EC2 Auto Scaling launches new instances before terminating the old ones.\n\n\nOnDemandPercentageAboveBaseCapacity (integer) --Controls the percentages of On-Demand Instances and Spot Instances for your additional capacity beyond OnDemandBaseCapacity .\nDefault if not set is 100. If you leave it set to 100, the percentages are 100% for On-Demand Instances and 0% for Spot Instances.\n\nNote\nAn update to this setting means a gradual replacement of instances to maintain the percentage of On-Demand Instances for your additional capacity above the base capacity. When replacing instances, Amazon EC2 Auto Scaling launches new instances before terminating the old ones.\n\nValid Range: Minimum value of 0. Maximum value of 100.\n\nSpotAllocationStrategy (string) --Indicates how to allocate instances across Spot Instance pools.\nIf the allocation strategy is lowest-price , the Auto Scaling group launches instances using the Spot pools with the lowest price, and evenly allocates your instances across the number of Spot pools that you specify. If the allocation strategy is capacity-optimized , the Auto Scaling group launches instances using Spot pools that are optimally chosen based on the available Spot capacity.\nThe default Spot allocation strategy for calls that you make through the API, the AWS CLI, or the AWS SDKs is lowest-price . The default Spot allocation strategy for the AWS Management Console is capacity-optimized .\nValid values: lowest-price | capacity-optimized\n\nSpotInstancePools (integer) --The number of Spot Instance pools across which to allocate your Spot Instances. The Spot pools are determined from the different instance types in the Overrides array of LaunchTemplate . Default if not set is 2.\nUsed only when the Spot allocation strategy is lowest-price .\nValid Range: Minimum value of 1. Maximum value of 20.\n\nSpotMaxPrice (string) --The maximum price per unit hour that you are willing to pay for a Spot Instance. If you leave the value of this parameter blank (which is the default), the maximum Spot price is set at the On-Demand price.\nTo remove a value that you previously set, include the parameter but leave the value blank.\n\n\n\n\n

    :type InstanceId: string
    :param InstanceId: The ID of the instance used to create a launch configuration for the group. To get the instance ID, use the Amazon EC2 DescribeInstances API operation.\nWhen you specify an ID of an instance, Amazon EC2 Auto Scaling creates a new launch configuration and associates it with the group. This launch configuration derives its attributes from the specified instance, except for the block device mapping.\nYou must specify one of the following parameters in your request: LaunchConfigurationName , LaunchTemplate , InstanceId , or MixedInstancesPolicy .\n

    :type MinSize: integer
    :param MinSize: [REQUIRED]\nThe minimum size of the group.\n

    :type MaxSize: integer
    :param MaxSize: [REQUIRED]\nThe maximum size of the group.\n\nNote\nWith a mixed instances policy that uses instance weighting, Amazon EC2 Auto Scaling may need to go above MaxSize to meet your capacity requirements. In this event, Amazon EC2 Auto Scaling will never go above MaxSize by more than your maximum instance weight (weights that define how many capacity units each instance contributes to the capacity of the group).\n\n

    :type DesiredCapacity: integer
    :param DesiredCapacity: The desired capacity is the initial capacity of the Auto Scaling group at the time of its creation and the capacity it attempts to maintain. It can scale beyond this capacity if you configure automatic scaling.\nThis number must be greater than or equal to the minimum size of the group and less than or equal to the maximum size of the group. If you do not specify a desired capacity, the default is the minimum size of the group.\n

    :type DefaultCooldown: integer
    :param DefaultCooldown: The amount of time, in seconds, after a scaling activity completes before another scaling activity can start. The default value is 300 .\nFor more information, see Scaling Cooldowns in the Amazon EC2 Auto Scaling User Guide .\n

    :type AvailabilityZones: list
    :param AvailabilityZones: One or more Availability Zones for the group. This parameter is optional if you specify one or more subnets for VPCZoneIdentifier .\nConditional: If your account supports EC2-Classic and VPC, this parameter is required to launch instances into EC2-Classic.\n\n(string) --\n\n

    :type LoadBalancerNames: list
    :param LoadBalancerNames: A list of Classic Load Balancers associated with this Auto Scaling group. For Application Load Balancers and Network Load Balancers, specify a list of target groups using the TargetGroupARNs property instead.\nFor more information, see Using a Load Balancer with an Auto Scaling Group in the Amazon EC2 Auto Scaling User Guide .\n\n(string) --\n\n

    :type TargetGroupARNs: list
    :param TargetGroupARNs: The Amazon Resource Names (ARN) of the target groups to associate with the Auto Scaling group. Instances are registered as targets in a target group, and traffic is routed to the target group.\nFor more information, see Using a Load Balancer with an Auto Scaling Group in the Amazon EC2 Auto Scaling User Guide .\n\n(string) --\n\n

    :type HealthCheckType: string
    :param HealthCheckType: The service to use for the health checks. The valid values are EC2 and ELB . The default value is EC2 . If you configure an Auto Scaling group to use ELB health checks, it considers the instance unhealthy if it fails either the EC2 status checks or the load balancer health checks.\nFor more information, see Health Checks for Auto Scaling Instances in the Amazon EC2 Auto Scaling User Guide .\n

    :type HealthCheckGracePeriod: integer
    :param HealthCheckGracePeriod: The amount of time, in seconds, that Amazon EC2 Auto Scaling waits before checking the health status of an EC2 instance that has come into service. During this time, any health check failures for the instance are ignored. The default value is 0 .\nFor more information, see Health Check Grace Period in the Amazon EC2 Auto Scaling User Guide .\nConditional: This parameter is required if you are adding an ELB health check.\n

    :type PlacementGroup: string
    :param PlacementGroup: The name of the placement group into which to launch your instances, if any. A placement group is a logical grouping of instances within a single Availability Zone. You cannot specify multiple Availability Zones and a placement group. For more information, see Placement Groups in the Amazon EC2 User Guide for Linux Instances .

    :type VPCZoneIdentifier: string
    :param VPCZoneIdentifier: A comma-separated list of subnet IDs for your virtual private cloud (VPC).\nIf you specify VPCZoneIdentifier with AvailabilityZones , the subnets that you specify for this parameter must reside in those Availability Zones.\nConditional: If your account supports EC2-Classic and VPC, this parameter is required to launch instances into a VPC.\n

    :type TerminationPolicies: list
    :param TerminationPolicies: One or more termination policies used to select the instance to terminate. These policies are executed in the order that they are listed.\nFor more information, see Controlling Which Instances Auto Scaling Terminates During Scale In in the Amazon EC2 Auto Scaling User Guide .\n\n(string) --\n\n

    :type NewInstancesProtectedFromScaleIn: boolean
    :param NewInstancesProtectedFromScaleIn: Indicates whether newly launched instances are protected from termination by Amazon EC2 Auto Scaling when scaling in.\nFor more information about preventing instances from terminating on scale in, see Instance Protection in the Amazon EC2 Auto Scaling User Guide .\n

    :type LifecycleHookSpecificationList: list
    :param LifecycleHookSpecificationList: One or more lifecycle hooks.\n\n(dict) --Describes information used to specify a lifecycle hook for an Auto Scaling group.\nA lifecycle hook tells Amazon EC2 Auto Scaling to perform an action on an instance when the instance launches (before it is put into service) or as the instance terminates (before it is fully terminated).\nThis step is a part of the procedure for creating a lifecycle hook for an Auto Scaling group:\n\n(Optional) Create a Lambda function and a rule that allows CloudWatch Events to invoke your Lambda function when Amazon EC2 Auto Scaling launches or terminates instances.\n(Optional) Create a notification target and an IAM role. The target can be either an Amazon SQS queue or an Amazon SNS topic. The role allows Amazon EC2 Auto Scaling to publish lifecycle notifications to the target.\nCreate the lifecycle hook. Specify whether the hook is used when the instances launch or terminate.\nIf you need more time, record the lifecycle action heartbeat to keep the instance in a pending state.\nIf you finish before the timeout period ends, complete the lifecycle action.\n\nFor more information, see Amazon EC2 Auto Scaling Lifecycle Hooks in the Amazon EC2 Auto Scaling User Guide .\n\nLifecycleHookName (string) -- [REQUIRED]The name of the lifecycle hook.\n\nLifecycleTransition (string) -- [REQUIRED]The state of the EC2 instance to which you want to attach the lifecycle hook. The valid values are:\n\nautoscaling:EC2_INSTANCE_LAUNCHING\nautoscaling:EC2_INSTANCE_TERMINATING\n\n\nNotificationMetadata (string) --Additional information that you want to include any time Amazon EC2 Auto Scaling sends a message to the notification target.\n\nHeartbeatTimeout (integer) --The maximum time, in seconds, that can elapse before the lifecycle hook times out.\nIf the lifecycle hook times out, Amazon EC2 Auto Scaling performs the action that you specified in the DefaultResult parameter. You can prevent the lifecycle hook from timing out by calling RecordLifecycleActionHeartbeat .\n\nDefaultResult (string) --Defines the action the Auto Scaling group should take when the lifecycle hook timeout elapses or if an unexpected failure occurs. The valid values are CONTINUE and ABANDON . The default value is ABANDON .\n\nNotificationTargetARN (string) --The ARN of the target that Amazon EC2 Auto Scaling sends notifications to when an instance is in the transition state for the lifecycle hook. The notification target can be either an SQS queue or an SNS topic.\n\nRoleARN (string) --The ARN of the IAM role that allows the Auto Scaling group to publish to the specified notification target, for example, an Amazon SNS topic or an Amazon SQS queue.\n\n\n\n\n

    :type Tags: list
    :param Tags: One or more tags. You can tag your Auto Scaling group and propagate the tags to the Amazon EC2 instances it launches.\nTags are not propagated to Amazon EBS volumes. To add tags to Amazon EBS volumes, specify the tags in a launch template but use caution. If the launch template specifies an instance tag with a key that is also specified for the Auto Scaling group, Amazon EC2 Auto Scaling overrides the value of that instance tag with the value specified by the Auto Scaling group.\nFor more information, see Tagging Auto Scaling Groups and Instances in the Amazon EC2 Auto Scaling User Guide .\n\n(dict) --Describes a tag for an Auto Scaling group.\n\nResourceId (string) --The name of the group.\n\nResourceType (string) --The type of resource. The only supported value is auto-scaling-group .\n\nKey (string) -- [REQUIRED]The tag key.\n\nValue (string) --The tag value.\n\nPropagateAtLaunch (boolean) --Determines whether the tag is added to new instances as they are launched in the group.\n\n\n\n\n

    :type ServiceLinkedRoleARN: string
    :param ServiceLinkedRoleARN: The Amazon Resource Name (ARN) of the service-linked role that the Auto Scaling group uses to call other AWS services on your behalf. By default, Amazon EC2 Auto Scaling uses a service-linked role named AWSServiceRoleForAutoScaling, which it creates if it does not exist. For more information, see Service-Linked Roles in the Amazon EC2 Auto Scaling User Guide .

    :type MaxInstanceLifetime: integer
    :param MaxInstanceLifetime: The maximum amount of time, in seconds, that an instance can be in service. The default is null.\nThis parameter is optional, but if you specify a value for it, you must specify a value of at least 604,800 seconds (7 days). To clear a previously set value, specify a new value of 0.\nFor more information, see Replacing Auto Scaling Instances Based on Maximum Instance Lifetime in the Amazon EC2 Auto Scaling User Guide .\nValid Range: Minimum value of 0.\n

    :return: response = client.create_auto_scaling_group(
        AutoScalingGroupName='my-auto-scaling-group',
        LaunchConfigurationName='my-launch-config',
        MaxSize=3,
        MinSize=1,
        VPCZoneIdentifier='subnet-4176792c',
    )
    
    print(response)
    
    
    :returns: 
    AutoScaling.Client.exceptions.AlreadyExistsFault
    AutoScaling.Client.exceptions.LimitExceededFault
    AutoScaling.Client.exceptions.ResourceContentionFault
    AutoScaling.Client.exceptions.ServiceLinkedRoleFailure
    
    """
    pass

def create_launch_configuration(LaunchConfigurationName=None, ImageId=None, KeyName=None, SecurityGroups=None, ClassicLinkVPCId=None, ClassicLinkVPCSecurityGroups=None, UserData=None, InstanceId=None, InstanceType=None, KernelId=None, RamdiskId=None, BlockDeviceMappings=None, InstanceMonitoring=None, SpotPrice=None, IamInstanceProfile=None, EbsOptimized=None, AssociatePublicIpAddress=None, PlacementTenancy=None):
    """
    Creates a launch configuration.
    If you exceed your maximum limit of launch configurations, the call fails. To query this limit, call the  DescribeAccountLimits API. For information about updating this limit, see Amazon EC2 Auto Scaling Service Quotas in the Amazon EC2 Auto Scaling User Guide .
    For more information, see Launch Configurations in the Amazon EC2 Auto Scaling User Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example creates a launch configuration.
    Expected Output:
    
    :example: response = client.create_launch_configuration(
        LaunchConfigurationName='string',
        ImageId='string',
        KeyName='string',
        SecurityGroups=[
            'string',
        ],
        ClassicLinkVPCId='string',
        ClassicLinkVPCSecurityGroups=[
            'string',
        ],
        UserData='string',
        InstanceId='string',
        InstanceType='string',
        KernelId='string',
        RamdiskId='string',
        BlockDeviceMappings=[
            {
                'VirtualName': 'string',
                'DeviceName': 'string',
                'Ebs': {
                    'SnapshotId': 'string',
                    'VolumeSize': 123,
                    'VolumeType': 'string',
                    'DeleteOnTermination': True|False,
                    'Iops': 123,
                    'Encrypted': True|False
                },
                'NoDevice': True|False
            },
        ],
        InstanceMonitoring={
            'Enabled': True|False
        },
        SpotPrice='string',
        IamInstanceProfile='string',
        EbsOptimized=True|False,
        AssociatePublicIpAddress=True|False,
        PlacementTenancy='string'
    )
    
    
    :type LaunchConfigurationName: string
    :param LaunchConfigurationName: [REQUIRED]\nThe name of the launch configuration. This name must be unique per Region per account.\n

    :type ImageId: string
    :param ImageId: The ID of the Amazon Machine Image (AMI) that was assigned during registration. For more information, see Finding an AMI in the Amazon EC2 User Guide for Linux Instances .\nIf you do not specify InstanceId , you must specify ImageId .\n

    :type KeyName: string
    :param KeyName: The name of the key pair. For more information, see Amazon EC2 Key Pairs in the Amazon EC2 User Guide for Linux Instances .

    :type SecurityGroups: list
    :param SecurityGroups: A list that contains the security groups to assign to the instances in the Auto Scaling group.\n[EC2-VPC] Specify the security group IDs. For more information, see Security Groups for Your VPC in the Amazon Virtual Private Cloud User Guide .\n[EC2-Classic] Specify either the security group names or the security group IDs. For more information, see Amazon EC2 Security Groups in the Amazon EC2 User Guide for Linux Instances .\n\n(string) --\n\n

    :type ClassicLinkVPCId: string
    :param ClassicLinkVPCId: The ID of a ClassicLink-enabled VPC to link your EC2-Classic instances to. For more information, see ClassicLink in the Amazon EC2 User Guide for Linux Instances and Linking EC2-Classic Instances to a VPC in the Amazon EC2 Auto Scaling User Guide .\nThis parameter can only be used if you are launching EC2-Classic instances.\n

    :type ClassicLinkVPCSecurityGroups: list
    :param ClassicLinkVPCSecurityGroups: The IDs of one or more security groups for the specified ClassicLink-enabled VPC. For more information, see ClassicLink in the Amazon EC2 User Guide for Linux Instances and Linking EC2-Classic Instances to a VPC in the Amazon EC2 Auto Scaling User Guide .\nIf you specify the ClassicLinkVPCId parameter, you must specify this parameter.\n\n(string) --\n\n

    :type UserData: string
    :param UserData: The Base64-encoded user data to make available to the launched EC2 instances. For more information, see Instance Metadata and User Data in the Amazon EC2 User Guide for Linux Instances .\n\nThis value will be base64 encoded automatically. Do not base64 encode this value prior to performing the operation.\n

    :type InstanceId: string
    :param InstanceId: The ID of the instance to use to create the launch configuration. The new launch configuration derives attributes from the instance, except for the block device mapping.\nTo create a launch configuration with a block device mapping or override any other instance attributes, specify them as part of the same request.\nFor more information, see Create a Launch Configuration Using an EC2 Instance in the Amazon EC2 Auto Scaling User Guide .\nIf you do not specify InstanceId , you must specify both ImageId and InstanceType .\n

    :type InstanceType: string
    :param InstanceType: Specifies the instance type of the EC2 instance.\nFor information about available instance types, see Available Instance Types in the Amazon EC2 User Guide for Linux Instances.\nIf you do not specify InstanceId , you must specify InstanceType .\n

    :type KernelId: string
    :param KernelId: The ID of the kernel associated with the AMI.

    :type RamdiskId: string
    :param RamdiskId: The ID of the RAM disk to select.

    :type BlockDeviceMappings: list
    :param BlockDeviceMappings: A block device mapping, which specifies the block devices for the instance. You can specify virtual devices and EBS volumes. For more information, see Block Device Mapping in the Amazon EC2 User Guide for Linux Instances .\n\n(dict) --Describes a block device mapping.\n\nVirtualName (string) --The name of the virtual device (for example, ephemeral0 ).\nYou can specify either VirtualName or Ebs , but not both.\n\nDeviceName (string) -- [REQUIRED]The device name exposed to the EC2 instance (for example, /dev/sdh or xvdh ). For more information, see Device Naming on Linux Instances in the Amazon EC2 User Guide for Linux Instances .\n\nEbs (dict) --Parameters used to automatically set up EBS volumes when an instance is launched.\nYou can specify either VirtualName or Ebs , but not both.\n\nSnapshotId (string) --The snapshot ID of the volume to use.\nConditional: This parameter is optional if you specify a volume size. If you specify both SnapshotId and VolumeSize , VolumeSize must be equal or greater than the size of the snapshot.\n\nVolumeSize (integer) --The volume size, in Gibibytes (GiB).\nThis can be a number from 1-1,024 for standard , 4-16,384 for io1 , 1-16,384 for gp2 , and 500-16,384 for st1 and sc1 . If you specify a snapshot, the volume size must be equal to or larger than the snapshot size.\nDefault: If you create a volume from a snapshot and you don\'t specify a volume size, the default is the snapshot size.\n\nNote\nAt least one of VolumeSize or SnapshotId is required.\n\n\nVolumeType (string) --The volume type, which can be standard for Magnetic, io1 for Provisioned IOPS SSD, gp2 for General Purpose SSD, st1 for Throughput Optimized HDD, or sc1 for Cold HDD. For more information, see Amazon EBS Volume Types in the Amazon EC2 User Guide for Linux Instances .\nValid Values: standard | io1 | gp2 | st1 | sc1\n\nDeleteOnTermination (boolean) --Indicates whether the volume is deleted on instance termination. For Amazon EC2 Auto Scaling, the default value is true .\n\nIops (integer) --The number of I/O operations per second (IOPS) to provision for the volume. The maximum ratio of IOPS to volume size (in GiB) is 50:1. For more information, see Amazon EBS Volume Types in the Amazon EC2 User Guide for Linux Instances .\nConditional: This parameter is required when the volume type is io1 . (Not used with standard , gp2 , st1 , or sc1 volumes.)\n\nEncrypted (boolean) --Specifies whether the volume should be encrypted. Encrypted EBS volumes can only be attached to instances that support Amazon EBS encryption. For more information, see Supported Instance Types . If your AMI uses encrypted volumes, you can also only launch it on supported instance types.\n\nNote\nIf you are creating a volume from a snapshot, you cannot specify an encryption value. Volumes that are created from encrypted snapshots are automatically encrypted, and volumes that are created from unencrypted snapshots are automatically unencrypted. By default, encrypted snapshots use the AWS managed CMK that is used for EBS encryption, but you can specify a custom CMK when you create the snapshot. The ability to encrypt a snapshot during copying also allows you to apply a new CMK to an already-encrypted snapshot. Volumes restored from the resulting copy are only accessible using the new CMK.\nEnabling encryption by default results in all EBS volumes being encrypted with the AWS managed CMK or a customer managed CMK, whether or not the snapshot was encrypted.\n\nFor more information, see Using Encryption with EBS-Backed AMIs in the Amazon EC2 User Guide for Linux Instances and Required CMK Key Policy for Use with Encrypted Volumes in the Amazon EC2 Auto Scaling User Guide .\n\n\n\nNoDevice (boolean) --Setting this value to true suppresses the specified device included in the block device mapping of the AMI.\nIf NoDevice is true for the root device, instances might fail the EC2 health check. In that case, Amazon EC2 Auto Scaling launches replacement instances.\nIf you specify NoDevice , you cannot specify Ebs .\n\n\n\n\n

    :type InstanceMonitoring: dict
    :param InstanceMonitoring: Controls whether instances in this group are launched with detailed (true ) or basic (false ) monitoring.\nThe default value is true (enabled).\n\nWarning\nWhen detailed monitoring is enabled, Amazon CloudWatch generates metrics every minute and your account is charged a fee. When you disable detailed monitoring, CloudWatch generates metrics every 5 minutes. For more information, see Configure Monitoring for Auto Scaling Instances in the Amazon EC2 Auto Scaling User Guide .\n\n\nEnabled (boolean) --If true , detailed monitoring is enabled. Otherwise, basic monitoring is enabled.\n\n\n

    :type SpotPrice: string
    :param SpotPrice: The maximum hourly price to be paid for any Spot Instance launched to fulfill the request. Spot Instances are launched when the price you specify exceeds the current Spot price. For more information, see Launching Spot Instances in Your Auto Scaling Group in the Amazon EC2 Auto Scaling User Guide .\n\nNote\nWhen you change your maximum price by creating a new launch configuration, running instances will continue to run as long as the maximum price for those running instances is higher than the current Spot price.\n\n

    :type IamInstanceProfile: string
    :param IamInstanceProfile: The name or the Amazon Resource Name (ARN) of the instance profile associated with the IAM role for the instance. The instance profile contains the IAM role.\nFor more information, see IAM Role for Applications That Run on Amazon EC2 Instances in the Amazon EC2 Auto Scaling User Guide .\n

    :type EbsOptimized: boolean
    :param EbsOptimized: Specifies whether the launch configuration is optimized for EBS I/O (true ) or not (false ). The optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal I/O performance. This optimization is not available with all instance types. Additional fees are incurred when you enable EBS optimization for an instance type that is not EBS-optimized by default. For more information, see Amazon EBS-Optimized Instances in the Amazon EC2 User Guide for Linux Instances .\nThe default value is false .\n

    :type AssociatePublicIpAddress: boolean
    :param AssociatePublicIpAddress: For Auto Scaling groups that are running in a virtual private cloud (VPC), specifies whether to assign a public IP address to the group\'s instances. If you specify true , each instance in the Auto Scaling group receives a unique public IP address. For more information, see Launching Auto Scaling Instances in a VPC in the Amazon EC2 Auto Scaling User Guide .\nIf you specify this parameter, you must specify at least one subnet for VPCZoneIdentifier when you create your group.\n\nNote\nIf the instance is launched into a default subnet, the default is to assign a public IP address, unless you disabled the option to assign a public IP address on the subnet. If the instance is launched into a nondefault subnet, the default is not to assign a public IP address, unless you enabled the option to assign a public IP address on the subnet.\n\n

    :type PlacementTenancy: string
    :param PlacementTenancy: The tenancy of the instance. An instance with dedicated tenancy runs on isolated, single-tenant hardware and can only be launched into a VPC.\nTo launch dedicated instances into a shared tenancy VPC (a VPC with the instance placement tenancy attribute set to default ), you must set the value of this parameter to dedicated .\nIf you specify PlacementTenancy , you must specify at least one subnet for VPCZoneIdentifier when you create your group.\nFor more information, see Instance Placement Tenancy in the Amazon EC2 Auto Scaling User Guide .\nValid Values: default | dedicated\n

    :return: response = client.create_launch_configuration(
        IamInstanceProfile='my-iam-role',
        ImageId='ami-12345678',
        InstanceType='m3.medium',
        LaunchConfigurationName='my-launch-config',
        SecurityGroups=[
            'sg-eb2af88e',
        ],
    )
    
    print(response)
    
    
    :returns: 
    AutoScaling.Client.exceptions.AlreadyExistsFault
    AutoScaling.Client.exceptions.LimitExceededFault
    AutoScaling.Client.exceptions.ResourceContentionFault
    
    """
    pass

def create_or_update_tags(Tags=None):
    """
    Creates or updates tags for the specified Auto Scaling group.
    When you specify a tag with a key that already exists, the operation overwrites the previous tag definition, and you do not get an error message.
    For more information, see Tagging Auto Scaling Groups and Instances in the Amazon EC2 Auto Scaling User Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example adds two tags to the specified Auto Scaling group.
    Expected Output:
    
    :example: response = client.create_or_update_tags(
        Tags=[
            {
                'ResourceId': 'string',
                'ResourceType': 'string',
                'Key': 'string',
                'Value': 'string',
                'PropagateAtLaunch': True|False
            },
        ]
    )
    
    
    :type Tags: list
    :param Tags: [REQUIRED]\nOne or more tags.\n\n(dict) --Describes a tag for an Auto Scaling group.\n\nResourceId (string) --The name of the group.\n\nResourceType (string) --The type of resource. The only supported value is auto-scaling-group .\n\nKey (string) -- [REQUIRED]The tag key.\n\nValue (string) --The tag value.\n\nPropagateAtLaunch (boolean) --Determines whether the tag is added to new instances as they are launched in the group.\n\n\n\n\n

    :return: response = client.create_or_update_tags(
        Tags=[
            {
                'Key': 'Role',
                'PropagateAtLaunch': True,
                'ResourceId': 'my-auto-scaling-group',
                'ResourceType': 'auto-scaling-group',
                'Value': 'WebServer',
            },
            {
                'Key': 'Dept',
                'PropagateAtLaunch': True,
                'ResourceId': 'my-auto-scaling-group',
                'ResourceType': 'auto-scaling-group',
                'Value': 'Research',
            },
        ],
    )
    
    print(response)
    
    
    """
    pass

def delete_auto_scaling_group(AutoScalingGroupName=None, ForceDelete=None):
    """
    Deletes the specified Auto Scaling group.
    If the group has instances or scaling activities in progress, you must specify the option to force the deletion in order for it to succeed.
    If the group has policies, deleting the group deletes the policies, the underlying alarm actions, and any alarm that no longer has an associated action.
    To remove instances from the Auto Scaling group before deleting it, call the  DetachInstances API with the list of instances and the option to decrement the desired capacity. This ensures that Amazon EC2 Auto Scaling does not launch replacement instances.
    To terminate all instances before deleting the Auto Scaling group, call the  UpdateAutoScalingGroup API and set the minimum size and desired capacity of the Auto Scaling group to zero.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example deletes the specified Auto Scaling group.
    Expected Output:
    This example deletes the specified Auto Scaling group and all its instances.
    Expected Output:
    
    :example: response = client.delete_auto_scaling_group(
        AutoScalingGroupName='string',
        ForceDelete=True|False
    )
    
    
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: [REQUIRED]\nThe name of the Auto Scaling group.\n

    :type ForceDelete: boolean
    :param ForceDelete: Specifies that the group is to be deleted along with all instances associated with the group, without waiting for all instances to be terminated. This parameter also deletes any lifecycle actions associated with the group.

    :return: response = client.delete_auto_scaling_group(
        AutoScalingGroupName='my-auto-scaling-group',
    )
    
    print(response)
    
    
    :returns: 
    AutoScaling.Client.exceptions.ScalingActivityInProgressFault
    AutoScaling.Client.exceptions.ResourceInUseFault
    AutoScaling.Client.exceptions.ResourceContentionFault
    
    """
    pass

def delete_launch_configuration(LaunchConfigurationName=None):
    """
    Deletes the specified launch configuration.
    The launch configuration must not be attached to an Auto Scaling group. When this call completes, the launch configuration is no longer available for use.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example deletes the specified launch configuration.
    Expected Output:
    
    :example: response = client.delete_launch_configuration(
        LaunchConfigurationName='string'
    )
    
    
    :type LaunchConfigurationName: string
    :param LaunchConfigurationName: [REQUIRED]\nThe name of the launch configuration.\n

    :return: response = client.delete_launch_configuration(
        LaunchConfigurationName='my-launch-config',
    )
    
    print(response)
    
    
    """
    pass

def delete_lifecycle_hook(LifecycleHookName=None, AutoScalingGroupName=None):
    """
    Deletes the specified lifecycle hook.
    If there are any outstanding lifecycle actions, they are completed first (ABANDON for launching instances, CONTINUE for terminating instances).
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example deletes the specified lifecycle hook.
    Expected Output:
    
    :example: response = client.delete_lifecycle_hook(
        LifecycleHookName='string',
        AutoScalingGroupName='string'
    )
    
    
    :type LifecycleHookName: string
    :param LifecycleHookName: [REQUIRED]\nThe name of the lifecycle hook.\n

    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: [REQUIRED]\nThe name of the Auto Scaling group.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

AutoScaling.Client.exceptions.ResourceContentionFault

Examples
This example deletes the specified lifecycle hook.
response = client.delete_lifecycle_hook(
    AutoScalingGroupName='my-auto-scaling-group',
    LifecycleHookName='my-lifecycle-hook',
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

def delete_notification_configuration(AutoScalingGroupName=None, TopicARN=None):
    """
    Deletes the specified notification.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example deletes the specified notification from the specified Auto Scaling group.
    Expected Output:
    
    :example: response = client.delete_notification_configuration(
        AutoScalingGroupName='string',
        TopicARN='string'
    )
    
    
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: [REQUIRED]\nThe name of the Auto Scaling group.\n

    :type TopicARN: string
    :param TopicARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the Amazon Simple Notification Service (Amazon SNS) topic.\n

    :return: response = client.delete_notification_configuration(
        AutoScalingGroupName='my-auto-scaling-group',
        TopicARN='arn:aws:sns:us-west-2:123456789012:my-sns-topic',
    )
    
    print(response)
    
    
    :returns: 
    AutoScaling.Client.exceptions.ResourceContentionFault
    
    """
    pass

def delete_policy(AutoScalingGroupName=None, PolicyName=None):
    """
    Deletes the specified scaling policy.
    Deleting either a step scaling policy or a simple scaling policy deletes the underlying alarm action, but does not delete the alarm, even if it no longer has an associated action.
    For more information, see Deleting a Scaling Policy in the Amazon EC2 Auto Scaling User Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example deletes the specified Auto Scaling policy.
    Expected Output:
    
    :example: response = client.delete_policy(
        AutoScalingGroupName='string',
        PolicyName='string'
    )
    
    
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: The name of the Auto Scaling group.

    :type PolicyName: string
    :param PolicyName: [REQUIRED]\nThe name or Amazon Resource Name (ARN) of the policy.\n

    :return: response = client.delete_policy(
        AutoScalingGroupName='my-auto-scaling-group',
        PolicyName='ScaleIn',
    )
    
    print(response)
    
    
    :returns: 
    AutoScaling.Client.exceptions.ResourceContentionFault
    AutoScaling.Client.exceptions.ServiceLinkedRoleFailure
    
    """
    pass

def delete_scheduled_action(AutoScalingGroupName=None, ScheduledActionName=None):
    """
    Deletes the specified scheduled action.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example deletes the specified scheduled action from the specified Auto Scaling group.
    Expected Output:
    
    :example: response = client.delete_scheduled_action(
        AutoScalingGroupName='string',
        ScheduledActionName='string'
    )
    
    
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: [REQUIRED]\nThe name of the Auto Scaling group.\n

    :type ScheduledActionName: string
    :param ScheduledActionName: [REQUIRED]\nThe name of the action to delete.\n

    :return: response = client.delete_scheduled_action(
        AutoScalingGroupName='my-auto-scaling-group',
        ScheduledActionName='my-scheduled-action',
    )
    
    print(response)
    
    
    :returns: 
    AutoScaling.Client.exceptions.ResourceContentionFault
    
    """
    pass

def delete_tags(Tags=None):
    """
    Deletes the specified tags.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example deletes the specified tag from the specified Auto Scaling group.
    Expected Output:
    
    :example: response = client.delete_tags(
        Tags=[
            {
                'ResourceId': 'string',
                'ResourceType': 'string',
                'Key': 'string',
                'Value': 'string',
                'PropagateAtLaunch': True|False
            },
        ]
    )
    
    
    :type Tags: list
    :param Tags: [REQUIRED]\nOne or more tags.\n\n(dict) --Describes a tag for an Auto Scaling group.\n\nResourceId (string) --The name of the group.\n\nResourceType (string) --The type of resource. The only supported value is auto-scaling-group .\n\nKey (string) -- [REQUIRED]The tag key.\n\nValue (string) --The tag value.\n\nPropagateAtLaunch (boolean) --Determines whether the tag is added to new instances as they are launched in the group.\n\n\n\n\n

    :return: response = client.delete_tags(
        Tags=[
            {
                'Key': 'Dept',
                'ResourceId': 'my-auto-scaling-group',
                'ResourceType': 'auto-scaling-group',
                'Value': 'Research',
            },
        ],
    )
    
    print(response)
    
    
    """
    pass

def describe_account_limits():
    """
    Describes the current Amazon EC2 Auto Scaling resource quotas for your AWS account.
    For information about requesting an increase, see Amazon EC2 Auto Scaling Service Quotas in the Amazon EC2 Auto Scaling User Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example describes the Auto Scaling limits for your AWS account.
    Expected Output:
    
    :example: response = client.describe_account_limits()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'MaxNumberOfAutoScalingGroups': 123,
    'MaxNumberOfLaunchConfigurations': 123,
    'NumberOfAutoScalingGroups': 123,
    'NumberOfLaunchConfigurations': 123
}


Response Structure

(dict) --
MaxNumberOfAutoScalingGroups (integer) --The maximum number of groups allowed for your AWS account. The default is 200 groups per AWS Region.

MaxNumberOfLaunchConfigurations (integer) --The maximum number of launch configurations allowed for your AWS account. The default is 200 launch configurations per AWS Region.

NumberOfAutoScalingGroups (integer) --The current number of groups for your AWS account.

NumberOfLaunchConfigurations (integer) --The current number of launch configurations for your AWS account.






Exceptions

AutoScaling.Client.exceptions.ResourceContentionFault

Examples
This example describes the Auto Scaling limits for your AWS account.
response = client.describe_account_limits(
)

print(response)


Expected Output:
{
    'MaxNumberOfAutoScalingGroups': 20,
    'MaxNumberOfLaunchConfigurations': 100,
    'NumberOfAutoScalingGroups': 3,
    'NumberOfLaunchConfigurations': 5,
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'MaxNumberOfAutoScalingGroups': 123,
        'MaxNumberOfLaunchConfigurations': 123,
        'NumberOfAutoScalingGroups': 123,
        'NumberOfLaunchConfigurations': 123
    }
    
    
    """
    pass

def describe_adjustment_types():
    """
    Describes the available adjustment types for Amazon EC2 Auto Scaling scaling policies. These settings apply to step scaling policies and simple scaling policies; they do not apply to target tracking scaling policies.
    The following adjustment types are supported:
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example describes the available adjustment types.
    Expected Output:
    
    :example: response = client.describe_adjustment_types()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'AdjustmentTypes': [
        {
            'AdjustmentType': 'string'
        },
    ]
}


Response Structure

(dict) --
AdjustmentTypes (list) --The policy adjustment types.

(dict) --Describes a policy adjustment type.

AdjustmentType (string) --The policy adjustment type. The valid values are ChangeInCapacity , ExactCapacity , and PercentChangeInCapacity .










Exceptions

AutoScaling.Client.exceptions.ResourceContentionFault

Examples
This example describes the available adjustment types.
response = client.describe_adjustment_types(
)

print(response)


Expected Output:
{
    'AdjustmentTypes': [
        {
            'AdjustmentType': 'ChangeInCapacity',
        },
        {
            'AdjustmentType': 'ExactCapcity',
        },
        {
            'AdjustmentType': 'PercentChangeInCapacity',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'AdjustmentTypes': [
            {
                'AdjustmentType': 'string'
            },
        ]
    }
    
    
    :returns: 
    AutoScaling.Client.exceptions.ResourceContentionFault
    
    """
    pass

def describe_auto_scaling_groups(AutoScalingGroupNames=None, NextToken=None, MaxRecords=None):
    """
    Describes one or more Auto Scaling groups.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example describes the specified Auto Scaling group.
    Expected Output:
    
    :example: response = client.describe_auto_scaling_groups(
        AutoScalingGroupNames=[
            'string',
        ],
        NextToken='string',
        MaxRecords=123
    )
    
    
    :type AutoScalingGroupNames: list
    :param AutoScalingGroupNames: The names of the Auto Scaling groups. Each name can be a maximum of 1600 characters. By default, you can only specify up to 50 names. You can optionally increase this limit using the MaxRecords parameter.\nIf you omit this parameter, all Auto Scaling groups are described.\n\n(string) --\n\n

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of items to return with this call. The default value is 50 and the maximum value is 100 .

    :rtype: dict

ReturnsResponse Syntax
{
    'AutoScalingGroups': [
        {
            'AutoScalingGroupName': 'string',
            'AutoScalingGroupARN': 'string',
            'LaunchConfigurationName': 'string',
            'LaunchTemplate': {
                'LaunchTemplateId': 'string',
                'LaunchTemplateName': 'string',
                'Version': 'string'
            },
            'MixedInstancesPolicy': {
                'LaunchTemplate': {
                    'LaunchTemplateSpecification': {
                        'LaunchTemplateId': 'string',
                        'LaunchTemplateName': 'string',
                        'Version': 'string'
                    },
                    'Overrides': [
                        {
                            'InstanceType': 'string',
                            'WeightedCapacity': 'string'
                        },
                    ]
                },
                'InstancesDistribution': {
                    'OnDemandAllocationStrategy': 'string',
                    'OnDemandBaseCapacity': 123,
                    'OnDemandPercentageAboveBaseCapacity': 123,
                    'SpotAllocationStrategy': 'string',
                    'SpotInstancePools': 123,
                    'SpotMaxPrice': 'string'
                }
            },
            'MinSize': 123,
            'MaxSize': 123,
            'DesiredCapacity': 123,
            'DefaultCooldown': 123,
            'AvailabilityZones': [
                'string',
            ],
            'LoadBalancerNames': [
                'string',
            ],
            'TargetGroupARNs': [
                'string',
            ],
            'HealthCheckType': 'string',
            'HealthCheckGracePeriod': 123,
            'Instances': [
                {
                    'InstanceId': 'string',
                    'InstanceType': 'string',
                    'AvailabilityZone': 'string',
                    'LifecycleState': 'Pending'|'Pending:Wait'|'Pending:Proceed'|'Quarantined'|'InService'|'Terminating'|'Terminating:Wait'|'Terminating:Proceed'|'Terminated'|'Detaching'|'Detached'|'EnteringStandby'|'Standby',
                    'HealthStatus': 'string',
                    'LaunchConfigurationName': 'string',
                    'LaunchTemplate': {
                        'LaunchTemplateId': 'string',
                        'LaunchTemplateName': 'string',
                        'Version': 'string'
                    },
                    'ProtectedFromScaleIn': True|False,
                    'WeightedCapacity': 'string'
                },
            ],
            'CreatedTime': datetime(2015, 1, 1),
            'SuspendedProcesses': [
                {
                    'ProcessName': 'string',
                    'SuspensionReason': 'string'
                },
            ],
            'PlacementGroup': 'string',
            'VPCZoneIdentifier': 'string',
            'EnabledMetrics': [
                {
                    'Metric': 'string',
                    'Granularity': 'string'
                },
            ],
            'Status': 'string',
            'Tags': [
                {
                    'ResourceId': 'string',
                    'ResourceType': 'string',
                    'Key': 'string',
                    'Value': 'string',
                    'PropagateAtLaunch': True|False
                },
            ],
            'TerminationPolicies': [
                'string',
            ],
            'NewInstancesProtectedFromScaleIn': True|False,
            'ServiceLinkedRoleARN': 'string',
            'MaxInstanceLifetime': 123
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

AutoScalingGroups (list) --
The groups.

(dict) --
Describes an Auto Scaling group.

AutoScalingGroupName (string) --
The name of the Auto Scaling group.

AutoScalingGroupARN (string) --
The Amazon Resource Name (ARN) of the Auto Scaling group.

LaunchConfigurationName (string) --
The name of the associated launch configuration.

LaunchTemplate (dict) --
The launch template for the group.

LaunchTemplateId (string) --
The ID of the launch template. To get the template ID, use the Amazon EC2 DescribeLaunchTemplates API operation. New launch templates can be created using the Amazon EC2 CreateLaunchTemplate API.
You must specify either a template ID or a template name.

LaunchTemplateName (string) --
The name of the launch template. To get the template name, use the Amazon EC2 DescribeLaunchTemplates API operation. New launch templates can be created using the Amazon EC2 CreateLaunchTemplate API.
You must specify either a template ID or a template name.

Version (string) --
The version number, $Latest , or $Default . To get the version number, use the Amazon EC2 DescribeLaunchTemplateVersions API operation. New launch template versions can be created using the Amazon EC2 CreateLaunchTemplateVersion API.
If the value is $Latest , Amazon EC2 Auto Scaling selects the latest version of the launch template when launching instances. If the value is $Default , Amazon EC2 Auto Scaling selects the default version of the launch template when launching instances. The default value is $Default .



MixedInstancesPolicy (dict) --
The mixed instances policy for the group.

LaunchTemplate (dict) --
The launch template and instance types (overrides).
This parameter must be specified when creating a mixed instances policy.

LaunchTemplateSpecification (dict) --
The launch template to use. You must specify either the launch template ID or launch template name in the request.

LaunchTemplateId (string) --
The ID of the launch template. To get the template ID, use the Amazon EC2 DescribeLaunchTemplates API operation. New launch templates can be created using the Amazon EC2 CreateLaunchTemplate API.
You must specify either a template ID or a template name.

LaunchTemplateName (string) --
The name of the launch template. To get the template name, use the Amazon EC2 DescribeLaunchTemplates API operation. New launch templates can be created using the Amazon EC2 CreateLaunchTemplate API.
You must specify either a template ID or a template name.

Version (string) --
The version number, $Latest , or $Default . To get the version number, use the Amazon EC2 DescribeLaunchTemplateVersions API operation. New launch template versions can be created using the Amazon EC2 CreateLaunchTemplateVersion API.
If the value is $Latest , Amazon EC2 Auto Scaling selects the latest version of the launch template when launching instances. If the value is $Default , Amazon EC2 Auto Scaling selects the default version of the launch template when launching instances. The default value is $Default .



Overrides (list) --
Any parameters that you specify override the same parameters in the launch template. Currently, the only supported override is instance type. You can specify between 1 and 20 instance types.
If not provided, Amazon EC2 Auto Scaling will use the instance type specified in the launch template to launch instances.

(dict) --
Describes an override for a launch template. Currently, the only supported override is instance type.
The maximum number of instance type overrides that can be associated with an Auto Scaling group is 20.

InstanceType (string) --
The instance type. You must use an instance type that is supported in your requested Region and Availability Zones.
For information about available instance types, see Available Instance Types in the Amazon Elastic Compute Cloud User Guide.

WeightedCapacity (string) --
The number of capacity units, which gives the instance type a proportional weight to other instance types. For example, larger instance types are generally weighted more than smaller instance types. These are the same units that you chose to set the desired capacity in terms of instances, or a performance attribute such as vCPUs, memory, or I/O.
For more information, see Instance Weighting for Amazon EC2 Auto Scaling in the Amazon EC2 Auto Scaling User Guide .
Valid Range: Minimum value of 1. Maximum value of 999.







InstancesDistribution (dict) --
The instances distribution to use.
If you leave this parameter unspecified, the value for each parameter in InstancesDistribution uses a default value.

OnDemandAllocationStrategy (string) --
Indicates how to allocate instance types to fulfill On-Demand capacity.
The only valid value is prioritized , which is also the default value. This strategy uses the order of instance type overrides for the  LaunchTemplate to define the launch priority of each instance type. The first instance type in the array is prioritized higher than the last. If all your On-Demand capacity cannot be fulfilled using your highest priority instance, then the Auto Scaling groups launches the remaining capacity using the second priority instance type, and so on.

OnDemandBaseCapacity (integer) --
The minimum amount of the Auto Scaling group\'s capacity that must be fulfilled by On-Demand Instances. This base portion is provisioned first as your group scales.
Default if not set is 0. If you leave it set to 0, On-Demand Instances are launched as a percentage of the Auto Scaling group\'s desired capacity, per the OnDemandPercentageAboveBaseCapacity setting.

Note
An update to this setting means a gradual replacement of instances to maintain the specified number of On-Demand Instances for your base capacity. When replacing instances, Amazon EC2 Auto Scaling launches new instances before terminating the old ones.


OnDemandPercentageAboveBaseCapacity (integer) --
Controls the percentages of On-Demand Instances and Spot Instances for your additional capacity beyond OnDemandBaseCapacity .
Default if not set is 100. If you leave it set to 100, the percentages are 100% for On-Demand Instances and 0% for Spot Instances.

Note
An update to this setting means a gradual replacement of instances to maintain the percentage of On-Demand Instances for your additional capacity above the base capacity. When replacing instances, Amazon EC2 Auto Scaling launches new instances before terminating the old ones.

Valid Range: Minimum value of 0. Maximum value of 100.

SpotAllocationStrategy (string) --
Indicates how to allocate instances across Spot Instance pools.
If the allocation strategy is lowest-price , the Auto Scaling group launches instances using the Spot pools with the lowest price, and evenly allocates your instances across the number of Spot pools that you specify. If the allocation strategy is capacity-optimized , the Auto Scaling group launches instances using Spot pools that are optimally chosen based on the available Spot capacity.
The default Spot allocation strategy for calls that you make through the API, the AWS CLI, or the AWS SDKs is lowest-price . The default Spot allocation strategy for the AWS Management Console is capacity-optimized .
Valid values: lowest-price | capacity-optimized

SpotInstancePools (integer) --
The number of Spot Instance pools across which to allocate your Spot Instances. The Spot pools are determined from the different instance types in the Overrides array of  LaunchTemplate . Default if not set is 2.
Used only when the Spot allocation strategy is lowest-price .
Valid Range: Minimum value of 1. Maximum value of 20.

SpotMaxPrice (string) --
The maximum price per unit hour that you are willing to pay for a Spot Instance. If you leave the value of this parameter blank (which is the default), the maximum Spot price is set at the On-Demand price.
To remove a value that you previously set, include the parameter but leave the value blank.





MinSize (integer) --
The minimum size of the group.

MaxSize (integer) --
The maximum size of the group.

DesiredCapacity (integer) --
The desired size of the group.

DefaultCooldown (integer) --
The amount of time, in seconds, after a scaling activity completes before another scaling activity can start.

AvailabilityZones (list) --
One or more Availability Zones for the group.

(string) --


LoadBalancerNames (list) --
One or more load balancers associated with the group.

(string) --


TargetGroupARNs (list) --
The Amazon Resource Names (ARN) of the target groups for your load balancer.

(string) --


HealthCheckType (string) --
The service to use for the health checks. The valid values are EC2 and ELB . If you configure an Auto Scaling group to use ELB health checks, it considers the instance unhealthy if it fails either the EC2 status checks or the load balancer health checks.

HealthCheckGracePeriod (integer) --
The amount of time, in seconds, that Amazon EC2 Auto Scaling waits before checking the health status of an EC2 instance that has come into service.

Instances (list) --
The EC2 instances associated with the group.

(dict) --
Describes an EC2 instance.

InstanceId (string) --
The ID of the instance.

InstanceType (string) --
The instance type of the EC2 instance.

AvailabilityZone (string) --
The Availability Zone in which the instance is running.

LifecycleState (string) --
A description of the current lifecycle state. The Quarantined state is not used.

HealthStatus (string) --
The last reported health status of the instance. "Healthy" means that the instance is healthy and should remain in service. "Unhealthy" means that the instance is unhealthy and that Amazon EC2 Auto Scaling should terminate and replace it.

LaunchConfigurationName (string) --
The launch configuration associated with the instance.

LaunchTemplate (dict) --
The launch template for the instance.

LaunchTemplateId (string) --
The ID of the launch template. To get the template ID, use the Amazon EC2 DescribeLaunchTemplates API operation. New launch templates can be created using the Amazon EC2 CreateLaunchTemplate API.
You must specify either a template ID or a template name.

LaunchTemplateName (string) --
The name of the launch template. To get the template name, use the Amazon EC2 DescribeLaunchTemplates API operation. New launch templates can be created using the Amazon EC2 CreateLaunchTemplate API.
You must specify either a template ID or a template name.

Version (string) --
The version number, $Latest , or $Default . To get the version number, use the Amazon EC2 DescribeLaunchTemplateVersions API operation. New launch template versions can be created using the Amazon EC2 CreateLaunchTemplateVersion API.
If the value is $Latest , Amazon EC2 Auto Scaling selects the latest version of the launch template when launching instances. If the value is $Default , Amazon EC2 Auto Scaling selects the default version of the launch template when launching instances. The default value is $Default .



ProtectedFromScaleIn (boolean) --
Indicates whether the instance is protected from termination by Amazon EC2 Auto Scaling when scaling in.

WeightedCapacity (string) --
The number of capacity units contributed by the instance based on its instance type.
Valid Range: Minimum value of 1. Maximum value of 999.





CreatedTime (datetime) --
The date and time the group was created.

SuspendedProcesses (list) --
The suspended processes associated with the group.

(dict) --
Describes an automatic scaling process that has been suspended.
For more information, see Scaling Processes in the Amazon EC2 Auto Scaling User Guide .

ProcessName (string) --
The name of the suspended process.

SuspensionReason (string) --
The reason that the process was suspended.





PlacementGroup (string) --
The name of the placement group into which to launch your instances, if any.

VPCZoneIdentifier (string) --
One or more subnet IDs, if applicable, separated by commas.

EnabledMetrics (list) --
The metrics enabled for the group.

(dict) --
Describes an enabled metric.

Metric (string) --
One of the following metrics:

GroupMinSize
GroupMaxSize
GroupDesiredCapacity
GroupInServiceInstances
GroupPendingInstances
GroupStandbyInstances
GroupTerminatingInstances
GroupTotalInstances
GroupInServiceCapacity
GroupPendingCapacity
GroupStandbyCapacity
GroupTerminatingCapacity
GroupTotalCapacity


Granularity (string) --
The granularity of the metric. The only valid value is 1Minute .





Status (string) --
The current state of the group when the  DeleteAutoScalingGroup operation is in progress.

Tags (list) --
The tags for the group.

(dict) --
Describes a tag for an Auto Scaling group.

ResourceId (string) --
The name of the group.

ResourceType (string) --
The type of resource. The only supported value is auto-scaling-group .

Key (string) --
The tag key.

Value (string) --
The tag value.

PropagateAtLaunch (boolean) --
Determines whether the tag is added to new instances as they are launched in the group.





TerminationPolicies (list) --
The termination policies for the group.

(string) --


NewInstancesProtectedFromScaleIn (boolean) --
Indicates whether newly launched instances are protected from termination by Amazon EC2 Auto Scaling when scaling in.

ServiceLinkedRoleARN (string) --
The Amazon Resource Name (ARN) of the service-linked role that the Auto Scaling group uses to call other AWS services on your behalf.

MaxInstanceLifetime (integer) --
The maximum amount of time, in seconds, that an instance can be in service.
Valid Range: Minimum value of 0.





NextToken (string) --
A string that indicates that the response contains more items than can be returned in a single response. To receive additional items, specify this string for the NextToken value when requesting the next set of items. This value is null when there are no more items to return.







Exceptions

AutoScaling.Client.exceptions.InvalidNextToken
AutoScaling.Client.exceptions.ResourceContentionFault

Examples
This example describes the specified Auto Scaling group.
response = client.describe_auto_scaling_groups(
    AutoScalingGroupNames=[
        'my-auto-scaling-group',
    ],
)

print(response)


Expected Output:
{
    'AutoScalingGroups': [
        {
            'AutoScalingGroupARN': 'arn:aws:autoscaling:us-west-2:123456789012:autoScalingGroup:930d940e-891e-4781-a11a-7b0acd480f03:autoScalingGroupName/my-auto-scaling-group',
            'AutoScalingGroupName': 'my-auto-scaling-group',
            'AvailabilityZones': [
                'us-west-2c',
            ],
            'CreatedTime': datetime(2013, 8, 19, 20, 53, 25, 0, 231, 0),
            'DefaultCooldown': 300,
            'DesiredCapacity': 1,
            'EnabledMetrics': [
            ],
            'HealthCheckGracePeriod': 300,
            'HealthCheckType': 'EC2',
            'Instances': [
                {
                    'AvailabilityZone': 'us-west-2c',
                    'HealthStatus': 'Healthy',
                    'InstanceId': 'i-4ba0837f',
                    'LaunchConfigurationName': 'my-launch-config',
                    'LifecycleState': 'InService',
                    'ProtectedFromScaleIn': False,
                },
            ],
            'LaunchConfigurationName': 'my-launch-config',
            'LoadBalancerNames': [
            ],
            'MaxSize': 1,
            'MinSize': 0,
            'NewInstancesProtectedFromScaleIn': False,
            'SuspendedProcesses': [
            ],
            'Tags': [
            ],
            'TerminationPolicies': [
                'Default',
            ],
            'VPCZoneIdentifier': 'subnet-12345678',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'AutoScalingGroups': [
            {
                'AutoScalingGroupName': 'string',
                'AutoScalingGroupARN': 'string',
                'LaunchConfigurationName': 'string',
                'LaunchTemplate': {
                    'LaunchTemplateId': 'string',
                    'LaunchTemplateName': 'string',
                    'Version': 'string'
                },
                'MixedInstancesPolicy': {
                    'LaunchTemplate': {
                        'LaunchTemplateSpecification': {
                            'LaunchTemplateId': 'string',
                            'LaunchTemplateName': 'string',
                            'Version': 'string'
                        },
                        'Overrides': [
                            {
                                'InstanceType': 'string',
                                'WeightedCapacity': 'string'
                            },
                        ]
                    },
                    'InstancesDistribution': {
                        'OnDemandAllocationStrategy': 'string',
                        'OnDemandBaseCapacity': 123,
                        'OnDemandPercentageAboveBaseCapacity': 123,
                        'SpotAllocationStrategy': 'string',
                        'SpotInstancePools': 123,
                        'SpotMaxPrice': 'string'
                    }
                },
                'MinSize': 123,
                'MaxSize': 123,
                'DesiredCapacity': 123,
                'DefaultCooldown': 123,
                'AvailabilityZones': [
                    'string',
                ],
                'LoadBalancerNames': [
                    'string',
                ],
                'TargetGroupARNs': [
                    'string',
                ],
                'HealthCheckType': 'string',
                'HealthCheckGracePeriod': 123,
                'Instances': [
                    {
                        'InstanceId': 'string',
                        'InstanceType': 'string',
                        'AvailabilityZone': 'string',
                        'LifecycleState': 'Pending'|'Pending:Wait'|'Pending:Proceed'|'Quarantined'|'InService'|'Terminating'|'Terminating:Wait'|'Terminating:Proceed'|'Terminated'|'Detaching'|'Detached'|'EnteringStandby'|'Standby',
                        'HealthStatus': 'string',
                        'LaunchConfigurationName': 'string',
                        'LaunchTemplate': {
                            'LaunchTemplateId': 'string',
                            'LaunchTemplateName': 'string',
                            'Version': 'string'
                        },
                        'ProtectedFromScaleIn': True|False,
                        'WeightedCapacity': 'string'
                    },
                ],
                'CreatedTime': datetime(2015, 1, 1),
                'SuspendedProcesses': [
                    {
                        'ProcessName': 'string',
                        'SuspensionReason': 'string'
                    },
                ],
                'PlacementGroup': 'string',
                'VPCZoneIdentifier': 'string',
                'EnabledMetrics': [
                    {
                        'Metric': 'string',
                        'Granularity': 'string'
                    },
                ],
                'Status': 'string',
                'Tags': [
                    {
                        'ResourceId': 'string',
                        'ResourceType': 'string',
                        'Key': 'string',
                        'Value': 'string',
                        'PropagateAtLaunch': True|False
                    },
                ],
                'TerminationPolicies': [
                    'string',
                ],
                'NewInstancesProtectedFromScaleIn': True|False,
                'ServiceLinkedRoleARN': 'string',
                'MaxInstanceLifetime': 123
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_auto_scaling_instances(InstanceIds=None, MaxRecords=None, NextToken=None):
    """
    Describes one or more Auto Scaling instances.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example describes the specified Auto Scaling instance.
    Expected Output:
    
    :example: response = client.describe_auto_scaling_instances(
        InstanceIds=[
            'string',
        ],
        MaxRecords=123,
        NextToken='string'
    )
    
    
    :type InstanceIds: list
    :param InstanceIds: The IDs of the instances. You can specify up to MaxRecords IDs. If you omit this parameter, all Auto Scaling instances are described. If you specify an ID that does not exist, it is ignored with no error.\n\n(string) --\n\n

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of items to return with this call. The default value is 50 and the maximum value is 50 .

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :rtype: dict

ReturnsResponse Syntax
{
    'AutoScalingInstances': [
        {
            'InstanceId': 'string',
            'InstanceType': 'string',
            'AutoScalingGroupName': 'string',
            'AvailabilityZone': 'string',
            'LifecycleState': 'string',
            'HealthStatus': 'string',
            'LaunchConfigurationName': 'string',
            'LaunchTemplate': {
                'LaunchTemplateId': 'string',
                'LaunchTemplateName': 'string',
                'Version': 'string'
            },
            'ProtectedFromScaleIn': True|False,
            'WeightedCapacity': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

AutoScalingInstances (list) --
The instances.

(dict) --
Describes an EC2 instance associated with an Auto Scaling group.

InstanceId (string) --
The ID of the instance.

InstanceType (string) --
The instance type of the EC2 instance.

AutoScalingGroupName (string) --
The name of the Auto Scaling group for the instance.

AvailabilityZone (string) --
The Availability Zone for the instance.

LifecycleState (string) --
The lifecycle state for the instance.

HealthStatus (string) --
The last reported health status of this instance. "Healthy" means that the instance is healthy and should remain in service. "Unhealthy" means that the instance is unhealthy and Amazon EC2 Auto Scaling should terminate and replace it.

LaunchConfigurationName (string) --
The launch configuration used to launch the instance. This value is not available if you attached the instance to the Auto Scaling group.

LaunchTemplate (dict) --
The launch template for the instance.

LaunchTemplateId (string) --
The ID of the launch template. To get the template ID, use the Amazon EC2 DescribeLaunchTemplates API operation. New launch templates can be created using the Amazon EC2 CreateLaunchTemplate API.
You must specify either a template ID or a template name.

LaunchTemplateName (string) --
The name of the launch template. To get the template name, use the Amazon EC2 DescribeLaunchTemplates API operation. New launch templates can be created using the Amazon EC2 CreateLaunchTemplate API.
You must specify either a template ID or a template name.

Version (string) --
The version number, $Latest , or $Default . To get the version number, use the Amazon EC2 DescribeLaunchTemplateVersions API operation. New launch template versions can be created using the Amazon EC2 CreateLaunchTemplateVersion API.
If the value is $Latest , Amazon EC2 Auto Scaling selects the latest version of the launch template when launching instances. If the value is $Default , Amazon EC2 Auto Scaling selects the default version of the launch template when launching instances. The default value is $Default .



ProtectedFromScaleIn (boolean) --
Indicates whether the instance is protected from termination by Amazon EC2 Auto Scaling when scaling in.

WeightedCapacity (string) --
The number of capacity units contributed by the instance based on its instance type.
Valid Range: Minimum value of 1. Maximum value of 999.





NextToken (string) --
A string that indicates that the response contains more items than can be returned in a single response. To receive additional items, specify this string for the NextToken value when requesting the next set of items. This value is null when there are no more items to return.







Exceptions

AutoScaling.Client.exceptions.InvalidNextToken
AutoScaling.Client.exceptions.ResourceContentionFault

Examples
This example describes the specified Auto Scaling instance.
response = client.describe_auto_scaling_instances(
    InstanceIds=[
        'i-4ba0837f',
    ],
)

print(response)


Expected Output:
{
    'AutoScalingInstances': [
        {
            'AutoScalingGroupName': 'my-auto-scaling-group',
            'AvailabilityZone': 'us-west-2c',
            'HealthStatus': 'HEALTHY',
            'InstanceId': 'i-4ba0837f',
            'LaunchConfigurationName': 'my-launch-config',
            'LifecycleState': 'InService',
            'ProtectedFromScaleIn': False,
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'AutoScalingInstances': [
            {
                'InstanceId': 'string',
                'InstanceType': 'string',
                'AutoScalingGroupName': 'string',
                'AvailabilityZone': 'string',
                'LifecycleState': 'string',
                'HealthStatus': 'string',
                'LaunchConfigurationName': 'string',
                'LaunchTemplate': {
                    'LaunchTemplateId': 'string',
                    'LaunchTemplateName': 'string',
                    'Version': 'string'
                },
                'ProtectedFromScaleIn': True|False,
                'WeightedCapacity': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    AutoScaling.Client.exceptions.InvalidNextToken
    AutoScaling.Client.exceptions.ResourceContentionFault
    
    """
    pass

def describe_auto_scaling_notification_types():
    """
    Describes the notification types that are supported by Amazon EC2 Auto Scaling.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example describes the available notification types.
    Expected Output:
    
    :example: response = client.describe_auto_scaling_notification_types()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'AutoScalingNotificationTypes': [
        'string',
    ]
}


Response Structure

(dict) --
AutoScalingNotificationTypes (list) --The notification types.

(string) --







Exceptions

AutoScaling.Client.exceptions.ResourceContentionFault

Examples
This example describes the available notification types.
response = client.describe_auto_scaling_notification_types(
)

print(response)


Expected Output:
{
    'AutoScalingNotificationTypes': [
        'autoscaling:EC2_INSTANCE_LAUNCH',
        'autoscaling:EC2_INSTANCE_LAUNCH_ERROR',
        'autoscaling:EC2_INSTANCE_TERMINATE',
        'autoscaling:EC2_INSTANCE_TERMINATE_ERROR',
        'autoscaling:TEST_NOTIFICATION',
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'AutoScalingNotificationTypes': [
            'string',
        ]
    }
    
    
    :returns: 
    AutoScaling.Client.exceptions.ResourceContentionFault
    
    """
    pass

def describe_launch_configurations(LaunchConfigurationNames=None, NextToken=None, MaxRecords=None):
    """
    Describes one or more launch configurations.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example describes the specified launch configuration.
    Expected Output:
    
    :example: response = client.describe_launch_configurations(
        LaunchConfigurationNames=[
            'string',
        ],
        NextToken='string',
        MaxRecords=123
    )
    
    
    :type LaunchConfigurationNames: list
    :param LaunchConfigurationNames: The launch configuration names. If you omit this parameter, all launch configurations are described.\n\n(string) --\n\n

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of items to return with this call. The default value is 50 and the maximum value is 100 .

    :rtype: dict

ReturnsResponse Syntax
{
    'LaunchConfigurations': [
        {
            'LaunchConfigurationName': 'string',
            'LaunchConfigurationARN': 'string',
            'ImageId': 'string',
            'KeyName': 'string',
            'SecurityGroups': [
                'string',
            ],
            'ClassicLinkVPCId': 'string',
            'ClassicLinkVPCSecurityGroups': [
                'string',
            ],
            'UserData': 'string',
            'InstanceType': 'string',
            'KernelId': 'string',
            'RamdiskId': 'string',
            'BlockDeviceMappings': [
                {
                    'VirtualName': 'string',
                    'DeviceName': 'string',
                    'Ebs': {
                        'SnapshotId': 'string',
                        'VolumeSize': 123,
                        'VolumeType': 'string',
                        'DeleteOnTermination': True|False,
                        'Iops': 123,
                        'Encrypted': True|False
                    },
                    'NoDevice': True|False
                },
            ],
            'InstanceMonitoring': {
                'Enabled': True|False
            },
            'SpotPrice': 'string',
            'IamInstanceProfile': 'string',
            'CreatedTime': datetime(2015, 1, 1),
            'EbsOptimized': True|False,
            'AssociatePublicIpAddress': True|False,
            'PlacementTenancy': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

LaunchConfigurations (list) --
The launch configurations.

(dict) --
Describes a launch configuration.

LaunchConfigurationName (string) --
The name of the launch configuration.

LaunchConfigurationARN (string) --
The Amazon Resource Name (ARN) of the launch configuration.

ImageId (string) --
The ID of the Amazon Machine Image (AMI) to use to launch your EC2 instances.
For more information, see Finding an AMI in the Amazon EC2 User Guide for Linux Instances .

KeyName (string) --
The name of the key pair.
For more information, see Amazon EC2 Key Pairs in the Amazon EC2 User Guide for Linux Instances .

SecurityGroups (list) --
A list that contains the security groups to assign to the instances in the Auto Scaling group.
For more information, see Security Groups for Your VPC in the Amazon Virtual Private Cloud User Guide .

(string) --


ClassicLinkVPCId (string) --
The ID of a ClassicLink-enabled VPC to link your EC2-Classic instances to.
For more information, see ClassicLink in the Amazon EC2 User Guide for Linux Instances and Linking EC2-Classic Instances to a VPC in the Amazon EC2 Auto Scaling User Guide .

ClassicLinkVPCSecurityGroups (list) --
The IDs of one or more security groups for the VPC specified in ClassicLinkVPCId .
For more information, see ClassicLink in the Amazon EC2 User Guide for Linux Instances and Linking EC2-Classic Instances to a VPC in the Amazon EC2 Auto Scaling User Guide .

(string) --


UserData (string) --
The Base64-encoded user data to make available to the launched EC2 instances.
For more information, see Instance Metadata and User Data in the Amazon EC2 User Guide for Linux Instances .

InstanceType (string) --
The instance type for the instances.
For information about available instance types, see Available Instance Types in the Amazon EC2 User Guide for Linux Instances.

KernelId (string) --
The ID of the kernel associated with the AMI.

RamdiskId (string) --
The ID of the RAM disk associated with the AMI.

BlockDeviceMappings (list) --
A block device mapping, which specifies the block devices for the instance.
For more information, see Block Device Mapping in the Amazon EC2 User Guide for Linux Instances .

(dict) --
Describes a block device mapping.

VirtualName (string) --
The name of the virtual device (for example, ephemeral0 ).
You can specify either VirtualName or Ebs , but not both.

DeviceName (string) --
The device name exposed to the EC2 instance (for example, /dev/sdh or xvdh ). For more information, see Device Naming on Linux Instances in the Amazon EC2 User Guide for Linux Instances .

Ebs (dict) --
Parameters used to automatically set up EBS volumes when an instance is launched.
You can specify either VirtualName or Ebs , but not both.

SnapshotId (string) --
The snapshot ID of the volume to use.
Conditional: This parameter is optional if you specify a volume size. If you specify both SnapshotId and VolumeSize , VolumeSize must be equal or greater than the size of the snapshot.

VolumeSize (integer) --
The volume size, in Gibibytes (GiB).
This can be a number from 1-1,024 for standard , 4-16,384 for io1 , 1-16,384 for gp2 , and 500-16,384 for st1 and sc1 . If you specify a snapshot, the volume size must be equal to or larger than the snapshot size.
Default: If you create a volume from a snapshot and you don\'t specify a volume size, the default is the snapshot size.

Note
At least one of VolumeSize or SnapshotId is required.


VolumeType (string) --
The volume type, which can be standard for Magnetic, io1 for Provisioned IOPS SSD, gp2 for General Purpose SSD, st1 for Throughput Optimized HDD, or sc1 for Cold HDD. For more information, see Amazon EBS Volume Types in the Amazon EC2 User Guide for Linux Instances .
Valid Values: standard | io1 | gp2 | st1 | sc1

DeleteOnTermination (boolean) --
Indicates whether the volume is deleted on instance termination. For Amazon EC2 Auto Scaling, the default value is true .

Iops (integer) --
The number of I/O operations per second (IOPS) to provision for the volume. The maximum ratio of IOPS to volume size (in GiB) is 50:1. For more information, see Amazon EBS Volume Types in the Amazon EC2 User Guide for Linux Instances .
Conditional: This parameter is required when the volume type is io1 . (Not used with standard , gp2 , st1 , or sc1 volumes.)

Encrypted (boolean) --
Specifies whether the volume should be encrypted. Encrypted EBS volumes can only be attached to instances that support Amazon EBS encryption. For more information, see Supported Instance Types . If your AMI uses encrypted volumes, you can also only launch it on supported instance types.

Note
If you are creating a volume from a snapshot, you cannot specify an encryption value. Volumes that are created from encrypted snapshots are automatically encrypted, and volumes that are created from unencrypted snapshots are automatically unencrypted. By default, encrypted snapshots use the AWS managed CMK that is used for EBS encryption, but you can specify a custom CMK when you create the snapshot. The ability to encrypt a snapshot during copying also allows you to apply a new CMK to an already-encrypted snapshot. Volumes restored from the resulting copy are only accessible using the new CMK.
Enabling encryption by default results in all EBS volumes being encrypted with the AWS managed CMK or a customer managed CMK, whether or not the snapshot was encrypted.

For more information, see Using Encryption with EBS-Backed AMIs in the Amazon EC2 User Guide for Linux Instances and Required CMK Key Policy for Use with Encrypted Volumes in the Amazon EC2 Auto Scaling User Guide .



NoDevice (boolean) --
Setting this value to true suppresses the specified device included in the block device mapping of the AMI.
If NoDevice is true for the root device, instances might fail the EC2 health check. In that case, Amazon EC2 Auto Scaling launches replacement instances.
If you specify NoDevice , you cannot specify Ebs .





InstanceMonitoring (dict) --
Controls whether instances in this group are launched with detailed (true ) or basic (false ) monitoring.
For more information, see Configure Monitoring for Auto Scaling Instances in the Amazon EC2 Auto Scaling User Guide .

Enabled (boolean) --
If true , detailed monitoring is enabled. Otherwise, basic monitoring is enabled.



SpotPrice (string) --
The maximum hourly price to be paid for any Spot Instance launched to fulfill the request. Spot Instances are launched when the price you specify exceeds the current Spot price.
For more information, see Launching Spot Instances in Your Auto Scaling Group in the Amazon EC2 Auto Scaling User Guide .

IamInstanceProfile (string) --
The name or the Amazon Resource Name (ARN) of the instance profile associated with the IAM role for the instance. The instance profile contains the IAM role.
For more information, see IAM Role for Applications That Run on Amazon EC2 Instances in the Amazon EC2 Auto Scaling User Guide .

CreatedTime (datetime) --
The creation date and time for the launch configuration.

EbsOptimized (boolean) --
Specifies whether the launch configuration is optimized for EBS I/O (true ) or not (false ).
For more information, see Amazon EBS-Optimized Instances in the Amazon EC2 User Guide for Linux Instances .

AssociatePublicIpAddress (boolean) --
For Auto Scaling groups that are running in a VPC, specifies whether to assign a public IP address to the group\'s instances.
For more information, see Launching Auto Scaling Instances in a VPC in the Amazon EC2 Auto Scaling User Guide .

PlacementTenancy (string) --
The tenancy of the instance, either default or dedicated . An instance with dedicated tenancy runs on isolated, single-tenant hardware and can only be launched into a VPC.
For more information, see Instance Placement Tenancy in the Amazon EC2 Auto Scaling User Guide .





NextToken (string) --
A string that indicates that the response contains more items than can be returned in a single response. To receive additional items, specify this string for the NextToken value when requesting the next set of items. This value is null when there are no more items to return.







Exceptions

AutoScaling.Client.exceptions.InvalidNextToken
AutoScaling.Client.exceptions.ResourceContentionFault

Examples
This example describes the specified launch configuration.
response = client.describe_launch_configurations(
    LaunchConfigurationNames=[
        'my-launch-config',
    ],
)

print(response)


Expected Output:
{
    'LaunchConfigurations': [
        {
            'AssociatePublicIpAddress': True,
            'BlockDeviceMappings': [
            ],
            'CreatedTime': datetime(2014, 5, 7, 17, 39, 28, 2, 127, 0),
            'EbsOptimized': False,
            'ImageId': 'ami-043a5034',
            'InstanceMonitoring': {
                'Enabled': True,
            },
            'InstanceType': 't1.micro',
            'LaunchConfigurationARN': 'arn:aws:autoscaling:us-west-2:123456789012:launchConfiguration:98d3b196-4cf9-4e88-8ca1-8547c24ced8b:launchConfigurationName/my-launch-config',
            'LaunchConfigurationName': 'my-launch-config',
            'SecurityGroups': [
                'sg-67ef0308',
            ],
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'LaunchConfigurations': [
            {
                'LaunchConfigurationName': 'string',
                'LaunchConfigurationARN': 'string',
                'ImageId': 'string',
                'KeyName': 'string',
                'SecurityGroups': [
                    'string',
                ],
                'ClassicLinkVPCId': 'string',
                'ClassicLinkVPCSecurityGroups': [
                    'string',
                ],
                'UserData': 'string',
                'InstanceType': 'string',
                'KernelId': 'string',
                'RamdiskId': 'string',
                'BlockDeviceMappings': [
                    {
                        'VirtualName': 'string',
                        'DeviceName': 'string',
                        'Ebs': {
                            'SnapshotId': 'string',
                            'VolumeSize': 123,
                            'VolumeType': 'string',
                            'DeleteOnTermination': True|False,
                            'Iops': 123,
                            'Encrypted': True|False
                        },
                        'NoDevice': True|False
                    },
                ],
                'InstanceMonitoring': {
                    'Enabled': True|False
                },
                'SpotPrice': 'string',
                'IamInstanceProfile': 'string',
                'CreatedTime': datetime(2015, 1, 1),
                'EbsOptimized': True|False,
                'AssociatePublicIpAddress': True|False,
                'PlacementTenancy': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_lifecycle_hook_types():
    """
    Describes the available types of lifecycle hooks.
    The following hook types are supported:
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example describes the available lifecycle hook types.
    Expected Output:
    
    :example: response = client.describe_lifecycle_hook_types()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'LifecycleHookTypes': [
        'string',
    ]
}


Response Structure

(dict) --
LifecycleHookTypes (list) --The lifecycle hook types.

(string) --







Exceptions

AutoScaling.Client.exceptions.ResourceContentionFault

Examples
This example describes the available lifecycle hook types.
response = client.describe_lifecycle_hook_types(
)

print(response)


Expected Output:
{
    'LifecycleHookTypes': [
        'autoscaling:EC2_INSTANCE_LAUNCHING',
        'autoscaling:EC2_INSTANCE_TERMINATING',
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'LifecycleHookTypes': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_lifecycle_hooks(AutoScalingGroupName=None, LifecycleHookNames=None):
    """
    Describes the lifecycle hooks for the specified Auto Scaling group.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example describes the lifecycle hooks for the specified Auto Scaling group.
    Expected Output:
    
    :example: response = client.describe_lifecycle_hooks(
        AutoScalingGroupName='string',
        LifecycleHookNames=[
            'string',
        ]
    )
    
    
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: [REQUIRED]\nThe name of the Auto Scaling group.\n

    :type LifecycleHookNames: list
    :param LifecycleHookNames: The names of one or more lifecycle hooks. If you omit this parameter, all lifecycle hooks are described.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'LifecycleHooks': [
        {
            'LifecycleHookName': 'string',
            'AutoScalingGroupName': 'string',
            'LifecycleTransition': 'string',
            'NotificationTargetARN': 'string',
            'RoleARN': 'string',
            'NotificationMetadata': 'string',
            'HeartbeatTimeout': 123,
            'GlobalTimeout': 123,
            'DefaultResult': 'string'
        },
    ]
}


Response Structure

(dict) --

LifecycleHooks (list) --
The lifecycle hooks for the specified group.

(dict) --
Describes a lifecycle hook, which tells Amazon EC2 Auto Scaling that you want to perform an action whenever it launches instances or terminates instances.

LifecycleHookName (string) --
The name of the lifecycle hook.

AutoScalingGroupName (string) --
The name of the Auto Scaling group for the lifecycle hook.

LifecycleTransition (string) --
The state of the EC2 instance to which to attach the lifecycle hook. The following are possible values:

autoscaling:EC2_INSTANCE_LAUNCHING
autoscaling:EC2_INSTANCE_TERMINATING


NotificationTargetARN (string) --
The ARN of the target that Amazon EC2 Auto Scaling sends notifications to when an instance is in the transition state for the lifecycle hook. The notification target can be either an SQS queue or an SNS topic.

RoleARN (string) --
The ARN of the IAM role that allows the Auto Scaling group to publish to the specified notification target.

NotificationMetadata (string) --
Additional information that is included any time Amazon EC2 Auto Scaling sends a message to the notification target.

HeartbeatTimeout (integer) --
The maximum time, in seconds, that can elapse before the lifecycle hook times out. If the lifecycle hook times out, Amazon EC2 Auto Scaling performs the action that you specified in the DefaultResult parameter.

GlobalTimeout (integer) --
The maximum time, in seconds, that an instance can remain in a Pending:Wait or Terminating:Wait state. The maximum is 172800 seconds (48 hours) or 100 times HeartbeatTimeout , whichever is smaller.

DefaultResult (string) --
Defines the action the Auto Scaling group should take when the lifecycle hook timeout elapses or if an unexpected failure occurs. The possible values are CONTINUE and ABANDON .











Exceptions

AutoScaling.Client.exceptions.ResourceContentionFault

Examples
This example describes the lifecycle hooks for the specified Auto Scaling group.
response = client.describe_lifecycle_hooks(
    AutoScalingGroupName='my-auto-scaling-group',
)

print(response)


Expected Output:
{
    'LifecycleHooks': [
        {
            'AutoScalingGroupName': 'my-auto-scaling-group',
            'DefaultResult': 'ABANDON',
            'GlobalTimeout': 172800,
            'HeartbeatTimeout': 3600,
            'LifecycleHookName': 'my-lifecycle-hook',
            'LifecycleTransition': 'autoscaling:EC2_INSTANCE_LAUNCHING',
            'NotificationTargetARN': 'arn:aws:sns:us-west-2:123456789012:my-sns-topic',
            'RoleARN': 'arn:aws:iam::123456789012:role/my-auto-scaling-role',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'LifecycleHooks': [
            {
                'LifecycleHookName': 'string',
                'AutoScalingGroupName': 'string',
                'LifecycleTransition': 'string',
                'NotificationTargetARN': 'string',
                'RoleARN': 'string',
                'NotificationMetadata': 'string',
                'HeartbeatTimeout': 123,
                'GlobalTimeout': 123,
                'DefaultResult': 'string'
            },
        ]
    }
    
    
    :returns: 
    autoscaling:EC2_INSTANCE_LAUNCHING
    autoscaling:EC2_INSTANCE_TERMINATING
    
    """
    pass

def describe_load_balancer_target_groups(AutoScalingGroupName=None, NextToken=None, MaxRecords=None):
    """
    Describes the target groups for the specified Auto Scaling group.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example describes the target groups attached to the specified Auto Scaling group.
    Expected Output:
    
    :example: response = client.describe_load_balancer_target_groups(
        AutoScalingGroupName='string',
        NextToken='string',
        MaxRecords=123
    )
    
    
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: [REQUIRED]\nThe name of the Auto Scaling group.\n

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of items to return with this call. The default value is 100 and the maximum value is 100 .

    :rtype: dict

ReturnsResponse Syntax
{
    'LoadBalancerTargetGroups': [
        {
            'LoadBalancerTargetGroupARN': 'string',
            'State': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

LoadBalancerTargetGroups (list) --
Information about the target groups.

(dict) --
Describes the state of a target group.
If you attach a target group to an existing Auto Scaling group, the initial state is Adding . The state transitions to Added after all Auto Scaling instances are registered with the target group. If Elastic Load Balancing health checks are enabled, the state transitions to InService after at least one Auto Scaling instance passes the health check. If EC2 health checks are enabled instead, the target group remains in the Added state.

LoadBalancerTargetGroupARN (string) --
The Amazon Resource Name (ARN) of the target group.

State (string) --
The state of the target group.

Adding - The Auto Scaling instances are being registered with the target group.
Added - All Auto Scaling instances are registered with the target group.
InService - At least one Auto Scaling instance passed an ELB health check.
Removing - The Auto Scaling instances are being deregistered from the target group. If connection draining is enabled, Elastic Load Balancing waits for in-flight requests to complete before deregistering the instances.
Removed - All Auto Scaling instances are deregistered from the target group.






NextToken (string) --
A string that indicates that the response contains more items than can be returned in a single response. To receive additional items, specify this string for the NextToken value when requesting the next set of items. This value is null when there are no more items to return.







Exceptions

AutoScaling.Client.exceptions.ResourceContentionFault

Examples
This example describes the target groups attached to the specified Auto Scaling group.
response = client.describe_load_balancer_target_groups(
    AutoScalingGroupName='my-auto-scaling-group',
)

print(response)


Expected Output:
{
    'LoadBalancerTargetGroups': [
        {
            'LoadBalancerTargetGroupARN': 'arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067',
            'State': 'Added',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'LoadBalancerTargetGroups': [
            {
                'LoadBalancerTargetGroupARN': 'string',
                'State': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Adding - The Auto Scaling instances are being registered with the target group.
    Added - All Auto Scaling instances are registered with the target group.
    InService - At least one Auto Scaling instance passed an ELB health check.
    Removing - The Auto Scaling instances are being deregistered from the target group. If connection draining is enabled, Elastic Load Balancing waits for in-flight requests to complete before deregistering the instances.
    Removed - All Auto Scaling instances are deregistered from the target group.
    
    """
    pass

def describe_load_balancers(AutoScalingGroupName=None, NextToken=None, MaxRecords=None):
    """
    Describes the load balancers for the specified Auto Scaling group.
    This operation describes only Classic Load Balancers. If you have Application Load Balancers or Network Load Balancers, use the  DescribeLoadBalancerTargetGroups API instead.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example describes the load balancers attached to the specified Auto Scaling group.
    Expected Output:
    
    :example: response = client.describe_load_balancers(
        AutoScalingGroupName='string',
        NextToken='string',
        MaxRecords=123
    )
    
    
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: [REQUIRED]\nThe name of the Auto Scaling group.\n

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of items to return with this call. The default value is 100 and the maximum value is 100 .

    :rtype: dict

ReturnsResponse Syntax
{
    'LoadBalancers': [
        {
            'LoadBalancerName': 'string',
            'State': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

LoadBalancers (list) --
The load balancers.

(dict) --
Describes the state of a Classic Load Balancer.
If you specify a load balancer when creating the Auto Scaling group, the state of the load balancer is InService .
If you attach a load balancer to an existing Auto Scaling group, the initial state is Adding . The state transitions to Added after all instances in the group are registered with the load balancer. If Elastic Load Balancing health checks are enabled for the load balancer, the state transitions to InService after at least one instance in the group passes the health check. If EC2 health checks are enabled instead, the load balancer remains in the Added state.

LoadBalancerName (string) --
The name of the load balancer.

State (string) --
One of the following load balancer states:

Adding - The instances in the group are being registered with the load balancer.
Added - All instances in the group are registered with the load balancer.
InService - At least one instance in the group passed an ELB health check.
Removing - The instances in the group are being deregistered from the load balancer. If connection draining is enabled, Elastic Load Balancing waits for in-flight requests to complete before deregistering the instances.
Removed - All instances in the group are deregistered from the load balancer.






NextToken (string) --
A string that indicates that the response contains more items than can be returned in a single response. To receive additional items, specify this string for the NextToken value when requesting the next set of items. This value is null when there are no more items to return.







Exceptions

AutoScaling.Client.exceptions.ResourceContentionFault

Examples
This example describes the load balancers attached to the specified Auto Scaling group.
response = client.describe_load_balancers(
    AutoScalingGroupName='my-auto-scaling-group',
)

print(response)


Expected Output:
{
    'LoadBalancers': [
        {
            'LoadBalancerName': 'my-load-balancer',
            'State': 'Added',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'LoadBalancers': [
            {
                'LoadBalancerName': 'string',
                'State': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Adding - The instances in the group are being registered with the load balancer.
    Added - All instances in the group are registered with the load balancer.
    InService - At least one instance in the group passed an ELB health check.
    Removing - The instances in the group are being deregistered from the load balancer. If connection draining is enabled, Elastic Load Balancing waits for in-flight requests to complete before deregistering the instances.
    Removed - All instances in the group are deregistered from the load balancer.
    
    """
    pass

def describe_metric_collection_types():
    """
    Describes the available CloudWatch metrics for Amazon EC2 Auto Scaling.
    The GroupStandbyInstances metric is not returned by default. You must explicitly request this metric when calling the  EnableMetricsCollection API.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example describes the available metric collection types.
    Expected Output:
    
    :example: response = client.describe_metric_collection_types()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'Metrics': [
        {
            'Metric': 'string'
        },
    ],
    'Granularities': [
        {
            'Granularity': 'string'
        },
    ]
}


Response Structure

(dict) --
Metrics (list) --One or more metrics.

(dict) --Describes a metric.

Metric (string) --One of the following metrics:

GroupMinSize
GroupMaxSize
GroupDesiredCapacity
GroupInServiceInstances
GroupPendingInstances
GroupStandbyInstances
GroupTerminatingInstances
GroupTotalInstances






Granularities (list) --The granularities for the metrics.

(dict) --Describes a granularity of a metric.

Granularity (string) --The granularity. The only valid value is 1Minute .










Exceptions

AutoScaling.Client.exceptions.ResourceContentionFault

Examples
This example describes the available metric collection types.
response = client.describe_metric_collection_types(
)

print(response)


Expected Output:
{
    'Granularities': [
        {
            'Granularity': '1Minute',
        },
    ],
    'Metrics': [
        {
            'Metric': 'GroupMinSize',
        },
        {
            'Metric': 'GroupMaxSize',
        },
        {
            'Metric': 'GroupDesiredCapacity',
        },
        {
            'Metric': 'GroupInServiceInstances',
        },
        {
            'Metric': 'GroupPendingInstances',
        },
        {
            'Metric': 'GroupTerminatingInstances',
        },
        {
            'Metric': 'GroupStandbyInstances',
        },
        {
            'Metric': 'GroupTotalInstances',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Metrics': [
            {
                'Metric': 'string'
            },
        ],
        'Granularities': [
            {
                'Granularity': 'string'
            },
        ]
    }
    
    
    :returns: 
    AutoScaling.Client.exceptions.ResourceContentionFault
    
    """
    pass

def describe_notification_configurations(AutoScalingGroupNames=None, NextToken=None, MaxRecords=None):
    """
    Describes the notification actions associated with the specified Auto Scaling group.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example describes the notification configurations for the specified Auto Scaling group.
    Expected Output:
    
    :example: response = client.describe_notification_configurations(
        AutoScalingGroupNames=[
            'string',
        ],
        NextToken='string',
        MaxRecords=123
    )
    
    
    :type AutoScalingGroupNames: list
    :param AutoScalingGroupNames: The name of the Auto Scaling group.\n\n(string) --\n\n

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of items to return with this call. The default value is 50 and the maximum value is 100 .

    :rtype: dict

ReturnsResponse Syntax
{
    'NotificationConfigurations': [
        {
            'AutoScalingGroupName': 'string',
            'TopicARN': 'string',
            'NotificationType': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

NotificationConfigurations (list) --
The notification configurations.

(dict) --
Describes a notification.

AutoScalingGroupName (string) --
The name of the Auto Scaling group.

TopicARN (string) --
The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (Amazon SNS) topic.

NotificationType (string) --
One of the following event notification types:

autoscaling:EC2_INSTANCE_LAUNCH
autoscaling:EC2_INSTANCE_LAUNCH_ERROR
autoscaling:EC2_INSTANCE_TERMINATE
autoscaling:EC2_INSTANCE_TERMINATE_ERROR
autoscaling:TEST_NOTIFICATION






NextToken (string) --
A string that indicates that the response contains more items than can be returned in a single response. To receive additional items, specify this string for the NextToken value when requesting the next set of items. This value is null when there are no more items to return.







Exceptions

AutoScaling.Client.exceptions.InvalidNextToken
AutoScaling.Client.exceptions.ResourceContentionFault

Examples
This example describes the notification configurations for the specified Auto Scaling group.
response = client.describe_notification_configurations(
    AutoScalingGroupNames=[
        'my-auto-scaling-group',
    ],
)

print(response)


Expected Output:
{
    'NotificationConfigurations': [
        {
            'AutoScalingGroupName': 'my-auto-scaling-group',
            'NotificationType': 'autoscaling:TEST_NOTIFICATION',
            'TopicARN': 'arn:aws:sns:us-west-2:123456789012:my-sns-topic-2',
        },
        {
            'AutoScalingGroupName': 'my-auto-scaling-group',
            'NotificationType': 'autoscaling:TEST_NOTIFICATION',
            'TopicARN': 'arn:aws:sns:us-west-2:123456789012:my-sns-topic',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'NotificationConfigurations': [
            {
                'AutoScalingGroupName': 'string',
                'TopicARN': 'string',
                'NotificationType': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    autoscaling:EC2_INSTANCE_LAUNCH
    autoscaling:EC2_INSTANCE_LAUNCH_ERROR
    autoscaling:EC2_INSTANCE_TERMINATE
    autoscaling:EC2_INSTANCE_TERMINATE_ERROR
    autoscaling:TEST_NOTIFICATION
    
    """
    pass

def describe_policies(AutoScalingGroupName=None, PolicyNames=None, PolicyTypes=None, NextToken=None, MaxRecords=None):
    """
    Describes the policies for the specified Auto Scaling group.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example describes the policies for the specified Auto Scaling group.
    Expected Output:
    
    :example: response = client.describe_policies(
        AutoScalingGroupName='string',
        PolicyNames=[
            'string',
        ],
        PolicyTypes=[
            'string',
        ],
        NextToken='string',
        MaxRecords=123
    )
    
    
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: The name of the Auto Scaling group.

    :type PolicyNames: list
    :param PolicyNames: The names of one or more policies. If you omit this parameter, all policies are described. If a group name is provided, the results are limited to that group. This list is limited to 50 items. If you specify an unknown policy name, it is ignored with no error.\n\n(string) --\n\n

    :type PolicyTypes: list
    :param PolicyTypes: One or more policy types. The valid values are SimpleScaling , StepScaling , and TargetTrackingScaling .\n\n(string) --\n\n

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of items to be returned with each call. The default value is 50 and the maximum value is 100 .

    :rtype: dict

ReturnsResponse Syntax
{
    'ScalingPolicies': [
        {
            'AutoScalingGroupName': 'string',
            'PolicyName': 'string',
            'PolicyARN': 'string',
            'PolicyType': 'string',
            'AdjustmentType': 'string',
            'MinAdjustmentStep': 123,
            'MinAdjustmentMagnitude': 123,
            'ScalingAdjustment': 123,
            'Cooldown': 123,
            'StepAdjustments': [
                {
                    'MetricIntervalLowerBound': 123.0,
                    'MetricIntervalUpperBound': 123.0,
                    'ScalingAdjustment': 123
                },
            ],
            'MetricAggregationType': 'string',
            'EstimatedInstanceWarmup': 123,
            'Alarms': [
                {
                    'AlarmName': 'string',
                    'AlarmARN': 'string'
                },
            ],
            'TargetTrackingConfiguration': {
                'PredefinedMetricSpecification': {
                    'PredefinedMetricType': 'ASGAverageCPUUtilization'|'ASGAverageNetworkIn'|'ASGAverageNetworkOut'|'ALBRequestCountPerTarget',
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
                'TargetValue': 123.0,
                'DisableScaleIn': True|False
            },
            'Enabled': True|False
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

ScalingPolicies (list) --
The scaling policies.

(dict) --
Describes a scaling policy.

AutoScalingGroupName (string) --
The name of the Auto Scaling group.

PolicyName (string) --
The name of the scaling policy.

PolicyARN (string) --
The Amazon Resource Name (ARN) of the policy.

PolicyType (string) --
The policy type. The valid values are SimpleScaling , StepScaling , and TargetTrackingScaling .

AdjustmentType (string) --
The adjustment type, which specifies how ScalingAdjustment is interpreted. The valid values are ChangeInCapacity , ExactCapacity , and PercentChangeInCapacity .

MinAdjustmentStep (integer) --
Available for backward compatibility. Use MinAdjustmentMagnitude instead.

MinAdjustmentMagnitude (integer) --
The minimum number of instances to scale. If the value of AdjustmentType is PercentChangeInCapacity , the scaling policy changes the DesiredCapacity of the Auto Scaling group by at least this many instances. Otherwise, the error is ValidationError .

ScalingAdjustment (integer) --
The amount by which to scale, based on the specified adjustment type. A positive value adds to the current capacity while a negative number removes from the current capacity.

Cooldown (integer) --
The amount of time, in seconds, after a scaling activity completes before any further dynamic scaling activities can start.

StepAdjustments (list) --
A set of adjustments that enable you to scale based on the size of the alarm breach.

(dict) --
Describes information used to create a step adjustment for a step scaling policy.
For the following examples, suppose that you have an alarm with a breach threshold of 50:

To trigger the adjustment when the metric is greater than or equal to 50 and less than 60, specify a lower bound of 0 and an upper bound of 10.
To trigger the adjustment when the metric is greater than 40 and less than or equal to 50, specify a lower bound of -10 and an upper bound of 0.

There are a few rules for the step adjustments for your step policy:

The ranges of your step adjustments can\'t overlap or have a gap.
At most, one step adjustment can have a null lower bound. If one step adjustment has a negative lower bound, then there must be a step adjustment with a null lower bound.
At most, one step adjustment can have a null upper bound. If one step adjustment has a positive upper bound, then there must be a step adjustment with a null upper bound.
The upper and lower bound can\'t be null in the same step adjustment.

For more information, see Step Adjustments in the Amazon EC2 Auto Scaling User Guide .

MetricIntervalLowerBound (float) --
The lower bound for the difference between the alarm threshold and the CloudWatch metric. If the metric value is above the breach threshold, the lower bound is inclusive (the metric must be greater than or equal to the threshold plus the lower bound). Otherwise, it is exclusive (the metric must be greater than the threshold plus the lower bound). A null value indicates negative infinity.

MetricIntervalUpperBound (float) --
The upper bound for the difference between the alarm threshold and the CloudWatch metric. If the metric value is above the breach threshold, the upper bound is exclusive (the metric must be less than the threshold plus the upper bound). Otherwise, it is inclusive (the metric must be less than or equal to the threshold plus the upper bound). A null value indicates positive infinity.
The upper bound must be greater than the lower bound.

ScalingAdjustment (integer) --
The amount by which to scale, based on the specified adjustment type. A positive value adds to the current capacity while a negative number removes from the current capacity.





MetricAggregationType (string) --
The aggregation type for the CloudWatch metrics. The valid values are Minimum , Maximum , and Average .

EstimatedInstanceWarmup (integer) --
The estimated time, in seconds, until a newly launched instance can contribute to the CloudWatch metrics.

Alarms (list) --
The CloudWatch alarms related to the policy.

(dict) --
Describes an alarm.

AlarmName (string) --
The name of the alarm.

AlarmARN (string) --
The Amazon Resource Name (ARN) of the alarm.





TargetTrackingConfiguration (dict) --
A target tracking scaling policy.

PredefinedMetricSpecification (dict) --
A predefined metric. You must specify either a predefined metric or a customized metric.

PredefinedMetricType (string) --
The metric type. The following predefined metrics are available:

ASGAverageCPUUtilization - Average CPU utilization of the Auto Scaling group.
ASGAverageNetworkIn - Average number of bytes received on all network interfaces by the Auto Scaling group.
ASGAverageNetworkOut - Average number of bytes sent out on all network interfaces by the Auto Scaling group.
ALBRequestCountPerTarget - Number of requests completed per target in an Application Load Balancer target group.


ResourceLabel (string) --
Identifies the resource associated with the metric type. You can\'t specify a resource label unless the metric type is ALBRequestCountPerTarget and there is a target group attached to the Auto Scaling group.
The format is ``app/load-balancer-name /load-balancer-id /targetgroup/target-group-name /target-group-id `` , where

``app/load-balancer-name /load-balancer-id `` is the final portion of the load balancer ARN, and
``targetgroup/target-group-name /target-group-id `` is the final portion of the target group ARN.




CustomizedMetricSpecification (dict) --
A customized metric. You must specify either a predefined metric or a customized metric.

MetricName (string) --
The name of the metric.

Namespace (string) --
The namespace of the metric.

Dimensions (list) --
The dimensions of the metric.
Conditional: If you published your metric with dimensions, you must specify the same dimensions in your scaling policy.

(dict) --
Describes the dimension of a metric.

Name (string) --
The name of the dimension.

Value (string) --
The value of the dimension.





Statistic (string) --
The statistic of the metric.

Unit (string) --
The unit of the metric.



TargetValue (float) --
The target value for the metric.

DisableScaleIn (boolean) --
Indicates whether scaling in by the target tracking scaling policy is disabled. If scaling in is disabled, the target tracking scaling policy doesn\'t remove instances from the Auto Scaling group. Otherwise, the target tracking scaling policy can remove instances from the Auto Scaling group. The default is false .



Enabled (boolean) --
Indicates whether the policy is enabled (true ) or disabled (false ).





NextToken (string) --
A string that indicates that the response contains more items than can be returned in a single response. To receive additional items, specify this string for the NextToken value when requesting the next set of items. This value is null when there are no more items to return.







Exceptions

AutoScaling.Client.exceptions.InvalidNextToken
AutoScaling.Client.exceptions.ResourceContentionFault
AutoScaling.Client.exceptions.ServiceLinkedRoleFailure

Examples
This example describes the policies for the specified Auto Scaling group.
response = client.describe_policies(
    AutoScalingGroupName='my-auto-scaling-group',
)

print(response)


Expected Output:
{
    'ScalingPolicies': [
        {
            'AdjustmentType': 'ChangeInCapacity',
            'Alarms': [
            ],
            'AutoScalingGroupName': 'my-auto-scaling-group',
            'PolicyARN': 'arn:aws:autoscaling:us-west-2:123456789012:scalingPolicy:2233f3d7-6290-403b-b632-93c553560106:autoScalingGroupName/my-auto-scaling-group:policyName/ScaleIn',
            'PolicyName': 'ScaleIn',
            'ScalingAdjustment': -1,
        },
        {
            'AdjustmentType': 'PercentChangeInCapacity',
            'Alarms': [
            ],
            'AutoScalingGroupName': 'my-auto-scaling-group',
            'Cooldown': 60,
            'MinAdjustmentStep': 2,
            'PolicyARN': 'arn:aws:autoscaling:us-west-2:123456789012:scalingPolicy:2b435159-cf77-4e89-8c0e-d63b497baad7:autoScalingGroupName/my-auto-scaling-group:policyName/ScalePercentChange',
            'PolicyName': 'ScalePercentChange',
            'ScalingAdjustment': 25,
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ScalingPolicies': [
            {
                'AutoScalingGroupName': 'string',
                'PolicyName': 'string',
                'PolicyARN': 'string',
                'PolicyType': 'string',
                'AdjustmentType': 'string',
                'MinAdjustmentStep': 123,
                'MinAdjustmentMagnitude': 123,
                'ScalingAdjustment': 123,
                'Cooldown': 123,
                'StepAdjustments': [
                    {
                        'MetricIntervalLowerBound': 123.0,
                        'MetricIntervalUpperBound': 123.0,
                        'ScalingAdjustment': 123
                    },
                ],
                'MetricAggregationType': 'string',
                'EstimatedInstanceWarmup': 123,
                'Alarms': [
                    {
                        'AlarmName': 'string',
                        'AlarmARN': 'string'
                    },
                ],
                'TargetTrackingConfiguration': {
                    'PredefinedMetricSpecification': {
                        'PredefinedMetricType': 'ASGAverageCPUUtilization'|'ASGAverageNetworkIn'|'ASGAverageNetworkOut'|'ALBRequestCountPerTarget',
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
                    'TargetValue': 123.0,
                    'DisableScaleIn': True|False
                },
                'Enabled': True|False
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    To trigger the adjustment when the metric is greater than or equal to 50 and less than 60, specify a lower bound of 0 and an upper bound of 10.
    To trigger the adjustment when the metric is greater than 40 and less than or equal to 50, specify a lower bound of -10 and an upper bound of 0.
    
    """
    pass

def describe_scaling_activities(ActivityIds=None, AutoScalingGroupName=None, MaxRecords=None, NextToken=None):
    """
    Describes one or more scaling activities for the specified Auto Scaling group.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example describes the scaling activities for the specified Auto Scaling group.
    Expected Output:
    
    :example: response = client.describe_scaling_activities(
        ActivityIds=[
            'string',
        ],
        AutoScalingGroupName='string',
        MaxRecords=123,
        NextToken='string'
    )
    
    
    :type ActivityIds: list
    :param ActivityIds: The activity IDs of the desired scaling activities. You can specify up to 50 IDs. If you omit this parameter, all activities for the past six weeks are described. If unknown activities are requested, they are ignored with no error. If you specify an Auto Scaling group, the results are limited to that group.\n\n(string) --\n\n

    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: The name of the Auto Scaling group.

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of items to return with this call. The default value is 100 and the maximum value is 100 .

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :rtype: dict

ReturnsResponse Syntax
{
    'Activities': [
        {
            'ActivityId': 'string',
            'AutoScalingGroupName': 'string',
            'Description': 'string',
            'Cause': 'string',
            'StartTime': datetime(2015, 1, 1),
            'EndTime': datetime(2015, 1, 1),
            'StatusCode': 'PendingSpotBidPlacement'|'WaitingForSpotInstanceRequestId'|'WaitingForSpotInstanceId'|'WaitingForInstanceId'|'PreInService'|'InProgress'|'WaitingForELBConnectionDraining'|'MidLifecycleAction'|'WaitingForInstanceWarmup'|'Successful'|'Failed'|'Cancelled',
            'StatusMessage': 'string',
            'Progress': 123,
            'Details': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Activities (list) --
The scaling activities. Activities are sorted by start time. Activities still in progress are described first.

(dict) --
Describes scaling activity, which is a long-running process that represents a change to your Auto Scaling group, such as changing its size or replacing an instance.

ActivityId (string) --
The ID of the activity.

AutoScalingGroupName (string) --
The name of the Auto Scaling group.

Description (string) --
A friendly, more verbose description of the activity.

Cause (string) --
The reason the activity began.

StartTime (datetime) --
The start time of the activity.

EndTime (datetime) --
The end time of the activity.

StatusCode (string) --
The current status of the activity.

StatusMessage (string) --
A friendly, more verbose description of the activity status.

Progress (integer) --
A value between 0 and 100 that indicates the progress of the activity.

Details (string) --
The details about the activity.





NextToken (string) --
A string that indicates that the response contains more items than can be returned in a single response. To receive additional items, specify this string for the NextToken value when requesting the next set of items. This value is null when there are no more items to return.







Exceptions

AutoScaling.Client.exceptions.InvalidNextToken
AutoScaling.Client.exceptions.ResourceContentionFault

Examples
This example describes the scaling activities for the specified Auto Scaling group.
response = client.describe_scaling_activities(
    AutoScalingGroupName='my-auto-scaling-group',
)

print(response)


Expected Output:
{
    'Activities': [
        {
            'ActivityId': 'f9f2d65b-f1f2-43e7-b46d-d86756459699',
            'AutoScalingGroupName': 'my-auto-scaling-group',
            'Cause': 'At 2013-08-19T20:53:25Z a user request created an AutoScalingGroup changing the desired capacity from 0 to 1.  At 2013-08-19T20:53:29Z an instance was started in response to a difference between desired and actual capacity, increasing the capacity from 0 to 1.',
            'Description': 'Launching a new EC2 instance: i-4ba0837f',
            'Details': 'details',
            'EndTime': datetime(2013, 8, 19, 20, 54, 2, 0, 231, 0),
            'Progress': 100,
            'StartTime': datetime(2013, 8, 19, 20, 53, 29, 0, 231, 0),
            'StatusCode': 'Successful',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Activities': [
            {
                'ActivityId': 'string',
                'AutoScalingGroupName': 'string',
                'Description': 'string',
                'Cause': 'string',
                'StartTime': datetime(2015, 1, 1),
                'EndTime': datetime(2015, 1, 1),
                'StatusCode': 'PendingSpotBidPlacement'|'WaitingForSpotInstanceRequestId'|'WaitingForSpotInstanceId'|'WaitingForInstanceId'|'PreInService'|'InProgress'|'WaitingForELBConnectionDraining'|'MidLifecycleAction'|'WaitingForInstanceWarmup'|'Successful'|'Failed'|'Cancelled',
                'StatusMessage': 'string',
                'Progress': 123,
                'Details': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    AutoScaling.Client.exceptions.InvalidNextToken
    AutoScaling.Client.exceptions.ResourceContentionFault
    
    """
    pass

def describe_scaling_process_types():
    """
    Describes the scaling process types for use with the  ResumeProcesses and  SuspendProcesses APIs.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example describes the Auto Scaling process types.
    Expected Output:
    
    :example: response = client.describe_scaling_process_types()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'Processes': [
        {
            'ProcessName': 'string'
        },
    ]
}


Response Structure

(dict) --
Processes (list) --The names of the process types.

(dict) --Describes a process type.
For more information, see Scaling Processes in the Amazon EC2 Auto Scaling User Guide .

ProcessName (string) --One of the following processes:

Launch
Terminate
AddToLoadBalancer
AlarmNotification
AZRebalance
HealthCheck
ReplaceUnhealthy
ScheduledActions











Exceptions

AutoScaling.Client.exceptions.ResourceContentionFault

Examples
This example describes the Auto Scaling process types.
response = client.describe_scaling_process_types(
)

print(response)


Expected Output:
{
    'Processes': [
        {
            'ProcessName': 'AZRebalance',
        },
        {
            'ProcessName': 'AddToLoadBalancer',
        },
        {
            'ProcessName': 'AlarmNotification',
        },
        {
            'ProcessName': 'HealthCheck',
        },
        {
            'ProcessName': 'Launch',
        },
        {
            'ProcessName': 'ReplaceUnhealthy',
        },
        {
            'ProcessName': 'ScheduledActions',
        },
        {
            'ProcessName': 'Terminate',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Processes': [
            {
                'ProcessName': 'string'
            },
        ]
    }
    
    
    :returns: 
    AutoScaling.Client.exceptions.ResourceContentionFault
    
    """
    pass

def describe_scheduled_actions(AutoScalingGroupName=None, ScheduledActionNames=None, StartTime=None, EndTime=None, NextToken=None, MaxRecords=None):
    """
    Describes the actions scheduled for your Auto Scaling group that haven\'t run or that have not reached their end time. To describe the actions that have already run, call the  DescribeScalingActivities API.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example describes the scheduled actions for the specified Auto Scaling group.
    Expected Output:
    
    :example: response = client.describe_scheduled_actions(
        AutoScalingGroupName='string',
        ScheduledActionNames=[
            'string',
        ],
        StartTime=datetime(2015, 1, 1),
        EndTime=datetime(2015, 1, 1),
        NextToken='string',
        MaxRecords=123
    )
    
    
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: The name of the Auto Scaling group.

    :type ScheduledActionNames: list
    :param ScheduledActionNames: The names of one or more scheduled actions. You can specify up to 50 actions. If you omit this parameter, all scheduled actions are described. If you specify an unknown scheduled action, it is ignored with no error.\n\n(string) --\n\n

    :type StartTime: datetime
    :param StartTime: The earliest scheduled start time to return. If scheduled action names are provided, this parameter is ignored.

    :type EndTime: datetime
    :param EndTime: The latest scheduled start time to return. If scheduled action names are provided, this parameter is ignored.

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of items to return with this call. The default value is 50 and the maximum value is 100 .

    :rtype: dict

ReturnsResponse Syntax
{
    'ScheduledUpdateGroupActions': [
        {
            'AutoScalingGroupName': 'string',
            'ScheduledActionName': 'string',
            'ScheduledActionARN': 'string',
            'Time': datetime(2015, 1, 1),
            'StartTime': datetime(2015, 1, 1),
            'EndTime': datetime(2015, 1, 1),
            'Recurrence': 'string',
            'MinSize': 123,
            'MaxSize': 123,
            'DesiredCapacity': 123
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

ScheduledUpdateGroupActions (list) --
The scheduled actions.

(dict) --
Describes a scheduled scaling action.

AutoScalingGroupName (string) --
The name of the Auto Scaling group.

ScheduledActionName (string) --
The name of the scheduled action.

ScheduledActionARN (string) --
The Amazon Resource Name (ARN) of the scheduled action.

Time (datetime) --
This parameter is no longer used.

StartTime (datetime) --
The date and time in UTC for this action to start. For example, "2019-06-01T00:00:00Z" .

EndTime (datetime) --
The date and time in UTC for the recurring schedule to end. For example, "2019-06-01T00:00:00Z" .

Recurrence (string) --
The recurring schedule for the action, in Unix cron syntax format.
When StartTime and EndTime are specified with Recurrence , they form the boundaries of when the recurring action starts and stops.

MinSize (integer) --
The minimum size of the Auto Scaling group.

MaxSize (integer) --
The maximum size of the Auto Scaling group.

DesiredCapacity (integer) --
The desired capacity is the initial capacity of the Auto Scaling group after the scheduled action runs and the capacity it attempts to maintain.





NextToken (string) --
A string that indicates that the response contains more items than can be returned in a single response. To receive additional items, specify this string for the NextToken value when requesting the next set of items. This value is null when there are no more items to return.







Exceptions

AutoScaling.Client.exceptions.InvalidNextToken
AutoScaling.Client.exceptions.ResourceContentionFault

Examples
This example describes the scheduled actions for the specified Auto Scaling group.
response = client.describe_scheduled_actions(
    AutoScalingGroupName='my-auto-scaling-group',
)

print(response)


Expected Output:
{
    'ScheduledUpdateGroupActions': [
        {
            'AutoScalingGroupName': 'my-auto-scaling-group',
            'DesiredCapacity': 4,
            'MaxSize': 6,
            'MinSize': 2,
            'Recurrence': '30 0 1 12 0',
            'ScheduledActionARN': 'arn:aws:autoscaling:us-west-2:123456789012:scheduledUpdateGroupAction:8e86b655-b2e6-4410-8f29-b4f094d6871c:autoScalingGroupName/my-auto-scaling-group:scheduledActionName/my-scheduled-action',
            'ScheduledActionName': 'my-scheduled-action',
            'StartTime': datetime(2016, 12, 1, 0, 30, 0, 3, 336, 0),
            'Time': datetime(2016, 12, 1, 0, 30, 0, 3, 336, 0),
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ScheduledUpdateGroupActions': [
            {
                'AutoScalingGroupName': 'string',
                'ScheduledActionName': 'string',
                'ScheduledActionARN': 'string',
                'Time': datetime(2015, 1, 1),
                'StartTime': datetime(2015, 1, 1),
                'EndTime': datetime(2015, 1, 1),
                'Recurrence': 'string',
                'MinSize': 123,
                'MaxSize': 123,
                'DesiredCapacity': 123
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    AutoScaling.Client.exceptions.InvalidNextToken
    AutoScaling.Client.exceptions.ResourceContentionFault
    
    """
    pass

def describe_tags(Filters=None, NextToken=None, MaxRecords=None):
    """
    Describes the specified tags.
    You can use filters to limit the results. For example, you can query for the tags for a specific Auto Scaling group. You can specify multiple values for a filter. A tag must match at least one of the specified values for it to be included in the results.
    You can also specify multiple filters. The result includes information for a particular tag only if it matches all the filters. If there\'s no match, no special message is returned.
    For more information, see Tagging Auto Scaling Groups and Instances in the Amazon EC2 Auto Scaling User Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example describes the tags for the specified Auto Scaling group.
    Expected Output:
    
    :example: response = client.describe_tags(
        Filters=[
            {
                'Name': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        NextToken='string',
        MaxRecords=123
    )
    
    
    :type Filters: list
    :param Filters: One or more filters to scope the tags to return. The maximum number of filters per filter type (for example, auto-scaling-group ) is 1000.\n\n(dict) --Describes a filter that is used to return a more specific list of results when describing tags.\nFor more information, see Tagging Auto Scaling Groups and Instances in the Amazon EC2 Auto Scaling User Guide .\n\nName (string) --The name of the filter. The valid values are: auto-scaling-group , key , value , and propagate-at-launch .\n\nValues (list) --One or more filter values. Filter values are case-sensitive.\n\n(string) --\n\n\n\n\n\n

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of items to return with this call. The default value is 50 and the maximum value is 100 .

    :rtype: dict

ReturnsResponse Syntax
{
    'Tags': [
        {
            'ResourceId': 'string',
            'ResourceType': 'string',
            'Key': 'string',
            'Value': 'string',
            'PropagateAtLaunch': True|False
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Tags (list) --
One or more tags.

(dict) --
Describes a tag for an Auto Scaling group.

ResourceId (string) --
The name of the group.

ResourceType (string) --
The type of resource. The only supported value is auto-scaling-group .

Key (string) --
The tag key.

Value (string) --
The tag value.

PropagateAtLaunch (boolean) --
Determines whether the tag is added to new instances as they are launched in the group.





NextToken (string) --
A string that indicates that the response contains more items than can be returned in a single response. To receive additional items, specify this string for the NextToken value when requesting the next set of items. This value is null when there are no more items to return.







Exceptions

AutoScaling.Client.exceptions.InvalidNextToken
AutoScaling.Client.exceptions.ResourceContentionFault

Examples
This example describes the tags for the specified Auto Scaling group.
response = client.describe_tags(
    Filters=[
        {
            'Name': 'auto-scaling-group',
            'Values': [
                'my-auto-scaling-group',
            ],
        },
    ],
)

print(response)


Expected Output:
{
    'Tags': [
        {
            'Key': 'Dept',
            'PropagateAtLaunch': True,
            'ResourceId': 'my-auto-scaling-group',
            'ResourceType': 'auto-scaling-group',
            'Value': 'Research',
        },
        {
            'Key': 'Role',
            'PropagateAtLaunch': True,
            'ResourceId': 'my-auto-scaling-group',
            'ResourceType': 'auto-scaling-group',
            'Value': 'WebServer',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Tags': [
            {
                'ResourceId': 'string',
                'ResourceType': 'string',
                'Key': 'string',
                'Value': 'string',
                'PropagateAtLaunch': True|False
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    AutoScaling.Client.exceptions.InvalidNextToken
    AutoScaling.Client.exceptions.ResourceContentionFault
    
    """
    pass

def describe_termination_policy_types():
    """
    Describes the termination policies supported by Amazon EC2 Auto Scaling.
    For more information, see Controlling Which Auto Scaling Instances Terminate During Scale In in the Amazon EC2 Auto Scaling User Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example describes the available termination policy types.
    Expected Output:
    
    :example: response = client.describe_termination_policy_types()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'TerminationPolicyTypes': [
        'string',
    ]
}


Response Structure

(dict) --
TerminationPolicyTypes (list) --The termination policies supported by Amazon EC2 Auto Scaling: OldestInstance , OldestLaunchConfiguration , NewestInstance , ClosestToNextInstanceHour , Default , OldestLaunchTemplate , and AllocationStrategy .

(string) --







Exceptions

AutoScaling.Client.exceptions.ResourceContentionFault

Examples
This example describes the available termination policy types.
response = client.describe_termination_policy_types(
)

print(response)


Expected Output:
{
    'TerminationPolicyTypes': [
        'ClosestToNextInstanceHour',
        'Default',
        'NewestInstance',
        'OldestInstance',
        'OldestLaunchConfiguration',
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'TerminationPolicyTypes': [
            'string',
        ]
    }
    
    
    :returns: 
    AutoScaling.Client.exceptions.ResourceContentionFault
    
    """
    pass

def detach_instances(InstanceIds=None, AutoScalingGroupName=None, ShouldDecrementDesiredCapacity=None):
    """
    Removes one or more instances from the specified Auto Scaling group.
    After the instances are detached, you can manage them independent of the Auto Scaling group.
    If you do not specify the option to decrement the desired capacity, Amazon EC2 Auto Scaling launches instances to replace the ones that are detached.
    If there is a Classic Load Balancer attached to the Auto Scaling group, the instances are deregistered from the load balancer. If there are target groups attached to the Auto Scaling group, the instances are deregistered from the target groups.
    For more information, see Detach EC2 Instances from Your Auto Scaling Group in the Amazon EC2 Auto Scaling User Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example detaches the specified instance from the specified Auto Scaling group.
    Expected Output:
    
    :example: response = client.detach_instances(
        InstanceIds=[
            'string',
        ],
        AutoScalingGroupName='string',
        ShouldDecrementDesiredCapacity=True|False
    )
    
    
    :type InstanceIds: list
    :param InstanceIds: The IDs of the instances. You can specify up to 20 instances.\n\n(string) --\n\n

    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: [REQUIRED]\nThe name of the Auto Scaling group.\n

    :type ShouldDecrementDesiredCapacity: boolean
    :param ShouldDecrementDesiredCapacity: [REQUIRED]\nIndicates whether the Auto Scaling group decrements the desired capacity value by the number of instances detached.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Activities': [
        {
            'ActivityId': 'string',
            'AutoScalingGroupName': 'string',
            'Description': 'string',
            'Cause': 'string',
            'StartTime': datetime(2015, 1, 1),
            'EndTime': datetime(2015, 1, 1),
            'StatusCode': 'PendingSpotBidPlacement'|'WaitingForSpotInstanceRequestId'|'WaitingForSpotInstanceId'|'WaitingForInstanceId'|'PreInService'|'InProgress'|'WaitingForELBConnectionDraining'|'MidLifecycleAction'|'WaitingForInstanceWarmup'|'Successful'|'Failed'|'Cancelled',
            'StatusMessage': 'string',
            'Progress': 123,
            'Details': 'string'
        },
    ]
}


Response Structure

(dict) --

Activities (list) --
The activities related to detaching the instances from the Auto Scaling group.

(dict) --
Describes scaling activity, which is a long-running process that represents a change to your Auto Scaling group, such as changing its size or replacing an instance.

ActivityId (string) --
The ID of the activity.

AutoScalingGroupName (string) --
The name of the Auto Scaling group.

Description (string) --
A friendly, more verbose description of the activity.

Cause (string) --
The reason the activity began.

StartTime (datetime) --
The start time of the activity.

EndTime (datetime) --
The end time of the activity.

StatusCode (string) --
The current status of the activity.

StatusMessage (string) --
A friendly, more verbose description of the activity status.

Progress (integer) --
A value between 0 and 100 that indicates the progress of the activity.

Details (string) --
The details about the activity.











Exceptions

AutoScaling.Client.exceptions.ResourceContentionFault

Examples
This example detaches the specified instance from the specified Auto Scaling group.
response = client.detach_instances(
    AutoScalingGroupName='my-auto-scaling-group',
    InstanceIds=[
        'i-93633f9b',
    ],
    ShouldDecrementDesiredCapacity=True,
)

print(response)


Expected Output:
{
    'Activities': [
        {
            'ActivityId': '5091cb52-547a-47ce-a236-c9ccbc2cb2c9',
            'AutoScalingGroupName': 'my-auto-scaling-group',
            'Cause': 'At 2015-04-12T15:02:16Z instance i-93633f9b was detached in response to a user request, shrinking the capacity from 2 to 1.',
            'Description': 'Detaching EC2 instance: i-93633f9b',
            'Details': 'details',
            'Progress': 50,
            'StartTime': datetime(2015, 4, 12, 15, 2, 16, 6, 102, 0),
            'StatusCode': 'InProgress',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Activities': [
            {
                'ActivityId': 'string',
                'AutoScalingGroupName': 'string',
                'Description': 'string',
                'Cause': 'string',
                'StartTime': datetime(2015, 1, 1),
                'EndTime': datetime(2015, 1, 1),
                'StatusCode': 'PendingSpotBidPlacement'|'WaitingForSpotInstanceRequestId'|'WaitingForSpotInstanceId'|'WaitingForInstanceId'|'PreInService'|'InProgress'|'WaitingForELBConnectionDraining'|'MidLifecycleAction'|'WaitingForInstanceWarmup'|'Successful'|'Failed'|'Cancelled',
                'StatusMessage': 'string',
                'Progress': 123,
                'Details': 'string'
            },
        ]
    }
    
    
    :returns: 
    AutoScaling.Client.exceptions.ResourceContentionFault
    
    """
    pass

def detach_load_balancer_target_groups(AutoScalingGroupName=None, TargetGroupARNs=None):
    """
    Detaches one or more target groups from the specified Auto Scaling group.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example detaches the specified target group from the specified Auto Scaling group
    Expected Output:
    
    :example: response = client.detach_load_balancer_target_groups(
        AutoScalingGroupName='string',
        TargetGroupARNs=[
            'string',
        ]
    )
    
    
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: [REQUIRED]\nThe name of the Auto Scaling group.\n

    :type TargetGroupARNs: list
    :param TargetGroupARNs: [REQUIRED]\nThe Amazon Resource Names (ARN) of the target groups. You can specify up to 10 target groups.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

AutoScaling.Client.exceptions.ResourceContentionFault

Examples
This example detaches the specified target group from the specified Auto Scaling group
response = client.detach_load_balancer_target_groups(
    AutoScalingGroupName='my-auto-scaling-group',
    TargetGroupARNs=[
        'arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067',
    ],
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

def detach_load_balancers(AutoScalingGroupName=None, LoadBalancerNames=None):
    """
    Detaches one or more Classic Load Balancers from the specified Auto Scaling group.
    This operation detaches only Classic Load Balancers. If you have Application Load Balancers or Network Load Balancers, use the  DetachLoadBalancerTargetGroups API instead.
    When you detach a load balancer, it enters the Removing state while deregistering the instances in the group. When all instances are deregistered, then you can no longer describe the load balancer using the  DescribeLoadBalancers API call. The instances remain running.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example detaches the specified load balancer from the specified Auto Scaling group.
    Expected Output:
    
    :example: response = client.detach_load_balancers(
        AutoScalingGroupName='string',
        LoadBalancerNames=[
            'string',
        ]
    )
    
    
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: [REQUIRED]\nThe name of the Auto Scaling group.\n

    :type LoadBalancerNames: list
    :param LoadBalancerNames: [REQUIRED]\nThe names of the load balancers. You can specify up to 10 load balancers.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

AutoScaling.Client.exceptions.ResourceContentionFault

Examples
This example detaches the specified load balancer from the specified Auto Scaling group.
response = client.detach_load_balancers(
    AutoScalingGroupName='my-auto-scaling-group',
    LoadBalancerNames=[
        'my-load-balancer',
    ],
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

def disable_metrics_collection(AutoScalingGroupName=None, Metrics=None):
    """
    Disables group metrics for the specified Auto Scaling group.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example disables collecting data for the GroupDesiredCapacity metric for the specified Auto Scaling group.
    Expected Output:
    
    :example: response = client.disable_metrics_collection(
        AutoScalingGroupName='string',
        Metrics=[
            'string',
        ]
    )
    
    
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: [REQUIRED]\nThe name of the Auto Scaling group.\n

    :type Metrics: list
    :param Metrics: Specifies one or more of the following metrics:\n\nGroupMinSize\nGroupMaxSize\nGroupDesiredCapacity\nGroupInServiceInstances\nGroupPendingInstances\nGroupStandbyInstances\nGroupTerminatingInstances\nGroupTotalInstances\nGroupInServiceCapacity\nGroupPendingCapacity\nGroupStandbyCapacity\nGroupTerminatingCapacity\nGroupTotalCapacity\n\nIf you omit this parameter, all metrics are disabled.\n\n(string) --\n\n

    :return: response = client.disable_metrics_collection(
        AutoScalingGroupName='my-auto-scaling-group',
        Metrics=[
            'GroupDesiredCapacity',
        ],
    )
    
    print(response)
    
    
    :returns: 
    AutoScaling.Client.exceptions.ResourceContentionFault
    
    """
    pass

def enable_metrics_collection(AutoScalingGroupName=None, Metrics=None, Granularity=None):
    """
    Enables group metrics for the specified Auto Scaling group. For more information, see Monitoring Your Auto Scaling Groups and Instances in the Amazon EC2 Auto Scaling User Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example enables data collection for the specified Auto Scaling group.
    Expected Output:
    
    :example: response = client.enable_metrics_collection(
        AutoScalingGroupName='string',
        Metrics=[
            'string',
        ],
        Granularity='string'
    )
    
    
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: [REQUIRED]\nThe name of the Auto Scaling group.\n

    :type Metrics: list
    :param Metrics: Specifies which group-level metrics to start collecting. You can specify one or more of the following metrics:\n\nGroupMinSize\nGroupMaxSize\nGroupDesiredCapacity\nGroupInServiceInstances\nGroupPendingInstances\nGroupStandbyInstances\nGroupTerminatingInstances\nGroupTotalInstances\n\nThe instance weighting feature supports the following additional metrics:\n\nGroupInServiceCapacity\nGroupPendingCapacity\nGroupStandbyCapacity\nGroupTerminatingCapacity\nGroupTotalCapacity\n\nIf you omit this parameter, all metrics are enabled.\n\n(string) --\n\n

    :type Granularity: string
    :param Granularity: [REQUIRED]\nThe granularity to associate with the metrics to collect. The only valid value is 1Minute .\n

    :return: response = client.enable_metrics_collection(
        AutoScalingGroupName='my-auto-scaling-group',
        Granularity='1Minute',
    )
    
    print(response)
    
    
    :returns: 
    AutoScaling.Client.exceptions.ResourceContentionFault
    
    """
    pass

def enter_standby(InstanceIds=None, AutoScalingGroupName=None, ShouldDecrementDesiredCapacity=None):
    """
    Moves the specified instances into the standby state.
    If you choose to decrement the desired capacity of the Auto Scaling group, the instances can enter standby as long as the desired capacity of the Auto Scaling group after the instances are placed into standby is equal to or greater than the minimum capacity of the group.
    If you choose not to decrement the desired capacity of the Auto Scaling group, the Auto Scaling group launches new instances to replace the instances on standby.
    For more information, see Temporarily Removing Instances from Your Auto Scaling Group in the Amazon EC2 Auto Scaling User Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example puts the specified instance into standby mode.
    Expected Output:
    
    :example: response = client.enter_standby(
        InstanceIds=[
            'string',
        ],
        AutoScalingGroupName='string',
        ShouldDecrementDesiredCapacity=True|False
    )
    
    
    :type InstanceIds: list
    :param InstanceIds: The IDs of the instances. You can specify up to 20 instances.\n\n(string) --\n\n

    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: [REQUIRED]\nThe name of the Auto Scaling group.\n

    :type ShouldDecrementDesiredCapacity: boolean
    :param ShouldDecrementDesiredCapacity: [REQUIRED]\nIndicates whether to decrement the desired capacity of the Auto Scaling group by the number of instances moved to Standby mode.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Activities': [
        {
            'ActivityId': 'string',
            'AutoScalingGroupName': 'string',
            'Description': 'string',
            'Cause': 'string',
            'StartTime': datetime(2015, 1, 1),
            'EndTime': datetime(2015, 1, 1),
            'StatusCode': 'PendingSpotBidPlacement'|'WaitingForSpotInstanceRequestId'|'WaitingForSpotInstanceId'|'WaitingForInstanceId'|'PreInService'|'InProgress'|'WaitingForELBConnectionDraining'|'MidLifecycleAction'|'WaitingForInstanceWarmup'|'Successful'|'Failed'|'Cancelled',
            'StatusMessage': 'string',
            'Progress': 123,
            'Details': 'string'
        },
    ]
}


Response Structure

(dict) --

Activities (list) --
The activities related to moving instances into Standby mode.

(dict) --
Describes scaling activity, which is a long-running process that represents a change to your Auto Scaling group, such as changing its size or replacing an instance.

ActivityId (string) --
The ID of the activity.

AutoScalingGroupName (string) --
The name of the Auto Scaling group.

Description (string) --
A friendly, more verbose description of the activity.

Cause (string) --
The reason the activity began.

StartTime (datetime) --
The start time of the activity.

EndTime (datetime) --
The end time of the activity.

StatusCode (string) --
The current status of the activity.

StatusMessage (string) --
A friendly, more verbose description of the activity status.

Progress (integer) --
A value between 0 and 100 that indicates the progress of the activity.

Details (string) --
The details about the activity.











Exceptions

AutoScaling.Client.exceptions.ResourceContentionFault

Examples
This example puts the specified instance into standby mode.
response = client.enter_standby(
    AutoScalingGroupName='my-auto-scaling-group',
    InstanceIds=[
        'i-93633f9b',
    ],
    ShouldDecrementDesiredCapacity=True,
)

print(response)


Expected Output:
{
    'Activities': [
        {
            'ActivityId': 'ffa056b4-6ed3-41ba-ae7c-249dfae6eba1',
            'AutoScalingGroupName': 'my-auto-scaling-group',
            'Cause': 'At 2015-04-12T15:10:23Z instance i-93633f9b was moved to standby in response to a user request, shrinking the capacity from 2 to 1.',
            'Description': 'Moving EC2 instance to Standby: i-93633f9b',
            'Details': 'details',
            'Progress': 50,
            'StartTime': datetime(2015, 4, 12, 15, 10, 23, 6, 102, 0),
            'StatusCode': 'InProgress',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Activities': [
            {
                'ActivityId': 'string',
                'AutoScalingGroupName': 'string',
                'Description': 'string',
                'Cause': 'string',
                'StartTime': datetime(2015, 1, 1),
                'EndTime': datetime(2015, 1, 1),
                'StatusCode': 'PendingSpotBidPlacement'|'WaitingForSpotInstanceRequestId'|'WaitingForSpotInstanceId'|'WaitingForInstanceId'|'PreInService'|'InProgress'|'WaitingForELBConnectionDraining'|'MidLifecycleAction'|'WaitingForInstanceWarmup'|'Successful'|'Failed'|'Cancelled',
                'StatusMessage': 'string',
                'Progress': 123,
                'Details': 'string'
            },
        ]
    }
    
    
    :returns: 
    AutoScaling.Client.exceptions.ResourceContentionFault
    
    """
    pass

def execute_policy(AutoScalingGroupName=None, PolicyName=None, HonorCooldown=None, MetricValue=None, BreachThreshold=None):
    """
    Executes the specified policy.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example executes the specified Auto Scaling policy for the specified Auto Scaling group.
    Expected Output:
    
    :example: response = client.execute_policy(
        AutoScalingGroupName='string',
        PolicyName='string',
        HonorCooldown=True|False,
        MetricValue=123.0,
        BreachThreshold=123.0
    )
    
    
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: The name of the Auto Scaling group.

    :type PolicyName: string
    :param PolicyName: [REQUIRED]\nThe name or ARN of the policy.\n

    :type HonorCooldown: boolean
    :param HonorCooldown: Indicates whether Amazon EC2 Auto Scaling waits for the cooldown period to complete before executing the policy.\nThis parameter is not supported if the policy type is StepScaling or TargetTrackingScaling .\nFor more information, see Scaling Cooldowns in the Amazon EC2 Auto Scaling User Guide .\n

    :type MetricValue: float
    :param MetricValue: The metric value to compare to BreachThreshold . This enables you to execute a policy of type StepScaling and determine which step adjustment to use. For example, if the breach threshold is 50 and you want to use a step adjustment with a lower bound of 0 and an upper bound of 10, you can set the metric value to 59.\nIf you specify a metric value that doesn\'t correspond to a step adjustment for the policy, the call returns an error.\nConditional: This parameter is required if the policy type is StepScaling and not supported otherwise.\n

    :type BreachThreshold: float
    :param BreachThreshold: The breach threshold for the alarm.\nConditional: This parameter is required if the policy type is StepScaling and not supported otherwise.\n

    :return: response = client.execute_policy(
        AutoScalingGroupName='my-auto-scaling-group',
        HonorCooldown=True,
        PolicyName='ScaleIn',
    )
    
    print(response)
    
    
    :returns: 
    AutoScaling.Client.exceptions.ScalingActivityInProgressFault
    AutoScaling.Client.exceptions.ResourceContentionFault
    
    """
    pass

def exit_standby(InstanceIds=None, AutoScalingGroupName=None):
    """
    Moves the specified instances out of the standby state.
    After you put the instances back in service, the desired capacity is incremented.
    For more information, see Temporarily Removing Instances from Your Auto Scaling Group in the Amazon EC2 Auto Scaling User Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example moves the specified instance out of standby mode.
    Expected Output:
    
    :example: response = client.exit_standby(
        InstanceIds=[
            'string',
        ],
        AutoScalingGroupName='string'
    )
    
    
    :type InstanceIds: list
    :param InstanceIds: The IDs of the instances. You can specify up to 20 instances.\n\n(string) --\n\n

    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: [REQUIRED]\nThe name of the Auto Scaling group.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Activities': [
        {
            'ActivityId': 'string',
            'AutoScalingGroupName': 'string',
            'Description': 'string',
            'Cause': 'string',
            'StartTime': datetime(2015, 1, 1),
            'EndTime': datetime(2015, 1, 1),
            'StatusCode': 'PendingSpotBidPlacement'|'WaitingForSpotInstanceRequestId'|'WaitingForSpotInstanceId'|'WaitingForInstanceId'|'PreInService'|'InProgress'|'WaitingForELBConnectionDraining'|'MidLifecycleAction'|'WaitingForInstanceWarmup'|'Successful'|'Failed'|'Cancelled',
            'StatusMessage': 'string',
            'Progress': 123,
            'Details': 'string'
        },
    ]
}


Response Structure

(dict) --

Activities (list) --
The activities related to moving instances out of Standby mode.

(dict) --
Describes scaling activity, which is a long-running process that represents a change to your Auto Scaling group, such as changing its size or replacing an instance.

ActivityId (string) --
The ID of the activity.

AutoScalingGroupName (string) --
The name of the Auto Scaling group.

Description (string) --
A friendly, more verbose description of the activity.

Cause (string) --
The reason the activity began.

StartTime (datetime) --
The start time of the activity.

EndTime (datetime) --
The end time of the activity.

StatusCode (string) --
The current status of the activity.

StatusMessage (string) --
A friendly, more verbose description of the activity status.

Progress (integer) --
A value between 0 and 100 that indicates the progress of the activity.

Details (string) --
The details about the activity.











Exceptions

AutoScaling.Client.exceptions.ResourceContentionFault

Examples
This example moves the specified instance out of standby mode.
response = client.exit_standby(
    AutoScalingGroupName='my-auto-scaling-group',
    InstanceIds=[
        'i-93633f9b',
    ],
)

print(response)


Expected Output:
{
    'Activities': [
        {
            'ActivityId': '142928e1-a2dc-453a-9b24-b85ad6735928',
            'AutoScalingGroupName': 'my-auto-scaling-group',
            'Cause': 'At 2015-04-12T15:14:29Z instance i-93633f9b was moved out of standby in response to a user request, increasing the capacity from 1 to 2.',
            'Description': 'Moving EC2 instance out of Standby: i-93633f9b',
            'Details': 'details',
            'Progress': 30,
            'StartTime': datetime(2015, 4, 12, 15, 14, 29, 6, 102, 0),
            'StatusCode': 'PreInService',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Activities': [
            {
                'ActivityId': 'string',
                'AutoScalingGroupName': 'string',
                'Description': 'string',
                'Cause': 'string',
                'StartTime': datetime(2015, 1, 1),
                'EndTime': datetime(2015, 1, 1),
                'StatusCode': 'PendingSpotBidPlacement'|'WaitingForSpotInstanceRequestId'|'WaitingForSpotInstanceId'|'WaitingForInstanceId'|'PreInService'|'InProgress'|'WaitingForELBConnectionDraining'|'MidLifecycleAction'|'WaitingForInstanceWarmup'|'Successful'|'Failed'|'Cancelled',
                'StatusMessage': 'string',
                'Progress': 123,
                'Details': 'string'
            },
        ]
    }
    
    
    :returns: 
    AutoScaling.Client.exceptions.ResourceContentionFault
    
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

def put_lifecycle_hook(LifecycleHookName=None, AutoScalingGroupName=None, LifecycleTransition=None, RoleARN=None, NotificationTargetARN=None, NotificationMetadata=None, HeartbeatTimeout=None, DefaultResult=None):
    """
    Creates or updates a lifecycle hook for the specified Auto Scaling group.
    A lifecycle hook tells Amazon EC2 Auto Scaling to perform an action on an instance when the instance launches (before it is put into service) or as the instance terminates (before it is fully terminated).
    This step is a part of the procedure for adding a lifecycle hook to an Auto Scaling group:
    For more information, see Amazon EC2 Auto Scaling Lifecycle Hooks in the Amazon EC2 Auto Scaling User Guide .
    If you exceed your maximum limit of lifecycle hooks, which by default is 50 per Auto Scaling group, the call fails.
    You can view the lifecycle hooks for an Auto Scaling group using the  DescribeLifecycleHooks API call. If you are no longer using a lifecycle hook, you can delete it by calling the  DeleteLifecycleHook API.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example creates a lifecycle hook.
    Expected Output:
    
    :example: response = client.put_lifecycle_hook(
        LifecycleHookName='string',
        AutoScalingGroupName='string',
        LifecycleTransition='string',
        RoleARN='string',
        NotificationTargetARN='string',
        NotificationMetadata='string',
        HeartbeatTimeout=123,
        DefaultResult='string'
    )
    
    
    :type LifecycleHookName: string
    :param LifecycleHookName: [REQUIRED]\nThe name of the lifecycle hook.\n

    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: [REQUIRED]\nThe name of the Auto Scaling group.\n

    :type LifecycleTransition: string
    :param LifecycleTransition: The instance state to which you want to attach the lifecycle hook. The valid values are:\n\nautoscaling:EC2_INSTANCE_LAUNCHING\nautoscaling:EC2_INSTANCE_TERMINATING\n\nConditional: This parameter is required for new lifecycle hooks, but optional when updating existing hooks.\n

    :type RoleARN: string
    :param RoleARN: The ARN of the IAM role that allows the Auto Scaling group to publish to the specified notification target, for example, an Amazon SNS topic or an Amazon SQS queue.\nConditional: This parameter is required for new lifecycle hooks, but optional when updating existing hooks.\n

    :type NotificationTargetARN: string
    :param NotificationTargetARN: The ARN of the notification target that Amazon EC2 Auto Scaling uses to notify you when an instance is in the transition state for the lifecycle hook. This target can be either an SQS queue or an SNS topic.\nIf you specify an empty string, this overrides the current ARN.\nThis operation uses the JSON format when sending notifications to an Amazon SQS queue, and an email key-value pair format when sending notifications to an Amazon SNS topic.\nWhen you specify a notification target, Amazon EC2 Auto Scaling sends it a test message. Test messages contain the following additional key-value pair: 'Event': 'autoscaling:TEST_NOTIFICATION' .\n

    :type NotificationMetadata: string
    :param NotificationMetadata: Additional information that you want to include any time Amazon EC2 Auto Scaling sends a message to the notification target.

    :type HeartbeatTimeout: integer
    :param HeartbeatTimeout: The maximum time, in seconds, that can elapse before the lifecycle hook times out. The range is from 30 to 7200 seconds. The default value is 3600 seconds (1 hour).\nIf the lifecycle hook times out, Amazon EC2 Auto Scaling performs the action that you specified in the DefaultResult parameter. You can prevent the lifecycle hook from timing out by calling the RecordLifecycleActionHeartbeat API.\n

    :type DefaultResult: string
    :param DefaultResult: Defines the action the Auto Scaling group should take when the lifecycle hook timeout elapses or if an unexpected failure occurs. This parameter can be either CONTINUE or ABANDON . The default value is ABANDON .

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

AutoScaling.Client.exceptions.LimitExceededFault
AutoScaling.Client.exceptions.ResourceContentionFault

Examples
This example creates a lifecycle hook.
response = client.put_lifecycle_hook(
    AutoScalingGroupName='my-auto-scaling-group',
    LifecycleHookName='my-lifecycle-hook',
    LifecycleTransition='autoscaling:EC2_INSTANCE_LAUNCHING',
    NotificationTargetARN='arn:aws:sns:us-west-2:123456789012:my-sns-topic --role-arn',
    RoleARN='arn:aws:iam::123456789012:role/my-auto-scaling-role',
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
    LifecycleHookName (string) -- [REQUIRED]
    The name of the lifecycle hook.
    
    AutoScalingGroupName (string) -- [REQUIRED]
    The name of the Auto Scaling group.
    
    LifecycleTransition (string) -- The instance state to which you want to attach the lifecycle hook. The valid values are:
    
    autoscaling:EC2_INSTANCE_LAUNCHING
    autoscaling:EC2_INSTANCE_TERMINATING
    
    Conditional: This parameter is required for new lifecycle hooks, but optional when updating existing hooks.
    
    RoleARN (string) -- The ARN of the IAM role that allows the Auto Scaling group to publish to the specified notification target, for example, an Amazon SNS topic or an Amazon SQS queue.
    Conditional: This parameter is required for new lifecycle hooks, but optional when updating existing hooks.
    
    NotificationTargetARN (string) -- The ARN of the notification target that Amazon EC2 Auto Scaling uses to notify you when an instance is in the transition state for the lifecycle hook. This target can be either an SQS queue or an SNS topic.
    If you specify an empty string, this overrides the current ARN.
    This operation uses the JSON format when sending notifications to an Amazon SQS queue, and an email key-value pair format when sending notifications to an Amazon SNS topic.
    When you specify a notification target, Amazon EC2 Auto Scaling sends it a test message. Test messages contain the following additional key-value pair: "Event": "autoscaling:TEST_NOTIFICATION" .
    
    NotificationMetadata (string) -- Additional information that you want to include any time Amazon EC2 Auto Scaling sends a message to the notification target.
    HeartbeatTimeout (integer) -- The maximum time, in seconds, that can elapse before the lifecycle hook times out. The range is from 30 to 7200 seconds. The default value is 3600 seconds (1 hour).
    If the lifecycle hook times out, Amazon EC2 Auto Scaling performs the action that you specified in the DefaultResult parameter. You can prevent the lifecycle hook from timing out by calling the  RecordLifecycleActionHeartbeat API.
    
    DefaultResult (string) -- Defines the action the Auto Scaling group should take when the lifecycle hook timeout elapses or if an unexpected failure occurs. This parameter can be either CONTINUE or ABANDON . The default value is ABANDON .
    
    """
    pass

def put_notification_configuration(AutoScalingGroupName=None, TopicARN=None, NotificationTypes=None):
    """
    Configures an Auto Scaling group to send notifications when specified events take place. Subscribers to the specified topic can have messages delivered to an endpoint such as a web server or an email address.
    This configuration overwrites any existing configuration.
    For more information, see Getting Amazon SNS Notifications When Your Auto Scaling Group Scales in the Amazon EC2 Auto Scaling User Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example adds the specified notification to the specified Auto Scaling group.
    Expected Output:
    
    :example: response = client.put_notification_configuration(
        AutoScalingGroupName='string',
        TopicARN='string',
        NotificationTypes=[
            'string',
        ]
    )
    
    
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: [REQUIRED]\nThe name of the Auto Scaling group.\n

    :type TopicARN: string
    :param TopicARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the Amazon Simple Notification Service (Amazon SNS) topic.\n

    :type NotificationTypes: list
    :param NotificationTypes: [REQUIRED]\nThe type of event that causes the notification to be sent. To query the notification types supported by Amazon EC2 Auto Scaling, call the DescribeAutoScalingNotificationTypes API.\n\n(string) --\n\n

    :return: response = client.put_notification_configuration(
        AutoScalingGroupName='my-auto-scaling-group',
        NotificationTypes=[
            'autoscaling:TEST_NOTIFICATION',
        ],
        TopicARN='arn:aws:sns:us-west-2:123456789012:my-sns-topic',
    )
    
    print(response)
    
    
    :returns: 
    AutoScaling.Client.exceptions.LimitExceededFault
    AutoScaling.Client.exceptions.ResourceContentionFault
    AutoScaling.Client.exceptions.ServiceLinkedRoleFailure
    
    """
    pass

def put_scaling_policy(AutoScalingGroupName=None, PolicyName=None, PolicyType=None, AdjustmentType=None, MinAdjustmentStep=None, MinAdjustmentMagnitude=None, ScalingAdjustment=None, Cooldown=None, MetricAggregationType=None, StepAdjustments=None, EstimatedInstanceWarmup=None, TargetTrackingConfiguration=None, Enabled=None):
    """
    Creates or updates a scaling policy for an Auto Scaling group.
    For more information about using scaling policies to scale your Auto Scaling group, see Target Tracking Scaling Policies and Step and Simple Scaling Policies in the Amazon EC2 Auto Scaling User Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example adds the specified policy to the specified Auto Scaling group.
    Expected Output:
    
    :example: response = client.put_scaling_policy(
        AutoScalingGroupName='string',
        PolicyName='string',
        PolicyType='string',
        AdjustmentType='string',
        MinAdjustmentStep=123,
        MinAdjustmentMagnitude=123,
        ScalingAdjustment=123,
        Cooldown=123,
        MetricAggregationType='string',
        StepAdjustments=[
            {
                'MetricIntervalLowerBound': 123.0,
                'MetricIntervalUpperBound': 123.0,
                'ScalingAdjustment': 123
            },
        ],
        EstimatedInstanceWarmup=123,
        TargetTrackingConfiguration={
            'PredefinedMetricSpecification': {
                'PredefinedMetricType': 'ASGAverageCPUUtilization'|'ASGAverageNetworkIn'|'ASGAverageNetworkOut'|'ALBRequestCountPerTarget',
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
            'TargetValue': 123.0,
            'DisableScaleIn': True|False
        },
        Enabled=True|False
    )
    
    
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: [REQUIRED]\nThe name of the Auto Scaling group.\n

    :type PolicyName: string
    :param PolicyName: [REQUIRED]\nThe name of the policy.\n

    :type PolicyType: string
    :param PolicyType: The policy type. The valid values are SimpleScaling , StepScaling , and TargetTrackingScaling . If the policy type is null, the value is treated as SimpleScaling .

    :type AdjustmentType: string
    :param AdjustmentType: Specifies whether the ScalingAdjustment parameter is an absolute number or a percentage of the current capacity. The valid values are ChangeInCapacity , ExactCapacity , and PercentChangeInCapacity .\nValid only if the policy type is StepScaling or SimpleScaling . For more information, see Scaling Adjustment Types in the Amazon EC2 Auto Scaling User Guide .\n

    :type MinAdjustmentStep: integer
    :param MinAdjustmentStep: Available for backward compatibility. Use MinAdjustmentMagnitude instead.

    :type MinAdjustmentMagnitude: integer
    :param MinAdjustmentMagnitude: The minimum value to scale by when scaling by percentages. For example, suppose that you create a step scaling policy to scale out an Auto Scaling group by 25 percent and you specify a MinAdjustmentMagnitude of 2. If the group has 4 instances and the scaling policy is performed, 25 percent of 4 is 1. However, because you specified a MinAdjustmentMagnitude of 2, Amazon EC2 Auto Scaling scales out the group by 2 instances.\nValid only if the policy type is StepScaling or SimpleScaling and the adjustment type is PercentChangeInCapacity . For more information, see Scaling Adjustment Types in the Amazon EC2 Auto Scaling User Guide .\n

    :type ScalingAdjustment: integer
    :param ScalingAdjustment: The amount by which a simple scaling policy scales the Auto Scaling group in response to an alarm breach. The adjustment is based on the value that you specified in the AdjustmentType parameter (either an absolute number or a percentage). A positive value adds to the current capacity and a negative value subtracts from the current capacity. For exact capacity, you must specify a positive value.\nConditional: If you specify SimpleScaling for the policy type, you must specify this parameter. (Not used with any other policy type.)\n

    :type Cooldown: integer
    :param Cooldown: The amount of time, in seconds, after a scaling activity completes before any further dynamic scaling activities can start. If this parameter is not specified, the default cooldown period for the group applies.\nValid only if the policy type is SimpleScaling . For more information, see Scaling Cooldowns in the Amazon EC2 Auto Scaling User Guide .\n

    :type MetricAggregationType: string
    :param MetricAggregationType: The aggregation type for the CloudWatch metrics. The valid values are Minimum , Maximum , and Average . If the aggregation type is null, the value is treated as Average .\nValid only if the policy type is StepScaling .\n

    :type StepAdjustments: list
    :param StepAdjustments: A set of adjustments that enable you to scale based on the size of the alarm breach.\nConditional: If you specify StepScaling for the policy type, you must specify this parameter. (Not used with any other policy type.)\n\n(dict) --Describes information used to create a step adjustment for a step scaling policy.\nFor the following examples, suppose that you have an alarm with a breach threshold of 50:\n\nTo trigger the adjustment when the metric is greater than or equal to 50 and less than 60, specify a lower bound of 0 and an upper bound of 10.\nTo trigger the adjustment when the metric is greater than 40 and less than or equal to 50, specify a lower bound of -10 and an upper bound of 0.\n\nThere are a few rules for the step adjustments for your step policy:\n\nThe ranges of your step adjustments can\'t overlap or have a gap.\nAt most, one step adjustment can have a null lower bound. If one step adjustment has a negative lower bound, then there must be a step adjustment with a null lower bound.\nAt most, one step adjustment can have a null upper bound. If one step adjustment has a positive upper bound, then there must be a step adjustment with a null upper bound.\nThe upper and lower bound can\'t be null in the same step adjustment.\n\nFor more information, see Step Adjustments in the Amazon EC2 Auto Scaling User Guide .\n\nMetricIntervalLowerBound (float) --The lower bound for the difference between the alarm threshold and the CloudWatch metric. If the metric value is above the breach threshold, the lower bound is inclusive (the metric must be greater than or equal to the threshold plus the lower bound). Otherwise, it is exclusive (the metric must be greater than the threshold plus the lower bound). A null value indicates negative infinity.\n\nMetricIntervalUpperBound (float) --The upper bound for the difference between the alarm threshold and the CloudWatch metric. If the metric value is above the breach threshold, the upper bound is exclusive (the metric must be less than the threshold plus the upper bound). Otherwise, it is inclusive (the metric must be less than or equal to the threshold plus the upper bound). A null value indicates positive infinity.\nThe upper bound must be greater than the lower bound.\n\nScalingAdjustment (integer) -- [REQUIRED]The amount by which to scale, based on the specified adjustment type. A positive value adds to the current capacity while a negative number removes from the current capacity.\n\n\n\n\n

    :type EstimatedInstanceWarmup: integer
    :param EstimatedInstanceWarmup: The estimated time, in seconds, until a newly launched instance can contribute to the CloudWatch metrics. The default is to use the value specified for the default cooldown period for the group.\nValid only if the policy type is StepScaling or TargetTrackingScaling .\n

    :type TargetTrackingConfiguration: dict
    :param TargetTrackingConfiguration: A target tracking scaling policy. Includes support for predefined or customized metrics.\nFor more information, see TargetTrackingConfiguration in the Amazon EC2 Auto Scaling API Reference .\nConditional: If you specify TargetTrackingScaling for the policy type, you must specify this parameter. (Not used with any other policy type.)\n\nPredefinedMetricSpecification (dict) --A predefined metric. You must specify either a predefined metric or a customized metric.\n\nPredefinedMetricType (string) -- [REQUIRED]The metric type. The following predefined metrics are available:\n\nASGAverageCPUUtilization - Average CPU utilization of the Auto Scaling group.\nASGAverageNetworkIn - Average number of bytes received on all network interfaces by the Auto Scaling group.\nASGAverageNetworkOut - Average number of bytes sent out on all network interfaces by the Auto Scaling group.\nALBRequestCountPerTarget - Number of requests completed per target in an Application Load Balancer target group.\n\n\nResourceLabel (string) --Identifies the resource associated with the metric type. You can\'t specify a resource label unless the metric type is ALBRequestCountPerTarget and there is a target group attached to the Auto Scaling group.\nThe format is ``app/load-balancer-name /load-balancer-id /targetgroup/target-group-name /target-group-id `` , where\n\n``app/load-balancer-name /load-balancer-id `` is the final portion of the load balancer ARN, and\n``targetgroup/target-group-name /target-group-id `` is the final portion of the target group ARN.\n\n\n\n\nCustomizedMetricSpecification (dict) --A customized metric. You must specify either a predefined metric or a customized metric.\n\nMetricName (string) -- [REQUIRED]The name of the metric.\n\nNamespace (string) -- [REQUIRED]The namespace of the metric.\n\nDimensions (list) --The dimensions of the metric.\nConditional: If you published your metric with dimensions, you must specify the same dimensions in your scaling policy.\n\n(dict) --Describes the dimension of a metric.\n\nName (string) -- [REQUIRED]The name of the dimension.\n\nValue (string) -- [REQUIRED]The value of the dimension.\n\n\n\n\n\nStatistic (string) -- [REQUIRED]The statistic of the metric.\n\nUnit (string) --The unit of the metric.\n\n\n\nTargetValue (float) -- [REQUIRED]The target value for the metric.\n\nDisableScaleIn (boolean) --Indicates whether scaling in by the target tracking scaling policy is disabled. If scaling in is disabled, the target tracking scaling policy doesn\'t remove instances from the Auto Scaling group. Otherwise, the target tracking scaling policy can remove instances from the Auto Scaling group. The default is false .\n\n\n

    :type Enabled: boolean
    :param Enabled: Indicates whether the scaling policy is enabled or disabled. The default is enabled. For more information, see Disabling a Scaling Policy for an Auto Scaling Group in the Amazon EC2 Auto Scaling User Guide .

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
Contains the output of PutScalingPolicy.

PolicyARN (string) --
The Amazon Resource Name (ARN) of the policy.

Alarms (list) --
The CloudWatch alarms created for the target tracking scaling policy.

(dict) --
Describes an alarm.

AlarmName (string) --
The name of the alarm.

AlarmARN (string) --
The Amazon Resource Name (ARN) of the alarm.











Exceptions

AutoScaling.Client.exceptions.LimitExceededFault
AutoScaling.Client.exceptions.ResourceContentionFault
AutoScaling.Client.exceptions.ServiceLinkedRoleFailure

Examples
This example adds the specified policy to the specified Auto Scaling group.
response = client.put_scaling_policy(
    AdjustmentType='ChangeInCapacity',
    AutoScalingGroupName='my-auto-scaling-group',
    PolicyName='ScaleIn',
    ScalingAdjustment=-1,
)

print(response)


Expected Output:
{
    'PolicyARN': 'arn:aws:autoscaling:us-west-2:123456789012:scalingPolicy:2233f3d7-6290-403b-b632-93c553560106:autoScalingGroupName/my-auto-scaling-group:policyName/ScaleIn',
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
    AutoScaling.Client.exceptions.LimitExceededFault
    AutoScaling.Client.exceptions.ResourceContentionFault
    AutoScaling.Client.exceptions.ServiceLinkedRoleFailure
    
    """
    pass

def put_scheduled_update_group_action(AutoScalingGroupName=None, ScheduledActionName=None, Time=None, StartTime=None, EndTime=None, Recurrence=None, MinSize=None, MaxSize=None, DesiredCapacity=None):
    """
    Creates or updates a scheduled scaling action for an Auto Scaling group. If you leave a parameter unspecified when updating a scheduled scaling action, the corresponding value remains unchanged.
    For more information, see Scheduled Scaling in the Amazon EC2 Auto Scaling User Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example adds the specified scheduled action to the specified Auto Scaling group.
    Expected Output:
    
    :example: response = client.put_scheduled_update_group_action(
        AutoScalingGroupName='string',
        ScheduledActionName='string',
        Time=datetime(2015, 1, 1),
        StartTime=datetime(2015, 1, 1),
        EndTime=datetime(2015, 1, 1),
        Recurrence='string',
        MinSize=123,
        MaxSize=123,
        DesiredCapacity=123
    )
    
    
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: [REQUIRED]\nThe name of the Auto Scaling group.\n

    :type ScheduledActionName: string
    :param ScheduledActionName: [REQUIRED]\nThe name of this scaling action.\n

    :type Time: datetime
    :param Time: This parameter is no longer used.

    :type StartTime: datetime
    :param StartTime: The date and time for this action to start, in YYYY-MM-DDThh:mm:ssZ format in UTC/GMT only and in quotes (for example, '2019-06-01T00:00:00Z' ).\nIf you specify Recurrence and StartTime , Amazon EC2 Auto Scaling performs the action at this time, and then performs the action based on the specified recurrence.\nIf you try to schedule your action in the past, Amazon EC2 Auto Scaling returns an error message.\n

    :type EndTime: datetime
    :param EndTime: The date and time for the recurring schedule to end. Amazon EC2 Auto Scaling does not perform the action after this time.

    :type Recurrence: string
    :param Recurrence: The recurring schedule for this action, in Unix cron syntax format. This format consists of five fields separated by white spaces: [Minute] [Hour] [Day_of_Month] [Month_of_Year] [Day_of_Week]. The value must be in quotes (for example, '30 0 1 1,6,12 *' ). For more information about this format, see Crontab .\nWhen StartTime and EndTime are specified with Recurrence , they form the boundaries of when the recurring action starts and stops.\n

    :type MinSize: integer
    :param MinSize: The minimum size of the Auto Scaling group.

    :type MaxSize: integer
    :param MaxSize: The maximum size of the Auto Scaling group.

    :type DesiredCapacity: integer
    :param DesiredCapacity: The desired capacity is the initial capacity of the Auto Scaling group after the scheduled action runs and the capacity it attempts to maintain. It can scale beyond this capacity if you add more scaling conditions.

    :return: response = client.put_scheduled_update_group_action(
        AutoScalingGroupName='my-auto-scaling-group',
        DesiredCapacity=4,
        EndTime=datetime(2014, 5, 12, 8, 0, 0, 0, 132, 0),
        MaxSize=6,
        MinSize=2,
        ScheduledActionName='my-scheduled-action',
        StartTime=datetime(2014, 5, 12, 8, 0, 0, 0, 132, 0),
    )
    
    print(response)
    
    
    :returns: 
    AutoScaling.Client.exceptions.AlreadyExistsFault
    AutoScaling.Client.exceptions.LimitExceededFault
    AutoScaling.Client.exceptions.ResourceContentionFault
    
    """
    pass

def record_lifecycle_action_heartbeat(LifecycleHookName=None, AutoScalingGroupName=None, LifecycleActionToken=None, InstanceId=None):
    """
    Records a heartbeat for the lifecycle action associated with the specified token or instance. This extends the timeout by the length of time defined using the  PutLifecycleHook API call.
    This step is a part of the procedure for adding a lifecycle hook to an Auto Scaling group:
    For more information, see Auto Scaling Lifecycle in the Amazon EC2 Auto Scaling User Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example records a lifecycle action heartbeat to keep the instance in a pending state.
    Expected Output:
    
    :example: response = client.record_lifecycle_action_heartbeat(
        LifecycleHookName='string',
        AutoScalingGroupName='string',
        LifecycleActionToken='string',
        InstanceId='string'
    )
    
    
    :type LifecycleHookName: string
    :param LifecycleHookName: [REQUIRED]\nThe name of the lifecycle hook.\n

    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: [REQUIRED]\nThe name of the Auto Scaling group.\n

    :type LifecycleActionToken: string
    :param LifecycleActionToken: A token that uniquely identifies a specific lifecycle action associated with an instance. Amazon EC2 Auto Scaling sends this token to the notification target that you specified when you created the lifecycle hook.

    :type InstanceId: string
    :param InstanceId: The ID of the instance.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

AutoScaling.Client.exceptions.ResourceContentionFault

Examples
This example records a lifecycle action heartbeat to keep the instance in a pending state.
response = client.record_lifecycle_action_heartbeat(
    AutoScalingGroupName='my-auto-scaling-group',
    LifecycleActionToken='bcd2f1b8-9a78-44d3-8a7a-4dd07d7cf635',
    LifecycleHookName='my-lifecycle-hook',
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
    LifecycleHookName (string) -- [REQUIRED]
    The name of the lifecycle hook.
    
    AutoScalingGroupName (string) -- [REQUIRED]
    The name of the Auto Scaling group.
    
    LifecycleActionToken (string) -- A token that uniquely identifies a specific lifecycle action associated with an instance. Amazon EC2 Auto Scaling sends this token to the notification target that you specified when you created the lifecycle hook.
    InstanceId (string) -- The ID of the instance.
    
    """
    pass

def resume_processes(AutoScalingGroupName=None, ScalingProcesses=None):
    """
    Resumes the specified suspended automatic scaling processes, or all suspended process, for the specified Auto Scaling group.
    For more information, see Suspending and Resuming Scaling Processes in the Amazon EC2 Auto Scaling User Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example resumes the specified suspended scaling process for the specified Auto Scaling group.
    Expected Output:
    
    :example: response = client.resume_processes(
        AutoScalingGroupName='string',
        ScalingProcesses=[
            'string',
        ]
    )
    
    
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: [REQUIRED]\nThe name of the Auto Scaling group.\n

    :type ScalingProcesses: list
    :param ScalingProcesses: One or more of the following processes. If you omit this parameter, all processes are specified.\n\nLaunch\nTerminate\nHealthCheck\nReplaceUnhealthy\nAZRebalance\nAlarmNotification\nScheduledActions\nAddToLoadBalancer\n\n\n(string) --\n\n

    :return: response = client.resume_processes(
        AutoScalingGroupName='my-auto-scaling-group',
        ScalingProcesses=[
            'AlarmNotification',
        ],
    )
    
    print(response)
    
    
    :returns: 
    AutoScaling.Client.exceptions.ResourceInUseFault
    AutoScaling.Client.exceptions.ResourceContentionFault
    
    """
    pass

def set_desired_capacity(AutoScalingGroupName=None, DesiredCapacity=None, HonorCooldown=None):
    """
    Sets the size of the specified Auto Scaling group.
    If a scale-in activity occurs as a result of a new DesiredCapacity value that is lower than the current size of the group, the Auto Scaling group uses its termination policy to determine which instances to terminate.
    For more information, see Manual Scaling in the Amazon EC2 Auto Scaling User Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example sets the desired capacity for the specified Auto Scaling group.
    Expected Output:
    
    :example: response = client.set_desired_capacity(
        AutoScalingGroupName='string',
        DesiredCapacity=123,
        HonorCooldown=True|False
    )
    
    
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: [REQUIRED]\nThe name of the Auto Scaling group.\n

    :type DesiredCapacity: integer
    :param DesiredCapacity: [REQUIRED]\nThe desired capacity is the initial capacity of the Auto Scaling group after this operation completes and the capacity it attempts to maintain.\n

    :type HonorCooldown: boolean
    :param HonorCooldown: Indicates whether Amazon EC2 Auto Scaling waits for the cooldown period to complete before initiating a scaling activity to set your Auto Scaling group to its new capacity. By default, Amazon EC2 Auto Scaling does not honor the cooldown period during manual scaling activities.

    :return: response = client.set_desired_capacity(
        AutoScalingGroupName='my-auto-scaling-group',
        DesiredCapacity=2,
        HonorCooldown=True,
    )
    
    print(response)
    
    
    :returns: 
    AutoScaling.Client.exceptions.ScalingActivityInProgressFault
    AutoScaling.Client.exceptions.ResourceContentionFault
    
    """
    pass

def set_instance_health(InstanceId=None, HealthStatus=None, ShouldRespectGracePeriod=None):
    """
    Sets the health status of the specified instance.
    For more information, see Health Checks for Auto Scaling Instances in the Amazon EC2 Auto Scaling User Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example sets the health status of the specified instance to Unhealthy.
    Expected Output:
    
    :example: response = client.set_instance_health(
        InstanceId='string',
        HealthStatus='string',
        ShouldRespectGracePeriod=True|False
    )
    
    
    :type InstanceId: string
    :param InstanceId: [REQUIRED]\nThe ID of the instance.\n

    :type HealthStatus: string
    :param HealthStatus: [REQUIRED]\nThe health status of the instance. Set to Healthy to have the instance remain in service. Set to Unhealthy to have the instance be out of service. Amazon EC2 Auto Scaling terminates and replaces the unhealthy instance.\n

    :type ShouldRespectGracePeriod: boolean
    :param ShouldRespectGracePeriod: If the Auto Scaling group of the specified instance has a HealthCheckGracePeriod specified for the group, by default, this call respects the grace period. Set this to False , to have the call not respect the grace period associated with the group.\nFor more information about the health check grace period, see CreateAutoScalingGroup in the Amazon EC2 Auto Scaling API Reference .\n

    :return: response = client.set_instance_health(
        HealthStatus='Unhealthy',
        InstanceId='i-93633f9b',
    )
    
    print(response)
    
    
    :returns: 
    AutoScaling.Client.exceptions.ResourceContentionFault
    
    """
    pass

def set_instance_protection(InstanceIds=None, AutoScalingGroupName=None, ProtectedFromScaleIn=None):
    """
    Updates the instance protection settings of the specified instances.
    For more information about preventing instances that are part of an Auto Scaling group from terminating on scale in, see Instance Protection in the Amazon EC2 Auto Scaling User Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example enables instance protection for the specified instance.
    Expected Output:
    This example disables instance protection for the specified instance.
    Expected Output:
    
    :example: response = client.set_instance_protection(
        InstanceIds=[
            'string',
        ],
        AutoScalingGroupName='string',
        ProtectedFromScaleIn=True|False
    )
    
    
    :type InstanceIds: list
    :param InstanceIds: [REQUIRED]\nOne or more instance IDs.\n\n(string) --\n\n

    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: [REQUIRED]\nThe name of the Auto Scaling group.\n

    :type ProtectedFromScaleIn: boolean
    :param ProtectedFromScaleIn: [REQUIRED]\nIndicates whether the instance is protected from termination by Amazon EC2 Auto Scaling when scaling in.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

AutoScaling.Client.exceptions.LimitExceededFault
AutoScaling.Client.exceptions.ResourceContentionFault

Examples
This example enables instance protection for the specified instance.
response = client.set_instance_protection(
    AutoScalingGroupName='my-auto-scaling-group',
    InstanceIds=[
        'i-93633f9b',
    ],
    ProtectedFromScaleIn=True,
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}


This example disables instance protection for the specified instance.
response = client.set_instance_protection(
    AutoScalingGroupName='my-auto-scaling-group',
    InstanceIds=[
        'i-93633f9b',
    ],
    ProtectedFromScaleIn=False,
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

def suspend_processes(AutoScalingGroupName=None, ScalingProcesses=None):
    """
    Suspends the specified automatic scaling processes, or all processes, for the specified Auto Scaling group.
    If you suspend either the Launch or Terminate process types, it can prevent other process types from functioning properly. For more information, see Suspending and Resuming Scaling Processes in the Amazon EC2 Auto Scaling User Guide .
    To resume processes that have been suspended, call the  ResumeProcesses API.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example suspends the specified scaling process for the specified Auto Scaling group.
    Expected Output:
    
    :example: response = client.suspend_processes(
        AutoScalingGroupName='string',
        ScalingProcesses=[
            'string',
        ]
    )
    
    
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: [REQUIRED]\nThe name of the Auto Scaling group.\n

    :type ScalingProcesses: list
    :param ScalingProcesses: One or more of the following processes. If you omit this parameter, all processes are specified.\n\nLaunch\nTerminate\nHealthCheck\nReplaceUnhealthy\nAZRebalance\nAlarmNotification\nScheduledActions\nAddToLoadBalancer\n\n\n(string) --\n\n

    :return: response = client.suspend_processes(
        AutoScalingGroupName='my-auto-scaling-group',
        ScalingProcesses=[
            'AlarmNotification',
        ],
    )
    
    print(response)
    
    
    :returns: 
    AutoScaling.Client.exceptions.ResourceInUseFault
    AutoScaling.Client.exceptions.ResourceContentionFault
    
    """
    pass

def terminate_instance_in_auto_scaling_group(InstanceId=None, ShouldDecrementDesiredCapacity=None):
    """
    Terminates the specified instance and optionally adjusts the desired group size.
    This call simply makes a termination request. The instance is not terminated immediately. When an instance is terminated, the instance status changes to terminated . You can\'t connect to or start an instance after you\'ve terminated it.
    If you do not specify the option to decrement the desired capacity, Amazon EC2 Auto Scaling launches instances to replace the ones that are terminated.
    By default, Amazon EC2 Auto Scaling balances instances across all Availability Zones. If you decrement the desired capacity, your Auto Scaling group can become unbalanced between Availability Zones. Amazon EC2 Auto Scaling tries to rebalance the group, and rebalancing might terminate instances in other zones. For more information, see Rebalancing Activities in the Amazon EC2 Auto Scaling User Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example terminates the specified instance from the specified Auto Scaling group without updating the size of the group. Auto Scaling launches a replacement instance after the specified instance terminates.
    Expected Output:
    
    :example: response = client.terminate_instance_in_auto_scaling_group(
        InstanceId='string',
        ShouldDecrementDesiredCapacity=True|False
    )
    
    
    :type InstanceId: string
    :param InstanceId: [REQUIRED]\nThe ID of the instance.\n

    :type ShouldDecrementDesiredCapacity: boolean
    :param ShouldDecrementDesiredCapacity: [REQUIRED]\nIndicates whether terminating the instance also decrements the size of the Auto Scaling group.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Activity': {
        'ActivityId': 'string',
        'AutoScalingGroupName': 'string',
        'Description': 'string',
        'Cause': 'string',
        'StartTime': datetime(2015, 1, 1),
        'EndTime': datetime(2015, 1, 1),
        'StatusCode': 'PendingSpotBidPlacement'|'WaitingForSpotInstanceRequestId'|'WaitingForSpotInstanceId'|'WaitingForInstanceId'|'PreInService'|'InProgress'|'WaitingForELBConnectionDraining'|'MidLifecycleAction'|'WaitingForInstanceWarmup'|'Successful'|'Failed'|'Cancelled',
        'StatusMessage': 'string',
        'Progress': 123,
        'Details': 'string'
    }
}


Response Structure

(dict) --

Activity (dict) --
A scaling activity.

ActivityId (string) --
The ID of the activity.

AutoScalingGroupName (string) --
The name of the Auto Scaling group.

Description (string) --
A friendly, more verbose description of the activity.

Cause (string) --
The reason the activity began.

StartTime (datetime) --
The start time of the activity.

EndTime (datetime) --
The end time of the activity.

StatusCode (string) --
The current status of the activity.

StatusMessage (string) --
A friendly, more verbose description of the activity status.

Progress (integer) --
A value between 0 and 100 that indicates the progress of the activity.

Details (string) --
The details about the activity.









Exceptions

AutoScaling.Client.exceptions.ScalingActivityInProgressFault
AutoScaling.Client.exceptions.ResourceContentionFault

Examples
This example terminates the specified instance from the specified Auto Scaling group without updating the size of the group. Auto Scaling launches a replacement instance after the specified instance terminates.
response = client.terminate_instance_in_auto_scaling_group(
    InstanceId='i-93633f9b',
    ShouldDecrementDesiredCapacity=False,
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Activity': {
            'ActivityId': 'string',
            'AutoScalingGroupName': 'string',
            'Description': 'string',
            'Cause': 'string',
            'StartTime': datetime(2015, 1, 1),
            'EndTime': datetime(2015, 1, 1),
            'StatusCode': 'PendingSpotBidPlacement'|'WaitingForSpotInstanceRequestId'|'WaitingForSpotInstanceId'|'WaitingForInstanceId'|'PreInService'|'InProgress'|'WaitingForELBConnectionDraining'|'MidLifecycleAction'|'WaitingForInstanceWarmup'|'Successful'|'Failed'|'Cancelled',
            'StatusMessage': 'string',
            'Progress': 123,
            'Details': 'string'
        }
    }
    
    
    :returns: 
    AutoScaling.Client.exceptions.ScalingActivityInProgressFault
    AutoScaling.Client.exceptions.ResourceContentionFault
    
    """
    pass

def update_auto_scaling_group(AutoScalingGroupName=None, LaunchConfigurationName=None, LaunchTemplate=None, MixedInstancesPolicy=None, MinSize=None, MaxSize=None, DesiredCapacity=None, DefaultCooldown=None, AvailabilityZones=None, HealthCheckType=None, HealthCheckGracePeriod=None, PlacementGroup=None, VPCZoneIdentifier=None, TerminationPolicies=None, NewInstancesProtectedFromScaleIn=None, ServiceLinkedRoleARN=None, MaxInstanceLifetime=None):
    """
    Updates the configuration for the specified Auto Scaling group.
    To update an Auto Scaling group, specify the name of the group and the parameter that you want to change. Any parameters that you don\'t specify are not changed by this update request. The new settings take effect on any scaling activities after this call returns.
    If you associate a new launch configuration or template with an Auto Scaling group, all new instances will get the updated configuration. Existing instances continue to run with the configuration that they were originally launched with. When you update a group to specify a mixed instances policy instead of a launch configuration or template, existing instances may be replaced to match the new purchasing options that you specified in the policy. For example, if the group currently has 100% On-Demand capacity and the policy specifies 50% Spot capacity, this means that half of your instances will be gradually terminated and relaunched as Spot Instances. When replacing instances, Amazon EC2 Auto Scaling launches new instances before terminating the old ones, so that updating your group does not compromise the performance or availability of your application.
    Note the following about changing DesiredCapacity , MaxSize , or MinSize :
    To see which parameters have been set, call the  DescribeAutoScalingGroups API. To view the scaling policies for an Auto Scaling group, call the  DescribePolicies API. If the group has scaling policies, you can update them by calling the  PutScalingPolicy API.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example updates the launch configuration of the specified Auto Scaling group.
    Expected Output:
    This example updates the minimum size and maximum size of the specified Auto Scaling group.
    Expected Output:
    This example enables instance protection for the specified Auto Scaling group.
    Expected Output:
    
    :example: response = client.update_auto_scaling_group(
        AutoScalingGroupName='string',
        LaunchConfigurationName='string',
        LaunchTemplate={
            'LaunchTemplateId': 'string',
            'LaunchTemplateName': 'string',
            'Version': 'string'
        },
        MixedInstancesPolicy={
            'LaunchTemplate': {
                'LaunchTemplateSpecification': {
                    'LaunchTemplateId': 'string',
                    'LaunchTemplateName': 'string',
                    'Version': 'string'
                },
                'Overrides': [
                    {
                        'InstanceType': 'string',
                        'WeightedCapacity': 'string'
                    },
                ]
            },
            'InstancesDistribution': {
                'OnDemandAllocationStrategy': 'string',
                'OnDemandBaseCapacity': 123,
                'OnDemandPercentageAboveBaseCapacity': 123,
                'SpotAllocationStrategy': 'string',
                'SpotInstancePools': 123,
                'SpotMaxPrice': 'string'
            }
        },
        MinSize=123,
        MaxSize=123,
        DesiredCapacity=123,
        DefaultCooldown=123,
        AvailabilityZones=[
            'string',
        ],
        HealthCheckType='string',
        HealthCheckGracePeriod=123,
        PlacementGroup='string',
        VPCZoneIdentifier='string',
        TerminationPolicies=[
            'string',
        ],
        NewInstancesProtectedFromScaleIn=True|False,
        ServiceLinkedRoleARN='string',
        MaxInstanceLifetime=123
    )
    
    
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: [REQUIRED]\nThe name of the Auto Scaling group.\n

    :type LaunchConfigurationName: string
    :param LaunchConfigurationName: The name of the launch configuration. If you specify LaunchConfigurationName in your update request, you can\'t specify LaunchTemplate or MixedInstancesPolicy .

    :type LaunchTemplate: dict
    :param LaunchTemplate: The launch template and version to use to specify the updates. If you specify LaunchTemplate in your update request, you can\'t specify LaunchConfigurationName or MixedInstancesPolicy .\nFor more information, see LaunchTemplateSpecification in the Amazon EC2 Auto Scaling API Reference .\n\nLaunchTemplateId (string) --The ID of the launch template. To get the template ID, use the Amazon EC2 DescribeLaunchTemplates API operation. New launch templates can be created using the Amazon EC2 CreateLaunchTemplate API.\nYou must specify either a template ID or a template name.\n\nLaunchTemplateName (string) --The name of the launch template. To get the template name, use the Amazon EC2 DescribeLaunchTemplates API operation. New launch templates can be created using the Amazon EC2 CreateLaunchTemplate API.\nYou must specify either a template ID or a template name.\n\nVersion (string) --The version number, $Latest , or $Default . To get the version number, use the Amazon EC2 DescribeLaunchTemplateVersions API operation. New launch template versions can be created using the Amazon EC2 CreateLaunchTemplateVersion API.\nIf the value is $Latest , Amazon EC2 Auto Scaling selects the latest version of the launch template when launching instances. If the value is $Default , Amazon EC2 Auto Scaling selects the default version of the launch template when launching instances. The default value is $Default .\n\n\n

    :type MixedInstancesPolicy: dict
    :param MixedInstancesPolicy: An embedded object that specifies a mixed instances policy.\nIn your call to UpdateAutoScalingGroup , you can make changes to the policy that is specified. All optional parameters are left unchanged if not specified.\nFor more information, see MixedInstancesPolicy in the Amazon EC2 Auto Scaling API Reference and Auto Scaling Groups with Multiple Instance Types and Purchase Options in the Amazon EC2 Auto Scaling User Guide .\n\nLaunchTemplate (dict) --The launch template and instance types (overrides).\nThis parameter must be specified when creating a mixed instances policy.\n\nLaunchTemplateSpecification (dict) --The launch template to use. You must specify either the launch template ID or launch template name in the request.\n\nLaunchTemplateId (string) --The ID of the launch template. To get the template ID, use the Amazon EC2 DescribeLaunchTemplates API operation. New launch templates can be created using the Amazon EC2 CreateLaunchTemplate API.\nYou must specify either a template ID or a template name.\n\nLaunchTemplateName (string) --The name of the launch template. To get the template name, use the Amazon EC2 DescribeLaunchTemplates API operation. New launch templates can be created using the Amazon EC2 CreateLaunchTemplate API.\nYou must specify either a template ID or a template name.\n\nVersion (string) --The version number, $Latest , or $Default . To get the version number, use the Amazon EC2 DescribeLaunchTemplateVersions API operation. New launch template versions can be created using the Amazon EC2 CreateLaunchTemplateVersion API.\nIf the value is $Latest , Amazon EC2 Auto Scaling selects the latest version of the launch template when launching instances. If the value is $Default , Amazon EC2 Auto Scaling selects the default version of the launch template when launching instances. The default value is $Default .\n\n\n\nOverrides (list) --Any parameters that you specify override the same parameters in the launch template. Currently, the only supported override is instance type. You can specify between 1 and 20 instance types.\nIf not provided, Amazon EC2 Auto Scaling will use the instance type specified in the launch template to launch instances.\n\n(dict) --Describes an override for a launch template. Currently, the only supported override is instance type.\nThe maximum number of instance type overrides that can be associated with an Auto Scaling group is 20.\n\nInstanceType (string) --The instance type. You must use an instance type that is supported in your requested Region and Availability Zones.\nFor information about available instance types, see Available Instance Types in the Amazon Elastic Compute Cloud User Guide.\n\nWeightedCapacity (string) --The number of capacity units, which gives the instance type a proportional weight to other instance types. For example, larger instance types are generally weighted more than smaller instance types. These are the same units that you chose to set the desired capacity in terms of instances, or a performance attribute such as vCPUs, memory, or I/O.\nFor more information, see Instance Weighting for Amazon EC2 Auto Scaling in the Amazon EC2 Auto Scaling User Guide .\nValid Range: Minimum value of 1. Maximum value of 999.\n\n\n\n\n\n\n\nInstancesDistribution (dict) --The instances distribution to use.\nIf you leave this parameter unspecified, the value for each parameter in InstancesDistribution uses a default value.\n\nOnDemandAllocationStrategy (string) --Indicates how to allocate instance types to fulfill On-Demand capacity.\nThe only valid value is prioritized , which is also the default value. This strategy uses the order of instance type overrides for the LaunchTemplate to define the launch priority of each instance type. The first instance type in the array is prioritized higher than the last. If all your On-Demand capacity cannot be fulfilled using your highest priority instance, then the Auto Scaling groups launches the remaining capacity using the second priority instance type, and so on.\n\nOnDemandBaseCapacity (integer) --The minimum amount of the Auto Scaling group\'s capacity that must be fulfilled by On-Demand Instances. This base portion is provisioned first as your group scales.\nDefault if not set is 0. If you leave it set to 0, On-Demand Instances are launched as a percentage of the Auto Scaling group\'s desired capacity, per the OnDemandPercentageAboveBaseCapacity setting.\n\nNote\nAn update to this setting means a gradual replacement of instances to maintain the specified number of On-Demand Instances for your base capacity. When replacing instances, Amazon EC2 Auto Scaling launches new instances before terminating the old ones.\n\n\nOnDemandPercentageAboveBaseCapacity (integer) --Controls the percentages of On-Demand Instances and Spot Instances for your additional capacity beyond OnDemandBaseCapacity .\nDefault if not set is 100. If you leave it set to 100, the percentages are 100% for On-Demand Instances and 0% for Spot Instances.\n\nNote\nAn update to this setting means a gradual replacement of instances to maintain the percentage of On-Demand Instances for your additional capacity above the base capacity. When replacing instances, Amazon EC2 Auto Scaling launches new instances before terminating the old ones.\n\nValid Range: Minimum value of 0. Maximum value of 100.\n\nSpotAllocationStrategy (string) --Indicates how to allocate instances across Spot Instance pools.\nIf the allocation strategy is lowest-price , the Auto Scaling group launches instances using the Spot pools with the lowest price, and evenly allocates your instances across the number of Spot pools that you specify. If the allocation strategy is capacity-optimized , the Auto Scaling group launches instances using Spot pools that are optimally chosen based on the available Spot capacity.\nThe default Spot allocation strategy for calls that you make through the API, the AWS CLI, or the AWS SDKs is lowest-price . The default Spot allocation strategy for the AWS Management Console is capacity-optimized .\nValid values: lowest-price | capacity-optimized\n\nSpotInstancePools (integer) --The number of Spot Instance pools across which to allocate your Spot Instances. The Spot pools are determined from the different instance types in the Overrides array of LaunchTemplate . Default if not set is 2.\nUsed only when the Spot allocation strategy is lowest-price .\nValid Range: Minimum value of 1. Maximum value of 20.\n\nSpotMaxPrice (string) --The maximum price per unit hour that you are willing to pay for a Spot Instance. If you leave the value of this parameter blank (which is the default), the maximum Spot price is set at the On-Demand price.\nTo remove a value that you previously set, include the parameter but leave the value blank.\n\n\n\n\n

    :type MinSize: integer
    :param MinSize: The minimum size of the Auto Scaling group.

    :type MaxSize: integer
    :param MaxSize: The maximum size of the Auto Scaling group.\n\nNote\nWith a mixed instances policy that uses instance weighting, Amazon EC2 Auto Scaling may need to go above MaxSize to meet your capacity requirements. In this event, Amazon EC2 Auto Scaling will never go above MaxSize by more than your maximum instance weight (weights that define how many capacity units each instance contributes to the capacity of the group).\n\n

    :type DesiredCapacity: integer
    :param DesiredCapacity: The desired capacity is the initial capacity of the Auto Scaling group after this operation completes and the capacity it attempts to maintain.\nThis number must be greater than or equal to the minimum size of the group and less than or equal to the maximum size of the group.\n

    :type DefaultCooldown: integer
    :param DefaultCooldown: The amount of time, in seconds, after a scaling activity completes before another scaling activity can start. The default value is 300 . This cooldown period is not used when a scaling-specific cooldown is specified.\nCooldown periods are not supported for target tracking scaling policies, step scaling policies, or scheduled scaling. For more information, see Scaling Cooldowns in the Amazon EC2 Auto Scaling User Guide .\n

    :type AvailabilityZones: list
    :param AvailabilityZones: One or more Availability Zones for the group.\n\n(string) --\n\n

    :type HealthCheckType: string
    :param HealthCheckType: The service to use for the health checks. The valid values are EC2 and ELB . If you configure an Auto Scaling group to use ELB health checks, it considers the instance unhealthy if it fails either the EC2 status checks or the load balancer health checks.

    :type HealthCheckGracePeriod: integer
    :param HealthCheckGracePeriod: The amount of time, in seconds, that Amazon EC2 Auto Scaling waits before checking the health status of an EC2 instance that has come into service. The default value is 0 .\nFor more information, see Health Check Grace Period in the Amazon EC2 Auto Scaling User Guide .\nConditional: This parameter is required if you are adding an ELB health check.\n

    :type PlacementGroup: string
    :param PlacementGroup: The name of the placement group into which to launch your instances, if any. A placement group is a logical grouping of instances within a single Availability Zone. You cannot specify multiple Availability Zones and a placement group. For more information, see Placement Groups in the Amazon EC2 User Guide for Linux Instances .

    :type VPCZoneIdentifier: string
    :param VPCZoneIdentifier: A comma-separated list of subnet IDs for virtual private cloud (VPC).\nIf you specify VPCZoneIdentifier with AvailabilityZones , the subnets that you specify for this parameter must reside in those Availability Zones.\n

    :type TerminationPolicies: list
    :param TerminationPolicies: A standalone termination policy or a list of termination policies used to select the instance to terminate. The policies are executed in the order that they are listed.\nFor more information, see Controlling Which Instances Auto Scaling Terminates During Scale In in the Amazon EC2 Auto Scaling User Guide .\n\n(string) --\n\n

    :type NewInstancesProtectedFromScaleIn: boolean
    :param NewInstancesProtectedFromScaleIn: Indicates whether newly launched instances are protected from termination by Amazon EC2 Auto Scaling when scaling in.\nFor more information about preventing instances from terminating on scale in, see Instance Protection in the Amazon EC2 Auto Scaling User Guide .\n

    :type ServiceLinkedRoleARN: string
    :param ServiceLinkedRoleARN: The Amazon Resource Name (ARN) of the service-linked role that the Auto Scaling group uses to call other AWS services on your behalf. For more information, see Service-Linked Roles in the Amazon EC2 Auto Scaling User Guide .

    :type MaxInstanceLifetime: integer
    :param MaxInstanceLifetime: The maximum amount of time, in seconds, that an instance can be in service. The default is null.\nThis parameter is optional, but if you specify a value for it, you must specify a value of at least 604,800 seconds (7 days). To clear a previously set value, specify a new value of 0.\nFor more information, see Replacing Auto Scaling Instances Based on Maximum Instance Lifetime in the Amazon EC2 Auto Scaling User Guide .\nValid Range: Minimum value of 0.\n

    :return: response = client.update_auto_scaling_group(
        AutoScalingGroupName='my-auto-scaling-group',
        LaunchConfigurationName='new-launch-config',
    )
    
    print(response)
    
    
    :returns: 
    AutoScalingGroupName (string) -- [REQUIRED]
    The name of the Auto Scaling group.
    
    LaunchConfigurationName (string) -- The name of the launch configuration. If you specify LaunchConfigurationName in your update request, you can\'t specify LaunchTemplate or MixedInstancesPolicy .
    LaunchTemplate (dict) -- The launch template and version to use to specify the updates. If you specify LaunchTemplate in your update request, you can\'t specify LaunchConfigurationName or MixedInstancesPolicy .
    For more information, see LaunchTemplateSpecification in the Amazon EC2 Auto Scaling API Reference .
    
    LaunchTemplateId (string) --The ID of the launch template. To get the template ID, use the Amazon EC2 DescribeLaunchTemplates API operation. New launch templates can be created using the Amazon EC2 CreateLaunchTemplate API.
    You must specify either a template ID or a template name.
    
    LaunchTemplateName (string) --The name of the launch template. To get the template name, use the Amazon EC2 DescribeLaunchTemplates API operation. New launch templates can be created using the Amazon EC2 CreateLaunchTemplate API.
    You must specify either a template ID or a template name.
    
    Version (string) --The version number, $Latest , or $Default . To get the version number, use the Amazon EC2 DescribeLaunchTemplateVersions API operation. New launch template versions can be created using the Amazon EC2 CreateLaunchTemplateVersion API.
    If the value is $Latest , Amazon EC2 Auto Scaling selects the latest version of the launch template when launching instances. If the value is $Default , Amazon EC2 Auto Scaling selects the default version of the launch template when launching instances. The default value is $Default .
    
    
    
    MixedInstancesPolicy (dict) -- An embedded object that specifies a mixed instances policy.
    In your call to UpdateAutoScalingGroup , you can make changes to the policy that is specified. All optional parameters are left unchanged if not specified.
    For more information, see MixedInstancesPolicy in the Amazon EC2 Auto Scaling API Reference and Auto Scaling Groups with Multiple Instance Types and Purchase Options in the Amazon EC2 Auto Scaling User Guide .
    
    LaunchTemplate (dict) --The launch template and instance types (overrides).
    This parameter must be specified when creating a mixed instances policy.
    
    LaunchTemplateSpecification (dict) --The launch template to use. You must specify either the launch template ID or launch template name in the request.
    
    LaunchTemplateId (string) --The ID of the launch template. To get the template ID, use the Amazon EC2 DescribeLaunchTemplates API operation. New launch templates can be created using the Amazon EC2 CreateLaunchTemplate API.
    You must specify either a template ID or a template name.
    
    LaunchTemplateName (string) --The name of the launch template. To get the template name, use the Amazon EC2 DescribeLaunchTemplates API operation. New launch templates can be created using the Amazon EC2 CreateLaunchTemplate API.
    You must specify either a template ID or a template name.
    
    Version (string) --The version number, $Latest , or $Default . To get the version number, use the Amazon EC2 DescribeLaunchTemplateVersions API operation. New launch template versions can be created using the Amazon EC2 CreateLaunchTemplateVersion API.
    If the value is $Latest , Amazon EC2 Auto Scaling selects the latest version of the launch template when launching instances. If the value is $Default , Amazon EC2 Auto Scaling selects the default version of the launch template when launching instances. The default value is $Default .
    
    
    
    Overrides (list) --Any parameters that you specify override the same parameters in the launch template. Currently, the only supported override is instance type. You can specify between 1 and 20 instance types.
    If not provided, Amazon EC2 Auto Scaling will use the instance type specified in the launch template to launch instances.
    
    (dict) --Describes an override for a launch template. Currently, the only supported override is instance type.
    The maximum number of instance type overrides that can be associated with an Auto Scaling group is 20.
    
    InstanceType (string) --The instance type. You must use an instance type that is supported in your requested Region and Availability Zones.
    For information about available instance types, see Available Instance Types in the Amazon Elastic Compute Cloud User Guide.
    
    WeightedCapacity (string) --The number of capacity units, which gives the instance type a proportional weight to other instance types. For example, larger instance types are generally weighted more than smaller instance types. These are the same units that you chose to set the desired capacity in terms of instances, or a performance attribute such as vCPUs, memory, or I/O.
    For more information, see Instance Weighting for Amazon EC2 Auto Scaling in the Amazon EC2 Auto Scaling User Guide .
    Valid Range: Minimum value of 1. Maximum value of 999.
    
    
    
    
    
    
    
    InstancesDistribution (dict) --The instances distribution to use.
    If you leave this parameter unspecified, the value for each parameter in InstancesDistribution uses a default value.
    
    OnDemandAllocationStrategy (string) --Indicates how to allocate instance types to fulfill On-Demand capacity.
    The only valid value is prioritized , which is also the default value. This strategy uses the order of instance type overrides for the  LaunchTemplate to define the launch priority of each instance type. The first instance type in the array is prioritized higher than the last. If all your On-Demand capacity cannot be fulfilled using your highest priority instance, then the Auto Scaling groups launches the remaining capacity using the second priority instance type, and so on.
    
    OnDemandBaseCapacity (integer) --The minimum amount of the Auto Scaling group\'s capacity that must be fulfilled by On-Demand Instances. This base portion is provisioned first as your group scales.
    Default if not set is 0. If you leave it set to 0, On-Demand Instances are launched as a percentage of the Auto Scaling group\'s desired capacity, per the OnDemandPercentageAboveBaseCapacity setting.
    
    Note
    An update to this setting means a gradual replacement of instances to maintain the specified number of On-Demand Instances for your base capacity. When replacing instances, Amazon EC2 Auto Scaling launches new instances before terminating the old ones.
    
    
    OnDemandPercentageAboveBaseCapacity (integer) --Controls the percentages of On-Demand Instances and Spot Instances for your additional capacity beyond OnDemandBaseCapacity .
    Default if not set is 100. If you leave it set to 100, the percentages are 100% for On-Demand Instances and 0% for Spot Instances.
    
    Note
    An update to this setting means a gradual replacement of instances to maintain the percentage of On-Demand Instances for your additional capacity above the base capacity. When replacing instances, Amazon EC2 Auto Scaling launches new instances before terminating the old ones.
    
    Valid Range: Minimum value of 0. Maximum value of 100.
    
    SpotAllocationStrategy (string) --Indicates how to allocate instances across Spot Instance pools.
    If the allocation strategy is lowest-price , the Auto Scaling group launches instances using the Spot pools with the lowest price, and evenly allocates your instances across the number of Spot pools that you specify. If the allocation strategy is capacity-optimized , the Auto Scaling group launches instances using Spot pools that are optimally chosen based on the available Spot capacity.
    The default Spot allocation strategy for calls that you make through the API, the AWS CLI, or the AWS SDKs is lowest-price . The default Spot allocation strategy for the AWS Management Console is capacity-optimized .
    Valid values: lowest-price | capacity-optimized
    
    SpotInstancePools (integer) --The number of Spot Instance pools across which to allocate your Spot Instances. The Spot pools are determined from the different instance types in the Overrides array of  LaunchTemplate . Default if not set is 2.
    Used only when the Spot allocation strategy is lowest-price .
    Valid Range: Minimum value of 1. Maximum value of 20.
    
    SpotMaxPrice (string) --The maximum price per unit hour that you are willing to pay for a Spot Instance. If you leave the value of this parameter blank (which is the default), the maximum Spot price is set at the On-Demand price.
    To remove a value that you previously set, include the parameter but leave the value blank.
    
    
    
    
    
    MinSize (integer) -- The minimum size of the Auto Scaling group.
    MaxSize (integer) -- The maximum size of the Auto Scaling group.
    
    Note
    With a mixed instances policy that uses instance weighting, Amazon EC2 Auto Scaling may need to go above MaxSize to meet your capacity requirements. In this event, Amazon EC2 Auto Scaling will never go above MaxSize by more than your maximum instance weight (weights that define how many capacity units each instance contributes to the capacity of the group).
    
    
    DesiredCapacity (integer) -- The desired capacity is the initial capacity of the Auto Scaling group after this operation completes and the capacity it attempts to maintain.
    This number must be greater than or equal to the minimum size of the group and less than or equal to the maximum size of the group.
    
    DefaultCooldown (integer) -- The amount of time, in seconds, after a scaling activity completes before another scaling activity can start. The default value is 300 . This cooldown period is not used when a scaling-specific cooldown is specified.
    Cooldown periods are not supported for target tracking scaling policies, step scaling policies, or scheduled scaling. For more information, see Scaling Cooldowns in the Amazon EC2 Auto Scaling User Guide .
    
    AvailabilityZones (list) -- One or more Availability Zones for the group.
    
    (string) --
    
    
    HealthCheckType (string) -- The service to use for the health checks. The valid values are EC2 and ELB . If you configure an Auto Scaling group to use ELB health checks, it considers the instance unhealthy if it fails either the EC2 status checks or the load balancer health checks.
    HealthCheckGracePeriod (integer) -- The amount of time, in seconds, that Amazon EC2 Auto Scaling waits before checking the health status of an EC2 instance that has come into service. The default value is 0 .
    For more information, see Health Check Grace Period in the Amazon EC2 Auto Scaling User Guide .
    Conditional: This parameter is required if you are adding an ELB health check.
    
    PlacementGroup (string) -- The name of the placement group into which to launch your instances, if any. A placement group is a logical grouping of instances within a single Availability Zone. You cannot specify multiple Availability Zones and a placement group. For more information, see Placement Groups in the Amazon EC2 User Guide for Linux Instances .
    VPCZoneIdentifier (string) -- A comma-separated list of subnet IDs for virtual private cloud (VPC).
    If you specify VPCZoneIdentifier with AvailabilityZones , the subnets that you specify for this parameter must reside in those Availability Zones.
    
    TerminationPolicies (list) -- A standalone termination policy or a list of termination policies used to select the instance to terminate. The policies are executed in the order that they are listed.
    For more information, see Controlling Which Instances Auto Scaling Terminates During Scale In in the Amazon EC2 Auto Scaling User Guide .
    
    (string) --
    
    
    NewInstancesProtectedFromScaleIn (boolean) -- Indicates whether newly launched instances are protected from termination by Amazon EC2 Auto Scaling when scaling in.
    For more information about preventing instances from terminating on scale in, see Instance Protection in the Amazon EC2 Auto Scaling User Guide .
    
    ServiceLinkedRoleARN (string) -- The Amazon Resource Name (ARN) of the service-linked role that the Auto Scaling group uses to call other AWS services on your behalf. For more information, see Service-Linked Roles in the Amazon EC2 Auto Scaling User Guide .
    MaxInstanceLifetime (integer) -- The maximum amount of time, in seconds, that an instance can be in service. The default is null.
    This parameter is optional, but if you specify a value for it, you must specify a value of at least 604,800 seconds (7 days). To clear a previously set value, specify a new value of 0.
    For more information, see Replacing Auto Scaling Instances Based on Maximum Instance Lifetime in the Amazon EC2 Auto Scaling User Guide .
    Valid Range: Minimum value of 0.
    
    
    """
    pass

