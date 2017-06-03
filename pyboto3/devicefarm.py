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

def create_device_pool(projectArn=None, name=None, description=None, rules=None):
    """
    Creates a device pool.
    See also: AWS API Documentation
    
    Examples
    The following example creates a new device pool named MyDevicePool inside an existing project.
    Expected Output:
    
    :example: response = client.create_device_pool(
        projectArn='string',
        name='string',
        description='string',
        rules=[
            {
                'attribute': 'ARN'|'PLATFORM'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'APPIUM_VERSION',
                'operator': 'EQUALS'|'LESS_THAN'|'GREATER_THAN'|'IN'|'NOT_IN'|'CONTAINS',
                'value': 'string'
            },
        ]
    )
    
    
    :type projectArn: string
    :param projectArn: [REQUIRED]
            The ARN of the project for the device pool.
            

    :type name: string
    :param name: [REQUIRED]
            The device pool's name.
            

    :type description: string
    :param description: The device pool's description.

    :type rules: list
    :param rules: [REQUIRED]
            The device pool's rules.
            (dict) --Represents a condition for a device pool.
            attribute (string) --The rule's stringified attribute. For example, specify the value as '\'abc\'' .
            Allowed values include:
            ARN: The ARN.
            FORM_FACTOR: The form factor (for example, phone or tablet).
            MANUFACTURER: The manufacturer.
            PLATFORM: The platform (for example, Android or iOS).
            REMOTE_ACCESS_ENABLED: Whether the device is enabled for remote access.
            APPIUM_VERSION: The Appium version for the test.
            operator (string) --The rule's operator.
            EQUALS: The equals operator.
            GREATER_THAN: The greater-than operator.
            IN: The in operator.
            LESS_THAN: The less-than operator.
            NOT_IN: The not-in operator.
            CONTAINS: The contains operator.
            value (string) --The rule's value.
            
            

    :rtype: dict
    :return: {
        'devicePool': {
            'arn': 'string',
            'name': 'string',
            'description': 'string',
            'type': 'CURATED'|'PRIVATE',
            'rules': [
                {
                    'attribute': 'ARN'|'PLATFORM'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'APPIUM_VERSION',
                    'operator': 'EQUALS'|'LESS_THAN'|'GREATER_THAN'|'IN'|'NOT_IN'|'CONTAINS',
                    'value': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    CURATED: A device pool that is created and managed by AWS Device Farm.
    PRIVATE: A device pool that is created and managed by the device pool developer.
    
    """
    pass

