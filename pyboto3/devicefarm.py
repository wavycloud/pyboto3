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

def create_device_pool(projectArn=None, name=None, description=None, rules=None, maxDevices=None):
    """
    Creates a device pool.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example creates a new device pool named MyDevicePool inside an existing project.
    Expected Output:
    
    :example: response = client.create_device_pool(
        projectArn='string',
        name='string',
        description='string',
        rules=[
            {
                'attribute': 'ARN'|'PLATFORM'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'APPIUM_VERSION'|'INSTANCE_ARN'|'INSTANCE_LABELS'|'FLEET_TYPE'|'OS_VERSION'|'MODEL'|'AVAILABILITY',
                'operator': 'EQUALS'|'LESS_THAN'|'LESS_THAN_OR_EQUALS'|'GREATER_THAN'|'GREATER_THAN_OR_EQUALS'|'IN'|'NOT_IN'|'CONTAINS',
                'value': 'string'
            },
        ],
        maxDevices=123
    )
    
    
    :type projectArn: string
    :param projectArn: [REQUIRED]\nThe ARN of the project for the device pool.\n

    :type name: string
    :param name: [REQUIRED]\nThe device pool\'s name.\n

    :type description: string
    :param description: The device pool\'s description.

    :type rules: list
    :param rules: [REQUIRED]\nThe device pool\'s rules.\n\n(dict) --Represents a condition for a device pool.\n\nattribute (string) --The rule\'s stringified attribute. For example, specify the value as '\\'abc\\'' .\nThe supported operators for each attribute are provided in the following list.\n\nAPPIUM_VERSION\nThe Appium version for the test.\nSupported operators: CONTAINS\n\nARN\nThe Amazon Resource Name (ARN) of the device (for example, arn:aws:devicefarm:us-west-2::device:12345Example .\nSupported operators: EQUALS , IN , NOT_IN\n\nAVAILABILITY\nThe current availability of the device. Valid values are AVAILABLE, HIGHLY_AVAILABLE, BUSY, or TEMPORARY_NOT_AVAILABLE.\nSupported operators: EQUALS\n\nFLEET_TYPE\nThe fleet type. Valid values are PUBLIC or PRIVATE.\nSupported operators: EQUALS\n\nFORM_FACTOR\nThe device form factor. Valid values are PHONE or TABLET.\nSupported operators: EQUALS , IN , NOT_IN\n\nINSTANCE_ARN\nThe Amazon Resource Name (ARN) of the device instance.\nSupported operators: IN , NOT_IN\n\nINSTANCE_LABELS\nThe label of the device instance.\nSupported operators: CONTAINS\n\nMANUFACTURER\nThe device manufacturer (for example, Apple).\nSupported operators: EQUALS , IN , NOT_IN\n\nMODEL\nThe device model, such as Apple iPad Air 2 or Google Pixel.\nSupported operators: CONTAINS , EQUALS , IN , NOT_IN\n\nOS_VERSION\nThe operating system version (for example, 10.3.2).\nSupported operators: EQUALS , GREATER_THAN , GREATER_THAN_OR_EQUALS , IN , LESS_THAN , LESS_THAN_OR_EQUALS , NOT_IN\n\nPLATFORM\nThe device platform. Valid values are ANDROID or IOS.\nSupported operators: EQUALS , IN , NOT_IN\n\nREMOTE_ACCESS_ENABLED\nWhether the device is enabled for remote access. Valid values are TRUE or FALSE.\nSupported operators: EQUALS\n\nREMOTE_DEBUG_ENABLED\nWhether the device is enabled for remote debugging. Valid values are TRUE or FALSE.\nSupported operators: EQUALS\nBecause remote debugging is no longer supported , this filter is ignored.\n\noperator (string) --Specifies how Device Farm compares the rule\'s attribute to the value. For the operators that are supported by each attribute, see the attribute descriptions.\n\nvalue (string) --The rule\'s value.\n\n\n\n\n

    :type maxDevices: integer
    :param maxDevices: The number of devices that Device Farm can add to your device pool. Device Farm adds devices that are available and meet the criteria that you assign for the rules parameter. Depending on how many devices meet these constraints, your device pool might contain fewer devices than the value for this parameter.\nBy specifying the maximum number of devices, you can control the costs that you incur by running tests.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'devicePool': {
        'arn': 'string',
        'name': 'string',
        'description': 'string',
        'type': 'CURATED'|'PRIVATE',
        'rules': [
            {
                'attribute': 'ARN'|'PLATFORM'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'APPIUM_VERSION'|'INSTANCE_ARN'|'INSTANCE_LABELS'|'FLEET_TYPE'|'OS_VERSION'|'MODEL'|'AVAILABILITY',
                'operator': 'EQUALS'|'LESS_THAN'|'LESS_THAN_OR_EQUALS'|'GREATER_THAN'|'GREATER_THAN_OR_EQUALS'|'IN'|'NOT_IN'|'CONTAINS',
                'value': 'string'
            },
        ],
        'maxDevices': 123
    }
}


Response Structure

(dict) --
Represents the result of a create device pool request.

devicePool (dict) --
The newly created device pool.

arn (string) --
The device pool\'s ARN.

name (string) --
The device pool\'s name.

description (string) --
The device pool\'s description.

type (string) --
The device pool\'s type.
Allowed values include:

CURATED: A device pool that is created and managed by AWS Device Farm.
PRIVATE: A device pool that is created and managed by the device pool developer.


rules (list) --
Information about the device pool\'s rules.

(dict) --
Represents a condition for a device pool.

attribute (string) --
The rule\'s stringified attribute. For example, specify the value as "\\"abc\\"" .
The supported operators for each attribute are provided in the following list.

APPIUM_VERSION

The Appium version for the test.
Supported operators: CONTAINS

ARN

The Amazon Resource Name (ARN) of the device (for example, arn:aws:devicefarm:us-west-2::device:12345Example .
Supported operators: EQUALS , IN , NOT_IN

AVAILABILITY

The current availability of the device. Valid values are AVAILABLE, HIGHLY_AVAILABLE, BUSY, or TEMPORARY_NOT_AVAILABLE.
Supported operators: EQUALS

FLEET_TYPE

The fleet type. Valid values are PUBLIC or PRIVATE.
Supported operators: EQUALS

FORM_FACTOR

The device form factor. Valid values are PHONE or TABLET.
Supported operators: EQUALS , IN , NOT_IN

INSTANCE_ARN

The Amazon Resource Name (ARN) of the device instance.
Supported operators: IN , NOT_IN

INSTANCE_LABELS

The label of the device instance.
Supported operators: CONTAINS

MANUFACTURER

The device manufacturer (for example, Apple).
Supported operators: EQUALS , IN , NOT_IN

MODEL

The device model, such as Apple iPad Air 2 or Google Pixel.
Supported operators: CONTAINS , EQUALS , IN , NOT_IN

OS_VERSION

The operating system version (for example, 10.3.2).
Supported operators: EQUALS , GREATER_THAN , GREATER_THAN_OR_EQUALS , IN , LESS_THAN , LESS_THAN_OR_EQUALS , NOT_IN

PLATFORM

The device platform. Valid values are ANDROID or IOS.
Supported operators: EQUALS , IN , NOT_IN

REMOTE_ACCESS_ENABLED

Whether the device is enabled for remote access. Valid values are TRUE or FALSE.
Supported operators: EQUALS

REMOTE_DEBUG_ENABLED

Whether the device is enabled for remote debugging. Valid values are TRUE or FALSE.
Supported operators: EQUALS
Because remote debugging is no longer supported , this filter is ignored.

operator (string) --
Specifies how Device Farm compares the rule\'s attribute to the value. For the operators that are supported by each attribute, see the attribute descriptions.

value (string) --
The rule\'s value.





maxDevices (integer) --
The number of devices that Device Farm can add to your device pool. Device Farm adds devices that are available and meet the criteria that you assign for the rules parameter. Depending on how many devices meet these constraints, your device pool might contain fewer devices than the value for this parameter.
By specifying the maximum number of devices, you can control the costs that you incur by running tests.









Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.LimitExceededException
DeviceFarm.Client.exceptions.ServiceAccountException

Examples
The following example creates a new device pool named MyDevicePool inside an existing project.
response = client.create_device_pool(
    # A device pool contains related devices, such as devices that run only on Android or that run only on iOS.
    name='MyDevicePool',
    description='My Android devices',
    # You can get the project ARN by using the list-projects CLI command.
    projectArn='arn:aws:devicefarm:us-west-2:123456789101:project:EXAMPLE-GUID-123-456',
    rules=[
    ],
)

print(response)


Expected Output:
{
    'devicePool': {
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'devicePool': {
            'arn': 'string',
            'name': 'string',
            'description': 'string',
            'type': 'CURATED'|'PRIVATE',
            'rules': [
                {
                    'attribute': 'ARN'|'PLATFORM'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'APPIUM_VERSION'|'INSTANCE_ARN'|'INSTANCE_LABELS'|'FLEET_TYPE'|'OS_VERSION'|'MODEL'|'AVAILABILITY',
                    'operator': 'EQUALS'|'LESS_THAN'|'LESS_THAN_OR_EQUALS'|'GREATER_THAN'|'GREATER_THAN_OR_EQUALS'|'IN'|'NOT_IN'|'CONTAINS',
                    'value': 'string'
                },
            ],
            'maxDevices': 123
        }
    }
    
    
    :returns: 
    CURATED: A device pool that is created and managed by AWS Device Farm.
    PRIVATE: A device pool that is created and managed by the device pool developer.
    
    """
    pass

def create_instance_profile(name=None, description=None, packageCleanup=None, excludeAppPackagesFromCleanup=None, rebootAfterUse=None):
    """
    Creates a profile that can be applied to one or more private fleet device instances.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_instance_profile(
        name='string',
        description='string',
        packageCleanup=True|False,
        excludeAppPackagesFromCleanup=[
            'string',
        ],
        rebootAfterUse=True|False
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name of your instance profile.\n

    :type description: string
    :param description: The description of your instance profile.

    :type packageCleanup: boolean
    :param packageCleanup: When set to true , Device Farm removes app packages after a test run. The default value is false for private devices.

    :type excludeAppPackagesFromCleanup: list
    :param excludeAppPackagesFromCleanup: An array of strings that specifies the list of app packages that should not be cleaned up from the device after a test run.\nThe list of packages is considered only if you set packageCleanup to true .\n\n(string) --\n\n

    :type rebootAfterUse: boolean
    :param rebootAfterUse: When set to true , Device Farm reboots the instance after a test run. The default value is true .

    :rtype: dict

ReturnsResponse Syntax
{
    'instanceProfile': {
        'arn': 'string',
        'packageCleanup': True|False,
        'excludeAppPackagesFromCleanup': [
            'string',
        ],
        'rebootAfterUse': True|False,
        'name': 'string',
        'description': 'string'
    }
}


Response Structure

(dict) --

instanceProfile (dict) --
An object that contains information about your instance profile.

arn (string) --
The Amazon Resource Name (ARN) of the instance profile.

packageCleanup (boolean) --
When set to true , Device Farm removes app packages after a test run. The default value is false for private devices.

excludeAppPackagesFromCleanup (list) --
An array of strings containing the list of app packages that should not be cleaned up from the device after a test run completes.
The list of packages is considered only if you set packageCleanup to true .

(string) --


rebootAfterUse (boolean) --
When set to true , Device Farm reboots the instance after a test run. The default value is true .

name (string) --
The name of the instance profile.

description (string) --
The description of the instance profile.









Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.LimitExceededException
DeviceFarm.Client.exceptions.ServiceAccountException


    :return: {
        'instanceProfile': {
            'arn': 'string',
            'packageCleanup': True|False,
            'excludeAppPackagesFromCleanup': [
                'string',
            ],
            'rebootAfterUse': True|False,
            'name': 'string',
            'description': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_network_profile(projectArn=None, name=None, description=None, type=None, uplinkBandwidthBits=None, downlinkBandwidthBits=None, uplinkDelayMs=None, downlinkDelayMs=None, uplinkJitterMs=None, downlinkJitterMs=None, uplinkLossPercent=None, downlinkLossPercent=None):
    """
    Creates a network profile.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_network_profile(
        projectArn='string',
        name='string',
        description='string',
        type='CURATED'|'PRIVATE',
        uplinkBandwidthBits=123,
        downlinkBandwidthBits=123,
        uplinkDelayMs=123,
        downlinkDelayMs=123,
        uplinkJitterMs=123,
        downlinkJitterMs=123,
        uplinkLossPercent=123,
        downlinkLossPercent=123
    )
    
    
    :type projectArn: string
    :param projectArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the project for which you want to create a network profile.\n

    :type name: string
    :param name: [REQUIRED]\nThe name for the new network profile.\n

    :type description: string
    :param description: The description of the network profile.

    :type type: string
    :param type: The type of network profile to create. Valid values are listed here.

    :type uplinkBandwidthBits: integer
    :param uplinkBandwidthBits: The data throughput rate in bits per second, as an integer from 0 to 104857600.

    :type downlinkBandwidthBits: integer
    :param downlinkBandwidthBits: The data throughput rate in bits per second, as an integer from 0 to 104857600.

    :type uplinkDelayMs: integer
    :param uplinkDelayMs: Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.

    :type downlinkDelayMs: integer
    :param downlinkDelayMs: Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.

    :type uplinkJitterMs: integer
    :param uplinkJitterMs: Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.

    :type downlinkJitterMs: integer
    :param downlinkJitterMs: Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.

    :type uplinkLossPercent: integer
    :param uplinkLossPercent: Proportion of transmitted packets that fail to arrive from 0 to 100 percent.

    :type downlinkLossPercent: integer
    :param downlinkLossPercent: Proportion of received packets that fail to arrive from 0 to 100 percent.

    :rtype: dict

ReturnsResponse Syntax
{
    'networkProfile': {
        'arn': 'string',
        'name': 'string',
        'description': 'string',
        'type': 'CURATED'|'PRIVATE',
        'uplinkBandwidthBits': 123,
        'downlinkBandwidthBits': 123,
        'uplinkDelayMs': 123,
        'downlinkDelayMs': 123,
        'uplinkJitterMs': 123,
        'downlinkJitterMs': 123,
        'uplinkLossPercent': 123,
        'downlinkLossPercent': 123
    }
}


Response Structure

(dict) --

networkProfile (dict) --
The network profile that is returned by the create network profile request.

arn (string) --
The Amazon Resource Name (ARN) of the network profile.

name (string) --
The name of the network profile.

description (string) --
The description of the network profile.

type (string) --
The type of network profile. Valid values are listed here.

uplinkBandwidthBits (integer) --
The data throughput rate in bits per second, as an integer from 0 to 104857600.

downlinkBandwidthBits (integer) --
The data throughput rate in bits per second, as an integer from 0 to 104857600.

uplinkDelayMs (integer) --
Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.

downlinkDelayMs (integer) --
Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.

uplinkJitterMs (integer) --
Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.

downlinkJitterMs (integer) --
Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.

uplinkLossPercent (integer) --
Proportion of transmitted packets that fail to arrive from 0 to 100 percent.

downlinkLossPercent (integer) --
Proportion of received packets that fail to arrive from 0 to 100 percent.









Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.LimitExceededException
DeviceFarm.Client.exceptions.ServiceAccountException


    :return: {
        'networkProfile': {
            'arn': 'string',
            'name': 'string',
            'description': 'string',
            'type': 'CURATED'|'PRIVATE',
            'uplinkBandwidthBits': 123,
            'downlinkBandwidthBits': 123,
            'uplinkDelayMs': 123,
            'downlinkDelayMs': 123,
            'uplinkJitterMs': 123,
            'downlinkJitterMs': 123,
            'uplinkLossPercent': 123,
            'downlinkLossPercent': 123
        }
    }
    
    
    :returns: 
    DeviceFarm.Client.exceptions.ArgumentException
    DeviceFarm.Client.exceptions.NotFoundException
    DeviceFarm.Client.exceptions.LimitExceededException
    DeviceFarm.Client.exceptions.ServiceAccountException
    
    """
    pass

def create_project(name=None, defaultJobTimeoutMinutes=None):
    """
    Creates a project.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example creates a new project named MyProject.
    Expected Output:
    
    :example: response = client.create_project(
        name='string',
        defaultJobTimeoutMinutes=123
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe project\'s name.\n

    :type defaultJobTimeoutMinutes: integer
    :param defaultJobTimeoutMinutes: Sets the execution timeout value (in minutes) for a project. All test runs in this project use the specified execution timeout value unless overridden when scheduling a run.

    :rtype: dict

ReturnsResponse Syntax
{
    'project': {
        'arn': 'string',
        'name': 'string',
        'defaultJobTimeoutMinutes': 123,
        'created': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --
Represents the result of a create project request.

project (dict) --
The newly created project.

arn (string) --
The project\'s ARN.

name (string) --
The project\'s name.

defaultJobTimeoutMinutes (integer) --
The default number of minutes (at the project level) a test run executes before it times out. The default value is 150 minutes.

created (datetime) --
When the project was created.









Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.LimitExceededException
DeviceFarm.Client.exceptions.ServiceAccountException
DeviceFarm.Client.exceptions.TagOperationException

Examples
The following example creates a new project named MyProject.
response = client.create_project(
    # A project in Device Farm is a workspace that contains test runs. A run is a test of a single app against one or more devices.
    name='MyProject',
)

print(response)


Expected Output:
{
    'project': {
        'name': 'MyProject',
        'arn': 'arn:aws:devicefarm:us-west-2:123456789101:project:5e01a8c7-c861-4c0a-b1d5-12345EXAMPLE',
        'created': datetime(2016, 8, 31, 16, 28, 59, 2, 244, 0),
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'project': {
            'arn': 'string',
            'name': 'string',
            'defaultJobTimeoutMinutes': 123,
            'created': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    DeviceFarm.Client.exceptions.ArgumentException
    DeviceFarm.Client.exceptions.NotFoundException
    DeviceFarm.Client.exceptions.LimitExceededException
    DeviceFarm.Client.exceptions.ServiceAccountException
    DeviceFarm.Client.exceptions.TagOperationException
    
    """
    pass

def create_remote_access_session(projectArn=None, deviceArn=None, instanceArn=None, sshPublicKey=None, remoteDebugEnabled=None, remoteRecordEnabled=None, remoteRecordAppArn=None, name=None, clientId=None, configuration=None, interactionMode=None, skipAppResign=None):
    """
    Specifies and starts a remote access session.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example creates a remote access session named MySession.
    Expected Output:
    
    :example: response = client.create_remote_access_session(
        projectArn='string',
        deviceArn='string',
        instanceArn='string',
        sshPublicKey='string',
        remoteDebugEnabled=True|False,
        remoteRecordEnabled=True|False,
        remoteRecordAppArn='string',
        name='string',
        clientId='string',
        configuration={
            'billingMethod': 'METERED'|'UNMETERED',
            'vpceConfigurationArns': [
                'string',
            ]
        },
        interactionMode='INTERACTIVE'|'NO_VIDEO'|'VIDEO_ONLY',
        skipAppResign=True|False
    )
    
    
    :type projectArn: string
    :param projectArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the project for which you want to create a remote access session.\n

    :type deviceArn: string
    :param deviceArn: [REQUIRED]\nThe ARN of the device for which you want to create a remote access session.\n

    :type instanceArn: string
    :param instanceArn: The Amazon Resource Name (ARN) of the device instance for which you want to create a remote access session.

    :type sshPublicKey: string
    :param sshPublicKey: Ignored. The public key of the ssh key pair you want to use for connecting to remote devices in your remote debugging session. This key is required only if remoteDebugEnabled is set to true .\nRemote debugging is no longer supported .\n

    :type remoteDebugEnabled: boolean
    :param remoteDebugEnabled: Set to true if you want to access devices remotely for debugging in your remote access session.\nRemote debugging is no longer supported .\n

    :type remoteRecordEnabled: boolean
    :param remoteRecordEnabled: Set to true to enable remote recording for the remote access session.

    :type remoteRecordAppArn: string
    :param remoteRecordAppArn: The Amazon Resource Name (ARN) for the app to be recorded in the remote access session.

    :type name: string
    :param name: The name of the remote access session to create.

    :type clientId: string
    :param clientId: Unique identifier for the client. If you want access to multiple devices on the same client, you should pass the same clientId value in each call to CreateRemoteAccessSession . This identifier is required only if remoteDebugEnabled is set to true .\nRemote debugging is no longer supported .\n

    :type configuration: dict
    :param configuration: The configuration information for the remote access session request.\n\nbillingMethod (string) --The billing method for the remote access session.\n\nvpceConfigurationArns (list) --An array of ARNs included in the VPC endpoint configuration.\n\n(string) --\n\n\n\n

    :type interactionMode: string
    :param interactionMode: The interaction mode of the remote access session. Valid values are:\n\nINTERACTIVE: You can interact with the iOS device by viewing, touching, and rotating the screen. You cannot run XCUITest framework-based tests in this mode.\nNO_VIDEO: You are connected to the device, but cannot interact with it or view the screen. This mode has the fastest test execution speed. You can run XCUITest framework-based tests in this mode.\nVIDEO_ONLY: You can view the screen, but cannot touch or rotate it. You can run XCUITest framework-based tests and watch the screen in this mode.\n\n

    :type skipAppResign: boolean
    :param skipAppResign: When set to true , for private devices, Device Farm does not sign your app again. For public devices, Device Farm always signs your apps again.\nFor more information on how Device Farm modifies your uploads during tests, see Do you modify my app?\n

    :rtype: dict

ReturnsResponse Syntax
{
    'remoteAccessSession': {
        'arn': 'string',
        'name': 'string',
        'created': datetime(2015, 1, 1),
        'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
        'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
        'message': 'string',
        'started': datetime(2015, 1, 1),
        'stopped': datetime(2015, 1, 1),
        'device': {
            'arn': 'string',
            'name': 'string',
            'manufacturer': 'string',
            'model': 'string',
            'modelId': 'string',
            'formFactor': 'PHONE'|'TABLET',
            'platform': 'ANDROID'|'IOS',
            'os': 'string',
            'cpu': {
                'frequency': 'string',
                'architecture': 'string',
                'clock': 123.0
            },
            'resolution': {
                'width': 123,
                'height': 123
            },
            'heapSize': 123,
            'memory': 123,
            'image': 'string',
            'carrier': 'string',
            'radio': 'string',
            'remoteAccessEnabled': True|False,
            'remoteDebugEnabled': True|False,
            'fleetType': 'string',
            'fleetName': 'string',
            'instances': [
                {
                    'arn': 'string',
                    'deviceArn': 'string',
                    'labels': [
                        'string',
                    ],
                    'status': 'IN_USE'|'PREPARING'|'AVAILABLE'|'NOT_AVAILABLE',
                    'udid': 'string',
                    'instanceProfile': {
                        'arn': 'string',
                        'packageCleanup': True|False,
                        'excludeAppPackagesFromCleanup': [
                            'string',
                        ],
                        'rebootAfterUse': True|False,
                        'name': 'string',
                        'description': 'string'
                    }
                },
            ],
            'availability': 'TEMPORARY_NOT_AVAILABLE'|'BUSY'|'AVAILABLE'|'HIGHLY_AVAILABLE'
        },
        'instanceArn': 'string',
        'remoteDebugEnabled': True|False,
        'remoteRecordEnabled': True|False,
        'remoteRecordAppArn': 'string',
        'hostAddress': 'string',
        'clientId': 'string',
        'billingMethod': 'METERED'|'UNMETERED',
        'deviceMinutes': {
            'total': 123.0,
            'metered': 123.0,
            'unmetered': 123.0
        },
        'endpoint': 'string',
        'deviceUdid': 'string',
        'interactionMode': 'INTERACTIVE'|'NO_VIDEO'|'VIDEO_ONLY',
        'skipAppResign': True|False
    }
}


Response Structure

(dict) --
Represents the server response from a request to create a remote access session.

remoteAccessSession (dict) --
A container that describes the remote access session when the request to create a remote access session is sent.

arn (string) --
The Amazon Resource Name (ARN) of the remote access session.

name (string) --
The name of the remote access session.

created (datetime) --
The date and time the remote access session was created.

status (string) --
The status of the remote access session. Can be any of the following:

PENDING.
PENDING_CONCURRENCY.
PENDING_DEVICE.
PROCESSING.
SCHEDULING.
PREPARING.
RUNNING.
COMPLETED.
STOPPING.


result (string) --
The result of the remote access session. Can be any of the following:

PENDING.
PASSED.
WARNED.
FAILED.
SKIPPED.
ERRORED.
STOPPED.


message (string) --
A message about the remote access session.

started (datetime) --
The date and time the remote access session was started.

stopped (datetime) --
The date and time the remote access session was stopped.

device (dict) --
The device (phone or tablet) used in the remote access session.

arn (string) --
The device\'s ARN.

name (string) --
The device\'s display name.

manufacturer (string) --
The device\'s manufacturer name.

model (string) --
The device\'s model name.

modelId (string) --
The device\'s model ID.

formFactor (string) --
The device\'s form factor.
Allowed values include:

PHONE
TABLET


platform (string) --
The device\'s platform.
Allowed values include:

ANDROID
IOS


os (string) --
The device\'s operating system type.

cpu (dict) --
Information about the device\'s CPU.

frequency (string) --
The CPU\'s frequency.

architecture (string) --
The CPU\'s architecture (for example, x86 or ARM).

clock (float) --
The clock speed of the device\'s CPU, expressed in hertz (Hz). For example, a 1.2 GHz CPU is expressed as 1200000000.



resolution (dict) --
The resolution of the device.

width (integer) --
The screen resolution\'s width, expressed in pixels.

height (integer) --
The screen resolution\'s height, expressed in pixels.



heapSize (integer) --
The device\'s heap size, expressed in bytes.

memory (integer) --
The device\'s total memory size, expressed in bytes.

image (string) --
The device\'s image name.

carrier (string) --
The device\'s carrier.

radio (string) --
The device\'s radio.

remoteAccessEnabled (boolean) --
Specifies whether remote access has been enabled for the specified device.

remoteDebugEnabled (boolean) --
This flag is set to true if remote debugging is enabled for the device.
Remote debugging is no longer supported .

fleetType (string) --
The type of fleet to which this device belongs. Possible values are PRIVATE and PUBLIC.

fleetName (string) --
The name of the fleet to which this device belongs.

instances (list) --
The instances that belong to this device.

(dict) --
Represents the device instance.

arn (string) --
The Amazon Resource Name (ARN) of the device instance.

deviceArn (string) --
The ARN of the device.

labels (list) --
An array of strings that describe the device instance.

(string) --


status (string) --
The status of the device instance. Valid values are listed here.

udid (string) --
Unique device identifier for the device instance.

instanceProfile (dict) --
A object that contains information about the instance profile.

arn (string) --
The Amazon Resource Name (ARN) of the instance profile.

packageCleanup (boolean) --
When set to true , Device Farm removes app packages after a test run. The default value is false for private devices.

excludeAppPackagesFromCleanup (list) --
An array of strings containing the list of app packages that should not be cleaned up from the device after a test run completes.
The list of packages is considered only if you set packageCleanup to true .

(string) --


rebootAfterUse (boolean) --
When set to true , Device Farm reboots the instance after a test run. The default value is true .

name (string) --
The name of the instance profile.

description (string) --
The description of the instance profile.







availability (string) --
Indicates how likely a device is available for a test run. Currently available in the  ListDevices and GetDevice API methods.



instanceArn (string) --
The ARN of the instance.

remoteDebugEnabled (boolean) --
This flag is set to true if remote debugging is enabled for the remote access session.
Remote debugging is no longer supported .

remoteRecordEnabled (boolean) --
This flag is set to true if remote recording is enabled for the remote access session.

remoteRecordAppArn (string) --
The ARN for the app to be recorded in the remote access session.

hostAddress (string) --
IP address of the EC2 host where you need to connect to remotely debug devices. Only returned if remote debugging is enabled for the remote access session.
Remote debugging is no longer supported .

clientId (string) --
Unique identifier of your client for the remote access session. Only returned if remote debugging is enabled for the remote access session.
Remote debugging is no longer supported .

billingMethod (string) --
The billing method of the remote access session. Possible values include METERED or UNMETERED . For more information about metered devices, see AWS Device Farm terminology .

deviceMinutes (dict) --
The number of minutes a device is used in a remote access session (including setup and teardown minutes).

total (float) --
When specified, represents the total minutes used by the resource to run tests.

metered (float) --
When specified, represents only the sum of metered minutes used by the resource to run tests.

unmetered (float) --
When specified, represents only the sum of unmetered minutes used by the resource to run tests.



endpoint (string) --
The endpoint for the remote access sesssion.

deviceUdid (string) --
Unique device identifier for the remote device. Only returned if remote debugging is enabled for the remote access session.
Remote debugging is no longer supported .

interactionMode (string) --
The interaction mode of the remote access session. Valid values are:

INTERACTIVE: You can interact with the iOS device by viewing, touching, and rotating the screen. You cannot run XCUITest framework-based tests in this mode.
NO_VIDEO: You are connected to the device, but cannot interact with it or view the screen. This mode has the fastest test execution speed. You can run XCUITest framework-based tests in this mode.
VIDEO_ONLY: You can view the screen, but cannot touch or rotate it. You can run XCUITest framework-based tests and watch the screen in this mode.


skipAppResign (boolean) --
When set to true , for private devices, Device Farm does not sign your app again. For public devices, Device Farm always signs your apps again.
For more information about how Device Farm re-signs your apps, see Do you modify my app? in the AWS Device Farm FAQs .









Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.LimitExceededException
DeviceFarm.Client.exceptions.ServiceAccountException

Examples
The following example creates a remote access session named MySession.
response = client.create_remote_access_session(
    name='MySession',
    configuration={
        'billingMethod': 'METERED',
    },
    # You can get the device ARN by using the list-devices CLI command.
    deviceArn='arn:aws:devicefarm:us-west-2::device:123EXAMPLE',
    # You can get the project ARN by using the list-projects CLI command.
    projectArn='arn:aws:devicefarm:us-west-2:123456789101:project:EXAMPLE-GUID-123-456',
)

print(response)


Expected Output:
{
    'remoteAccessSession': {
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'remoteAccessSession': {
            'arn': 'string',
            'name': 'string',
            'created': datetime(2015, 1, 1),
            'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
            'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
            'message': 'string',
            'started': datetime(2015, 1, 1),
            'stopped': datetime(2015, 1, 1),
            'device': {
                'arn': 'string',
                'name': 'string',
                'manufacturer': 'string',
                'model': 'string',
                'modelId': 'string',
                'formFactor': 'PHONE'|'TABLET',
                'platform': 'ANDROID'|'IOS',
                'os': 'string',
                'cpu': {
                    'frequency': 'string',
                    'architecture': 'string',
                    'clock': 123.0
                },
                'resolution': {
                    'width': 123,
                    'height': 123
                },
                'heapSize': 123,
                'memory': 123,
                'image': 'string',
                'carrier': 'string',
                'radio': 'string',
                'remoteAccessEnabled': True|False,
                'remoteDebugEnabled': True|False,
                'fleetType': 'string',
                'fleetName': 'string',
                'instances': [
                    {
                        'arn': 'string',
                        'deviceArn': 'string',
                        'labels': [
                            'string',
                        ],
                        'status': 'IN_USE'|'PREPARING'|'AVAILABLE'|'NOT_AVAILABLE',
                        'udid': 'string',
                        'instanceProfile': {
                            'arn': 'string',
                            'packageCleanup': True|False,
                            'excludeAppPackagesFromCleanup': [
                                'string',
                            ],
                            'rebootAfterUse': True|False,
                            'name': 'string',
                            'description': 'string'
                        }
                    },
                ],
                'availability': 'TEMPORARY_NOT_AVAILABLE'|'BUSY'|'AVAILABLE'|'HIGHLY_AVAILABLE'
            },
            'instanceArn': 'string',
            'remoteDebugEnabled': True|False,
            'remoteRecordEnabled': True|False,
            'remoteRecordAppArn': 'string',
            'hostAddress': 'string',
            'clientId': 'string',
            'billingMethod': 'METERED'|'UNMETERED',
            'deviceMinutes': {
                'total': 123.0,
                'metered': 123.0,
                'unmetered': 123.0
            },
            'endpoint': 'string',
            'deviceUdid': 'string',
            'interactionMode': 'INTERACTIVE'|'NO_VIDEO'|'VIDEO_ONLY',
            'skipAppResign': True|False
        }
    }
    
    
    :returns: 
    PENDING.
    PENDING_CONCURRENCY.
    PENDING_DEVICE.
    PROCESSING.
    SCHEDULING.
    PREPARING.
    RUNNING.
    COMPLETED.
    STOPPING.
    
    """
    pass

def create_test_grid_project(name=None, description=None):
    """
    Creates a Selenium testing project. Projects are used to track  TestGridSession instances.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_test_grid_project(
        name='string',
        description='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nHuman-readable name of the Selenium testing project.\n

    :type description: string
    :param description: Human-readable description of the project.

    :rtype: dict

ReturnsResponse Syntax
{
    'testGridProject': {
        'arn': 'string',
        'name': 'string',
        'description': 'string',
        'created': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --

testGridProject (dict) --
ARN of the Selenium testing project that was created.

arn (string) --
The ARN for the project.

name (string) --
A human-readable name for the project.

description (string) --
A human-readable description for the project.

created (datetime) --
When the project was created.









Exceptions

DeviceFarm.Client.exceptions.InternalServiceException


    :return: {
        'testGridProject': {
            'arn': 'string',
            'name': 'string',
            'description': 'string',
            'created': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    DeviceFarm.Client.exceptions.InternalServiceException
    
    """
    pass

def create_test_grid_url(projectArn=None, expiresInSeconds=None):
    """
    Creates a signed, short-term URL that can be passed to a Selenium RemoteWebDriver constructor.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_test_grid_url(
        projectArn='string',
        expiresInSeconds=123
    )
    
    
    :type projectArn: string
    :param projectArn: [REQUIRED]\nARN (from CreateTestGridProject or ListTestGridProjects ) to associate with the short-term URL.\n

    :type expiresInSeconds: integer
    :param expiresInSeconds: [REQUIRED]\nLifetime, in seconds, of the URL.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'url': 'string',
    'expires': datetime(2015, 1, 1)
}


Response Structure

(dict) --

url (string) --
A signed URL, expiring in  CreateTestGridUrlRequest$expiresInSeconds seconds, to be passed to a RemoteWebDriver .

expires (datetime) --
The number of seconds the URL from  CreateTestGridUrlResult$url stays active.







Exceptions

DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.InternalServiceException


    :return: {
        'url': 'string',
        'expires': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    DeviceFarm.Client.exceptions.NotFoundException
    DeviceFarm.Client.exceptions.ArgumentException
    DeviceFarm.Client.exceptions.InternalServiceException
    
    """
    pass

def create_upload(projectArn=None, name=None, type=None, contentType=None):
    """
    Uploads an app or test scripts.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example creates a new Appium Python test package upload inside an existing project.
    Expected Output:
    
    :example: response = client.create_upload(
        projectArn='string',
        name='string',
        type='ANDROID_APP'|'IOS_APP'|'WEB_APP'|'EXTERNAL_DATA'|'APPIUM_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_PYTHON_TEST_PACKAGE'|'APPIUM_NODE_TEST_PACKAGE'|'APPIUM_RUBY_TEST_PACKAGE'|'APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_WEB_PYTHON_TEST_PACKAGE'|'APPIUM_WEB_NODE_TEST_PACKAGE'|'APPIUM_WEB_RUBY_TEST_PACKAGE'|'CALABASH_TEST_PACKAGE'|'INSTRUMENTATION_TEST_PACKAGE'|'UIAUTOMATION_TEST_PACKAGE'|'UIAUTOMATOR_TEST_PACKAGE'|'XCTEST_TEST_PACKAGE'|'XCTEST_UI_TEST_PACKAGE'|'APPIUM_JAVA_JUNIT_TEST_SPEC'|'APPIUM_JAVA_TESTNG_TEST_SPEC'|'APPIUM_PYTHON_TEST_SPEC'|'APPIUM_NODE_TEST_SPEC'|'APPIUM_RUBY_TEST_SPEC'|'APPIUM_WEB_JAVA_JUNIT_TEST_SPEC'|'APPIUM_WEB_JAVA_TESTNG_TEST_SPEC'|'APPIUM_WEB_PYTHON_TEST_SPEC'|'APPIUM_WEB_NODE_TEST_SPEC'|'APPIUM_WEB_RUBY_TEST_SPEC'|'INSTRUMENTATION_TEST_SPEC'|'XCTEST_UI_TEST_SPEC',
        contentType='string'
    )
    
    
    :type projectArn: string
    :param projectArn: [REQUIRED]\nThe ARN of the project for the upload.\n

    :type name: string
    :param name: [REQUIRED]\nThe upload\'s file name. The name should not contain any forward slashes (/ ). If you are uploading an iOS app, the file name must end with the .ipa extension. If you are uploading an Android app, the file name must end with the .apk extension. For all others, the file name must end with the .zip file extension.\n

    :type type: string
    :param type: [REQUIRED]\nThe upload\'s upload type.\nMust be one of the following values:\n\nANDROID_APP\nIOS_APP\nWEB_APP\nEXTERNAL_DATA\nAPPIUM_JAVA_JUNIT_TEST_PACKAGE\nAPPIUM_JAVA_TESTNG_TEST_PACKAGE\nAPPIUM_PYTHON_TEST_PACKAGE\nAPPIUM_NODE_TEST_PACKAGE\nAPPIUM_RUBY_TEST_PACKAGE\nAPPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE\nAPPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE\nAPPIUM_WEB_PYTHON_TEST_PACKAGE\nAPPIUM_WEB_NODE_TEST_PACKAGE\nAPPIUM_WEB_RUBY_TEST_PACKAGE\nCALABASH_TEST_PACKAGE\nINSTRUMENTATION_TEST_PACKAGE\nUIAUTOMATION_TEST_PACKAGE\nUIAUTOMATOR_TEST_PACKAGE\nXCTEST_TEST_PACKAGE\nXCTEST_UI_TEST_PACKAGE\nAPPIUM_JAVA_JUNIT_TEST_SPEC\nAPPIUM_JAVA_TESTNG_TEST_SPEC\nAPPIUM_PYTHON_TEST_SPEC\nAPPIUM_NODE_TEST_SPEC\nAPPIUM_RUBY_TEST_SPEC\nAPPIUM_WEB_JAVA_JUNIT_TEST_SPEC\nAPPIUM_WEB_JAVA_TESTNG_TEST_SPEC\nAPPIUM_WEB_PYTHON_TEST_SPEC\nAPPIUM_WEB_NODE_TEST_SPEC\nAPPIUM_WEB_RUBY_TEST_SPEC\nINSTRUMENTATION_TEST_SPEC\nXCTEST_UI_TEST_SPEC\n\nIf you call CreateUpload with WEB_APP specified, AWS Device Farm throws an ArgumentException error.\n

    :type contentType: string
    :param contentType: The upload\'s content type (for example, application/octet-stream ).

    :rtype: dict

ReturnsResponse Syntax
{
    'upload': {
        'arn': 'string',
        'name': 'string',
        'created': datetime(2015, 1, 1),
        'type': 'ANDROID_APP'|'IOS_APP'|'WEB_APP'|'EXTERNAL_DATA'|'APPIUM_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_PYTHON_TEST_PACKAGE'|'APPIUM_NODE_TEST_PACKAGE'|'APPIUM_RUBY_TEST_PACKAGE'|'APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_WEB_PYTHON_TEST_PACKAGE'|'APPIUM_WEB_NODE_TEST_PACKAGE'|'APPIUM_WEB_RUBY_TEST_PACKAGE'|'CALABASH_TEST_PACKAGE'|'INSTRUMENTATION_TEST_PACKAGE'|'UIAUTOMATION_TEST_PACKAGE'|'UIAUTOMATOR_TEST_PACKAGE'|'XCTEST_TEST_PACKAGE'|'XCTEST_UI_TEST_PACKAGE'|'APPIUM_JAVA_JUNIT_TEST_SPEC'|'APPIUM_JAVA_TESTNG_TEST_SPEC'|'APPIUM_PYTHON_TEST_SPEC'|'APPIUM_NODE_TEST_SPEC'|'APPIUM_RUBY_TEST_SPEC'|'APPIUM_WEB_JAVA_JUNIT_TEST_SPEC'|'APPIUM_WEB_JAVA_TESTNG_TEST_SPEC'|'APPIUM_WEB_PYTHON_TEST_SPEC'|'APPIUM_WEB_NODE_TEST_SPEC'|'APPIUM_WEB_RUBY_TEST_SPEC'|'INSTRUMENTATION_TEST_SPEC'|'XCTEST_UI_TEST_SPEC',
        'status': 'INITIALIZED'|'PROCESSING'|'SUCCEEDED'|'FAILED',
        'url': 'string',
        'metadata': 'string',
        'contentType': 'string',
        'message': 'string',
        'category': 'CURATED'|'PRIVATE'
    }
}


Response Structure

(dict) --
Represents the result of a create upload request.

upload (dict) --
The newly created upload.

arn (string) --
The upload\'s ARN.

name (string) --
The upload\'s file name.

created (datetime) --
When the upload was created.

type (string) --
The upload\'s type.
Must be one of the following values:

ANDROID_APP
IOS_APP
WEB_APP
EXTERNAL_DATA
APPIUM_JAVA_JUNIT_TEST_PACKAGE
APPIUM_JAVA_TESTNG_TEST_PACKAGE
APPIUM_PYTHON_TEST_PACKAGE
APPIUM_NODE_TEST_PACKAGE
APPIUM_RUBY_TEST_PACKAGE
APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE
APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE
APPIUM_WEB_PYTHON_TEST_PACKAGE
APPIUM_WEB_NODE_TEST_PACKAGE
APPIUM_WEB_RUBY_TEST_PACKAGE
CALABASH_TEST_PACKAGE
INSTRUMENTATION_TEST_PACKAGE
UIAUTOMATION_TEST_PACKAGE
UIAUTOMATOR_TEST_PACKAGE
XCTEST_TEST_PACKAGE
XCTEST_UI_TEST_PACKAGE
APPIUM_JAVA_JUNIT_TEST_SPEC
APPIUM_JAVA_TESTNG_TEST_SPEC
APPIUM_PYTHON_TEST_SPEC
APPIUM_NODE_TEST_SPEC
APPIUM_RUBY_TEST_SPEC
APPIUM_WEB_JAVA_JUNIT_TEST_SPEC
APPIUM_WEB_JAVA_TESTNG_TEST_SPEC
APPIUM_WEB_PYTHON_TEST_SPEC
APPIUM_WEB_NODE_TEST_SPEC
APPIUM_WEB_RUBY_TEST_SPEC
INSTRUMENTATION_TEST_SPEC
XCTEST_UI_TEST_SPEC


status (string) --
The upload\'s status.
Must be one of the following values:

FAILED
INITIALIZED
PROCESSING
SUCCEEDED


url (string) --
The presigned Amazon S3 URL that was used to store a file using a PUT request.

metadata (string) --
The upload\'s metadata. For example, for Android, this contains information that is parsed from the manifest and is displayed in the AWS Device Farm console after the associated app is uploaded.

contentType (string) --
The upload\'s content type (for example, application/octet-stream ).

message (string) --
A message about the upload\'s result.

category (string) --
The upload\'s category. Allowed values include:

CURATED: An upload managed by AWS Device Farm.
PRIVATE: An upload managed by the AWS Device Farm customer.










Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.LimitExceededException
DeviceFarm.Client.exceptions.ServiceAccountException

Examples
The following example creates a new Appium Python test package upload inside an existing project.
response = client.create_upload(
    name='MyAppiumPythonUpload',
    type='APPIUM_PYTHON_TEST_PACKAGE',
    # You can get the project ARN by using the list-projects CLI command.
    projectArn='arn:aws:devicefarm:us-west-2:123456789101:project:EXAMPLE-GUID-123-456',
)

print(response)


Expected Output:
{
    'upload': {
        'name': 'MyAppiumPythonUpload',
        'type': 'APPIUM_PYTHON_TEST_PACKAGE',
        'arn': 'arn:aws:devicefarm:us-west-2:123456789101:upload:5e01a8c7-c861-4c0a-b1d5-5ec6e6c6dd23/b5340a65-3da7-4da6-a26e-12345EXAMPLE',
        'created': datetime(2016, 8, 31, 16, 36, 44, 2, 244, 0),
        'status': 'INITIALIZED',
        'url': 'https://prod-us-west-2-uploads.s3-us-west-2.amazonaws.com/arn%3Aaws%3Adevicefarm%3Aus-west-2%3A123456789101%3Aproject%3A5e01a8c7-c861-4c0a-b1d5-12345EXAMPLE/uploads/arn%3Aaws%3Adevicefarm%3Aus-west-2%3A123456789101%3Aupload%3A5e01a8c7-c861-4c0a-b1d5-5ec6e6c6dd23/b5340a65-3da7-4da6-a26e-12345EXAMPLE/MyAppiumPythonUpload?AWSAccessKeyId=1234567891011EXAMPLE&Expires=1472747804&Signature=1234567891011EXAMPLE',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'upload': {
            'arn': 'string',
            'name': 'string',
            'created': datetime(2015, 1, 1),
            'type': 'ANDROID_APP'|'IOS_APP'|'WEB_APP'|'EXTERNAL_DATA'|'APPIUM_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_PYTHON_TEST_PACKAGE'|'APPIUM_NODE_TEST_PACKAGE'|'APPIUM_RUBY_TEST_PACKAGE'|'APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_WEB_PYTHON_TEST_PACKAGE'|'APPIUM_WEB_NODE_TEST_PACKAGE'|'APPIUM_WEB_RUBY_TEST_PACKAGE'|'CALABASH_TEST_PACKAGE'|'INSTRUMENTATION_TEST_PACKAGE'|'UIAUTOMATION_TEST_PACKAGE'|'UIAUTOMATOR_TEST_PACKAGE'|'XCTEST_TEST_PACKAGE'|'XCTEST_UI_TEST_PACKAGE'|'APPIUM_JAVA_JUNIT_TEST_SPEC'|'APPIUM_JAVA_TESTNG_TEST_SPEC'|'APPIUM_PYTHON_TEST_SPEC'|'APPIUM_NODE_TEST_SPEC'|'APPIUM_RUBY_TEST_SPEC'|'APPIUM_WEB_JAVA_JUNIT_TEST_SPEC'|'APPIUM_WEB_JAVA_TESTNG_TEST_SPEC'|'APPIUM_WEB_PYTHON_TEST_SPEC'|'APPIUM_WEB_NODE_TEST_SPEC'|'APPIUM_WEB_RUBY_TEST_SPEC'|'INSTRUMENTATION_TEST_SPEC'|'XCTEST_UI_TEST_SPEC',
            'status': 'INITIALIZED'|'PROCESSING'|'SUCCEEDED'|'FAILED',
            'url': 'string',
            'metadata': 'string',
            'contentType': 'string',
            'message': 'string',
            'category': 'CURATED'|'PRIVATE'
        }
    }
    
    
    :returns: 
    ANDROID_APP
    IOS_APP
    WEB_APP
    EXTERNAL_DATA
    APPIUM_JAVA_JUNIT_TEST_PACKAGE
    APPIUM_JAVA_TESTNG_TEST_PACKAGE
    APPIUM_PYTHON_TEST_PACKAGE
    APPIUM_NODE_TEST_PACKAGE
    APPIUM_RUBY_TEST_PACKAGE
    APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE
    APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE
    APPIUM_WEB_PYTHON_TEST_PACKAGE
    APPIUM_WEB_NODE_TEST_PACKAGE
    APPIUM_WEB_RUBY_TEST_PACKAGE
    CALABASH_TEST_PACKAGE
    INSTRUMENTATION_TEST_PACKAGE
    UIAUTOMATION_TEST_PACKAGE
    UIAUTOMATOR_TEST_PACKAGE
    XCTEST_TEST_PACKAGE
    XCTEST_UI_TEST_PACKAGE
    APPIUM_JAVA_JUNIT_TEST_SPEC
    APPIUM_JAVA_TESTNG_TEST_SPEC
    APPIUM_PYTHON_TEST_SPEC
    APPIUM_NODE_TEST_SPEC
    APPIUM_RUBY_TEST_SPEC
    APPIUM_WEB_JAVA_JUNIT_TEST_SPEC
    APPIUM_WEB_JAVA_TESTNG_TEST_SPEC
    APPIUM_WEB_PYTHON_TEST_SPEC
    APPIUM_WEB_NODE_TEST_SPEC
    APPIUM_WEB_RUBY_TEST_SPEC
    INSTRUMENTATION_TEST_SPEC
    XCTEST_UI_TEST_SPEC
    
    """
    pass

def create_vpce_configuration(vpceConfigurationName=None, vpceServiceName=None, serviceDnsName=None, vpceConfigurationDescription=None):
    """
    Creates a configuration record in Device Farm for your Amazon Virtual Private Cloud (VPC) endpoint.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_vpce_configuration(
        vpceConfigurationName='string',
        vpceServiceName='string',
        serviceDnsName='string',
        vpceConfigurationDescription='string'
    )
    
    
    :type vpceConfigurationName: string
    :param vpceConfigurationName: [REQUIRED]\nThe friendly name you give to your VPC endpoint configuration, to manage your configurations more easily.\n

    :type vpceServiceName: string
    :param vpceServiceName: [REQUIRED]\nThe name of the VPC endpoint service running in your AWS account that you want Device Farm to test.\n

    :type serviceDnsName: string
    :param serviceDnsName: [REQUIRED]\nThe DNS name of the service running in your VPC that you want Device Farm to test.\n

    :type vpceConfigurationDescription: string
    :param vpceConfigurationDescription: An optional description that provides details about your VPC endpoint configuration.

    :rtype: dict

ReturnsResponse Syntax
{
    'vpceConfiguration': {
        'arn': 'string',
        'vpceConfigurationName': 'string',
        'vpceServiceName': 'string',
        'serviceDnsName': 'string',
        'vpceConfigurationDescription': 'string'
    }
}


Response Structure

(dict) --

vpceConfiguration (dict) --
An object that contains information about your VPC endpoint configuration.

arn (string) --
The Amazon Resource Name (ARN) of the VPC endpoint configuration.

vpceConfigurationName (string) --
The friendly name you give to your VPC endpoint configuration to manage your configurations more easily.

vpceServiceName (string) --
The name of the VPC endpoint service running in your AWS account that you want Device Farm to test.

serviceDnsName (string) --
The DNS name that maps to the private IP address of the service you want to access.

vpceConfigurationDescription (string) --
An optional description that provides details about your VPC endpoint configuration.









Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.LimitExceededException
DeviceFarm.Client.exceptions.ServiceAccountException


    :return: {
        'vpceConfiguration': {
            'arn': 'string',
            'vpceConfigurationName': 'string',
            'vpceServiceName': 'string',
            'serviceDnsName': 'string',
            'vpceConfigurationDescription': 'string'
        }
    }
    
    
    :returns: 
    DeviceFarm.Client.exceptions.ArgumentException
    DeviceFarm.Client.exceptions.LimitExceededException
    DeviceFarm.Client.exceptions.ServiceAccountException
    
    """
    pass

def delete_device_pool(arn=None):
    """
    Deletes a device pool given the pool ARN. Does not allow deletion of curated pools owned by the system.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example deletes a specific device pool.
    Expected Output:
    
    :example: response = client.delete_device_pool(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]\nRepresents the Amazon Resource Name (ARN) of the Device Farm device pool to delete.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --Represents the result of a delete device pool request.




Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.LimitExceededException
DeviceFarm.Client.exceptions.ServiceAccountException

Examples
The following example deletes a specific device pool.
response = client.delete_device_pool(
    # You can get the device pool ARN by using the list-device-pools CLI command.
    arn='arn:aws:devicefarm:us-west-2::devicepool:123-456-EXAMPLE-GUID',
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {}
    
    
    """
    pass

def delete_instance_profile(arn=None):
    """
    Deletes a profile that can be applied to one or more private device instances.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_instance_profile(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the instance profile you are requesting to delete.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.LimitExceededException
DeviceFarm.Client.exceptions.ServiceAccountException


    :return: {}
    
    
    :returns: 
    DeviceFarm.Client.exceptions.ArgumentException
    DeviceFarm.Client.exceptions.NotFoundException
    DeviceFarm.Client.exceptions.LimitExceededException
    DeviceFarm.Client.exceptions.ServiceAccountException
    
    """
    pass

def delete_network_profile(arn=None):
    """
    Deletes a network profile.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_network_profile(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]\nThe ARN of the network profile to delete.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.LimitExceededException
DeviceFarm.Client.exceptions.ServiceAccountException


    :return: {}
    
    
    :returns: 
    DeviceFarm.Client.exceptions.ArgumentException
    DeviceFarm.Client.exceptions.NotFoundException
    DeviceFarm.Client.exceptions.LimitExceededException
    DeviceFarm.Client.exceptions.ServiceAccountException
    
    """
    pass

def delete_project(arn=None):
    """
    Deletes an AWS Device Farm project, given the project ARN.
    Deleting this resource does not stop an in-progress run.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example deletes a specific project.
    Expected Output:
    
    :example: response = client.delete_project(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]\nRepresents the Amazon Resource Name (ARN) of the Device Farm project to delete.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --Represents the result of a delete project request.




Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.LimitExceededException
DeviceFarm.Client.exceptions.ServiceAccountException

Examples
The following example deletes a specific project.
response = client.delete_project(
    # You can get the project ARN by using the list-projects CLI command.
    arn='arn:aws:devicefarm:us-west-2:123456789101:project:EXAMPLE-GUID-123-456',
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {}
    
    
    """
    pass

def delete_remote_access_session(arn=None):
    """
    Deletes a completed remote access session and its results.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example deletes a specific remote access session.
    Expected Output:
    
    :example: response = client.delete_remote_access_session(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the session for which you want to delete remote access.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --The response from the server when a request is made to delete the remote access session.




Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.LimitExceededException
DeviceFarm.Client.exceptions.ServiceAccountException

Examples
The following example deletes a specific remote access session.
response = client.delete_remote_access_session(
    # You can get the remote access session ARN by using the list-remote-access-sessions CLI command.
    arn='arn:aws:devicefarm:us-west-2:123456789101:session:EXAMPLE-GUID-123-456',
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {}
    
    
    """
    pass

def delete_run(arn=None):
    """
    Deletes the run, given the run ARN.
    Deleting this resource does not stop an in-progress run.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example deletes a specific test run.
    Expected Output:
    
    :example: response = client.delete_run(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]\nThe Amazon Resource Name (ARN) for the run to delete.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --Represents the result of a delete run request.




Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.LimitExceededException
DeviceFarm.Client.exceptions.ServiceAccountException

Examples
The following example deletes a specific test run.
response = client.delete_run(
    # You can get the run ARN by using the list-runs CLI command.
    arn='arn:aws:devicefarm:us-west-2:123456789101:run:EXAMPLE-GUID-123-456',
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {}
    
    
    """
    pass

def delete_test_grid_project(projectArn=None):
    """
    Deletes a Selenium testing project and all content generated under it.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_test_grid_project(
        projectArn='string'
    )
    
    
    :type projectArn: string
    :param projectArn: [REQUIRED]\nThe ARN of the project to delete, from CreateTestGridProject or ListTestGridProjects .\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.CannotDeleteException
DeviceFarm.Client.exceptions.InternalServiceException


    :return: {}
    
    
    :returns: 
    DeviceFarm.Client.exceptions.NotFoundException
    DeviceFarm.Client.exceptions.ArgumentException
    DeviceFarm.Client.exceptions.CannotDeleteException
    DeviceFarm.Client.exceptions.InternalServiceException
    
    """
    pass

def delete_upload(arn=None):
    """
    Deletes an upload given the upload ARN.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example deletes a specific upload.
    Expected Output:
    
    :example: response = client.delete_upload(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]\nRepresents the Amazon Resource Name (ARN) of the Device Farm upload to delete.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --Represents the result of a delete upload request.




Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.LimitExceededException
DeviceFarm.Client.exceptions.ServiceAccountException

Examples
The following example deletes a specific upload.
response = client.delete_upload(
    # You can get the upload ARN by using the list-uploads CLI command.
    arn='arn:aws:devicefarm:us-west-2:123456789101:upload:EXAMPLE-GUID-123-456',
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {}
    
    
    """
    pass

def delete_vpce_configuration(arn=None):
    """
    Deletes a configuration for your Amazon Virtual Private Cloud (VPC) endpoint.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_vpce_configuration(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the VPC endpoint configuration you want to delete.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.ServiceAccountException
DeviceFarm.Client.exceptions.InvalidOperationException


    :return: {}
    
    
    :returns: 
    DeviceFarm.Client.exceptions.ArgumentException
    DeviceFarm.Client.exceptions.NotFoundException
    DeviceFarm.Client.exceptions.ServiceAccountException
    DeviceFarm.Client.exceptions.InvalidOperationException
    
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

def get_account_settings():
    """
    Returns the number of unmetered iOS or unmetered Android devices that have been purchased by the account.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example returns information about your Device Farm account settings.
    Expected Output:
    
    :example: response = client.get_account_settings()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'accountSettings': {
        'awsAccountNumber': 'string',
        'unmeteredDevices': {
            'string': 123
        },
        'unmeteredRemoteAccessDevices': {
            'string': 123
        },
        'maxJobTimeoutMinutes': 123,
        'trialMinutes': {
            'total': 123.0,
            'remaining': 123.0
        },
        'maxSlots': {
            'string': 123
        },
        'defaultJobTimeoutMinutes': 123,
        'skipAppResign': True|False
    }
}


Response Structure

(dict) --Represents the account settings return values from the GetAccountSettings request.

accountSettings (dict) --The account settings.

awsAccountNumber (string) --The AWS account number specified in the AccountSettings container.

unmeteredDevices (dict) --Returns the unmetered devices you have purchased or want to purchase.

(string) --
(integer) --




unmeteredRemoteAccessDevices (dict) --Returns the unmetered remote access devices you have purchased or want to purchase.

(string) --
(integer) --




maxJobTimeoutMinutes (integer) --The maximum number of minutes a test run executes before it times out.

trialMinutes (dict) --Information about an AWS account\'s usage of free trial device minutes.

total (float) --The total number of free trial minutes that the account started with.

remaining (float) --The number of free trial minutes remaining in the account.



maxSlots (dict) --The maximum number of device slots that the AWS account can purchase. Each maximum is expressed as an offering-id:number pair, where the offering-id represents one of the IDs returned by the ListOfferings command.

(string) --
(integer) --




defaultJobTimeoutMinutes (integer) --The default number of minutes (at the account level) a test run executes before it times out. The default value is 150 minutes.

skipAppResign (boolean) --When set to true , for private devices, Device Farm does not sign your app again. For public devices, Device Farm always signs your apps again.
For more information about how Device Farm re-signs your apps, see Do you modify my app? in the AWS Device Farm FAQs .








Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.LimitExceededException
DeviceFarm.Client.exceptions.ServiceAccountException

Examples
The following example returns information about your Device Farm account settings.
response = client.get_account_settings(
)

print(response)


Expected Output:
{
    'accountSettings': {
        'awsAccountNumber': '123456789101',
        'unmeteredDevices': {
            'ANDROID': 1,
            'IOS': 2,
        },
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'accountSettings': {
            'awsAccountNumber': 'string',
            'unmeteredDevices': {
                'string': 123
            },
            'unmeteredRemoteAccessDevices': {
                'string': 123
            },
            'maxJobTimeoutMinutes': 123,
            'trialMinutes': {
                'total': 123.0,
                'remaining': 123.0
            },
            'maxSlots': {
                'string': 123
            },
            'defaultJobTimeoutMinutes': 123,
            'skipAppResign': True|False
        }
    }
    
    
    :returns: 
    (string) --
    (integer) --
    
    
    
    """
    pass

def get_device(arn=None):
    """
    Gets information about a unique device type.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example returns information about a specific device.
    Expected Output:
    
    :example: response = client.get_device(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]\nThe device type\'s ARN.\n

    :rtype: dict
ReturnsResponse Syntax{
    'device': {
        'arn': 'string',
        'name': 'string',
        'manufacturer': 'string',
        'model': 'string',
        'modelId': 'string',
        'formFactor': 'PHONE'|'TABLET',
        'platform': 'ANDROID'|'IOS',
        'os': 'string',
        'cpu': {
            'frequency': 'string',
            'architecture': 'string',
            'clock': 123.0
        },
        'resolution': {
            'width': 123,
            'height': 123
        },
        'heapSize': 123,
        'memory': 123,
        'image': 'string',
        'carrier': 'string',
        'radio': 'string',
        'remoteAccessEnabled': True|False,
        'remoteDebugEnabled': True|False,
        'fleetType': 'string',
        'fleetName': 'string',
        'instances': [
            {
                'arn': 'string',
                'deviceArn': 'string',
                'labels': [
                    'string',
                ],
                'status': 'IN_USE'|'PREPARING'|'AVAILABLE'|'NOT_AVAILABLE',
                'udid': 'string',
                'instanceProfile': {
                    'arn': 'string',
                    'packageCleanup': True|False,
                    'excludeAppPackagesFromCleanup': [
                        'string',
                    ],
                    'rebootAfterUse': True|False,
                    'name': 'string',
                    'description': 'string'
                }
            },
        ],
        'availability': 'TEMPORARY_NOT_AVAILABLE'|'BUSY'|'AVAILABLE'|'HIGHLY_AVAILABLE'
    }
}


Response Structure

(dict) --Represents the result of a get device request.

device (dict) --An object that contains information about the requested device.

arn (string) --The device\'s ARN.

name (string) --The device\'s display name.

manufacturer (string) --The device\'s manufacturer name.

model (string) --The device\'s model name.

modelId (string) --The device\'s model ID.

formFactor (string) --The device\'s form factor.
Allowed values include:

PHONE
TABLET


platform (string) --The device\'s platform.
Allowed values include:

ANDROID
IOS


os (string) --The device\'s operating system type.

cpu (dict) --Information about the device\'s CPU.

frequency (string) --The CPU\'s frequency.

architecture (string) --The CPU\'s architecture (for example, x86 or ARM).

clock (float) --The clock speed of the device\'s CPU, expressed in hertz (Hz). For example, a 1.2 GHz CPU is expressed as 1200000000.



resolution (dict) --The resolution of the device.

width (integer) --The screen resolution\'s width, expressed in pixels.

height (integer) --The screen resolution\'s height, expressed in pixels.



heapSize (integer) --The device\'s heap size, expressed in bytes.

memory (integer) --The device\'s total memory size, expressed in bytes.

image (string) --The device\'s image name.

carrier (string) --The device\'s carrier.

radio (string) --The device\'s radio.

remoteAccessEnabled (boolean) --Specifies whether remote access has been enabled for the specified device.

remoteDebugEnabled (boolean) --This flag is set to true if remote debugging is enabled for the device.
Remote debugging is no longer supported .

fleetType (string) --The type of fleet to which this device belongs. Possible values are PRIVATE and PUBLIC.

fleetName (string) --The name of the fleet to which this device belongs.

instances (list) --The instances that belong to this device.

(dict) --Represents the device instance.

arn (string) --The Amazon Resource Name (ARN) of the device instance.

deviceArn (string) --The ARN of the device.

labels (list) --An array of strings that describe the device instance.

(string) --


status (string) --The status of the device instance. Valid values are listed here.

udid (string) --Unique device identifier for the device instance.

instanceProfile (dict) --A object that contains information about the instance profile.

arn (string) --The Amazon Resource Name (ARN) of the instance profile.

packageCleanup (boolean) --When set to true , Device Farm removes app packages after a test run. The default value is false for private devices.

excludeAppPackagesFromCleanup (list) --An array of strings containing the list of app packages that should not be cleaned up from the device after a test run completes.
The list of packages is considered only if you set packageCleanup to true .

(string) --


rebootAfterUse (boolean) --When set to true , Device Farm reboots the instance after a test run. The default value is true .

name (string) --The name of the instance profile.

description (string) --The description of the instance profile.







availability (string) --Indicates how likely a device is available for a test run. Currently available in the  ListDevices and GetDevice API methods.








Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.LimitExceededException
DeviceFarm.Client.exceptions.ServiceAccountException

Examples
The following example returns information about a specific device.
response = client.get_device(
    arn='arn:aws:devicefarm:us-west-2::device:123EXAMPLE',
)

print(response)


Expected Output:
{
    'device': {
        'name': 'LG G2 (Sprint)',
        'arn': 'arn:aws:devicefarm:us-west-2::device:A0E6E6E1059E45918208DF75B2B7EF6C',
        'cpu': {
            'architecture': 'armeabi-v7a',
            'clock': 2265.6,
            'frequency': 'MHz',
        },
        'formFactor': 'PHONE',
        'heapSize': 256000000,
        'image': '75B2B7EF6C12345EXAMPLE',
        'manufacturer': 'LG',
        'memory': 16000000000,
        'model': 'G2 (Sprint)',
        'os': '4.2.2',
        'platform': 'ANDROID',
        'resolution': {
            'height': 1920,
            'width': 1080,
        },
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'device': {
            'arn': 'string',
            'name': 'string',
            'manufacturer': 'string',
            'model': 'string',
            'modelId': 'string',
            'formFactor': 'PHONE'|'TABLET',
            'platform': 'ANDROID'|'IOS',
            'os': 'string',
            'cpu': {
                'frequency': 'string',
                'architecture': 'string',
                'clock': 123.0
            },
            'resolution': {
                'width': 123,
                'height': 123
            },
            'heapSize': 123,
            'memory': 123,
            'image': 'string',
            'carrier': 'string',
            'radio': 'string',
            'remoteAccessEnabled': True|False,
            'remoteDebugEnabled': True|False,
            'fleetType': 'string',
            'fleetName': 'string',
            'instances': [
                {
                    'arn': 'string',
                    'deviceArn': 'string',
                    'labels': [
                        'string',
                    ],
                    'status': 'IN_USE'|'PREPARING'|'AVAILABLE'|'NOT_AVAILABLE',
                    'udid': 'string',
                    'instanceProfile': {
                        'arn': 'string',
                        'packageCleanup': True|False,
                        'excludeAppPackagesFromCleanup': [
                            'string',
                        ],
                        'rebootAfterUse': True|False,
                        'name': 'string',
                        'description': 'string'
                    }
                },
            ],
            'availability': 'TEMPORARY_NOT_AVAILABLE'|'BUSY'|'AVAILABLE'|'HIGHLY_AVAILABLE'
        }
    }
    
    
    :returns: 
    ANDROID
    IOS
    
    """
    pass

def get_device_instance(arn=None):
    """
    Returns information about a device instance that belongs to a private device fleet.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_device_instance(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the instance you\'re requesting information about.\n

    :rtype: dict
ReturnsResponse Syntax{
    'deviceInstance': {
        'arn': 'string',
        'deviceArn': 'string',
        'labels': [
            'string',
        ],
        'status': 'IN_USE'|'PREPARING'|'AVAILABLE'|'NOT_AVAILABLE',
        'udid': 'string',
        'instanceProfile': {
            'arn': 'string',
            'packageCleanup': True|False,
            'excludeAppPackagesFromCleanup': [
                'string',
            ],
            'rebootAfterUse': True|False,
            'name': 'string',
            'description': 'string'
        }
    }
}


Response Structure

(dict) --
deviceInstance (dict) --An object that contains information about your device instance.

arn (string) --The Amazon Resource Name (ARN) of the device instance.

deviceArn (string) --The ARN of the device.

labels (list) --An array of strings that describe the device instance.

(string) --


status (string) --The status of the device instance. Valid values are listed here.

udid (string) --Unique device identifier for the device instance.

instanceProfile (dict) --A object that contains information about the instance profile.

arn (string) --The Amazon Resource Name (ARN) of the instance profile.

packageCleanup (boolean) --When set to true , Device Farm removes app packages after a test run. The default value is false for private devices.

excludeAppPackagesFromCleanup (list) --An array of strings containing the list of app packages that should not be cleaned up from the device after a test run completes.
The list of packages is considered only if you set packageCleanup to true .

(string) --


rebootAfterUse (boolean) --When set to true , Device Farm reboots the instance after a test run. The default value is true .

name (string) --The name of the instance profile.

description (string) --The description of the instance profile.










Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.LimitExceededException
DeviceFarm.Client.exceptions.ServiceAccountException


    :return: {
        'deviceInstance': {
            'arn': 'string',
            'deviceArn': 'string',
            'labels': [
                'string',
            ],
            'status': 'IN_USE'|'PREPARING'|'AVAILABLE'|'NOT_AVAILABLE',
            'udid': 'string',
            'instanceProfile': {
                'arn': 'string',
                'packageCleanup': True|False,
                'excludeAppPackagesFromCleanup': [
                    'string',
                ],
                'rebootAfterUse': True|False,
                'name': 'string',
                'description': 'string'
            }
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_device_pool(arn=None):
    """
    Gets information about a device pool.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example returns information about a specific device pool, given a project ARN.
    Expected Output:
    
    :example: response = client.get_device_pool(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]\nThe device pool\'s ARN.\n

    :rtype: dict
ReturnsResponse Syntax{
    'devicePool': {
        'arn': 'string',
        'name': 'string',
        'description': 'string',
        'type': 'CURATED'|'PRIVATE',
        'rules': [
            {
                'attribute': 'ARN'|'PLATFORM'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'APPIUM_VERSION'|'INSTANCE_ARN'|'INSTANCE_LABELS'|'FLEET_TYPE'|'OS_VERSION'|'MODEL'|'AVAILABILITY',
                'operator': 'EQUALS'|'LESS_THAN'|'LESS_THAN_OR_EQUALS'|'GREATER_THAN'|'GREATER_THAN_OR_EQUALS'|'IN'|'NOT_IN'|'CONTAINS',
                'value': 'string'
            },
        ],
        'maxDevices': 123
    }
}


Response Structure

(dict) --Represents the result of a get device pool request.

devicePool (dict) --An object that contains information about the requested device pool.

arn (string) --The device pool\'s ARN.

name (string) --The device pool\'s name.

description (string) --The device pool\'s description.

type (string) --The device pool\'s type.
Allowed values include:

CURATED: A device pool that is created and managed by AWS Device Farm.
PRIVATE: A device pool that is created and managed by the device pool developer.


rules (list) --Information about the device pool\'s rules.

(dict) --Represents a condition for a device pool.

attribute (string) --The rule\'s stringified attribute. For example, specify the value as "\\"abc\\"" .
The supported operators for each attribute are provided in the following list.

APPIUM_VERSION
The Appium version for the test.
Supported operators: CONTAINS

ARN
The Amazon Resource Name (ARN) of the device (for example, arn:aws:devicefarm:us-west-2::device:12345Example .
Supported operators: EQUALS , IN , NOT_IN

AVAILABILITY
The current availability of the device. Valid values are AVAILABLE, HIGHLY_AVAILABLE, BUSY, or TEMPORARY_NOT_AVAILABLE.
Supported operators: EQUALS

FLEET_TYPE
The fleet type. Valid values are PUBLIC or PRIVATE.
Supported operators: EQUALS

FORM_FACTOR
The device form factor. Valid values are PHONE or TABLET.
Supported operators: EQUALS , IN , NOT_IN

INSTANCE_ARN
The Amazon Resource Name (ARN) of the device instance.
Supported operators: IN , NOT_IN

INSTANCE_LABELS
The label of the device instance.
Supported operators: CONTAINS

MANUFACTURER
The device manufacturer (for example, Apple).
Supported operators: EQUALS , IN , NOT_IN

MODEL
The device model, such as Apple iPad Air 2 or Google Pixel.
Supported operators: CONTAINS , EQUALS , IN , NOT_IN

OS_VERSION
The operating system version (for example, 10.3.2).
Supported operators: EQUALS , GREATER_THAN , GREATER_THAN_OR_EQUALS , IN , LESS_THAN , LESS_THAN_OR_EQUALS , NOT_IN

PLATFORM
The device platform. Valid values are ANDROID or IOS.
Supported operators: EQUALS , IN , NOT_IN

REMOTE_ACCESS_ENABLED
Whether the device is enabled for remote access. Valid values are TRUE or FALSE.
Supported operators: EQUALS

REMOTE_DEBUG_ENABLED
Whether the device is enabled for remote debugging. Valid values are TRUE or FALSE.
Supported operators: EQUALS
Because remote debugging is no longer supported , this filter is ignored.

operator (string) --Specifies how Device Farm compares the rule\'s attribute to the value. For the operators that are supported by each attribute, see the attribute descriptions.

value (string) --The rule\'s value.





maxDevices (integer) --The number of devices that Device Farm can add to your device pool. Device Farm adds devices that are available and meet the criteria that you assign for the rules parameter. Depending on how many devices meet these constraints, your device pool might contain fewer devices than the value for this parameter.
By specifying the maximum number of devices, you can control the costs that you incur by running tests.








Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.LimitExceededException
DeviceFarm.Client.exceptions.ServiceAccountException

Examples
The following example returns information about a specific device pool, given a project ARN.
response = client.get_device_pool(
    # You can obtain the project ARN by using the list-projects CLI command.
    arn='arn:aws:devicefarm:us-west-2:123456789101:project:EXAMPLE-GUID-123-456',
)

print(response)


Expected Output:
{
    'devicePool': {
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'devicePool': {
            'arn': 'string',
            'name': 'string',
            'description': 'string',
            'type': 'CURATED'|'PRIVATE',
            'rules': [
                {
                    'attribute': 'ARN'|'PLATFORM'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'APPIUM_VERSION'|'INSTANCE_ARN'|'INSTANCE_LABELS'|'FLEET_TYPE'|'OS_VERSION'|'MODEL'|'AVAILABILITY',
                    'operator': 'EQUALS'|'LESS_THAN'|'LESS_THAN_OR_EQUALS'|'GREATER_THAN'|'GREATER_THAN_OR_EQUALS'|'IN'|'NOT_IN'|'CONTAINS',
                    'value': 'string'
                },
            ],
            'maxDevices': 123
        }
    }
    
    
    :returns: 
    DeviceFarm.Client.exceptions.ArgumentException
    DeviceFarm.Client.exceptions.NotFoundException
    DeviceFarm.Client.exceptions.LimitExceededException
    DeviceFarm.Client.exceptions.ServiceAccountException
    
    """
    pass

def get_device_pool_compatibility(devicePoolArn=None, appArn=None, testType=None, test=None, configuration=None):
    """
    Gets information about compatibility with a device pool.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example returns information about the compatibility of a specific device pool, given its ARN.
    Expected Output:
    
    :example: response = client.get_device_pool_compatibility(
        devicePoolArn='string',
        appArn='string',
        testType='BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'WEB_PERFORMANCE_PROFILE'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_NODE'|'APPIUM_RUBY'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'APPIUM_WEB_NODE'|'APPIUM_WEB_RUBY'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI'|'REMOTE_ACCESS_RECORD'|'REMOTE_ACCESS_REPLAY',
        test={
            'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'WEB_PERFORMANCE_PROFILE'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_NODE'|'APPIUM_RUBY'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'APPIUM_WEB_NODE'|'APPIUM_WEB_RUBY'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI'|'REMOTE_ACCESS_RECORD'|'REMOTE_ACCESS_REPLAY',
            'testPackageArn': 'string',
            'testSpecArn': 'string',
            'filter': 'string',
            'parameters': {
                'string': 'string'
            }
        },
        configuration={
            'extraDataPackageArn': 'string',
            'networkProfileArn': 'string',
            'locale': 'string',
            'location': {
                'latitude': 123.0,
                'longitude': 123.0
            },
            'vpceConfigurationArns': [
                'string',
            ],
            'customerArtifactPaths': {
                'iosPaths': [
                    'string',
                ],
                'androidPaths': [
                    'string',
                ],
                'deviceHostPaths': [
                    'string',
                ]
            },
            'radios': {
                'wifi': True|False,
                'bluetooth': True|False,
                'nfc': True|False,
                'gps': True|False
            },
            'auxiliaryApps': [
                'string',
            ],
            'billingMethod': 'METERED'|'UNMETERED'
        }
    )
    
    
    :type devicePoolArn: string
    :param devicePoolArn: [REQUIRED]\nThe device pool\'s ARN.\n

    :type appArn: string
    :param appArn: The ARN of the app that is associated with the specified device pool.

    :type testType: string
    :param testType: The test type for the specified device pool.\nAllowed values include the following:\n\nBUILTIN_FUZZ.\nBUILTIN_EXPLORER. For Android, an app explorer that traverses an Android app, interacting with it and capturing screenshots at the same time.\nAPPIUM_JAVA_JUNIT.\nAPPIUM_JAVA_TESTNG.\nAPPIUM_PYTHON.\nAPPIUM_NODE.\nAPPIUM_RUBY.\nAPPIUM_WEB_JAVA_JUNIT.\nAPPIUM_WEB_JAVA_TESTNG.\nAPPIUM_WEB_PYTHON.\nAPPIUM_WEB_NODE.\nAPPIUM_WEB_RUBY.\nCALABASH.\nINSTRUMENTATION.\nUIAUTOMATION.\nUIAUTOMATOR.\nXCTEST.\nXCTEST_UI.\n\n

    :type test: dict
    :param test: Information about the uploaded test to be run against the device pool.\n\ntype (string) -- [REQUIRED]The test\'s type.\nMust be one of the following values:\n\nBUILTIN_FUZZ\nBUILTIN_EXPLORER. For Android, an app explorer that traverses an Android app, interacting with it and capturing screenshots at the same time.\nAPPIUM_JAVA_JUNIT\nAPPIUM_JAVA_TESTNG\nAPPIUM_PYTHON\nAPPIUM_NODE\nAPPIUM_RUBY\nAPPIUM_WEB_JAVA_JUNIT\nAPPIUM_WEB_JAVA_TESTNG\nAPPIUM_WEB_PYTHON\nAPPIUM_WEB_NODE\nAPPIUM_WEB_RUBY\nCALABASH\nINSTRUMENTATION\nUIAUTOMATION\nUIAUTOMATOR\nXCTEST\nXCTEST_UI\n\n\ntestPackageArn (string) --The ARN of the uploaded test to be run.\n\ntestSpecArn (string) --The ARN of the YAML-formatted test specification.\n\nfilter (string) --The test\'s filter.\n\nparameters (dict) --The test\'s parameters, such as test framework parameters and fixture settings. Parameters are represented by name-value pairs of strings.\nFor all tests:\n\napp_performance_monitoring : Performance monitoring is enabled by default. Set this parameter to false to disable it.\n\nFor Calabash tests:\n\nprofile: A cucumber profile (for example, my_profile_name ).\ntags: You can limit execution to features or scenarios that have (or don\'t have) certain tags (for example, @smoke or @smoke,~@wip).\n\nFor Appium tests (all types):\n\nappium_version: The Appium version. Currently supported values are 1.6.5 (and later), latest, and default.\nlatest runs the latest Appium version supported by Device Farm (1.9.1).\nFor default, Device Farm selects a compatible version of Appium for the device. The current behavior is to run 1.7.2 on Android devices and iOS 9 and earlier and 1.7.2 for iOS 10 and later.\nThis behavior is subject to change.\n\n\n\nFor fuzz tests (Android only):\n\nevent_count: The number of events, between 1 and 10000, that the UI fuzz test should perform.\nthrottle: The time, in ms, between 0 and 1000, that the UI fuzz test should wait between events.\nseed: A seed to use for randomizing the UI fuzz test. Using the same seed value between tests ensures identical event sequences.\n\nFor Explorer tests:\n\nusername: A user name to use if the Explorer encounters a login form. If not supplied, no user name is inserted.\npassword: A password to use if the Explorer encounters a login form. If not supplied, no password is inserted.\n\nFor Instrumentation:\n\nfilter: A test filter string. Examples:\nRunning a single test case: com.android.abc.Test1\nRunning a single test: com.android.abc.Test1#smoke\nRunning multiple tests: com.android.abc.Test1,com.android.abc.Test2\n\n\n\nFor XCTest and XCTestUI:\n\nfilter: A test filter string. Examples:\nRunning a single test class: LoginTests\nRunning a multiple test classes: LoginTests,SmokeTests\nRunning a single test: LoginTests/testValid\nRunning multiple tests: LoginTests/testValid,LoginTests/testInvalid\n\n\n\nFor UIAutomator:\n\nfilter: A test filter string. Examples:\nRunning a single test case: com.android.abc.Test1\nRunning a single test: com.android.abc.Test1#smoke\nRunning multiple tests: com.android.abc.Test1,com.android.abc.Test2\n\n\n\n\n(string) --\n(string) --\n\n\n\n\n\n

    :type configuration: dict
    :param configuration: An object that contains information about the settings for a run.\n\nextraDataPackageArn (string) --The ARN of the extra data for the run. The extra data is a .zip file that AWS Device Farm extracts to external data for Android or the app\'s sandbox for iOS.\n\nnetworkProfileArn (string) --Reserved for internal use.\n\nlocale (string) --Information about the locale that is used for the run.\n\nlocation (dict) --Information about the location that is used for the run.\n\nlatitude (float) -- [REQUIRED]The latitude.\n\nlongitude (float) -- [REQUIRED]The longitude.\n\n\n\nvpceConfigurationArns (list) --An array of ARNs for your VPC endpoint configurations.\n\n(string) --\n\n\ncustomerArtifactPaths (dict) --Input CustomerArtifactPaths object for the scheduled run configuration.\n\niosPaths (list) --Comma-separated list of paths on the iOS device where the artifacts generated by the customer\'s tests are pulled from.\n\n(string) --\n\n\nandroidPaths (list) --Comma-separated list of paths on the Android device where the artifacts generated by the customer\'s tests are pulled from.\n\n(string) --\n\n\ndeviceHostPaths (list) --Comma-separated list of paths in the test execution environment where the artifacts generated by the customer\'s tests are pulled from.\n\n(string) --\n\n\n\n\nradios (dict) --Information about the radio states for the run.\n\nwifi (boolean) --True if Wi-Fi is enabled at the beginning of the test. Otherwise, false.\n\nbluetooth (boolean) --True if Bluetooth is enabled at the beginning of the test. Otherwise, false.\n\nnfc (boolean) --True if NFC is enabled at the beginning of the test. Otherwise, false.\n\ngps (boolean) --True if GPS is enabled at the beginning of the test. Otherwise, false.\n\n\n\nauxiliaryApps (list) --A list of upload ARNs for app packages to be installed with your app.\n\n(string) --\n\n\nbillingMethod (string) --Specifies the billing method for a test run: metered or unmetered . If the parameter is not specified, the default value is metered .\n\nNote\nIf you have purchased unmetered device slots, you must set this parameter to unmetered to make use of them. Otherwise, your run counts against your metered time.\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'compatibleDevices': [
        {
            'device': {
                'arn': 'string',
                'name': 'string',
                'manufacturer': 'string',
                'model': 'string',
                'modelId': 'string',
                'formFactor': 'PHONE'|'TABLET',
                'platform': 'ANDROID'|'IOS',
                'os': 'string',
                'cpu': {
                    'frequency': 'string',
                    'architecture': 'string',
                    'clock': 123.0
                },
                'resolution': {
                    'width': 123,
                    'height': 123
                },
                'heapSize': 123,
                'memory': 123,
                'image': 'string',
                'carrier': 'string',
                'radio': 'string',
                'remoteAccessEnabled': True|False,
                'remoteDebugEnabled': True|False,
                'fleetType': 'string',
                'fleetName': 'string',
                'instances': [
                    {
                        'arn': 'string',
                        'deviceArn': 'string',
                        'labels': [
                            'string',
                        ],
                        'status': 'IN_USE'|'PREPARING'|'AVAILABLE'|'NOT_AVAILABLE',
                        'udid': 'string',
                        'instanceProfile': {
                            'arn': 'string',
                            'packageCleanup': True|False,
                            'excludeAppPackagesFromCleanup': [
                                'string',
                            ],
                            'rebootAfterUse': True|False,
                            'name': 'string',
                            'description': 'string'
                        }
                    },
                ],
                'availability': 'TEMPORARY_NOT_AVAILABLE'|'BUSY'|'AVAILABLE'|'HIGHLY_AVAILABLE'
            },
            'compatible': True|False,
            'incompatibilityMessages': [
                {
                    'message': 'string',
                    'type': 'ARN'|'PLATFORM'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'APPIUM_VERSION'|'INSTANCE_ARN'|'INSTANCE_LABELS'|'FLEET_TYPE'|'OS_VERSION'|'MODEL'|'AVAILABILITY'
                },
            ]
        },
    ],
    'incompatibleDevices': [
        {
            'device': {
                'arn': 'string',
                'name': 'string',
                'manufacturer': 'string',
                'model': 'string',
                'modelId': 'string',
                'formFactor': 'PHONE'|'TABLET',
                'platform': 'ANDROID'|'IOS',
                'os': 'string',
                'cpu': {
                    'frequency': 'string',
                    'architecture': 'string',
                    'clock': 123.0
                },
                'resolution': {
                    'width': 123,
                    'height': 123
                },
                'heapSize': 123,
                'memory': 123,
                'image': 'string',
                'carrier': 'string',
                'radio': 'string',
                'remoteAccessEnabled': True|False,
                'remoteDebugEnabled': True|False,
                'fleetType': 'string',
                'fleetName': 'string',
                'instances': [
                    {
                        'arn': 'string',
                        'deviceArn': 'string',
                        'labels': [
                            'string',
                        ],
                        'status': 'IN_USE'|'PREPARING'|'AVAILABLE'|'NOT_AVAILABLE',
                        'udid': 'string',
                        'instanceProfile': {
                            'arn': 'string',
                            'packageCleanup': True|False,
                            'excludeAppPackagesFromCleanup': [
                                'string',
                            ],
                            'rebootAfterUse': True|False,
                            'name': 'string',
                            'description': 'string'
                        }
                    },
                ],
                'availability': 'TEMPORARY_NOT_AVAILABLE'|'BUSY'|'AVAILABLE'|'HIGHLY_AVAILABLE'
            },
            'compatible': True|False,
            'incompatibilityMessages': [
                {
                    'message': 'string',
                    'type': 'ARN'|'PLATFORM'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'APPIUM_VERSION'|'INSTANCE_ARN'|'INSTANCE_LABELS'|'FLEET_TYPE'|'OS_VERSION'|'MODEL'|'AVAILABILITY'
                },
            ]
        },
    ]
}


Response Structure

(dict) --
Represents the result of describe device pool compatibility request.

compatibleDevices (list) --
Information about compatible devices.

(dict) --
Represents a device pool compatibility result.

device (dict) --
The device (phone or tablet) to return information about.

arn (string) --
The device\'s ARN.

name (string) --
The device\'s display name.

manufacturer (string) --
The device\'s manufacturer name.

model (string) --
The device\'s model name.

modelId (string) --
The device\'s model ID.

formFactor (string) --
The device\'s form factor.
Allowed values include:

PHONE
TABLET


platform (string) --
The device\'s platform.
Allowed values include:

ANDROID
IOS


os (string) --
The device\'s operating system type.

cpu (dict) --
Information about the device\'s CPU.

frequency (string) --
The CPU\'s frequency.

architecture (string) --
The CPU\'s architecture (for example, x86 or ARM).

clock (float) --
The clock speed of the device\'s CPU, expressed in hertz (Hz). For example, a 1.2 GHz CPU is expressed as 1200000000.



resolution (dict) --
The resolution of the device.

width (integer) --
The screen resolution\'s width, expressed in pixels.

height (integer) --
The screen resolution\'s height, expressed in pixels.



heapSize (integer) --
The device\'s heap size, expressed in bytes.

memory (integer) --
The device\'s total memory size, expressed in bytes.

image (string) --
The device\'s image name.

carrier (string) --
The device\'s carrier.

radio (string) --
The device\'s radio.

remoteAccessEnabled (boolean) --
Specifies whether remote access has been enabled for the specified device.

remoteDebugEnabled (boolean) --
This flag is set to true if remote debugging is enabled for the device.
Remote debugging is no longer supported .

fleetType (string) --
The type of fleet to which this device belongs. Possible values are PRIVATE and PUBLIC.

fleetName (string) --
The name of the fleet to which this device belongs.

instances (list) --
The instances that belong to this device.

(dict) --
Represents the device instance.

arn (string) --
The Amazon Resource Name (ARN) of the device instance.

deviceArn (string) --
The ARN of the device.

labels (list) --
An array of strings that describe the device instance.

(string) --


status (string) --
The status of the device instance. Valid values are listed here.

udid (string) --
Unique device identifier for the device instance.

instanceProfile (dict) --
A object that contains information about the instance profile.

arn (string) --
The Amazon Resource Name (ARN) of the instance profile.

packageCleanup (boolean) --
When set to true , Device Farm removes app packages after a test run. The default value is false for private devices.

excludeAppPackagesFromCleanup (list) --
An array of strings containing the list of app packages that should not be cleaned up from the device after a test run completes.
The list of packages is considered only if you set packageCleanup to true .

(string) --


rebootAfterUse (boolean) --
When set to true , Device Farm reboots the instance after a test run. The default value is true .

name (string) --
The name of the instance profile.

description (string) --
The description of the instance profile.







availability (string) --
Indicates how likely a device is available for a test run. Currently available in the  ListDevices and GetDevice API methods.



compatible (boolean) --
Whether the result was compatible with the device pool.

incompatibilityMessages (list) --
Information about the compatibility.

(dict) --
Represents information about incompatibility.

message (string) --
A message about the incompatibility.

type (string) --
The type of incompatibility.
Allowed values include:

ARN
FORM_FACTOR (for example, phone or tablet)
MANUFACTURER
PLATFORM (for example, Android or iOS)
REMOTE_ACCESS_ENABLED
APPIUM_VERSION










incompatibleDevices (list) --
Information about incompatible devices.

(dict) --
Represents a device pool compatibility result.

device (dict) --
The device (phone or tablet) to return information about.

arn (string) --
The device\'s ARN.

name (string) --
The device\'s display name.

manufacturer (string) --
The device\'s manufacturer name.

model (string) --
The device\'s model name.

modelId (string) --
The device\'s model ID.

formFactor (string) --
The device\'s form factor.
Allowed values include:

PHONE
TABLET


platform (string) --
The device\'s platform.
Allowed values include:

ANDROID
IOS


os (string) --
The device\'s operating system type.

cpu (dict) --
Information about the device\'s CPU.

frequency (string) --
The CPU\'s frequency.

architecture (string) --
The CPU\'s architecture (for example, x86 or ARM).

clock (float) --
The clock speed of the device\'s CPU, expressed in hertz (Hz). For example, a 1.2 GHz CPU is expressed as 1200000000.



resolution (dict) --
The resolution of the device.

width (integer) --
The screen resolution\'s width, expressed in pixels.

height (integer) --
The screen resolution\'s height, expressed in pixels.



heapSize (integer) --
The device\'s heap size, expressed in bytes.

memory (integer) --
The device\'s total memory size, expressed in bytes.

image (string) --
The device\'s image name.

carrier (string) --
The device\'s carrier.

radio (string) --
The device\'s radio.

remoteAccessEnabled (boolean) --
Specifies whether remote access has been enabled for the specified device.

remoteDebugEnabled (boolean) --
This flag is set to true if remote debugging is enabled for the device.
Remote debugging is no longer supported .

fleetType (string) --
The type of fleet to which this device belongs. Possible values are PRIVATE and PUBLIC.

fleetName (string) --
The name of the fleet to which this device belongs.

instances (list) --
The instances that belong to this device.

(dict) --
Represents the device instance.

arn (string) --
The Amazon Resource Name (ARN) of the device instance.

deviceArn (string) --
The ARN of the device.

labels (list) --
An array of strings that describe the device instance.

(string) --


status (string) --
The status of the device instance. Valid values are listed here.

udid (string) --
Unique device identifier for the device instance.

instanceProfile (dict) --
A object that contains information about the instance profile.

arn (string) --
The Amazon Resource Name (ARN) of the instance profile.

packageCleanup (boolean) --
When set to true , Device Farm removes app packages after a test run. The default value is false for private devices.

excludeAppPackagesFromCleanup (list) --
An array of strings containing the list of app packages that should not be cleaned up from the device after a test run completes.
The list of packages is considered only if you set packageCleanup to true .

(string) --


rebootAfterUse (boolean) --
When set to true , Device Farm reboots the instance after a test run. The default value is true .

name (string) --
The name of the instance profile.

description (string) --
The description of the instance profile.







availability (string) --
Indicates how likely a device is available for a test run. Currently available in the  ListDevices and GetDevice API methods.



compatible (boolean) --
Whether the result was compatible with the device pool.

incompatibilityMessages (list) --
Information about the compatibility.

(dict) --
Represents information about incompatibility.

message (string) --
A message about the incompatibility.

type (string) --
The type of incompatibility.
Allowed values include:

ARN
FORM_FACTOR (for example, phone or tablet)
MANUFACTURER
PLATFORM (for example, Android or iOS)
REMOTE_ACCESS_ENABLED
APPIUM_VERSION
















Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.LimitExceededException
DeviceFarm.Client.exceptions.ServiceAccountException

Examples
The following example returns information about the compatibility of a specific device pool, given its ARN.
response = client.get_device_pool_compatibility(
    appArn='arn:aws:devicefarm:us-west-2::app:123-456-EXAMPLE-GUID',
    # You can get the device pool ARN by using the list-device-pools CLI command.
    devicePoolArn='arn:aws:devicefarm:us-west-2::devicepool:123-456-EXAMPLE-GUID',
    testType='APPIUM_PYTHON',
)

print(response)


Expected Output:
{
    'compatibleDevices': [
    ],
    'incompatibleDevices': [
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'compatibleDevices': [
            {
                'device': {
                    'arn': 'string',
                    'name': 'string',
                    'manufacturer': 'string',
                    'model': 'string',
                    'modelId': 'string',
                    'formFactor': 'PHONE'|'TABLET',
                    'platform': 'ANDROID'|'IOS',
                    'os': 'string',
                    'cpu': {
                        'frequency': 'string',
                        'architecture': 'string',
                        'clock': 123.0
                    },
                    'resolution': {
                        'width': 123,
                        'height': 123
                    },
                    'heapSize': 123,
                    'memory': 123,
                    'image': 'string',
                    'carrier': 'string',
                    'radio': 'string',
                    'remoteAccessEnabled': True|False,
                    'remoteDebugEnabled': True|False,
                    'fleetType': 'string',
                    'fleetName': 'string',
                    'instances': [
                        {
                            'arn': 'string',
                            'deviceArn': 'string',
                            'labels': [
                                'string',
                            ],
                            'status': 'IN_USE'|'PREPARING'|'AVAILABLE'|'NOT_AVAILABLE',
                            'udid': 'string',
                            'instanceProfile': {
                                'arn': 'string',
                                'packageCleanup': True|False,
                                'excludeAppPackagesFromCleanup': [
                                    'string',
                                ],
                                'rebootAfterUse': True|False,
                                'name': 'string',
                                'description': 'string'
                            }
                        },
                    ],
                    'availability': 'TEMPORARY_NOT_AVAILABLE'|'BUSY'|'AVAILABLE'|'HIGHLY_AVAILABLE'
                },
                'compatible': True|False,
                'incompatibilityMessages': [
                    {
                        'message': 'string',
                        'type': 'ARN'|'PLATFORM'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'APPIUM_VERSION'|'INSTANCE_ARN'|'INSTANCE_LABELS'|'FLEET_TYPE'|'OS_VERSION'|'MODEL'|'AVAILABILITY'
                    },
                ]
            },
        ],
        'incompatibleDevices': [
            {
                'device': {
                    'arn': 'string',
                    'name': 'string',
                    'manufacturer': 'string',
                    'model': 'string',
                    'modelId': 'string',
                    'formFactor': 'PHONE'|'TABLET',
                    'platform': 'ANDROID'|'IOS',
                    'os': 'string',
                    'cpu': {
                        'frequency': 'string',
                        'architecture': 'string',
                        'clock': 123.0
                    },
                    'resolution': {
                        'width': 123,
                        'height': 123
                    },
                    'heapSize': 123,
                    'memory': 123,
                    'image': 'string',
                    'carrier': 'string',
                    'radio': 'string',
                    'remoteAccessEnabled': True|False,
                    'remoteDebugEnabled': True|False,
                    'fleetType': 'string',
                    'fleetName': 'string',
                    'instances': [
                        {
                            'arn': 'string',
                            'deviceArn': 'string',
                            'labels': [
                                'string',
                            ],
                            'status': 'IN_USE'|'PREPARING'|'AVAILABLE'|'NOT_AVAILABLE',
                            'udid': 'string',
                            'instanceProfile': {
                                'arn': 'string',
                                'packageCleanup': True|False,
                                'excludeAppPackagesFromCleanup': [
                                    'string',
                                ],
                                'rebootAfterUse': True|False,
                                'name': 'string',
                                'description': 'string'
                            }
                        },
                    ],
                    'availability': 'TEMPORARY_NOT_AVAILABLE'|'BUSY'|'AVAILABLE'|'HIGHLY_AVAILABLE'
                },
                'compatible': True|False,
                'incompatibilityMessages': [
                    {
                        'message': 'string',
                        'type': 'ARN'|'PLATFORM'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'APPIUM_VERSION'|'INSTANCE_ARN'|'INSTANCE_LABELS'|'FLEET_TYPE'|'OS_VERSION'|'MODEL'|'AVAILABILITY'
                    },
                ]
            },
        ]
    }
    
    
    :returns: 
    PHONE
    TABLET
    
    """
    pass

def get_instance_profile(arn=None):
    """
    Returns information about the specified instance profile.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_instance_profile(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]\nThe Amazon Resource Name (ARN) of an instance profile.\n

    :rtype: dict
ReturnsResponse Syntax{
    'instanceProfile': {
        'arn': 'string',
        'packageCleanup': True|False,
        'excludeAppPackagesFromCleanup': [
            'string',
        ],
        'rebootAfterUse': True|False,
        'name': 'string',
        'description': 'string'
    }
}


Response Structure

(dict) --
instanceProfile (dict) --An object that contains information about an instance profile.

arn (string) --The Amazon Resource Name (ARN) of the instance profile.

packageCleanup (boolean) --When set to true , Device Farm removes app packages after a test run. The default value is false for private devices.

excludeAppPackagesFromCleanup (list) --An array of strings containing the list of app packages that should not be cleaned up from the device after a test run completes.
The list of packages is considered only if you set packageCleanup to true .

(string) --


rebootAfterUse (boolean) --When set to true , Device Farm reboots the instance after a test run. The default value is true .

name (string) --The name of the instance profile.

description (string) --The description of the instance profile.








Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.LimitExceededException
DeviceFarm.Client.exceptions.ServiceAccountException


    :return: {
        'instanceProfile': {
            'arn': 'string',
            'packageCleanup': True|False,
            'excludeAppPackagesFromCleanup': [
                'string',
            ],
            'rebootAfterUse': True|False,
            'name': 'string',
            'description': 'string'
        }
    }
    
    
    :returns: 
    DeviceFarm.Client.exceptions.ArgumentException
    DeviceFarm.Client.exceptions.NotFoundException
    DeviceFarm.Client.exceptions.LimitExceededException
    DeviceFarm.Client.exceptions.ServiceAccountException
    
    """
    pass

def get_job(arn=None):
    """
    Gets information about a job.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example returns information about a specific job.
    Expected Output:
    
    :example: response = client.get_job(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]\nThe job\'s ARN.\n

    :rtype: dict
ReturnsResponse Syntax{
    'job': {
        'arn': 'string',
        'name': 'string',
        'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'WEB_PERFORMANCE_PROFILE'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_NODE'|'APPIUM_RUBY'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'APPIUM_WEB_NODE'|'APPIUM_WEB_RUBY'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI'|'REMOTE_ACCESS_RECORD'|'REMOTE_ACCESS_REPLAY',
        'created': datetime(2015, 1, 1),
        'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
        'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
        'started': datetime(2015, 1, 1),
        'stopped': datetime(2015, 1, 1),
        'counters': {
            'total': 123,
            'passed': 123,
            'failed': 123,
            'warned': 123,
            'errored': 123,
            'stopped': 123,
            'skipped': 123
        },
        'message': 'string',
        'device': {
            'arn': 'string',
            'name': 'string',
            'manufacturer': 'string',
            'model': 'string',
            'modelId': 'string',
            'formFactor': 'PHONE'|'TABLET',
            'platform': 'ANDROID'|'IOS',
            'os': 'string',
            'cpu': {
                'frequency': 'string',
                'architecture': 'string',
                'clock': 123.0
            },
            'resolution': {
                'width': 123,
                'height': 123
            },
            'heapSize': 123,
            'memory': 123,
            'image': 'string',
            'carrier': 'string',
            'radio': 'string',
            'remoteAccessEnabled': True|False,
            'remoteDebugEnabled': True|False,
            'fleetType': 'string',
            'fleetName': 'string',
            'instances': [
                {
                    'arn': 'string',
                    'deviceArn': 'string',
                    'labels': [
                        'string',
                    ],
                    'status': 'IN_USE'|'PREPARING'|'AVAILABLE'|'NOT_AVAILABLE',
                    'udid': 'string',
                    'instanceProfile': {
                        'arn': 'string',
                        'packageCleanup': True|False,
                        'excludeAppPackagesFromCleanup': [
                            'string',
                        ],
                        'rebootAfterUse': True|False,
                        'name': 'string',
                        'description': 'string'
                    }
                },
            ],
            'availability': 'TEMPORARY_NOT_AVAILABLE'|'BUSY'|'AVAILABLE'|'HIGHLY_AVAILABLE'
        },
        'instanceArn': 'string',
        'deviceMinutes': {
            'total': 123.0,
            'metered': 123.0,
            'unmetered': 123.0
        },
        'videoEndpoint': 'string',
        'videoCapture': True|False
    }
}


Response Structure

(dict) --Represents the result of a get job request.

job (dict) --An object that contains information about the requested job.

arn (string) --The job\'s ARN.

name (string) --The job\'s name.

type (string) --The job\'s type.
Allowed values include the following:

BUILTIN_FUZZ
BUILTIN_EXPLORER. For Android, an app explorer that traverses an Android app, interacting with it and capturing screenshots at the same time.
APPIUM_JAVA_JUNIT
APPIUM_JAVA_TESTNG
APPIUM_PYTHON
APPIUM_NODE
APPIUM_RUBY
APPIUM_WEB_JAVA_JUNIT
APPIUM_WEB_JAVA_TESTNG
APPIUM_WEB_PYTHON
APPIUM_WEB_NODE
APPIUM_WEB_RUBY
CALABASH
INSTRUMENTATION
UIAUTOMATION
UIAUTOMATOR
XCTEST
XCTEST_UI


created (datetime) --When the job was created.

status (string) --The job\'s status.
Allowed values include:

PENDING
PENDING_CONCURRENCY
PENDING_DEVICE
PROCESSING
SCHEDULING
PREPARING
RUNNING
COMPLETED
STOPPING


result (string) --The job\'s result.
Allowed values include:

PENDING
PASSED
WARNED
FAILED
SKIPPED
ERRORED
STOPPED


started (datetime) --The job\'s start time.

stopped (datetime) --The job\'s stop time.

counters (dict) --The job\'s result counters.

total (integer) --The total number of entities.

passed (integer) --The number of passed entities.

failed (integer) --The number of failed entities.

warned (integer) --The number of warned entities.

errored (integer) --The number of errored entities.

stopped (integer) --The number of stopped entities.

skipped (integer) --The number of skipped entities.



message (string) --A message about the job\'s result.

device (dict) --The device (phone or tablet).

arn (string) --The device\'s ARN.

name (string) --The device\'s display name.

manufacturer (string) --The device\'s manufacturer name.

model (string) --The device\'s model name.

modelId (string) --The device\'s model ID.

formFactor (string) --The device\'s form factor.
Allowed values include:

PHONE
TABLET


platform (string) --The device\'s platform.
Allowed values include:

ANDROID
IOS


os (string) --The device\'s operating system type.

cpu (dict) --Information about the device\'s CPU.

frequency (string) --The CPU\'s frequency.

architecture (string) --The CPU\'s architecture (for example, x86 or ARM).

clock (float) --The clock speed of the device\'s CPU, expressed in hertz (Hz). For example, a 1.2 GHz CPU is expressed as 1200000000.



resolution (dict) --The resolution of the device.

width (integer) --The screen resolution\'s width, expressed in pixels.

height (integer) --The screen resolution\'s height, expressed in pixels.



heapSize (integer) --The device\'s heap size, expressed in bytes.

memory (integer) --The device\'s total memory size, expressed in bytes.

image (string) --The device\'s image name.

carrier (string) --The device\'s carrier.

radio (string) --The device\'s radio.

remoteAccessEnabled (boolean) --Specifies whether remote access has been enabled for the specified device.

remoteDebugEnabled (boolean) --This flag is set to true if remote debugging is enabled for the device.
Remote debugging is no longer supported .

fleetType (string) --The type of fleet to which this device belongs. Possible values are PRIVATE and PUBLIC.

fleetName (string) --The name of the fleet to which this device belongs.

instances (list) --The instances that belong to this device.

(dict) --Represents the device instance.

arn (string) --The Amazon Resource Name (ARN) of the device instance.

deviceArn (string) --The ARN of the device.

labels (list) --An array of strings that describe the device instance.

(string) --


status (string) --The status of the device instance. Valid values are listed here.

udid (string) --Unique device identifier for the device instance.

instanceProfile (dict) --A object that contains information about the instance profile.

arn (string) --The Amazon Resource Name (ARN) of the instance profile.

packageCleanup (boolean) --When set to true , Device Farm removes app packages after a test run. The default value is false for private devices.

excludeAppPackagesFromCleanup (list) --An array of strings containing the list of app packages that should not be cleaned up from the device after a test run completes.
The list of packages is considered only if you set packageCleanup to true .

(string) --


rebootAfterUse (boolean) --When set to true , Device Farm reboots the instance after a test run. The default value is true .

name (string) --The name of the instance profile.

description (string) --The description of the instance profile.







availability (string) --Indicates how likely a device is available for a test run. Currently available in the  ListDevices and GetDevice API methods.



instanceArn (string) --The ARN of the instance.

deviceMinutes (dict) --Represents the total (metered or unmetered) minutes used by the job.

total (float) --When specified, represents the total minutes used by the resource to run tests.

metered (float) --When specified, represents only the sum of metered minutes used by the resource to run tests.

unmetered (float) --When specified, represents only the sum of unmetered minutes used by the resource to run tests.



videoEndpoint (string) --The endpoint for streaming device video.

videoCapture (boolean) --This value is set to true if video capture is enabled. Otherwise, it is set to false.








Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.LimitExceededException
DeviceFarm.Client.exceptions.ServiceAccountException

Examples
The following example returns information about a specific job.
response = client.get_job(
    # You can get the job ARN by using the list-jobs CLI command.
    arn='arn:aws:devicefarm:us-west-2::job:123-456-EXAMPLE-GUID',
)

print(response)


Expected Output:
{
    'job': {
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'job': {
            'arn': 'string',
            'name': 'string',
            'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'WEB_PERFORMANCE_PROFILE'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_NODE'|'APPIUM_RUBY'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'APPIUM_WEB_NODE'|'APPIUM_WEB_RUBY'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI'|'REMOTE_ACCESS_RECORD'|'REMOTE_ACCESS_REPLAY',
            'created': datetime(2015, 1, 1),
            'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
            'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
            'started': datetime(2015, 1, 1),
            'stopped': datetime(2015, 1, 1),
            'counters': {
                'total': 123,
                'passed': 123,
                'failed': 123,
                'warned': 123,
                'errored': 123,
                'stopped': 123,
                'skipped': 123
            },
            'message': 'string',
            'device': {
                'arn': 'string',
                'name': 'string',
                'manufacturer': 'string',
                'model': 'string',
                'modelId': 'string',
                'formFactor': 'PHONE'|'TABLET',
                'platform': 'ANDROID'|'IOS',
                'os': 'string',
                'cpu': {
                    'frequency': 'string',
                    'architecture': 'string',
                    'clock': 123.0
                },
                'resolution': {
                    'width': 123,
                    'height': 123
                },
                'heapSize': 123,
                'memory': 123,
                'image': 'string',
                'carrier': 'string',
                'radio': 'string',
                'remoteAccessEnabled': True|False,
                'remoteDebugEnabled': True|False,
                'fleetType': 'string',
                'fleetName': 'string',
                'instances': [
                    {
                        'arn': 'string',
                        'deviceArn': 'string',
                        'labels': [
                            'string',
                        ],
                        'status': 'IN_USE'|'PREPARING'|'AVAILABLE'|'NOT_AVAILABLE',
                        'udid': 'string',
                        'instanceProfile': {
                            'arn': 'string',
                            'packageCleanup': True|False,
                            'excludeAppPackagesFromCleanup': [
                                'string',
                            ],
                            'rebootAfterUse': True|False,
                            'name': 'string',
                            'description': 'string'
                        }
                    },
                ],
                'availability': 'TEMPORARY_NOT_AVAILABLE'|'BUSY'|'AVAILABLE'|'HIGHLY_AVAILABLE'
            },
            'instanceArn': 'string',
            'deviceMinutes': {
                'total': 123.0,
                'metered': 123.0,
                'unmetered': 123.0
            },
            'videoEndpoint': 'string',
            'videoCapture': True|False
        }
    }
    
    
    :returns: 
    PENDING
    PENDING_CONCURRENCY
    PENDING_DEVICE
    PROCESSING
    SCHEDULING
    PREPARING
    RUNNING
    COMPLETED
    STOPPING
    
    """
    pass

def get_network_profile(arn=None):
    """
    Returns information about a network profile.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_network_profile(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]\nThe ARN of the network profile to return information about.\n

    :rtype: dict
ReturnsResponse Syntax{
    'networkProfile': {
        'arn': 'string',
        'name': 'string',
        'description': 'string',
        'type': 'CURATED'|'PRIVATE',
        'uplinkBandwidthBits': 123,
        'downlinkBandwidthBits': 123,
        'uplinkDelayMs': 123,
        'downlinkDelayMs': 123,
        'uplinkJitterMs': 123,
        'downlinkJitterMs': 123,
        'uplinkLossPercent': 123,
        'downlinkLossPercent': 123
    }
}


Response Structure

(dict) --
networkProfile (dict) --The network profile.

arn (string) --The Amazon Resource Name (ARN) of the network profile.

name (string) --The name of the network profile.

description (string) --The description of the network profile.

type (string) --The type of network profile. Valid values are listed here.

uplinkBandwidthBits (integer) --The data throughput rate in bits per second, as an integer from 0 to 104857600.

downlinkBandwidthBits (integer) --The data throughput rate in bits per second, as an integer from 0 to 104857600.

uplinkDelayMs (integer) --Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.

downlinkDelayMs (integer) --Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.

uplinkJitterMs (integer) --Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.

downlinkJitterMs (integer) --Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.

uplinkLossPercent (integer) --Proportion of transmitted packets that fail to arrive from 0 to 100 percent.

downlinkLossPercent (integer) --Proportion of received packets that fail to arrive from 0 to 100 percent.








Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.LimitExceededException
DeviceFarm.Client.exceptions.ServiceAccountException


    :return: {
        'networkProfile': {
            'arn': 'string',
            'name': 'string',
            'description': 'string',
            'type': 'CURATED'|'PRIVATE',
            'uplinkBandwidthBits': 123,
            'downlinkBandwidthBits': 123,
            'uplinkDelayMs': 123,
            'downlinkDelayMs': 123,
            'uplinkJitterMs': 123,
            'downlinkJitterMs': 123,
            'uplinkLossPercent': 123,
            'downlinkLossPercent': 123
        }
    }
    
    
    """
    pass

def get_offering_status(nextToken=None):
    """
    Gets the current status and future status of all offerings purchased by an AWS account. The response indicates how many offerings are currently available and the offerings that will be available in the next period. The API returns a NotEligible error if the user is not permitted to invoke the operation. If you must be able to invoke this operation, contact aws-devicefarm-support@amazon.com .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example returns information about Device Farm offerings available to your account.
    Expected Output:
    
    :example: response = client.get_offering_status(
        nextToken='string'
    )
    
    
    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :rtype: dict
ReturnsResponse Syntax{
    'current': {
        'string': {
            'type': 'PURCHASE'|'RENEW'|'SYSTEM',
            'offering': {
                'id': 'string',
                'description': 'string',
                'type': 'RECURRING',
                'platform': 'ANDROID'|'IOS',
                'recurringCharges': [
                    {
                        'cost': {
                            'amount': 123.0,
                            'currencyCode': 'USD'
                        },
                        'frequency': 'MONTHLY'
                    },
                ]
            },
            'quantity': 123,
            'effectiveOn': datetime(2015, 1, 1)
        }
    },
    'nextPeriod': {
        'string': {
            'type': 'PURCHASE'|'RENEW'|'SYSTEM',
            'offering': {
                'id': 'string',
                'description': 'string',
                'type': 'RECURRING',
                'platform': 'ANDROID'|'IOS',
                'recurringCharges': [
                    {
                        'cost': {
                            'amount': 123.0,
                            'currencyCode': 'USD'
                        },
                        'frequency': 'MONTHLY'
                    },
                ]
            },
            'quantity': 123,
            'effectiveOn': datetime(2015, 1, 1)
        }
    },
    'nextToken': 'string'
}


Response Structure

(dict) --Returns the status result for a device offering.

current (dict) --When specified, gets the offering status for the current period.

(string) --
(dict) --The status of the offering.

type (string) --The type specified for the offering status.

offering (dict) --Represents the metadata of an offering status.

id (string) --The ID that corresponds to a device offering.

description (string) --A string that describes the offering.

type (string) --The type of offering (for example, RECURRING ) for a device.

platform (string) --The platform of the device (for example, ANDROID or IOS ).

recurringCharges (list) --Specifies whether there are recurring charges for the offering.

(dict) --Specifies whether charges for devices are recurring.

cost (dict) --The cost of the recurring charge.

amount (float) --The numerical amount of an offering or transaction.

currencyCode (string) --The currency code of a monetary amount. For example, USD means U.S. dollars.



frequency (string) --The frequency in which charges recur.







quantity (integer) --The number of available devices in the offering.

effectiveOn (datetime) --The date on which the offering is effective.







nextPeriod (dict) --When specified, gets the offering status for the next period.

(string) --
(dict) --The status of the offering.

type (string) --The type specified for the offering status.

offering (dict) --Represents the metadata of an offering status.

id (string) --The ID that corresponds to a device offering.

description (string) --A string that describes the offering.

type (string) --The type of offering (for example, RECURRING ) for a device.

platform (string) --The platform of the device (for example, ANDROID or IOS ).

recurringCharges (list) --Specifies whether there are recurring charges for the offering.

(dict) --Specifies whether charges for devices are recurring.

cost (dict) --The cost of the recurring charge.

amount (float) --The numerical amount of an offering or transaction.

currencyCode (string) --The currency code of a monetary amount. For example, USD means U.S. dollars.



frequency (string) --The frequency in which charges recur.







quantity (integer) --The number of available devices in the offering.

effectiveOn (datetime) --The date on which the offering is effective.







nextToken (string) --An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.






Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.NotEligibleException
DeviceFarm.Client.exceptions.LimitExceededException
DeviceFarm.Client.exceptions.ServiceAccountException

Examples
The following example returns information about Device Farm offerings available to your account.
response = client.get_offering_status(
    # A dynamically generated value, used for paginating results.
    nextToken='RW5DdDJkMWYwZjM2MzM2VHVpOHJIUXlDUXlhc2QzRGViYnc9SEXAMPLE=',
)

print(response)


Expected Output:
{
    'current': {
        'D68B3C05-1BA6-4360-BC69-12345EXAMPLE': {
            'offering': {
                'type': 'RECURRING',
                'description': 'Android Remote Access Unmetered Device Slot',
                'id': 'D68B3C05-1BA6-4360-BC69-12345EXAMPLE',
                'platform': 'ANDROID',
            },
            'quantity': 1,
        },
    },
    'nextPeriod': {
        'D68B3C05-1BA6-4360-BC69-12345EXAMPLE': {
            'effectiveOn': datetime(2016, 9, 1, 0, 0, 0, 3, 245, 0),
            'offering': {
                'type': 'RECURRING',
                'description': 'Android Remote Access Unmetered Device Slot',
                'id': 'D68B3C05-1BA6-4360-BC69-12345EXAMPLE',
                'platform': 'ANDROID',
            },
            'quantity': 1,
        },
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'current': {
            'string': {
                'type': 'PURCHASE'|'RENEW'|'SYSTEM',
                'offering': {
                    'id': 'string',
                    'description': 'string',
                    'type': 'RECURRING',
                    'platform': 'ANDROID'|'IOS',
                    'recurringCharges': [
                        {
                            'cost': {
                                'amount': 123.0,
                                'currencyCode': 'USD'
                            },
                            'frequency': 'MONTHLY'
                        },
                    ]
                },
                'quantity': 123,
                'effectiveOn': datetime(2015, 1, 1)
            }
        },
        'nextPeriod': {
            'string': {
                'type': 'PURCHASE'|'RENEW'|'SYSTEM',
                'offering': {
                    'id': 'string',
                    'description': 'string',
                    'type': 'RECURRING',
                    'platform': 'ANDROID'|'IOS',
                    'recurringCharges': [
                        {
                            'cost': {
                                'amount': 123.0,
                                'currencyCode': 'USD'
                            },
                            'frequency': 'MONTHLY'
                        },
                    ]
                },
                'quantity': 123,
                'effectiveOn': datetime(2015, 1, 1)
            }
        },
        'nextToken': 'string'
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

def get_project(arn=None):
    """
    Gets information about a project.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example gets information about a specific project.
    Expected Output:
    
    :example: response = client.get_project(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]\nThe project\'s ARN.\n

    :rtype: dict
ReturnsResponse Syntax{
    'project': {
        'arn': 'string',
        'name': 'string',
        'defaultJobTimeoutMinutes': 123,
        'created': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --Represents the result of a get project request.

project (dict) --The project to get information about.

arn (string) --The project\'s ARN.

name (string) --The project\'s name.

defaultJobTimeoutMinutes (integer) --The default number of minutes (at the project level) a test run executes before it times out. The default value is 150 minutes.

created (datetime) --When the project was created.








Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.LimitExceededException
DeviceFarm.Client.exceptions.ServiceAccountException

Examples
The following example gets information about a specific project.
response = client.get_project(
    # You can get the project ARN by using the list-projects CLI command.
    arn='arn:aws:devicefarm:us-west-2:123456789101:project:5e01a8c7-c861-4c0a-b1d5-12345EXAMPLE',
)

print(response)


Expected Output:
{
    'project': {
        'name': 'My Project',
        'arn': 'arn:aws:devicefarm:us-west-2:123456789101:project:5e01a8c7-c861-4c0a-b1d5-12345EXAMPLE',
        'created': datetime(2016, 8, 31, 16, 28, 59, 2, 244, 0),
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'project': {
            'arn': 'string',
            'name': 'string',
            'defaultJobTimeoutMinutes': 123,
            'created': datetime(2015, 1, 1)
        }
    }
    
    
    """
    pass

def get_remote_access_session(arn=None):
    """
    Returns a link to a currently running remote access session.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example gets a specific remote access session.
    Expected Output:
    
    :example: response = client.get_remote_access_session(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the remote access session about which you want to get session information.\n

    :rtype: dict
ReturnsResponse Syntax{
    'remoteAccessSession': {
        'arn': 'string',
        'name': 'string',
        'created': datetime(2015, 1, 1),
        'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
        'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
        'message': 'string',
        'started': datetime(2015, 1, 1),
        'stopped': datetime(2015, 1, 1),
        'device': {
            'arn': 'string',
            'name': 'string',
            'manufacturer': 'string',
            'model': 'string',
            'modelId': 'string',
            'formFactor': 'PHONE'|'TABLET',
            'platform': 'ANDROID'|'IOS',
            'os': 'string',
            'cpu': {
                'frequency': 'string',
                'architecture': 'string',
                'clock': 123.0
            },
            'resolution': {
                'width': 123,
                'height': 123
            },
            'heapSize': 123,
            'memory': 123,
            'image': 'string',
            'carrier': 'string',
            'radio': 'string',
            'remoteAccessEnabled': True|False,
            'remoteDebugEnabled': True|False,
            'fleetType': 'string',
            'fleetName': 'string',
            'instances': [
                {
                    'arn': 'string',
                    'deviceArn': 'string',
                    'labels': [
                        'string',
                    ],
                    'status': 'IN_USE'|'PREPARING'|'AVAILABLE'|'NOT_AVAILABLE',
                    'udid': 'string',
                    'instanceProfile': {
                        'arn': 'string',
                        'packageCleanup': True|False,
                        'excludeAppPackagesFromCleanup': [
                            'string',
                        ],
                        'rebootAfterUse': True|False,
                        'name': 'string',
                        'description': 'string'
                    }
                },
            ],
            'availability': 'TEMPORARY_NOT_AVAILABLE'|'BUSY'|'AVAILABLE'|'HIGHLY_AVAILABLE'
        },
        'instanceArn': 'string',
        'remoteDebugEnabled': True|False,
        'remoteRecordEnabled': True|False,
        'remoteRecordAppArn': 'string',
        'hostAddress': 'string',
        'clientId': 'string',
        'billingMethod': 'METERED'|'UNMETERED',
        'deviceMinutes': {
            'total': 123.0,
            'metered': 123.0,
            'unmetered': 123.0
        },
        'endpoint': 'string',
        'deviceUdid': 'string',
        'interactionMode': 'INTERACTIVE'|'NO_VIDEO'|'VIDEO_ONLY',
        'skipAppResign': True|False
    }
}


Response Structure

(dict) --Represents the response from the server that lists detailed information about the remote access session.

remoteAccessSession (dict) --A container that lists detailed information about the remote access session.

arn (string) --The Amazon Resource Name (ARN) of the remote access session.

name (string) --The name of the remote access session.

created (datetime) --The date and time the remote access session was created.

status (string) --The status of the remote access session. Can be any of the following:

PENDING.
PENDING_CONCURRENCY.
PENDING_DEVICE.
PROCESSING.
SCHEDULING.
PREPARING.
RUNNING.
COMPLETED.
STOPPING.


result (string) --The result of the remote access session. Can be any of the following:

PENDING.
PASSED.
WARNED.
FAILED.
SKIPPED.
ERRORED.
STOPPED.


message (string) --A message about the remote access session.

started (datetime) --The date and time the remote access session was started.

stopped (datetime) --The date and time the remote access session was stopped.

device (dict) --The device (phone or tablet) used in the remote access session.

arn (string) --The device\'s ARN.

name (string) --The device\'s display name.

manufacturer (string) --The device\'s manufacturer name.

model (string) --The device\'s model name.

modelId (string) --The device\'s model ID.

formFactor (string) --The device\'s form factor.
Allowed values include:

PHONE
TABLET


platform (string) --The device\'s platform.
Allowed values include:

ANDROID
IOS


os (string) --The device\'s operating system type.

cpu (dict) --Information about the device\'s CPU.

frequency (string) --The CPU\'s frequency.

architecture (string) --The CPU\'s architecture (for example, x86 or ARM).

clock (float) --The clock speed of the device\'s CPU, expressed in hertz (Hz). For example, a 1.2 GHz CPU is expressed as 1200000000.



resolution (dict) --The resolution of the device.

width (integer) --The screen resolution\'s width, expressed in pixels.

height (integer) --The screen resolution\'s height, expressed in pixels.



heapSize (integer) --The device\'s heap size, expressed in bytes.

memory (integer) --The device\'s total memory size, expressed in bytes.

image (string) --The device\'s image name.

carrier (string) --The device\'s carrier.

radio (string) --The device\'s radio.

remoteAccessEnabled (boolean) --Specifies whether remote access has been enabled for the specified device.

remoteDebugEnabled (boolean) --This flag is set to true if remote debugging is enabled for the device.
Remote debugging is no longer supported .

fleetType (string) --The type of fleet to which this device belongs. Possible values are PRIVATE and PUBLIC.

fleetName (string) --The name of the fleet to which this device belongs.

instances (list) --The instances that belong to this device.

(dict) --Represents the device instance.

arn (string) --The Amazon Resource Name (ARN) of the device instance.

deviceArn (string) --The ARN of the device.

labels (list) --An array of strings that describe the device instance.

(string) --


status (string) --The status of the device instance. Valid values are listed here.

udid (string) --Unique device identifier for the device instance.

instanceProfile (dict) --A object that contains information about the instance profile.

arn (string) --The Amazon Resource Name (ARN) of the instance profile.

packageCleanup (boolean) --When set to true , Device Farm removes app packages after a test run. The default value is false for private devices.

excludeAppPackagesFromCleanup (list) --An array of strings containing the list of app packages that should not be cleaned up from the device after a test run completes.
The list of packages is considered only if you set packageCleanup to true .

(string) --


rebootAfterUse (boolean) --When set to true , Device Farm reboots the instance after a test run. The default value is true .

name (string) --The name of the instance profile.

description (string) --The description of the instance profile.







availability (string) --Indicates how likely a device is available for a test run. Currently available in the  ListDevices and GetDevice API methods.



instanceArn (string) --The ARN of the instance.

remoteDebugEnabled (boolean) --This flag is set to true if remote debugging is enabled for the remote access session.
Remote debugging is no longer supported .

remoteRecordEnabled (boolean) --This flag is set to true if remote recording is enabled for the remote access session.

remoteRecordAppArn (string) --The ARN for the app to be recorded in the remote access session.

hostAddress (string) --IP address of the EC2 host where you need to connect to remotely debug devices. Only returned if remote debugging is enabled for the remote access session.
Remote debugging is no longer supported .

clientId (string) --Unique identifier of your client for the remote access session. Only returned if remote debugging is enabled for the remote access session.
Remote debugging is no longer supported .

billingMethod (string) --The billing method of the remote access session. Possible values include METERED or UNMETERED . For more information about metered devices, see AWS Device Farm terminology .

deviceMinutes (dict) --The number of minutes a device is used in a remote access session (including setup and teardown minutes).

total (float) --When specified, represents the total minutes used by the resource to run tests.

metered (float) --When specified, represents only the sum of metered minutes used by the resource to run tests.

unmetered (float) --When specified, represents only the sum of unmetered minutes used by the resource to run tests.



endpoint (string) --The endpoint for the remote access sesssion.

deviceUdid (string) --Unique device identifier for the remote device. Only returned if remote debugging is enabled for the remote access session.
Remote debugging is no longer supported .

interactionMode (string) --The interaction mode of the remote access session. Valid values are:

INTERACTIVE: You can interact with the iOS device by viewing, touching, and rotating the screen. You cannot run XCUITest framework-based tests in this mode.
NO_VIDEO: You are connected to the device, but cannot interact with it or view the screen. This mode has the fastest test execution speed. You can run XCUITest framework-based tests in this mode.
VIDEO_ONLY: You can view the screen, but cannot touch or rotate it. You can run XCUITest framework-based tests and watch the screen in this mode.


skipAppResign (boolean) --When set to true , for private devices, Device Farm does not sign your app again. For public devices, Device Farm always signs your apps again.
For more information about how Device Farm re-signs your apps, see Do you modify my app? in the AWS Device Farm FAQs .








Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.LimitExceededException
DeviceFarm.Client.exceptions.ServiceAccountException

Examples
The following example gets a specific remote access session.
response = client.get_remote_access_session(
    # You can get the remote access session ARN by using the list-remote-access-sessions CLI command.
    arn='arn:aws:devicefarm:us-west-2:123456789101:session:EXAMPLE-GUID-123-456',
)

print(response)


Expected Output:
{
    'remoteAccessSession': {
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'remoteAccessSession': {
            'arn': 'string',
            'name': 'string',
            'created': datetime(2015, 1, 1),
            'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
            'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
            'message': 'string',
            'started': datetime(2015, 1, 1),
            'stopped': datetime(2015, 1, 1),
            'device': {
                'arn': 'string',
                'name': 'string',
                'manufacturer': 'string',
                'model': 'string',
                'modelId': 'string',
                'formFactor': 'PHONE'|'TABLET',
                'platform': 'ANDROID'|'IOS',
                'os': 'string',
                'cpu': {
                    'frequency': 'string',
                    'architecture': 'string',
                    'clock': 123.0
                },
                'resolution': {
                    'width': 123,
                    'height': 123
                },
                'heapSize': 123,
                'memory': 123,
                'image': 'string',
                'carrier': 'string',
                'radio': 'string',
                'remoteAccessEnabled': True|False,
                'remoteDebugEnabled': True|False,
                'fleetType': 'string',
                'fleetName': 'string',
                'instances': [
                    {
                        'arn': 'string',
                        'deviceArn': 'string',
                        'labels': [
                            'string',
                        ],
                        'status': 'IN_USE'|'PREPARING'|'AVAILABLE'|'NOT_AVAILABLE',
                        'udid': 'string',
                        'instanceProfile': {
                            'arn': 'string',
                            'packageCleanup': True|False,
                            'excludeAppPackagesFromCleanup': [
                                'string',
                            ],
                            'rebootAfterUse': True|False,
                            'name': 'string',
                            'description': 'string'
                        }
                    },
                ],
                'availability': 'TEMPORARY_NOT_AVAILABLE'|'BUSY'|'AVAILABLE'|'HIGHLY_AVAILABLE'
            },
            'instanceArn': 'string',
            'remoteDebugEnabled': True|False,
            'remoteRecordEnabled': True|False,
            'remoteRecordAppArn': 'string',
            'hostAddress': 'string',
            'clientId': 'string',
            'billingMethod': 'METERED'|'UNMETERED',
            'deviceMinutes': {
                'total': 123.0,
                'metered': 123.0,
                'unmetered': 123.0
            },
            'endpoint': 'string',
            'deviceUdid': 'string',
            'interactionMode': 'INTERACTIVE'|'NO_VIDEO'|'VIDEO_ONLY',
            'skipAppResign': True|False
        }
    }
    
    
    :returns: 
    PENDING.
    PASSED.
    WARNED.
    FAILED.
    SKIPPED.
    ERRORED.
    STOPPED.
    
    """
    pass

def get_run(arn=None):
    """
    Gets information about a run.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example gets information about a specific test run.
    Expected Output:
    
    :example: response = client.get_run(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]\nThe run\'s ARN.\n

    :rtype: dict
ReturnsResponse Syntax{
    'run': {
        'arn': 'string',
        'name': 'string',
        'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'WEB_PERFORMANCE_PROFILE'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_NODE'|'APPIUM_RUBY'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'APPIUM_WEB_NODE'|'APPIUM_WEB_RUBY'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI'|'REMOTE_ACCESS_RECORD'|'REMOTE_ACCESS_REPLAY',
        'platform': 'ANDROID'|'IOS',
        'created': datetime(2015, 1, 1),
        'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
        'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
        'started': datetime(2015, 1, 1),
        'stopped': datetime(2015, 1, 1),
        'counters': {
            'total': 123,
            'passed': 123,
            'failed': 123,
            'warned': 123,
            'errored': 123,
            'stopped': 123,
            'skipped': 123
        },
        'message': 'string',
        'totalJobs': 123,
        'completedJobs': 123,
        'billingMethod': 'METERED'|'UNMETERED',
        'deviceMinutes': {
            'total': 123.0,
            'metered': 123.0,
            'unmetered': 123.0
        },
        'networkProfile': {
            'arn': 'string',
            'name': 'string',
            'description': 'string',
            'type': 'CURATED'|'PRIVATE',
            'uplinkBandwidthBits': 123,
            'downlinkBandwidthBits': 123,
            'uplinkDelayMs': 123,
            'downlinkDelayMs': 123,
            'uplinkJitterMs': 123,
            'downlinkJitterMs': 123,
            'uplinkLossPercent': 123,
            'downlinkLossPercent': 123
        },
        'parsingResultUrl': 'string',
        'resultCode': 'PARSING_FAILED'|'VPC_ENDPOINT_SETUP_FAILED',
        'seed': 123,
        'appUpload': 'string',
        'eventCount': 123,
        'jobTimeoutMinutes': 123,
        'devicePoolArn': 'string',
        'locale': 'string',
        'radios': {
            'wifi': True|False,
            'bluetooth': True|False,
            'nfc': True|False,
            'gps': True|False
        },
        'location': {
            'latitude': 123.0,
            'longitude': 123.0
        },
        'customerArtifactPaths': {
            'iosPaths': [
                'string',
            ],
            'androidPaths': [
                'string',
            ],
            'deviceHostPaths': [
                'string',
            ]
        },
        'webUrl': 'string',
        'skipAppResign': True|False,
        'testSpecArn': 'string',
        'deviceSelectionResult': {
            'filters': [
                {
                    'attribute': 'ARN'|'PLATFORM'|'OS_VERSION'|'MODEL'|'AVAILABILITY'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'INSTANCE_ARN'|'INSTANCE_LABELS'|'FLEET_TYPE',
                    'operator': 'EQUALS'|'LESS_THAN'|'LESS_THAN_OR_EQUALS'|'GREATER_THAN'|'GREATER_THAN_OR_EQUALS'|'IN'|'NOT_IN'|'CONTAINS',
                    'values': [
                        'string',
                    ]
                },
            ],
            'matchedDevicesCount': 123,
            'maxDevices': 123
        }
    }
}


Response Structure

(dict) --Represents the result of a get run request.

run (dict) --The run to get results from.

arn (string) --The run\'s ARN.

name (string) --The run\'s name.

type (string) --The run\'s type.
Must be one of the following values:

BUILTIN_FUZZ
BUILTIN_EXPLORER


Note
For Android, an app explorer that traverses an Android app, interacting with it and capturing screenshots at the same time.


APPIUM_JAVA_JUNIT
APPIUM_JAVA_TESTNG
APPIUM_PYTHON
APPIUM_NODE
APPIUM_RUBY
APPIUM_WEB_JAVA_JUNIT
APPIUM_WEB_JAVA_TESTNG
APPIUM_WEB_PYTHON
APPIUM_WEB_NODE
APPIUM_WEB_RUBY
CALABASH
INSTRUMENTATION
UIAUTOMATION
UIAUTOMATOR
XCTEST
XCTEST_UI


platform (string) --The run\'s platform.
Allowed values include:

ANDROID
IOS


created (datetime) --When the run was created.

status (string) --The run\'s status.
Allowed values include:

PENDING
PENDING_CONCURRENCY
PENDING_DEVICE
PROCESSING
SCHEDULING
PREPARING
RUNNING
COMPLETED
STOPPING


result (string) --The run\'s result.
Allowed values include:

PENDING
PASSED
WARNED
FAILED
SKIPPED
ERRORED
STOPPED


started (datetime) --The run\'s start time.

stopped (datetime) --The run\'s stop time.

counters (dict) --The run\'s result counters.

total (integer) --The total number of entities.

passed (integer) --The number of passed entities.

failed (integer) --The number of failed entities.

warned (integer) --The number of warned entities.

errored (integer) --The number of errored entities.

stopped (integer) --The number of stopped entities.

skipped (integer) --The number of skipped entities.



message (string) --A message about the run\'s result.

totalJobs (integer) --The total number of jobs for the run.

completedJobs (integer) --The total number of completed jobs.

billingMethod (string) --Specifies the billing method for a test run: metered or unmetered . If the parameter is not specified, the default value is metered .

Note
If you have unmetered device slots, you must set this to unmetered to use them. Otherwise, the run is counted toward metered device minutes.


deviceMinutes (dict) --Represents the total (metered or unmetered) minutes used by the test run.

total (float) --When specified, represents the total minutes used by the resource to run tests.

metered (float) --When specified, represents only the sum of metered minutes used by the resource to run tests.

unmetered (float) --When specified, represents only the sum of unmetered minutes used by the resource to run tests.



networkProfile (dict) --The network profile being used for a test run.

arn (string) --The Amazon Resource Name (ARN) of the network profile.

name (string) --The name of the network profile.

description (string) --The description of the network profile.

type (string) --The type of network profile. Valid values are listed here.

uplinkBandwidthBits (integer) --The data throughput rate in bits per second, as an integer from 0 to 104857600.

downlinkBandwidthBits (integer) --The data throughput rate in bits per second, as an integer from 0 to 104857600.

uplinkDelayMs (integer) --Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.

downlinkDelayMs (integer) --Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.

uplinkJitterMs (integer) --Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.

downlinkJitterMs (integer) --Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.

uplinkLossPercent (integer) --Proportion of transmitted packets that fail to arrive from 0 to 100 percent.

downlinkLossPercent (integer) --Proportion of received packets that fail to arrive from 0 to 100 percent.



parsingResultUrl (string) --Read-only URL for an object in an S3 bucket where you can get the parsing results of the test package. If the test package doesn\'t parse, the reason why it doesn\'t parse appears in the file that this URL points to.

resultCode (string) --Supporting field for the result field. Set only if result is SKIPPED . PARSING_FAILED if the result is skipped because of test package parsing failure.

seed (integer) --For fuzz tests, this is a seed to use for randomizing the UI fuzz test. Using the same seed value between tests ensures identical event sequences.

appUpload (string) --An app to upload or that has been uploaded.

eventCount (integer) --For fuzz tests, this is the number of events, between 1 and 10000, that the UI fuzz test should perform.

jobTimeoutMinutes (integer) --The number of minutes the job executes before it times out.

devicePoolArn (string) --The ARN of the device pool for the run.

locale (string) --Information about the locale that is used for the run.

radios (dict) --Information about the radio states for the run.

wifi (boolean) --True if Wi-Fi is enabled at the beginning of the test. Otherwise, false.

bluetooth (boolean) --True if Bluetooth is enabled at the beginning of the test. Otherwise, false.

nfc (boolean) --True if NFC is enabled at the beginning of the test. Otherwise, false.

gps (boolean) --True if GPS is enabled at the beginning of the test. Otherwise, false.



location (dict) --Information about the location that is used for the run.

latitude (float) --The latitude.

longitude (float) --The longitude.



customerArtifactPaths (dict) --Output CustomerArtifactPaths object for the test run.

iosPaths (list) --Comma-separated list of paths on the iOS device where the artifacts generated by the customer\'s tests are pulled from.

(string) --


androidPaths (list) --Comma-separated list of paths on the Android device where the artifacts generated by the customer\'s tests are pulled from.

(string) --


deviceHostPaths (list) --Comma-separated list of paths in the test execution environment where the artifacts generated by the customer\'s tests are pulled from.

(string) --




webUrl (string) --The Device Farm console URL for the recording of the run.

skipAppResign (boolean) --When set to true , for private devices, Device Farm does not sign your app again. For public devices, Device Farm always signs your apps again.
For more information about how Device Farm re-signs your apps, see Do you modify my app? in the AWS Device Farm FAQs .

testSpecArn (string) --The ARN of the YAML-formatted test specification for the run.

deviceSelectionResult (dict) --The results of a device filter used to select the devices for a test run.

filters (list) --The filters in a device selection result.

(dict) --Represents a device filter used to select a set of devices to be included in a test run. This data structure is passed in as the deviceSelectionConfiguration parameter to ScheduleRun . For an example of the JSON request syntax, see  ScheduleRun .
It is also passed in as the filters parameter to ListDevices . For an example of the JSON request syntax, see  ListDevices .

attribute (string) --The aspect of a device such as platform or model used as the selection criteria in a device filter.
The supported operators for each attribute are provided in the following list.

ARN
The Amazon Resource Name (ARN) of the device (for example, arn:aws:devicefarm:us-west-2::device:12345Example ).
Supported operators: EQUALS , IN , NOT_IN

PLATFORM
The device platform. Valid values are ANDROID or IOS.
Supported operators: EQUALS

OS_VERSION
The operating system version (for example, 10.3.2).
Supported operators: EQUALS , GREATER_THAN , GREATER_THAN_OR_EQUALS , IN , LESS_THAN , LESS_THAN_OR_EQUALS , NOT_IN

MODEL
The device model (for example, iPad 5th Gen).
Supported operators: CONTAINS , EQUALS , IN , NOT_IN

AVAILABILITY
The current availability of the device. Valid values are AVAILABLE, HIGHLY_AVAILABLE, BUSY, or TEMPORARY_NOT_AVAILABLE.
Supported operators: EQUALS

FORM_FACTOR
The device form factor. Valid values are PHONE or TABLET.
Supported operators: EQUALS

MANUFACTURER
The device manufacturer (for example, Apple).
Supported operators: EQUALS , IN , NOT_IN

REMOTE_ACCESS_ENABLED
Whether the device is enabled for remote access. Valid values are TRUE or FALSE.
Supported operators: EQUALS

REMOTE_DEBUG_ENABLED
Whether the device is enabled for remote debugging. Valid values are TRUE or FALSE.
Supported operators: EQUALS
Because remote debugging is no longer supported , this filter is ignored.

INSTANCE_ARN
The Amazon Resource Name (ARN) of the device instance.
Supported operators: EQUALS , IN , NOT_IN

INSTANCE_LABELS
The label of the device instance.
Supported operators: CONTAINS

FLEET_TYPE
The fleet type. Valid values are PUBLIC or PRIVATE.
Supported operators: EQUALS

operator (string) --Specifies how Device Farm compares the filter\'s attribute to the value. See the attribute descriptions.

values (list) --An array of one or more filter values used in a device filter.

Operator Values

The IN and NOT_IN operators can take a values array that has more than one element.
The other operators require an array with a single element.


Attribute Values

The PLATFORM attribute can be set to ANDROID or IOS.
The AVAILABILITY attribute can be set to AVAILABLE, HIGHLY_AVAILABLE, BUSY, or TEMPORARY_NOT_AVAILABLE.
The FORM_FACTOR attribute can be set to PHONE or TABLET.
The FLEET_TYPE attribute can be set to PUBLIC or PRIVATE.


(string) --






matchedDevicesCount (integer) --The number of devices that matched the device filter selection criteria.

maxDevices (integer) --The maximum number of devices to be selected by a device filter and included in a test run.










Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.LimitExceededException
DeviceFarm.Client.exceptions.ServiceAccountException

Examples
The following example gets information about a specific test run.
response = client.get_run(
    # You can get the run ARN by using the list-runs CLI command.
    arn='arn:aws:devicefarm:us-west-2:123456789101:run:5e01a8c7-c861-4c0a-b1d5-5ec6e6c6dd23/0fcac17b-6122-44d7-ae5a-12345EXAMPLE',
)

print(response)


Expected Output:
{
    'run': {
        'name': 'My Test Run',
        'type': 'BUILTIN_EXPLORER',
        'arn': 'arn:aws:devicefarm:us-west-2:123456789101:run:5e01a8c7-c861-4c0a-b1d5-5ec6e6c6dd23/0fcac17b-6122-44d7-ae5a-12345EXAMPLE',
        'billingMethod': 'METERED',
        'completedJobs': 0,
        'counters': {
            'errored': 0,
            'failed': 0,
            'passed': 0,
            'skipped': 0,
            'stopped': 0,
            'total': 0,
            'warned': 0,
        },
        'created': datetime(2016, 8, 31, 18, 18, 29, 2, 244, 0),
        'deviceMinutes': {
            'metered': 0.0,
            'total': 0.0,
            'unmetered': 0.0,
        },
        'platform': 'ANDROID',
        'result': 'PENDING',
        'status': 'RUNNING',
        'totalJobs': 3,
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'run': {
            'arn': 'string',
            'name': 'string',
            'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'WEB_PERFORMANCE_PROFILE'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_NODE'|'APPIUM_RUBY'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'APPIUM_WEB_NODE'|'APPIUM_WEB_RUBY'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI'|'REMOTE_ACCESS_RECORD'|'REMOTE_ACCESS_REPLAY',
            'platform': 'ANDROID'|'IOS',
            'created': datetime(2015, 1, 1),
            'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
            'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
            'started': datetime(2015, 1, 1),
            'stopped': datetime(2015, 1, 1),
            'counters': {
                'total': 123,
                'passed': 123,
                'failed': 123,
                'warned': 123,
                'errored': 123,
                'stopped': 123,
                'skipped': 123
            },
            'message': 'string',
            'totalJobs': 123,
            'completedJobs': 123,
            'billingMethod': 'METERED'|'UNMETERED',
            'deviceMinutes': {
                'total': 123.0,
                'metered': 123.0,
                'unmetered': 123.0
            },
            'networkProfile': {
                'arn': 'string',
                'name': 'string',
                'description': 'string',
                'type': 'CURATED'|'PRIVATE',
                'uplinkBandwidthBits': 123,
                'downlinkBandwidthBits': 123,
                'uplinkDelayMs': 123,
                'downlinkDelayMs': 123,
                'uplinkJitterMs': 123,
                'downlinkJitterMs': 123,
                'uplinkLossPercent': 123,
                'downlinkLossPercent': 123
            },
            'parsingResultUrl': 'string',
            'resultCode': 'PARSING_FAILED'|'VPC_ENDPOINT_SETUP_FAILED',
            'seed': 123,
            'appUpload': 'string',
            'eventCount': 123,
            'jobTimeoutMinutes': 123,
            'devicePoolArn': 'string',
            'locale': 'string',
            'radios': {
                'wifi': True|False,
                'bluetooth': True|False,
                'nfc': True|False,
                'gps': True|False
            },
            'location': {
                'latitude': 123.0,
                'longitude': 123.0
            },
            'customerArtifactPaths': {
                'iosPaths': [
                    'string',
                ],
                'androidPaths': [
                    'string',
                ],
                'deviceHostPaths': [
                    'string',
                ]
            },
            'webUrl': 'string',
            'skipAppResign': True|False,
            'testSpecArn': 'string',
            'deviceSelectionResult': {
                'filters': [
                    {
                        'attribute': 'ARN'|'PLATFORM'|'OS_VERSION'|'MODEL'|'AVAILABILITY'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'INSTANCE_ARN'|'INSTANCE_LABELS'|'FLEET_TYPE',
                        'operator': 'EQUALS'|'LESS_THAN'|'LESS_THAN_OR_EQUALS'|'GREATER_THAN'|'GREATER_THAN_OR_EQUALS'|'IN'|'NOT_IN'|'CONTAINS',
                        'values': [
                            'string',
                        ]
                    },
                ],
                'matchedDevicesCount': 123,
                'maxDevices': 123
            }
        }
    }
    
    
    :returns: 
    APPIUM_JAVA_JUNIT
    APPIUM_JAVA_TESTNG
    APPIUM_PYTHON
    APPIUM_NODE
    APPIUM_RUBY
    APPIUM_WEB_JAVA_JUNIT
    APPIUM_WEB_JAVA_TESTNG
    APPIUM_WEB_PYTHON
    APPIUM_WEB_NODE
    APPIUM_WEB_RUBY
    CALABASH
    INSTRUMENTATION
    UIAUTOMATION
    UIAUTOMATOR
    XCTEST
    XCTEST_UI
    
    """
    pass

def get_suite(arn=None):
    """
    Gets information about a suite.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example gets information about a specific test suite.
    Expected Output:
    
    :example: response = client.get_suite(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]\nThe suite\'s ARN.\n

    :rtype: dict
ReturnsResponse Syntax{
    'suite': {
        'arn': 'string',
        'name': 'string',
        'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'WEB_PERFORMANCE_PROFILE'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_NODE'|'APPIUM_RUBY'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'APPIUM_WEB_NODE'|'APPIUM_WEB_RUBY'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI'|'REMOTE_ACCESS_RECORD'|'REMOTE_ACCESS_REPLAY',
        'created': datetime(2015, 1, 1),
        'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
        'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
        'started': datetime(2015, 1, 1),
        'stopped': datetime(2015, 1, 1),
        'counters': {
            'total': 123,
            'passed': 123,
            'failed': 123,
            'warned': 123,
            'errored': 123,
            'stopped': 123,
            'skipped': 123
        },
        'message': 'string',
        'deviceMinutes': {
            'total': 123.0,
            'metered': 123.0,
            'unmetered': 123.0
        }
    }
}


Response Structure

(dict) --Represents the result of a get suite request.

suite (dict) --A collection of one or more tests.

arn (string) --The suite\'s ARN.

name (string) --The suite\'s name.

type (string) --The suite\'s type.
Must be one of the following values:

BUILTIN_FUZZ
BUILTIN_EXPLORER


Note
Only available for Android; an app explorer that traverses an Android app, interacting with it and capturing screenshots at the same time.


APPIUM_JAVA_JUNIT
APPIUM_JAVA_TESTNG
APPIUM_PYTHON
APPIUM_NODE
APPIUM_RUBY
APPIUM_WEB_JAVA_JUNIT
APPIUM_WEB_JAVA_TESTNG
APPIUM_WEB_PYTHON
APPIUM_WEB_NODE
APPIUM_WEB_RUBY
CALABASH
INSTRUMENTATION
UIAUTOMATION
UIAUTOMATOR
XCTEST
XCTEST_UI


created (datetime) --When the suite was created.

status (string) --The suite\'s status.
Allowed values include:

PENDING
PENDING_CONCURRENCY
PENDING_DEVICE
PROCESSING
SCHEDULING
PREPARING
RUNNING
COMPLETED
STOPPING


result (string) --The suite\'s result.
Allowed values include:

PENDING
PASSED
WARNED
FAILED
SKIPPED
ERRORED
STOPPED


started (datetime) --The suite\'s start time.

stopped (datetime) --The suite\'s stop time.

counters (dict) --The suite\'s result counters.

total (integer) --The total number of entities.

passed (integer) --The number of passed entities.

failed (integer) --The number of failed entities.

warned (integer) --The number of warned entities.

errored (integer) --The number of errored entities.

stopped (integer) --The number of stopped entities.

skipped (integer) --The number of skipped entities.



message (string) --A message about the suite\'s result.

deviceMinutes (dict) --Represents the total (metered or unmetered) minutes used by the test suite.

total (float) --When specified, represents the total minutes used by the resource to run tests.

metered (float) --When specified, represents only the sum of metered minutes used by the resource to run tests.

unmetered (float) --When specified, represents only the sum of unmetered minutes used by the resource to run tests.










Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.LimitExceededException
DeviceFarm.Client.exceptions.ServiceAccountException

Examples
The following example gets information about a specific test suite.
response = client.get_suite(
    # You can get the suite ARN by using the list-suites CLI command.
    arn='arn:aws:devicefarm:us-west-2:123456789101:suite:EXAMPLE-GUID-123-456',
)

print(response)


Expected Output:
{
    'suite': {
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'suite': {
            'arn': 'string',
            'name': 'string',
            'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'WEB_PERFORMANCE_PROFILE'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_NODE'|'APPIUM_RUBY'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'APPIUM_WEB_NODE'|'APPIUM_WEB_RUBY'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI'|'REMOTE_ACCESS_RECORD'|'REMOTE_ACCESS_REPLAY',
            'created': datetime(2015, 1, 1),
            'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
            'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
            'started': datetime(2015, 1, 1),
            'stopped': datetime(2015, 1, 1),
            'counters': {
                'total': 123,
                'passed': 123,
                'failed': 123,
                'warned': 123,
                'errored': 123,
                'stopped': 123,
                'skipped': 123
            },
            'message': 'string',
            'deviceMinutes': {
                'total': 123.0,
                'metered': 123.0,
                'unmetered': 123.0
            }
        }
    }
    
    
    :returns: 
    APPIUM_JAVA_JUNIT
    APPIUM_JAVA_TESTNG
    APPIUM_PYTHON
    APPIUM_NODE
    APPIUM_RUBY
    APPIUM_WEB_JAVA_JUNIT
    APPIUM_WEB_JAVA_TESTNG
    APPIUM_WEB_PYTHON
    APPIUM_WEB_NODE
    APPIUM_WEB_RUBY
    CALABASH
    INSTRUMENTATION
    UIAUTOMATION
    UIAUTOMATOR
    XCTEST
    XCTEST_UI
    
    """
    pass

def get_test(arn=None):
    """
    Gets information about a test.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example gets information about a specific test.
    Expected Output:
    
    :example: response = client.get_test(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]\nThe test\'s ARN.\n

    :rtype: dict
ReturnsResponse Syntax{
    'test': {
        'arn': 'string',
        'name': 'string',
        'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'WEB_PERFORMANCE_PROFILE'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_NODE'|'APPIUM_RUBY'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'APPIUM_WEB_NODE'|'APPIUM_WEB_RUBY'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI'|'REMOTE_ACCESS_RECORD'|'REMOTE_ACCESS_REPLAY',
        'created': datetime(2015, 1, 1),
        'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
        'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
        'started': datetime(2015, 1, 1),
        'stopped': datetime(2015, 1, 1),
        'counters': {
            'total': 123,
            'passed': 123,
            'failed': 123,
            'warned': 123,
            'errored': 123,
            'stopped': 123,
            'skipped': 123
        },
        'message': 'string',
        'deviceMinutes': {
            'total': 123.0,
            'metered': 123.0,
            'unmetered': 123.0
        }
    }
}


Response Structure

(dict) --Represents the result of a get test request.

test (dict) --A test condition that is evaluated.

arn (string) --The test\'s ARN.

name (string) --The test\'s name.

type (string) --The test\'s type.
Must be one of the following values:

BUILTIN_FUZZ
BUILTIN_EXPLORER


Note
For Android, an app explorer that traverses an Android app, interacting with it and capturing screenshots at the same time.


APPIUM_JAVA_JUNIT
APPIUM_JAVA_TESTNG
APPIUM_PYTHON
APPIUM_NODE
APPIUM_RUBY
APPIUM_WEB_JAVA_JUNIT
APPIUM_WEB_JAVA_TESTNG
APPIUM_WEB_PYTHON
APPIUM_WEB_NODE
APPIUM_WEB_RUBY
CALABASH
INSTRUMENTATION
UIAUTOMATION
UIAUTOMATOR
XCTEST
XCTEST_UI


created (datetime) --When the test was created.

status (string) --The test\'s status.
Allowed values include:

PENDING
PENDING_CONCURRENCY
PENDING_DEVICE
PROCESSING
SCHEDULING
PREPARING
RUNNING
COMPLETED
STOPPING


result (string) --The test\'s result.
Allowed values include:

PENDING
PASSED
WARNED
FAILED
SKIPPED
ERRORED
STOPPED


started (datetime) --The test\'s start time.

stopped (datetime) --The test\'s stop time.

counters (dict) --The test\'s result counters.

total (integer) --The total number of entities.

passed (integer) --The number of passed entities.

failed (integer) --The number of failed entities.

warned (integer) --The number of warned entities.

errored (integer) --The number of errored entities.

stopped (integer) --The number of stopped entities.

skipped (integer) --The number of skipped entities.



message (string) --A message about the test\'s result.

deviceMinutes (dict) --Represents the total (metered or unmetered) minutes used by the test.

total (float) --When specified, represents the total minutes used by the resource to run tests.

metered (float) --When specified, represents only the sum of metered minutes used by the resource to run tests.

unmetered (float) --When specified, represents only the sum of unmetered minutes used by the resource to run tests.










Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.LimitExceededException
DeviceFarm.Client.exceptions.ServiceAccountException

Examples
The following example gets information about a specific test.
response = client.get_test(
    # You can get the test ARN by using the list-tests CLI command.
    arn='arn:aws:devicefarm:us-west-2:123456789101:test:EXAMPLE-GUID-123-456',
)

print(response)


Expected Output:
{
    'test': {
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'test': {
            'arn': 'string',
            'name': 'string',
            'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'WEB_PERFORMANCE_PROFILE'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_NODE'|'APPIUM_RUBY'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'APPIUM_WEB_NODE'|'APPIUM_WEB_RUBY'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI'|'REMOTE_ACCESS_RECORD'|'REMOTE_ACCESS_REPLAY',
            'created': datetime(2015, 1, 1),
            'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
            'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
            'started': datetime(2015, 1, 1),
            'stopped': datetime(2015, 1, 1),
            'counters': {
                'total': 123,
                'passed': 123,
                'failed': 123,
                'warned': 123,
                'errored': 123,
                'stopped': 123,
                'skipped': 123
            },
            'message': 'string',
            'deviceMinutes': {
                'total': 123.0,
                'metered': 123.0,
                'unmetered': 123.0
            }
        }
    }
    
    
    :returns: 
    APPIUM_JAVA_JUNIT
    APPIUM_JAVA_TESTNG
    APPIUM_PYTHON
    APPIUM_NODE
    APPIUM_RUBY
    APPIUM_WEB_JAVA_JUNIT
    APPIUM_WEB_JAVA_TESTNG
    APPIUM_WEB_PYTHON
    APPIUM_WEB_NODE
    APPIUM_WEB_RUBY
    CALABASH
    INSTRUMENTATION
    UIAUTOMATION
    UIAUTOMATOR
    XCTEST
    XCTEST_UI
    
    """
    pass

def get_test_grid_project(projectArn=None):
    """
    Retrieves information about a Selenium testing project.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_test_grid_project(
        projectArn='string'
    )
    
    
    :type projectArn: string
    :param projectArn: [REQUIRED]\nThe ARN of the Selenium testing project, from either CreateTestGridProject or ListTestGridProjects .\n

    :rtype: dict
ReturnsResponse Syntax{
    'testGridProject': {
        'arn': 'string',
        'name': 'string',
        'description': 'string',
        'created': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --
testGridProject (dict) --A  TestGridProject .

arn (string) --The ARN for the project.

name (string) --A human-readable name for the project.

description (string) --A human-readable description for the project.

created (datetime) --When the project was created.








Exceptions

DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.InternalServiceException


    :return: {
        'testGridProject': {
            'arn': 'string',
            'name': 'string',
            'description': 'string',
            'created': datetime(2015, 1, 1)
        }
    }
    
    
    """
    pass

def get_test_grid_session(projectArn=None, sessionId=None, sessionArn=None):
    """
    A session is an instance of a browser created through a RemoteWebDriver with the URL from  CreateTestGridUrlResult$url . You can use the following to look up sessions:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_test_grid_session(
        projectArn='string',
        sessionId='string',
        sessionArn='string'
    )
    
    
    :type projectArn: string
    :param projectArn: The ARN for the project that this session belongs to. See CreateTestGridProject and ListTestGridProjects .

    :type sessionId: string
    :param sessionId: An ID associated with this session.

    :type sessionArn: string
    :param sessionArn: An ARN that uniquely identifies a TestGridSession .

    :rtype: dict

ReturnsResponse Syntax
{
    'testGridSession': {
        'arn': 'string',
        'status': 'ACTIVE'|'CLOSED'|'ERRORED',
        'created': datetime(2015, 1, 1),
        'ended': datetime(2015, 1, 1),
        'billingMinutes': 123.0,
        'seleniumProperties': 'string'
    }
}


Response Structure

(dict) --

testGridSession (dict) --
The  TestGridSession that was requested.

arn (string) --
The ARN of the session.

status (string) --
The state of the session.

created (datetime) --
The time that the session was started.

ended (datetime) --
The time the session ended.

billingMinutes (float) --
The number of billed minutes that were used for this session.

seleniumProperties (string) --
A JSON object of options and parameters passed to the Selenium WebDriver.









Exceptions

DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.InternalServiceException


    :return: {
        'testGridSession': {
            'arn': 'string',
            'status': 'ACTIVE'|'CLOSED'|'ERRORED',
            'created': datetime(2015, 1, 1),
            'ended': datetime(2015, 1, 1),
            'billingMinutes': 123.0,
            'seleniumProperties': 'string'
        }
    }
    
    
    :returns: 
    projectArn (string) -- The ARN for the project that this session belongs to. See  CreateTestGridProject and  ListTestGridProjects .
    sessionId (string) -- An ID associated with this session.
    sessionArn (string) -- An ARN that uniquely identifies a  TestGridSession .
    
    """
    pass

def get_upload(arn=None):
    """
    Gets information about an upload.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example gets information about a specific upload.
    Expected Output:
    
    :example: response = client.get_upload(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]\nThe upload\'s ARN.\n

    :rtype: dict
ReturnsResponse Syntax{
    'upload': {
        'arn': 'string',
        'name': 'string',
        'created': datetime(2015, 1, 1),
        'type': 'ANDROID_APP'|'IOS_APP'|'WEB_APP'|'EXTERNAL_DATA'|'APPIUM_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_PYTHON_TEST_PACKAGE'|'APPIUM_NODE_TEST_PACKAGE'|'APPIUM_RUBY_TEST_PACKAGE'|'APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_WEB_PYTHON_TEST_PACKAGE'|'APPIUM_WEB_NODE_TEST_PACKAGE'|'APPIUM_WEB_RUBY_TEST_PACKAGE'|'CALABASH_TEST_PACKAGE'|'INSTRUMENTATION_TEST_PACKAGE'|'UIAUTOMATION_TEST_PACKAGE'|'UIAUTOMATOR_TEST_PACKAGE'|'XCTEST_TEST_PACKAGE'|'XCTEST_UI_TEST_PACKAGE'|'APPIUM_JAVA_JUNIT_TEST_SPEC'|'APPIUM_JAVA_TESTNG_TEST_SPEC'|'APPIUM_PYTHON_TEST_SPEC'|'APPIUM_NODE_TEST_SPEC'|'APPIUM_RUBY_TEST_SPEC'|'APPIUM_WEB_JAVA_JUNIT_TEST_SPEC'|'APPIUM_WEB_JAVA_TESTNG_TEST_SPEC'|'APPIUM_WEB_PYTHON_TEST_SPEC'|'APPIUM_WEB_NODE_TEST_SPEC'|'APPIUM_WEB_RUBY_TEST_SPEC'|'INSTRUMENTATION_TEST_SPEC'|'XCTEST_UI_TEST_SPEC',
        'status': 'INITIALIZED'|'PROCESSING'|'SUCCEEDED'|'FAILED',
        'url': 'string',
        'metadata': 'string',
        'contentType': 'string',
        'message': 'string',
        'category': 'CURATED'|'PRIVATE'
    }
}


Response Structure

(dict) --Represents the result of a get upload request.

upload (dict) --An app or a set of one or more tests to upload or that have been uploaded.

arn (string) --The upload\'s ARN.

name (string) --The upload\'s file name.

created (datetime) --When the upload was created.

type (string) --The upload\'s type.
Must be one of the following values:

ANDROID_APP
IOS_APP
WEB_APP
EXTERNAL_DATA
APPIUM_JAVA_JUNIT_TEST_PACKAGE
APPIUM_JAVA_TESTNG_TEST_PACKAGE
APPIUM_PYTHON_TEST_PACKAGE
APPIUM_NODE_TEST_PACKAGE
APPIUM_RUBY_TEST_PACKAGE
APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE
APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE
APPIUM_WEB_PYTHON_TEST_PACKAGE
APPIUM_WEB_NODE_TEST_PACKAGE
APPIUM_WEB_RUBY_TEST_PACKAGE
CALABASH_TEST_PACKAGE
INSTRUMENTATION_TEST_PACKAGE
UIAUTOMATION_TEST_PACKAGE
UIAUTOMATOR_TEST_PACKAGE
XCTEST_TEST_PACKAGE
XCTEST_UI_TEST_PACKAGE
APPIUM_JAVA_JUNIT_TEST_SPEC
APPIUM_JAVA_TESTNG_TEST_SPEC
APPIUM_PYTHON_TEST_SPEC
APPIUM_NODE_TEST_SPEC
APPIUM_RUBY_TEST_SPEC
APPIUM_WEB_JAVA_JUNIT_TEST_SPEC
APPIUM_WEB_JAVA_TESTNG_TEST_SPEC
APPIUM_WEB_PYTHON_TEST_SPEC
APPIUM_WEB_NODE_TEST_SPEC
APPIUM_WEB_RUBY_TEST_SPEC
INSTRUMENTATION_TEST_SPEC
XCTEST_UI_TEST_SPEC


status (string) --The upload\'s status.
Must be one of the following values:

FAILED
INITIALIZED
PROCESSING
SUCCEEDED


url (string) --The presigned Amazon S3 URL that was used to store a file using a PUT request.

metadata (string) --The upload\'s metadata. For example, for Android, this contains information that is parsed from the manifest and is displayed in the AWS Device Farm console after the associated app is uploaded.

contentType (string) --The upload\'s content type (for example, application/octet-stream ).

message (string) --A message about the upload\'s result.

category (string) --The upload\'s category. Allowed values include:

CURATED: An upload managed by AWS Device Farm.
PRIVATE: An upload managed by the AWS Device Farm customer.









Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.LimitExceededException
DeviceFarm.Client.exceptions.ServiceAccountException

Examples
The following example gets information about a specific upload.
response = client.get_upload(
    # You can get the test ARN by using the list-uploads CLI command.
    arn='arn:aws:devicefarm:us-west-2:123456789101:upload:EXAMPLE-GUID-123-456',
)

print(response)


Expected Output:
{
    'upload': {
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'upload': {
            'arn': 'string',
            'name': 'string',
            'created': datetime(2015, 1, 1),
            'type': 'ANDROID_APP'|'IOS_APP'|'WEB_APP'|'EXTERNAL_DATA'|'APPIUM_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_PYTHON_TEST_PACKAGE'|'APPIUM_NODE_TEST_PACKAGE'|'APPIUM_RUBY_TEST_PACKAGE'|'APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_WEB_PYTHON_TEST_PACKAGE'|'APPIUM_WEB_NODE_TEST_PACKAGE'|'APPIUM_WEB_RUBY_TEST_PACKAGE'|'CALABASH_TEST_PACKAGE'|'INSTRUMENTATION_TEST_PACKAGE'|'UIAUTOMATION_TEST_PACKAGE'|'UIAUTOMATOR_TEST_PACKAGE'|'XCTEST_TEST_PACKAGE'|'XCTEST_UI_TEST_PACKAGE'|'APPIUM_JAVA_JUNIT_TEST_SPEC'|'APPIUM_JAVA_TESTNG_TEST_SPEC'|'APPIUM_PYTHON_TEST_SPEC'|'APPIUM_NODE_TEST_SPEC'|'APPIUM_RUBY_TEST_SPEC'|'APPIUM_WEB_JAVA_JUNIT_TEST_SPEC'|'APPIUM_WEB_JAVA_TESTNG_TEST_SPEC'|'APPIUM_WEB_PYTHON_TEST_SPEC'|'APPIUM_WEB_NODE_TEST_SPEC'|'APPIUM_WEB_RUBY_TEST_SPEC'|'INSTRUMENTATION_TEST_SPEC'|'XCTEST_UI_TEST_SPEC',
            'status': 'INITIALIZED'|'PROCESSING'|'SUCCEEDED'|'FAILED',
            'url': 'string',
            'metadata': 'string',
            'contentType': 'string',
            'message': 'string',
            'category': 'CURATED'|'PRIVATE'
        }
    }
    
    
    :returns: 
    FAILED
    INITIALIZED
    PROCESSING
    SUCCEEDED
    
    """
    pass

def get_vpce_configuration(arn=None):
    """
    Returns information about the configuration settings for your Amazon Virtual Private Cloud (VPC) endpoint.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_vpce_configuration(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the VPC endpoint configuration you want to describe.\n

    :rtype: dict
ReturnsResponse Syntax{
    'vpceConfiguration': {
        'arn': 'string',
        'vpceConfigurationName': 'string',
        'vpceServiceName': 'string',
        'serviceDnsName': 'string',
        'vpceConfigurationDescription': 'string'
    }
}


Response Structure

(dict) --
vpceConfiguration (dict) --An object that contains information about your VPC endpoint configuration.

arn (string) --The Amazon Resource Name (ARN) of the VPC endpoint configuration.

vpceConfigurationName (string) --The friendly name you give to your VPC endpoint configuration to manage your configurations more easily.

vpceServiceName (string) --The name of the VPC endpoint service running in your AWS account that you want Device Farm to test.

serviceDnsName (string) --The DNS name that maps to the private IP address of the service you want to access.

vpceConfigurationDescription (string) --An optional description that provides details about your VPC endpoint configuration.








Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.ServiceAccountException


    :return: {
        'vpceConfiguration': {
            'arn': 'string',
            'vpceConfigurationName': 'string',
            'vpceServiceName': 'string',
            'serviceDnsName': 'string',
            'vpceConfigurationDescription': 'string'
        }
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

def install_to_remote_access_session(remoteAccessSessionArn=None, appArn=None):
    """
    Installs an application to the device in a remote access session. For Android applications, the file must be in .apk format. For iOS applications, the file must be in .ipa format.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example installs a specific app to a device in a specific remote access session.
    Expected Output:
    
    :example: response = client.install_to_remote_access_session(
        remoteAccessSessionArn='string',
        appArn='string'
    )
    
    
    :type remoteAccessSessionArn: string
    :param remoteAccessSessionArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the remote access session about which you are requesting information.\n

    :type appArn: string
    :param appArn: [REQUIRED]\nThe ARN of the app about which you are requesting information.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'appUpload': {
        'arn': 'string',
        'name': 'string',
        'created': datetime(2015, 1, 1),
        'type': 'ANDROID_APP'|'IOS_APP'|'WEB_APP'|'EXTERNAL_DATA'|'APPIUM_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_PYTHON_TEST_PACKAGE'|'APPIUM_NODE_TEST_PACKAGE'|'APPIUM_RUBY_TEST_PACKAGE'|'APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_WEB_PYTHON_TEST_PACKAGE'|'APPIUM_WEB_NODE_TEST_PACKAGE'|'APPIUM_WEB_RUBY_TEST_PACKAGE'|'CALABASH_TEST_PACKAGE'|'INSTRUMENTATION_TEST_PACKAGE'|'UIAUTOMATION_TEST_PACKAGE'|'UIAUTOMATOR_TEST_PACKAGE'|'XCTEST_TEST_PACKAGE'|'XCTEST_UI_TEST_PACKAGE'|'APPIUM_JAVA_JUNIT_TEST_SPEC'|'APPIUM_JAVA_TESTNG_TEST_SPEC'|'APPIUM_PYTHON_TEST_SPEC'|'APPIUM_NODE_TEST_SPEC'|'APPIUM_RUBY_TEST_SPEC'|'APPIUM_WEB_JAVA_JUNIT_TEST_SPEC'|'APPIUM_WEB_JAVA_TESTNG_TEST_SPEC'|'APPIUM_WEB_PYTHON_TEST_SPEC'|'APPIUM_WEB_NODE_TEST_SPEC'|'APPIUM_WEB_RUBY_TEST_SPEC'|'INSTRUMENTATION_TEST_SPEC'|'XCTEST_UI_TEST_SPEC',
        'status': 'INITIALIZED'|'PROCESSING'|'SUCCEEDED'|'FAILED',
        'url': 'string',
        'metadata': 'string',
        'contentType': 'string',
        'message': 'string',
        'category': 'CURATED'|'PRIVATE'
    }
}


Response Structure

(dict) --
Represents the response from the server after AWS Device Farm makes a request to install to a remote access session.

appUpload (dict) --
An app to upload or that has been uploaded.

arn (string) --
The upload\'s ARN.

name (string) --
The upload\'s file name.

created (datetime) --
When the upload was created.

type (string) --
The upload\'s type.
Must be one of the following values:

ANDROID_APP
IOS_APP
WEB_APP
EXTERNAL_DATA
APPIUM_JAVA_JUNIT_TEST_PACKAGE
APPIUM_JAVA_TESTNG_TEST_PACKAGE
APPIUM_PYTHON_TEST_PACKAGE
APPIUM_NODE_TEST_PACKAGE
APPIUM_RUBY_TEST_PACKAGE
APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE
APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE
APPIUM_WEB_PYTHON_TEST_PACKAGE
APPIUM_WEB_NODE_TEST_PACKAGE
APPIUM_WEB_RUBY_TEST_PACKAGE
CALABASH_TEST_PACKAGE
INSTRUMENTATION_TEST_PACKAGE
UIAUTOMATION_TEST_PACKAGE
UIAUTOMATOR_TEST_PACKAGE
XCTEST_TEST_PACKAGE
XCTEST_UI_TEST_PACKAGE
APPIUM_JAVA_JUNIT_TEST_SPEC
APPIUM_JAVA_TESTNG_TEST_SPEC
APPIUM_PYTHON_TEST_SPEC
APPIUM_NODE_TEST_SPEC
APPIUM_RUBY_TEST_SPEC
APPIUM_WEB_JAVA_JUNIT_TEST_SPEC
APPIUM_WEB_JAVA_TESTNG_TEST_SPEC
APPIUM_WEB_PYTHON_TEST_SPEC
APPIUM_WEB_NODE_TEST_SPEC
APPIUM_WEB_RUBY_TEST_SPEC
INSTRUMENTATION_TEST_SPEC
XCTEST_UI_TEST_SPEC


status (string) --
The upload\'s status.
Must be one of the following values:

FAILED
INITIALIZED
PROCESSING
SUCCEEDED


url (string) --
The presigned Amazon S3 URL that was used to store a file using a PUT request.

metadata (string) --
The upload\'s metadata. For example, for Android, this contains information that is parsed from the manifest and is displayed in the AWS Device Farm console after the associated app is uploaded.

contentType (string) --
The upload\'s content type (for example, application/octet-stream ).

message (string) --
A message about the upload\'s result.

category (string) --
The upload\'s category. Allowed values include:

CURATED: An upload managed by AWS Device Farm.
PRIVATE: An upload managed by the AWS Device Farm customer.










Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.LimitExceededException
DeviceFarm.Client.exceptions.ServiceAccountException

Examples
The following example installs a specific app to a device in a specific remote access session.
response = client.install_to_remote_access_session(
    appArn='arn:aws:devicefarm:us-west-2:123456789101:app:EXAMPLE-GUID-123-456',
    # You can get the remote access session ARN by using the list-remote-access-sessions CLI command.
    remoteAccessSessionArn='arn:aws:devicefarm:us-west-2:123456789101:session:EXAMPLE-GUID-123-456',
)

print(response)


Expected Output:
{
    'appUpload': {
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'appUpload': {
            'arn': 'string',
            'name': 'string',
            'created': datetime(2015, 1, 1),
            'type': 'ANDROID_APP'|'IOS_APP'|'WEB_APP'|'EXTERNAL_DATA'|'APPIUM_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_PYTHON_TEST_PACKAGE'|'APPIUM_NODE_TEST_PACKAGE'|'APPIUM_RUBY_TEST_PACKAGE'|'APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_WEB_PYTHON_TEST_PACKAGE'|'APPIUM_WEB_NODE_TEST_PACKAGE'|'APPIUM_WEB_RUBY_TEST_PACKAGE'|'CALABASH_TEST_PACKAGE'|'INSTRUMENTATION_TEST_PACKAGE'|'UIAUTOMATION_TEST_PACKAGE'|'UIAUTOMATOR_TEST_PACKAGE'|'XCTEST_TEST_PACKAGE'|'XCTEST_UI_TEST_PACKAGE'|'APPIUM_JAVA_JUNIT_TEST_SPEC'|'APPIUM_JAVA_TESTNG_TEST_SPEC'|'APPIUM_PYTHON_TEST_SPEC'|'APPIUM_NODE_TEST_SPEC'|'APPIUM_RUBY_TEST_SPEC'|'APPIUM_WEB_JAVA_JUNIT_TEST_SPEC'|'APPIUM_WEB_JAVA_TESTNG_TEST_SPEC'|'APPIUM_WEB_PYTHON_TEST_SPEC'|'APPIUM_WEB_NODE_TEST_SPEC'|'APPIUM_WEB_RUBY_TEST_SPEC'|'INSTRUMENTATION_TEST_SPEC'|'XCTEST_UI_TEST_SPEC',
            'status': 'INITIALIZED'|'PROCESSING'|'SUCCEEDED'|'FAILED',
            'url': 'string',
            'metadata': 'string',
            'contentType': 'string',
            'message': 'string',
            'category': 'CURATED'|'PRIVATE'
        }
    }
    
    
    :returns: 
    ANDROID_APP
    IOS_APP
    WEB_APP
    EXTERNAL_DATA
    APPIUM_JAVA_JUNIT_TEST_PACKAGE
    APPIUM_JAVA_TESTNG_TEST_PACKAGE
    APPIUM_PYTHON_TEST_PACKAGE
    APPIUM_NODE_TEST_PACKAGE
    APPIUM_RUBY_TEST_PACKAGE
    APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE
    APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE
    APPIUM_WEB_PYTHON_TEST_PACKAGE
    APPIUM_WEB_NODE_TEST_PACKAGE
    APPIUM_WEB_RUBY_TEST_PACKAGE
    CALABASH_TEST_PACKAGE
    INSTRUMENTATION_TEST_PACKAGE
    UIAUTOMATION_TEST_PACKAGE
    UIAUTOMATOR_TEST_PACKAGE
    XCTEST_TEST_PACKAGE
    XCTEST_UI_TEST_PACKAGE
    APPIUM_JAVA_JUNIT_TEST_SPEC
    APPIUM_JAVA_TESTNG_TEST_SPEC
    APPIUM_PYTHON_TEST_SPEC
    APPIUM_NODE_TEST_SPEC
    APPIUM_RUBY_TEST_SPEC
    APPIUM_WEB_JAVA_JUNIT_TEST_SPEC
    APPIUM_WEB_JAVA_TESTNG_TEST_SPEC
    APPIUM_WEB_PYTHON_TEST_SPEC
    APPIUM_WEB_NODE_TEST_SPEC
    APPIUM_WEB_RUBY_TEST_SPEC
    INSTRUMENTATION_TEST_SPEC
    XCTEST_UI_TEST_SPEC
    
    """
    pass

def list_artifacts(arn=None, type=None, nextToken=None):
    """
    Gets information about artifacts.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example lists screenshot artifacts for a specific run.
    Expected Output:
    
    :example: response = client.list_artifacts(
        arn='string',
        type='SCREENSHOT'|'FILE'|'LOG',
        nextToken='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]\nThe run, job, suite, or test ARN.\n

    :type type: string
    :param type: [REQUIRED]\nThe artifacts\' type.\nAllowed values include:\n\nFILE\nLOG\nSCREENSHOT\n\n

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :rtype: dict

ReturnsResponse Syntax
{
    'artifacts': [
        {
            'arn': 'string',
            'name': 'string',
            'type': 'UNKNOWN'|'SCREENSHOT'|'DEVICE_LOG'|'MESSAGE_LOG'|'VIDEO_LOG'|'RESULT_LOG'|'SERVICE_LOG'|'WEBKIT_LOG'|'INSTRUMENTATION_OUTPUT'|'EXERCISER_MONKEY_OUTPUT'|'CALABASH_JSON_OUTPUT'|'CALABASH_PRETTY_OUTPUT'|'CALABASH_STANDARD_OUTPUT'|'CALABASH_JAVA_XML_OUTPUT'|'AUTOMATION_OUTPUT'|'APPIUM_SERVER_OUTPUT'|'APPIUM_JAVA_OUTPUT'|'APPIUM_JAVA_XML_OUTPUT'|'APPIUM_PYTHON_OUTPUT'|'APPIUM_PYTHON_XML_OUTPUT'|'EXPLORER_EVENT_LOG'|'EXPLORER_SUMMARY_LOG'|'APPLICATION_CRASH_REPORT'|'XCTEST_LOG'|'VIDEO'|'CUSTOMER_ARTIFACT'|'CUSTOMER_ARTIFACT_LOG'|'TESTSPEC_OUTPUT',
            'extension': 'string',
            'url': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --
Represents the result of a list artifacts operation.

artifacts (list) --
Information about the artifacts.

(dict) --
Represents the output of a test. Examples of artifacts include logs and screenshots.

arn (string) --
The artifact\'s ARN.

name (string) --
The artifact\'s name.

type (string) --
The artifact\'s type.
Allowed values include the following:

UNKNOWN
SCREENSHOT
DEVICE_LOG
MESSAGE_LOG
VIDEO_LOG
RESULT_LOG
SERVICE_LOG
WEBKIT_LOG
INSTRUMENTATION_OUTPUT
EXERCISER_MONKEY_OUTPUT: the artifact (log) generated by an Android fuzz test.
CALABASH_JSON_OUTPUT
CALABASH_PRETTY_OUTPUT
CALABASH_STANDARD_OUTPUT
CALABASH_JAVA_XML_OUTPUT
AUTOMATION_OUTPUT
APPIUM_SERVER_OUTPUT
APPIUM_JAVA_OUTPUT
APPIUM_JAVA_XML_OUTPUT
APPIUM_PYTHON_OUTPUT
APPIUM_PYTHON_XML_OUTPUT
EXPLORER_EVENT_LOG
EXPLORER_SUMMARY_LOG
APPLICATION_CRASH_REPORT
XCTEST_LOG
VIDEO
CUSTOMER_ARTIFACT
CUSTOMER_ARTIFACT_LOG
TESTSPEC_OUTPUT


extension (string) --
The artifact\'s file extension.

url (string) --
The presigned Amazon S3 URL that can be used with a GET request to download the artifact\'s file.





nextToken (string) --
If the number of items that are returned is significantly large, this is an identifier that is also returned. It can be used in a subsequent call to this operation to return the next set of items in the list.







Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.LimitExceededException
DeviceFarm.Client.exceptions.ServiceAccountException

Examples
The following example lists screenshot artifacts for a specific run.
response = client.list_artifacts(
    type='SCREENSHOT',
    # Can also be used to list artifacts for a Job, Suite, or Test ARN.
    arn='arn:aws:devicefarm:us-west-2:123456789101:run:EXAMPLE-GUID-123-456',
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'artifacts': [
            {
                'arn': 'string',
                'name': 'string',
                'type': 'UNKNOWN'|'SCREENSHOT'|'DEVICE_LOG'|'MESSAGE_LOG'|'VIDEO_LOG'|'RESULT_LOG'|'SERVICE_LOG'|'WEBKIT_LOG'|'INSTRUMENTATION_OUTPUT'|'EXERCISER_MONKEY_OUTPUT'|'CALABASH_JSON_OUTPUT'|'CALABASH_PRETTY_OUTPUT'|'CALABASH_STANDARD_OUTPUT'|'CALABASH_JAVA_XML_OUTPUT'|'AUTOMATION_OUTPUT'|'APPIUM_SERVER_OUTPUT'|'APPIUM_JAVA_OUTPUT'|'APPIUM_JAVA_XML_OUTPUT'|'APPIUM_PYTHON_OUTPUT'|'APPIUM_PYTHON_XML_OUTPUT'|'EXPLORER_EVENT_LOG'|'EXPLORER_SUMMARY_LOG'|'APPLICATION_CRASH_REPORT'|'XCTEST_LOG'|'VIDEO'|'CUSTOMER_ARTIFACT'|'CUSTOMER_ARTIFACT_LOG'|'TESTSPEC_OUTPUT',
                'extension': 'string',
                'url': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    UNKNOWN
    SCREENSHOT
    DEVICE_LOG
    MESSAGE_LOG
    VIDEO_LOG
    RESULT_LOG
    SERVICE_LOG
    WEBKIT_LOG
    INSTRUMENTATION_OUTPUT
    EXERCISER_MONKEY_OUTPUT: the artifact (log) generated by an Android fuzz test.
    CALABASH_JSON_OUTPUT
    CALABASH_PRETTY_OUTPUT
    CALABASH_STANDARD_OUTPUT
    CALABASH_JAVA_XML_OUTPUT
    AUTOMATION_OUTPUT
    APPIUM_SERVER_OUTPUT
    APPIUM_JAVA_OUTPUT
    APPIUM_JAVA_XML_OUTPUT
    APPIUM_PYTHON_OUTPUT
    APPIUM_PYTHON_XML_OUTPUT
    EXPLORER_EVENT_LOG
    EXPLORER_SUMMARY_LOG
    APPLICATION_CRASH_REPORT
    XCTEST_LOG
    VIDEO
    CUSTOMER_ARTIFACT
    CUSTOMER_ARTIFACT_LOG
    TESTSPEC_OUTPUT
    
    """
    pass

def list_device_instances(maxResults=None, nextToken=None):
    """
    Returns information about the private device instances associated with one or more AWS accounts.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_device_instances(
        maxResults=123,
        nextToken='string'
    )
    
    
    :type maxResults: integer
    :param maxResults: An integer that specifies the maximum number of items you want to return in the API response.

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :rtype: dict

ReturnsResponse Syntax
{
    'deviceInstances': [
        {
            'arn': 'string',
            'deviceArn': 'string',
            'labels': [
                'string',
            ],
            'status': 'IN_USE'|'PREPARING'|'AVAILABLE'|'NOT_AVAILABLE',
            'udid': 'string',
            'instanceProfile': {
                'arn': 'string',
                'packageCleanup': True|False,
                'excludeAppPackagesFromCleanup': [
                    'string',
                ],
                'rebootAfterUse': True|False,
                'name': 'string',
                'description': 'string'
            }
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

deviceInstances (list) --
An object that contains information about your device instances.

(dict) --
Represents the device instance.

arn (string) --
The Amazon Resource Name (ARN) of the device instance.

deviceArn (string) --
The ARN of the device.

labels (list) --
An array of strings that describe the device instance.

(string) --


status (string) --
The status of the device instance. Valid values are listed here.

udid (string) --
Unique device identifier for the device instance.

instanceProfile (dict) --
A object that contains information about the instance profile.

arn (string) --
The Amazon Resource Name (ARN) of the instance profile.

packageCleanup (boolean) --
When set to true , Device Farm removes app packages after a test run. The default value is false for private devices.

excludeAppPackagesFromCleanup (list) --
An array of strings containing the list of app packages that should not be cleaned up from the device after a test run completes.
The list of packages is considered only if you set packageCleanup to true .

(string) --


rebootAfterUse (boolean) --
When set to true , Device Farm reboots the instance after a test run. The default value is true .

name (string) --
The name of the instance profile.

description (string) --
The description of the instance profile.







nextToken (string) --
An identifier that can be used in the next call to this operation to return the next set of items in the list.







Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.LimitExceededException
DeviceFarm.Client.exceptions.ServiceAccountException


    :return: {
        'deviceInstances': [
            {
                'arn': 'string',
                'deviceArn': 'string',
                'labels': [
                    'string',
                ],
                'status': 'IN_USE'|'PREPARING'|'AVAILABLE'|'NOT_AVAILABLE',
                'udid': 'string',
                'instanceProfile': {
                    'arn': 'string',
                    'packageCleanup': True|False,
                    'excludeAppPackagesFromCleanup': [
                        'string',
                    ],
                    'rebootAfterUse': True|False,
                    'name': 'string',
                    'description': 'string'
                }
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_device_pools(arn=None, type=None, nextToken=None):
    """
    Gets information about device pools.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example returns information about the private device pools in a specific project.
    Expected Output:
    
    :example: response = client.list_device_pools(
        arn='string',
        type='CURATED'|'PRIVATE',
        nextToken='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]\nThe project ARN.\n

    :type type: string
    :param type: The device pools\' type.\nAllowed values include:\n\nCURATED: A device pool that is created and managed by AWS Device Farm.\nPRIVATE: A device pool that is created and managed by the device pool developer.\n\n

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :rtype: dict

ReturnsResponse Syntax
{
    'devicePools': [
        {
            'arn': 'string',
            'name': 'string',
            'description': 'string',
            'type': 'CURATED'|'PRIVATE',
            'rules': [
                {
                    'attribute': 'ARN'|'PLATFORM'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'APPIUM_VERSION'|'INSTANCE_ARN'|'INSTANCE_LABELS'|'FLEET_TYPE'|'OS_VERSION'|'MODEL'|'AVAILABILITY',
                    'operator': 'EQUALS'|'LESS_THAN'|'LESS_THAN_OR_EQUALS'|'GREATER_THAN'|'GREATER_THAN_OR_EQUALS'|'IN'|'NOT_IN'|'CONTAINS',
                    'value': 'string'
                },
            ],
            'maxDevices': 123
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --
Represents the result of a list device pools request.

devicePools (list) --
Information about the device pools.

(dict) --
Represents a collection of device types.

arn (string) --
The device pool\'s ARN.

name (string) --
The device pool\'s name.

description (string) --
The device pool\'s description.

type (string) --
The device pool\'s type.
Allowed values include:

CURATED: A device pool that is created and managed by AWS Device Farm.
PRIVATE: A device pool that is created and managed by the device pool developer.


rules (list) --
Information about the device pool\'s rules.

(dict) --
Represents a condition for a device pool.

attribute (string) --
The rule\'s stringified attribute. For example, specify the value as "\\"abc\\"" .
The supported operators for each attribute are provided in the following list.

APPIUM_VERSION

The Appium version for the test.
Supported operators: CONTAINS

ARN

The Amazon Resource Name (ARN) of the device (for example, arn:aws:devicefarm:us-west-2::device:12345Example .
Supported operators: EQUALS , IN , NOT_IN

AVAILABILITY

The current availability of the device. Valid values are AVAILABLE, HIGHLY_AVAILABLE, BUSY, or TEMPORARY_NOT_AVAILABLE.
Supported operators: EQUALS

FLEET_TYPE

The fleet type. Valid values are PUBLIC or PRIVATE.
Supported operators: EQUALS

FORM_FACTOR

The device form factor. Valid values are PHONE or TABLET.
Supported operators: EQUALS , IN , NOT_IN

INSTANCE_ARN

The Amazon Resource Name (ARN) of the device instance.
Supported operators: IN , NOT_IN

INSTANCE_LABELS

The label of the device instance.
Supported operators: CONTAINS

MANUFACTURER

The device manufacturer (for example, Apple).
Supported operators: EQUALS , IN , NOT_IN

MODEL

The device model, such as Apple iPad Air 2 or Google Pixel.
Supported operators: CONTAINS , EQUALS , IN , NOT_IN

OS_VERSION

The operating system version (for example, 10.3.2).
Supported operators: EQUALS , GREATER_THAN , GREATER_THAN_OR_EQUALS , IN , LESS_THAN , LESS_THAN_OR_EQUALS , NOT_IN

PLATFORM

The device platform. Valid values are ANDROID or IOS.
Supported operators: EQUALS , IN , NOT_IN

REMOTE_ACCESS_ENABLED

Whether the device is enabled for remote access. Valid values are TRUE or FALSE.
Supported operators: EQUALS

REMOTE_DEBUG_ENABLED

Whether the device is enabled for remote debugging. Valid values are TRUE or FALSE.
Supported operators: EQUALS
Because remote debugging is no longer supported , this filter is ignored.

operator (string) --
Specifies how Device Farm compares the rule\'s attribute to the value. For the operators that are supported by each attribute, see the attribute descriptions.

value (string) --
The rule\'s value.





maxDevices (integer) --
The number of devices that Device Farm can add to your device pool. Device Farm adds devices that are available and meet the criteria that you assign for the rules parameter. Depending on how many devices meet these constraints, your device pool might contain fewer devices than the value for this parameter.
By specifying the maximum number of devices, you can control the costs that you incur by running tests.





nextToken (string) --
If the number of items that are returned is significantly large, this is an identifier that is also returned. It can be used in a subsequent call to this operation to return the next set of items in the list.







Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.LimitExceededException
DeviceFarm.Client.exceptions.ServiceAccountException

Examples
The following example returns information about the private device pools in a specific project.
response = client.list_device_pools(
    type='PRIVATE',
    # You can get the project ARN by using the list-projects CLI command.
    arn='arn:aws:devicefarm:us-west-2:123456789101:project:EXAMPLE-GUID-123-456',
)

print(response)


Expected Output:
{
    'devicePools': [
        {
            'name': 'Top Devices',
            'arn': 'arn:aws:devicefarm:us-west-2::devicepool:082d10e5-d7d7-48a5-ba5c-12345EXAMPLE',
            'description': 'Top devices',
            'rules': [
                {
                    'value': '["arn:aws:devicefarm:us-west-2::device:123456789EXAMPLE","arn:aws:devicefarm:us-west-2::device:123456789EXAMPLE","arn:aws:devicefarm:us-west-2::device:123456789EXAMPLE","arn:aws:devicefarm:us-west-2::device:123456789EXAMPLE","arn:aws:devicefarm:us-west-2::device:123456789EXAMPLE","arn:aws:devicefarm:us-west-2::device:123456789EXAMPLE","arn:aws:devicefarm:us-west-2::device:123456789EXAMPLE","arn:aws:devicefarm:us-west-2::device:123456789EXAMPLE","arn:aws:devicefarm:us-west-2::device:123456789EXAMPLE","arn:aws:devicefarm:us-west-2::device:123456789EXAMPLE"]',
                    'attribute': 'ARN',
                    'operator': 'IN',
                },
            ],
        },
        {
            'name': 'My Android Device Pool',
            'arn': 'arn:aws:devicefarm:us-west-2:123456789101:devicepool:5e01a8c7-c861-4c0a-b1d5-5ec6e6c6dd23/bf96e75a-28f6-4e61-b6a7-12345EXAMPLE',
            'description': 'Samsung Galaxy Android devices',
            'rules': [
                {
                    'value': '["arn:aws:devicefarm:us-west-2::device:123456789EXAMPLE","arn:aws:devicefarm:us-west-2::device:123456789EXAMPLE","arn:aws:devicefarm:us-west-2::device:123456789EXAMPLE"]',
                    'attribute': 'ARN',
                    'operator': 'IN',
                },
            ],
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'devicePools': [
            {
                'arn': 'string',
                'name': 'string',
                'description': 'string',
                'type': 'CURATED'|'PRIVATE',
                'rules': [
                    {
                        'attribute': 'ARN'|'PLATFORM'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'APPIUM_VERSION'|'INSTANCE_ARN'|'INSTANCE_LABELS'|'FLEET_TYPE'|'OS_VERSION'|'MODEL'|'AVAILABILITY',
                        'operator': 'EQUALS'|'LESS_THAN'|'LESS_THAN_OR_EQUALS'|'GREATER_THAN'|'GREATER_THAN_OR_EQUALS'|'IN'|'NOT_IN'|'CONTAINS',
                        'value': 'string'
                    },
                ],
                'maxDevices': 123
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    CURATED: A device pool that is created and managed by AWS Device Farm.
    PRIVATE: A device pool that is created and managed by the device pool developer.
    
    """
    pass

def list_devices(arn=None, nextToken=None, filters=None):
    """
    Gets information about unique device types.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example returns information about the available devices in a specific project.
    Expected Output:
    
    :example: response = client.list_devices(
        arn='string',
        nextToken='string',
        filters=[
            {
                'attribute': 'ARN'|'PLATFORM'|'OS_VERSION'|'MODEL'|'AVAILABILITY'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'INSTANCE_ARN'|'INSTANCE_LABELS'|'FLEET_TYPE',
                'operator': 'EQUALS'|'LESS_THAN'|'LESS_THAN_OR_EQUALS'|'GREATER_THAN'|'GREATER_THAN_OR_EQUALS'|'IN'|'NOT_IN'|'CONTAINS',
                'values': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type arn: string
    :param arn: The Amazon Resource Name (ARN) of the project.

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :type filters: list
    :param filters: Used to select a set of devices. A filter is made up of an attribute, an operator, and one or more values.\n\nAttribute: The aspect of a device such as platform or model used as the selection criteria in a device filter. Allowed values include:\nARN: The Amazon Resource Name (ARN) of the device (for example, arn:aws:devicefarm:us-west-2::device:12345Example ).\nPLATFORM: The device platform. Valid values are ANDROID or IOS.\nOS_VERSION: The operating system version (for example, 10.3.2).\nMODEL: The device model (for example, iPad 5th Gen).\nAVAILABILITY: The current availability of the device. Valid values are AVAILABLE, HIGHLY_AVAILABLE, BUSY, or TEMPORARY_NOT_AVAILABLE.\nFORM_FACTOR: The device form factor. Valid values are PHONE or TABLET.\nMANUFACTURER: The device manufacturer (for example, Apple).\nREMOTE_ACCESS_ENABLED: Whether the device is enabled for remote access. Valid values are TRUE or FALSE.\nREMOTE_DEBUG_ENABLED: Whether the device is enabled for remote debugging. Valid values are TRUE or FALSE. Because remote debugging is no longer supported , this attribute is ignored.\nINSTANCE_ARN: The Amazon Resource Name (ARN) of the device instance.\nINSTANCE_LABELS: The label of the device instance.\nFLEET_TYPE: The fleet type. Valid values are PUBLIC or PRIVATE.\n\n\nOperator: The filter operator.\nThe EQUALS operator is available for every attribute except INSTANCE_LABELS.\nThe CONTAINS operator is available for the INSTANCE_LABELS and MODEL attributes.\nThe IN and NOT_IN operators are available for the ARN, OS_VERSION, MODEL, MANUFACTURER, and INSTANCE_ARN attributes.\nThe LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUALS, and GREATER_THAN_OR_EQUALS operators are also available for the OS_VERSION attribute.\n\n\nValues: An array of one or more filter values.\nThe IN and NOT_IN operators take a values array that has one or more elements.\nThe other operators require an array with a single element.\nIn a request, the AVAILABILITY attribute takes the following values: AVAILABLE, HIGHLY_AVAILABLE, BUSY, or TEMPORARY_NOT_AVAILABLE.\n\n\n\n\n(dict) --Represents a device filter used to select a set of devices to be included in a test run. This data structure is passed in as the deviceSelectionConfiguration parameter to ScheduleRun . For an example of the JSON request syntax, see ScheduleRun .\nIt is also passed in as the filters parameter to ListDevices . For an example of the JSON request syntax, see ListDevices .\n\nattribute (string) --The aspect of a device such as platform or model used as the selection criteria in a device filter.\nThe supported operators for each attribute are provided in the following list.\n\nARN\nThe Amazon Resource Name (ARN) of the device (for example, arn:aws:devicefarm:us-west-2::device:12345Example ).\nSupported operators: EQUALS , IN , NOT_IN\n\nPLATFORM\nThe device platform. Valid values are ANDROID or IOS.\nSupported operators: EQUALS\n\nOS_VERSION\nThe operating system version (for example, 10.3.2).\nSupported operators: EQUALS , GREATER_THAN , GREATER_THAN_OR_EQUALS , IN , LESS_THAN , LESS_THAN_OR_EQUALS , NOT_IN\n\nMODEL\nThe device model (for example, iPad 5th Gen).\nSupported operators: CONTAINS , EQUALS , IN , NOT_IN\n\nAVAILABILITY\nThe current availability of the device. Valid values are AVAILABLE, HIGHLY_AVAILABLE, BUSY, or TEMPORARY_NOT_AVAILABLE.\nSupported operators: EQUALS\n\nFORM_FACTOR\nThe device form factor. Valid values are PHONE or TABLET.\nSupported operators: EQUALS\n\nMANUFACTURER\nThe device manufacturer (for example, Apple).\nSupported operators: EQUALS , IN , NOT_IN\n\nREMOTE_ACCESS_ENABLED\nWhether the device is enabled for remote access. Valid values are TRUE or FALSE.\nSupported operators: EQUALS\n\nREMOTE_DEBUG_ENABLED\nWhether the device is enabled for remote debugging. Valid values are TRUE or FALSE.\nSupported operators: EQUALS\nBecause remote debugging is no longer supported , this filter is ignored.\n\nINSTANCE_ARN\nThe Amazon Resource Name (ARN) of the device instance.\nSupported operators: EQUALS , IN , NOT_IN\n\nINSTANCE_LABELS\nThe label of the device instance.\nSupported operators: CONTAINS\n\nFLEET_TYPE\nThe fleet type. Valid values are PUBLIC or PRIVATE.\nSupported operators: EQUALS\n\noperator (string) --Specifies how Device Farm compares the filter\'s attribute to the value. See the attribute descriptions.\n\nvalues (list) --An array of one or more filter values used in a device filter.\n\nOperator Values\n\nThe IN and NOT_IN operators can take a values array that has more than one element.\nThe other operators require an array with a single element.\n\n\nAttribute Values\n\nThe PLATFORM attribute can be set to ANDROID or IOS.\nThe AVAILABILITY attribute can be set to AVAILABLE, HIGHLY_AVAILABLE, BUSY, or TEMPORARY_NOT_AVAILABLE.\nThe FORM_FACTOR attribute can be set to PHONE or TABLET.\nThe FLEET_TYPE attribute can be set to PUBLIC or PRIVATE.\n\n\n(string) --\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'devices': [
        {
            'arn': 'string',
            'name': 'string',
            'manufacturer': 'string',
            'model': 'string',
            'modelId': 'string',
            'formFactor': 'PHONE'|'TABLET',
            'platform': 'ANDROID'|'IOS',
            'os': 'string',
            'cpu': {
                'frequency': 'string',
                'architecture': 'string',
                'clock': 123.0
            },
            'resolution': {
                'width': 123,
                'height': 123
            },
            'heapSize': 123,
            'memory': 123,
            'image': 'string',
            'carrier': 'string',
            'radio': 'string',
            'remoteAccessEnabled': True|False,
            'remoteDebugEnabled': True|False,
            'fleetType': 'string',
            'fleetName': 'string',
            'instances': [
                {
                    'arn': 'string',
                    'deviceArn': 'string',
                    'labels': [
                        'string',
                    ],
                    'status': 'IN_USE'|'PREPARING'|'AVAILABLE'|'NOT_AVAILABLE',
                    'udid': 'string',
                    'instanceProfile': {
                        'arn': 'string',
                        'packageCleanup': True|False,
                        'excludeAppPackagesFromCleanup': [
                            'string',
                        ],
                        'rebootAfterUse': True|False,
                        'name': 'string',
                        'description': 'string'
                    }
                },
            ],
            'availability': 'TEMPORARY_NOT_AVAILABLE'|'BUSY'|'AVAILABLE'|'HIGHLY_AVAILABLE'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --
Represents the result of a list devices operation.

devices (list) --
Information about the devices.

(dict) --
Represents a device type that an app is tested against.

arn (string) --
The device\'s ARN.

name (string) --
The device\'s display name.

manufacturer (string) --
The device\'s manufacturer name.

model (string) --
The device\'s model name.

modelId (string) --
The device\'s model ID.

formFactor (string) --
The device\'s form factor.
Allowed values include:

PHONE
TABLET


platform (string) --
The device\'s platform.
Allowed values include:

ANDROID
IOS


os (string) --
The device\'s operating system type.

cpu (dict) --
Information about the device\'s CPU.

frequency (string) --
The CPU\'s frequency.

architecture (string) --
The CPU\'s architecture (for example, x86 or ARM).

clock (float) --
The clock speed of the device\'s CPU, expressed in hertz (Hz). For example, a 1.2 GHz CPU is expressed as 1200000000.



resolution (dict) --
The resolution of the device.

width (integer) --
The screen resolution\'s width, expressed in pixels.

height (integer) --
The screen resolution\'s height, expressed in pixels.



heapSize (integer) --
The device\'s heap size, expressed in bytes.

memory (integer) --
The device\'s total memory size, expressed in bytes.

image (string) --
The device\'s image name.

carrier (string) --
The device\'s carrier.

radio (string) --
The device\'s radio.

remoteAccessEnabled (boolean) --
Specifies whether remote access has been enabled for the specified device.

remoteDebugEnabled (boolean) --
This flag is set to true if remote debugging is enabled for the device.
Remote debugging is no longer supported .

fleetType (string) --
The type of fleet to which this device belongs. Possible values are PRIVATE and PUBLIC.

fleetName (string) --
The name of the fleet to which this device belongs.

instances (list) --
The instances that belong to this device.

(dict) --
Represents the device instance.

arn (string) --
The Amazon Resource Name (ARN) of the device instance.

deviceArn (string) --
The ARN of the device.

labels (list) --
An array of strings that describe the device instance.

(string) --


status (string) --
The status of the device instance. Valid values are listed here.

udid (string) --
Unique device identifier for the device instance.

instanceProfile (dict) --
A object that contains information about the instance profile.

arn (string) --
The Amazon Resource Name (ARN) of the instance profile.

packageCleanup (boolean) --
When set to true , Device Farm removes app packages after a test run. The default value is false for private devices.

excludeAppPackagesFromCleanup (list) --
An array of strings containing the list of app packages that should not be cleaned up from the device after a test run completes.
The list of packages is considered only if you set packageCleanup to true .

(string) --


rebootAfterUse (boolean) --
When set to true , Device Farm reboots the instance after a test run. The default value is true .

name (string) --
The name of the instance profile.

description (string) --
The description of the instance profile.







availability (string) --
Indicates how likely a device is available for a test run. Currently available in the  ListDevices and GetDevice API methods.





nextToken (string) --
If the number of items that are returned is significantly large, this is an identifier that is also returned. It can be used in a subsequent call to this operation to return the next set of items in the list.







Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.LimitExceededException
DeviceFarm.Client.exceptions.ServiceAccountException

Examples
The following example returns information about the available devices in a specific project.
response = client.list_devices(
    # You can get the project ARN by using the list-projects CLI command.
    arn='arn:aws:devicefarm:us-west-2:123456789101:project:EXAMPLE-GUID-123-456',
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'devices': [
            {
                'arn': 'string',
                'name': 'string',
                'manufacturer': 'string',
                'model': 'string',
                'modelId': 'string',
                'formFactor': 'PHONE'|'TABLET',
                'platform': 'ANDROID'|'IOS',
                'os': 'string',
                'cpu': {
                    'frequency': 'string',
                    'architecture': 'string',
                    'clock': 123.0
                },
                'resolution': {
                    'width': 123,
                    'height': 123
                },
                'heapSize': 123,
                'memory': 123,
                'image': 'string',
                'carrier': 'string',
                'radio': 'string',
                'remoteAccessEnabled': True|False,
                'remoteDebugEnabled': True|False,
                'fleetType': 'string',
                'fleetName': 'string',
                'instances': [
                    {
                        'arn': 'string',
                        'deviceArn': 'string',
                        'labels': [
                            'string',
                        ],
                        'status': 'IN_USE'|'PREPARING'|'AVAILABLE'|'NOT_AVAILABLE',
                        'udid': 'string',
                        'instanceProfile': {
                            'arn': 'string',
                            'packageCleanup': True|False,
                            'excludeAppPackagesFromCleanup': [
                                'string',
                            ],
                            'rebootAfterUse': True|False,
                            'name': 'string',
                            'description': 'string'
                        }
                    },
                ],
                'availability': 'TEMPORARY_NOT_AVAILABLE'|'BUSY'|'AVAILABLE'|'HIGHLY_AVAILABLE'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    PHONE
    TABLET
    
    """
    pass

def list_instance_profiles(maxResults=None, nextToken=None):
    """
    Returns information about all the instance profiles in an AWS account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_instance_profiles(
        maxResults=123,
        nextToken='string'
    )
    
    
    :type maxResults: integer
    :param maxResults: An integer that specifies the maximum number of items you want to return in the API response.

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :rtype: dict

ReturnsResponse Syntax
{
    'instanceProfiles': [
        {
            'arn': 'string',
            'packageCleanup': True|False,
            'excludeAppPackagesFromCleanup': [
                'string',
            ],
            'rebootAfterUse': True|False,
            'name': 'string',
            'description': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

instanceProfiles (list) --
An object that contains information about your instance profiles.

(dict) --
Represents the instance profile.

arn (string) --
The Amazon Resource Name (ARN) of the instance profile.

packageCleanup (boolean) --
When set to true , Device Farm removes app packages after a test run. The default value is false for private devices.

excludeAppPackagesFromCleanup (list) --
An array of strings containing the list of app packages that should not be cleaned up from the device after a test run completes.
The list of packages is considered only if you set packageCleanup to true .

(string) --


rebootAfterUse (boolean) --
When set to true , Device Farm reboots the instance after a test run. The default value is true .

name (string) --
The name of the instance profile.

description (string) --
The description of the instance profile.





nextToken (string) --
An identifier that can be used in the next call to this operation to return the next set of items in the list.







Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.LimitExceededException
DeviceFarm.Client.exceptions.ServiceAccountException


    :return: {
        'instanceProfiles': [
            {
                'arn': 'string',
                'packageCleanup': True|False,
                'excludeAppPackagesFromCleanup': [
                    'string',
                ],
                'rebootAfterUse': True|False,
                'name': 'string',
                'description': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_jobs(arn=None, nextToken=None):
    """
    Gets information about jobs for a given test run.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example returns information about jobs in a specific project.
    Expected Output:
    
    :example: response = client.list_jobs(
        arn='string',
        nextToken='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]\nThe run\'s Amazon Resource Name (ARN).\n

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :rtype: dict

ReturnsResponse Syntax
{
    'jobs': [
        {
            'arn': 'string',
            'name': 'string',
            'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'WEB_PERFORMANCE_PROFILE'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_NODE'|'APPIUM_RUBY'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'APPIUM_WEB_NODE'|'APPIUM_WEB_RUBY'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI'|'REMOTE_ACCESS_RECORD'|'REMOTE_ACCESS_REPLAY',
            'created': datetime(2015, 1, 1),
            'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
            'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
            'started': datetime(2015, 1, 1),
            'stopped': datetime(2015, 1, 1),
            'counters': {
                'total': 123,
                'passed': 123,
                'failed': 123,
                'warned': 123,
                'errored': 123,
                'stopped': 123,
                'skipped': 123
            },
            'message': 'string',
            'device': {
                'arn': 'string',
                'name': 'string',
                'manufacturer': 'string',
                'model': 'string',
                'modelId': 'string',
                'formFactor': 'PHONE'|'TABLET',
                'platform': 'ANDROID'|'IOS',
                'os': 'string',
                'cpu': {
                    'frequency': 'string',
                    'architecture': 'string',
                    'clock': 123.0
                },
                'resolution': {
                    'width': 123,
                    'height': 123
                },
                'heapSize': 123,
                'memory': 123,
                'image': 'string',
                'carrier': 'string',
                'radio': 'string',
                'remoteAccessEnabled': True|False,
                'remoteDebugEnabled': True|False,
                'fleetType': 'string',
                'fleetName': 'string',
                'instances': [
                    {
                        'arn': 'string',
                        'deviceArn': 'string',
                        'labels': [
                            'string',
                        ],
                        'status': 'IN_USE'|'PREPARING'|'AVAILABLE'|'NOT_AVAILABLE',
                        'udid': 'string',
                        'instanceProfile': {
                            'arn': 'string',
                            'packageCleanup': True|False,
                            'excludeAppPackagesFromCleanup': [
                                'string',
                            ],
                            'rebootAfterUse': True|False,
                            'name': 'string',
                            'description': 'string'
                        }
                    },
                ],
                'availability': 'TEMPORARY_NOT_AVAILABLE'|'BUSY'|'AVAILABLE'|'HIGHLY_AVAILABLE'
            },
            'instanceArn': 'string',
            'deviceMinutes': {
                'total': 123.0,
                'metered': 123.0,
                'unmetered': 123.0
            },
            'videoEndpoint': 'string',
            'videoCapture': True|False
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --
Represents the result of a list jobs request.

jobs (list) --
Information about the jobs.

(dict) --
Represents a device.

arn (string) --
The job\'s ARN.

name (string) --
The job\'s name.

type (string) --
The job\'s type.
Allowed values include the following:

BUILTIN_FUZZ
BUILTIN_EXPLORER. For Android, an app explorer that traverses an Android app, interacting with it and capturing screenshots at the same time.
APPIUM_JAVA_JUNIT
APPIUM_JAVA_TESTNG
APPIUM_PYTHON
APPIUM_NODE
APPIUM_RUBY
APPIUM_WEB_JAVA_JUNIT
APPIUM_WEB_JAVA_TESTNG
APPIUM_WEB_PYTHON
APPIUM_WEB_NODE
APPIUM_WEB_RUBY
CALABASH
INSTRUMENTATION
UIAUTOMATION
UIAUTOMATOR
XCTEST
XCTEST_UI


created (datetime) --
When the job was created.

status (string) --
The job\'s status.
Allowed values include:

PENDING
PENDING_CONCURRENCY
PENDING_DEVICE
PROCESSING
SCHEDULING
PREPARING
RUNNING
COMPLETED
STOPPING


result (string) --
The job\'s result.
Allowed values include:

PENDING
PASSED
WARNED
FAILED
SKIPPED
ERRORED
STOPPED


started (datetime) --
The job\'s start time.

stopped (datetime) --
The job\'s stop time.

counters (dict) --
The job\'s result counters.

total (integer) --
The total number of entities.

passed (integer) --
The number of passed entities.

failed (integer) --
The number of failed entities.

warned (integer) --
The number of warned entities.

errored (integer) --
The number of errored entities.

stopped (integer) --
The number of stopped entities.

skipped (integer) --
The number of skipped entities.



message (string) --
A message about the job\'s result.

device (dict) --
The device (phone or tablet).

arn (string) --
The device\'s ARN.

name (string) --
The device\'s display name.

manufacturer (string) --
The device\'s manufacturer name.

model (string) --
The device\'s model name.

modelId (string) --
The device\'s model ID.

formFactor (string) --
The device\'s form factor.
Allowed values include:

PHONE
TABLET


platform (string) --
The device\'s platform.
Allowed values include:

ANDROID
IOS


os (string) --
The device\'s operating system type.

cpu (dict) --
Information about the device\'s CPU.

frequency (string) --
The CPU\'s frequency.

architecture (string) --
The CPU\'s architecture (for example, x86 or ARM).

clock (float) --
The clock speed of the device\'s CPU, expressed in hertz (Hz). For example, a 1.2 GHz CPU is expressed as 1200000000.



resolution (dict) --
The resolution of the device.

width (integer) --
The screen resolution\'s width, expressed in pixels.

height (integer) --
The screen resolution\'s height, expressed in pixels.



heapSize (integer) --
The device\'s heap size, expressed in bytes.

memory (integer) --
The device\'s total memory size, expressed in bytes.

image (string) --
The device\'s image name.

carrier (string) --
The device\'s carrier.

radio (string) --
The device\'s radio.

remoteAccessEnabled (boolean) --
Specifies whether remote access has been enabled for the specified device.

remoteDebugEnabled (boolean) --
This flag is set to true if remote debugging is enabled for the device.
Remote debugging is no longer supported .

fleetType (string) --
The type of fleet to which this device belongs. Possible values are PRIVATE and PUBLIC.

fleetName (string) --
The name of the fleet to which this device belongs.

instances (list) --
The instances that belong to this device.

(dict) --
Represents the device instance.

arn (string) --
The Amazon Resource Name (ARN) of the device instance.

deviceArn (string) --
The ARN of the device.

labels (list) --
An array of strings that describe the device instance.

(string) --


status (string) --
The status of the device instance. Valid values are listed here.

udid (string) --
Unique device identifier for the device instance.

instanceProfile (dict) --
A object that contains information about the instance profile.

arn (string) --
The Amazon Resource Name (ARN) of the instance profile.

packageCleanup (boolean) --
When set to true , Device Farm removes app packages after a test run. The default value is false for private devices.

excludeAppPackagesFromCleanup (list) --
An array of strings containing the list of app packages that should not be cleaned up from the device after a test run completes.
The list of packages is considered only if you set packageCleanup to true .

(string) --


rebootAfterUse (boolean) --
When set to true , Device Farm reboots the instance after a test run. The default value is true .

name (string) --
The name of the instance profile.

description (string) --
The description of the instance profile.







availability (string) --
Indicates how likely a device is available for a test run. Currently available in the  ListDevices and GetDevice API methods.



instanceArn (string) --
The ARN of the instance.

deviceMinutes (dict) --
Represents the total (metered or unmetered) minutes used by the job.

total (float) --
When specified, represents the total minutes used by the resource to run tests.

metered (float) --
When specified, represents only the sum of metered minutes used by the resource to run tests.

unmetered (float) --
When specified, represents only the sum of unmetered minutes used by the resource to run tests.



videoEndpoint (string) --
The endpoint for streaming device video.

videoCapture (boolean) --
This value is set to true if video capture is enabled. Otherwise, it is set to false.





nextToken (string) --
If the number of items that are returned is significantly large, this is an identifier that is also returned. It can be used in a subsequent call to this operation to return the next set of items in the list.







Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.LimitExceededException
DeviceFarm.Client.exceptions.ServiceAccountException

Examples
The following example returns information about jobs in a specific project.
response = client.list_jobs(
    # You can get the project ARN by using the list-jobs CLI command.
    arn='arn:aws:devicefarm:us-west-2:123456789101:project:EXAMPLE-GUID-123-456',
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'jobs': [
            {
                'arn': 'string',
                'name': 'string',
                'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'WEB_PERFORMANCE_PROFILE'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_NODE'|'APPIUM_RUBY'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'APPIUM_WEB_NODE'|'APPIUM_WEB_RUBY'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI'|'REMOTE_ACCESS_RECORD'|'REMOTE_ACCESS_REPLAY',
                'created': datetime(2015, 1, 1),
                'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
                'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
                'started': datetime(2015, 1, 1),
                'stopped': datetime(2015, 1, 1),
                'counters': {
                    'total': 123,
                    'passed': 123,
                    'failed': 123,
                    'warned': 123,
                    'errored': 123,
                    'stopped': 123,
                    'skipped': 123
                },
                'message': 'string',
                'device': {
                    'arn': 'string',
                    'name': 'string',
                    'manufacturer': 'string',
                    'model': 'string',
                    'modelId': 'string',
                    'formFactor': 'PHONE'|'TABLET',
                    'platform': 'ANDROID'|'IOS',
                    'os': 'string',
                    'cpu': {
                        'frequency': 'string',
                        'architecture': 'string',
                        'clock': 123.0
                    },
                    'resolution': {
                        'width': 123,
                        'height': 123
                    },
                    'heapSize': 123,
                    'memory': 123,
                    'image': 'string',
                    'carrier': 'string',
                    'radio': 'string',
                    'remoteAccessEnabled': True|False,
                    'remoteDebugEnabled': True|False,
                    'fleetType': 'string',
                    'fleetName': 'string',
                    'instances': [
                        {
                            'arn': 'string',
                            'deviceArn': 'string',
                            'labels': [
                                'string',
                            ],
                            'status': 'IN_USE'|'PREPARING'|'AVAILABLE'|'NOT_AVAILABLE',
                            'udid': 'string',
                            'instanceProfile': {
                                'arn': 'string',
                                'packageCleanup': True|False,
                                'excludeAppPackagesFromCleanup': [
                                    'string',
                                ],
                                'rebootAfterUse': True|False,
                                'name': 'string',
                                'description': 'string'
                            }
                        },
                    ],
                    'availability': 'TEMPORARY_NOT_AVAILABLE'|'BUSY'|'AVAILABLE'|'HIGHLY_AVAILABLE'
                },
                'instanceArn': 'string',
                'deviceMinutes': {
                    'total': 123.0,
                    'metered': 123.0,
                    'unmetered': 123.0
                },
                'videoEndpoint': 'string',
                'videoCapture': True|False
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    BUILTIN_FUZZ
    BUILTIN_EXPLORER. For Android, an app explorer that traverses an Android app, interacting with it and capturing screenshots at the same time.
    APPIUM_JAVA_JUNIT
    APPIUM_JAVA_TESTNG
    APPIUM_PYTHON
    APPIUM_NODE
    APPIUM_RUBY
    APPIUM_WEB_JAVA_JUNIT
    APPIUM_WEB_JAVA_TESTNG
    APPIUM_WEB_PYTHON
    APPIUM_WEB_NODE
    APPIUM_WEB_RUBY
    CALABASH
    INSTRUMENTATION
    UIAUTOMATION
    UIAUTOMATOR
    XCTEST
    XCTEST_UI
    
    """
    pass

def list_network_profiles(arn=None, type=None, nextToken=None):
    """
    Returns the list of available network profiles.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_network_profiles(
        arn='string',
        type='CURATED'|'PRIVATE',
        nextToken='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the project for which you want to list network profiles.\n

    :type type: string
    :param type: The type of network profile to return information about. Valid values are listed here.

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :rtype: dict

ReturnsResponse Syntax
{
    'networkProfiles': [
        {
            'arn': 'string',
            'name': 'string',
            'description': 'string',
            'type': 'CURATED'|'PRIVATE',
            'uplinkBandwidthBits': 123,
            'downlinkBandwidthBits': 123,
            'uplinkDelayMs': 123,
            'downlinkDelayMs': 123,
            'uplinkJitterMs': 123,
            'downlinkJitterMs': 123,
            'uplinkLossPercent': 123,
            'downlinkLossPercent': 123
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

networkProfiles (list) --
A list of the available network profiles.

(dict) --
An array of settings that describes characteristics of a network profile.

arn (string) --
The Amazon Resource Name (ARN) of the network profile.

name (string) --
The name of the network profile.

description (string) --
The description of the network profile.

type (string) --
The type of network profile. Valid values are listed here.

uplinkBandwidthBits (integer) --
The data throughput rate in bits per second, as an integer from 0 to 104857600.

downlinkBandwidthBits (integer) --
The data throughput rate in bits per second, as an integer from 0 to 104857600.

uplinkDelayMs (integer) --
Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.

downlinkDelayMs (integer) --
Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.

uplinkJitterMs (integer) --
Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.

downlinkJitterMs (integer) --
Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.

uplinkLossPercent (integer) --
Proportion of transmitted packets that fail to arrive from 0 to 100 percent.

downlinkLossPercent (integer) --
Proportion of received packets that fail to arrive from 0 to 100 percent.





nextToken (string) --
An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.







Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.LimitExceededException
DeviceFarm.Client.exceptions.ServiceAccountException


    :return: {
        'networkProfiles': [
            {
                'arn': 'string',
                'name': 'string',
                'description': 'string',
                'type': 'CURATED'|'PRIVATE',
                'uplinkBandwidthBits': 123,
                'downlinkBandwidthBits': 123,
                'uplinkDelayMs': 123,
                'downlinkDelayMs': 123,
                'uplinkJitterMs': 123,
                'downlinkJitterMs': 123,
                'uplinkLossPercent': 123,
                'downlinkLossPercent': 123
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    DeviceFarm.Client.exceptions.ArgumentException
    DeviceFarm.Client.exceptions.NotFoundException
    DeviceFarm.Client.exceptions.LimitExceededException
    DeviceFarm.Client.exceptions.ServiceAccountException
    
    """
    pass

def list_offering_promotions(nextToken=None):
    """
    Returns a list of offering promotions. Each offering promotion record contains the ID and description of the promotion. The API returns a NotEligible error if the caller is not permitted to invoke the operation. Contact aws-devicefarm-support@amazon.com if you must be able to invoke this operation.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_offering_promotions(
        nextToken='string'
    )
    
    
    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :rtype: dict
ReturnsResponse Syntax{
    'offeringPromotions': [
        {
            'id': 'string',
            'description': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --
offeringPromotions (list) --Information about the offering promotions.

(dict) --Represents information about an offering promotion.

id (string) --The ID of the offering promotion.

description (string) --A string that describes the offering promotion.





nextToken (string) --An identifier to be used in the next call to this operation, to return the next set of items in the list.






Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.NotEligibleException
DeviceFarm.Client.exceptions.LimitExceededException
DeviceFarm.Client.exceptions.ServiceAccountException


    :return: {
        'offeringPromotions': [
            {
                'id': 'string',
                'description': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def list_offering_transactions(nextToken=None):
    """
    Returns a list of all historical purchases, renewals, and system renewal transactions for an AWS account. The list is paginated and ordered by a descending timestamp (most recent transactions are first). The API returns a NotEligible error if the user is not permitted to invoke the operation. If you must be able to invoke this operation, contact aws-devicefarm-support@amazon.com .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example returns information about Device Farm offering transactions.
    Expected Output:
    
    :example: response = client.list_offering_transactions(
        nextToken='string'
    )
    
    
    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :rtype: dict
ReturnsResponse Syntax{
    'offeringTransactions': [
        {
            'offeringStatus': {
                'type': 'PURCHASE'|'RENEW'|'SYSTEM',
                'offering': {
                    'id': 'string',
                    'description': 'string',
                    'type': 'RECURRING',
                    'platform': 'ANDROID'|'IOS',
                    'recurringCharges': [
                        {
                            'cost': {
                                'amount': 123.0,
                                'currencyCode': 'USD'
                            },
                            'frequency': 'MONTHLY'
                        },
                    ]
                },
                'quantity': 123,
                'effectiveOn': datetime(2015, 1, 1)
            },
            'transactionId': 'string',
            'offeringPromotionId': 'string',
            'createdOn': datetime(2015, 1, 1),
            'cost': {
                'amount': 123.0,
                'currencyCode': 'USD'
            }
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --Returns the transaction log of the specified offerings.

offeringTransactions (list) --The audit log of subscriptions you have purchased and modified through AWS Device Farm.

(dict) --Represents the metadata of an offering transaction.

offeringStatus (dict) --The status of an offering transaction.

type (string) --The type specified for the offering status.

offering (dict) --Represents the metadata of an offering status.

id (string) --The ID that corresponds to a device offering.

description (string) --A string that describes the offering.

type (string) --The type of offering (for example, RECURRING ) for a device.

platform (string) --The platform of the device (for example, ANDROID or IOS ).

recurringCharges (list) --Specifies whether there are recurring charges for the offering.

(dict) --Specifies whether charges for devices are recurring.

cost (dict) --The cost of the recurring charge.

amount (float) --The numerical amount of an offering or transaction.

currencyCode (string) --The currency code of a monetary amount. For example, USD means U.S. dollars.



frequency (string) --The frequency in which charges recur.







quantity (integer) --The number of available devices in the offering.

effectiveOn (datetime) --The date on which the offering is effective.



transactionId (string) --The transaction ID of the offering transaction.

offeringPromotionId (string) --The ID that corresponds to a device offering promotion.

createdOn (datetime) --The date on which an offering transaction was created.

cost (dict) --The cost of an offering transaction.

amount (float) --The numerical amount of an offering or transaction.

currencyCode (string) --The currency code of a monetary amount. For example, USD means U.S. dollars.







nextToken (string) --An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.






Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.NotEligibleException
DeviceFarm.Client.exceptions.LimitExceededException
DeviceFarm.Client.exceptions.ServiceAccountException

Examples
The following example returns information about Device Farm offering transactions.
response = client.list_offering_transactions(
    # A dynamically generated value, used for paginating results.
    nextToken='RW5DdDJkMWYwZjM2MzM2VHVpOHJIUXlDUXlhc2QzRGViYnc9SEXAMPLE=',
)

print(response)


Expected Output:
{
    'offeringTransactions': [
        {
            'cost': {
                'amount': 0,
                'currencyCode': 'USD',
            },
            'createdOn': datetime(2016, 8, 1, 3, 17, 0, 0, 214, 0),
            'offeringStatus': {
                'type': 'RENEW',
                'effectiveOn': datetime(2016, 9, 1, 0, 0, 0, 3, 245, 0),
                'offering': {
                    'type': 'RECURRING',
                    'description': 'Android Remote Access Unmetered Device Slot',
                    'id': 'D68B3C05-1BA6-4360-BC69-12345EXAMPLE',
                    'platform': 'ANDROID',
                },
                'quantity': 0,
            },
            'transactionId': '03728003-d1ea-4851-abd6-12345EXAMPLE',
        },
        {
            'cost': {
                'amount': 250,
                'currencyCode': 'USD',
            },
            'createdOn': datetime(2016, 8, 1, 3, 17, 0, 0, 214, 0),
            'offeringStatus': {
                'type': 'PURCHASE',
                'effectiveOn': datetime(2016, 8, 1, 3, 17, 0, 0, 214, 0),
                'offering': {
                    'type': 'RECURRING',
                    'description': 'Android Remote Access Unmetered Device Slot',
                    'id': 'D68B3C05-1BA6-4360-BC69-12345EXAMPLE',
                    'platform': 'ANDROID',
                },
                'quantity': 1,
            },
            'transactionId': '56820b6e-06bd-473a-8ff8-12345EXAMPLE',
        },
        {
            'cost': {
                'amount': 175,
                'currencyCode': 'USD',
            },
            'createdOn': datetime(2016, 6, 10, 6, 2, 0, 4, 162, 0),
            'offeringStatus': {
                'type': 'PURCHASE',
                'effectiveOn': datetime(2016, 6, 10, 6, 2, 0, 4, 162, 0),
                'offering': {
                    'type': 'RECURRING',
                    'description': 'Android Unmetered Device Slot',
                    'id': '8980F81C-00D7-469D-8EC6-12345EXAMPLE',
                    'platform': 'ANDROID',
                },
                'quantity': 1,
            },
            'transactionId': '953ae2c6-d760-4a04-9597-12345EXAMPLE',
        },
        {
            'cost': {
                'amount': 8.07,
                'currencyCode': 'USD',
            },
            'createdOn': datetime(2016, 3, 30, 13, 25, 0, 2, 90, 0),
            'offeringStatus': {
                'type': 'PURCHASE',
                'effectiveOn': datetime(2016, 3, 30, 13, 25, 0, 2, 90, 0),
                'offering': {
                    'type': 'RECURRING',
                    'description': 'iOS Unmetered Device Slot',
                    'id': 'A53D4D73-A6F6-4B82-A0B0-12345EXAMPLE',
                    'platform': 'IOS',
                },
                'quantity': 1,
            },
            'transactionId': '2baf9021-ae3e-47f5-ab52-12345EXAMPLE',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'offeringTransactions': [
            {
                'offeringStatus': {
                    'type': 'PURCHASE'|'RENEW'|'SYSTEM',
                    'offering': {
                        'id': 'string',
                        'description': 'string',
                        'type': 'RECURRING',
                        'platform': 'ANDROID'|'IOS',
                        'recurringCharges': [
                            {
                                'cost': {
                                    'amount': 123.0,
                                    'currencyCode': 'USD'
                                },
                                'frequency': 'MONTHLY'
                            },
                        ]
                    },
                    'quantity': 123,
                    'effectiveOn': datetime(2015, 1, 1)
                },
                'transactionId': 'string',
                'offeringPromotionId': 'string',
                'createdOn': datetime(2015, 1, 1),
                'cost': {
                    'amount': 123.0,
                    'currencyCode': 'USD'
                }
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def list_offerings(nextToken=None):
    """
    Returns a list of products or offerings that the user can manage through the API. Each offering record indicates the recurring price per unit and the frequency for that offering. The API returns a NotEligible error if the user is not permitted to invoke the operation. If you must be able to invoke this operation, contact aws-devicefarm-support@amazon.com .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example returns information about available device offerings.
    Expected Output:
    
    :example: response = client.list_offerings(
        nextToken='string'
    )
    
    
    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :rtype: dict
ReturnsResponse Syntax{
    'offerings': [
        {
            'id': 'string',
            'description': 'string',
            'type': 'RECURRING',
            'platform': 'ANDROID'|'IOS',
            'recurringCharges': [
                {
                    'cost': {
                        'amount': 123.0,
                        'currencyCode': 'USD'
                    },
                    'frequency': 'MONTHLY'
                },
            ]
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --Represents the return values of the list of offerings.

offerings (list) --A value that represents the list offering results.

(dict) --Represents the metadata of a device offering.

id (string) --The ID that corresponds to a device offering.

description (string) --A string that describes the offering.

type (string) --The type of offering (for example, RECURRING ) for a device.

platform (string) --The platform of the device (for example, ANDROID or IOS ).

recurringCharges (list) --Specifies whether there are recurring charges for the offering.

(dict) --Specifies whether charges for devices are recurring.

cost (dict) --The cost of the recurring charge.

amount (float) --The numerical amount of an offering or transaction.

currencyCode (string) --The currency code of a monetary amount. For example, USD means U.S. dollars.



frequency (string) --The frequency in which charges recur.









nextToken (string) --An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.






Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.NotEligibleException
DeviceFarm.Client.exceptions.LimitExceededException
DeviceFarm.Client.exceptions.ServiceAccountException

Examples
The following example returns information about available device offerings.
response = client.list_offerings(
    # A dynamically generated value, used for paginating results.
    nextToken='RW5DdDJkMWYwZjM2MzM2VHVpOHJIUXlDUXlhc2QzRGViYnc9SEXAMPLE=',
)

print(response)


Expected Output:
{
    'offerings': [
        {
            'type': 'RECURRING',
            'description': 'iOS Unmetered Device Slot',
            'id': 'A53D4D73-A6F6-4B82-A0B0-12345EXAMPLE',
            'platform': 'IOS',
            'recurringCharges': [
                {
                    'cost': {
                        'amount': 250,
                        'currencyCode': 'USD',
                    },
                    'frequency': 'MONTHLY',
                },
            ],
        },
        {
            'type': 'RECURRING',
            'description': 'Android Unmetered Device Slot',
            'id': '8980F81C-00D7-469D-8EC6-12345EXAMPLE',
            'platform': 'ANDROID',
            'recurringCharges': [
                {
                    'cost': {
                        'amount': 250,
                        'currencyCode': 'USD',
                    },
                    'frequency': 'MONTHLY',
                },
            ],
        },
        {
            'type': 'RECURRING',
            'description': 'Android Remote Access Unmetered Device Slot',
            'id': 'D68B3C05-1BA6-4360-BC69-12345EXAMPLE',
            'platform': 'ANDROID',
            'recurringCharges': [
                {
                    'cost': {
                        'amount': 250,
                        'currencyCode': 'USD',
                    },
                    'frequency': 'MONTHLY',
                },
            ],
        },
        {
            'type': 'RECURRING',
            'description': 'iOS Remote Access Unmetered Device Slot',
            'id': '552B4DAD-A6C9-45C4-94FB-12345EXAMPLE',
            'platform': 'IOS',
            'recurringCharges': [
                {
                    'cost': {
                        'amount': 250,
                        'currencyCode': 'USD',
                    },
                    'frequency': 'MONTHLY',
                },
            ],
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'offerings': [
            {
                'id': 'string',
                'description': 'string',
                'type': 'RECURRING',
                'platform': 'ANDROID'|'IOS',
                'recurringCharges': [
                    {
                        'cost': {
                            'amount': 123.0,
                            'currencyCode': 'USD'
                        },
                        'frequency': 'MONTHLY'
                    },
                ]
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def list_projects(arn=None, nextToken=None):
    """
    Gets information about projects.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example returns information about the specified project in Device Farm.
    Expected Output:
    
    :example: response = client.list_projects(
        arn='string',
        nextToken='string'
    )
    
    
    :type arn: string
    :param arn: Optional. If no Amazon Resource Name (ARN) is specified, then AWS Device Farm returns a list of all projects for the AWS account. You can also specify a project ARN.

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :rtype: dict

ReturnsResponse Syntax
{
    'projects': [
        {
            'arn': 'string',
            'name': 'string',
            'defaultJobTimeoutMinutes': 123,
            'created': datetime(2015, 1, 1)
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --
Represents the result of a list projects request.

projects (list) --
Information about the projects.

(dict) --
Represents an operating-system neutral workspace for running and managing tests.

arn (string) --
The project\'s ARN.

name (string) --
The project\'s name.

defaultJobTimeoutMinutes (integer) --
The default number of minutes (at the project level) a test run executes before it times out. The default value is 150 minutes.

created (datetime) --
When the project was created.





nextToken (string) --
If the number of items that are returned is significantly large, this is an identifier that is also returned. It can be used in a subsequent call to this operation to return the next set of items in the list.







Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.LimitExceededException
DeviceFarm.Client.exceptions.ServiceAccountException

Examples
The following example returns information about the specified project in Device Farm.
response = client.list_projects(
    arn='arn:aws:devicefarm:us-west-2:123456789101:project:7ad300ed-8183-41a7-bf94-12345EXAMPLE',
    # A dynamically generated value, used for paginating results.
    nextToken='RW5DdDJkMWYwZjM2MzM2VHVpOHJIUXlDUXlhc2QzRGViYnc9SEXAMPLE',
)

print(response)


Expected Output:
{
    'projects': [
        {
            'name': 'My Test Project',
            'arn': 'arn:aws:devicefarm:us-west-2:123456789101:project:7ad300ed-8183-41a7-bf94-12345EXAMPLE',
            'created': datetime(2016, 1, 19, 0, 27, 42, 1, 19, 0),
        },
        {
            'name': 'Hello World',
            'arn': 'arn:aws:devicefarm:us-west-2:123456789101:project:d6b087d9-56db-4e44-b9ec-12345EXAMPLE',
            'created': datetime(2016, 8, 4, 22, 35, 12, 3, 217, 0),
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'projects': [
            {
                'arn': 'string',
                'name': 'string',
                'defaultJobTimeoutMinutes': 123,
                'created': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    DeviceFarm.Client.exceptions.ArgumentException
    DeviceFarm.Client.exceptions.NotFoundException
    DeviceFarm.Client.exceptions.LimitExceededException
    DeviceFarm.Client.exceptions.ServiceAccountException
    
    """
    pass

def list_remote_access_sessions(arn=None, nextToken=None):
    """
    Returns a list of all currently running remote access sessions.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example returns information about a specific Device Farm remote access session.
    Expected Output:
    
    :example: response = client.list_remote_access_sessions(
        arn='string',
        nextToken='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the project about which you are requesting information.\n

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :rtype: dict

ReturnsResponse Syntax
{
    'remoteAccessSessions': [
        {
            'arn': 'string',
            'name': 'string',
            'created': datetime(2015, 1, 1),
            'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
            'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
            'message': 'string',
            'started': datetime(2015, 1, 1),
            'stopped': datetime(2015, 1, 1),
            'device': {
                'arn': 'string',
                'name': 'string',
                'manufacturer': 'string',
                'model': 'string',
                'modelId': 'string',
                'formFactor': 'PHONE'|'TABLET',
                'platform': 'ANDROID'|'IOS',
                'os': 'string',
                'cpu': {
                    'frequency': 'string',
                    'architecture': 'string',
                    'clock': 123.0
                },
                'resolution': {
                    'width': 123,
                    'height': 123
                },
                'heapSize': 123,
                'memory': 123,
                'image': 'string',
                'carrier': 'string',
                'radio': 'string',
                'remoteAccessEnabled': True|False,
                'remoteDebugEnabled': True|False,
                'fleetType': 'string',
                'fleetName': 'string',
                'instances': [
                    {
                        'arn': 'string',
                        'deviceArn': 'string',
                        'labels': [
                            'string',
                        ],
                        'status': 'IN_USE'|'PREPARING'|'AVAILABLE'|'NOT_AVAILABLE',
                        'udid': 'string',
                        'instanceProfile': {
                            'arn': 'string',
                            'packageCleanup': True|False,
                            'excludeAppPackagesFromCleanup': [
                                'string',
                            ],
                            'rebootAfterUse': True|False,
                            'name': 'string',
                            'description': 'string'
                        }
                    },
                ],
                'availability': 'TEMPORARY_NOT_AVAILABLE'|'BUSY'|'AVAILABLE'|'HIGHLY_AVAILABLE'
            },
            'instanceArn': 'string',
            'remoteDebugEnabled': True|False,
            'remoteRecordEnabled': True|False,
            'remoteRecordAppArn': 'string',
            'hostAddress': 'string',
            'clientId': 'string',
            'billingMethod': 'METERED'|'UNMETERED',
            'deviceMinutes': {
                'total': 123.0,
                'metered': 123.0,
                'unmetered': 123.0
            },
            'endpoint': 'string',
            'deviceUdid': 'string',
            'interactionMode': 'INTERACTIVE'|'NO_VIDEO'|'VIDEO_ONLY',
            'skipAppResign': True|False
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --
Represents the response from the server after AWS Device Farm makes a request to return information about the remote access session.

remoteAccessSessions (list) --
A container that represents the metadata from the service about each remote access session you are requesting.

(dict) --
Represents information about the remote access session.

arn (string) --
The Amazon Resource Name (ARN) of the remote access session.

name (string) --
The name of the remote access session.

created (datetime) --
The date and time the remote access session was created.

status (string) --
The status of the remote access session. Can be any of the following:

PENDING.
PENDING_CONCURRENCY.
PENDING_DEVICE.
PROCESSING.
SCHEDULING.
PREPARING.
RUNNING.
COMPLETED.
STOPPING.


result (string) --
The result of the remote access session. Can be any of the following:

PENDING.
PASSED.
WARNED.
FAILED.
SKIPPED.
ERRORED.
STOPPED.


message (string) --
A message about the remote access session.

started (datetime) --
The date and time the remote access session was started.

stopped (datetime) --
The date and time the remote access session was stopped.

device (dict) --
The device (phone or tablet) used in the remote access session.

arn (string) --
The device\'s ARN.

name (string) --
The device\'s display name.

manufacturer (string) --
The device\'s manufacturer name.

model (string) --
The device\'s model name.

modelId (string) --
The device\'s model ID.

formFactor (string) --
The device\'s form factor.
Allowed values include:

PHONE
TABLET


platform (string) --
The device\'s platform.
Allowed values include:

ANDROID
IOS


os (string) --
The device\'s operating system type.

cpu (dict) --
Information about the device\'s CPU.

frequency (string) --
The CPU\'s frequency.

architecture (string) --
The CPU\'s architecture (for example, x86 or ARM).

clock (float) --
The clock speed of the device\'s CPU, expressed in hertz (Hz). For example, a 1.2 GHz CPU is expressed as 1200000000.



resolution (dict) --
The resolution of the device.

width (integer) --
The screen resolution\'s width, expressed in pixels.

height (integer) --
The screen resolution\'s height, expressed in pixels.



heapSize (integer) --
The device\'s heap size, expressed in bytes.

memory (integer) --
The device\'s total memory size, expressed in bytes.

image (string) --
The device\'s image name.

carrier (string) --
The device\'s carrier.

radio (string) --
The device\'s radio.

remoteAccessEnabled (boolean) --
Specifies whether remote access has been enabled for the specified device.

remoteDebugEnabled (boolean) --
This flag is set to true if remote debugging is enabled for the device.
Remote debugging is no longer supported .

fleetType (string) --
The type of fleet to which this device belongs. Possible values are PRIVATE and PUBLIC.

fleetName (string) --
The name of the fleet to which this device belongs.

instances (list) --
The instances that belong to this device.

(dict) --
Represents the device instance.

arn (string) --
The Amazon Resource Name (ARN) of the device instance.

deviceArn (string) --
The ARN of the device.

labels (list) --
An array of strings that describe the device instance.

(string) --


status (string) --
The status of the device instance. Valid values are listed here.

udid (string) --
Unique device identifier for the device instance.

instanceProfile (dict) --
A object that contains information about the instance profile.

arn (string) --
The Amazon Resource Name (ARN) of the instance profile.

packageCleanup (boolean) --
When set to true , Device Farm removes app packages after a test run. The default value is false for private devices.

excludeAppPackagesFromCleanup (list) --
An array of strings containing the list of app packages that should not be cleaned up from the device after a test run completes.
The list of packages is considered only if you set packageCleanup to true .

(string) --


rebootAfterUse (boolean) --
When set to true , Device Farm reboots the instance after a test run. The default value is true .

name (string) --
The name of the instance profile.

description (string) --
The description of the instance profile.







availability (string) --
Indicates how likely a device is available for a test run. Currently available in the  ListDevices and GetDevice API methods.



instanceArn (string) --
The ARN of the instance.

remoteDebugEnabled (boolean) --
This flag is set to true if remote debugging is enabled for the remote access session.
Remote debugging is no longer supported .

remoteRecordEnabled (boolean) --
This flag is set to true if remote recording is enabled for the remote access session.

remoteRecordAppArn (string) --
The ARN for the app to be recorded in the remote access session.

hostAddress (string) --
IP address of the EC2 host where you need to connect to remotely debug devices. Only returned if remote debugging is enabled for the remote access session.
Remote debugging is no longer supported .

clientId (string) --
Unique identifier of your client for the remote access session. Only returned if remote debugging is enabled for the remote access session.
Remote debugging is no longer supported .

billingMethod (string) --
The billing method of the remote access session. Possible values include METERED or UNMETERED . For more information about metered devices, see AWS Device Farm terminology .

deviceMinutes (dict) --
The number of minutes a device is used in a remote access session (including setup and teardown minutes).

total (float) --
When specified, represents the total minutes used by the resource to run tests.

metered (float) --
When specified, represents only the sum of metered minutes used by the resource to run tests.

unmetered (float) --
When specified, represents only the sum of unmetered minutes used by the resource to run tests.



endpoint (string) --
The endpoint for the remote access sesssion.

deviceUdid (string) --
Unique device identifier for the remote device. Only returned if remote debugging is enabled for the remote access session.
Remote debugging is no longer supported .

interactionMode (string) --
The interaction mode of the remote access session. Valid values are:

INTERACTIVE: You can interact with the iOS device by viewing, touching, and rotating the screen. You cannot run XCUITest framework-based tests in this mode.
NO_VIDEO: You are connected to the device, but cannot interact with it or view the screen. This mode has the fastest test execution speed. You can run XCUITest framework-based tests in this mode.
VIDEO_ONLY: You can view the screen, but cannot touch or rotate it. You can run XCUITest framework-based tests and watch the screen in this mode.


skipAppResign (boolean) --
When set to true , for private devices, Device Farm does not sign your app again. For public devices, Device Farm always signs your apps again.
For more information about how Device Farm re-signs your apps, see Do you modify my app? in the AWS Device Farm FAQs .





nextToken (string) --
An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.







Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.LimitExceededException
DeviceFarm.Client.exceptions.ServiceAccountException

Examples
The following example returns information about a specific Device Farm remote access session.
response = client.list_remote_access_sessions(
    # You can get the Amazon Resource Name (ARN) of the session by using the list-sessions CLI command.
    arn='arn:aws:devicefarm:us-west-2:123456789101:session:EXAMPLE-GUID-123-456',
    # A dynamically generated value, used for paginating results.
    nextToken='RW5DdDJkMWYwZjM2MzM2VHVpOHJIUXlDUXlhc2QzRGViYnc9SEXAMPLE=',
)

print(response)


Expected Output:
{
    'remoteAccessSessions': [
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'remoteAccessSessions': [
            {
                'arn': 'string',
                'name': 'string',
                'created': datetime(2015, 1, 1),
                'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
                'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
                'message': 'string',
                'started': datetime(2015, 1, 1),
                'stopped': datetime(2015, 1, 1),
                'device': {
                    'arn': 'string',
                    'name': 'string',
                    'manufacturer': 'string',
                    'model': 'string',
                    'modelId': 'string',
                    'formFactor': 'PHONE'|'TABLET',
                    'platform': 'ANDROID'|'IOS',
                    'os': 'string',
                    'cpu': {
                        'frequency': 'string',
                        'architecture': 'string',
                        'clock': 123.0
                    },
                    'resolution': {
                        'width': 123,
                        'height': 123
                    },
                    'heapSize': 123,
                    'memory': 123,
                    'image': 'string',
                    'carrier': 'string',
                    'radio': 'string',
                    'remoteAccessEnabled': True|False,
                    'remoteDebugEnabled': True|False,
                    'fleetType': 'string',
                    'fleetName': 'string',
                    'instances': [
                        {
                            'arn': 'string',
                            'deviceArn': 'string',
                            'labels': [
                                'string',
                            ],
                            'status': 'IN_USE'|'PREPARING'|'AVAILABLE'|'NOT_AVAILABLE',
                            'udid': 'string',
                            'instanceProfile': {
                                'arn': 'string',
                                'packageCleanup': True|False,
                                'excludeAppPackagesFromCleanup': [
                                    'string',
                                ],
                                'rebootAfterUse': True|False,
                                'name': 'string',
                                'description': 'string'
                            }
                        },
                    ],
                    'availability': 'TEMPORARY_NOT_AVAILABLE'|'BUSY'|'AVAILABLE'|'HIGHLY_AVAILABLE'
                },
                'instanceArn': 'string',
                'remoteDebugEnabled': True|False,
                'remoteRecordEnabled': True|False,
                'remoteRecordAppArn': 'string',
                'hostAddress': 'string',
                'clientId': 'string',
                'billingMethod': 'METERED'|'UNMETERED',
                'deviceMinutes': {
                    'total': 123.0,
                    'metered': 123.0,
                    'unmetered': 123.0
                },
                'endpoint': 'string',
                'deviceUdid': 'string',
                'interactionMode': 'INTERACTIVE'|'NO_VIDEO'|'VIDEO_ONLY',
                'skipAppResign': True|False
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    PENDING.
    PENDING_CONCURRENCY.
    PENDING_DEVICE.
    PROCESSING.
    SCHEDULING.
    PREPARING.
    RUNNING.
    COMPLETED.
    STOPPING.
    
    """
    pass

def list_runs(arn=None, nextToken=None):
    """
    Gets information about runs, given an AWS Device Farm project ARN.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example returns information about a specific test run.
    Expected Output:
    
    :example: response = client.list_runs(
        arn='string',
        nextToken='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the project for which you want to list runs.\n

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :rtype: dict

ReturnsResponse Syntax
{
    'runs': [
        {
            'arn': 'string',
            'name': 'string',
            'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'WEB_PERFORMANCE_PROFILE'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_NODE'|'APPIUM_RUBY'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'APPIUM_WEB_NODE'|'APPIUM_WEB_RUBY'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI'|'REMOTE_ACCESS_RECORD'|'REMOTE_ACCESS_REPLAY',
            'platform': 'ANDROID'|'IOS',
            'created': datetime(2015, 1, 1),
            'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
            'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
            'started': datetime(2015, 1, 1),
            'stopped': datetime(2015, 1, 1),
            'counters': {
                'total': 123,
                'passed': 123,
                'failed': 123,
                'warned': 123,
                'errored': 123,
                'stopped': 123,
                'skipped': 123
            },
            'message': 'string',
            'totalJobs': 123,
            'completedJobs': 123,
            'billingMethod': 'METERED'|'UNMETERED',
            'deviceMinutes': {
                'total': 123.0,
                'metered': 123.0,
                'unmetered': 123.0
            },
            'networkProfile': {
                'arn': 'string',
                'name': 'string',
                'description': 'string',
                'type': 'CURATED'|'PRIVATE',
                'uplinkBandwidthBits': 123,
                'downlinkBandwidthBits': 123,
                'uplinkDelayMs': 123,
                'downlinkDelayMs': 123,
                'uplinkJitterMs': 123,
                'downlinkJitterMs': 123,
                'uplinkLossPercent': 123,
                'downlinkLossPercent': 123
            },
            'parsingResultUrl': 'string',
            'resultCode': 'PARSING_FAILED'|'VPC_ENDPOINT_SETUP_FAILED',
            'seed': 123,
            'appUpload': 'string',
            'eventCount': 123,
            'jobTimeoutMinutes': 123,
            'devicePoolArn': 'string',
            'locale': 'string',
            'radios': {
                'wifi': True|False,
                'bluetooth': True|False,
                'nfc': True|False,
                'gps': True|False
            },
            'location': {
                'latitude': 123.0,
                'longitude': 123.0
            },
            'customerArtifactPaths': {
                'iosPaths': [
                    'string',
                ],
                'androidPaths': [
                    'string',
                ],
                'deviceHostPaths': [
                    'string',
                ]
            },
            'webUrl': 'string',
            'skipAppResign': True|False,
            'testSpecArn': 'string',
            'deviceSelectionResult': {
                'filters': [
                    {
                        'attribute': 'ARN'|'PLATFORM'|'OS_VERSION'|'MODEL'|'AVAILABILITY'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'INSTANCE_ARN'|'INSTANCE_LABELS'|'FLEET_TYPE',
                        'operator': 'EQUALS'|'LESS_THAN'|'LESS_THAN_OR_EQUALS'|'GREATER_THAN'|'GREATER_THAN_OR_EQUALS'|'IN'|'NOT_IN'|'CONTAINS',
                        'values': [
                            'string',
                        ]
                    },
                ],
                'matchedDevicesCount': 123,
                'maxDevices': 123
            }
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --
Represents the result of a list runs request.

runs (list) --
Information about the runs.

(dict) --
Represents a test run on a set of devices with a given app package, test parameters, and so on.

arn (string) --
The run\'s ARN.

name (string) --
The run\'s name.

type (string) --
The run\'s type.
Must be one of the following values:

BUILTIN_FUZZ
BUILTIN_EXPLORER


Note
For Android, an app explorer that traverses an Android app, interacting with it and capturing screenshots at the same time.


APPIUM_JAVA_JUNIT
APPIUM_JAVA_TESTNG
APPIUM_PYTHON
APPIUM_NODE
APPIUM_RUBY
APPIUM_WEB_JAVA_JUNIT
APPIUM_WEB_JAVA_TESTNG
APPIUM_WEB_PYTHON
APPIUM_WEB_NODE
APPIUM_WEB_RUBY
CALABASH
INSTRUMENTATION
UIAUTOMATION
UIAUTOMATOR
XCTEST
XCTEST_UI


platform (string) --
The run\'s platform.
Allowed values include:

ANDROID
IOS


created (datetime) --
When the run was created.

status (string) --
The run\'s status.
Allowed values include:

PENDING
PENDING_CONCURRENCY
PENDING_DEVICE
PROCESSING
SCHEDULING
PREPARING
RUNNING
COMPLETED
STOPPING


result (string) --
The run\'s result.
Allowed values include:

PENDING
PASSED
WARNED
FAILED
SKIPPED
ERRORED
STOPPED


started (datetime) --
The run\'s start time.

stopped (datetime) --
The run\'s stop time.

counters (dict) --
The run\'s result counters.

total (integer) --
The total number of entities.

passed (integer) --
The number of passed entities.

failed (integer) --
The number of failed entities.

warned (integer) --
The number of warned entities.

errored (integer) --
The number of errored entities.

stopped (integer) --
The number of stopped entities.

skipped (integer) --
The number of skipped entities.



message (string) --
A message about the run\'s result.

totalJobs (integer) --
The total number of jobs for the run.

completedJobs (integer) --
The total number of completed jobs.

billingMethod (string) --
Specifies the billing method for a test run: metered or unmetered . If the parameter is not specified, the default value is metered .

Note
If you have unmetered device slots, you must set this to unmetered to use them. Otherwise, the run is counted toward metered device minutes.


deviceMinutes (dict) --
Represents the total (metered or unmetered) minutes used by the test run.

total (float) --
When specified, represents the total minutes used by the resource to run tests.

metered (float) --
When specified, represents only the sum of metered minutes used by the resource to run tests.

unmetered (float) --
When specified, represents only the sum of unmetered minutes used by the resource to run tests.



networkProfile (dict) --
The network profile being used for a test run.

arn (string) --
The Amazon Resource Name (ARN) of the network profile.

name (string) --
The name of the network profile.

description (string) --
The description of the network profile.

type (string) --
The type of network profile. Valid values are listed here.

uplinkBandwidthBits (integer) --
The data throughput rate in bits per second, as an integer from 0 to 104857600.

downlinkBandwidthBits (integer) --
The data throughput rate in bits per second, as an integer from 0 to 104857600.

uplinkDelayMs (integer) --
Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.

downlinkDelayMs (integer) --
Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.

uplinkJitterMs (integer) --
Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.

downlinkJitterMs (integer) --
Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.

uplinkLossPercent (integer) --
Proportion of transmitted packets that fail to arrive from 0 to 100 percent.

downlinkLossPercent (integer) --
Proportion of received packets that fail to arrive from 0 to 100 percent.



parsingResultUrl (string) --
Read-only URL for an object in an S3 bucket where you can get the parsing results of the test package. If the test package doesn\'t parse, the reason why it doesn\'t parse appears in the file that this URL points to.

resultCode (string) --
Supporting field for the result field. Set only if result is SKIPPED . PARSING_FAILED if the result is skipped because of test package parsing failure.

seed (integer) --
For fuzz tests, this is a seed to use for randomizing the UI fuzz test. Using the same seed value between tests ensures identical event sequences.

appUpload (string) --
An app to upload or that has been uploaded.

eventCount (integer) --
For fuzz tests, this is the number of events, between 1 and 10000, that the UI fuzz test should perform.

jobTimeoutMinutes (integer) --
The number of minutes the job executes before it times out.

devicePoolArn (string) --
The ARN of the device pool for the run.

locale (string) --
Information about the locale that is used for the run.

radios (dict) --
Information about the radio states for the run.

wifi (boolean) --
True if Wi-Fi is enabled at the beginning of the test. Otherwise, false.

bluetooth (boolean) --
True if Bluetooth is enabled at the beginning of the test. Otherwise, false.

nfc (boolean) --
True if NFC is enabled at the beginning of the test. Otherwise, false.

gps (boolean) --
True if GPS is enabled at the beginning of the test. Otherwise, false.



location (dict) --
Information about the location that is used for the run.

latitude (float) --
The latitude.

longitude (float) --
The longitude.



customerArtifactPaths (dict) --
Output CustomerArtifactPaths object for the test run.

iosPaths (list) --
Comma-separated list of paths on the iOS device where the artifacts generated by the customer\'s tests are pulled from.

(string) --


androidPaths (list) --
Comma-separated list of paths on the Android device where the artifacts generated by the customer\'s tests are pulled from.

(string) --


deviceHostPaths (list) --
Comma-separated list of paths in the test execution environment where the artifacts generated by the customer\'s tests are pulled from.

(string) --




webUrl (string) --
The Device Farm console URL for the recording of the run.

skipAppResign (boolean) --
When set to true , for private devices, Device Farm does not sign your app again. For public devices, Device Farm always signs your apps again.
For more information about how Device Farm re-signs your apps, see Do you modify my app? in the AWS Device Farm FAQs .

testSpecArn (string) --
The ARN of the YAML-formatted test specification for the run.

deviceSelectionResult (dict) --
The results of a device filter used to select the devices for a test run.

filters (list) --
The filters in a device selection result.

(dict) --
Represents a device filter used to select a set of devices to be included in a test run. This data structure is passed in as the deviceSelectionConfiguration parameter to ScheduleRun . For an example of the JSON request syntax, see  ScheduleRun .
It is also passed in as the filters parameter to ListDevices . For an example of the JSON request syntax, see  ListDevices .

attribute (string) --
The aspect of a device such as platform or model used as the selection criteria in a device filter.
The supported operators for each attribute are provided in the following list.

ARN

The Amazon Resource Name (ARN) of the device (for example, arn:aws:devicefarm:us-west-2::device:12345Example ).
Supported operators: EQUALS , IN , NOT_IN

PLATFORM

The device platform. Valid values are ANDROID or IOS.
Supported operators: EQUALS

OS_VERSION

The operating system version (for example, 10.3.2).
Supported operators: EQUALS , GREATER_THAN , GREATER_THAN_OR_EQUALS , IN , LESS_THAN , LESS_THAN_OR_EQUALS , NOT_IN

MODEL

The device model (for example, iPad 5th Gen).
Supported operators: CONTAINS , EQUALS , IN , NOT_IN

AVAILABILITY

The current availability of the device. Valid values are AVAILABLE, HIGHLY_AVAILABLE, BUSY, or TEMPORARY_NOT_AVAILABLE.
Supported operators: EQUALS

FORM_FACTOR

The device form factor. Valid values are PHONE or TABLET.
Supported operators: EQUALS

MANUFACTURER

The device manufacturer (for example, Apple).
Supported operators: EQUALS , IN , NOT_IN

REMOTE_ACCESS_ENABLED

Whether the device is enabled for remote access. Valid values are TRUE or FALSE.
Supported operators: EQUALS

REMOTE_DEBUG_ENABLED

Whether the device is enabled for remote debugging. Valid values are TRUE or FALSE.
Supported operators: EQUALS
Because remote debugging is no longer supported , this filter is ignored.

INSTANCE_ARN

The Amazon Resource Name (ARN) of the device instance.
Supported operators: EQUALS , IN , NOT_IN

INSTANCE_LABELS

The label of the device instance.
Supported operators: CONTAINS

FLEET_TYPE

The fleet type. Valid values are PUBLIC or PRIVATE.
Supported operators: EQUALS

operator (string) --
Specifies how Device Farm compares the filter\'s attribute to the value. See the attribute descriptions.

values (list) --
An array of one or more filter values used in a device filter.

Operator Values


The IN and NOT_IN operators can take a values array that has more than one element.
The other operators require an array with a single element.


Attribute Values


The PLATFORM attribute can be set to ANDROID or IOS.
The AVAILABILITY attribute can be set to AVAILABLE, HIGHLY_AVAILABLE, BUSY, or TEMPORARY_NOT_AVAILABLE.
The FORM_FACTOR attribute can be set to PHONE or TABLET.
The FLEET_TYPE attribute can be set to PUBLIC or PRIVATE.


(string) --






matchedDevicesCount (integer) --
The number of devices that matched the device filter selection criteria.

maxDevices (integer) --
The maximum number of devices to be selected by a device filter and included in a test run.







nextToken (string) --
If the number of items that are returned is significantly large, this is an identifier that is also returned. It can be used in a subsequent call to this operation to return the next set of items in the list.







Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.LimitExceededException
DeviceFarm.Client.exceptions.ServiceAccountException

Examples
The following example returns information about a specific test run.
response = client.list_runs(
    # You can get the Amazon Resource Name (ARN) of the run by using the list-runs CLI command.
    arn='arn:aws:devicefarm:us-west-2:123456789101:run:5e01a8c7-c861-4c0a-b1d5-5ec6e6c6dd23/0fcac17b-6122-44d7-ae5a-12345EXAMPLE',
    # A dynamically generated value, used for paginating results.
    nextToken='RW5DdDJkMWYwZjM2MzM2VHVpOHJIUXlDUXlhc2QzRGViYnc9SEXAMPLE',
)

print(response)


Expected Output:
{
    'runs': [
        {
            'name': 'My Test Run',
            'type': 'BUILTIN_EXPLORER',
            'arn': 'arn:aws:devicefarm:us-west-2:123456789101:run:5e01a8c7-c861-4c0a-b1d5-5ec6e6c6dd23/0fcac17b-6122-44d7-ae5a-12345EXAMPLE',
            'billingMethod': 'METERED',
            'completedJobs': 0,
            'counters': {
                'errored': 0,
                'failed': 0,
                'passed': 0,
                'skipped': 0,
                'stopped': 0,
                'total': 0,
                'warned': 0,
            },
            'created': datetime(2016, 8, 31, 18, 18, 29, 2, 244, 0),
            'deviceMinutes': {
                'metered': 0.0,
                'total': 0.0,
                'unmetered': 0.0,
            },
            'platform': 'ANDROID',
            'result': 'PENDING',
            'status': 'RUNNING',
            'totalJobs': 3,
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'runs': [
            {
                'arn': 'string',
                'name': 'string',
                'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'WEB_PERFORMANCE_PROFILE'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_NODE'|'APPIUM_RUBY'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'APPIUM_WEB_NODE'|'APPIUM_WEB_RUBY'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI'|'REMOTE_ACCESS_RECORD'|'REMOTE_ACCESS_REPLAY',
                'platform': 'ANDROID'|'IOS',
                'created': datetime(2015, 1, 1),
                'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
                'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
                'started': datetime(2015, 1, 1),
                'stopped': datetime(2015, 1, 1),
                'counters': {
                    'total': 123,
                    'passed': 123,
                    'failed': 123,
                    'warned': 123,
                    'errored': 123,
                    'stopped': 123,
                    'skipped': 123
                },
                'message': 'string',
                'totalJobs': 123,
                'completedJobs': 123,
                'billingMethod': 'METERED'|'UNMETERED',
                'deviceMinutes': {
                    'total': 123.0,
                    'metered': 123.0,
                    'unmetered': 123.0
                },
                'networkProfile': {
                    'arn': 'string',
                    'name': 'string',
                    'description': 'string',
                    'type': 'CURATED'|'PRIVATE',
                    'uplinkBandwidthBits': 123,
                    'downlinkBandwidthBits': 123,
                    'uplinkDelayMs': 123,
                    'downlinkDelayMs': 123,
                    'uplinkJitterMs': 123,
                    'downlinkJitterMs': 123,
                    'uplinkLossPercent': 123,
                    'downlinkLossPercent': 123
                },
                'parsingResultUrl': 'string',
                'resultCode': 'PARSING_FAILED'|'VPC_ENDPOINT_SETUP_FAILED',
                'seed': 123,
                'appUpload': 'string',
                'eventCount': 123,
                'jobTimeoutMinutes': 123,
                'devicePoolArn': 'string',
                'locale': 'string',
                'radios': {
                    'wifi': True|False,
                    'bluetooth': True|False,
                    'nfc': True|False,
                    'gps': True|False
                },
                'location': {
                    'latitude': 123.0,
                    'longitude': 123.0
                },
                'customerArtifactPaths': {
                    'iosPaths': [
                        'string',
                    ],
                    'androidPaths': [
                        'string',
                    ],
                    'deviceHostPaths': [
                        'string',
                    ]
                },
                'webUrl': 'string',
                'skipAppResign': True|False,
                'testSpecArn': 'string',
                'deviceSelectionResult': {
                    'filters': [
                        {
                            'attribute': 'ARN'|'PLATFORM'|'OS_VERSION'|'MODEL'|'AVAILABILITY'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'INSTANCE_ARN'|'INSTANCE_LABELS'|'FLEET_TYPE',
                            'operator': 'EQUALS'|'LESS_THAN'|'LESS_THAN_OR_EQUALS'|'GREATER_THAN'|'GREATER_THAN_OR_EQUALS'|'IN'|'NOT_IN'|'CONTAINS',
                            'values': [
                                'string',
                            ]
                        },
                    ],
                    'matchedDevicesCount': 123,
                    'maxDevices': 123
                }
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    BUILTIN_FUZZ
    BUILTIN_EXPLORER
    
    """
    pass

def list_samples(arn=None, nextToken=None):
    """
    Gets information about samples, given an AWS Device Farm job ARN.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example returns information about samples, given a specific Device Farm project.
    Expected Output:
    
    :example: response = client.list_samples(
        arn='string',
        nextToken='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the job used to list samples.\n

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :rtype: dict

ReturnsResponse Syntax
{
    'samples': [
        {
            'arn': 'string',
            'type': 'CPU'|'MEMORY'|'THREADS'|'RX_RATE'|'TX_RATE'|'RX'|'TX'|'NATIVE_FRAMES'|'NATIVE_FPS'|'NATIVE_MIN_DRAWTIME'|'NATIVE_AVG_DRAWTIME'|'NATIVE_MAX_DRAWTIME'|'OPENGL_FRAMES'|'OPENGL_FPS'|'OPENGL_MIN_DRAWTIME'|'OPENGL_AVG_DRAWTIME'|'OPENGL_MAX_DRAWTIME',
            'url': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --
Represents the result of a list samples request.

samples (list) --
Information about the samples.

(dict) --
Represents a sample of performance data.

arn (string) --
The sample\'s ARN.

type (string) --
The sample\'s type.
Must be one of the following values:

CPU: A CPU sample type. This is expressed as the app processing CPU time (including child processes) as reported by process, as a percentage.
MEMORY: A memory usage sample type. This is expressed as the total proportional set size of an app process, in kilobytes.
NATIVE_AVG_DRAWTIME
NATIVE_FPS
NATIVE_FRAMES
NATIVE_MAX_DRAWTIME
NATIVE_MIN_DRAWTIME
OPENGL_AVG_DRAWTIME
OPENGL_FPS
OPENGL_FRAMES
OPENGL_MAX_DRAWTIME
OPENGL_MIN_DRAWTIME
RX
RX_RATE: The total number of bytes per second (TCP and UDP) that are sent, by app process.
THREADS: A threads sample type. This is expressed as the total number of threads per app process.
TX
TX_RATE: The total number of bytes per second (TCP and UDP) that are received, by app process.


url (string) --
The presigned Amazon S3 URL that can be used with a GET request to download the sample\'s file.





nextToken (string) --
If the number of items that are returned is significantly large, this is an identifier that is also returned. It can be used in a subsequent call to this operation to return the next set of items in the list.







Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.LimitExceededException
DeviceFarm.Client.exceptions.ServiceAccountException

Examples
The following example returns information about samples, given a specific Device Farm project.
response = client.list_samples(
    # You can get the Amazon Resource Name (ARN) of the project by using the list-projects CLI command.
    arn='arn:aws:devicefarm:us-west-2:123456789101:project:EXAMPLE-GUID-123-456',
    # A dynamically generated value, used for paginating results.
    nextToken='RW5DdDJkMWYwZjM2MzM2VHVpOHJIUXlDUXlhc2QzRGViYnc9SEXAMPLE',
)

print(response)


Expected Output:
{
    'samples': [
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'samples': [
            {
                'arn': 'string',
                'type': 'CPU'|'MEMORY'|'THREADS'|'RX_RATE'|'TX_RATE'|'RX'|'TX'|'NATIVE_FRAMES'|'NATIVE_FPS'|'NATIVE_MIN_DRAWTIME'|'NATIVE_AVG_DRAWTIME'|'NATIVE_MAX_DRAWTIME'|'OPENGL_FRAMES'|'OPENGL_FPS'|'OPENGL_MIN_DRAWTIME'|'OPENGL_AVG_DRAWTIME'|'OPENGL_MAX_DRAWTIME',
                'url': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    CPU: A CPU sample type. This is expressed as the app processing CPU time (including child processes) as reported by process, as a percentage.
    MEMORY: A memory usage sample type. This is expressed as the total proportional set size of an app process, in kilobytes.
    NATIVE_AVG_DRAWTIME
    NATIVE_FPS
    NATIVE_FRAMES
    NATIVE_MAX_DRAWTIME
    NATIVE_MIN_DRAWTIME
    OPENGL_AVG_DRAWTIME
    OPENGL_FPS
    OPENGL_FRAMES
    OPENGL_MAX_DRAWTIME
    OPENGL_MIN_DRAWTIME
    RX
    RX_RATE: The total number of bytes per second (TCP and UDP) that are sent, by app process.
    THREADS: A threads sample type. This is expressed as the total number of threads per app process.
    TX
    TX_RATE: The total number of bytes per second (TCP and UDP) that are received, by app process.
    
    """
    pass

def list_suites(arn=None, nextToken=None):
    """
    Gets information about test suites for a given job.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example returns information about suites, given a specific Device Farm project.
    Expected Output:
    
    :example: response = client.list_suites(
        arn='string',
        nextToken='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]\nThe job\'s Amazon Resource Name (ARN).\n

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :rtype: dict

ReturnsResponse Syntax
{
    'suites': [
        {
            'arn': 'string',
            'name': 'string',
            'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'WEB_PERFORMANCE_PROFILE'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_NODE'|'APPIUM_RUBY'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'APPIUM_WEB_NODE'|'APPIUM_WEB_RUBY'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI'|'REMOTE_ACCESS_RECORD'|'REMOTE_ACCESS_REPLAY',
            'created': datetime(2015, 1, 1),
            'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
            'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
            'started': datetime(2015, 1, 1),
            'stopped': datetime(2015, 1, 1),
            'counters': {
                'total': 123,
                'passed': 123,
                'failed': 123,
                'warned': 123,
                'errored': 123,
                'stopped': 123,
                'skipped': 123
            },
            'message': 'string',
            'deviceMinutes': {
                'total': 123.0,
                'metered': 123.0,
                'unmetered': 123.0
            }
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --
Represents the result of a list suites request.

suites (list) --
Information about the suites.

(dict) --
Represents a collection of one or more tests.

arn (string) --
The suite\'s ARN.

name (string) --
The suite\'s name.

type (string) --
The suite\'s type.
Must be one of the following values:

BUILTIN_FUZZ
BUILTIN_EXPLORER


Note
Only available for Android; an app explorer that traverses an Android app, interacting with it and capturing screenshots at the same time.


APPIUM_JAVA_JUNIT
APPIUM_JAVA_TESTNG
APPIUM_PYTHON
APPIUM_NODE
APPIUM_RUBY
APPIUM_WEB_JAVA_JUNIT
APPIUM_WEB_JAVA_TESTNG
APPIUM_WEB_PYTHON
APPIUM_WEB_NODE
APPIUM_WEB_RUBY
CALABASH
INSTRUMENTATION
UIAUTOMATION
UIAUTOMATOR
XCTEST
XCTEST_UI


created (datetime) --
When the suite was created.

status (string) --
The suite\'s status.
Allowed values include:

PENDING
PENDING_CONCURRENCY
PENDING_DEVICE
PROCESSING
SCHEDULING
PREPARING
RUNNING
COMPLETED
STOPPING


result (string) --
The suite\'s result.
Allowed values include:

PENDING
PASSED
WARNED
FAILED
SKIPPED
ERRORED
STOPPED


started (datetime) --
The suite\'s start time.

stopped (datetime) --
The suite\'s stop time.

counters (dict) --
The suite\'s result counters.

total (integer) --
The total number of entities.

passed (integer) --
The number of passed entities.

failed (integer) --
The number of failed entities.

warned (integer) --
The number of warned entities.

errored (integer) --
The number of errored entities.

stopped (integer) --
The number of stopped entities.

skipped (integer) --
The number of skipped entities.



message (string) --
A message about the suite\'s result.

deviceMinutes (dict) --
Represents the total (metered or unmetered) minutes used by the test suite.

total (float) --
When specified, represents the total minutes used by the resource to run tests.

metered (float) --
When specified, represents only the sum of metered minutes used by the resource to run tests.

unmetered (float) --
When specified, represents only the sum of unmetered minutes used by the resource to run tests.







nextToken (string) --
If the number of items that are returned is significantly large, this is an identifier that is also returned. It can be used in a subsequent call to this operation to return the next set of items in the list.







Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.LimitExceededException
DeviceFarm.Client.exceptions.ServiceAccountException

Examples
The following example returns information about suites, given a specific Device Farm project.
response = client.list_suites(
    # You can get the Amazon Resource Name (ARN) of the project by using the list-projects CLI command.
    arn='arn:aws:devicefarm:us-west-2:123456789101:project:EXAMPLE-GUID-123-456',
    # A dynamically generated value, used for paginating results.
    nextToken='RW5DdDJkMWYwZjM2MzM2VHVpOHJIUXlDUXlhc2QzRGViYnc9SEXAMPLE',
)

print(response)


Expected Output:
{
    'suites': [
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'suites': [
            {
                'arn': 'string',
                'name': 'string',
                'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'WEB_PERFORMANCE_PROFILE'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_NODE'|'APPIUM_RUBY'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'APPIUM_WEB_NODE'|'APPIUM_WEB_RUBY'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI'|'REMOTE_ACCESS_RECORD'|'REMOTE_ACCESS_REPLAY',
                'created': datetime(2015, 1, 1),
                'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
                'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
                'started': datetime(2015, 1, 1),
                'stopped': datetime(2015, 1, 1),
                'counters': {
                    'total': 123,
                    'passed': 123,
                    'failed': 123,
                    'warned': 123,
                    'errored': 123,
                    'stopped': 123,
                    'skipped': 123
                },
                'message': 'string',
                'deviceMinutes': {
                    'total': 123.0,
                    'metered': 123.0,
                    'unmetered': 123.0
                }
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    BUILTIN_FUZZ
    BUILTIN_EXPLORER
    
    """
    pass

def list_tags_for_resource(ResourceARN=None):
    """
    List the tags for an AWS Device Farm resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        ResourceARN='string'
    )
    
    
    :type ResourceARN: string
    :param ResourceARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource or resources for which to list tags. You can associate tags with the following Device Farm resources: PROJECT , RUN , NETWORK_PROFILE , INSTANCE_PROFILE , DEVICE_INSTANCE , SESSION , DEVICE_POOL , DEVICE , and VPCE_CONFIGURATION .\n

    :rtype: dict
ReturnsResponse Syntax{
    'Tags': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ]
}


Response Structure

(dict) --
Tags (list) --The tags to add to the resource. A tag is an array of key-value pairs. Tag keys can have a maximum character length of 128 characters. Tag values can have a maximum length of 256 characters.

(dict) --The metadata that you apply to a resource to help you categorize and organize it. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters. Tag values can have a maximum length of 256 characters.

Key (string) --One part of a key-value pair that makes up a tag. A key is a general label that acts like a category for more specific tag values.

Value (string) --The optional part of a key-value pair that makes up a tag. A value acts as a descriptor in a tag category (key).










Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.TagOperationException


    :return: {
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    """
    pass

def list_test_grid_projects(maxResult=None, nextToken=None):
    """
    Gets a list of all Selenium testing projects in your account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_test_grid_projects(
        maxResult=123,
        nextToken='string'
    )
    
    
    :type maxResult: integer
    :param maxResult: Return no more than this number of results.

    :type nextToken: string
    :param nextToken: From a response, used to continue a paginated listing.

    :rtype: dict

ReturnsResponse Syntax
{
    'testGridProjects': [
        {
            'arn': 'string',
            'name': 'string',
            'description': 'string',
            'created': datetime(2015, 1, 1)
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

testGridProjects (list) --
The list of TestGridProjects, based on a  ListTestGridProjectsRequest .

(dict) --
A Selenium testing project. Projects are used to collect and collate sessions.

arn (string) --
The ARN for the project.

name (string) --
A human-readable name for the project.

description (string) --
A human-readable description for the project.

created (datetime) --
When the project was created.





nextToken (string) --
Used for pagination. Pass into  ListTestGridProjects to get more results in a paginated request.







Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.InternalServiceException


    :return: {
        'testGridProjects': [
            {
                'arn': 'string',
                'name': 'string',
                'description': 'string',
                'created': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    DeviceFarm.Client.exceptions.ArgumentException
    DeviceFarm.Client.exceptions.InternalServiceException
    
    """
    pass

def list_test_grid_session_actions(sessionArn=None, maxResult=None, nextToken=None):
    """
    Returns a list of the actions taken in a  TestGridSession .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_test_grid_session_actions(
        sessionArn='string',
        maxResult=123,
        nextToken='string'
    )
    
    
    :type sessionArn: string
    :param sessionArn: [REQUIRED]\nThe ARN of the session to retrieve.\n

    :type maxResult: integer
    :param maxResult: The maximum number of sessions to return per response.

    :type nextToken: string
    :param nextToken: Pagination token.

    :rtype: dict

ReturnsResponse Syntax
{
    'actions': [
        {
            'action': 'string',
            'started': datetime(2015, 1, 1),
            'duration': 123,
            'statusCode': 'string',
            'requestMethod': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

actions (list) --
The action taken by the session.

(dict) --
An action taken by a  TestGridSession browser instance.

action (string) --
The action taken by the session.

started (datetime) --
The time that the session invoked the action.

duration (integer) --
The time, in milliseconds, that the action took to complete in the browser.

statusCode (string) --
HTTP status code returned to the browser when the action was taken.

requestMethod (string) --
HTTP method that the browser used to make the request.





nextToken (string) --
Pagination token.







Exceptions

DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.InternalServiceException


    :return: {
        'actions': [
            {
                'action': 'string',
                'started': datetime(2015, 1, 1),
                'duration': 123,
                'statusCode': 'string',
                'requestMethod': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    DeviceFarm.Client.exceptions.NotFoundException
    DeviceFarm.Client.exceptions.ArgumentException
    DeviceFarm.Client.exceptions.InternalServiceException
    
    """
    pass

def list_test_grid_session_artifacts(sessionArn=None, type=None, maxResult=None, nextToken=None):
    """
    Retrieves a list of artifacts created during the session.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_test_grid_session_artifacts(
        sessionArn='string',
        type='VIDEO'|'LOG',
        maxResult=123,
        nextToken='string'
    )
    
    
    :type sessionArn: string
    :param sessionArn: [REQUIRED]\nThe ARN of a TestGridSession .\n

    :type type: string
    :param type: Limit results to a specified type of artifact.

    :type maxResult: integer
    :param maxResult: The maximum number of results to be returned by a request.

    :type nextToken: string
    :param nextToken: Pagination token.

    :rtype: dict

ReturnsResponse Syntax
{
    'artifacts': [
        {
            'filename': 'string',
            'type': 'UNKNOWN'|'VIDEO'|'SELENIUM_LOG',
            'url': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

artifacts (list) --
A list of test grid session artifacts for a  TestGridSession .

(dict) --
Artifacts are video and other files that are produced in the process of running a browser in an automated context.

Note
Video elements might be broken up into multiple artifacts as they grow in size during creation.


filename (string) --
The file name of the artifact.

type (string) --
The kind of artifact.

url (string) --
A semi-stable URL to the content of the object.





nextToken (string) --
Pagination token.







Exceptions

DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.InternalServiceException


    :return: {
        'artifacts': [
            {
                'filename': 'string',
                'type': 'UNKNOWN'|'VIDEO'|'SELENIUM_LOG',
                'url': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    DeviceFarm.Client.exceptions.NotFoundException
    DeviceFarm.Client.exceptions.ArgumentException
    DeviceFarm.Client.exceptions.InternalServiceException
    
    """
    pass

def list_test_grid_sessions(projectArn=None, status=None, creationTimeAfter=None, creationTimeBefore=None, endTimeAfter=None, endTimeBefore=None, maxResult=None, nextToken=None):
    """
    Retrieves a list of sessions for a  TestGridProject .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_test_grid_sessions(
        projectArn='string',
        status='ACTIVE'|'CLOSED'|'ERRORED',
        creationTimeAfter=datetime(2015, 1, 1),
        creationTimeBefore=datetime(2015, 1, 1),
        endTimeAfter=datetime(2015, 1, 1),
        endTimeBefore=datetime(2015, 1, 1),
        maxResult=123,
        nextToken='string'
    )
    
    
    :type projectArn: string
    :param projectArn: [REQUIRED]\nARN of a TestGridProject .\n

    :type status: string
    :param status: Return only sessions in this state.

    :type creationTimeAfter: datetime
    :param creationTimeAfter: Return only sessions created after this time.

    :type creationTimeBefore: datetime
    :param creationTimeBefore: Return only sessions created before this time.

    :type endTimeAfter: datetime
    :param endTimeAfter: Return only sessions that ended after this time.

    :type endTimeBefore: datetime
    :param endTimeBefore: Return only sessions that ended before this time.

    :type maxResult: integer
    :param maxResult: Return only this many results at a time.

    :type nextToken: string
    :param nextToken: Pagination token.

    :rtype: dict

ReturnsResponse Syntax
{
    'testGridSessions': [
        {
            'arn': 'string',
            'status': 'ACTIVE'|'CLOSED'|'ERRORED',
            'created': datetime(2015, 1, 1),
            'ended': datetime(2015, 1, 1),
            'billingMinutes': 123.0,
            'seleniumProperties': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

testGridSessions (list) --
The sessions that match the criteria in a  ListTestGridSessionsRequest .

(dict) --
A  TestGridSession is a single instance of a browser launched from the URL provided by a call to  CreateTestGridUrl .

arn (string) --
The ARN of the session.

status (string) --
The state of the session.

created (datetime) --
The time that the session was started.

ended (datetime) --
The time the session ended.

billingMinutes (float) --
The number of billed minutes that were used for this session.

seleniumProperties (string) --
A JSON object of options and parameters passed to the Selenium WebDriver.





nextToken (string) --
Pagination token.







Exceptions

DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.InternalServiceException


    :return: {
        'testGridSessions': [
            {
                'arn': 'string',
                'status': 'ACTIVE'|'CLOSED'|'ERRORED',
                'created': datetime(2015, 1, 1),
                'ended': datetime(2015, 1, 1),
                'billingMinutes': 123.0,
                'seleniumProperties': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    DeviceFarm.Client.exceptions.NotFoundException
    DeviceFarm.Client.exceptions.ArgumentException
    DeviceFarm.Client.exceptions.InternalServiceException
    
    """
    pass

def list_tests(arn=None, nextToken=None):
    """
    Gets information about tests in a given test suite.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example returns information about tests, given a specific Device Farm project.
    Expected Output:
    
    :example: response = client.list_tests(
        arn='string',
        nextToken='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]\nThe test suite\'s Amazon Resource Name (ARN).\n

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :rtype: dict

ReturnsResponse Syntax
{
    'tests': [
        {
            'arn': 'string',
            'name': 'string',
            'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'WEB_PERFORMANCE_PROFILE'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_NODE'|'APPIUM_RUBY'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'APPIUM_WEB_NODE'|'APPIUM_WEB_RUBY'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI'|'REMOTE_ACCESS_RECORD'|'REMOTE_ACCESS_REPLAY',
            'created': datetime(2015, 1, 1),
            'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
            'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
            'started': datetime(2015, 1, 1),
            'stopped': datetime(2015, 1, 1),
            'counters': {
                'total': 123,
                'passed': 123,
                'failed': 123,
                'warned': 123,
                'errored': 123,
                'stopped': 123,
                'skipped': 123
            },
            'message': 'string',
            'deviceMinutes': {
                'total': 123.0,
                'metered': 123.0,
                'unmetered': 123.0
            }
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --
Represents the result of a list tests request.

tests (list) --
Information about the tests.

(dict) --
Represents a condition that is evaluated.

arn (string) --
The test\'s ARN.

name (string) --
The test\'s name.

type (string) --
The test\'s type.
Must be one of the following values:

BUILTIN_FUZZ
BUILTIN_EXPLORER


Note
For Android, an app explorer that traverses an Android app, interacting with it and capturing screenshots at the same time.


APPIUM_JAVA_JUNIT
APPIUM_JAVA_TESTNG
APPIUM_PYTHON
APPIUM_NODE
APPIUM_RUBY
APPIUM_WEB_JAVA_JUNIT
APPIUM_WEB_JAVA_TESTNG
APPIUM_WEB_PYTHON
APPIUM_WEB_NODE
APPIUM_WEB_RUBY
CALABASH
INSTRUMENTATION
UIAUTOMATION
UIAUTOMATOR
XCTEST
XCTEST_UI


created (datetime) --
When the test was created.

status (string) --
The test\'s status.
Allowed values include:

PENDING
PENDING_CONCURRENCY
PENDING_DEVICE
PROCESSING
SCHEDULING
PREPARING
RUNNING
COMPLETED
STOPPING


result (string) --
The test\'s result.
Allowed values include:

PENDING
PASSED
WARNED
FAILED
SKIPPED
ERRORED
STOPPED


started (datetime) --
The test\'s start time.

stopped (datetime) --
The test\'s stop time.

counters (dict) --
The test\'s result counters.

total (integer) --
The total number of entities.

passed (integer) --
The number of passed entities.

failed (integer) --
The number of failed entities.

warned (integer) --
The number of warned entities.

errored (integer) --
The number of errored entities.

stopped (integer) --
The number of stopped entities.

skipped (integer) --
The number of skipped entities.



message (string) --
A message about the test\'s result.

deviceMinutes (dict) --
Represents the total (metered or unmetered) minutes used by the test.

total (float) --
When specified, represents the total minutes used by the resource to run tests.

metered (float) --
When specified, represents only the sum of metered minutes used by the resource to run tests.

unmetered (float) --
When specified, represents only the sum of unmetered minutes used by the resource to run tests.







nextToken (string) --
If the number of items that are returned is significantly large, this is an identifier that is also returned. It can be used in a subsequent call to this operation to return the next set of items in the list.







Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.LimitExceededException
DeviceFarm.Client.exceptions.ServiceAccountException

Examples
The following example returns information about tests, given a specific Device Farm project.
response = client.list_tests(
    # You can get the Amazon Resource Name (ARN) of the project by using the list-projects CLI command.
    arn='arn:aws:devicefarm:us-west-2:123456789101:project:EXAMPLE-GUID-123-456',
    # A dynamically generated value, used for paginating results.
    nextToken='RW5DdDJkMWYwZjM2MzM2VHVpOHJIUXlDUXlhc2QzRGViYnc9SEXAMPLE',
)

print(response)


Expected Output:
{
    'tests': [
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'tests': [
            {
                'arn': 'string',
                'name': 'string',
                'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'WEB_PERFORMANCE_PROFILE'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_NODE'|'APPIUM_RUBY'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'APPIUM_WEB_NODE'|'APPIUM_WEB_RUBY'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI'|'REMOTE_ACCESS_RECORD'|'REMOTE_ACCESS_REPLAY',
                'created': datetime(2015, 1, 1),
                'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
                'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
                'started': datetime(2015, 1, 1),
                'stopped': datetime(2015, 1, 1),
                'counters': {
                    'total': 123,
                    'passed': 123,
                    'failed': 123,
                    'warned': 123,
                    'errored': 123,
                    'stopped': 123,
                    'skipped': 123
                },
                'message': 'string',
                'deviceMinutes': {
                    'total': 123.0,
                    'metered': 123.0,
                    'unmetered': 123.0
                }
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    BUILTIN_FUZZ
    BUILTIN_EXPLORER
    
    """
    pass

def list_unique_problems(arn=None, nextToken=None):
    """
    Gets information about unique problems, such as exceptions or crashes.
    Unique problems are defined as a single instance of an error across a run, job, or suite. For example, if a call in your application consistently raises an exception (OutOfBoundsException in MyActivity.java:386 ), ListUniqueProblems returns a single entry instead of many individual entries for that exception.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example returns information about unique problems, given a specific Device Farm project.
    Expected Output:
    
    :example: response = client.list_unique_problems(
        arn='string',
        nextToken='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]\nThe unique problems\' ARNs.\n

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :rtype: dict

ReturnsResponse Syntax
{
    'uniqueProblems': {
        'string': [
            {
                'message': 'string',
                'problems': [
                    {
                        'run': {
                            'arn': 'string',
                            'name': 'string'
                        },
                        'job': {
                            'arn': 'string',
                            'name': 'string'
                        },
                        'suite': {
                            'arn': 'string',
                            'name': 'string'
                        },
                        'test': {
                            'arn': 'string',
                            'name': 'string'
                        },
                        'device': {
                            'arn': 'string',
                            'name': 'string',
                            'manufacturer': 'string',
                            'model': 'string',
                            'modelId': 'string',
                            'formFactor': 'PHONE'|'TABLET',
                            'platform': 'ANDROID'|'IOS',
                            'os': 'string',
                            'cpu': {
                                'frequency': 'string',
                                'architecture': 'string',
                                'clock': 123.0
                            },
                            'resolution': {
                                'width': 123,
                                'height': 123
                            },
                            'heapSize': 123,
                            'memory': 123,
                            'image': 'string',
                            'carrier': 'string',
                            'radio': 'string',
                            'remoteAccessEnabled': True|False,
                            'remoteDebugEnabled': True|False,
                            'fleetType': 'string',
                            'fleetName': 'string',
                            'instances': [
                                {
                                    'arn': 'string',
                                    'deviceArn': 'string',
                                    'labels': [
                                        'string',
                                    ],
                                    'status': 'IN_USE'|'PREPARING'|'AVAILABLE'|'NOT_AVAILABLE',
                                    'udid': 'string',
                                    'instanceProfile': {
                                        'arn': 'string',
                                        'packageCleanup': True|False,
                                        'excludeAppPackagesFromCleanup': [
                                            'string',
                                        ],
                                        'rebootAfterUse': True|False,
                                        'name': 'string',
                                        'description': 'string'
                                    }
                                },
                            ],
                            'availability': 'TEMPORARY_NOT_AVAILABLE'|'BUSY'|'AVAILABLE'|'HIGHLY_AVAILABLE'
                        },
                        'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
                        'message': 'string'
                    },
                ]
            },
        ]
    },
    'nextToken': 'string'
}


Response Structure

(dict) --
Represents the result of a list unique problems request.

uniqueProblems (dict) --
Information about the unique problems.
Allowed values include:

PENDING
PASSED
WARNED
FAILED
SKIPPED
ERRORED
STOPPED


(string) --

(list) --

(dict) --
A collection of one or more problems, grouped by their result.

message (string) --
A message about the unique problems\' result.

problems (list) --
Information about the problems.

(dict) --
Represents a specific warning or failure.

run (dict) --
Information about the associated run.

arn (string) --
The problem detail\'s ARN.

name (string) --
The problem detail\'s name.



job (dict) --
Information about the associated job.

arn (string) --
The problem detail\'s ARN.

name (string) --
The problem detail\'s name.



suite (dict) --
Information about the associated suite.

arn (string) --
The problem detail\'s ARN.

name (string) --
The problem detail\'s name.



test (dict) --
Information about the associated test.

arn (string) --
The problem detail\'s ARN.

name (string) --
The problem detail\'s name.



device (dict) --
Information about the associated device.

arn (string) --
The device\'s ARN.

name (string) --
The device\'s display name.

manufacturer (string) --
The device\'s manufacturer name.

model (string) --
The device\'s model name.

modelId (string) --
The device\'s model ID.

formFactor (string) --
The device\'s form factor.
Allowed values include:

PHONE
TABLET


platform (string) --
The device\'s platform.
Allowed values include:

ANDROID
IOS


os (string) --
The device\'s operating system type.

cpu (dict) --
Information about the device\'s CPU.

frequency (string) --
The CPU\'s frequency.

architecture (string) --
The CPU\'s architecture (for example, x86 or ARM).

clock (float) --
The clock speed of the device\'s CPU, expressed in hertz (Hz). For example, a 1.2 GHz CPU is expressed as 1200000000.



resolution (dict) --
The resolution of the device.

width (integer) --
The screen resolution\'s width, expressed in pixels.

height (integer) --
The screen resolution\'s height, expressed in pixels.



heapSize (integer) --
The device\'s heap size, expressed in bytes.

memory (integer) --
The device\'s total memory size, expressed in bytes.

image (string) --
The device\'s image name.

carrier (string) --
The device\'s carrier.

radio (string) --
The device\'s radio.

remoteAccessEnabled (boolean) --
Specifies whether remote access has been enabled for the specified device.

remoteDebugEnabled (boolean) --
This flag is set to true if remote debugging is enabled for the device.
Remote debugging is no longer supported .

fleetType (string) --
The type of fleet to which this device belongs. Possible values are PRIVATE and PUBLIC.

fleetName (string) --
The name of the fleet to which this device belongs.

instances (list) --
The instances that belong to this device.

(dict) --
Represents the device instance.

arn (string) --
The Amazon Resource Name (ARN) of the device instance.

deviceArn (string) --
The ARN of the device.

labels (list) --
An array of strings that describe the device instance.

(string) --


status (string) --
The status of the device instance. Valid values are listed here.

udid (string) --
Unique device identifier for the device instance.

instanceProfile (dict) --
A object that contains information about the instance profile.

arn (string) --
The Amazon Resource Name (ARN) of the instance profile.

packageCleanup (boolean) --
When set to true , Device Farm removes app packages after a test run. The default value is false for private devices.

excludeAppPackagesFromCleanup (list) --
An array of strings containing the list of app packages that should not be cleaned up from the device after a test run completes.
The list of packages is considered only if you set packageCleanup to true .

(string) --


rebootAfterUse (boolean) --
When set to true , Device Farm reboots the instance after a test run. The default value is true .

name (string) --
The name of the instance profile.

description (string) --
The description of the instance profile.







availability (string) --
Indicates how likely a device is available for a test run. Currently available in the  ListDevices and GetDevice API methods.



result (string) --
The problem\'s result.
Allowed values include:

PENDING
PASSED
WARNED
FAILED
SKIPPED
ERRORED
STOPPED


message (string) --
A message about the problem\'s result.













nextToken (string) --
If the number of items that are returned is significantly large, this is an identifier that is also returned. It can be used in a subsequent call to this operation to return the next set of items in the list.







Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.LimitExceededException
DeviceFarm.Client.exceptions.ServiceAccountException

Examples
The following example returns information about unique problems, given a specific Device Farm project.
response = client.list_unique_problems(
    # You can get the Amazon Resource Name (ARN) of the project by using the list-projects CLI command.
    arn='arn:aws:devicefarm:us-west-2:123456789101:project:EXAMPLE-GUID-123-456',
    # A dynamically generated value, used for paginating results.
    nextToken='RW5DdDJkMWYwZjM2MzM2VHVpOHJIUXlDUXlhc2QzRGViYnc9SEXAMPLE',
)

print(response)


Expected Output:
{
    'uniqueProblems': {
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'uniqueProblems': {
            'string': [
                {
                    'message': 'string',
                    'problems': [
                        {
                            'run': {
                                'arn': 'string',
                                'name': 'string'
                            },
                            'job': {
                                'arn': 'string',
                                'name': 'string'
                            },
                            'suite': {
                                'arn': 'string',
                                'name': 'string'
                            },
                            'test': {
                                'arn': 'string',
                                'name': 'string'
                            },
                            'device': {
                                'arn': 'string',
                                'name': 'string',
                                'manufacturer': 'string',
                                'model': 'string',
                                'modelId': 'string',
                                'formFactor': 'PHONE'|'TABLET',
                                'platform': 'ANDROID'|'IOS',
                                'os': 'string',
                                'cpu': {
                                    'frequency': 'string',
                                    'architecture': 'string',
                                    'clock': 123.0
                                },
                                'resolution': {
                                    'width': 123,
                                    'height': 123
                                },
                                'heapSize': 123,
                                'memory': 123,
                                'image': 'string',
                                'carrier': 'string',
                                'radio': 'string',
                                'remoteAccessEnabled': True|False,
                                'remoteDebugEnabled': True|False,
                                'fleetType': 'string',
                                'fleetName': 'string',
                                'instances': [
                                    {
                                        'arn': 'string',
                                        'deviceArn': 'string',
                                        'labels': [
                                            'string',
                                        ],
                                        'status': 'IN_USE'|'PREPARING'|'AVAILABLE'|'NOT_AVAILABLE',
                                        'udid': 'string',
                                        'instanceProfile': {
                                            'arn': 'string',
                                            'packageCleanup': True|False,
                                            'excludeAppPackagesFromCleanup': [
                                                'string',
                                            ],
                                            'rebootAfterUse': True|False,
                                            'name': 'string',
                                            'description': 'string'
                                        }
                                    },
                                ],
                                'availability': 'TEMPORARY_NOT_AVAILABLE'|'BUSY'|'AVAILABLE'|'HIGHLY_AVAILABLE'
                            },
                            'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
                            'message': 'string'
                        },
                    ]
                },
            ]
        },
        'nextToken': 'string'
    }
    
    
    :returns: 
    PENDING
    PASSED
    WARNED
    FAILED
    SKIPPED
    ERRORED
    STOPPED
    
    """
    pass

def list_uploads(arn=None, type=None, nextToken=None):
    """
    Gets information about uploads, given an AWS Device Farm project ARN.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example returns information about uploads, given a specific Device Farm project.
    Expected Output:
    
    :example: response = client.list_uploads(
        arn='string',
        type='ANDROID_APP'|'IOS_APP'|'WEB_APP'|'EXTERNAL_DATA'|'APPIUM_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_PYTHON_TEST_PACKAGE'|'APPIUM_NODE_TEST_PACKAGE'|'APPIUM_RUBY_TEST_PACKAGE'|'APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_WEB_PYTHON_TEST_PACKAGE'|'APPIUM_WEB_NODE_TEST_PACKAGE'|'APPIUM_WEB_RUBY_TEST_PACKAGE'|'CALABASH_TEST_PACKAGE'|'INSTRUMENTATION_TEST_PACKAGE'|'UIAUTOMATION_TEST_PACKAGE'|'UIAUTOMATOR_TEST_PACKAGE'|'XCTEST_TEST_PACKAGE'|'XCTEST_UI_TEST_PACKAGE'|'APPIUM_JAVA_JUNIT_TEST_SPEC'|'APPIUM_JAVA_TESTNG_TEST_SPEC'|'APPIUM_PYTHON_TEST_SPEC'|'APPIUM_NODE_TEST_SPEC'|'APPIUM_RUBY_TEST_SPEC'|'APPIUM_WEB_JAVA_JUNIT_TEST_SPEC'|'APPIUM_WEB_JAVA_TESTNG_TEST_SPEC'|'APPIUM_WEB_PYTHON_TEST_SPEC'|'APPIUM_WEB_NODE_TEST_SPEC'|'APPIUM_WEB_RUBY_TEST_SPEC'|'INSTRUMENTATION_TEST_SPEC'|'XCTEST_UI_TEST_SPEC',
        nextToken='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the project for which you want to list uploads.\n

    :type type: string
    :param type: The type of upload.\nMust be one of the following values:\n\nANDROID_APP\nIOS_APP\nWEB_APP\nEXTERNAL_DATA\nAPPIUM_JAVA_JUNIT_TEST_PACKAGE\nAPPIUM_JAVA_TESTNG_TEST_PACKAGE\nAPPIUM_PYTHON_TEST_PACKAGE\nAPPIUM_NODE_TEST_PACKAGE\nAPPIUM_RUBY_TEST_PACKAGE\nAPPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE\nAPPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE\nAPPIUM_WEB_PYTHON_TEST_PACKAGE\nAPPIUM_WEB_NODE_TEST_PACKAGE\nAPPIUM_WEB_RUBY_TEST_PACKAGE\nCALABASH_TEST_PACKAGE\nINSTRUMENTATION_TEST_PACKAGE\nUIAUTOMATION_TEST_PACKAGE\nUIAUTOMATOR_TEST_PACKAGE\nXCTEST_TEST_PACKAGE\nXCTEST_UI_TEST_PACKAGE\nAPPIUM_JAVA_JUNIT_TEST_SPEC\nAPPIUM_JAVA_TESTNG_TEST_SPEC\nAPPIUM_PYTHON_TEST_SPEC\nAPPIUM_NODE_TEST_SPEC\nAPPIUM_RUBY_TEST_SPEC\nAPPIUM_WEB_JAVA_JUNIT_TEST_SPEC\nAPPIUM_WEB_JAVA_TESTNG_TEST_SPEC\nAPPIUM_WEB_PYTHON_TEST_SPEC\nAPPIUM_WEB_NODE_TEST_SPEC\nAPPIUM_WEB_RUBY_TEST_SPEC\nINSTRUMENTATION_TEST_SPEC\nXCTEST_UI_TEST_SPEC\n\n

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :rtype: dict

ReturnsResponse Syntax
{
    'uploads': [
        {
            'arn': 'string',
            'name': 'string',
            'created': datetime(2015, 1, 1),
            'type': 'ANDROID_APP'|'IOS_APP'|'WEB_APP'|'EXTERNAL_DATA'|'APPIUM_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_PYTHON_TEST_PACKAGE'|'APPIUM_NODE_TEST_PACKAGE'|'APPIUM_RUBY_TEST_PACKAGE'|'APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_WEB_PYTHON_TEST_PACKAGE'|'APPIUM_WEB_NODE_TEST_PACKAGE'|'APPIUM_WEB_RUBY_TEST_PACKAGE'|'CALABASH_TEST_PACKAGE'|'INSTRUMENTATION_TEST_PACKAGE'|'UIAUTOMATION_TEST_PACKAGE'|'UIAUTOMATOR_TEST_PACKAGE'|'XCTEST_TEST_PACKAGE'|'XCTEST_UI_TEST_PACKAGE'|'APPIUM_JAVA_JUNIT_TEST_SPEC'|'APPIUM_JAVA_TESTNG_TEST_SPEC'|'APPIUM_PYTHON_TEST_SPEC'|'APPIUM_NODE_TEST_SPEC'|'APPIUM_RUBY_TEST_SPEC'|'APPIUM_WEB_JAVA_JUNIT_TEST_SPEC'|'APPIUM_WEB_JAVA_TESTNG_TEST_SPEC'|'APPIUM_WEB_PYTHON_TEST_SPEC'|'APPIUM_WEB_NODE_TEST_SPEC'|'APPIUM_WEB_RUBY_TEST_SPEC'|'INSTRUMENTATION_TEST_SPEC'|'XCTEST_UI_TEST_SPEC',
            'status': 'INITIALIZED'|'PROCESSING'|'SUCCEEDED'|'FAILED',
            'url': 'string',
            'metadata': 'string',
            'contentType': 'string',
            'message': 'string',
            'category': 'CURATED'|'PRIVATE'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --
Represents the result of a list uploads request.

uploads (list) --
Information about the uploads.

(dict) --
An app or a set of one or more tests to upload or that have been uploaded.

arn (string) --
The upload\'s ARN.

name (string) --
The upload\'s file name.

created (datetime) --
When the upload was created.

type (string) --
The upload\'s type.
Must be one of the following values:

ANDROID_APP
IOS_APP
WEB_APP
EXTERNAL_DATA
APPIUM_JAVA_JUNIT_TEST_PACKAGE
APPIUM_JAVA_TESTNG_TEST_PACKAGE
APPIUM_PYTHON_TEST_PACKAGE
APPIUM_NODE_TEST_PACKAGE
APPIUM_RUBY_TEST_PACKAGE
APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE
APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE
APPIUM_WEB_PYTHON_TEST_PACKAGE
APPIUM_WEB_NODE_TEST_PACKAGE
APPIUM_WEB_RUBY_TEST_PACKAGE
CALABASH_TEST_PACKAGE
INSTRUMENTATION_TEST_PACKAGE
UIAUTOMATION_TEST_PACKAGE
UIAUTOMATOR_TEST_PACKAGE
XCTEST_TEST_PACKAGE
XCTEST_UI_TEST_PACKAGE
APPIUM_JAVA_JUNIT_TEST_SPEC
APPIUM_JAVA_TESTNG_TEST_SPEC
APPIUM_PYTHON_TEST_SPEC
APPIUM_NODE_TEST_SPEC
APPIUM_RUBY_TEST_SPEC
APPIUM_WEB_JAVA_JUNIT_TEST_SPEC
APPIUM_WEB_JAVA_TESTNG_TEST_SPEC
APPIUM_WEB_PYTHON_TEST_SPEC
APPIUM_WEB_NODE_TEST_SPEC
APPIUM_WEB_RUBY_TEST_SPEC
INSTRUMENTATION_TEST_SPEC
XCTEST_UI_TEST_SPEC


status (string) --
The upload\'s status.
Must be one of the following values:

FAILED
INITIALIZED
PROCESSING
SUCCEEDED


url (string) --
The presigned Amazon S3 URL that was used to store a file using a PUT request.

metadata (string) --
The upload\'s metadata. For example, for Android, this contains information that is parsed from the manifest and is displayed in the AWS Device Farm console after the associated app is uploaded.

contentType (string) --
The upload\'s content type (for example, application/octet-stream ).

message (string) --
A message about the upload\'s result.

category (string) --
The upload\'s category. Allowed values include:

CURATED: An upload managed by AWS Device Farm.
PRIVATE: An upload managed by the AWS Device Farm customer.






nextToken (string) --
If the number of items that are returned is significantly large, this is an identifier that is also returned. It can be used in a subsequent call to this operation to return the next set of items in the list.







Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.LimitExceededException
DeviceFarm.Client.exceptions.ServiceAccountException

Examples
The following example returns information about uploads, given a specific Device Farm project.
response = client.list_uploads(
    # You can get the Amazon Resource Name (ARN) of the project by using the list-projects CLI command.
    arn='arn:aws:devicefarm:us-west-2:123456789101:project:EXAMPLE-GUID-123-456',
    # A dynamically generated value, used for paginating results.
    nextToken='RW5DdDJkMWYwZjM2MzM2VHVpOHJIUXlDUXlhc2QzRGViYnc9SEXAMPLE',
)

print(response)


Expected Output:
{
    'uploads': [
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'uploads': [
            {
                'arn': 'string',
                'name': 'string',
                'created': datetime(2015, 1, 1),
                'type': 'ANDROID_APP'|'IOS_APP'|'WEB_APP'|'EXTERNAL_DATA'|'APPIUM_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_PYTHON_TEST_PACKAGE'|'APPIUM_NODE_TEST_PACKAGE'|'APPIUM_RUBY_TEST_PACKAGE'|'APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_WEB_PYTHON_TEST_PACKAGE'|'APPIUM_WEB_NODE_TEST_PACKAGE'|'APPIUM_WEB_RUBY_TEST_PACKAGE'|'CALABASH_TEST_PACKAGE'|'INSTRUMENTATION_TEST_PACKAGE'|'UIAUTOMATION_TEST_PACKAGE'|'UIAUTOMATOR_TEST_PACKAGE'|'XCTEST_TEST_PACKAGE'|'XCTEST_UI_TEST_PACKAGE'|'APPIUM_JAVA_JUNIT_TEST_SPEC'|'APPIUM_JAVA_TESTNG_TEST_SPEC'|'APPIUM_PYTHON_TEST_SPEC'|'APPIUM_NODE_TEST_SPEC'|'APPIUM_RUBY_TEST_SPEC'|'APPIUM_WEB_JAVA_JUNIT_TEST_SPEC'|'APPIUM_WEB_JAVA_TESTNG_TEST_SPEC'|'APPIUM_WEB_PYTHON_TEST_SPEC'|'APPIUM_WEB_NODE_TEST_SPEC'|'APPIUM_WEB_RUBY_TEST_SPEC'|'INSTRUMENTATION_TEST_SPEC'|'XCTEST_UI_TEST_SPEC',
                'status': 'INITIALIZED'|'PROCESSING'|'SUCCEEDED'|'FAILED',
                'url': 'string',
                'metadata': 'string',
                'contentType': 'string',
                'message': 'string',
                'category': 'CURATED'|'PRIVATE'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    ANDROID_APP
    IOS_APP
    WEB_APP
    EXTERNAL_DATA
    APPIUM_JAVA_JUNIT_TEST_PACKAGE
    APPIUM_JAVA_TESTNG_TEST_PACKAGE
    APPIUM_PYTHON_TEST_PACKAGE
    APPIUM_NODE_TEST_PACKAGE
    APPIUM_RUBY_TEST_PACKAGE
    APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE
    APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE
    APPIUM_WEB_PYTHON_TEST_PACKAGE
    APPIUM_WEB_NODE_TEST_PACKAGE
    APPIUM_WEB_RUBY_TEST_PACKAGE
    CALABASH_TEST_PACKAGE
    INSTRUMENTATION_TEST_PACKAGE
    UIAUTOMATION_TEST_PACKAGE
    UIAUTOMATOR_TEST_PACKAGE
    XCTEST_TEST_PACKAGE
    XCTEST_UI_TEST_PACKAGE
    APPIUM_JAVA_JUNIT_TEST_SPEC
    APPIUM_JAVA_TESTNG_TEST_SPEC
    APPIUM_PYTHON_TEST_SPEC
    APPIUM_NODE_TEST_SPEC
    APPIUM_RUBY_TEST_SPEC
    APPIUM_WEB_JAVA_JUNIT_TEST_SPEC
    APPIUM_WEB_JAVA_TESTNG_TEST_SPEC
    APPIUM_WEB_PYTHON_TEST_SPEC
    APPIUM_WEB_NODE_TEST_SPEC
    APPIUM_WEB_RUBY_TEST_SPEC
    INSTRUMENTATION_TEST_SPEC
    XCTEST_UI_TEST_SPEC
    
    """
    pass

def list_vpce_configurations(maxResults=None, nextToken=None):
    """
    Returns information about all Amazon Virtual Private Cloud (VPC) endpoint configurations in the AWS account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_vpce_configurations(
        maxResults=123,
        nextToken='string'
    )
    
    
    :type maxResults: integer
    :param maxResults: An integer that specifies the maximum number of items you want to return in the API response.

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :rtype: dict

ReturnsResponse Syntax
{
    'vpceConfigurations': [
        {
            'arn': 'string',
            'vpceConfigurationName': 'string',
            'vpceServiceName': 'string',
            'serviceDnsName': 'string',
            'vpceConfigurationDescription': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

vpceConfigurations (list) --
An array of VPCEConfiguration objects that contain information about your VPC endpoint configuration.

(dict) --
Represents an Amazon Virtual Private Cloud (VPC) endpoint configuration.

arn (string) --
The Amazon Resource Name (ARN) of the VPC endpoint configuration.

vpceConfigurationName (string) --
The friendly name you give to your VPC endpoint configuration to manage your configurations more easily.

vpceServiceName (string) --
The name of the VPC endpoint service running in your AWS account that you want Device Farm to test.

serviceDnsName (string) --
The DNS name that maps to the private IP address of the service you want to access.

vpceConfigurationDescription (string) --
An optional description that provides details about your VPC endpoint configuration.





nextToken (string) --
An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.







Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.ServiceAccountException


    :return: {
        'vpceConfigurations': [
            {
                'arn': 'string',
                'vpceConfigurationName': 'string',
                'vpceServiceName': 'string',
                'serviceDnsName': 'string',
                'vpceConfigurationDescription': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    DeviceFarm.Client.exceptions.ArgumentException
    DeviceFarm.Client.exceptions.ServiceAccountException
    
    """
    pass

def purchase_offering(offeringId=None, quantity=None, offeringPromotionId=None):
    """
    Immediately purchases offerings for an AWS account. Offerings renew with the latest total purchased quantity for an offering, unless the renewal was overridden. The API returns a NotEligible error if the user is not permitted to invoke the operation. If you must be able to invoke this operation, contact aws-devicefarm-support@amazon.com .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example purchases a specific device slot offering.
    Expected Output:
    
    :example: response = client.purchase_offering(
        offeringId='string',
        quantity=123,
        offeringPromotionId='string'
    )
    
    
    :type offeringId: string
    :param offeringId: The ID of the offering.

    :type quantity: integer
    :param quantity: The number of device slots to purchase in an offering request.

    :type offeringPromotionId: string
    :param offeringPromotionId: The ID of the offering promotion to be applied to the purchase.

    :rtype: dict

ReturnsResponse Syntax
{
    'offeringTransaction': {
        'offeringStatus': {
            'type': 'PURCHASE'|'RENEW'|'SYSTEM',
            'offering': {
                'id': 'string',
                'description': 'string',
                'type': 'RECURRING',
                'platform': 'ANDROID'|'IOS',
                'recurringCharges': [
                    {
                        'cost': {
                            'amount': 123.0,
                            'currencyCode': 'USD'
                        },
                        'frequency': 'MONTHLY'
                    },
                ]
            },
            'quantity': 123,
            'effectiveOn': datetime(2015, 1, 1)
        },
        'transactionId': 'string',
        'offeringPromotionId': 'string',
        'createdOn': datetime(2015, 1, 1),
        'cost': {
            'amount': 123.0,
            'currencyCode': 'USD'
        }
    }
}


Response Structure

(dict) --
The result of the purchase offering (for example, success or failure).

offeringTransaction (dict) --
Represents the offering transaction for the purchase result.

offeringStatus (dict) --
The status of an offering transaction.

type (string) --
The type specified for the offering status.

offering (dict) --
Represents the metadata of an offering status.

id (string) --
The ID that corresponds to a device offering.

description (string) --
A string that describes the offering.

type (string) --
The type of offering (for example, RECURRING ) for a device.

platform (string) --
The platform of the device (for example, ANDROID or IOS ).

recurringCharges (list) --
Specifies whether there are recurring charges for the offering.

(dict) --
Specifies whether charges for devices are recurring.

cost (dict) --
The cost of the recurring charge.

amount (float) --
The numerical amount of an offering or transaction.

currencyCode (string) --
The currency code of a monetary amount. For example, USD means U.S. dollars.



frequency (string) --
The frequency in which charges recur.







quantity (integer) --
The number of available devices in the offering.

effectiveOn (datetime) --
The date on which the offering is effective.



transactionId (string) --
The transaction ID of the offering transaction.

offeringPromotionId (string) --
The ID that corresponds to a device offering promotion.

createdOn (datetime) --
The date on which an offering transaction was created.

cost (dict) --
The cost of an offering transaction.

amount (float) --
The numerical amount of an offering or transaction.

currencyCode (string) --
The currency code of a monetary amount. For example, USD means U.S. dollars.











Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.NotEligibleException
DeviceFarm.Client.exceptions.LimitExceededException
DeviceFarm.Client.exceptions.ServiceAccountException

Examples
The following example purchases a specific device slot offering.
response = client.purchase_offering(
    # You can get the offering ID by using the list-offerings CLI command.
    offeringId='D68B3C05-1BA6-4360-BC69-12345EXAMPLE',
    quantity=1,
)

print(response)


Expected Output:
{
    'offeringTransaction': {
        'cost': {
            'amount': 8.07,
            'currencyCode': 'USD',
        },
        'createdOn': datetime(2016, 8, 31, 12, 59, 0, 2, 244, 0),
        'offeringStatus': {
            'type': 'PURCHASE',
            'effectiveOn': datetime(2016, 8, 31, 12, 59, 0, 2, 244, 0),
            'offering': {
                'type': 'RECURRING',
                'description': 'Android Remote Access Unmetered Device Slot',
                'id': 'D68B3C05-1BA6-4360-BC69-12345EXAMPLE',
                'platform': 'ANDROID',
            },
            'quantity': 1,
        },
        'transactionId': 'd30614ed-1b03-404c-9893-12345EXAMPLE',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'offeringTransaction': {
            'offeringStatus': {
                'type': 'PURCHASE'|'RENEW'|'SYSTEM',
                'offering': {
                    'id': 'string',
                    'description': 'string',
                    'type': 'RECURRING',
                    'platform': 'ANDROID'|'IOS',
                    'recurringCharges': [
                        {
                            'cost': {
                                'amount': 123.0,
                                'currencyCode': 'USD'
                            },
                            'frequency': 'MONTHLY'
                        },
                    ]
                },
                'quantity': 123,
                'effectiveOn': datetime(2015, 1, 1)
            },
            'transactionId': 'string',
            'offeringPromotionId': 'string',
            'createdOn': datetime(2015, 1, 1),
            'cost': {
                'amount': 123.0,
                'currencyCode': 'USD'
            }
        }
    }
    
    
    :returns: 
    DeviceFarm.Client.exceptions.ArgumentException
    DeviceFarm.Client.exceptions.NotFoundException
    DeviceFarm.Client.exceptions.NotEligibleException
    DeviceFarm.Client.exceptions.LimitExceededException
    DeviceFarm.Client.exceptions.ServiceAccountException
    
    """
    pass

def renew_offering(offeringId=None, quantity=None):
    """
    Explicitly sets the quantity of devices to renew for an offering, starting from the effectiveDate of the next period. The API returns a NotEligible error if the user is not permitted to invoke the operation. If you must be able to invoke this operation, contact aws-devicefarm-support@amazon.com .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example renews a specific device slot offering.
    Expected Output:
    
    :example: response = client.renew_offering(
        offeringId='string',
        quantity=123
    )
    
    
    :type offeringId: string
    :param offeringId: The ID of a request to renew an offering.

    :type quantity: integer
    :param quantity: The quantity requested in an offering renewal.

    :rtype: dict

ReturnsResponse Syntax
{
    'offeringTransaction': {
        'offeringStatus': {
            'type': 'PURCHASE'|'RENEW'|'SYSTEM',
            'offering': {
                'id': 'string',
                'description': 'string',
                'type': 'RECURRING',
                'platform': 'ANDROID'|'IOS',
                'recurringCharges': [
                    {
                        'cost': {
                            'amount': 123.0,
                            'currencyCode': 'USD'
                        },
                        'frequency': 'MONTHLY'
                    },
                ]
            },
            'quantity': 123,
            'effectiveOn': datetime(2015, 1, 1)
        },
        'transactionId': 'string',
        'offeringPromotionId': 'string',
        'createdOn': datetime(2015, 1, 1),
        'cost': {
            'amount': 123.0,
            'currencyCode': 'USD'
        }
    }
}


Response Structure

(dict) --
The result of a renewal offering.

offeringTransaction (dict) --
Represents the status of the offering transaction for the renewal.

offeringStatus (dict) --
The status of an offering transaction.

type (string) --
The type specified for the offering status.

offering (dict) --
Represents the metadata of an offering status.

id (string) --
The ID that corresponds to a device offering.

description (string) --
A string that describes the offering.

type (string) --
The type of offering (for example, RECURRING ) for a device.

platform (string) --
The platform of the device (for example, ANDROID or IOS ).

recurringCharges (list) --
Specifies whether there are recurring charges for the offering.

(dict) --
Specifies whether charges for devices are recurring.

cost (dict) --
The cost of the recurring charge.

amount (float) --
The numerical amount of an offering or transaction.

currencyCode (string) --
The currency code of a monetary amount. For example, USD means U.S. dollars.



frequency (string) --
The frequency in which charges recur.







quantity (integer) --
The number of available devices in the offering.

effectiveOn (datetime) --
The date on which the offering is effective.



transactionId (string) --
The transaction ID of the offering transaction.

offeringPromotionId (string) --
The ID that corresponds to a device offering promotion.

createdOn (datetime) --
The date on which an offering transaction was created.

cost (dict) --
The cost of an offering transaction.

amount (float) --
The numerical amount of an offering or transaction.

currencyCode (string) --
The currency code of a monetary amount. For example, USD means U.S. dollars.











Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.NotEligibleException
DeviceFarm.Client.exceptions.LimitExceededException
DeviceFarm.Client.exceptions.ServiceAccountException

Examples
The following example renews a specific device slot offering.
response = client.renew_offering(
    # You can get the offering ID by using the list-offerings CLI command.
    offeringId='D68B3C05-1BA6-4360-BC69-12345EXAMPLE',
    quantity=1,
)

print(response)


Expected Output:
{
    'offeringTransaction': {
        'cost': {
            'amount': 250,
            'currencyCode': 'USD',
        },
        'createdOn': datetime(2016, 8, 31, 13, 8, 0, 2, 244, 0),
        'offeringStatus': {
            'type': 'RENEW',
            'effectiveOn': datetime(2016, 9, 1, 0, 0, 0, 3, 245, 0),
            'offering': {
                'type': 'RECURRING',
                'description': 'Android Remote Access Unmetered Device Slot',
                'id': 'D68B3C05-1BA6-4360-BC69-12345EXAMPLE',
                'platform': 'ANDROID',
            },
            'quantity': 1,
        },
        'transactionId': 'e90f1405-8c35-4561-be43-12345EXAMPLE',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'offeringTransaction': {
            'offeringStatus': {
                'type': 'PURCHASE'|'RENEW'|'SYSTEM',
                'offering': {
                    'id': 'string',
                    'description': 'string',
                    'type': 'RECURRING',
                    'platform': 'ANDROID'|'IOS',
                    'recurringCharges': [
                        {
                            'cost': {
                                'amount': 123.0,
                                'currencyCode': 'USD'
                            },
                            'frequency': 'MONTHLY'
                        },
                    ]
                },
                'quantity': 123,
                'effectiveOn': datetime(2015, 1, 1)
            },
            'transactionId': 'string',
            'offeringPromotionId': 'string',
            'createdOn': datetime(2015, 1, 1),
            'cost': {
                'amount': 123.0,
                'currencyCode': 'USD'
            }
        }
    }
    
    
    :returns: 
    DeviceFarm.Client.exceptions.ArgumentException
    DeviceFarm.Client.exceptions.NotFoundException
    DeviceFarm.Client.exceptions.NotEligibleException
    DeviceFarm.Client.exceptions.LimitExceededException
    DeviceFarm.Client.exceptions.ServiceAccountException
    
    """
    pass

def schedule_run(projectArn=None, appArn=None, devicePoolArn=None, deviceSelectionConfiguration=None, name=None, test=None, configuration=None, executionConfiguration=None):
    """
    Schedules a run.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example schedules a test run named MyRun.
    Expected Output:
    
    :example: response = client.schedule_run(
        projectArn='string',
        appArn='string',
        devicePoolArn='string',
        deviceSelectionConfiguration={
            'filters': [
                {
                    'attribute': 'ARN'|'PLATFORM'|'OS_VERSION'|'MODEL'|'AVAILABILITY'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'INSTANCE_ARN'|'INSTANCE_LABELS'|'FLEET_TYPE',
                    'operator': 'EQUALS'|'LESS_THAN'|'LESS_THAN_OR_EQUALS'|'GREATER_THAN'|'GREATER_THAN_OR_EQUALS'|'IN'|'NOT_IN'|'CONTAINS',
                    'values': [
                        'string',
                    ]
                },
            ],
            'maxDevices': 123
        },
        name='string',
        test={
            'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'WEB_PERFORMANCE_PROFILE'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_NODE'|'APPIUM_RUBY'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'APPIUM_WEB_NODE'|'APPIUM_WEB_RUBY'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI'|'REMOTE_ACCESS_RECORD'|'REMOTE_ACCESS_REPLAY',
            'testPackageArn': 'string',
            'testSpecArn': 'string',
            'filter': 'string',
            'parameters': {
                'string': 'string'
            }
        },
        configuration={
            'extraDataPackageArn': 'string',
            'networkProfileArn': 'string',
            'locale': 'string',
            'location': {
                'latitude': 123.0,
                'longitude': 123.0
            },
            'vpceConfigurationArns': [
                'string',
            ],
            'customerArtifactPaths': {
                'iosPaths': [
                    'string',
                ],
                'androidPaths': [
                    'string',
                ],
                'deviceHostPaths': [
                    'string',
                ]
            },
            'radios': {
                'wifi': True|False,
                'bluetooth': True|False,
                'nfc': True|False,
                'gps': True|False
            },
            'auxiliaryApps': [
                'string',
            ],
            'billingMethod': 'METERED'|'UNMETERED'
        },
        executionConfiguration={
            'jobTimeoutMinutes': 123,
            'accountsCleanup': True|False,
            'appPackagesCleanup': True|False,
            'videoCapture': True|False,
            'skipAppResign': True|False
        }
    )
    
    
    :type projectArn: string
    :param projectArn: [REQUIRED]\nThe ARN of the project for the run to be scheduled.\n

    :type appArn: string
    :param appArn: The ARN of an application package to run tests against, created with CreateUpload . See ListUploads .

    :type devicePoolArn: string
    :param devicePoolArn: The ARN of the device pool for the run to be scheduled.

    :type deviceSelectionConfiguration: dict
    :param deviceSelectionConfiguration: The filter criteria used to dynamically select a set of devices for a test run and the maximum number of devices to be included in the run.\nEither ** devicePoolArn ** or ** deviceSelectionConfiguration ** is required in a request.\n\nfilters (list) -- [REQUIRED]Used to dynamically select a set of devices for a test run. A filter is made up of an attribute, an operator, and one or more values.\n\nAttribute  The aspect of a device such as platform or model used as the selection criteria in a device filter. Allowed values include:\nARN: The Amazon Resource Name (ARN) of the device (for example, arn:aws:devicefarm:us-west-2::device:12345Example ).\nPLATFORM: The device platform. Valid values are ANDROID or IOS.\nOS_VERSION: The operating system version (for example, 10.3.2).\nMODEL: The device model (for example, iPad 5th Gen).\nAVAILABILITY: The current availability of the device. Valid values are AVAILABLE, HIGHLY_AVAILABLE, BUSY, or TEMPORARY_NOT_AVAILABLE.\nFORM_FACTOR: The device form factor. Valid values are PHONE or TABLET.\nMANUFACTURER: The device manufacturer (for example, Apple).\nREMOTE_ACCESS_ENABLED: Whether the device is enabled for remote access. Valid values are TRUE or FALSE.\nREMOTE_DEBUG_ENABLED: Whether the device is enabled for remote debugging. Valid values are TRUE or FALSE. Because remote debugging is no longer supported , this filter is ignored.\nINSTANCE_ARN: The Amazon Resource Name (ARN) of the device instance.\nINSTANCE_LABELS: The label of the device instance.\nFLEET_TYPE: The fleet type. Valid values are PUBLIC or PRIVATE.\n\n\nOperator  The filter operator.\nThe EQUALS operator is available for every attribute except INSTANCE_LABELS.\nThe CONTAINS operator is available for the INSTANCE_LABELS and MODEL attributes.\nThe IN and NOT_IN operators are available for the ARN, OS_VERSION, MODEL, MANUFACTURER, and INSTANCE_ARN attributes.\nThe LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUALS, and GREATER_THAN_OR_EQUALS operators are also available for the OS_VERSION attribute.\n\n\nValues  An array of one or more filter values. Operator Values\nThe IN and NOT_IN operators can take a values array that has more than one element.\nThe other operators require an array with a single element.\n\n\n\n\nAttribute Values\n\nThe PLATFORM attribute can be set to ANDROID or IOS.\nThe AVAILABILITY attribute can be set to AVAILABLE, HIGHLY_AVAILABLE, BUSY, or TEMPORARY_NOT_AVAILABLE.\nThe FORM_FACTOR attribute can be set to PHONE or TABLET.\nThe FLEET_TYPE attribute can be set to PUBLIC or PRIVATE.\n\n\n\n\n(dict) --Represents a device filter used to select a set of devices to be included in a test run. This data structure is passed in as the deviceSelectionConfiguration parameter to ScheduleRun . For an example of the JSON request syntax, see ScheduleRun .\nIt is also passed in as the filters parameter to ListDevices . For an example of the JSON request syntax, see ListDevices .\n\nattribute (string) --The aspect of a device such as platform or model used as the selection criteria in a device filter.\nThe supported operators for each attribute are provided in the following list.\n\nARN\nThe Amazon Resource Name (ARN) of the device (for example, arn:aws:devicefarm:us-west-2::device:12345Example ).\nSupported operators: EQUALS , IN , NOT_IN\n\nPLATFORM\nThe device platform. Valid values are ANDROID or IOS.\nSupported operators: EQUALS\n\nOS_VERSION\nThe operating system version (for example, 10.3.2).\nSupported operators: EQUALS , GREATER_THAN , GREATER_THAN_OR_EQUALS , IN , LESS_THAN , LESS_THAN_OR_EQUALS , NOT_IN\n\nMODEL\nThe device model (for example, iPad 5th Gen).\nSupported operators: CONTAINS , EQUALS , IN , NOT_IN\n\nAVAILABILITY\nThe current availability of the device. Valid values are AVAILABLE, HIGHLY_AVAILABLE, BUSY, or TEMPORARY_NOT_AVAILABLE.\nSupported operators: EQUALS\n\nFORM_FACTOR\nThe device form factor. Valid values are PHONE or TABLET.\nSupported operators: EQUALS\n\nMANUFACTURER\nThe device manufacturer (for example, Apple).\nSupported operators: EQUALS , IN , NOT_IN\n\nREMOTE_ACCESS_ENABLED\nWhether the device is enabled for remote access. Valid values are TRUE or FALSE.\nSupported operators: EQUALS\n\nREMOTE_DEBUG_ENABLED\nWhether the device is enabled for remote debugging. Valid values are TRUE or FALSE.\nSupported operators: EQUALS\nBecause remote debugging is no longer supported , this filter is ignored.\n\nINSTANCE_ARN\nThe Amazon Resource Name (ARN) of the device instance.\nSupported operators: EQUALS , IN , NOT_IN\n\nINSTANCE_LABELS\nThe label of the device instance.\nSupported operators: CONTAINS\n\nFLEET_TYPE\nThe fleet type. Valid values are PUBLIC or PRIVATE.\nSupported operators: EQUALS\n\noperator (string) --Specifies how Device Farm compares the filter\'s attribute to the value. See the attribute descriptions.\n\nvalues (list) --An array of one or more filter values used in a device filter.\n\nOperator Values\n\nThe IN and NOT_IN operators can take a values array that has more than one element.\nThe other operators require an array with a single element.\n\n\nAttribute Values\n\nThe PLATFORM attribute can be set to ANDROID or IOS.\nThe AVAILABILITY attribute can be set to AVAILABLE, HIGHLY_AVAILABLE, BUSY, or TEMPORARY_NOT_AVAILABLE.\nThe FORM_FACTOR attribute can be set to PHONE or TABLET.\nThe FLEET_TYPE attribute can be set to PUBLIC or PRIVATE.\n\n\n(string) --\n\n\n\n\n\n\nmaxDevices (integer) -- [REQUIRED]The maximum number of devices to be included in a test run.\n\n\n

    :type name: string
    :param name: The name for the run to be scheduled.

    :type test: dict
    :param test: [REQUIRED]\nInformation about the test for the run to be scheduled.\n\ntype (string) -- [REQUIRED]The test\'s type.\nMust be one of the following values:\n\nBUILTIN_FUZZ\nBUILTIN_EXPLORER. For Android, an app explorer that traverses an Android app, interacting with it and capturing screenshots at the same time.\nAPPIUM_JAVA_JUNIT\nAPPIUM_JAVA_TESTNG\nAPPIUM_PYTHON\nAPPIUM_NODE\nAPPIUM_RUBY\nAPPIUM_WEB_JAVA_JUNIT\nAPPIUM_WEB_JAVA_TESTNG\nAPPIUM_WEB_PYTHON\nAPPIUM_WEB_NODE\nAPPIUM_WEB_RUBY\nCALABASH\nINSTRUMENTATION\nUIAUTOMATION\nUIAUTOMATOR\nXCTEST\nXCTEST_UI\n\n\ntestPackageArn (string) --The ARN of the uploaded test to be run.\n\ntestSpecArn (string) --The ARN of the YAML-formatted test specification.\n\nfilter (string) --The test\'s filter.\n\nparameters (dict) --The test\'s parameters, such as test framework parameters and fixture settings. Parameters are represented by name-value pairs of strings.\nFor all tests:\n\napp_performance_monitoring : Performance monitoring is enabled by default. Set this parameter to false to disable it.\n\nFor Calabash tests:\n\nprofile: A cucumber profile (for example, my_profile_name ).\ntags: You can limit execution to features or scenarios that have (or don\'t have) certain tags (for example, @smoke or @smoke,~@wip).\n\nFor Appium tests (all types):\n\nappium_version: The Appium version. Currently supported values are 1.6.5 (and later), latest, and default.\nlatest runs the latest Appium version supported by Device Farm (1.9.1).\nFor default, Device Farm selects a compatible version of Appium for the device. The current behavior is to run 1.7.2 on Android devices and iOS 9 and earlier and 1.7.2 for iOS 10 and later.\nThis behavior is subject to change.\n\n\n\nFor fuzz tests (Android only):\n\nevent_count: The number of events, between 1 and 10000, that the UI fuzz test should perform.\nthrottle: The time, in ms, between 0 and 1000, that the UI fuzz test should wait between events.\nseed: A seed to use for randomizing the UI fuzz test. Using the same seed value between tests ensures identical event sequences.\n\nFor Explorer tests:\n\nusername: A user name to use if the Explorer encounters a login form. If not supplied, no user name is inserted.\npassword: A password to use if the Explorer encounters a login form. If not supplied, no password is inserted.\n\nFor Instrumentation:\n\nfilter: A test filter string. Examples:\nRunning a single test case: com.android.abc.Test1\nRunning a single test: com.android.abc.Test1#smoke\nRunning multiple tests: com.android.abc.Test1,com.android.abc.Test2\n\n\n\nFor XCTest and XCTestUI:\n\nfilter: A test filter string. Examples:\nRunning a single test class: LoginTests\nRunning a multiple test classes: LoginTests,SmokeTests\nRunning a single test: LoginTests/testValid\nRunning multiple tests: LoginTests/testValid,LoginTests/testInvalid\n\n\n\nFor UIAutomator:\n\nfilter: A test filter string. Examples:\nRunning a single test case: com.android.abc.Test1\nRunning a single test: com.android.abc.Test1#smoke\nRunning multiple tests: com.android.abc.Test1,com.android.abc.Test2\n\n\n\n\n(string) --\n(string) --\n\n\n\n\n\n

    :type configuration: dict
    :param configuration: Information about the settings for the run to be scheduled.\n\nextraDataPackageArn (string) --The ARN of the extra data for the run. The extra data is a .zip file that AWS Device Farm extracts to external data for Android or the app\'s sandbox for iOS.\n\nnetworkProfileArn (string) --Reserved for internal use.\n\nlocale (string) --Information about the locale that is used for the run.\n\nlocation (dict) --Information about the location that is used for the run.\n\nlatitude (float) -- [REQUIRED]The latitude.\n\nlongitude (float) -- [REQUIRED]The longitude.\n\n\n\nvpceConfigurationArns (list) --An array of ARNs for your VPC endpoint configurations.\n\n(string) --\n\n\ncustomerArtifactPaths (dict) --Input CustomerArtifactPaths object for the scheduled run configuration.\n\niosPaths (list) --Comma-separated list of paths on the iOS device where the artifacts generated by the customer\'s tests are pulled from.\n\n(string) --\n\n\nandroidPaths (list) --Comma-separated list of paths on the Android device where the artifacts generated by the customer\'s tests are pulled from.\n\n(string) --\n\n\ndeviceHostPaths (list) --Comma-separated list of paths in the test execution environment where the artifacts generated by the customer\'s tests are pulled from.\n\n(string) --\n\n\n\n\nradios (dict) --Information about the radio states for the run.\n\nwifi (boolean) --True if Wi-Fi is enabled at the beginning of the test. Otherwise, false.\n\nbluetooth (boolean) --True if Bluetooth is enabled at the beginning of the test. Otherwise, false.\n\nnfc (boolean) --True if NFC is enabled at the beginning of the test. Otherwise, false.\n\ngps (boolean) --True if GPS is enabled at the beginning of the test. Otherwise, false.\n\n\n\nauxiliaryApps (list) --A list of upload ARNs for app packages to be installed with your app.\n\n(string) --\n\n\nbillingMethod (string) --Specifies the billing method for a test run: metered or unmetered . If the parameter is not specified, the default value is metered .\n\nNote\nIf you have purchased unmetered device slots, you must set this parameter to unmetered to make use of them. Otherwise, your run counts against your metered time.\n\n\n\n

    :type executionConfiguration: dict
    :param executionConfiguration: Specifies configuration information about a test run, such as the execution timeout (in minutes).\n\njobTimeoutMinutes (integer) --The number of minutes a test run executes before it times out.\n\naccountsCleanup (boolean) --True if account cleanup is enabled at the beginning of the test. Otherwise, false.\n\nappPackagesCleanup (boolean) --True if app package cleanup is enabled at the beginning of the test. Otherwise, false.\n\nvideoCapture (boolean) --Set to true to enable video capture. Otherwise, set to false. The default is true.\n\nskipAppResign (boolean) --When set to true , for private devices, Device Farm does not sign your app again. For public devices, Device Farm always signs your apps again.\nFor more information about how Device Farm re-signs your apps, see Do you modify my app? in the AWS Device Farm FAQs .\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'run': {
        'arn': 'string',
        'name': 'string',
        'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'WEB_PERFORMANCE_PROFILE'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_NODE'|'APPIUM_RUBY'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'APPIUM_WEB_NODE'|'APPIUM_WEB_RUBY'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI'|'REMOTE_ACCESS_RECORD'|'REMOTE_ACCESS_REPLAY',
        'platform': 'ANDROID'|'IOS',
        'created': datetime(2015, 1, 1),
        'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
        'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
        'started': datetime(2015, 1, 1),
        'stopped': datetime(2015, 1, 1),
        'counters': {
            'total': 123,
            'passed': 123,
            'failed': 123,
            'warned': 123,
            'errored': 123,
            'stopped': 123,
            'skipped': 123
        },
        'message': 'string',
        'totalJobs': 123,
        'completedJobs': 123,
        'billingMethod': 'METERED'|'UNMETERED',
        'deviceMinutes': {
            'total': 123.0,
            'metered': 123.0,
            'unmetered': 123.0
        },
        'networkProfile': {
            'arn': 'string',
            'name': 'string',
            'description': 'string',
            'type': 'CURATED'|'PRIVATE',
            'uplinkBandwidthBits': 123,
            'downlinkBandwidthBits': 123,
            'uplinkDelayMs': 123,
            'downlinkDelayMs': 123,
            'uplinkJitterMs': 123,
            'downlinkJitterMs': 123,
            'uplinkLossPercent': 123,
            'downlinkLossPercent': 123
        },
        'parsingResultUrl': 'string',
        'resultCode': 'PARSING_FAILED'|'VPC_ENDPOINT_SETUP_FAILED',
        'seed': 123,
        'appUpload': 'string',
        'eventCount': 123,
        'jobTimeoutMinutes': 123,
        'devicePoolArn': 'string',
        'locale': 'string',
        'radios': {
            'wifi': True|False,
            'bluetooth': True|False,
            'nfc': True|False,
            'gps': True|False
        },
        'location': {
            'latitude': 123.0,
            'longitude': 123.0
        },
        'customerArtifactPaths': {
            'iosPaths': [
                'string',
            ],
            'androidPaths': [
                'string',
            ],
            'deviceHostPaths': [
                'string',
            ]
        },
        'webUrl': 'string',
        'skipAppResign': True|False,
        'testSpecArn': 'string',
        'deviceSelectionResult': {
            'filters': [
                {
                    'attribute': 'ARN'|'PLATFORM'|'OS_VERSION'|'MODEL'|'AVAILABILITY'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'INSTANCE_ARN'|'INSTANCE_LABELS'|'FLEET_TYPE',
                    'operator': 'EQUALS'|'LESS_THAN'|'LESS_THAN_OR_EQUALS'|'GREATER_THAN'|'GREATER_THAN_OR_EQUALS'|'IN'|'NOT_IN'|'CONTAINS',
                    'values': [
                        'string',
                    ]
                },
            ],
            'matchedDevicesCount': 123,
            'maxDevices': 123
        }
    }
}


Response Structure

(dict) --
Represents the result of a schedule run request.

run (dict) --
Information about the scheduled run.

arn (string) --
The run\'s ARN.

name (string) --
The run\'s name.

type (string) --
The run\'s type.
Must be one of the following values:

BUILTIN_FUZZ
BUILTIN_EXPLORER


Note
For Android, an app explorer that traverses an Android app, interacting with it and capturing screenshots at the same time.


APPIUM_JAVA_JUNIT
APPIUM_JAVA_TESTNG
APPIUM_PYTHON
APPIUM_NODE
APPIUM_RUBY
APPIUM_WEB_JAVA_JUNIT
APPIUM_WEB_JAVA_TESTNG
APPIUM_WEB_PYTHON
APPIUM_WEB_NODE
APPIUM_WEB_RUBY
CALABASH
INSTRUMENTATION
UIAUTOMATION
UIAUTOMATOR
XCTEST
XCTEST_UI


platform (string) --
The run\'s platform.
Allowed values include:

ANDROID
IOS


created (datetime) --
When the run was created.

status (string) --
The run\'s status.
Allowed values include:

PENDING
PENDING_CONCURRENCY
PENDING_DEVICE
PROCESSING
SCHEDULING
PREPARING
RUNNING
COMPLETED
STOPPING


result (string) --
The run\'s result.
Allowed values include:

PENDING
PASSED
WARNED
FAILED
SKIPPED
ERRORED
STOPPED


started (datetime) --
The run\'s start time.

stopped (datetime) --
The run\'s stop time.

counters (dict) --
The run\'s result counters.

total (integer) --
The total number of entities.

passed (integer) --
The number of passed entities.

failed (integer) --
The number of failed entities.

warned (integer) --
The number of warned entities.

errored (integer) --
The number of errored entities.

stopped (integer) --
The number of stopped entities.

skipped (integer) --
The number of skipped entities.



message (string) --
A message about the run\'s result.

totalJobs (integer) --
The total number of jobs for the run.

completedJobs (integer) --
The total number of completed jobs.

billingMethod (string) --
Specifies the billing method for a test run: metered or unmetered . If the parameter is not specified, the default value is metered .

Note
If you have unmetered device slots, you must set this to unmetered to use them. Otherwise, the run is counted toward metered device minutes.


deviceMinutes (dict) --
Represents the total (metered or unmetered) minutes used by the test run.

total (float) --
When specified, represents the total minutes used by the resource to run tests.

metered (float) --
When specified, represents only the sum of metered minutes used by the resource to run tests.

unmetered (float) --
When specified, represents only the sum of unmetered minutes used by the resource to run tests.



networkProfile (dict) --
The network profile being used for a test run.

arn (string) --
The Amazon Resource Name (ARN) of the network profile.

name (string) --
The name of the network profile.

description (string) --
The description of the network profile.

type (string) --
The type of network profile. Valid values are listed here.

uplinkBandwidthBits (integer) --
The data throughput rate in bits per second, as an integer from 0 to 104857600.

downlinkBandwidthBits (integer) --
The data throughput rate in bits per second, as an integer from 0 to 104857600.

uplinkDelayMs (integer) --
Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.

downlinkDelayMs (integer) --
Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.

uplinkJitterMs (integer) --
Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.

downlinkJitterMs (integer) --
Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.

uplinkLossPercent (integer) --
Proportion of transmitted packets that fail to arrive from 0 to 100 percent.

downlinkLossPercent (integer) --
Proportion of received packets that fail to arrive from 0 to 100 percent.



parsingResultUrl (string) --
Read-only URL for an object in an S3 bucket where you can get the parsing results of the test package. If the test package doesn\'t parse, the reason why it doesn\'t parse appears in the file that this URL points to.

resultCode (string) --
Supporting field for the result field. Set only if result is SKIPPED . PARSING_FAILED if the result is skipped because of test package parsing failure.

seed (integer) --
For fuzz tests, this is a seed to use for randomizing the UI fuzz test. Using the same seed value between tests ensures identical event sequences.

appUpload (string) --
An app to upload or that has been uploaded.

eventCount (integer) --
For fuzz tests, this is the number of events, between 1 and 10000, that the UI fuzz test should perform.

jobTimeoutMinutes (integer) --
The number of minutes the job executes before it times out.

devicePoolArn (string) --
The ARN of the device pool for the run.

locale (string) --
Information about the locale that is used for the run.

radios (dict) --
Information about the radio states for the run.

wifi (boolean) --
True if Wi-Fi is enabled at the beginning of the test. Otherwise, false.

bluetooth (boolean) --
True if Bluetooth is enabled at the beginning of the test. Otherwise, false.

nfc (boolean) --
True if NFC is enabled at the beginning of the test. Otherwise, false.

gps (boolean) --
True if GPS is enabled at the beginning of the test. Otherwise, false.



location (dict) --
Information about the location that is used for the run.

latitude (float) --
The latitude.

longitude (float) --
The longitude.



customerArtifactPaths (dict) --
Output CustomerArtifactPaths object for the test run.

iosPaths (list) --
Comma-separated list of paths on the iOS device where the artifacts generated by the customer\'s tests are pulled from.

(string) --


androidPaths (list) --
Comma-separated list of paths on the Android device where the artifacts generated by the customer\'s tests are pulled from.

(string) --


deviceHostPaths (list) --
Comma-separated list of paths in the test execution environment where the artifacts generated by the customer\'s tests are pulled from.

(string) --




webUrl (string) --
The Device Farm console URL for the recording of the run.

skipAppResign (boolean) --
When set to true , for private devices, Device Farm does not sign your app again. For public devices, Device Farm always signs your apps again.
For more information about how Device Farm re-signs your apps, see Do you modify my app? in the AWS Device Farm FAQs .

testSpecArn (string) --
The ARN of the YAML-formatted test specification for the run.

deviceSelectionResult (dict) --
The results of a device filter used to select the devices for a test run.

filters (list) --
The filters in a device selection result.

(dict) --
Represents a device filter used to select a set of devices to be included in a test run. This data structure is passed in as the deviceSelectionConfiguration parameter to ScheduleRun . For an example of the JSON request syntax, see  ScheduleRun .
It is also passed in as the filters parameter to ListDevices . For an example of the JSON request syntax, see  ListDevices .

attribute (string) --
The aspect of a device such as platform or model used as the selection criteria in a device filter.
The supported operators for each attribute are provided in the following list.

ARN

The Amazon Resource Name (ARN) of the device (for example, arn:aws:devicefarm:us-west-2::device:12345Example ).
Supported operators: EQUALS , IN , NOT_IN

PLATFORM

The device platform. Valid values are ANDROID or IOS.
Supported operators: EQUALS

OS_VERSION

The operating system version (for example, 10.3.2).
Supported operators: EQUALS , GREATER_THAN , GREATER_THAN_OR_EQUALS , IN , LESS_THAN , LESS_THAN_OR_EQUALS , NOT_IN

MODEL

The device model (for example, iPad 5th Gen).
Supported operators: CONTAINS , EQUALS , IN , NOT_IN

AVAILABILITY

The current availability of the device. Valid values are AVAILABLE, HIGHLY_AVAILABLE, BUSY, or TEMPORARY_NOT_AVAILABLE.
Supported operators: EQUALS

FORM_FACTOR

The device form factor. Valid values are PHONE or TABLET.
Supported operators: EQUALS

MANUFACTURER

The device manufacturer (for example, Apple).
Supported operators: EQUALS , IN , NOT_IN

REMOTE_ACCESS_ENABLED

Whether the device is enabled for remote access. Valid values are TRUE or FALSE.
Supported operators: EQUALS

REMOTE_DEBUG_ENABLED

Whether the device is enabled for remote debugging. Valid values are TRUE or FALSE.
Supported operators: EQUALS
Because remote debugging is no longer supported , this filter is ignored.

INSTANCE_ARN

The Amazon Resource Name (ARN) of the device instance.
Supported operators: EQUALS , IN , NOT_IN

INSTANCE_LABELS

The label of the device instance.
Supported operators: CONTAINS

FLEET_TYPE

The fleet type. Valid values are PUBLIC or PRIVATE.
Supported operators: EQUALS

operator (string) --
Specifies how Device Farm compares the filter\'s attribute to the value. See the attribute descriptions.

values (list) --
An array of one or more filter values used in a device filter.

Operator Values


The IN and NOT_IN operators can take a values array that has more than one element.
The other operators require an array with a single element.


Attribute Values


The PLATFORM attribute can be set to ANDROID or IOS.
The AVAILABILITY attribute can be set to AVAILABLE, HIGHLY_AVAILABLE, BUSY, or TEMPORARY_NOT_AVAILABLE.
The FORM_FACTOR attribute can be set to PHONE or TABLET.
The FLEET_TYPE attribute can be set to PUBLIC or PRIVATE.


(string) --






matchedDevicesCount (integer) --
The number of devices that matched the device filter selection criteria.

maxDevices (integer) --
The maximum number of devices to be selected by a device filter and included in a test run.











Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.LimitExceededException
DeviceFarm.Client.exceptions.IdempotencyException
DeviceFarm.Client.exceptions.ServiceAccountException

Examples
The following example schedules a test run named MyRun.
response = client.schedule_run(
    name='MyRun',
    # You can get the Amazon Resource Name (ARN) of the device pool by using the list-pools CLI command.
    devicePoolArn='arn:aws:devicefarm:us-west-2:123456789101:pool:EXAMPLE-GUID-123-456',
    # You can get the Amazon Resource Name (ARN) of the project by using the list-projects CLI command.
    projectArn='arn:aws:devicefarm:us-west-2:123456789101:project:EXAMPLE-GUID-123-456',
    test={
        'type': 'APPIUM_JAVA_JUNIT',
        'testPackageArn': 'arn:aws:devicefarm:us-west-2:123456789101:test:EXAMPLE-GUID-123-456',
    },
)

print(response)


Expected Output:
{
    'run': {
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'run': {
            'arn': 'string',
            'name': 'string',
            'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'WEB_PERFORMANCE_PROFILE'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_NODE'|'APPIUM_RUBY'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'APPIUM_WEB_NODE'|'APPIUM_WEB_RUBY'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI'|'REMOTE_ACCESS_RECORD'|'REMOTE_ACCESS_REPLAY',
            'platform': 'ANDROID'|'IOS',
            'created': datetime(2015, 1, 1),
            'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
            'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
            'started': datetime(2015, 1, 1),
            'stopped': datetime(2015, 1, 1),
            'counters': {
                'total': 123,
                'passed': 123,
                'failed': 123,
                'warned': 123,
                'errored': 123,
                'stopped': 123,
                'skipped': 123
            },
            'message': 'string',
            'totalJobs': 123,
            'completedJobs': 123,
            'billingMethod': 'METERED'|'UNMETERED',
            'deviceMinutes': {
                'total': 123.0,
                'metered': 123.0,
                'unmetered': 123.0
            },
            'networkProfile': {
                'arn': 'string',
                'name': 'string',
                'description': 'string',
                'type': 'CURATED'|'PRIVATE',
                'uplinkBandwidthBits': 123,
                'downlinkBandwidthBits': 123,
                'uplinkDelayMs': 123,
                'downlinkDelayMs': 123,
                'uplinkJitterMs': 123,
                'downlinkJitterMs': 123,
                'uplinkLossPercent': 123,
                'downlinkLossPercent': 123
            },
            'parsingResultUrl': 'string',
            'resultCode': 'PARSING_FAILED'|'VPC_ENDPOINT_SETUP_FAILED',
            'seed': 123,
            'appUpload': 'string',
            'eventCount': 123,
            'jobTimeoutMinutes': 123,
            'devicePoolArn': 'string',
            'locale': 'string',
            'radios': {
                'wifi': True|False,
                'bluetooth': True|False,
                'nfc': True|False,
                'gps': True|False
            },
            'location': {
                'latitude': 123.0,
                'longitude': 123.0
            },
            'customerArtifactPaths': {
                'iosPaths': [
                    'string',
                ],
                'androidPaths': [
                    'string',
                ],
                'deviceHostPaths': [
                    'string',
                ]
            },
            'webUrl': 'string',
            'skipAppResign': True|False,
            'testSpecArn': 'string',
            'deviceSelectionResult': {
                'filters': [
                    {
                        'attribute': 'ARN'|'PLATFORM'|'OS_VERSION'|'MODEL'|'AVAILABILITY'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'INSTANCE_ARN'|'INSTANCE_LABELS'|'FLEET_TYPE',
                        'operator': 'EQUALS'|'LESS_THAN'|'LESS_THAN_OR_EQUALS'|'GREATER_THAN'|'GREATER_THAN_OR_EQUALS'|'IN'|'NOT_IN'|'CONTAINS',
                        'values': [
                            'string',
                        ]
                    },
                ],
                'matchedDevicesCount': 123,
                'maxDevices': 123
            }
        }
    }
    
    
    :returns: 
    BUILTIN_FUZZ
    BUILTIN_EXPLORER
    
    """
    pass

def stop_job(arn=None):
    """
    Initiates a stop request for the current job. AWS Device Farm immediately stops the job on the device where tests have not started. You are not billed for this device. On the device where tests have started, setup suite and teardown suite tests run to completion on the device. You are billed for setup, teardown, and any tests that were in progress or already completed.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.stop_job(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]\nRepresents the Amazon Resource Name (ARN) of the Device Farm job to stop.\n

    :rtype: dict
ReturnsResponse Syntax{
    'job': {
        'arn': 'string',
        'name': 'string',
        'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'WEB_PERFORMANCE_PROFILE'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_NODE'|'APPIUM_RUBY'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'APPIUM_WEB_NODE'|'APPIUM_WEB_RUBY'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI'|'REMOTE_ACCESS_RECORD'|'REMOTE_ACCESS_REPLAY',
        'created': datetime(2015, 1, 1),
        'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
        'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
        'started': datetime(2015, 1, 1),
        'stopped': datetime(2015, 1, 1),
        'counters': {
            'total': 123,
            'passed': 123,
            'failed': 123,
            'warned': 123,
            'errored': 123,
            'stopped': 123,
            'skipped': 123
        },
        'message': 'string',
        'device': {
            'arn': 'string',
            'name': 'string',
            'manufacturer': 'string',
            'model': 'string',
            'modelId': 'string',
            'formFactor': 'PHONE'|'TABLET',
            'platform': 'ANDROID'|'IOS',
            'os': 'string',
            'cpu': {
                'frequency': 'string',
                'architecture': 'string',
                'clock': 123.0
            },
            'resolution': {
                'width': 123,
                'height': 123
            },
            'heapSize': 123,
            'memory': 123,
            'image': 'string',
            'carrier': 'string',
            'radio': 'string',
            'remoteAccessEnabled': True|False,
            'remoteDebugEnabled': True|False,
            'fleetType': 'string',
            'fleetName': 'string',
            'instances': [
                {
                    'arn': 'string',
                    'deviceArn': 'string',
                    'labels': [
                        'string',
                    ],
                    'status': 'IN_USE'|'PREPARING'|'AVAILABLE'|'NOT_AVAILABLE',
                    'udid': 'string',
                    'instanceProfile': {
                        'arn': 'string',
                        'packageCleanup': True|False,
                        'excludeAppPackagesFromCleanup': [
                            'string',
                        ],
                        'rebootAfterUse': True|False,
                        'name': 'string',
                        'description': 'string'
                    }
                },
            ],
            'availability': 'TEMPORARY_NOT_AVAILABLE'|'BUSY'|'AVAILABLE'|'HIGHLY_AVAILABLE'
        },
        'instanceArn': 'string',
        'deviceMinutes': {
            'total': 123.0,
            'metered': 123.0,
            'unmetered': 123.0
        },
        'videoEndpoint': 'string',
        'videoCapture': True|False
    }
}


Response Structure

(dict) --
job (dict) --The job that was stopped.

arn (string) --The job\'s ARN.

name (string) --The job\'s name.

type (string) --The job\'s type.
Allowed values include the following:

BUILTIN_FUZZ
BUILTIN_EXPLORER. For Android, an app explorer that traverses an Android app, interacting with it and capturing screenshots at the same time.
APPIUM_JAVA_JUNIT
APPIUM_JAVA_TESTNG
APPIUM_PYTHON
APPIUM_NODE
APPIUM_RUBY
APPIUM_WEB_JAVA_JUNIT
APPIUM_WEB_JAVA_TESTNG
APPIUM_WEB_PYTHON
APPIUM_WEB_NODE
APPIUM_WEB_RUBY
CALABASH
INSTRUMENTATION
UIAUTOMATION
UIAUTOMATOR
XCTEST
XCTEST_UI


created (datetime) --When the job was created.

status (string) --The job\'s status.
Allowed values include:

PENDING
PENDING_CONCURRENCY
PENDING_DEVICE
PROCESSING
SCHEDULING
PREPARING
RUNNING
COMPLETED
STOPPING


result (string) --The job\'s result.
Allowed values include:

PENDING
PASSED
WARNED
FAILED
SKIPPED
ERRORED
STOPPED


started (datetime) --The job\'s start time.

stopped (datetime) --The job\'s stop time.

counters (dict) --The job\'s result counters.

total (integer) --The total number of entities.

passed (integer) --The number of passed entities.

failed (integer) --The number of failed entities.

warned (integer) --The number of warned entities.

errored (integer) --The number of errored entities.

stopped (integer) --The number of stopped entities.

skipped (integer) --The number of skipped entities.



message (string) --A message about the job\'s result.

device (dict) --The device (phone or tablet).

arn (string) --The device\'s ARN.

name (string) --The device\'s display name.

manufacturer (string) --The device\'s manufacturer name.

model (string) --The device\'s model name.

modelId (string) --The device\'s model ID.

formFactor (string) --The device\'s form factor.
Allowed values include:

PHONE
TABLET


platform (string) --The device\'s platform.
Allowed values include:

ANDROID
IOS


os (string) --The device\'s operating system type.

cpu (dict) --Information about the device\'s CPU.

frequency (string) --The CPU\'s frequency.

architecture (string) --The CPU\'s architecture (for example, x86 or ARM).

clock (float) --The clock speed of the device\'s CPU, expressed in hertz (Hz). For example, a 1.2 GHz CPU is expressed as 1200000000.



resolution (dict) --The resolution of the device.

width (integer) --The screen resolution\'s width, expressed in pixels.

height (integer) --The screen resolution\'s height, expressed in pixels.



heapSize (integer) --The device\'s heap size, expressed in bytes.

memory (integer) --The device\'s total memory size, expressed in bytes.

image (string) --The device\'s image name.

carrier (string) --The device\'s carrier.

radio (string) --The device\'s radio.

remoteAccessEnabled (boolean) --Specifies whether remote access has been enabled for the specified device.

remoteDebugEnabled (boolean) --This flag is set to true if remote debugging is enabled for the device.
Remote debugging is no longer supported .

fleetType (string) --The type of fleet to which this device belongs. Possible values are PRIVATE and PUBLIC.

fleetName (string) --The name of the fleet to which this device belongs.

instances (list) --The instances that belong to this device.

(dict) --Represents the device instance.

arn (string) --The Amazon Resource Name (ARN) of the device instance.

deviceArn (string) --The ARN of the device.

labels (list) --An array of strings that describe the device instance.

(string) --


status (string) --The status of the device instance. Valid values are listed here.

udid (string) --Unique device identifier for the device instance.

instanceProfile (dict) --A object that contains information about the instance profile.

arn (string) --The Amazon Resource Name (ARN) of the instance profile.

packageCleanup (boolean) --When set to true , Device Farm removes app packages after a test run. The default value is false for private devices.

excludeAppPackagesFromCleanup (list) --An array of strings containing the list of app packages that should not be cleaned up from the device after a test run completes.
The list of packages is considered only if you set packageCleanup to true .

(string) --


rebootAfterUse (boolean) --When set to true , Device Farm reboots the instance after a test run. The default value is true .

name (string) --The name of the instance profile.

description (string) --The description of the instance profile.







availability (string) --Indicates how likely a device is available for a test run. Currently available in the  ListDevices and GetDevice API methods.



instanceArn (string) --The ARN of the instance.

deviceMinutes (dict) --Represents the total (metered or unmetered) minutes used by the job.

total (float) --When specified, represents the total minutes used by the resource to run tests.

metered (float) --When specified, represents only the sum of metered minutes used by the resource to run tests.

unmetered (float) --When specified, represents only the sum of unmetered minutes used by the resource to run tests.



videoEndpoint (string) --The endpoint for streaming device video.

videoCapture (boolean) --This value is set to true if video capture is enabled. Otherwise, it is set to false.








Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.LimitExceededException
DeviceFarm.Client.exceptions.ServiceAccountException


    :return: {
        'job': {
            'arn': 'string',
            'name': 'string',
            'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'WEB_PERFORMANCE_PROFILE'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_NODE'|'APPIUM_RUBY'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'APPIUM_WEB_NODE'|'APPIUM_WEB_RUBY'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI'|'REMOTE_ACCESS_RECORD'|'REMOTE_ACCESS_REPLAY',
            'created': datetime(2015, 1, 1),
            'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
            'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
            'started': datetime(2015, 1, 1),
            'stopped': datetime(2015, 1, 1),
            'counters': {
                'total': 123,
                'passed': 123,
                'failed': 123,
                'warned': 123,
                'errored': 123,
                'stopped': 123,
                'skipped': 123
            },
            'message': 'string',
            'device': {
                'arn': 'string',
                'name': 'string',
                'manufacturer': 'string',
                'model': 'string',
                'modelId': 'string',
                'formFactor': 'PHONE'|'TABLET',
                'platform': 'ANDROID'|'IOS',
                'os': 'string',
                'cpu': {
                    'frequency': 'string',
                    'architecture': 'string',
                    'clock': 123.0
                },
                'resolution': {
                    'width': 123,
                    'height': 123
                },
                'heapSize': 123,
                'memory': 123,
                'image': 'string',
                'carrier': 'string',
                'radio': 'string',
                'remoteAccessEnabled': True|False,
                'remoteDebugEnabled': True|False,
                'fleetType': 'string',
                'fleetName': 'string',
                'instances': [
                    {
                        'arn': 'string',
                        'deviceArn': 'string',
                        'labels': [
                            'string',
                        ],
                        'status': 'IN_USE'|'PREPARING'|'AVAILABLE'|'NOT_AVAILABLE',
                        'udid': 'string',
                        'instanceProfile': {
                            'arn': 'string',
                            'packageCleanup': True|False,
                            'excludeAppPackagesFromCleanup': [
                                'string',
                            ],
                            'rebootAfterUse': True|False,
                            'name': 'string',
                            'description': 'string'
                        }
                    },
                ],
                'availability': 'TEMPORARY_NOT_AVAILABLE'|'BUSY'|'AVAILABLE'|'HIGHLY_AVAILABLE'
            },
            'instanceArn': 'string',
            'deviceMinutes': {
                'total': 123.0,
                'metered': 123.0,
                'unmetered': 123.0
            },
            'videoEndpoint': 'string',
            'videoCapture': True|False
        }
    }
    
    
    :returns: 
    PENDING
    PENDING_CONCURRENCY
    PENDING_DEVICE
    PROCESSING
    SCHEDULING
    PREPARING
    RUNNING
    COMPLETED
    STOPPING
    
    """
    pass

def stop_remote_access_session(arn=None):
    """
    Ends a specified remote access session.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.stop_remote_access_session(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the remote access session to stop.\n

    :rtype: dict
ReturnsResponse Syntax{
    'remoteAccessSession': {
        'arn': 'string',
        'name': 'string',
        'created': datetime(2015, 1, 1),
        'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
        'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
        'message': 'string',
        'started': datetime(2015, 1, 1),
        'stopped': datetime(2015, 1, 1),
        'device': {
            'arn': 'string',
            'name': 'string',
            'manufacturer': 'string',
            'model': 'string',
            'modelId': 'string',
            'formFactor': 'PHONE'|'TABLET',
            'platform': 'ANDROID'|'IOS',
            'os': 'string',
            'cpu': {
                'frequency': 'string',
                'architecture': 'string',
                'clock': 123.0
            },
            'resolution': {
                'width': 123,
                'height': 123
            },
            'heapSize': 123,
            'memory': 123,
            'image': 'string',
            'carrier': 'string',
            'radio': 'string',
            'remoteAccessEnabled': True|False,
            'remoteDebugEnabled': True|False,
            'fleetType': 'string',
            'fleetName': 'string',
            'instances': [
                {
                    'arn': 'string',
                    'deviceArn': 'string',
                    'labels': [
                        'string',
                    ],
                    'status': 'IN_USE'|'PREPARING'|'AVAILABLE'|'NOT_AVAILABLE',
                    'udid': 'string',
                    'instanceProfile': {
                        'arn': 'string',
                        'packageCleanup': True|False,
                        'excludeAppPackagesFromCleanup': [
                            'string',
                        ],
                        'rebootAfterUse': True|False,
                        'name': 'string',
                        'description': 'string'
                    }
                },
            ],
            'availability': 'TEMPORARY_NOT_AVAILABLE'|'BUSY'|'AVAILABLE'|'HIGHLY_AVAILABLE'
        },
        'instanceArn': 'string',
        'remoteDebugEnabled': True|False,
        'remoteRecordEnabled': True|False,
        'remoteRecordAppArn': 'string',
        'hostAddress': 'string',
        'clientId': 'string',
        'billingMethod': 'METERED'|'UNMETERED',
        'deviceMinutes': {
            'total': 123.0,
            'metered': 123.0,
            'unmetered': 123.0
        },
        'endpoint': 'string',
        'deviceUdid': 'string',
        'interactionMode': 'INTERACTIVE'|'NO_VIDEO'|'VIDEO_ONLY',
        'skipAppResign': True|False
    }
}


Response Structure

(dict) --Represents the response from the server that describes the remote access session when AWS Device Farm stops the session.

remoteAccessSession (dict) --A container that represents the metadata from the service about the remote access session you are stopping.

arn (string) --The Amazon Resource Name (ARN) of the remote access session.

name (string) --The name of the remote access session.

created (datetime) --The date and time the remote access session was created.

status (string) --The status of the remote access session. Can be any of the following:

PENDING.
PENDING_CONCURRENCY.
PENDING_DEVICE.
PROCESSING.
SCHEDULING.
PREPARING.
RUNNING.
COMPLETED.
STOPPING.


result (string) --The result of the remote access session. Can be any of the following:

PENDING.
PASSED.
WARNED.
FAILED.
SKIPPED.
ERRORED.
STOPPED.


message (string) --A message about the remote access session.

started (datetime) --The date and time the remote access session was started.

stopped (datetime) --The date and time the remote access session was stopped.

device (dict) --The device (phone or tablet) used in the remote access session.

arn (string) --The device\'s ARN.

name (string) --The device\'s display name.

manufacturer (string) --The device\'s manufacturer name.

model (string) --The device\'s model name.

modelId (string) --The device\'s model ID.

formFactor (string) --The device\'s form factor.
Allowed values include:

PHONE
TABLET


platform (string) --The device\'s platform.
Allowed values include:

ANDROID
IOS


os (string) --The device\'s operating system type.

cpu (dict) --Information about the device\'s CPU.

frequency (string) --The CPU\'s frequency.

architecture (string) --The CPU\'s architecture (for example, x86 or ARM).

clock (float) --The clock speed of the device\'s CPU, expressed in hertz (Hz). For example, a 1.2 GHz CPU is expressed as 1200000000.



resolution (dict) --The resolution of the device.

width (integer) --The screen resolution\'s width, expressed in pixels.

height (integer) --The screen resolution\'s height, expressed in pixels.



heapSize (integer) --The device\'s heap size, expressed in bytes.

memory (integer) --The device\'s total memory size, expressed in bytes.

image (string) --The device\'s image name.

carrier (string) --The device\'s carrier.

radio (string) --The device\'s radio.

remoteAccessEnabled (boolean) --Specifies whether remote access has been enabled for the specified device.

remoteDebugEnabled (boolean) --This flag is set to true if remote debugging is enabled for the device.
Remote debugging is no longer supported .

fleetType (string) --The type of fleet to which this device belongs. Possible values are PRIVATE and PUBLIC.

fleetName (string) --The name of the fleet to which this device belongs.

instances (list) --The instances that belong to this device.

(dict) --Represents the device instance.

arn (string) --The Amazon Resource Name (ARN) of the device instance.

deviceArn (string) --The ARN of the device.

labels (list) --An array of strings that describe the device instance.

(string) --


status (string) --The status of the device instance. Valid values are listed here.

udid (string) --Unique device identifier for the device instance.

instanceProfile (dict) --A object that contains information about the instance profile.

arn (string) --The Amazon Resource Name (ARN) of the instance profile.

packageCleanup (boolean) --When set to true , Device Farm removes app packages after a test run. The default value is false for private devices.

excludeAppPackagesFromCleanup (list) --An array of strings containing the list of app packages that should not be cleaned up from the device after a test run completes.
The list of packages is considered only if you set packageCleanup to true .

(string) --


rebootAfterUse (boolean) --When set to true , Device Farm reboots the instance after a test run. The default value is true .

name (string) --The name of the instance profile.

description (string) --The description of the instance profile.







availability (string) --Indicates how likely a device is available for a test run. Currently available in the  ListDevices and GetDevice API methods.



instanceArn (string) --The ARN of the instance.

remoteDebugEnabled (boolean) --This flag is set to true if remote debugging is enabled for the remote access session.
Remote debugging is no longer supported .

remoteRecordEnabled (boolean) --This flag is set to true if remote recording is enabled for the remote access session.

remoteRecordAppArn (string) --The ARN for the app to be recorded in the remote access session.

hostAddress (string) --IP address of the EC2 host where you need to connect to remotely debug devices. Only returned if remote debugging is enabled for the remote access session.
Remote debugging is no longer supported .

clientId (string) --Unique identifier of your client for the remote access session. Only returned if remote debugging is enabled for the remote access session.
Remote debugging is no longer supported .

billingMethod (string) --The billing method of the remote access session. Possible values include METERED or UNMETERED . For more information about metered devices, see AWS Device Farm terminology .

deviceMinutes (dict) --The number of minutes a device is used in a remote access session (including setup and teardown minutes).

total (float) --When specified, represents the total minutes used by the resource to run tests.

metered (float) --When specified, represents only the sum of metered minutes used by the resource to run tests.

unmetered (float) --When specified, represents only the sum of unmetered minutes used by the resource to run tests.



endpoint (string) --The endpoint for the remote access sesssion.

deviceUdid (string) --Unique device identifier for the remote device. Only returned if remote debugging is enabled for the remote access session.
Remote debugging is no longer supported .

interactionMode (string) --The interaction mode of the remote access session. Valid values are:

INTERACTIVE: You can interact with the iOS device by viewing, touching, and rotating the screen. You cannot run XCUITest framework-based tests in this mode.
NO_VIDEO: You are connected to the device, but cannot interact with it or view the screen. This mode has the fastest test execution speed. You can run XCUITest framework-based tests in this mode.
VIDEO_ONLY: You can view the screen, but cannot touch or rotate it. You can run XCUITest framework-based tests and watch the screen in this mode.


skipAppResign (boolean) --When set to true , for private devices, Device Farm does not sign your app again. For public devices, Device Farm always signs your apps again.
For more information about how Device Farm re-signs your apps, see Do you modify my app? in the AWS Device Farm FAQs .








Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.LimitExceededException
DeviceFarm.Client.exceptions.ServiceAccountException


    :return: {
        'remoteAccessSession': {
            'arn': 'string',
            'name': 'string',
            'created': datetime(2015, 1, 1),
            'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
            'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
            'message': 'string',
            'started': datetime(2015, 1, 1),
            'stopped': datetime(2015, 1, 1),
            'device': {
                'arn': 'string',
                'name': 'string',
                'manufacturer': 'string',
                'model': 'string',
                'modelId': 'string',
                'formFactor': 'PHONE'|'TABLET',
                'platform': 'ANDROID'|'IOS',
                'os': 'string',
                'cpu': {
                    'frequency': 'string',
                    'architecture': 'string',
                    'clock': 123.0
                },
                'resolution': {
                    'width': 123,
                    'height': 123
                },
                'heapSize': 123,
                'memory': 123,
                'image': 'string',
                'carrier': 'string',
                'radio': 'string',
                'remoteAccessEnabled': True|False,
                'remoteDebugEnabled': True|False,
                'fleetType': 'string',
                'fleetName': 'string',
                'instances': [
                    {
                        'arn': 'string',
                        'deviceArn': 'string',
                        'labels': [
                            'string',
                        ],
                        'status': 'IN_USE'|'PREPARING'|'AVAILABLE'|'NOT_AVAILABLE',
                        'udid': 'string',
                        'instanceProfile': {
                            'arn': 'string',
                            'packageCleanup': True|False,
                            'excludeAppPackagesFromCleanup': [
                                'string',
                            ],
                            'rebootAfterUse': True|False,
                            'name': 'string',
                            'description': 'string'
                        }
                    },
                ],
                'availability': 'TEMPORARY_NOT_AVAILABLE'|'BUSY'|'AVAILABLE'|'HIGHLY_AVAILABLE'
            },
            'instanceArn': 'string',
            'remoteDebugEnabled': True|False,
            'remoteRecordEnabled': True|False,
            'remoteRecordAppArn': 'string',
            'hostAddress': 'string',
            'clientId': 'string',
            'billingMethod': 'METERED'|'UNMETERED',
            'deviceMinutes': {
                'total': 123.0,
                'metered': 123.0,
                'unmetered': 123.0
            },
            'endpoint': 'string',
            'deviceUdid': 'string',
            'interactionMode': 'INTERACTIVE'|'NO_VIDEO'|'VIDEO_ONLY',
            'skipAppResign': True|False
        }
    }
    
    
    :returns: 
    PENDING.
    PASSED.
    WARNED.
    FAILED.
    SKIPPED.
    ERRORED.
    STOPPED.
    
    """
    pass

def stop_run(arn=None):
    """
    Initiates a stop request for the current test run. AWS Device Farm immediately stops the run on devices where tests have not started. You are not billed for these devices. On devices where tests have started executing, setup suite and teardown suite tests run to completion on those devices. You are billed for setup, teardown, and any tests that were in progress or already completed.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example stops a specific test run.
    Expected Output:
    
    :example: response = client.stop_run(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]\nRepresents the Amazon Resource Name (ARN) of the Device Farm run to stop.\n

    :rtype: dict
ReturnsResponse Syntax{
    'run': {
        'arn': 'string',
        'name': 'string',
        'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'WEB_PERFORMANCE_PROFILE'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_NODE'|'APPIUM_RUBY'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'APPIUM_WEB_NODE'|'APPIUM_WEB_RUBY'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI'|'REMOTE_ACCESS_RECORD'|'REMOTE_ACCESS_REPLAY',
        'platform': 'ANDROID'|'IOS',
        'created': datetime(2015, 1, 1),
        'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
        'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
        'started': datetime(2015, 1, 1),
        'stopped': datetime(2015, 1, 1),
        'counters': {
            'total': 123,
            'passed': 123,
            'failed': 123,
            'warned': 123,
            'errored': 123,
            'stopped': 123,
            'skipped': 123
        },
        'message': 'string',
        'totalJobs': 123,
        'completedJobs': 123,
        'billingMethod': 'METERED'|'UNMETERED',
        'deviceMinutes': {
            'total': 123.0,
            'metered': 123.0,
            'unmetered': 123.0
        },
        'networkProfile': {
            'arn': 'string',
            'name': 'string',
            'description': 'string',
            'type': 'CURATED'|'PRIVATE',
            'uplinkBandwidthBits': 123,
            'downlinkBandwidthBits': 123,
            'uplinkDelayMs': 123,
            'downlinkDelayMs': 123,
            'uplinkJitterMs': 123,
            'downlinkJitterMs': 123,
            'uplinkLossPercent': 123,
            'downlinkLossPercent': 123
        },
        'parsingResultUrl': 'string',
        'resultCode': 'PARSING_FAILED'|'VPC_ENDPOINT_SETUP_FAILED',
        'seed': 123,
        'appUpload': 'string',
        'eventCount': 123,
        'jobTimeoutMinutes': 123,
        'devicePoolArn': 'string',
        'locale': 'string',
        'radios': {
            'wifi': True|False,
            'bluetooth': True|False,
            'nfc': True|False,
            'gps': True|False
        },
        'location': {
            'latitude': 123.0,
            'longitude': 123.0
        },
        'customerArtifactPaths': {
            'iosPaths': [
                'string',
            ],
            'androidPaths': [
                'string',
            ],
            'deviceHostPaths': [
                'string',
            ]
        },
        'webUrl': 'string',
        'skipAppResign': True|False,
        'testSpecArn': 'string',
        'deviceSelectionResult': {
            'filters': [
                {
                    'attribute': 'ARN'|'PLATFORM'|'OS_VERSION'|'MODEL'|'AVAILABILITY'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'INSTANCE_ARN'|'INSTANCE_LABELS'|'FLEET_TYPE',
                    'operator': 'EQUALS'|'LESS_THAN'|'LESS_THAN_OR_EQUALS'|'GREATER_THAN'|'GREATER_THAN_OR_EQUALS'|'IN'|'NOT_IN'|'CONTAINS',
                    'values': [
                        'string',
                    ]
                },
            ],
            'matchedDevicesCount': 123,
            'maxDevices': 123
        }
    }
}


Response Structure

(dict) --Represents the results of your stop run attempt.

run (dict) --The run that was stopped.

arn (string) --The run\'s ARN.

name (string) --The run\'s name.

type (string) --The run\'s type.
Must be one of the following values:

BUILTIN_FUZZ
BUILTIN_EXPLORER


Note
For Android, an app explorer that traverses an Android app, interacting with it and capturing screenshots at the same time.


APPIUM_JAVA_JUNIT
APPIUM_JAVA_TESTNG
APPIUM_PYTHON
APPIUM_NODE
APPIUM_RUBY
APPIUM_WEB_JAVA_JUNIT
APPIUM_WEB_JAVA_TESTNG
APPIUM_WEB_PYTHON
APPIUM_WEB_NODE
APPIUM_WEB_RUBY
CALABASH
INSTRUMENTATION
UIAUTOMATION
UIAUTOMATOR
XCTEST
XCTEST_UI


platform (string) --The run\'s platform.
Allowed values include:

ANDROID
IOS


created (datetime) --When the run was created.

status (string) --The run\'s status.
Allowed values include:

PENDING
PENDING_CONCURRENCY
PENDING_DEVICE
PROCESSING
SCHEDULING
PREPARING
RUNNING
COMPLETED
STOPPING


result (string) --The run\'s result.
Allowed values include:

PENDING
PASSED
WARNED
FAILED
SKIPPED
ERRORED
STOPPED


started (datetime) --The run\'s start time.

stopped (datetime) --The run\'s stop time.

counters (dict) --The run\'s result counters.

total (integer) --The total number of entities.

passed (integer) --The number of passed entities.

failed (integer) --The number of failed entities.

warned (integer) --The number of warned entities.

errored (integer) --The number of errored entities.

stopped (integer) --The number of stopped entities.

skipped (integer) --The number of skipped entities.



message (string) --A message about the run\'s result.

totalJobs (integer) --The total number of jobs for the run.

completedJobs (integer) --The total number of completed jobs.

billingMethod (string) --Specifies the billing method for a test run: metered or unmetered . If the parameter is not specified, the default value is metered .

Note
If you have unmetered device slots, you must set this to unmetered to use them. Otherwise, the run is counted toward metered device minutes.


deviceMinutes (dict) --Represents the total (metered or unmetered) minutes used by the test run.

total (float) --When specified, represents the total minutes used by the resource to run tests.

metered (float) --When specified, represents only the sum of metered minutes used by the resource to run tests.

unmetered (float) --When specified, represents only the sum of unmetered minutes used by the resource to run tests.



networkProfile (dict) --The network profile being used for a test run.

arn (string) --The Amazon Resource Name (ARN) of the network profile.

name (string) --The name of the network profile.

description (string) --The description of the network profile.

type (string) --The type of network profile. Valid values are listed here.

uplinkBandwidthBits (integer) --The data throughput rate in bits per second, as an integer from 0 to 104857600.

downlinkBandwidthBits (integer) --The data throughput rate in bits per second, as an integer from 0 to 104857600.

uplinkDelayMs (integer) --Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.

downlinkDelayMs (integer) --Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.

uplinkJitterMs (integer) --Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.

downlinkJitterMs (integer) --Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.

uplinkLossPercent (integer) --Proportion of transmitted packets that fail to arrive from 0 to 100 percent.

downlinkLossPercent (integer) --Proportion of received packets that fail to arrive from 0 to 100 percent.



parsingResultUrl (string) --Read-only URL for an object in an S3 bucket where you can get the parsing results of the test package. If the test package doesn\'t parse, the reason why it doesn\'t parse appears in the file that this URL points to.

resultCode (string) --Supporting field for the result field. Set only if result is SKIPPED . PARSING_FAILED if the result is skipped because of test package parsing failure.

seed (integer) --For fuzz tests, this is a seed to use for randomizing the UI fuzz test. Using the same seed value between tests ensures identical event sequences.

appUpload (string) --An app to upload or that has been uploaded.

eventCount (integer) --For fuzz tests, this is the number of events, between 1 and 10000, that the UI fuzz test should perform.

jobTimeoutMinutes (integer) --The number of minutes the job executes before it times out.

devicePoolArn (string) --The ARN of the device pool for the run.

locale (string) --Information about the locale that is used for the run.

radios (dict) --Information about the radio states for the run.

wifi (boolean) --True if Wi-Fi is enabled at the beginning of the test. Otherwise, false.

bluetooth (boolean) --True if Bluetooth is enabled at the beginning of the test. Otherwise, false.

nfc (boolean) --True if NFC is enabled at the beginning of the test. Otherwise, false.

gps (boolean) --True if GPS is enabled at the beginning of the test. Otherwise, false.



location (dict) --Information about the location that is used for the run.

latitude (float) --The latitude.

longitude (float) --The longitude.



customerArtifactPaths (dict) --Output CustomerArtifactPaths object for the test run.

iosPaths (list) --Comma-separated list of paths on the iOS device where the artifacts generated by the customer\'s tests are pulled from.

(string) --


androidPaths (list) --Comma-separated list of paths on the Android device where the artifacts generated by the customer\'s tests are pulled from.

(string) --


deviceHostPaths (list) --Comma-separated list of paths in the test execution environment where the artifacts generated by the customer\'s tests are pulled from.

(string) --




webUrl (string) --The Device Farm console URL for the recording of the run.

skipAppResign (boolean) --When set to true , for private devices, Device Farm does not sign your app again. For public devices, Device Farm always signs your apps again.
For more information about how Device Farm re-signs your apps, see Do you modify my app? in the AWS Device Farm FAQs .

testSpecArn (string) --The ARN of the YAML-formatted test specification for the run.

deviceSelectionResult (dict) --The results of a device filter used to select the devices for a test run.

filters (list) --The filters in a device selection result.

(dict) --Represents a device filter used to select a set of devices to be included in a test run. This data structure is passed in as the deviceSelectionConfiguration parameter to ScheduleRun . For an example of the JSON request syntax, see  ScheduleRun .
It is also passed in as the filters parameter to ListDevices . For an example of the JSON request syntax, see  ListDevices .

attribute (string) --The aspect of a device such as platform or model used as the selection criteria in a device filter.
The supported operators for each attribute are provided in the following list.

ARN
The Amazon Resource Name (ARN) of the device (for example, arn:aws:devicefarm:us-west-2::device:12345Example ).
Supported operators: EQUALS , IN , NOT_IN

PLATFORM
The device platform. Valid values are ANDROID or IOS.
Supported operators: EQUALS

OS_VERSION
The operating system version (for example, 10.3.2).
Supported operators: EQUALS , GREATER_THAN , GREATER_THAN_OR_EQUALS , IN , LESS_THAN , LESS_THAN_OR_EQUALS , NOT_IN

MODEL
The device model (for example, iPad 5th Gen).
Supported operators: CONTAINS , EQUALS , IN , NOT_IN

AVAILABILITY
The current availability of the device. Valid values are AVAILABLE, HIGHLY_AVAILABLE, BUSY, or TEMPORARY_NOT_AVAILABLE.
Supported operators: EQUALS

FORM_FACTOR
The device form factor. Valid values are PHONE or TABLET.
Supported operators: EQUALS

MANUFACTURER
The device manufacturer (for example, Apple).
Supported operators: EQUALS , IN , NOT_IN

REMOTE_ACCESS_ENABLED
Whether the device is enabled for remote access. Valid values are TRUE or FALSE.
Supported operators: EQUALS

REMOTE_DEBUG_ENABLED
Whether the device is enabled for remote debugging. Valid values are TRUE or FALSE.
Supported operators: EQUALS
Because remote debugging is no longer supported , this filter is ignored.

INSTANCE_ARN
The Amazon Resource Name (ARN) of the device instance.
Supported operators: EQUALS , IN , NOT_IN

INSTANCE_LABELS
The label of the device instance.
Supported operators: CONTAINS

FLEET_TYPE
The fleet type. Valid values are PUBLIC or PRIVATE.
Supported operators: EQUALS

operator (string) --Specifies how Device Farm compares the filter\'s attribute to the value. See the attribute descriptions.

values (list) --An array of one or more filter values used in a device filter.

Operator Values

The IN and NOT_IN operators can take a values array that has more than one element.
The other operators require an array with a single element.


Attribute Values

The PLATFORM attribute can be set to ANDROID or IOS.
The AVAILABILITY attribute can be set to AVAILABLE, HIGHLY_AVAILABLE, BUSY, or TEMPORARY_NOT_AVAILABLE.
The FORM_FACTOR attribute can be set to PHONE or TABLET.
The FLEET_TYPE attribute can be set to PUBLIC or PRIVATE.


(string) --






matchedDevicesCount (integer) --The number of devices that matched the device filter selection criteria.

maxDevices (integer) --The maximum number of devices to be selected by a device filter and included in a test run.










Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.LimitExceededException
DeviceFarm.Client.exceptions.ServiceAccountException

Examples
The following example stops a specific test run.
response = client.stop_run(
    # You can get the Amazon Resource Name (ARN) of the test run by using the list-runs CLI command.
    arn='arn:aws:devicefarm:us-west-2:123456789101:run:EXAMPLE-GUID-123-456',
)

print(response)


Expected Output:
{
    'run': {
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'run': {
            'arn': 'string',
            'name': 'string',
            'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'WEB_PERFORMANCE_PROFILE'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_NODE'|'APPIUM_RUBY'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'APPIUM_WEB_NODE'|'APPIUM_WEB_RUBY'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI'|'REMOTE_ACCESS_RECORD'|'REMOTE_ACCESS_REPLAY',
            'platform': 'ANDROID'|'IOS',
            'created': datetime(2015, 1, 1),
            'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
            'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
            'started': datetime(2015, 1, 1),
            'stopped': datetime(2015, 1, 1),
            'counters': {
                'total': 123,
                'passed': 123,
                'failed': 123,
                'warned': 123,
                'errored': 123,
                'stopped': 123,
                'skipped': 123
            },
            'message': 'string',
            'totalJobs': 123,
            'completedJobs': 123,
            'billingMethod': 'METERED'|'UNMETERED',
            'deviceMinutes': {
                'total': 123.0,
                'metered': 123.0,
                'unmetered': 123.0
            },
            'networkProfile': {
                'arn': 'string',
                'name': 'string',
                'description': 'string',
                'type': 'CURATED'|'PRIVATE',
                'uplinkBandwidthBits': 123,
                'downlinkBandwidthBits': 123,
                'uplinkDelayMs': 123,
                'downlinkDelayMs': 123,
                'uplinkJitterMs': 123,
                'downlinkJitterMs': 123,
                'uplinkLossPercent': 123,
                'downlinkLossPercent': 123
            },
            'parsingResultUrl': 'string',
            'resultCode': 'PARSING_FAILED'|'VPC_ENDPOINT_SETUP_FAILED',
            'seed': 123,
            'appUpload': 'string',
            'eventCount': 123,
            'jobTimeoutMinutes': 123,
            'devicePoolArn': 'string',
            'locale': 'string',
            'radios': {
                'wifi': True|False,
                'bluetooth': True|False,
                'nfc': True|False,
                'gps': True|False
            },
            'location': {
                'latitude': 123.0,
                'longitude': 123.0
            },
            'customerArtifactPaths': {
                'iosPaths': [
                    'string',
                ],
                'androidPaths': [
                    'string',
                ],
                'deviceHostPaths': [
                    'string',
                ]
            },
            'webUrl': 'string',
            'skipAppResign': True|False,
            'testSpecArn': 'string',
            'deviceSelectionResult': {
                'filters': [
                    {
                        'attribute': 'ARN'|'PLATFORM'|'OS_VERSION'|'MODEL'|'AVAILABILITY'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'INSTANCE_ARN'|'INSTANCE_LABELS'|'FLEET_TYPE',
                        'operator': 'EQUALS'|'LESS_THAN'|'LESS_THAN_OR_EQUALS'|'GREATER_THAN'|'GREATER_THAN_OR_EQUALS'|'IN'|'NOT_IN'|'CONTAINS',
                        'values': [
                            'string',
                        ]
                    },
                ],
                'matchedDevicesCount': 123,
                'maxDevices': 123
            }
        }
    }
    
    
    :returns: 
    APPIUM_JAVA_JUNIT
    APPIUM_JAVA_TESTNG
    APPIUM_PYTHON
    APPIUM_NODE
    APPIUM_RUBY
    APPIUM_WEB_JAVA_JUNIT
    APPIUM_WEB_JAVA_TESTNG
    APPIUM_WEB_PYTHON
    APPIUM_WEB_NODE
    APPIUM_WEB_RUBY
    CALABASH
    INSTRUMENTATION
    UIAUTOMATION
    UIAUTOMATOR
    XCTEST
    XCTEST_UI
    
    """
    pass

def tag_resource(ResourceARN=None, Tags=None):
    """
    Associates the specified tags to a resource with the specified resourceArn . If existing tags on a resource are not specified in the request parameters, they are not changed. When a resource is deleted, the tags associated with that resource are also deleted.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        ResourceARN='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ResourceARN: string
    :param ResourceARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource or resources to which to add tags. You can associate tags with the following Device Farm resources: PROJECT , RUN , NETWORK_PROFILE , INSTANCE_PROFILE , DEVICE_INSTANCE , SESSION , DEVICE_POOL , DEVICE , and VPCE_CONFIGURATION .\n

    :type Tags: list
    :param Tags: [REQUIRED]\nThe tags to add to the resource. A tag is an array of key-value pairs. Tag keys can have a maximum character length of 128 characters. Tag values can have a maximum length of 256 characters.\n\n(dict) --The metadata that you apply to a resource to help you categorize and organize it. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters. Tag values can have a maximum length of 256 characters.\n\nKey (string) -- [REQUIRED]One part of a key-value pair that makes up a tag. A key is a general label that acts like a category for more specific tag values.\n\nValue (string) -- [REQUIRED]The optional part of a key-value pair that makes up a tag. A value acts as a descriptor in a tag category (key).\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.TagOperationException
DeviceFarm.Client.exceptions.TooManyTagsException
DeviceFarm.Client.exceptions.TagPolicyException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_resource(ResourceARN=None, TagKeys=None):
    """
    Deletes the specified tags from a resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        ResourceARN='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceARN: string
    :param ResourceARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource or resources from which to delete tags. You can associate tags with the following Device Farm resources: PROJECT , RUN , NETWORK_PROFILE , INSTANCE_PROFILE , DEVICE_INSTANCE , SESSION , DEVICE_POOL , DEVICE , and VPCE_CONFIGURATION .\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nThe keys of the tags to be removed.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.TagOperationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_device_instance(arn=None, profileArn=None, labels=None):
    """
    Updates information about a private device instance.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_device_instance(
        arn='string',
        profileArn='string',
        labels=[
            'string',
        ]
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the device instance.\n

    :type profileArn: string
    :param profileArn: The ARN of the profile that you want to associate with the device instance.

    :type labels: list
    :param labels: An array of strings that you want to associate with the device instance.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'deviceInstance': {
        'arn': 'string',
        'deviceArn': 'string',
        'labels': [
            'string',
        ],
        'status': 'IN_USE'|'PREPARING'|'AVAILABLE'|'NOT_AVAILABLE',
        'udid': 'string',
        'instanceProfile': {
            'arn': 'string',
            'packageCleanup': True|False,
            'excludeAppPackagesFromCleanup': [
                'string',
            ],
            'rebootAfterUse': True|False,
            'name': 'string',
            'description': 'string'
        }
    }
}


Response Structure

(dict) --

deviceInstance (dict) --
An object that contains information about your device instance.

arn (string) --
The Amazon Resource Name (ARN) of the device instance.

deviceArn (string) --
The ARN of the device.

labels (list) --
An array of strings that describe the device instance.

(string) --


status (string) --
The status of the device instance. Valid values are listed here.

udid (string) --
Unique device identifier for the device instance.

instanceProfile (dict) --
A object that contains information about the instance profile.

arn (string) --
The Amazon Resource Name (ARN) of the instance profile.

packageCleanup (boolean) --
When set to true , Device Farm removes app packages after a test run. The default value is false for private devices.

excludeAppPackagesFromCleanup (list) --
An array of strings containing the list of app packages that should not be cleaned up from the device after a test run completes.
The list of packages is considered only if you set packageCleanup to true .

(string) --


rebootAfterUse (boolean) --
When set to true , Device Farm reboots the instance after a test run. The default value is true .

name (string) --
The name of the instance profile.

description (string) --
The description of the instance profile.











Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.LimitExceededException
DeviceFarm.Client.exceptions.ServiceAccountException


    :return: {
        'deviceInstance': {
            'arn': 'string',
            'deviceArn': 'string',
            'labels': [
                'string',
            ],
            'status': 'IN_USE'|'PREPARING'|'AVAILABLE'|'NOT_AVAILABLE',
            'udid': 'string',
            'instanceProfile': {
                'arn': 'string',
                'packageCleanup': True|False,
                'excludeAppPackagesFromCleanup': [
                    'string',
                ],
                'rebootAfterUse': True|False,
                'name': 'string',
                'description': 'string'
            }
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def update_device_pool(arn=None, name=None, description=None, rules=None, maxDevices=None, clearMaxDevices=None):
    """
    Modifies the name, description, and rules in a device pool given the attributes and the pool ARN. Rule updates are all-or-nothing, meaning they can only be updated as a whole (or not at all).
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example updates the specified device pool with a new name and description. It also enables remote access of devices in the device pool.
    Expected Output:
    
    :example: response = client.update_device_pool(
        arn='string',
        name='string',
        description='string',
        rules=[
            {
                'attribute': 'ARN'|'PLATFORM'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'APPIUM_VERSION'|'INSTANCE_ARN'|'INSTANCE_LABELS'|'FLEET_TYPE'|'OS_VERSION'|'MODEL'|'AVAILABILITY',
                'operator': 'EQUALS'|'LESS_THAN'|'LESS_THAN_OR_EQUALS'|'GREATER_THAN'|'GREATER_THAN_OR_EQUALS'|'IN'|'NOT_IN'|'CONTAINS',
                'value': 'string'
            },
        ],
        maxDevices=123,
        clearMaxDevices=True|False
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the Device Farm device pool to update.\n

    :type name: string
    :param name: A string that represents the name of the device pool to update.

    :type description: string
    :param description: A description of the device pool to update.

    :type rules: list
    :param rules: Represents the rules to modify for the device pool. Updating rules is optional. If you update rules for your request, the update replaces the existing rules.\n\n(dict) --Represents a condition for a device pool.\n\nattribute (string) --The rule\'s stringified attribute. For example, specify the value as '\\'abc\\'' .\nThe supported operators for each attribute are provided in the following list.\n\nAPPIUM_VERSION\nThe Appium version for the test.\nSupported operators: CONTAINS\n\nARN\nThe Amazon Resource Name (ARN) of the device (for example, arn:aws:devicefarm:us-west-2::device:12345Example .\nSupported operators: EQUALS , IN , NOT_IN\n\nAVAILABILITY\nThe current availability of the device. Valid values are AVAILABLE, HIGHLY_AVAILABLE, BUSY, or TEMPORARY_NOT_AVAILABLE.\nSupported operators: EQUALS\n\nFLEET_TYPE\nThe fleet type. Valid values are PUBLIC or PRIVATE.\nSupported operators: EQUALS\n\nFORM_FACTOR\nThe device form factor. Valid values are PHONE or TABLET.\nSupported operators: EQUALS , IN , NOT_IN\n\nINSTANCE_ARN\nThe Amazon Resource Name (ARN) of the device instance.\nSupported operators: IN , NOT_IN\n\nINSTANCE_LABELS\nThe label of the device instance.\nSupported operators: CONTAINS\n\nMANUFACTURER\nThe device manufacturer (for example, Apple).\nSupported operators: EQUALS , IN , NOT_IN\n\nMODEL\nThe device model, such as Apple iPad Air 2 or Google Pixel.\nSupported operators: CONTAINS , EQUALS , IN , NOT_IN\n\nOS_VERSION\nThe operating system version (for example, 10.3.2).\nSupported operators: EQUALS , GREATER_THAN , GREATER_THAN_OR_EQUALS , IN , LESS_THAN , LESS_THAN_OR_EQUALS , NOT_IN\n\nPLATFORM\nThe device platform. Valid values are ANDROID or IOS.\nSupported operators: EQUALS , IN , NOT_IN\n\nREMOTE_ACCESS_ENABLED\nWhether the device is enabled for remote access. Valid values are TRUE or FALSE.\nSupported operators: EQUALS\n\nREMOTE_DEBUG_ENABLED\nWhether the device is enabled for remote debugging. Valid values are TRUE or FALSE.\nSupported operators: EQUALS\nBecause remote debugging is no longer supported , this filter is ignored.\n\noperator (string) --Specifies how Device Farm compares the rule\'s attribute to the value. For the operators that are supported by each attribute, see the attribute descriptions.\n\nvalue (string) --The rule\'s value.\n\n\n\n\n

    :type maxDevices: integer
    :param maxDevices: The number of devices that Device Farm can add to your device pool. Device Farm adds devices that are available and that meet the criteria that you assign for the rules parameter. Depending on how many devices meet these constraints, your device pool might contain fewer devices than the value for this parameter.\nBy specifying the maximum number of devices, you can control the costs that you incur by running tests.\nIf you use this parameter in your request, you cannot use the clearMaxDevices parameter in the same request.\n

    :type clearMaxDevices: boolean
    :param clearMaxDevices: Sets whether the maxDevices parameter applies to your device pool. If you set this parameter to true , the maxDevices parameter does not apply, and Device Farm does not limit the number of devices that it adds to your device pool. In this case, Device Farm adds all available devices that meet the criteria specified in the rules parameter.\nIf you use this parameter in your request, you cannot use the maxDevices parameter in the same request.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'devicePool': {
        'arn': 'string',
        'name': 'string',
        'description': 'string',
        'type': 'CURATED'|'PRIVATE',
        'rules': [
            {
                'attribute': 'ARN'|'PLATFORM'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'APPIUM_VERSION'|'INSTANCE_ARN'|'INSTANCE_LABELS'|'FLEET_TYPE'|'OS_VERSION'|'MODEL'|'AVAILABILITY',
                'operator': 'EQUALS'|'LESS_THAN'|'LESS_THAN_OR_EQUALS'|'GREATER_THAN'|'GREATER_THAN_OR_EQUALS'|'IN'|'NOT_IN'|'CONTAINS',
                'value': 'string'
            },
        ],
        'maxDevices': 123
    }
}


Response Structure

(dict) --
Represents the result of an update device pool request.

devicePool (dict) --
The device pool you just updated.

arn (string) --
The device pool\'s ARN.

name (string) --
The device pool\'s name.

description (string) --
The device pool\'s description.

type (string) --
The device pool\'s type.
Allowed values include:

CURATED: A device pool that is created and managed by AWS Device Farm.
PRIVATE: A device pool that is created and managed by the device pool developer.


rules (list) --
Information about the device pool\'s rules.

(dict) --
Represents a condition for a device pool.

attribute (string) --
The rule\'s stringified attribute. For example, specify the value as "\\"abc\\"" .
The supported operators for each attribute are provided in the following list.

APPIUM_VERSION

The Appium version for the test.
Supported operators: CONTAINS

ARN

The Amazon Resource Name (ARN) of the device (for example, arn:aws:devicefarm:us-west-2::device:12345Example .
Supported operators: EQUALS , IN , NOT_IN

AVAILABILITY

The current availability of the device. Valid values are AVAILABLE, HIGHLY_AVAILABLE, BUSY, or TEMPORARY_NOT_AVAILABLE.
Supported operators: EQUALS

FLEET_TYPE

The fleet type. Valid values are PUBLIC or PRIVATE.
Supported operators: EQUALS

FORM_FACTOR

The device form factor. Valid values are PHONE or TABLET.
Supported operators: EQUALS , IN , NOT_IN

INSTANCE_ARN

The Amazon Resource Name (ARN) of the device instance.
Supported operators: IN , NOT_IN

INSTANCE_LABELS

The label of the device instance.
Supported operators: CONTAINS

MANUFACTURER

The device manufacturer (for example, Apple).
Supported operators: EQUALS , IN , NOT_IN

MODEL

The device model, such as Apple iPad Air 2 or Google Pixel.
Supported operators: CONTAINS , EQUALS , IN , NOT_IN

OS_VERSION

The operating system version (for example, 10.3.2).
Supported operators: EQUALS , GREATER_THAN , GREATER_THAN_OR_EQUALS , IN , LESS_THAN , LESS_THAN_OR_EQUALS , NOT_IN

PLATFORM

The device platform. Valid values are ANDROID or IOS.
Supported operators: EQUALS , IN , NOT_IN

REMOTE_ACCESS_ENABLED

Whether the device is enabled for remote access. Valid values are TRUE or FALSE.
Supported operators: EQUALS

REMOTE_DEBUG_ENABLED

Whether the device is enabled for remote debugging. Valid values are TRUE or FALSE.
Supported operators: EQUALS
Because remote debugging is no longer supported , this filter is ignored.

operator (string) --
Specifies how Device Farm compares the rule\'s attribute to the value. For the operators that are supported by each attribute, see the attribute descriptions.

value (string) --
The rule\'s value.





maxDevices (integer) --
The number of devices that Device Farm can add to your device pool. Device Farm adds devices that are available and meet the criteria that you assign for the rules parameter. Depending on how many devices meet these constraints, your device pool might contain fewer devices than the value for this parameter.
By specifying the maximum number of devices, you can control the costs that you incur by running tests.









Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.LimitExceededException
DeviceFarm.Client.exceptions.ServiceAccountException

Examples
The following example updates the specified device pool with a new name and description. It also enables remote access of devices in the device pool.
response = client.update_device_pool(
    name='NewName',
    # You can get the Amazon Resource Name (ARN) of the device pool by using the list-pools CLI command.
    arn='arn:aws:devicefarm:us-west-2::devicepool:082d10e5-d7d7-48a5-ba5c-12345EXAMPLE',
    description='NewDescription',
    rules=[
        {
            'value': 'True',
            'attribute': 'REMOTE_ACCESS_ENABLED',
            'operator': 'EQUALS',
        },
    ],
)

print(response)


Expected Output:
{
    # Note: you cannot update curated device pools.
    'devicePool': {
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'devicePool': {
            'arn': 'string',
            'name': 'string',
            'description': 'string',
            'type': 'CURATED'|'PRIVATE',
            'rules': [
                {
                    'attribute': 'ARN'|'PLATFORM'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'APPIUM_VERSION'|'INSTANCE_ARN'|'INSTANCE_LABELS'|'FLEET_TYPE'|'OS_VERSION'|'MODEL'|'AVAILABILITY',
                    'operator': 'EQUALS'|'LESS_THAN'|'LESS_THAN_OR_EQUALS'|'GREATER_THAN'|'GREATER_THAN_OR_EQUALS'|'IN'|'NOT_IN'|'CONTAINS',
                    'value': 'string'
                },
            ],
            'maxDevices': 123
        }
    }
    
    
    :returns: 
    CURATED: A device pool that is created and managed by AWS Device Farm.
    PRIVATE: A device pool that is created and managed by the device pool developer.
    
    """
    pass

def update_instance_profile(arn=None, name=None, description=None, packageCleanup=None, excludeAppPackagesFromCleanup=None, rebootAfterUse=None):
    """
    Updates information about an existing private device instance profile.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_instance_profile(
        arn='string',
        name='string',
        description='string',
        packageCleanup=True|False,
        excludeAppPackagesFromCleanup=[
            'string',
        ],
        rebootAfterUse=True|False
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the instance profile.\n

    :type name: string
    :param name: The updated name for your instance profile.

    :type description: string
    :param description: The updated description for your instance profile.

    :type packageCleanup: boolean
    :param packageCleanup: The updated choice for whether you want to specify package cleanup. The default value is false for private devices.

    :type excludeAppPackagesFromCleanup: list
    :param excludeAppPackagesFromCleanup: An array of strings that specifies the list of app packages that should not be cleaned up from the device after a test run is over.\nThe list of packages is only considered if you set packageCleanup to true .\n\n(string) --\n\n

    :type rebootAfterUse: boolean
    :param rebootAfterUse: The updated choice for whether you want to reboot the device after use. The default value is true .

    :rtype: dict

ReturnsResponse Syntax
{
    'instanceProfile': {
        'arn': 'string',
        'packageCleanup': True|False,
        'excludeAppPackagesFromCleanup': [
            'string',
        ],
        'rebootAfterUse': True|False,
        'name': 'string',
        'description': 'string'
    }
}


Response Structure

(dict) --

instanceProfile (dict) --
An object that contains information about your instance profile.

arn (string) --
The Amazon Resource Name (ARN) of the instance profile.

packageCleanup (boolean) --
When set to true , Device Farm removes app packages after a test run. The default value is false for private devices.

excludeAppPackagesFromCleanup (list) --
An array of strings containing the list of app packages that should not be cleaned up from the device after a test run completes.
The list of packages is considered only if you set packageCleanup to true .

(string) --


rebootAfterUse (boolean) --
When set to true , Device Farm reboots the instance after a test run. The default value is true .

name (string) --
The name of the instance profile.

description (string) --
The description of the instance profile.









Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.LimitExceededException
DeviceFarm.Client.exceptions.ServiceAccountException


    :return: {
        'instanceProfile': {
            'arn': 'string',
            'packageCleanup': True|False,
            'excludeAppPackagesFromCleanup': [
                'string',
            ],
            'rebootAfterUse': True|False,
            'name': 'string',
            'description': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def update_network_profile(arn=None, name=None, description=None, type=None, uplinkBandwidthBits=None, downlinkBandwidthBits=None, uplinkDelayMs=None, downlinkDelayMs=None, uplinkJitterMs=None, downlinkJitterMs=None, uplinkLossPercent=None, downlinkLossPercent=None):
    """
    Updates the network profile.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_network_profile(
        arn='string',
        name='string',
        description='string',
        type='CURATED'|'PRIVATE',
        uplinkBandwidthBits=123,
        downlinkBandwidthBits=123,
        uplinkDelayMs=123,
        downlinkDelayMs=123,
        uplinkJitterMs=123,
        downlinkJitterMs=123,
        uplinkLossPercent=123,
        downlinkLossPercent=123
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the project for which you want to update network profile settings.\n

    :type name: string
    :param name: The name of the network profile about which you are returning information.

    :type description: string
    :param description: The description of the network profile about which you are returning information.

    :type type: string
    :param type: The type of network profile to return information about. Valid values are listed here.

    :type uplinkBandwidthBits: integer
    :param uplinkBandwidthBits: The data throughput rate in bits per second, as an integer from 0 to 104857600.

    :type downlinkBandwidthBits: integer
    :param downlinkBandwidthBits: The data throughput rate in bits per second, as an integer from 0 to 104857600.

    :type uplinkDelayMs: integer
    :param uplinkDelayMs: Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.

    :type downlinkDelayMs: integer
    :param downlinkDelayMs: Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.

    :type uplinkJitterMs: integer
    :param uplinkJitterMs: Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.

    :type downlinkJitterMs: integer
    :param downlinkJitterMs: Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.

    :type uplinkLossPercent: integer
    :param uplinkLossPercent: Proportion of transmitted packets that fail to arrive from 0 to 100 percent.

    :type downlinkLossPercent: integer
    :param downlinkLossPercent: Proportion of received packets that fail to arrive from 0 to 100 percent.

    :rtype: dict

ReturnsResponse Syntax
{
    'networkProfile': {
        'arn': 'string',
        'name': 'string',
        'description': 'string',
        'type': 'CURATED'|'PRIVATE',
        'uplinkBandwidthBits': 123,
        'downlinkBandwidthBits': 123,
        'uplinkDelayMs': 123,
        'downlinkDelayMs': 123,
        'uplinkJitterMs': 123,
        'downlinkJitterMs': 123,
        'uplinkLossPercent': 123,
        'downlinkLossPercent': 123
    }
}


Response Structure

(dict) --

networkProfile (dict) --
A list of the available network profiles.

arn (string) --
The Amazon Resource Name (ARN) of the network profile.

name (string) --
The name of the network profile.

description (string) --
The description of the network profile.

type (string) --
The type of network profile. Valid values are listed here.

uplinkBandwidthBits (integer) --
The data throughput rate in bits per second, as an integer from 0 to 104857600.

downlinkBandwidthBits (integer) --
The data throughput rate in bits per second, as an integer from 0 to 104857600.

uplinkDelayMs (integer) --
Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.

downlinkDelayMs (integer) --
Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.

uplinkJitterMs (integer) --
Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.

downlinkJitterMs (integer) --
Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.

uplinkLossPercent (integer) --
Proportion of transmitted packets that fail to arrive from 0 to 100 percent.

downlinkLossPercent (integer) --
Proportion of received packets that fail to arrive from 0 to 100 percent.









Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.LimitExceededException
DeviceFarm.Client.exceptions.ServiceAccountException


    :return: {
        'networkProfile': {
            'arn': 'string',
            'name': 'string',
            'description': 'string',
            'type': 'CURATED'|'PRIVATE',
            'uplinkBandwidthBits': 123,
            'downlinkBandwidthBits': 123,
            'uplinkDelayMs': 123,
            'downlinkDelayMs': 123,
            'uplinkJitterMs': 123,
            'downlinkJitterMs': 123,
            'uplinkLossPercent': 123,
            'downlinkLossPercent': 123
        }
    }
    
    
    :returns: 
    DeviceFarm.Client.exceptions.ArgumentException
    DeviceFarm.Client.exceptions.NotFoundException
    DeviceFarm.Client.exceptions.LimitExceededException
    DeviceFarm.Client.exceptions.ServiceAccountException
    
    """
    pass

def update_project(arn=None, name=None, defaultJobTimeoutMinutes=None):
    """
    Modifies the specified project name, given the project ARN and a new name.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example updates the specified project with a new name.
    Expected Output:
    
    :example: response = client.update_project(
        arn='string',
        name='string',
        defaultJobTimeoutMinutes=123
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the project whose name to update.\n

    :type name: string
    :param name: A string that represents the new name of the project that you are updating.

    :type defaultJobTimeoutMinutes: integer
    :param defaultJobTimeoutMinutes: The number of minutes a test run in the project executes before it times out.

    :rtype: dict

ReturnsResponse Syntax
{
    'project': {
        'arn': 'string',
        'name': 'string',
        'defaultJobTimeoutMinutes': 123,
        'created': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --
Represents the result of an update project request.

project (dict) --
The project to update.

arn (string) --
The project\'s ARN.

name (string) --
The project\'s name.

defaultJobTimeoutMinutes (integer) --
The default number of minutes (at the project level) a test run executes before it times out. The default value is 150 minutes.

created (datetime) --
When the project was created.









Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.LimitExceededException
DeviceFarm.Client.exceptions.ServiceAccountException

Examples
The following example updates the specified project with a new name.
response = client.update_project(
    name='NewName',
    # You can get the Amazon Resource Name (ARN) of the project by using the list-projects CLI command.
    arn='arn:aws:devicefarm:us-west-2:123456789101:project:8f75187d-101e-4625-accc-12345EXAMPLE',
)

print(response)


Expected Output:
{
    'project': {
        'name': 'NewName',
        'arn': 'arn:aws:devicefarm:us-west-2:123456789101:project:8f75187d-101e-4625-accc-12345EXAMPLE',
        'created': datetime(2015, 11, 24, 21, 31, 49, 1, 328, 0),
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'project': {
            'arn': 'string',
            'name': 'string',
            'defaultJobTimeoutMinutes': 123,
            'created': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    DeviceFarm.Client.exceptions.ArgumentException
    DeviceFarm.Client.exceptions.NotFoundException
    DeviceFarm.Client.exceptions.LimitExceededException
    DeviceFarm.Client.exceptions.ServiceAccountException
    
    """
    pass

def update_test_grid_project(projectArn=None, name=None, description=None):
    """
    Change details of a project.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_test_grid_project(
        projectArn='string',
        name='string',
        description='string'
    )
    
    
    :type projectArn: string
    :param projectArn: [REQUIRED]\nARN of the project to update.\n

    :type name: string
    :param name: Human-readable name for the project.

    :type description: string
    :param description: Human-readable description for the project.

    :rtype: dict

ReturnsResponse Syntax
{
    'testGridProject': {
        'arn': 'string',
        'name': 'string',
        'description': 'string',
        'created': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --

testGridProject (dict) --
The project, including updated information.

arn (string) --
The ARN for the project.

name (string) --
A human-readable name for the project.

description (string) --
A human-readable description for the project.

created (datetime) --
When the project was created.









Exceptions

DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.InternalServiceException


    :return: {
        'testGridProject': {
            'arn': 'string',
            'name': 'string',
            'description': 'string',
            'created': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    DeviceFarm.Client.exceptions.NotFoundException
    DeviceFarm.Client.exceptions.ArgumentException
    DeviceFarm.Client.exceptions.InternalServiceException
    
    """
    pass

def update_upload(arn=None, name=None, contentType=None, editContent=None):
    """
    Updates an uploaded test spec.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_upload(
        arn='string',
        name='string',
        contentType='string',
        editContent=True|False
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the uploaded test spec.\n

    :type name: string
    :param name: The upload\'s test spec file name. The name must not contain any forward slashes (/). The test spec file name must end with the .yaml or .yml file extension.

    :type contentType: string
    :param contentType: The upload\'s content type (for example, application/x-yaml ).

    :type editContent: boolean
    :param editContent: Set to true if the YAML file has changed and must be updated. Otherwise, set to false.

    :rtype: dict

ReturnsResponse Syntax
{
    'upload': {
        'arn': 'string',
        'name': 'string',
        'created': datetime(2015, 1, 1),
        'type': 'ANDROID_APP'|'IOS_APP'|'WEB_APP'|'EXTERNAL_DATA'|'APPIUM_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_PYTHON_TEST_PACKAGE'|'APPIUM_NODE_TEST_PACKAGE'|'APPIUM_RUBY_TEST_PACKAGE'|'APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_WEB_PYTHON_TEST_PACKAGE'|'APPIUM_WEB_NODE_TEST_PACKAGE'|'APPIUM_WEB_RUBY_TEST_PACKAGE'|'CALABASH_TEST_PACKAGE'|'INSTRUMENTATION_TEST_PACKAGE'|'UIAUTOMATION_TEST_PACKAGE'|'UIAUTOMATOR_TEST_PACKAGE'|'XCTEST_TEST_PACKAGE'|'XCTEST_UI_TEST_PACKAGE'|'APPIUM_JAVA_JUNIT_TEST_SPEC'|'APPIUM_JAVA_TESTNG_TEST_SPEC'|'APPIUM_PYTHON_TEST_SPEC'|'APPIUM_NODE_TEST_SPEC'|'APPIUM_RUBY_TEST_SPEC'|'APPIUM_WEB_JAVA_JUNIT_TEST_SPEC'|'APPIUM_WEB_JAVA_TESTNG_TEST_SPEC'|'APPIUM_WEB_PYTHON_TEST_SPEC'|'APPIUM_WEB_NODE_TEST_SPEC'|'APPIUM_WEB_RUBY_TEST_SPEC'|'INSTRUMENTATION_TEST_SPEC'|'XCTEST_UI_TEST_SPEC',
        'status': 'INITIALIZED'|'PROCESSING'|'SUCCEEDED'|'FAILED',
        'url': 'string',
        'metadata': 'string',
        'contentType': 'string',
        'message': 'string',
        'category': 'CURATED'|'PRIVATE'
    }
}


Response Structure

(dict) --

upload (dict) --
A test spec uploaded to Device Farm.

arn (string) --
The upload\'s ARN.

name (string) --
The upload\'s file name.

created (datetime) --
When the upload was created.

type (string) --
The upload\'s type.
Must be one of the following values:

ANDROID_APP
IOS_APP
WEB_APP
EXTERNAL_DATA
APPIUM_JAVA_JUNIT_TEST_PACKAGE
APPIUM_JAVA_TESTNG_TEST_PACKAGE
APPIUM_PYTHON_TEST_PACKAGE
APPIUM_NODE_TEST_PACKAGE
APPIUM_RUBY_TEST_PACKAGE
APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE
APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE
APPIUM_WEB_PYTHON_TEST_PACKAGE
APPIUM_WEB_NODE_TEST_PACKAGE
APPIUM_WEB_RUBY_TEST_PACKAGE
CALABASH_TEST_PACKAGE
INSTRUMENTATION_TEST_PACKAGE
UIAUTOMATION_TEST_PACKAGE
UIAUTOMATOR_TEST_PACKAGE
XCTEST_TEST_PACKAGE
XCTEST_UI_TEST_PACKAGE
APPIUM_JAVA_JUNIT_TEST_SPEC
APPIUM_JAVA_TESTNG_TEST_SPEC
APPIUM_PYTHON_TEST_SPEC
APPIUM_NODE_TEST_SPEC
APPIUM_RUBY_TEST_SPEC
APPIUM_WEB_JAVA_JUNIT_TEST_SPEC
APPIUM_WEB_JAVA_TESTNG_TEST_SPEC
APPIUM_WEB_PYTHON_TEST_SPEC
APPIUM_WEB_NODE_TEST_SPEC
APPIUM_WEB_RUBY_TEST_SPEC
INSTRUMENTATION_TEST_SPEC
XCTEST_UI_TEST_SPEC


status (string) --
The upload\'s status.
Must be one of the following values:

FAILED
INITIALIZED
PROCESSING
SUCCEEDED


url (string) --
The presigned Amazon S3 URL that was used to store a file using a PUT request.

metadata (string) --
The upload\'s metadata. For example, for Android, this contains information that is parsed from the manifest and is displayed in the AWS Device Farm console after the associated app is uploaded.

contentType (string) --
The upload\'s content type (for example, application/octet-stream ).

message (string) --
A message about the upload\'s result.

category (string) --
The upload\'s category. Allowed values include:

CURATED: An upload managed by AWS Device Farm.
PRIVATE: An upload managed by the AWS Device Farm customer.










Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.LimitExceededException
DeviceFarm.Client.exceptions.ServiceAccountException


    :return: {
        'upload': {
            'arn': 'string',
            'name': 'string',
            'created': datetime(2015, 1, 1),
            'type': 'ANDROID_APP'|'IOS_APP'|'WEB_APP'|'EXTERNAL_DATA'|'APPIUM_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_PYTHON_TEST_PACKAGE'|'APPIUM_NODE_TEST_PACKAGE'|'APPIUM_RUBY_TEST_PACKAGE'|'APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_WEB_PYTHON_TEST_PACKAGE'|'APPIUM_WEB_NODE_TEST_PACKAGE'|'APPIUM_WEB_RUBY_TEST_PACKAGE'|'CALABASH_TEST_PACKAGE'|'INSTRUMENTATION_TEST_PACKAGE'|'UIAUTOMATION_TEST_PACKAGE'|'UIAUTOMATOR_TEST_PACKAGE'|'XCTEST_TEST_PACKAGE'|'XCTEST_UI_TEST_PACKAGE'|'APPIUM_JAVA_JUNIT_TEST_SPEC'|'APPIUM_JAVA_TESTNG_TEST_SPEC'|'APPIUM_PYTHON_TEST_SPEC'|'APPIUM_NODE_TEST_SPEC'|'APPIUM_RUBY_TEST_SPEC'|'APPIUM_WEB_JAVA_JUNIT_TEST_SPEC'|'APPIUM_WEB_JAVA_TESTNG_TEST_SPEC'|'APPIUM_WEB_PYTHON_TEST_SPEC'|'APPIUM_WEB_NODE_TEST_SPEC'|'APPIUM_WEB_RUBY_TEST_SPEC'|'INSTRUMENTATION_TEST_SPEC'|'XCTEST_UI_TEST_SPEC',
            'status': 'INITIALIZED'|'PROCESSING'|'SUCCEEDED'|'FAILED',
            'url': 'string',
            'metadata': 'string',
            'contentType': 'string',
            'message': 'string',
            'category': 'CURATED'|'PRIVATE'
        }
    }
    
    
    :returns: 
    ANDROID_APP
    IOS_APP
    WEB_APP
    EXTERNAL_DATA
    APPIUM_JAVA_JUNIT_TEST_PACKAGE
    APPIUM_JAVA_TESTNG_TEST_PACKAGE
    APPIUM_PYTHON_TEST_PACKAGE
    APPIUM_NODE_TEST_PACKAGE
    APPIUM_RUBY_TEST_PACKAGE
    APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE
    APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE
    APPIUM_WEB_PYTHON_TEST_PACKAGE
    APPIUM_WEB_NODE_TEST_PACKAGE
    APPIUM_WEB_RUBY_TEST_PACKAGE
    CALABASH_TEST_PACKAGE
    INSTRUMENTATION_TEST_PACKAGE
    UIAUTOMATION_TEST_PACKAGE
    UIAUTOMATOR_TEST_PACKAGE
    XCTEST_TEST_PACKAGE
    XCTEST_UI_TEST_PACKAGE
    APPIUM_JAVA_JUNIT_TEST_SPEC
    APPIUM_JAVA_TESTNG_TEST_SPEC
    APPIUM_PYTHON_TEST_SPEC
    APPIUM_NODE_TEST_SPEC
    APPIUM_RUBY_TEST_SPEC
    APPIUM_WEB_JAVA_JUNIT_TEST_SPEC
    APPIUM_WEB_JAVA_TESTNG_TEST_SPEC
    APPIUM_WEB_PYTHON_TEST_SPEC
    APPIUM_WEB_NODE_TEST_SPEC
    APPIUM_WEB_RUBY_TEST_SPEC
    INSTRUMENTATION_TEST_SPEC
    XCTEST_UI_TEST_SPEC
    
    """
    pass

def update_vpce_configuration(arn=None, vpceConfigurationName=None, vpceServiceName=None, serviceDnsName=None, vpceConfigurationDescription=None):
    """
    Updates information about an Amazon Virtual Private Cloud (VPC) endpoint configuration.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_vpce_configuration(
        arn='string',
        vpceConfigurationName='string',
        vpceServiceName='string',
        serviceDnsName='string',
        vpceConfigurationDescription='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the VPC endpoint configuration you want to update.\n

    :type vpceConfigurationName: string
    :param vpceConfigurationName: The friendly name you give to your VPC endpoint configuration to manage your configurations more easily.

    :type vpceServiceName: string
    :param vpceServiceName: The name of the VPC endpoint service running in your AWS account that you want Device Farm to test.

    :type serviceDnsName: string
    :param serviceDnsName: The DNS (domain) name used to connect to your private service in your VPC. The DNS name must not already be in use on the internet.

    :type vpceConfigurationDescription: string
    :param vpceConfigurationDescription: An optional description that provides details about your VPC endpoint configuration.

    :rtype: dict

ReturnsResponse Syntax
{
    'vpceConfiguration': {
        'arn': 'string',
        'vpceConfigurationName': 'string',
        'vpceServiceName': 'string',
        'serviceDnsName': 'string',
        'vpceConfigurationDescription': 'string'
    }
}


Response Structure

(dict) --

vpceConfiguration (dict) --
An object that contains information about your VPC endpoint configuration.

arn (string) --
The Amazon Resource Name (ARN) of the VPC endpoint configuration.

vpceConfigurationName (string) --
The friendly name you give to your VPC endpoint configuration to manage your configurations more easily.

vpceServiceName (string) --
The name of the VPC endpoint service running in your AWS account that you want Device Farm to test.

serviceDnsName (string) --
The DNS name that maps to the private IP address of the service you want to access.

vpceConfigurationDescription (string) --
An optional description that provides details about your VPC endpoint configuration.









Exceptions

DeviceFarm.Client.exceptions.ArgumentException
DeviceFarm.Client.exceptions.NotFoundException
DeviceFarm.Client.exceptions.ServiceAccountException
DeviceFarm.Client.exceptions.InvalidOperationException


    :return: {
        'vpceConfiguration': {
            'arn': 'string',
            'vpceConfigurationName': 'string',
            'vpceServiceName': 'string',
            'serviceDnsName': 'string',
            'vpceConfigurationDescription': 'string'
        }
    }
    
    
    :returns: 
    DeviceFarm.Client.exceptions.ArgumentException
    DeviceFarm.Client.exceptions.NotFoundException
    DeviceFarm.Client.exceptions.ServiceAccountException
    DeviceFarm.Client.exceptions.InvalidOperationException
    
    """
    pass

