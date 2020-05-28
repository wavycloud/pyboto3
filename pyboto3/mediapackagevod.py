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

def create_asset(Id=None, PackagingGroupId=None, ResourceId=None, SourceArn=None, SourceRoleArn=None, Tags=None):
    """
    Creates a new MediaPackage VOD Asset resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_asset(
        Id='string',
        PackagingGroupId='string',
        ResourceId='string',
        SourceArn='string',
        SourceRoleArn='string',
        Tags={
            'string': 'string'
        }
    )
    
    
    :type Id: string
    :param Id: [REQUIRED] The unique identifier for the Asset.

    :type PackagingGroupId: string
    :param PackagingGroupId: [REQUIRED] The ID of the PackagingGroup for the Asset.

    :type ResourceId: string
    :param ResourceId: The resource ID to include in SPEKE key requests.

    :type SourceArn: string
    :param SourceArn: [REQUIRED] ARN of the source object in S3.

    :type SourceRoleArn: string
    :param SourceRoleArn: [REQUIRED] The IAM role ARN used to access the source S3 bucket.

    :type Tags: dict
    :param Tags: A collection of tags associated with a resource\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Arn': 'string',
    'CreatedAt': 'string',
    'EgressEndpoints': [
        {
            'PackagingConfigurationId': 'string',
            'Url': 'string'
        },
    ],
    'Id': 'string',
    'PackagingGroupId': 'string',
    'ResourceId': 'string',
    'SourceArn': 'string',
    'SourceRoleArn': 'string',
    'Tags': {
        'string': 'string'
    }
}


Response Structure

(dict) -- The new MediaPackage VOD Asset resource.
Arn (string) -- The ARN of the Asset.
CreatedAt (string) -- The time the Asset was initially submitted for Ingest.
EgressEndpoints (list) -- The list of egress endpoints available for the Asset.
(dict) -- The endpoint URL used to access an Asset using one PackagingConfiguration.
PackagingConfigurationId (string) -- The ID of the PackagingConfiguration being applied to the Asset.
Url (string) -- The URL of the parent manifest for the repackaged Asset.




Id (string) -- The unique identifier for the Asset.
PackagingGroupId (string) -- The ID of the PackagingGroup for the Asset.
ResourceId (string) -- The resource ID to include in SPEKE key requests.
SourceArn (string) -- ARN of the source object in S3.
SourceRoleArn (string) -- The IAM role_arn used to access the source S3 bucket.
Tags (dict) -- A collection of tags associated with a resource
(string) --
(string) --










Exceptions

MediaPackageVod.Client.exceptions.UnprocessableEntityException
MediaPackageVod.Client.exceptions.InternalServerErrorException
MediaPackageVod.Client.exceptions.ForbiddenException
MediaPackageVod.Client.exceptions.NotFoundException
MediaPackageVod.Client.exceptions.ServiceUnavailableException
MediaPackageVod.Client.exceptions.TooManyRequestsException


    :return: {
        'Arn': 'string',
        'CreatedAt': 'string',
        'EgressEndpoints': [
            {
                'PackagingConfigurationId': 'string',
                'Url': 'string'
            },
        ],
        'Id': 'string',
        'PackagingGroupId': 'string',
        'ResourceId': 'string',
        'SourceArn': 'string',
        'SourceRoleArn': 'string',
        'Tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    (dict) -- The new MediaPackage VOD Asset resource.
    Arn (string) -- The ARN of the Asset.
    CreatedAt (string) -- The time the Asset was initially submitted for Ingest.
    EgressEndpoints (list) -- The list of egress endpoints available for the Asset.
    (dict) -- The endpoint URL used to access an Asset using one PackagingConfiguration.
    PackagingConfigurationId (string) -- The ID of the PackagingConfiguration being applied to the Asset.
    Url (string) -- The URL of the parent manifest for the repackaged Asset.
    
    
    
    
    Id (string) -- The unique identifier for the Asset.
    PackagingGroupId (string) -- The ID of the PackagingGroup for the Asset.
    ResourceId (string) -- The resource ID to include in SPEKE key requests.
    SourceArn (string) -- ARN of the source object in S3.
    SourceRoleArn (string) -- The IAM role_arn used to access the source S3 bucket.
    Tags (dict) -- A collection of tags associated with a resource
    (string) --
    (string) --
    
    
    
    
    
    
    
    """
    pass

