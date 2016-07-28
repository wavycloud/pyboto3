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

import boto3


class Ssm(object):
    def __init__(self):
        self.client = boto3.client('Ssm')

    def add_tags_to_resource(self, ResourceType=None, ResourceId=None, Tags=None):
        """
        :param ResourceType: [REQUIRED]
            Specifies the type of resource you are tagging.
            
        :type ResourceType: string
        :param ResourceId: [REQUIRED]
            The resource ID you want to tag.
            
        :type ResourceId: string
        :param Tags: [REQUIRED]
            One or more tags. The value parameter is required, but if you don't want the tag to have a value, specify the parameter with no value, and we set the value to an empty string.
            (dict) --Metadata that you assign to your managed instances. Tags enable you to categorize your managed instances in different ways, for example, by purpose, owner, or environment.
            Key (string) -- [REQUIRED]The name of the tag.
            Value (string) -- [REQUIRED]The value of the tag.
            
            
        :type Tags: list
        """
        self.client.add_tags_to_resource(ResourceType=ResourceType, ResourceId=ResourceId, Tags=Tags)

    def can_paginate(self, operation_name=None):
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
        self.client.can_paginate(operation_name=operation_name)

    def cancel_command(self, CommandId=None, InstanceIds=None):
        """
        :param CommandId: [REQUIRED]
            The ID of the command you want to cancel.
            
        :type CommandId: string
        :param InstanceIds: (Optional) A list of instance IDs on which you want to cancel the command. If not provided, the command is canceled on every instance on which it was requested.
            (string) --
            
        :type InstanceIds: list
        """
        self.client.cancel_command(CommandId=CommandId, InstanceIds=InstanceIds)

    def create_activation(self, Description=None, DefaultInstanceName=None, IamRole=None, RegistrationLimit=None,
                          ExpirationDate=None):
        """
        :param Description: A user-defined description of the resource that you want to register with Amazon EC2.
        :type Description: string
        :param DefaultInstanceName: The name of the registered, managed instance as it will appear in the Amazon EC2 console or when you use the AWS command line tools to list EC2 resources.
        :type DefaultInstanceName: string
        :param IamRole: [REQUIRED]
            The Amazon Identity and Access Management (IAM) role that you want to assign to the managed instance.
            
        :type IamRole: string
        :param RegistrationLimit: Specify the maximum number of managed instances you want to register. The default value is 1 instance.
        :type RegistrationLimit: integer
        :param ExpirationDate: The date by which this activation request should expire. The default value is 24 hours.
        :type ExpirationDate: datetime
        """
        self.client.create_activation(Description=Description, DefaultInstanceName=DefaultInstanceName, IamRole=IamRole,
                                      RegistrationLimit=RegistrationLimit, ExpirationDate=ExpirationDate)

    def create_association(self, Name=None, InstanceId=None, Parameters=None):
        """
        :param Name: [REQUIRED]
            The name of the SSM document.
            
        :type Name: string
        :param InstanceId: [REQUIRED]
            The instance ID.
            
        :type InstanceId: string
        :param Parameters: The parameters for the documents runtime configuration.
            (string) --
            (list) --
            (string) --
            
            
        :type Parameters: dict
        """
        self.client.create_association(Name=Name, InstanceId=InstanceId, Parameters=Parameters)

    def create_association_batch(self, Entries=None):
        """
        :param Entries: [REQUIRED]
            One or more associations.
            (dict) --Describes the association of an SSM document and an instance.
            Name (string) --The name of the configuration document.
            InstanceId (string) --The ID of the instance.
            Parameters (dict) --A description of the parameters for a document.
            (string) --
            (list) --
            (string) --
            
            
            Return typedict
            ReturnsResponse Syntax{
              'Successful': [
                {
                  'Name': 'string',
                  'InstanceId': 'string',
                  'Date': datetime(2015, 1, 1),
                  'Status': {
                    'Date': datetime(2015, 1, 1),
                    'Name': 'Pending'|'Success'|'Failed',
                    'Message': 'string',
                    'AdditionalInfo': 'string'
                  },
                  'Parameters': {
                    'string': [
                      'string',
                    ]
                  }
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
                    }
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
            Name (string) --The name of the SSM document.
            InstanceId (string) --The ID of the instance.
            Date (datetime) --The date when the association was made.
            Status (dict) --The association status.
            Date (datetime) --The date when the status changed.
            Name (string) --The status.
            Message (string) --The reason for the status.
            AdditionalInfo (string) --A user-defined string.
            Parameters (dict) --A description of the parameters for a document.
            (string) --
            (list) --
            (string) --
            
            
            Failed (list) --Information about the associations that failed.
            (dict) --Describes a failed association.
            Entry (dict) --The association.
            Name (string) --The name of the configuration document.
            InstanceId (string) --The ID of the instance.
            Parameters (dict) --A description of the parameters for a document.
            (string) --
            (list) --
            (string) --
            
            
            Message (string) --A description of the failure.
            Fault (string) --The source of the failure.
            
            
            
        :type Entries: list
        """
        self.client.create_association_batch(Entries=Entries)

    def create_document(self, Content=None, Name=None):
        """
        :param Content: [REQUIRED]
            A valid JSON string.
            
        :type Content: string
        :param Name: [REQUIRED]
            A name for the SSM document.
            
        :type Name: string
        """
        self.client.create_document(Content=Content, Name=Name)

    def delete_activation(self, ActivationId=None):
        """
        :param ActivationId: [REQUIRED]
            The ID of the activation that you want to delete.
            Return typedict
            ReturnsResponse Syntax{}
            Response Structure
            (dict) --
            
        :type ActivationId: string
        """
        self.client.delete_activation(ActivationId=ActivationId)

    def delete_association(self, Name=None, InstanceId=None):
        """
        :param Name: [REQUIRED]
            The name of the SSM document.
            
        :type Name: string
        :param InstanceId: [REQUIRED]
            The ID of the instance.
            
        :type InstanceId: string
        """
        self.client.delete_association(Name=Name, InstanceId=InstanceId)

    def delete_document(self, Name=None):
        """
        :param Name: [REQUIRED]
            The name of the SSM document.
            Return typedict
            ReturnsResponse Syntax{}
            Response Structure
            (dict) --
            
        :type Name: string
        """
        self.client.delete_document(Name=Name)

    def deregister_managed_instance(self, InstanceId=None):
        """
        :param InstanceId: [REQUIRED]
            The ID assigned to the managed instance when you registered it using the activation process.
            Return typedict
            ReturnsResponse Syntax{}
            Response Structure
            (dict) --
            
        :type InstanceId: string
        """
        self.client.deregister_managed_instance(InstanceId=InstanceId)

    def describe_activations(self, Filters=None, MaxResults=None, NextToken=None):
        """
        :param Filters: A filter to view information about your activations.
            (dict) --Filter for the DescribeActivation API.
            FilterKey (string) --The name of the filter.
            FilterValues (list) --The filter values.
            (string) --
            
            
        :type Filters: list
        :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
        :type MaxResults: integer
        :param NextToken: A token to start the list. Use this token to get the next set of results.
        :type NextToken: string
        """
        self.client.describe_activations(Filters=Filters, MaxResults=MaxResults, NextToken=NextToken)

    def describe_association(self, Name=None, InstanceId=None):
        """
        :param Name: [REQUIRED]
            The name of the SSM document.
            
        :type Name: string
        :param InstanceId: [REQUIRED]
            The instance ID.
            
        :type InstanceId: string
        """
        self.client.describe_association(Name=Name, InstanceId=InstanceId)

    def describe_document(self, Name=None):
        """
        :param Name: [REQUIRED]
            The name of the SSM document.
            Return typedict
            ReturnsResponse Syntax{
              'Document': {
                'Sha1': 'string',
                'Hash': 'string',
                'HashType': 'Sha256'|'Sha1',
                'Name': 'string',
                'Owner': 'string',
                'CreatedDate': datetime(2015, 1, 1),
                'Status': 'Creating'|'Active'|'Deleting',
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
                ]
              }
            }
            Response Structure
            (dict) --
            Document (dict) --Information about the SSM document.
            Sha1 (string) --The SHA1 hash of the document, which you can use for verification purposes.
            Hash (string) --The Sha256 or Sha1 hash created by the system when the document was created.
            Note
            Sha1 hashes have been deprecated.
            HashType (string) --Sha256 or Sha1.
            Note
            Sha1 hashes have been deprecated.
            Name (string) --The name of the SSM document.
            Owner (string) --The AWS user account of the person who created the document.
            CreatedDate (datetime) --The date when the SSM document was created.
            Status (string) --The status of the SSM document.
            Description (string) --A description of the document.
            Parameters (list) --A description of the parameters for a document.
            (dict) --Parameters specified in the SSM document that execute on the server when the command is run.
            Name (string) --The name of the parameter.
            Type (string) --The type of parameter. The type can be either  String  or  StringList .
            Description (string) --A description of what the parameter does, how to use it, the default value, and whether or not the parameter is optional.
            DefaultValue (string) --If specified, the default values for the parameters. Parameters without a default value are required. Parameters with a default value are optional.
            
            PlatformTypes (list) --The list of OS platforms compatible with this SSM document.
            (string) --
            
            
            
        :type Name: string
        """
        self.client.describe_document(Name=Name)

    def describe_document_permission(self, Name=None, PermissionType=None):
        """
        :param Name: [REQUIRED]
            The name of the document for which you are the owner.
            
        :type Name: string
        :param PermissionType: [REQUIRED]
            The permission type for the document. The permission type can be Share .
            
        :type PermissionType: string
        """
        self.client.describe_document_permission(Name=Name, PermissionType=PermissionType)

    def describe_instance_information(self, InstanceInformationFilterList=None, MaxResults=None, NextToken=None):
        """
        :param InstanceInformationFilterList: One or more filters. Use a filter to return a more specific list of instances.
            (dict) --Describes a filter for a specific list of instances.
            key (string) -- [REQUIRED]The name of the filter.
            valueSet (list) -- [REQUIRED]The filter values.
            (string) --
            
            
        :type InstanceInformationFilterList: list
        :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
        :type MaxResults: integer
        :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)
        :type NextToken: string
        """
        self.client.describe_instance_information(InstanceInformationFilterList=InstanceInformationFilterList,
                                                  MaxResults=MaxResults, NextToken=NextToken)

    def generate_presigned_url(self, ClientMethod=None, Params=None, ExpiresIn=None, HttpMethod=None):
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
        self.client.generate_presigned_url(ClientMethod=ClientMethod, Params=Params, ExpiresIn=ExpiresIn,
                                           HttpMethod=HttpMethod)

    def get_document(self, Name=None):
        """
        :param Name: [REQUIRED]
            The name of the SSM document.
            Return typedict
            ReturnsResponse Syntax{
              'Name': 'string',
              'Content': 'string'
            }
            Response Structure
            (dict) --
            Name (string) --The name of the SSM document.
            Content (string) --The contents of the SSM document.
            
            
        :type Name: string
        """
        self.client.get_document(Name=Name)

    def get_paginator(self, operation_name=None):
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
        self.client.get_paginator(operation_name=operation_name)

    def get_waiter(self):
        """
        """
        self.client.get_waiter()

    def list_associations(self, AssociationFilterList=None, MaxResults=None, NextToken=None):
        """
        :param AssociationFilterList: [REQUIRED]
            One or more filters. Use a filter to return a more specific list of results.
            (dict) --Describes a filter.
            key (string) -- [REQUIRED]The name of the filter.
            value (string) -- [REQUIRED]The filter value.
            
            
        :type AssociationFilterList: list
        :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
        :type MaxResults: integer
        :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)
        :type NextToken: string
        """
        self.client.list_associations(AssociationFilterList=AssociationFilterList, MaxResults=MaxResults,
                                      NextToken=NextToken)

    def list_command_invocations(self, CommandId=None, InstanceId=None, MaxResults=None, NextToken=None, Filters=None,
                                 Details=None):
        """
        :param CommandId: (Optional) The invocations for a specific command ID.
        :type CommandId: string
        :param InstanceId: (Optional) The command execution details for a specific instance ID.
        :type InstanceId: string
        :param MaxResults: (Optional) The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
        :type MaxResults: integer
        :param NextToken: (Optional) The token for the next set of items to return. (You received this token from a previous call.)
        :type NextToken: string
        :param Filters: (Optional) One or more filters. Use a filter to return a more specific list of results.
            (dict) --Describes a command filter.
            key (string) -- [REQUIRED]The name of the filter. For example, requested date and time.
            value (string) -- [REQUIRED]The filter value. For example: June 30, 2015.
            
            
        :type Filters: list
        :param Details: (Optional) If set this returns the response of the command executions and any command output. By default this is set to False.
        :type Details: boolean
        """
        self.client.list_command_invocations(CommandId=CommandId, InstanceId=InstanceId, MaxResults=MaxResults,
                                             NextToken=NextToken, Filters=Filters, Details=Details)

    def list_commands(self, CommandId=None, InstanceId=None, MaxResults=None, NextToken=None, Filters=None):
        """
        :param CommandId: (Optional) If provided, lists only the specified command.
        :type CommandId: string
        :param InstanceId: (Optional) Lists commands issued against this instance ID.
        :type InstanceId: string
        :param MaxResults: (Optional) The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
        :type MaxResults: integer
        :param NextToken: (Optional) The token for the next set of items to return. (You received this token from a previous call.)
        :type NextToken: string
        :param Filters: (Optional) One or more filters. Use a filter to return a more specific list of results.
            (dict) --Describes a command filter.
            key (string) -- [REQUIRED]The name of the filter. For example, requested date and time.
            value (string) -- [REQUIRED]The filter value. For example: June 30, 2015.
            
            
        :type Filters: list
        """
        self.client.list_commands(CommandId=CommandId, InstanceId=InstanceId, MaxResults=MaxResults,
                                  NextToken=NextToken, Filters=Filters)

    def list_documents(self, DocumentFilterList=None, MaxResults=None, NextToken=None):
        """
        :param DocumentFilterList: One or more filters. Use a filter to return a more specific list of results.
            (dict) --Describes a filter.
            key (string) -- [REQUIRED]The name of the filter.
            value (string) -- [REQUIRED]The value of the filter.
            
            
        :type DocumentFilterList: list
        :param MaxResults: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
        :type MaxResults: integer
        :param NextToken: The token for the next set of items to return. (You received this token from a previous call.)
        :type NextToken: string
        """
        self.client.list_documents(DocumentFilterList=DocumentFilterList, MaxResults=MaxResults, NextToken=NextToken)

    def list_tags_for_resource(self, ResourceType=None, ResourceId=None):
        """
        :param ResourceType: [REQUIRED]
            Returns a list of tags for a specific resource type.
            
        :type ResourceType: string
        :param ResourceId: [REQUIRED]
            The resource ID for which you want to see a list of tags.
            
        :type ResourceId: string
        """
        self.client.list_tags_for_resource(ResourceType=ResourceType, ResourceId=ResourceId)

    def modify_document_permission(self, Name=None, PermissionType=None, AccountIdsToAdd=None, AccountIdsToRemove=None):
        """
        :param Name: [REQUIRED]
            The name of the document that you want to share.
            
        :type Name: string
        :param PermissionType: [REQUIRED]
            The permission type for the document. The permission type can be Share .
            
        :type PermissionType: string
        :param AccountIdsToAdd: The AWS user accounts that should have access to the document. The account IDs can either be a group of account IDs or All .
            (string) --
            
        :type AccountIdsToAdd: list
        :param AccountIdsToRemove: The AWS user accounts that should no longer have access to the document. The AWS user account can either be a group of account IDs or All . This action has a higher priority than AccountIdsToAdd . If you specify an account ID to add and the same ID to remove, the system removes access to the document.
            (string) --
            
        :type AccountIdsToRemove: list
        """
        self.client.modify_document_permission(Name=Name, PermissionType=PermissionType,
                                               AccountIdsToAdd=AccountIdsToAdd, AccountIdsToRemove=AccountIdsToRemove)

    def remove_tags_from_resource(self, ResourceType=None, ResourceId=None, TagKeys=None):
        """
        :param ResourceType: [REQUIRED]
            The type of resource of which you want to remove a tag.
            
        :type ResourceType: string
        :param ResourceId: [REQUIRED]
            The resource ID for which you want to remove tags.
            
        :type ResourceId: string
        :param TagKeys: [REQUIRED]
            Tag keys that you want to remove from the specified resource.
            (string) --
            
        :type TagKeys: list
        """
        self.client.remove_tags_from_resource(ResourceType=ResourceType, ResourceId=ResourceId, TagKeys=TagKeys)

    def send_command(self, InstanceIds=None, DocumentName=None, DocumentHash=None, DocumentHashType=None,
                     TimeoutSeconds=None, Comment=None, Parameters=None, OutputS3BucketName=None,
                     OutputS3KeyPrefix=None, ServiceRoleArn=None, NotificationConfig=None):
        """
        :param InstanceIds: [REQUIRED]
            Required. The instance IDs where the command should execute. You can specify a maximum of 50 IDs.
            (string) --
            
        :type InstanceIds: list
        :param DocumentName: [REQUIRED]
            Required. The name of the SSM document to execute. This can be an SSM public document or a custom document.
            
        :type DocumentName: string
        :param DocumentHash: The Sha256 or Sha1 hash created by the system when the document was created.
            Note
            Sha1 hashes have been deprecated.
            
        :type DocumentHash: string
        :param DocumentHashType: Sha256 or Sha1.
            Note
            Sha1 hashes have been deprecated.
            
        :type DocumentHashType: string
        :param TimeoutSeconds: If this time is reached and the command has not already started executing, it will not execute.
        :type TimeoutSeconds: integer
        :param Comment: User-specified information about the command, such as a brief description of what the command should do.
        :type Comment: string
        :param Parameters: The required and optional parameters specified in the SSM document being executed.
            (string) --
            (list) --
            (string) --
            
            
        :type Parameters: dict
        :param OutputS3BucketName: The name of the S3 bucket where command execution responses should be stored.
        :type OutputS3BucketName: string
        :param OutputS3KeyPrefix: The directory structure within the S3 bucket where the responses should be stored.
        :type OutputS3KeyPrefix: string
        :param ServiceRoleArn: The IAM role that SSM uses to send notifications.
        :type ServiceRoleArn: string
        :param NotificationConfig: Configurations for sending notifications.
            NotificationArn (string) --An Amazon Resource Name (ARN) for a Simple Notification Service (SNS) topic. SSM pushes notifications about command status changes to this topic.
            NotificationEvents (list) --The different events for which you can receive notifications. These events include the following: All (events), InProgress, Success, TimedOut, Cancelled, Failed. To learn more about these events, see Monitoring Commands in the Amazon Elastic Compute Cloud User Guide .
            (string) --
            NotificationType (string) --Command: Receive notification when the status of a command changes. Invocation: For commands sent to multiple instances, receive notification on a per-instance basis when the status of a command changes.
            
        :type NotificationConfig: dict
        """
        self.client.send_command(InstanceIds=InstanceIds, DocumentName=DocumentName, DocumentHash=DocumentHash,
                                 DocumentHashType=DocumentHashType, TimeoutSeconds=TimeoutSeconds, Comment=Comment,
                                 Parameters=Parameters, OutputS3BucketName=OutputS3BucketName,
                                 OutputS3KeyPrefix=OutputS3KeyPrefix, ServiceRoleArn=ServiceRoleArn,
                                 NotificationConfig=NotificationConfig)

    def update_association_status(self, Name=None, InstanceId=None, AssociationStatus=None):
        """
        :param Name: [REQUIRED]
            The name of the SSM document.
            
        :type Name: string
        :param InstanceId: [REQUIRED]
            The ID of the instance.
            
        :type InstanceId: string
        :param AssociationStatus: [REQUIRED]
            The association status.
            Date (datetime) -- [REQUIRED]The date when the status changed.
            Name (string) -- [REQUIRED]The status.
            Message (string) -- [REQUIRED]The reason for the status.
            AdditionalInfo (string) --A user-defined string.
            
        :type AssociationStatus: dict
        """
        self.client.update_association_status(Name=Name, InstanceId=InstanceId, AssociationStatus=AssociationStatus)

    def update_managed_instance_role(self, InstanceId=None, IamRole=None):
        """
        :param InstanceId: [REQUIRED]
            The ID of the managed instance where you want to update the role.
            
        :type InstanceId: string
        :param IamRole: [REQUIRED]
            The IAM role you want to assign or change.
            
        :type IamRole: string
        """
        self.client.update_managed_instance_role(InstanceId=InstanceId, IamRole=IamRole)
