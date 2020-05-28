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

def add_tags_to_resource(ResourceArn=None, TagList=None):
    """
    This is documentation for AWS CloudHSM Classic . For more information, see AWS CloudHSM Classic FAQs , the AWS CloudHSM Classic User Guide , and the AWS CloudHSM Classic API Reference .
    Adds or overwrites one or more tags for the specified AWS CloudHSM resource.
    Each tag consists of a key and a value. Tag keys must be unique to each resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.add_tags_to_resource(
        ResourceArn='string',
        TagList=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the AWS CloudHSM resource to tag.\n

    :type TagList: list
    :param TagList: [REQUIRED]\nOne or more tags.\n\n(dict) --A key-value pair that identifies or specifies metadata about an AWS CloudHSM resource.\n\nKey (string) -- [REQUIRED]The key of the tag.\n\nValue (string) -- [REQUIRED]The value of the tag.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Status': 'string'
}


Response Structure

(dict) --

Status (string) --
The status of the operation.







Exceptions

CloudHSM.Client.exceptions.CloudHsmServiceException
CloudHSM.Client.exceptions.CloudHsmInternalException
CloudHSM.Client.exceptions.InvalidRequestException


    :return: {
        'Status': 'string'
    }
    
    
    :returns: 
    CloudHSM.Client.exceptions.CloudHsmServiceException
    CloudHSM.Client.exceptions.CloudHsmInternalException
    CloudHSM.Client.exceptions.InvalidRequestException
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def create_hapg(Label=None):
    """
    This is documentation for AWS CloudHSM Classic . For more information, see AWS CloudHSM Classic FAQs , the AWS CloudHSM Classic User Guide , and the AWS CloudHSM Classic API Reference .
    Creates a high-availability partition group. A high-availability partition group is a group of partitions that spans multiple physical HSMs.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_hapg(
        Label='string'
    )
    
    
    :type Label: string
    :param Label: [REQUIRED]\nThe label of the new high-availability partition group.\n

    :rtype: dict
ReturnsResponse Syntax{
    'HapgArn': 'string'
}


Response Structure

(dict) --Contains the output of the  CreateHAPartitionGroup action.

HapgArn (string) --The ARN of the high-availability partition group.






Exceptions

CloudHSM.Client.exceptions.CloudHsmServiceException
CloudHSM.Client.exceptions.CloudHsmInternalException
CloudHSM.Client.exceptions.InvalidRequestException


    :return: {
        'HapgArn': 'string'
    }
    
    
    """
    pass

def create_hsm(SubnetId=None, SshKey=None, EniIp=None, IamRoleArn=None, ExternalId=None, SubscriptionType=None, ClientToken=None, SyslogIp=None):
    """
    This is documentation for AWS CloudHSM Classic . For more information, see AWS CloudHSM Classic FAQs , the AWS CloudHSM Classic User Guide , and the AWS CloudHSM Classic API Reference .
    Creates an uninitialized HSM instance.
    There is an upfront fee charged for each HSM instance that you create with the CreateHsm operation. If you accidentally provision an HSM and want to request a refund, delete the instance using the  DeleteHsm operation, go to the AWS Support Center , create a new case, and select Account and Billing Support .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_hsm(
        SubnetId='string',
        SshKey='string',
        EniIp='string',
        IamRoleArn='string',
        ExternalId='string',
        SubscriptionType='PRODUCTION',
        ClientToken='string',
        SyslogIp='string'
    )
    
    
    :type SubnetId: string
    :param SubnetId: [REQUIRED]\nThe identifier of the subnet in your VPC in which to place the HSM.\n

    :type SshKey: string
    :param SshKey: [REQUIRED]\nThe SSH public key to install on the HSM.\n

    :type EniIp: string
    :param EniIp: The IP address to assign to the HSM\'s ENI.\nIf an IP address is not specified, an IP address will be randomly chosen from the CIDR range of the subnet.\n

    :type IamRoleArn: string
    :param IamRoleArn: [REQUIRED]\nThe ARN of an IAM role to enable the AWS CloudHSM service to allocate an ENI on your behalf.\n

    :type ExternalId: string
    :param ExternalId: The external ID from IamRoleArn , if present.

    :type SubscriptionType: string
    :param SubscriptionType: [REQUIRED]\nSpecifies the type of subscription for the HSM.\n\nPRODUCTION - The HSM is being used in a production environment.\nTRIAL - The HSM is being used in a product trial.\n\n

    :type ClientToken: string
    :param ClientToken: A user-defined token to ensure idempotence. Subsequent calls to this operation with the same token will be ignored.

    :type SyslogIp: string
    :param SyslogIp: The IP address for the syslog monitoring server. The AWS CloudHSM service only supports one syslog monitoring server.

    :rtype: dict

