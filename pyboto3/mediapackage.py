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

def create_channel(Description=None, Id=None, Tags=None):
    """
    Creates a new Channel.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_channel(
        Description='string',
        Id='string',
        Tags={
            'string': 'string'
        }
    )
    
    
    :type Description: string
    :param Description: A short text description of the Channel.

    :type Id: string
    :param Id: [REQUIRED] The ID of the Channel. The ID must be unique within the region and it cannot be changed after a Channel is created.

    :type Tags: dict
    :param Tags: A collection of tags associated with a resource\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Arn': 'string',
    'Description': 'string',
    'HlsIngest': {
        'IngestEndpoints': [
            {
                'Id': 'string',
                'Password': 'string',
                'Url': 'string',
                'Username': 'string'
            },
        ]
    },
    'Id': 'string',
    'Tags': {
        'string': 'string'
    }
}


Response Structure

(dict) -- The new Channel record.
Arn (string) -- The Amazon Resource Name (ARN) assigned to the Channel.
Description (string) -- A short text description of the Channel.
HlsIngest (dict) -- An HTTP Live Streaming (HLS) ingest resource configuration.
IngestEndpoints (list) -- A list of endpoints to which the source stream should be sent.
(dict) -- An endpoint for ingesting source content for a Channel.
Id (string) -- The system generated unique identifier for the IngestEndpoint
Password (string) -- The system generated password for ingest authentication.
Url (string) -- The ingest URL to which the source stream should be sent.
Username (string) -- The system generated username for ingest authentication.






Id (string) -- The ID of the Channel.
Tags (dict) -- A collection of tags associated with a resource
(string) --
(string) --










Exceptions

MediaPackage.Client.exceptions.UnprocessableEntityException
MediaPackage.Client.exceptions.InternalServerErrorException
MediaPackage.Client.exceptions.ForbiddenException
MediaPackage.Client.exceptions.NotFoundException
MediaPackage.Client.exceptions.ServiceUnavailableException
MediaPackage.Client.exceptions.TooManyRequestsException


    :return: {
        'Arn': 'string',
        'Description': 'string',
        'HlsIngest': {
            'IngestEndpoints': [
                {
                    'Id': 'string',
                    'Password': 'string',
                    'Url': 'string',
                    'Username': 'string'
                },
            ]
        },
        'Id': 'string',
        'Tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    (dict) -- The new Channel record.
    Arn (string) -- The Amazon Resource Name (ARN) assigned to the Channel.
    Description (string) -- A short text description of the Channel.
    HlsIngest (dict) -- An HTTP Live Streaming (HLS) ingest resource configuration.
    IngestEndpoints (list) -- A list of endpoints to which the source stream should be sent.
    (dict) -- An endpoint for ingesting source content for a Channel.
    Id (string) -- The system generated unique identifier for the IngestEndpoint
    Password (string) -- The system generated password for ingest authentication.
    Url (string) -- The ingest URL to which the source stream should be sent.
    Username (string) -- The system generated username for ingest authentication.
    
    
    
    
    
    
    Id (string) -- The ID of the Channel.
    Tags (dict) -- A collection of tags associated with a resource
    (string) --
    (string) --
    
    
    
    
    
    
    
    """
    pass

def create_harvest_job(EndTime=None, Id=None, OriginEndpointId=None, S3Destination=None, StartTime=None):
    """
    Creates a new HarvestJob record.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_harvest_job(
        EndTime='string',
        Id='string',
        OriginEndpointId='string',
        S3Destination={
            'BucketName': 'string',
            'ManifestKey': 'string',
            'RoleArn': 'string'
        },
        StartTime='string'
    )
    
    
    :type EndTime: string
    :param EndTime: [REQUIRED] The end of the time-window which will be harvested

    :type Id: string
    :param Id: [REQUIRED] The ID of the HarvestJob. The ID must be unique within the region and it cannot be changed after the HarvestJob is submitted

    :type OriginEndpointId: string
    :param OriginEndpointId: [REQUIRED] The ID of the OriginEndpoint that the HarvestJob will harvest from. This cannot be changed after the HarvestJob is submitted.

    :type S3Destination: dict
    :param S3Destination: [REQUIRED] Configuration parameters for where in an S3 bucket to place the harvested content\n\nBucketName (string) -- [REQUIRED] The name of an S3 bucket within which harvested content will be exported\nManifestKey (string) -- [REQUIRED] The key in the specified S3 bucket where the harvested top-level manifest will be placed.\nRoleArn (string) -- [REQUIRED] The IAM role used to write to the specified S3 bucket\n\n

    :type StartTime: string
    :param StartTime: [REQUIRED] The start of the time-window which will be harvested

    :rtype: dict

ReturnsResponse Syntax
{
    'Arn': 'string',
    'ChannelId': 'string',
    'CreatedAt': 'string',
    'EndTime': 'string',
    'Id': 'string',
    'OriginEndpointId': 'string',
    'S3Destination': {
        'BucketName': 'string',
        'ManifestKey': 'string',
        'RoleArn': 'string'
    },
    'StartTime': 'string',
    'Status': 'IN_PROGRESS'|'SUCCEEDED'|'FAILED'
}


Response Structure

(dict) -- A new HarvestJob record.
Arn (string) -- The Amazon Resource Name (ARN) assigned to the HarvestJob.
ChannelId (string) -- The ID of the Channel that the HarvestJob will harvest from.
CreatedAt (string) -- The time the HarvestJob was submitted
EndTime (string) -- The end of the time-window which will be harvested.
Id (string) -- The ID of the HarvestJob. The ID must be unique within the region and it cannot be changed after the HarvestJob is submitted.
OriginEndpointId (string) -- The ID of the OriginEndpoint that the HarvestJob will harvest from. This cannot be changed after the HarvestJob is submitted.
S3Destination (dict) -- Configuration parameters for where in an S3 bucket to place the harvested content
BucketName (string) -- The name of an S3 bucket within which harvested content will be exported
ManifestKey (string) -- The key in the specified S3 bucket where the harvested top-level manifest will be placed.
RoleArn (string) -- The IAM role used to write to the specified S3 bucket


StartTime (string) -- The start of the time-window which will be harvested.
Status (string) -- The current status of the HarvestJob. Consider setting up a CloudWatch Event to listen for HarvestJobs as they succeed or fail. In the event of failure, the CloudWatch Event will include an explanation of why the HarvestJob failed.






Exceptions

MediaPackage.Client.exceptions.UnprocessableEntityException
MediaPackage.Client.exceptions.InternalServerErrorException
MediaPackage.Client.exceptions.ForbiddenException
MediaPackage.Client.exceptions.NotFoundException
MediaPackage.Client.exceptions.ServiceUnavailableException
MediaPackage.Client.exceptions.TooManyRequestsException


    :return: {
        'Arn': 'string',
        'ChannelId': 'string',
        'CreatedAt': 'string',
        'EndTime': 'string',
        'Id': 'string',
        'OriginEndpointId': 'string',
        'S3Destination': {
            'BucketName': 'string',
            'ManifestKey': 'string',
            'RoleArn': 'string'
        },
        'StartTime': 'string',
        'Status': 'IN_PROGRESS'|'SUCCEEDED'|'FAILED'
    }
    
    
    :returns: 
    (dict) -- A new HarvestJob record.
    Arn (string) -- The Amazon Resource Name (ARN) assigned to the HarvestJob.
    ChannelId (string) -- The ID of the Channel that the HarvestJob will harvest from.
    CreatedAt (string) -- The time the HarvestJob was submitted
    EndTime (string) -- The end of the time-window which will be harvested.
    Id (string) -- The ID of the HarvestJob. The ID must be unique within the region and it cannot be changed after the HarvestJob is submitted.
    OriginEndpointId (string) -- The ID of the OriginEndpoint that the HarvestJob will harvest from. This cannot be changed after the HarvestJob is submitted.
    S3Destination (dict) -- Configuration parameters for where in an S3 bucket to place the harvested content
    BucketName (string) -- The name of an S3 bucket within which harvested content will be exported
    ManifestKey (string) -- The key in the specified S3 bucket where the harvested top-level manifest will be placed.
    RoleArn (string) -- The IAM role used to write to the specified S3 bucket
    
    
    StartTime (string) -- The start of the time-window which will be harvested.
    Status (string) -- The current status of the HarvestJob. Consider setting up a CloudWatch Event to listen for HarvestJobs as they succeed or fail. In the event of failure, the CloudWatch Event will include an explanation of why the HarvestJob failed.
    
    
    
    """
    pass

