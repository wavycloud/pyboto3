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


def add_tags_to_resource(ResourceArn=None, Tags=None):
    """
    :param ResourceArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the AWS DMS resource the tag is to be added to. AWS DMS resources include a replication instance, endpoint, and a replication task.
            
    :type ResourceArn: string
    :param Tags: [REQUIRED]
            The tag to be assigned to the DMS resource.
            (dict) --
            Key (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and cannot be prefixed with 'aws:' or 'dms:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            Value (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and cannot be prefixed with 'aws:' or 'dms:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            
            
    :type Tags: list
    """
    pass


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


def create_endpoint(EndpointIdentifier=None, EndpointType=None, EngineName=None, Username=None, Password=None,
                    ServerName=None, Port=None, DatabaseName=None, ExtraConnectionAttributes=None, KmsKeyId=None,
                    Tags=None, CertificateArn=None, SslMode=None):
    """
    :param EndpointIdentifier: [REQUIRED]
            The database endpoint identifier. Identifiers must begin with a letter; must contain only ASCII letters, digits, and hyphens; and must not end with a hyphen or contain two consecutive hyphens.
            
    :type EndpointIdentifier: string
    :param EndpointType: [REQUIRED]
            The type of endpoint.
            
    :type EndpointType: string
    :param EngineName: [REQUIRED]
            The type of engine for the endpoint. Valid values include MYSQL, ORACLE, POSTGRES, MARIADB, AURORA, REDSHIFT, and SQLSERVER.
            
    :type EngineName: string
    :param Username: [REQUIRED]
            The user name to be used to login to the endpoint database.
            
    :type Username: string
    :param Password: [REQUIRED]
            The password to be used to login to the endpoint database.
            
    :type Password: string
    :param ServerName: [REQUIRED]
            The name of the server where the endpoint database resides.
            
    :type ServerName: string
    :param Port: [REQUIRED]
            The port used by the endpoint database.
            
    :type Port: integer
    :param DatabaseName: The name of the endpoint database.
    :type DatabaseName: string
    :param ExtraConnectionAttributes: Additional attributes associated with the connection.
    :type ExtraConnectionAttributes: string
    :param KmsKeyId: The KMS key identifier that will be used to encrypt the connection parameters. If you do not specify a value for the KmsKeyId parameter, then AWS DMS will use your default encryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS region.
    :type KmsKeyId: string
    :param Tags: Tags to be added to the endpoint.
            (dict) --
            Key (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and cannot be prefixed with 'aws:' or 'dms:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            Value (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and cannot be prefixed with 'aws:' or 'dms:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            
            
    :type Tags: list
    :param CertificateArn: The Amazon Resource Number (ARN) for the certificate.
    :type CertificateArn: string
    :param SslMode: The SSL mode to use for the SSL connection.
            SSL mode can be one of four values: none, require, verify-ca, verify-full.
            The default value is none.
            
    :type SslMode: string
    """
    pass


def create_replication_instance(ReplicationInstanceIdentifier=None, AllocatedStorage=None,
                                ReplicationInstanceClass=None, VpcSecurityGroupIds=None, AvailabilityZone=None,
                                ReplicationSubnetGroupIdentifier=None, PreferredMaintenanceWindow=None, MultiAZ=None,
                                EngineVersion=None, AutoMinorVersionUpgrade=None, Tags=None, KmsKeyId=None,
                                PubliclyAccessible=None):
    """
    :param ReplicationInstanceIdentifier: [REQUIRED]
            The replication instance identifier. This parameter is stored as a lowercase string.
            Constraints:
            Must contain from 1 to 63 alphanumeric characters or hyphens.
            First character must be a letter.
            Cannot end with a hyphen or contain two consecutive hyphens.
            Example: myrepinstance
            
    :type ReplicationInstanceIdentifier: string
    :param AllocatedStorage: The amount of storage (in gigabytes) to be initially allocated for the replication instance.
    :type AllocatedStorage: integer
    :param ReplicationInstanceClass: [REQUIRED]
            The compute and memory capacity of the replication instance as specified by the replication instance class.
            Valid Values: dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge
            
    :type ReplicationInstanceClass: string
    :param VpcSecurityGroupIds: Specifies the VPC security group to be used with the replication instance. The VPC security group must work with the VPC containing the replication instance.
            (string) --
            
    :type VpcSecurityGroupIds: list
    :param AvailabilityZone: The EC2 Availability Zone that the replication instance will be created in.
            Default: A random, system-chosen Availability Zone in the endpoint's region.
            Example: us-east-1d
            
    :type AvailabilityZone: string
    :param ReplicationSubnetGroupIdentifier: A subnet group to associate with the replication instance.
    :type ReplicationSubnetGroupIdentifier: string
    :param PreferredMaintenanceWindow: The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).
            Format: ddd:hh24:mi-ddd:hh24:mi
            Default: A 30-minute window selected at random from an 8-hour block of time per region, occurring on a random day of the week.
            Valid Days: Mon, Tue, Wed, Thu, Fri, Sat, Sun
            Constraints: Minimum 30-minute window.
            
    :type PreferredMaintenanceWindow: string
    :param MultiAZ: Specifies if the replication instance is a Multi-AZ deployment. You cannot set the AvailabilityZone parameter if the Multi-AZ parameter is set to true .
    :type MultiAZ: boolean
    :param EngineVersion: The engine version number of the replication instance.
    :type EngineVersion: string
    :param AutoMinorVersionUpgrade: Indicates that minor engine upgrades will be applied automatically to the replication instance during the maintenance window.
            Default: true
            
    :type AutoMinorVersionUpgrade: boolean
    :param Tags: Tags to be associated with the replication instance.
            (dict) --
            Key (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and cannot be prefixed with 'aws:' or 'dms:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            Value (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and cannot be prefixed with 'aws:' or 'dms:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            
            
    :type Tags: list
    :param KmsKeyId: The KMS key identifier that will be used to encrypt the content on the replication instance. If you do not specify a value for the KmsKeyId parameter, then AWS DMS will use your default encryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS region.
    :type KmsKeyId: string
    :param PubliclyAccessible: Specifies the accessibility options for the replication instance. A value of true represents an instance with a public IP address. A value of false represents an instance with a private IP address. The default value is true .
    :type PubliclyAccessible: boolean
    """
    pass