def create_packaging_configuration(CmafPackage=None, DashPackage=None, HlsPackage=None, Id=None, MssPackage=None, PackagingGroupId=None, Tags=None):
    """
    Creates a new MediaPackage VOD PackagingConfiguration resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_packaging_configuration(
        CmafPackage={
            'Encryption': {
                'SpekeKeyProvider': {
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
                    'IncludeIframeOnlyStream': True|False,
                    'ManifestName': 'string',
                    'ProgramDateTimeIntervalSeconds': 123,
                    'RepeatExtXKey': True|False,
                    'StreamSelection': {
                        'MaxVideoBitsPerSecond': 123,
                        'MinVideoBitsPerSecond': 123,
                        'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
                    }
                },
            ],
            'SegmentDurationSeconds': 123
        },
        DashPackage={
            'DashManifests': [
                {
                    'ManifestLayout': 'FULL'|'COMPACT',
                    'ManifestName': 'string',
                    'MinBufferTimeSeconds': 123,
                    'Profile': 'NONE'|'HBBTV_1_5',
                    'StreamSelection': {
                        'MaxVideoBitsPerSecond': 123,
                        'MinVideoBitsPerSecond': 123,
                        'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
                    }
                },
            ],
            'Encryption': {
                'SpekeKeyProvider': {
                    'RoleArn': 'string',
                    'SystemIds': [
                        'string',
                    ],
                    'Url': 'string'
                }
            },
            'PeriodTriggers': [
                'ADS',
            ],
            'SegmentDurationSeconds': 123,
            'SegmentTemplateFormat': 'NUMBER_WITH_TIMELINE'|'TIME_WITH_TIMELINE'|'NUMBER_WITH_DURATION'
        },
        HlsPackage={
            'Encryption': {
                'ConstantInitializationVector': 'string',
                'EncryptionMethod': 'AES_128'|'SAMPLE_AES',
                'SpekeKeyProvider': {
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
                    'IncludeIframeOnlyStream': True|False,
                    'ManifestName': 'string',
                    'ProgramDateTimeIntervalSeconds': 123,
                    'RepeatExtXKey': True|False,
                    'StreamSelection': {
                        'MaxVideoBitsPerSecond': 123,
                        'MinVideoBitsPerSecond': 123,
                        'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
                    }
                },
            ],
            'SegmentDurationSeconds': 123,
            'UseAudioRenditionGroup': True|False
        },
        Id='string',
        MssPackage={
            'Encryption': {
                'SpekeKeyProvider': {
                    'RoleArn': 'string',
                    'SystemIds': [
                        'string',
                    ],
                    'Url': 'string'
                }
            },
            'MssManifests': [
                {
                    'ManifestName': 'string',
                    'StreamSelection': {
                        'MaxVideoBitsPerSecond': 123,
                        'MinVideoBitsPerSecond': 123,
                        'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
                    }
                },
            ],
            'SegmentDurationSeconds': 123
        },
        PackagingGroupId='string',
        Tags={
            'string': 'string'
        }
    )
    
    
    :type CmafPackage: dict
    :param CmafPackage: A CMAF packaging configuration.\n\nEncryption (dict) -- A CMAF encryption configuration.\nSpekeKeyProvider (dict) -- [REQUIRED] A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.\nRoleArn (string) -- [REQUIRED] An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.\nSystemIds (list) -- [REQUIRED] The system IDs to include in key requests.\n(string) --\n\n\nUrl (string) -- [REQUIRED] The URL of the external key provider service.\n\n\n\n\nHlsManifests (list) -- [REQUIRED] A list of HLS manifest configurations.\n(dict) -- An HTTP Live Streaming (HLS) manifest configuration.\nAdMarkers (string) -- This setting controls how ad markers are included in the packaged OriginEndpoint. 'NONE' will omit all SCTE-35 ad markers from the output. 'PASSTHROUGH' causes the manifest to contain a copy of the SCTE-35 ad markers (comments) taken directly from the input HTTP Live Streaming (HLS) manifest. 'SCTE35_ENHANCED' generates ad markers and blackout tags based on SCTE-35 messages in the input source.\nIncludeIframeOnlyStream (boolean) -- When enabled, an I-Frame only stream will be included in the output.\nManifestName (string) -- An optional string to include in the name of the manifest.\nProgramDateTimeIntervalSeconds (integer) -- The interval (in seconds) between each EXT-X-PROGRAM-DATE-TIME tag inserted into manifests. Additionally, when an interval is specified ID3Timed Metadata messages will be generated every 5 seconds using the ingest time of the content. If the interval is not specified, or set to 0, then no EXT-X-PROGRAM-DATE-TIME tags will be inserted into manifests and no ID3Timed Metadata messages will be generated. Note that irrespective of this parameter, if any ID3 Timed Metadata is found in HTTP Live Streaming (HLS) input, it will be passed through to HLS output.\nRepeatExtXKey (boolean) -- When enabled, the EXT-X-KEY tag will be repeated in output manifests.\nStreamSelection (dict) -- A StreamSelection configuration.\nMaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.\nMinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.\nStreamOrder (string) -- A directive that determines the order of streams in the output.\n\n\n\n\n\n\nSegmentDurationSeconds (integer) -- Duration (in seconds) of each fragment. Actual fragments will be rounded to the nearest multiple of the source fragment duration.\n\n

    :type DashPackage: dict
    :param DashPackage: A Dynamic Adaptive Streaming over HTTP (DASH) packaging configuration.\n\nDashManifests (list) -- [REQUIRED] A list of DASH manifest configurations.\n(dict) -- A DASH manifest configuration.\nManifestLayout (string) -- Determines the position of some tags in the Media Presentation Description (MPD). When set to FULL, elements like SegmentTemplate and ContentProtection are included in each Representation. When set to COMPACT, duplicate elements are combined and presented at the AdaptationSet level.\nManifestName (string) -- An optional string to include in the name of the manifest.\nMinBufferTimeSeconds (integer) -- Minimum duration (in seconds) that a player will buffer media before starting the presentation.\nProfile (string) -- The Dynamic Adaptive Streaming over HTTP (DASH) profile type. When set to 'HBBTV_1_5', HbbTV 1.5 compliant output is enabled.\nStreamSelection (dict) -- A StreamSelection configuration.\nMaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.\nMinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.\nStreamOrder (string) -- A directive that determines the order of streams in the output.\n\n\n\n\n\n\nEncryption (dict) -- A Dynamic Adaptive Streaming over HTTP (DASH) encryption configuration.\nSpekeKeyProvider (dict) -- [REQUIRED] A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.\nRoleArn (string) -- [REQUIRED] An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.\nSystemIds (list) -- [REQUIRED] The system IDs to include in key requests.\n(string) --\n\n\nUrl (string) -- [REQUIRED] The URL of the external key provider service.\n\n\n\n\nPeriodTriggers (list) -- A list of triggers that controls when the outgoing Dynamic Adaptive Streaming over HTTP (DASH) Media Presentation Description (MPD) will be partitioned into multiple periods. If empty, the content will not be partitioned into more than one period. If the list contains 'ADS', new periods will be created where the Asset contains SCTE-35 ad markers.\n(string) --\n\n\nSegmentDurationSeconds (integer) -- Duration (in seconds) of each segment. Actual segments will be rounded to the nearest multiple of the source segment duration.\nSegmentTemplateFormat (string) -- Determines the type of SegmentTemplate included in the Media Presentation Description (MPD). When set to NUMBER_WITH_TIMELINE, a full timeline is presented in each SegmentTemplate, with $Number$ media URLs. When set to TIME_WITH_TIMELINE, a full timeline is presented in each SegmentTemplate, with $Time$ media URLs. When set to NUMBER_WITH_DURATION, only a duration is included in each SegmentTemplate, with $Number$ media URLs.\n\n

    :type HlsPackage: dict
    :param HlsPackage: An HTTP Live Streaming (HLS) packaging configuration.\n\nEncryption (dict) -- An HTTP Live Streaming (HLS) encryption configuration.\nConstantInitializationVector (string) -- A constant initialization vector for encryption (optional). When not specified the initialization vector will be periodically rotated.\nEncryptionMethod (string) -- The encryption method to use.\nSpekeKeyProvider (dict) -- [REQUIRED] A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.\nRoleArn (string) -- [REQUIRED] An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.\nSystemIds (list) -- [REQUIRED] The system IDs to include in key requests.\n(string) --\n\n\nUrl (string) -- [REQUIRED] The URL of the external key provider service.\n\n\n\n\nHlsManifests (list) -- [REQUIRED] A list of HLS manifest configurations.\n(dict) -- An HTTP Live Streaming (HLS) manifest configuration.\nAdMarkers (string) -- This setting controls how ad markers are included in the packaged OriginEndpoint. 'NONE' will omit all SCTE-35 ad markers from the output. 'PASSTHROUGH' causes the manifest to contain a copy of the SCTE-35 ad markers (comments) taken directly from the input HTTP Live Streaming (HLS) manifest. 'SCTE35_ENHANCED' generates ad markers and blackout tags based on SCTE-35 messages in the input source.\nIncludeIframeOnlyStream (boolean) -- When enabled, an I-Frame only stream will be included in the output.\nManifestName (string) -- An optional string to include in the name of the manifest.\nProgramDateTimeIntervalSeconds (integer) -- The interval (in seconds) between each EXT-X-PROGRAM-DATE-TIME tag inserted into manifests. Additionally, when an interval is specified ID3Timed Metadata messages will be generated every 5 seconds using the ingest time of the content. If the interval is not specified, or set to 0, then no EXT-X-PROGRAM-DATE-TIME tags will be inserted into manifests and no ID3Timed Metadata messages will be generated. Note that irrespective of this parameter, if any ID3 Timed Metadata is found in HTTP Live Streaming (HLS) input, it will be passed through to HLS output.\nRepeatExtXKey (boolean) -- When enabled, the EXT-X-KEY tag will be repeated in output manifests.\nStreamSelection (dict) -- A StreamSelection configuration.\nMaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.\nMinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.\nStreamOrder (string) -- A directive that determines the order of streams in the output.\n\n\n\n\n\n\nSegmentDurationSeconds (integer) -- Duration (in seconds) of each fragment. Actual fragments will be rounded to the nearest multiple of the source fragment duration.\nUseAudioRenditionGroup (boolean) -- When enabled, audio streams will be placed in rendition groups in the output.\n\n

    :type Id: string
    :param Id: [REQUIRED] The ID of the PackagingConfiguration.

    :type MssPackage: dict
    :param MssPackage: A Microsoft Smooth Streaming (MSS) PackagingConfiguration.\n\nEncryption (dict) -- A Microsoft Smooth Streaming (MSS) encryption configuration.\nSpekeKeyProvider (dict) -- [REQUIRED] A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.\nRoleArn (string) -- [REQUIRED] An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.\nSystemIds (list) -- [REQUIRED] The system IDs to include in key requests.\n(string) --\n\n\nUrl (string) -- [REQUIRED] The URL of the external key provider service.\n\n\n\n\nMssManifests (list) -- [REQUIRED] A list of MSS manifest configurations.\n(dict) -- A Microsoft Smooth Streaming (MSS) manifest configuration.\nManifestName (string) -- An optional string to include in the name of the manifest.\nStreamSelection (dict) -- A StreamSelection configuration.\nMaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.\nMinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.\nStreamOrder (string) -- A directive that determines the order of streams in the output.\n\n\n\n\n\n\nSegmentDurationSeconds (integer) -- The duration (in seconds) of each segment.\n\n

    :type PackagingGroupId: string
    :param PackagingGroupId: [REQUIRED] The ID of a PackagingGroup.

    :type Tags: dict
    :param Tags: A collection of tags associated with a resource\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Arn': 'string',
    'CmafPackage': {
        'Encryption': {
            'SpekeKeyProvider': {
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
                'IncludeIframeOnlyStream': True|False,
                'ManifestName': 'string',
                'ProgramDateTimeIntervalSeconds': 123,
                'RepeatExtXKey': True|False,
                'StreamSelection': {
                    'MaxVideoBitsPerSecond': 123,
                    'MinVideoBitsPerSecond': 123,
                    'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
                }
            },
        ],
        'SegmentDurationSeconds': 123
    },
    'DashPackage': {
        'DashManifests': [
            {
                'ManifestLayout': 'FULL'|'COMPACT',
                'ManifestName': 'string',
                'MinBufferTimeSeconds': 123,
                'Profile': 'NONE'|'HBBTV_1_5',
                'StreamSelection': {
                    'MaxVideoBitsPerSecond': 123,
                    'MinVideoBitsPerSecond': 123,
                    'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
                }
            },
        ],
        'Encryption': {
            'SpekeKeyProvider': {
                'RoleArn': 'string',
                'SystemIds': [
                    'string',
                ],
                'Url': 'string'
            }
        },
        'PeriodTriggers': [
            'ADS',
        ],
        'SegmentDurationSeconds': 123,
        'SegmentTemplateFormat': 'NUMBER_WITH_TIMELINE'|'TIME_WITH_TIMELINE'|'NUMBER_WITH_DURATION'
    },
    'HlsPackage': {
        'Encryption': {
            'ConstantInitializationVector': 'string',
            'EncryptionMethod': 'AES_128'|'SAMPLE_AES',
            'SpekeKeyProvider': {
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
                'IncludeIframeOnlyStream': True|False,
                'ManifestName': 'string',
                'ProgramDateTimeIntervalSeconds': 123,
                'RepeatExtXKey': True|False,
                'StreamSelection': {
                    'MaxVideoBitsPerSecond': 123,
                    'MinVideoBitsPerSecond': 123,
                    'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
                }
            },
        ],
        'SegmentDurationSeconds': 123,
        'UseAudioRenditionGroup': True|False
    },
    'Id': 'string',
    'MssPackage': {
        'Encryption': {
            'SpekeKeyProvider': {
                'RoleArn': 'string',
                'SystemIds': [
                    'string',
                ],
                'Url': 'string'
            }
        },
        'MssManifests': [
            {
                'ManifestName': 'string',
                'StreamSelection': {
                    'MaxVideoBitsPerSecond': 123,
                    'MinVideoBitsPerSecond': 123,
                    'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
                }
            },
        ],
        'SegmentDurationSeconds': 123
    },
    'PackagingGroupId': 'string',
    'Tags': {
        'string': 'string'
    }
}


Response Structure

(dict) -- The new MediaPackage VOD PackagingConfiguration resource.
Arn (string) -- The ARN of the PackagingConfiguration.
CmafPackage (dict) -- A CMAF packaging configuration.
Encryption (dict) -- A CMAF encryption configuration.
SpekeKeyProvider (dict) -- A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
RoleArn (string) -- An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.
SystemIds (list) -- The system IDs to include in key requests.
(string) --


Url (string) -- The URL of the external key provider service.




HlsManifests (list) -- A list of HLS manifest configurations.
(dict) -- An HTTP Live Streaming (HLS) manifest configuration.
AdMarkers (string) -- This setting controls how ad markers are included in the packaged OriginEndpoint. "NONE" will omit all SCTE-35 ad markers from the output. "PASSTHROUGH" causes the manifest to contain a copy of the SCTE-35 ad markers (comments) taken directly from the input HTTP Live Streaming (HLS) manifest. "SCTE35_ENHANCED" generates ad markers and blackout tags based on SCTE-35 messages in the input source.
IncludeIframeOnlyStream (boolean) -- When enabled, an I-Frame only stream will be included in the output.
ManifestName (string) -- An optional string to include in the name of the manifest.
ProgramDateTimeIntervalSeconds (integer) -- The interval (in seconds) between each EXT-X-PROGRAM-DATE-TIME tag inserted into manifests. Additionally, when an interval is specified ID3Timed Metadata messages will be generated every 5 seconds using the ingest time of the content. If the interval is not specified, or set to 0, then no EXT-X-PROGRAM-DATE-TIME tags will be inserted into manifests and no ID3Timed Metadata messages will be generated. Note that irrespective of this parameter, if any ID3 Timed Metadata is found in HTTP Live Streaming (HLS) input, it will be passed through to HLS output.
RepeatExtXKey (boolean) -- When enabled, the EXT-X-KEY tag will be repeated in output manifests.
StreamSelection (dict) -- A StreamSelection configuration.
MaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.
MinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.
StreamOrder (string) -- A directive that determines the order of streams in the output.






SegmentDurationSeconds (integer) -- Duration (in seconds) of each fragment. Actual fragments will be rounded to the nearest multiple of the source fragment duration.


DashPackage (dict) -- A Dynamic Adaptive Streaming over HTTP (DASH) packaging configuration.
DashManifests (list) -- A list of DASH manifest configurations.
(dict) -- A DASH manifest configuration.
ManifestLayout (string) -- Determines the position of some tags in the Media Presentation Description (MPD). When set to FULL, elements like SegmentTemplate and ContentProtection are included in each Representation. When set to COMPACT, duplicate elements are combined and presented at the AdaptationSet level.
ManifestName (string) -- An optional string to include in the name of the manifest.
MinBufferTimeSeconds (integer) -- Minimum duration (in seconds) that a player will buffer media before starting the presentation.
Profile (string) -- The Dynamic Adaptive Streaming over HTTP (DASH) profile type. When set to "HBBTV_1_5", HbbTV 1.5 compliant output is enabled.
StreamSelection (dict) -- A StreamSelection configuration.
MaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.
MinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.
StreamOrder (string) -- A directive that determines the order of streams in the output.






Encryption (dict) -- A Dynamic Adaptive Streaming over HTTP (DASH) encryption configuration.
SpekeKeyProvider (dict) -- A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
RoleArn (string) -- An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.
SystemIds (list) -- The system IDs to include in key requests.
(string) --


Url (string) -- The URL of the external key provider service.




PeriodTriggers (list) -- A list of triggers that controls when the outgoing Dynamic Adaptive Streaming over HTTP (DASH) Media Presentation Description (MPD) will be partitioned into multiple periods. If empty, the content will not be partitioned into more than one period. If the list contains "ADS", new periods will be created where the Asset contains SCTE-35 ad markers.
(string) --


SegmentDurationSeconds (integer) -- Duration (in seconds) of each segment. Actual segments will be rounded to the nearest multiple of the source segment duration.
SegmentTemplateFormat (string) -- Determines the type of SegmentTemplate included in the Media Presentation Description (MPD). When set to NUMBER_WITH_TIMELINE, a full timeline is presented in each SegmentTemplate, with $Number$ media URLs. When set to TIME_WITH_TIMELINE, a full timeline is presented in each SegmentTemplate, with $Time$ media URLs. When set to NUMBER_WITH_DURATION, only a duration is included in each SegmentTemplate, with $Number$ media URLs.


HlsPackage (dict) -- An HTTP Live Streaming (HLS) packaging configuration.
Encryption (dict) -- An HTTP Live Streaming (HLS) encryption configuration.
ConstantInitializationVector (string) -- A constant initialization vector for encryption (optional). When not specified the initialization vector will be periodically rotated.
EncryptionMethod (string) -- The encryption method to use.
SpekeKeyProvider (dict) -- A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
RoleArn (string) -- An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.
SystemIds (list) -- The system IDs to include in key requests.
(string) --


Url (string) -- The URL of the external key provider service.




HlsManifests (list) -- A list of HLS manifest configurations.
(dict) -- An HTTP Live Streaming (HLS) manifest configuration.
AdMarkers (string) -- This setting controls how ad markers are included in the packaged OriginEndpoint. "NONE" will omit all SCTE-35 ad markers from the output. "PASSTHROUGH" causes the manifest to contain a copy of the SCTE-35 ad markers (comments) taken directly from the input HTTP Live Streaming (HLS) manifest. "SCTE35_ENHANCED" generates ad markers and blackout tags based on SCTE-35 messages in the input source.
IncludeIframeOnlyStream (boolean) -- When enabled, an I-Frame only stream will be included in the output.
ManifestName (string) -- An optional string to include in the name of the manifest.
ProgramDateTimeIntervalSeconds (integer) -- The interval (in seconds) between each EXT-X-PROGRAM-DATE-TIME tag inserted into manifests. Additionally, when an interval is specified ID3Timed Metadata messages will be generated every 5 seconds using the ingest time of the content. If the interval is not specified, or set to 0, then no EXT-X-PROGRAM-DATE-TIME tags will be inserted into manifests and no ID3Timed Metadata messages will be generated. Note that irrespective of this parameter, if any ID3 Timed Metadata is found in HTTP Live Streaming (HLS) input, it will be passed through to HLS output.
RepeatExtXKey (boolean) -- When enabled, the EXT-X-KEY tag will be repeated in output manifests.
StreamSelection (dict) -- A StreamSelection configuration.
MaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.
MinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.
StreamOrder (string) -- A directive that determines the order of streams in the output.






SegmentDurationSeconds (integer) -- Duration (in seconds) of each fragment. Actual fragments will be rounded to the nearest multiple of the source fragment duration.
UseAudioRenditionGroup (boolean) -- When enabled, audio streams will be placed in rendition groups in the output.


Id (string) -- The ID of the PackagingConfiguration.
MssPackage (dict) -- A Microsoft Smooth Streaming (MSS) PackagingConfiguration.
Encryption (dict) -- A Microsoft Smooth Streaming (MSS) encryption configuration.
SpekeKeyProvider (dict) -- A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
RoleArn (string) -- An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.
SystemIds (list) -- The system IDs to include in key requests.
(string) --


Url (string) -- The URL of the external key provider service.




MssManifests (list) -- A list of MSS manifest configurations.
(dict) -- A Microsoft Smooth Streaming (MSS) manifest configuration.
ManifestName (string) -- An optional string to include in the name of the manifest.
StreamSelection (dict) -- A StreamSelection configuration.
MaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.
MinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.
StreamOrder (string) -- A directive that determines the order of streams in the output.






SegmentDurationSeconds (integer) -- The duration (in seconds) of each segment.


PackagingGroupId (string) -- The ID of a PackagingGroup.
Tags (dict) -- A collection of tags associated with a resource
(string) --
(string) --










Exceptions

MediaPackageVod.Client.exceptions.UnprocessableEntityException
MediaPackageVod.Client.exceptions.InternalServerErrorException
MediaPackageVod.Client.exceptions.ForbiddenException
MediaPackageVod.Client.exceptions.NotFoundException
MediaPackageVod.Client.exceptions.ServiceUnavailableException
MediaPackageVod.Client.exceptions.TooManyRequestsException


    :return: {
        'Arn': 'string',
        'CmafPackage': {
            'Encryption': {
                'SpekeKeyProvider': {
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
                    'IncludeIframeOnlyStream': True|False,
                    'ManifestName': 'string',
                    'ProgramDateTimeIntervalSeconds': 123,
                    'RepeatExtXKey': True|False,
                    'StreamSelection': {
                        'MaxVideoBitsPerSecond': 123,
                        'MinVideoBitsPerSecond': 123,
                        'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
                    }
                },
            ],
            'SegmentDurationSeconds': 123
        },
        'DashPackage': {
            'DashManifests': [
                {
                    'ManifestLayout': 'FULL'|'COMPACT',
                    'ManifestName': 'string',
                    'MinBufferTimeSeconds': 123,
                    'Profile': 'NONE'|'HBBTV_1_5',
                    'StreamSelection': {
                        'MaxVideoBitsPerSecond': 123,
                        'MinVideoBitsPerSecond': 123,
                        'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
                    }
                },
            ],
            'Encryption': {
                'SpekeKeyProvider': {
                    'RoleArn': 'string',
                    'SystemIds': [
                        'string',
                    ],
                    'Url': 'string'
                }
            },
            'PeriodTriggers': [
                'ADS',
            ],
            'SegmentDurationSeconds': 123,
            'SegmentTemplateFormat': 'NUMBER_WITH_TIMELINE'|'TIME_WITH_TIMELINE'|'NUMBER_WITH_DURATION'
        },
        'HlsPackage': {
            'Encryption': {
                'ConstantInitializationVector': 'string',
                'EncryptionMethod': 'AES_128'|'SAMPLE_AES',
                'SpekeKeyProvider': {
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
                    'IncludeIframeOnlyStream': True|False,
                    'ManifestName': 'string',
                    'ProgramDateTimeIntervalSeconds': 123,
                    'RepeatExtXKey': True|False,
                    'StreamSelection': {
                        'MaxVideoBitsPerSecond': 123,
                        'MinVideoBitsPerSecond': 123,
                        'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
                    }
                },
            ],
            'SegmentDurationSeconds': 123,
            'UseAudioRenditionGroup': True|False
        },
        'Id': 'string',
        'MssPackage': {
            'Encryption': {
                'SpekeKeyProvider': {
                    'RoleArn': 'string',
                    'SystemIds': [
                        'string',
                    ],
                    'Url': 'string'
                }
            },
            'MssManifests': [
                {
                    'ManifestName': 'string',
                    'StreamSelection': {
                        'MaxVideoBitsPerSecond': 123,
                        'MinVideoBitsPerSecond': 123,
                        'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
                    }
                },
            ],
            'SegmentDurationSeconds': 123
        },
        'PackagingGroupId': 'string',
        'Tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    (dict) -- The new MediaPackage VOD PackagingConfiguration resource.
    Arn (string) -- The ARN of the PackagingConfiguration.
    CmafPackage (dict) -- A CMAF packaging configuration.
    Encryption (dict) -- A CMAF encryption configuration.
    SpekeKeyProvider (dict) -- A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
    RoleArn (string) -- An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.
    SystemIds (list) -- The system IDs to include in key requests.
    (string) --
    
    
    Url (string) -- The URL of the external key provider service.
    
    
    
    
    HlsManifests (list) -- A list of HLS manifest configurations.
    (dict) -- An HTTP Live Streaming (HLS) manifest configuration.
    AdMarkers (string) -- This setting controls how ad markers are included in the packaged OriginEndpoint. "NONE" will omit all SCTE-35 ad markers from the output. "PASSTHROUGH" causes the manifest to contain a copy of the SCTE-35 ad markers (comments) taken directly from the input HTTP Live Streaming (HLS) manifest. "SCTE35_ENHANCED" generates ad markers and blackout tags based on SCTE-35 messages in the input source.
    IncludeIframeOnlyStream (boolean) -- When enabled, an I-Frame only stream will be included in the output.
    ManifestName (string) -- An optional string to include in the name of the manifest.
    ProgramDateTimeIntervalSeconds (integer) -- The interval (in seconds) between each EXT-X-PROGRAM-DATE-TIME tag inserted into manifests. Additionally, when an interval is specified ID3Timed Metadata messages will be generated every 5 seconds using the ingest time of the content. If the interval is not specified, or set to 0, then no EXT-X-PROGRAM-DATE-TIME tags will be inserted into manifests and no ID3Timed Metadata messages will be generated. Note that irrespective of this parameter, if any ID3 Timed Metadata is found in HTTP Live Streaming (HLS) input, it will be passed through to HLS output.
    RepeatExtXKey (boolean) -- When enabled, the EXT-X-KEY tag will be repeated in output manifests.
    StreamSelection (dict) -- A StreamSelection configuration.
    MaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.
    MinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.
    StreamOrder (string) -- A directive that determines the order of streams in the output.
    
    
    
    
    
    
    SegmentDurationSeconds (integer) -- Duration (in seconds) of each fragment. Actual fragments will be rounded to the nearest multiple of the source fragment duration.
    
    
    DashPackage (dict) -- A Dynamic Adaptive Streaming over HTTP (DASH) packaging configuration.
    DashManifests (list) -- A list of DASH manifest configurations.
    (dict) -- A DASH manifest configuration.
    ManifestLayout (string) -- Determines the position of some tags in the Media Presentation Description (MPD). When set to FULL, elements like SegmentTemplate and ContentProtection are included in each Representation. When set to COMPACT, duplicate elements are combined and presented at the AdaptationSet level.
    ManifestName (string) -- An optional string to include in the name of the manifest.
    MinBufferTimeSeconds (integer) -- Minimum duration (in seconds) that a player will buffer media before starting the presentation.
    Profile (string) -- The Dynamic Adaptive Streaming over HTTP (DASH) profile type. When set to "HBBTV_1_5", HbbTV 1.5 compliant output is enabled.
    StreamSelection (dict) -- A StreamSelection configuration.
    MaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.
    MinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.
    StreamOrder (string) -- A directive that determines the order of streams in the output.
    
    
    
    
    
    
    Encryption (dict) -- A Dynamic Adaptive Streaming over HTTP (DASH) encryption configuration.
    SpekeKeyProvider (dict) -- A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
    RoleArn (string) -- An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.
    SystemIds (list) -- The system IDs to include in key requests.
    (string) --
    
    
    Url (string) -- The URL of the external key provider service.
    
    
    
    
    PeriodTriggers (list) -- A list of triggers that controls when the outgoing Dynamic Adaptive Streaming over HTTP (DASH) Media Presentation Description (MPD) will be partitioned into multiple periods. If empty, the content will not be partitioned into more than one period. If the list contains "ADS", new periods will be created where the Asset contains SCTE-35 ad markers.
    (string) --
    
    
    SegmentDurationSeconds (integer) -- Duration (in seconds) of each segment. Actual segments will be rounded to the nearest multiple of the source segment duration.
    SegmentTemplateFormat (string) -- Determines the type of SegmentTemplate included in the Media Presentation Description (MPD). When set to NUMBER_WITH_TIMELINE, a full timeline is presented in each SegmentTemplate, with $Number$ media URLs. When set to TIME_WITH_TIMELINE, a full timeline is presented in each SegmentTemplate, with $Time$ media URLs. When set to NUMBER_WITH_DURATION, only a duration is included in each SegmentTemplate, with $Number$ media URLs.
    
    
    HlsPackage (dict) -- An HTTP Live Streaming (HLS) packaging configuration.
    Encryption (dict) -- An HTTP Live Streaming (HLS) encryption configuration.
    ConstantInitializationVector (string) -- A constant initialization vector for encryption (optional). When not specified the initialization vector will be periodically rotated.
    EncryptionMethod (string) -- The encryption method to use.
    SpekeKeyProvider (dict) -- A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
    RoleArn (string) -- An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.
    SystemIds (list) -- The system IDs to include in key requests.
    (string) --
    
    
    Url (string) -- The URL of the external key provider service.
    
    
    
    
    HlsManifests (list) -- A list of HLS manifest configurations.
    (dict) -- An HTTP Live Streaming (HLS) manifest configuration.
    AdMarkers (string) -- This setting controls how ad markers are included in the packaged OriginEndpoint. "NONE" will omit all SCTE-35 ad markers from the output. "PASSTHROUGH" causes the manifest to contain a copy of the SCTE-35 ad markers (comments) taken directly from the input HTTP Live Streaming (HLS) manifest. "SCTE35_ENHANCED" generates ad markers and blackout tags based on SCTE-35 messages in the input source.
    IncludeIframeOnlyStream (boolean) -- When enabled, an I-Frame only stream will be included in the output.
    ManifestName (string) -- An optional string to include in the name of the manifest.
    ProgramDateTimeIntervalSeconds (integer) -- The interval (in seconds) between each EXT-X-PROGRAM-DATE-TIME tag inserted into manifests. Additionally, when an interval is specified ID3Timed Metadata messages will be generated every 5 seconds using the ingest time of the content. If the interval is not specified, or set to 0, then no EXT-X-PROGRAM-DATE-TIME tags will be inserted into manifests and no ID3Timed Metadata messages will be generated. Note that irrespective of this parameter, if any ID3 Timed Metadata is found in HTTP Live Streaming (HLS) input, it will be passed through to HLS output.
    RepeatExtXKey (boolean) -- When enabled, the EXT-X-KEY tag will be repeated in output manifests.
    StreamSelection (dict) -- A StreamSelection configuration.
    MaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.
    MinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.
    StreamOrder (string) -- A directive that determines the order of streams in the output.
    
    
    
    
    
    
    SegmentDurationSeconds (integer) -- Duration (in seconds) of each fragment. Actual fragments will be rounded to the nearest multiple of the source fragment duration.
    UseAudioRenditionGroup (boolean) -- When enabled, audio streams will be placed in rendition groups in the output.
    
    
    Id (string) -- The ID of the PackagingConfiguration.
    MssPackage (dict) -- A Microsoft Smooth Streaming (MSS) PackagingConfiguration.
    Encryption (dict) -- A Microsoft Smooth Streaming (MSS) encryption configuration.
    SpekeKeyProvider (dict) -- A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
    RoleArn (string) -- An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.
    SystemIds (list) -- The system IDs to include in key requests.
    (string) --
    
    
    Url (string) -- The URL of the external key provider service.
    
    
    
    
    MssManifests (list) -- A list of MSS manifest configurations.
    (dict) -- A Microsoft Smooth Streaming (MSS) manifest configuration.
    ManifestName (string) -- An optional string to include in the name of the manifest.
    StreamSelection (dict) -- A StreamSelection configuration.
    MaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.
    MinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.
    StreamOrder (string) -- A directive that determines the order of streams in the output.
    
    
    
    
    
    
    SegmentDurationSeconds (integer) -- The duration (in seconds) of each segment.
    
    
    PackagingGroupId (string) -- The ID of a PackagingGroup.
    Tags (dict) -- A collection of tags associated with a resource
    (string) --
    (string) --
    
    
    
    
    
    
    
    """
    pass

