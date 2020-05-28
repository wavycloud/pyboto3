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

def create_cluster(BrokerNodeGroupInfo=None, ClientAuthentication=None, ClusterName=None, ConfigurationInfo=None, EncryptionInfo=None, EnhancedMonitoring=None, OpenMonitoring=None, KafkaVersion=None, LoggingInfo=None, NumberOfBrokerNodes=None, Tags=None):
    """
    Creates a new MSK cluster.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_cluster(
        BrokerNodeGroupInfo={
            'BrokerAZDistribution': 'DEFAULT',
            'ClientSubnets': [
                'string',
            ],
            'InstanceType': 'string',
            'SecurityGroups': [
                'string',
            ],
            'StorageInfo': {
                'EbsStorageInfo': {
                    'VolumeSize': 123
                }
            }
        },
        ClientAuthentication={
            'Tls': {
                'CertificateAuthorityArnList': [
                    'string',
                ]
            }
        },
        ClusterName='string',
        ConfigurationInfo={
            'Arn': 'string',
            'Revision': 123
        },
        EncryptionInfo={
            'EncryptionAtRest': {
                'DataVolumeKMSKeyId': 'string'
            },
            'EncryptionInTransit': {
                'ClientBroker': 'TLS'|'TLS_PLAINTEXT'|'PLAINTEXT',
                'InCluster': True|False
            }
        },
        EnhancedMonitoring='DEFAULT'|'PER_BROKER'|'PER_TOPIC_PER_BROKER',
        OpenMonitoring={
            'Prometheus': {
                'JmxExporter': {
                    'EnabledInBroker': True|False
                },
                'NodeExporter': {
                    'EnabledInBroker': True|False
                }
            }
        },
        KafkaVersion='string',
        LoggingInfo={
            'BrokerLogs': {
                'CloudWatchLogs': {
                    'Enabled': True|False,
                    'LogGroup': 'string'
                },
                'Firehose': {
                    'DeliveryStream': 'string',
                    'Enabled': True|False
                },
                'S3': {
                    'Bucket': 'string',
                    'Enabled': True|False,
                    'Prefix': 'string'
                }
            }
        },
        NumberOfBrokerNodes=123,
        Tags={
            'string': 'string'
        }
    )
    
    
    :type BrokerNodeGroupInfo: dict
    :param BrokerNodeGroupInfo: [REQUIRED]\nInformation about the broker nodes in the cluster.\n\nBrokerAZDistribution (string) --The distribution of broker nodes across Availability Zones. This is an optional parameter. If you don\'t specify it, Amazon MSK gives it the value DEFAULT. You can also explicitly set this parameter to the value DEFAULT. No other values are currently allowed.\nAmazon MSK distributes the broker nodes evenly across the Availability Zones that correspond to the subnets you provide when you create the cluster.\n\nClientSubnets (list) -- [REQUIRED]The list of subnets to connect to in the client virtual private cloud (VPC). AWS creates elastic network interfaces inside these subnets. Client applications use elastic network interfaces to produce and consume data. Client subnets can\'t be in Availability Zone us-east-1e.\n\n(string) --\n\n\nInstanceType (string) -- [REQUIRED]The type of Amazon EC2 instances to use for Kafka brokers. The following instance types are allowed: kafka.m5.large, kafka.m5.xlarge, kafka.m5.2xlarge, kafka.m5.4xlarge, kafka.m5.12xlarge, and kafka.m5.24xlarge.\n\nSecurityGroups (list) --The AWS security groups to associate with the elastic network interfaces in order to specify who can connect to and communicate with the Amazon MSK cluster. If you don\'t specify a security group, Amazon MSK uses the default security group associated with the VPC.\n\n(string) --\n\n\nStorageInfo (dict) --Contains information about storage volumes attached to MSK broker nodes.\n\nEbsStorageInfo (dict) --EBS volume information.\n\nVolumeSize (integer) --The size in GiB of the EBS volume for the data drive on each broker node.\n\n\n\n\n\n\n

    :type ClientAuthentication: dict
    :param ClientAuthentication: Includes all client authentication related information.\n\nTls (dict) --Details for ClientAuthentication using TLS.\n\nCertificateAuthorityArnList (list) --List of ACM Certificate Authority ARNs.\n\n(string) --\n\n\n\n\n\n

    :type ClusterName: string
    :param ClusterName: [REQUIRED]\nThe name of the cluster.\n

    :type ConfigurationInfo: dict
    :param ConfigurationInfo: Represents the configuration that you want MSK to use for the brokers in a cluster.\n\nArn (string) -- [REQUIRED]ARN of the configuration to use.\n\nRevision (integer) -- [REQUIRED]The revision of the configuration to use.\n\n\n

    :type EncryptionInfo: dict
    :param EncryptionInfo: Includes all encryption-related information.\n\nEncryptionAtRest (dict) --The data-volume encryption details.\n\nDataVolumeKMSKeyId (string) -- [REQUIRED]The ARN of the AWS KMS key for encrypting data at rest. If you don\'t specify a KMS key, MSK creates one for you and uses it.\n\n\n\nEncryptionInTransit (dict) --The details for encryption in transit.\n\nClientBroker (string) --Indicates the encryption setting for data in transit between clients and brokers. The following are the possible values.\nTLS means that client-broker communication is enabled with TLS only.\nTLS_PLAINTEXT means that client-broker communication is enabled for both TLS-encrypted, as well as plaintext data.\nPLAINTEXT means that client-broker communication is enabled in plaintext only.\nThe default value is TLS_PLAINTEXT.\n\nInCluster (boolean) --When set to true, it indicates that data communication among the broker nodes of the cluster is encrypted. When set to false, the communication happens in plaintext.\nThe default value is true.\n\n\n\n\n

    :type EnhancedMonitoring: string
    :param EnhancedMonitoring: Specifies the level of monitoring for the MSK cluster. The possible values are DEFAULT, PER_BROKER, and PER_TOPIC_PER_BROKER.

    :type OpenMonitoring: dict
    :param OpenMonitoring: The settings for open monitoring.\n\nPrometheus (dict) -- [REQUIRED]Prometheus settings.\n\nJmxExporter (dict) --Indicates whether you want to enable or disable the JMX Exporter.\n\nEnabledInBroker (boolean) -- [REQUIRED]Indicates whether you want to enable or disable the JMX Exporter.\n\n\n\nNodeExporter (dict) --Indicates whether you want to enable or disable the Node Exporter.\n\nEnabledInBroker (boolean) -- [REQUIRED]Indicates whether you want to enable or disable the Node Exporter.\n\n\n\n\n\n\n

    :type KafkaVersion: string
    :param KafkaVersion: [REQUIRED]\nThe version of Apache Kafka.\n

    :type LoggingInfo: dict
    :param LoggingInfo: \nBrokerLogs (dict) -- [REQUIRED]\nCloudWatchLogs (dict) --\nEnabled (boolean) -- [REQUIRED]\nLogGroup (string) --\n\n\nFirehose (dict) --\nDeliveryStream (string) --\nEnabled (boolean) -- [REQUIRED]\n\n\nS3 (dict) --\nBucket (string) --\nEnabled (boolean) -- [REQUIRED]\nPrefix (string) --\n\n\n\n\n\n

    :type NumberOfBrokerNodes: integer
    :param NumberOfBrokerNodes: [REQUIRED]\nThe number of broker nodes in the cluster.\n

    :type Tags: dict
    :param Tags: Create tags when creating the cluster.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ClusterArn': 'string',
    'ClusterName': 'string',
    'State': 'ACTIVE'|'CREATING'|'UPDATING'|'DELETING'|'FAILED'
}


Response Structure

(dict) --

ClusterArn (string) --
The Amazon Resource Name (ARN) of the cluster.

ClusterName (string) --
The name of the MSK cluster.

State (string) --
The state of the cluster. The possible states are CREATING, ACTIVE, and FAILED.







Exceptions

Kafka.Client.exceptions.BadRequestException
Kafka.Client.exceptions.InternalServerErrorException
Kafka.Client.exceptions.UnauthorizedException
Kafka.Client.exceptions.ForbiddenException
Kafka.Client.exceptions.ServiceUnavailableException
Kafka.Client.exceptions.TooManyRequestsException
Kafka.Client.exceptions.ConflictException


    :return: {
        'ClusterArn': 'string',
        'ClusterName': 'string',
        'State': 'ACTIVE'|'CREATING'|'UPDATING'|'DELETING'|'FAILED'
    }
    
    
    :returns: 
    Kafka.Client.exceptions.BadRequestException
    Kafka.Client.exceptions.InternalServerErrorException
    Kafka.Client.exceptions.UnauthorizedException
    Kafka.Client.exceptions.ForbiddenException
    Kafka.Client.exceptions.ServiceUnavailableException
    Kafka.Client.exceptions.TooManyRequestsException
    Kafka.Client.exceptions.ConflictException
    
    """
    pass

def create_configuration(Description=None, KafkaVersions=None, Name=None, ServerProperties=None):
    """
    Creates a new MSK configuration.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_configuration(
        Description='string',
        KafkaVersions=[
            'string',
        ],
        Name='string',
        ServerProperties=b'bytes'
    )
    
    
    :type Description: string
    :param Description: The description of the configuration.

    :type KafkaVersions: list
    :param KafkaVersions: [REQUIRED]\nThe versions of Apache Kafka with which you can use this MSK configuration.\n\n(string) --\n\n

    :type Name: string
    :param Name: [REQUIRED]\nThe name of the configuration.\n

    :type ServerProperties: bytes
    :param ServerProperties: [REQUIRED]\nContents of the server.propertiesfile. When using the API, you must ensure that the contents of the file are base64 encoded. When using the AWS Management Console, the SDK, or the AWS CLI, the contents of server.propertiescan be in plaintext.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Arn': 'string',
    'CreationTime': datetime(2015, 1, 1),
    'LatestRevision': {
        'CreationTime': datetime(2015, 1, 1),
        'Description': 'string',
        'Revision': 123
    },
    'Name': 'string'
}


Response Structure

(dict) --
200 response

Arn (string) --
The Amazon Resource Name (ARN) of the configuration.

CreationTime (datetime) --
The time when the configuration was created.

LatestRevision (dict) --
Latest revision of the configuration.

CreationTime (datetime) --
The time when the configuration revision was created.

Description (string) --
The description of the configuration revision.

Revision (integer) --
The revision number.



Name (string) --
The name of the configuration.







Exceptions

Kafka.Client.exceptions.BadRequestException
Kafka.Client.exceptions.InternalServerErrorException
Kafka.Client.exceptions.UnauthorizedException
Kafka.Client.exceptions.ForbiddenException
Kafka.Client.exceptions.ServiceUnavailableException
Kafka.Client.exceptions.TooManyRequestsException
Kafka.Client.exceptions.ConflictException


    :return: {
        'Arn': 'string',
        'CreationTime': datetime(2015, 1, 1),
        'LatestRevision': {
            'CreationTime': datetime(2015, 1, 1),
            'Description': 'string',
            'Revision': 123
        },
        'Name': 'string'
    }
    
    
    :returns: 
    Kafka.Client.exceptions.BadRequestException
    Kafka.Client.exceptions.InternalServerErrorException
    Kafka.Client.exceptions.UnauthorizedException
    Kafka.Client.exceptions.ForbiddenException
    Kafka.Client.exceptions.ServiceUnavailableException
    Kafka.Client.exceptions.TooManyRequestsException
    Kafka.Client.exceptions.ConflictException
    
    """
    pass