def create_replication_subnet_group(ReplicationSubnetGroupIdentifier=None, ReplicationSubnetGroupDescription=None,
                                    SubnetIds=None, Tags=None):
    """
    :param ReplicationSubnetGroupIdentifier: [REQUIRED]
            The name for the replication subnet group. This value is stored as a lowercase string.
            Constraints: Must contain no more than 255 alphanumeric characters, periods, spaces, underscores, or hyphens. Must not be 'default'.
            Example: mySubnetgroup
            
    :type ReplicationSubnetGroupIdentifier: string
    :param ReplicationSubnetGroupDescription: [REQUIRED]
            The description for the subnet group.
            
    :type ReplicationSubnetGroupDescription: string
    :param SubnetIds: [REQUIRED]
            The EC2 subnet IDs for the subnet group.
            (string) --
            
    :type SubnetIds: list
    :param Tags: The tag to be assigned to the subnet group.
            (dict) --
            Key (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and cannot be prefixed with 'aws:' or 'dms:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            Value (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and cannot be prefixed with 'aws:' or 'dms:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            
            
    :type Tags: list
    """
    pass


def create_replication_task(ReplicationTaskIdentifier=None, SourceEndpointArn=None, TargetEndpointArn=None,
                            ReplicationInstanceArn=None, MigrationType=None, TableMappings=None,
                            ReplicationTaskSettings=None, CdcStartTime=None, Tags=None):
    """
    :param ReplicationTaskIdentifier: [REQUIRED]
            The replication task identifier.
            Constraints:
            Must contain from 1 to 63 alphanumeric characters or hyphens.
            First character must be a letter.
            Cannot end with a hyphen or contain two consecutive hyphens.
            
    :type ReplicationTaskIdentifier: string
    :param SourceEndpointArn: [REQUIRED]
            The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.
            
    :type SourceEndpointArn: string
    :param TargetEndpointArn: [REQUIRED]
            The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.
            
    :type TargetEndpointArn: string
    :param ReplicationInstanceArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the replication instance.
            
    :type ReplicationInstanceArn: string
    :param MigrationType: [REQUIRED]
            The migration type.
            
    :type MigrationType: string
    :param TableMappings: [REQUIRED]
            The path of the JSON file that contains the table mappings. Preceed the path with 'file://'.
            For example, --table-mappings file://mappingfile.json
            
    :type TableMappings: string
    :param ReplicationTaskSettings: Settings for the task, such as target metadata settings.
    :type ReplicationTaskSettings: string
    :param CdcStartTime: The start time for the Change Data Capture (CDC) operation.
    :type CdcStartTime: datetime
    :param Tags: Tags to be added to the replication instance.
            (dict) --
            Key (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and cannot be prefixed with 'aws:' or 'dms:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            Value (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and cannot be prefixed with 'aws:' or 'dms:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            
            
    :type Tags: list
    """
    pass


