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

def activate_gateway(ActivationKey=None, GatewayName=None, GatewayTimezone=None, GatewayRegion=None, GatewayType=None, TapeDriveType=None, MediumChangerType=None, Tags=None):
    """
    Activates the gateway you previously deployed on your host. In the activation process, you specify information such as the AWS Region that you want to use for storing snapshots or tapes, the time zone for scheduled snapshots the gateway snapshot schedule window, an activation key, and a name for your gateway. The activation process also associates your gateway with your account; for more information, see  UpdateGatewayInformation .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Activates the gateway you previously deployed on your host.
    Expected Output:
    
    :example: response = client.activate_gateway(
        ActivationKey='string',
        GatewayName='string',
        GatewayTimezone='string',
        GatewayRegion='string',
        GatewayType='string',
        TapeDriveType='string',
        MediumChangerType='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ActivationKey: string
    :param ActivationKey: [REQUIRED]\nYour gateway activation key. You can obtain the activation key by sending an HTTP GET request with redirects enabled to the gateway IP address (port 80). The redirect URL returned in the response provides you the activation key for your gateway in the query string parameter activationKey . It may also include other activation-related parameters, however, these are merely defaults -- the arguments you pass to the ActivateGateway API call determine the actual configuration of your gateway.\nFor more information, see https://docs.aws.amazon.com/storagegateway/latest/userguide/get-activation-key.html in the Storage Gateway User Guide.\n

    :type GatewayName: string
    :param GatewayName: [REQUIRED]\nThe name you configured for your gateway.\n

    :type GatewayTimezone: string
    :param GatewayTimezone: [REQUIRED]\nA value that indicates the time zone you want to set for the gateway. The time zone is of the format 'GMT-hr:mm' or 'GMT+hr:mm'. For example, GMT-4:00 indicates the time is 4 hours behind GMT. GMT+2:00 indicates the time is 2 hours ahead of GMT. The time zone is used, for example, for scheduling snapshots and your gateway\'s maintenance schedule.\n

    :type GatewayRegion: string
    :param GatewayRegion: [REQUIRED]\nA value that indicates the AWS Region where you want to store your data. The gateway AWS Region specified must be the same AWS Region as the AWS Region in your Host header in the request. For more information about available AWS Regions and endpoints for AWS Storage Gateway, see Regions and Endpoints in the Amazon Web Services Glossary .\nValid Values: See AWS Storage Gateway Regions and Endpoints in the AWS General Reference.\n

    :type GatewayType: string
    :param GatewayType: A value that defines the type of gateway to activate. The type specified is critical to all later functions of the gateway and cannot be changed after activation. The default value is CACHED .\nValid Values: 'STORED', 'CACHED', 'VTL', 'FILE_S3'\n

    :type TapeDriveType: string
    :param TapeDriveType: The value that indicates the type of tape drive to use for tape gateway. This field is optional.\nValid Values: 'IBM-ULT3580-TD5'\n

    :type MediumChangerType: string
    :param MediumChangerType: The value that indicates the type of medium changer to use for tape gateway. This field is optional.\nValid Values: 'STK-L700', 'AWS-Gateway-VTL'\n

    :type Tags: list
    :param Tags: A list of up to 50 tags that you can assign to the gateway. Each tag is a key-value pair.\n\nNote\nValid characters for key and value are letters, spaces, and numbers that can be represented in UTF-8 format, and the following special characters: + - = . _ : / @. The maximum length of a tag\'s key is 128 characters, and the maximum length for a tag\'s value is 256 characters.\n\n\n(dict) --A key-value pair that helps you manage, filter, and search for your resource. Allowed characters: letters, white space, and numbers, representable in UTF-8, and the following characters: + - = . _ : /\n\nKey (string) -- [REQUIRED]Tag key (String). The key can\'t start with aws:.\n\nValue (string) -- [REQUIRED]Value of the tag key.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'GatewayARN': 'string'
}


Response Structure

(dict) --
AWS Storage Gateway returns the Amazon Resource Name (ARN) of the activated gateway. It is a string made of information such as your account, gateway name, and AWS Region. This ARN is used to reference the gateway in other API operations as well as resource-based authorization.

Note
For gateways activated prior to September 02, 2015, the gateway ARN contains the gateway name rather than the gateway ID. Changing the name of the gateway has no effect on the gateway ARN.


GatewayARN (string) --
The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and AWS Region.







Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError

Examples
Activates the gateway you previously deployed on your host.
response = client.activate_gateway(
    ActivationKey='29AV1-3OFV9-VVIUB-NKT0I-LRO6V',
    GatewayName='My_Gateway',
    GatewayRegion='us-east-1',
    GatewayTimezone='GMT-12:00',
    GatewayType='STORED',
    MediumChangerType='AWS-Gateway-VTL',
    TapeDriveType='IBM-ULT3580-TD5',
)

print(response)


Expected Output:
{
    'GatewayARN': 'arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-11A2222B',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'GatewayARN': 'string'
    }
    
    
    :returns: 
    StorageGateway.Client.exceptions.InvalidGatewayRequestException
    StorageGateway.Client.exceptions.InternalServerError
    
    """
    pass

def add_cache(GatewayARN=None, DiskIds=None):
    """
    Configures one or more gateway local disks as cache for a gateway. This operation is only supported in the cached volume, tape and file gateway type (see Storage Gateway Concepts ).
    In the request, you specify the gateway Amazon Resource Name (ARN) to which you want to add cache, and one or more disk IDs that you want to configure as cache.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example shows a request that activates a gateway-stored volume.
    Expected Output:
    
    :example: response = client.add_cache(
        GatewayARN='string',
        DiskIds=[
            'string',
        ]
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and AWS Region.\n

    :type DiskIds: list
    :param DiskIds: [REQUIRED]\nAn array of strings that identify disks that are to be configured as working storage. Each string has a minimum length of 1 and maximum length of 300. You can get the disk IDs from the ListLocalDisks API.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'GatewayARN': 'string'
}


Response Structure

(dict) --

GatewayARN (string) --
The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and AWS Region.







Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError

Examples
The following example shows a request that activates a gateway-stored volume.
response = client.add_cache(
    DiskIds=[
        'pci-0000:03:00.0-scsi-0:0:0:0',
        'pci-0000:03:00.0-scsi-0:0:1:0',
    ],
    GatewayARN='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B',
)

print(response)


Expected Output:
{
    'GatewayARN': 'arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'GatewayARN': 'string'
    }
    
    
    :returns: 
    StorageGateway.Client.exceptions.InvalidGatewayRequestException
    StorageGateway.Client.exceptions.InternalServerError
    
    """
    pass

def add_tags_to_resource(ResourceARN=None, Tags=None):
    """
    Adds one or more tags to the specified resource. You use tags to add metadata to resources, which you can use to categorize these resources. For example, you can categorize resources by purpose, owner, environment, or team. Each tag consists of a key and a value, which you define. You can add tags to the following AWS Storage Gateway resources:
    You can create a maximum of 50 tags for each resource. Virtual tapes and storage volumes that are recovered to a new gateway maintain their tags.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Adds one or more tags to the specified resource.
    Expected Output:
    
    :example: response = client.add_tags_to_resource(
        ResourceARN='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ResourceARN: string
    :param ResourceARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource you want to add tags to.\n

    :type Tags: list
    :param Tags: [REQUIRED]\nThe key-value pair that represents the tag you want to add to the resource. The value can be an empty string.\n\nNote\nValid characters for key and value are letters, spaces, and numbers representable in UTF-8 format, and the following special characters: + - = . _ : / @. The maximum length of a tag\'s key is 128 characters, and the maximum length for a tag\'s value is 256.\n\n\n(dict) --A key-value pair that helps you manage, filter, and search for your resource. Allowed characters: letters, white space, and numbers, representable in UTF-8, and the following characters: + - = . _ : /\n\nKey (string) -- [REQUIRED]Tag key (String). The key can\'t start with aws:.\n\nValue (string) -- [REQUIRED]Value of the tag key.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ResourceARN': 'string'
}


Response Structure

(dict) --
AddTagsToResourceOutput

ResourceARN (string) --
The Amazon Resource Name (ARN) of the resource you want to add tags to.







Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError

Examples
Adds one or more tags to the specified resource.
response = client.add_tags_to_resource(
    ResourceARN='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-11A2222B',
    Tags=[
        {
            'Key': 'Dev Gatgeway Region',
            'Value': 'East Coast',
        },
    ],
)

print(response)


Expected Output:
{
    'ResourceARN': 'arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-11A2222B',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ResourceARN': 'string'
    }
    
    
    :returns: 
    ResourceARN (string) -- [REQUIRED]
    The Amazon Resource Name (ARN) of the resource you want to add tags to.
    
    Tags (list) -- [REQUIRED]
    The key-value pair that represents the tag you want to add to the resource. The value can be an empty string.
    
    Note
    Valid characters for key and value are letters, spaces, and numbers representable in UTF-8 format, and the following special characters: + - = . _ : / @. The maximum length of a tag\'s key is 128 characters, and the maximum length for a tag\'s value is 256.
    
    
    (dict) --A key-value pair that helps you manage, filter, and search for your resource. Allowed characters: letters, white space, and numbers, representable in UTF-8, and the following characters: + - = . _ : /
    
    Key (string) -- [REQUIRED]Tag key (String). The key can\'t start with aws:.
    
    Value (string) -- [REQUIRED]Value of the tag key.
    
    
    
    
    
    
    """
    pass

def add_upload_buffer(GatewayARN=None, DiskIds=None):
    """
    Configures one or more gateway local disks as upload buffer for a specified gateway. This operation is supported for the stored volume, cached volume and tape gateway types.
    In the request, you specify the gateway Amazon Resource Name (ARN) to which you want to add upload buffer, and one or more disk IDs that you want to configure as upload buffer.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Configures one or more gateway local disks as upload buffer for a specified gateway.
    Expected Output:
    
    :example: response = client.add_upload_buffer(
        GatewayARN='string',
        DiskIds=[
            'string',
        ]
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and AWS Region.\n

    :type DiskIds: list
    :param DiskIds: [REQUIRED]\nAn array of strings that identify disks that are to be configured as working storage. Each string has a minimum length of 1 and maximum length of 300. You can get the disk IDs from the ListLocalDisks API.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'GatewayARN': 'string'
}


Response Structure

(dict) --

GatewayARN (string) --
The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and AWS Region.







Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError

Examples
Configures one or more gateway local disks as upload buffer for a specified gateway.
response = client.add_upload_buffer(
    DiskIds=[
        'pci-0000:03:00.0-scsi-0:0:0:0',
        'pci-0000:03:00.0-scsi-0:0:1:0',
    ],
    GatewayARN='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B',
)

print(response)


Expected Output:
{
    'GatewayARN': 'arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'GatewayARN': 'string'
    }
    
    
    :returns: 
    StorageGateway.Client.exceptions.InvalidGatewayRequestException
    StorageGateway.Client.exceptions.InternalServerError
    
    """
    pass

def add_working_storage(GatewayARN=None, DiskIds=None):
    """
    Configures one or more gateway local disks as working storage for a gateway. This operation is only supported in the stored volume gateway type. This operation is deprecated in cached volume API version 20120630. Use  AddUploadBuffer instead.
    In the request, you specify the gateway Amazon Resource Name (ARN) to which you want to add working storage, and one or more disk IDs that you want to configure as working storage.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Configures one or more gateway local disks as working storage for a gateway. (Working storage is also referred to as upload buffer.)
    Expected Output:
    
    :example: response = client.add_working_storage(
        GatewayARN='string',
        DiskIds=[
            'string',
        ]
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and AWS Region.\n

    :type DiskIds: list
    :param DiskIds: [REQUIRED]\nAn array of strings that identify disks that are to be configured as working storage. Each string has a minimum length of 1 and maximum length of 300. You can get the disk IDs from the ListLocalDisks API.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'GatewayARN': 'string'
}


Response Structure

(dict) --
A JSON object containing the Amazon Resource Name (ARN) of the gateway for which working storage was configured.

GatewayARN (string) --
The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and AWS Region.







Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError

Examples
Configures one or more gateway local disks as working storage for a gateway. (Working storage is also referred to as upload buffer.)
response = client.add_working_storage(
    DiskIds=[
        'pci-0000:03:00.0-scsi-0:0:0:0',
        'pci-0000:03:00.0-scsi-0:0:1:0',
    ],
    GatewayARN='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B',
)

print(response)


Expected Output:
{
    'GatewayARN': 'arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'GatewayARN': 'string'
    }
    
    
    :returns: 
    StorageGateway.Client.exceptions.InvalidGatewayRequestException
    StorageGateway.Client.exceptions.InternalServerError
    
    """
    pass

def assign_tape_pool(TapeARN=None, PoolId=None):
    """
    Assigns a tape to a tape pool for archiving. The tape assigned to a pool is archived in the S3 storage class that is associated with the pool. When you use your backup application to eject the tape, the tape is archived directly into the S3 storage class (S3 Glacier or S3 Glacier Deep Archive) that corresponds to the pool.
    Valid values: "GLACIER", "DEEP_ARCHIVE"
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.assign_tape_pool(
        TapeARN='string',
        PoolId='string'
    )
    
    
    :type TapeARN: string
    :param TapeARN: [REQUIRED]\nThe unique Amazon Resource Name (ARN) of the virtual tape that you want to add to the tape pool.\n

    :type PoolId: string
    :param PoolId: [REQUIRED]\nThe ID of the pool that you want to add your tape to for archiving. The tape in this pool is archived in the S3 storage class that is associated with the pool. When you use your backup application to eject the tape, the tape is archived directly into the storage class (S3 Glacier or S3 Glacier Deep Archive) that corresponds to the pool.\nValid values: 'GLACIER', 'DEEP_ARCHIVE'\n

    :rtype: dict

ReturnsResponse Syntax
{
    'TapeARN': 'string'
}


Response Structure

(dict) --

TapeARN (string) --
The unique Amazon Resource Names (ARN) of the virtual tape that was added to the tape pool.







Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError


    :return: {
        'TapeARN': 'string'
    }
    
    
    :returns: 
    StorageGateway.Client.exceptions.InvalidGatewayRequestException
    StorageGateway.Client.exceptions.InternalServerError
    
    """
    pass

def attach_volume(GatewayARN=None, TargetName=None, VolumeARN=None, NetworkInterfaceId=None, DiskId=None):
    """
    Connects a volume to an iSCSI connection and then attaches the volume to the specified gateway. Detaching and attaching a volume enables you to recover your data from one gateway to a different gateway without creating a snapshot. It also makes it easier to move your volumes from an on-premises gateway to a gateway hosted on an Amazon EC2 instance.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.attach_volume(
        GatewayARN='string',
        TargetName='string',
        VolumeARN='string',
        NetworkInterfaceId='string',
        DiskId='string'
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the gateway that you want to attach the volume to.\n

    :type TargetName: string
    :param TargetName: The name of the iSCSI target used by an initiator to connect to a volume and used as a suffix for the target ARN. For example, specifying TargetName as myvolume results in the target ARN of arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/target/iqn.1997-05.com.amazon:myvolume . The target name must be unique across all volumes on a gateway.\nIf you don\'t specify a value, Storage Gateway uses the value that was previously used for this volume as the new target name.\n

    :type VolumeARN: string
    :param VolumeARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the volume to attach to the specified gateway.\n

    :type NetworkInterfaceId: string
    :param NetworkInterfaceId: [REQUIRED]\nThe network interface of the gateway on which to expose the iSCSI target. Only IPv4 addresses are accepted. Use DescribeGatewayInformation to get a list of the network interfaces available on a gateway.\nValid Values: A valid IP address.\n

    :type DiskId: string
    :param DiskId: The unique device ID or other distinguishing data that identifies the local disk used to create the volume. This value is only required when you are attaching a stored volume.

    :rtype: dict

ReturnsResponse Syntax
{
    'VolumeARN': 'string',
    'TargetARN': 'string'
}


Response Structure

(dict) --
AttachVolumeOutput

VolumeARN (string) --
The Amazon Resource Name (ARN) of the volume that was attached to the gateway.

TargetARN (string) --
The Amazon Resource Name (ARN) of the volume target, which includes the iSCSI name for the initiator that was used to connect to the target.







Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError


    :return: {
        'VolumeARN': 'string',
        'TargetARN': 'string'
    }
    
    
    :returns: 
    StorageGateway.Client.exceptions.InvalidGatewayRequestException
    StorageGateway.Client.exceptions.InternalServerError
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def cancel_archival(GatewayARN=None, TapeARN=None):
    """
    Cancels archiving of a virtual tape to the virtual tape shelf (VTS) after the archiving process is initiated. This operation is only supported in the tape gateway type.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Cancels archiving of a virtual tape to the virtual tape shelf (VTS) after the archiving process is initiated.
    Expected Output:
    
    :example: response = client.cancel_archival(
        GatewayARN='string',
        TapeARN='string'
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and AWS Region.\n

    :type TapeARN: string
    :param TapeARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the virtual tape you want to cancel archiving for.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'TapeARN': 'string'
}


Response Structure

(dict) --
CancelArchivalOutput

TapeARN (string) --
The Amazon Resource Name (ARN) of the virtual tape for which archiving was canceled.







Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError

Examples
Cancels archiving of a virtual tape to the virtual tape shelf (VTS) after the archiving process is initiated.
response = client.cancel_archival(
    GatewayARN='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B',
    TapeARN='arn:aws:storagegateway:us-east-1:999999999999:tape/AMZN01A2A4',
)

print(response)


Expected Output:
{
    'TapeARN': 'arn:aws:storagegateway:us-east-1:999999999999:tape/AMZN01A2A4',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'TapeARN': 'string'
    }
    
    
    :returns: 
    StorageGateway.Client.exceptions.InvalidGatewayRequestException
    StorageGateway.Client.exceptions.InternalServerError
    
    """
    pass

def cancel_retrieval(GatewayARN=None, TapeARN=None):
    """
    Cancels retrieval of a virtual tape from the virtual tape shelf (VTS) to a gateway after the retrieval process is initiated. The virtual tape is returned to the VTS. This operation is only supported in the tape gateway type.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Cancels retrieval of a virtual tape from the virtual tape shelf (VTS) to a gateway after the retrieval process is initiated.
    Expected Output:
    
    :example: response = client.cancel_retrieval(
        GatewayARN='string',
        TapeARN='string'
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and AWS Region.\n

    :type TapeARN: string
    :param TapeARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the virtual tape you want to cancel retrieval for.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'TapeARN': 'string'
}


Response Structure

(dict) --
CancelRetrievalOutput

TapeARN (string) --
The Amazon Resource Name (ARN) of the virtual tape for which retrieval was canceled.







Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError

Examples
Cancels retrieval of a virtual tape from the virtual tape shelf (VTS) to a gateway after the retrieval process is initiated.
response = client.cancel_retrieval(
    GatewayARN='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B',
    TapeARN='arn:aws:storagegateway:us-east-1:999999999999:tape/AMZN01A2A4',
)

print(response)


Expected Output:
{
    'TapeARN': 'arn:aws:storagegateway:us-east-1:999999999999:tape/AMZN01A2A4',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'TapeARN': 'string'
    }
    
    
    :returns: 
    StorageGateway.Client.exceptions.InvalidGatewayRequestException
    StorageGateway.Client.exceptions.InternalServerError
    
    """
    pass

def create_cached_iscsi_volume(GatewayARN=None, VolumeSizeInBytes=None, SnapshotId=None, TargetName=None, SourceVolumeARN=None, NetworkInterfaceId=None, ClientToken=None, KMSEncrypted=None, KMSKey=None, Tags=None):
    """
    Creates a cached volume on a specified cached volume gateway. This operation is only supported in the cached volume gateway type.
    In the request, you must specify the gateway, size of the volume in bytes, the iSCSI target name, an IP address on which to expose the target, and a unique client token. In response, the gateway creates the volume and returns information about it. This information includes the volume Amazon Resource Name (ARN), its size, and the iSCSI target ARN that initiators can use to connect to the volume target.
    Optionally, you can provide the ARN for an existing volume as the SourceVolumeARN for this cached volume, which creates an exact copy of the existing volume\xe2\x80\x99s latest recovery point. The VolumeSizeInBytes value must be equal to or larger than the size of the copied volume, in bytes.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Creates a cached volume on a specified cached gateway.
    Expected Output:
    
    :example: response = client.create_cached_iscsi_volume(
        GatewayARN='string',
        VolumeSizeInBytes=123,
        SnapshotId='string',
        TargetName='string',
        SourceVolumeARN='string',
        NetworkInterfaceId='string',
        ClientToken='string',
        KMSEncrypted=True|False,
        KMSKey='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and AWS Region.\n

    :type VolumeSizeInBytes: integer
    :param VolumeSizeInBytes: [REQUIRED]\nThe size of the volume in bytes.\n

    :type SnapshotId: string
    :param SnapshotId: The snapshot ID (e.g. 'snap-1122aabb') of the snapshot to restore as the new cached volume. Specify this field if you want to create the iSCSI storage volume from a snapshot otherwise do not include this field. To list snapshots for your account use DescribeSnapshots in the Amazon Elastic Compute Cloud API Reference .

    :type TargetName: string
    :param TargetName: [REQUIRED]\nThe name of the iSCSI target used by an initiator to connect to a volume and used as a suffix for the target ARN. For example, specifying TargetName as myvolume results in the target ARN of arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/target/iqn.1997-05.com.amazon:myvolume . The target name must be unique across all volumes on a gateway.\nIf you don\'t specify a value, Storage Gateway uses the value that was previously used for this volume as the new target name.\n

    :type SourceVolumeARN: string
    :param SourceVolumeARN: The ARN for an existing volume. Specifying this ARN makes the new volume into an exact copy of the specified existing volume\'s latest recovery point. The VolumeSizeInBytes value for this new volume must be equal to or larger than the size of the existing volume, in bytes.

    :type NetworkInterfaceId: string
    :param NetworkInterfaceId: [REQUIRED]\nThe network interface of the gateway on which to expose the iSCSI target. Only IPv4 addresses are accepted. Use DescribeGatewayInformation to get a list of the network interfaces available on a gateway.\nValid Values: A valid IP address.\n

    :type ClientToken: string
    :param ClientToken: [REQUIRED]\nA unique identifier that you use to retry a request. If you retry a request, use the same ClientToken you specified in the initial request.\n

    :type KMSEncrypted: boolean
    :param KMSEncrypted: True to use Amazon S3 server-side encryption with your own AWS KMS key, or false to use a key managed by Amazon S3. Optional.

    :type KMSKey: string
    :param KMSKey: The Amazon Resource Name (ARN) of the AWS KMS key used for Amazon S3 server-side encryption. This value can only be set when KMSEncrypted is true. Optional.

    :type Tags: list
    :param Tags: A list of up to 50 tags that you can assign to a cached volume. Each tag is a key-value pair.\n\nNote\nValid characters for key and value are letters, spaces, and numbers that you can represent in UTF-8 format, and the following special characters: + - = . _ : / @. The maximum length of a tag\'s key is 128 characters, and the maximum length for a tag\'s value is 256 characters.\n\n\n(dict) --A key-value pair that helps you manage, filter, and search for your resource. Allowed characters: letters, white space, and numbers, representable in UTF-8, and the following characters: + - = . _ : /\n\nKey (string) -- [REQUIRED]Tag key (String). The key can\'t start with aws:.\n\nValue (string) -- [REQUIRED]Value of the tag key.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'VolumeARN': 'string',
    'TargetARN': 'string'
}


Response Structure

(dict) --

VolumeARN (string) --
The Amazon Resource Name (ARN) of the configured volume.

TargetARN (string) --
The Amazon Resource Name (ARN) of the volume target, which includes the iSCSI name that initiators can use to connect to the target.







Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError

Examples
Creates a cached volume on a specified cached gateway.
response = client.create_cached_iscsi_volume(
    ClientToken='cachedvol112233',
    GatewayARN='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B',
    NetworkInterfaceId='10.1.1.1',
    SnapshotId='snap-f47b7b94',
    TargetName='my-volume',
    VolumeSizeInBytes=536870912000,
)

print(response)


Expected Output:
{
    'TargetARN': 'arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B/target/iqn.1997-05.com.amazon:myvolume',
    'VolumeARN': 'arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B/volume/vol-1122AABB',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'VolumeARN': 'string',
        'TargetARN': 'string'
    }
    
    
    :returns: 
    StorageGateway.Client.exceptions.InvalidGatewayRequestException
    StorageGateway.Client.exceptions.InternalServerError
    
    """
    pass

def create_nfs_file_share(ClientToken=None, NFSFileShareDefaults=None, GatewayARN=None, KMSEncrypted=None, KMSKey=None, Role=None, LocationARN=None, DefaultStorageClass=None, ObjectACL=None, ClientList=None, Squash=None, ReadOnly=None, GuessMIMETypeEnabled=None, RequesterPays=None, Tags=None):
    """
    Creates a Network File System (NFS) file share on an existing file gateway. In Storage Gateway, a file share is a file system mount point backed by Amazon S3 cloud storage. Storage Gateway exposes file shares using an NFS interface. This operation is only supported for file gateways.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_nfs_file_share(
        ClientToken='string',
        NFSFileShareDefaults={
            'FileMode': 'string',
            'DirectoryMode': 'string',
            'GroupId': 123,
            'OwnerId': 123
        },
        GatewayARN='string',
        KMSEncrypted=True|False,
        KMSKey='string',
        Role='string',
        LocationARN='string',
        DefaultStorageClass='string',
        ObjectACL='private'|'public-read'|'public-read-write'|'authenticated-read'|'bucket-owner-read'|'bucket-owner-full-control'|'aws-exec-read',
        ClientList=[
            'string',
        ],
        Squash='string',
        ReadOnly=True|False,
        GuessMIMETypeEnabled=True|False,
        RequesterPays=True|False,
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ClientToken: string
    :param ClientToken: [REQUIRED]\nA unique string value that you supply that is used by file gateway to ensure idempotent file share creation.\n

    :type NFSFileShareDefaults: dict
    :param NFSFileShareDefaults: File share default values. Optional.\n\nFileMode (string) --The Unix file mode in the form 'nnnn'. For example, '0666' represents the default file mode inside the file share. The default value is 0666.\n\nDirectoryMode (string) --The Unix directory mode in the form 'nnnn'. For example, '0666' represents the default access mode for all directories inside the file share. The default value is 0777.\n\nGroupId (integer) --The default group ID for the file share (unless the files have another group ID specified). The default value is nfsnobody.\n\nOwnerId (integer) --The default owner ID for files in the file share (unless the files have another owner ID specified). The default value is nfsnobody.\n\n\n

    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the file gateway on which you want to create a file share.\n

    :type KMSEncrypted: boolean
    :param KMSEncrypted: True to use Amazon S3 server-side encryption with your own AWS KMS key, or false to use a key managed by Amazon S3. Optional.

    :type KMSKey: string
    :param KMSKey: The Amazon Resource Name (ARN) AWS KMS key used for Amazon S3 server-side encryption. This value can only be set when KMSEncrypted is true. Optional.

    :type Role: string
    :param Role: [REQUIRED]\nThe ARN of the AWS Identity and Access Management (IAM) role that a file gateway assumes when it accesses the underlying storage.\n

    :type LocationARN: string
    :param LocationARN: [REQUIRED]\nThe ARN of the backed storage used for storing file data.\n

    :type DefaultStorageClass: string
    :param DefaultStorageClass: The default storage class for objects put into an Amazon S3 bucket by the file gateway. Possible values are S3_STANDARD , S3_STANDARD_IA , or S3_ONEZONE_IA . If this field is not populated, the default value S3_STANDARD is used. Optional.

    :type ObjectACL: string
    :param ObjectACL: A value that sets the access control list permission for objects in the S3 bucket that a file gateway puts objects into. The default value is 'private'.

    :type ClientList: list
    :param ClientList: The list of clients that are allowed to access the file gateway. The list must contain either valid IP addresses or valid CIDR blocks.\n\n(string) --\n\n

    :type Squash: string
    :param Squash: A value that maps a user to anonymous user. Valid options are the following:\n\nRootSquash - Only root is mapped to anonymous user.\nNoSquash - No one is mapped to anonymous user\nAllSquash - Everyone is mapped to anonymous user.\n\n

    :type ReadOnly: boolean
    :param ReadOnly: A value that sets the write status of a file share. This value is true if the write status is read-only, and otherwise false.

    :type GuessMIMETypeEnabled: boolean
    :param GuessMIMETypeEnabled: A value that enables guessing of the MIME type for uploaded objects based on file extensions. Set this value to true to enable MIME type guessing, and otherwise to false. The default value is true.

    :type RequesterPays: boolean
    :param RequesterPays: A value that sets who pays the cost of the request and the cost associated with data download from the S3 bucket. If this value is set to true, the requester pays the costs. Otherwise the S3 bucket owner pays. However, the S3 bucket owner always pays the cost of storing data.\n\nNote\nRequesterPays is a configuration for the S3 bucket that backs the file share, so make sure that the configuration on the file share is the same as the S3 bucket configuration.\n\n

    :type Tags: list
    :param Tags: A list of up to 50 tags that can be assigned to the NFS file share. Each tag is a key-value pair.\n\nNote\nValid characters for key and value are letters, spaces, and numbers representable in UTF-8 format, and the following special characters: + - = . _ : / @. The maximum length of a tag\'s key is 128 characters, and the maximum length for a tag\'s value is 256.\n\n\n(dict) --A key-value pair that helps you manage, filter, and search for your resource. Allowed characters: letters, white space, and numbers, representable in UTF-8, and the following characters: + - = . _ : /\n\nKey (string) -- [REQUIRED]Tag key (String). The key can\'t start with aws:.\n\nValue (string) -- [REQUIRED]Value of the tag key.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'FileShareARN': 'string'
}