def delete_cluster(ClusterArn=None, CurrentVersion=None):
    """
    Deletes the MSK cluster specified by the Amazon Resource Name (ARN) in the request.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_cluster(
        ClusterArn='string',
        CurrentVersion='string'
    )
    
    
    :type ClusterArn: string
    :param ClusterArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that uniquely identifies the cluster.\n

    :type CurrentVersion: string
    :param CurrentVersion: The current version of the MSK cluster.

    :rtype: dict

ReturnsResponse Syntax
{
    'ClusterArn': 'string',
    'State': 'ACTIVE'|'CREATING'|'UPDATING'|'DELETING'|'FAILED'
}


Response Structure

(dict) --
Successful response.

ClusterArn (string) --
The Amazon Resource Name (ARN) of the cluster.

State (string) --
The state of the cluster. The possible states are CREATING, ACTIVE, and FAILED.







Exceptions

Kafka.Client.exceptions.NotFoundException
Kafka.Client.exceptions.BadRequestException
Kafka.Client.exceptions.InternalServerErrorException
Kafka.Client.exceptions.ForbiddenException


    :return: {
        'ClusterArn': 'string',
        'State': 'ACTIVE'|'CREATING'|'UPDATING'|'DELETING'|'FAILED'
    }
    
    
    :returns: 
    Kafka.Client.exceptions.NotFoundException
    Kafka.Client.exceptions.BadRequestException
    Kafka.Client.exceptions.InternalServerErrorException
    Kafka.Client.exceptions.ForbiddenException
    
    """
    pass

def describe_cluster(ClusterArn=None):
    """
    Returns a description of the MSK cluster whose Amazon Resource Name (ARN) is specified in the request.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_cluster(
        ClusterArn='string'
    )
    
    
    :type ClusterArn: string
    :param ClusterArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that uniquely identifies the cluster.\n

    :rtype: dict
ReturnsResponse Syntax{
    'ClusterInfo': {
        'ActiveOperationArn': 'string',
        'BrokerNodeGroupInfo': {
            'BrokerAZDistribution': 'DEFAULT',
            'ClientSubnets': [
                'string',
            ],
            'InstanceType': 'string',
            'SecurityGroups': [
                'string',
            ],
            'StorageInfo': {
                'EbsStorageInfo': {
                    'VolumeSize': 123
                }
            }
        },
        'ClientAuthentication': {
            'Tls': {
                'CertificateAuthorityArnList': [
                    'string',
                ]
            }
        },
        'ClusterArn': 'string',
        'ClusterName': 'string',
        'CreationTime': datetime(2015, 1, 1),
        'CurrentBrokerSoftwareInfo': {
            'ConfigurationArn': 'string',
            'ConfigurationRevision': 123,
            'KafkaVersion': 'string'
        },
        'CurrentVersion': 'string',
        'EncryptionInfo': {
            'EncryptionAtRest': {
                'DataVolumeKMSKeyId': 'string'
            },
            'EncryptionInTransit': {
                'ClientBroker': 'TLS'|'TLS_PLAINTEXT'|'PLAINTEXT',
                'InCluster': True|False
            }
        },
        'EnhancedMonitoring': 'DEFAULT'|'PER_BROKER'|'PER_TOPIC_PER_BROKER',
        'OpenMonitoring': {
            'Prometheus': {
                'JmxExporter': {
                    'EnabledInBroker': True|False
                },
                'NodeExporter': {
                    'EnabledInBroker': True|False
                }
            }
        },
        'LoggingInfo': {
            'BrokerLogs': {
                'CloudWatchLogs': {
                    'Enabled': True|False,
                    'LogGroup': 'string'
                },
                'Firehose': {
                    'DeliveryStream': 'string',
                    'Enabled': True|False
                },
                'S3': {
                    'Bucket': 'string',
                    'Enabled': True|False,
                    'Prefix': 'string'
                }
            }
        },
        'NumberOfBrokerNodes': 123,
        'State': 'ACTIVE'|'CREATING'|'UPDATING'|'DELETING'|'FAILED',
        'StateInfo': {
            'Code': 'string',
            'Message': 'string'
        },
        'Tags': {
            'string': 'string'
        },
        'ZookeeperConnectString': 'string'
    }
}


Response Structure

(dict) --Successful response.

ClusterInfo (dict) --The cluster information.

ActiveOperationArn (string) --Arn of active cluster operation.

BrokerNodeGroupInfo (dict) --Information about the broker nodes.

BrokerAZDistribution (string) --The distribution of broker nodes across Availability Zones. This is an optional parameter. If you don\'t specify it, Amazon MSK gives it the value DEFAULT. You can also explicitly set this parameter to the value DEFAULT. No other values are currently allowed.
Amazon MSK distributes the broker nodes evenly across the Availability Zones that correspond to the subnets you provide when you create the cluster.

ClientSubnets (list) --The list of subnets to connect to in the client virtual private cloud (VPC). AWS creates elastic network interfaces inside these subnets. Client applications use elastic network interfaces to produce and consume data. Client subnets can\'t be in Availability Zone us-east-1e.

(string) --


InstanceType (string) --The type of Amazon EC2 instances to use for Kafka brokers. The following instance types are allowed: kafka.m5.large, kafka.m5.xlarge, kafka.m5.2xlarge, kafka.m5.4xlarge, kafka.m5.12xlarge, and kafka.m5.24xlarge.

SecurityGroups (list) --The AWS security groups to associate with the elastic network interfaces in order to specify who can connect to and communicate with the Amazon MSK cluster. If you don\'t specify a security group, Amazon MSK uses the default security group associated with the VPC.

(string) --


StorageInfo (dict) --Contains information about storage volumes attached to MSK broker nodes.

EbsStorageInfo (dict) --EBS volume information.

VolumeSize (integer) --The size in GiB of the EBS volume for the data drive on each broker node.







ClientAuthentication (dict) --Includes all client authentication information.

Tls (dict) --Details for ClientAuthentication using TLS.

CertificateAuthorityArnList (list) --List of ACM Certificate Authority ARNs.

(string) --






ClusterArn (string) --The Amazon Resource Name (ARN) that uniquely identifies the cluster.

ClusterName (string) --The name of the cluster.

CreationTime (datetime) --The time when the cluster was created.

CurrentBrokerSoftwareInfo (dict) --Information about the version of software currently deployed on the Kafka brokers in the cluster.

ConfigurationArn (string) --The Amazon Resource Name (ARN) of the configuration used for the cluster. This field isn\'t visible in this preview release.

ConfigurationRevision (integer) --The revision of the configuration to use. This field isn\'t visible in this preview release.

KafkaVersion (string) --The version of Apache Kafka.



CurrentVersion (string) --The current version of the MSK cluster.

EncryptionInfo (dict) --Includes all encryption-related information.

EncryptionAtRest (dict) --The data-volume encryption details.

DataVolumeKMSKeyId (string) --The ARN of the AWS KMS key for encrypting data at rest. If you don\'t specify a KMS key, MSK creates one for you and uses it.



EncryptionInTransit (dict) --The details for encryption in transit.

ClientBroker (string) --Indicates the encryption setting for data in transit between clients and brokers. The following are the possible values.
TLS means that client-broker communication is enabled with TLS only.
TLS_PLAINTEXT means that client-broker communication is enabled for both TLS-encrypted, as well as plaintext data.
PLAINTEXT means that client-broker communication is enabled in plaintext only.
The default value is TLS_PLAINTEXT.

InCluster (boolean) --When set to true, it indicates that data communication among the broker nodes of the cluster is encrypted. When set to false, the communication happens in plaintext.
The default value is true.





EnhancedMonitoring (string) --Specifies which metrics are gathered for the MSK cluster. This property has three possible values: DEFAULT, PER_BROKER, and PER_TOPIC_PER_BROKER. For a list of the metrics associated with each of these three levels of monitoring, see Monitoring .

OpenMonitoring (dict) --Settings for open monitoring using Prometheus.

Prometheus (dict) --Prometheus settings.

JmxExporter (dict) --Indicates whether you want to enable or disable the JMX Exporter.

EnabledInBroker (boolean) --Indicates whether you want to enable or disable the JMX Exporter.



NodeExporter (dict) --Indicates whether you want to enable or disable the Node Exporter.

EnabledInBroker (boolean) --Indicates whether you want to enable or disable the Node Exporter.







LoggingInfo (dict) --
BrokerLogs (dict) --
CloudWatchLogs (dict) --
Enabled (boolean) --
LogGroup (string) --


Firehose (dict) --
DeliveryStream (string) --
Enabled (boolean) --


S3 (dict) --
Bucket (string) --
Enabled (boolean) --
Prefix (string) --






NumberOfBrokerNodes (integer) --The number of broker nodes in the cluster.

State (string) --The state of the cluster. The possible states are CREATING, ACTIVE, and FAILED.

StateInfo (dict) --
Code (string) --
Message (string) --


Tags (dict) --Tags attached to the cluster.

(string) --
(string) --




ZookeeperConnectString (string) --The connection string to use to connect to the Apache ZooKeeper cluster.








Exceptions

Kafka.Client.exceptions.NotFoundException
Kafka.Client.exceptions.BadRequestException
Kafka.Client.exceptions.UnauthorizedException
Kafka.Client.exceptions.InternalServerErrorException
Kafka.Client.exceptions.ForbiddenException


    :return: {
        'ClusterInfo': {
            'ActiveOperationArn': 'string',
            'BrokerNodeGroupInfo': {
                'BrokerAZDistribution': 'DEFAULT',
                'ClientSubnets': [
                    'string',
                ],
                'InstanceType': 'string',
                'SecurityGroups': [
                    'string',
                ],
                'StorageInfo': {
                    'EbsStorageInfo': {
                        'VolumeSize': 123
                    }
                }
            },
            'ClientAuthentication': {
                'Tls': {
                    'CertificateAuthorityArnList': [
                        'string',
                    ]
                }
            },
            'ClusterArn': 'string',
            'ClusterName': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'CurrentBrokerSoftwareInfo': {
                'ConfigurationArn': 'string',
                'ConfigurationRevision': 123,
                'KafkaVersion': 'string'
            },
            'CurrentVersion': 'string',
            'EncryptionInfo': {
                'EncryptionAtRest': {
                    'DataVolumeKMSKeyId': 'string'
                },
                'EncryptionInTransit': {
                    'ClientBroker': 'TLS'|'TLS_PLAINTEXT'|'PLAINTEXT',
                    'InCluster': True|False
                }
            },
            'EnhancedMonitoring': 'DEFAULT'|'PER_BROKER'|'PER_TOPIC_PER_BROKER',
            'OpenMonitoring': {
                'Prometheus': {
                    'JmxExporter': {
                        'EnabledInBroker': True|False
                    },
                    'NodeExporter': {
                        'EnabledInBroker': True|False
                    }
                }
            },
            'LoggingInfo': {
                'BrokerLogs': {
                    'CloudWatchLogs': {
                        'Enabled': True|False,
                        'LogGroup': 'string'
                    },
                    'Firehose': {
                        'DeliveryStream': 'string',
                        'Enabled': True|False
                    },
                    'S3': {
                        'Bucket': 'string',
                        'Enabled': True|False,
                        'Prefix': 'string'
                    }
                }
            },
            'NumberOfBrokerNodes': 123,
            'State': 'ACTIVE'|'CREATING'|'UPDATING'|'DELETING'|'FAILED',
            'StateInfo': {
                'Code': 'string',
                'Message': 'string'
            },
            'Tags': {
                'string': 'string'
            },
            'ZookeeperConnectString': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_cluster_operation(ClusterOperationArn=None):
    """
    Returns a description of the cluster operation specified by the ARN.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_cluster_operation(
        ClusterOperationArn='string'
    )
    
    
    :type ClusterOperationArn: string
    :param ClusterOperationArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that uniquely identifies the MSK cluster operation.\n

    :rtype: dict