ReturnsResponse Syntax
{
    'HsmArn': 'string'
}


Response Structure

(dict) --
Contains the output of the CreateHsm operation.

HsmArn (string) --
The ARN of the HSM.







Exceptions

CloudHSM.Client.exceptions.CloudHsmServiceException
CloudHSM.Client.exceptions.CloudHsmInternalException
CloudHSM.Client.exceptions.InvalidRequestException


    :return: {
        'HsmArn': 'string'
    }
    
    
    :returns: 
    CloudHSM.Client.exceptions.CloudHsmServiceException
    CloudHSM.Client.exceptions.CloudHsmInternalException
    CloudHSM.Client.exceptions.InvalidRequestException
    
    """
    pass

def create_luna_client(Label=None, Certificate=None):
    """
    This is documentation for AWS CloudHSM Classic . For more information, see AWS CloudHSM Classic FAQs , the AWS CloudHSM Classic User Guide , and the AWS CloudHSM Classic API Reference .
    Creates an HSM client.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_luna_client(
        Label='string',
        Certificate='string'
    )
    
    
    :type Label: string
    :param Label: The label for the client.

    :type Certificate: string
    :param Certificate: [REQUIRED]\nThe contents of a Base64-Encoded X.509 v3 certificate to be installed on the HSMs used by this client.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ClientArn': 'string'
}


Response Structure

(dict) --
Contains the output of the  CreateLunaClient action.

ClientArn (string) --
The ARN of the client.







Exceptions

CloudHSM.Client.exceptions.CloudHsmServiceException
CloudHSM.Client.exceptions.CloudHsmInternalException
CloudHSM.Client.exceptions.InvalidRequestException


    :return: {
        'ClientArn': 'string'
    }
    
    
    :returns: 
    CloudHSM.Client.exceptions.CloudHsmServiceException
    CloudHSM.Client.exceptions.CloudHsmInternalException
    CloudHSM.Client.exceptions.InvalidRequestException
    
    """
    pass

def delete_hapg(HapgArn=None):
    """
    This is documentation for AWS CloudHSM Classic . For more information, see AWS CloudHSM Classic FAQs , the AWS CloudHSM Classic User Guide , and the AWS CloudHSM Classic API Reference .
    Deletes a high-availability partition group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_hapg(
        HapgArn='string'
    )
    
    
    :type HapgArn: string
    :param HapgArn: [REQUIRED]\nThe ARN of the high-availability partition group to delete.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Status': 'string'
}


Response Structure

(dict) --Contains the output of the  DeleteHapg action.

Status (string) --The status of the action.






Exceptions

CloudHSM.Client.exceptions.CloudHsmServiceException
CloudHSM.Client.exceptions.CloudHsmInternalException
CloudHSM.Client.exceptions.InvalidRequestException


    :return: {
        'Status': 'string'
    }
    
    
    """
    pass

def delete_hsm(HsmArn=None):
    """
    This is documentation for AWS CloudHSM Classic . For more information, see AWS CloudHSM Classic FAQs , the AWS CloudHSM Classic User Guide , and the AWS CloudHSM Classic API Reference .
    Deletes an HSM. After completion, this operation cannot be undone and your key material cannot be recovered.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_hsm(
        HsmArn='string'
    )
    
    
    :type HsmArn: string
    :param HsmArn: [REQUIRED]\nThe ARN of the HSM to delete.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Status': 'string'
}


