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
    Associates a new node with the server. For more information about how to disassociate a node, see  DisassociateNode .
    On a Chef server: This command is an alternative to knife bootstrap .
    Example (Chef): aws opsworks-cm associate-node --server-name *MyServer* --node-name *MyManagedNode* --engine-attributes "Name=*CHEF_ORGANIZATION* ,Value=default" "Name=*CHEF_NODE_PUBLIC_KEY* ,Value=*public-key-pem* "
    On a Puppet server, this command is an alternative to the puppet cert sign command that signs a Puppet node CSR.
    Example (Chef): aws opsworks-cm associate-node --server-name *MyServer* --node-name *MyManagedNode* --engine-attributes "Name=*PUPPET_NODE_CSR* ,Value=*csr-pem* "
    A node can can only be associated with servers that are in a HEALTHY state. Otherwise, an InvalidStateException is thrown. A ResourceNotFoundException is thrown when the server does not exist. A ValidationException is raised when parameters of the request are not valid. The AssociateNode API call can be integrated into Auto Scaling configurations, AWS Cloudformation templates, or the user data of a server\'s instance.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param ServerName: [REQUIRED]\nThe name of the server with which to associate the node.\n

    :type NodeName: string
    :param NodeName: [REQUIRED]\nThe name of the node.\n

    :type EngineAttributes: list
    :param EngineAttributes: [REQUIRED]\nEngine attributes used for associating the node.\n\nAttributes accepted in a AssociateNode request for Chef\n\nCHEF_ORGANIZATION : The Chef organization with which the node is associated. By default only one organization named default can exist.\nCHEF_NODE_PUBLIC_KEY : A PEM-formatted public key. This key is required for the chef-client agent to access the Chef API.\n\n\nAttributes accepted in a AssociateNode request for Puppet\n\nPUPPET_NODE_CSR : A PEM-formatted certificate-signing request (CSR) that is created by the node.\n\n\n(dict) --A name and value pair that is specific to the engine of the server.\n\nName (string) --The name of the engine attribute.\n\nValue (string) --The value of the engine attribute.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'NodeAssociationStatusToken': 'string'
}


Response Structure

(dict) --

NodeAssociationStatusToken (string) --
Contains a token which can be passed to the DescribeNodeAssociationStatus API call to get the status of the association request.







Exceptions