def create_packaging_group(Id=None, Tags=None):
    """
    Creates a new MediaPackage VOD PackagingGroup resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_packaging_group(
        Id='string',
        Tags={
            'string': 'string'
        }
    )
    
    
    :type Id: string
    :param Id: [REQUIRED] The ID of the PackagingGroup.

    :type Tags: dict
    :param Tags: A collection of tags associated with a resource\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Arn': 'string',
    'DomainName': 'string',
    'Id': 'string',
    'Tags': {
        'string': 'string'
    }
}


Response Structure

(dict) -- The new MediaPackage VOD PackagingGroup resource.
Arn (string) -- The ARN of the PackagingGroup.
DomainName (string) -- The fully qualified domain name for Assets in the PackagingGroup.
Id (string) -- The ID of the PackagingGroup.
Tags (dict) -- A collection of tags associated with a resource
(string) --
(string) --










Exceptions

MediaPackageVod.Client.exceptions.UnprocessableEntityException
MediaPackageVod.Client.exceptions.InternalServerErrorException
MediaPackageVod.Client.exceptions.ForbiddenException
MediaPackageVod.Client.exceptions.NotFoundException
MediaPackageVod.Client.exceptions.ServiceUnavailableException
MediaPackageVod.Client.exceptions.TooManyRequestsException


    :return: {
        'Arn': 'string',
        'DomainName': 'string',
        'Id': 'string',
        'Tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    (dict) -- The new MediaPackage VOD PackagingGroup resource.
    Arn (string) -- The ARN of the PackagingGroup.
    DomainName (string) -- The fully qualified domain name for Assets in the PackagingGroup.
    Id (string) -- The ID of the PackagingGroup.
    Tags (dict) -- A collection of tags associated with a resource
    (string) --
    (string) --
    
    
    
    
    
    
    
    """
    pass

