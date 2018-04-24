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
    :param operation_name: The operation name. This is the same name
            as the method name on the client. For example, if the
            method name is create_foo, and you'd normally invoke the
            operation as client.create_foo(**kwargs), if the
            create_foo operation can be paginated, you can use the
            call client.get_paginator('create_foo').

    """
    pass

def cancel_update_stack(StackName=None, ClientRequestToken=None):
    """
    Cancels an update on the specified stack. If the call completes successfully, the stack rolls back the update and reverts to the previous stack configuration.
    See also: AWS API Documentation
    
    Examples
    This example cancels an update of the specified stack.
    Expected Output:
    
    :example: response = client.cancel_update_stack(
        StackName='string',
        ClientRequestToken='string'
    )
    
    
    :type StackName: string
    :param StackName: [REQUIRED]
            The name or the unique stack ID that is associated with the stack.
            

    :type ClientRequestToken: string
    :param ClientRequestToken: A unique identifier for this CancelUpdateStack request. Specify this token if you plan to retry requests so that AWS CloudFormation knows that you're not attempting to cancel an update on a stack with the same name. You might retry CancelUpdateStack requests to ensure that AWS CloudFormation successfully received them.

    :return: response = client.cancel_update_stack(
        StackName='MyStack',
    )
    
    print(response)
    
    
    """
    pass

def continue_update_rollback(StackName=None, RoleARN=None, ResourcesToSkip=None, ClientRequestToken=None):
    """
    For a specified stack that is in the UPDATE_ROLLBACK_FAILED state, continues rolling it back to the UPDATE_ROLLBACK_COMPLETE state. Depending on the cause of the failure, you can manually fix the error and continue the rollback. By continuing the rollback, you can return your stack to a working state (the UPDATE_ROLLBACK_COMPLETE state), and then try to update the stack again.
    A stack goes into the UPDATE_ROLLBACK_FAILED state when AWS CloudFormation cannot roll back all changes after a failed stack update. For example, you might have a stack that is rolling back to an old database instance that was deleted outside of AWS CloudFormation. Because AWS CloudFormation doesn't know the database was deleted, it assumes that the database instance still exists and attempts to roll back to it, causing the update rollback to fail.
    See also: AWS API Documentation
    
    
    :example: response = client.continue_update_rollback(
        StackName='string',
        RoleARN='string',
        ResourcesToSkip=[
            'string',
        ],
        ClientRequestToken='string'
    )
    
    
    :type StackName: string
    :param StackName: [REQUIRED]
            The name or the unique ID of the stack that you want to continue rolling back.
            Note
            Don't specify the name of a nested stack (a stack that was created by using the AWS::CloudFormation::Stack resource). Instead, use this operation on the parent stack (the stack that contains the AWS::CloudFormation::Stack resource).
            

    :type RoleARN: string
    :param RoleARN: The Amazon Resource Name (ARN) of an AWS Identity and Access Management (IAM) role that AWS CloudFormation assumes to roll back the stack. AWS CloudFormation uses the role's credentials to make calls on your behalf. AWS CloudFormation always uses this role for all future operations on the stack. As long as users have permission to operate on the stack, AWS CloudFormation uses this role even if the users don't have permission to pass it. Ensure that the role grants least privilege.
            If you don't specify a value, AWS CloudFormation uses the role that was previously associated with the stack. If no role is available, AWS CloudFormation uses a temporary session that is generated from your user credentials.
            

    :type ResourcesToSkip: list
    :param ResourcesToSkip: A list of the logical IDs of the resources that AWS CloudFormation skips during the continue update rollback operation. You can specify only resources that are in the UPDATE_FAILED state because a rollback failed. You can't specify resources that are in the UPDATE_FAILED state for other reasons, for example, because an update was cancelled. To check why a resource update failed, use the DescribeStackResources action, and view the resource status reason.
            Warning
            Specify this property to skip rolling back resources that AWS CloudFormation can't successfully roll back. We recommend that you troubleshoot resources before skipping them. AWS CloudFormation sets the status of the specified resources to UPDATE_COMPLETE and continues to roll back the stack. After the rollback is complete, the state of the skipped resources will be inconsistent with the state of the resources in the stack template. Before performing another stack update, you must update the stack or resources to be consistent with each other. If you don't, subsequent stack updates might fail, and the stack will become unrecoverable.
            Specify the minimum number of resources required to successfully roll back your stack. For example, a failed resource update might cause dependent resources to fail. In this case, it might not be necessary to skip the dependent resources.
            To skip resources that are part of nested stacks, use the following format: NestedStackName.ResourceLogicalID . If you want to specify the logical ID of a stack resource (Type: AWS::CloudFormation::Stack ) in the ResourcesToSkip list, then its corresponding embedded stack must be in one of the following states: DELETE_IN_PROGRESS , DELETE_COMPLETE , or DELETE_FAILED .
            Note
            Don't confuse a child stack's name with its corresponding logical ID defined in the parent stack. For an example of a continue update rollback operation with nested stacks, see Using ResourcesToSkip to recover a nested stacks hierarchy .
            (string) --
            

    :type ClientRequestToken: string
    :param ClientRequestToken: A unique identifier for this ContinueUpdateRollback request. Specify this token if you plan to retry requests so that AWS CloudFormation knows that you're not attempting to continue the rollback to a stack with the same name. You might retry ContinueUpdateRollback requests to ensure that AWS CloudFormation successfully received them.

    :rtype: dict
    :return: {}
    
    
    """
    pass

def create_change_set(StackName=None, TemplateBody=None, TemplateURL=None, UsePreviousTemplate=None, Parameters=None, Capabilities=None, ResourceTypes=None, RoleARN=None, RollbackConfiguration=None, NotificationARNs=None, Tags=None, ChangeSetName=None, ClientToken=None, Description=None, ChangeSetType=None):
    """
    Creates a list of changes that will be applied to a stack so that you can review the changes before executing them. You can create a change set for a stack that doesn't exist or an existing stack. If you create a change set for a stack that doesn't exist, the change set shows all of the resources that AWS CloudFormation will create. If you create a change set for an existing stack, AWS CloudFormation compares the stack's information with the information that you submit in the change set and lists the differences. Use change sets to understand which resources AWS CloudFormation will create or change, and how it will change resources in an existing stack, before you create or update a stack.
    To create a change set for a stack that doesn't exist, for the ChangeSetType parameter, specify CREATE . To create a change set for an existing stack, specify UPDATE for the ChangeSetType parameter. After the CreateChangeSet call successfully completes, AWS CloudFormation starts creating the change set. To check the status of the change set or to review it, use the  DescribeChangeSet action.
    When you are satisfied with the changes the change set will make, execute the change set by using the  ExecuteChangeSet action. AWS CloudFormation doesn't make changes until you execute the change set.
    See also: AWS API Documentation
    
    
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
            'CAPABILITY_IAM'|'CAPABILITY_NAMED_IAM',
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
        ChangeSetType='CREATE'|'UPDATE'
    )
    
    
    :type StackName: string
    :param StackName: [REQUIRED]
            The name or the unique ID of the stack for which you are creating a change set. AWS CloudFormation generates the change set by comparing this stack's information with the information that you submit, such as a modified template or different parameter input values.
            

    :type TemplateBody: string
    :param TemplateBody: A structure that contains the body of the revised template, with a minimum length of 1 byte and a maximum length of 51,200 bytes. AWS CloudFormation generates the change set by comparing this template with the template of the stack that you specified.
            Conditional: You must specify only TemplateBody or TemplateURL .
            

    :type TemplateURL: string
    :param TemplateURL: The location of the file that contains the revised template. The URL must point to a template (max size: 460,800 bytes) that is located in an S3 bucket. AWS CloudFormation generates the change set by comparing this template with the stack that you specified.
            Conditional: You must specify only TemplateBody or TemplateURL .
            

    :type UsePreviousTemplate: boolean
    :param UsePreviousTemplate: Whether to reuse the template that is associated with the stack to create the change set.

    :type Parameters: list
    :param Parameters: A list of Parameter structures that specify input parameters for the change set. For more information, see the Parameter data type.
            (dict) --The Parameter data type.
            ParameterKey (string) --The key associated with the parameter. If you don't specify a key and value for a particular parameter, AWS CloudFormation uses the default value that is specified in your template.
            ParameterValue (string) --The input value associated with the parameter.
            UsePreviousValue (boolean) --During a stack update, use the existing parameter value that the stack is using for a given parameter key. If you specify true , do not specify a parameter value.
            ResolvedValue (string) --Read-only. The value that corresponds to a Systems Manager parameter key. This field is returned only for ` SSM parameter types <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html#aws-ssm-parameter-types>`__ in the template.
            
            

    :type Capabilities: list
    :param Capabilities: A list of values that you must specify before AWS CloudFormation can update certain stacks. Some stack templates might include resources that can affect permissions in your AWS account, for example, by creating new AWS Identity and Access Management (IAM) users. For those stacks, you must explicitly acknowledge their capabilities by specifying this parameter.
            The only valid values are CAPABILITY_IAM and CAPABILITY_NAMED_IAM . The following resources require you to specify this parameter: AWS::IAM::AccessKey , AWS::IAM::Group , AWS::IAM::InstanceProfile , AWS::IAM::Policy , AWS::IAM::Role , AWS::IAM::User , and AWS::IAM::UserToGroupAddition . If your stack template contains these resources, we recommend that you review all permissions associated with them and edit their permissions if necessary.
            If you have IAM resources, you can specify either capability. If you have IAM resources with custom names, you must specify CAPABILITY_NAMED_IAM . If you don't specify this parameter, this action returns an InsufficientCapabilities error.
            For more information, see Acknowledging IAM Resources in AWS CloudFormation Templates .
            (string) --
            

    :type ResourceTypes: list
    :param ResourceTypes: The template resource types that you have permissions to work with if you execute this change set, such as AWS::EC2::Instance , AWS::EC2::* , or Custom::MyCustomInstance .
            If the list of resource types doesn't include a resource type that you're updating, the stack update fails. By default, AWS CloudFormation grants permissions to all resource types. AWS Identity and Access Management (IAM) uses this parameter for condition keys in IAM policies for AWS CloudFormation. For more information, see Controlling Access with AWS Identity and Access Management in the AWS CloudFormation User Guide.
            (string) --
            

    :type RoleARN: string
    :param RoleARN: The Amazon Resource Name (ARN) of an AWS Identity and Access Management (IAM) role that AWS CloudFormation assumes when executing the change set. AWS CloudFormation uses the role's credentials to make calls on your behalf. AWS CloudFormation uses this role for all future operations on the stack. As long as users have permission to operate on the stack, AWS CloudFormation uses this role even if the users don't have permission to pass it. Ensure that the role grants least privilege.
            If you don't specify a value, AWS CloudFormation uses the role that was previously associated with the stack. If no role is available, AWS CloudFormation uses a temporary session that is generated from your user credentials.
            

    :type RollbackConfiguration: dict
    :param RollbackConfiguration: The rollback triggers for AWS CloudFormation to monitor during stack creation and updating operations, and for the specified monitoring period afterwards.
            RollbackTriggers (list) --The triggers to monitor during stack creation or update actions.
            By default, AWS CloudFormation saves the rollback triggers specified for a stack and applies them to any subsequent update operations for the stack, unless you specify otherwise. If you do specify rollback triggers for this parameter, those triggers replace any list of triggers previously specified for the stack. This means:
            To use the rollback triggers previously specified for this stack, if any, don't specify this parameter.
            To specify new or updated rollback triggers, you must specify all the triggers that you want used for this stack, even triggers you've specifed before (for example, when creating the stack or during a previous stack update). Any triggers that you don't include in the updated list of triggers are no longer applied to the stack.
            To remove all currently specified triggers, specify an empty list for this parameter.
            If a specified trigger is missing, the entire stack operation fails and is rolled back.
            (dict) --A rollback trigger AWS CloudFormation monitors during creation and updating of stacks. If any of the alarms you specify goes to ALARM state during the stack operation or within the specified monitoring period afterwards, CloudFormation rolls back the entire stack operation.
            Arn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the rollback trigger.
            If a specified trigger is missing, the entire stack operation fails and is rolled back.
            Type (string) -- [REQUIRED]The resource type of the rollback trigger. Currently, AWS::CloudWatch::Alarm is the only supported resource type.
            
            MonitoringTimeInMinutes (integer) --The amount of time, in minutes, during which CloudFormation should monitor all the rollback triggers after the stack creation or update operation deploys all necessary resources.
            The default is 0 minutes.
            If you specify a monitoring period but do not specify any rollback triggers, CloudFormation still waits the specified period of time before cleaning up old resources after update operations. You can use this monitoring period to perform any manual stack validation desired, and manually cancel the stack creation or update (using CancelUpdateStack , for example) as necessary.
            If you specify 0 for this parameter, CloudFormation still monitors the specified rollback triggers during stack creation and update operations. Then, for update operations, it begins disposing of old resources immediately once the operation completes.
            

    :type NotificationARNs: list
    :param NotificationARNs: The Amazon Resource Names (ARNs) of Amazon Simple Notification Service (Amazon SNS) topics that AWS CloudFormation associates with the stack. To remove all associated notification topics, specify an empty list.
            (string) --
            

    :type Tags: list
    :param Tags: Key-value pairs to associate with this stack. AWS CloudFormation also propagates these tags to resources in the stack. You can specify a maximum of 50 tags.
            (dict) --The Tag type enables you to specify a key-value pair that can be used to store information about an AWS CloudFormation stack.
            Key (string) -- [REQUIRED]
            Required . A string used to identify this tag. You can specify a maximum of 128 characters for a tag key. Tags owned by Amazon Web Services (AWS) have the reserved prefix: aws: .
            Value (string) -- [REQUIRED]
            Required . A string containing the value for this tag. You can specify a maximum of 256 characters for a tag value.
            
            

    :type ChangeSetName: string
    :param ChangeSetName: [REQUIRED]
            The name of the change set. The name must be unique among all change sets that are associated with the specified stack.
            A change set name can contain only alphanumeric, case sensitive characters and hyphens. It must start with an alphabetic character and cannot exceed 128 characters.
            

    :type ClientToken: string
    :param ClientToken: A unique identifier for this CreateChangeSet request. Specify this token if you plan to retry requests so that AWS CloudFormation knows that you're not attempting to create another change set with the same name. You might retry CreateChangeSet requests to ensure that AWS CloudFormation successfully received them.

    :type Description: string
    :param Description: A description to help you identify this change set.

    :type ChangeSetType: string
    :param ChangeSetType: The type of change set operation. To create a change set for a new stack, specify CREATE . To create a change set for an existing stack, specify UPDATE .
            If you create a change set for a new stack, AWS Cloudformation creates a stack with a unique stack ID, but no template or resources. The stack will be in the ` REVIEW_IN_PROGRESS http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-describing-stacks.html#d0e11995`__ state until you execute the change set.
            By default, AWS CloudFormation specifies UPDATE . You can't use the UPDATE type to create a change set for a new stack or the CREATE type to create a change set for an existing stack.
            

    :rtype: dict
    :return: {
        'Id': 'string',
        'StackId': 'string'
    }
    
    
    """
    pass

def create_stack(StackName=None, TemplateBody=None, TemplateURL=None, Parameters=None, DisableRollback=None, RollbackConfiguration=None, TimeoutInMinutes=None, NotificationARNs=None, Capabilities=None, ResourceTypes=None, RoleARN=None, OnFailure=None, StackPolicyBody=None, StackPolicyURL=None, Tags=None, ClientRequestToken=None, EnableTerminationProtection=None):
    """
    Creates a stack as specified in the template. After the call completes successfully, the stack creation starts. You can check the status of the stack via the  DescribeStacks API.
    See also: AWS API Documentation
    
    
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
            'CAPABILITY_IAM'|'CAPABILITY_NAMED_IAM',
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
    :param StackName: [REQUIRED]
            The name that is associated with the stack. The name must be unique in the region in which you are creating the stack.
            Note
            A stack name can contain only alphanumeric characters (case sensitive) and hyphens. It must start with an alphabetic character and cannot be longer than 128 characters.
            

    :type TemplateBody: string
    :param TemplateBody: Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes. For more information, go to Template Anatomy in the AWS CloudFormation User Guide.
            Conditional: You must specify either the TemplateBody or the TemplateURL parameter, but not both.
            

    :type TemplateURL: string
    :param TemplateURL: Location of file containing the template body. The URL must point to a template (max size: 460,800 bytes) that is located in an Amazon S3 bucket. For more information, go to the Template Anatomy in the AWS CloudFormation User Guide.
            Conditional: You must specify either the TemplateBody or the TemplateURL parameter, but not both.
            

    :type Parameters: list
    :param Parameters: A list of Parameter structures that specify input parameters for the stack. For more information, see the Parameter data type.
            (dict) --The Parameter data type.
            ParameterKey (string) --The key associated with the parameter. If you don't specify a key and value for a particular parameter, AWS CloudFormation uses the default value that is specified in your template.
            ParameterValue (string) --The input value associated with the parameter.
            UsePreviousValue (boolean) --During a stack update, use the existing parameter value that the stack is using for a given parameter key. If you specify true , do not specify a parameter value.
            ResolvedValue (string) --Read-only. The value that corresponds to a Systems Manager parameter key. This field is returned only for ` SSM parameter types <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html#aws-ssm-parameter-types>`__ in the template.
            
            

    :type DisableRollback: boolean
    :param DisableRollback: Set to true to disable rollback of the stack if stack creation failed. You can specify either DisableRollback or OnFailure , but not both.
            Default: false
            

    :type RollbackConfiguration: dict
    :param RollbackConfiguration: The rollback triggers for AWS CloudFormation to monitor during stack creation and updating operations, and for the specified monitoring period afterwards.
            RollbackTriggers (list) --The triggers to monitor during stack creation or update actions.
            By default, AWS CloudFormation saves the rollback triggers specified for a stack and applies them to any subsequent update operations for the stack, unless you specify otherwise. If you do specify rollback triggers for this parameter, those triggers replace any list of triggers previously specified for the stack. This means:
            To use the rollback triggers previously specified for this stack, if any, don't specify this parameter.
            To specify new or updated rollback triggers, you must specify all the triggers that you want used for this stack, even triggers you've specifed before (for example, when creating the stack or during a previous stack update). Any triggers that you don't include in the updated list of triggers are no longer applied to the stack.
            To remove all currently specified triggers, specify an empty list for this parameter.
            If a specified trigger is missing, the entire stack operation fails and is rolled back.
            (dict) --A rollback trigger AWS CloudFormation monitors during creation and updating of stacks. If any of the alarms you specify goes to ALARM state during the stack operation or within the specified monitoring period afterwards, CloudFormation rolls back the entire stack operation.
            Arn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the rollback trigger.
            If a specified trigger is missing, the entire stack operation fails and is rolled back.
            Type (string) -- [REQUIRED]The resource type of the rollback trigger. Currently, AWS::CloudWatch::Alarm is the only supported resource type.
            
            MonitoringTimeInMinutes (integer) --The amount of time, in minutes, during which CloudFormation should monitor all the rollback triggers after the stack creation or update operation deploys all necessary resources.
            The default is 0 minutes.
            If you specify a monitoring period but do not specify any rollback triggers, CloudFormation still waits the specified period of time before cleaning up old resources after update operations. You can use this monitoring period to perform any manual stack validation desired, and manually cancel the stack creation or update (using CancelUpdateStack , for example) as necessary.
            If you specify 0 for this parameter, CloudFormation still monitors the specified rollback triggers during stack creation and update operations. Then, for update operations, it begins disposing of old resources immediately once the operation completes.
            

    :type TimeoutInMinutes: integer
    :param TimeoutInMinutes: The amount of time that can pass before the stack status becomes CREATE_FAILED; if DisableRollback is not set or is set to false , the stack will be rolled back.

    :type NotificationARNs: list
    :param NotificationARNs: The Simple Notification Service (SNS) topic ARNs to publish stack related events. You can find your SNS topic ARNs using the SNS console or your Command Line Interface (CLI).
            (string) --
            

    :type Capabilities: list
    :param Capabilities: A list of values that you must specify before AWS CloudFormation can create certain stacks. Some stack templates might include resources that can affect permissions in your AWS account, for example, by creating new AWS Identity and Access Management (IAM) users. For those stacks, you must explicitly acknowledge their capabilities by specifying this parameter.
            The only valid values are CAPABILITY_IAM and CAPABILITY_NAMED_IAM . The following resources require you to specify this parameter: AWS::IAM::AccessKey , AWS::IAM::Group , AWS::IAM::InstanceProfile , AWS::IAM::Policy , AWS::IAM::Role , AWS::IAM::User , and AWS::IAM::UserToGroupAddition . If your stack template contains these resources, we recommend that you review all permissions associated with them and edit their permissions if necessary.
            If you have IAM resources, you can specify either capability. If you have IAM resources with custom names, you must specify CAPABILITY_NAMED_IAM . If you don't specify this parameter, this action returns an InsufficientCapabilities error.
            For more information, see Acknowledging IAM Resources in AWS CloudFormation Templates .
            (string) --
            

    :type ResourceTypes: list
    :param ResourceTypes: The template resource types that you have permissions to work with for this create stack action, such as AWS::EC2::Instance , AWS::EC2::* , or Custom::MyCustomInstance . Use the following syntax to describe template resource types: AWS::* (for all AWS resource), Custom::* (for all custom resources), Custom::*logical_ID* `` (for a specific custom resource), ``AWS::*service_name* ::* (for all resources of a particular AWS service), and ``AWS::service_name ::resource_logical_ID `` (for a specific AWS resource).
            If the list of resource types doesn't include a resource that you're creating, the stack creation fails. By default, AWS CloudFormation grants permissions to all resource types. AWS Identity and Access Management (IAM) uses this parameter for AWS CloudFormation-specific condition keys in IAM policies. For more information, see Controlling Access with AWS Identity and Access Management .
            (string) --
            

    :type RoleARN: string
    :param RoleARN: The Amazon Resource Name (ARN) of an AWS Identity and Access Management (IAM) role that AWS CloudFormation assumes to create the stack. AWS CloudFormation uses the role's credentials to make calls on your behalf. AWS CloudFormation always uses this role for all future operations on the stack. As long as users have permission to operate on the stack, AWS CloudFormation uses this role even if the users don't have permission to pass it. Ensure that the role grants least privilege.
            If you don't specify a value, AWS CloudFormation uses the role that was previously associated with the stack. If no role is available, AWS CloudFormation uses a temporary session that is generated from your user credentials.
            

    :type OnFailure: string
    :param OnFailure: Determines what action will be taken if stack creation fails. This must be one of: DO_NOTHING, ROLLBACK, or DELETE. You can specify either OnFailure or DisableRollback , but not both.
            Default: ROLLBACK
            

    :type StackPolicyBody: string
    :param StackPolicyBody: Structure containing the stack policy body. For more information, go to Prevent Updates to Stack Resources in the AWS CloudFormation User Guide . You can specify either the StackPolicyBody or the StackPolicyURL parameter, but not both.

    :type StackPolicyURL: string
    :param StackPolicyURL: Location of a file containing the stack policy. The URL must point to a policy (maximum size: 16 KB) located in an S3 bucket in the same region as the stack. You can specify either the StackPolicyBody or the StackPolicyURL parameter, but not both.

    :type Tags: list
    :param Tags: Key-value pairs to associate with this stack. AWS CloudFormation also propagates these tags to the resources created in the stack. A maximum number of 50 tags can be specified.
            (dict) --The Tag type enables you to specify a key-value pair that can be used to store information about an AWS CloudFormation stack.
            Key (string) -- [REQUIRED]
            Required . A string used to identify this tag. You can specify a maximum of 128 characters for a tag key. Tags owned by Amazon Web Services (AWS) have the reserved prefix: aws: .
            Value (string) -- [REQUIRED]
            Required . A string containing the value for this tag. You can specify a maximum of 256 characters for a tag value.
            
            

    :type ClientRequestToken: string
    :param ClientRequestToken: A unique identifier for this CreateStack request. Specify this token if you plan to retry requests so that AWS CloudFormation knows that you're not attempting to create a stack with the same name. You might retry CreateStack requests to ensure that AWS CloudFormation successfully received them.
            All events triggered by a given stack operation are assigned the same client request token, which you can use to track operations. For example, if you execute a CreateStack operation with the token token1 , then all the StackEvents generated by that operation will have ClientRequestToken set as token1 .
            In the console, stack operations display the client request token on the Events tab. Stack operations that are initiated from the console use the token format Console-StackOperation-ID , which helps you easily identify the stack operation . For example, if you create a stack using the console, each stack event would be assigned the same token in the following format: Console-CreateStack-7f59c3cf-00d2-40c7-b2ff-e75db0987002 .
            

    :type EnableTerminationProtection: boolean
    :param EnableTerminationProtection: Whether to enable termination protection on the specified stack. If a user attempts to delete a stack with termination protection enabled, the operation fails and the stack remains unchanged. For more information, see Protecting a Stack From Being Deleted in the AWS CloudFormation User Guide . Termination protection is disabled on stacks by default.
            For nested stacks , termination protection is set on the root stack and cannot be changed directly on the nested stack.
            

    :rtype: dict
    :return: {
        'StackId': 'string'
    }
    
    
    """
    pass

def create_stack_instances(StackSetName=None, Accounts=None, Regions=None, ParameterOverrides=None, OperationPreferences=None, OperationId=None):
    """
    Creates stack instances for the specified accounts, within the specified regions. A stack instance refers to a stack in a specific account and region. Accounts and Regions are required parametersyou must specify at least one account and one region.
    See also: AWS API Documentation
    
    
    :example: response = client.create_stack_instances(
        StackSetName='string',
        Accounts=[
            'string',
        ],
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
    :param StackSetName: [REQUIRED]
            The name or unique ID of the stack set that you want to create stack instances from.
            

    :type Accounts: list
    :param Accounts: [REQUIRED]
            The names of one or more AWS accounts that you want to create stack instances in the specified region(s) for.
            (string) --
            

    :type Regions: list
    :param Regions: [REQUIRED]
            The names of one or more regions where you want to create stack instances using the specified AWS account(s).
            (string) --
            

    :type ParameterOverrides: list
    :param ParameterOverrides: A list of stack set parameters whose values you want to override in the selected stack instances.
            Any overridden parameter values will be applied to all stack instances in the specified accounts and regions. When specifying parameters and their values, be aware of how AWS CloudFormation sets parameter values during stack instance operations:
            To override the current value for a parameter, include the parameter and specify its value.
            To leave a parameter set to its present value, you can do one of the following:
            Do not include the parameter in the list.
            Include the parameter and specify UsePreviousValue as true . (You cannot specify both a value and set UsePreviousValue to true .)
            To set all overridden parameter back to the values specified in the stack set, specify a parameter list but do not include any parameters.
            To leave all parameters set to their present values, do not specify this property at all.
            During stack set updates, any parameter values overridden for a stack instance are not updated, but retain their overridden value.
            You can only override the parameter values that are specified in the stack set; to add or delete a parameter itself, use UpdateStackSet to update the stack set template.
            (dict) --The Parameter data type.
            ParameterKey (string) --The key associated with the parameter. If you don't specify a key and value for a particular parameter, AWS CloudFormation uses the default value that is specified in your template.
            ParameterValue (string) --The input value associated with the parameter.
            UsePreviousValue (boolean) --During a stack update, use the existing parameter value that the stack is using for a given parameter key. If you specify true , do not specify a parameter value.
            ResolvedValue (string) --Read-only. The value that corresponds to a Systems Manager parameter key. This field is returned only for ` SSM parameter types <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html#aws-ssm-parameter-types>`__ in the template.
            
            

    :type OperationPreferences: dict
    :param OperationPreferences: Preferences for how AWS CloudFormation performs this stack set operation.
            RegionOrder (list) --The order of the regions in where you want to perform the stack operation.
            (string) --
            FailureToleranceCount (integer) --The number of accounts, per region, for which this operation can fail before AWS CloudFormation stops the operation in that region. If the operation is stopped in a region, AWS CloudFormation doesn't attempt the operation in any subsequent regions.
            Conditional: You must specify either FailureToleranceCount or FailureTolerancePercentage (but not both).
            FailureTolerancePercentage (integer) --The percentage of accounts, per region, for which this stack operation can fail before AWS CloudFormation stops the operation in that region. If the operation is stopped in a region, AWS CloudFormation doesn't attempt the operation in any subsequent regions.
            When calculating the number of accounts based on the specified percentage, AWS CloudFormation rounds down to the next whole number.
            Conditional: You must specify either FailureToleranceCount or FailureTolerancePercentage , but not both.
            MaxConcurrentCount (integer) --The maximum number of accounts in which to perform this operation at one time. This is dependent on the value of FailureToleranceCount  MaxConcurrentCount is at most one more than the FailureToleranceCount .
            Note that this setting lets you specify the maximum for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling.
            Conditional: You must specify either MaxConcurrentCount or MaxConcurrentPercentage , but not both.
            MaxConcurrentPercentage (integer) --The maximum percentage of accounts in which to perform this operation at one time.
            When calculating the number of accounts based on the specified percentage, AWS CloudFormation rounds down to the next whole number. This is true except in cases where rounding down would result is zero. In this case, CloudFormation sets the number as one instead.
            Note that this setting lets you specify the maximum for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling.
            Conditional: You must specify either MaxConcurrentCount or MaxConcurrentPercentage , but not both.
            

    :type OperationId: string
    :param OperationId: The unique identifier for this stack set operation.
            The operation ID also functions as an idempotency token, to ensure that AWS CloudFormation performs the stack set operation only once, even if you retry the request multiple times. You might retry stack set operation requests to ensure that AWS CloudFormation successfully received them.
            If you don't specify an operation ID, the SDK generates one automatically.
            Repeating this stack set operation with a new operation ID retries all stack instances whose status is OUTDATED .
            This field is autopopulated if not provided.
            

    :rtype: dict
    :return: {
        'OperationId': 'string'
    }
    
    
    """
    pass

def create_stack_set(StackSetName=None, Description=None, TemplateBody=None, TemplateURL=None, Parameters=None, Capabilities=None, Tags=None, AdministrationRoleARN=None, ClientRequestToken=None):
    """
    Creates a stack set.
    See also: AWS API Documentation
    
    
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
            'CAPABILITY_IAM'|'CAPABILITY_NAMED_IAM',
        ],
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        AdministrationRoleARN='string',
        ClientRequestToken='string'
    )
    
    
    :type StackSetName: string
    :param StackSetName: [REQUIRED]
            The name to associate with the stack set. The name must be unique in the region where you create your stack set.
            Note
            A stack name can contain only alphanumeric characters (case-sensitive) and hyphens. It must start with an alphabetic character and can't be longer than 128 characters.
            

    :type Description: string
    :param Description: A description of the stack set. You can use the description to identify the stack set's purpose or other important information.

    :type TemplateBody: string
    :param TemplateBody: The structure that contains the template body, with a minimum length of 1 byte and a maximum length of 51,200 bytes. For more information, see Template Anatomy in the AWS CloudFormation User Guide.
            Conditional: You must specify either the TemplateBody or the TemplateURL parameter, but not both.
            

    :type TemplateURL: string
    :param TemplateURL: The location of the file that contains the template body. The URL must point to a template (maximum size: 460,800 bytes) that's located in an Amazon S3 bucket. For more information, see Template Anatomy in the AWS CloudFormation User Guide.
            Conditional: You must specify either the TemplateBody or the TemplateURL parameter, but not both.
            

    :type Parameters: list
    :param Parameters: The input parameters for the stack set template.
            (dict) --The Parameter data type.
            ParameterKey (string) --The key associated with the parameter. If you don't specify a key and value for a particular parameter, AWS CloudFormation uses the default value that is specified in your template.
            ParameterValue (string) --The input value associated with the parameter.
            UsePreviousValue (boolean) --During a stack update, use the existing parameter value that the stack is using for a given parameter key. If you specify true , do not specify a parameter value.
            ResolvedValue (string) --Read-only. The value that corresponds to a Systems Manager parameter key. This field is returned only for ` SSM parameter types <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html#aws-ssm-parameter-types>`__ in the template.
            
            

    :type Capabilities: list
    :param Capabilities: A list of values that you must specify before AWS CloudFormation can create certain stack sets. Some stack set templates might include resources that can affect permissions in your AWS account for example, by creating new AWS Identity and Access Management (IAM) users. For those stack sets, you must explicitly acknowledge their capabilities by specifying this parameter.
            The only valid values are CAPABILITY_IAM and CAPABILITY_NAMED_IAM. The following resources require you to specify this parameter:
            AWS::IAM::AccessKey
            AWS::IAM::Group
            AWS::IAM::InstanceProfile
            AWS::IAM::Policy
            AWS::IAM::Role
            AWS::IAM::User
            AWS::IAM::UserToGroupAddition
            If your stack template contains these resources, we recommend that you review all permissions that are associated with them and edit their permissions if necessary.
            If you have IAM resources, you can specify either capability. If you have IAM resources with custom names, you must specify CAPABILITY_NAMED_IAM. If you don't specify this parameter, this action returns an InsufficientCapabilities error.
            For more information, see Acknowledging IAM Resources in AWS CloudFormation Templates.
            (string) --
            

    :type Tags: list
    :param Tags: The key-value pairs to associate with this stack set and the stacks created from it. AWS CloudFormation also propagates these tags to supported resources that are created in the stacks. A maximum number of 50 tags can be specified.
            If you specify tags as part of a CreateStackSet action, AWS CloudFormation checks to see if you have the required IAM permission to tag resources. If you don't, the entire CreateStackSet action fails with an access denied error, and the stack set is not created.
            (dict) --The Tag type enables you to specify a key-value pair that can be used to store information about an AWS CloudFormation stack.
            Key (string) -- [REQUIRED]
            Required . A string used to identify this tag. You can specify a maximum of 128 characters for a tag key. Tags owned by Amazon Web Services (AWS) have the reserved prefix: aws: .
            Value (string) -- [REQUIRED]
            Required . A string containing the value for this tag. You can specify a maximum of 256 characters for a tag value.
            
            

    :type AdministrationRoleARN: string
    :param AdministrationRoleARN: The Amazon Resource Number (ARN) of the IAM role to use to create this stack set.
            Specify an IAM role only if you are using customized administrator roles to control which users or groups can manage specific stack sets within the same administrator account. For more information, see Define Permissions for Multiple Administrators in the AWS CloudFormation User Guide .
            

    :type ClientRequestToken: string
    :param ClientRequestToken: A unique identifier for this CreateStackSet request. Specify this token if you plan to retry requests so that AWS CloudFormation knows that you're not attempting to create another stack set with the same name. You might retry CreateStackSet requests to ensure that AWS CloudFormation successfully received them.
            If you don't specify an operation ID, the SDK generates one automatically.
            This field is autopopulated if not provided.
            

    :rtype: dict
    :return: {
        'StackSetId': 'string'
    }
    
    
    """
    pass

def delete_change_set(ChangeSetName=None, StackName=None):
    """
    Deletes the specified change set. Deleting change sets ensures that no one executes the wrong change set.
    If the call successfully completes, AWS CloudFormation successfully deleted the change set.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_change_set(
        ChangeSetName='string',
        StackName='string'
    )
    
    
    :type ChangeSetName: string
    :param ChangeSetName: [REQUIRED]
            The name or Amazon Resource Name (ARN) of the change set that you want to delete.
            

    :type StackName: string
    :param StackName: If you specified the name of a change set to delete, specify the stack name or ID (ARN) that is associated with it.

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_stack(StackName=None, RetainResources=None, RoleARN=None, ClientRequestToken=None):
    """
    Deletes a specified stack. Once the call completes successfully, stack deletion starts. Deleted stacks do not show up in the  DescribeStacks API if the deletion has been completed successfully.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_stack(
        StackName='string',
        RetainResources=[
            'string',
        ],
        RoleARN='string',
        ClientRequestToken='string'
    )
    
    
    :type StackName: string
    :param StackName: [REQUIRED]
            The name or the unique stack ID that is associated with the stack.
            

    :type RetainResources: list
    :param RetainResources: For stacks in the DELETE_FAILED state, a list of resource logical IDs that are associated with the resources you want to retain. During deletion, AWS CloudFormation deletes the stack but does not delete the retained resources.
            Retaining resources is useful when you cannot delete a resource, such as a non-empty S3 bucket, but you want to delete the stack.
            (string) --
            

    :type RoleARN: string
    :param RoleARN: The Amazon Resource Name (ARN) of an AWS Identity and Access Management (IAM) role that AWS CloudFormation assumes to delete the stack. AWS CloudFormation uses the role's credentials to make calls on your behalf.
            If you don't specify a value, AWS CloudFormation uses the role that was previously associated with the stack. If no role is available, AWS CloudFormation uses a temporary session that is generated from your user credentials.
            

    :type ClientRequestToken: string
    :param ClientRequestToken: A unique identifier for this DeleteStack request. Specify this token if you plan to retry requests so that AWS CloudFormation knows that you're not attempting to delete a stack with the same name. You might retry DeleteStack requests to ensure that AWS CloudFormation successfully received them.
            All events triggered by a given stack operation are assigned the same client request token, which you can use to track operations. For example, if you execute a CreateStack operation with the token token1 , then all the StackEvents generated by that operation will have ClientRequestToken set as token1 .
            In the console, stack operations display the client request token on the Events tab. Stack operations that are initiated from the console use the token format Console-StackOperation-ID , which helps you easily identify the stack operation . For example, if you create a stack using the console, each stack event would be assigned the same token in the following format: Console-CreateStack-7f59c3cf-00d2-40c7-b2ff-e75db0987002 .
            

    """
    pass