ReturnsResponse Syntax{
    'ClusterOperationInfo': {
        'ClientRequestId': 'string',
        'ClusterArn': 'string',
        'CreationTime': datetime(2015, 1, 1),
        'EndTime': datetime(2015, 1, 1),
        'ErrorInfo': {
            'ErrorCode': 'string',
            'ErrorString': 'string'
        },
        'OperationArn': 'string',
        'OperationState': 'string',
        'OperationType': 'string',
        'SourceClusterInfo': {
            'BrokerEBSVolumeInfo': [
                {
                    'KafkaBrokerNodeId': 'string',
                    'VolumeSizeGB': 123
                },
            ],
            'ConfigurationInfo': {
                'Arn': 'string',
                'Revision': 123
            },
            'NumberOfBrokerNodes': 123,
            'EnhancedMonitoring': 'DEFAULT'|'PER_BROKER'|'PER_TOPIC_PER_BROKER',
            'OpenMonitoring': {
                'Prometheus': {
                    'JmxExporter': {
                        'EnabledInBroker': True|False
                    },
                    'NodeExporter': {
                        'EnabledInBroker': True|False
                    }
                }
            },
            'LoggingInfo': {
                'BrokerLogs': {
                    'CloudWatchLogs': {
                        'Enabled': True|False,
                        'LogGroup': 'string'
                    },
                    'Firehose': {
                        'DeliveryStream': 'string',
                        'Enabled': True|False
                    },
                    'S3': {
                        'Bucket': 'string',
                        'Enabled': True|False,
                        'Prefix': 'string'
                    }
                }
            }
        },
        'TargetClusterInfo': {
            'BrokerEBSVolumeInfo': [
                {
                    'KafkaBrokerNodeId': 'string',
                    'VolumeSizeGB': 123
                },
            ],
            'ConfigurationInfo': {
                'Arn': 'string',
                'Revision': 123
            },
            'NumberOfBrokerNodes': 123,
            'EnhancedMonitoring': 'DEFAULT'|'PER_BROKER'|'PER_TOPIC_PER_BROKER',
            'OpenMonitoring': {
                'Prometheus': {
                    'JmxExporter': {
                        'EnabledInBroker': True|False
                    },
                    'NodeExporter': {
                        'EnabledInBroker': True|False
                    }
                }
            },
            'LoggingInfo': {
                'BrokerLogs': {
                    'CloudWatchLogs': {
                        'Enabled': True|False,
                        'LogGroup': 'string'
                    },
                    'Firehose': {
                        'DeliveryStream': 'string',
                        'Enabled': True|False
                    },
                    'S3': {
                        'Bucket': 'string',
                        'Enabled': True|False,
                        'Prefix': 'string'
                    }
                }
            }
        }
    }
}


Response Structure

(dict) --200 response

ClusterOperationInfo (dict) --Cluster operation information

ClientRequestId (string) --The ID of the API request that triggered this operation.

ClusterArn (string) --ARN of the cluster.

CreationTime (datetime) --The time that the operation was created.

EndTime (datetime) --The time at which the operation finished.

ErrorInfo (dict) --Describes the error if the operation fails.

ErrorCode (string) --A number describing the error programmatically.

ErrorString (string) --An optional field to provide more details about the error.



OperationArn (string) --ARN of the cluster operation.

OperationState (string) --State of the cluster operation.

OperationType (string) --Type of the cluster operation.

SourceClusterInfo (dict) --Information about cluster attributes before a cluster is updated.

BrokerEBSVolumeInfo (list) --Specifies the size of the EBS volume and the ID of the associated broker.

(dict) --Specifies the EBS volume upgrade information. The broker identifier must be set to the keyword ALL. This means the changes apply to all the brokers in the cluster.

KafkaBrokerNodeId (string) --The ID of the broker to update.

VolumeSizeGB (integer) --Size of the EBS volume to update.





ConfigurationInfo (dict) --Information about the changes in the configuration of the brokers.

Arn (string) --ARN of the configuration to use.

Revision (integer) --The revision of the configuration to use.



NumberOfBrokerNodes (integer) --The number of broker nodes in the cluster.

EnhancedMonitoring (string) --Specifies which Apache Kafka metrics Amazon MSK gathers and sends to Amazon CloudWatch for this cluster.

OpenMonitoring (dict) --The settings for open monitoring.

Prometheus (dict) --Prometheus settings.

JmxExporter (dict) --Indicates whether you want to enable or disable the JMX Exporter.

EnabledInBroker (boolean) --Indicates whether you want to enable or disable the JMX Exporter.



NodeExporter (dict) --Indicates whether you want to enable or disable the Node Exporter.

EnabledInBroker (boolean) --Indicates whether you want to enable or disable the Node Exporter.







LoggingInfo (dict) --
BrokerLogs (dict) --
CloudWatchLogs (dict) --
Enabled (boolean) --
LogGroup (string) --


Firehose (dict) --
DeliveryStream (string) --
Enabled (boolean) --


S3 (dict) --
Bucket (string) --
Enabled (boolean) --
Prefix (string) --








TargetClusterInfo (dict) --Information about cluster attributes after a cluster is updated.

BrokerEBSVolumeInfo (list) --Specifies the size of the EBS volume and the ID of the associated broker.

(dict) --Specifies the EBS volume upgrade information. The broker identifier must be set to the keyword ALL. This means the changes apply to all the brokers in the cluster.

KafkaBrokerNodeId (string) --The ID of the broker to update.

VolumeSizeGB (integer) --Size of the EBS volume to update.





ConfigurationInfo (dict) --Information about the changes in the configuration of the brokers.

Arn (string) --ARN of the configuration to use.

Revision (integer) --The revision of the configuration to use.



NumberOfBrokerNodes (integer) --The number of broker nodes in the cluster.

EnhancedMonitoring (string) --Specifies which Apache Kafka metrics Amazon MSK gathers and sends to Amazon CloudWatch for this cluster.

OpenMonitoring (dict) --The settings for open monitoring.

Prometheus (dict) --Prometheus settings.

JmxExporter (dict) --Indicates whether you want to enable or disable the JMX Exporter.

EnabledInBroker (boolean) --Indicates whether you want to enable or disable the JMX Exporter.



NodeExporter (dict) --Indicates whether you want to enable or disable the Node Exporter.

EnabledInBroker (boolean) --Indicates whether you want to enable or disable the Node Exporter.







LoggingInfo (dict) --
BrokerLogs (dict) --
CloudWatchLogs (dict) --
Enabled (boolean) --
LogGroup (string) --


Firehose (dict) --
DeliveryStream (string) --
Enabled (boolean) --


S3 (dict) --
Bucket (string) --
Enabled (boolean) --
Prefix (string) --















Exceptions