def delete_certificate(CertificateArn=None):
    """
    :param CertificateArn: [REQUIRED]
            the Amazon Resource Name (ARN) of the deleted certificate.
            Return typedict
            ReturnsResponse Syntax{
              'Certificate': {
                'CertificateIdentifier': 'string',
                'CertificateCreationDate': datetime(2015, 1, 1),
                'CertificatePem': 'string',
                'CertificateArn': 'string',
                'CertificateOwner': 'string',
                'ValidFromDate': datetime(2015, 1, 1),
                'ValidToDate': datetime(2015, 1, 1),
                'SigningAlgorithm': 'string',
                'KeyLength': 123
              }
            }
            Response Structure
            (dict) --
            Certificate (dict) --The SSL certificate.
            CertificateIdentifier (string) --The customer-assigned name of the certificate. Valid characters are [A-z_0-9].
            CertificateCreationDate (datetime) --the date the certificate was created.
            CertificatePem (string) --The contents of the .pem X.509 certificate file.
            CertificateArn (string) --The Amazon Resource Name (ARN) for the certificate.
            CertificateOwner (string) --The owner of the certificate.
            ValidFromDate (datetime) --The beginning date the certificate is valid.
            ValidToDate (datetime) --the final date the certificate is valid.
            SigningAlgorithm (string) --The signing algorithm for the certificate.
            KeyLength (integer) --The key length of the cryptographic algorithm being used.
            
            
            
    :type CertificateArn: string
    """
    pass


def delete_endpoint(EndpointArn=None):
    """
    :param EndpointArn: [REQUIRED]
            The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.
            Return typedict
            ReturnsResponse Syntax{
              'Endpoint': {
                'EndpointIdentifier': 'string',
                'EndpointType': 'source'|'target',
                'EngineName': 'string',
                'Username': 'string',
                'ServerName': 'string',
                'Port': 123,
                'DatabaseName': 'string',
                'ExtraConnectionAttributes': 'string',
                'Status': 'string',
                'KmsKeyId': 'string',
                'EndpointArn': 'string',
                'CertificateArn': 'string',
                'SslMode': 'none'|'require'|'verify-ca'|'verify-full'
              }
            }
            Response Structure
            (dict) --
            Endpoint (dict) --The endpoint that was deleted.
            EndpointIdentifier (string) --The database endpoint identifier. Identifiers must begin with a letter; must contain only ASCII letters, digits, and hyphens; and must not end with a hyphen or contain two consecutive hyphens.
            EndpointType (string) --The type of endpoint.
            EngineName (string) --The database engine name.
            Username (string) --The user name used to connect to the endpoint.
            ServerName (string) --The name of the server at the endpoint.
            Port (integer) --The port value used to access the endpoint.
            DatabaseName (string) --The name of the database at the endpoint.
            ExtraConnectionAttributes (string) --Additional connection attributes used to connect to the endpoint.
            Status (string) --The status of the endpoint.
            KmsKeyId (string) --The KMS key identifier that will be used to encrypt the connection parameters. If you do not specify a value for the KmsKeyId parameter, then AWS DMS will use your default encryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS region.
            EndpointArn (string) --The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.
            CertificateArn (string) --The Amazon Resource Name (ARN) used for SSL connection to the endpoint.
            SslMode (string) --The SSL mode used to connect to the endpoint.
            SSL mode can be one of four values: none, require, verify-ca, verify-full.
            The default value is none.
            
            
            
    :type EndpointArn: string
    """
    pass


