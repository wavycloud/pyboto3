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


def cancel_update_stack(StackName=None):
    """
    :param StackName: [REQUIRED]
            The name or the unique stack ID that is associated with the stack.
            ReturnsNone
            
    :type StackName: string
    """
    pass


def continue_update_rollback(StackName=None, RoleARN=None):
    """
    :param StackName: [REQUIRED]
            The name or the unique ID of the stack that you want to continue rolling back.
            
    :type StackName: string
    :param RoleARN: The Amazon Resource Name (ARN) of an AWS Identity and Access Management (IAM) role that AWS CloudFormation assumes to roll back the stack. AWS CloudFormation uses the role's credentials to make calls on your behalf. AWS CloudFormation always uses this role for all future operations on the stack. As long as users have permission to operate on the stack, AWS CloudFormation uses this role even if the users don't have permission to pass it. Ensure that the role grants least privilege.
            If you don't specify a value, AWS CloudFormation uses the role that was previously associated with the stack. If no role is available, AWS CloudFormation uses a temporary session that is generated from your user credentials.
            
    :type RoleARN: string
    """
    pass


def create_change_set(StackName=None, TemplateBody=None, TemplateURL=None, UsePreviousTemplate=None, Parameters=None,
                      Capabilities=None, ResourceTypes=None, RoleARN=None, NotificationARNs=None, Tags=None,
                      ChangeSetName=None, ClientToken=None, Description=None):
    """
    :param StackName: [REQUIRED]
            The name or the unique ID of the stack for which you are creating a change set. AWS CloudFormation generates the change set by comparing this stack's information with the information that you submit, such as a modified template or different parameter input values.
            
    :type StackName: string
    :param TemplateBody: A structure that contains the body of the revised template, with a minimum length of 1 byte and a maximum length of 51,200 bytes. AWS CloudFormation generates the change set by comparing this template with the template of the stack that you specified.
            Conditional: You must specify only TemplateBody or TemplateURL .
            
    :type TemplateBody: string
    :param TemplateURL: The location of the file that contains the revised template. The URL must point to a template (max size: 460,800 bytes) that is located in an S3 bucket. AWS CloudFormation generates the change set by comparing this template with the stack that you specified.
            Conditional: You must specify only TemplateBody or TemplateURL .
            
    :type TemplateURL: string
    :param UsePreviousTemplate: Whether to reuse the template that is associated with the stack to create the change set.
    :type UsePreviousTemplate: boolean
    :param Parameters: A list of Parameter structures that specify input parameters for the change set. For more information, see the Parameter data type.
            (dict) --The Parameter data type.
            ParameterKey (string) --The key associated with the parameter. If you don't specify a key and value for a particular parameter, AWS CloudFormation uses the default value that is specified in your template.
            ParameterValue (string) --The value associated with the parameter.
            UsePreviousValue (boolean) --During a stack update, use the existing parameter value that the stack is using for a given parameter key. If you specify true , do not specify a parameter value.
            
            
    :type Parameters: list
    :param Capabilities: A list of values that you must specify before AWS CloudFormation can update certain stacks. Some stack templates might include resources that can affect permissions in your AWS account, for example, by creating new AWS Identity and Access Management (IAM) users. For those stacks, you must explicitly acknowledge their capabilities by specifying this parameter.
            The only valid values are CAPABILITY_IAM and CAPABILITY_NAMED_IAM . The following resources require you to specify this parameter: AWS::IAM::AccessKey , AWS::IAM::Group , AWS::IAM::InstanceProfile , AWS::IAM::Policy , AWS::IAM::Role , AWS::IAM::User , and AWS::IAM::UserToGroupAddition . If your stack template contains these resources, we recommend that you review all permissions associated with them and edit their permissions if necessary.
            If you have IAM resources, you can specify either capability. If you have IAM resources with custom names, you must specify CAPABILITY_NAMED_IAM . If you don't specify this parameter, this action returns an InsufficientCapabilities error.
            For more information, see Acknowledging IAM Resources in AWS CloudFormation Templates .
            (string) --
            
    :type Capabilities: list
    :param ResourceTypes: The template resource types that you have permissions to work with if you execute this change set, such as AWS::EC2::Instance , AWS::EC2::* , or Custom::MyCustomInstance .
            If the list of resource types doesn't include a resource type that you're updating, the stack update fails. By default, AWS CloudFormation grants permissions to all resource types. AWS Identity and Access Management (IAM) uses this parameter for condition keys in IAM policies for AWS CloudFormation. For more information, see Controlling Access with AWS Identity and Access Management in the AWS CloudFormation User Guide.
            (string) --
            
    :type ResourceTypes: list
    :param RoleARN: The Amazon Resource Name (ARN) of an AWS Identity and Access Management (IAM) role that AWS CloudFormation assumes when executing the change set. AWS CloudFormation uses the role's credentials to make calls on your behalf. AWS CloudFormation always uses this role for all future operations on the stack. As long as users have permission to operate on the stack, AWS CloudFormation uses this role even if the users don't have permission to pass it. Ensure that the role grants least privilege.
            If you don't specify a value, AWS CloudFormation uses the role that was previously associated with the stack. If no role is available, AWS CloudFormation uses a temporary session that is generated from your user credentials.
            
    :type RoleARN: string
    :param NotificationARNs: The Amazon Resource Names (ARNs) of Amazon Simple Notification Service (Amazon SNS) topics that AWS CloudFormation associates with the stack. To remove all associated notification topics, specify an empty list.
            (string) --
            
    :type NotificationARNs: list
    :param Tags: Key-value pairs to associate with this stack. AWS CloudFormation also propagates these tags to resources in the stack. You can specify a maximum of 10 tags.
            (dict) --The Tag type enables you to specify a key-value pair that can be used to store information about an AWS CloudFormation stack.
            Key (string) --
            Required . A string used to identify this tag. You can specify a maximum of 128 characters for a tag key. Tags owned by Amazon Web Services (AWS) have the reserved prefix: aws: .
            Value (string) --
            Required . A string containing the value for this tag. You can specify a maximum of 256 characters for a tag value.
            
            
    :type Tags: list
    :param ChangeSetName: [REQUIRED]
            The name of the change set. The name must be unique among all change sets that are associated with the specified stack.
            A change set name can contain only alphanumeric, case sensitive characters and hyphens. It must start with an alphabetic character and cannot exceed 128 characters.
            
    :type ChangeSetName: string
    :param ClientToken: A unique identifier for this CreateChangeSet request. Specify this token if you plan to retry requests so that AWS CloudFormation knows that you're not attempting to create another change set with the same name. You might retry CreateChangeSet requests to ensure that AWS CloudFormation successfully received them.
    :type ClientToken: string
    :param Description: A description to help you identify this change set.
    :type Description: string
    """
    pass