Response Structure

(dict) --Contains the output of the  DeleteHsm operation.

Status (string) --The status of the operation.






Exceptions

CloudHSM.Client.exceptions.CloudHsmServiceException
CloudHSM.Client.exceptions.CloudHsmInternalException
CloudHSM.Client.exceptions.InvalidRequestException


    :return: {
        'Status': 'string'
    }
    
    
    """
    pass

def delete_luna_client(ClientArn=None):
    """
    This is documentation for AWS CloudHSM Classic . For more information, see AWS CloudHSM Classic FAQs , the AWS CloudHSM Classic User Guide , and the AWS CloudHSM Classic API Reference .
    Deletes a client.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_luna_client(
        ClientArn='string'
    )
    
    
    :type ClientArn: string
    :param ClientArn: [REQUIRED]\nThe ARN of the client to delete.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Status': 'string'
}


Response Structure

(dict) --
Status (string) --The status of the action.






Exceptions

CloudHSM.Client.exceptions.CloudHsmServiceException
CloudHSM.Client.exceptions.CloudHsmInternalException
CloudHSM.Client.exceptions.InvalidRequestException


    :return: {
        'Status': 'string'
    }
    
    
    """
    pass

def describe_hapg(HapgArn=None):
    """
    This is documentation for AWS CloudHSM Classic . For more information, see AWS CloudHSM Classic FAQs , the AWS CloudHSM Classic User Guide , and the AWS CloudHSM Classic API Reference .
    Retrieves information about a high-availability partition group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_hapg(
        HapgArn='string'
    )
    
    
    :type HapgArn: string
    :param HapgArn: [REQUIRED]\nThe ARN of the high-availability partition group to describe.\n

    :rtype: dict
ReturnsResponse Syntax{
    'HapgArn': 'string',
    'HapgSerial': 'string',
    'HsmsLastActionFailed': [
        'string',
    ],
    'HsmsPendingDeletion': [
        'string',
    ],
    'HsmsPendingRegistration': [
        'string',
    ],
    'Label': 'string',
    'LastModifiedTimestamp': 'string',
    'PartitionSerialList': [
        'string',
    ],
    'State': 'READY'|'UPDATING'|'DEGRADED'
}


Response Structure

(dict) --Contains the output of the  DescribeHapg action.

HapgArn (string) --The ARN of the high-availability partition group.

HapgSerial (string) --The serial number of the high-availability partition group.

HsmsLastActionFailed (list) --
(string) --An ARN that identifies an HSM.



HsmsPendingDeletion (list) --
(string) --An ARN that identifies an HSM.



HsmsPendingRegistration (list) --
(string) --An ARN that identifies an HSM.



Label (string) --The label for the high-availability partition group.

LastModifiedTimestamp (string) --The date and time the high-availability partition group was last modified.

PartitionSerialList (list) --The list of partition serial numbers that belong to the high-availability partition group.

(string) --


State (string) --The state of the high-availability partition group.






Exceptions

CloudHSM.Client.exceptions.CloudHsmServiceException
CloudHSM.Client.exceptions.CloudHsmInternalException
CloudHSM.Client.exceptions.InvalidRequestException


    :return: {
        'HapgArn': 'string',
        'HapgSerial': 'string',
        'HsmsLastActionFailed': [
            'string',
        ],
        'HsmsPendingDeletion': [
            'string',
        ],
        'HsmsPendingRegistration': [
            'string',
        ],
        'Label': 'string',
        'LastModifiedTimestamp': 'string',
        'PartitionSerialList': [
            'string',
        ],
        'State': 'READY'|'UPDATING'|'DEGRADED'
    }
    
    
    :returns: 
    CloudHSM.Client.exceptions.CloudHsmServiceException
    CloudHSM.Client.exceptions.CloudHsmInternalException
    CloudHSM.Client.exceptions.InvalidRequestException
    
    """
    pass

def describe_hsm(HsmArn=None, HsmSerialNumber=None):
    """
    This is documentation for AWS CloudHSM Classic . For more information, see AWS CloudHSM Classic FAQs , the AWS CloudHSM Classic User Guide , and the AWS CloudHSM Classic API Reference .
    Retrieves information about an HSM. You can identify the HSM by its ARN or its serial number.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_hsm(
        HsmArn='string',
        HsmSerialNumber='string'
    )
    
    
    :type HsmArn: string
    :param HsmArn: The ARN of the HSM. Either the HsmArn or the SerialNumber parameter must be specified.

    :type HsmSerialNumber: string
    :param HsmSerialNumber: The serial number of the HSM. Either the HsmArn or the HsmSerialNumber parameter must be specified.

    :rtype: dict