def delete_replication_instance(ReplicationInstanceArn=None):
    """
    :param ReplicationInstanceArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the replication instance to be deleted.
            Return typedict
            ReturnsResponse Syntax{
              'ReplicationInstance': {
                'ReplicationInstanceIdentifier': 'string',
                'ReplicationInstanceClass': 'string',
                'ReplicationInstanceStatus': 'string',
                'AllocatedStorage': 123,
                'InstanceCreateTime': datetime(2015, 1, 1),
                'VpcSecurityGroups': [
                  {
                    'VpcSecurityGroupId': 'string',
                    'Status': 'string'
                  },
                ],
                'AvailabilityZone': 'string',
                'ReplicationSubnetGroup': {
                  'ReplicationSubnetGroupIdentifier': 'string',
                  'ReplicationSubnetGroupDescription': 'string',
                  'VpcId': 'string',
                  'SubnetGroupStatus': 'string',
                  'Subnets': [
                    {
                      'SubnetIdentifier': 'string',
                      'SubnetAvailabilityZone': {
                        'Name': 'string'
                      },
                      'SubnetStatus': 'string'
                    },
                  ]
                },
                'PreferredMaintenanceWindow': 'string',
                'PendingModifiedValues': {
                  'ReplicationInstanceClass': 'string',
                  'AllocatedStorage': 123,
                  'MultiAZ': True|False,
                  'EngineVersion': 'string'
                },
                'MultiAZ': True|False,
                'EngineVersion': 'string',
                'AutoMinorVersionUpgrade': True|False,
                'KmsKeyId': 'string',
                'ReplicationInstanceArn': 'string',
                'ReplicationInstancePublicIpAddress': 'string',
                'ReplicationInstancePrivateIpAddress': 'string',
                'ReplicationInstancePublicIpAddresses': [
                  'string',
                ],
                'ReplicationInstancePrivateIpAddresses': [
                  'string',
                ],
                'PubliclyAccessible': True|False
              }
            }
            Response Structure
            (dict) --
            ReplicationInstance (dict) --The replication instance that was deleted.
            ReplicationInstanceIdentifier (string) --The replication instance identifier. This parameter is stored as a lowercase string.
            Constraints:
            Must contain from 1 to 63 alphanumeric characters or hyphens.
            First character must be a letter.
            Cannot end with a hyphen or contain two consecutive hyphens.
            Example: myrepinstance
            ReplicationInstanceClass (string) --The compute and memory capacity of the replication instance.
            Valid Values: dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge
            ReplicationInstanceStatus (string) --The status of the replication instance.
            AllocatedStorage (integer) --The amount of storage (in gigabytes) that is allocated for the replication instance.
            InstanceCreateTime (datetime) --The time the replication instance was created.
            VpcSecurityGroups (list) --The VPC security group for the instance.
            (dict) --
            VpcSecurityGroupId (string) --The VPC security group Id.
            Status (string) --The status of the VPC security group.
            
            AvailabilityZone (string) --The Availability Zone for the instance.
            ReplicationSubnetGroup (dict) --The subnet group for the replication instance.
            ReplicationSubnetGroupIdentifier (string) --The identifier of the replication instance subnet group.
            ReplicationSubnetGroupDescription (string) --The description of the replication subnet group.
            VpcId (string) --The ID of the VPC.
            SubnetGroupStatus (string) --The status of the subnet group.
            Subnets (list) --The subnets that are in the subnet group.
            (dict) --
            SubnetIdentifier (string) --The subnet identifier.
            SubnetAvailabilityZone (dict) --The Availability Zone of the subnet.
            Name (string) --The name of the availability zone.
            SubnetStatus (string) --The status of the subnet.
            
            PreferredMaintenanceWindow (string) --The maintenance window times for the replication instance.
            PendingModifiedValues (dict) --The pending modification values.
            ReplicationInstanceClass (string) --The compute and memory capacity of the replication instance.
            Valid Values: dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge
            AllocatedStorage (integer) --The amount of storage (in gigabytes) that is allocated for the replication instance.
            MultiAZ (boolean) --Specifies if the replication instance is a Multi-AZ deployment. You cannot set the AvailabilityZone parameter if the Multi-AZ parameter is set to true .
            EngineVersion (string) --The engine version number of the replication instance.
            MultiAZ (boolean) --Specifies if the replication instance is a Multi-AZ deployment. You cannot set the AvailabilityZone parameter if the Multi-AZ parameter is set to true .
            EngineVersion (string) --The engine version number of the replication instance.
            AutoMinorVersionUpgrade (boolean) --Boolean value indicating if minor version upgrades will be automatically applied to the instance.
            KmsKeyId (string) --The KMS key identifier that is used to encrypt the content on the replication instance. If you do not specify a value for the KmsKeyId parameter, then AWS DMS will use your default encryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS region.
            ReplicationInstanceArn (string) --The Amazon Resource Name (ARN) of the replication instance.
            ReplicationInstancePublicIpAddress (string) --The public IP address of the replication instance.
            ReplicationInstancePrivateIpAddress (string) --The private IP address of the replication instance.
            ReplicationInstancePublicIpAddresses (list) --The public IP address of the replication instance.
            (string) --
            ReplicationInstancePrivateIpAddresses (list) --The private IP address of the replication instance.
            (string) --
            PubliclyAccessible (boolean) --Specifies the accessibility options for the replication instance. A value of true represents an instance with a public IP address. A value of false represents an instance with a private IP address. The default value is true .
            
            
            
    :type ReplicationInstanceArn: string
    """
    pass


def delete_replication_subnet_group(ReplicationSubnetGroupIdentifier=None):
    """
    :param ReplicationSubnetGroupIdentifier: [REQUIRED]
            The subnet group name of the replication instance.
            Return typedict
            ReturnsResponse Syntax{}
            Response Structure
            (dict) --
            
    :type ReplicationSubnetGroupIdentifier: string
    """
    pass