def delete_stack_instances(StackSetName=None, Accounts=None, Regions=None, OperationPreferences=None, RetainStacks=None, OperationId=None):
    """
    Deletes stack instances for the specified accounts, in the specified regions.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_stack_instances(
        StackSetName='string',
        Accounts=[
            'string',
        ],
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
    :param StackSetName: [REQUIRED]
            The name or unique ID of the stack set that you want to delete stack instances for.
            

    :type Accounts: list
    :param Accounts: [REQUIRED]
            The names of the AWS accounts that you want to delete stack instances for.
            (string) --
            

    :type Regions: list
    :param Regions: [REQUIRED]
            The regions where you want to delete stack set instances.
            (string) --
            

    :type OperationPreferences: dict
    :param OperationPreferences: Preferences for how AWS CloudFormation performs this stack set operation.
            RegionOrder (list) --The order of the regions in where you want to perform the stack operation.
            (string) --
            FailureToleranceCount (integer) --The number of accounts, per region, for which this operation can fail before AWS CloudFormation stops the operation in that region. If the operation is stopped in a region, AWS CloudFormation doesn't attempt the operation in any subsequent regions.
            Conditional: You must specify either FailureToleranceCount or FailureTolerancePercentage (but not both).
            FailureTolerancePercentage (integer) --The percentage of accounts, per region, for which this stack operation can fail before AWS CloudFormation stops the operation in that region. If the operation is stopped in a region, AWS CloudFormation doesn't attempt the operation in any subsequent regions.
            When calculating the number of accounts based on the specified percentage, AWS CloudFormation rounds down to the next whole number.
            Conditional: You must specify either FailureToleranceCount or FailureTolerancePercentage , but not both.
            MaxConcurrentCount (integer) --The maximum number of accounts in which to perform this operation at one time. This is dependent on the value of FailureToleranceCount  MaxConcurrentCount is at most one more than the FailureToleranceCount .
            Note that this setting lets you specify the maximum for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling.
            Conditional: You must specify either MaxConcurrentCount or MaxConcurrentPercentage , but not both.
            MaxConcurrentPercentage (integer) --The maximum percentage of accounts in which to perform this operation at one time.
            When calculating the number of accounts based on the specified percentage, AWS CloudFormation rounds down to the next whole number. This is true except in cases where rounding down would result is zero. In this case, CloudFormation sets the number as one instead.
            Note that this setting lets you specify the maximum for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling.
            Conditional: You must specify either MaxConcurrentCount or MaxConcurrentPercentage , but not both.
            

    :type RetainStacks: boolean
    :param RetainStacks: [REQUIRED]
            Removes the stack instances from the specified stack set, but doesn't delete the stacks. You can't reassociate a retained stack or add an existing, saved stack to a new stack set.
            For more information, see Stack set operation options .
            

    :type OperationId: string
    :param OperationId: The unique identifier for this stack set operation.
            If you don't specify an operation ID, the SDK generates one automatically.
            The operation ID also functions as an idempotency token, to ensure that AWS CloudFormation performs the stack set operation only once, even if you retry the request multiple times. You can retry stack set operation requests to ensure that AWS CloudFormation successfully received them.
            Repeating this stack set operation with a new operation ID retries all stack instances whose status is OUTDATED .
            This field is autopopulated if not provided.
            

    :rtype: dict
    :return: {
        'OperationId': 'string'
    }
    
    
    """
    pass

