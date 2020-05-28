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

def get_clip(StreamName=None, StreamARN=None, ClipFragmentSelector=None):
    """
    Downloads an MP4 file (clip) containing the archived, on-demand media from the specified video stream over the specified time range.
    Both the StreamName and the StreamARN parameters are optional, but you must specify either the StreamName or the StreamARN when invoking this API operation.
    As a prerequsite to using GetCLip API, you must obtain an endpoint using GetDataEndpoint , specifying GET_CLIP forthe APIName parameter.
    An Amazon Kinesis video stream has the following requirements for providing data through MP4:
    You can monitor the amount of outgoing data by monitoring the GetClip.OutgoingBytes Amazon CloudWatch metric. For information about using CloudWatch to monitor Kinesis Video Streams, see Monitoring Kinesis Video Streams . For pricing information, see Amazon Kinesis Video Streams Pricing and AWS Pricing . Charges for outgoing AWS data apply.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_clip(
        StreamName='string',
        StreamARN='string',
        ClipFragmentSelector={
            'FragmentSelectorType': 'PRODUCER_TIMESTAMP'|'SERVER_TIMESTAMP',
            'TimestampRange': {
                'StartTimestamp': datetime(2015, 1, 1),
                'EndTimestamp': datetime(2015, 1, 1)
            }
        }
    )
    
    
    :type StreamName: string
    :param StreamName: The name of the stream for which to retrieve the media clip.\nYou must specify either the StreamName or the StreamARN.\n

    :type StreamARN: string
    :param StreamARN: The Amazon Resource Name (ARN) of the stream for which to retrieve the media clip.\nYou must specify either the StreamName or the StreamARN.\n

    :type ClipFragmentSelector: dict
    :param ClipFragmentSelector: [REQUIRED]\nThe time range of the requested clip and the source of the timestamps.\n\nFragmentSelectorType (string) -- [REQUIRED]The origin of the timestamps to use (Server or Producer).\n\nTimestampRange (dict) -- [REQUIRED]The range of timestamps to return.\n\nStartTimestamp (datetime) -- [REQUIRED]The starting timestamp in the range of timestamps for which to return fragments.\nThis value is inclusive. Fragments that start before the StartTimestamp and continue past it are included in the session. If FragmentSelectorType is SERVER_TIMESTAMP , the StartTimestamp must be later than the stream head.\n\nEndTimestamp (datetime) -- [REQUIRED]The end of the timestamp range for the requested media.\nThis value must be within 3 hours of the specified StartTimestamp , and it must be later than the StartTimestamp value. If FragmentSelectorType for the request is SERVER_TIMESTAMP , this value must be in the past.\nThis value is inclusive. The EndTimestamp is compared to the (starting) timestamp of the fragment. Fragments that start before the EndTimestamp value and continue past it are included in the session.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ContentType': 'string',
    'Payload': StreamingBody()
}


Response Structure

(dict) --

ContentType (string) --
The content type of the media in the requested clip.

Payload (StreamingBody) --
Traditional MP4 file that contains the media clip from the specified video stream. The output will contain the first 100 MB or the first 200 fragments from the specified start timestamp. For more information, see Kinesis Video Streams Limits .







Exceptions

KinesisVideoArchivedMedia.Client.exceptions.ResourceNotFoundException
KinesisVideoArchivedMedia.Client.exceptions.InvalidArgumentException
KinesisVideoArchivedMedia.Client.exceptions.ClientLimitExceededException
KinesisVideoArchivedMedia.Client.exceptions.NotAuthorizedException
KinesisVideoArchivedMedia.Client.exceptions.UnsupportedStreamMediaTypeException
KinesisVideoArchivedMedia.Client.exceptions.MissingCodecPrivateDataException
KinesisVideoArchivedMedia.Client.exceptions.InvalidCodecPrivateDataException
KinesisVideoArchivedMedia.Client.exceptions.InvalidMediaFrameException
KinesisVideoArchivedMedia.Client.exceptions.NoDataRetentionException


    :return: {
        'ContentType': 'string',
        'Payload': StreamingBody()
    }
    
    
    :returns: 
    StreamName (string) -- The name of the stream for which to retrieve the media clip.
    You must specify either the StreamName or the StreamARN.
    
    StreamARN (string) -- The Amazon Resource Name (ARN) of the stream for which to retrieve the media clip.
    You must specify either the StreamName or the StreamARN.
    
    ClipFragmentSelector (dict) -- [REQUIRED]
    The time range of the requested clip and the source of the timestamps.
    
    FragmentSelectorType (string) -- [REQUIRED]The origin of the timestamps to use (Server or Producer).
    
    TimestampRange (dict) -- [REQUIRED]The range of timestamps to return.
    
    StartTimestamp (datetime) -- [REQUIRED]The starting timestamp in the range of timestamps for which to return fragments.
    This value is inclusive. Fragments that start before the StartTimestamp and continue past it are included in the session. If FragmentSelectorType is SERVER_TIMESTAMP , the StartTimestamp must be later than the stream head.
    
    EndTimestamp (datetime) -- [REQUIRED]The end of the timestamp range for the requested media.
    This value must be within 3 hours of the specified StartTimestamp , and it must be later than the StartTimestamp value. If FragmentSelectorType for the request is SERVER_TIMESTAMP , this value must be in the past.
    This value is inclusive. The EndTimestamp is compared to the (starting) timestamp of the fragment. Fragments that start before the EndTimestamp value and continue past it are included in the session.
    
    
    
    
    
    
    """
    pass

