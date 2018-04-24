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

def create_channel(Description=None, Id=None):
    """
    Creates a new Channel.
    See also: AWS API Documentation
    
    
    :example: response = client.create_channel(
        Description='string',
        Id='string'
    )
    
    
    :type Description: string
    :param Description: A short text description of the Channel.

    :type Id: string
    :param Id: [REQUIRED] The ID of the Channel. The ID must be unique within the region and it cannot be changed after a Channel is created.

    :rtype: dict
    :return: {
        'Arn': 'string',
        'Description': 'string',
        'HlsIngest': {
            'IngestEndpoints': [
                {
                    'Password': 'string',
                    'Url': 'string',
                    'Username': 'string'
                },
            ]
        },
        'Id': 'string'
    }
    
    
    :returns: 
    (dict) -- The new Channel record.
    Arn (string) -- The Amazon Resource Name (ARN) assigned to the Channel.
    Description (string) -- A short text description of the Channel.
    HlsIngest (dict) -- An HTTP Live Streaming (HLS) ingest resource configuration.
    IngestEndpoints (list) -- A list of endpoints to which the source stream should be sent.
    (dict) -- An endpoint for ingesting source content for a Channel.
    Password (string) -- The system generated password for ingest authentication.
    Url (string) -- The ingest URL to which the source stream should be sent.
    Username (string) -- The system generated username for ingest authentication.
    
    
    
    
    
    
    Id (string) -- The ID of the Channel.
    
    
    
    """
    pass

