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
    
    Exceptions
    
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
    :param ClusterId: [REQUIRED]\nThe unique identifier of the cluster.\n

    :type InstanceFleet: dict
    :param InstanceFleet: [REQUIRED]\nSpecifies the configuration of the instance fleet.\n\nName (string) --The friendly name of the instance fleet.\n\nInstanceFleetType (string) -- [REQUIRED]The node type that the instance fleet hosts. Valid values are MASTER,CORE,and TASK.\n\nTargetOnDemandCapacity (integer) --The target capacity of On-Demand units for the instance fleet, which determines how many On-Demand instances to provision. When the instance fleet launches, Amazon EMR tries to provision On-Demand instances as specified by InstanceTypeConfig . Each instance configuration has a specified WeightedCapacity . When an On-Demand instance is provisioned, the WeightedCapacity units count toward the target capacity. Amazon EMR provisions instances until the target capacity is totally fulfilled, even if this results in an overage. For example, if there are 2 units remaining to fulfill capacity, and Amazon EMR can only provision an instance with a WeightedCapacity of 5 units, the instance is provisioned, and the target capacity is exceeded by 3 units.\n\nNote\nIf not specified or set to 0, only Spot instances are provisioned for the instance fleet using TargetSpotCapacity . At least one of TargetSpotCapacity and TargetOnDemandCapacity should be greater than 0. For a master instance fleet, only one of TargetSpotCapacity and TargetOnDemandCapacity can be specified, and its value must be 1.\n\n\nTargetSpotCapacity (integer) --The target capacity of Spot units for the instance fleet, which determines how many Spot instances to provision. When the instance fleet launches, Amazon EMR tries to provision Spot instances as specified by InstanceTypeConfig . Each instance configuration has a specified WeightedCapacity . When a Spot instance is provisioned, the WeightedCapacity units count toward the target capacity. Amazon EMR provisions instances until the target capacity is totally fulfilled, even if this results in an overage. For example, if there are 2 units remaining to fulfill capacity, and Amazon EMR can only provision an instance with a WeightedCapacity of 5 units, the instance is provisioned, and the target capacity is exceeded by 3 units.\n\nNote\nIf not specified or set to 0, only On-Demand instances are provisioned for the instance fleet. At least one of TargetSpotCapacity and TargetOnDemandCapacity should be greater than 0. For a master instance fleet, only one of TargetSpotCapacity and TargetOnDemandCapacity can be specified, and its value must be 1.\n\n\nInstanceTypeConfigs (list) --The instance type configurations that define the EC2 instances in the instance fleet.\n\n(dict) --An instance type configuration for each instance type in an instance fleet, which determines the EC2 instances Amazon EMR attempts to provision to fulfill On-Demand and Spot target capacities. There can be a maximum of 5 instance type configurations in a fleet.\n\nNote\nThe instance fleet configuration is available only in Amazon EMR versions 4.8.0 and later, excluding 5.0.x versions.\n\n\nInstanceType (string) -- [REQUIRED]An EC2 instance type, such as m3.xlarge .\n\nWeightedCapacity (integer) --The number of units that a provisioned instance of this type provides toward fulfilling the target capacities defined in InstanceFleetConfig . This value is 1 for a master instance fleet, and must be 1 or greater for core and task instance fleets. Defaults to 1 if not specified.\n\nBidPrice (string) --The bid price for each EC2 Spot instance type as defined by InstanceType . Expressed in USD. If neither BidPrice nor BidPriceAsPercentageOfOnDemandPrice is provided, BidPriceAsPercentageOfOnDemandPrice defaults to 100%.\n\nBidPriceAsPercentageOfOnDemandPrice (float) --The bid price, as a percentage of On-Demand price, for each EC2 Spot instance as defined by InstanceType . Expressed as a number (for example, 20 specifies 20%). If neither BidPrice nor BidPriceAsPercentageOfOnDemandPrice is provided, BidPriceAsPercentageOfOnDemandPrice defaults to 100%.\n\nEbsConfiguration (dict) --The configuration of Amazon Elastic Block Storage (EBS) attached to each instance as defined by InstanceType .\n\nEbsBlockDeviceConfigs (list) --An array of Amazon EBS volume specifications attached to a cluster instance.\n\n(dict) --Configuration of requested EBS block device associated with the instance group with count of volumes that will be associated to every instance.\n\nVolumeSpecification (dict) -- [REQUIRED]EBS volume specifications such as volume type, IOPS, and size (GiB) that will be requested for the EBS volume attached to an EC2 instance in the cluster.\n\nVolumeType (string) -- [REQUIRED]The volume type. Volume types supported are gp2, io1, standard.\n\nIops (integer) --The number of I/O operations per second (IOPS) that the volume supports.\n\nSizeInGB (integer) -- [REQUIRED]The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the volume type is EBS-optimized, the minimum value is 10.\n\n\n\nVolumesPerInstance (integer) --Number of EBS volumes with a specific volume configuration that will be associated with every instance in the instance group\n\n\n\n\n\nEbsOptimized (boolean) --Indicates whether an Amazon EBS volume is EBS-optimized.\n\n\n\nConfigurations (list) --A configuration classification that applies when provisioning cluster instances, which can include configurations for applications and software that run on the cluster.\n\n(dict) --\nNote\nAmazon EMR releases 4.x or later.\n\nAn optional configuration specification to be used when provisioning cluster instances, which can include configurations for applications and software bundled with Amazon EMR. A configuration consists of a classification, properties, and optional nested configurations. A classification refers to an application-specific configuration file. Properties are the settings you want to change in that file. For more information, see Configuring Applications .\n\nClassification (string) --The classification within a configuration.\n\nConfigurations (list) --A list of additional configurations to apply within a configuration object.\n\nProperties (dict) --A set of properties specified within a configuration classification.\n\n(string) --\n(string) --\n\n\n\n\n\n\n\n\n\n\n\n\nLaunchSpecifications (dict) --The launch specification for the instance fleet.\n\nSpotSpecification (dict) -- [REQUIRED]The launch specification for Spot instances in the fleet, which determines the defined duration and provisioning timeout behavior.\n\nTimeoutDurationMinutes (integer) -- [REQUIRED]The spot provisioning timeout period in minutes. If Spot instances are not provisioned within this time period, the TimeOutAction is taken. Minimum value is 5 and maximum value is 1440. The timeout applies only during initial provisioning, when the cluster is first created.\n\nTimeoutAction (string) -- [REQUIRED]The action to take when TargetSpotCapacity has not been fulfilled when the TimeoutDurationMinutes has expired; that is, when all Spot instances could not be provisioned within the Spot provisioning timeout. Valid values are TERMINATE_CLUSTER and SWITCH_TO_ON_DEMAND . SWITCH_TO_ON_DEMAND specifies that if no Spot instances are available, On-Demand Instances should be provisioned to fulfill any remaining Spot capacity.\n\nBlockDurationMinutes (integer) --The defined duration for Spot instances (also known as Spot blocks) in minutes. When specified, the Spot instance does not terminate before the defined duration expires, and defined duration pricing for Spot instances applies. Valid values are 60, 120, 180, 240, 300, or 360. The duration period starts as soon as a Spot instance receives its instance ID. At the end of the duration, Amazon EC2 marks the Spot instance for termination and provides a Spot instance termination notice, which gives the instance a two-minute warning before it terminates.\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ClusterId': 'string',
    'InstanceFleetId': 'string',
    'ClusterArn': 'string'
}


Response Structure

(dict) --

ClusterId (string) --
The unique identifier of the cluster.

InstanceFleetId (string) --
The unique identifier of the instance fleet.

ClusterArn (string) --
The Amazon Resource Name of the cluster.







Exceptions

EMR.Client.exceptions.InternalServerException
EMR.Client.exceptions.InvalidRequestException


    :return: {
        'ClusterId': 'string',
        'InstanceFleetId': 'string',
        'ClusterArn': 'string'
    }
    
    
    :returns: 
    EMR.Client.exceptions.InternalServerException
    EMR.Client.exceptions.InvalidRequestException
    
    """
    pass

def add_instance_groups(InstanceGroups=None, JobFlowId=None):
    """
    Adds one or more instance groups to a running cluster.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param InstanceGroups: [REQUIRED]\nInstance groups to add.\n\n(dict) --Configuration defining a new instance group.\n\nName (string) --Friendly name given to the instance group.\n\nMarket (string) --Market type of the EC2 instances used to create a cluster node.\n\nInstanceRole (string) -- [REQUIRED]The role of the instance group in the cluster.\n\nBidPrice (string) --The bid price for each EC2 Spot instance type as defined by InstanceType . Expressed in USD. If neither BidPrice nor BidPriceAsPercentageOfOnDemandPrice is provided, BidPriceAsPercentageOfOnDemandPrice defaults to 100%.\n\nInstanceType (string) -- [REQUIRED]The EC2 instance type for all instances in the instance group.\n\nInstanceCount (integer) -- [REQUIRED]Target number of instances for the instance group.\n\nConfigurations (list) --\nNote\nAmazon EMR releases 4.x or later.\n\nThe list of configurations supplied for an EMR cluster instance group. You can specify a separate configuration for each instance group (master, core, and task).\n\n(dict) --\nNote\nAmazon EMR releases 4.x or later.\n\nAn optional configuration specification to be used when provisioning cluster instances, which can include configurations for applications and software bundled with Amazon EMR. A configuration consists of a classification, properties, and optional nested configurations. A classification refers to an application-specific configuration file. Properties are the settings you want to change in that file. For more information, see Configuring Applications .\n\nClassification (string) --The classification within a configuration.\n\nConfigurations (list) --A list of additional configurations to apply within a configuration object.\n\nProperties (dict) --A set of properties specified within a configuration classification.\n\n(string) --\n(string) --\n\n\n\n\n\n\n\n\nEbsConfiguration (dict) --EBS configurations that will be attached to each EC2 instance in the instance group.\n\nEbsBlockDeviceConfigs (list) --An array of Amazon EBS volume specifications attached to a cluster instance.\n\n(dict) --Configuration of requested EBS block device associated with the instance group with count of volumes that will be associated to every instance.\n\nVolumeSpecification (dict) -- [REQUIRED]EBS volume specifications such as volume type, IOPS, and size (GiB) that will be requested for the EBS volume attached to an EC2 instance in the cluster.\n\nVolumeType (string) -- [REQUIRED]The volume type. Volume types supported are gp2, io1, standard.\n\nIops (integer) --The number of I/O operations per second (IOPS) that the volume supports.\n\nSizeInGB (integer) -- [REQUIRED]The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the volume type is EBS-optimized, the minimum value is 10.\n\n\n\nVolumesPerInstance (integer) --Number of EBS volumes with a specific volume configuration that will be associated with every instance in the instance group\n\n\n\n\n\nEbsOptimized (boolean) --Indicates whether an Amazon EBS volume is EBS-optimized.\n\n\n\nAutoScalingPolicy (dict) --An automatic scaling policy for a core instance group or task instance group in an Amazon EMR cluster. The automatic scaling policy defines how an instance group dynamically adds and terminates EC2 instances in response to the value of a CloudWatch metric. See PutAutoScalingPolicy .\n\nConstraints (dict) -- [REQUIRED]The upper and lower EC2 instance limits for an automatic scaling policy. Automatic scaling activity will not cause an instance group to grow above or below these limits.\n\nMinCapacity (integer) -- [REQUIRED]The lower boundary of EC2 instances in an instance group below which scaling activities are not allowed to shrink. Scale-in activities will not terminate instances below this boundary.\n\nMaxCapacity (integer) -- [REQUIRED]The upper boundary of EC2 instances in an instance group beyond which scaling activities are not allowed to grow. Scale-out activities will not add instances beyond this boundary.\n\n\n\nRules (list) -- [REQUIRED]The scale-in and scale-out rules that comprise the automatic scaling policy.\n\n(dict) --A scale-in or scale-out rule that defines scaling activity, including the CloudWatch metric alarm that triggers activity, how EC2 instances are added or removed, and the periodicity of adjustments. The automatic scaling policy for an instance group can comprise one or more automatic scaling rules.\n\nName (string) -- [REQUIRED]The name used to identify an automatic scaling rule. Rule names must be unique within a scaling policy.\n\nDescription (string) --A friendly, more verbose description of the automatic scaling rule.\n\nAction (dict) -- [REQUIRED]The conditions that trigger an automatic scaling activity.\n\nMarket (string) --Not available for instance groups. Instance groups use the market type specified for the group.\n\nSimpleScalingPolicyConfiguration (dict) -- [REQUIRED]The type of adjustment the automatic scaling activity makes when triggered, and the periodicity of the adjustment.\n\nAdjustmentType (string) --The way in which EC2 instances are added (if ScalingAdjustment is a positive number) or terminated (if ScalingAdjustment is a negative number) each time the scaling activity is triggered. CHANGE_IN_CAPACITY is the default. CHANGE_IN_CAPACITY indicates that the EC2 instance count increments or decrements by ScalingAdjustment , which should be expressed as an integer. PERCENT_CHANGE_IN_CAPACITY indicates the instance count increments or decrements by the percentage specified by ScalingAdjustment , which should be expressed as an integer. For example, 20 indicates an increase in 20% increments of cluster capacity. EXACT_CAPACITY indicates the scaling activity results in an instance group with the number of EC2 instances specified by ScalingAdjustment , which should be expressed as a positive integer.\n\nScalingAdjustment (integer) -- [REQUIRED]The amount by which to scale in or scale out, based on the specified AdjustmentType . A positive value adds to the instance group\'s EC2 instance count while a negative number removes instances. If AdjustmentType is set to EXACT_CAPACITY , the number should only be a positive integer. If AdjustmentType is set to PERCENT_CHANGE_IN_CAPACITY , the value should express the percentage as an integer. For example, -20 indicates a decrease in 20% increments of cluster capacity.\n\nCoolDown (integer) --The amount of time, in seconds, after a scaling activity completes before any further trigger-related scaling activities can start. The default value is 0.\n\n\n\n\n\nTrigger (dict) -- [REQUIRED]The CloudWatch alarm definition that determines when automatic scaling activity is triggered.\n\nCloudWatchAlarmDefinition (dict) -- [REQUIRED]The definition of a CloudWatch metric alarm. When the defined alarm conditions are met along with other trigger parameters, scaling activity begins.\n\nComparisonOperator (string) -- [REQUIRED]Determines how the metric specified by MetricName is compared to the value specified by Threshold .\n\nEvaluationPeriods (integer) --The number of periods, in five-minute increments, during which the alarm condition must exist before the alarm triggers automatic scaling activity. The default value is 1 .\n\nMetricName (string) -- [REQUIRED]The name of the CloudWatch metric that is watched to determine an alarm condition.\n\nNamespace (string) --The namespace for the CloudWatch metric. The default is AWS/ElasticMapReduce .\n\nPeriod (integer) -- [REQUIRED]The period, in seconds, over which the statistic is applied. EMR CloudWatch metrics are emitted every five minutes (300 seconds), so if an EMR CloudWatch metric is specified, specify 300 .\n\nStatistic (string) --The statistic to apply to the metric associated with the alarm. The default is AVERAGE .\n\nThreshold (float) -- [REQUIRED]The value against which the specified statistic is compared.\n\nUnit (string) --The unit of measure associated with the CloudWatch metric being watched. The value specified for Unit must correspond to the units specified in the CloudWatch metric.\n\nDimensions (list) --A CloudWatch metric dimension.\n\n(dict) --A CloudWatch dimension, which is specified using a Key (known as a Name in CloudWatch), Value pair. By default, Amazon EMR uses one dimension whose Key is JobFlowID and Value is a variable representing the cluster ID, which is ${emr.clusterId} . This enables the rule to bootstrap when the cluster ID becomes available.\n\nKey (string) --The dimension name.\n\nValue (string) --The dimension value.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n

    :type JobFlowId: string
    :param JobFlowId: [REQUIRED]\nJob flow in which to add the instance groups.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'JobFlowId': 'string',
    'InstanceGroupIds': [
        'string',
    ],
    'ClusterArn': 'string'
}


Response Structure

(dict) --
Output from an AddInstanceGroups call.

JobFlowId (string) --
The job flow ID in which the instance groups are added.

InstanceGroupIds (list) --
Instance group IDs of the newly created instance groups.

(string) --


ClusterArn (string) --
The Amazon Resource Name of the cluster.







Exceptions

EMR.Client.exceptions.InternalServerError


    :return: {
        'JobFlowId': 'string',
        'InstanceGroupIds': [
            'string',
        ],
        'ClusterArn': 'string'
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
    
    Exceptions
    
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
    :param JobFlowId: [REQUIRED]\nA string that uniquely identifies the job flow. This identifier is returned by RunJobFlow and can also be obtained from ListClusters .\n

    :type Steps: list
    :param Steps: [REQUIRED]\nA list of StepConfig to be executed by the job flow.\n\n(dict) --Specification of a cluster (job flow) step.\n\nName (string) -- [REQUIRED]The name of the step.\n\nActionOnFailure (string) --The action to take when the cluster step fails. Possible values are TERMINATE_CLUSTER, CANCEL_AND_WAIT, and CONTINUE. TERMINATE_JOB_FLOW is provided for backward compatibility. We recommend using TERMINATE_CLUSTER instead.\n\nHadoopJarStep (dict) -- [REQUIRED]The JAR file used for the step.\n\nProperties (list) --A list of Java properties that are set when the step runs. You can use these properties to pass key value pairs to your main function.\n\n(dict) --A key value pair.\n\nKey (string) --The unique identifier of a key value pair.\n\nValue (string) --The value part of the identified key.\n\n\n\n\n\nJar (string) -- [REQUIRED]A path to a JAR file run during the step.\n\nMainClass (string) --The name of the main class in the specified Java file. If not specified, the JAR file should specify a Main-Class in its manifest file.\n\nArgs (list) --A list of command line arguments passed to the JAR file\'s main function when executed.\n\n(string) --\n\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'StepIds': [
        'string',
    ]
}


Response Structure

(dict) --
The output for the  AddJobFlowSteps operation.

StepIds (list) --
The identifiers of the list of steps added to the job flow.

(string) --








Exceptions

