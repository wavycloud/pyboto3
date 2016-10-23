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


def add_instance_groups(InstanceGroups=None, JobFlowId=None):
    """
    :param InstanceGroups: [REQUIRED]
            Instance Groups to add.
            (dict) --Configuration defining a new instance group.
            Name (string) --Friendly name given to the instance group.
            Market (string) --Market type of the Amazon EC2 instances used to create a cluster node.
            InstanceRole (string) -- [REQUIRED]The role of the instance group in the cluster.
            BidPrice (string) --Bid price for each Amazon EC2 instance in the instance group when launching nodes as Spot Instances, expressed in USD.
            InstanceType (string) -- [REQUIRED]The Amazon EC2 instance type for all instances in the instance group.
            InstanceCount (integer) -- [REQUIRED]Target number of instances for the instance group.
            Configurations (list) --
            Note
            Amazon EMR releases 4.x or later.
            The list of configurations supplied for an EMR cluster instance group. You can specify a separate configuration for each instance group (master, core, and task).
            (dict) --
            Note
            Amazon EMR releases 4.x or later.
            Specifies a hardware and software configuration of the EMR cluster. This includes configurations for applications and software bundled with Amazon EMR. The Configuration object is a JSON object which is defined by a classification and a set of properties. Configurations can be nested, so a configuration may have its own Configuration objects listed.
            Classification (string) --The classification of a configuration. For more information see, Amazon EMR Configurations .
            Configurations (list) --A list of configurations you apply to this configuration object.
            Properties (dict) --A set of properties supplied to the Configuration object.
            (string) --
            (string) --
            
            
            EbsConfiguration (dict) --EBS configurations that will be attached to each Amazon EC2 instance in the instance group.
            EbsBlockDeviceConfigs (list) --
            (dict) --Configuration of requested EBS block device associated with the instance group with count of volumes that will be associated to every instance.
            VolumeSpecification (dict) -- [REQUIRED]EBS volume specifications such as volume type, IOPS, and size(GiB) that will be requested for the EBS volume attached to an EC2 instance in the cluster.
            VolumeType (string) -- [REQUIRED]The volume type. Volume types supported are gp2, io1, standard.
            Iops (integer) --The number of I/O operations per second (IOPS) that the volume supports.
            SizeInGB (integer) -- [REQUIRED]The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the volume type is EBS-optimized, the minimum value is 10.
            VolumesPerInstance (integer) --Number of EBS volumes with specific volume configuration, that will be associated with every instance in the instance group
            
            EbsOptimized (boolean) --
            
            
    :type InstanceGroups: list
    :param JobFlowId: [REQUIRED]
            Job flow in which to add the instance groups.
            
    :type JobFlowId: string
    """
    pass


def add_job_flow_steps(JobFlowId=None, Steps=None):
    """
    :param JobFlowId: [REQUIRED]
            A string that uniquely identifies the job flow. This identifier is returned by RunJobFlow and can also be obtained from ListClusters .
            
    :type JobFlowId: string
    :param Steps: [REQUIRED]
            A list of StepConfig to be executed by the job flow.
            (dict) --Specification of a job flow step.
            Name (string) -- [REQUIRED]The name of the job flow step.
            ActionOnFailure (string) --The action to take if the job flow step fails.
            HadoopJarStep (dict) -- [REQUIRED]The JAR file used for the job flow step.
            Properties (list) --A list of Java properties that are set when the step runs. You can use these properties to pass key value pairs to your main function.
            (dict) --A key value pair.
            Key (string) --The unique identifier of a key value pair.
            Value (string) --The value part of the identified key.
            
            Jar (string) -- [REQUIRED]A path to a JAR file run during the step.
            MainClass (string) --The name of the main class in the specified Java file. If not specified, the JAR file should specify a Main-Class in its manifest file.
            Args (list) --A list of command line arguments passed to the JAR file's main function when executed.
            (string) --
            
            
    :type Steps: list
    """
    pass


