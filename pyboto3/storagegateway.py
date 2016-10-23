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


def activate_gateway(ActivationKey=None, GatewayName=None, GatewayTimezone=None, GatewayRegion=None, GatewayType=None,
                     TapeDriveType=None, MediumChangerType=None):
    """
    :param ActivationKey: [REQUIRED]
            Your gateway activation key. You can obtain the activation key by sending an HTTP GET request with redirects enabled to the gateway IP address (port 80). The redirect URL returned in the response provides you the activation key for your gateway in the query string parameter activationKey . It may also include other activation-related parameters, however, these are merely defaults -- the arguments you pass to the ActivateGateway API call determine the actual configuration of your gateway.
            
    :type ActivationKey: string
    :param GatewayName: [REQUIRED]
            The name you configured for your gateway.
            
    :type GatewayName: string
    :param GatewayTimezone: [REQUIRED]
            A value that indicates the time zone you want to set for the gateway. The time zone is used, for example, for scheduling snapshots and your gateway's maintenance schedule.
            
    :type GatewayTimezone: string
    :param GatewayRegion: [REQUIRED]
            A value that indicates the region where you want to store the snapshot backups. The gateway region specified must be the same region as the region in your Host header in the request. For more information about available regions and endpoints for AWS Storage Gateway, see Regions and Endpoints in the Amazon Web Services Glossary .
            Valid Values: 'us-east-1', 'us-west-1', 'us-west-2', 'eu-west-1', 'eu-central-1', 'ap-northeast-1', 'ap-northeast-2', 'ap-southeast-1', 'ap-southeast-2', 'sa-east-1'
            
    :type GatewayRegion: string
    :param GatewayType: A value that defines the type of gateway to activate. The type specified is critical to all later functions of the gateway and cannot be changed after activation. The default value is STORED .
    :type GatewayType: string
    :param TapeDriveType: The value that indicates the type of tape drive to use for gateway-VTL. This field is optional.
            Valid Values: 'IBM-ULT3580-TD5'
            
    :type TapeDriveType: string
    :param MediumChangerType: The value that indicates the type of medium changer to use for gateway-VTL. This field is optional.
            Valid Values: 'STK-L700', 'AWS-Gateway-VTL'
            
    :type MediumChangerType: string
    """
    pass


def add_cache(GatewayARN=None, DiskIds=None):
    """
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            
    :type GatewayARN: string
    :param DiskIds: [REQUIRED]
            (string) --
            
    :type DiskIds: list
    """
    pass


def add_tags_to_resource(ResourceARN=None, Tags=None):
    """
    :param ResourceARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the resource you want to add tags to.
            
    :type ResourceARN: string
    :param Tags: [REQUIRED]
            The key-value pair that represents the tag you want to add to the resource. The value can be an empty string.
            Note
            Valid characters for key and value are letters, spaces, and numbers representable in UTF-8 format, and the following special characters: + - = . _ : / @.
            (dict) --
            Key (string) -- [REQUIRED]
            Value (string) -- [REQUIRED]
            
    :type Tags: list
    """
    pass


def add_upload_buffer(GatewayARN=None, DiskIds=None):
    """
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            
    :type GatewayARN: string
    :param DiskIds: [REQUIRED]
            (string) --
            
    :type DiskIds: list
    """
    pass


