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

def associate_fleet(FleetName=None, StackName=None):
    """
    Associate a fleet to a stack.
    See also: AWS API Documentation
    
    
    :example: response = client.associate_fleet(
        FleetName='string',
        StackName='string'
    )
    
    
    :type FleetName: string
    :param FleetName: [REQUIRED]
            The name of the fleet to associate.
            

    :type StackName: string
    :param StackName: [REQUIRED]
            The name of the stack to which the fleet is associated.
            

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

def create_fleet(Name=None, ImageName=None, InstanceType=None, ComputeCapacity=None, VpcConfig=None, MaxUserDurationInSeconds=None, DisconnectTimeoutInSeconds=None, Description=None, DisplayName=None, EnableDefaultInternetAccess=None):
    """
    Creates a new fleet.
    See also: AWS API Documentation
    
    
    :example: response = client.create_fleet(
        Name='string',
        ImageName='string',
        InstanceType='string',
        ComputeCapacity={
            'DesiredInstances': 123
        },
        VpcConfig={
            'SubnetIds': [
                'string',
            ]
        },
        MaxUserDurationInSeconds=123,
        DisconnectTimeoutInSeconds=123,
        Description='string',
        DisplayName='string',
        EnableDefaultInternetAccess=True|False
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            A unique identifier for the fleet.
            

    :type ImageName: string
    :param ImageName: [REQUIRED]
            Unique name of the image used by the fleet.
            

    :type InstanceType: string
    :param InstanceType: [REQUIRED]
            The instance type of compute resources for the fleet. Fleet instances are launched from this instance type.
            

    :type ComputeCapacity: dict
    :param ComputeCapacity: [REQUIRED]
            The parameters for the capacity allocated to the fleet.
            DesiredInstances (integer) -- [REQUIRED]The desired number of streaming instances.
            

    :type VpcConfig: dict
    :param VpcConfig: The VPC configuration for the fleet.
            SubnetIds (list) --The list of subnets to which a network interface is established from the fleet instance.
            (string) --
            

    :type MaxUserDurationInSeconds: integer
    :param MaxUserDurationInSeconds: The maximum time for which a streaming session can run. The input can be any numeric value in seconds between 600 and 57600.

    :type DisconnectTimeoutInSeconds: integer
    :param DisconnectTimeoutInSeconds: The time after disconnection when a session is considered to have ended. If a user who got disconnected reconnects within this timeout interval, the user is connected back to their previous session. The input can be any numeric value in seconds between 60 and 57600.

    :type Description: string
    :param Description: The description of the fleet.

    :type DisplayName: string
    :param DisplayName: The display name of the fleet.

    :type EnableDefaultInternetAccess: boolean
    :param EnableDefaultInternetAccess: Enables or disables default Internet access for the fleet.

    :rtype: dict
    :return: {
        'Fleet': {
            'Arn': 'string',
            'Name': 'string',
            'DisplayName': 'string',
            'Description': 'string',
            'ImageName': 'string',
            'InstanceType': 'string',
            'ComputeCapacityStatus': {
                'Desired': 123,
                'Running': 123,
                'InUse': 123,
                'Available': 123
            },
            'MaxUserDurationInSeconds': 123,
            'DisconnectTimeoutInSeconds': 123,
            'State': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED',
            'VpcConfig': {
                'SubnetIds': [
                    'string',
                ]
            },
            'CreatedTime': datetime(2015, 1, 1),
            'FleetErrors': [
                {
                    'ErrorCode': 'IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION'|'NETWORK_INTERFACE_LIMIT_EXCEEDED'|'INTERNAL_SERVICE_ERROR'|'IAM_SERVICE_ROLE_IS_MISSING'|'SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION'|'SUBNET_NOT_FOUND'|'IMAGE_NOT_FOUND'|'INVALID_SUBNET_CONFIGURATION',
                    'ErrorMessage': 'string'
                },
            ],
            'EnableDefaultInternetAccess': True|False
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_stack(Name=None, Description=None, DisplayName=None, StorageConnectors=None):
    """
    Create a new stack.
    See also: AWS API Documentation
    
    
    :example: response = client.create_stack(
        Name='string',
        Description='string',
        DisplayName='string',
        StorageConnectors=[
            {
                'ConnectorType': 'HOMEFOLDERS',
                'ResourceIdentifier': 'string'
            },
        ]
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The unique identifier for this stack.
            

    :type Description: string
    :param Description: The description displayed to end users on the AppStream 2.0 portal.

    :type DisplayName: string
    :param DisplayName: The name displayed to end users on the AppStream 2.0 portal.

    :type StorageConnectors: list
    :param StorageConnectors: The storage connectors to be enabled for the stack.
            (dict) --Contains the parameters for a storage connector.
            ConnectorType (string) -- [REQUIRED]The type of storage connector. The possible values include: HOMEFOLDERS.
            ResourceIdentifier (string) --The ARN associated with the storage connector.
            
            

    :rtype: dict
    :return: {
        'Stack': {
            'Arn': 'string',
            'Name': 'string',
            'Description': 'string',
            'DisplayName': 'string',
            'CreatedTime': datetime(2015, 1, 1),
            'StorageConnectors': [
                {
                    'ConnectorType': 'HOMEFOLDERS',
                    'ResourceIdentifier': 'string'
                },
            ],
            'StackErrors': [
                {
                    'ErrorCode': 'STORAGE_CONNECTOR_ERROR'|'INTERNAL_SERVICE_ERROR',
                    'ErrorMessage': 'string'
                },
            ]
        }
    }
    
    
    """
    pass

def create_streaming_url(StackName=None, FleetName=None, UserId=None, ApplicationId=None, Validity=None, SessionContext=None):
    """
    Creates a URL to start an AppStream 2.0 streaming session for a user. By default, the URL is valid only for 1 minute from the time that it is generated.
    See also: AWS API Documentation
    
    
    :example: response = client.create_streaming_url(
        StackName='string',
        FleetName='string',
        UserId='string',
        ApplicationId='string',
        Validity=123,
        SessionContext='string'
    )
    
    
    :type StackName: string
    :param StackName: [REQUIRED]
            The stack for which the URL is generated.
            

    :type FleetName: string
    :param FleetName: [REQUIRED]
            The fleet for which the URL is generated.
            

    :type UserId: string
    :param UserId: [REQUIRED]
            A unique user ID for whom the URL is generated.
            

    :type ApplicationId: string
    :param ApplicationId: The ID of the application that must be launched after the session starts.

    :type Validity: integer
    :param Validity: The duration up to which the URL returned by this action is valid. The input can be any numeric value in seconds between 1 and 604800 seconds.

    :type SessionContext: string
    :param SessionContext: The sessionContext of the streaming URL.

    :rtype: dict
    :return: {
        'StreamingURL': 'string',
        'Expires': datetime(2015, 1, 1)
    }
    
    
    """
    pass

def delete_fleet(Name=None):
    """
    Deletes a fleet.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_fleet(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the fleet to be deleted.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_stack(Name=None):
    """
    Deletes the stack. After this operation completes, the environment can no longer be activated, and any reservations made for the stack are released.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_stack(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the stack to delete.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def describe_fleets(Names=None, NextToken=None):
    """
    If fleet names are provided, this operation describes the specified fleets; otherwise, all the fleets in the account are described.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_fleets(
        Names=[
            'string',
        ],
        NextToken='string'
    )
    
    
    :type Names: list
    :param Names: The fleet names to describe. Use null to describe all the fleets for the AWS account.
            (string) --
            

    :type NextToken: string
    :param NextToken: The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.

    :rtype: dict
    :return: {
        'Fleets': [
            {
                'Arn': 'string',
                'Name': 'string',
                'DisplayName': 'string',
                'Description': 'string',
                'ImageName': 'string',
                'InstanceType': 'string',
                'ComputeCapacityStatus': {
                    'Desired': 123,
                    'Running': 123,
                    'InUse': 123,
                    'Available': 123
                },
                'MaxUserDurationInSeconds': 123,
                'DisconnectTimeoutInSeconds': 123,
                'State': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED',
                'VpcConfig': {
                    'SubnetIds': [
                        'string',
                    ]
                },
                'CreatedTime': datetime(2015, 1, 1),
                'FleetErrors': [
                    {
                        'ErrorCode': 'IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION'|'NETWORK_INTERFACE_LIMIT_EXCEEDED'|'INTERNAL_SERVICE_ERROR'|'IAM_SERVICE_ROLE_IS_MISSING'|'SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION'|'SUBNET_NOT_FOUND'|'IMAGE_NOT_FOUND'|'INVALID_SUBNET_CONFIGURATION',
                        'ErrorMessage': 'string'
                    },
                ],
                'EnableDefaultInternetAccess': True|False
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_images(Names=None):
    """
    Describes the images. If a list of names is not provided, all images in your account are returned. This operation does not return a paginated result.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_images(
        Names=[
            'string',
        ]
    )
    
    
    :type Names: list
    :param Names: A specific list of images to describe.
            (string) --
            

    :rtype: dict
    :return: {
        'Images': [
            {
                'Name': 'string',
                'Arn': 'string',
                'BaseImageArn': 'string',
                'DisplayName': 'string',
                'State': 'PENDING'|'AVAILABLE'|'FAILED'|'DELETING',
                'Visibility': 'PUBLIC'|'PRIVATE',
                'ImageBuilderSupported': True|False,
                'Platform': 'WINDOWS',
                'Description': 'string',
                'StateChangeReason': {
                    'Code': 'INTERNAL_ERROR'|'IMAGE_BUILDER_NOT_AVAILABLE',
                    'Message': 'string'
                },
                'Applications': [
                    {
                        'Name': 'string',
                        'DisplayName': 'string',
                        'IconURL': 'string',
                        'LaunchPath': 'string',
                        'LaunchParameters': 'string',
                        'Enabled': True|False,
                        'Metadata': {
                            'string': 'string'
                        }
                    },
                ],
                'CreatedTime': datetime(2015, 1, 1),
                'PublicBaseImageReleasedDate': datetime(2015, 1, 1)
            },
        ]
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def describe_sessions(StackName=None, FleetName=None, UserId=None, NextToken=None, Limit=None, AuthenticationType=None):
    """
    Describes the streaming sessions for a stack and a fleet. If a user ID is provided, this operation returns streaming sessions for only that user. Pass this value for the nextToken parameter in a subsequent call to this operation to retrieve the next set of items. If an authentication type is not provided, the operation defaults to users authenticated using a streaming URL.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_sessions(
        StackName='string',
        FleetName='string',
        UserId='string',
        NextToken='string',
        Limit=123,
        AuthenticationType='API'|'SAML'
    )
    
    
    :type StackName: string
    :param StackName: [REQUIRED]
            The name of the stack for which to list sessions.
            

    :type FleetName: string
    :param FleetName: [REQUIRED]
            The name of the fleet for which to list sessions.
            

    :type UserId: string
    :param UserId: The user for whom to list sessions. Use null to describe all the sessions for the stack and fleet.

    :type NextToken: string
    :param NextToken: The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.

    :type Limit: integer
    :param Limit: The size of each page of results. The default value is 20 and the maximum supported value is 50.

    :type AuthenticationType: string
    :param AuthenticationType: The authentication method of the user. It can be API for a user authenticated using a streaming URL, or SAML for a SAML federated user. If an authentication type is not provided, the operation defaults to users authenticated using a streaming URL.

    :rtype: dict
    :return: {
        'Sessions': [
            {
                'Id': 'string',
                'UserId': 'string',
                'StackName': 'string',
                'FleetName': 'string',
                'State': 'ACTIVE'|'PENDING'|'EXPIRED',
                'AuthenticationType': 'API'|'SAML'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def describe_stacks(Names=None, NextToken=None):
    """
    If stack names are not provided, this operation describes the specified stacks; otherwise, all stacks in the account are described. Pass the nextToken value in a subsequent call to this operation to retrieve the next set of items.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_stacks(
        Names=[
            'string',
        ],
        NextToken='string'
    )
    
    
    :type Names: list
    :param Names: The stack names to describe. Use null to describe all the stacks for the AWS account.
            (string) --
            

    :type NextToken: string
    :param NextToken: The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.

    :rtype: dict
    :return: {
        'Stacks': [
            {
                'Arn': 'string',
                'Name': 'string',
                'Description': 'string',
                'DisplayName': 'string',
                'CreatedTime': datetime(2015, 1, 1),
                'StorageConnectors': [
                    {
                        'ConnectorType': 'HOMEFOLDERS',
                        'ResourceIdentifier': 'string'
                    },
                ],
                'StackErrors': [
                    {
                        'ErrorCode': 'STORAGE_CONNECTOR_ERROR'|'INTERNAL_SERVICE_ERROR',
                        'ErrorMessage': 'string'
                    },
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def disassociate_fleet(FleetName=None, StackName=None):
    """
    Disassociates a fleet from a stack.
    See also: AWS API Documentation
    
    
    :example: response = client.disassociate_fleet(
        FleetName='string',
        StackName='string'
    )
    
    
    :type FleetName: string
    :param FleetName: [REQUIRED]
            The name of the fleet to disassociate.
            

    :type StackName: string
    :param StackName: [REQUIRED]
            The name of the stack with which the fleet is associated.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def expire_session(SessionId=None):
    """
    This operation immediately stops a streaming session.
    See also: AWS API Documentation
    
    
    :example: response = client.expire_session(
        SessionId='string'
    )
    
    
    :type SessionId: string
    :param SessionId: [REQUIRED]
            The unique identifier of the streaming session to be stopped.
            

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

def get_waiter():
    """
    
    """
    pass

def list_associated_fleets(StackName=None, NextToken=None):
    """
    Lists all fleets associated with the stack.
    See also: AWS API Documentation
    
    
    :example: response = client.list_associated_fleets(
        StackName='string',
        NextToken='string'
    )
    
    
    :type StackName: string
    :param StackName: [REQUIRED]
            The name of the stack whose associated fleets are listed.
            

    :type NextToken: string
    :param NextToken: The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.

    :rtype: dict
    :return: {
        'Names': [
            'string',
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_associated_stacks(FleetName=None, NextToken=None):
    """
    Lists all stacks to which the specified fleet is associated.
    See also: AWS API Documentation
    
    
    :example: response = client.list_associated_stacks(
        FleetName='string',
        NextToken='string'
    )
    
    
    :type FleetName: string
    :param FleetName: [REQUIRED]
            The name of the fleet whose associated stacks are listed.
            

    :type NextToken: string
    :param NextToken: The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.

    :rtype: dict
    :return: {
        'Names': [
            'string',
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def start_fleet(Name=None):
    """
    Starts a fleet.
    See also: AWS API Documentation
    
    
    :example: response = client.start_fleet(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the fleet to start.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def stop_fleet(Name=None):
    """
    Stops a fleet.
    See also: AWS API Documentation
    
    
    :example: response = client.stop_fleet(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the fleet to stop.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def update_fleet(ImageName=None, Name=None, InstanceType=None, ComputeCapacity=None, VpcConfig=None, MaxUserDurationInSeconds=None, DisconnectTimeoutInSeconds=None, DeleteVpcConfig=None, Description=None, DisplayName=None, EnableDefaultInternetAccess=None):
    """
    Updates an existing fleet. All the attributes except the fleet name can be updated in the STOPPED state. When a fleet is in the RUNNING state, only DisplayName and ComputeCapacity can be updated. A fleet cannot be updated in a status of STARTING or STOPPING .
    See also: AWS API Documentation
    
    
    :example: response = client.update_fleet(
        ImageName='string',
        Name='string',
        InstanceType='string',
        ComputeCapacity={
            'DesiredInstances': 123
        },
        VpcConfig={
            'SubnetIds': [
                'string',
            ]
        },
        MaxUserDurationInSeconds=123,
        DisconnectTimeoutInSeconds=123,
        DeleteVpcConfig=True|False,
        Description='string',
        DisplayName='string',
        EnableDefaultInternetAccess=True|False
    )
    
    
    :type ImageName: string
    :param ImageName: The image name from which a fleet is created.

    :type Name: string
    :param Name: [REQUIRED]
            The name of the fleet.
            

    :type InstanceType: string
    :param InstanceType: The instance type of compute resources for the fleet. Fleet instances are launched from this instance type.

    :type ComputeCapacity: dict
    :param ComputeCapacity: The parameters for the capacity allocated to the fleet.
            DesiredInstances (integer) -- [REQUIRED]The desired number of streaming instances.
            

    :type VpcConfig: dict
    :param VpcConfig: The VPC configuration for the fleet.
            SubnetIds (list) --The list of subnets to which a network interface is established from the fleet instance.
            (string) --
            

    :type MaxUserDurationInSeconds: integer
    :param MaxUserDurationInSeconds: The maximum time for which a streaming session can run. The input can be any numeric value in seconds between 600 and 57600.

    :type DisconnectTimeoutInSeconds: integer
    :param DisconnectTimeoutInSeconds: The time after disconnection when a session is considered to have ended. If a user who got disconnected reconnects within this timeout interval, the user is connected back to their previous session. The input can be any numeric value in seconds between 60 and 57600.

    :type DeleteVpcConfig: boolean
    :param DeleteVpcConfig: Delete the VPC association for the specified fleet.

    :type Description: string
    :param Description: The description displayed to end users on the AppStream 2.0 portal.

    :type DisplayName: string
    :param DisplayName: The name displayed to end users on the AppStream 2.0 portal.

    :type EnableDefaultInternetAccess: boolean
    :param EnableDefaultInternetAccess: Enables or disables default Internet access for the fleet.

    :rtype: dict
    :return: {
        'Fleet': {
            'Arn': 'string',
            'Name': 'string',
            'DisplayName': 'string',
            'Description': 'string',
            'ImageName': 'string',
            'InstanceType': 'string',
            'ComputeCapacityStatus': {
                'Desired': 123,
                'Running': 123,
                'InUse': 123,
                'Available': 123
            },
            'MaxUserDurationInSeconds': 123,
            'DisconnectTimeoutInSeconds': 123,
            'State': 'STARTING'|'RUNNING'|'STOPPING'|'STOPPED',
            'VpcConfig': {
                'SubnetIds': [
                    'string',
                ]
            },
            'CreatedTime': datetime(2015, 1, 1),
            'FleetErrors': [
                {
                    'ErrorCode': 'IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION'|'IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION'|'NETWORK_INTERFACE_LIMIT_EXCEEDED'|'INTERNAL_SERVICE_ERROR'|'IAM_SERVICE_ROLE_IS_MISSING'|'SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES'|'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION'|'SUBNET_NOT_FOUND'|'IMAGE_NOT_FOUND'|'INVALID_SUBNET_CONFIGURATION',
                    'ErrorMessage': 'string'
                },
            ],
            'EnableDefaultInternetAccess': True|False
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def update_stack(DisplayName=None, Description=None, Name=None, StorageConnectors=None, DeleteStorageConnectors=None):
    """
    Updates the specified fields in the stack with the specified name.
    See also: AWS API Documentation
    
    
    :example: response = client.update_stack(
        DisplayName='string',
        Description='string',
        Name='string',
        StorageConnectors=[
            {
                'ConnectorType': 'HOMEFOLDERS',
                'ResourceIdentifier': 'string'
            },
        ],
        DeleteStorageConnectors=True|False
    )
    
    
    :type DisplayName: string
    :param DisplayName: The name displayed to end users on the AppStream 2.0 portal.

    :type Description: string
    :param Description: The description displayed to end users on the AppStream 2.0 portal.

    :type Name: string
    :param Name: [REQUIRED]
            The name of the stack to update.
            

    :type StorageConnectors: list
    :param StorageConnectors: The storage connectors to be enabled for the stack.
            (dict) --Contains the parameters for a storage connector.
            ConnectorType (string) -- [REQUIRED]The type of storage connector. The possible values include: HOMEFOLDERS.
            ResourceIdentifier (string) --The ARN associated with the storage connector.
            
            

    :type DeleteStorageConnectors: boolean
    :param DeleteStorageConnectors: Remove all the storage connectors currently enabled for the stack.

    :rtype: dict
    :return: {
        'Stack': {
            'Arn': 'string',
            'Name': 'string',
            'Description': 'string',
            'DisplayName': 'string',
            'CreatedTime': datetime(2015, 1, 1),
            'StorageConnectors': [
                {
                    'ConnectorType': 'HOMEFOLDERS',
                    'ResourceIdentifier': 'string'
                },
            ],
            'StackErrors': [
                {
                    'ErrorCode': 'STORAGE_CONNECTOR_ERROR'|'INTERNAL_SERVICE_ERROR',
                    'ErrorMessage': 'string'
                },
            ]
        }
    }
    
    
    """
    pass