def create_stack(StackName=None, TemplateBody=None, TemplateURL=None, Parameters=None, DisableRollback=None,
                 TimeoutInMinutes=None, NotificationARNs=None, Capabilities=None, ResourceTypes=None, RoleARN=None,
                 OnFailure=None, StackPolicyBody=None, StackPolicyURL=None, Tags=None):
    """
    :param StackName: [REQUIRED]
            The name that is associated with the stack. The name must be unique in the region in which you are creating the stack.
            Note
            A stack name can contain only alphanumeric characters (case sensitive) and hyphens. It must start with an alphabetic character and cannot be longer than 128 characters.
            
    :type StackName: string
    :param TemplateBody: Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes. For more information, go to Template Anatomy in the AWS CloudFormation User Guide.
            Conditional: You must specify either the TemplateBody or the TemplateURL parameter, but not both.
            
    :type TemplateBody: string
    :param TemplateURL: Location of file containing the template body. The URL must point to a template (max size: 460,800 bytes) that is located in an Amazon S3 bucket. For more information, go to the Template Anatomy in the AWS CloudFormation User Guide.
            Conditional: You must specify either the TemplateBody or the TemplateURL parameter, but not both.
            
    :type TemplateURL: string
    :param Parameters: A list of Parameter structures that specify input parameters for the stack. For more information, see the Parameter data type.
            (dict) --The Parameter data type.
            ParameterKey (string) --The key associated with the parameter. If you don't specify a key and value for a particular parameter, AWS CloudFormation uses the default value that is specified in your template.
            ParameterValue (string) --The value associated with the parameter.
            UsePreviousValue (boolean) --During a stack update, use the existing parameter value that the stack is using for a given parameter key. If you specify true , do not specify a parameter value.
            
            
    :type Parameters: list
    :param DisableRollback: Set to true to disable rollback of the stack if stack creation failed. You can specify either DisableRollback or OnFailure , but not both.
            Default: false
            
    :type DisableRollback: boolean
    :param TimeoutInMinutes: The amount of time that can pass before the stack status becomes CREATE_FAILED; if DisableRollback is not set or is set to false , the stack will be rolled back.
    :type TimeoutInMinutes: integer
    :param NotificationARNs: The Simple Notification Service (SNS) topic ARNs to publish stack related events. You can find your SNS topic ARNs using the SNS console or your Command Line Interface (CLI).
            (string) --
            
    :type NotificationARNs: list
    :param Capabilities: A list of values that you must specify before AWS CloudFormation can create certain stacks. Some stack templates might include resources that can affect permissions in your AWS account, for example, by creating new AWS Identity and Access Management (IAM) users. For those stacks, you must explicitly acknowledge their capabilities by specifying this parameter.
            The only valid values are CAPABILITY_IAM and CAPABILITY_NAMED_IAM . The following resources require you to specify this parameter: AWS::IAM::AccessKey , AWS::IAM::Group , AWS::IAM::InstanceProfile , AWS::IAM::Policy , AWS::IAM::Role , AWS::IAM::User , and AWS::IAM::UserToGroupAddition . If your stack template contains these resources, we recommend that you review all permissions associated with them and edit their permissions if necessary.
            If you have IAM resources, you can specify either capability. If you have IAM resources with custom names, you must specify CAPABILITY_NAMED_IAM . If you don't specify this parameter, this action returns an InsufficientCapabilities error.
            For more information, see Acknowledging IAM Resources in AWS CloudFormation Templates .
            (string) --
            
    :type Capabilities: list
    :param ResourceTypes: The template resource types that you have permissions to work with for this create stack action, such as AWS::EC2::Instance , AWS::EC2::* , or Custom::MyCustomInstance . Use the following syntax to describe template resource types: AWS::* (for all AWS resource), Custom::* (for all custom resources), Custom::*logical_ID* `` (for a specific custom resource), ``AWS::*service_name* ::* (for all resources of a particular AWS service), and ``AWS::service_name ::resource_logical_ID `` (for a specific AWS resource).
            If the list of resource types doesn't include a resource that you're creating, the stack creation fails. By default, AWS CloudFormation grants permissions to all resource types. AWS Identity and Access Management (IAM) uses this parameter for AWS CloudFormation-specific condition keys in IAM policies. For more information, see Controlling Access with AWS Identity and Access Management .
            (string) --
            
    :type ResourceTypes: list
    :param RoleARN: The Amazon Resource Name (ARN) of an AWS Identity and Access Management (IAM) role that AWS CloudFormation assumes to create the stack. AWS CloudFormation uses the role's credentials to make calls on your behalf. AWS CloudFormation always uses this role for all future operations on the stack. As long as users have permission to operate on the stack, AWS CloudFormation uses this role even if the users don't have permission to pass it. Ensure that the role grants least privilege.
            If you don't specify a value, AWS CloudFormation uses the role that was previously associated with the stack. If no role is available, AWS CloudFormation uses a temporary session that is generated from your user credentials.
            
    :type RoleARN: string
    :param OnFailure: Determines what action will be taken if stack creation fails. This must be one of: DO_NOTHING, ROLLBACK, or DELETE. You can specify either OnFailure or DisableRollback , but not both.
            Default: ROLLBACK
            
    :type OnFailure: string
    :param StackPolicyBody: Structure containing the stack policy body. For more information, go to Prevent Updates to Stack Resources in the AWS CloudFormation User Guide . You can specify either the StackPolicyBody or the StackPolicyURL parameter, but not both.
    :type StackPolicyBody: string
    :param StackPolicyURL: Location of a file containing the stack policy. The URL must point to a policy (maximum size: 16 KB) located in an S3 bucket in the same region as the stack. You can specify either the StackPolicyBody or the StackPolicyURL parameter, but not both.
    :type StackPolicyURL: string
    :param Tags: Key-value pairs to associate with this stack. AWS CloudFormation also propagates these tags to the resources created in the stack. A maximum number of 10 tags can be specified.
            (dict) --The Tag type enables you to specify a key-value pair that can be used to store information about an AWS CloudFormation stack.
            Key (string) --
            Required . A string used to identify this tag. You can specify a maximum of 128 characters for a tag key. Tags owned by Amazon Web Services (AWS) have the reserved prefix: aws: .
            Value (string) --
            Required . A string containing the value for this tag. You can specify a maximum of 256 characters for a tag value.
            
            
    :type Tags: list
    """
    pass


