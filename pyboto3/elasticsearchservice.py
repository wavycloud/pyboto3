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


def add_tags(ARN=None, TagList=None):
    """
    :param ARN: [REQUIRED]
            Specify the ARN for which you want to add the tags.
            
    :type ARN: string
    :param TagList: [REQUIRED]
            List of Tag that need to be added for the Elasticsearch domain.
            (dict) --Specifies a key value pair for a resource tag.
            Key (string) -- [REQUIRED]Specifies the TagKey , the name of the tag. Tag keys must be unique for the Elasticsearch domain to which they are attached.
            Value (string) -- [REQUIRED]Specifies the TagValue , the value assigned to the corresponding tag key. Tag values can be null and do not have to be unique in a tag set. For example, you can have a key value pair in a tag set of project : Trinity and cost-center : Trinity
            
            
    :type TagList: list
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


def create_elasticsearch_domain(DomainName=None, ElasticsearchVersion=None, ElasticsearchClusterConfig=None,
                                EBSOptions=None, AccessPolicies=None, SnapshotOptions=None, AdvancedOptions=None):
    """
    :param DomainName: [REQUIRED]
            The name of the Elasticsearch domain that you are creating. Domain names are unique across the domains owned by an account within an AWS region. Domain names must start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).
            
    :type DomainName: string
    :param ElasticsearchVersion: String of format X.Y to specify version for the Elasticsearch domain eg. '1.5' or '2.3'. For more information, see Creating Elasticsearch Domains in the Amazon Elasticsearch Service Developer Guide .
    :type ElasticsearchVersion: string
    :param ElasticsearchClusterConfig: Configuration options for an Elasticsearch domain. Specifies the instance type and number of instances in the domain cluster.
            InstanceType (string) --The instance type for an Elasticsearch cluster.
            InstanceCount (integer) --The number of instances in the specified domain cluster.
            DedicatedMasterEnabled (boolean) --A boolean value to indicate whether a dedicated master node is enabled. See About Dedicated Master Nodes for more information.
            ZoneAwarenessEnabled (boolean) --A boolean value to indicate whether zone awareness is enabled. See About Zone Awareness for more information.
            DedicatedMasterType (string) --The instance type for a dedicated master node.
            DedicatedMasterCount (integer) --Total number of dedicated master nodes, active and on standby, for the cluster.
            
    :type ElasticsearchClusterConfig: dict
    :param EBSOptions: Options to enable, disable and specify the type and size of EBS storage volumes.
            EBSEnabled (boolean) --Specifies whether EBS-based storage is enabled.
            VolumeType (string) --Specifies the volume type for EBS-based storage.
            VolumeSize (integer) --Integer to specify the size of an EBS volume.
            Iops (integer) --Specifies the IOPD for a Provisioned IOPS EBS volume (SSD).
            
    :type EBSOptions: dict
    :param AccessPolicies: IAM access policy as a JSON-formatted string.
    :type AccessPolicies: string
    :param SnapshotOptions: Option to set time, in UTC format, of the daily automated snapshot. Default value is 0 hours.
            AutomatedSnapshotStartHour (integer) --Specifies the time, in UTC format, when the service takes a daily automated snapshot of the specified Elasticsearch domain. Default value is 0 hours.
            
    :type SnapshotOptions: dict
    :param AdvancedOptions: Option to allow references to indices in an HTTP request body. Must be false when configuring access to individual sub-resources. By default, the value is true . See Configuration Advanced Options for more information.
            (string) --
            (string) --
            
    :type AdvancedOptions: dict
    """
    pass


def delete_elasticsearch_domain(DomainName=None):
    """
    :param DomainName: [REQUIRED]
            The name of the Elasticsearch domain that you want to permanently delete.
            Return typedict
            ReturnsResponse Syntax{
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
                  'InstanceType': 'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch',
                  'InstanceCount': 123,
                  'DedicatedMasterEnabled': True|False,
                  'ZoneAwarenessEnabled': True|False,
                  'DedicatedMasterType': 'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch',
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
            Response Structure
            (dict) --The result of a DeleteElasticsearchDomain request. Contains the status of the pending deletion, or no status if the domain and all of its resources have been deleted.
            DomainStatus (dict) --The status of the Elasticsearch domain being deleted.
            DomainId (string) --The unique identifier for the specified Elasticsearch domain.
            DomainName (string) --The name of an Elasticsearch domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).
            ARN (string) --The Amazon resource name (ARN) of an Elasticsearch domain. See Identifiers for IAM Entities in Using AWS Identity and Access Management for more information.
            Created (boolean) --The domain creation status. True if the creation of an Elasticsearch domain is complete. False if domain creation is still in progress.
            Deleted (boolean) --The domain deletion status. True if a delete request has been received for the domain but resource cleanup is still in progress. False if the domain has not been deleted. Once domain deletion is complete, the status of the domain is no longer returned.
            Endpoint (string) --The Elasticsearch domain endpoint that you use to submit index and search requests.
            Processing (boolean) --The status of the Elasticsearch domain configuration. True if Amazon Elasticsearch Service is processing configuration changes. False if the configuration is active.
            ElasticsearchVersion (string) --
            ElasticsearchClusterConfig (dict) --The type and number of instances in the domain cluster.
            InstanceType (string) --The instance type for an Elasticsearch cluster.
            InstanceCount (integer) --The number of instances in the specified domain cluster.
            DedicatedMasterEnabled (boolean) --A boolean value to indicate whether a dedicated master node is enabled. See About Dedicated Master Nodes for more information.
            ZoneAwarenessEnabled (boolean) --A boolean value to indicate whether zone awareness is enabled. See About Zone Awareness for more information.
            DedicatedMasterType (string) --The instance type for a dedicated master node.
            DedicatedMasterCount (integer) --Total number of dedicated master nodes, active and on standby, for the cluster.
            EBSOptions (dict) --The EBSOptions for the specified domain. See Configuring EBS-based Storage for more information.
            EBSEnabled (boolean) --Specifies whether EBS-based storage is enabled.
            VolumeType (string) --Specifies the volume type for EBS-based storage.
            VolumeSize (integer) --Integer to specify the size of an EBS volume.
            Iops (integer) --Specifies the IOPD for a Provisioned IOPS EBS volume (SSD).
            AccessPolicies (string) --IAM access policy as a JSON-formatted string.
            SnapshotOptions (dict) --Specifies the status of the SnapshotOptions
            AutomatedSnapshotStartHour (integer) --Specifies the time, in UTC format, when the service takes a daily automated snapshot of the specified Elasticsearch domain. Default value is 0 hours.
            AdvancedOptions (dict) --Specifies the status of the AdvancedOptions
            (string) --
            (string) --
            
            
            
    :type DomainName: string
    """
    pass


def describe_elasticsearch_domain(DomainName=None):
    """
    :param DomainName: [REQUIRED]
            The name of the Elasticsearch domain for which you want information.
            Return typedict
            ReturnsResponse Syntax{
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
                  'InstanceType': 'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch',
                  'InstanceCount': 123,
                  'DedicatedMasterEnabled': True|False,
                  'ZoneAwarenessEnabled': True|False,
                  'DedicatedMasterType': 'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch',
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
            Response Structure
            (dict) --The result of a DescribeElasticsearchDomain request. Contains the status of the domain specified in the request.
            DomainStatus (dict) --The current status of the Elasticsearch domain.
            DomainId (string) --The unique identifier for the specified Elasticsearch domain.
            DomainName (string) --The name of an Elasticsearch domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).
            ARN (string) --The Amazon resource name (ARN) of an Elasticsearch domain. See Identifiers for IAM Entities in Using AWS Identity and Access Management for more information.
            Created (boolean) --The domain creation status. True if the creation of an Elasticsearch domain is complete. False if domain creation is still in progress.
            Deleted (boolean) --The domain deletion status. True if a delete request has been received for the domain but resource cleanup is still in progress. False if the domain has not been deleted. Once domain deletion is complete, the status of the domain is no longer returned.
            Endpoint (string) --The Elasticsearch domain endpoint that you use to submit index and search requests.
            Processing (boolean) --The status of the Elasticsearch domain configuration. True if Amazon Elasticsearch Service is processing configuration changes. False if the configuration is active.
            ElasticsearchVersion (string) --
            ElasticsearchClusterConfig (dict) --The type and number of instances in the domain cluster.
            InstanceType (string) --The instance type for an Elasticsearch cluster.
            InstanceCount (integer) --The number of instances in the specified domain cluster.
            DedicatedMasterEnabled (boolean) --A boolean value to indicate whether a dedicated master node is enabled. See About Dedicated Master Nodes for more information.
            ZoneAwarenessEnabled (boolean) --A boolean value to indicate whether zone awareness is enabled. See About Zone Awareness for more information.
            DedicatedMasterType (string) --The instance type for a dedicated master node.
            DedicatedMasterCount (integer) --Total number of dedicated master nodes, active and on standby, for the cluster.
            EBSOptions (dict) --The EBSOptions for the specified domain. See Configuring EBS-based Storage for more information.
            EBSEnabled (boolean) --Specifies whether EBS-based storage is enabled.
            VolumeType (string) --Specifies the volume type for EBS-based storage.
            VolumeSize (integer) --Integer to specify the size of an EBS volume.
            Iops (integer) --Specifies the IOPD for a Provisioned IOPS EBS volume (SSD).
            AccessPolicies (string) --IAM access policy as a JSON-formatted string.
            SnapshotOptions (dict) --Specifies the status of the SnapshotOptions
            AutomatedSnapshotStartHour (integer) --Specifies the time, in UTC format, when the service takes a daily automated snapshot of the specified Elasticsearch domain. Default value is 0 hours.
            AdvancedOptions (dict) --Specifies the status of the AdvancedOptions
            (string) --
            (string) --
            
            
            
    :type DomainName: string
    """
    pass


def describe_elasticsearch_domain_config(DomainName=None):
    """
    :param DomainName: [REQUIRED]
            The Elasticsearch domain that you want to get information about.
            Return typedict
            ReturnsResponse Syntax{
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
                    'InstanceType': 'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch',
                    'InstanceCount': 123,
                    'DedicatedMasterEnabled': True|False,
                    'ZoneAwarenessEnabled': True|False,
                    'DedicatedMasterType': 'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch',
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
            Response Structure
            (dict) --The result of a DescribeElasticsearchDomainConfig request. Contains the configuration information of the requested domain.
            DomainConfig (dict) --The configuration information of the domain requested in the DescribeElasticsearchDomainConfig request.
            ElasticsearchVersion (dict) --String of format X.Y to specify version for the Elasticsearch domain.
            Options (string) --Specifies the Elasticsearch version for the specified Elasticsearch domain.
            Status (dict) --Specifies the status of the Elasticsearch version options for the specified Elasticsearch domain.
            CreationDate (datetime) --Timestamp which tells the creation date for the entity.
            UpdateDate (datetime) --Timestamp which tells the last updated time for the entity.
            UpdateVersion (integer) --Specifies the latest version for the entity.
            State (string) --Provides the OptionState for the Elasticsearch domain.
            PendingDeletion (boolean) --Indicates whether the Elasticsearch domain is being deleted.
            
            ElasticsearchClusterConfig (dict) --Specifies the ElasticsearchClusterConfig for the Elasticsearch domain.
            Options (dict) --Specifies the cluster configuration for the specified Elasticsearch domain.
            InstanceType (string) --The instance type for an Elasticsearch cluster.
            InstanceCount (integer) --The number of instances in the specified domain cluster.
            DedicatedMasterEnabled (boolean) --A boolean value to indicate whether a dedicated master node is enabled. See About Dedicated Master Nodes for more information.
            ZoneAwarenessEnabled (boolean) --A boolean value to indicate whether zone awareness is enabled. See About Zone Awareness for more information.
            DedicatedMasterType (string) --The instance type for a dedicated master node.
            DedicatedMasterCount (integer) --Total number of dedicated master nodes, active and on standby, for the cluster.
            Status (dict) --Specifies the status of the configuration for the specified Elasticsearch domain.
            CreationDate (datetime) --Timestamp which tells the creation date for the entity.
            UpdateDate (datetime) --Timestamp which tells the last updated time for the entity.
            UpdateVersion (integer) --Specifies the latest version for the entity.
            State (string) --Provides the OptionState for the Elasticsearch domain.
            PendingDeletion (boolean) --Indicates whether the Elasticsearch domain is being deleted.
            
            EBSOptions (dict) --Specifies the EBSOptions for the Elasticsearch domain.
            Options (dict) --Specifies the EBS options for the specified Elasticsearch domain.
            EBSEnabled (boolean) --Specifies whether EBS-based storage is enabled.
            VolumeType (string) --Specifies the volume type for EBS-based storage.
            VolumeSize (integer) --Integer to specify the size of an EBS volume.
            Iops (integer) --Specifies the IOPD for a Provisioned IOPS EBS volume (SSD).
            Status (dict) --Specifies the status of the EBS options for the specified Elasticsearch domain.
            CreationDate (datetime) --Timestamp which tells the creation date for the entity.
            UpdateDate (datetime) --Timestamp which tells the last updated time for the entity.
            UpdateVersion (integer) --Specifies the latest version for the entity.
            State (string) --Provides the OptionState for the Elasticsearch domain.
            PendingDeletion (boolean) --Indicates whether the Elasticsearch domain is being deleted.
            
            AccessPolicies (dict) --IAM access policy as a JSON-formatted string.
            Options (string) --The access policy configured for the Elasticsearch domain. Access policies may be resource-based, IP-based, or IAM-based. See Configuring Access Policies for more information.
            Status (dict) --The status of the access policy for the Elasticsearch domain. See OptionStatus for the status information that's included.
            CreationDate (datetime) --Timestamp which tells the creation date for the entity.
            UpdateDate (datetime) --Timestamp which tells the last updated time for the entity.
            UpdateVersion (integer) --Specifies the latest version for the entity.
            State (string) --Provides the OptionState for the Elasticsearch domain.
            PendingDeletion (boolean) --Indicates whether the Elasticsearch domain is being deleted.
            
            SnapshotOptions (dict) --Specifies the SnapshotOptions for the Elasticsearch domain.
            Options (dict) --Specifies the daily snapshot options specified for the Elasticsearch domain.
            AutomatedSnapshotStartHour (integer) --Specifies the time, in UTC format, when the service takes a daily automated snapshot of the specified Elasticsearch domain. Default value is 0 hours.
            Status (dict) --Specifies the status of a daily automated snapshot.
            CreationDate (datetime) --Timestamp which tells the creation date for the entity.
            UpdateDate (datetime) --Timestamp which tells the last updated time for the entity.
            UpdateVersion (integer) --Specifies the latest version for the entity.
            State (string) --Provides the OptionState for the Elasticsearch domain.
            PendingDeletion (boolean) --Indicates whether the Elasticsearch domain is being deleted.
            
            AdvancedOptions (dict) --Specifies the AdvancedOptions for the domain. See Configuring Advanced Options for more information.
            Options (dict) --Specifies the status of advanced options for the specified Elasticsearch domain.
            (string) --
            (string) --
            
            Status (dict) --Specifies the status of OptionStatus for advanced options for the specified Elasticsearch domain.
            CreationDate (datetime) --Timestamp which tells the creation date for the entity.
            UpdateDate (datetime) --Timestamp which tells the last updated time for the entity.
            UpdateVersion (integer) --Specifies the latest version for the entity.
            State (string) --Provides the OptionState for the Elasticsearch domain.
            PendingDeletion (boolean) --Indicates whether the Elasticsearch domain is being deleted.
            
            
            
            
    :type DomainName: string
    """
    pass


def describe_elasticsearch_domains(DomainNames=None):
    """
    :param DomainNames: [REQUIRED]
            The Elasticsearch domains for which you want information.
            (string) --The name of an Elasticsearch domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).
            Return typedict
            ReturnsResponse Syntax{
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
                    'InstanceType': 'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch',
                    'InstanceCount': 123,
                    'DedicatedMasterEnabled': True|False,
                    'ZoneAwarenessEnabled': True|False,
                    'DedicatedMasterType': 'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch',
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
            Response Structure
            (dict) --The result of a DescribeElasticsearchDomains request. Contains the status of the specified domains or all domains owned by the account.
            DomainStatusList (list) --The status of the domains requested in the DescribeElasticsearchDomains request.
            (dict) --The current status of an Elasticsearch domain.
            DomainId (string) --The unique identifier for the specified Elasticsearch domain.
            DomainName (string) --The name of an Elasticsearch domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).
            ARN (string) --The Amazon resource name (ARN) of an Elasticsearch domain. See Identifiers for IAM Entities in Using AWS Identity and Access Management for more information.
            Created (boolean) --The domain creation status. True if the creation of an Elasticsearch domain is complete. False if domain creation is still in progress.
            Deleted (boolean) --The domain deletion status. True if a delete request has been received for the domain but resource cleanup is still in progress. False if the domain has not been deleted. Once domain deletion is complete, the status of the domain is no longer returned.
            Endpoint (string) --The Elasticsearch domain endpoint that you use to submit index and search requests.
            Processing (boolean) --The status of the Elasticsearch domain configuration. True if Amazon Elasticsearch Service is processing configuration changes. False if the configuration is active.
            ElasticsearchVersion (string) --
            ElasticsearchClusterConfig (dict) --The type and number of instances in the domain cluster.
            InstanceType (string) --The instance type for an Elasticsearch cluster.
            InstanceCount (integer) --The number of instances in the specified domain cluster.
            DedicatedMasterEnabled (boolean) --A boolean value to indicate whether a dedicated master node is enabled. See About Dedicated Master Nodes for more information.
            ZoneAwarenessEnabled (boolean) --A boolean value to indicate whether zone awareness is enabled. See About Zone Awareness for more information.
            DedicatedMasterType (string) --The instance type for a dedicated master node.
            DedicatedMasterCount (integer) --Total number of dedicated master nodes, active and on standby, for the cluster.
            EBSOptions (dict) --The EBSOptions for the specified domain. See Configuring EBS-based Storage for more information.
            EBSEnabled (boolean) --Specifies whether EBS-based storage is enabled.
            VolumeType (string) --Specifies the volume type for EBS-based storage.
            VolumeSize (integer) --Integer to specify the size of an EBS volume.
            Iops (integer) --Specifies the IOPD for a Provisioned IOPS EBS volume (SSD).
            AccessPolicies (string) --IAM access policy as a JSON-formatted string.
            SnapshotOptions (dict) --Specifies the status of the SnapshotOptions
            AutomatedSnapshotStartHour (integer) --Specifies the time, in UTC format, when the service takes a daily automated snapshot of the specified Elasticsearch domain. Default value is 0 hours.
            AdvancedOptions (dict) --Specifies the status of the AdvancedOptions
            (string) --
            (string) --
            
            
            
            
    :type DomainNames: list
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