EMR.Client.exceptions.InternalServerError


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
    Adds tags to an Amazon EMR resource. Tags make it easier to associate clusters in various ways, such as grouping clusters to track your Amazon EMR resource allocation costs. For more information, see Tag Clusters .
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param ResourceId: [REQUIRED]\nThe Amazon EMR resource identifier to which tags will be added. This value must be a cluster identifier.\n

    :type Tags: list
    :param Tags: [REQUIRED]\nA list of tags to associate with a cluster and propagate to EC2 instances. Tags are user-defined key/value pairs that consist of a required key string with a maximum of 128 characters, and an optional value string with a maximum of 256 characters.\n\n(dict) --A key/value pair containing user-defined metadata that you can associate with an Amazon EMR resource. Tags make it easier to associate clusters in various ways, such as grouping clusters to track your Amazon EMR resource allocation costs. For more information, see Tag Clusters .\n\nKey (string) --A user-defined key, which is the minimum required information for a valid tag. For more information, see Tag .\n\nValue (string) --A user-defined value, which is optional in a tag. For more information, see Tag Clusters .\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
This output indicates the result of adding tags to a resource.





Exceptions

EMR.Client.exceptions.InternalServerException
EMR.Client.exceptions.InvalidRequestException


    :return: {}
    
    
    :returns: 
    EMR.Client.exceptions.InternalServerException
    EMR.Client.exceptions.InvalidRequestException
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def cancel_steps(ClusterId=None, StepIds=None, StepCancellationOption=None):
    """
    Cancels a pending step or steps in a running cluster. Available only in Amazon EMR versions 4.8.0 and later, excluding version 5.0.0. A maximum of 256 steps are allowed in each CancelSteps request. CancelSteps is idempotent but asynchronous; it does not guarantee a step will be canceled, even if the request is successfully submitted. You can only cancel steps that are in a PENDING state.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.cancel_steps(
        ClusterId='string',
        StepIds=[
            'string',
        ],
        StepCancellationOption='SEND_INTERRUPT'|'TERMINATE_PROCESS'
    )
    
    
    :type ClusterId: string
    :param ClusterId: [REQUIRED]\nThe ClusterID for which specified steps will be canceled. Use RunJobFlow and ListClusters to get ClusterIDs.\n

    :type StepIds: list
    :param StepIds: [REQUIRED]\nThe list of StepIDs to cancel. Use ListSteps to get steps and their states for the specified cluster.\n\n(string) --\n\n

    :type StepCancellationOption: string
    :param StepCancellationOption: The option to choose for cancelling RUNNING steps. By default, the value is SEND_INTERRUPT .

    :rtype: dict

ReturnsResponse Syntax
{
    'CancelStepsInfoList': [
        {
            'StepId': 'string',
            'Status': 'SUBMITTED'|'FAILED',
            'Reason': 'string'
        },
    ]
}


Response Structure

(dict) --
The output for the  CancelSteps operation.

CancelStepsInfoList (list) --
A list of  CancelStepsInfo , which shows the status of specified cancel requests for each StepID specified.

(dict) --
Specification of the status of a CancelSteps request. Available only in Amazon EMR version 4.8.0 and later, excluding version 5.0.0.

StepId (string) --
The encrypted StepId of a step.

Status (string) --
The status of a CancelSteps Request. The value may be SUBMITTED or FAILED.

Reason (string) --
The reason for the failure if the CancelSteps request fails.











Exceptions

EMR.Client.exceptions.InternalServerError
EMR.Client.exceptions.InvalidRequestException


    :return: {
        'CancelStepsInfoList': [
            {
                'StepId': 'string',
                'Status': 'SUBMITTED'|'FAILED',
                'Reason': 'string'
            },
        ]
    }
    
    
    :returns: 
    EMR.Client.exceptions.InternalServerError
    EMR.Client.exceptions.InvalidRequestException
    
    """
    pass

def create_security_configuration(Name=None, SecurityConfiguration=None):
    """
    Creates a security configuration, which is stored in the service and can be specified when a cluster is created.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_security_configuration(
        Name='string',
        SecurityConfiguration='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the security configuration.\n

    :type SecurityConfiguration: string
    :param SecurityConfiguration: [REQUIRED]\nThe security configuration details in JSON format. For JSON parameters and examples, see Use Security Configurations to Set Up Cluster Security in the Amazon EMR Management Guide .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Name': 'string',
    'CreationDateTime': datetime(2015, 1, 1)
}


Response Structure

(dict) --

Name (string) --
The name of the security configuration.

CreationDateTime (datetime) --
The date and time the security configuration was created.







Exceptions

EMR.Client.exceptions.InternalServerException
EMR.Client.exceptions.InvalidRequestException


    :return: {
        'Name': 'string',
        'CreationDateTime': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    EMR.Client.exceptions.InternalServerException
    EMR.Client.exceptions.InvalidRequestException
    
    """
    pass

def delete_security_configuration(Name=None):
    """
    Deletes a security configuration.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_security_configuration(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the security configuration.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

EMR.Client.exceptions.InternalServerException
EMR.Client.exceptions.InvalidRequestException


    :return: {}
    
    
    :returns: 
    EMR.Client.exceptions.InternalServerException
    EMR.Client.exceptions.InvalidRequestException
    
    """
    pass

def describe_cluster(ClusterId=None):
    """
    Provides cluster-level details including status, hardware and software configuration, VPC settings, and so on.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_cluster(
        ClusterId='string'
    )
    
    
    :type ClusterId: string
    :param ClusterId: [REQUIRED]\nThe identifier of the cluster to describe.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Cluster': {
        'Id': 'string',
        'Name': 'string',
        'Status': {
            'State': 'STARTING'|'BOOTSTRAPPING'|'RUNNING'|'WAITING'|'TERMINATING'|'TERMINATED'|'TERMINATED_WITH_ERRORS',
            'StateChangeReason': {
                'Code': 'INTERNAL_ERROR'|'VALIDATION_ERROR'|'INSTANCE_FAILURE'|'INSTANCE_FLEET_TIMEOUT'|'BOOTSTRAP_FAILURE'|'USER_REQUEST'|'STEP_FAILURE'|'ALL_STEPS_COMPLETED',
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
        'ScaleDownBehavior': 'TERMINATE_AT_INSTANCE_HOUR'|'TERMINATE_AT_TASK_COMPLETION',
        'CustomAmiId': 'string',
        'EbsRootVolumeSize': 123,
        'RepoUpgradeOnBoot': 'SECURITY'|'NONE',
        'KerberosAttributes': {
            'Realm': 'string',
            'KdcAdminPassword': 'string',
            'CrossRealmTrustPrincipalPassword': 'string',
            'ADDomainJoinUser': 'string',
            'ADDomainJoinPassword': 'string'
        },
        'ClusterArn': 'string',
        'OutpostArn': 'string',
        'StepConcurrencyLevel': 123
    }
}


Response Structure

(dict) --This output contains the description of the cluster.

Cluster (dict) --This output contains the details for the requested cluster.

Id (string) --The unique identifier for the cluster.

Name (string) --The name of the cluster.

Status (dict) --The current status details about the cluster.

State (string) --The current state of the cluster.

StateChangeReason (dict) --The reason for the cluster status change.

Code (string) --The programmatic code for the state change reason.

Message (string) --The descriptive message for the state change reason.



Timeline (dict) --A timeline that represents the status of a cluster over the lifetime of the cluster.

CreationDateTime (datetime) --The creation date and time of the cluster.

ReadyDateTime (datetime) --The date and time when the cluster was ready to execute steps.

EndDateTime (datetime) --The date and time when the cluster was terminated.





Ec2InstanceAttributes (dict) --Provides information about the EC2 instances in a cluster grouped by category. For example, key name, subnet ID, IAM instance profile, and so on.

Ec2KeyName (string) --The name of the Amazon EC2 key pair to use when connecting with SSH into the master node as a user named "hadoop".

Ec2SubnetId (string) --Set this parameter to the identifier of the Amazon VPC subnet where you want the cluster to launch. If you do not specify this value, and your account supports EC2-Classic, the cluster launches in EC2-Classic.

RequestedEc2SubnetIds (list) --Applies to clusters configured with the instance fleets option. Specifies the unique identifier of one or more Amazon EC2 subnets in which to launch EC2 cluster instances. Subnets must exist within the same VPC. Amazon EMR chooses the EC2 subnet with the best fit from among the list of RequestedEc2SubnetIds , and then launches all cluster instances within that Subnet. If this value is not specified, and the account and Region support EC2-Classic networks, the cluster launches instances in the EC2-Classic network and uses RequestedEc2AvailabilityZones instead of this setting. If EC2-Classic is not supported, and no Subnet is specified, Amazon EMR chooses the subnet for you. RequestedEc2SubnetIDs and RequestedEc2AvailabilityZones cannot be specified together.

(string) --


Ec2AvailabilityZone (string) --The Availability Zone in which the cluster will run.

RequestedEc2AvailabilityZones (list) --Applies to clusters configured with the instance fleets option. Specifies one or more Availability Zones in which to launch EC2 cluster instances when the EC2-Classic network configuration is supported. Amazon EMR chooses the Availability Zone with the best fit from among the list of RequestedEc2AvailabilityZones , and then launches all cluster instances within that Availability Zone. If you do not specify this value, Amazon EMR chooses the Availability Zone for you. RequestedEc2SubnetIDs and RequestedEc2AvailabilityZones cannot be specified together.

(string) --


IamInstanceProfile (string) --The IAM role that was specified when the cluster was launched. The EC2 instances of the cluster assume this role.

EmrManagedMasterSecurityGroup (string) --The identifier of the Amazon EC2 security group for the master node.

EmrManagedSlaveSecurityGroup (string) --The identifier of the Amazon EC2 security group for the core and task nodes.

ServiceAccessSecurityGroup (string) --The identifier of the Amazon EC2 security group for the Amazon EMR service to access clusters in VPC private subnets.

AdditionalMasterSecurityGroups (list) --A list of additional Amazon EC2 security group IDs for the master node.

(string) --


AdditionalSlaveSecurityGroups (list) --A list of additional Amazon EC2 security group IDs for the core and task nodes.

(string) --




InstanceCollectionType (string) --
Note
The instance fleet configuration is available only in Amazon EMR versions 4.8.0 and later, excluding 5.0.x versions.

The instance group configuration of the cluster. A value of INSTANCE_GROUP indicates a uniform instance group configuration. A value of INSTANCE_FLEET indicates an instance fleets configuration.

LogUri (string) --The path to the Amazon S3 location where logs for this cluster are stored.

RequestedAmiVersion (string) --The AMI version requested for this cluster.

RunningAmiVersion (string) --The AMI version running on this cluster.

ReleaseLabel (string) --The Amazon EMR release label, which determines the version of open-source application packages installed on the cluster. Release labels are in the form emr-x.x.x , where x.x.x is an Amazon EMR release version such as emr-5.14.0 . For more information about Amazon EMR release versions and included application versions and features, see https://docs.aws.amazon.com/emr/latest/ReleaseGuide/ . The release label applies only to Amazon EMR releases version 4.0 and later. Earlier versions use AmiVersion .

AutoTerminate (boolean) --Specifies whether the cluster should terminate after completing all steps.

TerminationProtected (boolean) --Indicates whether Amazon EMR will lock the cluster to prevent the EC2 instances from being terminated by an API call or user intervention, or in the event of a cluster error.

VisibleToAllUsers (boolean) --Indicates whether the cluster is visible to all IAM users of the AWS account associated with the cluster. The default value, true , indicates that all IAM users in the AWS account can perform cluster actions if they have the proper IAM policy permissions. If this value is false , only the IAM user that created the cluster can perform actions. This value can be changed on a running cluster by using the  SetVisibleToAllUsers action. You can override the default value of true when you create a cluster by using the VisibleToAllUsers parameter of the RunJobFlow action.

Applications (list) --The applications installed on this cluster.

(dict) --With Amazon EMR release version 4.0 and later, the only accepted parameter is the application name. To pass arguments to applications, you use configuration classifications specified using configuration JSON objects. For more information, see Configuring Applications .
With earlier Amazon EMR releases, the application is any Amazon or third-party software that you can add to the cluster. This structure contains a list of strings that indicates the software to use with the cluster and accepts a user argument list. Amazon EMR accepts and forwards the argument list to the corresponding installation script as bootstrap action argument.

Name (string) --The name of the application.

Version (string) --The version of the application.

Args (list) --Arguments for Amazon EMR to pass to the application.

(string) --


AdditionalInfo (dict) --This option is for advanced users only. This is meta information about third-party applications that third-party vendors use for testing purposes.

(string) --
(string) --








Tags (list) --A list of tags associated with a cluster.

(dict) --A key/value pair containing user-defined metadata that you can associate with an Amazon EMR resource. Tags make it easier to associate clusters in various ways, such as grouping clusters to track your Amazon EMR resource allocation costs. For more information, see Tag Clusters .

Key (string) --A user-defined key, which is the minimum required information for a valid tag. For more information, see Tag .

Value (string) --A user-defined value, which is optional in a tag. For more information, see Tag Clusters .





ServiceRole (string) --The IAM role that will be assumed by the Amazon EMR service to access AWS resources on your behalf.

NormalizedInstanceHours (integer) --An approximation of the cost of the cluster, represented in m1.small/hours. This value is incremented one time for every hour an m1.small instance runs. Larger instances are weighted more, so an EC2 instance that is roughly four times more expensive would result in the normalized instance hours being incremented by four. This result is only an approximation and does not reflect the actual billing rate.

MasterPublicDnsName (string) --The DNS name of the master node. If the cluster is on a private subnet, this is the private DNS name. On a public subnet, this is the public DNS name.

Configurations (list) --Applies only to Amazon EMR releases 4.x and later. The list of Configurations supplied to the EMR cluster.

(dict) --
Note
Amazon EMR releases 4.x or later.

An optional configuration specification to be used when provisioning cluster instances, which can include configurations for applications and software bundled with Amazon EMR. A configuration consists of a classification, properties, and optional nested configurations. A classification refers to an application-specific configuration file. Properties are the settings you want to change in that file. For more information, see Configuring Applications .

Classification (string) --The classification within a configuration.

Configurations (list) --A list of additional configurations to apply within a configuration object.

Properties (dict) --A set of properties specified within a configuration classification.

(string) --
(string) --








SecurityConfiguration (string) --The name of the security configuration applied to the cluster.

AutoScalingRole (string) --An IAM role for automatic scaling policies. The default role is EMR_AutoScaling_DefaultRole . The IAM role provides permissions that the automatic scaling feature requires to launch and terminate EC2 instances in an instance group.

ScaleDownBehavior (string) --The way that individual Amazon EC2 instances terminate when an automatic scale-in activity occurs or an instance group is resized. TERMINATE_AT_INSTANCE_HOUR indicates that Amazon EMR terminates nodes at the instance-hour boundary, regardless of when the request to terminate the instance was submitted. This option is only available with Amazon EMR 5.1.0 and later and is the default for clusters created using that version. TERMINATE_AT_TASK_COMPLETION indicates that Amazon EMR blacklists and drains tasks from nodes before terminating the Amazon EC2 instances, regardless of the instance-hour boundary. With either behavior, Amazon EMR removes the least active nodes first and blocks instance termination if it could lead to HDFS corruption. TERMINATE_AT_TASK_COMPLETION is available only in Amazon EMR version 4.1.0 and later, and is the default for versions of Amazon EMR earlier than 5.1.0.

CustomAmiId (string) --Available only in Amazon EMR version 5.7.0 and later. The ID of a custom Amazon EBS-backed Linux AMI if the cluster uses a custom AMI.

EbsRootVolumeSize (integer) --The size, in GiB, of the EBS root device volume of the Linux AMI that is used for each EC2 instance. Available in Amazon EMR version 4.x and later.

RepoUpgradeOnBoot (string) --Applies only when CustomAmiID is used. Specifies the type of updates that are applied from the Amazon Linux AMI package repositories when an instance boots using the AMI.

KerberosAttributes (dict) --Attributes for Kerberos configuration when Kerberos authentication is enabled using a security configuration. For more information see Use Kerberos Authentication in the EMR Management Guide .

Realm (string) --The name of the Kerberos realm to which all nodes in a cluster belong. For example, EC2.INTERNAL .

KdcAdminPassword (string) --The password used within the cluster for the kadmin service on the cluster-dedicated KDC, which maintains Kerberos principals, password policies, and keytabs for the cluster.

CrossRealmTrustPrincipalPassword (string) --Required only when establishing a cross-realm trust with a KDC in a different realm. The cross-realm principal password, which must be identical across realms.

ADDomainJoinUser (string) --Required only when establishing a cross-realm trust with an Active Directory domain. A user with sufficient privileges to join resources to the domain.

ADDomainJoinPassword (string) --The Active Directory password for ADDomainJoinUser .



ClusterArn (string) --The Amazon Resource Name of the cluster.

OutpostArn (string) --The Amazon Resource Name (ARN) of the Outpost where the cluster is launched.

StepConcurrencyLevel (integer) --Specifies the number of steps that can be executed concurrently.








Exceptions

EMR.Client.exceptions.InternalServerException
EMR.Client.exceptions.InvalidRequestException


    :return: {
        'Cluster': {
            'Id': 'string',
            'Name': 'string',
            'Status': {
                'State': 'STARTING'|'BOOTSTRAPPING'|'RUNNING'|'WAITING'|'TERMINATING'|'TERMINATED'|'TERMINATED_WITH_ERRORS',
                'StateChangeReason': {
                    'Code': 'INTERNAL_ERROR'|'VALIDATION_ERROR'|'INSTANCE_FAILURE'|'INSTANCE_FLEET_TIMEOUT'|'BOOTSTRAP_FAILURE'|'USER_REQUEST'|'STEP_FAILURE'|'ALL_STEPS_COMPLETED',
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
            'ScaleDownBehavior': 'TERMINATE_AT_INSTANCE_HOUR'|'TERMINATE_AT_TASK_COMPLETION',
            'CustomAmiId': 'string',
            'EbsRootVolumeSize': 123,
            'RepoUpgradeOnBoot': 'SECURITY'|'NONE',
            'KerberosAttributes': {
                'Realm': 'string',
                'KdcAdminPassword': 'string',
                'CrossRealmTrustPrincipalPassword': 'string',
                'ADDomainJoinUser': 'string',
                'ADDomainJoinPassword': 'string'
            },
            'ClusterArn': 'string',
            'OutpostArn': 'string',
            'StepConcurrencyLevel': 123
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
    
    Exceptions
    
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
    :param JobFlowIds: Return only job flows whose job flow ID is contained in this list.\n\n(string) --\n\n

    :type JobFlowStates: list
    :param JobFlowStates: Return only job flows whose state is contained in this list.\n\n(string) --The type of instance.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
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
                        'State': 'PROVISIONING'|'BOOTSTRAPPING'|'RUNNING'|'RECONFIGURING'|'RESIZING'|'SUSPENDED'|'TERMINATING'|'TERMINATED'|'ARRESTED'|'SHUTTING_DOWN'|'ENDED',
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


Response Structure

(dict) --
The output for the  DescribeJobFlows operation.

JobFlows (list) --
A list of job flows matching the parameters supplied.

(dict) --
A description of a cluster (job flow).

JobFlowId (string) --
The job flow identifier.

Name (string) --
The name of the job flow.

LogUri (string) --
The location in Amazon S3 where log files for the job are stored.

AmiVersion (string) --
Applies only to Amazon EMR AMI versions 3.x and 2.x. For Amazon EMR releases 4.0 and later, ReleaseLabel is used. To specify a custom AMI, use CustomAmiID .

ExecutionStatusDetail (dict) --
Describes the execution status of the job flow.

State (string) --
The state of the job flow.

CreationDateTime (datetime) --
The creation date and time of the job flow.

StartDateTime (datetime) --
The start date and time of the job flow.

ReadyDateTime (datetime) --
The date and time when the job flow was ready to start running bootstrap actions.

EndDateTime (datetime) --
The completion date and time of the job flow.

LastStateChangeReason (string) --
Description of the job flow last changed state.



Instances (dict) --
Describes the Amazon EC2 instances of the job flow.

MasterInstanceType (string) --
The Amazon EC2 master node instance type.

MasterPublicDnsName (string) --
The DNS name of the master node. If the cluster is on a private subnet, this is the private DNS name. On a public subnet, this is the public DNS name.

MasterInstanceId (string) --
The Amazon EC2 instance identifier of the master node.

SlaveInstanceType (string) --
The Amazon EC2 core and task node instance type.

InstanceCount (integer) --
The number of Amazon EC2 instances in the cluster. If the value is 1, the same instance serves as both the master and core and task node. If the value is greater than 1, one instance is the master node and all others are core and task nodes.

InstanceGroups (list) --
Details about the instance groups in a cluster.

(dict) --
Detailed information about an instance group.

InstanceGroupId (string) --
Unique identifier for the instance group.

Name (string) --
Friendly name for the instance group.

Market (string) --
Market type of the EC2 instances used to create a cluster node.

InstanceRole (string) --
Instance group role in the cluster

BidPrice (string) --
The bid price for each EC2 Spot instance type as defined by InstanceType . Expressed in USD. If neither BidPrice nor BidPriceAsPercentageOfOnDemandPrice is provided, BidPriceAsPercentageOfOnDemandPrice defaults to 100%.

InstanceType (string) --
EC2 instance type.

InstanceRequestCount (integer) --
Target number of instances to run in the instance group.

InstanceRunningCount (integer) --
Actual count of running instances.

State (string) --
State of instance group. The following values are deprecated: STARTING, TERMINATED, and FAILED.

LastStateChangeReason (string) --
Details regarding the state of the instance group.

CreationDateTime (datetime) --
The date/time the instance group was created.

StartDateTime (datetime) --
The date/time the instance group was started.

ReadyDateTime (datetime) --
The date/time the instance group was available to the cluster.

EndDateTime (datetime) --
The date/time the instance group was terminated.





NormalizedInstanceHours (integer) --
An approximation of the cost of the cluster, represented in m1.small/hours. This value is incremented one time for every hour that an m1.small runs. Larger instances are weighted more, so an Amazon EC2 instance that is roughly four times more expensive would result in the normalized instance hours being incremented by four. This result is only an approximation and does not reflect the actual billing rate.

Ec2KeyName (string) --
The name of an Amazon EC2 key pair that can be used to ssh to the master node.

Ec2SubnetId (string) --
For clusters launched within Amazon Virtual Private Cloud, this is the identifier of the subnet where the cluster was launched.

Placement (dict) --
The Amazon EC2 Availability Zone for the cluster.

AvailabilityZone (string) --
The Amazon EC2 Availability Zone for the cluster. AvailabilityZone is used for uniform instance groups, while AvailabilityZones (plural) is used for instance fleets.

AvailabilityZones (list) --
When multiple Availability Zones are specified, Amazon EMR evaluates them and launches instances in the optimal Availability Zone. AvailabilityZones is used for instance fleets, while AvailabilityZone (singular) is used for uniform instance groups.

Note
The instance fleet configuration is available only in Amazon EMR versions 4.8.0 and later, excluding 5.0.x versions.


(string) --




KeepJobFlowAliveWhenNoSteps (boolean) --
Specifies whether the cluster should remain available after completing all steps.

TerminationProtected (boolean) --
Specifies whether the Amazon EC2 instances in the cluster are protected from termination by API calls, user intervention, or in the event of a job-flow error.

HadoopVersion (string) --
The Hadoop version for the cluster.



Steps (list) --
A list of steps run by the job flow.

(dict) --
Combines the execution state and configuration of a step.

StepConfig (dict) --
The step configuration.

Name (string) --
The name of the step.

ActionOnFailure (string) --
The action to take when the cluster step fails. Possible values are TERMINATE_CLUSTER, CANCEL_AND_WAIT, and CONTINUE. TERMINATE_JOB_FLOW is provided for backward compatibility. We recommend using TERMINATE_CLUSTER instead.

HadoopJarStep (dict) --
The JAR file used for the step.

Properties (list) --
A list of Java properties that are set when the step runs. You can use these properties to pass key value pairs to your main function.

(dict) --
A key value pair.

Key (string) --
The unique identifier of a key value pair.

Value (string) --
The value part of the identified key.





Jar (string) --
A path to a JAR file run during the step.

MainClass (string) --
The name of the main class in the specified Java file. If not specified, the JAR file should specify a Main-Class in its manifest file.

Args (list) --
A list of command line arguments passed to the JAR file\'s main function when executed.

(string) --






ExecutionStatusDetail (dict) --
The description of the step status.

State (string) --
The state of the step.

CreationDateTime (datetime) --
The creation date and time of the step.

StartDateTime (datetime) --
The start date and time of the step.

EndDateTime (datetime) --
The completion date and time of the step.

LastStateChangeReason (string) --
A description of the step\'s current state.







BootstrapActions (list) --
A list of the bootstrap actions run by the job flow.

(dict) --
Reports the configuration of a bootstrap action in a cluster (job flow).

BootstrapActionConfig (dict) --
A description of the bootstrap action.

Name (string) --
The name of the bootstrap action.

ScriptBootstrapAction (dict) --
The script run by the bootstrap action.

Path (string) --
Location of the script to run during a bootstrap action. Can be either a location in Amazon S3 or on a local file system.

Args (list) --
A list of command line arguments to pass to the bootstrap action script.

(string) --










SupportedProducts (list) --
A list of strings set by third party software when the job flow is launched. If you are not using third party software to manage the job flow this value is empty.

(string) --


VisibleToAllUsers (boolean) --
Indicates whether the cluster is visible to all IAM users of the AWS account associated with the cluster. The default value, true , indicates that all IAM users in the AWS account can perform cluster actions if they have the proper IAM policy permissions. If this value is false , only the IAM user that created the cluster can perform actions. This value can be changed on a running cluster by using the  SetVisibleToAllUsers action. You can override the default value of true when you create a cluster by using the VisibleToAllUsers parameter of the RunJobFlow action.

JobFlowRole (string) --
The IAM role that was specified when the job flow was launched. The EC2 instances of the job flow assume this role.

ServiceRole (string) --
The IAM role that will be assumed by the Amazon EMR service to access AWS resources on your behalf.

AutoScalingRole (string) --
An IAM role for automatic scaling policies. The default role is EMR_AutoScaling_DefaultRole . The IAM role provides a way for the automatic scaling feature to get the required permissions it needs to launch and terminate EC2 instances in an instance group.

ScaleDownBehavior (string) --
The way that individual Amazon EC2 instances terminate when an automatic scale-in activity occurs or an instance group is resized. TERMINATE_AT_INSTANCE_HOUR indicates that Amazon EMR terminates nodes at the instance-hour boundary, regardless of when the request to terminate the instance was submitted. This option is only available with Amazon EMR 5.1.0 and later and is the default for clusters created using that version. TERMINATE_AT_TASK_COMPLETION indicates that Amazon EMR blacklists and drains tasks from nodes before terminating the Amazon EC2 instances, regardless of the instance-hour boundary. With either behavior, Amazon EMR removes the least active nodes first and blocks instance termination if it could lead to HDFS corruption. TERMINATE_AT_TASK_COMPLETION available only in Amazon EMR version 4.1.0 and later, and is the default for versions of Amazon EMR earlier than 5.1.0.











Exceptions

EMR.Client.exceptions.InternalServerError


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
                            'State': 'PROVISIONING'|'BOOTSTRAPPING'|'RUNNING'|'RECONFIGURING'|'RESIZING'|'SUSPENDED'|'TERMINATING'|'TERMINATED'|'ARRESTED'|'SHUTTING_DOWN'|'ENDED',
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
    
    Exceptions
    
    :example: response = client.describe_security_configuration(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the security configuration.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Name': 'string',
    'SecurityConfiguration': 'string',
    'CreationDateTime': datetime(2015, 1, 1)
}


Response Structure

(dict) --
Name (string) --The name of the security configuration.

SecurityConfiguration (string) --The security configuration details in JSON format.

CreationDateTime (datetime) --The date and time the security configuration was created






Exceptions

EMR.Client.exceptions.InternalServerException
EMR.Client.exceptions.InvalidRequestException


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
    
    Exceptions
    
    :example: response = client.describe_step(
        ClusterId='string',
        StepId='string'
    )
    
    
    :type ClusterId: string
    :param ClusterId: [REQUIRED]\nThe identifier of the cluster with steps to describe.\n

    :type StepId: string
    :param StepId: [REQUIRED]\nThe identifier of the step to describe.\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --
This output contains the description of the cluster step.

Step (dict) --
The step details for the requested step identifier.

Id (string) --
The identifier of the cluster step.

Name (string) --
The name of the cluster step.

Config (dict) --
The Hadoop job configuration of the cluster step.

Jar (string) --
The path to the JAR file that runs during the step.

Properties (dict) --
The list of Java properties that are set when the step runs. You can use these properties to pass key value pairs to your main function.

(string) --
(string) --




MainClass (string) --
The name of the main class in the specified Java file. If not specified, the JAR file should specify a main class in its manifest file.

Args (list) --
The list of command line arguments to pass to the JAR file\'s main function for execution.

(string) --




ActionOnFailure (string) --
The action to take when the cluster step fails. Possible values are TERMINATE_CLUSTER, CANCEL_AND_WAIT, and CONTINUE. TERMINATE_JOB_FLOW is provided for backward compatibility. We recommend using TERMINATE_CLUSTER instead.

Status (dict) --
The current execution status details of the cluster step.

State (string) --
The execution state of the cluster step.

StateChangeReason (dict) --
The reason for the step execution status change.

Code (string) --
The programmable code for the state change reason. Note: Currently, the service provides no code for the state change.

Message (string) --
The descriptive message for the state change reason.



FailureDetails (dict) --
The details for the step failure including reason, message, and log file path where the root cause was identified.

Reason (string) --
The reason for the step failure. In the case where the service cannot successfully determine the root cause of the failure, it returns "Unknown Error" as a reason.

Message (string) --
The descriptive message including the error the EMR service has identified as the cause of step failure. This is text from an error log that describes the root cause of the failure.

LogFile (string) --
The path to the log file where the step failure root cause was originally recorded.



Timeline (dict) --
The timeline of the cluster step status over time.

CreationDateTime (datetime) --
The date and time when the cluster step was created.

StartDateTime (datetime) --
The date and time when the cluster step execution started.

EndDateTime (datetime) --
The date and time when the cluster step execution completed or failed.













Exceptions

EMR.Client.exceptions.InternalServerException
EMR.Client.exceptions.InvalidRequestException


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
    :param Params: The parameters normally passed to\nClientMethod.

    :type ExpiresIn: int
    :param ExpiresIn: The number of seconds the presigned url is valid\nfor. By default it expires in an hour (3600 seconds)

    :type HttpMethod: string
    :param HttpMethod: The http method to use on the generated url. By\ndefault, the http method is whatever is used in the method\'s model.

    """
    pass

