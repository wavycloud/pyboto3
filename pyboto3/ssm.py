'''

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

'''

def add_tags_to_resource(ResourceType=None, ResourceId=None, Tags=None):
    """
    Adds or overwrites one or more tags for the specified resource. Tags are metadata that you assign to your managed instances. Tags enable you to categorize your managed instances in different ways, for example, by purpose, owner, or environment. Each tag consists of a key and an optional value, both of which you define. For example, you could define a set of tags for your account's managed instances that helps you track each instance's owner and stack level. For example: Key=Owner and Value=DbAdmin, SysAdmin, or Dev. Or Key=Stack and Value=Production, Pre-Production, or Test. Each resource can have a maximum of 10 tags.
    We recommend that you devise a set of tag keys that meets your needs for each resource type. Using a consistent set of tag keys makes it easier for you to manage your resources. You can search and filter the resources based on the tags you add. Tags don't have any semantic meaning to Amazon EC2 and are interpreted strictly as a string of characters.
    For more information about tags, see Tagging Your Amazon EC2 Resources in the Amazon EC2 User Guide.
    
    
    :example: response = client.add_tags_to_resource(
        ResourceType='ManagedInstance',
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
            

    :type Tags: list
    :param Tags: [REQUIRED]
            One or more tags. The value parameter is required, but if you don't want the tag to have a value, specify the parameter with no value, and we set the value to an empty string.
            (dict) --Metadata that you assign to your managed instances. Tags enable you to categorize your managed instances in different ways, for example, by purpose, owner, or environment.
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
    Registers your on-premises server or virtual machine with Amazon EC2 so that you can manage these resources using Run Command. An on-premises server or virtual machine that has been registered with EC2 is called a managed instance. For more information about activations, see Setting Up Managed Instances (Linux) or Setting Up Managed Instances (Windows) in the Amazon EC2 User Guide.
    
    
    :example: response = client.create_activation(
        Description='string',
        DefaultInstanceName='string',
        IamRole='string',
        RegistrationLimit=123,
        ExpirationDate=datetime(2015, 1, 1)
    )
    
    
    :type Description: string
    :param Description: A user-defined description of the resource that you want to register with Amazon EC2.

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

def create_association(Name=None, InstanceId=None, Parameters=None):
    """
    Associates the specified SSM document with the specified instance.
    When you associate an SSM document with an instance, the configuration agent on the instance (SSM agent for Linux and EC2Config service for Windows) processes the document and configures the instance as specified.
    If you associate a document with an instance that already has an associated document, the system throws the AssociationAlreadyExists exception.
    
    
    :example: response = client.create_association(
        Name='string',
        InstanceId='string',
        Parameters={
            'string': [
                'string',
            ]
        }
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the SSM document.
            

    :type InstanceId: string
    :param InstanceId: [REQUIRED]
            The instance ID.
            

    :type Parameters: dict
    :param Parameters: The parameters for the documents runtime configuration.
            (string) --
            (list) --
            (string) --
            
            

    :rtype: dict
    :return: {
        'AssociationDescription': {
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
        }
    }
    
    
    :returns: 
    (string) --
    (list) --
    (string) --
    
    
    
    
    
    """
    pass

def create_association_batch(Entries=None):
    """
    Associates the specified SSM document with the specified instances.
    When you associate an SSM document with an instance, the configuration agent on the instance (SSM agent for Linux and EC2Config service for Windows) processes the document and configures the instance as specified.
    If you associate a document with an instance that already has an associated document, the system throws the AssociationAlreadyExists exception.
    
    
    :example: response = client.create_association_batch(
        Entries=[
            {
                'Name': 'string',
                'InstanceId': 'string',
                'Parameters': {
                    'string': [
                        'string',
                    ]
                }
            },
        ]
    )
    
    
    :type Entries: list
    :param Entries: [REQUIRED]
            One or more associations.
            (dict) --Describes the association of an SSM document and an instance.
            Name (string) --The name of the configuration document.
            InstanceId (string) --The ID of the instance.
            Parameters (dict) --A description of the parameters for a document.
            (string) --
            (list) --
            (string) --
            
            
            

    :rtype: dict
    :return: {
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
    
    
    :returns: 
    (string) --
    (list) --
    (string) --
    
    
    
    
    
    """
    pass

def create_document(Content=None, Name=None):
    """
    Creates an SSM document.
    After you create an SSM document, you can use CreateAssociation to associate it with one or more running instances.
    
    
    :example: response = client.create_document(
        Content='string',
        Name='string'
    )
    
    
    :type Content: string
    :param Content: [REQUIRED]
            A valid JSON string.
            

    :type Name: string
    :param Name: [REQUIRED]
            A name for the SSM document.
            

    :rtype: dict
    :return: {
        'DocumentDescription': {
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
    
    
    :returns: 
    (string) --
    
    """
    pass

def delete_activation(ActivationId=None):
    """
    Deletes an activation. You are not required to delete an activation. If you delete an activation, you can no longer use it to register additional managed instances. Deleting an activation does not de-register managed instances. You must manually de-register managed instances.
    
    
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

def delete_association(Name=None, InstanceId=None):
    """
    Disassociates the specified SSM document from the specified instance.
    When you disassociate an SSM document from an instance, it does not change the configuration of the instance. To change the configuration state of an instance after you disassociate a document, you must create a new document with the desired configuration and associate it with the instance.
    
    
    :example: response = client.delete_association(
        Name='string',
        InstanceId='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the SSM document.
            

    :type InstanceId: string
    :param InstanceId: [REQUIRED]
            The ID of the instance.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_document(Name=None):
    """
    Deletes the SSM document and all instance associations to the document.
    Before you delete the SSM document, we recommend that you use DeleteAssociation to disassociate all instances that are associated with the document.
    
    
    :example: response = client.delete_document(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the SSM document.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def deregister_managed_instance(InstanceId=None):
    """
    Removes the server or virtual machine from the list of registered servers. You can reregister the instance again at any time. If you dont plan to use Run Command on the server, we suggest uninstalling the SSM agent first.
    
    
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

def describe_activations(Filters=None, MaxResults=None, NextToken=None):
    """
    Details about the activation, including: the date and time the activation was created, the expiration date, the IAM role assigned to the instances in the activation, and the number of instances activated by this registration.
    
    
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

def describe_association(Name=None, InstanceId=None):
    """
    Describes the associations for the specified SSM document or instance.
    
    
    :example: response = client.describe_association(
        Name='string',
        InstanceId='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the SSM document.
            

    :type InstanceId: string
    :param InstanceId: [REQUIRED]
            The instance ID.
            

    :rtype: dict
    :return: {
        'AssociationDescription': {
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
        }
    }
    
    
    :returns: 
    (string) --
    (list) --
    (string) --
    
    
    
    
    
    """
    pass

def describe_document(Name=None):
    """
    Describes the specified SSM document.
    
    
    :example: response = client.describe_document(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the SSM document.
            

    :rtype: dict
    :return: {
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
    
    
    """
    pass

def describe_document_permission(Name=None, PermissionType=None):
    """
    Describes the permissions for an SSM document. If you created the document, you are the owner. If a document is shared, it can either be shared privately (by specifying a users AWS account ID) or publicly (All ).
    
    
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

def describe_instance_information(InstanceInformationFilterList=None, MaxResults=None, NextToken=None):
    """
    Describes one or more of your instances. You can use this to get information about instances like the operating system platform, the SSM agent version (Linux), status etc. If you specify one or more instance IDs, it returns information for those instances. If you do not specify instance IDs, it returns information for all your instances. If you specify an instance ID that is not valid or an instance that you do not own, you receive an error.
    
    
    :example: response = client.describe_instance_information(
        InstanceInformationFilterList=[
            {
                'key': 'InstanceIds'|'AgentVersion'|'PingStatus'|'PlatformTypes'|'ActivationIds'|'IamRole'|'ResourceType',
                'valueSet': [
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
                'ComputerName': 'string'
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

def get_document(Name=None):
    """
    Gets the contents of the specified SSM document.
    
    
    :example: response = client.get_document(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the SSM document.
            

    :rtype: dict
    :return: {
        'Name': 'string',
        'Content': 'string'
    }
    
    
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

def get_waiter():
    """
    
    """
    pass

def list_associations(AssociationFilterList=None, MaxResults=None, NextToken=None):
    """
    Lists the associations for the specified SSM document or instance.
    
    
    :example: response = client.list_associations(
        AssociationFilterList=[
            {
                'key': 'InstanceId'|'Name',
                'value': 'string'
            },
        ],
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type AssociationFilterList: list
    :param AssociationFilterList: [REQUIRED]
            One or more filters. Use a filter to return a more specific list of results.
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
                'InstanceId': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_command_invocations(CommandId=None, InstanceId=None, MaxResults=None, NextToken=None, Filters=None, Details=None):
    """
    An invocation is copy of a command sent to a specific instance. A command can apply to one or more instances. A command invocation applies to one instance. For example, if a user executes SendCommand against three instances, then a command invocation is created for each requested instance ID. ListCommandInvocations provide status about command execution.
    
    
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
            key (string) -- [REQUIRED]The name of the filter. For example, requested date and time.
            value (string) -- [REQUIRED]The filter value. For example: June 30, 2015.
            
            

    :type Details: boolean
    :param Details: (Optional) If set this returns the response of the command executions and any command output. By default this is set to False.

    :rtype: dict
    :return: {
        'CommandInvocations': [
            {
                'CommandId': 'string',
                'InstanceId': 'string',
                'Comment': 'string',
                'DocumentName': 'string',
                'RequestedDateTime': datetime(2015, 1, 1),
                'Status': 'Pending'|'InProgress'|'Cancelling'|'Success'|'TimedOut'|'Cancelled'|'Failed',
                'TraceOutput': 'string',
                'CommandPlugins': [
                    {
                        'Name': 'string',
                        'Status': 'Pending'|'InProgress'|'Success'|'TimedOut'|'Cancelled'|'Failed',
                        'ResponseCode': 123,
                        'ResponseStartDateTime': datetime(2015, 1, 1),
                        'ResponseFinishDateTime': datetime(2015, 1, 1),
                        'Output': 'string',
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
    (string) --
    
    """
    pass

def list_commands(CommandId=None, InstanceId=None, MaxResults=None, NextToken=None, Filters=None):
    """
    Lists the commands requested by users of the AWS account.
    
    
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
            key (string) -- [REQUIRED]The name of the filter. For example, requested date and time.
            value (string) -- [REQUIRED]The filter value. For example: June 30, 2015.
            
            

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
                'RequestedDateTime': datetime(2015, 1, 1),
                'Status': 'Pending'|'InProgress'|'Cancelling'|'Success'|'TimedOut'|'Cancelled'|'Failed',
                'OutputS3BucketName': 'string',
                'OutputS3KeyPrefix': 'string',
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

def list_documents(DocumentFilterList=None, MaxResults=None, NextToken=None):
    """
    Describes one or more of your SSM documents.
    
    
    :example: response = client.list_documents(
        DocumentFilterList=[
            {
                'key': 'Name'|'Owner'|'PlatformTypes',
                'value': 'string'
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
                ]
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
    
    
    :example: response = client.list_tags_for_resource(
        ResourceType='ManagedInstance',
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
    Share a document publicly or privately. If you share a document privately, you must specify the AWS user account IDs for those people who can use the document. If you share a document publicly, you must specify All as the account ID.
    
    
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

def remove_tags_from_resource(ResourceType=None, ResourceId=None, TagKeys=None):
    """
    Removes all tags from the specified resource.
    
    
    :example: response = client.remove_tags_from_resource(
        ResourceType='ManagedInstance',
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

def send_command(InstanceIds=None, DocumentName=None, DocumentHash=None, DocumentHashType=None, TimeoutSeconds=None, Comment=None, Parameters=None, OutputS3BucketName=None, OutputS3KeyPrefix=None, ServiceRoleArn=None, NotificationConfig=None):
    """
    Executes commands on one or more remote instances.
    
    
    :example: response = client.send_command(
        InstanceIds=[
            'string',
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
        OutputS3BucketName='string',
        OutputS3KeyPrefix='string',
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
    :param InstanceIds: [REQUIRED]
            Required. The instance IDs where the command should execute. You can specify a maximum of 50 IDs.
            (string) --
            

    :type DocumentName: string
    :param DocumentName: [REQUIRED]
            Required. The name of the SSM document to execute. This can be an SSM public document or a custom document.
            

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
    :param Parameters: The required and optional parameters specified in the SSM document being executed.
            (string) --
            (list) --
            (string) --
            
            

    :type OutputS3BucketName: string
    :param OutputS3BucketName: The name of the S3 bucket where command execution responses should be stored.

    :type OutputS3KeyPrefix: string
    :param OutputS3KeyPrefix: The directory structure within the S3 bucket where the responses should be stored.

    :type ServiceRoleArn: string
    :param ServiceRoleArn: The IAM role that SSM uses to send notifications.

    :type NotificationConfig: dict
    :param NotificationConfig: Configurations for sending notifications.
            NotificationArn (string) --An Amazon Resource Name (ARN) for a Simple Notification Service (SNS) topic. SSM pushes notifications about command status changes to this topic.
            NotificationEvents (list) --The different events for which you can receive notifications. These events include the following: All (events), InProgress, Success, TimedOut, Cancelled, Failed. To learn more about these events, see Monitoring Commands in the Amazon Elastic Compute Cloud User Guide .
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
            'RequestedDateTime': datetime(2015, 1, 1),
            'Status': 'Pending'|'InProgress'|'Cancelling'|'Success'|'TimedOut'|'Cancelled'|'Failed',
            'OutputS3BucketName': 'string',
            'OutputS3KeyPrefix': 'string',
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

def update_association_status(Name=None, InstanceId=None, AssociationStatus=None):
    """
    Updates the status of the SSM document associated with the specified instance.
    
    
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
            The name of the SSM document.
            

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
        }
    }
    
    
    :returns: 
    (string) --
    (list) --
    (string) --
    
    
    
    
    
    """
    pass

def update_managed_instance_role(InstanceId=None, IamRole=None):
    """
    Assigns or changes an Amazon Identity and Access Management (IAM) role to the managed instance.
    
    
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