ReturnsResponse Syntax
{
    'HsmArn': 'string',
    'Status': 'PENDING'|'RUNNING'|'UPDATING'|'SUSPENDED'|'TERMINATING'|'TERMINATED'|'DEGRADED',
    'StatusDetails': 'string',
    'AvailabilityZone': 'string',
    'EniId': 'string',
    'EniIp': 'string',
    'SubscriptionType': 'PRODUCTION',
    'SubscriptionStartDate': 'string',
    'SubscriptionEndDate': 'string',
    'VpcId': 'string',
    'SubnetId': 'string',
    'IamRoleArn': 'string',
    'SerialNumber': 'string',
    'VendorName': 'string',
    'HsmType': 'string',
    'SoftwareVersion': 'string',
    'SshPublicKey': 'string',
    'SshKeyLastUpdated': 'string',
    'ServerCertUri': 'string',
    'ServerCertLastUpdated': 'string',
    'Partitions': [
        'string',
    ]
}


Response Structure

(dict) --
Contains the output of the  DescribeHsm operation.

HsmArn (string) --
The ARN of the HSM.

Status (string) --
The status of the HSM.

StatusDetails (string) --
Contains additional information about the status of the HSM.

AvailabilityZone (string) --
The Availability Zone that the HSM is in.

EniId (string) --
The identifier of the elastic network interface (ENI) attached to the HSM.

EniIp (string) --
The IP address assigned to the HSM\'s ENI.

SubscriptionType (string) --
Specifies the type of subscription for the HSM.

PRODUCTION - The HSM is being used in a production environment.
TRIAL - The HSM is being used in a product trial.


SubscriptionStartDate (string) --
The subscription start date.

SubscriptionEndDate (string) --
The subscription end date.

VpcId (string) --
The identifier of the VPC that the HSM is in.

SubnetId (string) --
The identifier of the subnet that the HSM is in.

IamRoleArn (string) --
The ARN of the IAM role assigned to the HSM.

SerialNumber (string) --
The serial number of the HSM.

VendorName (string) --
The name of the HSM vendor.

HsmType (string) --
The HSM model type.

SoftwareVersion (string) --
The HSM software version.

SshPublicKey (string) --
The public SSH key.

SshKeyLastUpdated (string) --
The date and time that the SSH key was last updated.

ServerCertUri (string) --
The URI of the certificate server.

ServerCertLastUpdated (string) --
The date and time that the server certificate was last updated.

Partitions (list) --
The list of partitions on the HSM.

(string) --








Exceptions

