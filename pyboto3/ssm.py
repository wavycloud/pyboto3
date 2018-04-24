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

def add_tags_to_resource(ResourceType=None, ResourceId=None, Tags=None):
    """
    Adds or overwrites one or more tags for the specified resource. Tags are metadata that you can assign to your documents, managed instances, Maintenance Windows, Parameter Store parameters, and patch baselines. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment. Each tag consists of a key and an optional value, both of which you define. For example, you could define a set of tags for your account's managed instances that helps you track each instance's owner and stack level. For example: Key=Owner and Value=DbAdmin, SysAdmin, or Dev. Or Key=Stack and Value=Production, Pre-Production, or Test.
    Each resource can have a maximum of 50 tags.
    We recommend that you devise a set of tag keys that meets your needs for each resource type. Using a consistent set of tag keys makes it easier for you to manage your resources. You can search and filter the resources based on the tags you add. Tags don't have any semantic meaning to Amazon EC2 and are interpreted strictly as a string of characters.
    For more information about tags, see Tagging Your Amazon EC2 Resources in the Amazon EC2 User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.add_tags_to_resource(
        ResourceType='Document'|'ManagedInstance'|'MaintenanceWindow'|'Parameter'|'PatchBaseline',
        ResourceId='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ResourceType: string
    :param ResourceType: [REQUIRED]
            Specifies the type of resource you are tagging.
            

    :type ResourceId: string
    :param ResourceId: [REQUIRED]
            The resource ID you want to tag.
            For the ManagedInstance, MaintenanceWindow, and PatchBaseline values, use the ID of the resource, such as mw-01234361858c9b57b for a Maintenance Window.
            For the Document and Parameter values, use the name of the resource.
            

    :type Tags: list
    :param Tags: [REQUIRED]
            One or more tags. The value parameter is required, but if you don't want the tag to have a value, specify the parameter with no value, and we set the value to an empty string.
            (dict) --Metadata that you assign to your AWS resources. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment. In Systems Manager, you can apply tags to documents, managed instances, Maintenance Windows, Parameter Store parameters, and patch baselines.
            Key (string) -- [REQUIRED]The name of the tag.
            Value (string) -- [REQUIRED]The value of the tag.
            
            

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

def cancel_command(CommandId=None, InstanceIds=None):
    """
    Attempts to cancel the command specified by the Command ID. There is no guarantee that the command will be terminated and the underlying process stopped.
    See also: AWS API Documentation
    
    
    :example: response = client.cancel_command(
        CommandId='string',
        InstanceIds=[
            'string',
        ]
    )
    
    
    :type CommandId: string
    :param CommandId: [REQUIRED]
            The ID of the command you want to cancel.
            

    :type InstanceIds: list
    :param InstanceIds: (Optional) A list of instance IDs on which you want to cancel the command. If not provided, the command is canceled on every instance on which it was requested.
            (string) --
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def create_activation(Description=None, DefaultInstanceName=None, IamRole=None, RegistrationLimit=None, ExpirationDate=None):
    """
    Registers your on-premises server or virtual machine with Amazon EC2 so that you can manage these resources using Run Command. An on-premises server or virtual machine that has been registered with EC2 is called a managed instance. For more information about activations, see Setting Up Systems Manager in Hybrid Environments .
    See also: AWS API Documentation
    
    
    :example: response = client.create_activation(
        Description='string',
        DefaultInstanceName='string',
        IamRole='string',
        RegistrationLimit=123,
        ExpirationDate=datetime(2015, 1, 1)
    )
    
    
    :type Description: string
    :param Description: A userdefined description of the resource that you want to register with Amazon EC2.

    :type DefaultInstanceName: string
    :param DefaultInstanceName: The name of the registered, managed instance as it will appear in the Amazon EC2 console or when you use the AWS command line tools to list EC2 resources.

    :type IamRole: string
    :param IamRole: [REQUIRED]
            The Amazon Identity and Access Management (IAM) role that you want to assign to the managed instance.
            

    :type RegistrationLimit: integer
    :param RegistrationLimit: Specify the maximum number of managed instances you want to register. The default value is 1 instance.

    :type ExpirationDate: datetime
    :param ExpirationDate: The date by which this activation request should expire. The default value is 24 hours.

    :rtype: dict
    :return: {
        'ActivationId': 'string',
        'ActivationCode': 'string'
    }
    
    
    """
    pass

def create_association(Name=None, DocumentVersion=None, InstanceId=None, Parameters=None, Targets=None, ScheduleExpression=None, OutputLocation=None, AssociationName=None):
    """
    Associates the specified Systems Manager document with the specified instances or targets.
    When you associate a document with one or more instances using instance IDs or tags, the SSM Agent running on the instance processes the document and configures the instance as specified.
    If you associate a document with an instance that already has an associated document, the system throws the AssociationAlreadyExists exception.
    See also: AWS API Documentation
    
    
    :example: response = client.create_association(
        Name='string',
        DocumentVersion='string',
        InstanceId='string',
        Parameters={
            'string': [
                'string',
            ]
        },
        Targets=[
            {
                'Key': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        ScheduleExpression='string',
        OutputLocation={
            'S3Location': {
                'OutputS3Region': 'string',
                'OutputS3BucketName': 'string',
                'OutputS3KeyPrefix': 'string'
            }
        },
        AssociationName='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the Systems Manager document.
            

    :type DocumentVersion: string
    :param DocumentVersion: The document version you want to associate with the target(s). Can be a specific version or the default version.

    :type InstanceId: string
    :param InstanceId: The instance ID.

    :type Parameters: dict
    :param Parameters: The parameters for the documents runtime configuration.
            (string) --
            (list) --
            (string) --
            
            

    :type Targets: list
    :param Targets: The targets (either instances or tags) for the association.
            (dict) --An array of search criteria that targets instances using a Key,Value combination that you specify. Targets is required if you don't provide one or more instance IDs in the call.
            Key (string) --User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:Amazon EC2 tagor InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see Executing a Command Using Systems Manager Run Command .
            Values (list) --User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see Executing a Command Using Systems Manager Run Command .
            (string) --
            
            

    :type ScheduleExpression: string
    :param ScheduleExpression: A cron expression when the association will be applied to the target(s).

    :type OutputLocation: dict
    :param OutputLocation: An Amazon S3 bucket where you want to store the output details of the request.
            S3Location (dict) --An Amazon S3 bucket where you want to store the results of this request.
            OutputS3Region (string) --(Deprecated) You can no longer specify this parameter. The system ignores it. Instead, Systems Manager automatically determines the Amazon S3 bucket region.
            OutputS3BucketName (string) --The name of the Amazon S3 bucket.
            OutputS3KeyPrefix (string) --The Amazon S3 bucket subfolder.
            
            

    :type AssociationName: string
    :param AssociationName: Specify a descriptive name for the association.

    :rtype: dict
    :return: {
        'AssociationDescription': {
            'Name': 'string',
            'InstanceId': 'string',
            'AssociationVersion': 'string',
            'Date': datetime(2015, 1, 1),
            'LastUpdateAssociationDate': datetime(2015, 1, 1),
            'Status': {
                'Date': datetime(2015, 1, 1),
                'Name': 'Pending'|'Success'|'Failed',
                'Message': 'string',
                'AdditionalInfo': 'string'
            },
            'Overview': {
                'Status': 'string',
                'DetailedStatus': 'string',
                'AssociationStatusAggregatedCount': {
                    'string': 123
                }
            },
            'DocumentVersion': 'string',
            'Parameters': {
                'string': [
                    'string',
                ]
            },
            'AssociationId': 'string',
            'Targets': [
                {
                    'Key': 'string',
                    'Values': [
                        'string',
                    ]
                },
            ],
            'ScheduleExpression': 'string',
            'OutputLocation': {
                'S3Location': {
                    'OutputS3Region': 'string',
                    'OutputS3BucketName': 'string',
                    'OutputS3KeyPrefix': 'string'
                }
            },
            'LastExecutionDate': datetime(2015, 1, 1),
            'LastSuccessfulExecutionDate': datetime(2015, 1, 1),
            'AssociationName': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (integer) --
    
    
    
    """
    pass