def add_tags(ResourceId=None, Tags=None):
    """
    :param ResourceId: [REQUIRED]
            The Amazon EMR resource identifier to which tags will be added. This value must be a cluster identifier.
            
    :type ResourceId: string
    :param Tags: [REQUIRED]
            A list of tags to associate with a cluster and propagate to Amazon EC2 instances. Tags are user-defined key/value pairs that consist of a required key string with a maximum of 128 characters, and an optional value string with a maximum of 256 characters.
            (dict) --A key/value pair containing user-defined metadata that you can associate with an Amazon EMR resource. Tags make it easier to associate clusters in various ways, such as grouping clusters to track your Amazon EMR resource allocation costs. For more information, see Tagging Amazon EMR Resources .
            Key (string) --A user-defined key, which is the minimum required information for a valid tag. For more information, see Tagging Amazon EMR Resources .
            Value (string) --A user-defined value, which is optional in a tag. For more information, see Tagging Amazon EMR Resources .
            
            
    :type Tags: list
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


def create_security_configuration(Name=None, SecurityConfiguration=None):
    """
    :param Name: [REQUIRED]
            The name of the security configuration.
            
    :type Name: string
    :param SecurityConfiguration: [REQUIRED]
            The security configuration details in JSON format.
            
    :type SecurityConfiguration: string
    """
    pass


def delete_security_configuration(Name=None):
    """
    :param Name: [REQUIRED]
            The name of the security configuration.
            Return typedict
            ReturnsResponse Syntax{}
            Response Structure
            (dict) --
            
    :type Name: string
    """
    pass


def describe_cluster(ClusterId=None):
    """
    :param ClusterId: [REQUIRED]
            The identifier of the cluster to describe.
            Return typedict
            ReturnsResponse Syntax{
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
                  'Ec2AvailabilityZone': 'string',
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
                'SecurityConfiguration': 'string'
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
            Ec2KeyName (string) --The name of the Amazon EC2 key pair to use when connecting with SSH into the master node as a user named 'hadoop'.
            Ec2SubnetId (string) --To launch the job flow in Amazon VPC, set this parameter to the identifier of the Amazon VPC subnet where you want the job flow to launch. If you do not specify this value, the job flow is launched in the normal AWS cloud, outside of a VPC.
            Amazon VPC currently does not support cluster compute quadruple extra large (cc1.4xlarge) instances. Thus, you cannot specify the cc1.4xlarge instance type for nodes of a job flow launched in a VPC.
            Ec2AvailabilityZone (string) --The Availability Zone in which the cluster will run.
            IamInstanceProfile (string) --The IAM role that was specified when the job flow was launched. The EC2 instances of the job flow assume this role.
            EmrManagedMasterSecurityGroup (string) --The identifier of the Amazon EC2 security group for the master node.
            EmrManagedSlaveSecurityGroup (string) --The identifier of the Amazon EC2 security group for the slave nodes.
            ServiceAccessSecurityGroup (string) --The identifier of the Amazon EC2 security group for the Amazon EMR service to access clusters in VPC private subnets.
            AdditionalMasterSecurityGroups (list) --A list of additional Amazon EC2 security group IDs for the master node.
            (string) --
            AdditionalSlaveSecurityGroups (list) --A list of additional Amazon EC2 security group IDs for the slave nodes.
            (string) --
            
            LogUri (string) --The path to the Amazon S3 location where logs for this cluster are stored.
            RequestedAmiVersion (string) --The AMI version requested for this cluster.
            RunningAmiVersion (string) --The AMI version running on this cluster.
            ReleaseLabel (string) --The release label for the Amazon EMR release. For Amazon EMR 3.x and 2.x AMIs, use amiVersion instead instead of ReleaseLabel.
            AutoTerminate (boolean) --Specifies whether the cluster should terminate after completing all steps.
            TerminationProtected (boolean) --Indicates whether Amazon EMR will lock the cluster to prevent the EC2 instances from being terminated by an API call or user intervention, or in the event of a cluster error.
            VisibleToAllUsers (boolean) --Indicates whether the job flow is visible to all IAM users of the AWS account associated with the job flow. If this value is set to true , all IAM users of that AWS account can view and manage the job flow if they have the proper policy permissions set. If this value is false , only the IAM user that created the cluster can view and manage it. This value can be changed using the SetVisibleToAllUsers action.
            Applications (list) --The applications installed on this cluster.
            (dict) --An application is any Amazon or third-party software that you can add to the cluster. This structure contains a list of strings that indicates the software to use with the cluster and accepts a user argument list. Amazon EMR accepts and forwards the argument list to the corresponding installation script as bootstrap action argument. For more information, see Launch a Job Flow on the MapR Distribution for Hadoop . Currently supported values are:
            'mapr-m3' - launch the job flow using MapR M3 Edition.
            'mapr-m5' - launch the job flow using MapR M5 Edition.
            'mapr' with the user arguments specifying '--edition,m3' or '--edition,m5' - launch the job flow using MapR M3 or M5 Edition, respectively.
            Note
            In Amazon EMR releases 4.0 and greater, the only accepted parameter is the application name. To pass arguments to applications, you supply a configuration for each application.
            Name (string) --The name of the application.
            Version (string) --The version of the application.
            Args (list) --Arguments for Amazon EMR to pass to the application.
            (string) --
            AdditionalInfo (dict) --This option is for advanced users only. This is meta information about third-party applications that third-party vendors use for testing purposes.
            (string) --
            (string) --
            
            
            Tags (list) --A list of tags associated with a cluster.
            (dict) --A key/value pair containing user-defined metadata that you can associate with an Amazon EMR resource. Tags make it easier to associate clusters in various ways, such as grouping clusters to track your Amazon EMR resource allocation costs. For more information, see Tagging Amazon EMR Resources .
            Key (string) --A user-defined key, which is the minimum required information for a valid tag. For more information, see Tagging Amazon EMR Resources .
            Value (string) --A user-defined value, which is optional in a tag. For more information, see Tagging Amazon EMR Resources .
            
            ServiceRole (string) --The IAM role that will be assumed by the Amazon EMR service to access AWS resources on your behalf.
            NormalizedInstanceHours (integer) --An approximation of the cost of the job flow, represented in m1.small/hours. This value is incremented one time for every hour an m1.small instance runs. Larger instances are weighted more, so an EC2 instance that is roughly four times more expensive would result in the normalized instance hours being incremented by four. This result is only an approximation and does not reflect the actual billing rate.
            MasterPublicDnsName (string) --The public DNS name of the master EC2 instance.
            Configurations (list) --
            Note
            Amazon EMR releases 4.x or later.
            The list of Configurations supplied to the EMR cluster.
            (dict) --
            Note
            Amazon EMR releases 4.x or later.
            Specifies a hardware and software configuration of the EMR cluster. This includes configurations for applications and software bundled with Amazon EMR. The Configuration object is a JSON object which is defined by a classification and a set of properties. Configurations can be nested, so a configuration may have its own Configuration objects listed.
            Classification (string) --The classification of a configuration. For more information see, Amazon EMR Configurations .
            Configurations (list) --A list of configurations you apply to this configuration object.
            Properties (dict) --A set of properties supplied to the Configuration object.
            (string) --
            (string) --
            
            
            SecurityConfiguration (string) --The name of the security configuration applied to the cluster.
            
            
            
    :type ClusterId: string
    """
    pass


def describe_job_flows(CreatedAfter=None, CreatedBefore=None, JobFlowIds=None, JobFlowStates=None):
    """
    :param CreatedAfter: Return only job flows created after this date and time.
    :type CreatedAfter: datetime
    :param CreatedBefore: Return only job flows created before this date and time.
    :type CreatedBefore: datetime
    :param JobFlowIds: Return only job flows whose job flow ID is contained in this list.
            (string) --
            
    :type JobFlowIds: list
    :param JobFlowStates: Return only job flows whose state is contained in this list.
            (string) --The type of instance.
            
    :type JobFlowStates: list
    """
    pass


def describe_security_configuration(Name=None):
    """
    :param Name: [REQUIRED]
            The name of the security configuration.
            Return typedict
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
            
            
    :type Name: string
    """
    pass


def describe_step(ClusterId=None, StepId=None):
    """
    :param ClusterId: [REQUIRED]
            The identifier of the cluster with steps to describe.
            
    :type ClusterId: string
    :param StepId: [REQUIRED]
            The identifier of the step to describe.
            
    :type StepId: string
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


def list_bootstrap_actions(ClusterId=None, Marker=None):
    """
    :param ClusterId: [REQUIRED]
            The cluster identifier for the bootstrap actions to list .
            
    :type ClusterId: string
    :param Marker: The pagination token that indicates the next set of results to retrieve.
    :type Marker: string
    """
    pass


def list_clusters(CreatedAfter=None, CreatedBefore=None, ClusterStates=None, Marker=None):
    """
    :param CreatedAfter: The creation date and time beginning value filter for listing clusters .
    :type CreatedAfter: datetime
    :param CreatedBefore: The creation date and time end value filter for listing clusters .
    :type CreatedBefore: datetime
    :param ClusterStates: The cluster state filters to apply when listing clusters.
            (string) --
            
    :type ClusterStates: list
    :param Marker: The pagination token that indicates the next set of results to retrieve.
    :type Marker: string
    """
    pass


def list_instance_groups(ClusterId=None, Marker=None):
    """
    :param ClusterId: [REQUIRED]
            The identifier of the cluster for which to list the instance groups.
            
    :type ClusterId: string
    :param Marker: The pagination token that indicates the next set of results to retrieve.
    :type Marker: string
    """
    pass


def list_instances(ClusterId=None, InstanceGroupId=None, InstanceGroupTypes=None, InstanceStates=None, Marker=None):
    """
    :param ClusterId: [REQUIRED]
            The identifier of the cluster for which to list the instances.
            
    :type ClusterId: string
    :param InstanceGroupId: The identifier of the instance group for which to list the instances.
    :type InstanceGroupId: string
    :param InstanceGroupTypes: The type of instance group for which to list the instances.
            (string) --
            
    :type InstanceGroupTypes: list
    :param InstanceStates: A list of instance states that will filter the instances returned with this request.
            (string) --
            
    :type InstanceStates: list
    :param Marker: The pagination token that indicates the next set of results to retrieve.
    :type Marker: string
    """
    pass


def list_security_configurations(Marker=None):
    """
    :param Marker: The pagination token that indicates the set of results to retrieve.
            Return typedict
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
            
            
    :type Marker: string
    """
    pass


def list_steps(ClusterId=None, StepStates=None, StepIds=None, Marker=None):
    """
    :param ClusterId: [REQUIRED]
            The identifier of the cluster for which to list the steps.
            
    :type ClusterId: string
    :param StepStates: The filter to limit the step list based on certain states.
            (string) --
            
    :type StepStates: list
    :param StepIds: The filter to limit the step list based on the identifier of the steps.
            (string) --
            
    :type StepIds: list
    :param Marker: The pagination token that indicates the next set of results to retrieve.
    :type Marker: string
    """
    pass


def modify_instance_groups(InstanceGroups=None):
    """
    :param InstanceGroups: Instance groups to change.
            (dict) --Modify an instance group size.
            InstanceGroupId (string) -- [REQUIRED]Unique ID of the instance group to expand or shrink.
            InstanceCount (integer) --Target size for the instance group.
            EC2InstanceIdsToTerminate (list) --The EC2 InstanceIds to terminate. Once you terminate the instances, the instance group will not return to its original requested size.
            (string) --
            ShrinkPolicy (dict) --Policy for customizing shrink operations.
            DecommissionTimeout (integer) --The desired timeout for decommissioning an instance. Overrides the default YARN decommissioning timeout.
            InstanceResizePolicy (dict) --Custom policy for requesting termination protection or termination of specific instances when shrinking an instance group.
            InstancesToTerminate (list) --Specific list of instances to be terminated when shrinking an instance group.
            (string) --
            InstancesToProtect (list) --Specific list of instances to be protected when shrinking an instance group.
            (string) --
            InstanceTerminationTimeout (integer) --Decommissioning timeout override for the specific list of instances to be terminated.
            
            
            ReturnsNone
            
    :type InstanceGroups: list
    """
    pass


def remove_tags(ResourceId=None, TagKeys=None):
    """
    :param ResourceId: [REQUIRED]
            The Amazon EMR resource identifier from which tags will be removed. This value must be a cluster identifier.
            
    :type ResourceId: string
    :param TagKeys: [REQUIRED]
            A list of tag keys to remove from a resource.
            (string) --
            
    :type TagKeys: list
    """
    pass


def run_job_flow(Name=None, LogUri=None, AdditionalInfo=None, AmiVersion=None, ReleaseLabel=None, Instances=None,
                 Steps=None, BootstrapActions=None, SupportedProducts=None, NewSupportedProducts=None,
                 Applications=None, Configurations=None, VisibleToAllUsers=None, JobFlowRole=None, ServiceRole=None,
                 Tags=None, SecurityConfiguration=None):
    """
    :param Name: [REQUIRED]
            The name of the job flow.
            
    :type Name: string
    :param LogUri: The location in Amazon S3 to write the log files of the job flow. If a value is not provided, logs are not created.
    :type LogUri: string
    :param AdditionalInfo: A JSON string for selecting additional features.
    :type AdditionalInfo: string
    :param AmiVersion: 
            Note
            For Amazon EMR releases 3.x and 2.x. For Amazon EMR releases 4.x and greater, use ReleaseLabel.
            The version of the Amazon Machine Image (AMI) to use when launching Amazon EC2 instances in the job flow. The following values are valid:
            The version number of the AMI to use, for example, '2.0.'
            If the AMI supports multiple versions of Hadoop (for example, AMI 1.0 supports both Hadoop 0.18 and 0.20) you can use the JobFlowInstancesConfig HadoopVersion parameter to modify the version of Hadoop from the defaults shown above.
            For details about the AMI versions currently supported by Amazon Elastic MapReduce, go to AMI Versions Supported in Elastic MapReduce in the Amazon Elastic MapReduce Developer's Guide.
            
    :type AmiVersion: string
    :param ReleaseLabel: 
            Note
            Amazon EMR releases 4.x or later.
            The release label for the Amazon EMR release. For Amazon EMR 3.x and 2.x AMIs, use amiVersion instead instead of ReleaseLabel.
            
    :type ReleaseLabel: string
    :param Instances: [REQUIRED]
            A specification of the number and type of Amazon EC2 instances on which to run the job flow.
            MasterInstanceType (string) --The EC2 instance type of the master node.
            SlaveInstanceType (string) --The EC2 instance type of the slave nodes.
            InstanceCount (integer) --The number of Amazon EC2 instances used to execute the job flow.
            InstanceGroups (list) --Configuration for the job flow's instance groups.
            (dict) --Configuration defining a new instance group.
            Name (string) --Friendly name given to the instance group.
            Market (string) --Market type of the Amazon EC2 instances used to create a cluster node.
            InstanceRole (string) -- [REQUIRED]The role of the instance group in the cluster.
            BidPrice (string) --Bid price for each Amazon EC2 instance in the instance group when launching nodes as Spot Instances, expressed in USD.
            InstanceType (string) -- [REQUIRED]The Amazon EC2 instance type for all instances in the instance group.
            InstanceCount (integer) -- [REQUIRED]Target number of instances for the instance group.
            Configurations (list) --
            Note
            Amazon EMR releases 4.x or later.
            The list of configurations supplied for an EMR cluster instance group. You can specify a separate configuration for each instance group (master, core, and task).
            (dict) --
            Note
            Amazon EMR releases 4.x or later.
            Specifies a hardware and software configuration of the EMR cluster. This includes configurations for applications and software bundled with Amazon EMR. The Configuration object is a JSON object which is defined by a classification and a set of properties. Configurations can be nested, so a configuration may have its own Configuration objects listed.
            Classification (string) --The classification of a configuration. For more information see, Amazon EMR Configurations .
            Configurations (list) --A list of configurations you apply to this configuration object.
            Properties (dict) --A set of properties supplied to the Configuration object.
            (string) --
            (string) --
            
            
            EbsConfiguration (dict) --EBS configurations that will be attached to each Amazon EC2 instance in the instance group.
            EbsBlockDeviceConfigs (list) --
            (dict) --Configuration of requested EBS block device associated with the instance group with count of volumes that will be associated to every instance.
            VolumeSpecification (dict) -- [REQUIRED]EBS volume specifications such as volume type, IOPS, and size(GiB) that will be requested for the EBS volume attached to an EC2 instance in the cluster.
            VolumeType (string) -- [REQUIRED]The volume type. Volume types supported are gp2, io1, standard.
            Iops (integer) --The number of I/O operations per second (IOPS) that the volume supports.
            SizeInGB (integer) -- [REQUIRED]The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the volume type is EBS-optimized, the minimum value is 10.
            VolumesPerInstance (integer) --Number of EBS volumes with specific volume configuration, that will be associated with every instance in the instance group
            
            EbsOptimized (boolean) --
            
            Ec2KeyName (string) --The name of the Amazon EC2 key pair that can be used to ssh to the master node as the user called 'hadoop.'
            Placement (dict) --The Availability Zone the job flow will run in.
            AvailabilityZone (string) -- [REQUIRED]The Amazon EC2 Availability Zone for the job flow.
            KeepJobFlowAliveWhenNoSteps (boolean) --Specifies whether the job flow should be kept alive after completing all steps.
            TerminationProtected (boolean) --Specifies whether to lock the job flow to prevent the Amazon EC2 instances from being terminated by API call, user intervention, or in the event of a job flow error.
            HadoopVersion (string) --The Hadoop version for the job flow. Valid inputs are '0.18' (deprecated), '0.20' (deprecated), '0.20.205' (deprecated), '1.0.3', '2.2.0', or '2.4.0'. If you do not set this value, the default of 0.18 is used, unless the AmiVersion parameter is set in the RunJobFlow call, in which case the default version of Hadoop for that AMI version is used.
            Ec2SubnetId (string) --To launch the job flow in Amazon Virtual Private Cloud (Amazon VPC), set this parameter to the identifier of the Amazon VPC subnet where you want the job flow to launch. If you do not specify this value, the job flow is launched in the normal Amazon Web Services cloud, outside of an Amazon VPC.
            Amazon VPC currently does not support cluster compute quadruple extra large (cc1.4xlarge) instances. Thus you cannot specify the cc1.4xlarge instance type for nodes of a job flow launched in a Amazon VPC.
            EmrManagedMasterSecurityGroup (string) --The identifier of the Amazon EC2 security group for the master node.
            EmrManagedSlaveSecurityGroup (string) --The identifier of the Amazon EC2 security group for the slave nodes.
            ServiceAccessSecurityGroup (string) --The identifier of the Amazon EC2 security group for the Amazon EMR service to access clusters in VPC private subnets.
            AdditionalMasterSecurityGroups (list) --A list of additional Amazon EC2 security group IDs for the master node.
            (string) --
            AdditionalSlaveSecurityGroups (list) --A list of additional Amazon EC2 security group IDs for the slave nodes.
            (string) --
            
    :type Instances: dict
    :param Steps: A list of steps to be executed by the job flow.
            (dict) --Specification of a job flow step.
            Name (string) -- [REQUIRED]The name of the job flow step.
            ActionOnFailure (string) --The action to take if the job flow step fails.
            HadoopJarStep (dict) -- [REQUIRED]The JAR file used for the job flow step.
            Properties (list) --A list of Java properties that are set when the step runs. You can use these properties to pass key value pairs to your main function.
            (dict) --A key value pair.
            Key (string) --The unique identifier of a key value pair.
            Value (string) --The value part of the identified key.
            
            Jar (string) -- [REQUIRED]A path to a JAR file run during the step.
            MainClass (string) --The name of the main class in the specified Java file. If not specified, the JAR file should specify a Main-Class in its manifest file.
            Args (list) --A list of command line arguments passed to the JAR file's main function when executed.
            (string) --
            
            
    :type Steps: list
    :param BootstrapActions: A list of bootstrap actions that will be run before Hadoop is started on the cluster nodes.
            (dict) --
            Name (string) -- [REQUIRED]
            ScriptBootstrapAction (dict) -- [REQUIRED]
            Path (string) -- [REQUIRED]
            Args (list) --
            (string) --
            
            
    :type BootstrapActions: list
    :param SupportedProducts: 
            Note
            For Amazon EMR releases 3.x and 2.x. For Amazon EMR releases 4.x and greater, use Applications.
            A list of strings that indicates third-party software to use with the job flow. For more information, go to Use Third Party Applications with Amazon EMR . Currently supported values are:
            'mapr-m3' - launch the job flow using MapR M3 Edition.
            'mapr-m5' - launch the job flow using MapR M5 Edition.
            (string) --
            
    :type SupportedProducts: list
    :param NewSupportedProducts: 
            Note
            For Amazon EMR releases 3.x and 2.x. For Amazon EMR releases 4.x and greater, use Applications.
            A list of strings that indicates third-party software to use with the job flow that accepts a user argument list. EMR accepts and forwards the argument list to the corresponding installation script as bootstrap action arguments. For more information, see Launch a Job Flow on the MapR Distribution for Hadoop . Currently supported values are:
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
            
            
    :type NewSupportedProducts: list
    :param Applications: 
            Note
            Amazon EMR releases 4.x or later.
            A list of applications for the cluster. Valid values are: 'Hadoop', 'Hive', 'Mahout', 'Pig', and 'Spark.' They are case insensitive.
            (dict) --An application is any Amazon or third-party software that you can add to the cluster. This structure contains a list of strings that indicates the software to use with the cluster and accepts a user argument list. Amazon EMR accepts and forwards the argument list to the corresponding installation script as bootstrap action argument. For more information, see Launch a Job Flow on the MapR Distribution for Hadoop . Currently supported values are:
            'mapr-m3' - launch the job flow using MapR M3 Edition.
            'mapr-m5' - launch the job flow using MapR M5 Edition.
            'mapr' with the user arguments specifying '--edition,m3' or '--edition,m5' - launch the job flow using MapR M3 or M5 Edition, respectively.
            Note
            In Amazon EMR releases 4.0 and greater, the only accepted parameter is the application name. To pass arguments to applications, you supply a configuration for each application.
            Name (string) --The name of the application.
            Version (string) --The version of the application.
            Args (list) --Arguments for Amazon EMR to pass to the application.
            (string) --
            AdditionalInfo (dict) --This option is for advanced users only. This is meta information about third-party applications that third-party vendors use for testing purposes.
            (string) --
            (string) --
            
            
    :type Applications: list
    :param Configurations: 
            Note
            Amazon EMR releases 4.x or later.
            The list of configurations supplied for the EMR cluster you are creating.
            (dict) --
            Note
            Amazon EMR releases 4.x or later.
            Specifies a hardware and software configuration of the EMR cluster. This includes configurations for applications and software bundled with Amazon EMR. The Configuration object is a JSON object which is defined by a classification and a set of properties. Configurations can be nested, so a configuration may have its own Configuration objects listed.
            Classification (string) --The classification of a configuration. For more information see, Amazon EMR Configurations .
            Configurations (list) --A list of configurations you apply to this configuration object.
            Properties (dict) --A set of properties supplied to the Configuration object.
            (string) --
            (string) --
            
            
    :type Configurations: list
    :param VisibleToAllUsers: Whether the job flow is visible to all IAM users of the AWS account associated with the job flow. If this value is set to true , all IAM users of that AWS account can view and (if they have the proper policy permissions set) manage the job flow. If it is set to false , only the IAM user that created the job flow can view and manage it.
    :type VisibleToAllUsers: boolean
    :param JobFlowRole: Also called instance profile and EC2 role. An IAM role for an EMR cluster. The EC2 instances of the cluster assume this role. The default role is EMR_EC2_DefaultRole . In order to use the default role, you must have already created it using the CLI or console.
    :type JobFlowRole: string
    :param ServiceRole: The IAM role that will be assumed by the Amazon EMR service to access AWS resources on your behalf.
    :type ServiceRole: string
    :param Tags: A list of tags to associate with a cluster and propagate to Amazon EC2 instances.
            (dict) --A key/value pair containing user-defined metadata that you can associate with an Amazon EMR resource. Tags make it easier to associate clusters in various ways, such as grouping clusters to track your Amazon EMR resource allocation costs. For more information, see Tagging Amazon EMR Resources .
            Key (string) --A user-defined key, which is the minimum required information for a valid tag. For more information, see Tagging Amazon EMR Resources .
            Value (string) --A user-defined value, which is optional in a tag. For more information, see Tagging Amazon EMR Resources .
            
            
    :type Tags: list
    :param SecurityConfiguration: The name of a security configuration to apply to the cluster.
    :type SecurityConfiguration: string
    """
    pass


def set_termination_protection(JobFlowIds=None, TerminationProtected=None):
    """
    :param JobFlowIds: [REQUIRED]
            A list of strings that uniquely identify the job flows to protect. This identifier is returned by RunJobFlow and can also be obtained from DescribeJobFlows .
            (string) --
            
    :type JobFlowIds: list
    :param TerminationProtected: [REQUIRED]
            A Boolean that indicates whether to protect the job flow and prevent the Amazon EC2 instances in the cluster from shutting down due to API calls, user intervention, or job-flow error.
            
    :type TerminationProtected: boolean
    """
    pass


def set_visible_to_all_users(JobFlowIds=None, VisibleToAllUsers=None):
    """
    :param JobFlowIds: [REQUIRED]
            Identifiers of the job flows to receive the new visibility setting.
            (string) --
            
    :type JobFlowIds: list
    :param VisibleToAllUsers: [REQUIRED]
            Whether the specified job flows are visible to all IAM users of the AWS account associated with the job flow. If this value is set to True, all IAM users of that AWS account can view and, if they have the proper IAM policy permissions set, manage the job flows. If it is set to False, only the IAM user that created a job flow can view and manage it.
            
    :type VisibleToAllUsers: boolean
    """
    pass


def terminate_job_flows(JobFlowIds=None):
    """
    :param JobFlowIds: [REQUIRED]
            A list of job flows to be shutdown.
            (string) --
            ReturnsNone
            
    :type JobFlowIds: list
    """
    pass