CloudHSM.Client.exceptions.CloudHsmServiceException
CloudHSM.Client.exceptions.CloudHsmInternalException
CloudHSM.Client.exceptions.InvalidRequestException


    :return: {
        'HsmArn': 'string',
        'Status': 'PENDING'|'RUNNING'|'UPDATING'|'SUSPENDED'|'TERMINATING'|'TERMINATED'|'DEGRADED',
        'StatusDetails': 'string',
        'AvailabilityZone': 'string',
        'EniId': 'string',
        'EniIp': 'string',
        'SubscriptionType': 'PRODUCTION',
        'SubscriptionStartDate': 'string',
        'SubscriptionEndDate': 'string',
        'VpcId': 'string',
        'SubnetId': 'string',
        'IamRoleArn': 'string',
        'SerialNumber': 'string',
        'VendorName': 'string',
        'HsmType': 'string',
        'SoftwareVersion': 'string',
        'SshPublicKey': 'string',
        'SshKeyLastUpdated': 'string',
        'ServerCertUri': 'string',
        'ServerCertLastUpdated': 'string',
        'Partitions': [
            'string',
        ]
    }
    
    
    :returns: 
    PRODUCTION - The HSM is being used in a production environment.
    TRIAL - The HSM is being used in a product trial.
    
    """
    pass

def describe_luna_client(ClientArn=None, CertificateFingerprint=None):
    """
    This is documentation for AWS CloudHSM Classic . For more information, see AWS CloudHSM Classic FAQs , the AWS CloudHSM Classic User Guide , and the AWS CloudHSM Classic API Reference .
    Retrieves information about an HSM client.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_luna_client(
        ClientArn='string',
        CertificateFingerprint='string'
    )
    
    
    :type ClientArn: string
    :param ClientArn: The ARN of the client.

    :type CertificateFingerprint: string
    :param CertificateFingerprint: The certificate fingerprint.

    :rtype: dict

ReturnsResponse Syntax
{
    'ClientArn': 'string',
    'Certificate': 'string',
    'CertificateFingerprint': 'string',
    'LastModifiedTimestamp': 'string',
    'Label': 'string'
}


Response Structure

(dict) --

ClientArn (string) --
The ARN of the client.

Certificate (string) --
The certificate installed on the HSMs used by this client.

CertificateFingerprint (string) --
The certificate fingerprint.

LastModifiedTimestamp (string) --
The date and time the client was last modified.

Label (string) --
The label of the client.







Exceptions

CloudHSM.Client.exceptions.CloudHsmServiceException
CloudHSM.Client.exceptions.CloudHsmInternalException
CloudHSM.Client.exceptions.InvalidRequestException


    :return: {
        'ClientArn': 'string',
        'Certificate': 'string',
        'CertificateFingerprint': 'string',
        'LastModifiedTimestamp': 'string',
        'Label': 'string'
    }
    
    
    :returns: 
    CloudHSM.Client.exceptions.CloudHsmServiceException
    CloudHSM.Client.exceptions.CloudHsmInternalException
    CloudHSM.Client.exceptions.InvalidRequestException
    
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

def get_config(ClientArn=None, ClientVersion=None, HapgList=None):
    """
    This is documentation for AWS CloudHSM Classic . For more information, see AWS CloudHSM Classic FAQs , the AWS CloudHSM Classic User Guide , and the AWS CloudHSM Classic API Reference .
    Gets the configuration files necessary to connect to all high availability partition groups the client is associated with.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_config(
        ClientArn='string',
        ClientVersion='5.1'|'5.3',
        HapgList=[
            'string',
        ]
    )
    
    
    :type ClientArn: string
    :param ClientArn: [REQUIRED]\nThe ARN of the client.\n

    :type ClientVersion: string
    :param ClientVersion: [REQUIRED]\nThe client version.\n

    :type HapgList: list
    :param HapgList: [REQUIRED]\nA list of ARNs that identify the high-availability partition groups that are associated with the client.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ConfigType': 'string',
    'ConfigFile': 'string',
    'ConfigCred': 'string'
}


Response Structure

(dict) --

ConfigType (string) --
The type of credentials.

ConfigFile (string) --
The chrystoki.conf configuration file.

ConfigCred (string) --
The certificate file containing the server.pem files of the HSMs.







Exceptions

CloudHSM.Client.exceptions.CloudHsmServiceException
CloudHSM.Client.exceptions.CloudHsmInternalException
CloudHSM.Client.exceptions.InvalidRequestException


    :return: {
        'ConfigType': 'string',
        'ConfigFile': 'string',
        'ConfigCred': 'string'
    }
    
    
    :returns: 
    CloudHSM.Client.exceptions.CloudHsmServiceException
    CloudHSM.Client.exceptions.CloudHsmInternalException
    CloudHSM.Client.exceptions.InvalidRequestException
    
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

def list_available_zones():
    """
    This is documentation for AWS CloudHSM Classic . For more information, see AWS CloudHSM Classic FAQs , the AWS CloudHSM Classic User Guide , and the AWS CloudHSM Classic API Reference .
    Lists the Availability Zones that have available AWS CloudHSM capacity.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_available_zones()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'AZList': [
        'string',
    ]
}