def create_association_batch(Entries=None):
    """
    Associates the specified Systems Manager document with the specified instances or targets.
    When you associate a document with one or more instances using instance IDs or tags, the SSM Agent running on the instance processes the document and configures the instance as specified.
    If you associate a document with an instance that already has an associated document, the system throws the AssociationAlreadyExists exception.
    See also: AWS API Documentation
    
    
    :example: response = client.create_association_batch(
        Entries=[
            {
                'Name': 'string',
                'InstanceId': 'string',
                'Parameters': {
                    'string': [
                        'string',
                    ]
                },
                'DocumentVersion': 'string',
                'Targets': [
                    {
                        'Key': 'string',
                        'Values': [
                            'string',
                        ]
                    },
                ],
                'ScheduleExpression': 'string',
                'OutputLocation': {
                    'S3Location': {
                        'OutputS3Region': 'string',
                        'OutputS3BucketName': 'string',
                        'OutputS3KeyPrefix': 'string'
                    }
                },
                'AssociationName': 'string'
            },
        ]
    )
    
    
    :type Entries: list
    :param Entries: [REQUIRED]
            One or more associations.
            (dict) --Describes the association of a Systems Manager document and an instance.
            Name (string) -- [REQUIRED]The name of the configuration document.
            InstanceId (string) --The ID of the instance.
            Parameters (dict) --A description of the parameters for a document.
            (string) --
            (list) --
            (string) --
            
            DocumentVersion (string) --The document version.
            Targets (list) --The instances targeted by the request.
            (dict) --An array of search criteria that targets instances using a Key,Value combination that you specify. Targets is required if you don't provide one or more instance IDs in the call.
            Key (string) --User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:Amazon EC2 tagor InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see Executing a Command Using Systems Manager Run Command .
            Values (list) --User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see Executing a Command Using Systems Manager Run Command .
            (string) --
            
            ScheduleExpression (string) --A cron expression that specifies a schedule when the association runs.
            OutputLocation (dict) --An Amazon S3 bucket where you want to store the results of this request.
            S3Location (dict) --An Amazon S3 bucket where you want to store the results of this request.
            OutputS3Region (string) --(Deprecated) You can no longer specify this parameter. The system ignores it. Instead, Systems Manager automatically determines the Amazon S3 bucket region.
            OutputS3BucketName (string) --The name of the Amazon S3 bucket.
            OutputS3KeyPrefix (string) --The Amazon S3 bucket subfolder.
            
            AssociationName (string) --Specify a descriptive name for the association.
            
            

    :rtype: dict
    :return: {
        'Successful': [
            {
                'Name': 'string',
                'InstanceId': 'string',
                'AssociationVersion': 'string',
                'Date': datetime(2015, 1, 1),
                'LastUpdateAssociationDate': datetime(2015, 1, 1),
                'Status': {
                    'Date': datetime(2015, 1, 1),
                    'Name': 'Pending'|'Success'|'Failed',
                    'Message': 'string',
                    'AdditionalInfo': 'string'
                },
                'Overview': {
                    'Status': 'string',
                    'DetailedStatus': 'string',
                    'AssociationStatusAggregatedCount': {
                        'string': 123
                    }
                },
                'DocumentVersion': 'string',
                'Parameters': {
                    'string': [
                        'string',
                    ]
                },
                'AssociationId': 'string',
                'Targets': [
                    {
                        'Key': 'string',
                        'Values': [
                            'string',
                        ]
                    },
                ],
                'ScheduleExpression': 'string',
                'OutputLocation': {
                    'S3Location': {
                        'OutputS3Region': 'string',
                        'OutputS3BucketName': 'string',
                        'OutputS3KeyPrefix': 'string'
                    }
                },
                'LastExecutionDate': datetime(2015, 1, 1),
                'LastSuccessfulExecutionDate': datetime(2015, 1, 1),
                'AssociationName': 'string'
            },
        ],
        'Failed': [
            {
                'Entry': {
                    'Name': 'string',
                    'InstanceId': 'string',
                    'Parameters': {
                        'string': [
                            'string',
                        ]
                    },
                    'DocumentVersion': 'string',
                    'Targets': [
                        {
                            'Key': 'string',
                            'Values': [
                                'string',
                            ]
                        },
                    ],
                    'ScheduleExpression': 'string',
                    'OutputLocation': {
                        'S3Location': {
                            'OutputS3Region': 'string',
                            'OutputS3BucketName': 'string',
                            'OutputS3KeyPrefix': 'string'
                        }
                    },
                    'AssociationName': 'string'
                },
                'Message': 'string',
                'Fault': 'Client'|'Server'|'Unknown'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_document(Content=None, Name=None, DocumentType=None, DocumentFormat=None, TargetType=None):
    """
    Creates a Systems Manager document.
    After you create a document, you can use CreateAssociation to associate it with one or more running instances.
    See also: AWS API Documentation
    
    
    :example: response = client.create_document(
        Content='string',
        Name='string',
        DocumentType='Command'|'Policy'|'Automation',
        DocumentFormat='YAML'|'JSON',
        TargetType='string'
    )
    
    
    :type Content: string
    :param Content: [REQUIRED]
            A valid JSON or YAML string.
            

    :type Name: string
    :param Name: [REQUIRED]
            A name for the Systems Manager document.
            Warning
            Do not use the following to begin the names of documents you create. They are reserved by AWS for use as document prefixes:
            aws
            amazon
            amzn
            

    :type DocumentType: string
    :param DocumentType: The type of document to create. Valid document types include: Policy, Automation, and Command.

    :type DocumentFormat: string
    :param DocumentFormat: Specify the document format for the request. The document format can be either JSON or YAML. JSON is the default format.

    :type TargetType: string
    :param TargetType: Specify a target type to define the kinds of resources the document can run on. For example, to run a document on EC2 instances, specify the following value: /AWS::EC2::Instance. If you specify a value of '/' the document can run on all types of resources. If you don't specify a value, the document can't run on any resources. For a list of valid resource types, see AWS Resource Types Reference in the AWS CloudFormation User Guide .

    :rtype: dict
    :return: {
        'DocumentDescription': {
            'Sha1': 'string',
            'Hash': 'string',
            'HashType': 'Sha256'|'Sha1',
            'Name': 'string',
            'Owner': 'string',
            'CreatedDate': datetime(2015, 1, 1),
            'Status': 'Creating'|'Active'|'Updating'|'Deleting',
            'DocumentVersion': 'string',
            'Description': 'string',
            'Parameters': [
                {
                    'Name': 'string',
                    'Type': 'String'|'StringList',
                    'Description': 'string',
                    'DefaultValue': 'string'
                },
            ],
            'PlatformTypes': [
                'Windows'|'Linux',
            ],
            'DocumentType': 'Command'|'Policy'|'Automation',
            'SchemaVersion': 'string',
            'LatestVersion': 'string',
            'DefaultVersion': 'string',
            'DocumentFormat': 'YAML'|'JSON',
            'TargetType': 'string',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_maintenance_window(Name=None, Description=None, Schedule=None, Duration=None, Cutoff=None, AllowUnassociatedTargets=None, ClientToken=None):
    """
    Creates a new Maintenance Window.
    See also: AWS API Documentation
    
    
    :example: response = client.create_maintenance_window(
        Name='string',
        Description='string',
        Schedule='string',
        Duration=123,
        Cutoff=123,
        AllowUnassociatedTargets=True|False,
        ClientToken='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the Maintenance Window.
            

    :type Description: string
    :param Description: An optional description for the Maintenance Window. We recommend specifying a description to help you organize your Maintenance Windows.

    :type Schedule: string
    :param Schedule: [REQUIRED]
            The schedule of the Maintenance Window in the form of a cron or rate expression.
            

    :type Duration: integer
    :param Duration: [REQUIRED]
            The duration of the Maintenance Window in hours.
            

    :type Cutoff: integer
    :param Cutoff: [REQUIRED]
            The number of hours before the end of the Maintenance Window that Systems Manager stops scheduling new tasks for execution.
            

    :type AllowUnassociatedTargets: boolean
    :param AllowUnassociatedTargets: [REQUIRED]
            Enables a Maintenance Window task to execute on managed instances, even if you have not registered those instances as targets. If enabled, then you must specify the unregistered instances (by instance ID) when you register a task with the Maintenance Window
            If you don't enable this option, then you must specify previously-registered targets when you register a task with the Maintenance Window.
            

    :type ClientToken: string
    :param ClientToken: User-provided idempotency token.
            This field is autopopulated if not provided.
            

    :rtype: dict
    :return: {
        'WindowId': 'string'
    }
    
    
    """
    pass

def create_patch_baseline(OperatingSystem=None, Name=None, GlobalFilters=None, ApprovalRules=None, ApprovedPatches=None, ApprovedPatchesComplianceLevel=None, ApprovedPatchesEnableNonSecurity=None, RejectedPatches=None, Description=None, Sources=None, ClientToken=None):
    """
    Creates a patch baseline.
    See also: AWS API Documentation
    
    
    :example: response = client.create_patch_baseline(
        OperatingSystem='WINDOWS'|'AMAZON_LINUX'|'UBUNTU'|'REDHAT_ENTERPRISE_LINUX'|'SUSE'|'CENTOS',
        Name='string',
        GlobalFilters={
            'PatchFilters': [
                {
                    'Key': 'PRODUCT'|'CLASSIFICATION'|'MSRC_SEVERITY'|'PATCH_ID'|'SECTION'|'PRIORITY'|'SEVERITY',
                    'Values': [
                        'string',
                    ]
                },
            ]
        },
        ApprovalRules={
            'PatchRules': [
                {
                    'PatchFilterGroup': {
                        'PatchFilters': [
                            {
                                'Key': 'PRODUCT'|'CLASSIFICATION'|'MSRC_SEVERITY'|'PATCH_ID'|'SECTION'|'PRIORITY'|'SEVERITY',
                                'Values': [
                                    'string',
                                ]
                            },
                        ]
                    },
                    'ComplianceLevel': 'CRITICAL'|'HIGH'|'MEDIUM'|'LOW'|'INFORMATIONAL'|'UNSPECIFIED',
                    'ApproveAfterDays': 123,
                    'EnableNonSecurity': True|False
                },
            ]
        },
        ApprovedPatches=[
            'string',
        ],
        ApprovedPatchesComplianceLevel='CRITICAL'|'HIGH'|'MEDIUM'|'LOW'|'INFORMATIONAL'|'UNSPECIFIED',
        ApprovedPatchesEnableNonSecurity=True|False,
        RejectedPatches=[
            'string',
        ],
        Description='string',
        Sources=[
            {
                'Name': 'string',
                'Products': [
                    'string',
                ],
                'Configuration': 'string'
            },
        ],
        ClientToken='string'
    )
    
    
    :type OperatingSystem: string
    :param OperatingSystem: Defines the operating system the patch baseline applies to. The Default value is WINDOWS.

    :type Name: string
    :param Name: [REQUIRED]
            The name of the patch baseline.
            

    :type GlobalFilters: dict
    :param GlobalFilters: A set of global filters used to exclude patches from the baseline.
            PatchFilters (list) -- [REQUIRED]The set of patch filters that make up the group.
            (dict) --Defines a patch filter.
            A patch filter consists of key/value pairs, but not all keys are valid for all operating system types. For example, the key PRODUCT is valid for all supported operating system types. The key MSRC_SEVERITY , however, is valid only for Windows operating systems, and the key SECTION is valid only for Ubuntu operating systems.
            Refer to the following sections for information about which keys may be used with each major operating system, and which values are valid for each key.
            Windows Operating Systems
            The supported keys for Windows operating systems are PRODUCT , CLASSIFICATION , and MSRC_SEVERITY . See the following lists for valid values for each of these keys.
            Supported key: PRODUCTSupported values:
            Windows7
            Windows8
            Windows8.1
            Windows8Embedded
            Windows10
            Windows10LTSB
            WindowsServer2008
            WindowsServer2008R2
            WindowsServer2012
            WindowsServer2012R2
            WindowsServer2016
            Supported key: CLASSIFICATIONSupported values:
            CriticalUpdates
            DefinitionUpdates
            Drivers
            FeaturePacks
            SecurityUpdates
            ServicePacks
            Tools
            UpdateRollups
            Updates
            Upgrades
            Supported key: MSRC_SEVERITYSupported values:
            Critical
            Important
            Moderate
            Low
            Unspecified
            Ubuntu Operating Systems
            The supported keys for Ubuntu operating systems are PRODUCT , PRIORITY , and SECTION . See the following lists for valid values for each of these keys.
            Supported key: PRODUCTSupported values:
            Ubuntu14.04
            Ubuntu16.04
            Supported key: PRIORITYSupported values:
            Required
            Important
            Standard
            Optional
            Extra
            Supported key: SECTION
            Only the length of the key value is validated. Minimum length is 1. Maximum length is 64.
            Amazon Linux Operating Systems
            The supported keys for Amazon Linux operating systems are PRODUCT , CLASSIFICATION , and SEVERITY . See the following lists for valid values for each of these keys.
            Supported key: PRODUCTSupported values:
            AmazonLinux2012.03
            AmazonLinux2012.09
            AmazonLinux2013.03
            AmazonLinux2013.09
            AmazonLinux2014.03
            AmazonLinux2014.09
            AmazonLinux2015.03
            AmazonLinux2015.09
            AmazonLinux2016.03
            AmazonLinux2016.09
            AmazonLinux2017.03
            AmazonLinux2017.09
            Supported key: CLASSIFICATIONSupported values:
            Security
            Bugfix
            Enhancement
            Recommended
            Newpackage
            Supported key: SEVERITYSupported values:
            Critical
            Important
            Medium
            Low
            RedHat Enterprise Linux (RHEL) Operating Systems
            The supported keys for RedHat Enterprise Linux operating systems are PRODUCT , CLASSIFICATION , and SEVERITY . See the following lists for valid values for each of these keys.
            Supported key: PRODUCTSupported values:
            RedhatEnterpriseLinux6.5
            RedhatEnterpriseLinux6.6
            RedhatEnterpriseLinux6.7
            RedhatEnterpriseLinux6.8
            RedhatEnterpriseLinux6.9
            RedhatEnterpriseLinux7.0
            RedhatEnterpriseLinux7.1
            RedhatEnterpriseLinux7.2
            RedhatEnterpriseLinux7.3
            RedhatEnterpriseLinux7.4
            Supported key: CLASSIFICATIONSupported values:
            Security
            Bugfix
            Enhancement
            Recommended
            Newpackage
            Supported key: SEVERITYSupported values:
            Critical
            Important
            Medium
            Low
            SUSE Linux Enterprise Server (SUSE) Operating Systems
            The supported keys for SUSE operating systems are PRODUCT , CLASSIFICATION , and SEVERITY . See the following lists for valid values for each of these keys.
            Supported key: PRODUCTSupported values:
            Suse12.0
            Suse12.1
            Suse12.2
            Suse12.3
            Suse12.4
            Suse12.5
            Suse12.6
            Suse12.7
            Suse12.8
            Suse12.9
            Supported key: CLASSIFICATIONSupported values:
            Security
            Recommended
            Optional
            Feature
            Document
            Yast
            Supported key: SEVERITYSupported values:
            Critical
            Important
            Moderate
            Low
            Key (string) -- [REQUIRED]The key for the filter.
            See PatchFilter for lists of valid keys for each operating system type.
            Values (list) -- [REQUIRED]The value for the filter key.
            See PatchFilter for lists of valid values for each key based on operating system type.
            (string) --
            
            

    :type ApprovalRules: dict
    :param ApprovalRules: A set of rules used to include patches in the baseline.
            PatchRules (list) -- [REQUIRED]The rules that make up the rule group.
            (dict) --Defines an approval rule for a patch baseline.
            PatchFilterGroup (dict) -- [REQUIRED]The patch filter group that defines the criteria for the rule.
            PatchFilters (list) -- [REQUIRED]The set of patch filters that make up the group.
            (dict) --Defines a patch filter.
            A patch filter consists of key/value pairs, but not all keys are valid for all operating system types. For example, the key PRODUCT is valid for all supported operating system types. The key MSRC_SEVERITY , however, is valid only for Windows operating systems, and the key SECTION is valid only for Ubuntu operating systems.
            Refer to the following sections for information about which keys may be used with each major operating system, and which values are valid for each key.
            Windows Operating Systems
            The supported keys for Windows operating systems are PRODUCT , CLASSIFICATION , and MSRC_SEVERITY . See the following lists for valid values for each of these keys.
            Supported key: PRODUCTSupported values:
            Windows7
            Windows8
            Windows8.1
            Windows8Embedded
            Windows10
            Windows10LTSB
            WindowsServer2008
            WindowsServer2008R2
            WindowsServer2012
            WindowsServer2012R2
            WindowsServer2016
            Supported key: CLASSIFICATIONSupported values:
            CriticalUpdates
            DefinitionUpdates
            Drivers
            FeaturePacks
            SecurityUpdates
            ServicePacks
            Tools
            UpdateRollups
            Updates
            Upgrades
            Supported key: MSRC_SEVERITYSupported values:
            Critical
            Important
            Moderate
            Low
            Unspecified
            Ubuntu Operating Systems
            The supported keys for Ubuntu operating systems are PRODUCT , PRIORITY , and SECTION . See the following lists for valid values for each of these keys.
            Supported key: PRODUCTSupported values:
            Ubuntu14.04
            Ubuntu16.04
            Supported key: PRIORITYSupported values:
            Required
            Important
            Standard
            Optional
            Extra
            Supported key: SECTION
            Only the length of the key value is validated. Minimum length is 1. Maximum length is 64.
            Amazon Linux Operating Systems
            The supported keys for Amazon Linux operating systems are PRODUCT , CLASSIFICATION , and SEVERITY . See the following lists for valid values for each of these keys.
            Supported key: PRODUCTSupported values:
            AmazonLinux2012.03
            AmazonLinux2012.09
            AmazonLinux2013.03
            AmazonLinux2013.09
            AmazonLinux2014.03
            AmazonLinux2014.09
            AmazonLinux2015.03
            AmazonLinux2015.09
            AmazonLinux2016.03
            AmazonLinux2016.09
            AmazonLinux2017.03
            AmazonLinux2017.09
            Supported key: CLASSIFICATIONSupported values:
            Security
            Bugfix
            Enhancement
            Recommended
            Newpackage
            Supported key: SEVERITYSupported values:
            Critical
            Important
            Medium
            Low
            RedHat Enterprise Linux (RHEL) Operating Systems
            The supported keys for RedHat Enterprise Linux operating systems are PRODUCT , CLASSIFICATION , and SEVERITY . See the following lists for valid values for each of these keys.
            Supported key: PRODUCTSupported values:
            RedhatEnterpriseLinux6.5
            RedhatEnterpriseLinux6.6
            RedhatEnterpriseLinux6.7
            RedhatEnterpriseLinux6.8
            RedhatEnterpriseLinux6.9
            RedhatEnterpriseLinux7.0
            RedhatEnterpriseLinux7.1
            RedhatEnterpriseLinux7.2
            RedhatEnterpriseLinux7.3
            RedhatEnterpriseLinux7.4
            Supported key: CLASSIFICATIONSupported values:
            Security
            Bugfix
            Enhancement
            Recommended
            Newpackage
            Supported key: SEVERITYSupported values:
            Critical
            Important
            Medium
            Low
            SUSE Linux Enterprise Server (SUSE) Operating Systems
            The supported keys for SUSE operating systems are PRODUCT , CLASSIFICATION , and SEVERITY . See the following lists for valid values for each of these keys.
            Supported key: PRODUCTSupported values:
            Suse12.0
            Suse12.1
            Suse12.2
            Suse12.3
            Suse12.4
            Suse12.5
            Suse12.6
            Suse12.7
            Suse12.8
            Suse12.9
            Supported key: CLASSIFICATIONSupported values:
            Security
            Recommended
            Optional
            Feature
            Document
            Yast
            Supported key: SEVERITYSupported values:
            Critical
            Important
            Moderate
            Low
            Key (string) -- [REQUIRED]The key for the filter.
            See PatchFilter for lists of valid keys for each operating system type.
            Values (list) -- [REQUIRED]The value for the filter key.
            See PatchFilter for lists of valid values for each key based on operating system type.
            (string) --
            
            
            ComplianceLevel (string) --A compliance severity level for all approved patches in a patch baseline. Valid compliance severity levels include the following: Unspecified, Critical, High, Medium, Low, and Informational.
            ApproveAfterDays (integer) -- [REQUIRED]The number of days after the release date of each patch matched by the rule the patch is marked as approved in the patch baseline.
            EnableNonSecurity (boolean) --For instances identified by the approval rule filters, enables a patch baseline to apply non-security updates available in the specified repository. The default value is 'false'. Applies to Linux instances only.
            
            

    :type ApprovedPatches: list
    :param ApprovedPatches: A list of explicitly approved patches for the baseline.
            (string) --
            

    :type ApprovedPatchesComplianceLevel: string
    :param ApprovedPatchesComplianceLevel: Defines the compliance level for approved patches. This means that if an approved patch is reported as missing, this is the severity of the compliance violation. Valid compliance severity levels include the following: CRITICAL, HIGH, MEDIUM, LOW, INFORMATIONAL, UNSPECIFIED. The default value is UNSPECIFIED.

    :type ApprovedPatchesEnableNonSecurity: boolean
    :param ApprovedPatchesEnableNonSecurity: Indicates whether the list of approved patches includes non-security updates that should be applied to the instances. The default value is 'false'. Applies to Linux instances only.

    :type RejectedPatches: list
    :param RejectedPatches: A list of explicitly rejected patches for the baseline.
            (string) --
            

    :type Description: string
    :param Description: A description of the patch baseline.

    :type Sources: list
    :param Sources: Information about the patches to use to update the instances, including target operating systems and source repositories. Applies to Linux instances only.
            (dict) --Information about the patches to use to update the instances, including target operating systems and source repository. Applies to Linux instances only.
            Name (string) -- [REQUIRED]The name specified to identify the patch source.
            Products (list) -- [REQUIRED]The specific operating system versions a patch repository applies to, such as 'Ubuntu16.04', 'AmazonLinux2016.09', 'RedhatEnterpriseLinux7.2' or 'Suse12.7'. For lists of supported product values, see PatchFilter .
            (string) --
            Configuration (string) -- [REQUIRED]The value of the yum repo configuration. For example:
            cachedir=/var/cache/yum/$basesearch$releasever
            keepcache=0
            debualevel=2
            
            

    :type ClientToken: string
    :param ClientToken: User-provided idempotency token.
            This field is autopopulated if not provided.
            

    :rtype: dict
    :return: {
        'BaselineId': 'string'
    }
    
    
    """
    pass

def create_resource_data_sync(SyncName=None, S3Destination=None):
    """
    Creates a resource data sync configuration to a single bucket in Amazon S3. This is an asynchronous operation that returns immediately. After a successful initial sync is completed, the system continuously syncs data to the Amazon S3 bucket. To check the status of the sync, use the  ListResourceDataSync .
    By default, data is not encrypted in Amazon S3. We strongly recommend that you enable encryption in Amazon S3 to ensure secure data storage. We also recommend that you secure access to the Amazon S3 bucket by creating a restrictive bucket policy. To view an example of a restrictive Amazon S3 bucket policy for Resource Data Sync, see Configuring Resource Data Sync for Inventory .
    See also: AWS API Documentation
    
    
    :example: response = client.create_resource_data_sync(
        SyncName='string',
        S3Destination={
            'BucketName': 'string',
            'Prefix': 'string',
            'SyncFormat': 'JsonSerDe',
            'Region': 'string',
            'AWSKMSKeyARN': 'string'
        }
    )
    
    
    :type SyncName: string
    :param SyncName: [REQUIRED]
            A name for the configuration.
            

    :type S3Destination: dict
    :param S3Destination: [REQUIRED]
            Amazon S3 configuration details for the sync.
            BucketName (string) -- [REQUIRED]The name of the Amazon S3 bucket where the aggregated data is stored.
            Prefix (string) --An Amazon S3 prefix for the bucket.
            SyncFormat (string) -- [REQUIRED]A supported sync format. The following format is currently supported: JsonSerDe
            Region (string) -- [REQUIRED]The AWS Region with the Amazon S3 bucket targeted by the Resource Data Sync.
            AWSKMSKeyARN (string) --The ARN of an encryption key for a destination in Amazon S3. Must belong to the same region as the destination Amazon S3 bucket.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_activation(ActivationId=None):
    """
    Deletes an activation. You are not required to delete an activation. If you delete an activation, you can no longer use it to register additional managed instances. Deleting an activation does not de-register managed instances. You must manually de-register managed instances.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_activation(
        ActivationId='string'
    )
    
    
    :type ActivationId: string
    :param ActivationId: [REQUIRED]
            The ID of the activation that you want to delete.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_association(Name=None, InstanceId=None, AssociationId=None):
    """
    Disassociates the specified Systems Manager document from the specified instance.
    When you disassociate a document from an instance, it does not change the configuration of the instance. To change the configuration state of an instance after you disassociate a document, you must create a new document with the desired configuration and associate it with the instance.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_association(
        Name='string',
        InstanceId='string',
        AssociationId='string'
    )
    
    
    :type Name: string
    :param Name: The name of the Systems Manager document.

    :type InstanceId: string
    :param InstanceId: The ID of the instance.

    :type AssociationId: string
    :param AssociationId: The association ID that you want to delete.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_document(Name=None):
    """
    Deletes the Systems Manager document and all instance associations to the document.
    Before you delete the document, we recommend that you use  DeleteAssociation to disassociate all instances that are associated with the document.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_document(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the document.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_maintenance_window(WindowId=None):
    """
    Deletes a Maintenance Window.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_maintenance_window(
        WindowId='string'
    )
    
    
    :type WindowId: string
    :param WindowId: [REQUIRED]
            The ID of the Maintenance Window to delete.
            

    :rtype: dict
    :return: {
        'WindowId': 'string'
    }
    
    
    """
    pass

def delete_parameter(Name=None):
    """
    Delete a parameter from the system.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_parameter(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the parameter to delete.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_parameters(Names=None):
    """
    Delete a list of parameters. This API is used to delete parameters by using the Amazon EC2 console.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_parameters(
        Names=[
            'string',
        ]
    )
    
    
    :type Names: list
    :param Names: [REQUIRED]
            The names of the parameters to delete.
            (string) --
            

    :rtype: dict
    :return: {
        'DeletedParameters': [
            'string',
        ],
        'InvalidParameters': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def delete_patch_baseline(BaselineId=None):
    """
    Deletes a patch baseline.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_patch_baseline(
        BaselineId='string'
    )
    
    
    :type BaselineId: string
    :param BaselineId: [REQUIRED]
            The ID of the patch baseline to delete.
            

    :rtype: dict
    :return: {
        'BaselineId': 'string'
    }
    
    
    """
    pass

def delete_resource_data_sync(SyncName=None):
    """
    Deletes a Resource Data Sync configuration. After the configuration is deleted, changes to inventory data on managed instances are no longer synced with the target Amazon S3 bucket. Deleting a sync configuration does not delete data in the target Amazon S3 bucket.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_resource_data_sync(
        SyncName='string'
    )
    
    
    :type SyncName: string
    :param SyncName: [REQUIRED]
            The name of the configuration to delete.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def deregister_managed_instance(InstanceId=None):
    """
    Removes the server or virtual machine from the list of registered servers. You can reregister the instance again at any time. If you don't plan to use Run Command on the server, we suggest uninstalling the SSM Agent first.
    See also: AWS API Documentation
    
    
    :example: response = client.deregister_managed_instance(
        InstanceId='string'
    )
    
    
    :type InstanceId: string
    :param InstanceId: [REQUIRED]
            The ID assigned to the managed instance when you registered it using the activation process.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def deregister_patch_baseline_for_patch_group(BaselineId=None, PatchGroup=None):
    """
    Removes a patch group from a patch baseline.
    See also: AWS API Documentation
    
    
    :example: response = client.deregister_patch_baseline_for_patch_group(
        BaselineId='string',
        PatchGroup='string'
    )
    
    
    :type BaselineId: string
    :param BaselineId: [REQUIRED]
            The ID of the patch baseline to deregister the patch group from.
            

    :type PatchGroup: string
    :param PatchGroup: [REQUIRED]
            The name of the patch group that should be deregistered from the patch baseline.
            

    :rtype: dict
    :return: {
        'BaselineId': 'string',
        'PatchGroup': 'string'
    }
    
    
    """
    pass

def deregister_target_from_maintenance_window(WindowId=None, WindowTargetId=None, Safe=None):
    """
    Removes a target from a Maintenance Window.
    See also: AWS API Documentation
    
    
    :example: response = client.deregister_target_from_maintenance_window(
        WindowId='string',
        WindowTargetId='string',
        Safe=True|False
    )
    
    
    :type WindowId: string
    :param WindowId: [REQUIRED]
            The ID of the Maintenance Window the target should be removed from.
            

    :type WindowTargetId: string
    :param WindowTargetId: [REQUIRED]
            The ID of the target definition to remove.
            

    :type Safe: boolean
    :param Safe: The system checks if the target is being referenced by a task. If the target is being referenced, the system returns an error and does not deregister the target from the Maintenance Window.

    :rtype: dict
    :return: {
        'WindowId': 'string',
        'WindowTargetId': 'string'
    }
    
    
    """
    pass

def deregister_task_from_maintenance_window(WindowId=None, WindowTaskId=None):
    """
    Removes a task from a Maintenance Window.
    See also: AWS API Documentation
    
    
    :example: response = client.deregister_task_from_maintenance_window(
        WindowId='string',
        WindowTaskId='string'
    )
    
    
    :type WindowId: string
    :param WindowId: [REQUIRED]
            The ID of the Maintenance Window the task should be removed from.
            

    :type WindowTaskId: string
    :param WindowTaskId: [REQUIRED]
            The ID of the task to remove from the Maintenance Window.
            

    :rtype: dict
    :return: {
        'WindowId': 'string',
        'WindowTaskId': 'string'
    }
    
    
    """
    pass

def describe_activations(Filters=None, MaxResults=None, NextToken=None):
    """
    Details about the activation, including: the date and time the activation was created, the expiration date, the IAM role assigned to the instances in the activation, and the number of instances activated by this registration.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_activations(
        Filters=[
            {
                'FilterKey': 'ActivationIds'|'DefaultInstanceName'|'IamRole',
                'FilterValues': [
                    'string',
                ]
            },
        ],
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type Filters: list
    :param Filters: A filter to view information about your activations.
            (dict) --Filter for the DescribeActivation API.
            FilterKey (string) --The name of the filter.
            FilterValues (list) --The filter values.
            (string) --
            
            

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :type NextToken: string
    :param NextToken: A token to start the list. Use this token to get the next set of results.

    :rtype: dict
    :return: {
        'ActivationList': [
            {
                'ActivationId': 'string',
                'Description': 'string',
                'DefaultInstanceName': 'string',
                'IamRole': 'string',
                'RegistrationLimit': 123,
                'RegistrationsCount': 123,
                'ExpirationDate': datetime(2015, 1, 1),
                'Expired': True|False,
                'CreatedDate': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def describe_association(Name=None, InstanceId=None, AssociationId=None, AssociationVersion=None):
    """
    Describes the association for the specified target or instance. If you created the association by using the Targets parameter, then you must retrieve the association by using the association ID. If you created the association by specifying an instance ID and a Systems Manager document, then you retrieve the association by specifying the document name and the instance ID.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_association(
        Name='string',
        InstanceId='string',
        AssociationId='string',
        AssociationVersion='string'
    )
    
    
    :type Name: string
    :param Name: The name of the Systems Manager document.

    :type InstanceId: string
    :param InstanceId: The instance ID.

    :type AssociationId: string
    :param AssociationId: The association ID for which you want information.

    :type AssociationVersion: string
    :param AssociationVersion: Specify the association version to retrieve. To view the latest version, either specify $LATEST for this parameter, or omit this parameter. To view a list of all associations for an instance, use ListInstanceAssociations. To get a list of versions for a specific association, use ListAssociationVersions.

    :rtype: dict
    :return: {
        'AssociationDescription': {
            'Name': 'string',
            'InstanceId': 'string',
            'AssociationVersion': 'string',
            'Date': datetime(2015, 1, 1),
            'LastUpdateAssociationDate': datetime(2015, 1, 1),
            'Status': {
                'Date': datetime(2015, 1, 1),
                'Name': 'Pending'|'Success'|'Failed',
                'Message': 'string',
                'AdditionalInfo': 'string'
            },
            'Overview': {
                'Status': 'string',
                'DetailedStatus': 'string',
                'AssociationStatusAggregatedCount': {
                    'string': 123
                }
            },
            'DocumentVersion': 'string',
            'Parameters': {
                'string': [
                    'string',
                ]
            },
            'AssociationId': 'string',
            'Targets': [
                {
                    'Key': 'string',
                    'Values': [
                        'string',
                    ]
                },
            ],
            'ScheduleExpression': 'string',
            'OutputLocation': {
                'S3Location': {
                    'OutputS3Region': 'string',
                    'OutputS3BucketName': 'string',
                    'OutputS3KeyPrefix': 'string'
                }
            },
            'LastExecutionDate': datetime(2015, 1, 1),
            'LastSuccessfulExecutionDate': datetime(2015, 1, 1),
            'AssociationName': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (integer) --
    
    
    
    """
    pass

def describe_automation_executions(Filters=None, MaxResults=None, NextToken=None):
    """
    Provides details about all active and terminated Automation executions.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_automation_executions(
        Filters=[
            {
                'Key': 'DocumentNamePrefix'|'ExecutionStatus'|'ExecutionId'|'ParentExecutionId'|'CurrentAction'|'StartTimeBefore'|'StartTimeAfter',
                'Values': [
                    'string',
                ]
            },
        ],
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type Filters: list
    :param Filters: Filters used to limit the scope of executions that are requested.
            (dict) --A filter used to match specific automation executions. This is used to limit the scope of Automation execution information returned.
            Key (string) -- [REQUIRED]One or more keys to limit the results. Valid filter keys include the following: DocumentNamePrefix, ExecutionStatus, ExecutionId, ParentExecutionId, CurrentAction, StartTimeBefore, StartTimeAfter.
            Values (list) -- [REQUIRED]The values used to limit the execution information associated with the filter's key.
            (string) --
            
            

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :rtype: dict
    :return: {
        'AutomationExecutionMetadataList': [
            {
                'AutomationExecutionId': 'string',
                'DocumentName': 'string',
                'DocumentVersion': 'string',
                'AutomationExecutionStatus': 'Pending'|'InProgress'|'Waiting'|'Success'|'TimedOut'|'Cancelling'|'Cancelled'|'Failed',
                'ExecutionStartTime': datetime(2015, 1, 1),
                'ExecutionEndTime': datetime(2015, 1, 1),
                'ExecutedBy': 'string',
                'LogFile': 'string',
                'Outputs': {
                    'string': [
                        'string',
                    ]
                },
                'Mode': 'Auto'|'Interactive',
                'ParentAutomationExecutionId': 'string',
                'CurrentStepName': 'string',
                'CurrentAction': 'string',
                'FailureMessage': 'string',
                'TargetParameterName': 'string',
                'Targets': [
                    {
                        'Key': 'string',
                        'Values': [
                            'string',
                        ]
                    },
                ],
                'ResolvedTargets': {
                    'ParameterValues': [
                        'string',
                    ],
                    'Truncated': True|False
                },
                'MaxConcurrency': 'string',
                'MaxErrors': 'string',
                'Target': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (list) --
    (string) --
    
    
    
    
    
    """
    pass

def describe_automation_step_executions(AutomationExecutionId=None, Filters=None, NextToken=None, MaxResults=None, ReverseOrder=None):
    """
    Information about all active and terminated step executions in an Automation workflow.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_automation_step_executions(
        AutomationExecutionId='string',
        Filters=[
            {
                'Key': 'StartTimeBefore'|'StartTimeAfter'|'StepExecutionStatus'|'StepExecutionId'|'StepName'|'Action',
                'Values': [
                    'string',
                ]
            },
        ],
        NextToken='string',
        MaxResults=123,
        ReverseOrder=True|False
    )
    
    
    :type AutomationExecutionId: string
    :param AutomationExecutionId: [REQUIRED]
            The Automation execution ID for which you want step execution descriptions.
            

    :type Filters: list
    :param Filters: One or more filters to limit the number of step executions returned by the request.
            (dict) --A filter to limit the amount of step execution information returned by the call.
            Key (string) -- [REQUIRED]One or more keys to limit the results. Valid filter keys include the following: StepName, Action, StepExecutionId, StepExecutionStatus, StartTimeBefore, StartTimeAfter.
            Values (list) -- [REQUIRED]The values of the filter key.
            (string) --
            
            

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :type ReverseOrder: boolean
    :param ReverseOrder: A boolean that indicates whether to list step executions in reverse order by start time. The default value is false.

    :rtype: dict
    :return: {
        'StepExecutions': [
            {
                'StepName': 'string',
                'Action': 'string',
                'TimeoutSeconds': 123,
                'OnFailure': 'string',
                'MaxAttempts': 123,
                'ExecutionStartTime': datetime(2015, 1, 1),
                'ExecutionEndTime': datetime(2015, 1, 1),
                'StepStatus': 'Pending'|'InProgress'|'Waiting'|'Success'|'TimedOut'|'Cancelling'|'Cancelled'|'Failed',
                'ResponseCode': 'string',
                'Inputs': {
                    'string': 'string'
                },
                'Outputs': {
                    'string': [
                        'string',
                    ]
                },
                'Response': 'string',
                'FailureMessage': 'string',
                'FailureDetails': {
                    'FailureStage': 'string',
                    'FailureType': 'string',
                    'Details': {
                        'string': [
                            'string',
                        ]
                    }
                },
                'StepExecutionId': 'string',
                'OverriddenParameters': {
                    'string': [
                        'string',
                    ]
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def describe_available_patches(Filters=None, MaxResults=None, NextToken=None):
    """
    Lists all patches that could possibly be included in a patch baseline.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_available_patches(
        Filters=[
            {
                'Key': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type Filters: list
    :param Filters: Filters used to scope down the returned patches.
            (dict) --Defines a filter used in Patch Manager APIs.
            Key (string) --The key for the filter.
            Values (list) --The value for the filter.
            (string) --
            
            

    :type MaxResults: integer
    :param MaxResults: The maximum number of patches to return (per page).

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :rtype: dict
    :return: {
        'Patches': [
            {
                'Id': 'string',
                'ReleaseDate': datetime(2015, 1, 1),
                'Title': 'string',
                'Description': 'string',
                'ContentUrl': 'string',
                'Vendor': 'string',
                'ProductFamily': 'string',
                'Product': 'string',
                'Classification': 'string',
                'MsrcSeverity': 'string',
                'KbNumber': 'string',
                'MsrcNumber': 'string',
                'Language': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def describe_document(Name=None, DocumentVersion=None):
    """
    Describes the specified Systems Manager document.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_document(
        Name='string',
        DocumentVersion='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the Systems Manager document.
            

    :type DocumentVersion: string
    :param DocumentVersion: The document version for which you want information. Can be a specific version or the default version.

    :rtype: dict
    :return: {
        'Document': {
            'Sha1': 'string',
            'Hash': 'string',
            'HashType': 'Sha256'|'Sha1',
            'Name': 'string',
            'Owner': 'string',
            'CreatedDate': datetime(2015, 1, 1),
            'Status': 'Creating'|'Active'|'Updating'|'Deleting',
            'DocumentVersion': 'string',
            'Description': 'string',
            'Parameters': [
                {
                    'Name': 'string',
                    'Type': 'String'|'StringList',
                    'Description': 'string',
                    'DefaultValue': 'string'
                },
            ],
            'PlatformTypes': [
                'Windows'|'Linux',
            ],
            'DocumentType': 'Command'|'Policy'|'Automation',
            'SchemaVersion': 'string',
            'LatestVersion': 'string',
            'DefaultVersion': 'string',
            'DocumentFormat': 'YAML'|'JSON',
            'TargetType': 'string',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_document_permission(Name=None, PermissionType=None):
    """
    Describes the permissions for a Systems Manager document. If you created the document, you are the owner. If a document is shared, it can either be shared privately (by specifying a user's AWS account ID) or publicly (All ).
    See also: AWS API Documentation
    
    
    :example: response = client.describe_document_permission(
        Name='string',
        PermissionType='Share'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the document for which you are the owner.
            

    :type PermissionType: string
    :param PermissionType: [REQUIRED]
            The permission type for the document. The permission type can be Share .
            

    :rtype: dict
    :return: {
        'AccountIds': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_effective_instance_associations(InstanceId=None, MaxResults=None, NextToken=None):
    """
    All associations for the instance(s).
    See also: AWS API Documentation
    
    
    :example: response = client.describe_effective_instance_associations(
        InstanceId='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type InstanceId: string
    :param InstanceId: [REQUIRED]
            The instance ID for which you want to view all associations.
            

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :rtype: dict
    :return: {
        'Associations': [
            {
                'AssociationId': 'string',
                'InstanceId': 'string',
                'Content': 'string',
                'AssociationVersion': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def describe_effective_patches_for_patch_baseline(BaselineId=None, MaxResults=None, NextToken=None):
    """
    Retrieves the current effective patches (the patch and the approval state) for the specified patch baseline. Note that this API applies only to Windows patch baselines.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_effective_patches_for_patch_baseline(
        BaselineId='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type BaselineId: string
    :param BaselineId: [REQUIRED]
            The ID of the patch baseline to retrieve the effective patches for.
            

    :type MaxResults: integer
    :param MaxResults: The maximum number of patches to return (per page).

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :rtype: dict
    :return: {
        'EffectivePatches': [
            {
                'Patch': {
                    'Id': 'string',
                    'ReleaseDate': datetime(2015, 1, 1),
                    'Title': 'string',
                    'Description': 'string',
                    'ContentUrl': 'string',
                    'Vendor': 'string',
                    'ProductFamily': 'string',
                    'Product': 'string',
                    'Classification': 'string',
                    'MsrcSeverity': 'string',
                    'KbNumber': 'string',
                    'MsrcNumber': 'string',
                    'Language': 'string'
                },
                'PatchStatus': {
                    'DeploymentStatus': 'APPROVED'|'PENDING_APPROVAL'|'EXPLICIT_APPROVED'|'EXPLICIT_REJECTED',
                    'ComplianceLevel': 'CRITICAL'|'HIGH'|'MEDIUM'|'LOW'|'INFORMATIONAL'|'UNSPECIFIED',
                    'ApprovalDate': datetime(2015, 1, 1)
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def describe_instance_associations_status(InstanceId=None, MaxResults=None, NextToken=None):
    """
    The status of the associations for the instance(s).
    See also: AWS API Documentation
    
    
    :example: response = client.describe_instance_associations_status(
        InstanceId='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type InstanceId: string
    :param InstanceId: [REQUIRED]
            The instance IDs for which you want association status information.
            

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :rtype: dict
    :return: {
        'InstanceAssociationStatusInfos': [
            {
                'AssociationId': 'string',
                'Name': 'string',
                'DocumentVersion': 'string',
                'AssociationVersion': 'string',
                'InstanceId': 'string',
                'ExecutionDate': datetime(2015, 1, 1),
                'Status': 'string',
                'DetailedStatus': 'string',
                'ExecutionSummary': 'string',
                'ErrorCode': 'string',
                'OutputUrl': {
                    'S3OutputUrl': {
                        'OutputUrl': 'string'
                    }
                },
                'AssociationName': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def describe_instance_information(InstanceInformationFilterList=None, Filters=None, MaxResults=None, NextToken=None):
    """
    Describes one or more of your instances. You can use this to get information about instances like the operating system platform, the SSM Agent version (Linux), status etc. If you specify one or more instance IDs, it returns information for those instances. If you do not specify instance IDs, it returns information for all your instances. If you specify an instance ID that is not valid or an instance that you do not own, you receive an error.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_instance_information(
        InstanceInformationFilterList=[
            {
                'key': 'InstanceIds'|'AgentVersion'|'PingStatus'|'PlatformTypes'|'ActivationIds'|'IamRole'|'ResourceType'|'AssociationStatus',
                'valueSet': [
                    'string',
                ]
            },
        ],
        Filters=[
            {
                'Key': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type InstanceInformationFilterList: list
    :param InstanceInformationFilterList: One or more filters. Use a filter to return a more specific list of instances.
            (dict) --Describes a filter for a specific list of instances.
            key (string) -- [REQUIRED]The name of the filter.
            valueSet (list) -- [REQUIRED]The filter values.
            (string) --
            
            

    :type Filters: list
    :param Filters: One or more filters. Use a filter to return a more specific list of instances.
            (dict) --The filters to describe or get information about your managed instances.
            Key (string) -- [REQUIRED]The filter key name to describe your instances. For example:
            'InstanceIds'|'AgentVersion'|'PingStatus'|'PlatformTypes'|'ActivationIds'|'IamRole'|'ResourceType'|'AssociationStatus'|'Tag Key'
            Values (list) -- [REQUIRED]The filter values.
            (string) --
            
            

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :rtype: dict
    :return: {
        'InstanceInformationList': [
            {
                'InstanceId': 'string',
                'PingStatus': 'Online'|'ConnectionLost'|'Inactive',
                'LastPingDateTime': datetime(2015, 1, 1),
                'AgentVersion': 'string',
                'IsLatestVersion': True|False,
                'PlatformType': 'Windows'|'Linux',
                'PlatformName': 'string',
                'PlatformVersion': 'string',
                'ActivationId': 'string',
                'IamRole': 'string',
                'RegistrationDate': datetime(2015, 1, 1),
                'ResourceType': 'ManagedInstance'|'Document'|'EC2Instance',
                'Name': 'string',
                'IPAddress': 'string',
                'ComputerName': 'string',
                'AssociationStatus': 'string',
                'LastAssociationExecutionDate': datetime(2015, 1, 1),
                'LastSuccessfulAssociationExecutionDate': datetime(2015, 1, 1),
                'AssociationOverview': {
                    'DetailedStatus': 'string',
                    'InstanceAssociationStatusAggregatedCount': {
                        'string': 123
                    }
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (integer) --
    
    
    
    """
    pass

def describe_instance_patch_states(InstanceIds=None, NextToken=None, MaxResults=None):
    """
    Retrieves the high-level patch state of one or more instances.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_instance_patch_states(
        InstanceIds=[
            'string',
        ],
        NextToken='string',
        MaxResults=123
    )
    
    
    :type InstanceIds: list
    :param InstanceIds: [REQUIRED]
            The ID of the instance whose patch state information should be retrieved.
            (string) --
            

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :type MaxResults: integer
    :param MaxResults: The maximum number of instances to return (per page).

    :rtype: dict
    :return: {
        'InstancePatchStates': [
            {
                'InstanceId': 'string',
                'PatchGroup': 'string',
                'BaselineId': 'string',
                'SnapshotId': 'string',
                'OwnerInformation': 'string',
                'InstalledCount': 123,
                'InstalledOtherCount': 123,
                'MissingCount': 123,
                'FailedCount': 123,
                'NotApplicableCount': 123,
                'OperationStartTime': datetime(2015, 1, 1),
                'OperationEndTime': datetime(2015, 1, 1),
                'Operation': 'Scan'|'Install'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def describe_instance_patch_states_for_patch_group(PatchGroup=None, Filters=None, NextToken=None, MaxResults=None):
    """
    Retrieves the high-level patch state for the instances in the specified patch group.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_instance_patch_states_for_patch_group(
        PatchGroup='string',
        Filters=[
            {
                'Key': 'string',
                'Values': [
                    'string',
                ],
                'Type': 'Equal'|'NotEqual'|'LessThan'|'GreaterThan'
            },
        ],
        NextToken='string',
        MaxResults=123
    )
    
    
    :type PatchGroup: string
    :param PatchGroup: [REQUIRED]
            The name of the patch group for which the patch state information should be retrieved.
            

    :type Filters: list
    :param Filters: Each entry in the array is a structure containing:
            Key (string between 1 and 200 characters)
            Values (array containing a single string)
            Type (string 'Equal', 'NotEqual', 'LessThan', 'GreaterThan')
            (dict) --Defines a filter used in DescribeInstancePatchStatesForPatchGroup used to scope down the information returned by the API.
            Key (string) -- [REQUIRED]The key for the filter. Supported values are FailedCount, InstalledCount, InstalledOtherCount, MissingCount and NotApplicableCount.
            Values (list) -- [REQUIRED]The value for the filter, must be an integer greater than or equal to 0.
            (string) --
            Type (string) -- [REQUIRED]The type of comparison that should be performed for the value: Equal, NotEqual, LessThan or GreaterThan.
            
            

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :type MaxResults: integer
    :param MaxResults: The maximum number of patches to return (per page).

    :rtype: dict
    :return: {
        'InstancePatchStates': [
            {
                'InstanceId': 'string',
                'PatchGroup': 'string',
                'BaselineId': 'string',
                'SnapshotId': 'string',
                'OwnerInformation': 'string',
                'InstalledCount': 123,
                'InstalledOtherCount': 123,
                'MissingCount': 123,
                'FailedCount': 123,
                'NotApplicableCount': 123,
                'OperationStartTime': datetime(2015, 1, 1),
                'OperationEndTime': datetime(2015, 1, 1),
                'Operation': 'Scan'|'Install'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def describe_instance_patches(InstanceId=None, Filters=None, NextToken=None, MaxResults=None):
    """
    Retrieves information about the patches on the specified instance and their state relative to the patch baseline being used for the instance.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_instance_patches(
        InstanceId='string',
        Filters=[
            {
                'Key': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        NextToken='string',
        MaxResults=123
    )
    
    
    :type InstanceId: string
    :param InstanceId: [REQUIRED]
            The ID of the instance whose patch state information should be retrieved.
            

    :type Filters: list
    :param Filters: Each entry in the array is a structure containing:
            Key (string, between 1 and 128 characters)
            Values (array of strings, each string between 1 and 256 characters)
            (dict) --Defines a filter used in Patch Manager APIs.
            Key (string) --The key for the filter.
            Values (list) --The value for the filter.
            (string) --
            
            

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :type MaxResults: integer
    :param MaxResults: The maximum number of patches to return (per page).

    :rtype: dict
    :return: {
        'Patches': [
            {
                'Title': 'string',
                'KBId': 'string',
                'Classification': 'string',
                'Severity': 'string',
                'State': 'INSTALLED'|'INSTALLED_OTHER'|'MISSING'|'NOT_APPLICABLE'|'FAILED',
                'InstalledTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def describe_maintenance_window_execution_task_invocations(WindowExecutionId=None, TaskId=None, Filters=None, MaxResults=None, NextToken=None):
    """
    Retrieves the individual task executions (one per target) for a particular task executed as part of a Maintenance Window execution.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_maintenance_window_execution_task_invocations(
        WindowExecutionId='string',
        TaskId='string',
        Filters=[
            {
                'Key': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type WindowExecutionId: string
    :param WindowExecutionId: [REQUIRED]
            The ID of the Maintenance Window execution the task is part of.
            

    :type TaskId: string
    :param TaskId: [REQUIRED]
            The ID of the specific task in the Maintenance Window task that should be retrieved.
            

    :type Filters: list
    :param Filters: Optional filters used to scope down the returned task invocations. The supported filter key is STATUS with the corresponding values PENDING, IN_PROGRESS, SUCCESS, FAILED, TIMED_OUT, CANCELLING, and CANCELLED.
            (dict) --Filter used in the request.
            Key (string) --The name of the filter.
            Values (list) --The filter values.
            (string) --
            
            

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :rtype: dict
    :return: {
        'WindowExecutionTaskInvocationIdentities': [
            {
                'WindowExecutionId': 'string',
                'TaskExecutionId': 'string',
                'InvocationId': 'string',
                'ExecutionId': 'string',
                'TaskType': 'RUN_COMMAND'|'AUTOMATION'|'STEP_FUNCTIONS'|'LAMBDA',
                'Parameters': 'string',
                'Status': 'PENDING'|'IN_PROGRESS'|'SUCCESS'|'FAILED'|'TIMED_OUT'|'CANCELLING'|'CANCELLED'|'SKIPPED_OVERLAPPING',
                'StatusDetails': 'string',
                'StartTime': datetime(2015, 1, 1),
                'EndTime': datetime(2015, 1, 1),
                'OwnerInformation': 'string',
                'WindowTargetId': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def describe_maintenance_window_execution_tasks(WindowExecutionId=None, Filters=None, MaxResults=None, NextToken=None):
    """
    For a given Maintenance Window execution, lists the tasks that were executed.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_maintenance_window_execution_tasks(
        WindowExecutionId='string',
        Filters=[
            {
                'Key': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type WindowExecutionId: string
    :param WindowExecutionId: [REQUIRED]
            The ID of the Maintenance Window execution whose task executions should be retrieved.
            

    :type Filters: list
    :param Filters: Optional filters used to scope down the returned tasks. The supported filter key is STATUS with the corresponding values PENDING, IN_PROGRESS, SUCCESS, FAILED, TIMED_OUT, CANCELLING, and CANCELLED.
            (dict) --Filter used in the request.
            Key (string) --The name of the filter.
            Values (list) --The filter values.
            (string) --
            
            

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :rtype: dict
    :return: {
        'WindowExecutionTaskIdentities': [
            {
                'WindowExecutionId': 'string',
                'TaskExecutionId': 'string',
                'Status': 'PENDING'|'IN_PROGRESS'|'SUCCESS'|'FAILED'|'TIMED_OUT'|'CANCELLING'|'CANCELLED'|'SKIPPED_OVERLAPPING',
                'StatusDetails': 'string',
                'StartTime': datetime(2015, 1, 1),
                'EndTime': datetime(2015, 1, 1),
                'TaskArn': 'string',
                'TaskType': 'RUN_COMMAND'|'AUTOMATION'|'STEP_FUNCTIONS'|'LAMBDA'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def describe_maintenance_window_executions(WindowId=None, Filters=None, MaxResults=None, NextToken=None):
    """
    Lists the executions of a Maintenance Window. This includes information about when the Maintenance Window was scheduled to be active, and information about tasks registered and run with the Maintenance Window.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_maintenance_window_executions(
        WindowId='string',
        Filters=[
            {
                'Key': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type WindowId: string
    :param WindowId: [REQUIRED]
            The ID of the Maintenance Window whose executions should be retrieved.
            

    :type Filters: list
    :param Filters: Each entry in the array is a structure containing:
            Key (string, between 1 and 128 characters)
            Values (array of strings, each string is between 1 and 256 characters)
            The supported Keys are ExecutedBefore and ExecutedAfter with the value being a date/time string such as 2016-11-04T05:00:00Z.
            (dict) --Filter used in the request.
            Key (string) --The name of the filter.
            Values (list) --The filter values.
            (string) --
            
            

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :rtype: dict
    :return: {
        'WindowExecutions': [
            {
                'WindowId': 'string',
                'WindowExecutionId': 'string',
                'Status': 'PENDING'|'IN_PROGRESS'|'SUCCESS'|'FAILED'|'TIMED_OUT'|'CANCELLING'|'CANCELLED'|'SKIPPED_OVERLAPPING',
                'StatusDetails': 'string',
                'StartTime': datetime(2015, 1, 1),
                'EndTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def describe_maintenance_window_targets(WindowId=None, Filters=None, MaxResults=None, NextToken=None):
    """
    Lists the targets registered with the Maintenance Window.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_maintenance_window_targets(
        WindowId='string',
        Filters=[
            {
                'Key': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type WindowId: string
    :param WindowId: [REQUIRED]
            The ID of the Maintenance Window whose targets should be retrieved.
            

    :type Filters: list
    :param Filters: Optional filters that can be used to narrow down the scope of the returned window targets. The supported filter keys are Type, WindowTargetId and OwnerInformation.
            (dict) --Filter used in the request.
            Key (string) --The name of the filter.
            Values (list) --The filter values.
            (string) --
            
            

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :rtype: dict
    :return: {
        'Targets': [
            {
                'WindowId': 'string',
                'WindowTargetId': 'string',
                'ResourceType': 'INSTANCE',
                'Targets': [
                    {
                        'Key': 'string',
                        'Values': [
                            'string',
                        ]
                    },
                ],
                'OwnerInformation': 'string',
                'Name': 'string',
                'Description': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_maintenance_window_tasks(WindowId=None, Filters=None, MaxResults=None, NextToken=None):
    """
    Lists the tasks in a Maintenance Window.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_maintenance_window_tasks(
        WindowId='string',
        Filters=[
            {
                'Key': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type WindowId: string
    :param WindowId: [REQUIRED]
            The ID of the Maintenance Window whose tasks should be retrieved.
            

    :type Filters: list
    :param Filters: Optional filters used to narrow down the scope of the returned tasks. The supported filter keys are WindowTaskId, TaskArn, Priority, and TaskType.
            (dict) --Filter used in the request.
            Key (string) --The name of the filter.
            Values (list) --The filter values.
            (string) --
            
            

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :rtype: dict
    :return: {
        'Tasks': [
            {
                'WindowId': 'string',
                'WindowTaskId': 'string',
                'TaskArn': 'string',
                'Type': 'RUN_COMMAND'|'AUTOMATION'|'STEP_FUNCTIONS'|'LAMBDA',
                'Targets': [
                    {
                        'Key': 'string',
                        'Values': [
                            'string',
                        ]
                    },
                ],
                'TaskParameters': {
                    'string': {
                        'Values': [
                            'string',
                        ]
                    }
                },
                'Priority': 123,
                'LoggingInfo': {
                    'S3BucketName': 'string',
                    'S3KeyPrefix': 'string',
                    'S3Region': 'string'
                },
                'ServiceRoleArn': 'string',
                'MaxConcurrency': 'string',
                'MaxErrors': 'string',
                'Name': 'string',
                'Description': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_maintenance_windows(Filters=None, MaxResults=None, NextToken=None):
    """
    Retrieves the Maintenance Windows in an AWS account.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_maintenance_windows(
        Filters=[
            {
                'Key': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type Filters: list
    :param Filters: Optional filters used to narrow down the scope of the returned Maintenance Windows. Supported filter keys are Name and Enabled.
            (dict) --Filter used in the request.
            Key (string) --The name of the filter.
            Values (list) --The filter values.
            (string) --
            
            

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :rtype: dict
    :return: {
        'WindowIdentities': [
            {
                'WindowId': 'string',
                'Name': 'string',
                'Description': 'string',
                'Enabled': True|False,
                'Duration': 123,
                'Cutoff': 123
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def describe_parameters(Filters=None, ParameterFilters=None, MaxResults=None, NextToken=None):
    """
    Get information about a parameter.
    Request results are returned on a best-effort basis. If you specify MaxResults in the request, the response includes information up to the limit specified. The number of items returned, however, can be between zero and the value of MaxResults . If the service reaches an internal limit while processing the results, it stops the operation and returns the matching values up to that point and a NextToken . You can specify the NextToken in a subsequent call to get the next set of results.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_parameters(
        Filters=[
            {
                'Key': 'Name'|'Type'|'KeyId',
                'Values': [
                    'string',
                ]
            },
        ],
        ParameterFilters=[
            {
                'Key': 'string',
                'Option': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type Filters: list
    :param Filters: One or more filters. Use a filter to return a more specific list of results.
            (dict) --This data type is deprecated. Instead, use ParameterStringFilter .
            Key (string) -- [REQUIRED]The name of the filter.
            Values (list) -- [REQUIRED]The filter values.
            (string) --
            
            

    :type ParameterFilters: list
    :param ParameterFilters: Filters to limit the request results.
            (dict) --One or more filters. Use a filter to return a more specific list of results.
            Key (string) -- [REQUIRED]The name of the filter.
            Option (string) --Valid options are Equals and BeginsWith. For Path filter, valid options are Recursive and OneLevel.
            Values (list) --The value you want to search for.
            (string) --
            
            

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :rtype: dict
    :return: {
        'Parameters': [
            {
                'Name': 'string',
                'Type': 'String'|'StringList'|'SecureString',
                'KeyId': 'string',
                'LastModifiedDate': datetime(2015, 1, 1),
                'LastModifiedUser': 'string',
                'Description': 'string',
                'AllowedPattern': 'string',
                'Version': 123
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def describe_patch_baselines(Filters=None, MaxResults=None, NextToken=None):
    """
    Lists the patch baselines in your AWS account.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_patch_baselines(
        Filters=[
            {
                'Key': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type Filters: list
    :param Filters: Each element in the array is a structure containing:
            Key: (string, 'NAME_PREFIX' or 'OWNER')
            Value: (array of strings, exactly 1 entry, between 1 and 255 characters)
            (dict) --Defines a filter used in Patch Manager APIs.
            Key (string) --The key for the filter.
            Values (list) --The value for the filter.
            (string) --
            
            

    :type MaxResults: integer
    :param MaxResults: The maximum number of patch baselines to return (per page).

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :rtype: dict
    :return: {
        'BaselineIdentities': [
            {
                'BaselineId': 'string',
                'BaselineName': 'string',
                'OperatingSystem': 'WINDOWS'|'AMAZON_LINUX'|'UBUNTU'|'REDHAT_ENTERPRISE_LINUX'|'SUSE'|'CENTOS',
                'BaselineDescription': 'string',
                'DefaultBaseline': True|False
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def describe_patch_group_state(PatchGroup=None):
    """
    Returns high-level aggregated patch compliance state for a patch group.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_patch_group_state(
        PatchGroup='string'
    )
    
    
    :type PatchGroup: string
    :param PatchGroup: [REQUIRED]
            The name of the patch group whose patch snapshot should be retrieved.
            

    :rtype: dict
    :return: {
        'Instances': 123,
        'InstancesWithInstalledPatches': 123,
        'InstancesWithInstalledOtherPatches': 123,
        'InstancesWithMissingPatches': 123,
        'InstancesWithFailedPatches': 123,
        'InstancesWithNotApplicablePatches': 123
    }
    
    
    """
    pass

def describe_patch_groups(MaxResults=None, Filters=None, NextToken=None):
    """
    Lists all patch groups that have been registered with patch baselines.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_patch_groups(
        MaxResults=123,
        Filters=[
            {
                'Key': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        NextToken='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: The maximum number of patch groups to return (per page).

    :type Filters: list
    :param Filters: One or more filters. Use a filter to return a more specific list of results.
            (dict) --Defines a filter used in Patch Manager APIs.
            Key (string) --The key for the filter.
            Values (list) --The value for the filter.
            (string) --
            
            

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :rtype: dict
    :return: {
        'Mappings': [
            {
                'PatchGroup': 'string',
                'BaselineIdentity': {
                    'BaselineId': 'string',
                    'BaselineName': 'string',
                    'OperatingSystem': 'WINDOWS'|'AMAZON_LINUX'|'UBUNTU'|'REDHAT_ENTERPRISE_LINUX'|'SUSE'|'CENTOS',
                    'BaselineDescription': 'string',
                    'DefaultBaseline': True|False
                }
            },
        ],
        'NextToken': 'string'
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

def get_automation_execution(AutomationExecutionId=None):
    """
    Get detailed information about a particular Automation execution.
    See also: AWS API Documentation
    
    
    :example: response = client.get_automation_execution(
        AutomationExecutionId='string'
    )
    
    
    :type AutomationExecutionId: string
    :param AutomationExecutionId: [REQUIRED]
            The unique identifier for an existing automation execution to examine. The execution ID is returned by StartAutomationExecution when the execution of an Automation document is initiated.
            

    :rtype: dict
    :return: {
        'AutomationExecution': {
            'AutomationExecutionId': 'string',
            'DocumentName': 'string',
            'DocumentVersion': 'string',
            'ExecutionStartTime': datetime(2015, 1, 1),
            'ExecutionEndTime': datetime(2015, 1, 1),
            'AutomationExecutionStatus': 'Pending'|'InProgress'|'Waiting'|'Success'|'TimedOut'|'Cancelling'|'Cancelled'|'Failed',
            'StepExecutions': [
                {
                    'StepName': 'string',
                    'Action': 'string',
                    'TimeoutSeconds': 123,
                    'OnFailure': 'string',
                    'MaxAttempts': 123,
                    'ExecutionStartTime': datetime(2015, 1, 1),
                    'ExecutionEndTime': datetime(2015, 1, 1),
                    'StepStatus': 'Pending'|'InProgress'|'Waiting'|'Success'|'TimedOut'|'Cancelling'|'Cancelled'|'Failed',
                    'ResponseCode': 'string',
                    'Inputs': {
                        'string': 'string'
                    },
                    'Outputs': {
                        'string': [
                            'string',
                        ]
                    },
                    'Response': 'string',
                    'FailureMessage': 'string',
                    'FailureDetails': {
                        'FailureStage': 'string',
                        'FailureType': 'string',
                        'Details': {
                            'string': [
                                'string',
                            ]
                        }
                    },
                    'StepExecutionId': 'string',
                    'OverriddenParameters': {
                        'string': [
                            'string',
                        ]
                    }
                },
            ],
            'StepExecutionsTruncated': True|False,
            'Parameters': {
                'string': [
                    'string',
                ]
            },
            'Outputs': {
                'string': [
                    'string',
                ]
            },
            'FailureMessage': 'string',
            'Mode': 'Auto'|'Interactive',
            'ParentAutomationExecutionId': 'string',
            'ExecutedBy': 'string',
            'CurrentStepName': 'string',
            'CurrentAction': 'string',
            'TargetParameterName': 'string',
            'Targets': [
                {
                    'Key': 'string',
                    'Values': [
                        'string',
                    ]
                },
            ],
            'ResolvedTargets': {
                'ParameterValues': [
                    'string',
                ],
                'Truncated': True|False
            },
            'MaxConcurrency': 'string',
            'MaxErrors': 'string',
            'Target': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (list) --
    (string) --
    
    
    
    
    
    """
    pass

def get_command_invocation(CommandId=None, InstanceId=None, PluginName=None):
    """
    Returns detailed information about command execution for an invocation or plugin.
    See also: AWS API Documentation
    
    
    :example: response = client.get_command_invocation(
        CommandId='string',
        InstanceId='string',
        PluginName='string'
    )
    
    
    :type CommandId: string
    :param CommandId: [REQUIRED]
            (Required) The parent command ID of the invocation plugin.
            

    :type InstanceId: string
    :param InstanceId: [REQUIRED]
            (Required) The ID of the managed instance targeted by the command. A managed instance can be an Amazon EC2 instance or an instance in your hybrid environment that is configured for Systems Manager.
            

    :type PluginName: string
    :param PluginName: (Optional) The name of the plugin for which you want detailed results. If the document contains only one plugin, the name can be omitted and the details will be returned.

    :rtype: dict
    :return: {
        'CommandId': 'string',
        'InstanceId': 'string',
        'Comment': 'string',
        'DocumentName': 'string',
        'PluginName': 'string',
        'ResponseCode': 123,
        'ExecutionStartDateTime': 'string',
        'ExecutionElapsedTime': 'string',
        'ExecutionEndDateTime': 'string',
        'Status': 'Pending'|'InProgress'|'Delayed'|'Success'|'Cancelled'|'TimedOut'|'Failed'|'Cancelling',
        'StatusDetails': 'string',
        'StandardOutputContent': 'string',
        'StandardOutputUrl': 'string',
        'StandardErrorContent': 'string',
        'StandardErrorUrl': 'string'
    }
    
    
    :returns: 
    Pending: The command has not been sent to the instance.
    In Progress: The command has been sent to the instance but has not reached a terminal state.
    Delayed: The system attempted to send the command to the target, but the target was not available. The instance might not be available because of network issues, the instance was stopped, etc. The system will try to deliver the command again.
    Success: The command or plugin was executed successfully. This is a terminal state.
    Delivery Timed Out: The command was not delivered to the instance before the delivery timeout expired. Delivery timeouts do not count against the parent command's MaxErrors limit, but they do contribute to whether the parent command status is Success or Incomplete. This is a terminal state.
    Execution Timed Out: The command started to execute on the instance, but the execution was not complete before the timeout expired. Execution timeouts count against the MaxErrors limit of the parent command. This is a terminal state.
    Failed: The command wasn't executed successfully on the instance. For a plugin, this indicates that the result code was not zero. For a command invocation, this indicates that the result code for one or more plugins was not zero. Invocation failures count against the MaxErrors limit of the parent command. This is a terminal state.
    Canceled: The command was terminated before it was completed. This is a terminal state.
    Undeliverable: The command can't be delivered to the instance. The instance might not exist or might not be responding. Undeliverable invocations don't count against the parent command's MaxErrors limit and don't contribute to whether the parent command status is Success or Incomplete. This is a terminal state.
    Terminated: The parent command exceeded its MaxErrors limit and subsequent command invocations were canceled by the system. This is a terminal state.
    
    """
    pass

def get_default_patch_baseline(OperatingSystem=None):
    """
    Retrieves the default patch baseline. Note that Systems Manager supports creating multiple default patch baselines. For example, you can create a default patch baseline for each operating system.
    See also: AWS API Documentation
    
    
    :example: response = client.get_default_patch_baseline(
        OperatingSystem='WINDOWS'|'AMAZON_LINUX'|'UBUNTU'|'REDHAT_ENTERPRISE_LINUX'|'SUSE'|'CENTOS'
    )
    
    
    :type OperatingSystem: string
    :param OperatingSystem: Returns the default patch baseline for the specified operating system.

    :rtype: dict
    :return: {
        'BaselineId': 'string',
        'OperatingSystem': 'WINDOWS'|'AMAZON_LINUX'|'UBUNTU'|'REDHAT_ENTERPRISE_LINUX'|'SUSE'|'CENTOS'
    }
    
    
    """
    pass

def get_deployable_patch_snapshot_for_instance(InstanceId=None, SnapshotId=None):
    """
    Retrieves the current snapshot for the patch baseline the instance uses. This API is primarily used by the AWS-RunPatchBaseline Systems Manager document.
    See also: AWS API Documentation
    
    
    :example: response = client.get_deployable_patch_snapshot_for_instance(
        InstanceId='string',
        SnapshotId='string'
    )
    
    
    :type InstanceId: string
    :param InstanceId: [REQUIRED]
            The ID of the instance for which the appropriate patch snapshot should be retrieved.
            

    :type SnapshotId: string
    :param SnapshotId: [REQUIRED]
            The user-defined snapshot ID.
            

    :rtype: dict
    :return: {
        'InstanceId': 'string',
        'SnapshotId': 'string',
        'SnapshotDownloadUrl': 'string',
        'Product': 'string'
    }
    
    
    """
    pass

def get_document(Name=None, DocumentVersion=None, DocumentFormat=None):
    """
    Gets the contents of the specified Systems Manager document.
    See also: AWS API Documentation
    
    
    :example: response = client.get_document(
        Name='string',
        DocumentVersion='string',
        DocumentFormat='YAML'|'JSON'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the Systems Manager document.
            

    :type DocumentVersion: string
    :param DocumentVersion: The document version for which you want information.

    :type DocumentFormat: string
    :param DocumentFormat: Returns the document in the specified format. The document format can be either JSON or YAML. JSON is the default format.

    :rtype: dict
    :return: {
        'Name': 'string',
        'DocumentVersion': 'string',
        'Content': 'string',
        'DocumentType': 'Command'|'Policy'|'Automation',
        'DocumentFormat': 'YAML'|'JSON'
    }
    
    
    """
    pass

def get_inventory(Filters=None, Aggregators=None, ResultAttributes=None, NextToken=None, MaxResults=None):
    """
    Query inventory information.
    See also: AWS API Documentation
    
    
    :example: response = client.get_inventory(
        Filters=[
            {
                'Key': 'string',
                'Values': [
                    'string',
                ],
                'Type': 'Equal'|'NotEqual'|'BeginWith'|'LessThan'|'GreaterThan'
            },
        ],
        Aggregators=[
            {
                'Expression': 'string',
                'Aggregators': {'... recursive ...'}
            },
        ],
        ResultAttributes=[
            {
                'TypeName': 'string'
            },
        ],
        NextToken='string',
        MaxResults=123
    )
    
    
    :type Filters: list
    :param Filters: One or more filters. Use a filter to return a more specific list of results.
            (dict) --One or more filters. Use a filter to return a more specific list of results.
            Key (string) -- [REQUIRED]The name of the filter key.
            Values (list) -- [REQUIRED]Inventory filter values. Example: inventory filter where instance IDs are specified as values Key=AWS:InstanceInformation.InstanceId,Values= i-a12b3c4d5e6g, i-1a2b3c4d5e6,Type=Equal
            (string) --
            Type (string) --The type of filter. Valid values include the following: 'Equal'|'NotEqual'|'BeginWith'|'LessThan'|'GreaterThan'
            
            

    :type Aggregators: list
    :param Aggregators: Returns counts of inventory types based on one or more expressions. For example, if you aggregate by using an expression that uses the AWS:InstanceInformation.PlatformType type, you can see a count of how many Windows and Linux instances exist in your inventoried fleet.
            (dict) --Specifies the inventory type and attribute for the aggregation execution.
            Expression (string) --The inventory type and attribute name for aggregation.
            Aggregators (list) --Nested aggregators to further refine aggregation for an inventory type.
            
            

    :type ResultAttributes: list
    :param ResultAttributes: The list of inventory item types to return.
            (dict) --The inventory item result attribute.
            TypeName (string) -- [REQUIRED]Name of the inventory item type. Valid value: AWS:InstanceInformation. Default Value: AWS:InstanceInformation.
            
            

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :rtype: dict
    :return: {
        'Entities': [
            {
                'Id': 'string',
                'Data': {
                    'string': {
                        'TypeName': 'string',
                        'SchemaVersion': 'string',
                        'CaptureTime': 'string',
                        'ContentHash': 'string',
                        'Content': [
                            {
                                'string': 'string'
                            },
                        ]
                    }
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (dict) --
    (string) --
    (string) --
    
    
    
    
    
    """
    pass

def get_inventory_schema(TypeName=None, NextToken=None, MaxResults=None, Aggregator=None, SubType=None):
    """
    Return a list of inventory type names for the account, or return a list of attribute names for a specific Inventory item type.
    See also: AWS API Documentation
    
    
    :example: response = client.get_inventory_schema(
        TypeName='string',
        NextToken='string',
        MaxResults=123,
        Aggregator=True|False,
        SubType=True|False
    )
    
    
    :type TypeName: string
    :param TypeName: The type of inventory item to return.

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :type Aggregator: boolean
    :param Aggregator: Returns inventory schemas that support aggregation. For example, this call returns the AWS:InstanceInformation type, because it supports aggregation based on the PlatformName , PlatformType , and PlatformVersion attributes.

    :type SubType: boolean
    :param SubType: Returns the sub-type schema for a specified inventory type.

    :rtype: dict
    :return: {
        'Schemas': [
            {
                'TypeName': 'string',
                'Version': 'string',
                'Attributes': [
                    {
                        'Name': 'string',
                        'DataType': 'string'|'number'
                    },
                ],
                'DisplayName': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def get_maintenance_window(WindowId=None):
    """
    Retrieves a Maintenance Window.
    See also: AWS API Documentation
    
    
    :example: response = client.get_maintenance_window(
        WindowId='string'
    )
    
    
    :type WindowId: string
    :param WindowId: [REQUIRED]
            The ID of the desired Maintenance Window.
            

    :rtype: dict
    :return: {
        'WindowId': 'string',
        'Name': 'string',
        'Description': 'string',
        'Schedule': 'string',
        'Duration': 123,
        'Cutoff': 123,
        'AllowUnassociatedTargets': True|False,
        'Enabled': True|False,
        'CreatedDate': datetime(2015, 1, 1),
        'ModifiedDate': datetime(2015, 1, 1)
    }
    
    
    """
    pass

def get_maintenance_window_execution(WindowExecutionId=None):
    """
    Retrieves details about a specific task executed as part of a Maintenance Window execution.
    See also: AWS API Documentation
    
    
    :example: response = client.get_maintenance_window_execution(
        WindowExecutionId='string'
    )
    
    
    :type WindowExecutionId: string
    :param WindowExecutionId: [REQUIRED]
            The ID of the Maintenance Window execution that includes the task.
            

    :rtype: dict
    :return: {
        'WindowExecutionId': 'string',
        'TaskIds': [
            'string',
        ],
        'Status': 'PENDING'|'IN_PROGRESS'|'SUCCESS'|'FAILED'|'TIMED_OUT'|'CANCELLING'|'CANCELLED'|'SKIPPED_OVERLAPPING',
        'StatusDetails': 'string',
        'StartTime': datetime(2015, 1, 1),
        'EndTime': datetime(2015, 1, 1)
    }
    
    
    """
    pass

def get_maintenance_window_execution_task(WindowExecutionId=None, TaskId=None):
    """
    Retrieves the details about a specific task executed as part of a Maintenance Window execution.
    See also: AWS API Documentation
    
    
    :example: response = client.get_maintenance_window_execution_task(
        WindowExecutionId='string',
        TaskId='string'
    )
    
    
    :type WindowExecutionId: string
    :param WindowExecutionId: [REQUIRED]
            The ID of the Maintenance Window execution that includes the task.
            

    :type TaskId: string
    :param TaskId: [REQUIRED]
            The ID of the specific task execution in the Maintenance Window task that should be retrieved.
            

    :rtype: dict
    :return: {
        'WindowExecutionId': 'string',
        'TaskExecutionId': 'string',
        'TaskArn': 'string',
        'ServiceRole': 'string',
        'Type': 'RUN_COMMAND'|'AUTOMATION'|'STEP_FUNCTIONS'|'LAMBDA',
        'TaskParameters': [
            {
                'string': {
                    'Values': [
                        'string',
                    ]
                }
            },
        ],
        'Priority': 123,
        'MaxConcurrency': 'string',
        'MaxErrors': 'string',
        'Status': 'PENDING'|'IN_PROGRESS'|'SUCCESS'|'FAILED'|'TIMED_OUT'|'CANCELLING'|'CANCELLED'|'SKIPPED_OVERLAPPING',
        'StatusDetails': 'string',
        'StartTime': datetime(2015, 1, 1),
        'EndTime': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_maintenance_window_execution_task_invocation(WindowExecutionId=None, TaskId=None, InvocationId=None):
    """
    Retrieves a task invocation. A task invocation is a specific task executing on a specific target. Maintenance Windows report status for all invocations.
    See also: AWS API Documentation
    
    
    :example: response = client.get_maintenance_window_execution_task_invocation(
        WindowExecutionId='string',
        TaskId='string',
        InvocationId='string'
    )
    
    
    :type WindowExecutionId: string
    :param WindowExecutionId: [REQUIRED]
            The ID of the Maintenance Window execution for which the task is a part.
            

    :type TaskId: string
    :param TaskId: [REQUIRED]
            The ID of the specific task in the Maintenance Window task that should be retrieved.
            

    :type InvocationId: string
    :param InvocationId: [REQUIRED]
            The invocation ID to retrieve.
            

    :rtype: dict
    :return: {
        'WindowExecutionId': 'string',
        'TaskExecutionId': 'string',
        'InvocationId': 'string',
        'ExecutionId': 'string',
        'TaskType': 'RUN_COMMAND'|'AUTOMATION'|'STEP_FUNCTIONS'|'LAMBDA',
        'Parameters': 'string',
        'Status': 'PENDING'|'IN_PROGRESS'|'SUCCESS'|'FAILED'|'TIMED_OUT'|'CANCELLING'|'CANCELLED'|'SKIPPED_OVERLAPPING',
        'StatusDetails': 'string',
        'StartTime': datetime(2015, 1, 1),
        'EndTime': datetime(2015, 1, 1),
        'OwnerInformation': 'string',
        'WindowTargetId': 'string'
    }
    
    
    """
    pass

def get_maintenance_window_task(WindowId=None, WindowTaskId=None):
    """
    Lists the tasks in a Maintenance Window.
    See also: AWS API Documentation
    
    
    :example: response = client.get_maintenance_window_task(
        WindowId='string',
        WindowTaskId='string'
    )
    
    
    :type WindowId: string
    :param WindowId: [REQUIRED]
            The Maintenance Window ID that includes the task to retrieve.
            

    :type WindowTaskId: string
    :param WindowTaskId: [REQUIRED]
            The Maintenance Window task ID to retrieve.
            

    :rtype: dict
    :return: {
        'WindowId': 'string',
        'WindowTaskId': 'string',
        'Targets': [
            {
                'Key': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        'TaskArn': 'string',
        'ServiceRoleArn': 'string',
        'TaskType': 'RUN_COMMAND'|'AUTOMATION'|'STEP_FUNCTIONS'|'LAMBDA',
        'TaskParameters': {
            'string': {
                'Values': [
                    'string',
                ]
            }
        },
        'TaskInvocationParameters': {
            'RunCommand': {
                'Comment': 'string',
                'DocumentHash': 'string',
                'DocumentHashType': 'Sha256'|'Sha1',
                'NotificationConfig': {
                    'NotificationArn': 'string',
                    'NotificationEvents': [
                        'All'|'InProgress'|'Success'|'TimedOut'|'Cancelled'|'Failed',
                    ],
                    'NotificationType': 'Command'|'Invocation'
                },
                'OutputS3BucketName': 'string',
                'OutputS3KeyPrefix': 'string',
                'Parameters': {
                    'string': [
                        'string',
                    ]
                },
                'ServiceRoleArn': 'string',
                'TimeoutSeconds': 123
            },
            'Automation': {
                'DocumentVersion': 'string',
                'Parameters': {
                    'string': [
                        'string',
                    ]
                }
            },
            'StepFunctions': {
                'Input': 'string',
                'Name': 'string'
            },
            'Lambda': {
                'ClientContext': 'string',
                'Qualifier': 'string',
                'Payload': b'bytes'
            }
        },
        'Priority': 123,
        'MaxConcurrency': 'string',
        'MaxErrors': 'string',
        'LoggingInfo': {
            'S3BucketName': 'string',
            'S3KeyPrefix': 'string',
            'S3Region': 'string'
        },
        'Name': 'string',
        'Description': 'string'
    }
    
    
    :returns: 
    (string) --
    
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

def get_parameter(Name=None, WithDecryption=None):
    """
    Get information about a parameter by using the parameter name.
    See also: AWS API Documentation
    
    
    :example: response = client.get_parameter(
        Name='string',
        WithDecryption=True|False
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the parameter you want to query.
            

    :type WithDecryption: boolean
    :param WithDecryption: Return decrypted values for secure string parameters. This flag is ignored for String and StringList parameter types.

    :rtype: dict
    :return: {
        'Parameter': {
            'Name': 'string',
            'Type': 'String'|'StringList'|'SecureString',
            'Value': 'string',
            'Version': 123
        }
    }
    
    
    """
    pass

def get_parameter_history(Name=None, WithDecryption=None, MaxResults=None, NextToken=None):
    """
    Query a list of all parameters used by the AWS account.
    See also: AWS API Documentation
    
    
    :example: response = client.get_parameter_history(
        Name='string',
        WithDecryption=True|False,
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of a parameter you want to query.
            

    :type WithDecryption: boolean
    :param WithDecryption: Return decrypted values for secure string parameters. This flag is ignored for String and StringList parameter types.

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :rtype: dict
    :return: {
        'Parameters': [
            {
                'Name': 'string',
                'Type': 'String'|'StringList'|'SecureString',
                'KeyId': 'string',
                'LastModifiedDate': datetime(2015, 1, 1),
                'LastModifiedUser': 'string',
                'Description': 'string',
                'Value': 'string',
                'AllowedPattern': 'string',
                'Version': 123
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def get_parameters(Names=None, WithDecryption=None):
    """
    Get details of a parameter.
    See also: AWS API Documentation
    
    
    :example: response = client.get_parameters(
        Names=[
            'string',
        ],
        WithDecryption=True|False
    )
    
    
    :type Names: list
    :param Names: [REQUIRED]
            Names of the parameters for which you want to query information.
            (string) --
            

    :type WithDecryption: boolean
    :param WithDecryption: Return decrypted secure string value. Return decrypted values for secure string parameters. This flag is ignored for String and StringList parameter types.

    :rtype: dict
    :return: {
        'Parameters': [
            {
                'Name': 'string',
                'Type': 'String'|'StringList'|'SecureString',
                'Value': 'string',
                'Version': 123
            },
        ],
        'InvalidParameters': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_parameters_by_path(Path=None, Recursive=None, ParameterFilters=None, WithDecryption=None, MaxResults=None, NextToken=None):
    """
    Retrieve parameters in a specific hierarchy. For more information, see Working with Systems Manager Parameters .
    Request results are returned on a best-effort basis. If you specify MaxResults in the request, the response includes information up to the limit specified. The number of items returned, however, can be between zero and the value of MaxResults . If the service reaches an internal limit while processing the results, it stops the operation and returns the matching values up to that point and a NextToken . You can specify the NextToken in a subsequent call to get the next set of results.
    See also: AWS API Documentation
    
    
    :example: response = client.get_parameters_by_path(
        Path='string',
        Recursive=True|False,
        ParameterFilters=[
            {
                'Key': 'string',
                'Option': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        WithDecryption=True|False,
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type Path: string
    :param Path: [REQUIRED]
            The hierarchy for the parameter. Hierarchies start with a forward slash (/) and end with the parameter name. A hierarchy can have a maximum of 15 levels. Here is an example of a hierarchy: /Finance/Prod/IAD/WinServ2016/license33
            

    :type Recursive: boolean
    :param Recursive: Retrieve all parameters within a hierarchy.

    :type ParameterFilters: list
    :param ParameterFilters: Filters to limit the request results.
            (dict) --One or more filters. Use a filter to return a more specific list of results.
            Key (string) -- [REQUIRED]The name of the filter.
            Option (string) --Valid options are Equals and BeginsWith. For Path filter, valid options are Recursive and OneLevel.
            Values (list) --The value you want to search for.
            (string) --
            
            

    :type WithDecryption: boolean
    :param WithDecryption: Retrieve all parameters in a hierarchy with their value decrypted.

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :type NextToken: string
    :param NextToken: A token to start the list. Use this token to get the next set of results.

    :rtype: dict
    :return: {
        'Parameters': [
            {
                'Name': 'string',
                'Type': 'String'|'StringList'|'SecureString',
                'Value': 'string',
                'Version': 123
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def get_patch_baseline(BaselineId=None):
    """
    Retrieves information about a patch baseline.
    See also: AWS API Documentation
    
    
    :example: response = client.get_patch_baseline(
        BaselineId='string'
    )
    
    
    :type BaselineId: string
    :param BaselineId: [REQUIRED]
            The ID of the patch baseline to retrieve.
            

    :rtype: dict
    :return: {
        'BaselineId': 'string',
        'Name': 'string',
        'OperatingSystem': 'WINDOWS'|'AMAZON_LINUX'|'UBUNTU'|'REDHAT_ENTERPRISE_LINUX'|'SUSE'|'CENTOS',
        'GlobalFilters': {
            'PatchFilters': [
                {
                    'Key': 'PRODUCT'|'CLASSIFICATION'|'MSRC_SEVERITY'|'PATCH_ID'|'SECTION'|'PRIORITY'|'SEVERITY',
                    'Values': [
                        'string',
                    ]
                },
            ]
        },
        'ApprovalRules': {
            'PatchRules': [
                {
                    'PatchFilterGroup': {
                        'PatchFilters': [
                            {
                                'Key': 'PRODUCT'|'CLASSIFICATION'|'MSRC_SEVERITY'|'PATCH_ID'|'SECTION'|'PRIORITY'|'SEVERITY',
                                'Values': [
                                    'string',
                                ]
                            },
                        ]
                    },
                    'ComplianceLevel': 'CRITICAL'|'HIGH'|'MEDIUM'|'LOW'|'INFORMATIONAL'|'UNSPECIFIED',
                    'ApproveAfterDays': 123,
                    'EnableNonSecurity': True|False
                },
            ]
        },
        'ApprovedPatches': [
            'string',
        ],
        'ApprovedPatchesComplianceLevel': 'CRITICAL'|'HIGH'|'MEDIUM'|'LOW'|'INFORMATIONAL'|'UNSPECIFIED',
        'ApprovedPatchesEnableNonSecurity': True|False,
        'RejectedPatches': [
            'string',
        ],
        'PatchGroups': [
            'string',
        ],
        'CreatedDate': datetime(2015, 1, 1),
        'ModifiedDate': datetime(2015, 1, 1),
        'Description': 'string',
        'Sources': [
            {
                'Name': 'string',
                'Products': [
                    'string',
                ],
                'Configuration': 'string'
            },
        ]
    }
    
    
    :returns: 
    CriticalUpdates
    DefinitionUpdates
    Drivers
    FeaturePacks
    SecurityUpdates
    ServicePacks
    Tools
    UpdateRollups
    Updates
    Upgrades
    
    """
    pass

def get_patch_baseline_for_patch_group(PatchGroup=None, OperatingSystem=None):
    """
    Retrieves the patch baseline that should be used for the specified patch group.
    See also: AWS API Documentation
    
    
    :example: response = client.get_patch_baseline_for_patch_group(
        PatchGroup='string',
        OperatingSystem='WINDOWS'|'AMAZON_LINUX'|'UBUNTU'|'REDHAT_ENTERPRISE_LINUX'|'SUSE'|'CENTOS'
    )
    
    
    :type PatchGroup: string
    :param PatchGroup: [REQUIRED]
            The name of the patch group whose patch baseline should be retrieved.
            

    :type OperatingSystem: string
    :param OperatingSystem: Returns he operating system rule specified for patch groups using the patch baseline.

    :rtype: dict
    :return: {
        'BaselineId': 'string',
        'PatchGroup': 'string',
        'OperatingSystem': 'WINDOWS'|'AMAZON_LINUX'|'UBUNTU'|'REDHAT_ENTERPRISE_LINUX'|'SUSE'|'CENTOS'
    }
    
    
    """
    pass

def get_waiter(waiter_name=None):
    """
    
    :type waiter_name: 
    :param waiter_name: 

    """
    pass

def list_association_versions(AssociationId=None, MaxResults=None, NextToken=None):
    """
    Retrieves all versions of an association for a specific association ID.
    See also: AWS API Documentation
    
    
    :example: response = client.list_association_versions(
        AssociationId='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type AssociationId: string
    :param AssociationId: [REQUIRED]
            The association ID for which you want to view all versions.
            

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :type NextToken: string
    :param NextToken: A token to start the list. Use this token to get the next set of results.

    :rtype: dict
    :return: {
        'AssociationVersions': [
            {
                'AssociationId': 'string',
                'AssociationVersion': 'string',
                'CreatedDate': datetime(2015, 1, 1),
                'Name': 'string',
                'DocumentVersion': 'string',
                'Parameters': {
                    'string': [
                        'string',
                    ]
                },
                'Targets': [
                    {
                        'Key': 'string',
                        'Values': [
                            'string',
                        ]
                    },
                ],
                'ScheduleExpression': 'string',
                'OutputLocation': {
                    'S3Location': {
                        'OutputS3Region': 'string',
                        'OutputS3BucketName': 'string',
                        'OutputS3KeyPrefix': 'string'
                    }
                },
                'AssociationName': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (list) --
    (string) --
    
    
    
    
    
    """
    pass

def list_associations(AssociationFilterList=None, MaxResults=None, NextToken=None):
    """
    Lists the associations for the specified Systems Manager document or instance.
    See also: AWS API Documentation
    
    
    :example: response = client.list_associations(
        AssociationFilterList=[
            {
                'key': 'InstanceId'|'Name'|'AssociationId'|'AssociationStatusName'|'LastExecutedBefore'|'LastExecutedAfter'|'AssociationName',
                'value': 'string'
            },
        ],
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type AssociationFilterList: list
    :param AssociationFilterList: One or more filters. Use a filter to return a more specific list of results.
            (dict) --Describes a filter.
            key (string) -- [REQUIRED]The name of the filter.
            value (string) -- [REQUIRED]The filter value.
            
            

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :rtype: dict
    :return: {
        'Associations': [
            {
                'Name': 'string',
                'InstanceId': 'string',
                'AssociationId': 'string',
                'AssociationVersion': 'string',
                'DocumentVersion': 'string',
                'Targets': [
                    {
                        'Key': 'string',
                        'Values': [
                            'string',
                        ]
                    },
                ],
                'LastExecutionDate': datetime(2015, 1, 1),
                'Overview': {
                    'Status': 'string',
                    'DetailedStatus': 'string',
                    'AssociationStatusAggregatedCount': {
                        'string': 123
                    }
                },
                'ScheduleExpression': 'string',
                'AssociationName': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_command_invocations(CommandId=None, InstanceId=None, MaxResults=None, NextToken=None, Filters=None, Details=None):
    """
    An invocation is copy of a command sent to a specific instance. A command can apply to one or more instances. A command invocation applies to one instance. For example, if a user executes SendCommand against three instances, then a command invocation is created for each requested instance ID. ListCommandInvocations provide status about command execution.
    See also: AWS API Documentation
    
    
    :example: response = client.list_command_invocations(
        CommandId='string',
        InstanceId='string',
        MaxResults=123,
        NextToken='string',
        Filters=[
            {
                'key': 'InvokedAfter'|'InvokedBefore'|'Status',
                'value': 'string'
            },
        ],
        Details=True|False
    )
    
    
    :type CommandId: string
    :param CommandId: (Optional) The invocations for a specific command ID.

    :type InstanceId: string
    :param InstanceId: (Optional) The command execution details for a specific instance ID.

    :type MaxResults: integer
    :param MaxResults: (Optional) The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :type NextToken: string
    :param NextToken: (Optional) The token for the next set of items to return. (You received this token from a previous call.)

    :type Filters: list
    :param Filters: (Optional) One or more filters. Use a filter to return a more specific list of results.
            (dict) --Describes a command filter.
            key (string) -- [REQUIRED]The name of the filter.
            value (string) -- [REQUIRED]The filter value.
            
            

    :type Details: boolean
    :param Details: (Optional) If set this returns the response of the command executions and any command output. By default this is set to False.

    :rtype: dict
    :return: {
        'CommandInvocations': [
            {
                'CommandId': 'string',
                'InstanceId': 'string',
                'InstanceName': 'string',
                'Comment': 'string',
                'DocumentName': 'string',
                'RequestedDateTime': datetime(2015, 1, 1),
                'Status': 'Pending'|'InProgress'|'Delayed'|'Success'|'Cancelled'|'TimedOut'|'Failed'|'Cancelling',
                'StatusDetails': 'string',
                'TraceOutput': 'string',
                'StandardOutputUrl': 'string',
                'StandardErrorUrl': 'string',
                'CommandPlugins': [
                    {
                        'Name': 'string',
                        'Status': 'Pending'|'InProgress'|'Success'|'TimedOut'|'Cancelled'|'Failed',
                        'StatusDetails': 'string',
                        'ResponseCode': 123,
                        'ResponseStartDateTime': datetime(2015, 1, 1),
                        'ResponseFinishDateTime': datetime(2015, 1, 1),
                        'Output': 'string',
                        'StandardOutputUrl': 'string',
                        'StandardErrorUrl': 'string',
                        'OutputS3Region': 'string',
                        'OutputS3BucketName': 'string',
                        'OutputS3KeyPrefix': 'string'
                    },
                ],
                'ServiceRole': 'string',
                'NotificationConfig': {
                    'NotificationArn': 'string',
                    'NotificationEvents': [
                        'All'|'InProgress'|'Success'|'TimedOut'|'Cancelled'|'Failed',
                    ],
                    'NotificationType': 'Command'|'Invocation'
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Pending: The command has not been sent to the instance.
    In Progress: The command has been sent to the instance but has not reached a terminal state.
    Success: The execution of the command or plugin was successfully completed. This is a terminal state.
    Delivery Timed Out: The command was not delivered to the instance before the delivery timeout expired. Delivery timeouts do not count against the parent command's MaxErrors limit, but they do contribute to whether the parent command status is Success or Incomplete. This is a terminal state.
    Execution Timed Out: Command execution started on the instance, but the execution was not complete before the execution timeout expired. Execution timeouts count against the MaxErrors limit of the parent command. This is a terminal state.
    Failed: The command was not successful on the instance. For a plugin, this indicates that the result code was not zero. For a command invocation, this indicates that the result code for one or more plugins was not zero. Invocation failures count against the MaxErrors limit of the parent command. This is a terminal state.
    Canceled: The command was terminated before it was completed. This is a terminal state.
    Undeliverable: The command can't be delivered to the instance. The instance might not exist or might not be responding. Undeliverable invocations don't count against the parent command's MaxErrors limit and don't contribute to whether the parent command status is Success or Incomplete. This is a terminal state.
    Terminated: The parent command exceeded its MaxErrors limit and subsequent command invocations were canceled by the system. This is a terminal state.
    
    """
    pass

def list_commands(CommandId=None, InstanceId=None, MaxResults=None, NextToken=None, Filters=None):
    """
    Lists the commands requested by users of the AWS account.
    See also: AWS API Documentation
    
    
    :example: response = client.list_commands(
        CommandId='string',
        InstanceId='string',
        MaxResults=123,
        NextToken='string',
        Filters=[
            {
                'key': 'InvokedAfter'|'InvokedBefore'|'Status',
                'value': 'string'
            },
        ]
    )
    
    
    :type CommandId: string
    :param CommandId: (Optional) If provided, lists only the specified command.

    :type InstanceId: string
    :param InstanceId: (Optional) Lists commands issued against this instance ID.

    :type MaxResults: integer
    :param MaxResults: (Optional) The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :type NextToken: string
    :param NextToken: (Optional) The token for the next set of items to return. (You received this token from a previous call.)

    :type Filters: list
    :param Filters: (Optional) One or more filters. Use a filter to return a more specific list of results.
            (dict) --Describes a command filter.
            key (string) -- [REQUIRED]The name of the filter.
            value (string) -- [REQUIRED]The filter value.
            
            

    :rtype: dict
    :return: {
        'Commands': [
            {
                'CommandId': 'string',
                'DocumentName': 'string',
                'Comment': 'string',
                'ExpiresAfter': datetime(2015, 1, 1),
                'Parameters': {
                    'string': [
                        'string',
                    ]
                },
                'InstanceIds': [
                    'string',
                ],
                'Targets': [
                    {
                        'Key': 'string',
                        'Values': [
                            'string',
                        ]
                    },
                ],
                'RequestedDateTime': datetime(2015, 1, 1),
                'Status': 'Pending'|'InProgress'|'Success'|'Cancelled'|'Failed'|'TimedOut'|'Cancelling',
                'StatusDetails': 'string',
                'OutputS3Region': 'string',
                'OutputS3BucketName': 'string',
                'OutputS3KeyPrefix': 'string',
                'MaxConcurrency': 'string',
                'MaxErrors': 'string',
                'TargetCount': 123,
                'CompletedCount': 123,
                'ErrorCount': 123,
                'ServiceRole': 'string',
                'NotificationConfig': {
                    'NotificationArn': 'string',
                    'NotificationEvents': [
                        'All'|'InProgress'|'Success'|'TimedOut'|'Cancelled'|'Failed',
                    ],
                    'NotificationType': 'Command'|'Invocation'
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (list) --
    (string) --
    
    
    
    
    
    """
    pass

def list_compliance_items(Filters=None, ResourceIds=None, ResourceTypes=None, NextToken=None, MaxResults=None):
    """
    For a specified resource ID, this API action returns a list of compliance statuses for different resource types. Currently, you can only specify one resource ID per call. List results depend on the criteria specified in the filter.
    See also: AWS API Documentation
    
    
    :example: response = client.list_compliance_items(
        Filters=[
            {
                'Key': 'string',
                'Values': [
                    'string',
                ],
                'Type': 'EQUAL'|'NOT_EQUAL'|'BEGIN_WITH'|'LESS_THAN'|'GREATER_THAN'
            },
        ],
        ResourceIds=[
            'string',
        ],
        ResourceTypes=[
            'string',
        ],
        NextToken='string',
        MaxResults=123
    )
    
    
    :type Filters: list
    :param Filters: One or more compliance filters. Use a filter to return a more specific list of results.
            (dict) --One or more filters. Use a filter to return a more specific list of results.
            Key (string) --The name of the filter.
            Values (list) --The value for which to search.
            (string) --
            Type (string) --The type of comparison that should be performed for the value: Equal, NotEqual, BeginWith, LessThan, or GreaterThan.
            
            

    :type ResourceIds: list
    :param ResourceIds: The ID for the resources from which to get compliance information. Currently, you can only specify one resource ID.
            (string) --
            

    :type ResourceTypes: list
    :param ResourceTypes: The type of resource from which to get compliance information. Currently, the only supported resource type is ManagedInstance .
            (string) --
            

    :type NextToken: string
    :param NextToken: A token to start the list. Use this token to get the next set of results.

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :rtype: dict
    :return: {
        'ComplianceItems': [
            {
                'ComplianceType': 'string',
                'ResourceType': 'string',
                'ResourceId': 'string',
                'Id': 'string',
                'Title': 'string',
                'Status': 'COMPLIANT'|'NON_COMPLIANT',
                'Severity': 'CRITICAL'|'HIGH'|'MEDIUM'|'LOW'|'INFORMATIONAL'|'UNSPECIFIED',
                'ExecutionSummary': {
                    'ExecutionTime': datetime(2015, 1, 1),
                    'ExecutionId': 'string',
                    'ExecutionType': 'string'
                },
                'Details': {
                    'string': 'string'
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def list_compliance_summaries(Filters=None, NextToken=None, MaxResults=None):
    """
    Returns a summary count of compliant and non-compliant resources for a compliance type. For example, this call can return State Manager associations, patches, or custom compliance types according to the filter criteria that you specify.
    See also: AWS API Documentation
    
    
    :example: response = client.list_compliance_summaries(
        Filters=[
            {
                'Key': 'string',
                'Values': [
                    'string',
                ],
                'Type': 'EQUAL'|'NOT_EQUAL'|'BEGIN_WITH'|'LESS_THAN'|'GREATER_THAN'
            },
        ],
        NextToken='string',
        MaxResults=123
    )
    
    
    :type Filters: list
    :param Filters: One or more compliance or inventory filters. Use a filter to return a more specific list of results.
            (dict) --One or more filters. Use a filter to return a more specific list of results.
            Key (string) --The name of the filter.
            Values (list) --The value for which to search.
            (string) --
            Type (string) --The type of comparison that should be performed for the value: Equal, NotEqual, BeginWith, LessThan, or GreaterThan.
            
            

    :type NextToken: string
    :param NextToken: A token to start the list. Use this token to get the next set of results.

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. Currently, you can specify null or 50. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :rtype: dict
    :return: {
        'ComplianceSummaryItems': [
            {
                'ComplianceType': 'string',
                'CompliantSummary': {
                    'CompliantCount': 123,
                    'SeveritySummary': {
                        'CriticalCount': 123,
                        'HighCount': 123,
                        'MediumCount': 123,
                        'LowCount': 123,
                        'InformationalCount': 123,
                        'UnspecifiedCount': 123
                    }
                },
                'NonCompliantSummary': {
                    'NonCompliantCount': 123,
                    'SeveritySummary': {
                        'CriticalCount': 123,
                        'HighCount': 123,
                        'MediumCount': 123,
                        'LowCount': 123,
                        'InformationalCount': 123,
                        'UnspecifiedCount': 123
                    }
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_document_versions(Name=None, MaxResults=None, NextToken=None):
    """
    List all versions for a document.
    See also: AWS API Documentation
    
    
    :example: response = client.list_document_versions(
        Name='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the document about which you want version information.
            

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :rtype: dict
    :return: {
        'DocumentVersions': [
            {
                'Name': 'string',
                'DocumentVersion': 'string',
                'CreatedDate': datetime(2015, 1, 1),
                'IsDefaultVersion': True|False,
                'DocumentFormat': 'YAML'|'JSON'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_documents(DocumentFilterList=None, Filters=None, MaxResults=None, NextToken=None):
    """
    Describes one or more of your Systems Manager documents.
    See also: AWS API Documentation
    
    
    :example: response = client.list_documents(
        DocumentFilterList=[
            {
                'key': 'Name'|'Owner'|'PlatformTypes'|'DocumentType',
                'value': 'string'
            },
        ],
        Filters=[
            {
                'Key': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type DocumentFilterList: list
    :param DocumentFilterList: One or more filters. Use a filter to return a more specific list of results.
            (dict) --Describes a filter.
            key (string) -- [REQUIRED]The name of the filter.
            value (string) -- [REQUIRED]The value of the filter.
            
            

    :type Filters: list
    :param Filters: One or more filters. Use a filter to return a more specific list of results.
            (dict) --One or more filters. Use a filter to return a more specific list of documents.
            For keys, you can specify one or more tags that have been applied to a document.
            Other valid values include Owner, Name, PlatformTypes, and DocumentType.
            Note that only one Owner can be specified in a request. For example: Key=Owner,Values=Self .
            If you use Name as a key, you can use a name prefix to return a list of documents. For example, in the AWS CLI, to return a list of all documents that begin with Te , run the following command:
            aws ssm list-documents --filters Key=Name,Values=Te
            If you specify more than two keys, only documents that are identified by all the tags are returned in the results. If you specify more than two values for a key, documents that are identified by any of the values are returned in the results.
            To specify a custom key and value pair, use the format Key=tag:[tagName],Values=[valueName] .
            For example, if you created a Key called region and are using the AWS CLI to call the list-documents command:
            aws ssm list-documents --filters Key=tag:region,Values=east,west Key=Owner,Values=Self
            Key (string) --The name of the filter key.
            Values (list) --The value for the filter key.
            (string) --
            
            

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :rtype: dict
    :return: {
        'DocumentIdentifiers': [
            {
                'Name': 'string',
                'Owner': 'string',
                'PlatformTypes': [
                    'Windows'|'Linux',
                ],
                'DocumentVersion': 'string',
                'DocumentType': 'Command'|'Policy'|'Automation',
                'SchemaVersion': 'string',
                'DocumentFormat': 'YAML'|'JSON',
                'TargetType': 'string',
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_inventory_entries(InstanceId=None, TypeName=None, Filters=None, NextToken=None, MaxResults=None):
    """
    A list of inventory items returned by the request.
    See also: AWS API Documentation
    
    
    :example: response = client.list_inventory_entries(
        InstanceId='string',
        TypeName='string',
        Filters=[
            {
                'Key': 'string',
                'Values': [
                    'string',
                ],
                'Type': 'Equal'|'NotEqual'|'BeginWith'|'LessThan'|'GreaterThan'
            },
        ],
        NextToken='string',
        MaxResults=123
    )
    
    
    :type InstanceId: string
    :param InstanceId: [REQUIRED]
            The instance ID for which you want inventory information.
            

    :type TypeName: string
    :param TypeName: [REQUIRED]
            The type of inventory item for which you want information.
            

    :type Filters: list
    :param Filters: One or more filters. Use a filter to return a more specific list of results.
            (dict) --One or more filters. Use a filter to return a more specific list of results.
            Key (string) -- [REQUIRED]The name of the filter key.
            Values (list) -- [REQUIRED]Inventory filter values. Example: inventory filter where instance IDs are specified as values Key=AWS:InstanceInformation.InstanceId,Values= i-a12b3c4d5e6g, i-1a2b3c4d5e6,Type=Equal
            (string) --
            Type (string) --The type of filter. Valid values include the following: 'Equal'|'NotEqual'|'BeginWith'|'LessThan'|'GreaterThan'
            
            

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :rtype: dict
    :return: {
        'TypeName': 'string',
        'InstanceId': 'string',
        'SchemaVersion': 'string',
        'CaptureTime': 'string',
        'Entries': [
            {
                'string': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (dict) --
    (string) --
    (string) --
    
    
    
    
    
    """
    pass

def list_resource_compliance_summaries(Filters=None, NextToken=None, MaxResults=None):
    """
    Returns a resource-level summary count. The summary includes information about compliant and non-compliant statuses and detailed compliance-item severity counts, according to the filter criteria you specify.
    See also: AWS API Documentation
    
    
    :example: response = client.list_resource_compliance_summaries(
        Filters=[
            {
                'Key': 'string',
                'Values': [
                    'string',
                ],
                'Type': 'EQUAL'|'NOT_EQUAL'|'BEGIN_WITH'|'LESS_THAN'|'GREATER_THAN'
            },
        ],
        NextToken='string',
        MaxResults=123
    )
    
    
    :type Filters: list
    :param Filters: One or more filters. Use a filter to return a more specific list of results.
            (dict) --One or more filters. Use a filter to return a more specific list of results.
            Key (string) --The name of the filter.
            Values (list) --The value for which to search.
            (string) --
            Type (string) --The type of comparison that should be performed for the value: Equal, NotEqual, BeginWith, LessThan, or GreaterThan.
            
            

    :type NextToken: string
    :param NextToken: A token to start the list. Use this token to get the next set of results.

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :rtype: dict
    :return: {
        'ResourceComplianceSummaryItems': [
            {
                'ComplianceType': 'string',
                'ResourceType': 'string',
                'ResourceId': 'string',
                'Status': 'COMPLIANT'|'NON_COMPLIANT',
                'OverallSeverity': 'CRITICAL'|'HIGH'|'MEDIUM'|'LOW'|'INFORMATIONAL'|'UNSPECIFIED',
                'ExecutionSummary': {
                    'ExecutionTime': datetime(2015, 1, 1),
                    'ExecutionId': 'string',
                    'ExecutionType': 'string'
                },
                'CompliantSummary': {
                    'CompliantCount': 123,
                    'SeveritySummary': {
                        'CriticalCount': 123,
                        'HighCount': 123,
                        'MediumCount': 123,
                        'LowCount': 123,
                        'InformationalCount': 123,
                        'UnspecifiedCount': 123
                    }
                },
                'NonCompliantSummary': {
                    'NonCompliantCount': 123,
                    'SeveritySummary': {
                        'CriticalCount': 123,
                        'HighCount': 123,
                        'MediumCount': 123,
                        'LowCount': 123,
                        'InformationalCount': 123,
                        'UnspecifiedCount': 123
                    }
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_resource_data_sync(NextToken=None, MaxResults=None):
    """
    Lists your resource data sync configurations. Includes information about the last time a sync attempted to start, the last sync status, and the last time a sync successfully completed.
    The number of sync configurations might be too large to return using a single call to ListResourceDataSync . You can limit the number of sync configurations returned by using the MaxResults parameter. To determine whether there are more sync configurations to list, check the value of NextToken in the output. If there are more sync configurations to list, you can request them by specifying the NextToken returned in the call to the parameter of a subsequent call.
    See also: AWS API Documentation
    
    
    :example: response = client.list_resource_data_sync(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: A token to start the list. Use this token to get the next set of results.

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :rtype: dict
    :return: {
        'ResourceDataSyncItems': [
            {
                'SyncName': 'string',
                'S3Destination': {
                    'BucketName': 'string',
                    'Prefix': 'string',
                    'SyncFormat': 'JsonSerDe',
                    'Region': 'string',
                    'AWSKMSKeyARN': 'string'
                },
                'LastSyncTime': datetime(2015, 1, 1),
                'LastSuccessfulSyncTime': datetime(2015, 1, 1),
                'LastStatus': 'Successful'|'Failed'|'InProgress',
                'SyncCreatedTime': datetime(2015, 1, 1),
                'LastSyncStatusMessage': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_tags_for_resource(ResourceType=None, ResourceId=None):
    """
    Returns a list of the tags assigned to the specified resource.
    See also: AWS API Documentation
    
    
    :example: response = client.list_tags_for_resource(
        ResourceType='Document'|'ManagedInstance'|'MaintenanceWindow'|'Parameter'|'PatchBaseline',
        ResourceId='string'
    )
    
    
    :type ResourceType: string
    :param ResourceType: [REQUIRED]
            Returns a list of tags for a specific resource type.
            

    :type ResourceId: string
    :param ResourceId: [REQUIRED]
            The resource ID for which you want to see a list of tags.
            

    :rtype: dict
    :return: {
        'TagList': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    """
    pass

def modify_document_permission(Name=None, PermissionType=None, AccountIdsToAdd=None, AccountIdsToRemove=None):
    """
    Shares a Systems Manager document publicly or privately. If you share a document privately, you must specify the AWS user account IDs for those people who can use the document. If you share a document publicly, you must specify All as the account ID.
    See also: AWS API Documentation
    
    
    :example: response = client.modify_document_permission(
        Name='string',
        PermissionType='Share',
        AccountIdsToAdd=[
            'string',
        ],
        AccountIdsToRemove=[
            'string',
        ]
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the document that you want to share.
            

    :type PermissionType: string
    :param PermissionType: [REQUIRED]
            The permission type for the document. The permission type can be Share .
            

    :type AccountIdsToAdd: list
    :param AccountIdsToAdd: The AWS user accounts that should have access to the document. The account IDs can either be a group of account IDs or All .
            (string) --
            

    :type AccountIdsToRemove: list
    :param AccountIdsToRemove: The AWS user accounts that should no longer have access to the document. The AWS user account can either be a group of account IDs or All . This action has a higher priority than AccountIdsToAdd . If you specify an account ID to add and the same ID to remove, the system removes access to the document.
            (string) --
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def put_compliance_items(ResourceId=None, ResourceType=None, ComplianceType=None, ExecutionSummary=None, Items=None, ItemContentHash=None):
    """
    Registers a compliance type and other compliance details on a designated resource. This action lets you register custom compliance details with a resource. This call overwrites existing compliance information on the resource, so you must provide a full list of compliance items each time that you send the request.
    ComplianceType can be one of the following:
    See also: AWS API Documentation
    
    
    :example: response = client.put_compliance_items(
        ResourceId='string',
        ResourceType='string',
        ComplianceType='string',
        ExecutionSummary={
            'ExecutionTime': datetime(2015, 1, 1),
            'ExecutionId': 'string',
            'ExecutionType': 'string'
        },
        Items=[
            {
                'Id': 'string',
                'Title': 'string',
                'Severity': 'CRITICAL'|'HIGH'|'MEDIUM'|'LOW'|'INFORMATIONAL'|'UNSPECIFIED',
                'Status': 'COMPLIANT'|'NON_COMPLIANT',
                'Details': {
                    'string': 'string'
                }
            },
        ],
        ItemContentHash='string'
    )
    
    
    :type ResourceId: string
    :param ResourceId: [REQUIRED]
            Specify an ID for this resource. For a managed instance, this is the instance ID.
            

    :type ResourceType: string
    :param ResourceType: [REQUIRED]
            Specify the type of resource. ManagedInstance is currently the only supported resource type.
            

    :type ComplianceType: string
    :param ComplianceType: [REQUIRED]
            Specify the compliance type. For example, specify Association (for a State Manager association), Patch, or Custom:string .
            

    :type ExecutionSummary: dict
    :param ExecutionSummary: [REQUIRED]
            A summary of the call execution that includes an execution ID, the type of execution (for example, Command ), and the date/time of the execution using a datetime object that is saved in the following format: yyyy-MM-dd'T'HH:mm:ss'Z'.
            ExecutionTime (datetime) -- [REQUIRED]The time the execution ran as a datetime object that is saved in the following format: yyyy-MM-dd'T'HH:mm:ss'Z'.
            ExecutionId (string) --An ID created by the system when PutComplianceItems was called. For example, CommandID is a valid execution ID. You can use this ID in subsequent calls.
            ExecutionType (string) --The type of execution. For example, Command is a valid execution type.
            

    :type Items: list
    :param Items: [REQUIRED]
            Information about the compliance as defined by the resource type. For example, for a patch compliance type, Items includes information about the PatchSeverity, Classification, etc.
            (dict) --Information about a compliance item.
            Id (string) --The compliance item ID. For example, if the compliance item is a Windows patch, the ID could be the number of the KB article.
            Title (string) --The title of the compliance item. For example, if the compliance item is a Windows patch, the title could be the title of the KB article for the patch. Here's an example: Security Update for Active Directory Federation Services.
            Severity (string) -- [REQUIRED]The severity of the compliance status. Severity can be one of the following: Critical, High, Medium, Low, Informational, Unspecified.
            Status (string) -- [REQUIRED]The status of the compliance item. An item is either COMPLIANT or NON_COMPLIANT.
            Details (dict) --A 'Key': 'Value' tag combination for the compliance item.
            (string) --
            (string) --
            
            

    :type ItemContentHash: string
    :param ItemContentHash: MD5 or SHA-256 content hash. The content hash is used to determine if existing information should be overwritten or ignored. If the content hashes match, the request to put compliance information is ignored.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    ResourceId (string) -- [REQUIRED]
    Specify an ID for this resource. For a managed instance, this is the instance ID.
    
    ResourceType (string) -- [REQUIRED]
    Specify the type of resource. ManagedInstance is currently the only supported resource type.
    
    ComplianceType (string) -- [REQUIRED]
    Specify the compliance type. For example, specify Association (for a State Manager association), Patch, or Custom:string .
    
    ExecutionSummary (dict) -- [REQUIRED]
    A summary of the call execution that includes an execution ID, the type of execution (for example, Command ), and the date/time of the execution using a datetime object that is saved in the following format: yyyy-MM-dd'T'HH:mm:ss'Z'.
    
    ExecutionTime (datetime) -- [REQUIRED]The time the execution ran as a datetime object that is saved in the following format: yyyy-MM-dd'T'HH:mm:ss'Z'.
    
    ExecutionId (string) --An ID created by the system when PutComplianceItems was called. For example, CommandID is a valid execution ID. You can use this ID in subsequent calls.
    
    ExecutionType (string) --The type of execution. For example, Command is a valid execution type.
    
    
    
    Items (list) -- [REQUIRED]
    Information about the compliance as defined by the resource type. For example, for a patch compliance type, Items includes information about the PatchSeverity, Classification, etc.
    
    (dict) --Information about a compliance item.
    
    Id (string) --The compliance item ID. For example, if the compliance item is a Windows patch, the ID could be the number of the KB article.
    
    Title (string) --The title of the compliance item. For example, if the compliance item is a Windows patch, the title could be the title of the KB article for the patch. Here's an example: Security Update for Active Directory Federation Services.
    
    Severity (string) -- [REQUIRED]The severity of the compliance status. Severity can be one of the following: Critical, High, Medium, Low, Informational, Unspecified.
    
    Status (string) -- [REQUIRED]The status of the compliance item. An item is either COMPLIANT or NON_COMPLIANT.
    
    Details (dict) --A "Key": "Value" tag combination for the compliance item.
    
    (string) --
    (string) --
    
    
    
    
    
    
    
    
    ItemContentHash (string) -- MD5 or SHA-256 content hash. The content hash is used to determine if existing information should be overwritten or ignored. If the content hashes match, the request to put compliance information is ignored.
    
    """
    pass

def put_inventory(InstanceId=None, Items=None):
    """
    Bulk update custom inventory items on one more instance. The request adds an inventory item, if it doesn't already exist, or updates an inventory item, if it does exist.
    See also: AWS API Documentation
    
    
    :example: response = client.put_inventory(
        InstanceId='string',
        Items=[
            {
                'TypeName': 'string',
                'SchemaVersion': 'string',
                'CaptureTime': 'string',
                'ContentHash': 'string',
                'Content': [
                    {
                        'string': 'string'
                    },
                ],
                'Context': {
                    'string': 'string'
                }
            },
        ]
    )
    
    
    :type InstanceId: string
    :param InstanceId: [REQUIRED]
            One or more instance IDs where you want to add or update inventory items.
            

    :type Items: list
    :param Items: [REQUIRED]
            The inventory items that you want to add or update on instances.
            (dict) --Information collected from managed instances based on your inventory policy document
            TypeName (string) -- [REQUIRED]The name of the inventory type. Default inventory item type names start with AWS. Custom inventory type names will start with Custom. Default inventory item types include the following: AWS:AWSComponent, AWS:Application, AWS:InstanceInformation, AWS:Network, and AWS:WindowsUpdate.
            SchemaVersion (string) -- [REQUIRED]The schema version for the inventory item.
            CaptureTime (string) -- [REQUIRED]The time the inventory information was collected.
            ContentHash (string) --MD5 hash of the inventory item type contents. The content hash is used to determine whether to update inventory information. The PutInventory API does not update the inventory item type contents if the MD5 hash has not changed since last update.
            Content (list) --The inventory data of the inventory type.
            (dict) --
            (string) --
            (string) --
            
            Context (dict) --A map of associated properties for a specified inventory type. For example, with this attribute, you can specify the ExecutionId , ExecutionType , ComplianceType properties of the AWS:ComplianceItem type.
            (string) --
            (string) --
            
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def put_parameter(Name=None, Description=None, Value=None, Type=None, KeyId=None, Overwrite=None, AllowedPattern=None):
    """
    Add one or more parameters to the system.
    See also: AWS API Documentation
    
    
    :example: response = client.put_parameter(
        Name='string',
        Description='string',
        Value='string',
        Type='String'|'StringList'|'SecureString',
        KeyId='string',
        Overwrite=True|False,
        AllowedPattern='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The fully qualified name of the parameter that you want to add to the system. The fully qualified name includes the complete hierarchy of the parameter path and name. For example: /Dev/DBServer/MySQL/db-string13
            For information about parameter name requirements and restrictions, see About Creating Systems Manager Parameters in the AWS Systems Manager User Guide .
            Note
            The maximum length constraint listed below includes capacity for additional system attributes that are not part of the name. The maximum length for the fully qualified parameter name is 1011 characters.
            

    :type Description: string
    :param Description: Information about the parameter that you want to add to the system.

    :type Value: string
    :param Value: [REQUIRED]
            The parameter value that you want to add to the system.
            

    :type Type: string
    :param Type: [REQUIRED]
            The type of parameter that you want to add to the system.
            

    :type KeyId: string
    :param KeyId: The KMS Key ID that you want to use to encrypt a parameter when you choose the SecureString data type. If you don't specify a key ID, the system uses the default key associated with your AWS account.

    :type Overwrite: boolean
    :param Overwrite: Overwrite an existing parameter. If not specified, will default to 'false'.

    :type AllowedPattern: string
    :param AllowedPattern: A regular expression used to validate the parameter value. For example, for String types with values restricted to numbers, you can specify the following: AllowedPattern=^d+$

    :rtype: dict
    :return: {
        'Version': 123
    }
    
    
    """
    pass

def register_default_patch_baseline(BaselineId=None):
    """
    Defines the default patch baseline.
    See also: AWS API Documentation
    
    
    :example: response = client.register_default_patch_baseline(
        BaselineId='string'
    )
    
    
    :type BaselineId: string
    :param BaselineId: [REQUIRED]
            The ID of the patch baseline that should be the default patch baseline.
            

    :rtype: dict
    :return: {
        'BaselineId': 'string'
    }
    
    
    """
    pass

def register_patch_baseline_for_patch_group(BaselineId=None, PatchGroup=None):
    """
    Registers a patch baseline for a patch group.
    See also: AWS API Documentation
    
    
    :example: response = client.register_patch_baseline_for_patch_group(
        BaselineId='string',
        PatchGroup='string'
    )
    
    
    :type BaselineId: string
    :param BaselineId: [REQUIRED]
            The ID of the patch baseline to register the patch group with.
            

    :type PatchGroup: string
    :param PatchGroup: [REQUIRED]
            The name of the patch group that should be registered with the patch baseline.
            

    :rtype: dict
    :return: {
        'BaselineId': 'string',
        'PatchGroup': 'string'
    }
    
    
    """
    pass

def register_target_with_maintenance_window(WindowId=None, ResourceType=None, Targets=None, OwnerInformation=None, Name=None, Description=None, ClientToken=None):
    """
    Registers a target with a Maintenance Window.
    See also: AWS API Documentation
    
    
    :example: response = client.register_target_with_maintenance_window(
        WindowId='string',
        ResourceType='INSTANCE',
        Targets=[
            {
                'Key': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        OwnerInformation='string',
        Name='string',
        Description='string',
        ClientToken='string'
    )
    
    
    :type WindowId: string
    :param WindowId: [REQUIRED]
            The ID of the Maintenance Window the target should be registered with.
            

    :type ResourceType: string
    :param ResourceType: [REQUIRED]
            The type of target being registered with the Maintenance Window.
            

    :type Targets: list
    :param Targets: [REQUIRED]
            The targets (either instances or tags). Instances are specified using Key=instanceids,Values=instanceid1,instanceid2. Tags are specified using Key=tag name,Values=tag value.
            (dict) --An array of search criteria that targets instances using a Key,Value combination that you specify. Targets is required if you don't provide one or more instance IDs in the call.
            Key (string) --User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:Amazon EC2 tagor InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see Executing a Command Using Systems Manager Run Command .
            Values (list) --User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see Executing a Command Using Systems Manager Run Command .
            (string) --
            
            

    :type OwnerInformation: string
    :param OwnerInformation: User-provided value that will be included in any CloudWatch events raised while running tasks for these targets in this Maintenance Window.

    :type Name: string
    :param Name: An optional name for the target.

    :type Description: string
    :param Description: An optional description for the target.

    :type ClientToken: string
    :param ClientToken: User-provided idempotency token.
            This field is autopopulated if not provided.
            

    :rtype: dict
    :return: {
        'WindowTargetId': 'string'
    }
    
    
    """
    pass

def register_task_with_maintenance_window(WindowId=None, Targets=None, TaskArn=None, ServiceRoleArn=None, TaskType=None, TaskParameters=None, TaskInvocationParameters=None, Priority=None, MaxConcurrency=None, MaxErrors=None, LoggingInfo=None, Name=None, Description=None, ClientToken=None):
    """
    Adds a new task to a Maintenance Window.
    See also: AWS API Documentation
    
    
    :example: response = client.register_task_with_maintenance_window(
        WindowId='string',
        Targets=[
            {
                'Key': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        TaskArn='string',
        ServiceRoleArn='string',
        TaskType='RUN_COMMAND'|'AUTOMATION'|'STEP_FUNCTIONS'|'LAMBDA',
        TaskParameters={
            'string': {
                'Values': [
                    'string',
                ]
            }
        },
        TaskInvocationParameters={
            'RunCommand': {
                'Comment': 'string',
                'DocumentHash': 'string',
                'DocumentHashType': 'Sha256'|'Sha1',
                'NotificationConfig': {
                    'NotificationArn': 'string',
                    'NotificationEvents': [
                        'All'|'InProgress'|'Success'|'TimedOut'|'Cancelled'|'Failed',
                    ],
                    'NotificationType': 'Command'|'Invocation'
                },
                'OutputS3BucketName': 'string',
                'OutputS3KeyPrefix': 'string',
                'Parameters': {
                    'string': [
                        'string',
                    ]
                },
                'ServiceRoleArn': 'string',
                'TimeoutSeconds': 123
            },
            'Automation': {
                'DocumentVersion': 'string',
                'Parameters': {
                    'string': [
                        'string',
                    ]
                }
            },
            'StepFunctions': {
                'Input': 'string',
                'Name': 'string'
            },
            'Lambda': {
                'ClientContext': 'string',
                'Qualifier': 'string',
                'Payload': b'bytes'
            }
        },
        Priority=123,
        MaxConcurrency='string',
        MaxErrors='string',
        LoggingInfo={
            'S3BucketName': 'string',
            'S3KeyPrefix': 'string',
            'S3Region': 'string'
        },
        Name='string',
        Description='string',
        ClientToken='string'
    )
    
    
    :type WindowId: string
    :param WindowId: [REQUIRED]
            The id of the Maintenance Window the task should be added to.
            

    :type Targets: list
    :param Targets: [REQUIRED]
            The targets (either instances or tags). Instances are specified using Key=instanceids,Values=instanceid1,instanceid2. Tags are specified using Key=tag name,Values=tag value.
            (dict) --An array of search criteria that targets instances using a Key,Value combination that you specify. Targets is required if you don't provide one or more instance IDs in the call.
            Key (string) --User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:Amazon EC2 tagor InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see Executing a Command Using Systems Manager Run Command .
            Values (list) --User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see Executing a Command Using Systems Manager Run Command .
            (string) --
            
            

    :type TaskArn: string
    :param TaskArn: [REQUIRED]
            The ARN of the task to execute
            

    :type ServiceRoleArn: string
    :param ServiceRoleArn: [REQUIRED]
            The role that should be assumed when executing the task.
            

    :type TaskType: string
    :param TaskType: [REQUIRED]
            The type of task being registered.
            

    :type TaskParameters: dict
    :param TaskParameters: The parameters that should be passed to the task when it is executed.
            (string) --
            (dict) --Defines the values for a task parameter.
            Values (list) --This field contains an array of 0 or more strings, each 1 to 255 characters in length.
            (string) --
            
            

    :type TaskInvocationParameters: dict
    :param TaskInvocationParameters: The parameters that the task should use during execution. Populate only the fields that match the task type. All other fields should be empty.
            RunCommand (dict) --The parameters for a RUN_COMMAND task type.
            Comment (string) --Information about the command(s) to execute.
            DocumentHash (string) --The SHA-256 or SHA-1 hash created by the system when the document was created. SHA-1 hashes have been deprecated.
            DocumentHashType (string) --SHA-256 or SHA-1. SHA-1 hashes have been deprecated.
            NotificationConfig (dict) --Configurations for sending notifications about command status changes on a per-instance basis.
            NotificationArn (string) --An Amazon Resource Name (ARN) for a Simple Notification Service (SNS) topic. Run Command pushes notifications about command status changes to this topic.
            NotificationEvents (list) --The different events for which you can receive notifications. These events include the following: All (events), InProgress, Success, TimedOut, Cancelled, Failed. To learn more about these events, see Setting Up Events and Notifications in the AWS Systems Manager User Guide .
            (string) --
            NotificationType (string) --Command: Receive notification when the status of a command changes. Invocation: For commands sent to multiple instances, receive notification on a per-instance basis when the status of a command changes.
            OutputS3BucketName (string) --The name of the Amazon S3 bucket.
            OutputS3KeyPrefix (string) --The Amazon S3 bucket subfolder.
            Parameters (dict) --The parameters for the RUN_COMMAND task execution.
            (string) --
            (list) --
            (string) --
            
            ServiceRoleArn (string) --The IAM service role to assume during task execution.
            TimeoutSeconds (integer) --If this time is reached and the command has not already started executing, it doesn not execute.
            Automation (dict) --The parameters for a AUTOMATION task type.
            DocumentVersion (string) --The version of an Automation document to use during task execution.
            Parameters (dict) --The parameters for the AUTOMATION task.
            (string) --
            (list) --
            (string) --
            
            
            StepFunctions (dict) --The parameters for a STEP_FUNCTION task type.
            Input (string) --The inputs for the STEP_FUNCTION task.
            Name (string) --The name of the STEP_FUNCTION task.
            Lambda (dict) --The parameters for a LAMBDA task type.
            ClientContext (string) --Pass client-specific information to the Lambda function that you are invoking. You can then process the client information in your Lambda function as you choose through the context variable.
            Qualifier (string) --(Optional) Specify a Lambda function version or alias name. If you specify a function version, the action uses the qualified function ARN to invoke a specific Lambda function. If you specify an alias name, the action uses the alias ARN to invoke the Lambda function version to which the alias points.
            Payload (bytes) --JSON to provide to your Lambda function as input.
            
            

    :type Priority: integer
    :param Priority: The priority of the task in the Maintenance Window, the lower the number the higher the priority. Tasks in a Maintenance Window are scheduled in priority order with tasks that have the same priority scheduled in parallel.

    :type MaxConcurrency: string
    :param MaxConcurrency: [REQUIRED]
            The maximum number of targets this task can be run for in parallel.
            

    :type MaxErrors: string
    :param MaxErrors: [REQUIRED]
            The maximum number of errors allowed before this task stops being scheduled.
            

    :type LoggingInfo: dict
    :param LoggingInfo: A structure containing information about an Amazon S3 bucket to write instance-level logs to.
            S3BucketName (string) -- [REQUIRED]The name of an Amazon S3 bucket where execution logs are stored .
            S3KeyPrefix (string) --(Optional) The Amazon S3 bucket subfolder.
            S3Region (string) -- [REQUIRED]The region where the Amazon S3 bucket is located.
            

    :type Name: string
    :param Name: An optional name for the task.

    :type Description: string
    :param Description: An optional description for the task.

    :type ClientToken: string
    :param ClientToken: User-provided idempotency token.
            This field is autopopulated if not provided.
            

    :rtype: dict
    :return: {
        'WindowTaskId': 'string'
    }
    
    
    """
    pass

def remove_tags_from_resource(ResourceType=None, ResourceId=None, TagKeys=None):
    """
    Removes all tags from the specified resource.
    See also: AWS API Documentation
    
    
    :example: response = client.remove_tags_from_resource(
        ResourceType='Document'|'ManagedInstance'|'MaintenanceWindow'|'Parameter'|'PatchBaseline',
        ResourceId='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceType: string
    :param ResourceType: [REQUIRED]
            The type of resource of which you want to remove a tag.
            

    :type ResourceId: string
    :param ResourceId: [REQUIRED]
            The resource ID for which you want to remove tags.
            

    :type TagKeys: list
    :param TagKeys: [REQUIRED]
            Tag keys that you want to remove from the specified resource.
            (string) --
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def send_automation_signal(AutomationExecutionId=None, SignalType=None, Payload=None):
    """
    Sends a signal to an Automation execution to change the current behavior or status of the execution.
    See also: AWS API Documentation
    
    
    :example: response = client.send_automation_signal(
        AutomationExecutionId='string',
        SignalType='Approve'|'Reject'|'StartStep'|'StopStep'|'Resume',
        Payload={
            'string': [
                'string',
            ]
        }
    )
    
    
    :type AutomationExecutionId: string
    :param AutomationExecutionId: [REQUIRED]
            The unique identifier for an existing Automation execution that you want to send the signal to.
            

    :type SignalType: string
    :param SignalType: [REQUIRED]
            The type of signal. Valid signal types include the following: Approve and Reject
            

    :type Payload: dict
    :param Payload: The data sent with the signal. The data schema depends on the type of signal used in the request.
            (string) --
            (list) --
            (string) --
            
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def send_command(InstanceIds=None, Targets=None, DocumentName=None, DocumentHash=None, DocumentHashType=None, TimeoutSeconds=None, Comment=None, Parameters=None, OutputS3Region=None, OutputS3BucketName=None, OutputS3KeyPrefix=None, MaxConcurrency=None, MaxErrors=None, ServiceRoleArn=None, NotificationConfig=None):
    """
    Executes commands on one or more managed instances.
    See also: AWS API Documentation
    
    
    :example: response = client.send_command(
        InstanceIds=[
            'string',
        ],
        Targets=[
            {
                'Key': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        DocumentName='string',
        DocumentHash='string',
        DocumentHashType='Sha256'|'Sha1',
        TimeoutSeconds=123,
        Comment='string',
        Parameters={
            'string': [
                'string',
            ]
        },
        OutputS3Region='string',
        OutputS3BucketName='string',
        OutputS3KeyPrefix='string',
        MaxConcurrency='string',
        MaxErrors='string',
        ServiceRoleArn='string',
        NotificationConfig={
            'NotificationArn': 'string',
            'NotificationEvents': [
                'All'|'InProgress'|'Success'|'TimedOut'|'Cancelled'|'Failed',
            ],
            'NotificationType': 'Command'|'Invocation'
        }
    )
    
    
    :type InstanceIds: list
    :param InstanceIds: The instance IDs where the command should execute. You can specify a maximum of 50 IDs. If you prefer not to list individual instance IDs, you can instead send commands to a fleet of instances using the Targets parameter, which accepts EC2 tags. For more information about how to use Targets, see Sending Commands to a Fleet .
            (string) --
            

    :type Targets: list
    :param Targets: (Optional) An array of search criteria that targets instances using a Key,Value combination that you specify. Targets is required if you don't provide one or more instance IDs in the call. For more information about how to use Targets, see Sending Commands to a Fleet .
            (dict) --An array of search criteria that targets instances using a Key,Value combination that you specify. Targets is required if you don't provide one or more instance IDs in the call.
            Key (string) --User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:Amazon EC2 tagor InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see Executing a Command Using Systems Manager Run Command .
            Values (list) --User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see Executing a Command Using Systems Manager Run Command .
            (string) --
            
            

    :type DocumentName: string
    :param DocumentName: [REQUIRED]
            Required. The name of the Systems Manager document to execute. This can be a public document or a custom document.
            

    :type DocumentHash: string
    :param DocumentHash: The Sha256 or Sha1 hash created by the system when the document was created.
            Note
            Sha1 hashes have been deprecated.
            

    :type DocumentHashType: string
    :param DocumentHashType: Sha256 or Sha1.
            Note
            Sha1 hashes have been deprecated.
            

    :type TimeoutSeconds: integer
    :param TimeoutSeconds: If this time is reached and the command has not already started executing, it will not execute.

    :type Comment: string
    :param Comment: User-specified information about the command, such as a brief description of what the command should do.

    :type Parameters: dict
    :param Parameters: The required and optional parameters specified in the document being executed.
            (string) --
            (list) --
            (string) --
            
            

    :type OutputS3Region: string
    :param OutputS3Region: (Deprecated) You can no longer specify this parameter. The system ignores it. Instead, Systems Manager automatically determines the Amazon S3 bucket region.

    :type OutputS3BucketName: string
    :param OutputS3BucketName: The name of the S3 bucket where command execution responses should be stored.

    :type OutputS3KeyPrefix: string
    :param OutputS3KeyPrefix: The directory structure within the S3 bucket where the responses should be stored.

    :type MaxConcurrency: string
    :param MaxConcurrency: (Optional) The maximum number of instances that are allowed to execute the command at the same time. You can specify a number such as 10 or a percentage such as 10%. The default value is 50. For more information about how to use MaxConcurrency, see Using Concurrency Controls .

    :type MaxErrors: string
    :param MaxErrors: The maximum number of errors allowed without the command failing. When the command fails one more time beyond the value of MaxErrors, the systems stops sending the command to additional targets. You can specify a number like 10 or a percentage like 10%. The default value is 0. For more information about how to use MaxErrors, see Using Error Controls .

    :type ServiceRoleArn: string
    :param ServiceRoleArn: The IAM role that Systems Manager uses to send notifications.

    :type NotificationConfig: dict
    :param NotificationConfig: Configurations for sending notifications.
            NotificationArn (string) --An Amazon Resource Name (ARN) for a Simple Notification Service (SNS) topic. Run Command pushes notifications about command status changes to this topic.
            NotificationEvents (list) --The different events for which you can receive notifications. These events include the following: All (events), InProgress, Success, TimedOut, Cancelled, Failed. To learn more about these events, see Setting Up Events and Notifications in the AWS Systems Manager User Guide .
            (string) --
            NotificationType (string) --Command: Receive notification when the status of a command changes. Invocation: For commands sent to multiple instances, receive notification on a per-instance basis when the status of a command changes.
            

    :rtype: dict
    :return: {
        'Command': {
            'CommandId': 'string',
            'DocumentName': 'string',
            'Comment': 'string',
            'ExpiresAfter': datetime(2015, 1, 1),
            'Parameters': {
                'string': [
                    'string',
                ]
            },
            'InstanceIds': [
                'string',
            ],
            'Targets': [
                {
                    'Key': 'string',
                    'Values': [
                        'string',
                    ]
                },
            ],
            'RequestedDateTime': datetime(2015, 1, 1),
            'Status': 'Pending'|'InProgress'|'Success'|'Cancelled'|'Failed'|'TimedOut'|'Cancelling',
            'StatusDetails': 'string',
            'OutputS3Region': 'string',
            'OutputS3BucketName': 'string',
            'OutputS3KeyPrefix': 'string',
            'MaxConcurrency': 'string',
            'MaxErrors': 'string',
            'TargetCount': 123,
            'CompletedCount': 123,
            'ErrorCount': 123,
            'ServiceRole': 'string',
            'NotificationConfig': {
                'NotificationArn': 'string',
                'NotificationEvents': [
                    'All'|'InProgress'|'Success'|'TimedOut'|'Cancelled'|'Failed',
                ],
                'NotificationType': 'Command'|'Invocation'
            }
        }
    }
    
    
    :returns: 
    (string) --
    (list) --
    (string) --
    
    
    
    
    
    """
    pass

def start_automation_execution(DocumentName=None, DocumentVersion=None, Parameters=None, ClientToken=None, Mode=None, TargetParameterName=None, Targets=None, MaxConcurrency=None, MaxErrors=None):
    """
    Initiates execution of an Automation document.
    See also: AWS API Documentation
    
    
    :example: response = client.start_automation_execution(
        DocumentName='string',
        DocumentVersion='string',
        Parameters={
            'string': [
                'string',
            ]
        },
        ClientToken='string',
        Mode='Auto'|'Interactive',
        TargetParameterName='string',
        Targets=[
            {
                'Key': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        MaxConcurrency='string',
        MaxErrors='string'
    )
    
    
    :type DocumentName: string
    :param DocumentName: [REQUIRED]
            The name of the Automation document to use for this execution.
            

    :type DocumentVersion: string
    :param DocumentVersion: The version of the Automation document to use for this execution.

    :type Parameters: dict
    :param Parameters: A key-value map of execution parameters, which match the declared parameters in the Automation document.
            (string) --
            (list) --
            (string) --
            
            

    :type ClientToken: string
    :param ClientToken: User-provided idempotency token. The token must be unique, is case insensitive, enforces the UUID format, and can't be reused.

    :type Mode: string
    :param Mode: The execution mode of the automation. Valid modes include the following: Auto and Interactive. The default mode is Auto.

    :type TargetParameterName: string
    :param TargetParameterName: The name of the parameter used as the target resource for the rate-controlled execution. Required if you specify Targets.

    :type Targets: list
    :param Targets: A key-value mapping to target resources. Required if you specify TargetParameterName.
            (dict) --An array of search criteria that targets instances using a Key,Value combination that you specify. Targets is required if you don't provide one or more instance IDs in the call.
            Key (string) --User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:Amazon EC2 tagor InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see Executing a Command Using Systems Manager Run Command .
            Values (list) --User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see Executing a Command Using Systems Manager Run Command .
            (string) --
            
            

    :type MaxConcurrency: string
    :param MaxConcurrency: The maximum number of targets allowed to run this task in parallel. You can specify a number, such as 10, or a percentage, such as 10%. The default value is 10.

    :type MaxErrors: string
    :param MaxErrors: The number of errors that are allowed before the system stops running the automation on additional targets. You can specify either an absolute number of errors, for example 10, or a percentage of the target set, for example 10%. If you specify 3, for example, the system stops running the automation when the fourth error is received. If you specify 0, then the system stops running the automation on additional targets after the first error result is returned. If you run an automation on 50 resources and set max-errors to 10%, then the system stops running the automation on additional targets when the sixth error is received.
            Executions that are already running an automation when max-errors is reached are allowed to complete, but some of these executions may fail as well. If you need to ensure that there won't be more than max-errors failed executions, set max-concurrency to 1 so the executions proceed one at a time.
            

    :rtype: dict
    :return: {
        'AutomationExecutionId': 'string'
    }
    
    
    """
    pass

def stop_automation_execution(AutomationExecutionId=None, Type=None):
    """
    Stop an Automation that is currently executing.
    See also: AWS API Documentation
    
    
    :example: response = client.stop_automation_execution(
        AutomationExecutionId='string',
        Type='Complete'|'Cancel'
    )
    
    
    :type AutomationExecutionId: string
    :param AutomationExecutionId: [REQUIRED]
            The execution ID of the Automation to stop.
            

    :type Type: string
    :param Type: The stop request type. Valid types include the following: Cancel and Complete. The default type is Cancel.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_association(AssociationId=None, Parameters=None, DocumentVersion=None, ScheduleExpression=None, OutputLocation=None, Name=None, Targets=None, AssociationName=None, AssociationVersion=None):
    """
    Updates an association. You can update the association name and version, the document version, schedule, parameters, and Amazon S3 output.
    See also: AWS API Documentation
    
    
    :example: response = client.update_association(
        AssociationId='string',
        Parameters={
            'string': [
                'string',
            ]
        },
        DocumentVersion='string',
        ScheduleExpression='string',
        OutputLocation={
            'S3Location': {
                'OutputS3Region': 'string',
                'OutputS3BucketName': 'string',
                'OutputS3KeyPrefix': 'string'
            }
        },
        Name='string',
        Targets=[
            {
                'Key': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        AssociationName='string',
        AssociationVersion='string'
    )
    
    
    :type AssociationId: string
    :param AssociationId: [REQUIRED]
            The ID of the association you want to update.
            

    :type Parameters: dict
    :param Parameters: The parameters you want to update for the association. If you create a parameter using Parameter Store, you can reference the parameter using {{ssm:parameter-name}}
            (string) --
            (list) --
            (string) --
            
            

    :type DocumentVersion: string
    :param DocumentVersion: The document version you want update for the association.

    :type ScheduleExpression: string
    :param ScheduleExpression: The cron expression used to schedule the association that you want to update.

    :type OutputLocation: dict
    :param OutputLocation: An Amazon S3 bucket where you want to store the results of this request.
            S3Location (dict) --An Amazon S3 bucket where you want to store the results of this request.
            OutputS3Region (string) --(Deprecated) You can no longer specify this parameter. The system ignores it. Instead, Systems Manager automatically determines the Amazon S3 bucket region.
            OutputS3BucketName (string) --The name of the Amazon S3 bucket.
            OutputS3KeyPrefix (string) --The Amazon S3 bucket subfolder.
            
            

    :type Name: string
    :param Name: The name of the association document.

    :type Targets: list
    :param Targets: The targets of the association.
            (dict) --An array of search criteria that targets instances using a Key,Value combination that you specify. Targets is required if you don't provide one or more instance IDs in the call.
            Key (string) --User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:Amazon EC2 tagor InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see Executing a Command Using Systems Manager Run Command .
            Values (list) --User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see Executing a Command Using Systems Manager Run Command .
            (string) --
            
            

    :type AssociationName: string
    :param AssociationName: The name of the association that you want to update.

    :type AssociationVersion: string
    :param AssociationVersion: This parameter is provided for concurrency control purposes. You must specify the latest association version in the service. If you want to ensure that this request succeeds, either specify $LATEST , or omit this parameter.

    :rtype: dict
    :return: {
        'AssociationDescription': {
            'Name': 'string',
            'InstanceId': 'string',
            'AssociationVersion': 'string',
            'Date': datetime(2015, 1, 1),
            'LastUpdateAssociationDate': datetime(2015, 1, 1),
            'Status': {
                'Date': datetime(2015, 1, 1),
                'Name': 'Pending'|'Success'|'Failed',
                'Message': 'string',
                'AdditionalInfo': 'string'
            },
            'Overview': {
                'Status': 'string',
                'DetailedStatus': 'string',
                'AssociationStatusAggregatedCount': {
                    'string': 123
                }
            },
            'DocumentVersion': 'string',
            'Parameters': {
                'string': [
                    'string',
                ]
            },
            'AssociationId': 'string',
            'Targets': [
                {
                    'Key': 'string',
                    'Values': [
                        'string',
                    ]
                },
            ],
            'ScheduleExpression': 'string',
            'OutputLocation': {
                'S3Location': {
                    'OutputS3Region': 'string',
                    'OutputS3BucketName': 'string',
                    'OutputS3KeyPrefix': 'string'
                }
            },
            'LastExecutionDate': datetime(2015, 1, 1),
            'LastSuccessfulExecutionDate': datetime(2015, 1, 1),
            'AssociationName': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (integer) --
    
    
    
    """
    pass

def update_association_status(Name=None, InstanceId=None, AssociationStatus=None):
    """
    Updates the status of the Systems Manager document associated with the specified instance.
    See also: AWS API Documentation
    
    
    :example: response = client.update_association_status(
        Name='string',
        InstanceId='string',
        AssociationStatus={
            'Date': datetime(2015, 1, 1),
            'Name': 'Pending'|'Success'|'Failed',
            'Message': 'string',
            'AdditionalInfo': 'string'
        }
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the Systems Manager document.
            

    :type InstanceId: string
    :param InstanceId: [REQUIRED]
            The ID of the instance.
            

    :type AssociationStatus: dict
    :param AssociationStatus: [REQUIRED]
            The association status.
            Date (datetime) -- [REQUIRED]The date when the status changed.
            Name (string) -- [REQUIRED]The status.
            Message (string) -- [REQUIRED]The reason for the status.
            AdditionalInfo (string) --A user-defined string.
            

    :rtype: dict
    :return: {
        'AssociationDescription': {
            'Name': 'string',
            'InstanceId': 'string',
            'AssociationVersion': 'string',
            'Date': datetime(2015, 1, 1),
            'LastUpdateAssociationDate': datetime(2015, 1, 1),
            'Status': {
                'Date': datetime(2015, 1, 1),
                'Name': 'Pending'|'Success'|'Failed',
                'Message': 'string',
                'AdditionalInfo': 'string'
            },
            'Overview': {
                'Status': 'string',
                'DetailedStatus': 'string',
                'AssociationStatusAggregatedCount': {
                    'string': 123
                }
            },
            'DocumentVersion': 'string',
            'Parameters': {
                'string': [
                    'string',
                ]
            },
            'AssociationId': 'string',
            'Targets': [
                {
                    'Key': 'string',
                    'Values': [
                        'string',
                    ]
                },
            ],
            'ScheduleExpression': 'string',
            'OutputLocation': {
                'S3Location': {
                    'OutputS3Region': 'string',
                    'OutputS3BucketName': 'string',
                    'OutputS3KeyPrefix': 'string'
                }
            },
            'LastExecutionDate': datetime(2015, 1, 1),
            'LastSuccessfulExecutionDate': datetime(2015, 1, 1),
            'AssociationName': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (integer) --
    
    
    
    """
    pass

def update_document(Content=None, Name=None, DocumentVersion=None, DocumentFormat=None, TargetType=None):
    """
    The document you want to update.
    See also: AWS API Documentation
    
    
    :example: response = client.update_document(
        Content='string',
        Name='string',
        DocumentVersion='string',
        DocumentFormat='YAML'|'JSON',
        TargetType='string'
    )
    
    
    :type Content: string
    :param Content: [REQUIRED]
            The content in a document that you want to update.
            

    :type Name: string
    :param Name: [REQUIRED]
            The name of the document that you want to update.
            

    :type DocumentVersion: string
    :param DocumentVersion: The version of the document that you want to update.

    :type DocumentFormat: string
    :param DocumentFormat: Specify the document format for the new document version. Systems Manager supports JSON and YAML documents. JSON is the default format.

    :type TargetType: string
    :param TargetType: Specify a new target type for the document.

    :rtype: dict
    :return: {
        'DocumentDescription': {
            'Sha1': 'string',
            'Hash': 'string',
            'HashType': 'Sha256'|'Sha1',
            'Name': 'string',
            'Owner': 'string',
            'CreatedDate': datetime(2015, 1, 1),
            'Status': 'Creating'|'Active'|'Updating'|'Deleting',
            'DocumentVersion': 'string',
            'Description': 'string',
            'Parameters': [
                {
                    'Name': 'string',
                    'Type': 'String'|'StringList',
                    'Description': 'string',
                    'DefaultValue': 'string'
                },
            ],
            'PlatformTypes': [
                'Windows'|'Linux',
            ],
            'DocumentType': 'Command'|'Policy'|'Automation',
            'SchemaVersion': 'string',
            'LatestVersion': 'string',
            'DefaultVersion': 'string',
            'DocumentFormat': 'YAML'|'JSON',
            'TargetType': 'string',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def update_document_default_version(Name=None, DocumentVersion=None):
    """
    Set the default version of a document.
    See also: AWS API Documentation
    
    
    :example: response = client.update_document_default_version(
        Name='string',
        DocumentVersion='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of a custom document that you want to set as the default version.
            

    :type DocumentVersion: string
    :param DocumentVersion: [REQUIRED]
            The version of a custom document that you want to set as the default version.
            

    :rtype: dict
    :return: {
        'Description': {
            'Name': 'string',
            'DefaultVersion': 'string'
        }
    }
    
    
    """
    pass

def update_maintenance_window(WindowId=None, Name=None, Description=None, Schedule=None, Duration=None, Cutoff=None, AllowUnassociatedTargets=None, Enabled=None, Replace=None):
    """
    Updates an existing Maintenance Window. Only specified parameters are modified.
    See also: AWS API Documentation
    
    
    :example: response = client.update_maintenance_window(
        WindowId='string',
        Name='string',
        Description='string',
        Schedule='string',
        Duration=123,
        Cutoff=123,
        AllowUnassociatedTargets=True|False,
        Enabled=True|False,
        Replace=True|False
    )
    
    
    :type WindowId: string
    :param WindowId: [REQUIRED]
            The ID of the Maintenance Window to update.
            

    :type Name: string
    :param Name: The name of the Maintenance Window.

    :type Description: string
    :param Description: An optional description for the update request.

    :type Schedule: string
    :param Schedule: The schedule of the Maintenance Window in the form of a cron or rate expression.

    :type Duration: integer
    :param Duration: The duration of the Maintenance Window in hours.

    :type Cutoff: integer
    :param Cutoff: The number of hours before the end of the Maintenance Window that Systems Manager stops scheduling new tasks for execution.

    :type AllowUnassociatedTargets: boolean
    :param AllowUnassociatedTargets: Whether targets must be registered with the Maintenance Window before tasks can be defined for those targets.

    :type Enabled: boolean
    :param Enabled: Whether the Maintenance Window is enabled.

    :type Replace: boolean
    :param Replace: If True, then all fields that are required by the CreateMaintenanceWindow action are also required for this API request. Optional fields that are not specified are set to null.

    :rtype: dict
    :return: {
        'WindowId': 'string',
        'Name': 'string',
        'Description': 'string',
        'Schedule': 'string',
        'Duration': 123,
        'Cutoff': 123,
        'AllowUnassociatedTargets': True|False,
        'Enabled': True|False
    }
    
    
    """
    pass

def update_maintenance_window_target(WindowId=None, WindowTargetId=None, Targets=None, OwnerInformation=None, Name=None, Description=None, Replace=None):
    """
    Modifies the target of an existing Maintenance Window. You can't change the target type, but you can change the following:
    The target from being an ID target to a Tag target, or a Tag target to an ID target.
    IDs for an ID target.
    Tags for a Tag target.
    Owner.
    Name.
    Description.
    If a parameter is null, then the corresponding field is not modified.
    See also: AWS API Documentation
    
    
    :example: response = client.update_maintenance_window_target(
        WindowId='string',
        WindowTargetId='string',
        Targets=[
            {
                'Key': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        OwnerInformation='string',
        Name='string',
        Description='string',
        Replace=True|False
    )
    
    
    :type WindowId: string
    :param WindowId: [REQUIRED]
            The Maintenance Window ID with which to modify the target.
            

    :type WindowTargetId: string
    :param WindowTargetId: [REQUIRED]
            The target ID to modify.
            

    :type Targets: list
    :param Targets: The targets to add or replace.
            (dict) --An array of search criteria that targets instances using a Key,Value combination that you specify. Targets is required if you don't provide one or more instance IDs in the call.
            Key (string) --User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:Amazon EC2 tagor InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see Executing a Command Using Systems Manager Run Command .
            Values (list) --User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see Executing a Command Using Systems Manager Run Command .
            (string) --
            
            

    :type OwnerInformation: string
    :param OwnerInformation: User-provided value that will be included in any CloudWatch events raised while running tasks for these targets in this Maintenance Window.

    :type Name: string
    :param Name: A name for the update.

    :type Description: string
    :param Description: An optional description for the update.

    :type Replace: boolean
    :param Replace: If True, then all fields that are required by the RegisterTargetWithMaintenanceWindow action are also required for this API request. Optional fields that are not specified are set to null.

    :rtype: dict
    :return: {
        'WindowId': 'string',
        'WindowTargetId': 'string',
        'Targets': [
            {
                'Key': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        'OwnerInformation': 'string',
        'Name': 'string',
        'Description': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def update_maintenance_window_task(WindowId=None, WindowTaskId=None, Targets=None, TaskArn=None, ServiceRoleArn=None, TaskParameters=None, TaskInvocationParameters=None, Priority=None, MaxConcurrency=None, MaxErrors=None, LoggingInfo=None, Name=None, Description=None, Replace=None):
    """
    Modifies a task assigned to a Maintenance Window. You can't change the task type, but you can change the following values:
    Task ARN. For example, you can change a RUN_COMMAND task from AWS-RunPowerShellScript to AWS-RunShellScript.
    Service role ARN.
    Task parameters.
    Task priority.
    Task MaxConcurrency and MaxErrors.
    Log location.
    If a parameter is null, then the corresponding field is not modified. Also, if you set Replace to true, then all fields required by the RegisterTaskWithMaintenanceWindow action are required for this request. Optional fields that aren't specified are set to null.
    See also: AWS API Documentation
    
    
    :example: response = client.update_maintenance_window_task(
        WindowId='string',
        WindowTaskId='string',
        Targets=[
            {
                'Key': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        TaskArn='string',
        ServiceRoleArn='string',
        TaskParameters={
            'string': {
                'Values': [
                    'string',
                ]
            }
        },
        TaskInvocationParameters={
            'RunCommand': {
                'Comment': 'string',
                'DocumentHash': 'string',
                'DocumentHashType': 'Sha256'|'Sha1',
                'NotificationConfig': {
                    'NotificationArn': 'string',
                    'NotificationEvents': [
                        'All'|'InProgress'|'Success'|'TimedOut'|'Cancelled'|'Failed',
                    ],
                    'NotificationType': 'Command'|'Invocation'
                },
                'OutputS3BucketName': 'string',
                'OutputS3KeyPrefix': 'string',
                'Parameters': {
                    'string': [
                        'string',
                    ]
                },
                'ServiceRoleArn': 'string',
                'TimeoutSeconds': 123
            },
            'Automation': {
                'DocumentVersion': 'string',
                'Parameters': {
                    'string': [
                        'string',
                    ]
                }
            },
            'StepFunctions': {
                'Input': 'string',
                'Name': 'string'
            },
            'Lambda': {
                'ClientContext': 'string',
                'Qualifier': 'string',
                'Payload': b'bytes'
            }
        },
        Priority=123,
        MaxConcurrency='string',
        MaxErrors='string',
        LoggingInfo={
            'S3BucketName': 'string',
            'S3KeyPrefix': 'string',
            'S3Region': 'string'
        },
        Name='string',
        Description='string',
        Replace=True|False
    )
    
    
    :type WindowId: string
    :param WindowId: [REQUIRED]
            The Maintenance Window ID that contains the task to modify.
            

    :type WindowTaskId: string
    :param WindowTaskId: [REQUIRED]
            The task ID to modify.
            

    :type Targets: list
    :param Targets: The targets (either instances or tags) to modify. Instances are specified using Key=instanceids,Values=instanceID_1,instanceID_2. Tags are specified using Key=tag_name,Values=tag_value.
            (dict) --An array of search criteria that targets instances using a Key,Value combination that you specify. Targets is required if you don't provide one or more instance IDs in the call.
            Key (string) --User-defined criteria for sending commands that target instances that meet the criteria. Key can be tag:Amazon EC2 tagor InstanceIds. For more information about how to send commands that target instances using Key,Value parameters, see Executing a Command Using Systems Manager Run Command .
            Values (list) --User-defined criteria that maps to Key. For example, if you specified tag:ServerRole, you could specify value:WebServer to execute a command on instances that include Amazon EC2 tags of ServerRole,WebServer. For more information about how to send commands that target instances using Key,Value parameters, see Executing a Command Using Systems Manager Run Command .
            (string) --
            
            

    :type TaskArn: string
    :param TaskArn: The task ARN to modify.

    :type ServiceRoleArn: string
    :param ServiceRoleArn: The IAM service role ARN to modify. The system assumes this role during task execution.

    :type TaskParameters: dict
    :param TaskParameters: The parameters to modify. The map has the following format:
            Key: string, between 1 and 255 characters
            Value: an array of strings, each string is between 1 and 255 characters
            (string) --
            (dict) --Defines the values for a task parameter.
            Values (list) --This field contains an array of 0 or more strings, each 1 to 255 characters in length.
            (string) --
            
            

    :type TaskInvocationParameters: dict
    :param TaskInvocationParameters: The parameters that the task should use during execution. Populate only the fields that match the task type. All other fields should be empty.
            RunCommand (dict) --The parameters for a RUN_COMMAND task type.
            Comment (string) --Information about the command(s) to execute.
            DocumentHash (string) --The SHA-256 or SHA-1 hash created by the system when the document was created. SHA-1 hashes have been deprecated.
            DocumentHashType (string) --SHA-256 or SHA-1. SHA-1 hashes have been deprecated.
            NotificationConfig (dict) --Configurations for sending notifications about command status changes on a per-instance basis.
            NotificationArn (string) --An Amazon Resource Name (ARN) for a Simple Notification Service (SNS) topic. Run Command pushes notifications about command status changes to this topic.
            NotificationEvents (list) --The different events for which you can receive notifications. These events include the following: All (events), InProgress, Success, TimedOut, Cancelled, Failed. To learn more about these events, see Setting Up Events and Notifications in the AWS Systems Manager User Guide .
            (string) --
            NotificationType (string) --Command: Receive notification when the status of a command changes. Invocation: For commands sent to multiple instances, receive notification on a per-instance basis when the status of a command changes.
            OutputS3BucketName (string) --The name of the Amazon S3 bucket.
            OutputS3KeyPrefix (string) --The Amazon S3 bucket subfolder.
            Parameters (dict) --The parameters for the RUN_COMMAND task execution.
            (string) --
            (list) --
            (string) --
            
            ServiceRoleArn (string) --The IAM service role to assume during task execution.
            TimeoutSeconds (integer) --If this time is reached and the command has not already started executing, it doesn not execute.
            Automation (dict) --The parameters for a AUTOMATION task type.
            DocumentVersion (string) --The version of an Automation document to use during task execution.
            Parameters (dict) --The parameters for the AUTOMATION task.
            (string) --
            (list) --
            (string) --
            
            
            StepFunctions (dict) --The parameters for a STEP_FUNCTION task type.
            Input (string) --The inputs for the STEP_FUNCTION task.
            Name (string) --The name of the STEP_FUNCTION task.
            Lambda (dict) --The parameters for a LAMBDA task type.
            ClientContext (string) --Pass client-specific information to the Lambda function that you are invoking. You can then process the client information in your Lambda function as you choose through the context variable.
            Qualifier (string) --(Optional) Specify a Lambda function version or alias name. If you specify a function version, the action uses the qualified function ARN to invoke a specific Lambda function. If you specify an alias name, the action uses the alias ARN to invoke the Lambda function version to which the alias points.
            Payload (bytes) --JSON to provide to your Lambda function as input.
            
            

    :type Priority: integer
    :param Priority: The new task priority to specify. The lower the number, the higher the priority. Tasks that have the same priority are scheduled in parallel.

    :type MaxConcurrency: string
    :param MaxConcurrency: The new MaxConcurrency value you want to specify. MaxConcurrency is the number of targets that are allowed to run this task in parallel.

    :type MaxErrors: string
    :param MaxErrors: The new MaxErrors value to specify. MaxErrors is the maximum number of errors that are allowed before the task stops being scheduled.

    :type LoggingInfo: dict
    :param LoggingInfo: The new logging location in Amazon S3 to specify.
            S3BucketName (string) -- [REQUIRED]The name of an Amazon S3 bucket where execution logs are stored .
            S3KeyPrefix (string) --(Optional) The Amazon S3 bucket subfolder.
            S3Region (string) -- [REQUIRED]The region where the Amazon S3 bucket is located.
            

    :type Name: string
    :param Name: The new task name to specify.

    :type Description: string
    :param Description: The new task description to specify.

    :type Replace: boolean
    :param Replace: If True, then all fields that are required by the RegisterTaskWithMaintenanceWndow action are also required for this API request. Optional fields that are not specified are set to null.

    :rtype: dict
    :return: {
        'WindowId': 'string',
        'WindowTaskId': 'string',
        'Targets': [
            {
                'Key': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        'TaskArn': 'string',
        'ServiceRoleArn': 'string',
        'TaskParameters': {
            'string': {
                'Values': [
                    'string',
                ]
            }
        },
        'TaskInvocationParameters': {
            'RunCommand': {
                'Comment': 'string',
                'DocumentHash': 'string',
                'DocumentHashType': 'Sha256'|'Sha1',
                'NotificationConfig': {
                    'NotificationArn': 'string',
                    'NotificationEvents': [
                        'All'|'InProgress'|'Success'|'TimedOut'|'Cancelled'|'Failed',
                    ],
                    'NotificationType': 'Command'|'Invocation'
                },
                'OutputS3BucketName': 'string',
                'OutputS3KeyPrefix': 'string',
                'Parameters': {
                    'string': [
                        'string',
                    ]
                },
                'ServiceRoleArn': 'string',
                'TimeoutSeconds': 123
            },
            'Automation': {
                'DocumentVersion': 'string',
                'Parameters': {
                    'string': [
                        'string',
                    ]
                }
            },
            'StepFunctions': {
                'Input': 'string',
                'Name': 'string'
            },
            'Lambda': {
                'ClientContext': 'string',
                'Qualifier': 'string',
                'Payload': b'bytes'
            }
        },
        'Priority': 123,
        'MaxConcurrency': 'string',
        'MaxErrors': 'string',
        'LoggingInfo': {
            'S3BucketName': 'string',
            'S3KeyPrefix': 'string',
            'S3Region': 'string'
        },
        'Name': 'string',
        'Description': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def update_managed_instance_role(InstanceId=None, IamRole=None):
    """
    Assigns or changes an Amazon Identity and Access Management (IAM) role to the managed instance.
    See also: AWS API Documentation
    
    
    :example: response = client.update_managed_instance_role(
        InstanceId='string',
        IamRole='string'
    )
    
    
    :type InstanceId: string
    :param InstanceId: [REQUIRED]
            The ID of the managed instance where you want to update the role.
            

    :type IamRole: string
    :param IamRole: [REQUIRED]
            The IAM role you want to assign or change.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_patch_baseline(BaselineId=None, Name=None, GlobalFilters=None, ApprovalRules=None, ApprovedPatches=None, ApprovedPatchesComplianceLevel=None, ApprovedPatchesEnableNonSecurity=None, RejectedPatches=None, Description=None, Sources=None, Replace=None):
    """
    Modifies an existing patch baseline. Fields not specified in the request are left unchanged.
    See also: AWS API Documentation
    
    
    :example: response = client.update_patch_baseline(
        BaselineId='string',
        Name='string',
        GlobalFilters={
            'PatchFilters': [
                {
                    'Key': 'PRODUCT'|'CLASSIFICATION'|'MSRC_SEVERITY'|'PATCH_ID'|'SECTION'|'PRIORITY'|'SEVERITY',
                    'Values': [
                        'string',
                    ]
                },
            ]
        },
        ApprovalRules={
            'PatchRules': [
                {
                    'PatchFilterGroup': {
                        'PatchFilters': [
                            {
                                'Key': 'PRODUCT'|'CLASSIFICATION'|'MSRC_SEVERITY'|'PATCH_ID'|'SECTION'|'PRIORITY'|'SEVERITY',
                                'Values': [
                                    'string',
                                ]
                            },
                        ]
                    },
                    'ComplianceLevel': 'CRITICAL'|'HIGH'|'MEDIUM'|'LOW'|'INFORMATIONAL'|'UNSPECIFIED',
                    'ApproveAfterDays': 123,
                    'EnableNonSecurity': True|False
                },
            ]
        },
        ApprovedPatches=[
            'string',
        ],
        ApprovedPatchesComplianceLevel='CRITICAL'|'HIGH'|'MEDIUM'|'LOW'|'INFORMATIONAL'|'UNSPECIFIED',
        ApprovedPatchesEnableNonSecurity=True|False,
        RejectedPatches=[
            'string',
        ],
        Description='string',
        Sources=[
            {
                'Name': 'string',
                'Products': [
                    'string',
                ],
                'Configuration': 'string'
            },
        ],
        Replace=True|False
    )
    
    
    :type BaselineId: string
    :param BaselineId: [REQUIRED]
            The ID of the patch baseline to update.
            

    :type Name: string
    :param Name: The name of the patch baseline.

    :type GlobalFilters: dict
    :param GlobalFilters: A set of global filters used to exclude patches from the baseline.
            PatchFilters (list) -- [REQUIRED]The set of patch filters that make up the group.
            (dict) --Defines a patch filter.
            A patch filter consists of key/value pairs, but not all keys are valid for all operating system types. For example, the key PRODUCT is valid for all supported operating system types. The key MSRC_SEVERITY , however, is valid only for Windows operating systems, and the key SECTION is valid only for Ubuntu operating systems.
            Refer to the following sections for information about which keys may be used with each major operating system, and which values are valid for each key.
            Windows Operating Systems
            The supported keys for Windows operating systems are PRODUCT , CLASSIFICATION , and MSRC_SEVERITY . See the following lists for valid values for each of these keys.
            Supported key: PRODUCTSupported values:
            Windows7
            Windows8
            Windows8.1
            Windows8Embedded
            Windows10
            Windows10LTSB
            WindowsServer2008
            WindowsServer2008R2
            WindowsServer2012
            WindowsServer2012R2
            WindowsServer2016
            Supported key: CLASSIFICATIONSupported values:
            CriticalUpdates
            DefinitionUpdates
            Drivers
            FeaturePacks
            SecurityUpdates
            ServicePacks
            Tools
            UpdateRollups
            Updates
            Upgrades
            Supported key: MSRC_SEVERITYSupported values:
            Critical
            Important
            Moderate
            Low
            Unspecified
            Ubuntu Operating Systems
            The supported keys for Ubuntu operating systems are PRODUCT , PRIORITY , and SECTION . See the following lists for valid values for each of these keys.
            Supported key: PRODUCTSupported values:
            Ubuntu14.04
            Ubuntu16.04
            Supported key: PRIORITYSupported values:
            Required
            Important
            Standard
            Optional
            Extra
            Supported key: SECTION
            Only the length of the key value is validated. Minimum length is 1. Maximum length is 64.
            Amazon Linux Operating Systems
            The supported keys for Amazon Linux operating systems are PRODUCT , CLASSIFICATION , and SEVERITY . See the following lists for valid values for each of these keys.
            Supported key: PRODUCTSupported values:
            AmazonLinux2012.03
            AmazonLinux2012.09
            AmazonLinux2013.03
            AmazonLinux2013.09
            AmazonLinux2014.03
            AmazonLinux2014.09
            AmazonLinux2015.03
            AmazonLinux2015.09
            AmazonLinux2016.03
            AmazonLinux2016.09
            AmazonLinux2017.03
            AmazonLinux2017.09
            Supported key: CLASSIFICATIONSupported values:
            Security
            Bugfix
            Enhancement
            Recommended
            Newpackage
            Supported key: SEVERITYSupported values:
            Critical
            Important
            Medium
            Low
            RedHat Enterprise Linux (RHEL) Operating Systems
            The supported keys for RedHat Enterprise Linux operating systems are PRODUCT , CLASSIFICATION , and SEVERITY . See the following lists for valid values for each of these keys.
            Supported key: PRODUCTSupported values:
            RedhatEnterpriseLinux6.5
            RedhatEnterpriseLinux6.6
            RedhatEnterpriseLinux6.7
            RedhatEnterpriseLinux6.8
            RedhatEnterpriseLinux6.9
            RedhatEnterpriseLinux7.0
            RedhatEnterpriseLinux7.1
            RedhatEnterpriseLinux7.2
            RedhatEnterpriseLinux7.3
            RedhatEnterpriseLinux7.4
            Supported key: CLASSIFICATIONSupported values:
            Security
            Bugfix
            Enhancement
            Recommended
            Newpackage
            Supported key: SEVERITYSupported values:
            Critical
            Important
            Medium
            Low
            SUSE Linux Enterprise Server (SUSE) Operating Systems
            The supported keys for SUSE operating systems are PRODUCT , CLASSIFICATION , and SEVERITY . See the following lists for valid values for each of these keys.
            Supported key: PRODUCTSupported values:
            Suse12.0
            Suse12.1
            Suse12.2
            Suse12.3
            Suse12.4
            Suse12.5
            Suse12.6
            Suse12.7
            Suse12.8
            Suse12.9
            Supported key: CLASSIFICATIONSupported values:
            Security
            Recommended
            Optional
            Feature
            Document
            Yast
            Supported key: SEVERITYSupported values:
            Critical
            Important
            Moderate
            Low
            Key (string) -- [REQUIRED]The key for the filter.
            See PatchFilter for lists of valid keys for each operating system type.
            Values (list) -- [REQUIRED]The value for the filter key.
            See PatchFilter for lists of valid values for each key based on operating system type.
            (string) --
            
            

    :type ApprovalRules: dict
    :param ApprovalRules: A set of rules used to include patches in the baseline.
            PatchRules (list) -- [REQUIRED]The rules that make up the rule group.
            (dict) --Defines an approval rule for a patch baseline.
            PatchFilterGroup (dict) -- [REQUIRED]The patch filter group that defines the criteria for the rule.
            PatchFilters (list) -- [REQUIRED]The set of patch filters that make up the group.
            (dict) --Defines a patch filter.
            A patch filter consists of key/value pairs, but not all keys are valid for all operating system types. For example, the key PRODUCT is valid for all supported operating system types. The key MSRC_SEVERITY , however, is valid only for Windows operating systems, and the key SECTION is valid only for Ubuntu operating systems.
            Refer to the following sections for information about which keys may be used with each major operating system, and which values are valid for each key.
            Windows Operating Systems
            The supported keys for Windows operating systems are PRODUCT , CLASSIFICATION , and MSRC_SEVERITY . See the following lists for valid values for each of these keys.
            Supported key: PRODUCTSupported values:
            Windows7
            Windows8
            Windows8.1
            Windows8Embedded
            Windows10
            Windows10LTSB
            WindowsServer2008
            WindowsServer2008R2
            WindowsServer2012
            WindowsServer2012R2
            WindowsServer2016
            Supported key: CLASSIFICATIONSupported values:
            CriticalUpdates
            DefinitionUpdates
            Drivers
            FeaturePacks
            SecurityUpdates
            ServicePacks
            Tools
            UpdateRollups
            Updates
            Upgrades
            Supported key: MSRC_SEVERITYSupported values:
            Critical
            Important
            Moderate
            Low
            Unspecified
            Ubuntu Operating Systems
            The supported keys for Ubuntu operating systems are PRODUCT , PRIORITY , and SECTION . See the following lists for valid values for each of these keys.
            Supported key: PRODUCTSupported values:
            Ubuntu14.04
            Ubuntu16.04
            Supported key: PRIORITYSupported values:
            Required
            Important
            Standard
            Optional
            Extra
            Supported key: SECTION
            Only the length of the key value is validated. Minimum length is 1. Maximum length is 64.
            Amazon Linux Operating Systems
            The supported keys for Amazon Linux operating systems are PRODUCT , CLASSIFICATION , and SEVERITY . See the following lists for valid values for each of these keys.
            Supported key: PRODUCTSupported values:
            AmazonLinux2012.03
            AmazonLinux2012.09
            AmazonLinux2013.03
            AmazonLinux2013.09
            AmazonLinux2014.03
            AmazonLinux2014.09
            AmazonLinux2015.03
            AmazonLinux2015.09
            AmazonLinux2016.03
            AmazonLinux2016.09
            AmazonLinux2017.03
            AmazonLinux2017.09
            Supported key: CLASSIFICATIONSupported values:
            Security
            Bugfix
            Enhancement
            Recommended
            Newpackage
            Supported key: SEVERITYSupported values:
            Critical
            Important
            Medium
            Low
            RedHat Enterprise Linux (RHEL) Operating Systems
            The supported keys for RedHat Enterprise Linux operating systems are PRODUCT , CLASSIFICATION , and SEVERITY . See the following lists for valid values for each of these keys.
            Supported key: PRODUCTSupported values:
            RedhatEnterpriseLinux6.5
            RedhatEnterpriseLinux6.6
            RedhatEnterpriseLinux6.7
            RedhatEnterpriseLinux6.8
            RedhatEnterpriseLinux6.9
            RedhatEnterpriseLinux7.0
            RedhatEnterpriseLinux7.1
            RedhatEnterpriseLinux7.2
            RedhatEnterpriseLinux7.3
            RedhatEnterpriseLinux7.4
            Supported key: CLASSIFICATIONSupported values:
            Security
            Bugfix
            Enhancement
            Recommended
            Newpackage
            Supported key: SEVERITYSupported values:
            Critical
            Important
            Medium
            Low
            SUSE Linux Enterprise Server (SUSE) Operating Systems
            The supported keys for SUSE operating systems are PRODUCT , CLASSIFICATION , and SEVERITY . See the following lists for valid values for each of these keys.
            Supported key: PRODUCTSupported values:
            Suse12.0
            Suse12.1
            Suse12.2
            Suse12.3
            Suse12.4
            Suse12.5
            Suse12.6
            Suse12.7
            Suse12.8
            Suse12.9
            Supported key: CLASSIFICATIONSupported values:
            Security
            Recommended
            Optional
            Feature
            Document
            Yast
            Supported key: SEVERITYSupported values:
            Critical
            Important
            Moderate
            Low
            Key (string) -- [REQUIRED]The key for the filter.
            See PatchFilter for lists of valid keys for each operating system type.
            Values (list) -- [REQUIRED]The value for the filter key.
            See PatchFilter for lists of valid values for each key based on operating system type.
            (string) --
            
            
            ComplianceLevel (string) --A compliance severity level for all approved patches in a patch baseline. Valid compliance severity levels include the following: Unspecified, Critical, High, Medium, Low, and Informational.
            ApproveAfterDays (integer) -- [REQUIRED]The number of days after the release date of each patch matched by the rule the patch is marked as approved in the patch baseline.
            EnableNonSecurity (boolean) --For instances identified by the approval rule filters, enables a patch baseline to apply non-security updates available in the specified repository. The default value is 'false'. Applies to Linux instances only.
            
            

    :type ApprovedPatches: list
    :param ApprovedPatches: A list of explicitly approved patches for the baseline.
            (string) --
            

    :type ApprovedPatchesComplianceLevel: string
    :param ApprovedPatchesComplianceLevel: Assigns a new compliance severity level to an existing patch baseline.

    :type ApprovedPatchesEnableNonSecurity: boolean
    :param ApprovedPatchesEnableNonSecurity: Indicates whether the list of approved patches includes non-security updates that should be applied to the instances. The default value is 'false'. Applies to Linux instances only.

    :type RejectedPatches: list
    :param RejectedPatches: A list of explicitly rejected patches for the baseline.
            (string) --
            

    :type Description: string
    :param Description: A description of the patch baseline.

    :type Sources: list
    :param Sources: Information about the patches to use to update the instances, including target operating systems and source repositories. Applies to Linux instances only.
            (dict) --Information about the patches to use to update the instances, including target operating systems and source repository. Applies to Linux instances only.
            Name (string) -- [REQUIRED]The name specified to identify the patch source.
            Products (list) -- [REQUIRED]The specific operating system versions a patch repository applies to, such as 'Ubuntu16.04', 'AmazonLinux2016.09', 'RedhatEnterpriseLinux7.2' or 'Suse12.7'. For lists of supported product values, see PatchFilter .
            (string) --
            Configuration (string) -- [REQUIRED]The value of the yum repo configuration. For example:
            cachedir=/var/cache/yum/$basesearch$releasever
            keepcache=0
            debualevel=2
            
            

    :type Replace: boolean
    :param Replace: If True, then all fields that are required by the CreatePatchBaseline action are also required for this API request. Optional fields that are not specified are set to null.

    :rtype: dict
    :return: {
        'BaselineId': 'string',
        'Name': 'string',
        'OperatingSystem': 'WINDOWS'|'AMAZON_LINUX'|'UBUNTU'|'REDHAT_ENTERPRISE_LINUX'|'SUSE'|'CENTOS',
        'GlobalFilters': {
            'PatchFilters': [
                {
                    'Key': 'PRODUCT'|'CLASSIFICATION'|'MSRC_SEVERITY'|'PATCH_ID'|'SECTION'|'PRIORITY'|'SEVERITY',
                    'Values': [
                        'string',
                    ]
                },
            ]
        },
        'ApprovalRules': {
            'PatchRules': [
                {
                    'PatchFilterGroup': {
                        'PatchFilters': [
                            {
                                'Key': 'PRODUCT'|'CLASSIFICATION'|'MSRC_SEVERITY'|'PATCH_ID'|'SECTION'|'PRIORITY'|'SEVERITY',
                                'Values': [
                                    'string',
                                ]
                            },
                        ]
                    },
                    'ComplianceLevel': 'CRITICAL'|'HIGH'|'MEDIUM'|'LOW'|'INFORMATIONAL'|'UNSPECIFIED',
                    'ApproveAfterDays': 123,
                    'EnableNonSecurity': True|False
                },
            ]
        },
        'ApprovedPatches': [
            'string',
        ],
        'ApprovedPatchesComplianceLevel': 'CRITICAL'|'HIGH'|'MEDIUM'|'LOW'|'INFORMATIONAL'|'UNSPECIFIED',
        'ApprovedPatchesEnableNonSecurity': True|False,
        'RejectedPatches': [
            'string',
        ],
        'CreatedDate': datetime(2015, 1, 1),
        'ModifiedDate': datetime(2015, 1, 1),
        'Description': 'string',
        'Sources': [
            {
                'Name': 'string',
                'Products': [
                    'string',
                ],
                'Configuration': 'string'
            },
        ]
    }
    
    
    :returns: 
    Windows7
    Windows8
    Windows8.1
    Windows8Embedded
    Windows10
    Windows10LTSB
    WindowsServer2008
    WindowsServer2008R2
    WindowsServer2012
    WindowsServer2012R2
    WindowsServer2016
    
    """
    pass

