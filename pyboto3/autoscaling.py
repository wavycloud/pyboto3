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
    When you attach instances, Auto Scaling increases the desired capacity of the group by the number of instances being attached. If the number of instances being attached plus the desired capacity of the group exceeds the maximum size of the group, the operation fails.
    If there is a Classic Load Balancer attached to your Auto Scaling group, the instances are also registered with the load balancer. If there are target groups attached to your Auto Scaling group, the instances are also registered with the target groups.
    For more information, see Attach EC2 Instances to Your Auto Scaling Group in the Auto Scaling User Guide .
    See also: AWS API Documentation
    
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
    :param InstanceIds: One or more instance IDs.
            (string) --
            

    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: [REQUIRED]
            The name of the group.
            

    :return: response = client.attach_instances(
        AutoScalingGroupName='my-auto-scaling-group',
        InstanceIds=[
            'i-93633f9b',
        ],
    )
    
    print(response)
    
    
    """
    pass

def attach_load_balancer_target_groups(AutoScalingGroupName=None, TargetGroupARNs=None):
    """
    Attaches one or more target groups to the specified Auto Scaling group.
    To describe the target groups for an Auto Scaling group, use  DescribeLoadBalancerTargetGroups . To detach the target group from the Auto Scaling group, use  DetachLoadBalancerTargetGroups .
    For more information, see Attach a Load Balancer to Your Auto Scaling Group in the Auto Scaling User Guide .
    See also: AWS API Documentation
    
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
    :param AutoScalingGroupName: [REQUIRED]
            The name of the Auto Scaling group.
            

    :type TargetGroupARNs: list
    :param TargetGroupARNs: [REQUIRED]
            The Amazon Resource Names (ARN) of the target groups.
            (string) --
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def attach_load_balancers(AutoScalingGroupName=None, LoadBalancerNames=None):
    """
    Attaches one or more Classic Load Balancers to the specified Auto Scaling group.
    To attach an Application Load Balancer instead, see  AttachLoadBalancerTargetGroups .
    To describe the load balancers for an Auto Scaling group, use  DescribeLoadBalancers . To detach the load balancer from the Auto Scaling group, use  DetachLoadBalancers .
    For more information, see Attach a Load Balancer to Your Auto Scaling Group in the Auto Scaling User Guide .
    See also: AWS API Documentation
    
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
    :param AutoScalingGroupName: [REQUIRED]
            The name of the group.
            

    :type LoadBalancerNames: list
    :param LoadBalancerNames: [REQUIRED]
            One or more load balancer names.
            (string) --
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
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

def complete_lifecycle_action(LifecycleHookName=None, AutoScalingGroupName=None, LifecycleActionToken=None, LifecycleActionResult=None, InstanceId=None):
    """
    Completes the lifecycle action for the specified token or instance with the specified result.
    This step is a part of the procedure for adding a lifecycle hook to an Auto Scaling group:
    For more information, see Auto Scaling Lifecycle in the Auto Scaling User Guide .
    See also: AWS API Documentation
    
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
    :param LifecycleHookName: [REQUIRED]
            The name of the lifecycle hook.
            

    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: [REQUIRED]
            The name of the group for the lifecycle hook.
            

    :type LifecycleActionToken: string
    :param LifecycleActionToken: A universally unique identifier (UUID) that identifies a specific lifecycle action associated with an instance. Auto Scaling sends this token to the notification target you specified when you created the lifecycle hook.

    :type LifecycleActionResult: string
    :param LifecycleActionResult: [REQUIRED]
            The action for the group to take. This parameter can be either CONTINUE or ABANDON .
            

    :type InstanceId: string
    :param InstanceId: The ID of the instance.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    LifecycleHookName (string) -- [REQUIRED]
    The name of the lifecycle hook.
    
    AutoScalingGroupName (string) -- [REQUIRED]
    The name of the group for the lifecycle hook.
    
    LifecycleActionToken (string) -- A universally unique identifier (UUID) that identifies a specific lifecycle action associated with an instance. Auto Scaling sends this token to the notification target you specified when you created the lifecycle hook.
    LifecycleActionResult (string) -- [REQUIRED]
    The action for the group to take. This parameter can be either CONTINUE or ABANDON .
    
    InstanceId (string) -- The ID of the instance.
    
    """
    pass

def create_auto_scaling_group(AutoScalingGroupName=None, LaunchConfigurationName=None, InstanceId=None, MinSize=None, MaxSize=None, DesiredCapacity=None, DefaultCooldown=None, AvailabilityZones=None, LoadBalancerNames=None, TargetGroupARNs=None, HealthCheckType=None, HealthCheckGracePeriod=None, PlacementGroup=None, VPCZoneIdentifier=None, TerminationPolicies=None, NewInstancesProtectedFromScaleIn=None, Tags=None):
    """
    Creates an Auto Scaling group with the specified name and attributes.
    If you exceed your maximum limit of Auto Scaling groups, which by default is 20 per region, the call fails. For information about viewing and updating this limit, see  DescribeAccountLimits .
    For more information, see Auto Scaling Groups in the Auto Scaling User Guide .
    See also: AWS API Documentation
    
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
    
    
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: [REQUIRED]
            The name of the group. This name must be unique within the scope of your AWS account.
            

    :type LaunchConfigurationName: string
    :param LaunchConfigurationName: The name of the launch configuration. Alternatively, specify an EC2 instance instead of a launch configuration.

    :type InstanceId: string
    :param InstanceId: The ID of the instance used to create a launch configuration for the group. Alternatively, specify a launch configuration instead of an EC2 instance.
            When you specify an ID of an instance, Auto Scaling creates a new launch configuration and associates it with the group. This launch configuration derives its attributes from the specified instance, with the exception of the block device mapping.
            For more information, see Create an Auto Scaling Group Using an EC2 Instance in the Auto Scaling User Guide .
            

    :type MinSize: integer
    :param MinSize: [REQUIRED]
            The minimum size of the group.
            

    :type MaxSize: integer
    :param MaxSize: [REQUIRED]
            The maximum size of the group.
            

    :type DesiredCapacity: integer
    :param DesiredCapacity: The number of EC2 instances that should be running in the group. This number must be greater than or equal to the minimum size of the group and less than or equal to the maximum size of the group. If you do not specify a desired capacity, the default is the minimum size of the group.

    :type DefaultCooldown: integer
    :param DefaultCooldown: The amount of time, in seconds, after a scaling activity completes before another scaling activity can start. The default is 300.
            For more information, see Auto Scaling Cooldowns in the Auto Scaling User Guide .
            

    :type AvailabilityZones: list
    :param AvailabilityZones: One or more Availability Zones for the group. This parameter is optional if you specify one or more subnets.
            (string) --
            

    :type LoadBalancerNames: list
    :param LoadBalancerNames: One or more Classic Load Balancers. To specify an Application Load Balancer, use TargetGroupARNs instead.
            For more information, see Using a Load Balancer With an Auto Scaling Group in the Auto Scaling User Guide .
            (string) --
            

    :type TargetGroupARNs: list
    :param TargetGroupARNs: The Amazon Resource Names (ARN) of the target groups.
            (string) --
            

    :type HealthCheckType: string
    :param HealthCheckType: The service to use for the health checks. The valid values are EC2 and ELB .
            By default, health checks use Amazon EC2 instance status checks to determine the health of an instance. For more information, see Health Checks in the Auto Scaling User Guide .
            

    :type HealthCheckGracePeriod: integer
    :param HealthCheckGracePeriod: The amount of time, in seconds, that Auto Scaling waits before checking the health status of an EC2 instance that has come into service. During this time, any health check failures for the instance are ignored. The default is 0.
            This parameter is required if you are adding an ELB health check.
            For more information, see Health Checks in the Auto Scaling User Guide .
            

    :type PlacementGroup: string
    :param PlacementGroup: The name of the placement group into which you'll launch your instances, if any. For more information, see Placement Groups in the Amazon Elastic Compute Cloud User Guide .

    :type VPCZoneIdentifier: string
    :param VPCZoneIdentifier: A comma-separated list of subnet identifiers for your virtual private cloud (VPC).
            If you specify subnets and Availability Zones with this call, ensure that the subnets' Availability Zones match the Availability Zones specified.
            For more information, see Launching Auto Scaling Instances in a VPC in the Auto Scaling User Guide .
            

    :type TerminationPolicies: list
    :param TerminationPolicies: One or more termination policies used to select the instance to terminate. These policies are executed in the order that they are listed.
            For more information, see Controlling Which Instances Auto Scaling Terminates During Scale In in the Auto Scaling User Guide .
            (string) --
            

    :type NewInstancesProtectedFromScaleIn: boolean
    :param NewInstancesProtectedFromScaleIn: Indicates whether newly launched instances are protected from termination by Auto Scaling when scaling in.

    :type Tags: list
    :param Tags: One or more tags.
            For more information, see Tagging Auto Scaling Groups and Instances in the Auto Scaling User Guide .
            (dict) --Describes a tag for an Auto Scaling group.
            ResourceId (string) --The name of the group.
            ResourceType (string) --The type of resource. The only supported value is auto-scaling-group .
            Key (string) -- [REQUIRED]The tag key.
            Value (string) --The tag value.
            PropagateAtLaunch (boolean) --Determines whether the tag is added to new instances as they are launched in the group.
            
            

    :return: response = client.create_auto_scaling_group(
        AutoScalingGroupName='my-auto-scaling-group',
        LaunchConfigurationName='my-launch-config',
        MaxSize=3,
        MinSize=1,
        VPCZoneIdentifier='subnet-4176792c',
    )
    
    print(response)
    
    
    """
    pass

def create_launch_configuration(LaunchConfigurationName=None, ImageId=None, KeyName=None, SecurityGroups=None, ClassicLinkVPCId=None, ClassicLinkVPCSecurityGroups=None, UserData=None, InstanceId=None, InstanceType=None, KernelId=None, RamdiskId=None, BlockDeviceMappings=None, InstanceMonitoring=None, SpotPrice=None, IamInstanceProfile=None, EbsOptimized=None, AssociatePublicIpAddress=None, PlacementTenancy=None):
    """
    Creates a launch configuration.
    If you exceed your maximum limit of launch configurations, which by default is 100 per region, the call fails. For information about viewing and updating this limit, see  DescribeAccountLimits .
    For more information, see Launch Configurations in the Auto Scaling User Guide .
    See also: AWS API Documentation
    
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
    :param LaunchConfigurationName: [REQUIRED]
            The name of the launch configuration. This name must be unique within the scope of your AWS account.
            

    :type ImageId: string
    :param ImageId: The ID of the Amazon Machine Image (AMI) to use to launch your EC2 instances.
            If you do not specify InstanceId , you must specify ImageId .
            For more information, see Finding an AMI in the Amazon Elastic Compute Cloud User Guide .
            

    :type KeyName: string
    :param KeyName: The name of the key pair. For more information, see Amazon EC2 Key Pairs in the Amazon Elastic Compute Cloud User Guide .

    :type SecurityGroups: list
    :param SecurityGroups: One or more security groups with which to associate the instances.
            If your instances are launched in EC2-Classic, you can either specify security group names or the security group IDs. For more information about security groups for EC2-Classic, see Amazon EC2 Security Groups in the Amazon Elastic Compute Cloud User Guide .
            If your instances are launched into a VPC, specify security group IDs. For more information, see Security Groups for Your VPC in the Amazon Virtual Private Cloud User Guide .
            (string) --
            

    :type ClassicLinkVPCId: string
    :param ClassicLinkVPCId: The ID of a ClassicLink-enabled VPC to link your EC2-Classic instances to. This parameter is supported only if you are launching EC2-Classic instances. For more information, see ClassicLink in the Amazon Elastic Compute Cloud User Guide .

    :type ClassicLinkVPCSecurityGroups: list
    :param ClassicLinkVPCSecurityGroups: The IDs of one or more security groups for the specified ClassicLink-enabled VPC. This parameter is required if you specify a ClassicLink-enabled VPC, and is not supported otherwise. For more information, see ClassicLink in the Amazon Elastic Compute Cloud User Guide .
            (string) --
            

    :type UserData: string
    :param UserData: The user data to make available to the launched EC2 instances. For more information, see Instance Metadata and User Data in the Amazon Elastic Compute Cloud User Guide .
            This value will be base64 encoded automatically. Do not base64 encode this value prior to performing the operation.
            

    :type InstanceId: string
    :param InstanceId: The ID of the instance to use to create the launch configuration. The new launch configuration derives attributes from the instance, with the exception of the block device mapping.
            If you do not specify InstanceId , you must specify both ImageId and InstanceType .
            To create a launch configuration with a block device mapping or override any other instance attributes, specify them as part of the same request.
            For more information, see Create a Launch Configuration Using an EC2 Instance in the Auto Scaling User Guide .
            

    :type InstanceType: string
    :param InstanceType: The instance type of the EC2 instance.
            If you do not specify InstanceId , you must specify InstanceType .
            For information about available instance types, see Available Instance Types in the Amazon Elastic Compute Cloud User Guide.
            

    :type KernelId: string
    :param KernelId: The ID of the kernel associated with the AMI.

    :type RamdiskId: string
    :param RamdiskId: The ID of the RAM disk associated with the AMI.

    :type BlockDeviceMappings: list
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
            
            

    :type InstanceMonitoring: dict
    :param InstanceMonitoring: Enables detailed monitoring (true ) or basic monitoring (false ) for the Auto Scaling instances. The default is true .
            Enabled (boolean) --If true , detailed monitoring is enabled. Otherwise, basic monitoring is enabled.
            

    :type SpotPrice: string
    :param SpotPrice: The maximum hourly price to be paid for any Spot Instance launched to fulfill the request. Spot Instances are launched when the price you specify exceeds the current Spot market price. For more information, see Launching Spot Instances in Your Auto Scaling Group in the Auto Scaling User Guide .

    :type IamInstanceProfile: string
    :param IamInstanceProfile: The name or the Amazon Resource Name (ARN) of the instance profile associated with the IAM role for the instance.
            EC2 instances launched with an IAM role will automatically have AWS security credentials available. You can use IAM roles with Auto Scaling to automatically enable applications running on your EC2 instances to securely access other AWS resources. For more information, see Launch Auto Scaling Instances with an IAM Role in the Auto Scaling User Guide .
            

    :type EbsOptimized: boolean
    :param EbsOptimized: Indicates whether the instance is optimized for Amazon EBS I/O. By default, the instance is not optimized for EBS I/O. The optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal I/O performance. This optimization is not available with all instance types. Additional usage charges apply. For more information, see Amazon EBS-Optimized Instances in the Amazon Elastic Compute Cloud User Guide .

    :type AssociatePublicIpAddress: boolean
    :param AssociatePublicIpAddress: Used for groups that launch instances into a virtual private cloud (VPC). Specifies whether to assign a public IP address to each instance. For more information, see Launching Auto Scaling Instances in a VPC in the Auto Scaling User Guide .
            If you specify this parameter, be sure to specify at least one subnet when you create your group.
            Default: If the instance is launched into a default subnet, the default is true . If the instance is launched into a nondefault subnet, the default is false . For more information, see Supported Platforms in the Amazon Elastic Compute Cloud User Guide .
            

    :type PlacementTenancy: string
    :param PlacementTenancy: The tenancy of the instance. An instance with a tenancy of dedicated runs on single-tenant hardware and can only be launched into a VPC.
            You must set the value of this parameter to dedicated if want to launch Dedicated Instances into a shared tenancy VPC (VPC with instance placement tenancy attribute set to default ).
            If you specify this parameter, be sure to specify at least one subnet when you create your group.
            For more information, see Launching Auto Scaling Instances in a VPC in the Auto Scaling User Guide .
            Valid values: default | dedicated
            

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
    
    
    """
    pass

def create_or_update_tags(Tags=None):
    """
    Creates or updates tags for the specified Auto Scaling group.
    When you specify a tag with a key that already exists, the operation overwrites the previous tag definition, and you do not get an error message.
    For more information, see Tagging Auto Scaling Groups and Instances in the Auto Scaling User Guide .
    See also: AWS API Documentation
    
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
    :param Tags: [REQUIRED]
            One or more tags.
            (dict) --Describes a tag for an Auto Scaling group.
            ResourceId (string) --The name of the group.
            ResourceType (string) --The type of resource. The only supported value is auto-scaling-group .
            Key (string) -- [REQUIRED]The tag key.
            Value (string) --The tag value.
            PropagateAtLaunch (boolean) --Determines whether the tag is added to new instances as they are launched in the group.
            
            

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
    To remove instances from the Auto Scaling group before deleting it, call  DetachInstances with the list of instances and the option to decrement the desired capacity so that Auto Scaling does not launch replacement instances.
    To terminate all instances before deleting the Auto Scaling group, call  UpdateAutoScalingGroup and set the minimum size and desired capacity of the Auto Scaling group to zero.
    See also: AWS API Documentation
    
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
    :param AutoScalingGroupName: [REQUIRED]
            The name of the group to delete.
            

    :type ForceDelete: boolean
    :param ForceDelete: Specifies that the group will be deleted along with all instances associated with the group, without waiting for all instances to be terminated. This parameter also deletes any lifecycle actions associated with the group.

    :return: response = client.delete_auto_scaling_group(
        AutoScalingGroupName='my-auto-scaling-group',
    )
    
    print(response)
    
    
    """
    pass

def delete_launch_configuration(LaunchConfigurationName=None):
    """
    Deletes the specified launch configuration.
    The launch configuration must not be attached to an Auto Scaling group. When this call completes, the launch configuration is no longer available for use.
    See also: AWS API Documentation
    
    Examples
    This example deletes the specified launch configuration.
    Expected Output:
    
    :example: response = client.delete_launch_configuration(
        LaunchConfigurationName='string'
    )
    
    
    :type LaunchConfigurationName: string
    :param LaunchConfigurationName: [REQUIRED]
            The name of the launch configuration.
            

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
    
    Examples
    This example deletes the specified lifecycle hook.
    Expected Output:
    
    :example: response = client.delete_lifecycle_hook(
        LifecycleHookName='string',
        AutoScalingGroupName='string'
    )
    
    
    :type LifecycleHookName: string
    :param LifecycleHookName: [REQUIRED]
            The name of the lifecycle hook.
            

    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: [REQUIRED]
            The name of the Auto Scaling group for the lifecycle hook.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_notification_configuration(AutoScalingGroupName=None, TopicARN=None):
    """
    Deletes the specified notification.
    See also: AWS API Documentation
    
    Examples
    This example deletes the specified notification from the specified Auto Scaling group.
    Expected Output:
    
    :example: response = client.delete_notification_configuration(
        AutoScalingGroupName='string',
        TopicARN='string'
    )
    
    
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: [REQUIRED]
            The name of the Auto Scaling group.
            

    :type TopicARN: string
    :param TopicARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) topic.
            

    :return: response = client.delete_notification_configuration(
        AutoScalingGroupName='my-auto-scaling-group',
        TopicARN='arn:aws:sns:us-west-2:123456789012:my-sns-topic',
    )
    
    print(response)
    
    
    """
    pass

