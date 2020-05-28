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
    Adds or overwrites one or more tags for the specified resource. Tags are metadata that you can assign to your documents, managed instances, maintenance windows, Parameter Store parameters, and patch baselines. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment. Each tag consists of a key and an optional value, both of which you define. For example, you could define a set of tags for your account\'s managed instances that helps you track each instance\'s owner and stack level. For example: Key=Owner and Value=DbAdmin, SysAdmin, or Dev. Or Key=Stack and Value=Production, Pre-Production, or Test.
    Each resource can have a maximum of 50 tags.
    We recommend that you devise a set of tag keys that meets your needs for each resource type. Using a consistent set of tag keys makes it easier for you to manage your resources. You can search and filter the resources based on the tags you add. Tags don\'t have any semantic meaning to and are interpreted strictly as a string of characters.
    For more information about using tags with EC2 instances, see Tagging your Amazon EC2 resources in the Amazon EC2 User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.add_tags_to_resource(
        ResourceType='Document'|'ManagedInstance'|'MaintenanceWindow'|'Parameter'|'PatchBaseline'|'OpsItem',
        ResourceId='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ResourceType: string
    :param ResourceType: [REQUIRED]\nSpecifies the type of resource you are tagging.\n\nNote\nThe ManagedInstance type for this API action is for on-premises managed instances. You must specify the name of the managed instance in the following format: mi-ID_number. For example, mi-1a2b3c4d5e6f.\n\n

    :type ResourceId: string
    :param ResourceId: [REQUIRED]\nThe resource ID you want to tag.\nUse the ID of the resource. Here are some examples:\nManagedInstance: mi-012345abcde\nMaintenanceWindow: mw-012345abcde\nPatchBaseline: pb-012345abcde\nFor the Document and Parameter values, use the name of the resource.\n\nNote\nThe ManagedInstance type for this API action is only for on-premises managed instances. You must specify the name of the managed instance in the following format: mi-ID_number. For example, mi-1a2b3c4d5e6f.\n\n

    :type Tags: list
    :param Tags: [REQUIRED]\nOne or more tags. The value parameter is required, but if you don\'t want the tag to have a value, specify the parameter with no value, and we set the value to an empty string.\n\nWarning\nDo not enter personally identifiable information in this field.\n\n\n(dict) --Metadata that you assign to your AWS resources. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment. In Systems Manager, you can apply tags to documents, managed instances, maintenance windows, Parameter Store parameters, and patch baselines.\n\nKey (string) -- [REQUIRED]The name of the tag.\n\nValue (string) -- [REQUIRED]The value of the tag.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

SSM.Client.exceptions.InvalidResourceType
SSM.Client.exceptions.InvalidResourceId
SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.TooManyTagsError
SSM.Client.exceptions.TooManyUpdates


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def cancel_command(CommandId=None, InstanceIds=None):
    """
    Attempts to cancel the command specified by the Command ID. There is no guarantee that the command will be terminated and the underlying process stopped.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.cancel_command(
        CommandId='string',
        InstanceIds=[
            'string',
        ]
    )
    
    
    :type CommandId: string
    :param CommandId: [REQUIRED]\nThe ID of the command you want to cancel.\n

    :type InstanceIds: list
    :param InstanceIds: (Optional) A list of instance IDs on which you want to cancel the command. If not provided, the command is canceled on every instance on which it was requested.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
Whether or not the command was successfully canceled. There is no guarantee that a request can be canceled.





Exceptions

SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.InvalidCommandId
SSM.Client.exceptions.InvalidInstanceId
SSM.Client.exceptions.DuplicateInstanceId


    :return: {}
    
    
    :returns: 
    SSM.Client.exceptions.InternalServerError
    SSM.Client.exceptions.InvalidCommandId
    SSM.Client.exceptions.InvalidInstanceId
    SSM.Client.exceptions.DuplicateInstanceId
    
    """
    pass

def cancel_maintenance_window_execution(WindowExecutionId=None):
    """
    Stops a maintenance window execution that is already in progress and cancels any tasks in the window that have not already starting running. (Tasks already in progress will continue to completion.)
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.cancel_maintenance_window_execution(
        WindowExecutionId='string'
    )
    
    
    :type WindowExecutionId: string
    :param WindowExecutionId: [REQUIRED]\nThe ID of the maintenance window execution to stop.\n

    :rtype: dict
ReturnsResponse Syntax{
    'WindowExecutionId': 'string'
}


Response Structure

(dict) --
WindowExecutionId (string) --The ID of the maintenance window execution that has been stopped.






Exceptions

SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.DoesNotExistException


    :return: {
        'WindowExecutionId': 'string'
    }
    
    
    """
    pass

def create_activation(Description=None, DefaultInstanceName=None, IamRole=None, RegistrationLimit=None, ExpirationDate=None, Tags=None):
    """
    Generates an activation code and activation ID you can use to register your on-premises server or virtual machine (VM) with Systems Manager. Registering these machines with Systems Manager makes it possible to manage them using Systems Manager capabilities. You use the activation code and ID when installing SSM Agent on machines in your hybrid environment. For more information about requirements for managing on-premises instances and VMs using Systems Manager, see Setting up AWS Systems Manager for hybrid environments in the AWS Systems Manager User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_activation(
        Description='string',
        DefaultInstanceName='string',
        IamRole='string',
        RegistrationLimit=123,
        ExpirationDate=datetime(2015, 1, 1),
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type Description: string
    :param Description: A user-defined description of the resource that you want to register with Systems Manager.\n\nWarning\nDo not enter personally identifiable information in this field.\n\n

    :type DefaultInstanceName: string
    :param DefaultInstanceName: The name of the registered, managed instance as it will appear in the Systems Manager console or when you use the AWS command line tools to list Systems Manager resources.\n\nWarning\nDo not enter personally identifiable information in this field.\n\n

    :type IamRole: string
    :param IamRole: [REQUIRED]\nThe Amazon Identity and Access Management (IAM) role that you want to assign to the managed instance. This IAM role must provide AssumeRole permissions for the Systems Manager service principal ssm.amazonaws.com . For more information, see Create an IAM service role for a hybrid environment in the AWS Systems Manager User Guide .\n

    :type RegistrationLimit: integer
    :param RegistrationLimit: Specify the maximum number of managed instances you want to register. The default value is 1 instance.

    :type ExpirationDate: datetime
    :param ExpirationDate: The date by which this activation request should expire. The default value is 24 hours.

    :type Tags: list
    :param Tags: Optional metadata that you assign to a resource. Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For example, you might want to tag an activation to identify which servers or virtual machines (VMs) in your on-premises environment you intend to activate. In this case, you could specify the following key name/value pairs:\n\nKey=OS,Value=Windows\nKey=Environment,Value=Production\n\n\nWarning\nWhen you install SSM Agent on your on-premises servers and VMs, you specify an activation ID and code. When you specify the activation ID and code, tags assigned to the activation are automatically applied to the on-premises servers or VMs.\n\nYou can\'t add tags to or delete tags from an existing activation. You can tag your on-premises servers and VMs after they connect to Systems Manager for the first time and are assigned a managed instance ID. This means they are listed in the AWS Systems Manager console with an ID that is prefixed with 'mi-'. For information about how to add tags to your managed instances, see AddTagsToResource . For information about how to remove tags from your managed instances, see RemoveTagsFromResource .\n\n(dict) --Metadata that you assign to your AWS resources. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment. In Systems Manager, you can apply tags to documents, managed instances, maintenance windows, Parameter Store parameters, and patch baselines.\n\nKey (string) -- [REQUIRED]The name of the tag.\n\nValue (string) -- [REQUIRED]The value of the tag.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ActivationId': 'string',
    'ActivationCode': 'string'
}


Response Structure

(dict) --

ActivationId (string) --
The ID number generated by the system when it processed the activation. The activation ID functions like a user name.

ActivationCode (string) --
The code the system generates when it processes the activation. The activation code functions like a password to validate the activation ID.







Exceptions

SSM.Client.exceptions.InternalServerError


    :return: {
        'ActivationId': 'string',
        'ActivationCode': 'string'
    }
    
    
    :returns: 
    SSM.Client.exceptions.InternalServerError
    
    """
    pass

def create_association(Name=None, DocumentVersion=None, InstanceId=None, Parameters=None, Targets=None, ScheduleExpression=None, OutputLocation=None, AssociationName=None, AutomationTargetParameterName=None, MaxErrors=None, MaxConcurrency=None, ComplianceSeverity=None, SyncCompliance=None):
    """
    Associates the specified Systems Manager document with the specified instances or targets.
    When you associate a document with one or more instances, SSM Agent running on the instance processes the document and configures the instance as specified. If you associate a document with an instance that already has an associated document, the system returns the AssociationAlreadyExists exception.
    See also: AWS API Documentation
    
    Exceptions
    
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
        AssociationName='string',
        AutomationTargetParameterName='string',
        MaxErrors='string',
        MaxConcurrency='string',
        ComplianceSeverity='CRITICAL'|'HIGH'|'MEDIUM'|'LOW'|'UNSPECIFIED',
        SyncCompliance='AUTO'|'MANUAL'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the SSM document that contains the configuration information for the instance. You can specify Command or Automation documents.\nYou can specify AWS-predefined documents, documents you created, or a document that is shared with you from another account.\nFor SSM documents that are shared with you from other AWS accounts, you must specify the complete SSM document ARN, in the following format:\n\n``arn:partition :ssm:region :account-id :document/document-name ``\nFor example:\n\narn:aws:ssm:us-east-2:12345678912:document/My-Shared-Document\nFor AWS-predefined documents and SSM documents you created in your account, you only need to specify the document name. For example, AWS-ApplyPatchBaseline or My-Document .\n

    :type DocumentVersion: string
    :param DocumentVersion: The document version you want to associate with the target(s). Can be a specific version or the default version.

    :type InstanceId: string
    :param InstanceId: The instance ID.\n\nNote\nInstanceId has been deprecated. To specify an instance ID for an association, use the Targets parameter. Requests that include the parameter InstanceID with SSM documents that use schema version 2.0 or later will fail. In addition, if you use the parameter InstanceId , you cannot use the parameters AssociationName , DocumentVersion , MaxErrors , MaxConcurrency , OutputLocation , or ScheduleExpression . To use these parameters, you must use the Targets parameter.\n\n

    :type Parameters: dict
    :param Parameters: The parameters for the runtime configuration of the document.\n\n(string) --\n(list) --\n(string) --\n\n\n\n\n\n

    :type Targets: list
    :param Targets: The targets for the association. You can target instances by using tags, AWS Resource Groups, all instances in an AWS account, or individual instance IDs. For more information about choosing targets for an association, see Using targets and rate controls with State Manager associations in the AWS Systems Manager User Guide .\n\n(dict) --An array of search criteria that targets instances using a Key,Value combination that you specify.\nSupported formats include the following.\n\n``Key=InstanceIds,Values=*instance-id-1* ,*instance-id-2* ,*instance-id-3* ``\n``Key=tag:my-tag-key ,Values=*my-tag-value-1* ,*my-tag-value-2* ``\n``Key=tag-key,Values=*my-tag-key-1* ,*my-tag-key-2* ``\n(Maintenance window targets only) ``Key=resource-groups:Name,Values=*resource-group-name* ``\n(Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*resource-type-1* ,*resource-type-2* ``\n\nFor example:\n\nKey=InstanceIds,Values=i-02573cafcfEXAMPLE,i-0471e04240EXAMPLE,i-07782c72faEXAMPLE\nKey=tag:CostCenter,Values=CostCenter1,CostCenter2,CostCenter3\nKey=tag-key,Values=Name,Instance-Type,CostCenter\n(Maintenance window targets only) Key=resource-groups:Name,Values=ProductionResourceGroup  This example demonstrates how to target all resources in the resource group ProductionResourceGroup in your maintenance window.\n(Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*AWS::EC2::INSTANCE* ,*AWS::EC2::VPC* ``  This example demonstrates how to target only EC2 instances and VPCs in your maintenance window.\n(State Manager association targets only) Key=InstanceIds,Values=*  This example demonstrates how to target all managed instances in the AWS Region where the association was created.\n\nFor information about how to send commands that target instances using Key,Value parameters, see Targeting multiple instances in the AWS Systems Manager User Guide .\n\nKey (string) --User-defined criteria for sending commands that target instances that meet the criteria.\n\nValues (list) --User-defined criteria that maps to Key . For example, if you specified tag:ServerRole , you could specify value:WebServer to run a command on instances that include EC2 tags of ServerRole,WebServer .\n\n(string) --\n\n\n\n\n\n

    :type ScheduleExpression: string
    :param ScheduleExpression: A cron expression when the association will be applied to the target(s).

    :type OutputLocation: dict
    :param OutputLocation: An S3 bucket where you want to store the output details of the request.\n\nS3Location (dict) --An S3 bucket where you want to store the results of this request.\n\nOutputS3Region (string) --(Deprecated) You can no longer specify this parameter. The system ignores it. Instead, Systems Manager automatically determines the Region of the S3 bucket.\n\nOutputS3BucketName (string) --The name of the S3 bucket.\n\nOutputS3KeyPrefix (string) --The S3 bucket subfolder.\n\n\n\n\n

    :type AssociationName: string
    :param AssociationName: Specify a descriptive name for the association.

    :type AutomationTargetParameterName: string
    :param AutomationTargetParameterName: Specify the target for the association. This target is required for associations that use an Automation document and target resources by using rate controls.

    :type MaxErrors: string
    :param MaxErrors: The number of errors that are allowed before the system stops sending requests to run the association on additional targets. You can specify either an absolute number of errors, for example 10, or a percentage of the target set, for example 10%. If you specify 3, for example, the system stops sending requests when the fourth error is received. If you specify 0, then the system stops sending requests after the first error is returned. If you run an association on 50 instances and set MaxError to 10%, then the system stops sending the request when the sixth error is received.\nExecutions that are already running an association when MaxErrors is reached are allowed to complete, but some of these executions may fail as well. If you need to ensure that there won\'t be more than max-errors failed executions, set MaxConcurrency to 1 so that executions proceed one at a time.\n

    :type MaxConcurrency: string
    :param MaxConcurrency: The maximum number of targets allowed to run the association at the same time. You can specify a number, for example 10, or a percentage of the target set, for example 10%. The default value is 100%, which means all targets run the association at the same time.\nIf a new instance starts and attempts to run an association while Systems Manager is running MaxConcurrency associations, the association is allowed to run. During the next association interval, the new instance will process its association within the limit specified for MaxConcurrency.\n

    :type ComplianceSeverity: string
    :param ComplianceSeverity: The severity level to assign to the association.

    :type SyncCompliance: string
    :param SyncCompliance: The mode for generating association compliance. You can specify AUTO or MANUAL . In AUTO mode, the system uses the status of the association execution to determine the compliance status. If the association execution runs successfully, then the association is COMPLIANT . If the association execution doesn\'t run successfully, the association is NON-COMPLIANT .\nIn MANUAL mode, you must specify the AssociationId as a parameter for the PutComplianceItems API action. In this case, compliance data is not managed by State Manager. It is managed by your direct call to the PutComplianceItems API action.\nBy default, all associations use AUTO mode.\n

    :rtype: dict

ReturnsResponse Syntax
{
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
        'AutomationTargetParameterName': 'string',
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
        'AssociationName': 'string',
        'MaxErrors': 'string',
        'MaxConcurrency': 'string',
        'ComplianceSeverity': 'CRITICAL'|'HIGH'|'MEDIUM'|'LOW'|'UNSPECIFIED',
        'SyncCompliance': 'AUTO'|'MANUAL'
    }
}


Response Structure

(dict) --

AssociationDescription (dict) --
Information about the association.

Name (string) --
The name of the Systems Manager document.

InstanceId (string) --
The ID of the instance.

AssociationVersion (string) --
The association version.

Date (datetime) --
The date when the association was made.

LastUpdateAssociationDate (datetime) --
The date when the association was last updated.

Status (dict) --
The association status.

Date (datetime) --
The date when the status changed.

Name (string) --
The status.

Message (string) --
The reason for the status.

AdditionalInfo (string) --
A user-defined string.



Overview (dict) --
Information about the association.

Status (string) --
The status of the association. Status can be: Pending, Success, or Failed.

DetailedStatus (string) --
A detailed status of the association.

AssociationStatusAggregatedCount (dict) --
Returns the number of targets for the association status. For example, if you created an association with two instances, and one of them was successful, this would return the count of instances by status.

(string) --
(integer) --






DocumentVersion (string) --
The document version.

AutomationTargetParameterName (string) --
Specify the target for the association. This target is required for associations that use an Automation document and target resources by using rate controls.

Parameters (dict) --
A description of the parameters for a document.

(string) --
(list) --
(string) --






AssociationId (string) --
The association ID.

Targets (list) --
The instances targeted by the request.

(dict) --
An array of search criteria that targets instances using a Key,Value combination that you specify.
Supported formats include the following.

``Key=InstanceIds,Values=*instance-id-1* ,*instance-id-2* ,*instance-id-3* ``
``Key=tag:my-tag-key ,Values=*my-tag-value-1* ,*my-tag-value-2* ``
``Key=tag-key,Values=*my-tag-key-1* ,*my-tag-key-2* ``
(Maintenance window targets only) ``Key=resource-groups:Name,Values=*resource-group-name* ``
(Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*resource-type-1* ,*resource-type-2* ``

For example:

Key=InstanceIds,Values=i-02573cafcfEXAMPLE,i-0471e04240EXAMPLE,i-07782c72faEXAMPLE
Key=tag:CostCenter,Values=CostCenter1,CostCenter2,CostCenter3
Key=tag-key,Values=Name,Instance-Type,CostCenter
(Maintenance window targets only) Key=resource-groups:Name,Values=ProductionResourceGroup   This example demonstrates how to target all resources in the resource group ProductionResourceGroup in your maintenance window.
(Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*AWS::EC2::INSTANCE* ,*AWS::EC2::VPC* ``   This example demonstrates how to target only EC2 instances and VPCs in your maintenance window.
(State Manager association targets only) Key=InstanceIds,Values=*   This example demonstrates how to target all managed instances in the AWS Region where the association was created.

For information about how to send commands that target instances using Key,Value parameters, see Targeting multiple instances in the AWS Systems Manager User Guide .

Key (string) --
User-defined criteria for sending commands that target instances that meet the criteria.

Values (list) --
User-defined criteria that maps to Key . For example, if you specified tag:ServerRole , you could specify value:WebServer to run a command on instances that include EC2 tags of ServerRole,WebServer .

(string) --






ScheduleExpression (string) --
A cron expression that specifies a schedule when the association runs.

OutputLocation (dict) --
An S3 bucket where you want to store the output details of the request.

S3Location (dict) --
An S3 bucket where you want to store the results of this request.

OutputS3Region (string) --
(Deprecated) You can no longer specify this parameter. The system ignores it. Instead, Systems Manager automatically determines the Region of the S3 bucket.

OutputS3BucketName (string) --
The name of the S3 bucket.

OutputS3KeyPrefix (string) --
The S3 bucket subfolder.





LastExecutionDate (datetime) --
The date on which the association was last run.

LastSuccessfulExecutionDate (datetime) --
The last date on which the association was successfully run.

AssociationName (string) --
The association name.

MaxErrors (string) --
The number of errors that are allowed before the system stops sending requests to run the association on additional targets. You can specify either an absolute number of errors, for example 10, or a percentage of the target set, for example 10%. If you specify 3, for example, the system stops sending requests when the fourth error is received. If you specify 0, then the system stops sending requests after the first error is returned. If you run an association on 50 instances and set MaxError to 10%, then the system stops sending the request when the sixth error is received.
Executions that are already running an association when MaxErrors is reached are allowed to complete, but some of these executions may fail as well. If you need to ensure that there won\'t be more than max-errors failed executions, set MaxConcurrency to 1 so that executions proceed one at a time.

MaxConcurrency (string) --
The maximum number of targets allowed to run the association at the same time. You can specify a number, for example 10, or a percentage of the target set, for example 10%. The default value is 100%, which means all targets run the association at the same time.
If a new instance starts and attempts to run an association while Systems Manager is running MaxConcurrency associations, the association is allowed to run. During the next association interval, the new instance will process its association within the limit specified for MaxConcurrency.

ComplianceSeverity (string) --
The severity level that is assigned to the association.

SyncCompliance (string) --
The mode for generating association compliance. You can specify AUTO or MANUAL . In AUTO mode, the system uses the status of the association execution to determine the compliance status. If the association execution runs successfully, then the association is COMPLIANT . If the association execution doesn\'t run successfully, the association is NON-COMPLIANT .
In MANUAL mode, you must specify the AssociationId as a parameter for the  PutComplianceItems API action. In this case, compliance data is not managed by State Manager. It is managed by your direct call to the  PutComplianceItems API action.
By default, all associations use AUTO mode.









Exceptions

SSM.Client.exceptions.AssociationAlreadyExists
SSM.Client.exceptions.AssociationLimitExceeded
SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.InvalidDocument
SSM.Client.exceptions.InvalidDocumentVersion
SSM.Client.exceptions.InvalidInstanceId
SSM.Client.exceptions.UnsupportedPlatformType
SSM.Client.exceptions.InvalidOutputLocation
SSM.Client.exceptions.InvalidParameters
SSM.Client.exceptions.InvalidTarget
SSM.Client.exceptions.InvalidSchedule


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
            'AutomationTargetParameterName': 'string',
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
            'AssociationName': 'string',
            'MaxErrors': 'string',
            'MaxConcurrency': 'string',
            'ComplianceSeverity': 'CRITICAL'|'HIGH'|'MEDIUM'|'LOW'|'UNSPECIFIED',
            'SyncCompliance': 'AUTO'|'MANUAL'
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
    When you associate a document with one or more instances using instance IDs or tags, SSM Agent running on the instance processes the document and configures the instance as specified.
    If you associate a document with an instance that already has an associated document, the system returns the AssociationAlreadyExists exception.
    See also: AWS API Documentation
    
    Exceptions
    
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
                'AutomationTargetParameterName': 'string',
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
                'AssociationName': 'string',
                'MaxErrors': 'string',
                'MaxConcurrency': 'string',
                'ComplianceSeverity': 'CRITICAL'|'HIGH'|'MEDIUM'|'LOW'|'UNSPECIFIED',
                'SyncCompliance': 'AUTO'|'MANUAL'
            },
        ]
    )
    
    
    :type Entries: list
    :param Entries: [REQUIRED]\nOne or more associations.\n\n(dict) --Describes the association of a Systems Manager SSM document and an instance.\n\nName (string) -- [REQUIRED]The name of the SSM document that contains the configuration information for the instance. You can specify Command or Automation documents.\nYou can specify AWS-predefined documents, documents you created, or a document that is shared with you from another account.\nFor SSM documents that are shared with you from other AWS accounts, you must specify the complete SSM document ARN, in the following format:\n\n``arn:aws:ssm:region :account-id :document/document-name ``\nFor example:\n\narn:aws:ssm:us-east-2:12345678912:document/My-Shared-Document\nFor AWS-predefined documents and SSM documents you created in your account, you only need to specify the document name. For example, AWS-ApplyPatchBaseline or My-Document .\n\nInstanceId (string) --The ID of the instance.\n\nParameters (dict) --A description of the parameters for a document.\n\n(string) --\n(list) --\n(string) --\n\n\n\n\n\n\nAutomationTargetParameterName (string) --Specify the target for the association. This target is required for associations that use an Automation document and target resources by using rate controls.\n\nDocumentVersion (string) --The document version.\n\nTargets (list) --The instances targeted by the request.\n\n(dict) --An array of search criteria that targets instances using a Key,Value combination that you specify.\nSupported formats include the following.\n\n``Key=InstanceIds,Values=*instance-id-1* ,*instance-id-2* ,*instance-id-3* ``\n``Key=tag:my-tag-key ,Values=*my-tag-value-1* ,*my-tag-value-2* ``\n``Key=tag-key,Values=*my-tag-key-1* ,*my-tag-key-2* ``\n(Maintenance window targets only) ``Key=resource-groups:Name,Values=*resource-group-name* ``\n(Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*resource-type-1* ,*resource-type-2* ``\n\nFor example:\n\nKey=InstanceIds,Values=i-02573cafcfEXAMPLE,i-0471e04240EXAMPLE,i-07782c72faEXAMPLE\nKey=tag:CostCenter,Values=CostCenter1,CostCenter2,CostCenter3\nKey=tag-key,Values=Name,Instance-Type,CostCenter\n(Maintenance window targets only) Key=resource-groups:Name,Values=ProductionResourceGroup  This example demonstrates how to target all resources in the resource group ProductionResourceGroup in your maintenance window.\n(Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*AWS::EC2::INSTANCE* ,*AWS::EC2::VPC* ``  This example demonstrates how to target only EC2 instances and VPCs in your maintenance window.\n(State Manager association targets only) Key=InstanceIds,Values=*  This example demonstrates how to target all managed instances in the AWS Region where the association was created.\n\nFor information about how to send commands that target instances using Key,Value parameters, see Targeting multiple instances in the AWS Systems Manager User Guide .\n\nKey (string) --User-defined criteria for sending commands that target instances that meet the criteria.\n\nValues (list) --User-defined criteria that maps to Key . For example, if you specified tag:ServerRole , you could specify value:WebServer to run a command on instances that include EC2 tags of ServerRole,WebServer .\n\n(string) --\n\n\n\n\n\n\nScheduleExpression (string) --A cron expression that specifies a schedule when the association runs.\n\nOutputLocation (dict) --An S3 bucket where you want to store the results of this request.\n\nS3Location (dict) --An S3 bucket where you want to store the results of this request.\n\nOutputS3Region (string) --(Deprecated) You can no longer specify this parameter. The system ignores it. Instead, Systems Manager automatically determines the Region of the S3 bucket.\n\nOutputS3BucketName (string) --The name of the S3 bucket.\n\nOutputS3KeyPrefix (string) --The S3 bucket subfolder.\n\n\n\n\n\nAssociationName (string) --Specify a descriptive name for the association.\n\nMaxErrors (string) --The number of errors that are allowed before the system stops sending requests to run the association on additional targets. You can specify either an absolute number of errors, for example 10, or a percentage of the target set, for example 10%. If you specify 3, for example, the system stops sending requests when the fourth error is received. If you specify 0, then the system stops sending requests after the first error is returned. If you run an association on 50 instances and set MaxError to 10%, then the system stops sending the request when the sixth error is received.\nExecutions that are already running an association when MaxErrors is reached are allowed to complete, but some of these executions may fail as well. If you need to ensure that there won\'t be more than max-errors failed executions, set MaxConcurrency to 1 so that executions proceed one at a time.\n\nMaxConcurrency (string) --The maximum number of targets allowed to run the association at the same time. You can specify a number, for example 10, or a percentage of the target set, for example 10%. The default value is 100%, which means all targets run the association at the same time.\nIf a new instance starts and attempts to run an association while Systems Manager is running MaxConcurrency associations, the association is allowed to run. During the next association interval, the new instance will process its association within the limit specified for MaxConcurrency.\n\nComplianceSeverity (string) --The severity level to assign to the association.\n\nSyncCompliance (string) --The mode for generating association compliance. You can specify AUTO or MANUAL . In AUTO mode, the system uses the status of the association execution to determine the compliance status. If the association execution runs successfully, then the association is COMPLIANT . If the association execution doesn\'t run successfully, the association is NON-COMPLIANT .\nIn MANUAL mode, you must specify the AssociationId as a parameter for the PutComplianceItems API action. In this case, compliance data is not managed by State Manager. It is managed by your direct call to the PutComplianceItems API action.\nBy default, all associations use AUTO mode.\n\n\n\n\n

    :rtype: dict
ReturnsResponse Syntax{
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
            'AutomationTargetParameterName': 'string',
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
            'AssociationName': 'string',
            'MaxErrors': 'string',
            'MaxConcurrency': 'string',
            'ComplianceSeverity': 'CRITICAL'|'HIGH'|'MEDIUM'|'LOW'|'UNSPECIFIED',
            'SyncCompliance': 'AUTO'|'MANUAL'
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
                'AutomationTargetParameterName': 'string',
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
                'AssociationName': 'string',
                'MaxErrors': 'string',
                'MaxConcurrency': 'string',
                'ComplianceSeverity': 'CRITICAL'|'HIGH'|'MEDIUM'|'LOW'|'UNSPECIFIED',
                'SyncCompliance': 'AUTO'|'MANUAL'
            },
            'Message': 'string',
            'Fault': 'Client'|'Server'|'Unknown'
        },
    ]
}


Response Structure

(dict) --
Successful (list) --Information about the associations that succeeded.

(dict) --Describes the parameters for a document.

Name (string) --The name of the Systems Manager document.

InstanceId (string) --The ID of the instance.

AssociationVersion (string) --The association version.

Date (datetime) --The date when the association was made.

LastUpdateAssociationDate (datetime) --The date when the association was last updated.

Status (dict) --The association status.

Date (datetime) --The date when the status changed.

Name (string) --The status.

Message (string) --The reason for the status.

AdditionalInfo (string) --A user-defined string.



Overview (dict) --Information about the association.

Status (string) --The status of the association. Status can be: Pending, Success, or Failed.

DetailedStatus (string) --A detailed status of the association.

AssociationStatusAggregatedCount (dict) --Returns the number of targets for the association status. For example, if you created an association with two instances, and one of them was successful, this would return the count of instances by status.

(string) --
(integer) --






DocumentVersion (string) --The document version.

AutomationTargetParameterName (string) --Specify the target for the association. This target is required for associations that use an Automation document and target resources by using rate controls.

Parameters (dict) --A description of the parameters for a document.

(string) --
(list) --
(string) --






AssociationId (string) --The association ID.

Targets (list) --The instances targeted by the request.

(dict) --An array of search criteria that targets instances using a Key,Value combination that you specify.
Supported formats include the following.

``Key=InstanceIds,Values=*instance-id-1* ,*instance-id-2* ,*instance-id-3* ``
``Key=tag:my-tag-key ,Values=*my-tag-value-1* ,*my-tag-value-2* ``
``Key=tag-key,Values=*my-tag-key-1* ,*my-tag-key-2* ``
(Maintenance window targets only) ``Key=resource-groups:Name,Values=*resource-group-name* ``
(Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*resource-type-1* ,*resource-type-2* ``

For example:

Key=InstanceIds,Values=i-02573cafcfEXAMPLE,i-0471e04240EXAMPLE,i-07782c72faEXAMPLE
Key=tag:CostCenter,Values=CostCenter1,CostCenter2,CostCenter3
Key=tag-key,Values=Name,Instance-Type,CostCenter
(Maintenance window targets only) Key=resource-groups:Name,Values=ProductionResourceGroup   This example demonstrates how to target all resources in the resource group ProductionResourceGroup in your maintenance window.
(Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*AWS::EC2::INSTANCE* ,*AWS::EC2::VPC* ``   This example demonstrates how to target only EC2 instances and VPCs in your maintenance window.
(State Manager association targets only) Key=InstanceIds,Values=*   This example demonstrates how to target all managed instances in the AWS Region where the association was created.

For information about how to send commands that target instances using Key,Value parameters, see Targeting multiple instances in the AWS Systems Manager User Guide .

Key (string) --User-defined criteria for sending commands that target instances that meet the criteria.

Values (list) --User-defined criteria that maps to Key . For example, if you specified tag:ServerRole , you could specify value:WebServer to run a command on instances that include EC2 tags of ServerRole,WebServer .

(string) --






ScheduleExpression (string) --A cron expression that specifies a schedule when the association runs.

OutputLocation (dict) --An S3 bucket where you want to store the output details of the request.

S3Location (dict) --An S3 bucket where you want to store the results of this request.

OutputS3Region (string) --(Deprecated) You can no longer specify this parameter. The system ignores it. Instead, Systems Manager automatically determines the Region of the S3 bucket.

OutputS3BucketName (string) --The name of the S3 bucket.

OutputS3KeyPrefix (string) --The S3 bucket subfolder.





LastExecutionDate (datetime) --The date on which the association was last run.

LastSuccessfulExecutionDate (datetime) --The last date on which the association was successfully run.

AssociationName (string) --The association name.

MaxErrors (string) --The number of errors that are allowed before the system stops sending requests to run the association on additional targets. You can specify either an absolute number of errors, for example 10, or a percentage of the target set, for example 10%. If you specify 3, for example, the system stops sending requests when the fourth error is received. If you specify 0, then the system stops sending requests after the first error is returned. If you run an association on 50 instances and set MaxError to 10%, then the system stops sending the request when the sixth error is received.
Executions that are already running an association when MaxErrors is reached are allowed to complete, but some of these executions may fail as well. If you need to ensure that there won\'t be more than max-errors failed executions, set MaxConcurrency to 1 so that executions proceed one at a time.

MaxConcurrency (string) --The maximum number of targets allowed to run the association at the same time. You can specify a number, for example 10, or a percentage of the target set, for example 10%. The default value is 100%, which means all targets run the association at the same time.
If a new instance starts and attempts to run an association while Systems Manager is running MaxConcurrency associations, the association is allowed to run. During the next association interval, the new instance will process its association within the limit specified for MaxConcurrency.

ComplianceSeverity (string) --The severity level that is assigned to the association.

SyncCompliance (string) --The mode for generating association compliance. You can specify AUTO or MANUAL . In AUTO mode, the system uses the status of the association execution to determine the compliance status. If the association execution runs successfully, then the association is COMPLIANT . If the association execution doesn\'t run successfully, the association is NON-COMPLIANT .
In MANUAL mode, you must specify the AssociationId as a parameter for the  PutComplianceItems API action. In this case, compliance data is not managed by State Manager. It is managed by your direct call to the  PutComplianceItems API action.
By default, all associations use AUTO mode.





Failed (list) --Information about the associations that failed.

(dict) --Describes a failed association.

Entry (dict) --The association.

Name (string) --The name of the SSM document that contains the configuration information for the instance. You can specify Command or Automation documents.
You can specify AWS-predefined documents, documents you created, or a document that is shared with you from another account.
For SSM documents that are shared with you from other AWS accounts, you must specify the complete SSM document ARN, in the following format:

``arn:aws:ssm:region :account-id :document/document-name ``
For example:

arn:aws:ssm:us-east-2:12345678912:document/My-Shared-Document
For AWS-predefined documents and SSM documents you created in your account, you only need to specify the document name. For example, AWS-ApplyPatchBaseline or My-Document .

InstanceId (string) --The ID of the instance.

Parameters (dict) --A description of the parameters for a document.

(string) --
(list) --
(string) --






AutomationTargetParameterName (string) --Specify the target for the association. This target is required for associations that use an Automation document and target resources by using rate controls.

DocumentVersion (string) --The document version.

Targets (list) --The instances targeted by the request.

(dict) --An array of search criteria that targets instances using a Key,Value combination that you specify.
Supported formats include the following.

``Key=InstanceIds,Values=*instance-id-1* ,*instance-id-2* ,*instance-id-3* ``
``Key=tag:my-tag-key ,Values=*my-tag-value-1* ,*my-tag-value-2* ``
``Key=tag-key,Values=*my-tag-key-1* ,*my-tag-key-2* ``
(Maintenance window targets only) ``Key=resource-groups:Name,Values=*resource-group-name* ``
(Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*resource-type-1* ,*resource-type-2* ``

For example:

Key=InstanceIds,Values=i-02573cafcfEXAMPLE,i-0471e04240EXAMPLE,i-07782c72faEXAMPLE
Key=tag:CostCenter,Values=CostCenter1,CostCenter2,CostCenter3
Key=tag-key,Values=Name,Instance-Type,CostCenter
(Maintenance window targets only) Key=resource-groups:Name,Values=ProductionResourceGroup   This example demonstrates how to target all resources in the resource group ProductionResourceGroup in your maintenance window.
(Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*AWS::EC2::INSTANCE* ,*AWS::EC2::VPC* ``   This example demonstrates how to target only EC2 instances and VPCs in your maintenance window.
(State Manager association targets only) Key=InstanceIds,Values=*   This example demonstrates how to target all managed instances in the AWS Region where the association was created.

For information about how to send commands that target instances using Key,Value parameters, see Targeting multiple instances in the AWS Systems Manager User Guide .

Key (string) --User-defined criteria for sending commands that target instances that meet the criteria.

Values (list) --User-defined criteria that maps to Key . For example, if you specified tag:ServerRole , you could specify value:WebServer to run a command on instances that include EC2 tags of ServerRole,WebServer .

(string) --






ScheduleExpression (string) --A cron expression that specifies a schedule when the association runs.

OutputLocation (dict) --An S3 bucket where you want to store the results of this request.

S3Location (dict) --An S3 bucket where you want to store the results of this request.

OutputS3Region (string) --(Deprecated) You can no longer specify this parameter. The system ignores it. Instead, Systems Manager automatically determines the Region of the S3 bucket.

OutputS3BucketName (string) --The name of the S3 bucket.

OutputS3KeyPrefix (string) --The S3 bucket subfolder.





AssociationName (string) --Specify a descriptive name for the association.

MaxErrors (string) --The number of errors that are allowed before the system stops sending requests to run the association on additional targets. You can specify either an absolute number of errors, for example 10, or a percentage of the target set, for example 10%. If you specify 3, for example, the system stops sending requests when the fourth error is received. If you specify 0, then the system stops sending requests after the first error is returned. If you run an association on 50 instances and set MaxError to 10%, then the system stops sending the request when the sixth error is received.
Executions that are already running an association when MaxErrors is reached are allowed to complete, but some of these executions may fail as well. If you need to ensure that there won\'t be more than max-errors failed executions, set MaxConcurrency to 1 so that executions proceed one at a time.

MaxConcurrency (string) --The maximum number of targets allowed to run the association at the same time. You can specify a number, for example 10, or a percentage of the target set, for example 10%. The default value is 100%, which means all targets run the association at the same time.
If a new instance starts and attempts to run an association while Systems Manager is running MaxConcurrency associations, the association is allowed to run. During the next association interval, the new instance will process its association within the limit specified for MaxConcurrency.

ComplianceSeverity (string) --The severity level to assign to the association.

SyncCompliance (string) --The mode for generating association compliance. You can specify AUTO or MANUAL . In AUTO mode, the system uses the status of the association execution to determine the compliance status. If the association execution runs successfully, then the association is COMPLIANT . If the association execution doesn\'t run successfully, the association is NON-COMPLIANT .
In MANUAL mode, you must specify the AssociationId as a parameter for the  PutComplianceItems API action. In this case, compliance data is not managed by State Manager. It is managed by your direct call to the  PutComplianceItems API action.
By default, all associations use AUTO mode.



Message (string) --A description of the failure.

Fault (string) --The source of the failure.










Exceptions

SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.InvalidDocument
SSM.Client.exceptions.InvalidDocumentVersion
SSM.Client.exceptions.InvalidInstanceId
SSM.Client.exceptions.InvalidParameters
SSM.Client.exceptions.DuplicateInstanceId
SSM.Client.exceptions.AssociationLimitExceeded
SSM.Client.exceptions.UnsupportedPlatformType
SSM.Client.exceptions.InvalidOutputLocation
SSM.Client.exceptions.InvalidTarget
SSM.Client.exceptions.InvalidSchedule


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
                'AutomationTargetParameterName': 'string',
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
                'AssociationName': 'string',
                'MaxErrors': 'string',
                'MaxConcurrency': 'string',
                'ComplianceSeverity': 'CRITICAL'|'HIGH'|'MEDIUM'|'LOW'|'UNSPECIFIED',
                'SyncCompliance': 'AUTO'|'MANUAL'
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
                    'AutomationTargetParameterName': 'string',
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
                    'AssociationName': 'string',
                    'MaxErrors': 'string',
                    'MaxConcurrency': 'string',
                    'ComplianceSeverity': 'CRITICAL'|'HIGH'|'MEDIUM'|'LOW'|'UNSPECIFIED',
                    'SyncCompliance': 'AUTO'|'MANUAL'
                },
                'Message': 'string',
                'Fault': 'Client'|'Server'|'Unknown'
            },
        ]
    }
    
    
    :returns: 
    ``Key=InstanceIds,Values=*instance-id-1* ,*instance-id-2* ,*instance-id-3* ``
    ``Key=tag:my-tag-key ,Values=*my-tag-value-1* ,*my-tag-value-2* ``
    ``Key=tag-key,Values=*my-tag-key-1* ,*my-tag-key-2* ``
    (Maintenance window targets only) ``Key=resource-groups:Name,Values=*resource-group-name* ``
    (Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*resource-type-1* ,*resource-type-2* ``
    
    """
    pass

def create_document(Content=None, Requires=None, Attachments=None, Name=None, VersionName=None, DocumentType=None, DocumentFormat=None, TargetType=None, Tags=None):
    """
    Creates a Systems Manager (SSM) document. An SSM document defines the actions that Systems Manager performs on your managed instances. For more information about SSM documents, including information about supported schemas, features, and syntax, see AWS Systems Manager Documents in the AWS Systems Manager User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_document(
        Content='string',
        Requires=[
            {
                'Name': 'string',
                'Version': 'string'
            },
        ],
        Attachments=[
            {
                'Key': 'SourceUrl'|'S3FileUrl'|'AttachmentReference',
                'Values': [
                    'string',
                ],
                'Name': 'string'
            },
        ],
        Name='string',
        VersionName='string',
        DocumentType='Command'|'Policy'|'Automation'|'Session'|'Package'|'ApplicationConfiguration'|'ApplicationConfigurationSchema'|'DeploymentStrategy'|'ChangeCalendar',
        DocumentFormat='YAML'|'JSON'|'TEXT',
        TargetType='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type Content: string
    :param Content: [REQUIRED]\nThe content for the new SSM document in JSON or YAML format. We recommend storing the contents for your new document in an external JSON or YAML file and referencing the file in a command.\nFor examples, see the following topics in the AWS Systems Manager User Guide .\n\nCreate an SSM document (AWS API)\nCreate an SSM document (AWS CLI)\nCreate an SSM document (API)\n\n

    :type Requires: list
    :param Requires: A list of SSM documents required by a document. This parameter is used exclusively by AWS AppConfig. When a user creates an AppConfig configuration in an SSM document, the user must also specify a required document for validation purposes. In this case, an ApplicationConfiguration document requires an ApplicationConfigurationSchema document for validation purposes. For more information, see AWS AppConfig in the AWS Systems Manager User Guide .\n\n(dict) --An SSM document required by the current document.\n\nName (string) -- [REQUIRED]The name of the required SSM document. The name can be an Amazon Resource Name (ARN).\n\nVersion (string) --The document version required by the current document.\n\n\n\n\n

    :type Attachments: list
    :param Attachments: A list of key and value pairs that describe attachments to a version of a document.\n\n(dict) --Identifying information about a document attachment, including the file name and a key-value pair that identifies the location of an attachment to a document.\n\nKey (string) --The key of a key-value pair that identifies the location of an attachment to a document.\n\nValues (list) --The value of a key-value pair that identifies the location of an attachment to a document. The format for Value depends on the type of key you specify.\n\nFor the key SourceUrl , the value is an S3 bucket location. For example: 'Values': [ 's3://my-bucket/my-folder' ]\nFor the key S3FileUrl , the value is a file in an S3 bucket. For example: 'Values': [ 's3://my-bucket/my-folder/my-file.py' ]\nFor the key AttachmentReference , the value is constructed from the name of another SSM document in your account, a version number of that document, and a file attached to that document version that you want to reuse. For example: 'Values': [ 'MyOtherDocument/3/my-other-file.py' ]  However, if the SSM document is shared with you from another account, the full SSM document ARN must be specified instead of the document name only. For example: 'Values': [ 'arn:aws:ssm:us-east-2:111122223333:document/OtherAccountDocument/3/their-file.py' ]\n\n\n(string) --\n\n\nName (string) --The name of the document attachment file.\n\n\n\n\n

    :type Name: string
    :param Name: [REQUIRED]\nA name for the Systems Manager document.\n\nWarning\nYou can\'t use the following strings as document name prefixes. These are reserved by AWS for use as document name prefixes:\n\naws-\namazon\namzn\n\n\n

    :type VersionName: string
    :param VersionName: An optional field specifying the version of the artifact you are creating with the document. For example, 'Release 12, Update 6'. This value is unique across all versions of a document, and cannot be changed.

    :type DocumentType: string
    :param DocumentType: The type of document to create.

    :type DocumentFormat: string
    :param DocumentFormat: Specify the document format for the request. The document format can be JSON, YAML, or TEXT. JSON is the default format.

    :type TargetType: string
    :param TargetType: Specify a target type to define the kinds of resources the document can run on. For example, to run a document on EC2 instances, specify the following value: /AWS::EC2::Instance. If you specify a value of \'/\' the document can run on all types of resources. If you don\'t specify a value, the document can\'t run on any resources. For a list of valid resource types, see AWS resource and property types reference in the AWS CloudFormation User Guide .

    :type Tags: list
    :param Tags: Optional metadata that you assign to a resource. Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For example, you might want to tag an SSM document to identify the types of targets or the environment where it will run. In this case, you could specify the following key name/value pairs:\n\nKey=OS,Value=Windows\nKey=Environment,Value=Production\n\n\nNote\nTo add tags to an existing SSM document, use the AddTagsToResource action.\n\n\n(dict) --Metadata that you assign to your AWS resources. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment. In Systems Manager, you can apply tags to documents, managed instances, maintenance windows, Parameter Store parameters, and patch baselines.\n\nKey (string) -- [REQUIRED]The name of the tag.\n\nValue (string) -- [REQUIRED]The value of the tag.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'DocumentDescription': {
        'Sha1': 'string',
        'Hash': 'string',
        'HashType': 'Sha256'|'Sha1',
        'Name': 'string',
        'VersionName': 'string',
        'Owner': 'string',
        'CreatedDate': datetime(2015, 1, 1),
        'Status': 'Creating'|'Active'|'Updating'|'Deleting'|'Failed',
        'StatusInformation': 'string',
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
        'DocumentType': 'Command'|'Policy'|'Automation'|'Session'|'Package'|'ApplicationConfiguration'|'ApplicationConfigurationSchema'|'DeploymentStrategy'|'ChangeCalendar',
        'SchemaVersion': 'string',
        'LatestVersion': 'string',
        'DefaultVersion': 'string',
        'DocumentFormat': 'YAML'|'JSON'|'TEXT',
        'TargetType': 'string',
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        'AttachmentsInformation': [
            {
                'Name': 'string'
            },
        ],
        'Requires': [
            {
                'Name': 'string',
                'Version': 'string'
            },
        ]
    }
}


Response Structure

(dict) --

DocumentDescription (dict) --
Information about the Systems Manager document.

Sha1 (string) --
The SHA1 hash of the document, which you can use for verification.

Hash (string) --
The Sha256 or Sha1 hash created by the system when the document was created.

Note
Sha1 hashes have been deprecated.


HashType (string) --
The hash type of the document. Valid values include Sha256 or Sha1 .

Note
Sha1 hashes have been deprecated.


Name (string) --
The name of the Systems Manager document.

VersionName (string) --
The version of the artifact associated with the document.

Owner (string) --
The AWS user account that created the document.

CreatedDate (datetime) --
The date when the document was created.

Status (string) --
The status of the Systems Manager document.

StatusInformation (string) --
A message returned by AWS Systems Manager that explains the Status value. For example, a Failed status might be explained by the StatusInformation message, "The specified S3 bucket does not exist. Verify that the URL of the S3 bucket is correct."

DocumentVersion (string) --
The document version.

Description (string) --
A description of the document.

Parameters (list) --
A description of the parameters for a document.

(dict) --
Parameters specified in a System Manager document that run on the server when the command is run.

Name (string) --
The name of the parameter.

Type (string) --
The type of parameter. The type can be either String or StringList.

Description (string) --
A description of what the parameter does, how to use it, the default value, and whether or not the parameter is optional.

DefaultValue (string) --
If specified, the default values for the parameters. Parameters without a default value are required. Parameters with a default value are optional.





PlatformTypes (list) --
The list of OS platforms compatible with this Systems Manager document.

(string) --


DocumentType (string) --
The type of document.

SchemaVersion (string) --
The schema version.

LatestVersion (string) --
The latest version of the document.

DefaultVersion (string) --
The default version.

DocumentFormat (string) --
The document format, either JSON or YAML.

TargetType (string) --
The target type which defines the kinds of resources the document can run on. For example, /AWS::EC2::Instance. For a list of valid resource types, see AWS resource and property types reference in the AWS CloudFormation User Guide .

Tags (list) --
The tags, or metadata, that have been applied to the document.

(dict) --
Metadata that you assign to your AWS resources. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment. In Systems Manager, you can apply tags to documents, managed instances, maintenance windows, Parameter Store parameters, and patch baselines.

Key (string) --
The name of the tag.

Value (string) --
The value of the tag.





AttachmentsInformation (list) --
Details about the document attachments, including names, locations, sizes, and so on.

(dict) --
An attribute of an attachment, such as the attachment name.

Name (string) --
The name of the attachment.





Requires (list) --
A list of SSM documents required by a document. For example, an ApplicationConfiguration document requires an ApplicationConfigurationSchema document.

(dict) --
An SSM document required by the current document.

Name (string) --
The name of the required SSM document. The name can be an Amazon Resource Name (ARN).

Version (string) --
The document version required by the current document.













Exceptions

SSM.Client.exceptions.DocumentAlreadyExists
SSM.Client.exceptions.MaxDocumentSizeExceeded
SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.InvalidDocumentContent
SSM.Client.exceptions.DocumentLimitExceeded
SSM.Client.exceptions.InvalidDocumentSchemaVersion


    :return: {
        'DocumentDescription': {
            'Sha1': 'string',
            'Hash': 'string',
            'HashType': 'Sha256'|'Sha1',
            'Name': 'string',
            'VersionName': 'string',
            'Owner': 'string',
            'CreatedDate': datetime(2015, 1, 1),
            'Status': 'Creating'|'Active'|'Updating'|'Deleting'|'Failed',
            'StatusInformation': 'string',
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
            'DocumentType': 'Command'|'Policy'|'Automation'|'Session'|'Package'|'ApplicationConfiguration'|'ApplicationConfigurationSchema'|'DeploymentStrategy'|'ChangeCalendar',
            'SchemaVersion': 'string',
            'LatestVersion': 'string',
            'DefaultVersion': 'string',
            'DocumentFormat': 'YAML'|'JSON'|'TEXT',
            'TargetType': 'string',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'AttachmentsInformation': [
                {
                    'Name': 'string'
                },
            ],
            'Requires': [
                {
                    'Name': 'string',
                    'Version': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_maintenance_window(Name=None, Description=None, StartDate=None, EndDate=None, Schedule=None, ScheduleTimezone=None, Duration=None, Cutoff=None, AllowUnassociatedTargets=None, ClientToken=None, Tags=None):
    """
    Creates a new maintenance window.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_maintenance_window(
        Name='string',
        Description='string',
        StartDate='string',
        EndDate='string',
        Schedule='string',
        ScheduleTimezone='string',
        Duration=123,
        Cutoff=123,
        AllowUnassociatedTargets=True|False,
        ClientToken='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the maintenance window.\n

    :type Description: string
    :param Description: An optional description for the maintenance window. We recommend specifying a description to help you organize your maintenance windows.

    :type StartDate: string
    :param StartDate: The date and time, in ISO-8601 Extended format, for when you want the maintenance window to become active. StartDate allows you to delay activation of the maintenance window until the specified future date.

    :type EndDate: string
    :param EndDate: The date and time, in ISO-8601 Extended format, for when you want the maintenance window to become inactive. EndDate allows you to set a date and time in the future when the maintenance window will no longer run.

    :type Schedule: string
    :param Schedule: [REQUIRED]\nThe schedule of the maintenance window in the form of a cron or rate expression.\n

    :type ScheduleTimezone: string
    :param ScheduleTimezone: The time zone that the scheduled maintenance window executions are based on, in Internet Assigned Numbers Authority (IANA) format. For example: 'America/Los_Angeles', 'etc/UTC', or 'Asia/Seoul'. For more information, see the Time Zone Database on the IANA website.

    :type Duration: integer
    :param Duration: [REQUIRED]\nThe duration of the maintenance window in hours.\n

    :type Cutoff: integer
    :param Cutoff: [REQUIRED]\nThe number of hours before the end of the maintenance window that Systems Manager stops scheduling new tasks for execution.\n

    :type AllowUnassociatedTargets: boolean
    :param AllowUnassociatedTargets: [REQUIRED]\nEnables a maintenance window task to run on managed instances, even if you have not registered those instances as targets. If enabled, then you must specify the unregistered instances (by instance ID) when you register a task with the maintenance window.\nIf you don\'t enable this option, then you must specify previously-registered targets when you register a task with the maintenance window.\n

    :type ClientToken: string
    :param ClientToken: User-provided idempotency token.\nThis field is autopopulated if not provided.\n

    :type Tags: list
    :param Tags: Optional metadata that you assign to a resource. Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For example, you might want to tag a maintenance window to identify the type of tasks it will run, the types of targets, and the environment it will run in. In this case, you could specify the following key name/value pairs:\n\nKey=TaskType,Value=AgentUpdate\nKey=OS,Value=Windows\nKey=Environment,Value=Production\n\n\nNote\nTo add tags to an existing maintenance window, use the AddTagsToResource action.\n\n\n(dict) --Metadata that you assign to your AWS resources. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment. In Systems Manager, you can apply tags to documents, managed instances, maintenance windows, Parameter Store parameters, and patch baselines.\n\nKey (string) -- [REQUIRED]The name of the tag.\n\nValue (string) -- [REQUIRED]The value of the tag.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'WindowId': 'string'
}


Response Structure

(dict) --

WindowId (string) --
The ID of the created maintenance window.







Exceptions

SSM.Client.exceptions.IdempotentParameterMismatch
SSM.Client.exceptions.ResourceLimitExceededException
SSM.Client.exceptions.InternalServerError


    :return: {
        'WindowId': 'string'
    }
    
    
    :returns: 
    SSM.Client.exceptions.IdempotentParameterMismatch
    SSM.Client.exceptions.ResourceLimitExceededException
    SSM.Client.exceptions.InternalServerError
    
    """
    pass

def create_ops_item(Description=None, OperationalData=None, Notifications=None, Priority=None, RelatedOpsItems=None, Source=None, Title=None, Tags=None, Category=None, Severity=None):
    """
    Creates a new OpsItem. You must have permission in AWS Identity and Access Management (IAM) to create a new OpsItem. For more information, see Getting started with OpsCenter in the AWS Systems Manager User Guide .
    Operations engineers and IT professionals use OpsCenter to view, investigate, and remediate operational issues impacting the performance and health of their AWS resources. For more information, see AWS Systems Manager OpsCenter in the AWS Systems Manager User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_ops_item(
        Description='string',
        OperationalData={
            'string': {
                'Value': 'string',
                'Type': 'SearchableString'|'String'
            }
        },
        Notifications=[
            {
                'Arn': 'string'
            },
        ],
        Priority=123,
        RelatedOpsItems=[
            {
                'OpsItemId': 'string'
            },
        ],
        Source='string',
        Title='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        Category='string',
        Severity='string'
    )
    
    
    :type Description: string
    :param Description: [REQUIRED]\nInformation about the OpsItem.\n

    :type OperationalData: dict
    :param OperationalData: Operational data is custom data that provides useful reference details about the OpsItem. For example, you can specify log files, error strings, license keys, troubleshooting tips, or other relevant data. You enter operational data as key-value pairs. The key has a maximum length of 128 characters. The value has a maximum size of 20 KB.\n\nWarning\nOperational data keys can\'t begin with the following: amazon, aws, amzn, ssm, /amazon, /aws, /amzn, /ssm.\n\nYou can choose to make the data searchable by other users in the account or you can restrict search access. Searchable data means that all users with access to the OpsItem Overview page (as provided by the DescribeOpsItems API action) can view and search on the specified data. Operational data that is not searchable is only viewable by users who have access to the OpsItem (as provided by the GetOpsItem API action).\nUse the /aws/resources key in OperationalData to specify a related resource in the request. Use the /aws/automations key in OperationalData to associate an Automation runbook with the OpsItem. To view AWS CLI example commands that use these keys, see Creating OpsItems manually in the AWS Systems Manager User Guide .\n\n(string) --\n(dict) --An object that defines the value of the key and its type in the OperationalData map.\n\nValue (string) --The value of the OperationalData key.\n\nType (string) --The type of key-value pair. Valid types include SearchableString and String .\n\n\n\n\n\n\n

    :type Notifications: list
    :param Notifications: The Amazon Resource Name (ARN) of an SNS topic where notifications are sent when this OpsItem is edited or changed.\n\n(dict) --A notification about the OpsItem.\n\nArn (string) --The Amazon Resource Name (ARN) of an SNS topic where notifications are sent when this OpsItem is edited or changed.\n\n\n\n\n

    :type Priority: integer
    :param Priority: The importance of this OpsItem in relation to other OpsItems in the system.

    :type RelatedOpsItems: list
    :param RelatedOpsItems: One or more OpsItems that share something in common with the current OpsItems. For example, related OpsItems can include OpsItems with similar error messages, impacted resources, or statuses for the impacted resource.\n\n(dict) --An OpsItems that shares something in common with the current OpsItem. For example, related OpsItems can include OpsItems with similar error messages, impacted resources, or statuses for the impacted resource.\n\nOpsItemId (string) -- [REQUIRED]The ID of an OpsItem related to the current OpsItem.\n\n\n\n\n

    :type Source: string
    :param Source: [REQUIRED]\nThe origin of the OpsItem, such as Amazon EC2 or Systems Manager.\n\nNote\nThe source name can\'t contain the following strings: aws, amazon, and amzn.\n\n

    :type Title: string
    :param Title: [REQUIRED]\nA short heading that describes the nature of the OpsItem and the impacted resource.\n

    :type Tags: list
    :param Tags: Optional metadata that you assign to a resource. You can restrict access to OpsItems by using an inline IAM policy that specifies tags. For more information, see Getting started with OpsCenter in the AWS Systems Manager User Guide .\nTags use a key-value pair. For example:\n\nKey=Department,Value=Finance\n\nNote\nTo add tags to an existing OpsItem, use the AddTagsToResource action.\n\n\n(dict) --Metadata that you assign to your AWS resources. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment. In Systems Manager, you can apply tags to documents, managed instances, maintenance windows, Parameter Store parameters, and patch baselines.\n\nKey (string) -- [REQUIRED]The name of the tag.\n\nValue (string) -- [REQUIRED]The value of the tag.\n\n\n\n\n

    :type Category: string
    :param Category: Specify a category to assign to an OpsItem.

    :type Severity: string
    :param Severity: Specify a severity to assign to an OpsItem.

    :rtype: dict

ReturnsResponse Syntax
{
    'OpsItemId': 'string'
}


Response Structure

(dict) --

OpsItemId (string) --
The ID of the OpsItem.







Exceptions

SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.OpsItemAlreadyExistsException
SSM.Client.exceptions.OpsItemLimitExceededException
SSM.Client.exceptions.OpsItemInvalidParameterException


    :return: {
        'OpsItemId': 'string'
    }
    
    
    :returns: 
    SSM.Client.exceptions.InternalServerError
    SSM.Client.exceptions.OpsItemAlreadyExistsException
    SSM.Client.exceptions.OpsItemLimitExceededException
    SSM.Client.exceptions.OpsItemInvalidParameterException
    
    """
    pass

def create_patch_baseline(OperatingSystem=None, Name=None, GlobalFilters=None, ApprovalRules=None, ApprovedPatches=None, ApprovedPatchesComplianceLevel=None, ApprovedPatchesEnableNonSecurity=None, RejectedPatches=None, RejectedPatchesAction=None, Description=None, Sources=None, ClientToken=None, Tags=None):
    """
    Creates a patch baseline.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_patch_baseline(
        OperatingSystem='WINDOWS'|'AMAZON_LINUX'|'AMAZON_LINUX_2'|'UBUNTU'|'REDHAT_ENTERPRISE_LINUX'|'SUSE'|'CENTOS'|'ORACLE_LINUX'|'DEBIAN',
        Name='string',
        GlobalFilters={
            'PatchFilters': [
                {
                    'Key': 'PATCH_SET'|'PRODUCT'|'PRODUCT_FAMILY'|'CLASSIFICATION'|'MSRC_SEVERITY'|'PATCH_ID'|'SECTION'|'PRIORITY'|'SEVERITY',
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
                                'Key': 'PATCH_SET'|'PRODUCT'|'PRODUCT_FAMILY'|'CLASSIFICATION'|'MSRC_SEVERITY'|'PATCH_ID'|'SECTION'|'PRIORITY'|'SEVERITY',
                                'Values': [
                                    'string',
                                ]
                            },
                        ]
                    },
                    'ComplianceLevel': 'CRITICAL'|'HIGH'|'MEDIUM'|'LOW'|'INFORMATIONAL'|'UNSPECIFIED',
                    'ApproveAfterDays': 123,
                    'ApproveUntilDate': 'string',
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
        RejectedPatchesAction='ALLOW_AS_DEPENDENCY'|'BLOCK',
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
        ClientToken='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type OperatingSystem: string
    :param OperatingSystem: Defines the operating system the patch baseline applies to. The Default value is WINDOWS.

    :type Name: string
    :param Name: [REQUIRED]\nThe name of the patch baseline.\n

    :type GlobalFilters: dict
    :param GlobalFilters: A set of global filters used to include patches in the baseline.\n\nPatchFilters (list) -- [REQUIRED]The set of patch filters that make up the group.\n\n(dict) --Defines which patches should be included in a patch baseline.\nA patch filter consists of a key and a set of values. The filter key is a patch property. For example, the available filter keys for WINDOWS are PATCH_SET, PRODUCT, PRODUCT_FAMILY, CLASSIFICATION, and MSRC_SEVERITY. The filter values define a matching criterion for the patch property indicated by the key. For example, if the filter key is PRODUCT and the filter values are ['Office 2013', 'Office 2016'], then the filter accepts all patches where product name is either 'Office 2013' or 'Office 2016'. The filter values can be exact values for the patch property given as a key, or a wildcard (*), which matches all values.\nYou can view lists of valid values for the patch properties by running the DescribePatchProperties command. For information about which patch properties can be used with each major operating system, see DescribePatchProperties .\n\nKey (string) -- [REQUIRED]The key for the filter.\nRun the DescribePatchProperties command to view lists of valid keys for each operating system type.\n\nValues (list) -- [REQUIRED]The value for the filter key.\nRun the DescribePatchProperties command to view lists of valid values for each key based on operating system type.\n\n(string) --\n\n\n\n\n\n\n\n

    :type ApprovalRules: dict
    :param ApprovalRules: A set of rules used to include patches in the baseline.\n\nPatchRules (list) -- [REQUIRED]The rules that make up the rule group.\n\n(dict) --Defines an approval rule for a patch baseline.\n\nPatchFilterGroup (dict) -- [REQUIRED]The patch filter group that defines the criteria for the rule.\n\nPatchFilters (list) -- [REQUIRED]The set of patch filters that make up the group.\n\n(dict) --Defines which patches should be included in a patch baseline.\nA patch filter consists of a key and a set of values. The filter key is a patch property. For example, the available filter keys for WINDOWS are PATCH_SET, PRODUCT, PRODUCT_FAMILY, CLASSIFICATION, and MSRC_SEVERITY. The filter values define a matching criterion for the patch property indicated by the key. For example, if the filter key is PRODUCT and the filter values are ['Office 2013', 'Office 2016'], then the filter accepts all patches where product name is either 'Office 2013' or 'Office 2016'. The filter values can be exact values for the patch property given as a key, or a wildcard (*), which matches all values.\nYou can view lists of valid values for the patch properties by running the DescribePatchProperties command. For information about which patch properties can be used with each major operating system, see DescribePatchProperties .\n\nKey (string) -- [REQUIRED]The key for the filter.\nRun the DescribePatchProperties command to view lists of valid keys for each operating system type.\n\nValues (list) -- [REQUIRED]The value for the filter key.\nRun the DescribePatchProperties command to view lists of valid values for each key based on operating system type.\n\n(string) --\n\n\n\n\n\n\n\n\nComplianceLevel (string) --A compliance severity level for all approved patches in a patch baseline.\n\nApproveAfterDays (integer) --The number of days after the release date of each patch matched by the rule that the patch is marked as approved in the patch baseline. For example, a value of 7 means that patches are approved seven days after they are released. Not supported on Ubuntu Server.\n\nApproveUntilDate (string) --The cutoff date for auto approval of released patches. Any patches released on or before this date are installed automatically. Not supported on Ubuntu Server.\nEnter dates in the format YYYY-MM-DD . For example, 2020-12-31 .\n\nEnableNonSecurity (boolean) --For instances identified by the approval rule filters, enables a patch baseline to apply non-security updates available in the specified repository. The default value is \'false\'. Applies to Linux instances only.\n\n\n\n\n\n\n

    :type ApprovedPatches: list
    :param ApprovedPatches: A list of explicitly approved patches for the baseline.\nFor information about accepted formats for lists of approved patches and rejected patches, see About package name formats for approved and rejected patch lists in the AWS Systems Manager User Guide .\n\n(string) --\n\n

    :type ApprovedPatchesComplianceLevel: string
    :param ApprovedPatchesComplianceLevel: Defines the compliance level for approved patches. This means that if an approved patch is reported as missing, this is the severity of the compliance violation. The default value is UNSPECIFIED.

    :type ApprovedPatchesEnableNonSecurity: boolean
    :param ApprovedPatchesEnableNonSecurity: Indicates whether the list of approved patches includes non-security updates that should be applied to the instances. The default value is \'false\'. Applies to Linux instances only.

    :type RejectedPatches: list
    :param RejectedPatches: A list of explicitly rejected patches for the baseline.\nFor information about accepted formats for lists of approved patches and rejected patches, see About package name formats for approved and rejected patch lists in the AWS Systems Manager User Guide .\n\n(string) --\n\n

    :type RejectedPatchesAction: string
    :param RejectedPatchesAction: The action for Patch Manager to take on patches included in the RejectedPackages list.\n\nALLOW_AS_DEPENDENCY : A package in the Rejected patches list is installed only if it is a dependency of another package. It is considered compliant with the patch baseline, and its status is reported as InstalledOther . This is the default action if no option is specified.\nBLOCK : Packages in the RejectedPatches list, and packages that include them as dependencies, are not installed under any circumstances. If a package was installed before it was added to the Rejected patches list, it is considered non-compliant with the patch baseline, and its status is reported as InstalledRejected .\n\n

    :type Description: string
    :param Description: A description of the patch baseline.

    :type Sources: list
    :param Sources: Information about the patches to use to update the instances, including target operating systems and source repositories. Applies to Linux instances only.\n\n(dict) --Information about the patches to use to update the instances, including target operating systems and source repository. Applies to Linux instances only.\n\nName (string) -- [REQUIRED]The name specified to identify the patch source.\n\nProducts (list) -- [REQUIRED]The specific operating system versions a patch repository applies to, such as 'Ubuntu16.04', 'AmazonLinux2016.09', 'RedhatEnterpriseLinux7.2' or 'Suse12.7'. For lists of supported product values, see PatchFilter .\n\n(string) --\n\n\nConfiguration (string) -- [REQUIRED]The value of the yum repo configuration. For example:\n\n[main]cachedir=/var/cache/yum/$basesearch$releasever\nkeepcache=0\ndebuglevel=2\n\n\n\n\n\n

    :type ClientToken: string
    :param ClientToken: User-provided idempotency token.\nThis field is autopopulated if not provided.\n

    :type Tags: list
    :param Tags: Optional metadata that you assign to a resource. Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For example, you might want to tag a patch baseline to identify the severity level of patches it specifies and the operating system family it applies to. In this case, you could specify the following key name/value pairs:\n\nKey=PatchSeverity,Value=Critical\nKey=OS,Value=Windows\n\n\nNote\nTo add tags to an existing patch baseline, use the AddTagsToResource action.\n\n\n(dict) --Metadata that you assign to your AWS resources. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment. In Systems Manager, you can apply tags to documents, managed instances, maintenance windows, Parameter Store parameters, and patch baselines.\n\nKey (string) -- [REQUIRED]The name of the tag.\n\nValue (string) -- [REQUIRED]The value of the tag.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'BaselineId': 'string'
}


Response Structure

(dict) --

BaselineId (string) --
The ID of the created patch baseline.







Exceptions

SSM.Client.exceptions.IdempotentParameterMismatch
SSM.Client.exceptions.ResourceLimitExceededException
SSM.Client.exceptions.InternalServerError


    :return: {
        'BaselineId': 'string'
    }
    
    
    :returns: 
    SSM.Client.exceptions.IdempotentParameterMismatch
    SSM.Client.exceptions.ResourceLimitExceededException
    SSM.Client.exceptions.InternalServerError
    
    """
    pass

def create_resource_data_sync(SyncName=None, S3Destination=None, SyncType=None, SyncSource=None):
    """
    A resource data sync helps you view data from multiple sources in a single location. Systems Manager offers two types of resource data sync: SyncToDestination and SyncFromSource .
    You can configure Systems Manager Inventory to use the SyncToDestination type to synchronize Inventory data from multiple AWS Regions to a single S3 bucket. For more information, see Configuring Resource Data Sync for Inventory in the AWS Systems Manager User Guide .
    You can configure Systems Manager Explorer to use the SyncFromSource type to synchronize operational work items (OpsItems) and operational data (OpsData) from multiple AWS Regions to a single S3 bucket. This type can synchronize OpsItems and OpsData from multiple AWS accounts and Regions or EntireOrganization by using AWS Organizations. For more information, see Setting up Systems Manager Explorer to display data from multiple accounts and Regions in the AWS Systems Manager User Guide .
    A resource data sync is an asynchronous operation that returns immediately. After a successful initial sync is completed, the system continuously syncs data. To check the status of a sync, use the  ListResourceDataSync .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_resource_data_sync(
        SyncName='string',
        S3Destination={
            'BucketName': 'string',
            'Prefix': 'string',
            'SyncFormat': 'JsonSerDe',
            'Region': 'string',
            'AWSKMSKeyARN': 'string',
            'DestinationDataSharing': {
                'DestinationDataSharingType': 'string'
            }
        },
        SyncType='string',
        SyncSource={
            'SourceType': 'string',
            'AwsOrganizationsSource': {
                'OrganizationSourceType': 'string',
                'OrganizationalUnits': [
                    {
                        'OrganizationalUnitId': 'string'
                    },
                ]
            },
            'SourceRegions': [
                'string',
            ],
            'IncludeFutureRegions': True|False
        }
    )
    
    
    :type SyncName: string
    :param SyncName: [REQUIRED]\nA name for the configuration.\n

    :type S3Destination: dict
    :param S3Destination: Amazon S3 configuration details for the sync. This parameter is required if the SyncType value is SyncToDestination.\n\nBucketName (string) -- [REQUIRED]The name of the S3 bucket where the aggregated data is stored.\n\nPrefix (string) --An Amazon S3 prefix for the bucket.\n\nSyncFormat (string) -- [REQUIRED]A supported sync format. The following format is currently supported: JsonSerDe\n\nRegion (string) -- [REQUIRED]The AWS Region with the S3 bucket targeted by the Resource Data Sync.\n\nAWSKMSKeyARN (string) --The ARN of an encryption key for a destination in Amazon S3. Must belong to the same Region as the destination S3 bucket.\n\nDestinationDataSharing (dict) --Enables destination data sharing. By default, this field is null .\n\nDestinationDataSharingType (string) --The sharing data type. Only Organization is supported.\n\n\n\n\n

    :type SyncType: string
    :param SyncType: Specify SyncToDestination to create a resource data sync that synchronizes data to an S3 bucket for Inventory. If you specify SyncToDestination , you must provide a value for S3Destination . Specify SyncFromSource to synchronize data from a single account and multiple Regions, or multiple AWS accounts and Regions, as listed in AWS Organizations for Explorer. If you specify SyncFromSource , you must provide a value for SyncSource . The default value is SyncToDestination .

    :type SyncSource: dict
    :param SyncSource: Specify information about the data sources to synchronize. This parameter is required if the SyncType value is SyncFromSource.\n\nSourceType (string) -- [REQUIRED]The type of data source for the resource data sync. SourceType is either AwsOrganizations (if an organization is present in AWS Organizations) or singleAccountMultiRegions .\n\nAwsOrganizationsSource (dict) --Information about the AwsOrganizationsSource resource data sync source. A sync source of this type can synchronize data from AWS Organizations.\n\nOrganizationSourceType (string) -- [REQUIRED]If an AWS Organization is present, this is either OrganizationalUnits or EntireOrganization . For OrganizationalUnits , the data is aggregated from a set of organization units. For EntireOrganization , the data is aggregated from the entire AWS Organization.\n\nOrganizationalUnits (list) --The AWS Organizations organization units included in the sync.\n\n(dict) --The AWS Organizations organizational unit data source for the sync.\n\nOrganizationalUnitId (string) --The AWS Organization unit ID data source for the sync.\n\n\n\n\n\n\n\nSourceRegions (list) -- [REQUIRED]The SyncSource AWS Regions included in the resource data sync.\n\n(string) --\n\n\nIncludeFutureRegions (boolean) --Whether to automatically synchronize and aggregate data from new AWS Regions when those Regions come online.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.ResourceDataSyncCountExceededException
SSM.Client.exceptions.ResourceDataSyncAlreadyExistsException
SSM.Client.exceptions.ResourceDataSyncInvalidConfigurationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_activation(ActivationId=None):
    """
    Deletes an activation. You are not required to delete an activation. If you delete an activation, you can no longer use it to register additional managed instances. Deleting an activation does not de-register managed instances. You must manually de-register managed instances.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_activation(
        ActivationId='string'
    )
    
    
    :type ActivationId: string
    :param ActivationId: [REQUIRED]\nThe ID of the activation that you want to delete.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

SSM.Client.exceptions.InvalidActivationId
SSM.Client.exceptions.InvalidActivation
SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.TooManyUpdates


    :return: {}
    
    
    :returns: 
    SSM.Client.exceptions.InvalidActivationId
    SSM.Client.exceptions.InvalidActivation
    SSM.Client.exceptions.InternalServerError
    SSM.Client.exceptions.TooManyUpdates
    
    """
    pass

def delete_association(Name=None, InstanceId=None, AssociationId=None):
    """
    Disassociates the specified Systems Manager document from the specified instance.
    When you disassociate a document from an instance, it does not change the configuration of the instance. To change the configuration state of an instance after you disassociate a document, you must create a new document with the desired configuration and associate it with the instance.
    See also: AWS API Documentation
    
    Exceptions
    
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

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

SSM.Client.exceptions.AssociationDoesNotExist
SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.InvalidDocument
SSM.Client.exceptions.InvalidInstanceId
SSM.Client.exceptions.TooManyUpdates


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_document(Name=None, DocumentVersion=None, VersionName=None, Force=None):
    """
    Deletes the Systems Manager document and all instance associations to the document.
    Before you delete the document, we recommend that you use  DeleteAssociation to disassociate all instances that are associated with the document.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_document(
        Name='string',
        DocumentVersion='string',
        VersionName='string',
        Force=True|False
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the document.\n

    :type DocumentVersion: string
    :param DocumentVersion: The version of the document that you want to delete. If not provided, all versions of the document are deleted.

    :type VersionName: string
    :param VersionName: The version name of the document that you want to delete. If not provided, all versions of the document are deleted.

    :type Force: boolean
    :param Force: Some SSM document types require that you specify a Force flag before you can delete the document. For example, you must specify a Force flag to delete a document of type ApplicationConfigurationSchema . You can restrict access to the Force flag in an AWS Identity and Access Management (IAM) policy.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.InvalidDocument
SSM.Client.exceptions.InvalidDocumentOperation
SSM.Client.exceptions.AssociatedInstances


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_inventory(TypeName=None, SchemaDeleteOption=None, DryRun=None, ClientToken=None):
    """
    Delete a custom inventory type, or the data associated with a custom Inventory type. Deleting a custom inventory type is also referred to as deleting a custom inventory schema.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_inventory(
        TypeName='string',
        SchemaDeleteOption='DisableSchema'|'DeleteSchema',
        DryRun=True|False,
        ClientToken='string'
    )
    
    
    :type TypeName: string
    :param TypeName: [REQUIRED]\nThe name of the custom inventory type for which you want to delete either all previously collected data, or the inventory type itself.\n

    :type SchemaDeleteOption: string
    :param SchemaDeleteOption: Use the SchemaDeleteOption to delete a custom inventory type (schema). If you don\'t choose this option, the system only deletes existing inventory data associated with the custom inventory type. Choose one of the following options:\nDisableSchema: If you choose this option, the system ignores all inventory data for the specified version, and any earlier versions. To enable this schema again, you must call the PutInventory action for a version greater than the disabled version.\nDeleteSchema: This option deletes the specified custom type from the Inventory service. You can recreate the schema later, if you want.\n

    :type DryRun: boolean
    :param DryRun: Use this option to view a summary of the deletion request without deleting any data or the data type. This option is useful when you only want to understand what will be deleted. Once you validate that the data to be deleted is what you intend to delete, you can run the same command without specifying the DryRun option.

    :type ClientToken: string
    :param ClientToken: User-provided idempotency token.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'DeletionId': 'string',
    'TypeName': 'string',
    'DeletionSummary': {
        'TotalCount': 123,
        'RemainingCount': 123,
        'SummaryItems': [
            {
                'Version': 'string',
                'Count': 123,
                'RemainingCount': 123
            },
        ]
    }
}


Response Structure

(dict) --

DeletionId (string) --
Every DeleteInventory action is assigned a unique ID. This option returns a unique ID. You can use this ID to query the status of a delete operation. This option is useful for ensuring that a delete operation has completed before you begin other actions.

TypeName (string) --
The name of the inventory data type specified in the request.

DeletionSummary (dict) --
A summary of the delete operation. For more information about this summary, see Deleting custom inventory in the AWS Systems Manager User Guide .

TotalCount (integer) --
The total number of items to delete. This count does not change during the delete operation.

RemainingCount (integer) --
Remaining number of items to delete.

SummaryItems (list) --
A list of counts and versions for deleted items.

(dict) --
Either a count, remaining count, or a version number in a delete inventory summary.

Version (string) --
The inventory type version.

Count (integer) --
A count of the number of deleted items.

RemainingCount (integer) --
The remaining number of items to delete.













Exceptions

SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.InvalidTypeNameException
SSM.Client.exceptions.InvalidOptionException
SSM.Client.exceptions.InvalidDeleteInventoryParametersException
SSM.Client.exceptions.InvalidInventoryRequestException


    :return: {
        'DeletionId': 'string',
        'TypeName': 'string',
        'DeletionSummary': {
            'TotalCount': 123,
            'RemainingCount': 123,
            'SummaryItems': [
                {
                    'Version': 'string',
                    'Count': 123,
                    'RemainingCount': 123
                },
            ]
        }
    }
    
    
    :returns: 
    SSM.Client.exceptions.InternalServerError
    SSM.Client.exceptions.InvalidTypeNameException
    SSM.Client.exceptions.InvalidOptionException
    SSM.Client.exceptions.InvalidDeleteInventoryParametersException
    SSM.Client.exceptions.InvalidInventoryRequestException
    
    """
    pass

def delete_maintenance_window(WindowId=None):
    """
    Deletes a maintenance window.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_maintenance_window(
        WindowId='string'
    )
    
    
    :type WindowId: string
    :param WindowId: [REQUIRED]\nThe ID of the maintenance window to delete.\n

    :rtype: dict
ReturnsResponse Syntax{
    'WindowId': 'string'
}


Response Structure

(dict) --
WindowId (string) --The ID of the deleted maintenance window.






Exceptions

SSM.Client.exceptions.InternalServerError


    :return: {
        'WindowId': 'string'
    }
    
    
    """
    pass

def delete_parameter(Name=None):
    """
    Delete a parameter from the system.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_parameter(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the parameter to delete.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.ParameterNotFound


    :return: {}
    
    
    :returns: 
    SSM.Client.exceptions.InternalServerError
    SSM.Client.exceptions.ParameterNotFound
    
    """
    pass

def delete_parameters(Names=None):
    """
    Delete a list of parameters.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_parameters(
        Names=[
            'string',
        ]
    )
    
    
    :type Names: list
    :param Names: [REQUIRED]\nThe names of the parameters to delete.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'DeletedParameters': [
        'string',
    ],
    'InvalidParameters': [
        'string',
    ]
}


Response Structure

(dict) --
DeletedParameters (list) --The names of the deleted parameters.

(string) --


InvalidParameters (list) --The names of parameters that weren\'t deleted because the parameters are not valid.

(string) --







Exceptions

SSM.Client.exceptions.InternalServerError


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
    
    Exceptions
    
    :example: response = client.delete_patch_baseline(
        BaselineId='string'
    )
    
    
    :type BaselineId: string
    :param BaselineId: [REQUIRED]\nThe ID of the patch baseline to delete.\n

    :rtype: dict
ReturnsResponse Syntax{
    'BaselineId': 'string'
}


Response Structure

(dict) --
BaselineId (string) --The ID of the deleted patch baseline.






Exceptions

SSM.Client.exceptions.ResourceInUseException
SSM.Client.exceptions.InternalServerError


    :return: {
        'BaselineId': 'string'
    }
    
    
    """
    pass

def delete_resource_data_sync(SyncName=None, SyncType=None):
    """
    Deletes a Resource Data Sync configuration. After the configuration is deleted, changes to data on managed instances are no longer synced to or from the target. Deleting a sync configuration does not delete data.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_resource_data_sync(
        SyncName='string',
        SyncType='string'
    )
    
    
    :type SyncName: string
    :param SyncName: [REQUIRED]\nThe name of the configuration to delete.\n

    :type SyncType: string
    :param SyncType: Specify the type of resource data sync to delete.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.ResourceDataSyncNotFoundException
SSM.Client.exceptions.ResourceDataSyncInvalidConfigurationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def deregister_managed_instance(InstanceId=None):
    """
    Removes the server or virtual machine from the list of registered servers. You can reregister the instance again at any time. If you don\'t plan to use Run Command on the server, we suggest uninstalling SSM Agent first.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.deregister_managed_instance(
        InstanceId='string'
    )
    
    
    :type InstanceId: string
    :param InstanceId: [REQUIRED]\nThe ID assigned to the managed instance when you registered it using the activation process.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

SSM.Client.exceptions.InvalidInstanceId
SSM.Client.exceptions.InternalServerError


    :return: {}
    
    
    :returns: 
    SSM.Client.exceptions.InvalidInstanceId
    SSM.Client.exceptions.InternalServerError
    
    """
    pass

def deregister_patch_baseline_for_patch_group(BaselineId=None, PatchGroup=None):
    """
    Removes a patch group from a patch baseline.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.deregister_patch_baseline_for_patch_group(
        BaselineId='string',
        PatchGroup='string'
    )
    
    
    :type BaselineId: string
    :param BaselineId: [REQUIRED]\nThe ID of the patch baseline to deregister the patch group from.\n

    :type PatchGroup: string
    :param PatchGroup: [REQUIRED]\nThe name of the patch group that should be deregistered from the patch baseline.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'BaselineId': 'string',
    'PatchGroup': 'string'
}


Response Structure

(dict) --

BaselineId (string) --
The ID of the patch baseline the patch group was deregistered from.

PatchGroup (string) --
The name of the patch group deregistered from the patch baseline.







Exceptions

SSM.Client.exceptions.InvalidResourceId
SSM.Client.exceptions.InternalServerError


    :return: {
        'BaselineId': 'string',
        'PatchGroup': 'string'
    }
    
    
    :returns: 
    SSM.Client.exceptions.InvalidResourceId
    SSM.Client.exceptions.InternalServerError
    
    """
    pass

def deregister_target_from_maintenance_window(WindowId=None, WindowTargetId=None, Safe=None):
    """
    Removes a target from a maintenance window.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.deregister_target_from_maintenance_window(
        WindowId='string',
        WindowTargetId='string',
        Safe=True|False
    )
    
    
    :type WindowId: string
    :param WindowId: [REQUIRED]\nThe ID of the maintenance window the target should be removed from.\n

    :type WindowTargetId: string
    :param WindowTargetId: [REQUIRED]\nThe ID of the target definition to remove.\n

    :type Safe: boolean
    :param Safe: The system checks if the target is being referenced by a task. If the target is being referenced, the system returns an error and does not deregister the target from the maintenance window.

    :rtype: dict

ReturnsResponse Syntax
{
    'WindowId': 'string',
    'WindowTargetId': 'string'
}


Response Structure

(dict) --

WindowId (string) --
The ID of the maintenance window the target was removed from.

WindowTargetId (string) --
The ID of the removed target definition.







Exceptions

SSM.Client.exceptions.DoesNotExistException
SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.TargetInUseException


    :return: {
        'WindowId': 'string',
        'WindowTargetId': 'string'
    }
    
    
    :returns: 
    SSM.Client.exceptions.DoesNotExistException
    SSM.Client.exceptions.InternalServerError
    SSM.Client.exceptions.TargetInUseException
    
    """
    pass

def deregister_task_from_maintenance_window(WindowId=None, WindowTaskId=None):
    """
    Removes a task from a maintenance window.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.deregister_task_from_maintenance_window(
        WindowId='string',
        WindowTaskId='string'
    )
    
    
    :type WindowId: string
    :param WindowId: [REQUIRED]\nThe ID of the maintenance window the task should be removed from.\n

    :type WindowTaskId: string
    :param WindowTaskId: [REQUIRED]\nThe ID of the task to remove from the maintenance window.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'WindowId': 'string',
    'WindowTaskId': 'string'
}


Response Structure

(dict) --

WindowId (string) --
The ID of the maintenance window the task was removed from.

WindowTaskId (string) --
The ID of the task removed from the maintenance window.







Exceptions

SSM.Client.exceptions.DoesNotExistException
SSM.Client.exceptions.InternalServerError


    :return: {
        'WindowId': 'string',
        'WindowTaskId': 'string'
    }
    
    
    :returns: 
    SSM.Client.exceptions.DoesNotExistException
    SSM.Client.exceptions.InternalServerError
    
    """
    pass

def describe_activations(Filters=None, MaxResults=None, NextToken=None):
    """
    Describes details about the activation, such as the date and time the activation was created, its expiration date, the IAM role assigned to the instances in the activation, and the number of instances registered by using this activation.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param Filters: A filter to view information about your activations.\n\n(dict) --Filter for the DescribeActivation API.\n\nFilterKey (string) --The name of the filter.\n\nFilterValues (list) --The filter values.\n\n(string) --\n\n\n\n\n\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :type NextToken: string
    :param NextToken: A token to start the list. Use this token to get the next set of results.

    :rtype: dict

ReturnsResponse Syntax
{
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
            'CreatedDate': datetime(2015, 1, 1),
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


Response Structure

(dict) --

ActivationList (list) --
A list of activations for your AWS account.

(dict) --
An activation registers one or more on-premises servers or virtual machines (VMs) with AWS so that you can configure those servers or VMs using Run Command. A server or VM that has been registered with AWS is called a managed instance.

ActivationId (string) --
The ID created by Systems Manager when you submitted the activation.

Description (string) --
A user defined description of the activation.

DefaultInstanceName (string) --
A name for the managed instance when it is created.

IamRole (string) --
The Amazon Identity and Access Management (IAM) role to assign to the managed instance.

RegistrationLimit (integer) --
The maximum number of managed instances that can be registered using this activation.

RegistrationsCount (integer) --
The number of managed instances already registered with this activation.

ExpirationDate (datetime) --
The date when this activation can no longer be used to register managed instances.

Expired (boolean) --
Whether or not the activation is expired.

CreatedDate (datetime) --
The date the activation was created.

Tags (list) --
Tags assigned to the activation.

(dict) --
Metadata that you assign to your AWS resources. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment. In Systems Manager, you can apply tags to documents, managed instances, maintenance windows, Parameter Store parameters, and patch baselines.

Key (string) --
The name of the tag.

Value (string) --
The value of the tag.









NextToken (string) --
The token for the next set of items to return. Use this token to get the next set of results.







Exceptions

SSM.Client.exceptions.InvalidFilter
SSM.Client.exceptions.InvalidNextToken
SSM.Client.exceptions.InternalServerError


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
                'CreatedDate': datetime(2015, 1, 1),
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
    SSM.Client.exceptions.InvalidFilter
    SSM.Client.exceptions.InvalidNextToken
    SSM.Client.exceptions.InternalServerError
    
    """
    pass

def describe_association(Name=None, InstanceId=None, AssociationId=None, AssociationVersion=None):
    """
    Describes the association for the specified target or instance. If you created the association by using the Targets parameter, then you must retrieve the association by using the association ID. If you created the association by specifying an instance ID and a Systems Manager document, then you retrieve the association by specifying the document name and the instance ID.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param AssociationVersion: Specify the association version to retrieve. To view the latest version, either specify $LATEST for this parameter, or omit this parameter. To view a list of all associations for an instance, use ListAssociations . To get a list of versions for a specific association, use ListAssociationVersions .

    :rtype: dict

ReturnsResponse Syntax
{
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
        'AutomationTargetParameterName': 'string',
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
        'AssociationName': 'string',
        'MaxErrors': 'string',
        'MaxConcurrency': 'string',
        'ComplianceSeverity': 'CRITICAL'|'HIGH'|'MEDIUM'|'LOW'|'UNSPECIFIED',
        'SyncCompliance': 'AUTO'|'MANUAL'
    }
}


Response Structure

(dict) --

AssociationDescription (dict) --
Information about the association.

Name (string) --
The name of the Systems Manager document.

InstanceId (string) --
The ID of the instance.

AssociationVersion (string) --
The association version.

Date (datetime) --
The date when the association was made.

LastUpdateAssociationDate (datetime) --
The date when the association was last updated.

Status (dict) --
The association status.

Date (datetime) --
The date when the status changed.

Name (string) --
The status.

Message (string) --
The reason for the status.

AdditionalInfo (string) --
A user-defined string.



Overview (dict) --
Information about the association.

Status (string) --
The status of the association. Status can be: Pending, Success, or Failed.

DetailedStatus (string) --
A detailed status of the association.

AssociationStatusAggregatedCount (dict) --
Returns the number of targets for the association status. For example, if you created an association with two instances, and one of them was successful, this would return the count of instances by status.

(string) --
(integer) --






DocumentVersion (string) --
The document version.

AutomationTargetParameterName (string) --
Specify the target for the association. This target is required for associations that use an Automation document and target resources by using rate controls.

Parameters (dict) --
A description of the parameters for a document.

(string) --
(list) --
(string) --






AssociationId (string) --
The association ID.

Targets (list) --
The instances targeted by the request.

(dict) --
An array of search criteria that targets instances using a Key,Value combination that you specify.
Supported formats include the following.

``Key=InstanceIds,Values=*instance-id-1* ,*instance-id-2* ,*instance-id-3* ``
``Key=tag:my-tag-key ,Values=*my-tag-value-1* ,*my-tag-value-2* ``
``Key=tag-key,Values=*my-tag-key-1* ,*my-tag-key-2* ``
(Maintenance window targets only) ``Key=resource-groups:Name,Values=*resource-group-name* ``
(Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*resource-type-1* ,*resource-type-2* ``

For example:

Key=InstanceIds,Values=i-02573cafcfEXAMPLE,i-0471e04240EXAMPLE,i-07782c72faEXAMPLE
Key=tag:CostCenter,Values=CostCenter1,CostCenter2,CostCenter3
Key=tag-key,Values=Name,Instance-Type,CostCenter
(Maintenance window targets only) Key=resource-groups:Name,Values=ProductionResourceGroup   This example demonstrates how to target all resources in the resource group ProductionResourceGroup in your maintenance window.
(Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*AWS::EC2::INSTANCE* ,*AWS::EC2::VPC* ``   This example demonstrates how to target only EC2 instances and VPCs in your maintenance window.
(State Manager association targets only) Key=InstanceIds,Values=*   This example demonstrates how to target all managed instances in the AWS Region where the association was created.

For information about how to send commands that target instances using Key,Value parameters, see Targeting multiple instances in the AWS Systems Manager User Guide .

Key (string) --
User-defined criteria for sending commands that target instances that meet the criteria.

Values (list) --
User-defined criteria that maps to Key . For example, if you specified tag:ServerRole , you could specify value:WebServer to run a command on instances that include EC2 tags of ServerRole,WebServer .

(string) --






ScheduleExpression (string) --
A cron expression that specifies a schedule when the association runs.

OutputLocation (dict) --
An S3 bucket where you want to store the output details of the request.

S3Location (dict) --
An S3 bucket where you want to store the results of this request.

OutputS3Region (string) --
(Deprecated) You can no longer specify this parameter. The system ignores it. Instead, Systems Manager automatically determines the Region of the S3 bucket.

OutputS3BucketName (string) --
The name of the S3 bucket.

OutputS3KeyPrefix (string) --
The S3 bucket subfolder.





LastExecutionDate (datetime) --
The date on which the association was last run.

LastSuccessfulExecutionDate (datetime) --
The last date on which the association was successfully run.

AssociationName (string) --
The association name.

MaxErrors (string) --
The number of errors that are allowed before the system stops sending requests to run the association on additional targets. You can specify either an absolute number of errors, for example 10, or a percentage of the target set, for example 10%. If you specify 3, for example, the system stops sending requests when the fourth error is received. If you specify 0, then the system stops sending requests after the first error is returned. If you run an association on 50 instances and set MaxError to 10%, then the system stops sending the request when the sixth error is received.
Executions that are already running an association when MaxErrors is reached are allowed to complete, but some of these executions may fail as well. If you need to ensure that there won\'t be more than max-errors failed executions, set MaxConcurrency to 1 so that executions proceed one at a time.

MaxConcurrency (string) --
The maximum number of targets allowed to run the association at the same time. You can specify a number, for example 10, or a percentage of the target set, for example 10%. The default value is 100%, which means all targets run the association at the same time.
If a new instance starts and attempts to run an association while Systems Manager is running MaxConcurrency associations, the association is allowed to run. During the next association interval, the new instance will process its association within the limit specified for MaxConcurrency.

ComplianceSeverity (string) --
The severity level that is assigned to the association.

SyncCompliance (string) --
The mode for generating association compliance. You can specify AUTO or MANUAL . In AUTO mode, the system uses the status of the association execution to determine the compliance status. If the association execution runs successfully, then the association is COMPLIANT . If the association execution doesn\'t run successfully, the association is NON-COMPLIANT .
In MANUAL mode, you must specify the AssociationId as a parameter for the  PutComplianceItems API action. In this case, compliance data is not managed by State Manager. It is managed by your direct call to the  PutComplianceItems API action.
By default, all associations use AUTO mode.









Exceptions

SSM.Client.exceptions.AssociationDoesNotExist
SSM.Client.exceptions.InvalidAssociationVersion
SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.InvalidDocument
SSM.Client.exceptions.InvalidInstanceId


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
            'AutomationTargetParameterName': 'string',
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
            'AssociationName': 'string',
            'MaxErrors': 'string',
            'MaxConcurrency': 'string',
            'ComplianceSeverity': 'CRITICAL'|'HIGH'|'MEDIUM'|'LOW'|'UNSPECIFIED',
            'SyncCompliance': 'AUTO'|'MANUAL'
        }
    }
    
    
    :returns: 
    (string) --
    (integer) --
    
    
    
    """
    pass

def describe_association_execution_targets(AssociationId=None, ExecutionId=None, Filters=None, MaxResults=None, NextToken=None):
    """
    Use this API action to view information about a specific execution of a specific association.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_association_execution_targets(
        AssociationId='string',
        ExecutionId='string',
        Filters=[
            {
                'Key': 'Status'|'ResourceId'|'ResourceType',
                'Value': 'string'
            },
        ],
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type AssociationId: string
    :param AssociationId: [REQUIRED]\nThe association ID that includes the execution for which you want to view details.\n

    :type ExecutionId: string
    :param ExecutionId: [REQUIRED]\nThe execution ID for which you want to view details.\n

    :type Filters: list
    :param Filters: Filters for the request. You can specify the following filters and values.\nStatus (EQUAL)\nResourceId (EQUAL)\nResourceType (EQUAL)\n\n(dict) --Filters for the association execution.\n\nKey (string) -- [REQUIRED]The key value used in the request.\n\nValue (string) -- [REQUIRED]The value specified for the key.\n\n\n\n\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :type NextToken: string
    :param NextToken: A token to start the list. Use this token to get the next set of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'AssociationExecutionTargets': [
        {
            'AssociationId': 'string',
            'AssociationVersion': 'string',
            'ExecutionId': 'string',
            'ResourceId': 'string',
            'ResourceType': 'string',
            'Status': 'string',
            'DetailedStatus': 'string',
            'LastExecutionDate': datetime(2015, 1, 1),
            'OutputSource': {
                'OutputSourceId': 'string',
                'OutputSourceType': 'string'
            }
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

AssociationExecutionTargets (list) --
Information about the execution.

(dict) --
Includes information about the specified association execution.

AssociationId (string) --
The association ID.

AssociationVersion (string) --
The association version.

ExecutionId (string) --
The execution ID.

ResourceId (string) --
The resource ID, for example, the instance ID where the association ran.

ResourceType (string) --
The resource type, for example, instance.

Status (string) --
The association execution status.

DetailedStatus (string) --
Detailed information about the execution status.

LastExecutionDate (datetime) --
The date of the last execution.

OutputSource (dict) --
The location where the association details are saved.

OutputSourceId (string) --
The ID of the output source, for example the URL of an S3 bucket.

OutputSourceType (string) --
The type of source where the association execution details are stored, for example, Amazon S3.







NextToken (string) --
The token for the next set of items to return. Use this token to get the next set of results.







Exceptions

SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.AssociationDoesNotExist
SSM.Client.exceptions.InvalidNextToken
SSM.Client.exceptions.AssociationExecutionDoesNotExist


    :return: {
        'AssociationExecutionTargets': [
            {
                'AssociationId': 'string',
                'AssociationVersion': 'string',
                'ExecutionId': 'string',
                'ResourceId': 'string',
                'ResourceType': 'string',
                'Status': 'string',
                'DetailedStatus': 'string',
                'LastExecutionDate': datetime(2015, 1, 1),
                'OutputSource': {
                    'OutputSourceId': 'string',
                    'OutputSourceType': 'string'
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    SSM.Client.exceptions.InternalServerError
    SSM.Client.exceptions.AssociationDoesNotExist
    SSM.Client.exceptions.InvalidNextToken
    SSM.Client.exceptions.AssociationExecutionDoesNotExist
    
    """
    pass

def describe_association_executions(AssociationId=None, Filters=None, MaxResults=None, NextToken=None):
    """
    Use this API action to view all executions for a specific association ID.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_association_executions(
        AssociationId='string',
        Filters=[
            {
                'Key': 'ExecutionId'|'Status'|'CreatedTime',
                'Value': 'string',
                'Type': 'EQUAL'|'LESS_THAN'|'GREATER_THAN'
            },
        ],
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type AssociationId: string
    :param AssociationId: [REQUIRED]\nThe association ID for which you want to view execution history details.\n

    :type Filters: list
    :param Filters: Filters for the request. You can specify the following filters and values.\nExecutionId (EQUAL)\nStatus (EQUAL)\nCreatedTime (EQUAL, GREATER_THAN, LESS_THAN)\n\n(dict) --Filters used in the request.\n\nKey (string) -- [REQUIRED]The key value used in the request.\n\nValue (string) -- [REQUIRED]The value specified for the key.\n\nType (string) -- [REQUIRED]The filter type specified in the request.\n\n\n\n\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :type NextToken: string
    :param NextToken: A token to start the list. Use this token to get the next set of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'AssociationExecutions': [
        {
            'AssociationId': 'string',
            'AssociationVersion': 'string',
            'ExecutionId': 'string',
            'Status': 'string',
            'DetailedStatus': 'string',
            'CreatedTime': datetime(2015, 1, 1),
            'LastExecutionDate': datetime(2015, 1, 1),
            'ResourceCountByStatus': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

AssociationExecutions (list) --
A list of the executions for the specified association ID.

(dict) --
Includes information about the specified association.

AssociationId (string) --
The association ID.

AssociationVersion (string) --
The association version.

ExecutionId (string) --
The execution ID for the association.

Status (string) --
The status of the association execution.

DetailedStatus (string) --
Detailed status information about the execution.

CreatedTime (datetime) --
The time the execution started.

LastExecutionDate (datetime) --
The date of the last execution.

ResourceCountByStatus (string) --
An aggregate status of the resources in the execution based on the status type.





NextToken (string) --
The token for the next set of items to return. Use this token to get the next set of results.







Exceptions

SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.AssociationDoesNotExist
SSM.Client.exceptions.InvalidNextToken


    :return: {
        'AssociationExecutions': [
            {
                'AssociationId': 'string',
                'AssociationVersion': 'string',
                'ExecutionId': 'string',
                'Status': 'string',
                'DetailedStatus': 'string',
                'CreatedTime': datetime(2015, 1, 1),
                'LastExecutionDate': datetime(2015, 1, 1),
                'ResourceCountByStatus': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    SSM.Client.exceptions.InternalServerError
    SSM.Client.exceptions.AssociationDoesNotExist
    SSM.Client.exceptions.InvalidNextToken
    
    """
    pass

def describe_automation_executions(Filters=None, MaxResults=None, NextToken=None):
    """
    Provides details about all active and terminated Automation executions.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_automation_executions(
        Filters=[
            {
                'Key': 'DocumentNamePrefix'|'ExecutionStatus'|'ExecutionId'|'ParentExecutionId'|'CurrentAction'|'StartTimeBefore'|'StartTimeAfter'|'AutomationType'|'TagKey',
                'Values': [
                    'string',
                ]
            },
        ],
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type Filters: list
    :param Filters: Filters used to limit the scope of executions that are requested.\n\n(dict) --A filter used to match specific automation executions. This is used to limit the scope of Automation execution information returned.\n\nKey (string) -- [REQUIRED]One or more keys to limit the results. Valid filter keys include the following: DocumentNamePrefix, ExecutionStatus, ExecutionId, ParentExecutionId, CurrentAction, StartTimeBefore, StartTimeAfter.\n\nValues (list) -- [REQUIRED]The values used to limit the execution information associated with the filter\'s key.\n\n(string) --\n\n\n\n\n\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :rtype: dict

ReturnsResponse Syntax
{
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
            'TargetMaps': [
                {
                    'string': [
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
            'Target': 'string',
            'AutomationType': 'CrossAccount'|'Local'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

AutomationExecutionMetadataList (list) --
The list of details about each automation execution which has occurred which matches the filter specification, if any.

(dict) --
Details about a specific Automation execution.

AutomationExecutionId (string) --
The execution ID.

DocumentName (string) --
The name of the Automation document used during execution.

DocumentVersion (string) --
The document version used during the execution.

AutomationExecutionStatus (string) --
The status of the execution.

ExecutionStartTime (datetime) --
The time the execution started.

ExecutionEndTime (datetime) --
The time the execution finished. This is not populated if the execution is still in progress.

ExecutedBy (string) --
The IAM role ARN of the user who ran the Automation.

LogFile (string) --
An S3 bucket where execution information is stored.

Outputs (dict) --
The list of execution outputs as defined in the Automation document.

(string) --
(list) --
(string) --






Mode (string) --
The Automation execution mode.

ParentAutomationExecutionId (string) --
The ExecutionId of the parent Automation.

CurrentStepName (string) --
The name of the step that is currently running.

CurrentAction (string) --
The action of the step that is currently running.

FailureMessage (string) --
The list of execution outputs as defined in the Automation document.

TargetParameterName (string) --
The list of execution outputs as defined in the Automation document.

Targets (list) --
The targets defined by the user when starting the Automation.

(dict) --
An array of search criteria that targets instances using a Key,Value combination that you specify.
Supported formats include the following.

``Key=InstanceIds,Values=*instance-id-1* ,*instance-id-2* ,*instance-id-3* ``
``Key=tag:my-tag-key ,Values=*my-tag-value-1* ,*my-tag-value-2* ``
``Key=tag-key,Values=*my-tag-key-1* ,*my-tag-key-2* ``
(Maintenance window targets only) ``Key=resource-groups:Name,Values=*resource-group-name* ``
(Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*resource-type-1* ,*resource-type-2* ``

For example:

Key=InstanceIds,Values=i-02573cafcfEXAMPLE,i-0471e04240EXAMPLE,i-07782c72faEXAMPLE
Key=tag:CostCenter,Values=CostCenter1,CostCenter2,CostCenter3
Key=tag-key,Values=Name,Instance-Type,CostCenter
(Maintenance window targets only) Key=resource-groups:Name,Values=ProductionResourceGroup   This example demonstrates how to target all resources in the resource group ProductionResourceGroup in your maintenance window.
(Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*AWS::EC2::INSTANCE* ,*AWS::EC2::VPC* ``   This example demonstrates how to target only EC2 instances and VPCs in your maintenance window.
(State Manager association targets only) Key=InstanceIds,Values=*   This example demonstrates how to target all managed instances in the AWS Region where the association was created.

For information about how to send commands that target instances using Key,Value parameters, see Targeting multiple instances in the AWS Systems Manager User Guide .

Key (string) --
User-defined criteria for sending commands that target instances that meet the criteria.

Values (list) --
User-defined criteria that maps to Key . For example, if you specified tag:ServerRole , you could specify value:WebServer to run a command on instances that include EC2 tags of ServerRole,WebServer .

(string) --






TargetMaps (list) --
The specified key-value mapping of document parameters to target resources.

(dict) --
(string) --
(list) --
(string) --








ResolvedTargets (dict) --
A list of targets that resolved during the execution.

ParameterValues (list) --
A list of parameter values sent to targets that resolved during the Automation execution.

(string) --


Truncated (boolean) --
A boolean value indicating whether the resolved target list is truncated.



MaxConcurrency (string) --
The MaxConcurrency value specified by the user when starting the Automation.

MaxErrors (string) --
The MaxErrors value specified by the user when starting the Automation.

Target (string) --
The list of execution outputs as defined in the Automation document.

AutomationType (string) --
Use this filter with  DescribeAutomationExecutions . Specify either Local or CrossAccount. CrossAccount is an Automation that runs in multiple AWS Regions and accounts. For more information, see Running Automation workflows in multiple AWS Regions and accounts in the AWS Systems Manager User Guide .





NextToken (string) --
The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.







Exceptions

SSM.Client.exceptions.InvalidFilterKey
SSM.Client.exceptions.InvalidFilterValue
SSM.Client.exceptions.InvalidNextToken
SSM.Client.exceptions.InternalServerError


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
                'TargetMaps': [
                    {
                        'string': [
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
                'Target': 'string',
                'AutomationType': 'CrossAccount'|'Local'
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
    
    Exceptions
    
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
    :param AutomationExecutionId: [REQUIRED]\nThe Automation execution ID for which you want step execution descriptions.\n

    :type Filters: list
    :param Filters: One or more filters to limit the number of step executions returned by the request.\n\n(dict) --A filter to limit the amount of step execution information returned by the call.\n\nKey (string) -- [REQUIRED]One or more keys to limit the results. Valid filter keys include the following: StepName, Action, StepExecutionId, StepExecutionStatus, StartTimeBefore, StartTimeAfter.\n\nValues (list) -- [REQUIRED]The values of the filter key.\n\n(string) --\n\n\n\n\n\n

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :type ReverseOrder: boolean
    :param ReverseOrder: A boolean that indicates whether to list step executions in reverse order by start time. The default value is false.

    :rtype: dict

ReturnsResponse Syntax
{
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
            },
            'IsEnd': True|False,
            'NextStep': 'string',
            'IsCritical': True|False,
            'ValidNextSteps': [
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
            'TargetLocation': {
                'Accounts': [
                    'string',
                ],
                'Regions': [
                    'string',
                ],
                'TargetLocationMaxConcurrency': 'string',
                'TargetLocationMaxErrors': 'string',
                'ExecutionRoleName': 'string'
            }
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

StepExecutions (list) --
A list of details about the current state of all steps that make up an execution.

(dict) --
Detailed information about an the execution state of an Automation step.

StepName (string) --
The name of this execution step.

Action (string) --
The action this step performs. The action determines the behavior of the step.

TimeoutSeconds (integer) --
The timeout seconds of the step.

OnFailure (string) --
The action to take if the step fails. The default value is Abort.

MaxAttempts (integer) --
The maximum number of tries to run the action of the step. The default value is 1.

ExecutionStartTime (datetime) --
If a step has begun execution, this contains the time the step started. If the step is in Pending status, this field is not populated.

ExecutionEndTime (datetime) --
If a step has finished execution, this contains the time the execution ended. If the step has not yet concluded, this field is not populated.

StepStatus (string) --
The execution status for this step.

ResponseCode (string) --
The response code returned by the execution of the step.

Inputs (dict) --
Fully-resolved values passed into the step before execution.

(string) --
(string) --




Outputs (dict) --
Returned values from the execution of the step.

(string) --
(list) --
(string) --






Response (string) --
A message associated with the response code for an execution.

FailureMessage (string) --
If a step failed, this message explains why the execution failed.

FailureDetails (dict) --
Information about the Automation failure.

FailureStage (string) --
The stage of the Automation execution when the failure occurred. The stages include the following: InputValidation, PreVerification, Invocation, PostVerification.

FailureType (string) --
The type of Automation failure. Failure types include the following: Action, Permission, Throttling, Verification, Internal.

Details (dict) --
Detailed information about the Automation step failure.

(string) --
(list) --
(string) --








StepExecutionId (string) --
The unique ID of a step execution.

OverriddenParameters (dict) --
A user-specified list of parameters to override when running a step.

(string) --
(list) --
(string) --






IsEnd (boolean) --
The flag which can be used to end automation no matter whether the step succeeds or fails.

NextStep (string) --
The next step after the step succeeds.

IsCritical (boolean) --
The flag which can be used to help decide whether the failure of current step leads to the Automation failure.

ValidNextSteps (list) --
Strategies used when step fails, we support Continue and Abort. Abort will fail the automation when the step fails. Continue will ignore the failure of current step and allow automation to run the next step. With conditional branching, we add step:stepName to support the automation to go to another specific step.

(string) --


Targets (list) --
The targets for the step execution.

(dict) --
An array of search criteria that targets instances using a Key,Value combination that you specify.
Supported formats include the following.

``Key=InstanceIds,Values=*instance-id-1* ,*instance-id-2* ,*instance-id-3* ``
``Key=tag:my-tag-key ,Values=*my-tag-value-1* ,*my-tag-value-2* ``
``Key=tag-key,Values=*my-tag-key-1* ,*my-tag-key-2* ``
(Maintenance window targets only) ``Key=resource-groups:Name,Values=*resource-group-name* ``
(Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*resource-type-1* ,*resource-type-2* ``

For example:

Key=InstanceIds,Values=i-02573cafcfEXAMPLE,i-0471e04240EXAMPLE,i-07782c72faEXAMPLE
Key=tag:CostCenter,Values=CostCenter1,CostCenter2,CostCenter3
Key=tag-key,Values=Name,Instance-Type,CostCenter
(Maintenance window targets only) Key=resource-groups:Name,Values=ProductionResourceGroup   This example demonstrates how to target all resources in the resource group ProductionResourceGroup in your maintenance window.
(Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*AWS::EC2::INSTANCE* ,*AWS::EC2::VPC* ``   This example demonstrates how to target only EC2 instances and VPCs in your maintenance window.
(State Manager association targets only) Key=InstanceIds,Values=*   This example demonstrates how to target all managed instances in the AWS Region where the association was created.

For information about how to send commands that target instances using Key,Value parameters, see Targeting multiple instances in the AWS Systems Manager User Guide .

Key (string) --
User-defined criteria for sending commands that target instances that meet the criteria.

Values (list) --
User-defined criteria that maps to Key . For example, if you specified tag:ServerRole , you could specify value:WebServer to run a command on instances that include EC2 tags of ServerRole,WebServer .

(string) --






TargetLocation (dict) --
The combination of AWS Regions and accounts targeted by the current Automation execution.

Accounts (list) --
The AWS accounts targeted by the current Automation execution.

(string) --


Regions (list) --
The AWS Regions targeted by the current Automation execution.

(string) --


TargetLocationMaxConcurrency (string) --
The maximum number of AWS accounts and AWS regions allowed to run the Automation concurrently

TargetLocationMaxErrors (string) --
The maximum number of errors allowed before the system stops queueing additional Automation executions for the currently running Automation.

ExecutionRoleName (string) --
The Automation execution role used by the currently running Automation.







NextToken (string) --
The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.







Exceptions

SSM.Client.exceptions.AutomationExecutionNotFoundException
SSM.Client.exceptions.InvalidNextToken
SSM.Client.exceptions.InvalidFilterKey
SSM.Client.exceptions.InvalidFilterValue
SSM.Client.exceptions.InternalServerError


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
                },
                'IsEnd': True|False,
                'NextStep': 'string',
                'IsCritical': True|False,
                'ValidNextSteps': [
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
                'TargetLocation': {
                    'Accounts': [
                        'string',
                    ],
                    'Regions': [
                        'string',
                    ],
                    'TargetLocationMaxConcurrency': 'string',
                    'TargetLocationMaxErrors': 'string',
                    'ExecutionRoleName': 'string'
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
    Lists all patches eligible to be included in a patch baseline.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param Filters: Filters used to scope down the returned patches.\n\n(dict) --Defines a filter used in Patch Manager APIs.\n\nKey (string) --The key for the filter.\n\nValues (list) --The value for the filter.\n\n(string) --\n\n\n\n\n\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of patches to return (per page).

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

Patches (list) --
An array of patches. Each entry in the array is a patch structure.

(dict) --
Represents metadata about a patch.

Id (string) --
The ID of the patch (this is different than the Microsoft Knowledge Base ID).

ReleaseDate (datetime) --
The date the patch was released.

Title (string) --
The title of the patch.

Description (string) --
The description of the patch.

ContentUrl (string) --
The URL where more information can be obtained about the patch.

Vendor (string) --
The name of the vendor providing the patch.

ProductFamily (string) --
The product family the patch is applicable for (for example, Windows).

Product (string) --
The specific product the patch is applicable for (for example, WindowsServer2016).

Classification (string) --
The classification of the patch (for example, SecurityUpdates, Updates, CriticalUpdates).

MsrcSeverity (string) --
The severity of the patch (for example Critical, Important, Moderate).

KbNumber (string) --
The Microsoft Knowledge Base ID of the patch.

MsrcNumber (string) --
The ID of the MSRC bulletin the patch is related to.

Language (string) --
The language of the patch if it\'s language-specific.





NextToken (string) --
The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.







Exceptions

SSM.Client.exceptions.InternalServerError


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
    
    
    :returns: 
    SSM.Client.exceptions.InternalServerError
    
    """
    pass

def describe_document(Name=None, DocumentVersion=None, VersionName=None):
    """
    Describes the specified Systems Manager document.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_document(
        Name='string',
        DocumentVersion='string',
        VersionName='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the Systems Manager document.\n

    :type DocumentVersion: string
    :param DocumentVersion: The document version for which you want information. Can be a specific version or the default version.

    :type VersionName: string
    :param VersionName: An optional field specifying the version of the artifact associated with the document. For example, 'Release 12, Update 6'. This value is unique across all versions of a document, and cannot be changed.

    :rtype: dict

ReturnsResponse Syntax
{
    'Document': {
        'Sha1': 'string',
        'Hash': 'string',
        'HashType': 'Sha256'|'Sha1',
        'Name': 'string',
        'VersionName': 'string',
        'Owner': 'string',
        'CreatedDate': datetime(2015, 1, 1),
        'Status': 'Creating'|'Active'|'Updating'|'Deleting'|'Failed',
        'StatusInformation': 'string',
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
        'DocumentType': 'Command'|'Policy'|'Automation'|'Session'|'Package'|'ApplicationConfiguration'|'ApplicationConfigurationSchema'|'DeploymentStrategy'|'ChangeCalendar',
        'SchemaVersion': 'string',
        'LatestVersion': 'string',
        'DefaultVersion': 'string',
        'DocumentFormat': 'YAML'|'JSON'|'TEXT',
        'TargetType': 'string',
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        'AttachmentsInformation': [
            {
                'Name': 'string'
            },
        ],
        'Requires': [
            {
                'Name': 'string',
                'Version': 'string'
            },
        ]
    }
}


Response Structure

(dict) --

Document (dict) --
Information about the Systems Manager document.

Sha1 (string) --
The SHA1 hash of the document, which you can use for verification.

Hash (string) --
The Sha256 or Sha1 hash created by the system when the document was created.

Note
Sha1 hashes have been deprecated.


HashType (string) --
The hash type of the document. Valid values include Sha256 or Sha1 .

Note
Sha1 hashes have been deprecated.


Name (string) --
The name of the Systems Manager document.

VersionName (string) --
The version of the artifact associated with the document.

Owner (string) --
The AWS user account that created the document.

CreatedDate (datetime) --
The date when the document was created.

Status (string) --
The status of the Systems Manager document.

StatusInformation (string) --
A message returned by AWS Systems Manager that explains the Status value. For example, a Failed status might be explained by the StatusInformation message, "The specified S3 bucket does not exist. Verify that the URL of the S3 bucket is correct."

DocumentVersion (string) --
The document version.

Description (string) --
A description of the document.

Parameters (list) --
A description of the parameters for a document.

(dict) --
Parameters specified in a System Manager document that run on the server when the command is run.

Name (string) --
The name of the parameter.

Type (string) --
The type of parameter. The type can be either String or StringList.

Description (string) --
A description of what the parameter does, how to use it, the default value, and whether or not the parameter is optional.

DefaultValue (string) --
If specified, the default values for the parameters. Parameters without a default value are required. Parameters with a default value are optional.





PlatformTypes (list) --
The list of OS platforms compatible with this Systems Manager document.

(string) --


DocumentType (string) --
The type of document.

SchemaVersion (string) --
The schema version.

LatestVersion (string) --
The latest version of the document.

DefaultVersion (string) --
The default version.

DocumentFormat (string) --
The document format, either JSON or YAML.

TargetType (string) --
The target type which defines the kinds of resources the document can run on. For example, /AWS::EC2::Instance. For a list of valid resource types, see AWS resource and property types reference in the AWS CloudFormation User Guide .

Tags (list) --
The tags, or metadata, that have been applied to the document.

(dict) --
Metadata that you assign to your AWS resources. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment. In Systems Manager, you can apply tags to documents, managed instances, maintenance windows, Parameter Store parameters, and patch baselines.

Key (string) --
The name of the tag.

Value (string) --
The value of the tag.





AttachmentsInformation (list) --
Details about the document attachments, including names, locations, sizes, and so on.

(dict) --
An attribute of an attachment, such as the attachment name.

Name (string) --
The name of the attachment.





Requires (list) --
A list of SSM documents required by a document. For example, an ApplicationConfiguration document requires an ApplicationConfigurationSchema document.

(dict) --
An SSM document required by the current document.

Name (string) --
The name of the required SSM document. The name can be an Amazon Resource Name (ARN).

Version (string) --
The document version required by the current document.













Exceptions

SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.InvalidDocument
SSM.Client.exceptions.InvalidDocumentVersion


    :return: {
        'Document': {
            'Sha1': 'string',
            'Hash': 'string',
            'HashType': 'Sha256'|'Sha1',
            'Name': 'string',
            'VersionName': 'string',
            'Owner': 'string',
            'CreatedDate': datetime(2015, 1, 1),
            'Status': 'Creating'|'Active'|'Updating'|'Deleting'|'Failed',
            'StatusInformation': 'string',
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
            'DocumentType': 'Command'|'Policy'|'Automation'|'Session'|'Package'|'ApplicationConfiguration'|'ApplicationConfigurationSchema'|'DeploymentStrategy'|'ChangeCalendar',
            'SchemaVersion': 'string',
            'LatestVersion': 'string',
            'DefaultVersion': 'string',
            'DocumentFormat': 'YAML'|'JSON'|'TEXT',
            'TargetType': 'string',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'AttachmentsInformation': [
                {
                    'Name': 'string'
                },
            ],
            'Requires': [
                {
                    'Name': 'string',
                    'Version': 'string'
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
    Describes the permissions for a Systems Manager document. If you created the document, you are the owner. If a document is shared, it can either be shared privately (by specifying a user\'s AWS account ID) or publicly (All ).
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_document_permission(
        Name='string',
        PermissionType='Share'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the document for which you are the owner.\n

    :type PermissionType: string
    :param PermissionType: [REQUIRED]\nThe permission type for the document. The permission type can be Share .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'AccountIds': [
        'string',
    ],
    'AccountSharingInfoList': [
        {
            'AccountId': 'string',
            'SharedDocumentVersion': 'string'
        },
    ]
}


Response Structure

(dict) --

AccountIds (list) --
The account IDs that have permission to use this document. The ID can be either an AWS account or All .

(string) --


AccountSharingInfoList (list) --
A list of AWS accounts where the current document is shared and the version shared with each account.

(dict) --
Information includes the AWS account ID where the current document is shared and the version shared with that account.

AccountId (string) --
The AWS account ID where the current document is shared.

SharedDocumentVersion (string) --
The version of the current document shared with the account.











Exceptions

SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.InvalidDocument
SSM.Client.exceptions.InvalidPermissionType


    :return: {
        'AccountIds': [
            'string',
        ],
        'AccountSharingInfoList': [
            {
                'AccountId': 'string',
                'SharedDocumentVersion': 'string'
            },
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
    
    Exceptions
    
    :example: response = client.describe_effective_instance_associations(
        InstanceId='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type InstanceId: string
    :param InstanceId: [REQUIRED]\nThe instance ID for which you want to view all associations.\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

Associations (list) --
The associations for the requested instance.

(dict) --
One or more association documents on the instance.

AssociationId (string) --
The association ID.

InstanceId (string) --
The instance ID.

Content (string) --
The content of the association document for the instance(s).

AssociationVersion (string) --
Version information for the association on the instance.





NextToken (string) --
The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.







Exceptions

SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.InvalidInstanceId
SSM.Client.exceptions.InvalidNextToken


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
    
    
    :returns: 
    SSM.Client.exceptions.InternalServerError
    SSM.Client.exceptions.InvalidInstanceId
    SSM.Client.exceptions.InvalidNextToken
    
    """
    pass

def describe_effective_patches_for_patch_baseline(BaselineId=None, MaxResults=None, NextToken=None):
    """
    Retrieves the current effective patches (the patch and the approval state) for the specified patch baseline. Note that this API applies only to Windows patch baselines.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_effective_patches_for_patch_baseline(
        BaselineId='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type BaselineId: string
    :param BaselineId: [REQUIRED]\nThe ID of the patch baseline to retrieve the effective patches for.\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of patches to return (per page).

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

EffectivePatches (list) --
An array of patches and patch status.

(dict) --
The EffectivePatch structure defines metadata about a patch along with the approval state of the patch in a particular patch baseline. The approval state includes information about whether the patch is currently approved, due to be approved by a rule, explicitly approved, or explicitly rejected and the date the patch was or will be approved.

Patch (dict) --
Provides metadata for a patch, including information such as the KB ID, severity, classification and a URL for where more information can be obtained about the patch.

Id (string) --
The ID of the patch (this is different than the Microsoft Knowledge Base ID).

ReleaseDate (datetime) --
The date the patch was released.

Title (string) --
The title of the patch.

Description (string) --
The description of the patch.

ContentUrl (string) --
The URL where more information can be obtained about the patch.

Vendor (string) --
The name of the vendor providing the patch.

ProductFamily (string) --
The product family the patch is applicable for (for example, Windows).

Product (string) --
The specific product the patch is applicable for (for example, WindowsServer2016).

Classification (string) --
The classification of the patch (for example, SecurityUpdates, Updates, CriticalUpdates).

MsrcSeverity (string) --
The severity of the patch (for example Critical, Important, Moderate).

KbNumber (string) --
The Microsoft Knowledge Base ID of the patch.

MsrcNumber (string) --
The ID of the MSRC bulletin the patch is related to.

Language (string) --
The language of the patch if it\'s language-specific.



PatchStatus (dict) --
The status of the patch in a patch baseline. This includes information about whether the patch is currently approved, due to be approved by a rule, explicitly approved, or explicitly rejected and the date the patch was or will be approved.

DeploymentStatus (string) --
The approval status of a patch (APPROVED, PENDING_APPROVAL, EXPLICIT_APPROVED, EXPLICIT_REJECTED).

ComplianceLevel (string) --
The compliance severity level for a patch.

ApprovalDate (datetime) --
The date the patch was approved (or will be approved if the status is PENDING_APPROVAL).







NextToken (string) --
The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.







Exceptions

SSM.Client.exceptions.InvalidResourceId
SSM.Client.exceptions.DoesNotExistException
SSM.Client.exceptions.UnsupportedOperatingSystem
SSM.Client.exceptions.InternalServerError


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
    
    
    :returns: 
    SSM.Client.exceptions.InvalidResourceId
    SSM.Client.exceptions.DoesNotExistException
    SSM.Client.exceptions.UnsupportedOperatingSystem
    SSM.Client.exceptions.InternalServerError
    
    """
    pass

def describe_instance_associations_status(InstanceId=None, MaxResults=None, NextToken=None):
    """
    The status of the associations for the instance(s).
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_instance_associations_status(
        InstanceId='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type InstanceId: string
    :param InstanceId: [REQUIRED]\nThe instance IDs for which you want association status information.\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

InstanceAssociationStatusInfos (list) --
Status information about the association.

(dict) --
Status information about the instance association.

AssociationId (string) --
The association ID.

Name (string) --
The name of the association.

DocumentVersion (string) --
The association document versions.

AssociationVersion (string) --
The version of the association applied to the instance.

InstanceId (string) --
The instance ID where the association was created.

ExecutionDate (datetime) --
The date the instance association ran.

Status (string) --
Status information about the instance association.

DetailedStatus (string) --
Detailed status information about the instance association.

ExecutionSummary (string) --
Summary information about association execution.

ErrorCode (string) --
An error code returned by the request to create the association.

OutputUrl (dict) --
A URL for an S3 bucket where you want to store the results of this request.

S3OutputUrl (dict) --
The URL of S3 bucket where you want to store the results of this request.

OutputUrl (string) --
A URL for an S3 bucket where you want to store the results of this request.





AssociationName (string) --
The name of the association applied to the instance.





NextToken (string) --
The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.







Exceptions

SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.InvalidInstanceId
SSM.Client.exceptions.InvalidNextToken


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
    
    
    :returns: 
    SSM.Client.exceptions.InternalServerError
    SSM.Client.exceptions.InvalidInstanceId
    SSM.Client.exceptions.InvalidNextToken
    
    """
    pass

def describe_instance_information(InstanceInformationFilterList=None, Filters=None, MaxResults=None, NextToken=None):
    """
    Describes one or more of your instances, including information about the operating system platform, the version of SSM Agent installed on the instance, instance status, and so on.
    If you specify one or more instance IDs, it returns information for those instances. If you do not specify instance IDs, it returns information for all your instances. If you specify an instance ID that is not valid or an instance that you do not own, you receive an error.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param InstanceInformationFilterList: This is a legacy method. We recommend that you don\'t use this method. Instead, use the Filters data type. Filters enables you to return instance information by filtering based on tags applied to managed instances.\n\nNote\nAttempting to use InstanceInformationFilterList and Filters leads to an exception error.\n\n\n(dict) --Describes a filter for a specific list of instances. You can filter instances information by using tags. You specify tags by using a key-value mapping.\nUse this action instead of the DescribeInstanceInformationRequest$InstanceInformationFilterList method. The InstanceInformationFilterList method is a legacy method and does not support tags.\n\nkey (string) -- [REQUIRED]The name of the filter.\n\nvalueSet (list) -- [REQUIRED]The filter values.\n\n(string) --\n\n\n\n\n\n

    :type Filters: list
    :param Filters: One or more filters. Use a filter to return a more specific list of instances. You can filter based on tags applied to EC2 instances. Use this Filters data type instead of InstanceInformationFilterList , which is deprecated.\n\n(dict) --The filters to describe or get information about your managed instances.\n\nKey (string) -- [REQUIRED]The filter key name to describe your instances. For example:\n'InstanceIds'|'AgentVersion'|'PingStatus'|'PlatformTypes'|'ActivationIds'|'IamRole'|'ResourceType'|'AssociationStatus'|'Tag Key'\n\nValues (list) -- [REQUIRED]The filter values.\n\n(string) --\n\n\n\n\n\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

InstanceInformationList (list) --
The instance information list.

(dict) --
Describes a filter for a specific list of instances.

InstanceId (string) --
The instance ID.

PingStatus (string) --
Connection status of SSM Agent.

LastPingDateTime (datetime) --
The date and time when agent last pinged Systems Manager service.

AgentVersion (string) --
The version of SSM Agent running on your Linux instance.

IsLatestVersion (boolean) --
Indicates whether the latest version of SSM Agent is running on your Linux Managed Instance. This field does not indicate whether or not the latest version is installed on Windows managed instances, because some older versions of Windows Server use the EC2Config service to process SSM requests.

PlatformType (string) --
The operating system platform type.

PlatformName (string) --
The name of the operating system platform running on your instance.

PlatformVersion (string) --
The version of the OS platform running on your instance.

ActivationId (string) --
The activation ID created by Systems Manager when the server or VM was registered.

IamRole (string) --
The Amazon Identity and Access Management (IAM) role assigned to the on-premises Systems Manager managed instances. This call does not return the IAM role for EC2 instances.

RegistrationDate (datetime) --
The date the server or VM was registered with AWS as a managed instance.

ResourceType (string) --
The type of instance. Instances are either EC2 instances or managed instances.

Name (string) --
The name of the managed instance.

IPAddress (string) --
The IP address of the managed instance.

ComputerName (string) --
The fully qualified host name of the managed instance.

AssociationStatus (string) --
The status of the association.

LastAssociationExecutionDate (datetime) --
The date the association was last run.

LastSuccessfulAssociationExecutionDate (datetime) --
The last date the association was successfully run.

AssociationOverview (dict) --
Information about the association.

DetailedStatus (string) --
Detailed status information about the aggregated associations.

InstanceAssociationStatusAggregatedCount (dict) --
The number of associations for the instance(s).

(string) --
(integer) --










NextToken (string) --
The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.







Exceptions

SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.InvalidInstanceId
SSM.Client.exceptions.InvalidNextToken
SSM.Client.exceptions.InvalidInstanceInformationFilterValue
SSM.Client.exceptions.InvalidFilterKey


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
    
    Exceptions
    
    :example: response = client.describe_instance_patch_states(
        InstanceIds=[
            'string',
        ],
        NextToken='string',
        MaxResults=123
    )
    
    
    :type InstanceIds: list
    :param InstanceIds: [REQUIRED]\nThe ID of the instance whose patch state information should be retrieved.\n\n(string) --\n\n

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :type MaxResults: integer
    :param MaxResults: The maximum number of instances to return (per page).

    :rtype: dict

ReturnsResponse Syntax
{
    'InstancePatchStates': [
        {
            'InstanceId': 'string',
            'PatchGroup': 'string',
            'BaselineId': 'string',
            'SnapshotId': 'string',
            'InstallOverrideList': 'string',
            'OwnerInformation': 'string',
            'InstalledCount': 123,
            'InstalledOtherCount': 123,
            'InstalledPendingRebootCount': 123,
            'InstalledRejectedCount': 123,
            'MissingCount': 123,
            'FailedCount': 123,
            'UnreportedNotApplicableCount': 123,
            'NotApplicableCount': 123,
            'OperationStartTime': datetime(2015, 1, 1),
            'OperationEndTime': datetime(2015, 1, 1),
            'Operation': 'Scan'|'Install',
            'LastNoRebootInstallOperationTime': datetime(2015, 1, 1),
            'RebootOption': 'RebootIfNeeded'|'NoReboot'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

InstancePatchStates (list) --
The high-level patch state for the requested instances.

(dict) --
Defines the high-level patch compliance state for a managed instance, providing information about the number of installed, missing, not applicable, and failed patches along with metadata about the operation when this information was gathered for the instance.

InstanceId (string) --
The ID of the managed instance the high-level patch compliance information was collected for.

PatchGroup (string) --
The name of the patch group the managed instance belongs to.

BaselineId (string) --
The ID of the patch baseline used to patch the instance.

SnapshotId (string) --
The ID of the patch baseline snapshot used during the patching operation when this compliance data was collected.

InstallOverrideList (string) --
An https URL or an Amazon S3 path-style URL to a list of patches to be installed. This patch installation list, which you maintain in an S3 bucket in YAML format and specify in the SSM document AWS-RunPatchBaseline , overrides the patches specified by the default patch baseline.
For more information about the InstallOverrideList parameter, see About the SSM document AWS-RunPatchBaseline in the AWS Systems Manager User Guide .

OwnerInformation (string) --
Placeholder information. This field will always be empty in the current release of the service.

InstalledCount (integer) --
The number of patches from the patch baseline that are installed on the instance.

InstalledOtherCount (integer) --
The number of patches not specified in the patch baseline that are installed on the instance.

InstalledPendingRebootCount (integer) --
The number of patches installed by Patch Manager since the last time the instance was rebooted.

InstalledRejectedCount (integer) --
The number of instances with patches installed that are specified in a RejectedPatches list. Patches with a status of InstalledRejected were typically installed before they were added to a RejectedPatches list.

Note
If ALLOW_AS_DEPENDENCY is the specified option for RejectedPatchesAction, the value of InstalledRejectedCount will always be 0 (zero).


MissingCount (integer) --
The number of patches from the patch baseline that are applicable for the instance but aren\'t currently installed.

FailedCount (integer) --
The number of patches from the patch baseline that were attempted to be installed during the last patching operation, but failed to install.

UnreportedNotApplicableCount (integer) --
The number of patches beyond the supported limit of NotApplicableCount that are not reported by name to Systems Manager Inventory.

NotApplicableCount (integer) --
The number of patches from the patch baseline that aren\'t applicable for the instance and therefore aren\'t installed on the instance. This number may be truncated if the list of patch names is very large. The number of patches beyond this limit are reported in UnreportedNotApplicableCount .

OperationStartTime (datetime) --
The time the most recent patching operation was started on the instance.

OperationEndTime (datetime) --
The time the most recent patching operation completed on the instance.

Operation (string) --
The type of patching operation that was performed: SCAN (assess patch compliance state) or INSTALL (install missing patches).

LastNoRebootInstallOperationTime (datetime) --
The time of the last attempt to patch the instance with NoReboot specified as the reboot option.

RebootOption (string) --
Indicates the reboot option specified in the patch baseline.

Note
Reboot options apply to Install operations only. Reboots are not attempted for Patch Manager Scan operations.


RebootIfNeeded : Patch Manager tries to reboot the instance if it installed any patches, or if any patches are detected with a status of InstalledPendingReboot .
NoReboot : Patch Manager attempts to install missing packages without trying to reboot the system. Patches installed with this option are assigned a status of InstalledPendingReboot . These patches might not be in effect until a reboot is performed.






NextToken (string) --
The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.







Exceptions

SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.InvalidNextToken


    :return: {
        'InstancePatchStates': [
            {
                'InstanceId': 'string',
                'PatchGroup': 'string',
                'BaselineId': 'string',
                'SnapshotId': 'string',
                'InstallOverrideList': 'string',
                'OwnerInformation': 'string',
                'InstalledCount': 123,
                'InstalledOtherCount': 123,
                'InstalledPendingRebootCount': 123,
                'InstalledRejectedCount': 123,
                'MissingCount': 123,
                'FailedCount': 123,
                'UnreportedNotApplicableCount': 123,
                'NotApplicableCount': 123,
                'OperationStartTime': datetime(2015, 1, 1),
                'OperationEndTime': datetime(2015, 1, 1),
                'Operation': 'Scan'|'Install',
                'LastNoRebootInstallOperationTime': datetime(2015, 1, 1),
                'RebootOption': 'RebootIfNeeded'|'NoReboot'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    RebootIfNeeded : Patch Manager tries to reboot the instance if it installed any patches, or if any patches are detected with a status of InstalledPendingReboot .
    NoReboot : Patch Manager attempts to install missing packages without trying to reboot the system. Patches installed with this option are assigned a status of InstalledPendingReboot . These patches might not be in effect until a reboot is performed.
    
    """
    pass

def describe_instance_patch_states_for_patch_group(PatchGroup=None, Filters=None, NextToken=None, MaxResults=None):
    """
    Retrieves the high-level patch state for the instances in the specified patch group.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param PatchGroup: [REQUIRED]\nThe name of the patch group for which the patch state information should be retrieved.\n

    :type Filters: list
    :param Filters: Each entry in the array is a structure containing:\nKey (string between 1 and 200 characters)\nValues (array containing a single string)\nType (string 'Equal', 'NotEqual', 'LessThan', 'GreaterThan')\n\n(dict) --Defines a filter used in DescribeInstancePatchStatesForPatchGroup used to scope down the information returned by the API.\n\nKey (string) -- [REQUIRED]The key for the filter. Supported values are FailedCount, InstalledCount, InstalledOtherCount, MissingCount and NotApplicableCount.\n\nValues (list) -- [REQUIRED]The value for the filter, must be an integer greater than or equal to 0.\n\n(string) --\n\n\nType (string) -- [REQUIRED]The type of comparison that should be performed for the value: Equal, NotEqual, LessThan or GreaterThan.\n\n\n\n\n

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :type MaxResults: integer
    :param MaxResults: The maximum number of patches to return (per page).

    :rtype: dict

ReturnsResponse Syntax
{
    'InstancePatchStates': [
        {
            'InstanceId': 'string',
            'PatchGroup': 'string',
            'BaselineId': 'string',
            'SnapshotId': 'string',
            'InstallOverrideList': 'string',
            'OwnerInformation': 'string',
            'InstalledCount': 123,
            'InstalledOtherCount': 123,
            'InstalledPendingRebootCount': 123,
            'InstalledRejectedCount': 123,
            'MissingCount': 123,
            'FailedCount': 123,
            'UnreportedNotApplicableCount': 123,
            'NotApplicableCount': 123,
            'OperationStartTime': datetime(2015, 1, 1),
            'OperationEndTime': datetime(2015, 1, 1),
            'Operation': 'Scan'|'Install',
            'LastNoRebootInstallOperationTime': datetime(2015, 1, 1),
            'RebootOption': 'RebootIfNeeded'|'NoReboot'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

InstancePatchStates (list) --
The high-level patch state for the requested instances.

(dict) --
Defines the high-level patch compliance state for a managed instance, providing information about the number of installed, missing, not applicable, and failed patches along with metadata about the operation when this information was gathered for the instance.

InstanceId (string) --
The ID of the managed instance the high-level patch compliance information was collected for.

PatchGroup (string) --
The name of the patch group the managed instance belongs to.

BaselineId (string) --
The ID of the patch baseline used to patch the instance.

SnapshotId (string) --
The ID of the patch baseline snapshot used during the patching operation when this compliance data was collected.

InstallOverrideList (string) --
An https URL or an Amazon S3 path-style URL to a list of patches to be installed. This patch installation list, which you maintain in an S3 bucket in YAML format and specify in the SSM document AWS-RunPatchBaseline , overrides the patches specified by the default patch baseline.
For more information about the InstallOverrideList parameter, see About the SSM document AWS-RunPatchBaseline in the AWS Systems Manager User Guide .

OwnerInformation (string) --
Placeholder information. This field will always be empty in the current release of the service.

InstalledCount (integer) --
The number of patches from the patch baseline that are installed on the instance.

InstalledOtherCount (integer) --
The number of patches not specified in the patch baseline that are installed on the instance.

InstalledPendingRebootCount (integer) --
The number of patches installed by Patch Manager since the last time the instance was rebooted.

InstalledRejectedCount (integer) --
The number of instances with patches installed that are specified in a RejectedPatches list. Patches with a status of InstalledRejected were typically installed before they were added to a RejectedPatches list.

Note
If ALLOW_AS_DEPENDENCY is the specified option for RejectedPatchesAction, the value of InstalledRejectedCount will always be 0 (zero).


MissingCount (integer) --
The number of patches from the patch baseline that are applicable for the instance but aren\'t currently installed.

FailedCount (integer) --
The number of patches from the patch baseline that were attempted to be installed during the last patching operation, but failed to install.

UnreportedNotApplicableCount (integer) --
The number of patches beyond the supported limit of NotApplicableCount that are not reported by name to Systems Manager Inventory.

NotApplicableCount (integer) --
The number of patches from the patch baseline that aren\'t applicable for the instance and therefore aren\'t installed on the instance. This number may be truncated if the list of patch names is very large. The number of patches beyond this limit are reported in UnreportedNotApplicableCount .

OperationStartTime (datetime) --
The time the most recent patching operation was started on the instance.

OperationEndTime (datetime) --
The time the most recent patching operation completed on the instance.

Operation (string) --
The type of patching operation that was performed: SCAN (assess patch compliance state) or INSTALL (install missing patches).

LastNoRebootInstallOperationTime (datetime) --
The time of the last attempt to patch the instance with NoReboot specified as the reboot option.

RebootOption (string) --
Indicates the reboot option specified in the patch baseline.

Note
Reboot options apply to Install operations only. Reboots are not attempted for Patch Manager Scan operations.


RebootIfNeeded : Patch Manager tries to reboot the instance if it installed any patches, or if any patches are detected with a status of InstalledPendingReboot .
NoReboot : Patch Manager attempts to install missing packages without trying to reboot the system. Patches installed with this option are assigned a status of InstalledPendingReboot . These patches might not be in effect until a reboot is performed.






NextToken (string) --
The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.







Exceptions

SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.InvalidFilter
SSM.Client.exceptions.InvalidNextToken


    :return: {
        'InstancePatchStates': [
            {
                'InstanceId': 'string',
                'PatchGroup': 'string',
                'BaselineId': 'string',
                'SnapshotId': 'string',
                'InstallOverrideList': 'string',
                'OwnerInformation': 'string',
                'InstalledCount': 123,
                'InstalledOtherCount': 123,
                'InstalledPendingRebootCount': 123,
                'InstalledRejectedCount': 123,
                'MissingCount': 123,
                'FailedCount': 123,
                'UnreportedNotApplicableCount': 123,
                'NotApplicableCount': 123,
                'OperationStartTime': datetime(2015, 1, 1),
                'OperationEndTime': datetime(2015, 1, 1),
                'Operation': 'Scan'|'Install',
                'LastNoRebootInstallOperationTime': datetime(2015, 1, 1),
                'RebootOption': 'RebootIfNeeded'|'NoReboot'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    RebootIfNeeded : Patch Manager tries to reboot the instance if it installed any patches, or if any patches are detected with a status of InstalledPendingReboot .
    NoReboot : Patch Manager attempts to install missing packages without trying to reboot the system. Patches installed with this option are assigned a status of InstalledPendingReboot . These patches might not be in effect until a reboot is performed.
    
    """
    pass

def describe_instance_patches(InstanceId=None, Filters=None, NextToken=None, MaxResults=None):
    """
    Retrieves information about the patches on the specified instance and their state relative to the patch baseline being used for the instance.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param InstanceId: [REQUIRED]\nThe ID of the instance whose patch state information should be retrieved.\n

    :type Filters: list
    :param Filters: An array of structures. Each entry in the array is a structure containing a Key, Value combination. Valid values for Key are Classification | KBId | Severity | State .\n\n(dict) --Defines a filter used in Patch Manager APIs.\n\nKey (string) --The key for the filter.\n\nValues (list) --The value for the filter.\n\n(string) --\n\n\n\n\n\n

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :type MaxResults: integer
    :param MaxResults: The maximum number of patches to return (per page).

    :rtype: dict

ReturnsResponse Syntax
{
    'Patches': [
        {
            'Title': 'string',
            'KBId': 'string',
            'Classification': 'string',
            'Severity': 'string',
            'State': 'INSTALLED'|'INSTALLED_OTHER'|'INSTALLED_PENDING_REBOOT'|'INSTALLED_REJECTED'|'MISSING'|'NOT_APPLICABLE'|'FAILED',
            'InstalledTime': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Patches (list) --
Each entry in the array is a structure containing:
Title (string)
KBId (string)
Classification (string)
Severity (string)
State (string, such as "INSTALLED" or "FAILED")
InstalledTime (DateTime)
InstalledBy (string)

(dict) --
Information about the state of a patch on a particular instance as it relates to the patch baseline used to patch the instance.

Title (string) --
The title of the patch.

KBId (string) --
The operating system-specific ID of the patch.

Classification (string) --
The classification of the patch (for example, SecurityUpdates, Updates, CriticalUpdates).

Severity (string) --
The severity of the patch (for example, Critical, Important, Moderate).

State (string) --
The state of the patch on the instance, such as INSTALLED or FAILED.
For descriptions of each patch state, see About patch compliance in the AWS Systems Manager User Guide .

InstalledTime (datetime) --
The date/time the patch was installed on the instance. Note that not all operating systems provide this level of information.





NextToken (string) --
The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.







Exceptions

SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.InvalidInstanceId
SSM.Client.exceptions.InvalidFilter
SSM.Client.exceptions.InvalidNextToken


    :return: {
        'Patches': [
            {
                'Title': 'string',
                'KBId': 'string',
                'Classification': 'string',
                'Severity': 'string',
                'State': 'INSTALLED'|'INSTALLED_OTHER'|'INSTALLED_PENDING_REBOOT'|'INSTALLED_REJECTED'|'MISSING'|'NOT_APPLICABLE'|'FAILED',
                'InstalledTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    SSM.Client.exceptions.InternalServerError
    SSM.Client.exceptions.InvalidInstanceId
    SSM.Client.exceptions.InvalidFilter
    SSM.Client.exceptions.InvalidNextToken
    
    """
    pass

def describe_inventory_deletions(DeletionId=None, NextToken=None, MaxResults=None):
    """
    Describes a specific delete inventory operation.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_inventory_deletions(
        DeletionId='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type DeletionId: string
    :param DeletionId: Specify the delete inventory ID for which you want information. This ID was returned by the DeleteInventory action.

    :type NextToken: string
    :param NextToken: A token to start the list. Use this token to get the next set of results.

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'InventoryDeletions': [
        {
            'DeletionId': 'string',
            'TypeName': 'string',
            'DeletionStartTime': datetime(2015, 1, 1),
            'LastStatus': 'InProgress'|'Complete',
            'LastStatusMessage': 'string',
            'DeletionSummary': {
                'TotalCount': 123,
                'RemainingCount': 123,
                'SummaryItems': [
                    {
                        'Version': 'string',
                        'Count': 123,
                        'RemainingCount': 123
                    },
                ]
            },
            'LastStatusUpdateTime': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

InventoryDeletions (list) --
A list of status items for deleted inventory.

(dict) --
Status information returned by the DeleteInventory action.

DeletionId (string) --
The deletion ID returned by the DeleteInventory action.

TypeName (string) --
The name of the inventory data type.

DeletionStartTime (datetime) --
The UTC timestamp when the delete operation started.

LastStatus (string) --
The status of the operation. Possible values are InProgress and Complete.

LastStatusMessage (string) --
Information about the status.

DeletionSummary (dict) --
Information about the delete operation. For more information about this summary, see Understanding the delete inventory summary in the AWS Systems Manager User Guide .

TotalCount (integer) --
The total number of items to delete. This count does not change during the delete operation.

RemainingCount (integer) --
Remaining number of items to delete.

SummaryItems (list) --
A list of counts and versions for deleted items.

(dict) --
Either a count, remaining count, or a version number in a delete inventory summary.

Version (string) --
The inventory type version.

Count (integer) --
A count of the number of deleted items.

RemainingCount (integer) --
The remaining number of items to delete.







LastStatusUpdateTime (datetime) --
The UTC timestamp of when the last status report.





NextToken (string) --
The token for the next set of items to return. Use this token to get the next set of results.







Exceptions

SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.InvalidDeletionIdException
SSM.Client.exceptions.InvalidNextToken


    :return: {
        'InventoryDeletions': [
            {
                'DeletionId': 'string',
                'TypeName': 'string',
                'DeletionStartTime': datetime(2015, 1, 1),
                'LastStatus': 'InProgress'|'Complete',
                'LastStatusMessage': 'string',
                'DeletionSummary': {
                    'TotalCount': 123,
                    'RemainingCount': 123,
                    'SummaryItems': [
                        {
                            'Version': 'string',
                            'Count': 123,
                            'RemainingCount': 123
                        },
                    ]
                },
                'LastStatusUpdateTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    SSM.Client.exceptions.InternalServerError
    SSM.Client.exceptions.InvalidDeletionIdException
    SSM.Client.exceptions.InvalidNextToken
    
    """
    pass

def describe_maintenance_window_execution_task_invocations(WindowExecutionId=None, TaskId=None, Filters=None, MaxResults=None, NextToken=None):
    """
    Retrieves the individual task executions (one per target) for a particular task run as part of a maintenance window execution.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param WindowExecutionId: [REQUIRED]\nThe ID of the maintenance window execution the task is part of.\n

    :type TaskId: string
    :param TaskId: [REQUIRED]\nThe ID of the specific task in the maintenance window task that should be retrieved.\n

    :type Filters: list
    :param Filters: Optional filters used to scope down the returned task invocations. The supported filter key is STATUS with the corresponding values PENDING, IN_PROGRESS, SUCCESS, FAILED, TIMED_OUT, CANCELLING, and CANCELLED.\n\n(dict) --Filter used in the request. Supported filter keys are Name and Enabled.\n\nKey (string) --The name of the filter.\n\nValues (list) --The filter values.\n\n(string) --\n\n\n\n\n\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

WindowExecutionTaskInvocationIdentities (list) --
Information about the task invocation results per invocation.

(dict) --
Describes the information about a task invocation for a particular target as part of a task execution performed as part of a maintenance window execution.

WindowExecutionId (string) --
The ID of the maintenance window execution that ran the task.

TaskExecutionId (string) --
The ID of the specific task execution in the maintenance window execution.

InvocationId (string) --
The ID of the task invocation.

ExecutionId (string) --
The ID of the action performed in the service that actually handled the task invocation. If the task type is RUN_COMMAND, this value is the command ID.

TaskType (string) --
The task type.

Parameters (string) --
The parameters that were provided for the invocation when it was run.

Status (string) --
The status of the task invocation.

StatusDetails (string) --
The details explaining the status of the task invocation. Only available for certain Status values.

StartTime (datetime) --
The time the invocation started.

EndTime (datetime) --
The time the invocation finished.

OwnerInformation (string) --
User-provided value that was specified when the target was registered with the maintenance window. This was also included in any CloudWatch events raised during the task invocation.

WindowTargetId (string) --
The ID of the target definition in this maintenance window the invocation was performed for.





NextToken (string) --
The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.







Exceptions

SSM.Client.exceptions.DoesNotExistException
SSM.Client.exceptions.InternalServerError


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
    
    
    :returns: 
    SSM.Client.exceptions.DoesNotExistException
    SSM.Client.exceptions.InternalServerError
    
    """
    pass

def describe_maintenance_window_execution_tasks(WindowExecutionId=None, Filters=None, MaxResults=None, NextToken=None):
    """
    For a given maintenance window execution, lists the tasks that were run.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param WindowExecutionId: [REQUIRED]\nThe ID of the maintenance window execution whose task executions should be retrieved.\n

    :type Filters: list
    :param Filters: Optional filters used to scope down the returned tasks. The supported filter key is STATUS with the corresponding values PENDING, IN_PROGRESS, SUCCESS, FAILED, TIMED_OUT, CANCELLING, and CANCELLED.\n\n(dict) --Filter used in the request. Supported filter keys are Name and Enabled.\n\nKey (string) --The name of the filter.\n\nValues (list) --The filter values.\n\n(string) --\n\n\n\n\n\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

WindowExecutionTaskIdentities (list) --
Information about the task executions.

(dict) --
Information about a task execution performed as part of a maintenance window execution.

WindowExecutionId (string) --
The ID of the maintenance window execution that ran the task.

TaskExecutionId (string) --
The ID of the specific task execution in the maintenance window execution.

Status (string) --
The status of the task execution.

StatusDetails (string) --
The details explaining the status of the task execution. Only available for certain status values.

StartTime (datetime) --
The time the task execution started.

EndTime (datetime) --
The time the task execution finished.

TaskArn (string) --
The ARN of the task that ran.

TaskType (string) --
The type of task that ran.





NextToken (string) --
The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.







Exceptions

SSM.Client.exceptions.DoesNotExistException
SSM.Client.exceptions.InternalServerError


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
    
    
    :returns: 
    SSM.Client.exceptions.DoesNotExistException
    SSM.Client.exceptions.InternalServerError
    
    """
    pass

def describe_maintenance_window_executions(WindowId=None, Filters=None, MaxResults=None, NextToken=None):
    """
    Lists the executions of a maintenance window. This includes information about when the maintenance window was scheduled to be active, and information about tasks registered and run with the maintenance window.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param WindowId: [REQUIRED]\nThe ID of the maintenance window whose executions should be retrieved.\n

    :type Filters: list
    :param Filters: Each entry in the array is a structure containing:\nKey (string, between 1 and 128 characters)\nValues (array of strings, each string is between 1 and 256 characters)\nThe supported Keys are ExecutedBefore and ExecutedAfter with the value being a date/time string such as 2016-11-04T05:00:00Z.\n\n(dict) --Filter used in the request. Supported filter keys are Name and Enabled.\n\nKey (string) --The name of the filter.\n\nValues (list) --The filter values.\n\n(string) --\n\n\n\n\n\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

WindowExecutions (list) --
Information about the maintenance window executions.

(dict) --
Describes the information about an execution of a maintenance window.

WindowId (string) --
The ID of the maintenance window.

WindowExecutionId (string) --
The ID of the maintenance window execution.

Status (string) --
The status of the execution.

StatusDetails (string) --
The details explaining the Status. Only available for certain status values.

StartTime (datetime) --
The time the execution started.

EndTime (datetime) --
The time the execution finished.





NextToken (string) --
The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.







Exceptions

SSM.Client.exceptions.InternalServerError


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
    
    
    :returns: 
    SSM.Client.exceptions.InternalServerError
    
    """
    pass

def describe_maintenance_window_schedule(WindowId=None, Targets=None, ResourceType=None, Filters=None, MaxResults=None, NextToken=None):
    """
    Retrieves information about upcoming executions of a maintenance window.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_maintenance_window_schedule(
        WindowId='string',
        Targets=[
            {
                'Key': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        ResourceType='INSTANCE'|'RESOURCE_GROUP',
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
    :param WindowId: The ID of the maintenance window to retrieve information about.

    :type Targets: list
    :param Targets: The instance ID or key/value pair to retrieve information about.\n\n(dict) --An array of search criteria that targets instances using a Key,Value combination that you specify.\nSupported formats include the following.\n\n``Key=InstanceIds,Values=*instance-id-1* ,*instance-id-2* ,*instance-id-3* ``\n``Key=tag:my-tag-key ,Values=*my-tag-value-1* ,*my-tag-value-2* ``\n``Key=tag-key,Values=*my-tag-key-1* ,*my-tag-key-2* ``\n(Maintenance window targets only) ``Key=resource-groups:Name,Values=*resource-group-name* ``\n(Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*resource-type-1* ,*resource-type-2* ``\n\nFor example:\n\nKey=InstanceIds,Values=i-02573cafcfEXAMPLE,i-0471e04240EXAMPLE,i-07782c72faEXAMPLE\nKey=tag:CostCenter,Values=CostCenter1,CostCenter2,CostCenter3\nKey=tag-key,Values=Name,Instance-Type,CostCenter\n(Maintenance window targets only) Key=resource-groups:Name,Values=ProductionResourceGroup  This example demonstrates how to target all resources in the resource group ProductionResourceGroup in your maintenance window.\n(Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*AWS::EC2::INSTANCE* ,*AWS::EC2::VPC* ``  This example demonstrates how to target only EC2 instances and VPCs in your maintenance window.\n(State Manager association targets only) Key=InstanceIds,Values=*  This example demonstrates how to target all managed instances in the AWS Region where the association was created.\n\nFor information about how to send commands that target instances using Key,Value parameters, see Targeting multiple instances in the AWS Systems Manager User Guide .\n\nKey (string) --User-defined criteria for sending commands that target instances that meet the criteria.\n\nValues (list) --User-defined criteria that maps to Key . For example, if you specified tag:ServerRole , you could specify value:WebServer to run a command on instances that include EC2 tags of ServerRole,WebServer .\n\n(string) --\n\n\n\n\n\n

    :type ResourceType: string
    :param ResourceType: The type of resource you want to retrieve information about. For example, 'INSTANCE'.

    :type Filters: list
    :param Filters: Filters used to limit the range of results. For example, you can limit maintenance window executions to only those scheduled before or after a certain date and time.\n\n(dict) --Defines a filter used in Patch Manager APIs.\n\nKey (string) --The key for the filter.\n\nValues (list) --The value for the filter.\n\n(string) --\n\n\n\n\n\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :rtype: dict

ReturnsResponse Syntax
{
    'ScheduledWindowExecutions': [
        {
            'WindowId': 'string',
            'Name': 'string',
            'ExecutionTime': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

ScheduledWindowExecutions (list) --
Information about maintenance window executions scheduled for the specified time range.

(dict) --
Information about a scheduled execution for a maintenance window.

WindowId (string) --
The ID of the maintenance window to be run.

Name (string) --
The name of the maintenance window to be run.

ExecutionTime (string) --
The time, in ISO-8601 Extended format, that the maintenance window is scheduled to be run.





NextToken (string) --
The token for the next set of items to return. (You use this token in the next call.)







Exceptions

SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.DoesNotExistException


    :return: {
        'ScheduledWindowExecutions': [
            {
                'WindowId': 'string',
                'Name': 'string',
                'ExecutionTime': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    SSM.Client.exceptions.InternalServerError
    SSM.Client.exceptions.DoesNotExistException
    
    """
    pass

def describe_maintenance_window_targets(WindowId=None, Filters=None, MaxResults=None, NextToken=None):
    """
    Lists the targets registered with the maintenance window.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param WindowId: [REQUIRED]\nThe ID of the maintenance window whose targets should be retrieved.\n

    :type Filters: list
    :param Filters: Optional filters that can be used to narrow down the scope of the returned window targets. The supported filter keys are Type, WindowTargetId and OwnerInformation.\n\n(dict) --Filter used in the request. Supported filter keys are Name and Enabled.\n\nKey (string) --The name of the filter.\n\nValues (list) --The filter values.\n\n(string) --\n\n\n\n\n\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :rtype: dict

ReturnsResponse Syntax
{
    'Targets': [
        {
            'WindowId': 'string',
            'WindowTargetId': 'string',
            'ResourceType': 'INSTANCE'|'RESOURCE_GROUP',
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


Response Structure

(dict) --

Targets (list) --
Information about the targets in the maintenance window.

(dict) --
The target registered with the maintenance window.

WindowId (string) --
The ID of the maintenance window to register the target with.

WindowTargetId (string) --
The ID of the target.

ResourceType (string) --
The type of target that is being registered with the maintenance window.

Targets (list) --
The targets, either instances or tags.
Specify instances using the following format:

Key=instanceids,Values=<instanceid1>,<instanceid2>

Tags are specified using the following format:

Key=<tag name>,Values=<tag value> .


(dict) --
An array of search criteria that targets instances using a Key,Value combination that you specify.
Supported formats include the following.

``Key=InstanceIds,Values=*instance-id-1* ,*instance-id-2* ,*instance-id-3* ``
``Key=tag:my-tag-key ,Values=*my-tag-value-1* ,*my-tag-value-2* ``
``Key=tag-key,Values=*my-tag-key-1* ,*my-tag-key-2* ``
(Maintenance window targets only) ``Key=resource-groups:Name,Values=*resource-group-name* ``
(Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*resource-type-1* ,*resource-type-2* ``

For example:

Key=InstanceIds,Values=i-02573cafcfEXAMPLE,i-0471e04240EXAMPLE,i-07782c72faEXAMPLE
Key=tag:CostCenter,Values=CostCenter1,CostCenter2,CostCenter3
Key=tag-key,Values=Name,Instance-Type,CostCenter
(Maintenance window targets only) Key=resource-groups:Name,Values=ProductionResourceGroup   This example demonstrates how to target all resources in the resource group ProductionResourceGroup in your maintenance window.
(Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*AWS::EC2::INSTANCE* ,*AWS::EC2::VPC* ``   This example demonstrates how to target only EC2 instances and VPCs in your maintenance window.
(State Manager association targets only) Key=InstanceIds,Values=*   This example demonstrates how to target all managed instances in the AWS Region where the association was created.

For information about how to send commands that target instances using Key,Value parameters, see Targeting multiple instances in the AWS Systems Manager User Guide .

Key (string) --
User-defined criteria for sending commands that target instances that meet the criteria.

Values (list) --
User-defined criteria that maps to Key . For example, if you specified tag:ServerRole , you could specify value:WebServer to run a command on instances that include EC2 tags of ServerRole,WebServer .

(string) --






OwnerInformation (string) --
A user-provided value that will be included in any CloudWatch events that are raised while running tasks for these targets in this maintenance window.

Name (string) --
The name for the maintenance window target.

Description (string) --
A description for the target.





NextToken (string) --
The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.







Exceptions

SSM.Client.exceptions.DoesNotExistException
SSM.Client.exceptions.InternalServerError


    :return: {
        'Targets': [
            {
                'WindowId': 'string',
                'WindowTargetId': 'string',
                'ResourceType': 'INSTANCE'|'RESOURCE_GROUP',
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
    ``Key=InstanceIds,Values=*instance-id-1* ,*instance-id-2* ,*instance-id-3* ``
    ``Key=tag:my-tag-key ,Values=*my-tag-value-1* ,*my-tag-value-2* ``
    ``Key=tag-key,Values=*my-tag-key-1* ,*my-tag-key-2* ``
    (Maintenance window targets only) ``Key=resource-groups:Name,Values=*resource-group-name* ``
    (Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*resource-type-1* ,*resource-type-2* ``
    
    """
    pass

def describe_maintenance_window_tasks(WindowId=None, Filters=None, MaxResults=None, NextToken=None):
    """
    Lists the tasks in a maintenance window.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param WindowId: [REQUIRED]\nThe ID of the maintenance window whose tasks should be retrieved.\n

    :type Filters: list
    :param Filters: Optional filters used to narrow down the scope of the returned tasks. The supported filter keys are WindowTaskId, TaskArn, Priority, and TaskType.\n\n(dict) --Filter used in the request. Supported filter keys are Name and Enabled.\n\nKey (string) --The name of the filter.\n\nValues (list) --The filter values.\n\n(string) --\n\n\n\n\n\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

Tasks (list) --
Information about the tasks in the maintenance window.

(dict) --
Information about a task defined for a maintenance window.

WindowId (string) --
The ID of the maintenance window where the task is registered.

WindowTaskId (string) --
The task ID.

TaskArn (string) --
The resource that the task uses during execution. For RUN_COMMAND and AUTOMATION task types, TaskArn is the Systems Manager document name or ARN. For LAMBDA tasks, it\'s the function name or ARN. For STEP_FUNCTIONS tasks, it\'s the state machine ARN.

Type (string) --
The type of task. The type can be one of the following: RUN_COMMAND, AUTOMATION, LAMBDA, or STEP_FUNCTIONS.

Targets (list) --
The targets (either instances or tags). Instances are specified using Key=instanceids,Values=<instanceid1>,<instanceid2>. Tags are specified using Key=<tag name>,Values=<tag value>.

(dict) --
An array of search criteria that targets instances using a Key,Value combination that you specify.
Supported formats include the following.

``Key=InstanceIds,Values=*instance-id-1* ,*instance-id-2* ,*instance-id-3* ``
``Key=tag:my-tag-key ,Values=*my-tag-value-1* ,*my-tag-value-2* ``
``Key=tag-key,Values=*my-tag-key-1* ,*my-tag-key-2* ``
(Maintenance window targets only) ``Key=resource-groups:Name,Values=*resource-group-name* ``
(Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*resource-type-1* ,*resource-type-2* ``

For example:

Key=InstanceIds,Values=i-02573cafcfEXAMPLE,i-0471e04240EXAMPLE,i-07782c72faEXAMPLE
Key=tag:CostCenter,Values=CostCenter1,CostCenter2,CostCenter3
Key=tag-key,Values=Name,Instance-Type,CostCenter
(Maintenance window targets only) Key=resource-groups:Name,Values=ProductionResourceGroup   This example demonstrates how to target all resources in the resource group ProductionResourceGroup in your maintenance window.
(Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*AWS::EC2::INSTANCE* ,*AWS::EC2::VPC* ``   This example demonstrates how to target only EC2 instances and VPCs in your maintenance window.
(State Manager association targets only) Key=InstanceIds,Values=*   This example demonstrates how to target all managed instances in the AWS Region where the association was created.

For information about how to send commands that target instances using Key,Value parameters, see Targeting multiple instances in the AWS Systems Manager User Guide .

Key (string) --
User-defined criteria for sending commands that target instances that meet the criteria.

Values (list) --
User-defined criteria that maps to Key . For example, if you specified tag:ServerRole , you could specify value:WebServer to run a command on instances that include EC2 tags of ServerRole,WebServer .

(string) --






TaskParameters (dict) --
The parameters that should be passed to the task when it is run.

Note
TaskParameters has been deprecated. To specify parameters to pass to a task when it runs, instead use the Parameters option in the TaskInvocationParameters structure. For information about how Systems Manager handles these options for the supported maintenance window task types, see  MaintenanceWindowTaskInvocationParameters .


(string) --

(dict) --
Defines the values for a task parameter.

Values (list) --
This field contains an array of 0 or more strings, each 1 to 255 characters in length.

(string) --








Priority (integer) --
The priority of the task in the maintenance window. The lower the number, the higher the priority. Tasks that have the same priority are scheduled in parallel.

LoggingInfo (dict) --
Information about an S3 bucket to write task-level logs to.

Note
LoggingInfo has been deprecated. To specify an S3 bucket to contain logs, instead use the OutputS3BucketName and OutputS3KeyPrefix options in the TaskInvocationParameters structure. For information about how Systems Manager handles these options for the supported maintenance window task types, see  MaintenanceWindowTaskInvocationParameters .


S3BucketName (string) --
The name of an S3 bucket where execution logs are stored .

S3KeyPrefix (string) --
(Optional) The S3 bucket subfolder.

S3Region (string) --
The Region where the S3 bucket is located.



ServiceRoleArn (string) --
The ARN of the IAM service role to use to publish Amazon Simple Notification Service (Amazon SNS) notifications for maintenance window Run Command tasks.

MaxConcurrency (string) --
The maximum number of targets this task can be run for, in parallel.

MaxErrors (string) --
The maximum number of errors allowed before this task stops being scheduled.

Name (string) --
The task name.

Description (string) --
A description of the task.





NextToken (string) --
The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.







Exceptions

SSM.Client.exceptions.DoesNotExistException
SSM.Client.exceptions.InternalServerError


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
    ``Key=InstanceIds,Values=*instance-id-1* ,*instance-id-2* ,*instance-id-3* ``
    ``Key=tag:my-tag-key ,Values=*my-tag-value-1* ,*my-tag-value-2* ``
    ``Key=tag-key,Values=*my-tag-key-1* ,*my-tag-key-2* ``
    (Maintenance window targets only) ``Key=resource-groups:Name,Values=*resource-group-name* ``
    (Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*resource-type-1* ,*resource-type-2* ``
    
    """
    pass

def describe_maintenance_windows(Filters=None, MaxResults=None, NextToken=None):
    """
    Retrieves the maintenance windows in an AWS account.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param Filters: Optional filters used to narrow down the scope of the returned maintenance windows. Supported filter keys are Name and Enabled .\n\n(dict) --Filter used in the request. Supported filter keys are Name and Enabled.\n\nKey (string) --The name of the filter.\n\nValues (list) --The filter values.\n\n(string) --\n\n\n\n\n\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :rtype: dict

ReturnsResponse Syntax
{
    'WindowIdentities': [
        {
            'WindowId': 'string',
            'Name': 'string',
            'Description': 'string',
            'Enabled': True|False,
            'Duration': 123,
            'Cutoff': 123,
            'Schedule': 'string',
            'ScheduleTimezone': 'string',
            'EndDate': 'string',
            'StartDate': 'string',
            'NextExecutionTime': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

WindowIdentities (list) --
Information about the maintenance windows.

(dict) --
Information about the maintenance window.

WindowId (string) --
The ID of the maintenance window.

Name (string) --
The name of the maintenance window.

Description (string) --
A description of the maintenance window.

Enabled (boolean) --
Indicates whether the maintenance window is enabled.

Duration (integer) --
The duration of the maintenance window in hours.

Cutoff (integer) --
The number of hours before the end of the maintenance window that Systems Manager stops scheduling new tasks for execution.

Schedule (string) --
The schedule of the maintenance window in the form of a cron or rate expression.

ScheduleTimezone (string) --
The time zone that the scheduled maintenance window executions are based on, in Internet Assigned Numbers Authority (IANA) format.

EndDate (string) --
The date and time, in ISO-8601 Extended format, for when the maintenance window is scheduled to become inactive.

StartDate (string) --
The date and time, in ISO-8601 Extended format, for when the maintenance window is scheduled to become active.

NextExecutionTime (string) --
The next time the maintenance window will actually run, taking into account any specified times for the maintenance window to become active or inactive.





NextToken (string) --
The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.







Exceptions

SSM.Client.exceptions.InternalServerError


    :return: {
        'WindowIdentities': [
            {
                'WindowId': 'string',
                'Name': 'string',
                'Description': 'string',
                'Enabled': True|False,
                'Duration': 123,
                'Cutoff': 123,
                'Schedule': 'string',
                'ScheduleTimezone': 'string',
                'EndDate': 'string',
                'StartDate': 'string',
                'NextExecutionTime': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    SSM.Client.exceptions.InternalServerError
    
    """
    pass

def describe_maintenance_windows_for_target(Targets=None, ResourceType=None, MaxResults=None, NextToken=None):
    """
    Retrieves information about the maintenance window targets or tasks that an instance is associated with.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_maintenance_windows_for_target(
        Targets=[
            {
                'Key': 'string',
                'Values': [
                    'string',
                ]
            },
        ],
        ResourceType='INSTANCE'|'RESOURCE_GROUP',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type Targets: list
    :param Targets: [REQUIRED]\nThe instance ID or key/value pair to retrieve information about.\n\n(dict) --An array of search criteria that targets instances using a Key,Value combination that you specify.\nSupported formats include the following.\n\n``Key=InstanceIds,Values=*instance-id-1* ,*instance-id-2* ,*instance-id-3* ``\n``Key=tag:my-tag-key ,Values=*my-tag-value-1* ,*my-tag-value-2* ``\n``Key=tag-key,Values=*my-tag-key-1* ,*my-tag-key-2* ``\n(Maintenance window targets only) ``Key=resource-groups:Name,Values=*resource-group-name* ``\n(Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*resource-type-1* ,*resource-type-2* ``\n\nFor example:\n\nKey=InstanceIds,Values=i-02573cafcfEXAMPLE,i-0471e04240EXAMPLE,i-07782c72faEXAMPLE\nKey=tag:CostCenter,Values=CostCenter1,CostCenter2,CostCenter3\nKey=tag-key,Values=Name,Instance-Type,CostCenter\n(Maintenance window targets only) Key=resource-groups:Name,Values=ProductionResourceGroup  This example demonstrates how to target all resources in the resource group ProductionResourceGroup in your maintenance window.\n(Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*AWS::EC2::INSTANCE* ,*AWS::EC2::VPC* ``  This example demonstrates how to target only EC2 instances and VPCs in your maintenance window.\n(State Manager association targets only) Key=InstanceIds,Values=*  This example demonstrates how to target all managed instances in the AWS Region where the association was created.\n\nFor information about how to send commands that target instances using Key,Value parameters, see Targeting multiple instances in the AWS Systems Manager User Guide .\n\nKey (string) --User-defined criteria for sending commands that target instances that meet the criteria.\n\nValues (list) --User-defined criteria that maps to Key . For example, if you specified tag:ServerRole , you could specify value:WebServer to run a command on instances that include EC2 tags of ServerRole,WebServer .\n\n(string) --\n\n\n\n\n\n

    :type ResourceType: string
    :param ResourceType: [REQUIRED]\nThe type of resource you want to retrieve information about. For example, 'INSTANCE'.\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :rtype: dict

ReturnsResponse Syntax
{
    'WindowIdentities': [
        {
            'WindowId': 'string',
            'Name': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

WindowIdentities (list) --
Information about the maintenance window targets and tasks an instance is associated with.

(dict) --
The maintenance window to which the specified target belongs.

WindowId (string) --
The ID of the maintenance window.

Name (string) --
The name of the maintenance window.





NextToken (string) --
The token for the next set of items to return. (You use this token in the next call.)







Exceptions

SSM.Client.exceptions.InternalServerError


    :return: {
        'WindowIdentities': [
            {
                'WindowId': 'string',
                'Name': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    SSM.Client.exceptions.InternalServerError
    
    """
    pass

def describe_ops_items(OpsItemFilters=None, MaxResults=None, NextToken=None):
    """
    Query a set of OpsItems. You must have permission in AWS Identity and Access Management (IAM) to query a list of OpsItems. For more information, see Getting started with OpsCenter in the AWS Systems Manager User Guide .
    Operations engineers and IT professionals use OpsCenter to view, investigate, and remediate operational issues impacting the performance and health of their AWS resources. For more information, see AWS Systems Manager OpsCenter in the AWS Systems Manager User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_ops_items(
        OpsItemFilters=[
            {
                'Key': 'Status'|'CreatedBy'|'Source'|'Priority'|'Title'|'OpsItemId'|'CreatedTime'|'LastModifiedTime'|'OperationalData'|'OperationalDataKey'|'OperationalDataValue'|'ResourceId'|'AutomationId'|'Category'|'Severity',
                'Values': [
                    'string',
                ],
                'Operator': 'Equal'|'Contains'|'GreaterThan'|'LessThan'
            },
        ],
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type OpsItemFilters: list
    :param OpsItemFilters: One or more filters to limit the response.\n\nKey: CreatedTime Operations: GreaterThan, LessThan\nKey: LastModifiedBy Operations: Contains, Equals\nKey: LastModifiedTime Operations: GreaterThan, LessThan\nKey: Priority Operations: Equals\nKey: Source Operations: Contains, Equals\nKey: Status Operations: Equals\nKey: Title Operations: Contains\nKey: OperationalData* Operations: Equals\nKey: OperationalDataKey Operations: Equals\nKey: OperationalDataValue Operations: Equals, Contains\nKey: OpsItemId Operations: Equals\nKey: ResourceId Operations: Contains\nKey: AutomationId Operations: Equals\n\n*If you filter the response by using the OperationalData operator, specify a key-value pair by using the following JSON format: {'key':'key_name','value':'a_value'}\n\n(dict) --Describes an OpsItem filter.\n\nKey (string) -- [REQUIRED]The name of the filter.\n\nValues (list) -- [REQUIRED]The filter value.\n\n(string) --\n\n\nOperator (string) -- [REQUIRED]The operator used by the filter call.\n\n\n\n\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :type NextToken: string
    :param NextToken: A token to start the list. Use this token to get the next set of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'NextToken': 'string',
    'OpsItemSummaries': [
        {
            'CreatedBy': 'string',
            'CreatedTime': datetime(2015, 1, 1),
            'LastModifiedBy': 'string',
            'LastModifiedTime': datetime(2015, 1, 1),
            'Priority': 123,
            'Source': 'string',
            'Status': 'Open'|'InProgress'|'Resolved',
            'OpsItemId': 'string',
            'Title': 'string',
            'OperationalData': {
                'string': {
                    'Value': 'string',
                    'Type': 'SearchableString'|'String'
                }
            },
            'Category': 'string',
            'Severity': 'string'
        },
    ]
}


Response Structure

(dict) --

NextToken (string) --
The token for the next set of items to return. Use this token to get the next set of results.

OpsItemSummaries (list) --
A list of OpsItems.

(dict) --
A count of OpsItems.

CreatedBy (string) --
The Amazon Resource Name (ARN) of the IAM entity that created the OpsItem.

CreatedTime (datetime) --
The date and time the OpsItem was created.

LastModifiedBy (string) --
The Amazon Resource Name (ARN) of the IAM entity that created the OpsItem.

LastModifiedTime (datetime) --
The date and time the OpsItem was last updated.

Priority (integer) --
The importance of this OpsItem in relation to other OpsItems in the system.

Source (string) --
The impacted AWS resource.

Status (string) --
The OpsItem status. Status can be Open , In Progress , or Resolved .

OpsItemId (string) --
The ID of the OpsItem.

Title (string) --
A short heading that describes the nature of the OpsItem and the impacted resource.

OperationalData (dict) --
Operational data is custom data that provides useful reference details about the OpsItem.

(string) --

(dict) --
An object that defines the value of the key and its type in the OperationalData map.

Value (string) --
The value of the OperationalData key.

Type (string) --
The type of key-value pair. Valid types include SearchableString and String .







Category (string) --
A list of OpsItems by category.

Severity (string) --
A list of OpsItems by severity.











Exceptions

SSM.Client.exceptions.InternalServerError


    :return: {
        'NextToken': 'string',
        'OpsItemSummaries': [
            {
                'CreatedBy': 'string',
                'CreatedTime': datetime(2015, 1, 1),
                'LastModifiedBy': 'string',
                'LastModifiedTime': datetime(2015, 1, 1),
                'Priority': 123,
                'Source': 'string',
                'Status': 'Open'|'InProgress'|'Resolved',
                'OpsItemId': 'string',
                'Title': 'string',
                'OperationalData': {
                    'string': {
                        'Value': 'string',
                        'Type': 'SearchableString'|'String'
                    }
                },
                'Category': 'string',
                'Severity': 'string'
            },
        ]
    }
    
    
    :returns: 
    SSM.Client.exceptions.InternalServerError
    
    """
    pass

def describe_parameters(Filters=None, ParameterFilters=None, MaxResults=None, NextToken=None):
    """
    Get information about a parameter.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param Filters: This data type is deprecated. Instead, use ParameterFilters .\n\n(dict) --This data type is deprecated. Instead, use ParameterStringFilter .\n\nKey (string) -- [REQUIRED]The name of the filter.\n\nValues (list) -- [REQUIRED]The filter values.\n\n(string) --\n\n\n\n\n\n

    :type ParameterFilters: list
    :param ParameterFilters: Filters to limit the request results.\n\n(dict) --One or more filters. Use a filter to return a more specific list of results.\n\nWarning\nThe ParameterStringFilter object is used by the DescribeParameters and GetParametersByPath API actions. However, not all of the pattern values listed for Key can be used with both actions.\nFor DescribeActions , all of the listed patterns are valid, with the exception of Label .\nFor GetParametersByPath , the following patterns listed for Key are not valid: Name , Path , and Tier .\nFor examples of CLI commands demonstrating valid parameter filter constructions, see Searching for Systems Manager parameters in the AWS Systems Manager User Guide .\n\n\nKey (string) -- [REQUIRED]The name of the filter.\n\nOption (string) --For all filters used with DescribeParameters , valid options include Equals and BeginsWith . The Name filter additionally supports the Contains option. (Exception: For filters using the key Path , valid options include Recursive and OneLevel .)\nFor filters used with GetParametersByPath , valid options include Equals and BeginsWith . (Exception: For filters using the key Label , the only valid option is Equals .)\n\nValues (list) --The value you want to search for.\n\n(string) --\n\n\n\n\n\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :rtype: dict

ReturnsResponse Syntax
{
    'Parameters': [
        {
            'Name': 'string',
            'Type': 'String'|'StringList'|'SecureString',
            'KeyId': 'string',
            'LastModifiedDate': datetime(2015, 1, 1),
            'LastModifiedUser': 'string',
            'Description': 'string',
            'AllowedPattern': 'string',
            'Version': 123,
            'Tier': 'Standard'|'Advanced'|'Intelligent-Tiering',
            'Policies': [
                {
                    'PolicyText': 'string',
                    'PolicyType': 'string',
                    'PolicyStatus': 'string'
                },
            ],
            'DataType': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Parameters (list) --
Parameters returned by the request.

(dict) --
Metadata includes information like the ARN of the last user and the date/time the parameter was last used.

Name (string) --
The parameter name.

Type (string) --
The type of parameter. Valid parameter types include the following: String , StringList , and SecureString .

KeyId (string) --
The ID of the query key used for this parameter.

LastModifiedDate (datetime) --
Date the parameter was last changed or updated.

LastModifiedUser (string) --
Amazon Resource Name (ARN) of the AWS user who last changed the parameter.

Description (string) --
Description of the parameter actions.

AllowedPattern (string) --
A parameter name can include only the following letters and symbols.
a-zA-Z0-9_.-

Version (integer) --
The parameter version.

Tier (string) --
The parameter tier.

Policies (list) --
A list of policies associated with a parameter.

(dict) --
One or more policies assigned to a parameter.

PolicyText (string) --
The JSON text of the policy.

PolicyType (string) --
The type of policy. Parameter Store supports the following policy types: Expiration, ExpirationNotification, and NoChangeNotification.

PolicyStatus (string) --
The status of the policy. Policies report the following statuses: Pending (the policy has not been enforced or applied yet), Finished (the policy was applied), Failed (the policy was not applied), or InProgress (the policy is being applied now).





DataType (string) --
The data type of the parameter, such as text or aws:ec2:image . The default is text .





NextToken (string) --
The token to use when requesting the next set of items.







Exceptions

SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.InvalidFilterKey
SSM.Client.exceptions.InvalidFilterOption
SSM.Client.exceptions.InvalidFilterValue
SSM.Client.exceptions.InvalidNextToken


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
                'Version': 123,
                'Tier': 'Standard'|'Advanced'|'Intelligent-Tiering',
                'Policies': [
                    {
                        'PolicyText': 'string',
                        'PolicyType': 'string',
                        'PolicyStatus': 'string'
                    },
                ],
                'DataType': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    SSM.Client.exceptions.InternalServerError
    SSM.Client.exceptions.InvalidFilterKey
    SSM.Client.exceptions.InvalidFilterOption
    SSM.Client.exceptions.InvalidFilterValue
    SSM.Client.exceptions.InvalidNextToken
    
    """
    pass

def describe_patch_baselines(Filters=None, MaxResults=None, NextToken=None):
    """
    Lists the patch baselines in your AWS account.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param Filters: Each element in the array is a structure containing:\nKey: (string, 'NAME_PREFIX' or 'OWNER')\nValue: (array of strings, exactly 1 entry, between 1 and 255 characters)\n\n(dict) --Defines a filter used in Patch Manager APIs.\n\nKey (string) --The key for the filter.\n\nValues (list) --The value for the filter.\n\n(string) --\n\n\n\n\n\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of patch baselines to return (per page).

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :rtype: dict

ReturnsResponse Syntax
{
    'BaselineIdentities': [
        {
            'BaselineId': 'string',
            'BaselineName': 'string',
            'OperatingSystem': 'WINDOWS'|'AMAZON_LINUX'|'AMAZON_LINUX_2'|'UBUNTU'|'REDHAT_ENTERPRISE_LINUX'|'SUSE'|'CENTOS'|'ORACLE_LINUX'|'DEBIAN',
            'BaselineDescription': 'string',
            'DefaultBaseline': True|False
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

BaselineIdentities (list) --
An array of PatchBaselineIdentity elements.

(dict) --
Defines the basic information about a patch baseline.

BaselineId (string) --
The ID of the patch baseline.

BaselineName (string) --
The name of the patch baseline.

OperatingSystem (string) --
Defines the operating system the patch baseline applies to. The Default value is WINDOWS.

BaselineDescription (string) --
The description of the patch baseline.

DefaultBaseline (boolean) --
Whether this is the default baseline. Note that Systems Manager supports creating multiple default patch baselines. For example, you can create a default patch baseline for each operating system.





NextToken (string) --
The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.







Exceptions

SSM.Client.exceptions.InternalServerError


    :return: {
        'BaselineIdentities': [
            {
                'BaselineId': 'string',
                'BaselineName': 'string',
                'OperatingSystem': 'WINDOWS'|'AMAZON_LINUX'|'AMAZON_LINUX_2'|'UBUNTU'|'REDHAT_ENTERPRISE_LINUX'|'SUSE'|'CENTOS'|'ORACLE_LINUX'|'DEBIAN',
                'BaselineDescription': 'string',
                'DefaultBaseline': True|False
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    SSM.Client.exceptions.InternalServerError
    
    """
    pass

def describe_patch_group_state(PatchGroup=None):
    """
    Returns high-level aggregated patch compliance state for a patch group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_patch_group_state(
        PatchGroup='string'
    )
    
    
    :type PatchGroup: string
    :param PatchGroup: [REQUIRED]\nThe name of the patch group whose patch snapshot should be retrieved.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Instances': 123,
    'InstancesWithInstalledPatches': 123,
    'InstancesWithInstalledOtherPatches': 123,
    'InstancesWithInstalledPendingRebootPatches': 123,
    'InstancesWithInstalledRejectedPatches': 123,
    'InstancesWithMissingPatches': 123,
    'InstancesWithFailedPatches': 123,
    'InstancesWithNotApplicablePatches': 123,
    'InstancesWithUnreportedNotApplicablePatches': 123
}


Response Structure

(dict) --
Instances (integer) --The number of instances in the patch group.

InstancesWithInstalledPatches (integer) --The number of instances with installed patches.

InstancesWithInstalledOtherPatches (integer) --The number of instances with patches installed that aren\'t defined in the patch baseline.

InstancesWithInstalledPendingRebootPatches (integer) --The number of instances with patches installed by Patch Manager that have not been rebooted after the patch installation. The status of these instances is NON_COMPLIANT.

InstancesWithInstalledRejectedPatches (integer) --The number of instances with patches installed that are specified in a RejectedPatches list. Patches with a status of INSTALLED_REJECTED were typically installed before they were added to a RejectedPatches list.

Note
If ALLOW_AS_DEPENDENCY is the specified option for RejectedPatchesAction, the value of InstancesWithInstalledRejectedPatches will always be 0 (zero).


InstancesWithMissingPatches (integer) --The number of instances with missing patches from the patch baseline.

InstancesWithFailedPatches (integer) --The number of instances with patches from the patch baseline that failed to install.

InstancesWithNotApplicablePatches (integer) --The number of instances with patches that aren\'t applicable.

InstancesWithUnreportedNotApplicablePatches (integer) --The number of instances with NotApplicable patches beyond the supported limit, which are not reported by name to Systems Manager Inventory.






Exceptions

SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.InvalidNextToken


    :return: {
        'Instances': 123,
        'InstancesWithInstalledPatches': 123,
        'InstancesWithInstalledOtherPatches': 123,
        'InstancesWithInstalledPendingRebootPatches': 123,
        'InstancesWithInstalledRejectedPatches': 123,
        'InstancesWithMissingPatches': 123,
        'InstancesWithFailedPatches': 123,
        'InstancesWithNotApplicablePatches': 123,
        'InstancesWithUnreportedNotApplicablePatches': 123
    }
    
    
    """
    pass

def describe_patch_groups(MaxResults=None, Filters=None, NextToken=None):
    """
    Lists all patch groups that have been registered with patch baselines.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param Filters: One or more filters. Use a filter to return a more specific list of results.\n\n(dict) --Defines a filter used in Patch Manager APIs.\n\nKey (string) --The key for the filter.\n\nValues (list) --The value for the filter.\n\n(string) --\n\n\n\n\n\n

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :rtype: dict

ReturnsResponse Syntax
{
    'Mappings': [
        {
            'PatchGroup': 'string',
            'BaselineIdentity': {
                'BaselineId': 'string',
                'BaselineName': 'string',
                'OperatingSystem': 'WINDOWS'|'AMAZON_LINUX'|'AMAZON_LINUX_2'|'UBUNTU'|'REDHAT_ENTERPRISE_LINUX'|'SUSE'|'CENTOS'|'ORACLE_LINUX'|'DEBIAN',
                'BaselineDescription': 'string',
                'DefaultBaseline': True|False
            }
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Mappings (list) --
Each entry in the array contains:
PatchGroup: string (between 1 and 256 characters, Regex: ^([p{L}p{Z}p{N}_.:/=+-@]*)$)
PatchBaselineIdentity: A PatchBaselineIdentity element.

(dict) --
The mapping between a patch group and the patch baseline the patch group is registered with.

PatchGroup (string) --
The name of the patch group registered with the patch baseline.

BaselineIdentity (dict) --
The patch baseline the patch group is registered with.

BaselineId (string) --
The ID of the patch baseline.

BaselineName (string) --
The name of the patch baseline.

OperatingSystem (string) --
Defines the operating system the patch baseline applies to. The Default value is WINDOWS.

BaselineDescription (string) --
The description of the patch baseline.

DefaultBaseline (boolean) --
Whether this is the default baseline. Note that Systems Manager supports creating multiple default patch baselines. For example, you can create a default patch baseline for each operating system.







NextToken (string) --
The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.







Exceptions

SSM.Client.exceptions.InternalServerError


    :return: {
        'Mappings': [
            {
                'PatchGroup': 'string',
                'BaselineIdentity': {
                    'BaselineId': 'string',
                    'BaselineName': 'string',
                    'OperatingSystem': 'WINDOWS'|'AMAZON_LINUX'|'AMAZON_LINUX_2'|'UBUNTU'|'REDHAT_ENTERPRISE_LINUX'|'SUSE'|'CENTOS'|'ORACLE_LINUX'|'DEBIAN',
                    'BaselineDescription': 'string',
                    'DefaultBaseline': True|False
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    SSM.Client.exceptions.InternalServerError
    
    """
    pass

def describe_patch_properties(OperatingSystem=None, Property=None, PatchSet=None, MaxResults=None, NextToken=None):
    """
    Lists the properties of available patches organized by product, product family, classification, severity, and other properties of available patches. You can use the reported properties in the filters you specify in requests for actions such as  CreatePatchBaseline ,  UpdatePatchBaseline ,  DescribeAvailablePatches , and  DescribePatchBaselines .
    The following section lists the properties that can be used in filters for each major operating system type:
    Valid properties: PRODUCT, PRODUCT_FAMILY, CLASSIFICATION, MSRC_SEVERITY
    Valid properties: PRODUCT, CLASSIFICATION, SEVERITY
    Valid properties: PRODUCT, CLASSIFICATION, SEVERITY
    Valid properties: PRODUCT, PRIORITY
    Valid properties: PRODUCT, CLASSIFICATION, SEVERITY
    Valid properties: PRODUCT, CLASSIFICATION, SEVERITY
    Valid properties: PRODUCT, CLASSIFICATION, SEVERITY
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_patch_properties(
        OperatingSystem='WINDOWS'|'AMAZON_LINUX'|'AMAZON_LINUX_2'|'UBUNTU'|'REDHAT_ENTERPRISE_LINUX'|'SUSE'|'CENTOS'|'ORACLE_LINUX'|'DEBIAN',
        Property='PRODUCT'|'PRODUCT_FAMILY'|'CLASSIFICATION'|'MSRC_SEVERITY'|'PRIORITY'|'SEVERITY',
        PatchSet='OS'|'APPLICATION',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type OperatingSystem: string
    :param OperatingSystem: [REQUIRED]\nThe operating system type for which to list patches.\n

    :type Property: string
    :param Property: [REQUIRED]\nThe patch property for which you want to view patch details.\n

    :type PatchSet: string
    :param PatchSet: Indicates whether to list patches for the Windows operating system or for Microsoft applications. Not applicable for Linux operating systems.

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :rtype: dict

ReturnsResponse Syntax
{
    'Properties': [
        {
            'string': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Properties (list) --
A list of the properties for patches matching the filter request parameters.

(dict) --
(string) --
(string) --






NextToken (string) --
The token for the next set of items to return. (You use this token in the next call.)







Exceptions

SSM.Client.exceptions.InternalServerError


    :return: {
        'Properties': [
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

def describe_sessions(State=None, MaxResults=None, NextToken=None, Filters=None):
    """
    Retrieves a list of all active sessions (both connected and disconnected) or terminated sessions from the past 30 days.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_sessions(
        State='Active'|'History',
        MaxResults=123,
        NextToken='string',
        Filters=[
            {
                'key': 'InvokedAfter'|'InvokedBefore'|'Target'|'Owner'|'Status',
                'value': 'string'
            },
        ]
    )
    
    
    :type State: string
    :param State: [REQUIRED]\nThe session status to retrieve a list of sessions for. For example, 'Active'.\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :type Filters: list
    :param Filters: One or more filters to limit the type of sessions returned by the request.\n\n(dict) --Describes a filter for Session Manager information.\n\nkey (string) -- [REQUIRED]The name of the filter.\n\nvalue (string) -- [REQUIRED]The filter value. Valid values for each filter key are as follows:\n\nInvokedAfter: Specify a timestamp to limit your results. For example, specify 2018-08-29T00:00:00Z to see sessions that started August 29, 2018, and later.\nInvokedBefore: Specify a timestamp to limit your results. For example, specify 2018-08-29T00:00:00Z to see sessions that started before August 29, 2018.\nTarget: Specify an instance to which session connections have been made.\nOwner: Specify an AWS user account to see a list of sessions started by that user.\nStatus: Specify a valid session status to see a list of all sessions with that status. Status values you can specify include:\nConnected\nConnecting\nDisconnected\nTerminated\nTerminating\nFailed\n\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Sessions': [
        {
            'SessionId': 'string',
            'Target': 'string',
            'Status': 'Connected'|'Connecting'|'Disconnected'|'Terminated'|'Terminating'|'Failed',
            'StartDate': datetime(2015, 1, 1),
            'EndDate': datetime(2015, 1, 1),
            'DocumentName': 'string',
            'Owner': 'string',
            'Details': 'string',
            'OutputUrl': {
                'S3OutputUrl': 'string',
                'CloudWatchOutputUrl': 'string'
            }
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Sessions (list) --
A list of sessions meeting the request parameters.

(dict) --
Information about a Session Manager connection to an instance.

SessionId (string) --
The ID of the session.

Target (string) --
The instance that the Session Manager session connected to.

Status (string) --
The status of the session. For example, "Connected" or "Terminated".

StartDate (datetime) --
The date and time, in ISO-8601 Extended format, when the session began.

EndDate (datetime) --
The date and time, in ISO-8601 Extended format, when the session was terminated.

DocumentName (string) --
The name of the Session Manager SSM document used to define the parameters and plugin settings for the session. For example, SSM-SessionManagerRunShell .

Owner (string) --
The ID of the AWS user account that started the session.

Details (string) --
Reserved for future use.

OutputUrl (dict) --
Reserved for future use.

S3OutputUrl (string) --
Reserved for future use.

CloudWatchOutputUrl (string) --
Reserved for future use.







NextToken (string) --
The token for the next set of items to return. (You received this token from a previous call.)







Exceptions

SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.InvalidFilterKey
SSM.Client.exceptions.InvalidNextToken


    :return: {
        'Sessions': [
            {
                'SessionId': 'string',
                'Target': 'string',
                'Status': 'Connected'|'Connecting'|'Disconnected'|'Terminated'|'Terminating'|'Failed',
                'StartDate': datetime(2015, 1, 1),
                'EndDate': datetime(2015, 1, 1),
                'DocumentName': 'string',
                'Owner': 'string',
                'Details': 'string',
                'OutputUrl': {
                    'S3OutputUrl': 'string',
                    'CloudWatchOutputUrl': 'string'
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    SSM.Client.exceptions.InternalServerError
    SSM.Client.exceptions.InvalidFilterKey
    SSM.Client.exceptions.InvalidNextToken
    
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

def get_automation_execution(AutomationExecutionId=None):
    """
    Get detailed information about a particular Automation execution.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_automation_execution(
        AutomationExecutionId='string'
    )
    
    
    :type AutomationExecutionId: string
    :param AutomationExecutionId: [REQUIRED]\nThe unique identifier for an existing automation execution to examine. The execution ID is returned by StartAutomationExecution when the execution of an Automation document is initiated.\n

    :rtype: dict
ReturnsResponse Syntax{
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
                },
                'IsEnd': True|False,
                'NextStep': 'string',
                'IsCritical': True|False,
                'ValidNextSteps': [
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
                'TargetLocation': {
                    'Accounts': [
                        'string',
                    ],
                    'Regions': [
                        'string',
                    ],
                    'TargetLocationMaxConcurrency': 'string',
                    'TargetLocationMaxErrors': 'string',
                    'ExecutionRoleName': 'string'
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
        'TargetMaps': [
            {
                'string': [
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
        'Target': 'string',
        'TargetLocations': [
            {
                'Accounts': [
                    'string',
                ],
                'Regions': [
                    'string',
                ],
                'TargetLocationMaxConcurrency': 'string',
                'TargetLocationMaxErrors': 'string',
                'ExecutionRoleName': 'string'
            },
        ],
        'ProgressCounters': {
            'TotalSteps': 123,
            'SuccessSteps': 123,
            'FailedSteps': 123,
            'CancelledSteps': 123,
            'TimedOutSteps': 123
        }
    }
}


Response Structure

(dict) --
AutomationExecution (dict) --Detailed information about the current state of an automation execution.

AutomationExecutionId (string) --The execution ID.

DocumentName (string) --The name of the Automation document used during the execution.

DocumentVersion (string) --The version of the document to use during execution.

ExecutionStartTime (datetime) --The time the execution started.

ExecutionEndTime (datetime) --The time the execution finished.

AutomationExecutionStatus (string) --The execution status of the Automation.

StepExecutions (list) --A list of details about the current state of all steps that comprise an execution. An Automation document contains a list of steps that are run in order.

(dict) --Detailed information about an the execution state of an Automation step.

StepName (string) --The name of this execution step.

Action (string) --The action this step performs. The action determines the behavior of the step.

TimeoutSeconds (integer) --The timeout seconds of the step.

OnFailure (string) --The action to take if the step fails. The default value is Abort.

MaxAttempts (integer) --The maximum number of tries to run the action of the step. The default value is 1.

ExecutionStartTime (datetime) --If a step has begun execution, this contains the time the step started. If the step is in Pending status, this field is not populated.

ExecutionEndTime (datetime) --If a step has finished execution, this contains the time the execution ended. If the step has not yet concluded, this field is not populated.

StepStatus (string) --The execution status for this step.

ResponseCode (string) --The response code returned by the execution of the step.

Inputs (dict) --Fully-resolved values passed into the step before execution.

(string) --
(string) --




Outputs (dict) --Returned values from the execution of the step.

(string) --
(list) --
(string) --






Response (string) --A message associated with the response code for an execution.

FailureMessage (string) --If a step failed, this message explains why the execution failed.

FailureDetails (dict) --Information about the Automation failure.

FailureStage (string) --The stage of the Automation execution when the failure occurred. The stages include the following: InputValidation, PreVerification, Invocation, PostVerification.

FailureType (string) --The type of Automation failure. Failure types include the following: Action, Permission, Throttling, Verification, Internal.

Details (dict) --Detailed information about the Automation step failure.

(string) --
(list) --
(string) --








StepExecutionId (string) --The unique ID of a step execution.

OverriddenParameters (dict) --A user-specified list of parameters to override when running a step.

(string) --
(list) --
(string) --






IsEnd (boolean) --The flag which can be used to end automation no matter whether the step succeeds or fails.

NextStep (string) --The next step after the step succeeds.

IsCritical (boolean) --The flag which can be used to help decide whether the failure of current step leads to the Automation failure.

ValidNextSteps (list) --Strategies used when step fails, we support Continue and Abort. Abort will fail the automation when the step fails. Continue will ignore the failure of current step and allow automation to run the next step. With conditional branching, we add step:stepName to support the automation to go to another specific step.

(string) --


Targets (list) --The targets for the step execution.

(dict) --An array of search criteria that targets instances using a Key,Value combination that you specify.
Supported formats include the following.

``Key=InstanceIds,Values=*instance-id-1* ,*instance-id-2* ,*instance-id-3* ``
``Key=tag:my-tag-key ,Values=*my-tag-value-1* ,*my-tag-value-2* ``
``Key=tag-key,Values=*my-tag-key-1* ,*my-tag-key-2* ``
(Maintenance window targets only) ``Key=resource-groups:Name,Values=*resource-group-name* ``
(Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*resource-type-1* ,*resource-type-2* ``

For example:

Key=InstanceIds,Values=i-02573cafcfEXAMPLE,i-0471e04240EXAMPLE,i-07782c72faEXAMPLE
Key=tag:CostCenter,Values=CostCenter1,CostCenter2,CostCenter3
Key=tag-key,Values=Name,Instance-Type,CostCenter
(Maintenance window targets only) Key=resource-groups:Name,Values=ProductionResourceGroup   This example demonstrates how to target all resources in the resource group ProductionResourceGroup in your maintenance window.
(Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*AWS::EC2::INSTANCE* ,*AWS::EC2::VPC* ``   This example demonstrates how to target only EC2 instances and VPCs in your maintenance window.
(State Manager association targets only) Key=InstanceIds,Values=*   This example demonstrates how to target all managed instances in the AWS Region where the association was created.

For information about how to send commands that target instances using Key,Value parameters, see Targeting multiple instances in the AWS Systems Manager User Guide .

Key (string) --User-defined criteria for sending commands that target instances that meet the criteria.

Values (list) --User-defined criteria that maps to Key . For example, if you specified tag:ServerRole , you could specify value:WebServer to run a command on instances that include EC2 tags of ServerRole,WebServer .

(string) --






TargetLocation (dict) --The combination of AWS Regions and accounts targeted by the current Automation execution.

Accounts (list) --The AWS accounts targeted by the current Automation execution.

(string) --


Regions (list) --The AWS Regions targeted by the current Automation execution.

(string) --


TargetLocationMaxConcurrency (string) --The maximum number of AWS accounts and AWS regions allowed to run the Automation concurrently

TargetLocationMaxErrors (string) --The maximum number of errors allowed before the system stops queueing additional Automation executions for the currently running Automation.

ExecutionRoleName (string) --The Automation execution role used by the currently running Automation.







StepExecutionsTruncated (boolean) --A boolean value that indicates if the response contains the full list of the Automation step executions. If true, use the DescribeAutomationStepExecutions API action to get the full list of step executions.

Parameters (dict) --The key-value map of execution parameters, which were supplied when calling StartAutomationExecution.

(string) --
(list) --
(string) --






Outputs (dict) --The list of execution outputs as defined in the automation document.

(string) --
(list) --
(string) --






FailureMessage (string) --A message describing why an execution has failed, if the status is set to Failed.

Mode (string) --The automation execution mode.

ParentAutomationExecutionId (string) --The AutomationExecutionId of the parent automation.

ExecutedBy (string) --The Amazon Resource Name (ARN) of the user who ran the automation.

CurrentStepName (string) --The name of the step that is currently running.

CurrentAction (string) --The action of the step that is currently running.

TargetParameterName (string) --The parameter name.

Targets (list) --The specified targets.

(dict) --An array of search criteria that targets instances using a Key,Value combination that you specify.
Supported formats include the following.

``Key=InstanceIds,Values=*instance-id-1* ,*instance-id-2* ,*instance-id-3* ``
``Key=tag:my-tag-key ,Values=*my-tag-value-1* ,*my-tag-value-2* ``
``Key=tag-key,Values=*my-tag-key-1* ,*my-tag-key-2* ``
(Maintenance window targets only) ``Key=resource-groups:Name,Values=*resource-group-name* ``
(Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*resource-type-1* ,*resource-type-2* ``

For example:

Key=InstanceIds,Values=i-02573cafcfEXAMPLE,i-0471e04240EXAMPLE,i-07782c72faEXAMPLE
Key=tag:CostCenter,Values=CostCenter1,CostCenter2,CostCenter3
Key=tag-key,Values=Name,Instance-Type,CostCenter
(Maintenance window targets only) Key=resource-groups:Name,Values=ProductionResourceGroup   This example demonstrates how to target all resources in the resource group ProductionResourceGroup in your maintenance window.
(Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*AWS::EC2::INSTANCE* ,*AWS::EC2::VPC* ``   This example demonstrates how to target only EC2 instances and VPCs in your maintenance window.
(State Manager association targets only) Key=InstanceIds,Values=*   This example demonstrates how to target all managed instances in the AWS Region where the association was created.

For information about how to send commands that target instances using Key,Value parameters, see Targeting multiple instances in the AWS Systems Manager User Guide .

Key (string) --User-defined criteria for sending commands that target instances that meet the criteria.

Values (list) --User-defined criteria that maps to Key . For example, if you specified tag:ServerRole , you could specify value:WebServer to run a command on instances that include EC2 tags of ServerRole,WebServer .

(string) --






TargetMaps (list) --The specified key-value mapping of document parameters to target resources.

(dict) --
(string) --
(list) --
(string) --








ResolvedTargets (dict) --A list of resolved targets in the rate control execution.

ParameterValues (list) --A list of parameter values sent to targets that resolved during the Automation execution.

(string) --


Truncated (boolean) --A boolean value indicating whether the resolved target list is truncated.



MaxConcurrency (string) --The MaxConcurrency value specified by the user when the execution started.

MaxErrors (string) --The MaxErrors value specified by the user when the execution started.

Target (string) --The target of the execution.

TargetLocations (list) --The combination of AWS Regions and/or AWS accounts where you want to run the Automation.

(dict) --The combination of AWS Regions and accounts targeted by the current Automation execution.

Accounts (list) --The AWS accounts targeted by the current Automation execution.

(string) --


Regions (list) --The AWS Regions targeted by the current Automation execution.

(string) --


TargetLocationMaxConcurrency (string) --The maximum number of AWS accounts and AWS regions allowed to run the Automation concurrently

TargetLocationMaxErrors (string) --The maximum number of errors allowed before the system stops queueing additional Automation executions for the currently running Automation.

ExecutionRoleName (string) --The Automation execution role used by the currently running Automation.





ProgressCounters (dict) --An aggregate of step execution statuses displayed in the AWS Console for a multi-Region and multi-account Automation execution.

TotalSteps (integer) --The total number of steps run in all specified AWS Regions and accounts for the current Automation execution.

SuccessSteps (integer) --The total number of steps that successfully completed in all specified AWS Regions and accounts for the current Automation execution.

FailedSteps (integer) --The total number of steps that failed to run in all specified AWS Regions and accounts for the current Automation execution.

CancelledSteps (integer) --The total number of steps that the system cancelled in all specified AWS Regions and accounts for the current Automation execution.

TimedOutSteps (integer) --The total number of steps that timed out in all specified AWS Regions and accounts for the current Automation execution.










Exceptions

SSM.Client.exceptions.AutomationExecutionNotFoundException
SSM.Client.exceptions.InternalServerError


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
                    },
                    'IsEnd': True|False,
                    'NextStep': 'string',
                    'IsCritical': True|False,
                    'ValidNextSteps': [
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
                    'TargetLocation': {
                        'Accounts': [
                            'string',
                        ],
                        'Regions': [
                            'string',
                        ],
                        'TargetLocationMaxConcurrency': 'string',
                        'TargetLocationMaxErrors': 'string',
                        'ExecutionRoleName': 'string'
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
            'TargetMaps': [
                {
                    'string': [
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
            'Target': 'string',
            'TargetLocations': [
                {
                    'Accounts': [
                        'string',
                    ],
                    'Regions': [
                        'string',
                    ],
                    'TargetLocationMaxConcurrency': 'string',
                    'TargetLocationMaxErrors': 'string',
                    'ExecutionRoleName': 'string'
                },
            ],
            'ProgressCounters': {
                'TotalSteps': 123,
                'SuccessSteps': 123,
                'FailedSteps': 123,
                'CancelledSteps': 123,
                'TimedOutSteps': 123
            }
        }
    }
    
    
    :returns: 
    (string) --
    (list) --
    (string) --
    
    
    
    
    
    """
    pass

def get_calendar_state(CalendarNames=None, AtTime=None):
    """
    Gets the state of the AWS Systems Manager Change Calendar at an optional, specified time. If you specify a time, GetCalendarState returns the state of the calendar at a specific time, and returns the next time that the Change Calendar state will transition. If you do not specify a time, GetCalendarState assumes the current time. Change Calendar entries have two possible states: OPEN or CLOSED . For more information about Systems Manager Change Calendar, see AWS Systems Manager Change Calendar in the AWS Systems Manager User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_calendar_state(
        CalendarNames=[
            'string',
        ],
        AtTime='string'
    )
    
    
    :type CalendarNames: list
    :param CalendarNames: [REQUIRED]\nThe names or Amazon Resource Names (ARNs) of the Systems Manager documents that represent the calendar entries for which you want to get the state.\n\n(string) --\n\n

    :type AtTime: string
    :param AtTime: (Optional) The specific time for which you want to get calendar state information, in ISO 8601 format. If you do not add AtTime , the current time is assumed.

    :rtype: dict

ReturnsResponse Syntax
{
    'State': 'OPEN'|'CLOSED',
    'AtTime': 'string',
    'NextTransitionTime': 'string'
}


Response Structure

(dict) --

State (string) --
The state of the calendar. An OPEN calendar indicates that actions are allowed to proceed, and a CLOSED calendar indicates that actions are not allowed to proceed.

AtTime (string) --
The time, as an ISO 8601 string, that you specified in your command. If you did not specify a time, GetCalendarState uses the current time.

NextTransitionTime (string) --
The time, as an ISO 8601 string, that the calendar state will change. If the current calendar state is OPEN , NextTransitionTime indicates when the calendar state changes to CLOSED , and vice-versa.







Exceptions

SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.InvalidDocument
SSM.Client.exceptions.InvalidDocumentType
SSM.Client.exceptions.UnsupportedCalendarException


    :return: {
        'State': 'OPEN'|'CLOSED',
        'AtTime': 'string',
        'NextTransitionTime': 'string'
    }
    
    
    :returns: 
    SSM.Client.exceptions.InternalServerError
    SSM.Client.exceptions.InvalidDocument
    SSM.Client.exceptions.InvalidDocumentType
    SSM.Client.exceptions.UnsupportedCalendarException
    
    """
    pass

def get_command_invocation(CommandId=None, InstanceId=None, PluginName=None):
    """
    Returns detailed information about command execution for an invocation or plugin.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_command_invocation(
        CommandId='string',
        InstanceId='string',
        PluginName='string'
    )
    
    
    :type CommandId: string
    :param CommandId: [REQUIRED]\n(Required) The parent command ID of the invocation plugin.\n

    :type InstanceId: string
    :param InstanceId: [REQUIRED]\n(Required) The ID of the managed instance targeted by the command. A managed instance can be an EC2 instance or an instance in your hybrid environment that is configured for Systems Manager.\n

    :type PluginName: string
    :param PluginName: (Optional) The name of the plugin for which you want detailed results. If the document contains only one plugin, the name can be omitted and the details will be returned.

    :rtype: dict

ReturnsResponse Syntax
{
    'CommandId': 'string',
    'InstanceId': 'string',
    'Comment': 'string',
    'DocumentName': 'string',
    'DocumentVersion': 'string',
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
    'StandardErrorUrl': 'string',
    'CloudWatchOutputConfig': {
        'CloudWatchLogGroupName': 'string',
        'CloudWatchOutputEnabled': True|False
    }
}


Response Structure

(dict) --

CommandId (string) --
The parent command ID of the invocation plugin.

InstanceId (string) --
The ID of the managed instance targeted by the command. A managed instance can be an EC2 instance or an instance in your hybrid environment that is configured for Systems Manager.

Comment (string) --
The comment text for the command.

DocumentName (string) --
The name of the document that was run. For example, AWS-RunShellScript.

DocumentVersion (string) --
The SSM document version used in the request.

PluginName (string) --
The name of the plugin for which you want detailed results. For example, aws:RunShellScript is a plugin.

ResponseCode (integer) --
The error level response code for the plugin script. If the response code is -1, then the command has not started running on the instance, or it was not received by the instance.

ExecutionStartDateTime (string) --
The date and time the plugin started running. Date and time are written in ISO 8601 format. For example, June 7, 2017 is represented as 2017-06-7. The following sample AWS CLI command uses the InvokedBefore filter.

aws ssm list-commands --filters key=InvokedBefore,value=2017-06-07T00:00:00Z

If the plugin has not started to run, the string is empty.

ExecutionElapsedTime (string) --
Duration since ExecutionStartDateTime.

ExecutionEndDateTime (string) --
The date and time the plugin was finished running. Date and time are written in ISO 8601 format. For example, June 7, 2017 is represented as 2017-06-7. The following sample AWS CLI command uses the InvokedAfter filter.

aws ssm list-commands --filters key=InvokedAfter,value=2017-06-07T00:00:00Z

If the plugin has not started to run, the string is empty.

Status (string) --
The status of this invocation plugin. This status can be different than StatusDetails.

StatusDetails (string) --
A detailed status of the command execution for an invocation. StatusDetails includes more information than Status because it includes states resulting from error and concurrency control parameters. StatusDetails can show different results than Status. For more information about these statuses, see Understanding command statuses in the AWS Systems Manager User Guide . StatusDetails can be one of the following values:

Pending: The command has not been sent to the instance.
In Progress: The command has been sent to the instance but has not reached a terminal state.
Delayed: The system attempted to send the command to the target, but the target was not available. The instance might not be available because of network issues, because the instance was stopped, or for similar reasons. The system will try to send the command again.
Success: The command or plugin ran successfully. This is a terminal state.
Delivery Timed Out: The command was not delivered to the instance before the delivery timeout expired. Delivery timeouts do not count against the parent command\'s MaxErrors limit, but they do contribute to whether the parent command status is Success or Incomplete. This is a terminal state.
Execution Timed Out: The command started to run on the instance, but the execution was not complete before the timeout expired. Execution timeouts count against the MaxErrors limit of the parent command. This is a terminal state.
Failed: The command wasn\'t run successfully on the instance. For a plugin, this indicates that the result code was not zero. For a command invocation, this indicates that the result code for one or more plugins was not zero. Invocation failures count against the MaxErrors limit of the parent command. This is a terminal state.
Canceled: The command was terminated before it was completed. This is a terminal state.
Undeliverable: The command can\'t be delivered to the instance. The instance might not exist or might not be responding. Undeliverable invocations don\'t count against the parent command\'s MaxErrors limit and don\'t contribute to whether the parent command status is Success or Incomplete. This is a terminal state.
Terminated: The parent command exceeded its MaxErrors limit and subsequent command invocations were canceled by the system. This is a terminal state.


StandardOutputContent (string) --
The first 24,000 characters written by the plugin to stdout. If the command has not finished running, if ExecutionStatus is neither Succeeded nor Failed, then this string is empty.

StandardOutputUrl (string) --
The URL for the complete text written by the plugin to stdout in Amazon S3. If an S3 bucket was not specified, then this string is empty.

StandardErrorContent (string) --
The first 8,000 characters written by the plugin to stderr. If the command has not finished running, then this string is empty.

StandardErrorUrl (string) --
The URL for the complete text written by the plugin to stderr. If the command has not finished running, then this string is empty.

CloudWatchOutputConfig (dict) --
CloudWatch Logs information where Systems Manager sent the command output.

CloudWatchLogGroupName (string) --
The name of the CloudWatch log group where you want to send command output. If you don\'t specify a group name, Systems Manager automatically creates a log group for you. The log group uses the following naming format: aws/ssm/SystemsManagerDocumentName .

CloudWatchOutputEnabled (boolean) --
Enables Systems Manager to send command output to CloudWatch Logs.









Exceptions

SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.InvalidCommandId
SSM.Client.exceptions.InvalidInstanceId
SSM.Client.exceptions.InvalidPluginName
SSM.Client.exceptions.InvocationDoesNotExist


    :return: {
        'CommandId': 'string',
        'InstanceId': 'string',
        'Comment': 'string',
        'DocumentName': 'string',
        'DocumentVersion': 'string',
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
        'StandardErrorUrl': 'string',
        'CloudWatchOutputConfig': {
            'CloudWatchLogGroupName': 'string',
            'CloudWatchOutputEnabled': True|False
        }
    }
    
    
    :returns: 
    Pending: The command has not been sent to the instance.
    In Progress: The command has been sent to the instance but has not reached a terminal state.
    Delayed: The system attempted to send the command to the target, but the target was not available. The instance might not be available because of network issues, because the instance was stopped, or for similar reasons. The system will try to send the command again.
    Success: The command or plugin ran successfully. This is a terminal state.
    Delivery Timed Out: The command was not delivered to the instance before the delivery timeout expired. Delivery timeouts do not count against the parent command\'s MaxErrors limit, but they do contribute to whether the parent command status is Success or Incomplete. This is a terminal state.
    Execution Timed Out: The command started to run on the instance, but the execution was not complete before the timeout expired. Execution timeouts count against the MaxErrors limit of the parent command. This is a terminal state.
    Failed: The command wasn\'t run successfully on the instance. For a plugin, this indicates that the result code was not zero. For a command invocation, this indicates that the result code for one or more plugins was not zero. Invocation failures count against the MaxErrors limit of the parent command. This is a terminal state.
    Canceled: The command was terminated before it was completed. This is a terminal state.
    Undeliverable: The command can\'t be delivered to the instance. The instance might not exist or might not be responding. Undeliverable invocations don\'t count against the parent command\'s MaxErrors limit and don\'t contribute to whether the parent command status is Success or Incomplete. This is a terminal state.
    Terminated: The parent command exceeded its MaxErrors limit and subsequent command invocations were canceled by the system. This is a terminal state.
    
    """
    pass

def get_connection_status(Target=None):
    """
    Retrieves the Session Manager connection status for an instance to determine whether it is running and ready to receive Session Manager connections.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_connection_status(
        Target='string'
    )
    
    
    :type Target: string
    :param Target: [REQUIRED]\nThe ID of the instance.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Target': 'string',
    'Status': 'Connected'|'NotConnected'
}


Response Structure

(dict) --
Target (string) --The ID of the instance to check connection status.

Status (string) --The status of the connection to the instance. For example, \'Connected\' or \'Not Connected\'.






Exceptions

SSM.Client.exceptions.InternalServerError


    :return: {
        'Target': 'string',
        'Status': 'Connected'|'NotConnected'
    }
    
    
    """
    pass

def get_default_patch_baseline(OperatingSystem=None):
    """
    Retrieves the default patch baseline. Note that Systems Manager supports creating multiple default patch baselines. For example, you can create a default patch baseline for each operating system.
    If you do not specify an operating system value, the default patch baseline for Windows is returned.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_default_patch_baseline(
        OperatingSystem='WINDOWS'|'AMAZON_LINUX'|'AMAZON_LINUX_2'|'UBUNTU'|'REDHAT_ENTERPRISE_LINUX'|'SUSE'|'CENTOS'|'ORACLE_LINUX'|'DEBIAN'
    )
    
    
    :type OperatingSystem: string
    :param OperatingSystem: Returns the default patch baseline for the specified operating system.

    :rtype: dict
ReturnsResponse Syntax{
    'BaselineId': 'string',
    'OperatingSystem': 'WINDOWS'|'AMAZON_LINUX'|'AMAZON_LINUX_2'|'UBUNTU'|'REDHAT_ENTERPRISE_LINUX'|'SUSE'|'CENTOS'|'ORACLE_LINUX'|'DEBIAN'
}


Response Structure

(dict) --
BaselineId (string) --The ID of the default patch baseline.

OperatingSystem (string) --The operating system for the returned patch baseline.






Exceptions

SSM.Client.exceptions.InternalServerError


    :return: {
        'BaselineId': 'string',
        'OperatingSystem': 'WINDOWS'|'AMAZON_LINUX'|'AMAZON_LINUX_2'|'UBUNTU'|'REDHAT_ENTERPRISE_LINUX'|'SUSE'|'CENTOS'|'ORACLE_LINUX'|'DEBIAN'
    }
    
    
    """
    pass

def get_deployable_patch_snapshot_for_instance(InstanceId=None, SnapshotId=None):
    """
    Retrieves the current snapshot for the patch baseline the instance uses. This API is primarily used by the AWS-RunPatchBaseline Systems Manager document.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_deployable_patch_snapshot_for_instance(
        InstanceId='string',
        SnapshotId='string'
    )
    
    
    :type InstanceId: string
    :param InstanceId: [REQUIRED]\nThe ID of the instance for which the appropriate patch snapshot should be retrieved.\n

    :type SnapshotId: string
    :param SnapshotId: [REQUIRED]\nThe user-defined snapshot ID.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'InstanceId': 'string',
    'SnapshotId': 'string',
    'SnapshotDownloadUrl': 'string',
    'Product': 'string'
}


Response Structure

(dict) --

InstanceId (string) --
The ID of the instance.

SnapshotId (string) --
The user-defined snapshot ID.

SnapshotDownloadUrl (string) --
A pre-signed Amazon S3 URL that can be used to download the patch snapshot.

Product (string) --
Returns the specific operating system (for example Windows Server 2012 or Amazon Linux 2015.09) on the instance for the specified patch snapshot.







Exceptions

SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.UnsupportedOperatingSystem
SSM.Client.exceptions.UnsupportedFeatureRequiredException


    :return: {
        'InstanceId': 'string',
        'SnapshotId': 'string',
        'SnapshotDownloadUrl': 'string',
        'Product': 'string'
    }
    
    
    :returns: 
    SSM.Client.exceptions.InternalServerError
    SSM.Client.exceptions.UnsupportedOperatingSystem
    SSM.Client.exceptions.UnsupportedFeatureRequiredException
    
    """
    pass

def get_document(Name=None, VersionName=None, DocumentVersion=None, DocumentFormat=None):
    """
    Gets the contents of the specified Systems Manager document.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_document(
        Name='string',
        VersionName='string',
        DocumentVersion='string',
        DocumentFormat='YAML'|'JSON'|'TEXT'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the Systems Manager document.\n

    :type VersionName: string
    :param VersionName: An optional field specifying the version of the artifact associated with the document. For example, 'Release 12, Update 6'. This value is unique across all versions of a document and can\'t be changed.

    :type DocumentVersion: string
    :param DocumentVersion: The document version for which you want information.

    :type DocumentFormat: string
    :param DocumentFormat: Returns the document in the specified format. The document format can be either JSON or YAML. JSON is the default format.

    :rtype: dict

ReturnsResponse Syntax
{
    'Name': 'string',
    'VersionName': 'string',
    'DocumentVersion': 'string',
    'Status': 'Creating'|'Active'|'Updating'|'Deleting'|'Failed',
    'StatusInformation': 'string',
    'Content': 'string',
    'DocumentType': 'Command'|'Policy'|'Automation'|'Session'|'Package'|'ApplicationConfiguration'|'ApplicationConfigurationSchema'|'DeploymentStrategy'|'ChangeCalendar',
    'DocumentFormat': 'YAML'|'JSON'|'TEXT',
    'Requires': [
        {
            'Name': 'string',
            'Version': 'string'
        },
    ],
    'AttachmentsContent': [
        {
            'Name': 'string',
            'Size': 123,
            'Hash': 'string',
            'HashType': 'Sha256',
            'Url': 'string'
        },
    ]
}


Response Structure

(dict) --

Name (string) --
The name of the Systems Manager document.

VersionName (string) --
The version of the artifact associated with the document. For example, "Release 12, Update 6". This value is unique across all versions of a document, and cannot be changed.

DocumentVersion (string) --
The document version.

Status (string) --
The status of the Systems Manager document, such as Creating , Active , Updating , Failed , and Deleting .

StatusInformation (string) --
A message returned by AWS Systems Manager that explains the Status value. For example, a Failed status might be explained by the StatusInformation message, "The specified S3 bucket does not exist. Verify that the URL of the S3 bucket is correct."

Content (string) --
The contents of the Systems Manager document.

DocumentType (string) --
The document type.

DocumentFormat (string) --
The document format, either JSON or YAML.

Requires (list) --
A list of SSM documents required by a document. For example, an ApplicationConfiguration document requires an ApplicationConfigurationSchema document.

(dict) --
An SSM document required by the current document.

Name (string) --
The name of the required SSM document. The name can be an Amazon Resource Name (ARN).

Version (string) --
The document version required by the current document.





AttachmentsContent (list) --
A description of the document attachments, including names, locations, sizes, and so on.

(dict) --
A structure that includes attributes that describe a document attachment.

Name (string) --
The name of an attachment.

Size (integer) --
The size of an attachment in bytes.

Hash (string) --
The cryptographic hash value of the document content.

HashType (string) --
The hash algorithm used to calculate the hash value.

Url (string) --
The URL location of the attachment content.











Exceptions

SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.InvalidDocument
SSM.Client.exceptions.InvalidDocumentVersion


    :return: {
        'Name': 'string',
        'VersionName': 'string',
        'DocumentVersion': 'string',
        'Status': 'Creating'|'Active'|'Updating'|'Deleting'|'Failed',
        'StatusInformation': 'string',
        'Content': 'string',
        'DocumentType': 'Command'|'Policy'|'Automation'|'Session'|'Package'|'ApplicationConfiguration'|'ApplicationConfigurationSchema'|'DeploymentStrategy'|'ChangeCalendar',
        'DocumentFormat': 'YAML'|'JSON'|'TEXT',
        'Requires': [
            {
                'Name': 'string',
                'Version': 'string'
            },
        ],
        'AttachmentsContent': [
            {
                'Name': 'string',
                'Size': 123,
                'Hash': 'string',
                'HashType': 'Sha256',
                'Url': 'string'
            },
        ]
    }
    
    
    :returns: 
    SSM.Client.exceptions.InternalServerError
    SSM.Client.exceptions.InvalidDocument
    SSM.Client.exceptions.InvalidDocumentVersion
    
    """
    pass

def get_inventory(Filters=None, Aggregators=None, ResultAttributes=None, NextToken=None, MaxResults=None):
    """
    Query inventory information.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_inventory(
        Filters=[
            {
                'Key': 'string',
                'Values': [
                    'string',
                ],
                'Type': 'Equal'|'NotEqual'|'BeginWith'|'LessThan'|'GreaterThan'|'Exists'
            },
        ],
        Aggregators=[
            {
                'Expression': 'string',
                'Aggregators': {'... recursive ...'},
                'Groups': [
                    {
                        'Name': 'string',
                        'Filters': [
                            {
                                'Key': 'string',
                                'Values': [
                                    'string',
                                ],
                                'Type': 'Equal'|'NotEqual'|'BeginWith'|'LessThan'|'GreaterThan'|'Exists'
                            },
                        ]
                    },
                ]
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
    :param Filters: One or more filters. Use a filter to return a more specific list of results.\n\n(dict) --One or more filters. Use a filter to return a more specific list of results.\n\nKey (string) -- [REQUIRED]The name of the filter key.\n\nValues (list) -- [REQUIRED]Inventory filter values. Example: inventory filter where instance IDs are specified as values Key=AWS:InstanceInformation.InstanceId,Values= i-a12b3c4d5e6g, i-1a2b3c4d5e6,Type=Equal\n\n(string) --\n\n\nType (string) --The type of filter.\n\nNote\nThe Exists filter must be used with aggregators. For more information, see Aggregating inventory data in the AWS Systems Manager User Guide .\n\n\n\n\n\n

    :type Aggregators: list
    :param Aggregators: Returns counts of inventory types based on one or more expressions. For example, if you aggregate by using an expression that uses the AWS:InstanceInformation.PlatformType type, you can see a count of how many Windows and Linux instances exist in your inventoried fleet.\n\n(dict) --Specifies the inventory type and attribute for the aggregation execution.\n\nExpression (string) --The inventory type and attribute name for aggregation.\n\nAggregators (list) --Nested aggregators to further refine aggregation for an inventory type.\n\nGroups (list) --A user-defined set of one or more filters on which to aggregate inventory data. Groups return a count of resources that match and don\'t match the specified criteria.\n\n(dict) --A user-defined set of one or more filters on which to aggregate inventory data. Groups return a count of resources that match and don\'t match the specified criteria.\n\nName (string) -- [REQUIRED]The name of the group.\n\nFilters (list) -- [REQUIRED]Filters define the criteria for the group. The matchingCount field displays the number of resources that match the criteria. The notMatchingCount field displays the number of resources that don\'t match the criteria.\n\n(dict) --One or more filters. Use a filter to return a more specific list of results.\n\nKey (string) -- [REQUIRED]The name of the filter key.\n\nValues (list) -- [REQUIRED]Inventory filter values. Example: inventory filter where instance IDs are specified as values Key=AWS:InstanceInformation.InstanceId,Values= i-a12b3c4d5e6g, i-1a2b3c4d5e6,Type=Equal\n\n(string) --\n\n\nType (string) --The type of filter.\n\nNote\nThe Exists filter must be used with aggregators. For more information, see Aggregating inventory data in the AWS Systems Manager User Guide .\n\n\n\n\n\n\n\n\n\n\n\n\n\n

    :type ResultAttributes: list
    :param ResultAttributes: The list of inventory item types to return.\n\n(dict) --The inventory item result attribute.\n\nTypeName (string) -- [REQUIRED]Name of the inventory item type. Valid value: AWS:InstanceInformation. Default Value: AWS:InstanceInformation.\n\n\n\n\n

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

Entities (list) --
Collection of inventory entities such as a collection of instance inventory.

(dict) --
Inventory query results.

Id (string) --
ID of the inventory result entity. For example, for managed instance inventory the result will be the managed instance ID. For EC2 instance inventory, the result will be the instance ID.

Data (dict) --
The data section in the inventory result entity JSON.

(string) --

(dict) --
The inventory result item.

TypeName (string) --
The name of the inventory result item type.

SchemaVersion (string) --
The schema version for the inventory result item/

CaptureTime (string) --
The time inventory item data was captured.

ContentHash (string) --
MD5 hash of the inventory item type contents. The content hash is used to determine whether to update inventory information. The PutInventory API does not update the inventory item type contents if the MD5 hash has not changed since last update.

Content (list) --
Contains all the inventory data of the item type. Results include attribute names and values.

(dict) --
(string) --
(string) --
















NextToken (string) --
The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.







Exceptions

SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.InvalidFilter
SSM.Client.exceptions.InvalidInventoryGroupException
SSM.Client.exceptions.InvalidNextToken
SSM.Client.exceptions.InvalidTypeNameException
SSM.Client.exceptions.InvalidAggregatorException
SSM.Client.exceptions.InvalidResultAttributeException


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
    
    Exceptions
    
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

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

Schemas (list) --
Inventory schemas returned by the request.

(dict) --
The inventory item schema definition. Users can use this to compose inventory query filters.

TypeName (string) --
The name of the inventory type. Default inventory item type names start with AWS. Custom inventory type names will start with Custom. Default inventory item types include the following: AWS:AWSComponent, AWS:Application, AWS:InstanceInformation, AWS:Network, and AWS:WindowsUpdate.

Version (string) --
The schema version for the inventory item.

Attributes (list) --
The schema attributes for inventory. This contains data type and attribute name.

(dict) --
Attributes are the entries within the inventory item content. It contains name and value.

Name (string) --
Name of the inventory item attribute.

DataType (string) --
The data type of the inventory item attribute.





DisplayName (string) --
The alias name of the inventory type. The alias name is used for display purposes.





NextToken (string) --
The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.







Exceptions

SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.InvalidTypeNameException
SSM.Client.exceptions.InvalidNextToken


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
    
    
    :returns: 
    SSM.Client.exceptions.InternalServerError
    SSM.Client.exceptions.InvalidTypeNameException
    SSM.Client.exceptions.InvalidNextToken
    
    """
    pass

def get_maintenance_window(WindowId=None):
    """
    Retrieves a maintenance window.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_maintenance_window(
        WindowId='string'
    )
    
    
    :type WindowId: string
    :param WindowId: [REQUIRED]\nThe ID of the maintenance window for which you want to retrieve information.\n

    :rtype: dict
ReturnsResponse Syntax{
    'WindowId': 'string',
    'Name': 'string',
    'Description': 'string',
    'StartDate': 'string',
    'EndDate': 'string',
    'Schedule': 'string',
    'ScheduleTimezone': 'string',
    'NextExecutionTime': 'string',
    'Duration': 123,
    'Cutoff': 123,
    'AllowUnassociatedTargets': True|False,
    'Enabled': True|False,
    'CreatedDate': datetime(2015, 1, 1),
    'ModifiedDate': datetime(2015, 1, 1)
}


Response Structure

(dict) --
WindowId (string) --The ID of the created maintenance window.

Name (string) --The name of the maintenance window.

Description (string) --The description of the maintenance window.

StartDate (string) --The date and time, in ISO-8601 Extended format, for when the maintenance window is scheduled to become active. The maintenance window will not run before this specified time.

EndDate (string) --The date and time, in ISO-8601 Extended format, for when the maintenance window is scheduled to become inactive. The maintenance window will not run after this specified time.

Schedule (string) --The schedule of the maintenance window in the form of a cron or rate expression.

ScheduleTimezone (string) --The time zone that the scheduled maintenance window executions are based on, in Internet Assigned Numbers Authority (IANA) format. For example: "America/Los_Angeles", "etc/UTC", or "Asia/Seoul". For more information, see the Time Zone Database on the IANA website.

NextExecutionTime (string) --The next time the maintenance window will actually run, taking into account any specified times for the maintenance window to become active or inactive.

Duration (integer) --The duration of the maintenance window in hours.

Cutoff (integer) --The number of hours before the end of the maintenance window that Systems Manager stops scheduling new tasks for execution.

AllowUnassociatedTargets (boolean) --Whether targets must be registered with the maintenance window before tasks can be defined for those targets.

Enabled (boolean) --Indicates whether the maintenance window is enabled.

CreatedDate (datetime) --The date the maintenance window was created.

ModifiedDate (datetime) --The date the maintenance window was last modified.






Exceptions

SSM.Client.exceptions.DoesNotExistException
SSM.Client.exceptions.InternalServerError


    :return: {
        'WindowId': 'string',
        'Name': 'string',
        'Description': 'string',
        'StartDate': 'string',
        'EndDate': 'string',
        'Schedule': 'string',
        'ScheduleTimezone': 'string',
        'NextExecutionTime': 'string',
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
    Retrieves details about a specific a maintenance window execution.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_maintenance_window_execution(
        WindowExecutionId='string'
    )
    
    
    :type WindowExecutionId: string
    :param WindowExecutionId: [REQUIRED]\nThe ID of the maintenance window execution that includes the task.\n

    :rtype: dict
ReturnsResponse Syntax{
    'WindowExecutionId': 'string',
    'TaskIds': [
        'string',
    ],
    'Status': 'PENDING'|'IN_PROGRESS'|'SUCCESS'|'FAILED'|'TIMED_OUT'|'CANCELLING'|'CANCELLED'|'SKIPPED_OVERLAPPING',
    'StatusDetails': 'string',
    'StartTime': datetime(2015, 1, 1),
    'EndTime': datetime(2015, 1, 1)
}


Response Structure

(dict) --
WindowExecutionId (string) --The ID of the maintenance window execution.

TaskIds (list) --The ID of the task executions from the maintenance window execution.

(string) --


Status (string) --The status of the maintenance window execution.

StatusDetails (string) --The details explaining the Status. Only available for certain status values.

StartTime (datetime) --The time the maintenance window started running.

EndTime (datetime) --The time the maintenance window finished running.






Exceptions

SSM.Client.exceptions.DoesNotExistException
SSM.Client.exceptions.InternalServerError


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
    
    
    :returns: 
    SSM.Client.exceptions.DoesNotExistException
    SSM.Client.exceptions.InternalServerError
    
    """
    pass

def get_maintenance_window_execution_task(WindowExecutionId=None, TaskId=None):
    """
    Retrieves the details about a specific task run as part of a maintenance window execution.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_maintenance_window_execution_task(
        WindowExecutionId='string',
        TaskId='string'
    )
    
    
    :type WindowExecutionId: string
    :param WindowExecutionId: [REQUIRED]\nThe ID of the maintenance window execution that includes the task.\n

    :type TaskId: string
    :param TaskId: [REQUIRED]\nThe ID of the specific task execution in the maintenance window task that should be retrieved.\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

WindowExecutionId (string) --
The ID of the maintenance window execution that includes the task.

TaskExecutionId (string) --
The ID of the specific task execution in the maintenance window task that was retrieved.

TaskArn (string) --
The ARN of the task that ran.

ServiceRole (string) --
The role that was assumed when running the task.

Type (string) --
The type of task that was run.

TaskParameters (list) --
The parameters passed to the task when it was run.

Note
TaskParameters has been deprecated. To specify parameters to pass to a task when it runs, instead use the Parameters option in the TaskInvocationParameters structure. For information about how Systems Manager handles these options for the supported maintenance window task types, see  MaintenanceWindowTaskInvocationParameters .

The map has the following format:
Key: string, between 1 and 255 characters
Value: an array of strings, each string is between 1 and 255 characters

(dict) --

(string) --

(dict) --
Defines the values for a task parameter.

Values (list) --
This field contains an array of 0 or more strings, each 1 to 255 characters in length.

(string) --










Priority (integer) --
The priority of the task.

MaxConcurrency (string) --
The defined maximum number of task executions that could be run in parallel.

MaxErrors (string) --
The defined maximum number of task execution errors allowed before scheduling of the task execution would have been stopped.

Status (string) --
The status of the task.

StatusDetails (string) --
The details explaining the Status. Only available for certain status values.

StartTime (datetime) --
The time the task execution started.

EndTime (datetime) --
The time the task execution completed.







Exceptions

SSM.Client.exceptions.DoesNotExistException
SSM.Client.exceptions.InternalServerError


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
    Retrieves information about a specific task running on a specific target.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_maintenance_window_execution_task_invocation(
        WindowExecutionId='string',
        TaskId='string',
        InvocationId='string'
    )
    
    
    :type WindowExecutionId: string
    :param WindowExecutionId: [REQUIRED]\nThe ID of the maintenance window execution for which the task is a part.\n

    :type TaskId: string
    :param TaskId: [REQUIRED]\nThe ID of the specific task in the maintenance window task that should be retrieved.\n

    :type InvocationId: string
    :param InvocationId: [REQUIRED]\nThe invocation ID to retrieve.\n

    :rtype: dict

ReturnsResponse Syntax
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
}


Response Structure

(dict) --

WindowExecutionId (string) --
The maintenance window execution ID.

TaskExecutionId (string) --
The task execution ID.

InvocationId (string) --
The invocation ID.

ExecutionId (string) --
The execution ID.

TaskType (string) --
Retrieves the task type for a maintenance window. Task types include the following: LAMBDA, STEP_FUNCTIONS, AUTOMATION, RUN_COMMAND.

Parameters (string) --
The parameters used at the time that the task ran.

Status (string) --
The task status for an invocation.

StatusDetails (string) --
The details explaining the status. Details are only available for certain status values.

StartTime (datetime) --
The time that the task started running on the target.

EndTime (datetime) --
The time that the task finished running on the target.

OwnerInformation (string) --
User-provided value to be included in any CloudWatch events raised while running tasks for these targets in this maintenance window.

WindowTargetId (string) --
The maintenance window target ID.







Exceptions

SSM.Client.exceptions.DoesNotExistException
SSM.Client.exceptions.InternalServerError


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
    
    
    :returns: 
    SSM.Client.exceptions.DoesNotExistException
    SSM.Client.exceptions.InternalServerError
    
    """
    pass

def get_maintenance_window_task(WindowId=None, WindowTaskId=None):
    """
    Lists the tasks in a maintenance window.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_maintenance_window_task(
        WindowId='string',
        WindowTaskId='string'
    )
    
    
    :type WindowId: string
    :param WindowId: [REQUIRED]\nThe maintenance window ID that includes the task to retrieve.\n

    :type WindowTaskId: string
    :param WindowTaskId: [REQUIRED]\nThe maintenance window task ID to retrieve.\n

    :rtype: dict

ReturnsResponse Syntax
{
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
            'CloudWatchOutputConfig': {
                'CloudWatchLogGroupName': 'string',
                'CloudWatchOutputEnabled': True|False
            },
            'DocumentHash': 'string',
            'DocumentHashType': 'Sha256'|'Sha1',
            'DocumentVersion': 'string',
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


Response Structure

(dict) --

WindowId (string) --
The retrieved maintenance window ID.

WindowTaskId (string) --
The retrieved maintenance window task ID.

Targets (list) --
The targets where the task should run.

(dict) --
An array of search criteria that targets instances using a Key,Value combination that you specify.
Supported formats include the following.

``Key=InstanceIds,Values=*instance-id-1* ,*instance-id-2* ,*instance-id-3* ``
``Key=tag:my-tag-key ,Values=*my-tag-value-1* ,*my-tag-value-2* ``
``Key=tag-key,Values=*my-tag-key-1* ,*my-tag-key-2* ``
(Maintenance window targets only) ``Key=resource-groups:Name,Values=*resource-group-name* ``
(Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*resource-type-1* ,*resource-type-2* ``

For example:

Key=InstanceIds,Values=i-02573cafcfEXAMPLE,i-0471e04240EXAMPLE,i-07782c72faEXAMPLE
Key=tag:CostCenter,Values=CostCenter1,CostCenter2,CostCenter3
Key=tag-key,Values=Name,Instance-Type,CostCenter
(Maintenance window targets only) Key=resource-groups:Name,Values=ProductionResourceGroup   This example demonstrates how to target all resources in the resource group ProductionResourceGroup in your maintenance window.
(Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*AWS::EC2::INSTANCE* ,*AWS::EC2::VPC* ``   This example demonstrates how to target only EC2 instances and VPCs in your maintenance window.
(State Manager association targets only) Key=InstanceIds,Values=*   This example demonstrates how to target all managed instances in the AWS Region where the association was created.

For information about how to send commands that target instances using Key,Value parameters, see Targeting multiple instances in the AWS Systems Manager User Guide .

Key (string) --
User-defined criteria for sending commands that target instances that meet the criteria.

Values (list) --
User-defined criteria that maps to Key . For example, if you specified tag:ServerRole , you could specify value:WebServer to run a command on instances that include EC2 tags of ServerRole,WebServer .

(string) --






TaskArn (string) --
The resource that the task used during execution. For RUN_COMMAND and AUTOMATION task types, the TaskArn is the Systems Manager Document name/ARN. For LAMBDA tasks, the value is the function name/ARN. For STEP_FUNCTIONS tasks, the value is the state machine ARN.

ServiceRoleArn (string) --
The ARN of the IAM service role to use to publish Amazon Simple Notification Service (Amazon SNS) notifications for maintenance window Run Command tasks.

TaskType (string) --
The type of task to run.

TaskParameters (dict) --
The parameters to pass to the task when it runs.

Note
TaskParameters has been deprecated. To specify parameters to pass to a task when it runs, instead use the Parameters option in the TaskInvocationParameters structure. For information about how Systems Manager handles these options for the supported maintenance window task types, see  MaintenanceWindowTaskInvocationParameters .


(string) --

(dict) --
Defines the values for a task parameter.

Values (list) --
This field contains an array of 0 or more strings, each 1 to 255 characters in length.

(string) --








TaskInvocationParameters (dict) --
The parameters to pass to the task when it runs.

RunCommand (dict) --
The parameters for a RUN_COMMAND task type.

Comment (string) --
Information about the commands to run.

CloudWatchOutputConfig (dict) --
Configuration options for sending command output to CloudWatch Logs.

CloudWatchLogGroupName (string) --
The name of the CloudWatch log group where you want to send command output. If you don\'t specify a group name, Systems Manager automatically creates a log group for you. The log group uses the following naming format: aws/ssm/SystemsManagerDocumentName .

CloudWatchOutputEnabled (boolean) --
Enables Systems Manager to send command output to CloudWatch Logs.



DocumentHash (string) --
The SHA-256 or SHA-1 hash created by the system when the document was created. SHA-1 hashes have been deprecated.

DocumentHashType (string) --
SHA-256 or SHA-1. SHA-1 hashes have been deprecated.

DocumentVersion (string) --
The SSM document version to use in the request. You can specify $DEFAULT, $LATEST, or a specific version number. If you run commands by using the AWS CLI, then you must escape the first two options by using a backslash. If you specify a version number, then you don\'t need to use the backslash. For example:
--document-version "$DEFAULT"
--document-version "$LATEST"
--document-version "3"

NotificationConfig (dict) --
Configurations for sending notifications about command status changes on a per-instance basis.

NotificationArn (string) --
An Amazon Resource Name (ARN) for an Amazon Simple Notification Service (Amazon SNS) topic. Run Command pushes notifications about command status changes to this topic.

NotificationEvents (list) --
The different events for which you can receive notifications. These events include the following: All (events), InProgress, Success, TimedOut, Cancelled, Failed. To learn more about these events, see Monitoring Systems Manager status changes using Amazon SNS notifications in the AWS Systems Manager User Guide .

(string) --


NotificationType (string) --
Command: Receive notification when the status of a command changes. Invocation: For commands sent to multiple instances, receive notification on a per-instance basis when the status of a command changes.



OutputS3BucketName (string) --
The name of the S3 bucket.

OutputS3KeyPrefix (string) --
The S3 bucket subfolder.

Parameters (dict) --
The parameters for the RUN_COMMAND task execution.

(string) --
(list) --
(string) --






ServiceRoleArn (string) --
The ARN of the IAM service role to use to publish Amazon Simple Notification Service (Amazon SNS) notifications for maintenance window Run Command tasks.

TimeoutSeconds (integer) --
If this time is reached and the command has not already started running, it doesn\'t run.



Automation (dict) --
The parameters for an AUTOMATION task type.

DocumentVersion (string) --
The version of an Automation document to use during task execution.

Parameters (dict) --
The parameters for the AUTOMATION task.
For information about specifying and updating task parameters, see  RegisterTaskWithMaintenanceWindow and  UpdateMaintenanceWindowTask .

Note

LoggingInfo has been deprecated. To specify an S3 bucket to contain logs, instead use the OutputS3BucketName and OutputS3KeyPrefix options in the TaskInvocationParameters structure. For information about how Systems Manager handles these options for the supported maintenance window task types, see  MaintenanceWindowTaskInvocationParameters .
TaskParameters has been deprecated. To specify parameters to pass to a task when it runs, instead use the Parameters option in the TaskInvocationParameters structure. For information about how Systems Manager handles these options for the supported maintenance window task types, see  MaintenanceWindowTaskInvocationParameters .

For AUTOMATION task types, Systems Manager ignores any values specified for these parameters.


(string) --
(list) --
(string) --








StepFunctions (dict) --
The parameters for a STEP_FUNCTIONS task type.

Input (string) --
The inputs for the STEP_FUNCTIONS task.

Name (string) --
The name of the STEP_FUNCTIONS task.



Lambda (dict) --
The parameters for a LAMBDA task type.

ClientContext (string) --
Pass client-specific information to the Lambda function that you are invoking. You can then process the client information in your Lambda function as you choose through the context variable.

Qualifier (string) --
(Optional) Specify a Lambda function version or alias name. If you specify a function version, the action uses the qualified function ARN to invoke a specific Lambda function. If you specify an alias name, the action uses the alias ARN to invoke the Lambda function version to which the alias points.

Payload (bytes) --
JSON to provide to your Lambda function as input.





Priority (integer) --
The priority of the task when it runs. The lower the number, the higher the priority. Tasks that have the same priority are scheduled in parallel.

MaxConcurrency (string) --
The maximum number of targets allowed to run this task in parallel.

MaxErrors (string) --
The maximum number of errors allowed before the task stops being scheduled.

LoggingInfo (dict) --
The location in Amazon S3 where the task results are logged.

Note
LoggingInfo has been deprecated. To specify an S3 bucket to contain logs, instead use the OutputS3BucketName and OutputS3KeyPrefix options in the TaskInvocationParameters structure. For information about how Systems Manager handles these options for the supported maintenance window task types, see  MaintenanceWindowTaskInvocationParameters .


S3BucketName (string) --
The name of an S3 bucket where execution logs are stored .

S3KeyPrefix (string) --
(Optional) The S3 bucket subfolder.

S3Region (string) --
The Region where the S3 bucket is located.



Name (string) --
The retrieved task name.

Description (string) --
The retrieved task description.







Exceptions

SSM.Client.exceptions.DoesNotExistException
SSM.Client.exceptions.InternalServerError


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
                'CloudWatchOutputConfig': {
                    'CloudWatchLogGroupName': 'string',
                    'CloudWatchOutputEnabled': True|False
                },
                'DocumentHash': 'string',
                'DocumentHashType': 'Sha256'|'Sha1',
                'DocumentVersion': 'string',
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
    ``Key=InstanceIds,Values=*instance-id-1* ,*instance-id-2* ,*instance-id-3* ``
    ``Key=tag:my-tag-key ,Values=*my-tag-value-1* ,*my-tag-value-2* ``
    ``Key=tag-key,Values=*my-tag-key-1* ,*my-tag-key-2* ``
    (Maintenance window targets only) ``Key=resource-groups:Name,Values=*resource-group-name* ``
    (Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*resource-type-1* ,*resource-type-2* ``
    
    """
    pass

def get_ops_item(OpsItemId=None):
    """
    Get information about an OpsItem by using the ID. You must have permission in AWS Identity and Access Management (IAM) to view information about an OpsItem. For more information, see Getting started with OpsCenter in the AWS Systems Manager User Guide .
    Operations engineers and IT professionals use OpsCenter to view, investigate, and remediate operational issues impacting the performance and health of their AWS resources. For more information, see AWS Systems Manager OpsCenter in the AWS Systems Manager User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_ops_item(
        OpsItemId='string'
    )
    
    
    :type OpsItemId: string
    :param OpsItemId: [REQUIRED]\nThe ID of the OpsItem that you want to get.\n

    :rtype: dict
ReturnsResponse Syntax{
    'OpsItem': {
        'CreatedBy': 'string',
        'CreatedTime': datetime(2015, 1, 1),
        'Description': 'string',
        'LastModifiedBy': 'string',
        'LastModifiedTime': datetime(2015, 1, 1),
        'Notifications': [
            {
                'Arn': 'string'
            },
        ],
        'Priority': 123,
        'RelatedOpsItems': [
            {
                'OpsItemId': 'string'
            },
        ],
        'Status': 'Open'|'InProgress'|'Resolved',
        'OpsItemId': 'string',
        'Version': 'string',
        'Title': 'string',
        'Source': 'string',
        'OperationalData': {
            'string': {
                'Value': 'string',
                'Type': 'SearchableString'|'String'
            }
        },
        'Category': 'string',
        'Severity': 'string'
    }
}


Response Structure

(dict) --
OpsItem (dict) --The OpsItem.

CreatedBy (string) --The ARN of the AWS account that created the OpsItem.

CreatedTime (datetime) --The date and time the OpsItem was created.

Description (string) --The OpsItem description.

LastModifiedBy (string) --The ARN of the AWS account that last updated the OpsItem.

LastModifiedTime (datetime) --The date and time the OpsItem was last updated.

Notifications (list) --The Amazon Resource Name (ARN) of an SNS topic where notifications are sent when this OpsItem is edited or changed.

(dict) --A notification about the OpsItem.

Arn (string) --The Amazon Resource Name (ARN) of an SNS topic where notifications are sent when this OpsItem is edited or changed.





Priority (integer) --The importance of this OpsItem in relation to other OpsItems in the system.

RelatedOpsItems (list) --One or more OpsItems that share something in common with the current OpsItem. For example, related OpsItems can include OpsItems with similar error messages, impacted resources, or statuses for the impacted resource.

(dict) --An OpsItems that shares something in common with the current OpsItem. For example, related OpsItems can include OpsItems with similar error messages, impacted resources, or statuses for the impacted resource.

OpsItemId (string) --The ID of an OpsItem related to the current OpsItem.





Status (string) --The OpsItem status. Status can be Open , In Progress , or Resolved . For more information, see Editing OpsItem details in the AWS Systems Manager User Guide .

OpsItemId (string) --The ID of the OpsItem.

Version (string) --The version of this OpsItem. Each time the OpsItem is edited the version number increments by one.

Title (string) --A short heading that describes the nature of the OpsItem and the impacted resource.

Source (string) --The origin of the OpsItem, such as Amazon EC2 or Systems Manager. The impacted resource is a subset of source.

OperationalData (dict) --Operational data is custom data that provides useful reference details about the OpsItem. For example, you can specify log files, error strings, license keys, troubleshooting tips, or other relevant data. You enter operational data as key-value pairs. The key has a maximum length of 128 characters. The value has a maximum size of 20 KB.

Warning
Operational data keys can\'t begin with the following: amazon, aws, amzn, ssm, /amazon, /aws, /amzn, /ssm.

You can choose to make the data searchable by other users in the account or you can restrict search access. Searchable data means that all users with access to the OpsItem Overview page (as provided by the  DescribeOpsItems API action) can view and search on the specified data. Operational data that is not searchable is only viewable by users who have access to the OpsItem (as provided by the  GetOpsItem API action).
Use the /aws/resources key in OperationalData to specify a related resource in the request. Use the /aws/automations key in OperationalData to associate an Automation runbook with the OpsItem. To view AWS CLI example commands that use these keys, see Creating OpsItems manually in the AWS Systems Manager User Guide .

(string) --
(dict) --An object that defines the value of the key and its type in the OperationalData map.

Value (string) --The value of the OperationalData key.

Type (string) --The type of key-value pair. Valid types include SearchableString and String .







Category (string) --An OpsItem category. Category options include: Availability, Cost, Performance, Recovery, Security.

Severity (string) --The severity of the OpsItem. Severity options range from 1 to 4.








Exceptions

SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.OpsItemNotFoundException


    :return: {
        'OpsItem': {
            'CreatedBy': 'string',
            'CreatedTime': datetime(2015, 1, 1),
            'Description': 'string',
            'LastModifiedBy': 'string',
            'LastModifiedTime': datetime(2015, 1, 1),
            'Notifications': [
                {
                    'Arn': 'string'
                },
            ],
            'Priority': 123,
            'RelatedOpsItems': [
                {
                    'OpsItemId': 'string'
                },
            ],
            'Status': 'Open'|'InProgress'|'Resolved',
            'OpsItemId': 'string',
            'Version': 'string',
            'Title': 'string',
            'Source': 'string',
            'OperationalData': {
                'string': {
                    'Value': 'string',
                    'Type': 'SearchableString'|'String'
                }
            },
            'Category': 'string',
            'Severity': 'string'
        }
    }
    
    
    """
    pass

def get_ops_summary(SyncName=None, Filters=None, Aggregators=None, ResultAttributes=None, NextToken=None, MaxResults=None):
    """
    View a summary of OpsItems based on specified filters and aggregators.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_ops_summary(
        SyncName='string',
        Filters=[
            {
                'Key': 'string',
                'Values': [
                    'string',
                ],
                'Type': 'Equal'|'NotEqual'|'BeginWith'|'LessThan'|'GreaterThan'|'Exists'
            },
        ],
        Aggregators=[
            {
                'AggregatorType': 'string',
                'TypeName': 'string',
                'AttributeName': 'string',
                'Values': {
                    'string': 'string'
                },
                'Filters': [
                    {
                        'Key': 'string',
                        'Values': [
                            'string',
                        ],
                        'Type': 'Equal'|'NotEqual'|'BeginWith'|'LessThan'|'GreaterThan'|'Exists'
                    },
                ],
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
    
    
    :type SyncName: string
    :param SyncName: Specify the name of a resource data sync to get.

    :type Filters: list
    :param Filters: Optional filters used to scope down the returned OpsItems.\n\n(dict) --A filter for viewing OpsItem summaries.\n\nKey (string) -- [REQUIRED]The name of the filter.\n\nValues (list) -- [REQUIRED]The filter value.\n\n(string) --\n\n\nType (string) --The type of filter.\n\n\n\n\n

    :type Aggregators: list
    :param Aggregators: Optional aggregators that return counts of OpsItems based on one or more expressions.\n\n(dict) --One or more aggregators for viewing counts of OpsItems using different dimensions such as Source , CreatedTime , or Source and CreatedTime , to name a few.\n\nAggregatorType (string) --Either a Range or Count aggregator for limiting an OpsItem summary.\n\nTypeName (string) --The data type name to use for viewing counts of OpsItems.\n\nAttributeName (string) --The name of an OpsItem attribute on which to limit the count of OpsItems.\n\nValues (dict) --The aggregator value.\n\n(string) --\n(string) --\n\n\n\n\nFilters (list) --The aggregator filters.\n\n(dict) --A filter for viewing OpsItem summaries.\n\nKey (string) -- [REQUIRED]The name of the filter.\n\nValues (list) -- [REQUIRED]The filter value.\n\n(string) --\n\n\nType (string) --The type of filter.\n\n\n\n\n\nAggregators (list) --A nested aggregator for viewing counts of OpsItems.\n\n\n\n\n

    :type ResultAttributes: list
    :param ResultAttributes: The OpsItem data type to return.\n\n(dict) --The OpsItem data type to return.\n\nTypeName (string) -- [REQUIRED]Name of the data type. Valid value: AWS:OpsItem, AWS:EC2InstanceInformation, AWS:OpsItemTrendline, or AWS:ComplianceSummary.\n\n\n\n\n

    :type NextToken: string
    :param NextToken: A token to start the list. Use this token to get the next set of results.

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'Entities': [
        {
            'Id': 'string',
            'Data': {
                'string': {
                    'CaptureTime': 'string',
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


Response Structure

(dict) --

Entities (list) --
The list of aggregated and filtered OpsItems.

(dict) --
The result of the query.

Id (string) --
The query ID.

Data (dict) --
The data returned by the query.

(string) --

(dict) --
The OpsItem summaries result item.

CaptureTime (string) --
The time OpsItem data was captured.

Content (list) --
The detailed data content for an OpsItem summaries result item.

(dict) --
(string) --
(string) --
















NextToken (string) --
The token for the next set of items to return. Use this token to get the next set of results.







Exceptions

SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.ResourceDataSyncNotFoundException
SSM.Client.exceptions.InvalidFilter
SSM.Client.exceptions.InvalidNextToken
SSM.Client.exceptions.InvalidTypeNameException
SSM.Client.exceptions.InvalidAggregatorException


    :return: {
        'Entities': [
            {
                'Id': 'string',
                'Data': {
                    'string': {
                        'CaptureTime': 'string',
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

def get_paginator(operation_name=None):
    """
    Create a paginator for an operation.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    :rtype: L{botocore.paginate.Paginator}
ReturnsA paginator object.


    """
    pass

def get_parameter(Name=None, WithDecryption=None):
    """
    Get information about a parameter by using the parameter name. Don\'t confuse this API action with the  GetParameters API action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_parameter(
        Name='string',
        WithDecryption=True|False
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the parameter you want to query.\n

    :type WithDecryption: boolean
    :param WithDecryption: Return decrypted values for secure string parameters. This flag is ignored for String and StringList parameter types.

    :rtype: dict

ReturnsResponse Syntax
{
    'Parameter': {
        'Name': 'string',
        'Type': 'String'|'StringList'|'SecureString',
        'Value': 'string',
        'Version': 123,
        'Selector': 'string',
        'SourceResult': 'string',
        'LastModifiedDate': datetime(2015, 1, 1),
        'ARN': 'string',
        'DataType': 'string'
    }
}


Response Structure

(dict) --

Parameter (dict) --
Information about a parameter.

Name (string) --
The name of the parameter.

Type (string) --
The type of parameter. Valid values include the following: String , StringList , and SecureString .

Value (string) --
The parameter value.

Version (integer) --
The parameter version.

Selector (string) --
Either the version number or the label used to retrieve the parameter value. Specify selectors by using one of the following formats:
parameter_name:version
parameter_name:label

SourceResult (string) --
Applies to parameters that reference information in other AWS services. SourceResult is the raw result or response from the source.

LastModifiedDate (datetime) --
Date the parameter was last changed or updated and the parameter version was created.

ARN (string) --
The Amazon Resource Name (ARN) of the parameter.

DataType (string) --
The data type of the parameter, such as text or aws:ec2:image . The default is text .









Exceptions

SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.InvalidKeyId
SSM.Client.exceptions.ParameterNotFound
SSM.Client.exceptions.ParameterVersionNotFound


    :return: {
        'Parameter': {
            'Name': 'string',
            'Type': 'String'|'StringList'|'SecureString',
            'Value': 'string',
            'Version': 123,
            'Selector': 'string',
            'SourceResult': 'string',
            'LastModifiedDate': datetime(2015, 1, 1),
            'ARN': 'string',
            'DataType': 'string'
        }
    }
    
    
    :returns: 
    SSM.Client.exceptions.InternalServerError
    SSM.Client.exceptions.InvalidKeyId
    SSM.Client.exceptions.ParameterNotFound
    SSM.Client.exceptions.ParameterVersionNotFound
    
    """
    pass

def get_parameter_history(Name=None, WithDecryption=None, MaxResults=None, NextToken=None):
    """
    Query a list of all parameters used by the AWS account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_parameter_history(
        Name='string',
        WithDecryption=True|False,
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of a parameter you want to query.\n

    :type WithDecryption: boolean
    :param WithDecryption: Return decrypted values for secure string parameters. This flag is ignored for String and StringList parameter types.

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :rtype: dict

ReturnsResponse Syntax
{
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
            'Version': 123,
            'Labels': [
                'string',
            ],
            'Tier': 'Standard'|'Advanced'|'Intelligent-Tiering',
            'Policies': [
                {
                    'PolicyText': 'string',
                    'PolicyType': 'string',
                    'PolicyStatus': 'string'
                },
            ],
            'DataType': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Parameters (list) --
A list of parameters returned by the request.

(dict) --
Information about parameter usage.

Name (string) --
The name of the parameter.

Type (string) --
The type of parameter used.

KeyId (string) --
The ID of the query key used for this parameter.

LastModifiedDate (datetime) --
Date the parameter was last changed or updated.

LastModifiedUser (string) --
Amazon Resource Name (ARN) of the AWS user who last changed the parameter.

Description (string) --
Information about the parameter.

Value (string) --
The parameter value.

AllowedPattern (string) --
Parameter names can include the following letters and symbols.
a-zA-Z0-9_.-

Version (integer) --
The parameter version.

Labels (list) --
Labels assigned to the parameter version.

(string) --


Tier (string) --
The parameter tier.

Policies (list) --
Information about the policies assigned to a parameter.

Assigning parameter policies in the AWS Systems Manager User Guide .


(dict) --
One or more policies assigned to a parameter.

PolicyText (string) --
The JSON text of the policy.

PolicyType (string) --
The type of policy. Parameter Store supports the following policy types: Expiration, ExpirationNotification, and NoChangeNotification.

PolicyStatus (string) --
The status of the policy. Policies report the following statuses: Pending (the policy has not been enforced or applied yet), Finished (the policy was applied), Failed (the policy was not applied), or InProgress (the policy is being applied now).





DataType (string) --
The data type of the parameter, such as text or aws:ec2:image . The default is text .





NextToken (string) --
The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.







Exceptions

SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.ParameterNotFound
SSM.Client.exceptions.InvalidNextToken
SSM.Client.exceptions.InvalidKeyId


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
                'Version': 123,
                'Labels': [
                    'string',
                ],
                'Tier': 'Standard'|'Advanced'|'Intelligent-Tiering',
                'Policies': [
                    {
                        'PolicyText': 'string',
                        'PolicyType': 'string',
                        'PolicyStatus': 'string'
                    },
                ],
                'DataType': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_parameters(Names=None, WithDecryption=None):
    """
    Get details of a parameter. Don\'t confuse this API action with the  GetParameter API action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_parameters(
        Names=[
            'string',
        ],
        WithDecryption=True|False
    )
    
    
    :type Names: list
    :param Names: [REQUIRED]\nNames of the parameters for which you want to query information.\n\n(string) --\n\n

    :type WithDecryption: boolean
    :param WithDecryption: Return decrypted secure string value. Return decrypted values for secure string parameters. This flag is ignored for String and StringList parameter types.

    :rtype: dict

ReturnsResponse Syntax
{
    'Parameters': [
        {
            'Name': 'string',
            'Type': 'String'|'StringList'|'SecureString',
            'Value': 'string',
            'Version': 123,
            'Selector': 'string',
            'SourceResult': 'string',
            'LastModifiedDate': datetime(2015, 1, 1),
            'ARN': 'string',
            'DataType': 'string'
        },
    ],
    'InvalidParameters': [
        'string',
    ]
}


Response Structure

(dict) --

Parameters (list) --
A list of details for a parameter.

(dict) --
An Systems Manager parameter in Parameter Store.

Name (string) --
The name of the parameter.

Type (string) --
The type of parameter. Valid values include the following: String , StringList , and SecureString .

Value (string) --
The parameter value.

Version (integer) --
The parameter version.

Selector (string) --
Either the version number or the label used to retrieve the parameter value. Specify selectors by using one of the following formats:
parameter_name:version
parameter_name:label

SourceResult (string) --
Applies to parameters that reference information in other AWS services. SourceResult is the raw result or response from the source.

LastModifiedDate (datetime) --
Date the parameter was last changed or updated and the parameter version was created.

ARN (string) --
The Amazon Resource Name (ARN) of the parameter.

DataType (string) --
The data type of the parameter, such as text or aws:ec2:image . The default is text .





InvalidParameters (list) --
A list of parameters that are not formatted correctly or do not run during an execution.

(string) --








Exceptions

SSM.Client.exceptions.InvalidKeyId
SSM.Client.exceptions.InternalServerError


    :return: {
        'Parameters': [
            {
                'Name': 'string',
                'Type': 'String'|'StringList'|'SecureString',
                'Value': 'string',
                'Version': 123,
                'Selector': 'string',
                'SourceResult': 'string',
                'LastModifiedDate': datetime(2015, 1, 1),
                'ARN': 'string',
                'DataType': 'string'
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
    Retrieve information about one or more parameters in a specific hierarchy.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param Path: [REQUIRED]\nThe hierarchy for the parameter. Hierarchies start with a forward slash (/) and end with the parameter name. A parameter name hierarchy can have a maximum of 15 levels. Here is an example of a hierarchy: /Finance/Prod/IAD/WinServ2016/license33\n

    :type Recursive: boolean
    :param Recursive: Retrieve all parameters within a hierarchy.\n\nWarning\nIf a user has access to a path, then the user can access all levels of that path. For example, if a user has permission to access path /a , then the user can also access /a/b . Even if a user has explicitly been denied access in IAM for parameter /a/b , they can still call the GetParametersByPath API action recursively for /a and view /a/b .\n\n

    :type ParameterFilters: list
    :param ParameterFilters: Filters to limit the request results.\n\n(dict) --One or more filters. Use a filter to return a more specific list of results.\n\nWarning\nThe ParameterStringFilter object is used by the DescribeParameters and GetParametersByPath API actions. However, not all of the pattern values listed for Key can be used with both actions.\nFor DescribeActions , all of the listed patterns are valid, with the exception of Label .\nFor GetParametersByPath , the following patterns listed for Key are not valid: Name , Path , and Tier .\nFor examples of CLI commands demonstrating valid parameter filter constructions, see Searching for Systems Manager parameters in the AWS Systems Manager User Guide .\n\n\nKey (string) -- [REQUIRED]The name of the filter.\n\nOption (string) --For all filters used with DescribeParameters , valid options include Equals and BeginsWith . The Name filter additionally supports the Contains option. (Exception: For filters using the key Path , valid options include Recursive and OneLevel .)\nFor filters used with GetParametersByPath , valid options include Equals and BeginsWith . (Exception: For filters using the key Label , the only valid option is Equals .)\n\nValues (list) --The value you want to search for.\n\n(string) --\n\n\n\n\n\n

    :type WithDecryption: boolean
    :param WithDecryption: Retrieve all parameters in a hierarchy with their value decrypted.

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :type NextToken: string
    :param NextToken: A token to start the list. Use this token to get the next set of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'Parameters': [
        {
            'Name': 'string',
            'Type': 'String'|'StringList'|'SecureString',
            'Value': 'string',
            'Version': 123,
            'Selector': 'string',
            'SourceResult': 'string',
            'LastModifiedDate': datetime(2015, 1, 1),
            'ARN': 'string',
            'DataType': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Parameters (list) --
A list of parameters found in the specified hierarchy.

(dict) --
An Systems Manager parameter in Parameter Store.

Name (string) --
The name of the parameter.

Type (string) --
The type of parameter. Valid values include the following: String , StringList , and SecureString .

Value (string) --
The parameter value.

Version (integer) --
The parameter version.

Selector (string) --
Either the version number or the label used to retrieve the parameter value. Specify selectors by using one of the following formats:
parameter_name:version
parameter_name:label

SourceResult (string) --
Applies to parameters that reference information in other AWS services. SourceResult is the raw result or response from the source.

LastModifiedDate (datetime) --
Date the parameter was last changed or updated and the parameter version was created.

ARN (string) --
The Amazon Resource Name (ARN) of the parameter.

DataType (string) --
The data type of the parameter, such as text or aws:ec2:image . The default is text .





NextToken (string) --
The token for the next set of items to return. Use this token to get the next set of results.







Exceptions

SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.InvalidFilterKey
SSM.Client.exceptions.InvalidFilterOption
SSM.Client.exceptions.InvalidFilterValue
SSM.Client.exceptions.InvalidKeyId
SSM.Client.exceptions.InvalidNextToken


    :return: {
        'Parameters': [
            {
                'Name': 'string',
                'Type': 'String'|'StringList'|'SecureString',
                'Value': 'string',
                'Version': 123,
                'Selector': 'string',
                'SourceResult': 'string',
                'LastModifiedDate': datetime(2015, 1, 1),
                'ARN': 'string',
                'DataType': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    SSM.Client.exceptions.InternalServerError
    SSM.Client.exceptions.InvalidFilterKey
    SSM.Client.exceptions.InvalidFilterOption
    SSM.Client.exceptions.InvalidFilterValue
    SSM.Client.exceptions.InvalidKeyId
    SSM.Client.exceptions.InvalidNextToken
    
    """
    pass

def get_patch_baseline(BaselineId=None):
    """
    Retrieves information about a patch baseline.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_patch_baseline(
        BaselineId='string'
    )
    
    
    :type BaselineId: string
    :param BaselineId: [REQUIRED]\nThe ID of the patch baseline to retrieve.\n

    :rtype: dict
ReturnsResponse Syntax{
    'BaselineId': 'string',
    'Name': 'string',
    'OperatingSystem': 'WINDOWS'|'AMAZON_LINUX'|'AMAZON_LINUX_2'|'UBUNTU'|'REDHAT_ENTERPRISE_LINUX'|'SUSE'|'CENTOS'|'ORACLE_LINUX'|'DEBIAN',
    'GlobalFilters': {
        'PatchFilters': [
            {
                'Key': 'PATCH_SET'|'PRODUCT'|'PRODUCT_FAMILY'|'CLASSIFICATION'|'MSRC_SEVERITY'|'PATCH_ID'|'SECTION'|'PRIORITY'|'SEVERITY',
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
                            'Key': 'PATCH_SET'|'PRODUCT'|'PRODUCT_FAMILY'|'CLASSIFICATION'|'MSRC_SEVERITY'|'PATCH_ID'|'SECTION'|'PRIORITY'|'SEVERITY',
                            'Values': [
                                'string',
                            ]
                        },
                    ]
                },
                'ComplianceLevel': 'CRITICAL'|'HIGH'|'MEDIUM'|'LOW'|'INFORMATIONAL'|'UNSPECIFIED',
                'ApproveAfterDays': 123,
                'ApproveUntilDate': 'string',
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
    'RejectedPatchesAction': 'ALLOW_AS_DEPENDENCY'|'BLOCK',
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


Response Structure

(dict) --
BaselineId (string) --The ID of the retrieved patch baseline.

Name (string) --The name of the patch baseline.

OperatingSystem (string) --Returns the operating system specified for the patch baseline.

GlobalFilters (dict) --A set of global filters used to exclude patches from the baseline.

PatchFilters (list) --The set of patch filters that make up the group.

(dict) --Defines which patches should be included in a patch baseline.
A patch filter consists of a key and a set of values. The filter key is a patch property. For example, the available filter keys for WINDOWS are PATCH_SET, PRODUCT, PRODUCT_FAMILY, CLASSIFICATION, and MSRC_SEVERITY. The filter values define a matching criterion for the patch property indicated by the key. For example, if the filter key is PRODUCT and the filter values are ["Office 2013", "Office 2016"], then the filter accepts all patches where product name is either "Office 2013" or "Office 2016". The filter values can be exact values for the patch property given as a key, or a wildcard (*), which matches all values.
You can view lists of valid values for the patch properties by running the DescribePatchProperties command. For information about which patch properties can be used with each major operating system, see  DescribePatchProperties .

Key (string) --The key for the filter.
Run the  DescribePatchProperties command to view lists of valid keys for each operating system type.

Values (list) --The value for the filter key.
Run the  DescribePatchProperties command to view lists of valid values for each key based on operating system type.

(string) --








ApprovalRules (dict) --A set of rules used to include patches in the baseline.

PatchRules (list) --The rules that make up the rule group.

(dict) --Defines an approval rule for a patch baseline.

PatchFilterGroup (dict) --The patch filter group that defines the criteria for the rule.

PatchFilters (list) --The set of patch filters that make up the group.

(dict) --Defines which patches should be included in a patch baseline.
A patch filter consists of a key and a set of values. The filter key is a patch property. For example, the available filter keys for WINDOWS are PATCH_SET, PRODUCT, PRODUCT_FAMILY, CLASSIFICATION, and MSRC_SEVERITY. The filter values define a matching criterion for the patch property indicated by the key. For example, if the filter key is PRODUCT and the filter values are ["Office 2013", "Office 2016"], then the filter accepts all patches where product name is either "Office 2013" or "Office 2016". The filter values can be exact values for the patch property given as a key, or a wildcard (*), which matches all values.
You can view lists of valid values for the patch properties by running the DescribePatchProperties command. For information about which patch properties can be used with each major operating system, see  DescribePatchProperties .

Key (string) --The key for the filter.
Run the  DescribePatchProperties command to view lists of valid keys for each operating system type.

Values (list) --The value for the filter key.
Run the  DescribePatchProperties command to view lists of valid values for each key based on operating system type.

(string) --








ComplianceLevel (string) --A compliance severity level for all approved patches in a patch baseline.

ApproveAfterDays (integer) --The number of days after the release date of each patch matched by the rule that the patch is marked as approved in the patch baseline. For example, a value of 7 means that patches are approved seven days after they are released. Not supported on Ubuntu Server.

ApproveUntilDate (string) --The cutoff date for auto approval of released patches. Any patches released on or before this date are installed automatically. Not supported on Ubuntu Server.
Enter dates in the format YYYY-MM-DD . For example, 2020-12-31 .

EnableNonSecurity (boolean) --For instances identified by the approval rule filters, enables a patch baseline to apply non-security updates available in the specified repository. The default value is \'false\'. Applies to Linux instances only.







ApprovedPatches (list) --A list of explicitly approved patches for the baseline.

(string) --


ApprovedPatchesComplianceLevel (string) --Returns the specified compliance severity level for approved patches in the patch baseline.

ApprovedPatchesEnableNonSecurity (boolean) --Indicates whether the list of approved patches includes non-security updates that should be applied to the instances. The default value is \'false\'. Applies to Linux instances only.

RejectedPatches (list) --A list of explicitly rejected patches for the baseline.

(string) --


RejectedPatchesAction (string) --The action specified to take on patches included in the RejectedPatches list. A patch can be allowed only if it is a dependency of another package, or blocked entirely along with packages that include it as a dependency.

PatchGroups (list) --Patch groups included in the patch baseline.

(string) --


CreatedDate (datetime) --The date the patch baseline was created.

ModifiedDate (datetime) --The date the patch baseline was last modified.

Description (string) --A description of the patch baseline.

Sources (list) --Information about the patches to use to update the instances, including target operating systems and source repositories. Applies to Linux instances only.

(dict) --Information about the patches to use to update the instances, including target operating systems and source repository. Applies to Linux instances only.

Name (string) --The name specified to identify the patch source.

Products (list) --The specific operating system versions a patch repository applies to, such as "Ubuntu16.04", "AmazonLinux2016.09", "RedhatEnterpriseLinux7.2" or "Suse12.7". For lists of supported product values, see  PatchFilter .

(string) --


Configuration (string) --The value of the yum repo configuration. For example:

[main]cachedir=/var/cache/yum/$basesearch$releasever
keepcache=0
debuglevel=2











Exceptions

SSM.Client.exceptions.DoesNotExistException
SSM.Client.exceptions.InvalidResourceId
SSM.Client.exceptions.InternalServerError


    :return: {
        'BaselineId': 'string',
        'Name': 'string',
        'OperatingSystem': 'WINDOWS'|'AMAZON_LINUX'|'AMAZON_LINUX_2'|'UBUNTU'|'REDHAT_ENTERPRISE_LINUX'|'SUSE'|'CENTOS'|'ORACLE_LINUX'|'DEBIAN',
        'GlobalFilters': {
            'PatchFilters': [
                {
                    'Key': 'PATCH_SET'|'PRODUCT'|'PRODUCT_FAMILY'|'CLASSIFICATION'|'MSRC_SEVERITY'|'PATCH_ID'|'SECTION'|'PRIORITY'|'SEVERITY',
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
                                'Key': 'PATCH_SET'|'PRODUCT'|'PRODUCT_FAMILY'|'CLASSIFICATION'|'MSRC_SEVERITY'|'PATCH_ID'|'SECTION'|'PRIORITY'|'SEVERITY',
                                'Values': [
                                    'string',
                                ]
                            },
                        ]
                    },
                    'ComplianceLevel': 'CRITICAL'|'HIGH'|'MEDIUM'|'LOW'|'INFORMATIONAL'|'UNSPECIFIED',
                    'ApproveAfterDays': 123,
                    'ApproveUntilDate': 'string',
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
        'RejectedPatchesAction': 'ALLOW_AS_DEPENDENCY'|'BLOCK',
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
    (string) --
    
    """
    pass

def get_patch_baseline_for_patch_group(PatchGroup=None, OperatingSystem=None):
    """
    Retrieves the patch baseline that should be used for the specified patch group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_patch_baseline_for_patch_group(
        PatchGroup='string',
        OperatingSystem='WINDOWS'|'AMAZON_LINUX'|'AMAZON_LINUX_2'|'UBUNTU'|'REDHAT_ENTERPRISE_LINUX'|'SUSE'|'CENTOS'|'ORACLE_LINUX'|'DEBIAN'
    )
    
    
    :type PatchGroup: string
    :param PatchGroup: [REQUIRED]\nThe name of the patch group whose patch baseline should be retrieved.\n

    :type OperatingSystem: string
    :param OperatingSystem: Returns he operating system rule specified for patch groups using the patch baseline.

    :rtype: dict

ReturnsResponse Syntax
{
    'BaselineId': 'string',
    'PatchGroup': 'string',
    'OperatingSystem': 'WINDOWS'|'AMAZON_LINUX'|'AMAZON_LINUX_2'|'UBUNTU'|'REDHAT_ENTERPRISE_LINUX'|'SUSE'|'CENTOS'|'ORACLE_LINUX'|'DEBIAN'
}


Response Structure

(dict) --

BaselineId (string) --
The ID of the patch baseline that should be used for the patch group.

PatchGroup (string) --
The name of the patch group.

OperatingSystem (string) --
The operating system rule specified for patch groups using the patch baseline.







Exceptions

SSM.Client.exceptions.InternalServerError


    :return: {
        'BaselineId': 'string',
        'PatchGroup': 'string',
        'OperatingSystem': 'WINDOWS'|'AMAZON_LINUX'|'AMAZON_LINUX_2'|'UBUNTU'|'REDHAT_ENTERPRISE_LINUX'|'SUSE'|'CENTOS'|'ORACLE_LINUX'|'DEBIAN'
    }
    
    
    :returns: 
    SSM.Client.exceptions.InternalServerError
    
    """
    pass

def get_service_setting(SettingId=None):
    """
    Services map a SettingId object to a setting value. AWS services teams define the default value for a SettingId . You can\'t create a new SettingId , but you can overwrite the default value if you have the ssm:UpdateServiceSetting permission for the setting. Use the  UpdateServiceSetting API action to change the default setting. Or use the  ResetServiceSetting to change the value back to the original value defined by the AWS service team.
    Query the current service setting for the account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_service_setting(
        SettingId='string'
    )
    
    
    :type SettingId: string
    :param SettingId: [REQUIRED]\nThe ID of the service setting to get. The setting ID can be /ssm/parameter-store/default-parameter-tier , /ssm/parameter-store/high-throughput-enabled , or /ssm/managed-instance/activation-tier .\n

    :rtype: dict
ReturnsResponse Syntax{
    'ServiceSetting': {
        'SettingId': 'string',
        'SettingValue': 'string',
        'LastModifiedDate': datetime(2015, 1, 1),
        'LastModifiedUser': 'string',
        'ARN': 'string',
        'Status': 'string'
    }
}


Response Structure

(dict) --The query result body of the GetServiceSetting API action.

ServiceSetting (dict) --The query result of the current service setting.

SettingId (string) --The ID of the service setting.

SettingValue (string) --The value of the service setting.

LastModifiedDate (datetime) --The last time the service setting was modified.

LastModifiedUser (string) --The ARN of the last modified user. This field is populated only if the setting value was overwritten.

ARN (string) --The ARN of the service setting.

Status (string) --The status of the service setting. The value can be Default, Customized or PendingUpdate.

Default: The current setting uses a default value provisioned by the AWS service team.
Customized: The current setting use a custom value specified by the customer.
PendingUpdate: The current setting uses a default or custom value, but a setting change request is pending approval.









Exceptions

SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.ServiceSettingNotFound


    :return: {
        'ServiceSetting': {
            'SettingId': 'string',
            'SettingValue': 'string',
            'LastModifiedDate': datetime(2015, 1, 1),
            'LastModifiedUser': 'string',
            'ARN': 'string',
            'Status': 'string'
        }
    }
    
    
    :returns: 
    SSM.Client.exceptions.InternalServerError
    SSM.Client.exceptions.ServiceSettingNotFound
    
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

def label_parameter_version(Name=None, ParameterVersion=None, Labels=None):
    """
    A parameter label is a user-defined alias to help you manage different versions of a parameter. When you modify a parameter, Systems Manager automatically saves a new version and increments the version number by one. A label can help you remember the purpose of a parameter when there are multiple versions.
    Parameter labels have the following requirements and restrictions.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.label_parameter_version(
        Name='string',
        ParameterVersion=123,
        Labels=[
            'string',
        ]
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe parameter name on which you want to attach one or more labels.\n

    :type ParameterVersion: integer
    :param ParameterVersion: The specific version of the parameter on which you want to attach one or more labels. If no version is specified, the system attaches the label to the latest version.

    :type Labels: list
    :param Labels: [REQUIRED]\nOne or more labels to attach to the specified parameter version.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'InvalidLabels': [
        'string',
    ],
    'ParameterVersion': 123
}


Response Structure

(dict) --

InvalidLabels (list) --
The label does not meet the requirements. For information about parameter label requirements, see Labeling parameters in the AWS Systems Manager User Guide .

(string) --


ParameterVersion (integer) --
The version of the parameter that has been labeled.







Exceptions

SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.TooManyUpdates
SSM.Client.exceptions.ParameterNotFound
SSM.Client.exceptions.ParameterVersionNotFound
SSM.Client.exceptions.ParameterVersionLabelLimitExceeded


    :return: {
        'InvalidLabels': [
            'string',
        ],
        'ParameterVersion': 123
    }
    
    
    :returns: 
    Name (string) -- [REQUIRED]
    The parameter name on which you want to attach one or more labels.
    
    ParameterVersion (integer) -- The specific version of the parameter on which you want to attach one or more labels. If no version is specified, the system attaches the label to the latest version.
    Labels (list) -- [REQUIRED]
    One or more labels to attach to the specified parameter version.
    
    (string) --
    
    
    
    """
    pass

def list_association_versions(AssociationId=None, MaxResults=None, NextToken=None):
    """
    Retrieves all versions of an association for a specific association ID.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_association_versions(
        AssociationId='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type AssociationId: string
    :param AssociationId: [REQUIRED]\nThe association ID for which you want to view all versions.\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :type NextToken: string
    :param NextToken: A token to start the list. Use this token to get the next set of results.

    :rtype: dict

ReturnsResponse Syntax
{
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
            'AssociationName': 'string',
            'MaxErrors': 'string',
            'MaxConcurrency': 'string',
            'ComplianceSeverity': 'CRITICAL'|'HIGH'|'MEDIUM'|'LOW'|'UNSPECIFIED',
            'SyncCompliance': 'AUTO'|'MANUAL'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

AssociationVersions (list) --
Information about all versions of the association for the specified association ID.

(dict) --
Information about the association version.

AssociationId (string) --
The ID created by the system when the association was created.

AssociationVersion (string) --
The association version.

CreatedDate (datetime) --
The date the association version was created.

Name (string) --
The name specified when the association was created.

DocumentVersion (string) --
The version of a Systems Manager document used when the association version was created.

Parameters (dict) --
Parameters specified when the association version was created.

(string) --
(list) --
(string) --






Targets (list) --
The targets specified for the association when the association version was created.

(dict) --
An array of search criteria that targets instances using a Key,Value combination that you specify.
Supported formats include the following.

``Key=InstanceIds,Values=*instance-id-1* ,*instance-id-2* ,*instance-id-3* ``
``Key=tag:my-tag-key ,Values=*my-tag-value-1* ,*my-tag-value-2* ``
``Key=tag-key,Values=*my-tag-key-1* ,*my-tag-key-2* ``
(Maintenance window targets only) ``Key=resource-groups:Name,Values=*resource-group-name* ``
(Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*resource-type-1* ,*resource-type-2* ``

For example:

Key=InstanceIds,Values=i-02573cafcfEXAMPLE,i-0471e04240EXAMPLE,i-07782c72faEXAMPLE
Key=tag:CostCenter,Values=CostCenter1,CostCenter2,CostCenter3
Key=tag-key,Values=Name,Instance-Type,CostCenter
(Maintenance window targets only) Key=resource-groups:Name,Values=ProductionResourceGroup   This example demonstrates how to target all resources in the resource group ProductionResourceGroup in your maintenance window.
(Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*AWS::EC2::INSTANCE* ,*AWS::EC2::VPC* ``   This example demonstrates how to target only EC2 instances and VPCs in your maintenance window.
(State Manager association targets only) Key=InstanceIds,Values=*   This example demonstrates how to target all managed instances in the AWS Region where the association was created.

For information about how to send commands that target instances using Key,Value parameters, see Targeting multiple instances in the AWS Systems Manager User Guide .

Key (string) --
User-defined criteria for sending commands that target instances that meet the criteria.

Values (list) --
User-defined criteria that maps to Key . For example, if you specified tag:ServerRole , you could specify value:WebServer to run a command on instances that include EC2 tags of ServerRole,WebServer .

(string) --






ScheduleExpression (string) --
The cron or rate schedule specified for the association when the association version was created.

OutputLocation (dict) --
The location in Amazon S3 specified for the association when the association version was created.

S3Location (dict) --
An S3 bucket where you want to store the results of this request.

OutputS3Region (string) --
(Deprecated) You can no longer specify this parameter. The system ignores it. Instead, Systems Manager automatically determines the Region of the S3 bucket.

OutputS3BucketName (string) --
The name of the S3 bucket.

OutputS3KeyPrefix (string) --
The S3 bucket subfolder.





AssociationName (string) --
The name specified for the association version when the association version was created.

MaxErrors (string) --
The number of errors that are allowed before the system stops sending requests to run the association on additional targets. You can specify either an absolute number of errors, for example 10, or a percentage of the target set, for example 10%. If you specify 3, for example, the system stops sending requests when the fourth error is received. If you specify 0, then the system stops sending requests after the first error is returned. If you run an association on 50 instances and set MaxError to 10%, then the system stops sending the request when the sixth error is received.
Executions that are already running an association when MaxErrors is reached are allowed to complete, but some of these executions may fail as well. If you need to ensure that there won\'t be more than max-errors failed executions, set MaxConcurrency to 1 so that executions proceed one at a time.

MaxConcurrency (string) --
The maximum number of targets allowed to run the association at the same time. You can specify a number, for example 10, or a percentage of the target set, for example 10%. The default value is 100%, which means all targets run the association at the same time.
If a new instance starts and attempts to run an association while Systems Manager is running MaxConcurrency associations, the association is allowed to run. During the next association interval, the new instance will process its association within the limit specified for MaxConcurrency.

ComplianceSeverity (string) --
The severity level that is assigned to the association.

SyncCompliance (string) --
The mode for generating association compliance. You can specify AUTO or MANUAL . In AUTO mode, the system uses the status of the association execution to determine the compliance status. If the association execution runs successfully, then the association is COMPLIANT . If the association execution doesn\'t run successfully, the association is NON-COMPLIANT .
In MANUAL mode, you must specify the AssociationId as a parameter for the  PutComplianceItems API action. In this case, compliance data is not managed by State Manager. It is managed by your direct call to the  PutComplianceItems API action.
By default, all associations use AUTO mode.





NextToken (string) --
The token for the next set of items to return. Use this token to get the next set of results.







Exceptions

SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.InvalidNextToken
SSM.Client.exceptions.AssociationDoesNotExist


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
                'AssociationName': 'string',
                'MaxErrors': 'string',
                'MaxConcurrency': 'string',
                'ComplianceSeverity': 'CRITICAL'|'HIGH'|'MEDIUM'|'LOW'|'UNSPECIFIED',
                'SyncCompliance': 'AUTO'|'MANUAL'
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
    Returns all State Manager associations in the current AWS account and Region. You can limit the results to a specific State Manager association document or instance by specifying a filter.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_associations(
        AssociationFilterList=[
            {
                'key': 'InstanceId'|'Name'|'AssociationId'|'AssociationStatusName'|'LastExecutedBefore'|'LastExecutedAfter'|'AssociationName'|'ResourceGroupName',
                'value': 'string'
            },
        ],
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type AssociationFilterList: list
    :param AssociationFilterList: One or more filters. Use a filter to return a more specific list of results.\n\n(dict) --Describes a filter.\n\nkey (string) -- [REQUIRED]The name of the filter.\n\nvalue (string) -- [REQUIRED]The filter value.\n\n\n\n\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

Associations (list) --
The associations.

(dict) --
Describes an association of a Systems Manager document and an instance.

Name (string) --
The name of the Systems Manager document.

InstanceId (string) --
The ID of the instance.

AssociationId (string) --
The ID created by the system when you create an association. An association is a binding between a document and a set of targets with a schedule.

AssociationVersion (string) --
The association version.

DocumentVersion (string) --
The version of the document used in the association.

Targets (list) --
The instances targeted by the request to create an association.

(dict) --
An array of search criteria that targets instances using a Key,Value combination that you specify.
Supported formats include the following.

``Key=InstanceIds,Values=*instance-id-1* ,*instance-id-2* ,*instance-id-3* ``
``Key=tag:my-tag-key ,Values=*my-tag-value-1* ,*my-tag-value-2* ``
``Key=tag-key,Values=*my-tag-key-1* ,*my-tag-key-2* ``
(Maintenance window targets only) ``Key=resource-groups:Name,Values=*resource-group-name* ``
(Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*resource-type-1* ,*resource-type-2* ``

For example:

Key=InstanceIds,Values=i-02573cafcfEXAMPLE,i-0471e04240EXAMPLE,i-07782c72faEXAMPLE
Key=tag:CostCenter,Values=CostCenter1,CostCenter2,CostCenter3
Key=tag-key,Values=Name,Instance-Type,CostCenter
(Maintenance window targets only) Key=resource-groups:Name,Values=ProductionResourceGroup   This example demonstrates how to target all resources in the resource group ProductionResourceGroup in your maintenance window.
(Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*AWS::EC2::INSTANCE* ,*AWS::EC2::VPC* ``   This example demonstrates how to target only EC2 instances and VPCs in your maintenance window.
(State Manager association targets only) Key=InstanceIds,Values=*   This example demonstrates how to target all managed instances in the AWS Region where the association was created.

For information about how to send commands that target instances using Key,Value parameters, see Targeting multiple instances in the AWS Systems Manager User Guide .

Key (string) --
User-defined criteria for sending commands that target instances that meet the criteria.

Values (list) --
User-defined criteria that maps to Key . For example, if you specified tag:ServerRole , you could specify value:WebServer to run a command on instances that include EC2 tags of ServerRole,WebServer .

(string) --






LastExecutionDate (datetime) --
The date on which the association was last run.

Overview (dict) --
Information about the association.

Status (string) --
The status of the association. Status can be: Pending, Success, or Failed.

DetailedStatus (string) --
A detailed status of the association.

AssociationStatusAggregatedCount (dict) --
Returns the number of targets for the association status. For example, if you created an association with two instances, and one of them was successful, this would return the count of instances by status.

(string) --
(integer) --






ScheduleExpression (string) --
A cron expression that specifies a schedule when the association runs.

AssociationName (string) --
The association name.





NextToken (string) --
The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.







Exceptions

SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.InvalidNextToken


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
    ``Key=InstanceIds,Values=*instance-id-1* ,*instance-id-2* ,*instance-id-3* ``
    ``Key=tag:my-tag-key ,Values=*my-tag-value-1* ,*my-tag-value-2* ``
    ``Key=tag-key,Values=*my-tag-key-1* ,*my-tag-key-2* ``
    (Maintenance window targets only) ``Key=resource-groups:Name,Values=*resource-group-name* ``
    (Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*resource-type-1* ,*resource-type-2* ``
    
    """
    pass

def list_command_invocations(CommandId=None, InstanceId=None, MaxResults=None, NextToken=None, Filters=None, Details=None):
    """
    An invocation is copy of a command sent to a specific instance. A command can apply to one or more instances. A command invocation applies to one instance. For example, if a user runs SendCommand against three instances, then a command invocation is created for each requested instance ID. ListCommandInvocations provide status about command execution.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_command_invocations(
        CommandId='string',
        InstanceId='string',
        MaxResults=123,
        NextToken='string',
        Filters=[
            {
                'key': 'InvokedAfter'|'InvokedBefore'|'Status'|'ExecutionStage'|'DocumentName',
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
    :param Filters: (Optional) One or more filters. Use a filter to return a more specific list of results.\n\n(dict) --Describes a command filter.\n\nkey (string) -- [REQUIRED]The name of the filter.\n\nvalue (string) -- [REQUIRED]The filter value. Valid values for each filter key are as follows:\n\nInvokedAfter : Specify a timestamp to limit your results. For example, specify 2018-07-07T00:00:00Z to see a list of command executions occurring July 7, 2018, and later.\nInvokedBefore : Specify a timestamp to limit your results. For example, specify 2018-07-07T00:00:00Z to see a list of command executions from before July 7, 2018.\nStatus : Specify a valid command status to see a list of all command executions with that status. Status values you can specify include:\nPending\nInProgress\nSuccess\nCancelled\nFailed\nTimedOut\nCancelling\n\n\nDocumentName : Specify name of the SSM document for which you want to see command execution results. For example, specify AWS-RunPatchBaseline to see command executions that used this SSM document to perform security patching operations on instances.\nExecutionStage : Specify one of the following values:\nExecuting : Returns a list of command executions that are currently still running.\nComplete : Returns a list of command executions that have already completed.\n\n\n\n\n\n\n\n

    :type Details: boolean
    :param Details: (Optional) If set this returns the response of the command executions and any command output. By default this is set to False.

    :rtype: dict

ReturnsResponse Syntax
{
    'CommandInvocations': [
        {
            'CommandId': 'string',
            'InstanceId': 'string',
            'InstanceName': 'string',
            'Comment': 'string',
            'DocumentName': 'string',
            'DocumentVersion': 'string',
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
            },
            'CloudWatchOutputConfig': {
                'CloudWatchLogGroupName': 'string',
                'CloudWatchOutputEnabled': True|False
            }
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

CommandInvocations (list) --
(Optional) A list of all invocations.

(dict) --
An invocation is copy of a command sent to a specific instance. A command can apply to one or more instances. A command invocation applies to one instance. For example, if a user runs SendCommand against three instances, then a command invocation is created for each requested instance ID. A command invocation returns status and detail information about a command you ran.

CommandId (string) --
The command against which this invocation was requested.

InstanceId (string) --
The instance ID in which this invocation was requested.

InstanceName (string) --
The name of the invocation target. For EC2 instances this is the value for the aws:Name tag. For on-premises instances, this is the name of the instance.

Comment (string) --
User-specified information about the command, such as a brief description of what the command should do.

DocumentName (string) --
The document name that was requested for execution.

DocumentVersion (string) --
The SSM document version.

RequestedDateTime (datetime) --
The time and date the request was sent to this instance.

Status (string) --
Whether or not the invocation succeeded, failed, or is pending.

StatusDetails (string) --
A detailed status of the command execution for each invocation (each instance targeted by the command). StatusDetails includes more information than Status because it includes states resulting from error and concurrency control parameters. StatusDetails can show different results than Status. For more information about these statuses, see Understanding command statuses in the AWS Systems Manager User Guide . StatusDetails can be one of the following values:

Pending: The command has not been sent to the instance.
In Progress: The command has been sent to the instance but has not reached a terminal state.
Success: The execution of the command or plugin was successfully completed. This is a terminal state.
Delivery Timed Out: The command was not delivered to the instance before the delivery timeout expired. Delivery timeouts do not count against the parent command\'s MaxErrors limit, but they do contribute to whether the parent command status is Success or Incomplete. This is a terminal state.
Execution Timed Out: Command execution started on the instance, but the execution was not complete before the execution timeout expired. Execution timeouts count against the MaxErrors limit of the parent command. This is a terminal state.
Failed: The command was not successful on the instance. For a plugin, this indicates that the result code was not zero. For a command invocation, this indicates that the result code for one or more plugins was not zero. Invocation failures count against the MaxErrors limit of the parent command. This is a terminal state.
Canceled: The command was terminated before it was completed. This is a terminal state.
Undeliverable: The command can\'t be delivered to the instance. The instance might not exist or might not be responding. Undeliverable invocations don\'t count against the parent command\'s MaxErrors limit and don\'t contribute to whether the parent command status is Success or Incomplete. This is a terminal state.
Terminated: The parent command exceeded its MaxErrors limit and subsequent command invocations were canceled by the system. This is a terminal state.


TraceOutput (string) --
Gets the trace output sent by the agent.

StandardOutputUrl (string) --
The URL to the plugin\'s StdOut file in Amazon S3, if the S3 bucket was defined for the parent command. For an invocation, StandardOutputUrl is populated if there is just one plugin defined for the command, and the S3 bucket was defined for the command.

StandardErrorUrl (string) --
The URL to the plugin\'s StdErr file in Amazon S3, if the S3 bucket was defined for the parent command. For an invocation, StandardErrorUrl is populated if there is just one plugin defined for the command, and the S3 bucket was defined for the command.

CommandPlugins (list) --

(dict) --
Describes plugin details.

Name (string) --
The name of the plugin. Must be one of the following: aws:updateAgent, aws:domainjoin, aws:applications, aws:runPowerShellScript, aws:psmodule, aws:cloudWatch, aws:runShellScript, or aws:updateSSMAgent.

Status (string) --
The status of this plugin. You can run a document with multiple plugins.

StatusDetails (string) --
A detailed status of the plugin execution. StatusDetails includes more information than Status because it includes states resulting from error and concurrency control parameters. StatusDetails can show different results than Status. For more information about these statuses, see Understanding command statuses in the AWS Systems Manager User Guide . StatusDetails can be one of the following values:

Pending: The command has not been sent to the instance.
In Progress: The command has been sent to the instance but has not reached a terminal state.
Success: The execution of the command or plugin was successfully completed. This is a terminal state.
Delivery Timed Out: The command was not delivered to the instance before the delivery timeout expired. Delivery timeouts do not count against the parent command\'s MaxErrors limit, but they do contribute to whether the parent command status is Success or Incomplete. This is a terminal state.
Execution Timed Out: Command execution started on the instance, but the execution was not complete before the execution timeout expired. Execution timeouts count against the MaxErrors limit of the parent command. This is a terminal state.
Failed: The command was not successful on the instance. For a plugin, this indicates that the result code was not zero. For a command invocation, this indicates that the result code for one or more plugins was not zero. Invocation failures count against the MaxErrors limit of the parent command. This is a terminal state.
Canceled: The command was terminated before it was completed. This is a terminal state.
Undeliverable: The command can\'t be delivered to the instance. The instance might not exist, or it might not be responding. Undeliverable invocations don\'t count against the parent command\'s MaxErrors limit, and they don\'t contribute to whether the parent command status is Success or Incomplete. This is a terminal state.
Terminated: The parent command exceeded its MaxErrors limit and subsequent command invocations were canceled by the system. This is a terminal state.


ResponseCode (integer) --
A numeric response code generated after running the plugin.

ResponseStartDateTime (datetime) --
The time the plugin started running.

ResponseFinishDateTime (datetime) --
The time the plugin stopped running. Could stop prematurely if, for example, a cancel command was sent.

Output (string) --
Output of the plugin execution.

StandardOutputUrl (string) --
The URL for the complete text written by the plugin to stdout in Amazon S3. If the S3 bucket for the command was not specified, then this string is empty.

StandardErrorUrl (string) --
The URL for the complete text written by the plugin to stderr. If execution is not yet complete, then this string is empty.

OutputS3Region (string) --
(Deprecated) You can no longer specify this parameter. The system ignores it. Instead, Systems Manager automatically determines the S3 bucket region.

OutputS3BucketName (string) --
The S3 bucket where the responses to the command executions should be stored. This was requested when issuing the command. For example, in the following response:
test_folder/ab19cb99-a030-46dd-9dfc-8eSAMPLEPre-Fix/i-1234567876543/awsrunShellScript
test_folder is the name of the S3 bucket;
ab19cb99-a030-46dd-9dfc-8eSAMPLEPre-Fix is the name of the S3 prefix;
i-1234567876543 is the instance ID;
awsrunShellScript is the name of the plugin.

OutputS3KeyPrefix (string) --
The S3 directory path inside the bucket where the responses to the command executions should be stored. This was requested when issuing the command. For example, in the following response:
test_folder/ab19cb99-a030-46dd-9dfc-8eSAMPLEPre-Fix/i-1234567876543/awsrunShellScript
test_folder is the name of the S3 bucket;
ab19cb99-a030-46dd-9dfc-8eSAMPLEPre-Fix is the name of the S3 prefix;
i-1234567876543 is the instance ID;
awsrunShellScript is the name of the plugin.





ServiceRole (string) --
The IAM service role that Run Command uses to act on your behalf when sending notifications about command status changes on a per instance basis.

NotificationConfig (dict) --
Configurations for sending notifications about command status changes on a per instance basis.

NotificationArn (string) --
An Amazon Resource Name (ARN) for an Amazon Simple Notification Service (Amazon SNS) topic. Run Command pushes notifications about command status changes to this topic.

NotificationEvents (list) --
The different events for which you can receive notifications. These events include the following: All (events), InProgress, Success, TimedOut, Cancelled, Failed. To learn more about these events, see Monitoring Systems Manager status changes using Amazon SNS notifications in the AWS Systems Manager User Guide .

(string) --


NotificationType (string) --
Command: Receive notification when the status of a command changes. Invocation: For commands sent to multiple instances, receive notification on a per-instance basis when the status of a command changes.



CloudWatchOutputConfig (dict) --
CloudWatch Logs information where you want Systems Manager to send the command output.

CloudWatchLogGroupName (string) --
The name of the CloudWatch log group where you want to send command output. If you don\'t specify a group name, Systems Manager automatically creates a log group for you. The log group uses the following naming format: aws/ssm/SystemsManagerDocumentName .

CloudWatchOutputEnabled (boolean) --
Enables Systems Manager to send command output to CloudWatch Logs.







NextToken (string) --
(Optional) The token for the next set of items to return. (You received this token from a previous call.)







Exceptions

SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.InvalidCommandId
SSM.Client.exceptions.InvalidInstanceId
SSM.Client.exceptions.InvalidFilterKey
SSM.Client.exceptions.InvalidNextToken


    :return: {
        'CommandInvocations': [
            {
                'CommandId': 'string',
                'InstanceId': 'string',
                'InstanceName': 'string',
                'Comment': 'string',
                'DocumentName': 'string',
                'DocumentVersion': 'string',
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
                },
                'CloudWatchOutputConfig': {
                    'CloudWatchLogGroupName': 'string',
                    'CloudWatchOutputEnabled': True|False
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Pending: The command has not been sent to the instance.
    In Progress: The command has been sent to the instance but has not reached a terminal state.
    Success: The execution of the command or plugin was successfully completed. This is a terminal state.
    Delivery Timed Out: The command was not delivered to the instance before the delivery timeout expired. Delivery timeouts do not count against the parent command\'s MaxErrors limit, but they do contribute to whether the parent command status is Success or Incomplete. This is a terminal state.
    Execution Timed Out: Command execution started on the instance, but the execution was not complete before the execution timeout expired. Execution timeouts count against the MaxErrors limit of the parent command. This is a terminal state.
    Failed: The command was not successful on the instance. For a plugin, this indicates that the result code was not zero. For a command invocation, this indicates that the result code for one or more plugins was not zero. Invocation failures count against the MaxErrors limit of the parent command. This is a terminal state.
    Canceled: The command was terminated before it was completed. This is a terminal state.
    Undeliverable: The command can\'t be delivered to the instance. The instance might not exist or might not be responding. Undeliverable invocations don\'t count against the parent command\'s MaxErrors limit and don\'t contribute to whether the parent command status is Success or Incomplete. This is a terminal state.
    Terminated: The parent command exceeded its MaxErrors limit and subsequent command invocations were canceled by the system. This is a terminal state.
    
    """
    pass

def list_commands(CommandId=None, InstanceId=None, MaxResults=None, NextToken=None, Filters=None):
    """
    Lists the commands requested by users of the AWS account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_commands(
        CommandId='string',
        InstanceId='string',
        MaxResults=123,
        NextToken='string',
        Filters=[
            {
                'key': 'InvokedAfter'|'InvokedBefore'|'Status'|'ExecutionStage'|'DocumentName',
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
    :param Filters: (Optional) One or more filters. Use a filter to return a more specific list of results.\n\n(dict) --Describes a command filter.\n\nkey (string) -- [REQUIRED]The name of the filter.\n\nvalue (string) -- [REQUIRED]The filter value. Valid values for each filter key are as follows:\n\nInvokedAfter : Specify a timestamp to limit your results. For example, specify 2018-07-07T00:00:00Z to see a list of command executions occurring July 7, 2018, and later.\nInvokedBefore : Specify a timestamp to limit your results. For example, specify 2018-07-07T00:00:00Z to see a list of command executions from before July 7, 2018.\nStatus : Specify a valid command status to see a list of all command executions with that status. Status values you can specify include:\nPending\nInProgress\nSuccess\nCancelled\nFailed\nTimedOut\nCancelling\n\n\nDocumentName : Specify name of the SSM document for which you want to see command execution results. For example, specify AWS-RunPatchBaseline to see command executions that used this SSM document to perform security patching operations on instances.\nExecutionStage : Specify one of the following values:\nExecuting : Returns a list of command executions that are currently still running.\nComplete : Returns a list of command executions that have already completed.\n\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Commands': [
        {
            'CommandId': 'string',
            'DocumentName': 'string',
            'DocumentVersion': 'string',
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
            'DeliveryTimedOutCount': 123,
            'ServiceRole': 'string',
            'NotificationConfig': {
                'NotificationArn': 'string',
                'NotificationEvents': [
                    'All'|'InProgress'|'Success'|'TimedOut'|'Cancelled'|'Failed',
                ],
                'NotificationType': 'Command'|'Invocation'
            },
            'CloudWatchOutputConfig': {
                'CloudWatchLogGroupName': 'string',
                'CloudWatchOutputEnabled': True|False
            },
            'TimeoutSeconds': 123
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Commands (list) --
(Optional) The list of commands requested by the user.

(dict) --
Describes a command request.

CommandId (string) --
A unique identifier for this command.

DocumentName (string) --
The name of the document requested for execution.

DocumentVersion (string) --
The SSM document version.

Comment (string) --
User-specified information about the command, such as a brief description of what the command should do.

ExpiresAfter (datetime) --
If this time is reached and the command has not already started running, it will not run. Calculated based on the ExpiresAfter user input provided as part of the SendCommand API.

Parameters (dict) --
The parameter values to be inserted in the document when running the command.

(string) --
(list) --
(string) --






InstanceIds (list) --
The instance IDs against which this command was requested.

(string) --


Targets (list) --
An array of search criteria that targets instances using a Key,Value combination that you specify. Targets is required if you don\'t provide one or more instance IDs in the call.

(dict) --
An array of search criteria that targets instances using a Key,Value combination that you specify.
Supported formats include the following.

``Key=InstanceIds,Values=*instance-id-1* ,*instance-id-2* ,*instance-id-3* ``
``Key=tag:my-tag-key ,Values=*my-tag-value-1* ,*my-tag-value-2* ``
``Key=tag-key,Values=*my-tag-key-1* ,*my-tag-key-2* ``
(Maintenance window targets only) ``Key=resource-groups:Name,Values=*resource-group-name* ``
(Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*resource-type-1* ,*resource-type-2* ``

For example:

Key=InstanceIds,Values=i-02573cafcfEXAMPLE,i-0471e04240EXAMPLE,i-07782c72faEXAMPLE
Key=tag:CostCenter,Values=CostCenter1,CostCenter2,CostCenter3
Key=tag-key,Values=Name,Instance-Type,CostCenter
(Maintenance window targets only) Key=resource-groups:Name,Values=ProductionResourceGroup   This example demonstrates how to target all resources in the resource group ProductionResourceGroup in your maintenance window.
(Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*AWS::EC2::INSTANCE* ,*AWS::EC2::VPC* ``   This example demonstrates how to target only EC2 instances and VPCs in your maintenance window.
(State Manager association targets only) Key=InstanceIds,Values=*   This example demonstrates how to target all managed instances in the AWS Region where the association was created.

For information about how to send commands that target instances using Key,Value parameters, see Targeting multiple instances in the AWS Systems Manager User Guide .

Key (string) --
User-defined criteria for sending commands that target instances that meet the criteria.

Values (list) --
User-defined criteria that maps to Key . For example, if you specified tag:ServerRole , you could specify value:WebServer to run a command on instances that include EC2 tags of ServerRole,WebServer .

(string) --






RequestedDateTime (datetime) --
The date and time the command was requested.

Status (string) --
The status of the command.

StatusDetails (string) --
A detailed status of the command execution. StatusDetails includes more information than Status because it includes states resulting from error and concurrency control parameters. StatusDetails can show different results than Status. For more information about these statuses, see Understanding command statuses in the AWS Systems Manager User Guide . StatusDetails can be one of the following values:

Pending: The command has not been sent to any instances.
In Progress: The command has been sent to at least one instance but has not reached a final state on all instances.
Success: The command successfully ran on all invocations. This is a terminal state.
Delivery Timed Out: The value of MaxErrors or more command invocations shows a status of Delivery Timed Out. This is a terminal state.
Execution Timed Out: The value of MaxErrors or more command invocations shows a status of Execution Timed Out. This is a terminal state.
Failed: The value of MaxErrors or more command invocations shows a status of Failed. This is a terminal state.
Incomplete: The command was attempted on all instances and one or more invocations does not have a value of Success but not enough invocations failed for the status to be Failed. This is a terminal state.
Canceled: The command was terminated before it was completed. This is a terminal state.
Rate Exceeded: The number of instances targeted by the command exceeded the account limit for pending invocations. The system has canceled the command before running it on any instance. This is a terminal state.


OutputS3Region (string) --
(Deprecated) You can no longer specify this parameter. The system ignores it. Instead, Systems Manager automatically determines the Region of the S3 bucket.

OutputS3BucketName (string) --
The S3 bucket where the responses to the command executions should be stored. This was requested when issuing the command.

OutputS3KeyPrefix (string) --
The S3 directory path inside the bucket where the responses to the command executions should be stored. This was requested when issuing the command.

MaxConcurrency (string) --
The maximum number of instances that are allowed to run the command at the same time. You can specify a number of instances, such as 10, or a percentage of instances, such as 10%. The default value is 50. For more information about how to use MaxConcurrency, see Running commands using Systems Manager Run Command in the AWS Systems Manager User Guide .

MaxErrors (string) --
The maximum number of errors allowed before the system stops sending the command to additional targets. You can specify a number of errors, such as 10, or a percentage or errors, such as 10%. The default value is 0. For more information about how to use MaxErrors, see Running commands using Systems Manager Run Command in the AWS Systems Manager User Guide .

TargetCount (integer) --
The number of targets for the command.

CompletedCount (integer) --
The number of targets for which the command invocation reached a terminal state. Terminal states include the following: Success, Failed, Execution Timed Out, Delivery Timed Out, Canceled, Terminated, or Undeliverable.

ErrorCount (integer) --
The number of targets for which the status is Failed or Execution Timed Out.

DeliveryTimedOutCount (integer) --
The number of targets for which the status is Delivery Timed Out.

ServiceRole (string) --
The IAM service role that Run Command uses to act on your behalf when sending notifications about command status changes.

NotificationConfig (dict) --
Configurations for sending notifications about command status changes.

NotificationArn (string) --
An Amazon Resource Name (ARN) for an Amazon Simple Notification Service (Amazon SNS) topic. Run Command pushes notifications about command status changes to this topic.

NotificationEvents (list) --
The different events for which you can receive notifications. These events include the following: All (events), InProgress, Success, TimedOut, Cancelled, Failed. To learn more about these events, see Monitoring Systems Manager status changes using Amazon SNS notifications in the AWS Systems Manager User Guide .

(string) --


NotificationType (string) --
Command: Receive notification when the status of a command changes. Invocation: For commands sent to multiple instances, receive notification on a per-instance basis when the status of a command changes.



CloudWatchOutputConfig (dict) --
CloudWatch Logs information where you want Systems Manager to send the command output.

CloudWatchLogGroupName (string) --
The name of the CloudWatch log group where you want to send command output. If you don\'t specify a group name, Systems Manager automatically creates a log group for you. The log group uses the following naming format: aws/ssm/SystemsManagerDocumentName .

CloudWatchOutputEnabled (boolean) --
Enables Systems Manager to send command output to CloudWatch Logs.



TimeoutSeconds (integer) --
The TimeoutSeconds value specified for a command.





NextToken (string) --
(Optional) The token for the next set of items to return. (You received this token from a previous call.)







Exceptions

SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.InvalidCommandId
SSM.Client.exceptions.InvalidInstanceId
SSM.Client.exceptions.InvalidFilterKey
SSM.Client.exceptions.InvalidNextToken


    :return: {
        'Commands': [
            {
                'CommandId': 'string',
                'DocumentName': 'string',
                'DocumentVersion': 'string',
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
                'DeliveryTimedOutCount': 123,
                'ServiceRole': 'string',
                'NotificationConfig': {
                    'NotificationArn': 'string',
                    'NotificationEvents': [
                        'All'|'InProgress'|'Success'|'TimedOut'|'Cancelled'|'Failed',
                    ],
                    'NotificationType': 'Command'|'Invocation'
                },
                'CloudWatchOutputConfig': {
                    'CloudWatchLogGroupName': 'string',
                    'CloudWatchOutputEnabled': True|False
                },
                'TimeoutSeconds': 123
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
    
    Exceptions
    
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
    :param Filters: One or more compliance filters. Use a filter to return a more specific list of results.\n\n(dict) --One or more filters. Use a filter to return a more specific list of results.\n\nKey (string) --The name of the filter.\n\nValues (list) --The value for which to search.\n\n(string) --\n\n\nType (string) --The type of comparison that should be performed for the value: Equal, NotEqual, BeginWith, LessThan, or GreaterThan.\n\n\n\n\n

    :type ResourceIds: list
    :param ResourceIds: The ID for the resources from which to get compliance information. Currently, you can only specify one resource ID.\n\n(string) --\n\n

    :type ResourceTypes: list
    :param ResourceTypes: The type of resource from which to get compliance information. Currently, the only supported resource type is ManagedInstance .\n\n(string) --\n\n

    :type NextToken: string
    :param NextToken: A token to start the list. Use this token to get the next set of results.

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

ComplianceItems (list) --
A list of compliance information for the specified resource ID.

(dict) --
Information about the compliance as defined by the resource type. For example, for a patch resource type, Items includes information about the PatchSeverity, Classification, and so on.

ComplianceType (string) --
The compliance type. For example, Association (for a State Manager association), Patch, or Custom:string are all valid compliance types.

ResourceType (string) --
The type of resource. ManagedInstance is currently the only supported resource type.

ResourceId (string) --
An ID for the resource. For a managed instance, this is the instance ID.

Id (string) --
An ID for the compliance item. For example, if the compliance item is a Windows patch, the ID could be the number of the KB article; for example: KB4010320.

Title (string) --
A title for the compliance item. For example, if the compliance item is a Windows patch, the title could be the title of the KB article for the patch; for example: Security Update for Active Directory Federation Services.

Status (string) --
The status of the compliance item. An item is either COMPLIANT or NON_COMPLIANT.

Severity (string) --
The severity of the compliance status. Severity can be one of the following: Critical, High, Medium, Low, Informational, Unspecified.

ExecutionSummary (dict) --
A summary for the compliance item. The summary includes an execution ID, the execution type (for example, command), and the execution time.

ExecutionTime (datetime) --
The time the execution ran as a datetime object that is saved in the following format: yyyy-MM-dd\'T\'HH:mm:ss\'Z\'.

ExecutionId (string) --
An ID created by the system when PutComplianceItems was called. For example, CommandID is a valid execution ID. You can use this ID in subsequent calls.

ExecutionType (string) --
The type of execution. For example, Command is a valid execution type.



Details (dict) --
A "Key": "Value" tag combination for the compliance item.

(string) --
(string) --








NextToken (string) --
The token for the next set of items to return. Use this token to get the next set of results.







Exceptions

SSM.Client.exceptions.InvalidResourceType
SSM.Client.exceptions.InvalidResourceId
SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.InvalidFilter
SSM.Client.exceptions.InvalidNextToken


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
    
    Exceptions
    
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
    :param Filters: One or more compliance or inventory filters. Use a filter to return a more specific list of results.\n\n(dict) --One or more filters. Use a filter to return a more specific list of results.\n\nKey (string) --The name of the filter.\n\nValues (list) --The value for which to search.\n\n(string) --\n\n\nType (string) --The type of comparison that should be performed for the value: Equal, NotEqual, BeginWith, LessThan, or GreaterThan.\n\n\n\n\n

    :type NextToken: string
    :param NextToken: A token to start the list. Use this token to get the next set of results.

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. Currently, you can specify null or 50. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

ComplianceSummaryItems (list) --
A list of compliant and non-compliant summary counts based on compliance types. For example, this call returns State Manager associations, patches, or custom compliance types according to the filter criteria that you specified.

(dict) --
A summary of compliance information by compliance type.

ComplianceType (string) --
The type of compliance item. For example, the compliance type can be Association, Patch, or Custom:string.

CompliantSummary (dict) --
A list of COMPLIANT items for the specified compliance type.

CompliantCount (integer) --
The total number of resources that are compliant.

SeveritySummary (dict) --
A summary of the compliance severity by compliance type.

CriticalCount (integer) --
The total number of resources or compliance items that have a severity level of critical. Critical severity is determined by the organization that published the compliance items.

HighCount (integer) --
The total number of resources or compliance items that have a severity level of high. High severity is determined by the organization that published the compliance items.

MediumCount (integer) --
The total number of resources or compliance items that have a severity level of medium. Medium severity is determined by the organization that published the compliance items.

LowCount (integer) --
The total number of resources or compliance items that have a severity level of low. Low severity is determined by the organization that published the compliance items.

InformationalCount (integer) --
The total number of resources or compliance items that have a severity level of informational. Informational severity is determined by the organization that published the compliance items.

UnspecifiedCount (integer) --
The total number of resources or compliance items that have a severity level of unspecified. Unspecified severity is determined by the organization that published the compliance items.





NonCompliantSummary (dict) --
A list of NON_COMPLIANT items for the specified compliance type.

NonCompliantCount (integer) --
The total number of compliance items that are not compliant.

SeveritySummary (dict) --
A summary of the non-compliance severity by compliance type

CriticalCount (integer) --
The total number of resources or compliance items that have a severity level of critical. Critical severity is determined by the organization that published the compliance items.

HighCount (integer) --
The total number of resources or compliance items that have a severity level of high. High severity is determined by the organization that published the compliance items.

MediumCount (integer) --
The total number of resources or compliance items that have a severity level of medium. Medium severity is determined by the organization that published the compliance items.

LowCount (integer) --
The total number of resources or compliance items that have a severity level of low. Low severity is determined by the organization that published the compliance items.

InformationalCount (integer) --
The total number of resources or compliance items that have a severity level of informational. Informational severity is determined by the organization that published the compliance items.

UnspecifiedCount (integer) --
The total number of resources or compliance items that have a severity level of unspecified. Unspecified severity is determined by the organization that published the compliance items.









NextToken (string) --
The token for the next set of items to return. Use this token to get the next set of results.







Exceptions

SSM.Client.exceptions.InvalidFilter
SSM.Client.exceptions.InvalidNextToken
SSM.Client.exceptions.InternalServerError


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
    
    
    :returns: 
    SSM.Client.exceptions.InvalidFilter
    SSM.Client.exceptions.InvalidNextToken
    SSM.Client.exceptions.InternalServerError
    
    """
    pass

def list_document_versions(Name=None, MaxResults=None, NextToken=None):
    """
    List all versions for a document.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_document_versions(
        Name='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the document. You can specify an Amazon Resource Name (ARN).\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :rtype: dict

ReturnsResponse Syntax
{
    'DocumentVersions': [
        {
            'Name': 'string',
            'DocumentVersion': 'string',
            'VersionName': 'string',
            'CreatedDate': datetime(2015, 1, 1),
            'IsDefaultVersion': True|False,
            'DocumentFormat': 'YAML'|'JSON'|'TEXT',
            'Status': 'Creating'|'Active'|'Updating'|'Deleting'|'Failed',
            'StatusInformation': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

DocumentVersions (list) --
The document versions.

(dict) --
Version information about the document.

Name (string) --
The document name.

DocumentVersion (string) --
The document version.

VersionName (string) --
The version of the artifact associated with the document. For example, "Release 12, Update 6". This value is unique across all versions of a document, and cannot be changed.

CreatedDate (datetime) --
The date the document was created.

IsDefaultVersion (boolean) --
An identifier for the default version of the document.

DocumentFormat (string) --
The document format, either JSON or YAML.

Status (string) --
The status of the Systems Manager document, such as Creating , Active , Failed , and Deleting .

StatusInformation (string) --
A message returned by AWS Systems Manager that explains the Status value. For example, a Failed status might be explained by the StatusInformation message, "The specified S3 bucket does not exist. Verify that the URL of the S3 bucket is correct."





NextToken (string) --
The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.







Exceptions

SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.InvalidNextToken
SSM.Client.exceptions.InvalidDocument


    :return: {
        'DocumentVersions': [
            {
                'Name': 'string',
                'DocumentVersion': 'string',
                'VersionName': 'string',
                'CreatedDate': datetime(2015, 1, 1),
                'IsDefaultVersion': True|False,
                'DocumentFormat': 'YAML'|'JSON'|'TEXT',
                'Status': 'Creating'|'Active'|'Updating'|'Deleting'|'Failed',
                'StatusInformation': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    SSM.Client.exceptions.InternalServerError
    SSM.Client.exceptions.InvalidNextToken
    SSM.Client.exceptions.InvalidDocument
    
    """
    pass

def list_documents(DocumentFilterList=None, Filters=None, MaxResults=None, NextToken=None):
    """
    Returns all Systems Manager (SSM) documents in the current AWS account and Region. You can limit the results of this request by using a filter.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param DocumentFilterList: This data type is deprecated. Instead, use Filters .\n\n(dict) --This data type is deprecated. Instead, use DocumentKeyValuesFilter .\n\nkey (string) -- [REQUIRED]The name of the filter.\n\nvalue (string) -- [REQUIRED]The value of the filter.\n\n\n\n\n

    :type Filters: list
    :param Filters: One or more DocumentKeyValuesFilter objects. Use a filter to return a more specific list of results. For keys, you can specify one or more key-value pair tags that have been applied to a document. Other valid keys include Owner , Name , PlatformTypes , DocumentType , and TargetType . For example, to return documents you own use Key=Owner,Values=Self . To specify a custom key-value pair, use the format Key=tag:tagName,Values=valueName .\n\n(dict) --One or more filters. Use a filter to return a more specific list of documents.\nFor keys, you can specify one or more tags that have been applied to a document.\nOther valid values include Owner , Name , PlatformTypes , DocumentType , and TargetType .\nNote that only one Owner can be specified in a request. For example: Key=Owner,Values=Self .\nIf you use Name as a key, you can use a name prefix to return a list of documents. For example, in the AWS CLI, to return a list of all documents that begin with Te , run the following command:\n\naws ssm list-documents --filters Key=Name,Values=Te\nIf you specify more than two keys, only documents that are identified by all the tags are returned in the results. If you specify more than two values for a key, documents that are identified by any of the values are returned in the results.\nTo specify a custom key and value pair, use the format Key=tag:tagName,Values=valueName .\nFor example, if you created a Key called region and are using the AWS CLI to call the list-documents command:\n\naws ssm list-documents --filters Key=tag:region,Values=east,west Key=Owner,Values=Self\n\nKey (string) --The name of the filter key.\n\nValues (list) --The value for the filter key.\n\n(string) --\n\n\n\n\n\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :rtype: dict

ReturnsResponse Syntax
{
    'DocumentIdentifiers': [
        {
            'Name': 'string',
            'Owner': 'string',
            'VersionName': 'string',
            'PlatformTypes': [
                'Windows'|'Linux',
            ],
            'DocumentVersion': 'string',
            'DocumentType': 'Command'|'Policy'|'Automation'|'Session'|'Package'|'ApplicationConfiguration'|'ApplicationConfigurationSchema'|'DeploymentStrategy'|'ChangeCalendar',
            'SchemaVersion': 'string',
            'DocumentFormat': 'YAML'|'JSON'|'TEXT',
            'TargetType': 'string',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'Requires': [
                {
                    'Name': 'string',
                    'Version': 'string'
                },
            ]
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

DocumentIdentifiers (list) --
The names of the Systems Manager documents.

(dict) --
Describes the name of a Systems Manager document.

Name (string) --
The name of the Systems Manager document.

Owner (string) --
The AWS user account that created the document.

VersionName (string) --
An optional field specifying the version of the artifact associated with the document. For example, "Release 12, Update 6". This value is unique across all versions of a document, and cannot be changed.

PlatformTypes (list) --
The operating system platform.

(string) --


DocumentVersion (string) --
The document version.

DocumentType (string) --
The document type.

SchemaVersion (string) --
The schema version.

DocumentFormat (string) --
The document format, either JSON or YAML.

TargetType (string) --
The target type which defines the kinds of resources the document can run on. For example, /AWS::EC2::Instance. For a list of valid resource types, see AWS resource and property types reference in the AWS CloudFormation User Guide .

Tags (list) --
The tags, or metadata, that have been applied to the document.

(dict) --
Metadata that you assign to your AWS resources. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment. In Systems Manager, you can apply tags to documents, managed instances, maintenance windows, Parameter Store parameters, and patch baselines.

Key (string) --
The name of the tag.

Value (string) --
The value of the tag.





Requires (list) --
A list of SSM documents required by a document. For example, an ApplicationConfiguration document requires an ApplicationConfigurationSchema document.

(dict) --
An SSM document required by the current document.

Name (string) --
The name of the required SSM document. The name can be an Amazon Resource Name (ARN).

Version (string) --
The document version required by the current document.









NextToken (string) --
The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.







Exceptions

SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.InvalidNextToken
SSM.Client.exceptions.InvalidFilterKey


    :return: {
        'DocumentIdentifiers': [
            {
                'Name': 'string',
                'Owner': 'string',
                'VersionName': 'string',
                'PlatformTypes': [
                    'Windows'|'Linux',
                ],
                'DocumentVersion': 'string',
                'DocumentType': 'Command'|'Policy'|'Automation'|'Session'|'Package'|'ApplicationConfiguration'|'ApplicationConfigurationSchema'|'DeploymentStrategy'|'ChangeCalendar',
                'SchemaVersion': 'string',
                'DocumentFormat': 'YAML'|'JSON'|'TEXT',
                'TargetType': 'string',
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],
                'Requires': [
                    {
                        'Name': 'string',
                        'Version': 'string'
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
    
    Exceptions
    
    :example: response = client.list_inventory_entries(
        InstanceId='string',
        TypeName='string',
        Filters=[
            {
                'Key': 'string',
                'Values': [
                    'string',
                ],
                'Type': 'Equal'|'NotEqual'|'BeginWith'|'LessThan'|'GreaterThan'|'Exists'
            },
        ],
        NextToken='string',
        MaxResults=123
    )
    
    
    :type InstanceId: string
    :param InstanceId: [REQUIRED]\nThe instance ID for which you want inventory information.\n

    :type TypeName: string
    :param TypeName: [REQUIRED]\nThe type of inventory item for which you want information.\n

    :type Filters: list
    :param Filters: One or more filters. Use a filter to return a more specific list of results.\n\n(dict) --One or more filters. Use a filter to return a more specific list of results.\n\nKey (string) -- [REQUIRED]The name of the filter key.\n\nValues (list) -- [REQUIRED]Inventory filter values. Example: inventory filter where instance IDs are specified as values Key=AWS:InstanceInformation.InstanceId,Values= i-a12b3c4d5e6g, i-1a2b3c4d5e6,Type=Equal\n\n(string) --\n\n\nType (string) --The type of filter.\n\nNote\nThe Exists filter must be used with aggregators. For more information, see Aggregating inventory data in the AWS Systems Manager User Guide .\n\n\n\n\n\n

    :type NextToken: string
    :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

TypeName (string) --
The type of inventory item returned by the request.

InstanceId (string) --
The instance ID targeted by the request to query inventory information.

SchemaVersion (string) --
The inventory schema version used by the instance(s).

CaptureTime (string) --
The time that inventory information was collected for the instance(s).

Entries (list) --
A list of inventory items on the instance(s).

(dict) --
(string) --
(string) --






NextToken (string) --
The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.







Exceptions

SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.InvalidInstanceId
SSM.Client.exceptions.InvalidTypeNameException
SSM.Client.exceptions.InvalidFilter
SSM.Client.exceptions.InvalidNextToken


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
    
    Exceptions
    
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
    :param Filters: One or more filters. Use a filter to return a more specific list of results.\n\n(dict) --One or more filters. Use a filter to return a more specific list of results.\n\nKey (string) --The name of the filter.\n\nValues (list) --The value for which to search.\n\n(string) --\n\n\nType (string) --The type of comparison that should be performed for the value: Equal, NotEqual, BeginWith, LessThan, or GreaterThan.\n\n\n\n\n

    :type NextToken: string
    :param NextToken: A token to start the list. Use this token to get the next set of results.

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

ResourceComplianceSummaryItems (list) --
A summary count for specified or targeted managed instances. Summary count includes information about compliant and non-compliant State Manager associations, patch status, or custom items according to the filter criteria that you specify.

(dict) --
Compliance summary information for a specific resource.

ComplianceType (string) --
The compliance type.

ResourceType (string) --
The resource type.

ResourceId (string) --
The resource ID.

Status (string) --
The compliance status for the resource.

OverallSeverity (string) --
The highest severity item found for the resource. The resource is compliant for this item.

ExecutionSummary (dict) --
Information about the execution.

ExecutionTime (datetime) --
The time the execution ran as a datetime object that is saved in the following format: yyyy-MM-dd\'T\'HH:mm:ss\'Z\'.

ExecutionId (string) --
An ID created by the system when PutComplianceItems was called. For example, CommandID is a valid execution ID. You can use this ID in subsequent calls.

ExecutionType (string) --
The type of execution. For example, Command is a valid execution type.



CompliantSummary (dict) --
A list of items that are compliant for the resource.

CompliantCount (integer) --
The total number of resources that are compliant.

SeveritySummary (dict) --
A summary of the compliance severity by compliance type.

CriticalCount (integer) --
The total number of resources or compliance items that have a severity level of critical. Critical severity is determined by the organization that published the compliance items.

HighCount (integer) --
The total number of resources or compliance items that have a severity level of high. High severity is determined by the organization that published the compliance items.

MediumCount (integer) --
The total number of resources or compliance items that have a severity level of medium. Medium severity is determined by the organization that published the compliance items.

LowCount (integer) --
The total number of resources or compliance items that have a severity level of low. Low severity is determined by the organization that published the compliance items.

InformationalCount (integer) --
The total number of resources or compliance items that have a severity level of informational. Informational severity is determined by the organization that published the compliance items.

UnspecifiedCount (integer) --
The total number of resources or compliance items that have a severity level of unspecified. Unspecified severity is determined by the organization that published the compliance items.





NonCompliantSummary (dict) --
A list of items that aren\'t compliant for the resource.

NonCompliantCount (integer) --
The total number of compliance items that are not compliant.

SeveritySummary (dict) --
A summary of the non-compliance severity by compliance type

CriticalCount (integer) --
The total number of resources or compliance items that have a severity level of critical. Critical severity is determined by the organization that published the compliance items.

HighCount (integer) --
The total number of resources or compliance items that have a severity level of high. High severity is determined by the organization that published the compliance items.

MediumCount (integer) --
The total number of resources or compliance items that have a severity level of medium. Medium severity is determined by the organization that published the compliance items.

LowCount (integer) --
The total number of resources or compliance items that have a severity level of low. Low severity is determined by the organization that published the compliance items.

InformationalCount (integer) --
The total number of resources or compliance items that have a severity level of informational. Informational severity is determined by the organization that published the compliance items.

UnspecifiedCount (integer) --
The total number of resources or compliance items that have a severity level of unspecified. Unspecified severity is determined by the organization that published the compliance items.









NextToken (string) --
The token for the next set of items to return. Use this token to get the next set of results.







Exceptions

SSM.Client.exceptions.InvalidFilter
SSM.Client.exceptions.InvalidNextToken
SSM.Client.exceptions.InternalServerError


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
    
    
    :returns: 
    SSM.Client.exceptions.InvalidFilter
    SSM.Client.exceptions.InvalidNextToken
    SSM.Client.exceptions.InternalServerError
    
    """
    pass

def list_resource_data_sync(SyncType=None, NextToken=None, MaxResults=None):
    """
    Lists your resource data sync configurations. Includes information about the last time a sync attempted to start, the last sync status, and the last time a sync successfully completed.
    The number of sync configurations might be too large to return using a single call to ListResourceDataSync . You can limit the number of sync configurations returned by using the MaxResults parameter. To determine whether there are more sync configurations to list, check the value of NextToken in the output. If there are more sync configurations to list, you can request them by specifying the NextToken returned in the call to the parameter of a subsequent call.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_resource_data_sync(
        SyncType='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type SyncType: string
    :param SyncType: View a list of resource data syncs according to the sync type. Specify SyncToDestination to view resource data syncs that synchronize data to an Amazon S3 buckets. Specify SyncFromSource to view resource data syncs from AWS Organizations or from multiple AWS Regions.

    :type NextToken: string
    :param NextToken: A token to start the list. Use this token to get the next set of results.

    :type MaxResults: integer
    :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'ResourceDataSyncItems': [
        {
            'SyncName': 'string',
            'SyncType': 'string',
            'SyncSource': {
                'SourceType': 'string',
                'AwsOrganizationsSource': {
                    'OrganizationSourceType': 'string',
                    'OrganizationalUnits': [
                        {
                            'OrganizationalUnitId': 'string'
                        },
                    ]
                },
                'SourceRegions': [
                    'string',
                ],
                'IncludeFutureRegions': True|False,
                'State': 'string'
            },
            'S3Destination': {
                'BucketName': 'string',
                'Prefix': 'string',
                'SyncFormat': 'JsonSerDe',
                'Region': 'string',
                'AWSKMSKeyARN': 'string',
                'DestinationDataSharing': {
                    'DestinationDataSharingType': 'string'
                }
            },
            'LastSyncTime': datetime(2015, 1, 1),
            'LastSuccessfulSyncTime': datetime(2015, 1, 1),
            'SyncLastModifiedTime': datetime(2015, 1, 1),
            'LastStatus': 'Successful'|'Failed'|'InProgress',
            'SyncCreatedTime': datetime(2015, 1, 1),
            'LastSyncStatusMessage': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

ResourceDataSyncItems (list) --
A list of your current Resource Data Sync configurations and their statuses.

(dict) --
Information about a Resource Data Sync configuration, including its current status and last successful sync.

SyncName (string) --
The name of the Resource Data Sync.

SyncType (string) --
The type of resource data sync. If SyncType is SyncToDestination , then the resource data sync synchronizes data to an S3 bucket. If the SyncType is SyncFromSource then the resource data sync synchronizes data from AWS Organizations or from multiple AWS Regions.

SyncSource (dict) --
Information about the source where the data was synchronized.

SourceType (string) --
The type of data source for the resource data sync. SourceType is either AwsOrganizations (if an organization is present in AWS Organizations) or singleAccountMultiRegions .

AwsOrganizationsSource (dict) --
The field name in SyncSource for the ResourceDataSyncAwsOrganizationsSource type.

OrganizationSourceType (string) --
If an AWS Organization is present, this is either OrganizationalUnits or EntireOrganization . For OrganizationalUnits , the data is aggregated from a set of organization units. For EntireOrganization , the data is aggregated from the entire AWS Organization.

OrganizationalUnits (list) --
The AWS Organizations organization units included in the sync.

(dict) --
The AWS Organizations organizational unit data source for the sync.

OrganizationalUnitId (string) --
The AWS Organization unit ID data source for the sync.







SourceRegions (list) --
The SyncSource AWS Regions included in the resource data sync.

(string) --


IncludeFutureRegions (boolean) --
Whether to automatically synchronize and aggregate data from new AWS Regions when those Regions come online.

State (string) --
The data type name for including resource data sync state. There are four sync states:

OrganizationNotExists : Your organization doesn\'t exist.
NoPermissions : The system can\'t locate the service-linked role. This role is automatically created when a user creates a resource data sync in Explorer.
InvalidOrganizationalUnit : You specified or selected an invalid unit in the resource data sync configuration.
TrustedAccessDisabled : You disabled Systems Manager access in the organization in AWS Organizations.




S3Destination (dict) --
Configuration information for the target S3 bucket.

BucketName (string) --
The name of the S3 bucket where the aggregated data is stored.

Prefix (string) --
An Amazon S3 prefix for the bucket.

SyncFormat (string) --
A supported sync format. The following format is currently supported: JsonSerDe

Region (string) --
The AWS Region with the S3 bucket targeted by the Resource Data Sync.

AWSKMSKeyARN (string) --
The ARN of an encryption key for a destination in Amazon S3. Must belong to the same Region as the destination S3 bucket.

DestinationDataSharing (dict) --
Enables destination data sharing. By default, this field is null .

DestinationDataSharingType (string) --
The sharing data type. Only Organization is supported.





LastSyncTime (datetime) --
The last time the configuration attempted to sync (UTC).

LastSuccessfulSyncTime (datetime) --
The last time the sync operations returned a status of SUCCESSFUL (UTC).

SyncLastModifiedTime (datetime) --
The date and time the resource data sync was changed.

LastStatus (string) --
The status reported by the last sync.

SyncCreatedTime (datetime) --
The date and time the configuration was created (UTC).

LastSyncStatusMessage (string) --
The status message details reported by the last sync.





NextToken (string) --
The token for the next set of items to return. Use this token to get the next set of results.







Exceptions

SSM.Client.exceptions.ResourceDataSyncInvalidConfigurationException
SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.InvalidNextToken


    :return: {
        'ResourceDataSyncItems': [
            {
                'SyncName': 'string',
                'SyncType': 'string',
                'SyncSource': {
                    'SourceType': 'string',
                    'AwsOrganizationsSource': {
                        'OrganizationSourceType': 'string',
                        'OrganizationalUnits': [
                            {
                                'OrganizationalUnitId': 'string'
                            },
                        ]
                    },
                    'SourceRegions': [
                        'string',
                    ],
                    'IncludeFutureRegions': True|False,
                    'State': 'string'
                },
                'S3Destination': {
                    'BucketName': 'string',
                    'Prefix': 'string',
                    'SyncFormat': 'JsonSerDe',
                    'Region': 'string',
                    'AWSKMSKeyARN': 'string',
                    'DestinationDataSharing': {
                        'DestinationDataSharingType': 'string'
                    }
                },
                'LastSyncTime': datetime(2015, 1, 1),
                'LastSuccessfulSyncTime': datetime(2015, 1, 1),
                'SyncLastModifiedTime': datetime(2015, 1, 1),
                'LastStatus': 'Successful'|'Failed'|'InProgress',
                'SyncCreatedTime': datetime(2015, 1, 1),
                'LastSyncStatusMessage': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_tags_for_resource(ResourceType=None, ResourceId=None):
    """
    Returns a list of the tags assigned to the specified resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        ResourceType='Document'|'ManagedInstance'|'MaintenanceWindow'|'Parameter'|'PatchBaseline'|'OpsItem',
        ResourceId='string'
    )
    
    
    :type ResourceType: string
    :param ResourceType: [REQUIRED]\nReturns a list of tags for a specific resource type.\n

    :type ResourceId: string
    :param ResourceId: [REQUIRED]\nThe resource ID for which you want to see a list of tags.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'TagList': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ]
}


Response Structure

(dict) --

TagList (list) --
A list of tags.

(dict) --
Metadata that you assign to your AWS resources. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment. In Systems Manager, you can apply tags to documents, managed instances, maintenance windows, Parameter Store parameters, and patch baselines.

Key (string) --
The name of the tag.

Value (string) --
The value of the tag.











Exceptions

SSM.Client.exceptions.InvalidResourceType
SSM.Client.exceptions.InvalidResourceId
SSM.Client.exceptions.InternalServerError


    :return: {
        'TagList': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    :returns: 
    SSM.Client.exceptions.InvalidResourceType
    SSM.Client.exceptions.InvalidResourceId
    SSM.Client.exceptions.InternalServerError
    
    """
    pass

def modify_document_permission(Name=None, PermissionType=None, AccountIdsToAdd=None, AccountIdsToRemove=None, SharedDocumentVersion=None):
    """
    Shares a Systems Manager document publicly or privately. If you share a document privately, you must specify the AWS user account IDs for those people who can use the document. If you share a document publicly, you must specify All as the account ID.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.modify_document_permission(
        Name='string',
        PermissionType='Share',
        AccountIdsToAdd=[
            'string',
        ],
        AccountIdsToRemove=[
            'string',
        ],
        SharedDocumentVersion='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the document that you want to share.\n

    :type PermissionType: string
    :param PermissionType: [REQUIRED]\nThe permission type for the document. The permission type can be Share .\n

    :type AccountIdsToAdd: list
    :param AccountIdsToAdd: The AWS user accounts that should have access to the document. The account IDs can either be a group of account IDs or All .\n\n(string) --\n\n

    :type AccountIdsToRemove: list
    :param AccountIdsToRemove: The AWS user accounts that should no longer have access to the document. The AWS user account can either be a group of account IDs or All . This action has a higher priority than AccountIdsToAdd . If you specify an account ID to add and the same ID to remove, the system removes access to the document.\n\n(string) --\n\n

    :type SharedDocumentVersion: string
    :param SharedDocumentVersion: (Optional) The version of the document to share. If it\'s not specified, the system choose the Default version to share.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.InvalidDocument
SSM.Client.exceptions.InvalidPermissionType
SSM.Client.exceptions.DocumentPermissionLimit
SSM.Client.exceptions.DocumentLimitExceeded


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def put_compliance_items(ResourceId=None, ResourceType=None, ComplianceType=None, ExecutionSummary=None, Items=None, ItemContentHash=None, UploadType=None):
    """
    Registers a compliance type and other compliance details on a designated resource. This action lets you register custom compliance details with a resource. This call overwrites existing compliance information on the resource, so you must provide a full list of compliance items each time that you send the request.
    ComplianceType can be one of the following:
    See also: AWS API Documentation
    
    Exceptions
    
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
        ItemContentHash='string',
        UploadType='COMPLETE'|'PARTIAL'
    )
    
    
    :type ResourceId: string
    :param ResourceId: [REQUIRED]\nSpecify an ID for this resource. For a managed instance, this is the instance ID.\n

    :type ResourceType: string
    :param ResourceType: [REQUIRED]\nSpecify the type of resource. ManagedInstance is currently the only supported resource type.\n

    :type ComplianceType: string
    :param ComplianceType: [REQUIRED]\nSpecify the compliance type. For example, specify Association (for a State Manager association), Patch, or Custom:string .\n

    :type ExecutionSummary: dict
    :param ExecutionSummary: [REQUIRED]\nA summary of the call execution that includes an execution ID, the type of execution (for example, Command ), and the date/time of the execution using a datetime object that is saved in the following format: yyyy-MM-dd\'T\'HH:mm:ss\'Z\'.\n\nExecutionTime (datetime) -- [REQUIRED]The time the execution ran as a datetime object that is saved in the following format: yyyy-MM-dd\'T\'HH:mm:ss\'Z\'.\n\nExecutionId (string) --An ID created by the system when PutComplianceItems was called. For example, CommandID is a valid execution ID. You can use this ID in subsequent calls.\n\nExecutionType (string) --The type of execution. For example, Command is a valid execution type.\n\n\n

    :type Items: list
    :param Items: [REQUIRED]\nInformation about the compliance as defined by the resource type. For example, for a patch compliance type, Items includes information about the PatchSeverity, Classification, and so on.\n\n(dict) --Information about a compliance item.\n\nId (string) --The compliance item ID. For example, if the compliance item is a Windows patch, the ID could be the number of the KB article.\n\nTitle (string) --The title of the compliance item. For example, if the compliance item is a Windows patch, the title could be the title of the KB article for the patch; for example: Security Update for Active Directory Federation Services.\n\nSeverity (string) -- [REQUIRED]The severity of the compliance status. Severity can be one of the following: Critical, High, Medium, Low, Informational, Unspecified.\n\nStatus (string) -- [REQUIRED]The status of the compliance item. An item is either COMPLIANT or NON_COMPLIANT.\n\nDetails (dict) --A 'Key': 'Value' tag combination for the compliance item.\n\n(string) --\n(string) --\n\n\n\n\n\n\n\n

    :type ItemContentHash: string
    :param ItemContentHash: MD5 or SHA-256 content hash. The content hash is used to determine if existing information should be overwritten or ignored. If the content hashes match, the request to put compliance information is ignored.

    :type UploadType: string
    :param UploadType: The mode for uploading compliance items. You can specify COMPLETE or PARTIAL . In COMPLETE mode, the system overwrites all existing compliance information for the resource. You must provide a full list of compliance items each time you send the request.\nIn PARTIAL mode, the system overwrites compliance information for a specific association. The association must be configured with SyncCompliance set to MANUAL . By default, all requests use COMPLETE mode.\n\nNote\nThis attribute is only valid for association compliance.\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.InvalidItemContentException
SSM.Client.exceptions.TotalSizeLimitExceededException
SSM.Client.exceptions.ItemSizeLimitExceededException
SSM.Client.exceptions.ComplianceTypeCountLimitExceededException
SSM.Client.exceptions.InvalidResourceType
SSM.Client.exceptions.InvalidResourceId


    :return: {}
    
    
    :returns: 
    ResourceId (string) -- [REQUIRED]
    Specify an ID for this resource. For a managed instance, this is the instance ID.
    
    ResourceType (string) -- [REQUIRED]
    Specify the type of resource. ManagedInstance is currently the only supported resource type.
    
    ComplianceType (string) -- [REQUIRED]
    Specify the compliance type. For example, specify Association (for a State Manager association), Patch, or Custom:string .
    
    ExecutionSummary (dict) -- [REQUIRED]
    A summary of the call execution that includes an execution ID, the type of execution (for example, Command ), and the date/time of the execution using a datetime object that is saved in the following format: yyyy-MM-dd\'T\'HH:mm:ss\'Z\'.
    
    ExecutionTime (datetime) -- [REQUIRED]The time the execution ran as a datetime object that is saved in the following format: yyyy-MM-dd\'T\'HH:mm:ss\'Z\'.
    
    ExecutionId (string) --An ID created by the system when PutComplianceItems was called. For example, CommandID is a valid execution ID. You can use this ID in subsequent calls.
    
    ExecutionType (string) --The type of execution. For example, Command is a valid execution type.
    
    
    
    Items (list) -- [REQUIRED]
    Information about the compliance as defined by the resource type. For example, for a patch compliance type, Items includes information about the PatchSeverity, Classification, and so on.
    
    (dict) --Information about a compliance item.
    
    Id (string) --The compliance item ID. For example, if the compliance item is a Windows patch, the ID could be the number of the KB article.
    
    Title (string) --The title of the compliance item. For example, if the compliance item is a Windows patch, the title could be the title of the KB article for the patch; for example: Security Update for Active Directory Federation Services.
    
    Severity (string) -- [REQUIRED]The severity of the compliance status. Severity can be one of the following: Critical, High, Medium, Low, Informational, Unspecified.
    
    Status (string) -- [REQUIRED]The status of the compliance item. An item is either COMPLIANT or NON_COMPLIANT.
    
    Details (dict) --A "Key": "Value" tag combination for the compliance item.
    
    (string) --
    (string) --
    
    
    
    
    
    
    
    
    ItemContentHash (string) -- MD5 or SHA-256 content hash. The content hash is used to determine if existing information should be overwritten or ignored. If the content hashes match, the request to put compliance information is ignored.
    UploadType (string) -- The mode for uploading compliance items. You can specify COMPLETE or PARTIAL . In COMPLETE mode, the system overwrites all existing compliance information for the resource. You must provide a full list of compliance items each time you send the request.
    In PARTIAL mode, the system overwrites compliance information for a specific association. The association must be configured with SyncCompliance set to MANUAL . By default, all requests use COMPLETE mode.
    
    Note
    This attribute is only valid for association compliance.
    
    
    
    """
    pass

def put_inventory(InstanceId=None, Items=None):
    """
    Bulk update custom inventory items on one more instance. The request adds an inventory item, if it doesn\'t already exist, or updates an inventory item, if it does exist.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param InstanceId: [REQUIRED]\nAn instance ID where you want to add or update inventory items.\n

    :type Items: list
    :param Items: [REQUIRED]\nThe inventory items that you want to add or update on instances.\n\n(dict) --Information collected from managed instances based on your inventory policy document\n\nTypeName (string) -- [REQUIRED]The name of the inventory type. Default inventory item type names start with AWS. Custom inventory type names will start with Custom. Default inventory item types include the following: AWS:AWSComponent, AWS:Application, AWS:InstanceInformation, AWS:Network, and AWS:WindowsUpdate.\n\nSchemaVersion (string) -- [REQUIRED]The schema version for the inventory item.\n\nCaptureTime (string) -- [REQUIRED]The time the inventory information was collected.\n\nContentHash (string) --MD5 hash of the inventory item type contents. The content hash is used to determine whether to update inventory information. The PutInventory API does not update the inventory item type contents if the MD5 hash has not changed since last update.\n\nContent (list) --The inventory data of the inventory type.\n\n(dict) --\n(string) --\n(string) --\n\n\n\n\n\n\nContext (dict) --A map of associated properties for a specified inventory type. For example, with this attribute, you can specify the ExecutionId , ExecutionType , ComplianceType properties of the AWS:ComplianceItem type.\n\n(string) --\n(string) --\n\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Message': 'string'
}


Response Structure

(dict) --

Message (string) --
Information about the request.







Exceptions

SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.InvalidInstanceId
SSM.Client.exceptions.InvalidTypeNameException
SSM.Client.exceptions.InvalidItemContentException
SSM.Client.exceptions.TotalSizeLimitExceededException
SSM.Client.exceptions.ItemSizeLimitExceededException
SSM.Client.exceptions.ItemContentMismatchException
SSM.Client.exceptions.CustomSchemaCountLimitExceededException
SSM.Client.exceptions.UnsupportedInventorySchemaVersionException
SSM.Client.exceptions.UnsupportedInventoryItemContextException
SSM.Client.exceptions.InvalidInventoryItemContextException
SSM.Client.exceptions.SubTypeCountLimitExceededException


    :return: {
        'Message': 'string'
    }
    
    
    :returns: 
    SSM.Client.exceptions.InternalServerError
    SSM.Client.exceptions.InvalidInstanceId
    SSM.Client.exceptions.InvalidTypeNameException
    SSM.Client.exceptions.InvalidItemContentException
    SSM.Client.exceptions.TotalSizeLimitExceededException
    SSM.Client.exceptions.ItemSizeLimitExceededException
    SSM.Client.exceptions.ItemContentMismatchException
    SSM.Client.exceptions.CustomSchemaCountLimitExceededException
    SSM.Client.exceptions.UnsupportedInventorySchemaVersionException
    SSM.Client.exceptions.UnsupportedInventoryItemContextException
    SSM.Client.exceptions.InvalidInventoryItemContextException
    SSM.Client.exceptions.SubTypeCountLimitExceededException
    
    """
    pass

def put_parameter(Name=None, Description=None, Value=None, Type=None, KeyId=None, Overwrite=None, AllowedPattern=None, Tags=None, Tier=None, Policies=None, DataType=None):
    """
    Add a parameter to the system.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_parameter(
        Name='string',
        Description='string',
        Value='string',
        Type='String'|'StringList'|'SecureString',
        KeyId='string',
        Overwrite=True|False,
        AllowedPattern='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        Tier='Standard'|'Advanced'|'Intelligent-Tiering',
        Policies='string',
        DataType='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe fully qualified name of the parameter that you want to add to the system. The fully qualified name includes the complete hierarchy of the parameter path and name. For parameters in a hierarchy, you must include a leading forward slash character (/) when you create or reference a parameter. For example: /Dev/DBServer/MySQL/db-string13\nNaming Constraints:\n\nParameter names are case sensitive.\nA parameter name must be unique within an AWS Region\nA parameter name can\'t be prefixed with 'aws' or 'ssm' (case-insensitive).\nParameter names can include only the following symbols and letters: a-zA-Z0-9_.-/\nA parameter name can\'t include spaces.\nParameter hierarchies are limited to a maximum depth of fifteen levels.\n\nFor additional information about valid values for parameter names, see About requirements and constraints for parameter names in the AWS Systems Manager User Guide .\n\nNote\nThe maximum length constraint listed below includes capacity for additional system attributes that are not part of the name. The maximum length for a parameter name, including the full length of the parameter ARN, is 1011 characters. For example, the length of the following parameter name is 65 characters, not 20 characters:\n\narn:aws:ssm:us-east-2:111122223333:parameter/ExampleParameterName\n\n

    :type Description: string
    :param Description: Information about the parameter that you want to add to the system. Optional but recommended.\n\nWarning\nDo not enter personally identifiable information in this field.\n\n

    :type Value: string
    :param Value: [REQUIRED]\nThe parameter value that you want to add to the system. Standard parameters have a value limit of 4 KB. Advanced parameters have a value limit of 8 KB.\n

    :type Type: string
    :param Type: The type of parameter that you want to add to the system.\nItems in a StringList must be separated by a comma (,). You can\'t use other punctuation or special character to escape items in the list. If you have a parameter value that requires a comma, then use the String data type.\n\nNote\nSecureString is not currently supported for AWS CloudFormation templates or in the China Regions.\n\n

    :type KeyId: string
    :param KeyId: The KMS Key ID that you want to use to encrypt a parameter. Either the default AWS Key Management Service (AWS KMS) key automatically assigned to your AWS account or a custom key. Required for parameters that use the SecureString data type.\nIf you don\'t specify a key ID, the system uses the default key associated with your AWS account.\n\nTo use your default AWS KMS key, choose the SecureString data type, and do not specify the Key ID when you create the parameter. The system automatically populates Key ID with your default KMS key.\nTo use a custom KMS key, choose the SecureString data type with the Key ID parameter.\n\n

    :type Overwrite: boolean
    :param Overwrite: Overwrite an existing parameter. If not specified, will default to 'false'.

    :type AllowedPattern: string
    :param AllowedPattern: A regular expression used to validate the parameter value. For example, for String types with values restricted to numbers, you can specify the following: AllowedPattern=^d+$

    :type Tags: list
    :param Tags: Optional metadata that you assign to a resource. Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For example, you might want to tag a Systems Manager parameter to identify the type of resource to which it applies, the environment, or the type of configuration data referenced by the parameter. In this case, you could specify the following key name/value pairs:\n\nKey=Resource,Value=S3bucket\nKey=OS,Value=Windows\nKey=ParameterType,Value=LicenseKey\n\n\nNote\nTo add tags to an existing Systems Manager parameter, use the AddTagsToResource action.\n\n\n(dict) --Metadata that you assign to your AWS resources. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment. In Systems Manager, you can apply tags to documents, managed instances, maintenance windows, Parameter Store parameters, and patch baselines.\n\nKey (string) -- [REQUIRED]The name of the tag.\n\nValue (string) -- [REQUIRED]The value of the tag.\n\n\n\n\n

    :type Tier: string
    :param Tier: The parameter tier to assign to a parameter.\nParameter Store offers a standard tier and an advanced tier for parameters. Standard parameters have a content size limit of 4 KB and can\'t be configured to use parameter policies. You can create a maximum of 10,000 standard parameters for each Region in an AWS account. Standard parameters are offered at no additional cost.\nAdvanced parameters have a content size limit of 8 KB and can be configured to use parameter policies. You can create a maximum of 100,000 advanced parameters for each Region in an AWS account. Advanced parameters incur a charge. For more information, see Standard and advanced parameter tiers in the AWS Systems Manager User Guide .\nYou can change a standard parameter to an advanced parameter any time. But you can\'t revert an advanced parameter to a standard parameter. Reverting an advanced parameter to a standard parameter would result in data loss because the system would truncate the size of the parameter from 8 KB to 4 KB. Reverting would also remove any policies attached to the parameter. Lastly, advanced parameters use a different form of encryption than standard parameters.\nIf you no longer need an advanced parameter, or if you no longer want to incur charges for an advanced parameter, you must delete it and recreate it as a new standard parameter.\n\nUsing the Default Tier Configuration\nIn PutParameter requests, you can specify the tier to create the parameter in. Whenever you specify a tier in the request, Parameter Store creates or updates the parameter according to that request. However, if you do not specify a tier in a request, Parameter Store assigns the tier based on the current Parameter Store default tier configuration.\nThe default tier when you begin using Parameter Store is the standard-parameter tier. If you use the advanced-parameter tier, you can specify one of the following as the default:\n\nAdvanced : With this option, Parameter Store evaluates all requests as advanced parameters.\nIntelligent-Tiering : With this option, Parameter Store evaluates each request to determine if the parameter is standard or advanced. If the request doesn\'t include any options that require an advanced parameter, the parameter is created in the standard-parameter tier. If one or more options requiring an advanced parameter are included in the request, Parameter Store create a parameter in the advanced-parameter tier. This approach helps control your parameter-related costs by always creating standard parameters unless an advanced parameter is necessary.\n\nOptions that require an advanced parameter include the following:\n\nThe content size of the parameter is more than 4 KB.\nThe parameter uses a parameter policy.\nMore than 10,000 parameters already exist in your AWS account in the current Region.\n\nFor more information about configuring the default tier option, see Specifying a default parameter tier in the AWS Systems Manager User Guide .\n

    :type Policies: string
    :param Policies: One or more policies to apply to a parameter. This action takes a JSON array. Parameter Store supports the following policy types:\nExpiration: This policy deletes the parameter after it expires. When you create the policy, you specify the expiration date. You can update the expiration date and time by updating the policy. Updating the parameter does not affect the expiration date and time. When the expiration time is reached, Parameter Store deletes the parameter.\nExpirationNotification: This policy triggers an event in Amazon CloudWatch Events that notifies you about the expiration. By using this policy, you can receive notification before or after the expiration time is reached, in units of days or hours.\nNoChangeNotification: This policy triggers a CloudWatch event if a parameter has not been modified for a specified period of time. This policy type is useful when, for example, a secret needs to be changed within a period of time, but it has not been changed.\nAll existing policies are preserved until you send new policies or an empty policy. For more information about parameter policies, see Assigning parameter policies .\n

    :type DataType: string
    :param DataType: The data type for a String parameter. Supported data types include plain text and Amazon Machine Image IDs.\n\nThe following data type values are supported.\n\ntext\naws:ec2:image\n\nWhen you create a String parameter and specify aws:ec2:image , Systems Manager validates the parameter value is in the required format, such as ami-12345abcdeEXAMPLE , and that the specified AMI is available in your AWS account. For more information, see Native parameter support for Amazon Machine Image IDs in the AWS Systems Manager User Guide .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Version': 123,
    'Tier': 'Standard'|'Advanced'|'Intelligent-Tiering'
}


Response Structure

(dict) --

Version (integer) --
The new version number of a parameter. If you edit a parameter value, Parameter Store automatically creates a new version and assigns this new version a unique ID. You can reference a parameter version ID in API actions or in Systems Manager documents (SSM documents). By default, if you don\'t specify a specific version, the system returns the latest parameter value when a parameter is called.

Tier (string) --
The tier assigned to the parameter.







Exceptions

SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.InvalidKeyId
SSM.Client.exceptions.ParameterLimitExceeded
SSM.Client.exceptions.TooManyUpdates
SSM.Client.exceptions.ParameterAlreadyExists
SSM.Client.exceptions.HierarchyLevelLimitExceededException
SSM.Client.exceptions.HierarchyTypeMismatchException
SSM.Client.exceptions.InvalidAllowedPatternException
SSM.Client.exceptions.ParameterMaxVersionLimitExceeded
SSM.Client.exceptions.ParameterPatternMismatchException
SSM.Client.exceptions.UnsupportedParameterType
SSM.Client.exceptions.PoliciesLimitExceededException
SSM.Client.exceptions.InvalidPolicyTypeException
SSM.Client.exceptions.InvalidPolicyAttributeException
SSM.Client.exceptions.IncompatiblePolicyException


    :return: {
        'Version': 123,
        'Tier': 'Standard'|'Advanced'|'Intelligent-Tiering'
    }
    
    
    :returns: 
    SSM.Client.exceptions.InternalServerError
    SSM.Client.exceptions.InvalidKeyId
    SSM.Client.exceptions.ParameterLimitExceeded
    SSM.Client.exceptions.TooManyUpdates
    SSM.Client.exceptions.ParameterAlreadyExists
    SSM.Client.exceptions.HierarchyLevelLimitExceededException
    SSM.Client.exceptions.HierarchyTypeMismatchException
    SSM.Client.exceptions.InvalidAllowedPatternException
    SSM.Client.exceptions.ParameterMaxVersionLimitExceeded
    SSM.Client.exceptions.ParameterPatternMismatchException
    SSM.Client.exceptions.UnsupportedParameterType
    SSM.Client.exceptions.PoliciesLimitExceededException
    SSM.Client.exceptions.InvalidPolicyTypeException
    SSM.Client.exceptions.InvalidPolicyAttributeException
    SSM.Client.exceptions.IncompatiblePolicyException
    
    """
    pass

def register_default_patch_baseline(BaselineId=None):
    """
    Defines the default patch baseline for the relevant operating system.
    To reset the AWS predefined patch baseline as the default, specify the full patch baseline ARN as the baseline ID value. For example, for CentOS, specify arn:aws:ssm:us-east-2:733109147000:patchbaseline/pb-0574b43a65ea646ed instead of pb-0574b43a65ea646ed .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.register_default_patch_baseline(
        BaselineId='string'
    )
    
    
    :type BaselineId: string
    :param BaselineId: [REQUIRED]\nThe ID of the patch baseline that should be the default patch baseline.\n

    :rtype: dict
ReturnsResponse Syntax{
    'BaselineId': 'string'
}


Response Structure

(dict) --
BaselineId (string) --The ID of the default patch baseline.






Exceptions

SSM.Client.exceptions.InvalidResourceId
SSM.Client.exceptions.DoesNotExistException
SSM.Client.exceptions.InternalServerError


    :return: {
        'BaselineId': 'string'
    }
    
    
    """
    pass

def register_patch_baseline_for_patch_group(BaselineId=None, PatchGroup=None):
    """
    Registers a patch baseline for a patch group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.register_patch_baseline_for_patch_group(
        BaselineId='string',
        PatchGroup='string'
    )
    
    
    :type BaselineId: string
    :param BaselineId: [REQUIRED]\nThe ID of the patch baseline to register the patch group with.\n

    :type PatchGroup: string
    :param PatchGroup: [REQUIRED]\nThe name of the patch group that should be registered with the patch baseline.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'BaselineId': 'string',
    'PatchGroup': 'string'
}


Response Structure

(dict) --

BaselineId (string) --
The ID of the patch baseline the patch group was registered with.

PatchGroup (string) --
The name of the patch group registered with the patch baseline.







Exceptions

SSM.Client.exceptions.AlreadyExistsException
SSM.Client.exceptions.DoesNotExistException
SSM.Client.exceptions.InvalidResourceId
SSM.Client.exceptions.ResourceLimitExceededException
SSM.Client.exceptions.InternalServerError


    :return: {
        'BaselineId': 'string',
        'PatchGroup': 'string'
    }
    
    
    :returns: 
    SSM.Client.exceptions.AlreadyExistsException
    SSM.Client.exceptions.DoesNotExistException
    SSM.Client.exceptions.InvalidResourceId
    SSM.Client.exceptions.ResourceLimitExceededException
    SSM.Client.exceptions.InternalServerError
    
    """
    pass

def register_target_with_maintenance_window(WindowId=None, ResourceType=None, Targets=None, OwnerInformation=None, Name=None, Description=None, ClientToken=None):
    """
    Registers a target with a maintenance window.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.register_target_with_maintenance_window(
        WindowId='string',
        ResourceType='INSTANCE'|'RESOURCE_GROUP',
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
    :param WindowId: [REQUIRED]\nThe ID of the maintenance window the target should be registered with.\n

    :type ResourceType: string
    :param ResourceType: [REQUIRED]\nThe type of target being registered with the maintenance window.\n

    :type Targets: list
    :param Targets: [REQUIRED]\nThe targets to register with the maintenance window. In other words, the instances to run commands on when the maintenance window runs.\nYou can specify targets using instance IDs, resource group names, or tags that have been applied to instances.\n\nExample 1 : Specify instance IDs``Key=InstanceIds,Values=*instance-id-1* ,*instance-id-2* ,*instance-id-3* ``\nExample 2 : Use tag key-pairs applied to instances\n``Key=tag:my-tag-key ,Values=*my-tag-value-1* ,*my-tag-value-2* ``\nExample 3 : Use tag-keys applied to instances\n``Key=tag-key,Values=*my-tag-key-1* ,*my-tag-key-2* ``\nExample 4 : Use resource group names\n``Key=resource-groups:Name,Values=*resource-group-name* ``\nExample 5 : Use filters for resource group types\n``Key=resource-groups:ResourceTypeFilters,Values=*resource-type-1* ,*resource-type-2* ``\n\n\nNote\nFor Key=resource-groups:ResourceTypeFilters , specify resource types in the following format\n\n``Key=resource-groups:ResourceTypeFilters,Values=*AWS::EC2::INSTANCE* ,*AWS::EC2::VPC* ``\n\nFor more information about these examples formats, including the best use case for each one, see Examples: Register targets with a maintenance window in the AWS Systems Manager User Guide .\n\n(dict) --An array of search criteria that targets instances using a Key,Value combination that you specify.\nSupported formats include the following.\n\n``Key=InstanceIds,Values=*instance-id-1* ,*instance-id-2* ,*instance-id-3* ``\n``Key=tag:my-tag-key ,Values=*my-tag-value-1* ,*my-tag-value-2* ``\n``Key=tag-key,Values=*my-tag-key-1* ,*my-tag-key-2* ``\n(Maintenance window targets only) ``Key=resource-groups:Name,Values=*resource-group-name* ``\n(Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*resource-type-1* ,*resource-type-2* ``\n\nFor example:\n\nKey=InstanceIds,Values=i-02573cafcfEXAMPLE,i-0471e04240EXAMPLE,i-07782c72faEXAMPLE\nKey=tag:CostCenter,Values=CostCenter1,CostCenter2,CostCenter3\nKey=tag-key,Values=Name,Instance-Type,CostCenter\n(Maintenance window targets only) Key=resource-groups:Name,Values=ProductionResourceGroup  This example demonstrates how to target all resources in the resource group ProductionResourceGroup in your maintenance window.\n(Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*AWS::EC2::INSTANCE* ,*AWS::EC2::VPC* ``  This example demonstrates how to target only EC2 instances and VPCs in your maintenance window.\n(State Manager association targets only) Key=InstanceIds,Values=*  This example demonstrates how to target all managed instances in the AWS Region where the association was created.\n\nFor information about how to send commands that target instances using Key,Value parameters, see Targeting multiple instances in the AWS Systems Manager User Guide .\n\nKey (string) --User-defined criteria for sending commands that target instances that meet the criteria.\n\nValues (list) --User-defined criteria that maps to Key . For example, if you specified tag:ServerRole , you could specify value:WebServer to run a command on instances that include EC2 tags of ServerRole,WebServer .\n\n(string) --\n\n\n\n\n\n

    :type OwnerInformation: string
    :param OwnerInformation: User-provided value that will be included in any CloudWatch events raised while running tasks for these targets in this maintenance window.

    :type Name: string
    :param Name: An optional name for the target.

    :type Description: string
    :param Description: An optional description for the target.

    :type ClientToken: string
    :param ClientToken: User-provided idempotency token.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'WindowTargetId': 'string'
}


Response Structure

(dict) --

WindowTargetId (string) --
The ID of the target definition in this maintenance window.







Exceptions

SSM.Client.exceptions.IdempotentParameterMismatch
SSM.Client.exceptions.DoesNotExistException
SSM.Client.exceptions.ResourceLimitExceededException
SSM.Client.exceptions.InternalServerError


    :return: {
        'WindowTargetId': 'string'
    }
    
    
    :returns: 
    SSM.Client.exceptions.IdempotentParameterMismatch
    SSM.Client.exceptions.DoesNotExistException
    SSM.Client.exceptions.ResourceLimitExceededException
    SSM.Client.exceptions.InternalServerError
    
    """
    pass

def register_task_with_maintenance_window(WindowId=None, Targets=None, TaskArn=None, ServiceRoleArn=None, TaskType=None, TaskParameters=None, TaskInvocationParameters=None, Priority=None, MaxConcurrency=None, MaxErrors=None, LoggingInfo=None, Name=None, Description=None, ClientToken=None):
    """
    Adds a new task to a maintenance window.
    See also: AWS API Documentation
    
    Exceptions
    
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
                'CloudWatchOutputConfig': {
                    'CloudWatchLogGroupName': 'string',
                    'CloudWatchOutputEnabled': True|False
                },
                'DocumentHash': 'string',
                'DocumentHashType': 'Sha256'|'Sha1',
                'DocumentVersion': 'string',
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
    :param WindowId: [REQUIRED]\nThe ID of the maintenance window the task should be added to.\n

    :type Targets: list
    :param Targets: [REQUIRED]\nThe targets (either instances or maintenance window targets).\nSpecify instances using the following format:\n\nKey=InstanceIds,Values=<instance-id-1>,<instance-id-2>\nSpecify maintenance window targets using the following format:\n\nKey=WindowTargetIds;,Values=<window-target-id-1>,<window-target-id-2>\n\n(dict) --An array of search criteria that targets instances using a Key,Value combination that you specify.\nSupported formats include the following.\n\n``Key=InstanceIds,Values=*instance-id-1* ,*instance-id-2* ,*instance-id-3* ``\n``Key=tag:my-tag-key ,Values=*my-tag-value-1* ,*my-tag-value-2* ``\n``Key=tag-key,Values=*my-tag-key-1* ,*my-tag-key-2* ``\n(Maintenance window targets only) ``Key=resource-groups:Name,Values=*resource-group-name* ``\n(Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*resource-type-1* ,*resource-type-2* ``\n\nFor example:\n\nKey=InstanceIds,Values=i-02573cafcfEXAMPLE,i-0471e04240EXAMPLE,i-07782c72faEXAMPLE\nKey=tag:CostCenter,Values=CostCenter1,CostCenter2,CostCenter3\nKey=tag-key,Values=Name,Instance-Type,CostCenter\n(Maintenance window targets only) Key=resource-groups:Name,Values=ProductionResourceGroup  This example demonstrates how to target all resources in the resource group ProductionResourceGroup in your maintenance window.\n(Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*AWS::EC2::INSTANCE* ,*AWS::EC2::VPC* ``  This example demonstrates how to target only EC2 instances and VPCs in your maintenance window.\n(State Manager association targets only) Key=InstanceIds,Values=*  This example demonstrates how to target all managed instances in the AWS Region where the association was created.\n\nFor information about how to send commands that target instances using Key,Value parameters, see Targeting multiple instances in the AWS Systems Manager User Guide .\n\nKey (string) --User-defined criteria for sending commands that target instances that meet the criteria.\n\nValues (list) --User-defined criteria that maps to Key . For example, if you specified tag:ServerRole , you could specify value:WebServer to run a command on instances that include EC2 tags of ServerRole,WebServer .\n\n(string) --\n\n\n\n\n\n

    :type TaskArn: string
    :param TaskArn: [REQUIRED]\nThe ARN of the task to run.\n

    :type ServiceRoleArn: string
    :param ServiceRoleArn: The ARN of the IAM service role for Systems Manager to assume when running a maintenance window task. If you do not specify a service role ARN, Systems Manager uses your account\'s service-linked role. If no service-linked role for Systems Manager exists in your account, it is created when you run RegisterTaskWithMaintenanceWindow .\nFor more information, see the following topics in the in the AWS Systems Manager User Guide :\n\nUsing service-linked roles for Systems Manager\nShould I use a service-linked role or a custom service role to run maintenance window tasks?\n\n

    :type TaskType: string
    :param TaskType: [REQUIRED]\nThe type of task being registered.\n

    :type TaskParameters: dict
    :param TaskParameters: The parameters that should be passed to the task when it is run.\n\nNote\nTaskParameters has been deprecated. To specify parameters to pass to a task when it runs, instead use the Parameters option in the TaskInvocationParameters structure. For information about how Systems Manager handles these options for the supported maintenance window task types, see MaintenanceWindowTaskInvocationParameters .\n\n\n(string) --\n(dict) --Defines the values for a task parameter.\n\nValues (list) --This field contains an array of 0 or more strings, each 1 to 255 characters in length.\n\n(string) --\n\n\n\n\n\n\n\n

    :type TaskInvocationParameters: dict
    :param TaskInvocationParameters: The parameters that the task should use during execution. Populate only the fields that match the task type. All other fields should be empty.\n\nRunCommand (dict) --The parameters for a RUN_COMMAND task type.\n\nComment (string) --Information about the commands to run.\n\nCloudWatchOutputConfig (dict) --Configuration options for sending command output to CloudWatch Logs.\n\nCloudWatchLogGroupName (string) --The name of the CloudWatch log group where you want to send command output. If you don\'t specify a group name, Systems Manager automatically creates a log group for you. The log group uses the following naming format: aws/ssm/SystemsManagerDocumentName .\n\nCloudWatchOutputEnabled (boolean) --Enables Systems Manager to send command output to CloudWatch Logs.\n\n\n\nDocumentHash (string) --The SHA-256 or SHA-1 hash created by the system when the document was created. SHA-1 hashes have been deprecated.\n\nDocumentHashType (string) --SHA-256 or SHA-1. SHA-1 hashes have been deprecated.\n\nDocumentVersion (string) --The SSM document version to use in the request. You can specify $DEFAULT, $LATEST, or a specific version number. If you run commands by using the AWS CLI, then you must escape the first two options by using a backslash. If you specify a version number, then you don\'t need to use the backslash. For example:\n--document-version '$DEFAULT'\n--document-version '$LATEST'\n--document-version '3'\n\nNotificationConfig (dict) --Configurations for sending notifications about command status changes on a per-instance basis.\n\nNotificationArn (string) --An Amazon Resource Name (ARN) for an Amazon Simple Notification Service (Amazon SNS) topic. Run Command pushes notifications about command status changes to this topic.\n\nNotificationEvents (list) --The different events for which you can receive notifications. These events include the following: All (events), InProgress, Success, TimedOut, Cancelled, Failed. To learn more about these events, see Monitoring Systems Manager status changes using Amazon SNS notifications in the AWS Systems Manager User Guide .\n\n(string) --\n\n\nNotificationType (string) --Command: Receive notification when the status of a command changes. Invocation: For commands sent to multiple instances, receive notification on a per-instance basis when the status of a command changes.\n\n\n\nOutputS3BucketName (string) --The name of the S3 bucket.\n\nOutputS3KeyPrefix (string) --The S3 bucket subfolder.\n\nParameters (dict) --The parameters for the RUN_COMMAND task execution.\n\n(string) --\n(list) --\n(string) --\n\n\n\n\n\n\nServiceRoleArn (string) --The ARN of the IAM service role to use to publish Amazon Simple Notification Service (Amazon SNS) notifications for maintenance window Run Command tasks.\n\nTimeoutSeconds (integer) --If this time is reached and the command has not already started running, it doesn\'t run.\n\n\n\nAutomation (dict) --The parameters for an AUTOMATION task type.\n\nDocumentVersion (string) --The version of an Automation document to use during task execution.\n\nParameters (dict) --The parameters for the AUTOMATION task.\nFor information about specifying and updating task parameters, see RegisterTaskWithMaintenanceWindow and UpdateMaintenanceWindowTask .\n\nNote\n\nLoggingInfo has been deprecated. To specify an S3 bucket to contain logs, instead use the OutputS3BucketName and OutputS3KeyPrefix options in the TaskInvocationParameters structure. For information about how Systems Manager handles these options for the supported maintenance window task types, see MaintenanceWindowTaskInvocationParameters .TaskParameters has been deprecated. To specify parameters to pass to a task when it runs, instead use the Parameters option in the TaskInvocationParameters structure. For information about how Systems Manager handles these options for the supported maintenance window task types, see MaintenanceWindowTaskInvocationParameters .\n\nFor AUTOMATION task types, Systems Manager ignores any values specified for these parameters.\n\n\n(string) --\n(list) --\n(string) --\n\n\n\n\n\n\n\n\nStepFunctions (dict) --The parameters for a STEP_FUNCTIONS task type.\n\nInput (string) --The inputs for the STEP_FUNCTIONS task.\n\nName (string) --The name of the STEP_FUNCTIONS task.\n\n\n\nLambda (dict) --The parameters for a LAMBDA task type.\n\nClientContext (string) --Pass client-specific information to the Lambda function that you are invoking. You can then process the client information in your Lambda function as you choose through the context variable.\n\nQualifier (string) --(Optional) Specify a Lambda function version or alias name. If you specify a function version, the action uses the qualified function ARN to invoke a specific Lambda function. If you specify an alias name, the action uses the alias ARN to invoke the Lambda function version to which the alias points.\n\nPayload (bytes) --JSON to provide to your Lambda function as input.\n\n\n\n\n

    :type Priority: integer
    :param Priority: The priority of the task in the maintenance window, the lower the number the higher the priority. Tasks in a maintenance window are scheduled in priority order with tasks that have the same priority scheduled in parallel.

    :type MaxConcurrency: string
    :param MaxConcurrency: [REQUIRED]\nThe maximum number of targets this task can be run for in parallel.\n

    :type MaxErrors: string
    :param MaxErrors: [REQUIRED]\nThe maximum number of errors allowed before this task stops being scheduled.\n

    :type LoggingInfo: dict
    :param LoggingInfo: A structure containing information about an S3 bucket to write instance-level logs to.\n\nNote\nLoggingInfo has been deprecated. To specify an S3 bucket to contain logs, instead use the OutputS3BucketName and OutputS3KeyPrefix options in the TaskInvocationParameters structure. For information about how Systems Manager handles these options for the supported maintenance window task types, see MaintenanceWindowTaskInvocationParameters .\n\n\nS3BucketName (string) -- [REQUIRED]The name of an S3 bucket where execution logs are stored .\n\nS3KeyPrefix (string) --(Optional) The S3 bucket subfolder.\n\nS3Region (string) -- [REQUIRED]The Region where the S3 bucket is located.\n\n\n

    :type Name: string
    :param Name: An optional name for the task.

    :type Description: string
    :param Description: An optional description for the task.

    :type ClientToken: string
    :param ClientToken: User-provided idempotency token.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'WindowTaskId': 'string'
}


Response Structure

(dict) --

WindowTaskId (string) --
The ID of the task in the maintenance window.







Exceptions

SSM.Client.exceptions.IdempotentParameterMismatch
SSM.Client.exceptions.DoesNotExistException
SSM.Client.exceptions.ResourceLimitExceededException
SSM.Client.exceptions.FeatureNotAvailableException
SSM.Client.exceptions.InternalServerError


    :return: {
        'WindowTaskId': 'string'
    }
    
    
    :returns: 
    SSM.Client.exceptions.IdempotentParameterMismatch
    SSM.Client.exceptions.DoesNotExistException
    SSM.Client.exceptions.ResourceLimitExceededException
    SSM.Client.exceptions.FeatureNotAvailableException
    SSM.Client.exceptions.InternalServerError
    
    """
    pass

def remove_tags_from_resource(ResourceType=None, ResourceId=None, TagKeys=None):
    """
    Removes tag keys from the specified resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.remove_tags_from_resource(
        ResourceType='Document'|'ManagedInstance'|'MaintenanceWindow'|'Parameter'|'PatchBaseline'|'OpsItem',
        ResourceId='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceType: string
    :param ResourceType: [REQUIRED]\nThe type of resource from which you want to remove a tag.\n\nNote\nThe ManagedInstance type for this API action is only for on-premises managed instances. Specify the name of the managed instance in the following format: mi-ID_number. For example, mi-1a2b3c4d5e6f.\n\n

    :type ResourceId: string
    :param ResourceId: [REQUIRED]\nThe ID of the resource from which you want to remove tags. For example:\nManagedInstance: mi-012345abcde\nMaintenanceWindow: mw-012345abcde\nPatchBaseline: pb-012345abcde\nFor the Document and Parameter values, use the name of the resource.\n\nNote\nThe ManagedInstance type for this API action is only for on-premises managed instances. Specify the name of the managed instance in the following format: mi-ID_number. For example, mi-1a2b3c4d5e6f.\n\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nTag keys that you want to remove from the specified resource.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

SSM.Client.exceptions.InvalidResourceType
SSM.Client.exceptions.InvalidResourceId
SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.TooManyUpdates


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def reset_service_setting(SettingId=None):
    """
    Services map a SettingId object to a setting value. AWS services teams define the default value for a SettingId . You can\'t create a new SettingId , but you can overwrite the default value if you have the ssm:UpdateServiceSetting permission for the setting. Use the  GetServiceSetting API action to view the current value. Use the  UpdateServiceSetting API action to change the default setting.
    Reset the service setting for the account to the default value as provisioned by the AWS service team.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.reset_service_setting(
        SettingId='string'
    )
    
    
    :type SettingId: string
    :param SettingId: [REQUIRED]\nThe Amazon Resource Name (ARN) of the service setting to reset. The setting ID can be /ssm/parameter-store/default-parameter-tier , /ssm/parameter-store/high-throughput-enabled , or /ssm/managed-instance/activation-tier . For example, arn:aws:ssm:us-east-1:111122223333:servicesetting/ssm/parameter-store/high-throughput-enabled .\n

    :rtype: dict
ReturnsResponse Syntax{
    'ServiceSetting': {
        'SettingId': 'string',
        'SettingValue': 'string',
        'LastModifiedDate': datetime(2015, 1, 1),
        'LastModifiedUser': 'string',
        'ARN': 'string',
        'Status': 'string'
    }
}


Response Structure

(dict) --The result body of the ResetServiceSetting API action.

ServiceSetting (dict) --The current, effective service setting after calling the ResetServiceSetting API action.

SettingId (string) --The ID of the service setting.

SettingValue (string) --The value of the service setting.

LastModifiedDate (datetime) --The last time the service setting was modified.

LastModifiedUser (string) --The ARN of the last modified user. This field is populated only if the setting value was overwritten.

ARN (string) --The ARN of the service setting.

Status (string) --The status of the service setting. The value can be Default, Customized or PendingUpdate.

Default: The current setting uses a default value provisioned by the AWS service team.
Customized: The current setting use a custom value specified by the customer.
PendingUpdate: The current setting uses a default or custom value, but a setting change request is pending approval.









Exceptions

SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.ServiceSettingNotFound
SSM.Client.exceptions.TooManyUpdates


    :return: {
        'ServiceSetting': {
            'SettingId': 'string',
            'SettingValue': 'string',
            'LastModifiedDate': datetime(2015, 1, 1),
            'LastModifiedUser': 'string',
            'ARN': 'string',
            'Status': 'string'
        }
    }
    
    
    :returns: 
    SSM.Client.exceptions.InternalServerError
    SSM.Client.exceptions.ServiceSettingNotFound
    SSM.Client.exceptions.TooManyUpdates
    
    """
    pass

def resume_session(SessionId=None):
    """
    Reconnects a session to an instance after it has been disconnected. Connections can be resumed for disconnected sessions, but not terminated sessions.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.resume_session(
        SessionId='string'
    )
    
    
    :type SessionId: string
    :param SessionId: [REQUIRED]\nThe ID of the disconnected session to resume.\n

    :rtype: dict
ReturnsResponse Syntax{
    'SessionId': 'string',
    'TokenValue': 'string',
    'StreamUrl': 'string'
}


Response Structure

(dict) --
SessionId (string) --The ID of the session.

TokenValue (string) --An encrypted token value containing session and caller information. Used to authenticate the connection to the instance.

StreamUrl (string) --A URL back to SSM Agent on the instance that the Session Manager client uses to send commands and receive output from the instance. Format: wss://ssmmessages.**region** .amazonaws.com/v1/data-channel/**session-id** ?stream=(input|output) .

region represents the Region identifier for an AWS Region supported by AWS Systems Manager, such as us-east-2 for the US East (Ohio) Region. For a list of supported region values, see the Region column in Systems Manager service endpoints in the AWS General Reference .session-id represents the ID of a Session Manager session, such as 1a2b3c4dEXAMPLE .







Exceptions

SSM.Client.exceptions.DoesNotExistException
SSM.Client.exceptions.InternalServerError


    :return: {
        'SessionId': 'string',
        'TokenValue': 'string',
        'StreamUrl': 'string'
    }
    
    
    """
    pass

def send_automation_signal(AutomationExecutionId=None, SignalType=None, Payload=None):
    """
    Sends a signal to an Automation execution to change the current behavior or status of the execution.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param AutomationExecutionId: [REQUIRED]\nThe unique identifier for an existing Automation execution that you want to send the signal to.\n

    :type SignalType: string
    :param SignalType: [REQUIRED]\nThe type of signal to send to an Automation execution.\n

    :type Payload: dict
    :param Payload: The data sent with the signal. The data schema depends on the type of signal used in the request.\nFor Approve and Reject signal types, the payload is an optional comment that you can send with the signal type. For example:\n\nComment='Looks good'\nFor StartStep and Resume signal types, you must send the name of the Automation step to start or resume as the payload. For example:\n\nStepName='step1'\nFor the StopStep signal type, you must send the step execution ID as the payload. For example:\n\nStepExecutionId='97fff367-fc5a-4299-aed8-0123456789ab'\n\n(string) --\n(list) --\n(string) --\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

SSM.Client.exceptions.AutomationExecutionNotFoundException
SSM.Client.exceptions.AutomationStepNotFoundException
SSM.Client.exceptions.InvalidAutomationSignalException
SSM.Client.exceptions.InternalServerError


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def send_command(InstanceIds=None, Targets=None, DocumentName=None, DocumentVersion=None, DocumentHash=None, DocumentHashType=None, TimeoutSeconds=None, Comment=None, Parameters=None, OutputS3Region=None, OutputS3BucketName=None, OutputS3KeyPrefix=None, MaxConcurrency=None, MaxErrors=None, ServiceRoleArn=None, NotificationConfig=None, CloudWatchOutputConfig=None):
    """
    Runs commands on one or more managed instances.
    See also: AWS API Documentation
    
    Exceptions
    
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
        DocumentVersion='string',
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
        },
        CloudWatchOutputConfig={
            'CloudWatchLogGroupName': 'string',
            'CloudWatchOutputEnabled': True|False
        }
    )
    
    
    :type InstanceIds: list
    :param InstanceIds: The instance IDs where the command should run. You can specify a maximum of 50 IDs. If you prefer not to list individual instance IDs, you can instead send commands to a fleet of instances using the Targets parameter, which accepts EC2 tags. For more information about how to use targets, see Using targets and rate controls to send commands to a fleet in the AWS Systems Manager User Guide .\n\n(string) --\n\n

    :type Targets: list
    :param Targets: (Optional) An array of search criteria that targets instances using a Key,Value combination that you specify. Targets is required if you don\'t provide one or more instance IDs in the call. For more information about how to use targets, see Sending commands to a fleet in the AWS Systems Manager User Guide .\n\n(dict) --An array of search criteria that targets instances using a Key,Value combination that you specify.\nSupported formats include the following.\n\n``Key=InstanceIds,Values=*instance-id-1* ,*instance-id-2* ,*instance-id-3* ``\n``Key=tag:my-tag-key ,Values=*my-tag-value-1* ,*my-tag-value-2* ``\n``Key=tag-key,Values=*my-tag-key-1* ,*my-tag-key-2* ``\n(Maintenance window targets only) ``Key=resource-groups:Name,Values=*resource-group-name* ``\n(Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*resource-type-1* ,*resource-type-2* ``\n\nFor example:\n\nKey=InstanceIds,Values=i-02573cafcfEXAMPLE,i-0471e04240EXAMPLE,i-07782c72faEXAMPLE\nKey=tag:CostCenter,Values=CostCenter1,CostCenter2,CostCenter3\nKey=tag-key,Values=Name,Instance-Type,CostCenter\n(Maintenance window targets only) Key=resource-groups:Name,Values=ProductionResourceGroup  This example demonstrates how to target all resources in the resource group ProductionResourceGroup in your maintenance window.\n(Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*AWS::EC2::INSTANCE* ,*AWS::EC2::VPC* ``  This example demonstrates how to target only EC2 instances and VPCs in your maintenance window.\n(State Manager association targets only) Key=InstanceIds,Values=*  This example demonstrates how to target all managed instances in the AWS Region where the association was created.\n\nFor information about how to send commands that target instances using Key,Value parameters, see Targeting multiple instances in the AWS Systems Manager User Guide .\n\nKey (string) --User-defined criteria for sending commands that target instances that meet the criteria.\n\nValues (list) --User-defined criteria that maps to Key . For example, if you specified tag:ServerRole , you could specify value:WebServer to run a command on instances that include EC2 tags of ServerRole,WebServer .\n\n(string) --\n\n\n\n\n\n

    :type DocumentName: string
    :param DocumentName: [REQUIRED]\nRequired. The name of the Systems Manager document to run. This can be a public document or a custom document.\n

    :type DocumentVersion: string
    :param DocumentVersion: The SSM document version to use in the request. You can specify $DEFAULT, $LATEST, or a specific version number. If you run commands by using the AWS CLI, then you must escape the first two options by using a backslash. If you specify a version number, then you don\'t need to use the backslash. For example:\n--document-version '$DEFAULT'\n--document-version '$LATEST'\n--document-version '3'\n

    :type DocumentHash: string
    :param DocumentHash: The Sha256 or Sha1 hash created by the system when the document was created.\n\nNote\nSha1 hashes have been deprecated.\n\n

    :type DocumentHashType: string
    :param DocumentHashType: Sha256 or Sha1.\n\nNote\nSha1 hashes have been deprecated.\n\n

    :type TimeoutSeconds: integer
    :param TimeoutSeconds: If this time is reached and the command has not already started running, it will not run.

    :type Comment: string
    :param Comment: User-specified information about the command, such as a brief description of what the command should do.

    :type Parameters: dict
    :param Parameters: The required and optional parameters specified in the document being run.\n\n(string) --\n(list) --\n(string) --\n\n\n\n\n\n

    :type OutputS3Region: string
    :param OutputS3Region: (Deprecated) You can no longer specify this parameter. The system ignores it. Instead, Systems Manager automatically determines the Region of the S3 bucket.

    :type OutputS3BucketName: string
    :param OutputS3BucketName: The name of the S3 bucket where command execution responses should be stored.

    :type OutputS3KeyPrefix: string
    :param OutputS3KeyPrefix: The directory structure within the S3 bucket where the responses should be stored.

    :type MaxConcurrency: string
    :param MaxConcurrency: (Optional) The maximum number of instances that are allowed to run the command at the same time. You can specify a number such as 10 or a percentage such as 10%. The default value is 50. For more information about how to use MaxConcurrency, see Using concurrency controls in the AWS Systems Manager User Guide .

    :type MaxErrors: string
    :param MaxErrors: The maximum number of errors allowed without the command failing. When the command fails one more time beyond the value of MaxErrors, the systems stops sending the command to additional targets. You can specify a number like 10 or a percentage like 10%. The default value is 0. For more information about how to use MaxErrors, see Using error controls in the AWS Systems Manager User Guide .

    :type ServiceRoleArn: string
    :param ServiceRoleArn: The ARN of the IAM service role to use to publish Amazon Simple Notification Service (Amazon SNS) notifications for Run Command commands.

    :type NotificationConfig: dict
    :param NotificationConfig: Configurations for sending notifications.\n\nNotificationArn (string) --An Amazon Resource Name (ARN) for an Amazon Simple Notification Service (Amazon SNS) topic. Run Command pushes notifications about command status changes to this topic.\n\nNotificationEvents (list) --The different events for which you can receive notifications. These events include the following: All (events), InProgress, Success, TimedOut, Cancelled, Failed. To learn more about these events, see Monitoring Systems Manager status changes using Amazon SNS notifications in the AWS Systems Manager User Guide .\n\n(string) --\n\n\nNotificationType (string) --Command: Receive notification when the status of a command changes. Invocation: For commands sent to multiple instances, receive notification on a per-instance basis when the status of a command changes.\n\n\n

    :type CloudWatchOutputConfig: dict
    :param CloudWatchOutputConfig: Enables Systems Manager to send Run Command output to Amazon CloudWatch Logs.\n\nCloudWatchLogGroupName (string) --The name of the CloudWatch log group where you want to send command output. If you don\'t specify a group name, Systems Manager automatically creates a log group for you. The log group uses the following naming format: aws/ssm/SystemsManagerDocumentName .\n\nCloudWatchOutputEnabled (boolean) --Enables Systems Manager to send command output to CloudWatch Logs.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Command': {
        'CommandId': 'string',
        'DocumentName': 'string',
        'DocumentVersion': 'string',
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
        'DeliveryTimedOutCount': 123,
        'ServiceRole': 'string',
        'NotificationConfig': {
            'NotificationArn': 'string',
            'NotificationEvents': [
                'All'|'InProgress'|'Success'|'TimedOut'|'Cancelled'|'Failed',
            ],
            'NotificationType': 'Command'|'Invocation'
        },
        'CloudWatchOutputConfig': {
            'CloudWatchLogGroupName': 'string',
            'CloudWatchOutputEnabled': True|False
        },
        'TimeoutSeconds': 123
    }
}


Response Structure

(dict) --

Command (dict) --
The request as it was received by Systems Manager. Also provides the command ID which can be used future references to this request.

CommandId (string) --
A unique identifier for this command.

DocumentName (string) --
The name of the document requested for execution.

DocumentVersion (string) --
The SSM document version.

Comment (string) --
User-specified information about the command, such as a brief description of what the command should do.

ExpiresAfter (datetime) --
If this time is reached and the command has not already started running, it will not run. Calculated based on the ExpiresAfter user input provided as part of the SendCommand API.

Parameters (dict) --
The parameter values to be inserted in the document when running the command.

(string) --
(list) --
(string) --






InstanceIds (list) --
The instance IDs against which this command was requested.

(string) --


Targets (list) --
An array of search criteria that targets instances using a Key,Value combination that you specify. Targets is required if you don\'t provide one or more instance IDs in the call.

(dict) --
An array of search criteria that targets instances using a Key,Value combination that you specify.
Supported formats include the following.

``Key=InstanceIds,Values=*instance-id-1* ,*instance-id-2* ,*instance-id-3* ``
``Key=tag:my-tag-key ,Values=*my-tag-value-1* ,*my-tag-value-2* ``
``Key=tag-key,Values=*my-tag-key-1* ,*my-tag-key-2* ``
(Maintenance window targets only) ``Key=resource-groups:Name,Values=*resource-group-name* ``
(Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*resource-type-1* ,*resource-type-2* ``

For example:

Key=InstanceIds,Values=i-02573cafcfEXAMPLE,i-0471e04240EXAMPLE,i-07782c72faEXAMPLE
Key=tag:CostCenter,Values=CostCenter1,CostCenter2,CostCenter3
Key=tag-key,Values=Name,Instance-Type,CostCenter
(Maintenance window targets only) Key=resource-groups:Name,Values=ProductionResourceGroup   This example demonstrates how to target all resources in the resource group ProductionResourceGroup in your maintenance window.
(Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*AWS::EC2::INSTANCE* ,*AWS::EC2::VPC* ``   This example demonstrates how to target only EC2 instances and VPCs in your maintenance window.
(State Manager association targets only) Key=InstanceIds,Values=*   This example demonstrates how to target all managed instances in the AWS Region where the association was created.

For information about how to send commands that target instances using Key,Value parameters, see Targeting multiple instances in the AWS Systems Manager User Guide .

Key (string) --
User-defined criteria for sending commands that target instances that meet the criteria.

Values (list) --
User-defined criteria that maps to Key . For example, if you specified tag:ServerRole , you could specify value:WebServer to run a command on instances that include EC2 tags of ServerRole,WebServer .

(string) --






RequestedDateTime (datetime) --
The date and time the command was requested.

Status (string) --
The status of the command.

StatusDetails (string) --
A detailed status of the command execution. StatusDetails includes more information than Status because it includes states resulting from error and concurrency control parameters. StatusDetails can show different results than Status. For more information about these statuses, see Understanding command statuses in the AWS Systems Manager User Guide . StatusDetails can be one of the following values:

Pending: The command has not been sent to any instances.
In Progress: The command has been sent to at least one instance but has not reached a final state on all instances.
Success: The command successfully ran on all invocations. This is a terminal state.
Delivery Timed Out: The value of MaxErrors or more command invocations shows a status of Delivery Timed Out. This is a terminal state.
Execution Timed Out: The value of MaxErrors or more command invocations shows a status of Execution Timed Out. This is a terminal state.
Failed: The value of MaxErrors or more command invocations shows a status of Failed. This is a terminal state.
Incomplete: The command was attempted on all instances and one or more invocations does not have a value of Success but not enough invocations failed for the status to be Failed. This is a terminal state.
Canceled: The command was terminated before it was completed. This is a terminal state.
Rate Exceeded: The number of instances targeted by the command exceeded the account limit for pending invocations. The system has canceled the command before running it on any instance. This is a terminal state.


OutputS3Region (string) --
(Deprecated) You can no longer specify this parameter. The system ignores it. Instead, Systems Manager automatically determines the Region of the S3 bucket.

OutputS3BucketName (string) --
The S3 bucket where the responses to the command executions should be stored. This was requested when issuing the command.

OutputS3KeyPrefix (string) --
The S3 directory path inside the bucket where the responses to the command executions should be stored. This was requested when issuing the command.

MaxConcurrency (string) --
The maximum number of instances that are allowed to run the command at the same time. You can specify a number of instances, such as 10, or a percentage of instances, such as 10%. The default value is 50. For more information about how to use MaxConcurrency, see Running commands using Systems Manager Run Command in the AWS Systems Manager User Guide .

MaxErrors (string) --
The maximum number of errors allowed before the system stops sending the command to additional targets. You can specify a number of errors, such as 10, or a percentage or errors, such as 10%. The default value is 0. For more information about how to use MaxErrors, see Running commands using Systems Manager Run Command in the AWS Systems Manager User Guide .

TargetCount (integer) --
The number of targets for the command.

CompletedCount (integer) --
The number of targets for which the command invocation reached a terminal state. Terminal states include the following: Success, Failed, Execution Timed Out, Delivery Timed Out, Canceled, Terminated, or Undeliverable.

ErrorCount (integer) --
The number of targets for which the status is Failed or Execution Timed Out.

DeliveryTimedOutCount (integer) --
The number of targets for which the status is Delivery Timed Out.

ServiceRole (string) --
The IAM service role that Run Command uses to act on your behalf when sending notifications about command status changes.

NotificationConfig (dict) --
Configurations for sending notifications about command status changes.

NotificationArn (string) --
An Amazon Resource Name (ARN) for an Amazon Simple Notification Service (Amazon SNS) topic. Run Command pushes notifications about command status changes to this topic.

NotificationEvents (list) --
The different events for which you can receive notifications. These events include the following: All (events), InProgress, Success, TimedOut, Cancelled, Failed. To learn more about these events, see Monitoring Systems Manager status changes using Amazon SNS notifications in the AWS Systems Manager User Guide .

(string) --


NotificationType (string) --
Command: Receive notification when the status of a command changes. Invocation: For commands sent to multiple instances, receive notification on a per-instance basis when the status of a command changes.



CloudWatchOutputConfig (dict) --
CloudWatch Logs information where you want Systems Manager to send the command output.

CloudWatchLogGroupName (string) --
The name of the CloudWatch log group where you want to send command output. If you don\'t specify a group name, Systems Manager automatically creates a log group for you. The log group uses the following naming format: aws/ssm/SystemsManagerDocumentName .

CloudWatchOutputEnabled (boolean) --
Enables Systems Manager to send command output to CloudWatch Logs.



TimeoutSeconds (integer) --
The TimeoutSeconds value specified for a command.









Exceptions

SSM.Client.exceptions.DuplicateInstanceId
SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.InvalidInstanceId
SSM.Client.exceptions.InvalidDocument
SSM.Client.exceptions.InvalidDocumentVersion
SSM.Client.exceptions.InvalidOutputFolder
SSM.Client.exceptions.InvalidParameters
SSM.Client.exceptions.UnsupportedPlatformType
SSM.Client.exceptions.MaxDocumentSizeExceeded
SSM.Client.exceptions.InvalidRole
SSM.Client.exceptions.InvalidNotificationConfig


    :return: {
        'Command': {
            'CommandId': 'string',
            'DocumentName': 'string',
            'DocumentVersion': 'string',
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
            'DeliveryTimedOutCount': 123,
            'ServiceRole': 'string',
            'NotificationConfig': {
                'NotificationArn': 'string',
                'NotificationEvents': [
                    'All'|'InProgress'|'Success'|'TimedOut'|'Cancelled'|'Failed',
                ],
                'NotificationType': 'Command'|'Invocation'
            },
            'CloudWatchOutputConfig': {
                'CloudWatchLogGroupName': 'string',
                'CloudWatchOutputEnabled': True|False
            },
            'TimeoutSeconds': 123
        }
    }
    
    
    :returns: 
    (string) --
    (list) --
    (string) --
    
    
    
    
    
    """
    pass

def start_associations_once(AssociationIds=None):
    """
    Use this API action to run an association immediately and only one time. This action can be helpful when troubleshooting associations.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_associations_once(
        AssociationIds=[
            'string',
        ]
    )
    
    
    :type AssociationIds: list
    :param AssociationIds: [REQUIRED]\nThe association IDs that you want to run immediately and only one time.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

SSM.Client.exceptions.InvalidAssociation
SSM.Client.exceptions.AssociationDoesNotExist


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def start_automation_execution(DocumentName=None, DocumentVersion=None, Parameters=None, ClientToken=None, Mode=None, TargetParameterName=None, Targets=None, TargetMaps=None, MaxConcurrency=None, MaxErrors=None, TargetLocations=None, Tags=None):
    """
    Initiates execution of an Automation document.
    See also: AWS API Documentation
    
    Exceptions
    
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
        TargetMaps=[
            {
                'string': [
                    'string',
                ]
            },
        ],
        MaxConcurrency='string',
        MaxErrors='string',
        TargetLocations=[
            {
                'Accounts': [
                    'string',
                ],
                'Regions': [
                    'string',
                ],
                'TargetLocationMaxConcurrency': 'string',
                'TargetLocationMaxErrors': 'string',
                'ExecutionRoleName': 'string'
            },
        ],
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type DocumentName: string
    :param DocumentName: [REQUIRED]\nThe name of the Automation document to use for this execution.\n

    :type DocumentVersion: string
    :param DocumentVersion: The version of the Automation document to use for this execution.

    :type Parameters: dict
    :param Parameters: A key-value map of execution parameters, which match the declared parameters in the Automation document.\n\n(string) --\n(list) --\n(string) --\n\n\n\n\n\n

    :type ClientToken: string
    :param ClientToken: User-provided idempotency token. The token must be unique, is case insensitive, enforces the UUID format, and can\'t be reused.

    :type Mode: string
    :param Mode: The execution mode of the automation. Valid modes include the following: Auto and Interactive. The default mode is Auto.

    :type TargetParameterName: string
    :param TargetParameterName: The name of the parameter used as the target resource for the rate-controlled execution. Required if you specify targets.

    :type Targets: list
    :param Targets: A key-value mapping to target resources. Required if you specify TargetParameterName.\n\n(dict) --An array of search criteria that targets instances using a Key,Value combination that you specify.\nSupported formats include the following.\n\n``Key=InstanceIds,Values=*instance-id-1* ,*instance-id-2* ,*instance-id-3* ``\n``Key=tag:my-tag-key ,Values=*my-tag-value-1* ,*my-tag-value-2* ``\n``Key=tag-key,Values=*my-tag-key-1* ,*my-tag-key-2* ``\n(Maintenance window targets only) ``Key=resource-groups:Name,Values=*resource-group-name* ``\n(Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*resource-type-1* ,*resource-type-2* ``\n\nFor example:\n\nKey=InstanceIds,Values=i-02573cafcfEXAMPLE,i-0471e04240EXAMPLE,i-07782c72faEXAMPLE\nKey=tag:CostCenter,Values=CostCenter1,CostCenter2,CostCenter3\nKey=tag-key,Values=Name,Instance-Type,CostCenter\n(Maintenance window targets only) Key=resource-groups:Name,Values=ProductionResourceGroup  This example demonstrates how to target all resources in the resource group ProductionResourceGroup in your maintenance window.\n(Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*AWS::EC2::INSTANCE* ,*AWS::EC2::VPC* ``  This example demonstrates how to target only EC2 instances and VPCs in your maintenance window.\n(State Manager association targets only) Key=InstanceIds,Values=*  This example demonstrates how to target all managed instances in the AWS Region where the association was created.\n\nFor information about how to send commands that target instances using Key,Value parameters, see Targeting multiple instances in the AWS Systems Manager User Guide .\n\nKey (string) --User-defined criteria for sending commands that target instances that meet the criteria.\n\nValues (list) --User-defined criteria that maps to Key . For example, if you specified tag:ServerRole , you could specify value:WebServer to run a command on instances that include EC2 tags of ServerRole,WebServer .\n\n(string) --\n\n\n\n\n\n

    :type TargetMaps: list
    :param TargetMaps: A key-value mapping of document parameters to target resources. Both Targets and TargetMaps cannot be specified together.\n\n(dict) --\n(string) --\n(list) --\n(string) --\n\n\n\n\n\n\n\n

    :type MaxConcurrency: string
    :param MaxConcurrency: The maximum number of targets allowed to run this task in parallel. You can specify a number, such as 10, or a percentage, such as 10%. The default value is 10.

    :type MaxErrors: string
    :param MaxErrors: The number of errors that are allowed before the system stops running the automation on additional targets. You can specify either an absolute number of errors, for example 10, or a percentage of the target set, for example 10%. If you specify 3, for example, the system stops running the automation when the fourth error is received. If you specify 0, then the system stops running the automation on additional targets after the first error result is returned. If you run an automation on 50 resources and set max-errors to 10%, then the system stops running the automation on additional targets when the sixth error is received.\nExecutions that are already running an automation when max-errors is reached are allowed to complete, but some of these executions may fail as well. If you need to ensure that there won\'t be more than max-errors failed executions, set max-concurrency to 1 so the executions proceed one at a time.\n

    :type TargetLocations: list
    :param TargetLocations: A location is a combination of AWS Regions and/or AWS accounts where you want to run the Automation. Use this action to start an Automation in multiple Regions and multiple accounts. For more information, see Running Automation workflows in multiple AWS Regions and accounts in the AWS Systems Manager User Guide .\n\n(dict) --The combination of AWS Regions and accounts targeted by the current Automation execution.\n\nAccounts (list) --The AWS accounts targeted by the current Automation execution.\n\n(string) --\n\n\nRegions (list) --The AWS Regions targeted by the current Automation execution.\n\n(string) --\n\n\nTargetLocationMaxConcurrency (string) --The maximum number of AWS accounts and AWS regions allowed to run the Automation concurrently\n\nTargetLocationMaxErrors (string) --The maximum number of errors allowed before the system stops queueing additional Automation executions for the currently running Automation.\n\nExecutionRoleName (string) --The Automation execution role used by the currently running Automation.\n\n\n\n\n

    :type Tags: list
    :param Tags: Optional metadata that you assign to a resource. You can specify a maximum of five tags for an automation. Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For example, you might want to tag an automation to identify an environment or operating system. In this case, you could specify the following key name/value pairs:\n\nKey=environment,Value=test\nKey=OS,Value=Windows\n\n\nNote\nTo add tags to an existing patch baseline, use the AddTagsToResource action.\n\n\n(dict) --Metadata that you assign to your AWS resources. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment. In Systems Manager, you can apply tags to documents, managed instances, maintenance windows, Parameter Store parameters, and patch baselines.\n\nKey (string) -- [REQUIRED]The name of the tag.\n\nValue (string) -- [REQUIRED]The value of the tag.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'AutomationExecutionId': 'string'
}


Response Structure

(dict) --

AutomationExecutionId (string) --
The unique ID of a newly scheduled automation execution.







Exceptions

SSM.Client.exceptions.AutomationDefinitionNotFoundException
SSM.Client.exceptions.InvalidAutomationExecutionParametersException
SSM.Client.exceptions.AutomationExecutionLimitExceededException
SSM.Client.exceptions.AutomationDefinitionVersionNotFoundException
SSM.Client.exceptions.IdempotentParameterMismatch
SSM.Client.exceptions.InvalidTarget
SSM.Client.exceptions.InternalServerError


    :return: {
        'AutomationExecutionId': 'string'
    }
    
    
    :returns: 
    SSM.Client.exceptions.AutomationDefinitionNotFoundException
    SSM.Client.exceptions.InvalidAutomationExecutionParametersException
    SSM.Client.exceptions.AutomationExecutionLimitExceededException
    SSM.Client.exceptions.AutomationDefinitionVersionNotFoundException
    SSM.Client.exceptions.IdempotentParameterMismatch
    SSM.Client.exceptions.InvalidTarget
    SSM.Client.exceptions.InternalServerError
    
    """
    pass

def start_session(Target=None, DocumentName=None, Parameters=None):
    """
    Initiates a connection to a target (for example, an instance) for a Session Manager session. Returns a URL and token that can be used to open a WebSocket connection for sending input and receiving outputs.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_session(
        Target='string',
        DocumentName='string',
        Parameters={
            'string': [
                'string',
            ]
        }
    )
    
    
    :type Target: string
    :param Target: [REQUIRED]\nThe instance to connect to for the session.\n

    :type DocumentName: string
    :param DocumentName: The name of the SSM document to define the parameters and plugin settings for the session. For example, SSM-SessionManagerRunShell . If no document name is provided, a shell to the instance is launched by default.

    :type Parameters: dict
    :param Parameters: Reserved for future use.\n\n(string) --\n(list) --\n(string) --\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'SessionId': 'string',
    'TokenValue': 'string',
    'StreamUrl': 'string'
}


Response Structure

(dict) --

SessionId (string) --
The ID of the session.

TokenValue (string) --
An encrypted token value containing session and caller information. Used to authenticate the connection to the instance.

StreamUrl (string) --
A URL back to SSM Agent on the instance that the Session Manager client uses to send commands and receive output from the instance. Format: wss://ssmmessages.**region** .amazonaws.com/v1/data-channel/**session-id** ?stream=(input|output)

region represents the Region identifier for an AWS Region supported by AWS Systems Manager, such as us-east-2 for the US East (Ohio) Region. For a list of supported region values, see the Region column in Systems Manager service endpoints in the AWS General Reference .
session-id represents the ID of a Session Manager session, such as 1a2b3c4dEXAMPLE .








Exceptions

SSM.Client.exceptions.InvalidDocument
SSM.Client.exceptions.TargetNotConnected
SSM.Client.exceptions.InternalServerError


    :return: {
        'SessionId': 'string',
        'TokenValue': 'string',
        'StreamUrl': 'string'
    }
    
    
    :returns: 
    SSM.Client.exceptions.InvalidDocument
    SSM.Client.exceptions.TargetNotConnected
    SSM.Client.exceptions.InternalServerError
    
    """
    pass

def stop_automation_execution(AutomationExecutionId=None, Type=None):
    """
    Stop an Automation that is currently running.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.stop_automation_execution(
        AutomationExecutionId='string',
        Type='Complete'|'Cancel'
    )
    
    
    :type AutomationExecutionId: string
    :param AutomationExecutionId: [REQUIRED]\nThe execution ID of the Automation to stop.\n

    :type Type: string
    :param Type: The stop request type. Valid types include the following: Cancel and Complete. The default type is Cancel.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

SSM.Client.exceptions.AutomationExecutionNotFoundException
SSM.Client.exceptions.InvalidAutomationStatusUpdateException
SSM.Client.exceptions.InternalServerError


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def terminate_session(SessionId=None):
    """
    Permanently ends a session and closes the data connection between the Session Manager client and SSM Agent on the instance. A terminated session cannot be resumed.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.terminate_session(
        SessionId='string'
    )
    
    
    :type SessionId: string
    :param SessionId: [REQUIRED]\nThe ID of the session to terminate.\n

    :rtype: dict
ReturnsResponse Syntax{
    'SessionId': 'string'
}


Response Structure

(dict) --
SessionId (string) --The ID of the session that has been terminated.






Exceptions

SSM.Client.exceptions.DoesNotExistException
SSM.Client.exceptions.InternalServerError


    :return: {
        'SessionId': 'string'
    }
    
    
    """
    pass

def update_association(AssociationId=None, Parameters=None, DocumentVersion=None, ScheduleExpression=None, OutputLocation=None, Name=None, Targets=None, AssociationName=None, AssociationVersion=None, AutomationTargetParameterName=None, MaxErrors=None, MaxConcurrency=None, ComplianceSeverity=None, SyncCompliance=None):
    """
    Updates an association. You can update the association name and version, the document version, schedule, parameters, and Amazon S3 output.
    In order to call this API action, your IAM user account, group, or role must be configured with permission to call the  DescribeAssociation API action. If you don\'t have permission to call DescribeAssociation, then you receive the following error: An error occurred (AccessDeniedException) when calling the UpdateAssociation operation: User: <user_arn> is not authorized to perform: ssm:DescribeAssociation on resource: <resource_arn>
    See also: AWS API Documentation
    
    Exceptions
    
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
        AssociationVersion='string',
        AutomationTargetParameterName='string',
        MaxErrors='string',
        MaxConcurrency='string',
        ComplianceSeverity='CRITICAL'|'HIGH'|'MEDIUM'|'LOW'|'UNSPECIFIED',
        SyncCompliance='AUTO'|'MANUAL'
    )
    
    
    :type AssociationId: string
    :param AssociationId: [REQUIRED]\nThe ID of the association you want to update.\n

    :type Parameters: dict
    :param Parameters: The parameters you want to update for the association. If you create a parameter using Parameter Store, you can reference the parameter using {{ssm:parameter-name}}\n\n(string) --\n(list) --\n(string) --\n\n\n\n\n\n

    :type DocumentVersion: string
    :param DocumentVersion: The document version you want update for the association.

    :type ScheduleExpression: string
    :param ScheduleExpression: The cron expression used to schedule the association that you want to update.

    :type OutputLocation: dict
    :param OutputLocation: An S3 bucket where you want to store the results of this request.\n\nS3Location (dict) --An S3 bucket where you want to store the results of this request.\n\nOutputS3Region (string) --(Deprecated) You can no longer specify this parameter. The system ignores it. Instead, Systems Manager automatically determines the Region of the S3 bucket.\n\nOutputS3BucketName (string) --The name of the S3 bucket.\n\nOutputS3KeyPrefix (string) --The S3 bucket subfolder.\n\n\n\n\n

    :type Name: string
    :param Name: The name of the SSM document that contains the configuration information for the instance. You can specify Command or Automation documents.\nYou can specify AWS-predefined documents, documents you created, or a document that is shared with you from another account.\nFor SSM documents that are shared with you from other AWS accounts, you must specify the complete SSM document ARN, in the following format:\n\n``arn:aws:ssm:region :account-id :document/document-name ``\nFor example:\n\narn:aws:ssm:us-east-2:12345678912:document/My-Shared-Document\nFor AWS-predefined documents and SSM documents you created in your account, you only need to specify the document name. For example, AWS-ApplyPatchBaseline or My-Document .\n

    :type Targets: list
    :param Targets: The targets of the association.\n\n(dict) --An array of search criteria that targets instances using a Key,Value combination that you specify.\nSupported formats include the following.\n\n``Key=InstanceIds,Values=*instance-id-1* ,*instance-id-2* ,*instance-id-3* ``\n``Key=tag:my-tag-key ,Values=*my-tag-value-1* ,*my-tag-value-2* ``\n``Key=tag-key,Values=*my-tag-key-1* ,*my-tag-key-2* ``\n(Maintenance window targets only) ``Key=resource-groups:Name,Values=*resource-group-name* ``\n(Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*resource-type-1* ,*resource-type-2* ``\n\nFor example:\n\nKey=InstanceIds,Values=i-02573cafcfEXAMPLE,i-0471e04240EXAMPLE,i-07782c72faEXAMPLE\nKey=tag:CostCenter,Values=CostCenter1,CostCenter2,CostCenter3\nKey=tag-key,Values=Name,Instance-Type,CostCenter\n(Maintenance window targets only) Key=resource-groups:Name,Values=ProductionResourceGroup  This example demonstrates how to target all resources in the resource group ProductionResourceGroup in your maintenance window.\n(Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*AWS::EC2::INSTANCE* ,*AWS::EC2::VPC* ``  This example demonstrates how to target only EC2 instances and VPCs in your maintenance window.\n(State Manager association targets only) Key=InstanceIds,Values=*  This example demonstrates how to target all managed instances in the AWS Region where the association was created.\n\nFor information about how to send commands that target instances using Key,Value parameters, see Targeting multiple instances in the AWS Systems Manager User Guide .\n\nKey (string) --User-defined criteria for sending commands that target instances that meet the criteria.\n\nValues (list) --User-defined criteria that maps to Key . For example, if you specified tag:ServerRole , you could specify value:WebServer to run a command on instances that include EC2 tags of ServerRole,WebServer .\n\n(string) --\n\n\n\n\n\n

    :type AssociationName: string
    :param AssociationName: The name of the association that you want to update.

    :type AssociationVersion: string
    :param AssociationVersion: This parameter is provided for concurrency control purposes. You must specify the latest association version in the service. If you want to ensure that this request succeeds, either specify $LATEST , or omit this parameter.

    :type AutomationTargetParameterName: string
    :param AutomationTargetParameterName: Specify the target for the association. This target is required for associations that use an Automation document and target resources by using rate controls.

    :type MaxErrors: string
    :param MaxErrors: The number of errors that are allowed before the system stops sending requests to run the association on additional targets. You can specify either an absolute number of errors, for example 10, or a percentage of the target set, for example 10%. If you specify 3, for example, the system stops sending requests when the fourth error is received. If you specify 0, then the system stops sending requests after the first error is returned. If you run an association on 50 instances and set MaxError to 10%, then the system stops sending the request when the sixth error is received.\nExecutions that are already running an association when MaxErrors is reached are allowed to complete, but some of these executions may fail as well. If you need to ensure that there won\'t be more than max-errors failed executions, set MaxConcurrency to 1 so that executions proceed one at a time.\n

    :type MaxConcurrency: string
    :param MaxConcurrency: The maximum number of targets allowed to run the association at the same time. You can specify a number, for example 10, or a percentage of the target set, for example 10%. The default value is 100%, which means all targets run the association at the same time.\nIf a new instance starts and attempts to run an association while Systems Manager is running MaxConcurrency associations, the association is allowed to run. During the next association interval, the new instance will process its association within the limit specified for MaxConcurrency.\n

    :type ComplianceSeverity: string
    :param ComplianceSeverity: The severity level to assign to the association.

    :type SyncCompliance: string
    :param SyncCompliance: The mode for generating association compliance. You can specify AUTO or MANUAL . In AUTO mode, the system uses the status of the association execution to determine the compliance status. If the association execution runs successfully, then the association is COMPLIANT . If the association execution doesn\'t run successfully, the association is NON-COMPLIANT .\nIn MANUAL mode, you must specify the AssociationId as a parameter for the PutComplianceItems API action. In this case, compliance data is not managed by State Manager. It is managed by your direct call to the PutComplianceItems API action.\nBy default, all associations use AUTO mode.\n

    :rtype: dict

ReturnsResponse Syntax
{
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
        'AutomationTargetParameterName': 'string',
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
        'AssociationName': 'string',
        'MaxErrors': 'string',
        'MaxConcurrency': 'string',
        'ComplianceSeverity': 'CRITICAL'|'HIGH'|'MEDIUM'|'LOW'|'UNSPECIFIED',
        'SyncCompliance': 'AUTO'|'MANUAL'
    }
}


Response Structure

(dict) --

AssociationDescription (dict) --
The description of the association that was updated.

Name (string) --
The name of the Systems Manager document.

InstanceId (string) --
The ID of the instance.

AssociationVersion (string) --
The association version.

Date (datetime) --
The date when the association was made.

LastUpdateAssociationDate (datetime) --
The date when the association was last updated.

Status (dict) --
The association status.

Date (datetime) --
The date when the status changed.

Name (string) --
The status.

Message (string) --
The reason for the status.

AdditionalInfo (string) --
A user-defined string.



Overview (dict) --
Information about the association.

Status (string) --
The status of the association. Status can be: Pending, Success, or Failed.

DetailedStatus (string) --
A detailed status of the association.

AssociationStatusAggregatedCount (dict) --
Returns the number of targets for the association status. For example, if you created an association with two instances, and one of them was successful, this would return the count of instances by status.

(string) --
(integer) --






DocumentVersion (string) --
The document version.

AutomationTargetParameterName (string) --
Specify the target for the association. This target is required for associations that use an Automation document and target resources by using rate controls.

Parameters (dict) --
A description of the parameters for a document.

(string) --
(list) --
(string) --






AssociationId (string) --
The association ID.

Targets (list) --
The instances targeted by the request.

(dict) --
An array of search criteria that targets instances using a Key,Value combination that you specify.
Supported formats include the following.

``Key=InstanceIds,Values=*instance-id-1* ,*instance-id-2* ,*instance-id-3* ``
``Key=tag:my-tag-key ,Values=*my-tag-value-1* ,*my-tag-value-2* ``
``Key=tag-key,Values=*my-tag-key-1* ,*my-tag-key-2* ``
(Maintenance window targets only) ``Key=resource-groups:Name,Values=*resource-group-name* ``
(Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*resource-type-1* ,*resource-type-2* ``

For example:

Key=InstanceIds,Values=i-02573cafcfEXAMPLE,i-0471e04240EXAMPLE,i-07782c72faEXAMPLE
Key=tag:CostCenter,Values=CostCenter1,CostCenter2,CostCenter3
Key=tag-key,Values=Name,Instance-Type,CostCenter
(Maintenance window targets only) Key=resource-groups:Name,Values=ProductionResourceGroup   This example demonstrates how to target all resources in the resource group ProductionResourceGroup in your maintenance window.
(Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*AWS::EC2::INSTANCE* ,*AWS::EC2::VPC* ``   This example demonstrates how to target only EC2 instances and VPCs in your maintenance window.
(State Manager association targets only) Key=InstanceIds,Values=*   This example demonstrates how to target all managed instances in the AWS Region where the association was created.

For information about how to send commands that target instances using Key,Value parameters, see Targeting multiple instances in the AWS Systems Manager User Guide .

Key (string) --
User-defined criteria for sending commands that target instances that meet the criteria.

Values (list) --
User-defined criteria that maps to Key . For example, if you specified tag:ServerRole , you could specify value:WebServer to run a command on instances that include EC2 tags of ServerRole,WebServer .

(string) --






ScheduleExpression (string) --
A cron expression that specifies a schedule when the association runs.

OutputLocation (dict) --
An S3 bucket where you want to store the output details of the request.

S3Location (dict) --
An S3 bucket where you want to store the results of this request.

OutputS3Region (string) --
(Deprecated) You can no longer specify this parameter. The system ignores it. Instead, Systems Manager automatically determines the Region of the S3 bucket.

OutputS3BucketName (string) --
The name of the S3 bucket.

OutputS3KeyPrefix (string) --
The S3 bucket subfolder.





LastExecutionDate (datetime) --
The date on which the association was last run.

LastSuccessfulExecutionDate (datetime) --
The last date on which the association was successfully run.

AssociationName (string) --
The association name.

MaxErrors (string) --
The number of errors that are allowed before the system stops sending requests to run the association on additional targets. You can specify either an absolute number of errors, for example 10, or a percentage of the target set, for example 10%. If you specify 3, for example, the system stops sending requests when the fourth error is received. If you specify 0, then the system stops sending requests after the first error is returned. If you run an association on 50 instances and set MaxError to 10%, then the system stops sending the request when the sixth error is received.
Executions that are already running an association when MaxErrors is reached are allowed to complete, but some of these executions may fail as well. If you need to ensure that there won\'t be more than max-errors failed executions, set MaxConcurrency to 1 so that executions proceed one at a time.

MaxConcurrency (string) --
The maximum number of targets allowed to run the association at the same time. You can specify a number, for example 10, or a percentage of the target set, for example 10%. The default value is 100%, which means all targets run the association at the same time.
If a new instance starts and attempts to run an association while Systems Manager is running MaxConcurrency associations, the association is allowed to run. During the next association interval, the new instance will process its association within the limit specified for MaxConcurrency.

ComplianceSeverity (string) --
The severity level that is assigned to the association.

SyncCompliance (string) --
The mode for generating association compliance. You can specify AUTO or MANUAL . In AUTO mode, the system uses the status of the association execution to determine the compliance status. If the association execution runs successfully, then the association is COMPLIANT . If the association execution doesn\'t run successfully, the association is NON-COMPLIANT .
In MANUAL mode, you must specify the AssociationId as a parameter for the  PutComplianceItems API action. In this case, compliance data is not managed by State Manager. It is managed by your direct call to the  PutComplianceItems API action.
By default, all associations use AUTO mode.









Exceptions

SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.InvalidSchedule
SSM.Client.exceptions.InvalidParameters
SSM.Client.exceptions.InvalidOutputLocation
SSM.Client.exceptions.InvalidDocumentVersion
SSM.Client.exceptions.AssociationDoesNotExist
SSM.Client.exceptions.InvalidUpdate
SSM.Client.exceptions.TooManyUpdates
SSM.Client.exceptions.InvalidDocument
SSM.Client.exceptions.InvalidTarget
SSM.Client.exceptions.InvalidAssociationVersion
SSM.Client.exceptions.AssociationVersionLimitExceeded


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
            'AutomationTargetParameterName': 'string',
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
            'AssociationName': 'string',
            'MaxErrors': 'string',
            'MaxConcurrency': 'string',
            'ComplianceSeverity': 'CRITICAL'|'HIGH'|'MEDIUM'|'LOW'|'UNSPECIFIED',
            'SyncCompliance': 'AUTO'|'MANUAL'
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
    
    Exceptions
    
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
    :param Name: [REQUIRED]\nThe name of the Systems Manager document.\n

    :type InstanceId: string
    :param InstanceId: [REQUIRED]\nThe ID of the instance.\n

    :type AssociationStatus: dict
    :param AssociationStatus: [REQUIRED]\nThe association status.\n\nDate (datetime) -- [REQUIRED]The date when the status changed.\n\nName (string) -- [REQUIRED]The status.\n\nMessage (string) -- [REQUIRED]The reason for the status.\n\nAdditionalInfo (string) --A user-defined string.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
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
        'AutomationTargetParameterName': 'string',
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
        'AssociationName': 'string',
        'MaxErrors': 'string',
        'MaxConcurrency': 'string',
        'ComplianceSeverity': 'CRITICAL'|'HIGH'|'MEDIUM'|'LOW'|'UNSPECIFIED',
        'SyncCompliance': 'AUTO'|'MANUAL'
    }
}


Response Structure

(dict) --

AssociationDescription (dict) --
Information about the association.

Name (string) --
The name of the Systems Manager document.

InstanceId (string) --
The ID of the instance.

AssociationVersion (string) --
The association version.

Date (datetime) --
The date when the association was made.

LastUpdateAssociationDate (datetime) --
The date when the association was last updated.

Status (dict) --
The association status.

Date (datetime) --
The date when the status changed.

Name (string) --
The status.

Message (string) --
The reason for the status.

AdditionalInfo (string) --
A user-defined string.



Overview (dict) --
Information about the association.

Status (string) --
The status of the association. Status can be: Pending, Success, or Failed.

DetailedStatus (string) --
A detailed status of the association.

AssociationStatusAggregatedCount (dict) --
Returns the number of targets for the association status. For example, if you created an association with two instances, and one of them was successful, this would return the count of instances by status.

(string) --
(integer) --






DocumentVersion (string) --
The document version.

AutomationTargetParameterName (string) --
Specify the target for the association. This target is required for associations that use an Automation document and target resources by using rate controls.

Parameters (dict) --
A description of the parameters for a document.

(string) --
(list) --
(string) --






AssociationId (string) --
The association ID.

Targets (list) --
The instances targeted by the request.

(dict) --
An array of search criteria that targets instances using a Key,Value combination that you specify.
Supported formats include the following.

``Key=InstanceIds,Values=*instance-id-1* ,*instance-id-2* ,*instance-id-3* ``
``Key=tag:my-tag-key ,Values=*my-tag-value-1* ,*my-tag-value-2* ``
``Key=tag-key,Values=*my-tag-key-1* ,*my-tag-key-2* ``
(Maintenance window targets only) ``Key=resource-groups:Name,Values=*resource-group-name* ``
(Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*resource-type-1* ,*resource-type-2* ``

For example:

Key=InstanceIds,Values=i-02573cafcfEXAMPLE,i-0471e04240EXAMPLE,i-07782c72faEXAMPLE
Key=tag:CostCenter,Values=CostCenter1,CostCenter2,CostCenter3
Key=tag-key,Values=Name,Instance-Type,CostCenter
(Maintenance window targets only) Key=resource-groups:Name,Values=ProductionResourceGroup   This example demonstrates how to target all resources in the resource group ProductionResourceGroup in your maintenance window.
(Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*AWS::EC2::INSTANCE* ,*AWS::EC2::VPC* ``   This example demonstrates how to target only EC2 instances and VPCs in your maintenance window.
(State Manager association targets only) Key=InstanceIds,Values=*   This example demonstrates how to target all managed instances in the AWS Region where the association was created.

For information about how to send commands that target instances using Key,Value parameters, see Targeting multiple instances in the AWS Systems Manager User Guide .

Key (string) --
User-defined criteria for sending commands that target instances that meet the criteria.

Values (list) --
User-defined criteria that maps to Key . For example, if you specified tag:ServerRole , you could specify value:WebServer to run a command on instances that include EC2 tags of ServerRole,WebServer .

(string) --






ScheduleExpression (string) --
A cron expression that specifies a schedule when the association runs.

OutputLocation (dict) --
An S3 bucket where you want to store the output details of the request.

S3Location (dict) --
An S3 bucket where you want to store the results of this request.

OutputS3Region (string) --
(Deprecated) You can no longer specify this parameter. The system ignores it. Instead, Systems Manager automatically determines the Region of the S3 bucket.

OutputS3BucketName (string) --
The name of the S3 bucket.

OutputS3KeyPrefix (string) --
The S3 bucket subfolder.





LastExecutionDate (datetime) --
The date on which the association was last run.

LastSuccessfulExecutionDate (datetime) --
The last date on which the association was successfully run.

AssociationName (string) --
The association name.

MaxErrors (string) --
The number of errors that are allowed before the system stops sending requests to run the association on additional targets. You can specify either an absolute number of errors, for example 10, or a percentage of the target set, for example 10%. If you specify 3, for example, the system stops sending requests when the fourth error is received. If you specify 0, then the system stops sending requests after the first error is returned. If you run an association on 50 instances and set MaxError to 10%, then the system stops sending the request when the sixth error is received.
Executions that are already running an association when MaxErrors is reached are allowed to complete, but some of these executions may fail as well. If you need to ensure that there won\'t be more than max-errors failed executions, set MaxConcurrency to 1 so that executions proceed one at a time.

MaxConcurrency (string) --
The maximum number of targets allowed to run the association at the same time. You can specify a number, for example 10, or a percentage of the target set, for example 10%. The default value is 100%, which means all targets run the association at the same time.
If a new instance starts and attempts to run an association while Systems Manager is running MaxConcurrency associations, the association is allowed to run. During the next association interval, the new instance will process its association within the limit specified for MaxConcurrency.

ComplianceSeverity (string) --
The severity level that is assigned to the association.

SyncCompliance (string) --
The mode for generating association compliance. You can specify AUTO or MANUAL . In AUTO mode, the system uses the status of the association execution to determine the compliance status. If the association execution runs successfully, then the association is COMPLIANT . If the association execution doesn\'t run successfully, the association is NON-COMPLIANT .
In MANUAL mode, you must specify the AssociationId as a parameter for the  PutComplianceItems API action. In this case, compliance data is not managed by State Manager. It is managed by your direct call to the  PutComplianceItems API action.
By default, all associations use AUTO mode.









Exceptions

SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.InvalidInstanceId
SSM.Client.exceptions.InvalidDocument
SSM.Client.exceptions.AssociationDoesNotExist
SSM.Client.exceptions.StatusUnchanged
SSM.Client.exceptions.TooManyUpdates


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
            'AutomationTargetParameterName': 'string',
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
            'AssociationName': 'string',
            'MaxErrors': 'string',
            'MaxConcurrency': 'string',
            'ComplianceSeverity': 'CRITICAL'|'HIGH'|'MEDIUM'|'LOW'|'UNSPECIFIED',
            'SyncCompliance': 'AUTO'|'MANUAL'
        }
    }
    
    
    :returns: 
    (string) --
    (integer) --
    
    
    
    """
    pass

def update_document(Content=None, Attachments=None, Name=None, VersionName=None, DocumentVersion=None, DocumentFormat=None, TargetType=None):
    """
    Updates one or more values for an SSM document.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_document(
        Content='string',
        Attachments=[
            {
                'Key': 'SourceUrl'|'S3FileUrl'|'AttachmentReference',
                'Values': [
                    'string',
                ],
                'Name': 'string'
            },
        ],
        Name='string',
        VersionName='string',
        DocumentVersion='string',
        DocumentFormat='YAML'|'JSON'|'TEXT',
        TargetType='string'
    )
    
    
    :type Content: string
    :param Content: [REQUIRED]\nA valid JSON or YAML string.\n

    :type Attachments: list
    :param Attachments: A list of key and value pairs that describe attachments to a version of a document.\n\n(dict) --Identifying information about a document attachment, including the file name and a key-value pair that identifies the location of an attachment to a document.\n\nKey (string) --The key of a key-value pair that identifies the location of an attachment to a document.\n\nValues (list) --The value of a key-value pair that identifies the location of an attachment to a document. The format for Value depends on the type of key you specify.\n\nFor the key SourceUrl , the value is an S3 bucket location. For example: 'Values': [ 's3://my-bucket/my-folder' ]\nFor the key S3FileUrl , the value is a file in an S3 bucket. For example: 'Values': [ 's3://my-bucket/my-folder/my-file.py' ]\nFor the key AttachmentReference , the value is constructed from the name of another SSM document in your account, a version number of that document, and a file attached to that document version that you want to reuse. For example: 'Values': [ 'MyOtherDocument/3/my-other-file.py' ]  However, if the SSM document is shared with you from another account, the full SSM document ARN must be specified instead of the document name only. For example: 'Values': [ 'arn:aws:ssm:us-east-2:111122223333:document/OtherAccountDocument/3/their-file.py' ]\n\n\n(string) --\n\n\nName (string) --The name of the document attachment file.\n\n\n\n\n

    :type Name: string
    :param Name: [REQUIRED]\nThe name of the document that you want to update.\n

    :type VersionName: string
    :param VersionName: An optional field specifying the version of the artifact you are updating with the document. For example, 'Release 12, Update 6'. This value is unique across all versions of a document, and cannot be changed.

    :type DocumentVersion: string
    :param DocumentVersion: (Required) The latest version of the document that you want to update. The latest document version can be specified using the $LATEST variable or by the version number. Updating a previous version of a document is not supported.

    :type DocumentFormat: string
    :param DocumentFormat: Specify the document format for the new document version. Systems Manager supports JSON and YAML documents. JSON is the default format.

    :type TargetType: string
    :param TargetType: Specify a new target type for the document.

    :rtype: dict

ReturnsResponse Syntax
{
    'DocumentDescription': {
        'Sha1': 'string',
        'Hash': 'string',
        'HashType': 'Sha256'|'Sha1',
        'Name': 'string',
        'VersionName': 'string',
        'Owner': 'string',
        'CreatedDate': datetime(2015, 1, 1),
        'Status': 'Creating'|'Active'|'Updating'|'Deleting'|'Failed',
        'StatusInformation': 'string',
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
        'DocumentType': 'Command'|'Policy'|'Automation'|'Session'|'Package'|'ApplicationConfiguration'|'ApplicationConfigurationSchema'|'DeploymentStrategy'|'ChangeCalendar',
        'SchemaVersion': 'string',
        'LatestVersion': 'string',
        'DefaultVersion': 'string',
        'DocumentFormat': 'YAML'|'JSON'|'TEXT',
        'TargetType': 'string',
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        'AttachmentsInformation': [
            {
                'Name': 'string'
            },
        ],
        'Requires': [
            {
                'Name': 'string',
                'Version': 'string'
            },
        ]
    }
}


Response Structure

(dict) --

DocumentDescription (dict) --
A description of the document that was updated.

Sha1 (string) --
The SHA1 hash of the document, which you can use for verification.

Hash (string) --
The Sha256 or Sha1 hash created by the system when the document was created.

Note
Sha1 hashes have been deprecated.


HashType (string) --
The hash type of the document. Valid values include Sha256 or Sha1 .

Note
Sha1 hashes have been deprecated.


Name (string) --
The name of the Systems Manager document.

VersionName (string) --
The version of the artifact associated with the document.

Owner (string) --
The AWS user account that created the document.

CreatedDate (datetime) --
The date when the document was created.

Status (string) --
The status of the Systems Manager document.

StatusInformation (string) --
A message returned by AWS Systems Manager that explains the Status value. For example, a Failed status might be explained by the StatusInformation message, "The specified S3 bucket does not exist. Verify that the URL of the S3 bucket is correct."

DocumentVersion (string) --
The document version.

Description (string) --
A description of the document.

Parameters (list) --
A description of the parameters for a document.

(dict) --
Parameters specified in a System Manager document that run on the server when the command is run.

Name (string) --
The name of the parameter.

Type (string) --
The type of parameter. The type can be either String or StringList.

Description (string) --
A description of what the parameter does, how to use it, the default value, and whether or not the parameter is optional.

DefaultValue (string) --
If specified, the default values for the parameters. Parameters without a default value are required. Parameters with a default value are optional.





PlatformTypes (list) --
The list of OS platforms compatible with this Systems Manager document.

(string) --


DocumentType (string) --
The type of document.

SchemaVersion (string) --
The schema version.

LatestVersion (string) --
The latest version of the document.

DefaultVersion (string) --
The default version.

DocumentFormat (string) --
The document format, either JSON or YAML.

TargetType (string) --
The target type which defines the kinds of resources the document can run on. For example, /AWS::EC2::Instance. For a list of valid resource types, see AWS resource and property types reference in the AWS CloudFormation User Guide .

Tags (list) --
The tags, or metadata, that have been applied to the document.

(dict) --
Metadata that you assign to your AWS resources. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment. In Systems Manager, you can apply tags to documents, managed instances, maintenance windows, Parameter Store parameters, and patch baselines.

Key (string) --
The name of the tag.

Value (string) --
The value of the tag.





AttachmentsInformation (list) --
Details about the document attachments, including names, locations, sizes, and so on.

(dict) --
An attribute of an attachment, such as the attachment name.

Name (string) --
The name of the attachment.





Requires (list) --
A list of SSM documents required by a document. For example, an ApplicationConfiguration document requires an ApplicationConfigurationSchema document.

(dict) --
An SSM document required by the current document.

Name (string) --
The name of the required SSM document. The name can be an Amazon Resource Name (ARN).

Version (string) --
The document version required by the current document.













Exceptions

SSM.Client.exceptions.MaxDocumentSizeExceeded
SSM.Client.exceptions.DocumentVersionLimitExceeded
SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.DuplicateDocumentContent
SSM.Client.exceptions.DuplicateDocumentVersionName
SSM.Client.exceptions.InvalidDocumentContent
SSM.Client.exceptions.InvalidDocumentVersion
SSM.Client.exceptions.InvalidDocumentSchemaVersion
SSM.Client.exceptions.InvalidDocument
SSM.Client.exceptions.InvalidDocumentOperation


    :return: {
        'DocumentDescription': {
            'Sha1': 'string',
            'Hash': 'string',
            'HashType': 'Sha256'|'Sha1',
            'Name': 'string',
            'VersionName': 'string',
            'Owner': 'string',
            'CreatedDate': datetime(2015, 1, 1),
            'Status': 'Creating'|'Active'|'Updating'|'Deleting'|'Failed',
            'StatusInformation': 'string',
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
            'DocumentType': 'Command'|'Policy'|'Automation'|'Session'|'Package'|'ApplicationConfiguration'|'ApplicationConfigurationSchema'|'DeploymentStrategy'|'ChangeCalendar',
            'SchemaVersion': 'string',
            'LatestVersion': 'string',
            'DefaultVersion': 'string',
            'DocumentFormat': 'YAML'|'JSON'|'TEXT',
            'TargetType': 'string',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'AttachmentsInformation': [
                {
                    'Name': 'string'
                },
            ],
            'Requires': [
                {
                    'Name': 'string',
                    'Version': 'string'
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
    
    Exceptions
    
    :example: response = client.update_document_default_version(
        Name='string',
        DocumentVersion='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of a custom document that you want to set as the default version.\n

    :type DocumentVersion: string
    :param DocumentVersion: [REQUIRED]\nThe version of a custom document that you want to set as the default version.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Description': {
        'Name': 'string',
        'DefaultVersion': 'string',
        'DefaultVersionName': 'string'
    }
}


Response Structure

(dict) --

Description (dict) --
The description of a custom document that you want to set as the default version.

Name (string) --
The name of the document.

DefaultVersion (string) --
The default version of the document.

DefaultVersionName (string) --
The default version of the artifact associated with the document.









Exceptions

SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.InvalidDocument
SSM.Client.exceptions.InvalidDocumentVersion
SSM.Client.exceptions.InvalidDocumentSchemaVersion


    :return: {
        'Description': {
            'Name': 'string',
            'DefaultVersion': 'string',
            'DefaultVersionName': 'string'
        }
    }
    
    
    :returns: 
    SSM.Client.exceptions.InternalServerError
    SSM.Client.exceptions.InvalidDocument
    SSM.Client.exceptions.InvalidDocumentVersion
    SSM.Client.exceptions.InvalidDocumentSchemaVersion
    
    """
    pass

def update_maintenance_window(WindowId=None, Name=None, Description=None, StartDate=None, EndDate=None, Schedule=None, ScheduleTimezone=None, Duration=None, Cutoff=None, AllowUnassociatedTargets=None, Enabled=None, Replace=None):
    """
    Updates an existing maintenance window. Only specified parameters are modified.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_maintenance_window(
        WindowId='string',
        Name='string',
        Description='string',
        StartDate='string',
        EndDate='string',
        Schedule='string',
        ScheduleTimezone='string',
        Duration=123,
        Cutoff=123,
        AllowUnassociatedTargets=True|False,
        Enabled=True|False,
        Replace=True|False
    )
    
    
    :type WindowId: string
    :param WindowId: [REQUIRED]\nThe ID of the maintenance window to update.\n

    :type Name: string
    :param Name: The name of the maintenance window.

    :type Description: string
    :param Description: An optional description for the update request.

    :type StartDate: string
    :param StartDate: The time zone that the scheduled maintenance window executions are based on, in Internet Assigned Numbers Authority (IANA) format. For example: 'America/Los_Angeles', 'etc/UTC', or 'Asia/Seoul'. For more information, see the Time Zone Database on the IANA website.

    :type EndDate: string
    :param EndDate: The date and time, in ISO-8601 Extended format, for when you want the maintenance window to become inactive. EndDate allows you to set a date and time in the future when the maintenance window will no longer run.

    :type Schedule: string
    :param Schedule: The schedule of the maintenance window in the form of a cron or rate expression.

    :type ScheduleTimezone: string
    :param ScheduleTimezone: The time zone that the scheduled maintenance window executions are based on, in Internet Assigned Numbers Authority (IANA) format. For example: 'America/Los_Angeles', 'etc/UTC', or 'Asia/Seoul'. For more information, see the Time Zone Database on the IANA website.

    :type Duration: integer
    :param Duration: The duration of the maintenance window in hours.

    :type Cutoff: integer
    :param Cutoff: The number of hours before the end of the maintenance window that Systems Manager stops scheduling new tasks for execution.

    :type AllowUnassociatedTargets: boolean
    :param AllowUnassociatedTargets: Whether targets must be registered with the maintenance window before tasks can be defined for those targets.

    :type Enabled: boolean
    :param Enabled: Whether the maintenance window is enabled.

    :type Replace: boolean
    :param Replace: If True, then all fields that are required by the CreateMaintenanceWindow action are also required for this API request. Optional fields that are not specified are set to null.

    :rtype: dict

ReturnsResponse Syntax
{
    'WindowId': 'string',
    'Name': 'string',
    'Description': 'string',
    'StartDate': 'string',
    'EndDate': 'string',
    'Schedule': 'string',
    'ScheduleTimezone': 'string',
    'Duration': 123,
    'Cutoff': 123,
    'AllowUnassociatedTargets': True|False,
    'Enabled': True|False
}


Response Structure

(dict) --

WindowId (string) --
The ID of the created maintenance window.

Name (string) --
The name of the maintenance window.

Description (string) --
An optional description of the update.

StartDate (string) --
The date and time, in ISO-8601 Extended format, for when the maintenance window is scheduled to become active. The maintenance window will not run before this specified time.

EndDate (string) --
The date and time, in ISO-8601 Extended format, for when the maintenance window is scheduled to become inactive. The maintenance window will not run after this specified time.

Schedule (string) --
The schedule of the maintenance window in the form of a cron or rate expression.

ScheduleTimezone (string) --
The time zone that the scheduled maintenance window executions are based on, in Internet Assigned Numbers Authority (IANA) format. For example: "America/Los_Angeles", "etc/UTC", or "Asia/Seoul". For more information, see the Time Zone Database on the IANA website.

Duration (integer) --
The duration of the maintenance window in hours.

Cutoff (integer) --
The number of hours before the end of the maintenance window that Systems Manager stops scheduling new tasks for execution.

AllowUnassociatedTargets (boolean) --
Whether targets must be registered with the maintenance window before tasks can be defined for those targets.

Enabled (boolean) --
Whether the maintenance window is enabled.







Exceptions

SSM.Client.exceptions.DoesNotExistException
SSM.Client.exceptions.InternalServerError


    :return: {
        'WindowId': 'string',
        'Name': 'string',
        'Description': 'string',
        'StartDate': 'string',
        'EndDate': 'string',
        'Schedule': 'string',
        'ScheduleTimezone': 'string',
        'Duration': 123,
        'Cutoff': 123,
        'AllowUnassociatedTargets': True|False,
        'Enabled': True|False
    }
    
    
    :returns: 
    SSM.Client.exceptions.DoesNotExistException
    SSM.Client.exceptions.InternalServerError
    
    """
    pass

def update_maintenance_window_target(WindowId=None, WindowTargetId=None, Targets=None, OwnerInformation=None, Name=None, Description=None, Replace=None):
    """
    Modifies the target of an existing maintenance window. You can change the following:
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param WindowId: [REQUIRED]\nThe maintenance window ID with which to modify the target.\n

    :type WindowTargetId: string
    :param WindowTargetId: [REQUIRED]\nThe target ID to modify.\n

    :type Targets: list
    :param Targets: The targets to add or replace.\n\n(dict) --An array of search criteria that targets instances using a Key,Value combination that you specify.\nSupported formats include the following.\n\n``Key=InstanceIds,Values=*instance-id-1* ,*instance-id-2* ,*instance-id-3* ``\n``Key=tag:my-tag-key ,Values=*my-tag-value-1* ,*my-tag-value-2* ``\n``Key=tag-key,Values=*my-tag-key-1* ,*my-tag-key-2* ``\n(Maintenance window targets only) ``Key=resource-groups:Name,Values=*resource-group-name* ``\n(Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*resource-type-1* ,*resource-type-2* ``\n\nFor example:\n\nKey=InstanceIds,Values=i-02573cafcfEXAMPLE,i-0471e04240EXAMPLE,i-07782c72faEXAMPLE\nKey=tag:CostCenter,Values=CostCenter1,CostCenter2,CostCenter3\nKey=tag-key,Values=Name,Instance-Type,CostCenter\n(Maintenance window targets only) Key=resource-groups:Name,Values=ProductionResourceGroup  This example demonstrates how to target all resources in the resource group ProductionResourceGroup in your maintenance window.\n(Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*AWS::EC2::INSTANCE* ,*AWS::EC2::VPC* ``  This example demonstrates how to target only EC2 instances and VPCs in your maintenance window.\n(State Manager association targets only) Key=InstanceIds,Values=*  This example demonstrates how to target all managed instances in the AWS Region where the association was created.\n\nFor information about how to send commands that target instances using Key,Value parameters, see Targeting multiple instances in the AWS Systems Manager User Guide .\n\nKey (string) --User-defined criteria for sending commands that target instances that meet the criteria.\n\nValues (list) --User-defined criteria that maps to Key . For example, if you specified tag:ServerRole , you could specify value:WebServer to run a command on instances that include EC2 tags of ServerRole,WebServer .\n\n(string) --\n\n\n\n\n\n

    :type OwnerInformation: string
    :param OwnerInformation: User-provided value that will be included in any CloudWatch events raised while running tasks for these targets in this maintenance window.

    :type Name: string
    :param Name: A name for the update.

    :type Description: string
    :param Description: An optional description for the update.

    :type Replace: boolean
    :param Replace: If True, then all fields that are required by the RegisterTargetWithMaintenanceWindow action are also required for this API request. Optional fields that are not specified are set to null.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

WindowId (string) --
The maintenance window ID specified in the update request.

WindowTargetId (string) --
The target ID specified in the update request.

Targets (list) --
The updated targets.

(dict) --
An array of search criteria that targets instances using a Key,Value combination that you specify.
Supported formats include the following.

``Key=InstanceIds,Values=*instance-id-1* ,*instance-id-2* ,*instance-id-3* ``
``Key=tag:my-tag-key ,Values=*my-tag-value-1* ,*my-tag-value-2* ``
``Key=tag-key,Values=*my-tag-key-1* ,*my-tag-key-2* ``
(Maintenance window targets only) ``Key=resource-groups:Name,Values=*resource-group-name* ``
(Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*resource-type-1* ,*resource-type-2* ``

For example:

Key=InstanceIds,Values=i-02573cafcfEXAMPLE,i-0471e04240EXAMPLE,i-07782c72faEXAMPLE
Key=tag:CostCenter,Values=CostCenter1,CostCenter2,CostCenter3
Key=tag-key,Values=Name,Instance-Type,CostCenter
(Maintenance window targets only) Key=resource-groups:Name,Values=ProductionResourceGroup   This example demonstrates how to target all resources in the resource group ProductionResourceGroup in your maintenance window.
(Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*AWS::EC2::INSTANCE* ,*AWS::EC2::VPC* ``   This example demonstrates how to target only EC2 instances and VPCs in your maintenance window.
(State Manager association targets only) Key=InstanceIds,Values=*   This example demonstrates how to target all managed instances in the AWS Region where the association was created.

For information about how to send commands that target instances using Key,Value parameters, see Targeting multiple instances in the AWS Systems Manager User Guide .

Key (string) --
User-defined criteria for sending commands that target instances that meet the criteria.

Values (list) --
User-defined criteria that maps to Key . For example, if you specified tag:ServerRole , you could specify value:WebServer to run a command on instances that include EC2 tags of ServerRole,WebServer .

(string) --






OwnerInformation (string) --
The updated owner.

Name (string) --
The updated name.

Description (string) --
The updated description.







Exceptions

SSM.Client.exceptions.DoesNotExistException
SSM.Client.exceptions.InternalServerError


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
    WindowId (string) -- [REQUIRED]
    The maintenance window ID with which to modify the target.
    
    WindowTargetId (string) -- [REQUIRED]
    The target ID to modify.
    
    Targets (list) -- The targets to add or replace.
    
    (dict) --An array of search criteria that targets instances using a Key,Value combination that you specify.
    Supported formats include the following.
    
    ``Key=InstanceIds,Values=*instance-id-1* ,*instance-id-2* ,*instance-id-3* ``
    ``Key=tag:my-tag-key ,Values=*my-tag-value-1* ,*my-tag-value-2* ``
    ``Key=tag-key,Values=*my-tag-key-1* ,*my-tag-key-2* ``
    (Maintenance window targets only) ``Key=resource-groups:Name,Values=*resource-group-name* ``
    (Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*resource-type-1* ,*resource-type-2* ``
    
    For example:
    
    Key=InstanceIds,Values=i-02573cafcfEXAMPLE,i-0471e04240EXAMPLE,i-07782c72faEXAMPLE
    Key=tag:CostCenter,Values=CostCenter1,CostCenter2,CostCenter3
    Key=tag-key,Values=Name,Instance-Type,CostCenter
    (Maintenance window targets only) Key=resource-groups:Name,Values=ProductionResourceGroup   This example demonstrates how to target all resources in the resource group ProductionResourceGroup in your maintenance window.
    (Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*AWS::EC2::INSTANCE* ,*AWS::EC2::VPC* ``   This example demonstrates how to target only EC2 instances and VPCs in your maintenance window.
    (State Manager association targets only) Key=InstanceIds,Values=*   This example demonstrates how to target all managed instances in the AWS Region where the association was created.
    
    For information about how to send commands that target instances using Key,Value parameters, see Targeting multiple instances in the AWS Systems Manager User Guide .
    
    Key (string) --User-defined criteria for sending commands that target instances that meet the criteria.
    
    Values (list) --User-defined criteria that maps to Key . For example, if you specified tag:ServerRole , you could specify value:WebServer to run a command on instances that include EC2 tags of ServerRole,WebServer .
    
    (string) --
    
    
    
    
    
    
    OwnerInformation (string) -- User-provided value that will be included in any CloudWatch events raised while running tasks for these targets in this maintenance window.
    Name (string) -- A name for the update.
    Description (string) -- An optional description for the update.
    Replace (boolean) -- If True, then all fields that are required by the RegisterTargetWithMaintenanceWindow action are also required for this API request. Optional fields that are not specified are set to null.
    
    """
    pass

def update_maintenance_window_task(WindowId=None, WindowTaskId=None, Targets=None, TaskArn=None, ServiceRoleArn=None, TaskParameters=None, TaskInvocationParameters=None, Priority=None, MaxConcurrency=None, MaxErrors=None, LoggingInfo=None, Name=None, Description=None, Replace=None):
    """
    Modifies a task assigned to a maintenance window. You can\'t change the task type, but you can change the following values:
    If a parameter is null, then the corresponding field is not modified. Also, if you set Replace to true, then all fields required by the  RegisterTaskWithMaintenanceWindow action are required for this request. Optional fields that aren\'t specified are set to null.
    See also: AWS API Documentation
    
    Exceptions
    
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
                'CloudWatchOutputConfig': {
                    'CloudWatchLogGroupName': 'string',
                    'CloudWatchOutputEnabled': True|False
                },
                'DocumentHash': 'string',
                'DocumentHashType': 'Sha256'|'Sha1',
                'DocumentVersion': 'string',
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
    :param WindowId: [REQUIRED]\nThe maintenance window ID that contains the task to modify.\n

    :type WindowTaskId: string
    :param WindowTaskId: [REQUIRED]\nThe task ID to modify.\n

    :type Targets: list
    :param Targets: The targets (either instances or tags) to modify. Instances are specified using Key=instanceids,Values=instanceID_1,instanceID_2. Tags are specified using Key=tag_name,Values=tag_value.\n\n(dict) --An array of search criteria that targets instances using a Key,Value combination that you specify.\nSupported formats include the following.\n\n``Key=InstanceIds,Values=*instance-id-1* ,*instance-id-2* ,*instance-id-3* ``\n``Key=tag:my-tag-key ,Values=*my-tag-value-1* ,*my-tag-value-2* ``\n``Key=tag-key,Values=*my-tag-key-1* ,*my-tag-key-2* ``\n(Maintenance window targets only) ``Key=resource-groups:Name,Values=*resource-group-name* ``\n(Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*resource-type-1* ,*resource-type-2* ``\n\nFor example:\n\nKey=InstanceIds,Values=i-02573cafcfEXAMPLE,i-0471e04240EXAMPLE,i-07782c72faEXAMPLE\nKey=tag:CostCenter,Values=CostCenter1,CostCenter2,CostCenter3\nKey=tag-key,Values=Name,Instance-Type,CostCenter\n(Maintenance window targets only) Key=resource-groups:Name,Values=ProductionResourceGroup  This example demonstrates how to target all resources in the resource group ProductionResourceGroup in your maintenance window.\n(Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*AWS::EC2::INSTANCE* ,*AWS::EC2::VPC* ``  This example demonstrates how to target only EC2 instances and VPCs in your maintenance window.\n(State Manager association targets only) Key=InstanceIds,Values=*  This example demonstrates how to target all managed instances in the AWS Region where the association was created.\n\nFor information about how to send commands that target instances using Key,Value parameters, see Targeting multiple instances in the AWS Systems Manager User Guide .\n\nKey (string) --User-defined criteria for sending commands that target instances that meet the criteria.\n\nValues (list) --User-defined criteria that maps to Key . For example, if you specified tag:ServerRole , you could specify value:WebServer to run a command on instances that include EC2 tags of ServerRole,WebServer .\n\n(string) --\n\n\n\n\n\n

    :type TaskArn: string
    :param TaskArn: The task ARN to modify.

    :type ServiceRoleArn: string
    :param ServiceRoleArn: The ARN of the IAM service role for Systems Manager to assume when running a maintenance window task. If you do not specify a service role ARN, Systems Manager uses your account\'s service-linked role. If no service-linked role for Systems Manager exists in your account, it is created when you run RegisterTaskWithMaintenanceWindow .\nFor more information, see the following topics in the in the AWS Systems Manager User Guide :\n\nUsing service-linked roles for Systems Manager\nShould I use a service-linked role or a custom service role to run maintenance window tasks?\n\n

    :type TaskParameters: dict
    :param TaskParameters: The parameters to modify.\n\nNote\nTaskParameters has been deprecated. To specify parameters to pass to a task when it runs, instead use the Parameters option in the TaskInvocationParameters structure. For information about how Systems Manager handles these options for the supported maintenance window task types, see MaintenanceWindowTaskInvocationParameters .\n\nThe map has the following format:\nKey: string, between 1 and 255 characters\nValue: an array of strings, each string is between 1 and 255 characters\n\n(string) --\n(dict) --Defines the values for a task parameter.\n\nValues (list) --This field contains an array of 0 or more strings, each 1 to 255 characters in length.\n\n(string) --\n\n\n\n\n\n\n\n

    :type TaskInvocationParameters: dict
    :param TaskInvocationParameters: The parameters that the task should use during execution. Populate only the fields that match the task type. All other fields should be empty.\n\nRunCommand (dict) --The parameters for a RUN_COMMAND task type.\n\nComment (string) --Information about the commands to run.\n\nCloudWatchOutputConfig (dict) --Configuration options for sending command output to CloudWatch Logs.\n\nCloudWatchLogGroupName (string) --The name of the CloudWatch log group where you want to send command output. If you don\'t specify a group name, Systems Manager automatically creates a log group for you. The log group uses the following naming format: aws/ssm/SystemsManagerDocumentName .\n\nCloudWatchOutputEnabled (boolean) --Enables Systems Manager to send command output to CloudWatch Logs.\n\n\n\nDocumentHash (string) --The SHA-256 or SHA-1 hash created by the system when the document was created. SHA-1 hashes have been deprecated.\n\nDocumentHashType (string) --SHA-256 or SHA-1. SHA-1 hashes have been deprecated.\n\nDocumentVersion (string) --The SSM document version to use in the request. You can specify $DEFAULT, $LATEST, or a specific version number. If you run commands by using the AWS CLI, then you must escape the first two options by using a backslash. If you specify a version number, then you don\'t need to use the backslash. For example:\n--document-version '$DEFAULT'\n--document-version '$LATEST'\n--document-version '3'\n\nNotificationConfig (dict) --Configurations for sending notifications about command status changes on a per-instance basis.\n\nNotificationArn (string) --An Amazon Resource Name (ARN) for an Amazon Simple Notification Service (Amazon SNS) topic. Run Command pushes notifications about command status changes to this topic.\n\nNotificationEvents (list) --The different events for which you can receive notifications. These events include the following: All (events), InProgress, Success, TimedOut, Cancelled, Failed. To learn more about these events, see Monitoring Systems Manager status changes using Amazon SNS notifications in the AWS Systems Manager User Guide .\n\n(string) --\n\n\nNotificationType (string) --Command: Receive notification when the status of a command changes. Invocation: For commands sent to multiple instances, receive notification on a per-instance basis when the status of a command changes.\n\n\n\nOutputS3BucketName (string) --The name of the S3 bucket.\n\nOutputS3KeyPrefix (string) --The S3 bucket subfolder.\n\nParameters (dict) --The parameters for the RUN_COMMAND task execution.\n\n(string) --\n(list) --\n(string) --\n\n\n\n\n\n\nServiceRoleArn (string) --The ARN of the IAM service role to use to publish Amazon Simple Notification Service (Amazon SNS) notifications for maintenance window Run Command tasks.\n\nTimeoutSeconds (integer) --If this time is reached and the command has not already started running, it doesn\'t run.\n\n\n\nAutomation (dict) --The parameters for an AUTOMATION task type.\n\nDocumentVersion (string) --The version of an Automation document to use during task execution.\n\nParameters (dict) --The parameters for the AUTOMATION task.\nFor information about specifying and updating task parameters, see RegisterTaskWithMaintenanceWindow and UpdateMaintenanceWindowTask .\n\nNote\n\nLoggingInfo has been deprecated. To specify an S3 bucket to contain logs, instead use the OutputS3BucketName and OutputS3KeyPrefix options in the TaskInvocationParameters structure. For information about how Systems Manager handles these options for the supported maintenance window task types, see MaintenanceWindowTaskInvocationParameters .TaskParameters has been deprecated. To specify parameters to pass to a task when it runs, instead use the Parameters option in the TaskInvocationParameters structure. For information about how Systems Manager handles these options for the supported maintenance window task types, see MaintenanceWindowTaskInvocationParameters .\n\nFor AUTOMATION task types, Systems Manager ignores any values specified for these parameters.\n\n\n(string) --\n(list) --\n(string) --\n\n\n\n\n\n\n\n\nStepFunctions (dict) --The parameters for a STEP_FUNCTIONS task type.\n\nInput (string) --The inputs for the STEP_FUNCTIONS task.\n\nName (string) --The name of the STEP_FUNCTIONS task.\n\n\n\nLambda (dict) --The parameters for a LAMBDA task type.\n\nClientContext (string) --Pass client-specific information to the Lambda function that you are invoking. You can then process the client information in your Lambda function as you choose through the context variable.\n\nQualifier (string) --(Optional) Specify a Lambda function version or alias name. If you specify a function version, the action uses the qualified function ARN to invoke a specific Lambda function. If you specify an alias name, the action uses the alias ARN to invoke the Lambda function version to which the alias points.\n\nPayload (bytes) --JSON to provide to your Lambda function as input.\n\n\n\n\n

    :type Priority: integer
    :param Priority: The new task priority to specify. The lower the number, the higher the priority. Tasks that have the same priority are scheduled in parallel.

    :type MaxConcurrency: string
    :param MaxConcurrency: The new MaxConcurrency value you want to specify. MaxConcurrency is the number of targets that are allowed to run this task in parallel.

    :type MaxErrors: string
    :param MaxErrors: The new MaxErrors value to specify. MaxErrors is the maximum number of errors that are allowed before the task stops being scheduled.

    :type LoggingInfo: dict
    :param LoggingInfo: The new logging location in Amazon S3 to specify.\n\nNote\nLoggingInfo has been deprecated. To specify an S3 bucket to contain logs, instead use the OutputS3BucketName and OutputS3KeyPrefix options in the TaskInvocationParameters structure. For information about how Systems Manager handles these options for the supported maintenance window task types, see MaintenanceWindowTaskInvocationParameters .\n\n\nS3BucketName (string) -- [REQUIRED]The name of an S3 bucket where execution logs are stored .\n\nS3KeyPrefix (string) --(Optional) The S3 bucket subfolder.\n\nS3Region (string) -- [REQUIRED]The Region where the S3 bucket is located.\n\n\n

    :type Name: string
    :param Name: The new task name to specify.

    :type Description: string
    :param Description: The new task description to specify.

    :type Replace: boolean
    :param Replace: If True, then all fields that are required by the RegisterTaskWithMaintenanceWndow action are also required for this API request. Optional fields that are not specified are set to null.

    :rtype: dict

ReturnsResponse Syntax
{
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
            'CloudWatchOutputConfig': {
                'CloudWatchLogGroupName': 'string',
                'CloudWatchOutputEnabled': True|False
            },
            'DocumentHash': 'string',
            'DocumentHashType': 'Sha256'|'Sha1',
            'DocumentVersion': 'string',
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


Response Structure

(dict) --

WindowId (string) --
The ID of the maintenance window that was updated.

WindowTaskId (string) --
The task ID of the maintenance window that was updated.

Targets (list) --
The updated target values.

(dict) --
An array of search criteria that targets instances using a Key,Value combination that you specify.
Supported formats include the following.

``Key=InstanceIds,Values=*instance-id-1* ,*instance-id-2* ,*instance-id-3* ``
``Key=tag:my-tag-key ,Values=*my-tag-value-1* ,*my-tag-value-2* ``
``Key=tag-key,Values=*my-tag-key-1* ,*my-tag-key-2* ``
(Maintenance window targets only) ``Key=resource-groups:Name,Values=*resource-group-name* ``
(Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*resource-type-1* ,*resource-type-2* ``

For example:

Key=InstanceIds,Values=i-02573cafcfEXAMPLE,i-0471e04240EXAMPLE,i-07782c72faEXAMPLE
Key=tag:CostCenter,Values=CostCenter1,CostCenter2,CostCenter3
Key=tag-key,Values=Name,Instance-Type,CostCenter
(Maintenance window targets only) Key=resource-groups:Name,Values=ProductionResourceGroup   This example demonstrates how to target all resources in the resource group ProductionResourceGroup in your maintenance window.
(Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*AWS::EC2::INSTANCE* ,*AWS::EC2::VPC* ``   This example demonstrates how to target only EC2 instances and VPCs in your maintenance window.
(State Manager association targets only) Key=InstanceIds,Values=*   This example demonstrates how to target all managed instances in the AWS Region where the association was created.

For information about how to send commands that target instances using Key,Value parameters, see Targeting multiple instances in the AWS Systems Manager User Guide .

Key (string) --
User-defined criteria for sending commands that target instances that meet the criteria.

Values (list) --
User-defined criteria that maps to Key . For example, if you specified tag:ServerRole , you could specify value:WebServer to run a command on instances that include EC2 tags of ServerRole,WebServer .

(string) --






TaskArn (string) --
The updated task ARN value.

ServiceRoleArn (string) --
The ARN of the IAM service role to use to publish Amazon Simple Notification Service (Amazon SNS) notifications for maintenance window Run Command tasks.

TaskParameters (dict) --
The updated parameter values.

Note
TaskParameters has been deprecated. To specify parameters to pass to a task when it runs, instead use the Parameters option in the TaskInvocationParameters structure. For information about how Systems Manager handles these options for the supported maintenance window task types, see  MaintenanceWindowTaskInvocationParameters .


(string) --

(dict) --
Defines the values for a task parameter.

Values (list) --
This field contains an array of 0 or more strings, each 1 to 255 characters in length.

(string) --








TaskInvocationParameters (dict) --
The updated parameter values.

RunCommand (dict) --
The parameters for a RUN_COMMAND task type.

Comment (string) --
Information about the commands to run.

CloudWatchOutputConfig (dict) --
Configuration options for sending command output to CloudWatch Logs.

CloudWatchLogGroupName (string) --
The name of the CloudWatch log group where you want to send command output. If you don\'t specify a group name, Systems Manager automatically creates a log group for you. The log group uses the following naming format: aws/ssm/SystemsManagerDocumentName .

CloudWatchOutputEnabled (boolean) --
Enables Systems Manager to send command output to CloudWatch Logs.



DocumentHash (string) --
The SHA-256 or SHA-1 hash created by the system when the document was created. SHA-1 hashes have been deprecated.

DocumentHashType (string) --
SHA-256 or SHA-1. SHA-1 hashes have been deprecated.

DocumentVersion (string) --
The SSM document version to use in the request. You can specify $DEFAULT, $LATEST, or a specific version number. If you run commands by using the AWS CLI, then you must escape the first two options by using a backslash. If you specify a version number, then you don\'t need to use the backslash. For example:
--document-version "$DEFAULT"
--document-version "$LATEST"
--document-version "3"

NotificationConfig (dict) --
Configurations for sending notifications about command status changes on a per-instance basis.

NotificationArn (string) --
An Amazon Resource Name (ARN) for an Amazon Simple Notification Service (Amazon SNS) topic. Run Command pushes notifications about command status changes to this topic.

NotificationEvents (list) --
The different events for which you can receive notifications. These events include the following: All (events), InProgress, Success, TimedOut, Cancelled, Failed. To learn more about these events, see Monitoring Systems Manager status changes using Amazon SNS notifications in the AWS Systems Manager User Guide .

(string) --


NotificationType (string) --
Command: Receive notification when the status of a command changes. Invocation: For commands sent to multiple instances, receive notification on a per-instance basis when the status of a command changes.



OutputS3BucketName (string) --
The name of the S3 bucket.

OutputS3KeyPrefix (string) --
The S3 bucket subfolder.

Parameters (dict) --
The parameters for the RUN_COMMAND task execution.

(string) --
(list) --
(string) --






ServiceRoleArn (string) --
The ARN of the IAM service role to use to publish Amazon Simple Notification Service (Amazon SNS) notifications for maintenance window Run Command tasks.

TimeoutSeconds (integer) --
If this time is reached and the command has not already started running, it doesn\'t run.



Automation (dict) --
The parameters for an AUTOMATION task type.

DocumentVersion (string) --
The version of an Automation document to use during task execution.

Parameters (dict) --
The parameters for the AUTOMATION task.
For information about specifying and updating task parameters, see  RegisterTaskWithMaintenanceWindow and  UpdateMaintenanceWindowTask .

Note

LoggingInfo has been deprecated. To specify an S3 bucket to contain logs, instead use the OutputS3BucketName and OutputS3KeyPrefix options in the TaskInvocationParameters structure. For information about how Systems Manager handles these options for the supported maintenance window task types, see  MaintenanceWindowTaskInvocationParameters .
TaskParameters has been deprecated. To specify parameters to pass to a task when it runs, instead use the Parameters option in the TaskInvocationParameters structure. For information about how Systems Manager handles these options for the supported maintenance window task types, see  MaintenanceWindowTaskInvocationParameters .

For AUTOMATION task types, Systems Manager ignores any values specified for these parameters.


(string) --
(list) --
(string) --








StepFunctions (dict) --
The parameters for a STEP_FUNCTIONS task type.

Input (string) --
The inputs for the STEP_FUNCTIONS task.

Name (string) --
The name of the STEP_FUNCTIONS task.



Lambda (dict) --
The parameters for a LAMBDA task type.

ClientContext (string) --
Pass client-specific information to the Lambda function that you are invoking. You can then process the client information in your Lambda function as you choose through the context variable.

Qualifier (string) --
(Optional) Specify a Lambda function version or alias name. If you specify a function version, the action uses the qualified function ARN to invoke a specific Lambda function. If you specify an alias name, the action uses the alias ARN to invoke the Lambda function version to which the alias points.

Payload (bytes) --
JSON to provide to your Lambda function as input.





Priority (integer) --
The updated priority value.

MaxConcurrency (string) --
The updated MaxConcurrency value.

MaxErrors (string) --
The updated MaxErrors value.

LoggingInfo (dict) --
The updated logging information in Amazon S3.

Note
LoggingInfo has been deprecated. To specify an S3 bucket to contain logs, instead use the OutputS3BucketName and OutputS3KeyPrefix options in the TaskInvocationParameters structure. For information about how Systems Manager handles these options for the supported maintenance window task types, see  MaintenanceWindowTaskInvocationParameters .


S3BucketName (string) --
The name of an S3 bucket where execution logs are stored .

S3KeyPrefix (string) --
(Optional) The S3 bucket subfolder.

S3Region (string) --
The Region where the S3 bucket is located.



Name (string) --
The updated task name.

Description (string) --
The updated task description.







Exceptions

SSM.Client.exceptions.DoesNotExistException
SSM.Client.exceptions.InternalServerError


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
                'CloudWatchOutputConfig': {
                    'CloudWatchLogGroupName': 'string',
                    'CloudWatchOutputEnabled': True|False
                },
                'DocumentHash': 'string',
                'DocumentHashType': 'Sha256'|'Sha1',
                'DocumentVersion': 'string',
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
    WindowId (string) -- [REQUIRED]
    The maintenance window ID that contains the task to modify.
    
    WindowTaskId (string) -- [REQUIRED]
    The task ID to modify.
    
    Targets (list) -- The targets (either instances or tags) to modify. Instances are specified using Key=instanceids,Values=instanceID_1,instanceID_2. Tags are specified using Key=tag_name,Values=tag_value.
    
    (dict) --An array of search criteria that targets instances using a Key,Value combination that you specify.
    Supported formats include the following.
    
    ``Key=InstanceIds,Values=*instance-id-1* ,*instance-id-2* ,*instance-id-3* ``
    ``Key=tag:my-tag-key ,Values=*my-tag-value-1* ,*my-tag-value-2* ``
    ``Key=tag-key,Values=*my-tag-key-1* ,*my-tag-key-2* ``
    (Maintenance window targets only) ``Key=resource-groups:Name,Values=*resource-group-name* ``
    (Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*resource-type-1* ,*resource-type-2* ``
    
    For example:
    
    Key=InstanceIds,Values=i-02573cafcfEXAMPLE,i-0471e04240EXAMPLE,i-07782c72faEXAMPLE
    Key=tag:CostCenter,Values=CostCenter1,CostCenter2,CostCenter3
    Key=tag-key,Values=Name,Instance-Type,CostCenter
    (Maintenance window targets only) Key=resource-groups:Name,Values=ProductionResourceGroup   This example demonstrates how to target all resources in the resource group ProductionResourceGroup in your maintenance window.
    (Maintenance window targets only) ``Key=resource-groups:ResourceTypeFilters,Values=*AWS::EC2::INSTANCE* ,*AWS::EC2::VPC* ``   This example demonstrates how to target only EC2 instances and VPCs in your maintenance window.
    (State Manager association targets only) Key=InstanceIds,Values=*   This example demonstrates how to target all managed instances in the AWS Region where the association was created.
    
    For information about how to send commands that target instances using Key,Value parameters, see Targeting multiple instances in the AWS Systems Manager User Guide .
    
    Key (string) --User-defined criteria for sending commands that target instances that meet the criteria.
    
    Values (list) --User-defined criteria that maps to Key . For example, if you specified tag:ServerRole , you could specify value:WebServer to run a command on instances that include EC2 tags of ServerRole,WebServer .
    
    (string) --
    
    
    
    
    
    
    TaskArn (string) -- The task ARN to modify.
    ServiceRoleArn (string) -- The ARN of the IAM service role for Systems Manager to assume when running a maintenance window task. If you do not specify a service role ARN, Systems Manager uses your account\'s service-linked role. If no service-linked role for Systems Manager exists in your account, it is created when you run RegisterTaskWithMaintenanceWindow .
    For more information, see the following topics in the in the AWS Systems Manager User Guide :
    
    Using service-linked roles for Systems Manager
    Should I use a service-linked role or a custom service role to run maintenance window tasks?
    
    
    TaskParameters (dict) -- The parameters to modify.
    
    Note
    TaskParameters has been deprecated. To specify parameters to pass to a task when it runs, instead use the Parameters option in the TaskInvocationParameters structure. For information about how Systems Manager handles these options for the supported maintenance window task types, see  MaintenanceWindowTaskInvocationParameters .
    
    The map has the following format:
    Key: string, between 1 and 255 characters
    Value: an array of strings, each string is between 1 and 255 characters
    
    (string) --
    (dict) --Defines the values for a task parameter.
    
    Values (list) --This field contains an array of 0 or more strings, each 1 to 255 characters in length.
    
    (string) --
    
    
    
    
    
    
    
    
    TaskInvocationParameters (dict) -- The parameters that the task should use during execution. Populate only the fields that match the task type. All other fields should be empty.
    
    RunCommand (dict) --The parameters for a RUN_COMMAND task type.
    
    Comment (string) --Information about the commands to run.
    
    CloudWatchOutputConfig (dict) --Configuration options for sending command output to CloudWatch Logs.
    
    CloudWatchLogGroupName (string) --The name of the CloudWatch log group where you want to send command output. If you don\'t specify a group name, Systems Manager automatically creates a log group for you. The log group uses the following naming format: aws/ssm/SystemsManagerDocumentName .
    
    CloudWatchOutputEnabled (boolean) --Enables Systems Manager to send command output to CloudWatch Logs.
    
    
    
    DocumentHash (string) --The SHA-256 or SHA-1 hash created by the system when the document was created. SHA-1 hashes have been deprecated.
    
    DocumentHashType (string) --SHA-256 or SHA-1. SHA-1 hashes have been deprecated.
    
    DocumentVersion (string) --The SSM document version to use in the request. You can specify $DEFAULT, $LATEST, or a specific version number. If you run commands by using the AWS CLI, then you must escape the first two options by using a backslash. If you specify a version number, then you don\'t need to use the backslash. For example:
    --document-version "$DEFAULT"
    --document-version "$LATEST"
    --document-version "3"
    
    NotificationConfig (dict) --Configurations for sending notifications about command status changes on a per-instance basis.
    
    NotificationArn (string) --An Amazon Resource Name (ARN) for an Amazon Simple Notification Service (Amazon SNS) topic. Run Command pushes notifications about command status changes to this topic.
    
    NotificationEvents (list) --The different events for which you can receive notifications. These events include the following: All (events), InProgress, Success, TimedOut, Cancelled, Failed. To learn more about these events, see Monitoring Systems Manager status changes using Amazon SNS notifications in the AWS Systems Manager User Guide .
    
    (string) --
    
    
    NotificationType (string) --Command: Receive notification when the status of a command changes. Invocation: For commands sent to multiple instances, receive notification on a per-instance basis when the status of a command changes.
    
    
    
    OutputS3BucketName (string) --The name of the S3 bucket.
    
    OutputS3KeyPrefix (string) --The S3 bucket subfolder.
    
    Parameters (dict) --The parameters for the RUN_COMMAND task execution.
    
    (string) --
    (list) --
    (string) --
    
    
    
    
    
    
    ServiceRoleArn (string) --The ARN of the IAM service role to use to publish Amazon Simple Notification Service (Amazon SNS) notifications for maintenance window Run Command tasks.
    
    TimeoutSeconds (integer) --If this time is reached and the command has not already started running, it doesn\'t run.
    
    
    
    Automation (dict) --The parameters for an AUTOMATION task type.
    
    DocumentVersion (string) --The version of an Automation document to use during task execution.
    
    Parameters (dict) --The parameters for the AUTOMATION task.
    For information about specifying and updating task parameters, see  RegisterTaskWithMaintenanceWindow and  UpdateMaintenanceWindowTask .
    
    Note
    
    LoggingInfo has been deprecated. To specify an S3 bucket to contain logs, instead use the OutputS3BucketName and OutputS3KeyPrefix options in the TaskInvocationParameters structure. For information about how Systems Manager handles these options for the supported maintenance window task types, see  MaintenanceWindowTaskInvocationParameters .TaskParameters has been deprecated. To specify parameters to pass to a task when it runs, instead use the Parameters option in the TaskInvocationParameters structure. For information about how Systems Manager handles these options for the supported maintenance window task types, see  MaintenanceWindowTaskInvocationParameters .
    
    For AUTOMATION task types, Systems Manager ignores any values specified for these parameters.
    
    
    (string) --
    (list) --
    (string) --
    
    
    
    
    
    
    
    
    StepFunctions (dict) --The parameters for a STEP_FUNCTIONS task type.
    
    Input (string) --The inputs for the STEP_FUNCTIONS task.
    
    Name (string) --The name of the STEP_FUNCTIONS task.
    
    
    
    Lambda (dict) --The parameters for a LAMBDA task type.
    
    ClientContext (string) --Pass client-specific information to the Lambda function that you are invoking. You can then process the client information in your Lambda function as you choose through the context variable.
    
    Qualifier (string) --(Optional) Specify a Lambda function version or alias name. If you specify a function version, the action uses the qualified function ARN to invoke a specific Lambda function. If you specify an alias name, the action uses the alias ARN to invoke the Lambda function version to which the alias points.
    
    Payload (bytes) --JSON to provide to your Lambda function as input.
    
    
    
    
    
    Priority (integer) -- The new task priority to specify. The lower the number, the higher the priority. Tasks that have the same priority are scheduled in parallel.
    MaxConcurrency (string) -- The new MaxConcurrency value you want to specify. MaxConcurrency is the number of targets that are allowed to run this task in parallel.
    MaxErrors (string) -- The new MaxErrors value to specify. MaxErrors is the maximum number of errors that are allowed before the task stops being scheduled.
    LoggingInfo (dict) -- The new logging location in Amazon S3 to specify.
    
    Note
    LoggingInfo has been deprecated. To specify an S3 bucket to contain logs, instead use the OutputS3BucketName and OutputS3KeyPrefix options in the TaskInvocationParameters structure. For information about how Systems Manager handles these options for the supported maintenance window task types, see  MaintenanceWindowTaskInvocationParameters .
    
    
    S3BucketName (string) -- [REQUIRED]The name of an S3 bucket where execution logs are stored .
    
    S3KeyPrefix (string) --(Optional) The S3 bucket subfolder.
    
    S3Region (string) -- [REQUIRED]The Region where the S3 bucket is located.
    
    
    
    Name (string) -- The new task name to specify.
    Description (string) -- The new task description to specify.
    Replace (boolean) -- If True, then all fields that are required by the RegisterTaskWithMaintenanceWndow action are also required for this API request. Optional fields that are not specified are set to null.
    
    """
    pass

def update_managed_instance_role(InstanceId=None, IamRole=None):
    """
    Changes the Amazon Identity and Access Management (IAM) role that is assigned to the on-premises instance or virtual machines (VM). IAM roles are first assigned to these hybrid instances during the activation process. For more information, see  CreateActivation .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_managed_instance_role(
        InstanceId='string',
        IamRole='string'
    )
    
    
    :type InstanceId: string
    :param InstanceId: [REQUIRED]\nThe ID of the managed instance where you want to update the role.\n

    :type IamRole: string
    :param IamRole: [REQUIRED]\nThe IAM role you want to assign or change.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

SSM.Client.exceptions.InvalidInstanceId
SSM.Client.exceptions.InternalServerError


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_ops_item(Description=None, OperationalData=None, OperationalDataToDelete=None, Notifications=None, Priority=None, RelatedOpsItems=None, Status=None, OpsItemId=None, Title=None, Category=None, Severity=None):
    """
    Edit or change an OpsItem. You must have permission in AWS Identity and Access Management (IAM) to update an OpsItem. For more information, see Getting started with OpsCenter in the AWS Systems Manager User Guide .
    Operations engineers and IT professionals use OpsCenter to view, investigate, and remediate operational issues impacting the performance and health of their AWS resources. For more information, see AWS Systems Manager OpsCenter in the AWS Systems Manager User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_ops_item(
        Description='string',
        OperationalData={
            'string': {
                'Value': 'string',
                'Type': 'SearchableString'|'String'
            }
        },
        OperationalDataToDelete=[
            'string',
        ],
        Notifications=[
            {
                'Arn': 'string'
            },
        ],
        Priority=123,
        RelatedOpsItems=[
            {
                'OpsItemId': 'string'
            },
        ],
        Status='Open'|'InProgress'|'Resolved',
        OpsItemId='string',
        Title='string',
        Category='string',
        Severity='string'
    )
    
    
    :type Description: string
    :param Description: Update the information about the OpsItem. Provide enough information so that users reading this OpsItem for the first time understand the issue.

    :type OperationalData: dict
    :param OperationalData: Add new keys or edit existing key-value pairs of the OperationalData map in the OpsItem object.\nOperational data is custom data that provides useful reference details about the OpsItem. For example, you can specify log files, error strings, license keys, troubleshooting tips, or other relevant data. You enter operational data as key-value pairs. The key has a maximum length of 128 characters. The value has a maximum size of 20 KB.\n\nWarning\nOperational data keys can\'t begin with the following: amazon, aws, amzn, ssm, /amazon, /aws, /amzn, /ssm.\n\nYou can choose to make the data searchable by other users in the account or you can restrict search access. Searchable data means that all users with access to the OpsItem Overview page (as provided by the DescribeOpsItems API action) can view and search on the specified data. Operational data that is not searchable is only viewable by users who have access to the OpsItem (as provided by the GetOpsItem API action).\nUse the /aws/resources key in OperationalData to specify a related resource in the request. Use the /aws/automations key in OperationalData to associate an Automation runbook with the OpsItem. To view AWS CLI example commands that use these keys, see Creating OpsItems manually in the AWS Systems Manager User Guide .\n\n(string) --\n(dict) --An object that defines the value of the key and its type in the OperationalData map.\n\nValue (string) --The value of the OperationalData key.\n\nType (string) --The type of key-value pair. Valid types include SearchableString and String .\n\n\n\n\n\n\n

    :type OperationalDataToDelete: list
    :param OperationalDataToDelete: Keys that you want to remove from the OperationalData map.\n\n(string) --\n\n

    :type Notifications: list
    :param Notifications: The Amazon Resource Name (ARN) of an SNS topic where notifications are sent when this OpsItem is edited or changed.\n\n(dict) --A notification about the OpsItem.\n\nArn (string) --The Amazon Resource Name (ARN) of an SNS topic where notifications are sent when this OpsItem is edited or changed.\n\n\n\n\n

    :type Priority: integer
    :param Priority: The importance of this OpsItem in relation to other OpsItems in the system.

    :type RelatedOpsItems: list
    :param RelatedOpsItems: One or more OpsItems that share something in common with the current OpsItems. For example, related OpsItems can include OpsItems with similar error messages, impacted resources, or statuses for the impacted resource.\n\n(dict) --An OpsItems that shares something in common with the current OpsItem. For example, related OpsItems can include OpsItems with similar error messages, impacted resources, or statuses for the impacted resource.\n\nOpsItemId (string) -- [REQUIRED]The ID of an OpsItem related to the current OpsItem.\n\n\n\n\n

    :type Status: string
    :param Status: The OpsItem status. Status can be Open , In Progress , or Resolved . For more information, see Editing OpsItem details in the AWS Systems Manager User Guide .

    :type OpsItemId: string
    :param OpsItemId: [REQUIRED]\nThe ID of the OpsItem.\n

    :type Title: string
    :param Title: A short heading that describes the nature of the OpsItem and the impacted resource.

    :type Category: string
    :param Category: Specify a new category for an OpsItem.

    :type Severity: string
    :param Severity: Specify a new severity for an OpsItem.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.OpsItemNotFoundException
SSM.Client.exceptions.OpsItemAlreadyExistsException
SSM.Client.exceptions.OpsItemLimitExceededException
SSM.Client.exceptions.OpsItemInvalidParameterException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_patch_baseline(BaselineId=None, Name=None, GlobalFilters=None, ApprovalRules=None, ApprovedPatches=None, ApprovedPatchesComplianceLevel=None, ApprovedPatchesEnableNonSecurity=None, RejectedPatches=None, RejectedPatchesAction=None, Description=None, Sources=None, Replace=None):
    """
    Modifies an existing patch baseline. Fields not specified in the request are left unchanged.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_patch_baseline(
        BaselineId='string',
        Name='string',
        GlobalFilters={
            'PatchFilters': [
                {
                    'Key': 'PATCH_SET'|'PRODUCT'|'PRODUCT_FAMILY'|'CLASSIFICATION'|'MSRC_SEVERITY'|'PATCH_ID'|'SECTION'|'PRIORITY'|'SEVERITY',
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
                                'Key': 'PATCH_SET'|'PRODUCT'|'PRODUCT_FAMILY'|'CLASSIFICATION'|'MSRC_SEVERITY'|'PATCH_ID'|'SECTION'|'PRIORITY'|'SEVERITY',
                                'Values': [
                                    'string',
                                ]
                            },
                        ]
                    },
                    'ComplianceLevel': 'CRITICAL'|'HIGH'|'MEDIUM'|'LOW'|'INFORMATIONAL'|'UNSPECIFIED',
                    'ApproveAfterDays': 123,
                    'ApproveUntilDate': 'string',
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
        RejectedPatchesAction='ALLOW_AS_DEPENDENCY'|'BLOCK',
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
    :param BaselineId: [REQUIRED]\nThe ID of the patch baseline to update.\n

    :type Name: string
    :param Name: The name of the patch baseline.

    :type GlobalFilters: dict
    :param GlobalFilters: A set of global filters used to include patches in the baseline.\n\nPatchFilters (list) -- [REQUIRED]The set of patch filters that make up the group.\n\n(dict) --Defines which patches should be included in a patch baseline.\nA patch filter consists of a key and a set of values. The filter key is a patch property. For example, the available filter keys for WINDOWS are PATCH_SET, PRODUCT, PRODUCT_FAMILY, CLASSIFICATION, and MSRC_SEVERITY. The filter values define a matching criterion for the patch property indicated by the key. For example, if the filter key is PRODUCT and the filter values are ['Office 2013', 'Office 2016'], then the filter accepts all patches where product name is either 'Office 2013' or 'Office 2016'. The filter values can be exact values for the patch property given as a key, or a wildcard (*), which matches all values.\nYou can view lists of valid values for the patch properties by running the DescribePatchProperties command. For information about which patch properties can be used with each major operating system, see DescribePatchProperties .\n\nKey (string) -- [REQUIRED]The key for the filter.\nRun the DescribePatchProperties command to view lists of valid keys for each operating system type.\n\nValues (list) -- [REQUIRED]The value for the filter key.\nRun the DescribePatchProperties command to view lists of valid values for each key based on operating system type.\n\n(string) --\n\n\n\n\n\n\n\n

    :type ApprovalRules: dict
    :param ApprovalRules: A set of rules used to include patches in the baseline.\n\nPatchRules (list) -- [REQUIRED]The rules that make up the rule group.\n\n(dict) --Defines an approval rule for a patch baseline.\n\nPatchFilterGroup (dict) -- [REQUIRED]The patch filter group that defines the criteria for the rule.\n\nPatchFilters (list) -- [REQUIRED]The set of patch filters that make up the group.\n\n(dict) --Defines which patches should be included in a patch baseline.\nA patch filter consists of a key and a set of values. The filter key is a patch property. For example, the available filter keys for WINDOWS are PATCH_SET, PRODUCT, PRODUCT_FAMILY, CLASSIFICATION, and MSRC_SEVERITY. The filter values define a matching criterion for the patch property indicated by the key. For example, if the filter key is PRODUCT and the filter values are ['Office 2013', 'Office 2016'], then the filter accepts all patches where product name is either 'Office 2013' or 'Office 2016'. The filter values can be exact values for the patch property given as a key, or a wildcard (*), which matches all values.\nYou can view lists of valid values for the patch properties by running the DescribePatchProperties command. For information about which patch properties can be used with each major operating system, see DescribePatchProperties .\n\nKey (string) -- [REQUIRED]The key for the filter.\nRun the DescribePatchProperties command to view lists of valid keys for each operating system type.\n\nValues (list) -- [REQUIRED]The value for the filter key.\nRun the DescribePatchProperties command to view lists of valid values for each key based on operating system type.\n\n(string) --\n\n\n\n\n\n\n\n\nComplianceLevel (string) --A compliance severity level for all approved patches in a patch baseline.\n\nApproveAfterDays (integer) --The number of days after the release date of each patch matched by the rule that the patch is marked as approved in the patch baseline. For example, a value of 7 means that patches are approved seven days after they are released. Not supported on Ubuntu Server.\n\nApproveUntilDate (string) --The cutoff date for auto approval of released patches. Any patches released on or before this date are installed automatically. Not supported on Ubuntu Server.\nEnter dates in the format YYYY-MM-DD . For example, 2020-12-31 .\n\nEnableNonSecurity (boolean) --For instances identified by the approval rule filters, enables a patch baseline to apply non-security updates available in the specified repository. The default value is \'false\'. Applies to Linux instances only.\n\n\n\n\n\n\n

    :type ApprovedPatches: list
    :param ApprovedPatches: A list of explicitly approved patches for the baseline.\nFor information about accepted formats for lists of approved patches and rejected patches, see About package name formats for approved and rejected patch lists in the AWS Systems Manager User Guide .\n\n(string) --\n\n

    :type ApprovedPatchesComplianceLevel: string
    :param ApprovedPatchesComplianceLevel: Assigns a new compliance severity level to an existing patch baseline.

    :type ApprovedPatchesEnableNonSecurity: boolean
    :param ApprovedPatchesEnableNonSecurity: Indicates whether the list of approved patches includes non-security updates that should be applied to the instances. The default value is \'false\'. Applies to Linux instances only.

    :type RejectedPatches: list
    :param RejectedPatches: A list of explicitly rejected patches for the baseline.\nFor information about accepted formats for lists of approved patches and rejected patches, see About package name formats for approved and rejected patch lists in the AWS Systems Manager User Guide .\n\n(string) --\n\n

    :type RejectedPatchesAction: string
    :param RejectedPatchesAction: The action for Patch Manager to take on patches included in the RejectedPackages list.\n\nALLOW_AS_DEPENDENCY : A package in the Rejected patches list is installed only if it is a dependency of another package. It is considered compliant with the patch baseline, and its status is reported as InstalledOther . This is the default action if no option is specified.\nBLOCK : Packages in the RejectedPatches list, and packages that include them as dependencies, are not installed under any circumstances. If a package was installed before it was added to the Rejected patches list, it is considered non-compliant with the patch baseline, and its status is reported as InstalledRejected .\n\n

    :type Description: string
    :param Description: A description of the patch baseline.

    :type Sources: list
    :param Sources: Information about the patches to use to update the instances, including target operating systems and source repositories. Applies to Linux instances only.\n\n(dict) --Information about the patches to use to update the instances, including target operating systems and source repository. Applies to Linux instances only.\n\nName (string) -- [REQUIRED]The name specified to identify the patch source.\n\nProducts (list) -- [REQUIRED]The specific operating system versions a patch repository applies to, such as 'Ubuntu16.04', 'AmazonLinux2016.09', 'RedhatEnterpriseLinux7.2' or 'Suse12.7'. For lists of supported product values, see PatchFilter .\n\n(string) --\n\n\nConfiguration (string) -- [REQUIRED]The value of the yum repo configuration. For example:\n\n[main]cachedir=/var/cache/yum/$basesearch$releasever\nkeepcache=0\ndebuglevel=2\n\n\n\n\n\n

    :type Replace: boolean
    :param Replace: If True, then all fields that are required by the CreatePatchBaseline action are also required for this API request. Optional fields that are not specified are set to null.

    :rtype: dict

ReturnsResponse Syntax
{
    'BaselineId': 'string',
    'Name': 'string',
    'OperatingSystem': 'WINDOWS'|'AMAZON_LINUX'|'AMAZON_LINUX_2'|'UBUNTU'|'REDHAT_ENTERPRISE_LINUX'|'SUSE'|'CENTOS'|'ORACLE_LINUX'|'DEBIAN',
    'GlobalFilters': {
        'PatchFilters': [
            {
                'Key': 'PATCH_SET'|'PRODUCT'|'PRODUCT_FAMILY'|'CLASSIFICATION'|'MSRC_SEVERITY'|'PATCH_ID'|'SECTION'|'PRIORITY'|'SEVERITY',
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
                            'Key': 'PATCH_SET'|'PRODUCT'|'PRODUCT_FAMILY'|'CLASSIFICATION'|'MSRC_SEVERITY'|'PATCH_ID'|'SECTION'|'PRIORITY'|'SEVERITY',
                            'Values': [
                                'string',
                            ]
                        },
                    ]
                },
                'ComplianceLevel': 'CRITICAL'|'HIGH'|'MEDIUM'|'LOW'|'INFORMATIONAL'|'UNSPECIFIED',
                'ApproveAfterDays': 123,
                'ApproveUntilDate': 'string',
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
    'RejectedPatchesAction': 'ALLOW_AS_DEPENDENCY'|'BLOCK',
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


Response Structure

(dict) --

BaselineId (string) --
The ID of the deleted patch baseline.

Name (string) --
The name of the patch baseline.

OperatingSystem (string) --
The operating system rule used by the updated patch baseline.

GlobalFilters (dict) --
A set of global filters used to exclude patches from the baseline.

PatchFilters (list) --
The set of patch filters that make up the group.

(dict) --
Defines which patches should be included in a patch baseline.
A patch filter consists of a key and a set of values. The filter key is a patch property. For example, the available filter keys for WINDOWS are PATCH_SET, PRODUCT, PRODUCT_FAMILY, CLASSIFICATION, and MSRC_SEVERITY. The filter values define a matching criterion for the patch property indicated by the key. For example, if the filter key is PRODUCT and the filter values are ["Office 2013", "Office 2016"], then the filter accepts all patches where product name is either "Office 2013" or "Office 2016". The filter values can be exact values for the patch property given as a key, or a wildcard (*), which matches all values.
You can view lists of valid values for the patch properties by running the DescribePatchProperties command. For information about which patch properties can be used with each major operating system, see  DescribePatchProperties .

Key (string) --
The key for the filter.
Run the  DescribePatchProperties command to view lists of valid keys for each operating system type.

Values (list) --
The value for the filter key.
Run the  DescribePatchProperties command to view lists of valid values for each key based on operating system type.

(string) --








ApprovalRules (dict) --
A set of rules used to include patches in the baseline.

PatchRules (list) --
The rules that make up the rule group.

(dict) --
Defines an approval rule for a patch baseline.

PatchFilterGroup (dict) --
The patch filter group that defines the criteria for the rule.

PatchFilters (list) --
The set of patch filters that make up the group.

(dict) --
Defines which patches should be included in a patch baseline.
A patch filter consists of a key and a set of values. The filter key is a patch property. For example, the available filter keys for WINDOWS are PATCH_SET, PRODUCT, PRODUCT_FAMILY, CLASSIFICATION, and MSRC_SEVERITY. The filter values define a matching criterion for the patch property indicated by the key. For example, if the filter key is PRODUCT and the filter values are ["Office 2013", "Office 2016"], then the filter accepts all patches where product name is either "Office 2013" or "Office 2016". The filter values can be exact values for the patch property given as a key, or a wildcard (*), which matches all values.
You can view lists of valid values for the patch properties by running the DescribePatchProperties command. For information about which patch properties can be used with each major operating system, see  DescribePatchProperties .

Key (string) --
The key for the filter.
Run the  DescribePatchProperties command to view lists of valid keys for each operating system type.

Values (list) --
The value for the filter key.
Run the  DescribePatchProperties command to view lists of valid values for each key based on operating system type.

(string) --








ComplianceLevel (string) --
A compliance severity level for all approved patches in a patch baseline.

ApproveAfterDays (integer) --
The number of days after the release date of each patch matched by the rule that the patch is marked as approved in the patch baseline. For example, a value of 7 means that patches are approved seven days after they are released. Not supported on Ubuntu Server.

ApproveUntilDate (string) --
The cutoff date for auto approval of released patches. Any patches released on or before this date are installed automatically. Not supported on Ubuntu Server.
Enter dates in the format YYYY-MM-DD . For example, 2020-12-31 .

EnableNonSecurity (boolean) --
For instances identified by the approval rule filters, enables a patch baseline to apply non-security updates available in the specified repository. The default value is \'false\'. Applies to Linux instances only.







ApprovedPatches (list) --
A list of explicitly approved patches for the baseline.

(string) --


ApprovedPatchesComplianceLevel (string) --
The compliance severity level assigned to the patch baseline after the update completed.

ApprovedPatchesEnableNonSecurity (boolean) --
Indicates whether the list of approved patches includes non-security updates that should be applied to the instances. The default value is \'false\'. Applies to Linux instances only.

RejectedPatches (list) --
A list of explicitly rejected patches for the baseline.

(string) --


RejectedPatchesAction (string) --
The action specified to take on patches included in the RejectedPatches list. A patch can be allowed only if it is a dependency of another package, or blocked entirely along with packages that include it as a dependency.

CreatedDate (datetime) --
The date when the patch baseline was created.

ModifiedDate (datetime) --
The date when the patch baseline was last modified.

Description (string) --
A description of the Patch Baseline.

Sources (list) --
Information about the patches to use to update the instances, including target operating systems and source repositories. Applies to Linux instances only.

(dict) --
Information about the patches to use to update the instances, including target operating systems and source repository. Applies to Linux instances only.

Name (string) --
The name specified to identify the patch source.

Products (list) --
The specific operating system versions a patch repository applies to, such as "Ubuntu16.04", "AmazonLinux2016.09", "RedhatEnterpriseLinux7.2" or "Suse12.7". For lists of supported product values, see  PatchFilter .

(string) --


Configuration (string) --
The value of the yum repo configuration. For example:

[main]
cachedir=/var/cache/yum/$basesearch$releasever
keepcache=0
debuglevel=2












Exceptions

SSM.Client.exceptions.DoesNotExistException
SSM.Client.exceptions.InternalServerError


    :return: {
        'BaselineId': 'string',
        'Name': 'string',
        'OperatingSystem': 'WINDOWS'|'AMAZON_LINUX'|'AMAZON_LINUX_2'|'UBUNTU'|'REDHAT_ENTERPRISE_LINUX'|'SUSE'|'CENTOS'|'ORACLE_LINUX'|'DEBIAN',
        'GlobalFilters': {
            'PatchFilters': [
                {
                    'Key': 'PATCH_SET'|'PRODUCT'|'PRODUCT_FAMILY'|'CLASSIFICATION'|'MSRC_SEVERITY'|'PATCH_ID'|'SECTION'|'PRIORITY'|'SEVERITY',
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
                                'Key': 'PATCH_SET'|'PRODUCT'|'PRODUCT_FAMILY'|'CLASSIFICATION'|'MSRC_SEVERITY'|'PATCH_ID'|'SECTION'|'PRIORITY'|'SEVERITY',
                                'Values': [
                                    'string',
                                ]
                            },
                        ]
                    },
                    'ComplianceLevel': 'CRITICAL'|'HIGH'|'MEDIUM'|'LOW'|'INFORMATIONAL'|'UNSPECIFIED',
                    'ApproveAfterDays': 123,
                    'ApproveUntilDate': 'string',
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
        'RejectedPatchesAction': 'ALLOW_AS_DEPENDENCY'|'BLOCK',
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
    (string) --
    
    """
    pass

def update_resource_data_sync(SyncName=None, SyncType=None, SyncSource=None):
    """
    Update a resource data sync. After you create a resource data sync for a Region, you can\'t change the account options for that sync. For example, if you create a sync in the us-east-2 (Ohio) Region and you choose the Include only the current account option, you can\'t edit that sync later and choose the Include all accounts from my AWS Organizations configuration option. Instead, you must delete the first resource data sync, and create a new one.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_resource_data_sync(
        SyncName='string',
        SyncType='string',
        SyncSource={
            'SourceType': 'string',
            'AwsOrganizationsSource': {
                'OrganizationSourceType': 'string',
                'OrganizationalUnits': [
                    {
                        'OrganizationalUnitId': 'string'
                    },
                ]
            },
            'SourceRegions': [
                'string',
            ],
            'IncludeFutureRegions': True|False
        }
    )
    
    
    :type SyncName: string
    :param SyncName: [REQUIRED]\nThe name of the resource data sync you want to update.\n

    :type SyncType: string
    :param SyncType: [REQUIRED]\nThe type of resource data sync. The supported SyncType is SyncFromSource.\n

    :type SyncSource: dict
    :param SyncSource: [REQUIRED]\nSpecify information about the data sources to synchronize.\n\nSourceType (string) -- [REQUIRED]The type of data source for the resource data sync. SourceType is either AwsOrganizations (if an organization is present in AWS Organizations) or singleAccountMultiRegions .\n\nAwsOrganizationsSource (dict) --Information about the AwsOrganizationsSource resource data sync source. A sync source of this type can synchronize data from AWS Organizations.\n\nOrganizationSourceType (string) -- [REQUIRED]If an AWS Organization is present, this is either OrganizationalUnits or EntireOrganization . For OrganizationalUnits , the data is aggregated from a set of organization units. For EntireOrganization , the data is aggregated from the entire AWS Organization.\n\nOrganizationalUnits (list) --The AWS Organizations organization units included in the sync.\n\n(dict) --The AWS Organizations organizational unit data source for the sync.\n\nOrganizationalUnitId (string) --The AWS Organization unit ID data source for the sync.\n\n\n\n\n\n\n\nSourceRegions (list) -- [REQUIRED]The SyncSource AWS Regions included in the resource data sync.\n\n(string) --\n\n\nIncludeFutureRegions (boolean) --Whether to automatically synchronize and aggregate data from new AWS Regions when those Regions come online.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

SSM.Client.exceptions.ResourceDataSyncNotFoundException
SSM.Client.exceptions.ResourceDataSyncInvalidConfigurationException
SSM.Client.exceptions.ResourceDataSyncConflictException
SSM.Client.exceptions.InternalServerError


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_service_setting(SettingId=None, SettingValue=None):
    """
    Services map a SettingId object to a setting value. AWS services teams define the default value for a SettingId . You can\'t create a new SettingId , but you can overwrite the default value if you have the ssm:UpdateServiceSetting permission for the setting. Use the  GetServiceSetting API action to view the current value. Or, use the  ResetServiceSetting to change the value back to the original value defined by the AWS service team.
    Update the service setting for the account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_service_setting(
        SettingId='string',
        SettingValue='string'
    )
    
    
    :type SettingId: string
    :param SettingId: [REQUIRED]\nThe Amazon Resource Name (ARN) of the service setting to reset. For example, arn:aws:ssm:us-east-1:111122223333:servicesetting/ssm/parameter-store/high-throughput-enabled . The setting ID can be one of the following.\n\n/ssm/parameter-store/default-parameter-tier\n/ssm/parameter-store/high-throughput-enabled\n/ssm/managed-instance/activation-tier\n\n

    :type SettingValue: string
    :param SettingValue: [REQUIRED]\nThe new value to specify for the service setting. For the /ssm/parameter-store/default-parameter-tier setting ID, the setting value can be one of the following.\n\nStandard\nAdvanced\nIntelligent-Tiering\n\nFor the /ssm/parameter-store/high-throughput-enabled , and /ssm/managed-instance/activation-tier setting IDs, the setting value can be true or false.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
The result body of the UpdateServiceSetting API action.





Exceptions

SSM.Client.exceptions.InternalServerError
SSM.Client.exceptions.ServiceSettingNotFound
SSM.Client.exceptions.TooManyUpdates


    :return: {}
    
    
    :returns: 
    SSM.Client.exceptions.InternalServerError
    SSM.Client.exceptions.ServiceSettingNotFound
    SSM.Client.exceptions.TooManyUpdates
    
    """
    pass