Kafka.Client.exceptions.NotFoundException
Kafka.Client.exceptions.BadRequestException
Kafka.Client.exceptions.UnauthorizedException
Kafka.Client.exceptions.InternalServerErrorException
Kafka.Client.exceptions.ForbiddenException


    :return: {
        'ClusterOperationInfo': {
            'ClientRequestId': 'string',
            'ClusterArn': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'EndTime': datetime(2015, 1, 1),
            'ErrorInfo': {
                'ErrorCode': 'string',
                'ErrorString': 'string'
            },
            'OperationArn': 'string',
            'OperationState': 'string',
            'OperationType': 'string',
            'SourceClusterInfo': {
                'BrokerEBSVolumeInfo': [
                    {
                        'KafkaBrokerNodeId': 'string',
                        'VolumeSizeGB': 123
                    },
                ],
                'ConfigurationInfo': {
                    'Arn': 'string',
                    'Revision': 123
                },
                'NumberOfBrokerNodes': 123,
                'EnhancedMonitoring': 'DEFAULT'|'PER_BROKER'|'PER_TOPIC_PER_BROKER',
                'OpenMonitoring': {
                    'Prometheus': {
                        'JmxExporter': {
                            'EnabledInBroker': True|False
                        },
                        'NodeExporter': {
                            'EnabledInBroker': True|False
                        }
                    }
                },
                'LoggingInfo': {
                    'BrokerLogs': {
                        'CloudWatchLogs': {
                            'Enabled': True|False,
                            'LogGroup': 'string'
                        },
                        'Firehose': {
                            'DeliveryStream': 'string',
                            'Enabled': True|False
                        },
                        'S3': {
                            'Bucket': 'string',
                            'Enabled': True|False,
                            'Prefix': 'string'
                        }
                    }
                }
            },
            'TargetClusterInfo': {
                'BrokerEBSVolumeInfo': [
                    {
                        'KafkaBrokerNodeId': 'string',
                        'VolumeSizeGB': 123
                    },
                ],
                'ConfigurationInfo': {
                    'Arn': 'string',
                    'Revision': 123
                },
                'NumberOfBrokerNodes': 123,
                'EnhancedMonitoring': 'DEFAULT'|'PER_BROKER'|'PER_TOPIC_PER_BROKER',
                'OpenMonitoring': {
                    'Prometheus': {
                        'JmxExporter': {
                            'EnabledInBroker': True|False
                        },
                        'NodeExporter': {
                            'EnabledInBroker': True|False
                        }
                    }
                },
                'LoggingInfo': {
                    'BrokerLogs': {
                        'CloudWatchLogs': {
                            'Enabled': True|False,
                            'LogGroup': 'string'
                        },
                        'Firehose': {
                            'DeliveryStream': 'string',
                            'Enabled': True|False
                        },
                        'S3': {
                            'Bucket': 'string',
                            'Enabled': True|False,
                            'Prefix': 'string'
                        }
                    }
                }
            }
        }
    }
    
    
    :returns: 
    BrokerLogs (dict) --
    CloudWatchLogs (dict) --
    Enabled (boolean) --
    LogGroup (string) --
    
    
    Firehose (dict) --
    DeliveryStream (string) --
    Enabled (boolean) --
    
    
    S3 (dict) --
    Bucket (string) --
    Enabled (boolean) --
    Prefix (string) --
    
    
    
    
    
    """
    pass

def describe_configuration(Arn=None):
    """
    Returns a description of this MSK configuration.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_configuration(
        Arn='string'
    )
    
    
    :type Arn: string
    :param Arn: [REQUIRED]\nThe Amazon Resource Name (ARN) that uniquely identifies an MSK configuration and all of its revisions.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Arn': 'string',
    'CreationTime': datetime(2015, 1, 1),
    'Description': 'string',
    'KafkaVersions': [
        'string',
    ],
    'LatestRevision': {
        'CreationTime': datetime(2015, 1, 1),
        'Description': 'string',
        'Revision': 123
    },
    'Name': 'string'
}


Response Structure

(dict) --200 response

Arn (string) --The Amazon Resource Name (ARN) of the configuration.

CreationTime (datetime) --The time when the configuration was created.

Description (string) --The description of the configuration.

KafkaVersions (list) --The versions of Apache Kafka with which you can use this MSK configuration.

(string) --


LatestRevision (dict) --Latest revision of the configuration.

CreationTime (datetime) --The time when the configuration revision was created.

Description (string) --The description of the configuration revision.

Revision (integer) --The revision number.



Name (string) --The name of the configuration.






Exceptions

Kafka.Client.exceptions.BadRequestException
Kafka.Client.exceptions.UnauthorizedException
Kafka.Client.exceptions.InternalServerErrorException
Kafka.Client.exceptions.ForbiddenException
Kafka.Client.exceptions.NotFoundException
Kafka.Client.exceptions.ServiceUnavailableException


    :return: {
        'Arn': 'string',
        'CreationTime': datetime(2015, 1, 1),
        'Description': 'string',
        'KafkaVersions': [
            'string',
        ],
        'LatestRevision': {
            'CreationTime': datetime(2015, 1, 1),
            'Description': 'string',
            'Revision': 123
        },
        'Name': 'string'
    }
    
    
    :returns: 
    Kafka.Client.exceptions.BadRequestException
    Kafka.Client.exceptions.UnauthorizedException
    Kafka.Client.exceptions.InternalServerErrorException
    Kafka.Client.exceptions.ForbiddenException
    Kafka.Client.exceptions.NotFoundException
    Kafka.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def describe_configuration_revision(Arn=None, Revision=None):
    """
    Returns a description of this revision of the configuration.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_configuration_revision(
        Arn='string',
        Revision=123
    )
    
    
    :type Arn: string
    :param Arn: [REQUIRED]\nThe Amazon Resource Name (ARN) that uniquely identifies an MSK configuration and all of its revisions.\n

    :type Revision: integer
    :param Revision: [REQUIRED]\nA string that uniquely identifies a revision of an MSK configuration.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Arn': 'string',
    'CreationTime': datetime(2015, 1, 1),
    'Description': 'string',
    'Revision': 123,
    'ServerProperties': b'bytes'
}


Response Structure

(dict) --
200 response

Arn (string) --
The Amazon Resource Name (ARN) of the configuration.

CreationTime (datetime) --
The time when the configuration was created.

Description (string) --
The description of the configuration.

Revision (integer) --
The revision number.

ServerProperties (bytes) --
Contents of the server.propertiesfile. When using the API, you must ensure that the contents of the file are base64 encoded. When using the AWS Management Console, the SDK, or the AWS CLI, the contents of server.propertiescan be in plaintext.







Exceptions

Kafka.Client.exceptions.BadRequestException
Kafka.Client.exceptions.UnauthorizedException
Kafka.Client.exceptions.InternalServerErrorException
Kafka.Client.exceptions.ForbiddenException
Kafka.Client.exceptions.NotFoundException
Kafka.Client.exceptions.ServiceUnavailableException


    :return: {
        'Arn': 'string',
        'CreationTime': datetime(2015, 1, 1),
        'Description': 'string',
        'Revision': 123,
        'ServerProperties': b'bytes'
    }
    
    
    :returns: 
    Kafka.Client.exceptions.BadRequestException
    Kafka.Client.exceptions.UnauthorizedException
    Kafka.Client.exceptions.InternalServerErrorException
    Kafka.Client.exceptions.ForbiddenException
    Kafka.Client.exceptions.NotFoundException
    Kafka.Client.exceptions.ServiceUnavailableException
    
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

def get_bootstrap_brokers(ClusterArn=None):
    """
    A list of brokers that a client application can use to bootstrap.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_bootstrap_brokers(
        ClusterArn='string'
    )
    
    
    :type ClusterArn: string
    :param ClusterArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that uniquely identifies the cluster.\n

    :rtype: dict
ReturnsResponse Syntax{
    'BootstrapBrokerString': 'string',
    'BootstrapBrokerStringTls': 'string'
}


Response Structure

(dict) --Successful response.

BootstrapBrokerString (string) --A string containing one or more hostname:port pairs.

BootstrapBrokerStringTls (string) --A string containing one or more DNS names (or IP) and TLS port pairs.






Exceptions

Kafka.Client.exceptions.BadRequestException
Kafka.Client.exceptions.UnauthorizedException
Kafka.Client.exceptions.InternalServerErrorException
Kafka.Client.exceptions.ConflictException
Kafka.Client.exceptions.ForbiddenException


    :return: {
        'BootstrapBrokerString': 'string',
        'BootstrapBrokerStringTls': 'string'
    }
    
    
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