def delete_policy(AutoScalingGroupName=None, PolicyName=None):
    """
    Deletes the specified Auto Scaling policy.
    Deleting a policy deletes the underlying alarm action, but does not delete the alarm, even if it no longer has an associated action.
    See also: AWS API Documentation
    
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
    :param PolicyName: [REQUIRED]
            The name or Amazon Resource Name (ARN) of the policy.
            

    :return: response = client.delete_policy(
        AutoScalingGroupName='my-auto-scaling-group',
        PolicyName='ScaleIn',
    )
    
    print(response)
    
    
    """
    pass

def delete_scheduled_action(AutoScalingGroupName=None, ScheduledActionName=None):
    """
    Deletes the specified scheduled action.
    See also: AWS API Documentation
    
    Examples
    This example deletes the specified scheduled action from the specified Auto Scaling group.
    Expected Output:
    
    :example: response = client.delete_scheduled_action(
        AutoScalingGroupName='string',
        ScheduledActionName='string'
    )
    
    
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: [REQUIRED]
            The name of the Auto Scaling group.
            

    :type ScheduledActionName: string
    :param ScheduledActionName: [REQUIRED]
            The name of the action to delete.
            

    :return: response = client.delete_scheduled_action(
        AutoScalingGroupName='my-auto-scaling-group',
        ScheduledActionName='my-scheduled-action',
    )
    
    print(response)
    
    
    """
    pass

