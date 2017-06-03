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

def add_tags(ARN=None, TagList=None):
    """
    Attaches tags to an existing Elasticsearch domain. Tags are a set of case-sensitive key value pairs. An Elasticsearch domain may have up to 10 tags. See Tagging Amazon Elasticsearch Service Domains for more information.
    See also: AWS API Documentation
    
    
    :example: response = client.add_tags(
        ARN='string',
        TagList=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ARN: string
    :param ARN: [REQUIRED]
            Specify the ARN for which you want to add the tags.
            

    :type TagList: list
    :param TagList: [REQUIRED]
            List of Tag that need to be added for the Elasticsearch domain.
            (dict) --Specifies a key value pair for a resource tag.
            Key (string) -- [REQUIRED]Specifies the TagKey , the name of the tag. Tag keys must be unique for the Elasticsearch domain to which they are attached.
            Value (string) -- [REQUIRED]Specifies the TagValue , the value assigned to the corresponding tag key. Tag values can be null and do not have to be unique in a tag set. For example, you can have a key value pair in a tag set of project : Trinity and cost-center : Trinity
            
            

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

def create_elasticsearch_domain(DomainName=None, ElasticsearchVersion=None, ElasticsearchClusterConfig=None, EBSOptions=None, AccessPolicies=None, SnapshotOptions=None, AdvancedOptions=None):
    """
    Creates a new Elasticsearch domain. For more information, see Creating Elasticsearch Domains in the Amazon Elasticsearch Service Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.create_elasticsearch_domain(
        DomainName='string',
        ElasticsearchVersion='string',
        ElasticsearchClusterConfig={
            'InstanceType': 'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch'|'d2.xlarge.elasticsearch'|'d2.2xlarge.elasticsearch'|'d2.4xlarge.elasticsearch'|'d2.8xlarge.elasticsearch'|'c4.large.elasticsearch'|'c4.xlarge.elasticsearch'|'c4.2xlarge.elasticsearch'|'c4.4xlarge.elasticsearch'|'c4.8xlarge.elasticsearch'|'r4.large.elasticsearch'|'r4.xlarge.elasticsearch'|'r4.2xlarge.elasticsearch'|'r4.4xlarge.elasticsearch'|'r4.8xlarge.elasticsearch'|'r4.16xlarge.elasticsearch',
            'InstanceCount': 123,
            'DedicatedMasterEnabled': True|False,
            'ZoneAwarenessEnabled': True|False,
            'DedicatedMasterType': 'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch'|'d2.xlarge.elasticsearch'|'d2.2xlarge.elasticsearch'|'d2.4xlarge.elasticsearch'|'d2.8xlarge.elasticsearch'|'c4.large.elasticsearch'|'c4.xlarge.elasticsearch'|'c4.2xlarge.elasticsearch'|'c4.4xlarge.elasticsearch'|'c4.8xlarge.elasticsearch'|'r4.large.elasticsearch'|'r4.xlarge.elasticsearch'|'r4.2xlarge.elasticsearch'|'r4.4xlarge.elasticsearch'|'r4.8xlarge.elasticsearch'|'r4.16xlarge.elasticsearch',
            'DedicatedMasterCount': 123
        },
        EBSOptions={
            'EBSEnabled': True|False,
            'VolumeType': 'standard'|'gp2'|'io1',
            'VolumeSize': 123,
            'Iops': 123
        },
        AccessPolicies='string',
        SnapshotOptions={
            'AutomatedSnapshotStartHour': 123
        },
        AdvancedOptions={
            'string': 'string'
        }
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]
            The name of the Elasticsearch domain that you are creating. Domain names are unique across the domains owned by an account within an AWS region. Domain names must start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).
            

    :type ElasticsearchVersion: string
    :param ElasticsearchVersion: String of format X.Y to specify version for the Elasticsearch domain eg. '1.5' or '2.3'. For more information, see Creating Elasticsearch Domains in the Amazon Elasticsearch Service Developer Guide .

    :type ElasticsearchClusterConfig: dict
    :param ElasticsearchClusterConfig: Configuration options for an Elasticsearch domain. Specifies the instance type and number of instances in the domain cluster.
            InstanceType (string) --The instance type for an Elasticsearch cluster.
            InstanceCount (integer) --The number of instances in the specified domain cluster.
            DedicatedMasterEnabled (boolean) --A boolean value to indicate whether a dedicated master node is enabled. See About Dedicated Master Nodes for more information.
            ZoneAwarenessEnabled (boolean) --A boolean value to indicate whether zone awareness is enabled. See About Zone Awareness for more information.
            DedicatedMasterType (string) --The instance type for a dedicated master node.
            DedicatedMasterCount (integer) --Total number of dedicated master nodes, active and on standby, for the cluster.
            

    :type EBSOptions: dict
    :param EBSOptions: Options to enable, disable and specify the type and size of EBS storage volumes.
            EBSEnabled (boolean) --Specifies whether EBS-based storage is enabled.
            VolumeType (string) --Specifies the volume type for EBS-based storage.
            VolumeSize (integer) --Integer to specify the size of an EBS volume.
            Iops (integer) --Specifies the IOPD for a Provisioned IOPS EBS volume (SSD).
            

    :type AccessPolicies: string
    :param AccessPolicies: IAM access policy as a JSON-formatted string.

    :type SnapshotOptions: dict
    :param SnapshotOptions: Option to set time, in UTC format, of the daily automated snapshot. Default value is 0 hours.
            AutomatedSnapshotStartHour (integer) --Specifies the time, in UTC format, when the service takes a daily automated snapshot of the specified Elasticsearch domain. Default value is 0 hours.
            

    :type AdvancedOptions: dict
    :param AdvancedOptions: Option to allow references to indices in an HTTP request body. Must be false when configuring access to individual sub-resources. By default, the value is true . See Configuration Advanced Options for more information.
            (string) --
            (string) --
            

    :rtype: dict
    :return: {
        'DomainStatus': {
            'DomainId': 'string',
            'DomainName': 'string',
            'ARN': 'string',
            'Created': True|False,
            'Deleted': True|False,
            'Endpoint': 'string',
            'Processing': True|False,
            'ElasticsearchVersion': 'string',
            'ElasticsearchClusterConfig': {
                'InstanceType': 'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch'|'d2.xlarge.elasticsearch'|'d2.2xlarge.elasticsearch'|'d2.4xlarge.elasticsearch'|'d2.8xlarge.elasticsearch'|'c4.large.elasticsearch'|'c4.xlarge.elasticsearch'|'c4.2xlarge.elasticsearch'|'c4.4xlarge.elasticsearch'|'c4.8xlarge.elasticsearch'|'r4.large.elasticsearch'|'r4.xlarge.elasticsearch'|'r4.2xlarge.elasticsearch'|'r4.4xlarge.elasticsearch'|'r4.8xlarge.elasticsearch'|'r4.16xlarge.elasticsearch',
                'InstanceCount': 123,
                'DedicatedMasterEnabled': True|False,
                'ZoneAwarenessEnabled': True|False,
                'DedicatedMasterType': 'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch'|'d2.xlarge.elasticsearch'|'d2.2xlarge.elasticsearch'|'d2.4xlarge.elasticsearch'|'d2.8xlarge.elasticsearch'|'c4.large.elasticsearch'|'c4.xlarge.elasticsearch'|'c4.2xlarge.elasticsearch'|'c4.4xlarge.elasticsearch'|'c4.8xlarge.elasticsearch'|'r4.large.elasticsearch'|'r4.xlarge.elasticsearch'|'r4.2xlarge.elasticsearch'|'r4.4xlarge.elasticsearch'|'r4.8xlarge.elasticsearch'|'r4.16xlarge.elasticsearch',
                'DedicatedMasterCount': 123
            },
            'EBSOptions': {
                'EBSEnabled': True|False,
                'VolumeType': 'standard'|'gp2'|'io1',
                'VolumeSize': 123,
                'Iops': 123
            },
            'AccessPolicies': 'string',
            'SnapshotOptions': {
                'AutomatedSnapshotStartHour': 123
            },
            'AdvancedOptions': {
                'string': 'string'
            }
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def delete_elasticsearch_domain(DomainName=None):
    """
    Permanently deletes the specified Elasticsearch domain and all of its data. Once a domain is deleted, it cannot be recovered.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_elasticsearch_domain(
        DomainName='string'
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]
            The name of the Elasticsearch domain that you want to permanently delete.
            

    :rtype: dict
    :return: {
        'DomainStatus': {
            'DomainId': 'string',
            'DomainName': 'string',
            'ARN': 'string',
            'Created': True|False,
            'Deleted': True|False,
            'Endpoint': 'string',
            'Processing': True|False,
            'ElasticsearchVersion': 'string',
            'ElasticsearchClusterConfig': {
                'InstanceType': 'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch'|'d2.xlarge.elasticsearch'|'d2.2xlarge.elasticsearch'|'d2.4xlarge.elasticsearch'|'d2.8xlarge.elasticsearch'|'c4.large.elasticsearch'|'c4.xlarge.elasticsearch'|'c4.2xlarge.elasticsearch'|'c4.4xlarge.elasticsearch'|'c4.8xlarge.elasticsearch'|'r4.large.elasticsearch'|'r4.xlarge.elasticsearch'|'r4.2xlarge.elasticsearch'|'r4.4xlarge.elasticsearch'|'r4.8xlarge.elasticsearch'|'r4.16xlarge.elasticsearch',
                'InstanceCount': 123,
                'DedicatedMasterEnabled': True|False,
                'ZoneAwarenessEnabled': True|False,
                'DedicatedMasterType': 'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch'|'d2.xlarge.elasticsearch'|'d2.2xlarge.elasticsearch'|'d2.4xlarge.elasticsearch'|'d2.8xlarge.elasticsearch'|'c4.large.elasticsearch'|'c4.xlarge.elasticsearch'|'c4.2xlarge.elasticsearch'|'c4.4xlarge.elasticsearch'|'c4.8xlarge.elasticsearch'|'r4.large.elasticsearch'|'r4.xlarge.elasticsearch'|'r4.2xlarge.elasticsearch'|'r4.4xlarge.elasticsearch'|'r4.8xlarge.elasticsearch'|'r4.16xlarge.elasticsearch',
                'DedicatedMasterCount': 123
            },
            'EBSOptions': {
                'EBSEnabled': True|False,
                'VolumeType': 'standard'|'gp2'|'io1',
                'VolumeSize': 123,
                'Iops': 123
            },
            'AccessPolicies': 'string',
            'SnapshotOptions': {
                'AutomatedSnapshotStartHour': 123
            },
            'AdvancedOptions': {
                'string': 'string'
            }
        }
    }
    
    
    """
    pass

def describe_elasticsearch_domain(DomainName=None):
    """
    Returns domain configuration information about the specified Elasticsearch domain, including the domain ID, domain endpoint, and domain ARN.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_elasticsearch_domain(
        DomainName='string'
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]
            The name of the Elasticsearch domain for which you want information.
            

    :rtype: dict
    :return: {
        'DomainStatus': {
            'DomainId': 'string',
            'DomainName': 'string',
            'ARN': 'string',
            'Created': True|False,
            'Deleted': True|False,
            'Endpoint': 'string',
            'Processing': True|False,
            'ElasticsearchVersion': 'string',
            'ElasticsearchClusterConfig': {
                'InstanceType': 'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch'|'d2.xlarge.elasticsearch'|'d2.2xlarge.elasticsearch'|'d2.4xlarge.elasticsearch'|'d2.8xlarge.elasticsearch'|'c4.large.elasticsearch'|'c4.xlarge.elasticsearch'|'c4.2xlarge.elasticsearch'|'c4.4xlarge.elasticsearch'|'c4.8xlarge.elasticsearch'|'r4.large.elasticsearch'|'r4.xlarge.elasticsearch'|'r4.2xlarge.elasticsearch'|'r4.4xlarge.elasticsearch'|'r4.8xlarge.elasticsearch'|'r4.16xlarge.elasticsearch',
                'InstanceCount': 123,
                'DedicatedMasterEnabled': True|False,
                'ZoneAwarenessEnabled': True|False,
                'DedicatedMasterType': 'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch'|'d2.xlarge.elasticsearch'|'d2.2xlarge.elasticsearch'|'d2.4xlarge.elasticsearch'|'d2.8xlarge.elasticsearch'|'c4.large.elasticsearch'|'c4.xlarge.elasticsearch'|'c4.2xlarge.elasticsearch'|'c4.4xlarge.elasticsearch'|'c4.8xlarge.elasticsearch'|'r4.large.elasticsearch'|'r4.xlarge.elasticsearch'|'r4.2xlarge.elasticsearch'|'r4.4xlarge.elasticsearch'|'r4.8xlarge.elasticsearch'|'r4.16xlarge.elasticsearch',
                'DedicatedMasterCount': 123
            },
            'EBSOptions': {
                'EBSEnabled': True|False,
                'VolumeType': 'standard'|'gp2'|'io1',
                'VolumeSize': 123,
                'Iops': 123
            },
            'AccessPolicies': 'string',
            'SnapshotOptions': {
                'AutomatedSnapshotStartHour': 123
            },
            'AdvancedOptions': {
                'string': 'string'
            }
        }
    }
    
    
    """
    pass

def describe_elasticsearch_domain_config(DomainName=None):
    """
    Provides cluster configuration information about the specified Elasticsearch domain, such as the state, creation date, update version, and update date for cluster options.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_elasticsearch_domain_config(
        DomainName='string'
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]
            The Elasticsearch domain that you want to get information about.
            

    :rtype: dict
    :return: {
        'DomainConfig': {
            'ElasticsearchVersion': {
                'Options': 'string',
                'Status': {
                    'CreationDate': datetime(2015, 1, 1),
                    'UpdateDate': datetime(2015, 1, 1),
                    'UpdateVersion': 123,
                    'State': 'RequiresIndexDocuments'|'Processing'|'Active',
                    'PendingDeletion': True|False
                }
            },
            'ElasticsearchClusterConfig': {
                'Options': {
                    'InstanceType': 'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch'|'d2.xlarge.elasticsearch'|'d2.2xlarge.elasticsearch'|'d2.4xlarge.elasticsearch'|'d2.8xlarge.elasticsearch'|'c4.large.elasticsearch'|'c4.xlarge.elasticsearch'|'c4.2xlarge.elasticsearch'|'c4.4xlarge.elasticsearch'|'c4.8xlarge.elasticsearch'|'r4.large.elasticsearch'|'r4.xlarge.elasticsearch'|'r4.2xlarge.elasticsearch'|'r4.4xlarge.elasticsearch'|'r4.8xlarge.elasticsearch'|'r4.16xlarge.elasticsearch',
                    'InstanceCount': 123,
                    'DedicatedMasterEnabled': True|False,
                    'ZoneAwarenessEnabled': True|False,
                    'DedicatedMasterType': 'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch'|'d2.xlarge.elasticsearch'|'d2.2xlarge.elasticsearch'|'d2.4xlarge.elasticsearch'|'d2.8xlarge.elasticsearch'|'c4.large.elasticsearch'|'c4.xlarge.elasticsearch'|'c4.2xlarge.elasticsearch'|'c4.4xlarge.elasticsearch'|'c4.8xlarge.elasticsearch'|'r4.large.elasticsearch'|'r4.xlarge.elasticsearch'|'r4.2xlarge.elasticsearch'|'r4.4xlarge.elasticsearch'|'r4.8xlarge.elasticsearch'|'r4.16xlarge.elasticsearch',
                    'DedicatedMasterCount': 123
                },
                'Status': {
                    'CreationDate': datetime(2015, 1, 1),
                    'UpdateDate': datetime(2015, 1, 1),
                    'UpdateVersion': 123,
                    'State': 'RequiresIndexDocuments'|'Processing'|'Active',
                    'PendingDeletion': True|False
                }
            },
            'EBSOptions': {
                'Options': {
                    'EBSEnabled': True|False,
                    'VolumeType': 'standard'|'gp2'|'io1',
                    'VolumeSize': 123,
                    'Iops': 123
                },
                'Status': {
                    'CreationDate': datetime(2015, 1, 1),
                    'UpdateDate': datetime(2015, 1, 1),
                    'UpdateVersion': 123,
                    'State': 'RequiresIndexDocuments'|'Processing'|'Active',
                    'PendingDeletion': True|False
                }
            },
            'AccessPolicies': {
                'Options': 'string',
                'Status': {
                    'CreationDate': datetime(2015, 1, 1),
                    'UpdateDate': datetime(2015, 1, 1),
                    'UpdateVersion': 123,
                    'State': 'RequiresIndexDocuments'|'Processing'|'Active',
                    'PendingDeletion': True|False
                }
            },
            'SnapshotOptions': {
                'Options': {
                    'AutomatedSnapshotStartHour': 123
                },
                'Status': {
                    'CreationDate': datetime(2015, 1, 1),
                    'UpdateDate': datetime(2015, 1, 1),
                    'UpdateVersion': 123,
                    'State': 'RequiresIndexDocuments'|'Processing'|'Active',
                    'PendingDeletion': True|False
                }
            },
            'AdvancedOptions': {
                'Options': {
                    'string': 'string'
                },
                'Status': {
                    'CreationDate': datetime(2015, 1, 1),
                    'UpdateDate': datetime(2015, 1, 1),
                    'UpdateVersion': 123,
                    'State': 'RequiresIndexDocuments'|'Processing'|'Active',
                    'PendingDeletion': True|False
                }
            }
        }
    }
    
    
    """
    pass

def describe_elasticsearch_domains(DomainNames=None):
    """
    Returns domain configuration information about the specified Elasticsearch domains, including the domain ID, domain endpoint, and domain ARN.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_elasticsearch_domains(
        DomainNames=[
            'string',
        ]
    )
    
    
    :type DomainNames: list
    :param DomainNames: [REQUIRED]
            The Elasticsearch domains for which you want information.
            (string) --The name of an Elasticsearch domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).
            

    :rtype: dict
    :return: {
        'DomainStatusList': [
            {
                'DomainId': 'string',
                'DomainName': 'string',
                'ARN': 'string',
                'Created': True|False,
                'Deleted': True|False,
                'Endpoint': 'string',
                'Processing': True|False,
                'ElasticsearchVersion': 'string',
                'ElasticsearchClusterConfig': {
                    'InstanceType': 'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch'|'d2.xlarge.elasticsearch'|'d2.2xlarge.elasticsearch'|'d2.4xlarge.elasticsearch'|'d2.8xlarge.elasticsearch'|'c4.large.elasticsearch'|'c4.xlarge.elasticsearch'|'c4.2xlarge.elasticsearch'|'c4.4xlarge.elasticsearch'|'c4.8xlarge.elasticsearch'|'r4.large.elasticsearch'|'r4.xlarge.elasticsearch'|'r4.2xlarge.elasticsearch'|'r4.4xlarge.elasticsearch'|'r4.8xlarge.elasticsearch'|'r4.16xlarge.elasticsearch',
                    'InstanceCount': 123,
                    'DedicatedMasterEnabled': True|False,
                    'ZoneAwarenessEnabled': True|False,
                    'DedicatedMasterType': 'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch'|'d2.xlarge.elasticsearch'|'d2.2xlarge.elasticsearch'|'d2.4xlarge.elasticsearch'|'d2.8xlarge.elasticsearch'|'c4.large.elasticsearch'|'c4.xlarge.elasticsearch'|'c4.2xlarge.elasticsearch'|'c4.4xlarge.elasticsearch'|'c4.8xlarge.elasticsearch'|'r4.large.elasticsearch'|'r4.xlarge.elasticsearch'|'r4.2xlarge.elasticsearch'|'r4.4xlarge.elasticsearch'|'r4.8xlarge.elasticsearch'|'r4.16xlarge.elasticsearch',
                    'DedicatedMasterCount': 123
                },
                'EBSOptions': {
                    'EBSEnabled': True|False,
                    'VolumeType': 'standard'|'gp2'|'io1',
                    'VolumeSize': 123,
                    'Iops': 123
                },
                'AccessPolicies': 'string',
                'SnapshotOptions': {
                    'AutomatedSnapshotStartHour': 123
                },
                'AdvancedOptions': {
                    'string': 'string'
                }
            },
        ]
    }
    
    
    """
    pass

def describe_elasticsearch_instance_type_limits(DomainName=None, InstanceType=None, ElasticsearchVersion=None):
    """
    Describe Elasticsearch Limits for a given InstanceType and ElasticsearchVersion. When modifying existing Domain, specify the ``  DomainName `` to know what Limits are supported for modifying.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_elasticsearch_instance_type_limits(
        DomainName='string',
        InstanceType='m3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch'|'d2.xlarge.elasticsearch'|'d2.2xlarge.elasticsearch'|'d2.4xlarge.elasticsearch'|'d2.8xlarge.elasticsearch'|'c4.large.elasticsearch'|'c4.xlarge.elasticsearch'|'c4.2xlarge.elasticsearch'|'c4.4xlarge.elasticsearch'|'c4.8xlarge.elasticsearch'|'r4.large.elasticsearch'|'r4.xlarge.elasticsearch'|'r4.2xlarge.elasticsearch'|'r4.4xlarge.elasticsearch'|'r4.8xlarge.elasticsearch'|'r4.16xlarge.elasticsearch',
        ElasticsearchVersion='string'
    )
    
    
    :type DomainName: string
    :param DomainName: DomainName represents the name of the Domain that we are trying to modify. This should be present only if we are querying for Elasticsearch `` Limits `` for existing domain.

    :type InstanceType: string
    :param InstanceType: [REQUIRED]
            The instance type for an Elasticsearch cluster for which Elasticsearch `` Limits `` are needed.
            

    :type ElasticsearchVersion: string
    :param ElasticsearchVersion: [REQUIRED]
            Version of Elasticsearch for which `` Limits `` are needed.
            

    :rtype: dict
    :return: {
        'LimitsByRole': {
            'string': {
                'StorageTypes': [
                    {
                        'StorageTypeName': 'string',
                        'StorageSubTypeName': 'string',
                        'StorageTypeLimits': [
                            {
                                'LimitName': 'string',
                                'LimitValues': [
                                    'string',
                                ]
                            },
                        ]
                    },
                ],
                'InstanceLimits': {
                    'InstanceCountLimits': {
                        'MinimumInstanceCount': 123,
                        'MaximumInstanceCount': 123
                    }
                },
                'AdditionalLimits': [
                    {
                        'LimitName': 'string',
                        'LimitValues': [
                            'string',
                        ]
                    },
                ]
            }
        }
    }
    
    
    :returns: 
    Data: If the given InstanceType is used as Data node
    Master: If the given InstanceType is used as Master node
    
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

def list_domain_names():
    """
    Returns the name of all Elasticsearch domains owned by the current user's account.
    See also: AWS API Documentation
    
    
    :example: response = client.list_domain_names()
    
    
    :rtype: dict
    :return: {
        'DomainNames': [
            {
                'DomainName': 'string'
            },
        ]
    }
    
    
    """
    pass

def list_elasticsearch_instance_types(ElasticsearchVersion=None, DomainName=None, MaxResults=None, NextToken=None):
    """
    List all Elasticsearch instance types that are supported for given ElasticsearchVersion
    See also: AWS API Documentation
    
    
    :example: response = client.list_elasticsearch_instance_types(
        ElasticsearchVersion='string',
        DomainName='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type ElasticsearchVersion: string
    :param ElasticsearchVersion: [REQUIRED]
            Version of Elasticsearch for which list of supported elasticsearch instance types are needed.
            

    :type DomainName: string
    :param DomainName: DomainName represents the name of the Domain that we are trying to modify. This should be present only if we are querying for list of available Elasticsearch instance types when modifying existing domain.

    :type MaxResults: integer
    :param MaxResults: Set this value to limit the number of results returned. Value provided must be greater than 30 else it wont be honored.

    :type NextToken: string
    :param NextToken: NextToken should be sent in case if earlier API call produced result containing NextToken. It is used for pagination.

    :rtype: dict
    :return: {
        'ElasticsearchInstanceTypes': [
            'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch'|'d2.xlarge.elasticsearch'|'d2.2xlarge.elasticsearch'|'d2.4xlarge.elasticsearch'|'d2.8xlarge.elasticsearch'|'c4.large.elasticsearch'|'c4.xlarge.elasticsearch'|'c4.2xlarge.elasticsearch'|'c4.4xlarge.elasticsearch'|'c4.8xlarge.elasticsearch'|'r4.large.elasticsearch'|'r4.xlarge.elasticsearch'|'r4.2xlarge.elasticsearch'|'r4.4xlarge.elasticsearch'|'r4.8xlarge.elasticsearch'|'r4.16xlarge.elasticsearch',
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_elasticsearch_versions(MaxResults=None, NextToken=None):
    """
    List all supported Elasticsearch versions
    See also: AWS API Documentation
    
    
    :example: response = client.list_elasticsearch_versions(
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: Set this value to limit the number of results returned. Value provided must be greater than 10 else it wont be honored.

    :type NextToken: string
    :param NextToken: Paginated APIs accepts NextToken input to returns next page results and provides a NextToken output in the response which can be used by the client to retrieve more results.

    :rtype: dict
    :return: {
        'ElasticsearchVersions': [
            'string',
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_tags(ARN=None):
    """
    Returns all tags for the given Elasticsearch domain.
    See also: AWS API Documentation
    
    
    :example: response = client.list_tags(
        ARN='string'
    )
    
    
    :type ARN: string
    :param ARN: [REQUIRED]
            Specify the ARN for the Elasticsearch domain to which the tags are attached that you want to view.
            

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

def remove_tags(ARN=None, TagKeys=None):
    """
    Removes the specified set of tags from the specified Elasticsearch domain.
    See also: AWS API Documentation
    
    
    :example: response = client.remove_tags(
        ARN='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ARN: string
    :param ARN: [REQUIRED]
            Specifies the ARN for the Elasticsearch domain from which you want to delete the specified tags.
            

    :type TagKeys: list
    :param TagKeys: [REQUIRED]
            Specifies the TagKey list which you want to remove from the Elasticsearch domain.
            (string) --
            

    """
    pass

def update_elasticsearch_domain_config(DomainName=None, ElasticsearchClusterConfig=None, EBSOptions=None, SnapshotOptions=None, AdvancedOptions=None, AccessPolicies=None):
    """
    Modifies the cluster configuration of the specified Elasticsearch domain, setting as setting the instance type and the number of instances.
    See also: AWS API Documentation
    
    
    :example: response = client.update_elasticsearch_domain_config(
        DomainName='string',
        ElasticsearchClusterConfig={
            'InstanceType': 'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch'|'d2.xlarge.elasticsearch'|'d2.2xlarge.elasticsearch'|'d2.4xlarge.elasticsearch'|'d2.8xlarge.elasticsearch'|'c4.large.elasticsearch'|'c4.xlarge.elasticsearch'|'c4.2xlarge.elasticsearch'|'c4.4xlarge.elasticsearch'|'c4.8xlarge.elasticsearch'|'r4.large.elasticsearch'|'r4.xlarge.elasticsearch'|'r4.2xlarge.elasticsearch'|'r4.4xlarge.elasticsearch'|'r4.8xlarge.elasticsearch'|'r4.16xlarge.elasticsearch',
            'InstanceCount': 123,
            'DedicatedMasterEnabled': True|False,
            'ZoneAwarenessEnabled': True|False,
            'DedicatedMasterType': 'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch'|'d2.xlarge.elasticsearch'|'d2.2xlarge.elasticsearch'|'d2.4xlarge.elasticsearch'|'d2.8xlarge.elasticsearch'|'c4.large.elasticsearch'|'c4.xlarge.elasticsearch'|'c4.2xlarge.elasticsearch'|'c4.4xlarge.elasticsearch'|'c4.8xlarge.elasticsearch'|'r4.large.elasticsearch'|'r4.xlarge.elasticsearch'|'r4.2xlarge.elasticsearch'|'r4.4xlarge.elasticsearch'|'r4.8xlarge.elasticsearch'|'r4.16xlarge.elasticsearch',
            'DedicatedMasterCount': 123
        },
        EBSOptions={
            'EBSEnabled': True|False,
            'VolumeType': 'standard'|'gp2'|'io1',
            'VolumeSize': 123,
            'Iops': 123
        },
        SnapshotOptions={
            'AutomatedSnapshotStartHour': 123
        },
        AdvancedOptions={
            'string': 'string'
        },
        AccessPolicies='string'
    )
    
    
    :type DomainName: string
    :param DomainName: [REQUIRED]
            The name of the Elasticsearch domain that you are updating.
            

    :type ElasticsearchClusterConfig: dict
    :param ElasticsearchClusterConfig: The type and number of instances to instantiate for the domain cluster.
            InstanceType (string) --The instance type for an Elasticsearch cluster.
            InstanceCount (integer) --The number of instances in the specified domain cluster.
            DedicatedMasterEnabled (boolean) --A boolean value to indicate whether a dedicated master node is enabled. See About Dedicated Master Nodes for more information.
            ZoneAwarenessEnabled (boolean) --A boolean value to indicate whether zone awareness is enabled. See About Zone Awareness for more information.
            DedicatedMasterType (string) --The instance type for a dedicated master node.
            DedicatedMasterCount (integer) --Total number of dedicated master nodes, active and on standby, for the cluster.
            

    :type EBSOptions: dict
    :param EBSOptions: Specify the type and size of the EBS volume that you want to use.
            EBSEnabled (boolean) --Specifies whether EBS-based storage is enabled.
            VolumeType (string) --Specifies the volume type for EBS-based storage.
            VolumeSize (integer) --Integer to specify the size of an EBS volume.
            Iops (integer) --Specifies the IOPD for a Provisioned IOPS EBS volume (SSD).
            

    :type SnapshotOptions: dict
    :param SnapshotOptions: Option to set the time, in UTC format, for the daily automated snapshot. Default value is 0 hours.
            AutomatedSnapshotStartHour (integer) --Specifies the time, in UTC format, when the service takes a daily automated snapshot of the specified Elasticsearch domain. Default value is 0 hours.
            

    :type AdvancedOptions: dict
    :param AdvancedOptions: Modifies the advanced option to allow references to indices in an HTTP request body. Must be false when configuring access to individual sub-resources. By default, the value is true . See Configuration Advanced Options for more information.
            (string) --
            (string) --
            

    :type AccessPolicies: string
    :param AccessPolicies: IAM access policy as a JSON-formatted string.

    :rtype: dict
    :return: {
        'DomainConfig': {
            'ElasticsearchVersion': {
                'Options': 'string',
                'Status': {
                    'CreationDate': datetime(2015, 1, 1),
                    'UpdateDate': datetime(2015, 1, 1),
                    'UpdateVersion': 123,
                    'State': 'RequiresIndexDocuments'|'Processing'|'Active',
                    'PendingDeletion': True|False
                }
            },
            'ElasticsearchClusterConfig': {
                'Options': {
                    'InstanceType': 'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch'|'d2.xlarge.elasticsearch'|'d2.2xlarge.elasticsearch'|'d2.4xlarge.elasticsearch'|'d2.8xlarge.elasticsearch'|'c4.large.elasticsearch'|'c4.xlarge.elasticsearch'|'c4.2xlarge.elasticsearch'|'c4.4xlarge.elasticsearch'|'c4.8xlarge.elasticsearch'|'r4.large.elasticsearch'|'r4.xlarge.elasticsearch'|'r4.2xlarge.elasticsearch'|'r4.4xlarge.elasticsearch'|'r4.8xlarge.elasticsearch'|'r4.16xlarge.elasticsearch',
                    'InstanceCount': 123,
                    'DedicatedMasterEnabled': True|False,
                    'ZoneAwarenessEnabled': True|False,
                    'DedicatedMasterType': 'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch'|'d2.xlarge.elasticsearch'|'d2.2xlarge.elasticsearch'|'d2.4xlarge.elasticsearch'|'d2.8xlarge.elasticsearch'|'c4.large.elasticsearch'|'c4.xlarge.elasticsearch'|'c4.2xlarge.elasticsearch'|'c4.4xlarge.elasticsearch'|'c4.8xlarge.elasticsearch'|'r4.large.elasticsearch'|'r4.xlarge.elasticsearch'|'r4.2xlarge.elasticsearch'|'r4.4xlarge.elasticsearch'|'r4.8xlarge.elasticsearch'|'r4.16xlarge.elasticsearch',
                    'DedicatedMasterCount': 123
                },
                'Status': {
                    'CreationDate': datetime(2015, 1, 1),
                    'UpdateDate': datetime(2015, 1, 1),
                    'UpdateVersion': 123,
                    'State': 'RequiresIndexDocuments'|'Processing'|'Active',
                    'PendingDeletion': True|False
                }
            },
            'EBSOptions': {
                'Options': {
                    'EBSEnabled': True|False,
                    'VolumeType': 'standard'|'gp2'|'io1',
                    'VolumeSize': 123,
                    'Iops': 123
                },
                'Status': {
                    'CreationDate': datetime(2015, 1, 1),
                    'UpdateDate': datetime(2015, 1, 1),
                    'UpdateVersion': 123,
                    'State': 'RequiresIndexDocuments'|'Processing'|'Active',
                    'PendingDeletion': True|False
                }
            },
            'AccessPolicies': {
                'Options': 'string',
                'Status': {
                    'CreationDate': datetime(2015, 1, 1),
                    'UpdateDate': datetime(2015, 1, 1),
                    'UpdateVersion': 123,
                    'State': 'RequiresIndexDocuments'|'Processing'|'Active',
                    'PendingDeletion': True|False
                }
            },
            'SnapshotOptions': {
                'Options': {
                    'AutomatedSnapshotStartHour': 123
                },
                'Status': {
                    'CreationDate': datetime(2015, 1, 1),
                    'UpdateDate': datetime(2015, 1, 1),
                    'UpdateVersion': 123,
                    'State': 'RequiresIndexDocuments'|'Processing'|'Active',
                    'PendingDeletion': True|False
                }
            },
            'AdvancedOptions': {
                'Options': {
                    'string': 'string'
                },
                'Status': {
                    'CreationDate': datetime(2015, 1, 1),
                    'UpdateDate': datetime(2015, 1, 1),
                    'UpdateVersion': 123,
                    'State': 'RequiresIndexDocuments'|'Processing'|'Active',
                    'PendingDeletion': True|False
                }
            }
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

