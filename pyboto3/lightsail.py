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

def allocate_static_ip(staticIpName=None):
    """
    Allocates a static IP address.
    See also: AWS API Documentation
    
    
    :example: response = client.allocate_static_ip(
        staticIpName='string'
    )
    
    
    :type staticIpName: string
    :param staticIpName: [REQUIRED]
            The name of the static IP address.
            

    :rtype: dict
    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def attach_static_ip(staticIpName=None, instanceName=None):
    """
    Attaches a static IP address to a specific Amazon Lightsail instance.
    See also: AWS API Documentation
    
    
    :example: response = client.attach_static_ip(
        staticIpName='string',
        instanceName='string'
    )
    
    
    :type staticIpName: string
    :param staticIpName: [REQUIRED]
            The name of the static IP.
            

    :type instanceName: string
    :param instanceName: [REQUIRED]
            The instance name to which you want to attach the static IP address.
            

    :rtype: dict
    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
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

def close_instance_public_ports(portInfo=None, instanceName=None):
    """
    Closes the public ports on a specific Amazon Lightsail instance.
    See also: AWS API Documentation
    
    
    :example: response = client.close_instance_public_ports(
        portInfo={
            'fromPort': 123,
            'toPort': 123,
            'protocol': 'tcp'|'all'|'udp'
        },
        instanceName='string'
    )
    
    
    :type portInfo: dict
    :param portInfo: [REQUIRED]
            Information about the public port you are trying to close.
            fromPort (integer) --The first port in the range.
            toPort (integer) --The last port in the range.
            protocol (string) --The protocol.
            

    :type instanceName: string
    :param instanceName: [REQUIRED]
            The name of the instance on which you're attempting to close the public ports.
            

    :rtype: dict
    :return: {
        'operation': {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        }
    }
    
    
    """
    pass

def create_domain(domainName=None):
    """
    Creates a domain resource for the specified domain (e.g., example.com).
    See also: AWS API Documentation
    
    
    :example: response = client.create_domain(
        domainName='string'
    )
    
    
    :type domainName: string
    :param domainName: [REQUIRED]
            The domain name to manage (e.g., example.com ).
            Note
            You cannot register a new domain name using Lightsail. You must register a domain name using Amazon Route 53 or another domain name registrar. If you have already registered your domain, you can enter its name in this parameter to manage the DNS records for that domain.
            

    :rtype: dict
    :return: {
        'operation': {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        }
    }
    
    
    """
    pass

def create_domain_entry(domainName=None, domainEntry=None):
    """
    Creates one of the following entry records associated with the domain: A record, CNAME record, TXT record, or MX record.
    See also: AWS API Documentation
    
    
    :example: response = client.create_domain_entry(
        domainName='string',
        domainEntry={
            'id': 'string',
            'name': 'string',
            'target': 'string',
            'type': 'string',
            'options': {
                'string': 'string'
            }
        }
    )
    
    
    :type domainName: string
    :param domainName: [REQUIRED]
            The domain name (e.g., example.com ) for which you want to create the domain entry.
            

    :type domainEntry: dict
    :param domainEntry: [REQUIRED]
            An array of key-value pairs containing information about the domain entry request.
            id (string) --The ID of the domain recordset entry.
            name (string) --The name of the domain.
            target (string) --The target AWS name server (e.g., ns-111.awsdns-22.com. ).
            type (string) --The type of domain entry (e.g., SOA or NS ).
            options (dict) --The options for the domain entry.
            (string) --
            (string) --
            
            

    :rtype: dict
    :return: {
        'operation': {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        }
    }
    
    
    """
    pass