def delete_tags(Tags=None):
    """
    Deletes the specified tags.
    See also: AWS API Documentation
    
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
    :param Tags: [REQUIRED]
            One or more tags.
            (dict) --Describes a tag for an Auto Scaling group.
            ResourceId (string) --The name of the group.
            ResourceType (string) --The type of resource. The only supported value is auto-scaling-group .
            Key (string) -- [REQUIRED]The tag key.
            Value (string) --The tag value.
            PropagateAtLaunch (boolean) --Determines whether the tag is added to new instances as they are launched in the group.
            
            

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
    Describes the current Auto Scaling resource limits for your AWS account.
    For information about requesting an increase in these limits, see AWS Service Limits in the Amazon Web Services General Reference .
    See also: AWS API Documentation
    
    Examples
    This example describes the Auto Scaling limits for your AWS account.
    Expected Output:
    
    :example: response = client.describe_account_limits()
    
    
    :rtype: dict
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
    Describes the policy adjustment types for use with  PutScalingPolicy .
    See also: AWS API Documentation
    
    Examples
    This example describes the available adjustment types.
    Expected Output:
    
    :example: response = client.describe_adjustment_types()
    
    
    :rtype: dict
    :return: {
        'AdjustmentTypes': [
            {
                'AdjustmentType': 'string'
            },
        ]
    }
    
    
    """
    pass

