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

def add_instance_fleet(ClusterId=None, InstanceFleet=None):
    """
    Adds an instance fleet to a running cluster.
    See also: AWS API Documentation
    
    
    :example: response = client.add_instance_fleet(
        ClusterId='string',
        InstanceFleet={
            'Name': 'string',
            'InstanceFleetType': 'MASTER'|'CORE'|'TASK',
            'TargetOnDemandCapacity': 123,
            'TargetSpotCapacity': 123,
            'InstanceTypeConfigs': [
                {
                    'InstanceType': 'string',
                    'WeightedCapacity': 123,
                    'BidPrice': 'string',
                    'BidPriceAsPercentageOfOnDemandPrice': 123.0,
                    'EbsConfiguration': {
                        'EbsBlockDeviceConfigs': [
                            {
                                'VolumeSpecification': {
                                    'VolumeType': 'string',
                                    'Iops': 123,
                                    'SizeInGB': 123
                                },
                                'VolumesPerInstance': 123
                            },
                        ],
                        'EbsOptimized': True|False
                    },
                    'Configurations': [
                        {
                            'Classification': 'string',
                            'Configurations': {'... recursive ...'},
                            'Properties': {
                                'string': 'string'
                            }
                        },
                    ]
                },
            ],
            'LaunchSpecifications': {
                'SpotSpecification': {
                    'TimeoutDurationMinutes': 123,
                    'TimeoutAction': 'SWITCH_TO_ON_DEMAND'|'TERMINATE_CLUSTER',
                    'BlockDurationMinutes': 123
                }
            }
        }
    )
    
    
    :type ClusterId: string
    :param ClusterId: [REQUIRED]
            The unique identifier of the cluster.
            

    :type InstanceFleet: dict
    :param InstanceFleet: [REQUIRED]
            Specifies the configuration of the instance fleet.
            Name (string) --The friendly name of the instance fleet.
            InstanceFleetType (string) -- [REQUIRED]The node type that the instance fleet hosts. Valid values are MASTER,CORE,and TASK.
            TargetOnDemandCapacity (integer) --The target capacity of On-Demand units for the instance fleet, which determines how many On-Demand instances to provision. When the instance fleet launches, Amazon EMR tries to provision On-Demand instances as specified by InstanceTypeConfig . Each instance configuration has a specified WeightedCapacity . When an On-Demand instance is provisioned, the WeightedCapacity units count toward the target capacity. Amazon EMR provisions instances until the target capacity is totally fulfilled, even if this results in an overage. For example, if there are 2 units remaining to fulfill capacity, and Amazon EMR can only provision an instance with a WeightedCapacity of 5 units, the instance is provisioned, and the target capacity is exceeded by 3 units.
            Note
            If not specified or set to 0, only Spot instances are provisioned for the instance fleet using TargetSpotCapacity . At least one of TargetSpotCapacity and TargetOnDemandCapacity should be greater than 0. For a master instance fleet, only one of TargetSpotCapacity and TargetOnDemandCapacity can be specified, and its value must be 1.
            TargetSpotCapacity (integer) --The target capacity of Spot units for the instance fleet, which determines how many Spot instances to provision. When the instance fleet launches, Amazon EMR tries to provision Spot instances as specified by InstanceTypeConfig . Each instance configuration has a specified WeightedCapacity . When a Spot instance is provisioned, the WeightedCapacity units count toward the target capacity. Amazon EMR provisions instances until the target capacity is totally fulfilled, even if this results in an overage. For example, if there are 2 units remaining to fulfill capacity, and Amazon EMR can only provision an instance with a WeightedCapacity of 5 units, the instance is provisioned, and the target capacity is exceeded by 3 units.
            Note
            If not specified or set to 0, only On-Demand instances are provisioned for the instance fleet. At least one of TargetSpotCapacity and TargetOnDemandCapacity should be greater than 0. For a master instance fleet, only one of TargetSpotCapacity and TargetOnDemandCapacity can be specified, and its value must be 1.
            InstanceTypeConfigs (list) --The instance type configurations that define the EC2 instances in the instance fleet.
            (dict) --An instance type configuration for each instance type in an instance fleet, which determines the EC2 instances Amazon EMR attempts to provision to fulfill On-Demand and Spot target capacities. There can be a maximum of 5 instance type configurations in a fleet.
            Note
            The instance fleet configuration is available only in Amazon EMR versions 4.8.0 and later, excluding 5.0.x versions.
            InstanceType (string) -- [REQUIRED]An EC2 instance type, such as m3.xlarge .
            WeightedCapacity (integer) --The number of units that a provisioned instance of this type provides toward fulfilling the target capacities defined in InstanceFleetConfig . This value is 1 for a master instance fleet, and must be greater than 0 for core and task instance fleets.
            BidPrice (string) --The bid price for each EC2 Spot instance type as defined by InstanceType . Expressed in USD. If neither BidPrice nor BidPriceAsPercentageOfOnDemandPrice is provided, BidPriceAsPercentageOfOnDemandPrice defaults to 100%.
            BidPriceAsPercentageOfOnDemandPrice (float) --The bid price, as a percentage of On-Demand price, for each EC2 Spot instance as defined by InstanceType . Expressed as a number between 0 and 1000 (for example, 20 specifies 20%). If neither BidPrice nor BidPriceAsPercentageOfOnDemandPrice is provided, BidPriceAsPercentageOfOnDemandPrice defaults to 100%.
            EbsConfiguration (dict) --The configuration of Amazon Elastic Block Storage (EBS) attached to each instance as defined by InstanceType .
            EbsBlockDeviceConfigs (list) --An array of Amazon EBS volume specifications attached to a cluster instance.
            (dict) --Configuration of requested EBS block device associated with the instance group with count of volumes that will be associated to every instance.
            VolumeSpecification (dict) -- [REQUIRED]EBS volume specifications such as volume type, IOPS, and size (GiB) that will be requested for the EBS volume attached to an EC2 instance in the cluster.
            VolumeType (string) -- [REQUIRED]The volume type. Volume types supported are gp2, io1, standard.
            Iops (integer) --The number of I/O operations per second (IOPS) that the volume supports.
            SizeInGB (integer) -- [REQUIRED]The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the volume type is EBS-optimized, the minimum value is 10.
            VolumesPerInstance (integer) --Number of EBS volumes with a specific volume configuration that will be associated with every instance in the instance group
            
            EbsOptimized (boolean) --Indicates whether an Amazon EBS volume is EBS-optimized.
            Configurations (list) --A configuration classification that applies when provisioning cluster instances, which can include configurations for applications and software that run on the cluster.
            (dict) --
            Note
            Amazon EMR releases 4.x or later.
            An optional configuration specification to be used when provisioning cluster instances, which can include configurations for applications and software bundled with Amazon EMR. A configuration consists of a classification, properties, and optional nested configurations. A classification refers to an application-specific configuration file. Properties are the settings you want to change in that file. For more information, see Configuring Applications .
            Classification (string) --The classification within a configuration.
            Configurations (list) --A list of additional configurations to apply within a configuration object.
            Properties (dict) --A set of properties specified within a configuration classification.
            (string) --
            (string) --
            
            
            
            LaunchSpecifications (dict) --The launch specification for the instance fleet.
            SpotSpecification (dict) -- [REQUIRED]The launch specification for Spot instances in the fleet, which determines the defined duration and provisioning timeout behavior.
            TimeoutDurationMinutes (integer) -- [REQUIRED]The spot provisioning timeout period in minutes. If Spot instances are not provisioned within this time period, the TimeOutAction is taken. Minimum value is 5 and maximum value is 1440. The timeout applies only during initial provisioning, when the cluster is first created.
            TimeoutAction (string) -- [REQUIRED]The action to take when TargetSpotCapacity has not been fulfilled when the TimeoutDurationMinutes has expired. Spot instances are not uprovisioned within the Spot provisioining timeout. Valid values are TERMINATE_CLUSTER and SWITCH_TO_ON_DEMAND to fulfill the remaining capacity.
            BlockDurationMinutes (integer) --The defined duration for Spot instances (also known as Spot blocks) in minutes. When specified, the Spot instance does not terminate before the defined duration expires, and defined duration pricing for Spot instances applies. Valid values are 60, 120, 180, 240, 300, or 360. The duration period starts as soon as a Spot instance receives its instance ID. At the end of the duration, Amazon EC2 marks the Spot instance for termination and provides a Spot instance termination notice, which gives the instance a two-minute warning before it terminates.
            
            

    :rtype: dict
    :return: {
        'ClusterId': 'string',
        'InstanceFleetId': 'string'
    }
    
    
    """
    pass