def get_dash_streaming_session_url(StreamName=None, StreamARN=None, PlaybackMode=None, DisplayFragmentTimestamp=None, DisplayFragmentNumber=None, DASHFragmentSelector=None, Expires=None, MaxManifestFragmentResults=None):
    """
    Retrieves an MPEG Dynamic Adaptive Streaming over HTTP (DASH) URL for the stream. You can then open the URL in a media player to view the stream contents.
    Both the StreamName and the StreamARN parameters are optional, but you must specify either the StreamName or the StreamARN when invoking this API operation.
    An Amazon Kinesis video stream has the following requirements for providing data through MPEG-DASH:
    The following procedure shows how to use MPEG-DASH with Kinesis Video Streams:
    You can monitor the amount of data that the media player consumes by monitoring the GetMP4MediaFragment.OutgoingBytes Amazon CloudWatch metric. For information about using CloudWatch to monitor Kinesis Video Streams, see Monitoring Kinesis Video Streams . For pricing information, see Amazon Kinesis Video Streams Pricing and AWS Pricing . Charges for both HLS sessions and outgoing AWS data apply.
    For more information about HLS, see HTTP Live Streaming on the Apple Developer site .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_dash_streaming_session_url(
        StreamName='string',
        StreamARN='string',
        PlaybackMode='LIVE'|'LIVE_REPLAY'|'ON_DEMAND',
        DisplayFragmentTimestamp='ALWAYS'|'NEVER',
        DisplayFragmentNumber='ALWAYS'|'NEVER',
        DASHFragmentSelector={
            'FragmentSelectorType': 'PRODUCER_TIMESTAMP'|'SERVER_TIMESTAMP',
            'TimestampRange': {
                'StartTimestamp': datetime(2015, 1, 1),
                'EndTimestamp': datetime(2015, 1, 1)
            }
        },
        Expires=123,
        MaxManifestFragmentResults=123
    )
    
    
    :type StreamName: string
    :param StreamName: The name of the stream for which to retrieve the MPEG-DASH manifest URL.\nYou must specify either the StreamName or the StreamARN .\n

    :type StreamARN: string
    :param StreamARN: The Amazon Resource Name (ARN) of the stream for which to retrieve the MPEG-DASH manifest URL.\nYou must specify either the StreamName or the StreamARN .\n

    :type PlaybackMode: string
    :param PlaybackMode: Whether to retrieve live, live replay, or archived, on-demand data.\nFeatures of the three types of sessions include the following:\n\n**LIVE ** : For sessions of this type, the MPEG-DASH manifest is continually updated with the latest fragments as they become available. We recommend that the media player retrieve a new manifest on a one-second interval. When this type of session is played in a media player, the user interface typically displays a 'live' notification, with no scrubber control for choosing the position in the playback window to display.\n\n\nNote\nIn LIVE mode, the newest available fragments are included in an MPEG-DASH manifest, even if there is a gap between fragments (that is, if a fragment is missing). A gap like this might cause a media player to halt or cause a jump in playback. In this mode, fragments are not added to the MPEG-DASH manifest if they are older than the newest fragment in the playlist. If the missing fragment becomes available after a subsequent fragment is added to the manifest, the older fragment is not added, and the gap is not filled.\n\n\n**LIVE_REPLAY ** : For sessions of this type, the MPEG-DASH manifest is updated similarly to how it is updated for LIVE mode except that it starts by including fragments from a given start time. Instead of fragments being added as they are ingested, fragments are added as the duration of the next fragment elapses. For example, if the fragments in the session are two seconds long, then a new fragment is added to the manifest every two seconds. This mode is useful to be able to start playback from when an event is detected and continue live streaming media that has not yet been ingested as of the time of the session creation. This mode is also useful to stream previously archived media without being limited by the 1,000 fragment limit in the ON_DEMAND mode.\n**ON_DEMAND ** : For sessions of this type, the MPEG-DASH manifest contains all the fragments for the session, up to the number that is specified in MaxMediaPlaylistFragmentResults . The manifest must be retrieved only once for each session. When this type of session is played in a media player, the user interface typically displays a scrubber control for choosing the position in the playback window to display.\n\nIn all playback modes, if FragmentSelectorType is PRODUCER_TIMESTAMP , and if there are multiple fragments with the same start timestamp, the fragment that has the larger fragment number (that is, the newer fragment) is included in the MPEG-DASH manifest. The other fragments are not included. Fragments that have different timestamps but have overlapping durations are still included in the MPEG-DASH manifest. This can lead to unexpected behavior in the media player.\nThe default is LIVE .\n

    :type DisplayFragmentTimestamp: string
    :param DisplayFragmentTimestamp: Per the MPEG-DASH specification, the wall-clock time of fragments in the manifest file can be derived using attributes in the manifest itself. However, typically, MPEG-DASH compatible media players do not properly handle gaps in the media timeline. Kinesis Video Streams adjusts the media timeline in the manifest file to enable playback of media with discontinuities. Therefore, the wall-clock time derived from the manifest file may be inaccurate. If DisplayFragmentTimestamp is set to ALWAYS , the accurate fragment timestamp is added to each S element in the manifest file with the attribute name \xe2\x80\x9ckvs:ts\xe2\x80\x9d. A custom MPEG-DASH media player is necessary to leverage this custom attribute.\nThe default value is NEVER . When DASHFragmentSelector is SERVER_TIMESTAMP , the timestamps will be the server start timestamps. Similarly, when DASHFragmentSelector is PRODUCER_TIMESTAMP , the timestamps will be the producer start timestamps.\n

    :type DisplayFragmentNumber: string
    :param DisplayFragmentNumber: Fragments are identified in the manifest file based on their sequence number in the session. If DisplayFragmentNumber is set to ALWAYS , the Kinesis Video Streams fragment number is added to each S element in the manifest file with the attribute name \xe2\x80\x9ckvs:fn\xe2\x80\x9d. These fragment numbers can be used for logging or for use with other APIs (e.g. GetMedia and GetMediaForFragmentList ). A custom MPEG-DASH media player is necessary to leverage these this custom attribute.\nThe default value is NEVER .\n

    :type DASHFragmentSelector: dict
    :param DASHFragmentSelector: The time range of the requested fragment and the source of the timestamps.\nThis parameter is required if PlaybackMode is ON_DEMAND or LIVE_REPLAY . This parameter is optional if PlaybackMode is LIVE . If PlaybackMode is LIVE , the FragmentSelectorType can be set, but the TimestampRange should not be set. If PlaybackMode is ON_DEMAND or LIVE_REPLAY , both FragmentSelectorType and TimestampRange must be set.\n\nFragmentSelectorType (string) --The source of the timestamps for the requested media.\nWhen FragmentSelectorType is set to PRODUCER_TIMESTAMP and GetDASHStreamingSessionURLInput$PlaybackMode is ON_DEMAND or LIVE_REPLAY , the first fragment ingested with a producer timestamp within the specified FragmentSelector$TimestampRange is included in the media playlist. In addition, the fragments with producer timestamps within the TimestampRange ingested immediately following the first fragment (up to the GetDASHStreamingSessionURLInput$MaxManifestFragmentResults value) are included.\nFragments that have duplicate producer timestamps are deduplicated. This means that if producers are producing a stream of fragments with producer timestamps that are approximately equal to the true clock time, the MPEG-DASH manifest will contain all of the fragments within the requested timestamp range. If some fragments are ingested within the same time range and very different points in time, only the oldest ingested collection of fragments are returned.\nWhen FragmentSelectorType is set to PRODUCER_TIMESTAMP and GetDASHStreamingSessionURLInput$PlaybackMode is LIVE , the producer timestamps are used in the MP4 fragments and for deduplication. But the most recently ingested fragments based on server timestamps are included in the MPEG-DASH manifest. This means that even if fragments ingested in the past have producer timestamps with values now, they are not included in the HLS media playlist.\nThe default is SERVER_TIMESTAMP .\n\nTimestampRange (dict) --The start and end of the timestamp range for the requested media.\nThis value should not be present if PlaybackType is LIVE .\n\nStartTimestamp (datetime) --The start of the timestamp range for the requested media.\nIf the DASHTimestampRange value is specified, the StartTimestamp value is required.\n\nNote\nThis value is inclusive. Fragments that start before the StartTimestamp and continue past it are included in the session. If FragmentSelectorType is SERVER_TIMESTAMP , the StartTimestamp must be later than the stream head.\n\n\nEndTimestamp (datetime) --The end of the timestamp range for the requested media. This value must be within 3 hours of the specified StartTimestamp , and it must be later than the StartTimestamp value.\nIf FragmentSelectorType for the request is SERVER_TIMESTAMP , this value must be in the past.\nThe EndTimestamp value is required for ON_DEMAND mode, but optional for LIVE_REPLAY mode. If the EndTimestamp is not set for LIVE_REPLAY mode then the session will continue to include newly ingested fragments until the session expires.\n\nNote\nThis value is inclusive. The EndTimestamp is compared to the (starting) timestamp of the fragment. Fragments that start before the EndTimestamp value and continue past it are included in the session.\n\n\n\n\n\n

    :type Expires: integer
    :param Expires: The time in seconds until the requested session expires. This value can be between 300 (5 minutes) and 43200 (12 hours).\nWhen a session expires, no new calls to GetDashManifest , GetMP4InitFragment , or GetMP4MediaFragment can be made for that session.\nThe default is 300 (5 minutes).\n

    :type MaxManifestFragmentResults: integer
    :param MaxManifestFragmentResults: The maximum number of fragments that are returned in the MPEG-DASH manifest.\nWhen the PlaybackMode is LIVE , the most recent fragments are returned up to this value. When the PlaybackMode is ON_DEMAND , the oldest fragments are returned, up to this maximum number.\nWhen there are a higher number of fragments available in a live MPEG-DASH manifest, video players often buffer content before starting playback. Increasing the buffer size increases the playback latency, but it decreases the likelihood that rebuffering will occur during playback. We recommend that a live MPEG-DASH manifest have a minimum of 3 fragments and a maximum of 10 fragments.\nThe default is 5 fragments if PlaybackMode is LIVE or LIVE_REPLAY , and 1,000 if PlaybackMode is ON_DEMAND .\nThe maximum value of 1,000 fragments corresponds to more than 16 minutes of video on streams with 1-second fragments, and more than 2 1/2 hours of video on streams with 10-second fragments.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'DASHStreamingSessionURL': 'string'
}


Response Structure

(dict) --

DASHStreamingSessionURL (string) --
The URL (containing the session token) that a media player can use to retrieve the MPEG-DASH manifest.







Exceptions

KinesisVideoArchivedMedia.Client.exceptions.ResourceNotFoundException
KinesisVideoArchivedMedia.Client.exceptions.InvalidArgumentException
KinesisVideoArchivedMedia.Client.exceptions.ClientLimitExceededException
KinesisVideoArchivedMedia.Client.exceptions.NotAuthorizedException
KinesisVideoArchivedMedia.Client.exceptions.UnsupportedStreamMediaTypeException
KinesisVideoArchivedMedia.Client.exceptions.NoDataRetentionException
KinesisVideoArchivedMedia.Client.exceptions.MissingCodecPrivateDataException
KinesisVideoArchivedMedia.Client.exceptions.InvalidCodecPrivateDataException


    :return: {
        'DASHStreamingSessionURL': 'string'
    }
    
    
    :returns: 
    Get an endpoint using GetDataEndpoint , specifying GET_DASH_STREAMING_SESSION_URL for the APIName parameter.
    Retrieve the MPEG-DASH URL using GetDASHStreamingSessionURL . Kinesis Video Streams creates an MPEG-DASH streaming session to be used for accessing content in a stream using the MPEG-DASH protocol. GetDASHStreamingSessionURL returns an authenticated URL (that includes an encrypted session token) for the session\'s MPEG-DASH manifest (the root resource needed for streaming with MPEG-DASH).
    
    """
    pass

