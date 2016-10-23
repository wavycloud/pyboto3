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


def attach_instances(InstanceIds=None, AutoScalingGroupName=None):
    """
    :param InstanceIds: One or more instance IDs.
            (string) --
            
    :type InstanceIds: list
    :param AutoScalingGroupName: [REQUIRED]
            The name of the group.
            
    :type AutoScalingGroupName: string
    """
    pass


def attach_load_balancer_target_groups(AutoScalingGroupName=None, TargetGroupARNs=None):
    """
    :param AutoScalingGroupName: [REQUIRED]
            The name of the Auto Scaling group.
            
    :type AutoScalingGroupName: string
    :param TargetGroupARNs: [REQUIRED]
            The Amazon Resource Names (ARN) of the target groups.
            (string) --
            
    :type TargetGroupARNs: list
    """
    pass


def attach_load_balancers(AutoScalingGroupName=None, LoadBalancerNames=None):
    """
    :param AutoScalingGroupName: [REQUIRED]
            The name of the group.
            
    :type AutoScalingGroupName: string
    :param LoadBalancerNames: [REQUIRED]
            One or more load balancer names.
            (string) --
            
    :type LoadBalancerNames: list
    """
    pass


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


def complete_lifecycle_action(LifecycleHookName=None, AutoScalingGroupName=None, LifecycleActionToken=None,
                              LifecycleActionResult=None, InstanceId=None):
    """
    :param LifecycleHookName: [REQUIRED]
            The name of the lifecycle hook.
            
    :type LifecycleHookName: string
    :param AutoScalingGroupName: [REQUIRED]
            The name of the group for the lifecycle hook.
            
    :type AutoScalingGroupName: string
    :param LifecycleActionToken: A universally unique identifier (UUID) that identifies a specific lifecycle action associated with an instance. Auto Scaling sends this token to the notification target you specified when you created the lifecycle hook.
    :type LifecycleActionToken: string
    :param LifecycleActionResult: [REQUIRED]
            The action for the group to take. This parameter can be either CONTINUE or ABANDON .
            
    :type LifecycleActionResult: string
    :param InstanceId: The ID of the instance.
    :type InstanceId: string
    """
    pass


def create_auto_scaling_group(AutoScalingGroupName=None, LaunchConfigurationName=None, InstanceId=None, MinSize=None,
                              MaxSize=None, DesiredCapacity=None, DefaultCooldown=None, AvailabilityZones=None,
                              LoadBalancerNames=None, TargetGroupARNs=None, HealthCheckType=None,
                              HealthCheckGracePeriod=None, PlacementGroup=None, VPCZoneIdentifier=None,
                              TerminationPolicies=None, NewInstancesProtectedFromScaleIn=None, Tags=None):
    """
    :param AutoScalingGroupName: [REQUIRED]
            The name of the group. This name must be unique within the scope of your AWS account.
            
    :type AutoScalingGroupName: string
    :param LaunchConfigurationName: The name of the launch configuration. Alternatively, specify an EC2 instance instead of a launch configuration.
    :type LaunchConfigurationName: string
    :param InstanceId: The ID of the instance used to create a launch configuration for the group. Alternatively, specify a launch configuration instead of an EC2 instance.
            When you specify an ID of an instance, Auto Scaling creates a new launch configuration and associates it with the group. This launch configuration derives its attributes from the specified instance, with the exception of the block device mapping.
            For more information, see Create an Auto Scaling Group Using an EC2 Instance in the Auto Scaling User Guide .
            
    :type InstanceId: string
    :param MinSize: [REQUIRED]
            The minimum size of the group.
            
    :type MinSize: integer
    :param MaxSize: [REQUIRED]
            The maximum size of the group.
            
    :type MaxSize: integer
    :param DesiredCapacity: The number of EC2 instances that should be running in the group. This number must be greater than or equal to the minimum size of the group and less than or equal to the maximum size of the group.
    :type DesiredCapacity: integer
    :param DefaultCooldown: The amount of time, in seconds, after a scaling activity completes before another scaling activity can start. The default is 300.
            For more information, see Auto Scaling Cooldowns in the Auto Scaling User Guide .
            
    :type DefaultCooldown: integer
    :param AvailabilityZones: One or more Availability Zones for the group. This parameter is optional if you specify one or more subnets.
            (string) --
            
    :type AvailabilityZones: list
    :param LoadBalancerNames: One or more Classic load balancers. To specify an Application load balancer, use TargetGroupARNs instead.
            For more information, see Using a Load Balancer With an Auto Scaling Group in the Auto Scaling User Guide .
            (string) --
            
    :type LoadBalancerNames: list
    :param TargetGroupARNs: The Amazon Resource Names (ARN) of the target groups.
            (string) --
            
    :type TargetGroupARNs: list
    :param HealthCheckType: The service to use for the health checks. The valid values are EC2 and ELB .
            By default, health checks use Amazon EC2 instance status checks to determine the health of an instance. For more information, see Health Checks in the Auto Scaling User Guide .
            
    :type HealthCheckType: string
    :param HealthCheckGracePeriod: The amount of time, in seconds, that Auto Scaling waits before checking the health status of an EC2 instance that has come into service. During this time, any health check failures for the instance are ignored. The default is 0.
            This parameter is required if you are adding an ELB health check.
            For more information, see Health Checks in the Auto Scaling User Guide .
            
    :type HealthCheckGracePeriod: integer
    :param PlacementGroup: The name of the placement group into which you'll launch your instances, if any. For more information, see Placement Groups in the Amazon Elastic Compute Cloud User Guide .
    :type PlacementGroup: string
    :param VPCZoneIdentifier: A comma-separated list of subnet identifiers for your virtual private cloud (VPC).
            If you specify subnets and Availability Zones with this call, ensure that the subnets' Availability Zones match the Availability Zones specified.
            For more information, see Launching Auto Scaling Instances in a VPC in the Auto Scaling User Guide .
            
    :type VPCZoneIdentifier: string
    :param TerminationPolicies: One or more termination policies used to select the instance to terminate. These policies are executed in the order that they are listed.
            For more information, see Controlling Which Instances Auto Scaling Terminates During Scale In in the Auto Scaling User Guide .
            (string) --
            
    :type TerminationPolicies: list
    :param NewInstancesProtectedFromScaleIn: Indicates whether newly launched instances are protected from termination by Auto Scaling when scaling in.
    :type NewInstancesProtectedFromScaleIn: boolean
    :param Tags: One or more tags.
            For more information, see Tagging Auto Scaling Groups and Instances in the Auto Scaling User Guide .
            (dict) --Describes a tag for an Auto Scaling group.
            ResourceId (string) --The name of the group.
            ResourceType (string) --The type of resource. The only supported value is auto-scaling-group .
            Key (string) -- [REQUIRED]The tag key.
            Value (string) --The tag value.
            PropagateAtLaunch (boolean) --Determines whether the tag is added to new instances as they are launched in the group.
            
            
    :type Tags: list
    """
    pass


