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

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def cancel_update_stack(StackName=None, ClientRequestToken=None):
    """
    Cancels an update on the specified stack. If the call completes successfully, the stack rolls back the update and reverts to the previous stack configuration.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.cancel_update_stack(
        StackName='string',
        ClientRequestToken='string'
    )
    
    
    :type StackName: string
    :param StackName: [REQUIRED]\nThe name or the unique stack ID that is associated with the stack.\n

    :type ClientRequestToken: string
    :param ClientRequestToken: A unique identifier for this CancelUpdateStack request. Specify this token if you plan to retry requests so that AWS CloudFormation knows that you\'re not attempting to cancel an update on a stack with the same name. You might retry CancelUpdateStack requests to ensure that AWS CloudFormation successfully received them.

    :returns: 
    CloudFormation.Client.exceptions.TokenAlreadyExistsException
    
    """
    pass

def continue_update_rollback(StackName=None, RoleARN=None, ResourcesToSkip=None, ClientRequestToken=None):
    """
    For a specified stack that is in the UPDATE_ROLLBACK_FAILED state, continues rolling it back to the UPDATE_ROLLBACK_COMPLETE state. Depending on the cause of the failure, you can manually fix the error and continue the rollback. By continuing the rollback, you can return your stack to a working state (the UPDATE_ROLLBACK_COMPLETE state), and then try to update the stack again.
    A stack goes into the UPDATE_ROLLBACK_FAILED state when AWS CloudFormation cannot roll back all changes after a failed stack update. For example, you might have a stack that is rolling back to an old database instance that was deleted outside of AWS CloudFormation. Because AWS CloudFormation doesn\'t know the database was deleted, it assumes that the database instance still exists and attempts to roll back to it, causing the update rollback to fail.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.continue_update_rollback(
        StackName='string',
        RoleARN='string',
        ResourcesToSkip=[
            'string',
        ],
        ClientRequestToken='string'
    )
    
    
    :type StackName: string
    :param StackName: [REQUIRED]\nThe name or the unique ID of the stack that you want to continue rolling back.\n\nNote\nDon\'t specify the name of a nested stack (a stack that was created by using the AWS::CloudFormation::Stack resource). Instead, use this operation on the parent stack (the stack that contains the AWS::CloudFormation::Stack resource).\n\n

    :type RoleARN: string
    :param RoleARN: The Amazon Resource Name (ARN) of an AWS Identity and Access Management (IAM) role that AWS CloudFormation assumes to roll back the stack. AWS CloudFormation uses the role\'s credentials to make calls on your behalf. AWS CloudFormation always uses this role for all future operations on the stack. As long as users have permission to operate on the stack, AWS CloudFormation uses this role even if the users don\'t have permission to pass it. Ensure that the role grants least privilege.\nIf you don\'t specify a value, AWS CloudFormation uses the role that was previously associated with the stack. If no role is available, AWS CloudFormation uses a temporary session that is generated from your user credentials.\n

    :type ResourcesToSkip: list
    :param ResourcesToSkip: A list of the logical IDs of the resources that AWS CloudFormation skips during the continue update rollback operation. You can specify only resources that are in the UPDATE_FAILED state because a rollback failed. You can\'t specify resources that are in the UPDATE_FAILED state for other reasons, for example, because an update was cancelled. To check why a resource update failed, use the DescribeStackResources action, and view the resource status reason.\n\nWarning\nSpecify this property to skip rolling back resources that AWS CloudFormation can\'t successfully roll back. We recommend that you troubleshoot resources before skipping them. AWS CloudFormation sets the status of the specified resources to UPDATE_COMPLETE and continues to roll back the stack. After the rollback is complete, the state of the skipped resources will be inconsistent with the state of the resources in the stack template. Before performing another stack update, you must update the stack or resources to be consistent with each other. If you don\'t, subsequent stack updates might fail, and the stack will become unrecoverable.\n\nSpecify the minimum number of resources required to successfully roll back your stack. For example, a failed resource update might cause dependent resources to fail. In this case, it might not be necessary to skip the dependent resources.\nTo skip resources that are part of nested stacks, use the following format: NestedStackName.ResourceLogicalID . If you want to specify the logical ID of a stack resource (Type: AWS::CloudFormation::Stack ) in the ResourcesToSkip list, then its corresponding embedded stack must be in one of the following states: DELETE_IN_PROGRESS , DELETE_COMPLETE , or DELETE_FAILED .\n\nNote\nDon\'t confuse a child stack\'s name with its corresponding logical ID defined in the parent stack. For an example of a continue update rollback operation with nested stacks, see Using ResourcesToSkip to recover a nested stacks hierarchy .\n\n\n(string) --\n\n

    :type ClientRequestToken: string
    :param ClientRequestToken: A unique identifier for this ContinueUpdateRollback request. Specify this token if you plan to retry requests so that AWS CloudFormation knows that you\'re not attempting to continue the rollback to a stack with the same name. You might retry ContinueUpdateRollback requests to ensure that AWS CloudFormation successfully received them.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
The output for a  ContinueUpdateRollback action.





Exceptions

CloudFormation.Client.exceptions.TokenAlreadyExistsException


    :return: {}
    
    
    :returns: 
    CloudFormation.Client.exceptions.TokenAlreadyExistsException
    
    """
    pass

def create_change_set(StackName=None, TemplateBody=None, TemplateURL=None, UsePreviousTemplate=None, Parameters=None, Capabilities=None, ResourceTypes=None, RoleARN=None, RollbackConfiguration=None, NotificationARNs=None, Tags=None, ChangeSetName=None, ClientToken=None, Description=None, ChangeSetType=None, ResourcesToImport=None):
    """
    Creates a list of changes that will be applied to a stack so that you can review the changes before executing them. You can create a change set for a stack that doesn\'t exist or an existing stack. If you create a change set for a stack that doesn\'t exist, the change set shows all of the resources that AWS CloudFormation will create. If you create a change set for an existing stack, AWS CloudFormation compares the stack\'s information with the information that you submit in the change set and lists the differences. Use change sets to understand which resources AWS CloudFormation will create or change, and how it will change resources in an existing stack, before you create or update a stack.
    To create a change set for a stack that doesn\'t exist, for the ChangeSetType parameter, specify CREATE . To create a change set for an existing stack, specify UPDATE for the ChangeSetType parameter. To create a change set for an import operation, specify IMPORT for the ChangeSetType parameter. After the CreateChangeSet call successfully completes, AWS CloudFormation starts creating the change set. To check the status of the change set or to review it, use the  DescribeChangeSet action.
    When you are satisfied with the changes the change set will make, execute the change set by using the  ExecuteChangeSet action. AWS CloudFormation doesn\'t make changes until you execute the change set.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_change_set(
        StackName='string',
        TemplateBody='string',
        TemplateURL='string',
        UsePreviousTemplate=True|False,
        Parameters=[
            {
                'ParameterKey': 'string',
                'ParameterValue': 'string',
                'UsePreviousValue': True|False,
                'ResolvedValue': 'string'
            },
        ],
        Capabilities=[
            'CAPABILITY_IAM'|'CAPABILITY_NAMED_IAM'|'CAPABILITY_AUTO_EXPAND',
        ],
        ResourceTypes=[
            'string',
        ],
        RoleARN='string',
        RollbackConfiguration={
            'RollbackTriggers': [
                {
                    'Arn': 'string',
                    'Type': 'string'
                },
            ],
            'MonitoringTimeInMinutes': 123
        },
        NotificationARNs=[
            'string',
        ],
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        ChangeSetName='string',
        ClientToken='string',
        Description='string',
        ChangeSetType='CREATE'|'UPDATE'|'IMPORT',
        ResourcesToImport=[
            {
                'ResourceType': 'string',
                'LogicalResourceId': 'string',
                'ResourceIdentifier': {
                    'string': 'string'
                }
            },
        ]
    )
    
    
    :type StackName: string
    :param StackName: [REQUIRED]\nThe name or the unique ID of the stack for which you are creating a change set. AWS CloudFormation generates the change set by comparing this stack\'s information with the information that you submit, such as a modified template or different parameter input values.\n

    :type TemplateBody: string
    :param TemplateBody: A structure that contains the body of the revised template, with a minimum length of 1 byte and a maximum length of 51,200 bytes. AWS CloudFormation generates the change set by comparing this template with the template of the stack that you specified.\nConditional: You must specify only TemplateBody or TemplateURL .\n

    :type TemplateURL: string
    :param TemplateURL: The location of the file that contains the revised template. The URL must point to a template (max size: 460,800 bytes) that is located in an S3 bucket. AWS CloudFormation generates the change set by comparing this template with the stack that you specified.\nConditional: You must specify only TemplateBody or TemplateURL .\n

    :type UsePreviousTemplate: boolean
    :param UsePreviousTemplate: Whether to reuse the template that is associated with the stack to create the change set.

    :type Parameters: list
    :param Parameters: A list of Parameter structures that specify input parameters for the change set. For more information, see the Parameter data type.\n\n(dict) --The Parameter data type.\n\nParameterKey (string) --The key associated with the parameter. If you don\'t specify a key and value for a particular parameter, AWS CloudFormation uses the default value that is specified in your template.\n\nParameterValue (string) --The input value associated with the parameter.\n\nUsePreviousValue (boolean) --During a stack update, use the existing parameter value that the stack is using for a given parameter key. If you specify true , do not specify a parameter value.\n\nResolvedValue (string) --Read-only. The value that corresponds to a Systems Manager parameter key. This field is returned only for ` SSM parameter types <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html#aws-ssm-parameter-types>`__ in the template.\n\n\n\n\n

    :type Capabilities: list
    :param Capabilities: In some cases, you must explicitly acknowledge that your stack template contains certain capabilities in order for AWS CloudFormation to create the stack.\n\nCAPABILITY_IAM and CAPABILITY_NAMED_IAM  Some stack templates might include resources that can affect permissions in your AWS account; for example, by creating new AWS Identity and Access Management (IAM) users. For those stacks, you must explicitly acknowledge this by specifying one of these capabilities. The following IAM resources require you to specify either the CAPABILITY_IAM or CAPABILITY_NAMED_IAM capability.\nIf you have IAM resources, you can specify either capability.\nIf you have IAM resources with custom names, you must specify CAPABILITY_NAMED_IAM .\nIf you don\'t specify either of these capabilities, AWS CloudFormation returns an InsufficientCapabilities error.\n\n\n\nIf your stack template contains these resources, we recommend that you review all permissions associated with them and edit their permissions if necessary.\n\n\nAWS::IAM::AccessKey\nAWS::IAM::Group\nAWS::IAM::InstanceProfile\nAWS::IAM::Policy\nAWS::IAM::Role\nAWS::IAM::User\nAWS::IAM::UserToGroupAddition\n\n\nFor more information, see Acknowledging IAM Resources in AWS CloudFormation Templates .\n\nCAPABILITY_AUTO_EXPAND  Some template contain macros. Macros perform custom processing on templates; this can include simple actions like find-and-replace operations, all the way to extensive transformations of entire templates. Because of this, users typically create a change set from the processed template, so that they can review the changes resulting from the macros before actually creating the stack. If your stack template contains one or more macros, and you choose to create a stack directly from the processed template, without first reviewing the resulting changes in a change set, you must acknowledge this capability. This includes the AWS::Include and AWS::Serverless transforms, which are macros hosted by AWS CloudFormation.\n\n\nNote\n\nThis capacity does not apply to creating change sets, and specifying it when creating change sets has no effect. Also, change sets do not currently support nested stacks. If you want to create a stack from a stack template that contains macros and nested stacks, you must create or update the stack directly from the template using the CreateStack or UpdateStack action, and specifying this capability.\nFor more information on macros, see Using AWS CloudFormation Macros to Perform Custom Processing on Templates .\n\n\n(string) --\n\n

    :type ResourceTypes: list
    :param ResourceTypes: The template resource types that you have permissions to work with if you execute this change set, such as AWS::EC2::Instance , AWS::EC2::* , or Custom::MyCustomInstance .\nIf the list of resource types doesn\'t include a resource type that you\'re updating, the stack update fails. By default, AWS CloudFormation grants permissions to all resource types. AWS Identity and Access Management (IAM) uses this parameter for condition keys in IAM policies for AWS CloudFormation. For more information, see Controlling Access with AWS Identity and Access Management in the AWS CloudFormation User Guide.\n\n(string) --\n\n

    :type RoleARN: string
    :param RoleARN: The Amazon Resource Name (ARN) of an AWS Identity and Access Management (IAM) role that AWS CloudFormation assumes when executing the change set. AWS CloudFormation uses the role\'s credentials to make calls on your behalf. AWS CloudFormation uses this role for all future operations on the stack. As long as users have permission to operate on the stack, AWS CloudFormation uses this role even if the users don\'t have permission to pass it. Ensure that the role grants least privilege.\nIf you don\'t specify a value, AWS CloudFormation uses the role that was previously associated with the stack. If no role is available, AWS CloudFormation uses a temporary session that is generated from your user credentials.\n

    :type RollbackConfiguration: dict
    :param RollbackConfiguration: The rollback triggers for AWS CloudFormation to monitor during stack creation and updating operations, and for the specified monitoring period afterwards.\n\nRollbackTriggers (list) --The triggers to monitor during stack creation or update actions.\nBy default, AWS CloudFormation saves the rollback triggers specified for a stack and applies them to any subsequent update operations for the stack, unless you specify otherwise. If you do specify rollback triggers for this parameter, those triggers replace any list of triggers previously specified for the stack. This means:\n\nTo use the rollback triggers previously specified for this stack, if any, don\'t specify this parameter.\nTo specify new or updated rollback triggers, you must specify all the triggers that you want used for this stack, even triggers you\'ve specifed before (for example, when creating the stack or during a previous stack update). Any triggers that you don\'t include in the updated list of triggers are no longer applied to the stack.\nTo remove all currently specified triggers, specify an empty list for this parameter.\n\nIf a specified trigger is missing, the entire stack operation fails and is rolled back.\n\n(dict) --A rollback trigger AWS CloudFormation monitors during creation and updating of stacks. If any of the alarms you specify goes to ALARM state during the stack operation or within the specified monitoring period afterwards, CloudFormation rolls back the entire stack operation.\n\nArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the rollback trigger.\nIf a specified trigger is missing, the entire stack operation fails and is rolled back.\n\nType (string) -- [REQUIRED]The resource type of the rollback trigger. Currently, AWS::CloudWatch::Alarm is the only supported resource type.\n\n\n\n\n\nMonitoringTimeInMinutes (integer) --The amount of time, in minutes, during which CloudFormation should monitor all the rollback triggers after the stack creation or update operation deploys all necessary resources.\nThe default is 0 minutes.\nIf you specify a monitoring period but do not specify any rollback triggers, CloudFormation still waits the specified period of time before cleaning up old resources after update operations. You can use this monitoring period to perform any manual stack validation desired, and manually cancel the stack creation or update (using CancelUpdateStack , for example) as necessary.\nIf you specify 0 for this parameter, CloudFormation still monitors the specified rollback triggers during stack creation and update operations. Then, for update operations, it begins disposing of old resources immediately once the operation completes.\n\n\n

    :type NotificationARNs: list
    :param NotificationARNs: The Amazon Resource Names (ARNs) of Amazon Simple Notification Service (Amazon SNS) topics that AWS CloudFormation associates with the stack. To remove all associated notification topics, specify an empty list.\n\n(string) --\n\n

    :type Tags: list
    :param Tags: Key-value pairs to associate with this stack. AWS CloudFormation also propagates these tags to resources in the stack. You can specify a maximum of 50 tags.\n\n(dict) --The Tag type enables you to specify a key-value pair that can be used to store information about an AWS CloudFormation stack.\n\nKey (string) -- [REQUIRED]\nRequired . A string used to identify this tag. You can specify a maximum of 128 characters for a tag key. Tags owned by Amazon Web Services (AWS) have the reserved prefix: aws: .\n\nValue (string) -- [REQUIRED]\nRequired . A string containing the value for this tag. You can specify a maximum of 256 characters for a tag value.\n\n\n\n\n

    :type ChangeSetName: string
    :param ChangeSetName: [REQUIRED]\nThe name of the change set. The name must be unique among all change sets that are associated with the specified stack.\nA change set name can contain only alphanumeric, case sensitive characters and hyphens. It must start with an alphabetic character and cannot exceed 128 characters.\n

    :type ClientToken: string
    :param ClientToken: A unique identifier for this CreateChangeSet request. Specify this token if you plan to retry requests so that AWS CloudFormation knows that you\'re not attempting to create another change set with the same name. You might retry CreateChangeSet requests to ensure that AWS CloudFormation successfully received them.

    :type Description: string
    :param Description: A description to help you identify this change set.

    :type ChangeSetType: string
    :param ChangeSetType: The type of change set operation. To create a change set for a new stack, specify CREATE . To create a change set for an existing stack, specify UPDATE . To create a change set for an import operation, specify IMPORT .\nIf you create a change set for a new stack, AWS Cloudformation creates a stack with a unique stack ID, but no template or resources. The stack will be in the ` REVIEW_IN_PROGRESS https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-describing-stacks.html#d0e11995`__ state until you execute the change set.\nBy default, AWS CloudFormation specifies UPDATE . You can\'t use the UPDATE type to create a change set for a new stack or the CREATE type to create a change set for an existing stack.\n

    :type ResourcesToImport: list
    :param ResourcesToImport: The resources to import into your stack.\n\n(dict) --Describes the target resource of an import operation.\n\nResourceType (string) -- [REQUIRED]The type of resource to import into your stack, such as AWS::S3::Bucket .\n\nLogicalResourceId (string) -- [REQUIRED]The logical ID of the target resource as specified in the template.\n\nResourceIdentifier (dict) -- [REQUIRED]A key-value pair that identifies the target resource. The key is an identifier property (for example, BucketName for AWS::S3::Bucket resources) and the value is the actual property value (for example, MyS3Bucket ).\n\n(string) --\n(string) --\n\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Id': 'string',
    'StackId': 'string'
}


Response Structure

(dict) --
The output for the  CreateChangeSet action.

Id (string) --
The Amazon Resource Name (ARN) of the change set.

StackId (string) --
The unique ID of the stack.







Exceptions

CloudFormation.Client.exceptions.AlreadyExistsException
CloudFormation.Client.exceptions.InsufficientCapabilitiesException
CloudFormation.Client.exceptions.LimitExceededException


    :return: {
        'Id': 'string',
        'StackId': 'string'
    }
    
    
    :returns: 
    CloudFormation.Client.exceptions.AlreadyExistsException
    CloudFormation.Client.exceptions.InsufficientCapabilitiesException
    CloudFormation.Client.exceptions.LimitExceededException
    
    """
    pass

def create_stack(StackName=None, TemplateBody=None, TemplateURL=None, Parameters=None, DisableRollback=None, RollbackConfiguration=None, TimeoutInMinutes=None, NotificationARNs=None, Capabilities=None, ResourceTypes=None, RoleARN=None, OnFailure=None, StackPolicyBody=None, StackPolicyURL=None, Tags=None, ClientRequestToken=None, EnableTerminationProtection=None):
    """
    Creates a stack as specified in the template. After the call completes successfully, the stack creation starts. You can check the status of the stack via the  DescribeStacks API.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_stack(
        StackName='string',
        TemplateBody='string',
        TemplateURL='string',
        Parameters=[
            {
                'ParameterKey': 'string',
                'ParameterValue': 'string',
                'UsePreviousValue': True|False,
                'ResolvedValue': 'string'
            },
        ],
        DisableRollback=True|False,
        RollbackConfiguration={
            'RollbackTriggers': [
                {
                    'Arn': 'string',
                    'Type': 'string'
                },
            ],
            'MonitoringTimeInMinutes': 123
        },
        TimeoutInMinutes=123,
        NotificationARNs=[
            'string',
        ],
        Capabilities=[
            'CAPABILITY_IAM'|'CAPABILITY_NAMED_IAM'|'CAPABILITY_AUTO_EXPAND',
        ],
        ResourceTypes=[
            'string',
        ],
        RoleARN='string',
        OnFailure='DO_NOTHING'|'ROLLBACK'|'DELETE',
        StackPolicyBody='string',
        StackPolicyURL='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        ClientRequestToken='string',
        EnableTerminationProtection=True|False
    )
    
    
    :type StackName: string
    :param StackName: [REQUIRED]\nThe name that is associated with the stack. The name must be unique in the Region in which you are creating the stack.\n\nNote\nA stack name can contain only alphanumeric characters (case sensitive) and hyphens. It must start with an alphabetic character and cannot be longer than 128 characters.\n\n

    :type TemplateBody: string
    :param TemplateBody: Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes. For more information, go to Template Anatomy in the AWS CloudFormation User Guide.\nConditional: You must specify either the TemplateBody or the TemplateURL parameter, but not both.\n

    :type TemplateURL: string
    :param TemplateURL: Location of file containing the template body. The URL must point to a template (max size: 460,800 bytes) that is located in an Amazon S3 bucket. For more information, go to the Template Anatomy in the AWS CloudFormation User Guide.\nConditional: You must specify either the TemplateBody or the TemplateURL parameter, but not both.\n

    :type Parameters: list
    :param Parameters: A list of Parameter structures that specify input parameters for the stack. For more information, see the Parameter data type.\n\n(dict) --The Parameter data type.\n\nParameterKey (string) --The key associated with the parameter. If you don\'t specify a key and value for a particular parameter, AWS CloudFormation uses the default value that is specified in your template.\n\nParameterValue (string) --The input value associated with the parameter.\n\nUsePreviousValue (boolean) --During a stack update, use the existing parameter value that the stack is using for a given parameter key. If you specify true , do not specify a parameter value.\n\nResolvedValue (string) --Read-only. The value that corresponds to a Systems Manager parameter key. This field is returned only for ` SSM parameter types <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html#aws-ssm-parameter-types>`__ in the template.\n\n\n\n\n

    :type DisableRollback: boolean
    :param DisableRollback: Set to true to disable rollback of the stack if stack creation failed. You can specify either DisableRollback or OnFailure , but not both.\nDefault: false\n

    :type RollbackConfiguration: dict
    :param RollbackConfiguration: The rollback triggers for AWS CloudFormation to monitor during stack creation and updating operations, and for the specified monitoring period afterwards.\n\nRollbackTriggers (list) --The triggers to monitor during stack creation or update actions.\nBy default, AWS CloudFormation saves the rollback triggers specified for a stack and applies them to any subsequent update operations for the stack, unless you specify otherwise. If you do specify rollback triggers for this parameter, those triggers replace any list of triggers previously specified for the stack. This means:\n\nTo use the rollback triggers previously specified for this stack, if any, don\'t specify this parameter.\nTo specify new or updated rollback triggers, you must specify all the triggers that you want used for this stack, even triggers you\'ve specifed before (for example, when creating the stack or during a previous stack update). Any triggers that you don\'t include in the updated list of triggers are no longer applied to the stack.\nTo remove all currently specified triggers, specify an empty list for this parameter.\n\nIf a specified trigger is missing, the entire stack operation fails and is rolled back.\n\n(dict) --A rollback trigger AWS CloudFormation monitors during creation and updating of stacks. If any of the alarms you specify goes to ALARM state during the stack operation or within the specified monitoring period afterwards, CloudFormation rolls back the entire stack operation.\n\nArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the rollback trigger.\nIf a specified trigger is missing, the entire stack operation fails and is rolled back.\n\nType (string) -- [REQUIRED]The resource type of the rollback trigger. Currently, AWS::CloudWatch::Alarm is the only supported resource type.\n\n\n\n\n\nMonitoringTimeInMinutes (integer) --The amount of time, in minutes, during which CloudFormation should monitor all the rollback triggers after the stack creation or update operation deploys all necessary resources.\nThe default is 0 minutes.\nIf you specify a monitoring period but do not specify any rollback triggers, CloudFormation still waits the specified period of time before cleaning up old resources after update operations. You can use this monitoring period to perform any manual stack validation desired, and manually cancel the stack creation or update (using CancelUpdateStack , for example) as necessary.\nIf you specify 0 for this parameter, CloudFormation still monitors the specified rollback triggers during stack creation and update operations. Then, for update operations, it begins disposing of old resources immediately once the operation completes.\n\n\n

    :type TimeoutInMinutes: integer
    :param TimeoutInMinutes: The amount of time that can pass before the stack status becomes CREATE_FAILED; if DisableRollback is not set or is set to false , the stack will be rolled back.

    :type NotificationARNs: list
    :param NotificationARNs: The Simple Notification Service (SNS) topic ARNs to publish stack related events. You can find your SNS topic ARNs using the SNS console or your Command Line Interface (CLI).\n\n(string) --\n\n

    :type Capabilities: list
    :param Capabilities: In some cases, you must explicitly acknowledge that your stack template contains certain capabilities in order for AWS CloudFormation to create the stack.\n\nCAPABILITY_IAM and CAPABILITY_NAMED_IAM  Some stack templates might include resources that can affect permissions in your AWS account; for example, by creating new AWS Identity and Access Management (IAM) users. For those stacks, you must explicitly acknowledge this by specifying one of these capabilities. The following IAM resources require you to specify either the CAPABILITY_IAM or CAPABILITY_NAMED_IAM capability.\nIf you have IAM resources, you can specify either capability.\nIf you have IAM resources with custom names, you must specify CAPABILITY_NAMED_IAM .\nIf you don\'t specify either of these capabilities, AWS CloudFormation returns an InsufficientCapabilities error.\n\n\n\nIf your stack template contains these resources, we recommend that you review all permissions associated with them and edit their permissions if necessary.\n\n\nAWS::IAM::AccessKey\nAWS::IAM::Group\nAWS::IAM::InstanceProfile\nAWS::IAM::Policy\nAWS::IAM::Role\nAWS::IAM::User\nAWS::IAM::UserToGroupAddition\n\n\nFor more information, see Acknowledging IAM Resources in AWS CloudFormation Templates .\n\nCAPABILITY_AUTO_EXPAND  Some template contain macros. Macros perform custom processing on templates; this can include simple actions like find-and-replace operations, all the way to extensive transformations of entire templates. Because of this, users typically create a change set from the processed template, so that they can review the changes resulting from the macros before actually creating the stack. If your stack template contains one or more macros, and you choose to create a stack directly from the processed template, without first reviewing the resulting changes in a change set, you must acknowledge this capability. This includes the AWS::Include and AWS::Serverless transforms, which are macros hosted by AWS CloudFormation. Change sets do not currently support nested stacks. If you want to create a stack from a stack template that contains macros and nested stacks, you must create the stack directly from the template using this capability.\n\n\nWarning\n\nYou should only create stacks directly from a stack template that contains macros if you know what processing the macro performs. Each macro relies on an underlying Lambda service function for processing stack templates. Be aware that the Lambda function owner can update the function operation without AWS CloudFormation being notified.\nFor more information, see Using AWS CloudFormation Macros to Perform Custom Processing on Templates .\n\n\n(string) --\n\n

    :type ResourceTypes: list
    :param ResourceTypes: The template resource types that you have permissions to work with for this create stack action, such as AWS::EC2::Instance , AWS::EC2::* , or Custom::MyCustomInstance . Use the following syntax to describe template resource types: AWS::* (for all AWS resource), Custom::* (for all custom resources), Custom::*logical_ID* `` (for a specific custom resource), ``AWS::*service_name* ::* (for all resources of a particular AWS service), and ``AWS::service_name ::resource_logical_ID `` (for a specific AWS resource).\nIf the list of resource types doesn\'t include a resource that you\'re creating, the stack creation fails. By default, AWS CloudFormation grants permissions to all resource types. AWS Identity and Access Management (IAM) uses this parameter for AWS CloudFormation-specific condition keys in IAM policies. For more information, see Controlling Access with AWS Identity and Access Management .\n\n(string) --\n\n

    :type RoleARN: string
    :param RoleARN: The Amazon Resource Name (ARN) of an AWS Identity and Access Management (IAM) role that AWS CloudFormation assumes to create the stack. AWS CloudFormation uses the role\'s credentials to make calls on your behalf. AWS CloudFormation always uses this role for all future operations on the stack. As long as users have permission to operate on the stack, AWS CloudFormation uses this role even if the users don\'t have permission to pass it. Ensure that the role grants least privilege.\nIf you don\'t specify a value, AWS CloudFormation uses the role that was previously associated with the stack. If no role is available, AWS CloudFormation uses a temporary session that is generated from your user credentials.\n

    :type OnFailure: string
    :param OnFailure: Determines what action will be taken if stack creation fails. This must be one of: DO_NOTHING, ROLLBACK, or DELETE. You can specify either OnFailure or DisableRollback , but not both.\nDefault: ROLLBACK\n

    :type StackPolicyBody: string
    :param StackPolicyBody: Structure containing the stack policy body. For more information, go to Prevent Updates to Stack Resources in the AWS CloudFormation User Guide . You can specify either the StackPolicyBody or the StackPolicyURL parameter, but not both.

    :type StackPolicyURL: string
    :param StackPolicyURL: Location of a file containing the stack policy. The URL must point to a policy (maximum size: 16 KB) located in an S3 bucket in the same Region as the stack. You can specify either the StackPolicyBody or the StackPolicyURL parameter, but not both.

    :type Tags: list
    :param Tags: Key-value pairs to associate with this stack. AWS CloudFormation also propagates these tags to the resources created in the stack. A maximum number of 50 tags can be specified.\n\n(dict) --The Tag type enables you to specify a key-value pair that can be used to store information about an AWS CloudFormation stack.\n\nKey (string) -- [REQUIRED]\nRequired . A string used to identify this tag. You can specify a maximum of 128 characters for a tag key. Tags owned by Amazon Web Services (AWS) have the reserved prefix: aws: .\n\nValue (string) -- [REQUIRED]\nRequired . A string containing the value for this tag. You can specify a maximum of 256 characters for a tag value.\n\n\n\n\n

    :type ClientRequestToken: string
    :param ClientRequestToken: A unique identifier for this CreateStack request. Specify this token if you plan to retry requests so that AWS CloudFormation knows that you\'re not attempting to create a stack with the same name. You might retry CreateStack requests to ensure that AWS CloudFormation successfully received them.\nAll events triggered by a given stack operation are assigned the same client request token, which you can use to track operations. For example, if you execute a CreateStack operation with the token token1 , then all the StackEvents generated by that operation will have ClientRequestToken set as token1 .\nIn the console, stack operations display the client request token on the Events tab. Stack operations that are initiated from the console use the token format Console-StackOperation-ID , which helps you easily identify the stack operation . For example, if you create a stack using the console, each stack event would be assigned the same token in the following format: Console-CreateStack-7f59c3cf-00d2-40c7-b2ff-e75db0987002 .\n

    :type EnableTerminationProtection: boolean
    :param EnableTerminationProtection: Whether to enable termination protection on the specified stack. If a user attempts to delete a stack with termination protection enabled, the operation fails and the stack remains unchanged. For more information, see Protecting a Stack From Being Deleted in the AWS CloudFormation User Guide . Termination protection is disabled on stacks by default.\nFor nested stacks , termination protection is set on the root stack and cannot be changed directly on the nested stack.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'StackId': 'string'
}


Response Structure

(dict) --
The output for a  CreateStack action.

StackId (string) --
Unique identifier of the stack.







Exceptions

CloudFormation.Client.exceptions.LimitExceededException
CloudFormation.Client.exceptions.AlreadyExistsException
CloudFormation.Client.exceptions.TokenAlreadyExistsException
CloudFormation.Client.exceptions.InsufficientCapabilitiesException


    :return: {
        'StackId': 'string'
    }
    
    
    :returns: 
    CloudFormation.Client.exceptions.LimitExceededException
    CloudFormation.Client.exceptions.AlreadyExistsException
    CloudFormation.Client.exceptions.TokenAlreadyExistsException
    CloudFormation.Client.exceptions.InsufficientCapabilitiesException
    
    """
    pass