def add_working_storage(GatewayARN=None, DiskIds=None):
    """
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            
    :type GatewayARN: string
    :param DiskIds: [REQUIRED]
            An array of strings that identify disks that are to be configured as working storage. Each string have a minimum length of 1 and maximum length of 300. You can get the disk IDs from the ListLocalDisks API.
            (string) --
            
    :type DiskIds: list
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


def cancel_archival(GatewayARN=None, TapeARN=None):
    """
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            
    :type GatewayARN: string
    :param TapeARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the virtual tape you want to cancel archiving for.
            
    :type TapeARN: string
    """
    pass


def cancel_retrieval(GatewayARN=None, TapeARN=None):
    """
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            
    :type GatewayARN: string
    :param TapeARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the virtual tape you want to cancel retrieval for.
            
    :type TapeARN: string
    """
    pass


def create_cached_iscsi_volume(GatewayARN=None, VolumeSizeInBytes=None, SnapshotId=None, TargetName=None,
                               NetworkInterfaceId=None, ClientToken=None):
    """
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            
    :type GatewayARN: string
    :param VolumeSizeInBytes: [REQUIRED]
    :type VolumeSizeInBytes: integer
    :param SnapshotId: 
    :type SnapshotId: string
    :param TargetName: [REQUIRED]
    :type TargetName: string
    :param NetworkInterfaceId: [REQUIRED]
    :type NetworkInterfaceId: string
    :param ClientToken: [REQUIRED]
    :type ClientToken: string
    """
    pass


def create_snapshot(VolumeARN=None, SnapshotDescription=None):
    """
    :param VolumeARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the volume. Use the ListVolumes operation to return a list of gateway volumes.
            
    :type VolumeARN: string
    :param SnapshotDescription: [REQUIRED]
            Textual description of the snapshot that appears in the Amazon EC2 console, Elastic Block Store snapshots panel in the Description field, and in the AWS Storage Gateway snapshot Details pane, Description field
            
    :type SnapshotDescription: string
    """
    pass


def create_snapshot_from_volume_recovery_point(VolumeARN=None, SnapshotDescription=None):
    """
    :param VolumeARN: [REQUIRED]
    :type VolumeARN: string
    :param SnapshotDescription: [REQUIRED]
    :type SnapshotDescription: string
    """
    pass


def create_stored_iscsi_volume(GatewayARN=None, DiskId=None, SnapshotId=None, PreserveExistingData=None,
                               TargetName=None, NetworkInterfaceId=None):
    """
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            
    :type GatewayARN: string
    :param DiskId: [REQUIRED]
            The unique identifier for the gateway local disk that is configured as a stored volume. Use ListLocalDisks to list disk IDs for a gateway.
            
    :type DiskId: string
    :param SnapshotId: The snapshot ID (e.g. 'snap-1122aabb') of the snapshot to restore as the new stored volume. Specify this field if you want to create the iSCSI storage volume from a snapshot otherwise do not include this field. To list snapshots for your account use DescribeSnapshots in the Amazon Elastic Compute Cloud API Reference .
    :type SnapshotId: string
    :param PreserveExistingData: [REQUIRED]
            Specify this field as true if you want to preserve the data on the local disk. Otherwise, specifying this field as false creates an empty volume.
            Valid Values: true, false
            
    :type PreserveExistingData: boolean
    :param TargetName: [REQUIRED]
            The name of the iSCSI target used by initiators to connect to the target and as a suffix for the target ARN. For example, specifying TargetName as myvolume results in the target ARN of arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-12A3456B/target/iqn.1997-05.com.amazon:myvolume. The target name must be unique across all volumes of a gateway.
            
    :type TargetName: string
    :param NetworkInterfaceId: [REQUIRED]
            The network interface of the gateway on which to expose the iSCSI target. Only IPv4 addresses are accepted. Use DescribeGatewayInformation to get a list of the network interfaces available on a gateway.
            Valid Values: A valid IP address.
            
    :type NetworkInterfaceId: string
    """
    pass


def create_tape_with_barcode(GatewayARN=None, TapeSizeInBytes=None, TapeBarcode=None):
    """
    :param GatewayARN: [REQUIRED]
            The unique Amazon Resource Name (ARN) that represents the gateway to associate the virtual tape with. Use the ListGateways operation to return a list of gateways for your account and region.
            
    :type GatewayARN: string
    :param TapeSizeInBytes: [REQUIRED]
            The size, in bytes, of the virtual tape that you want to create.
            Note
            The size must be aligned by gigabyte (1024*1024*1024 byte).
            
    :type TapeSizeInBytes: integer
    :param TapeBarcode: [REQUIRED]
            The barcode that you want to assign to the tape.
            
    :type TapeBarcode: string
    """
    pass


def create_tapes(GatewayARN=None, TapeSizeInBytes=None, ClientToken=None, NumTapesToCreate=None,
                 TapeBarcodePrefix=None):
    """
    :param GatewayARN: [REQUIRED]
            The unique Amazon Resource Name (ARN) that represents the gateway to associate the virtual tapes with. Use the ListGateways operation to return a list of gateways for your account and region.
            
    :type GatewayARN: string
    :param TapeSizeInBytes: [REQUIRED]
            The size, in bytes, of the virtual tapes that you want to create.
            Note
            The size must be aligned by gigabyte (1024*1024*1024 byte).
            
    :type TapeSizeInBytes: integer
    :param ClientToken: [REQUIRED]
            A unique identifier that you use to retry a request. If you retry a request, use the same ClientToken you specified in the initial request.
            Note
            Using the same ClientToken prevents creating the tape multiple times.
            
    :type ClientToken: string
    :param NumTapesToCreate: [REQUIRED]
            The number of virtual tapes that you want to create.
            
    :type NumTapesToCreate: integer
    :param TapeBarcodePrefix: [REQUIRED]
            A prefix that you append to the barcode of the virtual tape you are creating. This prefix makes the barcode unique.
            Note
            The prefix must be 1 to 4 characters in length and must be one of the uppercase letters from A to Z.
            
    :type TapeBarcodePrefix: string
    """
    pass


def delete_bandwidth_rate_limit(GatewayARN=None, BandwidthType=None):
    """
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            
    :type GatewayARN: string
    :param BandwidthType: [REQUIRED]
    :type BandwidthType: string
    """
    pass


def delete_chap_credentials(TargetARN=None, InitiatorName=None):
    """
    :param TargetARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the iSCSI volume target. Use the DescribeStorediSCSIVolumes operation to return to retrieve the TargetARN for specified VolumeARN.
            
    :type TargetARN: string
    :param InitiatorName: [REQUIRED]
            The iSCSI initiator that connects to the target.
            
    :type InitiatorName: string
    """
    pass


def delete_gateway(GatewayARN=None):
    """
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            Return typedict
            ReturnsResponse Syntax{
              'GatewayARN': 'string'
            }
            Response Structure
            (dict) --A JSON object containing the id of the deleted gateway.
            GatewayARN (string) --The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            
            
    :type GatewayARN: string
    """
    pass


def delete_snapshot_schedule(VolumeARN=None):
    """
    :param VolumeARN: [REQUIRED]
            Return typedict
            ReturnsResponse Syntax{
              'VolumeARN': 'string'
            }
            Response Structure
            (dict) --
            VolumeARN (string) --
            
            
    :type VolumeARN: string
    """
    pass


def delete_tape(GatewayARN=None, TapeARN=None):
    """
    :param GatewayARN: [REQUIRED]
            The unique Amazon Resource Name (ARN) of the gateway that the virtual tape to delete is associated with. Use the ListGateways operation to return a list of gateways for your account and region.
            
    :type GatewayARN: string
    :param TapeARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the virtual tape to delete.
            
    :type TapeARN: string
    """
    pass


def delete_tape_archive(TapeARN=None):
    """
    :param TapeARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the virtual tape to delete from the virtual tape shelf (VTS).
            Return typedict
            ReturnsResponse Syntax{
              'TapeARN': 'string'
            }
            Response Structure
            (dict) --DeleteTapeArchiveOutput
            TapeARN (string) --The Amazon Resource Name (ARN) of the virtual tape that was deleted from the virtual tape shelf (VTS).
            
            
    :type TapeARN: string
    """
    pass


def delete_volume(VolumeARN=None):
    """
    :param VolumeARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the volume. Use the ListVolumes operation to return a list of gateway volumes.
            Return typedict
            ReturnsResponse Syntax{
              'VolumeARN': 'string'
            }
            Response Structure
            (dict) --A JSON object containing the of the storage volume that was deleted
            VolumeARN (string) --The Amazon Resource Name (ARN) of the storage volume that was deleted. It is the same ARN you provided in the request.
            
            
    :type VolumeARN: string
    """
    pass


def describe_bandwidth_rate_limit(GatewayARN=None):
    """
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            Return typedict
            ReturnsResponse Syntax{
              'GatewayARN': 'string',
              'AverageUploadRateLimitInBitsPerSec': 123,
              'AverageDownloadRateLimitInBitsPerSec': 123
            }
            Response Structure
            (dict) --A JSON object containing the following fields:
            GatewayARN (string) --The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            AverageUploadRateLimitInBitsPerSec (integer) --The average upload bandwidth rate limit in bits per second. This field does not appear in the response if the upload rate limit is not set.
            AverageDownloadRateLimitInBitsPerSec (integer) --The average download bandwidth rate limit in bits per second. This field does not appear in the response if the download rate limit is not set.
            
            
    :type GatewayARN: string
    """
    pass


def describe_cache(GatewayARN=None):
    """
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            Return typedict
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
            GatewayARN (string) --The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            DiskIds (list) --
            (string) --
            CacheAllocatedInBytes (integer) --
            CacheUsedPercentage (float) --
            CacheDirtyPercentage (float) --
            CacheHitPercentage (float) --
            CacheMissPercentage (float) --
            
            
    :type GatewayARN: string
    """
    pass


def describe_cached_iscsi_volumes(VolumeARNs=None):
    """
    :param VolumeARNs: [REQUIRED]
            (string) --
            Return typedict
            ReturnsResponse Syntax{
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
                  }
                },
              ]
            }
            Response Structure
            (dict) --A JSON object containing the following fields:
            CachediSCSIVolumes (list) --An array of objects where each object contains metadata about one cached volume.
            (dict) --
            VolumeARN (string) --
            VolumeId (string) --
            VolumeType (string) --
            VolumeStatus (string) --
            VolumeSizeInBytes (integer) --
            VolumeProgress (float) --
            SourceSnapshotId (string) --
            VolumeiSCSIAttributes (dict) --Lists iSCSI information about a volume.
            TargetARN (string) --The Amazon Resource Name (ARN) of the volume target.
            NetworkInterfaceId (string) --The network interface identifier.
            NetworkInterfacePort (integer) --The port used to communicate with iSCSI targets.
            LunNumber (integer) --The logical disk number.
            ChapEnabled (boolean) --Indicates whether mutual CHAP is enabled for the iSCSI target.
            
            
            
            
    :type VolumeARNs: list
    """
    pass


def describe_chap_credentials(TargetARN=None):
    """
    :param TargetARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the iSCSI volume target. Use the DescribeStorediSCSIVolumes operation to return to retrieve the TargetARN for specified VolumeARN.
            Return typedict
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
            ChapCredentials (list) --An array of ChapInfo objects that represent CHAP credentials. Each object in the array contains CHAP credential information for one target-initiator pair. If no CHAP credentials are set, an empty array is returned. CHAP credential information is provided in a JSON object with the following fields:
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
            
            
            
    :type TargetARN: string
    """
    pass


def describe_gateway_information(GatewayARN=None):
    """
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            Return typedict
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
              'LastSoftwareUpdate': 'string'
            }
            Response Structure
            (dict) --A JSON object containing the following fields:
            GatewayARN (string) --The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            GatewayId (string) --The unique identifier assigned to your gateway during activation. This ID becomes part of the gateway Amazon Resource Name (ARN), which you use as input for other operations.
            GatewayName (string) --The name you configured for your gateway.
            GatewayTimezone (string) --A value that indicates the time zone configured for the gateway.
            GatewayState (string) --A value that indicates the operating state of the gateway.
            GatewayNetworkInterfaces (list) --A NetworkInterface array that contains descriptions of the gateway network interfaces.
            (dict) --Describes a gateway's network interface.
            Ipv4Address (string) --The Internet Protocol version 4 (IPv4) address of the interface.
            MacAddress (string) --The Media Access Control (MAC) address of the interface.
            Note
            This is currently unsupported and will not be returned in output.
            Ipv6Address (string) --The Internet Protocol version 6 (IPv6) address of the interface. Currently not supported .
            
            GatewayType (string) --The type of the gateway.
            NextUpdateAvailabilityDate (string) --The date on which an update to the gateway is available. This date is in the time zone of the gateway. If the gateway is not available for an update this field is not returned in the response.
            LastSoftwareUpdate (string) --The date on which the last software update was applied to the gateway. If the gateway has never been updated, this field does not return a value in the response.
            
            
    :type GatewayARN: string
    """
    pass


def describe_maintenance_start_time(GatewayARN=None):
    """
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            Return typedict
            ReturnsResponse Syntax{
              'GatewayARN': 'string',
              'HourOfDay': 123,
              'MinuteOfHour': 123,
              'DayOfWeek': 123,
              'Timezone': 'string'
            }
            Response Structure
            (dict) --
            GatewayARN (string) --The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            HourOfDay (integer) --
            MinuteOfHour (integer) --
            DayOfWeek (integer) --
            Timezone (string) --
            
            
    :type GatewayARN: string
    """
    pass


def describe_snapshot_schedule(VolumeARN=None):
    """
    :param VolumeARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the volume. Use the ListVolumes operation to return a list of gateway volumes.
            Return typedict
            ReturnsResponse Syntax{
              'VolumeARN': 'string',
              'StartAt': 123,
              'RecurrenceInHours': 123,
              'Description': 'string',
              'Timezone': 'string'
            }
            Response Structure
            (dict) --
            VolumeARN (string) --
            StartAt (integer) --
            RecurrenceInHours (integer) --
            Description (string) --
            Timezone (string) --
            
            
    :type VolumeARN: string
    """
    pass


def describe_stored_iscsi_volumes(VolumeARNs=None):
    """
    :param VolumeARNs: [REQUIRED]
            An array of strings where each string represents the Amazon Resource Name (ARN) of a stored volume. All of the specified stored volumes must from the same gateway. Use ListVolumes to get volume ARNs for a gateway.
            (string) --
            Return typedict
            ReturnsResponse Syntax{
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
                  }
                },
              ]
            }
            Response Structure
            (dict) --
            StorediSCSIVolumes (list) --
            (dict) --
            VolumeARN (string) --
            VolumeId (string) --
            VolumeType (string) --
            VolumeStatus (string) --
            VolumeSizeInBytes (integer) --
            VolumeProgress (float) --
            VolumeDiskId (string) --
            SourceSnapshotId (string) --
            PreservedExistingData (boolean) --
            VolumeiSCSIAttributes (dict) --Lists iSCSI information about a volume.
            TargetARN (string) --The Amazon Resource Name (ARN) of the volume target.
            NetworkInterfaceId (string) --The network interface identifier.
            NetworkInterfacePort (integer) --The port used to communicate with iSCSI targets.
            LunNumber (integer) --The logical disk number.
            ChapEnabled (boolean) --Indicates whether mutual CHAP is enabled for the iSCSI target.
            
            
            
            
    :type VolumeARNs: list
    """
    pass


def describe_tape_archives(TapeARNs=None, Marker=None, Limit=None):
    """
    :param TapeARNs: Specifies one or more unique Amazon Resource Names (ARNs) that represent the virtual tapes you want to describe.
            (string) --
            
    :type TapeARNs: list
    :param Marker: An opaque string that indicates the position at which to begin describing virtual tapes.
    :type Marker: string
    :param Limit: Specifies that the number of virtual tapes descried be limited to the specified number.
    :type Limit: integer
    """
    pass


def describe_tape_recovery_points(GatewayARN=None, Marker=None, Limit=None):
    """
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            
    :type GatewayARN: string
    :param Marker: An opaque string that indicates the position at which to begin describing the virtual tape recovery points.
    :type Marker: string
    :param Limit: Specifies that the number of virtual tape recovery points that are described be limited to the specified number.
    :type Limit: integer
    """
    pass


def describe_tapes(GatewayARN=None, TapeARNs=None, Marker=None, Limit=None):
    """
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            
    :type GatewayARN: string
    :param TapeARNs: Specifies one or more unique Amazon Resource Names (ARNs) that represent the virtual tapes you want to describe. If this parameter is not specified, AWS Storage Gateway returns a description of all virtual tapes associated with the specified gateway.
            (string) --
            
    :type TapeARNs: list
    :param Marker: A marker value, obtained in a previous call to DescribeTapes . This marker indicates which page of results to retrieve.
            If not specified, the first page of results is retrieved.
            
    :type Marker: string
    :param Limit: Specifies that the number of virtual tapes described be limited to the specified number.
            Note
            Amazon Web Services may impose its own limit, if this field is not set.
            
    :type Limit: integer
    """
    pass


def describe_upload_buffer(GatewayARN=None):
    """
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            Return typedict
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
            GatewayARN (string) --The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            DiskIds (list) --
            (string) --
            UploadBufferUsedInBytes (integer) --
            UploadBufferAllocatedInBytes (integer) --
            
            
    :type GatewayARN: string
    """
    pass


def describe_vtl_devices(GatewayARN=None, VTLDeviceARNs=None, Marker=None, Limit=None):
    """
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            
    :type GatewayARN: string
    :param VTLDeviceARNs: An array of strings, where each string represents the Amazon Resource Name (ARN) of a VTL device.
            Note
            All of the specified VTL devices must be from the same gateway. If no VTL devices are specified, the result will contain all devices on the specified gateway.
            (string) --
            
    :type VTLDeviceARNs: list
    :param Marker: An opaque string that indicates the position at which to begin describing the VTL devices.
    :type Marker: string
    :param Limit: Specifies that the number of VTL devices described be limited to the specified number.
    :type Limit: integer
    """
    pass


def describe_working_storage(GatewayARN=None):
    """
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            Return typedict
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
            GatewayARN (string) --The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            DiskIds (list) --An array of the gateway's local disk IDs that are configured as working storage. Each local disk ID is specified as a string (minimum length of 1 and maximum length of 300). If no local disks are configured as working storage, then the DiskIds array is empty.
            (string) --
            WorkingStorageUsedInBytes (integer) --The total working storage in bytes in use by the gateway. If no working storage is configured for the gateway, this field returns 0.
            WorkingStorageAllocatedInBytes (integer) --The total working storage in bytes allocated for the gateway. If no working storage is configured for the gateway, this field returns 0.
            
            
    :type GatewayARN: string
    """
    pass


def disable_gateway(GatewayARN=None):
    """
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            Return typedict
            ReturnsResponse Syntax{
              'GatewayARN': 'string'
            }
            Response Structure
            (dict) --DisableGatewayOutput
            GatewayARN (string) --The unique Amazon Resource Name of the disabled gateway.
            
            
    :type GatewayARN: string
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