def delete_replication_task(ReplicationTaskArn=None):
    """
    :param ReplicationTaskArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the replication task to be deleted.
            Return typedict
            ReturnsResponse Syntax{
              'ReplicationTask': {
                'ReplicationTaskIdentifier': 'string',
                'SourceEndpointArn': 'string',
                'TargetEndpointArn': 'string',
                'ReplicationInstanceArn': 'string',
                'MigrationType': 'full-load'|'cdc'|'full-load-and-cdc',
                'TableMappings': 'string',
                'ReplicationTaskSettings': 'string',
                'Status': 'string',
                'LastFailureMessage': 'string',
                'ReplicationTaskCreationDate': datetime(2015, 1, 1),
                'ReplicationTaskStartDate': datetime(2015, 1, 1),
                'ReplicationTaskArn': 'string',
                'ReplicationTaskStats': {
                  'FullLoadProgressPercent': 123,
                  'ElapsedTimeMillis': 123,
                  'TablesLoaded': 123,
                  'TablesLoading': 123,
                  'TablesQueued': 123,
                  'TablesErrored': 123
                }
              }
            }
            Response Structure
            (dict) --
            ReplicationTask (dict) --The deleted replication task.
            ReplicationTaskIdentifier (string) --The replication task identifier.
            Constraints:
            Must contain from 1 to 63 alphanumeric characters or hyphens.
            First character must be a letter.
            Cannot end with a hyphen or contain two consecutive hyphens.
            SourceEndpointArn (string) --The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.
            TargetEndpointArn (string) --The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.
            ReplicationInstanceArn (string) --The Amazon Resource Name (ARN) of the replication instance.
            MigrationType (string) --The type of migration.
            TableMappings (string) --Table mappings specified in the task.
            ReplicationTaskSettings (string) --The settings for the replication task.
            Status (string) --The status of the replication task.
            LastFailureMessage (string) --The last error (failure) message generated for the replication instance.
            ReplicationTaskCreationDate (datetime) --The date the replication task was created.
            ReplicationTaskStartDate (datetime) --The date the replication task is scheduled to start.
            ReplicationTaskArn (string) --The Amazon Resource Name (ARN) of the replication task.
            ReplicationTaskStats (dict) --The statistics for the task, including elapsed time, tables loaded, and table errors.
            FullLoadProgressPercent (integer) --The percent complete for the full load migration task.
            ElapsedTimeMillis (integer) --The elapsed time of the task, in milliseconds.
            TablesLoaded (integer) --The number of tables loaded for this task.
            TablesLoading (integer) --The number of tables currently loading for this task.
            TablesQueued (integer) --The number of tables queued for this task.
            TablesErrored (integer) --The number of errors that have occurred during this task.
            
            
            
    :type ReplicationTaskArn: string
    """
    pass


def describe_account_attributes():
    """
    """
    pass


def describe_certificates(Filters=None, MaxRecords=None, Marker=None):
    """
    :param Filters: Filters applied to the certificate described in the form of key-value pairs.
            (dict) --
            Name (string) -- [REQUIRED]The name of the filter.
            Values (list) -- [REQUIRED]The filter value.
            (string) --
            
            
    :type Filters: list
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
            Default: 10
            
    :type MaxRecords: integer
    :param Marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .
    :type Marker: string
    """
    pass


def describe_connections(Filters=None, MaxRecords=None, Marker=None):
    """
    :param Filters: The filters applied to the connection.
            Valid filter names: endpoint-arn | replication-instance-arn
            (dict) --
            Name (string) -- [REQUIRED]The name of the filter.
            Values (list) -- [REQUIRED]The filter value.
            (string) --
            
            
    :type Filters: list
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: Minimum 20, maximum 100.
            
    :type MaxRecords: integer
    :param Marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .
    :type Marker: string
    """
    pass


def describe_endpoint_types(Filters=None, MaxRecords=None, Marker=None):
    """
    :param Filters: Filters applied to the describe action.
            Valid filter names: engine-name | endpoint-type
            (dict) --
            Name (string) -- [REQUIRED]The name of the filter.
            Values (list) -- [REQUIRED]The filter value.
            (string) --
            
            
    :type Filters: list
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: Minimum 20, maximum 100.
            
    :type MaxRecords: integer
    :param Marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .
    :type Marker: string
    """
    pass


def describe_endpoints(Filters=None, MaxRecords=None, Marker=None):
    """
    :param Filters: Filters applied to the describe action.
            Valid filter names: endpoint-arn | endpoint-type | endpoint-id | engine-name
            (dict) --
            Name (string) -- [REQUIRED]The name of the filter.
            Values (list) -- [REQUIRED]The filter value.
            (string) --
            
            
    :type Filters: list
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: Minimum 20, maximum 100.
            
    :type MaxRecords: integer
    :param Marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .
    :type Marker: string
    """
    pass


def describe_orderable_replication_instances(MaxRecords=None, Marker=None):
    """
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: Minimum 20, maximum 100.
            
    :type MaxRecords: integer
    :param Marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .
    :type Marker: string
    """
    pass