def describe_auto_scaling_groups(AutoScalingGroupNames=None, NextToken=None, MaxRecords=None):
    """
    Describes one or more Auto Scaling groups.
    See also: AWS API Documentation
    
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
    :param AutoScalingGroupNames: The group names. If you omit this parameter, all Auto Scaling groups are described.
            (string) --
            

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of items to return with this call. The default value is 50 and the maximum value is 100.

    :rtype: dict
    :return: {
        'AutoScalingGroups': [
            {
                'AutoScalingGroupName': 'string',
                'AutoScalingGroupARN': 'string',
                'LaunchConfigurationName': 'string',
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
                        'AvailabilityZone': 'string',
                        'LifecycleState': 'Pending'|'Pending:Wait'|'Pending:Proceed'|'Quarantined'|'InService'|'Terminating'|'Terminating:Wait'|'Terminating:Proceed'|'Terminated'|'Detaching'|'Detached'|'EnteringStandby'|'Standby',
                        'HealthStatus': 'string',
                        'LaunchConfigurationName': 'string',
                        'ProtectedFromScaleIn': True|False
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
                'NewInstancesProtectedFromScaleIn': True|False
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
    :param InstanceIds: The instances to describe; up to 50 instance IDs. If you omit this parameter, all Auto Scaling instances are described. If you specify an ID that does not exist, it is ignored with no error.
            (string) --
            

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of items to return with this call. The default value is 50 and the maximum value is 100.

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :rtype: dict
    :return: {
        'AutoScalingInstances': [
            {
                'InstanceId': 'string',
                'AutoScalingGroupName': 'string',
                'AvailabilityZone': 'string',
                'LifecycleState': 'string',
                'HealthStatus': 'string',
                'LaunchConfigurationName': 'string',
                'ProtectedFromScaleIn': True|False
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def describe_auto_scaling_notification_types():
    """
    Describes the notification types that are supported by Auto Scaling.
    See also: AWS API Documentation
    
    Examples
    This example describes the available notification types.
    Expected Output:
    
    :example: response = client.describe_auto_scaling_notification_types()
    
    
    :rtype: dict
    :return: {
        'AutoScalingNotificationTypes': [
            'string',
        ]
    }
    
    
    """
    pass

def describe_launch_configurations(LaunchConfigurationNames=None, NextToken=None, MaxRecords=None):
    """
    Describes one or more launch configurations.
    See also: AWS API Documentation
    
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
    :param LaunchConfigurationNames: The launch configuration names. If you omit this parameter, all launch configurations are described.
            (string) --
            

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of items to return with this call. The default value is 50 and the maximum value is 100.

    :rtype: dict
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
    See also: AWS API Documentation
    
    Examples
    This example describes the available lifecycle hook types.
    Expected Output:
    
    :example: response = client.describe_lifecycle_hook_types()
    
    
    :rtype: dict
    :return: {
        'LifecycleHookTypes': [
            'string',
        ]
    }
    
    
    """
    pass

def describe_lifecycle_hooks(AutoScalingGroupName=None, LifecycleHookNames=None):
    """
    Describes the lifecycle hooks for the specified Auto Scaling group.
    See also: AWS API Documentation
    
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
    :param AutoScalingGroupName: [REQUIRED]
            The name of the group.
            

    :type LifecycleHookNames: list
    :param LifecycleHookNames: The names of one or more lifecycle hooks. If you omit this parameter, all lifecycle hooks are described.
            (string) --
            

    :rtype: dict
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
    Pause the instance after it launches, but before it is put into service
    Pause the instance as it terminates, but before it is fully terminated
    
    """
    pass

def describe_load_balancer_target_groups(AutoScalingGroupName=None, NextToken=None, MaxRecords=None):
    """
    Describes the target groups for the specified Auto Scaling group.
    See also: AWS API Documentation
    
    Examples
    This example describes the target groups attached to the specified Auto Scaling group.
    Expected Output:
    
    :example: response = client.describe_load_balancer_target_groups(
        AutoScalingGroupName='string',
        NextToken='string',
        MaxRecords=123
    )
    
    
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: [REQUIRED]
            The name of the Auto Scaling group.
            

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of items to return with this call. The default value is 50 and the maximum value is 100.

    :rtype: dict
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
    Note that this operation describes only Classic Load Balancers. If you have Application Load Balancers, use  DescribeLoadBalancerTargetGroups instead.
    See also: AWS API Documentation
    
    Examples
    This example describes the load balancers attached to the specified Auto Scaling group.
    Expected Output:
    
    :example: response = client.describe_load_balancers(
        AutoScalingGroupName='string',
        NextToken='string',
        MaxRecords=123
    )
    
    
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: [REQUIRED]
            The name of the group.
            

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of items to return with this call. The default value is 50 and the maximum value is 100.

    :rtype: dict
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
    Describes the available CloudWatch metrics for Auto Scaling.
    Note that the GroupStandbyInstances metric is not returned by default. You must explicitly request this metric when calling  EnableMetricsCollection .
    See also: AWS API Documentation
    
    Examples
    This example describes the available metric collection types.
    Expected Output:
    
    :example: response = client.describe_metric_collection_types()
    
    
    :rtype: dict
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
    
    
    """
    pass

def describe_notification_configurations(AutoScalingGroupNames=None, NextToken=None, MaxRecords=None):
    """
    Describes the notification actions associated with the specified Auto Scaling group.
    See also: AWS API Documentation
    
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
    :param AutoScalingGroupNames: The name of the group.
            (string) --
            

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of items to return with this call. The default value is 50 and the maximum value is 100.

    :rtype: dict
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
    :param AutoScalingGroupName: The name of the group.

    :type PolicyNames: list
    :param PolicyNames: One or more policy names or policy ARNs to be described. If you omit this parameter, all policy names are described. If an group name is provided, the results are limited to that group. This list is limited to 50 items. If you specify an unknown policy name, it is ignored with no error.
            (string) --
            

    :type PolicyTypes: list
    :param PolicyTypes: One or more policy types. Valid values are SimpleScaling and StepScaling .
            (string) --
            

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of items to be returned with each call. The default value is 50 and the maximum value is 100.

    :rtype: dict
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
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    If you want the adjustment to be triggered when the metric is greater than or equal to 50 and less than 60, specify a lower bound of 0 and an upper bound of 10.
    If you want the adjustment to be triggered when the metric is greater than 40 and less than or equal to 50, specify a lower bound of -10 and an upper bound of 0.
    
    """
    pass

def describe_scaling_activities(ActivityIds=None, AutoScalingGroupName=None, MaxRecords=None, NextToken=None):
    """
    Describes one or more scaling activities for the specified Auto Scaling group.
    See also: AWS API Documentation
    
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
    :param ActivityIds: The activity IDs of the desired scaling activities. If you omit this parameter, all activities for the past six weeks are described. If you specify an Auto Scaling group, the results are limited to that group. The list of requested activities cannot contain more than 50 items. If unknown activities are requested, they are ignored with no error.
            (string) --
            

    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: The name of the group.

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of items to return with this call. The default value is 100.

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :rtype: dict
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
    
    
    """
    pass

def describe_scaling_process_types():
    """
    Describes the scaling process types for use with  ResumeProcesses and  SuspendProcesses .
    See also: AWS API Documentation
    
    Examples
    This example describes the Auto Scaling process types.
    Expected Output:
    
    :example: response = client.describe_scaling_process_types()
    
    
    :rtype: dict
    :return: {
        'Processes': [
            {
                'ProcessName': 'string'
            },
        ]
    }
    
    
    """
    pass

def describe_scheduled_actions(AutoScalingGroupName=None, ScheduledActionNames=None, StartTime=None, EndTime=None, NextToken=None, MaxRecords=None):
    """
    Describes the actions scheduled for your Auto Scaling group that haven't run. To describe the actions that have already run, use  DescribeScalingActivities .
    See also: AWS API Documentation
    
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
    :param AutoScalingGroupName: The name of the group.

    :type ScheduledActionNames: list
    :param ScheduledActionNames: Describes one or more scheduled actions. If you omit this parameter, all scheduled actions are described. If you specify an unknown scheduled action, it is ignored with no error.
            You can describe up to a maximum of 50 instances with a single call. If there are more items to return, the call returns a token. To get the next set of items, repeat the call with the returned token.
            (string) --
            

    :type StartTime: datetime
    :param StartTime: The earliest scheduled start time to return. If scheduled action names are provided, this parameter is ignored.

    :type EndTime: datetime
    :param EndTime: The latest scheduled start time to return. If scheduled action names are provided, this parameter is ignored.

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of items to return with this call. The default value is 50 and the maximum value is 100.

    :rtype: dict
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
    
    
    """
    pass

def describe_tags(Filters=None, NextToken=None, MaxRecords=None):
    """
    Describes the specified tags.
    You can use filters to limit the results. For example, you can query for the tags for a specific Auto Scaling group. You can specify multiple values for a filter. A tag must match at least one of the specified values for it to be included in the results.
    You can also specify multiple filters. The result includes information for a particular tag only if it matches all the filters. If there's no match, no special message is returned.
    See also: AWS API Documentation
    
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
    :param Filters: A filter used to scope the tags to return.
            (dict) --Describes a filter.
            Name (string) --The name of the filter. The valid values are: 'auto-scaling-group' , 'key' , 'value' , and 'propagate-at-launch' .
            Values (list) --The value of the filter.
            (string) --
            
            

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :type MaxRecords: integer
    :param MaxRecords: The maximum number of items to return with this call. The default value is 50 and the maximum value is 100.

    :rtype: dict
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
    
    
    """
    pass

def describe_termination_policy_types():
    """
    Describes the termination policies supported by Auto Scaling.
    See also: AWS API Documentation
    
    Examples
    This example describes the available termination policy types.
    Expected Output:
    
    :example: response = client.describe_termination_policy_types()
    
    
    :rtype: dict
    :return: {
        'TerminationPolicyTypes': [
            'string',
        ]
    }
    
    
    """
    pass

def detach_instances(InstanceIds=None, AutoScalingGroupName=None, ShouldDecrementDesiredCapacity=None):
    """
    Removes one or more instances from the specified Auto Scaling group.
    After the instances are detached, you can manage them independent of the Auto Scaling group.
    If you do not specify the option to decrement the desired capacity, Auto Scaling launches instances to replace the ones that are detached.
    If there is a Classic Load Balancer attached to the Auto Scaling group, the instances are deregistered from the load balancer. If there are target groups attached to the Auto Scaling group, the instances are deregistered from the target groups.
    For more information, see Detach EC2 Instances from Your Auto Scaling Group in the Auto Scaling User Guide .
    See also: AWS API Documentation
    
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
    :param InstanceIds: One or more instance IDs.
            (string) --
            

    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: [REQUIRED]
            The name of the group.
            

    :type ShouldDecrementDesiredCapacity: boolean
    :param ShouldDecrementDesiredCapacity: [REQUIRED]
            If True , the Auto Scaling group decrements the desired capacity value by the number of instances detached.
            

    :rtype: dict
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
    
    
    """
    pass

def detach_load_balancer_target_groups(AutoScalingGroupName=None, TargetGroupARNs=None):
    """
    Detaches one or more target groups from the specified Auto Scaling group.
    See also: AWS API Documentation
    
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
    :param AutoScalingGroupName: [REQUIRED]
            The name of the Auto Scaling group.
            

    :type TargetGroupARNs: list
    :param TargetGroupARNs: [REQUIRED]
            The Amazon Resource Names (ARN) of the target groups.
            (string) --
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def detach_load_balancers(AutoScalingGroupName=None, LoadBalancerNames=None):
    """
    Detaches one or more Classic Load Balancers from the specified Auto Scaling group.
    Note that this operation detaches only Classic Load Balancers. If you have Application Load Balancers, use  DetachLoadBalancerTargetGroups instead.
    When you detach a load balancer, it enters the Removing state while deregistering the instances in the group. When all instances are deregistered, then you can no longer describe the load balancer using  DescribeLoadBalancers . Note that the instances remain running.
    See also: AWS API Documentation
    
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
    :param AutoScalingGroupName: [REQUIRED]
            The name of the Auto Scaling group.
            

    :type LoadBalancerNames: list
    :param LoadBalancerNames: [REQUIRED]
            One or more load balancer names.
            (string) --
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def disable_metrics_collection(AutoScalingGroupName=None, Metrics=None):
    """
    Disables group metrics for the specified Auto Scaling group.
    See also: AWS API Documentation
    
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
    :param AutoScalingGroupName: [REQUIRED]
            The name or Amazon Resource Name (ARN) of the group.
            

    :type Metrics: list
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
            

    :return: response = client.disable_metrics_collection(
        AutoScalingGroupName='my-auto-scaling-group',
        Metrics=[
            'GroupDesiredCapacity',
        ],
    )
    
    print(response)
    
    
    """
    pass

def enable_metrics_collection(AutoScalingGroupName=None, Metrics=None, Granularity=None):
    """
    Enables group metrics for the specified Auto Scaling group. For more information, see Monitoring Your Auto Scaling Groups and Instances in the Auto Scaling User Guide .
    See also: AWS API Documentation
    
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
    :param AutoScalingGroupName: [REQUIRED]
            The name or ARN of the Auto Scaling group.
            

    :type Metrics: list
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
            

    :type Granularity: string
    :param Granularity: [REQUIRED]
            The granularity to associate with the metrics to collect. The only valid value is 1Minute .
            

    :return: response = client.enable_metrics_collection(
        AutoScalingGroupName='my-auto-scaling-group',
        Granularity='1Minute',
    )
    
    print(response)
    
    
    """
    pass

def enter_standby(InstanceIds=None, AutoScalingGroupName=None, ShouldDecrementDesiredCapacity=None):
    """
    Moves the specified instances into the standby state.
    For more information, see Temporarily Removing Instances from Your Auto Scaling Group in the Auto Scaling User Guide .
    See also: AWS API Documentation
    
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
    :param InstanceIds: One or more instances to move into Standby mode. You must specify at least one instance ID.
            (string) --
            

    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: [REQUIRED]
            The name of the Auto Scaling group.
            

    :type ShouldDecrementDesiredCapacity: boolean
    :param ShouldDecrementDesiredCapacity: [REQUIRED]
            Specifies whether the instances moved to Standby mode count as part of the Auto Scaling group's desired capacity. If set, the desired capacity for the Auto Scaling group decrements by the number of instances moved to Standby mode.
            

    :rtype: dict
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
    
    
    """
    pass

def execute_policy(AutoScalingGroupName=None, PolicyName=None, HonorCooldown=None, MetricValue=None, BreachThreshold=None):
    """
    Executes the specified policy.
    See also: AWS API Documentation
    
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
    :param AutoScalingGroupName: The name or Amazon Resource Name (ARN) of the Auto Scaling group.

    :type PolicyName: string
    :param PolicyName: [REQUIRED]
            The name or ARN of the policy.
            

    :type HonorCooldown: boolean
    :param HonorCooldown: If this parameter is true, Auto Scaling waits for the cooldown period to complete before executing the policy. Otherwise, Auto Scaling executes the policy without waiting for the cooldown period to complete.
            This parameter is not supported if the policy type is StepScaling .
            For more information, see Auto Scaling Cooldowns in the Auto Scaling User Guide .
            

    :type MetricValue: float
    :param MetricValue: The metric value to compare to BreachThreshold . This enables you to execute a policy of type StepScaling and determine which step adjustment to use. For example, if the breach threshold is 50 and you want to use a step adjustment with a lower bound of 0 and an upper bound of 10, you can set the metric value to 59.
            If you specify a metric value that doesn't correspond to a step adjustment for the policy, the call returns an error.
            This parameter is required if the policy type is StepScaling and not supported otherwise.
            

    :type BreachThreshold: float
    :param BreachThreshold: The breach threshold for the alarm.
            This parameter is required if the policy type is StepScaling and not supported otherwise.
            

    :return: response = client.execute_policy(
        AutoScalingGroupName='my-auto-scaling-group',
        HonorCooldown=True,
        PolicyName='ScaleIn',
    )
    
    print(response)
    
    
    """
    pass

def exit_standby(InstanceIds=None, AutoScalingGroupName=None):
    """
    Moves the specified instances out of the standby state.
    For more information, see Temporarily Removing Instances from Your Auto Scaling Group in the Auto Scaling User Guide .
    See also: AWS API Documentation
    
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
    :param InstanceIds: One or more instance IDs. You must specify at least one instance ID.
            (string) --
            

    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: [REQUIRED]
            The name of the Auto Scaling group.
            

    :rtype: dict
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