def get_hls_streaming_session_url(StreamName=None, StreamARN=None, PlaybackMode=None, HLSFragmentSelector=None, ContainerFormat=None, DiscontinuityMode=None, DisplayFragmentTimestamp=None, Expires=None, MaxMediaPlaylistFragmentResults=None):
    """
    Retrieves an HTTP Live Streaming (HLS) URL for the stream. You can then open the URL in a browser or media player to view the stream contents.
    Both the StreamName and the StreamARN parameters are optional, but you must specify either the StreamName or the StreamARN when invoking this API operation.
    An Amazon Kinesis video stream has the following requirements for providing data through HLS:
    Kinesis Video Streams HLS sessions contain fragments in the fragmented MPEG-4 form (also called fMP4 or CMAF) or the MPEG-2 form (also called TS chunks, which the HLS specification also supports). For more information about HLS fragment types, see the HLS specification .
    The following procedure shows how to use HLS with Kinesis Video Streams:
    You can monitor the amount of data that the media player consumes by monitoring the GetMP4MediaFragment.OutgoingBytes Amazon CloudWatch metric. For information about using CloudWatch to monitor Kinesis Video Streams, see Monitoring Kinesis Video Streams . For pricing information, see Amazon Kinesis Video Streams Pricing and AWS Pricing . Charges for both HLS sessions and outgoing AWS data apply.
    For more information about HLS, see HTTP Live Streaming on the Apple Developer site .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_hls_streaming_session_url(
        StreamName='string',
        StreamARN='string',
        PlaybackMode='LIVE'|'LIVE_REPLAY'|'ON_DEMAND',
        HLSFragmentSelector={
            'FragmentSelectorType': 'PRODUCER_TIMESTAMP'|'SERVER_TIMESTAMP',
            'TimestampRange': {
                'StartTimestamp': datetime(2015, 1, 1),
                'EndTimestamp': datetime(2015, 1, 1)
            }
        },
        ContainerFormat='FRAGMENTED_MP4'|'MPEG_TS',
        DiscontinuityMode='ALWAYS'|'NEVER'|'ON_DISCONTINUITY',
        DisplayFragmentTimestamp='ALWAYS'|'NEVER',
        Expires=123,
        MaxMediaPlaylistFragmentResults=123
    )
    
    
    :type StreamName: string
    :param StreamName: The name of the stream for which to retrieve the HLS master playlist URL.\nYou must specify either the StreamName or the StreamARN .\n

    :type StreamARN: string
    :param StreamARN: The Amazon Resource Name (ARN) of the stream for which to retrieve the HLS master playlist URL.\nYou must specify either the StreamName or the StreamARN .\n

    :type PlaybackMode: string
    :param PlaybackMode: Whether to retrieve live, live replay, or archived, on-demand data.\nFeatures of the three types of sessions include the following:\n\n**LIVE ** : For sessions of this type, the HLS media playlist is continually updated with the latest fragments as they become available. We recommend that the media player retrieve a new playlist on a one-second interval. When this type of session is played in a media player, the user interface typically displays a 'live' notification, with no scrubber control for choosing the position in the playback window to display.\n\n\nNote\nIn LIVE mode, the newest available fragments are included in an HLS media playlist, even if there is a gap between fragments (that is, if a fragment is missing). A gap like this might cause a media player to halt or cause a jump in playback. In this mode, fragments are not added to the HLS media playlist if they are older than the newest fragment in the playlist. If the missing fragment becomes available after a subsequent fragment is added to the playlist, the older fragment is not added, and the gap is not filled.\n\n\n**LIVE_REPLAY ** : For sessions of this type, the HLS media playlist is updated similarly to how it is updated for LIVE mode except that it starts by including fragments from a given start time. Instead of fragments being added as they are ingested, fragments are added as the duration of the next fragment elapses. For example, if the fragments in the session are two seconds long, then a new fragment is added to the media playlist every two seconds. This mode is useful to be able to start playback from when an event is detected and continue live streaming media that has not yet been ingested as of the time of the session creation. This mode is also useful to stream previously archived media without being limited by the 1,000 fragment limit in the ON_DEMAND mode.\n**ON_DEMAND ** : For sessions of this type, the HLS media playlist contains all the fragments for the session, up to the number that is specified in MaxMediaPlaylistFragmentResults . The playlist must be retrieved only once for each session. When this type of session is played in a media player, the user interface typically displays a scrubber control for choosing the position in the playback window to display.\n\nIn all playback modes, if FragmentSelectorType is PRODUCER_TIMESTAMP , and if there are multiple fragments with the same start timestamp, the fragment that has the larger fragment number (that is, the newer fragment) is included in the HLS media playlist. The other fragments are not included. Fragments that have different timestamps but have overlapping durations are still included in the HLS media playlist. This can lead to unexpected behavior in the media player.\nThe default is LIVE .\n

    :type HLSFragmentSelector: dict
    :param HLSFragmentSelector: The time range of the requested fragment and the source of the timestamps.\nThis parameter is required if PlaybackMode is ON_DEMAND or LIVE_REPLAY . This parameter is optional if PlaybackMode is LIVE . If PlaybackMode is LIVE , the FragmentSelectorType can be set, but the TimestampRange should not be set. If PlaybackMode is ON_DEMAND or LIVE_REPLAY , both FragmentSelectorType and TimestampRange must be set.\n\nFragmentSelectorType (string) --The source of the timestamps for the requested media.\nWhen FragmentSelectorType is set to PRODUCER_TIMESTAMP and GetHLSStreamingSessionURLInput$PlaybackMode is ON_DEMAND or LIVE_REPLAY , the first fragment ingested with a producer timestamp within the specified FragmentSelector$TimestampRange is included in the media playlist. In addition, the fragments with producer timestamps within the TimestampRange ingested immediately following the first fragment (up to the GetHLSStreamingSessionURLInput$MaxMediaPlaylistFragmentResults value) are included.\nFragments that have duplicate producer timestamps are deduplicated. This means that if producers are producing a stream of fragments with producer timestamps that are approximately equal to the true clock time, the HLS media playlists will contain all of the fragments within the requested timestamp range. If some fragments are ingested within the same time range and very different points in time, only the oldest ingested collection of fragments are returned.\nWhen FragmentSelectorType is set to PRODUCER_TIMESTAMP and GetHLSStreamingSessionURLInput$PlaybackMode is LIVE , the producer timestamps are used in the MP4 fragments and for deduplication. But the most recently ingested fragments based on server timestamps are included in the HLS media playlist. This means that even if fragments ingested in the past have producer timestamps with values now, they are not included in the HLS media playlist.\nThe default is SERVER_TIMESTAMP .\n\nTimestampRange (dict) --The start and end of the timestamp range for the requested media.\nThis value should not be present if PlaybackType is LIVE .\n\nStartTimestamp (datetime) --The start of the timestamp range for the requested media.\nIf the HLSTimestampRange value is specified, the StartTimestamp value is required.\n\nNote\nThis value is inclusive. Fragments that start before the StartTimestamp and continue past it are included in the session. If FragmentSelectorType is SERVER_TIMESTAMP , the StartTimestamp must be later than the stream head.\n\n\nEndTimestamp (datetime) --The end of the timestamp range for the requested media. This value must be within 3 hours of the specified StartTimestamp , and it must be later than the StartTimestamp value.\nIf FragmentSelectorType for the request is SERVER_TIMESTAMP , this value must be in the past.\nThe EndTimestamp value is required for ON_DEMAND mode, but optional for LIVE_REPLAY mode. If the EndTimestamp is not set for LIVE_REPLAY mode then the session will continue to include newly ingested fragments until the session expires.\n\nNote\nThis value is inclusive. The EndTimestamp is compared to the (starting) timestamp of the fragment. Fragments that start before the EndTimestamp value and continue past it are included in the session.\n\n\n\n\n\n

    :type ContainerFormat: string
    :param ContainerFormat: Specifies which format should be used for packaging the media. Specifying the FRAGMENTED_MP4 container format packages the media into MP4 fragments (fMP4 or CMAF). This is the recommended packaging because there is minimal packaging overhead. The other container format option is MPEG_TS . HLS has supported MPEG TS chunks since it was released and is sometimes the only supported packaging on older HLS players. MPEG TS typically has a 5-25 percent packaging overhead. This means MPEG TS typically requires 5-25 percent more bandwidth and cost than fMP4.\nThe default is FRAGMENTED_MP4 .\n

    :type DiscontinuityMode: string
    :param DiscontinuityMode: Specifies when flags marking discontinuities between fragments are added to the media playlists.\nMedia players typically build a timeline of media content to play, based on the timestamps of each fragment. This means that if there is any overlap or gap between fragments (as is typical if HLSFragmentSelector is set to SERVER_TIMESTAMP ), the media player timeline will also have small gaps between fragments in some places, and will overwrite frames in other places. Gaps in the media player timeline can cause playback to stall and overlaps can cause playback to be jittery. When there are discontinuity flags between fragments, the media player is expected to reset the timeline, resulting in the next fragment being played immediately after the previous fragment.\nThe following modes are supported:\n\nALWAYS : a discontinuity marker is placed between every fragment in the HLS media playlist. It is recommended to use a value of ALWAYS if the fragment timestamps are not accurate.\nNEVER : no discontinuity markers are placed anywhere. It is recommended to use a value of NEVER to ensure the media player timeline most accurately maps to the producer timestamps.\nON_DISCONTIUNITY : a discontinuity marker is placed between fragments that have a gap or overlap of more than 50 milliseconds. For most playback scenarios, it is recommended to use a value of ON_DISCONTINUITY so that the media player timeline is only reset when there is a significant issue with the media timeline (e.g. a missing fragment).\n\nThe default is ALWAYS when HLSFragmentSelector is set to SERVER_TIMESTAMP , and NEVER when it is set to PRODUCER_TIMESTAMP .\n

    :type DisplayFragmentTimestamp: string
    :param DisplayFragmentTimestamp: Specifies when the fragment start timestamps should be included in the HLS media playlist. Typically, media players report the playhead position as a time relative to the start of the first fragment in the playback session. However, when the start timestamps are included in the HLS media playlist, some media players might report the current playhead as an absolute time based on the fragment timestamps. This can be useful for creating a playback experience that shows viewers the wall-clock time of the media.\nThe default is NEVER . When HLSFragmentSelector is SERVER_TIMESTAMP , the timestamps will be the server start timestamps. Similarly, when HLSFragmentSelector is PRODUCER_TIMESTAMP , the timestamps will be the producer start timestamps.\n

    :type Expires: integer
    :param Expires: The time in seconds until the requested session expires. This value can be between 300 (5 minutes) and 43200 (12 hours).\nWhen a session expires, no new calls to GetHLSMasterPlaylist , GetHLSMediaPlaylist , GetMP4InitFragment , GetMP4MediaFragment , or GetTSFragment can be made for that session.\nThe default is 300 (5 minutes).\n

    :type MaxMediaPlaylistFragmentResults: integer
    :param MaxMediaPlaylistFragmentResults: The maximum number of fragments that are returned in the HLS media playlists.\nWhen the PlaybackMode is LIVE , the most recent fragments are returned up to this value. When the PlaybackMode is ON_DEMAND , the oldest fragments are returned, up to this maximum number.\nWhen there are a higher number of fragments available in a live HLS media playlist, video players often buffer content before starting playback. Increasing the buffer size increases the playback latency, but it decreases the likelihood that rebuffering will occur during playback. We recommend that a live HLS media playlist have a minimum of 3 fragments and a maximum of 10 fragments.\nThe default is 5 fragments if PlaybackMode is LIVE or LIVE_REPLAY , and 1,000 if PlaybackMode is ON_DEMAND .\nThe maximum value of 1,000 fragments corresponds to more than 16 minutes of video on streams with 1-second fragments, and more than 2 1/2 hours of video on streams with 10-second fragments.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'HLSStreamingSessionURL': 'string'
}


Response Structure

(dict) --

HLSStreamingSessionURL (string) --
The URL (containing the session token) that a media player can use to retrieve the HLS master playlist.







Exceptions

KinesisVideoArchivedMedia.Client.exceptions.ResourceNotFoundException
KinesisVideoArchivedMedia.Client.exceptions.InvalidArgumentException
KinesisVideoArchivedMedia.Client.exceptions.ClientLimitExceededException
KinesisVideoArchivedMedia.Client.exceptions.NotAuthorizedException
KinesisVideoArchivedMedia.Client.exceptions.UnsupportedStreamMediaTypeException
KinesisVideoArchivedMedia.Client.exceptions.NoDataRetentionException
KinesisVideoArchivedMedia.Client.exceptions.MissingCodecPrivateDataException
KinesisVideoArchivedMedia.Client.exceptions.InvalidCodecPrivateDataException


    :return: {
        'HLSStreamingSessionURL': 'string'
    }
    
    
    :returns: 
    Get an endpoint using GetDataEndpoint , specifying GET_HLS_STREAMING_SESSION_URL for the APIName parameter.
    Retrieve the HLS URL using GetHLSStreamingSessionURL . Kinesis Video Streams creates an HLS streaming session to be used for accessing content in a stream using the HLS protocol. GetHLSStreamingSessionURL returns an authenticated URL (that includes an encrypted session token) for the session\'s HLS master playlist (the root resource needed for streaming with HLS).
    
    """
    pass

