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
    
    Exceptions
    
    :example: response = client.allocate_static_ip(
        staticIpName='string'
    )
    
    
    :type staticIpName: string
    :param staticIpName: [REQUIRED]\nThe name of the static IP address.\n

    :rtype: dict
ReturnsResponse Syntax{
    'operations': [
        {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        },
    ]
}


Response Structure

(dict) --
operations (list) --An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

(dict) --Describes the API operation.

id (string) --The ID of the operation.

resourceName (string) --The resource name.

resourceType (string) --The resource type.

createdAt (datetime) --The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --The AWS Region and Availability Zone.

availabilityZone (string) --The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --The AWS Region name.



isTerminal (boolean) --A Boolean value indicating whether the operation is terminal.

operationDetails (string) --Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --The type of operation.

status (string) --The status of the operation.

statusChangedAt (datetime) --The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --The error code.

errorDetails (string) --The error details.










Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def attach_disk(diskName=None, instanceName=None, diskPath=None):
    """
    Attaches a block storage disk to a running or stopped Lightsail instance and exposes it to the instance with the specified disk name.
    The attach disk operation supports tag-based access control via resource tags applied to the resource identified by disk name . For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.attach_disk(
        diskName='string',
        instanceName='string',
        diskPath='string'
    )
    
    
    :type diskName: string
    :param diskName: [REQUIRED]\nThe unique Lightsail disk name (e.g., my-disk ).\n

    :type instanceName: string
    :param instanceName: [REQUIRED]\nThe name of the Lightsail instance where you want to utilize the storage disk.\n

    :type diskPath: string
    :param diskPath: [REQUIRED]\nThe disk path to expose to the instance (e.g., /dev/xvdf ).\n

    :rtype: dict

ReturnsResponse Syntax
{
    'operations': [
        {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        },
    ]
}


Response Structure

(dict) --

operations (list) --
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

(dict) --
Describes the API operation.

id (string) --
The ID of the operation.

resourceName (string) --
The resource name.

resourceType (string) --
The resource type.

createdAt (datetime) --
The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --
The AWS Region and Availability Zone.

availabilityZone (string) --
The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --
The AWS Region name.



isTerminal (boolean) --
A Boolean value indicating whether the operation is terminal.

operationDetails (string) --
Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --
The type of operation.

status (string) --
The status of the operation.

statusChangedAt (datetime) --
The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --
The error code.

errorDetails (string) --
The error details.











Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    :returns: 
    Lightsail.Client.exceptions.ServiceException
    Lightsail.Client.exceptions.InvalidInputException
    Lightsail.Client.exceptions.NotFoundException
    Lightsail.Client.exceptions.OperationFailureException
    Lightsail.Client.exceptions.AccessDeniedException
    Lightsail.Client.exceptions.AccountSetupInProgressException
    Lightsail.Client.exceptions.UnauthenticatedException
    
    """
    pass

def attach_instances_to_load_balancer(loadBalancerName=None, instanceNames=None):
    """
    Attaches one or more Lightsail instances to a load balancer.
    After some time, the instances are attached to the load balancer and the health check status is available.
    The attach instances to load balancer operation supports tag-based access control via resource tags applied to the resource identified by load balancer name . For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.attach_instances_to_load_balancer(
        loadBalancerName='string',
        instanceNames=[
            'string',
        ]
    )
    
    
    :type loadBalancerName: string
    :param loadBalancerName: [REQUIRED]\nThe name of the load balancer.\n

    :type instanceNames: list
    :param instanceNames: [REQUIRED]\nAn array of strings representing the instance name(s) you want to attach to your load balancer.\nAn instance must be running before you can attach it to your load balancer.\nThere are no additional limits on the number of instances you can attach to your load balancer, aside from the limit of Lightsail instances you can create in your account (20).\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'operations': [
        {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        },
    ]
}


Response Structure

(dict) --

operations (list) --
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

(dict) --
Describes the API operation.

id (string) --
The ID of the operation.

resourceName (string) --
The resource name.

resourceType (string) --
The resource type.

createdAt (datetime) --
The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --
The AWS Region and Availability Zone.

availabilityZone (string) --
The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --
The AWS Region name.



isTerminal (boolean) --
A Boolean value indicating whether the operation is terminal.

operationDetails (string) --
Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --
The type of operation.

status (string) --
The status of the operation.

statusChangedAt (datetime) --
The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --
The error code.

errorDetails (string) --
The error details.











Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    :returns: 
    Lightsail.Client.exceptions.ServiceException
    Lightsail.Client.exceptions.InvalidInputException
    Lightsail.Client.exceptions.NotFoundException
    Lightsail.Client.exceptions.OperationFailureException
    Lightsail.Client.exceptions.AccessDeniedException
    Lightsail.Client.exceptions.AccountSetupInProgressException
    Lightsail.Client.exceptions.UnauthenticatedException
    
    """
    pass

def attach_load_balancer_tls_certificate(loadBalancerName=None, certificateName=None):
    """
    Attaches a Transport Layer Security (TLS) certificate to your load balancer. TLS is just an updated, more secure version of Secure Socket Layer (SSL).
    Once you create and validate your certificate, you can attach it to your load balancer. You can also use this API to rotate the certificates on your account. Use the AttachLoadBalancerTlsCertificate action with the non-attached certificate, and it will replace the existing one and become the attached certificate.
    The AttachLoadBalancerTlsCertificate operation supports tag-based access control via resource tags applied to the resource identified by load balancer name . For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.attach_load_balancer_tls_certificate(
        loadBalancerName='string',
        certificateName='string'
    )
    
    
    :type loadBalancerName: string
    :param loadBalancerName: [REQUIRED]\nThe name of the load balancer to which you want to associate the SSL/TLS certificate.\n

    :type certificateName: string
    :param certificateName: [REQUIRED]\nThe name of your SSL/TLS certificate.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'operations': [
        {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        },
    ]
}


Response Structure

(dict) --

operations (list) --
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.
These SSL/TLS certificates are only usable by Lightsail load balancers. You can\'t get the certificate and use it for another purpose.

(dict) --
Describes the API operation.

id (string) --
The ID of the operation.

resourceName (string) --
The resource name.

resourceType (string) --
The resource type.

createdAt (datetime) --
The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --
The AWS Region and Availability Zone.

availabilityZone (string) --
The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --
The AWS Region name.



isTerminal (boolean) --
A Boolean value indicating whether the operation is terminal.

operationDetails (string) --
Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --
The type of operation.

status (string) --
The status of the operation.

statusChangedAt (datetime) --
The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --
The error code.

errorDetails (string) --
The error details.











Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    :returns: 
    Lightsail.Client.exceptions.ServiceException
    Lightsail.Client.exceptions.InvalidInputException
    Lightsail.Client.exceptions.NotFoundException
    Lightsail.Client.exceptions.OperationFailureException
    Lightsail.Client.exceptions.AccessDeniedException
    Lightsail.Client.exceptions.AccountSetupInProgressException
    Lightsail.Client.exceptions.UnauthenticatedException
    
    """
    pass

def attach_static_ip(staticIpName=None, instanceName=None):
    """
    Attaches a static IP address to a specific Amazon Lightsail instance.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.attach_static_ip(
        staticIpName='string',
        instanceName='string'
    )
    
    
    :type staticIpName: string
    :param staticIpName: [REQUIRED]\nThe name of the static IP.\n

    :type instanceName: string
    :param instanceName: [REQUIRED]\nThe instance name to which you want to attach the static IP address.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'operations': [
        {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        },
    ]
}


Response Structure

(dict) --

operations (list) --
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

(dict) --
Describes the API operation.

id (string) --
The ID of the operation.

resourceName (string) --
The resource name.

resourceType (string) --
The resource type.

createdAt (datetime) --
The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --
The AWS Region and Availability Zone.

availabilityZone (string) --
The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --
The AWS Region name.



isTerminal (boolean) --
A Boolean value indicating whether the operation is terminal.

operationDetails (string) --
Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --
The type of operation.

status (string) --
The status of the operation.

statusChangedAt (datetime) --
The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --
The error code.

errorDetails (string) --
The error details.











Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    :returns: 
    Lightsail.Client.exceptions.ServiceException
    Lightsail.Client.exceptions.InvalidInputException
    Lightsail.Client.exceptions.NotFoundException
    Lightsail.Client.exceptions.OperationFailureException
    Lightsail.Client.exceptions.AccessDeniedException
    Lightsail.Client.exceptions.AccountSetupInProgressException
    Lightsail.Client.exceptions.UnauthenticatedException
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def close_instance_public_ports(portInfo=None, instanceName=None):
    """
    Closes ports for a specific Amazon Lightsail instance.
    The CloseInstancePublicPorts action supports tag-based access control via resource tags applied to the resource identified by instanceName . For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.close_instance_public_ports(
        portInfo={
            'fromPort': 123,
            'toPort': 123,
            'protocol': 'tcp'|'all'|'udp'|'icmp',
            'cidrs': [
                'string',
            ],
            'cidrListAliases': [
                'string',
            ]
        },
        instanceName='string'
    )
    
    
    :type portInfo: dict
    :param portInfo: [REQUIRED]\nAn object to describe the ports to close for the specified instance.\n\nfromPort (integer) --The first port in a range of open ports on an instance.\nAllowed ports:\n\nTCP and UDP - 0 to 65535\nICMP - 8 (to configure Ping)\n\n\nNote\nPing is the only communication supported through the ICMP protocol in Lightsail. To configure ping, specify the fromPort parameter as 8 , and the toPort parameter as -1 .\n\n\ntoPort (integer) --The last port in a range of open ports on an instance.\nAllowed ports:\n\nTCP and UDP - 0 to 65535\nICMP - -1 (to configure Ping)\n\n\nNote\nPing is the only communication supported through the ICMP protocol in Lightsail. To configure ping, specify the fromPort parameter as 8 , and the toPort parameter as -1 .\n\n\nprotocol (string) --The IP protocol name.\nThe name can be one of the following:\n\ntcp - Transmission Control Protocol (TCP) provides reliable, ordered, and error-checked delivery of streamed data between applications running on hosts communicating by an IP network. If you have an application that doesn\'t require reliable data stream service, use UDP instead.\nall - All transport layer protocol types. For more general information, see Transport layer on Wikipedia .\nudp - With User Datagram Protocol (UDP), computer applications can send messages (or datagrams) to other hosts on an Internet Protocol (IP) network. Prior communications are not required to set up transmission channels or data paths. Applications that don\'t require reliable data stream service can use UDP, which provides a connectionless datagram service that emphasizes reduced latency over reliability. If you do require reliable data stream service, use TCP instead.\nicmp - Internet Control Message Protocol (ICMP) is used to send error messages and operational information indicating success or failure when communicating with an instance. For example, an error is indicated when an instance could not be reached.\n\n\nNote\nPing is the only communication supported through the ICMP protocol in Lightsail. To configure ping, specify the fromPort parameter as 8 , and the toPort parameter as -1 .\n\n\ncidrs (list) --The IP address, or range of IP addresses in CIDR notation, that are allowed to connect to an instance through the ports, and the protocol. Lightsail supports IPv4 addresses.\nExamples:\n\nTo allow the IP address 192.0.2.44 , specify 192.0.2.44 or 192.0.2.44/32 .\nTo allow the IP addresses 192.0.2.0 to 192.0.2.255 , specify 192.0.2.0/24 .\n\nFor more information about CIDR block notation, see Classless Inter-Domain Routing on Wikipedia .\n\n(string) --\n\n\ncidrListAliases (list) --An alias that defines access for a preconfigured range of IP addresses.\nThe only alias currently supported is lightsail-connect , which allows IP addresses of the browser-based RDP/SSH client in the Lightsail console to connect to your instance.\n\n(string) --\n\n\n\n

    :type instanceName: string
    :param instanceName: [REQUIRED]\nThe name of the instance for which to close ports.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'operation': {
        'id': 'string',
        'resourceName': 'string',
        'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
        'createdAt': datetime(2015, 1, 1),
        'location': {
            'availabilityZone': 'string',
            'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
        },
        'isTerminal': True|False,
        'operationDetails': 'string',
        'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
        'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
        'statusChangedAt': datetime(2015, 1, 1),
        'errorCode': 'string',
        'errorDetails': 'string'
    }
}


Response Structure

(dict) --

operation (dict) --
An object that describes the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

id (string) --
The ID of the operation.

resourceName (string) --
The resource name.

resourceType (string) --
The resource type.

createdAt (datetime) --
The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --
The AWS Region and Availability Zone.

availabilityZone (string) --
The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --
The AWS Region name.



isTerminal (boolean) --
A Boolean value indicating whether the operation is terminal.

operationDetails (string) --
Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --
The type of operation.

status (string) --
The status of the operation.

statusChangedAt (datetime) --
The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --
The error code.

errorDetails (string) --
The error details.









Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operation': {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        }
    }
    
    
    :returns: 
    Lightsail.Client.exceptions.ServiceException
    Lightsail.Client.exceptions.InvalidInputException
    Lightsail.Client.exceptions.NotFoundException
    Lightsail.Client.exceptions.OperationFailureException
    Lightsail.Client.exceptions.AccessDeniedException
    Lightsail.Client.exceptions.AccountSetupInProgressException
    Lightsail.Client.exceptions.UnauthenticatedException
    
    """
    pass

def copy_snapshot(sourceSnapshotName=None, sourceResourceName=None, restoreDate=None, useLatestRestorableAutoSnapshot=None, targetSnapshotName=None, sourceRegion=None):
    """
    Copies a manual snapshot of an instance or disk as another manual snapshot, or copies an automatic snapshot of an instance or disk as a manual snapshot. This operation can also be used to copy a manual or automatic snapshot of an instance or a disk from one AWS Region to another in Amazon Lightsail.
    When copying a manual snapshot , be sure to define the source region , source snapshot name , and target snapshot name parameters.
    When copying an automatic snapshot , be sure to define the source region , source resource name , target snapshot name , and either the restore date or the use latest restorable auto snapshot parameters.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.copy_snapshot(
        sourceSnapshotName='string',
        sourceResourceName='string',
        restoreDate='string',
        useLatestRestorableAutoSnapshot=True|False,
        targetSnapshotName='string',
        sourceRegion='us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
    )
    
    
    :type sourceSnapshotName: string
    :param sourceSnapshotName: The name of the source manual snapshot to copy.\nConstraint:\n\nDefine this parameter only when copying a manual snapshot as another manual snapshot.\n\n

    :type sourceResourceName: string
    :param sourceResourceName: The name of the source instance or disk from which the source automatic snapshot was created.\nConstraint:\n\nDefine this parameter only when copying an automatic snapshot as a manual snapshot. For more information, see the Lightsail Dev Guide .\n\n

    :type restoreDate: string
    :param restoreDate: The date of the source automatic snapshot to copy. Use the get auto snapshots operation to identify the dates of the available automatic snapshots.\nConstraints:\n\nMust be specified in YYYY-MM-DD format.\nThis parameter cannot be defined together with the use latest restorable auto snapshot parameter. The restore date and use latest restorable auto snapshot parameters are mutually exclusive.\nDefine this parameter only when copying an automatic snapshot as a manual snapshot. For more information, see the Lightsail Dev Guide .\n\n

    :type useLatestRestorableAutoSnapshot: boolean
    :param useLatestRestorableAutoSnapshot: A Boolean value to indicate whether to use the latest available automatic snapshot of the specified source instance or disk.\nConstraints:\n\nThis parameter cannot be defined together with the restore date parameter. The use latest restorable auto snapshot and restore date parameters are mutually exclusive.\nDefine this parameter only when copying an automatic snapshot as a manual snapshot. For more information, see the Lightsail Dev Guide .\n\n

    :type targetSnapshotName: string
    :param targetSnapshotName: [REQUIRED]\nThe name of the new manual snapshot to be created as a copy.\n

    :type sourceRegion: string
    :param sourceRegion: [REQUIRED]\nThe AWS Region where the source manual or automatic snapshot is located.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'operations': [
        {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        },
    ]
}


Response Structure

(dict) --

operations (list) --
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

(dict) --
Describes the API operation.

id (string) --
The ID of the operation.

resourceName (string) --
The resource name.

resourceType (string) --
The resource type.

createdAt (datetime) --
The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --
The AWS Region and Availability Zone.

availabilityZone (string) --
The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --
The AWS Region name.



isTerminal (boolean) --
A Boolean value indicating whether the operation is terminal.

operationDetails (string) --
Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --
The type of operation.

status (string) --
The status of the operation.

statusChangedAt (datetime) --
The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --
The error code.

errorDetails (string) --
The error details.











Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    :returns: 
    Lightsail.Client.exceptions.ServiceException
    Lightsail.Client.exceptions.InvalidInputException
    Lightsail.Client.exceptions.NotFoundException
    Lightsail.Client.exceptions.OperationFailureException
    Lightsail.Client.exceptions.AccessDeniedException
    Lightsail.Client.exceptions.AccountSetupInProgressException
    Lightsail.Client.exceptions.UnauthenticatedException
    
    """
    pass

def create_cloud_formation_stack(instances=None):
    """
    Creates an AWS CloudFormation stack, which creates a new Amazon EC2 instance from an exported Amazon Lightsail snapshot. This operation results in a CloudFormation stack record that can be used to track the AWS CloudFormation stack created. Use the get cloud formation stack records operation to get a list of the CloudFormation stacks created.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_cloud_formation_stack(
        instances=[
            {
                'sourceName': 'string',
                'instanceType': 'string',
                'portInfoSource': 'DEFAULT'|'INSTANCE'|'NONE'|'CLOSED',
                'userData': 'string',
                'availabilityZone': 'string'
            },
        ]
    )
    
    
    :type instances: list
    :param instances: [REQUIRED]\nAn array of parameters that will be used to create the new Amazon EC2 instance. You can only pass one instance entry at a time in this array. You will get an invalid parameter error if you pass more than one instance entry in this array.\n\n(dict) --Describes the Amazon Elastic Compute Cloud instance and related resources to be created using the create cloud formation stack operation.\n\nsourceName (string) -- [REQUIRED]The name of the export snapshot record, which contains the exported Lightsail instance snapshot that will be used as the source of the new Amazon EC2 instance.\nUse the get export snapshot records operation to get a list of export snapshot records that you can use to create a CloudFormation stack.\n\ninstanceType (string) -- [REQUIRED]The instance type (e.g., t2.micro ) to use for the new Amazon EC2 instance.\n\nportInfoSource (string) -- [REQUIRED]The port configuration to use for the new Amazon EC2 instance.\nThe following configuration options are available:\n\nDEFAULT - Use the default firewall settings from the Lightsail instance blueprint.\nINSTANCE - Use the configured firewall settings from the source Lightsail instance.\nNONE - Use the default Amazon EC2 security group.\nCLOSED - All ports closed.\n\n\nNote\nIf you configured lightsail-connect as a cidrListAliases on your instance, or if you chose to allow the Lightsail browser-based SSH or RDP clients to connect to your instance, that configuration is not carried over to your new Amazon EC2 instance.\n\n\nuserData (string) --A launch script you can create that configures a server with additional user data. For example, you might want to run apt-get -y update .\n\nNote\nDepending on the machine image you choose, the command to get software on your instance varies. Amazon Linux and CentOS use yum , Debian and Ubuntu use apt-get , and FreeBSD uses pkg .\n\n\navailabilityZone (string) -- [REQUIRED]The Availability Zone for the new Amazon EC2 instance.\n\n\n\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'operations': [
        {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        },
    ]
}


Response Structure

(dict) --
operations (list) --An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

(dict) --Describes the API operation.

id (string) --The ID of the operation.

resourceName (string) --The resource name.

resourceType (string) --The resource type.

createdAt (datetime) --The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --The AWS Region and Availability Zone.

availabilityZone (string) --The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --The AWS Region name.



isTerminal (boolean) --A Boolean value indicating whether the operation is terminal.

operationDetails (string) --Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --The type of operation.

status (string) --The status of the operation.

statusChangedAt (datetime) --The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --The error code.

errorDetails (string) --The error details.










Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    :returns: 
    Lightsail.Client.exceptions.ServiceException
    Lightsail.Client.exceptions.InvalidInputException
    Lightsail.Client.exceptions.NotFoundException
    Lightsail.Client.exceptions.OperationFailureException
    Lightsail.Client.exceptions.AccessDeniedException
    Lightsail.Client.exceptions.AccountSetupInProgressException
    Lightsail.Client.exceptions.UnauthenticatedException
    
    """
    pass

def create_contact_method(protocol=None, contactEndpoint=None):
    """
    Creates an email or SMS text message contact method.
    A contact method is used to send you notifications about your Amazon Lightsail resources. You can add one email address and one mobile phone number contact method in each AWS Region. However, SMS text messaging is not supported in some AWS Regions, and SMS text messages cannot be sent to some countries/regions. For more information, see Notifications in Amazon Lightsail .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_contact_method(
        protocol='Email'|'SMS',
        contactEndpoint='string'
    )
    
    
    :type protocol: string
    :param protocol: [REQUIRED]\nThe protocol of the contact method, such as Email or SMS (text messaging).\nThe SMS protocol is supported only in the following AWS Regions.\n\nUS East (N. Virginia) (us-east-1 )\nUS West (Oregon) (us-west-2 )\nEurope (Ireland) (eu-west-1 )\nAsia Pacific (Tokyo) (ap-northeast-1 )\nAsia Pacific (Singapore) (ap-southeast-1 )\nAsia Pacific (Sydney) (ap-southeast-2 )\n\nFor a list of countries/regions where SMS text messages can be sent, and the latest AWS Regions where SMS text messaging is supported, see Supported Regions and Countries in the Amazon SNS Developer Guide .\nFor more information about notifications in Amazon Lightsail, see Notifications in Amazon Lightsail .\n

    :type contactEndpoint: string
    :param contactEndpoint: [REQUIRED]\nThe destination of the contact method, such as an email address or a mobile phone number.\nUse the E.164 format when specifying a mobile phone number. E.164 is a standard for the phone number structure used for international telecommunication. Phone numbers that follow this format can have a maximum of 15 digits, and they are prefixed with the plus character (+) and the country code. For example, a U.S. phone number in E.164 format would be specified as +1XXX5550100. For more information, see E.164 on Wikipedia .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'operations': [
        {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        },
    ]
}


Response Structure

(dict) --

operations (list) --
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

(dict) --
Describes the API operation.

id (string) --
The ID of the operation.

resourceName (string) --
The resource name.

resourceType (string) --
The resource type.

createdAt (datetime) --
The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --
The AWS Region and Availability Zone.

availabilityZone (string) --
The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --
The AWS Region name.



isTerminal (boolean) --
A Boolean value indicating whether the operation is terminal.

operationDetails (string) --
Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --
The type of operation.

status (string) --
The status of the operation.

statusChangedAt (datetime) --
The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --
The error code.

errorDetails (string) --
The error details.











Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    :returns: 
    Lightsail.Client.exceptions.ServiceException
    Lightsail.Client.exceptions.InvalidInputException
    Lightsail.Client.exceptions.NotFoundException
    Lightsail.Client.exceptions.OperationFailureException
    Lightsail.Client.exceptions.AccessDeniedException
    Lightsail.Client.exceptions.UnauthenticatedException
    
    """
    pass

def create_disk(diskName=None, availabilityZone=None, sizeInGb=None, tags=None, addOns=None):
    """
    Creates a block storage disk that can be attached to an Amazon Lightsail instance in the same Availability Zone (e.g., us-east-2a ).
    The create disk operation supports tag-based access control via request tags. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_disk(
        diskName='string',
        availabilityZone='string',
        sizeInGb=123,
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ],
        addOns=[
            {
                'addOnType': 'AutoSnapshot',
                'autoSnapshotAddOnRequest': {
                    'snapshotTimeOfDay': 'string'
                }
            },
        ]
    )
    
    
    :type diskName: string
    :param diskName: [REQUIRED]\nThe unique Lightsail disk name (e.g., my-disk ).\n

    :type availabilityZone: string
    :param availabilityZone: [REQUIRED]\nThe Availability Zone where you want to create the disk (e.g., us-east-2a ). Use the same Availability Zone as the Lightsail instance to which you want to attach the disk.\nUse the get regions operation to list the Availability Zones where Lightsail is currently available.\n

    :type sizeInGb: integer
    :param sizeInGb: [REQUIRED]\nThe size of the disk in GB (e.g., 32 ).\n

    :type tags: list
    :param tags: The tag keys and optional values to add to the resource during create.\nTo tag a resource after it has been created, see the tag resource operation.\n\n(dict) --Describes a tag key and optional value assigned to an Amazon Lightsail resource.\nFor more information about tags in Lightsail, see the Lightsail Dev Guide .\n\nkey (string) --The key of the tag.\nConstraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @\n\nvalue (string) --The value of the tag.\nConstraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @\n\n\n\n\n

    :type addOns: list
    :param addOns: An array of objects that represent the add-ons to enable for the new disk.\n\n(dict) --Describes a request to enable, modify, or disable an add-on for an Amazon Lightsail resource.\n\nNote\nAn additional cost may be associated with enabling add-ons. For more information, see the Lightsail pricing page .\n\n\naddOnType (string) -- [REQUIRED]The add-on type.\n\nautoSnapshotAddOnRequest (dict) --An object that represents additional parameters when enabling or modifying the automatic snapshot add-on.\n\nsnapshotTimeOfDay (string) --The daily time when an automatic snapshot will be created.\nConstraints:\n\nMust be in HH:00 format, and in an hourly increment.\nSpecified in Coordinated Universal Time (UTC).\nThe snapshot will be automatically created between the time specified and up to 45 minutes after.\n\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'operations': [
        {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        },
    ]
}


Response Structure

(dict) --

operations (list) --
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

(dict) --
Describes the API operation.

id (string) --
The ID of the operation.

resourceName (string) --
The resource name.

resourceType (string) --
The resource type.

createdAt (datetime) --
The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --
The AWS Region and Availability Zone.

availabilityZone (string) --
The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --
The AWS Region name.



isTerminal (boolean) --
A Boolean value indicating whether the operation is terminal.

operationDetails (string) --
Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --
The type of operation.

status (string) --
The status of the operation.

statusChangedAt (datetime) --
The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --
The error code.

errorDetails (string) --
The error details.











Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    :returns: 
    Lightsail.Client.exceptions.ServiceException
    Lightsail.Client.exceptions.InvalidInputException
    Lightsail.Client.exceptions.NotFoundException
    Lightsail.Client.exceptions.OperationFailureException
    Lightsail.Client.exceptions.AccessDeniedException
    Lightsail.Client.exceptions.AccountSetupInProgressException
    Lightsail.Client.exceptions.UnauthenticatedException
    
    """
    pass

def create_disk_from_snapshot(diskName=None, diskSnapshotName=None, availabilityZone=None, sizeInGb=None, tags=None, addOns=None, sourceDiskName=None, restoreDate=None, useLatestRestorableAutoSnapshot=None):
    """
    Creates a block storage disk from a manual or automatic snapshot of a disk. The resulting disk can be attached to an Amazon Lightsail instance in the same Availability Zone (e.g., us-east-2a ).
    The create disk from snapshot operation supports tag-based access control via request tags and resource tags applied to the resource identified by disk snapshot name . For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_disk_from_snapshot(
        diskName='string',
        diskSnapshotName='string',
        availabilityZone='string',
        sizeInGb=123,
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ],
        addOns=[
            {
                'addOnType': 'AutoSnapshot',
                'autoSnapshotAddOnRequest': {
                    'snapshotTimeOfDay': 'string'
                }
            },
        ],
        sourceDiskName='string',
        restoreDate='string',
        useLatestRestorableAutoSnapshot=True|False
    )
    
    
    :type diskName: string
    :param diskName: [REQUIRED]\nThe unique Lightsail disk name (e.g., my-disk ).\n

    :type diskSnapshotName: string
    :param diskSnapshotName: The name of the disk snapshot (e.g., my-snapshot ) from which to create the new storage disk.\nConstraint:\n\nThis parameter cannot be defined together with the source disk name parameter. The disk snapshot name and source disk name parameters are mutually exclusive.\n\n

    :type availabilityZone: string
    :param availabilityZone: [REQUIRED]\nThe Availability Zone where you want to create the disk (e.g., us-east-2a ). Choose the same Availability Zone as the Lightsail instance where you want to create the disk.\nUse the GetRegions operation to list the Availability Zones where Lightsail is currently available.\n

    :type sizeInGb: integer
    :param sizeInGb: [REQUIRED]\nThe size of the disk in GB (e.g., 32 ).\n

    :type tags: list
    :param tags: The tag keys and optional values to add to the resource during create.\nTo tag a resource after it has been created, see the tag resource operation.\n\n(dict) --Describes a tag key and optional value assigned to an Amazon Lightsail resource.\nFor more information about tags in Lightsail, see the Lightsail Dev Guide .\n\nkey (string) --The key of the tag.\nConstraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @\n\nvalue (string) --The value of the tag.\nConstraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @\n\n\n\n\n

    :type addOns: list
    :param addOns: An array of objects that represent the add-ons to enable for the new disk.\n\n(dict) --Describes a request to enable, modify, or disable an add-on for an Amazon Lightsail resource.\n\nNote\nAn additional cost may be associated with enabling add-ons. For more information, see the Lightsail pricing page .\n\n\naddOnType (string) -- [REQUIRED]The add-on type.\n\nautoSnapshotAddOnRequest (dict) --An object that represents additional parameters when enabling or modifying the automatic snapshot add-on.\n\nsnapshotTimeOfDay (string) --The daily time when an automatic snapshot will be created.\nConstraints:\n\nMust be in HH:00 format, and in an hourly increment.\nSpecified in Coordinated Universal Time (UTC).\nThe snapshot will be automatically created between the time specified and up to 45 minutes after.\n\n\n\n\n\n\n\n

    :type sourceDiskName: string
    :param sourceDiskName: The name of the source disk from which the source automatic snapshot was created.\nConstraints:\n\nThis parameter cannot be defined together with the disk snapshot name parameter. The source disk name and disk snapshot name parameters are mutually exclusive.\nDefine this parameter only when creating a new disk from an automatic snapshot. For more information, see the Lightsail Dev Guide .\n\n

    :type restoreDate: string
    :param restoreDate: The date of the automatic snapshot to use for the new disk. Use the get auto snapshots operation to identify the dates of the available automatic snapshots.\nConstraints:\n\nMust be specified in YYYY-MM-DD format.\nThis parameter cannot be defined together with the use latest restorable auto snapshot parameter. The restore date and use latest restorable auto snapshot parameters are mutually exclusive.\nDefine this parameter only when creating a new disk from an automatic snapshot. For more information, see the Lightsail Dev Guide .\n\n

    :type useLatestRestorableAutoSnapshot: boolean
    :param useLatestRestorableAutoSnapshot: A Boolean value to indicate whether to use the latest available automatic snapshot.\nConstraints:\n\nThis parameter cannot be defined together with the restore date parameter. The use latest restorable auto snapshot and restore date parameters are mutually exclusive.\nDefine this parameter only when creating a new disk from an automatic snapshot. For more information, see the Lightsail Dev Guide .\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'operations': [
        {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        },
    ]
}


Response Structure

(dict) --

operations (list) --
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

(dict) --
Describes the API operation.

id (string) --
The ID of the operation.

resourceName (string) --
The resource name.

resourceType (string) --
The resource type.

createdAt (datetime) --
The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --
The AWS Region and Availability Zone.

availabilityZone (string) --
The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --
The AWS Region name.



isTerminal (boolean) --
A Boolean value indicating whether the operation is terminal.

operationDetails (string) --
Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --
The type of operation.

status (string) --
The status of the operation.

statusChangedAt (datetime) --
The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --
The error code.

errorDetails (string) --
The error details.











Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    :returns: 
    Lightsail.Client.exceptions.ServiceException
    Lightsail.Client.exceptions.InvalidInputException
    Lightsail.Client.exceptions.NotFoundException
    Lightsail.Client.exceptions.OperationFailureException
    Lightsail.Client.exceptions.AccessDeniedException
    Lightsail.Client.exceptions.AccountSetupInProgressException
    Lightsail.Client.exceptions.UnauthenticatedException
    
    """
    pass

def create_disk_snapshot(diskName=None, diskSnapshotName=None, instanceName=None, tags=None):
    """
    Creates a snapshot of a block storage disk. You can use snapshots for backups, to make copies of disks, and to save data before shutting down a Lightsail instance.
    You can take a snapshot of an attached disk that is in use; however, snapshots only capture data that has been written to your disk at the time the snapshot command is issued. This may exclude any data that has been cached by any applications or the operating system. If you can pause any file systems on the disk long enough to take a snapshot, your snapshot should be complete. Nevertheless, if you cannot pause all file writes to the disk, you should unmount the disk from within the Lightsail instance, issue the create disk snapshot command, and then remount the disk to ensure a consistent and complete snapshot. You may remount and use your disk while the snapshot status is pending.
    You can also use this operation to create a snapshot of an instance\'s system volume. You might want to do this, for example, to recover data from the system volume of a botched instance or to create a backup of the system volume like you would for a block storage disk. To create a snapshot of a system volume, just define the instance name parameter when issuing the snapshot command, and a snapshot of the defined instance\'s system volume will be created. After the snapshot is available, you can create a block storage disk from the snapshot and attach it to a running instance to access the data on the disk.
    The create disk snapshot operation supports tag-based access control via request tags. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_disk_snapshot(
        diskName='string',
        diskSnapshotName='string',
        instanceName='string',
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type diskName: string
    :param diskName: The unique name of the source disk (e.g., Disk-Virginia-1 ).\n\nNote\nThis parameter cannot be defined together with the instance name parameter. The disk name and instance name parameters are mutually exclusive.\n\n

    :type diskSnapshotName: string
    :param diskSnapshotName: [REQUIRED]\nThe name of the destination disk snapshot (e.g., my-disk-snapshot ) based on the source disk.\n

    :type instanceName: string
    :param instanceName: The unique name of the source instance (e.g., Amazon_Linux-512MB-Virginia-1 ). When this is defined, a snapshot of the instance\'s system volume is created.\n\nNote\nThis parameter cannot be defined together with the disk name parameter. The instance name and disk name parameters are mutually exclusive.\n\n

    :type tags: list
    :param tags: The tag keys and optional values to add to the resource during create.\nTo tag a resource after it has been created, see the tag resource operation.\n\n(dict) --Describes a tag key and optional value assigned to an Amazon Lightsail resource.\nFor more information about tags in Lightsail, see the Lightsail Dev Guide .\n\nkey (string) --The key of the tag.\nConstraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @\n\nvalue (string) --The value of the tag.\nConstraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'operations': [
        {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        },
    ]
}


Response Structure

(dict) --

operations (list) --
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

(dict) --
Describes the API operation.

id (string) --
The ID of the operation.

resourceName (string) --
The resource name.

resourceType (string) --
The resource type.

createdAt (datetime) --
The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --
The AWS Region and Availability Zone.

availabilityZone (string) --
The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --
The AWS Region name.



isTerminal (boolean) --
A Boolean value indicating whether the operation is terminal.

operationDetails (string) --
Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --
The type of operation.

status (string) --
The status of the operation.

statusChangedAt (datetime) --
The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --
The error code.

errorDetails (string) --
The error details.











Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    :returns: 
    Lightsail.Client.exceptions.ServiceException
    Lightsail.Client.exceptions.InvalidInputException
    Lightsail.Client.exceptions.NotFoundException
    Lightsail.Client.exceptions.OperationFailureException
    Lightsail.Client.exceptions.AccessDeniedException
    Lightsail.Client.exceptions.AccountSetupInProgressException
    Lightsail.Client.exceptions.UnauthenticatedException
    
    """
    pass

def create_domain(domainName=None, tags=None):
    """
    Creates a domain resource for the specified domain (e.g., example.com).
    The create domain operation supports tag-based access control via request tags. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_domain(
        domainName='string',
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type domainName: string
    :param domainName: [REQUIRED]\nThe domain name to manage (e.g., example.com ).\n\nNote\nYou cannot register a new domain name using Lightsail. You must register a domain name using Amazon Route 53 or another domain name registrar. If you have already registered your domain, you can enter its name in this parameter to manage the DNS records for that domain.\n\n

    :type tags: list
    :param tags: The tag keys and optional values to add to the resource during create.\nTo tag a resource after it has been created, see the tag resource operation.\n\n(dict) --Describes a tag key and optional value assigned to an Amazon Lightsail resource.\nFor more information about tags in Lightsail, see the Lightsail Dev Guide .\n\nkey (string) --The key of the tag.\nConstraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @\n\nvalue (string) --The value of the tag.\nConstraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'operation': {
        'id': 'string',
        'resourceName': 'string',
        'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
        'createdAt': datetime(2015, 1, 1),
        'location': {
            'availabilityZone': 'string',
            'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
        },
        'isTerminal': True|False,
        'operationDetails': 'string',
        'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
        'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
        'statusChangedAt': datetime(2015, 1, 1),
        'errorCode': 'string',
        'errorDetails': 'string'
    }
}


Response Structure

(dict) --

operation (dict) --
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

id (string) --
The ID of the operation.

resourceName (string) --
The resource name.

resourceType (string) --
The resource type.

createdAt (datetime) --
The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --
The AWS Region and Availability Zone.

availabilityZone (string) --
The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --
The AWS Region name.



isTerminal (boolean) --
A Boolean value indicating whether the operation is terminal.

operationDetails (string) --
Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --
The type of operation.

status (string) --
The status of the operation.

statusChangedAt (datetime) --
The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --
The error code.

errorDetails (string) --
The error details.









Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operation': {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        }
    }
    
    
    :returns: 
    Lightsail.Client.exceptions.ServiceException
    Lightsail.Client.exceptions.InvalidInputException
    Lightsail.Client.exceptions.NotFoundException
    Lightsail.Client.exceptions.OperationFailureException
    Lightsail.Client.exceptions.AccessDeniedException
    Lightsail.Client.exceptions.AccountSetupInProgressException
    Lightsail.Client.exceptions.UnauthenticatedException
    
    """
    pass

def create_domain_entry(domainName=None, domainEntry=None):
    """
    Creates one of the following entry records associated with the domain: Address (A), canonical name (CNAME), mail exchanger (MX), name server (NS), start of authority (SOA), service locator (SRV), or text (TXT).
    The create domain entry operation supports tag-based access control via resource tags applied to the resource identified by domain name . For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_domain_entry(
        domainName='string',
        domainEntry={
            'id': 'string',
            'name': 'string',
            'target': 'string',
            'isAlias': True|False,
            'type': 'string',
            'options': {
                'string': 'string'
            }
        }
    )
    
    
    :type domainName: string
    :param domainName: [REQUIRED]\nThe domain name (e.g., example.com ) for which you want to create the domain entry.\n

    :type domainEntry: dict
    :param domainEntry: [REQUIRED]\nAn array of key-value pairs containing information about the domain entry request.\n\nid (string) --The ID of the domain recordset entry.\n\nname (string) --The name of the domain.\n\ntarget (string) --The target AWS name server (e.g., ns-111.awsdns-22.com. ).\nFor Lightsail load balancers, the value looks like ab1234c56789c6b86aba6fb203d443bc-123456789.us-east-2.elb.amazonaws.com . Be sure to also set isAlias to true when setting up an A record for a load balancer.\n\nisAlias (boolean) --When true , specifies whether the domain entry is an alias used by the Lightsail load balancer. You can include an alias (A type) record in your request, which points to a load balancer DNS name and routes traffic to your load balancer\n\ntype (string) --The type of domain entry, such as address (A), canonical name (CNAME), mail exchanger (MX), name server (NS), start of authority (SOA), service locator (SRV), or text (TXT).\nThe following domain entry types can be used:\n\nA\nCNAME\nMX\nNS\nSOA\nSRV\nTXT\n\n\noptions (dict) --(Deprecated) The options for the domain entry.\n\nNote\nIn releases prior to November 29, 2017, this parameter was not included in the API response. It is now deprecated.\n\n\n(string) --\n(string) --\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'operation': {
        'id': 'string',
        'resourceName': 'string',
        'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
        'createdAt': datetime(2015, 1, 1),
        'location': {
            'availabilityZone': 'string',
            'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
        },
        'isTerminal': True|False,
        'operationDetails': 'string',
        'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
        'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
        'statusChangedAt': datetime(2015, 1, 1),
        'errorCode': 'string',
        'errorDetails': 'string'
    }
}


Response Structure

(dict) --

operation (dict) --
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

id (string) --
The ID of the operation.

resourceName (string) --
The resource name.

resourceType (string) --
The resource type.

createdAt (datetime) --
The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --
The AWS Region and Availability Zone.

availabilityZone (string) --
The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --
The AWS Region name.



isTerminal (boolean) --
A Boolean value indicating whether the operation is terminal.

operationDetails (string) --
Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --
The type of operation.

status (string) --
The status of the operation.

statusChangedAt (datetime) --
The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --
The error code.

errorDetails (string) --
The error details.









Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operation': {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        }
    }
    
    
    :returns: 
    Lightsail.Client.exceptions.ServiceException
    Lightsail.Client.exceptions.InvalidInputException
    Lightsail.Client.exceptions.NotFoundException
    Lightsail.Client.exceptions.OperationFailureException
    Lightsail.Client.exceptions.AccessDeniedException
    Lightsail.Client.exceptions.AccountSetupInProgressException
    Lightsail.Client.exceptions.UnauthenticatedException
    
    """
    pass

def create_instance_snapshot(instanceSnapshotName=None, instanceName=None, tags=None):
    """
    Creates a snapshot of a specific virtual private server, or instance . You can use a snapshot to create a new instance that is based on that snapshot.
    The create instance snapshot operation supports tag-based access control via request tags. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_instance_snapshot(
        instanceSnapshotName='string',
        instanceName='string',
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type instanceSnapshotName: string
    :param instanceSnapshotName: [REQUIRED]\nThe name for your new snapshot.\n

    :type instanceName: string
    :param instanceName: [REQUIRED]\nThe Lightsail instance on which to base your snapshot.\n

    :type tags: list
    :param tags: The tag keys and optional values to add to the resource during create.\nTo tag a resource after it has been created, see the tag resource operation.\n\n(dict) --Describes a tag key and optional value assigned to an Amazon Lightsail resource.\nFor more information about tags in Lightsail, see the Lightsail Dev Guide .\n\nkey (string) --The key of the tag.\nConstraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @\n\nvalue (string) --The value of the tag.\nConstraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'operations': [
        {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        },
    ]
}


Response Structure

(dict) --

operations (list) --
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

(dict) --
Describes the API operation.

id (string) --
The ID of the operation.

resourceName (string) --
The resource name.

resourceType (string) --
The resource type.

createdAt (datetime) --
The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --
The AWS Region and Availability Zone.

availabilityZone (string) --
The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --
The AWS Region name.



isTerminal (boolean) --
A Boolean value indicating whether the operation is terminal.

operationDetails (string) --
Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --
The type of operation.

status (string) --
The status of the operation.

statusChangedAt (datetime) --
The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --
The error code.

errorDetails (string) --
The error details.











Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    :returns: 
    Lightsail.Client.exceptions.ServiceException
    Lightsail.Client.exceptions.InvalidInputException
    Lightsail.Client.exceptions.NotFoundException
    Lightsail.Client.exceptions.OperationFailureException
    Lightsail.Client.exceptions.AccessDeniedException
    Lightsail.Client.exceptions.AccountSetupInProgressException
    Lightsail.Client.exceptions.UnauthenticatedException
    
    """
    pass

def create_instances(instanceNames=None, availabilityZone=None, customImageName=None, blueprintId=None, bundleId=None, userData=None, keyPairName=None, tags=None, addOns=None):
    """
    Creates one or more Amazon Lightsail instances.
    The create instances operation supports tag-based access control via request tags. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_instances(
        instanceNames=[
            'string',
        ],
        availabilityZone='string',
        customImageName='string',
        blueprintId='string',
        bundleId='string',
        userData='string',
        keyPairName='string',
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ],
        addOns=[
            {
                'addOnType': 'AutoSnapshot',
                'autoSnapshotAddOnRequest': {
                    'snapshotTimeOfDay': 'string'
                }
            },
        ]
    )
    
    
    :type instanceNames: list
    :param instanceNames: [REQUIRED]\nThe names to use for your new Lightsail instances. Separate multiple values using quotation marks and commas, for example: ['MyFirstInstance','MySecondInstance']\n\n(string) --\n\n

    :type availabilityZone: string
    :param availabilityZone: [REQUIRED]\nThe Availability Zone in which to create your instance. Use the following format: us-east-2a (case sensitive). You can get a list of Availability Zones by using the get regions operation. Be sure to add the include Availability Zones parameter to your request.\n

    :type customImageName: string
    :param customImageName: (Deprecated) The name for your custom image.\n\nNote\nIn releases prior to June 12, 2017, this parameter was ignored by the API. It is now deprecated.\n\n

    :type blueprintId: string
    :param blueprintId: [REQUIRED]\nThe ID for a virtual private server image (e.g., app_wordpress_4_4 or app_lamp_7_0 ). Use the get blueprints operation to return a list of available images (or blueprints ).\n\nNote\nUse active blueprints when creating new instances. Inactive blueprints are listed to support customers with existing instances and are not necessarily available to create new instances. Blueprints are marked inactive when they become outdated due to operating system updates or new application releases.\n\n

    :type bundleId: string
    :param bundleId: [REQUIRED]\nThe bundle of specification information for your virtual private server (or instance ), including the pricing plan (e.g., micro_1_0 ).\n

    :type userData: string
    :param userData: A launch script you can create that configures a server with additional user data. For example, you might want to run apt-get -y update .\n\nNote\nDepending on the machine image you choose, the command to get software on your instance varies. Amazon Linux and CentOS use yum , Debian and Ubuntu use apt-get , and FreeBSD uses pkg . For a complete list, see the Dev Guide .\n\n

    :type keyPairName: string
    :param keyPairName: The name of your key pair.

    :type tags: list
    :param tags: The tag keys and optional values to add to the resource during create.\nTo tag a resource after it has been created, see the tag resource operation.\n\n(dict) --Describes a tag key and optional value assigned to an Amazon Lightsail resource.\nFor more information about tags in Lightsail, see the Lightsail Dev Guide .\n\nkey (string) --The key of the tag.\nConstraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @\n\nvalue (string) --The value of the tag.\nConstraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @\n\n\n\n\n

    :type addOns: list
    :param addOns: An array of objects representing the add-ons to enable for the new instance.\n\n(dict) --Describes a request to enable, modify, or disable an add-on for an Amazon Lightsail resource.\n\nNote\nAn additional cost may be associated with enabling add-ons. For more information, see the Lightsail pricing page .\n\n\naddOnType (string) -- [REQUIRED]The add-on type.\n\nautoSnapshotAddOnRequest (dict) --An object that represents additional parameters when enabling or modifying the automatic snapshot add-on.\n\nsnapshotTimeOfDay (string) --The daily time when an automatic snapshot will be created.\nConstraints:\n\nMust be in HH:00 format, and in an hourly increment.\nSpecified in Coordinated Universal Time (UTC).\nThe snapshot will be automatically created between the time specified and up to 45 minutes after.\n\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'operations': [
        {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        },
    ]
}


Response Structure

(dict) --

operations (list) --
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

(dict) --
Describes the API operation.

id (string) --
The ID of the operation.

resourceName (string) --
The resource name.

resourceType (string) --
The resource type.

createdAt (datetime) --
The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --
The AWS Region and Availability Zone.

availabilityZone (string) --
The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --
The AWS Region name.



isTerminal (boolean) --
A Boolean value indicating whether the operation is terminal.

operationDetails (string) --
Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --
The type of operation.

status (string) --
The status of the operation.

statusChangedAt (datetime) --
The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --
The error code.

errorDetails (string) --
The error details.











Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    :returns: 
    Lightsail.Client.exceptions.ServiceException
    Lightsail.Client.exceptions.InvalidInputException
    Lightsail.Client.exceptions.NotFoundException
    Lightsail.Client.exceptions.OperationFailureException
    Lightsail.Client.exceptions.AccessDeniedException
    Lightsail.Client.exceptions.AccountSetupInProgressException
    Lightsail.Client.exceptions.UnauthenticatedException
    
    """
    pass

def create_instances_from_snapshot(instanceNames=None, attachedDiskMapping=None, availabilityZone=None, instanceSnapshotName=None, bundleId=None, userData=None, keyPairName=None, tags=None, addOns=None, sourceInstanceName=None, restoreDate=None, useLatestRestorableAutoSnapshot=None):
    """
    Creates one or more new instances from a manual or automatic snapshot of an instance.
    The create instances from snapshot operation supports tag-based access control via request tags and resource tags applied to the resource identified by instance snapshot name . For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_instances_from_snapshot(
        instanceNames=[
            'string',
        ],
        attachedDiskMapping={
            'string': [
                {
                    'originalDiskPath': 'string',
                    'newDiskName': 'string'
                },
            ]
        },
        availabilityZone='string',
        instanceSnapshotName='string',
        bundleId='string',
        userData='string',
        keyPairName='string',
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ],
        addOns=[
            {
                'addOnType': 'AutoSnapshot',
                'autoSnapshotAddOnRequest': {
                    'snapshotTimeOfDay': 'string'
                }
            },
        ],
        sourceInstanceName='string',
        restoreDate='string',
        useLatestRestorableAutoSnapshot=True|False
    )
    
    
    :type instanceNames: list
    :param instanceNames: [REQUIRED]\nThe names for your new instances.\n\n(string) --\n\n

    :type attachedDiskMapping: dict
    :param attachedDiskMapping: An object containing information about one or more disk mappings.\n\n(string) --\n(list) --\n(dict) --Describes a block storage disk mapping.\n\noriginalDiskPath (string) --The original disk path exposed to the instance (for example, /dev/sdh ).\n\nnewDiskName (string) --The new disk name (e.g., my-new-disk ).\n\n\n\n\n\n\n\n\n

    :type availabilityZone: string
    :param availabilityZone: [REQUIRED]\nThe Availability Zone where you want to create your instances. Use the following formatting: us-east-2a (case sensitive). You can get a list of Availability Zones by using the get regions operation. Be sure to add the include Availability Zones parameter to your request.\n

    :type instanceSnapshotName: string
    :param instanceSnapshotName: The name of the instance snapshot on which you are basing your new instances. Use the get instance snapshots operation to return information about your existing snapshots.\nConstraint:\n\nThis parameter cannot be defined together with the source instance name parameter. The instance snapshot name and source instance name parameters are mutually exclusive.\n\n

    :type bundleId: string
    :param bundleId: [REQUIRED]\nThe bundle of specification information for your virtual private server (or instance ), including the pricing plan (e.g., micro_1_0 ).\n

    :type userData: string
    :param userData: You can create a launch script that configures a server with additional user data. For example, apt-get -y update .\n\nNote\nDepending on the machine image you choose, the command to get software on your instance varies. Amazon Linux and CentOS use yum , Debian and Ubuntu use apt-get , and FreeBSD uses pkg . For a complete list, see the Dev Guide .\n\n

    :type keyPairName: string
    :param keyPairName: The name for your key pair.

    :type tags: list
    :param tags: The tag keys and optional values to add to the resource during create.\nTo tag a resource after it has been created, see the tag resource operation.\n\n(dict) --Describes a tag key and optional value assigned to an Amazon Lightsail resource.\nFor more information about tags in Lightsail, see the Lightsail Dev Guide .\n\nkey (string) --The key of the tag.\nConstraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @\n\nvalue (string) --The value of the tag.\nConstraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @\n\n\n\n\n

    :type addOns: list
    :param addOns: An array of objects representing the add-ons to enable for the new instance.\n\n(dict) --Describes a request to enable, modify, or disable an add-on for an Amazon Lightsail resource.\n\nNote\nAn additional cost may be associated with enabling add-ons. For more information, see the Lightsail pricing page .\n\n\naddOnType (string) -- [REQUIRED]The add-on type.\n\nautoSnapshotAddOnRequest (dict) --An object that represents additional parameters when enabling or modifying the automatic snapshot add-on.\n\nsnapshotTimeOfDay (string) --The daily time when an automatic snapshot will be created.\nConstraints:\n\nMust be in HH:00 format, and in an hourly increment.\nSpecified in Coordinated Universal Time (UTC).\nThe snapshot will be automatically created between the time specified and up to 45 minutes after.\n\n\n\n\n\n\n\n

    :type sourceInstanceName: string
    :param sourceInstanceName: The name of the source instance from which the source automatic snapshot was created.\nConstraints:\n\nThis parameter cannot be defined together with the instance snapshot name parameter. The source instance name and instance snapshot name parameters are mutually exclusive.\nDefine this parameter only when creating a new instance from an automatic snapshot. For more information, see the Lightsail Dev Guide .\n\n

    :type restoreDate: string
    :param restoreDate: The date of the automatic snapshot to use for the new instance. Use the get auto snapshots operation to identify the dates of the available automatic snapshots.\nConstraints:\n\nMust be specified in YYYY-MM-DD format.\nThis parameter cannot be defined together with the use latest restorable auto snapshot parameter. The restore date and use latest restorable auto snapshot parameters are mutually exclusive.\nDefine this parameter only when creating a new instance from an automatic snapshot. For more information, see the Lightsail Dev Guide .\n\n

    :type useLatestRestorableAutoSnapshot: boolean
    :param useLatestRestorableAutoSnapshot: A Boolean value to indicate whether to use the latest available automatic snapshot.\nConstraints:\n\nThis parameter cannot be defined together with the restore date parameter. The use latest restorable auto snapshot and restore date parameters are mutually exclusive.\nDefine this parameter only when creating a new instance from an automatic snapshot. For more information, see the Lightsail Dev Guide .\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'operations': [
        {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        },
    ]
}


Response Structure

(dict) --

operations (list) --
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

(dict) --
Describes the API operation.

id (string) --
The ID of the operation.

resourceName (string) --
The resource name.

resourceType (string) --
The resource type.

createdAt (datetime) --
The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --
The AWS Region and Availability Zone.

availabilityZone (string) --
The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --
The AWS Region name.



isTerminal (boolean) --
A Boolean value indicating whether the operation is terminal.

operationDetails (string) --
Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --
The type of operation.

status (string) --
The status of the operation.

statusChangedAt (datetime) --
The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --
The error code.

errorDetails (string) --
The error details.











Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    :returns: 
    Lightsail.Client.exceptions.ServiceException
    Lightsail.Client.exceptions.InvalidInputException
    Lightsail.Client.exceptions.NotFoundException
    Lightsail.Client.exceptions.OperationFailureException
    Lightsail.Client.exceptions.AccessDeniedException
    Lightsail.Client.exceptions.AccountSetupInProgressException
    Lightsail.Client.exceptions.UnauthenticatedException
    
    """
    pass

def create_key_pair(keyPairName=None, tags=None):
    """
    Creates an SSH key pair.
    The create key pair operation supports tag-based access control via request tags. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_key_pair(
        keyPairName='string',
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type keyPairName: string
    :param keyPairName: [REQUIRED]\nThe name for your new key pair.\n

    :type tags: list
    :param tags: The tag keys and optional values to add to the resource during create.\nTo tag a resource after it has been created, see the tag resource operation.\n\n(dict) --Describes a tag key and optional value assigned to an Amazon Lightsail resource.\nFor more information about tags in Lightsail, see the Lightsail Dev Guide .\n\nkey (string) --The key of the tag.\nConstraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @\n\nvalue (string) --The value of the tag.\nConstraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'keyPair': {
        'name': 'string',
        'arn': 'string',
        'supportCode': 'string',
        'createdAt': datetime(2015, 1, 1),
        'location': {
            'availabilityZone': 'string',
            'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
        },
        'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
        'tags': [
            {
                'key': 'string',
                'value': 'string'
            },
        ],
        'fingerprint': 'string'
    },
    'publicKeyBase64': 'string',
    'privateKeyBase64': 'string',
    'operation': {
        'id': 'string',
        'resourceName': 'string',
        'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
        'createdAt': datetime(2015, 1, 1),
        'location': {
            'availabilityZone': 'string',
            'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
        },
        'isTerminal': True|False,
        'operationDetails': 'string',
        'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
        'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
        'statusChangedAt': datetime(2015, 1, 1),
        'errorCode': 'string',
        'errorDetails': 'string'
    }
}


Response Structure

(dict) --

keyPair (dict) --
An array of key-value pairs containing information about the new key pair you just created.

name (string) --
The friendly name of the SSH key pair.

arn (string) --
The Amazon Resource Name (ARN) of the key pair (e.g., arn:aws:lightsail:us-east-2:123456789101:KeyPair/05859e3d-331d-48ba-9034-12345EXAMPLE ).

supportCode (string) --
The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.

createdAt (datetime) --
The timestamp when the key pair was created (e.g., 1479816991.349 ).

location (dict) --
The region name and Availability Zone where the key pair was created.

availabilityZone (string) --
The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --
The AWS Region name.



resourceType (string) --
The resource type (usually KeyPair ).

tags (list) --
The tag keys and optional values for the resource. For more information about tags in Lightsail, see the Lightsail Dev Guide .

(dict) --
Describes a tag key and optional value assigned to an Amazon Lightsail resource.
For more information about tags in Lightsail, see the Lightsail Dev Guide .

key (string) --
The key of the tag.
Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @

value (string) --
The value of the tag.
Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @





fingerprint (string) --
The RSA fingerprint of the key pair.



publicKeyBase64 (string) --
A base64-encoded public key of the ssh-rsa type.

privateKeyBase64 (string) --
A base64-encoded RSA private key.

operation (dict) --
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

id (string) --
The ID of the operation.

resourceName (string) --
The resource name.

resourceType (string) --
The resource type.

createdAt (datetime) --
The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --
The AWS Region and Availability Zone.

availabilityZone (string) --
The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --
The AWS Region name.



isTerminal (boolean) --
A Boolean value indicating whether the operation is terminal.

operationDetails (string) --
Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --
The type of operation.

status (string) --
The status of the operation.

statusChangedAt (datetime) --
The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --
The error code.

errorDetails (string) --
The error details.









Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'keyPair': {
            'name': 'string',
            'arn': 'string',
            'supportCode': 'string',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ],
            'fingerprint': 'string'
        },
        'publicKeyBase64': 'string',
        'privateKeyBase64': 'string',
        'operation': {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        }
    }
    
    
    :returns: 
    Lightsail.Client.exceptions.ServiceException
    Lightsail.Client.exceptions.InvalidInputException
    Lightsail.Client.exceptions.NotFoundException
    Lightsail.Client.exceptions.OperationFailureException
    Lightsail.Client.exceptions.AccessDeniedException
    Lightsail.Client.exceptions.AccountSetupInProgressException
    Lightsail.Client.exceptions.UnauthenticatedException
    
    """
    pass

def create_load_balancer(loadBalancerName=None, instancePort=None, healthCheckPath=None, certificateName=None, certificateDomainName=None, certificateAlternativeNames=None, tags=None):
    """
    Creates a Lightsail load balancer. To learn more about deciding whether to load balance your application, see Configure your Lightsail instances for load balancing . You can create up to 5 load balancers per AWS Region in your account.
    When you create a load balancer, you can specify a unique name and port settings. To change additional load balancer settings, use the UpdateLoadBalancerAttribute operation.
    The create load balancer operation supports tag-based access control via request tags. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_load_balancer(
        loadBalancerName='string',
        instancePort=123,
        healthCheckPath='string',
        certificateName='string',
        certificateDomainName='string',
        certificateAlternativeNames=[
            'string',
        ],
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type loadBalancerName: string
    :param loadBalancerName: [REQUIRED]\nThe name of your load balancer.\n

    :type instancePort: integer
    :param instancePort: [REQUIRED]\nThe instance port where you\'re creating your load balancer.\n

    :type healthCheckPath: string
    :param healthCheckPath: The path you provided to perform the load balancer health check. If you didn\'t specify a health check path, Lightsail uses the root path of your website (e.g., '/' ).\nYou may want to specify a custom health check path other than the root of your application if your home page loads slowly or has a lot of media or scripting on it.\n

    :type certificateName: string
    :param certificateName: The name of the SSL/TLS certificate.\nIf you specify certificateName , then certificateDomainName is required (and vice-versa).\n

    :type certificateDomainName: string
    :param certificateDomainName: The domain name with which your certificate is associated (e.g., example.com ).\nIf you specify certificateDomainName , then certificateName is required (and vice-versa).\n

    :type certificateAlternativeNames: list
    :param certificateAlternativeNames: The optional alternative domains and subdomains to use with your SSL/TLS certificate (e.g., www.example.com , example.com , m.example.com , blog.example.com ).\n\n(string) --\n\n

    :type tags: list
    :param tags: The tag keys and optional values to add to the resource during create.\nTo tag a resource after it has been created, see the tag resource operation.\n\n(dict) --Describes a tag key and optional value assigned to an Amazon Lightsail resource.\nFor more information about tags in Lightsail, see the Lightsail Dev Guide .\n\nkey (string) --The key of the tag.\nConstraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @\n\nvalue (string) --The value of the tag.\nConstraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'operations': [
        {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        },
    ]
}


Response Structure

(dict) --

operations (list) --
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

(dict) --
Describes the API operation.

id (string) --
The ID of the operation.

resourceName (string) --
The resource name.

resourceType (string) --
The resource type.

createdAt (datetime) --
The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --
The AWS Region and Availability Zone.

availabilityZone (string) --
The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --
The AWS Region name.



isTerminal (boolean) --
A Boolean value indicating whether the operation is terminal.

operationDetails (string) --
Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --
The type of operation.

status (string) --
The status of the operation.

statusChangedAt (datetime) --
The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --
The error code.

errorDetails (string) --
The error details.











Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    :returns: 
    Lightsail.Client.exceptions.ServiceException
    Lightsail.Client.exceptions.InvalidInputException
    Lightsail.Client.exceptions.NotFoundException
    Lightsail.Client.exceptions.OperationFailureException
    Lightsail.Client.exceptions.AccessDeniedException
    Lightsail.Client.exceptions.AccountSetupInProgressException
    Lightsail.Client.exceptions.UnauthenticatedException
    
    """
    pass

def create_load_balancer_tls_certificate(loadBalancerName=None, certificateName=None, certificateDomainName=None, certificateAlternativeNames=None, tags=None):
    """
    Creates a Lightsail load balancer TLS certificate.
    TLS is just an updated, more secure version of Secure Socket Layer (SSL).
    The CreateLoadBalancerTlsCertificate operation supports tag-based access control via resource tags applied to the resource identified by load balancer name . For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_load_balancer_tls_certificate(
        loadBalancerName='string',
        certificateName='string',
        certificateDomainName='string',
        certificateAlternativeNames=[
            'string',
        ],
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type loadBalancerName: string
    :param loadBalancerName: [REQUIRED]\nThe load balancer name where you want to create the SSL/TLS certificate.\n

    :type certificateName: string
    :param certificateName: [REQUIRED]\nThe SSL/TLS certificate name.\nYou can have up to 10 certificates in your account at one time. Each Lightsail load balancer can have up to 2 certificates associated with it at one time. There is also an overall limit to the number of certificates that can be issue in a 365-day period. For more information, see Limits .\n

    :type certificateDomainName: string
    :param certificateDomainName: [REQUIRED]\nThe domain name (e.g., example.com ) for your SSL/TLS certificate.\n

    :type certificateAlternativeNames: list
    :param certificateAlternativeNames: An array of strings listing alternative domains and subdomains for your SSL/TLS certificate. Lightsail will de-dupe the names for you. You can have a maximum of 9 alternative names (in addition to the 1 primary domain). We do not support wildcards (e.g., *.example.com ).\n\n(string) --\n\n

    :type tags: list
    :param tags: The tag keys and optional values to add to the resource during create.\nTo tag a resource after it has been created, see the tag resource operation.\n\n(dict) --Describes a tag key and optional value assigned to an Amazon Lightsail resource.\nFor more information about tags in Lightsail, see the Lightsail Dev Guide .\n\nkey (string) --The key of the tag.\nConstraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @\n\nvalue (string) --The value of the tag.\nConstraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'operations': [
        {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        },
    ]
}


Response Structure

(dict) --

operations (list) --
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

(dict) --
Describes the API operation.

id (string) --
The ID of the operation.

resourceName (string) --
The resource name.

resourceType (string) --
The resource type.

createdAt (datetime) --
The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --
The AWS Region and Availability Zone.

availabilityZone (string) --
The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --
The AWS Region name.



isTerminal (boolean) --
A Boolean value indicating whether the operation is terminal.

operationDetails (string) --
Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --
The type of operation.

status (string) --
The status of the operation.

statusChangedAt (datetime) --
The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --
The error code.

errorDetails (string) --
The error details.











Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    :returns: 
    Lightsail.Client.exceptions.ServiceException
    Lightsail.Client.exceptions.InvalidInputException
    Lightsail.Client.exceptions.NotFoundException
    Lightsail.Client.exceptions.OperationFailureException
    Lightsail.Client.exceptions.AccessDeniedException
    Lightsail.Client.exceptions.AccountSetupInProgressException
    Lightsail.Client.exceptions.UnauthenticatedException
    
    """
    pass

def create_relational_database(relationalDatabaseName=None, availabilityZone=None, relationalDatabaseBlueprintId=None, relationalDatabaseBundleId=None, masterDatabaseName=None, masterUsername=None, masterUserPassword=None, preferredBackupWindow=None, preferredMaintenanceWindow=None, publiclyAccessible=None, tags=None):
    """
    Creates a new database in Amazon Lightsail.
    The create relational database operation supports tag-based access control via request tags. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_relational_database(
        relationalDatabaseName='string',
        availabilityZone='string',
        relationalDatabaseBlueprintId='string',
        relationalDatabaseBundleId='string',
        masterDatabaseName='string',
        masterUsername='string',
        masterUserPassword='string',
        preferredBackupWindow='string',
        preferredMaintenanceWindow='string',
        publiclyAccessible=True|False,
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type relationalDatabaseName: string
    :param relationalDatabaseName: [REQUIRED]\nThe name to use for your new database.\nConstraints:\n\nMust contain from 2 to 255 alphanumeric characters, or hyphens.\nThe first and last character must be a letter or number.\n\n

    :type availabilityZone: string
    :param availabilityZone: The Availability Zone in which to create your new database. Use the us-east-2a case-sensitive format.\nYou can get a list of Availability Zones by using the get regions operation. Be sure to add the include relational database Availability Zones parameter to your request.\n

    :type relationalDatabaseBlueprintId: string
    :param relationalDatabaseBlueprintId: [REQUIRED]\nThe blueprint ID for your new database. A blueprint describes the major engine version of a database.\nYou can get a list of database blueprints IDs by using the get relational database blueprints operation.\n

    :type relationalDatabaseBundleId: string
    :param relationalDatabaseBundleId: [REQUIRED]\nThe bundle ID for your new database. A bundle describes the performance specifications for your database.\nYou can get a list of database bundle IDs by using the get relational database bundles operation.\n

    :type masterDatabaseName: string
    :param masterDatabaseName: [REQUIRED]\nThe name of the master database created when the Lightsail database resource is created.\nConstraints:\n\nMust contain from 1 to 64 alphanumeric characters.\nCannot be a word reserved by the specified database engine\n\n

    :type masterUsername: string
    :param masterUsername: [REQUIRED]\nThe master user name for your new database.\nConstraints:\n\nMaster user name is required.\nMust contain from 1 to 16 alphanumeric characters.\nThe first character must be a letter.\nCannot be a reserved word for the database engine you choose. For more information about reserved words in MySQL 5.6 or 5.7, see the Keywords and Reserved Words articles for MySQL 5.6 or MySQL 5.7 respectively.\n\n

    :type masterUserPassword: string
    :param masterUserPassword: The password for the master user of your new database. The password can include any printable ASCII character except '/', ''', or '@'.\nConstraints: Must contain 8 to 41 characters.\n

    :type preferredBackupWindow: string
    :param preferredBackupWindow: The daily time range during which automated backups are created for your new database if automated backups are enabled.\nThe default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region. For more information about the preferred backup window time blocks for each region, see the Working With Backups guide in the Amazon Relational Database Service (Amazon RDS) documentation.\nConstraints:\n\nMust be in the hh24:mi-hh24:mi format. Example: 16:00-16:30\nSpecified in Coordinated Universal Time (UTC).\nMust not conflict with the preferred maintenance window.\nMust be at least 30 minutes.\n\n

    :type preferredMaintenanceWindow: string
    :param preferredMaintenanceWindow: The weekly time range during which system maintenance can occur on your new database.\nThe default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week.\nConstraints:\n\nMust be in the ddd:hh24:mi-ddd:hh24:mi format.\nValid days: Mon, Tue, Wed, Thu, Fri, Sat, Sun.\nMust be at least 30 minutes.\nSpecified in Coordinated Universal Time (UTC).\nExample: Tue:17:00-Tue:17:30\n\n

    :type publiclyAccessible: boolean
    :param publiclyAccessible: Specifies the accessibility options for your new database. A value of true specifies a database that is available to resources outside of your Lightsail account. A value of false specifies a database that is available only to your Lightsail resources in the same region as your database.

    :type tags: list
    :param tags: The tag keys and optional values to add to the resource during create.\nTo tag a resource after it has been created, see the tag resource operation.\n\n(dict) --Describes a tag key and optional value assigned to an Amazon Lightsail resource.\nFor more information about tags in Lightsail, see the Lightsail Dev Guide .\n\nkey (string) --The key of the tag.\nConstraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @\n\nvalue (string) --The value of the tag.\nConstraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'operations': [
        {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        },
    ]
}


Response Structure

(dict) --

operations (list) --
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

(dict) --
Describes the API operation.

id (string) --
The ID of the operation.

resourceName (string) --
The resource name.

resourceType (string) --
The resource type.

createdAt (datetime) --
The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --
The AWS Region and Availability Zone.

availabilityZone (string) --
The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --
The AWS Region name.



isTerminal (boolean) --
A Boolean value indicating whether the operation is terminal.

operationDetails (string) --
Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --
The type of operation.

status (string) --
The status of the operation.

statusChangedAt (datetime) --
The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --
The error code.

errorDetails (string) --
The error details.











Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    :returns: 
    Lightsail.Client.exceptions.ServiceException
    Lightsail.Client.exceptions.InvalidInputException
    Lightsail.Client.exceptions.NotFoundException
    Lightsail.Client.exceptions.OperationFailureException
    Lightsail.Client.exceptions.AccessDeniedException
    Lightsail.Client.exceptions.AccountSetupInProgressException
    Lightsail.Client.exceptions.UnauthenticatedException
    
    """
    pass

def create_relational_database_from_snapshot(relationalDatabaseName=None, availabilityZone=None, publiclyAccessible=None, relationalDatabaseSnapshotName=None, relationalDatabaseBundleId=None, sourceRelationalDatabaseName=None, restoreTime=None, useLatestRestorableTime=None, tags=None):
    """
    Creates a new database from an existing database snapshot in Amazon Lightsail.
    You can create a new database from a snapshot in if something goes wrong with your original database, or to change it to a different plan, such as a high availability or standard plan.
    The create relational database from snapshot operation supports tag-based access control via request tags and resource tags applied to the resource identified by relationalDatabaseSnapshotName. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_relational_database_from_snapshot(
        relationalDatabaseName='string',
        availabilityZone='string',
        publiclyAccessible=True|False,
        relationalDatabaseSnapshotName='string',
        relationalDatabaseBundleId='string',
        sourceRelationalDatabaseName='string',
        restoreTime=datetime(2015, 1, 1),
        useLatestRestorableTime=True|False,
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type relationalDatabaseName: string
    :param relationalDatabaseName: [REQUIRED]\nThe name to use for your new database.\nConstraints:\n\nMust contain from 2 to 255 alphanumeric characters, or hyphens.\nThe first and last character must be a letter or number.\n\n

    :type availabilityZone: string
    :param availabilityZone: The Availability Zone in which to create your new database. Use the us-east-2a case-sensitive format.\nYou can get a list of Availability Zones by using the get regions operation. Be sure to add the include relational database Availability Zones parameter to your request.\n

    :type publiclyAccessible: boolean
    :param publiclyAccessible: Specifies the accessibility options for your new database. A value of true specifies a database that is available to resources outside of your Lightsail account. A value of false specifies a database that is available only to your Lightsail resources in the same region as your database.

    :type relationalDatabaseSnapshotName: string
    :param relationalDatabaseSnapshotName: The name of the database snapshot from which to create your new database.

    :type relationalDatabaseBundleId: string
    :param relationalDatabaseBundleId: The bundle ID for your new database. A bundle describes the performance specifications for your database.\nYou can get a list of database bundle IDs by using the get relational database bundles operation.\nWhen creating a new database from a snapshot, you cannot choose a bundle that is smaller than the bundle of the source database.\n

    :type sourceRelationalDatabaseName: string
    :param sourceRelationalDatabaseName: The name of the source database.

    :type restoreTime: datetime
    :param restoreTime: The date and time to restore your database from.\nConstraints:\n\nMust be before the latest restorable time for the database.\nCannot be specified if the use latest restorable time parameter is true .\nSpecified in Coordinated Universal Time (UTC).\nSpecified in the Unix time format. For example, if you wish to use a restore time of October 1, 2018, at 8 PM UTC, then you input 1538424000 as the restore time.\n\n

    :type useLatestRestorableTime: boolean
    :param useLatestRestorableTime: Specifies whether your database is restored from the latest backup time. A value of true restores from the latest backup time.\nDefault: false\nConstraints: Cannot be specified if the restore time parameter is provided.\n

    :type tags: list
    :param tags: The tag keys and optional values to add to the resource during create.\nTo tag a resource after it has been created, see the tag resource operation.\n\n(dict) --Describes a tag key and optional value assigned to an Amazon Lightsail resource.\nFor more information about tags in Lightsail, see the Lightsail Dev Guide .\n\nkey (string) --The key of the tag.\nConstraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @\n\nvalue (string) --The value of the tag.\nConstraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'operations': [
        {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        },
    ]
}


Response Structure

(dict) --

operations (list) --
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

(dict) --
Describes the API operation.

id (string) --
The ID of the operation.

resourceName (string) --
The resource name.

resourceType (string) --
The resource type.

createdAt (datetime) --
The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --
The AWS Region and Availability Zone.

availabilityZone (string) --
The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --
The AWS Region name.



isTerminal (boolean) --
A Boolean value indicating whether the operation is terminal.

operationDetails (string) --
Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --
The type of operation.

status (string) --
The status of the operation.

statusChangedAt (datetime) --
The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --
The error code.

errorDetails (string) --
The error details.











Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    :returns: 
    Lightsail.Client.exceptions.ServiceException
    Lightsail.Client.exceptions.InvalidInputException
    Lightsail.Client.exceptions.NotFoundException
    Lightsail.Client.exceptions.OperationFailureException
    Lightsail.Client.exceptions.AccessDeniedException
    Lightsail.Client.exceptions.AccountSetupInProgressException
    Lightsail.Client.exceptions.UnauthenticatedException
    
    """
    pass

def create_relational_database_snapshot(relationalDatabaseName=None, relationalDatabaseSnapshotName=None, tags=None):
    """
    Creates a snapshot of your database in Amazon Lightsail. You can use snapshots for backups, to make copies of a database, and to save data before deleting a database.
    The create relational database snapshot operation supports tag-based access control via request tags. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_relational_database_snapshot(
        relationalDatabaseName='string',
        relationalDatabaseSnapshotName='string',
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type relationalDatabaseName: string
    :param relationalDatabaseName: [REQUIRED]\nThe name of the database on which to base your new snapshot.\n

    :type relationalDatabaseSnapshotName: string
    :param relationalDatabaseSnapshotName: [REQUIRED]\nThe name for your new database snapshot.\nConstraints:\n\nMust contain from 2 to 255 alphanumeric characters, or hyphens.\nThe first and last character must be a letter or number.\n\n

    :type tags: list
    :param tags: The tag keys and optional values to add to the resource during create.\nTo tag a resource after it has been created, see the tag resource operation.\n\n(dict) --Describes a tag key and optional value assigned to an Amazon Lightsail resource.\nFor more information about tags in Lightsail, see the Lightsail Dev Guide .\n\nkey (string) --The key of the tag.\nConstraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @\n\nvalue (string) --The value of the tag.\nConstraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'operations': [
        {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        },
    ]
}


Response Structure

(dict) --

operations (list) --
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

(dict) --
Describes the API operation.

id (string) --
The ID of the operation.

resourceName (string) --
The resource name.

resourceType (string) --
The resource type.

createdAt (datetime) --
The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --
The AWS Region and Availability Zone.

availabilityZone (string) --
The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --
The AWS Region name.



isTerminal (boolean) --
A Boolean value indicating whether the operation is terminal.

operationDetails (string) --
Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --
The type of operation.

status (string) --
The status of the operation.

statusChangedAt (datetime) --
The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --
The error code.

errorDetails (string) --
The error details.











Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    :returns: 
    Lightsail.Client.exceptions.ServiceException
    Lightsail.Client.exceptions.InvalidInputException
    Lightsail.Client.exceptions.NotFoundException
    Lightsail.Client.exceptions.OperationFailureException
    Lightsail.Client.exceptions.AccessDeniedException
    Lightsail.Client.exceptions.AccountSetupInProgressException
    Lightsail.Client.exceptions.UnauthenticatedException
    
    """
    pass

def delete_alarm(alarmName=None):
    """
    Deletes an alarm.
    An alarm is used to monitor a single metric for one of your resources. When a metric condition is met, the alarm can notify you by email, SMS text message, and a banner displayed on the Amazon Lightsail console. For more information, see Alarms in Amazon Lightsail .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_alarm(
        alarmName='string'
    )
    
    
    :type alarmName: string
    :param alarmName: [REQUIRED]\nThe name of the alarm to delete.\n

    :rtype: dict
ReturnsResponse Syntax{
    'operations': [
        {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        },
    ]
}


Response Structure

(dict) --
operations (list) --An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

(dict) --Describes the API operation.

id (string) --The ID of the operation.

resourceName (string) --The resource name.

resourceType (string) --The resource type.

createdAt (datetime) --The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --The AWS Region and Availability Zone.

availabilityZone (string) --The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --The AWS Region name.



isTerminal (boolean) --A Boolean value indicating whether the operation is terminal.

operationDetails (string) --Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --The type of operation.

status (string) --The status of the operation.

statusChangedAt (datetime) --The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --The error code.

errorDetails (string) --The error details.










Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.UnauthenticatedException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.NotFoundException


    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def delete_auto_snapshot(resourceName=None, date=None):
    """
    Deletes an automatic snapshot of an instance or disk. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_auto_snapshot(
        resourceName='string',
        date='string'
    )
    
    
    :type resourceName: string
    :param resourceName: [REQUIRED]\nThe name of the source instance or disk from which to delete the automatic snapshot.\n

    :type date: string
    :param date: [REQUIRED]\nThe date of the automatic snapshot to delete in YYYY-MM-DD format. Use the get auto snapshots operation to get the available automatic snapshots for a resource.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'operations': [
        {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        },
    ]
}


Response Structure

(dict) --

operations (list) --
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

(dict) --
Describes the API operation.

id (string) --
The ID of the operation.

resourceName (string) --
The resource name.

resourceType (string) --
The resource type.

createdAt (datetime) --
The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --
The AWS Region and Availability Zone.

availabilityZone (string) --
The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --
The AWS Region name.



isTerminal (boolean) --
A Boolean value indicating whether the operation is terminal.

operationDetails (string) --
Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --
The type of operation.

status (string) --
The status of the operation.

statusChangedAt (datetime) --
The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --
The error code.

errorDetails (string) --
The error details.











Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    :returns: 
    Lightsail.Client.exceptions.ServiceException
    Lightsail.Client.exceptions.InvalidInputException
    Lightsail.Client.exceptions.NotFoundException
    Lightsail.Client.exceptions.OperationFailureException
    Lightsail.Client.exceptions.AccessDeniedException
    Lightsail.Client.exceptions.UnauthenticatedException
    
    """
    pass

def delete_contact_method(protocol=None):
    """
    Deletes a contact method.
    A contact method is used to send you notifications about your Amazon Lightsail resources. You can add one email address and one mobile phone number contact method in each AWS Region. However, SMS text messaging is not supported in some AWS Regions, and SMS text messages cannot be sent to some countries/regions. For more information, see Notifications in Amazon Lightsail .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_contact_method(
        protocol='Email'|'SMS'
    )
    
    
    :type protocol: string
    :param protocol: [REQUIRED]\nThe protocol that will be deleted, such as Email or SMS (text messaging).\n\nNote\nTo delete an Email and an SMS contact method if you added both, you must run separate DeleteContactMethod actions to delete each protocol.\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'operations': [
        {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        },
    ]
}


Response Structure

(dict) --
operations (list) --An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

(dict) --Describes the API operation.

id (string) --The ID of the operation.

resourceName (string) --The resource name.

resourceType (string) --The resource type.

createdAt (datetime) --The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --The AWS Region and Availability Zone.

availabilityZone (string) --The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --The AWS Region name.



isTerminal (boolean) --A Boolean value indicating whether the operation is terminal.

operationDetails (string) --Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --The type of operation.

status (string) --The status of the operation.

statusChangedAt (datetime) --The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --The error code.

errorDetails (string) --The error details.










Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.UnauthenticatedException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.NotFoundException


    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def delete_disk(diskName=None, forceDeleteAddOns=None):
    """
    Deletes the specified block storage disk. The disk must be in the available state (not attached to a Lightsail instance).
    The delete disk operation supports tag-based access control via resource tags applied to the resource identified by disk name . For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_disk(
        diskName='string',
        forceDeleteAddOns=True|False
    )
    
    
    :type diskName: string
    :param diskName: [REQUIRED]\nThe unique name of the disk you want to delete (e.g., my-disk ).\n

    :type forceDeleteAddOns: boolean
    :param forceDeleteAddOns: A Boolean value to indicate whether to delete the enabled add-ons for the disk.

    :rtype: dict

ReturnsResponse Syntax
{
    'operations': [
        {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        },
    ]
}


Response Structure

(dict) --

operations (list) --
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

(dict) --
Describes the API operation.

id (string) --
The ID of the operation.

resourceName (string) --
The resource name.

resourceType (string) --
The resource type.

createdAt (datetime) --
The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --
The AWS Region and Availability Zone.

availabilityZone (string) --
The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --
The AWS Region name.



isTerminal (boolean) --
A Boolean value indicating whether the operation is terminal.

operationDetails (string) --
Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --
The type of operation.

status (string) --
The status of the operation.

statusChangedAt (datetime) --
The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --
The error code.

errorDetails (string) --
The error details.











Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    :returns: 
    Lightsail.Client.exceptions.ServiceException
    Lightsail.Client.exceptions.InvalidInputException
    Lightsail.Client.exceptions.NotFoundException
    Lightsail.Client.exceptions.OperationFailureException
    Lightsail.Client.exceptions.AccessDeniedException
    Lightsail.Client.exceptions.AccountSetupInProgressException
    Lightsail.Client.exceptions.UnauthenticatedException
    
    """
    pass

def delete_disk_snapshot(diskSnapshotName=None):
    """
    Deletes the specified disk snapshot.
    When you make periodic snapshots of a disk, the snapshots are incremental, and only the blocks on the device that have changed since your last snapshot are saved in the new snapshot. When you delete a snapshot, only the data not needed for any other snapshot is removed. So regardless of which prior snapshots have been deleted, all active snapshots will have access to all the information needed to restore the disk.
    The delete disk snapshot operation supports tag-based access control via resource tags applied to the resource identified by disk snapshot name . For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_disk_snapshot(
        diskSnapshotName='string'
    )
    
    
    :type diskSnapshotName: string
    :param diskSnapshotName: [REQUIRED]\nThe name of the disk snapshot you want to delete (e.g., my-disk-snapshot ).\n

    :rtype: dict
ReturnsResponse Syntax{
    'operations': [
        {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        },
    ]
}


Response Structure

(dict) --
operations (list) --An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

(dict) --Describes the API operation.

id (string) --The ID of the operation.

resourceName (string) --The resource name.

resourceType (string) --The resource type.

createdAt (datetime) --The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --The AWS Region and Availability Zone.

availabilityZone (string) --The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --The AWS Region name.



isTerminal (boolean) --A Boolean value indicating whether the operation is terminal.

operationDetails (string) --Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --The type of operation.

status (string) --The status of the operation.

statusChangedAt (datetime) --The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --The error code.

errorDetails (string) --The error details.










Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def delete_domain(domainName=None):
    """
    Deletes the specified domain recordset and all of its domain records.
    The delete domain operation supports tag-based access control via resource tags applied to the resource identified by domain name . For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_domain(
        domainName='string'
    )
    
    
    :type domainName: string
    :param domainName: [REQUIRED]\nThe specific domain name to delete.\n

    :rtype: dict
ReturnsResponse Syntax{
    'operation': {
        'id': 'string',
        'resourceName': 'string',
        'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
        'createdAt': datetime(2015, 1, 1),
        'location': {
            'availabilityZone': 'string',
            'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
        },
        'isTerminal': True|False,
        'operationDetails': 'string',
        'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
        'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
        'statusChangedAt': datetime(2015, 1, 1),
        'errorCode': 'string',
        'errorDetails': 'string'
    }
}


Response Structure

(dict) --
operation (dict) --An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

id (string) --The ID of the operation.

resourceName (string) --The resource name.

resourceType (string) --The resource type.

createdAt (datetime) --The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --The AWS Region and Availability Zone.

availabilityZone (string) --The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --The AWS Region name.



isTerminal (boolean) --A Boolean value indicating whether the operation is terminal.

operationDetails (string) --Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --The type of operation.

status (string) --The status of the operation.

statusChangedAt (datetime) --The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --The error code.

errorDetails (string) --The error details.








Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operation': {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
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
    The delete domain entry operation supports tag-based access control via resource tags applied to the resource identified by domain name . For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_domain_entry(
        domainName='string',
        domainEntry={
            'id': 'string',
            'name': 'string',
            'target': 'string',
            'isAlias': True|False,
            'type': 'string',
            'options': {
                'string': 'string'
            }
        }
    )
    
    
    :type domainName: string
    :param domainName: [REQUIRED]\nThe name of the domain entry to delete.\n

    :type domainEntry: dict
    :param domainEntry: [REQUIRED]\nAn array of key-value pairs containing information about your domain entries.\n\nid (string) --The ID of the domain recordset entry.\n\nname (string) --The name of the domain.\n\ntarget (string) --The target AWS name server (e.g., ns-111.awsdns-22.com. ).\nFor Lightsail load balancers, the value looks like ab1234c56789c6b86aba6fb203d443bc-123456789.us-east-2.elb.amazonaws.com . Be sure to also set isAlias to true when setting up an A record for a load balancer.\n\nisAlias (boolean) --When true , specifies whether the domain entry is an alias used by the Lightsail load balancer. You can include an alias (A type) record in your request, which points to a load balancer DNS name and routes traffic to your load balancer\n\ntype (string) --The type of domain entry, such as address (A), canonical name (CNAME), mail exchanger (MX), name server (NS), start of authority (SOA), service locator (SRV), or text (TXT).\nThe following domain entry types can be used:\n\nA\nCNAME\nMX\nNS\nSOA\nSRV\nTXT\n\n\noptions (dict) --(Deprecated) The options for the domain entry.\n\nNote\nIn releases prior to November 29, 2017, this parameter was not included in the API response. It is now deprecated.\n\n\n(string) --\n(string) --\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'operation': {
        'id': 'string',
        'resourceName': 'string',
        'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
        'createdAt': datetime(2015, 1, 1),
        'location': {
            'availabilityZone': 'string',
            'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
        },
        'isTerminal': True|False,
        'operationDetails': 'string',
        'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
        'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
        'statusChangedAt': datetime(2015, 1, 1),
        'errorCode': 'string',
        'errorDetails': 'string'
    }
}


Response Structure

(dict) --

operation (dict) --
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

id (string) --
The ID of the operation.

resourceName (string) --
The resource name.

resourceType (string) --
The resource type.

createdAt (datetime) --
The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --
The AWS Region and Availability Zone.

availabilityZone (string) --
The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --
The AWS Region name.



isTerminal (boolean) --
A Boolean value indicating whether the operation is terminal.

operationDetails (string) --
Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --
The type of operation.

status (string) --
The status of the operation.

statusChangedAt (datetime) --
The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --
The error code.

errorDetails (string) --
The error details.









Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operation': {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        }
    }
    
    
    :returns: 
    Lightsail.Client.exceptions.ServiceException
    Lightsail.Client.exceptions.InvalidInputException
    Lightsail.Client.exceptions.NotFoundException
    Lightsail.Client.exceptions.OperationFailureException
    Lightsail.Client.exceptions.AccessDeniedException
    Lightsail.Client.exceptions.AccountSetupInProgressException
    Lightsail.Client.exceptions.UnauthenticatedException
    
    """
    pass

def delete_instance(instanceName=None, forceDeleteAddOns=None):
    """
    Deletes an Amazon Lightsail instance.
    The delete instance operation supports tag-based access control via resource tags applied to the resource identified by instance name . For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_instance(
        instanceName='string',
        forceDeleteAddOns=True|False
    )
    
    
    :type instanceName: string
    :param instanceName: [REQUIRED]\nThe name of the instance to delete.\n

    :type forceDeleteAddOns: boolean
    :param forceDeleteAddOns: A Boolean value to indicate whether to delete the enabled add-ons for the disk.

    :rtype: dict

ReturnsResponse Syntax
{
    'operations': [
        {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        },
    ]
}


Response Structure

(dict) --

operations (list) --
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

(dict) --
Describes the API operation.

id (string) --
The ID of the operation.

resourceName (string) --
The resource name.

resourceType (string) --
The resource type.

createdAt (datetime) --
The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --
The AWS Region and Availability Zone.

availabilityZone (string) --
The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --
The AWS Region name.



isTerminal (boolean) --
A Boolean value indicating whether the operation is terminal.

operationDetails (string) --
Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --
The type of operation.

status (string) --
The status of the operation.

statusChangedAt (datetime) --
The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --
The error code.

errorDetails (string) --
The error details.











Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    :returns: 
    Lightsail.Client.exceptions.ServiceException
    Lightsail.Client.exceptions.InvalidInputException
    Lightsail.Client.exceptions.NotFoundException
    Lightsail.Client.exceptions.OperationFailureException
    Lightsail.Client.exceptions.AccessDeniedException
    Lightsail.Client.exceptions.AccountSetupInProgressException
    Lightsail.Client.exceptions.UnauthenticatedException
    
    """
    pass

def delete_instance_snapshot(instanceSnapshotName=None):
    """
    Deletes a specific snapshot of a virtual private server (or instance ).
    The delete instance snapshot operation supports tag-based access control via resource tags applied to the resource identified by instance snapshot name . For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_instance_snapshot(
        instanceSnapshotName='string'
    )
    
    
    :type instanceSnapshotName: string
    :param instanceSnapshotName: [REQUIRED]\nThe name of the snapshot to delete.\n

    :rtype: dict
ReturnsResponse Syntax{
    'operations': [
        {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        },
    ]
}


Response Structure

(dict) --
operations (list) --An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

(dict) --Describes the API operation.

id (string) --The ID of the operation.

resourceName (string) --The resource name.

resourceType (string) --The resource type.

createdAt (datetime) --The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --The AWS Region and Availability Zone.

availabilityZone (string) --The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --The AWS Region name.



isTerminal (boolean) --A Boolean value indicating whether the operation is terminal.

operationDetails (string) --Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --The type of operation.

status (string) --The status of the operation.

statusChangedAt (datetime) --The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --The error code.

errorDetails (string) --The error details.










Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
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
    The delete key pair operation supports tag-based access control via resource tags applied to the resource identified by key pair name . For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_key_pair(
        keyPairName='string'
    )
    
    
    :type keyPairName: string
    :param keyPairName: [REQUIRED]\nThe name of the key pair to delete.\n

    :rtype: dict
ReturnsResponse Syntax{
    'operation': {
        'id': 'string',
        'resourceName': 'string',
        'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
        'createdAt': datetime(2015, 1, 1),
        'location': {
            'availabilityZone': 'string',
            'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
        },
        'isTerminal': True|False,
        'operationDetails': 'string',
        'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
        'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
        'statusChangedAt': datetime(2015, 1, 1),
        'errorCode': 'string',
        'errorDetails': 'string'
    }
}


Response Structure

(dict) --
operation (dict) --An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

id (string) --The ID of the operation.

resourceName (string) --The resource name.

resourceType (string) --The resource type.

createdAt (datetime) --The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --The AWS Region and Availability Zone.

availabilityZone (string) --The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --The AWS Region name.



isTerminal (boolean) --A Boolean value indicating whether the operation is terminal.

operationDetails (string) --Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --The type of operation.

status (string) --The status of the operation.

statusChangedAt (datetime) --The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --The error code.

errorDetails (string) --The error details.








Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operation': {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        }
    }
    
    
    """
    pass

def delete_known_host_keys(instanceName=None):
    """
    Deletes the known host key or certificate used by the Amazon Lightsail browser-based SSH or RDP clients to authenticate an instance. This operation enables the Lightsail browser-based SSH or RDP clients to connect to the instance after a host key mismatch.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_known_host_keys(
        instanceName='string'
    )
    
    
    :type instanceName: string
    :param instanceName: [REQUIRED]\nThe name of the instance for which you want to reset the host key or certificate.\n

    :rtype: dict
ReturnsResponse Syntax{
    'operations': [
        {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        },
    ]
}


Response Structure

(dict) --
operations (list) --An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

(dict) --Describes the API operation.

id (string) --The ID of the operation.

resourceName (string) --The resource name.

resourceType (string) --The resource type.

createdAt (datetime) --The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --The AWS Region and Availability Zone.

availabilityZone (string) --The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --The AWS Region name.



isTerminal (boolean) --A Boolean value indicating whether the operation is terminal.

operationDetails (string) --Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --The type of operation.

status (string) --The status of the operation.

statusChangedAt (datetime) --The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --The error code.

errorDetails (string) --The error details.










Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def delete_load_balancer(loadBalancerName=None):
    """
    Deletes a Lightsail load balancer and all its associated SSL/TLS certificates. Once the load balancer is deleted, you will need to create a new load balancer, create a new certificate, and verify domain ownership again.
    The delete load balancer operation supports tag-based access control via resource tags applied to the resource identified by load balancer name . For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_load_balancer(
        loadBalancerName='string'
    )
    
    
    :type loadBalancerName: string
    :param loadBalancerName: [REQUIRED]\nThe name of the load balancer you want to delete.\n

    :rtype: dict
ReturnsResponse Syntax{
    'operations': [
        {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        },
    ]
}


Response Structure

(dict) --
operations (list) --An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

(dict) --Describes the API operation.

id (string) --The ID of the operation.

resourceName (string) --The resource name.

resourceType (string) --The resource type.

createdAt (datetime) --The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --The AWS Region and Availability Zone.

availabilityZone (string) --The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --The AWS Region name.



isTerminal (boolean) --A Boolean value indicating whether the operation is terminal.

operationDetails (string) --Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --The type of operation.

status (string) --The status of the operation.

statusChangedAt (datetime) --The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --The error code.

errorDetails (string) --The error details.










Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def delete_load_balancer_tls_certificate(loadBalancerName=None, certificateName=None, force=None):
    """
    Deletes an SSL/TLS certificate associated with a Lightsail load balancer.
    The DeleteLoadBalancerTlsCertificate operation supports tag-based access control via resource tags applied to the resource identified by load balancer name . For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_load_balancer_tls_certificate(
        loadBalancerName='string',
        certificateName='string',
        force=True|False
    )
    
    
    :type loadBalancerName: string
    :param loadBalancerName: [REQUIRED]\nThe load balancer name.\n

    :type certificateName: string
    :param certificateName: [REQUIRED]\nThe SSL/TLS certificate name.\n

    :type force: boolean
    :param force: When true , forces the deletion of an SSL/TLS certificate.\nThere can be two certificates associated with a Lightsail load balancer: the primary and the backup. The force parameter is required when the primary SSL/TLS certificate is in use by an instance attached to the load balancer.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'operations': [
        {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        },
    ]
}


Response Structure

(dict) --

operations (list) --
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

(dict) --
Describes the API operation.

id (string) --
The ID of the operation.

resourceName (string) --
The resource name.

resourceType (string) --
The resource type.

createdAt (datetime) --
The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --
The AWS Region and Availability Zone.

availabilityZone (string) --
The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --
The AWS Region name.



isTerminal (boolean) --
A Boolean value indicating whether the operation is terminal.

operationDetails (string) --
Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --
The type of operation.

status (string) --
The status of the operation.

statusChangedAt (datetime) --
The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --
The error code.

errorDetails (string) --
The error details.











Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    :returns: 
    Lightsail.Client.exceptions.ServiceException
    Lightsail.Client.exceptions.InvalidInputException
    Lightsail.Client.exceptions.NotFoundException
    Lightsail.Client.exceptions.OperationFailureException
    Lightsail.Client.exceptions.AccessDeniedException
    Lightsail.Client.exceptions.AccountSetupInProgressException
    Lightsail.Client.exceptions.UnauthenticatedException
    
    """
    pass

def delete_relational_database(relationalDatabaseName=None, skipFinalSnapshot=None, finalRelationalDatabaseSnapshotName=None):
    """
    Deletes a database in Amazon Lightsail.
    The delete relational database operation supports tag-based access control via resource tags applied to the resource identified by relationalDatabaseName. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_relational_database(
        relationalDatabaseName='string',
        skipFinalSnapshot=True|False,
        finalRelationalDatabaseSnapshotName='string'
    )
    
    
    :type relationalDatabaseName: string
    :param relationalDatabaseName: [REQUIRED]\nThe name of the database that you are deleting.\n

    :type skipFinalSnapshot: boolean
    :param skipFinalSnapshot: Determines whether a final database snapshot is created before your database is deleted. If true is specified, no database snapshot is created. If false is specified, a database snapshot is created before your database is deleted.\nYou must specify the final relational database snapshot name parameter if the skip final snapshot parameter is false .\nDefault: false\n

    :type finalRelationalDatabaseSnapshotName: string
    :param finalRelationalDatabaseSnapshotName: The name of the database snapshot created if skip final snapshot is false , which is the default value for that parameter.\n\nNote\nSpecifying this parameter and also specifying the skip final snapshot parameter to true results in an error.\n\nConstraints:\n\nMust contain from 2 to 255 alphanumeric characters, or hyphens.\nThe first and last character must be a letter or number.\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'operations': [
        {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        },
    ]
}


Response Structure

(dict) --

operations (list) --
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

(dict) --
Describes the API operation.

id (string) --
The ID of the operation.

resourceName (string) --
The resource name.

resourceType (string) --
The resource type.

createdAt (datetime) --
The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --
The AWS Region and Availability Zone.

availabilityZone (string) --
The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --
The AWS Region name.



isTerminal (boolean) --
A Boolean value indicating whether the operation is terminal.

operationDetails (string) --
Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --
The type of operation.

status (string) --
The status of the operation.

statusChangedAt (datetime) --
The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --
The error code.

errorDetails (string) --
The error details.











Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    :returns: 
    Lightsail.Client.exceptions.ServiceException
    Lightsail.Client.exceptions.InvalidInputException
    Lightsail.Client.exceptions.NotFoundException
    Lightsail.Client.exceptions.OperationFailureException
    Lightsail.Client.exceptions.AccessDeniedException
    Lightsail.Client.exceptions.AccountSetupInProgressException
    Lightsail.Client.exceptions.UnauthenticatedException
    
    """
    pass

def delete_relational_database_snapshot(relationalDatabaseSnapshotName=None):
    """
    Deletes a database snapshot in Amazon Lightsail.
    The delete relational database snapshot operation supports tag-based access control via resource tags applied to the resource identified by relationalDatabaseName. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_relational_database_snapshot(
        relationalDatabaseSnapshotName='string'
    )
    
    
    :type relationalDatabaseSnapshotName: string
    :param relationalDatabaseSnapshotName: [REQUIRED]\nThe name of the database snapshot that you are deleting.\n

    :rtype: dict
ReturnsResponse Syntax{
    'operations': [
        {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        },
    ]
}


Response Structure

(dict) --
operations (list) --An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

(dict) --Describes the API operation.

id (string) --The ID of the operation.

resourceName (string) --The resource name.

resourceType (string) --The resource type.

createdAt (datetime) --The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --The AWS Region and Availability Zone.

availabilityZone (string) --The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --The AWS Region name.



isTerminal (boolean) --A Boolean value indicating whether the operation is terminal.

operationDetails (string) --Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --The type of operation.

status (string) --The status of the operation.

statusChangedAt (datetime) --The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --The error code.

errorDetails (string) --The error details.










Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def detach_disk(diskName=None):
    """
    Detaches a stopped block storage disk from a Lightsail instance. Make sure to unmount any file systems on the device within your operating system before stopping the instance and detaching the disk.
    The detach disk operation supports tag-based access control via resource tags applied to the resource identified by disk name . For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.detach_disk(
        diskName='string'
    )
    
    
    :type diskName: string
    :param diskName: [REQUIRED]\nThe unique name of the disk you want to detach from your instance (e.g., my-disk ).\n

    :rtype: dict
ReturnsResponse Syntax{
    'operations': [
        {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        },
    ]
}


Response Structure

(dict) --
operations (list) --An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

(dict) --Describes the API operation.

id (string) --The ID of the operation.

resourceName (string) --The resource name.

resourceType (string) --The resource type.

createdAt (datetime) --The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --The AWS Region and Availability Zone.

availabilityZone (string) --The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --The AWS Region name.



isTerminal (boolean) --A Boolean value indicating whether the operation is terminal.

operationDetails (string) --Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --The type of operation.

status (string) --The status of the operation.

statusChangedAt (datetime) --The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --The error code.

errorDetails (string) --The error details.










Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def detach_instances_from_load_balancer(loadBalancerName=None, instanceNames=None):
    """
    Detaches the specified instances from a Lightsail load balancer.
    This operation waits until the instances are no longer needed before they are detached from the load balancer.
    The detach instances from load balancer operation supports tag-based access control via resource tags applied to the resource identified by load balancer name . For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.detach_instances_from_load_balancer(
        loadBalancerName='string',
        instanceNames=[
            'string',
        ]
    )
    
    
    :type loadBalancerName: string
    :param loadBalancerName: [REQUIRED]\nThe name of the Lightsail load balancer.\n

    :type instanceNames: list
    :param instanceNames: [REQUIRED]\nAn array of strings containing the names of the instances you want to detach from the load balancer.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'operations': [
        {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        },
    ]
}


Response Structure

(dict) --

operations (list) --
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

(dict) --
Describes the API operation.

id (string) --
The ID of the operation.

resourceName (string) --
The resource name.

resourceType (string) --
The resource type.

createdAt (datetime) --
The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --
The AWS Region and Availability Zone.

availabilityZone (string) --
The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --
The AWS Region name.



isTerminal (boolean) --
A Boolean value indicating whether the operation is terminal.

operationDetails (string) --
Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --
The type of operation.

status (string) --
The status of the operation.

statusChangedAt (datetime) --
The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --
The error code.

errorDetails (string) --
The error details.











Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    :returns: 
    Lightsail.Client.exceptions.ServiceException
    Lightsail.Client.exceptions.InvalidInputException
    Lightsail.Client.exceptions.NotFoundException
    Lightsail.Client.exceptions.OperationFailureException
    Lightsail.Client.exceptions.AccessDeniedException
    Lightsail.Client.exceptions.AccountSetupInProgressException
    Lightsail.Client.exceptions.UnauthenticatedException
    
    """
    pass

def detach_static_ip(staticIpName=None):
    """
    Detaches a static IP from the Amazon Lightsail instance to which it is attached.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.detach_static_ip(
        staticIpName='string'
    )
    
    
    :type staticIpName: string
    :param staticIpName: [REQUIRED]\nThe name of the static IP to detach from the instance.\n

    :rtype: dict
ReturnsResponse Syntax{
    'operations': [
        {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        },
    ]
}


Response Structure

(dict) --
operations (list) --An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

(dict) --Describes the API operation.

id (string) --The ID of the operation.

resourceName (string) --The resource name.

resourceType (string) --The resource type.

createdAt (datetime) --The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --The AWS Region and Availability Zone.

availabilityZone (string) --The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --The AWS Region name.



isTerminal (boolean) --A Boolean value indicating whether the operation is terminal.

operationDetails (string) --Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --The type of operation.

status (string) --The status of the operation.

statusChangedAt (datetime) --The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --The error code.

errorDetails (string) --The error details.










Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def disable_add_on(addOnType=None, resourceName=None):
    """
    Disables an add-on for an Amazon Lightsail resource. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disable_add_on(
        addOnType='AutoSnapshot',
        resourceName='string'
    )
    
    
    :type addOnType: string
    :param addOnType: [REQUIRED]\nThe add-on type to disable.\n

    :type resourceName: string
    :param resourceName: [REQUIRED]\nThe name of the source resource for which to disable the add-on.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'operations': [
        {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        },
    ]
}


Response Structure

(dict) --

operations (list) --
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

(dict) --
Describes the API operation.

id (string) --
The ID of the operation.

resourceName (string) --
The resource name.

resourceType (string) --
The resource type.

createdAt (datetime) --
The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --
The AWS Region and Availability Zone.

availabilityZone (string) --
The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --
The AWS Region name.



isTerminal (boolean) --
A Boolean value indicating whether the operation is terminal.

operationDetails (string) --
Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --
The type of operation.

status (string) --
The status of the operation.

statusChangedAt (datetime) --
The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --
The error code.

errorDetails (string) --
The error details.











Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    :returns: 
    Lightsail.Client.exceptions.ServiceException
    Lightsail.Client.exceptions.InvalidInputException
    Lightsail.Client.exceptions.NotFoundException
    Lightsail.Client.exceptions.OperationFailureException
    Lightsail.Client.exceptions.AccessDeniedException
    Lightsail.Client.exceptions.UnauthenticatedException
    
    """
    pass

def download_default_key_pair():
    """
    Downloads the default SSH key pair from the user\'s account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.download_default_key_pair()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'publicKeyBase64': 'string',
    'privateKeyBase64': 'string'
}


Response Structure

(dict) --
publicKeyBase64 (string) --A base64-encoded public key of the ssh-rsa type.

privateKeyBase64 (string) --A base64-encoded RSA private key.






Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'publicKeyBase64': 'string',
        'privateKeyBase64': 'string'
    }
    
    
    """
    pass

def enable_add_on(resourceName=None, addOnRequest=None):
    """
    Enables or modifies an add-on for an Amazon Lightsail resource. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.enable_add_on(
        resourceName='string',
        addOnRequest={
            'addOnType': 'AutoSnapshot',
            'autoSnapshotAddOnRequest': {
                'snapshotTimeOfDay': 'string'
            }
        }
    )
    
    
    :type resourceName: string
    :param resourceName: [REQUIRED]\nThe name of the source resource for which to enable or modify the add-on.\n

    :type addOnRequest: dict
    :param addOnRequest: [REQUIRED]\nAn array of strings representing the add-on to enable or modify.\n\naddOnType (string) -- [REQUIRED]The add-on type.\n\nautoSnapshotAddOnRequest (dict) --An object that represents additional parameters when enabling or modifying the automatic snapshot add-on.\n\nsnapshotTimeOfDay (string) --The daily time when an automatic snapshot will be created.\nConstraints:\n\nMust be in HH:00 format, and in an hourly increment.\nSpecified in Coordinated Universal Time (UTC).\nThe snapshot will be automatically created between the time specified and up to 45 minutes after.\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'operations': [
        {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        },
    ]
}


Response Structure

(dict) --

operations (list) --
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

(dict) --
Describes the API operation.

id (string) --
The ID of the operation.

resourceName (string) --
The resource name.

resourceType (string) --
The resource type.

createdAt (datetime) --
The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --
The AWS Region and Availability Zone.

availabilityZone (string) --
The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --
The AWS Region name.



isTerminal (boolean) --
A Boolean value indicating whether the operation is terminal.

operationDetails (string) --
Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --
The type of operation.

status (string) --
The status of the operation.

statusChangedAt (datetime) --
The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --
The error code.

errorDetails (string) --
The error details.











Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    :returns: 
    Lightsail.Client.exceptions.ServiceException
    Lightsail.Client.exceptions.InvalidInputException
    Lightsail.Client.exceptions.NotFoundException
    Lightsail.Client.exceptions.OperationFailureException
    Lightsail.Client.exceptions.AccessDeniedException
    Lightsail.Client.exceptions.UnauthenticatedException
    
    """
    pass

def export_snapshot(sourceSnapshotName=None):
    """
    Exports an Amazon Lightsail instance or block storage disk snapshot to Amazon Elastic Compute Cloud (Amazon EC2). This operation results in an export snapshot record that can be used with the create cloud formation stack operation to create new Amazon EC2 instances.
    Exported instance snapshots appear in Amazon EC2 as Amazon Machine Images (AMIs), and the instance system disk appears as an Amazon Elastic Block Store (Amazon EBS) volume. Exported disk snapshots appear in Amazon EC2 as Amazon EBS volumes. Snapshots are exported to the same Amazon Web Services Region in Amazon EC2 as the source Lightsail snapshot.
    The export snapshot operation supports tag-based access control via resource tags applied to the resource identified by source snapshot name . For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.export_snapshot(
        sourceSnapshotName='string'
    )
    
    
    :type sourceSnapshotName: string
    :param sourceSnapshotName: [REQUIRED]\nThe name of the instance or disk snapshot to be exported to Amazon EC2.\n

    :rtype: dict
ReturnsResponse Syntax{
    'operations': [
        {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        },
    ]
}


Response Structure

(dict) --
operations (list) --An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

(dict) --Describes the API operation.

id (string) --The ID of the operation.

resourceName (string) --The resource name.

resourceType (string) --The resource type.

createdAt (datetime) --The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --The AWS Region and Availability Zone.

availabilityZone (string) --The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --The AWS Region name.



isTerminal (boolean) --A Boolean value indicating whether the operation is terminal.

operationDetails (string) --Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --The type of operation.

status (string) --The status of the operation.

statusChangedAt (datetime) --The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --The error code.

errorDetails (string) --The error details.










Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
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

def get_active_names(pageToken=None):
    """
    Returns the names of all active (not deleted) resources.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_active_names(
        pageToken='string'
    )
    
    
    :type pageToken: string
    :param pageToken: The token to advance to the next page of results from your request.\nTo get a page token, perform an initial GetActiveNames request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.\n

    :rtype: dict
ReturnsResponse Syntax{
    'activeNames': [
        'string',
    ],
    'nextPageToken': 'string'
}


Response Structure

(dict) --
activeNames (list) --The list of active names returned by the get active names request.

(string) --


nextPageToken (string) --The token to advance to the next page of resutls from your request.
A next page token is not returned if there are no more results to display.
To get the next page of results, perform another GetActiveNames request and specify the next page token using the pageToken parameter.






Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'activeNames': [
            'string',
        ],
        'nextPageToken': 'string'
    }
    
    
    :returns: 
    Lightsail.Client.exceptions.ServiceException
    Lightsail.Client.exceptions.InvalidInputException
    Lightsail.Client.exceptions.NotFoundException
    Lightsail.Client.exceptions.OperationFailureException
    Lightsail.Client.exceptions.AccessDeniedException
    Lightsail.Client.exceptions.AccountSetupInProgressException
    Lightsail.Client.exceptions.UnauthenticatedException
    
    """
    pass

def get_alarms(alarmName=None, pageToken=None, monitoredResourceName=None):
    """
    Returns information about the configured alarms. Specify an alarm name in your request to return information about a specific alarm, or specify a monitored resource name to return information about all alarms for a specific resource.
    An alarm is used to monitor a single metric for one of your resources. When a metric condition is met, the alarm can notify you by email, SMS text message, and a banner displayed on the Amazon Lightsail console. For more information, see Alarms in Amazon Lightsail .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_alarms(
        alarmName='string',
        pageToken='string',
        monitoredResourceName='string'
    )
    
    
    :type alarmName: string
    :param alarmName: The name of the alarm.\nSpecify an alarm name to return information about a specific alarm.\n

    :type pageToken: string
    :param pageToken: The token to advance to the next page of results from your request.\nTo get a page token, perform an initial GetAlarms request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.\n

    :type monitoredResourceName: string
    :param monitoredResourceName: The name of the Lightsail resource being monitored by the alarm.\nSpecify a monitored resource name to return information about all alarms for a specific resource.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'alarms': [
        {
            'name': 'string',
            'arn': 'string',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'supportCode': 'string',
            'monitoredResourceInfo': {
                'arn': 'string',
                'name': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod'
            },
            'comparisonOperator': 'GreaterThanOrEqualToThreshold'|'GreaterThanThreshold'|'LessThanThreshold'|'LessThanOrEqualToThreshold',
            'evaluationPeriods': 123,
            'period': 123,
            'threshold': 123.0,
            'datapointsToAlarm': 123,
            'treatMissingData': 'breaching'|'notBreaching'|'ignore'|'missing',
            'statistic': 'Minimum'|'Maximum'|'Sum'|'Average'|'SampleCount',
            'metricName': 'CPUUtilization'|'NetworkIn'|'NetworkOut'|'StatusCheckFailed'|'StatusCheckFailed_Instance'|'StatusCheckFailed_System'|'ClientTLSNegotiationErrorCount'|'HealthyHostCount'|'UnhealthyHostCount'|'HTTPCode_LB_4XX_Count'|'HTTPCode_LB_5XX_Count'|'HTTPCode_Instance_2XX_Count'|'HTTPCode_Instance_3XX_Count'|'HTTPCode_Instance_4XX_Count'|'HTTPCode_Instance_5XX_Count'|'InstanceResponseTime'|'RejectedConnectionCount'|'RequestCount'|'DatabaseConnections'|'DiskQueueDepth'|'FreeStorageSpace'|'NetworkReceiveThroughput'|'NetworkTransmitThroughput',
            'state': 'OK'|'ALARM'|'INSUFFICIENT_DATA',
            'unit': 'Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'|'Gigabytes'|'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Count'|'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'|'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'|'Megabits/Second'|'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None',
            'contactProtocols': [
                'Email'|'SMS',
            ],
            'notificationTriggers': [
                'OK'|'ALARM'|'INSUFFICIENT_DATA',
            ],
            'notificationEnabled': True|False
        },
    ],
    'nextPageToken': 'string'
}


Response Structure

(dict) --

alarms (list) --
An array of objects that describe the alarms.

(dict) --
Describes an alarm.
An alarm is a way to monitor your Amazon Lightsail resource metrics. For more information, see Alarms in Amazon Lightsail .

name (string) --
The name of the alarm.

arn (string) --
The Amazon Resource Name (ARN) of the alarm.

createdAt (datetime) --
The timestamp when the alarm was created.

location (dict) --
An object that lists information about the location of the alarm.

availabilityZone (string) --
The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --
The AWS Region name.



resourceType (string) --
The Lightsail resource type (e.g., Alarm ).

supportCode (string) --
The support code. Include this code in your email to support when you have questions about your Lightsail alarm. This code enables our support team to look up your Lightsail information more easily.

monitoredResourceInfo (dict) --
An object that lists information about the resource monitored by the alarm.

arn (string) --
The Amazon Resource Name (ARN) of the resource being monitored.

name (string) --
The name of the Lightsail resource being monitored.

resourceType (string) --
The Lightsail resource type of the resource being monitored.
Instances, load balancers, and relational databases are the only Lightsail resources that can currently be monitored by alarms.



comparisonOperator (string) --
The arithmetic operation used when comparing the specified statistic and threshold.

evaluationPeriods (integer) --
The number of periods over which data is compared to the specified threshold.

period (integer) --
The period, in seconds, over which the statistic is applied.

threshold (float) --
The value against which the specified statistic is compared.

datapointsToAlarm (integer) --
The number of data points that must not within the specified threshold to trigger the alarm.

treatMissingData (string) --
Specifies how the alarm handles missing data points.
An alarm can treat missing data in the following ways:

breaching - Assume the missing data is not within the threshold. Missing data counts towards the number of times the metric is not within the threshold.
notBreaching - Assume the missing data is within the threshold. Missing data does not count towards the number of times the metric is not within the threshold.
ignore - Ignore the missing data. Maintains the current alarm state.
missing - Missing data is treated as missing.


statistic (string) --
The statistic for the metric associated with the alarm.
The following statistics are available:

Minimum - The lowest value observed during the specified period. Use this value to determine low volumes of activity for your application.
Maximum - The highest value observed during the specified period. Use this value to determine high volumes of activity for your application.
Sum - All values submitted for the matching metric added together. You can use this statistic to determine the total volume of a metric.
Average - The value of Sum / SampleCount during the specified period. By comparing this statistic with the Minimum and Maximum values, you can determine the full scope of a metric and how close the average use is to the Minimum and Maximum values. This comparison helps you to know when to increase or decrease your resources.
SampleCount - The count, or number, of data points used for the statistical calculation.


metricName (string) --
The name of the metric associated with the alarm.

state (string) --
The current state of the alarm.
An alarm has the following possible states:

ALARM - The metric is outside of the defined threshold.
INSUFFICIENT_DATA - The alarm has just started, the metric is not available, or not enough data is available for the metric to determine the alarm state.
OK - The metric is within the defined threshold.


unit (string) --
The unit of the metric associated with the alarm.

contactProtocols (list) --
The contact protocols for the alarm, such as Email , SMS (text messaging), or both.

(string) --


notificationTriggers (list) --
The alarm states that trigger a notification.

(string) --


notificationEnabled (boolean) --
Indicates whether the alarm is enabled.





nextPageToken (string) --
The token to advance to the next page of resutls from your request.
A next page token is not returned if there are no more results to display.
To get the next page of results, perform another GetAlarms request and specify the next page token using the pageToken parameter.







Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.UnauthenticatedException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.NotFoundException


    :return: {
        'alarms': [
            {
                'name': 'string',
                'arn': 'string',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'supportCode': 'string',
                'monitoredResourceInfo': {
                    'arn': 'string',
                    'name': 'string',
                    'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod'
                },
                'comparisonOperator': 'GreaterThanOrEqualToThreshold'|'GreaterThanThreshold'|'LessThanThreshold'|'LessThanOrEqualToThreshold',
                'evaluationPeriods': 123,
                'period': 123,
                'threshold': 123.0,
                'datapointsToAlarm': 123,
                'treatMissingData': 'breaching'|'notBreaching'|'ignore'|'missing',
                'statistic': 'Minimum'|'Maximum'|'Sum'|'Average'|'SampleCount',
                'metricName': 'CPUUtilization'|'NetworkIn'|'NetworkOut'|'StatusCheckFailed'|'StatusCheckFailed_Instance'|'StatusCheckFailed_System'|'ClientTLSNegotiationErrorCount'|'HealthyHostCount'|'UnhealthyHostCount'|'HTTPCode_LB_4XX_Count'|'HTTPCode_LB_5XX_Count'|'HTTPCode_Instance_2XX_Count'|'HTTPCode_Instance_3XX_Count'|'HTTPCode_Instance_4XX_Count'|'HTTPCode_Instance_5XX_Count'|'InstanceResponseTime'|'RejectedConnectionCount'|'RequestCount'|'DatabaseConnections'|'DiskQueueDepth'|'FreeStorageSpace'|'NetworkReceiveThroughput'|'NetworkTransmitThroughput',
                'state': 'OK'|'ALARM'|'INSUFFICIENT_DATA',
                'unit': 'Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'|'Gigabytes'|'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Count'|'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'|'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'|'Megabits/Second'|'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None',
                'contactProtocols': [
                    'Email'|'SMS',
                ],
                'notificationTriggers': [
                    'OK'|'ALARM'|'INSUFFICIENT_DATA',
                ],
                'notificationEnabled': True|False
            },
        ],
        'nextPageToken': 'string'
    }
    
    
    :returns: 
    breaching - Assume the missing data is not within the threshold. Missing data counts towards the number of times the metric is not within the threshold.
    notBreaching - Assume the missing data is within the threshold. Missing data does not count towards the number of times the metric is not within the threshold.
    ignore - Ignore the missing data. Maintains the current alarm state.
    missing - Missing data is treated as missing.
    
    """
    pass

def get_auto_snapshots(resourceName=None):
    """
    Returns the available automatic snapshots for an instance or disk. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_auto_snapshots(
        resourceName='string'
    )
    
    
    :type resourceName: string
    :param resourceName: [REQUIRED]\nThe name of the source instance or disk from which to get automatic snapshot information.\n

    :rtype: dict
ReturnsResponse Syntax{
    'resourceName': 'string',
    'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
    'autoSnapshots': [
        {
            'date': 'string',
            'createdAt': datetime(2015, 1, 1),
            'status': 'Success'|'Failed'|'InProgress'|'NotFound',
            'fromAttachedDisks': [
                {
                    'path': 'string',
                    'sizeInGb': 123
                },
            ]
        },
    ]
}


Response Structure

(dict) --
resourceName (string) --The name of the source instance or disk for the automatic snapshots.

resourceType (string) --The resource type (e.g., Instance or Disk ).

autoSnapshots (list) --An array of objects that describe the automatic snapshots that are available for the specified source instance or disk.

(dict) --Describes an automatic snapshot.

date (string) --The date of the automatic snapshot in YYYY-MM-DD format.

createdAt (datetime) --The timestamp when the automatic snapshot was created.

status (string) --The status of the automatic snapshot.

fromAttachedDisks (list) --An array of objects that describe the block storage disks attached to the instance when the automatic snapshot was created.

(dict) --Describes a block storage disk that is attached to an instance, and is included in an automatic snapshot.

path (string) --The path of the disk (e.g., /dev/xvdf ).

sizeInGb (integer) --The size of the disk in GB.














Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'resourceName': 'string',
        'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
        'autoSnapshots': [
            {
                'date': 'string',
                'createdAt': datetime(2015, 1, 1),
                'status': 'Success'|'Failed'|'InProgress'|'NotFound',
                'fromAttachedDisks': [
                    {
                        'path': 'string',
                        'sizeInGb': 123
                    },
                ]
            },
        ]
    }
    
    
    """
    pass

def get_blueprints(includeInactive=None, pageToken=None):
    """
    Returns the list of available instance images, or blueprints . You can use a blueprint to create a new instance already running a specific operating system, as well as a preinstalled app or development stack. The software each instance is running depends on the blueprint image you choose.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_blueprints(
        includeInactive=True|False,
        pageToken='string'
    )
    
    
    :type includeInactive: boolean
    :param includeInactive: A Boolean value indicating whether to include inactive results in your request.

    :type pageToken: string
    :param pageToken: The token to advance to the next page of results from your request.\nTo get a page token, perform an initial GetBlueprints request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.\n

    :rtype: dict

ReturnsResponse Syntax
{
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
            'licenseUrl': 'string',
            'platform': 'LINUX_UNIX'|'WINDOWS'
        },
    ],
    'nextPageToken': 'string'
}


Response Structure

(dict) --

blueprints (list) --
An array of key-value pairs that contains information about the available blueprints.

(dict) --
Describes a blueprint (a virtual private server image).

blueprintId (string) --
The ID for the virtual private server image (e.g., app_wordpress_4_4 or app_lamp_7_0 ).

name (string) --
The friendly name of the blueprint (e.g., Amazon Linux ).

group (string) --
The group name of the blueprint (e.g., amazon-linux ).

type (string) --
The type of the blueprint (e.g., os or app ).

description (string) --
The description of the blueprint.

isActive (boolean) --
A Boolean value indicating whether the blueprint is active. Inactive blueprints are listed to support customers with existing instances but are not necessarily available for launch of new instances. Blueprints are marked inactive when they become outdated due to operating system updates or new application releases.

minPower (integer) --
The minimum bundle power required to run this blueprint. For example, you need a bundle with a power value of 500 or more to create an instance that uses a blueprint with a minimum power value of 500. 0 indicates that the blueprint runs on all instance sizes.

version (string) --
The version number of the operating system, application, or stack (e.g., 2016.03.0 ).

versionCode (string) --
The version code.

productUrl (string) --
The product URL to learn more about the image or blueprint.

licenseUrl (string) --
The end-user license agreement URL for the image or blueprint.

platform (string) --
The operating system platform (either Linux/Unix-based or Windows Server-based) of the blueprint.





nextPageToken (string) --
The token to advance to the next page of resutls from your request.
A next page token is not returned if there are no more results to display.
To get the next page of results, perform another GetBlueprints request and specify the next page token using the pageToken parameter.







Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


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
                'licenseUrl': 'string',
                'platform': 'LINUX_UNIX'|'WINDOWS'
            },
        ],
        'nextPageToken': 'string'
    }
    
    
    :returns: 
    Lightsail.Client.exceptions.ServiceException
    Lightsail.Client.exceptions.InvalidInputException
    Lightsail.Client.exceptions.NotFoundException
    Lightsail.Client.exceptions.OperationFailureException
    Lightsail.Client.exceptions.AccessDeniedException
    Lightsail.Client.exceptions.AccountSetupInProgressException
    Lightsail.Client.exceptions.UnauthenticatedException
    
    """
    pass

def get_bundles(includeInactive=None, pageToken=None):
    """
    Returns the list of bundles that are available for purchase. A bundle describes the specs for your virtual private server (or instance ).
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_bundles(
        includeInactive=True|False,
        pageToken='string'
    )
    
    
    :type includeInactive: boolean
    :param includeInactive: A Boolean value that indicates whether to include inactive bundle results in your request.

    :type pageToken: string
    :param pageToken: The token to advance to the next page of results from your request.\nTo get a page token, perform an initial GetBundles request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.\n

    :rtype: dict

ReturnsResponse Syntax
{
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
            'transferPerMonthInGb': 123,
            'supportedPlatforms': [
                'LINUX_UNIX'|'WINDOWS',
            ]
        },
    ],
    'nextPageToken': 'string'
}


Response Structure

(dict) --

bundles (list) --
An array of key-value pairs that contains information about the available bundles.

(dict) --
Describes a bundle, which is a set of specs describing your virtual private server (or instance ).

price (float) --
The price in US dollars (e.g., 5.0 ).

cpuCount (integer) --
The number of vCPUs included in the bundle (e.g., 2 ).

diskSizeInGb (integer) --
The size of the SSD (e.g., 30 ).

bundleId (string) --
The bundle ID (e.g., micro_1_0 ).

instanceType (string) --
The Amazon EC2 instance type (e.g., t2.micro ).

isActive (boolean) --
A Boolean value indicating whether the bundle is active.

name (string) --
A friendly name for the bundle (e.g., Micro ).

power (integer) --
A numeric value that represents the power of the bundle (e.g., 500 ). You can use the bundle\'s power value in conjunction with a blueprint\'s minimum power value to determine whether the blueprint will run on the bundle. For example, you need a bundle with a power value of 500 or more to create an instance that uses a blueprint with a minimum power value of 500.

ramSizeInGb (float) --
The amount of RAM in GB (e.g., 2.0 ).

transferPerMonthInGb (integer) --
The data transfer rate per month in GB (e.g., 2000 ).

supportedPlatforms (list) --
The operating system platform (Linux/Unix-based or Windows Server-based) that the bundle supports. You can only launch a WINDOWS bundle on a blueprint that supports the WINDOWS platform. LINUX_UNIX blueprints require a LINUX_UNIX bundle.

(string) --






nextPageToken (string) --
The token to advance to the next page of resutls from your request.
A next page token is not returned if there are no more results to display.
To get the next page of results, perform another GetBundles request and specify the next page token using the pageToken parameter.







Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


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
                'transferPerMonthInGb': 123,
                'supportedPlatforms': [
                    'LINUX_UNIX'|'WINDOWS',
                ]
            },
        ],
        'nextPageToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_cloud_formation_stack_records(pageToken=None):
    """
    Returns the CloudFormation stack record created as a result of the create cloud formation stack operation.
    An AWS CloudFormation stack is used to create a new Amazon EC2 instance from an exported Lightsail snapshot.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_cloud_formation_stack_records(
        pageToken='string'
    )
    
    
    :type pageToken: string
    :param pageToken: The token to advance to the next page of results from your request.\nTo get a page token, perform an initial GetClouFormationStackRecords request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.\n

    :rtype: dict
ReturnsResponse Syntax{
    'cloudFormationStackRecords': [
        {
            'name': 'string',
            'arn': 'string',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'state': 'Started'|'Succeeded'|'Failed',
            'sourceInfo': [
                {
                    'resourceType': 'ExportSnapshotRecord',
                    'name': 'string',
                    'arn': 'string'
                },
            ],
            'destinationInfo': {
                'id': 'string',
                'service': 'string'
            }
        },
    ],
    'nextPageToken': 'string'
}


Response Structure

(dict) --
cloudFormationStackRecords (list) --A list of objects describing the CloudFormation stack records.

(dict) --Describes a CloudFormation stack record created as a result of the create cloud formation stack operation.
A CloudFormation stack record provides information about the AWS CloudFormation stack used to create a new Amazon Elastic Compute Cloud instance from an exported Lightsail instance snapshot.

name (string) --The name of the CloudFormation stack record. It starts with CloudFormationStackRecord followed by a GUID.

arn (string) --The Amazon Resource Name (ARN) of the CloudFormation stack record.

createdAt (datetime) --The date when the CloudFormation stack record was created.

location (dict) --A list of objects describing the Availability Zone and AWS Region of the CloudFormation stack record.

availabilityZone (string) --The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --The AWS Region name.



resourceType (string) --The Lightsail resource type (e.g., CloudFormationStackRecord ).

state (string) --The current state of the CloudFormation stack record.

sourceInfo (list) --A list of objects describing the source of the CloudFormation stack record.

(dict) --Describes the source of a CloudFormation stack record (i.e., the export snapshot record).

resourceType (string) --The Lightsail resource type (e.g., ExportSnapshotRecord ).

name (string) --The name of the record.

arn (string) --The Amazon Resource Name (ARN) of the export snapshot record.





destinationInfo (dict) --A list of objects describing the destination service, which is AWS CloudFormation, and the Amazon Resource Name (ARN) of the AWS CloudFormation stack.

id (string) --The ID of the resource created at the destination.

service (string) --The destination service of the record.







nextPageToken (string) --The token to advance to the next page of resutls from your request.
A next page token is not returned if there are no more results to display.
To get the next page of results, perform another GetCloudFormationStackRecords request and specify the next page token using the pageToken parameter.






Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'cloudFormationStackRecords': [
            {
                'name': 'string',
                'arn': 'string',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'state': 'Started'|'Succeeded'|'Failed',
                'sourceInfo': [
                    {
                        'resourceType': 'ExportSnapshotRecord',
                        'name': 'string',
                        'arn': 'string'
                    },
                ],
                'destinationInfo': {
                    'id': 'string',
                    'service': 'string'
                }
            },
        ],
        'nextPageToken': 'string'
    }
    
    
    """
    pass

def get_contact_methods(protocols=None):
    """
    Returns information about the configured contact methods. Specify a protocol in your request to return information about a specific contact method.
    A contact method is used to send you notifications about your Amazon Lightsail resources. You can add one email address and one mobile phone number contact method in each AWS Region. However, SMS text messaging is not supported in some AWS Regions, and SMS text messages cannot be sent to some countries/regions. For more information, see Notifications in Amazon Lightsail .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_contact_methods(
        protocols=[
            'Email'|'SMS',
        ]
    )
    
    
    :type protocols: list
    :param protocols: The protocols used to send notifications, such as Email , or SMS (text messaging).\nSpecify a protocol in your request to return information about a specific contact method protocol.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'contactMethods': [
        {
            'contactEndpoint': 'string',
            'status': 'PendingVerification'|'Valid'|'Invalid',
            'protocol': 'Email'|'SMS',
            'name': 'string',
            'arn': 'string',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'supportCode': 'string'
        },
    ]
}


Response Structure

(dict) --
contactMethods (list) --An array of objects that describe the contact methods.

(dict) --Describes a contact method.
A contact method is a way to send you notifications. For more information, see Notifications in Amazon Lightsail .

contactEndpoint (string) --The destination of the contact method, such as an email address or a mobile phone number.

status (string) --The current status of the contact method.
A contact method has the following possible status:

PendingVerification - The contact method has not yet been verified, and the verification has not yet expired.
Valid - The contact method has been verified.
InValid - An attempt was made to verify the contact method, but the verification has expired.


protocol (string) --The protocol of the contact method, such as email or SMS (text messaging).

name (string) --The name of the contact method.

arn (string) --The Amazon Resource Name (ARN) of the contact method.

createdAt (datetime) --The timestamp when the contact method was created.

location (dict) --Describes the resource location.

availabilityZone (string) --The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --The AWS Region name.



resourceType (string) --The Lightsail resource type (e.g., ContactMethod ).

supportCode (string) --The support code. Include this code in your email to support when you have questions about your Lightsail contact method. This code enables our support team to look up your Lightsail information more easily.










Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'contactMethods': [
            {
                'contactEndpoint': 'string',
                'status': 'PendingVerification'|'Valid'|'Invalid',
                'protocol': 'Email'|'SMS',
                'name': 'string',
                'arn': 'string',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'supportCode': 'string'
            },
        ]
    }
    
    
    :returns: 
    PendingVerification - The contact method has not yet been verified, and the verification has not yet expired.
    Valid - The contact method has been verified.
    InValid - An attempt was made to verify the contact method, but the verification has expired.
    
    """
    pass

def get_disk(diskName=None):
    """
    Returns information about a specific block storage disk.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_disk(
        diskName='string'
    )
    
    
    :type diskName: string
    :param diskName: [REQUIRED]\nThe name of the disk (e.g., my-disk ).\n

    :rtype: dict
ReturnsResponse Syntax{
    'disk': {
        'name': 'string',
        'arn': 'string',
        'supportCode': 'string',
        'createdAt': datetime(2015, 1, 1),
        'location': {
            'availabilityZone': 'string',
            'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
        },
        'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
        'tags': [
            {
                'key': 'string',
                'value': 'string'
            },
        ],
        'addOns': [
            {
                'name': 'string',
                'status': 'string',
                'snapshotTimeOfDay': 'string',
                'nextSnapshotTimeOfDay': 'string'
            },
        ],
        'sizeInGb': 123,
        'isSystemDisk': True|False,
        'iops': 123,
        'path': 'string',
        'state': 'pending'|'error'|'available'|'in-use'|'unknown',
        'attachedTo': 'string',
        'isAttached': True|False,
        'attachmentState': 'string',
        'gbInUse': 123
    }
}


Response Structure

(dict) --
disk (dict) --An object containing information about the disk.

name (string) --The unique name of the disk.

arn (string) --The Amazon Resource Name (ARN) of the disk.

supportCode (string) --The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.

createdAt (datetime) --The date when the disk was created.

location (dict) --The AWS Region and Availability Zone where the disk is located.

availabilityZone (string) --The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --The AWS Region name.



resourceType (string) --The Lightsail resource type (e.g., Disk ).

tags (list) --The tag keys and optional values for the resource. For more information about tags in Lightsail, see the Lightsail Dev Guide .

(dict) --Describes a tag key and optional value assigned to an Amazon Lightsail resource.
For more information about tags in Lightsail, see the Lightsail Dev Guide .

key (string) --The key of the tag.
Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @

value (string) --The value of the tag.
Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @





addOns (list) --An array of objects representing the add-ons enabled on the disk.

(dict) --Describes an add-on that is enabled for an Amazon Lightsail resource.

name (string) --The name of the add-on.

status (string) --The status of the add-on.

snapshotTimeOfDay (string) --The daily time when an automatic snapshot is created.
The time shown is in HH:00 format, and in Coordinated Universal Time (UTC).
The snapshot is automatically created between the time shown and up to 45 minutes after.

nextSnapshotTimeOfDay (string) --The next daily time an automatic snapshot will be created.
The time shown is in HH:00 format, and in Coordinated Universal Time (UTC).
The snapshot is automatically created between the time shown and up to 45 minutes after.





sizeInGb (integer) --The size of the disk in GB.

isSystemDisk (boolean) --A Boolean value indicating whether this disk is a system disk (has an operating system loaded on it).

iops (integer) --The input/output operations per second (IOPS) of the disk.

path (string) --The disk path.

state (string) --Describes the status of the disk.

attachedTo (string) --The resources to which the disk is attached.

isAttached (boolean) --A Boolean value indicating whether the disk is attached.

attachmentState (string) --(Deprecated) The attachment state of the disk.

Note
In releases prior to November 14, 2017, this parameter returned attached for system disks in the API response. It is now deprecated, but still included in the response. Use isAttached instead.


gbInUse (integer) --(Deprecated) The number of GB in use by the disk.

Note
In releases prior to November 14, 2017, this parameter was not included in the API response. It is now deprecated.









Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'disk': {
            'name': 'string',
            'arn': 'string',
            'supportCode': 'string',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ],
            'addOns': [
                {
                    'name': 'string',
                    'status': 'string',
                    'snapshotTimeOfDay': 'string',
                    'nextSnapshotTimeOfDay': 'string'
                },
            ],
            'sizeInGb': 123,
            'isSystemDisk': True|False,
            'iops': 123,
            'path': 'string',
            'state': 'pending'|'error'|'available'|'in-use'|'unknown',
            'attachedTo': 'string',
            'isAttached': True|False,
            'attachmentState': 'string',
            'gbInUse': 123
        }
    }
    
    
    """
    pass

def get_disk_snapshot(diskSnapshotName=None):
    """
    Returns information about a specific block storage disk snapshot.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_disk_snapshot(
        diskSnapshotName='string'
    )
    
    
    :type diskSnapshotName: string
    :param diskSnapshotName: [REQUIRED]\nThe name of the disk snapshot (e.g., my-disk-snapshot ).\n

    :rtype: dict
ReturnsResponse Syntax{
    'diskSnapshot': {
        'name': 'string',
        'arn': 'string',
        'supportCode': 'string',
        'createdAt': datetime(2015, 1, 1),
        'location': {
            'availabilityZone': 'string',
            'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
        },
        'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
        'tags': [
            {
                'key': 'string',
                'value': 'string'
            },
        ],
        'sizeInGb': 123,
        'state': 'pending'|'completed'|'error'|'unknown',
        'progress': 'string',
        'fromDiskName': 'string',
        'fromDiskArn': 'string',
        'fromInstanceName': 'string',
        'fromInstanceArn': 'string',
        'isFromAutoSnapshot': True|False
    }
}


Response Structure

(dict) --
diskSnapshot (dict) --An object containing information about the disk snapshot.

name (string) --The name of the disk snapshot (e.g., my-disk-snapshot ).

arn (string) --The Amazon Resource Name (ARN) of the disk snapshot.

supportCode (string) --The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.

createdAt (datetime) --The date when the disk snapshot was created.

location (dict) --The AWS Region and Availability Zone where the disk snapshot was created.

availabilityZone (string) --The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --The AWS Region name.



resourceType (string) --The Lightsail resource type (e.g., DiskSnapshot ).

tags (list) --The tag keys and optional values for the resource. For more information about tags in Lightsail, see the Lightsail Dev Guide .

(dict) --Describes a tag key and optional value assigned to an Amazon Lightsail resource.
For more information about tags in Lightsail, see the Lightsail Dev Guide .

key (string) --The key of the tag.
Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @

value (string) --The value of the tag.
Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @





sizeInGb (integer) --The size of the disk in GB.

state (string) --The status of the disk snapshot operation.

progress (string) --The progress of the disk snapshot operation.

fromDiskName (string) --The unique name of the source disk from which the disk snapshot was created.

fromDiskArn (string) --The Amazon Resource Name (ARN) of the source disk from which the disk snapshot was created.

fromInstanceName (string) --The unique name of the source instance from which the disk (system volume) snapshot was created.

fromInstanceArn (string) --The Amazon Resource Name (ARN) of the source instance from which the disk (system volume) snapshot was created.

isFromAutoSnapshot (boolean) --A Boolean value indicating whether the snapshot was created from an automatic snapshot.








Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'diskSnapshot': {
            'name': 'string',
            'arn': 'string',
            'supportCode': 'string',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ],
            'sizeInGb': 123,
            'state': 'pending'|'completed'|'error'|'unknown',
            'progress': 'string',
            'fromDiskName': 'string',
            'fromDiskArn': 'string',
            'fromInstanceName': 'string',
            'fromInstanceArn': 'string',
            'isFromAutoSnapshot': True|False
        }
    }
    
    
    """
    pass

def get_disk_snapshots(pageToken=None):
    """
    Returns information about all block storage disk snapshots in your AWS account and region.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_disk_snapshots(
        pageToken='string'
    )
    
    
    :type pageToken: string
    :param pageToken: The token to advance to the next page of results from your request.\nTo get a page token, perform an initial GetDiskSnapshots request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.\n

    :rtype: dict
ReturnsResponse Syntax{
    'diskSnapshots': [
        {
            'name': 'string',
            'arn': 'string',
            'supportCode': 'string',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ],
            'sizeInGb': 123,
            'state': 'pending'|'completed'|'error'|'unknown',
            'progress': 'string',
            'fromDiskName': 'string',
            'fromDiskArn': 'string',
            'fromInstanceName': 'string',
            'fromInstanceArn': 'string',
            'isFromAutoSnapshot': True|False
        },
    ],
    'nextPageToken': 'string'
}


Response Structure

(dict) --
diskSnapshots (list) --An array of objects containing information about all block storage disk snapshots.

(dict) --Describes a block storage disk snapshot.

name (string) --The name of the disk snapshot (e.g., my-disk-snapshot ).

arn (string) --The Amazon Resource Name (ARN) of the disk snapshot.

supportCode (string) --The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.

createdAt (datetime) --The date when the disk snapshot was created.

location (dict) --The AWS Region and Availability Zone where the disk snapshot was created.

availabilityZone (string) --The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --The AWS Region name.



resourceType (string) --The Lightsail resource type (e.g., DiskSnapshot ).

tags (list) --The tag keys and optional values for the resource. For more information about tags in Lightsail, see the Lightsail Dev Guide .

(dict) --Describes a tag key and optional value assigned to an Amazon Lightsail resource.
For more information about tags in Lightsail, see the Lightsail Dev Guide .

key (string) --The key of the tag.
Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @

value (string) --The value of the tag.
Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @





sizeInGb (integer) --The size of the disk in GB.

state (string) --The status of the disk snapshot operation.

progress (string) --The progress of the disk snapshot operation.

fromDiskName (string) --The unique name of the source disk from which the disk snapshot was created.

fromDiskArn (string) --The Amazon Resource Name (ARN) of the source disk from which the disk snapshot was created.

fromInstanceName (string) --The unique name of the source instance from which the disk (system volume) snapshot was created.

fromInstanceArn (string) --The Amazon Resource Name (ARN) of the source instance from which the disk (system volume) snapshot was created.

isFromAutoSnapshot (boolean) --A Boolean value indicating whether the snapshot was created from an automatic snapshot.





nextPageToken (string) --The token to advance to the next page of resutls from your request.
A next page token is not returned if there are no more results to display.
To get the next page of results, perform another GetDiskSnapshots request and specify the next page token using the pageToken parameter.






Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'diskSnapshots': [
            {
                'name': 'string',
                'arn': 'string',
                'supportCode': 'string',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ],
                'sizeInGb': 123,
                'state': 'pending'|'completed'|'error'|'unknown',
                'progress': 'string',
                'fromDiskName': 'string',
                'fromDiskArn': 'string',
                'fromInstanceName': 'string',
                'fromInstanceArn': 'string',
                'isFromAutoSnapshot': True|False
            },
        ],
        'nextPageToken': 'string'
    }
    
    
    """
    pass

def get_disks(pageToken=None):
    """
    Returns information about all block storage disks in your AWS account and region.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_disks(
        pageToken='string'
    )
    
    
    :type pageToken: string
    :param pageToken: The token to advance to the next page of results from your request.\nTo get a page token, perform an initial GetDisks request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.\n

    :rtype: dict
ReturnsResponse Syntax{
    'disks': [
        {
            'name': 'string',
            'arn': 'string',
            'supportCode': 'string',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ],
            'addOns': [
                {
                    'name': 'string',
                    'status': 'string',
                    'snapshotTimeOfDay': 'string',
                    'nextSnapshotTimeOfDay': 'string'
                },
            ],
            'sizeInGb': 123,
            'isSystemDisk': True|False,
            'iops': 123,
            'path': 'string',
            'state': 'pending'|'error'|'available'|'in-use'|'unknown',
            'attachedTo': 'string',
            'isAttached': True|False,
            'attachmentState': 'string',
            'gbInUse': 123
        },
    ],
    'nextPageToken': 'string'
}


Response Structure

(dict) --
disks (list) --An array of objects containing information about all block storage disks.

(dict) --Describes a system disk or a block storage disk.

name (string) --The unique name of the disk.

arn (string) --The Amazon Resource Name (ARN) of the disk.

supportCode (string) --The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.

createdAt (datetime) --The date when the disk was created.

location (dict) --The AWS Region and Availability Zone where the disk is located.

availabilityZone (string) --The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --The AWS Region name.



resourceType (string) --The Lightsail resource type (e.g., Disk ).

tags (list) --The tag keys and optional values for the resource. For more information about tags in Lightsail, see the Lightsail Dev Guide .

(dict) --Describes a tag key and optional value assigned to an Amazon Lightsail resource.
For more information about tags in Lightsail, see the Lightsail Dev Guide .

key (string) --The key of the tag.
Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @

value (string) --The value of the tag.
Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @





addOns (list) --An array of objects representing the add-ons enabled on the disk.

(dict) --Describes an add-on that is enabled for an Amazon Lightsail resource.

name (string) --The name of the add-on.

status (string) --The status of the add-on.

snapshotTimeOfDay (string) --The daily time when an automatic snapshot is created.
The time shown is in HH:00 format, and in Coordinated Universal Time (UTC).
The snapshot is automatically created between the time shown and up to 45 minutes after.

nextSnapshotTimeOfDay (string) --The next daily time an automatic snapshot will be created.
The time shown is in HH:00 format, and in Coordinated Universal Time (UTC).
The snapshot is automatically created between the time shown and up to 45 minutes after.





sizeInGb (integer) --The size of the disk in GB.

isSystemDisk (boolean) --A Boolean value indicating whether this disk is a system disk (has an operating system loaded on it).

iops (integer) --The input/output operations per second (IOPS) of the disk.

path (string) --The disk path.

state (string) --Describes the status of the disk.

attachedTo (string) --The resources to which the disk is attached.

isAttached (boolean) --A Boolean value indicating whether the disk is attached.

attachmentState (string) --(Deprecated) The attachment state of the disk.

Note
In releases prior to November 14, 2017, this parameter returned attached for system disks in the API response. It is now deprecated, but still included in the response. Use isAttached instead.


gbInUse (integer) --(Deprecated) The number of GB in use by the disk.

Note
In releases prior to November 14, 2017, this parameter was not included in the API response. It is now deprecated.






nextPageToken (string) --The token to advance to the next page of resutls from your request.
A next page token is not returned if there are no more results to display.
To get the next page of results, perform another GetDisks request and specify the next page token using the pageToken parameter.






Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'disks': [
            {
                'name': 'string',
                'arn': 'string',
                'supportCode': 'string',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ],
                'addOns': [
                    {
                        'name': 'string',
                        'status': 'string',
                        'snapshotTimeOfDay': 'string',
                        'nextSnapshotTimeOfDay': 'string'
                    },
                ],
                'sizeInGb': 123,
                'isSystemDisk': True|False,
                'iops': 123,
                'path': 'string',
                'state': 'pending'|'error'|'available'|'in-use'|'unknown',
                'attachedTo': 'string',
                'isAttached': True|False,
                'attachmentState': 'string',
                'gbInUse': 123
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
    
    Exceptions
    
    :example: response = client.get_domain(
        domainName='string'
    )
    
    
    :type domainName: string
    :param domainName: [REQUIRED]\nThe domain name for which your want to return information about.\n

    :rtype: dict
ReturnsResponse Syntax{
    'domain': {
        'name': 'string',
        'arn': 'string',
        'supportCode': 'string',
        'createdAt': datetime(2015, 1, 1),
        'location': {
            'availabilityZone': 'string',
            'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
        },
        'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
        'tags': [
            {
                'key': 'string',
                'value': 'string'
            },
        ],
        'domainEntries': [
            {
                'id': 'string',
                'name': 'string',
                'target': 'string',
                'isAlias': True|False,
                'type': 'string',
                'options': {
                    'string': 'string'
                }
            },
        ]
    }
}


Response Structure

(dict) --
domain (dict) --An array of key-value pairs containing information about your get domain request.

name (string) --The name of the domain.

arn (string) --The Amazon Resource Name (ARN) of the domain recordset (e.g., arn:aws:lightsail:global:123456789101:Domain/824cede0-abc7-4f84-8dbc-12345EXAMPLE ).

supportCode (string) --The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.

createdAt (datetime) --The date when the domain recordset was created.

location (dict) --The AWS Region and Availability Zones where the domain recordset was created.

availabilityZone (string) --The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --The AWS Region name.



resourceType (string) --The resource type.

tags (list) --The tag keys and optional values for the resource. For more information about tags in Lightsail, see the Lightsail Dev Guide .

(dict) --Describes a tag key and optional value assigned to an Amazon Lightsail resource.
For more information about tags in Lightsail, see the Lightsail Dev Guide .

key (string) --The key of the tag.
Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @

value (string) --The value of the tag.
Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @





domainEntries (list) --An array of key-value pairs containing information about the domain entries.

(dict) --Describes a domain recordset entry.

id (string) --The ID of the domain recordset entry.

name (string) --The name of the domain.

target (string) --The target AWS name server (e.g., ns-111.awsdns-22.com. ).
For Lightsail load balancers, the value looks like ab1234c56789c6b86aba6fb203d443bc-123456789.us-east-2.elb.amazonaws.com . Be sure to also set isAlias to true when setting up an A record for a load balancer.

isAlias (boolean) --When true , specifies whether the domain entry is an alias used by the Lightsail load balancer. You can include an alias (A type) record in your request, which points to a load balancer DNS name and routes traffic to your load balancer

type (string) --The type of domain entry, such as address (A), canonical name (CNAME), mail exchanger (MX), name server (NS), start of authority (SOA), service locator (SRV), or text (TXT).
The following domain entry types can be used:

A
CNAME
MX
NS
SOA
SRV
TXT


options (dict) --(Deprecated) The options for the domain entry.

Note
In releases prior to November 29, 2017, this parameter was not included in the API response. It is now deprecated.


(string) --
(string) --















Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'domain': {
            'name': 'string',
            'arn': 'string',
            'supportCode': 'string',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ],
            'domainEntries': [
                {
                    'id': 'string',
                    'name': 'string',
                    'target': 'string',
                    'isAlias': True|False,
                    'type': 'string',
                    'options': {
                        'string': 'string'
                    }
                },
            ]
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def get_domains(pageToken=None):
    """
    Returns a list of all domains in the user\'s account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_domains(
        pageToken='string'
    )
    
    
    :type pageToken: string
    :param pageToken: The token to advance to the next page of results from your request.\nTo get a page token, perform an initial GetDomains request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.\n

    :rtype: dict
ReturnsResponse Syntax{
    'domains': [
        {
            'name': 'string',
            'arn': 'string',
            'supportCode': 'string',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ],
            'domainEntries': [
                {
                    'id': 'string',
                    'name': 'string',
                    'target': 'string',
                    'isAlias': True|False,
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


Response Structure

(dict) --
domains (list) --An array of key-value pairs containing information about each of the domain entries in the user\'s account.

(dict) --Describes a domain where you are storing recordsets in Lightsail.

name (string) --The name of the domain.

arn (string) --The Amazon Resource Name (ARN) of the domain recordset (e.g., arn:aws:lightsail:global:123456789101:Domain/824cede0-abc7-4f84-8dbc-12345EXAMPLE ).

supportCode (string) --The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.

createdAt (datetime) --The date when the domain recordset was created.

location (dict) --The AWS Region and Availability Zones where the domain recordset was created.

availabilityZone (string) --The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --The AWS Region name.



resourceType (string) --The resource type.

tags (list) --The tag keys and optional values for the resource. For more information about tags in Lightsail, see the Lightsail Dev Guide .

(dict) --Describes a tag key and optional value assigned to an Amazon Lightsail resource.
For more information about tags in Lightsail, see the Lightsail Dev Guide .

key (string) --The key of the tag.
Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @

value (string) --The value of the tag.
Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @





domainEntries (list) --An array of key-value pairs containing information about the domain entries.

(dict) --Describes a domain recordset entry.

id (string) --The ID of the domain recordset entry.

name (string) --The name of the domain.

target (string) --The target AWS name server (e.g., ns-111.awsdns-22.com. ).
For Lightsail load balancers, the value looks like ab1234c56789c6b86aba6fb203d443bc-123456789.us-east-2.elb.amazonaws.com . Be sure to also set isAlias to true when setting up an A record for a load balancer.

isAlias (boolean) --When true , specifies whether the domain entry is an alias used by the Lightsail load balancer. You can include an alias (A type) record in your request, which points to a load balancer DNS name and routes traffic to your load balancer

type (string) --The type of domain entry, such as address (A), canonical name (CNAME), mail exchanger (MX), name server (NS), start of authority (SOA), service locator (SRV), or text (TXT).
The following domain entry types can be used:

A
CNAME
MX
NS
SOA
SRV
TXT


options (dict) --(Deprecated) The options for the domain entry.

Note
In releases prior to November 29, 2017, this parameter was not included in the API response. It is now deprecated.


(string) --
(string) --












nextPageToken (string) --The token to advance to the next page of resutls from your request.
A next page token is not returned if there are no more results to display.
To get the next page of results, perform another GetDomains request and specify the next page token using the pageToken parameter.






Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'domains': [
            {
                'name': 'string',
                'arn': 'string',
                'supportCode': 'string',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ],
                'domainEntries': [
                    {
                        'id': 'string',
                        'name': 'string',
                        'target': 'string',
                        'isAlias': True|False,
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
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def get_export_snapshot_records(pageToken=None):
    """
    Returns the export snapshot record created as a result of the export snapshot operation.
    An export snapshot record can be used to create a new Amazon EC2 instance and its related resources with the create cloud formation stack operation.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_export_snapshot_records(
        pageToken='string'
    )
    
    
    :type pageToken: string
    :param pageToken: The token to advance to the next page of results from your request.\nTo get a page token, perform an initial GetExportSnapshotRecords request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.\n

    :rtype: dict
ReturnsResponse Syntax{
    'exportSnapshotRecords': [
        {
            'name': 'string',
            'arn': 'string',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'state': 'Started'|'Succeeded'|'Failed',
            'sourceInfo': {
                'resourceType': 'InstanceSnapshot'|'DiskSnapshot',
                'createdAt': datetime(2015, 1, 1),
                'name': 'string',
                'arn': 'string',
                'fromResourceName': 'string',
                'fromResourceArn': 'string',
                'instanceSnapshotInfo': {
                    'fromBundleId': 'string',
                    'fromBlueprintId': 'string',
                    'fromDiskInfo': [
                        {
                            'name': 'string',
                            'path': 'string',
                            'sizeInGb': 123,
                            'isSystemDisk': True|False
                        },
                    ]
                },
                'diskSnapshotInfo': {
                    'sizeInGb': 123
                }
            },
            'destinationInfo': {
                'id': 'string',
                'service': 'string'
            }
        },
    ],
    'nextPageToken': 'string'
}


Response Structure

(dict) --
exportSnapshotRecords (list) --A list of objects describing the export snapshot records.

(dict) --Describes an export snapshot record.

name (string) --The export snapshot record name.

arn (string) --The Amazon Resource Name (ARN) of the export snapshot record.

createdAt (datetime) --The date when the export snapshot record was created.

location (dict) --The AWS Region and Availability Zone where the export snapshot record is located.

availabilityZone (string) --The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --The AWS Region name.



resourceType (string) --The Lightsail resource type (e.g., ExportSnapshotRecord ).

state (string) --The state of the export snapshot record.

sourceInfo (dict) --A list of objects describing the source of the export snapshot record.

resourceType (string) --The Lightsail resource type (e.g., InstanceSnapshot or DiskSnapshot ).

createdAt (datetime) --The date when the source instance or disk snapshot was created.

name (string) --The name of the source instance or disk snapshot.

arn (string) --The Amazon Resource Name (ARN) of the source instance or disk snapshot.

fromResourceName (string) --The name of the snapshot\'s source instance or disk.

fromResourceArn (string) --The Amazon Resource Name (ARN) of the snapshot\'s source instance or disk.

instanceSnapshotInfo (dict) --A list of objects describing an instance snapshot.

fromBundleId (string) --The bundle ID from which the source instance was created (e.g., micro_1_0 ).

fromBlueprintId (string) --The blueprint ID from which the source instance (e.g., os_debian_8_3 ).

fromDiskInfo (list) --A list of objects describing the disks that were attached to the source instance.

(dict) --Describes a disk.

name (string) --The disk name.

path (string) --The disk path.

sizeInGb (integer) --The size of the disk in GB (e.g., 32 ).

isSystemDisk (boolean) --A Boolean value indicating whether this disk is a system disk (has an operating system loaded on it).







diskSnapshotInfo (dict) --A list of objects describing a disk snapshot.

sizeInGb (integer) --The size of the disk in GB (e.g., 32 ).





destinationInfo (dict) --A list of objects describing the destination of the export snapshot record.

id (string) --The ID of the resource created at the destination.

service (string) --The destination service of the record.







nextPageToken (string) --The token to advance to the next page of resutls from your request.
A next page token is not returned if there are no more results to display.
To get the next page of results, perform another GetExportSnapshotRecords request and specify the next page token using the pageToken parameter.






Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'exportSnapshotRecords': [
            {
                'name': 'string',
                'arn': 'string',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'state': 'Started'|'Succeeded'|'Failed',
                'sourceInfo': {
                    'resourceType': 'InstanceSnapshot'|'DiskSnapshot',
                    'createdAt': datetime(2015, 1, 1),
                    'name': 'string',
                    'arn': 'string',
                    'fromResourceName': 'string',
                    'fromResourceArn': 'string',
                    'instanceSnapshotInfo': {
                        'fromBundleId': 'string',
                        'fromBlueprintId': 'string',
                        'fromDiskInfo': [
                            {
                                'name': 'string',
                                'path': 'string',
                                'sizeInGb': 123,
                                'isSystemDisk': True|False
                            },
                        ]
                    },
                    'diskSnapshotInfo': {
                        'sizeInGb': 123
                    }
                },
                'destinationInfo': {
                    'id': 'string',
                    'service': 'string'
                }
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
    
    Exceptions
    
    :example: response = client.get_instance(
        instanceName='string'
    )
    
    
    :type instanceName: string
    :param instanceName: [REQUIRED]\nThe name of the instance.\n

    :rtype: dict
ReturnsResponse Syntax{
    'instance': {
        'name': 'string',
        'arn': 'string',
        'supportCode': 'string',
        'createdAt': datetime(2015, 1, 1),
        'location': {
            'availabilityZone': 'string',
            'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
        },
        'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
        'tags': [
            {
                'key': 'string',
                'value': 'string'
            },
        ],
        'blueprintId': 'string',
        'blueprintName': 'string',
        'bundleId': 'string',
        'addOns': [
            {
                'name': 'string',
                'status': 'string',
                'snapshotTimeOfDay': 'string',
                'nextSnapshotTimeOfDay': 'string'
            },
        ],
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
                        'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                    },
                    'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                    'tags': [
                        {
                            'key': 'string',
                            'value': 'string'
                        },
                    ],
                    'addOns': [
                        {
                            'name': 'string',
                            'status': 'string',
                            'snapshotTimeOfDay': 'string',
                            'nextSnapshotTimeOfDay': 'string'
                        },
                    ],
                    'sizeInGb': 123,
                    'isSystemDisk': True|False,
                    'iops': 123,
                    'path': 'string',
                    'state': 'pending'|'error'|'available'|'in-use'|'unknown',
                    'attachedTo': 'string',
                    'isAttached': True|False,
                    'attachmentState': 'string',
                    'gbInUse': 123
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
                    'protocol': 'tcp'|'all'|'udp'|'icmp',
                    'accessFrom': 'string',
                    'accessType': 'Public'|'Private',
                    'commonName': 'string',
                    'accessDirection': 'inbound'|'outbound',
                    'cidrs': [
                        'string',
                    ],
                    'cidrListAliases': [
                        'string',
                    ]
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


Response Structure

(dict) --
instance (dict) --An array of key-value pairs containing information about the specified instance.

name (string) --The name the user gave the instance (e.g., Amazon_Linux-1GB-Ohio-1 ).

arn (string) --The Amazon Resource Name (ARN) of the instance (e.g., arn:aws:lightsail:us-east-2:123456789101:Instance/244ad76f-8aad-4741-809f-12345EXAMPLE ).

supportCode (string) --The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.

createdAt (datetime) --The timestamp when the instance was created (e.g., 1479734909.17 ).

location (dict) --The region name and Availability Zone where the instance is located.

availabilityZone (string) --The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --The AWS Region name.



resourceType (string) --The type of resource (usually Instance ).

tags (list) --The tag keys and optional values for the resource. For more information about tags in Lightsail, see the Lightsail Dev Guide .

(dict) --Describes a tag key and optional value assigned to an Amazon Lightsail resource.
For more information about tags in Lightsail, see the Lightsail Dev Guide .

key (string) --The key of the tag.
Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @

value (string) --The value of the tag.
Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @





blueprintId (string) --The blueprint ID (e.g., os_amlinux_2016_03 ).

blueprintName (string) --The friendly name of the blueprint (e.g., Amazon Linux ).

bundleId (string) --The bundle for the instance (e.g., micro_1_0 ).

addOns (list) --An array of objects representing the add-ons enabled on the instance.

(dict) --Describes an add-on that is enabled for an Amazon Lightsail resource.

name (string) --The name of the add-on.

status (string) --The status of the add-on.

snapshotTimeOfDay (string) --The daily time when an automatic snapshot is created.
The time shown is in HH:00 format, and in Coordinated Universal Time (UTC).
The snapshot is automatically created between the time shown and up to 45 minutes after.

nextSnapshotTimeOfDay (string) --The next daily time an automatic snapshot will be created.
The time shown is in HH:00 format, and in Coordinated Universal Time (UTC).
The snapshot is automatically created between the time shown and up to 45 minutes after.





isStaticIp (boolean) --A Boolean value indicating whether this instance has a static IP assigned to it.

privateIpAddress (string) --The private IP address of the instance.

publicIpAddress (string) --The public IP address of the instance.

ipv6Address (string) --The IPv6 address of the instance.

hardware (dict) --The size of the vCPU and the amount of RAM for the instance.

cpuCount (integer) --The number of vCPUs the instance has.

disks (list) --The disks attached to the instance.

(dict) --Describes a system disk or a block storage disk.

name (string) --The unique name of the disk.

arn (string) --The Amazon Resource Name (ARN) of the disk.

supportCode (string) --The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.

createdAt (datetime) --The date when the disk was created.

location (dict) --The AWS Region and Availability Zone where the disk is located.

availabilityZone (string) --The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --The AWS Region name.



resourceType (string) --The Lightsail resource type (e.g., Disk ).

tags (list) --The tag keys and optional values for the resource. For more information about tags in Lightsail, see the Lightsail Dev Guide .

(dict) --Describes a tag key and optional value assigned to an Amazon Lightsail resource.
For more information about tags in Lightsail, see the Lightsail Dev Guide .

key (string) --The key of the tag.
Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @

value (string) --The value of the tag.
Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @





addOns (list) --An array of objects representing the add-ons enabled on the disk.

(dict) --Describes an add-on that is enabled for an Amazon Lightsail resource.

name (string) --The name of the add-on.

status (string) --The status of the add-on.

snapshotTimeOfDay (string) --The daily time when an automatic snapshot is created.
The time shown is in HH:00 format, and in Coordinated Universal Time (UTC).
The snapshot is automatically created between the time shown and up to 45 minutes after.

nextSnapshotTimeOfDay (string) --The next daily time an automatic snapshot will be created.
The time shown is in HH:00 format, and in Coordinated Universal Time (UTC).
The snapshot is automatically created between the time shown and up to 45 minutes after.





sizeInGb (integer) --The size of the disk in GB.

isSystemDisk (boolean) --A Boolean value indicating whether this disk is a system disk (has an operating system loaded on it).

iops (integer) --The input/output operations per second (IOPS) of the disk.

path (string) --The disk path.

state (string) --Describes the status of the disk.

attachedTo (string) --The resources to which the disk is attached.

isAttached (boolean) --A Boolean value indicating whether the disk is attached.

attachmentState (string) --(Deprecated) The attachment state of the disk.

Note
In releases prior to November 14, 2017, this parameter returned attached for system disks in the API response. It is now deprecated, but still included in the response. Use isAttached instead.


gbInUse (integer) --(Deprecated) The number of GB in use by the disk.

Note
In releases prior to November 14, 2017, this parameter was not included in the API response. It is now deprecated.






ramSizeInGb (float) --The amount of RAM in GB on the instance (e.g., 1.0 ).



networking (dict) --Information about the public ports and monthly data transfer rates for the instance.

monthlyTransfer (dict) --The amount of data in GB allocated for monthly data transfers.

gbPerMonthAllocated (integer) --The amount allocated per month (in GB).



ports (list) --An array of key-value pairs containing information about the ports on the instance.

(dict) --Describes information about ports for an Amazon Lightsail instance.

fromPort (integer) --The first port in a range of open ports on an instance.
Allowed ports:

TCP and UDP - 0 to 65535
ICMP - 8 (to configure Ping)


Note
Ping is the only communication supported through the ICMP protocol in Lightsail. To configure ping, specify the fromPort parameter as 8 , and the toPort parameter as -1 .


toPort (integer) --The last port in a range of open ports on an instance.
Allowed ports:

TCP and UDP - 0 to 65535
ICMP - -1 (to configure Ping)


Note
Ping is the only communication supported through the ICMP protocol in Lightsail. To configure ping, specify the fromPort parameter as 8 , and the toPort parameter as -1 .


protocol (string) --The IP protocol name.
The name can be one of the following:

tcp - Transmission Control Protocol (TCP) provides reliable, ordered, and error-checked delivery of streamed data between applications running on hosts communicating by an IP network. If you have an application that doesn\'t require reliable data stream service, use UDP instead.
all - All transport layer protocol types. For more general information, see Transport layer on Wikipedia .
udp - With User Datagram Protocol (UDP), computer applications can send messages (or datagrams) to other hosts on an Internet Protocol (IP) network. Prior communications are not required to set up transmission channels or data paths. Applications that don\'t require reliable data stream service can use UDP, which provides a connectionless datagram service that emphasizes reduced latency over reliability. If you do require reliable data stream service, use TCP instead.
icmp - Internet Control Message Protocol (ICMP) is used to send error messages and operational information indicating success or failure when communicating with an instance. For example, an error is indicated when an instance could not be reached.


Note
Ping is the only communication supported through the ICMP protocol in Lightsail. To configure ping, specify the fromPort parameter as 8 , and the toPort parameter as -1 .


accessFrom (string) --The location from which access is allowed. For example, Anywhere (0.0.0.0/0) , or Custom if a specific IP address or range of IP addresses is allowed.

accessType (string) --The type of access (Public or Private ).

commonName (string) --The common name of the port information.

accessDirection (string) --The access direction (inbound or outbound ).

Note
Lightsail currently supports only inbound access direction.


cidrs (list) --The IP address, or range of IP addresses in CIDR notation, that are allowed to connect to an instance through the ports, and the protocol. Lightsail supports IPv4 addresses.
For more information about CIDR block notation, see Classless Inter-Domain Routing on Wikipedia .

(string) --


cidrListAliases (list) --An alias that defines access for a preconfigured range of IP addresses.
The only alias currently supported is lightsail-connect , which allows IP addresses of the browser-based RDP/SSH client in the Lightsail console to connect to your instance.

(string) --








state (dict) --The status code and the state (e.g., running ) for the instance.

code (integer) --The status code for the instance.

name (string) --The state of the instance (e.g., running or pending ).



username (string) --The user name for connecting to the instance (e.g., ec2-user ).

sshKeyName (string) --The name of the SSH key being used to connect to the instance (e.g., LightsailDefaultKeyPair ).








Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'instance': {
            'name': 'string',
            'arn': 'string',
            'supportCode': 'string',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ],
            'blueprintId': 'string',
            'blueprintName': 'string',
            'bundleId': 'string',
            'addOns': [
                {
                    'name': 'string',
                    'status': 'string',
                    'snapshotTimeOfDay': 'string',
                    'nextSnapshotTimeOfDay': 'string'
                },
            ],
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
                            'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                        },
                        'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                        'tags': [
                            {
                                'key': 'string',
                                'value': 'string'
                            },
                        ],
                        'addOns': [
                            {
                                'name': 'string',
                                'status': 'string',
                                'snapshotTimeOfDay': 'string',
                                'nextSnapshotTimeOfDay': 'string'
                            },
                        ],
                        'sizeInGb': 123,
                        'isSystemDisk': True|False,
                        'iops': 123,
                        'path': 'string',
                        'state': 'pending'|'error'|'available'|'in-use'|'unknown',
                        'attachedTo': 'string',
                        'isAttached': True|False,
                        'attachmentState': 'string',
                        'gbInUse': 123
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
                        'protocol': 'tcp'|'all'|'udp'|'icmp',
                        'accessFrom': 'string',
                        'accessType': 'Public'|'Private',
                        'commonName': 'string',
                        'accessDirection': 'inbound'|'outbound',
                        'cidrs': [
                            'string',
                        ],
                        'cidrListAliases': [
                            'string',
                        ]
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
    
    
    :returns: 
    TCP and UDP - 0 to 65535
    ICMP - -1 (to configure Ping)
    
    """
    pass

def get_instance_access_details(instanceName=None, protocol=None):
    """
    Returns temporary SSH keys you can use to connect to a specific virtual private server, or instance .
    The get instance access details operation supports tag-based access control via resource tags applied to the resource identified by instance name . For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_instance_access_details(
        instanceName='string',
        protocol='ssh'|'rdp'
    )
    
    
    :type instanceName: string
    :param instanceName: [REQUIRED]\nThe name of the instance to access.\n

    :type protocol: string
    :param protocol: The protocol to use to connect to your instance. Defaults to ssh .

    :rtype: dict

ReturnsResponse Syntax
{
    'accessDetails': {
        'certKey': 'string',
        'expiresAt': datetime(2015, 1, 1),
        'ipAddress': 'string',
        'password': 'string',
        'passwordData': {
            'ciphertext': 'string',
            'keyPairName': 'string'
        },
        'privateKey': 'string',
        'protocol': 'ssh'|'rdp',
        'instanceName': 'string',
        'username': 'string',
        'hostKeys': [
            {
                'algorithm': 'string',
                'publicKey': 'string',
                'witnessedAt': datetime(2015, 1, 1),
                'fingerprintSHA1': 'string',
                'fingerprintSHA256': 'string',
                'notValidBefore': datetime(2015, 1, 1),
                'notValidAfter': datetime(2015, 1, 1)
            },
        ]
    }
}


Response Structure

(dict) --

accessDetails (dict) --
An array of key-value pairs containing information about a get instance access request.

certKey (string) --
For SSH access, the public key to use when accessing your instance For OpenSSH clients (e.g., command line SSH), you should save this value to tempkey-cert.pub .

expiresAt (datetime) --
For SSH access, the date on which the temporary keys expire.

ipAddress (string) --
The public IP address of the Amazon Lightsail instance.

password (string) --
For RDP access, the password for your Amazon Lightsail instance. Password will be an empty string if the password for your new instance is not ready yet. When you create an instance, it can take up to 15 minutes for the instance to be ready.

Note
If you create an instance using any key pair other than the default (LightsailDefaultKeyPair ), password will always be an empty string.
If you change the Administrator password on the instance, Lightsail will continue to return the original password value. When accessing the instance using RDP, you need to manually enter the Administrator password after changing it from the default.


passwordData (dict) --
For a Windows Server-based instance, an object with the data you can use to retrieve your password. This is only needed if password is empty and the instance is not new (and therefore the password is not ready yet). When you create an instance, it can take up to 15 minutes for the instance to be ready.

ciphertext (string) --
The encrypted password. Ciphertext will be an empty string if access to your new instance is not ready yet. When you create an instance, it can take up to 15 minutes for the instance to be ready.

Note
If you use the default key pair (LightsailDefaultKeyPair ), the decrypted password will be available in the password field.
If you are using a custom key pair, you need to use your own means of decryption.
If you change the Administrator password on the instance, Lightsail will continue to return the original ciphertext value. When accessing the instance using RDP, you need to manually enter the Administrator password after changing it from the default.


keyPairName (string) --
The name of the key pair that you used when creating your instance. If no key pair name was specified when creating the instance, Lightsail uses the default key pair (LightsailDefaultKeyPair ).
If you are using a custom key pair, you need to use your own means of decrypting your password using the ciphertext . Lightsail creates the ciphertext by encrypting your password with the public key part of this key pair.



privateKey (string) --
For SSH access, the temporary private key. For OpenSSH clients (e.g., command line SSH), you should save this value to tempkey ).

protocol (string) --
The protocol for these Amazon Lightsail instance access details.

instanceName (string) --
The name of this Amazon Lightsail instance.

username (string) --
The user name to use when logging in to the Amazon Lightsail instance.

hostKeys (list) --
Describes the public SSH host keys or the RDP certificate.

(dict) --
Describes the public SSH host keys or the RDP certificate.

algorithm (string) --
The SSH host key algorithm or the RDP certificate format.
For SSH host keys, the algorithm may be ssh-rsa , ecdsa-sha2-nistp256 , ssh-ed25519 , etc. For RDP certificates, the algorithm is always x509-cert .

publicKey (string) --
The public SSH host key or the RDP certificate.

witnessedAt (datetime) --
The time that the SSH host key or RDP certificate was recorded by Lightsail.

fingerprintSHA1 (string) --
The SHA-1 fingerprint of the returned SSH host key or RDP certificate.

Example of an SHA-1 SSH fingerprint:  SHA1:1CHH6FaAaXjtFOsR/t83vf91SR0
Example of an SHA-1 RDP fingerprint:  af:34:51:fe:09:f0:e0:da:b8:4e:56:ca:60:c2:10:ff:38:06:db:45


fingerprintSHA256 (string) --
The SHA-256 fingerprint of the returned SSH host key or RDP certificate.

Example of an SHA-256 SSH fingerprint:  SHA256:KTsMnRBh1IhD17HpdfsbzeGA4jOijm5tyXsMjKVbB8o
Example of an SHA-256 RDP fingerprint:  03:9b:36:9f:4b:de:4e:61:70:fc:7c:c9:78:e7:d2:1a:1c:25:a8:0c:91:f6:7c:e4:d6:a0:85:c8:b4:53:99:68


notValidBefore (datetime) --
The returned RDP certificate is valid after this point in time.
This value is listed only for RDP certificates.

notValidAfter (datetime) --
The returned RDP certificate is not valid after this point in time.
This value is listed only for RDP certificates.













Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'accessDetails': {
            'certKey': 'string',
            'expiresAt': datetime(2015, 1, 1),
            'ipAddress': 'string',
            'password': 'string',
            'passwordData': {
                'ciphertext': 'string',
                'keyPairName': 'string'
            },
            'privateKey': 'string',
            'protocol': 'ssh'|'rdp',
            'instanceName': 'string',
            'username': 'string',
            'hostKeys': [
                {
                    'algorithm': 'string',
                    'publicKey': 'string',
                    'witnessedAt': datetime(2015, 1, 1),
                    'fingerprintSHA1': 'string',
                    'fingerprintSHA256': 'string',
                    'notValidBefore': datetime(2015, 1, 1),
                    'notValidAfter': datetime(2015, 1, 1)
                },
            ]
        }
    }
    
    
    :returns: 
    Example of an SHA-1 SSH fingerprint:  SHA1:1CHH6FaAaXjtFOsR/t83vf91SR0
    Example of an SHA-1 RDP fingerprint:  af:34:51:fe:09:f0:e0:da:b8:4e:56:ca:60:c2:10:ff:38:06:db:45
    
    """
    pass

def get_instance_metric_data(instanceName=None, metricName=None, period=None, startTime=None, endTime=None, unit=None, statistics=None):
    """
    Returns the data points for the specified Amazon Lightsail instance metric, given an instance name.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param instanceName: [REQUIRED]\nThe name of the instance for which you want to get metrics data.\n

    :type metricName: string
    :param metricName: [REQUIRED]\nThe metric for which you want to return information.\nValid instance metric names are listed below, along with the most useful statistics to include in your request, and the published unit value.\n\n**CPUUtilization ** - The percentage of allocated compute units that are currently in use on the instance. This metric identifies the processing power to run the applications on the instance. Tools in your operating system can show a lower percentage than Lightsail when the instance is not allocated a full processor core. Statistics : The most useful statistics are Maximum and Average . Unit : The published unit is Percent .\n**NetworkIn ** - The number of bytes received on all network interfaces by the instance. This metric identifies the volume of incoming network traffic to the instance. The number reported is the number of bytes received during the period. Because this metric is reported in 5-minute intervals, divide the reported number by 300 to find Bytes/second. Statistics : The most useful statistic is Sum . Unit : The published unit is Bytes .\n**NetworkOut ** - The number of bytes sent out on all network interfaces by the instance. This metric identifies the volume of outgoing network traffic from the instance. The number reported is the number of bytes sent during the period. Because this metric is reported in 5-minute intervals, divide the reported number by 300 to find Bytes/second. Statistics : The most useful statistic is Sum . Unit : The published unit is Bytes .\n**StatusCheckFailed ** - Reports whether the instance passed or failed both the instance status check and the system status check. This metric can be either 0 (passed) or 1 (failed). This metric data is available in 1-minute (60 seconds) granularity. Statistics : The most useful statistic is Sum . Unit : The published unit is Count .\n**StatusCheckFailed_Instance ** - Reports whether the instance passed or failed the instance status check. This metric can be either 0 (passed) or 1 (failed). This metric data is available in 1-minute (60 seconds) granularity. Statistics : The most useful statistic is Sum . Unit : The published unit is Count .\n**StatusCheckFailed_System ** - Reports whether the instance passed or failed the system status check. This metric can be either 0 (passed) or 1 (failed). This metric data is available in 1-minute (60 seconds) granularity. Statistics : The most useful statistic is Sum . Unit : The published unit is Count .\n\n

    :type period: integer
    :param period: [REQUIRED]\nThe granularity, in seconds, of the returned data points.\nThe StatusCheckFailed , StatusCheckFailed_Instance , and StatusCheckFailed_System instance metric data is available in 1-minute (60 seconds) granularity. All other instance metric data is available in 5-minute (300 seconds) granularity.\n

    :type startTime: datetime
    :param startTime: [REQUIRED]\nThe start time of the time period.\n

    :type endTime: datetime
    :param endTime: [REQUIRED]\nThe end time of the time period.\n

    :type unit: string
    :param unit: [REQUIRED]\nThe unit for the metric data request. Valid units depend on the metric data being requested. For the valid units to specify with each available metric, see the metricName parameter.\n

    :type statistics: list
    :param statistics: [REQUIRED]\nThe statistic for the metric.\nThe following statistics are available:\n\nMinimum - The lowest value observed during the specified period. Use this value to determine low volumes of activity for your application.\nMaximum - The highest value observed during the specified period. Use this value to determine high volumes of activity for your application.\nSum - All values submitted for the matching metric added together. You can use this statistic to determine the total volume of a metric.\nAverage - The value of Sum / SampleCount during the specified period. By comparing this statistic with the Minimum and Maximum values, you can determine the full scope of a metric and how close the average use is to the Minimum and Maximum values. This comparison helps you to know when to increase or decrease your resources.\nSampleCount - The count, or number, of data points used for the statistical calculation.\n\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

metricName (string) --
The metric name to return data for.

metricData (list) --
An array of key-value pairs containing information about the results of your get instance metric data request.

(dict) --
Describes the metric data point.

average (float) --
The average.

maximum (float) --
The maximum.

minimum (float) --
The minimum.

sampleCount (float) --
The sample count.

sum (float) --
The sum.

timestamp (datetime) --
The timestamp (e.g., 1479816991.349 ).

unit (string) --
The unit.











Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


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
    
    
    :returns: 
    Lightsail.Client.exceptions.ServiceException
    Lightsail.Client.exceptions.InvalidInputException
    Lightsail.Client.exceptions.NotFoundException
    Lightsail.Client.exceptions.OperationFailureException
    Lightsail.Client.exceptions.AccessDeniedException
    Lightsail.Client.exceptions.AccountSetupInProgressException
    Lightsail.Client.exceptions.UnauthenticatedException
    
    """
    pass

def get_instance_port_states(instanceName=None):
    """
    Returns the firewall port states for a specific Amazon Lightsail instance, the IP addresses allowed to connect to the instance through the ports, and the protocol.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_instance_port_states(
        instanceName='string'
    )
    
    
    :type instanceName: string
    :param instanceName: [REQUIRED]\nThe name of the instance for which to return firewall port states.\n

    :rtype: dict
ReturnsResponse Syntax{
    'portStates': [
        {
            'fromPort': 123,
            'toPort': 123,
            'protocol': 'tcp'|'all'|'udp'|'icmp',
            'state': 'open'|'closed',
            'cidrs': [
                'string',
            ],
            'cidrListAliases': [
                'string',
            ]
        },
    ]
}


Response Structure

(dict) --
portStates (list) --An array of objects that describe the firewall port states for the specified instance.

(dict) --Describes open ports on an instance, the IP addresses allowed to connect to the instance through the ports, and the protocol.

fromPort (integer) --The first port in a range of open ports on an instance.
Allowed ports:

TCP and UDP - 0 to 65535
ICMP - 8 (to configure Ping)


Note
Ping is the only communication supported through the ICMP protocol in Lightsail. To configure ping, specify the fromPort parameter as 8 , and the toPort parameter as -1 .


toPort (integer) --The last port in a range of open ports on an instance.
Allowed ports:

TCP and UDP - 0 to 65535
ICMP - -1 (to configure Ping)


Note
Ping is the only communication supported through the ICMP protocol in Lightsail. To configure ping, specify the fromPort parameter as 8 , and the toPort parameter as -1 .


protocol (string) --The IP protocol name.
The name can be one of the following:

tcp - Transmission Control Protocol (TCP) provides reliable, ordered, and error-checked delivery of streamed data between applications running on hosts communicating by an IP network. If you have an application that doesn\'t require reliable data stream service, use UDP instead.
all - All transport layer protocol types. For more general information, see Transport layer on Wikipedia .
udp - With User Datagram Protocol (UDP), computer applications can send messages (or datagrams) to other hosts on an Internet Protocol (IP) network. Prior communications are not required to set up transmission channels or data paths. Applications that don\'t require reliable data stream service can use UDP, which provides a connectionless datagram service that emphasizes reduced latency over reliability. If you do require reliable data stream service, use TCP instead.
icmp - Internet Control Message Protocol (ICMP) is used to send error messages and operational information indicating success or failure when communicating with an instance. For example, an error is indicated when an instance could not be reached.


Note
Ping is the only communication supported through the ICMP protocol in Lightsail. To configure ping, specify the fromPort parameter as 8 , and the toPort parameter as -1 .


state (string) --Specifies whether the instance port is open or closed .

Note
The port state for Lightsail instances is always open .


cidrs (list) --The IP address, or range of IP addresses in CIDR notation, that are allowed to connect to an instance through the ports, and the protocol. Lightsail supports IPv4 addresses.
For more information about CIDR block notation, see Classless Inter-Domain Routing on Wikipedia .

(string) --


cidrListAliases (list) --An alias that defines access for a preconfigured range of IP addresses.
The only alias currently supported is lightsail-connect , which allows IP addresses of the browser-based RDP/SSH client in the Lightsail console to connect to your instance.

(string) --











Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'portStates': [
            {
                'fromPort': 123,
                'toPort': 123,
                'protocol': 'tcp'|'all'|'udp'|'icmp',
                'state': 'open'|'closed',
                'cidrs': [
                    'string',
                ],
                'cidrListAliases': [
                    'string',
                ]
            },
        ]
    }
    
    
    :returns: 
    TCP and UDP - 0 to 65535
    ICMP - -1 (to configure Ping)
    
    """
    pass

def get_instance_snapshot(instanceSnapshotName=None):
    """
    Returns information about a specific instance snapshot.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_instance_snapshot(
        instanceSnapshotName='string'
    )
    
    
    :type instanceSnapshotName: string
    :param instanceSnapshotName: [REQUIRED]\nThe name of the snapshot for which you are requesting information.\n

    :rtype: dict
ReturnsResponse Syntax{
    'instanceSnapshot': {
        'name': 'string',
        'arn': 'string',
        'supportCode': 'string',
        'createdAt': datetime(2015, 1, 1),
        'location': {
            'availabilityZone': 'string',
            'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
        },
        'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
        'tags': [
            {
                'key': 'string',
                'value': 'string'
            },
        ],
        'state': 'pending'|'error'|'available',
        'progress': 'string',
        'fromAttachedDisks': [
            {
                'name': 'string',
                'arn': 'string',
                'supportCode': 'string',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ],
                'addOns': [
                    {
                        'name': 'string',
                        'status': 'string',
                        'snapshotTimeOfDay': 'string',
                        'nextSnapshotTimeOfDay': 'string'
                    },
                ],
                'sizeInGb': 123,
                'isSystemDisk': True|False,
                'iops': 123,
                'path': 'string',
                'state': 'pending'|'error'|'available'|'in-use'|'unknown',
                'attachedTo': 'string',
                'isAttached': True|False,
                'attachmentState': 'string',
                'gbInUse': 123
            },
        ],
        'fromInstanceName': 'string',
        'fromInstanceArn': 'string',
        'fromBlueprintId': 'string',
        'fromBundleId': 'string',
        'isFromAutoSnapshot': True|False,
        'sizeInGb': 123
    }
}


Response Structure

(dict) --
instanceSnapshot (dict) --An array of key-value pairs containing information about the results of your get instance snapshot request.

name (string) --The name of the snapshot.

arn (string) --The Amazon Resource Name (ARN) of the snapshot (e.g., arn:aws:lightsail:us-east-2:123456789101:InstanceSnapshot/d23b5706-3322-4d83-81e5-12345EXAMPLE ).

supportCode (string) --The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.

createdAt (datetime) --The timestamp when the snapshot was created (e.g., 1479907467.024 ).

location (dict) --The region name and Availability Zone where you created the snapshot.

availabilityZone (string) --The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --The AWS Region name.



resourceType (string) --The type of resource (usually InstanceSnapshot ).

tags (list) --The tag keys and optional values for the resource. For more information about tags in Lightsail, see the Lightsail Dev Guide .

(dict) --Describes a tag key and optional value assigned to an Amazon Lightsail resource.
For more information about tags in Lightsail, see the Lightsail Dev Guide .

key (string) --The key of the tag.
Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @

value (string) --The value of the tag.
Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @





state (string) --The state the snapshot is in.

progress (string) --The progress of the snapshot.

fromAttachedDisks (list) --An array of disk objects containing information about all block storage disks.

(dict) --Describes a system disk or a block storage disk.

name (string) --The unique name of the disk.

arn (string) --The Amazon Resource Name (ARN) of the disk.

supportCode (string) --The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.

createdAt (datetime) --The date when the disk was created.

location (dict) --The AWS Region and Availability Zone where the disk is located.

availabilityZone (string) --The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --The AWS Region name.



resourceType (string) --The Lightsail resource type (e.g., Disk ).

tags (list) --The tag keys and optional values for the resource. For more information about tags in Lightsail, see the Lightsail Dev Guide .

(dict) --Describes a tag key and optional value assigned to an Amazon Lightsail resource.
For more information about tags in Lightsail, see the Lightsail Dev Guide .

key (string) --The key of the tag.
Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @

value (string) --The value of the tag.
Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @





addOns (list) --An array of objects representing the add-ons enabled on the disk.

(dict) --Describes an add-on that is enabled for an Amazon Lightsail resource.

name (string) --The name of the add-on.

status (string) --The status of the add-on.

snapshotTimeOfDay (string) --The daily time when an automatic snapshot is created.
The time shown is in HH:00 format, and in Coordinated Universal Time (UTC).
The snapshot is automatically created between the time shown and up to 45 minutes after.

nextSnapshotTimeOfDay (string) --The next daily time an automatic snapshot will be created.
The time shown is in HH:00 format, and in Coordinated Universal Time (UTC).
The snapshot is automatically created between the time shown and up to 45 minutes after.





sizeInGb (integer) --The size of the disk in GB.

isSystemDisk (boolean) --A Boolean value indicating whether this disk is a system disk (has an operating system loaded on it).

iops (integer) --The input/output operations per second (IOPS) of the disk.

path (string) --The disk path.

state (string) --Describes the status of the disk.

attachedTo (string) --The resources to which the disk is attached.

isAttached (boolean) --A Boolean value indicating whether the disk is attached.

attachmentState (string) --(Deprecated) The attachment state of the disk.

Note
In releases prior to November 14, 2017, this parameter returned attached for system disks in the API response. It is now deprecated, but still included in the response. Use isAttached instead.


gbInUse (integer) --(Deprecated) The number of GB in use by the disk.

Note
In releases prior to November 14, 2017, this parameter was not included in the API response. It is now deprecated.






fromInstanceName (string) --The instance from which the snapshot was created.

fromInstanceArn (string) --The Amazon Resource Name (ARN) of the instance from which the snapshot was created (e.g., arn:aws:lightsail:us-east-2:123456789101:Instance/64b8404c-ccb1-430b-8daf-12345EXAMPLE ).

fromBlueprintId (string) --The blueprint ID from which you created the snapshot (e.g., os_debian_8_3 ). A blueprint is a virtual private server (or instance ) image used to create instances quickly.

fromBundleId (string) --The bundle ID from which you created the snapshot (e.g., micro_1_0 ).

isFromAutoSnapshot (boolean) --A Boolean value indicating whether the snapshot was created from an automatic snapshot.

sizeInGb (integer) --The size in GB of the SSD.








Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'instanceSnapshot': {
            'name': 'string',
            'arn': 'string',
            'supportCode': 'string',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ],
            'state': 'pending'|'error'|'available',
            'progress': 'string',
            'fromAttachedDisks': [
                {
                    'name': 'string',
                    'arn': 'string',
                    'supportCode': 'string',
                    'createdAt': datetime(2015, 1, 1),
                    'location': {
                        'availabilityZone': 'string',
                        'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                    },
                    'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                    'tags': [
                        {
                            'key': 'string',
                            'value': 'string'
                        },
                    ],
                    'addOns': [
                        {
                            'name': 'string',
                            'status': 'string',
                            'snapshotTimeOfDay': 'string',
                            'nextSnapshotTimeOfDay': 'string'
                        },
                    ],
                    'sizeInGb': 123,
                    'isSystemDisk': True|False,
                    'iops': 123,
                    'path': 'string',
                    'state': 'pending'|'error'|'available'|'in-use'|'unknown',
                    'attachedTo': 'string',
                    'isAttached': True|False,
                    'attachmentState': 'string',
                    'gbInUse': 123
                },
            ],
            'fromInstanceName': 'string',
            'fromInstanceArn': 'string',
            'fromBlueprintId': 'string',
            'fromBundleId': 'string',
            'isFromAutoSnapshot': True|False,
            'sizeInGb': 123
        }
    }
    
    
    """
    pass

def get_instance_snapshots(pageToken=None):
    """
    Returns all instance snapshots for the user\'s account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_instance_snapshots(
        pageToken='string'
    )
    
    
    :type pageToken: string
    :param pageToken: The token to advance to the next page of results from your request.\nTo get a page token, perform an initial GetInstanceSnapshots request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.\n

    :rtype: dict
ReturnsResponse Syntax{
    'instanceSnapshots': [
        {
            'name': 'string',
            'arn': 'string',
            'supportCode': 'string',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ],
            'state': 'pending'|'error'|'available',
            'progress': 'string',
            'fromAttachedDisks': [
                {
                    'name': 'string',
                    'arn': 'string',
                    'supportCode': 'string',
                    'createdAt': datetime(2015, 1, 1),
                    'location': {
                        'availabilityZone': 'string',
                        'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                    },
                    'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                    'tags': [
                        {
                            'key': 'string',
                            'value': 'string'
                        },
                    ],
                    'addOns': [
                        {
                            'name': 'string',
                            'status': 'string',
                            'snapshotTimeOfDay': 'string',
                            'nextSnapshotTimeOfDay': 'string'
                        },
                    ],
                    'sizeInGb': 123,
                    'isSystemDisk': True|False,
                    'iops': 123,
                    'path': 'string',
                    'state': 'pending'|'error'|'available'|'in-use'|'unknown',
                    'attachedTo': 'string',
                    'isAttached': True|False,
                    'attachmentState': 'string',
                    'gbInUse': 123
                },
            ],
            'fromInstanceName': 'string',
            'fromInstanceArn': 'string',
            'fromBlueprintId': 'string',
            'fromBundleId': 'string',
            'isFromAutoSnapshot': True|False,
            'sizeInGb': 123
        },
    ],
    'nextPageToken': 'string'
}


Response Structure

(dict) --
instanceSnapshots (list) --An array of key-value pairs containing information about the results of your get instance snapshots request.

(dict) --Describes an instance snapshot.

name (string) --The name of the snapshot.

arn (string) --The Amazon Resource Name (ARN) of the snapshot (e.g., arn:aws:lightsail:us-east-2:123456789101:InstanceSnapshot/d23b5706-3322-4d83-81e5-12345EXAMPLE ).

supportCode (string) --The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.

createdAt (datetime) --The timestamp when the snapshot was created (e.g., 1479907467.024 ).

location (dict) --The region name and Availability Zone where you created the snapshot.

availabilityZone (string) --The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --The AWS Region name.



resourceType (string) --The type of resource (usually InstanceSnapshot ).

tags (list) --The tag keys and optional values for the resource. For more information about tags in Lightsail, see the Lightsail Dev Guide .

(dict) --Describes a tag key and optional value assigned to an Amazon Lightsail resource.
For more information about tags in Lightsail, see the Lightsail Dev Guide .

key (string) --The key of the tag.
Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @

value (string) --The value of the tag.
Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @





state (string) --The state the snapshot is in.

progress (string) --The progress of the snapshot.

fromAttachedDisks (list) --An array of disk objects containing information about all block storage disks.

(dict) --Describes a system disk or a block storage disk.

name (string) --The unique name of the disk.

arn (string) --The Amazon Resource Name (ARN) of the disk.

supportCode (string) --The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.

createdAt (datetime) --The date when the disk was created.

location (dict) --The AWS Region and Availability Zone where the disk is located.

availabilityZone (string) --The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --The AWS Region name.



resourceType (string) --The Lightsail resource type (e.g., Disk ).

tags (list) --The tag keys and optional values for the resource. For more information about tags in Lightsail, see the Lightsail Dev Guide .

(dict) --Describes a tag key and optional value assigned to an Amazon Lightsail resource.
For more information about tags in Lightsail, see the Lightsail Dev Guide .

key (string) --The key of the tag.
Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @

value (string) --The value of the tag.
Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @





addOns (list) --An array of objects representing the add-ons enabled on the disk.

(dict) --Describes an add-on that is enabled for an Amazon Lightsail resource.

name (string) --The name of the add-on.

status (string) --The status of the add-on.

snapshotTimeOfDay (string) --The daily time when an automatic snapshot is created.
The time shown is in HH:00 format, and in Coordinated Universal Time (UTC).
The snapshot is automatically created between the time shown and up to 45 minutes after.

nextSnapshotTimeOfDay (string) --The next daily time an automatic snapshot will be created.
The time shown is in HH:00 format, and in Coordinated Universal Time (UTC).
The snapshot is automatically created between the time shown and up to 45 minutes after.





sizeInGb (integer) --The size of the disk in GB.

isSystemDisk (boolean) --A Boolean value indicating whether this disk is a system disk (has an operating system loaded on it).

iops (integer) --The input/output operations per second (IOPS) of the disk.

path (string) --The disk path.

state (string) --Describes the status of the disk.

attachedTo (string) --The resources to which the disk is attached.

isAttached (boolean) --A Boolean value indicating whether the disk is attached.

attachmentState (string) --(Deprecated) The attachment state of the disk.

Note
In releases prior to November 14, 2017, this parameter returned attached for system disks in the API response. It is now deprecated, but still included in the response. Use isAttached instead.


gbInUse (integer) --(Deprecated) The number of GB in use by the disk.

Note
In releases prior to November 14, 2017, this parameter was not included in the API response. It is now deprecated.






fromInstanceName (string) --The instance from which the snapshot was created.

fromInstanceArn (string) --The Amazon Resource Name (ARN) of the instance from which the snapshot was created (e.g., arn:aws:lightsail:us-east-2:123456789101:Instance/64b8404c-ccb1-430b-8daf-12345EXAMPLE ).

fromBlueprintId (string) --The blueprint ID from which you created the snapshot (e.g., os_debian_8_3 ). A blueprint is a virtual private server (or instance ) image used to create instances quickly.

fromBundleId (string) --The bundle ID from which you created the snapshot (e.g., micro_1_0 ).

isFromAutoSnapshot (boolean) --A Boolean value indicating whether the snapshot was created from an automatic snapshot.

sizeInGb (integer) --The size in GB of the SSD.





nextPageToken (string) --The token to advance to the next page of resutls from your request.
A next page token is not returned if there are no more results to display.
To get the next page of results, perform another GetInstanceSnapshots request and specify the next page token using the pageToken parameter.






Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'instanceSnapshots': [
            {
                'name': 'string',
                'arn': 'string',
                'supportCode': 'string',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ],
                'state': 'pending'|'error'|'available',
                'progress': 'string',
                'fromAttachedDisks': [
                    {
                        'name': 'string',
                        'arn': 'string',
                        'supportCode': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'location': {
                            'availabilityZone': 'string',
                            'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                        },
                        'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                        'tags': [
                            {
                                'key': 'string',
                                'value': 'string'
                            },
                        ],
                        'addOns': [
                            {
                                'name': 'string',
                                'status': 'string',
                                'snapshotTimeOfDay': 'string',
                                'nextSnapshotTimeOfDay': 'string'
                            },
                        ],
                        'sizeInGb': 123,
                        'isSystemDisk': True|False,
                        'iops': 123,
                        'path': 'string',
                        'state': 'pending'|'error'|'available'|'in-use'|'unknown',
                        'attachedTo': 'string',
                        'isAttached': True|False,
                        'attachmentState': 'string',
                        'gbInUse': 123
                    },
                ],
                'fromInstanceName': 'string',
                'fromInstanceArn': 'string',
                'fromBlueprintId': 'string',
                'fromBundleId': 'string',
                'isFromAutoSnapshot': True|False,
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
    
    Exceptions
    
    :example: response = client.get_instance_state(
        instanceName='string'
    )
    
    
    :type instanceName: string
    :param instanceName: [REQUIRED]\nThe name of the instance to get state information about.\n

    :rtype: dict
ReturnsResponse Syntax{
    'state': {
        'code': 123,
        'name': 'string'
    }
}


Response Structure

(dict) --
state (dict) --The state of the instance.

code (integer) --The status code for the instance.

name (string) --The state of the instance (e.g., running or pending ).








Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


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
    
    Exceptions
    
    :example: response = client.get_instances(
        pageToken='string'
    )
    
    
    :type pageToken: string
    :param pageToken: The token to advance to the next page of results from your request.\nTo get a page token, perform an initial GetInstances request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.\n

    :rtype: dict
ReturnsResponse Syntax{
    'instances': [
        {
            'name': 'string',
            'arn': 'string',
            'supportCode': 'string',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ],
            'blueprintId': 'string',
            'blueprintName': 'string',
            'bundleId': 'string',
            'addOns': [
                {
                    'name': 'string',
                    'status': 'string',
                    'snapshotTimeOfDay': 'string',
                    'nextSnapshotTimeOfDay': 'string'
                },
            ],
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
                            'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                        },
                        'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                        'tags': [
                            {
                                'key': 'string',
                                'value': 'string'
                            },
                        ],
                        'addOns': [
                            {
                                'name': 'string',
                                'status': 'string',
                                'snapshotTimeOfDay': 'string',
                                'nextSnapshotTimeOfDay': 'string'
                            },
                        ],
                        'sizeInGb': 123,
                        'isSystemDisk': True|False,
                        'iops': 123,
                        'path': 'string',
                        'state': 'pending'|'error'|'available'|'in-use'|'unknown',
                        'attachedTo': 'string',
                        'isAttached': True|False,
                        'attachmentState': 'string',
                        'gbInUse': 123
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
                        'protocol': 'tcp'|'all'|'udp'|'icmp',
                        'accessFrom': 'string',
                        'accessType': 'Public'|'Private',
                        'commonName': 'string',
                        'accessDirection': 'inbound'|'outbound',
                        'cidrs': [
                            'string',
                        ],
                        'cidrListAliases': [
                            'string',
                        ]
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


Response Structure

(dict) --
instances (list) --An array of key-value pairs containing information about your instances.

(dict) --Describes an instance (a virtual private server).

name (string) --The name the user gave the instance (e.g., Amazon_Linux-1GB-Ohio-1 ).

arn (string) --The Amazon Resource Name (ARN) of the instance (e.g., arn:aws:lightsail:us-east-2:123456789101:Instance/244ad76f-8aad-4741-809f-12345EXAMPLE ).

supportCode (string) --The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.

createdAt (datetime) --The timestamp when the instance was created (e.g., 1479734909.17 ).

location (dict) --The region name and Availability Zone where the instance is located.

availabilityZone (string) --The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --The AWS Region name.



resourceType (string) --The type of resource (usually Instance ).

tags (list) --The tag keys and optional values for the resource. For more information about tags in Lightsail, see the Lightsail Dev Guide .

(dict) --Describes a tag key and optional value assigned to an Amazon Lightsail resource.
For more information about tags in Lightsail, see the Lightsail Dev Guide .

key (string) --The key of the tag.
Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @

value (string) --The value of the tag.
Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @





blueprintId (string) --The blueprint ID (e.g., os_amlinux_2016_03 ).

blueprintName (string) --The friendly name of the blueprint (e.g., Amazon Linux ).

bundleId (string) --The bundle for the instance (e.g., micro_1_0 ).

addOns (list) --An array of objects representing the add-ons enabled on the instance.

(dict) --Describes an add-on that is enabled for an Amazon Lightsail resource.

name (string) --The name of the add-on.

status (string) --The status of the add-on.

snapshotTimeOfDay (string) --The daily time when an automatic snapshot is created.
The time shown is in HH:00 format, and in Coordinated Universal Time (UTC).
The snapshot is automatically created between the time shown and up to 45 minutes after.

nextSnapshotTimeOfDay (string) --The next daily time an automatic snapshot will be created.
The time shown is in HH:00 format, and in Coordinated Universal Time (UTC).
The snapshot is automatically created between the time shown and up to 45 minutes after.





isStaticIp (boolean) --A Boolean value indicating whether this instance has a static IP assigned to it.

privateIpAddress (string) --The private IP address of the instance.

publicIpAddress (string) --The public IP address of the instance.

ipv6Address (string) --The IPv6 address of the instance.

hardware (dict) --The size of the vCPU and the amount of RAM for the instance.

cpuCount (integer) --The number of vCPUs the instance has.

disks (list) --The disks attached to the instance.

(dict) --Describes a system disk or a block storage disk.

name (string) --The unique name of the disk.

arn (string) --The Amazon Resource Name (ARN) of the disk.

supportCode (string) --The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.

createdAt (datetime) --The date when the disk was created.

location (dict) --The AWS Region and Availability Zone where the disk is located.

availabilityZone (string) --The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --The AWS Region name.



resourceType (string) --The Lightsail resource type (e.g., Disk ).

tags (list) --The tag keys and optional values for the resource. For more information about tags in Lightsail, see the Lightsail Dev Guide .

(dict) --Describes a tag key and optional value assigned to an Amazon Lightsail resource.
For more information about tags in Lightsail, see the Lightsail Dev Guide .

key (string) --The key of the tag.
Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @

value (string) --The value of the tag.
Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @





addOns (list) --An array of objects representing the add-ons enabled on the disk.

(dict) --Describes an add-on that is enabled for an Amazon Lightsail resource.

name (string) --The name of the add-on.

status (string) --The status of the add-on.

snapshotTimeOfDay (string) --The daily time when an automatic snapshot is created.
The time shown is in HH:00 format, and in Coordinated Universal Time (UTC).
The snapshot is automatically created between the time shown and up to 45 minutes after.

nextSnapshotTimeOfDay (string) --The next daily time an automatic snapshot will be created.
The time shown is in HH:00 format, and in Coordinated Universal Time (UTC).
The snapshot is automatically created between the time shown and up to 45 minutes after.





sizeInGb (integer) --The size of the disk in GB.

isSystemDisk (boolean) --A Boolean value indicating whether this disk is a system disk (has an operating system loaded on it).

iops (integer) --The input/output operations per second (IOPS) of the disk.

path (string) --The disk path.

state (string) --Describes the status of the disk.

attachedTo (string) --The resources to which the disk is attached.

isAttached (boolean) --A Boolean value indicating whether the disk is attached.

attachmentState (string) --(Deprecated) The attachment state of the disk.

Note
In releases prior to November 14, 2017, this parameter returned attached for system disks in the API response. It is now deprecated, but still included in the response. Use isAttached instead.


gbInUse (integer) --(Deprecated) The number of GB in use by the disk.

Note
In releases prior to November 14, 2017, this parameter was not included in the API response. It is now deprecated.






ramSizeInGb (float) --The amount of RAM in GB on the instance (e.g., 1.0 ).



networking (dict) --Information about the public ports and monthly data transfer rates for the instance.

monthlyTransfer (dict) --The amount of data in GB allocated for monthly data transfers.

gbPerMonthAllocated (integer) --The amount allocated per month (in GB).



ports (list) --An array of key-value pairs containing information about the ports on the instance.

(dict) --Describes information about ports for an Amazon Lightsail instance.

fromPort (integer) --The first port in a range of open ports on an instance.
Allowed ports:

TCP and UDP - 0 to 65535
ICMP - 8 (to configure Ping)


Note
Ping is the only communication supported through the ICMP protocol in Lightsail. To configure ping, specify the fromPort parameter as 8 , and the toPort parameter as -1 .


toPort (integer) --The last port in a range of open ports on an instance.
Allowed ports:

TCP and UDP - 0 to 65535
ICMP - -1 (to configure Ping)


Note
Ping is the only communication supported through the ICMP protocol in Lightsail. To configure ping, specify the fromPort parameter as 8 , and the toPort parameter as -1 .


protocol (string) --The IP protocol name.
The name can be one of the following:

tcp - Transmission Control Protocol (TCP) provides reliable, ordered, and error-checked delivery of streamed data between applications running on hosts communicating by an IP network. If you have an application that doesn\'t require reliable data stream service, use UDP instead.
all - All transport layer protocol types. For more general information, see Transport layer on Wikipedia .
udp - With User Datagram Protocol (UDP), computer applications can send messages (or datagrams) to other hosts on an Internet Protocol (IP) network. Prior communications are not required to set up transmission channels or data paths. Applications that don\'t require reliable data stream service can use UDP, which provides a connectionless datagram service that emphasizes reduced latency over reliability. If you do require reliable data stream service, use TCP instead.
icmp - Internet Control Message Protocol (ICMP) is used to send error messages and operational information indicating success or failure when communicating with an instance. For example, an error is indicated when an instance could not be reached.


Note
Ping is the only communication supported through the ICMP protocol in Lightsail. To configure ping, specify the fromPort parameter as 8 , and the toPort parameter as -1 .


accessFrom (string) --The location from which access is allowed. For example, Anywhere (0.0.0.0/0) , or Custom if a specific IP address or range of IP addresses is allowed.

accessType (string) --The type of access (Public or Private ).

commonName (string) --The common name of the port information.

accessDirection (string) --The access direction (inbound or outbound ).

Note
Lightsail currently supports only inbound access direction.


cidrs (list) --The IP address, or range of IP addresses in CIDR notation, that are allowed to connect to an instance through the ports, and the protocol. Lightsail supports IPv4 addresses.
For more information about CIDR block notation, see Classless Inter-Domain Routing on Wikipedia .

(string) --


cidrListAliases (list) --An alias that defines access for a preconfigured range of IP addresses.
The only alias currently supported is lightsail-connect , which allows IP addresses of the browser-based RDP/SSH client in the Lightsail console to connect to your instance.

(string) --








state (dict) --The status code and the state (e.g., running ) for the instance.

code (integer) --The status code for the instance.

name (string) --The state of the instance (e.g., running or pending ).



username (string) --The user name for connecting to the instance (e.g., ec2-user ).

sshKeyName (string) --The name of the SSH key being used to connect to the instance (e.g., LightsailDefaultKeyPair ).





nextPageToken (string) --The token to advance to the next page of resutls from your request.
A next page token is not returned if there are no more results to display.
To get the next page of results, perform another GetInstances request and specify the next page token using the pageToken parameter.






Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'instances': [
            {
                'name': 'string',
                'arn': 'string',
                'supportCode': 'string',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ],
                'blueprintId': 'string',
                'blueprintName': 'string',
                'bundleId': 'string',
                'addOns': [
                    {
                        'name': 'string',
                        'status': 'string',
                        'snapshotTimeOfDay': 'string',
                        'nextSnapshotTimeOfDay': 'string'
                    },
                ],
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
                                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                            },
                            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                            'tags': [
                                {
                                    'key': 'string',
                                    'value': 'string'
                                },
                            ],
                            'addOns': [
                                {
                                    'name': 'string',
                                    'status': 'string',
                                    'snapshotTimeOfDay': 'string',
                                    'nextSnapshotTimeOfDay': 'string'
                                },
                            ],
                            'sizeInGb': 123,
                            'isSystemDisk': True|False,
                            'iops': 123,
                            'path': 'string',
                            'state': 'pending'|'error'|'available'|'in-use'|'unknown',
                            'attachedTo': 'string',
                            'isAttached': True|False,
                            'attachmentState': 'string',
                            'gbInUse': 123
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
                            'protocol': 'tcp'|'all'|'udp'|'icmp',
                            'accessFrom': 'string',
                            'accessType': 'Public'|'Private',
                            'commonName': 'string',
                            'accessDirection': 'inbound'|'outbound',
                            'cidrs': [
                                'string',
                            ],
                            'cidrListAliases': [
                                'string',
                            ]
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
    
    
    :returns: 
    TCP and UDP - 0 to 65535
    ICMP - -1 (to configure Ping)
    
    """
    pass

def get_key_pair(keyPairName=None):
    """
    Returns information about a specific key pair.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_key_pair(
        keyPairName='string'
    )
    
    
    :type keyPairName: string
    :param keyPairName: [REQUIRED]\nThe name of the key pair for which you are requesting information.\n

    :rtype: dict
ReturnsResponse Syntax{
    'keyPair': {
        'name': 'string',
        'arn': 'string',
        'supportCode': 'string',
        'createdAt': datetime(2015, 1, 1),
        'location': {
            'availabilityZone': 'string',
            'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
        },
        'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
        'tags': [
            {
                'key': 'string',
                'value': 'string'
            },
        ],
        'fingerprint': 'string'
    }
}


Response Structure

(dict) --
keyPair (dict) --An array of key-value pairs containing information about the key pair.

name (string) --The friendly name of the SSH key pair.

arn (string) --The Amazon Resource Name (ARN) of the key pair (e.g., arn:aws:lightsail:us-east-2:123456789101:KeyPair/05859e3d-331d-48ba-9034-12345EXAMPLE ).

supportCode (string) --The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.

createdAt (datetime) --The timestamp when the key pair was created (e.g., 1479816991.349 ).

location (dict) --The region name and Availability Zone where the key pair was created.

availabilityZone (string) --The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --The AWS Region name.



resourceType (string) --The resource type (usually KeyPair ).

tags (list) --The tag keys and optional values for the resource. For more information about tags in Lightsail, see the Lightsail Dev Guide .

(dict) --Describes a tag key and optional value assigned to an Amazon Lightsail resource.
For more information about tags in Lightsail, see the Lightsail Dev Guide .

key (string) --The key of the tag.
Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @

value (string) --The value of the tag.
Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @





fingerprint (string) --The RSA fingerprint of the key pair.








Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'keyPair': {
            'name': 'string',
            'arn': 'string',
            'supportCode': 'string',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ],
            'fingerprint': 'string'
        }
    }
    
    
    """
    pass

def get_key_pairs(pageToken=None):
    """
    Returns information about all key pairs in the user\'s account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_key_pairs(
        pageToken='string'
    )
    
    
    :type pageToken: string
    :param pageToken: The token to advance to the next page of results from your request.\nTo get a page token, perform an initial GetKeyPairs request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.\n

    :rtype: dict
ReturnsResponse Syntax{
    'keyPairs': [
        {
            'name': 'string',
            'arn': 'string',
            'supportCode': 'string',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ],
            'fingerprint': 'string'
        },
    ],
    'nextPageToken': 'string'
}


Response Structure

(dict) --
keyPairs (list) --An array of key-value pairs containing information about the key pairs.

(dict) --Describes the SSH key pair.

name (string) --The friendly name of the SSH key pair.

arn (string) --The Amazon Resource Name (ARN) of the key pair (e.g., arn:aws:lightsail:us-east-2:123456789101:KeyPair/05859e3d-331d-48ba-9034-12345EXAMPLE ).

supportCode (string) --The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.

createdAt (datetime) --The timestamp when the key pair was created (e.g., 1479816991.349 ).

location (dict) --The region name and Availability Zone where the key pair was created.

availabilityZone (string) --The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --The AWS Region name.



resourceType (string) --The resource type (usually KeyPair ).

tags (list) --The tag keys and optional values for the resource. For more information about tags in Lightsail, see the Lightsail Dev Guide .

(dict) --Describes a tag key and optional value assigned to an Amazon Lightsail resource.
For more information about tags in Lightsail, see the Lightsail Dev Guide .

key (string) --The key of the tag.
Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @

value (string) --The value of the tag.
Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @





fingerprint (string) --The RSA fingerprint of the key pair.





nextPageToken (string) --The token to advance to the next page of resutls from your request.
A next page token is not returned if there are no more results to display.
To get the next page of results, perform another GetKeyPairs request and specify the next page token using the pageToken parameter.






Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'keyPairs': [
            {
                'name': 'string',
                'arn': 'string',
                'supportCode': 'string',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ],
                'fingerprint': 'string'
            },
        ],
        'nextPageToken': 'string'
    }
    
    
    """
    pass

def get_load_balancer(loadBalancerName=None):
    """
    Returns information about the specified Lightsail load balancer.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_load_balancer(
        loadBalancerName='string'
    )
    
    
    :type loadBalancerName: string
    :param loadBalancerName: [REQUIRED]\nThe name of the load balancer.\n

    :rtype: dict
ReturnsResponse Syntax{
    'loadBalancer': {
        'name': 'string',
        'arn': 'string',
        'supportCode': 'string',
        'createdAt': datetime(2015, 1, 1),
        'location': {
            'availabilityZone': 'string',
            'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
        },
        'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
        'tags': [
            {
                'key': 'string',
                'value': 'string'
            },
        ],
        'dnsName': 'string',
        'state': 'active'|'provisioning'|'active_impaired'|'failed'|'unknown',
        'protocol': 'HTTP_HTTPS'|'HTTP',
        'publicPorts': [
            123,
        ],
        'healthCheckPath': 'string',
        'instancePort': 123,
        'instanceHealthSummary': [
            {
                'instanceName': 'string',
                'instanceHealth': 'initial'|'healthy'|'unhealthy'|'unused'|'draining'|'unavailable',
                'instanceHealthReason': 'Lb.RegistrationInProgress'|'Lb.InitialHealthChecking'|'Lb.InternalError'|'Instance.ResponseCodeMismatch'|'Instance.Timeout'|'Instance.FailedHealthChecks'|'Instance.NotRegistered'|'Instance.NotInUse'|'Instance.DeregistrationInProgress'|'Instance.InvalidState'|'Instance.IpUnusable'
            },
        ],
        'tlsCertificateSummaries': [
            {
                'name': 'string',
                'isAttached': True|False
            },
        ],
        'configurationOptions': {
            'string': 'string'
        }
    }
}


Response Structure

(dict) --
loadBalancer (dict) --An object containing information about your load balancer.

name (string) --The name of the load balancer (e.g., my-load-balancer ).

arn (string) --The Amazon Resource Name (ARN) of the load balancer.

supportCode (string) --The support code. Include this code in your email to support when you have questions about your Lightsail load balancer. This code enables our support team to look up your Lightsail information more easily.

createdAt (datetime) --The date when your load balancer was created.

location (dict) --The AWS Region where your load balancer was created (e.g., us-east-2a ). Lightsail automatically creates your load balancer across Availability Zones.

availabilityZone (string) --The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --The AWS Region name.



resourceType (string) --The resource type (e.g., LoadBalancer .

tags (list) --The tag keys and optional values for the resource. For more information about tags in Lightsail, see the Lightsail Dev Guide .

(dict) --Describes a tag key and optional value assigned to an Amazon Lightsail resource.
For more information about tags in Lightsail, see the Lightsail Dev Guide .

key (string) --The key of the tag.
Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @

value (string) --The value of the tag.
Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @





dnsName (string) --The DNS name of your Lightsail load balancer.

state (string) --The status of your load balancer. Valid values are below.

protocol (string) --The protocol you have enabled for your load balancer. Valid values are below.
You can\'t just have HTTP_HTTPS , but you can have just HTTP .

publicPorts (list) --An array of public port settings for your load balancer. For HTTP, use port 80. For HTTPS, use port 443.

(integer) --


healthCheckPath (string) --The path you specified to perform your health checks. If no path is specified, the load balancer tries to make a request to the default (root) page.

instancePort (integer) --The port where the load balancer will direct traffic to your Lightsail instances. For HTTP traffic, it\'s port 80. For HTTPS traffic, it\'s port 443.

instanceHealthSummary (list) --An array of InstanceHealthSummary objects describing the health of the load balancer.

(dict) --Describes information about the health of the instance.

instanceName (string) --The name of the Lightsail instance for which you are requesting health check data.

instanceHealth (string) --Describes the overall instance health. Valid values are below.

instanceHealthReason (string) --More information about the instance health. If the instanceHealth is healthy , then an instanceHealthReason value is not provided.
If ** instanceHealth ** is initial , the ** instanceHealthReason ** value can be one of the following:

**Lb.RegistrationInProgress ** - The target instance is in the process of being registered with the load balancer.
**Lb.InitialHealthChecking ** - The Lightsail load balancer is still sending the target instance the minimum number of health checks required to determine its health status.

If ** instanceHealth ** is unhealthy , the ** instanceHealthReason ** value can be one of the following:

**Instance.ResponseCodeMismatch ** - The health checks did not return an expected HTTP code.
**Instance.Timeout ** - The health check requests timed out.
**Instance.FailedHealthChecks ** - The health checks failed because the connection to the target instance timed out, the target instance response was malformed, or the target instance failed the health check for an unknown reason.
**Lb.InternalError ** - The health checks failed due to an internal error.

If ** instanceHealth ** is unused , the ** instanceHealthReason ** value can be one of the following:

**Instance.NotRegistered ** - The target instance is not registered with the target group.
**Instance.NotInUse ** - The target group is not used by any load balancer, or the target instance is in an Availability Zone that is not enabled for its load balancer.
**Instance.IpUnusable ** - The target IP address is reserved for use by a Lightsail load balancer.
**Instance.InvalidState ** - The target is in the stopped or terminated state.

If ** instanceHealth ** is draining , the ** instanceHealthReason ** value can be one of the following:

**Instance.DeregistrationInProgress ** - The target instance is in the process of being deregistered and the deregistration delay period has not expired.






tlsCertificateSummaries (list) --An array of LoadBalancerTlsCertificateSummary objects that provide additional information about the SSL/TLS certificates. For example, if true , the certificate is attached to the load balancer.

(dict) --Provides a summary of SSL/TLS certificate metadata.

name (string) --The name of the SSL/TLS certificate.

isAttached (boolean) --When true , the SSL/TLS certificate is attached to the Lightsail load balancer.





configurationOptions (dict) --A string to string map of the configuration options for your load balancer. Valid values are listed below.

(string) --
(string) --











Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'loadBalancer': {
            'name': 'string',
            'arn': 'string',
            'supportCode': 'string',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ],
            'dnsName': 'string',
            'state': 'active'|'provisioning'|'active_impaired'|'failed'|'unknown',
            'protocol': 'HTTP_HTTPS'|'HTTP',
            'publicPorts': [
                123,
            ],
            'healthCheckPath': 'string',
            'instancePort': 123,
            'instanceHealthSummary': [
                {
                    'instanceName': 'string',
                    'instanceHealth': 'initial'|'healthy'|'unhealthy'|'unused'|'draining'|'unavailable',
                    'instanceHealthReason': 'Lb.RegistrationInProgress'|'Lb.InitialHealthChecking'|'Lb.InternalError'|'Instance.ResponseCodeMismatch'|'Instance.Timeout'|'Instance.FailedHealthChecks'|'Instance.NotRegistered'|'Instance.NotInUse'|'Instance.DeregistrationInProgress'|'Instance.InvalidState'|'Instance.IpUnusable'
                },
            ],
            'tlsCertificateSummaries': [
                {
                    'name': 'string',
                    'isAttached': True|False
                },
            ],
            'configurationOptions': {
                'string': 'string'
            }
        }
    }
    
    
    :returns: 
    **Lb.RegistrationInProgress ** - The target instance is in the process of being registered with the load balancer.
    **Lb.InitialHealthChecking ** - The Lightsail load balancer is still sending the target instance the minimum number of health checks required to determine its health status.
    
    """
    pass

def get_load_balancer_metric_data(loadBalancerName=None, metricName=None, period=None, startTime=None, endTime=None, unit=None, statistics=None):
    """
    Returns information about health metrics for your Lightsail load balancer.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_load_balancer_metric_data(
        loadBalancerName='string',
        metricName='ClientTLSNegotiationErrorCount'|'HealthyHostCount'|'UnhealthyHostCount'|'HTTPCode_LB_4XX_Count'|'HTTPCode_LB_5XX_Count'|'HTTPCode_Instance_2XX_Count'|'HTTPCode_Instance_3XX_Count'|'HTTPCode_Instance_4XX_Count'|'HTTPCode_Instance_5XX_Count'|'InstanceResponseTime'|'RejectedConnectionCount'|'RequestCount',
        period=123,
        startTime=datetime(2015, 1, 1),
        endTime=datetime(2015, 1, 1),
        unit='Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'|'Gigabytes'|'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Count'|'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'|'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'|'Megabits/Second'|'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None',
        statistics=[
            'Minimum'|'Maximum'|'Sum'|'Average'|'SampleCount',
        ]
    )
    
    
    :type loadBalancerName: string
    :param loadBalancerName: [REQUIRED]\nThe name of the load balancer.\n

    :type metricName: string
    :param metricName: [REQUIRED]\nThe metric for which you want to return information.\nValid load balancer metric names are listed below, along with the most useful statistics to include in your request, and the published unit value.\n\n**ClientTLSNegotiationErrorCount ** - The number of TLS connections initiated by the client that did not establish a session with the load balancer due to a TLS error generated by the load balancer. Possible causes include a mismatch of ciphers or protocols. Statistics : The most useful statistic is Sum . Unit : The published unit is Count .\n**HealthyHostCount ** - The number of target instances that are considered healthy. Statistics : The most useful statistic are Average , Minimum , and Maximum . Unit : The published unit is Count .\n**HTTPCode_Instance_2XX_Count ** - The number of HTTP 2XX response codes generated by the target instances. This does not include any response codes generated by the load balancer. Statistics : The most useful statistic is Sum . Note that Minimum , Maximum , and Average all return 1 . Unit : The published unit is Count .\n**HTTPCode_Instance_3XX_Count ** - The number of HTTP 3XX response codes generated by the target instances. This does not include any response codes generated by the load balancer. Statistics : The most useful statistic is Sum . Note that Minimum , Maximum , and Average all return 1 . Unit : The published unit is Count .\n**HTTPCode_Instance_4XX_Count ** - The number of HTTP 4XX response codes generated by the target instances. This does not include any response codes generated by the load balancer. Statistics : The most useful statistic is Sum . Note that Minimum , Maximum , and Average all return 1 . Unit : The published unit is Count .\n**HTTPCode_Instance_5XX_Count ** - The number of HTTP 5XX response codes generated by the target instances. This does not include any response codes generated by the load balancer. Statistics : The most useful statistic is Sum . Note that Minimum , Maximum , and Average all return 1 . Unit : The published unit is Count .\n**HTTPCode_LB_4XX_Count ** - The number of HTTP 4XX client error codes that originated from the load balancer. Client errors are generated when requests are malformed or incomplete. These requests were not received by the target instance. This count does not include response codes generated by the target instances. Statistics : The most useful statistic is Sum . Note that Minimum , Maximum , and Average all return 1 . Unit : The published unit is Count .\n**HTTPCode_LB_5XX_Count ** - The number of HTTP 5XX server error codes that originated from the load balancer. This does not include any response codes generated by the target instance. This metric is reported if there are no healthy instances attached to the load balancer, or if the request rate exceeds the capacity of the instances (spillover) or the load balancer. Statistics : The most useful statistic is Sum . Note that Minimum , Maximum , and Average all return 1 . Unit : The published unit is Count .\n**InstanceResponseTime ** - The time elapsed, in seconds, after the request leaves the load balancer until a response from the target instance is received. Statistics : The most useful statistic is Average . Unit : The published unit is Seconds .\n**RejectedConnectionCount ** - The number of connections that were rejected because the load balancer had reached its maximum number of connections. Statistics : The most useful statistic is Sum . Unit : The published unit is Count .\n**RequestCount ** - The number of requests processed over IPv4. This count includes only the requests with a response generated by a target instance of the load balancer. Statistics : The most useful statistic is Sum . Note that Minimum , Maximum , and Average all return 1 . Unit : The published unit is Count .\n**UnhealthyHostCount ** - The number of target instances that are considered unhealthy. Statistics : The most useful statistic are Average , Minimum , and Maximum . Unit : The published unit is Count .\n\n

    :type period: integer
    :param period: [REQUIRED]\nThe granularity, in seconds, of the returned data points.\n

    :type startTime: datetime
    :param startTime: [REQUIRED]\nThe start time of the period.\n

    :type endTime: datetime
    :param endTime: [REQUIRED]\nThe end time of the period.\n

    :type unit: string
    :param unit: [REQUIRED]\nThe unit for the metric data request. Valid units depend on the metric data being required. For the valid units with each available metric, see the metricName parameter.\n

    :type statistics: list
    :param statistics: [REQUIRED]\nThe statistic for the metric.\nThe following statistics are available:\n\nMinimum - The lowest value observed during the specified period. Use this value to determine low volumes of activity for your application.\nMaximum - The highest value observed during the specified period. Use this value to determine high volumes of activity for your application.\nSum - All values submitted for the matching metric added together. You can use this statistic to determine the total volume of a metric.\nAverage - The value of Sum / SampleCount during the specified period. By comparing this statistic with the Minimum and Maximum values, you can determine the full scope of a metric and how close the average use is to the Minimum and Maximum values. This comparison helps you to know when to increase or decrease your resources.\nSampleCount - The count, or number, of data points used for the statistical calculation.\n\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'metricName': 'ClientTLSNegotiationErrorCount'|'HealthyHostCount'|'UnhealthyHostCount'|'HTTPCode_LB_4XX_Count'|'HTTPCode_LB_5XX_Count'|'HTTPCode_Instance_2XX_Count'|'HTTPCode_Instance_3XX_Count'|'HTTPCode_Instance_4XX_Count'|'HTTPCode_Instance_5XX_Count'|'InstanceResponseTime'|'RejectedConnectionCount'|'RequestCount',
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


Response Structure

(dict) --

metricName (string) --
The metric about which you are receiving information. Valid values are listed below, along with the most useful statistics to include in your request.

**ClientTLSNegotiationErrorCount ** - The number of TLS connections initiated by the client that did not establish a session with the load balancer. Possible causes include a mismatch of ciphers or protocols.  Statistics : The most useful statistic is Sum .
**HealthyHostCount ** - The number of target instances that are considered healthy.  Statistics : The most useful statistic are Average , Minimum , and Maximum .
**UnhealthyHostCount ** - The number of target instances that are considered unhealthy.  Statistics : The most useful statistic are Average , Minimum , and Maximum .
**HTTPCode_LB_4XX_Count ** - The number of HTTP 4XX client error codes that originate from the load balancer. Client errors are generated when requests are malformed or incomplete. These requests have not been received by the target instance. This count does not include any response codes generated by the target instances.  Statistics : The most useful statistic is Sum . Note that Minimum , Maximum , and Average all return 1 .
**HTTPCode_LB_5XX_Count ** - The number of HTTP 5XX server error codes that originate from the load balancer. This count does not include any response codes generated by the target instances.  Statistics : The most useful statistic is Sum . Note that Minimum , Maximum , and Average all return 1 . Note that Minimum , Maximum , and Average all return 1 .
**HTTPCode_Instance_2XX_Count ** - The number of HTTP response codes generated by the target instances. This does not include any response codes generated by the load balancer.  Statistics : The most useful statistic is Sum . Note that Minimum , Maximum , and Average all return 1 .
**HTTPCode_Instance_3XX_Count ** - The number of HTTP response codes generated by the target instances. This does not include any response codes generated by the load balancer.   Statistics : The most useful statistic is Sum . Note that Minimum , Maximum , and Average all return 1 .
**HTTPCode_Instance_4XX_Count ** - The number of HTTP response codes generated by the target instances. This does not include any response codes generated by the load balancer.  Statistics : The most useful statistic is Sum . Note that Minimum , Maximum , and Average all return 1 .
**HTTPCode_Instance_5XX_Count ** - The number of HTTP response codes generated by the target instances. This does not include any response codes generated by the load balancer.  Statistics : The most useful statistic is Sum . Note that Minimum , Maximum , and Average all return 1 .
**InstanceResponseTime ** - The time elapsed, in seconds, after the request leaves the load balancer until a response from the target instance is received.  Statistics : The most useful statistic is Average .
**RejectedConnectionCount ** - The number of connections that were rejected because the load balancer had reached its maximum number of connections.  Statistics : The most useful statistic is Sum .
**RequestCount ** - The number of requests processed over IPv4. This count includes only the requests with a response generated by a target instance of the load balancer.  Statistics : The most useful statistic is Sum . Note that Minimum , Maximum , and Average all return 1 .


metricData (list) --
An array of metric datapoint objects.

(dict) --
Describes the metric data point.

average (float) --
The average.

maximum (float) --
The maximum.

minimum (float) --
The minimum.

sampleCount (float) --
The sample count.

sum (float) --
The sum.

timestamp (datetime) --
The timestamp (e.g., 1479816991.349 ).

unit (string) --
The unit.











Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'metricName': 'ClientTLSNegotiationErrorCount'|'HealthyHostCount'|'UnhealthyHostCount'|'HTTPCode_LB_4XX_Count'|'HTTPCode_LB_5XX_Count'|'HTTPCode_Instance_2XX_Count'|'HTTPCode_Instance_3XX_Count'|'HTTPCode_Instance_4XX_Count'|'HTTPCode_Instance_5XX_Count'|'InstanceResponseTime'|'RejectedConnectionCount'|'RequestCount',
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
    
    
    :returns: 
    **ClientTLSNegotiationErrorCount ** - The number of TLS connections initiated by the client that did not establish a session with the load balancer. Possible causes include a mismatch of ciphers or protocols.  Statistics : The most useful statistic is Sum .
    **HealthyHostCount ** - The number of target instances that are considered healthy.  Statistics : The most useful statistic are Average , Minimum , and Maximum .
    **UnhealthyHostCount ** - The number of target instances that are considered unhealthy.  Statistics : The most useful statistic are Average , Minimum , and Maximum .
    **HTTPCode_LB_4XX_Count ** - The number of HTTP 4XX client error codes that originate from the load balancer. Client errors are generated when requests are malformed or incomplete. These requests have not been received by the target instance. This count does not include any response codes generated by the target instances.  Statistics : The most useful statistic is Sum . Note that Minimum , Maximum , and Average all return 1 .
    **HTTPCode_LB_5XX_Count ** - The number of HTTP 5XX server error codes that originate from the load balancer. This count does not include any response codes generated by the target instances.  Statistics : The most useful statistic is Sum . Note that Minimum , Maximum , and Average all return 1 . Note that Minimum , Maximum , and Average all return 1 .
    **HTTPCode_Instance_2XX_Count ** - The number of HTTP response codes generated by the target instances. This does not include any response codes generated by the load balancer.  Statistics : The most useful statistic is Sum . Note that Minimum , Maximum , and Average all return 1 .
    **HTTPCode_Instance_3XX_Count ** - The number of HTTP response codes generated by the target instances. This does not include any response codes generated by the load balancer.   Statistics : The most useful statistic is Sum . Note that Minimum , Maximum , and Average all return 1 .
    **HTTPCode_Instance_4XX_Count ** - The number of HTTP response codes generated by the target instances. This does not include any response codes generated by the load balancer.  Statistics : The most useful statistic is Sum . Note that Minimum , Maximum , and Average all return 1 .
    **HTTPCode_Instance_5XX_Count ** - The number of HTTP response codes generated by the target instances. This does not include any response codes generated by the load balancer.  Statistics : The most useful statistic is Sum . Note that Minimum , Maximum , and Average all return 1 .
    **InstanceResponseTime ** - The time elapsed, in seconds, after the request leaves the load balancer until a response from the target instance is received.  Statistics : The most useful statistic is Average .
    **RejectedConnectionCount ** - The number of connections that were rejected because the load balancer had reached its maximum number of connections.  Statistics : The most useful statistic is Sum .
    **RequestCount ** - The number of requests processed over IPv4. This count includes only the requests with a response generated by a target instance of the load balancer.  Statistics : The most useful statistic is Sum . Note that Minimum , Maximum , and Average all return 1 .
    
    """
    pass

def get_load_balancer_tls_certificates(loadBalancerName=None):
    """
    Returns information about the TLS certificates that are associated with the specified Lightsail load balancer.
    TLS is just an updated, more secure version of Secure Socket Layer (SSL).
    You can have a maximum of 2 certificates associated with a Lightsail load balancer. One is active and the other is inactive.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_load_balancer_tls_certificates(
        loadBalancerName='string'
    )
    
    
    :type loadBalancerName: string
    :param loadBalancerName: [REQUIRED]\nThe name of the load balancer you associated with your SSL/TLS certificate.\n

    :rtype: dict
ReturnsResponse Syntax{
    'tlsCertificates': [
        {
            'name': 'string',
            'arn': 'string',
            'supportCode': 'string',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ],
            'loadBalancerName': 'string',
            'isAttached': True|False,
            'status': 'PENDING_VALIDATION'|'ISSUED'|'INACTIVE'|'EXPIRED'|'VALIDATION_TIMED_OUT'|'REVOKED'|'FAILED'|'UNKNOWN',
            'domainName': 'string',
            'domainValidationRecords': [
                {
                    'name': 'string',
                    'type': 'string',
                    'value': 'string',
                    'validationStatus': 'PENDING_VALIDATION'|'FAILED'|'SUCCESS',
                    'domainName': 'string'
                },
            ],
            'failureReason': 'NO_AVAILABLE_CONTACTS'|'ADDITIONAL_VERIFICATION_REQUIRED'|'DOMAIN_NOT_ALLOWED'|'INVALID_PUBLIC_DOMAIN'|'OTHER',
            'issuedAt': datetime(2015, 1, 1),
            'issuer': 'string',
            'keyAlgorithm': 'string',
            'notAfter': datetime(2015, 1, 1),
            'notBefore': datetime(2015, 1, 1),
            'renewalSummary': {
                'renewalStatus': 'PENDING_AUTO_RENEWAL'|'PENDING_VALIDATION'|'SUCCESS'|'FAILED',
                'domainValidationOptions': [
                    {
                        'domainName': 'string',
                        'validationStatus': 'PENDING_VALIDATION'|'FAILED'|'SUCCESS'
                    },
                ]
            },
            'revocationReason': 'UNSPECIFIED'|'KEY_COMPROMISE'|'CA_COMPROMISE'|'AFFILIATION_CHANGED'|'SUPERCEDED'|'CESSATION_OF_OPERATION'|'CERTIFICATE_HOLD'|'REMOVE_FROM_CRL'|'PRIVILEGE_WITHDRAWN'|'A_A_COMPROMISE',
            'revokedAt': datetime(2015, 1, 1),
            'serial': 'string',
            'signatureAlgorithm': 'string',
            'subject': 'string',
            'subjectAlternativeNames': [
                'string',
            ]
        },
    ]
}


Response Structure

(dict) --
tlsCertificates (list) --An array of LoadBalancerTlsCertificate objects describing your SSL/TLS certificates.

(dict) --Describes a load balancer SSL/TLS certificate.
TLS is just an updated, more secure version of Secure Socket Layer (SSL).

name (string) --The name of the SSL/TLS certificate (e.g., my-certificate ).

arn (string) --The Amazon Resource Name (ARN) of the SSL/TLS certificate.

supportCode (string) --The support code. Include this code in your email to support when you have questions about your Lightsail load balancer or SSL/TLS certificate. This code enables our support team to look up your Lightsail information more easily.

createdAt (datetime) --The time when you created your SSL/TLS certificate.

location (dict) --The AWS Region and Availability Zone where you created your certificate.

availabilityZone (string) --The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --The AWS Region name.



resourceType (string) --The resource type (e.g., LoadBalancerTlsCertificate ).

**Instance ** - A Lightsail instance (a virtual private server)
**StaticIp ** - A static IP address
**KeyPair ** - The key pair used to connect to a Lightsail instance
**InstanceSnapshot ** - A Lightsail instance snapshot
**Domain ** - A DNS zone
**PeeredVpc ** - A peered VPC
**LoadBalancer ** - A Lightsail load balancer
**LoadBalancerTlsCertificate ** - An SSL/TLS certificate associated with a Lightsail load balancer
**Disk ** - A Lightsail block storage disk
**DiskSnapshot ** - A block storage disk snapshot


tags (list) --The tag keys and optional values for the resource. For more information about tags in Lightsail, see the Lightsail Dev Guide .

(dict) --Describes a tag key and optional value assigned to an Amazon Lightsail resource.
For more information about tags in Lightsail, see the Lightsail Dev Guide .

key (string) --The key of the tag.
Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @

value (string) --The value of the tag.
Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @





loadBalancerName (string) --The load balancer name where your SSL/TLS certificate is attached.

isAttached (boolean) --When true , the SSL/TLS certificate is attached to the Lightsail load balancer.

status (string) --The status of the SSL/TLS certificate. Valid values are below.

domainName (string) --The domain name for your SSL/TLS certificate.

domainValidationRecords (list) --An array of LoadBalancerTlsCertificateDomainValidationRecord objects describing the records.

(dict) --Describes the validation record of each domain name in the SSL/TLS certificate.

name (string) --A fully qualified domain name in the certificate. For example, example.com .

type (string) --The type of validation record. For example, CNAME for domain validation.

value (string) --The value for that type.

validationStatus (string) --The validation status. Valid values are listed below.

domainName (string) --The domain name against which your SSL/TLS certificate was validated.





failureReason (string) --The reason for the SSL/TLS certificate validation failure.

issuedAt (datetime) --The time when the SSL/TLS certificate was issued.

issuer (string) --The issuer of the certificate.

keyAlgorithm (string) --The algorithm that was used to generate the key pair (the public and private key).

notAfter (datetime) --The timestamp when the SSL/TLS certificate expires.

notBefore (datetime) --The timestamp when the SSL/TLS certificate is first valid.

renewalSummary (dict) --An object containing information about the status of Lightsail\'s managed renewal for the certificate.

renewalStatus (string) --The status of Lightsail\'s managed renewal of the certificate. Valid values are listed below.

domainValidationOptions (list) --Contains information about the validation of each domain name in the certificate, as it pertains to Lightsail\'s managed renewal. This is different from the initial validation that occurs as a result of the RequestCertificate request.

(dict) --Contains information about the domain names on an SSL/TLS certificate that you will use to validate domain ownership.

domainName (string) --The fully qualified domain name in the certificate request.

validationStatus (string) --The status of the domain validation. Valid values are listed below.







revocationReason (string) --The reason the certificate was revoked. Valid values are below.

revokedAt (datetime) --The timestamp when the SSL/TLS certificate was revoked.

serial (string) --The serial number of the certificate.

signatureAlgorithm (string) --The algorithm that was used to sign the certificate.

subject (string) --The name of the entity that is associated with the public key contained in the certificate.

subjectAlternativeNames (list) --One or more domains or subdomains included in the certificate. This list contains the domain names that are bound to the public key that is contained in the certificate. The subject alternative names include the canonical domain name (CNAME) of the certificate and additional domain names that can be used to connect to the website, such as example.com , www.example.com , or m.example.com .

(string) --











Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'tlsCertificates': [
            {
                'name': 'string',
                'arn': 'string',
                'supportCode': 'string',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ],
                'loadBalancerName': 'string',
                'isAttached': True|False,
                'status': 'PENDING_VALIDATION'|'ISSUED'|'INACTIVE'|'EXPIRED'|'VALIDATION_TIMED_OUT'|'REVOKED'|'FAILED'|'UNKNOWN',
                'domainName': 'string',
                'domainValidationRecords': [
                    {
                        'name': 'string',
                        'type': 'string',
                        'value': 'string',
                        'validationStatus': 'PENDING_VALIDATION'|'FAILED'|'SUCCESS',
                        'domainName': 'string'
                    },
                ],
                'failureReason': 'NO_AVAILABLE_CONTACTS'|'ADDITIONAL_VERIFICATION_REQUIRED'|'DOMAIN_NOT_ALLOWED'|'INVALID_PUBLIC_DOMAIN'|'OTHER',
                'issuedAt': datetime(2015, 1, 1),
                'issuer': 'string',
                'keyAlgorithm': 'string',
                'notAfter': datetime(2015, 1, 1),
                'notBefore': datetime(2015, 1, 1),
                'renewalSummary': {
                    'renewalStatus': 'PENDING_AUTO_RENEWAL'|'PENDING_VALIDATION'|'SUCCESS'|'FAILED',
                    'domainValidationOptions': [
                        {
                            'domainName': 'string',
                            'validationStatus': 'PENDING_VALIDATION'|'FAILED'|'SUCCESS'
                        },
                    ]
                },
                'revocationReason': 'UNSPECIFIED'|'KEY_COMPROMISE'|'CA_COMPROMISE'|'AFFILIATION_CHANGED'|'SUPERCEDED'|'CESSATION_OF_OPERATION'|'CERTIFICATE_HOLD'|'REMOVE_FROM_CRL'|'PRIVILEGE_WITHDRAWN'|'A_A_COMPROMISE',
                'revokedAt': datetime(2015, 1, 1),
                'serial': 'string',
                'signatureAlgorithm': 'string',
                'subject': 'string',
                'subjectAlternativeNames': [
                    'string',
                ]
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_load_balancers(pageToken=None):
    """
    Returns information about all load balancers in an account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_load_balancers(
        pageToken='string'
    )
    
    
    :type pageToken: string
    :param pageToken: The token to advance to the next page of results from your request.\nTo get a page token, perform an initial GetLoadBalancers request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.\n

    :rtype: dict
ReturnsResponse Syntax{
    'loadBalancers': [
        {
            'name': 'string',
            'arn': 'string',
            'supportCode': 'string',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ],
            'dnsName': 'string',
            'state': 'active'|'provisioning'|'active_impaired'|'failed'|'unknown',
            'protocol': 'HTTP_HTTPS'|'HTTP',
            'publicPorts': [
                123,
            ],
            'healthCheckPath': 'string',
            'instancePort': 123,
            'instanceHealthSummary': [
                {
                    'instanceName': 'string',
                    'instanceHealth': 'initial'|'healthy'|'unhealthy'|'unused'|'draining'|'unavailable',
                    'instanceHealthReason': 'Lb.RegistrationInProgress'|'Lb.InitialHealthChecking'|'Lb.InternalError'|'Instance.ResponseCodeMismatch'|'Instance.Timeout'|'Instance.FailedHealthChecks'|'Instance.NotRegistered'|'Instance.NotInUse'|'Instance.DeregistrationInProgress'|'Instance.InvalidState'|'Instance.IpUnusable'
                },
            ],
            'tlsCertificateSummaries': [
                {
                    'name': 'string',
                    'isAttached': True|False
                },
            ],
            'configurationOptions': {
                'string': 'string'
            }
        },
    ],
    'nextPageToken': 'string'
}


Response Structure

(dict) --
loadBalancers (list) --An array of LoadBalancer objects describing your load balancers.

(dict) --Describes the Lightsail load balancer.

name (string) --The name of the load balancer (e.g., my-load-balancer ).

arn (string) --The Amazon Resource Name (ARN) of the load balancer.

supportCode (string) --The support code. Include this code in your email to support when you have questions about your Lightsail load balancer. This code enables our support team to look up your Lightsail information more easily.

createdAt (datetime) --The date when your load balancer was created.

location (dict) --The AWS Region where your load balancer was created (e.g., us-east-2a ). Lightsail automatically creates your load balancer across Availability Zones.

availabilityZone (string) --The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --The AWS Region name.



resourceType (string) --The resource type (e.g., LoadBalancer .

tags (list) --The tag keys and optional values for the resource. For more information about tags in Lightsail, see the Lightsail Dev Guide .

(dict) --Describes a tag key and optional value assigned to an Amazon Lightsail resource.
For more information about tags in Lightsail, see the Lightsail Dev Guide .

key (string) --The key of the tag.
Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @

value (string) --The value of the tag.
Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @





dnsName (string) --The DNS name of your Lightsail load balancer.

state (string) --The status of your load balancer. Valid values are below.

protocol (string) --The protocol you have enabled for your load balancer. Valid values are below.
You can\'t just have HTTP_HTTPS , but you can have just HTTP .

publicPorts (list) --An array of public port settings for your load balancer. For HTTP, use port 80. For HTTPS, use port 443.

(integer) --


healthCheckPath (string) --The path you specified to perform your health checks. If no path is specified, the load balancer tries to make a request to the default (root) page.

instancePort (integer) --The port where the load balancer will direct traffic to your Lightsail instances. For HTTP traffic, it\'s port 80. For HTTPS traffic, it\'s port 443.

instanceHealthSummary (list) --An array of InstanceHealthSummary objects describing the health of the load balancer.

(dict) --Describes information about the health of the instance.

instanceName (string) --The name of the Lightsail instance for which you are requesting health check data.

instanceHealth (string) --Describes the overall instance health. Valid values are below.

instanceHealthReason (string) --More information about the instance health. If the instanceHealth is healthy , then an instanceHealthReason value is not provided.
If ** instanceHealth ** is initial , the ** instanceHealthReason ** value can be one of the following:

**Lb.RegistrationInProgress ** - The target instance is in the process of being registered with the load balancer.
**Lb.InitialHealthChecking ** - The Lightsail load balancer is still sending the target instance the minimum number of health checks required to determine its health status.

If ** instanceHealth ** is unhealthy , the ** instanceHealthReason ** value can be one of the following:

**Instance.ResponseCodeMismatch ** - The health checks did not return an expected HTTP code.
**Instance.Timeout ** - The health check requests timed out.
**Instance.FailedHealthChecks ** - The health checks failed because the connection to the target instance timed out, the target instance response was malformed, or the target instance failed the health check for an unknown reason.
**Lb.InternalError ** - The health checks failed due to an internal error.

If ** instanceHealth ** is unused , the ** instanceHealthReason ** value can be one of the following:

**Instance.NotRegistered ** - The target instance is not registered with the target group.
**Instance.NotInUse ** - The target group is not used by any load balancer, or the target instance is in an Availability Zone that is not enabled for its load balancer.
**Instance.IpUnusable ** - The target IP address is reserved for use by a Lightsail load balancer.
**Instance.InvalidState ** - The target is in the stopped or terminated state.

If ** instanceHealth ** is draining , the ** instanceHealthReason ** value can be one of the following:

**Instance.DeregistrationInProgress ** - The target instance is in the process of being deregistered and the deregistration delay period has not expired.






tlsCertificateSummaries (list) --An array of LoadBalancerTlsCertificateSummary objects that provide additional information about the SSL/TLS certificates. For example, if true , the certificate is attached to the load balancer.

(dict) --Provides a summary of SSL/TLS certificate metadata.

name (string) --The name of the SSL/TLS certificate.

isAttached (boolean) --When true , the SSL/TLS certificate is attached to the Lightsail load balancer.





configurationOptions (dict) --A string to string map of the configuration options for your load balancer. Valid values are listed below.

(string) --
(string) --








nextPageToken (string) --The token to advance to the next page of resutls from your request.
A next page token is not returned if there are no more results to display.
To get the next page of results, perform another GetLoadBalancers request and specify the next page token using the pageToken parameter.






Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'loadBalancers': [
            {
                'name': 'string',
                'arn': 'string',
                'supportCode': 'string',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ],
                'dnsName': 'string',
                'state': 'active'|'provisioning'|'active_impaired'|'failed'|'unknown',
                'protocol': 'HTTP_HTTPS'|'HTTP',
                'publicPorts': [
                    123,
                ],
                'healthCheckPath': 'string',
                'instancePort': 123,
                'instanceHealthSummary': [
                    {
                        'instanceName': 'string',
                        'instanceHealth': 'initial'|'healthy'|'unhealthy'|'unused'|'draining'|'unavailable',
                        'instanceHealthReason': 'Lb.RegistrationInProgress'|'Lb.InitialHealthChecking'|'Lb.InternalError'|'Instance.ResponseCodeMismatch'|'Instance.Timeout'|'Instance.FailedHealthChecks'|'Instance.NotRegistered'|'Instance.NotInUse'|'Instance.DeregistrationInProgress'|'Instance.InvalidState'|'Instance.IpUnusable'
                    },
                ],
                'tlsCertificateSummaries': [
                    {
                        'name': 'string',
                        'isAttached': True|False
                    },
                ],
                'configurationOptions': {
                    'string': 'string'
                }
            },
        ],
        'nextPageToken': 'string'
    }
    
    
    :returns: 
    **Lb.RegistrationInProgress ** - The target instance is in the process of being registered with the load balancer.
    **Lb.InitialHealthChecking ** - The Lightsail load balancer is still sending the target instance the minimum number of health checks required to determine its health status.
    
    """
    pass

def get_operation(operationId=None):
    """
    Returns information about a specific operation. Operations include events such as when you create an instance, allocate a static IP, attach a static IP, and so on.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_operation(
        operationId='string'
    )
    
    
    :type operationId: string
    :param operationId: [REQUIRED]\nA GUID used to identify the operation.\n

    :rtype: dict
ReturnsResponse Syntax{
    'operation': {
        'id': 'string',
        'resourceName': 'string',
        'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
        'createdAt': datetime(2015, 1, 1),
        'location': {
            'availabilityZone': 'string',
            'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
        },
        'isTerminal': True|False,
        'operationDetails': 'string',
        'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
        'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
        'statusChangedAt': datetime(2015, 1, 1),
        'errorCode': 'string',
        'errorDetails': 'string'
    }
}


Response Structure

(dict) --
operation (dict) --An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

id (string) --The ID of the operation.

resourceName (string) --The resource name.

resourceType (string) --The resource type.

createdAt (datetime) --The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --The AWS Region and Availability Zone.

availabilityZone (string) --The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --The AWS Region name.



isTerminal (boolean) --A Boolean value indicating whether the operation is terminal.

operationDetails (string) --Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --The type of operation.

status (string) --The status of the operation.

statusChangedAt (datetime) --The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --The error code.

errorDetails (string) --The error details.








Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operation': {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
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
    
    Exceptions
    
    :example: response = client.get_operations(
        pageToken='string'
    )
    
    
    :type pageToken: string
    :param pageToken: The token to advance to the next page of results from your request.\nTo get a page token, perform an initial GetOperations request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.\n

    :rtype: dict
ReturnsResponse Syntax{
    'operations': [
        {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        },
    ],
    'nextPageToken': 'string'
}


Response Structure

(dict) --
operations (list) --An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

(dict) --Describes the API operation.

id (string) --The ID of the operation.

resourceName (string) --The resource name.

resourceType (string) --The resource type.

createdAt (datetime) --The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --The AWS Region and Availability Zone.

availabilityZone (string) --The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --The AWS Region name.



isTerminal (boolean) --A Boolean value indicating whether the operation is terminal.

operationDetails (string) --Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --The type of operation.

status (string) --The status of the operation.

statusChangedAt (datetime) --The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --The error code.

errorDetails (string) --The error details.





nextPageToken (string) --The token to advance to the next page of resutls from your request.
A next page token is not returned if there are no more results to display.
To get the next page of results, perform another GetOperations request and specify the next page token using the pageToken parameter.






Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
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
    
    Exceptions
    
    :example: response = client.get_operations_for_resource(
        resourceName='string',
        pageToken='string'
    )
    
    
    :type resourceName: string
    :param resourceName: [REQUIRED]\nThe name of the resource for which you are requesting information.\n

    :type pageToken: string
    :param pageToken: The token to advance to the next page of results from your request.\nTo get a page token, perform an initial GetOperationsForResource request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'operations': [
        {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        },
    ],
    'nextPageCount': 'string',
    'nextPageToken': 'string'
}


Response Structure

(dict) --

operations (list) --
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

(dict) --
Describes the API operation.

id (string) --
The ID of the operation.

resourceName (string) --
The resource name.

resourceType (string) --
The resource type.

createdAt (datetime) --
The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --
The AWS Region and Availability Zone.

availabilityZone (string) --
The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --
The AWS Region name.



isTerminal (boolean) --
A Boolean value indicating whether the operation is terminal.

operationDetails (string) --
Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --
The type of operation.

status (string) --
The status of the operation.

statusChangedAt (datetime) --
The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --
The error code.

errorDetails (string) --
The error details.





nextPageCount (string) --
(Deprecated) Returns the number of pages of results that remain.

Note
In releases prior to June 12, 2017, this parameter returned null by the API. It is now deprecated, and the API returns the next page token parameter instead.


nextPageToken (string) --
The token to advance to the next page of resutls from your request.
A next page token is not returned if there are no more results to display.
To get the next page of results, perform another GetOperationsForResource request and specify the next page token using the pageToken parameter.







Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ],
        'nextPageCount': 'string',
        'nextPageToken': 'string'
    }
    
    
    :returns: 
    Lightsail.Client.exceptions.ServiceException
    Lightsail.Client.exceptions.InvalidInputException
    Lightsail.Client.exceptions.NotFoundException
    Lightsail.Client.exceptions.OperationFailureException
    Lightsail.Client.exceptions.AccessDeniedException
    Lightsail.Client.exceptions.AccountSetupInProgressException
    Lightsail.Client.exceptions.UnauthenticatedException
    
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

def get_regions(includeAvailabilityZones=None, includeRelationalDatabaseAvailabilityZones=None):
    """
    Returns a list of all valid regions for Amazon Lightsail. Use the include availability zones parameter to also return the Availability Zones in a region.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_regions(
        includeAvailabilityZones=True|False,
        includeRelationalDatabaseAvailabilityZones=True|False
    )
    
    
    :type includeAvailabilityZones: boolean
    :param includeAvailabilityZones: A Boolean value indicating whether to also include Availability Zones in your get regions request. Availability Zones are indicated with a letter: e.g., us-east-2a .

    :type includeRelationalDatabaseAvailabilityZones: boolean
    :param includeRelationalDatabaseAvailabilityZones: >A Boolean value indicating whether to also include Availability Zones for databases in your get regions request. Availability Zones are indicated with a letter (e.g., us-east-2a ).

    :rtype: dict

ReturnsResponse Syntax
{
    'regions': [
        {
            'continentCode': 'string',
            'description': 'string',
            'displayName': 'string',
            'name': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2',
            'availabilityZones': [
                {
                    'zoneName': 'string',
                    'state': 'string'
                },
            ],
            'relationalDatabaseAvailabilityZones': [
                {
                    'zoneName': 'string',
                    'state': 'string'
                },
            ]
        },
    ]
}


Response Structure

(dict) --

regions (list) --
An array of key-value pairs containing information about your get regions request.

(dict) --
Describes the AWS Region.

continentCode (string) --
The continent code (e.g., NA , meaning North America).

description (string) --
The description of the AWS Region (e.g., This region is recommended to serve users in the eastern United States and eastern Canada ).

displayName (string) --
The display name (e.g., Ohio ).

name (string) --
The region name (e.g., us-east-2 ).

availabilityZones (list) --
The Availability Zones. Follows the format us-east-2a (case-sensitive).

(dict) --
Describes an Availability Zone.

zoneName (string) --
The name of the Availability Zone. The format is us-east-2a (case-sensitive).

state (string) --
The state of the Availability Zone.





relationalDatabaseAvailabilityZones (list) --
The Availability Zones for databases. Follows the format us-east-2a (case-sensitive).

(dict) --
Describes an Availability Zone.

zoneName (string) --
The name of the Availability Zone. The format is us-east-2a (case-sensitive).

state (string) --
The state of the Availability Zone.















Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'regions': [
            {
                'continentCode': 'string',
                'description': 'string',
                'displayName': 'string',
                'name': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2',
                'availabilityZones': [
                    {
                        'zoneName': 'string',
                        'state': 'string'
                    },
                ],
                'relationalDatabaseAvailabilityZones': [
                    {
                        'zoneName': 'string',
                        'state': 'string'
                    },
                ]
            },
        ]
    }
    
    
    :returns: 
    Lightsail.Client.exceptions.ServiceException
    Lightsail.Client.exceptions.InvalidInputException
    Lightsail.Client.exceptions.NotFoundException
    Lightsail.Client.exceptions.OperationFailureException
    Lightsail.Client.exceptions.AccessDeniedException
    Lightsail.Client.exceptions.AccountSetupInProgressException
    Lightsail.Client.exceptions.UnauthenticatedException
    
    """
    pass

def get_relational_database(relationalDatabaseName=None):
    """
    Returns information about a specific database in Amazon Lightsail.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_relational_database(
        relationalDatabaseName='string'
    )
    
    
    :type relationalDatabaseName: string
    :param relationalDatabaseName: [REQUIRED]\nThe name of the database that you are looking up.\n

    :rtype: dict
ReturnsResponse Syntax{
    'relationalDatabase': {
        'name': 'string',
        'arn': 'string',
        'supportCode': 'string',
        'createdAt': datetime(2015, 1, 1),
        'location': {
            'availabilityZone': 'string',
            'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
        },
        'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
        'tags': [
            {
                'key': 'string',
                'value': 'string'
            },
        ],
        'relationalDatabaseBlueprintId': 'string',
        'relationalDatabaseBundleId': 'string',
        'masterDatabaseName': 'string',
        'hardware': {
            'cpuCount': 123,
            'diskSizeInGb': 123,
            'ramSizeInGb': ...
        },
        'state': 'string',
        'secondaryAvailabilityZone': 'string',
        'backupRetentionEnabled': True|False,
        'pendingModifiedValues': {
            'masterUserPassword': 'string',
            'engineVersion': 'string',
            'backupRetentionEnabled': True|False
        },
        'engine': 'string',
        'engineVersion': 'string',
        'latestRestorableTime': datetime(2015, 1, 1),
        'masterUsername': 'string',
        'parameterApplyStatus': 'string',
        'preferredBackupWindow': 'string',
        'preferredMaintenanceWindow': 'string',
        'publiclyAccessible': True|False,
        'masterEndpoint': {
            'port': 123,
            'address': 'string'
        },
        'pendingMaintenanceActions': [
            {
                'action': 'string',
                'description': 'string',
                'currentApplyDate': datetime(2015, 1, 1)
            },
        ],
        'caCertificateIdentifier': 'string'
    }
}


Response Structure

(dict) --
relationalDatabase (dict) --An object describing the specified database.

name (string) --The unique name of the database resource in Lightsail.

arn (string) --The Amazon Resource Name (ARN) of the database.

supportCode (string) --The support code for the database. Include this code in your email to support when you have questions about a database in Lightsail. This code enables our support team to look up your Lightsail information more easily.

createdAt (datetime) --The timestamp when the database was created. Formatted in Unix time.

location (dict) --The Region name and Availability Zone where the database is located.

availabilityZone (string) --The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --The AWS Region name.



resourceType (string) --The Lightsail resource type for the database (for example, RelationalDatabase ).

tags (list) --The tag keys and optional values for the resource. For more information about tags in Lightsail, see the Lightsail Dev Guide .

(dict) --Describes a tag key and optional value assigned to an Amazon Lightsail resource.
For more information about tags in Lightsail, see the Lightsail Dev Guide .

key (string) --The key of the tag.
Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @

value (string) --The value of the tag.
Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @





relationalDatabaseBlueprintId (string) --The blueprint ID for the database. A blueprint describes the major engine version of a database.

relationalDatabaseBundleId (string) --The bundle ID for the database. A bundle describes the performance specifications for your database.

masterDatabaseName (string) --The name of the master database created when the Lightsail database resource is created.

hardware (dict) --Describes the hardware of the database.

cpuCount (integer) --The number of vCPUs for the database.

diskSizeInGb (integer) --The size of the disk for the database.

ramSizeInGb (float) --The amount of RAM in GB for the database.



state (string) --Describes the current state of the database.

secondaryAvailabilityZone (string) --Describes the secondary Availability Zone of a high availability database.
The secondary database is used for failover support of a high availability database.

backupRetentionEnabled (boolean) --A Boolean value indicating whether automated backup retention is enabled for the database.

pendingModifiedValues (dict) --Describes pending database value modifications.

masterUserPassword (string) --The password for the master user of the database.

engineVersion (string) --The database engine version.

backupRetentionEnabled (boolean) --A Boolean value indicating whether automated backup retention is enabled.



engine (string) --The database software (for example, MySQL ).

engineVersion (string) --The database engine version (for example, 5.7.23 ).

latestRestorableTime (datetime) --The latest point in time to which the database can be restored. Formatted in Unix time.

masterUsername (string) --The master user name of the database.

parameterApplyStatus (string) --The status of parameter updates for the database.

preferredBackupWindow (string) --The daily time range during which automated backups are created for the database (for example, 16:00-16:30 ).

preferredMaintenanceWindow (string) --The weekly time range during which system maintenance can occur on the database.
In the format ddd:hh24:mi-ddd:hh24:mi . For example, Tue:17:00-Tue:17:30 .

publiclyAccessible (boolean) --A Boolean value indicating whether the database is publicly accessible.

masterEndpoint (dict) --The master endpoint for the database.

port (integer) --Specifies the port that the database is listening on.

address (string) --Specifies the DNS address of the database.



pendingMaintenanceActions (list) --Describes the pending maintenance actions for the database.

(dict) --Describes a pending database maintenance action.

action (string) --The type of pending database maintenance action.

description (string) --Additional detail about the pending database maintenance action.

currentApplyDate (datetime) --The effective date of the pending database maintenance action.





caCertificateIdentifier (string) --The certificate associated with the database.








Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'relationalDatabase': {
            'name': 'string',
            'arn': 'string',
            'supportCode': 'string',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ],
            'relationalDatabaseBlueprintId': 'string',
            'relationalDatabaseBundleId': 'string',
            'masterDatabaseName': 'string',
            'hardware': {
                'cpuCount': 123,
                'diskSizeInGb': 123,
                'ramSizeInGb': ...
            },
            'state': 'string',
            'secondaryAvailabilityZone': 'string',
            'backupRetentionEnabled': True|False,
            'pendingModifiedValues': {
                'masterUserPassword': 'string',
                'engineVersion': 'string',
                'backupRetentionEnabled': True|False
            },
            'engine': 'string',
            'engineVersion': 'string',
            'latestRestorableTime': datetime(2015, 1, 1),
            'masterUsername': 'string',
            'parameterApplyStatus': 'string',
            'preferredBackupWindow': 'string',
            'preferredMaintenanceWindow': 'string',
            'publiclyAccessible': True|False,
            'masterEndpoint': {
                'port': 123,
                'address': 'string'
            },
            'pendingMaintenanceActions': [
                {
                    'action': 'string',
                    'description': 'string',
                    'currentApplyDate': datetime(2015, 1, 1)
                },
            ],
            'caCertificateIdentifier': 'string'
        }
    }
    
    
    """
    pass

def get_relational_database_blueprints(pageToken=None):
    """
    Returns a list of available database blueprints in Amazon Lightsail. A blueprint describes the major engine version of a database.
    You can use a blueprint ID to create a new database that runs a specific database engine.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_relational_database_blueprints(
        pageToken='string'
    )
    
    
    :type pageToken: string
    :param pageToken: The token to advance to the next page of results from your request.\nTo get a page token, perform an initial GetRelationalDatabaseBlueprints request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.\n

    :rtype: dict
ReturnsResponse Syntax{
    'blueprints': [
        {
            'blueprintId': 'string',
            'engine': 'mysql',
            'engineVersion': 'string',
            'engineDescription': 'string',
            'engineVersionDescription': 'string',
            'isEngineDefault': True|False
        },
    ],
    'nextPageToken': 'string'
}


Response Structure

(dict) --
blueprints (list) --An object describing the result of your get relational database blueprints request.

(dict) --Describes a database image, or blueprint. A blueprint describes the major engine version of a database.

blueprintId (string) --The ID for the database blueprint.

engine (string) --The database software of the database blueprint (for example, MySQL ).

engineVersion (string) --The database engine version for the database blueprint (for example, 5.7.23 ).

engineDescription (string) --The description of the database engine for the database blueprint.

engineVersionDescription (string) --The description of the database engine version for the database blueprint.

isEngineDefault (boolean) --A Boolean value indicating whether the engine version is the default for the database blueprint.





nextPageToken (string) --The token to advance to the next page of resutls from your request.
A next page token is not returned if there are no more results to display.
To get the next page of results, perform another GetRelationalDatabaseBlueprints request and specify the next page token using the pageToken parameter.






Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'blueprints': [
            {
                'blueprintId': 'string',
                'engine': 'mysql',
                'engineVersion': 'string',
                'engineDescription': 'string',
                'engineVersionDescription': 'string',
                'isEngineDefault': True|False
            },
        ],
        'nextPageToken': 'string'
    }
    
    
    """
    pass

def get_relational_database_bundles(pageToken=None):
    """
    Returns the list of bundles that are available in Amazon Lightsail. A bundle describes the performance specifications for a database.
    You can use a bundle ID to create a new database with explicit performance specifications.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_relational_database_bundles(
        pageToken='string'
    )
    
    
    :type pageToken: string
    :param pageToken: The token to advance to the next page of results from your request.\nTo get a page token, perform an initial GetRelationalDatabaseBundles request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.\n

    :rtype: dict
ReturnsResponse Syntax{
    'bundles': [
        {
            'bundleId': 'string',
            'name': 'string',
            'price': ...,
            'ramSizeInGb': ...,
            'diskSizeInGb': 123,
            'transferPerMonthInGb': 123,
            'cpuCount': 123,
            'isEncrypted': True|False,
            'isActive': True|False
        },
    ],
    'nextPageToken': 'string'
}


Response Structure

(dict) --
bundles (list) --An object describing the result of your get relational database bundles request.

(dict) --Describes a database bundle. A bundle describes the performance specifications of the database.

bundleId (string) --The ID for the database bundle.

name (string) --The name for the database bundle.

price (float) --The cost of the database bundle in US currency.

ramSizeInGb (float) --The amount of RAM in GB (for example, 2.0 ) for the database bundle.

diskSizeInGb (integer) --The size of the disk for the database bundle.

transferPerMonthInGb (integer) --The data transfer rate per month in GB for the database bundle.

cpuCount (integer) --The number of virtual CPUs (vCPUs) for the database bundle.

isEncrypted (boolean) --A Boolean value indicating whether the database bundle is encrypted.

isActive (boolean) --A Boolean value indicating whether the database bundle is active.





nextPageToken (string) --The token to advance to the next page of resutls from your request.
A next page token is not returned if there are no more results to display.
To get the next page of results, perform another GetRelationalDatabaseBundles request and specify the next page token using the pageToken parameter.






Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'bundles': [
            {
                'bundleId': 'string',
                'name': 'string',
                'price': ...,
                'ramSizeInGb': ...,
                'diskSizeInGb': 123,
                'transferPerMonthInGb': 123,
                'cpuCount': 123,
                'isEncrypted': True|False,
                'isActive': True|False
            },
        ],
        'nextPageToken': 'string'
    }
    
    
    """
    pass

def get_relational_database_events(relationalDatabaseName=None, durationInMinutes=None, pageToken=None):
    """
    Returns a list of events for a specific database in Amazon Lightsail.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_relational_database_events(
        relationalDatabaseName='string',
        durationInMinutes=123,
        pageToken='string'
    )
    
    
    :type relationalDatabaseName: string
    :param relationalDatabaseName: [REQUIRED]\nThe name of the database from which to get events.\n

    :type durationInMinutes: integer
    :param durationInMinutes: The number of minutes in the past from which to retrieve events. For example, to get all events from the past 2 hours, enter 120.\nDefault: 60\nThe minimum is 1 and the maximum is 14 days (20160 minutes).\n

    :type pageToken: string
    :param pageToken: The token to advance to the next page of results from your request.\nTo get a page token, perform an initial GetRelationalDatabaseEvents request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'relationalDatabaseEvents': [
        {
            'resource': 'string',
            'createdAt': datetime(2015, 1, 1),
            'message': 'string',
            'eventCategories': [
                'string',
            ]
        },
    ],
    'nextPageToken': 'string'
}


Response Structure

(dict) --

relationalDatabaseEvents (list) --
An object describing the result of your get relational database events request.

(dict) --
Describes an event for a database.

resource (string) --
The database that the database event relates to.

createdAt (datetime) --
The timestamp when the database event was created.

message (string) --
The message of the database event.

eventCategories (list) --
The category that the database event belongs to.

(string) --






nextPageToken (string) --
The token to advance to the next page of resutls from your request.
A next page token is not returned if there are no more results to display.
To get the next page of results, perform another GetRelationalDatabaseEvents request and specify the next page token using the pageToken parameter.







Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'relationalDatabaseEvents': [
            {
                'resource': 'string',
                'createdAt': datetime(2015, 1, 1),
                'message': 'string',
                'eventCategories': [
                    'string',
                ]
            },
        ],
        'nextPageToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_relational_database_log_events(relationalDatabaseName=None, logStreamName=None, startTime=None, endTime=None, startFromHead=None, pageToken=None):
    """
    Returns a list of log events for a database in Amazon Lightsail.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_relational_database_log_events(
        relationalDatabaseName='string',
        logStreamName='string',
        startTime=datetime(2015, 1, 1),
        endTime=datetime(2015, 1, 1),
        startFromHead=True|False,
        pageToken='string'
    )
    
    
    :type relationalDatabaseName: string
    :param relationalDatabaseName: [REQUIRED]\nThe name of your database for which to get log events.\n

    :type logStreamName: string
    :param logStreamName: [REQUIRED]\nThe name of the log stream.\nUse the get relational database log streams operation to get a list of available log streams.\n

    :type startTime: datetime
    :param startTime: The start of the time interval from which to get log events.\nConstraints:\n\nSpecified in Coordinated Universal Time (UTC).\nSpecified in the Unix time format. For example, if you wish to use a start time of October 1, 2018, at 8 PM UTC, then you input 1538424000 as the start time.\n\n

    :type endTime: datetime
    :param endTime: The end of the time interval from which to get log events.\nConstraints:\n\nSpecified in Coordinated Universal Time (UTC).\nSpecified in the Unix time format. For example, if you wish to use an end time of October 1, 2018, at 8 PM UTC, then you input 1538424000 as the end time.\n\n

    :type startFromHead: boolean
    :param startFromHead: Parameter to specify if the log should start from head or tail. If true is specified, the log event starts from the head of the log. If false is specified, the log event starts from the tail of the log.\n\nNote\nFor PostgreSQL, the default value of false is the only option available.\n\n

    :type pageToken: string
    :param pageToken: The token to advance to the next or previous page of results from your request.\nTo get a page token, perform an initial GetRelationalDatabaseLogEvents request. If your results are paginated, the response will return a next forward token and/or next backward token that you can specify as the page token in a subsequent request.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'resourceLogEvents': [
        {
            'createdAt': datetime(2015, 1, 1),
            'message': 'string'
        },
    ],
    'nextBackwardToken': 'string',
    'nextForwardToken': 'string'
}


Response Structure

(dict) --

resourceLogEvents (list) --
An object describing the result of your get relational database log events request.

(dict) --
Describes a database log event.

createdAt (datetime) --
The timestamp when the database log event was created.

message (string) --
The message of the database log event.





nextBackwardToken (string) --
A token used for advancing to the previous page of results from your get relational database log events request.

nextForwardToken (string) --
A token used for advancing to the next page of results from your get relational database log events request.







Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'resourceLogEvents': [
            {
                'createdAt': datetime(2015, 1, 1),
                'message': 'string'
            },
        ],
        'nextBackwardToken': 'string',
        'nextForwardToken': 'string'
    }
    
    
    :returns: 
    Lightsail.Client.exceptions.ServiceException
    Lightsail.Client.exceptions.InvalidInputException
    Lightsail.Client.exceptions.NotFoundException
    Lightsail.Client.exceptions.OperationFailureException
    Lightsail.Client.exceptions.AccessDeniedException
    Lightsail.Client.exceptions.AccountSetupInProgressException
    Lightsail.Client.exceptions.UnauthenticatedException
    
    """
    pass

def get_relational_database_log_streams(relationalDatabaseName=None):
    """
    Returns a list of available log streams for a specific database in Amazon Lightsail.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_relational_database_log_streams(
        relationalDatabaseName='string'
    )
    
    
    :type relationalDatabaseName: string
    :param relationalDatabaseName: [REQUIRED]\nThe name of your database for which to get log streams.\n

    :rtype: dict
ReturnsResponse Syntax{
    'logStreams': [
        'string',
    ]
}


Response Structure

(dict) --
logStreams (list) --An object describing the result of your get relational database log streams request.

(string) --







Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'logStreams': [
            'string',
        ]
    }
    
    
    :returns: 
    Lightsail.Client.exceptions.ServiceException
    Lightsail.Client.exceptions.InvalidInputException
    Lightsail.Client.exceptions.NotFoundException
    Lightsail.Client.exceptions.OperationFailureException
    Lightsail.Client.exceptions.AccessDeniedException
    Lightsail.Client.exceptions.AccountSetupInProgressException
    Lightsail.Client.exceptions.UnauthenticatedException
    
    """
    pass

def get_relational_database_master_user_password(relationalDatabaseName=None, passwordVersion=None):
    """
    Returns the current, previous, or pending versions of the master user password for a Lightsail database.
    The GetRelationalDatabaseMasterUserPassword operation supports tag-based access control via resource tags applied to the resource identified by relationalDatabaseName.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_relational_database_master_user_password(
        relationalDatabaseName='string',
        passwordVersion='CURRENT'|'PREVIOUS'|'PENDING'
    )
    
    
    :type relationalDatabaseName: string
    :param relationalDatabaseName: [REQUIRED]\nThe name of your database for which to get the master user password.\n

    :type passwordVersion: string
    :param passwordVersion: The password version to return.\nSpecifying CURRENT or PREVIOUS returns the current or previous passwords respectively. Specifying PENDING returns the newest version of the password that will rotate to CURRENT . After the PENDING password rotates to CURRENT , the PENDING password is no longer available.\nDefault: CURRENT\n

    :rtype: dict

ReturnsResponse Syntax
{
    'masterUserPassword': 'string',
    'createdAt': datetime(2015, 1, 1)
}


Response Structure

(dict) --

masterUserPassword (string) --
The master user password for the password version specified.

createdAt (datetime) --
The timestamp when the specified version of the master user password was created.







Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'masterUserPassword': 'string',
        'createdAt': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    Lightsail.Client.exceptions.ServiceException
    Lightsail.Client.exceptions.InvalidInputException
    Lightsail.Client.exceptions.NotFoundException
    Lightsail.Client.exceptions.OperationFailureException
    Lightsail.Client.exceptions.AccessDeniedException
    Lightsail.Client.exceptions.AccountSetupInProgressException
    Lightsail.Client.exceptions.UnauthenticatedException
    
    """
    pass

def get_relational_database_metric_data(relationalDatabaseName=None, metricName=None, period=None, startTime=None, endTime=None, unit=None, statistics=None):
    """
    Returns the data points of the specified metric for a database in Amazon Lightsail.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_relational_database_metric_data(
        relationalDatabaseName='string',
        metricName='CPUUtilization'|'DatabaseConnections'|'DiskQueueDepth'|'FreeStorageSpace'|'NetworkReceiveThroughput'|'NetworkTransmitThroughput',
        period=123,
        startTime=datetime(2015, 1, 1),
        endTime=datetime(2015, 1, 1),
        unit='Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'|'Gigabytes'|'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Count'|'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'|'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'|'Megabits/Second'|'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None',
        statistics=[
            'Minimum'|'Maximum'|'Sum'|'Average'|'SampleCount',
        ]
    )
    
    
    :type relationalDatabaseName: string
    :param relationalDatabaseName: [REQUIRED]\nThe name of your database from which to get metric data.\n

    :type metricName: string
    :param metricName: [REQUIRED]\nThe metric for which you want to return information.\nValid relational database metric names are listed below, along with the most useful statistics to include in your request, and the published unit value. All relational database metric data is available in 1-minute (60 seconds) granularity.\n\n**CPUUtilization ** - The percentage of CPU utilization currently in use on the database. Statistics : The most useful statistics are Maximum and Average . Unit : The published unit is Percent .\n**DatabaseConnections ** - The number of database connections in use. Statistics : The most useful statistics are Maximum and Sum . Unit : The published unit is Count .\n**DiskQueueDepth ** - The number of outstanding IOs (read/write requests) that are waiting to access the disk. Statistics : The most useful statistic is Sum . Unit : The published unit is Count .\n**FreeStorageSpace ** - The amount of available storage space. Statistics : The most useful statistic is Sum . Unit : The published unit is Bytes .\n**NetworkReceiveThroughput ** - The incoming (Receive) network traffic on the database, including both customer database traffic and AWS traffic used for monitoring and replication. Statistics : The most useful statistic is Average . Unit : The published unit is Bytes/Second .\n**NetworkTransmitThroughput ** - The outgoing (Transmit) network traffic on the database, including both customer database traffic and AWS traffic used for monitoring and replication. Statistics : The most useful statistic is Average . Unit : The published unit is Bytes/Second .\n\n

    :type period: integer
    :param period: [REQUIRED]\nThe granularity, in seconds, of the returned data points.\nAll relational database metric data is available in 1-minute (60 seconds) granularity.\n

    :type startTime: datetime
    :param startTime: [REQUIRED]\nThe start of the time interval from which to get metric data.\nConstraints:\n\nSpecified in Coordinated Universal Time (UTC).\nSpecified in the Unix time format. For example, if you wish to use a start time of October 1, 2018, at 8 PM UTC, then you input 1538424000 as the start time.\n\n

    :type endTime: datetime
    :param endTime: [REQUIRED]\nThe end of the time interval from which to get metric data.\nConstraints:\n\nSpecified in Coordinated Universal Time (UTC).\nSpecified in the Unix time format. For example, if you wish to use an end time of October 1, 2018, at 8 PM UTC, then you input 1538424000 as the end time.\n\n

    :type unit: string
    :param unit: [REQUIRED]\nThe unit for the metric data request. Valid units depend on the metric data being required. For the valid units with each available metric, see the metricName parameter.\n

    :type statistics: list
    :param statistics: [REQUIRED]\nThe statistic for the metric.\nThe following statistics are available:\n\nMinimum - The lowest value observed during the specified period. Use this value to determine low volumes of activity for your application.\nMaximum - The highest value observed during the specified period. Use this value to determine high volumes of activity for your application.\nSum - All values submitted for the matching metric added together. You can use this statistic to determine the total volume of a metric.\nAverage - The value of Sum / SampleCount during the specified period. By comparing this statistic with the Minimum and Maximum values, you can determine the full scope of a metric and how close the average use is to the Minimum and Maximum values. This comparison helps you to know when to increase or decrease your resources.\nSampleCount - The count, or number, of data points used for the statistical calculation.\n\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'metricName': 'CPUUtilization'|'DatabaseConnections'|'DiskQueueDepth'|'FreeStorageSpace'|'NetworkReceiveThroughput'|'NetworkTransmitThroughput',
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


Response Structure

(dict) --

metricName (string) --
The name of the metric.

metricData (list) --
An object describing the result of your get relational database metric data request.

(dict) --
Describes the metric data point.

average (float) --
The average.

maximum (float) --
The maximum.

minimum (float) --
The minimum.

sampleCount (float) --
The sample count.

sum (float) --
The sum.

timestamp (datetime) --
The timestamp (e.g., 1479816991.349 ).

unit (string) --
The unit.











Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'metricName': 'CPUUtilization'|'DatabaseConnections'|'DiskQueueDepth'|'FreeStorageSpace'|'NetworkReceiveThroughput'|'NetworkTransmitThroughput',
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
    
    
    :returns: 
    Lightsail.Client.exceptions.ServiceException
    Lightsail.Client.exceptions.InvalidInputException
    Lightsail.Client.exceptions.NotFoundException
    Lightsail.Client.exceptions.OperationFailureException
    Lightsail.Client.exceptions.AccessDeniedException
    Lightsail.Client.exceptions.AccountSetupInProgressException
    Lightsail.Client.exceptions.UnauthenticatedException
    
    """
    pass

def get_relational_database_parameters(relationalDatabaseName=None, pageToken=None):
    """
    Returns all of the runtime parameters offered by the underlying database software, or engine, for a specific database in Amazon Lightsail.
    In addition to the parameter names and values, this operation returns other information about each parameter. This information includes whether changes require a reboot, whether the parameter is modifiable, the allowed values, and the data types.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_relational_database_parameters(
        relationalDatabaseName='string',
        pageToken='string'
    )
    
    
    :type relationalDatabaseName: string
    :param relationalDatabaseName: [REQUIRED]\nThe name of your database for which to get parameters.\n

    :type pageToken: string
    :param pageToken: The token to advance to the next page of results from your request.\nTo get a page token, perform an initial GetRelationalDatabaseParameters request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'parameters': [
        {
            'allowedValues': 'string',
            'applyMethod': 'string',
            'applyType': 'string',
            'dataType': 'string',
            'description': 'string',
            'isModifiable': True|False,
            'parameterName': 'string',
            'parameterValue': 'string'
        },
    ],
    'nextPageToken': 'string'
}


Response Structure

(dict) --

parameters (list) --
An object describing the result of your get relational database parameters request.

(dict) --
Describes the parameters of a database.

allowedValues (string) --
Specifies the valid range of values for the parameter.

applyMethod (string) --
Indicates when parameter updates are applied.
Can be immediate or pending-reboot .

applyType (string) --
Specifies the engine-specific parameter type.

dataType (string) --
Specifies the valid data type for the parameter.

description (string) --
Provides a description of the parameter.

isModifiable (boolean) --
A Boolean value indicating whether the parameter can be modified.

parameterName (string) --
Specifies the name of the parameter.

parameterValue (string) --
Specifies the value of the parameter.





nextPageToken (string) --
The token to advance to the next page of resutls from your request.
A next page token is not returned if there are no more results to display.
To get the next page of results, perform another GetRelationalDatabaseParameters request and specify the next page token using the pageToken parameter.







Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'parameters': [
            {
                'allowedValues': 'string',
                'applyMethod': 'string',
                'applyType': 'string',
                'dataType': 'string',
                'description': 'string',
                'isModifiable': True|False,
                'parameterName': 'string',
                'parameterValue': 'string'
            },
        ],
        'nextPageToken': 'string'
    }
    
    
    :returns: 
    Lightsail.Client.exceptions.ServiceException
    Lightsail.Client.exceptions.InvalidInputException
    Lightsail.Client.exceptions.NotFoundException
    Lightsail.Client.exceptions.OperationFailureException
    Lightsail.Client.exceptions.AccessDeniedException
    Lightsail.Client.exceptions.AccountSetupInProgressException
    Lightsail.Client.exceptions.UnauthenticatedException
    
    """
    pass

def get_relational_database_snapshot(relationalDatabaseSnapshotName=None):
    """
    Returns information about a specific database snapshot in Amazon Lightsail.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_relational_database_snapshot(
        relationalDatabaseSnapshotName='string'
    )
    
    
    :type relationalDatabaseSnapshotName: string
    :param relationalDatabaseSnapshotName: [REQUIRED]\nThe name of the database snapshot for which to get information.\n

    :rtype: dict
ReturnsResponse Syntax{
    'relationalDatabaseSnapshot': {
        'name': 'string',
        'arn': 'string',
        'supportCode': 'string',
        'createdAt': datetime(2015, 1, 1),
        'location': {
            'availabilityZone': 'string',
            'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
        },
        'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
        'tags': [
            {
                'key': 'string',
                'value': 'string'
            },
        ],
        'engine': 'string',
        'engineVersion': 'string',
        'sizeInGb': 123,
        'state': 'string',
        'fromRelationalDatabaseName': 'string',
        'fromRelationalDatabaseArn': 'string',
        'fromRelationalDatabaseBundleId': 'string',
        'fromRelationalDatabaseBlueprintId': 'string'
    }
}


Response Structure

(dict) --
relationalDatabaseSnapshot (dict) --An object describing the specified database snapshot.

name (string) --The name of the database snapshot.

arn (string) --The Amazon Resource Name (ARN) of the database snapshot.

supportCode (string) --The support code for the database snapshot. Include this code in your email to support when you have questions about a database snapshot in Lightsail. This code enables our support team to look up your Lightsail information more easily.

createdAt (datetime) --The timestamp when the database snapshot was created.

location (dict) --The Region name and Availability Zone where the database snapshot is located.

availabilityZone (string) --The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --The AWS Region name.



resourceType (string) --The Lightsail resource type.

tags (list) --The tag keys and optional values for the resource. For more information about tags in Lightsail, see the Lightsail Dev Guide .

(dict) --Describes a tag key and optional value assigned to an Amazon Lightsail resource.
For more information about tags in Lightsail, see the Lightsail Dev Guide .

key (string) --The key of the tag.
Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @

value (string) --The value of the tag.
Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @





engine (string) --The software of the database snapshot (for example, MySQL )

engineVersion (string) --The database engine version for the database snapshot (for example, 5.7.23 ).

sizeInGb (integer) --The size of the disk in GB (for example, 32 ) for the database snapshot.

state (string) --The state of the database snapshot.

fromRelationalDatabaseName (string) --The name of the source database from which the database snapshot was created.

fromRelationalDatabaseArn (string) --The Amazon Resource Name (ARN) of the database from which the database snapshot was created.

fromRelationalDatabaseBundleId (string) --The bundle ID of the database from which the database snapshot was created.

fromRelationalDatabaseBlueprintId (string) --The blueprint ID of the database from which the database snapshot was created. A blueprint describes the major engine version of a database.








Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'relationalDatabaseSnapshot': {
            'name': 'string',
            'arn': 'string',
            'supportCode': 'string',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ],
            'engine': 'string',
            'engineVersion': 'string',
            'sizeInGb': 123,
            'state': 'string',
            'fromRelationalDatabaseName': 'string',
            'fromRelationalDatabaseArn': 'string',
            'fromRelationalDatabaseBundleId': 'string',
            'fromRelationalDatabaseBlueprintId': 'string'
        }
    }
    
    
    """
    pass

def get_relational_database_snapshots(pageToken=None):
    """
    Returns information about all of your database snapshots in Amazon Lightsail.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_relational_database_snapshots(
        pageToken='string'
    )
    
    
    :type pageToken: string
    :param pageToken: The token to advance to the next page of results from your request.\nTo get a page token, perform an initial GetRelationalDatabaseSnapshots request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.\n

    :rtype: dict
ReturnsResponse Syntax{
    'relationalDatabaseSnapshots': [
        {
            'name': 'string',
            'arn': 'string',
            'supportCode': 'string',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ],
            'engine': 'string',
            'engineVersion': 'string',
            'sizeInGb': 123,
            'state': 'string',
            'fromRelationalDatabaseName': 'string',
            'fromRelationalDatabaseArn': 'string',
            'fromRelationalDatabaseBundleId': 'string',
            'fromRelationalDatabaseBlueprintId': 'string'
        },
    ],
    'nextPageToken': 'string'
}


Response Structure

(dict) --
relationalDatabaseSnapshots (list) --An object describing the result of your get relational database snapshots request.

(dict) --Describes a database snapshot.

name (string) --The name of the database snapshot.

arn (string) --The Amazon Resource Name (ARN) of the database snapshot.

supportCode (string) --The support code for the database snapshot. Include this code in your email to support when you have questions about a database snapshot in Lightsail. This code enables our support team to look up your Lightsail information more easily.

createdAt (datetime) --The timestamp when the database snapshot was created.

location (dict) --The Region name and Availability Zone where the database snapshot is located.

availabilityZone (string) --The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --The AWS Region name.



resourceType (string) --The Lightsail resource type.

tags (list) --The tag keys and optional values for the resource. For more information about tags in Lightsail, see the Lightsail Dev Guide .

(dict) --Describes a tag key and optional value assigned to an Amazon Lightsail resource.
For more information about tags in Lightsail, see the Lightsail Dev Guide .

key (string) --The key of the tag.
Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @

value (string) --The value of the tag.
Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @





engine (string) --The software of the database snapshot (for example, MySQL )

engineVersion (string) --The database engine version for the database snapshot (for example, 5.7.23 ).

sizeInGb (integer) --The size of the disk in GB (for example, 32 ) for the database snapshot.

state (string) --The state of the database snapshot.

fromRelationalDatabaseName (string) --The name of the source database from which the database snapshot was created.

fromRelationalDatabaseArn (string) --The Amazon Resource Name (ARN) of the database from which the database snapshot was created.

fromRelationalDatabaseBundleId (string) --The bundle ID of the database from which the database snapshot was created.

fromRelationalDatabaseBlueprintId (string) --The blueprint ID of the database from which the database snapshot was created. A blueprint describes the major engine version of a database.





nextPageToken (string) --The token to advance to the next page of resutls from your request.
A next page token is not returned if there are no more results to display.
To get the next page of results, perform another GetRelationalDatabaseSnapshots request and specify the next page token using the pageToken parameter.






Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'relationalDatabaseSnapshots': [
            {
                'name': 'string',
                'arn': 'string',
                'supportCode': 'string',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ],
                'engine': 'string',
                'engineVersion': 'string',
                'sizeInGb': 123,
                'state': 'string',
                'fromRelationalDatabaseName': 'string',
                'fromRelationalDatabaseArn': 'string',
                'fromRelationalDatabaseBundleId': 'string',
                'fromRelationalDatabaseBlueprintId': 'string'
            },
        ],
        'nextPageToken': 'string'
    }
    
    
    """
    pass

def get_relational_databases(pageToken=None):
    """
    Returns information about all of your databases in Amazon Lightsail.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_relational_databases(
        pageToken='string'
    )
    
    
    :type pageToken: string
    :param pageToken: The token to advance to the next page of results from your request.\nTo get a page token, perform an initial GetRelationalDatabases request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.\n

    :rtype: dict
ReturnsResponse Syntax{
    'relationalDatabases': [
        {
            'name': 'string',
            'arn': 'string',
            'supportCode': 'string',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ],
            'relationalDatabaseBlueprintId': 'string',
            'relationalDatabaseBundleId': 'string',
            'masterDatabaseName': 'string',
            'hardware': {
                'cpuCount': 123,
                'diskSizeInGb': 123,
                'ramSizeInGb': ...
            },
            'state': 'string',
            'secondaryAvailabilityZone': 'string',
            'backupRetentionEnabled': True|False,
            'pendingModifiedValues': {
                'masterUserPassword': 'string',
                'engineVersion': 'string',
                'backupRetentionEnabled': True|False
            },
            'engine': 'string',
            'engineVersion': 'string',
            'latestRestorableTime': datetime(2015, 1, 1),
            'masterUsername': 'string',
            'parameterApplyStatus': 'string',
            'preferredBackupWindow': 'string',
            'preferredMaintenanceWindow': 'string',
            'publiclyAccessible': True|False,
            'masterEndpoint': {
                'port': 123,
                'address': 'string'
            },
            'pendingMaintenanceActions': [
                {
                    'action': 'string',
                    'description': 'string',
                    'currentApplyDate': datetime(2015, 1, 1)
                },
            ],
            'caCertificateIdentifier': 'string'
        },
    ],
    'nextPageToken': 'string'
}


Response Structure

(dict) --
relationalDatabases (list) --An object describing the result of your get relational databases request.

(dict) --Describes a database.

name (string) --The unique name of the database resource in Lightsail.

arn (string) --The Amazon Resource Name (ARN) of the database.

supportCode (string) --The support code for the database. Include this code in your email to support when you have questions about a database in Lightsail. This code enables our support team to look up your Lightsail information more easily.

createdAt (datetime) --The timestamp when the database was created. Formatted in Unix time.

location (dict) --The Region name and Availability Zone where the database is located.

availabilityZone (string) --The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --The AWS Region name.



resourceType (string) --The Lightsail resource type for the database (for example, RelationalDatabase ).

tags (list) --The tag keys and optional values for the resource. For more information about tags in Lightsail, see the Lightsail Dev Guide .

(dict) --Describes a tag key and optional value assigned to an Amazon Lightsail resource.
For more information about tags in Lightsail, see the Lightsail Dev Guide .

key (string) --The key of the tag.
Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @

value (string) --The value of the tag.
Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @





relationalDatabaseBlueprintId (string) --The blueprint ID for the database. A blueprint describes the major engine version of a database.

relationalDatabaseBundleId (string) --The bundle ID for the database. A bundle describes the performance specifications for your database.

masterDatabaseName (string) --The name of the master database created when the Lightsail database resource is created.

hardware (dict) --Describes the hardware of the database.

cpuCount (integer) --The number of vCPUs for the database.

diskSizeInGb (integer) --The size of the disk for the database.

ramSizeInGb (float) --The amount of RAM in GB for the database.



state (string) --Describes the current state of the database.

secondaryAvailabilityZone (string) --Describes the secondary Availability Zone of a high availability database.
The secondary database is used for failover support of a high availability database.

backupRetentionEnabled (boolean) --A Boolean value indicating whether automated backup retention is enabled for the database.

pendingModifiedValues (dict) --Describes pending database value modifications.

masterUserPassword (string) --The password for the master user of the database.

engineVersion (string) --The database engine version.

backupRetentionEnabled (boolean) --A Boolean value indicating whether automated backup retention is enabled.



engine (string) --The database software (for example, MySQL ).

engineVersion (string) --The database engine version (for example, 5.7.23 ).

latestRestorableTime (datetime) --The latest point in time to which the database can be restored. Formatted in Unix time.

masterUsername (string) --The master user name of the database.

parameterApplyStatus (string) --The status of parameter updates for the database.

preferredBackupWindow (string) --The daily time range during which automated backups are created for the database (for example, 16:00-16:30 ).

preferredMaintenanceWindow (string) --The weekly time range during which system maintenance can occur on the database.
In the format ddd:hh24:mi-ddd:hh24:mi . For example, Tue:17:00-Tue:17:30 .

publiclyAccessible (boolean) --A Boolean value indicating whether the database is publicly accessible.

masterEndpoint (dict) --The master endpoint for the database.

port (integer) --Specifies the port that the database is listening on.

address (string) --Specifies the DNS address of the database.



pendingMaintenanceActions (list) --Describes the pending maintenance actions for the database.

(dict) --Describes a pending database maintenance action.

action (string) --The type of pending database maintenance action.

description (string) --Additional detail about the pending database maintenance action.

currentApplyDate (datetime) --The effective date of the pending database maintenance action.





caCertificateIdentifier (string) --The certificate associated with the database.





nextPageToken (string) --The token to advance to the next page of resutls from your request.
A next page token is not returned if there are no more results to display.
To get the next page of results, perform another GetRelationalDatabases request and specify the next page token using the pageToken parameter.






Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'relationalDatabases': [
            {
                'name': 'string',
                'arn': 'string',
                'supportCode': 'string',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ],
                'relationalDatabaseBlueprintId': 'string',
                'relationalDatabaseBundleId': 'string',
                'masterDatabaseName': 'string',
                'hardware': {
                    'cpuCount': 123,
                    'diskSizeInGb': 123,
                    'ramSizeInGb': ...
                },
                'state': 'string',
                'secondaryAvailabilityZone': 'string',
                'backupRetentionEnabled': True|False,
                'pendingModifiedValues': {
                    'masterUserPassword': 'string',
                    'engineVersion': 'string',
                    'backupRetentionEnabled': True|False
                },
                'engine': 'string',
                'engineVersion': 'string',
                'latestRestorableTime': datetime(2015, 1, 1),
                'masterUsername': 'string',
                'parameterApplyStatus': 'string',
                'preferredBackupWindow': 'string',
                'preferredMaintenanceWindow': 'string',
                'publiclyAccessible': True|False,
                'masterEndpoint': {
                    'port': 123,
                    'address': 'string'
                },
                'pendingMaintenanceActions': [
                    {
                        'action': 'string',
                        'description': 'string',
                        'currentApplyDate': datetime(2015, 1, 1)
                    },
                ],
                'caCertificateIdentifier': 'string'
            },
        ],
        'nextPageToken': 'string'
    }
    
    
    """
    pass

def get_static_ip(staticIpName=None):
    """
    Returns information about a specific static IP.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_static_ip(
        staticIpName='string'
    )
    
    
    :type staticIpName: string
    :param staticIpName: [REQUIRED]\nThe name of the static IP in Lightsail.\n

    :rtype: dict
ReturnsResponse Syntax{
    'staticIp': {
        'name': 'string',
        'arn': 'string',
        'supportCode': 'string',
        'createdAt': datetime(2015, 1, 1),
        'location': {
            'availabilityZone': 'string',
            'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
        },
        'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
        'ipAddress': 'string',
        'attachedTo': 'string',
        'isAttached': True|False
    }
}


Response Structure

(dict) --
staticIp (dict) --An array of key-value pairs containing information about the requested static IP.

name (string) --The name of the static IP (e.g., StaticIP-Ohio-EXAMPLE ).

arn (string) --The Amazon Resource Name (ARN) of the static IP (e.g., arn:aws:lightsail:us-east-2:123456789101:StaticIp/9cbb4a9e-f8e3-4dfe-b57e-12345EXAMPLE ).

supportCode (string) --The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.

createdAt (datetime) --The timestamp when the static IP was created (e.g., 1479735304.222 ).

location (dict) --The region and Availability Zone where the static IP was created.

availabilityZone (string) --The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --The AWS Region name.



resourceType (string) --The resource type (usually StaticIp ).

ipAddress (string) --The static IP address.

attachedTo (string) --The instance where the static IP is attached (e.g., Amazon_Linux-1GB-Ohio-1 ).

isAttached (boolean) --A Boolean value indicating whether the static IP is attached.








Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'staticIp': {
            'name': 'string',
            'arn': 'string',
            'supportCode': 'string',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'ipAddress': 'string',
            'attachedTo': 'string',
            'isAttached': True|False
        }
    }
    
    
    """
    pass

def get_static_ips(pageToken=None):
    """
    Returns information about all static IPs in the user\'s account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_static_ips(
        pageToken='string'
    )
    
    
    :type pageToken: string
    :param pageToken: The token to advance to the next page of results from your request.\nTo get a page token, perform an initial GetStaticIps request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.\n

    :rtype: dict
ReturnsResponse Syntax{
    'staticIps': [
        {
            'name': 'string',
            'arn': 'string',
            'supportCode': 'string',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'ipAddress': 'string',
            'attachedTo': 'string',
            'isAttached': True|False
        },
    ],
    'nextPageToken': 'string'
}


Response Structure

(dict) --
staticIps (list) --An array of key-value pairs containing information about your get static IPs request.

(dict) --Describes the static IP.

name (string) --The name of the static IP (e.g., StaticIP-Ohio-EXAMPLE ).

arn (string) --The Amazon Resource Name (ARN) of the static IP (e.g., arn:aws:lightsail:us-east-2:123456789101:StaticIp/9cbb4a9e-f8e3-4dfe-b57e-12345EXAMPLE ).

supportCode (string) --The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.

createdAt (datetime) --The timestamp when the static IP was created (e.g., 1479735304.222 ).

location (dict) --The region and Availability Zone where the static IP was created.

availabilityZone (string) --The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --The AWS Region name.



resourceType (string) --The resource type (usually StaticIp ).

ipAddress (string) --The static IP address.

attachedTo (string) --The instance where the static IP is attached (e.g., Amazon_Linux-1GB-Ohio-1 ).

isAttached (boolean) --A Boolean value indicating whether the static IP is attached.





nextPageToken (string) --The token to advance to the next page of resutls from your request.
A next page token is not returned if there are no more results to display.
To get the next page of results, perform another GetStaticIps request and specify the next page token using the pageToken parameter.






Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'staticIps': [
            {
                'name': 'string',
                'arn': 'string',
                'supportCode': 'string',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'ipAddress': 'string',
                'attachedTo': 'string',
                'isAttached': True|False
            },
        ],
        'nextPageToken': 'string'
    }
    
    
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

def import_key_pair(keyPairName=None, publicKeyBase64=None):
    """
    Imports a public SSH key from a specific key pair.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.import_key_pair(
        keyPairName='string',
        publicKeyBase64='string'
    )
    
    
    :type keyPairName: string
    :param keyPairName: [REQUIRED]\nThe name of the key pair for which you want to import the public key.\n

    :type publicKeyBase64: string
    :param publicKeyBase64: [REQUIRED]\nA base64-encoded public key of the ssh-rsa type.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'operation': {
        'id': 'string',
        'resourceName': 'string',
        'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
        'createdAt': datetime(2015, 1, 1),
        'location': {
            'availabilityZone': 'string',
            'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
        },
        'isTerminal': True|False,
        'operationDetails': 'string',
        'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
        'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
        'statusChangedAt': datetime(2015, 1, 1),
        'errorCode': 'string',
        'errorDetails': 'string'
    }
}


Response Structure

(dict) --

operation (dict) --
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

id (string) --
The ID of the operation.

resourceName (string) --
The resource name.

resourceType (string) --
The resource type.

createdAt (datetime) --
The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --
The AWS Region and Availability Zone.

availabilityZone (string) --
The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --
The AWS Region name.



isTerminal (boolean) --
A Boolean value indicating whether the operation is terminal.

operationDetails (string) --
Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --
The type of operation.

status (string) --
The status of the operation.

statusChangedAt (datetime) --
The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --
The error code.

errorDetails (string) --
The error details.









Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operation': {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        }
    }
    
    
    :returns: 
    Lightsail.Client.exceptions.ServiceException
    Lightsail.Client.exceptions.InvalidInputException
    Lightsail.Client.exceptions.NotFoundException
    Lightsail.Client.exceptions.OperationFailureException
    Lightsail.Client.exceptions.AccessDeniedException
    Lightsail.Client.exceptions.AccountSetupInProgressException
    Lightsail.Client.exceptions.UnauthenticatedException
    
    """
    pass

def is_vpc_peered():
    """
    Returns a Boolean value indicating whether your Lightsail VPC is peered.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.is_vpc_peered()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'isPeered': True|False
}


Response Structure

(dict) --
isPeered (boolean) --Returns true if the Lightsail VPC is peered; otherwise, false .






Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'isPeered': True|False
    }
    
    
    """
    pass

def open_instance_public_ports(portInfo=None, instanceName=None):
    """
    Opens ports for a specific Amazon Lightsail instance, and specifies the IP addresses allowed to connect to the instance through the ports, and the protocol.
    The OpenInstancePublicPorts action supports tag-based access control via resource tags applied to the resource identified by instanceName . For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.open_instance_public_ports(
        portInfo={
            'fromPort': 123,
            'toPort': 123,
            'protocol': 'tcp'|'all'|'udp'|'icmp',
            'cidrs': [
                'string',
            ],
            'cidrListAliases': [
                'string',
            ]
        },
        instanceName='string'
    )
    
    
    :type portInfo: dict
    :param portInfo: [REQUIRED]\nAn object to describe the ports to open for the specified instance.\n\nfromPort (integer) --The first port in a range of open ports on an instance.\nAllowed ports:\n\nTCP and UDP - 0 to 65535\nICMP - 8 (to configure Ping)\n\n\nNote\nPing is the only communication supported through the ICMP protocol in Lightsail. To configure ping, specify the fromPort parameter as 8 , and the toPort parameter as -1 .\n\n\ntoPort (integer) --The last port in a range of open ports on an instance.\nAllowed ports:\n\nTCP and UDP - 0 to 65535\nICMP - -1 (to configure Ping)\n\n\nNote\nPing is the only communication supported through the ICMP protocol in Lightsail. To configure ping, specify the fromPort parameter as 8 , and the toPort parameter as -1 .\n\n\nprotocol (string) --The IP protocol name.\nThe name can be one of the following:\n\ntcp - Transmission Control Protocol (TCP) provides reliable, ordered, and error-checked delivery of streamed data between applications running on hosts communicating by an IP network. If you have an application that doesn\'t require reliable data stream service, use UDP instead.\nall - All transport layer protocol types. For more general information, see Transport layer on Wikipedia .\nudp - With User Datagram Protocol (UDP), computer applications can send messages (or datagrams) to other hosts on an Internet Protocol (IP) network. Prior communications are not required to set up transmission channels or data paths. Applications that don\'t require reliable data stream service can use UDP, which provides a connectionless datagram service that emphasizes reduced latency over reliability. If you do require reliable data stream service, use TCP instead.\nicmp - Internet Control Message Protocol (ICMP) is used to send error messages and operational information indicating success or failure when communicating with an instance. For example, an error is indicated when an instance could not be reached.\n\n\nNote\nPing is the only communication supported through the ICMP protocol in Lightsail. To configure ping, specify the fromPort parameter as 8 , and the toPort parameter as -1 .\n\n\ncidrs (list) --The IP address, or range of IP addresses in CIDR notation, that are allowed to connect to an instance through the ports, and the protocol. Lightsail supports IPv4 addresses.\nExamples:\n\nTo allow the IP address 192.0.2.44 , specify 192.0.2.44 or 192.0.2.44/32 .\nTo allow the IP addresses 192.0.2.0 to 192.0.2.255 , specify 192.0.2.0/24 .\n\nFor more information about CIDR block notation, see Classless Inter-Domain Routing on Wikipedia .\n\n(string) --\n\n\ncidrListAliases (list) --An alias that defines access for a preconfigured range of IP addresses.\nThe only alias currently supported is lightsail-connect , which allows IP addresses of the browser-based RDP/SSH client in the Lightsail console to connect to your instance.\n\n(string) --\n\n\n\n

    :type instanceName: string
    :param instanceName: [REQUIRED]\nThe name of the instance for which to open ports.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'operation': {
        'id': 'string',
        'resourceName': 'string',
        'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
        'createdAt': datetime(2015, 1, 1),
        'location': {
            'availabilityZone': 'string',
            'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
        },
        'isTerminal': True|False,
        'operationDetails': 'string',
        'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
        'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
        'statusChangedAt': datetime(2015, 1, 1),
        'errorCode': 'string',
        'errorDetails': 'string'
    }
}


Response Structure

(dict) --

operation (dict) --
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

id (string) --
The ID of the operation.

resourceName (string) --
The resource name.

resourceType (string) --
The resource type.

createdAt (datetime) --
The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --
The AWS Region and Availability Zone.

availabilityZone (string) --
The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --
The AWS Region name.



isTerminal (boolean) --
A Boolean value indicating whether the operation is terminal.

operationDetails (string) --
Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --
The type of operation.

status (string) --
The status of the operation.

statusChangedAt (datetime) --
The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --
The error code.

errorDetails (string) --
The error details.









Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operation': {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        }
    }
    
    
    :returns: 
    Lightsail.Client.exceptions.ServiceException
    Lightsail.Client.exceptions.InvalidInputException
    Lightsail.Client.exceptions.NotFoundException
    Lightsail.Client.exceptions.OperationFailureException
    Lightsail.Client.exceptions.AccessDeniedException
    Lightsail.Client.exceptions.AccountSetupInProgressException
    Lightsail.Client.exceptions.UnauthenticatedException
    
    """
    pass

def peer_vpc():
    """
    Tries to peer the Lightsail VPC with the user\'s default VPC.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.peer_vpc()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'operation': {
        'id': 'string',
        'resourceName': 'string',
        'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
        'createdAt': datetime(2015, 1, 1),
        'location': {
            'availabilityZone': 'string',
            'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
        },
        'isTerminal': True|False,
        'operationDetails': 'string',
        'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
        'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
        'statusChangedAt': datetime(2015, 1, 1),
        'errorCode': 'string',
        'errorDetails': 'string'
    }
}


Response Structure

(dict) --
operation (dict) --An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

id (string) --The ID of the operation.

resourceName (string) --The resource name.

resourceType (string) --The resource type.

createdAt (datetime) --The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --The AWS Region and Availability Zone.

availabilityZone (string) --The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --The AWS Region name.



isTerminal (boolean) --A Boolean value indicating whether the operation is terminal.

operationDetails (string) --Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --The type of operation.

status (string) --The status of the operation.

statusChangedAt (datetime) --The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --The error code.

errorDetails (string) --The error details.








Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operation': {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        }
    }
    
    
    """
    pass

def put_alarm(alarmName=None, metricName=None, monitoredResourceName=None, comparisonOperator=None, threshold=None, evaluationPeriods=None, datapointsToAlarm=None, treatMissingData=None, contactProtocols=None, notificationTriggers=None, notificationEnabled=None):
    """
    Creates or updates an alarm, and associates it with the specified metric.
    An alarm is used to monitor a single metric for one of your resources. When a metric condition is met, the alarm can notify you by email, SMS text message, and a banner displayed on the Amazon Lightsail console. For more information, see Alarms in Amazon Lightsail .
    When this action creates an alarm, the alarm state is immediately set to INSUFFICIENT_DATA . The alarm is then evaluated and its state is set appropriately. Any actions associated with the new state are then executed.
    When you update an existing alarm, its state is left unchanged, but the update completely overwrites the previous configuration of the alarm. The alarm is then evaluated with the updated configuration.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_alarm(
        alarmName='string',
        metricName='CPUUtilization'|'NetworkIn'|'NetworkOut'|'StatusCheckFailed'|'StatusCheckFailed_Instance'|'StatusCheckFailed_System'|'ClientTLSNegotiationErrorCount'|'HealthyHostCount'|'UnhealthyHostCount'|'HTTPCode_LB_4XX_Count'|'HTTPCode_LB_5XX_Count'|'HTTPCode_Instance_2XX_Count'|'HTTPCode_Instance_3XX_Count'|'HTTPCode_Instance_4XX_Count'|'HTTPCode_Instance_5XX_Count'|'InstanceResponseTime'|'RejectedConnectionCount'|'RequestCount'|'DatabaseConnections'|'DiskQueueDepth'|'FreeStorageSpace'|'NetworkReceiveThroughput'|'NetworkTransmitThroughput',
        monitoredResourceName='string',
        comparisonOperator='GreaterThanOrEqualToThreshold'|'GreaterThanThreshold'|'LessThanThreshold'|'LessThanOrEqualToThreshold',
        threshold=123.0,
        evaluationPeriods=123,
        datapointsToAlarm=123,
        treatMissingData='breaching'|'notBreaching'|'ignore'|'missing',
        contactProtocols=[
            'Email'|'SMS',
        ],
        notificationTriggers=[
            'OK'|'ALARM'|'INSUFFICIENT_DATA',
        ],
        notificationEnabled=True|False
    )
    
    
    :type alarmName: string
    :param alarmName: [REQUIRED]\nThe name for the alarm. Specify the name of an existing alarm to update, and overwrite the previous configuration of the alarm.\n

    :type metricName: string
    :param metricName: [REQUIRED]\nThe name of the metric to associate with the alarm.\nYou can configure up to two alarms per metric.\nThe following metrics are available for each resource type:\n\nInstances : CPUUtilization , NetworkIn , NetworkOut , StatusCheckFailed , StatusCheckFailed_Instance , and StatusCheckFailed_System .\nLoad balancers : ClientTLSNegotiationErrorCount , HealthyHostCount , UnhealthyHostCount , HTTPCode_LB_4XX_Count , HTTPCode_LB_5XX_Count , HTTPCode_Instance_2XX_Count , HTTPCode_Instance_3XX_Count , HTTPCode_Instance_4XX_Count , HTTPCode_Instance_5XX_Count , InstanceResponseTime , RejectedConnectionCount , and RequestCount .\nRelational databases : CPUUtilization , DatabaseConnections , DiskQueueDepth , FreeStorageSpace , NetworkReceiveThroughput , and NetworkTransmitThroughput .\n\n

    :type monitoredResourceName: string
    :param monitoredResourceName: [REQUIRED]\nThe name of the Lightsail resource that will be monitored.\nInstances, load balancers, and relational databases are the only Lightsail resources that can currently be monitored by alarms.\n

    :type comparisonOperator: string
    :param comparisonOperator: [REQUIRED]\nThe arithmetic operation to use when comparing the specified statistic to the threshold. The specified statistic value is used as the first operand.\n

    :type threshold: float
    :param threshold: [REQUIRED]\nThe value against which the specified statistic is compared.\n

    :type evaluationPeriods: integer
    :param evaluationPeriods: [REQUIRED]\nThe number of most recent periods over which data is compared to the specified threshold. If you are setting an 'M out of N' alarm, this value (evaluationPeriods ) is the N.\nIf you are setting an alarm that requires that a number of consecutive data points be breaching to trigger the alarm, this value specifies the rolling period of time in which data points are evaluated.\nEach evaluation period is five minutes long. For example, specify an evaluation period of 24 to evaluate a metric over a rolling period of two hours.\nYou can specify a minimum valuation period of 1 (5 minutes), and a maximum evaluation period of 288 (24 hours).\n

    :type datapointsToAlarm: integer
    :param datapointsToAlarm: The number of data points that must be not within the specified threshold to trigger the alarm. If you are setting an 'M out of N' alarm, this value (datapointsToAlarm ) is the M.

    :type treatMissingData: string
    :param treatMissingData: Sets how this alarm will handle missing data points.\nAn alarm can treat missing data in the following ways:\n\nbreaching - Assume the missing data is not within the threshold. Missing data counts towards the number of times the metric is not within the threshold.\nnotBreaching - Assume the missing data is within the threshold. Missing data does not count towards the number of times the metric is not within the threshold.\nignore - Ignore the missing data. Maintains the current alarm state.\nmissing - Missing data is treated as missing.\n\nIf treatMissingData is not specified, the default behavior of missing is used.\n

    :type contactProtocols: list
    :param contactProtocols: The contact protocols to use for the alarm, such as Email , SMS (text messaging), or both.\nA notification is sent via the specified contact protocol if notifications are enabled for the alarm, and when the alarm is triggered.\nA notification is not sent if a contact protocol is not specified, if the specified contact protocol is not configured in the AWS Region, or if notifications are not enabled for the alarm using the notificationEnabled paramater.\nUse the CreateContactMethod action to configure a contact protocol in an AWS Region.\n\n(string) --\n\n

    :type notificationTriggers: list
    :param notificationTriggers: The alarm states that trigger a notification.\nAn alarm has the following possible states:\n\nALARM - The metric is outside of the defined threshold.\nINSUFFICIENT_DATA - The alarm has just started, the metric is not available, or not enough data is available for the metric to determine the alarm state.\nOK - The metric is within the defined threshold.\n\nWhen you specify a notification trigger, the ALARM state must be specified. The INSUFFICIENT_DATA and OK states can be specified in addition to the ALARM state.\n\nIf you specify OK as an alarm trigger, a notification is sent when the alarm switches from an ALARM or INSUFFICIENT_DATA alarm state to an OK state. This can be thought of as an all clear alarm notification.\nIf you specify INSUFFICIENT_DATA as the alarm trigger, a notification is sent when the alarm switches from an OK or ALARM alarm state to an INSUFFICIENT_DATA state.\n\nThe notification trigger defaults to ALARM if you don\'t specify this parameter.\n\n(string) --\n\n

    :type notificationEnabled: boolean
    :param notificationEnabled: Indicates whether the alarm is enabled.\nNotifications are enabled by default if you don\'t specify this parameter.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'operations': [
        {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        },
    ]
}


Response Structure

(dict) --

operations (list) --
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

(dict) --
Describes the API operation.

id (string) --
The ID of the operation.

resourceName (string) --
The resource name.

resourceType (string) --
The resource type.

createdAt (datetime) --
The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --
The AWS Region and Availability Zone.

availabilityZone (string) --
The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --
The AWS Region name.



isTerminal (boolean) --
A Boolean value indicating whether the operation is terminal.

operationDetails (string) --
Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --
The type of operation.

status (string) --
The status of the operation.

statusChangedAt (datetime) --
The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --
The error code.

errorDetails (string) --
The error details.











Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.UnauthenticatedException
Lightsail.Client.exceptions.NotFoundException


    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    :returns: 
    Lightsail.Client.exceptions.ServiceException
    Lightsail.Client.exceptions.InvalidInputException
    Lightsail.Client.exceptions.OperationFailureException
    Lightsail.Client.exceptions.AccessDeniedException
    Lightsail.Client.exceptions.UnauthenticatedException
    Lightsail.Client.exceptions.NotFoundException
    
    """
    pass

def put_instance_public_ports(portInfos=None, instanceName=None):
    """
    Opens ports for a specific Amazon Lightsail instance, and specifies the IP addresses allowed to connect to the instance through the ports, and the protocol. This action also closes all currently open ports that are not included in the request. Include all of the ports and the protocols you want to open in your PutInstancePublicPorts request. Or use the OpenInstancePublicPorts action to open ports without closing currently open ports.
    The PutInstancePublicPorts action supports tag-based access control via resource tags applied to the resource identified by instanceName . For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_instance_public_ports(
        portInfos=[
            {
                'fromPort': 123,
                'toPort': 123,
                'protocol': 'tcp'|'all'|'udp'|'icmp',
                'cidrs': [
                    'string',
                ],
                'cidrListAliases': [
                    'string',
                ]
            },
        ],
        instanceName='string'
    )
    
    
    :type portInfos: list
    :param portInfos: [REQUIRED]\nAn array of objects to describe the ports to open for the specified instance.\n\n(dict) --Describes ports to open on an instance, the IP addresses allowed to connect to the instance through the ports, and the protocol.\n\nfromPort (integer) --The first port in a range of open ports on an instance.\nAllowed ports:\n\nTCP and UDP - 0 to 65535\nICMP - 8 (to configure Ping)\n\n\nNote\nPing is the only communication supported through the ICMP protocol in Lightsail. To configure ping, specify the fromPort parameter as 8 , and the toPort parameter as -1 .\n\n\ntoPort (integer) --The last port in a range of open ports on an instance.\nAllowed ports:\n\nTCP and UDP - 0 to 65535\nICMP - -1 (to configure Ping)\n\n\nNote\nPing is the only communication supported through the ICMP protocol in Lightsail. To configure ping, specify the fromPort parameter as 8 , and the toPort parameter as -1 .\n\n\nprotocol (string) --The IP protocol name.\nThe name can be one of the following:\n\ntcp - Transmission Control Protocol (TCP) provides reliable, ordered, and error-checked delivery of streamed data between applications running on hosts communicating by an IP network. If you have an application that doesn\'t require reliable data stream service, use UDP instead.\nall - All transport layer protocol types. For more general information, see Transport layer on Wikipedia .\nudp - With User Datagram Protocol (UDP), computer applications can send messages (or datagrams) to other hosts on an Internet Protocol (IP) network. Prior communications are not required to set up transmission channels or data paths. Applications that don\'t require reliable data stream service can use UDP, which provides a connectionless datagram service that emphasizes reduced latency over reliability. If you do require reliable data stream service, use TCP instead.\nicmp - Internet Control Message Protocol (ICMP) is used to send error messages and operational information indicating success or failure when communicating with an instance. For example, an error is indicated when an instance could not be reached.\n\n\nNote\nPing is the only communication supported through the ICMP protocol in Lightsail. To configure ping, specify the fromPort parameter as 8 , and the toPort parameter as -1 .\n\n\ncidrs (list) --The IP address, or range of IP addresses in CIDR notation, that are allowed to connect to an instance through the ports, and the protocol. Lightsail supports IPv4 addresses.\nExamples:\n\nTo allow the IP address 192.0.2.44 , specify 192.0.2.44 or 192.0.2.44/32 .\nTo allow the IP addresses 192.0.2.0 to 192.0.2.255 , specify 192.0.2.0/24 .\n\nFor more information about CIDR block notation, see Classless Inter-Domain Routing on Wikipedia .\n\n(string) --\n\n\ncidrListAliases (list) --An alias that defines access for a preconfigured range of IP addresses.\nThe only alias currently supported is lightsail-connect , which allows IP addresses of the browser-based RDP/SSH client in the Lightsail console to connect to your instance.\n\n(string) --\n\n\n\n\n\n

    :type instanceName: string
    :param instanceName: [REQUIRED]\nThe name of the instance for which to open ports.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'operation': {
        'id': 'string',
        'resourceName': 'string',
        'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
        'createdAt': datetime(2015, 1, 1),
        'location': {
            'availabilityZone': 'string',
            'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
        },
        'isTerminal': True|False,
        'operationDetails': 'string',
        'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
        'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
        'statusChangedAt': datetime(2015, 1, 1),
        'errorCode': 'string',
        'errorDetails': 'string'
    }
}


Response Structure

(dict) --

operation (dict) --
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

id (string) --
The ID of the operation.

resourceName (string) --
The resource name.

resourceType (string) --
The resource type.

createdAt (datetime) --
The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --
The AWS Region and Availability Zone.

availabilityZone (string) --
The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --
The AWS Region name.



isTerminal (boolean) --
A Boolean value indicating whether the operation is terminal.

operationDetails (string) --
Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --
The type of operation.

status (string) --
The status of the operation.

statusChangedAt (datetime) --
The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --
The error code.

errorDetails (string) --
The error details.









Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operation': {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        }
    }
    
    
    :returns: 
    Lightsail.Client.exceptions.ServiceException
    Lightsail.Client.exceptions.InvalidInputException
    Lightsail.Client.exceptions.NotFoundException
    Lightsail.Client.exceptions.OperationFailureException
    Lightsail.Client.exceptions.AccessDeniedException
    Lightsail.Client.exceptions.AccountSetupInProgressException
    Lightsail.Client.exceptions.UnauthenticatedException
    
    """
    pass

def reboot_instance(instanceName=None):
    """
    Restarts a specific instance.
    The reboot instance operation supports tag-based access control via resource tags applied to the resource identified by instance name . For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.reboot_instance(
        instanceName='string'
    )
    
    
    :type instanceName: string
    :param instanceName: [REQUIRED]\nThe name of the instance to reboot.\n

    :rtype: dict
ReturnsResponse Syntax{
    'operations': [
        {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        },
    ]
}


Response Structure

(dict) --
operations (list) --An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

(dict) --Describes the API operation.

id (string) --The ID of the operation.

resourceName (string) --The resource name.

resourceType (string) --The resource type.

createdAt (datetime) --The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --The AWS Region and Availability Zone.

availabilityZone (string) --The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --The AWS Region name.



isTerminal (boolean) --A Boolean value indicating whether the operation is terminal.

operationDetails (string) --Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --The type of operation.

status (string) --The status of the operation.

statusChangedAt (datetime) --The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --The error code.

errorDetails (string) --The error details.










Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def reboot_relational_database(relationalDatabaseName=None):
    """
    Restarts a specific database in Amazon Lightsail.
    The reboot relational database operation supports tag-based access control via resource tags applied to the resource identified by relationalDatabaseName. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.reboot_relational_database(
        relationalDatabaseName='string'
    )
    
    
    :type relationalDatabaseName: string
    :param relationalDatabaseName: [REQUIRED]\nThe name of your database to reboot.\n

    :rtype: dict
ReturnsResponse Syntax{
    'operations': [
        {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        },
    ]
}


Response Structure

(dict) --
operations (list) --An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

(dict) --Describes the API operation.

id (string) --The ID of the operation.

resourceName (string) --The resource name.

resourceType (string) --The resource type.

createdAt (datetime) --The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --The AWS Region and Availability Zone.

availabilityZone (string) --The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --The AWS Region name.



isTerminal (boolean) --A Boolean value indicating whether the operation is terminal.

operationDetails (string) --Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --The type of operation.

status (string) --The status of the operation.

statusChangedAt (datetime) --The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --The error code.

errorDetails (string) --The error details.










Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
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
    
    Exceptions
    
    :example: response = client.release_static_ip(
        staticIpName='string'
    )
    
    
    :type staticIpName: string
    :param staticIpName: [REQUIRED]\nThe name of the static IP to delete.\n

    :rtype: dict
ReturnsResponse Syntax{
    'operations': [
        {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        },
    ]
}


Response Structure

(dict) --
operations (list) --An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

(dict) --Describes the API operation.

id (string) --The ID of the operation.

resourceName (string) --The resource name.

resourceType (string) --The resource type.

createdAt (datetime) --The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --The AWS Region and Availability Zone.

availabilityZone (string) --The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --The AWS Region name.



isTerminal (boolean) --A Boolean value indicating whether the operation is terminal.

operationDetails (string) --Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --The type of operation.

status (string) --The status of the operation.

statusChangedAt (datetime) --The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --The error code.

errorDetails (string) --The error details.










Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def send_contact_method_verification(protocol=None):
    """
    Sends a verification request to an email contact method to ensure it\'s owned by the requester. SMS contact methods don\'t need to be verified.
    A contact method is used to send you notifications about your Amazon Lightsail resources. You can add one email address and one mobile phone number contact method in each AWS Region. However, SMS text messaging is not supported in some AWS Regions, and SMS text messages cannot be sent to some countries/regions. For more information, see Notifications in Amazon Lightsail .
    A verification request is sent to the contact method when you initially create it. Use this action to send another verification request if a previous verification request was deleted, or has expired.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.send_contact_method_verification(
        protocol='Email'
    )
    
    
    :type protocol: string
    :param protocol: [REQUIRED]\nThe protocol to verify, such as Email or SMS (text messaging).\n

    :rtype: dict
ReturnsResponse Syntax{
    'operations': [
        {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        },
    ]
}


Response Structure

(dict) --
operations (list) --An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

(dict) --Describes the API operation.

id (string) --The ID of the operation.

resourceName (string) --The resource name.

resourceType (string) --The resource type.

createdAt (datetime) --The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --The AWS Region and Availability Zone.

availabilityZone (string) --The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --The AWS Region name.



isTerminal (boolean) --A Boolean value indicating whether the operation is terminal.

operationDetails (string) --Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --The type of operation.

status (string) --The status of the operation.

statusChangedAt (datetime) --The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --The error code.

errorDetails (string) --The error details.










Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.UnauthenticatedException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.NotFoundException


    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
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
    The start instance operation supports tag-based access control via resource tags applied to the resource identified by instance name . For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_instance(
        instanceName='string'
    )
    
    
    :type instanceName: string
    :param instanceName: [REQUIRED]\nThe name of the instance (a virtual private server) to start.\n

    :rtype: dict
ReturnsResponse Syntax{
    'operations': [
        {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        },
    ]
}


Response Structure

(dict) --
operations (list) --An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

(dict) --Describes the API operation.

id (string) --The ID of the operation.

resourceName (string) --The resource name.

resourceType (string) --The resource type.

createdAt (datetime) --The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --The AWS Region and Availability Zone.

availabilityZone (string) --The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --The AWS Region name.



isTerminal (boolean) --A Boolean value indicating whether the operation is terminal.

operationDetails (string) --Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --The type of operation.

status (string) --The status of the operation.

statusChangedAt (datetime) --The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --The error code.

errorDetails (string) --The error details.










Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def start_relational_database(relationalDatabaseName=None):
    """
    Starts a specific database from a stopped state in Amazon Lightsail. To restart a database, use the reboot relational database operation.
    The start relational database operation supports tag-based access control via resource tags applied to the resource identified by relationalDatabaseName. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_relational_database(
        relationalDatabaseName='string'
    )
    
    
    :type relationalDatabaseName: string
    :param relationalDatabaseName: [REQUIRED]\nThe name of your database to start.\n

    :rtype: dict
ReturnsResponse Syntax{
    'operations': [
        {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        },
    ]
}


Response Structure

(dict) --
operations (list) --An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

(dict) --Describes the API operation.

id (string) --The ID of the operation.

resourceName (string) --The resource name.

resourceType (string) --The resource type.

createdAt (datetime) --The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --The AWS Region and Availability Zone.

availabilityZone (string) --The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --The AWS Region name.



isTerminal (boolean) --A Boolean value indicating whether the operation is terminal.

operationDetails (string) --Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --The type of operation.

status (string) --The status of the operation.

statusChangedAt (datetime) --The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --The error code.

errorDetails (string) --The error details.










Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    """
    pass

def stop_instance(instanceName=None, force=None):
    """
    Stops a specific Amazon Lightsail instance that is currently running.
    The stop instance operation supports tag-based access control via resource tags applied to the resource identified by instance name . For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.stop_instance(
        instanceName='string',
        force=True|False
    )
    
    
    :type instanceName: string
    :param instanceName: [REQUIRED]\nThe name of the instance (a virtual private server) to stop.\n

    :type force: boolean
    :param force: When set to True , forces a Lightsail instance that is stuck in a stopping state to stop.\n\nWarning\nOnly use the force parameter if your instance is stuck in the stopping state. In any other state, your instance should stop normally without adding this parameter to your API request.\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'operations': [
        {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        },
    ]
}


Response Structure

(dict) --

operations (list) --
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

(dict) --
Describes the API operation.

id (string) --
The ID of the operation.

resourceName (string) --
The resource name.

resourceType (string) --
The resource type.

createdAt (datetime) --
The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --
The AWS Region and Availability Zone.

availabilityZone (string) --
The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --
The AWS Region name.



isTerminal (boolean) --
A Boolean value indicating whether the operation is terminal.

operationDetails (string) --
Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --
The type of operation.

status (string) --
The status of the operation.

statusChangedAt (datetime) --
The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --
The error code.

errorDetails (string) --
The error details.











Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    :returns: 
    Lightsail.Client.exceptions.ServiceException
    Lightsail.Client.exceptions.InvalidInputException
    Lightsail.Client.exceptions.NotFoundException
    Lightsail.Client.exceptions.OperationFailureException
    Lightsail.Client.exceptions.AccessDeniedException
    Lightsail.Client.exceptions.AccountSetupInProgressException
    Lightsail.Client.exceptions.UnauthenticatedException
    
    """
    pass

def stop_relational_database(relationalDatabaseName=None, relationalDatabaseSnapshotName=None):
    """
    Stops a specific database that is currently running in Amazon Lightsail.
    The stop relational database operation supports tag-based access control via resource tags applied to the resource identified by relationalDatabaseName. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.stop_relational_database(
        relationalDatabaseName='string',
        relationalDatabaseSnapshotName='string'
    )
    
    
    :type relationalDatabaseName: string
    :param relationalDatabaseName: [REQUIRED]\nThe name of your database to stop.\n

    :type relationalDatabaseSnapshotName: string
    :param relationalDatabaseSnapshotName: The name of your new database snapshot to be created before stopping your database.

    :rtype: dict

ReturnsResponse Syntax
{
    'operations': [
        {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        },
    ]
}


Response Structure

(dict) --

operations (list) --
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

(dict) --
Describes the API operation.

id (string) --
The ID of the operation.

resourceName (string) --
The resource name.

resourceType (string) --
The resource type.

createdAt (datetime) --
The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --
The AWS Region and Availability Zone.

availabilityZone (string) --
The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --
The AWS Region name.



isTerminal (boolean) --
A Boolean value indicating whether the operation is terminal.

operationDetails (string) --
Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --
The type of operation.

status (string) --
The status of the operation.

statusChangedAt (datetime) --
The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --
The error code.

errorDetails (string) --
The error details.











Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    :returns: 
    Lightsail.Client.exceptions.ServiceException
    Lightsail.Client.exceptions.InvalidInputException
    Lightsail.Client.exceptions.NotFoundException
    Lightsail.Client.exceptions.OperationFailureException
    Lightsail.Client.exceptions.AccessDeniedException
    Lightsail.Client.exceptions.AccountSetupInProgressException
    Lightsail.Client.exceptions.UnauthenticatedException
    
    """
    pass

def tag_resource(resourceName=None, resourceArn=None, tags=None):
    """
    Adds one or more tags to the specified Amazon Lightsail resource. Each resource can have a maximum of 50 tags. Each tag consists of a key and an optional value. Tag keys must be unique per resource. For more information about tags, see the Lightsail Dev Guide .
    The tag resource operation supports tag-based access control via request tags and resource tags applied to the resource identified by resource name . For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        resourceName='string',
        resourceArn='string',
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type resourceName: string
    :param resourceName: [REQUIRED]\nThe name of the resource to which you are adding tags.\n

    :type resourceArn: string
    :param resourceArn: The Amazon Resource Name (ARN) of the resource to which you want to add a tag.

    :type tags: list
    :param tags: [REQUIRED]\nThe tag key and optional value.\n\n(dict) --Describes a tag key and optional value assigned to an Amazon Lightsail resource.\nFor more information about tags in Lightsail, see the Lightsail Dev Guide .\n\nkey (string) --The key of the tag.\nConstraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @\n\nvalue (string) --The value of the tag.\nConstraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'operations': [
        {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        },
    ]
}


Response Structure

(dict) --

operations (list) --
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

(dict) --
Describes the API operation.

id (string) --
The ID of the operation.

resourceName (string) --
The resource name.

resourceType (string) --
The resource type.

createdAt (datetime) --
The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --
The AWS Region and Availability Zone.

availabilityZone (string) --
The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --
The AWS Region name.



isTerminal (boolean) --
A Boolean value indicating whether the operation is terminal.

operationDetails (string) --
Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --
The type of operation.

status (string) --
The status of the operation.

statusChangedAt (datetime) --
The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --
The error code.

errorDetails (string) --
The error details.











Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    :returns: 
    Lightsail.Client.exceptions.ServiceException
    Lightsail.Client.exceptions.InvalidInputException
    Lightsail.Client.exceptions.NotFoundException
    Lightsail.Client.exceptions.OperationFailureException
    Lightsail.Client.exceptions.AccessDeniedException
    Lightsail.Client.exceptions.AccountSetupInProgressException
    Lightsail.Client.exceptions.UnauthenticatedException
    
    """
    pass

def test_alarm(alarmName=None, state=None):
    """
    Tests an alarm by displaying a banner on the Amazon Lightsail console. If a notification trigger is configured for the specified alarm, the test also sends a notification to the notification protocol (Email and/or SMS ) configured for the alarm.
    An alarm is used to monitor a single metric for one of your resources. When a metric condition is met, the alarm can notify you by email, SMS text message, and a banner displayed on the Amazon Lightsail console. For more information, see Alarms in Amazon Lightsail .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.test_alarm(
        alarmName='string',
        state='OK'|'ALARM'|'INSUFFICIENT_DATA'
    )
    
    
    :type alarmName: string
    :param alarmName: [REQUIRED]\nThe name of the alarm to test.\n

    :type state: string
    :param state: [REQUIRED]\nThe alarm state to test.\nAn alarm has the following possible states that can be tested:\n\nALARM - The metric is outside of the defined threshold.\nINSUFFICIENT_DATA - The alarm has just started, the metric is not available, or not enough data is available for the metric to determine the alarm state.\nOK - The metric is within the defined threshold.\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'operations': [
        {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        },
    ]
}


Response Structure

(dict) --

operations (list) --
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

(dict) --
Describes the API operation.

id (string) --
The ID of the operation.

resourceName (string) --
The resource name.

resourceType (string) --
The resource type.

createdAt (datetime) --
The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --
The AWS Region and Availability Zone.

availabilityZone (string) --
The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --
The AWS Region name.



isTerminal (boolean) --
A Boolean value indicating whether the operation is terminal.

operationDetails (string) --
Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --
The type of operation.

status (string) --
The status of the operation.

statusChangedAt (datetime) --
The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --
The error code.

errorDetails (string) --
The error details.











Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.UnauthenticatedException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.NotFoundException


    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    :returns: 
    Lightsail.Client.exceptions.ServiceException
    Lightsail.Client.exceptions.InvalidInputException
    Lightsail.Client.exceptions.OperationFailureException
    Lightsail.Client.exceptions.UnauthenticatedException
    Lightsail.Client.exceptions.AccessDeniedException
    Lightsail.Client.exceptions.NotFoundException
    
    """
    pass

def unpeer_vpc():
    """
    Attempts to unpeer the Lightsail VPC from the user\'s default VPC.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.unpeer_vpc()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'operation': {
        'id': 'string',
        'resourceName': 'string',
        'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
        'createdAt': datetime(2015, 1, 1),
        'location': {
            'availabilityZone': 'string',
            'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
        },
        'isTerminal': True|False,
        'operationDetails': 'string',
        'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
        'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
        'statusChangedAt': datetime(2015, 1, 1),
        'errorCode': 'string',
        'errorDetails': 'string'
    }
}


Response Structure

(dict) --
operation (dict) --An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

id (string) --The ID of the operation.

resourceName (string) --The resource name.

resourceType (string) --The resource type.

createdAt (datetime) --The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --The AWS Region and Availability Zone.

availabilityZone (string) --The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --The AWS Region name.



isTerminal (boolean) --A Boolean value indicating whether the operation is terminal.

operationDetails (string) --Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --The type of operation.

status (string) --The status of the operation.

statusChangedAt (datetime) --The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --The error code.

errorDetails (string) --The error details.








Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operation': {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        }
    }
    
    
    """
    pass

def untag_resource(resourceName=None, resourceArn=None, tagKeys=None):
    """
    Deletes the specified set of tag keys and their values from the specified Amazon Lightsail resource.
    The untag resource operation supports tag-based access control via request tags and resource tags applied to the resource identified by resource name . For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        resourceName='string',
        resourceArn='string',
        tagKeys=[
            'string',
        ]
    )
    
    
    :type resourceName: string
    :param resourceName: [REQUIRED]\nThe name of the resource from which you are removing a tag.\n

    :type resourceArn: string
    :param resourceArn: The Amazon Resource Name (ARN) of the resource from which you want to remove a tag.

    :type tagKeys: list
    :param tagKeys: [REQUIRED]\nThe tag keys to delete from the specified resource.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'operations': [
        {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        },
    ]
}


Response Structure

(dict) --

operations (list) --
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

(dict) --
Describes the API operation.

id (string) --
The ID of the operation.

resourceName (string) --
The resource name.

resourceType (string) --
The resource type.

createdAt (datetime) --
The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --
The AWS Region and Availability Zone.

availabilityZone (string) --
The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --
The AWS Region name.



isTerminal (boolean) --
A Boolean value indicating whether the operation is terminal.

operationDetails (string) --
Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --
The type of operation.

status (string) --
The status of the operation.

statusChangedAt (datetime) --
The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --
The error code.

errorDetails (string) --
The error details.











Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    :returns: 
    Lightsail.Client.exceptions.ServiceException
    Lightsail.Client.exceptions.InvalidInputException
    Lightsail.Client.exceptions.NotFoundException
    Lightsail.Client.exceptions.OperationFailureException
    Lightsail.Client.exceptions.AccessDeniedException
    Lightsail.Client.exceptions.AccountSetupInProgressException
    Lightsail.Client.exceptions.UnauthenticatedException
    
    """
    pass

def update_domain_entry(domainName=None, domainEntry=None):
    """
    Updates a domain recordset after it is created.
    The update domain entry operation supports tag-based access control via resource tags applied to the resource identified by domain name . For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_domain_entry(
        domainName='string',
        domainEntry={
            'id': 'string',
            'name': 'string',
            'target': 'string',
            'isAlias': True|False,
            'type': 'string',
            'options': {
                'string': 'string'
            }
        }
    )
    
    
    :type domainName: string
    :param domainName: [REQUIRED]\nThe name of the domain recordset to update.\n

    :type domainEntry: dict
    :param domainEntry: [REQUIRED]\nAn array of key-value pairs containing information about the domain entry.\n\nid (string) --The ID of the domain recordset entry.\n\nname (string) --The name of the domain.\n\ntarget (string) --The target AWS name server (e.g., ns-111.awsdns-22.com. ).\nFor Lightsail load balancers, the value looks like ab1234c56789c6b86aba6fb203d443bc-123456789.us-east-2.elb.amazonaws.com . Be sure to also set isAlias to true when setting up an A record for a load balancer.\n\nisAlias (boolean) --When true , specifies whether the domain entry is an alias used by the Lightsail load balancer. You can include an alias (A type) record in your request, which points to a load balancer DNS name and routes traffic to your load balancer\n\ntype (string) --The type of domain entry, such as address (A), canonical name (CNAME), mail exchanger (MX), name server (NS), start of authority (SOA), service locator (SRV), or text (TXT).\nThe following domain entry types can be used:\n\nA\nCNAME\nMX\nNS\nSOA\nSRV\nTXT\n\n\noptions (dict) --(Deprecated) The options for the domain entry.\n\nNote\nIn releases prior to November 29, 2017, this parameter was not included in the API response. It is now deprecated.\n\n\n(string) --\n(string) --\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'operations': [
        {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        },
    ]
}


Response Structure

(dict) --

operations (list) --
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

(dict) --
Describes the API operation.

id (string) --
The ID of the operation.

resourceName (string) --
The resource name.

resourceType (string) --
The resource type.

createdAt (datetime) --
The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --
The AWS Region and Availability Zone.

availabilityZone (string) --
The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --
The AWS Region name.



isTerminal (boolean) --
A Boolean value indicating whether the operation is terminal.

operationDetails (string) --
Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --
The type of operation.

status (string) --
The status of the operation.

statusChangedAt (datetime) --
The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --
The error code.

errorDetails (string) --
The error details.











Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    :returns: 
    Lightsail.Client.exceptions.ServiceException
    Lightsail.Client.exceptions.InvalidInputException
    Lightsail.Client.exceptions.NotFoundException
    Lightsail.Client.exceptions.OperationFailureException
    Lightsail.Client.exceptions.AccessDeniedException
    Lightsail.Client.exceptions.AccountSetupInProgressException
    Lightsail.Client.exceptions.UnauthenticatedException
    
    """
    pass

def update_load_balancer_attribute(loadBalancerName=None, attributeName=None, attributeValue=None):
    """
    Updates the specified attribute for a load balancer. You can only update one attribute at a time.
    The update load balancer attribute operation supports tag-based access control via resource tags applied to the resource identified by load balancer name . For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_load_balancer_attribute(
        loadBalancerName='string',
        attributeName='HealthCheckPath'|'SessionStickinessEnabled'|'SessionStickiness_LB_CookieDurationSeconds',
        attributeValue='string'
    )
    
    
    :type loadBalancerName: string
    :param loadBalancerName: [REQUIRED]\nThe name of the load balancer that you want to modify (e.g., my-load-balancer .\n

    :type attributeName: string
    :param attributeName: [REQUIRED]\nThe name of the attribute you want to update. Valid values are below.\n

    :type attributeValue: string
    :param attributeValue: [REQUIRED]\nThe value that you want to specify for the attribute name.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'operations': [
        {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        },
    ]
}


Response Structure

(dict) --

operations (list) --
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

(dict) --
Describes the API operation.

id (string) --
The ID of the operation.

resourceName (string) --
The resource name.

resourceType (string) --
The resource type.

createdAt (datetime) --
The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --
The AWS Region and Availability Zone.

availabilityZone (string) --
The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --
The AWS Region name.



isTerminal (boolean) --
A Boolean value indicating whether the operation is terminal.

operationDetails (string) --
Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --
The type of operation.

status (string) --
The status of the operation.

statusChangedAt (datetime) --
The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --
The error code.

errorDetails (string) --
The error details.











Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    :returns: 
    Lightsail.Client.exceptions.ServiceException
    Lightsail.Client.exceptions.InvalidInputException
    Lightsail.Client.exceptions.NotFoundException
    Lightsail.Client.exceptions.OperationFailureException
    Lightsail.Client.exceptions.AccessDeniedException
    Lightsail.Client.exceptions.AccountSetupInProgressException
    Lightsail.Client.exceptions.UnauthenticatedException
    
    """
    pass

def update_relational_database(relationalDatabaseName=None, masterUserPassword=None, rotateMasterUserPassword=None, preferredBackupWindow=None, preferredMaintenanceWindow=None, enableBackupRetention=None, disableBackupRetention=None, publiclyAccessible=None, applyImmediately=None, caCertificateIdentifier=None):
    """
    Allows the update of one or more attributes of a database in Amazon Lightsail.
    Updates are applied immediately, or in cases where the updates could result in an outage, are applied during the database\'s predefined maintenance window.
    The update relational database operation supports tag-based access control via resource tags applied to the resource identified by relationalDatabaseName. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_relational_database(
        relationalDatabaseName='string',
        masterUserPassword='string',
        rotateMasterUserPassword=True|False,
        preferredBackupWindow='string',
        preferredMaintenanceWindow='string',
        enableBackupRetention=True|False,
        disableBackupRetention=True|False,
        publiclyAccessible=True|False,
        applyImmediately=True|False,
        caCertificateIdentifier='string'
    )
    
    
    :type relationalDatabaseName: string
    :param relationalDatabaseName: [REQUIRED]\nThe name of your database to update.\n

    :type masterUserPassword: string
    :param masterUserPassword: The password for the master user of your database. The password can include any printable ASCII character except '/', ''', or '@'.\nConstraints: Must contain 8 to 41 characters.\n

    :type rotateMasterUserPassword: boolean
    :param rotateMasterUserPassword: When true , the master user password is changed to a new strong password generated by Lightsail.\nUse the get relational database master user password operation to get the new password.\n

    :type preferredBackupWindow: string
    :param preferredBackupWindow: The daily time range during which automated backups are created for your database if automated backups are enabled.\nConstraints:\n\nMust be in the hh24:mi-hh24:mi format. Example: 16:00-16:30\nSpecified in Coordinated Universal Time (UTC).\nMust not conflict with the preferred maintenance window.\nMust be at least 30 minutes.\n\n

    :type preferredMaintenanceWindow: string
    :param preferredMaintenanceWindow: The weekly time range during which system maintenance can occur on your database.\nThe default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week.\nConstraints:\n\nMust be in the ddd:hh24:mi-ddd:hh24:mi format.\nValid days: Mon, Tue, Wed, Thu, Fri, Sat, Sun.\nMust be at least 30 minutes.\nSpecified in Coordinated Universal Time (UTC).\nExample: Tue:17:00-Tue:17:30\n\n

    :type enableBackupRetention: boolean
    :param enableBackupRetention: When true , enables automated backup retention for your database.\nUpdates are applied during the next maintenance window because this can result in an outage.\n

    :type disableBackupRetention: boolean
    :param disableBackupRetention: When true , disables automated backup retention for your database.\nDisabling backup retention deletes all automated database backups. Before disabling this, you may want to create a snapshot of your database using the create relational database snapshot operation.\nUpdates are applied during the next maintenance window because this can result in an outage.\n

    :type publiclyAccessible: boolean
    :param publiclyAccessible: Specifies the accessibility options for your database. A value of true specifies a database that is available to resources outside of your Lightsail account. A value of false specifies a database that is available only to your Lightsail resources in the same region as your database.

    :type applyImmediately: boolean
    :param applyImmediately: When true , applies changes immediately. When false , applies changes during the preferred maintenance window. Some changes may cause an outage.\nDefault: false\n

    :type caCertificateIdentifier: string
    :param caCertificateIdentifier: Indicates the certificate that needs to be associated with the database.

    :rtype: dict

ReturnsResponse Syntax
{
    'operations': [
        {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        },
    ]
}


Response Structure

(dict) --

operations (list) --
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

(dict) --
Describes the API operation.

id (string) --
The ID of the operation.

resourceName (string) --
The resource name.

resourceType (string) --
The resource type.

createdAt (datetime) --
The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --
The AWS Region and Availability Zone.

availabilityZone (string) --
The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --
The AWS Region name.



isTerminal (boolean) --
A Boolean value indicating whether the operation is terminal.

operationDetails (string) --
Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --
The type of operation.

status (string) --
The status of the operation.

statusChangedAt (datetime) --
The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --
The error code.

errorDetails (string) --
The error details.











Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    :returns: 
    Lightsail.Client.exceptions.ServiceException
    Lightsail.Client.exceptions.InvalidInputException
    Lightsail.Client.exceptions.NotFoundException
    Lightsail.Client.exceptions.OperationFailureException
    Lightsail.Client.exceptions.AccessDeniedException
    Lightsail.Client.exceptions.AccountSetupInProgressException
    Lightsail.Client.exceptions.UnauthenticatedException
    
    """
    pass

def update_relational_database_parameters(relationalDatabaseName=None, parameters=None):
    """
    Allows the update of one or more parameters of a database in Amazon Lightsail.
    Parameter updates don\'t cause outages; therefore, their application is not subject to the preferred maintenance window. However, there are two ways in which parameter updates are applied: dynamic or pending-reboot . Parameters marked with a dynamic apply type are applied immediately. Parameters marked with a pending-reboot apply type are applied only after the database is rebooted using the reboot relational database operation.
    The update relational database parameters operation supports tag-based access control via resource tags applied to the resource identified by relationalDatabaseName. For more information, see the Lightsail Dev Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_relational_database_parameters(
        relationalDatabaseName='string',
        parameters=[
            {
                'allowedValues': 'string',
                'applyMethod': 'string',
                'applyType': 'string',
                'dataType': 'string',
                'description': 'string',
                'isModifiable': True|False,
                'parameterName': 'string',
                'parameterValue': 'string'
            },
        ]
    )
    
    
    :type relationalDatabaseName: string
    :param relationalDatabaseName: [REQUIRED]\nThe name of your database for which to update parameters.\n

    :type parameters: list
    :param parameters: [REQUIRED]\nThe database parameters to update.\n\n(dict) --Describes the parameters of a database.\n\nallowedValues (string) --Specifies the valid range of values for the parameter.\n\napplyMethod (string) --Indicates when parameter updates are applied.\nCan be immediate or pending-reboot .\n\napplyType (string) --Specifies the engine-specific parameter type.\n\ndataType (string) --Specifies the valid data type for the parameter.\n\ndescription (string) --Provides a description of the parameter.\n\nisModifiable (boolean) --A Boolean value indicating whether the parameter can be modified.\n\nparameterName (string) --Specifies the name of the parameter.\n\nparameterValue (string) --Specifies the value of the parameter.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'operations': [
        {
            'id': 'string',
            'resourceName': 'string',
            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
            'createdAt': datetime(2015, 1, 1),
            'location': {
                'availabilityZone': 'string',
                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
            },
            'isTerminal': True|False,
            'operationDetails': 'string',
            'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
            'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
            'statusChangedAt': datetime(2015, 1, 1),
            'errorCode': 'string',
            'errorDetails': 'string'
        },
    ]
}


Response Structure

(dict) --

operations (list) --
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

(dict) --
Describes the API operation.

id (string) --
The ID of the operation.

resourceName (string) --
The resource name.

resourceType (string) --
The resource type.

createdAt (datetime) --
The timestamp when the operation was initialized (e.g., 1479816991.349 ).

location (dict) --
The AWS Region and Availability Zone.

availabilityZone (string) --
The Availability Zone. Follows the format us-east-2a (case-sensitive).

regionName (string) --
The AWS Region name.



isTerminal (boolean) --
A Boolean value indicating whether the operation is terminal.

operationDetails (string) --
Details about the operation (e.g., Debian-1GB-Ohio-1 ).

operationType (string) --
The type of operation.

status (string) --
The status of the operation.

statusChangedAt (datetime) --
The timestamp when the status was changed (e.g., 1479816991.349 ).

errorCode (string) --
The error code.

errorDetails (string) --
The error details.











Exceptions

Lightsail.Client.exceptions.ServiceException
Lightsail.Client.exceptions.InvalidInputException
Lightsail.Client.exceptions.NotFoundException
Lightsail.Client.exceptions.OperationFailureException
Lightsail.Client.exceptions.AccessDeniedException
Lightsail.Client.exceptions.AccountSetupInProgressException
Lightsail.Client.exceptions.UnauthenticatedException


    :return: {
        'operations': [
            {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot'|'RelationalDatabase'|'RelationalDatabaseSnapshot'|'ExportSnapshotRecord'|'CloudFormationStackRecord'|'Alarm'|'ContactMethod',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'eu-central-1'|'ca-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteKnownHostKeys'|'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot'|'CreateRelationalDatabase'|'UpdateRelationalDatabase'|'DeleteRelationalDatabase'|'CreateRelationalDatabaseFromSnapshot'|'CreateRelationalDatabaseSnapshot'|'DeleteRelationalDatabaseSnapshot'|'UpdateRelationalDatabaseParameters'|'StartRelationalDatabase'|'RebootRelationalDatabase'|'StopRelationalDatabase'|'EnableAddOn'|'DisableAddOn'|'PutAlarm'|'GetAlarms'|'DeleteAlarm'|'TestAlarm'|'CreateContactMethod'|'GetContactMethods'|'SendContactMethodVerification'|'DeleteContactMethod',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed'|'Succeeded',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            },
        ]
    }
    
    
    :returns: 
    Lightsail.Client.exceptions.ServiceException
    Lightsail.Client.exceptions.InvalidInputException
    Lightsail.Client.exceptions.NotFoundException
    Lightsail.Client.exceptions.OperationFailureException
    Lightsail.Client.exceptions.AccessDeniedException
    Lightsail.Client.exceptions.AccountSetupInProgressException
    Lightsail.Client.exceptions.UnauthenticatedException
    
    """
    pass