def get_waiter():
    """
    
    """
    pass

def put_lifecycle_hook(LifecycleHookName=None, AutoScalingGroupName=None, LifecycleTransition=None, RoleARN=None, NotificationTargetARN=None, NotificationMetadata=None, HeartbeatTimeout=None, DefaultResult=None):
    """
    Creates or updates a lifecycle hook for the specified Auto Scaling Group.
    A lifecycle hook tells Auto Scaling that you want to perform an action on an instance that is not actively in service; for example, either when the instance launches or before the instance terminates.
    This step is a part of the procedure for adding a lifecycle hook to an Auto Scaling group:
    For more information, see Auto Scaling Lifecycle Hooks in the Auto Scaling User Guide .
    If you exceed your maximum limit of lifecycle hooks, which by default is 50 per Auto Scaling group, the call fails. For information about updating this limit, see AWS Service Limits in the Amazon Web Services General Reference .
    See also: AWS API Documentation
    
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
    :param LifecycleHookName: [REQUIRED]
            The name of the lifecycle hook.
            

    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: [REQUIRED]
            The name of the Auto Scaling group to which you want to assign the lifecycle hook.
            

    :type LifecycleTransition: string
    :param LifecycleTransition: The instance state to which you want to attach the lifecycle hook. For a list of lifecycle hook types, see DescribeLifecycleHookTypes .
            This parameter is required for new lifecycle hooks, but optional when updating existing hooks.
            

    :type RoleARN: string
    :param RoleARN: The ARN of the IAM role that allows the Auto Scaling group to publish to the specified notification target.
            This parameter is required for new lifecycle hooks, but optional when updating existing hooks.
            

    :type NotificationTargetARN: string
    :param NotificationTargetARN: The ARN of the notification target that Auto Scaling will use to notify you when an instance is in the transition state for the lifecycle hook. This target can be either an SQS queue or an SNS topic. If you specify an empty string, this overrides the current ARN.
            This operation uses the JSON format when sending notifications to an Amazon SQS queue, and an email key/value pair format when sending notifications to an Amazon SNS topic.
            When you specify a notification target, Auto Scaling sends it a test message. Test messages contains the following additional key/value pair: 'Event': 'autoscaling:TEST_NOTIFICATION' .
            

    :type NotificationMetadata: string
    :param NotificationMetadata: Contains additional information that you want to include any time Auto Scaling sends a message to the notification target.

    :type HeartbeatTimeout: integer
    :param HeartbeatTimeout: The amount of time, in seconds, that can elapse before the lifecycle hook times out. When the lifecycle hook times out, Auto Scaling performs the default action. You can prevent the lifecycle hook from timing out by calling RecordLifecycleActionHeartbeat . The default is 3600 seconds (1 hour).

    :type DefaultResult: string
    :param DefaultResult: Defines the action the Auto Scaling group should take when the lifecycle hook timeout elapses or if an unexpected failure occurs. This parameter can be either CONTINUE or ABANDON . The default value is ABANDON .

    :rtype: dict
    :return: {}
    
    
    :returns: 
    LifecycleHookName (string) -- [REQUIRED]
    The name of the lifecycle hook.
    
    AutoScalingGroupName (string) -- [REQUIRED]
    The name of the Auto Scaling group to which you want to assign the lifecycle hook.
    
    LifecycleTransition (string) -- The instance state to which you want to attach the lifecycle hook. For a list of lifecycle hook types, see  DescribeLifecycleHookTypes .
    This parameter is required for new lifecycle hooks, but optional when updating existing hooks.
    
    RoleARN (string) -- The ARN of the IAM role that allows the Auto Scaling group to publish to the specified notification target.
    This parameter is required for new lifecycle hooks, but optional when updating existing hooks.
    
    NotificationTargetARN (string) -- The ARN of the notification target that Auto Scaling will use to notify you when an instance is in the transition state for the lifecycle hook. This target can be either an SQS queue or an SNS topic. If you specify an empty string, this overrides the current ARN.
    This operation uses the JSON format when sending notifications to an Amazon SQS queue, and an email key/value pair format when sending notifications to an Amazon SNS topic.
    When you specify a notification target, Auto Scaling sends it a test message. Test messages contains the following additional key/value pair: "Event": "autoscaling:TEST_NOTIFICATION" .
    
    NotificationMetadata (string) -- Contains additional information that you want to include any time Auto Scaling sends a message to the notification target.
    HeartbeatTimeout (integer) -- The amount of time, in seconds, that can elapse before the lifecycle hook times out. When the lifecycle hook times out, Auto Scaling performs the default action. You can prevent the lifecycle hook from timing out by calling  RecordLifecycleActionHeartbeat . The default is 3600 seconds (1 hour).
    DefaultResult (string) -- Defines the action the Auto Scaling group should take when the lifecycle hook timeout elapses or if an unexpected failure occurs. This parameter can be either CONTINUE or ABANDON . The default value is ABANDON .
    
    """
    pass