def list_cluster_operations(ClusterArn=None, MaxResults=None, NextToken=None):
    """
    Returns a list of all the operations that have been performed on the specified MSK cluster.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_cluster_operations(
        ClusterArn='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type ClusterArn: string
    :param ClusterArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that uniquely identifies the cluster.\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in the response. If there are more results, the response includes a NextToken parameter.

    :type NextToken: string
    :param NextToken: The paginated results marker. When the result of the operation is truncated, the call returns NextToken in the response. To get the next batch, provide this token in your next request.

    :rtype: dict

ReturnsResponse Syntax
{
    'ClusterOperationInfoList': [
        {
            'ClientRequestId': 'string',
            'ClusterArn': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'EndTime': datetime(2015, 1, 1),
            'ErrorInfo': {
                'ErrorCode': 'string',
                'ErrorString': 'string'
            },
            'OperationArn': 'string',
            'OperationState': 'string',
            'OperationType': 'string',
            'SourceClusterInfo': {
                'BrokerEBSVolumeInfo': [
                    {
                        'KafkaBrokerNodeId': 'string',
                        'VolumeSizeGB': 123
                    },
                ],
                'ConfigurationInfo': {
                    'Arn': 'string',
                    'Revision': 123
                },
                'NumberOfBrokerNodes': 123,
                'EnhancedMonitoring': 'DEFAULT'|'PER_BROKER'|'PER_TOPIC_PER_BROKER',
                'OpenMonitoring': {
                    'Prometheus': {
                        'JmxExporter': {
                            'EnabledInBroker': True|False
                        },
                        'NodeExporter': {
                            'EnabledInBroker': True|False
                        }
                    }
                },
                'LoggingInfo': {
                    'BrokerLogs': {
                        'CloudWatchLogs': {
                            'Enabled': True|False,
                            'LogGroup': 'string'
                        },
                        'Firehose': {
                            'DeliveryStream': 'string',
                            'Enabled': True|False
                        },
                        'S3': {
                            'Bucket': 'string',
                            'Enabled': True|False,
                            'Prefix': 'string'
                        }
                    }
                }
            },
            'TargetClusterInfo': {
                'BrokerEBSVolumeInfo': [
                    {
                        'KafkaBrokerNodeId': 'string',
                        'VolumeSizeGB': 123
                    },
                ],
                'ConfigurationInfo': {
                    'Arn': 'string',
                    'Revision': 123
                },
                'NumberOfBrokerNodes': 123,
                'EnhancedMonitoring': 'DEFAULT'|'PER_BROKER'|'PER_TOPIC_PER_BROKER',
                'OpenMonitoring': {
                    'Prometheus': {
                        'JmxExporter': {
                            'EnabledInBroker': True|False
                        },
                        'NodeExporter': {
                            'EnabledInBroker': True|False
                        }
                    }
                },
                'LoggingInfo': {
                    'BrokerLogs': {
                        'CloudWatchLogs': {
                            'Enabled': True|False,
                            'LogGroup': 'string'
                        },
                        'Firehose': {
                            'DeliveryStream': 'string',
                            'Enabled': True|False
                        },
                        'S3': {
                            'Bucket': 'string',
                            'Enabled': True|False,
                            'Prefix': 'string'
                        }
                    }
                }
            }
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
Successful response.

ClusterOperationInfoList (list) --
An array of cluster operation information objects.

(dict) --
Returns information about a cluster operation.

ClientRequestId (string) --
The ID of the API request that triggered this operation.

ClusterArn (string) --
ARN of the cluster.

CreationTime (datetime) --
The time that the operation was created.

EndTime (datetime) --
The time at which the operation finished.

ErrorInfo (dict) --
Describes the error if the operation fails.

ErrorCode (string) --
A number describing the error programmatically.

ErrorString (string) --
An optional field to provide more details about the error.



OperationArn (string) --
ARN of the cluster operation.

OperationState (string) --
State of the cluster operation.

OperationType (string) --
Type of the cluster operation.

SourceClusterInfo (dict) --
Information about cluster attributes before a cluster is updated.

BrokerEBSVolumeInfo (list) --
Specifies the size of the EBS volume and the ID of the associated broker.

(dict) --
Specifies the EBS volume upgrade information. The broker identifier must be set to the keyword ALL. This means the changes apply to all the brokers in the cluster.

KafkaBrokerNodeId (string) --
The ID of the broker to update.

VolumeSizeGB (integer) --
Size of the EBS volume to update.





ConfigurationInfo (dict) --
Information about the changes in the configuration of the brokers.

Arn (string) --
ARN of the configuration to use.

Revision (integer) --
The revision of the configuration to use.



NumberOfBrokerNodes (integer) --
The number of broker nodes in the cluster.

EnhancedMonitoring (string) --
Specifies which Apache Kafka metrics Amazon MSK gathers and sends to Amazon CloudWatch for this cluster.

OpenMonitoring (dict) --
The settings for open monitoring.

Prometheus (dict) --
Prometheus settings.

JmxExporter (dict) --
Indicates whether you want to enable or disable the JMX Exporter.

EnabledInBroker (boolean) --
Indicates whether you want to enable or disable the JMX Exporter.



NodeExporter (dict) --
Indicates whether you want to enable or disable the Node Exporter.

EnabledInBroker (boolean) --
Indicates whether you want to enable or disable the Node Exporter.







LoggingInfo (dict) --

BrokerLogs (dict) --
CloudWatchLogs (dict) --
Enabled (boolean) --
LogGroup (string) --


Firehose (dict) --
DeliveryStream (string) --
Enabled (boolean) --


S3 (dict) --
Bucket (string) --
Enabled (boolean) --
Prefix (string) --








TargetClusterInfo (dict) --
Information about cluster attributes after a cluster is updated.

BrokerEBSVolumeInfo (list) --
Specifies the size of the EBS volume and the ID of the associated broker.

(dict) --
Specifies the EBS volume upgrade information. The broker identifier must be set to the keyword ALL. This means the changes apply to all the brokers in the cluster.

KafkaBrokerNodeId (string) --
The ID of the broker to update.

VolumeSizeGB (integer) --
Size of the EBS volume to update.





ConfigurationInfo (dict) --
Information about the changes in the configuration of the brokers.

Arn (string) --
ARN of the configuration to use.

Revision (integer) --
The revision of the configuration to use.



NumberOfBrokerNodes (integer) --
The number of broker nodes in the cluster.

EnhancedMonitoring (string) --
Specifies which Apache Kafka metrics Amazon MSK gathers and sends to Amazon CloudWatch for this cluster.

OpenMonitoring (dict) --
The settings for open monitoring.

Prometheus (dict) --
Prometheus settings.

JmxExporter (dict) --
Indicates whether you want to enable or disable the JMX Exporter.

EnabledInBroker (boolean) --
Indicates whether you want to enable or disable the JMX Exporter.



NodeExporter (dict) --
Indicates whether you want to enable or disable the Node Exporter.

EnabledInBroker (boolean) --
Indicates whether you want to enable or disable the Node Exporter.







LoggingInfo (dict) --

BrokerLogs (dict) --
CloudWatchLogs (dict) --
Enabled (boolean) --
LogGroup (string) --


Firehose (dict) --
DeliveryStream (string) --
Enabled (boolean) --


S3 (dict) --
Bucket (string) --
Enabled (boolean) --
Prefix (string) --












NextToken (string) --
If the response of ListClusterOperations is truncated, it returns a NextToken in the response. This Nexttoken should be sent in the subsequent request to ListClusterOperations.







Exceptions

Kafka.Client.exceptions.BadRequestException
Kafka.Client.exceptions.InternalServerErrorException
Kafka.Client.exceptions.UnauthorizedException
Kafka.Client.exceptions.ForbiddenException


    :return: {
        'ClusterOperationInfoList': [
            {
                'ClientRequestId': 'string',
                'ClusterArn': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'EndTime': datetime(2015, 1, 1),
                'ErrorInfo': {
                    'ErrorCode': 'string',
                    'ErrorString': 'string'
                },
                'OperationArn': 'string',
                'OperationState': 'string',
                'OperationType': 'string',
                'SourceClusterInfo': {
                    'BrokerEBSVolumeInfo': [
                        {
                            'KafkaBrokerNodeId': 'string',
                            'VolumeSizeGB': 123
                        },
                    ],
                    'ConfigurationInfo': {
                        'Arn': 'string',
                        'Revision': 123
                    },
                    'NumberOfBrokerNodes': 123,
                    'EnhancedMonitoring': 'DEFAULT'|'PER_BROKER'|'PER_TOPIC_PER_BROKER',
                    'OpenMonitoring': {
                        'Prometheus': {
                            'JmxExporter': {
                                'EnabledInBroker': True|False
                            },
                            'NodeExporter': {
                                'EnabledInBroker': True|False
                            }
                        }
                    },
                    'LoggingInfo': {
                        'BrokerLogs': {
                            'CloudWatchLogs': {
                                'Enabled': True|False,
                                'LogGroup': 'string'
                            },
                            'Firehose': {
                                'DeliveryStream': 'string',
                                'Enabled': True|False
                            },
                            'S3': {
                                'Bucket': 'string',
                                'Enabled': True|False,
                                'Prefix': 'string'
                            }
                        }
                    }
                },
                'TargetClusterInfo': {
                    'BrokerEBSVolumeInfo': [
                        {
                            'KafkaBrokerNodeId': 'string',
                            'VolumeSizeGB': 123
                        },
                    ],
                    'ConfigurationInfo': {
                        'Arn': 'string',
                        'Revision': 123
                    },
                    'NumberOfBrokerNodes': 123,
                    'EnhancedMonitoring': 'DEFAULT'|'PER_BROKER'|'PER_TOPIC_PER_BROKER',
                    'OpenMonitoring': {
                        'Prometheus': {
                            'JmxExporter': {
                                'EnabledInBroker': True|False
                            },
                            'NodeExporter': {
                                'EnabledInBroker': True|False
                            }
                        }
                    },
                    'LoggingInfo': {
                        'BrokerLogs': {
                            'CloudWatchLogs': {
                                'Enabled': True|False,
                                'LogGroup': 'string'
                            },
                            'Firehose': {
                                'DeliveryStream': 'string',
                                'Enabled': True|False
                            },
                            'S3': {
                                'Bucket': 'string',
                                'Enabled': True|False,
                                'Prefix': 'string'
                            }
                        }
                    }
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    BrokerLogs (dict) --
    CloudWatchLogs (dict) --
    Enabled (boolean) --
    LogGroup (string) --
    
    
    Firehose (dict) --
    DeliveryStream (string) --
    Enabled (boolean) --
    
    
    S3 (dict) --
    Bucket (string) --
    Enabled (boolean) --
    Prefix (string) --
    
    
    
    
    
    """
    pass

