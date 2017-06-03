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
    :param ResourcesToSkip: A list of the logical IDs of the resources that AWS CloudFormation skips during the continue update rollback operation. You can specify only resources that are in the UPDATE_FAILED state because a rollback failed. You can't specify resources that are in the UPDATE_FAILED state for other reasons, for example, because an update was canceled. To check why a resource update failed, use the DescribeStackResources action, and view the resource status reason.
            Warning
            Specify this property to skip rolling back resources that AWS CloudFormation can't successfully roll back. We recommend that you troubleshoot resources before skipping them. AWS CloudFormation sets the status of the specified resources to UPDATE_COMPLETE and continues to roll back the stack. After the rollback is complete, the state of the skipped resources will be inconsistent with the state of the resources in the stack template. Before performing another stack update, you must update the stack or resources to be consistent with each other. If you don't, subsequent stack updates might fail, and the stack will become unrecoverable.
            Specify the minimum number of resources required to successfully roll back your stack. For example, a failed resource update might cause dependent resources to fail. In this case, it might not be necessary to skip the dependent resources.
            To specify resources in a nested stack, use the following format: NestedStackName.ResourceLogicalID . If the ResourceLogicalID is a stack resource (Type: AWS::CloudFormation::Stack ), it must be in one of the following states: DELETE_IN_PROGRESS , DELETE_COMPLETE , or DELETE_FAILED .
            (string) --
            

    :type ClientRequestToken: string
    :param ClientRequestToken: A unique identifier for this ContinueUpdateRollback request. Specify this token if you plan to retry requests so that AWS CloudFormation knows that you're not attempting to continue the rollback to a stack with the same name. You might retry ContinueUpdateRollback requests to ensure that AWS CloudFormation successfully received them.

    :rtype: dict
    :return: {}
    
    
    """
    pass

def create_change_set(StackName=None, TemplateBody=None, TemplateURL=None, UsePreviousTemplate=None, Parameters=None, Capabilities=None, ResourceTypes=None, RoleARN=None, NotificationARNs=None, Tags=None, ChangeSetName=None, ClientToken=None, Description=None, ChangeSetType=None):
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
                'UsePreviousValue': True|False
            },
        ],
        Capabilities=[
            'CAPABILITY_IAM'|'CAPABILITY_NAMED_IAM',
        ],
        ResourceTypes=[
            'string',
        ],
        RoleARN='string',
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
            ParameterValue (string) --The value associated with the parameter.
            UsePreviousValue (boolean) --During a stack update, use the existing parameter value that the stack is using for a given parameter key. If you specify true , do not specify a parameter value.
            
            

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
            

    :type NotificationARNs: list
    :param NotificationARNs: The Amazon Resource Names (ARNs) of Amazon Simple Notification Service (Amazon SNS) topics that AWS CloudFormation associates with the stack. To remove all associated notification topics, specify an empty list.
            (string) --
            

    :type Tags: list
    :param Tags: Key-value pairs to associate with this stack. AWS CloudFormation also propagates these tags to resources in the stack. You can specify a maximum of 10 tags.
            (dict) --The Tag type enables you to specify a key-value pair that can be used to store information about an AWS CloudFormation stack.
            Key (string) --
            Required . A string used to identify this tag. You can specify a maximum of 128 characters for a tag key. Tags owned by Amazon Web Services (AWS) have the reserved prefix: aws: .
            Value (string) --
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
            If you create a change set for a new stack, AWS Cloudformation creates a stack with a unique stack ID, but no template or resources. The stack will be in the ` REVIEW_IN_PROGRESS http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-describing-stacks.html#d0e11995`_ state until you execute the change set.
            By default, AWS CloudFormation specifies UPDATE . You can't use the UPDATE type to create a change set for a new stack or the CREATE type to create a change set for an existing stack.
            

    :rtype: dict
    :return: {
        'Id': 'string',
        'StackId': 'string'
    }
    
    
    """
    pass