def put_notification_configuration(AutoScalingGroupName=None, TopicARN=None, NotificationTypes=None):
    """
    Configures an Auto Scaling group to send notifications when specified events take place. Subscribers to the specified topic can have messages delivered to an endpoint such as a web server or an email address.
    This configuration overwrites any existing configuration.
    For more information see Getting SNS Notifications When Your Auto Scaling Group Scales in the Auto Scaling User Guide .
    See also: AWS API Documentation
    
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
    :param AutoScalingGroupName: [REQUIRED]
            The name of the Auto Scaling group.
            

    :type TopicARN: string
    :param TopicARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) topic.
            

    :type NotificationTypes: list
    :param NotificationTypes: [REQUIRED]
            The type of event that will cause the notification to be sent. For details about notification types supported by Auto Scaling, see DescribeAutoScalingNotificationTypes .
            (string) --
            

    :return: response = client.put_notification_configuration(
        AutoScalingGroupName='my-auto-scaling-group',
        NotificationTypes=[
            'autoscaling:TEST_NOTIFICATION',
        ],
        TopicARN='arn:aws:sns:us-west-2:123456789012:my-sns-topic',
    )
    
    print(response)
    
    
    """
    pass

def put_scaling_policy(AutoScalingGroupName=None, PolicyName=None, PolicyType=None, AdjustmentType=None, MinAdjustmentStep=None, MinAdjustmentMagnitude=None, ScalingAdjustment=None, Cooldown=None, MetricAggregationType=None, StepAdjustments=None, EstimatedInstanceWarmup=None):
    """
    Creates or updates a policy for an Auto Scaling group. To update an existing policy, use the existing policy name and set the parameters you want to change. Any existing parameter not changed in an update to an existing policy is not changed in this update request.
    If you exceed your maximum limit of step adjustments, which by default is 20 per region, the call fails. For information about updating this limit, see AWS Service Limits in the Amazon Web Services General Reference .
    See also: AWS API Documentation
    
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
        EstimatedInstanceWarmup=123
    )
    
    
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: [REQUIRED]
            The name or ARN of the group.
            

    :type PolicyName: string
    :param PolicyName: [REQUIRED]
            The name of the policy.
            

    :type PolicyType: string
    :param PolicyType: The policy type. Valid values are SimpleScaling and StepScaling . If the policy type is null, the value is treated as SimpleScaling .

    :type AdjustmentType: string
    :param AdjustmentType: [REQUIRED]
            The adjustment type. Valid values are ChangeInCapacity , ExactCapacity , and PercentChangeInCapacity .
            For more information, see Dynamic Scaling in the Auto Scaling User Guide .
            

    :type MinAdjustmentStep: integer
    :param MinAdjustmentStep: Available for backward compatibility. Use MinAdjustmentMagnitude instead.

    :type MinAdjustmentMagnitude: integer
    :param MinAdjustmentMagnitude: The minimum number of instances to scale. If the value of AdjustmentType is PercentChangeInCapacity , the scaling policy changes the DesiredCapacity of the Auto Scaling group by at least this many instances. Otherwise, the error is ValidationError .

    :type ScalingAdjustment: integer
    :param ScalingAdjustment: The amount by which to scale, based on the specified adjustment type. A positive value adds to the current capacity while a negative number removes from the current capacity.
            This parameter is required if the policy type is SimpleScaling and not supported otherwise.
            

    :type Cooldown: integer
    :param Cooldown: The amount of time, in seconds, after a scaling activity completes and before the next scaling activity can start. If this parameter is not specified, the default cooldown period for the group applies.
            This parameter is not supported unless the policy type is SimpleScaling .
            For more information, see Auto Scaling Cooldowns in the Auto Scaling User Guide .
            

    :type MetricAggregationType: string
    :param MetricAggregationType: The aggregation type for the CloudWatch metrics. Valid values are Minimum , Maximum , and Average . If the aggregation type is null, the value is treated as Average .
            This parameter is not supported if the policy type is SimpleScaling .
            

    :type StepAdjustments: list
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
            
            

    :type EstimatedInstanceWarmup: integer
    :param EstimatedInstanceWarmup: The estimated time, in seconds, until a newly launched instance can contribute to the CloudWatch metrics. The default is to use the value specified for the default cooldown period for the group.
            This parameter is not supported if the policy type is SimpleScaling .
            

    :rtype: dict
    :return: {
        'PolicyARN': 'string'
    }
    
    
    """
    pass

