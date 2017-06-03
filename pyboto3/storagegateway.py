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

def activate_gateway(ActivationKey=None, GatewayName=None, GatewayTimezone=None, GatewayRegion=None, GatewayType=None, TapeDriveType=None, MediumChangerType=None):
    """
    Activates the gateway you previously deployed on your host. For more information, see Activate the AWS Storage Gateway . In the activation process, you specify information such as the region you want to use for storing snapshots or tapes, the time zone for scheduled snapshots the gateway snapshot schedule window, an activation key, and a name for your gateway. The activation process also associates your gateway with your account; for more information, see  UpdateGatewayInformation .
    See also: AWS API Documentation
    
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
        MediumChangerType='string'
    )
    
    
    :type ActivationKey: string
    :param ActivationKey: [REQUIRED]
            Your gateway activation key. You can obtain the activation key by sending an HTTP GET request with redirects enabled to the gateway IP address (port 80). The redirect URL returned in the response provides you the activation key for your gateway in the query string parameter activationKey . It may also include other activation-related parameters, however, these are merely defaults -- the arguments you pass to the ActivateGateway API call determine the actual configuration of your gateway.
            

    :type GatewayName: string
    :param GatewayName: [REQUIRED]
            The name you configured for your gateway.
            

    :type GatewayTimezone: string
    :param GatewayTimezone: [REQUIRED]
            A value that indicates the time zone you want to set for the gateway. The time zone is of the format 'GMT-hr:mm' or 'GMT+hr:mm'. For example, GMT-4:00 indicates the time is 4 hours behind GMT. GMT+2:00 indicates the time is 2 hours ahead of GMT. The time zone is used, for example, for scheduling snapshots and your gateway's maintenance schedule.
            

    :type GatewayRegion: string
    :param GatewayRegion: [REQUIRED]
            A value that indicates the region where you want to store your data. The gateway region specified must be the same region as the region in your Host header in the request. For more information about available regions and endpoints for AWS Storage Gateway, see Regions and Endpoints in the Amazon Web Services Glossary .
            Valid Values: 'us-east-1', 'us-east-2', 'us-west-1', 'us-west-2', 'ca-central-1', 'eu-west-1', 'eu-central-1', 'eu-west-2', 'ap-northeast-1', 'ap-northeast-2', 'ap-southeast-1', 'ap-southeast-2', 'ap-south-1', 'sa-east-1'
            

    :type GatewayType: string
    :param GatewayType: A value that defines the type of gateway to activate. The type specified is critical to all later functions of the gateway and cannot be changed after activation. The default value is STORED .
            Valid Values: 'STORED', 'CACHED', 'VTL', 'FILE_S3'
            

    :type TapeDriveType: string
    :param TapeDriveType: The value that indicates the type of tape drive to use for tape gateway. This field is optional.
            Valid Values: 'IBM-ULT3580-TD5'
            

    :type MediumChangerType: string
    :param MediumChangerType: The value that indicates the type of medium changer to use for tape gateway. This field is optional.
            Valid Values: 'STK-L700', 'AWS-Gateway-VTL'
            

    :rtype: dict
    :return: {
        'GatewayARN': 'string'
    }
    
    
    """
    pass

def add_cache(GatewayARN=None, DiskIds=None):
    """
    Configures one or more gateway local disks as cache for a gateway. This operation is only supported in the cached volume, tape and file gateway architectures (see Storage Gateway Concepts ).
    In the request, you specify the gateway Amazon Resource Name (ARN) to which you want to add cache, and one or more disk IDs that you want to configure as cache.
    See also: AWS API Documentation
    
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
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            

    :type DiskIds: list
    :param DiskIds: [REQUIRED]
            (string) --
            

    :rtype: dict
    :return: {
        'GatewayARN': 'string'
    }
    
    
    """
    pass

def add_tags_to_resource(ResourceARN=None, Tags=None):
    """
    Adds one or more tags to the specified resource. You use tags to add metadata to resources, which you can use to categorize these resources. For example, you can categorize resources by purpose, owner, environment, or team. Each tag consists of a key and a value, which you define. You can add tags to the following AWS Storage Gateway resources:
    You can create a maximum of 10 tags for each resource. Virtual tapes and storage volumes that are recovered to a new gateway maintain their tags.
    See also: AWS API Documentation
    
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
    :param ResourceARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the resource you want to add tags to.
            

    :type Tags: list
    :param Tags: [REQUIRED]
            The key-value pair that represents the tag you want to add to the resource. The value can be an empty string.
            Note
            Valid characters for key and value are letters, spaces, and numbers representable in UTF-8 format, and the following special characters: + - = . _ : / @.
            (dict) --
            Key (string) -- [REQUIRED]
            Value (string) -- [REQUIRED]
            

    :rtype: dict
    :return: {
        'ResourceARN': 'string'
    }
    
    
    :returns: 
    ResourceARN (string) -- [REQUIRED]
    The Amazon Resource Name (ARN) of the resource you want to add tags to.
    
    Tags (list) -- [REQUIRED]
    The key-value pair that represents the tag you want to add to the resource. The value can be an empty string.
    
    Note
    Valid characters for key and value are letters, spaces, and numbers representable in UTF-8 format, and the following special characters: + - = . _ : / @.
    
    
    (dict) --
    Key (string) -- [REQUIRED]
    Value (string) -- [REQUIRED]
    
    
    
    
    
    """
    pass

def add_upload_buffer(GatewayARN=None, DiskIds=None):
    """
    Configures one or more gateway local disks as upload buffer for a specified gateway. This operation is supported for the stored volume, cached volume and tape gateway architectures.
    In the request, you specify the gateway Amazon Resource Name (ARN) to which you want to add upload buffer, and one or more disk IDs that you want to configure as upload buffer.
    See also: AWS API Documentation
    
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
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            

    :type DiskIds: list
    :param DiskIds: [REQUIRED]
            (string) --
            

    :rtype: dict
    :return: {
        'GatewayARN': 'string'
    }
    
    
    """
    pass