def create_stack(StackName=None, TemplateBody=None, TemplateURL=None, Parameters=None, DisableRollback=None, TimeoutInMinutes=None, NotificationARNs=None, Capabilities=None, ResourceTypes=None, RoleARN=None, OnFailure=None, StackPolicyBody=None, StackPolicyURL=None, Tags=None, ClientRequestToken=None):
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
                'UsePreviousValue': True|False
            },
        ],
        DisableRollback=True|False,
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
        ClientRequestToken='string'
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
            ParameterValue (string) --The value associated with the parameter.
            UsePreviousValue (boolean) --During a stack update, use the existing parameter value that the stack is using for a given parameter key. If you specify true , do not specify a parameter value.
            
            

    :type DisableRollback: boolean
    :param DisableRollback: Set to true to disable rollback of the stack if stack creation failed. You can specify either DisableRollback or OnFailure , but not both.
            Default: false
            

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
    :param Tags: Key-value pairs to associate with this stack. AWS CloudFormation also propagates these tags to the resources created in the stack. A maximum number of 10 tags can be specified.
            (dict) --The Tag type enables you to specify a key-value pair that can be used to store information about an AWS CloudFormation stack.
            Key (string) --
            Required . A string used to identify this tag. You can specify a maximum of 128 characters for a tag key. Tags owned by Amazon Web Services (AWS) have the reserved prefix: aws: .
            Value (string) --
            Required . A string containing the value for this tag. You can specify a maximum of 256 characters for a tag value.
            
            

    :type ClientRequestToken: string
    :param ClientRequestToken: A unique identifier for this CreateStack request. Specify this token if you plan to retry requests so that AWS CloudFormation knows that you're not attempting to create a stack with the same name. You might retry CreateStack requests to ensure that AWS CloudFormation successfully received them.

    :rtype: dict
    :return: {
        'StackId': 'string'
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
                'UsePreviousValue': True|False
            },
        ],
        'CreationTime': datetime(2015, 1, 1),
        'ExecutionStatus': 'UNAVAILABLE'|'AVAILABLE'|'EXECUTE_IN_PROGRESS'|'EXECUTE_COMPLETE'|'EXECUTE_FAILED'|'OBSOLETE',
        'Status': 'CREATE_PENDING'|'CREATE_IN_PROGRESS'|'CREATE_COMPLETE'|'DELETE_COMPLETE'|'FAILED',
        'StatusReason': 'string',
        'NotificationARNs': [
            'string',
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
                        'UsePreviousValue': True|False
                    },
                ],
                'CreationTime': datetime(2015, 1, 1),
                'LastUpdatedTime': datetime(2015, 1, 1),
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
                        'Description': 'string'
                    },
                ],
                'RoleARN': 'string',
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
    true : disable rollback
    false : enable rollback
    
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
                'UsePreviousValue': True|False
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
            ParameterValue (string) --The value associated with the parameter.
            UsePreviousValue (boolean) --During a stack update, use the existing parameter value that the stack is using for a given parameter key. If you specify true , do not specify a parameter value.
            
            

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

def get_template_summary(TemplateBody=None, TemplateURL=None, StackName=None):
    """
    Returns information about a new or existing template. The GetTemplateSummary action is useful for viewing parameter information, such as default parameter values and parameter types, before you create or update a stack.
    You can use the GetTemplateSummary action when you submit a template, or you can get template information for a running or deleted stack.
    For deleted stacks, GetTemplateSummary returns the template information for up to 90 days after the stack has been deleted. If the template does not exist, a ValidationError is returned.
    See also: AWS API Documentation
    
    
    :example: response = client.get_template_summary(
        TemplateBody='string',
        TemplateURL='string',
        StackName='string'
    )
    
    
    :type TemplateBody: string
    :param TemplateBody: Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes. For more information about templates, see Template Anatomy in the AWS CloudFormation User Guide.
            Conditional: You must specify only one of the following parameters: StackName , TemplateBody , or TemplateURL .
            

    :type TemplateURL: string
    :param TemplateURL: Location of file containing the template body. The URL must point to a template (max size: 460,800 bytes) that is located in an Amazon S3 bucket. For more information about templates, see Template Anatomy in the AWS CloudFormation User Guide.
            Conditional: You must specify only one of the following parameters: StackName , TemplateBody , or TemplateURL .
            

    :type StackName: string
    :param StackName: The name or the stack ID that is associated with the stack, which are not always interchangeable. For running stacks, you can specify either the stack's name or its unique stack ID. For deleted stack, you must specify the unique stack ID.
            Conditional: You must specify only one of the following parameters: StackName , TemplateBody , or TemplateURL .
            

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
    Lists all exported output values in the account and region in which you call this action. Use this action to see the exported output values that you can import into other stacks. To import values, use the ` Fn::ImportValue http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-importvalue.html`_ function.
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
    For more information about importing an exported output value, see the ` Fn::ImportValue http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-importvalue.html`_ function.
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
                'StackStatusReason': 'string'
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

def update_stack(StackName=None, TemplateBody=None, TemplateURL=None, UsePreviousTemplate=None, StackPolicyDuringUpdateBody=None, StackPolicyDuringUpdateURL=None, Parameters=None, Capabilities=None, ResourceTypes=None, RoleARN=None, StackPolicyBody=None, StackPolicyURL=None, NotificationARNs=None, Tags=None, ClientRequestToken=None):
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
                'UsePreviousValue': True|False
            },
        ],
        Capabilities=[
            'CAPABILITY_IAM'|'CAPABILITY_NAMED_IAM',
        ],
        ResourceTypes=[
            'string',
        ],
        RoleARN='string',
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
            ParameterValue (string) --The value associated with the parameter.
            UsePreviousValue (boolean) --During a stack update, use the existing parameter value that the stack is using for a given parameter key. If you specify true , do not specify a parameter value.
            
            

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
    :param Tags: Key-value pairs to associate with this stack. AWS CloudFormation also propagates these tags to supported resources in the stack. You can specify a maximum number of 10 tags.
            If you don't specify this parameter, AWS CloudFormation doesn't modify the stack's tags. If you specify an empty value, AWS CloudFormation removes all associated tags.
            (dict) --The Tag type enables you to specify a key-value pair that can be used to store information about an AWS CloudFormation stack.
            Key (string) --
            Required . A string used to identify this tag. You can specify a maximum of 128 characters for a tag key. Tags owned by Amazon Web Services (AWS) have the reserved prefix: aws: .
            Value (string) --
            Required . A string containing the value for this tag. You can specify a maximum of 256 characters for a tag value.
            
            

    :type ClientRequestToken: string
    :param ClientRequestToken: A unique identifier for this UpdateStack request. Specify this token if you plan to retry requests so that AWS CloudFormation knows that you're not attempting to update a stack with the same name. You might retry UpdateStack requests to ensure that AWS CloudFormation successfully received them.

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