def create_instance_snapshot(instanceSnapshotName=None, instanceName=None):
    """
    Creates a snapshot of a specific virtual private server, or instance . You can use a snapshot to create a new instance that is based on that snapshot.
    See also: AWS API Documentation
    
    
    :example: response = client.create_instance_snapshot(
        instanceSnapshotName='string',
        instanceName='string'
    )
    
    
    :type instanceSnapshotName: string
    :param instanceSnapshotName: [REQUIRED]
            The name for your new snapshot.
            

    :type instanceName: string
    :param instanceName: [REQUIRED]
            The Lightsail instance on which to base your snapshot.
            

    :rtype: dict
    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def create_instances(instanceNames=None, availabilityZone=None, customImageName=None, blueprintId=None, bundleId=None, userData=None, keyPairName=None):
    """
    Creates one or more Amazon Lightsail virtual private servers, or instances .
    See also: AWS API Documentation
    
    
    :example: response = client.create_instances(
        instanceNames=[
            'string',
        ],
        availabilityZone='string',
        customImageName='string',
        blueprintId='string',
        bundleId='string',
        userData='string',
        keyPairName='string'
    )
    
    
    :type instanceNames: list
    :param instanceNames: [REQUIRED]
            The names to use for your new Lightsail instances. Separate multiple values using quotation marks and commas, for example: ['MyFirstInstance','MySecondInstance']
            (string) --
            

    :type availabilityZone: string
    :param availabilityZone: [REQUIRED]
            The Availability Zone in which to create your instance. Use the following format: us-east-1a (case sensitive). You can get a list of availability zones by using the get regions operation. Be sure to add the include availability zones parameter to your request.
            

    :type customImageName: string
    :param customImageName: The name for your custom image.

    :type blueprintId: string
    :param blueprintId: [REQUIRED]
            The ID for a virtual private server image (e.g., app_wordpress_4_4 or app_lamp_7_0 ). Use the get blueprints operation to return a list of available images (or blueprints ).
            

    :type bundleId: string
    :param bundleId: [REQUIRED]
            The bundle of specification information for your virtual private server (or instance ), including the pricing plan (e.g., micro_1_0 ).
            

    :type userData: string
    :param userData: A launch script you can create that configures a server with additional user data. For example, you might want to run apt-get  y update .
            Note
            Depending on the machine image you choose, the command to get software on your instance varies. Amazon Linux and CentOS use yum , Debian and Ubuntu use apt-get , and FreeBSD uses pkg . For a complete list, see the Dev Guide .
            

    :type keyPairName: string
    :param keyPairName: The name of your key pair.

    :rtype: dict
    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def create_instances_from_snapshot(instanceNames=None, availabilityZone=None, instanceSnapshotName=None, bundleId=None, userData=None, keyPairName=None):
    """
    Uses a specific snapshot as a blueprint for creating one or more new instances that are based on that identical configuration.
    See also: AWS API Documentation
    
    
    :example: response = client.create_instances_from_snapshot(
        instanceNames=[
            'string',
        ],
        availabilityZone='string',
        instanceSnapshotName='string',
        bundleId='string',
        userData='string',
        keyPairName='string'
    )
    
    
    :type instanceNames: list
    :param instanceNames: [REQUIRED]
            The names for your new instances.
            (string) --
            

    :type availabilityZone: string
    :param availabilityZone: [REQUIRED]
            The Availability Zone where you want to create your instances. Use the following formatting: us-east-1a (case sensitive). You can get a list of availability zones by using the get regions operation. Be sure to add the include availability zones parameter to your request.
            

    :type instanceSnapshotName: string
    :param instanceSnapshotName: [REQUIRED]
            The name of the instance snapshot on which you are basing your new instances. Use the get instance snapshots operation to return information about your existing snapshots.
            

    :type bundleId: string
    :param bundleId: [REQUIRED]
            The bundle of specification information for your virtual private server (or instance ), including the pricing plan (e.g., micro_1_0 ).
            

    :type userData: string
    :param userData: You can create a launch script that configures a server with additional user data. For example, apt-get  y update .
            Note
            Depending on the machine image you choose, the command to get software on your instance varies. Amazon Linux and CentOS use yum , Debian and Ubuntu use apt-get , and FreeBSD uses pkg . For a complete list, see the Dev Guide .
            

    :type keyPairName: string
    :param keyPairName: The name for your key pair.

    :rtype: dict
    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def create_key_pair(keyPairName=None):
    """
    Creates sn SSH key pair.
    See also: AWS API Documentation
    
    
    :example: response = client.create_key_pair(
        keyPairName='string'
    )
    
    
    :type keyPairName: string
    :param keyPairName: [REQUIRED]
            The name for your new key pair.
            

    :rtype: dict
    :return: {
        'keyPair': {
            'name': 'string',
            'arn': 'string',
            'supportCode': 'string',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc',
            'fingerprint': 'string'
        },
        'publicKeyBase64': 'string',
        'privateKeyBase64': 'string',
        'operation': {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        }
    }
    
    
    """
    pass

def delete_domain(domainName=None):
    """
    Deletes the specified domain recordset and all of its domain records.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_domain(
        domainName='string'
    )
    
    
    :type domainName: string
    :param domainName: [REQUIRED]
            The specific domain name to delete.
            

    :rtype: dict
    :return: {
        'operation': {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        }
    }
    
    
    """
    pass

def delete_domain_entry(domainName=None, domainEntry=None):
    """
    Deletes a specific domain entry.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_domain_entry(
        domainName='string',
        domainEntry={
            'id': 'string',
            'name': 'string',
            'target': 'string',
            'type': 'string',
            'options': {
                'string': 'string'
            }
        }
    )
    
    
    :type domainName: string
    :param domainName: [REQUIRED]
            The name of the domain entry to delete.
            

    :type domainEntry: dict
    :param domainEntry: [REQUIRED]
            An array of key-value pairs containing information about your domain entries.
            id (string) --The ID of the domain recordset entry.
            name (string) --The name of the domain.
            target (string) --The target AWS name server (e.g., ns-111.awsdns-22.com. ).
            type (string) --The type of domain entry (e.g., SOA or NS ).
            options (dict) --The options for the domain entry.
            (string) --
            (string) --
            
            

    :rtype: dict
    :return: {
        'operation': {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        }
    }
    
    
    """
    pass

def delete_instance(instanceName=None):
    """
    Deletes a specific Amazon Lightsail virtual private server, or instance .
    See also: AWS API Documentation
    
    
    :example: response = client.delete_instance(
        instanceName='string'
    )
    
    
    :type instanceName: string
    :param instanceName: [REQUIRED]
            The name of the instance to delete.
            

    :rtype: dict
    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def delete_instance_snapshot(instanceSnapshotName=None):
    """
    Deletes a specific snapshot of a virtual private server (or instance ).
    See also: AWS API Documentation
    
    
    :example: response = client.delete_instance_snapshot(
        instanceSnapshotName='string'
    )
    
    
    :type instanceSnapshotName: string
    :param instanceSnapshotName: [REQUIRED]
            The name of the snapshot to delete.
            

    :rtype: dict
    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def delete_key_pair(keyPairName=None):
    """
    Deletes a specific SSH key pair.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_key_pair(
        keyPairName='string'
    )
    
    
    :type keyPairName: string
    :param keyPairName: [REQUIRED]
            The name of the key pair to delete.
            

    :rtype: dict
    :return: {
        'operation': {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        }
    }
    
    
    """
    pass

def detach_static_ip(staticIpName=None):
    """
    Detaches a static IP from the Amazon Lightsail instance to which it is attached.
    See also: AWS API Documentation
    
    
    :example: response = client.detach_static_ip(
        staticIpName='string'
    )
    
    
    :type staticIpName: string
    :param staticIpName: [REQUIRED]
            The name of the static IP to detach from the instance.
            

    :rtype: dict
    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def download_default_key_pair():
    """
    Downloads the default SSH key pair from the user's account.
    See also: AWS API Documentation
    
    
    :example: response = client.download_default_key_pair()
    
    
    :rtype: dict
    :return: {
        'publicKeyBase64': 'string',
        'privateKeyBase64': 'string'
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

def get_active_names(pageToken=None):
    """
    Returns the names of all active (not deleted) resources.
    See also: AWS API Documentation
    
    
    :example: response = client.get_active_names(
        pageToken='string'
    )
    
    
    :type pageToken: string
    :param pageToken: A token used for paginating results from your get active names request.

    :rtype: dict
    :return: {
        'activeNames': [
            'string',
        ],
        'nextPageToken': 'string'
    }
    
    
    """
    pass

def get_blueprints(includeInactive=None, pageToken=None):
    """
    Returns the list of available instance images, or blueprints . You can use a blueprint to create a new virtual private server already running a specific operating system, as well as a preinstalled app or development stack. The software each instance is running depends on the blueprint image you choose.
    See also: AWS API Documentation
    
    
    :example: response = client.get_blueprints(
        includeInactive=True|False,
        pageToken='string'
    )
    
    
    :type includeInactive: boolean
    :param includeInactive: A Boolean value indicating whether to include inactive results in your request.

    :type pageToken: string
    :param pageToken: A token used for advancing to the next page of results from your get blueprints request.

    :rtype: dict
    :return: {
        'blueprints': [
            {
                'blueprintId': 'string',
                'name': 'string',
                'group': 'string',
                'type': 'os'|'app',
                'description': 'string',
                'isActive': True|False,
                'minPower': 123,
                'version': 'string',
                'versionCode': 'string',
                'productUrl': 'string',
                'licenseUrl': 'string'
            },
        ],
        'nextPageToken': 'string'
    }
    
    
    """
    pass

def get_bundles(includeInactive=None, pageToken=None):
    """
    Returns the list of bundles that are available for purchase. A bundle describes the specs for your virtual private server (or instance ).
    See also: AWS API Documentation
    
    
    :example: response = client.get_bundles(
        includeInactive=True|False,
        pageToken='string'
    )
    
    
    :type includeInactive: boolean
    :param includeInactive: A Boolean value that indicates whether to include inactive bundle results in your request.

    :type pageToken: string
    :param pageToken: A token used for advancing to the next page of results from your get bundles request.

    :rtype: dict
    :return: {
        'bundles': [
            {
                'price': ...,
                'cpuCount': 123,
                'diskSizeInGb': 123,
                'bundleId': 'string',
                'instanceType': 'string',
                'isActive': True|False,
                'name': 'string',
                'power': 123,
                'ramSizeInGb': ...,
                'transferPerMonthInGb': 123
            },
        ],
        'nextPageToken': 'string'
    }
    
    
    """
    pass

def get_domain(domainName=None):
    """
    Returns information about a specific domain recordset.
    See also: AWS API Documentation
    
    
    :example: response = client.get_domain(
        domainName='string'
    )
    
    
    :type domainName: string
    :param domainName: [REQUIRED]
            The domain name for which your want to return information about.
            

    :rtype: dict
    :return: {
        'domain': {
            'name': 'string',
            'arn': 'string',
            'supportCode': 'string',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc',
            'domainEntries': [
                {
                    'id': 'string',
                    'name': 'string',
                    'target': 'string',
                    'type': 'string',
                    'options': {
                        'string': 'string'
                    }
                },
            ]
        }
    }
    
    
    """
    pass

def get_domains(pageToken=None):
    """
    Returns a list of all domains in the user's account.
    See also: AWS API Documentation
    
    
    :example: response = client.get_domains(
        pageToken='string'
    )
    
    
    :type pageToken: string
    :param pageToken: A token used for advancing to the next page of results from your get domains request.

    :rtype: dict
    :return: {
        'domains': [
            {
                'name': 'string',
                'arn': 'string',
                'supportCode': 'string',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc',
                'domainEntries': [
                    {
                        'id': 'string',
                        'name': 'string',
                        'target': 'string',
                        'type': 'string',
                        'options': {
                            'string': 'string'
                        }
                    },
                ]
            },
        ],
        'nextPageToken': 'string'
    }
    
    
    """
    pass

def get_instance(instanceName=None):
    """
    Returns information about a specific Amazon Lightsail instance, which is a virtual private server.
    See also: AWS API Documentation
    
    
    :example: response = client.get_instance(
        instanceName='string'
    )
    
    
    :type instanceName: string
    :param instanceName: [REQUIRED]
            The name of the instance.
            

    :rtype: dict
    :return: {
        'instance': {
            'name': 'string',
            'arn': 'string',
            'supportCode': 'string',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc',
            'blueprintId': 'string',
            'blueprintName': 'string',
            'bundleId': 'string',
            'isStaticIp': True|False,
            'privateIpAddress': 'string',
            'publicIpAddress': 'string',
            'ipv6Address': 'string',
            'hardware': {
                'cpuCount': 123,
                'disks': [
                    {
                        'name': 'string',
                        'arn': 'string',
                        'supportCode': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'location': {
                            'availabilityZone': 'string',
                            'regionName': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                        },
                        'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc',
                        'sizeInGb': 123,
                        'gbInUse': 123,
                        'isSystemDisk': True|False,
                        'iops': 123,
                        'path': 'string',
                        'attachedTo': 'string',
                        'isAttached': True|False,
                        'attachmentState': 'string'
                    },
                ],
                'ramSizeInGb': ...
            },
            'networking': {
                'monthlyTransfer': {
                    'gbPerMonthAllocated': 123
                },
                'ports': [
                    {
                        'fromPort': 123,
                        'toPort': 123,
                        'protocol': 'tcp'|'all'|'udp',
                        'accessFrom': 'string',
                        'accessType': 'Public'|'Private',
                        'commonName': 'string',
                        'accessDirection': 'inbound'|'outbound'
                    },
                ]
            },
            'state': {
                'code': 123,
                'name': 'string'
            },
            'username': 'string',
            'sshKeyName': 'string'
        }
    }
    
    
    """
    pass

def get_instance_access_details(instanceName=None, protocol=None):
    """
    Returns temporary SSH keys you can use to connect to a specific virtual private server, or instance .
    See also: AWS API Documentation
    
    
    :example: response = client.get_instance_access_details(
        instanceName='string',
        protocol='ssh'|'rdp'
    )
    
    
    :type instanceName: string
    :param instanceName: [REQUIRED]
            The name of the instance to access.
            

    :type protocol: string
    :param protocol: The protocol to use to connect to your instance. Defaults to ssh .

    :rtype: dict
    :return: {
        'accessDetails': {
            'certKey': 'string',
            'expiresAt': datetime(2015, 1, 1),
            'ipAddress': 'string',
            'password': 'string',
            'privateKey': 'string',
            'protocol': 'ssh'|'rdp',
            'instanceName': 'string',
            'username': 'string'
        }
    }
    
    
    """
    pass

def get_instance_metric_data(instanceName=None, metricName=None, period=None, startTime=None, endTime=None, unit=None, statistics=None):
    """
    Returns the data points for the specified Amazon Lightsail instance metric, given an instance name.
    See also: AWS API Documentation
    
    
    :example: response = client.get_instance_metric_data(
        instanceName='string',
        metricName='CPUUtilization'|'NetworkIn'|'NetworkOut'|'StatusCheckFailed'|'StatusCheckFailed_Instance'|'StatusCheckFailed_System',
        period=123,
        startTime=datetime(2015, 1, 1),
        endTime=datetime(2015, 1, 1),
        unit='Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'|'Gigabytes'|'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Count'|'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'|'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'|'Megabits/Second'|'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None',
        statistics=[
            'Minimum'|'Maximum'|'Sum'|'Average'|'SampleCount',
        ]
    )
    
    
    :type instanceName: string
    :param instanceName: [REQUIRED]
            The name of the instance for which you want to get metrics data.
            

    :type metricName: string
    :param metricName: [REQUIRED]
            The metric name to get data about.
            

    :type period: integer
    :param period: [REQUIRED]
            The time period for which you are requesting data.
            

    :type startTime: datetime
    :param startTime: [REQUIRED]
            The start time of the time period.
            

    :type endTime: datetime
    :param endTime: [REQUIRED]
            The end time of the time period.
            

    :type unit: string
    :param unit: [REQUIRED]
            The unit. The list of valid values is below.
            

    :type statistics: list
    :param statistics: [REQUIRED]
            The instance statistics.
            (string) --
            

    :rtype: dict
    :return: {
        'metricName': 'CPUUtilization'|'NetworkIn'|'NetworkOut'|'StatusCheckFailed'|'StatusCheckFailed_Instance'|'StatusCheckFailed_System',
        'metricData': [
            {
                'average': 123.0,
                'maximum': 123.0,
                'minimum': 123.0,
                'sampleCount': 123.0,
                'sum': 123.0,
                'timestamp': datetime(2015, 1, 1),
                'unit': 'Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'|'Gigabytes'|'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Count'|'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'|'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'|'Megabits/Second'|'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None'
            },
        ]
    }
    
    
    """
    pass

def get_instance_port_states(instanceName=None):
    """
    Returns the port states for a specific virtual private server, or instance .
    See also: AWS API Documentation
    
    
    :example: response = client.get_instance_port_states(
        instanceName='string'
    )
    
    
    :type instanceName: string
    :param instanceName: [REQUIRED]
            The name of the instance.
            

    :rtype: dict
    :return: {
        'portStates': [
            {
                'fromPort': 123,
                'toPort': 123,
                'protocol': 'tcp'|'all'|'udp',
                'state': 'open'|'closed'
            },
        ]
    }
    
    
    """
    pass

def get_instance_snapshot(instanceSnapshotName=None):
    """
    Returns information about a specific instance snapshot.
    See also: AWS API Documentation
    
    
    :example: response = client.get_instance_snapshot(
        instanceSnapshotName='string'
    )
    
    
    :type instanceSnapshotName: string
    :param instanceSnapshotName: [REQUIRED]
            The name of the snapshot for which you are requesting information.
            

    :rtype: dict
    :return: {
        'instanceSnapshot': {
            'name': 'string',
            'arn': 'string',
            'supportCode': 'string',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc',
            'state': 'pending'|'error'|'available',
            'progress': 'string',
            'fromInstanceName': 'string',
            'fromInstanceArn': 'string',
            'fromBlueprintId': 'string',
            'fromBundleId': 'string',
            'sizeInGb': 123
        }
    }
    
    
    """
    pass

def get_instance_snapshots(pageToken=None):
    """
    Returns all instance snapshots for the user's account.
    See also: AWS API Documentation
    
    
    :example: response = client.get_instance_snapshots(
        pageToken='string'
    )
    
    
    :type pageToken: string
    :param pageToken: A token used for advancing to the next page of results from your get instance snapshots request.

    :rtype: dict
    :return: {
        'instanceSnapshots': [
            {
                'name': 'string',
                'arn': 'string',
                'supportCode': 'string',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc',
                'state': 'pending'|'error'|'available',
                'progress': 'string',
                'fromInstanceName': 'string',
                'fromInstanceArn': 'string',
                'fromBlueprintId': 'string',
                'fromBundleId': 'string',
                'sizeInGb': 123
            },
        ],
        'nextPageToken': 'string'
    }
    
    
    """
    pass

def get_instance_state(instanceName=None):
    """
    Returns the state of a specific instance. Works on one instance at a time.
    See also: AWS API Documentation
    
    
    :example: response = client.get_instance_state(
        instanceName='string'
    )
    
    
    :type instanceName: string
    :param instanceName: [REQUIRED]
            The name of the instance to get state information about.
            

    :rtype: dict
    :return: {
        'state': {
            'code': 123,
            'name': 'string'
        }
    }
    
    
    """
    pass

def get_instances(pageToken=None):
    """
    Returns information about all Amazon Lightsail virtual private servers, or instances .
    See also: AWS API Documentation
    
    
    :example: response = client.get_instances(
        pageToken='string'
    )
    
    
    :type pageToken: string
    :param pageToken: A token used for advancing to the next page of results from your get instances request.

    :rtype: dict
    :return: {
        'instances': [
            {
                'name': 'string',
                'arn': 'string',
                'supportCode': 'string',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc',
                'blueprintId': 'string',
                'blueprintName': 'string',
                'bundleId': 'string',
                'isStaticIp': True|False,
                'privateIpAddress': 'string',
                'publicIpAddress': 'string',
                'ipv6Address': 'string',
                'hardware': {
                    'cpuCount': 123,
                    'disks': [
                        {
                            'name': 'string',
                            'arn': 'string',
                            'supportCode': 'string',
                            'createdAt': datetime(2015, 1, 1),
                            'location': {
                                'availabilityZone': 'string',
                                'regionName': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                            },
                            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc',
                            'sizeInGb': 123,
                            'gbInUse': 123,
                            'isSystemDisk': True|False,
                            'iops': 123,
                            'path': 'string',
                            'attachedTo': 'string',
                            'isAttached': True|False,
                            'attachmentState': 'string'
                        },
                    ],
                    'ramSizeInGb': ...
                },
                'networking': {
                    'monthlyTransfer': {
                        'gbPerMonthAllocated': 123
                    },
                    'ports': [
                        {
                            'fromPort': 123,
                            'toPort': 123,
                            'protocol': 'tcp'|'all'|'udp',
                            'accessFrom': 'string',
                            'accessType': 'Public'|'Private',
                            'commonName': 'string',
                            'accessDirection': 'inbound'|'outbound'
                        },
                    ]
                },
                'state': {
                    'code': 123,
                    'name': 'string'
                },
                'username': 'string',
                'sshKeyName': 'string'
            },
        ],
        'nextPageToken': 'string'
    }
    
    
    """
    pass

def get_key_pair(keyPairName=None):
    """
    Returns information about a specific key pair.
    See also: AWS API Documentation
    
    
    :example: response = client.get_key_pair(
        keyPairName='string'
    )
    
    
    :type keyPairName: string
    :param keyPairName: [REQUIRED]
            The name of the key pair for which you are requesting information.
            

    :rtype: dict
    :return: {
        'keyPair': {
            'name': 'string',
            'arn': 'string',
            'supportCode': 'string',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc',
            'fingerprint': 'string'
        }
    }
    
    
    """
    pass

def get_key_pairs(pageToken=None):
    """
    Returns information about all key pairs in the user's account.
    See also: AWS API Documentation
    
    
    :example: response = client.get_key_pairs(
        pageToken='string'
    )
    
    
    :type pageToken: string
    :param pageToken: A token used for advancing to the next page of results from your get key pairs request.

    :rtype: dict
    :return: {
        'keyPairs': [
            {
                'name': 'string',
                'arn': 'string',
                'supportCode': 'string',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc',
                'fingerprint': 'string'
            },
        ],
        'nextPageToken': 'string'
    }
    
    
    """
    pass

def get_operation(operationId=None):
    """
    Returns information about a specific operation. Operations include events such as when you create an instance, allocate a static IP, attach a static IP, and so on.
    See also: AWS API Documentation
    
    
    :example: response = client.get_operation(
        operationId='string'
    )
    
    
    :type operationId: string
    :param operationId: [REQUIRED]
            A GUID used to identify the operation.
            

    :rtype: dict
    :return: {
        'operation': {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        }
    }
    
    
    """
    pass

def get_operations(pageToken=None):
    """
    Returns information about all operations.
    Results are returned from oldest to newest, up to a maximum of 200. Results can be paged by making each subsequent call to GetOperations use the maximum (last) statusChangedAt value from the previous request.
    See also: AWS API Documentation
    
    
    :example: response = client.get_operations(
        pageToken='string'
    )
    
    
    :type pageToken: string
    :param pageToken: A token used for advancing to the next page of results from your get operations request.

    :rtype: dict
    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ],
        'nextPageToken': 'string'
    }
    
    
    """
    pass

def get_operations_for_resource(resourceName=None, pageToken=None):
    """
    Gets operations for a specific resource (e.g., an instance or a static IP).
    See also: AWS API Documentation
    
    
    :example: response = client.get_operations_for_resource(
        resourceName='string',
        pageToken='string'
    )
    
    
    :type resourceName: string
    :param resourceName: [REQUIRED]
            The name of the resource for which you are requesting information.
            

    :type pageToken: string
    :param pageToken: A token used for advancing to the next page of results from your get operations for resource request.

    :rtype: dict
    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ],
        'nextPageCount': 'string'
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