def add_working_storage(GatewayARN=None, DiskIds=None):
    """
    Configures one or more gateway local disks as working storage for a gateway. This operation is only supported in the stored volume gateway architecture. This operation is deprecated in cached volume API version 20120630. Use  AddUploadBuffer instead.
    In the request, you specify the gateway Amazon Resource Name (ARN) to which you want to add working storage, and one or more disk IDs that you want to configure as working storage.
    See also: AWS API Documentation
    
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
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            

    :type DiskIds: list
    :param DiskIds: [REQUIRED]
            An array of strings that identify disks that are to be configured as working storage. Each string have a minimum length of 1 and maximum length of 300. You can get the disk IDs from the ListLocalDisks API.
            (string) --
            

    :rtype: dict
    :return: {
        'GatewayARN': 'string'
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

def cancel_archival(GatewayARN=None, TapeARN=None):
    """
    Cancels archiving of a virtual tape to the virtual tape shelf (VTS) after the archiving process is initiated. This operation is only supported in the tape gateway architecture.
    See also: AWS API Documentation
    
    Examples
    Cancels archiving of a virtual tape to the virtual tape shelf (VTS) after the archiving process is initiated.
    Expected Output:
    
    :example: response = client.cancel_archival(
        GatewayARN='string',
        TapeARN='string'
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            

    :type TapeARN: string
    :param TapeARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the virtual tape you want to cancel archiving for.
            

    :rtype: dict
    :return: {
        'TapeARN': 'string'
    }
    
    
    """
    pass

def cancel_retrieval(GatewayARN=None, TapeARN=None):
    """
    Cancels retrieval of a virtual tape from the virtual tape shelf (VTS) to a gateway after the retrieval process is initiated. The virtual tape is returned to the VTS.
    See also: AWS API Documentation
    
    Examples
    Cancels retrieval of a virtual tape from the virtual tape shelf (VTS) to a gateway after the retrieval process is initiated.
    Expected Output:
    
    :example: response = client.cancel_retrieval(
        GatewayARN='string',
        TapeARN='string'
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            

    :type TapeARN: string
    :param TapeARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the virtual tape you want to cancel retrieval for.
            

    :rtype: dict
    :return: {
        'TapeARN': 'string'
    }
    
    
    """
    pass

def create_cached_iscsi_volume(GatewayARN=None, VolumeSizeInBytes=None, SnapshotId=None, TargetName=None, SourceVolumeARN=None, NetworkInterfaceId=None, ClientToken=None):
    """
    Creates a cached volume on a specified cached volume gateway. This operation is only supported in the cached volume gateway architecture.
    In the request, you must specify the gateway, size of the volume in bytes, the iSCSI target name, an IP address on which to expose the target, and a unique client token. In response, the gateway creates the volume and returns information about it. This information includes the volume Amazon Resource Name (ARN), its size, and the iSCSI target ARN that initiators can use to connect to the volume target.
    Optionally, you can provide the ARN for an existing volume as the SourceVolumeARN for this cached volume, which creates an exact copy of the existing volumes latest recovery point. The VolumeSizeInBytes value must be equal to or larger than the size of the copied volume, in bytes.
    See also: AWS API Documentation
    
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
        ClientToken='string'
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            

    :type VolumeSizeInBytes: integer
    :param VolumeSizeInBytes: [REQUIRED]

    :type SnapshotId: string
    :param SnapshotId: 

    :type TargetName: string
    :param TargetName: [REQUIRED]

    :type SourceVolumeARN: string
    :param SourceVolumeARN: The ARN for an existing volume. Specifying this ARN makes the new volume into an exact copy of the specified existing volume's latest recovery point. The VolumeSizeInBytes value for this new volume must be equal to or larger than the size of the existing volume, in bytes.

    :type NetworkInterfaceId: string
    :param NetworkInterfaceId: [REQUIRED]

    :type ClientToken: string
    :param ClientToken: [REQUIRED]

    :rtype: dict
    :return: {
        'VolumeARN': 'string',
        'TargetARN': 'string'
    }
    
    
    :returns: 
    (dict) --
    VolumeARN (string) --
    TargetARN (string) --
    
    
    
    """
    pass

def create_nfs_file_share(ClientToken=None, NFSFileShareDefaults=None, GatewayARN=None, KMSEncrypted=None, KMSKey=None, Role=None, LocationARN=None, DefaultStorageClass=None, ClientList=None, Squash=None, ReadOnly=None):
    """
    Creates a file share on an existing file gateway. In Storage Gateway, a file share is a file system mount point backed by Amazon S3 cloud storage. Storage Gateway exposes file shares using a Network File System (NFS) interface. This operation is only supported in the file gateway architecture.
    See also: AWS API Documentation
    
    
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
        ClientList=[
            'string',
        ],
        Squash='string',
        ReadOnly=True|False
    )
    
    
    :type ClientToken: string
    :param ClientToken: [REQUIRED]
            A unique string value that you supply that is used by file gateway to ensure idempotent file share creation.
            

    :type NFSFileShareDefaults: dict
    :param NFSFileShareDefaults: File share default values. Optional.
            FileMode (string) --The Unix file mode in the form 'nnnn'. For example, '0666' represents the default file mode inside the file share. The default value is 0666.
            DirectoryMode (string) --The Unix directory mode in the form 'nnnn'. For example, '0666' represents the default access mode for all directories inside the file share. The default value is 0777.
            GroupId (integer) --The default group ID for the file share (unless the files have another group ID specified). The default value is nfsnobody.
            OwnerId (integer) --The default owner ID for files in the file share (unless the files have another owner ID specified). The default value is nfsnobody.
            

    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the file gateway on which you want to create a file share.
            

    :type KMSEncrypted: boolean
    :param KMSEncrypted: True to use Amazon S3 server side encryption with your own AWS KMS key, or false to use a key managed by Amazon S3. Optional.

    :type KMSKey: string
    :param KMSKey: The KMS key used for Amazon S3 server side encryption. This value can only be set when KmsEncrypted is true. Optional.

    :type Role: string
    :param Role: [REQUIRED]
            The ARN of the AWS Identity and Access Management (IAM) role that a file gateway assumes when it accesses the underlying storage.
            

    :type LocationARN: string
    :param LocationARN: [REQUIRED]
            The ARN of the backed storage used for storing file data.
            

    :type DefaultStorageClass: string
    :param DefaultStorageClass: The default storage class for objects put into an Amazon S3 bucket by file gateway. Possible values are S3_STANDARD or S3_STANDARD_IA. If this field is not populated, the default value S3_STANDARD is used. Optional.

    :type ClientList: list
    :param ClientList: The list of clients that are allowed to access the file gateway. The list must contain either valid IP addresses or valid CIDR blocks.
            (string) --
            

    :type Squash: string
    :param Squash: Maps a user to anonymous user. Valid options are the following:
            'RootSquash' - Only root is mapped to anonymous user.
            'NoSquash' - No one is mapped to anonymous user.
            'AllSquash' - Everyone is mapped to anonymous user.
            

    :type ReadOnly: boolean
    :param ReadOnly: Sets the write status of a file share: 'true' if the write status is read-only, and otherwise 'false'.

    :rtype: dict
    :return: {
        'FileShareARN': 'string'
    }
    
    
    """
    pass

def create_snapshot(VolumeARN=None, SnapshotDescription=None):
    """
    Initiates a snapshot of a volume.
    AWS Storage Gateway provides the ability to back up point-in-time snapshots of your data to Amazon Simple Storage (S3) for durable off-site recovery, as well as import the data to an Amazon Elastic Block Store (EBS) volume in Amazon Elastic Compute Cloud (EC2). You can take snapshots of your gateway volume on a scheduled or ad-hoc basis. This API enables you to take ad-hoc snapshot. For more information, see Editing a Snapshot Schedule .
    In the CreateSnapshot request you identify the volume by providing its Amazon Resource Name (ARN). You must also provide description for the snapshot. When AWS Storage Gateway takes the snapshot of specified volume, the snapshot and description appears in the AWS Storage Gateway Console. In response, AWS Storage Gateway returns you a snapshot ID. You can use this snapshot ID to check the snapshot progress or later use it when you want to create a volume from a snapshot. This operation is only supported in stored and cached volume gateway architecture.
    See also: AWS API Documentation
    
    Examples
    Initiates an ad-hoc snapshot of a gateway volume.
    Expected Output:
    
    :example: response = client.create_snapshot(
        VolumeARN='string',
        SnapshotDescription='string'
    )
    
    
    :type VolumeARN: string
    :param VolumeARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the volume. Use the ListVolumes operation to return a list of gateway volumes.
            

    :type SnapshotDescription: string
    :param SnapshotDescription: [REQUIRED]
            Textual description of the snapshot that appears in the Amazon EC2 console, Elastic Block Store snapshots panel in the Description field, and in the AWS Storage Gateway snapshot Details pane, Description field
            

    :rtype: dict
    :return: {
        'VolumeARN': 'string',
        'SnapshotId': 'string'
    }
    
    
    """
    pass

def create_snapshot_from_volume_recovery_point(VolumeARN=None, SnapshotDescription=None):
    """
    Initiates a snapshot of a gateway from a volume recovery point. This operation is only supported in the cached volume gateway architecture.
    A volume recovery point is a point in time at which all data of the volume is consistent and from which you can create a snapshot. To get a list of volume recovery point for cached volume gateway, use  ListVolumeRecoveryPoints .
    In the CreateSnapshotFromVolumeRecoveryPoint request, you identify the volume by providing its Amazon Resource Name (ARN). You must also provide a description for the snapshot. When the gateway takes a snapshot of the specified volume, the snapshot and its description appear in the AWS Storage Gateway console. In response, the gateway returns you a snapshot ID. You can use this snapshot ID to check the snapshot progress or later use it when you want to create a volume from a snapshot.
    See also: AWS API Documentation
    
    Examples
    Initiates a snapshot of a gateway from a volume recovery point.
    Expected Output:
    
    :example: response = client.create_snapshot_from_volume_recovery_point(
        VolumeARN='string',
        SnapshotDescription='string'
    )
    
    
    :type VolumeARN: string
    :param VolumeARN: [REQUIRED]

    :type SnapshotDescription: string
    :param SnapshotDescription: [REQUIRED]

    :rtype: dict
    :return: {
        'SnapshotId': 'string',
        'VolumeARN': 'string',
        'VolumeRecoveryPointTime': 'string'
    }
    
    
    :returns: 
    (dict) --
    SnapshotId (string) --
    VolumeARN (string) --
    VolumeRecoveryPointTime (string) --
    
    
    
    """
    pass

def create_stored_iscsi_volume(GatewayARN=None, DiskId=None, SnapshotId=None, PreserveExistingData=None, TargetName=None, NetworkInterfaceId=None):
    """
    Creates a volume on a specified gateway. This operation is only supported in the stored volume gateway architecture.
    The size of the volume to create is inferred from the disk size. You can choose to preserve existing data on the disk, create volume from an existing snapshot, or create an empty volume. If you choose to create an empty gateway volume, then any existing data on the disk is erased.
    In the request you must specify the gateway and the disk information on which you are creating the volume. In response, the gateway creates the volume and returns volume information such as the volume Amazon Resource Name (ARN), its size, and the iSCSI target ARN that initiators can use to connect to the volume target.
    See also: AWS API Documentation
    
    Examples
    Creates a stored volume on a specified stored gateway.
    Expected Output:
    
    :example: response = client.create_stored_iscsi_volume(
        GatewayARN='string',
        DiskId='string',
        SnapshotId='string',
        PreserveExistingData=True|False,
        TargetName='string',
        NetworkInterfaceId='string'
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            

    :type DiskId: string
    :param DiskId: [REQUIRED]
            The unique identifier for the gateway local disk that is configured as a stored volume. Use ListLocalDisks to list disk IDs for a gateway.
            

    :type SnapshotId: string
    :param SnapshotId: The snapshot ID (e.g. 'snap-1122aabb') of the snapshot to restore as the new stored volume. Specify this field if you want to create the iSCSI storage volume from a snapshot otherwise do not include this field. To list snapshots for your account use DescribeSnapshots in the Amazon Elastic Compute Cloud API Reference .

    :type PreserveExistingData: boolean
    :param PreserveExistingData: [REQUIRED]
            Specify this field as true if you want to preserve the data on the local disk. Otherwise, specifying this field as false creates an empty volume.
            Valid Values: true, false
            

    :type TargetName: string
    :param TargetName: [REQUIRED]
            The name of the iSCSI target used by initiators to connect to the target and as a suffix for the target ARN. For example, specifying TargetName as myvolume results in the target ARN of arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B/target/iqn.1997-05.com.amazon:myvolume. The target name must be unique across all volumes of a gateway.
            

    :type NetworkInterfaceId: string
    :param NetworkInterfaceId: [REQUIRED]
            The network interface of the gateway on which to expose the iSCSI target. Only IPv4 addresses are accepted. Use DescribeGatewayInformation to get a list of the network interfaces available on a gateway.
            Valid Values: A valid IP address.
            

    :rtype: dict
    :return: {
        'VolumeARN': 'string',
        'VolumeSizeInBytes': 123,
        'TargetARN': 'string'
    }
    
    
    """
    pass

def create_tape_with_barcode(GatewayARN=None, TapeSizeInBytes=None, TapeBarcode=None):
    """
    Creates a virtual tape by using your own barcode. You write data to the virtual tape and then archive the tape. This operation is only supported in the tape gateway architecture.
    See also: AWS API Documentation
    
    Examples
    Creates a virtual tape by using your own barcode.
    Expected Output:
    
    :example: response = client.create_tape_with_barcode(
        GatewayARN='string',
        TapeSizeInBytes=123,
        TapeBarcode='string'
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]
            The unique Amazon Resource Name (ARN) that represents the gateway to associate the virtual tape with. Use the ListGateways operation to return a list of gateways for your account and region.
            

    :type TapeSizeInBytes: integer
    :param TapeSizeInBytes: [REQUIRED]
            The size, in bytes, of the virtual tape that you want to create.
            Note
            The size must be aligned by gigabyte (1024*1024*1024 byte).
            

    :type TapeBarcode: string
    :param TapeBarcode: [REQUIRED]
            The barcode that you want to assign to the tape.
            

    :rtype: dict
    :return: {
        'TapeARN': 'string'
    }
    
    
    """
    pass

def create_tapes(GatewayARN=None, TapeSizeInBytes=None, ClientToken=None, NumTapesToCreate=None, TapeBarcodePrefix=None):
    """
    Creates one or more virtual tapes. You write data to the virtual tapes and then archive the tapes. This operation is only supported in the tape gateway architecture.
    See also: AWS API Documentation
    
    Examples
    Creates one or more virtual tapes.
    Expected Output:
    
    :example: response = client.create_tapes(
        GatewayARN='string',
        TapeSizeInBytes=123,
        ClientToken='string',
        NumTapesToCreate=123,
        TapeBarcodePrefix='string'
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]
            The unique Amazon Resource Name (ARN) that represents the gateway to associate the virtual tapes with. Use the ListGateways operation to return a list of gateways for your account and region.
            

    :type TapeSizeInBytes: integer
    :param TapeSizeInBytes: [REQUIRED]
            The size, in bytes, of the virtual tapes that you want to create.
            Note
            The size must be aligned by gigabyte (1024*1024*1024 byte).
            

    :type ClientToken: string
    :param ClientToken: [REQUIRED]
            A unique identifier that you use to retry a request. If you retry a request, use the same ClientToken you specified in the initial request.
            Note
            Using the same ClientToken prevents creating the tape multiple times.
            

    :type NumTapesToCreate: integer
    :param NumTapesToCreate: [REQUIRED]
            The number of virtual tapes that you want to create.
            

    :type TapeBarcodePrefix: string
    :param TapeBarcodePrefix: [REQUIRED]
            A prefix that you append to the barcode of the virtual tape you are creating. This prefix makes the barcode unique.
            Note
            The prefix must be 1 to 4 characters in length and must be one of the uppercase letters from A to Z.
            

    :rtype: dict
    :return: {
        'TapeARNs': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def delete_bandwidth_rate_limit(GatewayARN=None, BandwidthType=None):
    """
    Deletes the bandwidth rate limits of a gateway. You can delete either the upload and download bandwidth rate limit, or you can delete both. If you delete only one of the limits, the other limit remains unchanged. To specify which gateway to work with, use the Amazon Resource Name (ARN) of the gateway in your request.
    See also: AWS API Documentation
    
    Examples
    Deletes the bandwidth rate limits of a gateway; either the upload or download limit, or both.
    Expected Output:
    
    :example: response = client.delete_bandwidth_rate_limit(
        GatewayARN='string',
        BandwidthType='string'
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            

    :type BandwidthType: string
    :param BandwidthType: [REQUIRED]
            One of the BandwidthType values that indicates the gateway bandwidth rate limit to delete.
            Valid Values: Upload , Download , All .
            

    :rtype: dict
    :return: {
        'GatewayARN': 'string'
    }
    
    
    """
    pass

def delete_chap_credentials(TargetARN=None, InitiatorName=None):
    """
    Deletes Challenge-Handshake Authentication Protocol (CHAP) credentials for a specified iSCSI target and initiator pair.
    See also: AWS API Documentation
    
    Examples
    Deletes Challenge-Handshake Authentication Protocol (CHAP) credentials for a specified iSCSI target and initiator pair.
    Expected Output:
    
    :example: response = client.delete_chap_credentials(
        TargetARN='string',
        InitiatorName='string'
    )
    
    
    :type TargetARN: string
    :param TargetARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the iSCSI volume target. Use the DescribeStorediSCSIVolumes operation to return to retrieve the TargetARN for specified VolumeARN.
            

    :type InitiatorName: string
    :param InitiatorName: [REQUIRED]
            The iSCSI initiator that connects to the target.
            

    :rtype: dict
    :return: {
        'TargetARN': 'string',
        'InitiatorName': 'string'
    }
    
    
    """
    pass

def delete_file_share(FileShareARN=None):
    """
    Deletes a file share from a file gateway. This operation is only supported in the file gateway architecture.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_file_share(
        FileShareARN='string'
    )
    
    
    :type FileShareARN: string
    :param FileShareARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the file share to be deleted.
            

    :rtype: dict
    :return: {
        'FileShareARN': 'string'
    }
    
    
    """
    pass

def delete_gateway(GatewayARN=None):
    """
    Deletes a gateway. To specify which gateway to delete, use the Amazon Resource Name (ARN) of the gateway in your request. The operation deletes the gateway; however, it does not delete the gateway virtual machine (VM) from your host computer.
    After you delete a gateway, you cannot reactivate it. Completed snapshots of the gateway volumes are not deleted upon deleting the gateway, however, pending snapshots will not complete. After you delete a gateway, your next step is to remove it from your environment.
    See also: AWS API Documentation
    
    Examples
    This operation deletes the gateway, but not the gateway's VM from the host computer.
    Expected Output:
    
    :example: response = client.delete_gateway(
        GatewayARN='string'
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            

    :rtype: dict
    :return: {
        'GatewayARN': 'string'
    }
    
    
    """
    pass

def delete_snapshot_schedule(VolumeARN=None):
    """
    Deletes a snapshot of a volume.
    You can take snapshots of your gateway volumes on a scheduled or ad hoc basis. This API action enables you to delete a snapshot schedule for a volume. For more information, see Working with Snapshots . In the DeleteSnapshotSchedule request, you identify the volume by providing its Amazon Resource Name (ARN).
    See also: AWS API Documentation
    
    Examples
    This action enables you to delete a snapshot schedule for a volume.
    Expected Output:
    
    :example: response = client.delete_snapshot_schedule(
        VolumeARN='string'
    )
    
    
    :type VolumeARN: string
    :param VolumeARN: [REQUIRED]

    :rtype: dict
    :return: {
        'VolumeARN': 'string'
    }
    
    
    """
    pass

def delete_tape(GatewayARN=None, TapeARN=None):
    """
    Deletes the specified virtual tape. This operation is only supported in the tape gateway architecture.
    See also: AWS API Documentation
    
    Examples
    This example deletes the specified virtual tape.
    Expected Output:
    
    :example: response = client.delete_tape(
        GatewayARN='string',
        TapeARN='string'
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]
            The unique Amazon Resource Name (ARN) of the gateway that the virtual tape to delete is associated with. Use the ListGateways operation to return a list of gateways for your account and region.
            

    :type TapeARN: string
    :param TapeARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the virtual tape to delete.
            

    :rtype: dict
    :return: {
        'TapeARN': 'string'
    }
    
    
    """
    pass

def delete_tape_archive(TapeARN=None):
    """
    Deletes the specified virtual tape from the virtual tape shelf (VTS). This operation is only supported in the tape gateway architecture.
    See also: AWS API Documentation
    
    Examples
    Deletes the specified virtual tape from the virtual tape shelf (VTS).
    Expected Output:
    
    :example: response = client.delete_tape_archive(
        TapeARN='string'
    )
    
    
    :type TapeARN: string
    :param TapeARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the virtual tape to delete from the virtual tape shelf (VTS).
            

    :rtype: dict
    :return: {
        'TapeARN': 'string'
    }
    
    
    """
    pass

def delete_volume(VolumeARN=None):
    """
    Deletes the specified storage volume that you previously created using the  CreateCachediSCSIVolume or  CreateStorediSCSIVolume API. This operation is only supported in the cached volume and stored volume architectures. For stored volume gateways, the local disk that was configured as the storage volume is not deleted. You can reuse the local disk to create another storage volume.
    Before you delete a volume, make sure there are no iSCSI connections to the volume you are deleting. You should also make sure there is no snapshot in progress. You can use the Amazon Elastic Compute Cloud (Amazon EC2) API to query snapshots on the volume you are deleting and check the snapshot status. For more information, go to DescribeSnapshots in the Amazon Elastic Compute Cloud API Reference .
    In the request, you must provide the Amazon Resource Name (ARN) of the storage volume you want to delete.
    See also: AWS API Documentation
    
    Examples
    Deletes the specified gateway volume that you previously created using the CreateCachediSCSIVolume or CreateStorediSCSIVolume API.
    Expected Output:
    
    :example: response = client.delete_volume(
        VolumeARN='string'
    )
    
    
    :type VolumeARN: string
    :param VolumeARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the volume. Use the ListVolumes operation to return a list of gateway volumes.
            

    :rtype: dict
    :return: {
        'VolumeARN': 'string'
    }
    
    
    """
    pass

def describe_bandwidth_rate_limit(GatewayARN=None):
    """
    Returns the bandwidth rate limits of a gateway. By default, these limits are not set, which means no bandwidth rate limiting is in effect.
    This operation only returns a value for a bandwidth rate limit only if the limit is set. If no limits are set for the gateway, then this operation returns only the gateway ARN in the response body. To specify which gateway to describe, use the Amazon Resource Name (ARN) of the gateway in your request.
    See also: AWS API Documentation
    
    Examples
    Returns a value for a bandwidth rate limit if set. If not set, then only the gateway ARN is returned.
    Expected Output:
    
    :example: response = client.describe_bandwidth_rate_limit(
        GatewayARN='string'
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            

    :rtype: dict
    :return: {
        'GatewayARN': 'string',
        'AverageUploadRateLimitInBitsPerSec': 123,
        'AverageDownloadRateLimitInBitsPerSec': 123
    }
    
    
    """
    pass

def describe_cache(GatewayARN=None):
    """
    Returns information about the cache of a gateway. This operation is only supported in the cached volume,tape and file gateway architectures.
    The response includes disk IDs that are configured as cache, and it includes the amount of cache allocated and used.
    See also: AWS API Documentation
    
    Examples
    Returns information about the cache of a gateway.
    Expected Output:
    
    :example: response = client.describe_cache(
        GatewayARN='string'
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            

    :rtype: dict
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
    
    
    """
    pass

def describe_cached_iscsi_volumes(VolumeARNs=None):
    """
    Returns a description of the gateway volumes specified in the request. This operation is only supported in the cached volume gateway architecture.
    The list of gateway volumes in the request must be from one gateway. In the response Amazon Storage Gateway returns volume information sorted by volume Amazon Resource Name (ARN).
    See also: AWS API Documentation
    
    Examples
    Returns a description of the gateway cached iSCSI volumes specified in the request.
    Expected Output:
    
    :example: response = client.describe_cached_iscsi_volumes(
        VolumeARNs=[
            'string',
        ]
    )
    
    
    :type VolumeARNs: list
    :param VolumeARNs: [REQUIRED]
            (string) --
            

    :rtype: dict
    :return: {
        'CachediSCSIVolumes': [
            {
                'VolumeARN': 'string',
                'VolumeId': 'string',
                'VolumeType': 'string',
                'VolumeStatus': 'string',
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
                'CreatedDate': datetime(2015, 1, 1)
            },
        ]
    }
    
    
    """
    pass

def describe_chap_credentials(TargetARN=None):
    """
    Returns an array of Challenge-Handshake Authentication Protocol (CHAP) credentials information for a specified iSCSI target, one for each target-initiator pair.
    See also: AWS API Documentation
    
    Examples
    Returns an array of Challenge-Handshake Authentication Protocol (CHAP) credentials information for a specified iSCSI target, one for each target-initiator pair.
    Expected Output:
    
    :example: response = client.describe_chap_credentials(
        TargetARN='string'
    )
    
    
    :type TargetARN: string
    :param TargetARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the iSCSI volume target. Use the DescribeStorediSCSIVolumes operation to return to retrieve the TargetARN for specified VolumeARN.
            

    :rtype: dict
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
    
    
    """
    pass

def describe_gateway_information(GatewayARN=None):
    """
    Returns metadata about a gateway such as its name, network interfaces, configured time zone, and the state (whether the gateway is running or not). To specify which gateway to describe, use the Amazon Resource Name (ARN) of the gateway in your request.
    See also: AWS API Documentation
    
    Examples
    Returns metadata about a gateway such as its name, network interfaces, configured time zone, and the state (whether the gateway is running or not).
    Expected Output:
    
    :example: response = client.describe_gateway_information(
        GatewayARN='string'
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            

    :rtype: dict
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
        'LastSoftwareUpdate': 'string'
    }
    
    
    """
    pass

def describe_maintenance_start_time(GatewayARN=None):
    """
    Returns your gateway's weekly maintenance start time including the day and time of the week. Note that values are in terms of the gateway's time zone.
    See also: AWS API Documentation
    
    Examples
    Returns your gateway's weekly maintenance start time including the day and time of the week.
    Expected Output:
    
    :example: response = client.describe_maintenance_start_time(
        GatewayARN='string'
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            

    :rtype: dict
    :return: {
        'GatewayARN': 'string',
        'HourOfDay': 123,
        'MinuteOfHour': 123,
        'DayOfWeek': 123,
        'Timezone': 'string'
    }
    
    
    """
    pass

def describe_nfs_file_shares(FileShareARNList=None):
    """
    Gets a description for one or more file shares from a file gateway. This operation is only supported in file gateways.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_nfs_file_shares(
        FileShareARNList=[
            'string',
        ]
    )
    
    
    :type FileShareARNList: list
    :param FileShareARNList: [REQUIRED]
            An array containing the Amazon Resource Name (ARN) of each file share to be described.
            (string) --The Amazon Resource Name (ARN) of the file share.
            

    :rtype: dict
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
                'ClientList': [
                    'string',
                ],
                'Squash': 'string',
                'ReadOnly': True|False
            },
        ]
    }
    
    
    :returns: 
    "RootSquash" - Only root is mapped to anonymous user.
    "NoSquash" - No one is mapped to anonymous user
    "AllSquash" - Everyone is mapped to anonymous user.
    
    """
    pass

def describe_snapshot_schedule(VolumeARN=None):
    """
    Describes the snapshot schedule for the specified gateway volume. The snapshot schedule information includes intervals at which snapshots are automatically initiated on the volume. This operation is only supported in the cached volume and stored volume architectures.
    See also: AWS API Documentation
    
    Examples
    Describes the snapshot schedule for the specified gateway volume including intervals at which snapshots are automatically initiated.
    Expected Output:
    
    :example: response = client.describe_snapshot_schedule(
        VolumeARN='string'
    )
    
    
    :type VolumeARN: string
    :param VolumeARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the volume. Use the ListVolumes operation to return a list of gateway volumes.
            

    :rtype: dict
    :return: {
        'VolumeARN': 'string',
        'StartAt': 123,
        'RecurrenceInHours': 123,
        'Description': 'string',
        'Timezone': 'string'
    }
    
    
    """
    pass

def describe_stored_iscsi_volumes(VolumeARNs=None):
    """
    Returns the description of the gateway volumes specified in the request. The list of gateway volumes in the request must be from one gateway. In the response Amazon Storage Gateway returns volume information sorted by volume ARNs. This operation is only supported in stored volume gateway architecture.
    See also: AWS API Documentation
    
    Examples
    Returns the description of the gateway volumes specified in the request belonging to the same gateway.
    Expected Output:
    
    :example: response = client.describe_stored_iscsi_volumes(
        VolumeARNs=[
            'string',
        ]
    )
    
    
    :type VolumeARNs: list
    :param VolumeARNs: [REQUIRED]
            An array of strings where each string represents the Amazon Resource Name (ARN) of a stored volume. All of the specified stored volumes must from the same gateway. Use ListVolumes to get volume ARNs for a gateway.
            (string) --
            

    :rtype: dict
    :return: {
        'StorediSCSIVolumes': [
            {
                'VolumeARN': 'string',
                'VolumeId': 'string',
                'VolumeType': 'string',
                'VolumeStatus': 'string',
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
                'CreatedDate': datetime(2015, 1, 1)
            },
        ]
    }
    
    
    """
    pass

def describe_tape_archives(TapeARNs=None, Marker=None, Limit=None):
    """
    Returns a description of specified virtual tapes in the virtual tape shelf (VTS). This operation is only supported in the tape gateway architecture.
    If a specific TapeARN is not specified, AWS Storage Gateway returns a description of all virtual tapes found in the VTS associated with your account.
    See also: AWS API Documentation
    
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
    :param TapeARNs: Specifies one or more unique Amazon Resource Names (ARNs) that represent the virtual tapes you want to describe.
            (string) --
            

    :type Marker: string
    :param Marker: An opaque string that indicates the position at which to begin describing virtual tapes.

    :type Limit: integer
    :param Limit: Specifies that the number of virtual tapes descried be limited to the specified number.

    :rtype: dict
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
                'TapeUsedInBytes': 123
            },
        ],
        'Marker': 'string'
    }
    
    
    """
    pass

def describe_tape_recovery_points(GatewayARN=None, Marker=None, Limit=None):
    """
    Returns a list of virtual tape recovery points that are available for the specified tape gateway.
    A recovery point is a point-in-time view of a virtual tape at which all the data on the virtual tape is consistent. If your gateway crashes, virtual tapes that have recovery points can be recovered to a new gateway. This operation is only supported in the tape gateway architecture.
    See also: AWS API Documentation
    
    Examples
    Returns a list of virtual tape recovery points that are available for the specified gateway-VTL.
    Expected Output:
    
    :example: response = client.describe_tape_recovery_points(
        GatewayARN='string',
        Marker='string',
        Limit=123
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            

    :type Marker: string
    :param Marker: An opaque string that indicates the position at which to begin describing the virtual tape recovery points.

    :type Limit: integer
    :param Limit: Specifies that the number of virtual tape recovery points that are described be limited to the specified number.

    :rtype: dict
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
    
    
    """
    pass

def describe_tapes(GatewayARN=None, TapeARNs=None, Marker=None, Limit=None):
    """
    Returns a description of the specified Amazon Resource Name (ARN) of virtual tapes. If a TapeARN is not specified, returns a description of all virtual tapes associated with the specified gateway. This operation is only supported in the tape gateway architecture.
    See also: AWS API Documentation
    
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
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            

    :type TapeARNs: list
    :param TapeARNs: Specifies one or more unique Amazon Resource Names (ARNs) that represent the virtual tapes you want to describe. If this parameter is not specified, Tape gateway returns a description of all virtual tapes associated with the specified gateway.
            (string) --
            

    :type Marker: string
    :param Marker: A marker value, obtained in a previous call to DescribeTapes . This marker indicates which page of results to retrieve.
            If not specified, the first page of results is retrieved.
            

    :type Limit: integer
    :param Limit: Specifies that the number of virtual tapes described be limited to the specified number.
            Note
            Amazon Web Services may impose its own limit, if this field is not set.
            

    :rtype: dict
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
                'TapeUsedInBytes': 123
            },
        ],
        'Marker': 'string'
    }
    
    
    """
    pass

def describe_upload_buffer(GatewayARN=None):
    """
    Returns information about the upload buffer of a gateway. This operation is supported for the stored volume, cached volume and tape gateway architectures.
    The response includes disk IDs that are configured as upload buffer space, and it includes the amount of upload buffer space allocated and used.
    See also: AWS API Documentation
    
    Examples
    Returns information about the upload buffer of a gateway including disk IDs and the amount of upload buffer space allocated/used.
    Expected Output:
    Returns information about the upload buffer of a gateway including disk IDs and the amount of upload buffer space allocated and used.
    Expected Output:
    
    :example: response = client.describe_upload_buffer(
        GatewayARN='string'
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            

    :rtype: dict
    :return: {
        'GatewayARN': 'string',
        'DiskIds': [
            'string',
        ],
        'UploadBufferUsedInBytes': 123,
        'UploadBufferAllocatedInBytes': 123
    }
    
    
    """
    pass

def describe_vtl_devices(GatewayARN=None, VTLDeviceARNs=None, Marker=None, Limit=None):
    """
    Returns a description of virtual tape library (VTL) devices for the specified tape gateway. In the response, AWS Storage Gateway returns VTL device information.
    This operation is only supported in the tape gateway architecture.
    See also: AWS API Documentation
    
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
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            

    :type VTLDeviceARNs: list
    :param VTLDeviceARNs: An array of strings, where each string represents the Amazon Resource Name (ARN) of a VTL device.
            Note
            All of the specified VTL devices must be from the same gateway. If no VTL devices are specified, the result will contain all devices on the specified gateway.
            (string) --
            

    :type Marker: string
    :param Marker: An opaque string that indicates the position at which to begin describing the VTL devices.

    :type Limit: integer
    :param Limit: Specifies that the number of VTL devices described be limited to the specified number.

    :rtype: dict
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
    
    
    """
    pass

def describe_working_storage(GatewayARN=None):
    """
    Returns information about the working storage of a gateway. This operation is only supported in the stored volumes gateway architecture. This operation is deprecated in cached volumes API version (20120630). Use DescribeUploadBuffer instead.
    The response includes disk IDs that are configured as working storage, and it includes the amount of working storage allocated and used.
    See also: AWS API Documentation
    
    Examples
    This operation is supported only for the gateway-stored volume architecture. This operation is deprecated in cached-volumes API version (20120630). Use DescribeUploadBuffer instead.
    Expected Output:
    
    :example: response = client.describe_working_storage(
        GatewayARN='string'
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            

    :rtype: dict
    :return: {
        'GatewayARN': 'string',
        'DiskIds': [
            'string',
        ],
        'WorkingStorageUsedInBytes': 123,
        'WorkingStorageAllocatedInBytes': 123
    }
    
    
    """
    pass

def disable_gateway(GatewayARN=None):
    """
    Disables a tape gateway when the gateway is no longer functioning. For example, if your gateway VM is damaged, you can disable the gateway so you can recover virtual tapes.
    Use this operation for a tape gateway that is not reachable or not functioning. This operation is only supported in the tape gateway architectures.
    See also: AWS API Documentation
    
    Examples
    Disables a gateway when the gateway is no longer functioning. Use this operation for a gateway-VTL that is not reachable or not functioning.
    Expected Output:
    
    :example: response = client.disable_gateway(
        GatewayARN='string'
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            

    :rtype: dict
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

def list_file_shares(GatewayARN=None, Limit=None, Marker=None):
    """
    Gets a list of the file shares for a specific file gateway, or the list of file shares that belong to the calling user account. This operation is only supported in the file gateway architecture.
    See also: AWS API Documentation
    
    
    :example: response = client.list_file_shares(
        GatewayARN='string',
        Limit=123,
        Marker='string'
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: The Amazon resource Name (ARN) of the gateway whose file shares you want to list. If this field is not present, all file shares under your account are listed.

    :type Limit: integer
    :param Limit: The maximum number of file shares to return in the response. The value must be an integer with a value greater than zero. Optional.

    :type Marker: string
    :param Marker: Opaque pagination token returned from a previous ListFileShares operation. If present, Marker specifies where to continue the list from after a previous call to ListFileShares. Optional.

    :rtype: dict
    :return: {
        'Marker': 'string',
        'NextMarker': 'string',
        'FileShareInfoList': [
            {
                'FileShareARN': 'string',
                'FileShareId': 'string',
                'FileShareStatus': 'string',
                'GatewayARN': 'string'
            },
        ]
    }
    
    
    """
    pass

def list_gateways(Marker=None, Limit=None):
    """
    Lists gateways owned by an AWS account in a region specified in the request. The returned list is ordered by gateway Amazon Resource Name (ARN).
    By default, the operation returns a maximum of 100 gateways. This operation supports pagination that allows you to optionally reduce the number of gateways returned in a response.
    If you have more gateways than are returned in a response (that is, the response returns only a truncated list of your gateways), the response contains a marker that you can specify in your next request to fetch the next page of gateways.
    See also: AWS API Documentation
    
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
    :return: {
        'Gateways': [
            {
                'GatewayId': 'string',
                'GatewayARN': 'string',
                'GatewayType': 'string',
                'GatewayOperationalState': 'string',
                'GatewayName': 'string'
            },
        ],
        'Marker': 'string'
    }
    
    
    """
    pass

def list_local_disks(GatewayARN=None):
    """
    Returns a list of the gateway's local disks. To specify which gateway to describe, you use the Amazon Resource Name (ARN) of the gateway in the body of the request.
    The request returns a list of all disks, specifying which are configured as working storage, cache storage, or stored volume or not configured at all. The response includes a DiskStatus field. This field can have a value of present (the disk is available to use), missing (the disk is no longer connected to the gateway), or mismatch (the disk node is occupied by a disk that has incorrect metadata or the disk content is corrupted).
    See also: AWS API Documentation
    
    Examples
    The request returns a list of all disks, specifying which are configured as working storage, cache storage, or stored volume or not configured at all.
    Expected Output:
    
    :example: response = client.list_local_disks(
        GatewayARN='string'
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            

    :rtype: dict
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
                'DiskAllocationResource': 'string'
            },
        ]
    }
    
    
    """
    pass

def list_tags_for_resource(ResourceARN=None, Marker=None, Limit=None):
    """
    Lists the tags that have been added to the specified resource. This operation is only supported in the cached volume, stored volume and tape gateway architecture.
    See also: AWS API Documentation
    
    Examples
    Lists the tags that have been added to the specified resource.
    Expected Output:
    
    :example: response = client.list_tags_for_resource(
        ResourceARN='string',
        Marker='string',
        Limit=123
    )
    
    
    :type ResourceARN: string
    :param ResourceARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the resource for which you want to list tags.
            

    :type Marker: string
    :param Marker: An opaque string that indicates the position at which to begin returning the list of tags.

    :type Limit: integer
    :param Limit: Specifies that the list of tags returned be limited to the specified number of items.

    :rtype: dict
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
    (dict) --
    Key (string) --
    Value (string) --
    
    
    
    """
    pass

def list_tapes(TapeARNs=None, Marker=None, Limit=None):
    """
    Lists virtual tapes in your virtual tape library (VTL) and your virtual tape shelf (VTS). You specify the tapes to list by specifying one or more tape Amazon Resource Names (ARNs). If you don't specify a tape ARN, the operation lists all virtual tapes in both your VTL and VTS.
    This operation supports pagination. By default, the operation returns a maximum of up to 100 tapes. You can optionally specify the Limit parameter in the body to limit the number of tapes in the response. If the number of tapes returned in the response is truncated, the response includes a Marker element that you can use in your subsequent request to retrieve the next set of tapes. This operation is only supported in the tape gateway architecture.
    See also: AWS API Documentation
    
    
    :example: response = client.list_tapes(
        TapeARNs=[
            'string',
        ],
        Marker='string',
        Limit=123
    )
    
    
    :type TapeARNs: list
    :param TapeARNs: The Amazon Resource Name (ARN) of each of the tapes you want to list. If you don't specify a tape ARN, the response lists all tapes in both your VTL and VTS.
            (string) --
            

    :type Marker: string
    :param Marker: A string that indicates the position at which to begin the returned list of tapes.

    :type Limit: integer
    :param Limit: An optional number limit for the tapes in the list returned by this call.

    :rtype: dict
    :return: {
        'TapeInfos': [
            {
                'TapeARN': 'string',
                'TapeBarcode': 'string',
                'TapeSizeInBytes': 123,
                'TapeStatus': 'string',
                'GatewayARN': 'string'
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
    Lists iSCSI initiators that are connected to a volume. You can use this operation to determine whether a volume is being used or not. This operation is only supported in the cached volume and stored volume gateway architecture.
    See also: AWS API Documentation
    
    
    :example: response = client.list_volume_initiators(
        VolumeARN='string'
    )
    
    
    :type VolumeARN: string
    :param VolumeARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the volume. Use the ListVolumes operation to return a list of gateway volumes for the gateway.
            

    :rtype: dict
    :return: {
        'Initiators': [
            'string',
        ]
    }
    
    
    """
    pass

def list_volume_recovery_points(GatewayARN=None):
    """
    Lists the recovery points for a specified gateway. This operation is only supported in the cached volume gateway architecture.
    Each cache volume has one recovery point. A volume recovery point is a point in time at which all data of the volume is consistent and from which you can create a snapshot or clone a new cached volume from a source volume. To create a snapshot from a volume recovery point use the  CreateSnapshotFromVolumeRecoveryPoint operation.
    See also: AWS API Documentation
    
    Examples
    Lists the recovery points for a specified gateway in which all data of the volume is consistent and can be used to create a snapshot.
    Expected Output:
    
    :example: response = client.list_volume_recovery_points(
        GatewayARN='string'
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            

    :rtype: dict
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
    The operation supports pagination. By default, the operation returns a maximum of up to 100 volumes. You can optionally specify the Limit field in the body to limit the number of volumes in the response. If the number of volumes returned in the response is truncated, the response includes a Marker field. You can use this Marker value in your subsequent request to retrieve the next set of volumes. This operation is only supported in the cached volume and stored volume gateway architectures.
    See also: AWS API Documentation
    
    Examples
    Lists the iSCSI stored volumes of a gateway. Results are sorted by volume ARN up to a maximum of 100 volumes.
    Expected Output:
    
    :example: response = client.list_volumes(
        GatewayARN='string',
        Marker='string',
        Limit=123
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.

    :type Marker: string
    :param Marker: A string that indicates the position at which to begin the returned list of volumes. Obtain the marker from the response of a previous List iSCSI Volumes request.

    :type Limit: integer
    :param Limit: Specifies that the list of volumes returned be limited to the specified number of items.

    :rtype: dict
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
                'VolumeSizeInBytes': 123
            },
        ]
    }
    
    
    """
    pass

def refresh_cache(FileShareARN=None):
    """
    Refreshes the cache for the specified file share. This operation finds objects in the Amazon S3 bucket that were added or removed since the gateway last listed the bucket's contents and cached the results.
    See also: AWS API Documentation
    
    
    :example: response = client.refresh_cache(
        FileShareARN='string'
    )
    
    
    :type FileShareARN: string
    :param FileShareARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the file share.
            

    :rtype: dict
    :return: {
        'FileShareARN': 'string'
    }
    
    
    """
    pass

def remove_tags_from_resource(ResourceARN=None, TagKeys=None):
    """
    Removes one or more tags from the specified resource. This operation is only supported in the cached volume, stored volume and tape gateway architectures.
    See also: AWS API Documentation
    
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
    :param ResourceARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the resource you want to remove the tags from.
            

    :type TagKeys: list
    :param TagKeys: [REQUIRED]
            The keys of the tags you want to remove from the specified resource. A tag is composed of a key/value pair.
            (string) --
            

    :rtype: dict
    :return: {
        'ResourceARN': 'string'
    }
    
    
    """
    pass

def reset_cache(GatewayARN=None):
    """
    Resets all cache disks that have encountered a error and makes the disks available for reconfiguration as cache storage. If your cache disk encounters a error, the gateway prevents read and write operations on virtual tapes in the gateway. For example, an error can occur when a disk is corrupted or removed from the gateway. When a cache is reset, the gateway loses its cache storage. At this point you can reconfigure the disks as cache disks. This operation is only supported in the cached volume,tape and file gateway architectures.
    See also: AWS API Documentation
    
    Examples
    Resets all cache disks that have encountered a error and makes the disks available for reconfiguration as cache storage.
    Expected Output:
    
    :example: response = client.reset_cache(
        GatewayARN='string'
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            

    :rtype: dict
    :return: {
        'GatewayARN': 'string'
    }
    
    
    """
    pass

def retrieve_tape_archive(TapeARN=None, GatewayARN=None):
    """
    Retrieves an archived virtual tape from the virtual tape shelf (VTS) to a tape gateway. Virtual tapes archived in the VTS are not associated with any gateway. However after a tape is retrieved, it is associated with a gateway, even though it is also listed in the VTS, that is, archive. This operation is only supported in the tape gateway architecture.
    Once a tape is successfully retrieved to a gateway, it cannot be retrieved again to another gateway. You must archive the tape again before you can retrieve it to another gateway. This operation is only supported in the tape gateway architecture.
    See also: AWS API Documentation
    
    Examples
    Retrieves an archived virtual tape from the virtual tape shelf (VTS) to a gateway-VTL. Virtual tapes archived in the VTS are not associated with any gateway.
    Expected Output:
    
    :example: response = client.retrieve_tape_archive(
        TapeARN='string',
        GatewayARN='string'
    )
    
    
    :type TapeARN: string
    :param TapeARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the virtual tape you want to retrieve from the virtual tape shelf (VTS).
            

    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway you want to retrieve the virtual tape to. Use the ListGateways operation to return a list of gateways for your account and region.
            You retrieve archived virtual tapes to only one gateway and the gateway must be a tape gateway.
            

    :rtype: dict
    :return: {
        'TapeARN': 'string'
    }
    
    
    """
    pass

def retrieve_tape_recovery_point(TapeARN=None, GatewayARN=None):
    """
    Retrieves the recovery point for the specified virtual tape. This operation is only supported in the tape gateway architecture.
    A recovery point is a point in time view of a virtual tape at which all the data on the tape is consistent. If your gateway crashes, virtual tapes that have recovery points can be recovered to a new gateway.
    See also: AWS API Documentation
    
    Examples
    Retrieves the recovery point for the specified virtual tape.
    Expected Output:
    
    :example: response = client.retrieve_tape_recovery_point(
        TapeARN='string',
        GatewayARN='string'
    )
    
    
    :type TapeARN: string
    :param TapeARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the virtual tape for which you want to retrieve the recovery point.
            

    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            

    :rtype: dict
    :return: {
        'TapeARN': 'string'
    }
    
    
    """
    pass

def set_local_console_password(GatewayARN=None, LocalConsolePassword=None):
    """
    Sets the password for your VM local console. When you log in to the local console for the first time, you log in to the VM with the default credentials. We recommend that you set a new password. You don't need to know the default password to set a new password.
    See also: AWS API Documentation
    
    Examples
    Sets the password for your VM local console.
    Expected Output:
    
    :example: response = client.set_local_console_password(
        GatewayARN='string',
        LocalConsolePassword='string'
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            

    :type LocalConsolePassword: string
    :param LocalConsolePassword: [REQUIRED]
            The password you want to set for your VM local console.
            

    :rtype: dict
    :return: {
        'GatewayARN': 'string'
    }
    
    
    """
    pass

def shutdown_gateway(GatewayARN=None):
    """
    Shuts down a gateway. To specify which gateway to shut down, use the Amazon Resource Name (ARN) of the gateway in the body of your request.
    The operation shuts down the gateway service component running in the gateway's virtual machine (VM) and not the host VM.
    After the gateway is shutdown, you cannot call any other API except  StartGateway ,  DescribeGatewayInformation , and  ListGateways . For more information, see  ActivateGateway . Your applications cannot read from or write to the gateway's storage volumes, and there are no snapshots taken.
    If do not intend to use the gateway again, you must delete the gateway (using  DeleteGateway ) to no longer pay software charges associated with the gateway.
    See also: AWS API Documentation
    
    Examples
    This operation shuts down the gateway service component running in the storage gateway's virtual machine (VM) and not the VM.
    Expected Output:
    
    :example: response = client.shutdown_gateway(
        GatewayARN='string'
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            

    :rtype: dict
    :return: {
        'GatewayARN': 'string'
    }
    
    
    """
    pass

def start_gateway(GatewayARN=None):
    """
    Starts a gateway that you previously shut down (see  ShutdownGateway ). After the gateway starts, you can then make other API calls, your applications can read from or write to the gateway's storage volumes and you will be able to take snapshot backups.
    To specify which gateway to start, use the Amazon Resource Name (ARN) of the gateway in your request.
    See also: AWS API Documentation
    
    Examples
    Starts a gateway service that was previously shut down.
    Expected Output:
    
    :example: response = client.start_gateway(
        GatewayARN='string'
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            

    :rtype: dict
    :return: {
        'GatewayARN': 'string'
    }
    
    
    """
    pass

def update_bandwidth_rate_limit(GatewayARN=None, AverageUploadRateLimitInBitsPerSec=None, AverageDownloadRateLimitInBitsPerSec=None):
    """
    Updates the bandwidth rate limits of a gateway. You can update both the upload and download bandwidth rate limit or specify only one of the two. If you don't set a bandwidth rate limit, the existing rate limit remains.
    By default, a gateway's bandwidth rate limits are not set. If you don't set any limit, the gateway does not have any limitations on its bandwidth usage and could potentially use the maximum available bandwidth.
    To specify which gateway to update, use the Amazon Resource Name (ARN) of the gateway in your request.
    See also: AWS API Documentation
    
    Examples
    Updates the bandwidth rate limits of a gateway. Both the upload and download bandwidth rate limit can be set, or either one of the two. If a new limit is not set, the existing rate limit remains.
    Expected Output:
    
    :example: response = client.update_bandwidth_rate_limit(
        GatewayARN='string',
        AverageUploadRateLimitInBitsPerSec=123,
        AverageDownloadRateLimitInBitsPerSec=123
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            

    :type AverageUploadRateLimitInBitsPerSec: integer
    :param AverageUploadRateLimitInBitsPerSec: The average upload bandwidth rate limit in bits per second.

    :type AverageDownloadRateLimitInBitsPerSec: integer
    :param AverageDownloadRateLimitInBitsPerSec: The average download bandwidth rate limit in bits per second.

    :rtype: dict
    :return: {
        'GatewayARN': 'string'
    }
    
    
    """
    pass

def update_chap_credentials(TargetARN=None, SecretToAuthenticateInitiator=None, InitiatorName=None, SecretToAuthenticateTarget=None):
    """
    Updates the Challenge-Handshake Authentication Protocol (CHAP) credentials for a specified iSCSI target. By default, a gateway does not have CHAP enabled; however, for added security, you might use it.
    See also: AWS API Documentation
    
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
    :param TargetARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the iSCSI volume target. Use the DescribeStorediSCSIVolumes operation to return the TargetARN for specified VolumeARN.
            

    :type SecretToAuthenticateInitiator: string
    :param SecretToAuthenticateInitiator: [REQUIRED]
            The secret key that the initiator (for example, the Windows client) must provide to participate in mutual CHAP with the target.
            Note
            The secret key must be between 12 and 16 bytes when encoded in UTF-8.
            

    :type InitiatorName: string
    :param InitiatorName: [REQUIRED]
            The iSCSI initiator that connects to the target.
            

    :type SecretToAuthenticateTarget: string
    :param SecretToAuthenticateTarget: The secret key that the target must provide to participate in mutual CHAP with the initiator (e.g. Windows client).
            Byte constraints: Minimum bytes of 12. Maximum bytes of 16.
            Note
            The secret key must be between 12 and 16 bytes when encoded in UTF-8.
            

    :rtype: dict
    :return: {
        'TargetARN': 'string',
        'InitiatorName': 'string'
    }
    
    
    """
    pass

def update_gateway_information(GatewayARN=None, GatewayName=None, GatewayTimezone=None):
    """
    Updates a gateway's metadata, which includes the gateway's name and time zone. To specify which gateway to update, use the Amazon Resource Name (ARN) of the gateway in your request.
    See also: AWS API Documentation
    
    Examples
    Updates a gateway's metadata, which includes the gateway's name and time zone.
    Expected Output:
    
    :example: response = client.update_gateway_information(
        GatewayARN='string',
        GatewayName='string',
        GatewayTimezone='string'
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            

    :type GatewayName: string
    :param GatewayName: The name you configured for your gateway.

    :type GatewayTimezone: string
    :param GatewayTimezone: 

    :rtype: dict
    :return: {
        'GatewayARN': 'string',
        'GatewayName': 'string'
    }
    
    
    """
    pass

def update_gateway_software_now(GatewayARN=None):
    """
    Updates the gateway virtual machine (VM) software. The request immediately triggers the software update.
    See also: AWS API Documentation
    
    Examples
    Updates the gateway virtual machine (VM) software. The request immediately triggers the software update.
    Expected Output:
    
    :example: response = client.update_gateway_software_now(
        GatewayARN='string'
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            

    :rtype: dict
    :return: {
        'GatewayARN': 'string'
    }
    
    
    """
    pass

def update_maintenance_start_time(GatewayARN=None, HourOfDay=None, MinuteOfHour=None, DayOfWeek=None):
    """
    Updates a gateway's weekly maintenance start time information, including day and time of the week. The maintenance time is the time in your gateway's time zone.
    See also: AWS API Documentation
    
    Examples
    Updates a gateway's weekly maintenance start time information, including day and time of the week. The maintenance time is in your gateway's time zone.
    Expected Output:
    
    :example: response = client.update_maintenance_start_time(
        GatewayARN='string',
        HourOfDay=123,
        MinuteOfHour=123,
        DayOfWeek=123
    )
    
    
    :type GatewayARN: string
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            

    :type HourOfDay: integer
    :param HourOfDay: [REQUIRED]
            The hour component of the maintenance start time represented as hh , where hh is the hour (00 to 23). The hour of the day is in the time zone of the gateway.
            

    :type MinuteOfHour: integer
    :param MinuteOfHour: [REQUIRED]
            The minute component of the maintenance start time represented as mm , where mm is the minute (00 to 59). The minute of the hour is in the time zone of the gateway.
            

    :type DayOfWeek: integer
    :param DayOfWeek: [REQUIRED]
            The maintenance start time day of the week represented as an ordinal number from 0 to 6, where 0 represents Sunday and 6 Saturday.
            

    :rtype: dict
    :return: {
        'GatewayARN': 'string'
    }
    
    
    """
    pass

def update_nfs_file_share(FileShareARN=None, KMSEncrypted=None, KMSKey=None, NFSFileShareDefaults=None, DefaultStorageClass=None, ClientList=None, Squash=None, ReadOnly=None):
    """
    Updates a file share. This operation is only supported in the file gateway architecture.
    Updates the following file share setting:
    See also: AWS API Documentation
    
    
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
        ClientList=[
            'string',
        ],
        Squash='string',
        ReadOnly=True|False
    )
    
    
    :type FileShareARN: string
    :param FileShareARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the file share to be updated.
            

    :type KMSEncrypted: boolean
    :param KMSEncrypted: True to use Amazon S3 server side encryption with your own AWS KMS key, or false to use a key managed by Amazon S3. Optional.

    :type KMSKey: string
    :param KMSKey: The KMS key used for Amazon S3 server side encryption. This value can only be set when KmsEncrypted is true. Optional.

    :type NFSFileShareDefaults: dict
    :param NFSFileShareDefaults: The default values for the file share. Optional.
            FileMode (string) --The Unix file mode in the form 'nnnn'. For example, '0666' represents the default file mode inside the file share. The default value is 0666.
            DirectoryMode (string) --The Unix directory mode in the form 'nnnn'. For example, '0666' represents the default access mode for all directories inside the file share. The default value is 0777.
            GroupId (integer) --The default group ID for the file share (unless the files have another group ID specified). The default value is nfsnobody.
            OwnerId (integer) --The default owner ID for files in the file share (unless the files have another owner ID specified). The default value is nfsnobody.
            

    :type DefaultStorageClass: string
    :param DefaultStorageClass: The default storage class for objects put into an Amazon S3 bucket by a file gateway. Possible values are S3_STANDARD or S3_STANDARD_IA. If this field is not populated, the default value S3_STANDARD is used. Optional.

    :type ClientList: list
    :param ClientList: The list of clients that are allowed to access the file gateway. The list must contain either valid IP addresses or valid CIDR blocks.
            (string) --
            

    :type Squash: string
    :param Squash: The user mapped to anonymous user. Valid options are the following:
            'RootSquash' - Only root is mapped to anonymous user.
            'NoSquash' - No one is mapped to anonymous user
            'AllSquash' - Everyone is mapped to anonymous user.
            

    :type ReadOnly: boolean
    :param ReadOnly: Sets the write status of a file share: 'true' if the write status is read-only, and otherwise 'false'.

    :rtype: dict
    :return: {
        'FileShareARN': 'string'
    }
    
    
    :returns: 
    FileShareARN (string) -- [REQUIRED]
    The Amazon Resource Name (ARN) of the file share to be updated.
    
    KMSEncrypted (boolean) -- True to use Amazon S3 server side encryption with your own AWS KMS key, or false to use a key managed by Amazon S3. Optional.
    KMSKey (string) -- The KMS key used for Amazon S3 server side encryption. This value can only be set when KmsEncrypted is true. Optional.
    NFSFileShareDefaults (dict) -- The default values for the file share. Optional.
    
    FileMode (string) --The Unix file mode in the form "nnnn". For example, "0666" represents the default file mode inside the file share. The default value is 0666.
    
    DirectoryMode (string) --The Unix directory mode in the form "nnnn". For example, "0666" represents the default access mode for all directories inside the file share. The default value is 0777.
    
    GroupId (integer) --The default group ID for the file share (unless the files have another group ID specified). The default value is nfsnobody.
    
    OwnerId (integer) --The default owner ID for files in the file share (unless the files have another owner ID specified). The default value is nfsnobody.
    
    
    
    DefaultStorageClass (string) -- The default storage class for objects put into an Amazon S3 bucket by a file gateway. Possible values are S3_STANDARD or S3_STANDARD_IA. If this field is not populated, the default value S3_STANDARD is used. Optional.
    ClientList (list) -- The list of clients that are allowed to access the file gateway. The list must contain either valid IP addresses or valid CIDR blocks.
    
    (string) --
    
    
    Squash (string) -- The user mapped to anonymous user. Valid options are the following:
    
    "RootSquash" - Only root is mapped to anonymous user.
    "NoSquash" - No one is mapped to anonymous user
    "AllSquash" - Everyone is mapped to anonymous user.
    
    
    ReadOnly (boolean) -- Sets the write status of a file share: "true" if the write status is read-only, and otherwise "false".
    
    """
    pass

def update_snapshot_schedule(VolumeARN=None, StartAt=None, RecurrenceInHours=None, Description=None):
    """
    Updates a snapshot schedule configured for a gateway volume. This operation is only supported in the cached volume and stored volume gateway architectures.
    The default snapshot schedule for volume is once every 24 hours, starting at the creation time of the volume. You can use this API to change the snapshot schedule configured for the volume.
    In the request you must identify the gateway volume whose snapshot schedule you want to update, and the schedule information, including when you want the snapshot to begin on a day and the frequency (in hours) of snapshots.
    See also: AWS API Documentation
    
    Examples
    Updates a snapshot schedule configured for a gateway volume.
    Expected Output:
    
    :example: response = client.update_snapshot_schedule(
        VolumeARN='string',
        StartAt=123,
        RecurrenceInHours=123,
        Description='string'
    )
    
    
    :type VolumeARN: string
    :param VolumeARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the volume. Use the ListVolumes operation to return a list of gateway volumes.
            

    :type StartAt: integer
    :param StartAt: [REQUIRED]
            The hour of the day at which the snapshot schedule begins represented as hh , where hh is the hour (0 to 23). The hour of the day is in the time zone of the gateway.
            

    :type RecurrenceInHours: integer
    :param RecurrenceInHours: [REQUIRED]
            Frequency of snapshots. Specify the number of hours between snapshots.
            

    :type Description: string
    :param Description: Optional description of the snapshot that overwrites the existing description.

    :rtype: dict
    :return: {
        'VolumeARN': 'string'
    }
    
    
    :returns: 
    VolumeARN (string) --
    
    """
    pass

def update_vtl_device_type(VTLDeviceARN=None, DeviceType=None):
    """
    Updates the type of medium changer in a tape gateway. When you activate a tape gateway, you select a medium changer type for the tape gateway. This operation enables you to select a different type of medium changer after a tape gateway is activated. This operation is only supported in the tape gateway architecture.
    See also: AWS API Documentation
    
    Examples
    Updates the type of medium changer in a gateway-VTL after a gateway-VTL is activated.
    Expected Output:
    
    :example: response = client.update_vtl_device_type(
        VTLDeviceARN='string',
        DeviceType='string'
    )
    
    
    :type VTLDeviceARN: string
    :param VTLDeviceARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the medium changer you want to select.
            

    :type DeviceType: string
    :param DeviceType: [REQUIRED]
            The type of medium changer you want to select.
            Valid Values: 'STK-L700', 'AWS-Gateway-VTL'
            

    :rtype: dict
    :return: {
        'VTLDeviceARN': 'string'
    }
    
    
    """
    pass