def create_launch_configuration(LaunchConfigurationName=None, ImageId=None, KeyName=None, SecurityGroups=None,
                                ClassicLinkVPCId=None, ClassicLinkVPCSecurityGroups=None, UserData=None,
                                InstanceId=None, InstanceType=None, KernelId=None, RamdiskId=None,
                                BlockDeviceMappings=None, InstanceMonitoring=None, SpotPrice=None,
                                IamInstanceProfile=None, EbsOptimized=None, AssociatePublicIpAddress=None,
                                PlacementTenancy=None):
    """
    :param LaunchConfigurationName: [REQUIRED]
            The name of the launch configuration. This name must be unique within the scope of your AWS account.
            
    :type LaunchConfigurationName: string
    :param ImageId: The ID of the Amazon Machine Image (AMI) to use to launch your EC2 instances. For more information, see Finding an AMI in the Amazon Elastic Compute Cloud User Guide .
    :type ImageId: string
    :param KeyName: The name of the key pair. For more information, see Amazon EC2 Key Pairs in the Amazon Elastic Compute Cloud User Guide .
    :type KeyName: string
    :param SecurityGroups: One or more security groups with which to associate the instances.
            If your instances are launched in EC2-Classic, you can either specify security group names or the security group IDs. For more information about security groups for EC2-Classic, see Amazon EC2 Security Groups in the Amazon Elastic Compute Cloud User Guide .
            If your instances are launched into a VPC, specify security group IDs. For more information, see Security Groups for Your VPC in the Amazon Virtual Private Cloud User Guide .
            (string) --
            
    :type SecurityGroups: list
    :param ClassicLinkVPCId: The ID of a ClassicLink-enabled VPC to link your EC2-Classic instances to. This parameter is supported only if you are launching EC2-Classic instances. For more information, see ClassicLink in the Amazon Elastic Compute Cloud User Guide .
    :type ClassicLinkVPCId: string
    :param ClassicLinkVPCSecurityGroups: The IDs of one or more security groups for the specified ClassicLink-enabled VPC. This parameter is required if you specify a ClassicLink-enabled VPC, and is not supported otherwise. For more information, see ClassicLink in the Amazon Elastic Compute Cloud User Guide .
            (string) --
            
    :type ClassicLinkVPCSecurityGroups: list
    :param UserData: The user data to make available to the launched EC2 instances. For more information, see Instance Metadata and User Data in the Amazon Elastic Compute Cloud User Guide .
            This value will be base64 encoded automatically. Do not base64 encode this value prior to performing the operation.
            
    :type UserData: string
    :param InstanceId: The ID of the instance to use to create the launch configuration.
            The new launch configuration derives attributes from the instance, with the exception of the block device mapping.
            To create a launch configuration with a block device mapping or override any other instance attributes, specify them as part of the same request.
            For more information, see Create a Launch Configuration Using an EC2 Instance in the Auto Scaling User Guide .
            
    :type InstanceId: string
    :param InstanceType: The instance type of the EC2 instance. For information about available instance types, see Available Instance Types in the Amazon Elastic Compute Cloud User Guide.
    :type InstanceType: string
    :param KernelId: The ID of the kernel associated with the AMI.
    :type KernelId: string
    :param RamdiskId: The ID of the RAM disk associated with the AMI.
    :type RamdiskId: string
    :param BlockDeviceMappings: One or more mappings that specify how block devices are exposed to the instance. For more information, see Block Device Mapping in the Amazon Elastic Compute Cloud User Guide .
            (dict) --Describes a block device mapping.
            VirtualName (string) --The name of the virtual device (for example, ephemeral0 ).
            DeviceName (string) -- [REQUIRED]The device name exposed to the EC2 instance (for example, /dev/sdh or xvdh ).
            Ebs (dict) --The information about the Amazon EBS volume.
            SnapshotId (string) --The ID of the snapshot.
            VolumeSize (integer) --The volume size, in GiB. For standard volumes, specify a value from 1 to 1,024. For io1 volumes, specify a value from 4 to 16,384. For gp2 volumes, specify a value from 1 to 16,384. If you specify a snapshot, the volume size must be equal to or larger than the snapshot size.
            Default: If you create a volume from a snapshot and you don't specify a volume size, the default is the snapshot size.
            VolumeType (string) --The volume type. For more information, see Amazon EBS Volume Types in the Amazon Elastic Compute Cloud User Guide .
            Valid values: standard | io1 | gp2
            Default: standard
            DeleteOnTermination (boolean) --Indicates whether the volume is deleted on instance termination.
            Default: true
            Iops (integer) --The number of I/O operations per second (IOPS) to provision for the volume.
            Constraint: Required when the volume type is io1 .
            Encrypted (boolean) --Indicates whether the volume should be encrypted. Encrypted EBS volumes must be attached to instances that support Amazon EBS encryption. Volumes that are created from encrypted snapshots are automatically encrypted. There is no way to create an encrypted volume from an unencrypted snapshot or an unencrypted volume from an encrypted snapshot. For more information, see Amazon EBS Encryption in the Amazon Elastic Compute Cloud User Guide .
            NoDevice (boolean) --Suppresses a device mapping.
            If this parameter is true for the root device, the instance might fail the EC2 health check. Auto Scaling launches a replacement instance if the instance fails the health check.
            
            
    :type BlockDeviceMappings: list
    :param InstanceMonitoring: Enables detailed monitoring (true ) or basic monitoring (false ) for the Auto Scaling instances.
            Enabled (boolean) --If True , instance monitoring is enabled.
            
    :type InstanceMonitoring: dict
    :param SpotPrice: The maximum hourly price to be paid for any Spot Instance launched to fulfill the request. Spot Instances are launched when the price you specify exceeds the current Spot market price. For more information, see Launching Spot Instances in Your Auto Scaling Group in the Auto Scaling User Guide .
    :type SpotPrice: string
    :param IamInstanceProfile: The name or the Amazon Resource Name (ARN) of the instance profile associated with the IAM role for the instance.
            EC2 instances launched with an IAM role will automatically have AWS security credentials available. You can use IAM roles with Auto Scaling to automatically enable applications running on your EC2 instances to securely access other AWS resources. For more information, see Launch Auto Scaling Instances with an IAM Role in the Auto Scaling User Guide .
            
    :type IamInstanceProfile: string
    :param EbsOptimized: Indicates whether the instance is optimized for Amazon EBS I/O. By default, the instance is not optimized for EBS I/O. The optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal I/O performance. This optimization is not available with all instance types. Additional usage charges apply. For more information, see Amazon EBS-Optimized Instances in the Amazon Elastic Compute Cloud User Guide .
    :type EbsOptimized: boolean
    :param AssociatePublicIpAddress: Used for groups that launch instances into a virtual private cloud (VPC). Specifies whether to assign a public IP address to each instance. For more information, see Launching Auto Scaling Instances in a VPC in the Auto Scaling User Guide .
            If you specify this parameter, be sure to specify at least one subnet when you create your group.
            Default: If the instance is launched into a default subnet, the default is true . If the instance is launched into a nondefault subnet, the default is false . For more information, see Supported Platforms in the Amazon Elastic Compute Cloud User Guide .
            
    :type AssociatePublicIpAddress: boolean
    :param PlacementTenancy: The tenancy of the instance. An instance with a tenancy of dedicated runs on single-tenant hardware and can only be launched into a VPC.
            You must set the value of this parameter to dedicated if want to launch Dedicated Instances into a shared tenancy VPC (VPC with instance placement tenancy attribute set to default ).
            If you specify this parameter, be sure to specify at least one subnet when you create your group.
            For more information, see Launching Auto Scaling Instances in a VPC in the Auto Scaling User Guide .
            Valid values: default | dedicated
            
    :type PlacementTenancy: string
    """
    pass