def get_media_for_fragment_list(StreamName=None, Fragments=None):
    """
    Gets media for a list of fragments (specified by fragment number) from the archived data in an Amazon Kinesis video stream.
    The following limits apply when using the GetMediaForFragmentList API:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_media_for_fragment_list(
        StreamName='string',
        Fragments=[
            'string',
        ]
    )
    
    
    :type StreamName: string
    :param StreamName: [REQUIRED]\nThe name of the stream from which to retrieve fragment media.\n

    :type Fragments: list
    :param Fragments: [REQUIRED]\nA list of the numbers of fragments for which to retrieve media. You retrieve these values with ListFragments .\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ContentType': 'string',
    'Payload': StreamingBody()
}


Response Structure

(dict) --

ContentType (string) --
The content type of the requested media.

Payload (StreamingBody) --
The payload that Kinesis Video Streams returns is a sequence of chunks from the specified stream. For information about the chunks, see PutMedia . The chunks that Kinesis Video Streams returns in the GetMediaForFragmentList call also include the following additional Matroska (MKV) tags:

AWS_KINESISVIDEO_FRAGMENT_NUMBER - Fragment number returned in the chunk.
AWS_KINESISVIDEO_SERVER_SIDE_TIMESTAMP - Server-side timestamp of the fragment.
AWS_KINESISVIDEO_PRODUCER_SIDE_TIMESTAMP - Producer-side timestamp of the fragment.

The following tags will be included if an exception occurs:

AWS_KINESISVIDEO_FRAGMENT_NUMBER - The number of the fragment that threw the exception
AWS_KINESISVIDEO_EXCEPTION_ERROR_CODE - The integer code of the exception
AWS_KINESISVIDEO_EXCEPTION_MESSAGE - A text description of the exception








Exceptions

KinesisVideoArchivedMedia.Client.exceptions.ResourceNotFoundException
KinesisVideoArchivedMedia.Client.exceptions.InvalidArgumentException
KinesisVideoArchivedMedia.Client.exceptions.ClientLimitExceededException
KinesisVideoArchivedMedia.Client.exceptions.NotAuthorizedException


    :return: {
        'ContentType': 'string',
        'Payload': StreamingBody()
    }
    
    
    :returns: 
    x-amz-ErrorType HTTP header \xe2\x80\x93 contains a more specific error type in addition to what the HTTP status code provides.
    x-amz-RequestId HTTP header \xe2\x80\x93 if you want to report an issue to AWS, the support team can better diagnose the problem if given the Request Id.
    
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

def list_fragments(StreamName=None, MaxResults=None, NextToken=None, FragmentSelector=None):
    """
    Returns a list of  Fragment objects from the specified stream and timestamp range within the archived data.
    Listing fragments is eventually consistent. This means that even if the producer receives an acknowledgment that a fragment is persisted, the result might not be returned immediately from a request to ListFragments . However, results are typically available in less than one second.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_fragments(
        StreamName='string',
        MaxResults=123,
        NextToken='string',
        FragmentSelector={
            'FragmentSelectorType': 'PRODUCER_TIMESTAMP'|'SERVER_TIMESTAMP',
            'TimestampRange': {
                'StartTimestamp': datetime(2015, 1, 1),
                'EndTimestamp': datetime(2015, 1, 1)
            }
        }
    )
    
    
    :type StreamName: string
    :param StreamName: [REQUIRED]\nThe name of the stream from which to retrieve a fragment list.\n

    :type MaxResults: integer
    :param MaxResults: The total number of fragments to return. If the total number of fragments available is more than the value specified in max-results , then a ListFragmentsOutput$NextToken is provided in the output that you can use to resume pagination.

    :type NextToken: string
    :param NextToken: A token to specify where to start paginating. This is the ListFragmentsOutput$NextToken from a previously truncated response.

    :type FragmentSelector: dict
    :param FragmentSelector: Describes the timestamp range and timestamp origin for the range of fragments to return.\n\nFragmentSelectorType (string) -- [REQUIRED]The origin of the timestamps to use (Server or Producer).\n\nTimestampRange (dict) -- [REQUIRED]The range of timestamps to return.\n\nStartTimestamp (datetime) -- [REQUIRED]The starting timestamp in the range of timestamps for which to return fragments.\n\nEndTimestamp (datetime) -- [REQUIRED]The ending timestamp in the range of timestamps for which to return fragments.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Fragments': [
        {
            'FragmentNumber': 'string',
            'FragmentSizeInBytes': 123,
            'ProducerTimestamp': datetime(2015, 1, 1),
            'ServerTimestamp': datetime(2015, 1, 1),
            'FragmentLengthInMilliseconds': 123
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Fragments (list) --
A list of archived  Fragment objects from the stream that meet the selector criteria. Results are in no specific order, even across pages.

(dict) --
Represents a segment of video or other time-delimited data.

FragmentNumber (string) --
The unique identifier of the fragment. This value monotonically increases based on the ingestion order.

FragmentSizeInBytes (integer) --
The total fragment size, including information about the fragment and contained media data.

ProducerTimestamp (datetime) --
The timestamp from the producer corresponding to the fragment.

ServerTimestamp (datetime) --
The timestamp from the AWS server corresponding to the fragment.

FragmentLengthInMilliseconds (integer) --
The playback duration or other time value associated with the fragment.





NextToken (string) --
If the returned list is truncated, the operation returns this token to use to retrieve the next page of results. This value is null when there are no more results to return.







Exceptions

KinesisVideoArchivedMedia.Client.exceptions.ResourceNotFoundException
KinesisVideoArchivedMedia.Client.exceptions.InvalidArgumentException
KinesisVideoArchivedMedia.Client.exceptions.ClientLimitExceededException
KinesisVideoArchivedMedia.Client.exceptions.NotAuthorizedException


    :return: {
        'Fragments': [
            {
                'FragmentNumber': 'string',
                'FragmentSizeInBytes': 123,
                'ProducerTimestamp': datetime(2015, 1, 1),
                'ServerTimestamp': datetime(2015, 1, 1),
                'FragmentLengthInMilliseconds': 123
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    StreamName (string) -- [REQUIRED]
    The name of the stream from which to retrieve a fragment list.
    
    MaxResults (integer) -- The total number of fragments to return. If the total number of fragments available is more than the value specified in max-results , then a  ListFragmentsOutput$NextToken is provided in the output that you can use to resume pagination.
    NextToken (string) -- A token to specify where to start paginating. This is the  ListFragmentsOutput$NextToken from a previously truncated response.
    FragmentSelector (dict) -- Describes the timestamp range and timestamp origin for the range of fragments to return.
    
    FragmentSelectorType (string) -- [REQUIRED]The origin of the timestamps to use (Server or Producer).
    
    TimestampRange (dict) -- [REQUIRED]The range of timestamps to return.
    
    StartTimestamp (datetime) -- [REQUIRED]The starting timestamp in the range of timestamps for which to return fragments.
    
    EndTimestamp (datetime) -- [REQUIRED]The ending timestamp in the range of timestamps for which to return fragments.
    
    
    
    
    
    
    """
    pass