def delete_change_set(ChangeSetName=None, StackName=None):
    """
    :param ChangeSetName: [REQUIRED]
            The name or Amazon Resource Name (ARN) of the change set that you want to delete.
            
    :type ChangeSetName: string
    :param StackName: If you specified the name of a change set to delete, specify the stack name or ID (ARN) that is associated with it.
    :type StackName: string
    """
    pass


def delete_stack(StackName=None, RetainResources=None, RoleARN=None):
    """
    :param StackName: [REQUIRED]
            The name or the unique stack ID that is associated with the stack.
            
    :type StackName: string
    :param RetainResources: For stacks in the DELETE_FAILED state, a list of resource logical IDs that are associated with the resources you want to retain. During deletion, AWS CloudFormation deletes the stack but does not delete the retained resources.
            Retaining resources is useful when you cannot delete a resource, such as a non-empty S3 bucket, but you want to delete the stack.
            (string) --
            
    :type RetainResources: list
    :param RoleARN: The Amazon Resource Name (ARN) of an AWS Identity and Access Management (IAM) role that AWS CloudFormation assumes to delete the stack. AWS CloudFormation uses the role's credentials to make calls on your behalf.
            If you don't specify a value, AWS CloudFormation uses the role that was previously associated with the stack. If no role is available, AWS CloudFormation uses a temporary session that is generated from your user credentials.
            
    :type RoleARN: string
    """
    pass