Response Structure

(dict) --
AZList (list) --The list of Availability Zones that have available AWS CloudHSM capacity.

(string) --







Exceptions

CloudHSM.Client.exceptions.CloudHsmServiceException
CloudHSM.Client.exceptions.CloudHsmInternalException
CloudHSM.Client.exceptions.InvalidRequestException


    :return: {
        'AZList': [
            'string',
        ]
    }
    
    
    :returns: 
    CloudHSM.Client.exceptions.CloudHsmServiceException
    CloudHSM.Client.exceptions.CloudHsmInternalException
    CloudHSM.Client.exceptions.InvalidRequestException
    
    """
    pass

def list_hapgs(NextToken=None):
    """
    This is documentation for AWS CloudHSM Classic . For more information, see AWS CloudHSM Classic FAQs , the AWS CloudHSM Classic User Guide , and the AWS CloudHSM Classic API Reference .
    Lists the high-availability partition groups for the account.
    This operation supports pagination with the use of the NextToken member. If more results are available, the NextToken member of the response contains a token that you pass in the next call to ListHapgs to retrieve the next set of items.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_hapgs(
        NextToken='string'
    )
    
    
    :type NextToken: string
    :param NextToken: The NextToken value from a previous call to ListHapgs . Pass null if this is the first call.

    :rtype: dict