def get_block_public_access_configuration():
    """
    Returns the Amazon EMR block public access configuration for your AWS account in the current Region. For more information see Configure Block Public Access for Amazon EMR in the Amazon EMR Management Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_block_public_access_configuration()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'BlockPublicAccessConfiguration': {
        'BlockPublicSecurityGroupRules': True|False,
        'PermittedPublicSecurityGroupRuleRanges': [
            {
                'MinRange': 123,
                'MaxRange': 123
            },
        ]
    },
    'BlockPublicAccessConfigurationMetadata': {
        'CreationDateTime': datetime(2015, 1, 1),
        'CreatedByArn': 'string'
    }
}


Response Structure

(dict) --
BlockPublicAccessConfiguration (dict) --A configuration for Amazon EMR block public access. The configuration applies to all clusters created in your account for the current Region. The configuration specifies whether block public access is enabled. If block public access is enabled, security groups associated with the cluster cannot have rules that allow inbound traffic from 0.0.0.0/0 or ::/0 on a port, unless the port is specified as an exception using PermittedPublicSecurityGroupRuleRanges in the BlockPublicAccessConfiguration . By default, Port 22 (SSH) is an exception, and public access is allowed on this port. You can change this by updating the block public access configuration to remove the exception.

Note
For accounts that created clusters in a Region before November 25, 2019, block public access is disabled by default in that Region. To use this feature, you must manually enable and configure it. For accounts that did not create an EMR cluster in a Region before this date, block public access is enabled by default in that Region.


BlockPublicSecurityGroupRules (boolean) --Indicates whether EMR block public access is enabled (true ) or disabled (false ). By default, the value is false for accounts that have created EMR clusters before July 2019. For accounts created after this, the default is true .

PermittedPublicSecurityGroupRuleRanges (list) --Specifies ports and port ranges that are permitted to have security group rules that allow inbound traffic from all public sources. For example, if Port 23 (Telnet) is specified for PermittedPublicSecurityGroupRuleRanges , Amazon EMR allows cluster creation if a security group associated with the cluster has a rule that allows inbound traffic on Port 23 from IPv4 0.0.0.0/0 or IPv6 port ::/0 as the source.
By default, Port 22, which is used for SSH access to the cluster EC2 instances, is in the list of PermittedPublicSecurityGroupRuleRanges .

(dict) --A list of port ranges that are permitted to allow inbound traffic from all public IP addresses. To specify a single port, use the same value for MinRange and MaxRange .

MinRange (integer) --The smallest port number in a specified range of port numbers.

MaxRange (integer) --The smallest port number in a specified range of port numbers.







BlockPublicAccessConfigurationMetadata (dict) --Properties that describe the AWS principal that created the BlockPublicAccessConfiguration using the PutBlockPublicAccessConfiguration action as well as the date and time that the configuration was created. Each time a configuration for block public access is updated, Amazon EMR updates this metadata.

CreationDateTime (datetime) --The date and time that the configuration was created.

CreatedByArn (string) --The Amazon Resource Name that created or last modified the configuration.








Exceptions

EMR.Client.exceptions.InternalServerException
EMR.Client.exceptions.InvalidRequestException


    :return: {
        'BlockPublicAccessConfiguration': {
            'BlockPublicSecurityGroupRules': True|False,
            'PermittedPublicSecurityGroupRuleRanges': [
                {
                    'MinRange': 123,
                    'MaxRange': 123
                },
            ]
        },
        'BlockPublicAccessConfigurationMetadata': {
            'CreationDateTime': datetime(2015, 1, 1),
            'CreatedByArn': 'string'
        }
    }
    
    
    """
    pass

def get_managed_scaling_policy(ClusterId=None):
    """
    Fetches the attached managed scaling policy for an Amazon EMR cluster.
    See also: AWS API Documentation
    
    
    :example: response = client.get_managed_scaling_policy(
        ClusterId='string'
    )
    
    
    :type ClusterId: string
    :param ClusterId: [REQUIRED]\nSpecifies the ID of the cluster for which the managed scaling policy will be fetched.\n

    :rtype: dict
ReturnsResponse Syntax{
    'ManagedScalingPolicy': {
        'ComputeLimits': {
            'UnitType': 'InstanceFleetUnits'|'Instances'|'VCPU',
            'MinimumCapacityUnits': 123,
            'MaximumCapacityUnits': 123,
            'MaximumOnDemandCapacityUnits': 123
        }
    }
}


Response Structure

(dict) --
ManagedScalingPolicy (dict) --Specifies the managed scaling policy that is attached to an Amazon EMR cluster.

ComputeLimits (dict) --The EC2 unit limits for a managed scaling policy. The managed scaling activity of a cluster is not allowed to go above or below these limits. The limit only applies to the core and task nodes. The master node cannot be scaled after initial configuration.

UnitType (string) --The unit type used for specifying a managed scaling policy.

MinimumCapacityUnits (integer) --The lower boundary of EC2 units. It is measured through VCPU cores or instances for instance groups and measured through units for instance fleets. Managed scaling activities are not allowed beyond this boundary. The limit only applies to the core and task nodes. The master node cannot be scaled after initial configuration.

MaximumCapacityUnits (integer) --The upper boundary of EC2 units. It is measured through VCPU cores or instances for instance groups and measured through units for instance fleets. Managed scaling activities are not allowed beyond this boundary. The limit only applies to the core and task nodes. The master node cannot be scaled after initial configuration.

MaximumOnDemandCapacityUnits (integer) --The upper boundary of on-demand EC2 units. It is measured through VCPU cores or instances for instance groups and measured through units for instance fleets. The on-demand units are not allowed to scale beyond this boundary. The limit only applies to the core and task nodes. The master node cannot be scaled after initial configuration.











    :return: {
        'ManagedScalingPolicy': {
            'ComputeLimits': {
                'UnitType': 'InstanceFleetUnits'|'Instances'|'VCPU',
                'MinimumCapacityUnits': 123,
                'MaximumCapacityUnits': 123,
                'MaximumOnDemandCapacityUnits': 123
            }
        }
    }
    
    
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

def list_bootstrap_actions(ClusterId=None, Marker=None):
    """
    Provides information about the bootstrap actions associated with a cluster.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_bootstrap_actions(
        ClusterId='string',
        Marker='string'
    )
    
    
    :type ClusterId: string
    :param ClusterId: [REQUIRED]\nThe cluster identifier for the bootstrap actions to list.\n

    :type Marker: string
    :param Marker: The pagination token that indicates the next set of results to retrieve.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --
This output contains the bootstrap actions detail.

BootstrapActions (list) --
The bootstrap actions associated with the cluster.

(dict) --
An entity describing an executable that runs on a cluster.

Name (string) --
The name of the command.

ScriptPath (string) --
The Amazon S3 location of the command script.

Args (list) --
Arguments for Amazon EMR to pass to the command for execution.