def describe_account_limits(NextToken=None):
    """
    :param NextToken: A string that identifies the next page of limits that you want to retrieve.
            Return typedict
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
            (dict) --The output for the DescribeAccountLimits action.
            AccountLimits (list) --An account limit structure that contain a list of AWS CloudFormation account limits and their values.
            (dict) --The AccountLimit data type.
            Name (string) --The name of the account limit. Currently, the only account limit is StackLimit .
            Value (integer) --The value that is associated with the account limit name.
            
            NextToken (string) --If the output exceeds 1 MB in size, a string that identifies the next page of limits. If no additional page exists, this value is null.
            
            
    :type NextToken: string
    """
    pass


def describe_change_set(ChangeSetName=None, StackName=None, NextToken=None):
    """
    :param ChangeSetName: [REQUIRED]
            The name or Amazon Resource Name (ARN) of the change set that you want to describe.
            
    :type ChangeSetName: string
    :param StackName: If you specified the name of a change set, specify the stack name or ID (ARN) of the change set you want to describe.
    :type StackName: string
    :param NextToken: A string (provided by the DescribeChangeSet response output) that identifies the next page of information that you want to retrieve.
    :type NextToken: string
    """
    pass


def describe_stack_events(StackName=None, NextToken=None):
    """
    :param StackName: The name or the unique stack ID that is associated with the stack, which are not always interchangeable:
            Running stacks: You can specify either the stack's name or its unique stack ID.
            Deleted stacks: You must specify the unique stack ID.
            Default: There is no default value.
            
    :type StackName: string
    :param NextToken: A string that identifies the next page of events that you want to retrieve.
    :type NextToken: string
    """
    pass