def describe_refresh_schemas_status(EndpointArn=None):
    """
    :param EndpointArn: [REQUIRED]
            The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.
            Return typedict
            ReturnsResponse Syntax{
              'RefreshSchemasStatus': {
                'EndpointArn': 'string',
                'ReplicationInstanceArn': 'string',
                'Status': 'successful'|'failed'|'refreshing',
                'LastRefreshDate': datetime(2015, 1, 1),
                'LastFailureMessage': 'string'
              }
            }
            Response Structure
            (dict) --
            RefreshSchemasStatus (dict) --The status of the schema.
            EndpointArn (string) --The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.
            ReplicationInstanceArn (string) --The Amazon Resource Name (ARN) of the replication instance.
            Status (string) --The status of the schema.
            LastRefreshDate (datetime) --The date the schema was last refreshed.
            LastFailureMessage (string) --The last failure message for the schema.
            
            
            
    :type EndpointArn: string
    """
    pass


def describe_replication_instances(Filters=None, MaxRecords=None, Marker=None):
    """
    :param Filters: Filters applied to the describe action.
            Valid filter names: replication-instance-arn | replication-instance-id | replication-instance-class | engine-version
            (dict) --
            Name (string) -- [REQUIRED]The name of the filter.
            Values (list) -- [REQUIRED]The filter value.
            (string) --
            
            
    :type Filters: list
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: Minimum 20, maximum 100.
            
    :type MaxRecords: integer
    :param Marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .
    :type Marker: string
    """
    pass


def describe_replication_subnet_groups(Filters=None, MaxRecords=None, Marker=None):
    """
    :param Filters: Filters applied to the describe action.
            (dict) --
            Name (string) -- [REQUIRED]The name of the filter.
            Values (list) -- [REQUIRED]The filter value.
            (string) --
            
            
    :type Filters: list
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: Minimum 20, maximum 100.
            
    :type MaxRecords: integer
    :param Marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .
    :type Marker: string
    """
    pass


def describe_replication_tasks(Filters=None, MaxRecords=None, Marker=None):
    """
    :param Filters: Filters applied to the describe action.
            Valid filter names: replication-task-arn | replication-task-id | migration-type | endpoint-arn | replication-instance-arn
            (dict) --
            Name (string) -- [REQUIRED]The name of the filter.
            Values (list) -- [REQUIRED]The filter value.
            (string) --
            
            
    :type Filters: list
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: Minimum 20, maximum 100.
            
    :type MaxRecords: integer
    :param Marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .
    :type Marker: string
    """
    pass


def describe_schemas(EndpointArn=None, MaxRecords=None, Marker=None):
    """
    :param EndpointArn: [REQUIRED]
            The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.
            
    :type EndpointArn: string
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: Minimum 20, maximum 100.
            
    :type MaxRecords: integer
    :param Marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .
    :type Marker: string
    """
    pass