def create_origin_endpoint(ChannelId=None, CmafPackage=None, DashPackage=None, Description=None, HlsPackage=None, Id=None, ManifestName=None, MssPackage=None, StartoverWindowSeconds=None, TimeDelaySeconds=None, Whitelist=None):
    """
    Creates a new OriginEndpoint record.
    See also: AWS API Documentation
    
    
    :example: response = client.create_origin_endpoint(
        ChannelId='string',
        CmafPackage={
            'Encryption': {
                'KeyRotationIntervalSeconds': 123,
                'SpekeKeyProvider': {
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
            'Encryption': {
                'KeyRotationIntervalSeconds': 123,
                'SpekeKeyProvider': {
                    'ResourceId': 'string',
                    'RoleArn': 'string',
                    'SystemIds': [
                        'string',
                    ],
                    'Url': 'string'
                }
            },
            'ManifestWindowSeconds': 123,
            'MinBufferTimeSeconds': 123,
            'MinUpdatePeriodSeconds': 123,
            'Profile': 'NONE'|'HBBTV_1_5',
            'SegmentDurationSeconds': 123,
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
            'Encryption': {
                'ConstantInitializationVector': 'string',
                'EncryptionMethod': 'AES_128'|'SAMPLE_AES',
                'KeyRotationIntervalSeconds': 123,
                'RepeatExtXKey': True|False,
                'SpekeKeyProvider': {
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
        StartoverWindowSeconds=123,
        TimeDelaySeconds=123,
        Whitelist=[
            'string',
        ]
    )
    
    
    :type ChannelId: string
    :param ChannelId: [REQUIRED] The ID of the Channel that the OriginEndpoint will be associated with. This cannot be changed after the OriginEndpoint is created.

    :type CmafPackage: dict
    :param CmafPackage: A Common Media Application Format (CMAF) packaging configuration.
            Encryption (dict) -- A Common Media Application Format (CMAF) encryption configuration.
            KeyRotationIntervalSeconds (integer) -- Time (in seconds) between each encryption key rotation.
            SpekeKeyProvider (dict) -- [REQUIRED] A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
            ResourceId (string) -- [REQUIRED] The resource ID to include in key requests.
            RoleArn (string) -- [REQUIRED] An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.
            SystemIds (list) -- [REQUIRED] The system IDs to include in key requests.
            (string) --
            Url (string) -- [REQUIRED] The URL of the external key provider service.
            
            HlsManifests (list) -- A list of HLS manifest configurations
            (dict) -- A HTTP Live Streaming (HLS) manifest configuration.
            AdMarkers (string) -- This setting controls how ad markers are included in the packaged OriginEndpoint. 'NONE' will omit all SCTE-35 ad markers from the output. 'PASSTHROUGH' causes the manifest to contain a copy of the SCTE-35 ad markers (comments) taken directly from the input HTTP Live Streaming (HLS) manifest. 'SCTE35_ENHANCED' generates ad markers and blackout tags based on SCTE-35 messages in the input source.
            Id (string) -- [REQUIRED] The ID of the manifest. The ID must be unique within the OriginEndpoint and it cannot be changed after it is created.
            IncludeIframeOnlyStream (boolean) -- When enabled, an I-Frame only stream will be included in the output.
            ManifestName (string) -- An optional short string appended to the end of the OriginEndpoint URL. If not specified, defaults to the manifestName for the OriginEndpoint.
            PlaylistType (string) -- The HTTP Live Streaming (HLS) playlist type. When either 'EVENT' or 'VOD' is specified, a corresponding EXT-X-PLAYLIST-TYPE entry will be included in the media playlist.
            PlaylistWindowSeconds (integer) -- Time window (in seconds) contained in each parent manifest.
            ProgramDateTimeIntervalSeconds (integer) -- The interval (in seconds) between each EXT-X-PROGRAM-DATE-TIME tag inserted into manifests. Additionally, when an interval is specified ID3Timed Metadata messages will be generated every 5 seconds using the ingest time of the content. If the interval is not specified, or set to 0, then no EXT-X-PROGRAM-DATE-TIME tags will be inserted into manifests and no ID3Timed Metadata messages will be generated. Note that irrespective of this parameter, if any ID3 Timed Metadata is found in HTTP Live Streaming (HLS) input, it will be passed through to HLS output.
            
            SegmentDurationSeconds (integer) -- Duration (in seconds) of each segment. Actual segments will be rounded to the nearest multiple of the source segment duration.
            SegmentPrefix (string) -- An optional custom string that is prepended to the name of each segment. If not specified, it defaults to the ChannelId.
            StreamSelection (dict) -- A StreamSelection configuration.
            MaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.
            MinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.
            StreamOrder (string) -- A directive that determines the order of streams in the output.
            

    :type DashPackage: dict
    :param DashPackage: A Dynamic Adaptive Streaming over HTTP (DASH) packaging configuration.
            Encryption (dict) -- A Dynamic Adaptive Streaming over HTTP (DASH) encryption configuration.
            KeyRotationIntervalSeconds (integer) -- Time (in seconds) between each encryption key rotation.
            SpekeKeyProvider (dict) -- [REQUIRED] A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
            ResourceId (string) -- [REQUIRED] The resource ID to include in key requests.
            RoleArn (string) -- [REQUIRED] An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.
            SystemIds (list) -- [REQUIRED] The system IDs to include in key requests.
            (string) --
            Url (string) -- [REQUIRED] The URL of the external key provider service.
            
            ManifestWindowSeconds (integer) -- Time window (in seconds) contained in each manifest.
            MinBufferTimeSeconds (integer) -- Minimum duration (in seconds) that a player will buffer media before starting the presentation.
            MinUpdatePeriodSeconds (integer) -- Minimum duration (in seconds) between potential changes to the Dynamic Adaptive Streaming over HTTP (DASH) Media Presentation Description (MPD).
            Profile (string) -- The Dynamic Adaptive Streaming over HTTP (DASH) profile type. When set to 'HBBTV_1_5', HbbTV 1.5 compliant output is enabled.
            SegmentDurationSeconds (integer) -- Duration (in seconds) of each segment. Actual segments will be rounded to the nearest multiple of the source segment duration.
            StreamSelection (dict) -- A StreamSelection configuration.
            MaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.
            MinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.
            StreamOrder (string) -- A directive that determines the order of streams in the output.
            SuggestedPresentationDelaySeconds (integer) -- Duration (in seconds) to delay live content before presentation.
            

    :type Description: string
    :param Description: A short text description of the OriginEndpoint.

    :type HlsPackage: dict
    :param HlsPackage: An HTTP Live Streaming (HLS) packaging configuration.
            AdMarkers (string) -- This setting controls how ad markers are included in the packaged OriginEndpoint. 'NONE' will omit all SCTE-35 ad markers from the output. 'PASSTHROUGH' causes the manifest to contain a copy of the SCTE-35 ad markers (comments) taken directly from the input HTTP Live Streaming (HLS) manifest. 'SCTE35_ENHANCED' generates ad markers and blackout tags based on SCTE-35 messages in the input source.
            Encryption (dict) -- An HTTP Live Streaming (HLS) encryption configuration.
            ConstantInitializationVector (string) -- A constant initialization vector for encryption (optional). When not specified the initialization vector will be periodically rotated.
            EncryptionMethod (string) -- The encryption method to use.
            KeyRotationIntervalSeconds (integer) -- Interval (in seconds) between each encryption key rotation.
            RepeatExtXKey (boolean) -- When enabled, the EXT-X-KEY tag will be repeated in output manifests.
            SpekeKeyProvider (dict) -- [REQUIRED] A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
            ResourceId (string) -- [REQUIRED] The resource ID to include in key requests.
            RoleArn (string) -- [REQUIRED] An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.
            SystemIds (list) -- [REQUIRED] The system IDs to include in key requests.
            (string) --
            Url (string) -- [REQUIRED] The URL of the external key provider service.
            
            IncludeIframeOnlyStream (boolean) -- When enabled, an I-Frame only stream will be included in the output.
            PlaylistType (string) -- The HTTP Live Streaming (HLS) playlist type. When either 'EVENT' or 'VOD' is specified, a corresponding EXT-X-PLAYLIST-TYPE entry will be included in the media playlist.
            PlaylistWindowSeconds (integer) -- Time window (in seconds) contained in each parent manifest.
            ProgramDateTimeIntervalSeconds (integer) -- The interval (in seconds) between each EXT-X-PROGRAM-DATE-TIME tag inserted into manifests. Additionally, when an interval is specified ID3Timed Metadata messages will be generated every 5 seconds using the ingest time of the content. If the interval is not specified, or set to 0, then no EXT-X-PROGRAM-DATE-TIME tags will be inserted into manifests and no ID3Timed Metadata messages will be generated. Note that irrespective of this parameter, if any ID3 Timed Metadata is found in HTTP Live Streaming (HLS) input, it will be passed through to HLS output.
            SegmentDurationSeconds (integer) -- Duration (in seconds) of each fragment. Actual fragments will be rounded to the nearest multiple of the source fragment duration.
            StreamSelection (dict) -- A StreamSelection configuration.
            MaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.
            MinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.
            StreamOrder (string) -- A directive that determines the order of streams in the output.
            UseAudioRenditionGroup (boolean) -- When enabled, audio streams will be placed in rendition groups in the output.
            

    :type Id: string
    :param Id: [REQUIRED] The ID of the OriginEndpoint. The ID must be unique within the region and it cannot be changed after the OriginEndpoint is created.

    :type ManifestName: string
    :param ManifestName: A short string that will be used as the filename of the OriginEndpoint URL (defaults to 'index').

    :type MssPackage: dict
    :param MssPackage: A Microsoft Smooth Streaming (MSS) packaging configuration.
            Encryption (dict) -- A Microsoft Smooth Streaming (MSS) encryption configuration.
            SpekeKeyProvider (dict) -- [REQUIRED] A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
            ResourceId (string) -- [REQUIRED] The resource ID to include in key requests.
            RoleArn (string) -- [REQUIRED] An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.
            SystemIds (list) -- [REQUIRED] The system IDs to include in key requests.
            (string) --
            Url (string) -- [REQUIRED] The URL of the external key provider service.
            
            ManifestWindowSeconds (integer) -- The time window (in seconds) contained in each manifest.
            SegmentDurationSeconds (integer) -- The duration (in seconds) of each segment.
            StreamSelection (dict) -- A StreamSelection configuration.
            MaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.
            MinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.
            StreamOrder (string) -- A directive that determines the order of streams in the output.
            

    :type StartoverWindowSeconds: integer
    :param StartoverWindowSeconds: Maximum duration (seconds) of content to retain for startover playback. If not specified, startover playback will be disabled for the OriginEndpoint.

    :type TimeDelaySeconds: integer
    :param TimeDelaySeconds: Amount of delay (seconds) to enforce on the playback of live content. If not specified, there will be no time delay in effect for the OriginEndpoint.

    :type Whitelist: list
    :param Whitelist: A list of source IP CIDR blocks that will be allowed to access the OriginEndpoint.
            (string) --
            

    :rtype: dict
    :return: {
        'Arn': 'string',
        'ChannelId': 'string',
        'CmafPackage': {
            'Encryption': {
                'KeyRotationIntervalSeconds': 123,
                'SpekeKeyProvider': {
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
            'Encryption': {
                'KeyRotationIntervalSeconds': 123,
                'SpekeKeyProvider': {
                    'ResourceId': 'string',
                    'RoleArn': 'string',
                    'SystemIds': [
                        'string',
                    ],
                    'Url': 'string'
                }
            },
            'ManifestWindowSeconds': 123,
            'MinBufferTimeSeconds': 123,
            'MinUpdatePeriodSeconds': 123,
            'Profile': 'NONE'|'HBBTV_1_5',
            'SegmentDurationSeconds': 123,
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
            'Encryption': {
                'ConstantInitializationVector': 'string',
                'EncryptionMethod': 'AES_128'|'SAMPLE_AES',
                'KeyRotationIntervalSeconds': 123,
                'RepeatExtXKey': True|False,
                'SpekeKeyProvider': {
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
        'StartoverWindowSeconds': 123,
        'TimeDelaySeconds': 123,
        'Url': 'string',
        'Whitelist': [
            'string',
        ]
    }
    
    
    :returns: 
    (dict) -- A new OriginEndpoint record.
    Arn (string) -- The Amazon Resource Name (ARN) assigned to the OriginEndpoint.
    ChannelId (string) -- The ID of the Channel the OriginEndpoint is associated with.
    CmafPackage (dict) -- A Common Media Application Format (CMAF) packaging configuration.
    Encryption (dict) -- A Common Media Application Format (CMAF) encryption configuration.
    KeyRotationIntervalSeconds (integer) -- Time (in seconds) between each encryption key rotation.
    SpekeKeyProvider (dict) -- A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
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
    Encryption (dict) -- A Dynamic Adaptive Streaming over HTTP (DASH) encryption configuration.
    KeyRotationIntervalSeconds (integer) -- Time (in seconds) between each encryption key rotation.
    SpekeKeyProvider (dict) -- A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
    ResourceId (string) -- The resource ID to include in key requests.
    RoleArn (string) -- An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.
    SystemIds (list) -- The system IDs to include in key requests.
    (string) --
    
    
    Url (string) -- The URL of the external key provider service.
    
    
    
    
    ManifestWindowSeconds (integer) -- Time window (in seconds) contained in each manifest.
    MinBufferTimeSeconds (integer) -- Minimum duration (in seconds) that a player will buffer media before starting the presentation.
    MinUpdatePeriodSeconds (integer) -- Minimum duration (in seconds) between potential changes to the Dynamic Adaptive Streaming over HTTP (DASH) Media Presentation Description (MPD).
    Profile (string) -- The Dynamic Adaptive Streaming over HTTP (DASH) profile type. When set to "HBBTV_1_5", HbbTV 1.5 compliant output is enabled.
    SegmentDurationSeconds (integer) -- Duration (in seconds) of each segment. Actual segments will be rounded to the nearest multiple of the source segment duration.
    StreamSelection (dict) -- A StreamSelection configuration.
    MaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.
    MinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.
    StreamOrder (string) -- A directive that determines the order of streams in the output.
    
    
    SuggestedPresentationDelaySeconds (integer) -- Duration (in seconds) to delay live content before presentation.
    
    
    Description (string) -- A short text description of the OriginEndpoint.
    HlsPackage (dict) -- An HTTP Live Streaming (HLS) packaging configuration.
    AdMarkers (string) -- This setting controls how ad markers are included in the packaged OriginEndpoint. "NONE" will omit all SCTE-35 ad markers from the output. "PASSTHROUGH" causes the manifest to contain a copy of the SCTE-35 ad markers (comments) taken directly from the input HTTP Live Streaming (HLS) manifest. "SCTE35_ENHANCED" generates ad markers and blackout tags based on SCTE-35 messages in the input source.
    Encryption (dict) -- An HTTP Live Streaming (HLS) encryption configuration.
    ConstantInitializationVector (string) -- A constant initialization vector for encryption (optional). When not specified the initialization vector will be periodically rotated.
    EncryptionMethod (string) -- The encryption method to use.
    KeyRotationIntervalSeconds (integer) -- Interval (in seconds) between each encryption key rotation.
    RepeatExtXKey (boolean) -- When enabled, the EXT-X-KEY tag will be repeated in output manifests.
    SpekeKeyProvider (dict) -- A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
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
    
    
    
    
    StartoverWindowSeconds (integer) -- Maximum duration (seconds) of content to retain for startover playback. If not specified, startover playback will be disabled for the OriginEndpoint.
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
    
    
    :example: response = client.delete_channel(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED] The ID of the Channel to delete.

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_origin_endpoint(Id=None):
    """
    Deletes an existing OriginEndpoint.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_origin_endpoint(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED] The ID of the OriginEndpoint to delete.

    :rtype: dict
    :return: {}
    
    
    """
    pass

def describe_channel(Id=None):
    """
    Gets details about a Channel.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_channel(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED] The ID of a Channel.

    :rtype: dict
    :return: {
        'Arn': 'string',
        'Description': 'string',
        'HlsIngest': {
            'IngestEndpoints': [
                {
                    'Password': 'string',
                    'Url': 'string',
                    'Username': 'string'
                },
            ]
        },
        'Id': 'string'
    }
    
    
    """
    pass

def describe_origin_endpoint(Id=None):
    """
    Gets details about an existing OriginEndpoint.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_origin_endpoint(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED] The ID of the OriginEndpoint.

    :rtype: dict
    :return: {
        'Arn': 'string',
        'ChannelId': 'string',
        'CmafPackage': {
            'Encryption': {
                'KeyRotationIntervalSeconds': 123,
                'SpekeKeyProvider': {
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
            'Encryption': {
                'KeyRotationIntervalSeconds': 123,
                'SpekeKeyProvider': {
                    'ResourceId': 'string',
                    'RoleArn': 'string',
                    'SystemIds': [
                        'string',
                    ],
                    'Url': 'string'
                }
            },
            'ManifestWindowSeconds': 123,
            'MinBufferTimeSeconds': 123,
            'MinUpdatePeriodSeconds': 123,
            'Profile': 'NONE'|'HBBTV_1_5',
            'SegmentDurationSeconds': 123,
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
            'Encryption': {
                'ConstantInitializationVector': 'string',
                'EncryptionMethod': 'AES_128'|'SAMPLE_AES',
                'KeyRotationIntervalSeconds': 123,
                'RepeatExtXKey': True|False,
                'SpekeKeyProvider': {
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
        'StartoverWindowSeconds': 123,
        'TimeDelaySeconds': 123,
        'Url': 'string',
        'Whitelist': [
            'string',
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

def list_channels(MaxResults=None, NextToken=None):
    """
    Returns a collection of Channels.
    See also: AWS API Documentation
    
    
    :example: response = client.list_channels(
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: Upper bound on number of records to return.

    :type NextToken: string
    :param NextToken: A token used to resume pagination from the end of a previous request.

    :rtype: dict
    :return: {
        'Channels': [
            {
                'Arn': 'string',
                'Description': 'string',
                'HlsIngest': {
                    'IngestEndpoints': [
                        {
                            'Password': 'string',
                            'Url': 'string',
                            'Username': 'string'
                        },
                    ]
                },
                'Id': 'string'
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
    Password (string) -- The system generated password for ingest authentication.
    Url (string) -- The ingest URL to which the source stream should be sent.
    Username (string) -- The system generated username for ingest authentication.
    
    
    
    
    
    
    Id (string) -- The ID of the Channel.
    
    
    
    
    NextToken (string) -- A token that can be used to resume pagination from the end of the collection.
    
    
    
    """
    pass

def list_origin_endpoints(ChannelId=None, MaxResults=None, NextToken=None):
    """
    Returns a collection of OriginEndpoint records.
    See also: AWS API Documentation
    
    
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
    :return: {
        'NextToken': 'string',
        'OriginEndpoints': [
            {
                'Arn': 'string',
                'ChannelId': 'string',
                'CmafPackage': {
                    'Encryption': {
                        'KeyRotationIntervalSeconds': 123,
                        'SpekeKeyProvider': {
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
                    'Encryption': {
                        'KeyRotationIntervalSeconds': 123,
                        'SpekeKeyProvider': {
                            'ResourceId': 'string',
                            'RoleArn': 'string',
                            'SystemIds': [
                                'string',
                            ],
                            'Url': 'string'
                        }
                    },
                    'ManifestWindowSeconds': 123,
                    'MinBufferTimeSeconds': 123,
                    'MinUpdatePeriodSeconds': 123,
                    'Profile': 'NONE'|'HBBTV_1_5',
                    'SegmentDurationSeconds': 123,
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
                    'Encryption': {
                        'ConstantInitializationVector': 'string',
                        'EncryptionMethod': 'AES_128'|'SAMPLE_AES',
                        'KeyRotationIntervalSeconds': 123,
                        'RepeatExtXKey': True|False,
                        'SpekeKeyProvider': {
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
                'StartoverWindowSeconds': 123,
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
    ChannelId (string) -- The ID of the Channel the OriginEndpoint is associated with.
    CmafPackage (dict) -- A Common Media Application Format (CMAF) packaging configuration.
    Encryption (dict) -- A Common Media Application Format (CMAF) encryption configuration.
    KeyRotationIntervalSeconds (integer) -- Time (in seconds) between each encryption key rotation.
    SpekeKeyProvider (dict) -- A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
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
    Encryption (dict) -- A Dynamic Adaptive Streaming over HTTP (DASH) encryption configuration.
    KeyRotationIntervalSeconds (integer) -- Time (in seconds) between each encryption key rotation.
    SpekeKeyProvider (dict) -- A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
    ResourceId (string) -- The resource ID to include in key requests.
    RoleArn (string) -- An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.
    SystemIds (list) -- The system IDs to include in key requests.
    (string) --
    
    
    Url (string) -- The URL of the external key provider service.
    
    
    
    
    ManifestWindowSeconds (integer) -- Time window (in seconds) contained in each manifest.
    MinBufferTimeSeconds (integer) -- Minimum duration (in seconds) that a player will buffer media before starting the presentation.
    MinUpdatePeriodSeconds (integer) -- Minimum duration (in seconds) between potential changes to the Dynamic Adaptive Streaming over HTTP (DASH) Media Presentation Description (MPD).
    Profile (string) -- The Dynamic Adaptive Streaming over HTTP (DASH) profile type. When set to "HBBTV_1_5", HbbTV 1.5 compliant output is enabled.
    SegmentDurationSeconds (integer) -- Duration (in seconds) of each segment. Actual segments will be rounded to the nearest multiple of the source segment duration.
    StreamSelection (dict) -- A StreamSelection configuration.
    MaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.
    MinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.
    StreamOrder (string) -- A directive that determines the order of streams in the output.
    
    
    SuggestedPresentationDelaySeconds (integer) -- Duration (in seconds) to delay live content before presentation.
    
    
    Description (string) -- A short text description of the OriginEndpoint.
    HlsPackage (dict) -- An HTTP Live Streaming (HLS) packaging configuration.
    AdMarkers (string) -- This setting controls how ad markers are included in the packaged OriginEndpoint. "NONE" will omit all SCTE-35 ad markers from the output. "PASSTHROUGH" causes the manifest to contain a copy of the SCTE-35 ad markers (comments) taken directly from the input HTTP Live Streaming (HLS) manifest. "SCTE35_ENHANCED" generates ad markers and blackout tags based on SCTE-35 messages in the input source.
    Encryption (dict) -- An HTTP Live Streaming (HLS) encryption configuration.
    ConstantInitializationVector (string) -- A constant initialization vector for encryption (optional). When not specified the initialization vector will be periodically rotated.
    EncryptionMethod (string) -- The encryption method to use.
    KeyRotationIntervalSeconds (integer) -- Interval (in seconds) between each encryption key rotation.
    RepeatExtXKey (boolean) -- When enabled, the EXT-X-KEY tag will be repeated in output manifests.
    SpekeKeyProvider (dict) -- A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
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
    
    
    
    
    StartoverWindowSeconds (integer) -- Maximum duration (seconds) of content to retain for startover playback. If not specified, startover playback will be disabled for the OriginEndpoint.
    TimeDelaySeconds (integer) -- Amount of delay (seconds) to enforce on the playback of live content. If not specified, there will be no time delay in effect for the OriginEndpoint.
    Url (string) -- The URL of the packaged OriginEndpoint for consumption.
    Whitelist (list) -- A list of source IP CIDR blocks that will be allowed to access the OriginEndpoint.
    (string) --
    
    
    
    
    
    
    
    
    
    """
    pass

def rotate_channel_credentials(Id=None):
    """
    Changes the Channel ingest username and password.
    See also: AWS API Documentation
    
    
    :example: response = client.rotate_channel_credentials(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED] The ID of the channel to update.

    :rtype: dict
    :return: {
        'Arn': 'string',
        'Description': 'string',
        'HlsIngest': {
            'IngestEndpoints': [
                {
                    'Password': 'string',
                    'Url': 'string',
                    'Username': 'string'
                },
            ]
        },
        'Id': 'string'
    }
    
    
    """
    pass

def update_channel(Description=None, Id=None):
    """
    Updates an existing Channel.
    See also: AWS API Documentation
    
    
    :example: response = client.update_channel(
        Description='string',
        Id='string'
    )
    
    
    :type Description: string
    :param Description: A short text description of the Channel.

    :type Id: string
    :param Id: [REQUIRED] The ID of the Channel to update.

    :rtype: dict
    :return: {
        'Arn': 'string',
        'Description': 'string',
        'HlsIngest': {
            'IngestEndpoints': [
                {
                    'Password': 'string',
                    'Url': 'string',
                    'Username': 'string'
                },
            ]
        },
        'Id': 'string'
    }
    
    
    :returns: 
    (dict) -- The updated Channel record.
    Arn (string) -- The Amazon Resource Name (ARN) assigned to the Channel.
    Description (string) -- A short text description of the Channel.
    HlsIngest (dict) -- An HTTP Live Streaming (HLS) ingest resource configuration.
    IngestEndpoints (list) -- A list of endpoints to which the source stream should be sent.
    (dict) -- An endpoint for ingesting source content for a Channel.
    Password (string) -- The system generated password for ingest authentication.
    Url (string) -- The ingest URL to which the source stream should be sent.
    Username (string) -- The system generated username for ingest authentication.
    
    
    
    
    
    
    Id (string) -- The ID of the Channel.
    
    
    
    """
    pass

def update_origin_endpoint(CmafPackage=None, DashPackage=None, Description=None, HlsPackage=None, Id=None, ManifestName=None, MssPackage=None, StartoverWindowSeconds=None, TimeDelaySeconds=None, Whitelist=None):
    """
    Updates an existing OriginEndpoint.
    See also: AWS API Documentation
    
    
    :example: response = client.update_origin_endpoint(
        CmafPackage={
            'Encryption': {
                'KeyRotationIntervalSeconds': 123,
                'SpekeKeyProvider': {
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
            'Encryption': {
                'KeyRotationIntervalSeconds': 123,
                'SpekeKeyProvider': {
                    'ResourceId': 'string',
                    'RoleArn': 'string',
                    'SystemIds': [
                        'string',
                    ],
                    'Url': 'string'
                }
            },
            'ManifestWindowSeconds': 123,
            'MinBufferTimeSeconds': 123,
            'MinUpdatePeriodSeconds': 123,
            'Profile': 'NONE'|'HBBTV_1_5',
            'SegmentDurationSeconds': 123,
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
            'Encryption': {
                'ConstantInitializationVector': 'string',
                'EncryptionMethod': 'AES_128'|'SAMPLE_AES',
                'KeyRotationIntervalSeconds': 123,
                'RepeatExtXKey': True|False,
                'SpekeKeyProvider': {
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
        StartoverWindowSeconds=123,
        TimeDelaySeconds=123,
        Whitelist=[
            'string',
        ]
    )
    
    
    :type CmafPackage: dict
    :param CmafPackage: A Common Media Application Format (CMAF) packaging configuration.
            Encryption (dict) -- A Common Media Application Format (CMAF) encryption configuration.
            KeyRotationIntervalSeconds (integer) -- Time (in seconds) between each encryption key rotation.
            SpekeKeyProvider (dict) -- [REQUIRED] A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
            ResourceId (string) -- [REQUIRED] The resource ID to include in key requests.
            RoleArn (string) -- [REQUIRED] An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.
            SystemIds (list) -- [REQUIRED] The system IDs to include in key requests.
            (string) --
            Url (string) -- [REQUIRED] The URL of the external key provider service.
            
            HlsManifests (list) -- A list of HLS manifest configurations
            (dict) -- A HTTP Live Streaming (HLS) manifest configuration.
            AdMarkers (string) -- This setting controls how ad markers are included in the packaged OriginEndpoint. 'NONE' will omit all SCTE-35 ad markers from the output. 'PASSTHROUGH' causes the manifest to contain a copy of the SCTE-35 ad markers (comments) taken directly from the input HTTP Live Streaming (HLS) manifest. 'SCTE35_ENHANCED' generates ad markers and blackout tags based on SCTE-35 messages in the input source.
            Id (string) -- [REQUIRED] The ID of the manifest. The ID must be unique within the OriginEndpoint and it cannot be changed after it is created.
            IncludeIframeOnlyStream (boolean) -- When enabled, an I-Frame only stream will be included in the output.
            ManifestName (string) -- An optional short string appended to the end of the OriginEndpoint URL. If not specified, defaults to the manifestName for the OriginEndpoint.
            PlaylistType (string) -- The HTTP Live Streaming (HLS) playlist type. When either 'EVENT' or 'VOD' is specified, a corresponding EXT-X-PLAYLIST-TYPE entry will be included in the media playlist.
            PlaylistWindowSeconds (integer) -- Time window (in seconds) contained in each parent manifest.
            ProgramDateTimeIntervalSeconds (integer) -- The interval (in seconds) between each EXT-X-PROGRAM-DATE-TIME tag inserted into manifests. Additionally, when an interval is specified ID3Timed Metadata messages will be generated every 5 seconds using the ingest time of the content. If the interval is not specified, or set to 0, then no EXT-X-PROGRAM-DATE-TIME tags will be inserted into manifests and no ID3Timed Metadata messages will be generated. Note that irrespective of this parameter, if any ID3 Timed Metadata is found in HTTP Live Streaming (HLS) input, it will be passed through to HLS output.
            
            SegmentDurationSeconds (integer) -- Duration (in seconds) of each segment. Actual segments will be rounded to the nearest multiple of the source segment duration.
            SegmentPrefix (string) -- An optional custom string that is prepended to the name of each segment. If not specified, it defaults to the ChannelId.
            StreamSelection (dict) -- A StreamSelection configuration.
            MaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.
            MinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.
            StreamOrder (string) -- A directive that determines the order of streams in the output.
            

    :type DashPackage: dict
    :param DashPackage: A Dynamic Adaptive Streaming over HTTP (DASH) packaging configuration.
            Encryption (dict) -- A Dynamic Adaptive Streaming over HTTP (DASH) encryption configuration.
            KeyRotationIntervalSeconds (integer) -- Time (in seconds) between each encryption key rotation.
            SpekeKeyProvider (dict) -- [REQUIRED] A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
            ResourceId (string) -- [REQUIRED] The resource ID to include in key requests.
            RoleArn (string) -- [REQUIRED] An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.
            SystemIds (list) -- [REQUIRED] The system IDs to include in key requests.
            (string) --
            Url (string) -- [REQUIRED] The URL of the external key provider service.
            
            ManifestWindowSeconds (integer) -- Time window (in seconds) contained in each manifest.
            MinBufferTimeSeconds (integer) -- Minimum duration (in seconds) that a player will buffer media before starting the presentation.
            MinUpdatePeriodSeconds (integer) -- Minimum duration (in seconds) between potential changes to the Dynamic Adaptive Streaming over HTTP (DASH) Media Presentation Description (MPD).
            Profile (string) -- The Dynamic Adaptive Streaming over HTTP (DASH) profile type. When set to 'HBBTV_1_5', HbbTV 1.5 compliant output is enabled.
            SegmentDurationSeconds (integer) -- Duration (in seconds) of each segment. Actual segments will be rounded to the nearest multiple of the source segment duration.
            StreamSelection (dict) -- A StreamSelection configuration.
            MaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.
            MinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.
            StreamOrder (string) -- A directive that determines the order of streams in the output.
            SuggestedPresentationDelaySeconds (integer) -- Duration (in seconds) to delay live content before presentation.
            

    :type Description: string
    :param Description: A short text description of the OriginEndpoint.

    :type HlsPackage: dict
    :param HlsPackage: An HTTP Live Streaming (HLS) packaging configuration.
            AdMarkers (string) -- This setting controls how ad markers are included in the packaged OriginEndpoint. 'NONE' will omit all SCTE-35 ad markers from the output. 'PASSTHROUGH' causes the manifest to contain a copy of the SCTE-35 ad markers (comments) taken directly from the input HTTP Live Streaming (HLS) manifest. 'SCTE35_ENHANCED' generates ad markers and blackout tags based on SCTE-35 messages in the input source.
            Encryption (dict) -- An HTTP Live Streaming (HLS) encryption configuration.
            ConstantInitializationVector (string) -- A constant initialization vector for encryption (optional). When not specified the initialization vector will be periodically rotated.
            EncryptionMethod (string) -- The encryption method to use.
            KeyRotationIntervalSeconds (integer) -- Interval (in seconds) between each encryption key rotation.
            RepeatExtXKey (boolean) -- When enabled, the EXT-X-KEY tag will be repeated in output manifests.
            SpekeKeyProvider (dict) -- [REQUIRED] A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
            ResourceId (string) -- [REQUIRED] The resource ID to include in key requests.
            RoleArn (string) -- [REQUIRED] An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.
            SystemIds (list) -- [REQUIRED] The system IDs to include in key requests.
            (string) --
            Url (string) -- [REQUIRED] The URL of the external key provider service.
            
            IncludeIframeOnlyStream (boolean) -- When enabled, an I-Frame only stream will be included in the output.
            PlaylistType (string) -- The HTTP Live Streaming (HLS) playlist type. When either 'EVENT' or 'VOD' is specified, a corresponding EXT-X-PLAYLIST-TYPE entry will be included in the media playlist.
            PlaylistWindowSeconds (integer) -- Time window (in seconds) contained in each parent manifest.
            ProgramDateTimeIntervalSeconds (integer) -- The interval (in seconds) between each EXT-X-PROGRAM-DATE-TIME tag inserted into manifests. Additionally, when an interval is specified ID3Timed Metadata messages will be generated every 5 seconds using the ingest time of the content. If the interval is not specified, or set to 0, then no EXT-X-PROGRAM-DATE-TIME tags will be inserted into manifests and no ID3Timed Metadata messages will be generated. Note that irrespective of this parameter, if any ID3 Timed Metadata is found in HTTP Live Streaming (HLS) input, it will be passed through to HLS output.
            SegmentDurationSeconds (integer) -- Duration (in seconds) of each fragment. Actual fragments will be rounded to the nearest multiple of the source fragment duration.
            StreamSelection (dict) -- A StreamSelection configuration.
            MaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.
            MinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.
            StreamOrder (string) -- A directive that determines the order of streams in the output.
            UseAudioRenditionGroup (boolean) -- When enabled, audio streams will be placed in rendition groups in the output.
            

    :type Id: string
    :param Id: [REQUIRED] The ID of the OriginEndpoint to update.

    :type ManifestName: string
    :param ManifestName: A short string that will be appended to the end of the Endpoint URL.

    :type MssPackage: dict
    :param MssPackage: A Microsoft Smooth Streaming (MSS) packaging configuration.
            Encryption (dict) -- A Microsoft Smooth Streaming (MSS) encryption configuration.
            SpekeKeyProvider (dict) -- [REQUIRED] A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
            ResourceId (string) -- [REQUIRED] The resource ID to include in key requests.
            RoleArn (string) -- [REQUIRED] An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.
            SystemIds (list) -- [REQUIRED] The system IDs to include in key requests.
            (string) --
            Url (string) -- [REQUIRED] The URL of the external key provider service.
            
            ManifestWindowSeconds (integer) -- The time window (in seconds) contained in each manifest.
            SegmentDurationSeconds (integer) -- The duration (in seconds) of each segment.
            StreamSelection (dict) -- A StreamSelection configuration.
            MaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.
            MinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.
            StreamOrder (string) -- A directive that determines the order of streams in the output.
            

    :type StartoverWindowSeconds: integer
    :param StartoverWindowSeconds: Maximum duration (in seconds) of content to retain for startover playback. If not specified, startover playback will be disabled for the OriginEndpoint.

    :type TimeDelaySeconds: integer
    :param TimeDelaySeconds: Amount of delay (in seconds) to enforce on the playback of live content. If not specified, there will be no time delay in effect for the OriginEndpoint.

    :type Whitelist: list
    :param Whitelist: A list of source IP CIDR blocks that will be allowed to access the OriginEndpoint.
            (string) --
            

    :rtype: dict
    :return: {
        'Arn': 'string',
        'ChannelId': 'string',
        'CmafPackage': {
            'Encryption': {
                'KeyRotationIntervalSeconds': 123,
                'SpekeKeyProvider': {
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
            'Encryption': {
                'KeyRotationIntervalSeconds': 123,
                'SpekeKeyProvider': {
                    'ResourceId': 'string',
                    'RoleArn': 'string',
                    'SystemIds': [
                        'string',
                    ],
                    'Url': 'string'
                }
            },
            'ManifestWindowSeconds': 123,
            'MinBufferTimeSeconds': 123,
            'MinUpdatePeriodSeconds': 123,
            'Profile': 'NONE'|'HBBTV_1_5',
            'SegmentDurationSeconds': 123,
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
            'Encryption': {
                'ConstantInitializationVector': 'string',
                'EncryptionMethod': 'AES_128'|'SAMPLE_AES',
                'KeyRotationIntervalSeconds': 123,
                'RepeatExtXKey': True|False,
                'SpekeKeyProvider': {
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
        'StartoverWindowSeconds': 123,
        'TimeDelaySeconds': 123,
        'Url': 'string',
        'Whitelist': [
            'string',
        ]
    }
    
    
    :returns: 
    (dict) -- An updated OriginEndpoint record.
    Arn (string) -- The Amazon Resource Name (ARN) assigned to the OriginEndpoint.
    ChannelId (string) -- The ID of the Channel the OriginEndpoint is associated with.
    CmafPackage (dict) -- A Common Media Application Format (CMAF) packaging configuration.
    Encryption (dict) -- A Common Media Application Format (CMAF) encryption configuration.
    KeyRotationIntervalSeconds (integer) -- Time (in seconds) between each encryption key rotation.
    SpekeKeyProvider (dict) -- A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
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
    Encryption (dict) -- A Dynamic Adaptive Streaming over HTTP (DASH) encryption configuration.
    KeyRotationIntervalSeconds (integer) -- Time (in seconds) between each encryption key rotation.
    SpekeKeyProvider (dict) -- A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
    ResourceId (string) -- The resource ID to include in key requests.
    RoleArn (string) -- An Amazon Resource Name (ARN) of an IAM role that AWS Elemental MediaPackage will assume when accessing the key provider service.
    SystemIds (list) -- The system IDs to include in key requests.
    (string) --
    
    
    Url (string) -- The URL of the external key provider service.
    
    
    
    
    ManifestWindowSeconds (integer) -- Time window (in seconds) contained in each manifest.
    MinBufferTimeSeconds (integer) -- Minimum duration (in seconds) that a player will buffer media before starting the presentation.
    MinUpdatePeriodSeconds (integer) -- Minimum duration (in seconds) between potential changes to the Dynamic Adaptive Streaming over HTTP (DASH) Media Presentation Description (MPD).
    Profile (string) -- The Dynamic Adaptive Streaming over HTTP (DASH) profile type. When set to "HBBTV_1_5", HbbTV 1.5 compliant output is enabled.
    SegmentDurationSeconds (integer) -- Duration (in seconds) of each segment. Actual segments will be rounded to the nearest multiple of the source segment duration.
    StreamSelection (dict) -- A StreamSelection configuration.
    MaxVideoBitsPerSecond (integer) -- The maximum video bitrate (bps) to include in output.
    MinVideoBitsPerSecond (integer) -- The minimum video bitrate (bps) to include in output.
    StreamOrder (string) -- A directive that determines the order of streams in the output.
    
    
    SuggestedPresentationDelaySeconds (integer) -- Duration (in seconds) to delay live content before presentation.
    
    
    Description (string) -- A short text description of the OriginEndpoint.
    HlsPackage (dict) -- An HTTP Live Streaming (HLS) packaging configuration.
    AdMarkers (string) -- This setting controls how ad markers are included in the packaged OriginEndpoint. "NONE" will omit all SCTE-35 ad markers from the output. "PASSTHROUGH" causes the manifest to contain a copy of the SCTE-35 ad markers (comments) taken directly from the input HTTP Live Streaming (HLS) manifest. "SCTE35_ENHANCED" generates ad markers and blackout tags based on SCTE-35 messages in the input source.
    Encryption (dict) -- An HTTP Live Streaming (HLS) encryption configuration.
    ConstantInitializationVector (string) -- A constant initialization vector for encryption (optional). When not specified the initialization vector will be periodically rotated.
    EncryptionMethod (string) -- The encryption method to use.
    KeyRotationIntervalSeconds (integer) -- Interval (in seconds) between each encryption key rotation.
    RepeatExtXKey (boolean) -- When enabled, the EXT-X-KEY tag will be repeated in output manifests.
    SpekeKeyProvider (dict) -- A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.
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
    
    
    
    
    StartoverWindowSeconds (integer) -- Maximum duration (seconds) of content to retain for startover playback. If not specified, startover playback will be disabled for the OriginEndpoint.
    TimeDelaySeconds (integer) -- Amount of delay (seconds) to enforce on the playback of live content. If not specified, there will be no time delay in effect for the OriginEndpoint.
    Url (string) -- The URL of the packaged OriginEndpoint for consumption.
    Whitelist (list) -- A list of source IP CIDR blocks that will be allowed to access the OriginEndpoint.
    (string) --
    
    
    
    
    
    """
    pass