def create_origin_endpoint(Authorization=None, ChannelId=None, CmafPackage=None, DashPackage=None, Description=None, HlsPackage=None, Id=None, ManifestName=None, MssPackage=None, Origination=None, StartoverWindowSeconds=None, Tags=None, TimeDelaySeconds=None, Whitelist=None):
    """
    Creates a new OriginEndpoint record.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_origin_endpoint(
        Authorization={
            'CdnIdentifierSecret': 'string',
            'SecretsRoleArn': 'string'
        },
        ChannelId='string',
        CmafPackage={
            'Encryption': {
                'KeyRotationIntervalSeconds': 123,
                'SpekeKeyProvider': {
                    'CertificateArn': 'string',
                    'ResourceId': 'string',
                    'RoleArn': 'string',
                    'SystemIds': [
                        'string',
                    ],
                    'Url': 'string'
                }
            },
            'HlsManifests': [
                {
                    'AdMarkers': 'NONE'|'SCTE35_ENHANCED'|'PASSTHROUGH',
                    'AdTriggers': [
                        'SPLICE_INSERT'|'BREAK'|'PROVIDER_ADVERTISEMENT'|'DISTRIBUTOR_ADVERTISEMENT'|'PROVIDER_PLACEMENT_OPPORTUNITY'|'DISTRIBUTOR_PLACEMENT_OPPORTUNITY'|'PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY'|'DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY',
                    ],
                    'AdsOnDeliveryRestrictions': 'NONE'|'RESTRICTED'|'UNRESTRICTED'|'BOTH',
                    'Id': 'string',
                    'IncludeIframeOnlyStream': True|False,
                    'ManifestName': 'string',
                    'PlaylistType': 'NONE'|'EVENT'|'VOD',
                    'PlaylistWindowSeconds': 123,
                    'ProgramDateTimeIntervalSeconds': 123
                },
            ],
            'SegmentDurationSeconds': 123,
            'SegmentPrefix': 'string',
            'StreamSelection': {
                'MaxVideoBitsPerSecond': 123,
                'MinVideoBitsPerSecond': 123,
                'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
            }
        },
        DashPackage={
            'AdTriggers': [
                'SPLICE_INSERT'|'BREAK'|'PROVIDER_ADVERTISEMENT'|'DISTRIBUTOR_ADVERTISEMENT'|'PROVIDER_PLACEMENT_OPPORTUNITY'|'DISTRIBUTOR_PLACEMENT_OPPORTUNITY'|'PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY'|'DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY',
            ],
            'AdsOnDeliveryRestrictions': 'NONE'|'RESTRICTED'|'UNRESTRICTED'|'BOTH',
            'Encryption': {
                'KeyRotationIntervalSeconds': 123,
                'SpekeKeyProvider': {
                    'CertificateArn': 'string',
                    'ResourceId': 'string',
                    'RoleArn': 'string',
                    'SystemIds': [
                        'string',
                    ],
                    'Url': 'string'
                }
            },
            'ManifestLayout': 'FULL'|'COMPACT',
            'ManifestWindowSeconds': 123,
            'MinBufferTimeSeconds': 123,
            'MinUpdatePeriodSeconds': 123,
            'PeriodTriggers': [
                'ADS',
            ],
            'Profile': 'NONE'|'HBBTV_1_5',
            'SegmentDurationSeconds': 123,
            'SegmentTemplateFormat': 'NUMBER_WITH_TIMELINE'|'TIME_WITH_TIMELINE'|'NUMBER_WITH_DURATION',
            'StreamSelection': {
                'MaxVideoBitsPerSecond': 123,
                'MinVideoBitsPerSecond': 123,
                'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
            },
            'SuggestedPresentationDelaySeconds': 123
        },
        Description='string',
        HlsPackage={
            'AdMarkers': 'NONE'|'SCTE35_ENHANCED'|'PASSTHROUGH',
            'AdTriggers': [
                'SPLICE_INSERT'|'BREAK'|'PROVIDER_ADVERTISEMENT'|'DISTRIBUTOR_ADVERTISEMENT'|'PROVIDER_PLACEMENT_OPPORTUNITY'|'DISTRIBUTOR_PLACEMENT_OPPORTUNITY'|'PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY'|'DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY',
            ],
            'AdsOnDeliveryRestrictions': 'NONE'|'RESTRICTED'|'UNRESTRICTED'|'BOTH',
            'Encryption': {
                'ConstantInitializationVector': 'string',
                'EncryptionMethod': 'AES_128'|'SAMPLE_AES',
                'KeyRotationIntervalSeconds': 123,
                'RepeatExtXKey': True|False,
                'SpekeKeyProvider': {
                    'CertificateArn': 'string',
                    'ResourceId': 'string',
                    'RoleArn': 'string',
                    'SystemIds': [
                        'string',
                    ],
                    'Url': 'string'
                }
            },
            'IncludeIframeOnlyStream': True|False,
            'PlaylistType': 'NONE'|'EVENT'|'VOD',
            'PlaylistWindowSeconds': 123,
            'ProgramDateTimeIntervalSeconds': 123,
            'SegmentDurationSeconds': 123,
            'StreamSelection': {
                'MaxVideoBitsPerSecond': 123,
                'MinVideoBitsPerSecond': 123,
                'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
            },
            'UseAudioRenditionGroup': True|False
        },
        Id='string',
        ManifestName='string',
        MssPackage={
            'Encryption': {
                'SpekeKeyProvider': {
                    'CertificateArn': 'string',
                    'ResourceId': 'string',
                    'RoleArn': 'string',
                    'SystemIds': [
                        'string',
                    ],
                    'Url': 'string'
                }
            },
            'ManifestWindowSeconds': 123,
            'SegmentDurationSeconds': 123,
            'StreamSelection': {
                'MaxVideoBitsPerSecond': 123,
                'MinVideoBitsPerSecond': 123,
                'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
            }
        },
        Origination='ALLOW'|'DENY',
        StartoverWindowSeconds=123,
        Tags={
            'string': 'string'
        },
        TimeDelaySeconds=123,
        Whitelist=[
            'string',
        ]
    )
    
    
    :type Authorization: dict
    :param Authorization: CDN Authorization credentials\n\nCdnIdentifierSecret (string) -- [REQUIRED] The Amazon Resource Name (ARN) for the secret in Secrets Manager that your Content Distribution Network (CDN) uses for authorization to access your endpoint.\nSecretsRoleArn (string) -- [REQUIRED] The Amazon Resource Name (ARN) for the IAM role that allows MediaPackage to communicate with AWS Secrets Manager.\n\n

    :type ChannelId: string
    :param ChannelId: [REQUIRED] The ID of the Channel that the OriginEndpoint will be associated with. This cannot be changed after the OriginEndpoint is created.

    :type CmafPackage: dict
    :param CmafPackage: A Common Media Application Format (CMAF) packaging configuration.\n\nEncryption (dict) -- A Common Media Application Format (CMAF) encryption configuration.\nKeyRotationIntervalSeconds (integer) -- Time (in seconds) between each encryption key rotation.\nSpekeKeyProvider (dict) -- [REQUIRED] A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.\nCertificateArn (string) -- An Amazon Resource Name (ARN) of a Certificate Manager certificate that MediaPackage will use for enforcing secure end-to-end data transfer with the key provider service.\nResourceId (string) -- [REQUIRED] The resource ID to include in key requests.\nRoleArn (string) -- [REQUIRED] An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.\nSystemIds (list) -- [REQUIRED] The system IDs to include in key requests.\n(string) --\n\n\nUrl (string) -- [REQUIRED] The URL of the external key provider service.\n\n\n\n\nHlsManifests (list) -- A list of HLS manifest configurations\n(dict) -- A HTTP Live Streaming (HLS) manifest configuration.\nAdMarkers (string) -- This setting controls how ad markers are included in the packaged OriginEndpoint. 'NONE' will omit all SCTE-35 ad markers from the output. 'PASSTHROUGH' causes the manifest to contain a copy of the SCTE-35 ad markers (comments) taken directly from the input HTTP Live Streaming (HLS) manifest. 'SCTE35_ENHANCED' generates ad markers and blackout tags based on SCTE-35 messages in the input source.\nAdTriggers (list) -- A list of SCTE-35 message types that are treated as ad markers in the output. If empty, no ad markers are output. Specify multiple items to create ad markers for all of the included message types.\n(string) --\n\n\nAdsOnDeliveryRestrictions (string) -- This setting allows the delivery restriction flags on SCTE-35 segmentation descriptors to determine whether a message signals an ad. Choosing 'NONE' means no SCTE-35 messages become ads. Choosing 'RESTRICTED' means SCTE-35 messages of the types specified in AdTriggers that contain delivery restrictions will be treated as ads. Choosing 'UNRESTRICTED' means SCTE-35 messages of the types specified in AdTriggers that do not contain delivery restrictions will be treated as ads. Choosing 'BOTH' means all SCTE-35 messages of the types specified in AdTriggers will be treated as ads. Note that Splice Insert messages do not have these flags and are always treated as ads if specified in AdTriggers.\nId (string) -- [REQUIRED] The ID of the manifest. The ID must be unique within the OriginEndpoint and it cannot be changed after it is created.\nIncludeIframeOnlyStream (boolean) -- When enabled, an I-Frame only stream will be included in the output.\nManifestName (string) -- An optional short string appended to the end of the OriginEndpoint URL. If not specified, defaults to the manifestName for the OriginEndpoint.\nPlaylistType (string) -- The HTTP Live Streaming (HLS) playlist type. When either 'EVENT' or 'VOD' is specified, a corresponding EXT-X-PLAYLIST-TYPE entry will be included in the media playlist.\nPlaylistWindowSeconds (integer) -- Time window (in seconds) contained in each parent manifest.\nProgramDateTimeIntervalSeconds (integer) -- The interval (in seconds) between each EXT-X-PROGRAM-DATE-TIME tag inserted into manifests. Additionally, when an interval is specified ID3Timed Metadata messages will be generated every 5 seconds using the ingest time of the content. If the interval is not specified, or set to 0, then no EXT-X-PROGRAM-DATE-TIME tags will be inserted into manifests and no ID3Timed Metadata messages will be generated. Note that irrespective of this parameter, if any ID3 Timed Metadata is found in HTTP Live Streaming (HLS) input, it will be passed through to HLS output.\n\n\n\n\nSegmentDurationSeconds (integer) -- Duration (in seconds) of each segment. Actual segments will be rounded to the nearest multiple of the source segment duration.\nSegmentPrefix (string) -- An optional custom string that is prepended to the name of each segment. If not specified, it defaults to the ChannelId.\nStreamSelection (dict) -- A StreamSelection configuration.\nMaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.\nMinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.\nStreamOrder (string) -- A directive that determines the order of streams in the output.\n\n\n\n

    :type DashPackage: dict
    :param DashPackage: A Dynamic Adaptive Streaming over HTTP (DASH) packaging configuration.\n\nAdTriggers (list) -- A list of SCTE-35 message types that are treated as ad markers in the output. If empty, no ad markers are output. Specify multiple items to create ad markers for all of the included message types.\n(string) --\n\n\nAdsOnDeliveryRestrictions (string) -- This setting allows the delivery restriction flags on SCTE-35 segmentation descriptors to determine whether a message signals an ad. Choosing 'NONE' means no SCTE-35 messages become ads. Choosing 'RESTRICTED' means SCTE-35 messages of the types specified in AdTriggers that contain delivery restrictions will be treated as ads. Choosing 'UNRESTRICTED' means SCTE-35 messages of the types specified in AdTriggers that do not contain delivery restrictions will be treated as ads. Choosing 'BOTH' means all SCTE-35 messages of the types specified in AdTriggers will be treated as ads. Note that Splice Insert messages do not have these flags and are always treated as ads if specified in AdTriggers.\nEncryption (dict) -- A Dynamic Adaptive Streaming over HTTP (DASH) encryption configuration.\nKeyRotationIntervalSeconds (integer) -- Time (in seconds) between each encryption key rotation.\nSpekeKeyProvider (dict) -- [REQUIRED] A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.\nCertificateArn (string) -- An Amazon Resource Name (ARN) of a Certificate Manager certificate that MediaPackage will use for enforcing secure end-to-end data transfer with the key provider service.\nResourceId (string) -- [REQUIRED] The resource ID to include in key requests.\nRoleArn (string) -- [REQUIRED] An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.\nSystemIds (list) -- [REQUIRED] The system IDs to include in key requests.\n(string) --\n\n\nUrl (string) -- [REQUIRED] The URL of the external key provider service.\n\n\n\n\nManifestLayout (string) -- Determines the position of some tags in the Media Presentation Description (MPD). When set to FULL, elements like SegmentTemplate and ContentProtection are included in each Representation. When set to COMPACT, duplicate elements are combined and presented at the AdaptationSet level.\nManifestWindowSeconds (integer) -- Time window (in seconds) contained in each manifest.\nMinBufferTimeSeconds (integer) -- Minimum duration (in seconds) that a player will buffer media before starting the presentation.\nMinUpdatePeriodSeconds (integer) -- Minimum duration (in seconds) between potential changes to the Dynamic Adaptive Streaming over HTTP (DASH) Media Presentation Description (MPD).\nPeriodTriggers (list) -- A list of triggers that controls when the outgoing Dynamic Adaptive Streaming over HTTP (DASH) Media Presentation Description (MPD) will be partitioned into multiple periods. If empty, the content will not be partitioned into more than one period. If the list contains 'ADS', new periods will be created where the Channel source contains SCTE-35 ad markers.\n(string) --\n\n\nProfile (string) -- The Dynamic Adaptive Streaming over HTTP (DASH) profile type. When set to 'HBBTV_1_5', HbbTV 1.5 compliant output is enabled.\nSegmentDurationSeconds (integer) -- Duration (in seconds) of each segment. Actual segments will be rounded to the nearest multiple of the source segment duration.\nSegmentTemplateFormat (string) -- Determines the type of SegmentTemplate included in the Media Presentation Description (MPD). When set to NUMBER_WITH_TIMELINE, a full timeline is presented in each SegmentTemplate, with $Number$ media URLs. When set to TIME_WITH_TIMELINE, a full timeline is presented in each SegmentTemplate, with $Time$ media URLs. When set to NUMBER_WITH_DURATION, only a duration is included in each SegmentTemplate, with $Number$ media URLs.\nStreamSelection (dict) -- A StreamSelection configuration.\nMaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.\nMinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.\nStreamOrder (string) -- A directive that determines the order of streams in the output.\n\n\nSuggestedPresentationDelaySeconds (integer) -- Duration (in seconds) to delay live content before presentation.\n\n

    :type Description: string
    :param Description: A short text description of the OriginEndpoint.

    :type HlsPackage: dict
    :param HlsPackage: An HTTP Live Streaming (HLS) packaging configuration.\n\nAdMarkers (string) -- This setting controls how ad markers are included in the packaged OriginEndpoint. 'NONE' will omit all SCTE-35 ad markers from the output. 'PASSTHROUGH' causes the manifest to contain a copy of the SCTE-35 ad markers (comments) taken directly from the input HTTP Live Streaming (HLS) manifest. 'SCTE35_ENHANCED' generates ad markers and blackout tags based on SCTE-35 messages in the input source.\nAdTriggers (list) -- A list of SCTE-35 message types that are treated as ad markers in the output. If empty, no ad markers are output. Specify multiple items to create ad markers for all of the included message types.\n(string) --\n\n\nAdsOnDeliveryRestrictions (string) -- This setting allows the delivery restriction flags on SCTE-35 segmentation descriptors to determine whether a message signals an ad. Choosing 'NONE' means no SCTE-35 messages become ads. Choosing 'RESTRICTED' means SCTE-35 messages of the types specified in AdTriggers that contain delivery restrictions will be treated as ads. Choosing 'UNRESTRICTED' means SCTE-35 messages of the types specified in AdTriggers that do not contain delivery restrictions will be treated as ads. Choosing 'BOTH' means all SCTE-35 messages of the types specified in AdTriggers will be treated as ads. Note that Splice Insert messages do not have these flags and are always treated as ads if specified in AdTriggers.\nEncryption (dict) -- An HTTP Live Streaming (HLS) encryption configuration.\nConstantInitializationVector (string) -- A constant initialization vector for encryption (optional). When not specified the initialization vector will be periodically rotated.\nEncryptionMethod (string) -- The encryption method to use.\nKeyRotationIntervalSeconds (integer) -- Interval (in seconds) between each encryption key rotation.\nRepeatExtXKey (boolean) -- When enabled, the EXT-X-KEY tag will be repeated in output manifests.\nSpekeKeyProvider (dict) -- [REQUIRED] A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.\nCertificateArn (string) -- An Amazon Resource Name (ARN) of a Certificate Manager certificate that MediaPackage will use for enforcing secure end-to-end data transfer with the key provider service.\nResourceId (string) -- [REQUIRED] The resource ID to include in key requests.\nRoleArn (string) -- [REQUIRED] An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.\nSystemIds (list) -- [REQUIRED] The system IDs to include in key requests.\n(string) --\n\n\nUrl (string) -- [REQUIRED] The URL of the external key provider service.\n\n\n\n\nIncludeIframeOnlyStream (boolean) -- When enabled, an I-Frame only stream will be included in the output.\nPlaylistType (string) -- The HTTP Live Streaming (HLS) playlist type. When either 'EVENT' or 'VOD' is specified, a corresponding EXT-X-PLAYLIST-TYPE entry will be included in the media playlist.\nPlaylistWindowSeconds (integer) -- Time window (in seconds) contained in each parent manifest.\nProgramDateTimeIntervalSeconds (integer) -- The interval (in seconds) between each EXT-X-PROGRAM-DATE-TIME tag inserted into manifests. Additionally, when an interval is specified ID3Timed Metadata messages will be generated every 5 seconds using the ingest time of the content. If the interval is not specified, or set to 0, then no EXT-X-PROGRAM-DATE-TIME tags will be inserted into manifests and no ID3Timed Metadata messages will be generated. Note that irrespective of this parameter, if any ID3 Timed Metadata is found in HTTP Live Streaming (HLS) input, it will be passed through to HLS output.\nSegmentDurationSeconds (integer) -- Duration (in seconds) of each fragment. Actual fragments will be rounded to the nearest multiple of the source fragment duration.\nStreamSelection (dict) -- A StreamSelection configuration.\nMaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.\nMinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.\nStreamOrder (string) -- A directive that determines the order of streams in the output.\n\n\nUseAudioRenditionGroup (boolean) -- When enabled, audio streams will be placed in rendition groups in the output.\n\n

    :type Id: string
    :param Id: [REQUIRED] The ID of the OriginEndpoint. The ID must be unique within the region and it cannot be changed after the OriginEndpoint is created.

    :type ManifestName: string
    :param ManifestName: A short string that will be used as the filename of the OriginEndpoint URL (defaults to 'index').

    :type MssPackage: dict
    :param MssPackage: A Microsoft Smooth Streaming (MSS) packaging configuration.\n\nEncryption (dict) -- A Microsoft Smooth Streaming (MSS) encryption configuration.\nSpekeKeyProvider (dict) -- [REQUIRED] A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.\nCertificateArn (string) -- An Amazon Resource Name (ARN) of a Certificate Manager certificate that MediaPackage will use for enforcing secure end-to-end data transfer with the key provider service.\nResourceId (string) -- [REQUIRED] The resource ID to include in key requests.\nRoleArn (string) -- [REQUIRED] An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.\nSystemIds (list) -- [REQUIRED] The system IDs to include in key requests.\n(string) --\n\n\nUrl (string) -- [REQUIRED] The URL of the external key provider service.\n\n\n\n\nManifestWindowSeconds (integer) -- The time window (in seconds) contained in each manifest.\nSegmentDurationSeconds (integer) -- The duration (in seconds) of each segment.\nStreamSelection (dict) -- A StreamSelection configuration.\nMaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.\nMinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.\nStreamOrder (string) -- A directive that determines the order of streams in the output.\n\n\n\n

    :type Origination: string
    :param Origination: Control whether origination of video is allowed for this OriginEndpoint. If set to ALLOW, the OriginEndpoint may by requested, pursuant to any other form of access control. If set to DENY, the OriginEndpoint may not be requested. This can be helpful for Live to VOD harvesting, or for temporarily disabling origination

    :type StartoverWindowSeconds: integer
    :param StartoverWindowSeconds: Maximum duration (seconds) of content to retain for startover playback. If not specified, startover playback will be disabled for the OriginEndpoint.

    :type Tags: dict
    :param Tags: A collection of tags associated with a resource\n\n(string) --\n(string) --\n\n\n\n

    :type TimeDelaySeconds: integer
    :param TimeDelaySeconds: Amount of delay (seconds) to enforce on the playback of live content. If not specified, there will be no time delay in effect for the OriginEndpoint.

    :type Whitelist: list
    :param Whitelist: A list of source IP CIDR blocks that will be allowed to access the OriginEndpoint.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Arn': 'string',
    'Authorization': {
        'CdnIdentifierSecret': 'string',
        'SecretsRoleArn': 'string'
    },
    'ChannelId': 'string',
    'CmafPackage': {
        'Encryption': {
            'KeyRotationIntervalSeconds': 123,
            'SpekeKeyProvider': {
                'CertificateArn': 'string',
                'ResourceId': 'string',
                'RoleArn': 'string',
                'SystemIds': [
                    'string',
                ],
                'Url': 'string'
            }
        },
        'HlsManifests': [
            {
                'AdMarkers': 'NONE'|'SCTE35_ENHANCED'|'PASSTHROUGH',
                'Id': 'string',
                'IncludeIframeOnlyStream': True|False,
                'ManifestName': 'string',
                'PlaylistType': 'NONE'|'EVENT'|'VOD',
                'PlaylistWindowSeconds': 123,
                'ProgramDateTimeIntervalSeconds': 123,
                'Url': 'string'
            },
        ],
        'SegmentDurationSeconds': 123,
        'SegmentPrefix': 'string',
        'StreamSelection': {
            'MaxVideoBitsPerSecond': 123,
            'MinVideoBitsPerSecond': 123,
            'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
        }
    },
    'DashPackage': {
        'AdTriggers': [
            'SPLICE_INSERT'|'BREAK'|'PROVIDER_ADVERTISEMENT'|'DISTRIBUTOR_ADVERTISEMENT'|'PROVIDER_PLACEMENT_OPPORTUNITY'|'DISTRIBUTOR_PLACEMENT_OPPORTUNITY'|'PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY'|'DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY',
        ],
        'AdsOnDeliveryRestrictions': 'NONE'|'RESTRICTED'|'UNRESTRICTED'|'BOTH',
        'Encryption': {
            'KeyRotationIntervalSeconds': 123,
            'SpekeKeyProvider': {
                'CertificateArn': 'string',
                'ResourceId': 'string',
                'RoleArn': 'string',
                'SystemIds': [
                    'string',
                ],
                'Url': 'string'
            }
        },
        'ManifestLayout': 'FULL'|'COMPACT',
        'ManifestWindowSeconds': 123,
        'MinBufferTimeSeconds': 123,
        'MinUpdatePeriodSeconds': 123,
        'PeriodTriggers': [
            'ADS',
        ],
        'Profile': 'NONE'|'HBBTV_1_5',
        'SegmentDurationSeconds': 123,
        'SegmentTemplateFormat': 'NUMBER_WITH_TIMELINE'|'TIME_WITH_TIMELINE'|'NUMBER_WITH_DURATION',
        'StreamSelection': {
            'MaxVideoBitsPerSecond': 123,
            'MinVideoBitsPerSecond': 123,
            'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
        },
        'SuggestedPresentationDelaySeconds': 123
    },
    'Description': 'string',
    'HlsPackage': {
        'AdMarkers': 'NONE'|'SCTE35_ENHANCED'|'PASSTHROUGH',
        'AdTriggers': [
            'SPLICE_INSERT'|'BREAK'|'PROVIDER_ADVERTISEMENT'|'DISTRIBUTOR_ADVERTISEMENT'|'PROVIDER_PLACEMENT_OPPORTUNITY'|'DISTRIBUTOR_PLACEMENT_OPPORTUNITY'|'PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY'|'DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY',
        ],
        'AdsOnDeliveryRestrictions': 'NONE'|'RESTRICTED'|'UNRESTRICTED'|'BOTH',
        'Encryption': {
            'ConstantInitializationVector': 'string',
            'EncryptionMethod': 'AES_128'|'SAMPLE_AES',
            'KeyRotationIntervalSeconds': 123,
            'RepeatExtXKey': True|False,
            'SpekeKeyProvider': {
                'CertificateArn': 'string',
                'ResourceId': 'string',
                'RoleArn': 'string',
                'SystemIds': [
                    'string',
                ],
                'Url': 'string'
            }
        },
        'IncludeIframeOnlyStream': True|False,
        'PlaylistType': 'NONE'|'EVENT'|'VOD',
        'PlaylistWindowSeconds': 123,
        'ProgramDateTimeIntervalSeconds': 123,
        'SegmentDurationSeconds': 123,
        'StreamSelection': {
            'MaxVideoBitsPerSecond': 123,
            'MinVideoBitsPerSecond': 123,
            'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
        },
        'UseAudioRenditionGroup': True|False
    },
    'Id': 'string',
    'ManifestName': 'string',
    'MssPackage': {
        'Encryption': {
            'SpekeKeyProvider': {
                'CertificateArn': 'string',
                'ResourceId': 'string',
                'RoleArn': 'string',
                'SystemIds': [
                    'string',
                ],
                'Url': 'string'
            }
        },
        'ManifestWindowSeconds': 123,
        'SegmentDurationSeconds': 123,
        'StreamSelection': {
            'MaxVideoBitsPerSecond': 123,
            'MinVideoBitsPerSecond': 123,
            'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
        }
    },
    'Origination': 'ALLOW'|'DENY',
    'StartoverWindowSeconds': 123,
    'Tags': {
        'string': 'string'
    },
    'TimeDelaySeconds': 123,
    'Url': 'string',
    'Whitelist': [
        'string',
    ]
}


Response Structure

(dict) -- A new OriginEndpoint record.
Arn (string) -- The Amazon Resource Name (ARN) assigned to the OriginEndpoint.
Authorization (dict) -- CDN Authorization credentials
CdnIdentifierSecret (string) -- The Amazon Resource Name (ARN) for the secret in Secrets Manager that your Content Distribution Network (CDN) uses for authorization to access your endpoint.
SecretsRoleArn (string) -- The Amazon Resource Name (ARN) for the IAM role that allows MediaPackage to communicate with AWS Secrets Manager.


ChannelId (string) -- The ID of the Channel the OriginEndpoint is associated with.
CmafPackage (dict) -- A Common Media Application Format (CMAF) packaging configuration.
Encryption (dict) -- A Common Media Application Format (CMAF) encryption configuration.
KeyRotationIntervalSeconds (integer) -- Time (in seconds) between each encryption key rotation.
SpekeKeyProvider (dict) -- A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
CertificateArn (string) -- An Amazon Resource Name (ARN) of a Certificate Manager certificate that MediaPackage will use for enforcing secure end-to-end data transfer with the key provider service.
ResourceId (string) -- The resource ID to include in key requests.
RoleArn (string) -- An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.
SystemIds (list) -- The system IDs to include in key requests.
(string) --


Url (string) -- The URL of the external key provider service.




HlsManifests (list) -- A list of HLS manifest configurations
(dict) -- A HTTP Live Streaming (HLS) manifest configuration.
AdMarkers (string) -- This setting controls how ad markers are included in the packaged OriginEndpoint. "NONE" will omit all SCTE-35 ad markers from the output. "PASSTHROUGH" causes the manifest to contain a copy of the SCTE-35 ad markers (comments) taken directly from the input HTTP Live Streaming (HLS) manifest. "SCTE35_ENHANCED" generates ad markers and blackout tags based on SCTE-35 messages in the input source.
Id (string) -- The ID of the manifest. The ID must be unique within the OriginEndpoint and it cannot be changed after it is created.
IncludeIframeOnlyStream (boolean) -- When enabled, an I-Frame only stream will be included in the output.
ManifestName (string) -- An optional short string appended to the end of the OriginEndpoint URL. If not specified, defaults to the manifestName for the OriginEndpoint.
PlaylistType (string) -- The HTTP Live Streaming (HLS) playlist type. When either "EVENT" or "VOD" is specified, a corresponding EXT-X-PLAYLIST-TYPE entry will be included in the media playlist.
PlaylistWindowSeconds (integer) -- Time window (in seconds) contained in each parent manifest.
ProgramDateTimeIntervalSeconds (integer) -- The interval (in seconds) between each EXT-X-PROGRAM-DATE-TIME tag inserted into manifests. Additionally, when an interval is specified ID3Timed Metadata messages will be generated every 5 seconds using the ingest time of the content. If the interval is not specified, or set to 0, then no EXT-X-PROGRAM-DATE-TIME tags will be inserted into manifests and no ID3Timed Metadata messages will be generated. Note that irrespective of this parameter, if any ID3 Timed Metadata is found in HTTP Live Streaming (HLS) input, it will be passed through to HLS output.
Url (string) -- The URL of the packaged OriginEndpoint for consumption.




SegmentDurationSeconds (integer) -- Duration (in seconds) of each segment. Actual segments will be rounded to the nearest multiple of the source segment duration.
SegmentPrefix (string) -- An optional custom string that is prepended to the name of each segment. If not specified, it defaults to the ChannelId.
StreamSelection (dict) -- A StreamSelection configuration.
MaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.
MinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.
StreamOrder (string) -- A directive that determines the order of streams in the output.




DashPackage (dict) -- A Dynamic Adaptive Streaming over HTTP (DASH) packaging configuration.
AdTriggers (list) -- A list of SCTE-35 message types that are treated as ad markers in the output. If empty, no ad markers are output. Specify multiple items to create ad markers for all of the included message types.
(string) --


AdsOnDeliveryRestrictions (string) -- This setting allows the delivery restriction flags on SCTE-35 segmentation descriptors to determine whether a message signals an ad. Choosing "NONE" means no SCTE-35 messages become ads. Choosing "RESTRICTED" means SCTE-35 messages of the types specified in AdTriggers that contain delivery restrictions will be treated as ads. Choosing "UNRESTRICTED" means SCTE-35 messages of the types specified in AdTriggers that do not contain delivery restrictions will be treated as ads. Choosing "BOTH" means all SCTE-35 messages of the types specified in AdTriggers will be treated as ads. Note that Splice Insert messages do not have these flags and are always treated as ads if specified in AdTriggers.
Encryption (dict) -- A Dynamic Adaptive Streaming over HTTP (DASH) encryption configuration.
KeyRotationIntervalSeconds (integer) -- Time (in seconds) between each encryption key rotation.
SpekeKeyProvider (dict) -- A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
CertificateArn (string) -- An Amazon Resource Name (ARN) of a Certificate Manager certificate that MediaPackage will use for enforcing secure end-to-end data transfer with the key provider service.
ResourceId (string) -- The resource ID to include in key requests.
RoleArn (string) -- An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.
SystemIds (list) -- The system IDs to include in key requests.
(string) --


Url (string) -- The URL of the external key provider service.




ManifestLayout (string) -- Determines the position of some tags in the Media Presentation Description (MPD). When set to FULL, elements like SegmentTemplate and ContentProtection are included in each Representation. When set to COMPACT, duplicate elements are combined and presented at the AdaptationSet level.
ManifestWindowSeconds (integer) -- Time window (in seconds) contained in each manifest.
MinBufferTimeSeconds (integer) -- Minimum duration (in seconds) that a player will buffer media before starting the presentation.
MinUpdatePeriodSeconds (integer) -- Minimum duration (in seconds) between potential changes to the Dynamic Adaptive Streaming over HTTP (DASH) Media Presentation Description (MPD).
PeriodTriggers (list) -- A list of triggers that controls when the outgoing Dynamic Adaptive Streaming over HTTP (DASH) Media Presentation Description (MPD) will be partitioned into multiple periods. If empty, the content will not be partitioned into more than one period. If the list contains "ADS", new periods will be created where the Channel source contains SCTE-35 ad markers.
(string) --


Profile (string) -- The Dynamic Adaptive Streaming over HTTP (DASH) profile type. When set to "HBBTV_1_5", HbbTV 1.5 compliant output is enabled.
SegmentDurationSeconds (integer) -- Duration (in seconds) of each segment. Actual segments will be rounded to the nearest multiple of the source segment duration.
SegmentTemplateFormat (string) -- Determines the type of SegmentTemplate included in the Media Presentation Description (MPD). When set to NUMBER_WITH_TIMELINE, a full timeline is presented in each SegmentTemplate, with $Number$ media URLs. When set to TIME_WITH_TIMELINE, a full timeline is presented in each SegmentTemplate, with $Time$ media URLs. When set to NUMBER_WITH_DURATION, only a duration is included in each SegmentTemplate, with $Number$ media URLs.
StreamSelection (dict) -- A StreamSelection configuration.
MaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.
MinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.
StreamOrder (string) -- A directive that determines the order of streams in the output.


SuggestedPresentationDelaySeconds (integer) -- Duration (in seconds) to delay live content before presentation.


Description (string) -- A short text description of the OriginEndpoint.
HlsPackage (dict) -- An HTTP Live Streaming (HLS) packaging configuration.
AdMarkers (string) -- This setting controls how ad markers are included in the packaged OriginEndpoint. "NONE" will omit all SCTE-35 ad markers from the output. "PASSTHROUGH" causes the manifest to contain a copy of the SCTE-35 ad markers (comments) taken directly from the input HTTP Live Streaming (HLS) manifest. "SCTE35_ENHANCED" generates ad markers and blackout tags based on SCTE-35 messages in the input source.
AdTriggers (list) -- A list of SCTE-35 message types that are treated as ad markers in the output. If empty, no ad markers are output. Specify multiple items to create ad markers for all of the included message types.
(string) --


AdsOnDeliveryRestrictions (string) -- This setting allows the delivery restriction flags on SCTE-35 segmentation descriptors to determine whether a message signals an ad. Choosing "NONE" means no SCTE-35 messages become ads. Choosing "RESTRICTED" means SCTE-35 messages of the types specified in AdTriggers that contain delivery restrictions will be treated as ads. Choosing "UNRESTRICTED" means SCTE-35 messages of the types specified in AdTriggers that do not contain delivery restrictions will be treated as ads. Choosing "BOTH" means all SCTE-35 messages of the types specified in AdTriggers will be treated as ads. Note that Splice Insert messages do not have these flags and are always treated as ads if specified in AdTriggers.
Encryption (dict) -- An HTTP Live Streaming (HLS) encryption configuration.
ConstantInitializationVector (string) -- A constant initialization vector for encryption (optional). When not specified the initialization vector will be periodically rotated.
EncryptionMethod (string) -- The encryption method to use.
KeyRotationIntervalSeconds (integer) -- Interval (in seconds) between each encryption key rotation.
RepeatExtXKey (boolean) -- When enabled, the EXT-X-KEY tag will be repeated in output manifests.
SpekeKeyProvider (dict) -- A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
CertificateArn (string) -- An Amazon Resource Name (ARN) of a Certificate Manager certificate that MediaPackage will use for enforcing secure end-to-end data transfer with the key provider service.
ResourceId (string) -- The resource ID to include in key requests.
RoleArn (string) -- An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.
SystemIds (list) -- The system IDs to include in key requests.
(string) --


Url (string) -- The URL of the external key provider service.




IncludeIframeOnlyStream (boolean) -- When enabled, an I-Frame only stream will be included in the output.
PlaylistType (string) -- The HTTP Live Streaming (HLS) playlist type. When either "EVENT" or "VOD" is specified, a corresponding EXT-X-PLAYLIST-TYPE entry will be included in the media playlist.
PlaylistWindowSeconds (integer) -- Time window (in seconds) contained in each parent manifest.
ProgramDateTimeIntervalSeconds (integer) -- The interval (in seconds) between each EXT-X-PROGRAM-DATE-TIME tag inserted into manifests. Additionally, when an interval is specified ID3Timed Metadata messages will be generated every 5 seconds using the ingest time of the content. If the interval is not specified, or set to 0, then no EXT-X-PROGRAM-DATE-TIME tags will be inserted into manifests and no ID3Timed Metadata messages will be generated. Note that irrespective of this parameter, if any ID3 Timed Metadata is found in HTTP Live Streaming (HLS) input, it will be passed through to HLS output.
SegmentDurationSeconds (integer) -- Duration (in seconds) of each fragment. Actual fragments will be rounded to the nearest multiple of the source fragment duration.
StreamSelection (dict) -- A StreamSelection configuration.
MaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.
MinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.
StreamOrder (string) -- A directive that determines the order of streams in the output.


UseAudioRenditionGroup (boolean) -- When enabled, audio streams will be placed in rendition groups in the output.


Id (string) -- The ID of the OriginEndpoint.
ManifestName (string) -- A short string appended to the end of the OriginEndpoint URL.
MssPackage (dict) -- A Microsoft Smooth Streaming (MSS) packaging configuration.
Encryption (dict) -- A Microsoft Smooth Streaming (MSS) encryption configuration.
SpekeKeyProvider (dict) -- A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
CertificateArn (string) -- An Amazon Resource Name (ARN) of a Certificate Manager certificate that MediaPackage will use for enforcing secure end-to-end data transfer with the key provider service.
ResourceId (string) -- The resource ID to include in key requests.
RoleArn (string) -- An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.
SystemIds (list) -- The system IDs to include in key requests.
(string) --


Url (string) -- The URL of the external key provider service.




ManifestWindowSeconds (integer) -- The time window (in seconds) contained in each manifest.
SegmentDurationSeconds (integer) -- The duration (in seconds) of each segment.
StreamSelection (dict) -- A StreamSelection configuration.
MaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.
MinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.
StreamOrder (string) -- A directive that determines the order of streams in the output.




Origination (string) -- Control whether origination of video is allowed for this OriginEndpoint. If set to ALLOW, the OriginEndpoint may by requested, pursuant to any other form of access control. If set to DENY, the OriginEndpoint may not be requested. This can be helpful for Live to VOD harvesting, or for temporarily disabling origination
StartoverWindowSeconds (integer) -- Maximum duration (seconds) of content to retain for startover playback. If not specified, startover playback will be disabled for the OriginEndpoint.
Tags (dict) -- A collection of tags associated with a resource
(string) --
(string) --




TimeDelaySeconds (integer) -- Amount of delay (seconds) to enforce on the playback of live content. If not specified, there will be no time delay in effect for the OriginEndpoint.
Url (string) -- The URL of the packaged OriginEndpoint for consumption.
Whitelist (list) -- A list of source IP CIDR blocks that will be allowed to access the OriginEndpoint.
(string) --








Exceptions

MediaPackage.Client.exceptions.UnprocessableEntityException
MediaPackage.Client.exceptions.InternalServerErrorException
MediaPackage.Client.exceptions.ForbiddenException
MediaPackage.Client.exceptions.NotFoundException
MediaPackage.Client.exceptions.ServiceUnavailableException
MediaPackage.Client.exceptions.TooManyRequestsException


    :return: {
        'Arn': 'string',
        'Authorization': {
            'CdnIdentifierSecret': 'string',
            'SecretsRoleArn': 'string'
        },
        'ChannelId': 'string',
        'CmafPackage': {
            'Encryption': {
                'KeyRotationIntervalSeconds': 123,
                'SpekeKeyProvider': {
                    'CertificateArn': 'string',
                    'ResourceId': 'string',
                    'RoleArn': 'string',
                    'SystemIds': [
                        'string',
                    ],
                    'Url': 'string'
                }
            },
            'HlsManifests': [
                {
                    'AdMarkers': 'NONE'|'SCTE35_ENHANCED'|'PASSTHROUGH',
                    'Id': 'string',
                    'IncludeIframeOnlyStream': True|False,
                    'ManifestName': 'string',
                    'PlaylistType': 'NONE'|'EVENT'|'VOD',
                    'PlaylistWindowSeconds': 123,
                    'ProgramDateTimeIntervalSeconds': 123,
                    'Url': 'string'
                },
            ],
            'SegmentDurationSeconds': 123,
            'SegmentPrefix': 'string',
            'StreamSelection': {
                'MaxVideoBitsPerSecond': 123,
                'MinVideoBitsPerSecond': 123,
                'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
            }
        },
        'DashPackage': {
            'AdTriggers': [
                'SPLICE_INSERT'|'BREAK'|'PROVIDER_ADVERTISEMENT'|'DISTRIBUTOR_ADVERTISEMENT'|'PROVIDER_PLACEMENT_OPPORTUNITY'|'DISTRIBUTOR_PLACEMENT_OPPORTUNITY'|'PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY'|'DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY',
            ],
            'AdsOnDeliveryRestrictions': 'NONE'|'RESTRICTED'|'UNRESTRICTED'|'BOTH',
            'Encryption': {
                'KeyRotationIntervalSeconds': 123,
                'SpekeKeyProvider': {
                    'CertificateArn': 'string',
                    'ResourceId': 'string',
                    'RoleArn': 'string',
                    'SystemIds': [
                        'string',
                    ],
                    'Url': 'string'
                }
            },
            'ManifestLayout': 'FULL'|'COMPACT',
            'ManifestWindowSeconds': 123,
            'MinBufferTimeSeconds': 123,
            'MinUpdatePeriodSeconds': 123,
            'PeriodTriggers': [
                'ADS',
            ],
            'Profile': 'NONE'|'HBBTV_1_5',
            'SegmentDurationSeconds': 123,
            'SegmentTemplateFormat': 'NUMBER_WITH_TIMELINE'|'TIME_WITH_TIMELINE'|'NUMBER_WITH_DURATION',
            'StreamSelection': {
                'MaxVideoBitsPerSecond': 123,
                'MinVideoBitsPerSecond': 123,
                'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
            },
            'SuggestedPresentationDelaySeconds': 123
        },
        'Description': 'string',
        'HlsPackage': {
            'AdMarkers': 'NONE'|'SCTE35_ENHANCED'|'PASSTHROUGH',
            'AdTriggers': [
                'SPLICE_INSERT'|'BREAK'|'PROVIDER_ADVERTISEMENT'|'DISTRIBUTOR_ADVERTISEMENT'|'PROVIDER_PLACEMENT_OPPORTUNITY'|'DISTRIBUTOR_PLACEMENT_OPPORTUNITY'|'PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY'|'DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY',
            ],
            'AdsOnDeliveryRestrictions': 'NONE'|'RESTRICTED'|'UNRESTRICTED'|'BOTH',
            'Encryption': {
                'ConstantInitializationVector': 'string',
                'EncryptionMethod': 'AES_128'|'SAMPLE_AES',
                'KeyRotationIntervalSeconds': 123,
                'RepeatExtXKey': True|False,
                'SpekeKeyProvider': {
                    'CertificateArn': 'string',
                    'ResourceId': 'string',
                    'RoleArn': 'string',
                    'SystemIds': [
                        'string',
                    ],
                    'Url': 'string'
                }
            },
            'IncludeIframeOnlyStream': True|False,
            'PlaylistType': 'NONE'|'EVENT'|'VOD',
            'PlaylistWindowSeconds': 123,
            'ProgramDateTimeIntervalSeconds': 123,
            'SegmentDurationSeconds': 123,
            'StreamSelection': {
                'MaxVideoBitsPerSecond': 123,
                'MinVideoBitsPerSecond': 123,
                'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
            },
            'UseAudioRenditionGroup': True|False
        },
        'Id': 'string',
        'ManifestName': 'string',
        'MssPackage': {
            'Encryption': {
                'SpekeKeyProvider': {
                    'CertificateArn': 'string',
                    'ResourceId': 'string',
                    'RoleArn': 'string',
                    'SystemIds': [
                        'string',
                    ],
                    'Url': 'string'
                }
            },
            'ManifestWindowSeconds': 123,
            'SegmentDurationSeconds': 123,
            'StreamSelection': {
                'MaxVideoBitsPerSecond': 123,
                'MinVideoBitsPerSecond': 123,
                'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
            }
        },
        'Origination': 'ALLOW'|'DENY',
        'StartoverWindowSeconds': 123,
        'Tags': {
            'string': 'string'
        },
        'TimeDelaySeconds': 123,
        'Url': 'string',
        'Whitelist': [
            'string',
        ]
    }
    
    
    :returns: 
    (dict) -- A new OriginEndpoint record.
    Arn (string) -- The Amazon Resource Name (ARN) assigned to the OriginEndpoint.
    Authorization (dict) -- CDN Authorization credentials
    CdnIdentifierSecret (string) -- The Amazon Resource Name (ARN) for the secret in Secrets Manager that your Content Distribution Network (CDN) uses for authorization to access your endpoint.
    SecretsRoleArn (string) -- The Amazon Resource Name (ARN) for the IAM role that allows MediaPackage to communicate with AWS Secrets Manager.
    
    
    ChannelId (string) -- The ID of the Channel the OriginEndpoint is associated with.
    CmafPackage (dict) -- A Common Media Application Format (CMAF) packaging configuration.
    Encryption (dict) -- A Common Media Application Format (CMAF) encryption configuration.
    KeyRotationIntervalSeconds (integer) -- Time (in seconds) between each encryption key rotation.
    SpekeKeyProvider (dict) -- A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
    CertificateArn (string) -- An Amazon Resource Name (ARN) of a Certificate Manager certificate that MediaPackage will use for enforcing secure end-to-end data transfer with the key provider service.
    ResourceId (string) -- The resource ID to include in key requests.
    RoleArn (string) -- An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.
    SystemIds (list) -- The system IDs to include in key requests.
    (string) --
    
    
    Url (string) -- The URL of the external key provider service.
    
    
    
    
    HlsManifests (list) -- A list of HLS manifest configurations
    (dict) -- A HTTP Live Streaming (HLS) manifest configuration.
    AdMarkers (string) -- This setting controls how ad markers are included in the packaged OriginEndpoint. "NONE" will omit all SCTE-35 ad markers from the output. "PASSTHROUGH" causes the manifest to contain a copy of the SCTE-35 ad markers (comments) taken directly from the input HTTP Live Streaming (HLS) manifest. "SCTE35_ENHANCED" generates ad markers and blackout tags based on SCTE-35 messages in the input source.
    Id (string) -- The ID of the manifest. The ID must be unique within the OriginEndpoint and it cannot be changed after it is created.
    IncludeIframeOnlyStream (boolean) -- When enabled, an I-Frame only stream will be included in the output.
    ManifestName (string) -- An optional short string appended to the end of the OriginEndpoint URL. If not specified, defaults to the manifestName for the OriginEndpoint.
    PlaylistType (string) -- The HTTP Live Streaming (HLS) playlist type. When either "EVENT" or "VOD" is specified, a corresponding EXT-X-PLAYLIST-TYPE entry will be included in the media playlist.
    PlaylistWindowSeconds (integer) -- Time window (in seconds) contained in each parent manifest.
    ProgramDateTimeIntervalSeconds (integer) -- The interval (in seconds) between each EXT-X-PROGRAM-DATE-TIME tag inserted into manifests. Additionally, when an interval is specified ID3Timed Metadata messages will be generated every 5 seconds using the ingest time of the content. If the interval is not specified, or set to 0, then no EXT-X-PROGRAM-DATE-TIME tags will be inserted into manifests and no ID3Timed Metadata messages will be generated. Note that irrespective of this parameter, if any ID3 Timed Metadata is found in HTTP Live Streaming (HLS) input, it will be passed through to HLS output.
    Url (string) -- The URL of the packaged OriginEndpoint for consumption.
    
    
    
    
    SegmentDurationSeconds (integer) -- Duration (in seconds) of each segment. Actual segments will be rounded to the nearest multiple of the source segment duration.
    SegmentPrefix (string) -- An optional custom string that is prepended to the name of each segment. If not specified, it defaults to the ChannelId.
    StreamSelection (dict) -- A StreamSelection configuration.
    MaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.
    MinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.
    StreamOrder (string) -- A directive that determines the order of streams in the output.
    
    
    
    
    DashPackage (dict) -- A Dynamic Adaptive Streaming over HTTP (DASH) packaging configuration.
    AdTriggers (list) -- A list of SCTE-35 message types that are treated as ad markers in the output. If empty, no ad markers are output. Specify multiple items to create ad markers for all of the included message types.
    (string) --
    
    
    AdsOnDeliveryRestrictions (string) -- This setting allows the delivery restriction flags on SCTE-35 segmentation descriptors to determine whether a message signals an ad. Choosing "NONE" means no SCTE-35 messages become ads. Choosing "RESTRICTED" means SCTE-35 messages of the types specified in AdTriggers that contain delivery restrictions will be treated as ads. Choosing "UNRESTRICTED" means SCTE-35 messages of the types specified in AdTriggers that do not contain delivery restrictions will be treated as ads. Choosing "BOTH" means all SCTE-35 messages of the types specified in AdTriggers will be treated as ads. Note that Splice Insert messages do not have these flags and are always treated as ads if specified in AdTriggers.
    Encryption (dict) -- A Dynamic Adaptive Streaming over HTTP (DASH) encryption configuration.
    KeyRotationIntervalSeconds (integer) -- Time (in seconds) between each encryption key rotation.
    SpekeKeyProvider (dict) -- A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
    CertificateArn (string) -- An Amazon Resource Name (ARN) of a Certificate Manager certificate that MediaPackage will use for enforcing secure end-to-end data transfer with the key provider service.
    ResourceId (string) -- The resource ID to include in key requests.
    RoleArn (string) -- An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.
    SystemIds (list) -- The system IDs to include in key requests.
    (string) --
    
    
    Url (string) -- The URL of the external key provider service.
    
    
    
    
    ManifestLayout (string) -- Determines the position of some tags in the Media Presentation Description (MPD). When set to FULL, elements like SegmentTemplate and ContentProtection are included in each Representation. When set to COMPACT, duplicate elements are combined and presented at the AdaptationSet level.
    ManifestWindowSeconds (integer) -- Time window (in seconds) contained in each manifest.
    MinBufferTimeSeconds (integer) -- Minimum duration (in seconds) that a player will buffer media before starting the presentation.
    MinUpdatePeriodSeconds (integer) -- Minimum duration (in seconds) between potential changes to the Dynamic Adaptive Streaming over HTTP (DASH) Media Presentation Description (MPD).
    PeriodTriggers (list) -- A list of triggers that controls when the outgoing Dynamic Adaptive Streaming over HTTP (DASH) Media Presentation Description (MPD) will be partitioned into multiple periods. If empty, the content will not be partitioned into more than one period. If the list contains "ADS", new periods will be created where the Channel source contains SCTE-35 ad markers.
    (string) --
    
    
    Profile (string) -- The Dynamic Adaptive Streaming over HTTP (DASH) profile type. When set to "HBBTV_1_5", HbbTV 1.5 compliant output is enabled.
    SegmentDurationSeconds (integer) -- Duration (in seconds) of each segment. Actual segments will be rounded to the nearest multiple of the source segment duration.
    SegmentTemplateFormat (string) -- Determines the type of SegmentTemplate included in the Media Presentation Description (MPD). When set to NUMBER_WITH_TIMELINE, a full timeline is presented in each SegmentTemplate, with $Number$ media URLs. When set to TIME_WITH_TIMELINE, a full timeline is presented in each SegmentTemplate, with $Time$ media URLs. When set to NUMBER_WITH_DURATION, only a duration is included in each SegmentTemplate, with $Number$ media URLs.
    StreamSelection (dict) -- A StreamSelection configuration.
    MaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.
    MinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.
    StreamOrder (string) -- A directive that determines the order of streams in the output.
    
    
    SuggestedPresentationDelaySeconds (integer) -- Duration (in seconds) to delay live content before presentation.
    
    
    Description (string) -- A short text description of the OriginEndpoint.
    HlsPackage (dict) -- An HTTP Live Streaming (HLS) packaging configuration.
    AdMarkers (string) -- This setting controls how ad markers are included in the packaged OriginEndpoint. "NONE" will omit all SCTE-35 ad markers from the output. "PASSTHROUGH" causes the manifest to contain a copy of the SCTE-35 ad markers (comments) taken directly from the input HTTP Live Streaming (HLS) manifest. "SCTE35_ENHANCED" generates ad markers and blackout tags based on SCTE-35 messages in the input source.
    AdTriggers (list) -- A list of SCTE-35 message types that are treated as ad markers in the output. If empty, no ad markers are output. Specify multiple items to create ad markers for all of the included message types.
    (string) --
    
    
    AdsOnDeliveryRestrictions (string) -- This setting allows the delivery restriction flags on SCTE-35 segmentation descriptors to determine whether a message signals an ad. Choosing "NONE" means no SCTE-35 messages become ads. Choosing "RESTRICTED" means SCTE-35 messages of the types specified in AdTriggers that contain delivery restrictions will be treated as ads. Choosing "UNRESTRICTED" means SCTE-35 messages of the types specified in AdTriggers that do not contain delivery restrictions will be treated as ads. Choosing "BOTH" means all SCTE-35 messages of the types specified in AdTriggers will be treated as ads. Note that Splice Insert messages do not have these flags and are always treated as ads if specified in AdTriggers.
    Encryption (dict) -- An HTTP Live Streaming (HLS) encryption configuration.
    ConstantInitializationVector (string) -- A constant initialization vector for encryption (optional). When not specified the initialization vector will be periodically rotated.
    EncryptionMethod (string) -- The encryption method to use.
    KeyRotationIntervalSeconds (integer) -- Interval (in seconds) between each encryption key rotation.
    RepeatExtXKey (boolean) -- When enabled, the EXT-X-KEY tag will be repeated in output manifests.
    SpekeKeyProvider (dict) -- A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
    CertificateArn (string) -- An Amazon Resource Name (ARN) of a Certificate Manager certificate that MediaPackage will use for enforcing secure end-to-end data transfer with the key provider service.
    ResourceId (string) -- The resource ID to include in key requests.
    RoleArn (string) -- An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.
    SystemIds (list) -- The system IDs to include in key requests.
    (string) --
    
    
    Url (string) -- The URL of the external key provider service.
    
    
    
    
    IncludeIframeOnlyStream (boolean) -- When enabled, an I-Frame only stream will be included in the output.
    PlaylistType (string) -- The HTTP Live Streaming (HLS) playlist type. When either "EVENT" or "VOD" is specified, a corresponding EXT-X-PLAYLIST-TYPE entry will be included in the media playlist.
    PlaylistWindowSeconds (integer) -- Time window (in seconds) contained in each parent manifest.
    ProgramDateTimeIntervalSeconds (integer) -- The interval (in seconds) between each EXT-X-PROGRAM-DATE-TIME tag inserted into manifests. Additionally, when an interval is specified ID3Timed Metadata messages will be generated every 5 seconds using the ingest time of the content. If the interval is not specified, or set to 0, then no EXT-X-PROGRAM-DATE-TIME tags will be inserted into manifests and no ID3Timed Metadata messages will be generated. Note that irrespective of this parameter, if any ID3 Timed Metadata is found in HTTP Live Streaming (HLS) input, it will be passed through to HLS output.
    SegmentDurationSeconds (integer) -- Duration (in seconds) of each fragment. Actual fragments will be rounded to the nearest multiple of the source fragment duration.
    StreamSelection (dict) -- A StreamSelection configuration.
    MaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.
    MinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.
    StreamOrder (string) -- A directive that determines the order of streams in the output.
    
    
    UseAudioRenditionGroup (boolean) -- When enabled, audio streams will be placed in rendition groups in the output.
    
    
    Id (string) -- The ID of the OriginEndpoint.
    ManifestName (string) -- A short string appended to the end of the OriginEndpoint URL.
    MssPackage (dict) -- A Microsoft Smooth Streaming (MSS) packaging configuration.
    Encryption (dict) -- A Microsoft Smooth Streaming (MSS) encryption configuration.
    SpekeKeyProvider (dict) -- A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
    CertificateArn (string) -- An Amazon Resource Name (ARN) of a Certificate Manager certificate that MediaPackage will use for enforcing secure end-to-end data transfer with the key provider service.
    ResourceId (string) -- The resource ID to include in key requests.
    RoleArn (string) -- An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.
    SystemIds (list) -- The system IDs to include in key requests.
    (string) --
    
    
    Url (string) -- The URL of the external key provider service.
    
    
    
    
    ManifestWindowSeconds (integer) -- The time window (in seconds) contained in each manifest.
    SegmentDurationSeconds (integer) -- The duration (in seconds) of each segment.
    StreamSelection (dict) -- A StreamSelection configuration.
    MaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.
    MinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.
    StreamOrder (string) -- A directive that determines the order of streams in the output.
    
    
    
    
    Origination (string) -- Control whether origination of video is allowed for this OriginEndpoint. If set to ALLOW, the OriginEndpoint may by requested, pursuant to any other form of access control. If set to DENY, the OriginEndpoint may not be requested. This can be helpful for Live to VOD harvesting, or for temporarily disabling origination
    StartoverWindowSeconds (integer) -- Maximum duration (seconds) of content to retain for startover playback. If not specified, startover playback will be disabled for the OriginEndpoint.
    Tags (dict) -- A collection of tags associated with a resource
    (string) --
    (string) --
    
    
    
    
    TimeDelaySeconds (integer) -- Amount of delay (seconds) to enforce on the playback of live content. If not specified, there will be no time delay in effect for the OriginEndpoint.
    Url (string) -- The URL of the packaged OriginEndpoint for consumption.
    Whitelist (list) -- A list of source IP CIDR blocks that will be allowed to access the OriginEndpoint.
    (string) --
    
    
    
    
    
    """
    pass