def describe_table_statistics(ReplicationTaskArn=None, MaxRecords=None, Marker=None):
    """
    :param ReplicationTaskArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the replication task.
            
    :type ReplicationTaskArn: string
    :param MaxRecords: The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
            Default: 100
            Constraints: Minimum 20, maximum 100.
            
    :type MaxRecords: integer
    :param Marker: An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords .
    :type Marker: string
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


def get_waiter():
    """
    """
    pass


def import_certificate(CertificateIdentifier=None, CertificatePem=None):
    """
    :param CertificateIdentifier: [REQUIRED]
            The customer-assigned name of the certificate. Valid characters are [A-z_0-9].
            
    :type CertificateIdentifier: string
    :param CertificatePem: The contents of the .pem X.509 certificate file.
    :type CertificatePem: string
    """
    pass


def list_tags_for_resource(ResourceArn=None):
    """
    :param ResourceArn: [REQUIRED]
            The Amazon Resource Name (ARN) string that uniquely identifies the AWS DMS resource.
            Return typedict
            ReturnsResponse Syntax{
              'TagList': [
                {
                  'Key': 'string',
                  'Value': 'string'
                },
              ]
            }
            Response Structure
            (dict) --
            TagList (list) --A list of tags for the resource.
            (dict) --
            Key (string) --A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and cannot be prefixed with 'aws:' or 'dms:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            Value (string) --A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and cannot be prefixed with 'aws:' or 'dms:'. The string can only contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-' (Java regex: '^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$').
            
            
            
    :type ResourceArn: string
    """
    pass


def modify_endpoint(EndpointArn=None, EndpointIdentifier=None, EndpointType=None, EngineName=None, Username=None,
                    Password=None, ServerName=None, Port=None, DatabaseName=None, ExtraConnectionAttributes=None,
                    CertificateArn=None, SslMode=None):
    """
    :param EndpointArn: [REQUIRED]
            The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.
            
    :type EndpointArn: string
    :param EndpointIdentifier: The database endpoint identifier. Identifiers must begin with a letter; must contain only ASCII letters, digits, and hyphens; and must not end with a hyphen or contain two consecutive hyphens.
    :type EndpointIdentifier: string
    :param EndpointType: The type of endpoint.
    :type EndpointType: string
    :param EngineName: The type of engine for the endpoint. Valid values include MYSQL, ORACLE, POSTGRES, MARIADB, AURORA, REDSHIFT, and SQLSERVER.
    :type EngineName: string
    :param Username: The user name to be used to login to the endpoint database.
    :type Username: string
    :param Password: The password to be used to login to the endpoint database.
    :type Password: string
    :param ServerName: The name of the server where the endpoint database resides.
    :type ServerName: string
    :param Port: The port used by the endpoint database.
    :type Port: integer
    :param DatabaseName: The name of the endpoint database.
    :type DatabaseName: string
    :param ExtraConnectionAttributes: Additional attributes associated with the connection.
    :type ExtraConnectionAttributes: string
    :param CertificateArn: The Amazon Resource Name (ARN) of the certificate used for SSL connection.
    :type CertificateArn: string
    :param SslMode: The SSL mode to be used.
            SSL mode can be one of four values: none, require, verify-ca, verify-full.
            The default value is none.
            
    :type SslMode: string
    """
    pass


def modify_replication_instance(ReplicationInstanceArn=None, AllocatedStorage=None, ApplyImmediately=None,
                                ReplicationInstanceClass=None, VpcSecurityGroupIds=None,
                                PreferredMaintenanceWindow=None, MultiAZ=None, EngineVersion=None,
                                AllowMajorVersionUpgrade=None, AutoMinorVersionUpgrade=None,
                                ReplicationInstanceIdentifier=None):
    """
    :param ReplicationInstanceArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the replication instance.
            
    :type ReplicationInstanceArn: string
    :param AllocatedStorage: The amount of storage (in gigabytes) to be allocated for the replication instance.
    :type AllocatedStorage: integer
    :param ApplyImmediately: Indicates whether the changes should be applied immediately or during the next maintenance window.
    :type ApplyImmediately: boolean
    :param ReplicationInstanceClass: The compute and memory capacity of the replication instance.
            Valid Values: dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge
            
    :type ReplicationInstanceClass: string
    :param VpcSecurityGroupIds: Specifies the VPC security group to be used with the replication instance. The VPC security group must work with the VPC containing the replication instance.
            (string) --
            
    :type VpcSecurityGroupIds: list
    :param PreferredMaintenanceWindow: The weekly time range (in UTC) during which system maintenance can occur, which might result in an outage. Changing this parameter does not result in an outage, except in the following situation, and the change is asynchronously applied as soon as possible. If moving this window to the current time, there must be at least 30 minutes between the current time and end of the window to ensure pending changes are applied.
            Default: Uses existing setting
            Format: ddd:hh24:mi-ddd:hh24:mi
            Valid Days: Mon | Tue | Wed | Thu | Fri | Sat | Sun
            Constraints: Must be at least 30 minutes
            
    :type PreferredMaintenanceWindow: string
    :param MultiAZ: Specifies if the replication instance is a Multi-AZ deployment. You cannot set the AvailabilityZone parameter if the Multi-AZ parameter is set to true .
    :type MultiAZ: boolean
    :param EngineVersion: The engine version number of the replication instance.
    :type EngineVersion: string
    :param AllowMajorVersionUpgrade: Indicates that major version upgrades are allowed. Changing this parameter does not result in an outage and the change is asynchronously applied as soon as possible.
            Constraints: This parameter must be set to true when specifying a value for the EngineVersion parameter that is a different major version than the replication instance's current version.
            
    :type AllowMajorVersionUpgrade: boolean
    :param AutoMinorVersionUpgrade: Indicates that minor version upgrades will be applied automatically to the replication instance during the maintenance window. Changing this parameter does not result in an outage except in the following case and the change is asynchronously applied as soon as possible. An outage will result if this parameter is set to true during the maintenance window, and a newer minor version is available, and AWS DMS has enabled auto patching for that engine version.
    :type AutoMinorVersionUpgrade: boolean
    :param ReplicationInstanceIdentifier: The replication instance identifier. This parameter is stored as a lowercase string.
    :type ReplicationInstanceIdentifier: string
    """
    pass


def modify_replication_subnet_group(ReplicationSubnetGroupIdentifier=None, ReplicationSubnetGroupDescription=None,
                                    SubnetIds=None):
    """
    :param ReplicationSubnetGroupIdentifier: [REQUIRED]
            The name of the replication instance subnet group.
            
    :type ReplicationSubnetGroupIdentifier: string
    :param ReplicationSubnetGroupDescription: The description of the replication instance subnet group.
    :type ReplicationSubnetGroupDescription: string
    :param SubnetIds: [REQUIRED]
            A list of subnet IDs.
            (string) --
            
    :type SubnetIds: list
    """
    pass


def refresh_schemas(EndpointArn=None, ReplicationInstanceArn=None):
    """
    :param EndpointArn: [REQUIRED]
            The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.
            
    :type EndpointArn: string
    :param ReplicationInstanceArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the replication instance.
            
    :type ReplicationInstanceArn: string
    """
    pass


def remove_tags_from_resource(ResourceArn=None, TagKeys=None):
    """
    :param ResourceArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the AWS DMS resource the tag is to be removed from.
            
    :type ResourceArn: string
    :param TagKeys: [REQUIRED]
            The tag key (name) of the tag to be removed.
            (string) --
            
    :type TagKeys: list
    """
    pass


def start_replication_task(ReplicationTaskArn=None, StartReplicationTaskType=None, CdcStartTime=None):
    """
    :param ReplicationTaskArn: [REQUIRED]
            The Amazon Resource Number (ARN) of the replication task to be started.
            
    :type ReplicationTaskArn: string
    :param StartReplicationTaskType: [REQUIRED]
            The type of replication task.
            
    :type StartReplicationTaskType: string
    :param CdcStartTime: The start time for the Change Data Capture (CDC) operation.
    :type CdcStartTime: datetime
    """
    pass


def stop_replication_task(ReplicationTaskArn=None):
    """
    :param ReplicationTaskArn: [REQUIRED]
            The Amazon Resource Number(ARN) of the replication task to be stopped.
            Return typedict
            ReturnsResponse Syntax{
              'ReplicationTask': {
                'ReplicationTaskIdentifier': 'string',
                'SourceEndpointArn': 'string',
                'TargetEndpointArn': 'string',
                'ReplicationInstanceArn': 'string',
                'MigrationType': 'full-load'|'cdc'|'full-load-and-cdc',
                'TableMappings': 'string',
                'ReplicationTaskSettings': 'string',
                'Status': 'string',
                'LastFailureMessage': 'string',
                'ReplicationTaskCreationDate': datetime(2015, 1, 1),
                'ReplicationTaskStartDate': datetime(2015, 1, 1),
                'ReplicationTaskArn': 'string',
                'ReplicationTaskStats': {
                  'FullLoadProgressPercent': 123,
                  'ElapsedTimeMillis': 123,
                  'TablesLoaded': 123,
                  'TablesLoading': 123,
                  'TablesQueued': 123,
                  'TablesErrored': 123
                }
              }
            }
            Response Structure
            (dict) --
            ReplicationTask (dict) --The replication task stopped.
            ReplicationTaskIdentifier (string) --The replication task identifier.
            Constraints:
            Must contain from 1 to 63 alphanumeric characters or hyphens.
            First character must be a letter.
            Cannot end with a hyphen or contain two consecutive hyphens.
            SourceEndpointArn (string) --The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.
            TargetEndpointArn (string) --The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.
            ReplicationInstanceArn (string) --The Amazon Resource Name (ARN) of the replication instance.
            MigrationType (string) --The type of migration.
            TableMappings (string) --Table mappings specified in the task.
            ReplicationTaskSettings (string) --The settings for the replication task.
            Status (string) --The status of the replication task.
            LastFailureMessage (string) --The last error (failure) message generated for the replication instance.
            ReplicationTaskCreationDate (datetime) --The date the replication task was created.
            ReplicationTaskStartDate (datetime) --The date the replication task is scheduled to start.
            ReplicationTaskArn (string) --The Amazon Resource Name (ARN) of the replication task.
            ReplicationTaskStats (dict) --The statistics for the task, including elapsed time, tables loaded, and table errors.
            FullLoadProgressPercent (integer) --The percent complete for the full load migration task.
            ElapsedTimeMillis (integer) --The elapsed time of the task, in milliseconds.
            TablesLoaded (integer) --The number of tables loaded for this task.
            TablesLoading (integer) --The number of tables currently loading for this task.
            TablesQueued (integer) --The number of tables queued for this task.
            TablesErrored (integer) --The number of errors that have occurred during this task.
            
            
            
    :type ReplicationTaskArn: string
    """
    pass


def test_connection(ReplicationInstanceArn=None, EndpointArn=None):
    """
    :param ReplicationInstanceArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the replication instance.
            
    :type ReplicationInstanceArn: string
    :param EndpointArn: [REQUIRED]
            The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.
            
    :type EndpointArn: string
    """
    pass