def delete_stack_set(StackSetName=None):
    """
    Deletes a stack set. Before you can delete a stack set, all of its member stack instances must be deleted. For more information about how to do this, see  DeleteStackInstances .
    See also: AWS API Documentation
    
    
    :example: response = client.delete_stack_set(
        StackSetName='string'
    )
    
    
    :type StackSetName: string
    :param StackSetName: [REQUIRED]
            The name or unique ID of the stack set that you're deleting. You can obtain this value by running ListStackSets .
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def describe_account_limits(NextToken=None):
    """
    Retrieves your account's AWS CloudFormation limits, such as the maximum number of stacks that you can create in your account.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_account_limits(
        NextToken='string'
    )
    
    
    :type NextToken: string
    :param NextToken: A string that identifies the next page of limits that you want to retrieve.

    :rtype: dict
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
    
    
    :example: response = client.describe_change_set(
        ChangeSetName='string',
        StackName='string',
        NextToken='string'
    )
    
    
    :type ChangeSetName: string
    :param ChangeSetName: [REQUIRED]
            The name or Amazon Resource Name (ARN) of the change set that you want to describe.
            

    :type StackName: string
    :param StackName: If you specified the name of a change set, specify the stack name or ID (ARN) of the change set you want to describe.

    :type NextToken: string
    :param NextToken: A string (provided by the DescribeChangeSet response output) that identifies the next page of information that you want to retrieve.

    :rtype: dict
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
            'CAPABILITY_IAM'|'CAPABILITY_NAMED_IAM',
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
                    'Action': 'Add'|'Modify'|'Remove',
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