(string) --






Marker (string) --
The pagination token that indicates the next set of results to retrieve.







Exceptions

EMR.Client.exceptions.InternalServerException
EMR.Client.exceptions.InvalidRequestException


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
    
    Exceptions
    
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
    :param ClusterStates: The cluster state filters to apply when listing clusters.\n\n(string) --\n\n

    :type Marker: string
    :param Marker: The pagination token that indicates the next set of results to retrieve.

    :rtype: dict

ReturnsResponse Syntax
{
    'Clusters': [
        {
            'Id': 'string',
            'Name': 'string',
            'Status': {
                'State': 'STARTING'|'BOOTSTRAPPING'|'RUNNING'|'WAITING'|'TERMINATING'|'TERMINATED'|'TERMINATED_WITH_ERRORS',
                'StateChangeReason': {
                    'Code': 'INTERNAL_ERROR'|'VALIDATION_ERROR'|'INSTANCE_FAILURE'|'INSTANCE_FLEET_TIMEOUT'|'BOOTSTRAP_FAILURE'|'USER_REQUEST'|'STEP_FAILURE'|'ALL_STEPS_COMPLETED',
                    'Message': 'string'
                },
                'Timeline': {
                    'CreationDateTime': datetime(2015, 1, 1),
                    'ReadyDateTime': datetime(2015, 1, 1),
                    'EndDateTime': datetime(2015, 1, 1)
                }
            },
            'NormalizedInstanceHours': 123,
            'ClusterArn': 'string',
            'OutpostArn': 'string'
        },
    ],
    'Marker': 'string'
}


Response Structure

(dict) --
This contains a ClusterSummaryList with the cluster details; for example, the cluster IDs, names, and status.

Clusters (list) --
The list of clusters for the account based on the given filters.

(dict) --
The summary description of the cluster.

Id (string) --
The unique identifier for the cluster.

Name (string) --
The name of the cluster.

Status (dict) --
The details about the current status of the cluster.

State (string) --
The current state of the cluster.

StateChangeReason (dict) --
The reason for the cluster status change.

Code (string) --
The programmatic code for the state change reason.

Message (string) --
The descriptive message for the state change reason.



Timeline (dict) --
A timeline that represents the status of a cluster over the lifetime of the cluster.

CreationDateTime (datetime) --
The creation date and time of the cluster.

ReadyDateTime (datetime) --
The date and time when the cluster was ready to execute steps.

EndDateTime (datetime) --
The date and time when the cluster was terminated.





NormalizedInstanceHours (integer) --
An approximation of the cost of the cluster, represented in m1.small/hours. This value is incremented one time for every hour an m1.small instance runs. Larger instances are weighted more, so an EC2 instance that is roughly four times more expensive would result in the normalized instance hours being incremented by four. This result is only an approximation and does not reflect the actual billing rate.

ClusterArn (string) --
The Amazon Resource Name of the cluster.

OutpostArn (string) --
The Amazon Resource Name (ARN) of the Outpost where the cluster is launched.





Marker (string) --
The pagination token that indicates the next set of results to retrieve.







Exceptions

EMR.Client.exceptions.InternalServerException
EMR.Client.exceptions.InvalidRequestException


    :return: {
        'Clusters': [
            {
                'Id': 'string',
                'Name': 'string',
                'Status': {
                    'State': 'STARTING'|'BOOTSTRAPPING'|'RUNNING'|'WAITING'|'TERMINATING'|'TERMINATED'|'TERMINATED_WITH_ERRORS',
                    'StateChangeReason': {
                        'Code': 'INTERNAL_ERROR'|'VALIDATION_ERROR'|'INSTANCE_FAILURE'|'INSTANCE_FLEET_TIMEOUT'|'BOOTSTRAP_FAILURE'|'USER_REQUEST'|'STEP_FAILURE'|'ALL_STEPS_COMPLETED',
                        'Message': 'string'
                    },
                    'Timeline': {
                        'CreationDateTime': datetime(2015, 1, 1),
                        'ReadyDateTime': datetime(2015, 1, 1),
                        'EndDateTime': datetime(2015, 1, 1)
                    }
                },
                'NormalizedInstanceHours': 123,
                'ClusterArn': 'string',
                'OutpostArn': 'string'
            },
        ],
        'Marker': 'string'
    }
    
    
    :returns: 
    EMR.Client.exceptions.InternalServerException
    EMR.Client.exceptions.InvalidRequestException
    
    """
    pass

def list_instance_fleets(ClusterId=None, Marker=None):
    """
    Lists all available details about the instance fleets in a cluster.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_instance_fleets(
        ClusterId='string',
        Marker='string'
    )
    
    
    :type ClusterId: string
    :param ClusterId: [REQUIRED]\nThe unique identifier of the cluster.\n

    :type Marker: string
    :param Marker: The pagination token that indicates the next set of results to retrieve.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

InstanceFleets (list) --
The list of instance fleets for the cluster and given filters.

(dict) --
Describes an instance fleet, which is a group of EC2 instances that host a particular node type (master, core, or task) in an Amazon EMR cluster. Instance fleets can consist of a mix of instance types and On-Demand and Spot instances, which are provisioned to meet a defined target capacity.

Note
The instance fleet configuration is available only in Amazon EMR versions 4.8.0 and later, excluding 5.0.x versions.


Id (string) --
The unique identifier of the instance fleet.

Name (string) --
A friendly name for the instance fleet.

Status (dict) --
The current status of the instance fleet.

State (string) --
A code representing the instance fleet status.

PROVISIONING \xe2\x80\x94The instance fleet is provisioning EC2 resources and is not yet ready to run jobs.
BOOTSTRAPPING \xe2\x80\x94EC2 instances and other resources have been provisioned and the bootstrap actions specified for the instances are underway.
RUNNING \xe2\x80\x94EC2 instances and other resources are running. They are either executing jobs or waiting to execute jobs.
RESIZING \xe2\x80\x94A resize operation is underway. EC2 instances are either being added or removed.
SUSPENDED \xe2\x80\x94A resize operation could not complete. Existing EC2 instances are running, but instances can\'t be added or removed.
TERMINATING \xe2\x80\x94The instance fleet is terminating EC2 instances.
TERMINATED \xe2\x80\x94The instance fleet is no longer active, and all EC2 instances have been terminated.


StateChangeReason (dict) --
Provides status change reason details for the instance fleet.

Code (string) --
A code corresponding to the reason the state change occurred.

Message (string) --
An explanatory message.



Timeline (dict) --
Provides historical timestamps for the instance fleet, including the time of creation, the time it became ready to run jobs, and the time of termination.

CreationDateTime (datetime) --
The time and date the instance fleet was created.

ReadyDateTime (datetime) --
The time and date the instance fleet was ready to run jobs.

EndDateTime (datetime) --
The time and date the instance fleet terminated.





InstanceFleetType (string) --
The node type that the instance fleet hosts. Valid values are MASTER, CORE, or TASK.

TargetOnDemandCapacity (integer) --
The target capacity of On-Demand units for the instance fleet, which determines how many On-Demand instances to provision. When the instance fleet launches, Amazon EMR tries to provision On-Demand instances as specified by  InstanceTypeConfig . Each instance configuration has a specified WeightedCapacity . When an On-Demand instance is provisioned, the WeightedCapacity units count toward the target capacity. Amazon EMR provisions instances until the target capacity is totally fulfilled, even if this results in an overage. For example, if there are 2 units remaining to fulfill capacity, and Amazon EMR can only provision an instance with a WeightedCapacity of 5 units, the instance is provisioned, and the target capacity is exceeded by 3 units. You can use  InstanceFleet$ProvisionedOnDemandCapacity to determine the Spot capacity units that have been provisioned for the instance fleet.

Note
If not specified or set to 0, only Spot instances are provisioned for the instance fleet using TargetSpotCapacity . At least one of TargetSpotCapacity and TargetOnDemandCapacity should be greater than 0. For a master instance fleet, only one of TargetSpotCapacity and TargetOnDemandCapacity can be specified, and its value must be 1.


TargetSpotCapacity (integer) --
The target capacity of Spot units for the instance fleet, which determines how many Spot instances to provision. When the instance fleet launches, Amazon EMR tries to provision Spot instances as specified by  InstanceTypeConfig . Each instance configuration has a specified WeightedCapacity . When a Spot instance is provisioned, the WeightedCapacity units count toward the target capacity. Amazon EMR provisions instances until the target capacity is totally fulfilled, even if this results in an overage. For example, if there are 2 units remaining to fulfill capacity, and Amazon EMR can only provision an instance with a WeightedCapacity of 5 units, the instance is provisioned, and the target capacity is exceeded by 3 units. You can use  InstanceFleet$ProvisionedSpotCapacity to determine the Spot capacity units that have been provisioned for the instance fleet.

Note
If not specified or set to 0, only On-Demand instances are provisioned for the instance fleet. At least one of TargetSpotCapacity and TargetOnDemandCapacity should be greater than 0. For a master instance fleet, only one of TargetSpotCapacity and TargetOnDemandCapacity can be specified, and its value must be 1.


ProvisionedOnDemandCapacity (integer) --
The number of On-Demand units that have been provisioned for the instance fleet to fulfill TargetOnDemandCapacity . This provisioned capacity might be less than or greater than TargetOnDemandCapacity .

ProvisionedSpotCapacity (integer) --
The number of Spot units that have been provisioned for this instance fleet to fulfill TargetSpotCapacity . This provisioned capacity might be less than or greater than TargetSpotCapacity .

InstanceTypeSpecifications (list) --
The specification for the instance types that comprise an instance fleet. Up to five unique instance specifications may be defined for each instance fleet.

(dict) --
The configuration specification for each instance type in an instance fleet.

Note
The instance fleet configuration is available only in Amazon EMR versions 4.8.0 and later, excluding 5.0.x versions.


InstanceType (string) --
The EC2 instance type, for example m3.xlarge .

WeightedCapacity (integer) --
The number of units that a provisioned instance of this type provides toward fulfilling the target capacities defined in  InstanceFleetConfig . Capacity values represent performance characteristics such as vCPUs, memory, or I/O. If not specified, the default value is 1.

BidPrice (string) --
The bid price for each EC2 Spot instance type as defined by InstanceType . Expressed in USD.

BidPriceAsPercentageOfOnDemandPrice (float) --
The bid price, as a percentage of On-Demand price, for each EC2 Spot instance as defined by InstanceType . Expressed as a number (for example, 20 specifies 20%).

Configurations (list) --
A configuration classification that applies when provisioning cluster instances, which can include configurations for applications and software bundled with Amazon EMR.

(dict) --

Note
Amazon EMR releases 4.x or later.

An optional configuration specification to be used when provisioning cluster instances, which can include configurations for applications and software bundled with Amazon EMR. A configuration consists of a classification, properties, and optional nested configurations. A classification refers to an application-specific configuration file. Properties are the settings you want to change in that file. For more information, see Configuring Applications .

Classification (string) --
The classification within a configuration.

Configurations (list) --
A list of additional configurations to apply within a configuration object.

Properties (dict) --
A set of properties specified within a configuration classification.

(string) --
(string) --








EbsBlockDevices (list) --
The configuration of Amazon Elastic Block Storage (EBS) attached to each instance as defined by InstanceType .

(dict) --
Configuration of requested EBS block device associated with the instance group.

VolumeSpecification (dict) --
EBS volume specifications such as volume type, IOPS, and size (GiB) that will be requested for the EBS volume attached to an EC2 instance in the cluster.

VolumeType (string) --
The volume type. Volume types supported are gp2, io1, standard.

Iops (integer) --
The number of I/O operations per second (IOPS) that the volume supports.

SizeInGB (integer) --
The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the volume type is EBS-optimized, the minimum value is 10.



Device (string) --
The device name that is exposed to the instance, such as /dev/sdh.





EbsOptimized (boolean) --
Evaluates to TRUE when the specified InstanceType is EBS-optimized.





LaunchSpecifications (dict) --
Describes the launch specification for an instance fleet.

SpotSpecification (dict) --
The launch specification for Spot instances in the fleet, which determines the defined duration and provisioning timeout behavior.

TimeoutDurationMinutes (integer) --
The spot provisioning timeout period in minutes. If Spot instances are not provisioned within this time period, the TimeOutAction is taken. Minimum value is 5 and maximum value is 1440. The timeout applies only during initial provisioning, when the cluster is first created.

TimeoutAction (string) --
The action to take when TargetSpotCapacity has not been fulfilled when the TimeoutDurationMinutes has expired; that is, when all Spot instances could not be provisioned within the Spot provisioning timeout. Valid values are TERMINATE_CLUSTER and SWITCH_TO_ON_DEMAND . SWITCH_TO_ON_DEMAND specifies that if no Spot instances are available, On-Demand Instances should be provisioned to fulfill any remaining Spot capacity.

BlockDurationMinutes (integer) --
The defined duration for Spot instances (also known as Spot blocks) in minutes. When specified, the Spot instance does not terminate before the defined duration expires, and defined duration pricing for Spot instances applies. Valid values are 60, 120, 180, 240, 300, or 360. The duration period starts as soon as a Spot instance receives its instance ID. At the end of the duration, Amazon EC2 marks the Spot instance for termination and provides a Spot instance termination notice, which gives the instance a two-minute warning before it terminates.









Marker (string) --
The pagination token that indicates the next set of results to retrieve.







Exceptions

EMR.Client.exceptions.InternalServerException
EMR.Client.exceptions.InvalidRequestException


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
    PROVISIONING \xe2\x80\x94The instance fleet is provisioning EC2 resources and is not yet ready to run jobs.
    BOOTSTRAPPING \xe2\x80\x94EC2 instances and other resources have been provisioned and the bootstrap actions specified for the instances are underway.
    RUNNING \xe2\x80\x94EC2 instances and other resources are running. They are either executing jobs or waiting to execute jobs.
    RESIZING \xe2\x80\x94A resize operation is underway. EC2 instances are either being added or removed.
    SUSPENDED \xe2\x80\x94A resize operation could not complete. Existing EC2 instances are running, but instances can\'t be added or removed.
    TERMINATING \xe2\x80\x94The instance fleet is terminating EC2 instances.
    TERMINATED \xe2\x80\x94The instance fleet is no longer active, and all EC2 instances have been terminated.
    
    """
    pass

def list_instance_groups(ClusterId=None, Marker=None):
    """
    Provides all available details about the instance groups in a cluster.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_instance_groups(
        ClusterId='string',
        Marker='string'
    )
    
    
    :type ClusterId: string
    :param ClusterId: [REQUIRED]\nThe identifier of the cluster for which to list the instance groups.\n

    :type Marker: string
    :param Marker: The pagination token that indicates the next set of results to retrieve.

    :rtype: dict