def delete_asset(Id=None):
    """
    Deletes an existing MediaPackage VOD Asset resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_asset(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED] The ID of the MediaPackage VOD Asset resource to delete.

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) -- The MediaPackage VOD Asset resource has been deleted.



Exceptions

MediaPackageVod.Client.exceptions.UnprocessableEntityException
MediaPackageVod.Client.exceptions.InternalServerErrorException
MediaPackageVod.Client.exceptions.ForbiddenException
MediaPackageVod.Client.exceptions.NotFoundException
MediaPackageVod.Client.exceptions.ServiceUnavailableException
MediaPackageVod.Client.exceptions.TooManyRequestsException


    :return: {}
    
    
    :returns: 
    MediaPackageVod.Client.exceptions.UnprocessableEntityException
    MediaPackageVod.Client.exceptions.InternalServerErrorException
    MediaPackageVod.Client.exceptions.ForbiddenException
    MediaPackageVod.Client.exceptions.NotFoundException
    MediaPackageVod.Client.exceptions.ServiceUnavailableException
    MediaPackageVod.Client.exceptions.TooManyRequestsException
    
    """
    pass

def delete_packaging_configuration(Id=None):
    """
    Deletes a MediaPackage VOD PackagingConfiguration resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_packaging_configuration(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED] The ID of the MediaPackage VOD PackagingConfiguration resource to delete.

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) -- The MediaPackage VOD PackagingConfiguration resource has been deleted.



Exceptions

MediaPackageVod.Client.exceptions.UnprocessableEntityException
MediaPackageVod.Client.exceptions.InternalServerErrorException
MediaPackageVod.Client.exceptions.ForbiddenException
MediaPackageVod.Client.exceptions.NotFoundException
MediaPackageVod.Client.exceptions.ServiceUnavailableException
MediaPackageVod.Client.exceptions.TooManyRequestsException


    :return: {}
    
    
    :returns: 
    MediaPackageVod.Client.exceptions.UnprocessableEntityException
    MediaPackageVod.Client.exceptions.InternalServerErrorException
    MediaPackageVod.Client.exceptions.ForbiddenException
    MediaPackageVod.Client.exceptions.NotFoundException
    MediaPackageVod.Client.exceptions.ServiceUnavailableException
    MediaPackageVod.Client.exceptions.TooManyRequestsException
    
    """
    pass

def delete_packaging_group(Id=None):
    """
    Deletes a MediaPackage VOD PackagingGroup resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_packaging_group(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED] The ID of the MediaPackage VOD PackagingGroup resource to delete.

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) -- The MediaPackage VOD PackagingGroup resource has been deleted.



Exceptions

MediaPackageVod.Client.exceptions.UnprocessableEntityException
MediaPackageVod.Client.exceptions.InternalServerErrorException
MediaPackageVod.Client.exceptions.ForbiddenException
MediaPackageVod.Client.exceptions.NotFoundException
MediaPackageVod.Client.exceptions.ServiceUnavailableException
MediaPackageVod.Client.exceptions.TooManyRequestsException


    :return: {}
    
    
    :returns: 
    MediaPackageVod.Client.exceptions.UnprocessableEntityException
    MediaPackageVod.Client.exceptions.InternalServerErrorException
    MediaPackageVod.Client.exceptions.ForbiddenException
    MediaPackageVod.Client.exceptions.NotFoundException
    MediaPackageVod.Client.exceptions.ServiceUnavailableException
    MediaPackageVod.Client.exceptions.TooManyRequestsException
    
    """
    pass

def describe_asset(Id=None):
    """
    Returns a description of a MediaPackage VOD Asset resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_asset(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED] The ID of an MediaPackage VOD Asset resource.

    :rtype: dict
ReturnsResponse Syntax{
    'Arn': 'string',
    'CreatedAt': 'string',
    'EgressEndpoints': [
        {
            'PackagingConfigurationId': 'string',
            'Url': 'string'
        },
    ],
    'Id': 'string',
    'PackagingGroupId': 'string',
    'ResourceId': 'string',
    'SourceArn': 'string',
    'SourceRoleArn': 'string',
    'Tags': {
        'string': 'string'
    }
}


Response Structure

(dict) -- A MediaPackage VOD Asset resource.
Arn (string) -- The ARN of the Asset.
CreatedAt (string) -- The time the Asset was initially submitted for Ingest.
EgressEndpoints (list) -- The list of egress endpoints available for the Asset.
(dict) -- The endpoint URL used to access an Asset using one PackagingConfiguration.
PackagingConfigurationId (string) -- The ID of the PackagingConfiguration being applied to the Asset.
Url (string) -- The URL of the parent manifest for the repackaged Asset.




Id (string) -- The unique identifier for the Asset.
PackagingGroupId (string) -- The ID of the PackagingGroup for the Asset.
ResourceId (string) -- The resource ID to include in SPEKE key requests.
SourceArn (string) -- ARN of the source object in S3.
SourceRoleArn (string) -- The IAM role_arn used to access the source S3 bucket.
Tags (dict) -- A collection of tags associated with a resource
(string) --
(string) --









Exceptions

MediaPackageVod.Client.exceptions.UnprocessableEntityException
MediaPackageVod.Client.exceptions.InternalServerErrorException
MediaPackageVod.Client.exceptions.ForbiddenException
MediaPackageVod.Client.exceptions.NotFoundException
MediaPackageVod.Client.exceptions.ServiceUnavailableException
MediaPackageVod.Client.exceptions.TooManyRequestsException


    :return: {
        'Arn': 'string',
        'CreatedAt': 'string',
        'EgressEndpoints': [
            {
                'PackagingConfigurationId': 'string',
                'Url': 'string'
            },
        ],
        'Id': 'string',
        'PackagingGroupId': 'string',
        'ResourceId': 'string',
        'SourceArn': 'string',
        'SourceRoleArn': 'string',
        'Tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    MediaPackageVod.Client.exceptions.UnprocessableEntityException
    MediaPackageVod.Client.exceptions.InternalServerErrorException
    MediaPackageVod.Client.exceptions.ForbiddenException
    MediaPackageVod.Client.exceptions.NotFoundException
    MediaPackageVod.Client.exceptions.ServiceUnavailableException
    MediaPackageVod.Client.exceptions.TooManyRequestsException
    
    """
    pass