def describe_stack_events(StackName=None, NextToken=None):
    """
    Returns all stack related events for a specified stack in reverse chronological order. For more information about a stack's event history, go to Stacks in the AWS CloudFormation User Guide.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_stack_events(
        StackName='string',
        NextToken='string'
    )
    
    
    :type StackName: string
    :param StackName: The name or the unique stack ID that is associated with the stack, which are not always interchangeable:
            Running stacks: You can specify either the stack's name or its unique stack ID.
            Deleted stacks: You must specify the unique stack ID.
            Default: There is no default value.
            

    :type NextToken: string
    :param NextToken: A string that identifies the next page of events that you want to retrieve.

    :rtype: dict
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
                'ResourceStatus': 'CREATE_IN_PROGRESS'|'CREATE_FAILED'|'CREATE_COMPLETE'|'DELETE_IN_PROGRESS'|'DELETE_FAILED'|'DELETE_COMPLETE'|'DELETE_SKIPPED'|'UPDATE_IN_PROGRESS'|'UPDATE_FAILED'|'UPDATE_COMPLETE',
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
    Returns the stack instance that's associated with the specified stack set, AWS account, and region.
    For a list of stack instances that are associated with a specific stack set, use  ListStackInstances .
    See also: AWS API Documentation
    
    
    :example: response = client.describe_stack_instance(
        StackSetName='string',
        StackInstanceAccount='string',
        StackInstanceRegion='string'
    )
    
    
    :type StackSetName: string
    :param StackSetName: [REQUIRED]
            The name or the unique stack ID of the stack set that you want to get stack instance information for.
            

    :type StackInstanceAccount: string
    :param StackInstanceAccount: [REQUIRED]
            The ID of an AWS account that's associated with this stack instance.
            

    :type StackInstanceRegion: string
    :param StackInstanceRegion: [REQUIRED]
            The name of a region that's associated with this stack instance.
            

    :rtype: dict
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
            'StatusReason': 'string'
        }
    }
    
    
    :returns: 
    INOPERABLE : A DeleteStackInstances operation has failed and left the stack in an unstable state. Stacks in this state are excluded from further UpdateStackSet operations. You might need to perform a DeleteStackInstances operation, with RetainStacks set to true , to delete the stack instance, and then delete the stack manually.
    OUTDATED : The stack isn't currently up to date with the stack set because:
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
    :param StackName: [REQUIRED]
            The name or the unique stack ID that is associated with the stack, which are not always interchangeable:
            Running stacks: You can specify either the stack's name or its unique stack ID.
            Deleted stacks: You must specify the unique stack ID.
            Default: There is no default value.
            

    :type LogicalResourceId: string
    :param LogicalResourceId: [REQUIRED]
            The logical name of the resource as specified in the template.
            Default: There is no default value.
            

    :rtype: dict
    :return: {
        'StackResourceDetail': {
            'StackName': 'string',
            'StackId': 'string',
            'LogicalResourceId': 'string',
            'PhysicalResourceId': 'string',
            'ResourceType': 'string',
            'LastUpdatedTimestamp': datetime(2015, 1, 1),
            'ResourceStatus': 'CREATE_IN_PROGRESS'|'CREATE_FAILED'|'CREATE_COMPLETE'|'DELETE_IN_PROGRESS'|'DELETE_FAILED'|'DELETE_COMPLETE'|'DELETE_SKIPPED'|'UPDATE_IN_PROGRESS'|'UPDATE_FAILED'|'UPDATE_COMPLETE',
            'ResourceStatusReason': 'string',
            'Description': 'string',
            'Metadata': 'string'
        }
    }
    
    
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
    :param StackName: The name or the unique stack ID that is associated with the stack, which are not always interchangeable:
            Running stacks: You can specify either the stack's name or its unique stack ID.
            Deleted stacks: You must specify the unique stack ID.
            Default: There is no default value.
            Required: Conditional. If you do not specify StackName , you must specify PhysicalResourceId .
            

    :type LogicalResourceId: string
    :param LogicalResourceId: The logical name of the resource as specified in the template.
            Default: There is no default value.
            

    :type PhysicalResourceId: string
    :param PhysicalResourceId: The name or unique identifier that corresponds to a physical instance ID of a resource supported by AWS CloudFormation.
            For example, for an Amazon Elastic Compute Cloud (EC2) instance, PhysicalResourceId corresponds to the InstanceId . You can pass the EC2 InstanceId to DescribeStackResources to find which stack the instance belongs to and what other resources are part of the stack.
            Required: Conditional. If you do not specify PhysicalResourceId , you must specify StackName .
            Default: There is no default value.
            

    :rtype: dict
    :return: {
        'StackResources': [
            {
                'StackName': 'string',
                'StackId': 'string',
                'LogicalResourceId': 'string',
                'PhysicalResourceId': 'string',
                'ResourceType': 'string',
                'Timestamp': datetime(2015, 1, 1),
                'ResourceStatus': 'CREATE_IN_PROGRESS'|'CREATE_FAILED'|'CREATE_COMPLETE'|'DELETE_IN_PROGRESS'|'DELETE_FAILED'|'DELETE_COMPLETE'|'DELETE_SKIPPED'|'UPDATE_IN_PROGRESS'|'UPDATE_FAILED'|'UPDATE_COMPLETE',
                'ResourceStatusReason': 'string',
                'Description': 'string'
            },
        ]
    }
    
    
    """
    pass