def create_network_profile(projectArn=None, name=None, description=None, type=None, uplinkBandwidthBits=None, downlinkBandwidthBits=None, uplinkDelayMs=None, downlinkDelayMs=None, uplinkJitterMs=None, downlinkJitterMs=None, uplinkLossPercent=None, downlinkLossPercent=None):
    """
    Creates a network profile.
    See also: AWS API Documentation
    
    
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
    :param projectArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the project for which you want to create a network profile.
            

    :type name: string
    :param name: [REQUIRED]
            The name you wish to specify for the new network profile.
            

    :type description: string
    :param description: The description of the network profile.

    :type type: string
    :param type: The type of network profile you wish to create. Valid values are listed below.

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

def create_project(name=None, defaultJobTimeoutMinutes=None):
    """
    Creates a new project.
    See also: AWS API Documentation
    
    Examples
    The following example creates a new project named MyProject.
    Expected Output:
    
    :example: response = client.create_project(
        name='string',
        defaultJobTimeoutMinutes=123
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            The project's name.
            

    :type defaultJobTimeoutMinutes: integer
    :param defaultJobTimeoutMinutes: Sets the execution timeout value (in minutes) for a project. All test runs in this project will use the specified execution timeout value unless overridden when scheduling a run.

    :rtype: dict
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

def create_remote_access_session(projectArn=None, deviceArn=None, name=None, configuration=None):
    """
    Specifies and starts a remote access session.
    See also: AWS API Documentation
    
    Examples
    The following example creates a remote access session named MySession.
    Expected Output:
    
    :example: response = client.create_remote_access_session(
        projectArn='string',
        deviceArn='string',
        name='string',
        configuration={
            'billingMethod': 'METERED'|'UNMETERED'
        }
    )
    
    
    :type projectArn: string
    :param projectArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the project for which you want to create a remote access session.
            

    :type deviceArn: string
    :param deviceArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the device for which you want to create a remote access session.
            

    :type name: string
    :param name: The name of the remote access session that you wish to create.

    :type configuration: dict
    :param configuration: The configuration information for the remote access session request.
            billingMethod (string) --Returns the billing method for purposes of configuring a remote access session.
            

    :rtype: dict
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
                'fleetType': 'string',
                'fleetName': 'string'
            },
            'billingMethod': 'METERED'|'UNMETERED',
            'deviceMinutes': {
                'total': 123.0,
                'metered': 123.0,
                'unmetered': 123.0
            },
            'endpoint': 'string'
        }
    }
    
    
    :returns: 
    PENDING: A pending status.
    PENDING_CONCURRENCY: A pending concurrency status.
    PENDING_DEVICE: A pending device status.
    PROCESSING: A processing status.
    SCHEDULING: A scheduling status.
    PREPARING: A preparing status.
    RUNNING: A running status.
    COMPLETED: A completed status.
    STOPPING: A stopping status.
    
    """
    pass

def create_upload(projectArn=None, name=None, type=None, contentType=None):
    """
    Uploads an app or test scripts.
    See also: AWS API Documentation
    
    Examples
    The following example creates a new Appium Python test package upload inside an existing project.
    Expected Output:
    
    :example: response = client.create_upload(
        projectArn='string',
        name='string',
        type='ANDROID_APP'|'IOS_APP'|'WEB_APP'|'EXTERNAL_DATA'|'APPIUM_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_PYTHON_TEST_PACKAGE'|'APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_WEB_PYTHON_TEST_PACKAGE'|'CALABASH_TEST_PACKAGE'|'INSTRUMENTATION_TEST_PACKAGE'|'UIAUTOMATION_TEST_PACKAGE'|'UIAUTOMATOR_TEST_PACKAGE'|'XCTEST_TEST_PACKAGE'|'XCTEST_UI_TEST_PACKAGE',
        contentType='string'
    )
    
    
    :type projectArn: string
    :param projectArn: [REQUIRED]
            The ARN of the project for the upload.
            

    :type name: string
    :param name: [REQUIRED]
            The upload's file name. The name should not contain the '/' character. If uploading an iOS app, the file name needs to end with the .ipa extension. If uploading an Android app, the file name needs to end with the .apk extension. For all others, the file name must end with the .zip file extension.
            

    :type type: string
    :param type: [REQUIRED]
            The upload's upload type.
            Must be one of the following values:
            ANDROID_APP: An Android upload.
            IOS_APP: An iOS upload.
            WEB_APP: A web appliction upload.
            EXTERNAL_DATA: An external data upload.
            APPIUM_JAVA_JUNIT_TEST_PACKAGE: An Appium Java JUnit test package upload.
            APPIUM_JAVA_TESTNG_TEST_PACKAGE: An Appium Java TestNG test package upload.
            APPIUM_PYTHON_TEST_PACKAGE: An Appium Python test package upload.
            APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE: An Appium Java JUnit test package upload.
            APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE: An Appium Java TestNG test package upload.
            APPIUM_WEB_PYTHON_TEST_PACKAGE: An Appium Python test package upload.
            CALABASH_TEST_PACKAGE: A Calabash test package upload.
            INSTRUMENTATION_TEST_PACKAGE: An instrumentation upload.
            UIAUTOMATION_TEST_PACKAGE: A uiautomation test package upload.
            UIAUTOMATOR_TEST_PACKAGE: A uiautomator test package upload.
            XCTEST_TEST_PACKAGE: An XCode test package upload.
            XCTEST_UI_TEST_PACKAGE: An XCode UI test package upload.
            Note If you call CreateUpload with WEB_APP specified, AWS Device Farm throws an ArgumentException error.
            

    :type contentType: string
    :param contentType: The upload's content type (for example, 'application/octet-stream').

    :rtype: dict
    :return: {
        'upload': {
            'arn': 'string',
            'name': 'string',
            'created': datetime(2015, 1, 1),
            'type': 'ANDROID_APP'|'IOS_APP'|'WEB_APP'|'EXTERNAL_DATA'|'APPIUM_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_PYTHON_TEST_PACKAGE'|'APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_WEB_PYTHON_TEST_PACKAGE'|'CALABASH_TEST_PACKAGE'|'INSTRUMENTATION_TEST_PACKAGE'|'UIAUTOMATION_TEST_PACKAGE'|'UIAUTOMATOR_TEST_PACKAGE'|'XCTEST_TEST_PACKAGE'|'XCTEST_UI_TEST_PACKAGE',
            'status': 'INITIALIZED'|'PROCESSING'|'SUCCEEDED'|'FAILED',
            'url': 'string',
            'metadata': 'string',
            'contentType': 'string',
            'message': 'string'
        }
    }
    
    
    :returns: 
    ANDROID_APP: An Android upload.
    IOS_APP: An iOS upload.
    WEB_APP: A web appliction upload.
    EXTERNAL_DATA: An external data upload.
    APPIUM_JAVA_JUNIT_TEST_PACKAGE: An Appium Java JUnit test package upload.
    APPIUM_JAVA_TESTNG_TEST_PACKAGE: An Appium Java TestNG test package upload.
    APPIUM_PYTHON_TEST_PACKAGE: An Appium Python test package upload.
    APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE: An Appium Java JUnit test package upload.
    APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE: An Appium Java TestNG test package upload.
    APPIUM_WEB_PYTHON_TEST_PACKAGE: An Appium Python test package upload.
    CALABASH_TEST_PACKAGE: A Calabash test package upload.
    INSTRUMENTATION_TEST_PACKAGE: An instrumentation upload.
    UIAUTOMATION_TEST_PACKAGE: A uiautomation test package upload.
    UIAUTOMATOR_TEST_PACKAGE: A uiautomator test package upload.
    XCTEST_TEST_PACKAGE: An XCode test package upload.
    XCTEST_UI_TEST_PACKAGE: An XCode UI test package upload.
    
    """
    pass

def delete_device_pool(arn=None):
    """
    Deletes a device pool given the pool ARN. Does not allow deletion of curated pools owned by the system.
    See also: AWS API Documentation
    
    Examples
    The following example deletes a specific device pool.
    Expected Output:
    
    :example: response = client.delete_device_pool(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            Represents the Amazon Resource Name (ARN) of the Device Farm device pool you wish to delete.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_network_profile(arn=None):
    """
    Deletes a network profile.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_network_profile(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The Amazon Resource Name (ARN) of the network profile you want to delete.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_project(arn=None):
    """
    Deletes an AWS Device Farm project, given the project ARN.
    See also: AWS API Documentation
    
    Examples
    The following example deletes a specific project.
    Expected Output:
    
    :example: response = client.delete_project(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            Represents the Amazon Resource Name (ARN) of the Device Farm project you wish to delete.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_remote_access_session(arn=None):
    """
    Deletes a completed remote access session and its results.
    See also: AWS API Documentation
    
    Examples
    The following example deletes a specific remote access session.
    Expected Output:
    
    :example: response = client.delete_remote_access_session(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The Amazon Resource Name (ARN) of the sesssion for which you want to delete remote access.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_run(arn=None):
    """
    Deletes the run, given the run ARN.
    See also: AWS API Documentation
    
    Examples
    The following example deletes a specific test run.
    Expected Output:
    
    :example: response = client.delete_run(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The Amazon Resource Name (ARN) for the run you wish to delete.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_upload(arn=None):
    """
    Deletes an upload given the upload ARN.
    See also: AWS API Documentation
    
    Examples
    The following example deletes a specific upload.
    Expected Output:
    
    :example: response = client.delete_upload(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            Represents the Amazon Resource Name (ARN) of the Device Farm upload you wish to delete.
            

    :rtype: dict
    :return: {}
    
    
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

def get_account_settings():
    """
    Returns the number of unmetered iOS and/or unmetered Android devices that have been purchased by the account.
    See also: AWS API Documentation
    
    Examples
    The following example returns information about your Device Farm account settings.
    Expected Output:
    
    :example: response = client.get_account_settings()
    
    
    :rtype: dict
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
            'defaultJobTimeoutMinutes': 123
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
    
    Examples
    The following example returns information about a specific device.
    Expected Output:
    
    :example: response = client.get_device(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The device type's ARN.
            

    :rtype: dict
    :return: {
        'device': {
            'arn': 'string',
            'name': 'string',
            'manufacturer': 'string',
            'model': 'string',
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
            'fleetType': 'string',
            'fleetName': 'string'
        }
    }
    
    
    :returns: 
    ANDROID: The Android platform.
    IOS: The iOS platform.
    
    """
    pass

def get_device_pool(arn=None):
    """
    Gets information about a device pool.
    See also: AWS API Documentation
    
    Examples
    The following example returns information about a specific device pool, given a project ARN.
    Expected Output:
    
    :example: response = client.get_device_pool(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The device pool's ARN.
            

    :rtype: dict
    :return: {
        'devicePool': {
            'arn': 'string',
            'name': 'string',
            'description': 'string',
            'type': 'CURATED'|'PRIVATE',
            'rules': [
                {
                    'attribute': 'ARN'|'PLATFORM'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'APPIUM_VERSION',
                    'operator': 'EQUALS'|'LESS_THAN'|'GREATER_THAN'|'IN'|'NOT_IN'|'CONTAINS',
                    'value': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    ARN: The ARN.
    FORM_FACTOR: The form factor (for example, phone or tablet).
    MANUFACTURER: The manufacturer.
    PLATFORM: The platform (for example, Android or iOS).
    REMOTE_ACCESS_ENABLED: Whether the device is enabled for remote access.
    APPIUM_VERSION: The Appium version for the test.
    
    """
    pass

def get_device_pool_compatibility(devicePoolArn=None, appArn=None, testType=None, test=None):
    """
    Gets information about compatibility with a device pool.
    See also: AWS API Documentation
    
    Examples
    The following example returns information about the compatibility of a specific device pool, given its ARN.
    Expected Output:
    
    :example: response = client.get_device_pool_compatibility(
        devicePoolArn='string',
        appArn='string',
        testType='BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI',
        test={
            'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI',
            'testPackageArn': 'string',
            'filter': 'string',
            'parameters': {
                'string': 'string'
            }
        }
    )
    
    
    :type devicePoolArn: string
    :param devicePoolArn: [REQUIRED]
            The device pool's ARN.
            

    :type appArn: string
    :param appArn: The ARN of the app that is associated with the specified device pool.

    :type testType: string
    :param testType: The test type for the specified device pool.
            Allowed values include the following:
            BUILTIN_FUZZ: The built-in fuzz type.
            BUILTIN_EXPLORER: For Android, an app explorer that will traverse an Android app, interacting with it and capturing screenshots at the same time.
            APPIUM_JAVA_JUNIT: The Appium Java JUnit type.
            APPIUM_JAVA_TESTNG: The Appium Java TestNG type.
            APPIUM_PYTHON: The Appium Python type.
            APPIUM_WEB_JAVA_JUNIT: The Appium Java JUnit type for Web apps.
            APPIUM_WEB_JAVA_TESTNG: The Appium Java TestNG type for Web apps.
            APPIUM_WEB_PYTHON: The Appium Python type for Web apps.
            CALABASH: The Calabash type.
            INSTRUMENTATION: The Instrumentation type.
            UIAUTOMATION: The uiautomation type.
            UIAUTOMATOR: The uiautomator type.
            XCTEST: The XCode test type.
            XCTEST_UI: The XCode UI test type.
            

    :type test: dict
    :param test: Information about the uploaded test to be run against the device pool.
            type (string) -- [REQUIRED]The test's type.
            Must be one of the following values:
            BUILTIN_FUZZ: The built-in fuzz type.
            BUILTIN_EXPLORER: For Android, an app explorer that will traverse an Android app, interacting with it and capturing screenshots at the same time.
            APPIUM_JAVA_JUNIT: The Appium Java JUnit type.
            APPIUM_JAVA_TESTNG: The Appium Java TestNG type.
            APPIUM_PYTHON: The Appium Python type.
            APPIUM_WEB_JAVA_JUNIT: The Appium Java JUnit type for Web apps.
            APPIUM_WEB_JAVA_TESTNG: The Appium Java TestNG type for Web apps.
            APPIUM_WEB_PYTHON: The Appium Python type for Web apps.
            CALABASH: The Calabash type.
            INSTRUMENTATION: The Instrumentation type.
            UIAUTOMATION: The uiautomation type.
            UIAUTOMATOR: The uiautomator type.
            XCTEST: The XCode test type.
            XCTEST_UI: The XCode UI test type.
            testPackageArn (string) --The ARN of the uploaded test that will be run.
            filter (string) --The test's filter.
            parameters (dict) --The test's parameters, such as the following test framework parameters and fixture settings:
            For Calabash tests:
            profile: A cucumber profile, for example, 'my_profile_name'.
            tags: You can limit execution to features or scenarios that have (or don't have) certain tags, for example, '@smoke' or '@smoke,~@wip'.
            For Appium tests (all types):
            appium_version: The Appium version. Currently supported values are '1.4.16', '1.6.3', 'latest', and 'default'.
             latest  will run the latest Appium version supported by Device Farm (1.6.3).
            For  default , Device Farm will choose a compatible version of Appium for the device. The current behavior is to run 1.4.16 on Android devices and iOS 9 and earlier, 1.6.3 for iOS 10 and later.
            This behavior is subject to change.
            For Fuzz tests (Android only):
            event_count: The number of events, between 1 and 10000, that the UI fuzz test should perform.
            throttle: The time, in ms, between 0 and 1000, that the UI fuzz test should wait between events.
            seed: A seed to use for randomizing the UI fuzz test. Using the same seed value between tests ensures identical event sequences.
            For Explorer tests:
            username: A username to use if the Explorer encounters a login form. If not supplied, no username will be inserted.
            password: A password to use if the Explorer encounters a login form. If not supplied, no password will be inserted.
            For Instrumentation:
            filter: A test filter string. Examples:
            Running a single test case: 'com.android.abc.Test1'
            Running a single test: 'com.android.abc.Test1#smoke'
            Running multiple tests: 'com.android.abc.Test1,com.android.abc.Test2'
            For XCTest and XCTestUI:
            filter: A test filter string. Examples:
            Running a single test class: 'LoginTests'
            Running a multiple test classes: 'LoginTests,SmokeTests'
            Running a single test: 'LoginTests/testValid'
            Running multiple tests: 'LoginTests/testValid,LoginTests/testInvalid'
            For UIAutomator:
            filter: A test filter string. Examples:
            Running a single test case: 'com.android.abc.Test1'
            Running a single test: 'com.android.abc.Test1#smoke'
            Running multiple tests: 'com.android.abc.Test1,com.android.abc.Test2'
            
            (string) --
            (string) --
            
            

    :rtype: dict
    :return: {
        'compatibleDevices': [
            {
                'device': {
                    'arn': 'string',
                    'name': 'string',
                    'manufacturer': 'string',
                    'model': 'string',
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
                    'fleetType': 'string',
                    'fleetName': 'string'
                },
                'compatible': True|False,
                'incompatibilityMessages': [
                    {
                        'message': 'string',
                        'type': 'ARN'|'PLATFORM'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'APPIUM_VERSION'
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
                    'fleetType': 'string',
                    'fleetName': 'string'
                },
                'compatible': True|False,
                'incompatibilityMessages': [
                    {
                        'message': 'string',
                        'type': 'ARN'|'PLATFORM'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'APPIUM_VERSION'
                    },
                ]
            },
        ]
    }
    
    
    :returns: 
    PHONE: The phone form factor.
    TABLET: The tablet form factor.
    
    """
    pass

def get_job(arn=None):
    """
    Gets information about a job.
    See also: AWS API Documentation
    
    Examples
    The following example returns information about a specific job.
    Expected Output:
    
    :example: response = client.get_job(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The job's ARN.
            

    :rtype: dict
    :return: {
        'job': {
            'arn': 'string',
            'name': 'string',
            'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI',
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
                'fleetType': 'string',
                'fleetName': 'string'
            },
            'deviceMinutes': {
                'total': 123.0,
                'metered': 123.0,
                'unmetered': 123.0
            }
        }
    }
    
    
    :returns: 
    PENDING: A pending status.
    PENDING_CONCURRENCY: A pending concurrency status.
    PENDING_DEVICE: A pending device status.
    PROCESSING: A processing status.
    SCHEDULING: A scheduling status.
    PREPARING: A preparing status.
    RUNNING: A running status.
    COMPLETED: A completed status.
    STOPPING: A stopping status.
    
    """
    pass

def get_network_profile(arn=None):
    """
    Returns information about a network profile.
    See also: AWS API Documentation
    
    
    :example: response = client.get_network_profile(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The Amazon Resource Name (ARN) of the network profile you want to return information about.
            

    :rtype: dict
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
    Gets the current status and future status of all offerings purchased by an AWS account. The response indicates how many offerings are currently available and the offerings that will be available in the next period. The API returns a NotEligible error if the user is not permitted to invoke the operation. Please contact aws-devicefarm-support@amazon.com if you believe that you should be able to invoke this operation.
    See also: AWS API Documentation
    
    Examples
    The following example returns information about Device Farm offerings available to your account.
    Expected Output:
    
    :example: response = client.get_offering_status(
        nextToken='string'
    )
    
    
    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :rtype: dict
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
    :param operation_name: The operation name. This is the same name
            as the method name on the client. For example, if the
            method name is create_foo, and you'd normally invoke the
            operation as client.create_foo(**kwargs), if the
            create_foo operation can be paginated, you can use the
            call client.get_paginator('create_foo').

    :rtype: L{botocore.paginate.Paginator}
    """
    pass

def get_project(arn=None):
    """
    Gets information about a project.
    See also: AWS API Documentation
    
    Examples
    The following example gets information about a specific project.
    Expected Output:
    
    :example: response = client.get_project(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The project's ARN.
            

    :rtype: dict
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
    
    Examples
    The following example gets a specific remote access session.
    Expected Output:
    
    :example: response = client.get_remote_access_session(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The Amazon Resource Name (ARN) of the remote access session about which you want to get session information.
            

    :rtype: dict
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
                'fleetType': 'string',
                'fleetName': 'string'
            },
            'billingMethod': 'METERED'|'UNMETERED',
            'deviceMinutes': {
                'total': 123.0,
                'metered': 123.0,
                'unmetered': 123.0
            },
            'endpoint': 'string'
        }
    }
    
    
    :returns: 
    PENDING: A pending condition.
    PASSED: A passing condition.
    WARNED: A warning condition.
    FAILED: A failed condition.
    SKIPPED: A skipped condition.
    ERRORED: An error condition.
    STOPPED: A stopped condition.
    
    """
    pass

def get_run(arn=None):
    """
    Gets information about a run.
    See also: AWS API Documentation
    
    Examples
    The following example gets information about a specific test run.
    Expected Output:
    
    :example: response = client.get_run(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The run's ARN.
            

    :rtype: dict
    :return: {
        'run': {
            'arn': 'string',
            'name': 'string',
            'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI',
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
            }
        }
    }
    
    
    :returns: 
    ANDROID: The Android platform.
    IOS: The iOS platform.
    
    """
    pass

def get_suite(arn=None):
    """
    Gets information about a suite.
    See also: AWS API Documentation
    
    Examples
    The following example gets information about a specific test suite.
    Expected Output:
    
    :example: response = client.get_suite(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The suite's ARN.
            

    :rtype: dict
    :return: {
        'suite': {
            'arn': 'string',
            'name': 'string',
            'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI',
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
    PENDING: A pending status.
    PENDING_CONCURRENCY: A pending concurrency status.
    PENDING_DEVICE: A pending device status.
    PROCESSING: A processing status.
    SCHEDULING: A scheduling status.
    PREPARING: A preparing status.
    RUNNING: A running status.
    COMPLETED: A completed status.
    STOPPING: A stopping status.
    
    """
    pass

def get_test(arn=None):
    """
    Gets information about a test.
    See also: AWS API Documentation
    
    Examples
    The following example gets information about a specific test.
    Expected Output:
    
    :example: response = client.get_test(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The test's ARN.
            

    :rtype: dict
    :return: {
        'test': {
            'arn': 'string',
            'name': 'string',
            'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI',
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
    PENDING: A pending status.
    PENDING_CONCURRENCY: A pending concurrency status.
    PENDING_DEVICE: A pending device status.
    PROCESSING: A processing status.
    SCHEDULING: A scheduling status.
    PREPARING: A preparing status.
    RUNNING: A running status.
    COMPLETED: A completed status.
    STOPPING: A stopping status.
    
    """
    pass

def get_upload(arn=None):
    """
    Gets information about an upload.
    See also: AWS API Documentation
    
    Examples
    The following example gets information about a specific upload.
    Expected Output:
    
    :example: response = client.get_upload(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The upload's ARN.
            

    :rtype: dict
    :return: {
        'upload': {
            'arn': 'string',
            'name': 'string',
            'created': datetime(2015, 1, 1),
            'type': 'ANDROID_APP'|'IOS_APP'|'WEB_APP'|'EXTERNAL_DATA'|'APPIUM_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_PYTHON_TEST_PACKAGE'|'APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_WEB_PYTHON_TEST_PACKAGE'|'CALABASH_TEST_PACKAGE'|'INSTRUMENTATION_TEST_PACKAGE'|'UIAUTOMATION_TEST_PACKAGE'|'UIAUTOMATOR_TEST_PACKAGE'|'XCTEST_TEST_PACKAGE'|'XCTEST_UI_TEST_PACKAGE',
            'status': 'INITIALIZED'|'PROCESSING'|'SUCCEEDED'|'FAILED',
            'url': 'string',
            'metadata': 'string',
            'contentType': 'string',
            'message': 'string'
        }
    }
    
    
    :returns: 
    FAILED: A failed status.
    INITIALIZED: An initialized status.
    PROCESSING: A processing status.
    SUCCEEDED: A succeeded status.
    
    """
    pass

def get_waiter():
    """
    
    """
    pass

def install_to_remote_access_session(remoteAccessSessionArn=None, appArn=None):
    """
    Installs an application to the device in a remote access session. For Android applications, the file must be in .apk format. For iOS applications, the file must be in .ipa format.
    See also: AWS API Documentation
    
    Examples
    The following example installs a specific app to a device in a specific remote access session.
    Expected Output:
    
    :example: response = client.install_to_remote_access_session(
        remoteAccessSessionArn='string',
        appArn='string'
    )
    
    
    :type remoteAccessSessionArn: string
    :param remoteAccessSessionArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the remote access session about which you are requesting information.
            

    :type appArn: string
    :param appArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the app about which you are requesting information.
            

    :rtype: dict
    :return: {
        'appUpload': {
            'arn': 'string',
            'name': 'string',
            'created': datetime(2015, 1, 1),
            'type': 'ANDROID_APP'|'IOS_APP'|'WEB_APP'|'EXTERNAL_DATA'|'APPIUM_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_PYTHON_TEST_PACKAGE'|'APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_WEB_PYTHON_TEST_PACKAGE'|'CALABASH_TEST_PACKAGE'|'INSTRUMENTATION_TEST_PACKAGE'|'UIAUTOMATION_TEST_PACKAGE'|'UIAUTOMATOR_TEST_PACKAGE'|'XCTEST_TEST_PACKAGE'|'XCTEST_UI_TEST_PACKAGE',
            'status': 'INITIALIZED'|'PROCESSING'|'SUCCEEDED'|'FAILED',
            'url': 'string',
            'metadata': 'string',
            'contentType': 'string',
            'message': 'string'
        }
    }
    
    
    :returns: 
    ANDROID_APP: An Android upload.
    IOS_APP: An iOS upload.
    WEB_APP: A web appliction upload.
    EXTERNAL_DATA: An external data upload.
    APPIUM_JAVA_JUNIT_TEST_PACKAGE: An Appium Java JUnit test package upload.
    APPIUM_JAVA_TESTNG_TEST_PACKAGE: An Appium Java TestNG test package upload.
    APPIUM_PYTHON_TEST_PACKAGE: An Appium Python test package upload.
    APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE: An Appium Java JUnit test package upload.
    APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE: An Appium Java TestNG test package upload.
    APPIUM_WEB_PYTHON_TEST_PACKAGE: An Appium Python test package upload.
    CALABASH_TEST_PACKAGE: A Calabash test package upload.
    INSTRUMENTATION_TEST_PACKAGE: An instrumentation upload.
    UIAUTOMATION_TEST_PACKAGE: A uiautomation test package upload.
    UIAUTOMATOR_TEST_PACKAGE: A uiautomator test package upload.
    XCTEST_TEST_PACKAGE: An XCode test package upload.
    XCTEST_UI_TEST_PACKAGE: An XCode UI test package upload.
    
    """
    pass

def list_artifacts(arn=None, type=None, nextToken=None):
    """
    Gets information about artifacts.
    See also: AWS API Documentation
    
    Examples
    The following example lists screenshot artifacts for a specific run.
    Expected Output:
    
    :example: response = client.list_artifacts(
        arn='string',
        type='SCREENSHOT'|'FILE'|'LOG',
        nextToken='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The Run, Job, Suite, or Test ARN.
            

    :type type: string
    :param type: [REQUIRED]
            The artifacts' type.
            Allowed values include:
            FILE: The artifacts are files.
            LOG: The artifacts are logs.
            SCREENSHOT: The artifacts are screenshots.
            

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :rtype: dict
    :return: {
        'artifacts': [
            {
                'arn': 'string',
                'name': 'string',
                'type': 'UNKNOWN'|'SCREENSHOT'|'DEVICE_LOG'|'MESSAGE_LOG'|'VIDEO_LOG'|'RESULT_LOG'|'SERVICE_LOG'|'WEBKIT_LOG'|'INSTRUMENTATION_OUTPUT'|'EXERCISER_MONKEY_OUTPUT'|'CALABASH_JSON_OUTPUT'|'CALABASH_PRETTY_OUTPUT'|'CALABASH_STANDARD_OUTPUT'|'CALABASH_JAVA_XML_OUTPUT'|'AUTOMATION_OUTPUT'|'APPIUM_SERVER_OUTPUT'|'APPIUM_JAVA_OUTPUT'|'APPIUM_JAVA_XML_OUTPUT'|'APPIUM_PYTHON_OUTPUT'|'APPIUM_PYTHON_XML_OUTPUT'|'EXPLORER_EVENT_LOG'|'EXPLORER_SUMMARY_LOG'|'APPLICATION_CRASH_REPORT'|'XCTEST_LOG'|'VIDEO',
                'extension': 'string',
                'url': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    UNKNOWN: An unknown type.
    SCREENSHOT: The screenshot type.
    DEVICE_LOG: The device log type.
    MESSAGE_LOG: The message log type.
    RESULT_LOG: The result log type.
    SERVICE_LOG: The service log type.
    WEBKIT_LOG: The web kit log type.
    INSTRUMENTATION_OUTPUT: The instrumentation type.
    EXERCISER_MONKEY_OUTPUT: For Android, the artifact (log) generated by an Android fuzz test.
    CALABASH_JSON_OUTPUT: The Calabash JSON output type.
    CALABASH_PRETTY_OUTPUT: The Calabash pretty output type.
    CALABASH_STANDARD_OUTPUT: The Calabash standard output type.
    CALABASH_JAVA_XML_OUTPUT: The Calabash Java XML output type.
    AUTOMATION_OUTPUT: The automation output type.
    APPIUM_SERVER_OUTPUT: The Appium server output type.
    APPIUM_JAVA_OUTPUT: The Appium Java output type.
    APPIUM_JAVA_XML_OUTPUT: The Appium Java XML output type.
    APPIUM_PYTHON_OUTPUT: The Appium Python output type.
    APPIUM_PYTHON_XML_OUTPUT: The Appium Python XML output type.
    EXPLORER_EVENT_LOG: The Explorer event log output type.
    EXPLORER_SUMMARY_LOG: The Explorer summary log output type.
    APPLICATION_CRASH_REPORT: The application crash report output type.
    XCTEST_LOG: The XCode test output type.
    
    """
    pass

def list_device_pools(arn=None, type=None, nextToken=None):
    """
    Gets information about device pools.
    See also: AWS API Documentation
    
    Examples
    The following example returns information about the private device pools in a specific project.
    Expected Output:
    
    :example: response = client.list_device_pools(
        arn='string',
        type='CURATED'|'PRIVATE',
        nextToken='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The project ARN.
            

    :type type: string
    :param type: The device pools' type.
            Allowed values include:
            CURATED: A device pool that is created and managed by AWS Device Farm.
            PRIVATE: A device pool that is created and managed by the device pool developer.
            

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :rtype: dict
    :return: {
        'devicePools': [
            {
                'arn': 'string',
                'name': 'string',
                'description': 'string',
                'type': 'CURATED'|'PRIVATE',
                'rules': [
                    {
                        'attribute': 'ARN'|'PLATFORM'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'APPIUM_VERSION',
                        'operator': 'EQUALS'|'LESS_THAN'|'GREATER_THAN'|'IN'|'NOT_IN'|'CONTAINS',
                        'value': 'string'
                    },
                ]
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    CURATED: A device pool that is created and managed by AWS Device Farm.
    PRIVATE: A device pool that is created and managed by the device pool developer.
    
    """
    pass

def list_devices(arn=None, nextToken=None):
    """
    Gets information about unique device types.
    See also: AWS API Documentation
    
    Examples
    The following example returns information about the available devices in a specific project.
    Expected Output:
    
    :example: response = client.list_devices(
        arn='string',
        nextToken='string'
    )
    
    
    :type arn: string
    :param arn: The Amazon Resource Name (ARN) of the project.

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :rtype: dict
    :return: {
        'devices': [
            {
                'arn': 'string',
                'name': 'string',
                'manufacturer': 'string',
                'model': 'string',
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
                'fleetType': 'string',
                'fleetName': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    PHONE: The phone form factor.
    TABLET: The tablet form factor.
    
    """
    pass

def list_jobs(arn=None, nextToken=None):
    """
    Gets information about jobs.
    See also: AWS API Documentation
    
    Examples
    The following example returns information about jobs in a specific project.
    Expected Output:
    
    :example: response = client.list_jobs(
        arn='string',
        nextToken='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The jobs' ARNs.
            

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :rtype: dict
    :return: {
        'jobs': [
            {
                'arn': 'string',
                'name': 'string',
                'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI',
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
                    'fleetType': 'string',
                    'fleetName': 'string'
                },
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
    BUILTIN_FUZZ: The built-in fuzz type.
    BUILTIN_EXPLORER: For Android, an app explorer that will traverse an Android app, interacting with it and capturing screenshots at the same time.
    APPIUM_JAVA_JUNIT: The Appium Java JUnit type.
    APPIUM_JAVA_TESTNG: The Appium Java TestNG type.
    APPIUM_PYTHON: The Appium Python type.
    APPIUM_WEB_JAVA_JUNIT: The Appium Java JUnit type for Web apps.
    APPIUM_WEB_JAVA_TESTNG: The Appium Java TestNG type for Web apps.
    APPIUM_WEB_PYTHON: The Appium Python type for Web apps.
    CALABASH: The Calabash type.
    INSTRUMENTATION: The Instrumentation type.
    UIAUTOMATION: The uiautomation type.
    UIAUTOMATOR: The uiautomator type.
    XCTEST: The XCode test type.
    XCTEST_UI: The XCode UI test type.
    
    """
    pass

def list_network_profiles(arn=None, type=None, nextToken=None):
    """
    Returns the list of available network profiles.
    See also: AWS API Documentation
    
    
    :example: response = client.list_network_profiles(
        arn='string',
        type='CURATED'|'PRIVATE',
        nextToken='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The Amazon Resource Name (ARN) of the project for which you want to list network profiles.
            

    :type type: string
    :param type: The type of network profile you wish to return information about. Valid values are listed below.

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :rtype: dict
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
    
    
    """
    pass

def list_offering_promotions(nextToken=None):
    """
    Returns a list of offering promotions. Each offering promotion record contains the ID and description of the promotion. The API returns a NotEligible error if the caller is not permitted to invoke the operation. Contact aws-devicefarm-support@amazon.com if you believe that you should be able to invoke this operation.
    See also: AWS API Documentation
    
    
    :example: response = client.list_offering_promotions(
        nextToken='string'
    )
    
    
    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :rtype: dict
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
    Returns a list of all historical purchases, renewals, and system renewal transactions for an AWS account. The list is paginated and ordered by a descending timestamp (most recent transactions are first). The API returns a NotEligible error if the user is not permitted to invoke the operation. Please contact aws-devicefarm-support@amazon.com if you believe that you should be able to invoke this operation.
    See also: AWS API Documentation
    
    Examples
    The following example returns information about Device Farm offering transactions.
    Expected Output:
    
    :example: response = client.list_offering_transactions(
        nextToken='string'
    )
    
    
    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :rtype: dict
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
    Returns a list of products or offerings that the user can manage through the API. Each offering record indicates the recurring price per unit and the frequency for that offering. The API returns a NotEligible error if the user is not permitted to invoke the operation. Please contact aws-devicefarm-support@amazon.com if you believe that you should be able to invoke this operation.
    See also: AWS API Documentation
    
    Examples
    The following example returns information about available device offerings.
    Expected Output:
    
    :example: response = client.list_offerings(
        nextToken='string'
    )
    
    
    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :rtype: dict
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
    
    
    """
    pass

def list_remote_access_sessions(arn=None, nextToken=None):
    """
    Returns a list of all currently running remote access sessions.
    See also: AWS API Documentation
    
    Examples
    The following example returns information about a specific Device Farm remote access session.
    Expected Output:
    
    :example: response = client.list_remote_access_sessions(
        arn='string',
        nextToken='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The Amazon Resource Name (ARN) of the remote access session about which you are requesting information.
            

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :rtype: dict
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
                    'fleetType': 'string',
                    'fleetName': 'string'
                },
                'billingMethod': 'METERED'|'UNMETERED',
                'deviceMinutes': {
                    'total': 123.0,
                    'metered': 123.0,
                    'unmetered': 123.0
                },
                'endpoint': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    PENDING: A pending status.
    PENDING_CONCURRENCY: A pending concurrency status.
    PENDING_DEVICE: A pending device status.
    PROCESSING: A processing status.
    SCHEDULING: A scheduling status.
    PREPARING: A preparing status.
    RUNNING: A running status.
    COMPLETED: A completed status.
    STOPPING: A stopping status.
    
    """
    pass

def list_runs(arn=None, nextToken=None):
    """
    Gets information about runs, given an AWS Device Farm project ARN.
    See also: AWS API Documentation
    
    Examples
    The following example returns information about a specific test run.
    Expected Output:
    
    :example: response = client.list_runs(
        arn='string',
        nextToken='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The Amazon Resource Name (ARN) of the project for which you want to list runs.
            

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :rtype: dict
    :return: {
        'runs': [
            {
                'arn': 'string',
                'name': 'string',
                'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI',
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
                }
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    BUILTIN_FUZZ: The built-in fuzz type.
    BUILTIN_EXPLORER: For Android, an app explorer that will traverse an Android app, interacting with it and capturing screenshots at the same time.
    APPIUM_JAVA_JUNIT: The Appium Java JUnit type.
    APPIUM_JAVA_TESTNG: The Appium Java TestNG type.
    APPIUM_PYTHON: The Appium Python type.
    APPIUM_WEB_JAVA_JUNIT: The Appium Java JUnit type for Web apps.
    APPIUM_WEB_JAVA_TESTNG: The Appium Java TestNG type for Web apps.
    APPIUM_WEB_PYTHON: The Appium Python type for Web apps.
    CALABASH: The Calabash type.
    INSTRUMENTATION: The Instrumentation type.
    UIAUTOMATION: The uiautomation type.
    UIAUTOMATOR: The uiautomator type.
    XCTEST: The XCode test type.
    XCTEST_UI: The XCode UI test type.
    
    """
    pass

def list_samples(arn=None, nextToken=None):
    """
    Gets information about samples, given an AWS Device Farm project ARN
    See also: AWS API Documentation
    
    Examples
    The following example returns information about samples, given a specific Device Farm project.
    Expected Output:
    
    :example: response = client.list_samples(
        arn='string',
        nextToken='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The Amazon Resource Name (ARN) of the project for which you want to list samples.
            

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :rtype: dict
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
    Gets information about suites.
    See also: AWS API Documentation
    
    Examples
    The following example returns information about suites, given a specific Device Farm project.
    Expected Output:
    
    :example: response = client.list_suites(
        arn='string',
        nextToken='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The suites' ARNs.
            

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :rtype: dict
    :return: {
        'suites': [
            {
                'arn': 'string',
                'name': 'string',
                'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI',
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
    BUILTIN_FUZZ: The built-in fuzz type.
    BUILTIN_EXPLORER: For Android, an app explorer that will traverse an Android app, interacting with it and capturing screenshots at the same time.
    APPIUM_JAVA_JUNIT: The Appium Java JUnit type.
    APPIUM_JAVA_TESTNG: The Appium Java TestNG type.
    APPIUM_PYTHON: The Appium Python type.
    APPIUM_WEB_JAVA_JUNIT: The Appium Java JUnit type for Web apps.
    APPIUM_WEB_JAVA_TESTNG: The Appium Java TestNG type for Web apps.
    APPIUM_WEB_PYTHON: The Appium Python type for Web apps.
    CALABASH: The Calabash type.
    INSTRUMENTATION: The Instrumentation type.
    UIAUTOMATION: The uiautomation type.
    UIAUTOMATOR: The uiautomator type.
    XCTEST: The XCode test type.
    XCTEST_UI: The XCode UI test type.
    
    """
    pass

def list_tests(arn=None, nextToken=None):
    """
    Gets information about tests.
    See also: AWS API Documentation
    
    Examples
    The following example returns information about tests, given a specific Device Farm project.
    Expected Output:
    
    :example: response = client.list_tests(
        arn='string',
        nextToken='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The tests' ARNs.
            

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :rtype: dict
    :return: {
        'tests': [
            {
                'arn': 'string',
                'name': 'string',
                'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI',
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
    BUILTIN_FUZZ: The built-in fuzz type.
    BUILTIN_EXPLORER: For Android, an app explorer that will traverse an Android app, interacting with it and capturing screenshots at the same time.
    APPIUM_JAVA_JUNIT: The Appium Java JUnit type.
    APPIUM_JAVA_TESTNG: The Appium Java TestNG type.
    APPIUM_PYTHON: The Appium Python type.
    APPIUM_WEB_JAVA_JUNIT: The Appium Java JUnit type for Web apps.
    APPIUM_WEB_JAVA_TESTNG: The Appium Java TestNG type for Web apps.
    APPIUM_WEB_PYTHON: The Appium Python type for Web apps.
    CALABASH: The Calabash type.
    INSTRUMENTATION: The Instrumentation type.
    UIAUTOMATION: The uiautomation type.
    UIAUTOMATOR: The uiautomator type.
    XCTEST: The XCode test type.
    XCTEST_UI: The XCode UI test type.
    
    """
    pass

def list_unique_problems(arn=None, nextToken=None):
    """
    Gets information about unique problems.
    See also: AWS API Documentation
    
    Examples
    The following example returns information about unique problems, given a specific Device Farm project.
    Expected Output:
    
    :example: response = client.list_unique_problems(
        arn='string',
        nextToken='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The unique problems' ARNs.
            

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :rtype: dict
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
                                'fleetType': 'string',
                                'fleetName': 'string'
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
    PENDING: A pending condition.
    PASSED: A passing condition.
    WARNED: A warning condition.
    FAILED: A failed condition.
    SKIPPED: A skipped condition.
    ERRORED: An error condition.
    STOPPED: A stopped condition.
    
    """
    pass

def list_uploads(arn=None, nextToken=None):
    """
    Gets information about uploads, given an AWS Device Farm project ARN.
    See also: AWS API Documentation
    
    Examples
    The following example returns information about uploads, given a specific Device Farm project.
    Expected Output:
    
    :example: response = client.list_uploads(
        arn='string',
        nextToken='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The Amazon Resource Name (ARN) of the project for which you want to list uploads.
            

    :type nextToken: string
    :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

    :rtype: dict
    :return: {
        'uploads': [
            {
                'arn': 'string',
                'name': 'string',
                'created': datetime(2015, 1, 1),
                'type': 'ANDROID_APP'|'IOS_APP'|'WEB_APP'|'EXTERNAL_DATA'|'APPIUM_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_PYTHON_TEST_PACKAGE'|'APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_WEB_PYTHON_TEST_PACKAGE'|'CALABASH_TEST_PACKAGE'|'INSTRUMENTATION_TEST_PACKAGE'|'UIAUTOMATION_TEST_PACKAGE'|'UIAUTOMATOR_TEST_PACKAGE'|'XCTEST_TEST_PACKAGE'|'XCTEST_UI_TEST_PACKAGE',
                'status': 'INITIALIZED'|'PROCESSING'|'SUCCEEDED'|'FAILED',
                'url': 'string',
                'metadata': 'string',
                'contentType': 'string',
                'message': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    ANDROID_APP: An Android upload.
    IOS_APP: An iOS upload.
    WEB_APP: A web appliction upload.
    EXTERNAL_DATA: An external data upload.
    APPIUM_JAVA_JUNIT_TEST_PACKAGE: An Appium Java JUnit test package upload.
    APPIUM_JAVA_TESTNG_TEST_PACKAGE: An Appium Java TestNG test package upload.
    APPIUM_PYTHON_TEST_PACKAGE: An Appium Python test package upload.
    APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE: An Appium Java JUnit test package upload.
    APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE: An Appium Java TestNG test package upload.
    APPIUM_WEB_PYTHON_TEST_PACKAGE: An Appium Python test package upload.
    CALABASH_TEST_PACKAGE: A Calabash test package upload.
    INSTRUMENTATION_TEST_PACKAGE: An instrumentation upload.
    UIAUTOMATION_TEST_PACKAGE: A uiautomation test package upload.
    UIAUTOMATOR_TEST_PACKAGE: A uiautomator test package upload.
    XCTEST_TEST_PACKAGE: An XCode test package upload.
    XCTEST_UI_TEST_PACKAGE: An XCode UI test package upload.
    
    """
    pass

def purchase_offering(offeringId=None, quantity=None, offeringPromotionId=None):
    """
    Immediately purchases offerings for an AWS account. Offerings renew with the latest total purchased quantity for an offering, unless the renewal was overridden. The API returns a NotEligible error if the user is not permitted to invoke the operation. Please contact aws-devicefarm-support@amazon.com if you believe that you should be able to invoke this operation.
    See also: AWS API Documentation
    
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
    :param quantity: The number of device slots you wish to purchase in an offering request.

    :type offeringPromotionId: string
    :param offeringPromotionId: The ID of the offering promotion to be applied to the purchase.

    :rtype: dict
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
    
    
    """
    pass

def renew_offering(offeringId=None, quantity=None):
    """
    Explicitly sets the quantity of devices to renew for an offering, starting from the effectiveDate of the next period. The API returns a NotEligible error if the user is not permitted to invoke the operation. Please contact aws-devicefarm-support@amazon.com if you believe that you should be able to invoke this operation.
    See also: AWS API Documentation
    
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
    
    
    """
    pass

def schedule_run(projectArn=None, appArn=None, devicePoolArn=None, name=None, test=None, configuration=None, executionConfiguration=None):
    """
    Schedules a run.
    See also: AWS API Documentation
    
    Examples
    The following example schedules a test run named MyRun.
    Expected Output:
    
    :example: response = client.schedule_run(
        projectArn='string',
        appArn='string',
        devicePoolArn='string',
        name='string',
        test={
            'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI',
            'testPackageArn': 'string',
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
            'appPackagesCleanup': True|False
        }
    )
    
    
    :type projectArn: string
    :param projectArn: [REQUIRED]
            The ARN of the project for the run to be scheduled.
            

    :type appArn: string
    :param appArn: The ARN of the app to schedule a run.

    :type devicePoolArn: string
    :param devicePoolArn: [REQUIRED]
            The ARN of the device pool for the run to be scheduled.
            

    :type name: string
    :param name: The name for the run to be scheduled.

    :type test: dict
    :param test: [REQUIRED]
            Information about the test for the run to be scheduled.
            type (string) -- [REQUIRED]The test's type.
            Must be one of the following values:
            BUILTIN_FUZZ: The built-in fuzz type.
            BUILTIN_EXPLORER: For Android, an app explorer that will traverse an Android app, interacting with it and capturing screenshots at the same time.
            APPIUM_JAVA_JUNIT: The Appium Java JUnit type.
            APPIUM_JAVA_TESTNG: The Appium Java TestNG type.
            APPIUM_PYTHON: The Appium Python type.
            APPIUM_WEB_JAVA_JUNIT: The Appium Java JUnit type for Web apps.
            APPIUM_WEB_JAVA_TESTNG: The Appium Java TestNG type for Web apps.
            APPIUM_WEB_PYTHON: The Appium Python type for Web apps.
            CALABASH: The Calabash type.
            INSTRUMENTATION: The Instrumentation type.
            UIAUTOMATION: The uiautomation type.
            UIAUTOMATOR: The uiautomator type.
            XCTEST: The XCode test type.
            XCTEST_UI: The XCode UI test type.
            testPackageArn (string) --The ARN of the uploaded test that will be run.
            filter (string) --The test's filter.
            parameters (dict) --The test's parameters, such as the following test framework parameters and fixture settings:
            For Calabash tests:
            profile: A cucumber profile, for example, 'my_profile_name'.
            tags: You can limit execution to features or scenarios that have (or don't have) certain tags, for example, '@smoke' or '@smoke,~@wip'.
            For Appium tests (all types):
            appium_version: The Appium version. Currently supported values are '1.4.16', '1.6.3', 'latest', and 'default'.
             latest  will run the latest Appium version supported by Device Farm (1.6.3).
            For  default , Device Farm will choose a compatible version of Appium for the device. The current behavior is to run 1.4.16 on Android devices and iOS 9 and earlier, 1.6.3 for iOS 10 and later.
            This behavior is subject to change.
            For Fuzz tests (Android only):
            event_count: The number of events, between 1 and 10000, that the UI fuzz test should perform.
            throttle: The time, in ms, between 0 and 1000, that the UI fuzz test should wait between events.
            seed: A seed to use for randomizing the UI fuzz test. Using the same seed value between tests ensures identical event sequences.
            For Explorer tests:
            username: A username to use if the Explorer encounters a login form. If not supplied, no username will be inserted.
            password: A password to use if the Explorer encounters a login form. If not supplied, no password will be inserted.
            For Instrumentation:
            filter: A test filter string. Examples:
            Running a single test case: 'com.android.abc.Test1'
            Running a single test: 'com.android.abc.Test1#smoke'
            Running multiple tests: 'com.android.abc.Test1,com.android.abc.Test2'
            For XCTest and XCTestUI:
            filter: A test filter string. Examples:
            Running a single test class: 'LoginTests'
            Running a multiple test classes: 'LoginTests,SmokeTests'
            Running a single test: 'LoginTests/testValid'
            Running multiple tests: 'LoginTests/testValid,LoginTests/testInvalid'
            For UIAutomator:
            filter: A test filter string. Examples:
            Running a single test case: 'com.android.abc.Test1'
            Running a single test: 'com.android.abc.Test1#smoke'
            Running multiple tests: 'com.android.abc.Test1,com.android.abc.Test2'
            
            (string) --
            (string) --
            
            

    :type configuration: dict
    :param configuration: Information about the settings for the run to be scheduled.
            extraDataPackageArn (string) --The ARN of the extra data for the run. The extra data is a .zip file that AWS Device Farm will extract to external data for Android or the app's sandbox for iOS.
            networkProfileArn (string) --Reserved for internal use.
            locale (string) --Information about the locale that is used for the run.
            location (dict) --Information about the location that is used for the run.
            latitude (float) -- [REQUIRED]The latitude.
            longitude (float) -- [REQUIRED]The longitude.
            radios (dict) --Information about the radio states for the run.
            wifi (boolean) --True if Wi-Fi is enabled at the beginning of the test; otherwise, false.
            bluetooth (boolean) --True if Bluetooth is enabled at the beginning of the test; otherwise, false.
            nfc (boolean) --True if NFC is enabled at the beginning of the test; otherwise, false.
            gps (boolean) --True if GPS is enabled at the beginning of the test; otherwise, false.
            auxiliaryApps (list) --A list of auxiliary apps for the run.
            (string) --
            billingMethod (string) --Specifies the billing method for a test run: metered or unmetered . If the parameter is not specified, the default value is metered .
            

    :type executionConfiguration: dict
    :param executionConfiguration: Specifies configuration information about a test run, such as the execution timeout (in minutes).
            jobTimeoutMinutes (integer) --The number of minutes a test run will execute before it times out.
            accountsCleanup (boolean) --True if account cleanup is enabled at the beginning of the test; otherwise, false.
            appPackagesCleanup (boolean) --True if app package cleanup is enabled at the beginning of the test; otherwise, false.
            

    :rtype: dict
    :return: {
        'run': {
            'arn': 'string',
            'name': 'string',
            'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI',
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
            }
        }
    }
    
    
    :returns: 
    BUILTIN_FUZZ: The built-in fuzz type.
    BUILTIN_EXPLORER: For Android, an app explorer that will traverse an Android app, interacting with it and capturing screenshots at the same time.
    APPIUM_JAVA_JUNIT: The Appium Java JUnit type.
    APPIUM_JAVA_TESTNG: The Appium Java TestNG type.
    APPIUM_PYTHON: The Appium Python type.
    APPIUM_WEB_JAVA_JUNIT: The Appium Java JUnit type for Web apps.
    APPIUM_WEB_JAVA_TESTNG: The Appium Java TestNG type for Web apps.
    APPIUM_WEB_PYTHON: The Appium Python type for Web apps.
    CALABASH: The Calabash type.
    INSTRUMENTATION: The Instrumentation type.
    UIAUTOMATION: The uiautomation type.
    UIAUTOMATOR: The uiautomator type.
    XCTEST: The XCode test type.
    XCTEST_UI: The XCode UI test type.
    
    """
    pass

def stop_remote_access_session(arn=None):
    """
    Ends a specified remote access session.
    See also: AWS API Documentation
    
    
    :example: response = client.stop_remote_access_session(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The Amazon Resource Name (ARN) of the remote access session you wish to stop.
            

    :rtype: dict
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
                'fleetType': 'string',
                'fleetName': 'string'
            },
            'billingMethod': 'METERED'|'UNMETERED',
            'deviceMinutes': {
                'total': 123.0,
                'metered': 123.0,
                'unmetered': 123.0
            },
            'endpoint': 'string'
        }
    }
    
    
    :returns: 
    PENDING: A pending condition.
    PASSED: A passing condition.
    WARNED: A warning condition.
    FAILED: A failed condition.
    SKIPPED: A skipped condition.
    ERRORED: An error condition.
    STOPPED: A stopped condition.
    
    """
    pass

def stop_run(arn=None):
    """
    Initiates a stop request for the current test run. AWS Device Farm will immediately stop the run on devices where tests have not started executing, and you will not be billed for these devices. On devices where tests have started executing, Setup Suite and Teardown Suite tests will run to completion before stopping execution on those devices. You will be billed for Setup, Teardown, and any tests that were in progress or already completed.
    See also: AWS API Documentation
    
    Examples
    The following example stops a specific test run.
    Expected Output:
    
    :example: response = client.stop_run(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            Represents the Amazon Resource Name (ARN) of the Device Farm run you wish to stop.
            

    :rtype: dict
    :return: {
        'run': {
            'arn': 'string',
            'name': 'string',
            'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI',
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
            }
        }
    }
    
    
    :returns: 
    ANDROID: The Android platform.
    IOS: The iOS platform.
    
    """
    pass

def update_device_pool(arn=None, name=None, description=None, rules=None):
    """
    Modifies the name, description, and rules in a device pool given the attributes and the pool ARN. Rule updates are all-or-nothing, meaning they can only be updated as a whole (or not at all).
    See also: AWS API Documentation
    
    Examples
    The following example updates the specified device pool with a new name and description. It also enables remote access of devices in the device pool.
    Expected Output:
    
    :example: response = client.update_device_pool(
        arn='string',
        name='string',
        description='string',
        rules=[
            {
                'attribute': 'ARN'|'PLATFORM'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'APPIUM_VERSION',
                'operator': 'EQUALS'|'LESS_THAN'|'GREATER_THAN'|'IN'|'NOT_IN'|'CONTAINS',
                'value': 'string'
            },
        ]
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The Amazon Resourc Name (ARN) of the Device Farm device pool you wish to update.
            

    :type name: string
    :param name: A string representing the name of the device pool you wish to update.

    :type description: string
    :param description: A description of the device pool you wish to update.

    :type rules: list
    :param rules: Represents the rules you wish to modify for the device pool. Updating rules is optional; however, if you choose to update rules for your request, the update will replace the existing rules.
            (dict) --Represents a condition for a device pool.
            attribute (string) --The rule's stringified attribute. For example, specify the value as '\'abc\'' .
            Allowed values include:
            ARN: The ARN.
            FORM_FACTOR: The form factor (for example, phone or tablet).
            MANUFACTURER: The manufacturer.
            PLATFORM: The platform (for example, Android or iOS).
            REMOTE_ACCESS_ENABLED: Whether the device is enabled for remote access.
            APPIUM_VERSION: The Appium version for the test.
            operator (string) --The rule's operator.
            EQUALS: The equals operator.
            GREATER_THAN: The greater-than operator.
            IN: The in operator.
            LESS_THAN: The less-than operator.
            NOT_IN: The not-in operator.
            CONTAINS: The contains operator.
            value (string) --The rule's value.
            
            

    :rtype: dict
    :return: {
        'devicePool': {
            'arn': 'string',
            'name': 'string',
            'description': 'string',
            'type': 'CURATED'|'PRIVATE',
            'rules': [
                {
                    'attribute': 'ARN'|'PLATFORM'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'APPIUM_VERSION',
                    'operator': 'EQUALS'|'LESS_THAN'|'GREATER_THAN'|'IN'|'NOT_IN'|'CONTAINS',
                    'value': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    CURATED: A device pool that is created and managed by AWS Device Farm.
    PRIVATE: A device pool that is created and managed by the device pool developer.
    
    """
    pass

def update_network_profile(arn=None, name=None, description=None, type=None, uplinkBandwidthBits=None, downlinkBandwidthBits=None, uplinkDelayMs=None, downlinkDelayMs=None, uplinkJitterMs=None, downlinkJitterMs=None, uplinkLossPercent=None, downlinkLossPercent=None):
    """
    Updates the network profile with specific settings.
    See also: AWS API Documentation
    
    
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
    :param arn: [REQUIRED]
            The Amazon Resource Name (ARN) of the project that you wish to update network profile settings.
            

    :type name: string
    :param name: The name of the network profile about which you are returning information.

    :type description: string
    :param description: The descriptoin of the network profile about which you are returning information.

    :type type: string
    :param type: The type of network profile you wish to return information about. Valid values are listed below.

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

def update_project(arn=None, name=None, defaultJobTimeoutMinutes=None):
    """
    Modifies the specified project name, given the project ARN and a new name.
    See also: AWS API Documentation
    
    Examples
    The following example updates the specified project with a new name.
    Expected Output:
    
    :example: response = client.update_project(
        arn='string',
        name='string',
        defaultJobTimeoutMinutes=123
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]
            The Amazon Resource Name (ARN) of the project whose name you wish to update.
            

    :type name: string
    :param name: A string representing the new name of the project that you are updating.

    :type defaultJobTimeoutMinutes: integer
    :param defaultJobTimeoutMinutes: The number of minutes a test run in the project will execute before it times out.

    :rtype: dict
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