def create_or_update_tags(Tags=None):
    """
    :param Tags: [REQUIRED]
            One or more tags.
            (dict) --Describes a tag for an Auto Scaling group.
            ResourceId (string) --The name of the group.
            ResourceType (string) --The type of resource. The only supported value is auto-scaling-group .
            Key (string) -- [REQUIRED]The tag key.
            Value (string) --The tag value.
            PropagateAtLaunch (boolean) --Determines whether the tag is added to new instances as they are launched in the group.
            
            ReturnsNone
            
    :type Tags: list
    """
    pass


def delete_auto_scaling_group(AutoScalingGroupName=None, ForceDelete=None):
    """
    :param AutoScalingGroupName: [REQUIRED]
            The name of the group to delete.
            
    :type AutoScalingGroupName: string
    :param ForceDelete: Specifies that the group will be deleted along with all instances associated with the group, without waiting for all instances to be terminated. This parameter also deletes any lifecycle actions associated with the group.
    :type ForceDelete: boolean
    """
    pass


def delete_launch_configuration(LaunchConfigurationName=None):
    """
    :param LaunchConfigurationName: [REQUIRED]
            The name of the launch configuration.
            ReturnsNone
            
    :type LaunchConfigurationName: string
    """
    pass


def delete_lifecycle_hook(LifecycleHookName=None, AutoScalingGroupName=None):
    """
    :param LifecycleHookName: [REQUIRED]
            The name of the lifecycle hook.
            
    :type LifecycleHookName: string
    :param AutoScalingGroupName: [REQUIRED]
            The name of the Auto Scaling group for the lifecycle hook.
            
    :type AutoScalingGroupName: string
    """
    pass


def delete_notification_configuration(AutoScalingGroupName=None, TopicARN=None):
    """
    :param AutoScalingGroupName: [REQUIRED]
            The name of the Auto Scaling group.
            
    :type AutoScalingGroupName: string
    :param TopicARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) topic.
            
    :type TopicARN: string
    """
    pass


def delete_policy(AutoScalingGroupName=None, PolicyName=None):
    """
    :param AutoScalingGroupName: The name of the Auto Scaling group.
    :type AutoScalingGroupName: string
    :param PolicyName: [REQUIRED]
            The name or Amazon Resource Name (ARN) of the policy.
            
    :type PolicyName: string
    """
    pass