def create_stack_instances(StackSetName=None, Accounts=None, DeploymentTargets=None, Regions=None, ParameterOverrides=None, OperationPreferences=None, OperationId=None):
    """
    Creates stack instances for the specified accounts, within the specified Regions. A stack instance refers to a stack in a specific account and Region. You must specify at least one value for either Accounts or DeploymentTargets , and you must specify at least one value for Regions .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_stack_instances(
        StackSetName='string',
        Accounts=[
            'string',
        ],
        DeploymentTargets={
            'Accounts': [
                'string',
            ],
            'OrganizationalUnitIds': [
                'string',
            ]
        },
        Regions=[
            'string',
        ],
        ParameterOverrides=[
            {
                'ParameterKey': 'string',
                'ParameterValue': 'string',
                'UsePreviousValue': True|False,
                'ResolvedValue': 'string'
            },
        ],
        OperationPreferences={
            'RegionOrder': [
                'string',
            ],
            'FailureToleranceCount': 123,
            'FailureTolerancePercentage': 123,
            'MaxConcurrentCount': 123,
            'MaxConcurrentPercentage': 123
        },
        OperationId='string'
    )
    
    
    :type StackSetName: string
    :param StackSetName: [REQUIRED]\nThe name or unique ID of the stack set that you want to create stack instances from.\n

    :type Accounts: list
    :param Accounts: [Self-managed permissions] The names of one or more AWS accounts that you want to create stack instances in the specified Region(s) for.\nYou can specify Accounts or DeploymentTargets , but not both.\n\n(string) --\n\n

    :type DeploymentTargets: dict
    :param DeploymentTargets: [Service-managed permissions] The AWS Organizations accounts for which to create stack instances in the specified Regions.\nYou can specify Accounts or DeploymentTargets , but not both.\n\nAccounts (list) --The names of one or more AWS accounts for which you want to deploy stack set updates.\n\n(string) --\n\n\nOrganizationalUnitIds (list) --The organization root ID or organizational unit (OU) IDs to which StackSets deploys.\n\n(string) --\n\n\n\n

    :type Regions: list
    :param Regions: [REQUIRED]\nThe names of one or more Regions where you want to create stack instances using the specified AWS account(s).\n\n(string) --\n\n

    :type ParameterOverrides: list
    :param ParameterOverrides: A list of stack set parameters whose values you want to override in the selected stack instances.\nAny overridden parameter values will be applied to all stack instances in the specified accounts and Regions. When specifying parameters and their values, be aware of how AWS CloudFormation sets parameter values during stack instance operations:\n\nTo override the current value for a parameter, include the parameter and specify its value.\nTo leave a parameter set to its present value, you can do one of the following:\nDo not include the parameter in the list.\nInclude the parameter and specify UsePreviousValue as true . (You cannot specify both a value and set UsePreviousValue to true .)\n\n\nTo set all overridden parameter back to the values specified in the stack set, specify a parameter list but do not include any parameters.\nTo leave all parameters set to their present values, do not specify this property at all.\n\nDuring stack set updates, any parameter values overridden for a stack instance are not updated, but retain their overridden value.\nYou can only override the parameter values that are specified in the stack set; to add or delete a parameter itself, use UpdateStackSet to update the stack set template.\n\n(dict) --The Parameter data type.\n\nParameterKey (string) --The key associated with the parameter. If you don\'t specify a key and value for a particular parameter, AWS CloudFormation uses the default value that is specified in your template.\n\nParameterValue (string) --The input value associated with the parameter.\n\nUsePreviousValue (boolean) --During a stack update, use the existing parameter value that the stack is using for a given parameter key. If you specify true , do not specify a parameter value.\n\nResolvedValue (string) --Read-only. The value that corresponds to a Systems Manager parameter key. This field is returned only for ` SSM parameter types <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html#aws-ssm-parameter-types>`__ in the template.\n\n\n\n\n

    :type OperationPreferences: dict
    :param OperationPreferences: Preferences for how AWS CloudFormation performs this stack set operation.\n\nRegionOrder (list) --The order of the Regions in where you want to perform the stack operation.\n\n(string) --\n\n\nFailureToleranceCount (integer) --The number of accounts, per Region, for which this operation can fail before AWS CloudFormation stops the operation in that Region. If the operation is stopped in a Region, AWS CloudFormation doesn\'t attempt the operation in any subsequent Regions.\nConditional: You must specify either FailureToleranceCount or FailureTolerancePercentage (but not both).\n\nFailureTolerancePercentage (integer) --The percentage of accounts, per Region, for which this stack operation can fail before AWS CloudFormation stops the operation in that Region. If the operation is stopped in a Region, AWS CloudFormation doesn\'t attempt the operation in any subsequent Regions.\nWhen calculating the number of accounts based on the specified percentage, AWS CloudFormation rounds down to the next whole number.\nConditional: You must specify either FailureToleranceCount or FailureTolerancePercentage , but not both.\n\nMaxConcurrentCount (integer) --The maximum number of accounts in which to perform this operation at one time. This is dependent on the value of FailureToleranceCount \xe2\x80\x94MaxConcurrentCount is at most one more than the FailureToleranceCount .\nNote that this setting lets you specify the maximum for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling.\nConditional: You must specify either MaxConcurrentCount or MaxConcurrentPercentage , but not both.\n\nMaxConcurrentPercentage (integer) --The maximum percentage of accounts in which to perform this operation at one time.\nWhen calculating the number of accounts based on the specified percentage, AWS CloudFormation rounds down to the next whole number. This is true except in cases where rounding down would result is zero. In this case, CloudFormation sets the number as one instead.\nNote that this setting lets you specify the maximum for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling.\nConditional: You must specify either MaxConcurrentCount or MaxConcurrentPercentage , but not both.\n\n\n

    :type OperationId: string
    :param OperationId: The unique identifier for this stack set operation.\nThe operation ID also functions as an idempotency token, to ensure that AWS CloudFormation performs the stack set operation only once, even if you retry the request multiple times. You might retry stack set operation requests to ensure that AWS CloudFormation successfully received them.\nIf you don\'t specify an operation ID, the SDK generates one automatically.\nRepeating this stack set operation with a new operation ID retries all stack instances whose status is OUTDATED .\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'OperationId': 'string'
}


Response Structure

(dict) --

OperationId (string) --
The unique identifier for this stack set operation.







Exceptions

CloudFormation.Client.exceptions.StackSetNotFoundException
CloudFormation.Client.exceptions.OperationInProgressException
CloudFormation.Client.exceptions.OperationIdAlreadyExistsException
CloudFormation.Client.exceptions.StaleRequestException
CloudFormation.Client.exceptions.InvalidOperationException
CloudFormation.Client.exceptions.LimitExceededException


    :return: {
        'OperationId': 'string'
    }
    
    
    :returns: 
    CloudFormation.Client.exceptions.StackSetNotFoundException
    CloudFormation.Client.exceptions.OperationInProgressException
    CloudFormation.Client.exceptions.OperationIdAlreadyExistsException
    CloudFormation.Client.exceptions.StaleRequestException
    CloudFormation.Client.exceptions.InvalidOperationException
    CloudFormation.Client.exceptions.LimitExceededException
    
    """
    pass

def create_stack_set(StackSetName=None, Description=None, TemplateBody=None, TemplateURL=None, Parameters=None, Capabilities=None, Tags=None, AdministrationRoleARN=None, ExecutionRoleName=None, PermissionModel=None, AutoDeployment=None, ClientRequestToken=None):
    """
    Creates a stack set.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_stack_set(
        StackSetName='string',
        Description='string',
        TemplateBody='string',
        TemplateURL='string',
        Parameters=[
            {
                'ParameterKey': 'string',
                'ParameterValue': 'string',
                'UsePreviousValue': True|False,
                'ResolvedValue': 'string'
            },
        ],
        Capabilities=[
            'CAPABILITY_IAM'|'CAPABILITY_NAMED_IAM'|'CAPABILITY_AUTO_EXPAND',
        ],
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        AdministrationRoleARN='string',
        ExecutionRoleName='string',
        PermissionModel='SERVICE_MANAGED'|'SELF_MANAGED',
        AutoDeployment={
            'Enabled': True|False,
            'RetainStacksOnAccountRemoval': True|False
        },
        ClientRequestToken='string'
    )
    
    
    :type StackSetName: string
    :param StackSetName: [REQUIRED]\nThe name to associate with the stack set. The name must be unique in the Region where you create your stack set.\n\nNote\nA stack name can contain only alphanumeric characters (case-sensitive) and hyphens. It must start with an alphabetic character and can\'t be longer than 128 characters.\n\n

    :type Description: string
    :param Description: A description of the stack set. You can use the description to identify the stack set\'s purpose or other important information.

    :type TemplateBody: string
    :param TemplateBody: The structure that contains the template body, with a minimum length of 1 byte and a maximum length of 51,200 bytes. For more information, see Template Anatomy in the AWS CloudFormation User Guide.\nConditional: You must specify either the TemplateBody or the TemplateURL parameter, but not both.\n

    :type TemplateURL: string
    :param TemplateURL: The location of the file that contains the template body. The URL must point to a template (maximum size: 460,800 bytes) that\'s located in an Amazon S3 bucket. For more information, see Template Anatomy in the AWS CloudFormation User Guide.\nConditional: You must specify either the TemplateBody or the TemplateURL parameter, but not both.\n

    :type Parameters: list
    :param Parameters: The input parameters for the stack set template.\n\n(dict) --The Parameter data type.\n\nParameterKey (string) --The key associated with the parameter. If you don\'t specify a key and value for a particular parameter, AWS CloudFormation uses the default value that is specified in your template.\n\nParameterValue (string) --The input value associated with the parameter.\n\nUsePreviousValue (boolean) --During a stack update, use the existing parameter value that the stack is using for a given parameter key. If you specify true , do not specify a parameter value.\n\nResolvedValue (string) --Read-only. The value that corresponds to a Systems Manager parameter key. This field is returned only for ` SSM parameter types <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html#aws-ssm-parameter-types>`__ in the template.\n\n\n\n\n

    :type Capabilities: list
    :param Capabilities: In some cases, you must explicitly acknowledge that your stack set template contains certain capabilities in order for AWS CloudFormation to create the stack set and related stack instances.\n\nCAPABILITY_IAM and CAPABILITY_NAMED_IAM  Some stack templates might include resources that can affect permissions in your AWS account; for example, by creating new AWS Identity and Access Management (IAM) users. For those stack sets, you must explicitly acknowledge this by specifying one of these capabilities. The following IAM resources require you to specify either the CAPABILITY_IAM or CAPABILITY_NAMED_IAM capability.\nIf you have IAM resources, you can specify either capability.\nIf you have IAM resources with custom names, you must specify CAPABILITY_NAMED_IAM .\nIf you don\'t specify either of these capabilities, AWS CloudFormation returns an InsufficientCapabilities error.\n\n\n\nIf your stack template contains these resources, we recommend that you review all permissions associated with them and edit their permissions if necessary.\n\n\nAWS::IAM::AccessKey\nAWS::IAM::Group\nAWS::IAM::InstanceProfile\nAWS::IAM::Policy\nAWS::IAM::Role\nAWS::IAM::User\nAWS::IAM::UserToGroupAddition\n\n\nFor more information, see Acknowledging IAM Resources in AWS CloudFormation Templates .\n\nCAPABILITY_AUTO_EXPAND  Some templates contain macros. If your stack template contains one or more macros, and you choose to create a stack directly from the processed template, without first reviewing the resulting changes in a change set, you must acknowledge this capability. For more information, see Using AWS CloudFormation Macros to Perform Custom Processing on Templates .\n\n\nNote\nStack sets do not currently support macros in stack templates. (This includes the AWS::Include and AWS::Serverless transforms, which are macros hosted by AWS CloudFormation.) Even if you specify this capability, if you include a macro in your template the stack set operation will fail.\n\n\n(string) --\n\n

    :type Tags: list
    :param Tags: The key-value pairs to associate with this stack set and the stacks created from it. AWS CloudFormation also propagates these tags to supported resources that are created in the stacks. A maximum number of 50 tags can be specified.\nIf you specify tags as part of a CreateStackSet action, AWS CloudFormation checks to see if you have the required IAM permission to tag resources. If you don\'t, the entire CreateStackSet action fails with an access denied error, and the stack set is not created.\n\n(dict) --The Tag type enables you to specify a key-value pair that can be used to store information about an AWS CloudFormation stack.\n\nKey (string) -- [REQUIRED]\nRequired . A string used to identify this tag. You can specify a maximum of 128 characters for a tag key. Tags owned by Amazon Web Services (AWS) have the reserved prefix: aws: .\n\nValue (string) -- [REQUIRED]\nRequired . A string containing the value for this tag. You can specify a maximum of 256 characters for a tag value.\n\n\n\n\n

    :type AdministrationRoleARN: string
    :param AdministrationRoleARN: The Amazon Resource Number (ARN) of the IAM role to use to create this stack set.\nSpecify an IAM role only if you are using customized administrator roles to control which users or groups can manage specific stack sets within the same administrator account. For more information, see Prerequisites: Granting Permissions for Stack Set Operations in the AWS CloudFormation User Guide .\n

    :type ExecutionRoleName: string
    :param ExecutionRoleName: The name of the IAM execution role to use to create the stack set. If you do not specify an execution role, AWS CloudFormation uses the AWSCloudFormationStackSetExecutionRole role for the stack set operation.\nSpecify an IAM role only if you are using customized execution roles to control which stack resources users and groups can include in their stack sets.\n

    :type PermissionModel: string
    :param PermissionModel: Describes how the IAM roles required for stack set operations are created. By default, SELF-MANAGED is specified.\n\nWith self-managed permissions, you must create the administrator and execution roles required to deploy to target accounts. For more information, see Grant Self-Managed Stack Set Permissions .\nWith service-managed permissions, StackSets automatically creates the IAM roles required to deploy to accounts managed by AWS Organizations. For more information, see Grant Service-Managed Stack Set Permissions .\n\n

    :type AutoDeployment: dict
    :param AutoDeployment: Describes whether StackSets automatically deploys to AWS Organizations accounts that are added to the target organization or organizational unit (OU). Specify only if PermissionModel is SERVICE_MANAGED .\n\nEnabled (boolean) --If set to true , StackSets automatically deploys additional stack instances to AWS Organizations accounts that are added to a target organization or organizational unit (OU) in the specified Regions. If an account is removed from a target organization or OU, StackSets deletes stack instances from the account in the specified Regions.\n\nRetainStacksOnAccountRemoval (boolean) --If set to true , stack resources are retained when an account is removed from a target organization or OU. If set to false , stack resources are deleted. Specify only if Enabled is set to True .\n\n\n

    :type ClientRequestToken: string
    :param ClientRequestToken: A unique identifier for this CreateStackSet request. Specify this token if you plan to retry requests so that AWS CloudFormation knows that you\'re not attempting to create another stack set with the same name. You might retry CreateStackSet requests to ensure that AWS CloudFormation successfully received them.\nIf you don\'t specify an operation ID, the SDK generates one automatically.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'StackSetId': 'string'
}


Response Structure

(dict) --

StackSetId (string) --
The ID of the stack set that you\'re creating.







Exceptions

CloudFormation.Client.exceptions.NameAlreadyExistsException
CloudFormation.Client.exceptions.CreatedButModifiedException
CloudFormation.Client.exceptions.LimitExceededException


    :return: {
        'StackSetId': 'string'
    }
    
    
    :returns: 
    CloudFormation.Client.exceptions.NameAlreadyExistsException
    CloudFormation.Client.exceptions.CreatedButModifiedException
    CloudFormation.Client.exceptions.LimitExceededException
    
    """
    pass

def delete_change_set(ChangeSetName=None, StackName=None):
    """
    Deletes the specified change set. Deleting change sets ensures that no one executes the wrong change set.
    If the call successfully completes, AWS CloudFormation successfully deleted the change set.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_change_set(
        ChangeSetName='string',
        StackName='string'
    )
    
    
    :type ChangeSetName: string
    :param ChangeSetName: [REQUIRED]\nThe name or Amazon Resource Name (ARN) of the change set that you want to delete.\n

    :type StackName: string
    :param StackName: If you specified the name of a change set to delete, specify the stack name or ID (ARN) that is associated with it.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
The output for the  DeleteChangeSet action.





Exceptions

CloudFormation.Client.exceptions.InvalidChangeSetStatusException


    :return: {}
    
    
    :returns: 
    CloudFormation.Client.exceptions.InvalidChangeSetStatusException
    
    """
    pass

def delete_stack(StackName=None, RetainResources=None, RoleARN=None, ClientRequestToken=None):
    """
    Deletes a specified stack. Once the call completes successfully, stack deletion starts. Deleted stacks do not show up in the  DescribeStacks API if the deletion has been completed successfully.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_stack(
        StackName='string',
        RetainResources=[
            'string',
        ],
        RoleARN='string',
        ClientRequestToken='string'
    )
    
    
    :type StackName: string
    :param StackName: [REQUIRED]\nThe name or the unique stack ID that is associated with the stack.\n

    :type RetainResources: list
    :param RetainResources: For stacks in the DELETE_FAILED state, a list of resource logical IDs that are associated with the resources you want to retain. During deletion, AWS CloudFormation deletes the stack but does not delete the retained resources.\nRetaining resources is useful when you cannot delete a resource, such as a non-empty S3 bucket, but you want to delete the stack.\n\n(string) --\n\n

    :type RoleARN: string
    :param RoleARN: The Amazon Resource Name (ARN) of an AWS Identity and Access Management (IAM) role that AWS CloudFormation assumes to delete the stack. AWS CloudFormation uses the role\'s credentials to make calls on your behalf.\nIf you don\'t specify a value, AWS CloudFormation uses the role that was previously associated with the stack. If no role is available, AWS CloudFormation uses a temporary session that is generated from your user credentials.\n

    :type ClientRequestToken: string
    :param ClientRequestToken: A unique identifier for this DeleteStack request. Specify this token if you plan to retry requests so that AWS CloudFormation knows that you\'re not attempting to delete a stack with the same name. You might retry DeleteStack requests to ensure that AWS CloudFormation successfully received them.\nAll events triggered by a given stack operation are assigned the same client request token, which you can use to track operations. For example, if you execute a CreateStack operation with the token token1 , then all the StackEvents generated by that operation will have ClientRequestToken set as token1 .\nIn the console, stack operations display the client request token on the Events tab. Stack operations that are initiated from the console use the token format Console-StackOperation-ID , which helps you easily identify the stack operation . For example, if you create a stack using the console, each stack event would be assigned the same token in the following format: Console-CreateStack-7f59c3cf-00d2-40c7-b2ff-e75db0987002 .\n

    :returns: 
    CloudFormation.Client.exceptions.TokenAlreadyExistsException
    
    """
    pass

def delete_stack_instances(StackSetName=None, Accounts=None, DeploymentTargets=None, Regions=None, OperationPreferences=None, RetainStacks=None, OperationId=None):
    """
    Deletes stack instances for the specified accounts, in the specified Regions.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_stack_instances(
        StackSetName='string',
        Accounts=[
            'string',
        ],
        DeploymentTargets={
            'Accounts': [
                'string',
            ],
            'OrganizationalUnitIds': [
                'string',
            ]
        },
        Regions=[
            'string',
        ],
        OperationPreferences={
            'RegionOrder': [
                'string',
            ],
            'FailureToleranceCount': 123,
            'FailureTolerancePercentage': 123,
            'MaxConcurrentCount': 123,
            'MaxConcurrentPercentage': 123
        },
        RetainStacks=True|False,
        OperationId='string'
    )
    
    
    :type StackSetName: string
    :param StackSetName: [REQUIRED]\nThe name or unique ID of the stack set that you want to delete stack instances for.\n

    :type Accounts: list
    :param Accounts: [Self-managed permissions] The names of the AWS accounts that you want to delete stack instances for.\nYou can specify Accounts or DeploymentTargets , but not both.\n\n(string) --\n\n

    :type DeploymentTargets: dict
    :param DeploymentTargets: [Service-managed permissions] The AWS Organizations accounts from which to delete stack instances.\nYou can specify Accounts or DeploymentTargets , but not both.\n\nAccounts (list) --The names of one or more AWS accounts for which you want to deploy stack set updates.\n\n(string) --\n\n\nOrganizationalUnitIds (list) --The organization root ID or organizational unit (OU) IDs to which StackSets deploys.\n\n(string) --\n\n\n\n

    :type Regions: list
    :param Regions: [REQUIRED]\nThe Regions where you want to delete stack set instances.\n\n(string) --\n\n

    :type OperationPreferences: dict
    :param OperationPreferences: Preferences for how AWS CloudFormation performs this stack set operation.\n\nRegionOrder (list) --The order of the Regions in where you want to perform the stack operation.\n\n(string) --\n\n\nFailureToleranceCount (integer) --The number of accounts, per Region, for which this operation can fail before AWS CloudFormation stops the operation in that Region. If the operation is stopped in a Region, AWS CloudFormation doesn\'t attempt the operation in any subsequent Regions.\nConditional: You must specify either FailureToleranceCount or FailureTolerancePercentage (but not both).\n\nFailureTolerancePercentage (integer) --The percentage of accounts, per Region, for which this stack operation can fail before AWS CloudFormation stops the operation in that Region. If the operation is stopped in a Region, AWS CloudFormation doesn\'t attempt the operation in any subsequent Regions.\nWhen calculating the number of accounts based on the specified percentage, AWS CloudFormation rounds down to the next whole number.\nConditional: You must specify either FailureToleranceCount or FailureTolerancePercentage , but not both.\n\nMaxConcurrentCount (integer) --The maximum number of accounts in which to perform this operation at one time. This is dependent on the value of FailureToleranceCount \xe2\x80\x94MaxConcurrentCount is at most one more than the FailureToleranceCount .\nNote that this setting lets you specify the maximum for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling.\nConditional: You must specify either MaxConcurrentCount or MaxConcurrentPercentage , but not both.\n\nMaxConcurrentPercentage (integer) --The maximum percentage of accounts in which to perform this operation at one time.\nWhen calculating the number of accounts based on the specified percentage, AWS CloudFormation rounds down to the next whole number. This is true except in cases where rounding down would result is zero. In this case, CloudFormation sets the number as one instead.\nNote that this setting lets you specify the maximum for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling.\nConditional: You must specify either MaxConcurrentCount or MaxConcurrentPercentage , but not both.\n\n\n

    :type RetainStacks: boolean
    :param RetainStacks: [REQUIRED]\nRemoves the stack instances from the specified stack set, but doesn\'t delete the stacks. You can\'t reassociate a retained stack or add an existing, saved stack to a new stack set.\nFor more information, see Stack set operation options .\n

    :type OperationId: string
    :param OperationId: The unique identifier for this stack set operation.\nIf you don\'t specify an operation ID, the SDK generates one automatically.\nThe operation ID also functions as an idempotency token, to ensure that AWS CloudFormation performs the stack set operation only once, even if you retry the request multiple times. You can retry stack set operation requests to ensure that AWS CloudFormation successfully received them.\nRepeating this stack set operation with a new operation ID retries all stack instances whose status is OUTDATED .\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'OperationId': 'string'
}


Response Structure

(dict) --

OperationId (string) --
The unique identifier for this stack set operation.







Exceptions

CloudFormation.Client.exceptions.StackSetNotFoundException
CloudFormation.Client.exceptions.OperationInProgressException
CloudFormation.Client.exceptions.OperationIdAlreadyExistsException
CloudFormation.Client.exceptions.StaleRequestException
CloudFormation.Client.exceptions.InvalidOperationException


    :return: {
        'OperationId': 'string'
    }
    
    
    :returns: 
    CloudFormation.Client.exceptions.StackSetNotFoundException
    CloudFormation.Client.exceptions.OperationInProgressException
    CloudFormation.Client.exceptions.OperationIdAlreadyExistsException
    CloudFormation.Client.exceptions.StaleRequestException
    CloudFormation.Client.exceptions.InvalidOperationException
    
    """
    pass

def delete_stack_set(StackSetName=None):
    """
    Deletes a stack set. Before you can delete a stack set, all of its member stack instances must be deleted. For more information about how to do this, see  DeleteStackInstances .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_stack_set(
        StackSetName='string'
    )
    
    
    :type StackSetName: string
    :param StackSetName: [REQUIRED]\nThe name or unique ID of the stack set that you\'re deleting. You can obtain this value by running ListStackSets .\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

CloudFormation.Client.exceptions.StackSetNotEmptyException
CloudFormation.Client.exceptions.OperationInProgressException


    :return: {}
    
    
    :returns: 
    CloudFormation.Client.exceptions.StackSetNotEmptyException
    CloudFormation.Client.exceptions.OperationInProgressException
    
    """
    pass

def deregister_type(Arn=None, Type=None, TypeName=None, VersionId=None):
    """
    Removes a type or type version from active use in the CloudFormation registry. If a type or type version is deregistered, it cannot be used in CloudFormation operations.
    To deregister a type, you must individually deregister all registered versions of that type. If a type has only a single registered version, deregistering that version results in the type itself being deregistered.
    You cannot deregister the default version of a type, unless it is the only registered version of that type, in which case the type itself is deregistered as well.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.deregister_type(
        Arn='string',
        Type='RESOURCE',
        TypeName='string',
        VersionId='string'
    )
    
    
    :type Arn: string
    :param Arn: The Amazon Resource Name (ARN) of the type.\nConditional: You must specify either TypeName and Type , or Arn .\n

    :type Type: string
    :param Type: The kind of type.\nCurrently the only valid value is RESOURCE .\nConditional: You must specify either TypeName and Type , or Arn .\n

    :type TypeName: string
    :param TypeName: The name of the type.\nConditional: You must specify either TypeName and Type , or Arn .\n

    :type VersionId: string
    :param VersionId: The ID of a specific version of the type. The version ID is the value at the end of the Amazon Resource Name (ARN) assigned to the type version when it is registered.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

CloudFormation.Client.exceptions.CFNRegistryException
CloudFormation.Client.exceptions.TypeNotFoundException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def describe_account_limits(NextToken=None):
    """
    Retrieves your account\'s AWS CloudFormation limits, such as the maximum number of stacks that you can create in your account. For more information about account limits, see AWS CloudFormation Limits in the AWS CloudFormation User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.describe_account_limits(
        NextToken='string'
    )
    
    
    :type NextToken: string
    :param NextToken: A string that identifies the next page of limits that you want to retrieve.

    :rtype: dict
