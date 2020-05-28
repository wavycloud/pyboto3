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

def delete_playback_configuration(Name=None):
    """
    Deletes the playback configuration for the specified name.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_playback_configuration(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe identifier for the playback configuration.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --The request was successful and there is no content in the response.





    :return: {}
    
    
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

def get_playback_configuration(Name=None):
    """
    Returns the playback configuration for the specified name.
    See also: AWS API Documentation
    
    
    :example: response = client.get_playback_configuration(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe identifier for the playback configuration.\n

    :rtype: dict
ReturnsResponse Syntax{
    'AdDecisionServerUrl': 'string',
    'AvailSuppression': {
        'Mode': 'OFF'|'BEHIND_LIVE_EDGE',
        'Value': 'string'
    },
    'CdnConfiguration': {
        'AdSegmentUrlPrefix': 'string',
        'ContentSegmentUrlPrefix': 'string'
    },
    'DashConfiguration': {
        'ManifestEndpointPrefix': 'string',
        'MpdLocation': 'string',
        'OriginManifestType': 'SINGLE_PERIOD'|'MULTI_PERIOD'
    },
    'HlsConfiguration': {
        'ManifestEndpointPrefix': 'string'
    },
    'LivePreRollConfiguration': {
        'AdDecisionServerUrl': 'string',
        'MaxDurationSeconds': 123
    },
    'Name': 'string',
    'PersonalizationThresholdSeconds': 123,
    'PlaybackConfigurationArn': 'string',
    'PlaybackEndpointPrefix': 'string',
    'SessionInitializationEndpointPrefix': 'string',
    'SlateAdUrl': 'string',
    'Tags': {
        'string': 'string'
    },
    'TranscodeProfileName': 'string',
    'VideoContentSourceUrl': 'string'
}


Response Structure

(dict) --Success.

AdDecisionServerUrl (string) --The URL for the ad decision server (ADS). This includes the specification of static parameters and placeholders for dynamic parameters. AWS Elemental MediaTailor substitutes player-specific and session-specific parameters as needed when calling the ADS. Alternately, for testing, you can provide a static VAST URL. The maximum length is 25,000 characters.

AvailSuppression (dict) --The configuration for Avail Suppression. Ad suppression can be used to turn off ad personalization in a long manifest, or if a viewer joins mid-break.

Mode (string) -- Sets the mode for avail suppression, also known as ad suppression. By default, ad suppression is off and all ad breaks are filled by MediaTailor with ads or slate.
Value (string) -- The avail suppression value is a live edge offset time in HH:MM:SS. MediaTailor won\'t fill ad breaks on or behind this time in the manifest lookback window.


CdnConfiguration (dict) --The configuration for using a content delivery network (CDN), like Amazon CloudFront, for content and ad segment management.

AdSegmentUrlPrefix (string) --A non-default content delivery network (CDN) to serve ad segments. By default, AWS Elemental MediaTailor uses Amazon CloudFront with default cache settings as its CDN for ad segments. To set up an alternate CDN, create a rule in your CDN for the following origin: ads.mediatailor.<region>.amazonaws.com. Then specify the rule\'s name in this AdSegmentUrlPrefix. When AWS Elemental MediaTailor serves a manifest, it reports your CDN as the source for ad segments.

ContentSegmentUrlPrefix (string) --A content delivery network (CDN) to cache content segments, so that content requests don\xe2\x80\x99t always have to go to the origin server. First, create a rule in your CDN for the content segment origin server. Then specify the rule\'s name in this ContentSegmentUrlPrefix. When AWS Elemental MediaTailor serves a manifest, it reports your CDN as the source for content segments.



DashConfiguration (dict) --The configuration for DASH content.

ManifestEndpointPrefix (string) --The URL generated by MediaTailor to initiate a playback session. The session uses server-side reporting. This setting is ignored in PUT operations.

MpdLocation (string) --The setting that controls whether MediaTailor includes the Location tag in DASH manifests. MediaTailor populates the Location tag with the URL for manifest update requests, to be used by players that don\'t support sticky redirects. Disable this if you have CDN routing rules set up for accessing MediaTailor manifests, and you are either using client-side reporting or your players support sticky HTTP redirects. Valid values are DISABLED and EMT_DEFAULT. The EMT_DEFAULT setting enables the inclusion of the tag and is the default value.

OriginManifestType (string) --The setting that controls whether MediaTailor handles manifests from the origin server as multi-period manifests or single-period manifests. If your origin server produces single-period manifests, set this to SINGLE_PERIOD. The default setting is MULTI_PERIOD. For multi-period manifests, omit this setting or set it to MULTI_PERIOD.



HlsConfiguration (dict) --The configuration for HLS content.

ManifestEndpointPrefix (string) --The URL that is used to initiate a playback session for devices that support Apple HLS. The session uses server-side reporting.



LivePreRollConfiguration (dict) --The configuration for pre-roll ad insertion.

AdDecisionServerUrl (string) --The URL for the ad decision server (ADS) for pre-roll ads. This includes the specification of static parameters and placeholders for dynamic parameters. AWS Elemental MediaTailor substitutes player-specific and session-specific parameters as needed when calling the ADS. Alternately, for testing, you can provide a static VAST URL. The maximum length is 25,000 characters.

MaxDurationSeconds (integer) -- The maximum allowed duration for the pre-roll ad avail. AWS Elemental MediaTailor won\'t play pre-roll ads to exceed this duration, regardless of the total duration of ads that the ADS returns.


Name (string) --The identifier for the playback configuration.

PersonalizationThresholdSeconds (integer) --The maximum duration of underfilled ad time (in seconds) allowed in an ad break.

PlaybackConfigurationArn (string) --The Amazon Resource Name (ARN) for the playback configuration.

PlaybackEndpointPrefix (string) --The URL that the player accesses to get a manifest from AWS Elemental MediaTailor. This session will use server-side reporting.

SessionInitializationEndpointPrefix (string) --The URL that the player uses to initialize a session that uses client-side reporting.

SlateAdUrl (string) --The URL for a high-quality video asset to transcode and use to fill in time that\'s not used by ads. AWS Elemental MediaTailor shows the slate to fill in gaps in media content. Configuring the slate is optional for non-VPAID playback configurations. For VPAID, the slate is required because MediaTailor provides it in the slots designated for dynamic ad content. The slate must be a high-quality asset that contains both audio and video.

Tags (dict) --The tags assigned to the playback configuration.

(string) --
(string) --




TranscodeProfileName (string) --The name that is used to associate this playback configuration with a custom transcode profile. This overrides the dynamic transcoding defaults of MediaTailor. Use this only if you have already set up custom profiles with the help of AWS Support.

VideoContentSourceUrl (string) --The URL prefix for the master playlist for the stream, minus the asset ID. The maximum length is 512 characters.







    :return: {
        'AdDecisionServerUrl': 'string',
        'AvailSuppression': {
            'Mode': 'OFF'|'BEHIND_LIVE_EDGE',
            'Value': 'string'
        },
        'CdnConfiguration': {
            'AdSegmentUrlPrefix': 'string',
            'ContentSegmentUrlPrefix': 'string'
        },
        'DashConfiguration': {
            'ManifestEndpointPrefix': 'string',
            'MpdLocation': 'string',
            'OriginManifestType': 'SINGLE_PERIOD'|'MULTI_PERIOD'
        },
        'HlsConfiguration': {
            'ManifestEndpointPrefix': 'string'
        },
        'LivePreRollConfiguration': {
            'AdDecisionServerUrl': 'string',
            'MaxDurationSeconds': 123
        },
        'Name': 'string',
        'PersonalizationThresholdSeconds': 123,
        'PlaybackConfigurationArn': 'string',
        'PlaybackEndpointPrefix': 'string',
        'SessionInitializationEndpointPrefix': 'string',
        'SlateAdUrl': 'string',
        'Tags': {
            'string': 'string'
        },
        'TranscodeProfileName': 'string',
        'VideoContentSourceUrl': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
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

def list_playback_configurations(MaxResults=None, NextToken=None):
    """
    Returns a list of the playback configurations defined in AWS Elemental MediaTailor. You can specify a maximum number of configurations to return at a time. The default maximum is 50. Results are returned in pagefuls. If MediaTailor has more configurations than the specified maximum, it provides parameters in the response that you can use to retrieve the next pageful.
    See also: AWS API Documentation
    
    
    :example: response = client.list_playback_configurations(
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: Maximum number of records to return.

    :type NextToken: string
    :param NextToken: Pagination token returned by the GET list request when results exceed the maximum allowed. Use the token to fetch the next page of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'Items': [
        {
            'AdDecisionServerUrl': 'string',
            'AvailSuppression': {
                'Mode': 'OFF'|'BEHIND_LIVE_EDGE',
                'Value': 'string'
            },
            'CdnConfiguration': {
                'AdSegmentUrlPrefix': 'string',
                'ContentSegmentUrlPrefix': 'string'
            },
            'DashConfiguration': {
                'ManifestEndpointPrefix': 'string',
                'MpdLocation': 'string',
                'OriginManifestType': 'SINGLE_PERIOD'|'MULTI_PERIOD'
            },
            'HlsConfiguration': {
                'ManifestEndpointPrefix': 'string'
            },
            'Name': 'string',
            'PlaybackConfigurationArn': 'string',
            'PlaybackEndpointPrefix': 'string',
            'SessionInitializationEndpointPrefix': 'string',
            'SlateAdUrl': 'string',
            'Tags': {
                'string': 'string'
            },
            'TranscodeProfileName': 'string',
            'PersonalizationThresholdSeconds': 123,
            'VideoContentSourceUrl': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
Success.

Items (list) --
Array of playback configurations. This might be all the available configurations or a subset, depending on the settings that you provide and the total number of configurations stored.

(dict) --
The AWSMediaTailor configuration.

AdDecisionServerUrl (string) --
The URL for the ad decision server (ADS). This includes the specification of static parameters and placeholders for dynamic parameters. AWS Elemental MediaTailor substitutes player-specific and session-specific parameters as needed when calling the ADS. Alternately, for testing, you can provide a static VAST URL. The maximum length is 25,000 characters.

AvailSuppression (dict) --
The configuration for Avail Suppression. Ad suppression can be used to turn off ad personalization in a long manifest, or if a viewer joins mid-break.

Mode (string) -- Sets the mode for avail suppression, also known as ad suppression. By default, ad suppression is off and all ad breaks are filled by MediaTailor with ads or slate.
Value (string) -- The avail suppression value is a live edge offset time in HH:MM:SS. MediaTailor won\'t fill ad breaks on or behind this time in the manifest lookback window.


CdnConfiguration (dict) --
The configuration for using a content delivery network (CDN), like Amazon CloudFront, for content and ad segment management.

AdSegmentUrlPrefix (string) --
A non-default content delivery network (CDN) to serve ad segments. By default, AWS Elemental MediaTailor uses Amazon CloudFront with default cache settings as its CDN for ad segments. To set up an alternate CDN, create a rule in your CDN for the following origin: ads.mediatailor.<region>.amazonaws.com. Then specify the rule\'s name in this AdSegmentUrlPrefix. When AWS Elemental MediaTailor serves a manifest, it reports your CDN as the source for ad segments.

ContentSegmentUrlPrefix (string) --
A content delivery network (CDN) to cache content segments, so that content requests don\xe2\x80\x99t always have to go to the origin server. First, create a rule in your CDN for the content segment origin server. Then specify the rule\'s name in this ContentSegmentUrlPrefix. When AWS Elemental MediaTailor serves a manifest, it reports your CDN as the source for content segments.



DashConfiguration (dict) --
The configuration for DASH content.

ManifestEndpointPrefix (string) --
The URL generated by MediaTailor to initiate a playback session. The session uses server-side reporting. This setting is ignored in PUT operations.

MpdLocation (string) --
The setting that controls whether MediaTailor includes the Location tag in DASH manifests. MediaTailor populates the Location tag with the URL for manifest update requests, to be used by players that don\'t support sticky redirects. Disable this if you have CDN routing rules set up for accessing MediaTailor manifests, and you are either using client-side reporting or your players support sticky HTTP redirects. Valid values are DISABLED and EMT_DEFAULT. The EMT_DEFAULT setting enables the inclusion of the tag and is the default value.

OriginManifestType (string) --
The setting that controls whether MediaTailor handles manifests from the origin server as multi-period manifests or single-period manifests. If your origin server produces single-period manifests, set this to SINGLE_PERIOD. The default setting is MULTI_PERIOD. For multi-period manifests, omit this setting or set it to MULTI_PERIOD.



HlsConfiguration (dict) --
The configuration for HLS content.

ManifestEndpointPrefix (string) --
The URL that is used to initiate a playback session for devices that support Apple HLS. The session uses server-side reporting.



Name (string) --
The identifier for the playback configuration.

PlaybackConfigurationArn (string) --
The Amazon Resource Name (ARN) for the playback configuration.

PlaybackEndpointPrefix (string) --
The URL that the player accesses to get a manifest from AWS Elemental MediaTailor. This session will use server-side reporting.

SessionInitializationEndpointPrefix (string) --
The URL that the player uses to initialize a session that uses client-side reporting.

SlateAdUrl (string) --
The URL for a high-quality video asset to transcode and use to fill in time that\'s not used by ads. AWS Elemental MediaTailor shows the slate to fill in gaps in media content. Configuring the slate is optional for non-VPAID playback configurations. For VPAID, the slate is required because MediaTailor provides it in the slots designated for dynamic ad content. The slate must be a high-quality asset that contains both audio and video.

Tags (dict) --
The tags assigned to the playback configuration.

(string) --
(string) --




TranscodeProfileName (string) --
The name that is used to associate this playback configuration with a custom transcode profile. This overrides the dynamic transcoding defaults of MediaTailor. Use this only if you have already set up custom profiles with the help of AWS Support.

PersonalizationThresholdSeconds (integer) --
The maximum duration of underfilled ad time (in seconds) allowed in an ad break.

VideoContentSourceUrl (string) --
The URL prefix for the master playlist for the stream, minus the asset ID. The maximum length is 512 characters.





NextToken (string) --
Pagination token returned by the GET list request when results exceed the maximum allowed. Use the token to fetch the next page of results.








    :return: {
        'Items': [
            {
                'AdDecisionServerUrl': 'string',
                'AvailSuppression': {
                    'Mode': 'OFF'|'BEHIND_LIVE_EDGE',
                    'Value': 'string'
                },
                'CdnConfiguration': {
                    'AdSegmentUrlPrefix': 'string',
                    'ContentSegmentUrlPrefix': 'string'
                },
                'DashConfiguration': {
                    'ManifestEndpointPrefix': 'string',
                    'MpdLocation': 'string',
                    'OriginManifestType': 'SINGLE_PERIOD'|'MULTI_PERIOD'
                },
                'HlsConfiguration': {
                    'ManifestEndpointPrefix': 'string'
                },
                'Name': 'string',
                'PlaybackConfigurationArn': 'string',
                'PlaybackEndpointPrefix': 'string',
                'SessionInitializationEndpointPrefix': 'string',
                'SlateAdUrl': 'string',
                'Tags': {
                    'string': 'string'
                },
                'TranscodeProfileName': 'string',
                'PersonalizationThresholdSeconds': 123,
                'VideoContentSourceUrl': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Mode (string) -- Sets the mode for avail suppression, also known as ad suppression. By default, ad suppression is off and all ad breaks are filled by MediaTailor with ads or slate.
    Value (string) -- The avail suppression value is a live edge offset time in HH:MM:SS. MediaTailor won\'t fill ad breaks on or behind this time in the manifest lookback window.
    
    """
    pass

def list_tags_for_resource(ResourceArn=None):
    """
    Returns a list of the tags assigned to the specified playback configuration resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        ResourceArn='string'
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) for the playback configuration. You can get this from the response to any playback configuration request.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --Success.

Tags (dict) --A comma-separated list of tag key:value pairs. For example: { "Key1": "Value1", "Key2": "Value2" }

(string) --
(string) --









Exceptions

MediaTailor.Client.exceptions.BadRequestException


    :return: {
        'Tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    MediaTailor.Client.exceptions.BadRequestException
    
    """
    pass

def put_playback_configuration(AdDecisionServerUrl=None, AvailSuppression=None, CdnConfiguration=None, DashConfiguration=None, LivePreRollConfiguration=None, Name=None, PersonalizationThresholdSeconds=None, SlateAdUrl=None, Tags=None, TranscodeProfileName=None, VideoContentSourceUrl=None):
    """
    Adds a new playback configuration to AWS Elemental MediaTailor.
    See also: AWS API Documentation
    
    
    :example: response = client.put_playback_configuration(
        AdDecisionServerUrl='string',
        AvailSuppression={
            'Mode': 'OFF'|'BEHIND_LIVE_EDGE',
            'Value': 'string'
        },
        CdnConfiguration={
            'AdSegmentUrlPrefix': 'string',
            'ContentSegmentUrlPrefix': 'string'
        },
        DashConfiguration={
            'MpdLocation': 'string',
            'OriginManifestType': 'SINGLE_PERIOD'|'MULTI_PERIOD'
        },
        LivePreRollConfiguration={
            'AdDecisionServerUrl': 'string',
            'MaxDurationSeconds': 123
        },
        Name='string',
        PersonalizationThresholdSeconds=123,
        SlateAdUrl='string',
        Tags={
            'string': 'string'
        },
        TranscodeProfileName='string',
        VideoContentSourceUrl='string'
    )
    
    
    :type AdDecisionServerUrl: string
    :param AdDecisionServerUrl: The URL for the ad decision server (ADS). This includes the specification of static parameters and placeholders for dynamic parameters. AWS Elemental MediaTailor substitutes player-specific and session-specific parameters as needed when calling the ADS. Alternately, for testing you can provide a static VAST URL. The maximum length is 25,000 characters.

    :type AvailSuppression: dict
    :param AvailSuppression: The configuration for Avail Suppression. Ad suppression can be used to turn off ad personalization in a long manifest, or if a viewer joins mid-break.\n\nMode (string) -- Sets the mode for avail suppression, also known as ad suppression. By default, ad suppression is off and all ad breaks are filled by MediaTailor with ads or slate.\nValue (string) -- The avail suppression value is a live edge offset time in HH:MM:SS. MediaTailor won\'t fill ad breaks on or behind this time in the manifest lookback window.\n\n

    :type CdnConfiguration: dict
    :param CdnConfiguration: The configuration for using a content delivery network (CDN), like Amazon CloudFront, for content and ad segment management.\n\nAdSegmentUrlPrefix (string) --A non-default content delivery network (CDN) to serve ad segments. By default, AWS Elemental MediaTailor uses Amazon CloudFront with default cache settings as its CDN for ad segments. To set up an alternate CDN, create a rule in your CDN for the following origin: ads.mediatailor.<region>.amazonaws.com. Then specify the rule\'s name in this AdSegmentUrlPrefix. When AWS Elemental MediaTailor serves a manifest, it reports your CDN as the source for ad segments.\n\nContentSegmentUrlPrefix (string) --A content delivery network (CDN) to cache content segments, so that content requests don\xe2\x80\x99t always have to go to the origin server. First, create a rule in your CDN for the content segment origin server. Then specify the rule\'s name in this ContentSegmentUrlPrefix. When AWS Elemental MediaTailor serves a manifest, it reports your CDN as the source for content segments.\n\n\n

    :type DashConfiguration: dict
    :param DashConfiguration: The configuration for DASH content.\n\nMpdLocation (string) --The setting that controls whether MediaTailor includes the Location tag in DASH manifests. MediaTailor populates the Location tag with the URL for manifest update requests, to be used by players that don\'t support sticky redirects. Disable this if you have CDN routing rules set up for accessing MediaTailor manifests, and you are either using client-side reporting or your players support sticky HTTP redirects. Valid values are DISABLED and EMT_DEFAULT. The EMT_DEFAULT setting enables the inclusion of the tag and is the default value.\n\nOriginManifestType (string) --The setting that controls whether MediaTailor handles manifests from the origin server as multi-period manifests or single-period manifests. If your origin server produces single-period manifests, set this to SINGLE_PERIOD. The default setting is MULTI_PERIOD. For multi-period manifests, omit this setting or set it to MULTI_PERIOD.\n\n\n

    :type LivePreRollConfiguration: dict
    :param LivePreRollConfiguration: The configuration for pre-roll ad insertion.\n\nAdDecisionServerUrl (string) --The URL for the ad decision server (ADS) for pre-roll ads. This includes the specification of static parameters and placeholders for dynamic parameters. AWS Elemental MediaTailor substitutes player-specific and session-specific parameters as needed when calling the ADS. Alternately, for testing, you can provide a static VAST URL. The maximum length is 25,000 characters.\n\nMaxDurationSeconds (integer) -- The maximum allowed duration for the pre-roll ad avail. AWS Elemental MediaTailor won\'t play pre-roll ads to exceed this duration, regardless of the total duration of ads that the ADS returns.\n\n

    :type Name: string
    :param Name: The identifier for the playback configuration.

    :type PersonalizationThresholdSeconds: integer
    :param PersonalizationThresholdSeconds: The maximum duration of underfilled ad time (in seconds) allowed in an ad break.

    :type SlateAdUrl: string
    :param SlateAdUrl: The URL for a high-quality video asset to transcode and use to fill in time that\'s not used by ads. AWS Elemental MediaTailor shows the slate to fill in gaps in media content. Configuring the slate is optional for non-VPAID configurations. For VPAID, the slate is required because MediaTailor provides it in the slots that are designated for dynamic ad content. The slate must be a high-quality asset that contains both audio and video.

    :type Tags: dict
    :param Tags: The tags to assign to the playback configuration.\n\n(string) --\n(string) --\n\n\n\n

    :type TranscodeProfileName: string
    :param TranscodeProfileName: The name that is used to associate this playback configuration with a custom transcode profile. This overrides the dynamic transcoding defaults of MediaTailor. Use this only if you have already set up custom profiles with the help of AWS Support.

    :type VideoContentSourceUrl: string
    :param VideoContentSourceUrl: The URL prefix for the master playlist for the stream, minus the asset ID. The maximum length is 512 characters.

    :rtype: dict

ReturnsResponse Syntax
{
    'AdDecisionServerUrl': 'string',
    'AvailSuppression': {
        'Mode': 'OFF'|'BEHIND_LIVE_EDGE',
        'Value': 'string'
    },
    'CdnConfiguration': {
        'AdSegmentUrlPrefix': 'string',
        'ContentSegmentUrlPrefix': 'string'
    },
    'DashConfiguration': {
        'ManifestEndpointPrefix': 'string',
        'MpdLocation': 'string',
        'OriginManifestType': 'SINGLE_PERIOD'|'MULTI_PERIOD'
    },
    'HlsConfiguration': {
        'ManifestEndpointPrefix': 'string'
    },
    'LivePreRollConfiguration': {
        'AdDecisionServerUrl': 'string',
        'MaxDurationSeconds': 123
    },
    'Name': 'string',
    'PersonalizationThresholdSeconds': 123,
    'PlaybackConfigurationArn': 'string',
    'PlaybackEndpointPrefix': 'string',
    'SessionInitializationEndpointPrefix': 'string',
    'SlateAdUrl': 'string',
    'Tags': {
        'string': 'string'
    },
    'TranscodeProfileName': 'string',
    'VideoContentSourceUrl': 'string'
}


Response Structure

(dict) --
Success.

AdDecisionServerUrl (string) --
The URL for the ad decision server (ADS). This includes the specification of static parameters and placeholders for dynamic parameters. AWS Elemental MediaTailor substitutes player-specific and session-specific parameters as needed when calling the ADS. Alternately, for testing, you can provide a static VAST URL. The maximum length is 25,000 characters.

AvailSuppression (dict) --
The configuration for Avail Suppression. Ad suppression can be used to turn off ad personalization in a long manifest, or if a viewer joins mid-break.

Mode (string) -- Sets the mode for avail suppression, also known as ad suppression. By default, ad suppression is off and all ad breaks are filled by MediaTailor with ads or slate.
Value (string) -- The avail suppression value is a live edge offset time in HH:MM:SS. MediaTailor won\'t fill ad breaks on or behind this time in the manifest lookback window.


CdnConfiguration (dict) --
The configuration for using a content delivery network (CDN), like Amazon CloudFront, for content and ad segment management.

AdSegmentUrlPrefix (string) --
A non-default content delivery network (CDN) to serve ad segments. By default, AWS Elemental MediaTailor uses Amazon CloudFront with default cache settings as its CDN for ad segments. To set up an alternate CDN, create a rule in your CDN for the following origin: ads.mediatailor.<region>.amazonaws.com. Then specify the rule\'s name in this AdSegmentUrlPrefix. When AWS Elemental MediaTailor serves a manifest, it reports your CDN as the source for ad segments.

ContentSegmentUrlPrefix (string) --
A content delivery network (CDN) to cache content segments, so that content requests don\xe2\x80\x99t always have to go to the origin server. First, create a rule in your CDN for the content segment origin server. Then specify the rule\'s name in this ContentSegmentUrlPrefix. When AWS Elemental MediaTailor serves a manifest, it reports your CDN as the source for content segments.



DashConfiguration (dict) --
The configuration for DASH content.

ManifestEndpointPrefix (string) --
The URL generated by MediaTailor to initiate a playback session. The session uses server-side reporting. This setting is ignored in PUT operations.

MpdLocation (string) --
The setting that controls whether MediaTailor includes the Location tag in DASH manifests. MediaTailor populates the Location tag with the URL for manifest update requests, to be used by players that don\'t support sticky redirects. Disable this if you have CDN routing rules set up for accessing MediaTailor manifests, and you are either using client-side reporting or your players support sticky HTTP redirects. Valid values are DISABLED and EMT_DEFAULT. The EMT_DEFAULT setting enables the inclusion of the tag and is the default value.

OriginManifestType (string) --
The setting that controls whether MediaTailor handles manifests from the origin server as multi-period manifests or single-period manifests. If your origin server produces single-period manifests, set this to SINGLE_PERIOD. The default setting is MULTI_PERIOD. For multi-period manifests, omit this setting or set it to MULTI_PERIOD.



HlsConfiguration (dict) --
The configuration for HLS content.

ManifestEndpointPrefix (string) --
The URL that is used to initiate a playback session for devices that support Apple HLS. The session uses server-side reporting.



LivePreRollConfiguration (dict) --
The configuration for pre-roll ad insertion.

AdDecisionServerUrl (string) --
The URL for the ad decision server (ADS) for pre-roll ads. This includes the specification of static parameters and placeholders for dynamic parameters. AWS Elemental MediaTailor substitutes player-specific and session-specific parameters as needed when calling the ADS. Alternately, for testing, you can provide a static VAST URL. The maximum length is 25,000 characters.

MaxDurationSeconds (integer) -- The maximum allowed duration for the pre-roll ad avail. AWS Elemental MediaTailor won\'t play pre-roll ads to exceed this duration, regardless of the total duration of ads that the ADS returns.



Name (string) --
The identifier for the playback configuration.

PersonalizationThresholdSeconds (integer) --
The maximum duration of underfilled ad time (in seconds) allowed in an ad break.

PlaybackConfigurationArn (string) --
The Amazon Resource Name (ARN) for the playback configuration.

PlaybackEndpointPrefix (string) --
The URL that the player accesses to get a manifest from AWS Elemental MediaTailor. This session will use server-side reporting.

SessionInitializationEndpointPrefix (string) --
The URL that the player uses to initialize a session that uses client-side reporting.

SlateAdUrl (string) --
The URL for a high-quality video asset to transcode and use to fill in time that\'s not used by ads. AWS Elemental MediaTailor shows the slate to fill in gaps in media content. Configuring the slate is optional for non-VPAID playback configurations. For VPAID, the slate is required because MediaTailor provides it in the slots designated for dynamic ad content. The slate must be a high-quality asset that contains both audio and video.

Tags (dict) --
The tags assigned to the playback configuration.

(string) --
(string) --




TranscodeProfileName (string) --
The name that is used to associate this playback configuration with a custom transcode profile. This overrides the dynamic transcoding defaults of MediaTailor. Use this only if you have already set up custom profiles with the help of AWS Support.

VideoContentSourceUrl (string) --
The URL prefix for the master playlist for the stream, minus the asset ID. The maximum length is 512 characters.








    :return: {
        'AdDecisionServerUrl': 'string',
        'AvailSuppression': {
            'Mode': 'OFF'|'BEHIND_LIVE_EDGE',
            'Value': 'string'
        },
        'CdnConfiguration': {
            'AdSegmentUrlPrefix': 'string',
            'ContentSegmentUrlPrefix': 'string'
        },
        'DashConfiguration': {
            'ManifestEndpointPrefix': 'string',
            'MpdLocation': 'string',
            'OriginManifestType': 'SINGLE_PERIOD'|'MULTI_PERIOD'
        },
        'HlsConfiguration': {
            'ManifestEndpointPrefix': 'string'
        },
        'LivePreRollConfiguration': {
            'AdDecisionServerUrl': 'string',
            'MaxDurationSeconds': 123
        },
        'Name': 'string',
        'PersonalizationThresholdSeconds': 123,
        'PlaybackConfigurationArn': 'string',
        'PlaybackEndpointPrefix': 'string',
        'SessionInitializationEndpointPrefix': 'string',
        'SlateAdUrl': 'string',
        'Tags': {
            'string': 'string'
        },
        'TranscodeProfileName': 'string',
        'VideoContentSourceUrl': 'string'
    }
    
    
    :returns: 
    Mode (string) -- Sets the mode for avail suppression, also known as ad suppression. By default, ad suppression is off and all ad breaks are filled by MediaTailor with ads or slate.
    Value (string) -- The avail suppression value is a live edge offset time in HH:MM:SS. MediaTailor won\'t fill ad breaks on or behind this time in the manifest lookback window.
    
    """
    pass

def tag_resource(ResourceArn=None, Tags=None):
    """
    Adds tags to the specified playback configuration resource. You can specify one or more tags to add.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        ResourceArn='string',
        Tags={
            'string': 'string'
        }
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) for the playback configuration. You can get this from the response to any playback configuration request.\n

    :type Tags: dict
    :param Tags: [REQUIRED]\nA comma-separated list of tag key:value pairs. For example: { 'Key1': 'Value1', 'Key2': 'Value2' }\n\n(string) --\n(string) --\n\n\n\n

    :returns: 
    MediaTailor.Client.exceptions.BadRequestException
    
    """
    pass

def untag_resource(ResourceArn=None, TagKeys=None):
    """
    Removes tags from the specified playback configuration resource. You can specify one or more tags to remove.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        ResourceArn='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) for the playback configuration. You can get this from the response to any playback configuration request.\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nA comma-separated list of the tag keys to remove from the playback configuration.\n\n(string) --\n\n

    :returns: 
    MediaTailor.Client.exceptions.BadRequestException
    
    """
    pass