def delete_scheduled_action(AutoScalingGroupName=None, ScheduledActionName=None):
    """
    :param AutoScalingGroupName: [REQUIRED]
            The name of the Auto Scaling group.
            
    :type AutoScalingGroupName: string
    :param ScheduledActionName: [REQUIRED]
            The name of the action to delete.
            
    :type ScheduledActionName: string
    """
    pass


def delete_tags(Tags=None):
    """
    :param Tags: [REQUIRED]
            One or more tags.
            (dict) --Describes a tag for an Auto Scaling group.
            ResourceId (string) --The name of the group.
            ResourceType (string) --The type of resource. The only supported value is auto-scaling-group .
            Key (string) -- [REQUIRED]The tag key.
            Value (string) --The tag value.
            PropagateAtLaunch (boolean) --Determines whether the tag is added to new instances as they are launched in the group.
            
            ReturnsNone
            
    :type Tags: list
    """
    pass


def describe_account_limits():
    """
    """
    pass


def describe_adjustment_types():
    """
    """
    pass


def describe_auto_scaling_groups(AutoScalingGroupNames=None, NextToken=None, MaxRecords=None):
    """
    :param AutoScalingGroupNames: The group names. If you omit this parameter, all Auto Scaling groups are described.
            (string) --
            
    :type AutoScalingGroupNames: list
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)
    :type NextToken: string
    :param MaxRecords: The maximum number of items to return with this call.
    :type MaxRecords: integer
    """
    pass


def describe_auto_scaling_instances(InstanceIds=None, MaxRecords=None, NextToken=None):
    """
    :param InstanceIds: The instances to describe; up to 50 instance IDs. If you omit this parameter, all Auto Scaling instances are described. If you specify an ID that does not exist, it is ignored with no error.
            (string) --
            
    :type InstanceIds: list
    :param MaxRecords: The maximum number of items to return with this call.
    :type MaxRecords: integer
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)
    :type NextToken: string
    """
    pass


def describe_auto_scaling_notification_types():
    """
    """
    pass


def describe_launch_configurations(LaunchConfigurationNames=None, NextToken=None, MaxRecords=None):
    """
    :param LaunchConfigurationNames: The launch configuration names. If you omit this parameter, all launch configurations are described.
            (string) --
            
    :type LaunchConfigurationNames: list
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)
    :type NextToken: string
    :param MaxRecords: The maximum number of items to return with this call. The default is 100.
    :type MaxRecords: integer
    """
    pass


def describe_lifecycle_hook_types():
    """
    """
    pass


def describe_lifecycle_hooks(AutoScalingGroupName=None, LifecycleHookNames=None):
    """
    :param AutoScalingGroupName: [REQUIRED]
            The name of the group.
            
    :type AutoScalingGroupName: string
    :param LifecycleHookNames: The names of one or more lifecycle hooks. If you omit this parameter, all lifecycle hooks are described.
            (string) --
            
    :type LifecycleHookNames: list
    """
    pass


def describe_load_balancer_target_groups(AutoScalingGroupName=None, NextToken=None, MaxRecords=None):
    """
    :param AutoScalingGroupName: [REQUIRED]
            The name of the Auto Scaling group.
            
    :type AutoScalingGroupName: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)
    :type NextToken: string
    :param MaxRecords: The maximum number of items to return with this call.
    :type MaxRecords: integer
    """
    pass


def describe_load_balancers(AutoScalingGroupName=None, NextToken=None, MaxRecords=None):
    """
    :param AutoScalingGroupName: [REQUIRED]
            The name of the group.
            
    :type AutoScalingGroupName: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)
    :type NextToken: string
    :param MaxRecords: The maximum number of items to return with this call.
    :type MaxRecords: integer
    """
    pass


def describe_metric_collection_types():
    """
    """
    pass


def describe_notification_configurations(AutoScalingGroupNames=None, NextToken=None, MaxRecords=None):
    """
    :param AutoScalingGroupNames: The name of the group.
            (string) --
            
    :type AutoScalingGroupNames: list
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)
    :type NextToken: string
    :param MaxRecords: The maximum number of items to return with this call.
    :type MaxRecords: integer
    """
    pass


def describe_policies(AutoScalingGroupName=None, PolicyNames=None, PolicyTypes=None, NextToken=None, MaxRecords=None):
    """
    :param AutoScalingGroupName: The name of the group.
    :type AutoScalingGroupName: string
    :param PolicyNames: One or more policy names or policy ARNs to be described. If you omit this parameter, all policy names are described. If an group name is provided, the results are limited to that group. This list is limited to 50 items. If you specify an unknown policy name, it is ignored with no error.
            (string) --
            
    :type PolicyNames: list
    :param PolicyTypes: One or more policy types. Valid values are SimpleScaling and StepScaling .
            (string) --
            
    :type PolicyTypes: list
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)
    :type NextToken: string
    :param MaxRecords: The maximum number of items to be returned with each call.
    :type MaxRecords: integer
    """
    pass


def describe_scaling_activities(ActivityIds=None, AutoScalingGroupName=None, MaxRecords=None, NextToken=None):
    """
    :param ActivityIds: The activity IDs of the desired scaling activities. If you omit this parameter, all activities for the past six weeks are described. If you specify an Auto Scaling group, the results are limited to that group. The list of requested activities cannot contain more than 50 items. If unknown activities are requested, they are ignored with no error.
            (string) --
            
    :type ActivityIds: list
    :param AutoScalingGroupName: The name of the group.
    :type AutoScalingGroupName: string
    :param MaxRecords: The maximum number of items to return with this call.
    :type MaxRecords: integer
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)
    :type NextToken: string
    """
    pass


def describe_scaling_process_types():
    """
    """
    pass