Response Structure

(dict) --
CreateNFSFileShareOutput

FileShareARN (string) --
The Amazon Resource Name (ARN) of the newly created file share.







Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError


    :return: {
        'FileShareARN': 'string'
    }
    
    
    :returns: 
    StorageGateway.Client.exceptions.InvalidGatewayRequestException
    StorageGateway.Client.exceptions.InternalServerError
    
    """
    pass

def create_smb_file_share(ClientToken=None, GatewayARN=None, KMSEncrypted=None, KMSKey=None, Role=None, LocationARN=None, DefaultStorageClass=None, ObjectACL=None, ReadOnly=None, GuessMIMETypeEnabled=None, RequesterPays=None, SMBACLEnabled=None, AdminUserList=None, ValidUserList=None, InvalidUserList=None, AuditDestinationARN=None, Authentication=None, Tags=None):
    """
    Creates a Server Message Block (SMB) file share on an existing file gateway. In Storage Gateway, a file share is a file system mount point backed by Amazon S3 cloud storage. Storage Gateway expose file shares using an SMB interface. This operation is only supported for file gateways.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_smb_file_share(
        ClientToken='string',
        GatewayARN='string',
        KMSEncrypted=True|False,
        KMSKey='string',
        Role='string',
        LocationARN='string',
        DefaultStorageClass='string',
        ObjectACL='private'|'public-read'|'public-read-write'|'authenticated-read'|'bucket-owner-read'|'bucket-owner-full-control'|'aws-exec-read',
        ReadOnly=True|False,
        GuessMIMETypeEnabled=True|False,
        RequesterPays=True|False,
        SMBACLEnabled=True|False,
        AdminUserList=[
            'string',
        ],
        ValidUserList=[
            'string',
        ],
        InvalidUserList=[
            'string',
        ],
        AuditDestinationARN='string',
        Authentication='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ClientToken: string
    :param ClientToken: [REQUIRED]\nA unique string value that you supply that is used by file gateway to ensure idempotent file share creation.\n

    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]\nThe ARN of the file gateway on which you want to create a file share.\n

    :type KMSEncrypted: boolean
    :param KMSEncrypted: True to use Amazon S3 server-side encryption with your own AWS KMS key, or false to use a key managed by Amazon S3. Optional.

    :type KMSKey: string
    :param KMSKey: The Amazon Resource Name (ARN) of the AWS KMS key used for Amazon S3 server-side encryption. This value can only be set when KMSEncrypted is true. Optional.

    :type Role: string
    :param Role: [REQUIRED]\nThe ARN of the AWS Identity and Access Management (IAM) role that a file gateway assumes when it accesses the underlying storage.\n

    :type LocationARN: string
    :param LocationARN: [REQUIRED]\nThe ARN of the backed storage used for storing file data.\n

    :type DefaultStorageClass: string
    :param DefaultStorageClass: The default storage class for objects put into an Amazon S3 bucket by the file gateway. Possible values are S3_STANDARD , S3_STANDARD_IA , or S3_ONEZONE_IA . If this field is not populated, the default value S3_STANDARD is used. Optional.

    :type ObjectACL: string
    :param ObjectACL: A value that sets the access control list permission for objects in the S3 bucket that a file gateway puts objects into. The default value is 'private'.

    :type ReadOnly: boolean
    :param ReadOnly: A value that sets the write status of a file share. This value is true if the write status is read-only, and otherwise false.

    :type GuessMIMETypeEnabled: boolean
    :param GuessMIMETypeEnabled: A value that enables guessing of the MIME type for uploaded objects based on file extensions. Set this value to true to enable MIME type guessing, and otherwise to false. The default value is true.

    :type RequesterPays: boolean
    :param RequesterPays: A value that sets who pays the cost of the request and the cost associated with data download from the S3 bucket. If this value is set to true, the requester pays the costs. Otherwise the S3 bucket owner pays. However, the S3 bucket owner always pays the cost of storing data.\n\nNote\nRequesterPays is a configuration for the S3 bucket that backs the file share, so make sure that the configuration on the file share is the same as the S3 bucket configuration.\n\n

    :type SMBACLEnabled: boolean
    :param SMBACLEnabled: Set this value to 'true to enable ACL (access control list) on the SMB file share. Set it to 'false' to map file and directory permissions to the POSIX permissions.\nFor more information, see https://docs.aws.amazon.com/storagegateway/latest/userguide/smb-acl.html in the Storage Gateway User Guide.\n

    :type AdminUserList: list
    :param AdminUserList: A list of users in the Active Directory that will be granted administrator privileges on the file share. These users can do all file operations as the super-user.\n\nWarning\nUse this option very carefully, because any user in this list can do anything they like on the file share, regardless of file permissions.\n\n\n(string) --\n\n

    :type ValidUserList: list
    :param ValidUserList: A list of users or groups in the Active Directory that are allowed to access the file share. A group must be prefixed with the @ character. For example @group1 . Can only be set if Authentication is set to ActiveDirectory .\n\n(string) --\n\n

    :type InvalidUserList: list
    :param InvalidUserList: A list of users or groups in the Active Directory that are not allowed to access the file share. A group must be prefixed with the @ character. For example, @group1 . Can only be set if Authentication is set to ActiveDirectory .\n\n(string) --\n\n

    :type AuditDestinationARN: string
    :param AuditDestinationARN: The Amazon Resource Name (ARN) of the storage used for the audit logs.

    :type Authentication: string
    :param Authentication: The authentication method that users use to access the file share.\nValid values are ActiveDirectory or GuestAccess . The default is ActiveDirectory .\n

    :type Tags: list
    :param Tags: A list of up to 50 tags that can be assigned to the NFS file share. Each tag is a key-value pair.\n\nNote\nValid characters for key and value are letters, spaces, and numbers representable in UTF-8 format, and the following special characters: + - = . _ : / @. The maximum length of a tag\'s key is 128 characters, and the maximum length for a tag\'s value is 256.\n\n\n(dict) --A key-value pair that helps you manage, filter, and search for your resource. Allowed characters: letters, white space, and numbers, representable in UTF-8, and the following characters: + - = . _ : /\n\nKey (string) -- [REQUIRED]Tag key (String). The key can\'t start with aws:.\n\nValue (string) -- [REQUIRED]Value of the tag key.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'FileShareARN': 'string'
}


Response Structure

(dict) --
CreateSMBFileShareOutput

FileShareARN (string) --
The Amazon Resource Name (ARN) of the newly created file share.







Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError


    :return: {
        'FileShareARN': 'string'
    }
    
    
    :returns: 
    StorageGateway.Client.exceptions.InvalidGatewayRequestException
    StorageGateway.Client.exceptions.InternalServerError
    
    """
    pass

def create_snapshot(VolumeARN=None, SnapshotDescription=None, Tags=None):
    """
    Initiates a snapshot of a volume.
    AWS Storage Gateway provides the ability to back up point-in-time snapshots of your data to Amazon Simple Storage Service (Amazon S3) for durable off-site recovery, as well as import the data to an Amazon Elastic Block Store (EBS) volume in Amazon Elastic Compute Cloud (EC2). You can take snapshots of your gateway volume on a scheduled or ad hoc basis. This API enables you to take an ad hoc snapshot. For more information, see Editing a Snapshot Schedule .
    In the CreateSnapshot request you identify the volume by providing its Amazon Resource Name (ARN). You must also provide description for the snapshot. When AWS Storage Gateway takes the snapshot of specified volume, the snapshot and description appears in the AWS Storage Gateway Console. In response, AWS Storage Gateway returns you a snapshot ID. You can use this snapshot ID to check the snapshot progress or later use it when you want to create a volume from a snapshot. This operation is only supported in stored and cached volume gateway type.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Initiates an ad-hoc snapshot of a gateway volume.
    Expected Output:
    
    :example: response = client.create_snapshot(
        VolumeARN='string',
        SnapshotDescription='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type VolumeARN: string
    :param VolumeARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the volume. Use the ListVolumes operation to return a list of gateway volumes.\n

    :type SnapshotDescription: string
    :param SnapshotDescription: [REQUIRED]\nTextual description of the snapshot that appears in the Amazon EC2 console, Elastic Block Store snapshots panel in the Description field, and in the AWS Storage Gateway snapshot Details pane, Description field\n

    :type Tags: list
    :param Tags: A list of up to 50 tags that can be assigned to a snapshot. Each tag is a key-value pair.\n\nNote\nValid characters for key and value are letters, spaces, and numbers representable in UTF-8 format, and the following special characters: + - = . _ : / @. The maximum length of a tag\'s key is 128 characters, and the maximum length for a tag\'s value is 256.\n\n\n(dict) --A key-value pair that helps you manage, filter, and search for your resource. Allowed characters: letters, white space, and numbers, representable in UTF-8, and the following characters: + - = . _ : /\n\nKey (string) -- [REQUIRED]Tag key (String). The key can\'t start with aws:.\n\nValue (string) -- [REQUIRED]Value of the tag key.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'VolumeARN': 'string',
    'SnapshotId': 'string'
}


Response Structure

(dict) --
A JSON object containing the following fields:

VolumeARN (string) --
The Amazon Resource Name (ARN) of the volume of which the snapshot was taken.

SnapshotId (string) --
The snapshot ID that is used to refer to the snapshot in future operations such as describing snapshots (Amazon Elastic Compute Cloud API DescribeSnapshots ) or creating a volume from a snapshot ( CreateStorediSCSIVolume ).







Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError
StorageGateway.Client.exceptions.ServiceUnavailableError

Examples
Initiates an ad-hoc snapshot of a gateway volume.
response = client.create_snapshot(
    SnapshotDescription='My root volume snapshot as of 10/03/2017',
    VolumeARN='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B/volume/vol-1122AABB',
)

print(response)


Expected Output:
{
    'SnapshotId': 'snap-78e22663',
    'VolumeARN': 'arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B/volume/vol-1122AABB',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'VolumeARN': 'string',
        'SnapshotId': 'string'
    }
    
    
    :returns: 
    StorageGateway.Client.exceptions.InvalidGatewayRequestException
    StorageGateway.Client.exceptions.InternalServerError
    StorageGateway.Client.exceptions.ServiceUnavailableError
    
    """
    pass

def create_snapshot_from_volume_recovery_point(VolumeARN=None, SnapshotDescription=None, Tags=None):
    """
    Initiates a snapshot of a gateway from a volume recovery point. This operation is only supported in the cached volume gateway type.
    A volume recovery point is a point in time at which all data of the volume is consistent and from which you can create a snapshot. To get a list of volume recovery point for cached volume gateway, use  ListVolumeRecoveryPoints .
    In the CreateSnapshotFromVolumeRecoveryPoint request, you identify the volume by providing its Amazon Resource Name (ARN). You must also provide a description for the snapshot. When the gateway takes a snapshot of the specified volume, the snapshot and its description appear in the AWS Storage Gateway console. In response, the gateway returns you a snapshot ID. You can use this snapshot ID to check the snapshot progress or later use it when you want to create a volume from a snapshot.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Initiates a snapshot of a gateway from a volume recovery point.
    Expected Output:
    
    :example: response = client.create_snapshot_from_volume_recovery_point(
        VolumeARN='string',
        SnapshotDescription='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type VolumeARN: string
    :param VolumeARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the iSCSI volume target. Use the DescribeStorediSCSIVolumes operation to return to retrieve the TargetARN for specified VolumeARN.\n

    :type SnapshotDescription: string
    :param SnapshotDescription: [REQUIRED]\nTextual description of the snapshot that appears in the Amazon EC2 console, Elastic Block Store snapshots panel in the Description field, and in the AWS Storage Gateway snapshot Details pane, Description field\n

    :type Tags: list
    :param Tags: A list of up to 50 tags that can be assigned to a snapshot. Each tag is a key-value pair.\n\nNote\nValid characters for key and value are letters, spaces, and numbers representable in UTF-8 format, and the following special characters: + - = . _ : / @. The maximum length of a tag\'s key is 128 characters, and the maximum length for a tag\'s value is 256.\n\n\n(dict) --A key-value pair that helps you manage, filter, and search for your resource. Allowed characters: letters, white space, and numbers, representable in UTF-8, and the following characters: + - = . _ : /\n\nKey (string) -- [REQUIRED]Tag key (String). The key can\'t start with aws:.\n\nValue (string) -- [REQUIRED]Value of the tag key.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'SnapshotId': 'string',
    'VolumeARN': 'string',
    'VolumeRecoveryPointTime': 'string'
}


Response Structure

(dict) --

SnapshotId (string) --
The ID of the snapshot.

VolumeARN (string) --
The Amazon Resource Name (ARN) of the iSCSI volume target. Use the  DescribeStorediSCSIVolumes operation to return to retrieve the TargetARN for specified VolumeARN.

VolumeRecoveryPointTime (string) --
The time the volume was created from the recovery point.







Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError
StorageGateway.Client.exceptions.ServiceUnavailableError

Examples
Initiates a snapshot of a gateway from a volume recovery point.
response = client.create_snapshot_from_volume_recovery_point(
    SnapshotDescription='My root volume snapshot as of 2017-06-30T10:10:10.000Z',
    VolumeARN='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B/volume/vol-1122AABB',
)

print(response)


Expected Output:
{
    'SnapshotId': 'snap-78e22663',
    'VolumeARN': 'arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B/volume/vol-1122AABB',
    'VolumeRecoveryPointTime': '2017-06-30T10:10:10.000Z',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'SnapshotId': 'string',
        'VolumeARN': 'string',
        'VolumeRecoveryPointTime': 'string'
    }
    
    
    :returns: 
    StorageGateway.Client.exceptions.InvalidGatewayRequestException
    StorageGateway.Client.exceptions.InternalServerError
    StorageGateway.Client.exceptions.ServiceUnavailableError
    
    """
    pass

def create_stored_iscsi_volume(GatewayARN=None, DiskId=None, SnapshotId=None, PreserveExistingData=None, TargetName=None, NetworkInterfaceId=None, KMSEncrypted=None, KMSKey=None, Tags=None):
    """
    Creates a volume on a specified gateway. This operation is only supported in the stored volume gateway type.
    The size of the volume to create is inferred from the disk size. You can choose to preserve existing data on the disk, create volume from an existing snapshot, or create an empty volume. If you choose to create an empty gateway volume, then any existing data on the disk is erased.
    In the request you must specify the gateway and the disk information on which you are creating the volume. In response, the gateway creates the volume and returns volume information such as the volume Amazon Resource Name (ARN), its size, and the iSCSI target ARN that initiators can use to connect to the volume target.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Creates a stored volume on a specified stored gateway.
    Expected Output:
    
    :example: response = client.create_stored_iscsi_volume(
        GatewayARN='string',
        DiskId='string',
        SnapshotId='string',
        PreserveExistingData=True|False,
        TargetName='string',
        NetworkInterfaceId='string',
        KMSEncrypted=True|False,
        KMSKey='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and AWS Region.\n

    :type DiskId: string
    :param DiskId: [REQUIRED]\nThe unique identifier for the gateway local disk that is configured as a stored volume. Use ListLocalDisks to list disk IDs for a gateway.\n

    :type SnapshotId: string
    :param SnapshotId: The snapshot ID (e.g. 'snap-1122aabb') of the snapshot to restore as the new stored volume. Specify this field if you want to create the iSCSI storage volume from a snapshot otherwise do not include this field. To list snapshots for your account use DescribeSnapshots in the Amazon Elastic Compute Cloud API Reference .

    :type PreserveExistingData: boolean
    :param PreserveExistingData: [REQUIRED]\nSpecify this field as true if you want to preserve the data on the local disk. Otherwise, specifying this field as false creates an empty volume.\nValid Values: true, false\n

    :type TargetName: string
    :param TargetName: [REQUIRED]\nThe name of the iSCSI target used by an initiator to connect to a volume and used as a suffix for the target ARN. For example, specifying TargetName as myvolume results in the target ARN of arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/target/iqn.1997-05.com.amazon:myvolume . The target name must be unique across all volumes on a gateway.\nIf you don\'t specify a value, Storage Gateway uses the value that was previously used for this volume as the new target name.\n

    :type NetworkInterfaceId: string
    :param NetworkInterfaceId: [REQUIRED]\nThe network interface of the gateway on which to expose the iSCSI target. Only IPv4 addresses are accepted. Use DescribeGatewayInformation to get a list of the network interfaces available on a gateway.\nValid Values: A valid IP address.\n

    :type KMSEncrypted: boolean
    :param KMSEncrypted: True to use Amazon S3 server-side encryption with your own AWS KMS key, or false to use a key managed by Amazon S3. Optional.

    :type KMSKey: string
    :param KMSKey: The Amazon Resource Name (ARN) of the KMS key used for Amazon S3 server-side encryption. This value can only be set when KMSEncrypted is true. Optional.

    :type Tags: list
    :param Tags: A list of up to 50 tags that can be assigned to a stored volume. Each tag is a key-value pair.\n\nNote\nValid characters for key and value are letters, spaces, and numbers representable in UTF-8 format, and the following special characters: + - = . _ : / @. The maximum length of a tag\'s key is 128 characters, and the maximum length for a tag\'s value is 256.\n\n\n(dict) --A key-value pair that helps you manage, filter, and search for your resource. Allowed characters: letters, white space, and numbers, representable in UTF-8, and the following characters: + - = . _ : /\n\nKey (string) -- [REQUIRED]Tag key (String). The key can\'t start with aws:.\n\nValue (string) -- [REQUIRED]Value of the tag key.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'VolumeARN': 'string',
    'VolumeSizeInBytes': 123,
    'TargetARN': 'string'
}


Response Structure

(dict) --
A JSON object containing the following fields:

VolumeARN (string) --
The Amazon Resource Name (ARN) of the configured volume.

VolumeSizeInBytes (integer) --
The size of the volume in bytes.

TargetARN (string) --
The Amazon Resource Name (ARN) of the volume target, which includes the iSCSI name that initiators can use to connect to the target.







Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError

Examples
Creates a stored volume on a specified stored gateway.
response = client.create_stored_iscsi_volume(
    DiskId='pci-0000:03:00.0-scsi-0:0:0:0',
    GatewayARN='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B',
    NetworkInterfaceId='10.1.1.1',
    PreserveExistingData=True,
    SnapshotId='snap-f47b7b94',
    TargetName='my-volume',
)

print(response)


Expected Output:
{
    'TargetARN': 'arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B/target/iqn.1997-05.com.amazon:myvolume',
    'VolumeARN': 'arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B/volume/vol-1122AABB',
    'VolumeSizeInBytes': 1099511627776,
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'VolumeARN': 'string',
        'VolumeSizeInBytes': 123,
        'TargetARN': 'string'
    }
    
    
    :returns: 
    StorageGateway.Client.exceptions.InvalidGatewayRequestException
    StorageGateway.Client.exceptions.InternalServerError
    
    """
    pass

def create_tape_with_barcode(GatewayARN=None, TapeSizeInBytes=None, TapeBarcode=None, KMSEncrypted=None, KMSKey=None, PoolId=None, Tags=None):
    """
    Creates a virtual tape by using your own barcode. You write data to the virtual tape and then archive the tape. A barcode is unique and cannot be reused if it has already been used on a tape. This applies to barcodes used on deleted tapes. This operation is only supported in the tape gateway type.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Creates a virtual tape by using your own barcode.
    Expected Output:
    
    :example: response = client.create_tape_with_barcode(
        GatewayARN='string',
        TapeSizeInBytes=123,
        TapeBarcode='string',
        KMSEncrypted=True|False,
        KMSKey='string',
        PoolId='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]\nThe unique Amazon Resource Name (ARN) that represents the gateway to associate the virtual tape with. Use the ListGateways operation to return a list of gateways for your account and AWS Region.\n

    :type TapeSizeInBytes: integer
    :param TapeSizeInBytes: [REQUIRED]\nThe size, in bytes, of the virtual tape that you want to create.\n\nNote\nThe size must be aligned by gigabyte (1024*1024*1024 bytes).\n\n

    :type TapeBarcode: string
    :param TapeBarcode: [REQUIRED]\nThe barcode that you want to assign to the tape.\n\nNote\nBarcodes cannot be reused. This includes barcodes used for tapes that have been deleted.\n\n

    :type KMSEncrypted: boolean
    :param KMSEncrypted: True to use Amazon S3 server-side encryption with your own AWS KMS key, or false to use a key managed by Amazon S3. Optional.

    :type KMSKey: string
    :param KMSKey: The Amazon Resource Name (ARN) of the AWS KMS key used for Amazon S3 server-side encryption. This value can only be set when KMSEncrypted is true. Optional.

    :type PoolId: string
    :param PoolId: The ID of the pool that you want to add your tape to for archiving. The tape in this pool is archived in the S3 storage class that is associated with the pool. When you use your backup application to eject the tape, the tape is archived directly into the storage class (S3 Glacier or S3 Glacier Deep Archive) that corresponds to the pool.\nValid values: 'GLACIER', 'DEEP_ARCHIVE'\n

    :type Tags: list
    :param Tags: A list of up to 50 tags that can be assigned to a virtual tape that has a barcode. Each tag is a key-value pair.\n\nNote\nValid characters for key and value are letters, spaces, and numbers representable in UTF-8 format, and the following special characters: + - = . _ : / @. The maximum length of a tag\'s key is 128 characters, and the maximum length for a tag\'s value is 256.\n\n\n(dict) --A key-value pair that helps you manage, filter, and search for your resource. Allowed characters: letters, white space, and numbers, representable in UTF-8, and the following characters: + - = . _ : /\n\nKey (string) -- [REQUIRED]Tag key (String). The key can\'t start with aws:.\n\nValue (string) -- [REQUIRED]Value of the tag key.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'TapeARN': 'string'
}


Response Structure

(dict) --
CreateTapeOutput

TapeARN (string) --
A unique Amazon Resource Name (ARN) that represents the virtual tape that was created.







Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError

Examples
Creates a virtual tape by using your own barcode.
response = client.create_tape_with_barcode(
    GatewayARN='arn:aws:storagegateway:us-east-1:999999999999:gateway/sgw-12A3456B',
    TapeBarcode='TEST12345',
    TapeSizeInBytes=107374182400,
)

print(response)


Expected Output:
{
    'TapeARN': 'arn:aws:storagegateway:us-east-1:999999999999:tape/TEST12345',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'TapeARN': 'string'
    }
    
    
    :returns: 
    StorageGateway.Client.exceptions.InvalidGatewayRequestException
    StorageGateway.Client.exceptions.InternalServerError
    
    """
    pass

def create_tapes(GatewayARN=None, TapeSizeInBytes=None, ClientToken=None, NumTapesToCreate=None, TapeBarcodePrefix=None, KMSEncrypted=None, KMSKey=None, PoolId=None, Tags=None):
    """
    Creates one or more virtual tapes. You write data to the virtual tapes and then archive the tapes. This operation is only supported in the tape gateway type.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Creates one or more virtual tapes.
    Expected Output:
    
    :example: response = client.create_tapes(
        GatewayARN='string',
        TapeSizeInBytes=123,
        ClientToken='string',
        NumTapesToCreate=123,
        TapeBarcodePrefix='string',
        KMSEncrypted=True|False,
        KMSKey='string',
        PoolId='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]\nThe unique Amazon Resource Name (ARN) that represents the gateway to associate the virtual tapes with. Use the ListGateways operation to return a list of gateways for your account and AWS Region.\n

    :type TapeSizeInBytes: integer
    :param TapeSizeInBytes: [REQUIRED]\nThe size, in bytes, of the virtual tapes that you want to create.\n\nNote\nThe size must be aligned by gigabyte (1024*1024*1024 bytes).\n\n

    :type ClientToken: string
    :param ClientToken: [REQUIRED]\nA unique identifier that you use to retry a request. If you retry a request, use the same ClientToken you specified in the initial request.\n\nNote\nUsing the same ClientToken prevents creating the tape multiple times.\n\n

    :type NumTapesToCreate: integer
    :param NumTapesToCreate: [REQUIRED]\nThe number of virtual tapes that you want to create.\n

    :type TapeBarcodePrefix: string
    :param TapeBarcodePrefix: [REQUIRED]\nA prefix that you append to the barcode of the virtual tape you are creating. This prefix makes the barcode unique.\n\nNote\nThe prefix must be 1 to 4 characters in length and must be one of the uppercase letters from A to Z.\n\n

    :type KMSEncrypted: boolean
    :param KMSEncrypted: True to use Amazon S3 server-side encryption with your own AWS KMS key, or false to use a key managed by Amazon S3. Optional.

    :type KMSKey: string
    :param KMSKey: The Amazon Resource Name (ARN) of the AWS KMS key used for Amazon S3 server-side encryption. This value can only be set when KMSEncrypted is true. Optional.

    :type PoolId: string
    :param PoolId: The ID of the pool that you want to add your tape to for archiving. The tape in this pool is archived in the S3 storage class that is associated with the pool. When you use your backup application to eject the tape, the tape is archived directly into the storage class (S3 Glacier or S3 Glacier Deep Archive) that corresponds to the pool.\nValid values: 'GLACIER', 'DEEP_ARCHIVE'\n

    :type Tags: list
    :param Tags: A list of up to 50 tags that can be assigned to a virtual tape. Each tag is a key-value pair.\n\nNote\nValid characters for key and value are letters, spaces, and numbers representable in UTF-8 format, and the following special characters: + - = . _ : / @. The maximum length of a tag\'s key is 128 characters, and the maximum length for a tag\'s value is 256.\n\n\n(dict) --A key-value pair that helps you manage, filter, and search for your resource. Allowed characters: letters, white space, and numbers, representable in UTF-8, and the following characters: + - = . _ : /\n\nKey (string) -- [REQUIRED]Tag key (String). The key can\'t start with aws:.\n\nValue (string) -- [REQUIRED]Value of the tag key.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'TapeARNs': [
        'string',
    ]
}