ReturnsResponse Syntax{
    'HapgList': [
        'string',
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
HapgList (list) --The list of high-availability partition groups.

(string) --


NextToken (string) --If not null, more results are available. Pass this value to ListHapgs to retrieve the next set of items.






Exceptions

CloudHSM.Client.exceptions.CloudHsmServiceException
CloudHSM.Client.exceptions.CloudHsmInternalException
CloudHSM.Client.exceptions.InvalidRequestException


    :return: {
        'HapgList': [
            'string',
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    CloudHSM.Client.exceptions.CloudHsmServiceException
    CloudHSM.Client.exceptions.CloudHsmInternalException
    CloudHSM.Client.exceptions.InvalidRequestException
    
    """
    pass

def list_hsms(NextToken=None):
    """
    This is documentation for AWS CloudHSM Classic . For more information, see AWS CloudHSM Classic FAQs , the AWS CloudHSM Classic User Guide , and the AWS CloudHSM Classic API Reference .
    Retrieves the identifiers of all of the HSMs provisioned for the current customer.
    This operation supports pagination with the use of the NextToken member. If more results are available, the NextToken member of the response contains a token that you pass in the next call to ListHsms to retrieve the next set of items.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_hsms(
        NextToken='string'
    )
    
    
    :type NextToken: string
    :param NextToken: The NextToken value from a previous call to ListHsms . Pass null if this is the first call.

    :rtype: dict
ReturnsResponse Syntax{
    'HsmList': [
        'string',
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --Contains the output of the ListHsms operation.

HsmList (list) --The list of ARNs that identify the HSMs.

(string) --An ARN that identifies an HSM.



NextToken (string) --If not null, more results are available. Pass this value to ListHsms to retrieve the next set of items.






Exceptions

CloudHSM.Client.exceptions.CloudHsmServiceException
CloudHSM.Client.exceptions.CloudHsmInternalException
CloudHSM.Client.exceptions.InvalidRequestException


    :return: {
        'HsmList': [
            'string',
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_luna_clients(NextToken=None):
    """
    This is documentation for AWS CloudHSM Classic . For more information, see AWS CloudHSM Classic FAQs , the AWS CloudHSM Classic User Guide , and the AWS CloudHSM Classic API Reference .
    Lists all of the clients.
    This operation supports pagination with the use of the NextToken member. If more results are available, the NextToken member of the response contains a token that you pass in the next call to ListLunaClients to retrieve the next set of items.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_luna_clients(
        NextToken='string'
    )
    
    
    :type NextToken: string
    :param NextToken: The NextToken value from a previous call to ListLunaClients . Pass null if this is the first call.

    :rtype: dict
ReturnsResponse Syntax{
    'ClientList': [
        'string',
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
ClientList (list) --The list of clients.

(string) --


NextToken (string) --If not null, more results are available. Pass this to ListLunaClients to retrieve the next set of items.






Exceptions

CloudHSM.Client.exceptions.CloudHsmServiceException
CloudHSM.Client.exceptions.CloudHsmInternalException
CloudHSM.Client.exceptions.InvalidRequestException


    :return: {
        'ClientList': [
            'string',
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    CloudHSM.Client.exceptions.CloudHsmServiceException
    CloudHSM.Client.exceptions.CloudHsmInternalException
    CloudHSM.Client.exceptions.InvalidRequestException
    
    """
    pass

def list_tags_for_resource(ResourceArn=None):
    """
    This is documentation for AWS CloudHSM Classic . For more information, see AWS CloudHSM Classic FAQs , the AWS CloudHSM Classic User Guide , and the AWS CloudHSM Classic API Reference .
    Returns a list of all tags for the specified AWS CloudHSM resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        ResourceArn='string'
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the AWS CloudHSM resource.\n

    :rtype: dict
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
TagList (list) --One or more tags.

(dict) --A key-value pair that identifies or specifies metadata about an AWS CloudHSM resource.

Key (string) --The key of the tag.

Value (string) --The value of the tag.










Exceptions

CloudHSM.Client.exceptions.CloudHsmServiceException
CloudHSM.Client.exceptions.CloudHsmInternalException
CloudHSM.Client.exceptions.InvalidRequestException


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

def modify_hapg(HapgArn=None, Label=None, PartitionSerialList=None):
    """
    This is documentation for AWS CloudHSM Classic . For more information, see AWS CloudHSM Classic FAQs , the AWS CloudHSM Classic User Guide , and the AWS CloudHSM Classic API Reference .
    Modifies an existing high-availability partition group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.modify_hapg(
        HapgArn='string',
        Label='string',
        PartitionSerialList=[
            'string',
        ]
    )
    
    
    :type HapgArn: string
    :param HapgArn: [REQUIRED]\nThe ARN of the high-availability partition group to modify.\n

    :type Label: string
    :param Label: The new label for the high-availability partition group.

    :type PartitionSerialList: list
    :param PartitionSerialList: The list of partition serial numbers to make members of the high-availability partition group.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'HapgArn': 'string'
}


Response Structure

(dict) --

HapgArn (string) --
The ARN of the high-availability partition group.







Exceptions

CloudHSM.Client.exceptions.CloudHsmServiceException
CloudHSM.Client.exceptions.CloudHsmInternalException
CloudHSM.Client.exceptions.InvalidRequestException


    :return: {
        'HapgArn': 'string'
    }
    
    
    :returns: 
    CloudHSM.Client.exceptions.CloudHsmServiceException
    CloudHSM.Client.exceptions.CloudHsmInternalException
    CloudHSM.Client.exceptions.InvalidRequestException
    
    """
    pass

def modify_hsm(HsmArn=None, SubnetId=None, EniIp=None, IamRoleArn=None, ExternalId=None, SyslogIp=None):
    """
    This is documentation for AWS CloudHSM Classic . For more information, see AWS CloudHSM Classic FAQs , the AWS CloudHSM Classic User Guide , and the AWS CloudHSM Classic API Reference .
    Modifies an HSM.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.modify_hsm(
        HsmArn='string',
        SubnetId='string',
        EniIp='string',
        IamRoleArn='string',
        ExternalId='string',
        SyslogIp='string'
    )
    
    
    :type HsmArn: string
    :param HsmArn: [REQUIRED]\nThe ARN of the HSM to modify.\n

    :type SubnetId: string
    :param SubnetId: The new identifier of the subnet that the HSM is in. The new subnet must be in the same Availability Zone as the current subnet.

    :type EniIp: string
    :param EniIp: The new IP address for the elastic network interface (ENI) attached to the HSM.\nIf the HSM is moved to a different subnet, and an IP address is not specified, an IP address will be randomly chosen from the CIDR range of the new subnet.\n

    :type IamRoleArn: string
    :param IamRoleArn: The new IAM role ARN.

    :type ExternalId: string
    :param ExternalId: The new external ID.

    :type SyslogIp: string
    :param SyslogIp: The new IP address for the syslog monitoring server. The AWS CloudHSM service only supports one syslog monitoring server.

    :rtype: dict

ReturnsResponse Syntax
{
    'HsmArn': 'string'
}


Response Structure

(dict) --
Contains the output of the  ModifyHsm operation.

HsmArn (string) --
The ARN of the HSM.







Exceptions

CloudHSM.Client.exceptions.CloudHsmServiceException
CloudHSM.Client.exceptions.CloudHsmInternalException
CloudHSM.Client.exceptions.InvalidRequestException


    :return: {
        'HsmArn': 'string'
    }
    
    
    :returns: 
    CloudHSM.Client.exceptions.CloudHsmServiceException
    CloudHSM.Client.exceptions.CloudHsmInternalException
    CloudHSM.Client.exceptions.InvalidRequestException
    
    """
    pass

def modify_luna_client(ClientArn=None, Certificate=None):
    """
    This is documentation for AWS CloudHSM Classic . For more information, see AWS CloudHSM Classic FAQs , the AWS CloudHSM Classic User Guide , and the AWS CloudHSM Classic API Reference .
    Modifies the certificate used by the client.
    This action can potentially start a workflow to install the new certificate on the client\'s HSMs.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.modify_luna_client(
        ClientArn='string',
        Certificate='string'
    )
    
    
    :type ClientArn: string
    :param ClientArn: [REQUIRED]\nThe ARN of the client.\n

    :type Certificate: string
    :param Certificate: [REQUIRED]\nThe new certificate for the client.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ClientArn': 'string'
}


Response Structure

(dict) --

ClientArn (string) --
The ARN of the client.







Exceptions

CloudHSM.Client.exceptions.CloudHsmServiceException


    :return: {
        'ClientArn': 'string'
    }
    
    
    :returns: 
    CloudHSM.Client.exceptions.CloudHsmServiceException
    
    """
    pass

def remove_tags_from_resource(ResourceArn=None, TagKeyList=None):
    """
    This is documentation for AWS CloudHSM Classic . For more information, see AWS CloudHSM Classic FAQs , the AWS CloudHSM Classic User Guide , and the AWS CloudHSM Classic API Reference .
    Removes one or more tags from the specified AWS CloudHSM resource.
    To remove a tag, specify only the tag key to remove (not the value). To overwrite the value for an existing tag, use  AddTagsToResource .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.remove_tags_from_resource(
        ResourceArn='string',
        TagKeyList=[
            'string',
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the AWS CloudHSM resource.\n

    :type TagKeyList: list
    :param TagKeyList: [REQUIRED]\nThe tag key or keys to remove.\nSpecify only the tag key to remove (not the value). To overwrite the value for an existing tag, use AddTagsToResource .\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Status': 'string'
}


Response Structure

(dict) --

Status (string) --
The status of the operation.







Exceptions

CloudHSM.Client.exceptions.CloudHsmServiceException
CloudHSM.Client.exceptions.CloudHsmInternalException
CloudHSM.Client.exceptions.InvalidRequestException


    :return: {
        'Status': 'string'
    }
    
    
    :returns: 
    CloudHSM.Client.exceptions.CloudHsmServiceException
    CloudHSM.Client.exceptions.CloudHsmInternalException
    CloudHSM.Client.exceptions.InvalidRequestException
    
    """
    pass