ReturnsResponse Syntax
{
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
                'State': 'PROVISIONING'|'BOOTSTRAPPING'|'RUNNING'|'RECONFIGURING'|'RESIZING'|'SUSPENDED'|'TERMINATING'|'TERMINATED'|'ARRESTED'|'SHUTTING_DOWN'|'ENDED',
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
            'ConfigurationsVersion': 123,
            'LastSuccessfullyAppliedConfigurations': [
                {
                    'Classification': 'string',
                    'Configurations': {'... recursive ...'},
                    'Properties': {
                        'string': 'string'
                    }
                },
            ],
            'LastSuccessfullyAppliedConfigurationsVersion': 123,
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


Response Structure

(dict) --
This input determines which instance groups to retrieve.

InstanceGroups (list) --
The list of instance groups for the cluster and given filters.

(dict) --
This entity represents an instance group, which is a group of instances that have common purpose. For example, CORE instance group is used for HDFS.

Id (string) --
The identifier of the instance group.

Name (string) --
The name of the instance group.

Market (string) --
The marketplace to provision instances for this group. Valid values are ON_DEMAND or SPOT.

InstanceGroupType (string) --
The type of the instance group. Valid values are MASTER, CORE or TASK.

BidPrice (string) --
The bid price for each EC2 Spot instance type as defined by InstanceType . Expressed in USD. If neither BidPrice nor BidPriceAsPercentageOfOnDemandPrice is provided, BidPriceAsPercentageOfOnDemandPrice defaults to 100%.

InstanceType (string) --
The EC2 instance type for all instances in the instance group.

RequestedInstanceCount (integer) --
The target number of instances for the instance group.

RunningInstanceCount (integer) --
The number of instances currently running in this instance group.

Status (dict) --
The current status of the instance group.

State (string) --
The current state of the instance group.

StateChangeReason (dict) --
The status change reason details for the instance group.

Code (string) --
The programmable code for the state change reason.

Message (string) --
The status change reason description.



Timeline (dict) --
The timeline of the instance group status over time.

CreationDateTime (datetime) --
The creation date and time of the instance group.

ReadyDateTime (datetime) --
The date and time when the instance group became ready to perform tasks.

EndDateTime (datetime) --
The date and time when the instance group terminated.





Configurations (list) --

Note
Amazon EMR releases 4.x or later.

The list of configurations supplied for an EMR cluster instance group. You can specify a separate configuration for each instance group (master, core, and task).

(dict) --

Note
Amazon EMR releases 4.x or later.

An optional configuration specification to be used when provisioning cluster instances, which can include configurations for applications and software bundled with Amazon EMR. A configuration consists of a classification, properties, and optional nested configurations. A classification refers to an application-specific configuration file. Properties are the settings you want to change in that file. For more information, see Configuring Applications .

Classification (string) --
The classification within a configuration.

Configurations (list) --
A list of additional configurations to apply within a configuration object.

Properties (dict) --
A set of properties specified within a configuration classification.

(string) --
(string) --








ConfigurationsVersion (integer) --
The version number of the requested configuration specification for this instance group.

LastSuccessfullyAppliedConfigurations (list) --
A list of configurations that were successfully applied for an instance group last time.

(dict) --

Note
Amazon EMR releases 4.x or later.

An optional configuration specification to be used when provisioning cluster instances, which can include configurations for applications and software bundled with Amazon EMR. A configuration consists of a classification, properties, and optional nested configurations. A classification refers to an application-specific configuration file. Properties are the settings you want to change in that file. For more information, see Configuring Applications .

Classification (string) --
The classification within a configuration.

Configurations (list) --
A list of additional configurations to apply within a configuration object.

Properties (dict) --
A set of properties specified within a configuration classification.

(string) --
(string) --








LastSuccessfullyAppliedConfigurationsVersion (integer) --
The version number of a configuration specification that was successfully applied for an instance group last time.

EbsBlockDevices (list) --
The EBS block devices that are mapped to this instance group.

(dict) --
Configuration of requested EBS block device associated with the instance group.

VolumeSpecification (dict) --
EBS volume specifications such as volume type, IOPS, and size (GiB) that will be requested for the EBS volume attached to an EC2 instance in the cluster.

VolumeType (string) --
The volume type. Volume types supported are gp2, io1, standard.

Iops (integer) --
The number of I/O operations per second (IOPS) that the volume supports.

SizeInGB (integer) --
The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the volume type is EBS-optimized, the minimum value is 10.



Device (string) --
The device name that is exposed to the instance, such as /dev/sdh.





EbsOptimized (boolean) --
If the instance group is EBS-optimized. An Amazon EBS-optimized instance uses an optimized configuration stack and provides additional, dedicated capacity for Amazon EBS I/O.

ShrinkPolicy (dict) --
Policy for customizing shrink operations.

DecommissionTimeout (integer) --
The desired timeout for decommissioning an instance. Overrides the default YARN decommissioning timeout.

InstanceResizePolicy (dict) --
Custom policy for requesting termination protection or termination of specific instances when shrinking an instance group.

InstancesToTerminate (list) --
Specific list of instances to be terminated when shrinking an instance group.

(string) --


InstancesToProtect (list) --
Specific list of instances to be protected when shrinking an instance group.

(string) --


InstanceTerminationTimeout (integer) --
Decommissioning timeout override for the specific list of instances to be terminated.





AutoScalingPolicy (dict) --
An automatic scaling policy for a core instance group or task instance group in an Amazon EMR cluster. The automatic scaling policy defines how an instance group dynamically adds and terminates EC2 instances in response to the value of a CloudWatch metric. See PutAutoScalingPolicy.

Status (dict) --
The status of an automatic scaling policy.

State (string) --
Indicates the status of the automatic scaling policy.

StateChangeReason (dict) --
The reason for a change in status.

Code (string) --
The code indicating the reason for the change in status.``USER_REQUEST`` indicates that the scaling policy status was changed by a user. PROVISION_FAILURE indicates that the status change was because the policy failed to provision. CLEANUP_FAILURE indicates an error.

Message (string) --
A friendly, more verbose message that accompanies an automatic scaling policy state change.





Constraints (dict) --
The upper and lower EC2 instance limits for an automatic scaling policy. Automatic scaling activity will not cause an instance group to grow above or below these limits.

MinCapacity (integer) --
The lower boundary of EC2 instances in an instance group below which scaling activities are not allowed to shrink. Scale-in activities will not terminate instances below this boundary.

MaxCapacity (integer) --
The upper boundary of EC2 instances in an instance group beyond which scaling activities are not allowed to grow. Scale-out activities will not add instances beyond this boundary.



Rules (list) --
The scale-in and scale-out rules that comprise the automatic scaling policy.

(dict) --
A scale-in or scale-out rule that defines scaling activity, including the CloudWatch metric alarm that triggers activity, how EC2 instances are added or removed, and the periodicity of adjustments. The automatic scaling policy for an instance group can comprise one or more automatic scaling rules.

Name (string) --
The name used to identify an automatic scaling rule. Rule names must be unique within a scaling policy.

Description (string) --
A friendly, more verbose description of the automatic scaling rule.

Action (dict) --
The conditions that trigger an automatic scaling activity.

Market (string) --
Not available for instance groups. Instance groups use the market type specified for the group.

SimpleScalingPolicyConfiguration (dict) --
The type of adjustment the automatic scaling activity makes when triggered, and the periodicity of the adjustment.

AdjustmentType (string) --
The way in which EC2 instances are added (if ScalingAdjustment is a positive number) or terminated (if ScalingAdjustment is a negative number) each time the scaling activity is triggered. CHANGE_IN_CAPACITY is the default. CHANGE_IN_CAPACITY indicates that the EC2 instance count increments or decrements by ScalingAdjustment , which should be expressed as an integer. PERCENT_CHANGE_IN_CAPACITY indicates the instance count increments or decrements by the percentage specified by ScalingAdjustment , which should be expressed as an integer. For example, 20 indicates an increase in 20% increments of cluster capacity. EXACT_CAPACITY indicates the scaling activity results in an instance group with the number of EC2 instances specified by ScalingAdjustment , which should be expressed as a positive integer.

ScalingAdjustment (integer) --
The amount by which to scale in or scale out, based on the specified AdjustmentType . A positive value adds to the instance group\'s EC2 instance count while a negative number removes instances. If AdjustmentType is set to EXACT_CAPACITY , the number should only be a positive integer. If AdjustmentType is set to PERCENT_CHANGE_IN_CAPACITY , the value should express the percentage as an integer. For example, -20 indicates a decrease in 20% increments of cluster capacity.

CoolDown (integer) --
The amount of time, in seconds, after a scaling activity completes before any further trigger-related scaling activities can start. The default value is 0.





Trigger (dict) --
The CloudWatch alarm definition that determines when automatic scaling activity is triggered.

CloudWatchAlarmDefinition (dict) --
The definition of a CloudWatch metric alarm. When the defined alarm conditions are met along with other trigger parameters, scaling activity begins.

ComparisonOperator (string) --
Determines how the metric specified by MetricName is compared to the value specified by Threshold .

EvaluationPeriods (integer) --
The number of periods, in five-minute increments, during which the alarm condition must exist before the alarm triggers automatic scaling activity. The default value is 1 .

MetricName (string) --
The name of the CloudWatch metric that is watched to determine an alarm condition.

Namespace (string) --
The namespace for the CloudWatch metric. The default is AWS/ElasticMapReduce .

Period (integer) --
The period, in seconds, over which the statistic is applied. EMR CloudWatch metrics are emitted every five minutes (300 seconds), so if an EMR CloudWatch metric is specified, specify 300 .

Statistic (string) --
The statistic to apply to the metric associated with the alarm. The default is AVERAGE .

Threshold (float) --
The value against which the specified statistic is compared.

Unit (string) --
The unit of measure associated with the CloudWatch metric being watched. The value specified for Unit must correspond to the units specified in the CloudWatch metric.

Dimensions (list) --
A CloudWatch metric dimension.

(dict) --
A CloudWatch dimension, which is specified using a Key (known as a Name in CloudWatch), Value pair. By default, Amazon EMR uses one dimension whose Key is JobFlowID and Value is a variable representing the cluster ID, which is ${emr.clusterId} . This enables the rule to bootstrap when the cluster ID becomes available.

Key (string) --
The dimension name.

Value (string) --
The dimension value.



















Marker (string) --
The pagination token that indicates the next set of results to retrieve.







Exceptions

EMR.Client.exceptions.InternalServerException
EMR.Client.exceptions.InvalidRequestException


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
                    'State': 'PROVISIONING'|'BOOTSTRAPPING'|'RUNNING'|'RECONFIGURING'|'RESIZING'|'SUSPENDED'|'TERMINATING'|'TERMINATED'|'ARRESTED'|'SHUTTING_DOWN'|'ENDED',
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
                'ConfigurationsVersion': 123,
                'LastSuccessfullyAppliedConfigurations': [
                    {
                        'Classification': 'string',
                        'Configurations': {'... recursive ...'},
                        'Properties': {
                            'string': 'string'
                        }
                    },
                ],
                'LastSuccessfullyAppliedConfigurationsVersion': 123,
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
    Provides information for all active EC2 instances and EC2 instances terminated in the last 30 days, up to a maximum of 2,000. EC2 instances in any of the following states are considered active: AWAITING_FULFILLMENT, PROVISIONING, BOOTSTRAPPING, RUNNING.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param ClusterId: [REQUIRED]\nThe identifier of the cluster for which to list the instances.\n

    :type InstanceGroupId: string
    :param InstanceGroupId: The identifier of the instance group for which to list the instances.

    :type InstanceGroupTypes: list
    :param InstanceGroupTypes: The type of instance group for which to list the instances.\n\n(string) --\n\n

    :type InstanceFleetId: string
    :param InstanceFleetId: The unique identifier of the instance fleet.

    :type InstanceFleetType: string
    :param InstanceFleetType: The node type of the instance fleet. For example MASTER, CORE, or TASK.

    :type InstanceStates: list
    :param InstanceStates: A list of instance states that will filter the instances returned with this request.\n\n(string) --\n\n

    :type Marker: string
    :param Marker: The pagination token that indicates the next set of results to retrieve.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --
This output contains the list of instances.

Instances (list) --
The list of instances for the cluster and given filters.

(dict) --
Represents an EC2 instance provisioned as part of cluster.

Id (string) --
The unique identifier for the instance in Amazon EMR.

Ec2InstanceId (string) --
The unique identifier of the instance in Amazon EC2.

PublicDnsName (string) --
The public DNS name of the instance.

PublicIpAddress (string) --
The public IP address of the instance.

PrivateDnsName (string) --
The private DNS name of the instance.

PrivateIpAddress (string) --
The private IP address of the instance.

Status (dict) --
The current status of the instance.

State (string) --
The current state of the instance.

StateChangeReason (dict) --
The details of the status change reason for the instance.

Code (string) --
The programmable code for the state change reason.

Message (string) --
The status change reason description.



Timeline (dict) --
The timeline of the instance status over time.

CreationDateTime (datetime) --
The creation date and time of the instance.

ReadyDateTime (datetime) --
The date and time when the instance was ready to perform tasks.

EndDateTime (datetime) --
The date and time when the instance was terminated.





InstanceGroupId (string) --
The identifier of the instance group to which this instance belongs.

InstanceFleetId (string) --
The unique identifier of the instance fleet to which an EC2 instance belongs.

Market (string) --
The instance purchasing option. Valid values are ON_DEMAND or SPOT .

InstanceType (string) --
The EC2 instance type, for example m3.xlarge .

EbsVolumes (list) --
The list of EBS volumes that are attached to this instance.

(dict) --
EBS block device that\'s attached to an EC2 instance.

Device (string) --
The device name that is exposed to the instance, such as /dev/sdh.

VolumeId (string) --
The volume identifier of the EBS volume.









Marker (string) --
The pagination token that indicates the next set of results to retrieve.







Exceptions

EMR.Client.exceptions.InternalServerException
EMR.Client.exceptions.InvalidRequestException


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
    
    
    :returns: 
    EMR.Client.exceptions.InternalServerException
    EMR.Client.exceptions.InvalidRequestException
    
    """
    pass

def list_security_configurations(Marker=None):
    """
    Lists all the security configurations visible to this account, providing their creation dates and times, and their names. This call returns a maximum of 50 clusters per call, but returns a marker to track the paging of the cluster list across multiple ListSecurityConfigurations calls.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_security_configurations(
        Marker='string'
    )
    
    
    :type Marker: string
    :param Marker: The pagination token that indicates the set of results to retrieve.

    :rtype: dict
ReturnsResponse Syntax{
    'SecurityConfigurations': [
        {
            'Name': 'string',
            'CreationDateTime': datetime(2015, 1, 1)
        },
    ],
    'Marker': 'string'
}


Response Structure

(dict) --
SecurityConfigurations (list) --The creation date and time, and name, of each security configuration.

(dict) --The creation date and time, and name, of a security configuration.

Name (string) --The name of the security configuration.

CreationDateTime (datetime) --The date and time the security configuration was created.





Marker (string) --A pagination token that indicates the next set of results to retrieve. Include the marker in the next ListSecurityConfiguration call to retrieve the next page of results, if required.






Exceptions

EMR.Client.exceptions.InternalServerException
EMR.Client.exceptions.InvalidRequestException


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
    Provides a list of steps for the cluster in reverse order unless you specify stepIds with the request of filter by StepStates . You can specify a maximum of ten stepIDs .
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param ClusterId: [REQUIRED]\nThe identifier of the cluster for which to list the steps.\n

    :type StepStates: list
    :param StepStates: The filter to limit the step list based on certain states.\n\n(string) --\n\n

    :type StepIds: list
    :param StepIds: The filter to limit the step list based on the identifier of the steps. You can specify a maximum of ten Step IDs. The character constraint applies to the overall length of the array.\n\n(string) --\n\n

    :type Marker: string
    :param Marker: The pagination token that indicates the next set of results to retrieve.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --
This output contains the list of steps returned in reverse order. This means that the last step is the first element in the list.

Steps (list) --
The filtered list of steps for the cluster.

(dict) --
The summary of the cluster step.

Id (string) --
The identifier of the cluster step.

Name (string) --
The name of the cluster step.

Config (dict) --
The Hadoop job configuration of the cluster step.

Jar (string) --
The path to the JAR file that runs during the step.

Properties (dict) --
The list of Java properties that are set when the step runs. You can use these properties to pass key value pairs to your main function.

(string) --
(string) --




MainClass (string) --
The name of the main class in the specified Java file. If not specified, the JAR file should specify a main class in its manifest file.

Args (list) --
The list of command line arguments to pass to the JAR file\'s main function for execution.

(string) --




ActionOnFailure (string) --
The action to take when the cluster step fails. Possible values are TERMINATE_CLUSTER, CANCEL_AND_WAIT, and CONTINUE. TERMINATE_JOB_FLOW is available for backward compatibility. We recommend using TERMINATE_CLUSTER instead.

Status (dict) --
The current execution status details of the cluster step.

State (string) --
The execution state of the cluster step.

StateChangeReason (dict) --
The reason for the step execution status change.

Code (string) --
The programmable code for the state change reason. Note: Currently, the service provides no code for the state change.

Message (string) --
The descriptive message for the state change reason.



FailureDetails (dict) --
The details for the step failure including reason, message, and log file path where the root cause was identified.

Reason (string) --
The reason for the step failure. In the case where the service cannot successfully determine the root cause of the failure, it returns "Unknown Error" as a reason.

Message (string) --
The descriptive message including the error the EMR service has identified as the cause of step failure. This is text from an error log that describes the root cause of the failure.

LogFile (string) --
The path to the log file where the step failure root cause was originally recorded.



Timeline (dict) --
The timeline of the cluster step status over time.

CreationDateTime (datetime) --
The date and time when the cluster step was created.

StartDateTime (datetime) --
The date and time when the cluster step execution started.

EndDateTime (datetime) --
The date and time when the cluster step execution completed or failed.









Marker (string) --
The pagination token that indicates the next set of results to retrieve.







Exceptions

EMR.Client.exceptions.InternalServerException
EMR.Client.exceptions.InvalidRequestException


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

def modify_cluster(ClusterId=None, StepConcurrencyLevel=None):
    """
    Modifies the number of steps that can be executed concurrently for the cluster specified using ClusterID.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.modify_cluster(
        ClusterId='string',
        StepConcurrencyLevel=123
    )
    
    
    :type ClusterId: string
    :param ClusterId: [REQUIRED]\nThe unique identifier of the cluster.\n

    :type StepConcurrencyLevel: integer
    :param StepConcurrencyLevel: The number of steps that can be executed concurrently. You can specify a maximum of 256 steps.

    :rtype: dict

ReturnsResponse Syntax
{
    'StepConcurrencyLevel': 123
}


Response Structure

(dict) --

StepConcurrencyLevel (integer) --
The number of steps that can be executed concurrently.







Exceptions

EMR.Client.exceptions.InternalServerError
EMR.Client.exceptions.InvalidRequestException


    :return: {
        'StepConcurrencyLevel': 123
    }
    
    
    :returns: 
    EMR.Client.exceptions.InternalServerError
    EMR.Client.exceptions.InvalidRequestException
    
    """
    pass

def modify_instance_fleet(ClusterId=None, InstanceFleet=None):
    """
    Modifies the target On-Demand and target Spot capacities for the instance fleet with the specified InstanceFleetID within the cluster specified using ClusterID. The call either succeeds or fails atomically.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.modify_instance_fleet(
        ClusterId='string',
        InstanceFleet={
            'InstanceFleetId': 'string',
            'TargetOnDemandCapacity': 123,
            'TargetSpotCapacity': 123
        }
    )
    
    
    :type ClusterId: string
    :param ClusterId: [REQUIRED]\nThe unique identifier of the cluster.\n

    :type InstanceFleet: dict
    :param InstanceFleet: [REQUIRED]\nThe unique identifier of the instance fleet.\n\nInstanceFleetId (string) -- [REQUIRED]A unique identifier for the instance fleet.\n\nTargetOnDemandCapacity (integer) --The target capacity of On-Demand units for the instance fleet. For more information see InstanceFleetConfig$TargetOnDemandCapacity .\n\nTargetSpotCapacity (integer) --The target capacity of Spot units for the instance fleet. For more information, see InstanceFleetConfig$TargetSpotCapacity .\n\n\n

    :returns: 
    EMR.Client.exceptions.InternalServerException
    EMR.Client.exceptions.InvalidRequestException
    
    """
    pass

def modify_instance_groups(ClusterId=None, InstanceGroups=None):
    """
    ModifyInstanceGroups modifies the number of nodes and configuration settings of an instance group. The input parameters include the new target instance count for the group and the instance group ID. The call will either succeed or fail atomically.
    See also: AWS API Documentation
    
    Exceptions
    
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
        ]
    )
    
    
    :type ClusterId: string
    :param ClusterId: The ID of the cluster to which the instance group belongs.

    :type InstanceGroups: list
    :param InstanceGroups: Instance groups to change.\n\n(dict) --Modify the size or configurations of an instance group.\n\nInstanceGroupId (string) -- [REQUIRED]Unique ID of the instance group to expand or shrink.\n\nInstanceCount (integer) --Target size for the instance group.\n\nEC2InstanceIdsToTerminate (list) --The EC2 InstanceIds to terminate. After you terminate the instances, the instance group will not return to its original requested size.\n\n(string) --\n\n\nShrinkPolicy (dict) --Policy for customizing shrink operations.\n\nDecommissionTimeout (integer) --The desired timeout for decommissioning an instance. Overrides the default YARN decommissioning timeout.\n\nInstanceResizePolicy (dict) --Custom policy for requesting termination protection or termination of specific instances when shrinking an instance group.\n\nInstancesToTerminate (list) --Specific list of instances to be terminated when shrinking an instance group.\n\n(string) --\n\n\nInstancesToProtect (list) --Specific list of instances to be protected when shrinking an instance group.\n\n(string) --\n\n\nInstanceTerminationTimeout (integer) --Decommissioning timeout override for the specific list of instances to be terminated.\n\n\n\n\n\nConfigurations (list) --A list of new or modified configurations to apply for an instance group.\n\n(dict) --\nNote\nAmazon EMR releases 4.x or later.\n\nAn optional configuration specification to be used when provisioning cluster instances, which can include configurations for applications and software bundled with Amazon EMR. A configuration consists of a classification, properties, and optional nested configurations. A classification refers to an application-specific configuration file. Properties are the settings you want to change in that file. For more information, see Configuring Applications .\n\nClassification (string) --The classification within a configuration.\n\nConfigurations (list) --A list of additional configurations to apply within a configuration object.\n\nProperties (dict) --A set of properties specified within a configuration classification.\n\n(string) --\n(string) --\n\n\n\n\n\n\n\n\n\n\n\n

    :returns: 
    EMR.Client.exceptions.InternalServerError
    
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
    :param ClusterId: [REQUIRED]\nSpecifies the ID of a cluster. The instance group to which the automatic scaling policy is applied is within this cluster.\n

    :type InstanceGroupId: string
    :param InstanceGroupId: [REQUIRED]\nSpecifies the ID of the instance group to which the automatic scaling policy is applied.\n

    :type AutoScalingPolicy: dict
    :param AutoScalingPolicy: [REQUIRED]\nSpecifies the definition of the automatic scaling policy.\n\nConstraints (dict) -- [REQUIRED]The upper and lower EC2 instance limits for an automatic scaling policy. Automatic scaling activity will not cause an instance group to grow above or below these limits.\n\nMinCapacity (integer) -- [REQUIRED]The lower boundary of EC2 instances in an instance group below which scaling activities are not allowed to shrink. Scale-in activities will not terminate instances below this boundary.\n\nMaxCapacity (integer) -- [REQUIRED]The upper boundary of EC2 instances in an instance group beyond which scaling activities are not allowed to grow. Scale-out activities will not add instances beyond this boundary.\n\n\n\nRules (list) -- [REQUIRED]The scale-in and scale-out rules that comprise the automatic scaling policy.\n\n(dict) --A scale-in or scale-out rule that defines scaling activity, including the CloudWatch metric alarm that triggers activity, how EC2 instances are added or removed, and the periodicity of adjustments. The automatic scaling policy for an instance group can comprise one or more automatic scaling rules.\n\nName (string) -- [REQUIRED]The name used to identify an automatic scaling rule. Rule names must be unique within a scaling policy.\n\nDescription (string) --A friendly, more verbose description of the automatic scaling rule.\n\nAction (dict) -- [REQUIRED]The conditions that trigger an automatic scaling activity.\n\nMarket (string) --Not available for instance groups. Instance groups use the market type specified for the group.\n\nSimpleScalingPolicyConfiguration (dict) -- [REQUIRED]The type of adjustment the automatic scaling activity makes when triggered, and the periodicity of the adjustment.\n\nAdjustmentType (string) --The way in which EC2 instances are added (if ScalingAdjustment is a positive number) or terminated (if ScalingAdjustment is a negative number) each time the scaling activity is triggered. CHANGE_IN_CAPACITY is the default. CHANGE_IN_CAPACITY indicates that the EC2 instance count increments or decrements by ScalingAdjustment , which should be expressed as an integer. PERCENT_CHANGE_IN_CAPACITY indicates the instance count increments or decrements by the percentage specified by ScalingAdjustment , which should be expressed as an integer. For example, 20 indicates an increase in 20% increments of cluster capacity. EXACT_CAPACITY indicates the scaling activity results in an instance group with the number of EC2 instances specified by ScalingAdjustment , which should be expressed as a positive integer.\n\nScalingAdjustment (integer) -- [REQUIRED]The amount by which to scale in or scale out, based on the specified AdjustmentType . A positive value adds to the instance group\'s EC2 instance count while a negative number removes instances. If AdjustmentType is set to EXACT_CAPACITY , the number should only be a positive integer. If AdjustmentType is set to PERCENT_CHANGE_IN_CAPACITY , the value should express the percentage as an integer. For example, -20 indicates a decrease in 20% increments of cluster capacity.\n\nCoolDown (integer) --The amount of time, in seconds, after a scaling activity completes before any further trigger-related scaling activities can start. The default value is 0.\n\n\n\n\n\nTrigger (dict) -- [REQUIRED]The CloudWatch alarm definition that determines when automatic scaling activity is triggered.\n\nCloudWatchAlarmDefinition (dict) -- [REQUIRED]The definition of a CloudWatch metric alarm. When the defined alarm conditions are met along with other trigger parameters, scaling activity begins.\n\nComparisonOperator (string) -- [REQUIRED]Determines how the metric specified by MetricName is compared to the value specified by Threshold .\n\nEvaluationPeriods (integer) --The number of periods, in five-minute increments, during which the alarm condition must exist before the alarm triggers automatic scaling activity. The default value is 1 .\n\nMetricName (string) -- [REQUIRED]The name of the CloudWatch metric that is watched to determine an alarm condition.\n\nNamespace (string) --The namespace for the CloudWatch metric. The default is AWS/ElasticMapReduce .\n\nPeriod (integer) -- [REQUIRED]The period, in seconds, over which the statistic is applied. EMR CloudWatch metrics are emitted every five minutes (300 seconds), so if an EMR CloudWatch metric is specified, specify 300 .\n\nStatistic (string) --The statistic to apply to the metric associated with the alarm. The default is AVERAGE .\n\nThreshold (float) -- [REQUIRED]The value against which the specified statistic is compared.\n\nUnit (string) --The unit of measure associated with the CloudWatch metric being watched. The value specified for Unit must correspond to the units specified in the CloudWatch metric.\n\nDimensions (list) --A CloudWatch metric dimension.\n\n(dict) --A CloudWatch dimension, which is specified using a Key (known as a Name in CloudWatch), Value pair. By default, Amazon EMR uses one dimension whose Key is JobFlowID and Value is a variable representing the cluster ID, which is ${emr.clusterId} . This enables the rule to bootstrap when the cluster ID becomes available.\n\nKey (string) --The dimension name.\n\nValue (string) --The dimension value.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
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
    },
    'ClusterArn': 'string'
}


Response Structure

(dict) --

ClusterId (string) --
Specifies the ID of a cluster. The instance group to which the automatic scaling policy is applied is within this cluster.

InstanceGroupId (string) --
Specifies the ID of the instance group to which the scaling policy is applied.

AutoScalingPolicy (dict) --
The automatic scaling policy definition.

Status (dict) --
The status of an automatic scaling policy.

State (string) --
Indicates the status of the automatic scaling policy.

StateChangeReason (dict) --
The reason for a change in status.

Code (string) --
The code indicating the reason for the change in status.``USER_REQUEST`` indicates that the scaling policy status was changed by a user. PROVISION_FAILURE indicates that the status change was because the policy failed to provision. CLEANUP_FAILURE indicates an error.

Message (string) --
A friendly, more verbose message that accompanies an automatic scaling policy state change.





Constraints (dict) --
The upper and lower EC2 instance limits for an automatic scaling policy. Automatic scaling activity will not cause an instance group to grow above or below these limits.

MinCapacity (integer) --
The lower boundary of EC2 instances in an instance group below which scaling activities are not allowed to shrink. Scale-in activities will not terminate instances below this boundary.

MaxCapacity (integer) --
The upper boundary of EC2 instances in an instance group beyond which scaling activities are not allowed to grow. Scale-out activities will not add instances beyond this boundary.



Rules (list) --
The scale-in and scale-out rules that comprise the automatic scaling policy.

(dict) --
A scale-in or scale-out rule that defines scaling activity, including the CloudWatch metric alarm that triggers activity, how EC2 instances are added or removed, and the periodicity of adjustments. The automatic scaling policy for an instance group can comprise one or more automatic scaling rules.

Name (string) --
The name used to identify an automatic scaling rule. Rule names must be unique within a scaling policy.

Description (string) --
A friendly, more verbose description of the automatic scaling rule.

Action (dict) --
The conditions that trigger an automatic scaling activity.

Market (string) --
Not available for instance groups. Instance groups use the market type specified for the group.

SimpleScalingPolicyConfiguration (dict) --
The type of adjustment the automatic scaling activity makes when triggered, and the periodicity of the adjustment.

AdjustmentType (string) --
The way in which EC2 instances are added (if ScalingAdjustment is a positive number) or terminated (if ScalingAdjustment is a negative number) each time the scaling activity is triggered. CHANGE_IN_CAPACITY is the default. CHANGE_IN_CAPACITY indicates that the EC2 instance count increments or decrements by ScalingAdjustment , which should be expressed as an integer. PERCENT_CHANGE_IN_CAPACITY indicates the instance count increments or decrements by the percentage specified by ScalingAdjustment , which should be expressed as an integer. For example, 20 indicates an increase in 20% increments of cluster capacity. EXACT_CAPACITY indicates the scaling activity results in an instance group with the number of EC2 instances specified by ScalingAdjustment , which should be expressed as a positive integer.

ScalingAdjustment (integer) --
The amount by which to scale in or scale out, based on the specified AdjustmentType . A positive value adds to the instance group\'s EC2 instance count while a negative number removes instances. If AdjustmentType is set to EXACT_CAPACITY , the number should only be a positive integer. If AdjustmentType is set to PERCENT_CHANGE_IN_CAPACITY , the value should express the percentage as an integer. For example, -20 indicates a decrease in 20% increments of cluster capacity.

CoolDown (integer) --
The amount of time, in seconds, after a scaling activity completes before any further trigger-related scaling activities can start. The default value is 0.





Trigger (dict) --
The CloudWatch alarm definition that determines when automatic scaling activity is triggered.

CloudWatchAlarmDefinition (dict) --
The definition of a CloudWatch metric alarm. When the defined alarm conditions are met along with other trigger parameters, scaling activity begins.

ComparisonOperator (string) --
Determines how the metric specified by MetricName is compared to the value specified by Threshold .

EvaluationPeriods (integer) --
The number of periods, in five-minute increments, during which the alarm condition must exist before the alarm triggers automatic scaling activity. The default value is 1 .

MetricName (string) --
The name of the CloudWatch metric that is watched to determine an alarm condition.

Namespace (string) --
The namespace for the CloudWatch metric. The default is AWS/ElasticMapReduce .

Period (integer) --
The period, in seconds, over which the statistic is applied. EMR CloudWatch metrics are emitted every five minutes (300 seconds), so if an EMR CloudWatch metric is specified, specify 300 .

Statistic (string) --
The statistic to apply to the metric associated with the alarm. The default is AVERAGE .

Threshold (float) --
The value against which the specified statistic is compared.

Unit (string) --
The unit of measure associated with the CloudWatch metric being watched. The value specified for Unit must correspond to the units specified in the CloudWatch metric.

Dimensions (list) --
A CloudWatch metric dimension.

(dict) --
A CloudWatch dimension, which is specified using a Key (known as a Name in CloudWatch), Value pair. By default, Amazon EMR uses one dimension whose Key is JobFlowID and Value is a variable representing the cluster ID, which is ${emr.clusterId} . This enables the rule to bootstrap when the cluster ID becomes available.

Key (string) --
The dimension name.

Value (string) --
The dimension value.















ClusterArn (string) --
The Amazon Resource Name of the cluster.








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
        },
        'ClusterArn': 'string'
    }
    
    
    """
    pass

def put_block_public_access_configuration(BlockPublicAccessConfiguration=None):
    """
    Creates or updates an Amazon EMR block public access configuration for your AWS account in the current Region. For more information see Configure Block Public Access for Amazon EMR in the Amazon EMR Management Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_block_public_access_configuration(
        BlockPublicAccessConfiguration={
            'BlockPublicSecurityGroupRules': True|False,
            'PermittedPublicSecurityGroupRuleRanges': [
                {
                    'MinRange': 123,
                    'MaxRange': 123
                },
            ]
        }
    )
    
    
    :type BlockPublicAccessConfiguration: dict
    :param BlockPublicAccessConfiguration: [REQUIRED]\nA configuration for Amazon EMR block public access. The configuration applies to all clusters created in your account for the current Region. The configuration specifies whether block public access is enabled. If block public access is enabled, security groups associated with the cluster cannot have rules that allow inbound traffic from 0.0.0.0/0 or ::/0 on a port, unless the port is specified as an exception using PermittedPublicSecurityGroupRuleRanges in the BlockPublicAccessConfiguration . By default, Port 22 (SSH) is an exception, and public access is allowed on this port. You can change this by updating BlockPublicSecurityGroupRules to remove the exception.\n\nNote\nFor accounts that created clusters in a Region before November 25, 2019, block public access is disabled by default in that Region. To use this feature, you must manually enable and configure it. For accounts that did not create an EMR cluster in a Region before this date, block public access is enabled by default in that Region.\n\n\nBlockPublicSecurityGroupRules (boolean) -- [REQUIRED]Indicates whether EMR block public access is enabled (true ) or disabled (false ). By default, the value is false for accounts that have created EMR clusters before July 2019. For accounts created after this, the default is true .\n\nPermittedPublicSecurityGroupRuleRanges (list) --Specifies ports and port ranges that are permitted to have security group rules that allow inbound traffic from all public sources. For example, if Port 23 (Telnet) is specified for PermittedPublicSecurityGroupRuleRanges , Amazon EMR allows cluster creation if a security group associated with the cluster has a rule that allows inbound traffic on Port 23 from IPv4 0.0.0.0/0 or IPv6 port ::/0 as the source.\nBy default, Port 22, which is used for SSH access to the cluster EC2 instances, is in the list of PermittedPublicSecurityGroupRuleRanges .\n\n(dict) --A list of port ranges that are permitted to allow inbound traffic from all public IP addresses. To specify a single port, use the same value for MinRange and MaxRange .\n\nMinRange (integer) -- [REQUIRED]The smallest port number in a specified range of port numbers.\n\nMaxRange (integer) --The smallest port number in a specified range of port numbers.\n\n\n\n\n\n\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

EMR.Client.exceptions.InternalServerException
EMR.Client.exceptions.InvalidRequestException


    :return: {}
    
    
    :returns: 
    EMR.Client.exceptions.InternalServerException
    EMR.Client.exceptions.InvalidRequestException
    
    """
    pass

def put_managed_scaling_policy(ClusterId=None, ManagedScalingPolicy=None):
    """
    Creates or updates a managed scaling policy for an Amazon EMR cluster. The managed scaling policy defines the limits for resources, such as EC2 instances that can be added or terminated from a cluster. The policy only applies to the core and task nodes. The master node cannot be scaled after initial configuration.
    See also: AWS API Documentation
    
    
    :example: response = client.put_managed_scaling_policy(
        ClusterId='string',
        ManagedScalingPolicy={
            'ComputeLimits': {
                'UnitType': 'InstanceFleetUnits'|'Instances'|'VCPU',
                'MinimumCapacityUnits': 123,
                'MaximumCapacityUnits': 123,
                'MaximumOnDemandCapacityUnits': 123
            }
        }
    )
    
    
    :type ClusterId: string
    :param ClusterId: [REQUIRED]\nSpecifies the ID of an EMR cluster where the managed scaling policy is attached.\n

    :type ManagedScalingPolicy: dict
    :param ManagedScalingPolicy: [REQUIRED]\nSpecifies the constraints for the managed scaling policy.\n\nComputeLimits (dict) --The EC2 unit limits for a managed scaling policy. The managed scaling activity of a cluster is not allowed to go above or below these limits. The limit only applies to the core and task nodes. The master node cannot be scaled after initial configuration.\n\nUnitType (string) -- [REQUIRED]The unit type used for specifying a managed scaling policy.\n\nMinimumCapacityUnits (integer) -- [REQUIRED]The lower boundary of EC2 units. It is measured through VCPU cores or instances for instance groups and measured through units for instance fleets. Managed scaling activities are not allowed beyond this boundary. The limit only applies to the core and task nodes. The master node cannot be scaled after initial configuration.\n\nMaximumCapacityUnits (integer) -- [REQUIRED]The upper boundary of EC2 units. It is measured through VCPU cores or instances for instance groups and measured through units for instance fleets. Managed scaling activities are not allowed beyond this boundary. The limit only applies to the core and task nodes. The master node cannot be scaled after initial configuration.\n\nMaximumOnDemandCapacityUnits (integer) --The upper boundary of on-demand EC2 units. It is measured through VCPU cores or instances for instance groups and measured through units for instance fleets. The on-demand units are not allowed to scale beyond this boundary. The limit only applies to the core and task nodes. The master node cannot be scaled after initial configuration.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --





    :return: {}
    
    
    :returns: 
    (dict) --
    
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
    :param ClusterId: [REQUIRED]\nSpecifies the ID of a cluster. The instance group to which the automatic scaling policy is applied is within this cluster.\n

    :type InstanceGroupId: string
    :param InstanceGroupId: [REQUIRED]\nSpecifies the ID of the instance group to which the scaling policy is applied.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --





    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def remove_managed_scaling_policy(ClusterId=None):
    """
    Removes a managed scaling policy from a specified EMR cluster.
    See also: AWS API Documentation
    
    
    :example: response = client.remove_managed_scaling_policy(
        ClusterId='string'
    )
    
    
    :type ClusterId: string
    :param ClusterId: [REQUIRED]\nSpecifies the ID of the cluster from which the managed scaling policy will be removed.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --




    :return: {}
    
    
    """
    pass

def remove_tags(ResourceId=None, TagKeys=None):
    """
    Removes tags from an Amazon EMR resource. Tags make it easier to associate clusters in various ways, such as grouping clusters to track your Amazon EMR resource allocation costs. For more information, see Tag Clusters .
    The following example removes the stack tag with value Prod from a cluster:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.remove_tags(
        ResourceId='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceId: string
    :param ResourceId: [REQUIRED]\nThe Amazon EMR resource identifier from which tags will be removed. This value must be a cluster identifier.\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nA list of tag keys to remove from a resource.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
This output indicates the result of removing tags from a resource.





Exceptions

EMR.Client.exceptions.InternalServerException
EMR.Client.exceptions.InvalidRequestException


    :return: {}
    
    
    :returns: 
    EMR.Client.exceptions.InternalServerException
    EMR.Client.exceptions.InvalidRequestException
    
    """
    pass

def run_job_flow(Name=None, LogUri=None, AdditionalInfo=None, AmiVersion=None, ReleaseLabel=None, Instances=None, Steps=None, BootstrapActions=None, SupportedProducts=None, NewSupportedProducts=None, Applications=None, Configurations=None, VisibleToAllUsers=None, JobFlowRole=None, ServiceRole=None, Tags=None, SecurityConfiguration=None, AutoScalingRole=None, ScaleDownBehavior=None, CustomAmiId=None, EbsRootVolumeSize=None, RepoUpgradeOnBoot=None, KerberosAttributes=None, StepConcurrencyLevel=None, ManagedScalingPolicy=None):
    """
    RunJobFlow creates and starts running a new cluster (job flow). The cluster runs the steps specified. After the steps complete, the cluster stops and the HDFS partition is lost. To prevent loss of data, configure the last step of the job flow to store results in Amazon S3. If the  JobFlowInstancesConfig  KeepJobFlowAliveWhenNoSteps parameter is set to TRUE , the cluster transitions to the WAITING state rather than shutting down after the steps have completed.
    For additional protection, you can set the  JobFlowInstancesConfig  TerminationProtected parameter to TRUE to lock the cluster and prevent it from being terminated by API call, user intervention, or in the event of a job flow error.
    A maximum of 256 steps are allowed in each job flow.
    If your cluster is long-running (such as a Hive data warehouse) or complex, you may require more than 256 steps to process your data. You can bypass the 256-step limitation in various ways, including using the SSH shell to connect to the master node and submitting queries directly to the software running on the master node, such as Hive and Hadoop. For more information on how to do this, see Add More than 256 Steps to a Cluster in the Amazon EMR Management Guide .
    For long running clusters, we recommend that you periodically store your results.
    See also: AWS API Documentation
    
    Exceptions
    
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
        ScaleDownBehavior='TERMINATE_AT_INSTANCE_HOUR'|'TERMINATE_AT_TASK_COMPLETION',
        CustomAmiId='string',
        EbsRootVolumeSize=123,
        RepoUpgradeOnBoot='SECURITY'|'NONE',
        KerberosAttributes={
            'Realm': 'string',
            'KdcAdminPassword': 'string',
            'CrossRealmTrustPrincipalPassword': 'string',
            'ADDomainJoinUser': 'string',
            'ADDomainJoinPassword': 'string'
        },
        StepConcurrencyLevel=123,
        ManagedScalingPolicy={
            'ComputeLimits': {
                'UnitType': 'InstanceFleetUnits'|'Instances'|'VCPU',
                'MinimumCapacityUnits': 123,
                'MaximumCapacityUnits': 123,
                'MaximumOnDemandCapacityUnits': 123
            }
        }
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the job flow.\n

    :type LogUri: string
    :param LogUri: The location in Amazon S3 to write the log files of the job flow. If a value is not provided, logs are not created.

    :type AdditionalInfo: string
    :param AdditionalInfo: A JSON string for selecting additional features.

    :type AmiVersion: string
    :param AmiVersion: Applies only to Amazon EMR AMI versions 3.x and 2.x. For Amazon EMR releases 4.0 and later, ReleaseLabel is used. To specify a custom AMI, use CustomAmiID .

    :type ReleaseLabel: string
    :param ReleaseLabel: The Amazon EMR release label, which determines the version of open-source application packages installed on the cluster. Release labels are in the form emr-x.x.x , where x.x.x is an Amazon EMR release version such as emr-5.14.0 . For more information about Amazon EMR release versions and included application versions and features, see https://docs.aws.amazon.com/emr/latest/ReleaseGuide/ . The release label applies only to Amazon EMR releases version 4.0 and later. Earlier versions use AmiVersion .

    :type Instances: dict
    :param Instances: [REQUIRED]\nA specification of the number and type of Amazon EC2 instances.\n\nMasterInstanceType (string) --The EC2 instance type of the master node.\n\nSlaveInstanceType (string) --The EC2 instance type of the core and task nodes.\n\nInstanceCount (integer) --The number of EC2 instances in the cluster.\n\nInstanceGroups (list) --Configuration for the instance groups in a cluster.\n\n(dict) --Configuration defining a new instance group.\n\nName (string) --Friendly name given to the instance group.\n\nMarket (string) --Market type of the EC2 instances used to create a cluster node.\n\nInstanceRole (string) -- [REQUIRED]The role of the instance group in the cluster.\n\nBidPrice (string) --The bid price for each EC2 Spot instance type as defined by InstanceType . Expressed in USD. If neither BidPrice nor BidPriceAsPercentageOfOnDemandPrice is provided, BidPriceAsPercentageOfOnDemandPrice defaults to 100%.\n\nInstanceType (string) -- [REQUIRED]The EC2 instance type for all instances in the instance group.\n\nInstanceCount (integer) -- [REQUIRED]Target number of instances for the instance group.\n\nConfigurations (list) --\nNote\nAmazon EMR releases 4.x or later.\n\nThe list of configurations supplied for an EMR cluster instance group. You can specify a separate configuration for each instance group (master, core, and task).\n\n(dict) --\nNote\nAmazon EMR releases 4.x or later.\n\nAn optional configuration specification to be used when provisioning cluster instances, which can include configurations for applications and software bundled with Amazon EMR. A configuration consists of a classification, properties, and optional nested configurations. A classification refers to an application-specific configuration file. Properties are the settings you want to change in that file. For more information, see Configuring Applications .\n\nClassification (string) --The classification within a configuration.\n\nConfigurations (list) --A list of additional configurations to apply within a configuration object.\n\nProperties (dict) --A set of properties specified within a configuration classification.\n\n(string) --\n(string) --\n\n\n\n\n\n\n\n\nEbsConfiguration (dict) --EBS configurations that will be attached to each EC2 instance in the instance group.\n\nEbsBlockDeviceConfigs (list) --An array of Amazon EBS volume specifications attached to a cluster instance.\n\n(dict) --Configuration of requested EBS block device associated with the instance group with count of volumes that will be associated to every instance.\n\nVolumeSpecification (dict) -- [REQUIRED]EBS volume specifications such as volume type, IOPS, and size (GiB) that will be requested for the EBS volume attached to an EC2 instance in the cluster.\n\nVolumeType (string) -- [REQUIRED]The volume type. Volume types supported are gp2, io1, standard.\n\nIops (integer) --The number of I/O operations per second (IOPS) that the volume supports.\n\nSizeInGB (integer) -- [REQUIRED]The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the volume type is EBS-optimized, the minimum value is 10.\n\n\n\nVolumesPerInstance (integer) --Number of EBS volumes with a specific volume configuration that will be associated with every instance in the instance group\n\n\n\n\n\nEbsOptimized (boolean) --Indicates whether an Amazon EBS volume is EBS-optimized.\n\n\n\nAutoScalingPolicy (dict) --An automatic scaling policy for a core instance group or task instance group in an Amazon EMR cluster. The automatic scaling policy defines how an instance group dynamically adds and terminates EC2 instances in response to the value of a CloudWatch metric. See PutAutoScalingPolicy .\n\nConstraints (dict) -- [REQUIRED]The upper and lower EC2 instance limits for an automatic scaling policy. Automatic scaling activity will not cause an instance group to grow above or below these limits.\n\nMinCapacity (integer) -- [REQUIRED]The lower boundary of EC2 instances in an instance group below which scaling activities are not allowed to shrink. Scale-in activities will not terminate instances below this boundary.\n\nMaxCapacity (integer) -- [REQUIRED]The upper boundary of EC2 instances in an instance group beyond which scaling activities are not allowed to grow. Scale-out activities will not add instances beyond this boundary.\n\n\n\nRules (list) -- [REQUIRED]The scale-in and scale-out rules that comprise the automatic scaling policy.\n\n(dict) --A scale-in or scale-out rule that defines scaling activity, including the CloudWatch metric alarm that triggers activity, how EC2 instances are added or removed, and the periodicity of adjustments. The automatic scaling policy for an instance group can comprise one or more automatic scaling rules.\n\nName (string) -- [REQUIRED]The name used to identify an automatic scaling rule. Rule names must be unique within a scaling policy.\n\nDescription (string) --A friendly, more verbose description of the automatic scaling rule.\n\nAction (dict) -- [REQUIRED]The conditions that trigger an automatic scaling activity.\n\nMarket (string) --Not available for instance groups. Instance groups use the market type specified for the group.\n\nSimpleScalingPolicyConfiguration (dict) -- [REQUIRED]The type of adjustment the automatic scaling activity makes when triggered, and the periodicity of the adjustment.\n\nAdjustmentType (string) --The way in which EC2 instances are added (if ScalingAdjustment is a positive number) or terminated (if ScalingAdjustment is a negative number) each time the scaling activity is triggered. CHANGE_IN_CAPACITY is the default. CHANGE_IN_CAPACITY indicates that the EC2 instance count increments or decrements by ScalingAdjustment , which should be expressed as an integer. PERCENT_CHANGE_IN_CAPACITY indicates the instance count increments or decrements by the percentage specified by ScalingAdjustment , which should be expressed as an integer. For example, 20 indicates an increase in 20% increments of cluster capacity. EXACT_CAPACITY indicates the scaling activity results in an instance group with the number of EC2 instances specified by ScalingAdjustment , which should be expressed as a positive integer.\n\nScalingAdjustment (integer) -- [REQUIRED]The amount by which to scale in or scale out, based on the specified AdjustmentType . A positive value adds to the instance group\'s EC2 instance count while a negative number removes instances. If AdjustmentType is set to EXACT_CAPACITY , the number should only be a positive integer. If AdjustmentType is set to PERCENT_CHANGE_IN_CAPACITY , the value should express the percentage as an integer. For example, -20 indicates a decrease in 20% increments of cluster capacity.\n\nCoolDown (integer) --The amount of time, in seconds, after a scaling activity completes before any further trigger-related scaling activities can start. The default value is 0.\n\n\n\n\n\nTrigger (dict) -- [REQUIRED]The CloudWatch alarm definition that determines when automatic scaling activity is triggered.\n\nCloudWatchAlarmDefinition (dict) -- [REQUIRED]The definition of a CloudWatch metric alarm. When the defined alarm conditions are met along with other trigger parameters, scaling activity begins.\n\nComparisonOperator (string) -- [REQUIRED]Determines how the metric specified by MetricName is compared to the value specified by Threshold .\n\nEvaluationPeriods (integer) --The number of periods, in five-minute increments, during which the alarm condition must exist before the alarm triggers automatic scaling activity. The default value is 1 .\n\nMetricName (string) -- [REQUIRED]The name of the CloudWatch metric that is watched to determine an alarm condition.\n\nNamespace (string) --The namespace for the CloudWatch metric. The default is AWS/ElasticMapReduce .\n\nPeriod (integer) -- [REQUIRED]The period, in seconds, over which the statistic is applied. EMR CloudWatch metrics are emitted every five minutes (300 seconds), so if an EMR CloudWatch metric is specified, specify 300 .\n\nStatistic (string) --The statistic to apply to the metric associated with the alarm. The default is AVERAGE .\n\nThreshold (float) -- [REQUIRED]The value against which the specified statistic is compared.\n\nUnit (string) --The unit of measure associated with the CloudWatch metric being watched. The value specified for Unit must correspond to the units specified in the CloudWatch metric.\n\nDimensions (list) --A CloudWatch metric dimension.\n\n(dict) --A CloudWatch dimension, which is specified using a Key (known as a Name in CloudWatch), Value pair. By default, Amazon EMR uses one dimension whose Key is JobFlowID and Value is a variable representing the cluster ID, which is ${emr.clusterId} . This enables the rule to bootstrap when the cluster ID becomes available.\n\nKey (string) --The dimension name.\n\nValue (string) --The dimension value.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nInstanceFleets (list) --\nNote\nThe instance fleet configuration is available only in Amazon EMR versions 4.8.0 and later, excluding 5.0.x versions.\n\nDescribes the EC2 instances and instance configurations for clusters that use the instance fleet configuration.\n\n(dict) --The configuration that defines an instance fleet.\n\nNote\nThe instance fleet configuration is available only in Amazon EMR versions 4.8.0 and later, excluding 5.0.x versions.\n\n\nName (string) --The friendly name of the instance fleet.\n\nInstanceFleetType (string) -- [REQUIRED]The node type that the instance fleet hosts. Valid values are MASTER,CORE,and TASK.\n\nTargetOnDemandCapacity (integer) --The target capacity of On-Demand units for the instance fleet, which determines how many On-Demand instances to provision. When the instance fleet launches, Amazon EMR tries to provision On-Demand instances as specified by InstanceTypeConfig . Each instance configuration has a specified WeightedCapacity . When an On-Demand instance is provisioned, the WeightedCapacity units count toward the target capacity. Amazon EMR provisions instances until the target capacity is totally fulfilled, even if this results in an overage. For example, if there are 2 units remaining to fulfill capacity, and Amazon EMR can only provision an instance with a WeightedCapacity of 5 units, the instance is provisioned, and the target capacity is exceeded by 3 units.\n\nNote\nIf not specified or set to 0, only Spot instances are provisioned for the instance fleet using TargetSpotCapacity . At least one of TargetSpotCapacity and TargetOnDemandCapacity should be greater than 0. For a master instance fleet, only one of TargetSpotCapacity and TargetOnDemandCapacity can be specified, and its value must be 1.\n\n\nTargetSpotCapacity (integer) --The target capacity of Spot units for the instance fleet, which determines how many Spot instances to provision. When the instance fleet launches, Amazon EMR tries to provision Spot instances as specified by InstanceTypeConfig . Each instance configuration has a specified WeightedCapacity . When a Spot instance is provisioned, the WeightedCapacity units count toward the target capacity. Amazon EMR provisions instances until the target capacity is totally fulfilled, even if this results in an overage. For example, if there are 2 units remaining to fulfill capacity, and Amazon EMR can only provision an instance with a WeightedCapacity of 5 units, the instance is provisioned, and the target capacity is exceeded by 3 units.\n\nNote\nIf not specified or set to 0, only On-Demand instances are provisioned for the instance fleet. At least one of TargetSpotCapacity and TargetOnDemandCapacity should be greater than 0. For a master instance fleet, only one of TargetSpotCapacity and TargetOnDemandCapacity can be specified, and its value must be 1.\n\n\nInstanceTypeConfigs (list) --The instance type configurations that define the EC2 instances in the instance fleet.\n\n(dict) --An instance type configuration for each instance type in an instance fleet, which determines the EC2 instances Amazon EMR attempts to provision to fulfill On-Demand and Spot target capacities. There can be a maximum of 5 instance type configurations in a fleet.\n\nNote\nThe instance fleet configuration is available only in Amazon EMR versions 4.8.0 and later, excluding 5.0.x versions.\n\n\nInstanceType (string) -- [REQUIRED]An EC2 instance type, such as m3.xlarge .\n\nWeightedCapacity (integer) --The number of units that a provisioned instance of this type provides toward fulfilling the target capacities defined in InstanceFleetConfig . This value is 1 for a master instance fleet, and must be 1 or greater for core and task instance fleets. Defaults to 1 if not specified.\n\nBidPrice (string) --The bid price for each EC2 Spot instance type as defined by InstanceType . Expressed in USD. If neither BidPrice nor BidPriceAsPercentageOfOnDemandPrice is provided, BidPriceAsPercentageOfOnDemandPrice defaults to 100%.\n\nBidPriceAsPercentageOfOnDemandPrice (float) --The bid price, as a percentage of On-Demand price, for each EC2 Spot instance as defined by InstanceType . Expressed as a number (for example, 20 specifies 20%). If neither BidPrice nor BidPriceAsPercentageOfOnDemandPrice is provided, BidPriceAsPercentageOfOnDemandPrice defaults to 100%.\n\nEbsConfiguration (dict) --The configuration of Amazon Elastic Block Storage (EBS) attached to each instance as defined by InstanceType .\n\nEbsBlockDeviceConfigs (list) --An array of Amazon EBS volume specifications attached to a cluster instance.\n\n(dict) --Configuration of requested EBS block device associated with the instance group with count of volumes that will be associated to every instance.\n\nVolumeSpecification (dict) -- [REQUIRED]EBS volume specifications such as volume type, IOPS, and size (GiB) that will be requested for the EBS volume attached to an EC2 instance in the cluster.\n\nVolumeType (string) -- [REQUIRED]The volume type. Volume types supported are gp2, io1, standard.\n\nIops (integer) --The number of I/O operations per second (IOPS) that the volume supports.\n\nSizeInGB (integer) -- [REQUIRED]The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the volume type is EBS-optimized, the minimum value is 10.\n\n\n\nVolumesPerInstance (integer) --Number of EBS volumes with a specific volume configuration that will be associated with every instance in the instance group\n\n\n\n\n\nEbsOptimized (boolean) --Indicates whether an Amazon EBS volume is EBS-optimized.\n\n\n\nConfigurations (list) --A configuration classification that applies when provisioning cluster instances, which can include configurations for applications and software that run on the cluster.\n\n(dict) --\nNote\nAmazon EMR releases 4.x or later.\n\nAn optional configuration specification to be used when provisioning cluster instances, which can include configurations for applications and software bundled with Amazon EMR. A configuration consists of a classification, properties, and optional nested configurations. A classification refers to an application-specific configuration file. Properties are the settings you want to change in that file. For more information, see Configuring Applications .\n\nClassification (string) --The classification within a configuration.\n\nConfigurations (list) --A list of additional configurations to apply within a configuration object.\n\nProperties (dict) --A set of properties specified within a configuration classification.\n\n(string) --\n(string) --\n\n\n\n\n\n\n\n\n\n\n\n\nLaunchSpecifications (dict) --The launch specification for the instance fleet.\n\nSpotSpecification (dict) -- [REQUIRED]The launch specification for Spot instances in the fleet, which determines the defined duration and provisioning timeout behavior.\n\nTimeoutDurationMinutes (integer) -- [REQUIRED]The spot provisioning timeout period in minutes. If Spot instances are not provisioned within this time period, the TimeOutAction is taken. Minimum value is 5 and maximum value is 1440. The timeout applies only during initial provisioning, when the cluster is first created.\n\nTimeoutAction (string) -- [REQUIRED]The action to take when TargetSpotCapacity has not been fulfilled when the TimeoutDurationMinutes has expired; that is, when all Spot instances could not be provisioned within the Spot provisioning timeout. Valid values are TERMINATE_CLUSTER and SWITCH_TO_ON_DEMAND . SWITCH_TO_ON_DEMAND specifies that if no Spot instances are available, On-Demand Instances should be provisioned to fulfill any remaining Spot capacity.\n\nBlockDurationMinutes (integer) --The defined duration for Spot instances (also known as Spot blocks) in minutes. When specified, the Spot instance does not terminate before the defined duration expires, and defined duration pricing for Spot instances applies. Valid values are 60, 120, 180, 240, 300, or 360. The duration period starts as soon as a Spot instance receives its instance ID. At the end of the duration, Amazon EC2 marks the Spot instance for termination and provides a Spot instance termination notice, which gives the instance a two-minute warning before it terminates.\n\n\n\n\n\n\n\n\n\nEc2KeyName (string) --The name of the EC2 key pair that can be used to ssh to the master node as the user called 'hadoop.'\n\nPlacement (dict) --The Availability Zone in which the cluster runs.\n\nAvailabilityZone (string) --The Amazon EC2 Availability Zone for the cluster. AvailabilityZone is used for uniform instance groups, while AvailabilityZones (plural) is used for instance fleets.\n\nAvailabilityZones (list) --When multiple Availability Zones are specified, Amazon EMR evaluates them and launches instances in the optimal Availability Zone. AvailabilityZones is used for instance fleets, while AvailabilityZone (singular) is used for uniform instance groups.\n\nNote\nThe instance fleet configuration is available only in Amazon EMR versions 4.8.0 and later, excluding 5.0.x versions.\n\n\n(string) --\n\n\n\n\nKeepJobFlowAliveWhenNoSteps (boolean) --Specifies whether the cluster should remain available after completing all steps.\n\nTerminationProtected (boolean) --Specifies whether to lock the cluster to prevent the Amazon EC2 instances from being terminated by API call, user intervention, or in the event of a job-flow error.\n\nHadoopVersion (string) --Applies only to Amazon EMR release versions earlier than 4.0. The Hadoop version for the cluster. Valid inputs are '0.18' (deprecated), '0.20' (deprecated), '0.20.205' (deprecated), '1.0.3', '2.2.0', or '2.4.0'. If you do not set this value, the default of 0.18 is used, unless the AmiVersion parameter is set in the RunJobFlow call, in which case the default version of Hadoop for that AMI version is used.\n\nEc2SubnetId (string) --Applies to clusters that use the uniform instance group configuration. To launch the cluster in Amazon Virtual Private Cloud (Amazon VPC), set this parameter to the identifier of the Amazon VPC subnet where you want the cluster to launch. If you do not specify this value and your account supports EC2-Classic, the cluster launches in EC2-Classic.\n\nEc2SubnetIds (list) --Applies to clusters that use the instance fleet configuration. When multiple EC2 subnet IDs are specified, Amazon EMR evaluates them and launches instances in the optimal subnet.\n\nNote\nThe instance fleet configuration is available only in Amazon EMR versions 4.8.0 and later, excluding 5.0.x versions.\n\n\n(string) --\n\n\nEmrManagedMasterSecurityGroup (string) --The identifier of the Amazon EC2 security group for the master node.\n\nEmrManagedSlaveSecurityGroup (string) --The identifier of the Amazon EC2 security group for the core and task nodes.\n\nServiceAccessSecurityGroup (string) --The identifier of the Amazon EC2 security group for the Amazon EMR service to access clusters in VPC private subnets.\n\nAdditionalMasterSecurityGroups (list) --A list of additional Amazon EC2 security group IDs for the master node.\n\n(string) --\n\n\nAdditionalSlaveSecurityGroups (list) --A list of additional Amazon EC2 security group IDs for the core and task nodes.\n\n(string) --\n\n\n\n

    :type Steps: list
    :param Steps: A list of steps to run.\n\n(dict) --Specification of a cluster (job flow) step.\n\nName (string) -- [REQUIRED]The name of the step.\n\nActionOnFailure (string) --The action to take when the cluster step fails. Possible values are TERMINATE_CLUSTER, CANCEL_AND_WAIT, and CONTINUE. TERMINATE_JOB_FLOW is provided for backward compatibility. We recommend using TERMINATE_CLUSTER instead.\n\nHadoopJarStep (dict) -- [REQUIRED]The JAR file used for the step.\n\nProperties (list) --A list of Java properties that are set when the step runs. You can use these properties to pass key value pairs to your main function.\n\n(dict) --A key value pair.\n\nKey (string) --The unique identifier of a key value pair.\n\nValue (string) --The value part of the identified key.\n\n\n\n\n\nJar (string) -- [REQUIRED]A path to a JAR file run during the step.\n\nMainClass (string) --The name of the main class in the specified Java file. If not specified, the JAR file should specify a Main-Class in its manifest file.\n\nArgs (list) --A list of command line arguments passed to the JAR file\'s main function when executed.\n\n(string) --\n\n\n\n\n\n\n\n

    :type BootstrapActions: list
    :param BootstrapActions: A list of bootstrap actions to run before Hadoop starts on the cluster nodes.\n\n(dict) --Configuration of a bootstrap action.\n\nName (string) -- [REQUIRED]The name of the bootstrap action.\n\nScriptBootstrapAction (dict) -- [REQUIRED]The script run by the bootstrap action.\n\nPath (string) -- [REQUIRED]Location of the script to run during a bootstrap action. Can be either a location in Amazon S3 or on a local file system.\n\nArgs (list) --A list of command line arguments to pass to the bootstrap action script.\n\n(string) --\n\n\n\n\n\n\n\n

    :type SupportedProducts: list
    :param SupportedProducts: \nNote\nFor Amazon EMR releases 3.x and 2.x. For Amazon EMR releases 4.x and later, use Applications.\n\nA list of strings that indicates third-party software to use. For more information, see the Amazon EMR Developer Guide . Currently supported values are:\n\n'mapr-m3' - launch the job flow using MapR M3 Edition.\n'mapr-m5' - launch the job flow using MapR M5 Edition.\n\n\n(string) --\n\n

    :type NewSupportedProducts: list
    :param NewSupportedProducts: \nNote\nFor Amazon EMR releases 3.x and 2.x. For Amazon EMR releases 4.x and later, use Applications.\n\nA list of strings that indicates third-party software to use with the job flow that accepts a user argument list. EMR accepts and forwards the argument list to the corresponding installation script as bootstrap action arguments. For more information, see 'Launch a Job Flow on the MapR Distribution for Hadoop' in the Amazon EMR Developer Guide . Supported values are:\n\n'mapr-m3' - launch the cluster using MapR M3 Edition.\n'mapr-m5' - launch the cluster using MapR M5 Edition.\n'mapr' with the user arguments specifying '--edition,m3' or '--edition,m5' - launch the job flow using MapR M3 or M5 Edition respectively.\n'mapr-m7' - launch the cluster using MapR M7 Edition.\n'hunk' - launch the cluster with the Hunk Big Data Analtics Platform.\n'hue'- launch the cluster with Hue installed.\n'spark' - launch the cluster with Apache Spark installed.\n'ganglia' - launch the cluster with the Ganglia Monitoring System installed.\n\n\n(dict) --The list of supported product configurations which allow user-supplied arguments. EMR accepts these arguments and forwards them to the corresponding installation script as bootstrap action arguments.\n\nName (string) --The name of the product configuration.\n\nArgs (list) --The list of user-supplied arguments.\n\n(string) --\n\n\n\n\n\n

    :type Applications: list
    :param Applications: Applies to Amazon EMR releases 4.0 and later. A case-insensitive list of applications for Amazon EMR to install and configure when launching the cluster. For a list of applications available for each Amazon EMR release version, see the Amazon EMR Release Guide .\n\n(dict) --With Amazon EMR release version 4.0 and later, the only accepted parameter is the application name. To pass arguments to applications, you use configuration classifications specified using configuration JSON objects. For more information, see Configuring Applications .\nWith earlier Amazon EMR releases, the application is any Amazon or third-party software that you can add to the cluster. This structure contains a list of strings that indicates the software to use with the cluster and accepts a user argument list. Amazon EMR accepts and forwards the argument list to the corresponding installation script as bootstrap action argument.\n\nName (string) --The name of the application.\n\nVersion (string) --The version of the application.\n\nArgs (list) --Arguments for Amazon EMR to pass to the application.\n\n(string) --\n\n\nAdditionalInfo (dict) --This option is for advanced users only. This is meta information about third-party applications that third-party vendors use for testing purposes.\n\n(string) --\n(string) --\n\n\n\n\n\n\n\n

    :type Configurations: list
    :param Configurations: For Amazon EMR releases 4.0 and later. The list of configurations supplied for the EMR cluster you are creating.\n\n(dict) --\nNote\nAmazon EMR releases 4.x or later.\n\nAn optional configuration specification to be used when provisioning cluster instances, which can include configurations for applications and software bundled with Amazon EMR. A configuration consists of a classification, properties, and optional nested configurations. A classification refers to an application-specific configuration file. Properties are the settings you want to change in that file. For more information, see Configuring Applications .\n\nClassification (string) --The classification within a configuration.\n\nConfigurations (list) --A list of additional configurations to apply within a configuration object.\n\nProperties (dict) --A set of properties specified within a configuration classification.\n\n(string) --\n(string) --\n\n\n\n\n\n\n\n

    :type VisibleToAllUsers: boolean
    :param VisibleToAllUsers: A value of true indicates that all IAM users in the AWS account can perform cluster actions if they have the proper IAM policy permissions. This is the default. A value of false indicates that only the IAM user who created the cluster can perform actions.

    :type JobFlowRole: string
    :param JobFlowRole: Also called instance profile and EC2 role. An IAM role for an EMR cluster. The EC2 instances of the cluster assume this role. The default role is EMR_EC2_DefaultRole . In order to use the default role, you must have already created it using the CLI or console.

    :type ServiceRole: string
    :param ServiceRole: The IAM role that will be assumed by the Amazon EMR service to access AWS resources on your behalf.

    :type Tags: list
    :param Tags: A list of tags to associate with a cluster and propagate to Amazon EC2 instances.\n\n(dict) --A key/value pair containing user-defined metadata that you can associate with an Amazon EMR resource. Tags make it easier to associate clusters in various ways, such as grouping clusters to track your Amazon EMR resource allocation costs. For more information, see Tag Clusters .\n\nKey (string) --A user-defined key, which is the minimum required information for a valid tag. For more information, see Tag .\n\nValue (string) --A user-defined value, which is optional in a tag. For more information, see Tag Clusters .\n\n\n\n\n

    :type SecurityConfiguration: string
    :param SecurityConfiguration: The name of a security configuration to apply to the cluster.

    :type AutoScalingRole: string
    :param AutoScalingRole: An IAM role for automatic scaling policies. The default role is EMR_AutoScaling_DefaultRole . The IAM role provides permissions that the automatic scaling feature requires to launch and terminate EC2 instances in an instance group.

    :type ScaleDownBehavior: string
    :param ScaleDownBehavior: Specifies the way that individual Amazon EC2 instances terminate when an automatic scale-in activity occurs or an instance group is resized. TERMINATE_AT_INSTANCE_HOUR indicates that Amazon EMR terminates nodes at the instance-hour boundary, regardless of when the request to terminate the instance was submitted. This option is only available with Amazon EMR 5.1.0 and later and is the default for clusters created using that version. TERMINATE_AT_TASK_COMPLETION indicates that Amazon EMR blacklists and drains tasks from nodes before terminating the Amazon EC2 instances, regardless of the instance-hour boundary. With either behavior, Amazon EMR removes the least active nodes first and blocks instance termination if it could lead to HDFS corruption. TERMINATE_AT_TASK_COMPLETION available only in Amazon EMR version 4.1.0 and later, and is the default for versions of Amazon EMR earlier than 5.1.0.

    :type CustomAmiId: string
    :param CustomAmiId: Available only in Amazon EMR version 5.7.0 and later. The ID of a custom Amazon EBS-backed Linux AMI. If specified, Amazon EMR uses this AMI when it launches cluster EC2 instances. For more information about custom AMIs in Amazon EMR, see Using a Custom AMI in the Amazon EMR Management Guide . If omitted, the cluster uses the base Linux AMI for the ReleaseLabel specified. For Amazon EMR versions 2.x and 3.x, use AmiVersion instead.\nFor information about creating a custom AMI, see Creating an Amazon EBS-Backed Linux AMI in the Amazon Elastic Compute Cloud User Guide for Linux Instances . For information about finding an AMI ID, see Finding a Linux AMI .\n

    :type EbsRootVolumeSize: integer
    :param EbsRootVolumeSize: The size, in GiB, of the EBS root device volume of the Linux AMI that is used for each EC2 instance. Available in Amazon EMR version 4.x and later.

    :type RepoUpgradeOnBoot: string
    :param RepoUpgradeOnBoot: Applies only when CustomAmiID is used. Specifies which updates from the Amazon Linux AMI package repositories to apply automatically when the instance boots using the AMI. If omitted, the default is SECURITY , which indicates that only security updates are applied. If NONE is specified, no updates are applied, and all updates must be applied manually.

    :type KerberosAttributes: dict
    :param KerberosAttributes: Attributes for Kerberos configuration when Kerberos authentication is enabled using a security configuration. For more information see Use Kerberos Authentication in the EMR Management Guide .\n\nRealm (string) -- [REQUIRED]The name of the Kerberos realm to which all nodes in a cluster belong. For example, EC2.INTERNAL .\n\nKdcAdminPassword (string) -- [REQUIRED]The password used within the cluster for the kadmin service on the cluster-dedicated KDC, which maintains Kerberos principals, password policies, and keytabs for the cluster.\n\nCrossRealmTrustPrincipalPassword (string) --Required only when establishing a cross-realm trust with a KDC in a different realm. The cross-realm principal password, which must be identical across realms.\n\nADDomainJoinUser (string) --Required only when establishing a cross-realm trust with an Active Directory domain. A user with sufficient privileges to join resources to the domain.\n\nADDomainJoinPassword (string) --The Active Directory password for ADDomainJoinUser .\n\n\n

    :type StepConcurrencyLevel: integer
    :param StepConcurrencyLevel: Specifies the number of steps that can be executed concurrently. The default value is 1 . The maximum value is 256 .

    :type ManagedScalingPolicy: dict
    :param ManagedScalingPolicy: The specified managed scaling policy for an Amazon EMR cluster.\n\nComputeLimits (dict) --The EC2 unit limits for a managed scaling policy. The managed scaling activity of a cluster is not allowed to go above or below these limits. The limit only applies to the core and task nodes. The master node cannot be scaled after initial configuration.\n\nUnitType (string) -- [REQUIRED]The unit type used for specifying a managed scaling policy.\n\nMinimumCapacityUnits (integer) -- [REQUIRED]The lower boundary of EC2 units. It is measured through VCPU cores or instances for instance groups and measured through units for instance fleets. Managed scaling activities are not allowed beyond this boundary. The limit only applies to the core and task nodes. The master node cannot be scaled after initial configuration.\n\nMaximumCapacityUnits (integer) -- [REQUIRED]The upper boundary of EC2 units. It is measured through VCPU cores or instances for instance groups and measured through units for instance fleets. Managed scaling activities are not allowed beyond this boundary. The limit only applies to the core and task nodes. The master node cannot be scaled after initial configuration.\n\nMaximumOnDemandCapacityUnits (integer) --The upper boundary of on-demand EC2 units. It is measured through VCPU cores or instances for instance groups and measured through units for instance fleets. The on-demand units are not allowed to scale beyond this boundary. The limit only applies to the core and task nodes. The master node cannot be scaled after initial configuration.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'JobFlowId': 'string',
    'ClusterArn': 'string'
}


Response Structure

(dict) --
The result of the  RunJobFlow operation.

JobFlowId (string) --
An unique identifier for the job flow.

ClusterArn (string) --
The Amazon Resource Name of the cluster.







Exceptions

EMR.Client.exceptions.InternalServerError


    :return: {
        'JobFlowId': 'string',
        'ClusterArn': 'string'
    }
    
    
    :returns: 
    EMR.Client.exceptions.InternalServerError
    
    """
    pass

def set_termination_protection(JobFlowIds=None, TerminationProtected=None):
    """
    SetTerminationProtection locks a cluster (job flow) so the EC2 instances in the cluster cannot be terminated by user intervention, an API call, or in the event of a job-flow error. The cluster still terminates upon successful completion of the job flow. Calling SetTerminationProtection on a cluster is similar to calling the Amazon EC2 DisableAPITermination API on all EC2 instances in a cluster.
    To terminate a cluster that has been locked by setting SetTerminationProtection to true , you must first unlock the job flow by a subsequent call to SetTerminationProtection in which you set the value to false .
    For more information, see`Managing Cluster Termination <https://docs.aws.amazon.com/emr/latest/ManagementGuide/UsingEMR_TerminationProtection.html>`__ in the Amazon EMR Management Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.set_termination_protection(
        JobFlowIds=[
            'string',
        ],
        TerminationProtected=True|False
    )
    
    
    :type JobFlowIds: list
    :param JobFlowIds: [REQUIRED]\nA list of strings that uniquely identify the clusters to protect. This identifier is returned by RunJobFlow and can also be obtained from DescribeJobFlows .\n\n(string) --\n\n

    :type TerminationProtected: boolean
    :param TerminationProtected: [REQUIRED]\nA Boolean that indicates whether to protect the cluster and prevent the Amazon EC2 instances in the cluster from shutting down due to API calls, user intervention, or job-flow error.\n

    :returns: 
    EMR.Client.exceptions.InternalServerError
    
    """
    pass

def set_visible_to_all_users(JobFlowIds=None, VisibleToAllUsers=None):
    """
    Sets the  Cluster$VisibleToAllUsers value, which determines whether the cluster is visible to all IAM users of the AWS account associated with the cluster. Only the IAM user who created the cluster or the AWS account root user can call this action. The default value, true , indicates that all IAM users in the AWS account can perform cluster actions if they have the proper IAM policy permissions. If set to false , only the IAM user that created the cluster can perform actions. This action works on running clusters. You can override the default true setting when you create a cluster by using the VisibleToAllUsers parameter with RunJobFlow .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.set_visible_to_all_users(
        JobFlowIds=[
            'string',
        ],
        VisibleToAllUsers=True|False
    )
    
    
    :type JobFlowIds: list
    :param JobFlowIds: [REQUIRED]\nThe unique identifier of the job flow (cluster).\n\n(string) --\n\n

    :type VisibleToAllUsers: boolean
    :param VisibleToAllUsers: [REQUIRED]\nA value of true indicates that all IAM users in the AWS account can perform cluster actions if they have the proper IAM policy permissions. This is the default. A value of false indicates that only the IAM user who created the cluster can perform actions.\n

    :returns: 
    EMR.Client.exceptions.InternalServerError
    
    """
    pass

def terminate_job_flows(JobFlowIds=None):
    """
    TerminateJobFlows shuts a list of clusters (job flows) down. When a job flow is shut down, any step not yet completed is canceled and the EC2 instances on which the cluster is running are stopped. Any log files not already saved are uploaded to Amazon S3 if a LogUri was specified when the cluster was created.
    The maximum number of clusters allowed is 10. The call to TerminateJobFlows is asynchronous. Depending on the configuration of the cluster, it may take up to 1-5 minutes for the cluster to completely terminate and release allocated resources, such as Amazon EC2 instances.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.terminate_job_flows(
        JobFlowIds=[
            'string',
        ]
    )
    
    
    :type JobFlowIds: list
    :param JobFlowIds: [REQUIRED]\nA list of job flows to be shutdown.\n\n(string) --\n\n

    :returns: 
    EMR.Client.exceptions.InternalServerError
    
    """
    pass