def list_gateways(Marker=None, Limit=None):
    """
    :param Marker: An opaque string that indicates the position at which to begin the returned list of gateways.
    :type Marker: string
    :param Limit: Specifies that the list of gateways returned be limited to the specified number of items.
    :type Limit: integer
    """
    pass


def list_local_disks(GatewayARN=None):
    """
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            Return typedict
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
                  'DiskAllocationResource': 'string'
                },
              ]
            }
            Response Structure
            (dict) --
            GatewayARN (string) --The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            Disks (list) --
            (dict) --
            DiskId (string) --
            DiskPath (string) --
            DiskNode (string) --
            DiskStatus (string) --
            DiskSizeInBytes (integer) --
            DiskAllocationType (string) --
            DiskAllocationResource (string) --
            
            
            
    :type GatewayARN: string
    """
    pass


def list_tags_for_resource(ResourceARN=None, Marker=None, Limit=None):
    """
    :param ResourceARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the resource for which you want to list tags.
            
    :type ResourceARN: string
    :param Marker: An opaque string that indicates the position at which to begin returning the list of tags.
    :type Marker: string
    :param Limit: Specifies that the list of tags returned be limited to the specified number of items.
    :type Limit: integer
    """
    pass


def list_tapes(TapeARNs=None, Marker=None, Limit=None):
    """
    :param TapeARNs: The Amazon Resource Name (ARN) of each of the tapes you want to list. If you don't specify a tape ARN, the response lists all tapes in both your VTL and VTS.
            (string) --
            
    :type TapeARNs: list
    :param Marker: A string that indicates the position at which to begin the returned list of tapes.
    :type Marker: string
    :param Limit: An optional number limit for the tapes in the list returned by this call.
    :type Limit: integer
    """
    pass