OpsWorksCM.Client.exceptions.InvalidStateException
OpsWorksCM.Client.exceptions.ResourceNotFoundException
OpsWorksCM.Client.exceptions.ValidationException


    :return: {
        'NodeAssociationStatusToken': 'string'
    }
    
    
    :returns: 
    OpsWorksCM.Client.exceptions.InvalidStateException
    OpsWorksCM.Client.exceptions.ResourceNotFoundException
    OpsWorksCM.Client.exceptions.ValidationException
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def create_backup(ServerName=None, Description=None, Tags=None):
    """
    Creates an application-level backup of a server. While the server is in the BACKING_UP state, the server cannot be changed, and no additional backup can be created.
    Backups can be created for servers in RUNNING , HEALTHY , and UNHEALTHY states. By default, you can create a maximum of 50 manual backups.
    This operation is asynchronous.
    A LimitExceededException is thrown when the maximum number of manual backups is reached. An InvalidStateException is thrown when the server is not in any of the following states: RUNNING, HEALTHY, or UNHEALTHY. A ResourceNotFoundException is thrown when the server is not found. A ValidationException is thrown when parameters of the request are not valid.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_backup(
        ServerName='string',
        Description='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ServerName: string
    :param ServerName: [REQUIRED]\nThe name of the server that you want to back up.\n

    :type Description: string
    :param Description: A user-defined description of the backup.

    :type Tags: list
    :param Tags: A map that contains tag keys and tag values to attach to an AWS OpsWorks-CM server backup.\n\nThe key cannot be empty.\nThe key can be a maximum of 127 characters, and can contain only Unicode letters, numbers, or separators, or the following special characters: + - = . _ : /\nThe value can be a maximum 255 characters, and contain only Unicode letters, numbers, or separators, or the following special characters: + - = . _ : /\nLeading and trailing white spaces are trimmed from both the key and value.\nA maximum of 50 user-applied tags is allowed for tag-supported AWS OpsWorks-CM resources.\n\n\n(dict) --A map that contains tag keys and tag values to attach to an AWS OpsWorks for Chef Automate or AWS OpsWorks for Puppet Enterprise server. Leading and trailing white spaces are trimmed from both the key and value. A maximum of 50 user-applied tags is allowed for tag-supported AWS OpsWorks-CM resources.\n\nKey (string) -- [REQUIRED]A tag key, such as Stage or Name . A tag key cannot be empty. The key can be a maximum of 127 characters, and can contain only Unicode letters, numbers, or separators, or the following special characters: + - = . _ : /\n\nValue (string) -- [REQUIRED]An optional tag value, such as Production or test-owcm-server . The value can be a maximum of 255 characters, and contain only Unicode letters, numbers, or separators, or the following special characters: + - = . _ : /\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

Backup (dict) --
Backup created by request.

BackupArn (string) --
The ARN of the backup.

BackupId (string) --
The generated ID of the backup. Example: myServerName-yyyyMMddHHmmssSSS

BackupType (string) --
The backup type. Valid values are automated or manual .

CreatedAt (datetime) --
The time stamp when the backup was created in the database. Example: 2016-07-29T13:38:47.520Z

Description (string) --
A user-provided description for a manual backup. This field is empty for automated backups.

Engine (string) --
The engine type that is obtained from the server when the backup is created.

EngineModel (string) --
The engine model that is obtained from the server when the backup is created.

EngineVersion (string) --
The engine version that is obtained from the server when the backup is created.

InstanceProfileArn (string) --
The EC2 instance profile ARN that is obtained from the server when the backup is created. Because this value is stored, you are not required to provide the InstanceProfileArn again if you restore a backup.

InstanceType (string) --
The instance type that is obtained from the server when the backup is created.

KeyPair (string) --
The key pair that is obtained from the server when the backup is created.

PreferredBackupWindow (string) --
The preferred backup period that is obtained from the server when the backup is created.

PreferredMaintenanceWindow (string) --
The preferred maintenance period that is obtained from the server when the backup is created.

S3DataSize (integer) --
This field is deprecated and is no longer used.

S3DataUrl (string) --
This field is deprecated and is no longer used.

S3LogUrl (string) --
The Amazon S3 URL of the backup\'s log file.

SecurityGroupIds (list) --
The security group IDs that are obtained from the server when the backup is created.

(string) --


ServerName (string) --
The name of the server from which the backup was made.

ServiceRoleArn (string) --
The service role ARN that is obtained from the server when the backup is created.

Status (string) --
The status of a backup while in progress.

StatusDescription (string) --
An informational message about backup status.

SubnetIds (list) --
The subnet IDs that are obtained from the server when the backup is created.

(string) --


ToolsVersion (string) --
The version of AWS OpsWorks CM-specific tools that is obtained from the server when the backup is created.

UserArn (string) --
The IAM user ARN of the requester for manual backups. This field is empty for automated backups.









Exceptions

OpsWorksCM.Client.exceptions.InvalidStateException
OpsWorksCM.Client.exceptions.LimitExceededException
OpsWorksCM.Client.exceptions.ResourceNotFoundException
OpsWorksCM.Client.exceptions.ValidationException


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

def create_server(AssociatePublicIpAddress=None, CustomDomain=None, CustomCertificate=None, CustomPrivateKey=None, DisableAutomatedBackup=None, Engine=None, EngineModel=None, EngineVersion=None, EngineAttributes=None, BackupRetentionCount=None, ServerName=None, InstanceProfileArn=None, InstanceType=None, KeyPair=None, PreferredMaintenanceWindow=None, PreferredBackupWindow=None, SecurityGroupIds=None, ServiceRoleArn=None, SubnetIds=None, Tags=None, BackupId=None):
    """
    Creates and immedately starts a new server. The server is ready to use when it is in the HEALTHY state. By default, you can create a maximum of 10 servers.
    This operation is asynchronous.
    A LimitExceededException is thrown when you have created the maximum number of servers (10). A ResourceAlreadyExistsException is thrown when a server with the same name already exists in the account. A ResourceNotFoundException is thrown when you specify a backup ID that is not valid or is for a backup that does not exist. A ValidationException is thrown when parameters of the request are not valid.
    If you do not specify a security group by adding the SecurityGroupIds parameter, AWS OpsWorks creates a new security group.
    By default, your server is accessible from any IP address. We recommend that you update your security group rules to allow access from known IP addresses and address ranges only. To edit security group rules, open Security Groups in the navigation pane of the EC2 management console.
    To specify your own domain for a server, and provide your own self-signed or CA-signed certificate and private key, specify values for CustomDomain , CustomCertificate , and CustomPrivateKey .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_server(
        AssociatePublicIpAddress=True|False,
        CustomDomain='string',
        CustomCertificate='string',
        CustomPrivateKey='string',
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
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        BackupId='string'
    )
    
    
    :type AssociatePublicIpAddress: boolean
    :param AssociatePublicIpAddress: Associate a public IP address with a server that you are launching. Valid values are true or false . The default value is true .

    :type CustomDomain: string
    :param CustomDomain: An optional public endpoint of a server, such as https://aws.my-company.com . To access the server, create a CNAME DNS record in your preferred DNS service that points the custom domain to the endpoint that is generated when the server is created (the value of the CreateServer Endpoint attribute). You cannot access the server by using the generated Endpoint value if the server is using a custom domain. If you specify a custom domain, you must also specify values for CustomCertificate and CustomPrivateKey .

    :type CustomCertificate: string
    :param CustomCertificate: A PEM-formatted HTTPS certificate. The value can be be a single, self-signed certificate, or a certificate chain. If you specify a custom certificate, you must also specify values for CustomDomain and CustomPrivateKey . The following are requirements for the CustomCertificate value:\n\nYou can provide either a self-signed, custom certificate, or the full certificate chain.\nThe certificate must be a valid X509 certificate, or a certificate chain in PEM format.\nThe certificate must be valid at the time of upload. A certificate can\'t be used before its validity period begins (the certificate\'s NotBefore date), or after it expires (the certificate\'s NotAfter date).\nThe certificate\xe2\x80\x99s common name or subject alternative names (SANs), if present, must match the value of CustomDomain .\nThe certificate must match the value of CustomPrivateKey .\n\n

    :type CustomPrivateKey: string
    :param CustomPrivateKey: A private key in PEM format for connecting to the server by using HTTPS. The private key must not be encrypted; it cannot be protected by a password or passphrase. If you specify a custom private key, you must also specify values for CustomDomain and CustomCertificate .

    :type DisableAutomatedBackup: boolean
    :param DisableAutomatedBackup: Enable or disable scheduled backups. Valid values are true or false . The default value is true .

    :type Engine: string
    :param Engine: The configuration management engine to use. Valid values include ChefAutomate and Puppet .

    :type EngineModel: string
    :param EngineModel: The engine model of the server. Valid values in this release include Monolithic for Puppet and Single for Chef.

    :type EngineVersion: string
    :param EngineVersion: The major release version of the engine that you want to use. For a Chef server, the valid value for EngineVersion is currently 12 . For a Puppet server, the valid value is 2017 .

    :type EngineAttributes: list
    :param EngineAttributes: Optional engine attributes on a specified server.\n\nAttributes accepted in a Chef createServer request:\n\nCHEF_AUTOMATE_PIVOTAL_KEY : A base64-encoded RSA public key. The corresponding private key is required to access the Chef API. When no CHEF_AUTOMATE_PIVOTAL_KEY is set, a private key is generated and returned in the response.\nCHEF_AUTOMATE_ADMIN_PASSWORD : The password for the administrative user in the Chef Automate web-based dashboard. The password length is a minimum of eight characters, and a maximum of 32. The password can contain letters, numbers, and special characters (!/@#$%^&+=_). The password must contain at least one lower case letter, one upper case letter, one number, and one special character. When no CHEF_AUTOMATE_ADMIN_PASSWORD is set, one is generated and returned in the response.\n\n\nAttributes accepted in a Puppet createServer request:\n\nPUPPET_ADMIN_PASSWORD : To work with the Puppet Enterprise console, a password must use ASCII characters.\nPUPPET_R10K_REMOTE : The r10k remote is the URL of your control repository (for example, ssh://git@your.git-repo.com:user/control-repo.git). Specifying an r10k remote opens TCP port 8170.\nPUPPET_R10K_PRIVATE_KEY : If you are using a private Git repository, add PUPPET_R10K_PRIVATE_KEY to specify a PEM-encoded private SSH key.\n\n\n(dict) --A name and value pair that is specific to the engine of the server.\n\nName (string) --The name of the engine attribute.\n\nValue (string) --The value of the engine attribute.\n\n\n\n\n

    :type BackupRetentionCount: integer
    :param BackupRetentionCount: The number of automated backups that you want to keep. Whenever a new backup is created, AWS OpsWorks CM deletes the oldest backups if this number is exceeded. The default value is 1 .

    :type ServerName: string
    :param ServerName: [REQUIRED]\nThe name of the server. The server name must be unique within your AWS account, within each region. Server names must start with a letter; then letters, numbers, or hyphens (-) are allowed, up to a maximum of 40 characters.\n

    :type InstanceProfileArn: string
    :param InstanceProfileArn: [REQUIRED]\nThe ARN of the instance profile that your Amazon EC2 instances use. Although the AWS OpsWorks console typically creates the instance profile for you, if you are using API commands instead, run the service-role-creation.yaml AWS CloudFormation template, located at https://s3.amazonaws.com/opsworks-cm-us-east-1-prod-default-assets/misc/opsworks-cm-roles.yaml. This template creates a CloudFormation stack that includes the instance profile you need.\n

    :type InstanceType: string
    :param InstanceType: [REQUIRED]\nThe Amazon EC2 instance type to use. For example, m5.large .\n

    :type KeyPair: string
    :param KeyPair: The Amazon EC2 key pair to set for the instance. This parameter is optional; if desired, you may specify this parameter to connect to your instances by using SSH.

    :type PreferredMaintenanceWindow: string
    :param PreferredMaintenanceWindow: The start time for a one-hour period each week during which AWS OpsWorks CM performs maintenance on the instance. Valid values must be specified in the following format: DDD:HH:MM . The specified time is in coordinated universal time (UTC). The default value is a random one-hour period on Tuesday, Wednesday, or Friday. See TimeWindowDefinition for more information.\n\nExample: Mon:08:00 , which represents a start time of every Monday at 08:00 UTC. (8:00 a.m.)\n

    :type PreferredBackupWindow: string
    :param PreferredBackupWindow: The start time for a one-hour period during which AWS OpsWorks CM backs up application-level data on your server if automated backups are enabled. Valid values must be specified in one of the following formats:\n\nHH:MM for daily backups\nDDD:HH:MM for weekly backups\n\nThe specified time is in coordinated universal time (UTC). The default value is a random, daily start time.\n\nExample: 08:00 , which represents a daily start time of 08:00 UTC.Example: Mon:08:00 , which represents a start time of every Monday at 08:00 UTC. (8:00 a.m.)\n\n

    :type SecurityGroupIds: list
    :param SecurityGroupIds: A list of security group IDs to attach to the Amazon EC2 instance. If you add this parameter, the specified security groups must be within the VPC that is specified by SubnetIds .\nIf you do not specify this parameter, AWS OpsWorks CM creates one new security group that uses TCP ports 22 and 443, open to 0.0.0.0/0 (everyone).\n\n(string) --\n\n

    :type ServiceRoleArn: string
    :param ServiceRoleArn: [REQUIRED]\nThe service role that the AWS OpsWorks CM service backend uses to work with your account. Although the AWS OpsWorks management console typically creates the service role for you, if you are using the AWS CLI or API commands, run the service-role-creation.yaml AWS CloudFormation template, located at https://s3.amazonaws.com/opsworks-cm-us-east-1-prod-default-assets/misc/opsworks-cm-roles.yaml. This template creates a CloudFormation stack that includes the service role and instance profile that you need.\n

    :type SubnetIds: list
    :param SubnetIds: The IDs of subnets in which to launch the server EC2 instance.\nAmazon EC2-Classic customers: This field is required. All servers must run within a VPC. The VPC must have 'Auto Assign Public IP' enabled.\nEC2-VPC customers: This field is optional. If you do not specify subnet IDs, your EC2 instances are created in a default subnet that is selected by Amazon EC2. If you specify subnet IDs, the VPC must have 'Auto Assign Public IP' enabled.\nFor more information about supported Amazon EC2 platforms, see Supported Platforms .\n\n(string) --\n\n

    :type Tags: list
    :param Tags: A map that contains tag keys and tag values to attach to an AWS OpsWorks for Chef Automate or AWS OpsWorks for Puppet Enterprise server.\n\nThe key cannot be empty.\nThe key can be a maximum of 127 characters, and can contain only Unicode letters, numbers, or separators, or the following special characters: + - = . _ : / @\nThe value can be a maximum 255 characters, and contain only Unicode letters, numbers, or separators, or the following special characters: + - = . _ : / @\nLeading and trailing white spaces are trimmed from both the key and value.\nA maximum of 50 user-applied tags is allowed for any AWS OpsWorks-CM server.\n\n\n(dict) --A map that contains tag keys and tag values to attach to an AWS OpsWorks for Chef Automate or AWS OpsWorks for Puppet Enterprise server. Leading and trailing white spaces are trimmed from both the key and value. A maximum of 50 user-applied tags is allowed for tag-supported AWS OpsWorks-CM resources.\n\nKey (string) -- [REQUIRED]A tag key, such as Stage or Name . A tag key cannot be empty. The key can be a maximum of 127 characters, and can contain only Unicode letters, numbers, or separators, or the following special characters: + - = . _ : /\n\nValue (string) -- [REQUIRED]An optional tag value, such as Production or test-owcm-server . The value can be a maximum of 255 characters, and contain only Unicode letters, numbers, or separators, or the following special characters: + - = . _ : /\n\n\n\n\n

    :type BackupId: string
    :param BackupId: If you specify this field, AWS OpsWorks CM creates the server by using the backup represented by BackupId.

    :rtype: dict

ReturnsResponse Syntax
{
    'Server': {
        'AssociatePublicIpAddress': True|False,
        'BackupRetentionCount': 123,
        'ServerName': 'string',
        'CreatedAt': datetime(2015, 1, 1),
        'CloudFormationStackArn': 'string',
        'CustomDomain': 'string',
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


Response Structure

(dict) --

Server (dict) --
The server that is created by the request.

AssociatePublicIpAddress (boolean) --
Associate a public IP address with a server that you are launching.

BackupRetentionCount (integer) --
The number of automated backups to keep.

ServerName (string) --
The name of the server.

CreatedAt (datetime) --
Time stamp of server creation. Example 2016-07-29T13:38:47.520Z

CloudFormationStackArn (string) --
The ARN of the CloudFormation stack that was used to create the server.

CustomDomain (string) --
An optional public endpoint of a server, such as https://aws.my-company.com . You cannot access the server by using the Endpoint value if the server has a CustomDomain specified.

DisableAutomatedBackup (boolean) --
Disables automated backups. The number of stored backups is dependent on the value of PreferredBackupCount.

Endpoint (string) --
A DNS name that can be used to access the engine. Example: myserver-asdfghjkl.us-east-1.opsworks.io . You cannot access the server by using the Endpoint value if the server has a CustomDomain specified.

Engine (string) --
The engine type of the server. Valid values in this release include ChefAutomate and Puppet .

EngineModel (string) --
The engine model of the server. Valid values in this release include Monolithic for Puppet and Single for Chef.

EngineAttributes (list) --
The response of a createServer() request returns the master credential to access the server in EngineAttributes. These credentials are not stored by AWS OpsWorks CM; they are returned only as part of the result of createServer().

Attributes returned in a createServer response for Chef


CHEF_AUTOMATE_PIVOTAL_KEY : A base64-encoded RSA private key that is generated by AWS OpsWorks for Chef Automate. This private key is required to access the Chef API.
CHEF_STARTER_KIT : A base64-encoded ZIP file. The ZIP file contains a Chef starter kit, which includes a README, a configuration file, and the required RSA private key. Save this file, unzip it, and then change to the directory where you\'ve unzipped the file contents. From this directory, you can run Knife commands.


Attributes returned in a createServer response for Puppet


PUPPET_STARTER_KIT : A base64-encoded ZIP file. The ZIP file contains a Puppet starter kit, including a README and a required private key. Save this file, unzip it, and then change to the directory where you\'ve unzipped the file contents.
PUPPET_ADMIN_PASSWORD : An administrator password that you can use to sign in to the Puppet Enterprise console after the server is online.


(dict) --
A name and value pair that is specific to the engine of the server.

Name (string) --
The name of the engine attribute.

Value (string) --
The value of the engine attribute.





EngineVersion (string) --
The engine version of the server. For a Chef server, the valid value for EngineVersion is currently 12 . For a Puppet server, the valid value is 2017 .

InstanceProfileArn (string) --
The instance profile ARN of the server.

InstanceType (string) --
The instance type for the server, as specified in the CloudFormation stack. This might not be the same instance type that is shown in the EC2 console.

KeyPair (string) --
The key pair associated with the server.

MaintenanceStatus (string) --
The status of the most recent server maintenance run. Shows SUCCESS or FAILED .

PreferredMaintenanceWindow (string) --
The preferred maintenance period specified for the server.

PreferredBackupWindow (string) --
The preferred backup period specified for the server.

SecurityGroupIds (list) --
The security group IDs for the server, as specified in the CloudFormation stack. These might not be the same security groups that are shown in the EC2 console.

(string) --


ServiceRoleArn (string) --
The service role ARN used to create the server.

Status (string) --
The server\'s status. This field displays the states of actions in progress, such as creating, running, or backing up the server, as well as the server\'s health state.

StatusReason (string) --
Depending on the server status, this field has either a human-readable message (such as a create or backup error), or an escaped block of JSON (used for health check results).

SubnetIds (list) --
The subnet IDs specified in a CreateServer request.

(string) --


ServerArn (string) --
The ARN of the server.









Exceptions

OpsWorksCM.Client.exceptions.LimitExceededException
OpsWorksCM.Client.exceptions.ResourceAlreadyExistsException
OpsWorksCM.Client.exceptions.ResourceNotFoundException
OpsWorksCM.Client.exceptions.ValidationException


    :return: {
        'Server': {
            'AssociatePublicIpAddress': True|False,
            'BackupRetentionCount': 123,
            'ServerName': 'string',
            'CreatedAt': datetime(2015, 1, 1),
            'CloudFormationStackArn': 'string',
            'CustomDomain': 'string',
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
    CHEF_AUTOMATE_PIVOTAL_KEY : A base64-encoded RSA private key that is generated by AWS OpsWorks for Chef Automate. This private key is required to access the Chef API.
    CHEF_STARTER_KIT : A base64-encoded ZIP file. The ZIP file contains a Chef starter kit, which includes a README, a configuration file, and the required RSA private key. Save this file, unzip it, and then change to the directory where you\'ve unzipped the file contents. From this directory, you can run Knife commands.
    
    """
    pass

def delete_backup(BackupId=None):
    """
    Deletes a backup. You can delete both manual and automated backups. This operation is asynchronous.
    An InvalidStateException is thrown when a backup deletion is already in progress. A ResourceNotFoundException is thrown when the backup does not exist. A ValidationException is thrown when parameters of the request are not valid.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_backup(
        BackupId='string'
    )
    
    
    :type BackupId: string
    :param BackupId: [REQUIRED]\nThe ID of the backup to delete. Run the DescribeBackups command to get a list of backup IDs. Backup IDs are in the format ServerName-yyyyMMddHHmmssSSS .\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

OpsWorksCM.Client.exceptions.InvalidStateException
OpsWorksCM.Client.exceptions.ResourceNotFoundException
OpsWorksCM.Client.exceptions.ValidationException


    :return: {}
    
    
    :returns: 
    OpsWorksCM.Client.exceptions.InvalidStateException
    OpsWorksCM.Client.exceptions.ResourceNotFoundException
    OpsWorksCM.Client.exceptions.ValidationException
    
    """
    pass

def delete_server(ServerName=None):
    """
    Deletes the server and the underlying AWS CloudFormation stacks (including the server\'s EC2 instance). When you run this command, the server state is updated to DELETING . After the server is deleted, it is no longer returned by DescribeServer requests. If the AWS CloudFormation stack cannot be deleted, the server cannot be deleted.
    This operation is asynchronous.
    An InvalidStateException is thrown when a server deletion is already in progress. A ResourceNotFoundException is thrown when the server does not exist. A ValidationException is raised when parameters of the request are not valid.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_server(
        ServerName='string'
    )
    
    
    :type ServerName: string
    :param ServerName: [REQUIRED]\nThe ID of the server to delete.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

OpsWorksCM.Client.exceptions.InvalidStateException
OpsWorksCM.Client.exceptions.ResourceNotFoundException
OpsWorksCM.Client.exceptions.ValidationException


    :return: {}
    
    
    :returns: 
    OpsWorksCM.Client.exceptions.InvalidStateException
    OpsWorksCM.Client.exceptions.ResourceNotFoundException
    OpsWorksCM.Client.exceptions.ValidationException
    
    """
    pass

def describe_account_attributes():
    """
    Describes your OpsWorks-CM account attributes.
    This operation is synchronous.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_account_attributes()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'Attributes': [
        {
            'Name': 'string',
            'Maximum': 123,
            'Used': 123
        },
    ]
}


Response Structure

(dict) --
Attributes (list) --The attributes that are currently set for the account.

(dict) --Stores account attributes.

Name (string) --The attribute name. The following are supported attribute names.

ServerLimit: The number of current servers/maximum number of servers allowed. By default, you can have a maximum of 10 servers.
ManualBackupLimit: The number of current manual backups/maximum number of backups allowed. By default, you can have a maximum of 50 manual backups saved.


Maximum (integer) --The maximum allowed value.

Used (integer) --The current usage, such as the current number of servers that are associated with the account.











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
    
    Exceptions
    
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
    :param NextToken: This is not currently implemented for DescribeBackups requests.

    :type MaxResults: integer
    :param MaxResults: This is not currently implemented for DescribeBackups requests.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

Backups (list) --
Contains the response to a DescribeBackups request.

(dict) --
Describes a single backup.

BackupArn (string) --
The ARN of the backup.

BackupId (string) --
The generated ID of the backup. Example: myServerName-yyyyMMddHHmmssSSS

BackupType (string) --
The backup type. Valid values are automated or manual .

CreatedAt (datetime) --
The time stamp when the backup was created in the database. Example: 2016-07-29T13:38:47.520Z

Description (string) --
A user-provided description for a manual backup. This field is empty for automated backups.

Engine (string) --
The engine type that is obtained from the server when the backup is created.

EngineModel (string) --
The engine model that is obtained from the server when the backup is created.

EngineVersion (string) --
The engine version that is obtained from the server when the backup is created.

InstanceProfileArn (string) --
The EC2 instance profile ARN that is obtained from the server when the backup is created. Because this value is stored, you are not required to provide the InstanceProfileArn again if you restore a backup.

InstanceType (string) --
The instance type that is obtained from the server when the backup is created.

KeyPair (string) --
The key pair that is obtained from the server when the backup is created.

PreferredBackupWindow (string) --
The preferred backup period that is obtained from the server when the backup is created.

PreferredMaintenanceWindow (string) --
The preferred maintenance period that is obtained from the server when the backup is created.

S3DataSize (integer) --
This field is deprecated and is no longer used.

S3DataUrl (string) --
This field is deprecated and is no longer used.

S3LogUrl (string) --
The Amazon S3 URL of the backup\'s log file.

SecurityGroupIds (list) --
The security group IDs that are obtained from the server when the backup is created.

(string) --


ServerName (string) --
The name of the server from which the backup was made.

ServiceRoleArn (string) --
The service role ARN that is obtained from the server when the backup is created.

Status (string) --
The status of a backup while in progress.

StatusDescription (string) --
An informational message about backup status.

SubnetIds (list) --
The subnet IDs that are obtained from the server when the backup is created.

(string) --


ToolsVersion (string) --
The version of AWS OpsWorks CM-specific tools that is obtained from the server when the backup is created.

UserArn (string) --
The IAM user ARN of the requester for manual backups. This field is empty for automated backups.





NextToken (string) --
This is not currently implemented for DescribeBackups requests.







Exceptions

OpsWorksCM.Client.exceptions.ValidationException
OpsWorksCM.Client.exceptions.ResourceNotFoundException
OpsWorksCM.Client.exceptions.InvalidNextTokenException


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
    
    Exceptions
    
    :example: response = client.describe_events(
        ServerName='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type ServerName: string
    :param ServerName: [REQUIRED]\nThe name of the server for which you want to view events.\n

    :type NextToken: string
    :param NextToken: NextToken is a string that is returned in some command responses. It indicates that not all entries have been returned, and that you must run at least one more request to get remaining items. To get remaining results, call DescribeEvents again, and assign the token from the previous results as the value of the nextToken parameter. If there are no more results, the response object\'s nextToken parameter value is null . Setting a nextToken value that was not returned in your previous results causes an InvalidNextTokenException to occur.

    :type MaxResults: integer
    :param MaxResults: To receive a paginated response, use this parameter to specify the maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a NextToken value that you can assign to the NextToken request parameter to get the next set of results.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

ServerEvents (list) --
Contains the response to a DescribeEvents request.

(dict) --
An event that is related to the server, such as the start of maintenance or backup.

CreatedAt (datetime) --
The time when the event occurred.

ServerName (string) --
The name of the server on or for which the event occurred.

Message (string) --
A human-readable informational or status message.

LogUrl (string) --
The Amazon S3 URL of the event\'s log file.





NextToken (string) --
NextToken is a string that is returned in some command responses. It indicates that not all entries have been returned, and that you must run at least one more request to get remaining items. To get remaining results, call DescribeEvents again, and assign the token from the previous results as the value of the nextToken parameter. If there are no more results, the response object\'s nextToken parameter value is null . Setting a nextToken value that was not returned in your previous results causes an InvalidNextTokenException to occur.







Exceptions

OpsWorksCM.Client.exceptions.ValidationException
OpsWorksCM.Client.exceptions.InvalidNextTokenException
OpsWorksCM.Client.exceptions.ResourceNotFoundException


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
    
    
    :returns: 
    OpsWorksCM.Client.exceptions.ValidationException
    OpsWorksCM.Client.exceptions.InvalidNextTokenException
    OpsWorksCM.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def describe_node_association_status(NodeAssociationStatusToken=None, ServerName=None):
    """
    Returns the current status of an existing association or disassociation request.
    A ResourceNotFoundException is thrown when no recent association or disassociation request with the specified token is found, or when the server does not exist. A ValidationException is raised when parameters of the request are not valid.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_node_association_status(
        NodeAssociationStatusToken='string',
        ServerName='string'
    )
    
    
    :type NodeAssociationStatusToken: string
    :param NodeAssociationStatusToken: [REQUIRED]\nThe token returned in either the AssociateNodeResponse or the DisassociateNodeResponse.\n

    :type ServerName: string
    :param ServerName: [REQUIRED]\nThe name of the server from which to disassociate the node.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'NodeAssociationStatus': 'SUCCESS'|'FAILED'|'IN_PROGRESS',
    'EngineAttributes': [
        {
            'Name': 'string',
            'Value': 'string'
        },
    ]
}


Response Structure

(dict) --

NodeAssociationStatus (string) --
The status of the association or disassociation request.

Possible values:


SUCCESS : The association or disassociation succeeded.
FAILED : The association or disassociation failed.
IN_PROGRESS : The association or disassociation is still in progress.


EngineAttributes (list) --
Attributes specific to the node association. In Puppet, the attibute PUPPET_NODE_CERT contains the signed certificate (the result of the CSR).

(dict) --
A name and value pair that is specific to the engine of the server.

Name (string) --
The name of the engine attribute.

Value (string) --
The value of the engine attribute.











Exceptions

OpsWorksCM.Client.exceptions.ResourceNotFoundException
OpsWorksCM.Client.exceptions.ValidationException


    :return: {
        'NodeAssociationStatus': 'SUCCESS'|'FAILED'|'IN_PROGRESS',
        'EngineAttributes': [
            {
                'Name': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    :returns: 
    SUCCESS : The association or disassociation succeeded.
    FAILED : The association or disassociation failed.
    IN_PROGRESS : The association or disassociation is still in progress.
    
    """
    pass

def describe_servers(ServerName=None, NextToken=None, MaxResults=None):
    """
    Lists all configuration management servers that are identified with your account. Only the stored results from Amazon DynamoDB are returned. AWS OpsWorks CM does not query other services.
    This operation is synchronous.
    A ResourceNotFoundException is thrown when the server does not exist. A ValidationException is raised when parameters of the request are not valid.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_servers(
        ServerName='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type ServerName: string
    :param ServerName: Describes the server with the specified ServerName.

    :type NextToken: string
    :param NextToken: This is not currently implemented for DescribeServers requests.

    :type MaxResults: integer
    :param MaxResults: This is not currently implemented for DescribeServers requests.

    :rtype: dict

ReturnsResponse Syntax
{
    'Servers': [
        {
            'AssociatePublicIpAddress': True|False,
            'BackupRetentionCount': 123,
            'ServerName': 'string',
            'CreatedAt': datetime(2015, 1, 1),
            'CloudFormationStackArn': 'string',
            'CustomDomain': 'string',
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


Response Structure

(dict) --

Servers (list) --
Contains the response to a DescribeServers request.

For Chef Automate servers: If DescribeServersResponse$Servers$EngineAttributes includes CHEF_MAJOR_UPGRADE_AVAILABLE, you can upgrade the Chef Automate server to Chef Automate 2. To be eligible for upgrade, a server running Chef Automate 1 must have had at least one successful maintenance run after November 1, 2019.
For Puppet Server: DescribeServersResponse$Servers$EngineAttributes contains PUPPET_API_CA_CERT. This is the PEM-encoded CA certificate that is used by the Puppet API over TCP port number 8140. The CA certificate is also used to sign node certificates.


(dict) --
Describes a configuration management server.

AssociatePublicIpAddress (boolean) --
Associate a public IP address with a server that you are launching.

BackupRetentionCount (integer) --
The number of automated backups to keep.

ServerName (string) --
The name of the server.

CreatedAt (datetime) --
Time stamp of server creation. Example 2016-07-29T13:38:47.520Z

CloudFormationStackArn (string) --
The ARN of the CloudFormation stack that was used to create the server.

CustomDomain (string) --
An optional public endpoint of a server, such as https://aws.my-company.com . You cannot access the server by using the Endpoint value if the server has a CustomDomain specified.

DisableAutomatedBackup (boolean) --
Disables automated backups. The number of stored backups is dependent on the value of PreferredBackupCount.

Endpoint (string) --
A DNS name that can be used to access the engine. Example: myserver-asdfghjkl.us-east-1.opsworks.io . You cannot access the server by using the Endpoint value if the server has a CustomDomain specified.

Engine (string) --
The engine type of the server. Valid values in this release include ChefAutomate and Puppet .

EngineModel (string) --
The engine model of the server. Valid values in this release include Monolithic for Puppet and Single for Chef.

EngineAttributes (list) --
The response of a createServer() request returns the master credential to access the server in EngineAttributes. These credentials are not stored by AWS OpsWorks CM; they are returned only as part of the result of createServer().

Attributes returned in a createServer response for Chef


CHEF_AUTOMATE_PIVOTAL_KEY : A base64-encoded RSA private key that is generated by AWS OpsWorks for Chef Automate. This private key is required to access the Chef API.
CHEF_STARTER_KIT : A base64-encoded ZIP file. The ZIP file contains a Chef starter kit, which includes a README, a configuration file, and the required RSA private key. Save this file, unzip it, and then change to the directory where you\'ve unzipped the file contents. From this directory, you can run Knife commands.


Attributes returned in a createServer response for Puppet


PUPPET_STARTER_KIT : A base64-encoded ZIP file. The ZIP file contains a Puppet starter kit, including a README and a required private key. Save this file, unzip it, and then change to the directory where you\'ve unzipped the file contents.
PUPPET_ADMIN_PASSWORD : An administrator password that you can use to sign in to the Puppet Enterprise console after the server is online.


(dict) --
A name and value pair that is specific to the engine of the server.

Name (string) --
The name of the engine attribute.

Value (string) --
The value of the engine attribute.





EngineVersion (string) --
The engine version of the server. For a Chef server, the valid value for EngineVersion is currently 12 . For a Puppet server, the valid value is 2017 .

InstanceProfileArn (string) --
The instance profile ARN of the server.

InstanceType (string) --
The instance type for the server, as specified in the CloudFormation stack. This might not be the same instance type that is shown in the EC2 console.

KeyPair (string) --
The key pair associated with the server.

MaintenanceStatus (string) --
The status of the most recent server maintenance run. Shows SUCCESS or FAILED .

PreferredMaintenanceWindow (string) --
The preferred maintenance period specified for the server.

PreferredBackupWindow (string) --
The preferred backup period specified for the server.

SecurityGroupIds (list) --
The security group IDs for the server, as specified in the CloudFormation stack. These might not be the same security groups that are shown in the EC2 console.

(string) --


ServiceRoleArn (string) --
The service role ARN used to create the server.

Status (string) --
The server\'s status. This field displays the states of actions in progress, such as creating, running, or backing up the server, as well as the server\'s health state.

StatusReason (string) --
Depending on the server status, this field has either a human-readable message (such as a create or backup error), or an escaped block of JSON (used for health check results).

SubnetIds (list) --
The subnet IDs specified in a CreateServer request.

(string) --


ServerArn (string) --
The ARN of the server.





NextToken (string) --
This is not currently implemented for DescribeServers requests.







Exceptions

OpsWorksCM.Client.exceptions.ValidationException
OpsWorksCM.Client.exceptions.ResourceNotFoundException
OpsWorksCM.Client.exceptions.InvalidNextTokenException


    :return: {
        'Servers': [
            {
                'AssociatePublicIpAddress': True|False,
                'BackupRetentionCount': 123,
                'ServerName': 'string',
                'CreatedAt': datetime(2015, 1, 1),
                'CloudFormationStackArn': 'string',
                'CustomDomain': 'string',
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
    CHEF_AUTOMATE_PIVOTAL_KEY : A base64-encoded RSA private key that is generated by AWS OpsWorks for Chef Automate. This private key is required to access the Chef API.
    CHEF_STARTER_KIT : A base64-encoded ZIP file. The ZIP file contains a Chef starter kit, which includes a README, a configuration file, and the required RSA private key. Save this file, unzip it, and then change to the directory where you\'ve unzipped the file contents. From this directory, you can run Knife commands.
    
    """
    pass

def disassociate_node(ServerName=None, NodeName=None, EngineAttributes=None):
    """
    Disassociates a node from an AWS OpsWorks CM server, and removes the node from the server\'s managed nodes. After a node is disassociated, the node key pair is no longer valid for accessing the configuration manager\'s API. For more information about how to associate a node, see  AssociateNode .
    A node can can only be disassociated from a server that is in a HEALTHY state. Otherwise, an InvalidStateException is thrown. A ResourceNotFoundException is thrown when the server does not exist. A ValidationException is raised when parameters of the request are not valid.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param ServerName: [REQUIRED]\nThe name of the server from which to disassociate the node.\n

    :type NodeName: string
    :param NodeName: [REQUIRED]\nThe name of the client node.\n

    :type EngineAttributes: list
    :param EngineAttributes: Engine attributes that are used for disassociating the node. No attributes are required for Puppet.\n\nAttributes required in a DisassociateNode request for Chef\n\nCHEF_ORGANIZATION : The Chef organization with which the node was associated. By default only one organization named default can exist.\n\n\n(dict) --A name and value pair that is specific to the engine of the server.\n\nName (string) --The name of the engine attribute.\n\nValue (string) --The value of the engine attribute.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'NodeAssociationStatusToken': 'string'
}


Response Structure

(dict) --

NodeAssociationStatusToken (string) --
Contains a token which can be passed to the DescribeNodeAssociationStatus API call to get the status of the disassociation request.







Exceptions

OpsWorksCM.Client.exceptions.InvalidStateException
OpsWorksCM.Client.exceptions.ResourceNotFoundException
OpsWorksCM.Client.exceptions.ValidationException


    :return: {
        'NodeAssociationStatusToken': 'string'
    }
    
    
    :returns: 
    OpsWorksCM.Client.exceptions.InvalidStateException
    OpsWorksCM.Client.exceptions.ResourceNotFoundException
    OpsWorksCM.Client.exceptions.ValidationException
    
    """
    pass

def export_server_engine_attribute(ExportAttributeName=None, ServerName=None, InputAttributes=None):
    """
    Exports a specified server engine attribute as a base64-encoded string. For example, you can export user data that you can use in EC2 to associate nodes with a server.
    This operation is synchronous.
    A ValidationException is raised when parameters of the request are not valid. A ResourceNotFoundException is thrown when the server does not exist. An InvalidStateException is thrown when the server is in any of the following states: CREATING, TERMINATED, FAILED or DELETING.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.export_server_engine_attribute(
        ExportAttributeName='string',
        ServerName='string',
        InputAttributes=[
            {
                'Name': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ExportAttributeName: string
    :param ExportAttributeName: [REQUIRED]\nThe name of the export attribute. Currently, the supported export attribute is Userdata . This exports a user data script that includes parameters and values provided in the InputAttributes list.\n

    :type ServerName: string
    :param ServerName: [REQUIRED]\nThe name of the server from which you are exporting the attribute.\n

    :type InputAttributes: list
    :param InputAttributes: The list of engine attributes. The list type is EngineAttribute . An EngineAttribute list item is a pair that includes an attribute name and its value. For the Userdata ExportAttributeName, the following are supported engine attribute names.\n\nRunList In Chef, a list of roles or recipes that are run in the specified order. In Puppet, this parameter is ignored.\nOrganizationName In Chef, an organization name. AWS OpsWorks for Chef Automate always creates the organization default . In Puppet, this parameter is ignored.\nNodeEnvironment In Chef, a node environment (for example, development, staging, or one-box). In Puppet, this parameter is ignored.\nNodeClientVersion In Chef, the version of the Chef engine (three numbers separated by dots, such as 13.8.5). If this attribute is empty, OpsWorks for Chef Automate uses the most current version. In Puppet, this parameter is ignored.\n\n\n(dict) --A name and value pair that is specific to the engine of the server.\n\nName (string) --The name of the engine attribute.\n\nValue (string) --The value of the engine attribute.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'EngineAttribute': {
        'Name': 'string',
        'Value': 'string'
    },
    'ServerName': 'string'
}


Response Structure

(dict) --

EngineAttribute (dict) --
The requested engine attribute pair with attribute name and value.

Name (string) --
The name of the engine attribute.

Value (string) --
The value of the engine attribute.



ServerName (string) --
The server name used in the request.







Exceptions

OpsWorksCM.Client.exceptions.ValidationException
OpsWorksCM.Client.exceptions.ResourceNotFoundException
OpsWorksCM.Client.exceptions.InvalidStateException


    :return: {
        'EngineAttribute': {
            'Name': 'string',
            'Value': 'string'
        },
        'ServerName': 'string'
    }
    
    
    :returns: 
    OpsWorksCM.Client.exceptions.ValidationException
    OpsWorksCM.Client.exceptions.ResourceNotFoundException
    OpsWorksCM.Client.exceptions.InvalidStateException
    
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

def get_waiter(waiter_name=None):
    """
    Returns an object that can wait for some condition.
    
    :type waiter_name: str
    :param waiter_name: The name of the waiter to get. See the waiters\nsection of the service docs for a list of available waiters.

    :rtype: botocore.waiter.Waiter


    """
    pass

def list_tags_for_resource(ResourceArn=None, NextToken=None, MaxResults=None):
    """
    Returns a list of tags that are applied to the specified AWS OpsWorks for Chef Automate or AWS OpsWorks for Puppet Enterprise servers or backups.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        ResourceArn='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Number (ARN) of an AWS OpsWorks for Chef Automate or AWS OpsWorks for Puppet Enterprise server for which you want to show applied tags. For example, arn:aws:opsworks-cm:us-west-2:123456789012:server/test-owcm-server/EXAMPLE-66b0-4196-8274-d1a2bEXAMPLE .\n

    :type NextToken: string
    :param NextToken: NextToken is a string that is returned in some command responses. It indicates that not all entries have been returned, and that you must run at least one more request to get remaining items. To get remaining results, call ListTagsForResource again, and assign the token from the previous results as the value of the nextToken parameter. If there are no more results, the response object\'s nextToken parameter value is null . Setting a nextToken value that was not returned in your previous results causes an InvalidNextTokenException to occur.

    :type MaxResults: integer
    :param MaxResults: To receive a paginated response, use this parameter to specify the maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a NextToken value that you can assign to the NextToken request parameter to get the next set of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'Tags': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Tags (list) --
Tags that have been applied to the resource.

(dict) --
A map that contains tag keys and tag values to attach to an AWS OpsWorks for Chef Automate or AWS OpsWorks for Puppet Enterprise server. Leading and trailing white spaces are trimmed from both the key and value. A maximum of 50 user-applied tags is allowed for tag-supported AWS OpsWorks-CM resources.

Key (string) --
A tag key, such as Stage or Name . A tag key cannot be empty. The key can be a maximum of 127 characters, and can contain only Unicode letters, numbers, or separators, or the following special characters: + - = . _ : /

Value (string) --
An optional tag value, such as Production or test-owcm-server . The value can be a maximum of 255 characters, and contain only Unicode letters, numbers, or separators, or the following special characters: + - = . _ : /





NextToken (string) --
A token that you can use as the value of NextToken in subsequent calls to the API to show more results.







Exceptions

OpsWorksCM.Client.exceptions.ResourceNotFoundException
OpsWorksCM.Client.exceptions.ValidationException


    :return: {
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    OpsWorksCM.Client.exceptions.ResourceNotFoundException
    OpsWorksCM.Client.exceptions.ValidationException
    
    """
    pass

def restore_server(BackupId=None, ServerName=None, InstanceType=None, KeyPair=None):
    """
    Restores a backup to a server that is in a CONNECTION_LOST , HEALTHY , RUNNING , UNHEALTHY , or TERMINATED state. When you run RestoreServer, the server\'s EC2 instance is deleted, and a new EC2 instance is configured. RestoreServer maintains the existing server endpoint, so configuration management of the server\'s client devices (nodes) should continue to work.
    Restoring from a backup is performed by creating a new EC2 instance. If restoration is successful, and the server is in a HEALTHY state, AWS OpsWorks CM switches traffic over to the new instance. After restoration is finished, the old EC2 instance is maintained in a Running or Stopped state, but is eventually terminated.
    This operation is asynchronous.
    An InvalidStateException is thrown when the server is not in a valid state. A ResourceNotFoundException is thrown when the server does not exist. A ValidationException is raised when parameters of the request are not valid.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.restore_server(
        BackupId='string',
        ServerName='string',
        InstanceType='string',
        KeyPair='string'
    )
    
    
    :type BackupId: string
    :param BackupId: [REQUIRED]\nThe ID of the backup that you want to use to restore a server.\n

    :type ServerName: string
    :param ServerName: [REQUIRED]\nThe name of the server that you want to restore.\n

    :type InstanceType: string
    :param InstanceType: The type of instance to restore. Valid values must be specified in the following format: ^([cm][34]|t2).* For example, m5.large . Valid values are m5.large , r5.xlarge , and r5.2xlarge . If you do not specify this parameter, RestoreServer uses the instance type from the specified backup.

    :type KeyPair: string
    :param KeyPair: The name of the key pair to set on the new EC2 instance. This can be helpful if the administrator no longer has the SSH key.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

OpsWorksCM.Client.exceptions.InvalidStateException
OpsWorksCM.Client.exceptions.ResourceNotFoundException
OpsWorksCM.Client.exceptions.ValidationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def start_maintenance(ServerName=None, EngineAttributes=None):
    """
    Manually starts server maintenance. This command can be useful if an earlier maintenance attempt failed, and the underlying cause of maintenance failure has been resolved. The server is in an UNDER_MAINTENANCE state while maintenance is in progress.
    Maintenance can only be started on servers in HEALTHY and UNHEALTHY states. Otherwise, an InvalidStateException is thrown. A ResourceNotFoundException is thrown when the server does not exist. A ValidationException is raised when parameters of the request are not valid.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_maintenance(
        ServerName='string',
        EngineAttributes=[
            {
                'Name': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ServerName: string
    :param ServerName: [REQUIRED]\nThe name of the server on which to run maintenance.\n

    :type EngineAttributes: list
    :param EngineAttributes: Engine attributes that are specific to the server on which you want to run maintenance.\n\nAttributes accepted in a StartMaintenance request for Chef\n\nCHEF_MAJOR_UPGRADE : If a Chef Automate server is eligible for upgrade to Chef Automate 2, add this engine attribute to a StartMaintenance request and set the value to true to upgrade the server to Chef Automate 2. For more information, see Upgrade an AWS OpsWorks for Chef Automate Server to Chef Automate 2 .\n\n\n(dict) --A name and value pair that is specific to the engine of the server.\n\nName (string) --The name of the engine attribute.\n\nValue (string) --The value of the engine attribute.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Server': {
        'AssociatePublicIpAddress': True|False,
        'BackupRetentionCount': 123,
        'ServerName': 'string',
        'CreatedAt': datetime(2015, 1, 1),
        'CloudFormationStackArn': 'string',
        'CustomDomain': 'string',
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


Response Structure

(dict) --

Server (dict) --
Contains the response to a StartMaintenance request.

AssociatePublicIpAddress (boolean) --
Associate a public IP address with a server that you are launching.

BackupRetentionCount (integer) --
The number of automated backups to keep.

ServerName (string) --
The name of the server.

CreatedAt (datetime) --
Time stamp of server creation. Example 2016-07-29T13:38:47.520Z

CloudFormationStackArn (string) --
The ARN of the CloudFormation stack that was used to create the server.

CustomDomain (string) --
An optional public endpoint of a server, such as https://aws.my-company.com . You cannot access the server by using the Endpoint value if the server has a CustomDomain specified.

DisableAutomatedBackup (boolean) --
Disables automated backups. The number of stored backups is dependent on the value of PreferredBackupCount.

Endpoint (string) --
A DNS name that can be used to access the engine. Example: myserver-asdfghjkl.us-east-1.opsworks.io . You cannot access the server by using the Endpoint value if the server has a CustomDomain specified.

Engine (string) --
The engine type of the server. Valid values in this release include ChefAutomate and Puppet .

EngineModel (string) --
The engine model of the server. Valid values in this release include Monolithic for Puppet and Single for Chef.

EngineAttributes (list) --
The response of a createServer() request returns the master credential to access the server in EngineAttributes. These credentials are not stored by AWS OpsWorks CM; they are returned only as part of the result of createServer().

Attributes returned in a createServer response for Chef


CHEF_AUTOMATE_PIVOTAL_KEY : A base64-encoded RSA private key that is generated by AWS OpsWorks for Chef Automate. This private key is required to access the Chef API.
CHEF_STARTER_KIT : A base64-encoded ZIP file. The ZIP file contains a Chef starter kit, which includes a README, a configuration file, and the required RSA private key. Save this file, unzip it, and then change to the directory where you\'ve unzipped the file contents. From this directory, you can run Knife commands.


Attributes returned in a createServer response for Puppet


PUPPET_STARTER_KIT : A base64-encoded ZIP file. The ZIP file contains a Puppet starter kit, including a README and a required private key. Save this file, unzip it, and then change to the directory where you\'ve unzipped the file contents.
PUPPET_ADMIN_PASSWORD : An administrator password that you can use to sign in to the Puppet Enterprise console after the server is online.


(dict) --
A name and value pair that is specific to the engine of the server.

Name (string) --
The name of the engine attribute.

Value (string) --
The value of the engine attribute.





EngineVersion (string) --
The engine version of the server. For a Chef server, the valid value for EngineVersion is currently 12 . For a Puppet server, the valid value is 2017 .

InstanceProfileArn (string) --
The instance profile ARN of the server.

InstanceType (string) --
The instance type for the server, as specified in the CloudFormation stack. This might not be the same instance type that is shown in the EC2 console.

KeyPair (string) --
The key pair associated with the server.

MaintenanceStatus (string) --
The status of the most recent server maintenance run. Shows SUCCESS or FAILED .

PreferredMaintenanceWindow (string) --
The preferred maintenance period specified for the server.

PreferredBackupWindow (string) --
The preferred backup period specified for the server.

SecurityGroupIds (list) --
The security group IDs for the server, as specified in the CloudFormation stack. These might not be the same security groups that are shown in the EC2 console.

(string) --


ServiceRoleArn (string) --
The service role ARN used to create the server.

Status (string) --
The server\'s status. This field displays the states of actions in progress, such as creating, running, or backing up the server, as well as the server\'s health state.

StatusReason (string) --
Depending on the server status, this field has either a human-readable message (such as a create or backup error), or an escaped block of JSON (used for health check results).

SubnetIds (list) --
The subnet IDs specified in a CreateServer request.

(string) --


ServerArn (string) --
The ARN of the server.









Exceptions

OpsWorksCM.Client.exceptions.InvalidStateException
OpsWorksCM.Client.exceptions.ResourceNotFoundException
OpsWorksCM.Client.exceptions.ValidationException


    :return: {
        'Server': {
            'AssociatePublicIpAddress': True|False,
            'BackupRetentionCount': 123,
            'ServerName': 'string',
            'CreatedAt': datetime(2015, 1, 1),
            'CloudFormationStackArn': 'string',
            'CustomDomain': 'string',
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
    CHEF_AUTOMATE_PIVOTAL_KEY : A base64-encoded RSA private key that is generated by AWS OpsWorks for Chef Automate. This private key is required to access the Chef API.
    CHEF_STARTER_KIT : A base64-encoded ZIP file. The ZIP file contains a Chef starter kit, which includes a README, a configuration file, and the required RSA private key. Save this file, unzip it, and then change to the directory where you\'ve unzipped the file contents. From this directory, you can run Knife commands.
    
    """
    pass

def tag_resource(ResourceArn=None, Tags=None):
    """
    Applies tags to an AWS OpsWorks for Chef Automate or AWS OpsWorks for Puppet Enterprise server, or to server backups.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        ResourceArn='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Number (ARN) of a resource to which you want to apply tags. For example, arn:aws:opsworks-cm:us-west-2:123456789012:server/test-owcm-server/EXAMPLE-66b0-4196-8274-d1a2bEXAMPLE .\n

    :type Tags: list
    :param Tags: [REQUIRED]\nA map that contains tag keys and tag values to attach to AWS OpsWorks-CM servers or backups.\n\nThe key cannot be empty.\nThe key can be a maximum of 127 characters, and can contain only Unicode letters, numbers, or separators, or the following special characters: + - = . _ : /\nThe value can be a maximum 255 characters, and contain only Unicode letters, numbers, or separators, or the following special characters: + - = . _ : /\nLeading and trailing white spaces are trimmed from both the key and value.\nA maximum of 50 user-applied tags is allowed for any AWS OpsWorks-CM server or backup.\n\n\n(dict) --A map that contains tag keys and tag values to attach to an AWS OpsWorks for Chef Automate or AWS OpsWorks for Puppet Enterprise server. Leading and trailing white spaces are trimmed from both the key and value. A maximum of 50 user-applied tags is allowed for tag-supported AWS OpsWorks-CM resources.\n\nKey (string) -- [REQUIRED]A tag key, such as Stage or Name . A tag key cannot be empty. The key can be a maximum of 127 characters, and can contain only Unicode letters, numbers, or separators, or the following special characters: + - = . _ : /\n\nValue (string) -- [REQUIRED]An optional tag value, such as Production or test-owcm-server . The value can be a maximum of 255 characters, and contain only Unicode letters, numbers, or separators, or the following special characters: + - = . _ : /\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

OpsWorksCM.Client.exceptions.ResourceNotFoundException
OpsWorksCM.Client.exceptions.ValidationException
OpsWorksCM.Client.exceptions.InvalidStateException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_resource(ResourceArn=None, TagKeys=None):
    """
    Removes specified tags from an AWS OpsWorks-CM server or backup.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        ResourceArn='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Number (ARN) of a resource from which you want to remove tags. For example, arn:aws:opsworks-cm:us-west-2:123456789012:server/test-owcm-server/EXAMPLE-66b0-4196-8274-d1a2bEXAMPLE .\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nThe keys of tags that you want to remove.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

OpsWorksCM.Client.exceptions.ResourceNotFoundException
OpsWorksCM.Client.exceptions.ValidationException
OpsWorksCM.Client.exceptions.InvalidStateException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_server(DisableAutomatedBackup=None, BackupRetentionCount=None, ServerName=None, PreferredMaintenanceWindow=None, PreferredBackupWindow=None):
    """
    Updates settings for a server.
    This operation is synchronous.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param ServerName: [REQUIRED]\nThe name of the server to update.\n

    :type PreferredMaintenanceWindow: string
    :param PreferredMaintenanceWindow: \nDDD:HH:MM (weekly start time) or HH:MM (daily start time).\nTime windows always use coordinated universal time (UTC). Valid strings for day of week (DDD ) are: Mon , Tue , Wed , Thr , Fri , Sat , or Sun .\n

    :type PreferredBackupWindow: string
    :param PreferredBackupWindow: \nDDD:HH:MM (weekly start time) or HH:MM (daily start time).\nTime windows always use coordinated universal time (UTC). Valid strings for day of week (DDD ) are: Mon , Tue , Wed , Thr , Fri , Sat , or Sun .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Server': {
        'AssociatePublicIpAddress': True|False,
        'BackupRetentionCount': 123,
        'ServerName': 'string',
        'CreatedAt': datetime(2015, 1, 1),
        'CloudFormationStackArn': 'string',
        'CustomDomain': 'string',
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


Response Structure

(dict) --

Server (dict) --
Contains the response to a UpdateServer request.

AssociatePublicIpAddress (boolean) --
Associate a public IP address with a server that you are launching.

BackupRetentionCount (integer) --
The number of automated backups to keep.

ServerName (string) --
The name of the server.

CreatedAt (datetime) --
Time stamp of server creation. Example 2016-07-29T13:38:47.520Z

CloudFormationStackArn (string) --
The ARN of the CloudFormation stack that was used to create the server.

CustomDomain (string) --
An optional public endpoint of a server, such as https://aws.my-company.com . You cannot access the server by using the Endpoint value if the server has a CustomDomain specified.

DisableAutomatedBackup (boolean) --
Disables automated backups. The number of stored backups is dependent on the value of PreferredBackupCount.

Endpoint (string) --
A DNS name that can be used to access the engine. Example: myserver-asdfghjkl.us-east-1.opsworks.io . You cannot access the server by using the Endpoint value if the server has a CustomDomain specified.

Engine (string) --
The engine type of the server. Valid values in this release include ChefAutomate and Puppet .

EngineModel (string) --
The engine model of the server. Valid values in this release include Monolithic for Puppet and Single for Chef.

EngineAttributes (list) --
The response of a createServer() request returns the master credential to access the server in EngineAttributes. These credentials are not stored by AWS OpsWorks CM; they are returned only as part of the result of createServer().

Attributes returned in a createServer response for Chef


CHEF_AUTOMATE_PIVOTAL_KEY : A base64-encoded RSA private key that is generated by AWS OpsWorks for Chef Automate. This private key is required to access the Chef API.
CHEF_STARTER_KIT : A base64-encoded ZIP file. The ZIP file contains a Chef starter kit, which includes a README, a configuration file, and the required RSA private key. Save this file, unzip it, and then change to the directory where you\'ve unzipped the file contents. From this directory, you can run Knife commands.


Attributes returned in a createServer response for Puppet


PUPPET_STARTER_KIT : A base64-encoded ZIP file. The ZIP file contains a Puppet starter kit, including a README and a required private key. Save this file, unzip it, and then change to the directory where you\'ve unzipped the file contents.
PUPPET_ADMIN_PASSWORD : An administrator password that you can use to sign in to the Puppet Enterprise console after the server is online.


(dict) --
A name and value pair that is specific to the engine of the server.

Name (string) --
The name of the engine attribute.

Value (string) --
The value of the engine attribute.





EngineVersion (string) --
The engine version of the server. For a Chef server, the valid value for EngineVersion is currently 12 . For a Puppet server, the valid value is 2017 .

InstanceProfileArn (string) --
The instance profile ARN of the server.

InstanceType (string) --
The instance type for the server, as specified in the CloudFormation stack. This might not be the same instance type that is shown in the EC2 console.

KeyPair (string) --
The key pair associated with the server.

MaintenanceStatus (string) --
The status of the most recent server maintenance run. Shows SUCCESS or FAILED .

PreferredMaintenanceWindow (string) --
The preferred maintenance period specified for the server.

PreferredBackupWindow (string) --
The preferred backup period specified for the server.

SecurityGroupIds (list) --
The security group IDs for the server, as specified in the CloudFormation stack. These might not be the same security groups that are shown in the EC2 console.

(string) --


ServiceRoleArn (string) --
The service role ARN used to create the server.

Status (string) --
The server\'s status. This field displays the states of actions in progress, such as creating, running, or backing up the server, as well as the server\'s health state.

StatusReason (string) --
Depending on the server status, this field has either a human-readable message (such as a create or backup error), or an escaped block of JSON (used for health check results).

SubnetIds (list) --
The subnet IDs specified in a CreateServer request.

(string) --


ServerArn (string) --
The ARN of the server.









Exceptions

OpsWorksCM.Client.exceptions.InvalidStateException
OpsWorksCM.Client.exceptions.ResourceNotFoundException
OpsWorksCM.Client.exceptions.ValidationException


    :return: {
        'Server': {
            'AssociatePublicIpAddress': True|False,
            'BackupRetentionCount': 123,
            'ServerName': 'string',
            'CreatedAt': datetime(2015, 1, 1),
            'CloudFormationStackArn': 'string',
            'CustomDomain': 'string',
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
    CHEF_AUTOMATE_PIVOTAL_KEY : A base64-encoded RSA private key that is generated by AWS OpsWorks for Chef Automate. This private key is required to access the Chef API.
    CHEF_STARTER_KIT : A base64-encoded ZIP file. The ZIP file contains a Chef starter kit, which includes a README, a configuration file, and the required RSA private key. Save this file, unzip it, and then change to the directory where you\'ve unzipped the file contents. From this directory, you can run Knife commands.
    
    """
    pass

def update_server_engine_attributes(ServerName=None, AttributeName=None, AttributeValue=None):
    """
    Updates engine-specific attributes on a specified server. The server enters the MODIFYING state when this operation is in progress. Only one update can occur at a time. You can use this command to reset a Chef server\'s public key (CHEF_PIVOTAL_KEY ) or a Puppet server\'s admin password (PUPPET_ADMIN_PASSWORD ).
    This operation is asynchronous.
    This operation can only be called for servers in HEALTHY or UNHEALTHY states. Otherwise, an InvalidStateException is raised. A ResourceNotFoundException is thrown when the server does not exist. A ValidationException is raised when parameters of the request are not valid.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_server_engine_attributes(
        ServerName='string',
        AttributeName='string',
        AttributeValue='string'
    )
    
    
    :type ServerName: string
    :param ServerName: [REQUIRED]\nThe name of the server to update.\n

    :type AttributeName: string
    :param AttributeName: [REQUIRED]\nThe name of the engine attribute to update.\n

    :type AttributeValue: string
    :param AttributeValue: The value to set for the attribute.

    :rtype: dict

ReturnsResponse Syntax
{
    'Server': {
        'AssociatePublicIpAddress': True|False,
        'BackupRetentionCount': 123,
        'ServerName': 'string',
        'CreatedAt': datetime(2015, 1, 1),
        'CloudFormationStackArn': 'string',
        'CustomDomain': 'string',
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


Response Structure

(dict) --

Server (dict) --
Contains the response to an UpdateServerEngineAttributes request.

AssociatePublicIpAddress (boolean) --
Associate a public IP address with a server that you are launching.

BackupRetentionCount (integer) --
The number of automated backups to keep.

ServerName (string) --
The name of the server.

CreatedAt (datetime) --
Time stamp of server creation. Example 2016-07-29T13:38:47.520Z

CloudFormationStackArn (string) --
The ARN of the CloudFormation stack that was used to create the server.

CustomDomain (string) --
An optional public endpoint of a server, such as https://aws.my-company.com . You cannot access the server by using the Endpoint value if the server has a CustomDomain specified.

DisableAutomatedBackup (boolean) --
Disables automated backups. The number of stored backups is dependent on the value of PreferredBackupCount.

Endpoint (string) --
A DNS name that can be used to access the engine. Example: myserver-asdfghjkl.us-east-1.opsworks.io . You cannot access the server by using the Endpoint value if the server has a CustomDomain specified.

Engine (string) --
The engine type of the server. Valid values in this release include ChefAutomate and Puppet .

EngineModel (string) --
The engine model of the server. Valid values in this release include Monolithic for Puppet and Single for Chef.

EngineAttributes (list) --
The response of a createServer() request returns the master credential to access the server in EngineAttributes. These credentials are not stored by AWS OpsWorks CM; they are returned only as part of the result of createServer().

Attributes returned in a createServer response for Chef


CHEF_AUTOMATE_PIVOTAL_KEY : A base64-encoded RSA private key that is generated by AWS OpsWorks for Chef Automate. This private key is required to access the Chef API.
CHEF_STARTER_KIT : A base64-encoded ZIP file. The ZIP file contains a Chef starter kit, which includes a README, a configuration file, and the required RSA private key. Save this file, unzip it, and then change to the directory where you\'ve unzipped the file contents. From this directory, you can run Knife commands.


Attributes returned in a createServer response for Puppet


PUPPET_STARTER_KIT : A base64-encoded ZIP file. The ZIP file contains a Puppet starter kit, including a README and a required private key. Save this file, unzip it, and then change to the directory where you\'ve unzipped the file contents.
PUPPET_ADMIN_PASSWORD : An administrator password that you can use to sign in to the Puppet Enterprise console after the server is online.


(dict) --
A name and value pair that is specific to the engine of the server.

Name (string) --
The name of the engine attribute.

Value (string) --
The value of the engine attribute.





EngineVersion (string) --
The engine version of the server. For a Chef server, the valid value for EngineVersion is currently 12 . For a Puppet server, the valid value is 2017 .

InstanceProfileArn (string) --
The instance profile ARN of the server.

InstanceType (string) --
The instance type for the server, as specified in the CloudFormation stack. This might not be the same instance type that is shown in the EC2 console.

KeyPair (string) --
The key pair associated with the server.

MaintenanceStatus (string) --
The status of the most recent server maintenance run. Shows SUCCESS or FAILED .

PreferredMaintenanceWindow (string) --
The preferred maintenance period specified for the server.

PreferredBackupWindow (string) --
The preferred backup period specified for the server.

SecurityGroupIds (list) --
The security group IDs for the server, as specified in the CloudFormation stack. These might not be the same security groups that are shown in the EC2 console.

(string) --


ServiceRoleArn (string) --
The service role ARN used to create the server.

Status (string) --
The server\'s status. This field displays the states of actions in progress, such as creating, running, or backing up the server, as well as the server\'s health state.

StatusReason (string) --
Depending on the server status, this field has either a human-readable message (such as a create or backup error), or an escaped block of JSON (used for health check results).

SubnetIds (list) --
The subnet IDs specified in a CreateServer request.

(string) --


ServerArn (string) --
The ARN of the server.









Exceptions

OpsWorksCM.Client.exceptions.InvalidStateException
OpsWorksCM.Client.exceptions.ResourceNotFoundException
OpsWorksCM.Client.exceptions.ValidationException


    :return: {
        'Server': {
            'AssociatePublicIpAddress': True|False,
            'BackupRetentionCount': 123,
            'ServerName': 'string',
            'CreatedAt': datetime(2015, 1, 1),
            'CloudFormationStackArn': 'string',
            'CustomDomain': 'string',
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
    CHEF_AUTOMATE_PIVOTAL_KEY : A base64-encoded RSA private key that is generated by AWS OpsWorks for Chef Automate. This private key is required to access the Chef API.
    CHEF_STARTER_KIT : A base64-encoded ZIP file. The ZIP file contains a Chef starter kit, which includes a README, a configuration file, and the required RSA private key. Save this file, unzip it, and then change to the directory where you\'ve unzipped the file contents. From this directory, you can run Knife commands.
    
    """
    pass