def list_clusters(ClusterNameFilter=None, MaxResults=None, NextToken=None):
    """
    Returns a list of all the MSK clusters in the current Region.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_clusters(
        ClusterNameFilter='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type ClusterNameFilter: string
    :param ClusterNameFilter: Specify a prefix of the name of the clusters that you want to list. The service lists all the clusters whose names start with this prefix.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in the response. If there are more results, the response includes a NextToken parameter.

    :type NextToken: string
    :param NextToken: The paginated results marker. When the result of the operation is truncated, the call returns NextToken in the response. To get the next batch, provide this token in your next request.

    :rtype: dict

ReturnsResponse Syntax
{
    'ClusterInfoList': [
        {
            'ActiveOperationArn': 'string',
            'BrokerNodeGroupInfo': {
                'BrokerAZDistribution': 'DEFAULT',
                'ClientSubnets': [
                    'string',
                ],
                'InstanceType': 'string',
                'SecurityGroups': [
                    'string',
                ],
                'StorageInfo': {
                    'EbsStorageInfo': {
                        'VolumeSize': 123
                    }
                }
            },
            'ClientAuthentication': {
                'Tls': {
                    'CertificateAuthorityArnList': [
                        'string',
                    ]
                }
            },
            'ClusterArn': 'string',
            'ClusterName': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'CurrentBrokerSoftwareInfo': {
                'ConfigurationArn': 'string',
                'ConfigurationRevision': 123,
                'KafkaVersion': 'string'
            },
            'CurrentVersion': 'string',
            'EncryptionInfo': {
                'EncryptionAtRest': {
                    'DataVolumeKMSKeyId': 'string'
                },
                'EncryptionInTransit': {
                    'ClientBroker': 'TLS'|'TLS_PLAINTEXT'|'PLAINTEXT',
                    'InCluster': True|False
                }
            },
            'EnhancedMonitoring': 'DEFAULT'|'PER_BROKER'|'PER_TOPIC_PER_BROKER',
            'OpenMonitoring': {
                'Prometheus': {
                    'JmxExporter': {
                        'EnabledInBroker': True|False
                    },
                    'NodeExporter': {
                        'EnabledInBroker': True|False
                    }
                }
            },
            'LoggingInfo': {
                'BrokerLogs': {
                    'CloudWatchLogs': {
                        'Enabled': True|False,
                        'LogGroup': 'string'
                    },
                    'Firehose': {
                        'DeliveryStream': 'string',
                        'Enabled': True|False
                    },
                    'S3': {
                        'Bucket': 'string',
                        'Enabled': True|False,
                        'Prefix': 'string'
                    }
                }
            },
            'NumberOfBrokerNodes': 123,
            'State': 'ACTIVE'|'CREATING'|'UPDATING'|'DELETING'|'FAILED',
            'StateInfo': {
                'Code': 'string',
                'Message': 'string'
            },
            'Tags': {
                'string': 'string'
            },
            'ZookeeperConnectString': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
Successful response.

ClusterInfoList (list) --
Information on each of the MSK clusters in the response.

(dict) --
Returns information about a cluster.

ActiveOperationArn (string) --
Arn of active cluster operation.

BrokerNodeGroupInfo (dict) --
Information about the broker nodes.

BrokerAZDistribution (string) --
The distribution of broker nodes across Availability Zones. This is an optional parameter. If you don\'t specify it, Amazon MSK gives it the value DEFAULT. You can also explicitly set this parameter to the value DEFAULT. No other values are currently allowed.
Amazon MSK distributes the broker nodes evenly across the Availability Zones that correspond to the subnets you provide when you create the cluster.

ClientSubnets (list) --
The list of subnets to connect to in the client virtual private cloud (VPC). AWS creates elastic network interfaces inside these subnets. Client applications use elastic network interfaces to produce and consume data. Client subnets can\'t be in Availability Zone us-east-1e.

(string) --


InstanceType (string) --
The type of Amazon EC2 instances to use for Kafka brokers. The following instance types are allowed: kafka.m5.large, kafka.m5.xlarge, kafka.m5.2xlarge, kafka.m5.4xlarge, kafka.m5.12xlarge, and kafka.m5.24xlarge.

SecurityGroups (list) --
The AWS security groups to associate with the elastic network interfaces in order to specify who can connect to and communicate with the Amazon MSK cluster. If you don\'t specify a security group, Amazon MSK uses the default security group associated with the VPC.

(string) --


StorageInfo (dict) --
Contains information about storage volumes attached to MSK broker nodes.

EbsStorageInfo (dict) --
EBS volume information.

VolumeSize (integer) --
The size in GiB of the EBS volume for the data drive on each broker node.







ClientAuthentication (dict) --
Includes all client authentication information.

Tls (dict) --
Details for ClientAuthentication using TLS.

CertificateAuthorityArnList (list) --
List of ACM Certificate Authority ARNs.

(string) --






ClusterArn (string) --
The Amazon Resource Name (ARN) that uniquely identifies the cluster.

ClusterName (string) --
The name of the cluster.

CreationTime (datetime) --
The time when the cluster was created.

CurrentBrokerSoftwareInfo (dict) --
Information about the version of software currently deployed on the Kafka brokers in the cluster.

ConfigurationArn (string) --
The Amazon Resource Name (ARN) of the configuration used for the cluster. This field isn\'t visible in this preview release.

ConfigurationRevision (integer) --
The revision of the configuration to use. This field isn\'t visible in this preview release.

KafkaVersion (string) --
The version of Apache Kafka.



CurrentVersion (string) --
The current version of the MSK cluster.

EncryptionInfo (dict) --
Includes all encryption-related information.

EncryptionAtRest (dict) --
The data-volume encryption details.

DataVolumeKMSKeyId (string) --
The ARN of the AWS KMS key for encrypting data at rest. If you don\'t specify a KMS key, MSK creates one for you and uses it.



EncryptionInTransit (dict) --
The details for encryption in transit.

ClientBroker (string) --
Indicates the encryption setting for data in transit between clients and brokers. The following are the possible values.
TLS means that client-broker communication is enabled with TLS only.
TLS_PLAINTEXT means that client-broker communication is enabled for both TLS-encrypted, as well as plaintext data.
PLAINTEXT means that client-broker communication is enabled in plaintext only.
The default value is TLS_PLAINTEXT.

InCluster (boolean) --
When set to true, it indicates that data communication among the broker nodes of the cluster is encrypted. When set to false, the communication happens in plaintext.
The default value is true.





EnhancedMonitoring (string) --
Specifies which metrics are gathered for the MSK cluster. This property has three possible values: DEFAULT, PER_BROKER, and PER_TOPIC_PER_BROKER. For a list of the metrics associated with each of these three levels of monitoring, see Monitoring .

OpenMonitoring (dict) --
Settings for open monitoring using Prometheus.

Prometheus (dict) --
Prometheus settings.

JmxExporter (dict) --
Indicates whether you want to enable or disable the JMX Exporter.

EnabledInBroker (boolean) --
Indicates whether you want to enable or disable the JMX Exporter.



NodeExporter (dict) --
Indicates whether you want to enable or disable the Node Exporter.

EnabledInBroker (boolean) --
Indicates whether you want to enable or disable the Node Exporter.







LoggingInfo (dict) --

BrokerLogs (dict) --
CloudWatchLogs (dict) --
Enabled (boolean) --
LogGroup (string) --


Firehose (dict) --
DeliveryStream (string) --
Enabled (boolean) --


S3 (dict) --
Bucket (string) --
Enabled (boolean) --
Prefix (string) --






NumberOfBrokerNodes (integer) --
The number of broker nodes in the cluster.

State (string) --
The state of the cluster. The possible states are CREATING, ACTIVE, and FAILED.

StateInfo (dict) --

Code (string) --
Message (string) --


Tags (dict) --
Tags attached to the cluster.

(string) --
(string) --




ZookeeperConnectString (string) --
The connection string to use to connect to the Apache ZooKeeper cluster.





NextToken (string) --
The paginated results marker. When the result of a ListClusters operation is truncated, the call returns NextToken in the response. To get another batch of clusters, provide this token in your next request.







Exceptions

Kafka.Client.exceptions.BadRequestException
Kafka.Client.exceptions.InternalServerErrorException
Kafka.Client.exceptions.UnauthorizedException
Kafka.Client.exceptions.ForbiddenException


    :return: {
        'ClusterInfoList': [
            {
                'ActiveOperationArn': 'string',
                'BrokerNodeGroupInfo': {
                    'BrokerAZDistribution': 'DEFAULT',
                    'ClientSubnets': [
                        'string',
                    ],
                    'InstanceType': 'string',
                    'SecurityGroups': [
                        'string',
                    ],
                    'StorageInfo': {
                        'EbsStorageInfo': {
                            'VolumeSize': 123
                        }
                    }
                },
                'ClientAuthentication': {
                    'Tls': {
                        'CertificateAuthorityArnList': [
                            'string',
                        ]
                    }
                },
                'ClusterArn': 'string',
                'ClusterName': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'CurrentBrokerSoftwareInfo': {
                    'ConfigurationArn': 'string',
                    'ConfigurationRevision': 123,
                    'KafkaVersion': 'string'
                },
                'CurrentVersion': 'string',
                'EncryptionInfo': {
                    'EncryptionAtRest': {
                        'DataVolumeKMSKeyId': 'string'
                    },
                    'EncryptionInTransit': {
                        'ClientBroker': 'TLS'|'TLS_PLAINTEXT'|'PLAINTEXT',
                        'InCluster': True|False
                    }
                },
                'EnhancedMonitoring': 'DEFAULT'|'PER_BROKER'|'PER_TOPIC_PER_BROKER',
                'OpenMonitoring': {
                    'Prometheus': {
                        'JmxExporter': {
                            'EnabledInBroker': True|False
                        },
                        'NodeExporter': {
                            'EnabledInBroker': True|False
                        }
                    }
                },
                'LoggingInfo': {
                    'BrokerLogs': {
                        'CloudWatchLogs': {
                            'Enabled': True|False,
                            'LogGroup': 'string'
                        },
                        'Firehose': {
                            'DeliveryStream': 'string',
                            'Enabled': True|False
                        },
                        'S3': {
                            'Bucket': 'string',
                            'Enabled': True|False,
                            'Prefix': 'string'
                        }
                    }
                },
                'NumberOfBrokerNodes': 123,
                'State': 'ACTIVE'|'CREATING'|'UPDATING'|'DELETING'|'FAILED',
                'StateInfo': {
                    'Code': 'string',
                    'Message': 'string'
                },
                'Tags': {
                    'string': 'string'
                },
                'ZookeeperConnectString': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_configuration_revisions(Arn=None, MaxResults=None, NextToken=None):
    """
    Returns a list of all the MSK configurations in this Region.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_configuration_revisions(
        Arn='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type Arn: string
    :param Arn: [REQUIRED]\nThe Amazon Resource Name (ARN) that uniquely identifies an MSK configuration and all of its revisions.\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in the response. If there are more results, the response includes a NextToken parameter.

    :type NextToken: string
    :param NextToken: The paginated results marker. When the result of the operation is truncated, the call returns NextToken in the response. To get the next batch, provide this token in your next request.

    :rtype: dict

ReturnsResponse Syntax
{
    'NextToken': 'string',
    'Revisions': [
        {
            'CreationTime': datetime(2015, 1, 1),
            'Description': 'string',
            'Revision': 123
        },
    ]
}


Response Structure

(dict) --
200 response

NextToken (string) --
Paginated results marker.

Revisions (list) --
List of ConfigurationRevision objects.

(dict) --
Describes a configuration revision.

CreationTime (datetime) --
The time when the configuration revision was created.

Description (string) --
The description of the configuration revision.

Revision (integer) --
The revision number.











Exceptions

Kafka.Client.exceptions.BadRequestException
Kafka.Client.exceptions.UnauthorizedException
Kafka.Client.exceptions.InternalServerErrorException
Kafka.Client.exceptions.ForbiddenException
Kafka.Client.exceptions.NotFoundException
Kafka.Client.exceptions.ServiceUnavailableException


    :return: {
        'NextToken': 'string',
        'Revisions': [
            {
                'CreationTime': datetime(2015, 1, 1),
                'Description': 'string',
                'Revision': 123
            },
        ]
    }
    
    
    :returns: 
    Kafka.Client.exceptions.BadRequestException
    Kafka.Client.exceptions.UnauthorizedException
    Kafka.Client.exceptions.InternalServerErrorException
    Kafka.Client.exceptions.ForbiddenException
    Kafka.Client.exceptions.NotFoundException
    Kafka.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def list_configurations(MaxResults=None, NextToken=None):
    """
    Returns a list of all the MSK configurations in this Region.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_configurations(
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in the response. If there are more results, the response includes a NextToken parameter.

    :type NextToken: string
    :param NextToken: The paginated results marker. When the result of the operation is truncated, the call returns NextToken in the response. To get the next batch, provide this token in your next request.

    :rtype: dict

ReturnsResponse Syntax
{
    'Configurations': [
        {
            'Arn': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'Description': 'string',
            'KafkaVersions': [
                'string',
            ],
            'LatestRevision': {
                'CreationTime': datetime(2015, 1, 1),
                'Description': 'string',
                'Revision': 123
            },
            'Name': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
200 response

Configurations (list) --
An array of MSK configurations.

(dict) --
Represents an MSK Configuration.

Arn (string) --
The Amazon Resource Name (ARN) of the configuration.

CreationTime (datetime) --
The time when the configuration was created.

Description (string) --
The description of the configuration.

KafkaVersions (list) --
An array of the versions of Apache Kafka with which you can use this MSK configuration. You can use this configuration for an MSK cluster only if the Apache Kafka version specified for the cluster appears in this array.

(string) --


LatestRevision (dict) --
Latest revision of the configuration.

CreationTime (datetime) --
The time when the configuration revision was created.

Description (string) --
The description of the configuration revision.

Revision (integer) --
The revision number.



Name (string) --
The name of the configuration.





NextToken (string) --
The paginated results marker. When the result of a ListConfigurations operation is truncated, the call returns NextToken in the response. To get another batch of configurations, provide this token in your next request.







Exceptions

Kafka.Client.exceptions.ServiceUnavailableException
Kafka.Client.exceptions.BadRequestException
Kafka.Client.exceptions.UnauthorizedException
Kafka.Client.exceptions.InternalServerErrorException
Kafka.Client.exceptions.ForbiddenException


    :return: {
        'Configurations': [
            {
                'Arn': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'Description': 'string',
                'KafkaVersions': [
                    'string',
                ],
                'LatestRevision': {
                    'CreationTime': datetime(2015, 1, 1),
                    'Description': 'string',
                    'Revision': 123
                },
                'Name': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_kafka_versions(MaxResults=None, NextToken=None):
    """
    Returns a list of Kafka versions.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_kafka_versions(
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in the response. If there are more results, the response includes a NextToken parameter.

    :type NextToken: string
    :param NextToken: The paginated results marker. When the result of the operation is truncated, the call returns NextToken in the response. To get the next batch, provide this token in your next request.

    :rtype: dict

ReturnsResponse Syntax
{
    'KafkaVersions': [
        {
            'Version': 'string',
            'Status': 'ACTIVE'|'DEPRECATED'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
KafkaVersions (list) --
(dict) --
Version (string) --
Status (string) --




NextToken (string) --






Exceptions

Kafka.Client.exceptions.BadRequestException
Kafka.Client.exceptions.UnauthorizedException
Kafka.Client.exceptions.InternalServerErrorException
Kafka.Client.exceptions.ForbiddenException


    :return: {
        'KafkaVersions': [
            {
                'Version': 'string',
                'Status': 'ACTIVE'|'DEPRECATED'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (dict) --
    KafkaVersions (list) --
    (dict) --
    Version (string) --
    Status (string) --
    
    
    
    
    NextToken (string) --
    
    
    
    """
    pass

def list_nodes(ClusterArn=None, MaxResults=None, NextToken=None):
    """
    Returns a list of the broker nodes in the cluster.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_nodes(
        ClusterArn='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type ClusterArn: string
    :param ClusterArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that uniquely identifies the cluster.\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in the response. If there are more results, the response includes a NextToken parameter.

    :type NextToken: string
    :param NextToken: The paginated results marker. When the result of the operation is truncated, the call returns NextToken in the response. To get the next batch, provide this token in your next request.

    :rtype: dict

ReturnsResponse Syntax
{
    'NextToken': 'string',
    'NodeInfoList': [
        {
            'AddedToClusterTime': 'string',
            'BrokerNodeInfo': {
                'AttachedENIId': 'string',
                'BrokerId': 123.0,
                'ClientSubnet': 'string',
                'ClientVpcIpAddress': 'string',
                'CurrentBrokerSoftwareInfo': {
                    'ConfigurationArn': 'string',
                    'ConfigurationRevision': 123,
                    'KafkaVersion': 'string'
                },
                'Endpoints': [
                    'string',
                ]
            },
            'InstanceType': 'string',
            'NodeARN': 'string',
            'NodeType': 'BROKER',
            'ZookeeperNodeInfo': {
                'AttachedENIId': 'string',
                'ClientVpcIpAddress': 'string',
                'Endpoints': [
                    'string',
                ],
                'ZookeeperId': 123.0,
                'ZookeeperVersion': 'string'
            }
        },
    ]
}


Response Structure

(dict) --
Successful response.

NextToken (string) --
The paginated results marker. When the result of a ListNodes operation is truncated, the call returns NextToken in the response. To get another batch of nodes, provide this token in your next request.

NodeInfoList (list) --
List containing a NodeInfo object.

(dict) --
The node information object.

AddedToClusterTime (string) --
The start time.

BrokerNodeInfo (dict) --
The broker node info.

AttachedENIId (string) --
The attached elastic network interface of the broker.

BrokerId (float) --
The ID of the broker.

ClientSubnet (string) --
The client subnet to which this broker node belongs.

ClientVpcIpAddress (string) --
The virtual private cloud (VPC) of the client.

CurrentBrokerSoftwareInfo (dict) --
Information about the version of software currently deployed on the Kafka brokers in the cluster.

ConfigurationArn (string) --
The Amazon Resource Name (ARN) of the configuration used for the cluster. This field isn\'t visible in this preview release.

ConfigurationRevision (integer) --
The revision of the configuration to use. This field isn\'t visible in this preview release.

KafkaVersion (string) --
The version of Apache Kafka.



Endpoints (list) --
Endpoints for accessing the broker.

(string) --




InstanceType (string) --
The instance type.

NodeARN (string) --
The Amazon Resource Name (ARN) of the node.

NodeType (string) --
The node type.

ZookeeperNodeInfo (dict) --
The ZookeeperNodeInfo.

AttachedENIId (string) --
The attached elastic network interface of the broker.

ClientVpcIpAddress (string) --
The virtual private cloud (VPC) IP address of the client.

Endpoints (list) --
Endpoints for accessing the ZooKeeper.

(string) --


ZookeeperId (float) --
The role-specific ID for Zookeeper.

ZookeeperVersion (string) --
The version of Zookeeper.













Exceptions

Kafka.Client.exceptions.NotFoundException
Kafka.Client.exceptions.BadRequestException
Kafka.Client.exceptions.InternalServerErrorException
Kafka.Client.exceptions.ForbiddenException


    :return: {
        'NextToken': 'string',
        'NodeInfoList': [
            {
                'AddedToClusterTime': 'string',
                'BrokerNodeInfo': {
                    'AttachedENIId': 'string',
                    'BrokerId': 123.0,
                    'ClientSubnet': 'string',
                    'ClientVpcIpAddress': 'string',
                    'CurrentBrokerSoftwareInfo': {
                        'ConfigurationArn': 'string',
                        'ConfigurationRevision': 123,
                        'KafkaVersion': 'string'
                    },
                    'Endpoints': [
                        'string',
                    ]
                },
                'InstanceType': 'string',
                'NodeARN': 'string',
                'NodeType': 'BROKER',
                'ZookeeperNodeInfo': {
                    'AttachedENIId': 'string',
                    'ClientVpcIpAddress': 'string',
                    'Endpoints': [
                        'string',
                    ],
                    'ZookeeperId': 123.0,
                    'ZookeeperVersion': 'string'
                }
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_tags_for_resource(ResourceArn=None):
    """
    Returns a list of the tags associated with the specified resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        ResourceArn='string'
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that uniquely identifies the resource that\'s associated with the tags.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --Success response.

Tags (dict) --The key-value pair for the resource tag.

(string) --
(string) --









Exceptions

Kafka.Client.exceptions.NotFoundException
Kafka.Client.exceptions.BadRequestException
Kafka.Client.exceptions.InternalServerErrorException


    :return: {
        'Tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    Kafka.Client.exceptions.NotFoundException
    Kafka.Client.exceptions.BadRequestException
    Kafka.Client.exceptions.InternalServerErrorException
    
    """
    pass

def tag_resource(ResourceArn=None, Tags=None):
    """
    Adds tags to the specified MSK resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        ResourceArn='string',
        Tags={
            'string': 'string'
        }
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that uniquely identifies the resource that\'s associated with the tags.\n

    :type Tags: dict
    :param Tags: [REQUIRED]\nThe key-value pair for the resource tag.\n\n(string) --\n(string) --\n\n\n\n

    :returns: 
    Kafka.Client.exceptions.NotFoundException
    Kafka.Client.exceptions.BadRequestException
    Kafka.Client.exceptions.InternalServerErrorException
    
    """
    pass

def untag_resource(ResourceArn=None, TagKeys=None):
    """
    Removes the tags associated with the keys that are provided in the query.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        ResourceArn='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that uniquely identifies the resource that\'s associated with the tags.\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nTag keys must be unique for a given cluster. In addition, the following restrictions apply:\n\nEach tag key must be unique. If you add a tag with a key that\'s already in use, your new tag overwrites the existing key-value pair.\nYou can\'t start a tag key with aws: because this prefix is reserved for use by AWS. AWS creates tags that begin with this prefix on your behalf, but you can\'t edit or delete them.\nTag keys must be between 1 and 128 Unicode characters in length.\nTag keys must consist of the following characters: Unicode letters, digits, white space, and the following special characters: _ . / = + - @.\n\n\n(string) --\n\n

    :returns: 
    Kafka.Client.exceptions.NotFoundException
    Kafka.Client.exceptions.BadRequestException
    Kafka.Client.exceptions.InternalServerErrorException
    
    """
    pass

def update_broker_count(ClusterArn=None, CurrentVersion=None, TargetNumberOfBrokerNodes=None):
    """
    Updates the number of broker nodes in the cluster.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_broker_count(
        ClusterArn='string',
        CurrentVersion='string',
        TargetNumberOfBrokerNodes=123
    )
    
    
    :type ClusterArn: string
    :param ClusterArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that uniquely identifies the cluster.\n

    :type CurrentVersion: string
    :param CurrentVersion: [REQUIRED]\nThe version of cluster to update from. A successful operation will then generate a new version.\n

    :type TargetNumberOfBrokerNodes: integer
    :param TargetNumberOfBrokerNodes: [REQUIRED]\nThe number of broker nodes that you want the cluster to have after this operation completes successfully.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ClusterArn': 'string',
    'ClusterOperationArn': 'string'
}


Response Structure

(dict) --
Successful response.

ClusterArn (string) --
The Amazon Resource Name (ARN) of the cluster.

ClusterOperationArn (string) --
The Amazon Resource Name (ARN) of the cluster operation.







Exceptions

Kafka.Client.exceptions.ServiceUnavailableException
Kafka.Client.exceptions.BadRequestException
Kafka.Client.exceptions.UnauthorizedException
Kafka.Client.exceptions.InternalServerErrorException
Kafka.Client.exceptions.ForbiddenException


    :return: {
        'ClusterArn': 'string',
        'ClusterOperationArn': 'string'
    }
    
    
    :returns: 
    Kafka.Client.exceptions.ServiceUnavailableException
    Kafka.Client.exceptions.BadRequestException
    Kafka.Client.exceptions.UnauthorizedException
    Kafka.Client.exceptions.InternalServerErrorException
    Kafka.Client.exceptions.ForbiddenException
    
    """
    pass

def update_broker_storage(ClusterArn=None, CurrentVersion=None, TargetBrokerEBSVolumeInfo=None):
    """
    Updates the EBS storage associated with MSK brokers.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_broker_storage(
        ClusterArn='string',
        CurrentVersion='string',
        TargetBrokerEBSVolumeInfo=[
            {
                'KafkaBrokerNodeId': 'string',
                'VolumeSizeGB': 123
            },
        ]
    )
    
    
    :type ClusterArn: string
    :param ClusterArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that uniquely identifies the cluster.\n

    :type CurrentVersion: string
    :param CurrentVersion: [REQUIRED]\nThe version of cluster to update from. A successful operation will then generate a new version.\n

    :type TargetBrokerEBSVolumeInfo: list
    :param TargetBrokerEBSVolumeInfo: [REQUIRED]\nDescribes the target volume size and the ID of the broker to apply the update to.\n\n(dict) --Specifies the EBS volume upgrade information. The broker identifier must be set to the keyword ALL. This means the changes apply to all the brokers in the cluster.\n\nKafkaBrokerNodeId (string) -- [REQUIRED]The ID of the broker to update.\n\nVolumeSizeGB (integer) -- [REQUIRED]Size of the EBS volume to update.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ClusterArn': 'string',
    'ClusterOperationArn': 'string'
}


Response Structure

(dict) --
Successful response.

ClusterArn (string) --
The Amazon Resource Name (ARN) of the cluster.

ClusterOperationArn (string) --
The Amazon Resource Name (ARN) of the cluster operation.







Exceptions

Kafka.Client.exceptions.ServiceUnavailableException
Kafka.Client.exceptions.BadRequestException
Kafka.Client.exceptions.UnauthorizedException
Kafka.Client.exceptions.InternalServerErrorException
Kafka.Client.exceptions.ForbiddenException


    :return: {
        'ClusterArn': 'string',
        'ClusterOperationArn': 'string'
    }
    
    
    :returns: 
    Kafka.Client.exceptions.ServiceUnavailableException
    Kafka.Client.exceptions.BadRequestException
    Kafka.Client.exceptions.UnauthorizedException
    Kafka.Client.exceptions.InternalServerErrorException
    Kafka.Client.exceptions.ForbiddenException
    
    """
    pass

def update_cluster_configuration(ClusterArn=None, ConfigurationInfo=None, CurrentVersion=None):
    """
    Updates the cluster with the configuration that is specified in the request body.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_cluster_configuration(
        ClusterArn='string',
        ConfigurationInfo={
            'Arn': 'string',
            'Revision': 123
        },
        CurrentVersion='string'
    )
    
    
    :type ClusterArn: string
    :param ClusterArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that uniquely identifies the cluster.\n

    :type ConfigurationInfo: dict
    :param ConfigurationInfo: [REQUIRED]\nRepresents the configuration that you want MSK to use for the brokers in a cluster.\n\nArn (string) -- [REQUIRED]ARN of the configuration to use.\n\nRevision (integer) -- [REQUIRED]The revision of the configuration to use.\n\n\n

    :type CurrentVersion: string
    :param CurrentVersion: [REQUIRED]\nThe version of the cluster that needs to be updated.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ClusterArn': 'string',
    'ClusterOperationArn': 'string'
}


Response Structure

(dict) --
Successful response.

ClusterArn (string) --
The Amazon Resource Name (ARN) of the cluster.

ClusterOperationArn (string) --
The Amazon Resource Name (ARN) of the cluster operation.







Exceptions

Kafka.Client.exceptions.BadRequestException
Kafka.Client.exceptions.UnauthorizedException
Kafka.Client.exceptions.InternalServerErrorException
Kafka.Client.exceptions.ForbiddenException
Kafka.Client.exceptions.NotFoundException
Kafka.Client.exceptions.ServiceUnavailableException


    :return: {
        'ClusterArn': 'string',
        'ClusterOperationArn': 'string'
    }
    
    
    :returns: 
    Kafka.Client.exceptions.BadRequestException
    Kafka.Client.exceptions.UnauthorizedException
    Kafka.Client.exceptions.InternalServerErrorException
    Kafka.Client.exceptions.ForbiddenException
    Kafka.Client.exceptions.NotFoundException
    Kafka.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def update_monitoring(ClusterArn=None, CurrentVersion=None, EnhancedMonitoring=None, OpenMonitoring=None, LoggingInfo=None):
    """
    Updates the monitoring settings for the cluster. You can use this operation to specify which Apache Kafka metrics you want Amazon MSK to send to Amazon CloudWatch. You can also specify settings for open monitoring with Prometheus.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_monitoring(
        ClusterArn='string',
        CurrentVersion='string',
        EnhancedMonitoring='DEFAULT'|'PER_BROKER'|'PER_TOPIC_PER_BROKER',
        OpenMonitoring={
            'Prometheus': {
                'JmxExporter': {
                    'EnabledInBroker': True|False
                },
                'NodeExporter': {
                    'EnabledInBroker': True|False
                }
            }
        },
        LoggingInfo={
            'BrokerLogs': {
                'CloudWatchLogs': {
                    'Enabled': True|False,
                    'LogGroup': 'string'
                },
                'Firehose': {
                    'DeliveryStream': 'string',
                    'Enabled': True|False
                },
                'S3': {
                    'Bucket': 'string',
                    'Enabled': True|False,
                    'Prefix': 'string'
                }
            }
        }
    )
    
    
    :type ClusterArn: string
    :param ClusterArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that uniquely identifies the cluster.\n

    :type CurrentVersion: string
    :param CurrentVersion: [REQUIRED]\nThe version of the MSK cluster to update. Cluster versions aren\'t simple numbers. You can describe an MSK cluster to find its version. When this update operation is successful, it generates a new cluster version.\n

    :type EnhancedMonitoring: string
    :param EnhancedMonitoring: Specifies which Apache Kafka metrics Amazon MSK gathers and sends to Amazon CloudWatch for this cluster.

    :type OpenMonitoring: dict
    :param OpenMonitoring: The settings for open monitoring.\n\nPrometheus (dict) -- [REQUIRED]Prometheus settings.\n\nJmxExporter (dict) --Indicates whether you want to enable or disable the JMX Exporter.\n\nEnabledInBroker (boolean) -- [REQUIRED]Indicates whether you want to enable or disable the JMX Exporter.\n\n\n\nNodeExporter (dict) --Indicates whether you want to enable or disable the Node Exporter.\n\nEnabledInBroker (boolean) -- [REQUIRED]Indicates whether you want to enable or disable the Node Exporter.\n\n\n\n\n\n\n

    :type LoggingInfo: dict
    :param LoggingInfo: \nBrokerLogs (dict) -- [REQUIRED]\nCloudWatchLogs (dict) --\nEnabled (boolean) -- [REQUIRED]\nLogGroup (string) --\n\n\nFirehose (dict) --\nDeliveryStream (string) --\nEnabled (boolean) -- [REQUIRED]\n\n\nS3 (dict) --\nBucket (string) --\nEnabled (boolean) -- [REQUIRED]\nPrefix (string) --\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ClusterArn': 'string',
    'ClusterOperationArn': 'string'
}


Response Structure

(dict) --
HTTP Status Code 200: OK.

ClusterArn (string) --
The Amazon Resource Name (ARN) of the cluster.

ClusterOperationArn (string) --
The Amazon Resource Name (ARN) of the cluster operation.







Exceptions

Kafka.Client.exceptions.ServiceUnavailableException
Kafka.Client.exceptions.BadRequestException
Kafka.Client.exceptions.UnauthorizedException
Kafka.Client.exceptions.InternalServerErrorException
Kafka.Client.exceptions.ForbiddenException


    :return: {
        'ClusterArn': 'string',
        'ClusterOperationArn': 'string'
    }
    
    
    :returns: 
    Kafka.Client.exceptions.ServiceUnavailableException
    Kafka.Client.exceptions.BadRequestException
    Kafka.Client.exceptions.UnauthorizedException
    Kafka.Client.exceptions.InternalServerErrorException
    Kafka.Client.exceptions.ForbiddenException
    
    """
    pass