def describe_packaging_configuration(Id=None):
    """
    Returns a description of a MediaPackage VOD PackagingConfiguration resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_packaging_configuration(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED] The ID of a MediaPackage VOD PackagingConfiguration resource.

    :rtype: dict
ReturnsResponse Syntax{
    'Arn': 'string',
    'CmafPackage': {
        'Encryption': {
            'SpekeKeyProvider': {
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
                'IncludeIframeOnlyStream': True|False,
                'ManifestName': 'string',
                'ProgramDateTimeIntervalSeconds': 123,
                'RepeatExtXKey': True|False,
                'StreamSelection': {
                    'MaxVideoBitsPerSecond': 123,
                    'MinVideoBitsPerSecond': 123,
                    'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
                }
            },
        ],
        'SegmentDurationSeconds': 123
    },
    'DashPackage': {
        'DashManifests': [
            {
                'ManifestLayout': 'FULL'|'COMPACT',
                'ManifestName': 'string',
                'MinBufferTimeSeconds': 123,
                'Profile': 'NONE'|'HBBTV_1_5',
                'StreamSelection': {
                    'MaxVideoBitsPerSecond': 123,
                    'MinVideoBitsPerSecond': 123,
                    'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
                }
            },
        ],
        'Encryption': {
            'SpekeKeyProvider': {
                'RoleArn': 'string',
                'SystemIds': [
                    'string',
                ],
                'Url': 'string'
            }
        },
        'PeriodTriggers': [
            'ADS',
        ],
        'SegmentDurationSeconds': 123,
        'SegmentTemplateFormat': 'NUMBER_WITH_TIMELINE'|'TIME_WITH_TIMELINE'|'NUMBER_WITH_DURATION'
    },
    'HlsPackage': {
        'Encryption': {
            'ConstantInitializationVector': 'string',
            'EncryptionMethod': 'AES_128'|'SAMPLE_AES',
            'SpekeKeyProvider': {
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
                'IncludeIframeOnlyStream': True|False,
                'ManifestName': 'string',
                'ProgramDateTimeIntervalSeconds': 123,
                'RepeatExtXKey': True|False,
                'StreamSelection': {
                    'MaxVideoBitsPerSecond': 123,
                    'MinVideoBitsPerSecond': 123,
                    'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
                }
            },
        ],
        'SegmentDurationSeconds': 123,
        'UseAudioRenditionGroup': True|False
    },
    'Id': 'string',
    'MssPackage': {
        'Encryption': {
            'SpekeKeyProvider': {
                'RoleArn': 'string',
                'SystemIds': [
                    'string',
                ],
                'Url': 'string'
            }
        },
        'MssManifests': [
            {
                'ManifestName': 'string',
                'StreamSelection': {
                    'MaxVideoBitsPerSecond': 123,
                    'MinVideoBitsPerSecond': 123,
                    'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
                }
            },
        ],
        'SegmentDurationSeconds': 123
    },
    'PackagingGroupId': 'string',
    'Tags': {
        'string': 'string'
    }
}


Response Structure

(dict) -- A MediaPackage VOD PackagingConfiguration resource.
Arn (string) -- The ARN of the PackagingConfiguration.
CmafPackage (dict) -- A CMAF packaging configuration.
Encryption (dict) -- A CMAF encryption configuration.
SpekeKeyProvider (dict) -- A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
RoleArn (string) -- An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.
SystemIds (list) -- The system IDs to include in key requests.
(string) --


Url (string) -- The URL of the external key provider service.




HlsManifests (list) -- A list of HLS manifest configurations.
(dict) -- An HTTP Live Streaming (HLS) manifest configuration.
AdMarkers (string) -- This setting controls how ad markers are included in the packaged OriginEndpoint. "NONE" will omit all SCTE-35 ad markers from the output. "PASSTHROUGH" causes the manifest to contain a copy of the SCTE-35 ad markers (comments) taken directly from the input HTTP Live Streaming (HLS) manifest. "SCTE35_ENHANCED" generates ad markers and blackout tags based on SCTE-35 messages in the input source.
IncludeIframeOnlyStream (boolean) -- When enabled, an I-Frame only stream will be included in the output.
ManifestName (string) -- An optional string to include in the name of the manifest.
ProgramDateTimeIntervalSeconds (integer) -- The interval (in seconds) between each EXT-X-PROGRAM-DATE-TIME tag inserted into manifests. Additionally, when an interval is specified ID3Timed Metadata messages will be generated every 5 seconds using the ingest time of the content. If the interval is not specified, or set to 0, then no EXT-X-PROGRAM-DATE-TIME tags will be inserted into manifests and no ID3Timed Metadata messages will be generated. Note that irrespective of this parameter, if any ID3 Timed Metadata is found in HTTP Live Streaming (HLS) input, it will be passed through to HLS output.
RepeatExtXKey (boolean) -- When enabled, the EXT-X-KEY tag will be repeated in output manifests.
StreamSelection (dict) -- A StreamSelection configuration.
MaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.
MinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.
StreamOrder (string) -- A directive that determines the order of streams in the output.






SegmentDurationSeconds (integer) -- Duration (in seconds) of each fragment. Actual fragments will be rounded to the nearest multiple of the source fragment duration.


DashPackage (dict) -- A Dynamic Adaptive Streaming over HTTP (DASH) packaging configuration.
DashManifests (list) -- A list of DASH manifest configurations.
(dict) -- A DASH manifest configuration.
ManifestLayout (string) -- Determines the position of some tags in the Media Presentation Description (MPD). When set to FULL, elements like SegmentTemplate and ContentProtection are included in each Representation. When set to COMPACT, duplicate elements are combined and presented at the AdaptationSet level.
ManifestName (string) -- An optional string to include in the name of the manifest.
MinBufferTimeSeconds (integer) -- Minimum duration (in seconds) that a player will buffer media before starting the presentation.
Profile (string) -- The Dynamic Adaptive Streaming over HTTP (DASH) profile type. When set to "HBBTV_1_5", HbbTV 1.5 compliant output is enabled.
StreamSelection (dict) -- A StreamSelection configuration.
MaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.
MinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.
StreamOrder (string) -- A directive that determines the order of streams in the output.






Encryption (dict) -- A Dynamic Adaptive Streaming over HTTP (DASH) encryption configuration.
SpekeKeyProvider (dict) -- A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
RoleArn (string) -- An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.
SystemIds (list) -- The system IDs to include in key requests.
(string) --


Url (string) -- The URL of the external key provider service.




PeriodTriggers (list) -- A list of triggers that controls when the outgoing Dynamic Adaptive Streaming over HTTP (DASH) Media Presentation Description (MPD) will be partitioned into multiple periods. If empty, the content will not be partitioned into more than one period. If the list contains "ADS", new periods will be created where the Asset contains SCTE-35 ad markers.
(string) --


SegmentDurationSeconds (integer) -- Duration (in seconds) of each segment. Actual segments will be rounded to the nearest multiple of the source segment duration.
SegmentTemplateFormat (string) -- Determines the type of SegmentTemplate included in the Media Presentation Description (MPD). When set to NUMBER_WITH_TIMELINE, a full timeline is presented in each SegmentTemplate, with $Number$ media URLs. When set to TIME_WITH_TIMELINE, a full timeline is presented in each SegmentTemplate, with $Time$ media URLs. When set to NUMBER_WITH_DURATION, only a duration is included in each SegmentTemplate, with $Number$ media URLs.


HlsPackage (dict) -- An HTTP Live Streaming (HLS) packaging configuration.
Encryption (dict) -- An HTTP Live Streaming (HLS) encryption configuration.
ConstantInitializationVector (string) -- A constant initialization vector for encryption (optional). When not specified the initialization vector will be periodically rotated.
EncryptionMethod (string) -- The encryption method to use.
SpekeKeyProvider (dict) -- A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
RoleArn (string) -- An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.
SystemIds (list) -- The system IDs to include in key requests.
(string) --


Url (string) -- The URL of the external key provider service.




HlsManifests (list) -- A list of HLS manifest configurations.
(dict) -- An HTTP Live Streaming (HLS) manifest configuration.
AdMarkers (string) -- This setting controls how ad markers are included in the packaged OriginEndpoint. "NONE" will omit all SCTE-35 ad markers from the output. "PASSTHROUGH" causes the manifest to contain a copy of the SCTE-35 ad markers (comments) taken directly from the input HTTP Live Streaming (HLS) manifest. "SCTE35_ENHANCED" generates ad markers and blackout tags based on SCTE-35 messages in the input source.
IncludeIframeOnlyStream (boolean) -- When enabled, an I-Frame only stream will be included in the output.
ManifestName (string) -- An optional string to include in the name of the manifest.
ProgramDateTimeIntervalSeconds (integer) -- The interval (in seconds) between each EXT-X-PROGRAM-DATE-TIME tag inserted into manifests. Additionally, when an interval is specified ID3Timed Metadata messages will be generated every 5 seconds using the ingest time of the content. If the interval is not specified, or set to 0, then no EXT-X-PROGRAM-DATE-TIME tags will be inserted into manifests and no ID3Timed Metadata messages will be generated. Note that irrespective of this parameter, if any ID3 Timed Metadata is found in HTTP Live Streaming (HLS) input, it will be passed through to HLS output.
RepeatExtXKey (boolean) -- When enabled, the EXT-X-KEY tag will be repeated in output manifests.
StreamSelection (dict) -- A StreamSelection configuration.
MaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.
MinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.
StreamOrder (string) -- A directive that determines the order of streams in the output.






SegmentDurationSeconds (integer) -- Duration (in seconds) of each fragment. Actual fragments will be rounded to the nearest multiple of the source fragment duration.
UseAudioRenditionGroup (boolean) -- When enabled, audio streams will be placed in rendition groups in the output.


Id (string) -- The ID of the PackagingConfiguration.
MssPackage (dict) -- A Microsoft Smooth Streaming (MSS) PackagingConfiguration.
Encryption (dict) -- A Microsoft Smooth Streaming (MSS) encryption configuration.
SpekeKeyProvider (dict) -- A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
RoleArn (string) -- An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.
SystemIds (list) -- The system IDs to include in key requests.
(string) --


Url (string) -- The URL of the external key provider service.




MssManifests (list) -- A list of MSS manifest configurations.
(dict) -- A Microsoft Smooth Streaming (MSS) manifest configuration.
ManifestName (string) -- An optional string to include in the name of the manifest.
StreamSelection (dict) -- A StreamSelection configuration.
MaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.
MinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.
StreamOrder (string) -- A directive that determines the order of streams in the output.






SegmentDurationSeconds (integer) -- The duration (in seconds) of each segment.


PackagingGroupId (string) -- The ID of a PackagingGroup.
Tags (dict) -- A collection of tags associated with a resource
(string) --
(string) --









Exceptions

MediaPackageVod.Client.exceptions.UnprocessableEntityException
MediaPackageVod.Client.exceptions.InternalServerErrorException
MediaPackageVod.Client.exceptions.ForbiddenException
MediaPackageVod.Client.exceptions.NotFoundException
MediaPackageVod.Client.exceptions.ServiceUnavailableException
MediaPackageVod.Client.exceptions.TooManyRequestsException


    :return: {
        'Arn': 'string',
        'CmafPackage': {
            'Encryption': {
                'SpekeKeyProvider': {
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
                    'IncludeIframeOnlyStream': True|False,
                    'ManifestName': 'string',
                    'ProgramDateTimeIntervalSeconds': 123,
                    'RepeatExtXKey': True|False,
                    'StreamSelection': {
                        'MaxVideoBitsPerSecond': 123,
                        'MinVideoBitsPerSecond': 123,
                        'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
                    }
                },
            ],
            'SegmentDurationSeconds': 123
        },
        'DashPackage': {
            'DashManifests': [
                {
                    'ManifestLayout': 'FULL'|'COMPACT',
                    'ManifestName': 'string',
                    'MinBufferTimeSeconds': 123,
                    'Profile': 'NONE'|'HBBTV_1_5',
                    'StreamSelection': {
                        'MaxVideoBitsPerSecond': 123,
                        'MinVideoBitsPerSecond': 123,
                        'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
                    }
                },
            ],
            'Encryption': {
                'SpekeKeyProvider': {
                    'RoleArn': 'string',
                    'SystemIds': [
                        'string',
                    ],
                    'Url': 'string'
                }
            },
            'PeriodTriggers': [
                'ADS',
            ],
            'SegmentDurationSeconds': 123,
            'SegmentTemplateFormat': 'NUMBER_WITH_TIMELINE'|'TIME_WITH_TIMELINE'|'NUMBER_WITH_DURATION'
        },
        'HlsPackage': {
            'Encryption': {
                'ConstantInitializationVector': 'string',
                'EncryptionMethod': 'AES_128'|'SAMPLE_AES',
                'SpekeKeyProvider': {
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
                    'IncludeIframeOnlyStream': True|False,
                    'ManifestName': 'string',
                    'ProgramDateTimeIntervalSeconds': 123,
                    'RepeatExtXKey': True|False,
                    'StreamSelection': {
                        'MaxVideoBitsPerSecond': 123,
                        'MinVideoBitsPerSecond': 123,
                        'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
                    }
                },
            ],
            'SegmentDurationSeconds': 123,
            'UseAudioRenditionGroup': True|False
        },
        'Id': 'string',
        'MssPackage': {
            'Encryption': {
                'SpekeKeyProvider': {
                    'RoleArn': 'string',
                    'SystemIds': [
                        'string',
                    ],
                    'Url': 'string'
                }
            },
            'MssManifests': [
                {
                    'ManifestName': 'string',
                    'StreamSelection': {
                        'MaxVideoBitsPerSecond': 123,
                        'MinVideoBitsPerSecond': 123,
                        'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
                    }
                },
            ],
            'SegmentDurationSeconds': 123
        },
        'PackagingGroupId': 'string',
        'Tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    MediaPackageVod.Client.exceptions.UnprocessableEntityException
    MediaPackageVod.Client.exceptions.InternalServerErrorException
    MediaPackageVod.Client.exceptions.ForbiddenException
    MediaPackageVod.Client.exceptions.NotFoundException
    MediaPackageVod.Client.exceptions.ServiceUnavailableException
    MediaPackageVod.Client.exceptions.TooManyRequestsException
    
    """
    pass