def list_volume_initiators(VolumeARN=None):
    """
    :param VolumeARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the volume. Use the ListVolumes operation to return a list of gateway volumes for the gateway.
            Return typedict
            ReturnsResponse Syntax{
              'Initiators': [
                'string',
              ]
            }
            Response Structure
            (dict) --ListVolumeInitiatorsOutput
            Initiators (list) --The host names and port numbers of all iSCSI initiators that are connected to the gateway.
            (string) --
            
            
    :type VolumeARN: string
    """
    pass


def list_volume_recovery_points(GatewayARN=None):
    """
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            Return typedict
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
            GatewayARN (string) --The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            VolumeRecoveryPointInfos (list) --
            (dict) --
            VolumeARN (string) --
            VolumeSizeInBytes (integer) --
            VolumeUsageInBytes (integer) --
            VolumeRecoveryPointTime (string) --
            
            
            
    :type GatewayARN: string
    """
    pass


def list_volumes(GatewayARN=None, Marker=None, Limit=None):
    """
    :param GatewayARN: The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
    :type GatewayARN: string
    :param Marker: A string that indicates the position at which to begin the returned list of volumes. Obtain the marker from the response of a previous List iSCSI Volumes request.
    :type Marker: string
    :param Limit: Specifies that the list of volumes returned be limited to the specified number of items.
    :type Limit: integer
    """
    pass


