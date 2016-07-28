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

import boto3


class Devicefarm(object):
    def __init__(self):
        self.client = boto3.client('Devicefarm')

    def can_paginate(self, operation_name=None):
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
        self.client.can_paginate(operation_name=operation_name)

    def create_device_pool(self, projectArn=None, name=None, description=None, rules=None):
        """
        :param projectArn: [REQUIRED]
            The ARN of the project for the device pool.
            
        :type projectArn: string
        :param name: [REQUIRED]
            The device pool's name.
            
        :type name: string
        :param description: The device pool's description.
        :type description: string
        :param rules: [REQUIRED]
            The device pool's rules.
            (dict) --Represents a condition for a device pool.
            attribute (string) --The rule's stringified attribute. For example, specify the value as '\'abc\'' .
            Allowed values include:
            ARN: The ARN.
            FORM_FACTOR: The form factor (for example, phone or tablet).
            MANUFACTURER: The manufacturer.
            PLATFORM: The platform (for example, Android or iOS).
            operator (string) --The rule's operator.
            EQUALS: The equals operator.
            GREATER_THAN: The greater-than operator.
            IN: The in operator.
            LESS_THAN: The less-than operator.
            NOT_IN: The not-in operator.
            value (string) --The rule's value.
            
            
        :type rules: list
        """
        self.client.create_device_pool(projectArn=projectArn, name=name, description=description, rules=rules)

    def create_project(self, name=None):
        """
        :param name: [REQUIRED]
            The project's name.
            Return typedict
            ReturnsResponse Syntax{
              'project': {
                'arn': 'string',
                'name': 'string',
                'created': datetime(2015, 1, 1)
              }
            }
            Response Structure
            (dict) --Represents the result of a create project request.
            project (dict) --The newly created project.
            arn (string) --The project's ARN.
            name (string) --The project's name.
            created (datetime) --When the project was created.
            
            
            
        :type name: string
        """
        self.client.create_project(name=name)

    def create_remote_access_session(self, projectArn=None, deviceArn=None, name=None, configuration=None):
        """
        :param projectArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the project for which you want to create a remote access session.
            
        :type projectArn: string
        :param deviceArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the device for which you want to create a remote access session.
            
        :type deviceArn: string
        :param name: The name of the remote access session that you wish to create.
        :type name: string
        :param configuration: The configuration information for the remote access session request.
            billingMethod (string) --Returns the billing method for purposes of configuring a remote access session.
            
        :type configuration: dict
        """
        self.client.create_remote_access_session(projectArn=projectArn, deviceArn=deviceArn, name=name,
                                                 configuration=configuration)

    def create_upload(self, projectArn=None, name=None, type=None, contentType=None):
        """
        :param projectArn: [REQUIRED]
            The ARN of the project for the upload.
            
        :type projectArn: string
        :param name: [REQUIRED]
            The upload's file name. The name should not contain the '/' character.
            
        :type name: string
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
            
        :type type: string
        :param contentType: The upload's content type (for example, 'application/octet-stream').
        :type contentType: string
        """
        self.client.create_upload(projectArn=projectArn, name=name, type=type, contentType=contentType)

    def delete_device_pool(self, arn=None):
        """
        :param arn: [REQUIRED]
            Represents the Amazon Resource Name (ARN) of the Device Farm device pool you wish to delete.
            Return typedict
            ReturnsResponse Syntax{}
            Response Structure
            (dict) --Represents the result of a delete device pool request.
            
            
        :type arn: string
        """
        self.client.delete_device_pool(arn=arn)

    def delete_project(self, arn=None):
        """
        :param arn: [REQUIRED]
            Represents the Amazon Resource Name (ARN) of the Device Farm project you wish to delete.
            Return typedict
            ReturnsResponse Syntax{}
            Response Structure
            (dict) --Represents the result of a delete project request.
            
            
        :type arn: string
        """
        self.client.delete_project(arn=arn)

    def delete_remote_access_session(self, arn=None):
        """
        :param arn: [REQUIRED]
            The Amazon Resource Name (ARN) of the sesssion for which you want to delete remote access.
            Return typedict
            ReturnsResponse Syntax{}
            Response Structure
            (dict) --The response from the server when a request is made to delete the remote access session.
            
            
        :type arn: string
        """
        self.client.delete_remote_access_session(arn=arn)

    def delete_run(self, arn=None):
        """
        :param arn: [REQUIRED]
            The Amazon Resource Name (ARN) for the run you wish to delete.
            Return typedict
            ReturnsResponse Syntax{}
            Response Structure
            (dict) --Represents the result of a delete run request.
            
            
        :type arn: string
        """
        self.client.delete_run(arn=arn)

    def delete_upload(self, arn=None):
        """
        :param arn: [REQUIRED]
            Represents the Amazon Resource Name (ARN) of the Device Farm upload you wish to delete.
            Return typedict
            ReturnsResponse Syntax{}
            Response Structure
            (dict) --Represents the result of a delete upload request.
            
            
        :type arn: string
        """
        self.client.delete_upload(arn=arn)

    def generate_presigned_url(self, ClientMethod=None, Params=None, ExpiresIn=None, HttpMethod=None):
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
        self.client.generate_presigned_url(ClientMethod=ClientMethod, Params=Params, ExpiresIn=ExpiresIn,
                                           HttpMethod=HttpMethod)

    def get_account_settings(self):
        """
        """
        self.client.get_account_settings()

    def get_device(self, arn=None):
        """
        :param arn: [REQUIRED]
            The device type's ARN.
            Return typedict
            ReturnsResponse Syntax{
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
            Response Structure
            (dict) --Represents the result of a get device request.
            device (dict) --Represents a device type that an app is tested against.
            arn (string) --The device's ARN.
            name (string) --The device's display name.
            manufacturer (string) --The device's manufacturer name.
            model (string) --The device's model name.
            formFactor (string) --The device's form factor.
            Allowed values include:
            PHONE: The phone form factor.
            TABLET: The tablet form factor.
            platform (string) --The device's platform.
            Allowed values include:
            ANDROID: The Android platform.
            IOS: The iOS platform.
            os (string) --The device's operating system type.
            cpu (dict) --Information about the device's CPU.
            frequency (string) --The CPU's frequency.
            architecture (string) --The CPU's architecture, for example x86 or ARM.
            clock (float) --The clock speed of the device's CPU, expressed in hertz (Hz). For example, a 1.2 GHz CPU is expressed as 1200000000.
            resolution (dict) --Represents the screen resolution of a device in height and width, expressed in pixels.
            width (integer) --The screen resolution's width, expressed in pixels.
            height (integer) --The screen resolution's height, expressed in pixels.
            heapSize (integer) --The device's heap size, expressed in bytes.
            memory (integer) --The device's total memory size, expressed in bytes.
            image (string) --The device's image name.
            carrier (string) --The device's carrier.
            radio (string) --The device's radio.
            remoteAccessEnabled (boolean) --Specifies whether remote access has been enabled for the specified device.
            fleetType (string) --The type of fleet to which this device belongs. Possible values for fleet type are PRIVATE and PUBLIC.
            fleetName (string) --The name of the fleet to which this device belongs.
            
            
            
        :type arn: string
        """
        self.client.get_device(arn=arn)

    def get_device_pool(self, arn=None):
        """
        :param arn: [REQUIRED]
            The device pool's ARN.
            Return typedict
            ReturnsResponse Syntax{
              'devicePool': {
                'arn': 'string',
                'name': 'string',
                'description': 'string',
                'type': 'CURATED'|'PRIVATE',
                'rules': [
                  {
                    'attribute': 'ARN'|'PLATFORM'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED',
                    'operator': 'EQUALS'|'LESS_THAN'|'GREATER_THAN'|'IN'|'NOT_IN',
                    'value': 'string'
                  },
                ]
              }
            }
            Response Structure
            (dict) --Represents the result of a get device pool request.
            devicePool (dict) --Represents a collection of device types.
            arn (string) --The device pool's ARN.
            name (string) --The device pool's name.
            description (string) --The device pool's description.
            type (string) --The device pool's type.
            Allowed values include:
            CURATED: A device pool that is created and managed by AWS Device Farm.
            PRIVATE: A device pool that is created and managed by the device pool developer.
            rules (list) --Information about the device pool's rules.
            (dict) --Represents a condition for a device pool.
            attribute (string) --The rule's stringified attribute. For example, specify the value as '\'abc\'' .
            Allowed values include:
            ARN: The ARN.
            FORM_FACTOR: The form factor (for example, phone or tablet).
            MANUFACTURER: The manufacturer.
            PLATFORM: The platform (for example, Android or iOS).
            operator (string) --The rule's operator.
            EQUALS: The equals operator.
            GREATER_THAN: The greater-than operator.
            IN: The in operator.
            LESS_THAN: The less-than operator.
            NOT_IN: The not-in operator.
            value (string) --The rule's value.
            
            
            
            
        :type arn: string
        """
        self.client.get_device_pool(arn=arn)

    def get_device_pool_compatibility(self, devicePoolArn=None, appArn=None, testType=None):
        """
        :param devicePoolArn: [REQUIRED]
            The device pool's ARN.
            
        :type devicePoolArn: string
        :param appArn: The ARN of the app that is associated with the specified device pool.
        :type appArn: string
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
            
        :type testType: string
        """
        self.client.get_device_pool_compatibility(devicePoolArn=devicePoolArn, appArn=appArn, testType=testType)

    def get_job(self, arn=None):
        """
        :param arn: [REQUIRED]
            The job's ARN.
            Return typedict
            ReturnsResponse Syntax{
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
            Response Structure
            (dict) --Represents the result of a get job request.
            job (dict) --Represents a device.
            arn (string) --The job's ARN.
            name (string) --The job's name.
            type (string) --The job's type.
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
            created (datetime) --When the job was created.
            status (string) --The job's status.
            Allowed values include:
            PENDING: A pending status.
            PENDING_CONCURRENCY: A pending concurrency status.
            PENDING_DEVICE: A pending device status.
            PROCESSING: A processing status.
            SCHEDULING: A scheduling status.
            PREPARING: A preparing status.
            RUNNING: A running status.
            COMPLETED: A completed status.
            STOPPING: A stopping status.
            result (string) --The job's result.
            Allowed values include:
            PENDING: A pending condition.
            PASSED: A passing condition.
            WARNED: A warning condition.
            FAILED: A failed condition.
            SKIPPED: A skipped condition.
            ERRORED: An error condition.
            STOPPED: A stopped condition.
            started (datetime) --The job's start time.
            stopped (datetime) --The job's stop time.
            counters (dict) --The job's result counters.
            total (integer) --The total number of entities.
            passed (integer) --The number of passed entities.
            failed (integer) --The number of failed entities.
            warned (integer) --The number of warned entities.
            errored (integer) --The number of errored entities.
            stopped (integer) --The number of stopped entities.
            skipped (integer) --The number of skipped entities.
            message (string) --A message about the job's result.
            device (dict) --Represents a device type that an app is tested against.
            arn (string) --The device's ARN.
            name (string) --The device's display name.
            manufacturer (string) --The device's manufacturer name.
            model (string) --The device's model name.
            formFactor (string) --The device's form factor.
            Allowed values include:
            PHONE: The phone form factor.
            TABLET: The tablet form factor.
            platform (string) --The device's platform.
            Allowed values include:
            ANDROID: The Android platform.
            IOS: The iOS platform.
            os (string) --The device's operating system type.
            cpu (dict) --Information about the device's CPU.
            frequency (string) --The CPU's frequency.
            architecture (string) --The CPU's architecture, for example x86 or ARM.
            clock (float) --The clock speed of the device's CPU, expressed in hertz (Hz). For example, a 1.2 GHz CPU is expressed as 1200000000.
            resolution (dict) --Represents the screen resolution of a device in height and width, expressed in pixels.
            width (integer) --The screen resolution's width, expressed in pixels.
            height (integer) --The screen resolution's height, expressed in pixels.
            heapSize (integer) --The device's heap size, expressed in bytes.
            memory (integer) --The device's total memory size, expressed in bytes.
            image (string) --The device's image name.
            carrier (string) --The device's carrier.
            radio (string) --The device's radio.
            remoteAccessEnabled (boolean) --Specifies whether remote access has been enabled for the specified device.
            fleetType (string) --The type of fleet to which this device belongs. Possible values for fleet type are PRIVATE and PUBLIC.
            fleetName (string) --The name of the fleet to which this device belongs.
            deviceMinutes (dict) --Represents the total (metered or unmetered) minutes used by the job.
            total (float) --When specified, represents the total minutes used by the resource to run tests.
            metered (float) --When specified, represents only the sum of metered minutes used by the resource to run tests.
            unmetered (float) --When specified, represents only the sum of unmetered minutes used by the resource to run tests.
            
            
            
        :type arn: string
        """
        self.client.get_job(arn=arn)

    def get_offering_status(self, nextToken=None):
        """
        :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
            Return typedict
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
            description (string) --A string describing the offering.
            type (string) --The type of offering (e.g., 'RECURRING') for a device.
            platform (string) --The platform of the device (e.g., ANDROID or IOS).
            recurringCharges (list) --Specifies whether there are recurring charges for the offering.
            (dict) --Specifies whether charges for devices will be recurring.
            cost (dict) --The cost of the recurring charge.
            amount (float) --The numerical amount of an offering or transaction.
            currencyCode (string) --The currency code of a monetary amount. For example, USD means 'U.S. dollars.'
            frequency (string) --The frequency in which charges will recur.
            
            quantity (integer) --The number of available devices in the offering.
            effectiveOn (datetime) --The date on which the offering is effective.
            
            nextPeriod (dict) --When specified, gets the offering status for the next period.
            (string) --
            (dict) --The status of the offering.
            type (string) --The type specified for the offering status.
            offering (dict) --Represents the metadata of an offering status.
            id (string) --The ID that corresponds to a device offering.
            description (string) --A string describing the offering.
            type (string) --The type of offering (e.g., 'RECURRING') for a device.
            platform (string) --The platform of the device (e.g., ANDROID or IOS).
            recurringCharges (list) --Specifies whether there are recurring charges for the offering.
            (dict) --Specifies whether charges for devices will be recurring.
            cost (dict) --The cost of the recurring charge.
            amount (float) --The numerical amount of an offering or transaction.
            currencyCode (string) --The currency code of a monetary amount. For example, USD means 'U.S. dollars.'
            frequency (string) --The frequency in which charges will recur.
            
            quantity (integer) --The number of available devices in the offering.
            effectiveOn (datetime) --The date on which the offering is effective.
            
            nextToken (string) --An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
            
            
        :type nextToken: string
        """
        self.client.get_offering_status(nextToken=nextToken)

    def get_paginator(self, operation_name=None):
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
        self.client.get_paginator(operation_name=operation_name)

    def get_project(self, arn=None):
        """
        :param arn: [REQUIRED]
            The project's ARN.
            Return typedict
            ReturnsResponse Syntax{
              'project': {
                'arn': 'string',
                'name': 'string',
                'created': datetime(2015, 1, 1)
              }
            }
            Response Structure
            (dict) --Represents the result of a get project request.
            project (dict) --Represents an operating-system neutral workspace for running and managing tests.
            arn (string) --The project's ARN.
            name (string) --The project's name.
            created (datetime) --When the project was created.
            
            
            
        :type arn: string
        """
        self.client.get_project(arn=arn)

    def get_remote_access_session(self, arn=None):
        """
        :param arn: [REQUIRED]
            The Amazon Resource Name (ARN) of the remote access session about which you want to get session information.
            Return typedict
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
            Response Structure
            (dict) --Represents the response from the server that lists detailed information about the remote access session.
            remoteAccessSession (dict) --A container that lists detailed information about the remote access session.
            arn (string) --The Amazon Resource Name (ARN) of the remote access session.
            name (string) --The name of the remote access session.
            created (datetime) --The date and time the remote access session was created.
            status (string) --The status of the remote access session. Can be any of the following:
            PENDING: A pending status.
            PENDING_CONCURRENCY: A pending concurrency status.
            PENDING_DEVICE: A pending device status.
            PROCESSING: A processing status.
            SCHEDULING: A scheduling status.
            PREPARING: A preparing status.
            RUNNING: A running status.
            COMPLETED: A completed status.
            STOPPING: A stopping status.
            result (string) --The result of the remote access session. Can be any of the following:
            PENDING: A pending condition.
            PASSED: A passing condition.
            WARNED: A warning condition.
            FAILED: A failed condition.
            SKIPPED: A skipped condition.
            ERRORED: An error condition.
            STOPPED: A stopped condition.
            message (string) --A message about the remote access session.
            started (datetime) --The date and time the remote access session was started.
            stopped (datetime) --The date and time the remote access session was stopped.
            device (dict) --Represents a device type that an app is tested against.
            arn (string) --The device's ARN.
            name (string) --The device's display name.
            manufacturer (string) --The device's manufacturer name.
            model (string) --The device's model name.
            formFactor (string) --The device's form factor.
            Allowed values include:
            PHONE: The phone form factor.
            TABLET: The tablet form factor.
            platform (string) --The device's platform.
            Allowed values include:
            ANDROID: The Android platform.
            IOS: The iOS platform.
            os (string) --The device's operating system type.
            cpu (dict) --Information about the device's CPU.
            frequency (string) --The CPU's frequency.
            architecture (string) --The CPU's architecture, for example x86 or ARM.
            clock (float) --The clock speed of the device's CPU, expressed in hertz (Hz). For example, a 1.2 GHz CPU is expressed as 1200000000.
            resolution (dict) --Represents the screen resolution of a device in height and width, expressed in pixels.
            width (integer) --The screen resolution's width, expressed in pixels.
            height (integer) --The screen resolution's height, expressed in pixels.
            heapSize (integer) --The device's heap size, expressed in bytes.
            memory (integer) --The device's total memory size, expressed in bytes.
            image (string) --The device's image name.
            carrier (string) --The device's carrier.
            radio (string) --The device's radio.
            remoteAccessEnabled (boolean) --Specifies whether remote access has been enabled for the specified device.
            fleetType (string) --The type of fleet to which this device belongs. Possible values for fleet type are PRIVATE and PUBLIC.
            fleetName (string) --The name of the fleet to which this device belongs.
            billingMethod (string) --The billing method of the remote access session. Possible values include METERED or UNMETERED . For more information about metered devices, see AWS Device Farm terminology .'
            deviceMinutes (dict) --Represents the total (metered or unmetered) minutes used by the resource to run tests. Contains the sum of minutes consumed by all children.
            total (float) --When specified, represents the total minutes used by the resource to run tests.
            metered (float) --When specified, represents only the sum of metered minutes used by the resource to run tests.
            unmetered (float) --When specified, represents only the sum of unmetered minutes used by the resource to run tests.
            endpoint (string) --The endpoint for the remote access sesssion.
            
            
            
        :type arn: string
        """
        self.client.get_remote_access_session(arn=arn)

    def get_run(self, arn=None):
        """
        :param arn: [REQUIRED]
            The run's ARN.
            Return typedict
            ReturnsResponse Syntax{
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
                }
              }
            }
            Response Structure
            (dict) --Represents the result of a get run request.
            run (dict) --Represents an app on a set of devices with a specific test and configuration.
            arn (string) --The run's ARN.
            name (string) --The run's name.
            type (string) --The run's type.
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
            platform (string) --The run's platform.
            Allowed values include:
            ANDROID: The Android platform.
            IOS: The iOS platform.
            created (datetime) --When the run was created.
            status (string) --The run's status.
            Allowed values include:
            PENDING: A pending status.
            PENDING_CONCURRENCY: A pending concurrency status.
            PENDING_DEVICE: A pending device status.
            PROCESSING: A processing status.
            SCHEDULING: A scheduling status.
            PREPARING: A preparing status.
            RUNNING: A running status.
            COMPLETED: A completed status.
            STOPPING: A stopping status.
            result (string) --The run's result.
            Allowed values include:
            PENDING: A pending condition.
            PASSED: A passing condition.
            WARNED: A warning condition.
            FAILED: A failed condition.
            SKIPPED: A skipped condition.
            ERRORED: An error condition.
            STOPPED: A stopped condition.
            started (datetime) --The run's start time.
            stopped (datetime) --The run's stop time.
            counters (dict) --The run's result counters.
            total (integer) --The total number of entities.
            passed (integer) --The number of passed entities.
            failed (integer) --The number of failed entities.
            warned (integer) --The number of warned entities.
            errored (integer) --The number of errored entities.
            stopped (integer) --The number of stopped entities.
            skipped (integer) --The number of skipped entities.
            message (string) --A message about the run's result.
            totalJobs (integer) --The total number of jobs for the run.
            completedJobs (integer) --The total number of completed jobs.
            billingMethod (string) --Specifies the billing method for a test run: metered or unmetered . If the parameter is not specified, the default value is unmetered .
            deviceMinutes (dict) --Represents the total (metered or unmetered) minutes used by the test run.
            total (float) --When specified, represents the total minutes used by the resource to run tests.
            metered (float) --When specified, represents only the sum of metered minutes used by the resource to run tests.
            unmetered (float) --When specified, represents only the sum of unmetered minutes used by the resource to run tests.
            
            
            
        :type arn: string
        """
        self.client.get_run(arn=arn)

    def get_suite(self, arn=None):
        """
        :param arn: [REQUIRED]
            The suite's ARN.
            Return typedict
            ReturnsResponse Syntax{
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
            Response Structure
            (dict) --Represents the result of a get suite request.
            suite (dict) --Represents a collection of one or more tests.
            arn (string) --The suite's ARN.
            name (string) --The suite's name.
            type (string) --The suite's type.
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
            created (datetime) --When the suite was created.
            status (string) --The suite's status.
            Allowed values include:
            PENDING: A pending status.
            PENDING_CONCURRENCY: A pending concurrency status.
            PENDING_DEVICE: A pending device status.
            PROCESSING: A processing status.
            SCHEDULING: A scheduling status.
            PREPARING: A preparing status.
            RUNNING: A running status.
            COMPLETED: A completed status.
            STOPPING: A stopping status.
            result (string) --The suite's result.
            Allowed values include:
            PENDING: A pending condition.
            PASSED: A passing condition.
            WARNED: A warning condition.
            FAILED: A failed condition.
            SKIPPED: A skipped condition.
            ERRORED: An error condition.
            STOPPED: A stopped condition.
            started (datetime) --The suite's start time.
            stopped (datetime) --The suite's stop time.
            counters (dict) --The suite's result counters.
            total (integer) --The total number of entities.
            passed (integer) --The number of passed entities.
            failed (integer) --The number of failed entities.
            warned (integer) --The number of warned entities.
            errored (integer) --The number of errored entities.
            stopped (integer) --The number of stopped entities.
            skipped (integer) --The number of skipped entities.
            message (string) --A message about the suite's result.
            deviceMinutes (dict) --Represents the total (metered or unmetered) minutes used by the test suite.
            total (float) --When specified, represents the total minutes used by the resource to run tests.
            metered (float) --When specified, represents only the sum of metered minutes used by the resource to run tests.
            unmetered (float) --When specified, represents only the sum of unmetered minutes used by the resource to run tests.
            
            
            
        :type arn: string
        """
        self.client.get_suite(arn=arn)

    def get_test(self, arn=None):
        """
        :param arn: [REQUIRED]
            The test's ARN.
            Return typedict
            ReturnsResponse Syntax{
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
            Response Structure
            (dict) --Represents the result of a get test request.
            test (dict) --Represents a condition that is evaluated.
            arn (string) --The test's ARN.
            name (string) --The test's name.
            type (string) --The test's type.
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
            created (datetime) --When the test was created.
            status (string) --The test's status.
            Allowed values include:
            PENDING: A pending status.
            PENDING_CONCURRENCY: A pending concurrency status.
            PENDING_DEVICE: A pending device status.
            PROCESSING: A processing status.
            SCHEDULING: A scheduling status.
            PREPARING: A preparing status.
            RUNNING: A running status.
            COMPLETED: A completed status.
            STOPPING: A stopping status.
            result (string) --The test's result.
            Allowed values include:
            PENDING: A pending condition.
            PASSED: A passing condition.
            WARNED: A warning condition.
            FAILED: A failed condition.
            SKIPPED: A skipped condition.
            ERRORED: An error condition.
            STOPPED: A stopped condition.
            started (datetime) --The test's start time.
            stopped (datetime) --The test's stop time.
            counters (dict) --The test's result counters.
            total (integer) --The total number of entities.
            passed (integer) --The number of passed entities.
            failed (integer) --The number of failed entities.
            warned (integer) --The number of warned entities.
            errored (integer) --The number of errored entities.
            stopped (integer) --The number of stopped entities.
            skipped (integer) --The number of skipped entities.
            message (string) --A message about the test's result.
            deviceMinutes (dict) --Represents the total (metered or unmetered) minutes used by the test.
            total (float) --When specified, represents the total minutes used by the resource to run tests.
            metered (float) --When specified, represents only the sum of metered minutes used by the resource to run tests.
            unmetered (float) --When specified, represents only the sum of unmetered minutes used by the resource to run tests.
            
            
            
        :type arn: string
        """
        self.client.get_test(arn=arn)

    def get_upload(self, arn=None):
        """
        :param arn: [REQUIRED]
            The upload's ARN.
            Return typedict
            ReturnsResponse Syntax{
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
            Response Structure
            (dict) --Represents the result of a get upload request.
            upload (dict) --An app or a set of one or more tests to upload or that have been uploaded.
            arn (string) --The upload's ARN.
            name (string) --The upload's file name.
            created (datetime) --When the upload was created.
            type (string) --The upload's type.
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
            status (string) --The upload's status.
            Must be one of the following values:
            FAILED: A failed status.
            INITIALIZED: An initialized status.
            PROCESSING: A processing status.
            SUCCEEDED: A succeeded status.
            url (string) --The pre-signed Amazon S3 URL that was used to store a file through a corresponding PUT request.
            metadata (string) --The upload's metadata. For example, for Android, this contains information that is parsed from the manifest and is displayed in the AWS Device Farm console after the associated app is uploaded.
            contentType (string) --The upload's content type (for example, 'application/octet-stream').
            message (string) --A message about the upload's result.
            
            
            
        :type arn: string
        """
        self.client.get_upload(arn=arn)

    def get_waiter(self):
        """
        """
        self.client.get_waiter()

    def install_to_remote_access_session(self, remoteAccessSessionArn=None, appArn=None):
        """
        :param remoteAccessSessionArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the remote access session about which you are requesting information.
            
        :type remoteAccessSessionArn: string
        :param appArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the app about which you are requesting information.
            
        :type appArn: string
        """
        self.client.install_to_remote_access_session(remoteAccessSessionArn=remoteAccessSessionArn, appArn=appArn)

    def list_artifacts(self, arn=None, type=None, nextToken=None):
        """
        :param arn: [REQUIRED]
            The Run, Job, Suite, or Test ARN.
            
        :type arn: string
        :param type: [REQUIRED]
            The artifacts' type.
            Allowed values include:
            FILE: The artifacts are files.
            LOG: The artifacts are logs.
            SCREENSHOT: The artifacts are screenshots.
            
        :type type: string
        :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
        :type nextToken: string
        """
        self.client.list_artifacts(arn=arn, type=type, nextToken=nextToken)

    def list_device_pools(self, arn=None, type=None, nextToken=None):
        """
        :param arn: [REQUIRED]
            The project ARN.
            
        :type arn: string
        :param type: The device pools' type.
            Allowed values include:
            CURATED: A device pool that is created and managed by AWS Device Farm.
            PRIVATE: A device pool that is created and managed by the device pool developer.
            
        :type type: string
        :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
        :type nextToken: string
        """
        self.client.list_device_pools(arn=arn, type=type, nextToken=nextToken)

    def list_devices(self, arn=None, nextToken=None):
        """
        :param arn: The device types' ARNs.
        :type arn: string
        :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
        :type nextToken: string
        """
        self.client.list_devices(arn=arn, nextToken=nextToken)

    def list_jobs(self, arn=None, nextToken=None):
        """
        :param arn: [REQUIRED]
            The jobs' ARNs.
            
        :type arn: string
        :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
        :type nextToken: string
        """
        self.client.list_jobs(arn=arn, nextToken=nextToken)

    def list_offering_transactions(self, nextToken=None):
        """
        :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
            Return typedict
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
            description (string) --A string describing the offering.
            type (string) --The type of offering (e.g., 'RECURRING') for a device.
            platform (string) --The platform of the device (e.g., ANDROID or IOS).
            recurringCharges (list) --Specifies whether there are recurring charges for the offering.
            (dict) --Specifies whether charges for devices will be recurring.
            cost (dict) --The cost of the recurring charge.
            amount (float) --The numerical amount of an offering or transaction.
            currencyCode (string) --The currency code of a monetary amount. For example, USD means 'U.S. dollars.'
            frequency (string) --The frequency in which charges will recur.
            
            quantity (integer) --The number of available devices in the offering.
            effectiveOn (datetime) --The date on which the offering is effective.
            transactionId (string) --The transaction ID of the offering transaction.
            createdOn (datetime) --The date on which an offering transaction was created.
            cost (dict) --The cost of an offering transaction.
            amount (float) --The numerical amount of an offering or transaction.
            currencyCode (string) --The currency code of a monetary amount. For example, USD means 'U.S. dollars.'
            
            nextToken (string) --An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
            
            
        :type nextToken: string
        """
        self.client.list_offering_transactions(nextToken=nextToken)

    def list_offerings(self, nextToken=None):
        """
        :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
            Return typedict
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
            offerings (list) --A value representing the list offering results.
            (dict) --Represents the metadata of a device offering.
            id (string) --The ID that corresponds to a device offering.
            description (string) --A string describing the offering.
            type (string) --The type of offering (e.g., 'RECURRING') for a device.
            platform (string) --The platform of the device (e.g., ANDROID or IOS).
            recurringCharges (list) --Specifies whether there are recurring charges for the offering.
            (dict) --Specifies whether charges for devices will be recurring.
            cost (dict) --The cost of the recurring charge.
            amount (float) --The numerical amount of an offering or transaction.
            currencyCode (string) --The currency code of a monetary amount. For example, USD means 'U.S. dollars.'
            frequency (string) --The frequency in which charges will recur.
            
            
            nextToken (string) --An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
            
            
        :type nextToken: string
        """
        self.client.list_offerings(nextToken=nextToken)

    def list_projects(self, arn=None, nextToken=None):
        """
        :param arn: The projects' ARNs.
        :type arn: string
        :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
        :type nextToken: string
        """
        self.client.list_projects(arn=arn, nextToken=nextToken)

    def list_remote_access_sessions(self, arn=None, nextToken=None):
        """
        :param arn: [REQUIRED]
            The Amazon Resource Name (ARN) of the remote access session about which you are requesting information.
            
        :type arn: string
        :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
        :type nextToken: string
        """
        self.client.list_remote_access_sessions(arn=arn, nextToken=nextToken)

    def list_runs(self, arn=None, nextToken=None):
        """
        :param arn: [REQUIRED]
            The runs' ARNs.
            
        :type arn: string
        :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
        :type nextToken: string
        """
        self.client.list_runs(arn=arn, nextToken=nextToken)

    def list_samples(self, arn=None, nextToken=None):
        """
        :param arn: [REQUIRED]
            The samples' ARNs.
            
        :type arn: string
        :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
        :type nextToken: string
        """
        self.client.list_samples(arn=arn, nextToken=nextToken)

    def list_suites(self, arn=None, nextToken=None):
        """
        :param arn: [REQUIRED]
            The suites' ARNs.
            
        :type arn: string
        :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
        :type nextToken: string
        """
        self.client.list_suites(arn=arn, nextToken=nextToken)

    def list_tests(self, arn=None, nextToken=None):
        """
        :param arn: [REQUIRED]
            The tests' ARNs.
            
        :type arn: string
        :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
        :type nextToken: string
        """
        self.client.list_tests(arn=arn, nextToken=nextToken)

    def list_unique_problems(self, arn=None, nextToken=None):
        """
        :param arn: [REQUIRED]
            The unique problems' ARNs.
            
        :type arn: string
        :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
        :type nextToken: string
        """
        self.client.list_unique_problems(arn=arn, nextToken=nextToken)

    def list_uploads(self, arn=None, nextToken=None):
        """
        :param arn: [REQUIRED]
            The uploads' ARNs.
            
        :type arn: string
        :param nextToken: An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
        :type nextToken: string
        """
        self.client.list_uploads(arn=arn, nextToken=nextToken)

    def purchase_offering(self, offeringId=None, quantity=None):
        """
        :param offeringId: The ID of the offering.
        :type offeringId: string
        :param quantity: The number of device slots you wish to purchase in an offering request.
        :type quantity: integer
        """
        self.client.purchase_offering(offeringId=offeringId, quantity=quantity)

    def renew_offering(self, offeringId=None, quantity=None):
        """
        :param offeringId: The ID of a request to renew an offering.
        :type offeringId: string
        :param quantity: The quantity requested in an offering renewal.
        :type quantity: integer
        """
        self.client.renew_offering(offeringId=offeringId, quantity=quantity)

    def schedule_run(self, projectArn=None, appArn=None, devicePoolArn=None, name=None, test=None, configuration=None):
        """
        :param projectArn: [REQUIRED]
            The ARN of the project for the run to be scheduled.
            
        :type projectArn: string
        :param appArn: The ARN of the app to schedule a run.
        :type appArn: string
        :param devicePoolArn: [REQUIRED]
            The ARN of the device pool for the run to be scheduled.
            
        :type devicePoolArn: string
        :param name: The name for the run to be scheduled.
        :type name: string
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
            parameters (dict) --The test's parameters, such as test framework parameters and fixture settings.
            (string) --
            (string) --
            
            
        :type test: dict
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
            billingMethod (string) --Specifies the billing method for a test run: metered or unmetered . If the parameter is not specified, the default value is unmetered .
            
        :type configuration: dict
        """
        self.client.schedule_run(projectArn=projectArn, appArn=appArn, devicePoolArn=devicePoolArn, name=name,
                                 test=test, configuration=configuration)

    def stop_remote_access_session(self, arn=None):
        """
        :param arn: [REQUIRED]
            The Amazon Resource Name (ARN) of the remote access session you wish to stop.
            Return typedict
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
            Response Structure
            (dict) --Represents the response from the server that describes the remote access session when AWS Device Farm stops the session.
            remoteAccessSession (dict) --A container representing the metadata from the service about the remote access session you are stopping.
            arn (string) --The Amazon Resource Name (ARN) of the remote access session.
            name (string) --The name of the remote access session.
            created (datetime) --The date and time the remote access session was created.
            status (string) --The status of the remote access session. Can be any of the following:
            PENDING: A pending status.
            PENDING_CONCURRENCY: A pending concurrency status.
            PENDING_DEVICE: A pending device status.
            PROCESSING: A processing status.
            SCHEDULING: A scheduling status.
            PREPARING: A preparing status.
            RUNNING: A running status.
            COMPLETED: A completed status.
            STOPPING: A stopping status.
            result (string) --The result of the remote access session. Can be any of the following:
            PENDING: A pending condition.
            PASSED: A passing condition.
            WARNED: A warning condition.
            FAILED: A failed condition.
            SKIPPED: A skipped condition.
            ERRORED: An error condition.
            STOPPED: A stopped condition.
            message (string) --A message about the remote access session.
            started (datetime) --The date and time the remote access session was started.
            stopped (datetime) --The date and time the remote access session was stopped.
            device (dict) --Represents a device type that an app is tested against.
            arn (string) --The device's ARN.
            name (string) --The device's display name.
            manufacturer (string) --The device's manufacturer name.
            model (string) --The device's model name.
            formFactor (string) --The device's form factor.
            Allowed values include:
            PHONE: The phone form factor.
            TABLET: The tablet form factor.
            platform (string) --The device's platform.
            Allowed values include:
            ANDROID: The Android platform.
            IOS: The iOS platform.
            os (string) --The device's operating system type.
            cpu (dict) --Information about the device's CPU.
            frequency (string) --The CPU's frequency.
            architecture (string) --The CPU's architecture, for example x86 or ARM.
            clock (float) --The clock speed of the device's CPU, expressed in hertz (Hz). For example, a 1.2 GHz CPU is expressed as 1200000000.
            resolution (dict) --Represents the screen resolution of a device in height and width, expressed in pixels.
            width (integer) --The screen resolution's width, expressed in pixels.
            height (integer) --The screen resolution's height, expressed in pixels.
            heapSize (integer) --The device's heap size, expressed in bytes.
            memory (integer) --The device's total memory size, expressed in bytes.
            image (string) --The device's image name.
            carrier (string) --The device's carrier.
            radio (string) --The device's radio.
            remoteAccessEnabled (boolean) --Specifies whether remote access has been enabled for the specified device.
            fleetType (string) --The type of fleet to which this device belongs. Possible values for fleet type are PRIVATE and PUBLIC.
            fleetName (string) --The name of the fleet to which this device belongs.
            billingMethod (string) --The billing method of the remote access session. Possible values include METERED or UNMETERED . For more information about metered devices, see AWS Device Farm terminology .'
            deviceMinutes (dict) --Represents the total (metered or unmetered) minutes used by the resource to run tests. Contains the sum of minutes consumed by all children.
            total (float) --When specified, represents the total minutes used by the resource to run tests.
            metered (float) --When specified, represents only the sum of metered minutes used by the resource to run tests.
            unmetered (float) --When specified, represents only the sum of unmetered minutes used by the resource to run tests.
            endpoint (string) --The endpoint for the remote access sesssion.
            
            
            
        :type arn: string
        """
        self.client.stop_remote_access_session(arn=arn)

    def stop_run(self, arn=None):
        """
        :param arn: [REQUIRED]
            Represents the Amazon Resource Name (ARN) of the Device Farm run you wish to stop.
            Return typedict
            ReturnsResponse Syntax{
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
                }
              }
            }
            Response Structure
            (dict) --Represents the results of your stop run attempt.
            run (dict) --Represents an app on a set of devices with a specific test and configuration.
            arn (string) --The run's ARN.
            name (string) --The run's name.
            type (string) --The run's type.
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
            platform (string) --The run's platform.
            Allowed values include:
            ANDROID: The Android platform.
            IOS: The iOS platform.
            created (datetime) --When the run was created.
            status (string) --The run's status.
            Allowed values include:
            PENDING: A pending status.
            PENDING_CONCURRENCY: A pending concurrency status.
            PENDING_DEVICE: A pending device status.
            PROCESSING: A processing status.
            SCHEDULING: A scheduling status.
            PREPARING: A preparing status.
            RUNNING: A running status.
            COMPLETED: A completed status.
            STOPPING: A stopping status.
            result (string) --The run's result.
            Allowed values include:
            PENDING: A pending condition.
            PASSED: A passing condition.
            WARNED: A warning condition.
            FAILED: A failed condition.
            SKIPPED: A skipped condition.
            ERRORED: An error condition.
            STOPPED: A stopped condition.
            started (datetime) --The run's start time.
            stopped (datetime) --The run's stop time.
            counters (dict) --The run's result counters.
            total (integer) --The total number of entities.
            passed (integer) --The number of passed entities.
            failed (integer) --The number of failed entities.
            warned (integer) --The number of warned entities.
            errored (integer) --The number of errored entities.
            stopped (integer) --The number of stopped entities.
            skipped (integer) --The number of skipped entities.
            message (string) --A message about the run's result.
            totalJobs (integer) --The total number of jobs for the run.
            completedJobs (integer) --The total number of completed jobs.
            billingMethod (string) --Specifies the billing method for a test run: metered or unmetered . If the parameter is not specified, the default value is unmetered .
            deviceMinutes (dict) --Represents the total (metered or unmetered) minutes used by the test run.
            total (float) --When specified, represents the total minutes used by the resource to run tests.
            metered (float) --When specified, represents only the sum of metered minutes used by the resource to run tests.
            unmetered (float) --When specified, represents only the sum of unmetered minutes used by the resource to run tests.
            
            
            
        :type arn: string
        """
        self.client.stop_run(arn=arn)

    def update_device_pool(self, arn=None, name=None, description=None, rules=None):
        """
        :param arn: [REQUIRED]
            The Amazon Resourc Name (ARN) of the Device Farm device pool you wish to update.
            
        :type arn: string
        :param name: A string representing the name of the device pool you wish to update.
        :type name: string
        :param description: A description of the device pool you wish to update.
        :type description: string
        :param rules: Represents the rules you wish to modify for the device pool. Updating rules is optional; however, if you choose to update rules for your request, the update will replace the existing rules.
            (dict) --Represents a condition for a device pool.
            attribute (string) --The rule's stringified attribute. For example, specify the value as '\'abc\'' .
            Allowed values include:
            ARN: The ARN.
            FORM_FACTOR: The form factor (for example, phone or tablet).
            MANUFACTURER: The manufacturer.
            PLATFORM: The platform (for example, Android or iOS).
            operator (string) --The rule's operator.
            EQUALS: The equals operator.
            GREATER_THAN: The greater-than operator.
            IN: The in operator.
            LESS_THAN: The less-than operator.
            NOT_IN: The not-in operator.
            value (string) --The rule's value.
            
            
        :type rules: list
        """
        self.client.update_device_pool(arn=arn, name=name, description=description, rules=rules)

    def update_project(self, arn=None, name=None):
        """
        :param arn: [REQUIRED]
            The Amazon Resource Name (ARN) of the project whose name you wish to update.
            
        :type arn: string
        :param name: A string representing the new name of the project that you are updating.
        :type name: string
        """
        self.client.update_project(arn=arn, name=name)