def add_instance_groups(InstanceGroups=None, JobFlowId=None):
    """
    Adds one or more instance groups to a running cluster.
    See also: AWS API Documentation
    
    
    :example: response = client.add_instance_groups(
        InstanceGroups=[
            {
                'Name': 'string',
                'Market': 'ON_DEMAND'|'SPOT',
                'InstanceRole': 'MASTER'|'CORE'|'TASK',
                'BidPrice': 'string',
                'InstanceType': 'string',
                'InstanceCount': 123,
                'Configurations': [
                    {
                        'Classification': 'string',
                        'Configurations': {'... recursive ...'},
                        'Properties': {
                            'string': 'string'
                        }
                    },
                ],
                'EbsConfiguration': {
                    'EbsBlockDeviceConfigs': [
                        {
                            'VolumeSpecification': {
                                'VolumeType': 'string',
                                'Iops': 123,
                                'SizeInGB': 123
                            },
                            'VolumesPerInstance': 123
                        },
                    ],
                    'EbsOptimized': True|False
                },
                'AutoScalingPolicy': {
                    'Constraints': {
                        'MinCapacity': 123,
                        'MaxCapacity': 123
                    },
                    'Rules': [
                        {
                            'Name': 'string',
                            'Description': 'string',
                            'Action': {
                                'Market': 'ON_DEMAND'|'SPOT',
                                'SimpleScalingPolicyConfiguration': {
                                    'AdjustmentType': 'CHANGE_IN_CAPACITY'|'PERCENT_CHANGE_IN_CAPACITY'|'EXACT_CAPACITY',
                                    'ScalingAdjustment': 123,
                                    'CoolDown': 123
                                }
                            },
                            'Trigger': {
                                'CloudWatchAlarmDefinition': {
                                    'ComparisonOperator': 'GREATER_THAN_OR_EQUAL'|'GREATER_THAN'|'LESS_THAN'|'LESS_THAN_OR_EQUAL',
                                    'EvaluationPeriods': 123,
                                    'MetricName': 'string',
                                    'Namespace': 'string',
                                    'Period': 123,
                                    'Statistic': 'SAMPLE_COUNT'|'AVERAGE'|'SUM'|'MINIMUM'|'MAXIMUM',
                                    'Threshold': 123.0,
                                    'Unit': 'NONE'|'SECONDS'|'MICRO_SECONDS'|'MILLI_SECONDS'|'BYTES'|'KILO_BYTES'|'MEGA_BYTES'|'GIGA_BYTES'|'TERA_BYTES'|'BITS'|'KILO_BITS'|'MEGA_BITS'|'GIGA_BITS'|'TERA_BITS'|'PERCENT'|'COUNT'|'BYTES_PER_SECOND'|'KILO_BYTES_PER_SECOND'|'MEGA_BYTES_PER_SECOND'|'GIGA_BYTES_PER_SECOND'|'TERA_BYTES_PER_SECOND'|'BITS_PER_SECOND'|'KILO_BITS_PER_SECOND'|'MEGA_BITS_PER_SECOND'|'GIGA_BITS_PER_SECOND'|'TERA_BITS_PER_SECOND'|'COUNT_PER_SECOND',
                                    'Dimensions': [
                                        {
                                            'Key': 'string',
                                            'Value': 'string'
                                        },
                                    ]
                                }
                            }
                        },
                    ]
                }
            },
        ],
        JobFlowId='string'
    )
    
    
    :type InstanceGroups: list
    :param InstanceGroups: [REQUIRED]
            Instance groups to add.
            (dict) --Configuration defining a new instance group.
            Name (string) --Friendly name given to the instance group.
            Market (string) --Market type of the EC2 instances used to create a cluster node.
            InstanceRole (string) -- [REQUIRED]The role of the instance group in the cluster.
            BidPrice (string) --Bid price for each EC2 instance in the instance group when launching nodes as Spot Instances, expressed in USD.
            InstanceType (string) -- [REQUIRED]The EC2 instance type for all instances in the instance group.
            InstanceCount (integer) -- [REQUIRED]Target number of instances for the instance group.
            Configurations (list) --
            Note
            Amazon EMR releases 4.x or later.
            The list of configurations supplied for an EMR cluster instance group. You can specify a separate configuration for each instance group (master, core, and task).
            (dict) --
            Note
            Amazon EMR releases 4.x or later.
            An optional configuration specification to be used when provisioning cluster instances, which can include configurations for applications and software bundled with Amazon EMR. A configuration consists of a classification, properties, and optional nested configurations. A classification refers to an application-specific configuration file. Properties are the settings you want to change in that file. For more information, see Configuring Applications .
            Classification (string) --The classification within a configuration.
            Configurations (list) --A list of additional configurations to apply within a configuration object.
            Properties (dict) --A set of properties specified within a configuration classification.
            (string) --
            (string) --
            
            
            EbsConfiguration (dict) --EBS configurations that will be attached to each EC2 instance in the instance group.
            EbsBlockDeviceConfigs (list) --An array of Amazon EBS volume specifications attached to a cluster instance.
            (dict) --Configuration of requested EBS block device associated with the instance group with count of volumes that will be associated to every instance.
            VolumeSpecification (dict) -- [REQUIRED]EBS volume specifications such as volume type, IOPS, and size (GiB) that will be requested for the EBS volume attached to an EC2 instance in the cluster.
            VolumeType (string) -- [REQUIRED]The volume type. Volume types supported are gp2, io1, standard.
            Iops (integer) --The number of I/O operations per second (IOPS) that the volume supports.
            SizeInGB (integer) -- [REQUIRED]The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the volume type is EBS-optimized, the minimum value is 10.
            VolumesPerInstance (integer) --Number of EBS volumes with a specific volume configuration that will be associated with every instance in the instance group
            
            EbsOptimized (boolean) --Indicates whether an Amazon EBS volume is EBS-optimized.
            AutoScalingPolicy (dict) --An automatic scaling policy for a core instance group or task instance group in an Amazon EMR cluster. The automatic scaling policy defines how an instance group dynamically adds and terminates EC2 instances in response to the value of a CloudWatch metric. See PutAutoScalingPolicy .
            Constraints (dict) -- [REQUIRED]The upper and lower EC2 instance limits for an automatic scaling policy. Automatic scaling activity will not cause an instance group to grow above or below these limits.
            MinCapacity (integer) -- [REQUIRED]The lower boundary of EC2 instances in an instance group below which scaling activities are not allowed to shrink. Scale-in activities will not terminate instances below this boundary.
            MaxCapacity (integer) -- [REQUIRED]The upper boundary of EC2 instances in an instance group beyond which scaling activities are not allowed to grow. Scale-out activities will not add instances beyond this boundary.
            Rules (list) -- [REQUIRED]The scale-in and scale-out rules that comprise the automatic scaling policy.
            (dict) --A scale-in or scale-out rule that defines scaling activity, including the CloudWatch metric alarm that triggers activity, how EC2 instances are added or removed, and the periodicity of adjustments. The automatic scaling policy for an instance group can comprise one or more automatic scaling rules.
            Name (string) -- [REQUIRED]The name used to identify an automatic scaling rule. Rule names must be unique within a scaling policy.
            Description (string) --A friendly, more verbose description of the automatic scaling rule.
            Action (dict) -- [REQUIRED]The conditions that trigger an automatic scaling activity.
            Market (string) --Not available for instance groups. Instance groups use the market type specified for the group.
            SimpleScalingPolicyConfiguration (dict) -- [REQUIRED]The type of adjustment the automatic scaling activity makes when triggered, and the periodicity of the adjustment.
            AdjustmentType (string) --The way in which EC2 instances are added (if ScalingAdjustment is a positive number) or terminated (if ScalingAdjustment is a negative number) each time the scaling activity is triggered. CHANGE_IN_CAPACITY is the default. CHANGE_IN_CAPACITY indicates that the EC2 instance count increments or decrements by ScalingAdjustment , which should be expressed as an integer. PERCENT_CHANGE_IN_CAPACITY indicates the instance count increments or decrements by the percentage specified by ScalingAdjustment , which should be expressed as a decimal. For example, 0.20 indicates an increase in 20% increments of cluster capacity. EXACT_CAPACITY indicates the scaling activity results in an instance group with the number of EC2 instances specified by ScalingAdjustment , which should be expressed as a positive integer.
            ScalingAdjustment (integer) -- [REQUIRED]The amount by which to scale in or scale out, based on the specified AdjustmentType . A positive value adds to the instance group's EC2 instance count while a negative number removes instances. If AdjustmentType is set to EXACT_CAPACITY , the number should only be a positive integer. If AdjustmentType is set to PERCENT_CHANGE_IN_CAPACITY , the value should express the percentage as a decimal. For example, -0.20 indicates a decrease in 20% increments of cluster capacity.
            CoolDown (integer) --The amount of time, in seconds, after a scaling activity completes before any further trigger-related scaling activities can start. The default value is 0.
            
            Trigger (dict) -- [REQUIRED]The CloudWatch alarm definition that determines when automatic scaling activity is triggered.
            CloudWatchAlarmDefinition (dict) -- [REQUIRED]The definition of a CloudWatch metric alarm. When the defined alarm conditions are met along with other trigger parameters, scaling activity begins.
            ComparisonOperator (string) -- [REQUIRED]Determines how the metric specified by MetricName is compared to the value specified by Threshold .
            EvaluationPeriods (integer) --The number of periods, expressed in seconds using Period , during which the alarm condition must exist before the alarm triggers automatic scaling activity. The default value is 1 .
            MetricName (string) -- [REQUIRED]The name of the CloudWatch metric that is watched to determine an alarm condition.
            Namespace (string) --The namespace for the CloudWatch metric. The default is AWS/ElasticMapReduce .
            Period (integer) -- [REQUIRED]The period, in seconds, over which the statistic is applied. EMR CloudWatch metrics are emitted every five minutes (300 seconds), so if an EMR CloudWatch metric is specified, specify 300 .
            Statistic (string) --The statistic to apply to the metric associated with the alarm. The default is AVERAGE .
            Threshold (float) -- [REQUIRED]The value against which the specified statistic is compared.
            Unit (string) --The unit of measure associated with the CloudWatch metric being watched. The value specified for Unit must correspond to the units specified in the CloudWatch metric.
            Dimensions (list) --A CloudWatch metric dimension.
            (dict) --A CloudWatch dimension, which is specified using a Key (known as a Name in CloudWatch), Value pair. By default, Amazon EMR uses one dimension whose Key is JobFlowID and Value is a variable representing the cluster ID, which is ${emr.clusterId} . This enables the rule to bootstrap when the cluster ID becomes available.
            Key (string) --The dimension name.
            Value (string) --The dimension value.
            
            
            
            
            

    :type JobFlowId: string
    :param JobFlowId: [REQUIRED]
            Job flow in which to add the instance groups.
            

    :rtype: dict
    :return: {
        'JobFlowId': 'string',
        'InstanceGroupIds': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def add_job_flow_steps(JobFlowId=None, Steps=None):
    """
    AddJobFlowSteps adds new steps to a running cluster. A maximum of 256 steps are allowed in each job flow.
    If your cluster is long-running (such as a Hive data warehouse) or complex, you may require more than 256 steps to process your data. You can bypass the 256-step limitation in various ways, including using SSH to connect to the master node and submitting queries directly to the software running on the master node, such as Hive and Hadoop. For more information on how to do this, see Add More than 256 Steps to a Cluster in the Amazon EMR Management Guide .
    A step specifies the location of a JAR file stored either on the master node of the cluster or in Amazon S3. Each step is performed by the main function of the main class of the JAR file. The main class can be specified either in the manifest of the JAR or by using the MainFunction parameter of the step.
    Amazon EMR executes each step in the order listed. For a step to be considered complete, the main function must exit with a zero exit code and all Hadoop jobs started while the step was running must have completed and run successfully.
    You can only add steps to a cluster that is in one of the following states: STARTING, BOOTSTRAPPING, RUNNING, or WAITING.
    See also: AWS API Documentation
    
    
    :example: response = client.add_job_flow_steps(
        JobFlowId='string',
        Steps=[
            {
                'Name': 'string',
                'ActionOnFailure': 'TERMINATE_JOB_FLOW'|'TERMINATE_CLUSTER'|'CANCEL_AND_WAIT'|'CONTINUE',
                'HadoopJarStep': {
                    'Properties': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        },
                    ],
                    'Jar': 'string',
                    'MainClass': 'string',
                    'Args': [
                        'string',
                    ]
                }
            },
        ]
    )
    
    
    :type JobFlowId: string
    :param JobFlowId: [REQUIRED]
            A string that uniquely identifies the job flow. This identifier is returned by RunJobFlow and can also be obtained from ListClusters .
            

    :type Steps: list
    :param Steps: [REQUIRED]
            A list of StepConfig to be executed by the job flow.
            (dict) --Specification of a cluster (job flow) step.
            Name (string) -- [REQUIRED]The name of the step.
            ActionOnFailure (string) --The action to take if the step fails.
            HadoopJarStep (dict) -- [REQUIRED]The JAR file used for the step.
            Properties (list) --A list of Java properties that are set when the step runs. You can use these properties to pass key value pairs to your main function.
            (dict) --A key value pair.
            Key (string) --The unique identifier of a key value pair.
            Value (string) --The value part of the identified key.
            
            Jar (string) -- [REQUIRED]A path to a JAR file run during the step.
            MainClass (string) --The name of the main class in the specified Java file. If not specified, the JAR file should specify a Main-Class in its manifest file.
            Args (list) --A list of command line arguments passed to the JAR file's main function when executed.
            (string) --
            
            

    :rtype: dict
    :return: {
        'StepIds': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def add_tags(ResourceId=None, Tags=None):
    """
    Adds tags to an Amazon EMR resource. Tags make it easier to associate clusters in various ways, such as grouping clusters to track your Amazon EMR resource allocation costs. For more information, see Tagging Amazon EMR Resources .
    See also: AWS API Documentation
    
    
    :example: response = client.add_tags(
        ResourceId='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ResourceId: string
    :param ResourceId: [REQUIRED]
            The Amazon EMR resource identifier to which tags will be added. This value must be a cluster identifier.
            

    :type Tags: list
    :param Tags: [REQUIRED]
            A list of tags to associate with a cluster and propagate to EC2 instances. Tags are user-defined key/value pairs that consist of a required key string with a maximum of 128 characters, and an optional value string with a maximum of 256 characters.
            (dict) --A key/value pair containing user-defined metadata that you can associate with an Amazon EMR resource. Tags make it easier to associate clusters in various ways, such as grouping clusters to track your Amazon EMR resource allocation costs. For more information, see Tagging Amazon EMR Resources .
            Key (string) --A user-defined key, which is the minimum required information for a valid tag. For more information, see Tagging Amazon EMR Resources .
            Value (string) --A user-defined value, which is optional in a tag. For more information, see Tagging Amazon EMR Resources .
            
            

    :rtype: dict
    :return: {}
    
    
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

def cancel_steps(ClusterId=None, StepIds=None):
    """
    Cancels a pending step or steps in a running cluster. Available only in Amazon EMR versions 4.8.0 and later, excluding version 5.0.0. A maximum of 256 steps are allowed in each CancelSteps request. CancelSteps is idempotent but asynchronous; it does not guarantee a step will be canceled, even if the request is successfully submitted. You can only cancel steps that are in a PENDING state.
    See also: AWS API Documentation
    
    
    :example: response = client.cancel_steps(
        ClusterId='string',
        StepIds=[
            'string',
        ]
    )
    
    
    :type ClusterId: string
    :param ClusterId: The ClusterID for which specified steps will be canceled. Use RunJobFlow and ListClusters to get ClusterIDs.

    :type StepIds: list
    :param StepIds: The list of StepIDs to cancel. Use ListSteps to get steps and their states for the specified cluster.
            (string) --
            

    :rtype: dict
    :return: {
        'CancelStepsInfoList': [
            {
                'StepId': 'string',
                'Status': 'SUBMITTED'|'FAILED',
                'Reason': 'string'
            },
        ]
    }
    
    
    """
    pass

def create_security_configuration(Name=None, SecurityConfiguration=None):
    """
    Creates a security configuration, which is stored in the service and can be specified when a cluster is created.
    See also: AWS API Documentation
    
    
    :example: response = client.create_security_configuration(
        Name='string',
        SecurityConfiguration='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the security configuration.
            

    :type SecurityConfiguration: string
    :param SecurityConfiguration: [REQUIRED]
            The security configuration details in JSON format.
            

    :rtype: dict
    :return: {
        'Name': 'string',
        'CreationDateTime': datetime(2015, 1, 1)
    }
    
    
    """
    pass

def delete_security_configuration(Name=None):
    """
    Deletes a security configuration.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_security_configuration(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the security configuration.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def describe_cluster(ClusterId=None):
    """
    Provides cluster-level details including status, hardware and software configuration, VPC settings, and so on. For information about the cluster steps, see  ListSteps .
    See also: AWS API Documentation
    
    
    :example: response = client.describe_cluster(
        ClusterId='string'
    )
    
    
    :type ClusterId: string
    :param ClusterId: [REQUIRED]
            The identifier of the cluster to describe.
            

    :rtype: dict
    :return: {
        'Cluster': {
            'Id': 'string',
            'Name': 'string',
            'Status': {
                'State': 'STARTING'|'BOOTSTRAPPING'|'RUNNING'|'WAITING'|'TERMINATING'|'TERMINATED'|'TERMINATED_WITH_ERRORS',
                'StateChangeReason': {
                    'Code': 'INTERNAL_ERROR'|'VALIDATION_ERROR'|'INSTANCE_FAILURE'|'BOOTSTRAP_FAILURE'|'USER_REQUEST'|'STEP_FAILURE'|'ALL_STEPS_COMPLETED',
                    'Message': 'string'
                },
                'Timeline': {
                    'CreationDateTime': datetime(2015, 1, 1),
                    'ReadyDateTime': datetime(2015, 1, 1),
                    'EndDateTime': datetime(2015, 1, 1)
                }
            },
            'Ec2InstanceAttributes': {
                'Ec2KeyName': 'string',
                'Ec2SubnetId': 'string',
                'RequestedEc2SubnetIds': [
                    'string',
                ],
                'Ec2AvailabilityZone': 'string',
                'RequestedEc2AvailabilityZones': [
                    'string',
                ],
                'IamInstanceProfile': 'string',
                'EmrManagedMasterSecurityGroup': 'string',
                'EmrManagedSlaveSecurityGroup': 'string',
                'ServiceAccessSecurityGroup': 'string',
                'AdditionalMasterSecurityGroups': [
                    'string',
                ],
                'AdditionalSlaveSecurityGroups': [
                    'string',
                ]
            },
            'InstanceCollectionType': 'INSTANCE_FLEET'|'INSTANCE_GROUP',
            'LogUri': 'string',
            'RequestedAmiVersion': 'string',
            'RunningAmiVersion': 'string',
            'ReleaseLabel': 'string',
            'AutoTerminate': True|False,
            'TerminationProtected': True|False,
            'VisibleToAllUsers': True|False,
            'Applications': [
                {
                    'Name': 'string',
                    'Version': 'string',
                    'Args': [
                        'string',
                    ],
                    'AdditionalInfo': {
                        'string': 'string'
                    }
                },
            ],
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'ServiceRole': 'string',
            'NormalizedInstanceHours': 123,
            'MasterPublicDnsName': 'string',
            'Configurations': [
                {
                    'Classification': 'string',
                    'Configurations': {'... recursive ...'},
                    'Properties': {
                        'string': 'string'
                    }
                },
            ],
            'SecurityConfiguration': 'string',
            'AutoScalingRole': 'string',
            'ScaleDownBehavior': 'TERMINATE_AT_INSTANCE_HOUR'|'TERMINATE_AT_TASK_COMPLETION'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_job_flows(CreatedAfter=None, CreatedBefore=None, JobFlowIds=None, JobFlowStates=None):
    """
    This API is deprecated and will eventually be removed. We recommend you use  ListClusters ,  DescribeCluster ,  ListSteps ,  ListInstanceGroups and  ListBootstrapActions instead.
    DescribeJobFlows returns a list of job flows that match all of the supplied parameters. The parameters can include a list of job flow IDs, job flow states, and restrictions on job flow creation date and time.
    Regardless of supplied parameters, only job flows created within the last two months are returned.
    If no parameters are supplied, then job flows matching either of the following criteria are returned:
    Amazon EMR can return a maximum of 512 job flow descriptions.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_job_flows(
        CreatedAfter=datetime(2015, 1, 1),
        CreatedBefore=datetime(2015, 1, 1),
        JobFlowIds=[
            'string',
        ],
        JobFlowStates=[
            'STARTING'|'BOOTSTRAPPING'|'RUNNING'|'WAITING'|'SHUTTING_DOWN'|'TERMINATED'|'COMPLETED'|'FAILED',
        ]
    )
    
    
    :type CreatedAfter: datetime
    :param CreatedAfter: Return only job flows created after this date and time.

    :type CreatedBefore: datetime
    :param CreatedBefore: Return only job flows created before this date and time.

    :type JobFlowIds: list
    :param JobFlowIds: Return only job flows whose job flow ID is contained in this list.
            (string) --
            

    :type JobFlowStates: list
    :param JobFlowStates: Return only job flows whose state is contained in this list.
            (string) --The type of instance.
            

    :rtype: dict
    :return: {
        'JobFlows': [
            {
                'JobFlowId': 'string',
                'Name': 'string',
                'LogUri': 'string',
                'AmiVersion': 'string',
                'ExecutionStatusDetail': {
                    'State': 'STARTING'|'BOOTSTRAPPING'|'RUNNING'|'WAITING'|'SHUTTING_DOWN'|'TERMINATED'|'COMPLETED'|'FAILED',
                    'CreationDateTime': datetime(2015, 1, 1),
                    'StartDateTime': datetime(2015, 1, 1),
                    'ReadyDateTime': datetime(2015, 1, 1),
                    'EndDateTime': datetime(2015, 1, 1),
                    'LastStateChangeReason': 'string'
                },
                'Instances': {
                    'MasterInstanceType': 'string',
                    'MasterPublicDnsName': 'string',
                    'MasterInstanceId': 'string',
                    'SlaveInstanceType': 'string',
                    'InstanceCount': 123,
                    'InstanceGroups': [
                        {
                            'InstanceGroupId': 'string',
                            'Name': 'string',
                            'Market': 'ON_DEMAND'|'SPOT',
                            'InstanceRole': 'MASTER'|'CORE'|'TASK',
                            'BidPrice': 'string',
                            'InstanceType': 'string',
                            'InstanceRequestCount': 123,
                            'InstanceRunningCount': 123,
                            'State': 'PROVISIONING'|'BOOTSTRAPPING'|'RUNNING'|'RESIZING'|'SUSPENDED'|'TERMINATING'|'TERMINATED'|'ARRESTED'|'SHUTTING_DOWN'|'ENDED',
                            'LastStateChangeReason': 'string',
                            'CreationDateTime': datetime(2015, 1, 1),
                            'StartDateTime': datetime(2015, 1, 1),
                            'ReadyDateTime': datetime(2015, 1, 1),
                            'EndDateTime': datetime(2015, 1, 1)
                        },
                    ],
                    'NormalizedInstanceHours': 123,
                    'Ec2KeyName': 'string',
                    'Ec2SubnetId': 'string',
                    'Placement': {
                        'AvailabilityZone': 'string',
                        'AvailabilityZones': [
                            'string',
                        ]
                    },
                    'KeepJobFlowAliveWhenNoSteps': True|False,
                    'TerminationProtected': True|False,
                    'HadoopVersion': 'string'
                },
                'Steps': [
                    {
                        'StepConfig': {
                            'Name': 'string',
                            'ActionOnFailure': 'TERMINATE_JOB_FLOW'|'TERMINATE_CLUSTER'|'CANCEL_AND_WAIT'|'CONTINUE',
                            'HadoopJarStep': {
                                'Properties': [
                                    {
                                        'Key': 'string',
                                        'Value': 'string'
                                    },
                                ],
                                'Jar': 'string',
                                'MainClass': 'string',
                                'Args': [
                                    'string',
                                ]
                            }
                        },
                        'ExecutionStatusDetail': {
                            'State': 'PENDING'|'RUNNING'|'CONTINUE'|'COMPLETED'|'CANCELLED'|'FAILED'|'INTERRUPTED',
                            'CreationDateTime': datetime(2015, 1, 1),
                            'StartDateTime': datetime(2015, 1, 1),
                            'EndDateTime': datetime(2015, 1, 1),
                            'LastStateChangeReason': 'string'
                        }
                    },
                ],
                'BootstrapActions': [
                    {
                        'BootstrapActionConfig': {
                            'Name': 'string',
                            'ScriptBootstrapAction': {
                                'Path': 'string',
                                'Args': [
                                    'string',
                                ]
                            }
                        }
                    },
                ],
                'SupportedProducts': [
                    'string',
                ],
                'VisibleToAllUsers': True|False,
                'JobFlowRole': 'string',
                'ServiceRole': 'string',
                'AutoScalingRole': 'string',
                'ScaleDownBehavior': 'TERMINATE_AT_INSTANCE_HOUR'|'TERMINATE_AT_TASK_COMPLETION'
            },
        ]
    }
    
    
    :returns: 
    CreatedAfter (datetime) -- Return only job flows created after this date and time.
    CreatedBefore (datetime) -- Return only job flows created before this date and time.
    JobFlowIds (list) -- Return only job flows whose job flow ID is contained in this list.
    
    (string) --
    
    
    JobFlowStates (list) -- Return only job flows whose state is contained in this list.
    
    (string) --The type of instance.
    
    
    
    
    """
    pass

def describe_security_configuration(Name=None):
    """
    Provides the details of a security configuration by returning the configuration JSON.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_security_configuration(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the security configuration.
            

    :rtype: dict
    :return: {
        'Name': 'string',
        'SecurityConfiguration': 'string',
        'CreationDateTime': datetime(2015, 1, 1)
    }
    
    
    """
    pass

def describe_step(ClusterId=None, StepId=None):
    """
    Provides more detail about the cluster step.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_step(
        ClusterId='string',
        StepId='string'
    )
    
    
    :type ClusterId: string
    :param ClusterId: [REQUIRED]
            The identifier of the cluster with steps to describe.
            

    :type StepId: string
    :param StepId: [REQUIRED]
            The identifier of the step to describe.
            

    :rtype: dict
    :return: {
        'Step': {
            'Id': 'string',
            'Name': 'string',
            'Config': {
                'Jar': 'string',
                'Properties': {
                    'string': 'string'
                },
                'MainClass': 'string',
                'Args': [
                    'string',
                ]
            },
            'ActionOnFailure': 'TERMINATE_JOB_FLOW'|'TERMINATE_CLUSTER'|'CANCEL_AND_WAIT'|'CONTINUE',
            'Status': {
                'State': 'PENDING'|'CANCEL_PENDING'|'RUNNING'|'COMPLETED'|'CANCELLED'|'FAILED'|'INTERRUPTED',
                'StateChangeReason': {
                    'Code': 'NONE',
                    'Message': 'string'
                },
                'FailureDetails': {
                    'Reason': 'string',
                    'Message': 'string',
                    'LogFile': 'string'
                },
                'Timeline': {
                    'CreationDateTime': datetime(2015, 1, 1),
                    'StartDateTime': datetime(2015, 1, 1),
                    'EndDateTime': datetime(2015, 1, 1)
                }
            }
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
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

def list_bootstrap_actions(ClusterId=None, Marker=None):
    """
    Provides information about the bootstrap actions associated with a cluster.
    See also: AWS API Documentation
    
    
    :example: response = client.list_bootstrap_actions(
        ClusterId='string',
        Marker='string'
    )
    
    
    :type ClusterId: string
    :param ClusterId: [REQUIRED]
            The cluster identifier for the bootstrap actions to list.
            

    :type Marker: string
    :param Marker: The pagination token that indicates the next set of results to retrieve.

    :rtype: dict
    :return: {
        'BootstrapActions': [
            {
                'Name': 'string',
                'ScriptPath': 'string',
                'Args': [
                    'string',
                ]
            },
        ],
        'Marker': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_clusters(CreatedAfter=None, CreatedBefore=None, ClusterStates=None, Marker=None):
    """
    Provides the status of all clusters visible to this AWS account. Allows you to filter the list of clusters based on certain criteria; for example, filtering by cluster creation date and time or by status. This call returns a maximum of 50 clusters per call, but returns a marker to track the paging of the cluster list across multiple ListClusters calls.
    See also: AWS API Documentation
    
    
    :example: response = client.list_clusters(
        CreatedAfter=datetime(2015, 1, 1),
        CreatedBefore=datetime(2015, 1, 1),
        ClusterStates=[
            'STARTING'|'BOOTSTRAPPING'|'RUNNING'|'WAITING'|'TERMINATING'|'TERMINATED'|'TERMINATED_WITH_ERRORS',
        ],
        Marker='string'
    )
    
    
    :type CreatedAfter: datetime
    :param CreatedAfter: The creation date and time beginning value filter for listing clusters.

    :type CreatedBefore: datetime
    :param CreatedBefore: The creation date and time end value filter for listing clusters.

    :type ClusterStates: list
    :param ClusterStates: The cluster state filters to apply when listing clusters.
            (string) --
            

    :type Marker: string
    :param Marker: The pagination token that indicates the next set of results to retrieve.

    :rtype: dict
    :return: {
        'Clusters': [
            {
                'Id': 'string',
                'Name': 'string',
                'Status': {
                    'State': 'STARTING'|'BOOTSTRAPPING'|'RUNNING'|'WAITING'|'TERMINATING'|'TERMINATED'|'TERMINATED_WITH_ERRORS',
                    'StateChangeReason': {
                        'Code': 'INTERNAL_ERROR'|'VALIDATION_ERROR'|'INSTANCE_FAILURE'|'BOOTSTRAP_FAILURE'|'USER_REQUEST'|'STEP_FAILURE'|'ALL_STEPS_COMPLETED',
                        'Message': 'string'
                    },
                    'Timeline': {
                        'CreationDateTime': datetime(2015, 1, 1),
                        'ReadyDateTime': datetime(2015, 1, 1),
                        'EndDateTime': datetime(2015, 1, 1)
                    }
                },
                'NormalizedInstanceHours': 123
            },
        ],
        'Marker': 'string'
    }
    
    
    """
    pass

def list_instance_fleets(ClusterId=None, Marker=None):
    """
    Lists all available details about the instance fleets in a cluster.
    See also: AWS API Documentation
    
    
    :example: response = client.list_instance_fleets(
        ClusterId='string',
        Marker='string'
    )
    
    
    :type ClusterId: string
    :param ClusterId: [REQUIRED]
            The unique identifier of the cluster.
            

    :type Marker: string
    :param Marker: The pagination token that indicates the next set of results to retrieve.

    :rtype: dict
    :return: {
        'InstanceFleets': [
            {
                'Id': 'string',
                'Name': 'string',
                'Status': {
                    'State': 'PROVISIONING'|'BOOTSTRAPPING'|'RUNNING'|'RESIZING'|'SUSPENDED'|'TERMINATING'|'TERMINATED',
                    'StateChangeReason': {
                        'Code': 'INTERNAL_ERROR'|'VALIDATION_ERROR'|'INSTANCE_FAILURE'|'CLUSTER_TERMINATED',
                        'Message': 'string'
                    },
                    'Timeline': {
                        'CreationDateTime': datetime(2015, 1, 1),
                        'ReadyDateTime': datetime(2015, 1, 1),
                        'EndDateTime': datetime(2015, 1, 1)
                    }
                },
                'InstanceFleetType': 'MASTER'|'CORE'|'TASK',
                'TargetOnDemandCapacity': 123,
                'TargetSpotCapacity': 123,
                'ProvisionedOnDemandCapacity': 123,
                'ProvisionedSpotCapacity': 123,
                'InstanceTypeSpecifications': [
                    {
                        'InstanceType': 'string',
                        'WeightedCapacity': 123,
                        'BidPrice': 'string',
                        'BidPriceAsPercentageOfOnDemandPrice': 123.0,
                        'Configurations': [
                            {
                                'Classification': 'string',
                                'Configurations': {'... recursive ...'},
                                'Properties': {
                                    'string': 'string'
                                }
                            },
                        ],
                        'EbsBlockDevices': [
                            {
                                'VolumeSpecification': {
                                    'VolumeType': 'string',
                                    'Iops': 123,
                                    'SizeInGB': 123
                                },
                                'Device': 'string'
                            },
                        ],
                        'EbsOptimized': True|False
                    },
                ],
                'LaunchSpecifications': {
                    'SpotSpecification': {
                        'TimeoutDurationMinutes': 123,
                        'TimeoutAction': 'SWITCH_TO_ON_DEMAND'|'TERMINATE_CLUSTER',
                        'BlockDurationMinutes': 123
                    }
                }
            },
        ],
        'Marker': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def list_instance_groups(ClusterId=None, Marker=None):
    """
    Provides all available details about the instance groups in a cluster.
    See also: AWS API Documentation
    
    
    :example: response = client.list_instance_groups(
        ClusterId='string',
        Marker='string'
    )
    
    
    :type ClusterId: string
    :param ClusterId: [REQUIRED]
            The identifier of the cluster for which to list the instance groups.
            

    :type Marker: string
    :param Marker: The pagination token that indicates the next set of results to retrieve.

    :rtype: dict
    :return: {
        'InstanceGroups': [
            {
                'Id': 'string',
                'Name': 'string',
                'Market': 'ON_DEMAND'|'SPOT',
                'InstanceGroupType': 'MASTER'|'CORE'|'TASK',
                'BidPrice': 'string',
                'InstanceType': 'string',
                'RequestedInstanceCount': 123,
                'RunningInstanceCount': 123,
                'Status': {
                    'State': 'PROVISIONING'|'BOOTSTRAPPING'|'RUNNING'|'RESIZING'|'SUSPENDED'|'TERMINATING'|'TERMINATED'|'ARRESTED'|'SHUTTING_DOWN'|'ENDED',
                    'StateChangeReason': {
                        'Code': 'INTERNAL_ERROR'|'VALIDATION_ERROR'|'INSTANCE_FAILURE'|'CLUSTER_TERMINATED',
                        'Message': 'string'
                    },
                    'Timeline': {
                        'CreationDateTime': datetime(2015, 1, 1),
                        'ReadyDateTime': datetime(2015, 1, 1),
                        'EndDateTime': datetime(2015, 1, 1)
                    }
                },
                'Configurations': [
                    {
                        'Classification': 'string',
                        'Configurations': {'... recursive ...'},
                        'Properties': {
                            'string': 'string'
                        }
                    },
                ],
                'EbsBlockDevices': [
                    {
                        'VolumeSpecification': {
                            'VolumeType': 'string',
                            'Iops': 123,
                            'SizeInGB': 123
                        },
                        'Device': 'string'
                    },
                ],
                'EbsOptimized': True|False,
                'ShrinkPolicy': {
                    'DecommissionTimeout': 123,
                    'InstanceResizePolicy': {
                        'InstancesToTerminate': [
                            'string',
                        ],
                        'InstancesToProtect': [
                            'string',
                        ],
                        'InstanceTerminationTimeout': 123
                    }
                },
                'AutoScalingPolicy': {
                    'Status': {
                        'State': 'PENDING'|'ATTACHING'|'ATTACHED'|'DETACHING'|'DETACHED'|'FAILED',
                        'StateChangeReason': {
                            'Code': 'USER_REQUEST'|'PROVISION_FAILURE'|'CLEANUP_FAILURE',
                            'Message': 'string'
                        }
                    },
                    'Constraints': {
                        'MinCapacity': 123,
                        'MaxCapacity': 123
                    },
                    'Rules': [
                        {
                            'Name': 'string',
                            'Description': 'string',
                            'Action': {
                                'Market': 'ON_DEMAND'|'SPOT',
                                'SimpleScalingPolicyConfiguration': {
                                    'AdjustmentType': 'CHANGE_IN_CAPACITY'|'PERCENT_CHANGE_IN_CAPACITY'|'EXACT_CAPACITY',
                                    'ScalingAdjustment': 123,
                                    'CoolDown': 123
                                }
                            },
                            'Trigger': {
                                'CloudWatchAlarmDefinition': {
                                    'ComparisonOperator': 'GREATER_THAN_OR_EQUAL'|'GREATER_THAN'|'LESS_THAN'|'LESS_THAN_OR_EQUAL',
                                    'EvaluationPeriods': 123,
                                    'MetricName': 'string',
                                    'Namespace': 'string',
                                    'Period': 123,
                                    'Statistic': 'SAMPLE_COUNT'|'AVERAGE'|'SUM'|'MINIMUM'|'MAXIMUM',
                                    'Threshold': 123.0,
                                    'Unit': 'NONE'|'SECONDS'|'MICRO_SECONDS'|'MILLI_SECONDS'|'BYTES'|'KILO_BYTES'|'MEGA_BYTES'|'GIGA_BYTES'|'TERA_BYTES'|'BITS'|'KILO_BITS'|'MEGA_BITS'|'GIGA_BITS'|'TERA_BITS'|'PERCENT'|'COUNT'|'BYTES_PER_SECOND'|'KILO_BYTES_PER_SECOND'|'MEGA_BYTES_PER_SECOND'|'GIGA_BYTES_PER_SECOND'|'TERA_BYTES_PER_SECOND'|'BITS_PER_SECOND'|'KILO_BITS_PER_SECOND'|'MEGA_BITS_PER_SECOND'|'GIGA_BITS_PER_SECOND'|'TERA_BITS_PER_SECOND'|'COUNT_PER_SECOND',
                                    'Dimensions': [
                                        {
                                            'Key': 'string',
                                            'Value': 'string'
                                        },
                                    ]
                                }
                            }
                        },
                    ]
                }
            },
        ],
        'Marker': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def list_instances(ClusterId=None, InstanceGroupId=None, InstanceGroupTypes=None, InstanceFleetId=None, InstanceFleetType=None, InstanceStates=None, Marker=None):
    """
    Provides information about the cluster instances that Amazon EMR provisions on behalf of a user when it creates the cluster. For example, this operation indicates when the EC2 instances reach the Ready state, when instances become available to Amazon EMR to use for jobs, and the IP addresses for cluster instances, etc.
    See also: AWS API Documentation
    
    
    :example: response = client.list_instances(
        ClusterId='string',
        InstanceGroupId='string',
        InstanceGroupTypes=[
            'MASTER'|'CORE'|'TASK',
        ],
        InstanceFleetId='string',
        InstanceFleetType='MASTER'|'CORE'|'TASK',
        InstanceStates=[
            'AWAITING_FULFILLMENT'|'PROVISIONING'|'BOOTSTRAPPING'|'RUNNING'|'TERMINATED',
        ],
        Marker='string'
    )
    
    
    :type ClusterId: string
    :param ClusterId: [REQUIRED]
            The identifier of the cluster for which to list the instances.
            

    :type InstanceGroupId: string
    :param InstanceGroupId: The identifier of the instance group for which to list the instances.

    :type InstanceGroupTypes: list
    :param InstanceGroupTypes: The type of instance group for which to list the instances.
            (string) --
            

    :type InstanceFleetId: string
    :param InstanceFleetId: The unique identifier of the instance fleet.

    :type InstanceFleetType: string
    :param InstanceFleetType: The node type of the instance fleet. For example MASTER, CORE, or TASK.

    :type InstanceStates: list
    :param InstanceStates: A list of instance states that will filter the instances returned with this request.
            (string) --
            

    :type Marker: string
    :param Marker: The pagination token that indicates the next set of results to retrieve.

    :rtype: dict
    :return: {
        'Instances': [
            {
                'Id': 'string',
                'Ec2InstanceId': 'string',
                'PublicDnsName': 'string',
                'PublicIpAddress': 'string',
                'PrivateDnsName': 'string',
                'PrivateIpAddress': 'string',
                'Status': {
                    'State': 'AWAITING_FULFILLMENT'|'PROVISIONING'|'BOOTSTRAPPING'|'RUNNING'|'TERMINATED',
                    'StateChangeReason': {
                        'Code': 'INTERNAL_ERROR'|'VALIDATION_ERROR'|'INSTANCE_FAILURE'|'BOOTSTRAP_FAILURE'|'CLUSTER_TERMINATED',
                        'Message': 'string'
                    },
                    'Timeline': {
                        'CreationDateTime': datetime(2015, 1, 1),
                        'ReadyDateTime': datetime(2015, 1, 1),
                        'EndDateTime': datetime(2015, 1, 1)
                    }
                },
                'InstanceGroupId': 'string',
                'InstanceFleetId': 'string',
                'Market': 'ON_DEMAND'|'SPOT',
                'InstanceType': 'string',
                'EbsVolumes': [
                    {
                        'Device': 'string',
                        'VolumeId': 'string'
                    },
                ]
            },
        ],
        'Marker': 'string'
    }
    
    
    """
    pass

def list_security_configurations(Marker=None):
    """
    Lists all the security configurations visible to this account, providing their creation dates and times, and their names. This call returns a maximum of 50 clusters per call, but returns a marker to track the paging of the cluster list across multiple ListSecurityConfigurations calls.
    See also: AWS API Documentation
    
    
    :example: response = client.list_security_configurations(
        Marker='string'
    )
    
    
    :type Marker: string
    :param Marker: The pagination token that indicates the set of results to retrieve.

    :rtype: dict
    :return: {
        'SecurityConfigurations': [
            {
                'Name': 'string',
                'CreationDateTime': datetime(2015, 1, 1)
            },
        ],
        'Marker': 'string'
    }
    
    
    """
    pass

def list_steps(ClusterId=None, StepStates=None, StepIds=None, Marker=None):
    """
    Provides a list of steps for the cluster in reverse order unless you specify stepIds with the request.
    See also: AWS API Documentation
    
    
    :example: response = client.list_steps(
        ClusterId='string',
        StepStates=[
            'PENDING'|'CANCEL_PENDING'|'RUNNING'|'COMPLETED'|'CANCELLED'|'FAILED'|'INTERRUPTED',
        ],
        StepIds=[
            'string',
        ],
        Marker='string'
    )
    
    
    :type ClusterId: string
    :param ClusterId: [REQUIRED]
            The identifier of the cluster for which to list the steps.
            

    :type StepStates: list
    :param StepStates: The filter to limit the step list based on certain states.
            (string) --
            

    :type StepIds: list
    :param StepIds: The filter to limit the step list based on the identifier of the steps.
            (string) --
            

    :type Marker: string
    :param Marker: The pagination token that indicates the next set of results to retrieve.

    :rtype: dict
    :return: {
        'Steps': [
            {
                'Id': 'string',
                'Name': 'string',
                'Config': {
                    'Jar': 'string',
                    'Properties': {
                        'string': 'string'
                    },
                    'MainClass': 'string',
                    'Args': [
                        'string',
                    ]
                },
                'ActionOnFailure': 'TERMINATE_JOB_FLOW'|'TERMINATE_CLUSTER'|'CANCEL_AND_WAIT'|'CONTINUE',
                'Status': {
                    'State': 'PENDING'|'CANCEL_PENDING'|'RUNNING'|'COMPLETED'|'CANCELLED'|'FAILED'|'INTERRUPTED',
                    'StateChangeReason': {
                        'Code': 'NONE',
                        'Message': 'string'
                    },
                    'FailureDetails': {
                        'Reason': 'string',
                        'Message': 'string',
                        'LogFile': 'string'
                    },
                    'Timeline': {
                        'CreationDateTime': datetime(2015, 1, 1),
                        'StartDateTime': datetime(2015, 1, 1),
                        'EndDateTime': datetime(2015, 1, 1)
                    }
                }
            },
        ],
        'Marker': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def modify_instance_fleet(ClusterId=None, InstanceFleet=None):
    """
    Modifies the target On-Demand and target Spot capacities for the instance fleet with the specified InstanceFleetID within the cluster specified using ClusterID. The call either succeeds or fails atomically.
    See also: AWS API Documentation
    
    
    :example: response = client.modify_instance_fleet(
        ClusterId='string',
        InstanceFleet={
            'InstanceFleetId': 'string',
            'TargetOnDemandCapacity': 123,
            'TargetSpotCapacity': 123
        }
    )
    
    
    :type ClusterId: string
    :param ClusterId: [REQUIRED]
            The unique identifier of the cluster.
            

    :type InstanceFleet: dict
    :param InstanceFleet: [REQUIRED]
            The unique identifier of the instance fleet.
            InstanceFleetId (string) -- [REQUIRED]A unique identifier for the instance fleet.
            TargetOnDemandCapacity (integer) --The target capacity of On-Demand units for the instance fleet. For more information see InstanceFleetConfig$TargetOnDemandCapacity .
            TargetSpotCapacity (integer) --The target capacity of Spot units for the instance fleet. For more information, see InstanceFleetConfig$TargetSpotCapacity .
            

    """
    pass

def modify_instance_groups(ClusterId=None, InstanceGroups=None):
    """
    ModifyInstanceGroups modifies the number of nodes and configuration settings of an instance group. The input parameters include the new target instance count for the group and the instance group ID. The call will either succeed or fail atomically.
    See also: AWS API Documentation
    
    
    :example: response = client.modify_instance_groups(
        ClusterId='string',
        InstanceGroups=[
            {
                'InstanceGroupId': 'string',
                'InstanceCount': 123,
                'EC2InstanceIdsToTerminate': [
                    'string',
                ],
                'ShrinkPolicy': {
                    'DecommissionTimeout': 123,
                    'InstanceResizePolicy': {
                        'InstancesToTerminate': [
                            'string',
                        ],
                        'InstancesToProtect': [
                            'string',
                        ],
                        'InstanceTerminationTimeout': 123
                    }
                }
            },
        ]
    )
    
    
    :type ClusterId: string
    :param ClusterId: The ID of the cluster to which the instance group belongs.

    :type InstanceGroups: list
    :param InstanceGroups: Instance groups to change.
            (dict) --Modify an instance group size.
            InstanceGroupId (string) -- [REQUIRED]Unique ID of the instance group to expand or shrink.
            InstanceCount (integer) --Target size for the instance group.
            EC2InstanceIdsToTerminate (list) --The EC2 InstanceIds to terminate. After you terminate the instances, the instance group will not return to its original requested size.
            (string) --
            ShrinkPolicy (dict) --Policy for customizing shrink operations.
            DecommissionTimeout (integer) --The desired timeout for decommissioning an instance. Overrides the default YARN decommissioning timeout.
            InstanceResizePolicy (dict) --Custom policy for requesting termination protection or termination of specific instances when shrinking an instance group.
            InstancesToTerminate (list) --Specific list of instances to be terminated when shrinking an instance group.
            (string) --
            InstancesToProtect (list) --Specific list of instances to be protected when shrinking an instance group.
            (string) --
            InstanceTerminationTimeout (integer) --Decommissioning timeout override for the specific list of instances to be terminated.
            
            
            

    """
    pass

def put_auto_scaling_policy(ClusterId=None, InstanceGroupId=None, AutoScalingPolicy=None):
    """
    Creates or updates an automatic scaling policy for a core instance group or task instance group in an Amazon EMR cluster. The automatic scaling policy defines how an instance group dynamically adds and terminates EC2 instances in response to the value of a CloudWatch metric.
    See also: AWS API Documentation
    
    
    :example: response = client.put_auto_scaling_policy(
        ClusterId='string',
        InstanceGroupId='string',
        AutoScalingPolicy={
            'Constraints': {
                'MinCapacity': 123,
                'MaxCapacity': 123
            },
            'Rules': [
                {
                    'Name': 'string',
                    'Description': 'string',
                    'Action': {
                        'Market': 'ON_DEMAND'|'SPOT',
                        'SimpleScalingPolicyConfiguration': {
                            'AdjustmentType': 'CHANGE_IN_CAPACITY'|'PERCENT_CHANGE_IN_CAPACITY'|'EXACT_CAPACITY',
                            'ScalingAdjustment': 123,
                            'CoolDown': 123
                        }
                    },
                    'Trigger': {
                        'CloudWatchAlarmDefinition': {
                            'ComparisonOperator': 'GREATER_THAN_OR_EQUAL'|'GREATER_THAN'|'LESS_THAN'|'LESS_THAN_OR_EQUAL',
                            'EvaluationPeriods': 123,
                            'MetricName': 'string',
                            'Namespace': 'string',
                            'Period': 123,
                            'Statistic': 'SAMPLE_COUNT'|'AVERAGE'|'SUM'|'MINIMUM'|'MAXIMUM',
                            'Threshold': 123.0,
                            'Unit': 'NONE'|'SECONDS'|'MICRO_SECONDS'|'MILLI_SECONDS'|'BYTES'|'KILO_BYTES'|'MEGA_BYTES'|'GIGA_BYTES'|'TERA_BYTES'|'BITS'|'KILO_BITS'|'MEGA_BITS'|'GIGA_BITS'|'TERA_BITS'|'PERCENT'|'COUNT'|'BYTES_PER_SECOND'|'KILO_BYTES_PER_SECOND'|'MEGA_BYTES_PER_SECOND'|'GIGA_BYTES_PER_SECOND'|'TERA_BYTES_PER_SECOND'|'BITS_PER_SECOND'|'KILO_BITS_PER_SECOND'|'MEGA_BITS_PER_SECOND'|'GIGA_BITS_PER_SECOND'|'TERA_BITS_PER_SECOND'|'COUNT_PER_SECOND',
                            'Dimensions': [
                                {
                                    'Key': 'string',
                                    'Value': 'string'
                                },
                            ]
                        }
                    }
                },
            ]
        }
    )
    
    
    :type ClusterId: string
    :param ClusterId: [REQUIRED]
            Specifies the ID of a cluster. The instance group to which the automatic scaling policy is applied is within this cluster.
            

    :type InstanceGroupId: string
    :param InstanceGroupId: [REQUIRED]
            Specifies the ID of the instance group to which the automatic scaling policy is applied.
            

    :type AutoScalingPolicy: dict
    :param AutoScalingPolicy: [REQUIRED]
            Specifies the definition of the automatic scaling policy.
            Constraints (dict) -- [REQUIRED]The upper and lower EC2 instance limits for an automatic scaling policy. Automatic scaling activity will not cause an instance group to grow above or below these limits.
            MinCapacity (integer) -- [REQUIRED]The lower boundary of EC2 instances in an instance group below which scaling activities are not allowed to shrink. Scale-in activities will not terminate instances below this boundary.
            MaxCapacity (integer) -- [REQUIRED]The upper boundary of EC2 instances in an instance group beyond which scaling activities are not allowed to grow. Scale-out activities will not add instances beyond this boundary.
            Rules (list) -- [REQUIRED]The scale-in and scale-out rules that comprise the automatic scaling policy.
            (dict) --A scale-in or scale-out rule that defines scaling activity, including the CloudWatch metric alarm that triggers activity, how EC2 instances are added or removed, and the periodicity of adjustments. The automatic scaling policy for an instance group can comprise one or more automatic scaling rules.
            Name (string) -- [REQUIRED]The name used to identify an automatic scaling rule. Rule names must be unique within a scaling policy.
            Description (string) --A friendly, more verbose description of the automatic scaling rule.
            Action (dict) -- [REQUIRED]The conditions that trigger an automatic scaling activity.
            Market (string) --Not available for instance groups. Instance groups use the market type specified for the group.
            SimpleScalingPolicyConfiguration (dict) -- [REQUIRED]The type of adjustment the automatic scaling activity makes when triggered, and the periodicity of the adjustment.
            AdjustmentType (string) --The way in which EC2 instances are added (if ScalingAdjustment is a positive number) or terminated (if ScalingAdjustment is a negative number) each time the scaling activity is triggered. CHANGE_IN_CAPACITY is the default. CHANGE_IN_CAPACITY indicates that the EC2 instance count increments or decrements by ScalingAdjustment , which should be expressed as an integer. PERCENT_CHANGE_IN_CAPACITY indicates the instance count increments or decrements by the percentage specified by ScalingAdjustment , which should be expressed as a decimal. For example, 0.20 indicates an increase in 20% increments of cluster capacity. EXACT_CAPACITY indicates the scaling activity results in an instance group with the number of EC2 instances specified by ScalingAdjustment , which should be expressed as a positive integer.
            ScalingAdjustment (integer) -- [REQUIRED]The amount by which to scale in or scale out, based on the specified AdjustmentType . A positive value adds to the instance group's EC2 instance count while a negative number removes instances. If AdjustmentType is set to EXACT_CAPACITY , the number should only be a positive integer. If AdjustmentType is set to PERCENT_CHANGE_IN_CAPACITY , the value should express the percentage as a decimal. For example, -0.20 indicates a decrease in 20% increments of cluster capacity.
            CoolDown (integer) --The amount of time, in seconds, after a scaling activity completes before any further trigger-related scaling activities can start. The default value is 0.
            
            Trigger (dict) -- [REQUIRED]The CloudWatch alarm definition that determines when automatic scaling activity is triggered.
            CloudWatchAlarmDefinition (dict) -- [REQUIRED]The definition of a CloudWatch metric alarm. When the defined alarm conditions are met along with other trigger parameters, scaling activity begins.
            ComparisonOperator (string) -- [REQUIRED]Determines how the metric specified by MetricName is compared to the value specified by Threshold .
            EvaluationPeriods (integer) --The number of periods, expressed in seconds using Period , during which the alarm condition must exist before the alarm triggers automatic scaling activity. The default value is 1 .
            MetricName (string) -- [REQUIRED]The name of the CloudWatch metric that is watched to determine an alarm condition.
            Namespace (string) --The namespace for the CloudWatch metric. The default is AWS/ElasticMapReduce .
            Period (integer) -- [REQUIRED]The period, in seconds, over which the statistic is applied. EMR CloudWatch metrics are emitted every five minutes (300 seconds), so if an EMR CloudWatch metric is specified, specify 300 .
            Statistic (string) --The statistic to apply to the metric associated with the alarm. The default is AVERAGE .
            Threshold (float) -- [REQUIRED]The value against which the specified statistic is compared.
            Unit (string) --The unit of measure associated with the CloudWatch metric being watched. The value specified for Unit must correspond to the units specified in the CloudWatch metric.
            Dimensions (list) --A CloudWatch metric dimension.
            (dict) --A CloudWatch dimension, which is specified using a Key (known as a Name in CloudWatch), Value pair. By default, Amazon EMR uses one dimension whose Key is JobFlowID and Value is a variable representing the cluster ID, which is ${emr.clusterId} . This enables the rule to bootstrap when the cluster ID becomes available.
            Key (string) --The dimension name.
            Value (string) --The dimension value.
            
            
            
            

    :rtype: dict
    :return: {
        'ClusterId': 'string',
        'InstanceGroupId': 'string',
        'AutoScalingPolicy': {
            'Status': {
                'State': 'PENDING'|'ATTACHING'|'ATTACHED'|'DETACHING'|'DETACHED'|'FAILED',
                'StateChangeReason': {
                    'Code': 'USER_REQUEST'|'PROVISION_FAILURE'|'CLEANUP_FAILURE',
                    'Message': 'string'
                }
            },
            'Constraints': {
                'MinCapacity': 123,
                'MaxCapacity': 123
            },
            'Rules': [
                {
                    'Name': 'string',
                    'Description': 'string',
                    'Action': {
                        'Market': 'ON_DEMAND'|'SPOT',
                        'SimpleScalingPolicyConfiguration': {
                            'AdjustmentType': 'CHANGE_IN_CAPACITY'|'PERCENT_CHANGE_IN_CAPACITY'|'EXACT_CAPACITY',
                            'ScalingAdjustment': 123,
                            'CoolDown': 123
                        }
                    },
                    'Trigger': {
                        'CloudWatchAlarmDefinition': {
                            'ComparisonOperator': 'GREATER_THAN_OR_EQUAL'|'GREATER_THAN'|'LESS_THAN'|'LESS_THAN_OR_EQUAL',
                            'EvaluationPeriods': 123,
                            'MetricName': 'string',
                            'Namespace': 'string',
                            'Period': 123,
                            'Statistic': 'SAMPLE_COUNT'|'AVERAGE'|'SUM'|'MINIMUM'|'MAXIMUM',
                            'Threshold': 123.0,
                            'Unit': 'NONE'|'SECONDS'|'MICRO_SECONDS'|'MILLI_SECONDS'|'BYTES'|'KILO_BYTES'|'MEGA_BYTES'|'GIGA_BYTES'|'TERA_BYTES'|'BITS'|'KILO_BITS'|'MEGA_BITS'|'GIGA_BITS'|'TERA_BITS'|'PERCENT'|'COUNT'|'BYTES_PER_SECOND'|'KILO_BYTES_PER_SECOND'|'MEGA_BYTES_PER_SECOND'|'GIGA_BYTES_PER_SECOND'|'TERA_BYTES_PER_SECOND'|'BITS_PER_SECOND'|'KILO_BITS_PER_SECOND'|'MEGA_BITS_PER_SECOND'|'GIGA_BITS_PER_SECOND'|'TERA_BITS_PER_SECOND'|'COUNT_PER_SECOND',
                            'Dimensions': [
                                {
                                    'Key': 'string',
                                    'Value': 'string'
                                },
                            ]
                        }
                    }
                },
            ]
        }
    }
    
    
    """
    pass

def remove_auto_scaling_policy(ClusterId=None, InstanceGroupId=None):
    """
    Removes an automatic scaling policy from a specified instance group within an EMR cluster.
    See also: AWS API Documentation
    
    
    :example: response = client.remove_auto_scaling_policy(
        ClusterId='string',
        InstanceGroupId='string'
    )
    
    
    :type ClusterId: string
    :param ClusterId: [REQUIRED]
            Specifies the ID of a cluster. The instance group to which the automatic scaling policy is applied is within this cluster.
            

    :type InstanceGroupId: string
    :param InstanceGroupId: [REQUIRED]
            Specifies the ID of the instance group to which the scaling policy is applied.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def remove_tags(ResourceId=None, TagKeys=None):
    """
    Removes tags from an Amazon EMR resource. Tags make it easier to associate clusters in various ways, such as grouping clusters to track your Amazon EMR resource allocation costs. For more information, see Tagging Amazon EMR Resources .
    The following example removes the stack tag with value Prod from a cluster:
    See also: AWS API Documentation
    
    
    :example: response = client.remove_tags(
        ResourceId='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceId: string
    :param ResourceId: [REQUIRED]
            The Amazon EMR resource identifier from which tags will be removed. This value must be a cluster identifier.
            

    :type TagKeys: list
    :param TagKeys: [REQUIRED]
            A list of tag keys to remove from a resource.
            (string) --
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def run_job_flow(Name=None, LogUri=None, AdditionalInfo=None, AmiVersion=None, ReleaseLabel=None, Instances=None, Steps=None, BootstrapActions=None, SupportedProducts=None, NewSupportedProducts=None, Applications=None, Configurations=None, VisibleToAllUsers=None, JobFlowRole=None, ServiceRole=None, Tags=None, SecurityConfiguration=None, AutoScalingRole=None, ScaleDownBehavior=None):
    """
    RunJobFlow creates and starts running a new cluster (job flow). The cluster runs the steps specified. After the steps complete, the cluster stops and the HDFS partition is lost. To prevent loss of data, configure the last step of the job flow to store results in Amazon S3. If the  JobFlowInstancesConfig  KeepJobFlowAliveWhenNoSteps parameter is set to TRUE , the cluster transitions to the WAITING state rather than shutting down after the steps have completed.
    For additional protection, you can set the  JobFlowInstancesConfig  TerminationProtected parameter to TRUE to lock the cluster and prevent it from being terminated by API call, user intervention, or in the event of a job flow error.
    A maximum of 256 steps are allowed in each job flow.
    If your cluster is long-running (such as a Hive data warehouse) or complex, you may require more than 256 steps to process your data. You can bypass the 256-step limitation in various ways, including using the SSH shell to connect to the master node and submitting queries directly to the software running on the master node, such as Hive and Hadoop. For more information on how to do this, see Add More than 256 Steps to a Cluster in the Amazon EMR Management Guide .
    For long running clusters, we recommend that you periodically store your results.
    See also: AWS API Documentation
    
    
    :example: response = client.run_job_flow(
        Name='string',
        LogUri='string',
        AdditionalInfo='string',
        AmiVersion='string',
        ReleaseLabel='string',
        Instances={
            'MasterInstanceType': 'string',
            'SlaveInstanceType': 'string',
            'InstanceCount': 123,
            'InstanceGroups': [
                {
                    'Name': 'string',
                    'Market': 'ON_DEMAND'|'SPOT',
                    'InstanceRole': 'MASTER'|'CORE'|'TASK',
                    'BidPrice': 'string',
                    'InstanceType': 'string',
                    'InstanceCount': 123,
                    'Configurations': [
                        {
                            'Classification': 'string',
                            'Configurations': {'... recursive ...'},
                            'Properties': {
                                'string': 'string'
                            }
                        },
                    ],
                    'EbsConfiguration': {
                        'EbsBlockDeviceConfigs': [
                            {
                                'VolumeSpecification': {
                                    'VolumeType': 'string',
                                    'Iops': 123,
                                    'SizeInGB': 123
                                },
                                'VolumesPerInstance': 123
                            },
                        ],
                        'EbsOptimized': True|False
                    },
                    'AutoScalingPolicy': {
                        'Constraints': {
                            'MinCapacity': 123,
                            'MaxCapacity': 123
                        },
                        'Rules': [
                            {
                                'Name': 'string',
                                'Description': 'string',
                                'Action': {
                                    'Market': 'ON_DEMAND'|'SPOT',
                                    'SimpleScalingPolicyConfiguration': {
                                        'AdjustmentType': 'CHANGE_IN_CAPACITY'|'PERCENT_CHANGE_IN_CAPACITY'|'EXACT_CAPACITY',
                                        'ScalingAdjustment': 123,
                                        'CoolDown': 123
                                    }
                                },
                                'Trigger': {
                                    'CloudWatchAlarmDefinition': {
                                        'ComparisonOperator': 'GREATER_THAN_OR_EQUAL'|'GREATER_THAN'|'LESS_THAN'|'LESS_THAN_OR_EQUAL',
                                        'EvaluationPeriods': 123,
                                        'MetricName': 'string',
                                        'Namespace': 'string',
                                        'Period': 123,
                                        'Statistic': 'SAMPLE_COUNT'|'AVERAGE'|'SUM'|'MINIMUM'|'MAXIMUM',
                                        'Threshold': 123.0,
                                        'Unit': 'NONE'|'SECONDS'|'MICRO_SECONDS'|'MILLI_SECONDS'|'BYTES'|'KILO_BYTES'|'MEGA_BYTES'|'GIGA_BYTES'|'TERA_BYTES'|'BITS'|'KILO_BITS'|'MEGA_BITS'|'GIGA_BITS'|'TERA_BITS'|'PERCENT'|'COUNT'|'BYTES_PER_SECOND'|'KILO_BYTES_PER_SECOND'|'MEGA_BYTES_PER_SECOND'|'GIGA_BYTES_PER_SECOND'|'TERA_BYTES_PER_SECOND'|'BITS_PER_SECOND'|'KILO_BITS_PER_SECOND'|'MEGA_BITS_PER_SECOND'|'GIGA_BITS_PER_SECOND'|'TERA_BITS_PER_SECOND'|'COUNT_PER_SECOND',
                                        'Dimensions': [
                                            {
                                                'Key': 'string',
                                                'Value': 'string'
                                            },
                                        ]
                                    }
                                }
                            },
                        ]
                    }
                },
            ],
            'InstanceFleets': [
                {
                    'Name': 'string',
                    'InstanceFleetType': 'MASTER'|'CORE'|'TASK',
                    'TargetOnDemandCapacity': 123,
                    'TargetSpotCapacity': 123,
                    'InstanceTypeConfigs': [
                        {
                            'InstanceType': 'string',
                            'WeightedCapacity': 123,
                            'BidPrice': 'string',
                            'BidPriceAsPercentageOfOnDemandPrice': 123.0,
                            'EbsConfiguration': {
                                'EbsBlockDeviceConfigs': [
                                    {
                                        'VolumeSpecification': {
                                            'VolumeType': 'string',
                                            'Iops': 123,
                                            'SizeInGB': 123
                                        },
                                        'VolumesPerInstance': 123
                                    },
                                ],
                                'EbsOptimized': True|False
                            },
                            'Configurations': [
                                {
                                    'Classification': 'string',
                                    'Configurations': {'... recursive ...'},
                                    'Properties': {
                                        'string': 'string'
                                    }
                                },
                            ]
                        },
                    ],
                    'LaunchSpecifications': {
                        'SpotSpecification': {
                            'TimeoutDurationMinutes': 123,
                            'TimeoutAction': 'SWITCH_TO_ON_DEMAND'|'TERMINATE_CLUSTER',
                            'BlockDurationMinutes': 123
                        }
                    }
                },
            ],
            'Ec2KeyName': 'string',
            'Placement': {
                'AvailabilityZone': 'string',
                'AvailabilityZones': [
                    'string',
                ]
            },
            'KeepJobFlowAliveWhenNoSteps': True|False,
            'TerminationProtected': True|False,
            'HadoopVersion': 'string',
            'Ec2SubnetId': 'string',
            'Ec2SubnetIds': [
                'string',
            ],
            'EmrManagedMasterSecurityGroup': 'string',
            'EmrManagedSlaveSecurityGroup': 'string',
            'ServiceAccessSecurityGroup': 'string',
            'AdditionalMasterSecurityGroups': [
                'string',
            ],
            'AdditionalSlaveSecurityGroups': [
                'string',
            ]
        },
        Steps=[
            {
                'Name': 'string',
                'ActionOnFailure': 'TERMINATE_JOB_FLOW'|'TERMINATE_CLUSTER'|'CANCEL_AND_WAIT'|'CONTINUE',
                'HadoopJarStep': {
                    'Properties': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        },
                    ],
                    'Jar': 'string',
                    'MainClass': 'string',
                    'Args': [
                        'string',
                    ]
                }
            },
        ],
        BootstrapActions=[
            {
                'Name': 'string',
                'ScriptBootstrapAction': {
                    'Path': 'string',
                    'Args': [
                        'string',
                    ]
                }
            },
        ],
        SupportedProducts=[
            'string',
        ],
        NewSupportedProducts=[
            {
                'Name': 'string',
                'Args': [
                    'string',
                ]
            },
        ],
        Applications=[
            {
                'Name': 'string',
                'Version': 'string',
                'Args': [
                    'string',
                ],
                'AdditionalInfo': {
                    'string': 'string'
                }
            },
        ],
        Configurations=[
            {
                'Classification': 'string',
                'Configurations': {'... recursive ...'},
                'Properties': {
                    'string': 'string'
                }
            },
        ],
        VisibleToAllUsers=True|False,
        JobFlowRole='string',
        ServiceRole='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        SecurityConfiguration='string',
        AutoScalingRole='string',
        ScaleDownBehavior='TERMINATE_AT_INSTANCE_HOUR'|'TERMINATE_AT_TASK_COMPLETION'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the job flow.
            

    :type LogUri: string
    :param LogUri: The location in Amazon S3 to write the log files of the job flow. If a value is not provided, logs are not created.

    :type AdditionalInfo: string
    :param AdditionalInfo: A JSON string for selecting additional features.

    :type AmiVersion: string
    :param AmiVersion: 
            Note
            For Amazon EMR releases 3.x and 2.x. For Amazon EMR releases 4.x and greater, use ReleaseLabel.
            The version of the Amazon Machine Image (AMI) to use when launching Amazon EC2 instances in the job flow. The following values are valid:
            The version number of the AMI to use, for example, '2.0.'
            If the AMI supports multiple versions of Hadoop (for example, AMI 1.0 supports both Hadoop 0.18 and 0.20) you can use the JobFlowInstancesConfig HadoopVersion parameter to modify the version of Hadoop from the defaults shown above.
            For details about the AMI versions currently supported by Amazon Elastic MapReduce, see AMI Versions Supported in Elastic MapReduce in the Amazon Elastic MapReduce Developer Guide.
            Note
            Previously, the EMR AMI version API parameter options allowed you to use latest for the latest AMI version rather than specify a numerical value. Some regions no longer support this deprecated option as they only have a newer release label version of EMR, which requires you to specify an EMR release label release (EMR 4.x or later).
            

    :type ReleaseLabel: string
    :param ReleaseLabel: 
            Note
            Amazon EMR releases 4.x or later.
            The release label for the Amazon EMR release. For Amazon EMR 3.x and 2.x AMIs, use amiVersion instead instead of ReleaseLabel.
            

    :type Instances: dict
    :param Instances: [REQUIRED]
            A specification of the number and type of Amazon EC2 instances.
            MasterInstanceType (string) --The EC2 instance type of the master node.
            SlaveInstanceType (string) --The EC2 instance type of the slave nodes.
            InstanceCount (integer) --The number of EC2 instances in the cluster.
            InstanceGroups (list) --Configuration for the instance groups in a cluster.
            (dict) --Configuration defining a new instance group.
            Name (string) --Friendly name given to the instance group.
            Market (string) --Market type of the EC2 instances used to create a cluster node.
            InstanceRole (string) -- [REQUIRED]The role of the instance group in the cluster.
            BidPrice (string) --Bid price for each EC2 instance in the instance group when launching nodes as Spot Instances, expressed in USD.
            InstanceType (string) -- [REQUIRED]The EC2 instance type for all instances in the instance group.
            InstanceCount (integer) -- [REQUIRED]Target number of instances for the instance group.
            Configurations (list) --
            Note
            Amazon EMR releases 4.x or later.
            The list of configurations supplied for an EMR cluster instance group. You can specify a separate configuration for each instance group (master, core, and task).
            (dict) --
            Note
            Amazon EMR releases 4.x or later.
            An optional configuration specification to be used when provisioning cluster instances, which can include configurations for applications and software bundled with Amazon EMR. A configuration consists of a classification, properties, and optional nested configurations. A classification refers to an application-specific configuration file. Properties are the settings you want to change in that file. For more information, see Configuring Applications .
            Classification (string) --The classification within a configuration.
            Configurations (list) --A list of additional configurations to apply within a configuration object.
            Properties (dict) --A set of properties specified within a configuration classification.
            (string) --
            (string) --
            
            
            EbsConfiguration (dict) --EBS configurations that will be attached to each EC2 instance in the instance group.
            EbsBlockDeviceConfigs (list) --An array of Amazon EBS volume specifications attached to a cluster instance.
            (dict) --Configuration of requested EBS block device associated with the instance group with count of volumes that will be associated to every instance.
            VolumeSpecification (dict) -- [REQUIRED]EBS volume specifications such as volume type, IOPS, and size (GiB) that will be requested for the EBS volume attached to an EC2 instance in the cluster.
            VolumeType (string) -- [REQUIRED]The volume type. Volume types supported are gp2, io1, standard.
            Iops (integer) --The number of I/O operations per second (IOPS) that the volume supports.
            SizeInGB (integer) -- [REQUIRED]The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the volume type is EBS-optimized, the minimum value is 10.
            VolumesPerInstance (integer) --Number of EBS volumes with a specific volume configuration that will be associated with every instance in the instance group
            
            EbsOptimized (boolean) --Indicates whether an Amazon EBS volume is EBS-optimized.
            AutoScalingPolicy (dict) --An automatic scaling policy for a core instance group or task instance group in an Amazon EMR cluster. The automatic scaling policy defines how an instance group dynamically adds and terminates EC2 instances in response to the value of a CloudWatch metric. See PutAutoScalingPolicy .
            Constraints (dict) -- [REQUIRED]The upper and lower EC2 instance limits for an automatic scaling policy. Automatic scaling activity will not cause an instance group to grow above or below these limits.
            MinCapacity (integer) -- [REQUIRED]The lower boundary of EC2 instances in an instance group below which scaling activities are not allowed to shrink. Scale-in activities will not terminate instances below this boundary.
            MaxCapacity (integer) -- [REQUIRED]The upper boundary of EC2 instances in an instance group beyond which scaling activities are not allowed to grow. Scale-out activities will not add instances beyond this boundary.
            Rules (list) -- [REQUIRED]The scale-in and scale-out rules that comprise the automatic scaling policy.
            (dict) --A scale-in or scale-out rule that defines scaling activity, including the CloudWatch metric alarm that triggers activity, how EC2 instances are added or removed, and the periodicity of adjustments. The automatic scaling policy for an instance group can comprise one or more automatic scaling rules.
            Name (string) -- [REQUIRED]The name used to identify an automatic scaling rule. Rule names must be unique within a scaling policy.
            Description (string) --A friendly, more verbose description of the automatic scaling rule.
            Action (dict) -- [REQUIRED]The conditions that trigger an automatic scaling activity.
            Market (string) --Not available for instance groups. Instance groups use the market type specified for the group.
            SimpleScalingPolicyConfiguration (dict) -- [REQUIRED]The type of adjustment the automatic scaling activity makes when triggered, and the periodicity of the adjustment.
            AdjustmentType (string) --The way in which EC2 instances are added (if ScalingAdjustment is a positive number) or terminated (if ScalingAdjustment is a negative number) each time the scaling activity is triggered. CHANGE_IN_CAPACITY is the default. CHANGE_IN_CAPACITY indicates that the EC2 instance count increments or decrements by ScalingAdjustment , which should be expressed as an integer. PERCENT_CHANGE_IN_CAPACITY indicates the instance count increments or decrements by the percentage specified by ScalingAdjustment , which should be expressed as a decimal. For example, 0.20 indicates an increase in 20% increments of cluster capacity. EXACT_CAPACITY indicates the scaling activity results in an instance group with the number of EC2 instances specified by ScalingAdjustment , which should be expressed as a positive integer.
            ScalingAdjustment (integer) -- [REQUIRED]The amount by which to scale in or scale out, based on the specified AdjustmentType . A positive value adds to the instance group's EC2 instance count while a negative number removes instances. If AdjustmentType is set to EXACT_CAPACITY , the number should only be a positive integer. If AdjustmentType is set to PERCENT_CHANGE_IN_CAPACITY , the value should express the percentage as a decimal. For example, -0.20 indicates a decrease in 20% increments of cluster capacity.
            CoolDown (integer) --The amount of time, in seconds, after a scaling activity completes before any further trigger-related scaling activities can start. The default value is 0.
            
            Trigger (dict) -- [REQUIRED]The CloudWatch alarm definition that determines when automatic scaling activity is triggered.
            CloudWatchAlarmDefinition (dict) -- [REQUIRED]The definition of a CloudWatch metric alarm. When the defined alarm conditions are met along with other trigger parameters, scaling activity begins.
            ComparisonOperator (string) -- [REQUIRED]Determines how the metric specified by MetricName is compared to the value specified by Threshold .
            EvaluationPeriods (integer) --The number of periods, expressed in seconds using Period , during which the alarm condition must exist before the alarm triggers automatic scaling activity. The default value is 1 .
            MetricName (string) -- [REQUIRED]The name of the CloudWatch metric that is watched to determine an alarm condition.
            Namespace (string) --The namespace for the CloudWatch metric. The default is AWS/ElasticMapReduce .
            Period (integer) -- [REQUIRED]The period, in seconds, over which the statistic is applied. EMR CloudWatch metrics are emitted every five minutes (300 seconds), so if an EMR CloudWatch metric is specified, specify 300 .
            Statistic (string) --The statistic to apply to the metric associated with the alarm. The default is AVERAGE .
            Threshold (float) -- [REQUIRED]The value against which the specified statistic is compared.
            Unit (string) --The unit of measure associated with the CloudWatch metric being watched. The value specified for Unit must correspond to the units specified in the CloudWatch metric.
            Dimensions (list) --A CloudWatch metric dimension.
            (dict) --A CloudWatch dimension, which is specified using a Key (known as a Name in CloudWatch), Value pair. By default, Amazon EMR uses one dimension whose Key is JobFlowID and Value is a variable representing the cluster ID, which is ${emr.clusterId} . This enables the rule to bootstrap when the cluster ID becomes available.
            Key (string) --The dimension name.
            Value (string) --The dimension value.
            
            
            
            
            InstanceFleets (list) --
            Note
            The instance fleet configuration is available only in Amazon EMR versions 4.8.0 and later, excluding 5.0.x versions.
            Describes the EC2 instances and instance configurations for clusters that use the instance fleet configuration.
            (dict) --The configuration that defines an instance fleet.
            Note
            The instance fleet configuration is available only in Amazon EMR versions 4.8.0 and later, excluding 5.0.x versions.
            Name (string) --The friendly name of the instance fleet.
            InstanceFleetType (string) -- [REQUIRED]The node type that the instance fleet hosts. Valid values are MASTER,CORE,and TASK.
            TargetOnDemandCapacity (integer) --The target capacity of On-Demand units for the instance fleet, which determines how many On-Demand instances to provision. When the instance fleet launches, Amazon EMR tries to provision On-Demand instances as specified by InstanceTypeConfig . Each instance configuration has a specified WeightedCapacity . When an On-Demand instance is provisioned, the WeightedCapacity units count toward the target capacity. Amazon EMR provisions instances until the target capacity is totally fulfilled, even if this results in an overage. For example, if there are 2 units remaining to fulfill capacity, and Amazon EMR can only provision an instance with a WeightedCapacity of 5 units, the instance is provisioned, and the target capacity is exceeded by 3 units.
            Note
            If not specified or set to 0, only Spot instances are provisioned for the instance fleet using TargetSpotCapacity . At least one of TargetSpotCapacity and TargetOnDemandCapacity should be greater than 0. For a master instance fleet, only one of TargetSpotCapacity and TargetOnDemandCapacity can be specified, and its value must be 1.
            TargetSpotCapacity (integer) --The target capacity of Spot units for the instance fleet, which determines how many Spot instances to provision. When the instance fleet launches, Amazon EMR tries to provision Spot instances as specified by InstanceTypeConfig . Each instance configuration has a specified WeightedCapacity . When a Spot instance is provisioned, the WeightedCapacity units count toward the target capacity. Amazon EMR provisions instances until the target capacity is totally fulfilled, even if this results in an overage. For example, if there are 2 units remaining to fulfill capacity, and Amazon EMR can only provision an instance with a WeightedCapacity of 5 units, the instance is provisioned, and the target capacity is exceeded by 3 units.
            Note
            If not specified or set to 0, only On-Demand instances are provisioned for the instance fleet. At least one of TargetSpotCapacity and TargetOnDemandCapacity should be greater than 0. For a master instance fleet, only one of TargetSpotCapacity and TargetOnDemandCapacity can be specified, and its value must be 1.
            InstanceTypeConfigs (list) --The instance type configurations that define the EC2 instances in the instance fleet.
            (dict) --An instance type configuration for each instance type in an instance fleet, which determines the EC2 instances Amazon EMR attempts to provision to fulfill On-Demand and Spot target capacities. There can be a maximum of 5 instance type configurations in a fleet.
            Note
            The instance fleet configuration is available only in Amazon EMR versions 4.8.0 and later, excluding 5.0.x versions.
            InstanceType (string) -- [REQUIRED]An EC2 instance type, such as m3.xlarge .
            WeightedCapacity (integer) --The number of units that a provisioned instance of this type provides toward fulfilling the target capacities defined in InstanceFleetConfig . This value is 1 for a master instance fleet, and must be greater than 0 for core and task instance fleets.
            BidPrice (string) --The bid price for each EC2 Spot instance type as defined by InstanceType . Expressed in USD. If neither BidPrice nor BidPriceAsPercentageOfOnDemandPrice is provided, BidPriceAsPercentageOfOnDemandPrice defaults to 100%.
            BidPriceAsPercentageOfOnDemandPrice (float) --The bid price, as a percentage of On-Demand price, for each EC2 Spot instance as defined by InstanceType . Expressed as a number between 0 and 1000 (for example, 20 specifies 20%). If neither BidPrice nor BidPriceAsPercentageOfOnDemandPrice is provided, BidPriceAsPercentageOfOnDemandPrice defaults to 100%.
            EbsConfiguration (dict) --The configuration of Amazon Elastic Block Storage (EBS) attached to each instance as defined by InstanceType .
            EbsBlockDeviceConfigs (list) --An array of Amazon EBS volume specifications attached to a cluster instance.
            (dict) --Configuration of requested EBS block device associated with the instance group with count of volumes that will be associated to every instance.
            VolumeSpecification (dict) -- [REQUIRED]EBS volume specifications such as volume type, IOPS, and size (GiB) that will be requested for the EBS volume attached to an EC2 instance in the cluster.
            VolumeType (string) -- [REQUIRED]The volume type. Volume types supported are gp2, io1, standard.
            Iops (integer) --The number of I/O operations per second (IOPS) that the volume supports.
            SizeInGB (integer) -- [REQUIRED]The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the volume type is EBS-optimized, the minimum value is 10.
            VolumesPerInstance (integer) --Number of EBS volumes with a specific volume configuration that will be associated with every instance in the instance group
            
            EbsOptimized (boolean) --Indicates whether an Amazon EBS volume is EBS-optimized.
            Configurations (list) --A configuration classification that applies when provisioning cluster instances, which can include configurations for applications and software that run on the cluster.
            (dict) --
            Note
            Amazon EMR releases 4.x or later.
            An optional configuration specification to be used when provisioning cluster instances, which can include configurations for applications and software bundled with Amazon EMR. A configuration consists of a classification, properties, and optional nested configurations. A classification refers to an application-specific configuration file. Properties are the settings you want to change in that file. For more information, see Configuring Applications .
            Classification (string) --The classification within a configuration.
            Configurations (list) --A list of additional configurations to apply within a configuration object.
            Properties (dict) --A set of properties specified within a configuration classification.
            (string) --
            (string) --
            
            
            
            LaunchSpecifications (dict) --The launch specification for the instance fleet.
            SpotSpecification (dict) -- [REQUIRED]The launch specification for Spot instances in the fleet, which determines the defined duration and provisioning timeout behavior.
            TimeoutDurationMinutes (integer) -- [REQUIRED]The spot provisioning timeout period in minutes. If Spot instances are not provisioned within this time period, the TimeOutAction is taken. Minimum value is 5 and maximum value is 1440. The timeout applies only during initial provisioning, when the cluster is first created.
            TimeoutAction (string) -- [REQUIRED]The action to take when TargetSpotCapacity has not been fulfilled when the TimeoutDurationMinutes has expired. Spot instances are not uprovisioned within the Spot provisioining timeout. Valid values are TERMINATE_CLUSTER and SWITCH_TO_ON_DEMAND to fulfill the remaining capacity.
            BlockDurationMinutes (integer) --The defined duration for Spot instances (also known as Spot blocks) in minutes. When specified, the Spot instance does not terminate before the defined duration expires, and defined duration pricing for Spot instances applies. Valid values are 60, 120, 180, 240, 300, or 360. The duration period starts as soon as a Spot instance receives its instance ID. At the end of the duration, Amazon EC2 marks the Spot instance for termination and provides a Spot instance termination notice, which gives the instance a two-minute warning before it terminates.
            
            
            Ec2KeyName (string) --The name of the EC2 key pair that can be used to ssh to the master node as the user called 'hadoop.'
            Placement (dict) --The Availability Zone in which the cluster runs.
            AvailabilityZone (string) --The Amazon EC2 Availability Zone for the cluster. AvailabilityZone is used for uniform instance groups, while AvailabilityZones (plural) is used for instance fleets.
            AvailabilityZones (list) --When multiple Availability Zones are specified, Amazon EMR evaluates them and launches instances in the optimal Availability Zone. AvailabilityZones is used for instance fleets, while AvailabilityZone (singular) is used for uniform instance groups.
            Note
            The instance fleet configuration is available only in Amazon EMR versions 4.8.0 and later, excluding 5.0.x versions.
            (string) --
            
            KeepJobFlowAliveWhenNoSteps (boolean) --Specifies whether the cluster should remain available after completing all steps.
            TerminationProtected (boolean) --Specifies whether to lock the cluster to prevent the Amazon EC2 instances from being terminated by API call, user intervention, or in the event of a job-flow error.
            HadoopVersion (string) --The Hadoop version for the cluster. Valid inputs are '0.18' (deprecated), '0.20' (deprecated), '0.20.205' (deprecated), '1.0.3', '2.2.0', or '2.4.0'. If you do not set this value, the default of 0.18 is used, unless the AmiVersion parameter is set in the RunJobFlow call, in which case the default version of Hadoop for that AMI version is used.
            Ec2SubnetId (string) --Applies to clusters that use the uniform instance group configuration. To launch the cluster in Amazon Virtual Private Cloud (Amazon VPC), set this parameter to the identifier of the Amazon VPC subnet where you want the cluster to launch. If you do not specify this value, the cluster launches in the normal Amazon Web Services cloud, outside of an Amazon VPC, if the account launching the cluster supports EC2 Classic networks in the region where the cluster launches.
            Amazon VPC currently does not support cluster compute quadruple extra large (cc1.4xlarge) instances. Thus you cannot specify the cc1.4xlarge instance type for clusters launched in an Amazon VPC.
            Ec2SubnetIds (list) --Applies to clusters that use the instance fleet configuration. When multiple EC2 subnet IDs are specified, Amazon EMR evaluates them and launches instances in the optimal subnet.
            Note
            The instance fleet configuration is available only in Amazon EMR versions 4.8.0 and later, excluding 5.0.x versions.
            (string) --
            EmrManagedMasterSecurityGroup (string) --The identifier of the Amazon EC2 security group for the master node.
            EmrManagedSlaveSecurityGroup (string) --The identifier of the Amazon EC2 security group for the slave nodes.
            ServiceAccessSecurityGroup (string) --The identifier of the Amazon EC2 security group for the Amazon EMR service to access clusters in VPC private subnets.
            AdditionalMasterSecurityGroups (list) --A list of additional Amazon EC2 security group IDs for the master node.
            (string) --
            AdditionalSlaveSecurityGroups (list) --A list of additional Amazon EC2 security group IDs for the slave nodes.
            (string) --
            

    :type Steps: list
    :param Steps: A list of steps to run.
            (dict) --Specification of a cluster (job flow) step.
            Name (string) -- [REQUIRED]The name of the step.
            ActionOnFailure (string) --The action to take if the step fails.
            HadoopJarStep (dict) -- [REQUIRED]The JAR file used for the step.
            Properties (list) --A list of Java properties that are set when the step runs. You can use these properties to pass key value pairs to your main function.
            (dict) --A key value pair.
            Key (string) --The unique identifier of a key value pair.
            Value (string) --The value part of the identified key.
            
            Jar (string) -- [REQUIRED]A path to a JAR file run during the step.
            MainClass (string) --The name of the main class in the specified Java file. If not specified, the JAR file should specify a Main-Class in its manifest file.
            Args (list) --A list of command line arguments passed to the JAR file's main function when executed.
            (string) --
            
            

    :type BootstrapActions: list
    :param BootstrapActions: A list of bootstrap actions to run before Hadoop starts on the cluster nodes.
            (dict) --Configuration of a bootstrap action.
            Name (string) -- [REQUIRED]The name of the bootstrap action.
            ScriptBootstrapAction (dict) -- [REQUIRED]The script run by the bootstrap action.
            Path (string) -- [REQUIRED]Location of the script to run during a bootstrap action. Can be either a location in Amazon S3 or on a local file system.
            Args (list) --A list of command line arguments to pass to the bootstrap action script.
            (string) --
            
            

    :type SupportedProducts: list
    :param SupportedProducts: 
            Note
            For Amazon EMR releases 3.x and 2.x. For Amazon EMR releases 4.x and greater, use Applications.
            A list of strings that indicates third-party software to use. For more information, see Use Third Party Applications with Amazon EMR . Currently supported values are:
            'mapr-m3' - launch the job flow using MapR M3 Edition.
            'mapr-m5' - launch the job flow using MapR M5 Edition.
            (string) --
            

    :type NewSupportedProducts: list
    :param NewSupportedProducts: 
            Note
            For Amazon EMR releases 3.x and 2.x. For Amazon EMR releases 4.x and greater, use Applications.
            A list of strings that indicates third-party software to use with the job flow that accepts a user argument list. EMR accepts and forwards the argument list to the corresponding installation script as bootstrap action arguments. For more information, see 'Launch a Job Flow on the MapR Distribution for Hadoop' in the Amazon EMR Developer Guide . Supported values are:
            'mapr-m3' - launch the cluster using MapR M3 Edition.
            'mapr-m5' - launch the cluster using MapR M5 Edition.
            'mapr' with the user arguments specifying '--edition,m3' or '--edition,m5' - launch the job flow using MapR M3 or M5 Edition respectively.
            'mapr-m7' - launch the cluster using MapR M7 Edition.
            'hunk' - launch the cluster with the Hunk Big Data Analtics Platform.
            'hue'- launch the cluster with Hue installed.
            'spark' - launch the cluster with Apache Spark installed.
            'ganglia' - launch the cluster with the Ganglia Monitoring System installed.
            (dict) --The list of supported product configurations which allow user-supplied arguments. EMR accepts these arguments and forwards them to the corresponding installation script as bootstrap action arguments.
            Name (string) --The name of the product configuration.
            Args (list) --The list of user-supplied arguments.
            (string) --
            
            

    :type Applications: list
    :param Applications: 
            Note
            Amazon EMR releases 4.x or later.
            A list of applications for the cluster. Valid values are: 'Hadoop', 'Hive', 'Mahout', 'Pig', and 'Spark.' They are case insensitive.
            (dict) --An application is any Amazon or third-party software that you can add to the cluster. This structure contains a list of strings that indicates the software to use with the cluster and accepts a user argument list. Amazon EMR accepts and forwards the argument list to the corresponding installation script as bootstrap action argument. For more information, see Using the MapR Distribution for Hadoop . Currently supported values are:
            'mapr-m3' - launch the cluster using MapR M3 Edition.
            'mapr-m5' - launch the cluster using MapR M5 Edition.
            'mapr' with the user arguments specifying '--edition,m3' or '--edition,m5' - launch the cluster using MapR M3 or M5 Edition, respectively.
            Note
            In Amazon EMR releases 4.0 and greater, the only accepted parameter is the application name. To pass arguments to applications, you supply a configuration for each application.
            Name (string) --The name of the application.
            Version (string) --The version of the application.
            Args (list) --Arguments for Amazon EMR to pass to the application.
            (string) --
            AdditionalInfo (dict) --This option is for advanced users only. This is meta information about third-party applications that third-party vendors use for testing purposes.
            (string) --
            (string) --
            
            

    :type Configurations: list
    :param Configurations: 
            Note
            Amazon EMR releases 4.x or later.
            The list of configurations supplied for the EMR cluster you are creating.
            (dict) --
            Note
            Amazon EMR releases 4.x or later.
            An optional configuration specification to be used when provisioning cluster instances, which can include configurations for applications and software bundled with Amazon EMR. A configuration consists of a classification, properties, and optional nested configurations. A classification refers to an application-specific configuration file. Properties are the settings you want to change in that file. For more information, see Configuring Applications .
            Classification (string) --The classification within a configuration.
            Configurations (list) --A list of additional configurations to apply within a configuration object.
            Properties (dict) --A set of properties specified within a configuration classification.
            (string) --
            (string) --
            
            

    :type VisibleToAllUsers: boolean
    :param VisibleToAllUsers: Whether the cluster is visible to all IAM users of the AWS account associated with the cluster. If this value is set to true , all IAM users of that AWS account can view and (if they have the proper policy permissions set) manage the cluster. If it is set to false , only the IAM user that created the cluster can view and manage it.

    :type JobFlowRole: string
    :param JobFlowRole: Also called instance profile and EC2 role. An IAM role for an EMR cluster. The EC2 instances of the cluster assume this role. The default role is EMR_EC2_DefaultRole . In order to use the default role, you must have already created it using the CLI or console.

    :type ServiceRole: string
    :param ServiceRole: The IAM role that will be assumed by the Amazon EMR service to access AWS resources on your behalf.

    :type Tags: list
    :param Tags: A list of tags to associate with a cluster and propagate to Amazon EC2 instances.
            (dict) --A key/value pair containing user-defined metadata that you can associate with an Amazon EMR resource. Tags make it easier to associate clusters in various ways, such as grouping clusters to track your Amazon EMR resource allocation costs. For more information, see Tagging Amazon EMR Resources .
            Key (string) --A user-defined key, which is the minimum required information for a valid tag. For more information, see Tagging Amazon EMR Resources .
            Value (string) --A user-defined value, which is optional in a tag. For more information, see Tagging Amazon EMR Resources .
            
            

    :type SecurityConfiguration: string
    :param SecurityConfiguration: The name of a security configuration to apply to the cluster.

    :type AutoScalingRole: string
    :param AutoScalingRole: An IAM role for automatic scaling policies. The default role is EMR_AutoScaling_DefaultRole . The IAM role provides permissions that the automatic scaling feature requires to launch and terminate EC2 instances in an instance group.

    :type ScaleDownBehavior: string
    :param ScaleDownBehavior: Specifies the way that individual Amazon EC2 instances terminate when an automatic scale-in activity occurs or an instance group is resized. TERMINATE_AT_INSTANCE_HOUR indicates that Amazon EMR terminates nodes at the instance-hour boundary, regardless of when the request to terminate the instance was submitted. This option is only available with Amazon EMR 5.1.0 and later and is the default for clusters created using that version. TERMINATE_AT_TASK_COMPLETION indicates that Amazon EMR blacklists and drains tasks from nodes before terminating the Amazon EC2 instances, regardless of the instance-hour boundary. With either behavior, Amazon EMR removes the least active nodes first and blocks instance termination if it could lead to HDFS corruption. TERMINATE_AT_TASK_COMPLETION available only in Amazon EMR version 4.1.0 and later, and is the default for versions of Amazon EMR earlier than 5.1.0.

    :rtype: dict
    :return: {
        'JobFlowId': 'string'
    }
    
    
    """
    pass

def set_termination_protection(JobFlowIds=None, TerminationProtected=None):
    """
    SetTerminationProtection locks a cluster (job flow) so the EC2 instances in the cluster cannot be terminated by user intervention, an API call, or in the event of a job-flow error. The cluster still terminates upon successful completion of the job flow. Calling SetTerminationProtection on a cluster is similar to calling the Amazon EC2 DisableAPITermination API on all EC2 instances in a cluster.
    To terminate a cluster that has been locked by setting SetTerminationProtection to true , you must first unlock the job flow by a subsequent call to SetTerminationProtection in which you set the value to false .
    For more information, see`Managing Cluster Termination`_ in the Amazon EMR Management Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.set_termination_protection(
        JobFlowIds=[
            'string',
        ],
        TerminationProtected=True|False
    )
    
    
    :type JobFlowIds: list
    :param JobFlowIds: [REQUIRED]
            A list of strings that uniquely identify the clusters to protect. This identifier is returned by RunJobFlow and can also be obtained from DescribeJobFlows .
            (string) --
            

    :type TerminationProtected: boolean
    :param TerminationProtected: [REQUIRED]
            A Boolean that indicates whether to protect the cluster and prevent the Amazon EC2 instances in the cluster from shutting down due to API calls, user intervention, or job-flow error.
            

    """
    pass

def set_visible_to_all_users(JobFlowIds=None, VisibleToAllUsers=None):
    """
    Sets whether all AWS Identity and Access Management (IAM) users under your account can access the specified clusters (job flows). This action works on running clusters. You can also set the visibility of a cluster when you launch it using the VisibleToAllUsers parameter of  RunJobFlow . The SetVisibleToAllUsers action can be called only by an IAM user who created the cluster or the AWS account that owns the cluster.
    See also: AWS API Documentation
    
    
    :example: response = client.set_visible_to_all_users(
        JobFlowIds=[
            'string',
        ],
        VisibleToAllUsers=True|False
    )
    
    
    :type JobFlowIds: list
    :param JobFlowIds: [REQUIRED]
            Identifiers of the job flows to receive the new visibility setting.
            (string) --
            

    :type VisibleToAllUsers: boolean
    :param VisibleToAllUsers: [REQUIRED]
            Whether the specified clusters are visible to all IAM users of the AWS account associated with the cluster. If this value is set to True, all IAM users of that AWS account can view and, if they have the proper IAM policy permissions set, manage the clusters. If it is set to False, only the IAM user that created a cluster can view and manage it.
            

    """
    pass

def terminate_job_flows(JobFlowIds=None):
    """
    TerminateJobFlows shuts a list of clusters (job flows) down. When a job flow is shut down, any step not yet completed is canceled and the EC2 instances on which the cluster is running are stopped. Any log files not already saved are uploaded to Amazon S3 if a LogUri was specified when the cluster was created.
    The maximum number of clusters allowed is 10. The call to TerminateJobFlows is asynchronous. Depending on the configuration of the cluster, it may take up to 1-5 minutes for the cluster to completely terminate and release allocated resources, such as Amazon EC2 instances.
    See also: AWS API Documentation
    
    
    :example: response = client.terminate_job_flows(
        JobFlowIds=[
            'string',
        ]
    )
    
    
    :type JobFlowIds: list
    :param JobFlowIds: [REQUIRED]
            A list of job flows to be shutdown.
            (string) --
            

    """
    pass

