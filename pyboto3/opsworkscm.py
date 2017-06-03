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

def associate_node(ServerName=None, NodeName=None, EngineAttributes=None):
    """
    Associates a new node with the Chef server. This command is an alternative to knife bootstrap . For more information about how to disassociate a node, see  DisassociateNode .
    A node can can only be associated with servers that are in a HEALTHY state. Otherwise, an InvalidStateException is thrown. A ResourceNotFoundException is thrown when the server does not exist. A ValidationException is raised when parameters of the request are not valid. The AssociateNode API call can be integrated into Auto Scaling configurations, AWS Cloudformation templates, or the user data of a server's instance.
    Example: aws opsworks-cm associate-node --server-name *MyServer* --node-name *MyManagedNode* --engine-attributes "Name=*MyOrganization* ,Value=default" "Name=*Chef_node_public_key* ,Value=*Public_key_contents* "
    See also: AWS API Documentation
    
    
    :example: response = client.associate_node(
        ServerName='string',
        NodeName='string',
        EngineAttributes=[
            {
                'Name': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ServerName: string
    :param ServerName: [REQUIRED]
            The name of the server with which to associate the node.
            

    :type NodeName: string
    :param NodeName: [REQUIRED]
            The name of the Chef client node.
            

    :type EngineAttributes: list
    :param EngineAttributes: [REQUIRED]
            Engine attributes used for associating the node.
            Attributes accepted in a AssociateNode request:
            CHEF_ORGANIZATION : The Chef organization with which the node is associated. By default only one organization named default can exist.
            CHEF_NODE_PUBLIC_KEY : A PEM-formatted public key. This key is required for the chef-client agent to access the Chef API.
            (dict) --A name and value pair that is specific to the engine of the server.
            Name (string) --The name of the engine attribute.
            Value (string) --The value of the engine attribute.
            
            

    :rtype: dict
    :return: {
        'NodeAssociationStatusToken': 'string'
    }
    
    
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

def create_backup(ServerName=None, Description=None):
    """
    Creates an application-level backup of a server. While the server is in the BACKING_UP state, the server cannot be changed, and no additional backup can be created.
    Backups can be created for servers in RUNNING , HEALTHY , and UNHEALTHY states. By default, you can create a maximum of 50 manual backups.
    This operation is asynchronous.
    A LimitExceededException is thrown when the maximum number of manual backups is reached. An InvalidStateException is thrown when the server is not in any of the following states: RUNNING, HEALTHY, or UNHEALTHY. A ResourceNotFoundException is thrown when the server is not found. A ValidationException is thrown when parameters of the request are not valid.
    See also: AWS API Documentation
    
    
    :example: response = client.create_backup(
        ServerName='string',
        Description='string'
    )
    
    
    :type ServerName: string
    :param ServerName: [REQUIRED]
            The name of the server that you want to back up.
            

    :type Description: string
    :param Description: A user-defined description of the backup.

    :rtype: dict
    :return: {
        'Backup': {
            'BackupArn': 'string',
            'BackupId': 'string',
            'BackupType': 'AUTOMATED'|'MANUAL',
            'CreatedAt': datetime(2015, 1, 1),
            'Description': 'string',
            'Engine': 'string',
            'EngineModel': 'string',
            'EngineVersion': 'string',
            'InstanceProfileArn': 'string',
            'InstanceType': 'string',
            'KeyPair': 'string',
            'PreferredBackupWindow': 'string',
            'PreferredMaintenanceWindow': 'string',
            'S3DataSize': 123,
            'S3DataUrl': 'string',
            'S3LogUrl': 'string',
            'SecurityGroupIds': [
                'string',
            ],
            'ServerName': 'string',
            'ServiceRoleArn': 'string',
            'Status': 'IN_PROGRESS'|'OK'|'FAILED'|'DELETING',
            'StatusDescription': 'string',
            'SubnetIds': [
                'string',
            ],
            'ToolsVersion': 'string',
            'UserArn': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_server(AssociatePublicIpAddress=None, DisableAutomatedBackup=None, Engine=None, EngineModel=None, EngineVersion=None, EngineAttributes=None, BackupRetentionCount=None, ServerName=None, InstanceProfileArn=None, InstanceType=None, KeyPair=None, PreferredMaintenanceWindow=None, PreferredBackupWindow=None, SecurityGroupIds=None, ServiceRoleArn=None, SubnetIds=None, BackupId=None):
    """
    Creates and immedately starts a new server. The server is ready to use when it is in the HEALTHY state. By default, you can create a maximum of 10 servers.
    This operation is asynchronous.
    A LimitExceededException is thrown when you have created the maximum number of servers (10). A ResourceAlreadyExistsException is thrown when a server with the same name already exists in the account. A ResourceNotFoundException is thrown when you specify a backup ID that is not valid or is for a backup that does not exist. A ValidationException is thrown when parameters of the request are not valid.
    If you do not specify a security group by adding the SecurityGroupIds parameter, AWS OpsWorks creates a new security group. The default security group opens the Chef server to the world on TCP port 443. If a KeyName is present, AWS OpsWorks enables SSH access. SSH is also open to the world on TCP port 22.
    By default, the Chef Server is accessible from any IP address. We recommend that you update your security group rules to allow access from known IP addresses and address ranges only. To edit security group rules, open Security Groups in the navigation pane of the EC2 management console.
    See also: AWS API Documentation
    
    
    :example: response = client.create_server(
        AssociatePublicIpAddress=True|False,
        DisableAutomatedBackup=True|False,
        Engine='string',
        EngineModel='string',
        EngineVersion='string',
        EngineAttributes=[
            {
                'Name': 'string',
                'Value': 'string'
            },
        ],
        BackupRetentionCount=123,
        ServerName='string',
        InstanceProfileArn='string',
        InstanceType='string',
        KeyPair='string',
        PreferredMaintenanceWindow='string',
        PreferredBackupWindow='string',
        SecurityGroupIds=[
            'string',
        ],
        ServiceRoleArn='string',
        SubnetIds=[
            'string',
        ],
        BackupId='string'
    )
    
    
    :type AssociatePublicIpAddress: boolean
    :param AssociatePublicIpAddress: Associate a public IP address with a server that you are launching. Valid values are true or false . The default value is true .

    :type DisableAutomatedBackup: boolean
    :param DisableAutomatedBackup: Enable or disable scheduled backups. Valid values are true or false . The default value is true .

    :type Engine: string
    :param Engine: The configuration management engine to use. Valid values include Chef .

    :type EngineModel: string
    :param EngineModel: The engine model, or option. Valid values include Single .

    :type EngineVersion: string
    :param EngineVersion: The major release version of the engine that you want to use. Values depend on the engine that you choose.

    :type EngineAttributes: list
    :param EngineAttributes: Optional engine attributes on a specified server.
            Attributes accepted in a createServer request:
            CHEF_PIVOTAL_KEY : A base64-encoded RSA private key that is not stored by AWS OpsWorks for Chef. This private key is required to access the Chef API. When no CHEF_PIVOTAL_KEY is set, one is generated and returned in the response.
            CHEF_DELIVERY_ADMIN_PASSWORD : The password for the administrative user in the Chef Automate GUI. The password length is a minimum of eight characters, and a maximum of 32. The password can contain letters, numbers, and special characters (!/@#$%^+=_). The password must contain at least one lower case letter, one upper case letter, one number, and one special character. When no CHEF_DELIVERY_ADMIN_PASSWORD is set, one is generated and returned in the response.
            (dict) --A name and value pair that is specific to the engine of the server.
            Name (string) --The name of the engine attribute.
            Value (string) --The value of the engine attribute.
            
            

    :type BackupRetentionCount: integer
    :param BackupRetentionCount: The number of automated backups that you want to keep. Whenever a new backup is created, AWS OpsWorks for Chef Automate deletes the oldest backups if this number is exceeded. The default value is 1 .

    :type ServerName: string
    :param ServerName: [REQUIRED]
            The name of the server. The server name must be unique within your AWS account, within each region. Server names must start with a letter; then letters, numbers, or hyphens (-) are allowed, up to a maximum of 40 characters.
            

    :type InstanceProfileArn: string
    :param InstanceProfileArn: [REQUIRED]
            The ARN of the instance profile that your Amazon EC2 instances use. Although the AWS OpsWorks console typically creates the instance profile for you, if you are using API commands instead, run the service-role-creation.yaml AWS CloudFormation template, located at https://s3.amazonaws.com/opsworks-cm-us-east-1-prod-default-assets/misc/opsworks-cm-roles.yaml. This template creates a CloudFormation stack that includes the instance profile you need.
            

    :type InstanceType: string
    :param InstanceType: [REQUIRED]
            The Amazon EC2 instance type to use. Valid values must be specified in the following format: ^([cm][34]|t2).* For example, m4.large . Valid values are t2.medium , m4.large , or m4.2xlarge .
            

    :type KeyPair: string
    :param KeyPair: The Amazon EC2 key pair to set for the instance. This parameter is optional; if desired, you may specify this parameter to connect to your instances by using SSH.

    :type PreferredMaintenanceWindow: string
    :param PreferredMaintenanceWindow: The start time for a one-hour period each week during which AWS OpsWorks for Chef Automate performs maintenance on the instance. Valid values must be specified in the following format: DDD:HH:MM . The specified time is in coordinated universal time (UTC). The default value is a random one-hour period on Tuesday, Wednesday, or Friday. See TimeWindowDefinition for more information.
            Example: Mon:08:00 , which represents a start time of every Monday at 08:00 UTC. (8:00 a.m.)
            

    :type PreferredBackupWindow: string
    :param PreferredBackupWindow: The start time for a one-hour period during which AWS OpsWorks for Chef Automate backs up application-level data on your server if automated backups are enabled. Valid values must be specified in one of the following formats:
            HH:MM for daily backups
            DDD:HH:MM for weekly backups
            The specified time is in coordinated universal time (UTC). The default value is a random, daily start time.
            Example: 08:00 , which represents a daily start time of 08:00 UTC.Example: Mon:08:00 , which represents a start time of every Monday at 08:00 UTC. (8:00 a.m.)
            

    :type SecurityGroupIds: list
    :param SecurityGroupIds: A list of security group IDs to attach to the Amazon EC2 instance. If you add this parameter, the specified security groups must be within the VPC that is specified by SubnetIds .
            If you do not specify this parameter, AWS OpsWorks for Chef Automate creates one new security group that uses TCP ports 22 and 443, open to 0.0.0.0/0 (everyone).
            (string) --
            

    :type ServiceRoleArn: string
    :param ServiceRoleArn: [REQUIRED]
            The service role that the AWS OpsWorks for Chef Automate service backend uses to work with your account. Although the AWS OpsWorks management console typically creates the service role for you, if you are using the AWS CLI or API commands, run the service-role-creation.yaml AWS CloudFormation template, located at https://s3.amazonaws.com/opsworks-stuff/latest/service-role-creation.yaml. This template creates a CloudFormation stack that includes the service role that you need.
            

    :type SubnetIds: list
    :param SubnetIds: The IDs of subnets in which to launch the server EC2 instance.
            Amazon EC2-Classic customers: This field is required. All servers must run within a VPC. The VPC must have 'Auto Assign Public IP' enabled.
            EC2-VPC customers: This field is optional. If you do not specify subnet IDs, your EC2 instances are created in a default subnet that is selected by Amazon EC2. If you specify subnet IDs, the VPC must have 'Auto Assign Public IP' enabled.
            For more information about supported Amazon EC2 platforms, see Supported Platforms .
            (string) --
            

    :type BackupId: string
    :param BackupId: If you specify this field, AWS OpsWorks for Chef Automate creates the server by using the backup represented by BackupId.

    :rtype: dict
    :return: {
        'Server': {
            'AssociatePublicIpAddress': True|False,
            'BackupRetentionCount': 123,
            'ServerName': 'string',
            'CreatedAt': datetime(2015, 1, 1),
            'CloudFormationStackArn': 'string',
            'DisableAutomatedBackup': True|False,
            'Endpoint': 'string',
            'Engine': 'string',
            'EngineModel': 'string',
            'EngineAttributes': [
                {
                    'Name': 'string',
                    'Value': 'string'
                },
            ],
            'EngineVersion': 'string',
            'InstanceProfileArn': 'string',
            'InstanceType': 'string',
            'KeyPair': 'string',
            'MaintenanceStatus': 'SUCCESS'|'FAILED',
            'PreferredMaintenanceWindow': 'string',
            'PreferredBackupWindow': 'string',
            'SecurityGroupIds': [
                'string',
            ],
            'ServiceRoleArn': 'string',
            'Status': 'BACKING_UP'|'CONNECTION_LOST'|'CREATING'|'DELETING'|'MODIFYING'|'FAILED'|'HEALTHY'|'RUNNING'|'RESTORING'|'SETUP'|'UNDER_MAINTENANCE'|'UNHEALTHY'|'TERMINATED',
            'StatusReason': 'string',
            'SubnetIds': [
                'string',
            ],
            'ServerArn': 'string'
        }
    }
    
    
    :returns: 
    CHEF_PIVOTAL_KEY : A base64-encoded RSA private key that is generated by AWS OpsWorks for Chef Automate. This private key is required to access the Chef API.
    CHEF_STARTER_KIT : A base64-encoded ZIP file. The ZIP file contains a Chef starter kit, which includes a README, a configuration file, and the required RSA private key. Save this file, unzip it, and then change to the directory where you've unzipped the file contents. From this directory, you can run Knife commands.
    
    """
    pass

def delete_backup(BackupId=None):
    """
    Deletes a backup. You can delete both manual and automated backups. This operation is asynchronous.
    An InvalidStateException is thrown when a backup deletion is already in progress. A ResourceNotFoundException is thrown when the backup does not exist. A ValidationException is thrown when parameters of the request are not valid.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_backup(
        BackupId='string'
    )
    
    
    :type BackupId: string
    :param BackupId: [REQUIRED]
            The ID of the backup to delete. Run the DescribeBackups command to get a list of backup IDs. Backup IDs are in the format ServerName-yyyyMMddHHmmssSSS .
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_server(ServerName=None):
    """
    Deletes the server and the underlying AWS CloudFormation stack (including the server's EC2 instance). When you run this command, the server state is updated to DELETING . After the server is deleted, it is no longer returned by DescribeServer requests. If the AWS CloudFormation stack cannot be deleted, the server cannot be deleted.
    This operation is asynchronous.
    An InvalidStateException is thrown when a server deletion is already in progress. A ResourceNotFoundException is thrown when the server does not exist. A ValidationException is raised when parameters of the request are not valid.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_server(
        ServerName='string'
    )
    
    
    :type ServerName: string
    :param ServerName: [REQUIRED]
            The ID of the server to delete.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def describe_account_attributes():
    """
    Describes your account attributes, and creates requests to increase limits before they are reached or exceeded.
    This operation is synchronous.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_account_attributes()
    
    
    :rtype: dict
    :return: {
        'Attributes': [
            {
                'Name': 'string',
                'Maximum': 123,
                'Used': 123
            },
        ]
    }
    
    
    """
    pass

def describe_backups(BackupId=None, ServerName=None, NextToken=None, MaxResults=None):
    """
    Describes backups. The results are ordered by time, with newest backups first. If you do not specify a BackupId or ServerName, the command returns all backups.
    This operation is synchronous.
    A ResourceNotFoundException is thrown when the backup does not exist. A ValidationException is raised when parameters of the request are not valid.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_backups(
        BackupId='string',
        ServerName='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type BackupId: string
    :param BackupId: Describes a single backup.

    :type ServerName: string
    :param ServerName: Returns backups for the server with the specified ServerName.

    :type NextToken: string
    :param NextToken: NextToken is a string that is returned in some command responses. It indicates that not all entries have been returned, and that you must run at least one more request to get remaining items. To get remaining results, call DescribeBackups again, and assign the token from the previous results as the value of the nextToken parameter. If there are no more results, the response object's nextToken parameter value is null . Setting a nextToken value that was not returned in your previous results causes an InvalidNextTokenException to occur.

    :type MaxResults: integer
    :param MaxResults: To receive a paginated response, use this parameter to specify the maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a NextToken value that you can assign to the NextToken request parameter to get the next set of results.

    :rtype: dict
    :return: {
        'Backups': [
            {
                'BackupArn': 'string',
                'BackupId': 'string',
                'BackupType': 'AUTOMATED'|'MANUAL',
                'CreatedAt': datetime(2015, 1, 1),
                'Description': 'string',
                'Engine': 'string',
                'EngineModel': 'string',
                'EngineVersion': 'string',
                'InstanceProfileArn': 'string',
                'InstanceType': 'string',
                'KeyPair': 'string',
                'PreferredBackupWindow': 'string',
                'PreferredMaintenanceWindow': 'string',
                'S3DataSize': 123,
                'S3DataUrl': 'string',
                'S3LogUrl': 'string',
                'SecurityGroupIds': [
                    'string',
                ],
                'ServerName': 'string',
                'ServiceRoleArn': 'string',
                'Status': 'IN_PROGRESS'|'OK'|'FAILED'|'DELETING',
                'StatusDescription': 'string',
                'SubnetIds': [
                    'string',
                ],
                'ToolsVersion': 'string',
                'UserArn': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_events(ServerName=None, NextToken=None, MaxResults=None):
    """
    Describes events for a specified server. Results are ordered by time, with newest events first.
    This operation is synchronous.
    A ResourceNotFoundException is thrown when the server does not exist. A ValidationException is raised when parameters of the request are not valid.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_events(
        ServerName='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type ServerName: string
    :param ServerName: [REQUIRED]
            The name of the server for which you want to view events.
            

    :type NextToken: string
    :param NextToken: NextToken is a string that is returned in some command responses. It indicates that not all entries have been returned, and that you must run at least one more request to get remaining items. To get remaining results, call DescribeEvents again, and assign the token from the previous results as the value of the nextToken parameter. If there are no more results, the response object's nextToken parameter value is null . Setting a nextToken value that was not returned in your previous results causes an InvalidNextTokenException to occur.

    :type MaxResults: integer
    :param MaxResults: To receive a paginated response, use this parameter to specify the maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a NextToken value that you can assign to the NextToken request parameter to get the next set of results.

    :rtype: dict
    :return: {
        'ServerEvents': [
            {
                'CreatedAt': datetime(2015, 1, 1),
                'ServerName': 'string',
                'Message': 'string',
                'LogUrl': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def describe_node_association_status(NodeAssociationStatusToken=None, ServerName=None):
    """
    Returns the current status of an existing association or disassociation request.
    A ResourceNotFoundException is thrown when no recent association or disassociation request with the specified token is found, or when the server does not exist. A ValidationException is raised when parameters of the request are not valid.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_node_association_status(
        NodeAssociationStatusToken='string',
        ServerName='string'
    )
    
    
    :type NodeAssociationStatusToken: string
    :param NodeAssociationStatusToken: [REQUIRED]

    :type ServerName: string
    :param ServerName: [REQUIRED]
            The name of the server from which to disassociate the node.
            

    :rtype: dict
    :return: {
        'NodeAssociationStatus': 'SUCCESS'|'FAILED'|'IN_PROGRESS'
    }
    
    
    :returns: 
    SUCCESS : The association or disassociation succeeded.
    FAILED : The association or disassociation failed.
    IN_PROGRESS : The association or disassociation is still in progress.
    
    """
    pass

def describe_servers(ServerName=None, NextToken=None, MaxResults=None):
    """
    Lists all configuration management servers that are identified with your account. Only the stored results from Amazon DynamoDB are returned. AWS OpsWorks for Chef Automate does not query other services.
    This operation is synchronous.
    A ResourceNotFoundException is thrown when the server does not exist. A ValidationException is raised when parameters of the request are not valid.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_servers(
        ServerName='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type ServerName: string
    :param ServerName: Describes the server with the specified ServerName.

    :type NextToken: string
    :param NextToken: NextToken is a string that is returned in some command responses. It indicates that not all entries have been returned, and that you must run at least one more request to get remaining items. To get remaining results, call DescribeServers again, and assign the token from the previous results as the value of the nextToken parameter. If there are no more results, the response object's nextToken parameter value is null . Setting a nextToken value that was not returned in your previous results causes an InvalidNextTokenException to occur.

    :type MaxResults: integer
    :param MaxResults: To receive a paginated response, use this parameter to specify the maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a NextToken value that you can assign to the NextToken request parameter to get the next set of results.

    :rtype: dict
    :return: {
        'Servers': [
            {
                'AssociatePublicIpAddress': True|False,
                'BackupRetentionCount': 123,
                'ServerName': 'string',
                'CreatedAt': datetime(2015, 1, 1),
                'CloudFormationStackArn': 'string',
                'DisableAutomatedBackup': True|False,
                'Endpoint': 'string',
                'Engine': 'string',
                'EngineModel': 'string',
                'EngineAttributes': [
                    {
                        'Name': 'string',
                        'Value': 'string'
                    },
                ],
                'EngineVersion': 'string',
                'InstanceProfileArn': 'string',
                'InstanceType': 'string',
                'KeyPair': 'string',
                'MaintenanceStatus': 'SUCCESS'|'FAILED',
                'PreferredMaintenanceWindow': 'string',
                'PreferredBackupWindow': 'string',
                'SecurityGroupIds': [
                    'string',
                ],
                'ServiceRoleArn': 'string',
                'Status': 'BACKING_UP'|'CONNECTION_LOST'|'CREATING'|'DELETING'|'MODIFYING'|'FAILED'|'HEALTHY'|'RUNNING'|'RESTORING'|'SETUP'|'UNDER_MAINTENANCE'|'UNHEALTHY'|'TERMINATED',
                'StatusReason': 'string',
                'SubnetIds': [
                    'string',
                ],
                'ServerArn': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    CHEF_PIVOTAL_KEY : A base64-encoded RSA private key that is generated by AWS OpsWorks for Chef Automate. This private key is required to access the Chef API.
    CHEF_STARTER_KIT : A base64-encoded ZIP file. The ZIP file contains a Chef starter kit, which includes a README, a configuration file, and the required RSA private key. Save this file, unzip it, and then change to the directory where you've unzipped the file contents. From this directory, you can run Knife commands.
    
    """
    pass

def disassociate_node(ServerName=None, NodeName=None, EngineAttributes=None):
    """
    Disassociates a node from a Chef server, and removes the node from the Chef server's managed nodes. After a node is disassociated, the node key pair is no longer valid for accessing the Chef API. For more information about how to associate a node, see  AssociateNode .
    A node can can only be disassociated from a server that is in a HEALTHY state. Otherwise, an InvalidStateException is thrown. A ResourceNotFoundException is thrown when the server does not exist. A ValidationException is raised when parameters of the request are not valid.
    See also: AWS API Documentation
    
    
    :example: response = client.disassociate_node(
        ServerName='string',
        NodeName='string',
        EngineAttributes=[
            {
                'Name': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ServerName: string
    :param ServerName: [REQUIRED]
            The name of the server from which to disassociate the node.
            

    :type NodeName: string
    :param NodeName: [REQUIRED]
            The name of the Chef client node.
            

    :type EngineAttributes: list
    :param EngineAttributes: Engine attributes used for disassociating the node.
            Attributes accepted in a DisassociateNode request:
            CHEF_ORGANIZATION : The Chef organization with which the node was associated. By default only one organization named default can exist.
            (dict) --A name and value pair that is specific to the engine of the server.
            Name (string) --The name of the engine attribute.
            Value (string) --The value of the engine attribute.
            
            

    :rtype: dict
    :return: {
        'NodeAssociationStatusToken': 'string'
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

def restore_server(BackupId=None, ServerName=None, InstanceType=None, KeyPair=None):
    """
    Restores a backup to a server that is in a CONNECTION_LOST , HEALTHY , RUNNING , UNHEALTHY , or TERMINATED state. When you run RestoreServer, the server's EC2 instance is deleted, and a new EC2 instance is configured. RestoreServer maintains the existing server endpoint, so configuration management of the server's client devices (nodes) should continue to work.
    This operation is asynchronous.
    An InvalidStateException is thrown when the server is not in a valid state. A ResourceNotFoundException is thrown when the server does not exist. A ValidationException is raised when parameters of the request are not valid.
    See also: AWS API Documentation
    
    
    :example: response = client.restore_server(
        BackupId='string',
        ServerName='string',
        InstanceType='string',
        KeyPair='string'
    )
    
    
    :type BackupId: string
    :param BackupId: [REQUIRED]
            The ID of the backup that you want to use to restore a server.
            

    :type ServerName: string
    :param ServerName: [REQUIRED]
            The name of the server that you want to restore.
            

    :type InstanceType: string
    :param InstanceType: The type of the instance to create. Valid values must be specified in the following format: ^([cm][34]|t2).* For example, m4.large . Valid values are t2.medium , m4.large , and m4.2xlarge . If you do not specify this parameter, RestoreServer uses the instance type from the specified backup.

    :type KeyPair: string
    :param KeyPair: The name of the key pair to set on the new EC2 instance. This can be helpful if the administrator no longer has the SSH key.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def start_maintenance(ServerName=None):
    """
    Manually starts server maintenance. This command can be useful if an earlier maintenance attempt failed, and the underlying cause of maintenance failure has been resolved. The server is in an UNDER_MAINTENANCE state while maintenance is in progress.
    Maintenance can only be started on servers in HEALTHY and UNHEALTHY states. Otherwise, an InvalidStateException is thrown. A ResourceNotFoundException is thrown when the server does not exist. A ValidationException is raised when parameters of the request are not valid.
    See also: AWS API Documentation
    
    
    :example: response = client.start_maintenance(
        ServerName='string'
    )
    
    
    :type ServerName: string
    :param ServerName: [REQUIRED]
            The name of the server on which to run maintenance.
            

    :rtype: dict
    :return: {
        'Server': {
            'AssociatePublicIpAddress': True|False,
            'BackupRetentionCount': 123,
            'ServerName': 'string',
            'CreatedAt': datetime(2015, 1, 1),
            'CloudFormationStackArn': 'string',
            'DisableAutomatedBackup': True|False,
            'Endpoint': 'string',
            'Engine': 'string',
            'EngineModel': 'string',
            'EngineAttributes': [
                {
                    'Name': 'string',
                    'Value': 'string'
                },
            ],
            'EngineVersion': 'string',
            'InstanceProfileArn': 'string',
            'InstanceType': 'string',
            'KeyPair': 'string',
            'MaintenanceStatus': 'SUCCESS'|'FAILED',
            'PreferredMaintenanceWindow': 'string',
            'PreferredBackupWindow': 'string',
            'SecurityGroupIds': [
                'string',
            ],
            'ServiceRoleArn': 'string',
            'Status': 'BACKING_UP'|'CONNECTION_LOST'|'CREATING'|'DELETING'|'MODIFYING'|'FAILED'|'HEALTHY'|'RUNNING'|'RESTORING'|'SETUP'|'UNDER_MAINTENANCE'|'UNHEALTHY'|'TERMINATED',
            'StatusReason': 'string',
            'SubnetIds': [
                'string',
            ],
            'ServerArn': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def update_server(DisableAutomatedBackup=None, BackupRetentionCount=None, ServerName=None, PreferredMaintenanceWindow=None, PreferredBackupWindow=None):
    """
    Updates settings for a server.
    This operation is synchronous.
    See also: AWS API Documentation
    
    
    :example: response = client.update_server(
        DisableAutomatedBackup=True|False,
        BackupRetentionCount=123,
        ServerName='string',
        PreferredMaintenanceWindow='string',
        PreferredBackupWindow='string'
    )
    
    
    :type DisableAutomatedBackup: boolean
    :param DisableAutomatedBackup: Setting DisableAutomatedBackup to true disables automated or scheduled backups. Automated backups are enabled by default.

    :type BackupRetentionCount: integer
    :param BackupRetentionCount: Sets the number of automated backups that you want to keep.

    :type ServerName: string
    :param ServerName: [REQUIRED]
            The name of the server to update.
            

    :type PreferredMaintenanceWindow: string
    :param PreferredMaintenanceWindow: 
            DDD:HH:MM (weekly start time) or HH:MM (daily start time).
            Time windows always use coordinated universal time (UTC). Valid strings for day of week (DDD ) are: Mon , Tue , Wed , Thr , Fri , Sat , or Sun .
            

    :type PreferredBackupWindow: string
    :param PreferredBackupWindow: 
            DDD:HH:MM (weekly start time) or HH:MM (daily start time).
            Time windows always use coordinated universal time (UTC). Valid strings for day of week (DDD ) are: Mon , Tue , Wed , Thr , Fri , Sat , or Sun .
            

    :rtype: dict
    :return: {
        'Server': {
            'AssociatePublicIpAddress': True|False,
            'BackupRetentionCount': 123,
            'ServerName': 'string',
            'CreatedAt': datetime(2015, 1, 1),
            'CloudFormationStackArn': 'string',
            'DisableAutomatedBackup': True|False,
            'Endpoint': 'string',
            'Engine': 'string',
            'EngineModel': 'string',
            'EngineAttributes': [
                {
                    'Name': 'string',
                    'Value': 'string'
                },
            ],
            'EngineVersion': 'string',
            'InstanceProfileArn': 'string',
            'InstanceType': 'string',
            'KeyPair': 'string',
            'MaintenanceStatus': 'SUCCESS'|'FAILED',
            'PreferredMaintenanceWindow': 'string',
            'PreferredBackupWindow': 'string',
            'SecurityGroupIds': [
                'string',
            ],
            'ServiceRoleArn': 'string',
            'Status': 'BACKING_UP'|'CONNECTION_LOST'|'CREATING'|'DELETING'|'MODIFYING'|'FAILED'|'HEALTHY'|'RUNNING'|'RESTORING'|'SETUP'|'UNDER_MAINTENANCE'|'UNHEALTHY'|'TERMINATED',
            'StatusReason': 'string',
            'SubnetIds': [
                'string',
            ],
            'ServerArn': 'string'
        }
    }
    
    
    :returns: 
    CHEF_PIVOTAL_KEY : A base64-encoded RSA private key that is generated by AWS OpsWorks for Chef Automate. This private key is required to access the Chef API.
    CHEF_STARTER_KIT : A base64-encoded ZIP file. The ZIP file contains a Chef starter kit, which includes a README, a configuration file, and the required RSA private key. Save this file, unzip it, and then change to the directory where you've unzipped the file contents. From this directory, you can run Knife commands.
    
    """
    pass

def update_server_engine_attributes(ServerName=None, AttributeName=None, AttributeValue=None):
    """
    Updates engine-specific attributes on a specified server. The server enters the MODIFYING state when this operation is in progress. Only one update can occur at a time. You can use this command to reset the Chef server's private key (CHEF_PIVOTAL_KEY ).
    This operation is asynchronous.
    This operation can only be called for servers in HEALTHY or UNHEALTHY states. Otherwise, an InvalidStateException is raised. A ResourceNotFoundException is thrown when the server does not exist. A ValidationException is raised when parameters of the request are not valid.
    See also: AWS API Documentation
    
    
    :example: response = client.update_server_engine_attributes(
        ServerName='string',
        AttributeName='string',
        AttributeValue='string'
    )
    
    
    :type ServerName: string
    :param ServerName: [REQUIRED]
            The name of the server to update.
            

    :type AttributeName: string
    :param AttributeName: [REQUIRED]
            The name of the engine attribute to update.
            

    :type AttributeValue: string
    :param AttributeValue: The value to set for the attribute.

    :rtype: dict
    :return: {
        'Server': {
            'AssociatePublicIpAddress': True|False,
            'BackupRetentionCount': 123,
            'ServerName': 'string',
            'CreatedAt': datetime(2015, 1, 1),
            'CloudFormationStackArn': 'string',
            'DisableAutomatedBackup': True|False,
            'Endpoint': 'string',
            'Engine': 'string',
            'EngineModel': 'string',
            'EngineAttributes': [
                {
                    'Name': 'string',
                    'Value': 'string'
                },
            ],
            'EngineVersion': 'string',
            'InstanceProfileArn': 'string',
            'InstanceType': 'string',
            'KeyPair': 'string',
            'MaintenanceStatus': 'SUCCESS'|'FAILED',
            'PreferredMaintenanceWindow': 'string',
            'PreferredBackupWindow': 'string',
            'SecurityGroupIds': [
                'string',
            ],
            'ServiceRoleArn': 'string',
            'Status': 'BACKING_UP'|'CONNECTION_LOST'|'CREATING'|'DELETING'|'MODIFYING'|'FAILED'|'HEALTHY'|'RUNNING'|'RESTORING'|'SETUP'|'UNDER_MAINTENANCE'|'UNHEALTHY'|'TERMINATED',
            'StatusReason': 'string',
            'SubnetIds': [
                'string',
            ],
            'ServerArn': 'string'
        }
    }
    
    
    :returns: 
    CHEF_PIVOTAL_KEY : A base64-encoded RSA private key that is generated by AWS OpsWorks for Chef Automate. This private key is required to access the Chef API.
    CHEF_STARTER_KIT : A base64-encoded ZIP file. The ZIP file contains a Chef starter kit, which includes a README, a configuration file, and the required RSA private key. Save this file, unzip it, and then change to the directory where you've unzipped the file contents. From this directory, you can run Knife commands.
    
    """
    pass

