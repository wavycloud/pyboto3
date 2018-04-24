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

def create_cluster(SubnetIds=None, HsmType=None, SourceBackupId=None):
    """
    Creates a new AWS CloudHSM cluster.
    See also: AWS API Documentation
    
    
    :example: response = client.create_cluster(
        SubnetIds=[
            'string',
        ],
        HsmType='string',
        SourceBackupId='string'
    )
    
    
    :type SubnetIds: list
    :param SubnetIds: [REQUIRED]
            The identifiers (IDs) of the subnets where you are creating the cluster. You must specify at least one subnet. If you specify multiple subnets, they must meet the following criteria:
            All subnets must be in the same virtual private cloud (VPC).
            You can specify only one subnet per Availability Zone.
            (string) --
            

    :type HsmType: string
    :param HsmType: [REQUIRED]
            The type of HSM to use in the cluster. Currently the only allowed value is hsm1.medium .
            

    :type SourceBackupId: string
    :param SourceBackupId: The identifier (ID) of the cluster backup to restore. Use this value to restore the cluster from a backup instead of creating a new cluster. To find the backup ID, use DescribeBackups .

    :rtype: dict
    :return: {
        'Cluster': {
            'BackupPolicy': 'DEFAULT',
            'ClusterId': 'string',
            'CreateTimestamp': datetime(2015, 1, 1),
            'Hsms': [
                {
                    'AvailabilityZone': 'string',
                    'ClusterId': 'string',
                    'SubnetId': 'string',
                    'EniId': 'string',
                    'EniIp': 'string',
                    'HsmId': 'string',
                    'State': 'CREATE_IN_PROGRESS'|'ACTIVE'|'DEGRADED'|'DELETE_IN_PROGRESS'|'DELETED',
                    'StateMessage': 'string'
                },
            ],
            'HsmType': 'string',
            'PreCoPassword': 'string',
            'SecurityGroup': 'string',
            'SourceBackupId': 'string',
            'State': 'CREATE_IN_PROGRESS'|'UNINITIALIZED'|'INITIALIZE_IN_PROGRESS'|'INITIALIZED'|'ACTIVE'|'UPDATE_IN_PROGRESS'|'DELETE_IN_PROGRESS'|'DELETED'|'DEGRADED',
            'StateMessage': 'string',
            'SubnetMapping': {
                'string': 'string'
            },
            'VpcId': 'string',
            'Certificates': {
                'ClusterCsr': 'string',
                'HsmCertificate': 'string',
                'AwsHardwareCertificate': 'string',
                'ManufacturerHardwareCertificate': 'string',
                'ClusterCertificate': 'string'
            }
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def create_hsm(ClusterId=None, AvailabilityZone=None, IpAddress=None):
    """
    Creates a new hardware security module (HSM) in the specified AWS CloudHSM cluster.
    See also: AWS API Documentation
    
    
    :example: response = client.create_hsm(
        ClusterId='string',
        AvailabilityZone='string',
        IpAddress='string'
    )
    
    
    :type ClusterId: string
    :param ClusterId: [REQUIRED]
            The identifier (ID) of the HSM's cluster. To find the cluster ID, use DescribeClusters .
            

    :type AvailabilityZone: string
    :param AvailabilityZone: [REQUIRED]
            The Availability Zone where you are creating the HSM. To find the cluster's Availability Zones, use DescribeClusters .
            

    :type IpAddress: string
    :param IpAddress: The HSM's IP address. If you specify an IP address, use an available address from the subnet that maps to the Availability Zone where you are creating the HSM. If you don't specify an IP address, one is chosen for you from that subnet.

    :rtype: dict
    :return: {
        'Hsm': {
            'AvailabilityZone': 'string',
            'ClusterId': 'string',
            'SubnetId': 'string',
            'EniId': 'string',
            'EniIp': 'string',
            'HsmId': 'string',
            'State': 'CREATE_IN_PROGRESS'|'ACTIVE'|'DEGRADED'|'DELETE_IN_PROGRESS'|'DELETED',
            'StateMessage': 'string'
        }
    }
    
    
    """
    pass

def delete_cluster(ClusterId=None):
    """
    Deletes the specified AWS CloudHSM cluster. Before you can delete a cluster, you must delete all HSMs in the cluster. To see if the cluster contains any HSMs, use  DescribeClusters . To delete an HSM, use  DeleteHsm .
    See also: AWS API Documentation
    
    
    :example: response = client.delete_cluster(
        ClusterId='string'
    )
    
    
    :type ClusterId: string
    :param ClusterId: [REQUIRED]
            The identifier (ID) of the cluster that you are deleting. To find the cluster ID, use DescribeClusters .
            

    :rtype: dict
    :return: {
        'Cluster': {
            'BackupPolicy': 'DEFAULT',
            'ClusterId': 'string',
            'CreateTimestamp': datetime(2015, 1, 1),
            'Hsms': [
                {
                    'AvailabilityZone': 'string',
                    'ClusterId': 'string',
                    'SubnetId': 'string',
                    'EniId': 'string',
                    'EniIp': 'string',
                    'HsmId': 'string',
                    'State': 'CREATE_IN_PROGRESS'|'ACTIVE'|'DEGRADED'|'DELETE_IN_PROGRESS'|'DELETED',
                    'StateMessage': 'string'
                },
            ],
            'HsmType': 'string',
            'PreCoPassword': 'string',
            'SecurityGroup': 'string',
            'SourceBackupId': 'string',
            'State': 'CREATE_IN_PROGRESS'|'UNINITIALIZED'|'INITIALIZE_IN_PROGRESS'|'INITIALIZED'|'ACTIVE'|'UPDATE_IN_PROGRESS'|'DELETE_IN_PROGRESS'|'DELETED'|'DEGRADED',
            'StateMessage': 'string',
            'SubnetMapping': {
                'string': 'string'
            },
            'VpcId': 'string',
            'Certificates': {
                'ClusterCsr': 'string',
                'HsmCertificate': 'string',
                'AwsHardwareCertificate': 'string',
                'ManufacturerHardwareCertificate': 'string',
                'ClusterCertificate': 'string'
            }
        }
    }
    
    
    """
    pass

def delete_hsm(ClusterId=None, HsmId=None, EniId=None, EniIp=None):
    """
    Deletes the specified HSM. To specify an HSM, you can use its identifier (ID), the IP address of the HSM's elastic network interface (ENI), or the ID of the HSM's ENI. You need to specify only one of these values. To find these values, use  DescribeClusters .
    See also: AWS API Documentation
    
    
    :example: response = client.delete_hsm(
        ClusterId='string',
        HsmId='string',
        EniId='string',
        EniIp='string'
    )
    
    
    :type ClusterId: string
    :param ClusterId: [REQUIRED]
            The identifier (ID) of the cluster that contains the HSM that you are deleting.
            

    :type HsmId: string
    :param HsmId: The identifier (ID) of the HSM that you are deleting.

    :type EniId: string
    :param EniId: The identifier (ID) of the elastic network interface (ENI) of the HSM that you are deleting.

    :type EniIp: string
    :param EniIp: The IP address of the elastic network interface (ENI) of the HSM that you are deleting.

    :rtype: dict
    :return: {
        'HsmId': 'string'
    }
    
    
    """
    pass

def describe_backups(NextToken=None, MaxResults=None, Filters=None):
    """
    Gets information about backups of AWS CloudHSM clusters.
    This is a paginated operation, which means that each response might contain only a subset of all the backups. When the response contains only a subset of backups, it includes a NextToken value. Use this value in a subsequent DescribeBackups request to get more backups. When you receive a response with no NextToken (or an empty or null value), that means there are no more backups to get.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_backups(
        NextToken='string',
        MaxResults=123,
        Filters={
            'string': [
                'string',
            ]
        }
    )
    
    
    :type NextToken: string
    :param NextToken: The NextToken value that you received in the previous response. Use this value to get more backups.

    :type MaxResults: integer
    :param MaxResults: The maximum number of backups to return in the response. When there are more backups than the number you specify, the response contains a NextToken value.

    :type Filters: dict
    :param Filters: One or more filters to limit the items returned in the response.
            Use the backupIds filter to return only the specified backups. Specify backups by their backup identifier (ID).
            Use the clusterIds filter to return only the backups for the specified clusters. Specify clusters by their cluster identifier (ID).
            Use the states filter to return only backups that match the specified state.
            (string) --
            (list) --
            (string) --
            
            

    :rtype: dict
    :return: {
        'Backups': [
            {
                'BackupId': 'string',
                'BackupState': 'CREATE_IN_PROGRESS'|'READY'|'DELETED',
                'ClusterId': 'string',
                'CreateTimestamp': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def describe_clusters(Filters=None, NextToken=None, MaxResults=None):
    """
    Gets information about AWS CloudHSM clusters.
    This is a paginated operation, which means that each response might contain only a subset of all the clusters. When the response contains only a subset of clusters, it includes a NextToken value. Use this value in a subsequent DescribeClusters request to get more clusters. When you receive a response with no NextToken (or an empty or null value), that means there are no more clusters to get.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_clusters(
        Filters={
            'string': [
                'string',
            ]
        },
        NextToken='string',
        MaxResults=123
    )
    
    
    :type Filters: dict
    :param Filters: One or more filters to limit the items returned in the response.
            Use the clusterIds filter to return only the specified clusters. Specify clusters by their cluster identifier (ID).
            Use the vpcIds filter to return only the clusters in the specified virtual private clouds (VPCs). Specify VPCs by their VPC identifier (ID).
            Use the states filter to return only clusters that match the specified state.
            (string) --
            (list) --
            (string) --
            
            

    :type NextToken: string
    :param NextToken: The NextToken value that you received in the previous response. Use this value to get more clusters.

    :type MaxResults: integer
    :param MaxResults: The maximum number of clusters to return in the response. When there are more clusters than the number you specify, the response contains a NextToken value.

    :rtype: dict
    :return: {
        'Clusters': [
            {
                'BackupPolicy': 'DEFAULT',
                'ClusterId': 'string',
                'CreateTimestamp': datetime(2015, 1, 1),
                'Hsms': [
                    {
                        'AvailabilityZone': 'string',
                        'ClusterId': 'string',
                        'SubnetId': 'string',
                        'EniId': 'string',
                        'EniIp': 'string',
                        'HsmId': 'string',
                        'State': 'CREATE_IN_PROGRESS'|'ACTIVE'|'DEGRADED'|'DELETE_IN_PROGRESS'|'DELETED',
                        'StateMessage': 'string'
                    },
                ],
                'HsmType': 'string',
                'PreCoPassword': 'string',
                'SecurityGroup': 'string',
                'SourceBackupId': 'string',
                'State': 'CREATE_IN_PROGRESS'|'UNINITIALIZED'|'INITIALIZE_IN_PROGRESS'|'INITIALIZED'|'ACTIVE'|'UPDATE_IN_PROGRESS'|'DELETE_IN_PROGRESS'|'DELETED'|'DEGRADED',
                'StateMessage': 'string',
                'SubnetMapping': {
                    'string': 'string'
                },
                'VpcId': 'string',
                'Certificates': {
                    'ClusterCsr': 'string',
                    'HsmCertificate': 'string',
                    'AwsHardwareCertificate': 'string',
                    'ManufacturerHardwareCertificate': 'string',
                    'ClusterCertificate': 'string'
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
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

def initialize_cluster(ClusterId=None, SignedCert=None, TrustAnchor=None):
    """
    Claims an AWS CloudHSM cluster by submitting the cluster certificate issued by your issuing certificate authority (CA) and the CA's root certificate. Before you can claim a cluster, you must sign the cluster's certificate signing request (CSR) with your issuing CA. To get the cluster's CSR, use  DescribeClusters .
    See also: AWS API Documentation
    
    
    :example: response = client.initialize_cluster(
        ClusterId='string',
        SignedCert='string',
        TrustAnchor='string'
    )
    
    
    :type ClusterId: string
    :param ClusterId: [REQUIRED]
            The identifier (ID) of the cluster that you are claiming. To find the cluster ID, use DescribeClusters .
            

    :type SignedCert: string
    :param SignedCert: [REQUIRED]
            The cluster certificate issued (signed) by your issuing certificate authority (CA). The certificate must be in PEM format and can contain a maximum of 5000 characters.
            

    :type TrustAnchor: string
    :param TrustAnchor: [REQUIRED]
            The issuing certificate of the issuing certificate authority (CA) that issued (signed) the cluster certificate. This can be a root (self-signed) certificate or a certificate chain that begins with the certificate that issued the cluster certificate and ends with a root certificate. The certificate or certificate chain must be in PEM format and can contain a maximum of 5000 characters.
            

    :rtype: dict
    :return: {
        'State': 'CREATE_IN_PROGRESS'|'UNINITIALIZED'|'INITIALIZE_IN_PROGRESS'|'INITIALIZED'|'ACTIVE'|'UPDATE_IN_PROGRESS'|'DELETE_IN_PROGRESS'|'DELETED'|'DEGRADED',
        'StateMessage': 'string'
    }
    
    
    """
    pass

def list_tags(ResourceId=None, NextToken=None, MaxResults=None):
    """
    Gets a list of tags for the specified AWS CloudHSM cluster.
    This is a paginated operation, which means that each response might contain only a subset of all the tags. When the response contains only a subset of tags, it includes a NextToken value. Use this value in a subsequent ListTags request to get more tags. When you receive a response with no NextToken (or an empty or null value), that means there are no more tags to get.
    See also: AWS API Documentation
    
    
    :example: response = client.list_tags(
        ResourceId='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type ResourceId: string
    :param ResourceId: [REQUIRED]
            The cluster identifier (ID) for the cluster whose tags you are getting. To find the cluster ID, use DescribeClusters .
            

    :type NextToken: string
    :param NextToken: The NextToken value that you received in the previous response. Use this value to get more tags.

    :type MaxResults: integer
    :param MaxResults: The maximum number of tags to return in the response. When there are more tags than the number you specify, the response contains a NextToken value.

    :rtype: dict
    :return: {
        'TagList': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def tag_resource(ResourceId=None, TagList=None):
    """
    Adds or overwrites one or more tags for the specified AWS CloudHSM cluster.
    See also: AWS API Documentation
    
    
    :example: response = client.tag_resource(
        ResourceId='string',
        TagList=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ResourceId: string
    :param ResourceId: [REQUIRED]
            The cluster identifier (ID) for the cluster that you are tagging. To find the cluster ID, use DescribeClusters .
            

    :type TagList: list
    :param TagList: [REQUIRED]
            A list of one or more tags.
            (dict) --Contains a tag. A tag is a key-value pair.
            Key (string) -- [REQUIRED]The key of the tag.
            Value (string) -- [REQUIRED]The value of the tag.
            
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_resource(ResourceId=None, TagKeyList=None):
    """
    Removes the specified tag or tags from the specified AWS CloudHSM cluster.
    See also: AWS API Documentation
    
    
    :example: response = client.untag_resource(
        ResourceId='string',
        TagKeyList=[
            'string',
        ]
    )
    
    
    :type ResourceId: string
    :param ResourceId: [REQUIRED]
            The cluster identifier (ID) for the cluster whose tags you are removing. To find the cluster ID, use DescribeClusters .
            

    :type TagKeyList: list
    :param TagKeyList: [REQUIRED]
            A list of one or more tag keys for the tags that you are removing. Specify only the tag keys, not the tag values.
            (string) --
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