def remove_tags_from_resource(ResourceARN=None, TagKeys=None):
    """
    :param ResourceARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the resource you want to remove the tags from.
            
    :type ResourceARN: string
    :param TagKeys: [REQUIRED]
            The keys of the tags you want to remove from the specified resource. A tag is composed of a key/value pair.
            (string) --
            
    :type TagKeys: list
    """
    pass


def reset_cache(GatewayARN=None):
    """
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            Return typedict
            ReturnsResponse Syntax{
              'GatewayARN': 'string'
            }
            Response Structure
            (dict) --
            GatewayARN (string) --The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            
            
    :type GatewayARN: string
    """
    pass


def retrieve_tape_archive(TapeARN=None, GatewayARN=None):
    """
    :param TapeARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the virtual tape you want to retrieve from the virtual tape shelf (VTS).
            
    :type TapeARN: string
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway you want to retrieve the virtual tape to. Use the ListGateways operation to return a list of gateways for your account and region.
            You retrieve archived virtual tapes to only one gateway and the gateway must be a gateway-VTL.
            
    :type GatewayARN: string
    """
    pass


def retrieve_tape_recovery_point(TapeARN=None, GatewayARN=None):
    """
    :param TapeARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the virtual tape for which you want to retrieve the recovery point.
            
    :type TapeARN: string
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            
    :type GatewayARN: string
    """
    pass