Response Structure

(dict) --
CreateTapeOutput

TapeARNs (list) --
A list of unique Amazon Resource Names (ARNs) that represents the virtual tapes that were created.

(string) --








Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError

Examples
Creates one or more virtual tapes.
response = client.create_tapes(
    ClientToken='77777',
    GatewayARN='arn:aws:storagegateway:us-east-1:999999999999:gateway/sgw-12A3456B',
    NumTapesToCreate=3,
    TapeBarcodePrefix='TEST',
    TapeSizeInBytes=107374182400,
)

print(response)


Expected Output:
{
    'TapeARNs': [
        'arn:aws:storagegateway:us-east-1:999999999999:tape/TEST38A29D',
        'arn:aws:storagegateway:us-east-1:204469490176:tape/TEST3AA29F',
        'arn:aws:storagegateway:us-east-1:204469490176:tape/TEST3BA29E',
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'TapeARNs': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def delete_automatic_tape_creation_policy(GatewayARN=None):
    """
    Deletes the automatic tape creation policy of a gateway. If you delete this policy, new virtual tapes must be created manually. Use the Amazon Resource Name (ARN) of the gateway in your request to remove the policy.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_automatic_tape_creation_policy(
        GatewayARN='string'
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and AWS Region.\n

    :rtype: dict
ReturnsResponse Syntax{
    'GatewayARN': 'string'
}


Response Structure

(dict) --
GatewayARN (string) --The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and AWS Region.






Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError


    :return: {
        'GatewayARN': 'string'
    }
    
    
    """
    pass

def delete_bandwidth_rate_limit(GatewayARN=None, BandwidthType=None):
    """
    Deletes the bandwidth rate limits of a gateway. You can delete either the upload and download bandwidth rate limit, or you can delete both. If you delete only one of the limits, the other limit remains unchanged. To specify which gateway to work with, use the Amazon Resource Name (ARN) of the gateway in your request. This operation is supported for the stored volume, cached volume and tape gateway types.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Deletes the bandwidth rate limits of a gateway; either the upload or download limit, or both.
    Expected Output:
    
    :example: response = client.delete_bandwidth_rate_limit(
        GatewayARN='string',
        BandwidthType='string'
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and AWS Region.\n

    :type BandwidthType: string
    :param BandwidthType: [REQUIRED]\nOne of the BandwidthType values that indicates the gateway bandwidth rate limit to delete.\nValid Values: Upload , Download , All .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'GatewayARN': 'string'
}


Response Structure

(dict) --
A JSON object containing the Amazon Resource Name (ARN) of the gateway whose bandwidth rate information was deleted.

GatewayARN (string) --
The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and AWS Region.







Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError

Examples
Deletes the bandwidth rate limits of a gateway; either the upload or download limit, or both.
response = client.delete_bandwidth_rate_limit(
    BandwidthType='All',
    GatewayARN='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B',
)

print(response)


Expected Output:
{
    'GatewayARN': 'arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'GatewayARN': 'string'
    }
    
    
    :returns: 
    StorageGateway.Client.exceptions.InvalidGatewayRequestException
    StorageGateway.Client.exceptions.InternalServerError
    
    """
    pass

def delete_chap_credentials(TargetARN=None, InitiatorName=None):
    """
    Deletes Challenge-Handshake Authentication Protocol (CHAP) credentials for a specified iSCSI target and initiator pair. This operation is supported in volume and tape gateway types.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Deletes Challenge-Handshake Authentication Protocol (CHAP) credentials for a specified iSCSI target and initiator pair.
    Expected Output:
    
    :example: response = client.delete_chap_credentials(
        TargetARN='string',
        InitiatorName='string'
    )
    
    
    :type TargetARN: string
    :param TargetARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the iSCSI volume target. Use the DescribeStorediSCSIVolumes operation to return to retrieve the TargetARN for specified VolumeARN.\n

    :type InitiatorName: string
    :param InitiatorName: [REQUIRED]\nThe iSCSI initiator that connects to the target.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'TargetARN': 'string',
    'InitiatorName': 'string'
}


Response Structure

(dict) --
A JSON object containing the following fields:

TargetARN (string) --
The Amazon Resource Name (ARN) of the target.

InitiatorName (string) --
The iSCSI initiator that connects to the target.







Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError

Examples
Deletes Challenge-Handshake Authentication Protocol (CHAP) credentials for a specified iSCSI target and initiator pair.
response = client.delete_chap_credentials(
    InitiatorName='iqn.1991-05.com.microsoft:computername.domain.example.com',
    TargetARN='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B/target/iqn.1997-05.com.amazon:myvolume',
)

print(response)


Expected Output:
{
    'InitiatorName': 'iqn.1991-05.com.microsoft:computername.domain.example.com',
    'TargetARN': 'arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B/target/iqn.1997-05.com.amazon:myvolume',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'TargetARN': 'string',
        'InitiatorName': 'string'
    }
    
    
    :returns: 
    StorageGateway.Client.exceptions.InvalidGatewayRequestException
    StorageGateway.Client.exceptions.InternalServerError
    
    """
    pass

def delete_file_share(FileShareARN=None, ForceDelete=None):
    """
    Deletes a file share from a file gateway. This operation is only supported for file gateways.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_file_share(
        FileShareARN='string',
        ForceDelete=True|False
    )
    
    
    :type FileShareARN: string
    :param FileShareARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the file share to be deleted.\n

    :type ForceDelete: boolean
    :param ForceDelete: If this value is set to true, the operation deletes a file share immediately and aborts all data uploads to AWS. Otherwise, the file share is not deleted until all data is uploaded to AWS. This process aborts the data upload process, and the file share enters the FORCE_DELETING status.

    :rtype: dict

ReturnsResponse Syntax
{
    'FileShareARN': 'string'
}


Response Structure

(dict) --
DeleteFileShareOutput

FileShareARN (string) --
The Amazon Resource Name (ARN) of the deleted file share.







Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError


    :return: {
        'FileShareARN': 'string'
    }
    
    
    :returns: 
    StorageGateway.Client.exceptions.InvalidGatewayRequestException
    StorageGateway.Client.exceptions.InternalServerError
    
    """
    pass

def delete_gateway(GatewayARN=None):
    """
    Deletes a gateway. To specify which gateway to delete, use the Amazon Resource Name (ARN) of the gateway in your request. The operation deletes the gateway; however, it does not delete the gateway virtual machine (VM) from your host computer.
    After you delete a gateway, you cannot reactivate it. Completed snapshots of the gateway volumes are not deleted upon deleting the gateway, however, pending snapshots will not complete. After you delete a gateway, your next step is to remove it from your environment.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This operation deletes the gateway, but not the gateway\'s VM from the host computer.
    Expected Output:
    
    :example: response = client.delete_gateway(
        GatewayARN='string'
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and AWS Region.\n

    :rtype: dict
ReturnsResponse Syntax{
    'GatewayARN': 'string'
}


Response Structure

(dict) --A JSON object containing the ID of the deleted gateway.

GatewayARN (string) --The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and AWS Region.






Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError

Examples
This operation deletes the gateway, but not the gateway\'s VM from the host computer.
response = client.delete_gateway(
    GatewayARN='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B',
)

print(response)


Expected Output:
{
    'GatewayARN': 'arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'GatewayARN': 'string'
    }
    
    
    """
    pass

def delete_snapshot_schedule(VolumeARN=None):
    """
    Deletes a snapshot of a volume.
    You can take snapshots of your gateway volumes on a scheduled or ad hoc basis. This API action enables you to delete a snapshot schedule for a volume. For more information, see Working with Snapshots . In the DeleteSnapshotSchedule request, you identify the volume by providing its Amazon Resource Name (ARN). This operation is only supported in stored and cached volume gateway types.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This action enables you to delete a snapshot schedule for a volume.
    Expected Output:
    
    :example: response = client.delete_snapshot_schedule(
        VolumeARN='string'
    )
    
    
    :type VolumeARN: string
    :param VolumeARN: [REQUIRED]\nThe volume which snapshot schedule to delete.\n

    :rtype: dict
ReturnsResponse Syntax{
    'VolumeARN': 'string'
}


Response Structure

(dict) --
VolumeARN (string) --The volume which snapshot schedule was deleted.






Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError

Examples
This action enables you to delete a snapshot schedule for a volume.
response = client.delete_snapshot_schedule(
    VolumeARN='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B/volume/vol-1122AABB',
)

print(response)


Expected Output:
{
    'VolumeARN': 'arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B/volume/vol-1122AABB',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'VolumeARN': 'string'
    }
    
    
    """
    pass

def delete_tape(GatewayARN=None, TapeARN=None):
    """
    Deletes the specified virtual tape. This operation is only supported in the tape gateway type.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This example deletes the specified virtual tape.
    Expected Output:
    
    :example: response = client.delete_tape(
        GatewayARN='string',
        TapeARN='string'
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]\nThe unique Amazon Resource Name (ARN) of the gateway that the virtual tape to delete is associated with. Use the ListGateways operation to return a list of gateways for your account and AWS Region.\n

    :type TapeARN: string
    :param TapeARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the virtual tape to delete.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'TapeARN': 'string'
}


Response Structure

(dict) --
DeleteTapeOutput

TapeARN (string) --
The Amazon Resource Name (ARN) of the deleted virtual tape.







Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError

Examples
This example deletes the specified virtual tape.
response = client.delete_tape(
    GatewayARN='arn:aws:storagegateway:us-east-1:204469490176:gateway/sgw-12A3456B',
    TapeARN='arn:aws:storagegateway:us-east-1:204469490176:tape/TEST05A2A0',
)

print(response)


Expected Output:
{
    'TapeARN': 'arn:aws:storagegateway:us-east-1:204469490176:tape/TEST05A2A0',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'TapeARN': 'string'
    }
    
    
    :returns: 
    StorageGateway.Client.exceptions.InvalidGatewayRequestException
    StorageGateway.Client.exceptions.InternalServerError
    
    """
    pass

def delete_tape_archive(TapeARN=None):
    """
    Deletes the specified virtual tape from the virtual tape shelf (VTS). This operation is only supported in the tape gateway type.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Deletes the specified virtual tape from the virtual tape shelf (VTS).
    Expected Output:
    
    :example: response = client.delete_tape_archive(
        TapeARN='string'
    )
    
    
    :type TapeARN: string
    :param TapeARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the virtual tape to delete from the virtual tape shelf (VTS).\n

    :rtype: dict
ReturnsResponse Syntax{
    'TapeARN': 'string'
}


Response Structure

(dict) --DeleteTapeArchiveOutput

TapeARN (string) --The Amazon Resource Name (ARN) of the virtual tape that was deleted from the virtual tape shelf (VTS).






Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError

Examples
Deletes the specified virtual tape from the virtual tape shelf (VTS).
response = client.delete_tape_archive(
    TapeARN='arn:aws:storagegateway:us-east-1:204469490176:tape/TEST05A2A0',
)

print(response)


Expected Output:
{
    'TapeARN': 'arn:aws:storagegateway:us-east-1:204469490176:tape/TEST05A2A0',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'TapeARN': 'string'
    }
    
    
    """
    pass

def delete_volume(VolumeARN=None):
    """
    Deletes the specified storage volume that you previously created using the  CreateCachediSCSIVolume or  CreateStorediSCSIVolume API. This operation is only supported in the cached volume and stored volume types. For stored volume gateways, the local disk that was configured as the storage volume is not deleted. You can reuse the local disk to create another storage volume.
    Before you delete a volume, make sure there are no iSCSI connections to the volume you are deleting. You should also make sure there is no snapshot in progress. You can use the Amazon Elastic Compute Cloud (Amazon EC2) API to query snapshots on the volume you are deleting and check the snapshot status. For more information, go to DescribeSnapshots in the Amazon Elastic Compute Cloud API Reference .
    In the request, you must provide the Amazon Resource Name (ARN) of the storage volume you want to delete.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Deletes the specified gateway volume that you previously created using the CreateCachediSCSIVolume or CreateStorediSCSIVolume API.
    Expected Output:
    
    :example: response = client.delete_volume(
        VolumeARN='string'
    )
    
    
    :type VolumeARN: string
    :param VolumeARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the volume. Use the ListVolumes operation to return a list of gateway volumes.\n

    :rtype: dict
ReturnsResponse Syntax{
    'VolumeARN': 'string'
}


Response Structure

(dict) --A JSON object containing the Amazon Resource Name (ARN) of the storage volume that was deleted

VolumeARN (string) --The Amazon Resource Name (ARN) of the storage volume that was deleted. It is the same ARN you provided in the request.






Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError

Examples
Deletes the specified gateway volume that you previously created using the CreateCachediSCSIVolume or CreateStorediSCSIVolume API.
response = client.delete_volume(
    VolumeARN='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B/volume/vol-1122AABB',
)

print(response)


Expected Output:
{
    'VolumeARN': 'arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B/volume/vol-1122AABB',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'VolumeARN': 'string'
    }
    
    
    """
    pass

def describe_availability_monitor_test(GatewayARN=None):
    """
    Returns information about the most recent High Availability monitoring test that was performed on the host in a cluster. If a test isn\'t performed, the status and start time in the response would be null.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_availability_monitor_test(
        GatewayARN='string'
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and AWS Region.\n

    :rtype: dict
ReturnsResponse Syntax{
    'GatewayARN': 'string',
    'Status': 'COMPLETE'|'FAILED'|'PENDING',
    'StartTime': datetime(2015, 1, 1)
}


Response Structure

(dict) --
GatewayARN (string) --The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and AWS Region.

Status (string) --The status of the High Availability monitoring test. If a test hasn\'t been performed, the value of this field is null.

StartTime (datetime) --The time the High Availability monitoring test was started. If a test hasn\'t been performed, the value of this field is null.






Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError


    :return: {
        'GatewayARN': 'string',
        'Status': 'COMPLETE'|'FAILED'|'PENDING',
        'StartTime': datetime(2015, 1, 1)
    }
    
    
    """
    pass

def describe_bandwidth_rate_limit(GatewayARN=None):
    """
    Returns the bandwidth rate limits of a gateway. By default, these limits are not set, which means no bandwidth rate limiting is in effect. This operation is supported for the stored volume, cached volume and tape gateway types.\'
    This operation only returns a value for a bandwidth rate limit only if the limit is set. If no limits are set for the gateway, then this operation returns only the gateway ARN in the response body. To specify which gateway to describe, use the Amazon Resource Name (ARN) of the gateway in your request.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Returns a value for a bandwidth rate limit if set. If not set, then only the gateway ARN is returned.
    Expected Output:
    
    :example: response = client.describe_bandwidth_rate_limit(
        GatewayARN='string'
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and AWS Region.\n

    :rtype: dict
ReturnsResponse Syntax{
    'GatewayARN': 'string',
    'AverageUploadRateLimitInBitsPerSec': 123,
    'AverageDownloadRateLimitInBitsPerSec': 123
}


Response Structure

(dict) --A JSON object containing the following fields:

GatewayARN (string) --The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and AWS Region.

AverageUploadRateLimitInBitsPerSec (integer) --The average upload bandwidth rate limit in bits per second. This field does not appear in the response if the upload rate limit is not set.

AverageDownloadRateLimitInBitsPerSec (integer) --The average download bandwidth rate limit in bits per second. This field does not appear in the response if the download rate limit is not set.






Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError

Examples
Returns a value for a bandwidth rate limit if set. If not set, then only the gateway ARN is returned.
response = client.describe_bandwidth_rate_limit(
    GatewayARN='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B',
)

print(response)


Expected Output:
{
    'AverageDownloadRateLimitInBitsPerSec': 204800,
    'AverageUploadRateLimitInBitsPerSec': 102400,
    'GatewayARN': 'arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'GatewayARN': 'string',
        'AverageUploadRateLimitInBitsPerSec': 123,
        'AverageDownloadRateLimitInBitsPerSec': 123
    }
    
    
    """
    pass

def describe_cache(GatewayARN=None):
    """
    Returns information about the cache of a gateway. This operation is only supported in the cached volume, tape, and file gateway types.
    The response includes disk IDs that are configured as cache, and it includes the amount of cache allocated and used.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Returns information about the cache of a gateway.
    Expected Output:
    
    :example: response = client.describe_cache(
        GatewayARN='string'
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and AWS Region.\n

    :rtype: dict
ReturnsResponse Syntax{
    'GatewayARN': 'string',
    'DiskIds': [
        'string',
    ],
    'CacheAllocatedInBytes': 123,
    'CacheUsedPercentage': 123.0,
    'CacheDirtyPercentage': 123.0,
    'CacheHitPercentage': 123.0,
    'CacheMissPercentage': 123.0
}


Response Structure

(dict) --
GatewayARN (string) --The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and AWS Region.

DiskIds (list) --An array of strings that identify disks that are to be configured as working storage. Each string has a minimum length of 1 and maximum length of 300. You can get the disk IDs from the  ListLocalDisks API.

(string) --


CacheAllocatedInBytes (integer) --The amount of cache in bytes allocated to a gateway.

CacheUsedPercentage (float) --Percent use of the gateway\'s cache storage. This metric applies only to the gateway-cached volume setup. The sample is taken at the end of the reporting period.

CacheDirtyPercentage (float) --The file share\'s contribution to the overall percentage of the gateway\'s cache that has not been persisted to AWS. The sample is taken at the end of the reporting period.

CacheHitPercentage (float) --Percent of application read operations from the file shares that are served from cache. The sample is taken at the end of the reporting period.

CacheMissPercentage (float) --Percent of application read operations from the file shares that are not served from cache. The sample is taken at the end of the reporting period.






Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError

Examples
Returns information about the cache of a gateway.
response = client.describe_cache(
    GatewayARN='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B',
)

print(response)


Expected Output:
{
    'CacheAllocatedInBytes': 2199023255552,
    'CacheDirtyPercentage': 0.07,
    'CacheHitPercentage': 99.68,
    'CacheMissPercentage': 0.32,
    'CacheUsedPercentage': 0.07,
    'DiskIds': [
        'pci-0000:03:00.0-scsi-0:0:0:0',
        'pci-0000:04:00.0-scsi-0:1:0:0',
    ],
    'GatewayARN': 'arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'GatewayARN': 'string',
        'DiskIds': [
            'string',
        ],
        'CacheAllocatedInBytes': 123,
        'CacheUsedPercentage': 123.0,
        'CacheDirtyPercentage': 123.0,
        'CacheHitPercentage': 123.0,
        'CacheMissPercentage': 123.0
    }
    
    
    :returns: 
    StorageGateway.Client.exceptions.InvalidGatewayRequestException
    StorageGateway.Client.exceptions.InternalServerError
    
    """
    pass

def describe_cached_iscsi_volumes(VolumeARNs=None):
    """
    Returns a description of the gateway volumes specified in the request. This operation is only supported in the cached volume gateway types.
    The list of gateway volumes in the request must be from one gateway. In the response, AWS Storage Gateway returns volume information sorted by volume Amazon Resource Name (ARN).
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Returns a description of the gateway cached iSCSI volumes specified in the request.
    Expected Output:
    
    :example: response = client.describe_cached_iscsi_volumes(
        VolumeARNs=[
            'string',
        ]
    )
    
    
    :type VolumeARNs: list
    :param VolumeARNs: [REQUIRED]\nAn array of strings where each string represents the Amazon Resource Name (ARN) of a cached volume. All of the specified cached volumes must be from the same gateway. Use ListVolumes to get volume ARNs for a gateway.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'CachediSCSIVolumes': [
        {
            'VolumeARN': 'string',
            'VolumeId': 'string',
            'VolumeType': 'string',
            'VolumeStatus': 'string',
            'VolumeAttachmentStatus': 'string',
            'VolumeSizeInBytes': 123,
            'VolumeProgress': 123.0,
            'SourceSnapshotId': 'string',
            'VolumeiSCSIAttributes': {
                'TargetARN': 'string',
                'NetworkInterfaceId': 'string',
                'NetworkInterfacePort': 123,
                'LunNumber': 123,
                'ChapEnabled': True|False
            },
            'CreatedDate': datetime(2015, 1, 1),
            'VolumeUsedInBytes': 123,
            'KMSKey': 'string',
            'TargetName': 'string'
        },
    ]
}


Response Structure

(dict) --A JSON object containing the following fields:

CachediSCSIVolumes (list) --An array of objects where each object contains metadata about one cached volume.

(dict) --Describes an iSCSI cached volume.

VolumeARN (string) --The Amazon Resource Name (ARN) of the storage volume.

VolumeId (string) --The unique identifier of the volume, e.g. vol-AE4B946D.

VolumeType (string) --One of the VolumeType enumeration values that describes the type of the volume.

VolumeStatus (string) --One of the VolumeStatus values that indicates the state of the storage volume.

VolumeAttachmentStatus (string) --A value that indicates whether a storage volume is attached to or detached from a gateway. For more information, see Moving Your Volumes to a Different Gateway .

VolumeSizeInBytes (integer) --The size, in bytes, of the volume capacity.

VolumeProgress (float) --Represents the percentage complete if the volume is restoring or bootstrapping that represents the percent of data transferred. This field does not appear in the response if the cached volume is not restoring or bootstrapping.

SourceSnapshotId (string) --If the cached volume was created from a snapshot, this field contains the snapshot ID used, e.g. snap-78e22663. Otherwise, this field is not included.

VolumeiSCSIAttributes (dict) --An  VolumeiSCSIAttributes object that represents a collection of iSCSI attributes for one stored volume.

TargetARN (string) --The Amazon Resource Name (ARN) of the volume target.

NetworkInterfaceId (string) --The network interface identifier.

NetworkInterfacePort (integer) --The port used to communicate with iSCSI targets.

LunNumber (integer) --The logical disk number.

ChapEnabled (boolean) --Indicates whether mutual CHAP is enabled for the iSCSI target.



CreatedDate (datetime) --The date the volume was created. Volumes created prior to March 28, 2017 don\xe2\x80\x99t have this time stamp.

VolumeUsedInBytes (integer) --The size of the data stored on the volume in bytes. This value is calculated based on the number of blocks that are touched, instead of the actual amount of data written. This value can be useful for sequential write patterns but less accurate for random write patterns. VolumeUsedInBytes is different from the compressed size of the volume, which is the value that is used to calculate your bill.

Note
This value is not available for volumes created prior to May 13, 2015, until you store data on the volume.


KMSKey (string) --The Amazon Resource Name (ARN) of the AWS KMS key used for Amazon S3 server-side encryption. This value can only be set when KMSEncrypted is true. Optional.

TargetName (string) --The name of the iSCSI target used by an initiator to connect to a volume and used as a suffix for the target ARN. For example, specifying TargetName as myvolume results in the target ARN of arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/target/iqn.1997-05.com.amazon:myvolume . The target name must be unique across all volumes on a gateway.
If you don\'t specify a value, Storage Gateway uses the value that was previously used for this volume as the new target name.










Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError

Examples
Returns a description of the gateway cached iSCSI volumes specified in the request.
response = client.describe_cached_iscsi_volumes(
    VolumeARNs=[
        'arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B/volume/vol-1122AABB',
    ],
)

print(response)


Expected Output:
{
    'CachediSCSIVolumes': [
        {
            'VolumeARN': 'arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B/volume/vol-1122AABB',
            'VolumeId': 'vol-1122AABB',
            'VolumeSizeInBytes': 1099511627776,
            'VolumeStatus': 'AVAILABLE',
            'VolumeType': 'CACHED iSCSI',
            'VolumeiSCSIAttributes': {
                'ChapEnabled': True,
                'LunNumber': 1,
                'NetworkInterfaceId': '10.243.43.207',
                'NetworkInterfacePort': 3260,
                'TargetARN': 'arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B/target/iqn.1997-05.com.amazon:myvolume',
            },
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'CachediSCSIVolumes': [
            {
                'VolumeARN': 'string',
                'VolumeId': 'string',
                'VolumeType': 'string',
                'VolumeStatus': 'string',
                'VolumeAttachmentStatus': 'string',
                'VolumeSizeInBytes': 123,
                'VolumeProgress': 123.0,
                'SourceSnapshotId': 'string',
                'VolumeiSCSIAttributes': {
                    'TargetARN': 'string',
                    'NetworkInterfaceId': 'string',
                    'NetworkInterfacePort': 123,
                    'LunNumber': 123,
                    'ChapEnabled': True|False
                },
                'CreatedDate': datetime(2015, 1, 1),
                'VolumeUsedInBytes': 123,
                'KMSKey': 'string',
                'TargetName': 'string'
            },
        ]
    }
    
    
    :returns: 
    StorageGateway.Client.exceptions.InvalidGatewayRequestException
    StorageGateway.Client.exceptions.InternalServerError
    
    """
    pass

def describe_chap_credentials(TargetARN=None):
    """
    Returns an array of Challenge-Handshake Authentication Protocol (CHAP) credentials information for a specified iSCSI target, one for each target-initiator pair. This operation is supported in the volume and tape gateway types.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Returns an array of Challenge-Handshake Authentication Protocol (CHAP) credentials information for a specified iSCSI target, one for each target-initiator pair.
    Expected Output:
    
    :example: response = client.describe_chap_credentials(
        TargetARN='string'
    )
    
    
    :type TargetARN: string
    :param TargetARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the iSCSI volume target. Use the DescribeStorediSCSIVolumes operation to return to retrieve the TargetARN for specified VolumeARN.\n

    :rtype: dict
ReturnsResponse Syntax{
    'ChapCredentials': [
        {
            'TargetARN': 'string',
            'SecretToAuthenticateInitiator': 'string',
            'InitiatorName': 'string',
            'SecretToAuthenticateTarget': 'string'
        },
    ]
}


Response Structure

(dict) --A JSON object containing a .

ChapCredentials (list) --An array of  ChapInfo objects that represent CHAP credentials. Each object in the array contains CHAP credential information for one target-initiator pair. If no CHAP credentials are set, an empty array is returned. CHAP credential information is provided in a JSON object with the following fields:

InitiatorName : The iSCSI initiator that connects to the target.
SecretToAuthenticateInitiator : The secret key that the initiator (for example, the Windows client) must provide to participate in mutual CHAP with the target.
SecretToAuthenticateTarget : The secret key that the target must provide to participate in mutual CHAP with the initiator (e.g. Windows client).
TargetARN : The Amazon Resource Name (ARN) of the storage volume.


(dict) --Describes Challenge-Handshake Authentication Protocol (CHAP) information that supports authentication between your gateway and iSCSI initiators.

TargetARN (string) --The Amazon Resource Name (ARN) of the volume.
Valid Values: 50 to 500 lowercase letters, numbers, periods (.), and hyphens (-).

SecretToAuthenticateInitiator (string) --The secret key that the initiator (for example, the Windows client) must provide to participate in mutual CHAP with the target.

InitiatorName (string) --The iSCSI initiator that connects to the target.

SecretToAuthenticateTarget (string) --The secret key that the target must provide to participate in mutual CHAP with the initiator (e.g. Windows client).










Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError

Examples
Returns an array of Challenge-Handshake Authentication Protocol (CHAP) credentials information for a specified iSCSI target, one for each target-initiator pair.
response = client.describe_chap_credentials(
    TargetARN='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B/target/iqn.1997-05.com.amazon:myvolume',
)

print(response)


Expected Output:
{
    'ChapCredentials': [
        {
            'InitiatorName': 'iqn.1991-05.com.microsoft:computername.domain.example.com',
            'SecretToAuthenticateInitiator': '111111111111',
            'SecretToAuthenticateTarget': '222222222222',
            'TargetARN': 'arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B/target/iqn.1997-05.com.amazon:myvolume',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ChapCredentials': [
            {
                'TargetARN': 'string',
                'SecretToAuthenticateInitiator': 'string',
                'InitiatorName': 'string',
                'SecretToAuthenticateTarget': 'string'
            },
        ]
    }
    
    
    :returns: 
    StorageGateway.Client.exceptions.InvalidGatewayRequestException
    StorageGateway.Client.exceptions.InternalServerError
    
    """
    pass

def describe_gateway_information(GatewayARN=None):
    """
    Returns metadata about a gateway such as its name, network interfaces, configured time zone, and the state (whether the gateway is running or not). To specify which gateway to describe, use the Amazon Resource Name (ARN) of the gateway in your request.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Returns metadata about a gateway such as its name, network interfaces, configured time zone, and the state (whether the gateway is running or not).
    Expected Output:
    
    :example: response = client.describe_gateway_information(
        GatewayARN='string'
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and AWS Region.\n

    :rtype: dict
ReturnsResponse Syntax{
    'GatewayARN': 'string',
    'GatewayId': 'string',
    'GatewayName': 'string',
    'GatewayTimezone': 'string',
    'GatewayState': 'string',
    'GatewayNetworkInterfaces': [
        {
            'Ipv4Address': 'string',
            'MacAddress': 'string',
            'Ipv6Address': 'string'
        },
    ],
    'GatewayType': 'string',
    'NextUpdateAvailabilityDate': 'string',
    'LastSoftwareUpdate': 'string',
    'Ec2InstanceId': 'string',
    'Ec2InstanceRegion': 'string',
    'Tags': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ],
    'VPCEndpoint': 'string',
    'CloudWatchLogGroupARN': 'string',
    'HostEnvironment': 'VMWARE'|'HYPER-V'|'EC2'|'KVM'|'OTHER'
}


Response Structure

(dict) --A JSON object containing the following fields:

GatewayARN (string) --The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and AWS Region.

GatewayId (string) --The unique identifier assigned to your gateway during activation. This ID becomes part of the gateway Amazon Resource Name (ARN), which you use as input for other operations.

GatewayName (string) --The name you configured for your gateway.

GatewayTimezone (string) --A value that indicates the time zone configured for the gateway.

GatewayState (string) --A value that indicates the operating state of the gateway.

GatewayNetworkInterfaces (list) --A  NetworkInterface array that contains descriptions of the gateway network interfaces.

(dict) --Describes a gateway\'s network interface.

Ipv4Address (string) --The Internet Protocol version 4 (IPv4) address of the interface.

MacAddress (string) --The Media Access Control (MAC) address of the interface.

Note
This is currently unsupported and will not be returned in output.


Ipv6Address (string) --The Internet Protocol version 6 (IPv6) address of the interface. Currently not supported .





GatewayType (string) --The type of the gateway.

NextUpdateAvailabilityDate (string) --The date on which an update to the gateway is available. This date is in the time zone of the gateway. If the gateway is not available for an update this field is not returned in the response.

LastSoftwareUpdate (string) --The date on which the last software update was applied to the gateway. If the gateway has never been updated, this field does not return a value in the response.

Ec2InstanceId (string) --The ID of the Amazon EC2 instance that was used to launch the gateway.

Ec2InstanceRegion (string) --The AWS Region where the Amazon EC2 instance is located.

Tags (list) --A list of up to 50 tags assigned to the gateway, sorted alphabetically by key name. Each tag is a key-value pair. For a gateway with more than 10 tags assigned, you can view all tags using the ListTagsForResource API operation.

(dict) --A key-value pair that helps you manage, filter, and search for your resource. Allowed characters: letters, white space, and numbers, representable in UTF-8, and the following characters: + - = . _ : /

Key (string) --Tag key (String). The key can\'t start with aws:.

Value (string) --Value of the tag key.





VPCEndpoint (string) --The configuration settings for the virtual private cloud (VPC) endpoint for your gateway.

CloudWatchLogGroupARN (string) --The Amazon Resource Name (ARN) of the Amazon CloudWatch Log Group that is used to monitor events in the gateway.

HostEnvironment (string) --The type of hypervisor environment used by the host.






Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError

Examples
Returns metadata about a gateway such as its name, network interfaces, configured time zone, and the state (whether the gateway is running or not).
response = client.describe_gateway_information(
    GatewayARN='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B',
)

print(response)


Expected Output:
{
    'GatewayARN': 'arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B',
    'GatewayId': 'sgw-AABB1122',
    'GatewayName': 'My_Gateway',
    'GatewayNetworkInterfaces': [
        {
            'Ipv4Address': '10.35.69.216',
        },
    ],
    'GatewayState': 'STATE_RUNNING',
    'GatewayTimezone': 'GMT-8:00',
    'GatewayType': 'STORED',
    'LastSoftwareUpdate': '2016-01-02T16:00:00',
    'NextUpdateAvailabilityDate': '2017-01-02T16:00:00',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'GatewayARN': 'string',
        'GatewayId': 'string',
        'GatewayName': 'string',
        'GatewayTimezone': 'string',
        'GatewayState': 'string',
        'GatewayNetworkInterfaces': [
            {
                'Ipv4Address': 'string',
                'MacAddress': 'string',
                'Ipv6Address': 'string'
            },
        ],
        'GatewayType': 'string',
        'NextUpdateAvailabilityDate': 'string',
        'LastSoftwareUpdate': 'string',
        'Ec2InstanceId': 'string',
        'Ec2InstanceRegion': 'string',
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        'VPCEndpoint': 'string',
        'CloudWatchLogGroupARN': 'string',
        'HostEnvironment': 'VMWARE'|'HYPER-V'|'EC2'|'KVM'|'OTHER'
    }
    
    
    """
    pass

def describe_maintenance_start_time(GatewayARN=None):
    """
    Returns your gateway\'s weekly maintenance start time including the day and time of the week. Note that values are in terms of the gateway\'s time zone.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Returns your gateway\'s weekly maintenance start time including the day and time of the week.
    Expected Output:
    
    :example: response = client.describe_maintenance_start_time(
        GatewayARN='string'
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and AWS Region.\n

    :rtype: dict
ReturnsResponse Syntax{
    'GatewayARN': 'string',
    'HourOfDay': 123,
    'MinuteOfHour': 123,
    'DayOfWeek': 123,
    'DayOfMonth': 123,
    'Timezone': 'string'
}


Response Structure

(dict) --A JSON object containing the following fields:

DescribeMaintenanceStartTimeOutput$DayOfMonth
DescribeMaintenanceStartTimeOutput$DayOfWeek
DescribeMaintenanceStartTimeOutput$HourOfDay
DescribeMaintenanceStartTimeOutput$MinuteOfHour
DescribeMaintenanceStartTimeOutput$Timezone


GatewayARN (string) --The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and AWS Region.

HourOfDay (integer) --The hour component of the maintenance start time represented as hh , where hh is the hour (0 to 23). The hour of the day is in the time zone of the gateway.

MinuteOfHour (integer) --The minute component of the maintenance start time represented as mm , where mm is the minute (0 to 59). The minute of the hour is in the time zone of the gateway.

DayOfWeek (integer) --An ordinal number between 0 and 6 that represents the day of the week, where 0 represents Sunday and 6 represents Saturday. The day of week is in the time zone of the gateway.

DayOfMonth (integer) --The day of the month component of the maintenance start time represented as an ordinal number from 1 to 28, where 1 represents the first day of the month and 28 represents the last day of the month.

Note
This value is only available for tape and volume gateways.


Timezone (string) --A value that indicates the time zone that is set for the gateway. The start time and day of week specified should be in the time zone of the gateway.






Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError

Examples
Returns your gateway\'s weekly maintenance start time including the day and time of the week.
response = client.describe_maintenance_start_time(
    GatewayARN='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B',
)

print(response)


Expected Output:
{
    'DayOfWeek': 2,
    'GatewayARN': 'arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B',
    'HourOfDay': 15,
    'MinuteOfHour': 35,
    'Timezone': 'GMT+7:00',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'GatewayARN': 'string',
        'HourOfDay': 123,
        'MinuteOfHour': 123,
        'DayOfWeek': 123,
        'DayOfMonth': 123,
        'Timezone': 'string'
    }
    
    
    :returns: 
    StorageGateway.Client.exceptions.InvalidGatewayRequestException
    StorageGateway.Client.exceptions.InternalServerError
    
    """
    pass

def describe_nfs_file_shares(FileShareARNList=None):
    """
    Gets a description for one or more Network File System (NFS) file shares from a file gateway. This operation is only supported for file gateways.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_nfs_file_shares(
        FileShareARNList=[
            'string',
        ]
    )
    
    
    :type FileShareARNList: list
    :param FileShareARNList: [REQUIRED]\nAn array containing the Amazon Resource Name (ARN) of each file share to be described.\n\n(string) --The Amazon Resource Name (ARN) of the file share.\n\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'NFSFileShareInfoList': [
        {
            'NFSFileShareDefaults': {
                'FileMode': 'string',
                'DirectoryMode': 'string',
                'GroupId': 123,
                'OwnerId': 123
            },
            'FileShareARN': 'string',
            'FileShareId': 'string',
            'FileShareStatus': 'string',
            'GatewayARN': 'string',
            'KMSEncrypted': True|False,
            'KMSKey': 'string',
            'Path': 'string',
            'Role': 'string',
            'LocationARN': 'string',
            'DefaultStorageClass': 'string',
            'ObjectACL': 'private'|'public-read'|'public-read-write'|'authenticated-read'|'bucket-owner-read'|'bucket-owner-full-control'|'aws-exec-read',
            'ClientList': [
                'string',
            ],
            'Squash': 'string',
            'ReadOnly': True|False,
            'GuessMIMETypeEnabled': True|False,
            'RequesterPays': True|False,
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        },
    ]
}


Response Structure

(dict) --DescribeNFSFileSharesOutput

NFSFileShareInfoList (list) --An array containing a description for each requested file share.

(dict) --The Unix file permissions and ownership information assigned, by default, to native S3 objects when file gateway discovers them in S3 buckets. This operation is only supported in file gateways.

NFSFileShareDefaults (dict) --Describes Network File System (NFS) file share default values. Files and folders stored as Amazon S3 objects in S3 buckets don\'t, by default, have Unix file permissions assigned to them. Upon discovery in an S3 bucket by Storage Gateway, the S3 objects that represent files and folders are assigned these default Unix permissions. This operation is only supported for file gateways.

FileMode (string) --The Unix file mode in the form "nnnn". For example, "0666" represents the default file mode inside the file share. The default value is 0666.

DirectoryMode (string) --The Unix directory mode in the form "nnnn". For example, "0666" represents the default access mode for all directories inside the file share. The default value is 0777.

GroupId (integer) --The default group ID for the file share (unless the files have another group ID specified). The default value is nfsnobody.

OwnerId (integer) --The default owner ID for files in the file share (unless the files have another owner ID specified). The default value is nfsnobody.



FileShareARN (string) --The Amazon Resource Name (ARN) of the file share.

FileShareId (string) --The ID of the file share.

FileShareStatus (string) --The status of the file share. Possible values are CREATING , UPDATING , AVAILABLE and DELETING .

GatewayARN (string) --The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and AWS Region.

KMSEncrypted (boolean) --True to use Amazon S3 server-side encryption with your own AWS KMS key, or false to use a key managed by Amazon S3. Optional.

KMSKey (string) --The Amazon Resource Name (ARN) of the AWS KMS key used for Amazon S3 server-side encryption. This value can only be set when KMSEncrypted is true. Optional.

Path (string) --The file share path used by the NFS client to identify the mount point.

Role (string) --The ARN of the IAM role that file gateway assumes when it accesses the underlying storage.

LocationARN (string) --The ARN of the backend storage used for storing file data.

DefaultStorageClass (string) --The default storage class for objects put into an Amazon S3 bucket by the file gateway. Possible values are S3_STANDARD , S3_STANDARD_IA , or S3_ONEZONE_IA . If this field is not populated, the default value S3_STANDARD is used. Optional.

ObjectACL (string) --A value that sets the access control list permission for objects in the S3 bucket that a file gateway puts objects into. The default value is "private".

ClientList (list) --The list of clients that are allowed to access the file gateway. The list must contain either valid IP addresses or valid CIDR blocks.

(string) --


Squash (string) --The user mapped to anonymous user. Valid options are the following:

RootSquash - Only root is mapped to anonymous user.
NoSquash - No one is mapped to anonymous user
AllSquash - Everyone is mapped to anonymous user.


ReadOnly (boolean) --A value that sets the write status of a file share. This value is true if the write status is read-only, and otherwise false.

GuessMIMETypeEnabled (boolean) --A value that enables guessing of the MIME type for uploaded objects based on file extensions. Set this value to true to enable MIME type guessing, and otherwise to false. The default value is true.

RequesterPays (boolean) --A value that sets who pays the cost of the request and the cost associated with data download from the S3 bucket. If this value is set to true, the requester pays the costs. Otherwise the S3 bucket owner pays. However, the S3 bucket owner always pays the cost of storing data.

Note
RequesterPays is a configuration for the S3 bucket that backs the file share, so make sure that the configuration on the file share is the same as the S3 bucket configuration.


Tags (list) --A list of up to 50 tags assigned to the NFS file share, sorted alphabetically by key name. Each tag is a key-value pair. For a gateway with more than 10 tags assigned, you can view all tags using the ListTagsForResource API operation.

(dict) --A key-value pair that helps you manage, filter, and search for your resource. Allowed characters: letters, white space, and numbers, representable in UTF-8, and the following characters: + - = . _ : /

Key (string) --Tag key (String). The key can\'t start with aws:.

Value (string) --Value of the tag key.














Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError


    :return: {
        'NFSFileShareInfoList': [
            {
                'NFSFileShareDefaults': {
                    'FileMode': 'string',
                    'DirectoryMode': 'string',
                    'GroupId': 123,
                    'OwnerId': 123
                },
                'FileShareARN': 'string',
                'FileShareId': 'string',
                'FileShareStatus': 'string',
                'GatewayARN': 'string',
                'KMSEncrypted': True|False,
                'KMSKey': 'string',
                'Path': 'string',
                'Role': 'string',
                'LocationARN': 'string',
                'DefaultStorageClass': 'string',
                'ObjectACL': 'private'|'public-read'|'public-read-write'|'authenticated-read'|'bucket-owner-read'|'bucket-owner-full-control'|'aws-exec-read',
                'ClientList': [
                    'string',
                ],
                'Squash': 'string',
                'ReadOnly': True|False,
                'GuessMIMETypeEnabled': True|False,
                'RequesterPays': True|False,
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            },
        ]
    }
    
    
    :returns: 
    RootSquash - Only root is mapped to anonymous user.
    NoSquash - No one is mapped to anonymous user
    AllSquash - Everyone is mapped to anonymous user.
    
    """
    pass

def describe_smb_file_shares(FileShareARNList=None):
    """
    Gets a description for one or more Server Message Block (SMB) file shares from a file gateway. This operation is only supported for file gateways.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_smb_file_shares(
        FileShareARNList=[
            'string',
        ]
    )
    
    
    :type FileShareARNList: list
    :param FileShareARNList: [REQUIRED]\nAn array containing the Amazon Resource Name (ARN) of each file share to be described.\n\n(string) --The Amazon Resource Name (ARN) of the file share.\n\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'SMBFileShareInfoList': [
        {
            'FileShareARN': 'string',
            'FileShareId': 'string',
            'FileShareStatus': 'string',
            'GatewayARN': 'string',
            'KMSEncrypted': True|False,
            'KMSKey': 'string',
            'Path': 'string',
            'Role': 'string',
            'LocationARN': 'string',
            'DefaultStorageClass': 'string',
            'ObjectACL': 'private'|'public-read'|'public-read-write'|'authenticated-read'|'bucket-owner-read'|'bucket-owner-full-control'|'aws-exec-read',
            'ReadOnly': True|False,
            'GuessMIMETypeEnabled': True|False,
            'RequesterPays': True|False,
            'SMBACLEnabled': True|False,
            'AdminUserList': [
                'string',
            ],
            'ValidUserList': [
                'string',
            ],
            'InvalidUserList': [
                'string',
            ],
            'AuditDestinationARN': 'string',
            'Authentication': 'string',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        },
    ]
}


Response Structure

(dict) --DescribeSMBFileSharesOutput

SMBFileShareInfoList (list) --An array containing a description for each requested file share.

(dict) --The Windows file permissions and ownership information assigned, by default, to native S3 objects when file gateway discovers them in S3 buckets. This operation is only supported for file gateways.

FileShareARN (string) --The Amazon Resource Name (ARN) of the file share.

FileShareId (string) --The ID of the file share.

FileShareStatus (string) --The status of the file share. Possible values are CREATING , UPDATING , AVAILABLE and DELETING .

GatewayARN (string) --The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and AWS Region.

KMSEncrypted (boolean) --True to use Amazon S3 server-side encryption with your own AWS KMS key, or false to use a key managed by Amazon S3. Optional.

KMSKey (string) --The Amazon Resource Name (ARN) of the AWS KMS key used for Amazon S3 server-side encryption. This value can only be set when KMSEncrypted is true. Optional.

Path (string) --The file share path used by the SMB client to identify the mount point.

Role (string) --The ARN of the IAM role that file gateway assumes when it accesses the underlying storage.

LocationARN (string) --The ARN of the backend storage used for storing file data.

DefaultStorageClass (string) --The default storage class for objects put into an Amazon S3 bucket by the file gateway. Possible values are S3_STANDARD , S3_STANDARD_IA , or S3_ONEZONE_IA . If this field is not populated, the default value S3_STANDARD is used. Optional.

ObjectACL (string) --A value that sets the access control list permission for objects in the S3 bucket that a file gateway puts objects into. The default value is "private".

ReadOnly (boolean) --A value that sets the write status of a file share. This value is true if the write status is read-only, and otherwise false.

GuessMIMETypeEnabled (boolean) --A value that enables guessing of the MIME type for uploaded objects based on file extensions. Set this value to true to enable MIME type guessing, and otherwise to false. The default value is true.

RequesterPays (boolean) --A value that sets who pays the cost of the request and the cost associated with data download from the S3 bucket. If this value is set to true, the requester pays the costs. Otherwise the S3 bucket owner pays. However, the S3 bucket owner always pays the cost of storing data.

Note
RequesterPays is a configuration for the S3 bucket that backs the file share, so make sure that the configuration on the file share is the same as the S3 bucket configuration.


SMBACLEnabled (boolean) --If this value is set to "true", indicates that ACL (access control list) is enabled on the SMB file share. If it is set to "false", it indicates that file and directory permissions are mapped to the POSIX permission.
For more information, see https://docs.aws.amazon.com/storagegateway/latest/userguide/smb-acl.html in the Storage Gateway User Guide.

AdminUserList (list) --A list of users or groups in the Active Directory that have administrator rights to the file share. A group must be prefixed with the @ character. For example @group1 . Can only be set if Authentication is set to ActiveDirectory .

(string) --


ValidUserList (list) --A list of users or groups in the Active Directory that are allowed to access the file share. A group must be prefixed with the @ character. For example @group1 . Can only be set if Authentication is set to ActiveDirectory .

(string) --


InvalidUserList (list) --A list of users or groups in the Active Directory that are not allowed to access the file share. A group must be prefixed with the @ character. For example @group1 . Can only be set if Authentication is set to ActiveDirectory .

(string) --


AuditDestinationARN (string) --The Amazon Resource Name (ARN) of the storage used for the audit logs.

Authentication (string) --The authentication method of the file share.
Valid values are ActiveDirectory or GuestAccess . The default is ActiveDirectory .

Tags (list) --A list of up to 50 tags assigned to the SMB file share, sorted alphabetically by key name. Each tag is a key-value pair. For a gateway with more than 10 tags assigned, you can view all tags using the ListTagsForResource API operation.

(dict) --A key-value pair that helps you manage, filter, and search for your resource. Allowed characters: letters, white space, and numbers, representable in UTF-8, and the following characters: + - = . _ : /

Key (string) --Tag key (String). The key can\'t start with aws:.

Value (string) --Value of the tag key.














Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError


    :return: {
        'SMBFileShareInfoList': [
            {
                'FileShareARN': 'string',
                'FileShareId': 'string',
                'FileShareStatus': 'string',
                'GatewayARN': 'string',
                'KMSEncrypted': True|False,
                'KMSKey': 'string',
                'Path': 'string',
                'Role': 'string',
                'LocationARN': 'string',
                'DefaultStorageClass': 'string',
                'ObjectACL': 'private'|'public-read'|'public-read-write'|'authenticated-read'|'bucket-owner-read'|'bucket-owner-full-control'|'aws-exec-read',
                'ReadOnly': True|False,
                'GuessMIMETypeEnabled': True|False,
                'RequesterPays': True|False,
                'SMBACLEnabled': True|False,
                'AdminUserList': [
                    'string',
                ],
                'ValidUserList': [
                    'string',
                ],
                'InvalidUserList': [
                    'string',
                ],
                'AuditDestinationARN': 'string',
                'Authentication': 'string',
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_smb_settings(GatewayARN=None):
    """
    Gets a description of a Server Message Block (SMB) file share settings from a file gateway. This operation is only supported for file gateways.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_smb_settings(
        GatewayARN='string'
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and AWS Region.\n

    :rtype: dict
ReturnsResponse Syntax{
    'GatewayARN': 'string',
    'DomainName': 'string',
    'ActiveDirectoryStatus': 'ACCESS_DENIED'|'DETACHED'|'JOINED'|'JOINING'|'NETWORK_ERROR'|'TIMEOUT'|'UNKNOWN_ERROR',
    'SMBGuestPasswordSet': True|False,
    'SMBSecurityStrategy': 'ClientSpecified'|'MandatorySigning'|'MandatoryEncryption'
}


Response Structure

(dict) --
GatewayARN (string) --The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and AWS Region.

DomainName (string) --The name of the domain that the gateway is joined to.

ActiveDirectoryStatus (string) --Indicates the status of a gateway that is a member of the Active Directory domain.

ACCESS_DENIED: Indicates that the JoinDomain operation failed due to an authentication error.
DETACHED: Indicates that gateway is not joined to a domain.
JOINED: Indicates that the gateway has successfully joined a domain.
JOINING: Indicates that a JoinDomain operation is in progress.
NETWORK_ERROR: Indicates that JoinDomain operation failed due to a network or connectivity error.
TIMEOUT: Indicates that the JoinDomain operation failed because the operation didn\'t complete within the allotted time.
UNKNOWN_ERROR: Indicates that the JoinDomain operation failed due to another type of error.


SMBGuestPasswordSet (boolean) --This value is true if a password for the guest user \xe2\x80\x9csmbguest\xe2\x80\x9d is set, and otherwise false.

SMBSecurityStrategy (string) --The type of security strategy that was specified for file gateway.
ClientSpecified: if you use this option, requests are established based on what is negotiated by the client. This option is recommended when you want to maximize compatibility across different clients in your environment.
MandatorySigning: if you use this option, file gateway only allows connections from SMBv2 or SMBv3 clients that have signing enabled. This option works with SMB clients on Microsoft Windows Vista, Windows Server 2008 or newer.
MandatoryEncryption: if you use this option, file gateway only allows connections from SMBv3 clients that have encryption enabled. This option is highly recommended for environments that handle sensitive data. This option works with SMB clients on Microsoft Windows 8, Windows Server 2012 or newer.






Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError


    :return: {
        'GatewayARN': 'string',
        'DomainName': 'string',
        'ActiveDirectoryStatus': 'ACCESS_DENIED'|'DETACHED'|'JOINED'|'JOINING'|'NETWORK_ERROR'|'TIMEOUT'|'UNKNOWN_ERROR',
        'SMBGuestPasswordSet': True|False,
        'SMBSecurityStrategy': 'ClientSpecified'|'MandatorySigning'|'MandatoryEncryption'
    }
    
    
    :returns: 
    StorageGateway.Client.exceptions.InvalidGatewayRequestException
    StorageGateway.Client.exceptions.InternalServerError
    
    """
    pass

def describe_snapshot_schedule(VolumeARN=None):
    """
    Describes the snapshot schedule for the specified gateway volume. The snapshot schedule information includes intervals at which snapshots are automatically initiated on the volume. This operation is only supported in the cached volume and stored volume types.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Describes the snapshot schedule for the specified gateway volume including intervals at which snapshots are automatically initiated.
    Expected Output:
    
    :example: response = client.describe_snapshot_schedule(
        VolumeARN='string'
    )
    
    
    :type VolumeARN: string
    :param VolumeARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the volume. Use the ListVolumes operation to return a list of gateway volumes.\n

    :rtype: dict
ReturnsResponse Syntax{
    'VolumeARN': 'string',
    'StartAt': 123,
    'RecurrenceInHours': 123,
    'Description': 'string',
    'Timezone': 'string',
    'Tags': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ]
}


Response Structure

(dict) --
VolumeARN (string) --The Amazon Resource Name (ARN) of the volume that was specified in the request.

StartAt (integer) --The hour of the day at which the snapshot schedule begins represented as hh , where hh is the hour (0 to 23). The hour of the day is in the time zone of the gateway.

RecurrenceInHours (integer) --The number of hours between snapshots.

Description (string) --The snapshot description.

Timezone (string) --A value that indicates the time zone of the gateway.

Tags (list) --A list of up to 50 tags assigned to the snapshot schedule, sorted alphabetically by key name. Each tag is a key-value pair. For a gateway with more than 10 tags assigned, you can view all tags using the ListTagsForResource API operation.

(dict) --A key-value pair that helps you manage, filter, and search for your resource. Allowed characters: letters, white space, and numbers, representable in UTF-8, and the following characters: + - = . _ : /

Key (string) --Tag key (String). The key can\'t start with aws:.

Value (string) --Value of the tag key.










Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError

Examples
Describes the snapshot schedule for the specified gateway volume including intervals at which snapshots are automatically initiated.
response = client.describe_snapshot_schedule(
    VolumeARN='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B/volume/vol-1122AABB',
)

print(response)


Expected Output:
{
    'Description': 'sgw-AABB1122:vol-AABB1122:Schedule',
    'RecurrenceInHours': 24,
    'StartAt': 6,
    'Timezone': 'GMT+7:00',
    'VolumeARN': 'arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B/volume/vol-1122AABB',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'VolumeARN': 'string',
        'StartAt': 123,
        'RecurrenceInHours': 123,
        'Description': 'string',
        'Timezone': 'string',
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    """
    pass

def describe_stored_iscsi_volumes(VolumeARNs=None):
    """
    Returns the description of the gateway volumes specified in the request. The list of gateway volumes in the request must be from one gateway. In the response AWS Storage Gateway returns volume information sorted by volume ARNs. This operation is only supported in stored volume gateway type.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Returns the description of the gateway volumes specified in the request belonging to the same gateway.
    Expected Output:
    
    :example: response = client.describe_stored_iscsi_volumes(
        VolumeARNs=[
            'string',
        ]
    )
    
    
    :type VolumeARNs: list
    :param VolumeARNs: [REQUIRED]\nAn array of strings where each string represents the Amazon Resource Name (ARN) of a stored volume. All of the specified stored volumes must be from the same gateway. Use ListVolumes to get volume ARNs for a gateway.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'StorediSCSIVolumes': [
        {
            'VolumeARN': 'string',
            'VolumeId': 'string',
            'VolumeType': 'string',
            'VolumeStatus': 'string',
            'VolumeAttachmentStatus': 'string',
            'VolumeSizeInBytes': 123,
            'VolumeProgress': 123.0,
            'VolumeDiskId': 'string',
            'SourceSnapshotId': 'string',
            'PreservedExistingData': True|False,
            'VolumeiSCSIAttributes': {
                'TargetARN': 'string',
                'NetworkInterfaceId': 'string',
                'NetworkInterfacePort': 123,
                'LunNumber': 123,
                'ChapEnabled': True|False
            },
            'CreatedDate': datetime(2015, 1, 1),
            'VolumeUsedInBytes': 123,
            'KMSKey': 'string',
            'TargetName': 'string'
        },
    ]
}


Response Structure

(dict) --
StorediSCSIVolumes (list) --Describes a single unit of output from  DescribeStorediSCSIVolumes . The following fields are returned:

ChapEnabled : Indicates whether mutual CHAP is enabled for the iSCSI target.
LunNumber : The logical disk number.
NetworkInterfaceId : The network interface ID of the stored volume that initiator use to map the stored volume as an iSCSI target.
NetworkInterfacePort : The port used to communicate with iSCSI targets.
PreservedExistingData : Indicates if when the stored volume was created, existing data on the underlying local disk was preserved.
SourceSnapshotId : If the stored volume was created from a snapshot, this field contains the snapshot ID used, e.g. snap-1122aabb. Otherwise, this field is not included.
StorediSCSIVolumes : An array of StorediSCSIVolume objects where each object contains metadata about one stored volume.
TargetARN : The Amazon Resource Name (ARN) of the volume target.
VolumeARN : The Amazon Resource Name (ARN) of the stored volume.
VolumeDiskId : The disk ID of the local disk that was specified in the  CreateStorediSCSIVolume operation.
VolumeId : The unique identifier of the storage volume, e.g. vol-1122AABB.
VolumeiSCSIAttributes : An  VolumeiSCSIAttributes object that represents a collection of iSCSI attributes for one stored volume.
VolumeProgress : Represents the percentage complete if the volume is restoring or bootstrapping that represents the percent of data transferred. This field does not appear in the response if the stored volume is not restoring or bootstrapping.
VolumeSizeInBytes : The size of the volume in bytes.
VolumeStatus : One of the VolumeStatus values that indicates the state of the volume.
VolumeType : One of the enumeration values describing the type of the volume. Currently, on STORED volumes are supported.


(dict) --Describes an iSCSI stored volume.

VolumeARN (string) --The Amazon Resource Name (ARN) of the storage volume.

VolumeId (string) --The unique identifier of the volume, e.g. vol-AE4B946D.

VolumeType (string) --One of the VolumeType enumeration values describing the type of the volume.

VolumeStatus (string) --One of the VolumeStatus values that indicates the state of the storage volume.

VolumeAttachmentStatus (string) --A value that indicates whether a storage volume is attached to, detached from, or is in the process of detaching from a gateway. For more information, see Moving Your Volumes to a Different Gateway .

VolumeSizeInBytes (integer) --The size of the volume in bytes.

VolumeProgress (float) --Represents the percentage complete if the volume is restoring or bootstrapping that represents the percent of data transferred. This field does not appear in the response if the stored volume is not restoring or bootstrapping.

VolumeDiskId (string) --The ID of the local disk that was specified in the  CreateStorediSCSIVolume operation.

SourceSnapshotId (string) --If the stored volume was created from a snapshot, this field contains the snapshot ID used, e.g. snap-78e22663. Otherwise, this field is not included.

PreservedExistingData (boolean) --Indicates if when the stored volume was created, existing data on the underlying local disk was preserved.
Valid Values: true, false

VolumeiSCSIAttributes (dict) --An  VolumeiSCSIAttributes object that represents a collection of iSCSI attributes for one stored volume.

TargetARN (string) --The Amazon Resource Name (ARN) of the volume target.

NetworkInterfaceId (string) --The network interface identifier.

NetworkInterfacePort (integer) --The port used to communicate with iSCSI targets.

LunNumber (integer) --The logical disk number.

ChapEnabled (boolean) --Indicates whether mutual CHAP is enabled for the iSCSI target.



CreatedDate (datetime) --The date the volume was created. Volumes created prior to March 28, 2017 don\xe2\x80\x99t have this time stamp.

VolumeUsedInBytes (integer) --The size of the data stored on the volume in bytes. This value is calculated based on the number of blocks that are touched, instead of the actual amount of data written. This value can be useful for sequential write patterns but less accurate for random write patterns. VolumeUsedInBytes is different from the compressed size of the volume, which is the value that is used to calculate your bill.

Note
This value is not available for volumes created prior to May 13, 2015, until you store data on the volume.


KMSKey (string) --The Amazon Resource Name (ARN) of the AWS KMS key used for Amazon S3 server-side encryption. This value can only be set when KMSEncrypted is true. Optional.

TargetName (string) --The name of the iSCSI target used by an initiator to connect to a volume and used as a suffix for the target ARN. For example, specifying TargetName as myvolume results in the target ARN of arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/target/iqn.1997-05.com.amazon:myvolume . The target name must be unique across all volumes on a gateway.
If you don\'t specify a value, Storage Gateway uses the value that was previously used for this volume as the new target name.










Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError

Examples
Returns the description of the gateway volumes specified in the request belonging to the same gateway.
response = client.describe_stored_iscsi_volumes(
    VolumeARNs=[
        'arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B/volume/vol-1122AABB',
    ],
)

print(response)


Expected Output:
{
    'StorediSCSIVolumes': [
        {
            'PreservedExistingData': False,
            'VolumeARN': 'arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B/volume/vol-1122AABB',
            'VolumeDiskId': 'pci-0000:03:00.0-scsi-0:0:0:0',
            'VolumeId': 'vol-1122AABB',
            'VolumeProgress': 23.7,
            'VolumeSizeInBytes': 1099511627776,
            'VolumeStatus': 'BOOTSTRAPPING',
            'VolumeiSCSIAttributes': {
                'ChapEnabled': True,
                'NetworkInterfaceId': '10.243.43.207',
                'NetworkInterfacePort': 3260,
                'TargetARN': 'arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B/target/iqn.1997-05.com.amazon:myvolume',
            },
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'StorediSCSIVolumes': [
            {
                'VolumeARN': 'string',
                'VolumeId': 'string',
                'VolumeType': 'string',
                'VolumeStatus': 'string',
                'VolumeAttachmentStatus': 'string',
                'VolumeSizeInBytes': 123,
                'VolumeProgress': 123.0,
                'VolumeDiskId': 'string',
                'SourceSnapshotId': 'string',
                'PreservedExistingData': True|False,
                'VolumeiSCSIAttributes': {
                    'TargetARN': 'string',
                    'NetworkInterfaceId': 'string',
                    'NetworkInterfacePort': 123,
                    'LunNumber': 123,
                    'ChapEnabled': True|False
                },
                'CreatedDate': datetime(2015, 1, 1),
                'VolumeUsedInBytes': 123,
                'KMSKey': 'string',
                'TargetName': 'string'
            },
        ]
    }
    
    
    :returns: 
    ChapEnabled : Indicates whether mutual CHAP is enabled for the iSCSI target.
    LunNumber : The logical disk number.
    NetworkInterfaceId : The network interface ID of the stored volume that initiator use to map the stored volume as an iSCSI target.
    NetworkInterfacePort : The port used to communicate with iSCSI targets.
    PreservedExistingData : Indicates if when the stored volume was created, existing data on the underlying local disk was preserved.
    SourceSnapshotId : If the stored volume was created from a snapshot, this field contains the snapshot ID used, e.g. snap-1122aabb. Otherwise, this field is not included.
    StorediSCSIVolumes : An array of StorediSCSIVolume objects where each object contains metadata about one stored volume.
    TargetARN : The Amazon Resource Name (ARN) of the volume target.
    VolumeARN : The Amazon Resource Name (ARN) of the stored volume.
    VolumeDiskId : The disk ID of the local disk that was specified in the  CreateStorediSCSIVolume operation.
    VolumeId : The unique identifier of the storage volume, e.g. vol-1122AABB.
    VolumeiSCSIAttributes : An  VolumeiSCSIAttributes object that represents a collection of iSCSI attributes for one stored volume.
    VolumeProgress : Represents the percentage complete if the volume is restoring or bootstrapping that represents the percent of data transferred. This field does not appear in the response if the stored volume is not restoring or bootstrapping.
    VolumeSizeInBytes : The size of the volume in bytes.
    VolumeStatus : One of the VolumeStatus values that indicates the state of the volume.
    VolumeType : One of the enumeration values describing the type of the volume. Currently, on STORED volumes are supported.
    
    """
    pass

def describe_tape_archives(TapeARNs=None, Marker=None, Limit=None):
    """
    Returns a description of specified virtual tapes in the virtual tape shelf (VTS). This operation is only supported in the tape gateway type.
    If a specific TapeARN is not specified, AWS Storage Gateway returns a description of all virtual tapes found in the VTS associated with your account.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Returns a description of specified virtual tapes in the virtual tape shelf (VTS).
    Expected Output:
    
    :example: response = client.describe_tape_archives(
        TapeARNs=[
            'string',
        ],
        Marker='string',
        Limit=123
    )
    
    
    :type TapeARNs: list
    :param TapeARNs: Specifies one or more unique Amazon Resource Names (ARNs) that represent the virtual tapes you want to describe.\n\n(string) --\n\n

    :type Marker: string
    :param Marker: An opaque string that indicates the position at which to begin describing virtual tapes.

    :type Limit: integer
    :param Limit: Specifies that the number of virtual tapes described be limited to the specified number.

    :rtype: dict

ReturnsResponse Syntax
{
    'TapeArchives': [
        {
            'TapeARN': 'string',
            'TapeBarcode': 'string',
            'TapeCreatedDate': datetime(2015, 1, 1),
            'TapeSizeInBytes': 123,
            'CompletionTime': datetime(2015, 1, 1),
            'RetrievedTo': 'string',
            'TapeStatus': 'string',
            'TapeUsedInBytes': 123,
            'KMSKey': 'string',
            'PoolId': 'string'
        },
    ],
    'Marker': 'string'
}


Response Structure

(dict) --
DescribeTapeArchivesOutput

TapeArchives (list) --
An array of virtual tape objects in the virtual tape shelf (VTS). The description includes of the Amazon Resource Name (ARN) of the virtual tapes. The information returned includes the Amazon Resource Names (ARNs) of the tapes, size of the tapes, status of the tapes, progress of the description and tape barcode.

(dict) --
Represents a virtual tape that is archived in the virtual tape shelf (VTS).

TapeARN (string) --
The Amazon Resource Name (ARN) of an archived virtual tape.

TapeBarcode (string) --
The barcode that identifies the archived virtual tape.

TapeCreatedDate (datetime) --
The date the virtual tape was created.

TapeSizeInBytes (integer) --
The size, in bytes, of the archived virtual tape.

CompletionTime (datetime) --
The time that the archiving of the virtual tape was completed.
The default time stamp format is in the ISO8601 extended YYYY-MM-DD\'T\'HH:MM:SS\'Z\' format.

RetrievedTo (string) --
The Amazon Resource Name (ARN) of the tape gateway that the virtual tape is being retrieved to.
The virtual tape is retrieved from the virtual tape shelf (VTS).

TapeStatus (string) --
The current state of the archived virtual tape.

TapeUsedInBytes (integer) --
The size, in bytes, of data stored on the virtual tape.

Note
This value is not available for tapes created prior to May 13, 2015.


KMSKey (string) --
The Amazon Resource Name (ARN) of the AWS KMS key used for Amazon S3 server-side encryption. This value can only be set when KMSEncrypted is true. Optional.

PoolId (string) --
The ID of the pool that was used to archive the tape. The tapes in this pool are archived in the S3 storage class that is associated with the pool.
Valid values: "GLACIER", "DEEP_ARCHIVE"





Marker (string) --
An opaque string that indicates the position at which the virtual tapes that were fetched for description ended. Use this marker in your next request to fetch the next set of virtual tapes in the virtual tape shelf (VTS). If there are no more virtual tapes to describe, this field does not appear in the response.







Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError

Examples
Returns a description of specified virtual tapes in the virtual tape shelf (VTS).
response = client.describe_tape_archives(
    Limit=123,
    Marker='1',
    TapeARNs=[
        'arn:aws:storagegateway:us-east-1:999999999999:tape/AM08A1AD',
        'arn:aws:storagegateway:us-east-1:999999999999:tape/AMZN01A2A4',
    ],
)

print(response)


Expected Output:
{
    'Marker': '1',
    'TapeArchives': [
        {
            'CompletionTime': datetime(2016, 12, 16, 13, 50, 0, 4, 351, 0),
            'TapeARN': 'arn:aws:storagegateway:us-east-1:999999999:tape/AM08A1AD',
            'TapeBarcode': 'AM08A1AD',
            'TapeSizeInBytes': 107374182400,
            'TapeStatus': 'ARCHIVED',
        },
        {
            'CompletionTime': datetime(2016, 12, 16, 13, 59, 0, 4, 351, 0),
            'TapeARN': 'arn:aws:storagegateway:us-east-1:999999999:tape/AMZN01A2A4',
            'TapeBarcode': 'AMZN01A2A4',
            'TapeSizeInBytes': 429496729600,
            'TapeStatus': 'ARCHIVED',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'TapeArchives': [
            {
                'TapeARN': 'string',
                'TapeBarcode': 'string',
                'TapeCreatedDate': datetime(2015, 1, 1),
                'TapeSizeInBytes': 123,
                'CompletionTime': datetime(2015, 1, 1),
                'RetrievedTo': 'string',
                'TapeStatus': 'string',
                'TapeUsedInBytes': 123,
                'KMSKey': 'string',
                'PoolId': 'string'
            },
        ],
        'Marker': 'string'
    }
    
    
    :returns: 
    StorageGateway.Client.exceptions.InvalidGatewayRequestException
    StorageGateway.Client.exceptions.InternalServerError
    
    """
    pass

def describe_tape_recovery_points(GatewayARN=None, Marker=None, Limit=None):
    """
    Returns a list of virtual tape recovery points that are available for the specified tape gateway.
    A recovery point is a point-in-time view of a virtual tape at which all the data on the virtual tape is consistent. If your gateway crashes, virtual tapes that have recovery points can be recovered to a new gateway. This operation is only supported in the tape gateway type.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Returns a list of virtual tape recovery points that are available for the specified gateway-VTL.
    Expected Output:
    
    :example: response = client.describe_tape_recovery_points(
        GatewayARN='string',
        Marker='string',
        Limit=123
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and AWS Region.\n

    :type Marker: string
    :param Marker: An opaque string that indicates the position at which to begin describing the virtual tape recovery points.

    :type Limit: integer
    :param Limit: Specifies that the number of virtual tape recovery points that are described be limited to the specified number.

    :rtype: dict

ReturnsResponse Syntax
{
    'GatewayARN': 'string',
    'TapeRecoveryPointInfos': [
        {
            'TapeARN': 'string',
            'TapeRecoveryPointTime': datetime(2015, 1, 1),
            'TapeSizeInBytes': 123,
            'TapeStatus': 'string'
        },
    ],
    'Marker': 'string'
}


Response Structure

(dict) --
DescribeTapeRecoveryPointsOutput

GatewayARN (string) --
The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and AWS Region.

TapeRecoveryPointInfos (list) --
An array of TapeRecoveryPointInfos that are available for the specified gateway.

(dict) --
Describes a recovery point.

TapeARN (string) --
The Amazon Resource Name (ARN) of the virtual tape.

TapeRecoveryPointTime (datetime) --
The time when the point-in-time view of the virtual tape was replicated for later recovery.
The default time stamp format of the tape recovery point time is in the ISO8601 extended YYYY-MM-DD\'T\'HH:MM:SS\'Z\' format.

TapeSizeInBytes (integer) --
The size, in bytes, of the virtual tapes to recover.

TapeStatus (string) --
The status of the virtual tapes.





Marker (string) --
An opaque string that indicates the position at which the virtual tape recovery points that were listed for description ended.
Use this marker in your next request to list the next set of virtual tape recovery points in the list. If there are no more recovery points to describe, this field does not appear in the response.







Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError

Examples
Returns a list of virtual tape recovery points that are available for the specified gateway-VTL.
response = client.describe_tape_recovery_points(
    GatewayARN='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B',
    Limit=1,
    Marker='1',
)

print(response)


Expected Output:
{
    'GatewayARN': 'arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B',
    'Marker': '1',
    'TapeRecoveryPointInfos': [
        {
            'TapeARN': 'arn:aws:storagegateway:us-east-1:999999999:tape/AMZN01A2A4',
            'TapeRecoveryPointTime': datetime(2016, 12, 16, 13, 50, 0, 4, 351, 0),
            'TapeSizeInBytes': 1471550497,
            'TapeStatus': 'AVAILABLE',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'GatewayARN': 'string',
        'TapeRecoveryPointInfos': [
            {
                'TapeARN': 'string',
                'TapeRecoveryPointTime': datetime(2015, 1, 1),
                'TapeSizeInBytes': 123,
                'TapeStatus': 'string'
            },
        ],
        'Marker': 'string'
    }
    
    
    :returns: 
    StorageGateway.Client.exceptions.InvalidGatewayRequestException
    StorageGateway.Client.exceptions.InternalServerError
    
    """
    pass

def describe_tapes(GatewayARN=None, TapeARNs=None, Marker=None, Limit=None):
    """
    Returns a description of the specified Amazon Resource Name (ARN) of virtual tapes. If a TapeARN is not specified, returns a description of all virtual tapes associated with the specified gateway. This operation is only supported in the tape gateway type.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Returns a description of the specified Amazon Resource Name (ARN) of virtual tapes. If a TapeARN is not specified, returns a description of all virtual tapes.
    Expected Output:
    
    :example: response = client.describe_tapes(
        GatewayARN='string',
        TapeARNs=[
            'string',
        ],
        Marker='string',
        Limit=123
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and AWS Region.\n

    :type TapeARNs: list
    :param TapeARNs: Specifies one or more unique Amazon Resource Names (ARNs) that represent the virtual tapes you want to describe. If this parameter is not specified, Tape gateway returns a description of all virtual tapes associated with the specified gateway.\n\n(string) --\n\n

    :type Marker: string
    :param Marker: A marker value, obtained in a previous call to DescribeTapes . This marker indicates which page of results to retrieve.\nIf not specified, the first page of results is retrieved.\n

    :type Limit: integer
    :param Limit: Specifies that the number of virtual tapes described be limited to the specified number.\n\nNote\nAmazon Web Services may impose its own limit, if this field is not set.\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Tapes': [
        {
            'TapeARN': 'string',
            'TapeBarcode': 'string',
            'TapeCreatedDate': datetime(2015, 1, 1),
            'TapeSizeInBytes': 123,
            'TapeStatus': 'string',
            'VTLDevice': 'string',
            'Progress': 123.0,
            'TapeUsedInBytes': 123,
            'KMSKey': 'string',
            'PoolId': 'string'
        },
    ],
    'Marker': 'string'
}


Response Structure

(dict) --
DescribeTapesOutput

Tapes (list) --
An array of virtual tape descriptions.

(dict) --
Describes a virtual tape object.

TapeARN (string) --
The Amazon Resource Name (ARN) of the virtual tape.

TapeBarcode (string) --
The barcode that identifies a specific virtual tape.

TapeCreatedDate (datetime) --
The date the virtual tape was created.

TapeSizeInBytes (integer) --
The size, in bytes, of the virtual tape capacity.

TapeStatus (string) --
The current state of the virtual tape.

VTLDevice (string) --
The virtual tape library (VTL) device that the virtual tape is associated with.

Progress (float) --
For archiving virtual tapes, indicates how much data remains to be uploaded before archiving is complete.
Range: 0 (not started) to 100 (complete).

TapeUsedInBytes (integer) --
The size, in bytes, of data stored on the virtual tape.

Note
This value is not available for tapes created prior to May 13, 2015.


KMSKey (string) --
The Amazon Resource Name (ARN) of the AWS KMS key used for Amazon S3 server-side encryption. This value can only be set when KMSEncrypted is true. Optional.

PoolId (string) --
The ID of the pool that contains tapes that will be archived. The tapes in this pool are archived in the S3 storage class that is associated with the pool. When you use your backup application to eject the tape, the tape is archived directly into the storage class (S3 Glacier or S# Glacier Deep Archive) that corresponds to the pool.
Valid values: "GLACIER", "DEEP_ARCHIVE"





Marker (string) --
An opaque string which can be used as part of a subsequent DescribeTapes call to retrieve the next page of results.
If a response does not contain a marker, then there are no more results to be retrieved.







Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError

Examples
Returns a description of the specified Amazon Resource Name (ARN) of virtual tapes. If a TapeARN is not specified, returns a description of all virtual tapes.
response = client.describe_tapes(
    GatewayARN='arn:aws:storagegateway:us-east-1:999999999999:gateway/sgw-12A3456B',
    Limit=2,
    Marker='1',
    TapeARNs=[
        'arn:aws:storagegateway:us-east-1:999999999999:tape/TEST04A2A1',
        'arn:aws:storagegateway:us-east-1:999999999999:tape/TEST05A2A0',
    ],
)

print(response)


Expected Output:
{
    'Marker': '1',
    'Tapes': [
        {
            'TapeARN': 'arn:aws:storagegateway:us-east-1:999999999999:tape/TEST04A2A1',
            'TapeBarcode': 'TEST04A2A1',
            'TapeSizeInBytes': 107374182400,
            'TapeStatus': 'AVAILABLE',
        },
        {
            'TapeARN': 'arn:aws:storagegateway:us-east-1:999999999999:tape/TEST05A2A0',
            'TapeBarcode': 'TEST05A2A0',
            'TapeSizeInBytes': 107374182400,
            'TapeStatus': 'AVAILABLE',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Tapes': [
            {
                'TapeARN': 'string',
                'TapeBarcode': 'string',
                'TapeCreatedDate': datetime(2015, 1, 1),
                'TapeSizeInBytes': 123,
                'TapeStatus': 'string',
                'VTLDevice': 'string',
                'Progress': 123.0,
                'TapeUsedInBytes': 123,
                'KMSKey': 'string',
                'PoolId': 'string'
            },
        ],
        'Marker': 'string'
    }
    
    
    :returns: 
    StorageGateway.Client.exceptions.InvalidGatewayRequestException
    StorageGateway.Client.exceptions.InternalServerError
    
    """
    pass

def describe_upload_buffer(GatewayARN=None):
    """
    Returns information about the upload buffer of a gateway. This operation is supported for the stored volume, cached volume and tape gateway types.
    The response includes disk IDs that are configured as upload buffer space, and it includes the amount of upload buffer space allocated and used.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Returns information about the upload buffer of a gateway including disk IDs and the amount of upload buffer space allocated/used.
    Expected Output:
    Returns information about the upload buffer of a gateway including disk IDs and the amount of upload buffer space allocated and used.
    Expected Output:
    
    :example: response = client.describe_upload_buffer(
        GatewayARN='string'
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and AWS Region.\n

    :rtype: dict
ReturnsResponse Syntax{
    'GatewayARN': 'string',
    'DiskIds': [
        'string',
    ],
    'UploadBufferUsedInBytes': 123,
    'UploadBufferAllocatedInBytes': 123
}


Response Structure

(dict) --
GatewayARN (string) --The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and AWS Region.

DiskIds (list) --An array of the gateway\'s local disk IDs that are configured as working storage. Each local disk ID is specified as a string (minimum length of 1 and maximum length of 300). If no local disks are configured as working storage, then the DiskIds array is empty.

(string) --


UploadBufferUsedInBytes (integer) --The total number of bytes being used in the gateway\'s upload buffer.

UploadBufferAllocatedInBytes (integer) --The total number of bytes allocated in the gateway\'s as upload buffer.






Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError

Examples
Returns information about the upload buffer of a gateway including disk IDs and the amount of upload buffer space allocated/used.
response = client.describe_upload_buffer(
    GatewayARN='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B',
)

print(response)


Expected Output:
{
    'DiskIds': [
        'pci-0000:03:00.0-scsi-0:0:0:0',
        'pci-0000:04:00.0-scsi-0:1:0:0',
    ],
    'GatewayARN': 'arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B',
    'UploadBufferAllocatedInBytes': 0,
    'UploadBufferUsedInBytes': 161061273600,
    'ResponseMetadata': {
        '...': '...',
    },
}


Returns information about the upload buffer of a gateway including disk IDs and the amount of upload buffer space allocated and used.
response = client.describe_upload_buffer(
    GatewayARN='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B',
)

print(response)


Expected Output:
{
    'DiskIds': [
        'pci-0000:03:00.0-scsi-0:0:0:0',
        'pci-0000:04:00.0-scsi-0:1:0:0',
    ],
    'GatewayARN': 'arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B',
    'UploadBufferAllocatedInBytes': 161061273600,
    'UploadBufferUsedInBytes': 0,
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'GatewayARN': 'string',
        'DiskIds': [
            'string',
        ],
        'UploadBufferUsedInBytes': 123,
        'UploadBufferAllocatedInBytes': 123
    }
    
    
    :returns: 
    StorageGateway.Client.exceptions.InvalidGatewayRequestException
    StorageGateway.Client.exceptions.InternalServerError
    
    """
    pass

def describe_vtl_devices(GatewayARN=None, VTLDeviceARNs=None, Marker=None, Limit=None):
    """
    Returns a description of virtual tape library (VTL) devices for the specified tape gateway. In the response, AWS Storage Gateway returns VTL device information.
    This operation is only supported in the tape gateway type.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Returns a description of virtual tape library (VTL) devices for the specified gateway.
    Expected Output:
    
    :example: response = client.describe_vtl_devices(
        GatewayARN='string',
        VTLDeviceARNs=[
            'string',
        ],
        Marker='string',
        Limit=123
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and AWS Region.\n

    :type VTLDeviceARNs: list
    :param VTLDeviceARNs: An array of strings, where each string represents the Amazon Resource Name (ARN) of a VTL device.\n\nNote\nAll of the specified VTL devices must be from the same gateway. If no VTL devices are specified, the result will contain all devices on the specified gateway.\n\n\n(string) --\n\n

    :type Marker: string
    :param Marker: An opaque string that indicates the position at which to begin describing the VTL devices.

    :type Limit: integer
    :param Limit: Specifies that the number of VTL devices described be limited to the specified number.

    :rtype: dict

ReturnsResponse Syntax
{
    'GatewayARN': 'string',
    'VTLDevices': [
        {
            'VTLDeviceARN': 'string',
            'VTLDeviceType': 'string',
            'VTLDeviceVendor': 'string',
            'VTLDeviceProductIdentifier': 'string',
            'DeviceiSCSIAttributes': {
                'TargetARN': 'string',
                'NetworkInterfaceId': 'string',
                'NetworkInterfacePort': 123,
                'ChapEnabled': True|False
            }
        },
    ],
    'Marker': 'string'
}


Response Structure

(dict) --
DescribeVTLDevicesOutput

GatewayARN (string) --
The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and AWS Region.

VTLDevices (list) --
An array of VTL device objects composed of the Amazon Resource Name (ARN) of the VTL devices.

(dict) --
Represents a device object associated with a tape gateway.

VTLDeviceARN (string) --
Specifies the unique Amazon Resource Name (ARN) of the device (tape drive or media changer).

VTLDeviceType (string) --
Specifies the type of device that the VTL device emulates.

VTLDeviceVendor (string) --
Specifies the vendor of the device that the VTL device object emulates.

VTLDeviceProductIdentifier (string) --
Specifies the model number of device that the VTL device emulates.

DeviceiSCSIAttributes (dict) --
A list of iSCSI information about a VTL device.

TargetARN (string) --
Specifies the unique Amazon Resource Name (ARN) that encodes the iSCSI qualified name(iqn) of a tape drive or media changer target.

NetworkInterfaceId (string) --
The network interface identifier of the VTL device.

NetworkInterfacePort (integer) --
The port used to communicate with iSCSI VTL device targets.

ChapEnabled (boolean) --
Indicates whether mutual CHAP is enabled for the iSCSI target.







Marker (string) --
An opaque string that indicates the position at which the VTL devices that were fetched for description ended. Use the marker in your next request to fetch the next set of VTL devices in the list. If there are no more VTL devices to describe, this field does not appear in the response.







Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError

Examples
Returns a description of virtual tape library (VTL) devices for the specified gateway.
response = client.describe_vtl_devices(
    GatewayARN='arn:aws:storagegateway:us-east-1:999999999999:gateway/sgw-12A3456B',
    Limit=123,
    Marker='1',
    VTLDeviceARNs=[
    ],
)

print(response)


Expected Output:
{
    'GatewayARN': 'arn:aws:storagegateway:us-east-1:999999999999:gateway/sgw-12A3456B',
    'Marker': '1',
    'VTLDevices': [
        {
            'DeviceiSCSIAttributes': {
                'ChapEnabled': False,
                'NetworkInterfaceId': '10.243.43.207',
                'NetworkInterfacePort': 3260,
                'TargetARN': 'arn:aws:storagegateway:us-east-1:999999999999:gateway/sgw-12A3456B/target/iqn.1997-05.com.amazon:sgw-1fad4876-mediachanger',
            },
            'VTLDeviceARN': 'arn:aws:storagegateway:us-east-1:999999999999:gateway/sgw-12A3456B/device/AMZN_SGW-1FAD4876_MEDIACHANGER_00001',
            'VTLDeviceProductIdentifier': 'L700',
            'VTLDeviceType': 'Medium Changer',
            'VTLDeviceVendor': 'STK',
        },
        {
            'DeviceiSCSIAttributes': {
                'ChapEnabled': False,
                'NetworkInterfaceId': '10.243.43.209',
                'NetworkInterfacePort': 3260,
                'TargetARN': 'arn:aws:storagegateway:us-east-1:999999999999:gateway/sgw-12A3456B/target/iqn.1997-05.com.amazon:sgw-1fad4876-tapedrive-01',
            },
            'VTLDeviceARN': 'arn:aws:storagegateway:us-east-1:999999999999:gateway/sgw-12A3456B/device/AMZN_SGW-1FAD4876_TAPEDRIVE_00001',
            'VTLDeviceProductIdentifier': 'ULT3580-TD5',
            'VTLDeviceType': 'Tape Drive',
            'VTLDeviceVendor': 'IBM',
        },
        {
            'DeviceiSCSIAttributes': {
                'ChapEnabled': False,
                'NetworkInterfaceId': '10.243.43.209',
                'NetworkInterfacePort': 3260,
                'TargetARN': 'arn:aws:storagegateway:us-east-1:999999999999:gateway/sgw-12A3456B/target/iqn.1997-05.com.amazon:sgw-1fad4876-tapedrive-02',
            },
            'VTLDeviceARN': 'arn:aws:storagegateway:us-east-1:999999999999:gateway/sgw-12A3456B/device/AMZN_SGW-1FAD4876_TAPEDRIVE_00002',
            'VTLDeviceProductIdentifier': 'ULT3580-TD5',
            'VTLDeviceType': 'Tape Drive',
            'VTLDeviceVendor': 'IBM',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'GatewayARN': 'string',
        'VTLDevices': [
            {
                'VTLDeviceARN': 'string',
                'VTLDeviceType': 'string',
                'VTLDeviceVendor': 'string',
                'VTLDeviceProductIdentifier': 'string',
                'DeviceiSCSIAttributes': {
                    'TargetARN': 'string',
                    'NetworkInterfaceId': 'string',
                    'NetworkInterfacePort': 123,
                    'ChapEnabled': True|False
                }
            },
        ],
        'Marker': 'string'
    }
    
    
    :returns: 
    StorageGateway.Client.exceptions.InvalidGatewayRequestException
    StorageGateway.Client.exceptions.InternalServerError
    
    """
    pass

def describe_working_storage(GatewayARN=None):
    """
    Returns information about the working storage of a gateway. This operation is only supported in the stored volumes gateway type. This operation is deprecated in cached volumes API version (20120630). Use DescribeUploadBuffer instead.
    The response includes disk IDs that are configured as working storage, and it includes the amount of working storage allocated and used.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This operation is supported only for the gateway-stored volume architecture. This operation is deprecated in cached-volumes API version (20120630). Use DescribeUploadBuffer instead.
    Expected Output:
    
    :example: response = client.describe_working_storage(
        GatewayARN='string'
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and AWS Region.\n

    :rtype: dict
ReturnsResponse Syntax{
    'GatewayARN': 'string',
    'DiskIds': [
        'string',
    ],
    'WorkingStorageUsedInBytes': 123,
    'WorkingStorageAllocatedInBytes': 123
}


Response Structure

(dict) --A JSON object containing the following fields:

GatewayARN (string) --The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and AWS Region.

DiskIds (list) --An array of the gateway\'s local disk IDs that are configured as working storage. Each local disk ID is specified as a string (minimum length of 1 and maximum length of 300). If no local disks are configured as working storage, then the DiskIds array is empty.

(string) --


WorkingStorageUsedInBytes (integer) --The total working storage in bytes in use by the gateway. If no working storage is configured for the gateway, this field returns 0.

WorkingStorageAllocatedInBytes (integer) --The total working storage in bytes allocated for the gateway. If no working storage is configured for the gateway, this field returns 0.






Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError

Examples
This operation is supported only for the gateway-stored volume architecture. This operation is deprecated in cached-volumes API version (20120630). Use DescribeUploadBuffer instead.
response = client.describe_working_storage(
    GatewayARN='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B',
)

print(response)


Expected Output:
{
    'DiskIds': [
        'pci-0000:03:00.0-scsi-0:0:0:0',
        'pci-0000:03:00.0-scsi-0:0:1:0',
    ],
    'GatewayARN': 'arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B',
    'WorkingStorageAllocatedInBytes': 2199023255552,
    'WorkingStorageUsedInBytes': 789207040,
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'GatewayARN': 'string',
        'DiskIds': [
            'string',
        ],
        'WorkingStorageUsedInBytes': 123,
        'WorkingStorageAllocatedInBytes': 123
    }
    
    
    :returns: 
    StorageGateway.Client.exceptions.InvalidGatewayRequestException
    StorageGateway.Client.exceptions.InternalServerError
    
    """
    pass

def detach_volume(VolumeARN=None, ForceDetach=None):
    """
    Disconnects a volume from an iSCSI connection and then detaches the volume from the specified gateway. Detaching and attaching a volume enables you to recover your data from one gateway to a different gateway without creating a snapshot. It also makes it easier to move your volumes from an on-premises gateway to a gateway hosted on an Amazon EC2 instance. This operation is only supported in the volume gateway type.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.detach_volume(
        VolumeARN='string',
        ForceDetach=True|False
    )
    
    
    :type VolumeARN: string
    :param VolumeARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the volume to detach from the gateway.\n

    :type ForceDetach: boolean
    :param ForceDetach: Set to true to forcibly remove the iSCSI connection of the target volume and detach the volume. The default is false . If this value is set to false , you must manually disconnect the iSCSI connection from the target volume.

    :rtype: dict

ReturnsResponse Syntax
{
    'VolumeARN': 'string'
}


Response Structure

(dict) --
AttachVolumeOutput

VolumeARN (string) --
The Amazon Resource Name (ARN) of the volume that was detached.







Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError


    :return: {
        'VolumeARN': 'string'
    }
    
    
    :returns: 
    StorageGateway.Client.exceptions.InvalidGatewayRequestException
    StorageGateway.Client.exceptions.InternalServerError
    
    """
    pass

def disable_gateway(GatewayARN=None):
    """
    Disables a tape gateway when the gateway is no longer functioning. For example, if your gateway VM is damaged, you can disable the gateway so you can recover virtual tapes.
    Use this operation for a tape gateway that is not reachable or not functioning. This operation is only supported in the tape gateway type.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Disables a gateway when the gateway is no longer functioning. Use this operation for a gateway-VTL that is not reachable or not functioning.
    Expected Output:
    
    :example: response = client.disable_gateway(
        GatewayARN='string'
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and AWS Region.\n

    :rtype: dict
ReturnsResponse Syntax{
    'GatewayARN': 'string'
}


Response Structure

(dict) --DisableGatewayOutput

GatewayARN (string) --The unique Amazon Resource Name (ARN) of the disabled gateway.






Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError

Examples
Disables a gateway when the gateway is no longer functioning. Use this operation for a gateway-VTL that is not reachable or not functioning.
response = client.disable_gateway(
    GatewayARN='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B',
)

print(response)


Expected Output:
{
    'GatewayARN': 'arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'GatewayARN': 'string'
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

def join_domain(GatewayARN=None, DomainName=None, OrganizationalUnit=None, DomainControllers=None, TimeoutInSeconds=None, UserName=None, Password=None):
    """
    Adds a file gateway to an Active Directory domain. This operation is only supported for file gateways that support the SMB file protocol.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.join_domain(
        GatewayARN='string',
        DomainName='string',
        OrganizationalUnit='string',
        DomainControllers=[
            'string',
        ],
        TimeoutInSeconds=123,
        UserName='string',
        Password='string'
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and AWS Region.\n

    :type DomainName: string
    :param DomainName: [REQUIRED]\nThe name of the domain that you want the gateway to join.\n

    :type OrganizationalUnit: string
    :param OrganizationalUnit: The organizational unit (OU) is a container in an Active Directory that can hold users, groups, computers, and other OUs and this parameter specifies the OU that the gateway will join within the AD domain.

    :type DomainControllers: list
    :param DomainControllers: List of IPv4 addresses, NetBIOS names, or host names of your domain server. If you need to specify the port number include it after the colon (\xe2\x80\x9c:\xe2\x80\x9d). For example, mydc.mydomain.com:389 .\n\n(string) --\n\n

    :type TimeoutInSeconds: integer
    :param TimeoutInSeconds: Specifies the time in seconds, in which the JoinDomain operation must complete. The default is 20 seconds.

    :type UserName: string
    :param UserName: [REQUIRED]\nSets the user name of user who has permission to add the gateway to the Active Directory domain. The domain user account should be enabled to join computers to the domain. For example, you can use the domain administrator account or an account with delegated permissions to join computers to the domain.\n

    :type Password: string
    :param Password: [REQUIRED]\nSets the password of the user who has permission to add the gateway to the Active Directory domain.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'GatewayARN': 'string',
    'ActiveDirectoryStatus': 'ACCESS_DENIED'|'DETACHED'|'JOINED'|'JOINING'|'NETWORK_ERROR'|'TIMEOUT'|'UNKNOWN_ERROR'
}


Response Structure

(dict) --
JoinDomainOutput

GatewayARN (string) --
The unique Amazon Resource Name (ARN) of the gateway that joined the domain.

ActiveDirectoryStatus (string) --
Indicates the status of the gateway as a member of the Active Directory domain.

ACCESS_DENIED: Indicates that the JoinDomain operation failed due to an authentication error.
DETACHED: Indicates that gateway is not joined to a domain.
JOINED: Indicates that the gateway has successfully joined a domain.
JOINING: Indicates that a JoinDomain operation is in progress.
NETWORK_ERROR: Indicates that JoinDomain operation failed due to a network or connectivity error.
TIMEOUT: Indicates that the JoinDomain operation failed because the operation didn\'t complete within the allotted time.
UNKNOWN_ERROR: Indicates that the JoinDomain operation failed due to another type of error.








Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError


    :return: {
        'GatewayARN': 'string',
        'ActiveDirectoryStatus': 'ACCESS_DENIED'|'DETACHED'|'JOINED'|'JOINING'|'NETWORK_ERROR'|'TIMEOUT'|'UNKNOWN_ERROR'
    }
    
    
    :returns: 
    ACCESS_DENIED: Indicates that the JoinDomain operation failed due to an authentication error.
    DETACHED: Indicates that gateway is not joined to a domain.
    JOINED: Indicates that the gateway has successfully joined a domain.
    JOINING: Indicates that a JoinDomain operation is in progress.
    NETWORK_ERROR: Indicates that JoinDomain operation failed due to a network or connectivity error.
    TIMEOUT: Indicates that the JoinDomain operation failed because the operation didn\'t complete within the allotted time.
    UNKNOWN_ERROR: Indicates that the JoinDomain operation failed due to another type of error.
    
    """
    pass

def list_automatic_tape_creation_policies(GatewayARN=None):
    """
    Lists the automatic tape creation policies for a gateway. If there are no automatic tape creation policies for the gateway, it returns an empty list.
    This operation is only supported for tape gateways.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_automatic_tape_creation_policies(
        GatewayARN='string'
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and AWS Region.

    :rtype: dict
ReturnsResponse Syntax{
    'AutomaticTapeCreationPolicyInfos': [
        {
            'AutomaticTapeCreationRules': [
                {
                    'TapeBarcodePrefix': 'string',
                    'PoolId': 'string',
                    'TapeSizeInBytes': 123,
                    'MinimumNumTapes': 123
                },
            ],
            'GatewayARN': 'string'
        },
    ]
}


Response Structure

(dict) --
AutomaticTapeCreationPolicyInfos (list) --Gets a listing of information about the gateway\'s automatic tape creation policies, including the automatic tape creation rules and the gateway that is using the policies.

(dict) --Information about the gateway\'s automatic tape creation policies, including the automatic tape creation rules and the gateway that is using the policies.

AutomaticTapeCreationRules (list) --An automatic tape creation policy consists of a list of automatic tape creation rules. This returns the rules that determine when and how to automatically create new tapes.

(dict) --An automatic tape creation policy consists of automatic tape creation rules where each rule defines when and how to create new tapes.

TapeBarcodePrefix (string) --A prefix that you append to the barcode of the virtual tape that you are creating. This prefix makes the barcode unique.

Note
The prefix must be 1-4 characters in length and must be one of the uppercase letters from A to Z.


PoolId (string) --The ID of the pool that you want to add your tape to for archiving. The tape in this pool is archived in the Amazon S3 storage class that is associated with the pool. When you use your backup application to eject the tape, the tape is archived directly into the storage class (S3 Glacier or S3 Glacier Deep Archive) that corresponds to the pool.
Valid values: "GLACIER", "DEEP_ARCHIVE"

TapeSizeInBytes (integer) --The size, in bytes, of the virtual tape capacity.

MinimumNumTapes (integer) --The minimum number of available virtual tapes that the gateway maintains at all times. If the number of tapes on the gateway goes below this value, the gateway creates as many new tapes as are needed to have MinimumNumTapes on the gateway.





GatewayARN (string) --The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and AWS Region.










Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError


    :return: {
        'AutomaticTapeCreationPolicyInfos': [
            {
                'AutomaticTapeCreationRules': [
                    {
                        'TapeBarcodePrefix': 'string',
                        'PoolId': 'string',
                        'TapeSizeInBytes': 123,
                        'MinimumNumTapes': 123
                    },
                ],
                'GatewayARN': 'string'
            },
        ]
    }
    
    
    """
    pass

def list_file_shares(GatewayARN=None, Limit=None, Marker=None):
    """
    Gets a list of the file shares for a specific file gateway, or the list of file shares that belong to the calling user account. This operation is only supported for file gateways.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_file_shares(
        GatewayARN='string',
        Limit=123,
        Marker='string'
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: The Amazon Resource Name (ARN) of the gateway whose file shares you want to list. If this field is not present, all file shares under your account are listed.

    :type Limit: integer
    :param Limit: The maximum number of file shares to return in the response. The value must be an integer with a value greater than zero. Optional.

    :type Marker: string
    :param Marker: Opaque pagination token returned from a previous ListFileShares operation. If present, Marker specifies where to continue the list from after a previous call to ListFileShares. Optional.

    :rtype: dict

ReturnsResponse Syntax
{
    'Marker': 'string',
    'NextMarker': 'string',
    'FileShareInfoList': [
        {
            'FileShareType': 'NFS'|'SMB',
            'FileShareARN': 'string',
            'FileShareId': 'string',
            'FileShareStatus': 'string',
            'GatewayARN': 'string'
        },
    ]
}


Response Structure

(dict) --
ListFileShareOutput

Marker (string) --
If the request includes Marker , the response returns that value in this field.

NextMarker (string) --
If a value is present, there are more file shares to return. In a subsequent request, use NextMarker as the value for Marker to retrieve the next set of file shares.

FileShareInfoList (list) --
An array of information about the file gateway\'s file shares.

(dict) --
Describes a file share.

FileShareType (string) --
The type of the file share.

FileShareARN (string) --
The Amazon Resource Name (ARN) of the file share.

FileShareId (string) --
The ID of the file share.

FileShareStatus (string) --
The status of the file share. Possible values are CREATING , UPDATING , AVAILABLE and DELETING .

GatewayARN (string) --
The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and AWS Region.











Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError


    :return: {
        'Marker': 'string',
        'NextMarker': 'string',
        'FileShareInfoList': [
            {
                'FileShareType': 'NFS'|'SMB',
                'FileShareARN': 'string',
                'FileShareId': 'string',
                'FileShareStatus': 'string',
                'GatewayARN': 'string'
            },
        ]
    }
    
    
    :returns: 
    StorageGateway.Client.exceptions.InvalidGatewayRequestException
    StorageGateway.Client.exceptions.InternalServerError
    
    """
    pass

def list_gateways(Marker=None, Limit=None):
    """
    Lists gateways owned by an AWS account in an AWS Region specified in the request. The returned list is ordered by gateway Amazon Resource Name (ARN).
    By default, the operation returns a maximum of 100 gateways. This operation supports pagination that allows you to optionally reduce the number of gateways returned in a response.
    If you have more gateways than are returned in a response (that is, the response returns only a truncated list of your gateways), the response contains a marker that you can specify in your next request to fetch the next page of gateways.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Lists gateways owned by an AWS account in a specified region as requested. Results are sorted by gateway ARN up to a maximum of 100 gateways.
    Expected Output:
    
    :example: response = client.list_gateways(
        Marker='string',
        Limit=123
    )
    
    
    :type Marker: string
    :param Marker: An opaque string that indicates the position at which to begin the returned list of gateways.

    :type Limit: integer
    :param Limit: Specifies that the list of gateways returned be limited to the specified number of items.

    :rtype: dict

ReturnsResponse Syntax
{
    'Gateways': [
        {
            'GatewayId': 'string',
            'GatewayARN': 'string',
            'GatewayType': 'string',
            'GatewayOperationalState': 'string',
            'GatewayName': 'string',
            'Ec2InstanceId': 'string',
            'Ec2InstanceRegion': 'string'
        },
    ],
    'Marker': 'string'
}


Response Structure

(dict) --

Gateways (list) --
An array of  GatewayInfo objects.

(dict) --
Describes a gateway object.

GatewayId (string) --
The unique identifier assigned to your gateway during activation. This ID becomes part of the gateway Amazon Resource Name (ARN), which you use as input for other operations.

GatewayARN (string) --
The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and AWS Region.

GatewayType (string) --
The type of the gateway.

GatewayOperationalState (string) --
The state of the gateway.
Valid Values: DISABLED or ACTIVE

GatewayName (string) --
The name of the gateway.

Ec2InstanceId (string) --
The ID of the Amazon EC2 instance that was used to launch the gateway.

Ec2InstanceRegion (string) --
The AWS Region where the Amazon EC2 instance is located.





Marker (string) --
Use the marker in your next request to fetch the next set of gateways in the list. If there are no more gateways to list, this field does not appear in the response.







Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError

Examples
Lists gateways owned by an AWS account in a specified region as requested. Results are sorted by gateway ARN up to a maximum of 100 gateways.
response = client.list_gateways(
    Limit=2,
    Marker='1',
)

print(response)


Expected Output:
{
    'Gateways': [
        {
            'GatewayARN': 'arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B',
        },
        {
            'GatewayARN': 'arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-23A4567C',
        },
    ],
    'Marker': '1',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Gateways': [
            {
                'GatewayId': 'string',
                'GatewayARN': 'string',
                'GatewayType': 'string',
                'GatewayOperationalState': 'string',
                'GatewayName': 'string',
                'Ec2InstanceId': 'string',
                'Ec2InstanceRegion': 'string'
            },
        ],
        'Marker': 'string'
    }
    
    
    :returns: 
    StorageGateway.Client.exceptions.InvalidGatewayRequestException
    StorageGateway.Client.exceptions.InternalServerError
    
    """
    pass

def list_local_disks(GatewayARN=None):
    """
    Returns a list of the gateway\'s local disks. To specify which gateway to describe, you use the Amazon Resource Name (ARN) of the gateway in the body of the request.
    The request returns a list of all disks, specifying which are configured as working storage, cache storage, or stored volume or not configured at all. The response includes a DiskStatus field. This field can have a value of present (the disk is available to use), missing (the disk is no longer connected to the gateway), or mismatch (the disk node is occupied by a disk that has incorrect metadata or the disk content is corrupted).
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The request returns a list of all disks, specifying which are configured as working storage, cache storage, or stored volume or not configured at all.
    Expected Output:
    
    :example: response = client.list_local_disks(
        GatewayARN='string'
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and AWS Region.\n

    :rtype: dict
ReturnsResponse Syntax{
    'GatewayARN': 'string',
    'Disks': [
        {
            'DiskId': 'string',
            'DiskPath': 'string',
            'DiskNode': 'string',
            'DiskStatus': 'string',
            'DiskSizeInBytes': 123,
            'DiskAllocationType': 'string',
            'DiskAllocationResource': 'string',
            'DiskAttributeList': [
                'string',
            ]
        },
    ]
}


Response Structure

(dict) --
GatewayARN (string) --The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and AWS Region.

Disks (list) --A JSON object containing the following fields:

ListLocalDisksOutput$Disks


(dict) --Represents a gateway\'s local disk.

DiskId (string) --The unique device ID or other distinguishing data that identifies a local disk.

DiskPath (string) --The path of a local disk in the gateway virtual machine (VM).

DiskNode (string) --The device node of a local disk as assigned by the virtualization environment.

DiskStatus (string) --A value that represents the status of a local disk.

DiskSizeInBytes (integer) --The local disk size in bytes.

DiskAllocationType (string) --One of the DiskAllocationType enumeration values that identifies how a local disk is used. Valid values: UPLOAD_BUFFER , CACHE_STORAGE

DiskAllocationResource (string) --The iSCSI qualified name (IQN) that is defined for a disk. This field is not included in the response if the local disk is not defined as an iSCSI target. The format of this field is targetIqn::LUNNumber::region-volumeId .

DiskAttributeList (list) --A list of values that represents attributes of a local disk.

(string) --











Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError

Examples
The request returns a list of all disks, specifying which are configured as working storage, cache storage, or stored volume or not configured at all.
response = client.list_local_disks(
    GatewayARN='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B',
)

print(response)


Expected Output:
{
    'Disks': [
        {
            'DiskAllocationType': 'CACHE_STORAGE',
            'DiskId': 'pci-0000:03:00.0-scsi-0:0:0:0',
            'DiskNode': 'SCSI(0:0)',
            'DiskPath': '/dev/sda',
            'DiskSizeInBytes': 1099511627776,
            'DiskStatus': 'missing',
        },
        {
            'DiskAllocationResource': '',
            'DiskAllocationType': 'UPLOAD_BUFFER',
            'DiskId': 'pci-0000:03:00.0-scsi-0:0:1:0',
            'DiskNode': 'SCSI(0:1)',
            'DiskPath': '/dev/sdb',
            'DiskSizeInBytes': 1099511627776,
            'DiskStatus': 'present',
        },
    ],
    'GatewayARN': 'arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'GatewayARN': 'string',
        'Disks': [
            {
                'DiskId': 'string',
                'DiskPath': 'string',
                'DiskNode': 'string',
                'DiskStatus': 'string',
                'DiskSizeInBytes': 123,
                'DiskAllocationType': 'string',
                'DiskAllocationResource': 'string',
                'DiskAttributeList': [
                    'string',
                ]
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_tags_for_resource(ResourceARN=None, Marker=None, Limit=None):
    """
    Lists the tags that have been added to the specified resource. This operation is supported in storage gateways of all types.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Lists the tags that have been added to the specified resource.
    Expected Output:
    
    :example: response = client.list_tags_for_resource(
        ResourceARN='string',
        Marker='string',
        Limit=123
    )
    
    
    :type ResourceARN: string
    :param ResourceARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource for which you want to list tags.\n

    :type Marker: string
    :param Marker: An opaque string that indicates the position at which to begin returning the list of tags.

    :type Limit: integer
    :param Limit: Specifies that the list of tags returned be limited to the specified number of items.

    :rtype: dict

ReturnsResponse Syntax
{
    'ResourceARN': 'string',
    'Marker': 'string',
    'Tags': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ]
}


Response Structure

(dict) --
ListTagsForResourceOutput

ResourceARN (string) --
he Amazon Resource Name (ARN) of the resource for which you want to list tags.

Marker (string) --
An opaque string that indicates the position at which to stop returning the list of tags.

Tags (list) --
An array that contains the tags for the specified resource.

(dict) --
A key-value pair that helps you manage, filter, and search for your resource. Allowed characters: letters, white space, and numbers, representable in UTF-8, and the following characters: + - = . _ : /

Key (string) --
Tag key (String). The key can\'t start with aws:.

Value (string) --
Value of the tag key.











Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError

Examples
Lists the tags that have been added to the specified resource.
response = client.list_tags_for_resource(
    Limit=1,
    Marker='1',
    ResourceARN='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-11A2222B',
)

print(response)


Expected Output:
{
    'Marker': '1',
    'ResourceARN': 'arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-11A2222B',
    'Tags': [
        {
            'Key': 'Dev Gatgeway Region',
            'Value': 'East Coast',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ResourceARN': 'string',
        'Marker': 'string',
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    :returns: 
    StorageGateway.Client.exceptions.InvalidGatewayRequestException
    StorageGateway.Client.exceptions.InternalServerError
    
    """
    pass

def list_tapes(TapeARNs=None, Marker=None, Limit=None):
    """
    Lists virtual tapes in your virtual tape library (VTL) and your virtual tape shelf (VTS). You specify the tapes to list by specifying one or more tape Amazon Resource Names (ARNs). If you don\'t specify a tape ARN, the operation lists all virtual tapes in both your VTL and VTS.
    This operation supports pagination. By default, the operation returns a maximum of up to 100 tapes. You can optionally specify the Limit parameter in the body to limit the number of tapes in the response. If the number of tapes returned in the response is truncated, the response includes a Marker element that you can use in your subsequent request to retrieve the next set of tapes. This operation is only supported in the tape gateway type.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tapes(
        TapeARNs=[
            'string',
        ],
        Marker='string',
        Limit=123
    )
    
    
    :type TapeARNs: list
    :param TapeARNs: The Amazon Resource Name (ARN) of each of the tapes you want to list. If you don\'t specify a tape ARN, the response lists all tapes in both your VTL and VTS.\n\n(string) --\n\n

    :type Marker: string
    :param Marker: A string that indicates the position at which to begin the returned list of tapes.

    :type Limit: integer
    :param Limit: An optional number limit for the tapes in the list returned by this call.

    :rtype: dict

ReturnsResponse Syntax
{
    'TapeInfos': [
        {
            'TapeARN': 'string',
            'TapeBarcode': 'string',
            'TapeSizeInBytes': 123,
            'TapeStatus': 'string',
            'GatewayARN': 'string',
            'PoolId': 'string'
        },
    ],
    'Marker': 'string'
}


Response Structure

(dict) --
A JSON object containing the following fields:

ListTapesOutput$Marker
ListTapesOutput$VolumeInfos


TapeInfos (list) --
An array of  TapeInfo objects, where each object describes a single tape. If there are no tapes in the tape library or VTS, then the TapeInfos is an empty array.

(dict) --
Describes a virtual tape.

TapeARN (string) --
The Amazon Resource Name (ARN) of a virtual tape.

TapeBarcode (string) --
The barcode that identifies a specific virtual tape.

TapeSizeInBytes (integer) --
The size, in bytes, of a virtual tape.

TapeStatus (string) --
The status of the tape.

GatewayARN (string) --
The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and AWS Region.

PoolId (string) --
The ID of the pool that you want to add your tape to for archiving. The tape in this pool is archived in the S3 storage class that is associated with the pool. When you use your backup application to eject the tape, the tape is archived directly into the storage class (S3 Glacier or S3 Glacier Deep Archive) that corresponds to the pool.
Valid values: "GLACIER", "DEEP_ARCHIVE"





Marker (string) --
A string that indicates the position at which to begin returning the next list of tapes. Use the marker in your next request to continue pagination of tapes. If there are no more tapes to list, this element does not appear in the response body.







Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError


    :return: {
        'TapeInfos': [
            {
                'TapeARN': 'string',
                'TapeBarcode': 'string',
                'TapeSizeInBytes': 123,
                'TapeStatus': 'string',
                'GatewayARN': 'string',
                'PoolId': 'string'
            },
        ],
        'Marker': 'string'
    }
    
    
    :returns: 
    ListTapesOutput$Marker
    ListTapesOutput$VolumeInfos
    
    """
    pass

def list_volume_initiators(VolumeARN=None):
    """
    Lists iSCSI initiators that are connected to a volume. You can use this operation to determine whether a volume is being used or not. This operation is only supported in the cached volume and stored volume gateway types.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_volume_initiators(
        VolumeARN='string'
    )
    
    
    :type VolumeARN: string
    :param VolumeARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the volume. Use the ListVolumes operation to return a list of gateway volumes for the gateway.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Initiators': [
        'string',
    ]
}


Response Structure

(dict) --ListVolumeInitiatorsOutput

Initiators (list) --The host names and port numbers of all iSCSI initiators that are connected to the gateway.

(string) --







Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError


    :return: {
        'Initiators': [
            'string',
        ]
    }
    
    
    :returns: 
    StorageGateway.Client.exceptions.InvalidGatewayRequestException
    StorageGateway.Client.exceptions.InternalServerError
    
    """
    pass

def list_volume_recovery_points(GatewayARN=None):
    """
    Lists the recovery points for a specified gateway. This operation is only supported in the cached volume gateway type.
    Each cache volume has one recovery point. A volume recovery point is a point in time at which all data of the volume is consistent and from which you can create a snapshot or clone a new cached volume from a source volume. To create a snapshot from a volume recovery point use the  CreateSnapshotFromVolumeRecoveryPoint operation.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Lists the recovery points for a specified gateway in which all data of the volume is consistent and can be used to create a snapshot.
    Expected Output:
    
    :example: response = client.list_volume_recovery_points(
        GatewayARN='string'
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and AWS Region.\n

    :rtype: dict
ReturnsResponse Syntax{
    'GatewayARN': 'string',
    'VolumeRecoveryPointInfos': [
        {
            'VolumeARN': 'string',
            'VolumeSizeInBytes': 123,
            'VolumeUsageInBytes': 123,
            'VolumeRecoveryPointTime': 'string'
        },
    ]
}


Response Structure

(dict) --
GatewayARN (string) --The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and AWS Region.

VolumeRecoveryPointInfos (list) --An array of  VolumeRecoveryPointInfo objects.

(dict) --Describes a storage volume recovery point object.

VolumeARN (string) --The Amazon Resource Name (ARN) of the volume target.

VolumeSizeInBytes (integer) --The size of the volume in bytes.

VolumeUsageInBytes (integer) --The size of the data stored on the volume in bytes.

Note
This value is not available for volumes created prior to May 13, 2015, until you store data on the volume.


VolumeRecoveryPointTime (string) --The time the recovery point was taken.










Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError

Examples
Lists the recovery points for a specified gateway in which all data of the volume is consistent and can be used to create a snapshot.
response = client.list_volume_recovery_points(
    GatewayARN='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B',
)

print(response)


Expected Output:
{
    'GatewayARN': 'arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B',
    'VolumeRecoveryPointInfos': [
        {
            'VolumeARN': 'arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B/volume/vol-1122AABB',
            'VolumeRecoveryPointTime': '2012-09-04T21:08:44.627Z',
            'VolumeSizeInBytes': 536870912000,
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'GatewayARN': 'string',
        'VolumeRecoveryPointInfos': [
            {
                'VolumeARN': 'string',
                'VolumeSizeInBytes': 123,
                'VolumeUsageInBytes': 123,
                'VolumeRecoveryPointTime': 'string'
            },
        ]
    }
    
    
    """
    pass

def list_volumes(GatewayARN=None, Marker=None, Limit=None):
    """
    Lists the iSCSI stored volumes of a gateway. Results are sorted by volume ARN. The response includes only the volume ARNs. If you want additional volume information, use the  DescribeStorediSCSIVolumes or the  DescribeCachediSCSIVolumes API.
    The operation supports pagination. By default, the operation returns a maximum of up to 100 volumes. You can optionally specify the Limit field in the body to limit the number of volumes in the response. If the number of volumes returned in the response is truncated, the response includes a Marker field. You can use this Marker value in your subsequent request to retrieve the next set of volumes. This operation is only supported in the cached volume and stored volume gateway types.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Lists the iSCSI stored volumes of a gateway. Results are sorted by volume ARN up to a maximum of 100 volumes.
    Expected Output:
    
    :example: response = client.list_volumes(
        GatewayARN='string',
        Marker='string',
        Limit=123
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and AWS Region.

    :type Marker: string
    :param Marker: A string that indicates the position at which to begin the returned list of volumes. Obtain the marker from the response of a previous List iSCSI Volumes request.

    :type Limit: integer
    :param Limit: Specifies that the list of volumes returned be limited to the specified number of items.

    :rtype: dict

ReturnsResponse Syntax
{
    'GatewayARN': 'string',
    'Marker': 'string',
    'VolumeInfos': [
        {
            'VolumeARN': 'string',
            'VolumeId': 'string',
            'GatewayARN': 'string',
            'GatewayId': 'string',
            'VolumeType': 'string',
            'VolumeSizeInBytes': 123,
            'VolumeAttachmentStatus': 'string'
        },
    ]
}


Response Structure

(dict) --
A JSON object containing the following fields:

ListVolumesOutput$Marker
ListVolumesOutput$VolumeInfos


GatewayARN (string) --
The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and AWS Region.

Marker (string) --
Use the marker in your next request to continue pagination of iSCSI volumes. If there are no more volumes to list, this field does not appear in the response body.

VolumeInfos (list) --
An array of  VolumeInfo objects, where each object describes an iSCSI volume. If no volumes are defined for the gateway, then VolumeInfos is an empty array "[]".

(dict) --
Describes a storage volume object.

VolumeARN (string) --
The Amazon Resource Name (ARN) for the storage volume. For example, the following is a valid ARN:

arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/volume/vol-1122AABB

Valid Values: 50 to 500 lowercase letters, numbers, periods (.), and hyphens (-).

VolumeId (string) --
The unique identifier assigned to the volume. This ID becomes part of the volume Amazon Resource Name (ARN), which you use as input for other operations.
Valid Values: 50 to 500 lowercase letters, numbers, periods (.), and hyphens (-).

GatewayARN (string) --
The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and AWS Region.

GatewayId (string) --
The unique identifier assigned to your gateway during activation. This ID becomes part of the gateway Amazon Resource Name (ARN), which you use as input for other operations.
Valid Values: 50 to 500 lowercase letters, numbers, periods (.), and hyphens (-).

VolumeType (string) --
One of the VolumeType enumeration values describing the type of the volume.

VolumeSizeInBytes (integer) --
The size of the volume in bytes.
Valid Values: 50 to 500 lowercase letters, numbers, periods (.), and hyphens (-).

VolumeAttachmentStatus (string) --
One of the VolumeStatus values that indicates the state of the storage volume.











Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError

Examples
Lists the iSCSI stored volumes of a gateway. Results are sorted by volume ARN up to a maximum of 100 volumes.
response = client.list_volumes(
    GatewayARN='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B',
    Limit=2,
    Marker='1',
)

print(response)


Expected Output:
{
    'GatewayARN': 'arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B',
    'Marker': '1',
    'VolumeInfos': [
        {
            'GatewayARN': 'arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B',
            'GatewayId': 'sgw-12A3456B',
            'VolumeARN': 'arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B/volume/vol-1122AABB',
            'VolumeId': 'vol-1122AABB',
            'VolumeSizeInBytes': 107374182400,
            'VolumeType': 'STORED',
        },
        {
            'GatewayARN': 'arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-13B4567C',
            'GatewayId': 'sgw-gw-13B4567C',
            'VolumeARN': 'arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-13B4567C/volume/vol-3344CCDD',
            'VolumeId': 'vol-1122AABB',
            'VolumeSizeInBytes': 107374182400,
            'VolumeType': 'STORED',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'GatewayARN': 'string',
        'Marker': 'string',
        'VolumeInfos': [
            {
                'VolumeARN': 'string',
                'VolumeId': 'string',
                'GatewayARN': 'string',
                'GatewayId': 'string',
                'VolumeType': 'string',
                'VolumeSizeInBytes': 123,
                'VolumeAttachmentStatus': 'string'
            },
        ]
    }
    
    
    :returns: 
    ListVolumesOutput$Marker
    ListVolumesOutput$VolumeInfos
    
    """
    pass

def notify_when_uploaded(FileShareARN=None):
    """
    Sends you notification through CloudWatch Events when all files written to your file share have been uploaded to Amazon S3.
    AWS Storage Gateway can send a notification through Amazon CloudWatch Events when all files written to your file share up to that point in time have been uploaded to Amazon S3. These files include files written to the file share up to the time that you make a request for notification. When the upload is done, Storage Gateway sends you notification through an Amazon CloudWatch Event. You can configure CloudWatch Events to send the notification through event targets such as Amazon SNS or AWS Lambda function. This operation is only supported for file gateways.
    For more information, see Getting File Upload Notification in the Storage Gateway User Guide (https://docs.aws.amazon.com/storagegateway/latest/userguide/monitoring-file-gateway.html#get-upload-notification).
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.notify_when_uploaded(
        FileShareARN='string'
    )
    
    
    :type FileShareARN: string
    :param FileShareARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the file share.\n

    :rtype: dict
ReturnsResponse Syntax{
    'FileShareARN': 'string',
    'NotificationId': 'string'
}


Response Structure

(dict) --
FileShareARN (string) --The Amazon Resource Name (ARN) of the file share.

NotificationId (string) --The randomly generated ID of the notification that was sent. This ID is in UUID format.






Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError


    :return: {
        'FileShareARN': 'string',
        'NotificationId': 'string'
    }
    
    
    """
    pass

def refresh_cache(FileShareARN=None, FolderList=None, Recursive=None):
    """
    Refreshes the cache for the specified file share. This operation finds objects in the Amazon S3 bucket that were added, removed or replaced since the gateway last listed the bucket\'s contents and cached the results. This operation is only supported in the file gateway type. You can subscribe to be notified through an Amazon CloudWatch event when your RefreshCache operation completes. For more information, see Getting Notified About File Operations .
    When this API is called, it only initiates the refresh operation. When the API call completes and returns a success code, it doesn\'t necessarily mean that the file refresh has completed. You should use the refresh-complete notification to determine that the operation has completed before you check for new files on the gateway file share. You can subscribe to be notified through an CloudWatch event when your RefreshCache operation completes.
    Throttle limit: This API is asynchronous so the gateway will accept no more than two refreshes at any time. We recommend using the refresh-complete CloudWatch event notification before issuing additional requests. For more information, see Getting Notified About File Operations .
    If you invoke the RefreshCache API when two requests are already being processed, any new request will cause an InvalidGatewayRequestException error because too many requests were sent to the server.
    For more information, see "https://docs.aws.amazon.com/storagegateway/latest/userguide/monitoring-file-gateway.html#get-notification".
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.refresh_cache(
        FileShareARN='string',
        FolderList=[
            'string',
        ],
        Recursive=True|False
    )
    
    
    :type FileShareARN: string
    :param FileShareARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the file share you want to refresh.\n

    :type FolderList: list
    :param FolderList: A comma-separated list of the paths of folders to refresh in the cache. The default is ['/' ]. The default refreshes objects and folders at the root of the Amazon S3 bucket. If Recursive is set to 'true', the entire S3 bucket that the file share has access to is refreshed.\n\n(string) --\n\n

    :type Recursive: boolean
    :param Recursive: A value that specifies whether to recursively refresh folders in the cache. The refresh includes folders that were in the cache the last time the gateway listed the folder\'s contents. If this value set to 'true', each folder that is listed in FolderList is recursively updated. Otherwise, subfolders listed in FolderList are not refreshed. Only objects that are in folders listed directly under FolderList are found and used for the update. The default is 'true'.

    :rtype: dict

ReturnsResponse Syntax
{
    'FileShareARN': 'string',
    'NotificationId': 'string'
}


Response Structure

(dict) --
RefreshCacheOutput

FileShareARN (string) --
The Amazon Resource Name (ARN) of the file share.

NotificationId (string) --
The randomly generated ID of the notification that was sent. This ID is in UUID format.







Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError


    :return: {
        'FileShareARN': 'string',
        'NotificationId': 'string'
    }
    
    
    :returns: 
    StorageGateway.Client.exceptions.InvalidGatewayRequestException
    StorageGateway.Client.exceptions.InternalServerError
    
    """
    pass

def remove_tags_from_resource(ResourceARN=None, TagKeys=None):
    """
    Removes one or more tags from the specified resource. This operation is supported in storage gateways of all types.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Lists the iSCSI stored volumes of a gateway. Removes one or more tags from the specified resource.
    Expected Output:
    
    :example: response = client.remove_tags_from_resource(
        ResourceARN='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceARN: string
    :param ResourceARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource you want to remove the tags from.\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nThe keys of the tags you want to remove from the specified resource. A tag is composed of a key-value pair.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ResourceARN': 'string'
}


Response Structure

(dict) --
RemoveTagsFromResourceOutput

ResourceARN (string) --
The Amazon Resource Name (ARN) of the resource that the tags were removed from.







Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError

Examples
Lists the iSCSI stored volumes of a gateway. Removes one or more tags from the specified resource.
response = client.remove_tags_from_resource(
    ResourceARN='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-11A2222B',
    TagKeys=[
        'Dev Gatgeway Region',
        'East Coast',
    ],
)

print(response)


Expected Output:
{
    'ResourceARN': 'arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-11A2222B',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ResourceARN': 'string'
    }
    
    
    :returns: 
    StorageGateway.Client.exceptions.InvalidGatewayRequestException
    StorageGateway.Client.exceptions.InternalServerError
    
    """
    pass

def reset_cache(GatewayARN=None):
    """
    Resets all cache disks that have encountered an error and makes the disks available for reconfiguration as cache storage. If your cache disk encounters an error, the gateway prevents read and write operations on virtual tapes in the gateway. For example, an error can occur when a disk is corrupted or removed from the gateway. When a cache is reset, the gateway loses its cache storage. At this point, you can reconfigure the disks as cache disks. This operation is only supported in the cached volume and tape types.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Resets all cache disks that have encountered a error and makes the disks available for reconfiguration as cache storage.
    Expected Output:
    
    :example: response = client.reset_cache(
        GatewayARN='string'
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and AWS Region.\n

    :rtype: dict
ReturnsResponse Syntax{
    'GatewayARN': 'string'
}


Response Structure

(dict) --
GatewayARN (string) --The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and AWS Region.






Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError

Examples
Resets all cache disks that have encountered a error and makes the disks available for reconfiguration as cache storage.
response = client.reset_cache(
    GatewayARN='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-13B4567C',
)

print(response)


Expected Output:
{
    'GatewayARN': 'arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-13B4567C',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'GatewayARN': 'string'
    }
    
    
    """
    pass

def retrieve_tape_archive(TapeARN=None, GatewayARN=None):
    """
    Retrieves an archived virtual tape from the virtual tape shelf (VTS) to a tape gateway. Virtual tapes archived in the VTS are not associated with any gateway. However after a tape is retrieved, it is associated with a gateway, even though it is also listed in the VTS, that is, archive. This operation is only supported in the tape gateway type.
    Once a tape is successfully retrieved to a gateway, it cannot be retrieved again to another gateway. You must archive the tape again before you can retrieve it to another gateway. This operation is only supported in the tape gateway type.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Retrieves an archived virtual tape from the virtual tape shelf (VTS) to a gateway-VTL. Virtual tapes archived in the VTS are not associated with any gateway.
    Expected Output:
    
    :example: response = client.retrieve_tape_archive(
        TapeARN='string',
        GatewayARN='string'
    )
    
    
    :type TapeARN: string
    :param TapeARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the virtual tape you want to retrieve from the virtual tape shelf (VTS).\n

    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the gateway you want to retrieve the virtual tape to. Use the ListGateways operation to return a list of gateways for your account and AWS Region.\nYou retrieve archived virtual tapes to only one gateway and the gateway must be a tape gateway.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'TapeARN': 'string'
}


Response Structure

(dict) --
RetrieveTapeArchiveOutput

TapeARN (string) --
The Amazon Resource Name (ARN) of the retrieved virtual tape.







Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError

Examples
Retrieves an archived virtual tape from the virtual tape shelf (VTS) to a gateway-VTL. Virtual tapes archived in the VTS are not associated with any gateway.
response = client.retrieve_tape_archive(
    GatewayARN='arn:aws:storagegateway:us-east-1:999999999999:gateway/sgw-12A3456B',
    TapeARN='arn:aws:storagegateway:us-east-1:999999999999:tape/TEST0AA2AF',
)

print(response)


Expected Output:
{
    'TapeARN': 'arn:aws:storagegateway:us-east-1:999999999999:tape/TEST0AA2AF',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'TapeARN': 'string'
    }
    
    
    :returns: 
    StorageGateway.Client.exceptions.InvalidGatewayRequestException
    StorageGateway.Client.exceptions.InternalServerError
    
    """
    pass

def retrieve_tape_recovery_point(TapeARN=None, GatewayARN=None):
    """
    Retrieves the recovery point for the specified virtual tape. This operation is only supported in the tape gateway type.
    A recovery point is a point in time view of a virtual tape at which all the data on the tape is consistent. If your gateway crashes, virtual tapes that have recovery points can be recovered to a new gateway.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Retrieves the recovery point for the specified virtual tape.
    Expected Output:
    
    :example: response = client.retrieve_tape_recovery_point(
        TapeARN='string',
        GatewayARN='string'
    )
    
    
    :type TapeARN: string
    :param TapeARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the virtual tape for which you want to retrieve the recovery point.\n

    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and AWS Region.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'TapeARN': 'string'
}


Response Structure

(dict) --
RetrieveTapeRecoveryPointOutput

TapeARN (string) --
The Amazon Resource Name (ARN) of the virtual tape for which the recovery point was retrieved.







Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError

Examples
Retrieves the recovery point for the specified virtual tape.
response = client.retrieve_tape_recovery_point(
    GatewayARN='arn:aws:storagegateway:us-east-1:999999999999:gateway/sgw-12A3456B',
    TapeARN='arn:aws:storagegateway:us-east-1:999999999999:tape/TEST0AA2AF',
)

print(response)


Expected Output:
{
    'TapeARN': 'arn:aws:storagegateway:us-east-1:999999999999:tape/TEST0AA2AF',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'TapeARN': 'string'
    }
    
    
    :returns: 
    StorageGateway.Client.exceptions.InvalidGatewayRequestException
    StorageGateway.Client.exceptions.InternalServerError
    
    """
    pass

def set_local_console_password(GatewayARN=None, LocalConsolePassword=None):
    """
    Sets the password for your VM local console. When you log in to the local console for the first time, you log in to the VM with the default credentials. We recommend that you set a new password. You don\'t need to know the default password to set a new password.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Sets the password for your VM local console.
    Expected Output:
    
    :example: response = client.set_local_console_password(
        GatewayARN='string',
        LocalConsolePassword='string'
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and AWS Region.\n

    :type LocalConsolePassword: string
    :param LocalConsolePassword: [REQUIRED]\nThe password you want to set for your VM local console.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'GatewayARN': 'string'
}


Response Structure

(dict) --

GatewayARN (string) --
The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and AWS Region.







Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError

Examples
Sets the password for your VM local console.
response = client.set_local_console_password(
    GatewayARN='arn:aws:storagegateway:us-east-1:999999999999:gateway/sgw-12A3456B',
    LocalConsolePassword='PassWordMustBeAtLeast6Chars.',
)

print(response)


Expected Output:
{
    'GatewayARN': 'arn:aws:storagegateway:us-east-1:999999999999:gateway/sgw-12A3456B',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'GatewayARN': 'string'
    }
    
    
    :returns: 
    StorageGateway.Client.exceptions.InvalidGatewayRequestException
    StorageGateway.Client.exceptions.InternalServerError
    
    """
    pass

def set_smb_guest_password(GatewayARN=None, Password=None):
    """
    Sets the password for the guest user smbguest . The smbguest user is the user when the authentication method for the file share is set to GuestAccess .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.set_smb_guest_password(
        GatewayARN='string',
        Password='string'
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the file gateway the SMB file share is associated with.\n

    :type Password: string
    :param Password: [REQUIRED]\nThe password that you want to set for your SMB Server.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'GatewayARN': 'string'
}


Response Structure

(dict) --

GatewayARN (string) --
The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and AWS Region.







Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError


    :return: {
        'GatewayARN': 'string'
    }
    
    
    :returns: 
    StorageGateway.Client.exceptions.InvalidGatewayRequestException
    StorageGateway.Client.exceptions.InternalServerError
    
    """
    pass

def shutdown_gateway(GatewayARN=None):
    """
    Shuts down a gateway. To specify which gateway to shut down, use the Amazon Resource Name (ARN) of the gateway in the body of your request.
    The operation shuts down the gateway service component running in the gateway\'s virtual machine (VM) and not the host VM.
    After the gateway is shutdown, you cannot call any other API except  StartGateway ,  DescribeGatewayInformation and  ListGateways . For more information, see  ActivateGateway . Your applications cannot read from or write to the gateway\'s storage volumes, and there are no snapshots taken.
    If do not intend to use the gateway again, you must delete the gateway (using  DeleteGateway ) to no longer pay software charges associated with the gateway.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This operation shuts down the gateway service component running in the storage gateway\'s virtual machine (VM) and not the VM.
    Expected Output:
    
    :example: response = client.shutdown_gateway(
        GatewayARN='string'
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and AWS Region.\n

    :rtype: dict
ReturnsResponse Syntax{
    'GatewayARN': 'string'
}


Response Structure

(dict) --A JSON object containing the Amazon Resource Name (ARN) of the gateway that was shut down.

GatewayARN (string) --The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and AWS Region.






Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError

Examples
This operation shuts down the gateway service component running in the storage gateway\'s virtual machine (VM) and not the VM.
response = client.shutdown_gateway(
    GatewayARN='arn:aws:storagegateway:us-east-1:999999999999:gateway/sgw-12A3456B',
)

print(response)


Expected Output:
{
    'GatewayARN': 'arn:aws:storagegateway:us-east-1:999999999999:gateway/sgw-12A3456B',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'GatewayARN': 'string'
    }
    
    
    """
    pass

def start_availability_monitor_test(GatewayARN=None):
    """
    Start a test that verifies that the specified gateway is configured for High Availability monitoring in your host environment. This request only initiates the test and that a successful response only indicates that the test was started. It doesn\'t indicate that the test passed. For the status of the test, invoke the DescribeAvailabilityMonitorTest API.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_availability_monitor_test(
        GatewayARN='string'
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and AWS Region.\n

    :rtype: dict
ReturnsResponse Syntax{
    'GatewayARN': 'string'
}


Response Structure

(dict) --
GatewayARN (string) --The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and AWS Region.






Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError


    :return: {
        'GatewayARN': 'string'
    }
    
    
    """
    pass

def start_gateway(GatewayARN=None):
    """
    Starts a gateway that you previously shut down (see  ShutdownGateway ). After the gateway starts, you can then make other API calls, your applications can read from or write to the gateway\'s storage volumes and you will be able to take snapshot backups.
    To specify which gateway to start, use the Amazon Resource Name (ARN) of the gateway in your request.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Starts a gateway service that was previously shut down.
    Expected Output:
    
    :example: response = client.start_gateway(
        GatewayARN='string'
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and AWS Region.\n

    :rtype: dict
ReturnsResponse Syntax{
    'GatewayARN': 'string'
}


Response Structure

(dict) --A JSON object containing the Amazon Resource Name (ARN) of the gateway that was restarted.

GatewayARN (string) --The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and AWS Region.






Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError

Examples
Starts a gateway service that was previously shut down.
response = client.start_gateway(
    GatewayARN='arn:aws:storagegateway:us-east-1:999999999999:gateway/sgw-12A3456B',
)

print(response)


Expected Output:
{
    'GatewayARN': 'arn:aws:storagegateway:us-east-1:999999999999:gateway/sgw-12A3456B',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'GatewayARN': 'string'
    }
    
    
    """
    pass

def update_automatic_tape_creation_policy(AutomaticTapeCreationRules=None, GatewayARN=None):
    """
    Updates the automatic tape creation policy of a gateway. Use this to update the policy with a new set of automatic tape creation rules. This is only supported for tape gateways.
    By default, there is no automatic tape creation policy.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_automatic_tape_creation_policy(
        AutomaticTapeCreationRules=[
            {
                'TapeBarcodePrefix': 'string',
                'PoolId': 'string',
                'TapeSizeInBytes': 123,
                'MinimumNumTapes': 123
            },
        ],
        GatewayARN='string'
    )
    
    
    :type AutomaticTapeCreationRules: list
    :param AutomaticTapeCreationRules: [REQUIRED]\nAn automatic tape creation policy consists of a list of automatic tape creation rules. The rules determine when and how to automatically create new tapes.\n\n(dict) --An automatic tape creation policy consists of automatic tape creation rules where each rule defines when and how to create new tapes.\n\nTapeBarcodePrefix (string) -- [REQUIRED]A prefix that you append to the barcode of the virtual tape that you are creating. This prefix makes the barcode unique.\n\nNote\nThe prefix must be 1-4 characters in length and must be one of the uppercase letters from A to Z.\n\n\nPoolId (string) -- [REQUIRED]The ID of the pool that you want to add your tape to for archiving. The tape in this pool is archived in the Amazon S3 storage class that is associated with the pool. When you use your backup application to eject the tape, the tape is archived directly into the storage class (S3 Glacier or S3 Glacier Deep Archive) that corresponds to the pool.\nValid values: 'GLACIER', 'DEEP_ARCHIVE'\n\nTapeSizeInBytes (integer) -- [REQUIRED]The size, in bytes, of the virtual tape capacity.\n\nMinimumNumTapes (integer) -- [REQUIRED]The minimum number of available virtual tapes that the gateway maintains at all times. If the number of tapes on the gateway goes below this value, the gateway creates as many new tapes as are needed to have MinimumNumTapes on the gateway.\n\n\n\n\n

    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and AWS Region.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'GatewayARN': 'string'
}


Response Structure

(dict) --

GatewayARN (string) --
The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and AWS Region.







Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError


    :return: {
        'GatewayARN': 'string'
    }
    
    
    :returns: 
    StorageGateway.Client.exceptions.InvalidGatewayRequestException
    StorageGateway.Client.exceptions.InternalServerError
    
    """
    pass

def update_bandwidth_rate_limit(GatewayARN=None, AverageUploadRateLimitInBitsPerSec=None, AverageDownloadRateLimitInBitsPerSec=None):
    """
    Updates the bandwidth rate limits of a gateway. You can update both the upload and download bandwidth rate limit or specify only one of the two. If you don\'t set a bandwidth rate limit, the existing rate limit remains. This operation is supported for the stored volume, cached volume and tape gateway types.\'
    By default, a gateway\'s bandwidth rate limits are not set. If you don\'t set any limit, the gateway does not have any limitations on its bandwidth usage and could potentially use the maximum available bandwidth.
    To specify which gateway to update, use the Amazon Resource Name (ARN) of the gateway in your request.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Updates the bandwidth rate limits of a gateway. Both the upload and download bandwidth rate limit can be set, or either one of the two. If a new limit is not set, the existing rate limit remains.
    Expected Output:
    
    :example: response = client.update_bandwidth_rate_limit(
        GatewayARN='string',
        AverageUploadRateLimitInBitsPerSec=123,
        AverageDownloadRateLimitInBitsPerSec=123
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and AWS Region.\n

    :type AverageUploadRateLimitInBitsPerSec: integer
    :param AverageUploadRateLimitInBitsPerSec: The average upload bandwidth rate limit in bits per second.

    :type AverageDownloadRateLimitInBitsPerSec: integer
    :param AverageDownloadRateLimitInBitsPerSec: The average download bandwidth rate limit in bits per second.

    :rtype: dict

ReturnsResponse Syntax
{
    'GatewayARN': 'string'
}


Response Structure

(dict) --
A JSON object containing the Amazon Resource Name (ARN) of the gateway whose throttle information was updated.

GatewayARN (string) --
The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and AWS Region.







Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError

Examples
Updates the bandwidth rate limits of a gateway. Both the upload and download bandwidth rate limit can be set, or either one of the two. If a new limit is not set, the existing rate limit remains.
response = client.update_bandwidth_rate_limit(
    AverageDownloadRateLimitInBitsPerSec=102400,
    AverageUploadRateLimitInBitsPerSec=51200,
    GatewayARN='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B',
)

print(response)


Expected Output:
{
    'GatewayARN': 'arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'GatewayARN': 'string'
    }
    
    
    :returns: 
    StorageGateway.Client.exceptions.InvalidGatewayRequestException
    StorageGateway.Client.exceptions.InternalServerError
    
    """
    pass

def update_chap_credentials(TargetARN=None, SecretToAuthenticateInitiator=None, InitiatorName=None, SecretToAuthenticateTarget=None):
    """
    Updates the Challenge-Handshake Authentication Protocol (CHAP) credentials for a specified iSCSI target. By default, a gateway does not have CHAP enabled; however, for added security, you might use it. This operation is supported in the volume and tape gateway types.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Updates the Challenge-Handshake Authentication Protocol (CHAP) credentials for a specified iSCSI target.
    Expected Output:
    
    :example: response = client.update_chap_credentials(
        TargetARN='string',
        SecretToAuthenticateInitiator='string',
        InitiatorName='string',
        SecretToAuthenticateTarget='string'
    )
    
    
    :type TargetARN: string
    :param TargetARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the iSCSI volume target. Use the DescribeStorediSCSIVolumes operation to return the TargetARN for specified VolumeARN.\n

    :type SecretToAuthenticateInitiator: string
    :param SecretToAuthenticateInitiator: [REQUIRED]\nThe secret key that the initiator (for example, the Windows client) must provide to participate in mutual CHAP with the target.\n\nNote\nThe secret key must be between 12 and 16 bytes when encoded in UTF-8.\n\n

    :type InitiatorName: string
    :param InitiatorName: [REQUIRED]\nThe iSCSI initiator that connects to the target.\n

    :type SecretToAuthenticateTarget: string
    :param SecretToAuthenticateTarget: The secret key that the target must provide to participate in mutual CHAP with the initiator (e.g. Windows client).\nByte constraints: Minimum bytes of 12. Maximum bytes of 16.\n\nNote\nThe secret key must be between 12 and 16 bytes when encoded in UTF-8.\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'TargetARN': 'string',
    'InitiatorName': 'string'
}


Response Structure

(dict) --
A JSON object containing the following fields:

TargetARN (string) --
The Amazon Resource Name (ARN) of the target. This is the same target specified in the request.

InitiatorName (string) --
The iSCSI initiator that connects to the target. This is the same initiator name specified in the request.







Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError

Examples
Updates the Challenge-Handshake Authentication Protocol (CHAP) credentials for a specified iSCSI target.
response = client.update_chap_credentials(
    InitiatorName='iqn.1991-05.com.microsoft:computername.domain.example.com',
    SecretToAuthenticateInitiator='111111111111',
    SecretToAuthenticateTarget='222222222222',
    TargetARN='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B/target/iqn.1997-05.com.amazon:myvolume',
)

print(response)


Expected Output:
{
    'InitiatorName': 'iqn.1991-05.com.microsoft:computername.domain.example.com',
    'TargetARN': 'arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B/target/iqn.1997-05.com.amazon:myvolume',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'TargetARN': 'string',
        'InitiatorName': 'string'
    }
    
    
    :returns: 
    StorageGateway.Client.exceptions.InvalidGatewayRequestException
    StorageGateway.Client.exceptions.InternalServerError
    
    """
    pass

def update_gateway_information(GatewayARN=None, GatewayName=None, GatewayTimezone=None, CloudWatchLogGroupARN=None):
    """
    Updates a gateway\'s metadata, which includes the gateway\'s name and time zone. To specify which gateway to update, use the Amazon Resource Name (ARN) of the gateway in your request.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Updates a gateway\'s metadata, which includes the gateway\'s name and time zone.
    Expected Output:
    
    :example: response = client.update_gateway_information(
        GatewayARN='string',
        GatewayName='string',
        GatewayTimezone='string',
        CloudWatchLogGroupARN='string'
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and AWS Region.\n

    :type GatewayName: string
    :param GatewayName: The name you configured for your gateway.

    :type GatewayTimezone: string
    :param GatewayTimezone: A value that indicates the time zone of the gateway.

    :type CloudWatchLogGroupARN: string
    :param CloudWatchLogGroupARN: The Amazon Resource Name (ARN) of the Amazon CloudWatch log group that you want to use to monitor and log events in the gateway.\nFor more information, see What Is Amazon CloudWatch Logs? .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'GatewayARN': 'string',
    'GatewayName': 'string'
}


Response Structure

(dict) --
A JSON object containing the ARN of the gateway that was updated.

GatewayARN (string) --
The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and AWS Region.

GatewayName (string) --
The name you configured for your gateway.







Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError

Examples
Updates a gateway\'s metadata, which includes the gateway\'s name and time zone.
response = client.update_gateway_information(
    GatewayARN='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B',
    GatewayName='MyGateway2',
    GatewayTimezone='GMT-12:00',
)

print(response)


Expected Output:
{
    'GatewayARN': 'arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B',
    'GatewayName': '',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'GatewayARN': 'string',
        'GatewayName': 'string'
    }
    
    
    :returns: 
    StorageGateway.Client.exceptions.InvalidGatewayRequestException
    StorageGateway.Client.exceptions.InternalServerError
    
    """
    pass

def update_gateway_software_now(GatewayARN=None):
    """
    Updates the gateway virtual machine (VM) software. The request immediately triggers the software update.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Updates the gateway virtual machine (VM) software. The request immediately triggers the software update.
    Expected Output:
    
    :example: response = client.update_gateway_software_now(
        GatewayARN='string'
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and AWS Region.\n

    :rtype: dict
ReturnsResponse Syntax{
    'GatewayARN': 'string'
}


Response Structure

(dict) --A JSON object containing the Amazon Resource Name (ARN) of the gateway that was updated.

GatewayARN (string) --The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and AWS Region.






Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError

Examples
Updates the gateway virtual machine (VM) software. The request immediately triggers the software update.
response = client.update_gateway_software_now(
    GatewayARN='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B',
)

print(response)


Expected Output:
{
    'GatewayARN': 'arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'GatewayARN': 'string'
    }
    
    
    """
    pass

def update_maintenance_start_time(GatewayARN=None, HourOfDay=None, MinuteOfHour=None, DayOfWeek=None, DayOfMonth=None):
    """
    Updates a gateway\'s weekly maintenance start time information, including day and time of the week. The maintenance time is the time in your gateway\'s time zone.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Updates a gateway\'s weekly maintenance start time information, including day and time of the week. The maintenance time is in your gateway\'s time zone.
    Expected Output:
    
    :example: response = client.update_maintenance_start_time(
        GatewayARN='string',
        HourOfDay=123,
        MinuteOfHour=123,
        DayOfWeek=123,
        DayOfMonth=123
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and AWS Region.\n

    :type HourOfDay: integer
    :param HourOfDay: [REQUIRED]\nThe hour component of the maintenance start time represented as hh , where hh is the hour (00 to 23). The hour of the day is in the time zone of the gateway.\n

    :type MinuteOfHour: integer
    :param MinuteOfHour: [REQUIRED]\nThe minute component of the maintenance start time represented as mm , where mm is the minute (00 to 59). The minute of the hour is in the time zone of the gateway.\n

    :type DayOfWeek: integer
    :param DayOfWeek: The day of the week component of the maintenance start time week represented as an ordinal number from 0 to 6, where 0 represents Sunday and 6 Saturday.

    :type DayOfMonth: integer
    :param DayOfMonth: The day of the month component of the maintenance start time represented as an ordinal number from 1 to 28, where 1 represents the first day of the month and 28 represents the last day of the month.\n\nNote\nThis value is only available for tape and volume gateways.\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'GatewayARN': 'string'
}


Response Structure

(dict) --
A JSON object containing the Amazon Resource Name (ARN) of the gateway whose maintenance start time is updated.

GatewayARN (string) --
The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and AWS Region.







Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError

Examples
Updates a gateway\'s weekly maintenance start time information, including day and time of the week. The maintenance time is in your gateway\'s time zone.
response = client.update_maintenance_start_time(
    DayOfWeek=2,
    GatewayARN='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B',
    HourOfDay=0,
    MinuteOfHour=30,
)

print(response)


Expected Output:
{
    'GatewayARN': 'arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'GatewayARN': 'string'
    }
    
    
    :returns: 
    StorageGateway.Client.exceptions.InvalidGatewayRequestException
    StorageGateway.Client.exceptions.InternalServerError
    
    """
    pass

def update_nfs_file_share(FileShareARN=None, KMSEncrypted=None, KMSKey=None, NFSFileShareDefaults=None, DefaultStorageClass=None, ObjectACL=None, ClientList=None, Squash=None, ReadOnly=None, GuessMIMETypeEnabled=None, RequesterPays=None):
    """
    Updates a Network File System (NFS) file share. This operation is only supported in the file gateway type.
    Updates the following file share setting:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_nfs_file_share(
        FileShareARN='string',
        KMSEncrypted=True|False,
        KMSKey='string',
        NFSFileShareDefaults={
            'FileMode': 'string',
            'DirectoryMode': 'string',
            'GroupId': 123,
            'OwnerId': 123
        },
        DefaultStorageClass='string',
        ObjectACL='private'|'public-read'|'public-read-write'|'authenticated-read'|'bucket-owner-read'|'bucket-owner-full-control'|'aws-exec-read',
        ClientList=[
            'string',
        ],
        Squash='string',
        ReadOnly=True|False,
        GuessMIMETypeEnabled=True|False,
        RequesterPays=True|False
    )
    
    
    :type FileShareARN: string
    :param FileShareARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the file share to be updated.\n

    :type KMSEncrypted: boolean
    :param KMSEncrypted: True to use Amazon S3 server-side encryption with your own AWS KMS key, or false to use a key managed by Amazon S3. Optional.

    :type KMSKey: string
    :param KMSKey: The Amazon Resource Name (ARN) of the AWS KMS key used for Amazon S3 server-side encryption. This value can only be set when KMSEncrypted is true. Optional.

    :type NFSFileShareDefaults: dict
    :param NFSFileShareDefaults: The default values for the file share. Optional.\n\nFileMode (string) --The Unix file mode in the form 'nnnn'. For example, '0666' represents the default file mode inside the file share. The default value is 0666.\n\nDirectoryMode (string) --The Unix directory mode in the form 'nnnn'. For example, '0666' represents the default access mode for all directories inside the file share. The default value is 0777.\n\nGroupId (integer) --The default group ID for the file share (unless the files have another group ID specified). The default value is nfsnobody.\n\nOwnerId (integer) --The default owner ID for files in the file share (unless the files have another owner ID specified). The default value is nfsnobody.\n\n\n

    :type DefaultStorageClass: string
    :param DefaultStorageClass: The default storage class for objects put into an Amazon S3 bucket by the file gateway. Possible values are S3_STANDARD , S3_STANDARD_IA , or S3_ONEZONE_IA . If this field is not populated, the default value S3_STANDARD is used. Optional.

    :type ObjectACL: string
    :param ObjectACL: A value that sets the access control list permission for objects in the S3 bucket that a file gateway puts objects into. The default value is 'private'.

    :type ClientList: list
    :param ClientList: The list of clients that are allowed to access the file gateway. The list must contain either valid IP addresses or valid CIDR blocks.\n\n(string) --\n\n

    :type Squash: string
    :param Squash: The user mapped to anonymous user. Valid options are the following:\n\nRootSquash - Only root is mapped to anonymous user.\nNoSquash - No one is mapped to anonymous user\nAllSquash - Everyone is mapped to anonymous user.\n\n

    :type ReadOnly: boolean
    :param ReadOnly: A value that sets the write status of a file share. This value is true if the write status is read-only, and otherwise false.

    :type GuessMIMETypeEnabled: boolean
    :param GuessMIMETypeEnabled: A value that enables guessing of the MIME type for uploaded objects based on file extensions. Set this value to true to enable MIME type guessing, and otherwise to false. The default value is true.

    :type RequesterPays: boolean
    :param RequesterPays: A value that sets who pays the cost of the request and the cost associated with data download from the S3 bucket. If this value is set to true, the requester pays the costs. Otherwise the S3 bucket owner pays. However, the S3 bucket owner always pays the cost of storing data.\n\nNote\nRequesterPays is a configuration for the S3 bucket that backs the file share, so make sure that the configuration on the file share is the same as the S3 bucket configuration.\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'FileShareARN': 'string'
}


Response Structure

(dict) --
UpdateNFSFileShareOutput

FileShareARN (string) --
The Amazon Resource Name (ARN) of the updated file share.







Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError


    :return: {
        'FileShareARN': 'string'
    }
    
    
    :returns: 
    FileShareARN (string) -- [REQUIRED]
    The Amazon Resource Name (ARN) of the file share to be updated.
    
    KMSEncrypted (boolean) -- True to use Amazon S3 server-side encryption with your own AWS KMS key, or false to use a key managed by Amazon S3. Optional.
    KMSKey (string) -- The Amazon Resource Name (ARN) of the AWS KMS key used for Amazon S3 server-side encryption. This value can only be set when KMSEncrypted is true. Optional.
    NFSFileShareDefaults (dict) -- The default values for the file share. Optional.
    
    FileMode (string) --The Unix file mode in the form "nnnn". For example, "0666" represents the default file mode inside the file share. The default value is 0666.
    
    DirectoryMode (string) --The Unix directory mode in the form "nnnn". For example, "0666" represents the default access mode for all directories inside the file share. The default value is 0777.
    
    GroupId (integer) --The default group ID for the file share (unless the files have another group ID specified). The default value is nfsnobody.
    
    OwnerId (integer) --The default owner ID for files in the file share (unless the files have another owner ID specified). The default value is nfsnobody.
    
    
    
    DefaultStorageClass (string) -- The default storage class for objects put into an Amazon S3 bucket by the file gateway. Possible values are S3_STANDARD , S3_STANDARD_IA , or S3_ONEZONE_IA . If this field is not populated, the default value S3_STANDARD is used. Optional.
    ObjectACL (string) -- A value that sets the access control list permission for objects in the S3 bucket that a file gateway puts objects into. The default value is "private".
    ClientList (list) -- The list of clients that are allowed to access the file gateway. The list must contain either valid IP addresses or valid CIDR blocks.
    
    (string) --
    
    
    Squash (string) -- The user mapped to anonymous user. Valid options are the following:
    
    RootSquash - Only root is mapped to anonymous user.
    NoSquash - No one is mapped to anonymous user
    AllSquash - Everyone is mapped to anonymous user.
    
    
    ReadOnly (boolean) -- A value that sets the write status of a file share. This value is true if the write status is read-only, and otherwise false.
    GuessMIMETypeEnabled (boolean) -- A value that enables guessing of the MIME type for uploaded objects based on file extensions. Set this value to true to enable MIME type guessing, and otherwise to false. The default value is true.
    RequesterPays (boolean) -- A value that sets who pays the cost of the request and the cost associated with data download from the S3 bucket. If this value is set to true, the requester pays the costs. Otherwise the S3 bucket owner pays. However, the S3 bucket owner always pays the cost of storing data.
    
    Note
    RequesterPays is a configuration for the S3 bucket that backs the file share, so make sure that the configuration on the file share is the same as the S3 bucket configuration.
    
    
    
    """
    pass

def update_smb_file_share(FileShareARN=None, KMSEncrypted=None, KMSKey=None, DefaultStorageClass=None, ObjectACL=None, ReadOnly=None, GuessMIMETypeEnabled=None, RequesterPays=None, SMBACLEnabled=None, AdminUserList=None, ValidUserList=None, InvalidUserList=None, AuditDestinationARN=None):
    """
    Updates a Server Message Block (SMB) file share.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_smb_file_share(
        FileShareARN='string',
        KMSEncrypted=True|False,
        KMSKey='string',
        DefaultStorageClass='string',
        ObjectACL='private'|'public-read'|'public-read-write'|'authenticated-read'|'bucket-owner-read'|'bucket-owner-full-control'|'aws-exec-read',
        ReadOnly=True|False,
        GuessMIMETypeEnabled=True|False,
        RequesterPays=True|False,
        SMBACLEnabled=True|False,
        AdminUserList=[
            'string',
        ],
        ValidUserList=[
            'string',
        ],
        InvalidUserList=[
            'string',
        ],
        AuditDestinationARN='string'
    )
    
    
    :type FileShareARN: string
    :param FileShareARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the SMB file share that you want to update.\n

    :type KMSEncrypted: boolean
    :param KMSEncrypted: True to use Amazon S3 server-side encryption with your own AWS KMS key, or false to use a key managed by Amazon S3. Optional.

    :type KMSKey: string
    :param KMSKey: The Amazon Resource Name (ARN) of the AWS KMS key used for Amazon S3 server-side encryption. This value can only be set when KMSEncrypted is true. Optional.

    :type DefaultStorageClass: string
    :param DefaultStorageClass: The default storage class for objects put into an Amazon S3 bucket by the file gateway. Possible values are S3_STANDARD , S3_STANDARD_IA , or S3_ONEZONE_IA . If this field is not populated, the default value S3_STANDARD is used. Optional.

    :type ObjectACL: string
    :param ObjectACL: A value that sets the access control list permission for objects in the S3 bucket that a file gateway puts objects into. The default value is 'private'.

    :type ReadOnly: boolean
    :param ReadOnly: A value that sets the write status of a file share. This value is true if the write status is read-only, and otherwise false.

    :type GuessMIMETypeEnabled: boolean
    :param GuessMIMETypeEnabled: A value that enables guessing of the MIME type for uploaded objects based on file extensions. Set this value to true to enable MIME type guessing, and otherwise to false. The default value is true.

    :type RequesterPays: boolean
    :param RequesterPays: A value that sets who pays the cost of the request and the cost associated with data download from the S3 bucket. If this value is set to true, the requester pays the costs. Otherwise the S3 bucket owner pays. However, the S3 bucket owner always pays the cost of storing data.\n\nNote\nRequesterPays is a configuration for the S3 bucket that backs the file share, so make sure that the configuration on the file share is the same as the S3 bucket configuration.\n\n

    :type SMBACLEnabled: boolean
    :param SMBACLEnabled: Set this value to 'true to enable ACL (access control list) on the SMB file share. Set it to 'false' to map file and directory permissions to the POSIX permissions.\nFor more information, see https://docs.aws.amazon.com/storagegateway/latest/userguide/smb-acl.htmlin the Storage Gateway User Guide.\n

    :type AdminUserList: list
    :param AdminUserList: A list of users in the Active Directory that have administrator rights to the file share. A group must be prefixed with the @ character. For example @group1 . Can only be set if Authentication is set to ActiveDirectory .\n\n(string) --\n\n

    :type ValidUserList: list
    :param ValidUserList: A list of users or groups in the Active Directory that are allowed to access the file share. A group must be prefixed with the @ character. For example @group1 . Can only be set if Authentication is set to ActiveDirectory .\n\n(string) --\n\n

    :type InvalidUserList: list
    :param InvalidUserList: A list of users or groups in the Active Directory that are not allowed to access the file share. A group must be prefixed with the @ character. For example @group1 . Can only be set if Authentication is set to ActiveDirectory .\n\n(string) --\n\n

    :type AuditDestinationARN: string
    :param AuditDestinationARN: The Amazon Resource Name (ARN) of the storage used for the audit logs.

    :rtype: dict

ReturnsResponse Syntax
{
    'FileShareARN': 'string'
}


Response Structure

(dict) --
UpdateSMBFileShareOutput

FileShareARN (string) --
The Amazon Resource Name (ARN) of the updated SMB file share.







Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError


    :return: {
        'FileShareARN': 'string'
    }
    
    
    :returns: 
    StorageGateway.Client.exceptions.InvalidGatewayRequestException
    StorageGateway.Client.exceptions.InternalServerError
    
    """
    pass

def update_smb_security_strategy(GatewayARN=None, SMBSecurityStrategy=None):
    """
    Updates the SMB security strategy on a file gateway. This action is only supported in file gateways.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_smb_security_strategy(
        GatewayARN='string',
        SMBSecurityStrategy='ClientSpecified'|'MandatorySigning'|'MandatoryEncryption'
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and AWS Region.\n

    :type SMBSecurityStrategy: string
    :param SMBSecurityStrategy: [REQUIRED]\nSpecifies the type of security strategy.\nClientSpecified: if you use this option, requests are established based on what is negotiated by the client. This option is recommended when you want to maximize compatibility across different clients in your environment.\nMandatorySigning: if you use this option, file gateway only allows connections from SMBv2 or SMBv3 clients that have signing enabled. This option works with SMB clients on Microsoft Windows Vista, Windows Server 2008 or newer.\nMandatoryEncryption: if you use this option, file gateway only allows connections from SMBv3 clients that have encryption enabled. This option is highly recommended for environments that handle sensitive data. This option works with SMB clients on Microsoft Windows 8, Windows Server 2012 or newer.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'GatewayARN': 'string'
}


Response Structure

(dict) --

GatewayARN (string) --
The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and AWS Region.







Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError


    :return: {
        'GatewayARN': 'string'
    }
    
    
    :returns: 
    StorageGateway.Client.exceptions.InvalidGatewayRequestException
    StorageGateway.Client.exceptions.InternalServerError
    
    """
    pass

def update_snapshot_schedule(VolumeARN=None, StartAt=None, RecurrenceInHours=None, Description=None, Tags=None):
    """
    Updates a snapshot schedule configured for a gateway volume. This operation is only supported in the cached volume and stored volume gateway types.
    The default snapshot schedule for volume is once every 24 hours, starting at the creation time of the volume. You can use this API to change the snapshot schedule configured for the volume.
    In the request you must identify the gateway volume whose snapshot schedule you want to update, and the schedule information, including when you want the snapshot to begin on a day and the frequency (in hours) of snapshots.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Updates a snapshot schedule configured for a gateway volume.
    Expected Output:
    
    :example: response = client.update_snapshot_schedule(
        VolumeARN='string',
        StartAt=123,
        RecurrenceInHours=123,
        Description='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type VolumeARN: string
    :param VolumeARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the volume. Use the ListVolumes operation to return a list of gateway volumes.\n

    :type StartAt: integer
    :param StartAt: [REQUIRED]\nThe hour of the day at which the snapshot schedule begins represented as hh , where hh is the hour (0 to 23). The hour of the day is in the time zone of the gateway.\n

    :type RecurrenceInHours: integer
    :param RecurrenceInHours: [REQUIRED]\nFrequency of snapshots. Specify the number of hours between snapshots.\n

    :type Description: string
    :param Description: Optional description of the snapshot that overwrites the existing description.

    :type Tags: list
    :param Tags: A list of up to 50 tags that can be assigned to a snapshot. Each tag is a key-value pair.\n\nNote\nValid characters for key and value are letters, spaces, and numbers representable in UTF-8 format, and the following special characters: + - = . _ : / @. The maximum length of a tag\'s key is 128 characters, and the maximum length for a tag\'s value is 256.\n\n\n(dict) --A key-value pair that helps you manage, filter, and search for your resource. Allowed characters: letters, white space, and numbers, representable in UTF-8, and the following characters: + - = . _ : /\n\nKey (string) -- [REQUIRED]Tag key (String). The key can\'t start with aws:.\n\nValue (string) -- [REQUIRED]Value of the tag key.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'VolumeARN': 'string'
}


Response Structure

(dict) --
A JSON object containing the Amazon Resource Name (ARN) of the updated storage volume.

VolumeARN (string) --
The Amazon Resource Name (ARN) of the volume. Use the  ListVolumes operation to return a list of gateway volumes.







Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError

Examples
Updates a snapshot schedule configured for a gateway volume.
response = client.update_snapshot_schedule(
    Description='Hourly snapshot',
    RecurrenceInHours=1,
    StartAt=0,
    VolumeARN='arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B/volume/vol-1122AABB',
)

print(response)


Expected Output:
{
    'VolumeARN': 'arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B/volume/vol-1122AABB',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'VolumeARN': 'string'
    }
    
    
    :returns: 
    StorageGateway.Client.exceptions.InvalidGatewayRequestException
    StorageGateway.Client.exceptions.InternalServerError
    
    """
    pass

def update_vtl_device_type(VTLDeviceARN=None, DeviceType=None):
    """
    Updates the type of medium changer in a tape gateway. When you activate a tape gateway, you select a medium changer type for the tape gateway. This operation enables you to select a different type of medium changer after a tape gateway is activated. This operation is only supported in the tape gateway type.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Updates the type of medium changer in a gateway-VTL after a gateway-VTL is activated.
    Expected Output:
    
    :example: response = client.update_vtl_device_type(
        VTLDeviceARN='string',
        DeviceType='string'
    )
    
    
    :type VTLDeviceARN: string
    :param VTLDeviceARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the medium changer you want to select.\n

    :type DeviceType: string
    :param DeviceType: [REQUIRED]\nThe type of medium changer you want to select.\nValid Values: 'STK-L700', 'AWS-Gateway-VTL'\n

    :rtype: dict

ReturnsResponse Syntax
{
    'VTLDeviceARN': 'string'
}


Response Structure

(dict) --
UpdateVTLDeviceTypeOutput

VTLDeviceARN (string) --
The Amazon Resource Name (ARN) of the medium changer you have selected.







Exceptions

StorageGateway.Client.exceptions.InvalidGatewayRequestException
StorageGateway.Client.exceptions.InternalServerError

Examples
Updates the type of medium changer in a gateway-VTL after a gateway-VTL is activated.
response = client.update_vtl_device_type(
    DeviceType='Medium Changer',
    VTLDeviceARN='arn:aws:storagegateway:us-east-1:999999999999:gateway/sgw-12A3456B/device/AMZN_SGW-1FAD4876_MEDIACHANGER_00001',
)

print(response)


Expected Output:
{
    'VTLDeviceARN': 'arn:aws:storagegateway:us-east-1:999999999999:gateway/sgw-12A3456B/device/AMZN_SGW-1FAD4876_MEDIACHANGER_00001',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'VTLDeviceARN': 'string'
    }
    
    
    :returns: 
    StorageGateway.Client.exceptions.InvalidGatewayRequestException
    StorageGateway.Client.exceptions.InternalServerError
    
    """
    pass