def get_regions(includeAvailabilityZones=None):
    """
    Returns a list of all valid regions for Amazon Lightsail. Use the include availability zones parameter to also return the availability zones in a region.
    See also: AWS API Documentation
    
    
    :example: response = client.get_regions(
        includeAvailabilityZones=True|False
    )
    
    
    :type includeAvailabilityZones: boolean
    :param includeAvailabilityZones: A Boolean value indicating whether to also include Availability Zones in your get regions request. Availability Zones are indicated with a letter: e.g., us-east-1a .

    :rtype: dict
    :return: {
        'regions': [
            {
                'continentCode': 'string',
                'description': 'string',
                'displayName': 'string',
                'name': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2',
                'availabilityZones': [
                    {
                        'zoneName': 'string',
                        'state': 'string'
                    },
                ]
            },
        ]
    }
    
    
    """
    pass

def get_static_ip(staticIpName=None):
    """
    Returns information about a specific static IP.
    See also: AWS API Documentation
    
    
    :example: response = client.get_static_ip(
        staticIpName='string'
    )
    
    
    :type staticIpName: string
    :param staticIpName: [REQUIRED]
            The name of the static IP in Lightsail.
            

    :rtype: dict
    :return: {
        'staticIp': {
            'name': 'string',
            'arn': 'string',
            'supportCode': 'string',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc',
            'ipAddress': 'string',
            'attachedTo': 'string',
            'isAttached': True|False
        }
    }
    
    
    """
    pass