def set_local_console_password(GatewayARN=None, LocalConsolePassword=None):
    """
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            
    :type GatewayARN: string
    :param LocalConsolePassword: [REQUIRED]
            The password you want to set for your VM local console.
            
    :type LocalConsolePassword: string
    """
    pass


def shutdown_gateway(GatewayARN=None):
    """
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            Return typedict
            ReturnsResponse Syntax{
              'GatewayARN': 'string'
            }
            Response Structure
            (dict) --A JSON object containing the of the gateway that was shut down.
            GatewayARN (string) --The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            
            
    :type GatewayARN: string
    """
    pass


def start_gateway(GatewayARN=None):
    """
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            Return typedict
            ReturnsResponse Syntax{
              'GatewayARN': 'string'
            }
            Response Structure
            (dict) --A JSON object containing the of the gateway that was restarted.
            GatewayARN (string) --The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            
            
    :type GatewayARN: string
    """
    pass


def update_bandwidth_rate_limit(GatewayARN=None, AverageUploadRateLimitInBitsPerSec=None,
                                AverageDownloadRateLimitInBitsPerSec=None):
    """
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            
    :type GatewayARN: string
    :param AverageUploadRateLimitInBitsPerSec: The average upload bandwidth rate limit in bits per second.
    :type AverageUploadRateLimitInBitsPerSec: integer
    :param AverageDownloadRateLimitInBitsPerSec: The average download bandwidth rate limit in bits per second.
    :type AverageDownloadRateLimitInBitsPerSec: integer
    """
    pass