ReturnsResponse Syntax{
    'AccountLimits': [
        {
            'Name': 'string',
            'Value': 123
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --The output for the  DescribeAccountLimits action.

AccountLimits (list) --An account limit structure that contain a list of AWS CloudFormation account limits and their values.

(dict) --The AccountLimit data type.
CloudFormation has the following limits per account:

Number of concurrent resources
Number of stacks
Number of stack outputs

For more information about these account limits, and other CloudFormation limits, see AWS CloudFormation Limits in the AWS CloudFormation User Guide .

Name (string) --The name of the account limit.
Values: ConcurrentResourcesLimit | StackLimit | StackOutputsLimit

Value (integer) --The value that is associated with the account limit name.





NextToken (string) --If the output exceeds 1 MB in size, a string that identifies the next page of limits. If no additional page exists, this value is null.







    :return: {
        'AccountLimits': [
            {
                'Name': 'string',
                'Value': 123
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def describe_change_set(ChangeSetName=None, StackName=None, NextToken=None):
    """
    Returns the inputs for the change set and a list of changes that AWS CloudFormation will make if you execute the change set. For more information, see Updating Stacks Using Change Sets in the AWS CloudFormation User Guide.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_change_set(
        ChangeSetName='string',
        StackName='string',
        NextToken='string'
    )
    
    
    :type ChangeSetName: string
    :param ChangeSetName: [REQUIRED]\nThe name or Amazon Resource Name (ARN) of the change set that you want to describe.\n

    :type StackName: string
    :param StackName: If you specified the name of a change set, specify the stack name or ID (ARN) of the change set you want to describe.

    :type NextToken: string
    :param NextToken: A string (provided by the DescribeChangeSet response output) that identifies the next page of information that you want to retrieve.

    :rtype: dict

ReturnsResponse Syntax
{
    'ChangeSetName': 'string',
    'ChangeSetId': 'string',
    'StackId': 'string',
    'StackName': 'string',
    'Description': 'string',
    'Parameters': [
        {
            'ParameterKey': 'string',
            'ParameterValue': 'string',
            'UsePreviousValue': True|False,
            'ResolvedValue': 'string'
        },
    ],
    'CreationTime': datetime(2015, 1, 1),
    'ExecutionStatus': 'UNAVAILABLE'|'AVAILABLE'|'EXECUTE_IN_PROGRESS'|'EXECUTE_COMPLETE'|'EXECUTE_FAILED'|'OBSOLETE',
    'Status': 'CREATE_PENDING'|'CREATE_IN_PROGRESS'|'CREATE_COMPLETE'|'DELETE_COMPLETE'|'FAILED',
    'StatusReason': 'string',
    'NotificationARNs': [
        'string',
    ],
    'RollbackConfiguration': {
        'RollbackTriggers': [
            {
                'Arn': 'string',
                'Type': 'string'
            },
        ],
        'MonitoringTimeInMinutes': 123
    },
    'Capabilities': [
        'CAPABILITY_IAM'|'CAPABILITY_NAMED_IAM'|'CAPABILITY_AUTO_EXPAND',
    ],
    'Tags': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ],
    'Changes': [
        {
            'Type': 'Resource',
            'ResourceChange': {
                'Action': 'Add'|'Modify'|'Remove'|'Import',
                'LogicalResourceId': 'string',
                'PhysicalResourceId': 'string',
                'ResourceType': 'string',
                'Replacement': 'True'|'False'|'Conditional',
                'Scope': [
                    'Properties'|'Metadata'|'CreationPolicy'|'UpdatePolicy'|'DeletionPolicy'|'Tags',
                ],
                'Details': [
                    {
                        'Target': {
                            'Attribute': 'Properties'|'Metadata'|'CreationPolicy'|'UpdatePolicy'|'DeletionPolicy'|'Tags',
                            'Name': 'string',
                            'RequiresRecreation': 'Never'|'Conditionally'|'Always'
                        },
                        'Evaluation': 'Static'|'Dynamic',
                        'ChangeSource': 'ResourceReference'|'ParameterReference'|'ResourceAttribute'|'DirectModification'|'Automatic',
                        'CausingEntity': 'string'
                    },
                ]
            }
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
The output for the  DescribeChangeSet action.

ChangeSetName (string) --
The name of the change set.

ChangeSetId (string) --
The ARN of the change set.

StackId (string) --
The ARN of the stack that is associated with the change set.

StackName (string) --
The name of the stack that is associated with the change set.

Description (string) --
Information about the change set.

Parameters (list) --
A list of Parameter structures that describes the input parameters and their values used to create the change set. For more information, see the Parameter data type.

(dict) --
The Parameter data type.

ParameterKey (string) --
The key associated with the parameter. If you don\'t specify a key and value for a particular parameter, AWS CloudFormation uses the default value that is specified in your template.

ParameterValue (string) --
The input value associated with the parameter.

UsePreviousValue (boolean) --
During a stack update, use the existing parameter value that the stack is using for a given parameter key. If you specify true , do not specify a parameter value.

ResolvedValue (string) --
Read-only. The value that corresponds to a Systems Manager parameter key. This field is returned only for ` SSM parameter types <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html#aws-ssm-parameter-types>`__ in the template.





CreationTime (datetime) --
The start time when the change set was created, in UTC.

ExecutionStatus (string) --
If the change set execution status is AVAILABLE , you can execute the change set. If you can\xe2\x80\x99t execute the change set, the status indicates why. For example, a change set might be in an UNAVAILABLE state because AWS CloudFormation is still creating it or in an OBSOLETE state because the stack was already updated.

Status (string) --
The current status of the change set, such as CREATE_IN_PROGRESS , CREATE_COMPLETE , or FAILED .

StatusReason (string) --
A description of the change set\'s status. For example, if your attempt to create a change set failed, AWS CloudFormation shows the error message.

NotificationARNs (list) --
The ARNs of the Amazon Simple Notification Service (Amazon SNS) topics that will be associated with the stack if you execute the change set.

(string) --


RollbackConfiguration (dict) --
The rollback triggers for AWS CloudFormation to monitor during stack creation and updating operations, and for the specified monitoring period afterwards.

RollbackTriggers (list) --
The triggers to monitor during stack creation or update actions.
By default, AWS CloudFormation saves the rollback triggers specified for a stack and applies them to any subsequent update operations for the stack, unless you specify otherwise. If you do specify rollback triggers for this parameter, those triggers replace any list of triggers previously specified for the stack. This means:

To use the rollback triggers previously specified for this stack, if any, don\'t specify this parameter.
To specify new or updated rollback triggers, you must specify all the triggers that you want used for this stack, even triggers you\'ve specifed before (for example, when creating the stack or during a previous stack update). Any triggers that you don\'t include in the updated list of triggers are no longer applied to the stack.
To remove all currently specified triggers, specify an empty list for this parameter.

If a specified trigger is missing, the entire stack operation fails and is rolled back.

(dict) --
A rollback trigger AWS CloudFormation monitors during creation and updating of stacks. If any of the alarms you specify goes to ALARM state during the stack operation or within the specified monitoring period afterwards, CloudFormation rolls back the entire stack operation.

Arn (string) --
The Amazon Resource Name (ARN) of the rollback trigger.
If a specified trigger is missing, the entire stack operation fails and is rolled back.

Type (string) --
The resource type of the rollback trigger. Currently, AWS::CloudWatch::Alarm is the only supported resource type.





MonitoringTimeInMinutes (integer) --
The amount of time, in minutes, during which CloudFormation should monitor all the rollback triggers after the stack creation or update operation deploys all necessary resources.
The default is 0 minutes.
If you specify a monitoring period but do not specify any rollback triggers, CloudFormation still waits the specified period of time before cleaning up old resources after update operations. You can use this monitoring period to perform any manual stack validation desired, and manually cancel the stack creation or update (using CancelUpdateStack , for example) as necessary.
If you specify 0 for this parameter, CloudFormation still monitors the specified rollback triggers during stack creation and update operations. Then, for update operations, it begins disposing of old resources immediately once the operation completes.



Capabilities (list) --
If you execute the change set, the list of capabilities that were explicitly acknowledged when the change set was created.

(string) --


Tags (list) --
If you execute the change set, the tags that will be associated with the stack.

(dict) --
The Tag type enables you to specify a key-value pair that can be used to store information about an AWS CloudFormation stack.

Key (string) --

Required . A string used to identify this tag. You can specify a maximum of 128 characters for a tag key. Tags owned by Amazon Web Services (AWS) have the reserved prefix: aws: .


Value (string) --

Required . A string containing the value for this tag. You can specify a maximum of 256 characters for a tag value.






Changes (list) --
A list of Change structures that describes the resources AWS CloudFormation changes if you execute the change set.

(dict) --
The Change structure describes the changes AWS CloudFormation will perform if you execute the change set.

Type (string) --
The type of entity that AWS CloudFormation changes. Currently, the only entity type is Resource .

ResourceChange (dict) --
A ResourceChange structure that describes the resource and action that AWS CloudFormation will perform.

Action (string) --
The action that AWS CloudFormation takes on the resource, such as Add (adds a new resource), Modify (changes a resource), or Remove (deletes a resource).

LogicalResourceId (string) --
The resource\'s logical ID, which is defined in the stack\'s template.

PhysicalResourceId (string) --
The resource\'s physical ID (resource name). Resources that you are adding don\'t have physical IDs because they haven\'t been created.

ResourceType (string) --
The type of AWS CloudFormation resource, such as AWS::S3::Bucket .

Replacement (string) --
For the Modify action, indicates whether AWS CloudFormation will replace the resource by creating a new one and deleting the old one. This value depends on the value of the RequiresRecreation property in the ResourceTargetDefinition structure. For example, if the RequiresRecreation field is Always and the Evaluation field is Static , Replacement is True . If the RequiresRecreation field is Always and the Evaluation field is Dynamic , Replacement is Conditionally .
If you have multiple changes with different RequiresRecreation values, the Replacement value depends on the change with the most impact. A RequiresRecreation value of Always has the most impact, followed by Conditionally , and then Never .

Scope (list) --
For the Modify action, indicates which resource attribute is triggering this update, such as a change in the resource attribute\'s Metadata , Properties , or Tags .

(string) --


Details (list) --
For the Modify action, a list of ResourceChangeDetail structures that describes the changes that AWS CloudFormation will make to the resource.

(dict) --
For a resource with Modify as the action, the ResourceChange structure describes the changes AWS CloudFormation will make to that resource.

Target (dict) --
A ResourceTargetDefinition structure that describes the field that AWS CloudFormation will change and whether the resource will be recreated.

Attribute (string) --
Indicates which resource attribute is triggering this update, such as a change in the resource attribute\'s Metadata , Properties , or Tags .

Name (string) --
If the Attribute value is Properties , the name of the property. For all other attributes, the value is null.

RequiresRecreation (string) --
If the Attribute value is Properties , indicates whether a change to this property causes the resource to be recreated. The value can be Never , Always , or Conditionally . To determine the conditions for a Conditionally recreation, see the update behavior for that property in the AWS CloudFormation User Guide.



Evaluation (string) --
Indicates whether AWS CloudFormation can determine the target value, and whether the target value will change before you execute a change set.
For Static evaluations, AWS CloudFormation can determine that the target value will change, and its value. For example, if you directly modify the InstanceType property of an EC2 instance, AWS CloudFormation knows that this property value will change, and its value, so this is a Static evaluation.
For Dynamic evaluations, cannot determine the target value because it depends on the result of an intrinsic function, such as a Ref or Fn::GetAtt intrinsic function, when the stack is updated. For example, if your template includes a reference to a resource that is conditionally recreated, the value of the reference (the physical ID of the resource) might change, depending on if the resource is recreated. If the resource is recreated, it will have a new physical ID, so all references to that resource will also be updated.

ChangeSource (string) --
The group to which the CausingEntity value belongs. There are five entity groups:

ResourceReference entities are Ref intrinsic functions that refer to resources in the template, such as { "Ref" : "MyEC2InstanceResource" } .
ParameterReference entities are Ref intrinsic functions that get template parameter values, such as { "Ref" : "MyPasswordParameter" } .
ResourceAttribute entities are Fn::GetAtt intrinsic functions that get resource attribute values, such as { "Fn::GetAtt" : [ "MyEC2InstanceResource", "PublicDnsName" ] } .
DirectModification entities are changes that are made directly to the template.
Automatic entities are AWS::CloudFormation::Stack resource types, which are also known as nested stacks. If you made no changes to the AWS::CloudFormation::Stack resource, AWS CloudFormation sets the ChangeSource to Automatic because the nested stack\'s template might have changed. Changes to a nested stack\'s template aren\'t visible to AWS CloudFormation until you run an update on the parent stack.


CausingEntity (string) --
The identity of the entity that triggered this change. This entity is a member of the group that is specified by the ChangeSource field. For example, if you modified the value of the KeyPairName parameter, the CausingEntity is the name of the parameter (KeyPairName ).
If the ChangeSource value is DirectModification , no value is given for CausingEntity .











NextToken (string) --
If the output exceeds 1 MB, a string that identifies the next page of changes. If there is no additional page, this value is null.







Exceptions

CloudFormation.Client.exceptions.ChangeSetNotFoundException


    :return: {
        'ChangeSetName': 'string',
        'ChangeSetId': 'string',
        'StackId': 'string',
        'StackName': 'string',
        'Description': 'string',
        'Parameters': [
            {
                'ParameterKey': 'string',
                'ParameterValue': 'string',
                'UsePreviousValue': True|False,
                'ResolvedValue': 'string'
            },
        ],
        'CreationTime': datetime(2015, 1, 1),
        'ExecutionStatus': 'UNAVAILABLE'|'AVAILABLE'|'EXECUTE_IN_PROGRESS'|'EXECUTE_COMPLETE'|'EXECUTE_FAILED'|'OBSOLETE',
        'Status': 'CREATE_PENDING'|'CREATE_IN_PROGRESS'|'CREATE_COMPLETE'|'DELETE_COMPLETE'|'FAILED',
        'StatusReason': 'string',
        'NotificationARNs': [
            'string',
        ],
        'RollbackConfiguration': {
            'RollbackTriggers': [
                {
                    'Arn': 'string',
                    'Type': 'string'
                },
            ],
            'MonitoringTimeInMinutes': 123
        },
        'Capabilities': [
            'CAPABILITY_IAM'|'CAPABILITY_NAMED_IAM'|'CAPABILITY_AUTO_EXPAND',
        ],
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        'Changes': [
            {
                'Type': 'Resource',
                'ResourceChange': {
                    'Action': 'Add'|'Modify'|'Remove'|'Import',
                    'LogicalResourceId': 'string',
                    'PhysicalResourceId': 'string',
                    'ResourceType': 'string',
                    'Replacement': 'True'|'False'|'Conditional',
                    'Scope': [
                        'Properties'|'Metadata'|'CreationPolicy'|'UpdatePolicy'|'DeletionPolicy'|'Tags',
                    ],
                    'Details': [
                        {
                            'Target': {
                                'Attribute': 'Properties'|'Metadata'|'CreationPolicy'|'UpdatePolicy'|'DeletionPolicy'|'Tags',
                                'Name': 'string',
                                'RequiresRecreation': 'Never'|'Conditionally'|'Always'
                            },
                            'Evaluation': 'Static'|'Dynamic',
                            'ChangeSource': 'ResourceReference'|'ParameterReference'|'ResourceAttribute'|'DirectModification'|'Automatic',
                            'CausingEntity': 'string'
                        },
                    ]
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_stack_drift_detection_status(StackDriftDetectionId=None):
    """
    Returns information about a stack drift detection operation. A stack drift detection operation detects whether a stack\'s actual configuration differs, or has drifted , from it\'s expected configuration, as defined in the stack template and any values specified as template parameters. A stack is considered to have drifted if one or more of its resources have drifted. For more information on stack and resource drift, see Detecting Unregulated Configuration Changes to Stacks and Resources .
    Use  DetectStackDrift to initiate a stack drift detection operation. DetectStackDrift returns a StackDriftDetectionId you can use to monitor the progress of the operation using DescribeStackDriftDetectionStatus . Once the drift detection operation has completed, use  DescribeStackResourceDrifts to return drift information about the stack and its resources.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_stack_drift_detection_status(
        StackDriftDetectionId='string'
    )
    
    
    :type StackDriftDetectionId: string
    :param StackDriftDetectionId: [REQUIRED]\nThe ID of the drift detection results of this operation.\nAWS CloudFormation generates new results, with a new drift detection ID, each time this operation is run. However, the number of drift results AWS CloudFormation retains for any given stack, and for how long, may vary.\n

    :rtype: dict
ReturnsResponse Syntax{
    'StackId': 'string',
    'StackDriftDetectionId': 'string',
    'StackDriftStatus': 'DRIFTED'|'IN_SYNC'|'UNKNOWN'|'NOT_CHECKED',
    'DetectionStatus': 'DETECTION_IN_PROGRESS'|'DETECTION_FAILED'|'DETECTION_COMPLETE',
    'DetectionStatusReason': 'string',
    'DriftedStackResourceCount': 123,
    'Timestamp': datetime(2015, 1, 1)
}


Response Structure

(dict) --
StackId (string) --The ID of the stack.

StackDriftDetectionId (string) --The ID of the drift detection results of this operation.
AWS CloudFormation generates new results, with a new drift detection ID, each time this operation is run. However, the number of reports AWS CloudFormation retains for any given stack, and for how long, may vary.

StackDriftStatus (string) --Status of the stack\'s actual configuration compared to its expected configuration.

DRIFTED : The stack differs from its expected template configuration. A stack is considered to have drifted if one or more of its resources have drifted.
NOT_CHECKED : AWS CloudFormation has not checked if the stack differs from its expected template configuration.
IN_SYNC : The stack\'s actual configuration matches its expected template configuration.
UNKNOWN : This value is reserved for future use.


DetectionStatus (string) --The status of the stack drift detection operation.

DETECTION_COMPLETE : The stack drift detection operation has successfully completed for all resources in the stack that support drift detection. (Resources that do not currently support stack detection remain unchecked.) If you specified logical resource IDs for AWS CloudFormation to use as a filter for the stack drift detection operation, only the resources with those logical IDs are checked for drift.
DETECTION_FAILED : The stack drift detection operation has failed for at least one resource in the stack. Results will be available for resources on which AWS CloudFormation successfully completed drift detection.
DETECTION_IN_PROGRESS : The stack drift detection operation is currently in progress.


DetectionStatusReason (string) --The reason the stack drift detection operation has its current status.

DriftedStackResourceCount (integer) --Total number of stack resources that have drifted. This is NULL until the drift detection operation reaches a status of DETECTION_COMPLETE . This value will be 0 for stacks whose drift status is IN_SYNC .

Timestamp (datetime) --Time at which the stack drift detection operation was initiated.







    :return: {
        'StackId': 'string',
        'StackDriftDetectionId': 'string',
        'StackDriftStatus': 'DRIFTED'|'IN_SYNC'|'UNKNOWN'|'NOT_CHECKED',
        'DetectionStatus': 'DETECTION_IN_PROGRESS'|'DETECTION_FAILED'|'DETECTION_COMPLETE',
        'DetectionStatusReason': 'string',
        'DriftedStackResourceCount': 123,
        'Timestamp': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    DETECTION_COMPLETE : The stack drift detection operation has successfully completed for all resources in the stack that support drift detection. (Resources that do not currently support stack detection remain unchecked.) If you specified logical resource IDs for AWS CloudFormation to use as a filter for the stack drift detection operation, only the resources with those logical IDs are checked for drift.
    DETECTION_FAILED : The stack drift detection operation has failed for at least one resource in the stack. Results will be available for resources on which AWS CloudFormation successfully completed drift detection.
    DETECTION_IN_PROGRESS : The stack drift detection operation is currently in progress.
    
    """
    pass

def describe_stack_events(StackName=None, NextToken=None):
    """
    Returns all stack related events for a specified stack in reverse chronological order. For more information about a stack\'s event history, go to Stacks in the AWS CloudFormation User Guide.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_stack_events(
        StackName='string',
        NextToken='string'
    )
    
    
    :type StackName: string
    :param StackName: The name or the unique stack ID that is associated with the stack, which are not always interchangeable:\n\nRunning stacks: You can specify either the stack\'s name or its unique stack ID.\nDeleted stacks: You must specify the unique stack ID.\n\nDefault: There is no default value.\n

    :type NextToken: string
    :param NextToken: A string that identifies the next page of events that you want to retrieve.

    :rtype: dict

ReturnsResponse Syntax
{
    'StackEvents': [
        {
            'StackId': 'string',
            'EventId': 'string',
            'StackName': 'string',
            'LogicalResourceId': 'string',
            'PhysicalResourceId': 'string',
            'ResourceType': 'string',
            'Timestamp': datetime(2015, 1, 1),
            'ResourceStatus': 'CREATE_IN_PROGRESS'|'CREATE_FAILED'|'CREATE_COMPLETE'|'DELETE_IN_PROGRESS'|'DELETE_FAILED'|'DELETE_COMPLETE'|'DELETE_SKIPPED'|'UPDATE_IN_PROGRESS'|'UPDATE_FAILED'|'UPDATE_COMPLETE'|'IMPORT_FAILED'|'IMPORT_COMPLETE'|'IMPORT_IN_PROGRESS'|'IMPORT_ROLLBACK_IN_PROGRESS'|'IMPORT_ROLLBACK_FAILED'|'IMPORT_ROLLBACK_COMPLETE',
            'ResourceStatusReason': 'string',
            'ResourceProperties': 'string',
            'ClientRequestToken': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
The output for a  DescribeStackEvents action.

StackEvents (list) --
A list of StackEvents structures.

(dict) --
The StackEvent data type.

StackId (string) --
The unique ID name of the instance of the stack.

EventId (string) --
The unique ID of this event.

StackName (string) --
The name associated with a stack.

LogicalResourceId (string) --
The logical name of the resource specified in the template.

PhysicalResourceId (string) --
The name or unique identifier associated with the physical instance of the resource.

ResourceType (string) --
Type of resource. (For more information, go to AWS Resource Types Reference in the AWS CloudFormation User Guide.)

Timestamp (datetime) --
Time the status was updated.

ResourceStatus (string) --
Current status of the resource.

ResourceStatusReason (string) --
Success/failure message associated with the resource.

ResourceProperties (string) --
BLOB of the properties used to create the resource.

ClientRequestToken (string) --
The token passed to the operation that generated this event.
All events triggered by a given stack operation are assigned the same client request token, which you can use to track operations. For example, if you execute a CreateStack operation with the token token1 , then all the StackEvents generated by that operation will have ClientRequestToken set as token1 .
In the console, stack operations display the client request token on the Events tab. Stack operations that are initiated from the console use the token format Console-StackOperation-ID , which helps you easily identify the stack operation . For example, if you create a stack using the console, each stack event would be assigned the same token in the following format: Console-CreateStack-7f59c3cf-00d2-40c7-b2ff-e75db0987002 .





NextToken (string) --
If the output exceeds 1 MB in size, a string that identifies the next page of events. If no additional page exists, this value is null.








    :return: {
        'StackEvents': [
            {
                'StackId': 'string',
                'EventId': 'string',
                'StackName': 'string',
                'LogicalResourceId': 'string',
                'PhysicalResourceId': 'string',
                'ResourceType': 'string',
                'Timestamp': datetime(2015, 1, 1),
                'ResourceStatus': 'CREATE_IN_PROGRESS'|'CREATE_FAILED'|'CREATE_COMPLETE'|'DELETE_IN_PROGRESS'|'DELETE_FAILED'|'DELETE_COMPLETE'|'DELETE_SKIPPED'|'UPDATE_IN_PROGRESS'|'UPDATE_FAILED'|'UPDATE_COMPLETE'|'IMPORT_FAILED'|'IMPORT_COMPLETE'|'IMPORT_IN_PROGRESS'|'IMPORT_ROLLBACK_IN_PROGRESS'|'IMPORT_ROLLBACK_FAILED'|'IMPORT_ROLLBACK_COMPLETE',
                'ResourceStatusReason': 'string',
                'ResourceProperties': 'string',
                'ClientRequestToken': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def describe_stack_instance(StackSetName=None, StackInstanceAccount=None, StackInstanceRegion=None):
    """
    Returns the stack instance that\'s associated with the specified stack set, AWS account, and Region.
    For a list of stack instances that are associated with a specific stack set, use  ListStackInstances .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_stack_instance(
        StackSetName='string',
        StackInstanceAccount='string',
        StackInstanceRegion='string'
    )
    
    
    :type StackSetName: string
    :param StackSetName: [REQUIRED]\nThe name or the unique stack ID of the stack set that you want to get stack instance information for.\n

    :type StackInstanceAccount: string
    :param StackInstanceAccount: [REQUIRED]\nThe ID of an AWS account that\'s associated with this stack instance.\n

    :type StackInstanceRegion: string
    :param StackInstanceRegion: [REQUIRED]\nThe name of a Region that\'s associated with this stack instance.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'StackInstance': {
        'StackSetId': 'string',
        'Region': 'string',
        'Account': 'string',
        'StackId': 'string',
        'ParameterOverrides': [
            {
                'ParameterKey': 'string',
                'ParameterValue': 'string',
                'UsePreviousValue': True|False,
                'ResolvedValue': 'string'
            },
        ],
        'Status': 'CURRENT'|'OUTDATED'|'INOPERABLE',
        'StatusReason': 'string',
        'OrganizationalUnitId': 'string',
        'DriftStatus': 'DRIFTED'|'IN_SYNC'|'UNKNOWN'|'NOT_CHECKED',
        'LastDriftCheckTimestamp': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --

StackInstance (dict) --
The stack instance that matches the specified request parameters.

StackSetId (string) --
The name or unique ID of the stack set that the stack instance is associated with.

Region (string) --
The name of the AWS Region that the stack instance is associated with.

Account (string) --
[Self-managed permissions] The name of the AWS account that the stack instance is associated with.

StackId (string) --
The ID of the stack instance.

ParameterOverrides (list) --
A list of parameters from the stack set template whose values have been overridden in this stack instance.

(dict) --
The Parameter data type.

ParameterKey (string) --
The key associated with the parameter. If you don\'t specify a key and value for a particular parameter, AWS CloudFormation uses the default value that is specified in your template.

ParameterValue (string) --
The input value associated with the parameter.

UsePreviousValue (boolean) --
During a stack update, use the existing parameter value that the stack is using for a given parameter key. If you specify true , do not specify a parameter value.

ResolvedValue (string) --
Read-only. The value that corresponds to a Systems Manager parameter key. This field is returned only for ` SSM parameter types <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html#aws-ssm-parameter-types>`__ in the template.





Status (string) --
The status of the stack instance, in terms of its synchronization with its associated stack set.

INOPERABLE : A DeleteStackInstances operation has failed and left the stack in an unstable state. Stacks in this state are excluded from further UpdateStackSet operations. You might need to perform a DeleteStackInstances operation, with RetainStacks set to true , to delete the stack instance, and then delete the stack manually.
OUTDATED : The stack isn\'t currently up to date with the stack set because:
The associated stack failed during a CreateStackSet or UpdateStackSet operation.
The stack was part of a CreateStackSet or UpdateStackSet operation that failed or was stopped before the stack was created or updated.


CURRENT : The stack is currently up to date with the stack set.


StatusReason (string) --
The explanation for the specific status code that is assigned to this stack instance.

OrganizationalUnitId (string) --
Reserved for internal use. No data returned.

DriftStatus (string) --
Status of the stack instance\'s actual configuration compared to the expected template and parameter configuration of the stack set to which it belongs.

DRIFTED : The stack differs from the expected template and parameter configuration of the stack set to which it belongs. A stack instance is considered to have drifted if one or more of the resources in the associated stack have drifted.
NOT_CHECKED : AWS CloudFormation has not checked if the stack instance differs from its expected stack set configuration.
IN_SYNC : The stack instance\'s actual configuration matches its expected stack set configuration.
UNKNOWN : This value is reserved for future use.


LastDriftCheckTimestamp (datetime) --
Most recent time when CloudFormation performed a drift detection operation on the stack instance. This value will be NULL for any stack instance on which drift detection has not yet been performed.









Exceptions

CloudFormation.Client.exceptions.StackSetNotFoundException
CloudFormation.Client.exceptions.StackInstanceNotFoundException


    :return: {
        'StackInstance': {
            'StackSetId': 'string',
            'Region': 'string',
            'Account': 'string',
            'StackId': 'string',
            'ParameterOverrides': [
                {
                    'ParameterKey': 'string',
                    'ParameterValue': 'string',
                    'UsePreviousValue': True|False,
                    'ResolvedValue': 'string'
                },
            ],
            'Status': 'CURRENT'|'OUTDATED'|'INOPERABLE',
            'StatusReason': 'string',
            'OrganizationalUnitId': 'string',
            'DriftStatus': 'DRIFTED'|'IN_SYNC'|'UNKNOWN'|'NOT_CHECKED',
            'LastDriftCheckTimestamp': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    INOPERABLE : A DeleteStackInstances operation has failed and left the stack in an unstable state. Stacks in this state are excluded from further UpdateStackSet operations. You might need to perform a DeleteStackInstances operation, with RetainStacks set to true , to delete the stack instance, and then delete the stack manually.
    OUTDATED : The stack isn\'t currently up to date with the stack set because:
    The associated stack failed during a CreateStackSet or UpdateStackSet operation.
    The stack was part of a CreateStackSet or UpdateStackSet operation that failed or was stopped before the stack was created or updated.
    
    
    CURRENT : The stack is currently up to date with the stack set.
    
    """
    pass

def describe_stack_resource(StackName=None, LogicalResourceId=None):
    """
    Returns a description of the specified resource in the specified stack.
    For deleted stacks, DescribeStackResource returns resource information for up to 90 days after the stack has been deleted.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_stack_resource(
        StackName='string',
        LogicalResourceId='string'
    )
    
    
    :type StackName: string
    :param StackName: [REQUIRED]\nThe name or the unique stack ID that is associated with the stack, which are not always interchangeable:\n\nRunning stacks: You can specify either the stack\'s name or its unique stack ID.\nDeleted stacks: You must specify the unique stack ID.\n\nDefault: There is no default value.\n

    :type LogicalResourceId: string
    :param LogicalResourceId: [REQUIRED]\nThe logical name of the resource as specified in the template.\nDefault: There is no default value.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'StackResourceDetail': {
        'StackName': 'string',
        'StackId': 'string',
        'LogicalResourceId': 'string',
        'PhysicalResourceId': 'string',
        'ResourceType': 'string',
        'LastUpdatedTimestamp': datetime(2015, 1, 1),
        'ResourceStatus': 'CREATE_IN_PROGRESS'|'CREATE_FAILED'|'CREATE_COMPLETE'|'DELETE_IN_PROGRESS'|'DELETE_FAILED'|'DELETE_COMPLETE'|'DELETE_SKIPPED'|'UPDATE_IN_PROGRESS'|'UPDATE_FAILED'|'UPDATE_COMPLETE'|'IMPORT_FAILED'|'IMPORT_COMPLETE'|'IMPORT_IN_PROGRESS'|'IMPORT_ROLLBACK_IN_PROGRESS'|'IMPORT_ROLLBACK_FAILED'|'IMPORT_ROLLBACK_COMPLETE',
        'ResourceStatusReason': 'string',
        'Description': 'string',
        'Metadata': 'string',
        'DriftInformation': {
            'StackResourceDriftStatus': 'IN_SYNC'|'MODIFIED'|'DELETED'|'NOT_CHECKED',
            'LastCheckTimestamp': datetime(2015, 1, 1)
        }
    }
}


Response Structure

(dict) --
The output for a  DescribeStackResource action.

StackResourceDetail (dict) --
A StackResourceDetail structure containing the description of the specified resource in the specified stack.

StackName (string) --
The name associated with the stack.

StackId (string) --
Unique identifier of the stack.

LogicalResourceId (string) --
The logical name of the resource specified in the template.

PhysicalResourceId (string) --
The name or unique identifier that corresponds to a physical instance ID of a resource supported by AWS CloudFormation.

ResourceType (string) --
Type of resource. ((For more information, go to AWS Resource Types Reference in the AWS CloudFormation User Guide.)

LastUpdatedTimestamp (datetime) --
Time the status was updated.

ResourceStatus (string) --
Current status of the resource.

ResourceStatusReason (string) --
Success/failure message associated with the resource.

Description (string) --
User defined description associated with the resource.

Metadata (string) --
The content of the Metadata attribute declared for the resource. For more information, see Metadata Attribute in the AWS CloudFormation User Guide.

DriftInformation (dict) --
Information about whether the resource\'s actual configuration differs, or has drifted , from its expected configuration, as defined in the stack template and any values specified as template parameters. For more information, see Detecting Unregulated Configuration Changes to Stacks and Resources .

StackResourceDriftStatus (string) --
Status of the resource\'s actual configuration compared to its expected configuration

DELETED : The resource differs from its expected configuration in that it has been deleted.
MODIFIED : The resource differs from its expected configuration.
NOT_CHECKED : AWS CloudFormation has not checked if the resource differs from its expected configuration. Any resources that do not currently support drift detection have a status of NOT_CHECKED . For more information, see Resources that Support Drift Detection .
IN_SYNC : The resources\'s actual configuration matches its expected configuration.


LastCheckTimestamp (datetime) --
When AWS CloudFormation last checked if the resource had drifted from its expected configuration.












    :return: {
        'StackResourceDetail': {
            'StackName': 'string',
            'StackId': 'string',
            'LogicalResourceId': 'string',
            'PhysicalResourceId': 'string',
            'ResourceType': 'string',
            'LastUpdatedTimestamp': datetime(2015, 1, 1),
            'ResourceStatus': 'CREATE_IN_PROGRESS'|'CREATE_FAILED'|'CREATE_COMPLETE'|'DELETE_IN_PROGRESS'|'DELETE_FAILED'|'DELETE_COMPLETE'|'DELETE_SKIPPED'|'UPDATE_IN_PROGRESS'|'UPDATE_FAILED'|'UPDATE_COMPLETE'|'IMPORT_FAILED'|'IMPORT_COMPLETE'|'IMPORT_IN_PROGRESS'|'IMPORT_ROLLBACK_IN_PROGRESS'|'IMPORT_ROLLBACK_FAILED'|'IMPORT_ROLLBACK_COMPLETE',
            'ResourceStatusReason': 'string',
            'Description': 'string',
            'Metadata': 'string',
            'DriftInformation': {
                'StackResourceDriftStatus': 'IN_SYNC'|'MODIFIED'|'DELETED'|'NOT_CHECKED',
                'LastCheckTimestamp': datetime(2015, 1, 1)
            }
        }
    }
    
    
    :returns: 
    DELETED : The resource differs from its expected configuration in that it has been deleted.
    MODIFIED : The resource differs from its expected configuration.
    NOT_CHECKED : AWS CloudFormation has not checked if the resource differs from its expected configuration. Any resources that do not currently support drift detection have a status of NOT_CHECKED . For more information, see Resources that Support Drift Detection .
    IN_SYNC : The resources\'s actual configuration matches its expected configuration.
    
    """
    pass

def describe_stack_resource_drifts(StackName=None, StackResourceDriftStatusFilters=None, NextToken=None, MaxResults=None):
    """
    Returns drift information for the resources that have been checked for drift in the specified stack. This includes actual and expected configuration values for resources where AWS CloudFormation detects configuration drift.
    For a given stack, there will be one StackResourceDrift for each stack resource that has been checked for drift. Resources that have not yet been checked for drift are not included. Resources that do not currently support drift detection are not checked, and so not included. For a list of resources that support drift detection, see Resources that Support Drift Detection .
    Use  DetectStackResourceDrift to detect drift on individual resources, or  DetectStackDrift to detect drift on all supported resources for a given stack.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_stack_resource_drifts(
        StackName='string',
        StackResourceDriftStatusFilters=[
            'IN_SYNC'|'MODIFIED'|'DELETED'|'NOT_CHECKED',
        ],
        NextToken='string',
        MaxResults=123
    )
    
    
    :type StackName: string
    :param StackName: [REQUIRED]\nThe name of the stack for which you want drift information.\n

    :type StackResourceDriftStatusFilters: list
    :param StackResourceDriftStatusFilters: The resource drift status values to use as filters for the resource drift results returned.\n\nDELETED : The resource differs from its expected template configuration in that the resource has been deleted.\nMODIFIED : One or more resource properties differ from their expected template values.\nIN_SYNC : The resources\'s actual configuration matches its expected template configuration.\nNOT_CHECKED : AWS CloudFormation does not currently return this value.\n\n\n(string) --\n\n

    :type NextToken: string
    :param NextToken: A string that identifies the next page of stack resource drift results.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a NextToken value that you can assign to the NextToken request parameter to get the next set of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'StackResourceDrifts': [
        {
            'StackId': 'string',
            'LogicalResourceId': 'string',
            'PhysicalResourceId': 'string',
            'PhysicalResourceIdContext': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'ResourceType': 'string',
            'ExpectedProperties': 'string',
            'ActualProperties': 'string',
            'PropertyDifferences': [
                {
                    'PropertyPath': 'string',
                    'ExpectedValue': 'string',
                    'ActualValue': 'string',
                    'DifferenceType': 'ADD'|'REMOVE'|'NOT_EQUAL'
                },
            ],
            'StackResourceDriftStatus': 'IN_SYNC'|'MODIFIED'|'DELETED'|'NOT_CHECKED',
            'Timestamp': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

StackResourceDrifts (list) --
Drift information for the resources that have been checked for drift in the specified stack. This includes actual and expected configuration values for resources where AWS CloudFormation detects drift.
For a given stack, there will be one StackResourceDrift for each stack resource that has been checked for drift. Resources that have not yet been checked for drift are not included. Resources that do not currently support drift detection are not checked, and so not included. For a list of resources that support drift detection, see Resources that Support Drift Detection .

(dict) --
Contains the drift information for a resource that has been checked for drift. This includes actual and expected property values for resources in which AWS CloudFormation has detected drift. Only resource properties explicitly defined in the stack template are checked for drift. For more information, see Detecting Unregulated Configuration Changes to Stacks and Resources .
Resources that do not currently support drift detection cannot be checked. For a list of resources that support drift detection, see Resources that Support Drift Detection .
Use  DetectStackResourceDrift to detect drift on individual resources, or  DetectStackDrift to detect drift on all resources in a given stack that support drift detection.

StackId (string) --
The ID of the stack.

LogicalResourceId (string) --
The logical name of the resource specified in the template.

PhysicalResourceId (string) --
The name or unique identifier that corresponds to a physical instance ID of a resource supported by AWS CloudFormation.

PhysicalResourceIdContext (list) --
Context information that enables AWS CloudFormation to uniquely identify a resource. AWS CloudFormation uses context key-value pairs in cases where a resource\'s logical and physical IDs are not enough to uniquely identify that resource. Each context key-value pair specifies a unique resource that contains the targeted resource.

(dict) --
Context information that enables AWS CloudFormation to uniquely identify a resource. AWS CloudFormation uses context key-value pairs in cases where a resource\'s logical and physical IDs are not enough to uniquely identify that resource. Each context key-value pair specifies a resource that contains the targeted resource.

Key (string) --
The resource context key.

Value (string) --
The resource context value.





ResourceType (string) --
The type of the resource.

ExpectedProperties (string) --
A JSON structure containing the expected property values of the stack resource, as defined in the stack template and any values specified as template parameters.
For resources whose StackResourceDriftStatus is DELETED , this structure will not be present.

ActualProperties (string) --
A JSON structure containing the actual property values of the stack resource.
For resources whose StackResourceDriftStatus is DELETED , this structure will not be present.

PropertyDifferences (list) --
A collection of the resource properties whose actual values differ from their expected values. These will be present only for resources whose StackResourceDriftStatus is MODIFIED .

(dict) --
Information about a resource property whose actual value differs from its expected value, as defined in the stack template and any values specified as template parameters. These will be present only for resources whose StackResourceDriftStatus is MODIFIED . For more information, see Detecting Unregulated Configuration Changes to Stacks and Resources .

PropertyPath (string) --
The fully-qualified path to the resource property.

ExpectedValue (string) --
The expected property value of the resource property, as defined in the stack template and any values specified as template parameters.

ActualValue (string) --
The actual property value of the resource property.

DifferenceType (string) --
The type of property difference.

ADD : A value has been added to a resource property that is an array or list data type.
REMOVE : The property has been removed from the current resource configuration.
NOT_EQUAL : The current property value differs from its expected value (as defined in the stack template and any values specified as template parameters).






StackResourceDriftStatus (string) --
Status of the resource\'s actual configuration compared to its expected configuration

DELETED : The resource differs from its expected template configuration because the resource has been deleted.
MODIFIED : One or more resource properties differ from their expected values (as defined in the stack template and any values specified as template parameters).
IN_SYNC : The resources\'s actual configuration matches its expected template configuration.
NOT_CHECKED : AWS CloudFormation does not currently return this value.


Timestamp (datetime) --
Time at which AWS CloudFormation performed drift detection on the stack resource.





NextToken (string) --
If the request doesn\'t return all of the remaining results, NextToken is set to a token. To retrieve the next set of results, call DescribeStackResourceDrifts again and assign that token to the request object\'s NextToken parameter. If the request returns all results, NextToken is set to null .








    :return: {
        'StackResourceDrifts': [
            {
                'StackId': 'string',
                'LogicalResourceId': 'string',
                'PhysicalResourceId': 'string',
                'PhysicalResourceIdContext': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],
                'ResourceType': 'string',
                'ExpectedProperties': 'string',
                'ActualProperties': 'string',
                'PropertyDifferences': [
                    {
                        'PropertyPath': 'string',
                        'ExpectedValue': 'string',
                        'ActualValue': 'string',
                        'DifferenceType': 'ADD'|'REMOVE'|'NOT_EQUAL'
                    },
                ],
                'StackResourceDriftStatus': 'IN_SYNC'|'MODIFIED'|'DELETED'|'NOT_CHECKED',
                'Timestamp': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    ADD : A value has been added to a resource property that is an array or list data type.
    REMOVE : The property has been removed from the current resource configuration.
    NOT_EQUAL : The current property value differs from its expected value (as defined in the stack template and any values specified as template parameters).
    
    """
    pass

def describe_stack_resources(StackName=None, LogicalResourceId=None, PhysicalResourceId=None):
    """
    Returns AWS resource descriptions for running and deleted stacks. If StackName is specified, all the associated resources that are part of the stack are returned. If PhysicalResourceId is specified, the associated resources of the stack that the resource belongs to are returned.
    For deleted stacks, DescribeStackResources returns resource information for up to 90 days after the stack has been deleted.
    You must specify either StackName or PhysicalResourceId , but not both. In addition, you can specify LogicalResourceId to filter the returned result. For more information about resources, the LogicalResourceId and PhysicalResourceId , go to the AWS CloudFormation User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.describe_stack_resources(
        StackName='string',
        LogicalResourceId='string',
        PhysicalResourceId='string'
    )
    
    
    :type StackName: string
    :param StackName: The name or the unique stack ID that is associated with the stack, which are not always interchangeable:\n\nRunning stacks: You can specify either the stack\'s name or its unique stack ID.\nDeleted stacks: You must specify the unique stack ID.\n\nDefault: There is no default value.\nRequired: Conditional. If you do not specify StackName , you must specify PhysicalResourceId .\n

    :type LogicalResourceId: string
    :param LogicalResourceId: The logical name of the resource as specified in the template.\nDefault: There is no default value.\n

    :type PhysicalResourceId: string
    :param PhysicalResourceId: The name or unique identifier that corresponds to a physical instance ID of a resource supported by AWS CloudFormation.\nFor example, for an Amazon Elastic Compute Cloud (EC2) instance, PhysicalResourceId corresponds to the InstanceId . You can pass the EC2 InstanceId to DescribeStackResources to find which stack the instance belongs to and what other resources are part of the stack.\nRequired: Conditional. If you do not specify PhysicalResourceId , you must specify StackName .\nDefault: There is no default value.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'StackResources': [
        {
            'StackName': 'string',
            'StackId': 'string',
            'LogicalResourceId': 'string',
            'PhysicalResourceId': 'string',
            'ResourceType': 'string',
            'Timestamp': datetime(2015, 1, 1),
            'ResourceStatus': 'CREATE_IN_PROGRESS'|'CREATE_FAILED'|'CREATE_COMPLETE'|'DELETE_IN_PROGRESS'|'DELETE_FAILED'|'DELETE_COMPLETE'|'DELETE_SKIPPED'|'UPDATE_IN_PROGRESS'|'UPDATE_FAILED'|'UPDATE_COMPLETE'|'IMPORT_FAILED'|'IMPORT_COMPLETE'|'IMPORT_IN_PROGRESS'|'IMPORT_ROLLBACK_IN_PROGRESS'|'IMPORT_ROLLBACK_FAILED'|'IMPORT_ROLLBACK_COMPLETE',
            'ResourceStatusReason': 'string',
            'Description': 'string',
            'DriftInformation': {
                'StackResourceDriftStatus': 'IN_SYNC'|'MODIFIED'|'DELETED'|'NOT_CHECKED',
                'LastCheckTimestamp': datetime(2015, 1, 1)
            }
        },
    ]
}


Response Structure

(dict) --
The output for a  DescribeStackResources action.

StackResources (list) --
A list of StackResource structures.

(dict) --
The StackResource data type.

StackName (string) --
The name associated with the stack.

StackId (string) --
Unique identifier of the stack.

LogicalResourceId (string) --
The logical name of the resource specified in the template.

PhysicalResourceId (string) --
The name or unique identifier that corresponds to a physical instance ID of a resource supported by AWS CloudFormation.

ResourceType (string) --
Type of resource. (For more information, go to AWS Resource Types Reference in the AWS CloudFormation User Guide.)

Timestamp (datetime) --
Time the status was updated.

ResourceStatus (string) --
Current status of the resource.

ResourceStatusReason (string) --
Success/failure message associated with the resource.

Description (string) --
User defined description associated with the resource.

DriftInformation (dict) --
Information about whether the resource\'s actual configuration differs, or has drifted , from its expected configuration, as defined in the stack template and any values specified as template parameters. For more information, see Detecting Unregulated Configuration Changes to Stacks and Resources .

StackResourceDriftStatus (string) --
Status of the resource\'s actual configuration compared to its expected configuration

DELETED : The resource differs from its expected configuration in that it has been deleted.
MODIFIED : The resource differs from its expected configuration.
NOT_CHECKED : AWS CloudFormation has not checked if the resource differs from its expected configuration. Any resources that do not currently support drift detection have a status of NOT_CHECKED . For more information, see Resources that Support Drift Detection .
IN_SYNC : The resources\'s actual configuration matches its expected configuration.


LastCheckTimestamp (datetime) --
When AWS CloudFormation last checked if the resource had drifted from its expected configuration.














    :return: {
        'StackResources': [
            {
                'StackName': 'string',
                'StackId': 'string',
                'LogicalResourceId': 'string',
                'PhysicalResourceId': 'string',
                'ResourceType': 'string',
                'Timestamp': datetime(2015, 1, 1),
                'ResourceStatus': 'CREATE_IN_PROGRESS'|'CREATE_FAILED'|'CREATE_COMPLETE'|'DELETE_IN_PROGRESS'|'DELETE_FAILED'|'DELETE_COMPLETE'|'DELETE_SKIPPED'|'UPDATE_IN_PROGRESS'|'UPDATE_FAILED'|'UPDATE_COMPLETE'|'IMPORT_FAILED'|'IMPORT_COMPLETE'|'IMPORT_IN_PROGRESS'|'IMPORT_ROLLBACK_IN_PROGRESS'|'IMPORT_ROLLBACK_FAILED'|'IMPORT_ROLLBACK_COMPLETE',
                'ResourceStatusReason': 'string',
                'Description': 'string',
                'DriftInformation': {
                    'StackResourceDriftStatus': 'IN_SYNC'|'MODIFIED'|'DELETED'|'NOT_CHECKED',
                    'LastCheckTimestamp': datetime(2015, 1, 1)
                }
            },
        ]
    }
    
    
    :returns: 
    DELETED : The resource differs from its expected configuration in that it has been deleted.
    MODIFIED : The resource differs from its expected configuration.
    NOT_CHECKED : AWS CloudFormation has not checked if the resource differs from its expected configuration. Any resources that do not currently support drift detection have a status of NOT_CHECKED . For more information, see Resources that Support Drift Detection .
    IN_SYNC : The resources\'s actual configuration matches its expected configuration.
    
    """
    pass

def describe_stack_set(StackSetName=None):
    """
    Returns the description of the specified stack set.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_stack_set(
        StackSetName='string'
    )
    
    
    :type StackSetName: string
    :param StackSetName: [REQUIRED]\nThe name or unique ID of the stack set whose description you want.\n

    :rtype: dict
ReturnsResponse Syntax{
    'StackSet': {
        'StackSetName': 'string',
        'StackSetId': 'string',
        'Description': 'string',
        'Status': 'ACTIVE'|'DELETED',
        'TemplateBody': 'string',
        'Parameters': [
            {
                'ParameterKey': 'string',
                'ParameterValue': 'string',
                'UsePreviousValue': True|False,
                'ResolvedValue': 'string'
            },
        ],
        'Capabilities': [
            'CAPABILITY_IAM'|'CAPABILITY_NAMED_IAM'|'CAPABILITY_AUTO_EXPAND',
        ],
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        'StackSetARN': 'string',
        'AdministrationRoleARN': 'string',
        'ExecutionRoleName': 'string',
        'StackSetDriftDetectionDetails': {
            'DriftStatus': 'DRIFTED'|'IN_SYNC'|'NOT_CHECKED',
            'DriftDetectionStatus': 'COMPLETED'|'FAILED'|'PARTIAL_SUCCESS'|'IN_PROGRESS'|'STOPPED',
            'LastDriftCheckTimestamp': datetime(2015, 1, 1),
            'TotalStackInstancesCount': 123,
            'DriftedStackInstancesCount': 123,
            'InSyncStackInstancesCount': 123,
            'InProgressStackInstancesCount': 123,
            'FailedStackInstancesCount': 123
        },
        'AutoDeployment': {
            'Enabled': True|False,
            'RetainStacksOnAccountRemoval': True|False
        },
        'PermissionModel': 'SERVICE_MANAGED'|'SELF_MANAGED',
        'OrganizationalUnitIds': [
            'string',
        ]
    }
}


Response Structure

(dict) --
StackSet (dict) --The specified stack set.

StackSetName (string) --The name that\'s associated with the stack set.

StackSetId (string) --The ID of the stack set.

Description (string) --A description of the stack set that you specify when the stack set is created or updated.

Status (string) --The status of the stack set.

TemplateBody (string) --The structure that contains the body of the template that was used to create or update the stack set.

Parameters (list) --A list of input parameters for a stack set.

(dict) --The Parameter data type.

ParameterKey (string) --The key associated with the parameter. If you don\'t specify a key and value for a particular parameter, AWS CloudFormation uses the default value that is specified in your template.

ParameterValue (string) --The input value associated with the parameter.

UsePreviousValue (boolean) --During a stack update, use the existing parameter value that the stack is using for a given parameter key. If you specify true , do not specify a parameter value.

ResolvedValue (string) --Read-only. The value that corresponds to a Systems Manager parameter key. This field is returned only for ` SSM parameter types <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html#aws-ssm-parameter-types>`__ in the template.





Capabilities (list) --The capabilities that are allowed in the stack set. Some stack set templates might include resources that can affect permissions in your AWS account\xe2\x80\x94for example, by creating new AWS Identity and Access Management (IAM) users. For more information, see Acknowledging IAM Resources in AWS CloudFormation Templates.

(string) --


Tags (list) --A list of tags that specify information about the stack set. A maximum number of 50 tags can be specified.

(dict) --The Tag type enables you to specify a key-value pair that can be used to store information about an AWS CloudFormation stack.

Key (string) --
Required . A string used to identify this tag. You can specify a maximum of 128 characters for a tag key. Tags owned by Amazon Web Services (AWS) have the reserved prefix: aws: .

Value (string) --
Required . A string containing the value for this tag. You can specify a maximum of 256 characters for a tag value.





StackSetARN (string) --The Amazon Resource Number (ARN) of the stack set.

AdministrationRoleARN (string) --The Amazon Resource Number (ARN) of the IAM role used to create or update the stack set.
Use customized administrator roles to control which users or groups can manage specific stack sets within the same administrator account. For more information, see Prerequisites: Granting Permissions for Stack Set Operations in the AWS CloudFormation User Guide .

ExecutionRoleName (string) --The name of the IAM execution role used to create or update the stack set.
Use customized execution roles to control which stack resources users and groups can include in their stack sets.

StackSetDriftDetectionDetails (dict) --Detailed information about the drift status of the stack set.
For stack sets, contains information about the last completed drift operation performed on the stack set. Information about drift operations currently in progress is not included.

DriftStatus (string) --Status of the stack set\'s actual configuration compared to its expected template and parameter configuration. A stack set is considered to have drifted if one or more of its stack instances have drifted from their expected template and parameter configuration.

DRIFTED : One or more of the stack instances belonging to the stack set stack differs from the expected template and parameter configuration. A stack instance is considered to have drifted if one or more of the resources in the associated stack have drifted.
NOT_CHECKED : AWS CloudFormation has not checked the stack set for drift.
IN_SYNC : All of the stack instances belonging to the stack set stack match from the expected template and parameter configuration.


DriftDetectionStatus (string) --The status of the stack set drift detection operation.

COMPLETED : The drift detection operation completed without failing on any stack instances.
FAILED : The drift detection operation exceeded the specified failure tolerance.
PARTIAL_SUCCESS : The drift detection operation completed without exceeding the failure tolerance for the operation.
IN_PROGRESS : The drift detection operation is currently being performed.
STOPPED : The user has cancelled the drift detection operation.


LastDriftCheckTimestamp (datetime) --Most recent time when CloudFormation performed a drift detection operation on the stack set. This value will be NULL for any stack set on which drift detection has not yet been performed.

TotalStackInstancesCount (integer) --The total number of stack instances belonging to this stack set.
The total number of stack instances is equal to the total of:

Stack instances that match the stack set configuration.
Stack instances that have drifted from the stack set configuration.
Stack instances where the drift detection operation has failed.
Stack instances currently being checked for drift.


DriftedStackInstancesCount (integer) --The number of stack instances that have drifted from the expected template and parameter configuration of the stack set. A stack instance is considered to have drifted if one or more of the resources in the associated stack do not match their expected configuration.

InSyncStackInstancesCount (integer) --The number of stack instances which match the expected template and parameter configuration of the stack set.

InProgressStackInstancesCount (integer) --The number of stack instances that are currently being checked for drift.

FailedStackInstancesCount (integer) --The number of stack instances for which the drift detection operation failed.



AutoDeployment (dict) --[Service-managed permissions] Describes whether StackSets automatically deploys to AWS Organizations accounts that are added to a target organization or organizational unit (OU).

Enabled (boolean) --If set to true , StackSets automatically deploys additional stack instances to AWS Organizations accounts that are added to a target organization or organizational unit (OU) in the specified Regions. If an account is removed from a target organization or OU, StackSets deletes stack instances from the account in the specified Regions.

RetainStacksOnAccountRemoval (boolean) --If set to true , stack resources are retained when an account is removed from a target organization or OU. If set to false , stack resources are deleted. Specify only if Enabled is set to True .



PermissionModel (string) --Describes how the IAM roles required for stack set operations are created.

With self-managed permissions, you must create the administrator and execution roles required to deploy to target accounts. For more information, see Grant Self-Managed Stack Set Permissions .
With service-managed permissions, StackSets automatically creates the IAM roles required to deploy to accounts managed by AWS Organizations. For more information, see Grant Service-Managed Stack Set Permissions .


OrganizationalUnitIds (list) --Reserved for internal use. No data returned.

(string) --









Exceptions

CloudFormation.Client.exceptions.StackSetNotFoundException


    :return: {
        'StackSet': {
            'StackSetName': 'string',
            'StackSetId': 'string',
            'Description': 'string',
            'Status': 'ACTIVE'|'DELETED',
            'TemplateBody': 'string',
            'Parameters': [
                {
                    'ParameterKey': 'string',
                    'ParameterValue': 'string',
                    'UsePreviousValue': True|False,
                    'ResolvedValue': 'string'
                },
            ],
            'Capabilities': [
                'CAPABILITY_IAM'|'CAPABILITY_NAMED_IAM'|'CAPABILITY_AUTO_EXPAND',
            ],
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'StackSetARN': 'string',
            'AdministrationRoleARN': 'string',
            'ExecutionRoleName': 'string',
            'StackSetDriftDetectionDetails': {
                'DriftStatus': 'DRIFTED'|'IN_SYNC'|'NOT_CHECKED',
                'DriftDetectionStatus': 'COMPLETED'|'FAILED'|'PARTIAL_SUCCESS'|'IN_PROGRESS'|'STOPPED',
                'LastDriftCheckTimestamp': datetime(2015, 1, 1),
                'TotalStackInstancesCount': 123,
                'DriftedStackInstancesCount': 123,
                'InSyncStackInstancesCount': 123,
                'InProgressStackInstancesCount': 123,
                'FailedStackInstancesCount': 123
            },
            'AutoDeployment': {
                'Enabled': True|False,
                'RetainStacksOnAccountRemoval': True|False
            },
            'PermissionModel': 'SERVICE_MANAGED'|'SELF_MANAGED',
            'OrganizationalUnitIds': [
                'string',
            ]
        }
    }
    
    
    :returns: 
    DRIFTED : One or more of the stack instances belonging to the stack set stack differs from the expected template and parameter configuration. A stack instance is considered to have drifted if one or more of the resources in the associated stack have drifted.
    NOT_CHECKED : AWS CloudFormation has not checked the stack set for drift.
    IN_SYNC : All of the stack instances belonging to the stack set stack match from the expected template and parameter configuration.
    
    """
    pass

def describe_stack_set_operation(StackSetName=None, OperationId=None):
    """
    Returns the description of the specified stack set operation.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_stack_set_operation(
        StackSetName='string',
        OperationId='string'
    )
    
    
    :type StackSetName: string
    :param StackSetName: [REQUIRED]\nThe name or the unique stack ID of the stack set for the stack operation.\n

    :type OperationId: string
    :param OperationId: [REQUIRED]\nThe unique ID of the stack set operation.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'StackSetOperation': {
        'OperationId': 'string',
        'StackSetId': 'string',
        'Action': 'CREATE'|'UPDATE'|'DELETE'|'DETECT_DRIFT',
        'Status': 'RUNNING'|'SUCCEEDED'|'FAILED'|'STOPPING'|'STOPPED'|'QUEUED',
        'OperationPreferences': {
            'RegionOrder': [
                'string',
            ],
            'FailureToleranceCount': 123,
            'FailureTolerancePercentage': 123,
            'MaxConcurrentCount': 123,
            'MaxConcurrentPercentage': 123
        },
        'RetainStacks': True|False,
        'AdministrationRoleARN': 'string',
        'ExecutionRoleName': 'string',
        'CreationTimestamp': datetime(2015, 1, 1),
        'EndTimestamp': datetime(2015, 1, 1),
        'DeploymentTargets': {
            'Accounts': [
                'string',
            ],
            'OrganizationalUnitIds': [
                'string',
            ]
        },
        'StackSetDriftDetectionDetails': {
            'DriftStatus': 'DRIFTED'|'IN_SYNC'|'NOT_CHECKED',
            'DriftDetectionStatus': 'COMPLETED'|'FAILED'|'PARTIAL_SUCCESS'|'IN_PROGRESS'|'STOPPED',
            'LastDriftCheckTimestamp': datetime(2015, 1, 1),
            'TotalStackInstancesCount': 123,
            'DriftedStackInstancesCount': 123,
            'InSyncStackInstancesCount': 123,
            'InProgressStackInstancesCount': 123,
            'FailedStackInstancesCount': 123
        }
    }
}


Response Structure

(dict) --

StackSetOperation (dict) --
The specified stack set operation.

OperationId (string) --
The unique ID of a stack set operation.

StackSetId (string) --
The ID of the stack set.

Action (string) --
The type of stack set operation: CREATE , UPDATE , or DELETE . Create and delete operations affect only the specified stack set instances that are associated with the specified stack set. Update operations affect both the stack set itself, as well as all associated stack set instances.

Status (string) --
The status of the operation.

FAILED : The operation exceeded the specified failure tolerance. The failure tolerance value that you\'ve set for an operation is applied for each Region during stack create and update operations. If the number of failed stacks within a Region exceeds the failure tolerance, the status of the operation in the Region is set to FAILED . This in turn sets the status of the operation as a whole to FAILED , and AWS CloudFormation cancels the operation in any remaining Regions.
QUEUED : [Service-managed permissions] For automatic deployments that require a sequence of operations, the operation is queued to be performed. For more information, see the stack set operation status codes in the AWS CloudFormation User Guide.
RUNNING : The operation is currently being performed.
STOPPED : The user has cancelled the operation.
STOPPING : The operation is in the process of stopping, at user request.
SUCCEEDED : The operation completed creating or updating all the specified stacks without exceeding the failure tolerance for the operation.


OperationPreferences (dict) --
The preferences for how AWS CloudFormation performs this stack set operation.

RegionOrder (list) --
The order of the Regions in where you want to perform the stack operation.

(string) --


FailureToleranceCount (integer) --
The number of accounts, per Region, for which this operation can fail before AWS CloudFormation stops the operation in that Region. If the operation is stopped in a Region, AWS CloudFormation doesn\'t attempt the operation in any subsequent Regions.
Conditional: You must specify either FailureToleranceCount or FailureTolerancePercentage (but not both).

FailureTolerancePercentage (integer) --
The percentage of accounts, per Region, for which this stack operation can fail before AWS CloudFormation stops the operation in that Region. If the operation is stopped in a Region, AWS CloudFormation doesn\'t attempt the operation in any subsequent Regions.
When calculating the number of accounts based on the specified percentage, AWS CloudFormation rounds down to the next whole number.
Conditional: You must specify either FailureToleranceCount or FailureTolerancePercentage , but not both.

MaxConcurrentCount (integer) --
The maximum number of accounts in which to perform this operation at one time. This is dependent on the value of FailureToleranceCount \xe2\x80\x94MaxConcurrentCount is at most one more than the FailureToleranceCount .
Note that this setting lets you specify the maximum for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling.
Conditional: You must specify either MaxConcurrentCount or MaxConcurrentPercentage , but not both.

MaxConcurrentPercentage (integer) --
The maximum percentage of accounts in which to perform this operation at one time.
When calculating the number of accounts based on the specified percentage, AWS CloudFormation rounds down to the next whole number. This is true except in cases where rounding down would result is zero. In this case, CloudFormation sets the number as one instead.
Note that this setting lets you specify the maximum for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling.
Conditional: You must specify either MaxConcurrentCount or MaxConcurrentPercentage , but not both.



RetainStacks (boolean) --
For stack set operations of action type DELETE , specifies whether to remove the stack instances from the specified stack set, but doesn\'t delete the stacks. You can\'t reassociate a retained stack, or add an existing, saved stack to a new stack set.

AdministrationRoleARN (string) --
The Amazon Resource Number (ARN) of the IAM role used to perform this stack set operation.
Use customized administrator roles to control which users or groups can manage specific stack sets within the same administrator account. For more information, see Define Permissions for Multiple Administrators in the AWS CloudFormation User Guide .

ExecutionRoleName (string) --
The name of the IAM execution role used to create or update the stack set.
Use customized execution roles to control which stack resources users and groups can include in their stack sets.

CreationTimestamp (datetime) --
The time at which the operation was initiated. Note that the creation times for the stack set operation might differ from the creation time of the individual stacks themselves. This is because AWS CloudFormation needs to perform preparatory work for the operation, such as dispatching the work to the requested Regions, before actually creating the first stacks.

EndTimestamp (datetime) --
The time at which the stack set operation ended, across all accounts and Regions specified. Note that this doesn\'t necessarily mean that the stack set operation was successful, or even attempted, in each account or Region.

DeploymentTargets (dict) --
[Service-managed permissions] The AWS Organizations accounts affected by the stack operation.

Accounts (list) --
The names of one or more AWS accounts for which you want to deploy stack set updates.

(string) --


OrganizationalUnitIds (list) --
The organization root ID or organizational unit (OU) IDs to which StackSets deploys.

(string) --




StackSetDriftDetectionDetails (dict) --
Detailed information about the drift status of the stack set. This includes information about drift operations currently being performed on the stack set.
this information will only be present for stack set operations whose Action type is DETECT_DRIFT .
For more information, see Detecting Unmanaged Changes in Stack Sets in the AWS CloudFormation User Guide.

DriftStatus (string) --
Status of the stack set\'s actual configuration compared to its expected template and parameter configuration. A stack set is considered to have drifted if one or more of its stack instances have drifted from their expected template and parameter configuration.

DRIFTED : One or more of the stack instances belonging to the stack set stack differs from the expected template and parameter configuration. A stack instance is considered to have drifted if one or more of the resources in the associated stack have drifted.
NOT_CHECKED : AWS CloudFormation has not checked the stack set for drift.
IN_SYNC : All of the stack instances belonging to the stack set stack match from the expected template and parameter configuration.


DriftDetectionStatus (string) --
The status of the stack set drift detection operation.

COMPLETED : The drift detection operation completed without failing on any stack instances.
FAILED : The drift detection operation exceeded the specified failure tolerance.
PARTIAL_SUCCESS : The drift detection operation completed without exceeding the failure tolerance for the operation.
IN_PROGRESS : The drift detection operation is currently being performed.
STOPPED : The user has cancelled the drift detection operation.


LastDriftCheckTimestamp (datetime) --
Most recent time when CloudFormation performed a drift detection operation on the stack set. This value will be NULL for any stack set on which drift detection has not yet been performed.

TotalStackInstancesCount (integer) --
The total number of stack instances belonging to this stack set.
The total number of stack instances is equal to the total of:

Stack instances that match the stack set configuration.
Stack instances that have drifted from the stack set configuration.
Stack instances where the drift detection operation has failed.
Stack instances currently being checked for drift.


DriftedStackInstancesCount (integer) --
The number of stack instances that have drifted from the expected template and parameter configuration of the stack set. A stack instance is considered to have drifted if one or more of the resources in the associated stack do not match their expected configuration.

InSyncStackInstancesCount (integer) --
The number of stack instances which match the expected template and parameter configuration of the stack set.

InProgressStackInstancesCount (integer) --
The number of stack instances that are currently being checked for drift.

FailedStackInstancesCount (integer) --
The number of stack instances for which the drift detection operation failed.











Exceptions

CloudFormation.Client.exceptions.StackSetNotFoundException
CloudFormation.Client.exceptions.OperationNotFoundException


    :return: {
        'StackSetOperation': {
            'OperationId': 'string',
            'StackSetId': 'string',
            'Action': 'CREATE'|'UPDATE'|'DELETE'|'DETECT_DRIFT',
            'Status': 'RUNNING'|'SUCCEEDED'|'FAILED'|'STOPPING'|'STOPPED'|'QUEUED',
            'OperationPreferences': {
                'RegionOrder': [
                    'string',
                ],
                'FailureToleranceCount': 123,
                'FailureTolerancePercentage': 123,
                'MaxConcurrentCount': 123,
                'MaxConcurrentPercentage': 123
            },
            'RetainStacks': True|False,
            'AdministrationRoleARN': 'string',
            'ExecutionRoleName': 'string',
            'CreationTimestamp': datetime(2015, 1, 1),
            'EndTimestamp': datetime(2015, 1, 1),
            'DeploymentTargets': {
                'Accounts': [
                    'string',
                ],
                'OrganizationalUnitIds': [
                    'string',
                ]
            },
            'StackSetDriftDetectionDetails': {
                'DriftStatus': 'DRIFTED'|'IN_SYNC'|'NOT_CHECKED',
                'DriftDetectionStatus': 'COMPLETED'|'FAILED'|'PARTIAL_SUCCESS'|'IN_PROGRESS'|'STOPPED',
                'LastDriftCheckTimestamp': datetime(2015, 1, 1),
                'TotalStackInstancesCount': 123,
                'DriftedStackInstancesCount': 123,
                'InSyncStackInstancesCount': 123,
                'InProgressStackInstancesCount': 123,
                'FailedStackInstancesCount': 123
            }
        }
    }
    
    
    :returns: 
    FAILED : The operation exceeded the specified failure tolerance. The failure tolerance value that you\'ve set for an operation is applied for each Region during stack create and update operations. If the number of failed stacks within a Region exceeds the failure tolerance, the status of the operation in the Region is set to FAILED . This in turn sets the status of the operation as a whole to FAILED , and AWS CloudFormation cancels the operation in any remaining Regions.
    QUEUED : [Service-managed permissions] For automatic deployments that require a sequence of operations, the operation is queued to be performed. For more information, see the stack set operation status codes in the AWS CloudFormation User Guide.
    RUNNING : The operation is currently being performed.
    STOPPED : The user has cancelled the operation.
    STOPPING : The operation is in the process of stopping, at user request.
    SUCCEEDED : The operation completed creating or updating all the specified stacks without exceeding the failure tolerance for the operation.
    
    """
    pass

def describe_stacks(StackName=None, NextToken=None):
    """
    Returns the description for the specified stack; if no stack name was specified, then it returns the description for all the stacks created.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_stacks(
        StackName='string',
        NextToken='string'
    )
    
    
    :type StackName: string
    :param StackName: The name or the unique stack ID that is associated with the stack, which are not always interchangeable:\n\nRunning stacks: You can specify either the stack\'s name or its unique stack ID.\nDeleted stacks: You must specify the unique stack ID.\n\nDefault: There is no default value.\n

    :type NextToken: string
    :param NextToken: A string that identifies the next page of stacks that you want to retrieve.

    :rtype: dict

ReturnsResponse Syntax
{
    'Stacks': [
        {
            'StackId': 'string',
            'StackName': 'string',
            'ChangeSetId': 'string',
            'Description': 'string',
            'Parameters': [
                {
                    'ParameterKey': 'string',
                    'ParameterValue': 'string',
                    'UsePreviousValue': True|False,
                    'ResolvedValue': 'string'
                },
            ],
            'CreationTime': datetime(2015, 1, 1),
            'DeletionTime': datetime(2015, 1, 1),
            'LastUpdatedTime': datetime(2015, 1, 1),
            'RollbackConfiguration': {
                'RollbackTriggers': [
                    {
                        'Arn': 'string',
                        'Type': 'string'
                    },
                ],
                'MonitoringTimeInMinutes': 123
            },
            'StackStatus': 'CREATE_IN_PROGRESS'|'CREATE_FAILED'|'CREATE_COMPLETE'|'ROLLBACK_IN_PROGRESS'|'ROLLBACK_FAILED'|'ROLLBACK_COMPLETE'|'DELETE_IN_PROGRESS'|'DELETE_FAILED'|'DELETE_COMPLETE'|'UPDATE_IN_PROGRESS'|'UPDATE_COMPLETE_CLEANUP_IN_PROGRESS'|'UPDATE_COMPLETE'|'UPDATE_ROLLBACK_IN_PROGRESS'|'UPDATE_ROLLBACK_FAILED'|'UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS'|'UPDATE_ROLLBACK_COMPLETE'|'REVIEW_IN_PROGRESS'|'IMPORT_IN_PROGRESS'|'IMPORT_COMPLETE'|'IMPORT_ROLLBACK_IN_PROGRESS'|'IMPORT_ROLLBACK_FAILED'|'IMPORT_ROLLBACK_COMPLETE',
            'StackStatusReason': 'string',
            'DisableRollback': True|False,
            'NotificationARNs': [
                'string',
            ],
            'TimeoutInMinutes': 123,
            'Capabilities': [
                'CAPABILITY_IAM'|'CAPABILITY_NAMED_IAM'|'CAPABILITY_AUTO_EXPAND',
            ],
            'Outputs': [
                {
                    'OutputKey': 'string',
                    'OutputValue': 'string',
                    'Description': 'string',
                    'ExportName': 'string'
                },
            ],
            'RoleARN': 'string',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'EnableTerminationProtection': True|False,
            'ParentId': 'string',
            'RootId': 'string',
            'DriftInformation': {
                'StackDriftStatus': 'DRIFTED'|'IN_SYNC'|'UNKNOWN'|'NOT_CHECKED',
                'LastCheckTimestamp': datetime(2015, 1, 1)
            }
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
The output for a  DescribeStacks action.

Stacks (list) --
A list of stack structures.

(dict) --
The Stack data type.

StackId (string) --
Unique identifier of the stack.

StackName (string) --
The name associated with the stack.

ChangeSetId (string) --
The unique ID of the change set.

Description (string) --
A user-defined description associated with the stack.

Parameters (list) --
A list of Parameter structures.

(dict) --
The Parameter data type.

ParameterKey (string) --
The key associated with the parameter. If you don\'t specify a key and value for a particular parameter, AWS CloudFormation uses the default value that is specified in your template.

ParameterValue (string) --
The input value associated with the parameter.

UsePreviousValue (boolean) --
During a stack update, use the existing parameter value that the stack is using for a given parameter key. If you specify true , do not specify a parameter value.

ResolvedValue (string) --
Read-only. The value that corresponds to a Systems Manager parameter key. This field is returned only for ` SSM parameter types <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html#aws-ssm-parameter-types>`__ in the template.





CreationTime (datetime) --
The time at which the stack was created.

DeletionTime (datetime) --
The time the stack was deleted.

LastUpdatedTime (datetime) --
The time the stack was last updated. This field will only be returned if the stack has been updated at least once.

RollbackConfiguration (dict) --
The rollback triggers for AWS CloudFormation to monitor during stack creation and updating operations, and for the specified monitoring period afterwards.

RollbackTriggers (list) --
The triggers to monitor during stack creation or update actions.
By default, AWS CloudFormation saves the rollback triggers specified for a stack and applies them to any subsequent update operations for the stack, unless you specify otherwise. If you do specify rollback triggers for this parameter, those triggers replace any list of triggers previously specified for the stack. This means:

To use the rollback triggers previously specified for this stack, if any, don\'t specify this parameter.
To specify new or updated rollback triggers, you must specify all the triggers that you want used for this stack, even triggers you\'ve specifed before (for example, when creating the stack or during a previous stack update). Any triggers that you don\'t include in the updated list of triggers are no longer applied to the stack.
To remove all currently specified triggers, specify an empty list for this parameter.

If a specified trigger is missing, the entire stack operation fails and is rolled back.

(dict) --
A rollback trigger AWS CloudFormation monitors during creation and updating of stacks. If any of the alarms you specify goes to ALARM state during the stack operation or within the specified monitoring period afterwards, CloudFormation rolls back the entire stack operation.

Arn (string) --
The Amazon Resource Name (ARN) of the rollback trigger.
If a specified trigger is missing, the entire stack operation fails and is rolled back.

Type (string) --
The resource type of the rollback trigger. Currently, AWS::CloudWatch::Alarm is the only supported resource type.





MonitoringTimeInMinutes (integer) --
The amount of time, in minutes, during which CloudFormation should monitor all the rollback triggers after the stack creation or update operation deploys all necessary resources.
The default is 0 minutes.
If you specify a monitoring period but do not specify any rollback triggers, CloudFormation still waits the specified period of time before cleaning up old resources after update operations. You can use this monitoring period to perform any manual stack validation desired, and manually cancel the stack creation or update (using CancelUpdateStack , for example) as necessary.
If you specify 0 for this parameter, CloudFormation still monitors the specified rollback triggers during stack creation and update operations. Then, for update operations, it begins disposing of old resources immediately once the operation completes.



StackStatus (string) --
Current status of the stack.

StackStatusReason (string) --
Success/failure message associated with the stack status.

DisableRollback (boolean) --
Boolean to enable or disable rollback on stack creation failures:

true : disable rollback
false : enable rollback


NotificationARNs (list) --
SNS topic ARNs to which stack related events are published.

(string) --


TimeoutInMinutes (integer) --
The amount of time within which stack creation should complete.

Capabilities (list) --
The capabilities allowed in the stack.

(string) --


Outputs (list) --
A list of output structures.

(dict) --
The Output data type.

OutputKey (string) --
The key associated with the output.

OutputValue (string) --
The value associated with the output.

Description (string) --
User defined description associated with the output.

ExportName (string) --
The name of the export associated with the output.





RoleARN (string) --
The Amazon Resource Name (ARN) of an AWS Identity and Access Management (IAM) role that is associated with the stack. During a stack operation, AWS CloudFormation uses this role\'s credentials to make calls on your behalf.

Tags (list) --
A list of Tag s that specify information about the stack.

(dict) --
The Tag type enables you to specify a key-value pair that can be used to store information about an AWS CloudFormation stack.

Key (string) --

Required . A string used to identify this tag. You can specify a maximum of 128 characters for a tag key. Tags owned by Amazon Web Services (AWS) have the reserved prefix: aws: .


Value (string) --

Required . A string containing the value for this tag. You can specify a maximum of 256 characters for a tag value.






EnableTerminationProtection (boolean) --
Whether termination protection is enabled for the stack.
For nested stacks , termination protection is set on the root stack and cannot be changed directly on the nested stack. For more information, see Protecting a Stack From Being Deleted in the AWS CloudFormation User Guide .

ParentId (string) --
For nested stacks--stacks created as resources for another stack--the stack ID of the direct parent of this stack. For the first level of nested stacks, the root stack is also the parent stack.
For more information, see Working with Nested Stacks in the AWS CloudFormation User Guide .

RootId (string) --
For nested stacks--stacks created as resources for another stack--the stack ID of the top-level stack to which the nested stack ultimately belongs.
For more information, see Working with Nested Stacks in the AWS CloudFormation User Guide .

DriftInformation (dict) --
Information on whether a stack\'s actual configuration differs, or has drifted , from it\'s expected configuration, as defined in the stack template and any values specified as template parameters. For more information, see Detecting Unregulated Configuration Changes to Stacks and Resources .

StackDriftStatus (string) --
Status of the stack\'s actual configuration compared to its expected template configuration.

DRIFTED : The stack differs from its expected template configuration. A stack is considered to have drifted if one or more of its resources have drifted.
NOT_CHECKED : AWS CloudFormation has not checked if the stack differs from its expected template configuration.
IN_SYNC : The stack\'s actual configuration matches its expected template configuration.
UNKNOWN : This value is reserved for future use.


LastCheckTimestamp (datetime) --
Most recent time when a drift detection operation was initiated on the stack, or any of its individual resources that support drift detection.







NextToken (string) --
If the output exceeds 1 MB in size, a string that identifies the next page of stacks. If no additional page exists, this value is null.








    :return: {
        'Stacks': [
            {
                'StackId': 'string',
                'StackName': 'string',
                'ChangeSetId': 'string',
                'Description': 'string',
                'Parameters': [
                    {
                        'ParameterKey': 'string',
                        'ParameterValue': 'string',
                        'UsePreviousValue': True|False,
                        'ResolvedValue': 'string'
                    },
                ],
                'CreationTime': datetime(2015, 1, 1),
                'DeletionTime': datetime(2015, 1, 1),
                'LastUpdatedTime': datetime(2015, 1, 1),
                'RollbackConfiguration': {
                    'RollbackTriggers': [
                        {
                            'Arn': 'string',
                            'Type': 'string'
                        },
                    ],
                    'MonitoringTimeInMinutes': 123
                },
                'StackStatus': 'CREATE_IN_PROGRESS'|'CREATE_FAILED'|'CREATE_COMPLETE'|'ROLLBACK_IN_PROGRESS'|'ROLLBACK_FAILED'|'ROLLBACK_COMPLETE'|'DELETE_IN_PROGRESS'|'DELETE_FAILED'|'DELETE_COMPLETE'|'UPDATE_IN_PROGRESS'|'UPDATE_COMPLETE_CLEANUP_IN_PROGRESS'|'UPDATE_COMPLETE'|'UPDATE_ROLLBACK_IN_PROGRESS'|'UPDATE_ROLLBACK_FAILED'|'UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS'|'UPDATE_ROLLBACK_COMPLETE'|'REVIEW_IN_PROGRESS'|'IMPORT_IN_PROGRESS'|'IMPORT_COMPLETE'|'IMPORT_ROLLBACK_IN_PROGRESS'|'IMPORT_ROLLBACK_FAILED'|'IMPORT_ROLLBACK_COMPLETE',
                'StackStatusReason': 'string',
                'DisableRollback': True|False,
                'NotificationARNs': [
                    'string',
                ],
                'TimeoutInMinutes': 123,
                'Capabilities': [
                    'CAPABILITY_IAM'|'CAPABILITY_NAMED_IAM'|'CAPABILITY_AUTO_EXPAND',
                ],
                'Outputs': [
                    {
                        'OutputKey': 'string',
                        'OutputValue': 'string',
                        'Description': 'string',
                        'ExportName': 'string'
                    },
                ],
                'RoleARN': 'string',
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],
                'EnableTerminationProtection': True|False,
                'ParentId': 'string',
                'RootId': 'string',
                'DriftInformation': {
                    'StackDriftStatus': 'DRIFTED'|'IN_SYNC'|'UNKNOWN'|'NOT_CHECKED',
                    'LastCheckTimestamp': datetime(2015, 1, 1)
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    To use the rollback triggers previously specified for this stack, if any, don\'t specify this parameter.
    To specify new or updated rollback triggers, you must specify all the triggers that you want used for this stack, even triggers you\'ve specifed before (for example, when creating the stack or during a previous stack update). Any triggers that you don\'t include in the updated list of triggers are no longer applied to the stack.
    To remove all currently specified triggers, specify an empty list for this parameter.
    
    """
    pass

def describe_type(Type=None, TypeName=None, Arn=None, VersionId=None):
    """
    Returns detailed information about a type that has been registered.
    If you specify a VersionId , DescribeType returns information about that specific type version. Otherwise, it returns information about the default type version.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_type(
        Type='RESOURCE',
        TypeName='string',
        Arn='string',
        VersionId='string'
    )
    
    
    :type Type: string
    :param Type: The kind of type.\nCurrently the only valid value is RESOURCE .\nConditional: You must specify either TypeName and Type , or Arn .\n

    :type TypeName: string
    :param TypeName: The name of the type.\nConditional: You must specify either TypeName and Type , or Arn .\n

    :type Arn: string
    :param Arn: The Amazon Resource Name (ARN) of the type.\nConditional: You must specify either TypeName and Type , or Arn .\n

    :type VersionId: string
    :param VersionId: The ID of a specific version of the type. The version ID is the value at the end of the Amazon Resource Name (ARN) assigned to the type version when it is registered.\nIf you specify a VersionId , DescribeType returns information about that specific type version. Otherwise, it returns information about the default type version.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Arn': 'string',
    'Type': 'RESOURCE',
    'TypeName': 'string',
    'DefaultVersionId': 'string',
    'IsDefaultVersion': True|False,
    'Description': 'string',
    'Schema': 'string',
    'ProvisioningType': 'NON_PROVISIONABLE'|'IMMUTABLE'|'FULLY_MUTABLE',
    'DeprecatedStatus': 'LIVE'|'DEPRECATED',
    'LoggingConfig': {
        'LogRoleArn': 'string',
        'LogGroupName': 'string'
    },
    'ExecutionRoleArn': 'string',
    'Visibility': 'PUBLIC'|'PRIVATE',
    'SourceUrl': 'string',
    'DocumentationUrl': 'string',
    'LastUpdated': datetime(2015, 1, 1),
    'TimeCreated': datetime(2015, 1, 1)
}


Response Structure

(dict) --

Arn (string) --
The Amazon Resource Name (ARN) of the type.

Type (string) --
The kind of type.
Currently the only valid value is RESOURCE .

TypeName (string) --
The name of the registered type.

DefaultVersionId (string) --
The ID of the default version of the type. The default version is used when the type version is not specified.
To set the default version of a type, use ``  SetTypeDefaultVersion `` .

IsDefaultVersion (boolean) --
Whether the specified type version is set as the default version.

Description (string) --
The description of the registered type.

Schema (string) --
The schema that defines the type.
For more information on type schemas, see Resource Provider Schema in the CloudFormation CLI User Guide .

ProvisioningType (string) --
The provisioning behavior of the type. AWS CloudFormation determines the provisioning type during registration, based on the types of handlers in the schema handler package submitted.
Valid values include:

FULLY_MUTABLE : The type includes an update handler to process updates to the type during stack update operations.
IMMUTABLE : The type does not include an update handler, so the type cannot be updated and must instead be replaced during stack update operations.
NON_PROVISIONABLE : The type does not include all of the following handlers, and therefore cannot actually be provisioned.
create
read
delete




DeprecatedStatus (string) --
The deprecation status of the type.
Valid values include:

LIVE : The type is registered and can be used in CloudFormation operations, dependent on its provisioning behavior and visibility scope.
DEPRECATED : The type has been deregistered and can no longer be used in CloudFormation operations.


LoggingConfig (dict) --
Contains logging configuration information for a type.

LogRoleArn (string) --
The ARN of the role that CloudFormation should assume when sending log entries to CloudWatch logs.

LogGroupName (string) --
The Amazon CloudWatch log group to which CloudFormation sends error logging information when invoking the type\'s handlers.



ExecutionRoleArn (string) --
The Amazon Resource Name (ARN) of the IAM execution role used to register the type. If your resource type calls AWS APIs in any of its handlers, you must create an * IAM execution role * that includes the necessary permissions to call those AWS APIs, and provision that execution role in your account. CloudFormation then assumes that execution role to provide your resource type with the appropriate credentials.

Visibility (string) --
The scope at which the type is visible and usable in CloudFormation operations.
Valid values include:

PRIVATE : The type is only visible and usable within the account in which it is registered. Currently, AWS CloudFormation marks any types you register as PRIVATE .
PUBLIC : The type is publically visible and usable within any Amazon account.


SourceUrl (string) --
The URL of the source code for the type.

DocumentationUrl (string) --
The URL of a page providing detailed documentation for this type.

LastUpdated (datetime) --
When the specified type version was registered.

TimeCreated (datetime) --
When the specified type version was registered.







Exceptions

CloudFormation.Client.exceptions.CFNRegistryException
CloudFormation.Client.exceptions.TypeNotFoundException


    :return: {
        'Arn': 'string',
        'Type': 'RESOURCE',
        'TypeName': 'string',
        'DefaultVersionId': 'string',
        'IsDefaultVersion': True|False,
        'Description': 'string',
        'Schema': 'string',
        'ProvisioningType': 'NON_PROVISIONABLE'|'IMMUTABLE'|'FULLY_MUTABLE',
        'DeprecatedStatus': 'LIVE'|'DEPRECATED',
        'LoggingConfig': {
            'LogRoleArn': 'string',
            'LogGroupName': 'string'
        },
        'ExecutionRoleArn': 'string',
        'Visibility': 'PUBLIC'|'PRIVATE',
        'SourceUrl': 'string',
        'DocumentationUrl': 'string',
        'LastUpdated': datetime(2015, 1, 1),
        'TimeCreated': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    FULLY_MUTABLE : The type includes an update handler to process updates to the type during stack update operations.
    IMMUTABLE : The type does not include an update handler, so the type cannot be updated and must instead be replaced during stack update operations.
    NON_PROVISIONABLE : The type does not include all of the following handlers, and therefore cannot actually be provisioned.
    create
    read
    delete
    
    
    
    """
    pass

def describe_type_registration(RegistrationToken=None):
    """
    Returns information about a type\'s registration, including its current status and type and version identifiers.
    When you initiate a registration request using ``  RegisterType `` , you can then use ``  DescribeTypeRegistration `` to monitor the progress of that registration request.
    Once the registration request has completed, use ``  DescribeType `` to return detailed informaiton about a type.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_type_registration(
        RegistrationToken='string'
    )
    
    
    :type RegistrationToken: string
    :param RegistrationToken: [REQUIRED]\nThe identifier for this registration request.\nThis registration token is generated by CloudFormation when you initiate a registration request using `` RegisterType `` .\n

    :rtype: dict
ReturnsResponse Syntax{
    'ProgressStatus': 'COMPLETE'|'IN_PROGRESS'|'FAILED',
    'Description': 'string',
    'TypeArn': 'string',
    'TypeVersionArn': 'string'
}


Response Structure

(dict) --
ProgressStatus (string) --The current status of the type registration request.

Description (string) --The description of the type registration request.

TypeArn (string) --The Amazon Resource Name (ARN) of the type being registered.
For registration requests with a ProgressStatus of other than COMPLETE , this will be null .

TypeVersionArn (string) --The Amazon Resource Name (ARN) of this specific version of the type being registered.
For registration requests with a ProgressStatus of other than COMPLETE , this will be null .






Exceptions

CloudFormation.Client.exceptions.CFNRegistryException


    :return: {
        'ProgressStatus': 'COMPLETE'|'IN_PROGRESS'|'FAILED',
        'Description': 'string',
        'TypeArn': 'string',
        'TypeVersionArn': 'string'
    }
    
    
    """
    pass

def detect_stack_drift(StackName=None, LogicalResourceIds=None):
    """
    Detects whether a stack\'s actual configuration differs, or has drifted , from it\'s expected configuration, as defined in the stack template and any values specified as template parameters. For each resource in the stack that supports drift detection, AWS CloudFormation compares the actual configuration of the resource with its expected template configuration. Only resource properties explicitly defined in the stack template are checked for drift. A stack is considered to have drifted if one or more of its resources differ from their expected template configurations. For more information, see Detecting Unregulated Configuration Changes to Stacks and Resources .
    Use DetectStackDrift to detect drift on all supported resources for a given stack, or  DetectStackResourceDrift to detect drift on individual resources.
    For a list of stack resources that currently support drift detection, see Resources that Support Drift Detection .
    When detecting drift on a stack, AWS CloudFormation does not detect drift on any nested stacks belonging to that stack. Perform DetectStackDrift directly on the nested stack itself.
    See also: AWS API Documentation
    
    
    :example: response = client.detect_stack_drift(
        StackName='string',
        LogicalResourceIds=[
            'string',
        ]
    )
    
    
    :type StackName: string
    :param StackName: [REQUIRED]\nThe name of the stack for which you want to detect drift.\n

    :type LogicalResourceIds: list
    :param LogicalResourceIds: The logical names of any resources you want to use as filters.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'StackDriftDetectionId': 'string'
}


Response Structure

(dict) --

StackDriftDetectionId (string) --
The ID of the drift detection results of this operation.
AWS CloudFormation generates new results, with a new drift detection ID, each time this operation is run. However, the number of drift results AWS CloudFormation retains for any given stack, and for how long, may vary.








    :return: {
        'StackDriftDetectionId': 'string'
    }
    
    
    """
    pass

def detect_stack_resource_drift(StackName=None, LogicalResourceId=None):
    """
    Returns information about whether a resource\'s actual configuration differs, or has drifted , from it\'s expected configuration, as defined in the stack template and any values specified as template parameters. This information includes actual and expected property values for resources in which AWS CloudFormation detects drift. Only resource properties explicitly defined in the stack template are checked for drift. For more information about stack and resource drift, see Detecting Unregulated Configuration Changes to Stacks and Resources .
    Use DetectStackResourceDrift to detect drift on individual resources, or  DetectStackDrift to detect drift on all resources in a given stack that support drift detection.
    Resources that do not currently support drift detection cannot be checked. For a list of resources that support drift detection, see Resources that Support Drift Detection .
    See also: AWS API Documentation
    
    
    :example: response = client.detect_stack_resource_drift(
        StackName='string',
        LogicalResourceId='string'
    )
    
    
    :type StackName: string
    :param StackName: [REQUIRED]\nThe name of the stack to which the resource belongs.\n

    :type LogicalResourceId: string
    :param LogicalResourceId: [REQUIRED]\nThe logical name of the resource for which to return drift information.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'StackResourceDrift': {
        'StackId': 'string',
        'LogicalResourceId': 'string',
        'PhysicalResourceId': 'string',
        'PhysicalResourceIdContext': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        'ResourceType': 'string',
        'ExpectedProperties': 'string',
        'ActualProperties': 'string',
        'PropertyDifferences': [
            {
                'PropertyPath': 'string',
                'ExpectedValue': 'string',
                'ActualValue': 'string',
                'DifferenceType': 'ADD'|'REMOVE'|'NOT_EQUAL'
            },
        ],
        'StackResourceDriftStatus': 'IN_SYNC'|'MODIFIED'|'DELETED'|'NOT_CHECKED',
        'Timestamp': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --

StackResourceDrift (dict) --
Information about whether the resource\'s actual configuration has drifted from its expected template configuration, including actual and expected property values and any differences detected.

StackId (string) --
The ID of the stack.

LogicalResourceId (string) --
The logical name of the resource specified in the template.

PhysicalResourceId (string) --
The name or unique identifier that corresponds to a physical instance ID of a resource supported by AWS CloudFormation.

PhysicalResourceIdContext (list) --
Context information that enables AWS CloudFormation to uniquely identify a resource. AWS CloudFormation uses context key-value pairs in cases where a resource\'s logical and physical IDs are not enough to uniquely identify that resource. Each context key-value pair specifies a unique resource that contains the targeted resource.

(dict) --
Context information that enables AWS CloudFormation to uniquely identify a resource. AWS CloudFormation uses context key-value pairs in cases where a resource\'s logical and physical IDs are not enough to uniquely identify that resource. Each context key-value pair specifies a resource that contains the targeted resource.

Key (string) --
The resource context key.

Value (string) --
The resource context value.





ResourceType (string) --
The type of the resource.

ExpectedProperties (string) --
A JSON structure containing the expected property values of the stack resource, as defined in the stack template and any values specified as template parameters.
For resources whose StackResourceDriftStatus is DELETED , this structure will not be present.

ActualProperties (string) --
A JSON structure containing the actual property values of the stack resource.
For resources whose StackResourceDriftStatus is DELETED , this structure will not be present.

PropertyDifferences (list) --
A collection of the resource properties whose actual values differ from their expected values. These will be present only for resources whose StackResourceDriftStatus is MODIFIED .

(dict) --
Information about a resource property whose actual value differs from its expected value, as defined in the stack template and any values specified as template parameters. These will be present only for resources whose StackResourceDriftStatus is MODIFIED . For more information, see Detecting Unregulated Configuration Changes to Stacks and Resources .

PropertyPath (string) --
The fully-qualified path to the resource property.

ExpectedValue (string) --
The expected property value of the resource property, as defined in the stack template and any values specified as template parameters.

ActualValue (string) --
The actual property value of the resource property.

DifferenceType (string) --
The type of property difference.

ADD : A value has been added to a resource property that is an array or list data type.
REMOVE : The property has been removed from the current resource configuration.
NOT_EQUAL : The current property value differs from its expected value (as defined in the stack template and any values specified as template parameters).






StackResourceDriftStatus (string) --
Status of the resource\'s actual configuration compared to its expected configuration

DELETED : The resource differs from its expected template configuration because the resource has been deleted.
MODIFIED : One or more resource properties differ from their expected values (as defined in the stack template and any values specified as template parameters).
IN_SYNC : The resources\'s actual configuration matches its expected template configuration.
NOT_CHECKED : AWS CloudFormation does not currently return this value.


Timestamp (datetime) --
Time at which AWS CloudFormation performed drift detection on the stack resource.










    :return: {
        'StackResourceDrift': {
            'StackId': 'string',
            'LogicalResourceId': 'string',
            'PhysicalResourceId': 'string',
            'PhysicalResourceIdContext': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'ResourceType': 'string',
            'ExpectedProperties': 'string',
            'ActualProperties': 'string',
            'PropertyDifferences': [
                {
                    'PropertyPath': 'string',
                    'ExpectedValue': 'string',
                    'ActualValue': 'string',
                    'DifferenceType': 'ADD'|'REMOVE'|'NOT_EQUAL'
                },
            ],
            'StackResourceDriftStatus': 'IN_SYNC'|'MODIFIED'|'DELETED'|'NOT_CHECKED',
            'Timestamp': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    ADD : A value has been added to a resource property that is an array or list data type.
    REMOVE : The property has been removed from the current resource configuration.
    NOT_EQUAL : The current property value differs from its expected value (as defined in the stack template and any values specified as template parameters).
    
    """
    pass

def detect_stack_set_drift(StackSetName=None, OperationPreferences=None, OperationId=None):
    """
    Detect drift on a stack set. When CloudFormation performs drift detection on a stack set, it performs drift detection on the stack associated with each stack instance in the stack set. For more information, see How CloudFormation Performs Drift Detection on a Stack Set .
    Once the operation has completed, use the following actions to return drift information:
    For more information on performing a drift detection operation on a stack set, see Detecting Unmanaged Changes in Stack Sets .
    You can only run a single drift detection operation on a given stack set at one time.
    To stop a drift detection stack set operation, use ``  StopStackSetOperation `` .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.detect_stack_set_drift(
        StackSetName='string',
        OperationPreferences={
            'RegionOrder': [
                'string',
            ],
            'FailureToleranceCount': 123,
            'FailureTolerancePercentage': 123,
            'MaxConcurrentCount': 123,
            'MaxConcurrentPercentage': 123
        },
        OperationId='string'
    )
    
    
    :type StackSetName: string
    :param StackSetName: [REQUIRED]\nThe name of the stack set on which to perform the drift detection operation.\n

    :type OperationPreferences: dict
    :param OperationPreferences: The user-specified preferences for how AWS CloudFormation performs a stack set operation.\nFor more information on maximum concurrent accounts and failure tolerance, see Stack set operation options .\n\nRegionOrder (list) --The order of the Regions in where you want to perform the stack operation.\n\n(string) --\n\n\nFailureToleranceCount (integer) --The number of accounts, per Region, for which this operation can fail before AWS CloudFormation stops the operation in that Region. If the operation is stopped in a Region, AWS CloudFormation doesn\'t attempt the operation in any subsequent Regions.\nConditional: You must specify either FailureToleranceCount or FailureTolerancePercentage (but not both).\n\nFailureTolerancePercentage (integer) --The percentage of accounts, per Region, for which this stack operation can fail before AWS CloudFormation stops the operation in that Region. If the operation is stopped in a Region, AWS CloudFormation doesn\'t attempt the operation in any subsequent Regions.\nWhen calculating the number of accounts based on the specified percentage, AWS CloudFormation rounds down to the next whole number.\nConditional: You must specify either FailureToleranceCount or FailureTolerancePercentage , but not both.\n\nMaxConcurrentCount (integer) --The maximum number of accounts in which to perform this operation at one time. This is dependent on the value of FailureToleranceCount \xe2\x80\x94MaxConcurrentCount is at most one more than the FailureToleranceCount .\nNote that this setting lets you specify the maximum for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling.\nConditional: You must specify either MaxConcurrentCount or MaxConcurrentPercentage , but not both.\n\nMaxConcurrentPercentage (integer) --The maximum percentage of accounts in which to perform this operation at one time.\nWhen calculating the number of accounts based on the specified percentage, AWS CloudFormation rounds down to the next whole number. This is true except in cases where rounding down would result is zero. In this case, CloudFormation sets the number as one instead.\nNote that this setting lets you specify the maximum for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling.\nConditional: You must specify either MaxConcurrentCount or MaxConcurrentPercentage , but not both.\n\n\n

    :type OperationId: string
    :param OperationId: \nThe ID of the stack set operation.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'OperationId': 'string'
}


Response Structure

(dict) --

OperationId (string) --
The ID of the drift detection stack set operation.
you can use this operation id with ``  DescribeStackSetOperation `` to monitor the progress of the drift detection operation.







Exceptions

CloudFormation.Client.exceptions.InvalidOperationException
CloudFormation.Client.exceptions.OperationInProgressException
CloudFormation.Client.exceptions.StackSetNotFoundException


    :return: {
        'OperationId': 'string'
    }
    
    
    :returns: 
    StackSetName (string) -- [REQUIRED]
    The name of the stack set on which to perform the drift detection operation.
    
    OperationPreferences (dict) -- The user-specified preferences for how AWS CloudFormation performs a stack set operation.
    For more information on maximum concurrent accounts and failure tolerance, see Stack set operation options .
    
    RegionOrder (list) --The order of the Regions in where you want to perform the stack operation.
    
    (string) --
    
    
    FailureToleranceCount (integer) --The number of accounts, per Region, for which this operation can fail before AWS CloudFormation stops the operation in that Region. If the operation is stopped in a Region, AWS CloudFormation doesn\'t attempt the operation in any subsequent Regions.
    Conditional: You must specify either FailureToleranceCount or FailureTolerancePercentage (but not both).
    
    FailureTolerancePercentage (integer) --The percentage of accounts, per Region, for which this stack operation can fail before AWS CloudFormation stops the operation in that Region. If the operation is stopped in a Region, AWS CloudFormation doesn\'t attempt the operation in any subsequent Regions.
    When calculating the number of accounts based on the specified percentage, AWS CloudFormation rounds down to the next whole number.
    Conditional: You must specify either FailureToleranceCount or FailureTolerancePercentage , but not both.
    
    MaxConcurrentCount (integer) --The maximum number of accounts in which to perform this operation at one time. This is dependent on the value of FailureToleranceCount \xe2\x80\x94MaxConcurrentCount is at most one more than the FailureToleranceCount .
    Note that this setting lets you specify the maximum for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling.
    Conditional: You must specify either MaxConcurrentCount or MaxConcurrentPercentage , but not both.
    
    MaxConcurrentPercentage (integer) --The maximum percentage of accounts in which to perform this operation at one time.
    When calculating the number of accounts based on the specified percentage, AWS CloudFormation rounds down to the next whole number. This is true except in cases where rounding down would result is zero. In this case, CloudFormation sets the number as one instead.
    Note that this setting lets you specify the maximum for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling.
    Conditional: You must specify either MaxConcurrentCount or MaxConcurrentPercentage , but not both.
    
    
    
    OperationId (string) -- 
    The ID of the stack set operation.
    This field is autopopulated if not provided.
    
    
    """
    pass

def estimate_template_cost(TemplateBody=None, TemplateURL=None, Parameters=None):
    """
    Returns the estimated monthly cost of a template. The return value is an AWS Simple Monthly Calculator URL with a query string that describes the resources required to run the template.
    See also: AWS API Documentation
    
    
    :example: response = client.estimate_template_cost(
        TemplateBody='string',
        TemplateURL='string',
        Parameters=[
            {
                'ParameterKey': 'string',
                'ParameterValue': 'string',
                'UsePreviousValue': True|False,
                'ResolvedValue': 'string'
            },
        ]
    )
    
    
    :type TemplateBody: string
    :param TemplateBody: Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes. (For more information, go to Template Anatomy in the AWS CloudFormation User Guide.)\nConditional: You must pass TemplateBody or TemplateURL . If both are passed, only TemplateBody is used.\n

    :type TemplateURL: string
    :param TemplateURL: Location of file containing the template body. The URL must point to a template that is located in an Amazon S3 bucket. For more information, go to Template Anatomy in the AWS CloudFormation User Guide.\nConditional: You must pass TemplateURL or TemplateBody . If both are passed, only TemplateBody is used.\n

    :type Parameters: list
    :param Parameters: A list of Parameter structures that specify input parameters.\n\n(dict) --The Parameter data type.\n\nParameterKey (string) --The key associated with the parameter. If you don\'t specify a key and value for a particular parameter, AWS CloudFormation uses the default value that is specified in your template.\n\nParameterValue (string) --The input value associated with the parameter.\n\nUsePreviousValue (boolean) --During a stack update, use the existing parameter value that the stack is using for a given parameter key. If you specify true , do not specify a parameter value.\n\nResolvedValue (string) --Read-only. The value that corresponds to a Systems Manager parameter key. This field is returned only for ` SSM parameter types <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html#aws-ssm-parameter-types>`__ in the template.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Url': 'string'
}


Response Structure

(dict) --
The output for a  EstimateTemplateCost action.

Url (string) --
An AWS Simple Monthly Calculator URL with a query string that describes the resources required to run the template.








    :return: {
        'Url': 'string'
    }
    
    
    """
    pass

def execute_change_set(ChangeSetName=None, StackName=None, ClientRequestToken=None):
    """
    Updates a stack using the input information that was provided when the specified change set was created. After the call successfully completes, AWS CloudFormation starts updating the stack. Use the  DescribeStacks action to view the status of the update.
    When you execute a change set, AWS CloudFormation deletes all other change sets associated with the stack because they aren\'t valid for the updated stack.
    If a stack policy is associated with the stack, AWS CloudFormation enforces the policy during the update. You can\'t specify a temporary stack policy that overrides the current policy.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.execute_change_set(
        ChangeSetName='string',
        StackName='string',
        ClientRequestToken='string'
    )
    
    
    :type ChangeSetName: string
    :param ChangeSetName: [REQUIRED]\nThe name or ARN of the change set that you want use to update the specified stack.\n

    :type StackName: string
    :param StackName: If you specified the name of a change set, specify the stack name or ID (ARN) that is associated with the change set you want to execute.

    :type ClientRequestToken: string
    :param ClientRequestToken: A unique identifier for this ExecuteChangeSet request. Specify this token if you plan to retry requests so that AWS CloudFormation knows that you\'re not attempting to execute a change set to update a stack with the same name. You might retry ExecuteChangeSet requests to ensure that AWS CloudFormation successfully received them.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
The output for the  ExecuteChangeSet action.





Exceptions

CloudFormation.Client.exceptions.InvalidChangeSetStatusException
CloudFormation.Client.exceptions.ChangeSetNotFoundException
CloudFormation.Client.exceptions.InsufficientCapabilitiesException
CloudFormation.Client.exceptions.TokenAlreadyExistsException


    :return: {}
    
    
    :returns: 
    CloudFormation.Client.exceptions.InvalidChangeSetStatusException
    CloudFormation.Client.exceptions.ChangeSetNotFoundException
    CloudFormation.Client.exceptions.InsufficientCapabilitiesException
    CloudFormation.Client.exceptions.TokenAlreadyExistsException
    
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

def get_stack_policy(StackName=None):
    """
    Returns the stack policy for a specified stack. If a stack doesn\'t have a policy, a null value is returned.
    See also: AWS API Documentation
    
    
    :example: response = client.get_stack_policy(
        StackName='string'
    )
    
    
    :type StackName: string
    :param StackName: [REQUIRED]\nThe name or unique stack ID that is associated with the stack whose policy you want to get.\n

    :rtype: dict
ReturnsResponse Syntax{
    'StackPolicyBody': 'string'
}


Response Structure

(dict) --The output for the  GetStackPolicy action.

StackPolicyBody (string) --Structure containing the stack policy body. (For more information, go to Prevent Updates to Stack Resources in the AWS CloudFormation User Guide.)







    :return: {
        'StackPolicyBody': 'string'
    }
    
    
    """
    pass

def get_template(StackName=None, ChangeSetName=None, TemplateStage=None):
    """
    Returns the template body for a specified stack. You can get the template for running or deleted stacks.
    For deleted stacks, GetTemplate returns the template for up to 90 days after the stack has been deleted.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_template(
        StackName='string',
        ChangeSetName='string',
        TemplateStage='Original'|'Processed'
    )
    
    
    :type StackName: string
    :param StackName: The name or the unique stack ID that is associated with the stack, which are not always interchangeable:\n\nRunning stacks: You can specify either the stack\'s name or its unique stack ID.\nDeleted stacks: You must specify the unique stack ID.\n\nDefault: There is no default value.\n

    :type ChangeSetName: string
    :param ChangeSetName: The name or Amazon Resource Name (ARN) of a change set for which AWS CloudFormation returns the associated template. If you specify a name, you must also specify the StackName .

    :type TemplateStage: string
    :param TemplateStage: For templates that include transforms, the stage of the template that AWS CloudFormation returns. To get the user-submitted template, specify Original . To get the template after AWS CloudFormation has processed all transforms, specify Processed .\nIf the template doesn\'t include transforms, Original and Processed return the same template. By default, AWS CloudFormation specifies Original .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'TemplateBody': {},
    'StagesAvailable': [
        'Original'|'Processed',
    ]
}


Response Structure

(dict) --
The output for  GetTemplate action.

TemplateBody (dict) --
Structure containing the template body. (For more information, go to Template Anatomy in the AWS CloudFormation User Guide.)
AWS CloudFormation returns the same template that was used when the stack was created.

StagesAvailable (list) --
The stage of the template that you can retrieve. For stacks, the Original and Processed templates are always available. For change sets, the Original template is always available. After AWS CloudFormation finishes creating the change set, the Processed template becomes available.

(string) --








Exceptions

CloudFormation.Client.exceptions.ChangeSetNotFoundException


    :return: {
        'TemplateBody': {},
        'StagesAvailable': [
            'Original'|'Processed',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_template_summary(TemplateBody=None, TemplateURL=None, StackName=None, StackSetName=None):
    """
    Returns information about a new or existing template. The GetTemplateSummary action is useful for viewing parameter information, such as default parameter values and parameter types, before you create or update a stack or stack set.
    You can use the GetTemplateSummary action when you submit a template, or you can get template information for a stack set, or a running or deleted stack.
    For deleted stacks, GetTemplateSummary returns the template information for up to 90 days after the stack has been deleted. If the template does not exist, a ValidationError is returned.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_template_summary(
        TemplateBody='string',
        TemplateURL='string',
        StackName='string',
        StackSetName='string'
    )
    
    
    :type TemplateBody: string
    :param TemplateBody: Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes. For more information about templates, see Template Anatomy in the AWS CloudFormation User Guide.\nConditional: You must specify only one of the following parameters: StackName , StackSetName , TemplateBody , or TemplateURL .\n

    :type TemplateURL: string
    :param TemplateURL: Location of file containing the template body. The URL must point to a template (max size: 460,800 bytes) that is located in an Amazon S3 bucket. For more information about templates, see Template Anatomy in the AWS CloudFormation User Guide.\nConditional: You must specify only one of the following parameters: StackName , StackSetName , TemplateBody , or TemplateURL .\n

    :type StackName: string
    :param StackName: The name or the stack ID that is associated with the stack, which are not always interchangeable. For running stacks, you can specify either the stack\'s name or its unique stack ID. For deleted stack, you must specify the unique stack ID.\nConditional: You must specify only one of the following parameters: StackName , StackSetName , TemplateBody , or TemplateURL .\n

    :type StackSetName: string
    :param StackSetName: The name or unique ID of the stack set from which the stack was created.\nConditional: You must specify only one of the following parameters: StackName , StackSetName , TemplateBody , or TemplateURL .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Parameters': [
        {
            'ParameterKey': 'string',
            'DefaultValue': 'string',
            'ParameterType': 'string',
            'NoEcho': True|False,
            'Description': 'string',
            'ParameterConstraints': {
                'AllowedValues': [
                    'string',
                ]
            }
        },
    ],
    'Description': 'string',
    'Capabilities': [
        'CAPABILITY_IAM'|'CAPABILITY_NAMED_IAM'|'CAPABILITY_AUTO_EXPAND',
    ],
    'CapabilitiesReason': 'string',
    'ResourceTypes': [
        'string',
    ],
    'Version': 'string',
    'Metadata': 'string',
    'DeclaredTransforms': [
        'string',
    ],
    'ResourceIdentifierSummaries': [
        {
            'ResourceType': 'string',
            'LogicalResourceIds': [
                'string',
            ],
            'ResourceIdentifiers': [
                'string',
            ]
        },
    ]
}


Response Structure

(dict) --
The output for the  GetTemplateSummary action.

Parameters (list) --
A list of parameter declarations that describe various properties for each parameter.

(dict) --
The ParameterDeclaration data type.

ParameterKey (string) --
The name that is associated with the parameter.

DefaultValue (string) --
The default value of the parameter.

ParameterType (string) --
The type of parameter.

NoEcho (boolean) --
Flag that indicates whether the parameter value is shown as plain text in logs and in the AWS Management Console.

Description (string) --
The description that is associate with the parameter.

ParameterConstraints (dict) --
The criteria that AWS CloudFormation uses to validate parameter values.

AllowedValues (list) --
A list of values that are permitted for a parameter.

(string) --








Description (string) --
The value that is defined in the Description property of the template.

Capabilities (list) --
The capabilities found within the template. If your template contains IAM resources, you must specify the CAPABILITY_IAM or CAPABILITY_NAMED_IAM value for this parameter when you use the  CreateStack or  UpdateStack actions with your template; otherwise, those actions return an InsufficientCapabilities error.
For more information, see Acknowledging IAM Resources in AWS CloudFormation Templates .

(string) --


CapabilitiesReason (string) --
The list of resources that generated the values in the Capabilities response element.

ResourceTypes (list) --
A list of all the template resource types that are defined in the template, such as AWS::EC2::Instance , AWS::Dynamo::Table , and Custom::MyCustomInstance .

(string) --


Version (string) --
The AWS template format version, which identifies the capabilities of the template.

Metadata (string) --
The value that is defined for the Metadata property of the template.

DeclaredTransforms (list) --
A list of the transforms that are declared in the template.

(string) --


ResourceIdentifierSummaries (list) --
A list of resource identifier summaries that describe the target resources of an import operation and the properties you can provide during the import to identify the target resources. For example, BucketName is a possible identifier property for an AWS::S3::Bucket resource.

(dict) --
Describes the target resources of a specific type in your import template (for example, all AWS::S3::Bucket resources) and the properties you can provide during the import to identify resources of that type.

ResourceType (string) --
The template resource type of the target resources, such as AWS::S3::Bucket .

LogicalResourceIds (list) --
The logical IDs of the target resources of the specified ResourceType , as defined in the import template.

(string) --


ResourceIdentifiers (list) --
The resource properties you can provide during the import to identify your target resources. For example, BucketName is a possible identifier property for AWS::S3::Bucket resources.

(string) --












Exceptions

CloudFormation.Client.exceptions.StackSetNotFoundException


    :return: {
        'Parameters': [
            {
                'ParameterKey': 'string',
                'DefaultValue': 'string',
                'ParameterType': 'string',
                'NoEcho': True|False,
                'Description': 'string',
                'ParameterConstraints': {
                    'AllowedValues': [
                        'string',
                    ]
                }
            },
        ],
        'Description': 'string',
        'Capabilities': [
            'CAPABILITY_IAM'|'CAPABILITY_NAMED_IAM'|'CAPABILITY_AUTO_EXPAND',
        ],
        'CapabilitiesReason': 'string',
        'ResourceTypes': [
            'string',
        ],
        'Version': 'string',
        'Metadata': 'string',
        'DeclaredTransforms': [
            'string',
        ],
        'ResourceIdentifierSummaries': [
            {
                'ResourceType': 'string',
                'LogicalResourceIds': [
                    'string',
                ],
                'ResourceIdentifiers': [
                    'string',
                ]
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
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

def list_change_sets(StackName=None, NextToken=None):
    """
    Returns the ID and status of each active change set for a stack. For example, AWS CloudFormation lists change sets that are in the CREATE_IN_PROGRESS or CREATE_PENDING state.
    See also: AWS API Documentation
    
    
    :example: response = client.list_change_sets(
        StackName='string',
        NextToken='string'
    )
    
    
    :type StackName: string
    :param StackName: [REQUIRED]\nThe name or the Amazon Resource Name (ARN) of the stack for which you want to list change sets.\n

    :type NextToken: string
    :param NextToken: A string (provided by the ListChangeSets response output) that identifies the next page of change sets that you want to retrieve.

    :rtype: dict

ReturnsResponse Syntax
{
    'Summaries': [
        {
            'StackId': 'string',
            'StackName': 'string',
            'ChangeSetId': 'string',
            'ChangeSetName': 'string',
            'ExecutionStatus': 'UNAVAILABLE'|'AVAILABLE'|'EXECUTE_IN_PROGRESS'|'EXECUTE_COMPLETE'|'EXECUTE_FAILED'|'OBSOLETE',
            'Status': 'CREATE_PENDING'|'CREATE_IN_PROGRESS'|'CREATE_COMPLETE'|'DELETE_COMPLETE'|'FAILED',
            'StatusReason': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'Description': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
The output for the  ListChangeSets action.

Summaries (list) --
A list of ChangeSetSummary structures that provides the ID and status of each change set for the specified stack.

(dict) --
The ChangeSetSummary structure describes a change set, its status, and the stack with which it\'s associated.

StackId (string) --
The ID of the stack with which the change set is associated.

StackName (string) --
The name of the stack with which the change set is associated.

ChangeSetId (string) --
The ID of the change set.

ChangeSetName (string) --
The name of the change set.

ExecutionStatus (string) --
If the change set execution status is AVAILABLE , you can execute the change set. If you can\xe2\x80\x99t execute the change set, the status indicates why. For example, a change set might be in an UNAVAILABLE state because AWS CloudFormation is still creating it or in an OBSOLETE state because the stack was already updated.

Status (string) --
The state of the change set, such as CREATE_IN_PROGRESS , CREATE_COMPLETE , or FAILED .

StatusReason (string) --
A description of the change set\'s status. For example, if your change set is in the FAILED state, AWS CloudFormation shows the error message.

CreationTime (datetime) --
The start time when the change set was created, in UTC.

Description (string) --
Descriptive information about the change set.





NextToken (string) --
If the output exceeds 1 MB, a string that identifies the next page of change sets. If there is no additional page, this value is null.








    :return: {
        'Summaries': [
            {
                'StackId': 'string',
                'StackName': 'string',
                'ChangeSetId': 'string',
                'ChangeSetName': 'string',
                'ExecutionStatus': 'UNAVAILABLE'|'AVAILABLE'|'EXECUTE_IN_PROGRESS'|'EXECUTE_COMPLETE'|'EXECUTE_FAILED'|'OBSOLETE',
                'Status': 'CREATE_PENDING'|'CREATE_IN_PROGRESS'|'CREATE_COMPLETE'|'DELETE_COMPLETE'|'FAILED',
                'StatusReason': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'Description': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_exports(NextToken=None):
    """
    Lists all exported output values in the account and Region in which you call this action. Use this action to see the exported output values that you can import into other stacks. To import values, use the ` Fn::ImportValue https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-importvalue.html`__ function.
    For more information, see AWS CloudFormation Export Stack Output Values .
    See also: AWS API Documentation
    
    
    :example: response = client.list_exports(
        NextToken='string'
    )
    
    
    :type NextToken: string
    :param NextToken: A string (provided by the ListExports response output) that identifies the next page of exported output values that you asked to retrieve.

    :rtype: dict
ReturnsResponse Syntax{
    'Exports': [
        {
            'ExportingStackId': 'string',
            'Name': 'string',
            'Value': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
Exports (list) --The output for the  ListExports action.

(dict) --The Export structure describes the exported output values for a stack.

ExportingStackId (string) --The stack that contains the exported output name and value.

Name (string) --The name of exported output value. Use this name and the Fn::ImportValue function to import the associated value into other stacks. The name is defined in the Export field in the associated stack\'s Outputs section.

Value (string) --The value of the exported output, such as a resource physical ID. This value is defined in the Export field in the associated stack\'s Outputs section.





NextToken (string) --If the output exceeds 100 exported output values, a string that identifies the next page of exports. If there is no additional page, this value is null.







    :return: {
        'Exports': [
            {
                'ExportingStackId': 'string',
                'Name': 'string',
                'Value': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_imports(ExportName=None, NextToken=None):
    """
    Lists all stacks that are importing an exported output value. To modify or remove an exported output value, first use this action to see which stacks are using it. To see the exported output values in your account, see  ListExports .
    For more information about importing an exported output value, see the ` Fn::ImportValue https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-importvalue.html`__ function.
    See also: AWS API Documentation
    
    
    :example: response = client.list_imports(
        ExportName='string',
        NextToken='string'
    )
    
    
    :type ExportName: string
    :param ExportName: [REQUIRED]\nThe name of the exported output value. AWS CloudFormation returns the stack names that are importing this value.\n

    :type NextToken: string
    :param NextToken: A string (provided by the ListImports response output) that identifies the next page of stacks that are importing the specified exported output value.

    :rtype: dict

ReturnsResponse Syntax
{
    'Imports': [
        'string',
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Imports (list) --
A list of stack names that are importing the specified exported output value.

(string) --


NextToken (string) --
A string that identifies the next page of exports. If there is no additional page, this value is null.








    :return: {
        'Imports': [
            'string',
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_stack_instances(StackSetName=None, NextToken=None, MaxResults=None, StackInstanceAccount=None, StackInstanceRegion=None):
    """
    Returns summary information about stack instances that are associated with the specified stack set. You can filter for stack instances that are associated with a specific AWS account name or Region.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_stack_instances(
        StackSetName='string',
        NextToken='string',
        MaxResults=123,
        StackInstanceAccount='string',
        StackInstanceRegion='string'
    )
    
    
    :type StackSetName: string
    :param StackSetName: [REQUIRED]\nThe name or unique ID of the stack set that you want to list stack instances for.\n

    :type NextToken: string
    :param NextToken: If the previous request didn\'t return all of the remaining results, the response\'s NextToken parameter value is set to a token. To retrieve the next set of results, call ListStackInstances again and assign that token to the request object\'s NextToken parameter. If there are no remaining results, the previous response object\'s NextToken parameter is set to null .

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a NextToken value that you can assign to the NextToken request parameter to get the next set of results.

    :type StackInstanceAccount: string
    :param StackInstanceAccount: The name of the AWS account that you want to list stack instances for.

    :type StackInstanceRegion: string
    :param StackInstanceRegion: The name of the Region where you want to list stack instances.

    :rtype: dict

ReturnsResponse Syntax
{
    'Summaries': [
        {
            'StackSetId': 'string',
            'Region': 'string',
            'Account': 'string',
            'StackId': 'string',
            'Status': 'CURRENT'|'OUTDATED'|'INOPERABLE',
            'StatusReason': 'string',
            'OrganizationalUnitId': 'string',
            'DriftStatus': 'DRIFTED'|'IN_SYNC'|'UNKNOWN'|'NOT_CHECKED',
            'LastDriftCheckTimestamp': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Summaries (list) --
A list of StackInstanceSummary structures that contain information about the specified stack instances.

(dict) --
The structure that contains summary information about a stack instance.

StackSetId (string) --
The name or unique ID of the stack set that the stack instance is associated with.

Region (string) --
The name of the AWS Region that the stack instance is associated with.

Account (string) --
[Self-managed permissions] The name of the AWS account that the stack instance is associated with.

StackId (string) --
The ID of the stack instance.

Status (string) --
The status of the stack instance, in terms of its synchronization with its associated stack set.

INOPERABLE : A DeleteStackInstances operation has failed and left the stack in an unstable state. Stacks in this state are excluded from further UpdateStackSet operations. You might need to perform a DeleteStackInstances operation, with RetainStacks set to true , to delete the stack instance, and then delete the stack manually.
OUTDATED : The stack isn\'t currently up to date with the stack set because:
The associated stack failed during a CreateStackSet or UpdateStackSet operation.
The stack was part of a CreateStackSet or UpdateStackSet operation that failed or was stopped before the stack was created or updated.


CURRENT : The stack is currently up to date with the stack set.


StatusReason (string) --
The explanation for the specific status code assigned to this stack instance.

OrganizationalUnitId (string) --
Reserved for internal use. No data returned.

DriftStatus (string) --
Status of the stack instance\'s actual configuration compared to the expected template and parameter configuration of the stack set to which it belongs.

DRIFTED : The stack differs from the expected template and parameter configuration of the stack set to which it belongs. A stack instance is considered to have drifted if one or more of the resources in the associated stack have drifted.
NOT_CHECKED : AWS CloudFormation has not checked if the stack instance differs from its expected stack set configuration.
IN_SYNC : The stack instance\'s actual configuration matches its expected stack set configuration.
UNKNOWN : This value is reserved for future use.


LastDriftCheckTimestamp (datetime) --
Most recent time when CloudFormation performed a drift detection operation on the stack instance. This value will be NULL for any stack instance on which drift detection has not yet been performed.





NextToken (string) --
If the request doesn\'t return all of the remaining results, NextToken is set to a token. To retrieve the next set of results, call ListStackInstances again and assign that token to the request object\'s NextToken parameter. If the request returns all results, NextToken is set to null .







Exceptions

CloudFormation.Client.exceptions.StackSetNotFoundException


    :return: {
        'Summaries': [
            {
                'StackSetId': 'string',
                'Region': 'string',
                'Account': 'string',
                'StackId': 'string',
                'Status': 'CURRENT'|'OUTDATED'|'INOPERABLE',
                'StatusReason': 'string',
                'OrganizationalUnitId': 'string',
                'DriftStatus': 'DRIFTED'|'IN_SYNC'|'UNKNOWN'|'NOT_CHECKED',
                'LastDriftCheckTimestamp': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    INOPERABLE : A DeleteStackInstances operation has failed and left the stack in an unstable state. Stacks in this state are excluded from further UpdateStackSet operations. You might need to perform a DeleteStackInstances operation, with RetainStacks set to true , to delete the stack instance, and then delete the stack manually.
    OUTDATED : The stack isn\'t currently up to date with the stack set because:
    The associated stack failed during a CreateStackSet or UpdateStackSet operation.
    The stack was part of a CreateStackSet or UpdateStackSet operation that failed or was stopped before the stack was created or updated.
    
    
    CURRENT : The stack is currently up to date with the stack set.
    
    """
    pass

def list_stack_resources(StackName=None, NextToken=None):
    """
    Returns descriptions of all resources of the specified stack.
    For deleted stacks, ListStackResources returns resource information for up to 90 days after the stack has been deleted.
    See also: AWS API Documentation
    
    
    :example: response = client.list_stack_resources(
        StackName='string',
        NextToken='string'
    )
    
    
    :type StackName: string
    :param StackName: [REQUIRED]\nThe name or the unique stack ID that is associated with the stack, which are not always interchangeable:\n\nRunning stacks: You can specify either the stack\'s name or its unique stack ID.\nDeleted stacks: You must specify the unique stack ID.\n\nDefault: There is no default value.\n

    :type NextToken: string
    :param NextToken: A string that identifies the next page of stack resources that you want to retrieve.

    :rtype: dict

ReturnsResponse Syntax
{
    'StackResourceSummaries': [
        {
            'LogicalResourceId': 'string',
            'PhysicalResourceId': 'string',
            'ResourceType': 'string',
            'LastUpdatedTimestamp': datetime(2015, 1, 1),
            'ResourceStatus': 'CREATE_IN_PROGRESS'|'CREATE_FAILED'|'CREATE_COMPLETE'|'DELETE_IN_PROGRESS'|'DELETE_FAILED'|'DELETE_COMPLETE'|'DELETE_SKIPPED'|'UPDATE_IN_PROGRESS'|'UPDATE_FAILED'|'UPDATE_COMPLETE'|'IMPORT_FAILED'|'IMPORT_COMPLETE'|'IMPORT_IN_PROGRESS'|'IMPORT_ROLLBACK_IN_PROGRESS'|'IMPORT_ROLLBACK_FAILED'|'IMPORT_ROLLBACK_COMPLETE',
            'ResourceStatusReason': 'string',
            'DriftInformation': {
                'StackResourceDriftStatus': 'IN_SYNC'|'MODIFIED'|'DELETED'|'NOT_CHECKED',
                'LastCheckTimestamp': datetime(2015, 1, 1)
            }
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
The output for a  ListStackResources action.

StackResourceSummaries (list) --
A list of StackResourceSummary structures.

(dict) --
Contains high-level information about the specified stack resource.

LogicalResourceId (string) --
The logical name of the resource specified in the template.

PhysicalResourceId (string) --
The name or unique identifier that corresponds to a physical instance ID of the resource.

ResourceType (string) --
Type of resource. (For more information, go to AWS Resource Types Reference in the AWS CloudFormation User Guide.)

LastUpdatedTimestamp (datetime) --
Time the status was updated.

ResourceStatus (string) --
Current status of the resource.

ResourceStatusReason (string) --
Success/failure message associated with the resource.

DriftInformation (dict) --
Information about whether the resource\'s actual configuration differs, or has drifted , from its expected configuration, as defined in the stack template and any values specified as template parameters. For more information, see Detecting Unregulated Configuration Changes to Stacks and Resources .

StackResourceDriftStatus (string) --
Status of the resource\'s actual configuration compared to its expected configuration

DELETED : The resource differs from its expected configuration in that it has been deleted.
MODIFIED : The resource differs from its expected configuration.
NOT_CHECKED : AWS CloudFormation has not checked if the resource differs from its expected configuration. Any resources that do not currently support drift detection have a status of NOT_CHECKED . For more information, see Resources that Support Drift Detection . If you performed an  ContinueUpdateRollback operation on a stack, any resources included in ResourcesToSkip will also have a status of NOT_CHECKED . For more information on skipping resources during rollback operations, see Continue Rolling Back an Update in the AWS CloudFormation User Guide.
IN_SYNC : The resources\'s actual configuration matches its expected configuration.


LastCheckTimestamp (datetime) --
When AWS CloudFormation last checked if the resource had drifted from its expected configuration.







NextToken (string) --
If the output exceeds 1 MB, a string that identifies the next page of stack resources. If no additional page exists, this value is null.








    :return: {
        'StackResourceSummaries': [
            {
                'LogicalResourceId': 'string',
                'PhysicalResourceId': 'string',
                'ResourceType': 'string',
                'LastUpdatedTimestamp': datetime(2015, 1, 1),
                'ResourceStatus': 'CREATE_IN_PROGRESS'|'CREATE_FAILED'|'CREATE_COMPLETE'|'DELETE_IN_PROGRESS'|'DELETE_FAILED'|'DELETE_COMPLETE'|'DELETE_SKIPPED'|'UPDATE_IN_PROGRESS'|'UPDATE_FAILED'|'UPDATE_COMPLETE'|'IMPORT_FAILED'|'IMPORT_COMPLETE'|'IMPORT_IN_PROGRESS'|'IMPORT_ROLLBACK_IN_PROGRESS'|'IMPORT_ROLLBACK_FAILED'|'IMPORT_ROLLBACK_COMPLETE',
                'ResourceStatusReason': 'string',
                'DriftInformation': {
                    'StackResourceDriftStatus': 'IN_SYNC'|'MODIFIED'|'DELETED'|'NOT_CHECKED',
                    'LastCheckTimestamp': datetime(2015, 1, 1)
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    DELETED : The resource differs from its expected configuration in that it has been deleted.
    MODIFIED : The resource differs from its expected configuration.
    NOT_CHECKED : AWS CloudFormation has not checked if the resource differs from its expected configuration. Any resources that do not currently support drift detection have a status of NOT_CHECKED . For more information, see Resources that Support Drift Detection . If you performed an  ContinueUpdateRollback operation on a stack, any resources included in ResourcesToSkip will also have a status of NOT_CHECKED . For more information on skipping resources during rollback operations, see Continue Rolling Back an Update in the AWS CloudFormation User Guide.
    IN_SYNC : The resources\'s actual configuration matches its expected configuration.
    
    """
    pass

def list_stack_set_operation_results(StackSetName=None, OperationId=None, NextToken=None, MaxResults=None):
    """
    Returns summary information about the results of a stack set operation.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_stack_set_operation_results(
        StackSetName='string',
        OperationId='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type StackSetName: string
    :param StackSetName: [REQUIRED]\nThe name or unique ID of the stack set that you want to get operation results for.\n

    :type OperationId: string
    :param OperationId: [REQUIRED]\nThe ID of the stack set operation.\n

    :type NextToken: string
    :param NextToken: If the previous request didn\'t return all of the remaining results, the response object\'s NextToken parameter value is set to a token. To retrieve the next set of results, call ListStackSetOperationResults again and assign that token to the request object\'s NextToken parameter. If there are no remaining results, the previous response object\'s NextToken parameter is set to null .

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a NextToken value that you can assign to the NextToken request parameter to get the next set of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'Summaries': [
        {
            'Account': 'string',
            'Region': 'string',
            'Status': 'PENDING'|'RUNNING'|'SUCCEEDED'|'FAILED'|'CANCELLED',
            'StatusReason': 'string',
            'AccountGateResult': {
                'Status': 'SUCCEEDED'|'FAILED'|'SKIPPED',
                'StatusReason': 'string'
            },
            'OrganizationalUnitId': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Summaries (list) --
A list of StackSetOperationResultSummary structures that contain information about the specified operation results, for accounts and Regions that are included in the operation.

(dict) --
The structure that contains information about a specified operation\'s results for a given account in a given Region.

Account (string) --
[Self-managed permissions] The name of the AWS account for this operation result.

Region (string) --
The name of the AWS Region for this operation result.

Status (string) --
The result status of the stack set operation for the given account in the given Region.

CANCELLED : The operation in the specified account and Region has been cancelled. This is either because a user has stopped the stack set operation, or because the failure tolerance of the stack set operation has been exceeded.
FAILED : The operation in the specified account and Region failed.  If the stack set operation fails in enough accounts within a Region, the failure tolerance for the stack set operation as a whole might be exceeded.
RUNNING : The operation in the specified account and Region is currently in progress.
PENDING : The operation in the specified account and Region has yet to start.
SUCCEEDED : The operation in the specified account and Region completed successfully.


StatusReason (string) --
The reason for the assigned result status.

AccountGateResult (dict) --
The results of the account gate function AWS CloudFormation invokes, if present, before proceeding with stack set operations in an account

Status (string) --
The status of the account gate function.

SUCCEEDED : The account gate function has determined that the account and Region passes any requirements for a stack set operation to occur. AWS CloudFormation proceeds with the stack operation in that account and Region.
FAILED : The account gate function has determined that the account and Region does not meet the requirements for a stack set operation to occur. AWS CloudFormation cancels the stack set operation in that account and Region, and sets the stack set operation result status for that account and Region to FAILED .
SKIPPED : AWS CloudFormation has skipped calling the account gate function for this account and Region, for one of the following reasons:
An account gate function has not been specified for the account and Region. AWS CloudFormation proceeds with the stack set operation in this account and Region.
The AWSCloudFormationStackSetExecutionRole of the stack set adminstration account lacks permissions to invoke the function. AWS CloudFormation proceeds with the stack set operation in this account and Region.
Either no action is necessary, or no action is possible, on the stack. AWS CloudFormation skips the stack set operation in this account and Region.




StatusReason (string) --
The reason for the account gate status assigned to this account and Region for the stack set operation.



OrganizationalUnitId (string) --
Reserved for internal use. No data returned.





NextToken (string) --
If the request doesn\'t return all results, NextToken is set to a token. To retrieve the next set of results, call ListOperationResults again and assign that token to the request object\'s NextToken parameter. If there are no remaining results, NextToken is set to null .







Exceptions

CloudFormation.Client.exceptions.StackSetNotFoundException
CloudFormation.Client.exceptions.OperationNotFoundException


    :return: {
        'Summaries': [
            {
                'Account': 'string',
                'Region': 'string',
                'Status': 'PENDING'|'RUNNING'|'SUCCEEDED'|'FAILED'|'CANCELLED',
                'StatusReason': 'string',
                'AccountGateResult': {
                    'Status': 'SUCCEEDED'|'FAILED'|'SKIPPED',
                    'StatusReason': 'string'
                },
                'OrganizationalUnitId': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    CANCELLED : The operation in the specified account and Region has been cancelled. This is either because a user has stopped the stack set operation, or because the failure tolerance of the stack set operation has been exceeded.
    FAILED : The operation in the specified account and Region failed.  If the stack set operation fails in enough accounts within a Region, the failure tolerance for the stack set operation as a whole might be exceeded.
    RUNNING : The operation in the specified account and Region is currently in progress.
    PENDING : The operation in the specified account and Region has yet to start.
    SUCCEEDED : The operation in the specified account and Region completed successfully.
    
    """
    pass

def list_stack_set_operations(StackSetName=None, NextToken=None, MaxResults=None):
    """
    Returns summary information about operations performed on a stack set.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_stack_set_operations(
        StackSetName='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type StackSetName: string
    :param StackSetName: [REQUIRED]\nThe name or unique ID of the stack set that you want to get operation summaries for.\n

    :type NextToken: string
    :param NextToken: If the previous paginated request didn\'t return all of the remaining results, the response object\'s NextToken parameter value is set to a token. To retrieve the next set of results, call ListStackSetOperations again and assign that token to the request object\'s NextToken parameter. If there are no remaining results, the previous response object\'s NextToken parameter is set to null .

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a NextToken value that you can assign to the NextToken request parameter to get the next set of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'Summaries': [
        {
            'OperationId': 'string',
            'Action': 'CREATE'|'UPDATE'|'DELETE'|'DETECT_DRIFT',
            'Status': 'RUNNING'|'SUCCEEDED'|'FAILED'|'STOPPING'|'STOPPED'|'QUEUED',
            'CreationTimestamp': datetime(2015, 1, 1),
            'EndTimestamp': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Summaries (list) --
A list of StackSetOperationSummary structures that contain summary information about operations for the specified stack set.

(dict) --
The structures that contain summary information about the specified operation.

OperationId (string) --
The unique ID of the stack set operation.

Action (string) --
The type of operation: CREATE , UPDATE , or DELETE . Create and delete operations affect only the specified stack instances that are associated with the specified stack set. Update operations affect both the stack set itself as well as all associated stack set instances.

Status (string) --
The overall status of the operation.

FAILED : The operation exceeded the specified failure tolerance. The failure tolerance value that you\'ve set for an operation is applied for each Region during stack create and update operations. If the number of failed stacks within a Region exceeds the failure tolerance, the status of the operation in the Region is set to FAILED . This in turn sets the status of the operation as a whole to FAILED , and AWS CloudFormation cancels the operation in any remaining Regions.
QUEUED : [Service-managed permissions] For automatic deployments that require a sequence of operations, the operation is queued to be performed. For more information, see the stack set operation status codes in the AWS CloudFormation User Guide.
RUNNING : The operation is currently being performed.
STOPPED : The user has cancelled the operation.
STOPPING : The operation is in the process of stopping, at user request.
SUCCEEDED : The operation completed creating or updating all the specified stacks without exceeding the failure tolerance for the operation.


CreationTimestamp (datetime) --
The time at which the operation was initiated. Note that the creation times for the stack set operation might differ from the creation time of the individual stacks themselves. This is because AWS CloudFormation needs to perform preparatory work for the operation, such as dispatching the work to the requested Regions, before actually creating the first stacks.

EndTimestamp (datetime) --
The time at which the stack set operation ended, across all accounts and Regions specified. Note that this doesn\'t necessarily mean that the stack set operation was successful, or even attempted, in each account or Region.





NextToken (string) --
If the request doesn\'t return all results, NextToken is set to a token. To retrieve the next set of results, call ListOperationResults again and assign that token to the request object\'s NextToken parameter. If there are no remaining results, NextToken is set to null .







Exceptions

CloudFormation.Client.exceptions.StackSetNotFoundException


    :return: {
        'Summaries': [
            {
                'OperationId': 'string',
                'Action': 'CREATE'|'UPDATE'|'DELETE'|'DETECT_DRIFT',
                'Status': 'RUNNING'|'SUCCEEDED'|'FAILED'|'STOPPING'|'STOPPED'|'QUEUED',
                'CreationTimestamp': datetime(2015, 1, 1),
                'EndTimestamp': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    FAILED : The operation exceeded the specified failure tolerance. The failure tolerance value that you\'ve set for an operation is applied for each Region during stack create and update operations. If the number of failed stacks within a Region exceeds the failure tolerance, the status of the operation in the Region is set to FAILED . This in turn sets the status of the operation as a whole to FAILED , and AWS CloudFormation cancels the operation in any remaining Regions.
    QUEUED : [Service-managed permissions] For automatic deployments that require a sequence of operations, the operation is queued to be performed. For more information, see the stack set operation status codes in the AWS CloudFormation User Guide.
    RUNNING : The operation is currently being performed.
    STOPPED : The user has cancelled the operation.
    STOPPING : The operation is in the process of stopping, at user request.
    SUCCEEDED : The operation completed creating or updating all the specified stacks without exceeding the failure tolerance for the operation.
    
    """
    pass

def list_stack_sets(NextToken=None, MaxResults=None, Status=None):
    """
    Returns summary information about stack sets that are associated with the user.
    See also: AWS API Documentation
    
    
    :example: response = client.list_stack_sets(
        NextToken='string',
        MaxResults=123,
        Status='ACTIVE'|'DELETED'
    )
    
    
    :type NextToken: string
    :param NextToken: If the previous paginated request didn\'t return all of the remaining results, the response object\'s NextToken parameter value is set to a token. To retrieve the next set of results, call ListStackSets again and assign that token to the request object\'s NextToken parameter. If there are no remaining results, the previous response object\'s NextToken parameter is set to null .

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a NextToken value that you can assign to the NextToken request parameter to get the next set of results.

    :type Status: string
    :param Status: The status of the stack sets that you want to get summary information about.

    :rtype: dict

ReturnsResponse Syntax
{
    'Summaries': [
        {
            'StackSetName': 'string',
            'StackSetId': 'string',
            'Description': 'string',
            'Status': 'ACTIVE'|'DELETED',
            'AutoDeployment': {
                'Enabled': True|False,
                'RetainStacksOnAccountRemoval': True|False
            },
            'PermissionModel': 'SERVICE_MANAGED'|'SELF_MANAGED',
            'DriftStatus': 'DRIFTED'|'IN_SYNC'|'UNKNOWN'|'NOT_CHECKED',
            'LastDriftCheckTimestamp': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Summaries (list) --
A list of StackSetSummary structures that contain information about the user\'s stack sets.

(dict) --
The structures that contain summary information about the specified stack set.

StackSetName (string) --
The name of the stack set.

StackSetId (string) --
The ID of the stack set.

Description (string) --
A description of the stack set that you specify when the stack set is created or updated.

Status (string) --
The status of the stack set.

AutoDeployment (dict) --
[Service-managed permissions] Describes whether StackSets automatically deploys to AWS Organizations accounts that are added to a target organizational unit (OU).

Enabled (boolean) --
If set to true , StackSets automatically deploys additional stack instances to AWS Organizations accounts that are added to a target organization or organizational unit (OU) in the specified Regions. If an account is removed from a target organization or OU, StackSets deletes stack instances from the account in the specified Regions.

RetainStacksOnAccountRemoval (boolean) --
If set to true , stack resources are retained when an account is removed from a target organization or OU. If set to false , stack resources are deleted. Specify only if Enabled is set to True .



PermissionModel (string) --
Describes how the IAM roles required for stack set operations are created.

With self-managed permissions, you must create the administrator and execution roles required to deploy to target accounts. For more information, see Grant Self-Managed Stack Set Permissions .
With service-managed permissions, StackSets automatically creates the IAM roles required to deploy to accounts managed by AWS Organizations. For more information, see Grant Service-Managed Stack Set Permissions .


DriftStatus (string) --
Status of the stack set\'s actual configuration compared to its expected template and parameter configuration. A stack set is considered to have drifted if one or more of its stack instances have drifted from their expected template and parameter configuration.

DRIFTED : One or more of the stack instances belonging to the stack set stack differs from the expected template and parameter configuration. A stack instance is considered to have drifted if one or more of the resources in the associated stack have drifted.
NOT_CHECKED : AWS CloudFormation has not checked the stack set for drift.
IN_SYNC : All of the stack instances belonging to the stack set stack match from the expected template and parameter configuration.
UNKNOWN : This value is reserved for future use.


LastDriftCheckTimestamp (datetime) --
Most recent time when CloudFormation performed a drift detection operation on the stack set. This value will be NULL for any stack set on which drift detection has not yet been performed.





NextToken (string) --
If the request doesn\'t return all of the remaining results, NextToken is set to a token. To retrieve the next set of results, call ListStackInstances again and assign that token to the request object\'s NextToken parameter. If the request returns all results, NextToken is set to null .








    :return: {
        'Summaries': [
            {
                'StackSetName': 'string',
                'StackSetId': 'string',
                'Description': 'string',
                'Status': 'ACTIVE'|'DELETED',
                'AutoDeployment': {
                    'Enabled': True|False,
                    'RetainStacksOnAccountRemoval': True|False
                },
                'PermissionModel': 'SERVICE_MANAGED'|'SELF_MANAGED',
                'DriftStatus': 'DRIFTED'|'IN_SYNC'|'UNKNOWN'|'NOT_CHECKED',
                'LastDriftCheckTimestamp': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    With self-managed permissions, you must create the administrator and execution roles required to deploy to target accounts. For more information, see Grant Self-Managed Stack Set Permissions .
    With service-managed permissions, StackSets automatically creates the IAM roles required to deploy to accounts managed by AWS Organizations. For more information, see Grant Service-Managed Stack Set Permissions .
    
    """
    pass

def list_stacks(NextToken=None, StackStatusFilter=None):
    """
    Returns the summary information for stacks whose status matches the specified StackStatusFilter. Summary information for stacks that have been deleted is kept for 90 days after the stack is deleted. If no StackStatusFilter is specified, summary information for all stacks is returned (including existing stacks and stacks that have been deleted).
    See also: AWS API Documentation
    
    
    :example: response = client.list_stacks(
        NextToken='string',
        StackStatusFilter=[
            'CREATE_IN_PROGRESS'|'CREATE_FAILED'|'CREATE_COMPLETE'|'ROLLBACK_IN_PROGRESS'|'ROLLBACK_FAILED'|'ROLLBACK_COMPLETE'|'DELETE_IN_PROGRESS'|'DELETE_FAILED'|'DELETE_COMPLETE'|'UPDATE_IN_PROGRESS'|'UPDATE_COMPLETE_CLEANUP_IN_PROGRESS'|'UPDATE_COMPLETE'|'UPDATE_ROLLBACK_IN_PROGRESS'|'UPDATE_ROLLBACK_FAILED'|'UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS'|'UPDATE_ROLLBACK_COMPLETE'|'REVIEW_IN_PROGRESS'|'IMPORT_IN_PROGRESS'|'IMPORT_COMPLETE'|'IMPORT_ROLLBACK_IN_PROGRESS'|'IMPORT_ROLLBACK_FAILED'|'IMPORT_ROLLBACK_COMPLETE',
        ]
    )
    
    
    :type NextToken: string
    :param NextToken: A string that identifies the next page of stacks that you want to retrieve.

    :type StackStatusFilter: list
    :param StackStatusFilter: Stack status to use as a filter. Specify one or more stack status codes to list only stacks with the specified status codes. For a complete list of stack status codes, see the StackStatus parameter of the Stack data type.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'StackSummaries': [
        {
            'StackId': 'string',
            'StackName': 'string',
            'TemplateDescription': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'LastUpdatedTime': datetime(2015, 1, 1),
            'DeletionTime': datetime(2015, 1, 1),
            'StackStatus': 'CREATE_IN_PROGRESS'|'CREATE_FAILED'|'CREATE_COMPLETE'|'ROLLBACK_IN_PROGRESS'|'ROLLBACK_FAILED'|'ROLLBACK_COMPLETE'|'DELETE_IN_PROGRESS'|'DELETE_FAILED'|'DELETE_COMPLETE'|'UPDATE_IN_PROGRESS'|'UPDATE_COMPLETE_CLEANUP_IN_PROGRESS'|'UPDATE_COMPLETE'|'UPDATE_ROLLBACK_IN_PROGRESS'|'UPDATE_ROLLBACK_FAILED'|'UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS'|'UPDATE_ROLLBACK_COMPLETE'|'REVIEW_IN_PROGRESS'|'IMPORT_IN_PROGRESS'|'IMPORT_COMPLETE'|'IMPORT_ROLLBACK_IN_PROGRESS'|'IMPORT_ROLLBACK_FAILED'|'IMPORT_ROLLBACK_COMPLETE',
            'StackStatusReason': 'string',
            'ParentId': 'string',
            'RootId': 'string',
            'DriftInformation': {
                'StackDriftStatus': 'DRIFTED'|'IN_SYNC'|'UNKNOWN'|'NOT_CHECKED',
                'LastCheckTimestamp': datetime(2015, 1, 1)
            }
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
The output for  ListStacks action.

StackSummaries (list) --
A list of StackSummary structures containing information about the specified stacks.

(dict) --
The StackSummary Data Type

StackId (string) --
Unique stack identifier.

StackName (string) --
The name associated with the stack.

TemplateDescription (string) --
The template description of the template used to create the stack.

CreationTime (datetime) --
The time the stack was created.

LastUpdatedTime (datetime) --
The time the stack was last updated. This field will only be returned if the stack has been updated at least once.

DeletionTime (datetime) --
The time the stack was deleted.

StackStatus (string) --
The current status of the stack.

StackStatusReason (string) --
Success/Failure message associated with the stack status.

ParentId (string) --
For nested stacks--stacks created as resources for another stack--the stack ID of the direct parent of this stack. For the first level of nested stacks, the root stack is also the parent stack.
For more information, see Working with Nested Stacks in the AWS CloudFormation User Guide .

RootId (string) --
For nested stacks--stacks created as resources for another stack--the stack ID of the top-level stack to which the nested stack ultimately belongs.
For more information, see Working with Nested Stacks in the AWS CloudFormation User Guide .

DriftInformation (dict) --
Summarizes information on whether a stack\'s actual configuration differs, or has drifted , from it\'s expected configuration, as defined in the stack template and any values specified as template parameters. For more information, see Detecting Unregulated Configuration Changes to Stacks and Resources .

StackDriftStatus (string) --
Status of the stack\'s actual configuration compared to its expected template configuration.

DRIFTED : The stack differs from its expected template configuration. A stack is considered to have drifted if one or more of its resources have drifted.
NOT_CHECKED : AWS CloudFormation has not checked if the stack differs from its expected template configuration.
IN_SYNC : The stack\'s actual configuration matches its expected template configuration.
UNKNOWN : This value is reserved for future use.


LastCheckTimestamp (datetime) --
Most recent time when a drift detection operation was initiated on the stack, or any of its individual resources that support drift detection.







NextToken (string) --
If the output exceeds 1 MB in size, a string that identifies the next page of stacks. If no additional page exists, this value is null.








    :return: {
        'StackSummaries': [
            {
                'StackId': 'string',
                'StackName': 'string',
                'TemplateDescription': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'LastUpdatedTime': datetime(2015, 1, 1),
                'DeletionTime': datetime(2015, 1, 1),
                'StackStatus': 'CREATE_IN_PROGRESS'|'CREATE_FAILED'|'CREATE_COMPLETE'|'ROLLBACK_IN_PROGRESS'|'ROLLBACK_FAILED'|'ROLLBACK_COMPLETE'|'DELETE_IN_PROGRESS'|'DELETE_FAILED'|'DELETE_COMPLETE'|'UPDATE_IN_PROGRESS'|'UPDATE_COMPLETE_CLEANUP_IN_PROGRESS'|'UPDATE_COMPLETE'|'UPDATE_ROLLBACK_IN_PROGRESS'|'UPDATE_ROLLBACK_FAILED'|'UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS'|'UPDATE_ROLLBACK_COMPLETE'|'REVIEW_IN_PROGRESS'|'IMPORT_IN_PROGRESS'|'IMPORT_COMPLETE'|'IMPORT_ROLLBACK_IN_PROGRESS'|'IMPORT_ROLLBACK_FAILED'|'IMPORT_ROLLBACK_COMPLETE',
                'StackStatusReason': 'string',
                'ParentId': 'string',
                'RootId': 'string',
                'DriftInformation': {
                    'StackDriftStatus': 'DRIFTED'|'IN_SYNC'|'UNKNOWN'|'NOT_CHECKED',
                    'LastCheckTimestamp': datetime(2015, 1, 1)
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    DRIFTED : The stack differs from its expected template configuration. A stack is considered to have drifted if one or more of its resources have drifted.
    NOT_CHECKED : AWS CloudFormation has not checked if the stack differs from its expected template configuration.
    IN_SYNC : The stack\'s actual configuration matches its expected template configuration.
    UNKNOWN : This value is reserved for future use.
    
    """
    pass

def list_type_registrations(Type=None, TypeName=None, TypeArn=None, RegistrationStatusFilter=None, MaxResults=None, NextToken=None):
    """
    Returns a list of registration tokens for the specified type(s).
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_type_registrations(
        Type='RESOURCE',
        TypeName='string',
        TypeArn='string',
        RegistrationStatusFilter='COMPLETE'|'IN_PROGRESS'|'FAILED',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type Type: string
    :param Type: The kind of type.\nCurrently the only valid value is RESOURCE .\nConditional: You must specify either TypeName and Type , or Arn .\n

    :type TypeName: string
    :param TypeName: The name of the type.\nConditional: You must specify either TypeName and Type , or Arn .\n

    :type TypeArn: string
    :param TypeArn: The Amazon Resource Name (ARN) of the type.\nConditional: You must specify either TypeName and Type , or Arn .\n

    :type RegistrationStatusFilter: string
    :param RegistrationStatusFilter: The current status of the type registration request.\nThe default is IN_PROGRESS .\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a NextToken value that you can assign to the NextToken request parameter to get the next set of results.

    :type NextToken: string
    :param NextToken: If the previous paginated request didn\'t return all of the remaining results, the response object\'s NextToken parameter value is set to a token. To retrieve the next set of results, call this action again and assign that token to the request object\'s NextToken parameter. If there are no remaining results, the previous response object\'s NextToken parameter is set to null .

    :rtype: dict

ReturnsResponse Syntax
{
    'RegistrationTokenList': [
        'string',
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

RegistrationTokenList (list) --
A list of type registration tokens.
Use ``  DescribeTypeRegistration `` to return detailed information about a type registration request.

(string) --


NextToken (string) --
If the request doesn\'t return all of the remaining results, NextToken is set to a token. To retrieve the next set of results, call this action again and assign that token to the request object\'s NextToken parameter. If the request returns all results, NextToken is set to null .







Exceptions

CloudFormation.Client.exceptions.CFNRegistryException


    :return: {
        'RegistrationTokenList': [
            'string',
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_type_versions(Type=None, TypeName=None, Arn=None, MaxResults=None, NextToken=None, DeprecatedStatus=None):
    """
    Returns summary information about the versions of a type.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_type_versions(
        Type='RESOURCE',
        TypeName='string',
        Arn='string',
        MaxResults=123,
        NextToken='string',
        DeprecatedStatus='LIVE'|'DEPRECATED'
    )
    
    
    :type Type: string
    :param Type: The kind of the type.\nCurrently the only valid value is RESOURCE .\nConditional: You must specify either TypeName and Type , or Arn .\n

    :type TypeName: string
    :param TypeName: The name of the type for which you want version summary information.\nConditional: You must specify either TypeName and Type , or Arn .\n

    :type Arn: string
    :param Arn: The Amazon Resource Name (ARN) of the type for which you want version summary information.\nConditional: You must specify either TypeName and Type , or Arn .\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a NextToken value that you can assign to the NextToken request parameter to get the next set of results.

    :type NextToken: string
    :param NextToken: If the previous paginated request didn\'t return all of the remaining results, the response object\'s NextToken parameter value is set to a token. To retrieve the next set of results, call this action again and assign that token to the request object\'s NextToken parameter. If there are no remaining results, the previous response object\'s NextToken parameter is set to null .

    :type DeprecatedStatus: string
    :param DeprecatedStatus: The deprecation status of the type versions that you want to get summary information about.\nValid values include:\n\nLIVE : The type version is registered and can be used in CloudFormation operations, dependent on its provisioning behavior and visibility scope.\nDEPRECATED : The type version has been deregistered and can no longer be used in CloudFormation operations.\n\nThe default is LIVE .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'TypeVersionSummaries': [
        {
            'Type': 'RESOURCE',
            'TypeName': 'string',
            'VersionId': 'string',
            'IsDefaultVersion': True|False,
            'Arn': 'string',
            'TimeCreated': datetime(2015, 1, 1),
            'Description': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

TypeVersionSummaries (list) --
A list of TypeVersionSummary structures that contain information about the specified type\'s versions.

(dict) --
Contains summary information about a specific version of a CloudFormation type.

Type (string) --
The kind of type.

TypeName (string) --
The name of the type.

VersionId (string) --
The ID of a specific version of the type. The version ID is the value at the end of the Amazon Resource Name (ARN) assigned to the type version when it is registered.

IsDefaultVersion (boolean) --
Whether the specified type version is set as the default version.

Arn (string) --
The Amazon Resource Name (ARN) of the type version.

TimeCreated (datetime) --
When the version was registered.

Description (string) --
The description of the type version.





NextToken (string) --
If the request doesn\'t return all of the remaining results, NextToken is set to a token. To retrieve the next set of results, call this action again and assign that token to the request object\'s NextToken parameter. If the request returns all results, NextToken is set to null .







Exceptions

CloudFormation.Client.exceptions.CFNRegistryException


    :return: {
        'TypeVersionSummaries': [
            {
                'Type': 'RESOURCE',
                'TypeName': 'string',
                'VersionId': 'string',
                'IsDefaultVersion': True|False,
                'Arn': 'string',
                'TimeCreated': datetime(2015, 1, 1),
                'Description': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    CloudFormation.Client.exceptions.CFNRegistryException
    
    """
    pass

def list_types(Visibility=None, ProvisioningType=None, DeprecatedStatus=None, MaxResults=None, NextToken=None):
    """
    Returns summary information about types that have been registered with CloudFormation.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_types(
        Visibility='PUBLIC'|'PRIVATE',
        ProvisioningType='NON_PROVISIONABLE'|'IMMUTABLE'|'FULLY_MUTABLE',
        DeprecatedStatus='LIVE'|'DEPRECATED',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type Visibility: string
    :param Visibility: The scope at which the type is visible and usable in CloudFormation operations.\nValid values include:\n\nPRIVATE : The type is only visible and usable within the account in which it is registered. Currently, AWS CloudFormation marks any types you create as PRIVATE .\nPUBLIC : The type is publically visible and usable within any Amazon account.\n\nThe default is PRIVATE .\n

    :type ProvisioningType: string
    :param ProvisioningType: The provisioning behavior of the type. AWS CloudFormation determines the provisioning type during registration, based on the types of handlers in the schema handler package submitted.\nValid values include:\n\nFULLY_MUTABLE : The type includes an update handler to process updates to the type during stack update operations.\nIMMUTABLE : The type does not include an update handler, so the type cannot be updated and must instead be replaced during stack update operations.\nNON_PROVISIONABLE : The type does not include create, read, and delete handlers, and therefore cannot actually be provisioned.\n\n

    :type DeprecatedStatus: string
    :param DeprecatedStatus: The deprecation status of the types that you want to get summary information about.\nValid values include:\n\nLIVE : The type is registered for use in CloudFormation operations.\nDEPRECATED : The type has been deregistered and can no longer be used in CloudFormation operations.\n\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a NextToken value that you can assign to the NextToken request parameter to get the next set of results.

    :type NextToken: string
    :param NextToken: If the previous paginated request didn\'t return all of the remaining results, the response object\'s NextToken parameter value is set to a token. To retrieve the next set of results, call this action again and assign that token to the request object\'s NextToken parameter. If there are no remaining results, the previous response object\'s NextToken parameter is set to null .

    :rtype: dict

ReturnsResponse Syntax
{
    'TypeSummaries': [
        {
            'Type': 'RESOURCE',
            'TypeName': 'string',
            'DefaultVersionId': 'string',
            'TypeArn': 'string',
            'LastUpdated': datetime(2015, 1, 1),
            'Description': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

TypeSummaries (list) --
A list of TypeSummary structures that contain information about the specified types.

(dict) --
Contains summary information about the specified CloudFormation type.

Type (string) --
The kind of type.

TypeName (string) --
The name of the type.

DefaultVersionId (string) --
The ID of the default version of the type. The default version is used when the type version is not specified.
To set the default version of a type, use ``  SetTypeDefaultVersion `` .

TypeArn (string) --
The Amazon Resource Name (ARN) of the type.

LastUpdated (datetime) --
When the current default version of the type was registered.

Description (string) --
The description of the type.





NextToken (string) --
If the request doesn\'t return all of the remaining results, NextToken is set to a token. To retrieve the next set of results, call this action again and assign that token to the request object\'s NextToken parameter. If the request returns all results, NextToken is set to null .







Exceptions

CloudFormation.Client.exceptions.CFNRegistryException


    :return: {
        'TypeSummaries': [
            {
                'Type': 'RESOURCE',
                'TypeName': 'string',
                'DefaultVersionId': 'string',
                'TypeArn': 'string',
                'LastUpdated': datetime(2015, 1, 1),
                'Description': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    CloudFormation.Client.exceptions.CFNRegistryException
    
    """
    pass

def record_handler_progress(BearerToken=None, OperationStatus=None, CurrentOperationStatus=None, StatusMessage=None, ErrorCode=None, ResourceModel=None, ClientRequestToken=None):
    """
    Reports progress of a resource handler to CloudFormation.
    Reserved for use by the CloudFormation CLI . Do not use this API in your code.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.record_handler_progress(
        BearerToken='string',
        OperationStatus='PENDING'|'IN_PROGRESS'|'SUCCESS'|'FAILED',
        CurrentOperationStatus='PENDING'|'IN_PROGRESS'|'SUCCESS'|'FAILED',
        StatusMessage='string',
        ErrorCode='NotUpdatable'|'InvalidRequest'|'AccessDenied'|'InvalidCredentials'|'AlreadyExists'|'NotFound'|'ResourceConflict'|'Throttling'|'ServiceLimitExceeded'|'NotStabilized'|'GeneralServiceException'|'ServiceInternalError'|'NetworkFailure'|'InternalFailure',
        ResourceModel='string',
        ClientRequestToken='string'
    )
    
    
    :type BearerToken: string
    :param BearerToken: [REQUIRED]\nReserved for use by the CloudFormation CLI .\n

    :type OperationStatus: string
    :param OperationStatus: [REQUIRED]\nReserved for use by the CloudFormation CLI .\n

    :type CurrentOperationStatus: string
    :param CurrentOperationStatus: Reserved for use by the CloudFormation CLI .

    :type StatusMessage: string
    :param StatusMessage: Reserved for use by the CloudFormation CLI .

    :type ErrorCode: string
    :param ErrorCode: Reserved for use by the CloudFormation CLI .

    :type ResourceModel: string
    :param ResourceModel: Reserved for use by the CloudFormation CLI .

    :type ClientRequestToken: string
    :param ClientRequestToken: Reserved for use by the CloudFormation CLI .

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

CloudFormation.Client.exceptions.InvalidStateTransitionException
CloudFormation.Client.exceptions.OperationStatusCheckFailedException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def register_type(Type=None, TypeName=None, SchemaHandlerPackage=None, LoggingConfig=None, ExecutionRoleArn=None, ClientRequestToken=None):
    """
    Registers a type with the CloudFormation service. Registering a type makes it available for use in CloudFormation templates in your AWS account, and includes:
    For more information on how to develop types and ready them for registeration, see Creating Resource Providers in the CloudFormation CLI User Guide .
    You can have a maximum of 50 resource type versions registered at a time. This maximum is per account and per region. Use DeregisterType to deregister specific resource type versions if necessary.
    Once you have initiated a registration request using ``  RegisterType `` , you can use ``  DescribeTypeRegistration `` to monitor the progress of the registration request.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.register_type(
        Type='RESOURCE',
        TypeName='string',
        SchemaHandlerPackage='string',
        LoggingConfig={
            'LogRoleArn': 'string',
            'LogGroupName': 'string'
        },
        ExecutionRoleArn='string',
        ClientRequestToken='string'
    )
    
    
    :type Type: string
    :param Type: The kind of type.\nCurrently, the only valid value is RESOURCE .\n

    :type TypeName: string
    :param TypeName: [REQUIRED]\nThe name of the type being registered.\nWe recommend that type names adhere to the following pattern: company_or_organization ::service ::type .\n\nNote\nThe following organization namespaces are reserved and cannot be used in your resource type names:\n\nAlexa\nAMZN\nAmazon\nAWS\nCustom\nDev\n\n\n

    :type SchemaHandlerPackage: string
    :param SchemaHandlerPackage: [REQUIRED]\nA url to the S3 bucket containing the schema handler package that contains the schema, event handlers, and associated files for the type you want to register.\nFor information on generating a schema handler package for the type you want to register, see submit in the CloudFormation CLI User Guide .\n\nNote\nAs part of registering a resource provider type, CloudFormation must be able to access the S3 bucket which contains the schema handler package for that resource provider. For more information, see IAM Permissions for Registering a Resource Provider in the AWS CloudFormation User Guide .\n\n

    :type LoggingConfig: dict
    :param LoggingConfig: Specifies logging configuration information for a type.\n\nLogRoleArn (string) -- [REQUIRED]The ARN of the role that CloudFormation should assume when sending log entries to CloudWatch logs.\n\nLogGroupName (string) -- [REQUIRED]The Amazon CloudWatch log group to which CloudFormation sends error logging information when invoking the type\'s handlers.\n\n\n

    :type ExecutionRoleArn: string
    :param ExecutionRoleArn: The Amazon Resource Name (ARN) of the IAM execution role to use to register the type. If your resource type calls AWS APIs in any of its handlers, you must create an * IAM execution role * that includes the necessary permissions to call those AWS APIs, and provision that execution role in your account. CloudFormation then assumes that execution role to provide your resource type with the appropriate credentials.

    :type ClientRequestToken: string
    :param ClientRequestToken: A unique identifier that acts as an idempotency key for this registration request. Specifying a client request token prevents CloudFormation from generating more than one version of a type from the same registeration request, even if the request is submitted multiple times.

    :rtype: dict

ReturnsResponse Syntax
{
    'RegistrationToken': 'string'
}


Response Structure

(dict) --

RegistrationToken (string) --
The identifier for this registration request.
Use this registration token when calling ``  DescribeTypeRegistration `` , which returns information about the status and IDs of the type registration.







Exceptions

CloudFormation.Client.exceptions.CFNRegistryException


    :return: {
        'RegistrationToken': 'string'
    }
    
    
    :returns: 
    Type (string) -- The kind of type.
    Currently, the only valid value is RESOURCE .
    
    TypeName (string) -- [REQUIRED]
    The name of the type being registered.
    We recommend that type names adhere to the following pattern: company_or_organization ::service ::type .
    
    Note
    The following organization namespaces are reserved and cannot be used in your resource type names:
    
    Alexa
    AMZN
    Amazon
    AWS
    Custom
    Dev
    
    
    
    SchemaHandlerPackage (string) -- [REQUIRED]
    A url to the S3 bucket containing the schema handler package that contains the schema, event handlers, and associated files for the type you want to register.
    For information on generating a schema handler package for the type you want to register, see submit in the CloudFormation CLI User Guide .
    
    Note
    As part of registering a resource provider type, CloudFormation must be able to access the S3 bucket which contains the schema handler package for that resource provider. For more information, see IAM Permissions for Registering a Resource Provider in the AWS CloudFormation User Guide .
    
    
    LoggingConfig (dict) -- Specifies logging configuration information for a type.
    
    LogRoleArn (string) -- [REQUIRED]The ARN of the role that CloudFormation should assume when sending log entries to CloudWatch logs.
    
    LogGroupName (string) -- [REQUIRED]The Amazon CloudWatch log group to which CloudFormation sends error logging information when invoking the type\'s handlers.
    
    
    
    ExecutionRoleArn (string) -- The Amazon Resource Name (ARN) of the IAM execution role to use to register the type. If your resource type calls AWS APIs in any of its handlers, you must create an * IAM execution role * that includes the necessary permissions to call those AWS APIs, and provision that execution role in your account. CloudFormation then assumes that execution role to provide your resource type with the appropriate credentials.
    ClientRequestToken (string) -- A unique identifier that acts as an idempotency key for this registration request. Specifying a client request token prevents CloudFormation from generating more than one version of a type from the same registeration request, even if the request is submitted multiple times.
    
    """
    pass

def set_stack_policy(StackName=None, StackPolicyBody=None, StackPolicyURL=None):
    """
    Sets a stack policy for a specified stack.
    See also: AWS API Documentation
    
    
    :example: response = client.set_stack_policy(
        StackName='string',
        StackPolicyBody='string',
        StackPolicyURL='string'
    )
    
    
    :type StackName: string
    :param StackName: [REQUIRED]\nThe name or unique stack ID that you want to associate a policy with.\n

    :type StackPolicyBody: string
    :param StackPolicyBody: Structure containing the stack policy body. For more information, go to Prevent Updates to Stack Resources in the AWS CloudFormation User Guide. You can specify either the StackPolicyBody or the StackPolicyURL parameter, but not both.

    :type StackPolicyURL: string
    :param StackPolicyURL: Location of a file containing the stack policy. The URL must point to a policy (maximum size: 16 KB) located in an S3 bucket in the same Region as the stack. You can specify either the StackPolicyBody or the StackPolicyURL parameter, but not both.

    """
    pass

def set_type_default_version(Arn=None, Type=None, TypeName=None, VersionId=None):
    """
    Specify the default version of a type. The default version of a type will be used in CloudFormation operations.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.set_type_default_version(
        Arn='string',
        Type='RESOURCE',
        TypeName='string',
        VersionId='string'
    )
    
    
    :type Arn: string
    :param Arn: The Amazon Resource Name (ARN) of the type for which you want version summary information.\nConditional: You must specify either TypeName and Type , or Arn .\n

    :type Type: string
    :param Type: The kind of type.\nConditional: You must specify either TypeName and Type , or Arn .\n

    :type TypeName: string
    :param TypeName: The name of the type.\nConditional: You must specify either TypeName and Type , or Arn .\n

    :type VersionId: string
    :param VersionId: The ID of a specific version of the type. The version ID is the value at the end of the Amazon Resource Name (ARN) assigned to the type version when it is registered.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

CloudFormation.Client.exceptions.CFNRegistryException
CloudFormation.Client.exceptions.TypeNotFoundException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def signal_resource(StackName=None, LogicalResourceId=None, UniqueId=None, Status=None):
    """
    Sends a signal to the specified resource with a success or failure status. You can use the SignalResource API in conjunction with a creation policy or update policy. AWS CloudFormation doesn\'t proceed with a stack creation or update until resources receive the required number of signals or the timeout period is exceeded. The SignalResource API is useful in cases where you want to send signals from anywhere other than an Amazon EC2 instance.
    See also: AWS API Documentation
    
    
    :example: response = client.signal_resource(
        StackName='string',
        LogicalResourceId='string',
        UniqueId='string',
        Status='SUCCESS'|'FAILURE'
    )
    
    
    :type StackName: string
    :param StackName: [REQUIRED]\nThe stack name or unique stack ID that includes the resource that you want to signal.\n

    :type LogicalResourceId: string
    :param LogicalResourceId: [REQUIRED]\nThe logical ID of the resource that you want to signal. The logical ID is the name of the resource that given in the template.\n

    :type UniqueId: string
    :param UniqueId: [REQUIRED]\nA unique ID of the signal. When you signal Amazon EC2 instances or Auto Scaling groups, specify the instance ID that you are signaling as the unique ID. If you send multiple signals to a single resource (such as signaling a wait condition), each signal requires a different unique ID.\n

    :type Status: string
    :param Status: [REQUIRED]\nThe status of the signal, which is either success or failure. A failure signal causes AWS CloudFormation to immediately fail the stack creation or update.\n

    """
    pass

def stop_stack_set_operation(StackSetName=None, OperationId=None):
    """
    Stops an in-progress operation on a stack set and its associated stack instances.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.stop_stack_set_operation(
        StackSetName='string',
        OperationId='string'
    )
    
    
    :type StackSetName: string
    :param StackSetName: [REQUIRED]\nThe name or unique ID of the stack set that you want to stop the operation for.\n

    :type OperationId: string
    :param OperationId: [REQUIRED]\nThe ID of the stack operation.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

CloudFormation.Client.exceptions.StackSetNotFoundException
CloudFormation.Client.exceptions.OperationNotFoundException
CloudFormation.Client.exceptions.InvalidOperationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_stack(StackName=None, TemplateBody=None, TemplateURL=None, UsePreviousTemplate=None, StackPolicyDuringUpdateBody=None, StackPolicyDuringUpdateURL=None, Parameters=None, Capabilities=None, ResourceTypes=None, RoleARN=None, RollbackConfiguration=None, StackPolicyBody=None, StackPolicyURL=None, NotificationARNs=None, Tags=None, ClientRequestToken=None):
    """
    Updates a stack as specified in the template. After the call completes successfully, the stack update starts. You can check the status of the stack via the  DescribeStacks action.
    To get a copy of the template for an existing stack, you can use the  GetTemplate action.
    For more information about creating an update template, updating a stack, and monitoring the progress of the update, see Updating a Stack .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_stack(
        StackName='string',
        TemplateBody='string',
        TemplateURL='string',
        UsePreviousTemplate=True|False,
        StackPolicyDuringUpdateBody='string',
        StackPolicyDuringUpdateURL='string',
        Parameters=[
            {
                'ParameterKey': 'string',
                'ParameterValue': 'string',
                'UsePreviousValue': True|False,
                'ResolvedValue': 'string'
            },
        ],
        Capabilities=[
            'CAPABILITY_IAM'|'CAPABILITY_NAMED_IAM'|'CAPABILITY_AUTO_EXPAND',
        ],
        ResourceTypes=[
            'string',
        ],
        RoleARN='string',
        RollbackConfiguration={
            'RollbackTriggers': [
                {
                    'Arn': 'string',
                    'Type': 'string'
                },
            ],
            'MonitoringTimeInMinutes': 123
        },
        StackPolicyBody='string',
        StackPolicyURL='string',
        NotificationARNs=[
            'string',
        ],
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        ClientRequestToken='string'
    )
    
    
    :type StackName: string
    :param StackName: [REQUIRED]\nThe name or unique stack ID of the stack to update.\n

    :type TemplateBody: string
    :param TemplateBody: Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes. (For more information, go to Template Anatomy in the AWS CloudFormation User Guide.)\nConditional: You must specify only one of the following parameters: TemplateBody , TemplateURL , or set the UsePreviousTemplate to true .\n

    :type TemplateURL: string
    :param TemplateURL: Location of file containing the template body. The URL must point to a template that is located in an Amazon S3 bucket. For more information, go to Template Anatomy in the AWS CloudFormation User Guide.\nConditional: You must specify only one of the following parameters: TemplateBody , TemplateURL , or set the UsePreviousTemplate to true .\n

    :type UsePreviousTemplate: boolean
    :param UsePreviousTemplate: Reuse the existing template that is associated with the stack that you are updating.\nConditional: You must specify only one of the following parameters: TemplateBody , TemplateURL , or set the UsePreviousTemplate to true .\n

    :type StackPolicyDuringUpdateBody: string
    :param StackPolicyDuringUpdateBody: Structure containing the temporary overriding stack policy body. You can specify either the StackPolicyDuringUpdateBody or the StackPolicyDuringUpdateURL parameter, but not both.\nIf you want to update protected resources, specify a temporary overriding stack policy during this update. If you do not specify a stack policy, the current policy that is associated with the stack will be used.\n

    :type StackPolicyDuringUpdateURL: string
    :param StackPolicyDuringUpdateURL: Location of a file containing the temporary overriding stack policy. The URL must point to a policy (max size: 16KB) located in an S3 bucket in the same Region as the stack. You can specify either the StackPolicyDuringUpdateBody or the StackPolicyDuringUpdateURL parameter, but not both.\nIf you want to update protected resources, specify a temporary overriding stack policy during this update. If you do not specify a stack policy, the current policy that is associated with the stack will be used.\n

    :type Parameters: list
    :param Parameters: A list of Parameter structures that specify input parameters for the stack. For more information, see the Parameter data type.\n\n(dict) --The Parameter data type.\n\nParameterKey (string) --The key associated with the parameter. If you don\'t specify a key and value for a particular parameter, AWS CloudFormation uses the default value that is specified in your template.\n\nParameterValue (string) --The input value associated with the parameter.\n\nUsePreviousValue (boolean) --During a stack update, use the existing parameter value that the stack is using for a given parameter key. If you specify true , do not specify a parameter value.\n\nResolvedValue (string) --Read-only. The value that corresponds to a Systems Manager parameter key. This field is returned only for ` SSM parameter types <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html#aws-ssm-parameter-types>`__ in the template.\n\n\n\n\n

    :type Capabilities: list
    :param Capabilities: In some cases, you must explicitly acknowledge that your stack template contains certain capabilities in order for AWS CloudFormation to update the stack.\n\nCAPABILITY_IAM and CAPABILITY_NAMED_IAM  Some stack templates might include resources that can affect permissions in your AWS account; for example, by creating new AWS Identity and Access Management (IAM) users. For those stacks, you must explicitly acknowledge this by specifying one of these capabilities. The following IAM resources require you to specify either the CAPABILITY_IAM or CAPABILITY_NAMED_IAM capability.\nIf you have IAM resources, you can specify either capability.\nIf you have IAM resources with custom names, you must specify CAPABILITY_NAMED_IAM .\nIf you don\'t specify either of these capabilities, AWS CloudFormation returns an InsufficientCapabilities error.\n\n\n\nIf your stack template contains these resources, we recommend that you review all permissions associated with them and edit their permissions if necessary.\n\n\nAWS::IAM::AccessKey\nAWS::IAM::Group\nAWS::IAM::InstanceProfile\nAWS::IAM::Policy\nAWS::IAM::Role\nAWS::IAM::User\nAWS::IAM::UserToGroupAddition\n\n\nFor more information, see Acknowledging IAM Resources in AWS CloudFormation Templates .\n\nCAPABILITY_AUTO_EXPAND  Some template contain macros. Macros perform custom processing on templates; this can include simple actions like find-and-replace operations, all the way to extensive transformations of entire templates. Because of this, users typically create a change set from the processed template, so that they can review the changes resulting from the macros before actually updating the stack. If your stack template contains one or more macros, and you choose to update a stack directly from the processed template, without first reviewing the resulting changes in a change set, you must acknowledge this capability. This includes the AWS::Include and AWS::Serverless transforms, which are macros hosted by AWS CloudFormation. Change sets do not currently support nested stacks. If you want to update a stack from a stack template that contains macros and nested stacks, you must update the stack directly from the template using this capability.\n\n\nWarning\n\nYou should only update stacks directly from a stack template that contains macros if you know what processing the macro performs. Each macro relies on an underlying Lambda service function for processing stack templates. Be aware that the Lambda function owner can update the function operation without AWS CloudFormation being notified.\nFor more information, see Using AWS CloudFormation Macros to Perform Custom Processing on Templates .\n\n\n(string) --\n\n

    :type ResourceTypes: list
    :param ResourceTypes: The template resource types that you have permissions to work with for this update stack action, such as AWS::EC2::Instance , AWS::EC2::* , or Custom::MyCustomInstance .\nIf the list of resource types doesn\'t include a resource that you\'re updating, the stack update fails. By default, AWS CloudFormation grants permissions to all resource types. AWS Identity and Access Management (IAM) uses this parameter for AWS CloudFormation-specific condition keys in IAM policies. For more information, see Controlling Access with AWS Identity and Access Management .\n\n(string) --\n\n

    :type RoleARN: string
    :param RoleARN: The Amazon Resource Name (ARN) of an AWS Identity and Access Management (IAM) role that AWS CloudFormation assumes to update the stack. AWS CloudFormation uses the role\'s credentials to make calls on your behalf. AWS CloudFormation always uses this role for all future operations on the stack. As long as users have permission to operate on the stack, AWS CloudFormation uses this role even if the users don\'t have permission to pass it. Ensure that the role grants least privilege.\nIf you don\'t specify a value, AWS CloudFormation uses the role that was previously associated with the stack. If no role is available, AWS CloudFormation uses a temporary session that is generated from your user credentials.\n

    :type RollbackConfiguration: dict
    :param RollbackConfiguration: The rollback triggers for AWS CloudFormation to monitor during stack creation and updating operations, and for the specified monitoring period afterwards.\n\nRollbackTriggers (list) --The triggers to monitor during stack creation or update actions.\nBy default, AWS CloudFormation saves the rollback triggers specified for a stack and applies them to any subsequent update operations for the stack, unless you specify otherwise. If you do specify rollback triggers for this parameter, those triggers replace any list of triggers previously specified for the stack. This means:\n\nTo use the rollback triggers previously specified for this stack, if any, don\'t specify this parameter.\nTo specify new or updated rollback triggers, you must specify all the triggers that you want used for this stack, even triggers you\'ve specifed before (for example, when creating the stack or during a previous stack update). Any triggers that you don\'t include in the updated list of triggers are no longer applied to the stack.\nTo remove all currently specified triggers, specify an empty list for this parameter.\n\nIf a specified trigger is missing, the entire stack operation fails and is rolled back.\n\n(dict) --A rollback trigger AWS CloudFormation monitors during creation and updating of stacks. If any of the alarms you specify goes to ALARM state during the stack operation or within the specified monitoring period afterwards, CloudFormation rolls back the entire stack operation.\n\nArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the rollback trigger.\nIf a specified trigger is missing, the entire stack operation fails and is rolled back.\n\nType (string) -- [REQUIRED]The resource type of the rollback trigger. Currently, AWS::CloudWatch::Alarm is the only supported resource type.\n\n\n\n\n\nMonitoringTimeInMinutes (integer) --The amount of time, in minutes, during which CloudFormation should monitor all the rollback triggers after the stack creation or update operation deploys all necessary resources.\nThe default is 0 minutes.\nIf you specify a monitoring period but do not specify any rollback triggers, CloudFormation still waits the specified period of time before cleaning up old resources after update operations. You can use this monitoring period to perform any manual stack validation desired, and manually cancel the stack creation or update (using CancelUpdateStack , for example) as necessary.\nIf you specify 0 for this parameter, CloudFormation still monitors the specified rollback triggers during stack creation and update operations. Then, for update operations, it begins disposing of old resources immediately once the operation completes.\n\n\n

    :type StackPolicyBody: string
    :param StackPolicyBody: Structure containing a new stack policy body. You can specify either the StackPolicyBody or the StackPolicyURL parameter, but not both.\nYou might update the stack policy, for example, in order to protect a new resource that you created during a stack update. If you do not specify a stack policy, the current policy that is associated with the stack is unchanged.\n

    :type StackPolicyURL: string
    :param StackPolicyURL: Location of a file containing the updated stack policy. The URL must point to a policy (max size: 16KB) located in an S3 bucket in the same Region as the stack. You can specify either the StackPolicyBody or the StackPolicyURL parameter, but not both.\nYou might update the stack policy, for example, in order to protect a new resource that you created during a stack update. If you do not specify a stack policy, the current policy that is associated with the stack is unchanged.\n

    :type NotificationARNs: list
    :param NotificationARNs: Amazon Simple Notification Service topic Amazon Resource Names (ARNs) that AWS CloudFormation associates with the stack. Specify an empty list to remove all notification topics.\n\n(string) --\n\n

    :type Tags: list
    :param Tags: Key-value pairs to associate with this stack. AWS CloudFormation also propagates these tags to supported resources in the stack. You can specify a maximum number of 50 tags.\nIf you don\'t specify this parameter, AWS CloudFormation doesn\'t modify the stack\'s tags. If you specify an empty value, AWS CloudFormation removes all associated tags.\n\n(dict) --The Tag type enables you to specify a key-value pair that can be used to store information about an AWS CloudFormation stack.\n\nKey (string) -- [REQUIRED]\nRequired . A string used to identify this tag. You can specify a maximum of 128 characters for a tag key. Tags owned by Amazon Web Services (AWS) have the reserved prefix: aws: .\n\nValue (string) -- [REQUIRED]\nRequired . A string containing the value for this tag. You can specify a maximum of 256 characters for a tag value.\n\n\n\n\n

    :type ClientRequestToken: string
    :param ClientRequestToken: A unique identifier for this UpdateStack request. Specify this token if you plan to retry requests so that AWS CloudFormation knows that you\'re not attempting to update a stack with the same name. You might retry UpdateStack requests to ensure that AWS CloudFormation successfully received them.\nAll events triggered by a given stack operation are assigned the same client request token, which you can use to track operations. For example, if you execute a CreateStack operation with the token token1 , then all the StackEvents generated by that operation will have ClientRequestToken set as token1 .\nIn the console, stack operations display the client request token on the Events tab. Stack operations that are initiated from the console use the token format Console-StackOperation-ID , which helps you easily identify the stack operation . For example, if you create a stack using the console, each stack event would be assigned the same token in the following format: Console-CreateStack-7f59c3cf-00d2-40c7-b2ff-e75db0987002 .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'StackId': 'string'
}


Response Structure

(dict) --
The output for an  UpdateStack action.

StackId (string) --
Unique identifier of the stack.







Exceptions

CloudFormation.Client.exceptions.InsufficientCapabilitiesException
CloudFormation.Client.exceptions.TokenAlreadyExistsException


    :return: {
        'StackId': 'string'
    }
    
    
    :returns: 
    CloudFormation.Client.exceptions.InsufficientCapabilitiesException
    CloudFormation.Client.exceptions.TokenAlreadyExistsException
    
    """
    pass

def update_stack_instances(StackSetName=None, Accounts=None, DeploymentTargets=None, Regions=None, ParameterOverrides=None, OperationPreferences=None, OperationId=None):
    """
    Updates the parameter values for stack instances for the specified accounts, within the specified Regions. A stack instance refers to a stack in a specific account and Region.
    You can only update stack instances in Regions and accounts where they already exist; to create additional stack instances, use CreateStackInstances .
    During stack set updates, any parameters overridden for a stack instance are not updated, but retain their overridden value.
    You can only update the parameter values that are specified in the stack set; to add or delete a parameter itself, use UpdateStackSet to update the stack set template. If you add a parameter to a template, before you can override the parameter value specified in the stack set you must first use UpdateStackSet to update all stack instances with the updated template and parameter value specified in the stack set. Once a stack instance has been updated with the new parameter, you can then override the parameter value using UpdateStackInstances .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_stack_instances(
        StackSetName='string',
        Accounts=[
            'string',
        ],
        DeploymentTargets={
            'Accounts': [
                'string',
            ],
            'OrganizationalUnitIds': [
                'string',
            ]
        },
        Regions=[
            'string',
        ],
        ParameterOverrides=[
            {
                'ParameterKey': 'string',
                'ParameterValue': 'string',
                'UsePreviousValue': True|False,
                'ResolvedValue': 'string'
            },
        ],
        OperationPreferences={
            'RegionOrder': [
                'string',
            ],
            'FailureToleranceCount': 123,
            'FailureTolerancePercentage': 123,
            'MaxConcurrentCount': 123,
            'MaxConcurrentPercentage': 123
        },
        OperationId='string'
    )
    
    
    :type StackSetName: string
    :param StackSetName: [REQUIRED]\nThe name or unique ID of the stack set associated with the stack instances.\n

    :type Accounts: list
    :param Accounts: [Self-managed permissions] The names of one or more AWS accounts for which you want to update parameter values for stack instances. The overridden parameter values will be applied to all stack instances in the specified accounts and Regions.\nYou can specify Accounts or DeploymentTargets , but not both.\n\n(string) --\n\n

    :type DeploymentTargets: dict
    :param DeploymentTargets: [Service-managed permissions] The AWS Organizations accounts for which you want to update parameter values for stack instances. If your update targets OUs, the overridden parameter values only apply to the accounts that are currently in the target OUs and their child OUs. Accounts added to the target OUs and their child OUs in the future won\'t use the overridden values.\nYou can specify Accounts or DeploymentTargets , but not both.\n\nAccounts (list) --The names of one or more AWS accounts for which you want to deploy stack set updates.\n\n(string) --\n\n\nOrganizationalUnitIds (list) --The organization root ID or organizational unit (OU) IDs to which StackSets deploys.\n\n(string) --\n\n\n\n

    :type Regions: list
    :param Regions: [REQUIRED]\nThe names of one or more Regions in which you want to update parameter values for stack instances. The overridden parameter values will be applied to all stack instances in the specified accounts and Regions.\n\n(string) --\n\n

    :type ParameterOverrides: list
    :param ParameterOverrides: A list of input parameters whose values you want to update for the specified stack instances.\nAny overridden parameter values will be applied to all stack instances in the specified accounts and Regions. When specifying parameters and their values, be aware of how AWS CloudFormation sets parameter values during stack instance update operations:\n\nTo override the current value for a parameter, include the parameter and specify its value.\nTo leave a parameter set to its present value, you can do one of the following:\nDo not include the parameter in the list.\nInclude the parameter and specify UsePreviousValue as true . (You cannot specify both a value and set UsePreviousValue to true .)\n\n\nTo set all overridden parameter back to the values specified in the stack set, specify a parameter list but do not include any parameters.\nTo leave all parameters set to their present values, do not specify this property at all.\n\nDuring stack set updates, any parameter values overridden for a stack instance are not updated, but retain their overridden value.\nYou can only override the parameter values that are specified in the stack set; to add or delete a parameter itself, use UpdateStackSet to update the stack set template. If you add a parameter to a template, before you can override the parameter value specified in the stack set you must first use UpdateStackSet to update all stack instances with the updated template and parameter value specified in the stack set. Once a stack instance has been updated with the new parameter, you can then override the parameter value using UpdateStackInstances .\n\n(dict) --The Parameter data type.\n\nParameterKey (string) --The key associated with the parameter. If you don\'t specify a key and value for a particular parameter, AWS CloudFormation uses the default value that is specified in your template.\n\nParameterValue (string) --The input value associated with the parameter.\n\nUsePreviousValue (boolean) --During a stack update, use the existing parameter value that the stack is using for a given parameter key. If you specify true , do not specify a parameter value.\n\nResolvedValue (string) --Read-only. The value that corresponds to a Systems Manager parameter key. This field is returned only for ` SSM parameter types <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html#aws-ssm-parameter-types>`__ in the template.\n\n\n\n\n

    :type OperationPreferences: dict
    :param OperationPreferences: Preferences for how AWS CloudFormation performs this stack set operation.\n\nRegionOrder (list) --The order of the Regions in where you want to perform the stack operation.\n\n(string) --\n\n\nFailureToleranceCount (integer) --The number of accounts, per Region, for which this operation can fail before AWS CloudFormation stops the operation in that Region. If the operation is stopped in a Region, AWS CloudFormation doesn\'t attempt the operation in any subsequent Regions.\nConditional: You must specify either FailureToleranceCount or FailureTolerancePercentage (but not both).\n\nFailureTolerancePercentage (integer) --The percentage of accounts, per Region, for which this stack operation can fail before AWS CloudFormation stops the operation in that Region. If the operation is stopped in a Region, AWS CloudFormation doesn\'t attempt the operation in any subsequent Regions.\nWhen calculating the number of accounts based on the specified percentage, AWS CloudFormation rounds down to the next whole number.\nConditional: You must specify either FailureToleranceCount or FailureTolerancePercentage , but not both.\n\nMaxConcurrentCount (integer) --The maximum number of accounts in which to perform this operation at one time. This is dependent on the value of FailureToleranceCount \xe2\x80\x94MaxConcurrentCount is at most one more than the FailureToleranceCount .\nNote that this setting lets you specify the maximum for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling.\nConditional: You must specify either MaxConcurrentCount or MaxConcurrentPercentage , but not both.\n\nMaxConcurrentPercentage (integer) --The maximum percentage of accounts in which to perform this operation at one time.\nWhen calculating the number of accounts based on the specified percentage, AWS CloudFormation rounds down to the next whole number. This is true except in cases where rounding down would result is zero. In this case, CloudFormation sets the number as one instead.\nNote that this setting lets you specify the maximum for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling.\nConditional: You must specify either MaxConcurrentCount or MaxConcurrentPercentage , but not both.\n\n\n

    :type OperationId: string
    :param OperationId: The unique identifier for this stack set operation.\nThe operation ID also functions as an idempotency token, to ensure that AWS CloudFormation performs the stack set operation only once, even if you retry the request multiple times. You might retry stack set operation requests to ensure that AWS CloudFormation successfully received them.\nIf you don\'t specify an operation ID, the SDK generates one automatically.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'OperationId': 'string'
}


Response Structure

(dict) --

OperationId (string) --
The unique identifier for this stack set operation.







Exceptions

CloudFormation.Client.exceptions.StackSetNotFoundException
CloudFormation.Client.exceptions.StackInstanceNotFoundException
CloudFormation.Client.exceptions.OperationInProgressException
CloudFormation.Client.exceptions.OperationIdAlreadyExistsException
CloudFormation.Client.exceptions.StaleRequestException
CloudFormation.Client.exceptions.InvalidOperationException


    :return: {
        'OperationId': 'string'
    }
    
    
    :returns: 
    CloudFormation.Client.exceptions.StackSetNotFoundException
    CloudFormation.Client.exceptions.StackInstanceNotFoundException
    CloudFormation.Client.exceptions.OperationInProgressException
    CloudFormation.Client.exceptions.OperationIdAlreadyExistsException
    CloudFormation.Client.exceptions.StaleRequestException
    CloudFormation.Client.exceptions.InvalidOperationException
    
    """
    pass

def update_stack_set(StackSetName=None, Description=None, TemplateBody=None, TemplateURL=None, UsePreviousTemplate=None, Parameters=None, Capabilities=None, Tags=None, OperationPreferences=None, AdministrationRoleARN=None, ExecutionRoleName=None, DeploymentTargets=None, PermissionModel=None, AutoDeployment=None, OperationId=None, Accounts=None, Regions=None):
    """
    Updates the stack set, and associated stack instances in the specified accounts and Regions.
    Even if the stack set operation created by updating the stack set fails (completely or partially, below or above a specified failure tolerance), the stack set is updated with your changes. Subsequent  CreateStackInstances calls on the specified stack set use the updated stack set.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_stack_set(
        StackSetName='string',
        Description='string',
        TemplateBody='string',
        TemplateURL='string',
        UsePreviousTemplate=True|False,
        Parameters=[
            {
                'ParameterKey': 'string',
                'ParameterValue': 'string',
                'UsePreviousValue': True|False,
                'ResolvedValue': 'string'
            },
        ],
        Capabilities=[
            'CAPABILITY_IAM'|'CAPABILITY_NAMED_IAM'|'CAPABILITY_AUTO_EXPAND',
        ],
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        OperationPreferences={
            'RegionOrder': [
                'string',
            ],
            'FailureToleranceCount': 123,
            'FailureTolerancePercentage': 123,
            'MaxConcurrentCount': 123,
            'MaxConcurrentPercentage': 123
        },
        AdministrationRoleARN='string',
        ExecutionRoleName='string',
        DeploymentTargets={
            'Accounts': [
                'string',
            ],
            'OrganizationalUnitIds': [
                'string',
            ]
        },
        PermissionModel='SERVICE_MANAGED'|'SELF_MANAGED',
        AutoDeployment={
            'Enabled': True|False,
            'RetainStacksOnAccountRemoval': True|False
        },
        OperationId='string',
        Accounts=[
            'string',
        ],
        Regions=[
            'string',
        ]
    )
    
    
    :type StackSetName: string
    :param StackSetName: [REQUIRED]\nThe name or unique ID of the stack set that you want to update.\n

    :type Description: string
    :param Description: A brief description of updates that you are making.

    :type TemplateBody: string
    :param TemplateBody: The structure that contains the template body, with a minimum length of 1 byte and a maximum length of 51,200 bytes. For more information, see Template Anatomy in the AWS CloudFormation User Guide.\nConditional: You must specify only one of the following parameters: TemplateBody or TemplateURL \xe2\x80\x94or set UsePreviousTemplate to true.\n

    :type TemplateURL: string
    :param TemplateURL: The location of the file that contains the template body. The URL must point to a template (maximum size: 460,800 bytes) that is located in an Amazon S3 bucket. For more information, see Template Anatomy in the AWS CloudFormation User Guide.\nConditional: You must specify only one of the following parameters: TemplateBody or TemplateURL \xe2\x80\x94or set UsePreviousTemplate to true.\n

    :type UsePreviousTemplate: boolean
    :param UsePreviousTemplate: Use the existing template that\'s associated with the stack set that you\'re updating.\nConditional: You must specify only one of the following parameters: TemplateBody or TemplateURL \xe2\x80\x94or set UsePreviousTemplate to true.\n

    :type Parameters: list
    :param Parameters: A list of input parameters for the stack set template.\n\n(dict) --The Parameter data type.\n\nParameterKey (string) --The key associated with the parameter. If you don\'t specify a key and value for a particular parameter, AWS CloudFormation uses the default value that is specified in your template.\n\nParameterValue (string) --The input value associated with the parameter.\n\nUsePreviousValue (boolean) --During a stack update, use the existing parameter value that the stack is using for a given parameter key. If you specify true , do not specify a parameter value.\n\nResolvedValue (string) --Read-only. The value that corresponds to a Systems Manager parameter key. This field is returned only for ` SSM parameter types <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html#aws-ssm-parameter-types>`__ in the template.\n\n\n\n\n

    :type Capabilities: list
    :param Capabilities: In some cases, you must explicitly acknowledge that your stack template contains certain capabilities in order for AWS CloudFormation to update the stack set and its associated stack instances.\n\nCAPABILITY_IAM and CAPABILITY_NAMED_IAM  Some stack templates might include resources that can affect permissions in your AWS account; for example, by creating new AWS Identity and Access Management (IAM) users. For those stacks sets, you must explicitly acknowledge this by specifying one of these capabilities. The following IAM resources require you to specify either the CAPABILITY_IAM or CAPABILITY_NAMED_IAM capability.\nIf you have IAM resources, you can specify either capability.\nIf you have IAM resources with custom names, you must specify CAPABILITY_NAMED_IAM .\nIf you don\'t specify either of these capabilities, AWS CloudFormation returns an InsufficientCapabilities error.\n\n\n\nIf your stack template contains these resources, we recommend that you review all permissions associated with them and edit their permissions if necessary.\n\n\nAWS::IAM::AccessKey\nAWS::IAM::Group\nAWS::IAM::InstanceProfile\nAWS::IAM::Policy\nAWS::IAM::Role\nAWS::IAM::User\nAWS::IAM::UserToGroupAddition\n\n\nFor more information, see Acknowledging IAM Resources in AWS CloudFormation Templates .\n\nCAPABILITY_AUTO_EXPAND  Some templates contain macros. If your stack template contains one or more macros, and you choose to update a stack directly from the processed template, without first reviewing the resulting changes in a change set, you must acknowledge this capability. For more information, see Using AWS CloudFormation Macros to Perform Custom Processing on Templates .\n\n\nWarning\nStack sets do not currently support macros in stack templates. (This includes the AWS::Include and AWS::Serverless transforms, which are macros hosted by AWS CloudFormation.) Even if you specify this capability, if you include a macro in your template the stack set operation will fail.\n\n\n(string) --\n\n

    :type Tags: list
    :param Tags: The key-value pairs to associate with this stack set and the stacks created from it. AWS CloudFormation also propagates these tags to supported resources that are created in the stacks. You can specify a maximum number of 50 tags.\nIf you specify tags for this parameter, those tags replace any list of tags that are currently associated with this stack set. This means:\n\nIf you don\'t specify this parameter, AWS CloudFormation doesn\'t modify the stack\'s tags.\nIf you specify any tags using this parameter, you must specify all the tags that you want associated with this stack set, even tags you\'ve specifed before (for example, when creating the stack set or during a previous update of the stack set.). Any tags that you don\'t include in the updated list of tags are removed from the stack set, and therefore from the stacks and resources as well.\nIf you specify an empty value, AWS CloudFormation removes all currently associated tags.\n\nIf you specify new tags as part of an UpdateStackSet action, AWS CloudFormation checks to see if you have the required IAM permission to tag resources. If you omit tags that are currently associated with the stack set from the list of tags you specify, AWS CloudFormation assumes that you want to remove those tags from the stack set, and checks to see if you have permission to untag resources. If you don\'t have the necessary permission(s), the entire UpdateStackSet action fails with an access denied error, and the stack set is not updated.\n\n(dict) --The Tag type enables you to specify a key-value pair that can be used to store information about an AWS CloudFormation stack.\n\nKey (string) -- [REQUIRED]\nRequired . A string used to identify this tag. You can specify a maximum of 128 characters for a tag key. Tags owned by Amazon Web Services (AWS) have the reserved prefix: aws: .\n\nValue (string) -- [REQUIRED]\nRequired . A string containing the value for this tag. You can specify a maximum of 256 characters for a tag value.\n\n\n\n\n

    :type OperationPreferences: dict
    :param OperationPreferences: Preferences for how AWS CloudFormation performs this stack set operation.\n\nRegionOrder (list) --The order of the Regions in where you want to perform the stack operation.\n\n(string) --\n\n\nFailureToleranceCount (integer) --The number of accounts, per Region, for which this operation can fail before AWS CloudFormation stops the operation in that Region. If the operation is stopped in a Region, AWS CloudFormation doesn\'t attempt the operation in any subsequent Regions.\nConditional: You must specify either FailureToleranceCount or FailureTolerancePercentage (but not both).\n\nFailureTolerancePercentage (integer) --The percentage of accounts, per Region, for which this stack operation can fail before AWS CloudFormation stops the operation in that Region. If the operation is stopped in a Region, AWS CloudFormation doesn\'t attempt the operation in any subsequent Regions.\nWhen calculating the number of accounts based on the specified percentage, AWS CloudFormation rounds down to the next whole number.\nConditional: You must specify either FailureToleranceCount or FailureTolerancePercentage , but not both.\n\nMaxConcurrentCount (integer) --The maximum number of accounts in which to perform this operation at one time. This is dependent on the value of FailureToleranceCount \xe2\x80\x94MaxConcurrentCount is at most one more than the FailureToleranceCount .\nNote that this setting lets you specify the maximum for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling.\nConditional: You must specify either MaxConcurrentCount or MaxConcurrentPercentage , but not both.\n\nMaxConcurrentPercentage (integer) --The maximum percentage of accounts in which to perform this operation at one time.\nWhen calculating the number of accounts based on the specified percentage, AWS CloudFormation rounds down to the next whole number. This is true except in cases where rounding down would result is zero. In this case, CloudFormation sets the number as one instead.\nNote that this setting lets you specify the maximum for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling.\nConditional: You must specify either MaxConcurrentCount or MaxConcurrentPercentage , but not both.\n\n\n

    :type AdministrationRoleARN: string
    :param AdministrationRoleARN: The Amazon Resource Number (ARN) of the IAM role to use to update this stack set.\nSpecify an IAM role only if you are using customized administrator roles to control which users or groups can manage specific stack sets within the same administrator account. For more information, see Granting Permissions for Stack Set Operations in the AWS CloudFormation User Guide .\nIf you specified a customized administrator role when you created the stack set, you must specify a customized administrator role, even if it is the same customized administrator role used with this stack set previously.\n

    :type ExecutionRoleName: string
    :param ExecutionRoleName: The name of the IAM execution role to use to update the stack set. If you do not specify an execution role, AWS CloudFormation uses the AWSCloudFormationStackSetExecutionRole role for the stack set operation.\nSpecify an IAM role only if you are using customized execution roles to control which stack resources users and groups can include in their stack sets.\nIf you specify a customized execution role, AWS CloudFormation uses that role to update the stack. If you do not specify a customized execution role, AWS CloudFormation performs the update using the role previously associated with the stack set, so long as you have permissions to perform operations on the stack set.\n

    :type DeploymentTargets: dict
    :param DeploymentTargets: [Service-managed permissions] The AWS Organizations accounts in which to update associated stack instances.\nTo update all the stack instances associated with this stack set, do not specify DeploymentTargets or Regions .\nIf the stack set update includes changes to the template (that is, if TemplateBody or TemplateURL is specified), or the Parameters , AWS CloudFormation marks all stack instances with a status of OUTDATED prior to updating the stack instances in the specified accounts and Regions. If the stack set update does not include changes to the template or parameters, AWS CloudFormation updates the stack instances in the specified accounts and Regions, while leaving all other stack instances with their existing stack instance status.\n\nAccounts (list) --The names of one or more AWS accounts for which you want to deploy stack set updates.\n\n(string) --\n\n\nOrganizationalUnitIds (list) --The organization root ID or organizational unit (OU) IDs to which StackSets deploys.\n\n(string) --\n\n\n\n

    :type PermissionModel: string
    :param PermissionModel: Describes how the IAM roles required for stack set operations are created. You cannot modify PermissionModel if there are stack instances associated with your stack set.\n\nWith self-managed permissions, you must create the administrator and execution roles required to deploy to target accounts. For more information, see Grant Self-Managed Stack Set Permissions .\nWith service-managed permissions, StackSets automatically creates the IAM roles required to deploy to accounts managed by AWS Organizations. For more information, see Grant Service-Managed Stack Set Permissions .\n\n

    :type AutoDeployment: dict
    :param AutoDeployment: [Service-managed permissions] Describes whether StackSets automatically deploys to AWS Organizations accounts that are added to a target organization or organizational unit (OU).\nIf you specify AutoDeployment , do not specify DeploymentTargets or Regions .\n\nEnabled (boolean) --If set to true , StackSets automatically deploys additional stack instances to AWS Organizations accounts that are added to a target organization or organizational unit (OU) in the specified Regions. If an account is removed from a target organization or OU, StackSets deletes stack instances from the account in the specified Regions.\n\nRetainStacksOnAccountRemoval (boolean) --If set to true , stack resources are retained when an account is removed from a target organization or OU. If set to false , stack resources are deleted. Specify only if Enabled is set to True .\n\n\n

    :type OperationId: string
    :param OperationId: The unique ID for this stack set operation.\nThe operation ID also functions as an idempotency token, to ensure that AWS CloudFormation performs the stack set operation only once, even if you retry the request multiple times. You might retry stack set operation requests to ensure that AWS CloudFormation successfully received them.\nIf you don\'t specify an operation ID, AWS CloudFormation generates one automatically.\nRepeating this stack set operation with a new operation ID retries all stack instances whose status is OUTDATED .\nThis field is autopopulated if not provided.\n

    :type Accounts: list
    :param Accounts: [Self-managed permissions] The accounts in which to update associated stack instances. If you specify accounts, you must also specify the Regions in which to update stack set instances.\nTo update all the stack instances associated with this stack set, do not specify the Accounts or Regions properties.\nIf the stack set update includes changes to the template (that is, if the TemplateBody or TemplateURL properties are specified), or the Parameters property, AWS CloudFormation marks all stack instances with a status of OUTDATED prior to updating the stack instances in the specified accounts and Regions. If the stack set update does not include changes to the template or parameters, AWS CloudFormation updates the stack instances in the specified accounts and Regions, while leaving all other stack instances with their existing stack instance status.\n\n(string) --\n\n

    :type Regions: list
    :param Regions: The Regions in which to update associated stack instances. If you specify Regions, you must also specify accounts in which to update stack set instances.\nTo update all the stack instances associated with this stack set, do not specify the Accounts or Regions properties.\nIf the stack set update includes changes to the template (that is, if the TemplateBody or TemplateURL properties are specified), or the Parameters property, AWS CloudFormation marks all stack instances with a status of OUTDATED prior to updating the stack instances in the specified accounts and Regions. If the stack set update does not include changes to the template or parameters, AWS CloudFormation updates the stack instances in the specified accounts and Regions, while leaving all other stack instances with their existing stack instance status.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'OperationId': 'string'
}


Response Structure

(dict) --

OperationId (string) --
The unique ID for this stack set operation.







Exceptions

CloudFormation.Client.exceptions.StackSetNotFoundException
CloudFormation.Client.exceptions.OperationInProgressException
CloudFormation.Client.exceptions.OperationIdAlreadyExistsException
CloudFormation.Client.exceptions.StaleRequestException
CloudFormation.Client.exceptions.InvalidOperationException
CloudFormation.Client.exceptions.StackInstanceNotFoundException


    :return: {
        'OperationId': 'string'
    }
    
    
    :returns: 
    CloudFormation.Client.exceptions.StackSetNotFoundException
    CloudFormation.Client.exceptions.OperationInProgressException
    CloudFormation.Client.exceptions.OperationIdAlreadyExistsException
    CloudFormation.Client.exceptions.StaleRequestException
    CloudFormation.Client.exceptions.InvalidOperationException
    CloudFormation.Client.exceptions.StackInstanceNotFoundException
    
    """
    pass

def update_termination_protection(EnableTerminationProtection=None, StackName=None):
    """
    Updates termination protection for the specified stack. If a user attempts to delete a stack with termination protection enabled, the operation fails and the stack remains unchanged. For more information, see Protecting a Stack From Being Deleted in the AWS CloudFormation User Guide .
    For nested stacks , termination protection is set on the root stack and cannot be changed directly on the nested stack.
    See also: AWS API Documentation
    
    
    :example: response = client.update_termination_protection(
        EnableTerminationProtection=True|False,
        StackName='string'
    )
    
    
    :type EnableTerminationProtection: boolean
    :param EnableTerminationProtection: [REQUIRED]\nWhether to enable termination protection on the specified stack.\n

    :type StackName: string
    :param StackName: [REQUIRED]\nThe name or unique ID of the stack for which you want to set termination protection.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'StackId': 'string'
}


Response Structure

(dict) --

StackId (string) --
The unique ID of the stack.








    :return: {
        'StackId': 'string'
    }
    
    
    """
    pass

def validate_template(TemplateBody=None, TemplateURL=None):
    """
    Validates a specified template. AWS CloudFormation first checks if the template is valid JSON. If it isn\'t, AWS CloudFormation checks if the template is valid YAML. If both these checks fail, AWS CloudFormation returns a template validation error.
    See also: AWS API Documentation
    
    
    :example: response = client.validate_template(
        TemplateBody='string',
        TemplateURL='string'
    )
    
    
    :type TemplateBody: string
    :param TemplateBody: Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes. For more information, go to Template Anatomy in the AWS CloudFormation User Guide.\nConditional: You must pass TemplateURL or TemplateBody . If both are passed, only TemplateBody is used.\n

    :type TemplateURL: string
    :param TemplateURL: Location of file containing the template body. The URL must point to a template (max size: 460,800 bytes) that is located in an Amazon S3 bucket. For more information, go to Template Anatomy in the AWS CloudFormation User Guide.\nConditional: You must pass TemplateURL or TemplateBody . If both are passed, only TemplateBody is used.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Parameters': [
        {
            'ParameterKey': 'string',
            'DefaultValue': 'string',
            'NoEcho': True|False,
            'Description': 'string'
        },
    ],
    'Description': 'string',
    'Capabilities': [
        'CAPABILITY_IAM'|'CAPABILITY_NAMED_IAM'|'CAPABILITY_AUTO_EXPAND',
    ],
    'CapabilitiesReason': 'string',
    'DeclaredTransforms': [
        'string',
    ]
}


Response Structure

(dict) --
The output for  ValidateTemplate action.

Parameters (list) --
A list of TemplateParameter structures.

(dict) --
The TemplateParameter data type.

ParameterKey (string) --
The name associated with the parameter.

DefaultValue (string) --
The default value associated with the parameter.

NoEcho (boolean) --
Flag indicating whether the parameter should be displayed as plain text in logs and UIs.

Description (string) --
User defined description associated with the parameter.





Description (string) --
The description found within the template.

Capabilities (list) --
The capabilities found within the template. If your template contains IAM resources, you must specify the CAPABILITY_IAM or CAPABILITY_NAMED_IAM value for this parameter when you use the  CreateStack or  UpdateStack actions with your template; otherwise, those actions return an InsufficientCapabilities error.
For more information, see Acknowledging IAM Resources in AWS CloudFormation Templates .

(string) --


CapabilitiesReason (string) --
The list of resources that generated the values in the Capabilities response element.

DeclaredTransforms (list) --
A list of the transforms that are declared in the template.

(string) --









    :return: {
        'Parameters': [
            {
                'ParameterKey': 'string',
                'DefaultValue': 'string',
                'NoEcho': True|False,
                'Description': 'string'
            },
        ],
        'Description': 'string',
        'Capabilities': [
            'CAPABILITY_IAM'|'CAPABILITY_NAMED_IAM'|'CAPABILITY_AUTO_EXPAND',
        ],
        'CapabilitiesReason': 'string',
        'DeclaredTransforms': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