def get_static_ips(pageToken=None):
    """
    Returns information about all static IPs in the user's account.
    See also: AWS API Documentation
    
    
    :example: response = client.get_static_ips(
        pageToken='string'
    )
    
    
    :type pageToken: string
    :param pageToken: A token used for advancing to the next page of results from your get static IPs request.

    :rtype: dict
    :return: {
        'staticIps': [
            {
                'name': 'string',
                'arn': 'string',
                'supportCode': 'string',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc',
                'ipAddress': 'string',
                'attachedTo': 'string',
                'isAttached': True|False
            },
        ],
        'nextPageToken': 'string'
    }
    
    
    """
    pass

def get_waiter():
    """
    
    """
    pass

def import_key_pair(keyPairName=None, publicKeyBase64=None):
    """
    Imports a public SSH key from a specific key pair.
    See also: AWS API Documentation
    
    
    :example: response = client.import_key_pair(
        keyPairName='string',
        publicKeyBase64='string'
    )
    
    
    :type keyPairName: string
    :param keyPairName: [REQUIRED]
            The name of the key pair for which you want to import the public key.
            

    :type publicKeyBase64: string
    :param publicKeyBase64: [REQUIRED]
            A base64-encoded public key of the ssh-rsa type.
            

    :rtype: dict
    :return: {
        'operation': {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        }
    }
    
    
    """
    pass