def put_scheduled_update_group_action(AutoScalingGroupName=None, ScheduledActionName=None, Time=None, StartTime=None, EndTime=None, Recurrence=None, MinSize=None, MaxSize=None, DesiredCapacity=None):
    """
    Creates or updates a scheduled scaling action for an Auto Scaling group. When updating a scheduled scaling action, if you leave a parameter unspecified, the corresponding value remains unchanged.
    For more information, see Scheduled Scaling in the Auto Scaling User Guide .
    See also: AWS API Documentation
    
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
    :param AutoScalingGroupName: [REQUIRED]
            The name or Amazon Resource Name (ARN) of the Auto Scaling group.
            

    :type ScheduledActionName: string
    :param ScheduledActionName: [REQUIRED]
            The name of this scaling action.
            

    :type Time: datetime
    :param Time: This parameter is deprecated.

    :type StartTime: datetime
    :param StartTime: The time for this action to start, in 'YYYY-MM-DDThh:mm:ssZ' format in UTC/GMT only (for example, 2014-06-01T00:00:00Z ).
            If you specify Recurrence and StartTime , Auto Scaling performs the action at this time, and then performs the action based on the specified recurrence.
            If you try to schedule your action in the past, Auto Scaling returns an error message.
            

    :type EndTime: datetime
    :param EndTime: The time for the recurring schedule to end. Auto Scaling does not perform the action after this time.

    :type Recurrence: string
    :param Recurrence: The recurring schedule for this action, in Unix cron syntax format. For more information, see Cron in Wikipedia.

    :type MinSize: integer
    :param MinSize: The minimum size for the Auto Scaling group.

    :type MaxSize: integer
    :param MaxSize: The maximum size for the Auto Scaling group.

    :type DesiredCapacity: integer
    :param DesiredCapacity: The number of EC2 instances that should be running in the group.

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
    
    
    """
    pass

def record_lifecycle_action_heartbeat(LifecycleHookName=None, AutoScalingGroupName=None, LifecycleActionToken=None, InstanceId=None):
    """
    Records a heartbeat for the lifecycle action associated with the specified token or instance. This extends the timeout by the length of time defined using  PutLifecycleHook .
    This step is a part of the procedure for adding a lifecycle hook to an Auto Scaling group:
    For more information, see Auto Scaling Lifecycle in the Auto Scaling User Guide .
    See also: AWS API Documentation
    
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
    :param LifecycleHookName: [REQUIRED]
            The name of the lifecycle hook.
            

    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: [REQUIRED]
            The name of the Auto Scaling group for the hook.
            

    :type LifecycleActionToken: string
    :param LifecycleActionToken: A token that uniquely identifies a specific lifecycle action associated with an instance. Auto Scaling sends this token to the notification target you specified when you created the lifecycle hook.

    :type InstanceId: string
    :param InstanceId: The ID of the instance.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    LifecycleHookName (string) -- [REQUIRED]
    The name of the lifecycle hook.
    
    AutoScalingGroupName (string) -- [REQUIRED]
    The name of the Auto Scaling group for the hook.
    
    LifecycleActionToken (string) -- A token that uniquely identifies a specific lifecycle action associated with an instance. Auto Scaling sends this token to the notification target you specified when you created the lifecycle hook.
    InstanceId (string) -- The ID of the instance.
    
    """
    pass

def resume_processes(AutoScalingGroupName=None, ScalingProcesses=None):
    """
    Resumes the specified suspended Auto Scaling processes, or all suspended process, for the specified Auto Scaling group.
    For more information, see Suspending and Resuming Auto Scaling Processes in the Auto Scaling User Guide .
    See also: AWS API Documentation
    
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
    :param AutoScalingGroupName: [REQUIRED]
            The name or Amazon Resource Name (ARN) of the Auto Scaling group.
            

    :type ScalingProcesses: list
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
            

    :return: response = client.resume_processes(
        AutoScalingGroupName='my-auto-scaling-group',
        ScalingProcesses=[
            'AlarmNotification',
        ],
    )
    
    print(response)
    
    
    """
    pass

def set_desired_capacity(AutoScalingGroupName=None, DesiredCapacity=None, HonorCooldown=None):
    """
    Sets the size of the specified Auto Scaling group.
    For more information about desired capacity, see What Is Auto Scaling? in the Auto Scaling User Guide .
    See also: AWS API Documentation
    
    Examples
    This example sets the desired capacity for the specified Auto Scaling group.
    Expected Output:
    
    :example: response = client.set_desired_capacity(
        AutoScalingGroupName='string',
        DesiredCapacity=123,
        HonorCooldown=True|False
    )
    
    
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: [REQUIRED]
            The name of the Auto Scaling group.
            

    :type DesiredCapacity: integer
    :param DesiredCapacity: [REQUIRED]
            The number of EC2 instances that should be running in the Auto Scaling group.
            

    :type HonorCooldown: boolean
    :param HonorCooldown: By default, SetDesiredCapacity overrides any cooldown period associated with the Auto Scaling group. Specify True to make Auto Scaling to wait for the cool-down period associated with the Auto Scaling group to complete before initiating a scaling activity to set your Auto Scaling group to its new capacity.

    :return: response = client.set_desired_capacity(
        AutoScalingGroupName='my-auto-scaling-group',
        DesiredCapacity=2,
        HonorCooldown=True,
    )
    
    print(response)
    
    
    """
    pass

def set_instance_health(InstanceId=None, HealthStatus=None, ShouldRespectGracePeriod=None):
    """
    Sets the health status of the specified instance.
    For more information, see Health Checks in the Auto Scaling User Guide .
    See also: AWS API Documentation
    
    Examples
    This example sets the health status of the specified instance to Unhealthy.
    Expected Output:
    
    :example: response = client.set_instance_health(
        InstanceId='string',
        HealthStatus='string',
        ShouldRespectGracePeriod=True|False
    )
    
    
    :type InstanceId: string
    :param InstanceId: [REQUIRED]
            The ID of the instance.
            

    :type HealthStatus: string
    :param HealthStatus: [REQUIRED]
            The health status of the instance. Set to Healthy if you want the instance to remain in service. Set to Unhealthy if you want the instance to be out of service. Auto Scaling will terminate and replace the unhealthy instance.
            

    :type ShouldRespectGracePeriod: boolean
    :param ShouldRespectGracePeriod: If the Auto Scaling group of the specified instance has a HealthCheckGracePeriod specified for the group, by default, this call will respect the grace period. Set this to False , if you do not want the call to respect the grace period associated with the group.
            For more information, see the description of the health check grace period for CreateAutoScalingGroup .
            

    :return: response = client.set_instance_health(
        HealthStatus='Unhealthy',
        InstanceId='i-93633f9b',
    )
    
    print(response)
    
    
    """
    pass