def describe_scheduled_actions(AutoScalingGroupName=None, ScheduledActionNames=None, StartTime=None, EndTime=None,
                               NextToken=None, MaxRecords=None):
    """
    :param AutoScalingGroupName: The name of the group.
    :type AutoScalingGroupName: string
    :param ScheduledActionNames: Describes one or more scheduled actions. If you omit this parameter, all scheduled actions are described. If you specify an unknown scheduled action, it is ignored with no error.
            You can describe up to a maximum of 50 instances with a single call. If there are more items to return, the call returns a token. To get the next set of items, repeat the call with the returned token.
            (string) --
            
    :type ScheduledActionNames: list
    :param StartTime: The earliest scheduled start time to return. If scheduled action names are provided, this parameter is ignored.
    :type StartTime: datetime
    :param EndTime: The latest scheduled start time to return. If scheduled action names are provided, this parameter is ignored.
    :type EndTime: datetime
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)
    :type NextToken: string
    :param MaxRecords: The maximum number of items to return with this call.
    :type MaxRecords: integer
    """
    pass


def describe_tags(Filters=None, NextToken=None, MaxRecords=None):
    """
    :param Filters: A filter used to scope the tags to return.
            (dict) --Describes a filter.
            Name (string) --The name of the filter. The valid values are: 'auto-scaling-group' , 'key' , 'value' , and 'propagate-at-launch' .
            Values (list) --The value of the filter.
            (string) --
            
            
    :type Filters: list
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)
    :type NextToken: string
    :param MaxRecords: The maximum number of items to return with this call.
    :type MaxRecords: integer
    """
    pass


def describe_termination_policy_types():
    """
    """
    pass


def detach_instances(InstanceIds=None, AutoScalingGroupName=None, ShouldDecrementDesiredCapacity=None):
    """
    :param InstanceIds: One or more instance IDs.
            (string) --
            
    :type InstanceIds: list
    :param AutoScalingGroupName: [REQUIRED]
            The name of the group.
            
    :type AutoScalingGroupName: string
    :param ShouldDecrementDesiredCapacity: [REQUIRED]
            If True , the Auto Scaling group decrements the desired capacity value by the number of instances detached.
            
    :type ShouldDecrementDesiredCapacity: boolean
    """
    pass


def detach_load_balancer_target_groups(AutoScalingGroupName=None, TargetGroupARNs=None):
    """
    :param AutoScalingGroupName: [REQUIRED]
            The name of the Auto Scaling group.
            
    :type AutoScalingGroupName: string
    :param TargetGroupARNs: [REQUIRED]
            The Amazon Resource Names (ARN) of the target groups.
            (string) --
            
    :type TargetGroupARNs: list
    """
    pass


def detach_load_balancers(AutoScalingGroupName=None, LoadBalancerNames=None):
    """
    :param AutoScalingGroupName: [REQUIRED]
            The name of the Auto Scaling group.
            
    :type AutoScalingGroupName: string
    :param LoadBalancerNames: [REQUIRED]
            One or more load balancer names.
            (string) --
            
    :type LoadBalancerNames: list
    """
    pass


def disable_metrics_collection(AutoScalingGroupName=None, Metrics=None):
    """
    :param AutoScalingGroupName: [REQUIRED]
            The name or Amazon Resource Name (ARN) of the group.
            
    :type AutoScalingGroupName: string
    :param Metrics: One or more of the following metrics. If you omit this parameter, all metrics are disabled.
            GroupMinSize
            GroupMaxSize
            GroupDesiredCapacity
            GroupInServiceInstances
            GroupPendingInstances
            GroupStandbyInstances
            GroupTerminatingInstances
            GroupTotalInstances
            (string) --
            
    :type Metrics: list
    """
    pass


def enable_metrics_collection(AutoScalingGroupName=None, Metrics=None, Granularity=None):
    """
    :param AutoScalingGroupName: [REQUIRED]
            The name or ARN of the Auto Scaling group.
            
    :type AutoScalingGroupName: string
    :param Metrics: One or more of the following metrics. If you omit this parameter, all metrics are enabled.
            GroupMinSize
            GroupMaxSize
            GroupDesiredCapacity
            GroupInServiceInstances
            GroupPendingInstances
            GroupStandbyInstances
            GroupTerminatingInstances
            GroupTotalInstances
            (string) --
            
    :type Metrics: list
    :param Granularity: [REQUIRED]
            The granularity to associate with the metrics to collect. The only valid value is 1Minute .
            
    :type Granularity: string
    """
    pass


def enter_standby(InstanceIds=None, AutoScalingGroupName=None, ShouldDecrementDesiredCapacity=None):
    """
    :param InstanceIds: One or more instances to move into Standby mode. You must specify at least one instance ID.
            (string) --
            
    :type InstanceIds: list
    :param AutoScalingGroupName: [REQUIRED]
            The name of the Auto Scaling group.
            
    :type AutoScalingGroupName: string
    :param ShouldDecrementDesiredCapacity: [REQUIRED]
            Specifies whether the instances moved to Standby mode count as part of the Auto Scaling group's desired capacity. If set, the desired capacity for the Auto Scaling group decrements by the number of instances moved to Standby mode.
            
    :type ShouldDecrementDesiredCapacity: boolean
    """
    pass