def delete_channel(Id=None):
    """
    Deletes an existing Channel.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_channel(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED] The ID of the Channel to delete.

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) -- The Channel has been deleted.



Exceptions

MediaPackage.Client.exceptions.UnprocessableEntityException
MediaPackage.Client.exceptions.InternalServerErrorException
MediaPackage.Client.exceptions.ForbiddenException
MediaPackage.Client.exceptions.NotFoundException
MediaPackage.Client.exceptions.ServiceUnavailableException
MediaPackage.Client.exceptions.TooManyRequestsException


    :return: {}
    
    
    :returns: 
    MediaPackage.Client.exceptions.UnprocessableEntityException
    MediaPackage.Client.exceptions.InternalServerErrorException
    MediaPackage.Client.exceptions.ForbiddenException
    MediaPackage.Client.exceptions.NotFoundException
    MediaPackage.Client.exceptions.ServiceUnavailableException
    MediaPackage.Client.exceptions.TooManyRequestsException
    
    """
    pass

def delete_origin_endpoint(Id=None):
    """
    Deletes an existing OriginEndpoint.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_origin_endpoint(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED] The ID of the OriginEndpoint to delete.

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) -- The OriginEndpoint has been deleted.



Exceptions

MediaPackage.Client.exceptions.UnprocessableEntityException
MediaPackage.Client.exceptions.InternalServerErrorException
MediaPackage.Client.exceptions.ForbiddenException
MediaPackage.Client.exceptions.NotFoundException
MediaPackage.Client.exceptions.ServiceUnavailableException
MediaPackage.Client.exceptions.TooManyRequestsException


    :return: {}
    
    
    :returns: 
    MediaPackage.Client.exceptions.UnprocessableEntityException
    MediaPackage.Client.exceptions.InternalServerErrorException
    MediaPackage.Client.exceptions.ForbiddenException
    MediaPackage.Client.exceptions.NotFoundException
    MediaPackage.Client.exceptions.ServiceUnavailableException
    MediaPackage.Client.exceptions.TooManyRequestsException
    
    """
    pass

def describe_channel(Id=None):
    """
    Gets details about a Channel.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_channel(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED] The ID of a Channel.

    :rtype: dict
ReturnsResponse Syntax{
    'Arn': 'string',
    'Description': 'string',
    'HlsIngest': {
        'IngestEndpoints': [
            {
                'Id': 'string',
                'Password': 'string',
                'Url': 'string',
                'Username': 'string'
            },
        ]
    },
    'Id': 'string',
    'Tags': {
        'string': 'string'
    }
}


Response Structure

(dict) -- A Channel record.
Arn (string) -- The Amazon Resource Name (ARN) assigned to the Channel.
Description (string) -- A short text description of the Channel.
HlsIngest (dict) -- An HTTP Live Streaming (HLS) ingest resource configuration.
IngestEndpoints (list) -- A list of endpoints to which the source stream should be sent.
(dict) -- An endpoint for ingesting source content for a Channel.
Id (string) -- The system generated unique identifier for the IngestEndpoint
Password (string) -- The system generated password for ingest authentication.
Url (string) -- The ingest URL to which the source stream should be sent.
Username (string) -- The system generated username for ingest authentication.






Id (string) -- The ID of the Channel.
Tags (dict) -- A collection of tags associated with a resource
(string) --
(string) --









Exceptions

MediaPackage.Client.exceptions.UnprocessableEntityException
MediaPackage.Client.exceptions.InternalServerErrorException
MediaPackage.Client.exceptions.ForbiddenException
MediaPackage.Client.exceptions.NotFoundException
MediaPackage.Client.exceptions.ServiceUnavailableException
MediaPackage.Client.exceptions.TooManyRequestsException


    :return: {
        'Arn': 'string',
        'Description': 'string',
        'HlsIngest': {
            'IngestEndpoints': [
                {
                    'Id': 'string',
                    'Password': 'string',
                    'Url': 'string',
                    'Username': 'string'
                },
            ]
        },
        'Id': 'string',
        'Tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    MediaPackage.Client.exceptions.UnprocessableEntityException
    MediaPackage.Client.exceptions.InternalServerErrorException
    MediaPackage.Client.exceptions.ForbiddenException
    MediaPackage.Client.exceptions.NotFoundException
    MediaPackage.Client.exceptions.ServiceUnavailableException
    MediaPackage.Client.exceptions.TooManyRequestsException
    
    """
    pass

def describe_harvest_job(Id=None):
    """
    Gets details about an existing HarvestJob.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_harvest_job(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED] The ID of the HarvestJob.

    :rtype: dict
ReturnsResponse Syntax{
    'Arn': 'string',
    'ChannelId': 'string',
    'CreatedAt': 'string',
    'EndTime': 'string',
    'Id': 'string',
    'OriginEndpointId': 'string',
    'S3Destination': {
        'BucketName': 'string',
        'ManifestKey': 'string',
        'RoleArn': 'string'
    },
    'StartTime': 'string',
    'Status': 'IN_PROGRESS'|'SUCCEEDED'|'FAILED'
}


Response Structure

(dict) -- An HarvestJob record.
Arn (string) -- The Amazon Resource Name (ARN) assigned to the HarvestJob.
ChannelId (string) -- The ID of the Channel that the HarvestJob will harvest from.
CreatedAt (string) -- The time the HarvestJob was submitted
EndTime (string) -- The end of the time-window which will be harvested.
Id (string) -- The ID of the HarvestJob. The ID must be unique within the region and it cannot be changed after the HarvestJob is submitted.
OriginEndpointId (string) -- The ID of the OriginEndpoint that the HarvestJob will harvest from. This cannot be changed after the HarvestJob is submitted.
S3Destination (dict) -- Configuration parameters for where in an S3 bucket to place the harvested content
BucketName (string) -- The name of an S3 bucket within which harvested content will be exported
ManifestKey (string) -- The key in the specified S3 bucket where the harvested top-level manifest will be placed.
RoleArn (string) -- The IAM role used to write to the specified S3 bucket


StartTime (string) -- The start of the time-window which will be harvested.
Status (string) -- The current status of the HarvestJob. Consider setting up a CloudWatch Event to listen for HarvestJobs as they succeed or fail. In the event of failure, the CloudWatch Event will include an explanation of why the HarvestJob failed.





Exceptions

MediaPackage.Client.exceptions.UnprocessableEntityException
MediaPackage.Client.exceptions.InternalServerErrorException
MediaPackage.Client.exceptions.ForbiddenException
MediaPackage.Client.exceptions.NotFoundException
MediaPackage.Client.exceptions.ServiceUnavailableException
MediaPackage.Client.exceptions.TooManyRequestsException


    :return: {
        'Arn': 'string',
        'ChannelId': 'string',
        'CreatedAt': 'string',
        'EndTime': 'string',
        'Id': 'string',
        'OriginEndpointId': 'string',
        'S3Destination': {
            'BucketName': 'string',
            'ManifestKey': 'string',
            'RoleArn': 'string'
        },
        'StartTime': 'string',
        'Status': 'IN_PROGRESS'|'SUCCEEDED'|'FAILED'
    }
    
    
    :returns: 
    MediaPackage.Client.exceptions.UnprocessableEntityException
    MediaPackage.Client.exceptions.InternalServerErrorException
    MediaPackage.Client.exceptions.ForbiddenException
    MediaPackage.Client.exceptions.NotFoundException
    MediaPackage.Client.exceptions.ServiceUnavailableException
    MediaPackage.Client.exceptions.TooManyRequestsException
    
    """
    pass