def update_chap_credentials(TargetARN=None, SecretToAuthenticateInitiator=None, InitiatorName=None,
                            SecretToAuthenticateTarget=None):
    """
    :param TargetARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the iSCSI volume target. Use the DescribeStorediSCSIVolumes operation to return the TargetARN for specified VolumeARN.
            
    :type TargetARN: string
    :param SecretToAuthenticateInitiator: [REQUIRED]
            The secret key that the initiator (for example, the Windows client) must provide to participate in mutual CHAP with the target.
            Note
            The secret key must be between 12 and 16 bytes when encoded in UTF-8.
            
    :type SecretToAuthenticateInitiator: string
    :param InitiatorName: [REQUIRED]
            The iSCSI initiator that connects to the target.
            
    :type InitiatorName: string
    :param SecretToAuthenticateTarget: The secret key that the target must provide to participate in mutual CHAP with the initiator (e.g. Windows client).
            Byte constraints: Minimum bytes of 12. Maximum bytes of 16.
            Note
            The secret key must be between 12 and 16 bytes when encoded in UTF-8.
            
    :type SecretToAuthenticateTarget: string
    """
    pass


def update_gateway_information(GatewayARN=None, GatewayName=None, GatewayTimezone=None):
    """
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            
    :type GatewayARN: string
    :param GatewayName: The name you configured for your gateway.
    :type GatewayName: string
    :param GatewayTimezone: 
    :type GatewayTimezone: string
    """
    pass