def execute_policy(AutoScalingGroupName=None, PolicyName=None, HonorCooldown=None, MetricValue=None,
                   BreachThreshold=None):
    """
    :param AutoScalingGroupName: The name or Amazon Resource Name (ARN) of the Auto Scaling group.
    :type AutoScalingGroupName: string
    :param PolicyName: [REQUIRED]
            The name or ARN of the policy.
            
    :type PolicyName: string
    :param HonorCooldown: If this parameter is true, Auto Scaling waits for the cooldown period to complete before executing the policy. Otherwise, Auto Scaling executes the policy without waiting for the cooldown period to complete.
            This parameter is not supported if the policy type is StepScaling .
            For more information, see Auto Scaling Cooldowns in the Auto Scaling User Guide .
            
    :type HonorCooldown: boolean
    :param MetricValue: The metric value to compare to BreachThreshold . This enables you to execute a policy of type StepScaling and determine which step adjustment to use. For example, if the breach threshold is 50 and you want to use a step adjustment with a lower bound of 0 and an upper bound of 10, you can set the metric value to 59.
            If you specify a metric value that doesn't correspond to a step adjustment for the policy, the call returns an error.
            This parameter is required if the policy type is StepScaling and not supported otherwise.
            
    :type MetricValue: float
    :param BreachThreshold: The breach threshold for the alarm.
            This parameter is required if the policy type is StepScaling and not supported otherwise.
            
    :type BreachThreshold: float
    """
    pass