def describe_stack_set(StackSetName=None):
    """
    Returns the description of the specified stack set.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_stack_set(
        StackSetName='string'
    )
    
    
    :type StackSetName: string
    :param StackSetName: [REQUIRED]
            The name or unique ID of the stack set whose description you want.
            

    :rtype: dict
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
                'CAPABILITY_IAM'|'CAPABILITY_NAMED_IAM',
            ],
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'StackSetARN': 'string',
            'AdministrationRoleARN': 'string'
        }
    }
    
    
    """
    pass

def describe_stack_set_operation(StackSetName=None, OperationId=None):
    """
    Returns the description of the specified stack set operation.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_stack_set_operation(
        StackSetName='string',
        OperationId='string'
    )
    
    
    :type StackSetName: string
    :param StackSetName: [REQUIRED]
            The name or the unique stack ID of the stack set for the stack operation.
            

    :type OperationId: string
    :param OperationId: [REQUIRED]
            The unique ID of the stack set operation.
            

    :rtype: dict
    :return: {
        'StackSetOperation': {
            'OperationId': 'string',
            'StackSetId': 'string',
            'Action': 'CREATE'|'UPDATE'|'DELETE',
            'Status': 'RUNNING'|'SUCCEEDED'|'FAILED'|'STOPPING'|'STOPPED',
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
            'CreationTimestamp': datetime(2015, 1, 1),
            'EndTimestamp': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    FAILED : The operation exceeded the specified failure tolerance. The failure tolerance value that you've set for an operation is applied for each region during stack create and update operations. If the number of failed stacks within a region exceeds the failure tolerance, the status of the operation in the region is set to FAILED . This in turn sets the status of the operation as a whole to FAILED , and AWS CloudFormation cancels the operation in any remaining regions.
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
    :param StackName: The name or the unique stack ID that is associated with the stack, which are not always interchangeable:
            Running stacks: You can specify either the stack's name or its unique stack ID.
            Deleted stacks: You must specify the unique stack ID.
            Default: There is no default value.
            

    :type NextToken: string
    :param NextToken: A string that identifies the next page of stacks that you want to retrieve.

    :rtype: dict
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
                'StackStatus': 'CREATE_IN_PROGRESS'|'CREATE_FAILED'|'CREATE_COMPLETE'|'ROLLBACK_IN_PROGRESS'|'ROLLBACK_FAILED'|'ROLLBACK_COMPLETE'|'DELETE_IN_PROGRESS'|'DELETE_FAILED'|'DELETE_COMPLETE'|'UPDATE_IN_PROGRESS'|'UPDATE_COMPLETE_CLEANUP_IN_PROGRESS'|'UPDATE_COMPLETE'|'UPDATE_ROLLBACK_IN_PROGRESS'|'UPDATE_ROLLBACK_FAILED'|'UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS'|'UPDATE_ROLLBACK_COMPLETE'|'REVIEW_IN_PROGRESS',
                'StackStatusReason': 'string',
                'DisableRollback': True|False,
                'NotificationARNs': [
                    'string',
                ],
                'TimeoutInMinutes': 123,
                'Capabilities': [
                    'CAPABILITY_IAM'|'CAPABILITY_NAMED_IAM',
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
                'RootId': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    To use the rollback triggers previously specified for this stack, if any, don't specify this parameter.
    To specify new or updated rollback triggers, you must specify all the triggers that you want used for this stack, even triggers you've specifed before (for example, when creating the stack or during a previous stack update). Any triggers that you don't include in the updated list of triggers are no longer applied to the stack.
    To remove all currently specified triggers, specify an empty list for this parameter.
    
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
    :param TemplateBody: Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes. (For more information, go to Template Anatomy in the AWS CloudFormation User Guide.)
            Conditional: You must pass TemplateBody or TemplateURL . If both are passed, only TemplateBody is used.
            

    :type TemplateURL: string
    :param TemplateURL: Location of file containing the template body. The URL must point to a template that is located in an Amazon S3 bucket. For more information, go to Template Anatomy in the AWS CloudFormation User Guide.
            Conditional: You must pass TemplateURL or TemplateBody . If both are passed, only TemplateBody is used.
            

    :type Parameters: list
    :param Parameters: A list of Parameter structures that specify input parameters.
            (dict) --The Parameter data type.
            ParameterKey (string) --The key associated with the parameter. If you don't specify a key and value for a particular parameter, AWS CloudFormation uses the default value that is specified in your template.
            ParameterValue (string) --The input value associated with the parameter.
            UsePreviousValue (boolean) --During a stack update, use the existing parameter value that the stack is using for a given parameter key. If you specify true , do not specify a parameter value.
            ResolvedValue (string) --Read-only. The value that corresponds to a Systems Manager parameter key. This field is returned only for ` SSM parameter types <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html#aws-ssm-parameter-types>`__ in the template.
            
            

    :rtype: dict
    :return: {
        'Url': 'string'
    }
    
    
    """
    pass