def is_vpc_peered():
    """
    Returns a Boolean value indicating whether your Lightsail VPC is peered.
    See also: AWS API Documentation
    
    
    :example: response = client.is_vpc_peered()
    
    
    :rtype: dict
    :return: {
        'isPeered': True|False
    }
    
    
    """
    pass

def open_instance_public_ports(portInfo=None, instanceName=None):
    """
    Adds public ports to an Amazon Lightsail instance.
    See also: AWS API Documentation
    
    
    :example: response = client.open_instance_public_ports(
        portInfo={
            'fromPort': 123,
            'toPort': 123,
            'protocol': 'tcp'|'all'|'udp'
        },
        instanceName='string'
    )
    
    
    :type portInfo: dict
    :param portInfo: [REQUIRED]
            An array of key-value pairs containing information about the port mappings.
            fromPort (integer) --The first port in the range.
            toPort (integer) --The last port in the range.
            protocol (string) --The protocol.
            

    :type instanceName: string
    :param instanceName: [REQUIRED]
            The name of the instance for which you want to open the public ports.
            

    :rtype: dict
    :return: {
        'operation': {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        }
    }
    
    
    """
    pass

def peer_vpc():
    """
    Tries to peer the Lightsail VPC with the user's default VPC.
    See also: AWS API Documentation
    
    
    :example: response = client.peer_vpc()
    
    
    :rtype: dict
    :return: {
        'operation': {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        }
    }
    
    
    """
    pass