def exit_standby(InstanceIds=None, AutoScalingGroupName=None):
    """
    :param InstanceIds: One or more instance IDs. You must specify at least one instance ID.
            (string) --
            
    :type InstanceIds: list
    :param AutoScalingGroupName: [REQUIRED]
            The name of the Auto Scaling group.
            
    :type AutoScalingGroupName: string
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


def put_lifecycle_hook(LifecycleHookName=None, AutoScalingGroupName=None, LifecycleTransition=None, RoleARN=None,
                       NotificationTargetARN=None, NotificationMetadata=None, HeartbeatTimeout=None,
                       DefaultResult=None):
    """
    :param LifecycleHookName: [REQUIRED]
            The name of the lifecycle hook.
            
    :type LifecycleHookName: string
    :param AutoScalingGroupName: [REQUIRED]
            The name of the Auto Scaling group to which you want to assign the lifecycle hook.
            
    :type AutoScalingGroupName: string
    :param LifecycleTransition: The instance state to which you want to attach the lifecycle hook. For a list of lifecycle hook types, see DescribeLifecycleHookTypes .
            This parameter is required for new lifecycle hooks, but optional when updating existing hooks.
            
    :type LifecycleTransition: string
    :param RoleARN: The ARN of the IAM role that allows the Auto Scaling group to publish to the specified notification target.
            This parameter is required for new lifecycle hooks, but optional when updating existing hooks.
            
    :type RoleARN: string
    :param NotificationTargetARN: The ARN of the notification target that Auto Scaling will use to notify you when an instance is in the transition state for the lifecycle hook. This target can be either an SQS queue or an SNS topic. If you specify an empty string, this overrides the current ARN.
            The notification messages sent to the target include the following information:
            AutoScalingGroupName . The name of the Auto Scaling group.
            AccountId . The AWS account ID.
            LifecycleTransition . The lifecycle hook type.
            LifecycleActionToken . The lifecycle action token.
            EC2InstanceId . The EC2 instance ID.
            LifecycleHookName . The name of the lifecycle hook.
            NotificationMetadata . User-defined information.
            This operation uses the JSON format when sending notifications to an Amazon SQS queue, and an email key/value pair format when sending notifications to an Amazon SNS topic.
            When you specify a notification target, Auto Scaling sends it a test message. Test messages contains the following additional key/value pair: 'Event': 'autoscaling:TEST_NOTIFICATION' .
            
    :type NotificationTargetARN: string
    :param NotificationMetadata: Contains additional information that you want to include any time Auto Scaling sends a message to the notification target.
    :type NotificationMetadata: string
    :param HeartbeatTimeout: The amount of time, in seconds, that can elapse before the lifecycle hook times out. When the lifecycle hook times out, Auto Scaling performs the default action. You can prevent the lifecycle hook from timing out by calling RecordLifecycleActionHeartbeat . The default is 3600 seconds (1 hour).
    :type HeartbeatTimeout: integer
    :param DefaultResult: Defines the action the Auto Scaling group should take when the lifecycle hook timeout elapses or if an unexpected failure occurs. This parameter can be either CONTINUE or ABANDON . The default value is ABANDON .
    :type DefaultResult: string
    """
    pass


def put_notification_configuration(AutoScalingGroupName=None, TopicARN=None, NotificationTypes=None):
    """
    :param AutoScalingGroupName: [REQUIRED]
            The name of the Auto Scaling group.
            
    :type AutoScalingGroupName: string
    :param TopicARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) topic.
            
    :type TopicARN: string
    :param NotificationTypes: [REQUIRED]
            The type of event that will cause the notification to be sent. For details about notification types supported by Auto Scaling, see DescribeAutoScalingNotificationTypes .
            (string) --
            
    :type NotificationTypes: list
    """
    pass


def put_scaling_policy(AutoScalingGroupName=None, PolicyName=None, PolicyType=None, AdjustmentType=None,
                       MinAdjustmentStep=None, MinAdjustmentMagnitude=None, ScalingAdjustment=None, Cooldown=None,
                       MetricAggregationType=None, StepAdjustments=None, EstimatedInstanceWarmup=None):
    """
    :param AutoScalingGroupName: [REQUIRED]
            The name or ARN of the group.
            
    :type AutoScalingGroupName: string
    :param PolicyName: [REQUIRED]
            The name of the policy.
            
    :type PolicyName: string
    :param PolicyType: The policy type. Valid values are SimpleScaling and StepScaling . If the policy type is null, the value is treated as SimpleScaling .
    :type PolicyType: string
    :param AdjustmentType: [REQUIRED]
            The adjustment type. Valid values are ChangeInCapacity , ExactCapacity , and PercentChangeInCapacity .
            For more information, see Dynamic Scaling in the Auto Scaling User Guide .
            
    :type AdjustmentType: string
    :param MinAdjustmentStep: Available for backward compatibility. Use MinAdjustmentMagnitude instead.
    :type MinAdjustmentStep: integer
    :param MinAdjustmentMagnitude: The minimum number of instances to scale. If the value of AdjustmentType is PercentChangeInCapacity , the scaling policy changes the DesiredCapacity of the Auto Scaling group by at least this many instances. Otherwise, the error is ValidationError .
    :type MinAdjustmentMagnitude: integer
    :param ScalingAdjustment: The amount by which to scale, based on the specified adjustment type. A positive value adds to the current capacity while a negative number removes from the current capacity.
            This parameter is required if the policy type is SimpleScaling and not supported otherwise.
            
    :type ScalingAdjustment: integer
    :param Cooldown: The amount of time, in seconds, after a scaling activity completes and before the next scaling activity can start. If this parameter is not specified, the default cooldown period for the group applies.
            This parameter is not supported unless the policy type is SimpleScaling .
            For more information, see Auto Scaling Cooldowns in the Auto Scaling User Guide .
            
    :type Cooldown: integer
    :param MetricAggregationType: The aggregation type for the CloudWatch metrics. Valid values are Minimum , Maximum , and Average . If the aggregation type is null, the value is treated as Average .
            This parameter is not supported if the policy type is SimpleScaling .
            
    :type MetricAggregationType: string
    :param StepAdjustments: A set of adjustments that enable you to scale based on the size of the alarm breach.
            This parameter is required if the policy type is StepScaling and not supported otherwise.
            (dict) --Describes an adjustment based on the difference between the value of the aggregated CloudWatch metric and the breach threshold that you've defined for the alarm.
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
            ScalingAdjustment (integer) -- [REQUIRED]The amount by which to scale, based on the specified adjustment type. A positive value adds to the current capacity while a negative number removes from the current capacity.
            
            
    :type StepAdjustments: list
    :param EstimatedInstanceWarmup: The estimated time, in seconds, until a newly launched instance can contribute to the CloudWatch metrics. The default is to use the value specified for the default cooldown period for the group.
            This parameter is not supported if the policy type is SimpleScaling .
            
    :type EstimatedInstanceWarmup: integer
    """
    pass


def put_scheduled_update_group_action(AutoScalingGroupName=None, ScheduledActionName=None, Time=None, StartTime=None,
                                      EndTime=None, Recurrence=None, MinSize=None, MaxSize=None, DesiredCapacity=None):
    """
    :param AutoScalingGroupName: [REQUIRED]
            The name or Amazon Resource Name (ARN) of the Auto Scaling group.
            
    :type AutoScalingGroupName: string
    :param ScheduledActionName: [REQUIRED]
            The name of this scaling action.
            
    :type ScheduledActionName: string
    :param Time: This parameter is deprecated.
    :type Time: datetime
    :param StartTime: The time for this action to start, in 'YYYY-MM-DDThh:mm:ssZ' format in UTC/GMT only (for example, 2014-06-01T00:00:00Z ).
            If you try to schedule your action in the past, Auto Scaling returns an error message.
            When StartTime and EndTime are specified with Recurrence , they form the boundaries of when the recurring action starts and stops.
            
    :type StartTime: datetime
    :param EndTime: The time for this action to end.
    :type EndTime: datetime
    :param Recurrence: The time when recurring future actions will start. Start time is specified by the user following the Unix cron syntax format. For more information, see Cron in Wikipedia.
            When StartTime and EndTime are specified with Recurrence , they form the boundaries of when the recurring action will start and stop.
            
    :type Recurrence: string
    :param MinSize: The minimum size for the Auto Scaling group.
    :type MinSize: integer
    :param MaxSize: The maximum size for the Auto Scaling group.
    :type MaxSize: integer
    :param DesiredCapacity: The number of EC2 instances that should be running in the group.
    :type DesiredCapacity: integer
    """
    pass


def record_lifecycle_action_heartbeat(LifecycleHookName=None, AutoScalingGroupName=None, LifecycleActionToken=None,
                                      InstanceId=None):
    """
    :param LifecycleHookName: [REQUIRED]
            The name of the lifecycle hook.
            
    :type LifecycleHookName: string
    :param AutoScalingGroupName: [REQUIRED]
            The name of the Auto Scaling group for the hook.
            
    :type AutoScalingGroupName: string
    :param LifecycleActionToken: A token that uniquely identifies a specific lifecycle action associated with an instance. Auto Scaling sends this token to the notification target you specified when you created the lifecycle hook.
    :type LifecycleActionToken: string
    :param InstanceId: The ID of the instance.
    :type InstanceId: string
    """
    pass


def resume_processes(AutoScalingGroupName=None, ScalingProcesses=None):
    """
    :param AutoScalingGroupName: [REQUIRED]
            The name or Amazon Resource Name (ARN) of the Auto Scaling group.
            
    :type AutoScalingGroupName: string
    :param ScalingProcesses: One or more of the following processes. If you omit this parameter, all processes are specified.
            Launch
            Terminate
            HealthCheck
            ReplaceUnhealthy
            AZRebalance
            AlarmNotification
            ScheduledActions
            AddToLoadBalancer
            (string) --
            
    :type ScalingProcesses: list
    """
    pass


def set_desired_capacity(AutoScalingGroupName=None, DesiredCapacity=None, HonorCooldown=None):
    """
    :param AutoScalingGroupName: [REQUIRED]
            The name of the Auto Scaling group.
            
    :type AutoScalingGroupName: string
    :param DesiredCapacity: [REQUIRED]
            The number of EC2 instances that should be running in the Auto Scaling group.
            
    :type DesiredCapacity: integer
    :param HonorCooldown: By default, SetDesiredCapacity overrides any cooldown period associated with the Auto Scaling group. Specify True to make Auto Scaling to wait for the cool-down period associated with the Auto Scaling group to complete before initiating a scaling activity to set your Auto Scaling group to its new capacity.
    :type HonorCooldown: boolean
    """
    pass


def set_instance_health(InstanceId=None, HealthStatus=None, ShouldRespectGracePeriod=None):
    """
    :param InstanceId: [REQUIRED]
            The ID of the instance.
            
    :type InstanceId: string
    :param HealthStatus: [REQUIRED]
            The health status of the instance. Set to Healthy if you want the instance to remain in service. Set to Unhealthy if you want the instance to be out of service. Auto Scaling will terminate and replace the unhealthy instance.
            
    :type HealthStatus: string
    :param ShouldRespectGracePeriod: If the Auto Scaling group of the specified instance has a HealthCheckGracePeriod specified for the group, by default, this call will respect the grace period. Set this to False , if you do not want the call to respect the grace period associated with the group.
            For more information, see the description of the health check grace period for CreateAutoScalingGroup .
            
    :type ShouldRespectGracePeriod: boolean
    """
    pass


def set_instance_protection(InstanceIds=None, AutoScalingGroupName=None, ProtectedFromScaleIn=None):
    """
    :param InstanceIds: [REQUIRED]
            One or more instance IDs.
            (string) --
            
    :type InstanceIds: list
    :param AutoScalingGroupName: [REQUIRED]
            The name of the group.
            
    :type AutoScalingGroupName: string
    :param ProtectedFromScaleIn: [REQUIRED]
            Indicates whether the instance is protected from termination by Auto Scaling when scaling in.
            
    :type ProtectedFromScaleIn: boolean
    """
    pass


def suspend_processes(AutoScalingGroupName=None, ScalingProcesses=None):
    """
    :param AutoScalingGroupName: [REQUIRED]
            The name or Amazon Resource Name (ARN) of the Auto Scaling group.
            
    :type AutoScalingGroupName: string
    :param ScalingProcesses: One or more of the following processes. If you omit this parameter, all processes are specified.
            Launch
            Terminate
            HealthCheck
            ReplaceUnhealthy
            AZRebalance
            AlarmNotification
            ScheduledActions
            AddToLoadBalancer
            (string) --
            
    :type ScalingProcesses: list
    """
    pass


def terminate_instance_in_auto_scaling_group(InstanceId=None, ShouldDecrementDesiredCapacity=None):
    """
    :param InstanceId: [REQUIRED]
            The ID of the instance.
            
    :type InstanceId: string
    :param ShouldDecrementDesiredCapacity: [REQUIRED]
            If true , terminating the instance also decrements the size of the Auto Scaling group.
            
    :type ShouldDecrementDesiredCapacity: boolean
    """
    pass


def update_auto_scaling_group(AutoScalingGroupName=None, LaunchConfigurationName=None, MinSize=None, MaxSize=None,
                              DesiredCapacity=None, DefaultCooldown=None, AvailabilityZones=None, HealthCheckType=None,
                              HealthCheckGracePeriod=None, PlacementGroup=None, VPCZoneIdentifier=None,
                              TerminationPolicies=None, NewInstancesProtectedFromScaleIn=None):
    """
    :param AutoScalingGroupName: [REQUIRED]
            The name of the Auto Scaling group.
            
    :type AutoScalingGroupName: string
    :param LaunchConfigurationName: The name of the launch configuration.
    :type LaunchConfigurationName: string
    :param MinSize: The minimum size of the Auto Scaling group.
    :type MinSize: integer
    :param MaxSize: The maximum size of the Auto Scaling group.
    :type MaxSize: integer
    :param DesiredCapacity: The number of EC2 instances that should be running in the Auto Scaling group. This number must be greater than or equal to the minimum size of the group and less than or equal to the maximum size of the group.
    :type DesiredCapacity: integer
    :param DefaultCooldown: The amount of time, in seconds, after a scaling activity completes before another scaling activity can start. The default is 300.
            For more information, see Auto Scaling Cooldowns in the Auto Scaling User Guide .
            
    :type DefaultCooldown: integer
    :param AvailabilityZones: One or more Availability Zones for the group.
            (string) --
            
    :type AvailabilityZones: list
    :param HealthCheckType: The service to use for the health checks. The valid values are EC2 and ELB .
    :type HealthCheckType: string
    :param HealthCheckGracePeriod: The amount of time, in seconds, that Auto Scaling waits before checking the health status of an EC2 instance that has come into service. The default is 0.
            For more information, see Health Checks in the Auto Scaling User Guide .
            
    :type HealthCheckGracePeriod: integer
    :param PlacementGroup: The name of the placement group into which you'll launch your instances, if any. For more information, see Placement Groups in the Amazon Elastic Compute Cloud User Guide .
    :type PlacementGroup: string
    :param VPCZoneIdentifier: The ID of the subnet, if you are launching into a VPC. You can specify several subnets in a comma-separated list.
            When you specify VPCZoneIdentifier with AvailabilityZones , ensure that the subnets' Availability Zones match the values you specify for AvailabilityZones .
            For more information, see Launching Auto Scaling Instances in a VPC in the Auto Scaling User Guide .
            
    :type VPCZoneIdentifier: string
    :param TerminationPolicies: A standalone termination policy or a list of termination policies used to select the instance to terminate. The policies are executed in the order that they are listed.
            For more information, see Controlling Which Instances Auto Scaling Terminates During Scale In in the Auto Scaling User Guide .
            (string) --
            
    :type TerminationPolicies: list
    :param NewInstancesProtectedFromScaleIn: Indicates whether newly launched instances are protected from termination by Auto Scaling when scaling in.
    :type NewInstancesProtectedFromScaleIn: boolean
    """
    pass