def execute_change_set(ChangeSetName=None, StackName=None, ClientRequestToken=None):
    """
    Updates a stack using the input information that was provided when the specified change set was created. After the call successfully completes, AWS CloudFormation starts updating the stack. Use the  DescribeStacks action to view the status of the update.
    When you execute a change set, AWS CloudFormation deletes all other change sets associated with the stack because they aren't valid for the updated stack.
    If a stack policy is associated with the stack, AWS CloudFormation enforces the policy during the update. You can't specify a temporary stack policy that overrides the current policy.
    See also: AWS API Documentation
    
    
    :example: response = client.execute_change_set(
        ChangeSetName='string',
        StackName='string',
        ClientRequestToken='string'
    )
    
    
    :type ChangeSetName: string
    :param ChangeSetName: [REQUIRED]
            The name or ARN of the change set that you want use to update the specified stack.
            

    :type StackName: string
    :param StackName: If you specified the name of a change set, specify the stack name or ID (ARN) that is associated with the change set you want to execute.

    :type ClientRequestToken: string
    :param ClientRequestToken: A unique identifier for this ExecuteChangeSet request. Specify this token if you plan to retry requests so that AWS CloudFormation knows that you're not attempting to execute a change set to update a stack with the same name. You might retry ExecuteChangeSet requests to ensure that AWS CloudFormation successfully received them.

    :rtype: dict
    :return: {}
    
    
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

def get_stack_policy(StackName=None):
    """
    Returns the stack policy for a specified stack. If a stack doesn't have a policy, a null value is returned.
    See also: AWS API Documentation
    
    
    :example: response = client.get_stack_policy(
        StackName='string'
    )
    
    
    :type StackName: string
    :param StackName: [REQUIRED]
            The name or unique stack ID that is associated with the stack whose policy you want to get.
            

    :rtype: dict
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
    
    
    :example: response = client.get_template(
        StackName='string',
        ChangeSetName='string',
        TemplateStage='Original'|'Processed'
    )
    
    
    :type StackName: string
    :param StackName: The name or the unique stack ID that is associated with the stack, which are not always interchangeable:
            Running stacks: You can specify either the stack's name or its unique stack ID.
            Deleted stacks: You must specify the unique stack ID.
            Default: There is no default value.
            

    :type ChangeSetName: string
    :param ChangeSetName: The name or Amazon Resource Name (ARN) of a change set for which AWS CloudFormation returns the associated template. If you specify a name, you must also specify the StackName .

    :type TemplateStage: string
    :param TemplateStage: For templates that include transforms, the stage of the template that AWS CloudFormation returns. To get the user-submitted template, specify Original . To get the template after AWS CloudFormation has processed all transforms, specify Processed .
            If the template doesn't include transforms, Original and Processed return the same template. By default, AWS CloudFormation specifies Original .
            

    :rtype: dict
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
    
    
    :example: response = client.get_template_summary(
        TemplateBody='string',
        TemplateURL='string',
        StackName='string',
        StackSetName='string'
    )
    
    
    :type TemplateBody: string
    :param TemplateBody: Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes. For more information about templates, see Template Anatomy in the AWS CloudFormation User Guide.
            Conditional: You must specify only one of the following parameters: StackName , StackSetName , TemplateBody , or TemplateURL .
            

    :type TemplateURL: string
    :param TemplateURL: Location of file containing the template body. The URL must point to a template (max size: 460,800 bytes) that is located in an Amazon S3 bucket. For more information about templates, see Template Anatomy in the AWS CloudFormation User Guide.
            Conditional: You must specify only one of the following parameters: StackName , StackSetName , TemplateBody , or TemplateURL .
            

    :type StackName: string
    :param StackName: The name or the stack ID that is associated with the stack, which are not always interchangeable. For running stacks, you can specify either the stack's name or its unique stack ID. For deleted stack, you must specify the unique stack ID.
            Conditional: You must specify only one of the following parameters: StackName , StackSetName , TemplateBody , or TemplateURL .
            

    :type StackSetName: string
    :param StackSetName: The name or unique ID of the stack set from which the stack was created.
            Conditional: You must specify only one of the following parameters: StackName , StackSetName , TemplateBody , or TemplateURL .
            

    :rtype: dict
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
            'CAPABILITY_IAM'|'CAPABILITY_NAMED_IAM',
        ],
        'CapabilitiesReason': 'string',
        'ResourceTypes': [
            'string',
        ],
        'Version': 'string',
        'Metadata': 'string',
        'DeclaredTransforms': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_waiter():
    """
    
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
    :param StackName: [REQUIRED]
            The name or the Amazon Resource Name (ARN) of the stack for which you want to list change sets.
            

    :type NextToken: string
    :param NextToken: A string (provided by the ListChangeSets response output) that identifies the next page of change sets that you want to retrieve.

    :rtype: dict
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
    Lists all exported output values in the account and region in which you call this action. Use this action to see the exported output values that you can import into other stacks. To import values, use the ` Fn::ImportValue http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-importvalue.html`__ function.
    For more information, see AWS CloudFormation Export Stack Output Values .
    See also: AWS API Documentation
    
    
    :example: response = client.list_exports(
        NextToken='string'
    )
    
    
    :type NextToken: string
    :param NextToken: A string (provided by the ListExports response output) that identifies the next page of exported output values that you asked to retrieve.

    :rtype: dict
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
    For more information about importing an exported output value, see the ` Fn::ImportValue http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-importvalue.html`__ function.
    See also: AWS API Documentation
    
    
    :example: response = client.list_imports(
        ExportName='string',
        NextToken='string'
    )
    
    
    :type ExportName: string
    :param ExportName: [REQUIRED]
            The name of the exported output value. AWS CloudFormation returns the stack names that are importing this value.
            

    :type NextToken: string
    :param NextToken: A string (provided by the ListImports response output) that identifies the next page of stacks that are importing the specified exported output value.

    :rtype: dict
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
    Returns summary information about stack instances that are associated with the specified stack set. You can filter for stack instances that are associated with a specific AWS account name or region.
    See also: AWS API Documentation
    
    
    :example: response = client.list_stack_instances(
        StackSetName='string',
        NextToken='string',
        MaxResults=123,
        StackInstanceAccount='string',
        StackInstanceRegion='string'
    )
    
    
    :type StackSetName: string
    :param StackSetName: [REQUIRED]
            The name or unique ID of the stack set that you want to list stack instances for.
            

    :type NextToken: string
    :param NextToken: If the previous request didn't return all of the remaining results, the response's NextToken parameter value is set to a token. To retrieve the next set of results, call ListStackInstances again and assign that token to the request object's NextToken parameter. If there are no remaining results, the previous response object's NextToken parameter is set to null .

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a NextToken value that you can assign to the NextToken request parameter to get the next set of results.

    :type StackInstanceAccount: string
    :param StackInstanceAccount: The name of the AWS account that you want to list stack instances for.

    :type StackInstanceRegion: string
    :param StackInstanceRegion: The name of the region where you want to list stack instances.

    :rtype: dict
    :return: {
        'Summaries': [
            {
                'StackSetId': 'string',
                'Region': 'string',
                'Account': 'string',
                'StackId': 'string',
                'Status': 'CURRENT'|'OUTDATED'|'INOPERABLE',
                'StatusReason': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    INOPERABLE : A DeleteStackInstances operation has failed and left the stack in an unstable state. Stacks in this state are excluded from further UpdateStackSet operations. You might need to perform a DeleteStackInstances operation, with RetainStacks set to true , to delete the stack instance, and then delete the stack manually.
    OUTDATED : The stack isn't currently up to date with the stack set because:
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
    :param StackName: [REQUIRED]
            The name or the unique stack ID that is associated with the stack, which are not always interchangeable:
            Running stacks: You can specify either the stack's name or its unique stack ID.
            Deleted stacks: You must specify the unique stack ID.
            Default: There is no default value.
            

    :type NextToken: string
    :param NextToken: A string that identifies the next page of stack resources that you want to retrieve.

    :rtype: dict
    :return: {
        'StackResourceSummaries': [
            {
                'LogicalResourceId': 'string',
                'PhysicalResourceId': 'string',
                'ResourceType': 'string',
                'LastUpdatedTimestamp': datetime(2015, 1, 1),
                'ResourceStatus': 'CREATE_IN_PROGRESS'|'CREATE_FAILED'|'CREATE_COMPLETE'|'DELETE_IN_PROGRESS'|'DELETE_FAILED'|'DELETE_COMPLETE'|'DELETE_SKIPPED'|'UPDATE_IN_PROGRESS'|'UPDATE_FAILED'|'UPDATE_COMPLETE',
                'ResourceStatusReason': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_stack_set_operation_results(StackSetName=None, OperationId=None, NextToken=None, MaxResults=None):
    """
    Returns summary information about the results of a stack set operation.
    See also: AWS API Documentation
    
    
    :example: response = client.list_stack_set_operation_results(
        StackSetName='string',
        OperationId='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type StackSetName: string
    :param StackSetName: [REQUIRED]
            The name or unique ID of the stack set that you want to get operation results for.
            

    :type OperationId: string
    :param OperationId: [REQUIRED]
            The ID of the stack set operation.
            

    :type NextToken: string
    :param NextToken: If the previous request didn't return all of the remaining results, the response object's NextToken parameter value is set to a token. To retrieve the next set of results, call ListStackSetOperationResults again and assign that token to the request object's NextToken parameter. If there are no remaining results, the previous response object's NextToken parameter is set to null .

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a NextToken value that you can assign to the NextToken request parameter to get the next set of results.

    :rtype: dict
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
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    CANCELLED : The operation in the specified account and region has been cancelled. This is either because a user has stopped the stack set operation, or because the failure tolerance of the stack set operation has been exceeded.
    FAILED : The operation in the specified account and region failed.  If the stack set operation fails in enough accounts within a region, the failure tolerance for the stack set operation as a whole might be exceeded.
    RUNNING : The operation in the specified account and region is currently in progress.
    PENDING : The operation in the specified account and region has yet to start.
    SUCCEEDED : The operation in the specified account and region completed successfully.
    
    """
    pass

def list_stack_set_operations(StackSetName=None, NextToken=None, MaxResults=None):
    """
    Returns summary information about operations performed on a stack set.
    See also: AWS API Documentation
    
    
    :example: response = client.list_stack_set_operations(
        StackSetName='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type StackSetName: string
    :param StackSetName: [REQUIRED]
            The name or unique ID of the stack set that you want to get operation summaries for.
            

    :type NextToken: string
    :param NextToken: If the previous paginated request didn't return all of the remaining results, the response object's NextToken parameter value is set to a token. To retrieve the next set of results, call ListStackSetOperations again and assign that token to the request object's NextToken parameter. If there are no remaining results, the previous response object's NextToken parameter is set to null .

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a NextToken value that you can assign to the NextToken request parameter to get the next set of results.

    :rtype: dict
    :return: {
        'Summaries': [
            {
                'OperationId': 'string',
                'Action': 'CREATE'|'UPDATE'|'DELETE',
                'Status': 'RUNNING'|'SUCCEEDED'|'FAILED'|'STOPPING'|'STOPPED',
                'CreationTimestamp': datetime(2015, 1, 1),
                'EndTimestamp': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    FAILED : The operation exceeded the specified failure tolerance. The failure tolerance value that you've set for an operation is applied for each region during stack create and update operations. If the number of failed stacks within a region exceeds the failure tolerance, the status of the operation in the region is set to FAILED . This in turn sets the status of the operation as a whole to FAILED , and AWS CloudFormation cancels the operation in any remaining regions.
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
    :param NextToken: If the previous paginated request didn't return all of the remaining results, the response object's NextToken parameter value is set to a token. To retrieve the next set of results, call ListStackSets again and assign that token to the request object's NextToken parameter. If there are no remaining results, the previous response object's NextToken parameter is set to null .

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a NextToken value that you can assign to the NextToken request parameter to get the next set of results.

    :type Status: string
    :param Status: The status of the stack sets that you want to get summary information about.

    :rtype: dict
    :return: {
        'Summaries': [
            {
                'StackSetName': 'string',
                'StackSetId': 'string',
                'Description': 'string',
                'Status': 'ACTIVE'|'DELETED'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_stacks(NextToken=None, StackStatusFilter=None):
    """
    Returns the summary information for stacks whose status matches the specified StackStatusFilter. Summary information for stacks that have been deleted is kept for 90 days after the stack is deleted. If no StackStatusFilter is specified, summary information for all stacks is returned (including existing stacks and stacks that have been deleted).
    See also: AWS API Documentation
    
    
    :example: response = client.list_stacks(
        NextToken='string',
        StackStatusFilter=[
            'CREATE_IN_PROGRESS'|'CREATE_FAILED'|'CREATE_COMPLETE'|'ROLLBACK_IN_PROGRESS'|'ROLLBACK_FAILED'|'ROLLBACK_COMPLETE'|'DELETE_IN_PROGRESS'|'DELETE_FAILED'|'DELETE_COMPLETE'|'UPDATE_IN_PROGRESS'|'UPDATE_COMPLETE_CLEANUP_IN_PROGRESS'|'UPDATE_COMPLETE'|'UPDATE_ROLLBACK_IN_PROGRESS'|'UPDATE_ROLLBACK_FAILED'|'UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS'|'UPDATE_ROLLBACK_COMPLETE'|'REVIEW_IN_PROGRESS',
        ]
    )
    
    
    :type NextToken: string
    :param NextToken: A string that identifies the next page of stacks that you want to retrieve.

    :type StackStatusFilter: list
    :param StackStatusFilter: Stack status to use as a filter. Specify one or more stack status codes to list only stacks with the specified status codes. For a complete list of stack status codes, see the StackStatus parameter of the Stack data type.
            (string) --
            

    :rtype: dict
    :return: {
        'StackSummaries': [
            {
                'StackId': 'string',
                'StackName': 'string',
                'TemplateDescription': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'LastUpdatedTime': datetime(2015, 1, 1),
                'DeletionTime': datetime(2015, 1, 1),
                'StackStatus': 'CREATE_IN_PROGRESS'|'CREATE_FAILED'|'CREATE_COMPLETE'|'ROLLBACK_IN_PROGRESS'|'ROLLBACK_FAILED'|'ROLLBACK_COMPLETE'|'DELETE_IN_PROGRESS'|'DELETE_FAILED'|'DELETE_COMPLETE'|'UPDATE_IN_PROGRESS'|'UPDATE_COMPLETE_CLEANUP_IN_PROGRESS'|'UPDATE_COMPLETE'|'UPDATE_ROLLBACK_IN_PROGRESS'|'UPDATE_ROLLBACK_FAILED'|'UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS'|'UPDATE_ROLLBACK_COMPLETE'|'REVIEW_IN_PROGRESS',
                'StackStatusReason': 'string',
                'ParentId': 'string',
                'RootId': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
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
    :param StackName: [REQUIRED]
            The name or unique stack ID that you want to associate a policy with.
            

    :type StackPolicyBody: string
    :param StackPolicyBody: Structure containing the stack policy body. For more information, go to Prevent Updates to Stack Resources in the AWS CloudFormation User Guide. You can specify either the StackPolicyBody or the StackPolicyURL parameter, but not both.

    :type StackPolicyURL: string
    :param StackPolicyURL: Location of a file containing the stack policy. The URL must point to a policy (maximum size: 16 KB) located in an S3 bucket in the same region as the stack. You can specify either the StackPolicyBody or the StackPolicyURL parameter, but not both.

    """
    pass

def signal_resource(StackName=None, LogicalResourceId=None, UniqueId=None, Status=None):
    """
    Sends a signal to the specified resource with a success or failure status. You can use the SignalResource API in conjunction with a creation policy or update policy. AWS CloudFormation doesn't proceed with a stack creation or update until resources receive the required number of signals or the timeout period is exceeded. The SignalResource API is useful in cases where you want to send signals from anywhere other than an Amazon EC2 instance.
    See also: AWS API Documentation
    
    
    :example: response = client.signal_resource(
        StackName='string',
        LogicalResourceId='string',
        UniqueId='string',
        Status='SUCCESS'|'FAILURE'
    )
    
    
    :type StackName: string
    :param StackName: [REQUIRED]
            The stack name or unique stack ID that includes the resource that you want to signal.
            

    :type LogicalResourceId: string
    :param LogicalResourceId: [REQUIRED]
            The logical ID of the resource that you want to signal. The logical ID is the name of the resource that given in the template.
            

    :type UniqueId: string
    :param UniqueId: [REQUIRED]
            A unique ID of the signal. When you signal Amazon EC2 instances or Auto Scaling groups, specify the instance ID that you are signaling as the unique ID. If you send multiple signals to a single resource (such as signaling a wait condition), each signal requires a different unique ID.
            

    :type Status: string
    :param Status: [REQUIRED]
            The status of the signal, which is either success or failure. A failure signal causes AWS CloudFormation to immediately fail the stack creation or update.
            

    """
    pass

def stop_stack_set_operation(StackSetName=None, OperationId=None):
    """
    Stops an in-progress operation on a stack set and its associated stack instances.
    See also: AWS API Documentation
    
    
    :example: response = client.stop_stack_set_operation(
        StackSetName='string',
        OperationId='string'
    )
    
    
    :type StackSetName: string
    :param StackSetName: [REQUIRED]
            The name or unique ID of the stack set that you want to stop the operation for.
            

    :type OperationId: string
    :param OperationId: [REQUIRED]
            The ID of the stack operation.
            

    :rtype: dict
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
    
    Examples
    This example adds two stack notification topics to the specified stack.
    Expected Output:
    
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
            'CAPABILITY_IAM'|'CAPABILITY_NAMED_IAM',
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
    :param StackName: [REQUIRED]
            The name or unique stack ID of the stack to update.
            

    :type TemplateBody: string
    :param TemplateBody: Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes. (For more information, go to Template Anatomy in the AWS CloudFormation User Guide.)
            Conditional: You must specify only one of the following parameters: TemplateBody , TemplateURL , or set the UsePreviousTemplate to true .
            

    :type TemplateURL: string
    :param TemplateURL: Location of file containing the template body. The URL must point to a template that is located in an Amazon S3 bucket. For more information, go to Template Anatomy in the AWS CloudFormation User Guide.
            Conditional: You must specify only one of the following parameters: TemplateBody , TemplateURL , or set the UsePreviousTemplate to true .
            

    :type UsePreviousTemplate: boolean
    :param UsePreviousTemplate: Reuse the existing template that is associated with the stack that you are updating.
            Conditional: You must specify only one of the following parameters: TemplateBody , TemplateURL , or set the UsePreviousTemplate to true .
            

    :type StackPolicyDuringUpdateBody: string
    :param StackPolicyDuringUpdateBody: Structure containing the temporary overriding stack policy body. You can specify either the StackPolicyDuringUpdateBody or the StackPolicyDuringUpdateURL parameter, but not both.
            If you want to update protected resources, specify a temporary overriding stack policy during this update. If you do not specify a stack policy, the current policy that is associated with the stack will be used.
            

    :type StackPolicyDuringUpdateURL: string
    :param StackPolicyDuringUpdateURL: Location of a file containing the temporary overriding stack policy. The URL must point to a policy (max size: 16KB) located in an S3 bucket in the same region as the stack. You can specify either the StackPolicyDuringUpdateBody or the StackPolicyDuringUpdateURL parameter, but not both.
            If you want to update protected resources, specify a temporary overriding stack policy during this update. If you do not specify a stack policy, the current policy that is associated with the stack will be used.
            

    :type Parameters: list
    :param Parameters: A list of Parameter structures that specify input parameters for the stack. For more information, see the Parameter data type.
            (dict) --The Parameter data type.
            ParameterKey (string) --The key associated with the parameter. If you don't specify a key and value for a particular parameter, AWS CloudFormation uses the default value that is specified in your template.
            ParameterValue (string) --The input value associated with the parameter.
            UsePreviousValue (boolean) --During a stack update, use the existing parameter value that the stack is using for a given parameter key. If you specify true , do not specify a parameter value.
            ResolvedValue (string) --Read-only. The value that corresponds to a Systems Manager parameter key. This field is returned only for ` SSM parameter types <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html#aws-ssm-parameter-types>`__ in the template.
            
            

    :type Capabilities: list
    :param Capabilities: A list of values that you must specify before AWS CloudFormation can update certain stacks. Some stack templates might include resources that can affect permissions in your AWS account, for example, by creating new AWS Identity and Access Management (IAM) users. For those stacks, you must explicitly acknowledge their capabilities by specifying this parameter.
            The only valid values are CAPABILITY_IAM and CAPABILITY_NAMED_IAM . The following resources require you to specify this parameter: AWS::IAM::AccessKey , AWS::IAM::Group , AWS::IAM::InstanceProfile , AWS::IAM::Policy , AWS::IAM::Role , AWS::IAM::User , and AWS::IAM::UserToGroupAddition . If your stack template contains these resources, we recommend that you review all permissions associated with them and edit their permissions if necessary.
            If you have IAM resources, you can specify either capability. If you have IAM resources with custom names, you must specify CAPABILITY_NAMED_IAM . If you don't specify this parameter, this action returns an InsufficientCapabilities error.
            For more information, see Acknowledging IAM Resources in AWS CloudFormation Templates .
            (string) --
            

    :type ResourceTypes: list
    :param ResourceTypes: The template resource types that you have permissions to work with for this update stack action, such as AWS::EC2::Instance , AWS::EC2::* , or Custom::MyCustomInstance .
            If the list of resource types doesn't include a resource that you're updating, the stack update fails. By default, AWS CloudFormation grants permissions to all resource types. AWS Identity and Access Management (IAM) uses this parameter for AWS CloudFormation-specific condition keys in IAM policies. For more information, see Controlling Access with AWS Identity and Access Management .
            (string) --
            

    :type RoleARN: string
    :param RoleARN: The Amazon Resource Name (ARN) of an AWS Identity and Access Management (IAM) role that AWS CloudFormation assumes to update the stack. AWS CloudFormation uses the role's credentials to make calls on your behalf. AWS CloudFormation always uses this role for all future operations on the stack. As long as users have permission to operate on the stack, AWS CloudFormation uses this role even if the users don't have permission to pass it. Ensure that the role grants least privilege.
            If you don't specify a value, AWS CloudFormation uses the role that was previously associated with the stack. If no role is available, AWS CloudFormation uses a temporary session that is generated from your user credentials.
            

    :type RollbackConfiguration: dict
    :param RollbackConfiguration: The rollback triggers for AWS CloudFormation to monitor during stack creation and updating operations, and for the specified monitoring period afterwards.
            RollbackTriggers (list) --The triggers to monitor during stack creation or update actions.
            By default, AWS CloudFormation saves the rollback triggers specified for a stack and applies them to any subsequent update operations for the stack, unless you specify otherwise. If you do specify rollback triggers for this parameter, those triggers replace any list of triggers previously specified for the stack. This means:
            To use the rollback triggers previously specified for this stack, if any, don't specify this parameter.
            To specify new or updated rollback triggers, you must specify all the triggers that you want used for this stack, even triggers you've specifed before (for example, when creating the stack or during a previous stack update). Any triggers that you don't include in the updated list of triggers are no longer applied to the stack.
            To remove all currently specified triggers, specify an empty list for this parameter.
            If a specified trigger is missing, the entire stack operation fails and is rolled back.
            (dict) --A rollback trigger AWS CloudFormation monitors during creation and updating of stacks. If any of the alarms you specify goes to ALARM state during the stack operation or within the specified monitoring period afterwards, CloudFormation rolls back the entire stack operation.
            Arn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the rollback trigger.
            If a specified trigger is missing, the entire stack operation fails and is rolled back.
            Type (string) -- [REQUIRED]The resource type of the rollback trigger. Currently, AWS::CloudWatch::Alarm is the only supported resource type.
            
            MonitoringTimeInMinutes (integer) --The amount of time, in minutes, during which CloudFormation should monitor all the rollback triggers after the stack creation or update operation deploys all necessary resources.
            The default is 0 minutes.
            If you specify a monitoring period but do not specify any rollback triggers, CloudFormation still waits the specified period of time before cleaning up old resources after update operations. You can use this monitoring period to perform any manual stack validation desired, and manually cancel the stack creation or update (using CancelUpdateStack , for example) as necessary.
            If you specify 0 for this parameter, CloudFormation still monitors the specified rollback triggers during stack creation and update operations. Then, for update operations, it begins disposing of old resources immediately once the operation completes.
            

    :type StackPolicyBody: string
    :param StackPolicyBody: Structure containing a new stack policy body. You can specify either the StackPolicyBody or the StackPolicyURL parameter, but not both.
            You might update the stack policy, for example, in order to protect a new resource that you created during a stack update. If you do not specify a stack policy, the current policy that is associated with the stack is unchanged.
            

    :type StackPolicyURL: string
    :param StackPolicyURL: Location of a file containing the updated stack policy. The URL must point to a policy (max size: 16KB) located in an S3 bucket in the same region as the stack. You can specify either the StackPolicyBody or the StackPolicyURL parameter, but not both.
            You might update the stack policy, for example, in order to protect a new resource that you created during a stack update. If you do not specify a stack policy, the current policy that is associated with the stack is unchanged.
            

    :type NotificationARNs: list
    :param NotificationARNs: Amazon Simple Notification Service topic Amazon Resource Names (ARNs) that AWS CloudFormation associates with the stack. Specify an empty list to remove all notification topics.
            (string) --
            

    :type Tags: list
    :param Tags: Key-value pairs to associate with this stack. AWS CloudFormation also propagates these tags to supported resources in the stack. You can specify a maximum number of 50 tags.
            If you don't specify this parameter, AWS CloudFormation doesn't modify the stack's tags. If you specify an empty value, AWS CloudFormation removes all associated tags.
            (dict) --The Tag type enables you to specify a key-value pair that can be used to store information about an AWS CloudFormation stack.
            Key (string) -- [REQUIRED]
            Required . A string used to identify this tag. You can specify a maximum of 128 characters for a tag key. Tags owned by Amazon Web Services (AWS) have the reserved prefix: aws: .
            Value (string) -- [REQUIRED]
            Required . A string containing the value for this tag. You can specify a maximum of 256 characters for a tag value.
            
            

    :type ClientRequestToken: string
    :param ClientRequestToken: A unique identifier for this UpdateStack request. Specify this token if you plan to retry requests so that AWS CloudFormation knows that you're not attempting to update a stack with the same name. You might retry UpdateStack requests to ensure that AWS CloudFormation successfully received them.
            All events triggered by a given stack operation are assigned the same client request token, which you can use to track operations. For example, if you execute a CreateStack operation with the token token1 , then all the StackEvents generated by that operation will have ClientRequestToken set as token1 .
            In the console, stack operations display the client request token on the Events tab. Stack operations that are initiated from the console use the token format Console-StackOperation-ID , which helps you easily identify the stack operation . For example, if you create a stack using the console, each stack event would be assigned the same token in the following format: Console-CreateStack-7f59c3cf-00d2-40c7-b2ff-e75db0987002 .
            

    :rtype: dict
    :return: {
        'StackId': 'string'
    }
    
    
    """
    pass

def update_stack_instances(StackSetName=None, Accounts=None, Regions=None, ParameterOverrides=None, OperationPreferences=None, OperationId=None):
    """
    Updates the parameter values for stack instances for the specified accounts, within the specified regions. A stack instance refers to a stack in a specific account and region.
    You can only update stack instances in regions and accounts where they already exist; to create additional stack instances, use CreateStackInstances .
    During stack set updates, any parameters overridden for a stack instance are not updated, but retain their overridden value.
    You can only update the parameter values that are specified in the stack set; to add or delete a parameter itself, use UpdateStackSet to update the stack set template. If you add a parameter to a template, before you can override the parameter value specified in the stack set you must first use UpdateStackSet to update all stack instances with the updated template and parameter value specified in the stack set. Once a stack instance has been updated with the new parameter, you can then override the parameter value using UpdateStackInstances .
    See also: AWS API Documentation
    
    
    :example: response = client.update_stack_instances(
        StackSetName='string',
        Accounts=[
            'string',
        ],
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
    :param StackSetName: [REQUIRED]
            The name or unique ID of the stack set associated with the stack instances.
            

    :type Accounts: list
    :param Accounts: [REQUIRED]
            The names of one or more AWS accounts for which you want to update parameter values for stack instances. The overridden parameter values will be applied to all stack instances in the specified accounts and regions.
            (string) --
            

    :type Regions: list
    :param Regions: [REQUIRED]
            The names of one or more regions in which you want to update parameter values for stack instances. The overridden parameter values will be applied to all stack instances in the specified accounts and regions.
            (string) --
            

    :type ParameterOverrides: list
    :param ParameterOverrides: A list of input parameters whose values you want to update for the specified stack instances.
            Any overridden parameter values will be applied to all stack instances in the specified accounts and regions. When specifying parameters and their values, be aware of how AWS CloudFormation sets parameter values during stack instance update operations:
            To override the current value for a parameter, include the parameter and specify its value.
            To leave a parameter set to its present value, you can do one of the following:
            Do not include the parameter in the list.
            Include the parameter and specify UsePreviousValue as true . (You cannot specify both a value and set UsePreviousValue to true .)
            To set all overridden parameter back to the values specified in the stack set, specify a parameter list but do not include any parameters.
            To leave all parameters set to their present values, do not specify this property at all.
            During stack set updates, any parameter values overridden for a stack instance are not updated, but retain their overridden value.
            You can only override the parameter values that are specified in the stack set; to add or delete a parameter itself, use UpdateStackSet to update the stack set template. If you add a parameter to a template, before you can override the parameter value specified in the stack set you must first use UpdateStackSet to update all stack instances with the updated template and parameter value specified in the stack set. Once a stack instance has been updated with the new parameter, you can then override the parameter value using UpdateStackInstances .
            (dict) --The Parameter data type.
            ParameterKey (string) --The key associated with the parameter. If you don't specify a key and value for a particular parameter, AWS CloudFormation uses the default value that is specified in your template.
            ParameterValue (string) --The input value associated with the parameter.
            UsePreviousValue (boolean) --During a stack update, use the existing parameter value that the stack is using for a given parameter key. If you specify true , do not specify a parameter value.
            ResolvedValue (string) --Read-only. The value that corresponds to a Systems Manager parameter key. This field is returned only for ` SSM parameter types <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html#aws-ssm-parameter-types>`__ in the template.
            
            

    :type OperationPreferences: dict
    :param OperationPreferences: Preferences for how AWS CloudFormation performs this stack set operation.
            RegionOrder (list) --The order of the regions in where you want to perform the stack operation.
            (string) --
            FailureToleranceCount (integer) --The number of accounts, per region, for which this operation can fail before AWS CloudFormation stops the operation in that region. If the operation is stopped in a region, AWS CloudFormation doesn't attempt the operation in any subsequent regions.
            Conditional: You must specify either FailureToleranceCount or FailureTolerancePercentage (but not both).
            FailureTolerancePercentage (integer) --The percentage of accounts, per region, for which this stack operation can fail before AWS CloudFormation stops the operation in that region. If the operation is stopped in a region, AWS CloudFormation doesn't attempt the operation in any subsequent regions.
            When calculating the number of accounts based on the specified percentage, AWS CloudFormation rounds down to the next whole number.
            Conditional: You must specify either FailureToleranceCount or FailureTolerancePercentage , but not both.
            MaxConcurrentCount (integer) --The maximum number of accounts in which to perform this operation at one time. This is dependent on the value of FailureToleranceCount  MaxConcurrentCount is at most one more than the FailureToleranceCount .
            Note that this setting lets you specify the maximum for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling.
            Conditional: You must specify either MaxConcurrentCount or MaxConcurrentPercentage , but not both.
            MaxConcurrentPercentage (integer) --The maximum percentage of accounts in which to perform this operation at one time.
            When calculating the number of accounts based on the specified percentage, AWS CloudFormation rounds down to the next whole number. This is true except in cases where rounding down would result is zero. In this case, CloudFormation sets the number as one instead.
            Note that this setting lets you specify the maximum for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling.
            Conditional: You must specify either MaxConcurrentCount or MaxConcurrentPercentage , but not both.
            

    :type OperationId: string
    :param OperationId: The unique identifier for this stack set operation.
            The operation ID also functions as an idempotency token, to ensure that AWS CloudFormation performs the stack set operation only once, even if you retry the request multiple times. You might retry stack set operation requests to ensure that AWS CloudFormation successfully received them.
            If you don't specify an operation ID, the SDK generates one automatically.
            This field is autopopulated if not provided.
            

    :rtype: dict
    :return: {
        'OperationId': 'string'
    }
    
    
    """
    pass

def update_stack_set(StackSetName=None, Description=None, TemplateBody=None, TemplateURL=None, UsePreviousTemplate=None, Parameters=None, Capabilities=None, Tags=None, OperationPreferences=None, AdministrationRoleARN=None, OperationId=None):
    """
    Updates the stack set and all associated stack instances.
    Even if the stack set operation created by updating the stack set fails (completely or partially, below or above a specified failure tolerance), the stack set is updated with your changes. Subsequent  CreateStackInstances calls on the specified stack set use the updated stack set.
    See also: AWS API Documentation
    
    
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
            'CAPABILITY_IAM'|'CAPABILITY_NAMED_IAM',
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
        OperationId='string'
    )
    
    
    :type StackSetName: string
    :param StackSetName: [REQUIRED]
            The name or unique ID of the stack set that you want to update.
            

    :type Description: string
    :param Description: A brief description of updates that you are making.

    :type TemplateBody: string
    :param TemplateBody: The structure that contains the template body, with a minimum length of 1 byte and a maximum length of 51,200 bytes. For more information, see Template Anatomy in the AWS CloudFormation User Guide.
            Conditional: You must specify only one of the following parameters: TemplateBody or TemplateURL  or set UsePreviousTemplate to true.
            

    :type TemplateURL: string
    :param TemplateURL: The location of the file that contains the template body. The URL must point to a template (maximum size: 460,800 bytes) that is located in an Amazon S3 bucket. For more information, see Template Anatomy in the AWS CloudFormation User Guide.
            Conditional: You must specify only one of the following parameters: TemplateBody or TemplateURL  or set UsePreviousTemplate to true.
            

    :type UsePreviousTemplate: boolean
    :param UsePreviousTemplate: Use the existing template that's associated with the stack set that you're updating.
            Conditional: You must specify only one of the following parameters: TemplateBody or TemplateURL  or set UsePreviousTemplate to true.
            

    :type Parameters: list
    :param Parameters: A list of input parameters for the stack set template.
            (dict) --The Parameter data type.
            ParameterKey (string) --The key associated with the parameter. If you don't specify a key and value for a particular parameter, AWS CloudFormation uses the default value that is specified in your template.
            ParameterValue (string) --The input value associated with the parameter.
            UsePreviousValue (boolean) --During a stack update, use the existing parameter value that the stack is using for a given parameter key. If you specify true , do not specify a parameter value.
            ResolvedValue (string) --Read-only. The value that corresponds to a Systems Manager parameter key. This field is returned only for ` SSM parameter types <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html#aws-ssm-parameter-types>`__ in the template.
            
            

    :type Capabilities: list
    :param Capabilities: A list of values that you must specify before AWS CloudFormation can create certain stack sets. Some stack set templates might include resources that can affect permissions in your AWS account for example, by creating new AWS Identity and Access Management (IAM) users. For those stack sets, you must explicitly acknowledge their capabilities by specifying this parameter.
            The only valid values are CAPABILITY_IAM and CAPABILITY_NAMED_IAM. The following resources require you to specify this parameter:
            AWS::IAM::AccessKey
            AWS::IAM::Group
            AWS::IAM::InstanceProfile
            AWS::IAM::Policy
            AWS::IAM::Role
            AWS::IAM::User
            AWS::IAM::UserToGroupAddition
            If your stack template contains these resources, we recommend that you review all permissions that are associated with them and edit their permissions if necessary.
            If you have IAM resources, you can specify either capability. If you have IAM resources with custom names, you must specify CAPABILITY_NAMED_IAM. If you don't specify this parameter, this action returns an InsufficientCapabilities error.
            For more information, see Acknowledging IAM Resources in AWS CloudFormation Templates.
            (string) --
            

    :type Tags: list
    :param Tags: The key-value pairs to associate with this stack set and the stacks created from it. AWS CloudFormation also propagates these tags to supported resources that are created in the stacks. You can specify a maximum number of 50 tags.
            If you specify tags for this parameter, those tags replace any list of tags that are currently associated with this stack set. This means:
            If you don't specify this parameter, AWS CloudFormation doesn't modify the stack's tags.
            If you specify any tags using this parameter, you must specify all the tags that you want associated with this stack set, even tags you've specifed before (for example, when creating the stack set or during a previous update of the stack set.). Any tags that you don't include in the updated list of tags are removed from the stack set, and therefore from the stacks and resources as well.
            If you specify an empty value, AWS CloudFormation removes all currently associated tags.
            If you specify new tags as part of an UpdateStackSet action, AWS CloudFormation checks to see if you have the required IAM permission to tag resources. If you omit tags that are currently associated with the stack set from the list of tags you specify, AWS CloudFormation assumes that you want to remove those tags from the stack set, and checks to see if you have permission to untag resources. If you don't have the necessary permission(s), the entire UpdateStackSet action fails with an access denied error, and the stack set is not updated.
            (dict) --The Tag type enables you to specify a key-value pair that can be used to store information about an AWS CloudFormation stack.
            Key (string) -- [REQUIRED]
            Required . A string used to identify this tag. You can specify a maximum of 128 characters for a tag key. Tags owned by Amazon Web Services (AWS) have the reserved prefix: aws: .
            Value (string) -- [REQUIRED]
            Required . A string containing the value for this tag. You can specify a maximum of 256 characters for a tag value.
            
            

    :type OperationPreferences: dict
    :param OperationPreferences: Preferences for how AWS CloudFormation performs this stack set operation.
            RegionOrder (list) --The order of the regions in where you want to perform the stack operation.
            (string) --
            FailureToleranceCount (integer) --The number of accounts, per region, for which this operation can fail before AWS CloudFormation stops the operation in that region. If the operation is stopped in a region, AWS CloudFormation doesn't attempt the operation in any subsequent regions.
            Conditional: You must specify either FailureToleranceCount or FailureTolerancePercentage (but not both).
            FailureTolerancePercentage (integer) --The percentage of accounts, per region, for which this stack operation can fail before AWS CloudFormation stops the operation in that region. If the operation is stopped in a region, AWS CloudFormation doesn't attempt the operation in any subsequent regions.
            When calculating the number of accounts based on the specified percentage, AWS CloudFormation rounds down to the next whole number.
            Conditional: You must specify either FailureToleranceCount or FailureTolerancePercentage , but not both.
            MaxConcurrentCount (integer) --The maximum number of accounts in which to perform this operation at one time. This is dependent on the value of FailureToleranceCount  MaxConcurrentCount is at most one more than the FailureToleranceCount .
            Note that this setting lets you specify the maximum for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling.
            Conditional: You must specify either MaxConcurrentCount or MaxConcurrentPercentage , but not both.
            MaxConcurrentPercentage (integer) --The maximum percentage of accounts in which to perform this operation at one time.
            When calculating the number of accounts based on the specified percentage, AWS CloudFormation rounds down to the next whole number. This is true except in cases where rounding down would result is zero. In this case, CloudFormation sets the number as one instead.
            Note that this setting lets you specify the maximum for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling.
            Conditional: You must specify either MaxConcurrentCount or MaxConcurrentPercentage , but not both.
            

    :type AdministrationRoleARN: string
    :param AdministrationRoleARN: The Amazon Resource Number (ARN) of the IAM role to use to update this stack set.
            Specify an IAM role only if you are using customized administrator roles to control which users or groups can manage specific stack sets within the same administrator account. For more information, see Define Permissions for Multiple Administrators in the AWS CloudFormation User Guide .
            If you specify a customized administrator role, AWS CloudFormation uses that role to update the stack. If you do not specify a customized administrator role, AWS CloudFormation performs the update using the role previously associated with the stack set, so long as you have permissions to perform operations on the stack set.
            

    :type OperationId: string
    :param OperationId: The unique ID for this stack set operation.
            The operation ID also functions as an idempotency token, to ensure that AWS CloudFormation performs the stack set operation only once, even if you retry the request multiple times. You might retry stack set operation requests to ensure that AWS CloudFormation successfully received them.
            If you don't specify an operation ID, AWS CloudFormation generates one automatically.
            Repeating this stack set operation with a new operation ID retries all stack instances whose status is OUTDATED .
            This field is autopopulated if not provided.
            

    :rtype: dict
    :return: {
        'OperationId': 'string'
    }
    
    
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
    :param EnableTerminationProtection: [REQUIRED]
            Whether to enable termination protection on the specified stack.
            

    :type StackName: string
    :param StackName: [REQUIRED]
            The name or unique ID of the stack for which you want to set termination protection.
            

    :rtype: dict
    :return: {
        'StackId': 'string'
    }
    
    
    """
    pass

def validate_template(TemplateBody=None, TemplateURL=None):
    """
    Validates a specified template. AWS CloudFormation first checks if the template is valid JSON. If it isn't, AWS CloudFormation checks if the template is valid YAML. If both these checks fail, AWS CloudFormation returns a template validation error.
    See also: AWS API Documentation
    
    Examples
    This example validates the specified template.
    Expected Output:
    
    :example: response = client.validate_template(
        TemplateBody='string',
        TemplateURL='string'
    )
    
    
    :type TemplateBody: string
    :param TemplateBody: Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes. For more information, go to Template Anatomy in the AWS CloudFormation User Guide.
            Conditional: You must pass TemplateURL or TemplateBody . If both are passed, only TemplateBody is used.
            

    :type TemplateURL: string
    :param TemplateURL: Location of file containing the template body. The URL must point to a template (max size: 460,800 bytes) that is located in an Amazon S3 bucket. For more information, go to Template Anatomy in the AWS CloudFormation User Guide.
            Conditional: You must pass TemplateURL or TemplateBody . If both are passed, only TemplateBody is used.
            

    :rtype: dict
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
            'CAPABILITY_IAM'|'CAPABILITY_NAMED_IAM',
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