def put_instance_public_ports(portInfos=None, instanceName=None):
    """
    Sets the specified open ports for an Amazon Lightsail instance, and closes all ports for every protocol not included in the current request.
    See also: AWS API Documentation
    
    
    :example: response = client.put_instance_public_ports(
        portInfos=[
            {
                'fromPort': 123,
                'toPort': 123,
                'protocol': 'tcp'|'all'|'udp'
            },
        ],
        instanceName='string'
    )
    
    
    :type portInfos: list
    :param portInfos: [REQUIRED]
            Specifies information about the public port(s).
            (dict) --Describes information about the ports on your virtual private server (or instance ).
            fromPort (integer) --The first port in the range.
            toPort (integer) --The last port in the range.
            protocol (string) --The protocol.
            
            

    :type instanceName: string
    :param instanceName: [REQUIRED]
            The Lightsail instance name of the public port(s) you are setting.
            

    :rtype: dict
    :return: {
        'operation': {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        }
    }
    
    
    """
    pass

def reboot_instance(instanceName=None):
    """
    Restarts a specific instance. When your Amazon Lightsail instance is finished rebooting, Lightsail assigns a new public IP address. To use the same IP address after restarting, create a static IP address and attach it to the instance.
    See also: AWS API Documentation
    
    
    :example: response = client.reboot_instance(
        instanceName='string'
    )
    
    
    :type instanceName: string
    :param instanceName: [REQUIRED]
            The name of the instance to reboot.
            

    :rtype: dict
    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def release_static_ip(staticIpName=None):
    """
    Deletes a specific static IP from your account.
    See also: AWS API Documentation
    
    
    :example: response = client.release_static_ip(
        staticIpName='string'
    )
    
    
    :type staticIpName: string
    :param staticIpName: [REQUIRED]
            The name of the static IP to delete.
            

    :rtype: dict
    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def start_instance(instanceName=None):
    """
    Starts a specific Amazon Lightsail instance from a stopped state. To restart an instance, use the reboot instance operation.
    See also: AWS API Documentation
    
    
    :example: response = client.start_instance(
        instanceName='string'
    )
    
    
    :type instanceName: string
    :param instanceName: [REQUIRED]
            The name of the instance (a virtual private server) to start.
            

    :rtype: dict
    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def stop_instance(instanceName=None):
    """
    Stops a specific Amazon Lightsail instance that is currently running.
    See also: AWS API Documentation
    
    
    :example: response = client.stop_instance(
        instanceName='string'
    )
    
    
    :type instanceName: string
    :param instanceName: [REQUIRED]
            The name of the instance (a virtual private server) to stop.
            

    :rtype: dict
    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def unpeer_vpc():
    """
    Attempts to unpeer the Lightsail VPC from the user's default VPC.
    See also: AWS API Documentation
    
    
    :example: response = client.unpeer_vpc()
    
    
    :rtype: dict
    :return: {
        'operation': {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        }
    }
    
    
    """
    pass

def update_domain_entry(domainName=None, domainEntry=None):
    """
    Updates a domain recordset after it is created.
    See also: AWS API Documentation
    
    
    :example: response = client.update_domain_entry(
        domainName='string',
        domainEntry={
            'id': 'string',
            'name': 'string',
            'target': 'string',
            'type': 'string',
            'options': {
                'string': 'string'
            }
        }
    )
    
    
    :type domainName: string
    :param domainName: [REQUIRED]
            The name of the domain recordset to update.
            

    :type domainEntry: dict
    :param domainEntry: [REQUIRED]
            An array of key-value pairs containing information about the domain entry.
            id (string) --The ID of the domain recordset entry.
            name (string) --The name of the domain.
            target (string) --The target AWS name server (e.g., ns-111.awsdns-22.com. ).
            type (string) --The type of domain entry (e.g., SOA or NS ).
            options (dict) --The options for the domain entry.
            (string) --
            (string) --
            
            

    :rtype: dict
    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

