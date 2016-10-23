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


def assign_instance(InstanceId=None, LayerIds=None):
    """
    :param InstanceId: [REQUIRED]
            The instance ID.
            
    :type InstanceId: string
    :param LayerIds: [REQUIRED]
            The layer ID, which must correspond to a custom layer. You cannot assign a registered instance to a built-in layer.
            (string) --
            
    :type LayerIds: list
    """
    pass


def assign_volume(VolumeId=None, InstanceId=None):
    """
    :param VolumeId: [REQUIRED]
            The volume ID.
            
    :type VolumeId: string
    :param InstanceId: The instance ID.
    :type InstanceId: string
    """
    pass


def associate_elastic_ip(ElasticIp=None, InstanceId=None):
    """
    :param ElasticIp: [REQUIRED]
            The Elastic IP address.
            
    :type ElasticIp: string
    :param InstanceId: The instance ID.
    :type InstanceId: string
    """
    pass


def attach_elastic_load_balancer(ElasticLoadBalancerName=None, LayerId=None):
    """
    :param ElasticLoadBalancerName: [REQUIRED]
            The Elastic Load Balancing instance's name.
            
    :type ElasticLoadBalancerName: string
    :param LayerId: [REQUIRED]
            The ID of the layer that the Elastic Load Balancing instance is to be attached to.
            
    :type LayerId: string
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


def clone_stack(SourceStackId=None, Name=None, Region=None, VpcId=None, Attributes=None, ServiceRoleArn=None,
                DefaultInstanceProfileArn=None, DefaultOs=None, HostnameTheme=None, DefaultAvailabilityZone=None,
                DefaultSubnetId=None, CustomJson=None, ConfigurationManager=None, ChefConfiguration=None,
                UseCustomCookbooks=None, UseOpsworksSecurityGroups=None, CustomCookbooksSource=None,
                DefaultSshKeyName=None, ClonePermissions=None, CloneAppIds=None, DefaultRootDeviceType=None,
                AgentVersion=None):
    """
    :param SourceStackId: [REQUIRED]
            The source stack ID.
            
    :type SourceStackId: string
    :param Name: The cloned stack name.
    :type Name: string
    :param Region: The cloned stack AWS region, such as 'ap-northeast-2'. For more information about AWS regions, see Regions and Endpoints .
    :type Region: string
    :param VpcId: The ID of the VPC that the cloned stack is to be launched into. It must be in the specified region. All instances are launched into this VPC, and you cannot change the ID later.
            If your account supports EC2 Classic, the default value is no VPC.
            If your account does not support EC2 Classic, the default value is the default VPC for the specified region.
            If the VPC ID corresponds to a default VPC and you have specified either the DefaultAvailabilityZone or the DefaultSubnetId parameter only, AWS OpsWorks infers the value of the other parameter. If you specify neither parameter, AWS OpsWorks sets these parameters to the first valid Availability Zone for the specified region and the corresponding default VPC subnet ID, respectively.
            If you specify a nondefault VPC ID, note the following:
            It must belong to a VPC in your account that is in the specified region.
            You must specify a value for DefaultSubnetId .
            For more information on how to use AWS OpsWorks with a VPC, see Running a Stack in a VPC . For more information on default VPC and EC2 Classic, see Supported Platforms .
            
    :type VpcId: string
    :param Attributes: A list of stack attributes and values as key/value pairs to be added to the cloned stack.
            (string) --
            (string) --
            
    :type Attributes: dict
    :param ServiceRoleArn: [REQUIRED]
            The stack AWS Identity and Access Management (IAM) role, which allows AWS OpsWorks to work with AWS resources on your behalf. You must set this parameter to the Amazon Resource Name (ARN) for an existing IAM role. If you create a stack by using the AWS OpsWorks console, it creates the role for you. You can obtain an existing stack's IAM ARN programmatically by calling DescribePermissions . For more information about IAM ARNs, see Using Identifiers .
            Note
            You must set this parameter to a valid service role ARN or the action will fail; there is no default value. You can specify the source stack's service role ARN, if you prefer, but you must do so explicitly.
            
    :type ServiceRoleArn: string
    :param DefaultInstanceProfileArn: The Amazon Resource Name (ARN) of an IAM profile that is the default profile for all of the stack's EC2 instances. For more information about IAM ARNs, see Using Identifiers .
    :type DefaultInstanceProfileArn: string
    :param DefaultOs: The stack's operating system, which must be set to one of the following.
            A supported Linux operating system: An Amazon Linux version, such as Amazon Linux 2016.03 , Amazon Linux 2015.09 , or Amazon Linux 2015.03 .
            A supported Ubuntu operating system, such as Ubuntu 16.04 LTS , Ubuntu 14.04 LTS , or Ubuntu 12.04 LTS .
            CentOS 7
            Red Hat Enterprise Linux 7
            Microsoft Windows Server 2012 R2 Base , Microsoft Windows Server 2012 R2 with SQL Server Express , Microsoft Windows Server 2012 R2 with SQL Server Standard , or Microsoft Windows Server 2012 R2 with SQL Server Web .
            A custom AMI: Custom . You specify the custom AMI you want to use when you create instances. For more information on how to use custom AMIs with OpsWorks, see Using Custom AMIs .
            The default option is the parent stack's operating system. For more information on the supported operating systems, see AWS OpsWorks Operating Systems .
            Note
            You can specify a different Linux operating system for the cloned stack, but you cannot change from Linux to Windows or Windows to Linux.
            
    :type DefaultOs: string
    :param HostnameTheme: The stack's host name theme, with spaces are replaced by underscores. The theme is used to generate host names for the stack's instances. By default, HostnameTheme is set to Layer_Dependent , which creates host names by appending integers to the layer's short name. The other themes are:
            Baked_Goods
            Clouds
            Europe_Cities
            Fruits
            Greek_Deities
            Legendary_creatures_from_Japan
            Planets_and_Moons
            Roman_Deities
            Scottish_Islands
            US_Cities
            Wild_Cats
            To obtain a generated host name, call GetHostNameSuggestion , which returns a host name based on the current theme.
            
    :type HostnameTheme: string
    :param DefaultAvailabilityZone: The cloned stack's default Availability Zone, which must be in the specified region. For more information, see Regions and Endpoints . If you also specify a value for DefaultSubnetId , the subnet must be in the same zone. For more information, see the VpcId parameter description.
    :type DefaultAvailabilityZone: string
    :param DefaultSubnetId: The stack's default VPC subnet ID. This parameter is required if you specify a value for the VpcId parameter. All instances are launched into this subnet unless you specify otherwise when you create the instance. If you also specify a value for DefaultAvailabilityZone , the subnet must be in that zone. For information on default values and when this parameter is required, see the VpcId parameter description.
    :type DefaultSubnetId: string
    :param CustomJson: A string that contains user-defined, custom JSON. It is used to override the corresponding default stack configuration JSON values. The string should be in the following format:
            '{\'key1\': \'value1\', \'key2\': \'value2\',...}'
            For more information on custom JSON, see Use Custom JSON to Modify the Stack Configuration Attributes
            
    :type CustomJson: string
    :param ConfigurationManager: The configuration manager. When you clone a stack we recommend that you use the configuration manager to specify the Chef version: 12, 11.10, or 11.4 for Linux stacks, or 12.2 for Windows stacks. The default value for Linux stacks is currently 12.
            Name (string) --The name. This parameter must be set to 'Chef'.
            Version (string) --The Chef version. This parameter must be set to 12, 11.10, or 11.4 for Linux stacks, and to 12.2 for Windows stacks. The default value for Linux stacks is 11.4.
            
    :type ConfigurationManager: dict
    :param ChefConfiguration: A ChefConfiguration object that specifies whether to enable Berkshelf and the Berkshelf version on Chef 11.10 stacks. For more information, see Create a New Stack .
            ManageBerkshelf (boolean) --Whether to enable Berkshelf.
            BerkshelfVersion (string) --The Berkshelf version.
            
    :type ChefConfiguration: dict
    :param UseCustomCookbooks: Whether to use custom cookbooks.
    :type UseCustomCookbooks: boolean
    :param UseOpsworksSecurityGroups: Whether to associate the AWS OpsWorks built-in security groups with the stack's layers.
            AWS OpsWorks provides a standard set of built-in security groups, one for each layer, which are associated with layers by default. With UseOpsworksSecurityGroups you can instead provide your own custom security groups. UseOpsworksSecurityGroups has the following settings:
            True - AWS OpsWorks automatically associates the appropriate built-in security group with each layer (default setting). You can associate additional security groups with a layer after you create it but you cannot delete the built-in security group.
            False - AWS OpsWorks does not associate built-in security groups with layers. You must create appropriate Amazon Elastic Compute Cloud (Amazon EC2) security groups and associate a security group with each layer that you create. However, you can still manually associate a built-in security group with a layer on creation; custom security groups are required only for those layers that need custom settings.
            For more information, see Create a New Stack .
            
    :type UseOpsworksSecurityGroups: boolean
    :param CustomCookbooksSource: Contains the information required to retrieve an app or cookbook from a repository. For more information, see Creating Apps or Custom Recipes and Cookbooks .
            Type (string) --The repository type.
            Url (string) --The source URL.
            Username (string) --This parameter depends on the repository type.
            For Amazon S3 bundles, set Username to the appropriate IAM access key ID.
            For HTTP bundles, Git repositories, and Subversion repositories, set Username to the user name.
            Password (string) --When included in a request, the parameter depends on the repository type.
            For Amazon S3 bundles, set Password to the appropriate IAM secret access key.
            For HTTP bundles and Subversion repositories, set Password to the password.
            For more information on how to safely handle IAM credentials, see http://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html .
            In responses, AWS OpsWorks returns *****FILTERED***** instead of the actual value.
            SshKey (string) --In requests, the repository's SSH key.
            In responses, AWS OpsWorks returns *****FILTERED***** instead of the actual value.
            Revision (string) --The application's version. AWS OpsWorks enables you to easily deploy new versions of an application. One of the simplest approaches is to have branches or revisions in your repository that represent different versions that can potentially be deployed.
            
    :type CustomCookbooksSource: dict
    :param DefaultSshKeyName: A default Amazon EC2 key pair name. The default value is none. If you specify a key pair name, AWS OpsWorks installs the public key on the instance and you can use the private key with an SSH client to log in to the instance. For more information, see Using SSH to Communicate with an Instance and Managing SSH Access . You can override this setting by specifying a different key pair, or no key pair, when you create an instance .
    :type DefaultSshKeyName: string
    :param ClonePermissions: Whether to clone the source stack's permissions.
    :type ClonePermissions: boolean
    :param CloneAppIds: A list of source stack app IDs to be included in the cloned stack.
            (string) --
            
    :type CloneAppIds: list
    :param DefaultRootDeviceType: The default root device type. This value is used by default for all instances in the cloned stack, but you can override it when you create an instance. For more information, see Storage for the Root Device .
    :type DefaultRootDeviceType: string
    :param AgentVersion: The default AWS OpsWorks agent version. You have the following options:
            Auto-update - Set this parameter to LATEST . AWS OpsWorks automatically installs new agent versions on the stack's instances as soon as they are available.
            Fixed version - Set this parameter to your preferred agent version. To update the agent version, you must edit the stack configuration and specify a new version. AWS OpsWorks then automatically installs that version on the stack's instances.
            The default setting is LATEST . To specify an agent version, you must use the complete version number, not the abbreviated number shown on the console. For a list of available agent version numbers, call DescribeAgentVersions .
            Note
            You can also specify an agent version when you create or update an instance, which overrides the stack's default setting.
            
    :type AgentVersion: string
    """
    pass


def create_app(StackId=None, Shortname=None, Name=None, Description=None, DataSources=None, Type=None, AppSource=None,
               Domains=None, EnableSsl=None, SslConfiguration=None, Attributes=None, Environment=None):
    """
    :param StackId: [REQUIRED]
            The stack ID.
            
    :type StackId: string
    :param Shortname: The app's short name.
    :type Shortname: string
    :param Name: [REQUIRED]
            The app name.
            
    :type Name: string
    :param Description: A description of the app.
    :type Description: string
    :param DataSources: The app's data source.
            (dict) --Describes an app's data source.
            Type (string) --The data source's type, AutoSelectOpsworksMysqlInstance , OpsworksMysqlInstance , or RdsDbInstance .
            Arn (string) --The data source's ARN.
            DatabaseName (string) --The database name.
            
            
    :type DataSources: list
    :param Type: [REQUIRED]
            The app type. Each supported type is associated with a particular layer. For example, PHP applications are associated with a PHP layer. AWS OpsWorks deploys an application to those instances that are members of the corresponding layer. If your app isn't one of the standard types, or you prefer to implement your own Deploy recipes, specify other .
            
    :type Type: string
    :param AppSource: A Source object that specifies the app repository.
            Type (string) --The repository type.
            Url (string) --The source URL.
            Username (string) --This parameter depends on the repository type.
            For Amazon S3 bundles, set Username to the appropriate IAM access key ID.
            For HTTP bundles, Git repositories, and Subversion repositories, set Username to the user name.
            Password (string) --When included in a request, the parameter depends on the repository type.
            For Amazon S3 bundles, set Password to the appropriate IAM secret access key.
            For HTTP bundles and Subversion repositories, set Password to the password.
            For more information on how to safely handle IAM credentials, see http://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html .
            In responses, AWS OpsWorks returns *****FILTERED***** instead of the actual value.
            SshKey (string) --In requests, the repository's SSH key.
            In responses, AWS OpsWorks returns *****FILTERED***** instead of the actual value.
            Revision (string) --The application's version. AWS OpsWorks enables you to easily deploy new versions of an application. One of the simplest approaches is to have branches or revisions in your repository that represent different versions that can potentially be deployed.
            
    :type AppSource: dict
    :param Domains: The app virtual host settings, with multiple domains separated by commas. For example: 'www.example.com, example.com'
            (string) --
            
    :type Domains: list
    :param EnableSsl: Whether to enable SSL for the app.
    :type EnableSsl: boolean
    :param SslConfiguration: An SslConfiguration object with the SSL configuration.
            Certificate (string) -- [REQUIRED]The contents of the certificate's domain.crt file.
            PrivateKey (string) -- [REQUIRED]The private key; the contents of the certificate's domain.kex file.
            Chain (string) --Optional. Can be used to specify an intermediate certificate authority key or client authentication.
            
    :type SslConfiguration: dict
    :param Attributes: One or more user-defined key/value pairs to be added to the stack attributes.
            (string) --
            (string) --
            
    :type Attributes: dict
    :param Environment: An array of EnvironmentVariable objects that specify environment variables to be associated with the app. After you deploy the app, these variables are defined on the associated app server instance. For more information, see Environment Variables .
            There is no specific limit on the number of environment variables. However, the size of the associated data structure - which includes the variables' names, values, and protected flag values - cannot exceed 10 KB (10240 Bytes). This limit should accommodate most if not all use cases. Exceeding it will cause an exception with the message, 'Environment: is too large (maximum is 10KB).'
            Note
            This parameter is supported only by Chef 11.10 stacks. If you have specified one or more environment variables, you cannot modify the stack's Chef version.
            (dict) --Represents an app's environment variable.
            Key (string) -- [REQUIRED](Required) The environment variable's name, which can consist of up to 64 characters and must be specified. The name can contain upper- and lowercase letters, numbers, and underscores (_), but it must start with a letter or underscore.
            Value (string) -- [REQUIRED](Optional) The environment variable's value, which can be left empty. If you specify a value, it can contain up to 256 characters, which must all be printable.
            Secure (boolean) --(Optional) Whether the variable's value will be returned by the DescribeApps action. To conceal an environment variable's value, set Secure to true . DescribeApps then returns *****FILTERED***** instead of the actual value. The default value for Secure is false .
            
            
    :type Environment: list
    """
    pass


def create_deployment(StackId=None, AppId=None, InstanceIds=None, LayerIds=None, Command=None, Comment=None,
                      CustomJson=None):
    """
    :param StackId: [REQUIRED]
            The stack ID.
            
    :type StackId: string
    :param AppId: The app ID. This parameter is required for app deployments, but not for other deployment commands.
    :type AppId: string
    :param InstanceIds: The instance IDs for the deployment targets.
            (string) --
            
    :type InstanceIds: list
    :param LayerIds: The layer IDs for the deployment targets.
            (string) --
            
    :type LayerIds: list
    :param Command: [REQUIRED]
            A DeploymentCommand object that specifies the deployment command and any associated arguments.
            Name (string) -- [REQUIRED]Specifies the operation. You can specify only one command.
            For stacks, the following commands are available:
            execute_recipes : Execute one or more recipes. To specify the recipes, set an Args parameter named recipes to the list of recipes to be executed. For example, to execute phpapp::appsetup , set Args to {'recipes':['phpapp::appsetup']} .
            install_dependencies : Install the stack's dependencies.
            update_custom_cookbooks : Update the stack's custom cookbooks.
            update_dependencies : Update the stack's dependencies.
            Note
            The update_dependencies and install_dependencies commands are supported only for Linux instances. You can run the commands successfully on Windows instances, but they do nothing.
            For apps, the following commands are available:
            deploy : Deploy an app. Ruby on Rails apps have an optional Args parameter named migrate . Set Args to {'migrate':['true']} to migrate the database. The default setting is {'migrate':['false']}.
            rollback Roll the app back to the previous version. When you update an app, AWS OpsWorks stores the previous version, up to a maximum of five versions. You can use this command to roll an app back as many as four versions.
            start : Start the app's web or application server.
            stop : Stop the app's web or application server.
            restart : Restart the app's web or application server.
            undeploy : Undeploy the app.
            Args (dict) --The arguments of those commands that take arguments. It should be set to a JSON object with the following format:
            {'arg_name1' : ['value1', 'value2', ...], 'arg_name2' : ['value1', 'value2', ...], ...}
            The update_dependencies command takes two arguments:
            upgrade_os_to - Specifies the desired Amazon Linux version for instances whose OS you want to upgrade, such as Amazon Linux 2014.09 . You must also set the allow_reboot argument to true.
            allow_reboot - Specifies whether to allow AWS OpsWorks to reboot the instances if necessary, after installing the updates. This argument can be set to either true or false . The default value is false .
            For example, to upgrade an instance to Amazon Linux 2014.09, set Args to the following.
            { 'upgrade_os_to':['Amazon Linux 2014.09'], 'allow_reboot':['true'] }
            (string) --
            (list) --
            (string) --
            
            
    :type Command: dict
    :param Comment: A user-defined comment.
    :type Comment: string
    :param CustomJson: A string that contains user-defined, custom JSON. It is used to override the corresponding default stack configuration JSON values. The string should be in the following format:
            '{\'key1\': \'value1\', \'key2\': \'value2\',...}'
            For more information on custom JSON, see Use Custom JSON to Modify the Stack Configuration Attributes .
            
    :type CustomJson: string
    """
    pass


def create_instance(StackId=None, LayerIds=None, InstanceType=None, AutoScalingType=None, Hostname=None, Os=None,
                    AmiId=None, SshKeyName=None, AvailabilityZone=None, VirtualizationType=None, SubnetId=None,
                    Architecture=None, RootDeviceType=None, BlockDeviceMappings=None, InstallUpdatesOnBoot=None,
                    EbsOptimized=None, AgentVersion=None, Tenancy=None):
    """
    :param StackId: [REQUIRED]
            The stack ID.
            
    :type StackId: string
    :param LayerIds: [REQUIRED]
            An array that contains the instance's layer IDs.
            (string) --
            
    :type LayerIds: list
    :param InstanceType: [REQUIRED]
            The instance type, such as t2.micro . For a list of supported instance types, open the stack in the console, choose Instances , and choose + Instance . The Size list contains the currently supported types. For more information, see Instance Families and Types . The parameter values that you use to specify the various types are in the API Name column of the Available Instance Types table.
            
    :type InstanceType: string
    :param AutoScalingType: For load-based or time-based instances, the type. Windows stacks can use only time-based instances.
    :type AutoScalingType: string
    :param Hostname: The instance host name.
    :type Hostname: string
    :param Os: The instance's operating system, which must be set to one of the following.
            A supported Linux operating system: An Amazon Linux version, such as Amazon Linux 2016.03 , Amazon Linux 2015.09 , or Amazon Linux 2015.03 .
            A supported Ubuntu operating system, such as Ubuntu 16.04 LTS , Ubuntu 14.04 LTS , or Ubuntu 12.04 LTS .
            CentOS 7
            Red Hat Enterprise Linux 7
            A supported Windows operating system, such as Microsoft Windows Server 2012 R2 Base , Microsoft Windows Server 2012 R2 with SQL Server Express , Microsoft Windows Server 2012 R2 with SQL Server Standard , or Microsoft Windows Server 2012 R2 with SQL Server Web .
            A custom AMI: Custom .
            For more information on the supported operating systems, see AWS OpsWorks Operating Systems .
            The default option is the current Amazon Linux version. If you set this parameter to Custom , you must use the CreateInstance action's AmiId parameter to specify the custom AMI that you want to use. Block device mappings are not supported if the value is Custom . For more information on the supported operating systems, see Operating Systems For more information on how to use custom AMIs with AWS OpsWorks, see Using Custom AMIs .
            
    :type Os: string
    :param AmiId: A custom AMI ID to be used to create the instance. The AMI should be based on one of the supported operating systems. For more information, see Using Custom AMIs .
            Note
            If you specify a custom AMI, you must set Os to Custom .
            
    :type AmiId: string
    :param SshKeyName: The instance's Amazon EC2 key-pair name.
    :type SshKeyName: string
    :param AvailabilityZone: The instance Availability Zone. For more information, see Regions and Endpoints .
    :type AvailabilityZone: string
    :param VirtualizationType: The instance's virtualization type, paravirtual or hvm .
    :type VirtualizationType: string
    :param SubnetId: The ID of the instance's subnet. If the stack is running in a VPC, you can use this parameter to override the stack's default subnet ID value and direct AWS OpsWorks to launch the instance in a different subnet.
    :type SubnetId: string
    :param Architecture: The instance architecture. The default option is x86_64 . Instance types do not necessarily support both architectures. For a list of the architectures that are supported by the different instance types, see Instance Families and Types .
    :type Architecture: string
    :param RootDeviceType: The instance root device type. For more information, see Storage for the Root Device .
    :type RootDeviceType: string
    :param BlockDeviceMappings: An array of BlockDeviceMapping objects that specify the instance's block devices. For more information, see Block Device Mapping . Note that block device mappings are not supported for custom AMIs.
            (dict) --Describes a block device mapping. This data type maps directly to the Amazon EC2 BlockDeviceMapping data type.
            DeviceName (string) --The device name that is exposed to the instance, such as /dev/sdh . For the root device, you can use the explicit device name or you can set this parameter to ROOT_DEVICE and AWS OpsWorks will provide the correct device name.
            NoDevice (string) --Suppresses the specified device included in the AMI's block device mapping.
            VirtualName (string) --The virtual device name. For more information, see BlockDeviceMapping .
            Ebs (dict) --An EBSBlockDevice that defines how to configure an Amazon EBS volume when the instance is launched.
            SnapshotId (string) --The snapshot ID.
            Iops (integer) --The number of I/O operations per second (IOPS) that the volume supports. For more information, see EbsBlockDevice .
            VolumeSize (integer) --The volume size, in GiB. For more information, see EbsBlockDevice .
            VolumeType (string) --The volume type. gp2 for General Purpose (SSD) volumes, io1 for Provisioned IOPS (SSD) volumes, and standard for Magnetic volumes.
            DeleteOnTermination (boolean) --Whether the volume is deleted on instance termination.
            
            
    :type BlockDeviceMappings: list
    :param InstallUpdatesOnBoot: Whether to install operating system and package updates when the instance boots. The default value is true . To control when updates are installed, set this value to false . You must then update your instances manually by using CreateDeployment to run the update_dependencies stack command or by manually running yum (Amazon Linux) or apt-get (Ubuntu) on the instances.
            Note
            We strongly recommend using the default value of true to ensure that your instances have the latest security updates.
            
    :type InstallUpdatesOnBoot: boolean
    :param EbsOptimized: Whether to create an Amazon EBS-optimized instance.
    :type EbsOptimized: boolean
    :param AgentVersion: The default AWS OpsWorks agent version. You have the following options:
            INHERIT - Use the stack's default agent version setting.
            version_number - Use the specified agent version. This value overrides the stack's default setting. To update the agent version, edit the instance configuration and specify a new version. AWS OpsWorks then automatically installs that version on the instance.
            The default setting is INHERIT . To specify an agent version, you must use the complete version number, not the abbreviated number shown on the console. For a list of available agent version numbers, call DescribeAgentVersions .
            
    :type AgentVersion: string
    :param Tenancy: The instance's tenancy option. The default option is no tenancy, or if the instance is running in a VPC, inherit tenancy settings from the VPC. The following are valid values for this parameter: dedicated , default , or host . Because there are costs associated with changes in tenancy options, we recommend that you research tenancy options before choosing them for your instances. For more information about dedicated hosts, see Dedicated Hosts Overview and Amazon EC2 Dedicated Hosts . For more information about dedicated instances, see Dedicated Instances and Amazon EC2 Dedicated Instances .
    :type Tenancy: string
    """
    pass


def create_layer(StackId=None, Type=None, Name=None, Shortname=None, Attributes=None, CustomInstanceProfileArn=None,
                 CustomJson=None, CustomSecurityGroupIds=None, Packages=None, VolumeConfigurations=None,
                 EnableAutoHealing=None, AutoAssignElasticIps=None, AutoAssignPublicIps=None, CustomRecipes=None,
                 InstallUpdatesOnBoot=None, UseEbsOptimizedInstances=None, LifecycleEventConfiguration=None):
    """
    :param StackId: [REQUIRED]
            The layer stack ID.
            
    :type StackId: string
    :param Type: [REQUIRED]
            The layer type. A stack cannot have more than one built-in layer of the same type. It can have any number of custom layers. Built-in layers are not available in Chef 12 stacks.
            
    :type Type: string
    :param Name: [REQUIRED]
            The layer name, which is used by the console.
            
    :type Name: string
    :param Shortname: [REQUIRED]
            For custom layers only, use this parameter to specify the layer's short name, which is used internally by AWS OpsWorks and by Chef recipes. The short name is also used as the name for the directory where your app files are installed. It can have a maximum of 200 characters, which are limited to the alphanumeric characters, '-', '_', and '.'.
            The built-in layers' short names are defined by AWS OpsWorks. For more information, see the Layer Reference .
            
    :type Shortname: string
    :param Attributes: One or more user-defined key-value pairs to be added to the stack attributes.
            To create a cluster layer, set the EcsClusterArn attribute to the cluster's ARN.
            (string) --
            (string) --
            
    :type Attributes: dict
    :param CustomInstanceProfileArn: The ARN of an IAM profile to be used for the layer's EC2 instances. For more information about IAM ARNs, see Using Identifiers .
    :type CustomInstanceProfileArn: string
    :param CustomJson: A JSON-formatted string containing custom stack configuration and deployment attributes to be installed on the layer's instances. For more information, see Using Custom JSON . This feature is supported as of version 1.7.42 of the AWS CLI.
    :type CustomJson: string
    :param CustomSecurityGroupIds: An array containing the layer custom security group IDs.
            (string) --
            
    :type CustomSecurityGroupIds: list
    :param Packages: An array of Package objects that describes the layer packages.
            (string) --
            
    :type Packages: list
    :param VolumeConfigurations: A VolumeConfigurations object that describes the layer's Amazon EBS volumes.
            (dict) --Describes an Amazon EBS volume configuration.
            MountPoint (string) -- [REQUIRED]The volume mount point. For example '/dev/sdh'.
            RaidLevel (integer) --The volume RAID level .
            NumberOfDisks (integer) -- [REQUIRED]The number of disks in the volume.
            Size (integer) -- [REQUIRED]The volume size.
            VolumeType (string) --The volume type:
            standard - Magnetic
            io1 - Provisioned IOPS (SSD)
            gp2 - General Purpose (SSD)
            Iops (integer) --For PIOPS volumes, the IOPS per disk.
            
            
    :type VolumeConfigurations: list
    :param EnableAutoHealing: Whether to disable auto healing for the layer.
    :type EnableAutoHealing: boolean
    :param AutoAssignElasticIps: Whether to automatically assign an Elastic IP address to the layer's instances. For more information, see How to Edit a Layer .
    :type AutoAssignElasticIps: boolean
    :param AutoAssignPublicIps: For stacks that are running in a VPC, whether to automatically assign a public IP address to the layer's instances. For more information, see How to Edit a Layer .
    :type AutoAssignPublicIps: boolean
    :param CustomRecipes: A LayerCustomRecipes object that specifies the layer custom recipes.
            Setup (list) --An array of custom recipe names to be run following a setup event.
            (string) --
            Configure (list) --An array of custom recipe names to be run following a configure event.
            (string) --
            Deploy (list) --An array of custom recipe names to be run following a deploy event.
            (string) --
            Undeploy (list) --An array of custom recipe names to be run following a undeploy event.
            (string) --
            Shutdown (list) --An array of custom recipe names to be run following a shutdown event.
            (string) --
            
    :type CustomRecipes: dict
    :param InstallUpdatesOnBoot: Whether to install operating system and package updates when the instance boots. The default value is true . To control when updates are installed, set this value to false . You must then update your instances manually by using CreateDeployment to run the update_dependencies stack command or by manually running yum (Amazon Linux) or apt-get (Ubuntu) on the instances.
            Note
            To ensure that your instances have the latest security updates, we strongly recommend using the default value of true .
            
    :type InstallUpdatesOnBoot: boolean
    :param UseEbsOptimizedInstances: Whether to use Amazon EBS-optimized instances.
    :type UseEbsOptimizedInstances: boolean
    :param LifecycleEventConfiguration: A LifeCycleEventConfiguration object that you can use to configure the Shutdown event to specify an execution timeout and enable or disable Elastic Load Balancer connection draining.
            Shutdown (dict) --A ShutdownEventConfiguration object that specifies the Shutdown event configuration.
            ExecutionTimeout (integer) --The time, in seconds, that AWS OpsWorks will wait after triggering a Shutdown event before shutting down an instance.
            DelayUntilElbConnectionsDrained (boolean) --Whether to enable Elastic Load Balancing connection draining. For more information, see Connection Draining
            
            
    :type LifecycleEventConfiguration: dict
    """
    pass


def create_stack(Name=None, Region=None, VpcId=None, Attributes=None, ServiceRoleArn=None,
                 DefaultInstanceProfileArn=None, DefaultOs=None, HostnameTheme=None, DefaultAvailabilityZone=None,
                 DefaultSubnetId=None, CustomJson=None, ConfigurationManager=None, ChefConfiguration=None,
                 UseCustomCookbooks=None, UseOpsworksSecurityGroups=None, CustomCookbooksSource=None,
                 DefaultSshKeyName=None, DefaultRootDeviceType=None, AgentVersion=None):
    """
    :param Name: [REQUIRED]
            The stack name.
            
    :type Name: string
    :param Region: [REQUIRED]
            The stack's AWS region, such as 'ap-south-1'. For more information about Amazon regions, see Regions and Endpoints .
            
    :type Region: string
    :param VpcId: The ID of the VPC that the stack is to be launched into. The VPC must be in the stack's region. All instances are launched into this VPC. You cannot change the ID later.
            If your account supports EC2-Classic, the default value is no VPC .
            If your account does not support EC2-Classic, the default value is the default VPC for the specified region.
            If the VPC ID corresponds to a default VPC and you have specified either the DefaultAvailabilityZone or the DefaultSubnetId parameter only, AWS OpsWorks infers the value of the other parameter. If you specify neither parameter, AWS OpsWorks sets these parameters to the first valid Availability Zone for the specified region and the corresponding default VPC subnet ID, respectively.
            If you specify a nondefault VPC ID, note the following:
            It must belong to a VPC in your account that is in the specified region.
            You must specify a value for DefaultSubnetId .
            For more information on how to use AWS OpsWorks with a VPC, see Running a Stack in a VPC . For more information on default VPC and EC2-Classic, see Supported Platforms .
            
    :type VpcId: string
    :param Attributes: One or more user-defined key-value pairs to be added to the stack attributes.
            (string) --
            (string) --
            
    :type Attributes: dict
    :param ServiceRoleArn: [REQUIRED]
            The stack's AWS Identity and Access Management (IAM) role, which allows AWS OpsWorks to work with AWS resources on your behalf. You must set this parameter to the Amazon Resource Name (ARN) for an existing IAM role. For more information about IAM ARNs, see Using Identifiers .
            
    :type ServiceRoleArn: string
    :param DefaultInstanceProfileArn: [REQUIRED]
            The Amazon Resource Name (ARN) of an IAM profile that is the default profile for all of the stack's EC2 instances. For more information about IAM ARNs, see Using Identifiers .
            
    :type DefaultInstanceProfileArn: string
    :param DefaultOs: The stack's default operating system, which is installed on every instance unless you specify a different operating system when you create the instance. You can specify one of the following.
            A supported Linux operating system: An Amazon Linux version, such as Amazon Linux 2016.03 , Amazon Linux 2015.09 , or Amazon Linux 2015.03 .
            A supported Ubuntu operating system, such as Ubuntu 16.04 LTS , Ubuntu 14.04 LTS , or Ubuntu 12.04 LTS .
            CentOS 7
            Red Hat Enterprise Linux 7
            A supported Windows operating system, such as Microsoft Windows Server 2012 R2 Base , Microsoft Windows Server 2012 R2 with SQL Server Express , Microsoft Windows Server 2012 R2 with SQL Server Standard , or Microsoft Windows Server 2012 R2 with SQL Server Web .
            A custom AMI: Custom . You specify the custom AMI you want to use when you create instances. For more information, see Using Custom AMIs .
            The default option is the current Amazon Linux version. For more information on the supported operating systems, see AWS OpsWorks Operating Systems .
            
    :type DefaultOs: string
    :param HostnameTheme: The stack's host name theme, with spaces replaced by underscores. The theme is used to generate host names for the stack's instances. By default, HostnameTheme is set to Layer_Dependent , which creates host names by appending integers to the layer's short name. The other themes are:
            Baked_Goods
            Clouds
            Europe_Cities
            Fruits
            Greek_Deities
            Legendary_creatures_from_Japan
            Planets_and_Moons
            Roman_Deities
            Scottish_Islands
            US_Cities
            Wild_Cats
            To obtain a generated host name, call GetHostNameSuggestion , which returns a host name based on the current theme.
            
    :type HostnameTheme: string
    :param DefaultAvailabilityZone: The stack's default Availability Zone, which must be in the specified region. For more information, see Regions and Endpoints . If you also specify a value for DefaultSubnetId , the subnet must be in the same zone. For more information, see the VpcId parameter description.
    :type DefaultAvailabilityZone: string
    :param DefaultSubnetId: The stack's default VPC subnet ID. This parameter is required if you specify a value for the VpcId parameter. All instances are launched into this subnet unless you specify otherwise when you create the instance. If you also specify a value for DefaultAvailabilityZone , the subnet must be in that zone. For information on default values and when this parameter is required, see the VpcId parameter description.
    :type DefaultSubnetId: string
    :param CustomJson: A string that contains user-defined, custom JSON. It can be used to override the corresponding default stack configuration attribute values or to pass data to recipes. The string should be in the following format:
            '{\'key1\': \'value1\', \'key2\': \'value2\',...}'
            For more information on custom JSON, see Use Custom JSON to Modify the Stack Configuration Attributes .
            
    :type CustomJson: string
    :param ConfigurationManager: The configuration manager. When you create a stack we recommend that you use the configuration manager to specify the Chef version: 12, 11.10, or 11.4 for Linux stacks, or 12.2 for Windows stacks. The default value for Linux stacks is currently 11.4.
            Name (string) --The name. This parameter must be set to 'Chef'.
            Version (string) --The Chef version. This parameter must be set to 12, 11.10, or 11.4 for Linux stacks, and to 12.2 for Windows stacks. The default value for Linux stacks is 11.4.
            
    :type ConfigurationManager: dict
    :param ChefConfiguration: A ChefConfiguration object that specifies whether to enable Berkshelf and the Berkshelf version on Chef 11.10 stacks. For more information, see Create a New Stack .
            ManageBerkshelf (boolean) --Whether to enable Berkshelf.
            BerkshelfVersion (string) --The Berkshelf version.
            
    :type ChefConfiguration: dict
    :param UseCustomCookbooks: Whether the stack uses custom cookbooks.
    :type UseCustomCookbooks: boolean
    :param UseOpsworksSecurityGroups: Whether to associate the AWS OpsWorks built-in security groups with the stack's layers.
            AWS OpsWorks provides a standard set of built-in security groups, one for each layer, which are associated with layers by default. With UseOpsworksSecurityGroups you can instead provide your own custom security groups. UseOpsworksSecurityGroups has the following settings:
            True - AWS OpsWorks automatically associates the appropriate built-in security group with each layer (default setting). You can associate additional security groups with a layer after you create it, but you cannot delete the built-in security group.
            False - AWS OpsWorks does not associate built-in security groups with layers. You must create appropriate EC2 security groups and associate a security group with each layer that you create. However, you can still manually associate a built-in security group with a layer on creation; custom security groups are required only for those layers that need custom settings.
            For more information, see Create a New Stack .
            
    :type UseOpsworksSecurityGroups: boolean
    :param CustomCookbooksSource: Contains the information required to retrieve an app or cookbook from a repository. For more information, see Creating Apps or Custom Recipes and Cookbooks .
            Type (string) --The repository type.
            Url (string) --The source URL.
            Username (string) --This parameter depends on the repository type.
            For Amazon S3 bundles, set Username to the appropriate IAM access key ID.
            For HTTP bundles, Git repositories, and Subversion repositories, set Username to the user name.
            Password (string) --When included in a request, the parameter depends on the repository type.
            For Amazon S3 bundles, set Password to the appropriate IAM secret access key.
            For HTTP bundles and Subversion repositories, set Password to the password.
            For more information on how to safely handle IAM credentials, see http://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html .
            In responses, AWS OpsWorks returns *****FILTERED***** instead of the actual value.
            SshKey (string) --In requests, the repository's SSH key.
            In responses, AWS OpsWorks returns *****FILTERED***** instead of the actual value.
            Revision (string) --The application's version. AWS OpsWorks enables you to easily deploy new versions of an application. One of the simplest approaches is to have branches or revisions in your repository that represent different versions that can potentially be deployed.
            
    :type CustomCookbooksSource: dict
    :param DefaultSshKeyName: A default Amazon EC2 key pair name. The default value is none. If you specify a key pair name, AWS OpsWorks installs the public key on the instance and you can use the private key with an SSH client to log in to the instance. For more information, see Using SSH to Communicate with an Instance and Managing SSH Access . You can override this setting by specifying a different key pair, or no key pair, when you create an instance .
    :type DefaultSshKeyName: string
    :param DefaultRootDeviceType: The default root device type. This value is the default for all instances in the stack, but you can override it when you create an instance. The default option is instance-store . For more information, see Storage for the Root Device .
    :type DefaultRootDeviceType: string
    :param AgentVersion: The default AWS OpsWorks agent version. You have the following options:
            Auto-update - Set this parameter to LATEST . AWS OpsWorks automatically installs new agent versions on the stack's instances as soon as they are available.
            Fixed version - Set this parameter to your preferred agent version. To update the agent version, you must edit the stack configuration and specify a new version. AWS OpsWorks then automatically installs that version on the stack's instances.
            The default setting is the most recent release of the agent. To specify an agent version, you must use the complete version number, not the abbreviated number shown on the console. For a list of available agent version numbers, call DescribeAgentVersions .
            Note
            You can also specify an agent version when you create or update an instance, which overrides the stack's default setting.
            
    :type AgentVersion: string
    """
    pass


def create_user_profile(IamUserArn=None, SshUsername=None, SshPublicKey=None, AllowSelfManagement=None):
    """
    :param IamUserArn: [REQUIRED]
            The user's IAM ARN; this can also be a federated user's ARN.
            
    :type IamUserArn: string
    :param SshUsername: The user's SSH user name. The allowable characters are [a-z], [A-Z], [0-9], '-', and '_'. If the specified name includes other punctuation marks, AWS OpsWorks removes them. For example, my.name will be changed to myname . If you do not specify an SSH user name, AWS OpsWorks generates one from the IAM user name.
    :type SshUsername: string
    :param SshPublicKey: The user's public SSH key.
    :type SshPublicKey: string
    :param AllowSelfManagement: Whether users can specify their own SSH public key through the My Settings page. For more information, see Setting an IAM User's Public SSH Key .
    :type AllowSelfManagement: boolean
    """
    pass


def delete_app(AppId=None):
    """
    :param AppId: [REQUIRED]
            The app ID.
            ReturnsNone
            
    :type AppId: string
    """
    pass


def delete_instance(InstanceId=None, DeleteElasticIp=None, DeleteVolumes=None):
    """
    :param InstanceId: [REQUIRED]
            The instance ID.
            
    :type InstanceId: string
    :param DeleteElasticIp: Whether to delete the instance Elastic IP address.
    :type DeleteElasticIp: boolean
    :param DeleteVolumes: Whether to delete the instance's Amazon EBS volumes.
    :type DeleteVolumes: boolean
    """
    pass


def delete_layer(LayerId=None):
    """
    :param LayerId: [REQUIRED]
            The layer ID.
            ReturnsNone
            
    :type LayerId: string
    """
    pass


def delete_stack(StackId=None):
    """
    :param StackId: [REQUIRED]
            The stack ID.
            ReturnsNone
            
    :type StackId: string
    """
    pass


def delete_user_profile(IamUserArn=None):
    """
    :param IamUserArn: [REQUIRED]
            The user's IAM ARN. This can also be a federated user's ARN.
            ReturnsNone
            
    :type IamUserArn: string
    """
    pass


def deregister_ecs_cluster(EcsClusterArn=None):
    """
    :param EcsClusterArn: [REQUIRED]
            The cluster's ARN.
            ReturnsNone
            
    :type EcsClusterArn: string
    """
    pass


def deregister_elastic_ip(ElasticIp=None):
    """
    :param ElasticIp: [REQUIRED]
            The Elastic IP address.
            ReturnsNone
            
    :type ElasticIp: string
    """
    pass


def deregister_instance(InstanceId=None):
    """
    :param InstanceId: [REQUIRED]
            The instance ID.
            ReturnsNone
            
    :type InstanceId: string
    """
    pass


def deregister_rds_db_instance(RdsDbInstanceArn=None):
    """
    :param RdsDbInstanceArn: [REQUIRED]
            The Amazon RDS instance's ARN.
            ReturnsNone
            
    :type RdsDbInstanceArn: string
    """
    pass


def deregister_volume(VolumeId=None):
    """
    :param VolumeId: [REQUIRED]
            The AWS OpsWorks volume ID, which is the GUID that AWS OpsWorks assigned to the instance when you registered the volume with the stack, not the Amazon EC2 volume ID.
            ReturnsNone
            
    :type VolumeId: string
    """
    pass


def describe_agent_versions(StackId=None, ConfigurationManager=None):
    """
    :param StackId: The stack ID.
    :type StackId: string
    :param ConfigurationManager: The configuration manager.
            Name (string) --The name. This parameter must be set to 'Chef'.
            Version (string) --The Chef version. This parameter must be set to 12, 11.10, or 11.4 for Linux stacks, and to 12.2 for Windows stacks. The default value for Linux stacks is 11.4.
            
    :type ConfigurationManager: dict
    """
    pass


def describe_apps(StackId=None, AppIds=None):
    """
    :param StackId: The app stack ID. If you use this parameter, DescribeApps returns a description of the apps in the specified stack.
    :type StackId: string
    :param AppIds: An array of app IDs for the apps to be described. If you use this parameter, DescribeApps returns a description of the specified apps. Otherwise, it returns a description of every app.
            (string) --
            
    :type AppIds: list
    """
    pass


def describe_commands(DeploymentId=None, InstanceId=None, CommandIds=None):
    """
    :param DeploymentId: The deployment ID. If you include this parameter, DescribeCommands returns a description of the commands associated with the specified deployment.
    :type DeploymentId: string
    :param InstanceId: The instance ID. If you include this parameter, DescribeCommands returns a description of the commands associated with the specified instance.
    :type InstanceId: string
    :param CommandIds: An array of command IDs. If you include this parameter, DescribeCommands returns a description of the specified commands. Otherwise, it returns a description of every command.
            (string) --
            
    :type CommandIds: list
    """
    pass


def describe_deployments(StackId=None, AppId=None, DeploymentIds=None):
    """
    :param StackId: The stack ID. If you include this parameter, DescribeDeployments returns a description of the commands associated with the specified stack.
    :type StackId: string
    :param AppId: The app ID. If you include this parameter, DescribeDeployments returns a description of the commands associated with the specified app.
    :type AppId: string
    :param DeploymentIds: An array of deployment IDs to be described. If you include this parameter, DescribeDeployments returns a description of the specified deployments. Otherwise, it returns a description of every deployment.
            (string) --
            
    :type DeploymentIds: list
    """
    pass


def describe_ecs_clusters(EcsClusterArns=None, StackId=None, NextToken=None, MaxResults=None):
    """
    :param EcsClusterArns: A list of ARNs, one for each cluster to be described.
            (string) --
            
    :type EcsClusterArns: list
    :param StackId: A stack ID. DescribeEcsClusters returns a description of the cluster that is registered with the stack.
    :type StackId: string
    :param NextToken: If the previous paginated request did not return all of the remaining results, the response object's``NextToken`` parameter value is set to a token. To retrieve the next set of results, call DescribeEcsClusters again and assign that token to the request object's NextToken parameter. If there are no remaining results, the previous response object's NextToken parameter is set to null .
    :type NextToken: string
    :param MaxResults: To receive a paginated response, use this parameter to specify the maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a NextToken value that you can assign to the NextToken request parameter to get the next set of results.
    :type MaxResults: integer
    """
    pass


def describe_elastic_ips(InstanceId=None, StackId=None, Ips=None):
    """
    :param InstanceId: The instance ID. If you include this parameter, DescribeElasticIps returns a description of the Elastic IP addresses associated with the specified instance.
    :type InstanceId: string
    :param StackId: A stack ID. If you include this parameter, DescribeElasticIps returns a description of the Elastic IP addresses that are registered with the specified stack.
    :type StackId: string
    :param Ips: An array of Elastic IP addresses to be described. If you include this parameter, DescribeElasticIps returns a description of the specified Elastic IP addresses. Otherwise, it returns a description of every Elastic IP address.
            (string) --
            
    :type Ips: list
    """
    pass


def describe_elastic_load_balancers(StackId=None, LayerIds=None):
    """
    :param StackId: A stack ID. The action describes the stack's Elastic Load Balancing instances.
    :type StackId: string
    :param LayerIds: A list of layer IDs. The action describes the Elastic Load Balancing instances for the specified layers.
            (string) --
            
    :type LayerIds: list
    """
    pass


def describe_instances(StackId=None, LayerId=None, InstanceIds=None):
    """
    :param StackId: A stack ID. If you use this parameter, DescribeInstances returns descriptions of the instances associated with the specified stack.
    :type StackId: string
    :param LayerId: A layer ID. If you use this parameter, DescribeInstances returns descriptions of the instances associated with the specified layer.
    :type LayerId: string
    :param InstanceIds: An array of instance IDs to be described. If you use this parameter, DescribeInstances returns a description of the specified instances. Otherwise, it returns a description of every instance.
            (string) --
            
    :type InstanceIds: list
    """
    pass


def describe_layers(StackId=None, LayerIds=None):
    """
    :param StackId: The stack ID.
    :type StackId: string
    :param LayerIds: An array of layer IDs that specify the layers to be described. If you omit this parameter, DescribeLayers returns a description of every layer in the specified stack.
            (string) --
            
    :type LayerIds: list
    """
    pass


def describe_load_based_auto_scaling(LayerIds=None):
    """
    :param LayerIds: [REQUIRED]
            An array of layer IDs.
            (string) --
            Return typedict
            ReturnsResponse Syntax{
              'LoadBasedAutoScalingConfigurations': [
                {
                  'LayerId': 'string',
                  'Enable': True|False,
                  'UpScaling': {
                    'InstanceCount': 123,
                    'ThresholdsWaitTime': 123,
                    'IgnoreMetricsTime': 123,
                    'CpuThreshold': 123.0,
                    'MemoryThreshold': 123.0,
                    'LoadThreshold': 123.0,
                    'Alarms': [
                      'string',
                    ]
                  },
                  'DownScaling': {
                    'InstanceCount': 123,
                    'ThresholdsWaitTime': 123,
                    'IgnoreMetricsTime': 123,
                    'CpuThreshold': 123.0,
                    'MemoryThreshold': 123.0,
                    'LoadThreshold': 123.0,
                    'Alarms': [
                      'string',
                    ]
                  }
                },
              ]
            }
            Response Structure
            (dict) --Contains the response to a DescribeLoadBasedAutoScaling request.
            LoadBasedAutoScalingConfigurations (list) --An array of LoadBasedAutoScalingConfiguration objects that describe each layer's configuration.
            (dict) --Describes a layer's load-based auto scaling configuration.
            LayerId (string) --The layer ID.
            Enable (boolean) --Whether load-based auto scaling is enabled for the layer.
            UpScaling (dict) --An AutoScalingThresholds object that describes the upscaling configuration, which defines how and when AWS OpsWorks increases the number of instances.
            InstanceCount (integer) --The number of instances to add or remove when the load exceeds a threshold.
            ThresholdsWaitTime (integer) --The amount of time, in minutes, that the load must exceed a threshold before more instances are added or removed.
            IgnoreMetricsTime (integer) --The amount of time (in minutes) after a scaling event occurs that AWS OpsWorks should ignore metrics and suppress additional scaling events. For example, AWS OpsWorks adds new instances following an upscaling event but the instances won't start reducing the load until they have been booted and configured. There is no point in raising additional scaling events during that operation, which typically takes several minutes. IgnoreMetricsTime allows you to direct AWS OpsWorks to suppress scaling events long enough to get the new instances online.
            CpuThreshold (float) --The CPU utilization threshold, as a percent of the available CPU. A value of -1 disables the threshold.
            MemoryThreshold (float) --The memory utilization threshold, as a percent of the available memory. A value of -1 disables the threshold.
            LoadThreshold (float) --The load threshold. A value of -1 disables the threshold. For more information about how load is computed, see Load (computing) .
            Alarms (list) --Custom Cloudwatch auto scaling alarms, to be used as thresholds. This parameter takes a list of up to five alarm names, which are case sensitive and must be in the same region as the stack.
            Note
            To use custom alarms, you must update your service role to allow cloudwatch:DescribeAlarms . You can either have AWS OpsWorks update the role for you when you first use this feature or you can edit the role manually. For more information, see Allowing AWS OpsWorks to Act on Your Behalf .
            (string) --
            
            DownScaling (dict) --An AutoScalingThresholds object that describes the downscaling configuration, which defines how and when AWS OpsWorks reduces the number of instances.
            InstanceCount (integer) --The number of instances to add or remove when the load exceeds a threshold.
            ThresholdsWaitTime (integer) --The amount of time, in minutes, that the load must exceed a threshold before more instances are added or removed.
            IgnoreMetricsTime (integer) --The amount of time (in minutes) after a scaling event occurs that AWS OpsWorks should ignore metrics and suppress additional scaling events. For example, AWS OpsWorks adds new instances following an upscaling event but the instances won't start reducing the load until they have been booted and configured. There is no point in raising additional scaling events during that operation, which typically takes several minutes. IgnoreMetricsTime allows you to direct AWS OpsWorks to suppress scaling events long enough to get the new instances online.
            CpuThreshold (float) --The CPU utilization threshold, as a percent of the available CPU. A value of -1 disables the threshold.
            MemoryThreshold (float) --The memory utilization threshold, as a percent of the available memory. A value of -1 disables the threshold.
            LoadThreshold (float) --The load threshold. A value of -1 disables the threshold. For more information about how load is computed, see Load (computing) .
            Alarms (list) --Custom Cloudwatch auto scaling alarms, to be used as thresholds. This parameter takes a list of up to five alarm names, which are case sensitive and must be in the same region as the stack.
            Note
            To use custom alarms, you must update your service role to allow cloudwatch:DescribeAlarms . You can either have AWS OpsWorks update the role for you when you first use this feature or you can edit the role manually. For more information, see Allowing AWS OpsWorks to Act on Your Behalf .
            (string) --
            
            
            
            
    :type LayerIds: list
    """
    pass


def describe_my_user_profile():
    """
    """
    pass


def describe_permissions(IamUserArn=None, StackId=None):
    """
    :param IamUserArn: The user's IAM ARN. This can also be a federated user's ARN. For more information about IAM ARNs, see Using Identifiers .
    :type IamUserArn: string
    :param StackId: The stack ID.
    :type StackId: string
    """
    pass


def describe_raid_arrays(InstanceId=None, StackId=None, RaidArrayIds=None):
    """
    :param InstanceId: The instance ID. If you use this parameter, DescribeRaidArrays returns descriptions of the RAID arrays associated with the specified instance.
    :type InstanceId: string
    :param StackId: The stack ID.
    :type StackId: string
    :param RaidArrayIds: An array of RAID array IDs. If you use this parameter, DescribeRaidArrays returns descriptions of the specified arrays. Otherwise, it returns a description of every array.
            (string) --
            
    :type RaidArrayIds: list
    """
    pass


def describe_rds_db_instances(StackId=None, RdsDbInstanceArns=None):
    """
    :param StackId: [REQUIRED]
            The stack ID that the instances are registered with. The operation returns descriptions of all registered Amazon RDS instances.
            
    :type StackId: string
    :param RdsDbInstanceArns: An array containing the ARNs of the instances to be described.
            (string) --
            
    :type RdsDbInstanceArns: list
    """
    pass


def describe_service_errors(StackId=None, InstanceId=None, ServiceErrorIds=None):
    """
    :param StackId: The stack ID. If you use this parameter, DescribeServiceErrors returns descriptions of the errors associated with the specified stack.
    :type StackId: string
    :param InstanceId: The instance ID. If you use this parameter, DescribeServiceErrors returns descriptions of the errors associated with the specified instance.
    :type InstanceId: string
    :param ServiceErrorIds: An array of service error IDs. If you use this parameter, DescribeServiceErrors returns descriptions of the specified errors. Otherwise, it returns a description of every error.
            (string) --
            
    :type ServiceErrorIds: list
    """
    pass


def describe_stack_provisioning_parameters(StackId=None):
    """
    :param StackId: [REQUIRED]
            The stack ID
            Return typedict
            ReturnsResponse Syntax{
              'AgentInstallerUrl': 'string',
              'Parameters': {
                'string': 'string'
              }
            }
            Response Structure
            (dict) --Contains the response to a DescribeStackProvisioningParameters request.
            AgentInstallerUrl (string) --The AWS OpsWorks agent installer's URL.
            Parameters (dict) --An embedded object that contains the provisioning parameters.
            (string) --
            (string) --
            
            
            
    :type StackId: string
    """
    pass


def describe_stack_summary(StackId=None):
    """
    :param StackId: [REQUIRED]
            The stack ID.
            Return typedict
            ReturnsResponse Syntax{
              'StackSummary': {
                'StackId': 'string',
                'Name': 'string',
                'Arn': 'string',
                'LayersCount': 123,
                'AppsCount': 123,
                'InstancesCount': {
                  'Assigning': 123,
                  'Booting': 123,
                  'ConnectionLost': 123,
                  'Deregistering': 123,
                  'Online': 123,
                  'Pending': 123,
                  'Rebooting': 123,
                  'Registered': 123,
                  'Registering': 123,
                  'Requested': 123,
                  'RunningSetup': 123,
                  'SetupFailed': 123,
                  'ShuttingDown': 123,
                  'StartFailed': 123,
                  'Stopped': 123,
                  'Stopping': 123,
                  'Terminated': 123,
                  'Terminating': 123,
                  'Unassigning': 123
                }
              }
            }
            Response Structure
            (dict) --Contains the response to a DescribeStackSummary request.
            StackSummary (dict) --A StackSummary object that contains the results.
            StackId (string) --The stack ID.
            Name (string) --The stack name.
            Arn (string) --The stack's ARN.
            LayersCount (integer) --The number of layers.
            AppsCount (integer) --The number of apps.
            InstancesCount (dict) --An InstancesCount object with the number of instances in each status.
            Assigning (integer) --The number of instances in the Assigning state.
            Booting (integer) --The number of instances with booting status.
            ConnectionLost (integer) --The number of instances with connection_lost status.
            Deregistering (integer) --The number of instances in the Deregistering state.
            Online (integer) --The number of instances with online status.
            Pending (integer) --The number of instances with pending status.
            Rebooting (integer) --The number of instances with rebooting status.
            Registered (integer) --The number of instances in the Registered state.
            Registering (integer) --The number of instances in the Registering state.
            Requested (integer) --The number of instances with requested status.
            RunningSetup (integer) --The number of instances with running_setup status.
            SetupFailed (integer) --The number of instances with setup_failed status.
            ShuttingDown (integer) --The number of instances with shutting_down status.
            StartFailed (integer) --The number of instances with start_failed status.
            Stopped (integer) --The number of instances with stopped status.
            Stopping (integer) --The number of instances with stopping status.
            Terminated (integer) --The number of instances with terminated status.
            Terminating (integer) --The number of instances with terminating status.
            Unassigning (integer) --The number of instances in the Unassigning state.
            
            
            
    :type StackId: string
    """
    pass


def describe_stacks(StackIds=None):
    """
    :param StackIds: An array of stack IDs that specify the stacks to be described. If you omit this parameter, DescribeStacks returns a description of every stack.
            (string) --
            Return typedict
            ReturnsResponse Syntax{
              'Stacks': [
                {
                  'StackId': 'string',
                  'Name': 'string',
                  'Arn': 'string',
                  'Region': 'string',
                  'VpcId': 'string',
                  'Attributes': {
                    'string': 'string'
                  },
                  'ServiceRoleArn': 'string',
                  'DefaultInstanceProfileArn': 'string',
                  'DefaultOs': 'string',
                  'HostnameTheme': 'string',
                  'DefaultAvailabilityZone': 'string',
                  'DefaultSubnetId': 'string',
                  'CustomJson': 'string',
                  'ConfigurationManager': {
                    'Name': 'string',
                    'Version': 'string'
                  },
                  'ChefConfiguration': {
                    'ManageBerkshelf': True|False,
                    'BerkshelfVersion': 'string'
                  },
                  'UseCustomCookbooks': True|False,
                  'UseOpsworksSecurityGroups': True|False,
                  'CustomCookbooksSource': {
                    'Type': 'git'|'svn'|'archive'|'s3',
                    'Url': 'string',
                    'Username': 'string',
                    'Password': 'string',
                    'SshKey': 'string',
                    'Revision': 'string'
                  },
                  'DefaultSshKeyName': 'string',
                  'CreatedAt': 'string',
                  'DefaultRootDeviceType': 'ebs'|'instance-store',
                  'AgentVersion': 'string'
                },
              ]
            }
            Response Structure
            (dict) --Contains the response to a DescribeStacks request.
            Stacks (list) --An array of Stack objects that describe the stacks.
            (dict) --Describes a stack.
            StackId (string) --The stack ID.
            Name (string) --The stack name.
            Arn (string) --The stack's ARN.
            Region (string) --The stack AWS region, such as 'ap-northeast-2'. For more information about AWS regions, see Regions and Endpoints .
            VpcId (string) --The VPC ID; applicable only if the stack is running in a VPC.
            Attributes (dict) --The stack's attributes.
            (string) --
            (string) --
            
            ServiceRoleArn (string) --The stack AWS Identity and Access Management (IAM) role.
            DefaultInstanceProfileArn (string) --The ARN of an IAM profile that is the default profile for all of the stack's EC2 instances. For more information about IAM ARNs, see Using Identifiers .
            DefaultOs (string) --The stack's default operating system.
            HostnameTheme (string) --The stack host name theme, with spaces replaced by underscores.
            DefaultAvailabilityZone (string) --The stack's default Availability Zone. For more information, see Regions and Endpoints .
            DefaultSubnetId (string) --The default subnet ID; applicable only if the stack is running in a VPC.
            CustomJson (string) --A JSON object that contains user-defined attributes to be added to the stack configuration and deployment attributes. You can use custom JSON to override the corresponding default stack configuration attribute values or to pass data to recipes. The string should be in the following format:
            '{\'key1\': \'value1\', \'key2\': \'value2\',...}'
            For more information on custom JSON, see Use Custom JSON to Modify the Stack Configuration Attributes .
            ConfigurationManager (dict) --The configuration manager.
            Name (string) --The name. This parameter must be set to 'Chef'.
            Version (string) --The Chef version. This parameter must be set to 12, 11.10, or 11.4 for Linux stacks, and to 12.2 for Windows stacks. The default value for Linux stacks is 11.4.
            ChefConfiguration (dict) --A ChefConfiguration object that specifies whether to enable Berkshelf and the Berkshelf version. For more information, see Create a New Stack .
            ManageBerkshelf (boolean) --Whether to enable Berkshelf.
            BerkshelfVersion (string) --The Berkshelf version.
            UseCustomCookbooks (boolean) --Whether the stack uses custom cookbooks.
            UseOpsworksSecurityGroups (boolean) --Whether the stack automatically associates the AWS OpsWorks built-in security groups with the stack's layers.
            CustomCookbooksSource (dict) --Contains the information required to retrieve an app or cookbook from a repository. For more information, see Creating Apps or Custom Recipes and Cookbooks .
            Type (string) --The repository type.
            Url (string) --The source URL.
            Username (string) --This parameter depends on the repository type.
            For Amazon S3 bundles, set Username to the appropriate IAM access key ID.
            For HTTP bundles, Git repositories, and Subversion repositories, set Username to the user name.
            Password (string) --When included in a request, the parameter depends on the repository type.
            For Amazon S3 bundles, set Password to the appropriate IAM secret access key.
            For HTTP bundles and Subversion repositories, set Password to the password.
            For more information on how to safely handle IAM credentials, see http://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html .
            In responses, AWS OpsWorks returns *****FILTERED***** instead of the actual value.
            SshKey (string) --In requests, the repository's SSH key.
            In responses, AWS OpsWorks returns *****FILTERED***** instead of the actual value.
            Revision (string) --The application's version. AWS OpsWorks enables you to easily deploy new versions of an application. One of the simplest approaches is to have branches or revisions in your repository that represent different versions that can potentially be deployed.
            DefaultSshKeyName (string) --A default Amazon EC2 key pair for the stack's instances. You can override this value when you create or update an instance.
            CreatedAt (string) --The date when the stack was created.
            DefaultRootDeviceType (string) --The default root device type. This value is used by default for all instances in the stack, but you can override it when you create an instance. For more information, see Storage for the Root Device .
            AgentVersion (string) --The agent version. This parameter is set to LATEST for auto-update. or a version number for a fixed agent version.
            
            
            
    :type StackIds: list
    """
    pass


def describe_time_based_auto_scaling(InstanceIds=None):
    """
    :param InstanceIds: [REQUIRED]
            An array of instance IDs.
            (string) --
            Return typedict
            ReturnsResponse Syntax{
              'TimeBasedAutoScalingConfigurations': [
                {
                  'InstanceId': 'string',
                  'AutoScalingSchedule': {
                    'Monday': {
                      'string': 'string'
                    },
                    'Tuesday': {
                      'string': 'string'
                    },
                    'Wednesday': {
                      'string': 'string'
                    },
                    'Thursday': {
                      'string': 'string'
                    },
                    'Friday': {
                      'string': 'string'
                    },
                    'Saturday': {
                      'string': 'string'
                    },
                    'Sunday': {
                      'string': 'string'
                    }
                  }
                },
              ]
            }
            Response Structure
            (dict) --Contains the response to a DescribeTimeBasedAutoScaling request.
            TimeBasedAutoScalingConfigurations (list) --An array of TimeBasedAutoScalingConfiguration objects that describe the configuration for the specified instances.
            (dict) --Describes an instance's time-based auto scaling configuration.
            InstanceId (string) --The instance ID.
            AutoScalingSchedule (dict) --A WeeklyAutoScalingSchedule object with the instance schedule.
            Monday (dict) --The schedule for Monday.
            (string) --
            (string) --
            
            Tuesday (dict) --The schedule for Tuesday.
            (string) --
            (string) --
            
            Wednesday (dict) --The schedule for Wednesday.
            (string) --
            (string) --
            
            Thursday (dict) --The schedule for Thursday.
            (string) --
            (string) --
            
            Friday (dict) --The schedule for Friday.
            (string) --
            (string) --
            
            Saturday (dict) --The schedule for Saturday.
            (string) --
            (string) --
            
            Sunday (dict) --The schedule for Sunday.
            (string) --
            (string) --
            
            
            
            
    :type InstanceIds: list
    """
    pass


def describe_user_profiles(IamUserArns=None):
    """
    :param IamUserArns: An array of IAM or federated user ARNs that identify the users to be described.
            (string) --
            Return typedict
            ReturnsResponse Syntax{
              'UserProfiles': [
                {
                  'IamUserArn': 'string',
                  'Name': 'string',
                  'SshUsername': 'string',
                  'SshPublicKey': 'string',
                  'AllowSelfManagement': True|False
                },
              ]
            }
            Response Structure
            (dict) --Contains the response to a DescribeUserProfiles request.
            UserProfiles (list) --A Users object that describes the specified users.
            (dict) --Describes a user's SSH information.
            IamUserArn (string) --The user's IAM ARN.
            Name (string) --The user's name.
            SshUsername (string) --The user's SSH user name.
            SshPublicKey (string) --The user's SSH public key.
            AllowSelfManagement (boolean) --Whether users can specify their own SSH public key through the My Settings page. For more information, see Managing User Permissions .
            
            
            
    :type IamUserArns: list
    """
    pass


def describe_volumes(InstanceId=None, StackId=None, RaidArrayId=None, VolumeIds=None):
    """
    :param InstanceId: The instance ID. If you use this parameter, DescribeVolumes returns descriptions of the volumes associated with the specified instance.
    :type InstanceId: string
    :param StackId: A stack ID. The action describes the stack's registered Amazon EBS volumes.
    :type StackId: string
    :param RaidArrayId: The RAID array ID. If you use this parameter, DescribeVolumes returns descriptions of the volumes associated with the specified RAID array.
    :type RaidArrayId: string
    :param VolumeIds: Am array of volume IDs. If you use this parameter, DescribeVolumes returns descriptions of the specified volumes. Otherwise, it returns a description of every volume.
            (string) --
            
    :type VolumeIds: list
    """
    pass


def detach_elastic_load_balancer(ElasticLoadBalancerName=None, LayerId=None):
    """
    :param ElasticLoadBalancerName: [REQUIRED]
            The Elastic Load Balancing instance's name.
            
    :type ElasticLoadBalancerName: string
    :param LayerId: [REQUIRED]
            The ID of the layer that the Elastic Load Balancing instance is attached to.
            
    :type LayerId: string
    """
    pass


def disassociate_elastic_ip(ElasticIp=None):
    """
    :param ElasticIp: [REQUIRED]
            The Elastic IP address.
            ReturnsNone
            
    :type ElasticIp: string
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