def describe_stack_resource(StackName=None, LogicalResourceId=None):
    """
    :param StackName: [REQUIRED]
            The name or the unique stack ID that is associated with the stack, which are not always interchangeable:
            Running stacks: You can specify either the stack's name or its unique stack ID.
            Deleted stacks: You must specify the unique stack ID.
            Default: There is no default value.
            
    :type StackName: string
    :param LogicalResourceId: [REQUIRED]
            The logical name of the resource as specified in the template.
            Default: There is no default value.
            
    :type LogicalResourceId: string
    """
    pass


def describe_stack_resources(StackName=None, LogicalResourceId=None, PhysicalResourceId=None):
    """
    :param StackName: The name or the unique stack ID that is associated with the stack, which are not always interchangeable:
            Running stacks: You can specify either the stack's name or its unique stack ID.
            Deleted stacks: You must specify the unique stack ID.
            Default: There is no default value.
            Required: Conditional. If you do not specify StackName , you must specify PhysicalResourceId .
            
    :type StackName: string
    :param LogicalResourceId: The logical name of the resource as specified in the template.
            Default: There is no default value.
            
    :type LogicalResourceId: string
    :param PhysicalResourceId: The name or unique identifier that corresponds to a physical instance ID of a resource supported by AWS CloudFormation.
            For example, for an Amazon Elastic Compute Cloud (EC2) instance, PhysicalResourceId corresponds to the InstanceId . You can pass the EC2 InstanceId to DescribeStackResources to find which stack the instance belongs to and what other resources are part of the stack.
            Required: Conditional. If you do not specify PhysicalResourceId , you must specify StackName .
            Default: There is no default value.
            
    :type PhysicalResourceId: string
    """
    pass


def describe_stacks(StackName=None, NextToken=None):
    """
    :param StackName: The name or the unique stack ID that is associated with the stack, which are not always interchangeable:
            Running stacks: You can specify either the stack's name or its unique stack ID.
            Deleted stacks: You must specify the unique stack ID.
            Default: There is no default value.
            
    :type StackName: string
    :param NextToken: A string that identifies the next page of stacks that you want to retrieve.
    :type NextToken: string
    """
    pass


def estimate_template_cost(TemplateBody=None, TemplateURL=None, Parameters=None):
    """
    :param TemplateBody: Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes. (For more information, go to Template Anatomy in the AWS CloudFormation User Guide.)
            Conditional: You must pass TemplateBody or TemplateURL . If both are passed, only TemplateBody is used.
            
    :type TemplateBody: string
    :param TemplateURL: Location of file containing the template body. The URL must point to a template that is located in an Amazon S3 bucket. For more information, go to Template Anatomy in the AWS CloudFormation User Guide.
            Conditional: You must pass TemplateURL or TemplateBody . If both are passed, only TemplateBody is used.
            
    :type TemplateURL: string
    :param Parameters: A list of Parameter structures that specify input parameters.
            (dict) --The Parameter data type.
            ParameterKey (string) --The key associated with the parameter. If you don't specify a key and value for a particular parameter, AWS CloudFormation uses the default value that is specified in your template.
            ParameterValue (string) --The value associated with the parameter.
            UsePreviousValue (boolean) --During a stack update, use the existing parameter value that the stack is using for a given parameter key. If you specify true , do not specify a parameter value.
            
            
    :type Parameters: list
    """
    pass