def set_instance_protection(InstanceIds=None, AutoScalingGroupName=None, ProtectedFromScaleIn=None):
    """
    Updates the instance protection settings of the specified instances.
    For more information, see Instance Protection in the Auto Scaling User Guide .
    See also: AWS API Documentation
    
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
    :param InstanceIds: [REQUIRED]
            One or more instance IDs.
            (string) --
            

    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: [REQUIRED]
            The name of the group.
            

    :type ProtectedFromScaleIn: boolean
    :param ProtectedFromScaleIn: [REQUIRED]
            Indicates whether the instance is protected from termination by Auto Scaling when scaling in.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def suspend_processes(AutoScalingGroupName=None, ScalingProcesses=None):
    """
    Suspends the specified Auto Scaling processes, or all processes, for the specified Auto Scaling group.
    Note that if you suspend either the Launch or Terminate process types, it can prevent other process types from functioning properly.
    To resume processes that have been suspended, use  ResumeProcesses .
    For more information, see Suspending and Resuming Auto Scaling Processes in the Auto Scaling User Guide .
    See also: AWS API Documentation
    
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
    :param AutoScalingGroupName: [REQUIRED]
            The name or Amazon Resource Name (ARN) of the Auto Scaling group.
            

    :type ScalingProcesses: list
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
            

    :return: response = client.suspend_processes(
        AutoScalingGroupName='my-auto-scaling-group',
        ScalingProcesses=[
            'AlarmNotification',
        ],
    )
    
    print(response)
    
    
    """
    pass

def terminate_instance_in_auto_scaling_group(InstanceId=None, ShouldDecrementDesiredCapacity=None):
    """
    Terminates the specified instance and optionally adjusts the desired group size.
    This call simply makes a termination request. The instance is not terminated immediately.
    See also: AWS API Documentation
    
    Examples
    This example terminates the specified instance from the specified Auto Scaling group without updating the size of the group. Auto Scaling launches a replacement instance after the specified instance terminates.
    Expected Output:
    
    :example: response = client.terminate_instance_in_auto_scaling_group(
        InstanceId='string',
        ShouldDecrementDesiredCapacity=True|False
    )
    
    
    :type InstanceId: string
    :param InstanceId: [REQUIRED]
            The ID of the instance.
            

    :type ShouldDecrementDesiredCapacity: boolean
    :param ShouldDecrementDesiredCapacity: [REQUIRED]
            If true , terminating the instance also decrements the size of the Auto Scaling group.
            

    :rtype: dict
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
    
    
    """
    pass

def update_auto_scaling_group(AutoScalingGroupName=None, LaunchConfigurationName=None, MinSize=None, MaxSize=None, DesiredCapacity=None, DefaultCooldown=None, AvailabilityZones=None, HealthCheckType=None, HealthCheckGracePeriod=None, PlacementGroup=None, VPCZoneIdentifier=None, TerminationPolicies=None, NewInstancesProtectedFromScaleIn=None):
    """
    Updates the configuration for the specified Auto Scaling group.
    The new settings take effect on any scaling activities after this call returns. Scaling activities that are currently in progress aren't affected.
    To update an Auto Scaling group with a launch configuration with InstanceMonitoring set to false , you must first disable the collection of group metrics. Otherwise, you will get an error. If you have previously enabled the collection of group metrics, you can disable it using  DisableMetricsCollection .
    Note the following:
    See also: AWS API Documentation
    
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
        NewInstancesProtectedFromScaleIn=True|False
    )
    
    
    :type AutoScalingGroupName: string
    :param AutoScalingGroupName: [REQUIRED]
            The name of the Auto Scaling group.
            

    :type LaunchConfigurationName: string
    :param LaunchConfigurationName: The name of the launch configuration.

    :type MinSize: integer
    :param MinSize: The minimum size of the Auto Scaling group.

    :type MaxSize: integer
    :param MaxSize: The maximum size of the Auto Scaling group.

    :type DesiredCapacity: integer
    :param DesiredCapacity: The number of EC2 instances that should be running in the Auto Scaling group. This number must be greater than or equal to the minimum size of the group and less than or equal to the maximum size of the group.

    :type DefaultCooldown: integer
    :param DefaultCooldown: The amount of time, in seconds, after a scaling activity completes before another scaling activity can start. The default is 300.
            For more information, see Auto Scaling Cooldowns in the Auto Scaling User Guide .
            

    :type AvailabilityZones: list
    :param AvailabilityZones: One or more Availability Zones for the group.
            (string) --
            

    :type HealthCheckType: string
    :param HealthCheckType: The service to use for the health checks. The valid values are EC2 and ELB .

    :type HealthCheckGracePeriod: integer
    :param HealthCheckGracePeriod: The amount of time, in seconds, that Auto Scaling waits before checking the health status of an EC2 instance that has come into service. The default is 0.
            For more information, see Health Checks in the Auto Scaling User Guide .
            

    :type PlacementGroup: string
    :param PlacementGroup: The name of the placement group into which you'll launch your instances, if any. For more information, see Placement Groups in the Amazon Elastic Compute Cloud User Guide .

    :type VPCZoneIdentifier: string
    :param VPCZoneIdentifier: The ID of the subnet, if you are launching into a VPC. You can specify several subnets in a comma-separated list.
            When you specify VPCZoneIdentifier with AvailabilityZones , ensure that the subnets' Availability Zones match the values you specify for AvailabilityZones .
            For more information, see Launching Auto Scaling Instances in a VPC in the Auto Scaling User Guide .
            

    :type TerminationPolicies: list
    :param TerminationPolicies: A standalone termination policy or a list of termination policies used to select the instance to terminate. The policies are executed in the order that they are listed.
            For more information, see Controlling Which Instances Auto Scaling Terminates During Scale In in the Auto Scaling User Guide .
            (string) --
            

    :type NewInstancesProtectedFromScaleIn: boolean
    :param NewInstancesProtectedFromScaleIn: Indicates whether newly launched instances are protected from termination by Auto Scaling when scaling in.

    :return: response = client.update_auto_scaling_group(
        AutoScalingGroupName='my-auto-scaling-group',
        LaunchConfigurationName='new-launch-config',
    )
    
    print(response)
    
    
    :returns: 
    AutoScalingGroupName (string) -- [REQUIRED]
    The name of the Auto Scaling group.
    
    LaunchConfigurationName (string) -- The name of the launch configuration.
    MinSize (integer) -- The minimum size of the Auto Scaling group.
    MaxSize (integer) -- The maximum size of the Auto Scaling group.
    DesiredCapacity (integer) -- The number of EC2 instances that should be running in the Auto Scaling group. This number must be greater than or equal to the minimum size of the group and less than or equal to the maximum size of the group.
    DefaultCooldown (integer) -- The amount of time, in seconds, after a scaling activity completes before another scaling activity can start. The default is 300.
    For more information, see Auto Scaling Cooldowns in the Auto Scaling User Guide .
    
    AvailabilityZones (list) -- One or more Availability Zones for the group.
    
    (string) --
    
    
    HealthCheckType (string) -- The service to use for the health checks. The valid values are EC2 and ELB .
    HealthCheckGracePeriod (integer) -- The amount of time, in seconds, that Auto Scaling waits before checking the health status of an EC2 instance that has come into service. The default is 0.
    For more information, see Health Checks in the Auto Scaling User Guide .
    
    PlacementGroup (string) -- The name of the placement group into which you'll launch your instances, if any. For more information, see Placement Groups in the Amazon Elastic Compute Cloud User Guide .
    VPCZoneIdentifier (string) -- The ID of the subnet, if you are launching into a VPC. You can specify several subnets in a comma-separated list.
    When you specify VPCZoneIdentifier with AvailabilityZones , ensure that the subnets' Availability Zones match the values you specify for AvailabilityZones .
    For more information, see Launching Auto Scaling Instances in a VPC in the Auto Scaling User Guide .
    
    TerminationPolicies (list) -- A standalone termination policy or a list of termination policies used to select the instance to terminate. The policies are executed in the order that they are listed.
    For more information, see Controlling Which Instances Auto Scaling Terminates During Scale In in the Auto Scaling User Guide .
    
    (string) --
    
    
    NewInstancesProtectedFromScaleIn (boolean) -- Indicates whether newly launched instances are protected from termination by Auto Scaling when scaling in.
    
    """
    pass