def get_hostname_suggestion(LayerId=None):
    """
    :param LayerId: [REQUIRED]
            The layer ID.
            Return typedict
            ReturnsResponse Syntax{
              'LayerId': 'string',
              'Hostname': 'string'
            }
            Response Structure
            (dict) --Contains the response to a GetHostnameSuggestion request.
            LayerId (string) --The layer ID.
            Hostname (string) --The generated host name.
            
            
    :type LayerId: string
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


def grant_access(InstanceId=None, ValidForInMinutes=None):
    """
    :param InstanceId: [REQUIRED]
            The instance's AWS OpsWorks ID.
            
    :type InstanceId: string
    :param ValidForInMinutes: The length of time (in minutes) that the grant is valid. When the grant expires at the end of this period, the user will no longer be able to use the credentials to log in. If the user is logged in at the time, he or she automatically will be logged out.
    :type ValidForInMinutes: integer
    """
    pass


def reboot_instance(InstanceId=None):
    """
    :param InstanceId: [REQUIRED]
            The instance ID.
            ReturnsNone
            
    :type InstanceId: string
    """
    pass


def register_ecs_cluster(EcsClusterArn=None, StackId=None):
    """
    :param EcsClusterArn: [REQUIRED]
            The cluster's ARN.
            
    :type EcsClusterArn: string
    :param StackId: [REQUIRED]
            The stack ID.
            
    :type StackId: string
    """
    pass


def register_elastic_ip(ElasticIp=None, StackId=None):
    """
    :param ElasticIp: [REQUIRED]
            The Elastic IP address.
            
    :type ElasticIp: string
    :param StackId: [REQUIRED]
            The stack ID.
            
    :type StackId: string
    """
    pass


def register_instance(StackId=None, Hostname=None, PublicIp=None, PrivateIp=None, RsaPublicKey=None,
                      RsaPublicKeyFingerprint=None, InstanceIdentity=None):
    """
    :param StackId: [REQUIRED]
            The ID of the stack that the instance is to be registered with.
            
    :type StackId: string
    :param Hostname: The instance's hostname.
    :type Hostname: string
    :param PublicIp: The instance's public IP address.
    :type PublicIp: string
    :param PrivateIp: The instance's private IP address.
    :type PrivateIp: string
    :param RsaPublicKey: The instances public RSA key. This key is used to encrypt communication between the instance and the service.
    :type RsaPublicKey: string
    :param RsaPublicKeyFingerprint: The instances public RSA key fingerprint.
    :type RsaPublicKeyFingerprint: string
    :param InstanceIdentity: An InstanceIdentity object that contains the instance's identity.
            Document (string) --A JSON document that contains the metadata.
            Signature (string) --A signature that can be used to verify the document's accuracy and authenticity.
            
    :type InstanceIdentity: dict
    """
    pass


def register_rds_db_instance(StackId=None, RdsDbInstanceArn=None, DbUser=None, DbPassword=None):
    """
    :param StackId: [REQUIRED]
            The stack ID.
            
    :type StackId: string
    :param RdsDbInstanceArn: [REQUIRED]
            The Amazon RDS instance's ARN.
            
    :type RdsDbInstanceArn: string
    :param DbUser: [REQUIRED]
            The database's master user name.
            
    :type DbUser: string
    :param DbPassword: [REQUIRED]
            The database password.
            
    :type DbPassword: string
    """
    pass


def register_volume(Ec2VolumeId=None, StackId=None):
    """
    :param Ec2VolumeId: The Amazon EBS volume ID.
    :type Ec2VolumeId: string
    :param StackId: [REQUIRED]
            The stack ID.
            
    :type StackId: string
    """
    pass


def set_load_based_auto_scaling(LayerId=None, Enable=None, UpScaling=None, DownScaling=None):
    """
    :param LayerId: [REQUIRED]
            The layer ID.
            
    :type LayerId: string
    :param Enable: Enables load-based auto scaling for the layer.
    :type Enable: boolean
    :param UpScaling: An AutoScalingThresholds object with the upscaling threshold configuration. If the load exceeds these thresholds for a specified amount of time, AWS OpsWorks starts a specified number of instances.
            InstanceCount (integer) --The number of instances to add or remove when the load exceeds a threshold.
            ThresholdsWaitTime (integer) --The amount of time, in minutes, that the load must exceed a threshold before more instances are added or removed.
            IgnoreMetricsTime (integer) --The amount of time (in minutes) after a scaling event occurs that AWS OpsWorks should ignore metrics and suppress additional scaling events. For example, AWS OpsWorks adds new instances following an upscaling event but the instances won't start reducing the load until they have been booted and configured. There is no point in raising additional scaling events during that operation, which typically takes several minutes. IgnoreMetricsTime allows you to direct AWS OpsWorks to suppress scaling events long enough to get the new instances online.
            CpuThreshold (float) --The CPU utilization threshold, as a percent of the available CPU. A value of -1 disables the threshold.
            MemoryThreshold (float) --The memory utilization threshold, as a percent of the available memory. A value of -1 disables the threshold.
            LoadThreshold (float) --The load threshold. A value of -1 disables the threshold. For more information about how load is computed, see Load (computing) .
            Alarms (list) --Custom Cloudwatch auto scaling alarms, to be used as thresholds. This parameter takes a list of up to five alarm names, which are case sensitive and must be in the same region as the stack.
            Note
            To use custom alarms, you must update your service role to allow cloudwatch:DescribeAlarms . You can either have AWS OpsWorks update the role for you when you first use this feature or you can edit the role manually. For more information, see Allowing AWS OpsWorks to Act on Your Behalf .
            (string) --
            
    :type UpScaling: dict
    :param DownScaling: An AutoScalingThresholds object with the downscaling threshold configuration. If the load falls below these thresholds for a specified amount of time, AWS OpsWorks stops a specified number of instances.
            InstanceCount (integer) --The number of instances to add or remove when the load exceeds a threshold.
            ThresholdsWaitTime (integer) --The amount of time, in minutes, that the load must exceed a threshold before more instances are added or removed.
            IgnoreMetricsTime (integer) --The amount of time (in minutes) after a scaling event occurs that AWS OpsWorks should ignore metrics and suppress additional scaling events. For example, AWS OpsWorks adds new instances following an upscaling event but the instances won't start reducing the load until they have been booted and configured. There is no point in raising additional scaling events during that operation, which typically takes several minutes. IgnoreMetricsTime allows you to direct AWS OpsWorks to suppress scaling events long enough to get the new instances online.
            CpuThreshold (float) --The CPU utilization threshold, as a percent of the available CPU. A value of -1 disables the threshold.
            MemoryThreshold (float) --The memory utilization threshold, as a percent of the available memory. A value of -1 disables the threshold.
            LoadThreshold (float) --The load threshold. A value of -1 disables the threshold. For more information about how load is computed, see Load (computing) .
            Alarms (list) --Custom Cloudwatch auto scaling alarms, to be used as thresholds. This parameter takes a list of up to five alarm names, which are case sensitive and must be in the same region as the stack.
            Note
            To use custom alarms, you must update your service role to allow cloudwatch:DescribeAlarms . You can either have AWS OpsWorks update the role for you when you first use this feature or you can edit the role manually. For more information, see Allowing AWS OpsWorks to Act on Your Behalf .
            (string) --
            
    :type DownScaling: dict
    """
    pass


def set_permission(StackId=None, IamUserArn=None, AllowSsh=None, AllowSudo=None, Level=None):
    """
    :param StackId: [REQUIRED]
            The stack ID.
            
    :type StackId: string
    :param IamUserArn: [REQUIRED]
            The user's IAM ARN. This can also be a federated user's ARN.
            
    :type IamUserArn: string
    :param AllowSsh: The user is allowed to use SSH to communicate with the instance.
    :type AllowSsh: boolean
    :param AllowSudo: The user is allowed to use sudo to elevate privileges.
    :type AllowSudo: boolean
    :param Level: The user's permission level, which must be set to one of the following strings. You cannot set your own permissions level.
            deny
            show
            deploy
            manage
            iam_only
            For more information on the permissions associated with these levels, see Managing User Permissions .
            
    :type Level: string
    """
    pass


def set_time_based_auto_scaling(InstanceId=None, AutoScalingSchedule=None):
    """
    :param InstanceId: [REQUIRED]
            The instance ID.
            
    :type InstanceId: string
    :param AutoScalingSchedule: An AutoScalingSchedule with the instance schedule.
            Monday (dict) --The schedule for Monday.
            (string) --
            (string) --
            
            Tuesday (dict) --The schedule for Tuesday.
            (string) --
            (string) --
            
            Wednesday (dict) --The schedule for Wednesday.
            (string) --
            (string) --
            
            Thursday (dict) --The schedule for Thursday.
            (string) --
            (string) --
            
            Friday (dict) --The schedule for Friday.
            (string) --
            (string) --
            
            Saturday (dict) --The schedule for Saturday.
            (string) --
            (string) --
            
            Sunday (dict) --The schedule for Sunday.
            (string) --
            (string) --
            
            
    :type AutoScalingSchedule: dict
    """
    pass


def start_instance(InstanceId=None):
    """
    :param InstanceId: [REQUIRED]
            The instance ID.
            ReturnsNone
            
    :type InstanceId: string
    """
    pass


def start_stack(StackId=None):
    """
    :param StackId: [REQUIRED]
            The stack ID.
            ReturnsNone
            
    :type StackId: string
    """
    pass


def stop_instance(InstanceId=None):
    """
    :param InstanceId: [REQUIRED]
            The instance ID.
            ReturnsNone
            
    :type InstanceId: string
    """
    pass


def stop_stack(StackId=None):
    """
    :param StackId: [REQUIRED]
            The stack ID.
            ReturnsNone
            
    :type StackId: string
    """
    pass


def unassign_instance(InstanceId=None):
    """
    :param InstanceId: [REQUIRED]
            The instance ID.
            ReturnsNone
            
    :type InstanceId: string
    """
    pass


def unassign_volume(VolumeId=None):
    """
    :param VolumeId: [REQUIRED]
            The volume ID.
            ReturnsNone
            
    :type VolumeId: string
    """
    pass


def update_app(AppId=None, Name=None, Description=None, DataSources=None, Type=None, AppSource=None, Domains=None,
               EnableSsl=None, SslConfiguration=None, Attributes=None, Environment=None):
    """
    :param AppId: [REQUIRED]
            The app ID.
            
    :type AppId: string
    :param Name: The app name.
    :type Name: string
    :param Description: A description of the app.
    :type Description: string
    :param DataSources: The app's data sources.
            (dict) --Describes an app's data source.
            Type (string) --The data source's type, AutoSelectOpsworksMysqlInstance , OpsworksMysqlInstance , or RdsDbInstance .
            Arn (string) --The data source's ARN.
            DatabaseName (string) --The database name.
            
            
    :type DataSources: list
    :param Type: The app type.
    :type Type: string
    :param AppSource: A Source object that specifies the app repository.
            Type (string) --The repository type.
            Url (string) --The source URL.
            Username (string) --This parameter depends on the repository type.
            For Amazon S3 bundles, set Username to the appropriate IAM access key ID.
            For HTTP bundles, Git repositories, and Subversion repositories, set Username to the user name.
            Password (string) --When included in a request, the parameter depends on the repository type.
            For Amazon S3 bundles, set Password to the appropriate IAM secret access key.
            For HTTP bundles and Subversion repositories, set Password to the password.
            For more information on how to safely handle IAM credentials, see http://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html .
            In responses, AWS OpsWorks returns *****FILTERED***** instead of the actual value.
            SshKey (string) --In requests, the repository's SSH key.
            In responses, AWS OpsWorks returns *****FILTERED***** instead of the actual value.
            Revision (string) --The application's version. AWS OpsWorks enables you to easily deploy new versions of an application. One of the simplest approaches is to have branches or revisions in your repository that represent different versions that can potentially be deployed.
            
    :type AppSource: dict
    :param Domains: The app's virtual host settings, with multiple domains separated by commas. For example: 'www.example.com, example.com'
            (string) --
            
    :type Domains: list
    :param EnableSsl: Whether SSL is enabled for the app.
    :type EnableSsl: boolean
    :param SslConfiguration: An SslConfiguration object with the SSL configuration.
            Certificate (string) -- [REQUIRED]The contents of the certificate's domain.crt file.
            PrivateKey (string) -- [REQUIRED]The private key; the contents of the certificate's domain.kex file.
            Chain (string) --Optional. Can be used to specify an intermediate certificate authority key or client authentication.
            
    :type SslConfiguration: dict
    :param Attributes: One or more user-defined key/value pairs to be added to the stack attributes.
            (string) --
            (string) --
            
    :type Attributes: dict
    :param Environment: An array of EnvironmentVariable objects that specify environment variables to be associated with the app. After you deploy the app, these variables are defined on the associated app server instances.For more information, see Environment Variables .
            There is no specific limit on the number of environment variables. However, the size of the associated data structure - which includes the variables' names, values, and protected flag values - cannot exceed 10 KB (10240 Bytes). This limit should accommodate most if not all use cases. Exceeding it will cause an exception with the message, 'Environment: is too large (maximum is 10KB).'
            Note
            This parameter is supported only by Chef 11.10 stacks. If you have specified one or more environment variables, you cannot modify the stack's Chef version.
            (dict) --Represents an app's environment variable.
            Key (string) -- [REQUIRED](Required) The environment variable's name, which can consist of up to 64 characters and must be specified. The name can contain upper- and lowercase letters, numbers, and underscores (_), but it must start with a letter or underscore.
            Value (string) -- [REQUIRED](Optional) The environment variable's value, which can be left empty. If you specify a value, it can contain up to 256 characters, which must all be printable.
            Secure (boolean) --(Optional) Whether the variable's value will be returned by the DescribeApps action. To conceal an environment variable's value, set Secure to true . DescribeApps then returns *****FILTERED***** instead of the actual value. The default value for Secure is false .
            
            
    :type Environment: list
    """
    pass


def update_elastic_ip(ElasticIp=None, Name=None):
    """
    :param ElasticIp: [REQUIRED]
            The address.
            
    :type ElasticIp: string
    :param Name: The new name.
    :type Name: string
    """
    pass


def update_instance(InstanceId=None, LayerIds=None, InstanceType=None, AutoScalingType=None, Hostname=None, Os=None,
                    AmiId=None, SshKeyName=None, Architecture=None, InstallUpdatesOnBoot=None, EbsOptimized=None,
                    AgentVersion=None):
    """
    :param InstanceId: [REQUIRED]
            The instance ID.
            
    :type InstanceId: string
    :param LayerIds: The instance's layer IDs.
            (string) --
            
    :type LayerIds: list
    :param InstanceType: The instance type, such as t2.micro . For a list of supported instance types, open the stack in the console, choose Instances , and choose + Instance . The Size list contains the currently supported types. For more information, see Instance Families and Types . The parameter values that you use to specify the various types are in the API Name column of the Available Instance Types table.
    :type InstanceType: string
    :param AutoScalingType: For load-based or time-based instances, the type. Windows stacks can use only time-based instances.
    :type AutoScalingType: string
    :param Hostname: The instance host name.
    :type Hostname: string
    :param Os: The instance's operating system, which must be set to one of the following. You cannot update an instance that is using a custom AMI.
            A supported Linux operating system: An Amazon Linux version, such as Amazon Linux 2016.03 , Amazon Linux 2015.09 , or Amazon Linux 2015.03 .
            A supported Ubuntu operating system, such as Ubuntu 16.04 LTS , Ubuntu 14.04 LTS , or Ubuntu 12.04 LTS .
            CentOS 7
            Red Hat Enterprise Linux 7
            A supported Windows operating system, such as Microsoft Windows Server 2012 R2 Base , Microsoft Windows Server 2012 R2 with SQL Server Express , Microsoft Windows Server 2012 R2 with SQL Server Standard , or Microsoft Windows Server 2012 R2 with SQL Server Web .
            For more information on the supported operating systems, see AWS OpsWorks Operating Systems .
            The default option is the current Amazon Linux version. If you set this parameter to Custom , you must use the AmiId parameter to specify the custom AMI that you want to use. For more information on the supported operating systems, see Operating Systems . For more information on how to use custom AMIs with OpsWorks, see Using Custom AMIs .
            Note
            You can specify a different Linux operating system for the updated stack, but you cannot change from Linux to Windows or Windows to Linux.
            
    :type Os: string
    :param AmiId: The ID of the AMI that was used to create the instance. The value of this parameter must be the same AMI ID that the instance is already using. You cannot apply a new AMI to an instance by running UpdateInstance. UpdateInstance does not work on instances that are using custom AMIs.
    :type AmiId: string
    :param SshKeyName: The instance's Amazon EC2 key name.
    :type SshKeyName: string
    :param Architecture: The instance architecture. Instance types do not necessarily support both architectures. For a list of the architectures that are supported by the different instance types, see Instance Families and Types .
    :type Architecture: string
    :param InstallUpdatesOnBoot: Whether to install operating system and package updates when the instance boots. The default value is true . To control when updates are installed, set this value to false . You must then update your instances manually by using CreateDeployment to run the update_dependencies stack command or by manually running yum (Amazon Linux) or apt-get (Ubuntu) on the instances.
            Note
            We strongly recommend using the default value of true , to ensure that your instances have the latest security updates.
            
    :type InstallUpdatesOnBoot: boolean
    :param EbsOptimized: This property cannot be updated.
    :type EbsOptimized: boolean
    :param AgentVersion: The default AWS OpsWorks agent version. You have the following options:
            INHERIT - Use the stack's default agent version setting.
            version_number - Use the specified agent version. This value overrides the stack's default setting. To update the agent version, you must edit the instance configuration and specify a new version. AWS OpsWorks then automatically installs that version on the instance.
            The default setting is INHERIT . To specify an agent version, you must use the complete version number, not the abbreviated number shown on the console. For a list of available agent version numbers, call DescribeAgentVersions .
            
    :type AgentVersion: string
    """
    pass


def update_layer(LayerId=None, Name=None, Shortname=None, Attributes=None, CustomInstanceProfileArn=None,
                 CustomJson=None, CustomSecurityGroupIds=None, Packages=None, VolumeConfigurations=None,
                 EnableAutoHealing=None, AutoAssignElasticIps=None, AutoAssignPublicIps=None, CustomRecipes=None,
                 InstallUpdatesOnBoot=None, UseEbsOptimizedInstances=None, LifecycleEventConfiguration=None):
    """
    :param LayerId: [REQUIRED]
            The layer ID.
            
    :type LayerId: string
    :param Name: The layer name, which is used by the console.
    :type Name: string
    :param Shortname: For custom layers only, use this parameter to specify the layer's short name, which is used internally by AWS OpsWorksand by Chef. The short name is also used as the name for the directory where your app files are installed. It can have a maximum of 200 characters and must be in the following format: /A[a-z0-9-_.]+Z/.
            The built-in layers' short names are defined by AWS OpsWorks. For more information, see the Layer Reference
            
    :type Shortname: string
    :param Attributes: One or more user-defined key/value pairs to be added to the stack attributes.
            (string) --
            (string) --
            
    :type Attributes: dict
    :param CustomInstanceProfileArn: The ARN of an IAM profile to be used for all of the layer's EC2 instances. For more information about IAM ARNs, see Using Identifiers .
    :type CustomInstanceProfileArn: string
    :param CustomJson: A JSON-formatted string containing custom stack configuration and deployment attributes to be installed on the layer's instances. For more information, see Using Custom JSON .
    :type CustomJson: string
    :param CustomSecurityGroupIds: An array containing the layer's custom security group IDs.
            (string) --
            
    :type CustomSecurityGroupIds: list
    :param Packages: An array of Package objects that describe the layer's packages.
            (string) --
            
    :type Packages: list
    :param VolumeConfigurations: A VolumeConfigurations object that describes the layer's Amazon EBS volumes.
            (dict) --Describes an Amazon EBS volume configuration.
            MountPoint (string) -- [REQUIRED]The volume mount point. For example '/dev/sdh'.
            RaidLevel (integer) --The volume RAID level .
            NumberOfDisks (integer) -- [REQUIRED]The number of disks in the volume.
            Size (integer) -- [REQUIRED]The volume size.
            VolumeType (string) --The volume type:
            standard - Magnetic
            io1 - Provisioned IOPS (SSD)
            gp2 - General Purpose (SSD)
            Iops (integer) --For PIOPS volumes, the IOPS per disk.
            
            
    :type VolumeConfigurations: list
    :param EnableAutoHealing: Whether to disable auto healing for the layer.
    :type EnableAutoHealing: boolean
    :param AutoAssignElasticIps: Whether to automatically assign an Elastic IP address to the layer's instances. For more information, see How to Edit a Layer .
    :type AutoAssignElasticIps: boolean
    :param AutoAssignPublicIps: For stacks that are running in a VPC, whether to automatically assign a public IP address to the layer's instances. For more information, see How to Edit a Layer .
    :type AutoAssignPublicIps: boolean
    :param CustomRecipes: A LayerCustomRecipes object that specifies the layer's custom recipes.
            Setup (list) --An array of custom recipe names to be run following a setup event.
            (string) --
            Configure (list) --An array of custom recipe names to be run following a configure event.
            (string) --
            Deploy (list) --An array of custom recipe names to be run following a deploy event.
            (string) --
            Undeploy (list) --An array of custom recipe names to be run following a undeploy event.
            (string) --
            Shutdown (list) --An array of custom recipe names to be run following a shutdown event.
            (string) --
            
    :type CustomRecipes: dict
    :param InstallUpdatesOnBoot: Whether to install operating system and package updates when the instance boots. The default value is true . To control when updates are installed, set this value to false . You must then update your instances manually by using CreateDeployment to run the update_dependencies stack command or manually running yum (Amazon Linux) or apt-get (Ubuntu) on the instances.
            Note
            We strongly recommend using the default value of true , to ensure that your instances have the latest security updates.
            
    :type InstallUpdatesOnBoot: boolean
    :param UseEbsOptimizedInstances: Whether to use Amazon EBS-optimized instances.
    :type UseEbsOptimizedInstances: boolean
    :param LifecycleEventConfiguration: 
            Shutdown (dict) --A ShutdownEventConfiguration object that specifies the Shutdown event configuration.
            ExecutionTimeout (integer) --The time, in seconds, that AWS OpsWorks will wait after triggering a Shutdown event before shutting down an instance.
            DelayUntilElbConnectionsDrained (boolean) --Whether to enable Elastic Load Balancing connection draining. For more information, see Connection Draining
            
            
    :type LifecycleEventConfiguration: dict
    """
    pass


def update_my_user_profile(SshPublicKey=None):
    """
    :param SshPublicKey: The user's SSH public key.
            ReturnsNone
            
    :type SshPublicKey: string
    """
    pass


def update_rds_db_instance(RdsDbInstanceArn=None, DbUser=None, DbPassword=None):
    """
    :param RdsDbInstanceArn: [REQUIRED]
            The Amazon RDS instance's ARN.
            
    :type RdsDbInstanceArn: string
    :param DbUser: The master user name.
    :type DbUser: string
    :param DbPassword: The database password.
    :type DbPassword: string
    """
    pass


def update_stack(StackId=None, Name=None, Attributes=None, ServiceRoleArn=None, DefaultInstanceProfileArn=None,
                 DefaultOs=None, HostnameTheme=None, DefaultAvailabilityZone=None, DefaultSubnetId=None,
                 CustomJson=None, ConfigurationManager=None, ChefConfiguration=None, UseCustomCookbooks=None,
                 CustomCookbooksSource=None, DefaultSshKeyName=None, DefaultRootDeviceType=None,
                 UseOpsworksSecurityGroups=None, AgentVersion=None):
    """
    :param StackId: [REQUIRED]
            The stack ID.
            
    :type StackId: string
    :param Name: The stack's new name.
    :type Name: string
    :param Attributes: One or more user-defined key-value pairs to be added to the stack attributes.
            (string) --
            (string) --
            
    :type Attributes: dict
    :param ServiceRoleArn: Do not use this parameter. You cannot update a stack's service role.
    :type ServiceRoleArn: string
    :param DefaultInstanceProfileArn: The ARN of an IAM profile that is the default profile for all of the stack's EC2 instances. For more information about IAM ARNs, see Using Identifiers .
    :type DefaultInstanceProfileArn: string
    :param DefaultOs: The stack's operating system, which must be set to one of the following:
            A supported Linux operating system: An Amazon Linux version, such as Amazon Linux 2016.03 , Amazon Linux 2015.09 , or Amazon Linux 2015.03 .
            A supported Ubuntu operating system, such as Ubuntu 16.04 LTS , Ubuntu 14.04 LTS , or Ubuntu 12.04 LTS .
            CentOS 7
            Red Hat Enterprise Linux 7
            A supported Windows operating system, such as Microsoft Windows Server 2012 R2 Base , Microsoft Windows Server 2012 R2 with SQL Server Express , Microsoft Windows Server 2012 R2 with SQL Server Standard , or Microsoft Windows Server 2012 R2 with SQL Server Web .
            A custom AMI: Custom . You specify the custom AMI you want to use when you create instances. For more information on how to use custom AMIs with OpsWorks, see Using Custom AMIs .
            The default option is the stack's current operating system. For more information on the supported operating systems, see AWS OpsWorks Operating Systems .
            
    :type DefaultOs: string
    :param HostnameTheme: The stack's new host name theme, with spaces replaced by underscores. The theme is used to generate host names for the stack's instances. By default, HostnameTheme is set to Layer_Dependent , which creates host names by appending integers to the layer's short name. The other themes are:
            Baked_Goods
            Clouds
            Europe_Cities
            Fruits
            Greek_Deities
            Legendary_creatures_from_Japan
            Planets_and_Moons
            Roman_Deities
            Scottish_Islands
            US_Cities
            Wild_Cats
            To obtain a generated host name, call GetHostNameSuggestion , which returns a host name based on the current theme.
            
    :type HostnameTheme: string
    :param DefaultAvailabilityZone: The stack's default Availability Zone, which must be in the stack's region. For more information, see Regions and Endpoints . If you also specify a value for DefaultSubnetId , the subnet must be in the same zone. For more information, see CreateStack .
    :type DefaultAvailabilityZone: string
    :param DefaultSubnetId: The stack's default VPC subnet ID. This parameter is required if you specify a value for the VpcId parameter. All instances are launched into this subnet unless you specify otherwise when you create the instance. If you also specify a value for DefaultAvailabilityZone , the subnet must be in that zone. For information on default values and when this parameter is required, see the VpcId parameter description.
    :type DefaultSubnetId: string
    :param CustomJson: A string that contains user-defined, custom JSON. It can be used to override the corresponding default stack configuration JSON values or to pass data to recipes. The string should be in the following format:
            '{\'key1\': \'value1\', \'key2\': \'value2\',...}'
            For more information on custom JSON, see Use Custom JSON to Modify the Stack Configuration Attributes .
            
    :type CustomJson: string
    :param ConfigurationManager: The configuration manager. When you update a stack, we recommend that you use the configuration manager to specify the Chef version: 12, 11.10, or 11.4 for Linux stacks, or 12.2 for Windows stacks. The default value for Linux stacks is currently 11.4.
            Name (string) --The name. This parameter must be set to 'Chef'.
            Version (string) --The Chef version. This parameter must be set to 12, 11.10, or 11.4 for Linux stacks, and to 12.2 for Windows stacks. The default value for Linux stacks is 11.4.
            
    :type ConfigurationManager: dict
    :param ChefConfiguration: A ChefConfiguration object that specifies whether to enable Berkshelf and the Berkshelf version on Chef 11.10 stacks. For more information, see Create a New Stack .
            ManageBerkshelf (boolean) --Whether to enable Berkshelf.
            BerkshelfVersion (string) --The Berkshelf version.
            
    :type ChefConfiguration: dict
    :param UseCustomCookbooks: Whether the stack uses custom cookbooks.
    :type UseCustomCookbooks: boolean
    :param CustomCookbooksSource: Contains the information required to retrieve an app or cookbook from a repository. For more information, see Creating Apps or Custom Recipes and Cookbooks .
            Type (string) --The repository type.
            Url (string) --The source URL.
            Username (string) --This parameter depends on the repository type.
            For Amazon S3 bundles, set Username to the appropriate IAM access key ID.
            For HTTP bundles, Git repositories, and Subversion repositories, set Username to the user name.
            Password (string) --When included in a request, the parameter depends on the repository type.
            For Amazon S3 bundles, set Password to the appropriate IAM secret access key.
            For HTTP bundles and Subversion repositories, set Password to the password.
            For more information on how to safely handle IAM credentials, see http://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html .
            In responses, AWS OpsWorks returns *****FILTERED***** instead of the actual value.
            SshKey (string) --In requests, the repository's SSH key.
            In responses, AWS OpsWorks returns *****FILTERED***** instead of the actual value.
            Revision (string) --The application's version. AWS OpsWorks enables you to easily deploy new versions of an application. One of the simplest approaches is to have branches or revisions in your repository that represent different versions that can potentially be deployed.
            
    :type CustomCookbooksSource: dict
    :param DefaultSshKeyName: A default Amazon EC2 key-pair name. The default value is none . If you specify a key-pair name, AWS OpsWorks installs the public key on the instance and you can use the private key with an SSH client to log in to the instance. For more information, see Using SSH to Communicate with an Instance and Managing SSH Access . You can override this setting by specifying a different key pair, or no key pair, when you create an instance .
    :type DefaultSshKeyName: string
    :param DefaultRootDeviceType: The default root device type. This value is used by default for all instances in the stack, but you can override it when you create an instance. For more information, see Storage for the Root Device .
    :type DefaultRootDeviceType: string
    :param UseOpsworksSecurityGroups: Whether to associate the AWS OpsWorks built-in security groups with the stack's layers.
            AWS OpsWorks provides a standard set of built-in security groups, one for each layer, which are associated with layers by default. UseOpsworksSecurityGroups allows you to provide your own custom security groups instead of using the built-in groups. UseOpsworksSecurityGroups has the following settings:
            True - AWS OpsWorks automatically associates the appropriate built-in security group with each layer (default setting). You can associate additional security groups with a layer after you create it, but you cannot delete the built-in security group.
            False - AWS OpsWorks does not associate built-in security groups with layers. You must create appropriate EC2 security groups and associate a security group with each layer that you create. However, you can still manually associate a built-in security group with a layer on. Custom security groups are required only for those layers that need custom settings.
            For more information, see Create a New Stack .
            
    :type UseOpsworksSecurityGroups: boolean
    :param AgentVersion: The default AWS OpsWorks agent version. You have the following options:
            Auto-update - Set this parameter to LATEST . AWS OpsWorks automatically installs new agent versions on the stack's instances as soon as they are available.
            Fixed version - Set this parameter to your preferred agent version. To update the agent version, you must edit the stack configuration and specify a new version. AWS OpsWorks then automatically installs that version on the stack's instances.
            The default setting is LATEST . To specify an agent version, you must use the complete version number, not the abbreviated number shown on the console. For a list of available agent version numbers, call DescribeAgentVersions .
            Note
            You can also specify an agent version when you create or update an instance, which overrides the stack's default setting.
            
    :type AgentVersion: string
    """
    pass


def update_user_profile(IamUserArn=None, SshUsername=None, SshPublicKey=None, AllowSelfManagement=None):
    """
    :param IamUserArn: [REQUIRED]
            The user IAM ARN. This can also be a federated user's ARN.
            
    :type IamUserArn: string
    :param SshUsername: The user's SSH user name. The allowable characters are [a-z], [A-Z], [0-9], '-', and '_'. If the specified name includes other punctuation marks, AWS OpsWorks removes them. For example, my.name will be changed to myname . If you do not specify an SSH user name, AWS OpsWorks generates one from the IAM user name.
    :type SshUsername: string
    :param SshPublicKey: The user's new SSH public key.
    :type SshPublicKey: string
    :param AllowSelfManagement: Whether users can specify their own SSH public key through the My Settings page. For more information, see Managing User Permissions .
    :type AllowSelfManagement: boolean
    """
    pass


def update_volume(VolumeId=None, Name=None, MountPoint=None):
    """
    :param VolumeId: [REQUIRED]
            The volume ID.
            
    :type VolumeId: string
    :param Name: The new name.
    :type Name: string
    :param MountPoint: The new mount point.
    :type MountPoint: string
    """
    pass