def update_gateway_software_now(GatewayARN=None):
    """
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            Return typedict
            ReturnsResponse Syntax{
              'GatewayARN': 'string'
            }
            Response Structure
            (dict) --A JSON object containing the of the gateway that was updated.
            GatewayARN (string) --The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            
            
    :type GatewayARN: string
    """
    pass


def update_maintenance_start_time(GatewayARN=None, HourOfDay=None, MinuteOfHour=None, DayOfWeek=None):
    """
    :param GatewayARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and region.
            
    :type GatewayARN: string
    :param HourOfDay: [REQUIRED]
            The hour component of the maintenance start time represented as hh , where hh is the hour (00 to 23). The hour of the day is in the time zone of the gateway.
            
    :type HourOfDay: integer
    :param MinuteOfHour: [REQUIRED]
            The minute component of the maintenance start time represented as mm , where mm is the minute (00 to 59). The minute of the hour is in the time zone of the gateway.
            
    :type MinuteOfHour: integer
    :param DayOfWeek: [REQUIRED]
            The maintenance start time day of the week.
            
    :type DayOfWeek: integer
    """
    pass


def update_snapshot_schedule(VolumeARN=None, StartAt=None, RecurrenceInHours=None, Description=None):
    """
    :param VolumeARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the volume. Use the ListVolumes operation to return a list of gateway volumes.
            
    :type VolumeARN: string
    :param StartAt: [REQUIRED]
            The hour of the day at which the snapshot schedule begins represented as hh , where hh is the hour (0 to 23). The hour of the day is in the time zone of the gateway.
            
    :type StartAt: integer
    :param RecurrenceInHours: [REQUIRED]
            Frequency of snapshots. Specify the number of hours between snapshots.
            
    :type RecurrenceInHours: integer
    :param Description: Optional description of the snapshot that overwrites the existing description.
    :type Description: string
    """
    pass


def update_vtl_device_type(VTLDeviceARN=None, DeviceType=None):
    """
    :param VTLDeviceARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the medium changer you want to select.
            
    :type VTLDeviceARN: string
    :param DeviceType: [REQUIRED]
            The type of medium changer you want to select.
            Valid Values: 'STK-L700', 'AWS-Gateway-VTL'
            
    :type DeviceType: string
    """
    pass