def describe_origin_endpoint(Id=None):
    """
    Gets details about an existing OriginEndpoint.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_origin_endpoint(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED] The ID of the OriginEndpoint.

    :rtype: dict
ReturnsResponse Syntax{
    'Arn': 'string',
    'Authorization': {
        'CdnIdentifierSecret': 'string',
        'SecretsRoleArn': 'string'
    },
    'ChannelId': 'string',
    'CmafPackage': {
        'Encryption': {
            'KeyRotationIntervalSeconds': 123,
            'SpekeKeyProvider': {
                'CertificateArn': 'string',
                'ResourceId': 'string',
                'RoleArn': 'string',
                'SystemIds': [
                    'string',
                ],
                'Url': 'string'
            }
        },
        'HlsManifests': [
            {
                'AdMarkers': 'NONE'|'SCTE35_ENHANCED'|'PASSTHROUGH',
                'Id': 'string',
                'IncludeIframeOnlyStream': True|False,
                'ManifestName': 'string',
                'PlaylistType': 'NONE'|'EVENT'|'VOD',
                'PlaylistWindowSeconds': 123,
                'ProgramDateTimeIntervalSeconds': 123,
                'Url': 'string'
            },
        ],
        'SegmentDurationSeconds': 123,
        'SegmentPrefix': 'string',
        'StreamSelection': {
            'MaxVideoBitsPerSecond': 123,
            'MinVideoBitsPerSecond': 123,
            'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
        }
    },
    'DashPackage': {
        'AdTriggers': [
            'SPLICE_INSERT'|'BREAK'|'PROVIDER_ADVERTISEMENT'|'DISTRIBUTOR_ADVERTISEMENT'|'PROVIDER_PLACEMENT_OPPORTUNITY'|'DISTRIBUTOR_PLACEMENT_OPPORTUNITY'|'PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY'|'DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY',
        ],
        'AdsOnDeliveryRestrictions': 'NONE'|'RESTRICTED'|'UNRESTRICTED'|'BOTH',
        'Encryption': {
            'KeyRotationIntervalSeconds': 123,
            'SpekeKeyProvider': {
                'CertificateArn': 'string',
                'ResourceId': 'string',
                'RoleArn': 'string',
                'SystemIds': [
                    'string',
                ],
                'Url': 'string'
            }
        },
        'ManifestLayout': 'FULL'|'COMPACT',
        'ManifestWindowSeconds': 123,
        'MinBufferTimeSeconds': 123,
        'MinUpdatePeriodSeconds': 123,
        'PeriodTriggers': [
            'ADS',
        ],
        'Profile': 'NONE'|'HBBTV_1_5',
        'SegmentDurationSeconds': 123,
        'SegmentTemplateFormat': 'NUMBER_WITH_TIMELINE'|'TIME_WITH_TIMELINE'|'NUMBER_WITH_DURATION',
        'StreamSelection': {
            'MaxVideoBitsPerSecond': 123,
            'MinVideoBitsPerSecond': 123,
            'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
        },
        'SuggestedPresentationDelaySeconds': 123
    },
    'Description': 'string',
    'HlsPackage': {
        'AdMarkers': 'NONE'|'SCTE35_ENHANCED'|'PASSTHROUGH',
        'AdTriggers': [
            'SPLICE_INSERT'|'BREAK'|'PROVIDER_ADVERTISEMENT'|'DISTRIBUTOR_ADVERTISEMENT'|'PROVIDER_PLACEMENT_OPPORTUNITY'|'DISTRIBUTOR_PLACEMENT_OPPORTUNITY'|'PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY'|'DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY',
        ],
        'AdsOnDeliveryRestrictions': 'NONE'|'RESTRICTED'|'UNRESTRICTED'|'BOTH',
        'Encryption': {
            'ConstantInitializationVector': 'string',
            'EncryptionMethod': 'AES_128'|'SAMPLE_AES',
            'KeyRotationIntervalSeconds': 123,
            'RepeatExtXKey': True|False,
            'SpekeKeyProvider': {
                'CertificateArn': 'string',
                'ResourceId': 'string',
                'RoleArn': 'string',
                'SystemIds': [
                    'string',
                ],
                'Url': 'string'
            }
        },
        'IncludeIframeOnlyStream': True|False,
        'PlaylistType': 'NONE'|'EVENT'|'VOD',
        'PlaylistWindowSeconds': 123,
        'ProgramDateTimeIntervalSeconds': 123,
        'SegmentDurationSeconds': 123,
        'StreamSelection': {
            'MaxVideoBitsPerSecond': 123,
            'MinVideoBitsPerSecond': 123,
            'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
        },
        'UseAudioRenditionGroup': True|False
    },
    'Id': 'string',
    'ManifestName': 'string',
    'MssPackage': {
        'Encryption': {
            'SpekeKeyProvider': {
                'CertificateArn': 'string',
                'ResourceId': 'string',
                'RoleArn': 'string',
                'SystemIds': [
                    'string',
                ],
                'Url': 'string'
            }
        },
        'ManifestWindowSeconds': 123,
        'SegmentDurationSeconds': 123,
        'StreamSelection': {
            'MaxVideoBitsPerSecond': 123,
            'MinVideoBitsPerSecond': 123,
            'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
        }
    },
    'Origination': 'ALLOW'|'DENY',
    'StartoverWindowSeconds': 123,
    'Tags': {
        'string': 'string'
    },
    'TimeDelaySeconds': 123,
    'Url': 'string',
    'Whitelist': [
        'string',
    ]
}


Response Structure

(dict) -- An OriginEndpoint record.
Arn (string) -- The Amazon Resource Name (ARN) assigned to the OriginEndpoint.
Authorization (dict) -- CDN Authorization credentials
CdnIdentifierSecret (string) -- The Amazon Resource Name (ARN) for the secret in Secrets Manager that your Content Distribution Network (CDN) uses for authorization to access your endpoint.
SecretsRoleArn (string) -- The Amazon Resource Name (ARN) for the IAM role that allows MediaPackage to communicate with AWS Secrets Manager.


ChannelId (string) -- The ID of the Channel the OriginEndpoint is associated with.
CmafPackage (dict) -- A Common Media Application Format (CMAF) packaging configuration.
Encryption (dict) -- A Common Media Application Format (CMAF) encryption configuration.
KeyRotationIntervalSeconds (integer) -- Time (in seconds) between each encryption key rotation.
SpekeKeyProvider (dict) -- A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
CertificateArn (string) -- An Amazon Resource Name (ARN) of a Certificate Manager certificate that MediaPackage will use for enforcing secure end-to-end data transfer with the key provider service.
ResourceId (string) -- The resource ID to include in key requests.
RoleArn (string) -- An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.
SystemIds (list) -- The system IDs to include in key requests.
(string) --


Url (string) -- The URL of the external key provider service.




HlsManifests (list) -- A list of HLS manifest configurations
(dict) -- A HTTP Live Streaming (HLS) manifest configuration.
AdMarkers (string) -- This setting controls how ad markers are included in the packaged OriginEndpoint. "NONE" will omit all SCTE-35 ad markers from the output. "PASSTHROUGH" causes the manifest to contain a copy of the SCTE-35 ad markers (comments) taken directly from the input HTTP Live Streaming (HLS) manifest. "SCTE35_ENHANCED" generates ad markers and blackout tags based on SCTE-35 messages in the input source.
Id (string) -- The ID of the manifest. The ID must be unique within the OriginEndpoint and it cannot be changed after it is created.
IncludeIframeOnlyStream (boolean) -- When enabled, an I-Frame only stream will be included in the output.
ManifestName (string) -- An optional short string appended to the end of the OriginEndpoint URL. If not specified, defaults to the manifestName for the OriginEndpoint.
PlaylistType (string) -- The HTTP Live Streaming (HLS) playlist type. When either "EVENT" or "VOD" is specified, a corresponding EXT-X-PLAYLIST-TYPE entry will be included in the media playlist.
PlaylistWindowSeconds (integer) -- Time window (in seconds) contained in each parent manifest.
ProgramDateTimeIntervalSeconds (integer) -- The interval (in seconds) between each EXT-X-PROGRAM-DATE-TIME tag inserted into manifests. Additionally, when an interval is specified ID3Timed Metadata messages will be generated every 5 seconds using the ingest time of the content. If the interval is not specified, or set to 0, then no EXT-X-PROGRAM-DATE-TIME tags will be inserted into manifests and no ID3Timed Metadata messages will be generated. Note that irrespective of this parameter, if any ID3 Timed Metadata is found in HTTP Live Streaming (HLS) input, it will be passed through to HLS output.
Url (string) -- The URL of the packaged OriginEndpoint for consumption.




SegmentDurationSeconds (integer) -- Duration (in seconds) of each segment. Actual segments will be rounded to the nearest multiple of the source segment duration.
SegmentPrefix (string) -- An optional custom string that is prepended to the name of each segment. If not specified, it defaults to the ChannelId.
StreamSelection (dict) -- A StreamSelection configuration.
MaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.
MinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.
StreamOrder (string) -- A directive that determines the order of streams in the output.




DashPackage (dict) -- A Dynamic Adaptive Streaming over HTTP (DASH) packaging configuration.
AdTriggers (list) -- A list of SCTE-35 message types that are treated as ad markers in the output. If empty, no ad markers are output. Specify multiple items to create ad markers for all of the included message types.
(string) --


AdsOnDeliveryRestrictions (string) -- This setting allows the delivery restriction flags on SCTE-35 segmentation descriptors to determine whether a message signals an ad. Choosing "NONE" means no SCTE-35 messages become ads. Choosing "RESTRICTED" means SCTE-35 messages of the types specified in AdTriggers that contain delivery restrictions will be treated as ads. Choosing "UNRESTRICTED" means SCTE-35 messages of the types specified in AdTriggers that do not contain delivery restrictions will be treated as ads. Choosing "BOTH" means all SCTE-35 messages of the types specified in AdTriggers will be treated as ads. Note that Splice Insert messages do not have these flags and are always treated as ads if specified in AdTriggers.
Encryption (dict) -- A Dynamic Adaptive Streaming over HTTP (DASH) encryption configuration.
KeyRotationIntervalSeconds (integer) -- Time (in seconds) between each encryption key rotation.
SpekeKeyProvider (dict) -- A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
CertificateArn (string) -- An Amazon Resource Name (ARN) of a Certificate Manager certificate that MediaPackage will use for enforcing secure end-to-end data transfer with the key provider service.
ResourceId (string) -- The resource ID to include in key requests.
RoleArn (string) -- An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.
SystemIds (list) -- The system IDs to include in key requests.
(string) --


Url (string) -- The URL of the external key provider service.




ManifestLayout (string) -- Determines the position of some tags in the Media Presentation Description (MPD). When set to FULL, elements like SegmentTemplate and ContentProtection are included in each Representation. When set to COMPACT, duplicate elements are combined and presented at the AdaptationSet level.
ManifestWindowSeconds (integer) -- Time window (in seconds) contained in each manifest.
MinBufferTimeSeconds (integer) -- Minimum duration (in seconds) that a player will buffer media before starting the presentation.
MinUpdatePeriodSeconds (integer) -- Minimum duration (in seconds) between potential changes to the Dynamic Adaptive Streaming over HTTP (DASH) Media Presentation Description (MPD).
PeriodTriggers (list) -- A list of triggers that controls when the outgoing Dynamic Adaptive Streaming over HTTP (DASH) Media Presentation Description (MPD) will be partitioned into multiple periods. If empty, the content will not be partitioned into more than one period. If the list contains "ADS", new periods will be created where the Channel source contains SCTE-35 ad markers.
(string) --


Profile (string) -- The Dynamic Adaptive Streaming over HTTP (DASH) profile type. When set to "HBBTV_1_5", HbbTV 1.5 compliant output is enabled.
SegmentDurationSeconds (integer) -- Duration (in seconds) of each segment. Actual segments will be rounded to the nearest multiple of the source segment duration.
SegmentTemplateFormat (string) -- Determines the type of SegmentTemplate included in the Media Presentation Description (MPD). When set to NUMBER_WITH_TIMELINE, a full timeline is presented in each SegmentTemplate, with $Number$ media URLs. When set to TIME_WITH_TIMELINE, a full timeline is presented in each SegmentTemplate, with $Time$ media URLs. When set to NUMBER_WITH_DURATION, only a duration is included in each SegmentTemplate, with $Number$ media URLs.
StreamSelection (dict) -- A StreamSelection configuration.
MaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.
MinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.
StreamOrder (string) -- A directive that determines the order of streams in the output.


SuggestedPresentationDelaySeconds (integer) -- Duration (in seconds) to delay live content before presentation.


Description (string) -- A short text description of the OriginEndpoint.
HlsPackage (dict) -- An HTTP Live Streaming (HLS) packaging configuration.
AdMarkers (string) -- This setting controls how ad markers are included in the packaged OriginEndpoint. "NONE" will omit all SCTE-35 ad markers from the output. "PASSTHROUGH" causes the manifest to contain a copy of the SCTE-35 ad markers (comments) taken directly from the input HTTP Live Streaming (HLS) manifest. "SCTE35_ENHANCED" generates ad markers and blackout tags based on SCTE-35 messages in the input source.
AdTriggers (list) -- A list of SCTE-35 message types that are treated as ad markers in the output. If empty, no ad markers are output. Specify multiple items to create ad markers for all of the included message types.
(string) --


AdsOnDeliveryRestrictions (string) -- This setting allows the delivery restriction flags on SCTE-35 segmentation descriptors to determine whether a message signals an ad. Choosing "NONE" means no SCTE-35 messages become ads. Choosing "RESTRICTED" means SCTE-35 messages of the types specified in AdTriggers that contain delivery restrictions will be treated as ads. Choosing "UNRESTRICTED" means SCTE-35 messages of the types specified in AdTriggers that do not contain delivery restrictions will be treated as ads. Choosing "BOTH" means all SCTE-35 messages of the types specified in AdTriggers will be treated as ads. Note that Splice Insert messages do not have these flags and are always treated as ads if specified in AdTriggers.
Encryption (dict) -- An HTTP Live Streaming (HLS) encryption configuration.
ConstantInitializationVector (string) -- A constant initialization vector for encryption (optional). When not specified the initialization vector will be periodically rotated.
EncryptionMethod (string) -- The encryption method to use.
KeyRotationIntervalSeconds (integer) -- Interval (in seconds) between each encryption key rotation.
RepeatExtXKey (boolean) -- When enabled, the EXT-X-KEY tag will be repeated in output manifests.
SpekeKeyProvider (dict) -- A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
CertificateArn (string) -- An Amazon Resource Name (ARN) of a Certificate Manager certificate that MediaPackage will use for enforcing secure end-to-end data transfer with the key provider service.
ResourceId (string) -- The resource ID to include in key requests.
RoleArn (string) -- An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.
SystemIds (list) -- The system IDs to include in key requests.
(string) --


Url (string) -- The URL of the external key provider service.




IncludeIframeOnlyStream (boolean) -- When enabled, an I-Frame only stream will be included in the output.
PlaylistType (string) -- The HTTP Live Streaming (HLS) playlist type. When either "EVENT" or "VOD" is specified, a corresponding EXT-X-PLAYLIST-TYPE entry will be included in the media playlist.
PlaylistWindowSeconds (integer) -- Time window (in seconds) contained in each parent manifest.
ProgramDateTimeIntervalSeconds (integer) -- The interval (in seconds) between each EXT-X-PROGRAM-DATE-TIME tag inserted into manifests. Additionally, when an interval is specified ID3Timed Metadata messages will be generated every 5 seconds using the ingest time of the content. If the interval is not specified, or set to 0, then no EXT-X-PROGRAM-DATE-TIME tags will be inserted into manifests and no ID3Timed Metadata messages will be generated. Note that irrespective of this parameter, if any ID3 Timed Metadata is found in HTTP Live Streaming (HLS) input, it will be passed through to HLS output.
SegmentDurationSeconds (integer) -- Duration (in seconds) of each fragment. Actual fragments will be rounded to the nearest multiple of the source fragment duration.
StreamSelection (dict) -- A StreamSelection configuration.
MaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.
MinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.
StreamOrder (string) -- A directive that determines the order of streams in the output.


UseAudioRenditionGroup (boolean) -- When enabled, audio streams will be placed in rendition groups in the output.


Id (string) -- The ID of the OriginEndpoint.
ManifestName (string) -- A short string appended to the end of the OriginEndpoint URL.
MssPackage (dict) -- A Microsoft Smooth Streaming (MSS) packaging configuration.
Encryption (dict) -- A Microsoft Smooth Streaming (MSS) encryption configuration.
SpekeKeyProvider (dict) -- A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
CertificateArn (string) -- An Amazon Resource Name (ARN) of a Certificate Manager certificate that MediaPackage will use for enforcing secure end-to-end data transfer with the key provider service.
ResourceId (string) -- The resource ID to include in key requests.
RoleArn (string) -- An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.
SystemIds (list) -- The system IDs to include in key requests.
(string) --


Url (string) -- The URL of the external key provider service.




ManifestWindowSeconds (integer) -- The time window (in seconds) contained in each manifest.
SegmentDurationSeconds (integer) -- The duration (in seconds) of each segment.
StreamSelection (dict) -- A StreamSelection configuration.
MaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.
MinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.
StreamOrder (string) -- A directive that determines the order of streams in the output.




Origination (string) -- Control whether origination of video is allowed for this OriginEndpoint. If set to ALLOW, the OriginEndpoint may by requested, pursuant to any other form of access control. If set to DENY, the OriginEndpoint may not be requested. This can be helpful for Live to VOD harvesting, or for temporarily disabling origination
StartoverWindowSeconds (integer) -- Maximum duration (seconds) of content to retain for startover playback. If not specified, startover playback will be disabled for the OriginEndpoint.
Tags (dict) -- A collection of tags associated with a resource
(string) --
(string) --




TimeDelaySeconds (integer) -- Amount of delay (seconds) to enforce on the playback of live content. If not specified, there will be no time delay in effect for the OriginEndpoint.
Url (string) -- The URL of the packaged OriginEndpoint for consumption.
Whitelist (list) -- A list of source IP CIDR blocks that will be allowed to access the OriginEndpoint.
(string) --







Exceptions

MediaPackage.Client.exceptions.UnprocessableEntityException
MediaPackage.Client.exceptions.InternalServerErrorException
MediaPackage.Client.exceptions.ForbiddenException
MediaPackage.Client.exceptions.NotFoundException
MediaPackage.Client.exceptions.ServiceUnavailableException
MediaPackage.Client.exceptions.TooManyRequestsException


    :return: {
        'Arn': 'string',
        'Authorization': {
            'CdnIdentifierSecret': 'string',
            'SecretsRoleArn': 'string'
        },
        'ChannelId': 'string',
        'CmafPackage': {
            'Encryption': {
                'KeyRotationIntervalSeconds': 123,
                'SpekeKeyProvider': {
                    'CertificateArn': 'string',
                    'ResourceId': 'string',
                    'RoleArn': 'string',
                    'SystemIds': [
                        'string',
                    ],
                    'Url': 'string'
                }
            },
            'HlsManifests': [
                {
                    'AdMarkers': 'NONE'|'SCTE35_ENHANCED'|'PASSTHROUGH',
                    'Id': 'string',
                    'IncludeIframeOnlyStream': True|False,
                    'ManifestName': 'string',
                    'PlaylistType': 'NONE'|'EVENT'|'VOD',
                    'PlaylistWindowSeconds': 123,
                    'ProgramDateTimeIntervalSeconds': 123,
                    'Url': 'string'
                },
            ],
            'SegmentDurationSeconds': 123,
            'SegmentPrefix': 'string',
            'StreamSelection': {
                'MaxVideoBitsPerSecond': 123,
                'MinVideoBitsPerSecond': 123,
                'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
            }
        },
        'DashPackage': {
            'AdTriggers': [
                'SPLICE_INSERT'|'BREAK'|'PROVIDER_ADVERTISEMENT'|'DISTRIBUTOR_ADVERTISEMENT'|'PROVIDER_PLACEMENT_OPPORTUNITY'|'DISTRIBUTOR_PLACEMENT_OPPORTUNITY'|'PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY'|'DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY',
            ],
            'AdsOnDeliveryRestrictions': 'NONE'|'RESTRICTED'|'UNRESTRICTED'|'BOTH',
            'Encryption': {
                'KeyRotationIntervalSeconds': 123,
                'SpekeKeyProvider': {
                    'CertificateArn': 'string',
                    'ResourceId': 'string',
                    'RoleArn': 'string',
                    'SystemIds': [
                        'string',
                    ],
                    'Url': 'string'
                }
            },
            'ManifestLayout': 'FULL'|'COMPACT',
            'ManifestWindowSeconds': 123,
            'MinBufferTimeSeconds': 123,
            'MinUpdatePeriodSeconds': 123,
            'PeriodTriggers': [
                'ADS',
            ],
            'Profile': 'NONE'|'HBBTV_1_5',
            'SegmentDurationSeconds': 123,
            'SegmentTemplateFormat': 'NUMBER_WITH_TIMELINE'|'TIME_WITH_TIMELINE'|'NUMBER_WITH_DURATION',
            'StreamSelection': {
                'MaxVideoBitsPerSecond': 123,
                'MinVideoBitsPerSecond': 123,
                'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
            },
            'SuggestedPresentationDelaySeconds': 123
        },
        'Description': 'string',
        'HlsPackage': {
            'AdMarkers': 'NONE'|'SCTE35_ENHANCED'|'PASSTHROUGH',
            'AdTriggers': [
                'SPLICE_INSERT'|'BREAK'|'PROVIDER_ADVERTISEMENT'|'DISTRIBUTOR_ADVERTISEMENT'|'PROVIDER_PLACEMENT_OPPORTUNITY'|'DISTRIBUTOR_PLACEMENT_OPPORTUNITY'|'PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY'|'DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY',
            ],
            'AdsOnDeliveryRestrictions': 'NONE'|'RESTRICTED'|'UNRESTRICTED'|'BOTH',
            'Encryption': {
                'ConstantInitializationVector': 'string',
                'EncryptionMethod': 'AES_128'|'SAMPLE_AES',
                'KeyRotationIntervalSeconds': 123,
                'RepeatExtXKey': True|False,
                'SpekeKeyProvider': {
                    'CertificateArn': 'string',
                    'ResourceId': 'string',
                    'RoleArn': 'string',
                    'SystemIds': [
                        'string',
                    ],
                    'Url': 'string'
                }
            },
            'IncludeIframeOnlyStream': True|False,
            'PlaylistType': 'NONE'|'EVENT'|'VOD',
            'PlaylistWindowSeconds': 123,
            'ProgramDateTimeIntervalSeconds': 123,
            'SegmentDurationSeconds': 123,
            'StreamSelection': {
                'MaxVideoBitsPerSecond': 123,
                'MinVideoBitsPerSecond': 123,
                'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
            },
            'UseAudioRenditionGroup': True|False
        },
        'Id': 'string',
        'ManifestName': 'string',
        'MssPackage': {
            'Encryption': {
                'SpekeKeyProvider': {
                    'CertificateArn': 'string',
                    'ResourceId': 'string',
                    'RoleArn': 'string',
                    'SystemIds': [
                        'string',
                    ],
                    'Url': 'string'
                }
            },
            'ManifestWindowSeconds': 123,
            'SegmentDurationSeconds': 123,
            'StreamSelection': {
                'MaxVideoBitsPerSecond': 123,
                'MinVideoBitsPerSecond': 123,
                'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
            }
        },
        'Origination': 'ALLOW'|'DENY',
        'StartoverWindowSeconds': 123,
        'Tags': {
            'string': 'string'
        },
        'TimeDelaySeconds': 123,
        'Url': 'string',
        'Whitelist': [
            'string',
        ]
    }
    
    
    :returns: 
    MediaPackage.Client.exceptions.UnprocessableEntityException
    MediaPackage.Client.exceptions.InternalServerErrorException
    MediaPackage.Client.exceptions.ForbiddenException
    MediaPackage.Client.exceptions.NotFoundException
    MediaPackage.Client.exceptions.ServiceUnavailableException
    MediaPackage.Client.exceptions.TooManyRequestsException
    
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

def list_channels(MaxResults=None, NextToken=None):
    """
    Returns a collection of Channels.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_channels(
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: Upper bound on number of records to return.

    :type NextToken: string
    :param NextToken: A token used to resume pagination from the end of a previous request.

    :rtype: dict

ReturnsResponse Syntax
{
    'Channels': [
        {
            'Arn': 'string',
            'Description': 'string',
            'HlsIngest': {
                'IngestEndpoints': [
                    {
                        'Id': 'string',
                        'Password': 'string',
                        'Url': 'string',
                        'Username': 'string'
                    },
                ]
            },
            'Id': 'string',
            'Tags': {
                'string': 'string'
            }
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) -- A collection of Channel records.
Channels (list) -- A list of Channel records.
(dict) -- A Channel resource configuration.
Arn (string) -- The Amazon Resource Name (ARN) assigned to the Channel.
Description (string) -- A short text description of the Channel.
HlsIngest (dict) -- An HTTP Live Streaming (HLS) ingest resource configuration.
IngestEndpoints (list) -- A list of endpoints to which the source stream should be sent.
(dict) -- An endpoint for ingesting source content for a Channel.
Id (string) -- The system generated unique identifier for the IngestEndpoint
Password (string) -- The system generated password for ingest authentication.
Url (string) -- The ingest URL to which the source stream should be sent.
Username (string) -- The system generated username for ingest authentication.






Id (string) -- The ID of the Channel.
Tags (dict) -- A collection of tags associated with a resource
(string) --
(string) --








NextToken (string) -- A token that can be used to resume pagination from the end of the collection.






Exceptions

MediaPackage.Client.exceptions.UnprocessableEntityException
MediaPackage.Client.exceptions.InternalServerErrorException
MediaPackage.Client.exceptions.ForbiddenException
MediaPackage.Client.exceptions.NotFoundException
MediaPackage.Client.exceptions.ServiceUnavailableException
MediaPackage.Client.exceptions.TooManyRequestsException


    :return: {
        'Channels': [
            {
                'Arn': 'string',
                'Description': 'string',
                'HlsIngest': {
                    'IngestEndpoints': [
                        {
                            'Id': 'string',
                            'Password': 'string',
                            'Url': 'string',
                            'Username': 'string'
                        },
                    ]
                },
                'Id': 'string',
                'Tags': {
                    'string': 'string'
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (dict) -- A collection of Channel records.
    Channels (list) -- A list of Channel records.
    (dict) -- A Channel resource configuration.
    Arn (string) -- The Amazon Resource Name (ARN) assigned to the Channel.
    Description (string) -- A short text description of the Channel.
    HlsIngest (dict) -- An HTTP Live Streaming (HLS) ingest resource configuration.
    IngestEndpoints (list) -- A list of endpoints to which the source stream should be sent.
    (dict) -- An endpoint for ingesting source content for a Channel.
    Id (string) -- The system generated unique identifier for the IngestEndpoint
    Password (string) -- The system generated password for ingest authentication.
    Url (string) -- The ingest URL to which the source stream should be sent.
    Username (string) -- The system generated username for ingest authentication.
    
    
    
    
    
    
    Id (string) -- The ID of the Channel.
    Tags (dict) -- A collection of tags associated with a resource
    (string) --
    (string) --
    
    
    
    
    
    
    
    
    NextToken (string) -- A token that can be used to resume pagination from the end of the collection.
    
    
    
    """
    pass

def list_harvest_jobs(IncludeChannelId=None, IncludeStatus=None, MaxResults=None, NextToken=None):
    """
    Returns a collection of HarvestJob records.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_harvest_jobs(
        IncludeChannelId='string',
        IncludeStatus='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type IncludeChannelId: string
    :param IncludeChannelId: When specified, the request will return only HarvestJobs associated with the given Channel ID.

    :type IncludeStatus: string
    :param IncludeStatus: When specified, the request will return only HarvestJobs in the given status.

    :type MaxResults: integer
    :param MaxResults: The upper bound on the number of records to return.

    :type NextToken: string
    :param NextToken: A token used to resume pagination from the end of a previous request.

    :rtype: dict

ReturnsResponse Syntax
{
    'HarvestJobs': [
        {
            'Arn': 'string',
            'ChannelId': 'string',
            'CreatedAt': 'string',
            'EndTime': 'string',
            'Id': 'string',
            'OriginEndpointId': 'string',
            'S3Destination': {
                'BucketName': 'string',
                'ManifestKey': 'string',
                'RoleArn': 'string'
            },
            'StartTime': 'string',
            'Status': 'IN_PROGRESS'|'SUCCEEDED'|'FAILED'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) -- A collection of HarvestJob records.
HarvestJobs (list) -- A list of HarvestJob records.
(dict) -- A HarvestJob resource configuration
Arn (string) -- The Amazon Resource Name (ARN) assigned to the HarvestJob.
ChannelId (string) -- The ID of the Channel that the HarvestJob will harvest from.
CreatedAt (string) -- The time the HarvestJob was submitted
EndTime (string) -- The end of the time-window which will be harvested.
Id (string) -- The ID of the HarvestJob. The ID must be unique within the region and it cannot be changed after the HarvestJob is submitted.
OriginEndpointId (string) -- The ID of the OriginEndpoint that the HarvestJob will harvest from. This cannot be changed after the HarvestJob is submitted.
S3Destination (dict) -- Configuration parameters for where in an S3 bucket to place the harvested content
BucketName (string) -- The name of an S3 bucket within which harvested content will be exported
ManifestKey (string) -- The key in the specified S3 bucket where the harvested top-level manifest will be placed.
RoleArn (string) -- The IAM role used to write to the specified S3 bucket


StartTime (string) -- The start of the time-window which will be harvested.
Status (string) -- The current status of the HarvestJob. Consider setting up a CloudWatch Event to listen for HarvestJobs as they succeed or fail. In the event of failure, the CloudWatch Event will include an explanation of why the HarvestJob failed.




NextToken (string) -- A token that can be used to resume pagination from the end of the collection.






Exceptions

MediaPackage.Client.exceptions.UnprocessableEntityException
MediaPackage.Client.exceptions.InternalServerErrorException
MediaPackage.Client.exceptions.ForbiddenException
MediaPackage.Client.exceptions.NotFoundException
MediaPackage.Client.exceptions.ServiceUnavailableException
MediaPackage.Client.exceptions.TooManyRequestsException


    :return: {
        'HarvestJobs': [
            {
                'Arn': 'string',
                'ChannelId': 'string',
                'CreatedAt': 'string',
                'EndTime': 'string',
                'Id': 'string',
                'OriginEndpointId': 'string',
                'S3Destination': {
                    'BucketName': 'string',
                    'ManifestKey': 'string',
                    'RoleArn': 'string'
                },
                'StartTime': 'string',
                'Status': 'IN_PROGRESS'|'SUCCEEDED'|'FAILED'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (dict) -- A collection of HarvestJob records.
    HarvestJobs (list) -- A list of HarvestJob records.
    (dict) -- A HarvestJob resource configuration
    Arn (string) -- The Amazon Resource Name (ARN) assigned to the HarvestJob.
    ChannelId (string) -- The ID of the Channel that the HarvestJob will harvest from.
    CreatedAt (string) -- The time the HarvestJob was submitted
    EndTime (string) -- The end of the time-window which will be harvested.
    Id (string) -- The ID of the HarvestJob. The ID must be unique within the region and it cannot be changed after the HarvestJob is submitted.
    OriginEndpointId (string) -- The ID of the OriginEndpoint that the HarvestJob will harvest from. This cannot be changed after the HarvestJob is submitted.
    S3Destination (dict) -- Configuration parameters for where in an S3 bucket to place the harvested content
    BucketName (string) -- The name of an S3 bucket within which harvested content will be exported
    ManifestKey (string) -- The key in the specified S3 bucket where the harvested top-level manifest will be placed.
    RoleArn (string) -- The IAM role used to write to the specified S3 bucket
    
    
    StartTime (string) -- The start of the time-window which will be harvested.
    Status (string) -- The current status of the HarvestJob. Consider setting up a CloudWatch Event to listen for HarvestJobs as they succeed or fail. In the event of failure, the CloudWatch Event will include an explanation of why the HarvestJob failed.
    
    
    
    
    NextToken (string) -- A token that can be used to resume pagination from the end of the collection.
    
    
    
    """
    pass

def list_origin_endpoints(ChannelId=None, MaxResults=None, NextToken=None):
    """
    Returns a collection of OriginEndpoint records.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_origin_endpoints(
        ChannelId='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type ChannelId: string
    :param ChannelId: When specified, the request will return only OriginEndpoints associated with the given Channel ID.

    :type MaxResults: integer
    :param MaxResults: The upper bound on the number of records to return.

    :type NextToken: string
    :param NextToken: A token used to resume pagination from the end of a previous request.

    :rtype: dict

ReturnsResponse Syntax
{
    'NextToken': 'string',
    'OriginEndpoints': [
        {
            'Arn': 'string',
            'Authorization': {
                'CdnIdentifierSecret': 'string',
                'SecretsRoleArn': 'string'
            },
            'ChannelId': 'string',
            'CmafPackage': {
                'Encryption': {
                    'KeyRotationIntervalSeconds': 123,
                    'SpekeKeyProvider': {
                        'CertificateArn': 'string',
                        'ResourceId': 'string',
                        'RoleArn': 'string',
                        'SystemIds': [
                            'string',
                        ],
                        'Url': 'string'
                    }
                },
                'HlsManifests': [
                    {
                        'AdMarkers': 'NONE'|'SCTE35_ENHANCED'|'PASSTHROUGH',
                        'Id': 'string',
                        'IncludeIframeOnlyStream': True|False,
                        'ManifestName': 'string',
                        'PlaylistType': 'NONE'|'EVENT'|'VOD',
                        'PlaylistWindowSeconds': 123,
                        'ProgramDateTimeIntervalSeconds': 123,
                        'Url': 'string'
                    },
                ],
                'SegmentDurationSeconds': 123,
                'SegmentPrefix': 'string',
                'StreamSelection': {
                    'MaxVideoBitsPerSecond': 123,
                    'MinVideoBitsPerSecond': 123,
                    'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
                }
            },
            'DashPackage': {
                'AdTriggers': [
                    'SPLICE_INSERT'|'BREAK'|'PROVIDER_ADVERTISEMENT'|'DISTRIBUTOR_ADVERTISEMENT'|'PROVIDER_PLACEMENT_OPPORTUNITY'|'DISTRIBUTOR_PLACEMENT_OPPORTUNITY'|'PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY'|'DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY',
                ],
                'AdsOnDeliveryRestrictions': 'NONE'|'RESTRICTED'|'UNRESTRICTED'|'BOTH',
                'Encryption': {
                    'KeyRotationIntervalSeconds': 123,
                    'SpekeKeyProvider': {
                        'CertificateArn': 'string',
                        'ResourceId': 'string',
                        'RoleArn': 'string',
                        'SystemIds': [
                            'string',
                        ],
                        'Url': 'string'
                    }
                },
                'ManifestLayout': 'FULL'|'COMPACT',
                'ManifestWindowSeconds': 123,
                'MinBufferTimeSeconds': 123,
                'MinUpdatePeriodSeconds': 123,
                'PeriodTriggers': [
                    'ADS',
                ],
                'Profile': 'NONE'|'HBBTV_1_5',
                'SegmentDurationSeconds': 123,
                'SegmentTemplateFormat': 'NUMBER_WITH_TIMELINE'|'TIME_WITH_TIMELINE'|'NUMBER_WITH_DURATION',
                'StreamSelection': {
                    'MaxVideoBitsPerSecond': 123,
                    'MinVideoBitsPerSecond': 123,
                    'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
                },
                'SuggestedPresentationDelaySeconds': 123
            },
            'Description': 'string',
            'HlsPackage': {
                'AdMarkers': 'NONE'|'SCTE35_ENHANCED'|'PASSTHROUGH',
                'AdTriggers': [
                    'SPLICE_INSERT'|'BREAK'|'PROVIDER_ADVERTISEMENT'|'DISTRIBUTOR_ADVERTISEMENT'|'PROVIDER_PLACEMENT_OPPORTUNITY'|'DISTRIBUTOR_PLACEMENT_OPPORTUNITY'|'PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY'|'DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY',
                ],
                'AdsOnDeliveryRestrictions': 'NONE'|'RESTRICTED'|'UNRESTRICTED'|'BOTH',
                'Encryption': {
                    'ConstantInitializationVector': 'string',
                    'EncryptionMethod': 'AES_128'|'SAMPLE_AES',
                    'KeyRotationIntervalSeconds': 123,
                    'RepeatExtXKey': True|False,
                    'SpekeKeyProvider': {
                        'CertificateArn': 'string',
                        'ResourceId': 'string',
                        'RoleArn': 'string',
                        'SystemIds': [
                            'string',
                        ],
                        'Url': 'string'
                    }
                },
                'IncludeIframeOnlyStream': True|False,
                'PlaylistType': 'NONE'|'EVENT'|'VOD',
                'PlaylistWindowSeconds': 123,
                'ProgramDateTimeIntervalSeconds': 123,
                'SegmentDurationSeconds': 123,
                'StreamSelection': {
                    'MaxVideoBitsPerSecond': 123,
                    'MinVideoBitsPerSecond': 123,
                    'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
                },
                'UseAudioRenditionGroup': True|False
            },
            'Id': 'string',
            'ManifestName': 'string',
            'MssPackage': {
                'Encryption': {
                    'SpekeKeyProvider': {
                        'CertificateArn': 'string',
                        'ResourceId': 'string',
                        'RoleArn': 'string',
                        'SystemIds': [
                            'string',
                        ],
                        'Url': 'string'
                    }
                },
                'ManifestWindowSeconds': 123,
                'SegmentDurationSeconds': 123,
                'StreamSelection': {
                    'MaxVideoBitsPerSecond': 123,
                    'MinVideoBitsPerSecond': 123,
                    'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
                }
            },
            'Origination': 'ALLOW'|'DENY',
            'StartoverWindowSeconds': 123,
            'Tags': {
                'string': 'string'
            },
            'TimeDelaySeconds': 123,
            'Url': 'string',
            'Whitelist': [
                'string',
            ]
        },
    ]
}


Response Structure

(dict) -- A collection of OriginEndpoint records.
NextToken (string) -- A token that can be used to resume pagination from the end of the collection.
OriginEndpoints (list) -- A list of OriginEndpoint records.
(dict) -- An OriginEndpoint resource configuration.
Arn (string) -- The Amazon Resource Name (ARN) assigned to the OriginEndpoint.
Authorization (dict) -- CDN Authorization credentials
CdnIdentifierSecret (string) -- The Amazon Resource Name (ARN) for the secret in Secrets Manager that your Content Distribution Network (CDN) uses for authorization to access your endpoint.
SecretsRoleArn (string) -- The Amazon Resource Name (ARN) for the IAM role that allows MediaPackage to communicate with AWS Secrets Manager.


ChannelId (string) -- The ID of the Channel the OriginEndpoint is associated with.
CmafPackage (dict) -- A Common Media Application Format (CMAF) packaging configuration.
Encryption (dict) -- A Common Media Application Format (CMAF) encryption configuration.
KeyRotationIntervalSeconds (integer) -- Time (in seconds) between each encryption key rotation.
SpekeKeyProvider (dict) -- A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
CertificateArn (string) -- An Amazon Resource Name (ARN) of a Certificate Manager certificate that MediaPackage will use for enforcing secure end-to-end data transfer with the key provider service.
ResourceId (string) -- The resource ID to include in key requests.
RoleArn (string) -- An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.
SystemIds (list) -- The system IDs to include in key requests.
(string) --


Url (string) -- The URL of the external key provider service.




HlsManifests (list) -- A list of HLS manifest configurations
(dict) -- A HTTP Live Streaming (HLS) manifest configuration.
AdMarkers (string) -- This setting controls how ad markers are included in the packaged OriginEndpoint. "NONE" will omit all SCTE-35 ad markers from the output. "PASSTHROUGH" causes the manifest to contain a copy of the SCTE-35 ad markers (comments) taken directly from the input HTTP Live Streaming (HLS) manifest. "SCTE35_ENHANCED" generates ad markers and blackout tags based on SCTE-35 messages in the input source.
Id (string) -- The ID of the manifest. The ID must be unique within the OriginEndpoint and it cannot be changed after it is created.
IncludeIframeOnlyStream (boolean) -- When enabled, an I-Frame only stream will be included in the output.
ManifestName (string) -- An optional short string appended to the end of the OriginEndpoint URL. If not specified, defaults to the manifestName for the OriginEndpoint.
PlaylistType (string) -- The HTTP Live Streaming (HLS) playlist type. When either "EVENT" or "VOD" is specified, a corresponding EXT-X-PLAYLIST-TYPE entry will be included in the media playlist.
PlaylistWindowSeconds (integer) -- Time window (in seconds) contained in each parent manifest.
ProgramDateTimeIntervalSeconds (integer) -- The interval (in seconds) between each EXT-X-PROGRAM-DATE-TIME tag inserted into manifests. Additionally, when an interval is specified ID3Timed Metadata messages will be generated every 5 seconds using the ingest time of the content. If the interval is not specified, or set to 0, then no EXT-X-PROGRAM-DATE-TIME tags will be inserted into manifests and no ID3Timed Metadata messages will be generated. Note that irrespective of this parameter, if any ID3 Timed Metadata is found in HTTP Live Streaming (HLS) input, it will be passed through to HLS output.
Url (string) -- The URL of the packaged OriginEndpoint for consumption.




SegmentDurationSeconds (integer) -- Duration (in seconds) of each segment. Actual segments will be rounded to the nearest multiple of the source segment duration.
SegmentPrefix (string) -- An optional custom string that is prepended to the name of each segment. If not specified, it defaults to the ChannelId.
StreamSelection (dict) -- A StreamSelection configuration.
MaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.
MinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.
StreamOrder (string) -- A directive that determines the order of streams in the output.




DashPackage (dict) -- A Dynamic Adaptive Streaming over HTTP (DASH) packaging configuration.
AdTriggers (list) -- A list of SCTE-35 message types that are treated as ad markers in the output. If empty, no ad markers are output. Specify multiple items to create ad markers for all of the included message types.
(string) --


AdsOnDeliveryRestrictions (string) -- This setting allows the delivery restriction flags on SCTE-35 segmentation descriptors to determine whether a message signals an ad. Choosing "NONE" means no SCTE-35 messages become ads. Choosing "RESTRICTED" means SCTE-35 messages of the types specified in AdTriggers that contain delivery restrictions will be treated as ads. Choosing "UNRESTRICTED" means SCTE-35 messages of the types specified in AdTriggers that do not contain delivery restrictions will be treated as ads. Choosing "BOTH" means all SCTE-35 messages of the types specified in AdTriggers will be treated as ads. Note that Splice Insert messages do not have these flags and are always treated as ads if specified in AdTriggers.
Encryption (dict) -- A Dynamic Adaptive Streaming over HTTP (DASH) encryption configuration.
KeyRotationIntervalSeconds (integer) -- Time (in seconds) between each encryption key rotation.
SpekeKeyProvider (dict) -- A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
CertificateArn (string) -- An Amazon Resource Name (ARN) of a Certificate Manager certificate that MediaPackage will use for enforcing secure end-to-end data transfer with the key provider service.
ResourceId (string) -- The resource ID to include in key requests.
RoleArn (string) -- An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.
SystemIds (list) -- The system IDs to include in key requests.
(string) --


Url (string) -- The URL of the external key provider service.




ManifestLayout (string) -- Determines the position of some tags in the Media Presentation Description (MPD). When set to FULL, elements like SegmentTemplate and ContentProtection are included in each Representation. When set to COMPACT, duplicate elements are combined and presented at the AdaptationSet level.
ManifestWindowSeconds (integer) -- Time window (in seconds) contained in each manifest.
MinBufferTimeSeconds (integer) -- Minimum duration (in seconds) that a player will buffer media before starting the presentation.
MinUpdatePeriodSeconds (integer) -- Minimum duration (in seconds) between potential changes to the Dynamic Adaptive Streaming over HTTP (DASH) Media Presentation Description (MPD).
PeriodTriggers (list) -- A list of triggers that controls when the outgoing Dynamic Adaptive Streaming over HTTP (DASH) Media Presentation Description (MPD) will be partitioned into multiple periods. If empty, the content will not be partitioned into more than one period. If the list contains "ADS", new periods will be created where the Channel source contains SCTE-35 ad markers.
(string) --


Profile (string) -- The Dynamic Adaptive Streaming over HTTP (DASH) profile type. When set to "HBBTV_1_5", HbbTV 1.5 compliant output is enabled.
SegmentDurationSeconds (integer) -- Duration (in seconds) of each segment. Actual segments will be rounded to the nearest multiple of the source segment duration.
SegmentTemplateFormat (string) -- Determines the type of SegmentTemplate included in the Media Presentation Description (MPD). When set to NUMBER_WITH_TIMELINE, a full timeline is presented in each SegmentTemplate, with $Number$ media URLs. When set to TIME_WITH_TIMELINE, a full timeline is presented in each SegmentTemplate, with $Time$ media URLs. When set to NUMBER_WITH_DURATION, only a duration is included in each SegmentTemplate, with $Number$ media URLs.
StreamSelection (dict) -- A StreamSelection configuration.
MaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.
MinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.
StreamOrder (string) -- A directive that determines the order of streams in the output.


SuggestedPresentationDelaySeconds (integer) -- Duration (in seconds) to delay live content before presentation.


Description (string) -- A short text description of the OriginEndpoint.
HlsPackage (dict) -- An HTTP Live Streaming (HLS) packaging configuration.
AdMarkers (string) -- This setting controls how ad markers are included in the packaged OriginEndpoint. "NONE" will omit all SCTE-35 ad markers from the output. "PASSTHROUGH" causes the manifest to contain a copy of the SCTE-35 ad markers (comments) taken directly from the input HTTP Live Streaming (HLS) manifest. "SCTE35_ENHANCED" generates ad markers and blackout tags based on SCTE-35 messages in the input source.
AdTriggers (list) -- A list of SCTE-35 message types that are treated as ad markers in the output. If empty, no ad markers are output. Specify multiple items to create ad markers for all of the included message types.
(string) --


AdsOnDeliveryRestrictions (string) -- This setting allows the delivery restriction flags on SCTE-35 segmentation descriptors to determine whether a message signals an ad. Choosing "NONE" means no SCTE-35 messages become ads. Choosing "RESTRICTED" means SCTE-35 messages of the types specified in AdTriggers that contain delivery restrictions will be treated as ads. Choosing "UNRESTRICTED" means SCTE-35 messages of the types specified in AdTriggers that do not contain delivery restrictions will be treated as ads. Choosing "BOTH" means all SCTE-35 messages of the types specified in AdTriggers will be treated as ads. Note that Splice Insert messages do not have these flags and are always treated as ads if specified in AdTriggers.
Encryption (dict) -- An HTTP Live Streaming (HLS) encryption configuration.
ConstantInitializationVector (string) -- A constant initialization vector for encryption (optional). When not specified the initialization vector will be periodically rotated.
EncryptionMethod (string) -- The encryption method to use.
KeyRotationIntervalSeconds (integer) -- Interval (in seconds) between each encryption key rotation.
RepeatExtXKey (boolean) -- When enabled, the EXT-X-KEY tag will be repeated in output manifests.
SpekeKeyProvider (dict) -- A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
CertificateArn (string) -- An Amazon Resource Name (ARN) of a Certificate Manager certificate that MediaPackage will use for enforcing secure end-to-end data transfer with the key provider service.
ResourceId (string) -- The resource ID to include in key requests.
RoleArn (string) -- An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.
SystemIds (list) -- The system IDs to include in key requests.
(string) --


Url (string) -- The URL of the external key provider service.




IncludeIframeOnlyStream (boolean) -- When enabled, an I-Frame only stream will be included in the output.
PlaylistType (string) -- The HTTP Live Streaming (HLS) playlist type. When either "EVENT" or "VOD" is specified, a corresponding EXT-X-PLAYLIST-TYPE entry will be included in the media playlist.
PlaylistWindowSeconds (integer) -- Time window (in seconds) contained in each parent manifest.
ProgramDateTimeIntervalSeconds (integer) -- The interval (in seconds) between each EXT-X-PROGRAM-DATE-TIME tag inserted into manifests. Additionally, when an interval is specified ID3Timed Metadata messages will be generated every 5 seconds using the ingest time of the content. If the interval is not specified, or set to 0, then no EXT-X-PROGRAM-DATE-TIME tags will be inserted into manifests and no ID3Timed Metadata messages will be generated. Note that irrespective of this parameter, if any ID3 Timed Metadata is found in HTTP Live Streaming (HLS) input, it will be passed through to HLS output.
SegmentDurationSeconds (integer) -- Duration (in seconds) of each fragment. Actual fragments will be rounded to the nearest multiple of the source fragment duration.
StreamSelection (dict) -- A StreamSelection configuration.
MaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.
MinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.
StreamOrder (string) -- A directive that determines the order of streams in the output.


UseAudioRenditionGroup (boolean) -- When enabled, audio streams will be placed in rendition groups in the output.


Id (string) -- The ID of the OriginEndpoint.
ManifestName (string) -- A short string appended to the end of the OriginEndpoint URL.
MssPackage (dict) -- A Microsoft Smooth Streaming (MSS) packaging configuration.
Encryption (dict) -- A Microsoft Smooth Streaming (MSS) encryption configuration.
SpekeKeyProvider (dict) -- A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
CertificateArn (string) -- An Amazon Resource Name (ARN) of a Certificate Manager certificate that MediaPackage will use for enforcing secure end-to-end data transfer with the key provider service.
ResourceId (string) -- The resource ID to include in key requests.
RoleArn (string) -- An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.
SystemIds (list) -- The system IDs to include in key requests.
(string) --


Url (string) -- The URL of the external key provider service.




ManifestWindowSeconds (integer) -- The time window (in seconds) contained in each manifest.
SegmentDurationSeconds (integer) -- The duration (in seconds) of each segment.
StreamSelection (dict) -- A StreamSelection configuration.
MaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.
MinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.
StreamOrder (string) -- A directive that determines the order of streams in the output.




Origination (string) -- Control whether origination of video is allowed for this OriginEndpoint. If set to ALLOW, the OriginEndpoint may by requested, pursuant to any other form of access control. If set to DENY, the OriginEndpoint may not be requested. This can be helpful for Live to VOD harvesting, or for temporarily disabling origination
StartoverWindowSeconds (integer) -- Maximum duration (seconds) of content to retain for startover playback. If not specified, startover playback will be disabled for the OriginEndpoint.
Tags (dict) -- A collection of tags associated with a resource
(string) --
(string) --




TimeDelaySeconds (integer) -- Amount of delay (seconds) to enforce on the playback of live content. If not specified, there will be no time delay in effect for the OriginEndpoint.
Url (string) -- The URL of the packaged OriginEndpoint for consumption.
Whitelist (list) -- A list of source IP CIDR blocks that will be allowed to access the OriginEndpoint.
(string) --












Exceptions

MediaPackage.Client.exceptions.UnprocessableEntityException
MediaPackage.Client.exceptions.InternalServerErrorException
MediaPackage.Client.exceptions.ForbiddenException
MediaPackage.Client.exceptions.NotFoundException
MediaPackage.Client.exceptions.ServiceUnavailableException
MediaPackage.Client.exceptions.TooManyRequestsException


    :return: {
        'NextToken': 'string',
        'OriginEndpoints': [
            {
                'Arn': 'string',
                'Authorization': {
                    'CdnIdentifierSecret': 'string',
                    'SecretsRoleArn': 'string'
                },
                'ChannelId': 'string',
                'CmafPackage': {
                    'Encryption': {
                        'KeyRotationIntervalSeconds': 123,
                        'SpekeKeyProvider': {
                            'CertificateArn': 'string',
                            'ResourceId': 'string',
                            'RoleArn': 'string',
                            'SystemIds': [
                                'string',
                            ],
                            'Url': 'string'
                        }
                    },
                    'HlsManifests': [
                        {
                            'AdMarkers': 'NONE'|'SCTE35_ENHANCED'|'PASSTHROUGH',
                            'Id': 'string',
                            'IncludeIframeOnlyStream': True|False,
                            'ManifestName': 'string',
                            'PlaylistType': 'NONE'|'EVENT'|'VOD',
                            'PlaylistWindowSeconds': 123,
                            'ProgramDateTimeIntervalSeconds': 123,
                            'Url': 'string'
                        },
                    ],
                    'SegmentDurationSeconds': 123,
                    'SegmentPrefix': 'string',
                    'StreamSelection': {
                        'MaxVideoBitsPerSecond': 123,
                        'MinVideoBitsPerSecond': 123,
                        'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
                    }
                },
                'DashPackage': {
                    'AdTriggers': [
                        'SPLICE_INSERT'|'BREAK'|'PROVIDER_ADVERTISEMENT'|'DISTRIBUTOR_ADVERTISEMENT'|'PROVIDER_PLACEMENT_OPPORTUNITY'|'DISTRIBUTOR_PLACEMENT_OPPORTUNITY'|'PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY'|'DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY',
                    ],
                    'AdsOnDeliveryRestrictions': 'NONE'|'RESTRICTED'|'UNRESTRICTED'|'BOTH',
                    'Encryption': {
                        'KeyRotationIntervalSeconds': 123,
                        'SpekeKeyProvider': {
                            'CertificateArn': 'string',
                            'ResourceId': 'string',
                            'RoleArn': 'string',
                            'SystemIds': [
                                'string',
                            ],
                            'Url': 'string'
                        }
                    },
                    'ManifestLayout': 'FULL'|'COMPACT',
                    'ManifestWindowSeconds': 123,
                    'MinBufferTimeSeconds': 123,
                    'MinUpdatePeriodSeconds': 123,
                    'PeriodTriggers': [
                        'ADS',
                    ],
                    'Profile': 'NONE'|'HBBTV_1_5',
                    'SegmentDurationSeconds': 123,
                    'SegmentTemplateFormat': 'NUMBER_WITH_TIMELINE'|'TIME_WITH_TIMELINE'|'NUMBER_WITH_DURATION',
                    'StreamSelection': {
                        'MaxVideoBitsPerSecond': 123,
                        'MinVideoBitsPerSecond': 123,
                        'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
                    },
                    'SuggestedPresentationDelaySeconds': 123
                },
                'Description': 'string',
                'HlsPackage': {
                    'AdMarkers': 'NONE'|'SCTE35_ENHANCED'|'PASSTHROUGH',
                    'AdTriggers': [
                        'SPLICE_INSERT'|'BREAK'|'PROVIDER_ADVERTISEMENT'|'DISTRIBUTOR_ADVERTISEMENT'|'PROVIDER_PLACEMENT_OPPORTUNITY'|'DISTRIBUTOR_PLACEMENT_OPPORTUNITY'|'PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY'|'DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY',
                    ],
                    'AdsOnDeliveryRestrictions': 'NONE'|'RESTRICTED'|'UNRESTRICTED'|'BOTH',
                    'Encryption': {
                        'ConstantInitializationVector': 'string',
                        'EncryptionMethod': 'AES_128'|'SAMPLE_AES',
                        'KeyRotationIntervalSeconds': 123,
                        'RepeatExtXKey': True|False,
                        'SpekeKeyProvider': {
                            'CertificateArn': 'string',
                            'ResourceId': 'string',
                            'RoleArn': 'string',
                            'SystemIds': [
                                'string',
                            ],
                            'Url': 'string'
                        }
                    },
                    'IncludeIframeOnlyStream': True|False,
                    'PlaylistType': 'NONE'|'EVENT'|'VOD',
                    'PlaylistWindowSeconds': 123,
                    'ProgramDateTimeIntervalSeconds': 123,
                    'SegmentDurationSeconds': 123,
                    'StreamSelection': {
                        'MaxVideoBitsPerSecond': 123,
                        'MinVideoBitsPerSecond': 123,
                        'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
                    },
                    'UseAudioRenditionGroup': True|False
                },
                'Id': 'string',
                'ManifestName': 'string',
                'MssPackage': {
                    'Encryption': {
                        'SpekeKeyProvider': {
                            'CertificateArn': 'string',
                            'ResourceId': 'string',
                            'RoleArn': 'string',
                            'SystemIds': [
                                'string',
                            ],
                            'Url': 'string'
                        }
                    },
                    'ManifestWindowSeconds': 123,
                    'SegmentDurationSeconds': 123,
                    'StreamSelection': {
                        'MaxVideoBitsPerSecond': 123,
                        'MinVideoBitsPerSecond': 123,
                        'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
                    }
                },
                'Origination': 'ALLOW'|'DENY',
                'StartoverWindowSeconds': 123,
                'Tags': {
                    'string': 'string'
                },
                'TimeDelaySeconds': 123,
                'Url': 'string',
                'Whitelist': [
                    'string',
                ]
            },
        ]
    }
    
    
    :returns: 
    (dict) -- A collection of OriginEndpoint records.
    NextToken (string) -- A token that can be used to resume pagination from the end of the collection.
    OriginEndpoints (list) -- A list of OriginEndpoint records.
    (dict) -- An OriginEndpoint resource configuration.
    Arn (string) -- The Amazon Resource Name (ARN) assigned to the OriginEndpoint.
    Authorization (dict) -- CDN Authorization credentials
    CdnIdentifierSecret (string) -- The Amazon Resource Name (ARN) for the secret in Secrets Manager that your Content Distribution Network (CDN) uses for authorization to access your endpoint.
    SecretsRoleArn (string) -- The Amazon Resource Name (ARN) for the IAM role that allows MediaPackage to communicate with AWS Secrets Manager.
    
    
    ChannelId (string) -- The ID of the Channel the OriginEndpoint is associated with.
    CmafPackage (dict) -- A Common Media Application Format (CMAF) packaging configuration.
    Encryption (dict) -- A Common Media Application Format (CMAF) encryption configuration.
    KeyRotationIntervalSeconds (integer) -- Time (in seconds) between each encryption key rotation.
    SpekeKeyProvider (dict) -- A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
    CertificateArn (string) -- An Amazon Resource Name (ARN) of a Certificate Manager certificate that MediaPackage will use for enforcing secure end-to-end data transfer with the key provider service.
    ResourceId (string) -- The resource ID to include in key requests.
    RoleArn (string) -- An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.
    SystemIds (list) -- The system IDs to include in key requests.
    (string) --
    
    
    Url (string) -- The URL of the external key provider service.
    
    
    
    
    HlsManifests (list) -- A list of HLS manifest configurations
    (dict) -- A HTTP Live Streaming (HLS) manifest configuration.
    AdMarkers (string) -- This setting controls how ad markers are included in the packaged OriginEndpoint. "NONE" will omit all SCTE-35 ad markers from the output. "PASSTHROUGH" causes the manifest to contain a copy of the SCTE-35 ad markers (comments) taken directly from the input HTTP Live Streaming (HLS) manifest. "SCTE35_ENHANCED" generates ad markers and blackout tags based on SCTE-35 messages in the input source.
    Id (string) -- The ID of the manifest. The ID must be unique within the OriginEndpoint and it cannot be changed after it is created.
    IncludeIframeOnlyStream (boolean) -- When enabled, an I-Frame only stream will be included in the output.
    ManifestName (string) -- An optional short string appended to the end of the OriginEndpoint URL. If not specified, defaults to the manifestName for the OriginEndpoint.
    PlaylistType (string) -- The HTTP Live Streaming (HLS) playlist type. When either "EVENT" or "VOD" is specified, a corresponding EXT-X-PLAYLIST-TYPE entry will be included in the media playlist.
    PlaylistWindowSeconds (integer) -- Time window (in seconds) contained in each parent manifest.
    ProgramDateTimeIntervalSeconds (integer) -- The interval (in seconds) between each EXT-X-PROGRAM-DATE-TIME tag inserted into manifests. Additionally, when an interval is specified ID3Timed Metadata messages will be generated every 5 seconds using the ingest time of the content. If the interval is not specified, or set to 0, then no EXT-X-PROGRAM-DATE-TIME tags will be inserted into manifests and no ID3Timed Metadata messages will be generated. Note that irrespective of this parameter, if any ID3 Timed Metadata is found in HTTP Live Streaming (HLS) input, it will be passed through to HLS output.
    Url (string) -- The URL of the packaged OriginEndpoint for consumption.
    
    
    
    
    SegmentDurationSeconds (integer) -- Duration (in seconds) of each segment. Actual segments will be rounded to the nearest multiple of the source segment duration.
    SegmentPrefix (string) -- An optional custom string that is prepended to the name of each segment. If not specified, it defaults to the ChannelId.
    StreamSelection (dict) -- A StreamSelection configuration.
    MaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.
    MinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.
    StreamOrder (string) -- A directive that determines the order of streams in the output.
    
    
    
    
    DashPackage (dict) -- A Dynamic Adaptive Streaming over HTTP (DASH) packaging configuration.
    AdTriggers (list) -- A list of SCTE-35 message types that are treated as ad markers in the output. If empty, no ad markers are output. Specify multiple items to create ad markers for all of the included message types.
    (string) --
    
    
    AdsOnDeliveryRestrictions (string) -- This setting allows the delivery restriction flags on SCTE-35 segmentation descriptors to determine whether a message signals an ad. Choosing "NONE" means no SCTE-35 messages become ads. Choosing "RESTRICTED" means SCTE-35 messages of the types specified in AdTriggers that contain delivery restrictions will be treated as ads. Choosing "UNRESTRICTED" means SCTE-35 messages of the types specified in AdTriggers that do not contain delivery restrictions will be treated as ads. Choosing "BOTH" means all SCTE-35 messages of the types specified in AdTriggers will be treated as ads. Note that Splice Insert messages do not have these flags and are always treated as ads if specified in AdTriggers.
    Encryption (dict) -- A Dynamic Adaptive Streaming over HTTP (DASH) encryption configuration.
    KeyRotationIntervalSeconds (integer) -- Time (in seconds) between each encryption key rotation.
    SpekeKeyProvider (dict) -- A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
    CertificateArn (string) -- An Amazon Resource Name (ARN) of a Certificate Manager certificate that MediaPackage will use for enforcing secure end-to-end data transfer with the key provider service.
    ResourceId (string) -- The resource ID to include in key requests.
    RoleArn (string) -- An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.
    SystemIds (list) -- The system IDs to include in key requests.
    (string) --
    
    
    Url (string) -- The URL of the external key provider service.
    
    
    
    
    ManifestLayout (string) -- Determines the position of some tags in the Media Presentation Description (MPD). When set to FULL, elements like SegmentTemplate and ContentProtection are included in each Representation. When set to COMPACT, duplicate elements are combined and presented at the AdaptationSet level.
    ManifestWindowSeconds (integer) -- Time window (in seconds) contained in each manifest.
    MinBufferTimeSeconds (integer) -- Minimum duration (in seconds) that a player will buffer media before starting the presentation.
    MinUpdatePeriodSeconds (integer) -- Minimum duration (in seconds) between potential changes to the Dynamic Adaptive Streaming over HTTP (DASH) Media Presentation Description (MPD).
    PeriodTriggers (list) -- A list of triggers that controls when the outgoing Dynamic Adaptive Streaming over HTTP (DASH) Media Presentation Description (MPD) will be partitioned into multiple periods. If empty, the content will not be partitioned into more than one period. If the list contains "ADS", new periods will be created where the Channel source contains SCTE-35 ad markers.
    (string) --
    
    
    Profile (string) -- The Dynamic Adaptive Streaming over HTTP (DASH) profile type. When set to "HBBTV_1_5", HbbTV 1.5 compliant output is enabled.
    SegmentDurationSeconds (integer) -- Duration (in seconds) of each segment. Actual segments will be rounded to the nearest multiple of the source segment duration.
    SegmentTemplateFormat (string) -- Determines the type of SegmentTemplate included in the Media Presentation Description (MPD). When set to NUMBER_WITH_TIMELINE, a full timeline is presented in each SegmentTemplate, with $Number$ media URLs. When set to TIME_WITH_TIMELINE, a full timeline is presented in each SegmentTemplate, with $Time$ media URLs. When set to NUMBER_WITH_DURATION, only a duration is included in each SegmentTemplate, with $Number$ media URLs.
    StreamSelection (dict) -- A StreamSelection configuration.
    MaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.
    MinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.
    StreamOrder (string) -- A directive that determines the order of streams in the output.
    
    
    SuggestedPresentationDelaySeconds (integer) -- Duration (in seconds) to delay live content before presentation.
    
    
    Description (string) -- A short text description of the OriginEndpoint.
    HlsPackage (dict) -- An HTTP Live Streaming (HLS) packaging configuration.
    AdMarkers (string) -- This setting controls how ad markers are included in the packaged OriginEndpoint. "NONE" will omit all SCTE-35 ad markers from the output. "PASSTHROUGH" causes the manifest to contain a copy of the SCTE-35 ad markers (comments) taken directly from the input HTTP Live Streaming (HLS) manifest. "SCTE35_ENHANCED" generates ad markers and blackout tags based on SCTE-35 messages in the input source.
    AdTriggers (list) -- A list of SCTE-35 message types that are treated as ad markers in the output. If empty, no ad markers are output. Specify multiple items to create ad markers for all of the included message types.
    (string) --
    
    
    AdsOnDeliveryRestrictions (string) -- This setting allows the delivery restriction flags on SCTE-35 segmentation descriptors to determine whether a message signals an ad. Choosing "NONE" means no SCTE-35 messages become ads. Choosing "RESTRICTED" means SCTE-35 messages of the types specified in AdTriggers that contain delivery restrictions will be treated as ads. Choosing "UNRESTRICTED" means SCTE-35 messages of the types specified in AdTriggers that do not contain delivery restrictions will be treated as ads. Choosing "BOTH" means all SCTE-35 messages of the types specified in AdTriggers will be treated as ads. Note that Splice Insert messages do not have these flags and are always treated as ads if specified in AdTriggers.
    Encryption (dict) -- An HTTP Live Streaming (HLS) encryption configuration.
    ConstantInitializationVector (string) -- A constant initialization vector for encryption (optional). When not specified the initialization vector will be periodically rotated.
    EncryptionMethod (string) -- The encryption method to use.
    KeyRotationIntervalSeconds (integer) -- Interval (in seconds) between each encryption key rotation.
    RepeatExtXKey (boolean) -- When enabled, the EXT-X-KEY tag will be repeated in output manifests.
    SpekeKeyProvider (dict) -- A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
    CertificateArn (string) -- An Amazon Resource Name (ARN) of a Certificate Manager certificate that MediaPackage will use for enforcing secure end-to-end data transfer with the key provider service.
    ResourceId (string) -- The resource ID to include in key requests.
    RoleArn (string) -- An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.
    SystemIds (list) -- The system IDs to include in key requests.
    (string) --
    
    
    Url (string) -- The URL of the external key provider service.
    
    
    
    
    IncludeIframeOnlyStream (boolean) -- When enabled, an I-Frame only stream will be included in the output.
    PlaylistType (string) -- The HTTP Live Streaming (HLS) playlist type. When either "EVENT" or "VOD" is specified, a corresponding EXT-X-PLAYLIST-TYPE entry will be included in the media playlist.
    PlaylistWindowSeconds (integer) -- Time window (in seconds) contained in each parent manifest.
    ProgramDateTimeIntervalSeconds (integer) -- The interval (in seconds) between each EXT-X-PROGRAM-DATE-TIME tag inserted into manifests. Additionally, when an interval is specified ID3Timed Metadata messages will be generated every 5 seconds using the ingest time of the content. If the interval is not specified, or set to 0, then no EXT-X-PROGRAM-DATE-TIME tags will be inserted into manifests and no ID3Timed Metadata messages will be generated. Note that irrespective of this parameter, if any ID3 Timed Metadata is found in HTTP Live Streaming (HLS) input, it will be passed through to HLS output.
    SegmentDurationSeconds (integer) -- Duration (in seconds) of each fragment. Actual fragments will be rounded to the nearest multiple of the source fragment duration.
    StreamSelection (dict) -- A StreamSelection configuration.
    MaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.
    MinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.
    StreamOrder (string) -- A directive that determines the order of streams in the output.
    
    
    UseAudioRenditionGroup (boolean) -- When enabled, audio streams will be placed in rendition groups in the output.
    
    
    Id (string) -- The ID of the OriginEndpoint.
    ManifestName (string) -- A short string appended to the end of the OriginEndpoint URL.
    MssPackage (dict) -- A Microsoft Smooth Streaming (MSS) packaging configuration.
    Encryption (dict) -- A Microsoft Smooth Streaming (MSS) encryption configuration.
    SpekeKeyProvider (dict) -- A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
    CertificateArn (string) -- An Amazon Resource Name (ARN) of a Certificate Manager certificate that MediaPackage will use for enforcing secure end-to-end data transfer with the key provider service.
    ResourceId (string) -- The resource ID to include in key requests.
    RoleArn (string) -- An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.
    SystemIds (list) -- The system IDs to include in key requests.
    (string) --
    
    
    Url (string) -- The URL of the external key provider service.
    
    
    
    
    ManifestWindowSeconds (integer) -- The time window (in seconds) contained in each manifest.
    SegmentDurationSeconds (integer) -- The duration (in seconds) of each segment.
    StreamSelection (dict) -- A StreamSelection configuration.
    MaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.
    MinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.
    StreamOrder (string) -- A directive that determines the order of streams in the output.
    
    
    
    
    Origination (string) -- Control whether origination of video is allowed for this OriginEndpoint. If set to ALLOW, the OriginEndpoint may by requested, pursuant to any other form of access control. If set to DENY, the OriginEndpoint may not be requested. This can be helpful for Live to VOD harvesting, or for temporarily disabling origination
    StartoverWindowSeconds (integer) -- Maximum duration (seconds) of content to retain for startover playback. If not specified, startover playback will be disabled for the OriginEndpoint.
    Tags (dict) -- A collection of tags associated with a resource
    (string) --
    (string) --
    
    
    
    
    TimeDelaySeconds (integer) -- Amount of delay (seconds) to enforce on the playback of live content. If not specified, there will be no time delay in effect for the OriginEndpoint.
    Url (string) -- The URL of the packaged OriginEndpoint for consumption.
    Whitelist (list) -- A list of source IP CIDR blocks that will be allowed to access the OriginEndpoint.
    (string) --
    
    
    
    
    
    
    
    
    
    """
    pass

def list_tags_for_resource(ResourceArn=None):
    """
    See also: AWS API Documentation
    
    
    :example: response = client.list_tags_for_resource(
        ResourceArn='string'
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]

    :rtype: dict
ReturnsResponse Syntax{
    'Tags': {
        'string': 'string'
    }
}


Response Structure

(dict) -- 200 response
Tags (dict) --
(string) --
(string) --










    :return: {
        'Tags': {
            'string': 'string'
        }
    }
    
    
    """
    pass

def rotate_channel_credentials(Id=None):
    """
    Changes the Channel\'s first IngestEndpoint\'s username and password. WARNING - This API is deprecated. Please use RotateIngestEndpointCredentials instead
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.rotate_channel_credentials(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED] The ID of the channel to update.

    :rtype: dict
ReturnsResponse Syntax{
    'Arn': 'string',
    'Description': 'string',
    'HlsIngest': {
        'IngestEndpoints': [
            {
                'Id': 'string',
                'Password': 'string',
                'Url': 'string',
                'Username': 'string'
            },
        ]
    },
    'Id': 'string',
    'Tags': {
        'string': 'string'
    }
}


Response Structure

(dict) -- The updated Channel record.
Arn (string) -- The Amazon Resource Name (ARN) assigned to the Channel.
Description (string) -- A short text description of the Channel.
HlsIngest (dict) -- An HTTP Live Streaming (HLS) ingest resource configuration.
IngestEndpoints (list) -- A list of endpoints to which the source stream should be sent.
(dict) -- An endpoint for ingesting source content for a Channel.
Id (string) -- The system generated unique identifier for the IngestEndpoint
Password (string) -- The system generated password for ingest authentication.
Url (string) -- The ingest URL to which the source stream should be sent.
Username (string) -- The system generated username for ingest authentication.






Id (string) -- The ID of the Channel.
Tags (dict) -- A collection of tags associated with a resource
(string) --
(string) --









Exceptions

MediaPackage.Client.exceptions.UnprocessableEntityException
MediaPackage.Client.exceptions.InternalServerErrorException
MediaPackage.Client.exceptions.ForbiddenException
MediaPackage.Client.exceptions.NotFoundException
MediaPackage.Client.exceptions.ServiceUnavailableException
MediaPackage.Client.exceptions.TooManyRequestsException


    :return: {
        'Arn': 'string',
        'Description': 'string',
        'HlsIngest': {
            'IngestEndpoints': [
                {
                    'Id': 'string',
                    'Password': 'string',
                    'Url': 'string',
                    'Username': 'string'
                },
            ]
        },
        'Id': 'string',
        'Tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    MediaPackage.Client.exceptions.UnprocessableEntityException
    MediaPackage.Client.exceptions.InternalServerErrorException
    MediaPackage.Client.exceptions.ForbiddenException
    MediaPackage.Client.exceptions.NotFoundException
    MediaPackage.Client.exceptions.ServiceUnavailableException
    MediaPackage.Client.exceptions.TooManyRequestsException
    
    """
    pass

def rotate_ingest_endpoint_credentials(Id=None, IngestEndpointId=None):
    """
    Rotate the IngestEndpoint\'s username and password, as specified by the IngestEndpoint\'s id.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.rotate_ingest_endpoint_credentials(
        Id='string',
        IngestEndpointId='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED] The ID of the channel the IngestEndpoint is on.

    :type IngestEndpointId: string
    :param IngestEndpointId: [REQUIRED] The id of the IngestEndpoint whose credentials should be rotated

    :rtype: dict

ReturnsResponse Syntax
{
    'Arn': 'string',
    'Description': 'string',
    'HlsIngest': {
        'IngestEndpoints': [
            {
                'Id': 'string',
                'Password': 'string',
                'Url': 'string',
                'Username': 'string'
            },
        ]
    },
    'Id': 'string',
    'Tags': {
        'string': 'string'
    }
}


Response Structure

(dict) -- The updated Channel record.
Arn (string) -- The Amazon Resource Name (ARN) assigned to the Channel.
Description (string) -- A short text description of the Channel.
HlsIngest (dict) -- An HTTP Live Streaming (HLS) ingest resource configuration.
IngestEndpoints (list) -- A list of endpoints to which the source stream should be sent.
(dict) -- An endpoint for ingesting source content for a Channel.
Id (string) -- The system generated unique identifier for the IngestEndpoint
Password (string) -- The system generated password for ingest authentication.
Url (string) -- The ingest URL to which the source stream should be sent.
Username (string) -- The system generated username for ingest authentication.






Id (string) -- The ID of the Channel.
Tags (dict) -- A collection of tags associated with a resource
(string) --
(string) --










Exceptions

MediaPackage.Client.exceptions.UnprocessableEntityException
MediaPackage.Client.exceptions.InternalServerErrorException
MediaPackage.Client.exceptions.ForbiddenException
MediaPackage.Client.exceptions.NotFoundException
MediaPackage.Client.exceptions.ServiceUnavailableException
MediaPackage.Client.exceptions.TooManyRequestsException


    :return: {
        'Arn': 'string',
        'Description': 'string',
        'HlsIngest': {
            'IngestEndpoints': [
                {
                    'Id': 'string',
                    'Password': 'string',
                    'Url': 'string',
                    'Username': 'string'
                },
            ]
        },
        'Id': 'string',
        'Tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    (dict) -- The updated Channel record.
    Arn (string) -- The Amazon Resource Name (ARN) assigned to the Channel.
    Description (string) -- A short text description of the Channel.
    HlsIngest (dict) -- An HTTP Live Streaming (HLS) ingest resource configuration.
    IngestEndpoints (list) -- A list of endpoints to which the source stream should be sent.
    (dict) -- An endpoint for ingesting source content for a Channel.
    Id (string) -- The system generated unique identifier for the IngestEndpoint
    Password (string) -- The system generated password for ingest authentication.
    Url (string) -- The ingest URL to which the source stream should be sent.
    Username (string) -- The system generated username for ingest authentication.
    
    
    
    
    
    
    Id (string) -- The ID of the Channel.
    Tags (dict) -- A collection of tags associated with a resource
    (string) --
    (string) --
    
    
    
    
    
    
    
    """
    pass

def tag_resource(ResourceArn=None, Tags=None):
    """
    See also: AWS API Documentation
    
    
    :example: response = client.tag_resource(
        ResourceArn='string',
        Tags={
            'string': 'string'
        }
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]

    :type Tags: dict
    :param Tags: [REQUIRED]\n\n(string) --\n(string) --\n\n\n\n

    """
    pass

def untag_resource(ResourceArn=None, TagKeys=None):
    """
    See also: AWS API Documentation
    
    
    :example: response = client.untag_resource(
        ResourceArn='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]

    :type TagKeys: list
    :param TagKeys: [REQUIRED] The key(s) of tag to be deleted\n\n(string) --\n\n

    """
    pass

def update_channel(Description=None, Id=None):
    """
    Updates an existing Channel.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_channel(
        Description='string',
        Id='string'
    )
    
    
    :type Description: string
    :param Description: A short text description of the Channel.

    :type Id: string
    :param Id: [REQUIRED] The ID of the Channel to update.

    :rtype: dict

ReturnsResponse Syntax
{
    'Arn': 'string',
    'Description': 'string',
    'HlsIngest': {
        'IngestEndpoints': [
            {
                'Id': 'string',
                'Password': 'string',
                'Url': 'string',
                'Username': 'string'
            },
        ]
    },
    'Id': 'string',
    'Tags': {
        'string': 'string'
    }
}


Response Structure

(dict) -- The updated Channel record.
Arn (string) -- The Amazon Resource Name (ARN) assigned to the Channel.
Description (string) -- A short text description of the Channel.
HlsIngest (dict) -- An HTTP Live Streaming (HLS) ingest resource configuration.
IngestEndpoints (list) -- A list of endpoints to which the source stream should be sent.
(dict) -- An endpoint for ingesting source content for a Channel.
Id (string) -- The system generated unique identifier for the IngestEndpoint
Password (string) -- The system generated password for ingest authentication.
Url (string) -- The ingest URL to which the source stream should be sent.
Username (string) -- The system generated username for ingest authentication.






Id (string) -- The ID of the Channel.
Tags (dict) -- A collection of tags associated with a resource
(string) --
(string) --










Exceptions

MediaPackage.Client.exceptions.UnprocessableEntityException
MediaPackage.Client.exceptions.InternalServerErrorException
MediaPackage.Client.exceptions.ForbiddenException
MediaPackage.Client.exceptions.NotFoundException
MediaPackage.Client.exceptions.ServiceUnavailableException
MediaPackage.Client.exceptions.TooManyRequestsException


    :return: {
        'Arn': 'string',
        'Description': 'string',
        'HlsIngest': {
            'IngestEndpoints': [
                {
                    'Id': 'string',
                    'Password': 'string',
                    'Url': 'string',
                    'Username': 'string'
                },
            ]
        },
        'Id': 'string',
        'Tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    (dict) -- The updated Channel record.
    Arn (string) -- The Amazon Resource Name (ARN) assigned to the Channel.
    Description (string) -- A short text description of the Channel.
    HlsIngest (dict) -- An HTTP Live Streaming (HLS) ingest resource configuration.
    IngestEndpoints (list) -- A list of endpoints to which the source stream should be sent.
    (dict) -- An endpoint for ingesting source content for a Channel.
    Id (string) -- The system generated unique identifier for the IngestEndpoint
    Password (string) -- The system generated password for ingest authentication.
    Url (string) -- The ingest URL to which the source stream should be sent.
    Username (string) -- The system generated username for ingest authentication.
    
    
    
    
    
    
    Id (string) -- The ID of the Channel.
    Tags (dict) -- A collection of tags associated with a resource
    (string) --
    (string) --
    
    
    
    
    
    
    
    """
    pass

def update_origin_endpoint(Authorization=None, CmafPackage=None, DashPackage=None, Description=None, HlsPackage=None, Id=None, ManifestName=None, MssPackage=None, Origination=None, StartoverWindowSeconds=None, TimeDelaySeconds=None, Whitelist=None):
    """
    Updates an existing OriginEndpoint.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_origin_endpoint(
        Authorization={
            'CdnIdentifierSecret': 'string',
            'SecretsRoleArn': 'string'
        },
        CmafPackage={
            'Encryption': {
                'KeyRotationIntervalSeconds': 123,
                'SpekeKeyProvider': {
                    'CertificateArn': 'string',
                    'ResourceId': 'string',
                    'RoleArn': 'string',
                    'SystemIds': [
                        'string',
                    ],
                    'Url': 'string'
                }
            },
            'HlsManifests': [
                {
                    'AdMarkers': 'NONE'|'SCTE35_ENHANCED'|'PASSTHROUGH',
                    'AdTriggers': [
                        'SPLICE_INSERT'|'BREAK'|'PROVIDER_ADVERTISEMENT'|'DISTRIBUTOR_ADVERTISEMENT'|'PROVIDER_PLACEMENT_OPPORTUNITY'|'DISTRIBUTOR_PLACEMENT_OPPORTUNITY'|'PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY'|'DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY',
                    ],
                    'AdsOnDeliveryRestrictions': 'NONE'|'RESTRICTED'|'UNRESTRICTED'|'BOTH',
                    'Id': 'string',
                    'IncludeIframeOnlyStream': True|False,
                    'ManifestName': 'string',
                    'PlaylistType': 'NONE'|'EVENT'|'VOD',
                    'PlaylistWindowSeconds': 123,
                    'ProgramDateTimeIntervalSeconds': 123
                },
            ],
            'SegmentDurationSeconds': 123,
            'SegmentPrefix': 'string',
            'StreamSelection': {
                'MaxVideoBitsPerSecond': 123,
                'MinVideoBitsPerSecond': 123,
                'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
            }
        },
        DashPackage={
            'AdTriggers': [
                'SPLICE_INSERT'|'BREAK'|'PROVIDER_ADVERTISEMENT'|'DISTRIBUTOR_ADVERTISEMENT'|'PROVIDER_PLACEMENT_OPPORTUNITY'|'DISTRIBUTOR_PLACEMENT_OPPORTUNITY'|'PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY'|'DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY',
            ],
            'AdsOnDeliveryRestrictions': 'NONE'|'RESTRICTED'|'UNRESTRICTED'|'BOTH',
            'Encryption': {
                'KeyRotationIntervalSeconds': 123,
                'SpekeKeyProvider': {
                    'CertificateArn': 'string',
                    'ResourceId': 'string',
                    'RoleArn': 'string',
                    'SystemIds': [
                        'string',
                    ],
                    'Url': 'string'
                }
            },
            'ManifestLayout': 'FULL'|'COMPACT',
            'ManifestWindowSeconds': 123,
            'MinBufferTimeSeconds': 123,
            'MinUpdatePeriodSeconds': 123,
            'PeriodTriggers': [
                'ADS',
            ],
            'Profile': 'NONE'|'HBBTV_1_5',
            'SegmentDurationSeconds': 123,
            'SegmentTemplateFormat': 'NUMBER_WITH_TIMELINE'|'TIME_WITH_TIMELINE'|'NUMBER_WITH_DURATION',
            'StreamSelection': {
                'MaxVideoBitsPerSecond': 123,
                'MinVideoBitsPerSecond': 123,
                'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
            },
            'SuggestedPresentationDelaySeconds': 123
        },
        Description='string',
        HlsPackage={
            'AdMarkers': 'NONE'|'SCTE35_ENHANCED'|'PASSTHROUGH',
            'AdTriggers': [
                'SPLICE_INSERT'|'BREAK'|'PROVIDER_ADVERTISEMENT'|'DISTRIBUTOR_ADVERTISEMENT'|'PROVIDER_PLACEMENT_OPPORTUNITY'|'DISTRIBUTOR_PLACEMENT_OPPORTUNITY'|'PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY'|'DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY',
            ],
            'AdsOnDeliveryRestrictions': 'NONE'|'RESTRICTED'|'UNRESTRICTED'|'BOTH',
            'Encryption': {
                'ConstantInitializationVector': 'string',
                'EncryptionMethod': 'AES_128'|'SAMPLE_AES',
                'KeyRotationIntervalSeconds': 123,
                'RepeatExtXKey': True|False,
                'SpekeKeyProvider': {
                    'CertificateArn': 'string',
                    'ResourceId': 'string',
                    'RoleArn': 'string',
                    'SystemIds': [
                        'string',
                    ],
                    'Url': 'string'
                }
            },
            'IncludeIframeOnlyStream': True|False,
            'PlaylistType': 'NONE'|'EVENT'|'VOD',
            'PlaylistWindowSeconds': 123,
            'ProgramDateTimeIntervalSeconds': 123,
            'SegmentDurationSeconds': 123,
            'StreamSelection': {
                'MaxVideoBitsPerSecond': 123,
                'MinVideoBitsPerSecond': 123,
                'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
            },
            'UseAudioRenditionGroup': True|False
        },
        Id='string',
        ManifestName='string',
        MssPackage={
            'Encryption': {
                'SpekeKeyProvider': {
                    'CertificateArn': 'string',
                    'ResourceId': 'string',
                    'RoleArn': 'string',
                    'SystemIds': [
                        'string',
                    ],
                    'Url': 'string'
                }
            },
            'ManifestWindowSeconds': 123,
            'SegmentDurationSeconds': 123,
            'StreamSelection': {
                'MaxVideoBitsPerSecond': 123,
                'MinVideoBitsPerSecond': 123,
                'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
            }
        },
        Origination='ALLOW'|'DENY',
        StartoverWindowSeconds=123,
        TimeDelaySeconds=123,
        Whitelist=[
            'string',
        ]
    )
    
    
    :type Authorization: dict
    :param Authorization: CDN Authorization credentials\n\nCdnIdentifierSecret (string) -- [REQUIRED] The Amazon Resource Name (ARN) for the secret in Secrets Manager that your Content Distribution Network (CDN) uses for authorization to access your endpoint.\nSecretsRoleArn (string) -- [REQUIRED] The Amazon Resource Name (ARN) for the IAM role that allows MediaPackage to communicate with AWS Secrets Manager.\n\n

    :type CmafPackage: dict
    :param CmafPackage: A Common Media Application Format (CMAF) packaging configuration.\n\nEncryption (dict) -- A Common Media Application Format (CMAF) encryption configuration.\nKeyRotationIntervalSeconds (integer) -- Time (in seconds) between each encryption key rotation.\nSpekeKeyProvider (dict) -- [REQUIRED] A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.\nCertificateArn (string) -- An Amazon Resource Name (ARN) of a Certificate Manager certificate that MediaPackage will use for enforcing secure end-to-end data transfer with the key provider service.\nResourceId (string) -- [REQUIRED] The resource ID to include in key requests.\nRoleArn (string) -- [REQUIRED] An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.\nSystemIds (list) -- [REQUIRED] The system IDs to include in key requests.\n(string) --\n\n\nUrl (string) -- [REQUIRED] The URL of the external key provider service.\n\n\n\n\nHlsManifests (list) -- A list of HLS manifest configurations\n(dict) -- A HTTP Live Streaming (HLS) manifest configuration.\nAdMarkers (string) -- This setting controls how ad markers are included in the packaged OriginEndpoint. 'NONE' will omit all SCTE-35 ad markers from the output. 'PASSTHROUGH' causes the manifest to contain a copy of the SCTE-35 ad markers (comments) taken directly from the input HTTP Live Streaming (HLS) manifest. 'SCTE35_ENHANCED' generates ad markers and blackout tags based on SCTE-35 messages in the input source.\nAdTriggers (list) -- A list of SCTE-35 message types that are treated as ad markers in the output. If empty, no ad markers are output. Specify multiple items to create ad markers for all of the included message types.\n(string) --\n\n\nAdsOnDeliveryRestrictions (string) -- This setting allows the delivery restriction flags on SCTE-35 segmentation descriptors to determine whether a message signals an ad. Choosing 'NONE' means no SCTE-35 messages become ads. Choosing 'RESTRICTED' means SCTE-35 messages of the types specified in AdTriggers that contain delivery restrictions will be treated as ads. Choosing 'UNRESTRICTED' means SCTE-35 messages of the types specified in AdTriggers that do not contain delivery restrictions will be treated as ads. Choosing 'BOTH' means all SCTE-35 messages of the types specified in AdTriggers will be treated as ads. Note that Splice Insert messages do not have these flags and are always treated as ads if specified in AdTriggers.\nId (string) -- [REQUIRED] The ID of the manifest. The ID must be unique within the OriginEndpoint and it cannot be changed after it is created.\nIncludeIframeOnlyStream (boolean) -- When enabled, an I-Frame only stream will be included in the output.\nManifestName (string) -- An optional short string appended to the end of the OriginEndpoint URL. If not specified, defaults to the manifestName for the OriginEndpoint.\nPlaylistType (string) -- The HTTP Live Streaming (HLS) playlist type. When either 'EVENT' or 'VOD' is specified, a corresponding EXT-X-PLAYLIST-TYPE entry will be included in the media playlist.\nPlaylistWindowSeconds (integer) -- Time window (in seconds) contained in each parent manifest.\nProgramDateTimeIntervalSeconds (integer) -- The interval (in seconds) between each EXT-X-PROGRAM-DATE-TIME tag inserted into manifests. Additionally, when an interval is specified ID3Timed Metadata messages will be generated every 5 seconds using the ingest time of the content. If the interval is not specified, or set to 0, then no EXT-X-PROGRAM-DATE-TIME tags will be inserted into manifests and no ID3Timed Metadata messages will be generated. Note that irrespective of this parameter, if any ID3 Timed Metadata is found in HTTP Live Streaming (HLS) input, it will be passed through to HLS output.\n\n\n\n\nSegmentDurationSeconds (integer) -- Duration (in seconds) of each segment. Actual segments will be rounded to the nearest multiple of the source segment duration.\nSegmentPrefix (string) -- An optional custom string that is prepended to the name of each segment. If not specified, it defaults to the ChannelId.\nStreamSelection (dict) -- A StreamSelection configuration.\nMaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.\nMinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.\nStreamOrder (string) -- A directive that determines the order of streams in the output.\n\n\n\n

    :type DashPackage: dict
    :param DashPackage: A Dynamic Adaptive Streaming over HTTP (DASH) packaging configuration.\n\nAdTriggers (list) -- A list of SCTE-35 message types that are treated as ad markers in the output. If empty, no ad markers are output. Specify multiple items to create ad markers for all of the included message types.\n(string) --\n\n\nAdsOnDeliveryRestrictions (string) -- This setting allows the delivery restriction flags on SCTE-35 segmentation descriptors to determine whether a message signals an ad. Choosing 'NONE' means no SCTE-35 messages become ads. Choosing 'RESTRICTED' means SCTE-35 messages of the types specified in AdTriggers that contain delivery restrictions will be treated as ads. Choosing 'UNRESTRICTED' means SCTE-35 messages of the types specified in AdTriggers that do not contain delivery restrictions will be treated as ads. Choosing 'BOTH' means all SCTE-35 messages of the types specified in AdTriggers will be treated as ads. Note that Splice Insert messages do not have these flags and are always treated as ads if specified in AdTriggers.\nEncryption (dict) -- A Dynamic Adaptive Streaming over HTTP (DASH) encryption configuration.\nKeyRotationIntervalSeconds (integer) -- Time (in seconds) between each encryption key rotation.\nSpekeKeyProvider (dict) -- [REQUIRED] A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.\nCertificateArn (string) -- An Amazon Resource Name (ARN) of a Certificate Manager certificate that MediaPackage will use for enforcing secure end-to-end data transfer with the key provider service.\nResourceId (string) -- [REQUIRED] The resource ID to include in key requests.\nRoleArn (string) -- [REQUIRED] An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.\nSystemIds (list) -- [REQUIRED] The system IDs to include in key requests.\n(string) --\n\n\nUrl (string) -- [REQUIRED] The URL of the external key provider service.\n\n\n\n\nManifestLayout (string) -- Determines the position of some tags in the Media Presentation Description (MPD). When set to FULL, elements like SegmentTemplate and ContentProtection are included in each Representation. When set to COMPACT, duplicate elements are combined and presented at the AdaptationSet level.\nManifestWindowSeconds (integer) -- Time window (in seconds) contained in each manifest.\nMinBufferTimeSeconds (integer) -- Minimum duration (in seconds) that a player will buffer media before starting the presentation.\nMinUpdatePeriodSeconds (integer) -- Minimum duration (in seconds) between potential changes to the Dynamic Adaptive Streaming over HTTP (DASH) Media Presentation Description (MPD).\nPeriodTriggers (list) -- A list of triggers that controls when the outgoing Dynamic Adaptive Streaming over HTTP (DASH) Media Presentation Description (MPD) will be partitioned into multiple periods. If empty, the content will not be partitioned into more than one period. If the list contains 'ADS', new periods will be created where the Channel source contains SCTE-35 ad markers.\n(string) --\n\n\nProfile (string) -- The Dynamic Adaptive Streaming over HTTP (DASH) profile type. When set to 'HBBTV_1_5', HbbTV 1.5 compliant output is enabled.\nSegmentDurationSeconds (integer) -- Duration (in seconds) of each segment. Actual segments will be rounded to the nearest multiple of the source segment duration.\nSegmentTemplateFormat (string) -- Determines the type of SegmentTemplate included in the Media Presentation Description (MPD). When set to NUMBER_WITH_TIMELINE, a full timeline is presented in each SegmentTemplate, with $Number$ media URLs. When set to TIME_WITH_TIMELINE, a full timeline is presented in each SegmentTemplate, with $Time$ media URLs. When set to NUMBER_WITH_DURATION, only a duration is included in each SegmentTemplate, with $Number$ media URLs.\nStreamSelection (dict) -- A StreamSelection configuration.\nMaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.\nMinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.\nStreamOrder (string) -- A directive that determines the order of streams in the output.\n\n\nSuggestedPresentationDelaySeconds (integer) -- Duration (in seconds) to delay live content before presentation.\n\n

    :type Description: string
    :param Description: A short text description of the OriginEndpoint.

    :type HlsPackage: dict
    :param HlsPackage: An HTTP Live Streaming (HLS) packaging configuration.\n\nAdMarkers (string) -- This setting controls how ad markers are included in the packaged OriginEndpoint. 'NONE' will omit all SCTE-35 ad markers from the output. 'PASSTHROUGH' causes the manifest to contain a copy of the SCTE-35 ad markers (comments) taken directly from the input HTTP Live Streaming (HLS) manifest. 'SCTE35_ENHANCED' generates ad markers and blackout tags based on SCTE-35 messages in the input source.\nAdTriggers (list) -- A list of SCTE-35 message types that are treated as ad markers in the output. If empty, no ad markers are output. Specify multiple items to create ad markers for all of the included message types.\n(string) --\n\n\nAdsOnDeliveryRestrictions (string) -- This setting allows the delivery restriction flags on SCTE-35 segmentation descriptors to determine whether a message signals an ad. Choosing 'NONE' means no SCTE-35 messages become ads. Choosing 'RESTRICTED' means SCTE-35 messages of the types specified in AdTriggers that contain delivery restrictions will be treated as ads. Choosing 'UNRESTRICTED' means SCTE-35 messages of the types specified in AdTriggers that do not contain delivery restrictions will be treated as ads. Choosing 'BOTH' means all SCTE-35 messages of the types specified in AdTriggers will be treated as ads. Note that Splice Insert messages do not have these flags and are always treated as ads if specified in AdTriggers.\nEncryption (dict) -- An HTTP Live Streaming (HLS) encryption configuration.\nConstantInitializationVector (string) -- A constant initialization vector for encryption (optional). When not specified the initialization vector will be periodically rotated.\nEncryptionMethod (string) -- The encryption method to use.\nKeyRotationIntervalSeconds (integer) -- Interval (in seconds) between each encryption key rotation.\nRepeatExtXKey (boolean) -- When enabled, the EXT-X-KEY tag will be repeated in output manifests.\nSpekeKeyProvider (dict) -- [REQUIRED] A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.\nCertificateArn (string) -- An Amazon Resource Name (ARN) of a Certificate Manager certificate that MediaPackage will use for enforcing secure end-to-end data transfer with the key provider service.\nResourceId (string) -- [REQUIRED] The resource ID to include in key requests.\nRoleArn (string) -- [REQUIRED] An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.\nSystemIds (list) -- [REQUIRED] The system IDs to include in key requests.\n(string) --\n\n\nUrl (string) -- [REQUIRED] The URL of the external key provider service.\n\n\n\n\nIncludeIframeOnlyStream (boolean) -- When enabled, an I-Frame only stream will be included in the output.\nPlaylistType (string) -- The HTTP Live Streaming (HLS) playlist type. When either 'EVENT' or 'VOD' is specified, a corresponding EXT-X-PLAYLIST-TYPE entry will be included in the media playlist.\nPlaylistWindowSeconds (integer) -- Time window (in seconds) contained in each parent manifest.\nProgramDateTimeIntervalSeconds (integer) -- The interval (in seconds) between each EXT-X-PROGRAM-DATE-TIME tag inserted into manifests. Additionally, when an interval is specified ID3Timed Metadata messages will be generated every 5 seconds using the ingest time of the content. If the interval is not specified, or set to 0, then no EXT-X-PROGRAM-DATE-TIME tags will be inserted into manifests and no ID3Timed Metadata messages will be generated. Note that irrespective of this parameter, if any ID3 Timed Metadata is found in HTTP Live Streaming (HLS) input, it will be passed through to HLS output.\nSegmentDurationSeconds (integer) -- Duration (in seconds) of each fragment. Actual fragments will be rounded to the nearest multiple of the source fragment duration.\nStreamSelection (dict) -- A StreamSelection configuration.\nMaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.\nMinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.\nStreamOrder (string) -- A directive that determines the order of streams in the output.\n\n\nUseAudioRenditionGroup (boolean) -- When enabled, audio streams will be placed in rendition groups in the output.\n\n

    :type Id: string
    :param Id: [REQUIRED] The ID of the OriginEndpoint to update.

    :type ManifestName: string
    :param ManifestName: A short string that will be appended to the end of the Endpoint URL.

    :type MssPackage: dict
    :param MssPackage: A Microsoft Smooth Streaming (MSS) packaging configuration.\n\nEncryption (dict) -- A Microsoft Smooth Streaming (MSS) encryption configuration.\nSpekeKeyProvider (dict) -- [REQUIRED] A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.\nCertificateArn (string) -- An Amazon Resource Name (ARN) of a Certificate Manager certificate that MediaPackage will use for enforcing secure end-to-end data transfer with the key provider service.\nResourceId (string) -- [REQUIRED] The resource ID to include in key requests.\nRoleArn (string) -- [REQUIRED] An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.\nSystemIds (list) -- [REQUIRED] The system IDs to include in key requests.\n(string) --\n\n\nUrl (string) -- [REQUIRED] The URL of the external key provider service.\n\n\n\n\nManifestWindowSeconds (integer) -- The time window (in seconds) contained in each manifest.\nSegmentDurationSeconds (integer) -- The duration (in seconds) of each segment.\nStreamSelection (dict) -- A StreamSelection configuration.\nMaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.\nMinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.\nStreamOrder (string) -- A directive that determines the order of streams in the output.\n\n\n\n

    :type Origination: string
    :param Origination: Control whether origination of video is allowed for this OriginEndpoint. If set to ALLOW, the OriginEndpoint may by requested, pursuant to any other form of access control. If set to DENY, the OriginEndpoint may not be requested. This can be helpful for Live to VOD harvesting, or for temporarily disabling origination

    :type StartoverWindowSeconds: integer
    :param StartoverWindowSeconds: Maximum duration (in seconds) of content to retain for startover playback. If not specified, startover playback will be disabled for the OriginEndpoint.

    :type TimeDelaySeconds: integer
    :param TimeDelaySeconds: Amount of delay (in seconds) to enforce on the playback of live content. If not specified, there will be no time delay in effect for the OriginEndpoint.

    :type Whitelist: list
    :param Whitelist: A list of source IP CIDR blocks that will be allowed to access the OriginEndpoint.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Arn': 'string',
    'Authorization': {
        'CdnIdentifierSecret': 'string',
        'SecretsRoleArn': 'string'
    },
    'ChannelId': 'string',
    'CmafPackage': {
        'Encryption': {
            'KeyRotationIntervalSeconds': 123,
            'SpekeKeyProvider': {
                'CertificateArn': 'string',
                'ResourceId': 'string',
                'RoleArn': 'string',
                'SystemIds': [
                    'string',
                ],
                'Url': 'string'
            }
        },
        'HlsManifests': [
            {
                'AdMarkers': 'NONE'|'SCTE35_ENHANCED'|'PASSTHROUGH',
                'Id': 'string',
                'IncludeIframeOnlyStream': True|False,
                'ManifestName': 'string',
                'PlaylistType': 'NONE'|'EVENT'|'VOD',
                'PlaylistWindowSeconds': 123,
                'ProgramDateTimeIntervalSeconds': 123,
                'Url': 'string'
            },
        ],
        'SegmentDurationSeconds': 123,
        'SegmentPrefix': 'string',
        'StreamSelection': {
            'MaxVideoBitsPerSecond': 123,
            'MinVideoBitsPerSecond': 123,
            'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
        }
    },
    'DashPackage': {
        'AdTriggers': [
            'SPLICE_INSERT'|'BREAK'|'PROVIDER_ADVERTISEMENT'|'DISTRIBUTOR_ADVERTISEMENT'|'PROVIDER_PLACEMENT_OPPORTUNITY'|'DISTRIBUTOR_PLACEMENT_OPPORTUNITY'|'PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY'|'DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY',
        ],
        'AdsOnDeliveryRestrictions': 'NONE'|'RESTRICTED'|'UNRESTRICTED'|'BOTH',
        'Encryption': {
            'KeyRotationIntervalSeconds': 123,
            'SpekeKeyProvider': {
                'CertificateArn': 'string',
                'ResourceId': 'string',
                'RoleArn': 'string',
                'SystemIds': [
                    'string',
                ],
                'Url': 'string'
            }
        },
        'ManifestLayout': 'FULL'|'COMPACT',
        'ManifestWindowSeconds': 123,
        'MinBufferTimeSeconds': 123,
        'MinUpdatePeriodSeconds': 123,
        'PeriodTriggers': [
            'ADS',
        ],
        'Profile': 'NONE'|'HBBTV_1_5',
        'SegmentDurationSeconds': 123,
        'SegmentTemplateFormat': 'NUMBER_WITH_TIMELINE'|'TIME_WITH_TIMELINE'|'NUMBER_WITH_DURATION',
        'StreamSelection': {
            'MaxVideoBitsPerSecond': 123,
            'MinVideoBitsPerSecond': 123,
            'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
        },
        'SuggestedPresentationDelaySeconds': 123
    },
    'Description': 'string',
    'HlsPackage': {
        'AdMarkers': 'NONE'|'SCTE35_ENHANCED'|'PASSTHROUGH',
        'AdTriggers': [
            'SPLICE_INSERT'|'BREAK'|'PROVIDER_ADVERTISEMENT'|'DISTRIBUTOR_ADVERTISEMENT'|'PROVIDER_PLACEMENT_OPPORTUNITY'|'DISTRIBUTOR_PLACEMENT_OPPORTUNITY'|'PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY'|'DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY',
        ],
        'AdsOnDeliveryRestrictions': 'NONE'|'RESTRICTED'|'UNRESTRICTED'|'BOTH',
        'Encryption': {
            'ConstantInitializationVector': 'string',
            'EncryptionMethod': 'AES_128'|'SAMPLE_AES',
            'KeyRotationIntervalSeconds': 123,
            'RepeatExtXKey': True|False,
            'SpekeKeyProvider': {
                'CertificateArn': 'string',
                'ResourceId': 'string',
                'RoleArn': 'string',
                'SystemIds': [
                    'string',
                ],
                'Url': 'string'
            }
        },
        'IncludeIframeOnlyStream': True|False,
        'PlaylistType': 'NONE'|'EVENT'|'VOD',
        'PlaylistWindowSeconds': 123,
        'ProgramDateTimeIntervalSeconds': 123,
        'SegmentDurationSeconds': 123,
        'StreamSelection': {
            'MaxVideoBitsPerSecond': 123,
            'MinVideoBitsPerSecond': 123,
            'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
        },
        'UseAudioRenditionGroup': True|False
    },
    'Id': 'string',
    'ManifestName': 'string',
    'MssPackage': {
        'Encryption': {
            'SpekeKeyProvider': {
                'CertificateArn': 'string',
                'ResourceId': 'string',
                'RoleArn': 'string',
                'SystemIds': [
                    'string',
                ],
                'Url': 'string'
            }
        },
        'ManifestWindowSeconds': 123,
        'SegmentDurationSeconds': 123,
        'StreamSelection': {
            'MaxVideoBitsPerSecond': 123,
            'MinVideoBitsPerSecond': 123,
            'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
        }
    },
    'Origination': 'ALLOW'|'DENY',
    'StartoverWindowSeconds': 123,
    'Tags': {
        'string': 'string'
    },
    'TimeDelaySeconds': 123,
    'Url': 'string',
    'Whitelist': [
        'string',
    ]
}


Response Structure

(dict) -- An updated OriginEndpoint record.
Arn (string) -- The Amazon Resource Name (ARN) assigned to the OriginEndpoint.
Authorization (dict) -- CDN Authorization credentials
CdnIdentifierSecret (string) -- The Amazon Resource Name (ARN) for the secret in Secrets Manager that your Content Distribution Network (CDN) uses for authorization to access your endpoint.
SecretsRoleArn (string) -- The Amazon Resource Name (ARN) for the IAM role that allows MediaPackage to communicate with AWS Secrets Manager.


ChannelId (string) -- The ID of the Channel the OriginEndpoint is associated with.
CmafPackage (dict) -- A Common Media Application Format (CMAF) packaging configuration.
Encryption (dict) -- A Common Media Application Format (CMAF) encryption configuration.
KeyRotationIntervalSeconds (integer) -- Time (in seconds) between each encryption key rotation.
SpekeKeyProvider (dict) -- A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
CertificateArn (string) -- An Amazon Resource Name (ARN) of a Certificate Manager certificate that MediaPackage will use for enforcing secure end-to-end data transfer with the key provider service.
ResourceId (string) -- The resource ID to include in key requests.
RoleArn (string) -- An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.
SystemIds (list) -- The system IDs to include in key requests.
(string) --


Url (string) -- The URL of the external key provider service.




HlsManifests (list) -- A list of HLS manifest configurations
(dict) -- A HTTP Live Streaming (HLS) manifest configuration.
AdMarkers (string) -- This setting controls how ad markers are included in the packaged OriginEndpoint. "NONE" will omit all SCTE-35 ad markers from the output. "PASSTHROUGH" causes the manifest to contain a copy of the SCTE-35 ad markers (comments) taken directly from the input HTTP Live Streaming (HLS) manifest. "SCTE35_ENHANCED" generates ad markers and blackout tags based on SCTE-35 messages in the input source.
Id (string) -- The ID of the manifest. The ID must be unique within the OriginEndpoint and it cannot be changed after it is created.
IncludeIframeOnlyStream (boolean) -- When enabled, an I-Frame only stream will be included in the output.
ManifestName (string) -- An optional short string appended to the end of the OriginEndpoint URL. If not specified, defaults to the manifestName for the OriginEndpoint.
PlaylistType (string) -- The HTTP Live Streaming (HLS) playlist type. When either "EVENT" or "VOD" is specified, a corresponding EXT-X-PLAYLIST-TYPE entry will be included in the media playlist.
PlaylistWindowSeconds (integer) -- Time window (in seconds) contained in each parent manifest.
ProgramDateTimeIntervalSeconds (integer) -- The interval (in seconds) between each EXT-X-PROGRAM-DATE-TIME tag inserted into manifests. Additionally, when an interval is specified ID3Timed Metadata messages will be generated every 5 seconds using the ingest time of the content. If the interval is not specified, or set to 0, then no EXT-X-PROGRAM-DATE-TIME tags will be inserted into manifests and no ID3Timed Metadata messages will be generated. Note that irrespective of this parameter, if any ID3 Timed Metadata is found in HTTP Live Streaming (HLS) input, it will be passed through to HLS output.
Url (string) -- The URL of the packaged OriginEndpoint for consumption.




SegmentDurationSeconds (integer) -- Duration (in seconds) of each segment. Actual segments will be rounded to the nearest multiple of the source segment duration.
SegmentPrefix (string) -- An optional custom string that is prepended to the name of each segment. If not specified, it defaults to the ChannelId.
StreamSelection (dict) -- A StreamSelection configuration.
MaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.
MinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.
StreamOrder (string) -- A directive that determines the order of streams in the output.




DashPackage (dict) -- A Dynamic Adaptive Streaming over HTTP (DASH) packaging configuration.
AdTriggers (list) -- A list of SCTE-35 message types that are treated as ad markers in the output. If empty, no ad markers are output. Specify multiple items to create ad markers for all of the included message types.
(string) --


AdsOnDeliveryRestrictions (string) -- This setting allows the delivery restriction flags on SCTE-35 segmentation descriptors to determine whether a message signals an ad. Choosing "NONE" means no SCTE-35 messages become ads. Choosing "RESTRICTED" means SCTE-35 messages of the types specified in AdTriggers that contain delivery restrictions will be treated as ads. Choosing "UNRESTRICTED" means SCTE-35 messages of the types specified in AdTriggers that do not contain delivery restrictions will be treated as ads. Choosing "BOTH" means all SCTE-35 messages of the types specified in AdTriggers will be treated as ads. Note that Splice Insert messages do not have these flags and are always treated as ads if specified in AdTriggers.
Encryption (dict) -- A Dynamic Adaptive Streaming over HTTP (DASH) encryption configuration.
KeyRotationIntervalSeconds (integer) -- Time (in seconds) between each encryption key rotation.
SpekeKeyProvider (dict) -- A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
CertificateArn (string) -- An Amazon Resource Name (ARN) of a Certificate Manager certificate that MediaPackage will use for enforcing secure end-to-end data transfer with the key provider service.
ResourceId (string) -- The resource ID to include in key requests.
RoleArn (string) -- An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.
SystemIds (list) -- The system IDs to include in key requests.
(string) --


Url (string) -- The URL of the external key provider service.




ManifestLayout (string) -- Determines the position of some tags in the Media Presentation Description (MPD). When set to FULL, elements like SegmentTemplate and ContentProtection are included in each Representation. When set to COMPACT, duplicate elements are combined and presented at the AdaptationSet level.
ManifestWindowSeconds (integer) -- Time window (in seconds) contained in each manifest.
MinBufferTimeSeconds (integer) -- Minimum duration (in seconds) that a player will buffer media before starting the presentation.
MinUpdatePeriodSeconds (integer) -- Minimum duration (in seconds) between potential changes to the Dynamic Adaptive Streaming over HTTP (DASH) Media Presentation Description (MPD).
PeriodTriggers (list) -- A list of triggers that controls when the outgoing Dynamic Adaptive Streaming over HTTP (DASH) Media Presentation Description (MPD) will be partitioned into multiple periods. If empty, the content will not be partitioned into more than one period. If the list contains "ADS", new periods will be created where the Channel source contains SCTE-35 ad markers.
(string) --


Profile (string) -- The Dynamic Adaptive Streaming over HTTP (DASH) profile type. When set to "HBBTV_1_5", HbbTV 1.5 compliant output is enabled.
SegmentDurationSeconds (integer) -- Duration (in seconds) of each segment. Actual segments will be rounded to the nearest multiple of the source segment duration.
SegmentTemplateFormat (string) -- Determines the type of SegmentTemplate included in the Media Presentation Description (MPD). When set to NUMBER_WITH_TIMELINE, a full timeline is presented in each SegmentTemplate, with $Number$ media URLs. When set to TIME_WITH_TIMELINE, a full timeline is presented in each SegmentTemplate, with $Time$ media URLs. When set to NUMBER_WITH_DURATION, only a duration is included in each SegmentTemplate, with $Number$ media URLs.
StreamSelection (dict) -- A StreamSelection configuration.
MaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.
MinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.
StreamOrder (string) -- A directive that determines the order of streams in the output.


SuggestedPresentationDelaySeconds (integer) -- Duration (in seconds) to delay live content before presentation.


Description (string) -- A short text description of the OriginEndpoint.
HlsPackage (dict) -- An HTTP Live Streaming (HLS) packaging configuration.
AdMarkers (string) -- This setting controls how ad markers are included in the packaged OriginEndpoint. "NONE" will omit all SCTE-35 ad markers from the output. "PASSTHROUGH" causes the manifest to contain a copy of the SCTE-35 ad markers (comments) taken directly from the input HTTP Live Streaming (HLS) manifest. "SCTE35_ENHANCED" generates ad markers and blackout tags based on SCTE-35 messages in the input source.
AdTriggers (list) -- A list of SCTE-35 message types that are treated as ad markers in the output. If empty, no ad markers are output. Specify multiple items to create ad markers for all of the included message types.
(string) --


AdsOnDeliveryRestrictions (string) -- This setting allows the delivery restriction flags on SCTE-35 segmentation descriptors to determine whether a message signals an ad. Choosing "NONE" means no SCTE-35 messages become ads. Choosing "RESTRICTED" means SCTE-35 messages of the types specified in AdTriggers that contain delivery restrictions will be treated as ads. Choosing "UNRESTRICTED" means SCTE-35 messages of the types specified in AdTriggers that do not contain delivery restrictions will be treated as ads. Choosing "BOTH" means all SCTE-35 messages of the types specified in AdTriggers will be treated as ads. Note that Splice Insert messages do not have these flags and are always treated as ads if specified in AdTriggers.
Encryption (dict) -- An HTTP Live Streaming (HLS) encryption configuration.
ConstantInitializationVector (string) -- A constant initialization vector for encryption (optional). When not specified the initialization vector will be periodically rotated.
EncryptionMethod (string) -- The encryption method to use.
KeyRotationIntervalSeconds (integer) -- Interval (in seconds) between each encryption key rotation.
RepeatExtXKey (boolean) -- When enabled, the EXT-X-KEY tag will be repeated in output manifests.
SpekeKeyProvider (dict) -- A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
CertificateArn (string) -- An Amazon Resource Name (ARN) of a Certificate Manager certificate that MediaPackage will use for enforcing secure end-to-end data transfer with the key provider service.
ResourceId (string) -- The resource ID to include in key requests.
RoleArn (string) -- An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.
SystemIds (list) -- The system IDs to include in key requests.
(string) --


Url (string) -- The URL of the external key provider service.




IncludeIframeOnlyStream (boolean) -- When enabled, an I-Frame only stream will be included in the output.
PlaylistType (string) -- The HTTP Live Streaming (HLS) playlist type. When either "EVENT" or "VOD" is specified, a corresponding EXT-X-PLAYLIST-TYPE entry will be included in the media playlist.
PlaylistWindowSeconds (integer) -- Time window (in seconds) contained in each parent manifest.
ProgramDateTimeIntervalSeconds (integer) -- The interval (in seconds) between each EXT-X-PROGRAM-DATE-TIME tag inserted into manifests. Additionally, when an interval is specified ID3Timed Metadata messages will be generated every 5 seconds using the ingest time of the content. If the interval is not specified, or set to 0, then no EXT-X-PROGRAM-DATE-TIME tags will be inserted into manifests and no ID3Timed Metadata messages will be generated. Note that irrespective of this parameter, if any ID3 Timed Metadata is found in HTTP Live Streaming (HLS) input, it will be passed through to HLS output.
SegmentDurationSeconds (integer) -- Duration (in seconds) of each fragment. Actual fragments will be rounded to the nearest multiple of the source fragment duration.
StreamSelection (dict) -- A StreamSelection configuration.
MaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.
MinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.
StreamOrder (string) -- A directive that determines the order of streams in the output.


UseAudioRenditionGroup (boolean) -- When enabled, audio streams will be placed in rendition groups in the output.


Id (string) -- The ID of the OriginEndpoint.
ManifestName (string) -- A short string appended to the end of the OriginEndpoint URL.
MssPackage (dict) -- A Microsoft Smooth Streaming (MSS) packaging configuration.
Encryption (dict) -- A Microsoft Smooth Streaming (MSS) encryption configuration.
SpekeKeyProvider (dict) -- A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
CertificateArn (string) -- An Amazon Resource Name (ARN) of a Certificate Manager certificate that MediaPackage will use for enforcing secure end-to-end data transfer with the key provider service.
ResourceId (string) -- The resource ID to include in key requests.
RoleArn (string) -- An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.
SystemIds (list) -- The system IDs to include in key requests.
(string) --


Url (string) -- The URL of the external key provider service.




ManifestWindowSeconds (integer) -- The time window (in seconds) contained in each manifest.
SegmentDurationSeconds (integer) -- The duration (in seconds) of each segment.
StreamSelection (dict) -- A StreamSelection configuration.
MaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.
MinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.
StreamOrder (string) -- A directive that determines the order of streams in the output.




Origination (string) -- Control whether origination of video is allowed for this OriginEndpoint. If set to ALLOW, the OriginEndpoint may by requested, pursuant to any other form of access control. If set to DENY, the OriginEndpoint may not be requested. This can be helpful for Live to VOD harvesting, or for temporarily disabling origination
StartoverWindowSeconds (integer) -- Maximum duration (seconds) of content to retain for startover playback. If not specified, startover playback will be disabled for the OriginEndpoint.
Tags (dict) -- A collection of tags associated with a resource
(string) --
(string) --




TimeDelaySeconds (integer) -- Amount of delay (seconds) to enforce on the playback of live content. If not specified, there will be no time delay in effect for the OriginEndpoint.
Url (string) -- The URL of the packaged OriginEndpoint for consumption.
Whitelist (list) -- A list of source IP CIDR blocks that will be allowed to access the OriginEndpoint.
(string) --








Exceptions

MediaPackage.Client.exceptions.UnprocessableEntityException
MediaPackage.Client.exceptions.InternalServerErrorException
MediaPackage.Client.exceptions.ForbiddenException
MediaPackage.Client.exceptions.NotFoundException
MediaPackage.Client.exceptions.ServiceUnavailableException
MediaPackage.Client.exceptions.TooManyRequestsException


    :return: {
        'Arn': 'string',
        'Authorization': {
            'CdnIdentifierSecret': 'string',
            'SecretsRoleArn': 'string'
        },
        'ChannelId': 'string',
        'CmafPackage': {
            'Encryption': {
                'KeyRotationIntervalSeconds': 123,
                'SpekeKeyProvider': {
                    'CertificateArn': 'string',
                    'ResourceId': 'string',
                    'RoleArn': 'string',
                    'SystemIds': [
                        'string',
                    ],
                    'Url': 'string'
                }
            },
            'HlsManifests': [
                {
                    'AdMarkers': 'NONE'|'SCTE35_ENHANCED'|'PASSTHROUGH',
                    'Id': 'string',
                    'IncludeIframeOnlyStream': True|False,
                    'ManifestName': 'string',
                    'PlaylistType': 'NONE'|'EVENT'|'VOD',
                    'PlaylistWindowSeconds': 123,
                    'ProgramDateTimeIntervalSeconds': 123,
                    'Url': 'string'
                },
            ],
            'SegmentDurationSeconds': 123,
            'SegmentPrefix': 'string',
            'StreamSelection': {
                'MaxVideoBitsPerSecond': 123,
                'MinVideoBitsPerSecond': 123,
                'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
            }
        },
        'DashPackage': {
            'AdTriggers': [
                'SPLICE_INSERT'|'BREAK'|'PROVIDER_ADVERTISEMENT'|'DISTRIBUTOR_ADVERTISEMENT'|'PROVIDER_PLACEMENT_OPPORTUNITY'|'DISTRIBUTOR_PLACEMENT_OPPORTUNITY'|'PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY'|'DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY',
            ],
            'AdsOnDeliveryRestrictions': 'NONE'|'RESTRICTED'|'UNRESTRICTED'|'BOTH',
            'Encryption': {
                'KeyRotationIntervalSeconds': 123,
                'SpekeKeyProvider': {
                    'CertificateArn': 'string',
                    'ResourceId': 'string',
                    'RoleArn': 'string',
                    'SystemIds': [
                        'string',
                    ],
                    'Url': 'string'
                }
            },
            'ManifestLayout': 'FULL'|'COMPACT',
            'ManifestWindowSeconds': 123,
            'MinBufferTimeSeconds': 123,
            'MinUpdatePeriodSeconds': 123,
            'PeriodTriggers': [
                'ADS',
            ],
            'Profile': 'NONE'|'HBBTV_1_5',
            'SegmentDurationSeconds': 123,
            'SegmentTemplateFormat': 'NUMBER_WITH_TIMELINE'|'TIME_WITH_TIMELINE'|'NUMBER_WITH_DURATION',
            'StreamSelection': {
                'MaxVideoBitsPerSecond': 123,
                'MinVideoBitsPerSecond': 123,
                'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
            },
            'SuggestedPresentationDelaySeconds': 123
        },
        'Description': 'string',
        'HlsPackage': {
            'AdMarkers': 'NONE'|'SCTE35_ENHANCED'|'PASSTHROUGH',
            'AdTriggers': [
                'SPLICE_INSERT'|'BREAK'|'PROVIDER_ADVERTISEMENT'|'DISTRIBUTOR_ADVERTISEMENT'|'PROVIDER_PLACEMENT_OPPORTUNITY'|'DISTRIBUTOR_PLACEMENT_OPPORTUNITY'|'PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY'|'DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY',
            ],
            'AdsOnDeliveryRestrictions': 'NONE'|'RESTRICTED'|'UNRESTRICTED'|'BOTH',
            'Encryption': {
                'ConstantInitializationVector': 'string',
                'EncryptionMethod': 'AES_128'|'SAMPLE_AES',
                'KeyRotationIntervalSeconds': 123,
                'RepeatExtXKey': True|False,
                'SpekeKeyProvider': {
                    'CertificateArn': 'string',
                    'ResourceId': 'string',
                    'RoleArn': 'string',
                    'SystemIds': [
                        'string',
                    ],
                    'Url': 'string'
                }
            },
            'IncludeIframeOnlyStream': True|False,
            'PlaylistType': 'NONE'|'EVENT'|'VOD',
            'PlaylistWindowSeconds': 123,
            'ProgramDateTimeIntervalSeconds': 123,
            'SegmentDurationSeconds': 123,
            'StreamSelection': {
                'MaxVideoBitsPerSecond': 123,
                'MinVideoBitsPerSecond': 123,
                'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
            },
            'UseAudioRenditionGroup': True|False
        },
        'Id': 'string',
        'ManifestName': 'string',
        'MssPackage': {
            'Encryption': {
                'SpekeKeyProvider': {
                    'CertificateArn': 'string',
                    'ResourceId': 'string',
                    'RoleArn': 'string',
                    'SystemIds': [
                        'string',
                    ],
                    'Url': 'string'
                }
            },
            'ManifestWindowSeconds': 123,
            'SegmentDurationSeconds': 123,
            'StreamSelection': {
                'MaxVideoBitsPerSecond': 123,
                'MinVideoBitsPerSecond': 123,
                'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
            }
        },
        'Origination': 'ALLOW'|'DENY',
        'StartoverWindowSeconds': 123,
        'Tags': {
            'string': 'string'
        },
        'TimeDelaySeconds': 123,
        'Url': 'string',
        'Whitelist': [
            'string',
        ]
    }
    
    
    :returns: 
    (dict) -- An updated OriginEndpoint record.
    Arn (string) -- The Amazon Resource Name (ARN) assigned to the OriginEndpoint.
    Authorization (dict) -- CDN Authorization credentials
    CdnIdentifierSecret (string) -- The Amazon Resource Name (ARN) for the secret in Secrets Manager that your Content Distribution Network (CDN) uses for authorization to access your endpoint.
    SecretsRoleArn (string) -- The Amazon Resource Name (ARN) for the IAM role that allows MediaPackage to communicate with AWS Secrets Manager.
    
    
    ChannelId (string) -- The ID of the Channel the OriginEndpoint is associated with.
    CmafPackage (dict) -- A Common Media Application Format (CMAF) packaging configuration.
    Encryption (dict) -- A Common Media Application Format (CMAF) encryption configuration.
    KeyRotationIntervalSeconds (integer) -- Time (in seconds) between each encryption key rotation.
    SpekeKeyProvider (dict) -- A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
    CertificateArn (string) -- An Amazon Resource Name (ARN) of a Certificate Manager certificate that MediaPackage will use for enforcing secure end-to-end data transfer with the key provider service.
    ResourceId (string) -- The resource ID to include in key requests.
    RoleArn (string) -- An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.
    SystemIds (list) -- The system IDs to include in key requests.
    (string) --
    
    
    Url (string) -- The URL of the external key provider service.
    
    
    
    
    HlsManifests (list) -- A list of HLS manifest configurations
    (dict) -- A HTTP Live Streaming (HLS) manifest configuration.
    AdMarkers (string) -- This setting controls how ad markers are included in the packaged OriginEndpoint. "NONE" will omit all SCTE-35 ad markers from the output. "PASSTHROUGH" causes the manifest to contain a copy of the SCTE-35 ad markers (comments) taken directly from the input HTTP Live Streaming (HLS) manifest. "SCTE35_ENHANCED" generates ad markers and blackout tags based on SCTE-35 messages in the input source.
    Id (string) -- The ID of the manifest. The ID must be unique within the OriginEndpoint and it cannot be changed after it is created.
    IncludeIframeOnlyStream (boolean) -- When enabled, an I-Frame only stream will be included in the output.
    ManifestName (string) -- An optional short string appended to the end of the OriginEndpoint URL. If not specified, defaults to the manifestName for the OriginEndpoint.
    PlaylistType (string) -- The HTTP Live Streaming (HLS) playlist type. When either "EVENT" or "VOD" is specified, a corresponding EXT-X-PLAYLIST-TYPE entry will be included in the media playlist.
    PlaylistWindowSeconds (integer) -- Time window (in seconds) contained in each parent manifest.
    ProgramDateTimeIntervalSeconds (integer) -- The interval (in seconds) between each EXT-X-PROGRAM-DATE-TIME tag inserted into manifests. Additionally, when an interval is specified ID3Timed Metadata messages will be generated every 5 seconds using the ingest time of the content. If the interval is not specified, or set to 0, then no EXT-X-PROGRAM-DATE-TIME tags will be inserted into manifests and no ID3Timed Metadata messages will be generated. Note that irrespective of this parameter, if any ID3 Timed Metadata is found in HTTP Live Streaming (HLS) input, it will be passed through to HLS output.
    Url (string) -- The URL of the packaged OriginEndpoint for consumption.
    
    
    
    
    SegmentDurationSeconds (integer) -- Duration (in seconds) of each segment. Actual segments will be rounded to the nearest multiple of the source segment duration.
    SegmentPrefix (string) -- An optional custom string that is prepended to the name of each segment. If not specified, it defaults to the ChannelId.
    StreamSelection (dict) -- A StreamSelection configuration.
    MaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.
    MinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.
    StreamOrder (string) -- A directive that determines the order of streams in the output.
    
    
    
    
    DashPackage (dict) -- A Dynamic Adaptive Streaming over HTTP (DASH) packaging configuration.
    AdTriggers (list) -- A list of SCTE-35 message types that are treated as ad markers in the output. If empty, no ad markers are output. Specify multiple items to create ad markers for all of the included message types.
    (string) --
    
    
    AdsOnDeliveryRestrictions (string) -- This setting allows the delivery restriction flags on SCTE-35 segmentation descriptors to determine whether a message signals an ad. Choosing "NONE" means no SCTE-35 messages become ads. Choosing "RESTRICTED" means SCTE-35 messages of the types specified in AdTriggers that contain delivery restrictions will be treated as ads. Choosing "UNRESTRICTED" means SCTE-35 messages of the types specified in AdTriggers that do not contain delivery restrictions will be treated as ads. Choosing "BOTH" means all SCTE-35 messages of the types specified in AdTriggers will be treated as ads. Note that Splice Insert messages do not have these flags and are always treated as ads if specified in AdTriggers.
    Encryption (dict) -- A Dynamic Adaptive Streaming over HTTP (DASH) encryption configuration.
    KeyRotationIntervalSeconds (integer) -- Time (in seconds) between each encryption key rotation.
    SpekeKeyProvider (dict) -- A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
    CertificateArn (string) -- An Amazon Resource Name (ARN) of a Certificate Manager certificate that MediaPackage will use for enforcing secure end-to-end data transfer with the key provider service.
    ResourceId (string) -- The resource ID to include in key requests.
    RoleArn (string) -- An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.
    SystemIds (list) -- The system IDs to include in key requests.
    (string) --
    
    
    Url (string) -- The URL of the external key provider service.
    
    
    
    
    ManifestLayout (string) -- Determines the position of some tags in the Media Presentation Description (MPD). When set to FULL, elements like SegmentTemplate and ContentProtection are included in each Representation. When set to COMPACT, duplicate elements are combined and presented at the AdaptationSet level.
    ManifestWindowSeconds (integer) -- Time window (in seconds) contained in each manifest.
    MinBufferTimeSeconds (integer) -- Minimum duration (in seconds) that a player will buffer media before starting the presentation.
    MinUpdatePeriodSeconds (integer) -- Minimum duration (in seconds) between potential changes to the Dynamic Adaptive Streaming over HTTP (DASH) Media Presentation Description (MPD).
    PeriodTriggers (list) -- A list of triggers that controls when the outgoing Dynamic Adaptive Streaming over HTTP (DASH) Media Presentation Description (MPD) will be partitioned into multiple periods. If empty, the content will not be partitioned into more than one period. If the list contains "ADS", new periods will be created where the Channel source contains SCTE-35 ad markers.
    (string) --
    
    
    Profile (string) -- The Dynamic Adaptive Streaming over HTTP (DASH) profile type. When set to "HBBTV_1_5", HbbTV 1.5 compliant output is enabled.
    SegmentDurationSeconds (integer) -- Duration (in seconds) of each segment. Actual segments will be rounded to the nearest multiple of the source segment duration.
    SegmentTemplateFormat (string) -- Determines the type of SegmentTemplate included in the Media Presentation Description (MPD). When set to NUMBER_WITH_TIMELINE, a full timeline is presented in each SegmentTemplate, with $Number$ media URLs. When set to TIME_WITH_TIMELINE, a full timeline is presented in each SegmentTemplate, with $Time$ media URLs. When set to NUMBER_WITH_DURATION, only a duration is included in each SegmentTemplate, with $Number$ media URLs.
    StreamSelection (dict) -- A StreamSelection configuration.
    MaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.
    MinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.
    StreamOrder (string) -- A directive that determines the order of streams in the output.
    
    
    SuggestedPresentationDelaySeconds (integer) -- Duration (in seconds) to delay live content before presentation.
    
    
    Description (string) -- A short text description of the OriginEndpoint.
    HlsPackage (dict) -- An HTTP Live Streaming (HLS) packaging configuration.
    AdMarkers (string) -- This setting controls how ad markers are included in the packaged OriginEndpoint. "NONE" will omit all SCTE-35 ad markers from the output. "PASSTHROUGH" causes the manifest to contain a copy of the SCTE-35 ad markers (comments) taken directly from the input HTTP Live Streaming (HLS) manifest. "SCTE35_ENHANCED" generates ad markers and blackout tags based on SCTE-35 messages in the input source.
    AdTriggers (list) -- A list of SCTE-35 message types that are treated as ad markers in the output. If empty, no ad markers are output. Specify multiple items to create ad markers for all of the included message types.
    (string) --
    
    
    AdsOnDeliveryRestrictions (string) -- This setting allows the delivery restriction flags on SCTE-35 segmentation descriptors to determine whether a message signals an ad. Choosing "NONE" means no SCTE-35 messages become ads. Choosing "RESTRICTED" means SCTE-35 messages of the types specified in AdTriggers that contain delivery restrictions will be treated as ads. Choosing "UNRESTRICTED" means SCTE-35 messages of the types specified in AdTriggers that do not contain delivery restrictions will be treated as ads. Choosing "BOTH" means all SCTE-35 messages of the types specified in AdTriggers will be treated as ads. Note that Splice Insert messages do not have these flags and are always treated as ads if specified in AdTriggers.
    Encryption (dict) -- An HTTP Live Streaming (HLS) encryption configuration.
    ConstantInitializationVector (string) -- A constant initialization vector for encryption (optional). When not specified the initialization vector will be periodically rotated.
    EncryptionMethod (string) -- The encryption method to use.
    KeyRotationIntervalSeconds (integer) -- Interval (in seconds) between each encryption key rotation.
    RepeatExtXKey (boolean) -- When enabled, the EXT-X-KEY tag will be repeated in output manifests.
    SpekeKeyProvider (dict) -- A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
    CertificateArn (string) -- An Amazon Resource Name (ARN) of a Certificate Manager certificate that MediaPackage will use for enforcing secure end-to-end data transfer with the key provider service.
    ResourceId (string) -- The resource ID to include in key requests.
    RoleArn (string) -- An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.
    SystemIds (list) -- The system IDs to include in key requests.
    (string) --
    
    
    Url (string) -- The URL of the external key provider service.
    
    
    
    
    IncludeIframeOnlyStream (boolean) -- When enabled, an I-Frame only stream will be included in the output.
    PlaylistType (string) -- The HTTP Live Streaming (HLS) playlist type. When either "EVENT" or "VOD" is specified, a corresponding EXT-X-PLAYLIST-TYPE entry will be included in the media playlist.
    PlaylistWindowSeconds (integer) -- Time window (in seconds) contained in each parent manifest.
    ProgramDateTimeIntervalSeconds (integer) -- The interval (in seconds) between each EXT-X-PROGRAM-DATE-TIME tag inserted into manifests. Additionally, when an interval is specified ID3Timed Metadata messages will be generated every 5 seconds using the ingest time of the content. If the interval is not specified, or set to 0, then no EXT-X-PROGRAM-DATE-TIME tags will be inserted into manifests and no ID3Timed Metadata messages will be generated. Note that irrespective of this parameter, if any ID3 Timed Metadata is found in HTTP Live Streaming (HLS) input, it will be passed through to HLS output.
    SegmentDurationSeconds (integer) -- Duration (in seconds) of each fragment. Actual fragments will be rounded to the nearest multiple of the source fragment duration.
    StreamSelection (dict) -- A StreamSelection configuration.
    MaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.
    MinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.
    StreamOrder (string) -- A directive that determines the order of streams in the output.
    
    
    UseAudioRenditionGroup (boolean) -- When enabled, audio streams will be placed in rendition groups in the output.
    
    
    Id (string) -- The ID of the OriginEndpoint.
    ManifestName (string) -- A short string appended to the end of the OriginEndpoint URL.
    MssPackage (dict) -- A Microsoft Smooth Streaming (MSS) packaging configuration.
    Encryption (dict) -- A Microsoft Smooth Streaming (MSS) encryption configuration.
    SpekeKeyProvider (dict) -- A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
    CertificateArn (string) -- An Amazon Resource Name (ARN) of a Certificate Manager certificate that MediaPackage will use for enforcing secure end-to-end data transfer with the key provider service.
    ResourceId (string) -- The resource ID to include in key requests.
    RoleArn (string) -- An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.
    SystemIds (list) -- The system IDs to include in key requests.
    (string) --
    
    
    Url (string) -- The URL of the external key provider service.
    
    
    
    
    ManifestWindowSeconds (integer) -- The time window (in seconds) contained in each manifest.
    SegmentDurationSeconds (integer) -- The duration (in seconds) of each segment.
    StreamSelection (dict) -- A StreamSelection configuration.
    MaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.
    MinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.
    StreamOrder (string) -- A directive that determines the order of streams in the output.
    
    
    
    
    Origination (string) -- Control whether origination of video is allowed for this OriginEndpoint. If set to ALLOW, the OriginEndpoint may by requested, pursuant to any other form of access control. If set to DENY, the OriginEndpoint may not be requested. This can be helpful for Live to VOD harvesting, or for temporarily disabling origination
    StartoverWindowSeconds (integer) -- Maximum duration (seconds) of content to retain for startover playback. If not specified, startover playback will be disabled for the OriginEndpoint.
    Tags (dict) -- A collection of tags associated with a resource
    (string) --
    (string) --
    
    
    
    
    TimeDelaySeconds (integer) -- Amount of delay (seconds) to enforce on the playback of live content. If not specified, there will be no time delay in effect for the OriginEndpoint.
    Url (string) -- The URL of the packaged OriginEndpoint for consumption.
    Whitelist (list) -- A list of source IP CIDR blocks that will be allowed to access the OriginEndpoint.
    (string) --
    
    
    
    
    
    """
    pass