def list_domain_names():
    """
    """
    pass


def list_tags(ARN=None):
    """
    :param ARN: [REQUIRED]
            Specify the ARN for the Elasticsearch domain to which the tags are attached that you want to view.
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
            (dict) --The result of a ListTags operation. Contains tags for all requested Elasticsearch domains.
            TagList (list) --List of Tag for the requested Elasticsearch domain.
            (dict) --Specifies a key value pair for a resource tag.
            Key (string) --Specifies the TagKey , the name of the tag. Tag keys must be unique for the Elasticsearch domain to which they are attached.
            Value (string) --Specifies the TagValue , the value assigned to the corresponding tag key. Tag values can be null and do not have to be unique in a tag set. For example, you can have a key value pair in a tag set of project : Trinity and cost-center : Trinity
            
            
            
    :type ARN: string
    """
    pass


def remove_tags(ARN=None, TagKeys=None):
    """
    :param ARN: [REQUIRED]
            Specifies the ARN for the Elasticsearch domain from which you want to delete the specified tags.
            
    :type ARN: string
    :param TagKeys: [REQUIRED]
            Specifies the TagKey list which you want to remove from the Elasticsearch domain.
            (string) --
            
    :type TagKeys: list
    """
    pass


def update_elasticsearch_domain_config(DomainName=None, ElasticsearchClusterConfig=None, EBSOptions=None,
                                       SnapshotOptions=None, AdvancedOptions=None, AccessPolicies=None):
    """
    :param DomainName: [REQUIRED]
            The name of the Elasticsearch domain that you are updating.
            
    :type DomainName: string
    :param ElasticsearchClusterConfig: The type and number of instances to instantiate for the domain cluster.
            InstanceType (string) --The instance type for an Elasticsearch cluster.
            InstanceCount (integer) --The number of instances in the specified domain cluster.
            DedicatedMasterEnabled (boolean) --A boolean value to indicate whether a dedicated master node is enabled. See About Dedicated Master Nodes for more information.
            ZoneAwarenessEnabled (boolean) --A boolean value to indicate whether zone awareness is enabled. See About Zone Awareness for more information.
            DedicatedMasterType (string) --The instance type for a dedicated master node.
            DedicatedMasterCount (integer) --Total number of dedicated master nodes, active and on standby, for the cluster.
            
    :type ElasticsearchClusterConfig: dict
    :param EBSOptions: Specify the type and size of the EBS volume that you want to use.
            EBSEnabled (boolean) --Specifies whether EBS-based storage is enabled.
            VolumeType (string) --Specifies the volume type for EBS-based storage.
            VolumeSize (integer) --Integer to specify the size of an EBS volume.
            Iops (integer) --Specifies the IOPD for a Provisioned IOPS EBS volume (SSD).
            
    :type EBSOptions: dict
    :param SnapshotOptions: Option to set the time, in UTC format, for the daily automated snapshot. Default value is 0 hours.
            AutomatedSnapshotStartHour (integer) --Specifies the time, in UTC format, when the service takes a daily automated snapshot of the specified Elasticsearch domain. Default value is 0 hours.
            
    :type SnapshotOptions: dict
    :param AdvancedOptions: Modifies the advanced option to allow references to indices in an HTTP request body. Must be false when configuring access to individual sub-resources. By default, the value is true . See Configuration Advanced Options for more information.
            (string) --
            (string) --
            
    :type AdvancedOptions: dict
    :param AccessPolicies: IAM access policy as a JSON-formatted string.
    :type AccessPolicies: string
    """
    pass