def execute_change_set(ChangeSetName=None, StackName=None):
    """
    :param ChangeSetName: [REQUIRED]
            The name or ARN of the change set that you want use to update the specified stack.
            
    :type ChangeSetName: string
    :param StackName: If you specified the name of a change set, specify the stack name or ID (ARN) that is associated with the change set you want to execute.
    :type StackName: string
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


def get_stack_policy(StackName=None):
    """
    :param StackName: [REQUIRED]
            The name or unique stack ID that is associated with the stack whose policy you want to get.
            Return typedict
            ReturnsResponse Syntax{
              'StackPolicyBody': 'string'
            }
            Response Structure
            (dict) --The output for the GetStackPolicy action.
            StackPolicyBody (string) --Structure containing the stack policy body. (For more information, go to Prevent Updates to Stack Resources in the AWS CloudFormation User Guide.)
            
            
    :type StackName: string
    """
    pass


def get_template(StackName=None):
    """
    :param StackName: [REQUIRED]
            The name or the unique stack ID that is associated with the stack, which are not always interchangeable:
            Running stacks: You can specify either the stack's name or its unique stack ID.
            Deleted stacks: You must specify the unique stack ID.
            Default: There is no default value.
            Return typedict
            ReturnsResponse Syntax{
              'TemplateBody': 'string'
            }
            Response Structure
            (dict) --The output for GetTemplate action.
            TemplateBody (string) --Structure containing the template body. (For more information, go to Template Anatomy in the AWS CloudFormation User Guide.)
            AWS CloudFormation returns the same template that was used when the stack was created.
            
            
    :type StackName: string
    """
    pass


def get_template_summary(TemplateBody=None, TemplateURL=None, StackName=None):
    """
    :param TemplateBody: Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes. For more information about templates, see Template Anatomy in the AWS CloudFormation User Guide.
            Conditional: You must specify only one of the following parameters: StackName , TemplateBody , or TemplateURL .
            
    :type TemplateBody: string
    :param TemplateURL: Location of file containing the template body. The URL must point to a template (max size: 460,800 bytes) that is located in an Amazon S3 bucket. For more information about templates, see Template Anatomy in the AWS CloudFormation User Guide.
            Conditional: You must specify only one of the following parameters: StackName , TemplateBody , or TemplateURL .
            
    :type TemplateURL: string
    :param StackName: The name or the stack ID that is associated with the stack, which are not always interchangeable. For running stacks, you can specify either the stack's name or its unique stack ID. For deleted stack, you must specify the unique stack ID.
            Conditional: You must specify only one of the following parameters: StackName , TemplateBody , or TemplateURL .
            
    :type StackName: string
    """
    pass


def get_waiter():
    """
    """
    pass


def list_change_sets(StackName=None, NextToken=None):
    """
    :param StackName: [REQUIRED]
            The name or the Amazon Resource Name (ARN) of the stack for which you want to list change sets.
            
    :type StackName: string
    :param NextToken: A string (provided by the ListChangeSets response output) that identifies the next page of change sets that you want to retrieve.
    :type NextToken: string
    """
    pass


def list_stack_resources(StackName=None, NextToken=None):
    """
    :param StackName: [REQUIRED]
            The name or the unique stack ID that is associated with the stack, which are not always interchangeable:
            Running stacks: You can specify either the stack's name or its unique stack ID.
            Deleted stacks: You must specify the unique stack ID.
            Default: There is no default value.
            
    :type StackName: string
    :param NextToken: A string that identifies the next page of stack resources that you want to retrieve.
    :type NextToken: string
    """
    pass


def list_stacks(NextToken=None, StackStatusFilter=None):
    """
    :param NextToken: A string that identifies the next page of stacks that you want to retrieve.
    :type NextToken: string
    :param StackStatusFilter: Stack status to use as a filter. Specify one or more stack status codes to list only stacks with the specified status codes. For a complete list of stack status codes, see the StackStatus parameter of the Stack data type.
            (string) --
            
    :type StackStatusFilter: list
    """
    pass


def set_stack_policy(StackName=None, StackPolicyBody=None, StackPolicyURL=None):
    """
    :param StackName: [REQUIRED]
            The name or unique stack ID that you want to associate a policy with.
            
    :type StackName: string
    :param StackPolicyBody: Structure containing the stack policy body. For more information, go to Prevent Updates to Stack Resources in the AWS CloudFormation User Guide. You can specify either the StackPolicyBody or the StackPolicyURL parameter, but not both.
    :type StackPolicyBody: string
    :param StackPolicyURL: Location of a file containing the stack policy. The URL must point to a policy (maximum size: 16 KB) located in an S3 bucket in the same region as the stack. You can specify either the StackPolicyBody or the StackPolicyURL parameter, but not both.
    :type StackPolicyURL: string
    """
    pass


def signal_resource(StackName=None, LogicalResourceId=None, UniqueId=None, Status=None):
    """
    :param StackName: [REQUIRED]
            The stack name or unique stack ID that includes the resource that you want to signal.
            
    :type StackName: string
    :param LogicalResourceId: [REQUIRED]
            The logical ID of the resource that you want to signal. The logical ID is the name of the resource that given in the template.
            
    :type LogicalResourceId: string
    :param UniqueId: [REQUIRED]
            A unique ID of the signal. When you signal Amazon EC2 instances or Auto Scaling groups, specify the instance ID that you are signaling as the unique ID. If you send multiple signals to a single resource (such as signaling a wait condition), each signal requires a different unique ID.
            
    :type UniqueId: string
    :param Status: [REQUIRED]
            The status of the signal, which is either success or failure. A failure signal causes AWS CloudFormation to immediately fail the stack creation or update.
            
    :type Status: string
    """
    pass


def update_stack(StackName=None, TemplateBody=None, TemplateURL=None, UsePreviousTemplate=None,
                 StackPolicyDuringUpdateBody=None, StackPolicyDuringUpdateURL=None, Parameters=None, Capabilities=None,
                 ResourceTypes=None, RoleARN=None, StackPolicyBody=None, StackPolicyURL=None, NotificationARNs=None,
                 Tags=None):
    """
    :param StackName: [REQUIRED]
            The name or unique stack ID of the stack to update.
            
    :type StackName: string
    :param TemplateBody: Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes. (For more information, go to Template Anatomy in the AWS CloudFormation User Guide.)
            Conditional: You must specify either the TemplateBody or the TemplateURL parameter, but not both.
            
    :type TemplateBody: string
    :param TemplateURL: Location of file containing the template body. The URL must point to a template that is located in an Amazon S3 bucket. For more information, go to Template Anatomy in the AWS CloudFormation User Guide.
            Conditional: You must specify either the TemplateBody or the TemplateURL parameter, but not both.
            
    :type TemplateURL: string
    :param UsePreviousTemplate: Reuse the existing template that is associated with the stack that you are updating.
    :type UsePreviousTemplate: boolean
    :param StackPolicyDuringUpdateBody: Structure containing the temporary overriding stack policy body. You can specify either the StackPolicyDuringUpdateBody or the StackPolicyDuringUpdateURL parameter, but not both.
            If you want to update protected resources, specify a temporary overriding stack policy during this update. If you do not specify a stack policy, the current policy that is associated with the stack will be used.
            
    :type StackPolicyDuringUpdateBody: string
    :param StackPolicyDuringUpdateURL: Location of a file containing the temporary overriding stack policy. The URL must point to a policy (max size: 16KB) located in an S3 bucket in the same region as the stack. You can specify either the StackPolicyDuringUpdateBody or the StackPolicyDuringUpdateURL parameter, but not both.
            If you want to update protected resources, specify a temporary overriding stack policy during this update. If you do not specify a stack policy, the current policy that is associated with the stack will be used.
            
    :type StackPolicyDuringUpdateURL: string
    :param Parameters: A list of Parameter structures that specify input parameters for the stack. For more information, see the Parameter data type.
            (dict) --The Parameter data type.
            ParameterKey (string) --The key associated with the parameter. If you don't specify a key and value for a particular parameter, AWS CloudFormation uses the default value that is specified in your template.
            ParameterValue (string) --The value associated with the parameter.
            UsePreviousValue (boolean) --During a stack update, use the existing parameter value that the stack is using for a given parameter key. If you specify true , do not specify a parameter value.
            
            
    :type Parameters: list
    :param Capabilities: A list of values that you must specify before AWS CloudFormation can update certain stacks. Some stack templates might include resources that can affect permissions in your AWS account, for example, by creating new AWS Identity and Access Management (IAM) users. For those stacks, you must explicitly acknowledge their capabilities by specifying this parameter.
            The only valid values are CAPABILITY_IAM and CAPABILITY_NAMED_IAM . The following resources require you to specify this parameter: AWS::IAM::AccessKey , AWS::IAM::Group , AWS::IAM::InstanceProfile , AWS::IAM::Policy , AWS::IAM::Role , AWS::IAM::User , and AWS::IAM::UserToGroupAddition . If your stack template contains these resources, we recommend that you review all permissions associated with them and edit their permissions if necessary.
            If you have IAM resources, you can specify either capability. If you have IAM resources with custom names, you must specify CAPABILITY_NAMED_IAM . If you don't specify this parameter, this action returns an InsufficientCapabilities error.
            For more information, see Acknowledging IAM Resources in AWS CloudFormation Templates .
            (string) --
            
    :type Capabilities: list
    :param ResourceTypes: The template resource types that you have permissions to work with for this update stack action, such as AWS::EC2::Instance , AWS::EC2::* , or Custom::MyCustomInstance .
            If the list of resource types doesn't include a resource that you're updating, the stack update fails. By default, AWS CloudFormation grants permissions to all resource types. AWS Identity and Access Management (IAM) uses this parameter for AWS CloudFormation-specific condition keys in IAM policies. For more information, see Controlling Access with AWS Identity and Access Management .
            (string) --
            
    :type ResourceTypes: list
    :param RoleARN: The Amazon Resource Name (ARN) of an AWS Identity and Access Management (IAM) role that AWS CloudFormation assumes to update the stack. AWS CloudFormation uses the role's credentials to make calls on your behalf. AWS CloudFormation always uses this role for all future operations on the stack. As long as users have permission to operate on the stack, AWS CloudFormation uses this role even if the users don't have permission to pass it. Ensure that the role grants least privilege.
            If you don't specify a value, AWS CloudFormation uses the role that was previously associated with the stack. If no role is available, AWS CloudFormation uses a temporary session that is generated from your user credentials.
            
    :type RoleARN: string
    :param StackPolicyBody: Structure containing a new stack policy body. You can specify either the StackPolicyBody or the StackPolicyURL parameter, but not both.
            You might update the stack policy, for example, in order to protect a new resource that you created during a stack update. If you do not specify a stack policy, the current policy that is associated with the stack is unchanged.
            
    :type StackPolicyBody: string
    :param StackPolicyURL: Location of a file containing the updated stack policy. The URL must point to a policy (max size: 16KB) located in an S3 bucket in the same region as the stack. You can specify either the StackPolicyBody or the StackPolicyURL parameter, but not both.
            You might update the stack policy, for example, in order to protect a new resource that you created during a stack update. If you do not specify a stack policy, the current policy that is associated with the stack is unchanged.
            
    :type StackPolicyURL: string
    :param NotificationARNs: Amazon Simple Notification Service topic Amazon Resource Names (ARNs) that AWS CloudFormation associates with the stack. Specify an empty list to remove all notification topics.
            (string) --
            
    :type NotificationARNs: list
    :param Tags: Key-value pairs to associate with this stack. AWS CloudFormation also propagates these tags to supported resources in the stack. You can specify a maximum number of 10 tags.
            If you don't specify this parameter, AWS CloudFormation doesn't modify the stack's tags. If you specify an empty value, AWS CloudFormation removes all associated tags.
            (dict) --The Tag type enables you to specify a key-value pair that can be used to store information about an AWS CloudFormation stack.
            Key (string) --
            Required . A string used to identify this tag. You can specify a maximum of 128 characters for a tag key. Tags owned by Amazon Web Services (AWS) have the reserved prefix: aws: .
            Value (string) --
            Required . A string containing the value for this tag. You can specify a maximum of 256 characters for a tag value.
            
            
    :type Tags: list
    """
    pass


def validate_template(TemplateBody=None, TemplateURL=None):
    """
    :param TemplateBody: Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes. For more information, go to Template Anatomy in the AWS CloudFormation User Guide.
            Conditional: You must pass TemplateURL or TemplateBody . If both are passed, only TemplateBody is used.
            
    :type TemplateBody: string
    :param TemplateURL: Location of file containing the template body. The URL must point to a template (max size: 460,800 bytes) that is located in an Amazon S3 bucket. For more information, go to Template Anatomy in the AWS CloudFormation User Guide.
            Conditional: You must pass TemplateURL or TemplateBody . If both are passed, only TemplateBody is used.
            
    :type TemplateURL: string
    """
    pass