def describe_packaging_group(Id=None):
    """
    Returns a description of a MediaPackage VOD PackagingGroup resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_packaging_group(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED] The ID of a MediaPackage VOD PackagingGroup resource.

    :rtype: dict
ReturnsResponse Syntax{
    'Arn': 'string',
    'DomainName': 'string',
    'Id': 'string',
    'Tags': {
        'string': 'string'
    }
}


Response Structure

(dict) -- A MediaPackage VOD PackagingGroup resource.
Arn (string) -- The ARN of the PackagingGroup.
DomainName (string) -- The fully qualified domain name for Assets in the PackagingGroup.
Id (string) -- The ID of the PackagingGroup.
Tags (dict) -- A collection of tags associated with a resource
(string) --
(string) --









Exceptions

MediaPackageVod.Client.exceptions.UnprocessableEntityException
MediaPackageVod.Client.exceptions.InternalServerErrorException
MediaPackageVod.Client.exceptions.ForbiddenException
MediaPackageVod.Client.exceptions.NotFoundException
MediaPackageVod.Client.exceptions.ServiceUnavailableException
MediaPackageVod.Client.exceptions.TooManyRequestsException


    :return: {
        'Arn': 'string',
        'DomainName': 'string',
        'Id': 'string',
        'Tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    MediaPackageVod.Client.exceptions.UnprocessableEntityException
    MediaPackageVod.Client.exceptions.InternalServerErrorException
    MediaPackageVod.Client.exceptions.ForbiddenException
    MediaPackageVod.Client.exceptions.NotFoundException
    MediaPackageVod.Client.exceptions.ServiceUnavailableException
    MediaPackageVod.Client.exceptions.TooManyRequestsException
    
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

def list_assets(MaxResults=None, NextToken=None, PackagingGroupId=None):
    """
    Returns a collection of MediaPackage VOD Asset resources.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_assets(
        MaxResults=123,
        NextToken='string',
        PackagingGroupId='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: Upper bound on number of records to return.

    :type NextToken: string
    :param NextToken: A token used to resume pagination from the end of a previous request.

    :type PackagingGroupId: string
    :param PackagingGroupId: Returns Assets associated with the specified PackagingGroup.

    :rtype: dict

ReturnsResponse Syntax
{
    'Assets': [
        {
            'Arn': 'string',
            'CreatedAt': 'string',
            'Id': 'string',
            'PackagingGroupId': 'string',
            'ResourceId': 'string',
            'SourceArn': 'string',
            'SourceRoleArn': 'string',
            'Tags': {
                'string': 'string'
            }
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) -- A collection of MediaPackage VOD Asset resources.
Assets (list) -- A list of MediaPackage VOD Asset resources.
(dict) -- A MediaPackage VOD Asset resource.
Arn (string) -- The ARN of the Asset.
CreatedAt (string) -- The time the Asset was initially submitted for Ingest.
Id (string) -- The unique identifier for the Asset.
PackagingGroupId (string) -- The ID of the PackagingGroup for the Asset.
ResourceId (string) -- The resource ID to include in SPEKE key requests.
SourceArn (string) -- ARN of the source object in S3.
SourceRoleArn (string) -- The IAM role ARN used to access the source S3 bucket.
Tags (dict) -- A collection of tags associated with a resource
(string) --
(string) --








NextToken (string) -- A token that can be used to resume pagination from the end of the collection.






Exceptions

MediaPackageVod.Client.exceptions.UnprocessableEntityException
MediaPackageVod.Client.exceptions.InternalServerErrorException
MediaPackageVod.Client.exceptions.ForbiddenException
MediaPackageVod.Client.exceptions.NotFoundException
MediaPackageVod.Client.exceptions.ServiceUnavailableException
MediaPackageVod.Client.exceptions.TooManyRequestsException


    :return: {
        'Assets': [
            {
                'Arn': 'string',
                'CreatedAt': 'string',
                'Id': 'string',
                'PackagingGroupId': 'string',
                'ResourceId': 'string',
                'SourceArn': 'string',
                'SourceRoleArn': 'string',
                'Tags': {
                    'string': 'string'
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (dict) -- A collection of MediaPackage VOD Asset resources.
    Assets (list) -- A list of MediaPackage VOD Asset resources.
    (dict) -- A MediaPackage VOD Asset resource.
    Arn (string) -- The ARN of the Asset.
    CreatedAt (string) -- The time the Asset was initially submitted for Ingest.
    Id (string) -- The unique identifier for the Asset.
    PackagingGroupId (string) -- The ID of the PackagingGroup for the Asset.
    ResourceId (string) -- The resource ID to include in SPEKE key requests.
    SourceArn (string) -- ARN of the source object in S3.
    SourceRoleArn (string) -- The IAM role ARN used to access the source S3 bucket.
    Tags (dict) -- A collection of tags associated with a resource
    (string) --
    (string) --
    
    
    
    
    
    
    
    
    NextToken (string) -- A token that can be used to resume pagination from the end of the collection.
    
    
    
    """
    pass

def list_packaging_configurations(MaxResults=None, NextToken=None, PackagingGroupId=None):
    """
    Returns a collection of MediaPackage VOD PackagingConfiguration resources.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_packaging_configurations(
        MaxResults=123,
        NextToken='string',
        PackagingGroupId='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: Upper bound on number of records to return.

    :type NextToken: string
    :param NextToken: A token used to resume pagination from the end of a previous request.

    :type PackagingGroupId: string
    :param PackagingGroupId: Returns MediaPackage VOD PackagingConfigurations associated with the specified PackagingGroup.

    :rtype: dict

ReturnsResponse Syntax
{
    'NextToken': 'string',
    'PackagingConfigurations': [
        {
            'Arn': 'string',
            'CmafPackage': {
                'Encryption': {
                    'SpekeKeyProvider': {
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
                        'IncludeIframeOnlyStream': True|False,
                        'ManifestName': 'string',
                        'ProgramDateTimeIntervalSeconds': 123,
                        'RepeatExtXKey': True|False,
                        'StreamSelection': {
                            'MaxVideoBitsPerSecond': 123,
                            'MinVideoBitsPerSecond': 123,
                            'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
                        }
                    },
                ],
                'SegmentDurationSeconds': 123
            },
            'DashPackage': {
                'DashManifests': [
                    {
                        'ManifestLayout': 'FULL'|'COMPACT',
                        'ManifestName': 'string',
                        'MinBufferTimeSeconds': 123,
                        'Profile': 'NONE'|'HBBTV_1_5',
                        'StreamSelection': {
                            'MaxVideoBitsPerSecond': 123,
                            'MinVideoBitsPerSecond': 123,
                            'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
                        }
                    },
                ],
                'Encryption': {
                    'SpekeKeyProvider': {
                        'RoleArn': 'string',
                        'SystemIds': [
                            'string',
                        ],
                        'Url': 'string'
                    }
                },
                'PeriodTriggers': [
                    'ADS',
                ],
                'SegmentDurationSeconds': 123,
                'SegmentTemplateFormat': 'NUMBER_WITH_TIMELINE'|'TIME_WITH_TIMELINE'|'NUMBER_WITH_DURATION'
            },
            'HlsPackage': {
                'Encryption': {
                    'ConstantInitializationVector': 'string',
                    'EncryptionMethod': 'AES_128'|'SAMPLE_AES',
                    'SpekeKeyProvider': {
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
                        'IncludeIframeOnlyStream': True|False,
                        'ManifestName': 'string',
                        'ProgramDateTimeIntervalSeconds': 123,
                        'RepeatExtXKey': True|False,
                        'StreamSelection': {
                            'MaxVideoBitsPerSecond': 123,
                            'MinVideoBitsPerSecond': 123,
                            'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
                        }
                    },
                ],
                'SegmentDurationSeconds': 123,
                'UseAudioRenditionGroup': True|False
            },
            'Id': 'string',
            'MssPackage': {
                'Encryption': {
                    'SpekeKeyProvider': {
                        'RoleArn': 'string',
                        'SystemIds': [
                            'string',
                        ],
                        'Url': 'string'
                    }
                },
                'MssManifests': [
                    {
                        'ManifestName': 'string',
                        'StreamSelection': {
                            'MaxVideoBitsPerSecond': 123,
                            'MinVideoBitsPerSecond': 123,
                            'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
                        }
                    },
                ],
                'SegmentDurationSeconds': 123
            },
            'PackagingGroupId': 'string',
            'Tags': {
                'string': 'string'
            }
        },
    ]
}


Response Structure

(dict) -- A collection of MediaPackage VOD PackagingConfiguration resources.
NextToken (string) -- A token that can be used to resume pagination from the end of the collection.
PackagingConfigurations (list) -- A list of MediaPackage VOD PackagingConfiguration resources.
(dict) -- A MediaPackage VOD PackagingConfiguration resource.
Arn (string) -- The ARN of the PackagingConfiguration.
CmafPackage (dict) -- A CMAF packaging configuration.
Encryption (dict) -- A CMAF encryption configuration.
SpekeKeyProvider (dict) -- A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
RoleArn (string) -- An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.
SystemIds (list) -- The system IDs to include in key requests.
(string) --


Url (string) -- The URL of the external key provider service.




HlsManifests (list) -- A list of HLS manifest configurations.
(dict) -- An HTTP Live Streaming (HLS) manifest configuration.
AdMarkers (string) -- This setting controls how ad markers are included in the packaged OriginEndpoint. "NONE" will omit all SCTE-35 ad markers from the output. "PASSTHROUGH" causes the manifest to contain a copy of the SCTE-35 ad markers (comments) taken directly from the input HTTP Live Streaming (HLS) manifest. "SCTE35_ENHANCED" generates ad markers and blackout tags based on SCTE-35 messages in the input source.
IncludeIframeOnlyStream (boolean) -- When enabled, an I-Frame only stream will be included in the output.
ManifestName (string) -- An optional string to include in the name of the manifest.
ProgramDateTimeIntervalSeconds (integer) -- The interval (in seconds) between each EXT-X-PROGRAM-DATE-TIME tag inserted into manifests. Additionally, when an interval is specified ID3Timed Metadata messages will be generated every 5 seconds using the ingest time of the content. If the interval is not specified, or set to 0, then no EXT-X-PROGRAM-DATE-TIME tags will be inserted into manifests and no ID3Timed Metadata messages will be generated. Note that irrespective of this parameter, if any ID3 Timed Metadata is found in HTTP Live Streaming (HLS) input, it will be passed through to HLS output.
RepeatExtXKey (boolean) -- When enabled, the EXT-X-KEY tag will be repeated in output manifests.
StreamSelection (dict) -- A StreamSelection configuration.
MaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.
MinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.
StreamOrder (string) -- A directive that determines the order of streams in the output.






SegmentDurationSeconds (integer) -- Duration (in seconds) of each fragment. Actual fragments will be rounded to the nearest multiple of the source fragment duration.


DashPackage (dict) -- A Dynamic Adaptive Streaming over HTTP (DASH) packaging configuration.
DashManifests (list) -- A list of DASH manifest configurations.
(dict) -- A DASH manifest configuration.
ManifestLayout (string) -- Determines the position of some tags in the Media Presentation Description (MPD). When set to FULL, elements like SegmentTemplate and ContentProtection are included in each Representation. When set to COMPACT, duplicate elements are combined and presented at the AdaptationSet level.
ManifestName (string) -- An optional string to include in the name of the manifest.
MinBufferTimeSeconds (integer) -- Minimum duration (in seconds) that a player will buffer media before starting the presentation.
Profile (string) -- The Dynamic Adaptive Streaming over HTTP (DASH) profile type. When set to "HBBTV_1_5", HbbTV 1.5 compliant output is enabled.
StreamSelection (dict) -- A StreamSelection configuration.
MaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.
MinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.
StreamOrder (string) -- A directive that determines the order of streams in the output.






Encryption (dict) -- A Dynamic Adaptive Streaming over HTTP (DASH) encryption configuration.
SpekeKeyProvider (dict) -- A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
RoleArn (string) -- An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.
SystemIds (list) -- The system IDs to include in key requests.
(string) --


Url (string) -- The URL of the external key provider service.




PeriodTriggers (list) -- A list of triggers that controls when the outgoing Dynamic Adaptive Streaming over HTTP (DASH) Media Presentation Description (MPD) will be partitioned into multiple periods. If empty, the content will not be partitioned into more than one period. If the list contains "ADS", new periods will be created where the Asset contains SCTE-35 ad markers.
(string) --


SegmentDurationSeconds (integer) -- Duration (in seconds) of each segment. Actual segments will be rounded to the nearest multiple of the source segment duration.
SegmentTemplateFormat (string) -- Determines the type of SegmentTemplate included in the Media Presentation Description (MPD). When set to NUMBER_WITH_TIMELINE, a full timeline is presented in each SegmentTemplate, with $Number$ media URLs. When set to TIME_WITH_TIMELINE, a full timeline is presented in each SegmentTemplate, with $Time$ media URLs. When set to NUMBER_WITH_DURATION, only a duration is included in each SegmentTemplate, with $Number$ media URLs.


HlsPackage (dict) -- An HTTP Live Streaming (HLS) packaging configuration.
Encryption (dict) -- An HTTP Live Streaming (HLS) encryption configuration.
ConstantInitializationVector (string) -- A constant initialization vector for encryption (optional). When not specified the initialization vector will be periodically rotated.
EncryptionMethod (string) -- The encryption method to use.
SpekeKeyProvider (dict) -- A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
RoleArn (string) -- An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.
SystemIds (list) -- The system IDs to include in key requests.
(string) --


Url (string) -- The URL of the external key provider service.




HlsManifests (list) -- A list of HLS manifest configurations.
(dict) -- An HTTP Live Streaming (HLS) manifest configuration.
AdMarkers (string) -- This setting controls how ad markers are included in the packaged OriginEndpoint. "NONE" will omit all SCTE-35 ad markers from the output. "PASSTHROUGH" causes the manifest to contain a copy of the SCTE-35 ad markers (comments) taken directly from the input HTTP Live Streaming (HLS) manifest. "SCTE35_ENHANCED" generates ad markers and blackout tags based on SCTE-35 messages in the input source.
IncludeIframeOnlyStream (boolean) -- When enabled, an I-Frame only stream will be included in the output.
ManifestName (string) -- An optional string to include in the name of the manifest.
ProgramDateTimeIntervalSeconds (integer) -- The interval (in seconds) between each EXT-X-PROGRAM-DATE-TIME tag inserted into manifests. Additionally, when an interval is specified ID3Timed Metadata messages will be generated every 5 seconds using the ingest time of the content. If the interval is not specified, or set to 0, then no EXT-X-PROGRAM-DATE-TIME tags will be inserted into manifests and no ID3Timed Metadata messages will be generated. Note that irrespective of this parameter, if any ID3 Timed Metadata is found in HTTP Live Streaming (HLS) input, it will be passed through to HLS output.
RepeatExtXKey (boolean) -- When enabled, the EXT-X-KEY tag will be repeated in output manifests.
StreamSelection (dict) -- A StreamSelection configuration.
MaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.
MinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.
StreamOrder (string) -- A directive that determines the order of streams in the output.






SegmentDurationSeconds (integer) -- Duration (in seconds) of each fragment. Actual fragments will be rounded to the nearest multiple of the source fragment duration.
UseAudioRenditionGroup (boolean) -- When enabled, audio streams will be placed in rendition groups in the output.


Id (string) -- The ID of the PackagingConfiguration.
MssPackage (dict) -- A Microsoft Smooth Streaming (MSS) PackagingConfiguration.
Encryption (dict) -- A Microsoft Smooth Streaming (MSS) encryption configuration.
SpekeKeyProvider (dict) -- A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
RoleArn (string) -- An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.
SystemIds (list) -- The system IDs to include in key requests.
(string) --


Url (string) -- The URL of the external key provider service.




MssManifests (list) -- A list of MSS manifest configurations.
(dict) -- A Microsoft Smooth Streaming (MSS) manifest configuration.
ManifestName (string) -- An optional string to include in the name of the manifest.
StreamSelection (dict) -- A StreamSelection configuration.
MaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.
MinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.
StreamOrder (string) -- A directive that determines the order of streams in the output.






SegmentDurationSeconds (integer) -- The duration (in seconds) of each segment.


PackagingGroupId (string) -- The ID of a PackagingGroup.
Tags (dict) -- A collection of tags associated with a resource
(string) --
(string) --














Exceptions

MediaPackageVod.Client.exceptions.UnprocessableEntityException
MediaPackageVod.Client.exceptions.InternalServerErrorException
MediaPackageVod.Client.exceptions.ForbiddenException
MediaPackageVod.Client.exceptions.NotFoundException
MediaPackageVod.Client.exceptions.ServiceUnavailableException
MediaPackageVod.Client.exceptions.TooManyRequestsException


    :return: {
        'NextToken': 'string',
        'PackagingConfigurations': [
            {
                'Arn': 'string',
                'CmafPackage': {
                    'Encryption': {
                        'SpekeKeyProvider': {
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
                            'IncludeIframeOnlyStream': True|False,
                            'ManifestName': 'string',
                            'ProgramDateTimeIntervalSeconds': 123,
                            'RepeatExtXKey': True|False,
                            'StreamSelection': {
                                'MaxVideoBitsPerSecond': 123,
                                'MinVideoBitsPerSecond': 123,
                                'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
                            }
                        },
                    ],
                    'SegmentDurationSeconds': 123
                },
                'DashPackage': {
                    'DashManifests': [
                        {
                            'ManifestLayout': 'FULL'|'COMPACT',
                            'ManifestName': 'string',
                            'MinBufferTimeSeconds': 123,
                            'Profile': 'NONE'|'HBBTV_1_5',
                            'StreamSelection': {
                                'MaxVideoBitsPerSecond': 123,
                                'MinVideoBitsPerSecond': 123,
                                'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
                            }
                        },
                    ],
                    'Encryption': {
                        'SpekeKeyProvider': {
                            'RoleArn': 'string',
                            'SystemIds': [
                                'string',
                            ],
                            'Url': 'string'
                        }
                    },
                    'PeriodTriggers': [
                        'ADS',
                    ],
                    'SegmentDurationSeconds': 123,
                    'SegmentTemplateFormat': 'NUMBER_WITH_TIMELINE'|'TIME_WITH_TIMELINE'|'NUMBER_WITH_DURATION'
                },
                'HlsPackage': {
                    'Encryption': {
                        'ConstantInitializationVector': 'string',
                        'EncryptionMethod': 'AES_128'|'SAMPLE_AES',
                        'SpekeKeyProvider': {
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
                            'IncludeIframeOnlyStream': True|False,
                            'ManifestName': 'string',
                            'ProgramDateTimeIntervalSeconds': 123,
                            'RepeatExtXKey': True|False,
                            'StreamSelection': {
                                'MaxVideoBitsPerSecond': 123,
                                'MinVideoBitsPerSecond': 123,
                                'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
                            }
                        },
                    ],
                    'SegmentDurationSeconds': 123,
                    'UseAudioRenditionGroup': True|False
                },
                'Id': 'string',
                'MssPackage': {
                    'Encryption': {
                        'SpekeKeyProvider': {
                            'RoleArn': 'string',
                            'SystemIds': [
                                'string',
                            ],
                            'Url': 'string'
                        }
                    },
                    'MssManifests': [
                        {
                            'ManifestName': 'string',
                            'StreamSelection': {
                                'MaxVideoBitsPerSecond': 123,
                                'MinVideoBitsPerSecond': 123,
                                'StreamOrder': 'ORIGINAL'|'VIDEO_BITRATE_ASCENDING'|'VIDEO_BITRATE_DESCENDING'
                            }
                        },
                    ],
                    'SegmentDurationSeconds': 123
                },
                'PackagingGroupId': 'string',
                'Tags': {
                    'string': 'string'
                }
            },
        ]
    }
    
    
    :returns: 
    (dict) -- A collection of MediaPackage VOD PackagingConfiguration resources.
    NextToken (string) -- A token that can be used to resume pagination from the end of the collection.
    PackagingConfigurations (list) -- A list of MediaPackage VOD PackagingConfiguration resources.
    (dict) -- A MediaPackage VOD PackagingConfiguration resource.
    Arn (string) -- The ARN of the PackagingConfiguration.
    CmafPackage (dict) -- A CMAF packaging configuration.
    Encryption (dict) -- A CMAF encryption configuration.
    SpekeKeyProvider (dict) -- A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
    RoleArn (string) -- An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.
    SystemIds (list) -- The system IDs to include in key requests.
    (string) --
    
    
    Url (string) -- The URL of the external key provider service.
    
    
    
    
    HlsManifests (list) -- A list of HLS manifest configurations.
    (dict) -- An HTTP Live Streaming (HLS) manifest configuration.
    AdMarkers (string) -- This setting controls how ad markers are included in the packaged OriginEndpoint. "NONE" will omit all SCTE-35 ad markers from the output. "PASSTHROUGH" causes the manifest to contain a copy of the SCTE-35 ad markers (comments) taken directly from the input HTTP Live Streaming (HLS) manifest. "SCTE35_ENHANCED" generates ad markers and blackout tags based on SCTE-35 messages in the input source.
    IncludeIframeOnlyStream (boolean) -- When enabled, an I-Frame only stream will be included in the output.
    ManifestName (string) -- An optional string to include in the name of the manifest.
    ProgramDateTimeIntervalSeconds (integer) -- The interval (in seconds) between each EXT-X-PROGRAM-DATE-TIME tag inserted into manifests. Additionally, when an interval is specified ID3Timed Metadata messages will be generated every 5 seconds using the ingest time of the content. If the interval is not specified, or set to 0, then no EXT-X-PROGRAM-DATE-TIME tags will be inserted into manifests and no ID3Timed Metadata messages will be generated. Note that irrespective of this parameter, if any ID3 Timed Metadata is found in HTTP Live Streaming (HLS) input, it will be passed through to HLS output.
    RepeatExtXKey (boolean) -- When enabled, the EXT-X-KEY tag will be repeated in output manifests.
    StreamSelection (dict) -- A StreamSelection configuration.
    MaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.
    MinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.
    StreamOrder (string) -- A directive that determines the order of streams in the output.
    
    
    
    
    
    
    SegmentDurationSeconds (integer) -- Duration (in seconds) of each fragment. Actual fragments will be rounded to the nearest multiple of the source fragment duration.
    
    
    DashPackage (dict) -- A Dynamic Adaptive Streaming over HTTP (DASH) packaging configuration.
    DashManifests (list) -- A list of DASH manifest configurations.
    (dict) -- A DASH manifest configuration.
    ManifestLayout (string) -- Determines the position of some tags in the Media Presentation Description (MPD). When set to FULL, elements like SegmentTemplate and ContentProtection are included in each Representation. When set to COMPACT, duplicate elements are combined and presented at the AdaptationSet level.
    ManifestName (string) -- An optional string to include in the name of the manifest.
    MinBufferTimeSeconds (integer) -- Minimum duration (in seconds) that a player will buffer media before starting the presentation.
    Profile (string) -- The Dynamic Adaptive Streaming over HTTP (DASH) profile type. When set to "HBBTV_1_5", HbbTV 1.5 compliant output is enabled.
    StreamSelection (dict) -- A StreamSelection configuration.
    MaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.
    MinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.
    StreamOrder (string) -- A directive that determines the order of streams in the output.
    
    
    
    
    
    
    Encryption (dict) -- A Dynamic Adaptive Streaming over HTTP (DASH) encryption configuration.
    SpekeKeyProvider (dict) -- A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
    RoleArn (string) -- An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.
    SystemIds (list) -- The system IDs to include in key requests.
    (string) --
    
    
    Url (string) -- The URL of the external key provider service.
    
    
    
    
    PeriodTriggers (list) -- A list of triggers that controls when the outgoing Dynamic Adaptive Streaming over HTTP (DASH) Media Presentation Description (MPD) will be partitioned into multiple periods. If empty, the content will not be partitioned into more than one period. If the list contains "ADS", new periods will be created where the Asset contains SCTE-35 ad markers.
    (string) --
    
    
    SegmentDurationSeconds (integer) -- Duration (in seconds) of each segment. Actual segments will be rounded to the nearest multiple of the source segment duration.
    SegmentTemplateFormat (string) -- Determines the type of SegmentTemplate included in the Media Presentation Description (MPD). When set to NUMBER_WITH_TIMELINE, a full timeline is presented in each SegmentTemplate, with $Number$ media URLs. When set to TIME_WITH_TIMELINE, a full timeline is presented in each SegmentTemplate, with $Time$ media URLs. When set to NUMBER_WITH_DURATION, only a duration is included in each SegmentTemplate, with $Number$ media URLs.
    
    
    HlsPackage (dict) -- An HTTP Live Streaming (HLS) packaging configuration.
    Encryption (dict) -- An HTTP Live Streaming (HLS) encryption configuration.
    ConstantInitializationVector (string) -- A constant initialization vector for encryption (optional). When not specified the initialization vector will be periodically rotated.
    EncryptionMethod (string) -- The encryption method to use.
    SpekeKeyProvider (dict) -- A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
    RoleArn (string) -- An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.
    SystemIds (list) -- The system IDs to include in key requests.
    (string) --
    
    
    Url (string) -- The URL of the external key provider service.
    
    
    
    
    HlsManifests (list) -- A list of HLS manifest configurations.
    (dict) -- An HTTP Live Streaming (HLS) manifest configuration.
    AdMarkers (string) -- This setting controls how ad markers are included in the packaged OriginEndpoint. "NONE" will omit all SCTE-35 ad markers from the output. "PASSTHROUGH" causes the manifest to contain a copy of the SCTE-35 ad markers (comments) taken directly from the input HTTP Live Streaming (HLS) manifest. "SCTE35_ENHANCED" generates ad markers and blackout tags based on SCTE-35 messages in the input source.
    IncludeIframeOnlyStream (boolean) -- When enabled, an I-Frame only stream will be included in the output.
    ManifestName (string) -- An optional string to include in the name of the manifest.
    ProgramDateTimeIntervalSeconds (integer) -- The interval (in seconds) between each EXT-X-PROGRAM-DATE-TIME tag inserted into manifests. Additionally, when an interval is specified ID3Timed Metadata messages will be generated every 5 seconds using the ingest time of the content. If the interval is not specified, or set to 0, then no EXT-X-PROGRAM-DATE-TIME tags will be inserted into manifests and no ID3Timed Metadata messages will be generated. Note that irrespective of this parameter, if any ID3 Timed Metadata is found in HTTP Live Streaming (HLS) input, it will be passed through to HLS output.
    RepeatExtXKey (boolean) -- When enabled, the EXT-X-KEY tag will be repeated in output manifests.
    StreamSelection (dict) -- A StreamSelection configuration.
    MaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.
    MinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.
    StreamOrder (string) -- A directive that determines the order of streams in the output.
    
    
    
    
    
    
    SegmentDurationSeconds (integer) -- Duration (in seconds) of each fragment. Actual fragments will be rounded to the nearest multiple of the source fragment duration.
    UseAudioRenditionGroup (boolean) -- When enabled, audio streams will be placed in rendition groups in the output.
    
    
    Id (string) -- The ID of the PackagingConfiguration.
    MssPackage (dict) -- A Microsoft Smooth Streaming (MSS) PackagingConfiguration.
    Encryption (dict) -- A Microsoft Smooth Streaming (MSS) encryption configuration.
    SpekeKeyProvider (dict) -- A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
    RoleArn (string) -- An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.
    SystemIds (list) -- The system IDs to include in key requests.
    (string) --
    
    
    Url (string) -- The URL of the external key provider service.
    
    
    
    
    MssManifests (list) -- A list of MSS manifest configurations.
    (dict) -- A Microsoft Smooth Streaming (MSS) manifest configuration.
    ManifestName (string) -- An optional string to include in the name of the manifest.
    StreamSelection (dict) -- A StreamSelection configuration.
    MaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.
    MinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.
    StreamOrder (string) -- A directive that determines the order of streams in the output.
    
    
    
    
    
    
    SegmentDurationSeconds (integer) -- The duration (in seconds) of each segment.
    
    
    PackagingGroupId (string) -- The ID of a PackagingGroup.
    Tags (dict) -- A collection of tags associated with a resource
    (string) --
    (string) --
    
    
    
    
    
    
    
    
    
    
    
    """
    pass

def list_packaging_groups(MaxResults=None, NextToken=None):
    """
    Returns a collection of MediaPackage VOD PackagingGroup resources.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_packaging_groups(
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
    'NextToken': 'string',
    'PackagingGroups': [
        {
            'Arn': 'string',
            'DomainName': 'string',
            'Id': 'string',
            'Tags': {
                'string': 'string'
            }
        },
    ]
}


Response Structure

(dict) -- A collection of MediaPackage VOD PackagingGroup resources.
NextToken (string) -- A token that can be used to resume pagination from the end of the collection.
PackagingGroups (list) -- A list of MediaPackage VOD PackagingGroup resources.
(dict) -- A MediaPackage VOD PackagingGroup resource.
Arn (string) -- The ARN of the PackagingGroup.
DomainName (string) -- The fully qualified domain name for Assets in the PackagingGroup.
Id (string) -- The ID of the PackagingGroup.
Tags (dict) -- A collection of tags associated with a resource
(string) --
(string) --














Exceptions

MediaPackageVod.Client.exceptions.UnprocessableEntityException
MediaPackageVod.Client.exceptions.InternalServerErrorException
MediaPackageVod.Client.exceptions.ForbiddenException
MediaPackageVod.Client.exceptions.NotFoundException
MediaPackageVod.Client.exceptions.ServiceUnavailableException
MediaPackageVod.Client.exceptions.TooManyRequestsException


    :return: {
        'NextToken': 'string',
        'PackagingGroups': [
            {
                'Arn': 'string',
                'DomainName': 'string',
                'Id': 'string',
                'Tags': {
                    'string': 'string'
                }
            },
        ]
    }
    
    
    :returns: 
    (dict) -- A collection of MediaPackage VOD PackagingGroup resources.
    NextToken (string) -- A token that can be used to resume pagination from the end of the collection.
    PackagingGroups (list) -- A list of MediaPackage VOD PackagingGroup resources.
    (dict) -- A MediaPackage VOD PackagingGroup resource.
    Arn (string) -- The ARN of the PackagingGroup.
    DomainName (string) -- The fully qualified domain name for Assets in the PackagingGroup.
    Id (string) -- The ID of the PackagingGroup.
    Tags (dict) -- A collection of tags associated with a resource
    (string) --
    (string) --
    
    
    
    
    
    
    
    
    
    
    
    """
    pass

def list_tags_for_resource(ResourceArn=None):
    """
    List tags for a given MediaPackage VOD resource
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

def tag_resource(ResourceArn=None, Tags=None):
    """
    Set tags for a given MediaPackage VOD resource
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
    Delete tags for a given MediaPackage VOD resource
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

